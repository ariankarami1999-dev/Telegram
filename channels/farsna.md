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
<img src="https://cdn4.telesco.pe/file/hJBRH9lDJyOGbC8Is5ZAGJ_QGXwnkWVkOleCh9R574s3MBNs1gNTq85WNP5SqWFMuhVzkzuCP283ERNJtgwgU_zixbaq66ifZSaXY8mD9vFMiDERmB2Rzfbsxk9gc5mUIUU9mKW8NLLENO0dZACWcDiQpfA5E28gakk86J96Y2Hh1abZM2rtVH1Nja35BtJ2-GiADNTHluZiVqFxZNh1lS8_RFcp0lvFWdlWY0vf1rvIrv_VT2KgljvbIyrxQEoXKfr1VWJ4c45KAR42PyQtuyBL_hxhO4nmk7ds7pnwn5HfSxB3gQGiuhfEo1-PXZXsE83ahS6V5DsD4mpJUqOwHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 01:20:48</div>
<hr>

<div class="tg-post" id="msg-461677">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حملۀ موشکی و پهپادی یمن به پایگاه نظامی عربستان سعودی
🔹
سرتیپ یحیی سریع، سخنگوی نیروهای مسلح یمن اعلام کرد که ارتش یمن انبارهای تسلیحات و اتاق‌های فرماندهی و کنترل مرتبط با تهاجم علیه یمن را در یک پایگاه نظامی در منطقه شروره عربستان سعودی هدف قرار داده‌ است.
🔹
این عملیات با شلیک شمار زیادی از موشک‌های بالستیک و پرتاب پهپادها انجام شده و اهداف مورد نظر با دقت و به‌صورت مستقیم مورد اصابت قرار گرفته‌اند.
🔹
این عملیات در واکنش به تداوم حملات و تجاوزات عربستان سعودی علیه یمن انجام شده است.
🔸
یحیی سریع تأکید کرد، به دشمن سعودی جنایتکار اعلام می‌کنیم که ادامۀ تجاوزاتش علیه مردم ما، با عملیات‌های قوی‌تر و گسترده‌تری در اعماق خاک آن کشور مواجه خواهد شد و عواقب وخیمی را برای او به همراه خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 990 · <a href="https://t.me/farsna/461677" target="_blank">📅 01:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461676">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2y4gaTwbiusGPl1w1b0zeofzm5qDIhqUYve3Ept7gGR_KWN7EYIgEOS1qYVvGplVDSrf8eBJ2pbL_EZDCFkEmtzkVNDDHIcjkTRD9LN9WNIU1hFhWpCMDOYGjQ4yKhFMyAt_QYfVxE68rl5amCxIZUnxjU_mmHGl2XbUKDTYX5ynUCOPb2cxjahclKuGwneBITzhuNMmRAI0nFAEE1kTMZn6ZDXeZmWvbIwKioO6hIGJX0pGwylKZ9NDgeAe0BETycjB-gkJX742_7KtcR9g_Cqq9tqW8hyFJ7SDC5XtoRyE5FG9na0T9Q-QqySJVomH5EqampZfJ86jaMTUzQ-Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: مردم ما را نمی‌توان با زور و تهدید وادار به تسلیم کرد؛ ایران تسلیم نخواهد شد
🔹
اگر آمریکایی‌ها جنگ‌طلب هستند، باید با نیروهای نظامی شجاع ما روبرو شوند؛ چرا علیه زیرساخت‌های غیرنظامی، منابع غذایی و معیشت مردم جنگ به راه انداخته‌اند؟
🔹
اگر آنها انسان هستند، چرا مردم را از دسترسی به آب، غذا و دارو محروم می‌کنند؟
@Farsna</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/farsna/461676" target="_blank">📅 01:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461675">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دفتر سقاب: ادعای بلاگر اقتصادی دربارهٔ شهید رئیسی کذب است
🔹
مدیر حوزهٔ ریاست در ستاد تحول دولت شهید رئیسی، در واکنش به اظهارات یک بلاگر اقتصادی گفت: او را نمی‌شناسم و اسمش را هم نشنیده بودم و تمامی اظهارات وی دربارهٔ دعوت به ستاد راهبری تحول دولت و یا تهیه…</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/farsna/461675" target="_blank">📅 00:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461674">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c398ca191.mp4?token=Ej6CwXDKXYSbxYZDMIFqx2ggZqVnlzGIwM5OxzTpo8mOYzgEfKPAGqz6BWPsAR0ces3j2_uVvxdF2z3RZBalY-biI1AGCkAk11qoH7bQxO3YkjhHX1r9fXXVXNXKuN9MipEDqGvSyna9-aMYzKLsurDwIfukruRRB3dLkTHFG11WDp-ZEofxON4Udkzxy0sm-XZZMgeKCyOCPU1e-vC_gH-Oah3hImhwD_LyHFkWXKbIRZGLqVXEzzqeK4iMPFNXKOy6ThB3oc00iFXkY305EHIr-i6mYy3IthSkvjr5HAtx6FvDTsuHvGprLW-zrI9rx04KjyvSjxOv8Fe2gQmplQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c398ca191.mp4?token=Ej6CwXDKXYSbxYZDMIFqx2ggZqVnlzGIwM5OxzTpo8mOYzgEfKPAGqz6BWPsAR0ces3j2_uVvxdF2z3RZBalY-biI1AGCkAk11qoH7bQxO3YkjhHX1r9fXXVXNXKuN9MipEDqGvSyna9-aMYzKLsurDwIfukruRRB3dLkTHFG11WDp-ZEofxON4Udkzxy0sm-XZZMgeKCyOCPU1e-vC_gH-Oah3hImhwD_LyHFkWXKbIRZGLqVXEzzqeK4iMPFNXKOy6ThB3oc00iFXkY305EHIr-i6mYy3IthSkvjr5HAtx6FvDTsuHvGprLW-zrI9rx04KjyvSjxOv8Fe2gQmplQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال اهالی صنعاء از ۲۱۰ اسیری که سال‌ها در زندان المخا در اسارت بودند.
@Farsna</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/farsna/461674" target="_blank">📅 00:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461673">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tt2CGFZauX0tpX6pdzzIfD_2W4fCBfcP8JJ-y_VY6awQ7nSzTJA-3iWTaBHjQEHOrN5amjI6AycKD89thm4uxq26GczKVVe1S3SaLrFhHgvatzWPmnqJ3Ylm-UngW54Scx6oqRQ2GhR2xfl8O4AInUtgVQw1OKVDf6K3__N7N1MWFdSWPvl3qOnunKdbSFYRcpHdYoUobVfNsKxWk1Cnsh3wvEHxgThbreahdRBqEBaE2qb5yPQvIHm3vQl1DGxtBJz7yGrycVjWNGfVuLPIHrPEKKuyz_V2v31_B3g5tb166qzlV3L1sReGdaEat0VEa4SolBUevd-mN2qe6WXKXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز نخستین روز ماه ربیع‌الثانی است
🔹
بر اساس گزارش ستاد استهلال دفتر مقام معظم رهبری، ماه ربیع‌الاول ۳۰ روزه بوده و یکشنبه ۲۲ شهریور آغاز ماه ربیع‌الثانی خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/461673" target="_blank">📅 00:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461672">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31de2b1af9.mp4?token=LWkxNuB8lI9VokRsHuv-lV5GCmtTO7BDOL7Vl94M0tcBW0GFe_w0KZLad3KtTuZqvsmCRmc-ApfojvQBHQB-2CO1XNg4LMIkkH7EZCID6iPSUrMPTM65-Fbwwu-0PaatzTIhEyLghKmjT0F9qpXprvTNbQHzQ5q1Ef7VBEz_d4Gl4SOKGFP67QqqfM_oQuP5EAENVdfQ8w97ud8PBPLF641uDBJIlWJ0fW_2Cp8SV3OHyfrrZNu2PjNJieCTINPwpOpBACm3ESO8S0E3Y4UqhIxtOocBBPTdrf_3Rk7jMCVeXeQ32jC36_M2U7L4dw9k4RoDm9H7hreXKNBgecqxhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31de2b1af9.mp4?token=LWkxNuB8lI9VokRsHuv-lV5GCmtTO7BDOL7Vl94M0tcBW0GFe_w0KZLad3KtTuZqvsmCRmc-ApfojvQBHQB-2CO1XNg4LMIkkH7EZCID6iPSUrMPTM65-Fbwwu-0PaatzTIhEyLghKmjT0F9qpXprvTNbQHzQ5q1Ef7VBEz_d4Gl4SOKGFP67QqqfM_oQuP5EAENVdfQ8w97ud8PBPLF641uDBJIlWJ0fW_2Cp8SV3OHyfrrZNu2PjNJieCTINPwpOpBACm3ESO8S0E3Y4UqhIxtOocBBPTdrf_3Rk7jMCVeXeQ32jC36_M2U7L4dw9k4RoDm9H7hreXKNBgecqxhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای حرم مطهر رضوی و مزار رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/farsna/461672" target="_blank">📅 00:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461664">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6nzFXZwUnlb8F0pKhobzB0AsVY098Ec2cQk52wr8CzenRo3V2a-TbRUxkeLq840BhukabhX66VYqpk7LF1lB2jDx0_55gpHNdLqLHjDV3VNXhfwcOyfbm-bQ860GWiJM-cBNoYxY168ZTjpiPL9ROBzvD9VtoUeVQHS2Ch0hctTO6bKc5PqVk63JgGaor2V4AxL2mwqV--40-mL-p_QNFKg4110uAvngA8cF6pkbevGLvsI76RggE1bjWIcWT5zYnpXSEZsbLIVdQjfma3u0tqapmSbro6ykFY4-XZZXWyZnCgj1YNaaVWbK5ROT_I20JTiVHzto99avsit-43MTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CS5iNOtqoIH4pLQkzGguXVgtsr5oTlrcYkVLwY7eF6OIA__Hdspz088gjr1uxgIUzrwH3yw9cibk8-3nmVDlVrH8ON-RYAs6_hq_JZGu3gZLmfmNayqYqggSurwTWaOSz9gtg_t0DeNXONHpAko8_Sf3ixReFd3KCP6HM-fVF8yCgnEjKFuKsJMupw-7G_MRO5HAxpK4tbHF9ZXmePTvaLYBnbACy1OYLFru1fpmMho4SXjooMrK9z1LNTs6HvUvRQbdrtEnRev7w_pS0-fj1ujfRdDjpqVIvGSbcWmkZLUxZcO2_iWh3YPfLHEC0hv9aX121uOTppotp8oMrD27Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PsGgxzx3vsYL0UHIRiCaml0837RLEpRa0MdDw1JnFbFMZyDPRWJ1VEZKyI2SR34RMGjkZL1IvKJJ7JIKJlkBk1GyQ4Ps9X-apiVLoqAA3voPnHWV8tFTquXmjgWxoHIMegBfKui9eHxywoXmI5QdT2hevOGWa3r-mIcu6kygRMX7TiiZE-YZyOtIZNzBp9Dlxt6nYptauIMlRVunK39x8WbnFtlxN3w6L_9xUKfRhQZ7t6jDI8DszFvWi_ZHSmafFrECDpmcsnrzpGoEV-d0MtZqnZjVibU-UG0dkC_H-HfXsmlt3NupQheFPS07v1IMVvnRh_9_dHtNox2mOu-SkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gBoetHa08rK9nNpjKj9S0AXvtM5NDz9O-PWwPUOxB_t6DK2Zj3hNnXFIIr11FcylL8yrZL61R_hM6rwIm6bb68waayCQ33-X3mEy92JDExXPlC9Tq7kndaNMjCDewETfSUyjGsec74pZQg-qblWIYOaG2XGwTzatyiCVs7COcNcoxTWLCElaAzm7R_PNDrhW1-BslunORBl_ZXybCndClWUXp1E92_UDemZht10jWAFAsIYmFVevLH3LYEFSXONCHbfJc-Q2O11hLxN5rKKD_nNagMd_Fxa2WvJyts93d1v5SjV0YqQEpkZnMvF8bq-WUalXFm97BUsdDWbPad62iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j-Huh4Iy-eU7woQgaiCwbbQYFsphD67OefV0shRhWYiHtA1LokOFo_OHooHwERw4GCcwiLjpgjbiisKik5RejxGJ-BjEUM9VdJbqBimNezQdpII2SsHZl9suPoVfFYOIeAIvpzWgihslDD3qX98bzfPU4X2Nkcb6tm13TLHPdUnXVlSGX0jBCOMg9blYVBOVv0fBmm_5dMZo3eamzD0z9ghjZKqjcWLW_jPwcIKvApZlWEvX8EqQQnT4g8Cu_Tu28uIP-X9YaNP9b0yceRikw_tQqSX-Y4QPqWttXQsTzkRY2GAK4CFEhiM0XtVjuvNuTiFP52OSgdroP-XY6CUhCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KJwHqkW1oXtryx1jPylLGJq4WqKB7ybkroLdVdPfmTRNxZ4Ngn67oPDrJv5VaBwIS_aLqI2tAcqDiVCfs1TMC0vBY22olH4TIE1UgHSvOGVqH9EbIk_3pFopJ9nRh4oEctVW-VY_RLKuGhbaKoS7IXpBe7hFB5mbiSB85-Gjmwu23PRgS2f_jT3cwFuCvvdBv0bmQjqJLhuqgkzetACfjK_E6lgjMrmD8tChn3kdpjzyE20XzdnC6nwGIR5pp7zwQ--y1Lr76wKeecrSX0SYBVtdzmf3uNxnR85AhqerMd3ZaHU21COTd2ukJln4wnfc8r2hGxpy3kL3d2-UujMMfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bNOeZloOmrvUotu_zPrR0VPgS6kNXO8OuT6VRE6bTi_ITeKKySIi9puD4ETpz2TESnR-s39Wz3W2IWPCnOdvVsNoHOtEARc6LNZZjv1qu7Tb7A5zx17OgiPKHhWXa9tTcIRBKD8HqHvTq1pnflpP63lk6TYhbt_RFRvVKZoVlPJcTrsDz8zSXUIFO526bWEjvRN3n9a23PsuwKWo6Hiszasjavn2JY9CF40epLg-qWtHFtjEgSOWZevMB1i0fF8kLpG1KkISuLiUhB0m37td_wApjdp-QJOQYGu7s3s0FF0kG6XAWiozauelokfPpvIyijbOP0mbZH-sN-SBP6bYGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85060ad79.mp4?token=pjrXhjdbfh0HgWib3khjJf5p8hLbcxkCp6lxBxMQ0lg7-PhHVacYZmTjcVt09lsf990pw45s8Z5RIcJGhK8nIpPFx0G5c8hKNZycFQRCN7wnzCjcdSJKS5WsHTd_ggn1zF1gOlx3Ew3Sl3xfCMEZpxwxCQkNKCZDtpCZD8uTYiHZYNeyPKlpuLwuV8jWwzvVnUztPMmSOM5whqIeuMPJnCwQbd9Sove_kndCNm5BgDp0CZRIB8desN7x5m-EC9Aw1m6DmjRb8kdwhJc5nt06Xs6E71NsUUmjkusIlsu9sKgbB4RjZi4SdF0feaV3sFDKpazDJk-vns51KyDQpfje563Z2nq4pkW9nbw5Bg8tTkvS2hOdl0yEmO4GbOWqy107mFjqOwkY9d2x5oM6yf2kk05m-iVGapVKwHozjdK3ho2Gv1G72jdhBl6grrA1zNW-X70bxzsEvu94WJqnab3NWcWC4ciSMJpeug1m5-GV1VqVWsg_nJu5mJR7NTvzLKx2Pq6nA-RTn4orHuBCIIcg6hhc2Wtuc_t6AxbTVYln9mSlhU2qPuMfaO9tQDuskuikrofUEw-j0ozbj51YnWKLPc5MOFNFfqSKVXLRKD6P3amEQFAAMcaEEYlWLY86CWAC-iUsmpFWUv3o2QdL-L9Yr6r0Pa0oE3MALZrq9TIGIkY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85060ad79.mp4?token=pjrXhjdbfh0HgWib3khjJf5p8hLbcxkCp6lxBxMQ0lg7-PhHVacYZmTjcVt09lsf990pw45s8Z5RIcJGhK8nIpPFx0G5c8hKNZycFQRCN7wnzCjcdSJKS5WsHTd_ggn1zF1gOlx3Ew3Sl3xfCMEZpxwxCQkNKCZDtpCZD8uTYiHZYNeyPKlpuLwuV8jWwzvVnUztPMmSOM5whqIeuMPJnCwQbd9Sove_kndCNm5BgDp0CZRIB8desN7x5m-EC9Aw1m6DmjRb8kdwhJc5nt06Xs6E71NsUUmjkusIlsu9sKgbB4RjZi4SdF0feaV3sFDKpazDJk-vns51KyDQpfje563Z2nq4pkW9nbw5Bg8tTkvS2hOdl0yEmO4GbOWqy107mFjqOwkY9d2x5oM6yf2kk05m-iVGapVKwHozjdK3ho2Gv1G72jdhBl6grrA1zNW-X70bxzsEvu94WJqnab3NWcWC4ciSMJpeug1m5-GV1VqVWsg_nJu5mJR7NTvzLKx2Pq6nA-RTn4orHuBCIIcg6hhc2Wtuc_t6AxbTVYln9mSlhU2qPuMfaO9tQDuskuikrofUEw-j0ozbj51YnWKLPc5MOFNFfqSKVXLRKD6P3amEQFAAMcaEEYlWLY86CWAC-iUsmpFWUv3o2QdL-L9Yr6r0Pa0oE3MALZrq9TIGIkY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر الاعلام الحربی یمن از عملیات بزرگ کمین در مسیر مزدوران و نظامیان سعودی
🔹
این عملیات گسترده با نام «والله اشد بأسا و اشد تنکیلا» از چندین محور انجام شد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/461664" target="_blank">📅 00:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461663">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acLBkcMC77YXFleZz5-R8LKKvf6-wCddMLrGwtBS7VxKMvqyid7gJnGDteNf2BvDRGJE7liJfQTaV7vu8sm2nSsl93fKuTSZXIQE5jBtm416Wyhflc2NI9xyW0NIZgUHqGI25e3290ZJyCFgwHEnCZAT_mtBhsfmnJW9PbiIgNgIhfnRsEe7_dXWaoYAhKuqsvEal6LIdm7IeBeXyx8EF0UMrGz5611IHWkAxP2E3781az03P12tASG8I2dlDPOVg2-c5MVO-a5C2S9OUYryE6zdHR4dm4MHQ77ubwtiv3s0NDtm6FDCjxUnm071YGD24pVcUCAAzsal9WsVnLXNWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی درباره مرزها با وزیر خارجه عراق گفت‌وگو کرد
🔹
طرفین در این تماس با اشاره به مهم‌ترین موضوعات در روابط ایران و عراق، در خصوص وضعیت ثبات و امنیت در مرزهای ۲ کشور تاکید کردند.
@Farsna</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/461663" target="_blank">📅 23:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461662">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7ypdOZ3MdsV_bVdZ9nwTsj_8mcE-37jnhPVlzJRiIv2jLSq1k6mrUJ6b0ZxY92b9O8lf5wQKPTLysVHeciPzGLLO0N3r70FrPJrtzQapD_XwxFkSaVYJWaKI36PJg87PEV91oJSflHMWzXi_lCVteOL3yRaFIQJRCej15yU9eVhA-zVZND65sKKq9HKNUuVP6B3hzj186qUMpuwxawaS8S2bjgCroQzypEEu77Asx0w9q3HilKm0ne_S-UkAjmEn9EMiUIafzdgteiltVZMo5h8V5pWYBc8e-JyDwg9jO4MjrOVnnXDZXV6EGEhdekoqkgh-oe9R2WGxHG0mqwKgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا دولت از خانه‌های خالی مالیات نمی‌گیرد؟
🔹
با وجود شناسایی حدود ۲ میلیون خانه خالی، درآمد مالیات بر خانه‌های خالی در سال ۱۴۰۴ کمتر از ۱۰ میلیارد تومان بوده و وصولی این مالیات در ۴ ماه نخست ۱۴۰۵ صفر اعلام شده است.
🔹
کاربران با ثبت پویشی در فارس‌من خواستار شفاف‌سازی درباره تعداد خانه‌های شناسایی‌شده، مالیات تعیین‌شده و میزان وصولی و بررسی علت ضعف اجرای این قانون هستند.
🔗
اگر شما هم خواهان اجرای جدی قانون مالیات بر خانه‌های خالی هستید، با
حمایت از این پویش
به این مطالبه بپیوندید.
@Farsnews_My</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/461662" target="_blank">📅 23:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461661">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apLxGNyYM_X0wXpe1g2IhxE1Yxcw1HsRVMajziG4zeueMkrPKNso1RAuaPXkiCVofysh-6YyZl3fg1UnaqZUJX5nxO27iLt4Hic3tcoBWfcrElpMseywsd10x1b30TxSnESmPW5n1ekE08_4oTeO5aHvvI_RrQ0bm-Mk5DNp9sGQlXKfT8Q5nfMtQMn__MgVaa1INWpRSQyuJBBWaGu-o2p4YkvYvh7fkfOFEMDIno5_p5TebmkBHoTf0w9yzSV93ynTWjukJqJXUvXvgl54vy8wNTQDiiJ3M9Bwy84uYU1n_ITJmCCa5uXEqO_VVKOdsKNsjK31pLvvlYACNnKJpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل ۷۷۰۰ بار توافق با دولت لبنان را نقض کرده است
🔹
ارتش لبنان: نظامیان صهیونیست از زمان امضای توافق آتش‌بس با دولت لبنان حدودا ۷۷۰۰ بار آن را نقض کرده‌اند.
🔹
هدف نهایی اسرائیل، ضربه زدن به اعتبار ارتش در داخل لبنان و در برابر جامعۀ بین‌المللی است. @Farsna…</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/461661" target="_blank">📅 23:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461654">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yg-XhDORugdKVHCG8q5uo0e0yU8Nh-8uss1q2vzRWdKyFpCdKMG3cg6lzPvLpvgkPrUYS8lPx7lsk8JTCiFV3DsPXfAacKo1sFMqpYkC9RFIvZvbAysu1NBZa0JOGUGvWBlLWwAPbDsR7umY2DK0s_ZjxTh3SfvnVqfy86WBM4mIcQ2po5uZAcD7IVqZO1JAgQHbJ76qdoOl_m-JoqQVglQs7znZp1kf4z6PJb7wwbztiFw__5mY25cs7WtdcCbzjfyXm6eCJn39ozslDsiEdX8_QTHJic3ppyOJc6EIL13dFSHWA0Pn_b_mNq_LLBmcmiWXN8-msp7ucHzdXZXM6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-qdswPXjaiNjOTNZjmcmQCdPpYP9tp_I6WCJrSiA9pbnfIoceraUhKCQ0q4EVzlUtgzE3ssu4Zp293kVk3z9xcV_qU4NdqxQcarrgwLKd6H--an_HCVEsc55sQUCvVYCIpV6iZxh2oCxU3XGdm-GJnEOUq72rcrvjKhGBAev6ZpnEwA1bkYZyS8RfQNH193YLnM979hL9HuwsiUWPGseKRBeZt7bmMMp_D_pd7et2euuO5XmZEybG3lT7Qe1tjkHBEA9ZDG9lm4fnyII7gG4frEWSSgqZhkoi3mzfogLoi9v3eQWRqMq5hSSve1irvmJevBhB57hjANexg5iGqWPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/doamqdxB5W885ZPXm3xzO5jmLDYkLjySgLJUs-mYEv-gV3eEjeHvfwf_OcFg5icTY5LqB6jxt9vtT8JTOo3QMyfEPq16EjY7zzaTzw6rbu7w-AwJdZ3mOz6PSl-1Kc_tVpfVXxD2vXdnB8mKp6P2uFQ1j_Jd7HJ4Vdtud4GeOT469I1hX7RC-1t3RBoQQt2uN2QXL9yj4Io1X44SEmeG73GLmy9pQA90TZkec6o9pNaU2h-lCYp6SWzBExyOkiaeIDrwq451ws-nNkxvZ_5a3SZkKN7fu_Ojgk_09wOIDkmoBJ-1lRGNfc1FN3VXRAn5IRcZQ6XLaSQjZyvaKBA2RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CEphxkwnfAPhFq7_F0eLGPYkGyA_lpAbLhEZtG8HZQttj6Aq0G--EdenXSzEPjsGQXMiubuC22Pevc24vI9TKmkDv2RWeS9tkOaFD7buhH75p_WtfXkjGzcpK5qip6j2eKV9xeSjSkwUzzhWWjmjoejB_mWnXsCHYeo5eg_5TYsYJDo0AnSG4nYy8W4WN1QsKpGZ7jOZDYLnRP-JXDkeVsLRCqqka8rZxA7ZEIVeoNyxjKjg0POmzIROUH8-iwgadFWYxxGfJfgAVKF_VMPeTeQY4ikrVhl_qqIZr0A8dk8Btm2q0QgqZrPvlwUl1QdG980OFII8ogmg4TKya2au4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pdbYjxrguhssHcbZFa85hGSnI0nGccxkAR_NdoCJ6x2AKFcmB5lBcMMpNiah4MYNiwX52Fr6W_T_JoyWUKABexuEftdll-MmK6z7uiVryqR0RgMOndDia4Ce5AST4IJ67YfoU2cJumQJnGHCvx058I1qZYuQu2udivbdlNHSAUpEfNfxSaBEYr8q3A-QED2u86YTMoEJQ-oY0vr139BfIogXdh8mLLba3f5hL4p6z8N4no0YeO5Y8pvzGfxksLQ12EdB9a-1YV8EpZQzEXkg5AZdJgCbMTTjqTVSJLxIW5I0szVBQWA48Unfi7pfiwnQ6Z4tKQAL4TneXzkGzBUmlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QvfJUjFK0V9u2vI0tPfrT8nDCg4HXR6bRMOlcMZcM4UIMc5aD2AxXpAN_Ir14YUUxOj2vv8UG0zSXMyg8ScxJ0L8EvHyg4gid5oXkvfeu-jyCUe-oD3XDVsT56BPRwycSojmkGAA4mnBVb-V_DlB0fI749D4AxaIpsJqOdFi_CBLy8jG7CKBia5gncMLAz7AV1uBokRjr-zO0k9cHABvbhGDIf7MfCQJ-XkN-g9vLGqDFm-r2tS-E9hOC-osatO_I0MztOiv0q-sq8qNIyXUxjDnBPbgOyXLyuX9_qK1xQDr-meImHMeM1k_peeFIbUQCJoFW8R3aRcH35JeXK497Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lC7mYw6mPX44ZgImqRi7hbqDNZAd5luCY81bxKFv-2mNGKST0LnctB9VabkS_PPicfoiPPAIfOeFtAUwv7R9arfbF4EGzu5HmYCL5YPFYC-h_CB3oA0q4O4nSAcuek_kk-4fRYkX1KLFKZAdcUlwwDVKLVrOK_d2RPukWyI3beO1PXFMS0zIRWaNg03opc-Wi85hmBp45CGSF0R6FRk0fxEFMPOhGaFonZLVRtGhmugFK3jvGLScv77GXUgF7dxPCcHq5nHj2VfjiePZS-uBPD16UaCWuXL1tTOKAxnh3PVxgOA3OMdbcZ7aWntxnKyVEIMNsxoR2gFBgERwpe4s7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست خبری بقایی در محل شهادت شهدای لامرد
عکس: ا
حمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/461654" target="_blank">📅 23:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461653">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5460e8a8d.mp4?token=sWHfHZgkzSjyDt8ShKGyFnUbdcq7-f5oKu-DzJ7PgEvFxR_RFls7QDkTwp0R82IheUxegH3qQyw9cgdxrv_mco9cChqD0cKsLf6rE6vwPwiZMOVGkOw90WAz6XBNNxJfgR-1MjexNoYDHZi7stTeY-Ml1iHU8r1cnOtRI_bWFd0G2PiYbj_57QXBTv6qq4dn_dX1qZKfh81zLj62uO0gHpFjz2s1ZZNQIJ9AaIgrkWF7IDVkXXj7apfXo3C8_IDG1oVKzCxrljfqWpEmDu96DcEnDdRZC5raZjXllUA_eiXnGRMiAau9pcG3KaBmc7LxtgBPieYvImCDt6F5imIj6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5460e8a8d.mp4?token=sWHfHZgkzSjyDt8ShKGyFnUbdcq7-f5oKu-DzJ7PgEvFxR_RFls7QDkTwp0R82IheUxegH3qQyw9cgdxrv_mco9cChqD0cKsLf6rE6vwPwiZMOVGkOw90WAz6XBNNxJfgR-1MjexNoYDHZi7stTeY-Ml1iHU8r1cnOtRI_bWFd0G2PiYbj_57QXBTv6qq4dn_dX1qZKfh81zLj62uO0gHpFjz2s1ZZNQIJ9AaIgrkWF7IDVkXXj7apfXo3C8_IDG1oVKzCxrljfqWpEmDu96DcEnDdRZC5raZjXllUA_eiXnGRMiAau9pcG3KaBmc7LxtgBPieYvImCDt6F5imIj6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سست‌ترین پادشاه ایران در کلام سپهبد شهید غلامعلی رشید
@Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/461653" target="_blank">📅 23:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461652">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd72072398.mp4?token=O-WOEz5NDH3yAzFxAzmW1qS5th39JTN_XwS7jAVTogKGr2eB73YIcTQ90KEAQT9AIGAQtLzDoxF2tPu09538uljS4LZnGQ1JT_V9-XqayCGiiMbM-gT_UQmvL_obteG_E0mNxSH6ollv_7zFGGmSAcq11_7jBDYz3ZS4rAsnYMdezSFVV_Vq-UybBrrjxULx1hABotNocy5p2ajYgqb1SkpFAL3SF47L4rLwGl3vufYMeFPTYD5pLBMfTnxAiv9LLWDp3oNDxbUVBIYzFgHcQAkcLIeuoahDiNXUtM7k_lhgB8JB6Q66mtFIKG4wC1AvckEkl4Z4_v6liDoHZ819Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd72072398.mp4?token=O-WOEz5NDH3yAzFxAzmW1qS5th39JTN_XwS7jAVTogKGr2eB73YIcTQ90KEAQT9AIGAQtLzDoxF2tPu09538uljS4LZnGQ1JT_V9-XqayCGiiMbM-gT_UQmvL_obteG_E0mNxSH6ollv_7zFGGmSAcq11_7jBDYz3ZS4rAsnYMdezSFVV_Vq-UybBrrjxULx1hABotNocy5p2ajYgqb1SkpFAL3SF47L4rLwGl3vufYMeFPTYD5pLBMfTnxAiv9LLWDp3oNDxbUVBIYzFgHcQAkcLIeuoahDiNXUtM7k_lhgB8JB6Q66mtFIKG4wC1AvckEkl4Z4_v6liDoHZ819Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سهمیۀ مازاد سوخت تاکسی‌های اینترنتی تا ۳۰۰ لیتر افزایش می‌یابد
🔹
مدیرعامل شرکت پالایش و پخش فرآورده‌های نفتی: تا سقف ۳۰۰ لیتر سهمیۀ مازاد سوخت با نرخ سوم بر مبنای پیمایش به ناوگان فعال در سکوهای اینترنتی اختصاص داده می‌شود.
🔹
این تاکسی‌ها با اولویت‌دهی مبتنی…</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/461652" target="_blank">📅 23:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461651">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYPlPsrFfeSRYK19REnhn8wt0Fr066R-AlHXNqWUFQtLyE4-GQcaP79OLSZUPMu-3ikFYHvkPU6yiSlzjqtUrW2r3QaL3OQ_ag87sGuYlrAdFlyVZBbOH3OrEShWnuAId0vFRvWPriGfWW5jlHiknYONwufD7lZT7syOpFqZC2GhwrEKsUEFzFKmTAuLlxomXTig9hftT_ZQHwr9NL40wqribQDu-sLUbT6ArvFds9_Xov2WfY2X6GI4fAXlsCslNVZu0vyesKU53aEkicsfEkVH6L5uhVlf3iNi3uby7GOzUJ740vNgj7aa-0zQgQOT9cJIT2EdVhtu5EfLnEkzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گوشه‌ای از دیدار و نشست صمیمی فرماندهان ارتش و سپاه برای بررسی آخرین وضعیت میادین نبرد   @Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/461651" target="_blank">📅 23:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461650">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8051b458.mp4?token=JwLn_A2zTHrrJhgFKJ8nBUNRY9dJfneNg2FpR3ztma97oM2frbg3bwMA6utsjUMdpm4AidkVQM5Hb5fJzBuaE1oUN94miDmRoFwos5eofi8Tj0o7Ic20CU2-Jf_Y96-KHtHQFJB5lw2rSDd2DBxKS3VBZYAPOV513qBCKvw3VxksDnL1PlTYRD0eCqDYwtrZz4amYoearC3gHC7ke2yi-7pp2FVIW3X5vX7yRBOpvG4nqfkzFm7vSXNbXmVMH_88cImtfQCFGl3Lm57TuXIZzkSJ07l3zPrlehxGJXJRQJVkzlmYPd8dZoWWhWe1upwJCrlRyjCiG2IvxJILVE3M3YPVwybYPBiXiZc-fnfreHC_AkCm-9qv8P34wAkXgys_WGHOC4PECW_9SeSfE5yYXoPFRtAOScf2cMOLPYJsrL8LIqQZeQlpFUyvyeTtBPtmzDikalnuP6CfKn8JWr9SwLDN2ZqiUA2Ypez-pEOrupjv2pIYJGftmWeNlJLMovihscLv5kkLHm51ziyyXC6L1UXzWD3wgeP781wrxPomLwthjGXIJVRS-iYo2uDdqKxOhvYelqhpKjRk57KuQoOvfzzsRw8aI9mxzAQRVJvQl9xBtDmJyRu3_pOVHosjJMI5_GyFMPi-51plvJn-hzfqYEhoSgIbh0fPSZ1Himc40hE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8051b458.mp4?token=JwLn_A2zTHrrJhgFKJ8nBUNRY9dJfneNg2FpR3ztma97oM2frbg3bwMA6utsjUMdpm4AidkVQM5Hb5fJzBuaE1oUN94miDmRoFwos5eofi8Tj0o7Ic20CU2-Jf_Y96-KHtHQFJB5lw2rSDd2DBxKS3VBZYAPOV513qBCKvw3VxksDnL1PlTYRD0eCqDYwtrZz4amYoearC3gHC7ke2yi-7pp2FVIW3X5vX7yRBOpvG4nqfkzFm7vSXNbXmVMH_88cImtfQCFGl3Lm57TuXIZzkSJ07l3zPrlehxGJXJRQJVkzlmYPd8dZoWWhWe1upwJCrlRyjCiG2IvxJILVE3M3YPVwybYPBiXiZc-fnfreHC_AkCm-9qv8P34wAkXgys_WGHOC4PECW_9SeSfE5yYXoPFRtAOScf2cMOLPYJsrL8LIqQZeQlpFUyvyeTtBPtmzDikalnuP6CfKn8JWr9SwLDN2ZqiUA2Ypez-pEOrupjv2pIYJGftmWeNlJLMovihscLv5kkLHm51ziyyXC6L1UXzWD3wgeP781wrxPomLwthjGXIJVRS-iYo2uDdqKxOhvYelqhpKjRk57KuQoOvfzzsRw8aI9mxzAQRVJvQl9xBtDmJyRu3_pOVHosjJMI5_GyFMPi-51plvJn-hzfqYEhoSgIbh0fPSZ1Himc40hE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها امشب گود زورخانه را به خیابان آوردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/461650" target="_blank">📅 23:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461649">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2366b049.mp4?token=UYfeoFFY4X43Ji8mc5h9r-P9104MWcphSJXw7xf4OgKfFDsBFIUINi-liPPmWNa7AGfDxwqhWxLF_1da_fYNxoyVolLwC4u7JKu4AZVP5bmbJFnimSH-QEeesDi5T_Btxfs_oJQ72BsshGlQIVODzaayANpujsqO4G00hAUlSzIatz0eHVg5kkL7gqVnMN6LSNv8QhCbrvc7wQ-WqatbmPvTLUaD6I7gdEy6YzLjzYDtPBMVwG9XPrb0Sn5JRXlcRcx-QOJffhY8eeOloWY36DNrHi8gmpweFOujJsrTPri2s9yWDrlHcFbFO1nmTXwFGROsTwaL61JY04QiUCTIEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2366b049.mp4?token=UYfeoFFY4X43Ji8mc5h9r-P9104MWcphSJXw7xf4OgKfFDsBFIUINi-liPPmWNa7AGfDxwqhWxLF_1da_fYNxoyVolLwC4u7JKu4AZVP5bmbJFnimSH-QEeesDi5T_Btxfs_oJQ72BsshGlQIVODzaayANpujsqO4G00hAUlSzIatz0eHVg5kkL7gqVnMN6LSNv8QhCbrvc7wQ-WqatbmPvTLUaD6I7gdEy6YzLjzYDtPBMVwG9XPrb0Sn5JRXlcRcx-QOJffhY8eeOloWY36DNrHi8gmpweFOujJsrTPri2s9yWDrlHcFbFO1nmTXwFGROsTwaL61JY04QiUCTIEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرزند شهید دهه هشتادی جنگ رمضان متولد شد
🔹
دختر شهید جوان پاسدار امیرحسین کاویانی‌نیا امروز در اندیمشک متولد شد.
🔸
شهید کاویانی‌نیا در عملیات پهپادی ارتش تروریستی آمریکا و رژیم صهیونیستی در جنگ رمضان مجروح و بعداز گذشت بیست روز تحمل جراحت در چهارم فروردین امسال به درجه رفیع شهادت نائل آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/461649" target="_blank">📅 22:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461648">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c12ee2739.mp4?token=patmc5_3xJbC12zMer_nKi7bwi_CqrrkNDdTY__Bl7Qpn4-o-J2uEX-Mfk-64OknAwbuJWTr7sPYWCvEVqSoEVAw847ThDQ6eBIdFFhgi9Sb2HuxM-D_jkM2U5JI0AJipchE6euCalaCD8CPGxC_RF3P5AcLpPy_USfb3atYJ1o081uGYtDVPysO7wPQANatXXKge0tdBQBsiVwEK5EUYUxFjurNWXwZ6bexwiGNx8KhMHYhyoBMO7H_lJG82gCgLh0F0Nd1wYB6takng-Lg2ZVFpMcMc51K2-8I5eMaELT5lAAHo8IV0b7dAB_havQTg_ectZ6bGNqPYSaYjp7KKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c12ee2739.mp4?token=patmc5_3xJbC12zMer_nKi7bwi_CqrrkNDdTY__Bl7Qpn4-o-J2uEX-Mfk-64OknAwbuJWTr7sPYWCvEVqSoEVAw847ThDQ6eBIdFFhgi9Sb2HuxM-D_jkM2U5JI0AJipchE6euCalaCD8CPGxC_RF3P5AcLpPy_USfb3atYJ1o081uGYtDVPysO7wPQANatXXKge0tdBQBsiVwEK5EUYUxFjurNWXwZ6bexwiGNx8KhMHYhyoBMO7H_lJG82gCgLh0F0Nd1wYB6takng-Lg2ZVFpMcMc51K2-8I5eMaELT5lAAHo8IV0b7dAB_havQTg_ectZ6bGNqPYSaYjp7KKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهرستان ولایتمدار زرند در ایستگاه ۱۹۶ دفاع از وطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/461648" target="_blank">📅 22:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461647">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بازگشایی موقت مرزهای شلمچه و چذابه تا ساعت ۲۴ امشب
🔹
معاون امنیتی استانداری خوزستان: مرزهای زمینی شلمچه و چذابه تا ساعت ۲۴ امشب صرفاً برای تعیین‌تکلیف و عبور مسافرانی که پشت پایانه‌ها مانده‌اند بازگشایی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/461647" target="_blank">📅 22:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461639">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NCJ5eYuUrfdhF-0mw_MB1D2R8A2JH_LYgyYVAVsOznaSCIVLr4VvPQr5Q6GBlkaWw7-3wNHKbZVYg1yPysnSNlou3iHDg4ibSNfVi218aQzyma7fxKu8f_ytHygRfn-FVFue7U1V0WIPxt1vKGoDT07RA3T757lPTgcqEUmUvAwChzNjH6DHuaEONPKPSmLgRWfxBYfivlgZgIlDNAeh7T8Q-4FBjOO24_Kpx5RTn5Wih7KthKtZ1iT57lndEhpM3SKAwc7GPv8K5-aTEtW84lbf1I0Oi3VB1FR_cOsqVl7GP9yanDgAuMDgWCiLlIUx-7tA5PLHrAft7G2JVpV6cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/virkHb_2EhOi8e_HNfuLK4MiO5i1bXdw6fZJMCqqokr0lsyXKj0ZsMf3Ng0I65-DEwE_uhaA5RcfZpB2O_a3NhphInSb_1oGD3e2L67xsbApF3EuU-YvY9FQYL5GdTWf5Kk08dmoorkI5QhjoTuGK6FiPSO45JB0S-A8ox9rtTLq5fZfNHm4r4rYhCagLwyq18Fb8Zwfu2QSNQ_nKSBXmP42NounSP_mMHJSQlvO1VrkAsLbgmNHfxe3am0Q_XSzAtKuaB7PYb7g3Oq5I-JHRvtf_vhLNxzLYpUFo_ETRpj_-EKVEGgz0cJzzUOfgwoAQwrhsC15VPHSR9nfEKd-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L9NeiBaul_DpnkjmcVO9HmArIQl5Oa0YWcym2BRoO4CIAYToeuq7jIE4_AMGl8LohB9SiEymgZC0QMWEfMu31DV_dRqqy93AYECXDSzJXZA88BT-AYE7i2xeNEZpSC4V4Mrm6hXSQgiRWnQqoRkfM8ocLCCtaiqIa53Cw6gHhDX4otrc53SRedFgrNQV9hZ4IrjeEWhEWV1s6EQZQdT7l-IYiIZPBvGCJadCt_lDIh7nIZggXIRaqvnUDdxoKHV2jT40dTyJkX5W5PQoW8xfnhgQo2o4dNm_HyMMR5h_V41TczKDo9HYeH7eNaGbEG1K6aWywwSVupx9ZWlgEj41Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zceye5EiV5SVpUEukhsewzsbSb2XLcbBW00fLKXMFeHSVYCM-0efBCvlNKqrojGVqJAnSw6iUz90mLL6e3PkadbhKrBMju67un0_DdOzbnMgV8XG4QX5nVO6nX5e8YAqcsEZWnGrflvQdYs5fneAFvUFpfyna4Zj5WMLxdVK6c7656W4NUre64F_sklnBxx6MfDxa4xdnjN87jrta5flW-SVsqiUSXG-vkHW3sNnFeOv-7VWmNioQAxGBY1DY78t0u7ljmvXvwk2BCO7akIxzhnJnXTwTxtXH0Jbxxu4bmOvoPtKqzjAUoyyFMTP4VNjw0XFnDDgq2pl7ro9mKfnsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/spTooW0ZxsIcE6tqej9uJSLtbiX-7EaJwbe-M1tA_GpaOIY_tgqbyEsmp_8G1Dz40UmgabGxqgQGJkRHZymBer-zgL6ZyOqbpxACGaRxsSCAtNsF8n-nzoIE6p6rx64RI37BLSliQ5tGmbvTuMjPHhUj_QCkVKUyzLcSDdBs_epOQjro5ydyvBs0OgCPlV5xkAiRDfjG26O7vMdDBTRjFdgT9ax73UB2QjP1W0a65-p496_hxKCqabkQ2DbGm91JNCKkI8AUUJ3boZHPIJhW2yWSgoHdrB4oZ4My1zQ7B5p6xwjLU35VbQRlawGrRsEzjbOEtfLs67klYVmSPNKG-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sG90aid4kYYokbPAB4Cbk9RF7pN8AZlNjL7vz8nTRXxjGTcu2c8u5eJp1Q1zIu4P0JwPNkg4geLxp_6vdmBpgIW6OArlmApk_ORxhVvy3C0QKCPDmJ4w0GUUKIKJD2_jwGcF2qJXoPzUgV-UPBClqGNDxSBoXtKjhNTvzm5U-6mDmnnEOO4vvl9_KOQ3lUrXEsd9tGTSIu65gyxuQ_qxt03QM7RHFQZy5e7LACVAM-ZXSnm0nBDSEeJ5RNj18e3AlAEFkr4bGpyvdXE3ZpS1cer44bRV4boolNprYrWYmuPJ_AJGPPOVWaoP6lDcnzFKZVArQgJpbVMu827Is405wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r2_zl23_4GagA2QClpv8RGtAOBChbX5RamvUNwsYaK-N41y35OaZlmXK9W8JlRu-SaYRqOYtrqboqiuvTFQEa1rMOYkm5ceUBAXxOfmMipAzFu51m99pxDnOWazK7wSjxjlW63HVApDZWOXxBIdR8UW0OxI_7_r3agoyNNOOpFoEtMauTEOtx3sn1BV1bwkqHC9FeXHNLIF8iNFCbKUzAAayL7tIopnwC-uJdtsbg1H0R9aSH4imNcJbRAtybuMGaw4YMPhnhB5MsT5xCxtU1y4Z7-YjMD9qx5oWBI_iufyJDIlTl1VZvP8tAhtB8cYdK20VUi2iD3hQN2yb6vE9Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H9skPXt9q43HDNoeF7HsaDts1lClUcIIbXUg1kNz460WGnNLeHM_bYq6BWj6IaYNRU1AlJBy7-7KjRRxLmbFpXqNmX0N7G8n0K8kLu9b5h4f68ofIcusbgj45wFLx3jb7TBaVEeuSzuktuZC6DGjcdWoGng0LgNsCzCmgAeAozxZ2kEwezpukNJihnFoMaFRhNTDrTLRN1PHdWdbwqYudWSCLXxMQsx20xLNy-gBlCyvYReGa6Ed6Tm27Lx6AT2HMj6O84ZBKgSDTovNP0_Xyzw-MURvFFO-NAt_LZY-eUjr8aiSQ3SRjTCCgpf4jdCRLqP0YK3izy7pjZ5X16_pJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌هایی از عملیات گستردۀ زمینی جدید یمنی‌ها
@Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/461639" target="_blank">📅 22:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461638">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حملۀ موشکی یمن به عربستان
🔹
سازمان دفاع مدنی عربستان از به‌صدادرآمدن آژیرهای هشدار در أبها و‌ خمیس المشیط خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/461638" target="_blank">📅 22:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461637">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حملۀ عناصر داعش به ارتش عراق در کرکوک
🔹
برخی منابع خبری گزارش دادند تروریست‌های داعش به یک مقر ارتش عراق در استان کرکوک حمله کردند.
🔸
هنوز ارتش عراق به صورت رسمی این حمله را تأیید نکرده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/461637" target="_blank">📅 22:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461636">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b31d3b847.mp4?token=pgNHyE5BCg47YsP0x1ihqQYlTz6s9eneAC135y2X3dgmpoeF3PTI4lc61aIhbD3yC-5hTFPu3mwEFEVCbQREGktCjeMqBp5P-o8YiWMvlbpKrUCpQf0dv4r2B7AkmzOSBqotjBaATMUW0ZQRKvBi0O6jkmWAXVFCO5Jm2QlbfCDVGiqts0pWTNchHsDNqg-KqS7az7ObtLqiISgGlZxxCHFYKwIcZXeShRBh8RbYjm8eZ7VnrOjX0eqCSZN2mwmq3a87HqV9TdXn6DFB2tDL7i1rUKMi4bfM6gn09Z4dXqtb6HIxGCGG2Re9ZCQ2ivX5XJwZtqYXyWDqEGUexd2Umg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b31d3b847.mp4?token=pgNHyE5BCg47YsP0x1ihqQYlTz6s9eneAC135y2X3dgmpoeF3PTI4lc61aIhbD3yC-5hTFPu3mwEFEVCbQREGktCjeMqBp5P-o8YiWMvlbpKrUCpQf0dv4r2B7AkmzOSBqotjBaATMUW0ZQRKvBi0O6jkmWAXVFCO5Jm2QlbfCDVGiqts0pWTNchHsDNqg-KqS7az7ObtLqiISgGlZxxCHFYKwIcZXeShRBh8RbYjm8eZ7VnrOjX0eqCSZN2mwmq3a87HqV9TdXn6DFB2tDL7i1rUKMi4bfM6gn09Z4dXqtb6HIxGCGG2Re9ZCQ2ivX5XJwZtqYXyWDqEGUexd2Umg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۹۶ شب حضور و ایستادگی مردم خمینی‌شهر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/461636" target="_blank">📅 22:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461635">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8732cfd1f.mp4?token=iUiQ4TJxc1VnAEBzJ2Y2vx4_nwFKayoOTEkCX7YRYs4pXRpgyShVHzoMdvShG_M2e9n9XmhavPztmIWhF8GwKWn0kv58Ar0vzcIhXuyXIxc9N54z-TWDk1DPvZCZMOP6OH9HxtqKYKtpLdjLK7y81sulkAw1Wwtzu6c2vbCWK-BS929ajlxryeWcvn2O9j-kJCjbVmXuaL95asi1PWbVuT4gSEilosmH63EQepOvLO2I1bHGjjyqOF8I2NS3B-2cJO_R9M7jKnebbOT0X8dmvQ2xHuoO1kEGx27YY9ao251vlmdqBcgHppmH4RGWZQV99TyWV2H7oyPS2TfAV7mthg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8732cfd1f.mp4?token=iUiQ4TJxc1VnAEBzJ2Y2vx4_nwFKayoOTEkCX7YRYs4pXRpgyShVHzoMdvShG_M2e9n9XmhavPztmIWhF8GwKWn0kv58Ar0vzcIhXuyXIxc9N54z-TWDk1DPvZCZMOP6OH9HxtqKYKtpLdjLK7y81sulkAw1Wwtzu6c2vbCWK-BS929ajlxryeWcvn2O9j-kJCjbVmXuaL95asi1PWbVuT4gSEilosmH63EQepOvLO2I1bHGjjyqOF8I2NS3B-2cJO_R9M7jKnebbOT0X8dmvQ2xHuoO1kEGx27YY9ao251vlmdqBcgHppmH4RGWZQV99TyWV2H7oyPS2TfAV7mthg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت صادق محصولی از تلاش سپاه برای ساخت موشک ضدناوشکن
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/461635" target="_blank">📅 22:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461634">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac454eaaeb.mp4?token=H_bmNNqxhjUbIJQV51Xfkj_i3770602T2PwDW8Q-1siBDhS3SEiwl5KzaPicfn3ImZxi_iltAd3k_6JyB6A_0bgFRLFs3ncucJBKjHQE26wlTS5I_RjVpwkY_vIxiIXx7wtNE9lj1Z0T36akIAwk_nRPuIAS7Y6MBoUnwy2Gwjl3Dr4mhGLd8HOAi5LSSUDsVI-PemmLrJOqo3Z0bsQByatJwyV-gBteddHNFFLq4THgcbbfkvARdn4y6FlZm2qIhvt_OvJrZ9Kbn4tabdQuozlFL0_BJeyGh_1QTUdbPNXilYQtiQAdvqcH2c3StdlWO7_AKnVZViX0qgO2BS2irQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac454eaaeb.mp4?token=H_bmNNqxhjUbIJQV51Xfkj_i3770602T2PwDW8Q-1siBDhS3SEiwl5KzaPicfn3ImZxi_iltAd3k_6JyB6A_0bgFRLFs3ncucJBKjHQE26wlTS5I_RjVpwkY_vIxiIXx7wtNE9lj1Z0T36akIAwk_nRPuIAS7Y6MBoUnwy2Gwjl3Dr4mhGLd8HOAi5LSSUDsVI-PemmLrJOqo3Z0bsQByatJwyV-gBteddHNFFLq4THgcbbfkvARdn4y6FlZm2qIhvt_OvJrZ9Kbn4tabdQuozlFL0_BJeyGh_1QTUdbPNXilYQtiQAdvqcH2c3StdlWO7_AKnVZViX0qgO2BS2irQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش تگرگ در بشاگرد
🔹
شدت بارندگی در برخی نقاط شهرستان بشاگرد موجب جاری شدن روان‌آب و سیلاب در مسیرهای جاده‌ای شد و تردد در بعضی مسیرها را تحت تأثیر قرار داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/461634" target="_blank">📅 22:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461633">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
نزدیک ۱۲۰۰ تن ذرت علوفه‌ای روی زمین با بهترین کیفیت دارم اما خریدار نیست و دولت پیگیر
واردات نهاده
به قیمت بالاتر است. چرا کسی به داد ما نمی‌رسه؟
🔹
لطفاً پیگیر
افزایش مداوم قیمت پوشک
و افت کیفیت آن‌ها باشید. علاوه بر گرانی، گاهی در یک بسته از یک برند و یک سایز، اندازه برخی پوشک‌ها متفاوت است که مصداق کم‌فروشی و تضییع حق مصرف‌کننده است.
🔹
لطفا به
وزیر نیرو
اطلاع بدهید در استان ‌ما در کلیه شهرهایش همچنان
‌قطعی برنامه‌ریزی شده برق
از ۱۰ صبح تا ۱۲ شب داریم. سامانه ۱۲۱ هم اعلام می‌کند برای کنترل پیک بار هست.
🔹
در بحث
کالابرگ
، اعتبار مردادماه خانواده‌هایی که کد ملی سرپرستشان به ۷، ۸ و ۹ ختم می‌شود به‌دلیل فاصله در زمان فعال‌شدن، عملاً با تأخیر ۱۰روزه و در شهریورماه شارژ شد. چرا باید سهم این خانواده‌ها بی‌سروصدا با تأخیر پرداخت شود؟ از طرفی
افزایش مبلغ کالابرگ
برای دهک‌های پایین نیز همچنان در حد وعده و «امروز و فردا» مانده است.
🔹
مدیر مدرسۀ دخترم دریافت خدمات آموزشی مانند کارنامه یا تحویل پرونده برای ثبت‌نام در مدرسه دیگر را منوط به پرداخت شهریه کرده و برخورد نامناسبی هم با والدین دارد. کاش
آموزش‌وپرورش
یک
راه ارتباطی مشخص و پاسخ‌گو برای ثبت و پیگیری تخلفات
معرفی می‌کرد تا خانواده‌ها بتوانند موارد مشابه را گزارش کنند.
🔹
در طرح
جایگزینی خودروهای فرسوده ایران‌خودرو
برنده شدم و خودرو و مدارک خودروی فرسوده را تحویل دادم اما با گذشت حدود ۱۰ ماه هنوز اطلاعات خودروی من به ایران‌خودرو ارسال نشده است. پس از پیگیری‌های فراوان مشخص شده گواهی اسقاط من اشتباهاً برای سایپا شارژ شده، در حالی که در طرح سایپا برنده نشده بودم. این بی‌نظمی و عدم هماهنگی بین سازمان نوسازی و خودروسازان علاوه بر خسارت مالی باعث سردرگمی و خستگی ما از پیگیری‌های بی‌نتیجه شده است.
🔹
وزارت آموزش‌وپرورش با افتخار اعلام کرده
معوقات بازنشستگان
سال‌های ۱۴۰۰، ۱۴۰۱ و ۱۴۰۲ پرداخت شده است؛ اما آیا
ارزش پول
آن سال‌ها با امروز یکی است؟ چرا باید مطالبات فرهنگیان پس از چند سال و بدون جبران کاهش ارزش پول پرداخت شود؟ چه کسی پاسخگوی این بی‌عدالتی در حق بازنشستگان فرهنگی است؟ آیا در بانک‌ها و سایر دستگاه‌های دولتی نیز با مطالبات مردم چنین برخوردی می‌شود؟
🔹
متأسفانه بسیاری از
مدارس دولتی
برای ثبت‌نام از خانواده‌ها
پول دریافت می‌کنند
و تا زمانی که وجه پرداخت نشود، ثبت‌نام دانش‌آموز را انجام نمی‌دهند.
🔹
چرا خدمات حمایتی و پوشش‌های درمانی بیماران روزبه‌روز کمتر می‌شود؟ مادرم سال‌هاست با
سرطان
مبارزه می‌کند و در کرمانشاه بسیاری از آزمایش‌ها و خدمات درمانی که قبلاً با تعرفه دولتی انجام می‌شد، حالا آزاد حساب می‌شود.
هزینه‌های شیمی‌درمانی، پرتودرمانی، آزمایش
و بیمارستان برای خانواده‌ها بسیار سنگین است. بسیاری از بیماران توان پرداخت ندارند و حتی از ادامه درمان ناامید می‌شوند.
🔹
لطفاً پیگیر
مطالبات گندم‌کاران لرستان
باشید. تاکنون فقط ۳۰ درصد پول گندم پرداخت شده و بقیه مطالبات همچنان بلاتکلیف است. کشاورزان یک سال زحمت کشیده‌اند و بسیاری برای کشت و برداشت گندم قرض کرده‌اند. حالا با رسیدن فصل کشت جدید، پول محصولمان را هم دریافت نکرده‌ایم.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/461633" target="_blank">📅 22:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461632">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de67b0b2ed.mp4?token=EVhSI3PZl0yBZqfhkLm_LghOcWsSDgPzXTXZQpdk0an2EXbWMw751EodsrqeX7PxXbDp1--KV83L_UZL4Ex21JFOVnZsXJzS0K2GvS74yjjjWelOCss_LND8XWFpacXjPqcgyhK7Vp5R1iGVRmOUyAbwC5z8DHvqEN4g943fYo36BoCqWdUHiS75jjS6e3g84BiX-GNJij1lZEIMQ_eM_tXq3xdr1_uF4-R9S3cc85-NPTzFyUnqzwfY02RiBCEUmNELZQh3tS916IoVEHeHCqBOMjj37dxjypaWetGlIPcTrW7hUODnpAvQEnazRjCIebLsCUeZNEASLTcXqsBrkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de67b0b2ed.mp4?token=EVhSI3PZl0yBZqfhkLm_LghOcWsSDgPzXTXZQpdk0an2EXbWMw751EodsrqeX7PxXbDp1--KV83L_UZL4Ex21JFOVnZsXJzS0K2GvS74yjjjWelOCss_LND8XWFpacXjPqcgyhK7Vp5R1iGVRmOUyAbwC5z8DHvqEN4g943fYo36BoCqWdUHiS75jjS6e3g84BiX-GNJij1lZEIMQ_eM_tXq3xdr1_uF4-R9S3cc85-NPTzFyUnqzwfY02RiBCEUmNELZQh3tS916IoVEHeHCqBOMjj37dxjypaWetGlIPcTrW7hUODnpAvQEnazRjCIebLsCUeZNEASLTcXqsBrkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تردد در مرز ایران و ترکیه برخلاف شایعات جریان دارد
🔹
پیگیری خبرنگار فارس از پایانه مرزی بازرگان در آذربایجان غربی حاکی از تردد روان در این مرز بین‌المللی است. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/461632" target="_blank">📅 22:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461631">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4lT3iUeL7TT14jVvu5e4UGXnxRJmLuC-mVe-u_5B7XQe0vzNKi03n3TGbdfTTQjpV8Hx1pQx6cFHo5IAFaervuY2KKcLpiHGYEi_4ry_DERyIT4hthFfp_dQTNwZXigFlzKXuk4vr90RYq8CJBNJgsXPnFQuGCNvcg4b8gE-eprAaHJl6pdFeY9CrohH3Qte9xzQpo3cC1JrPE_VmhV332PoGzBFiUWKCGMQck4RGRaubWAur9PFYsAhARqqFre50lBxoLSBb6KPhb7P_ItujlBGXc4iRu4ELekRxN96RzytfL-lhaNM7r4LMKnpkRtNcuUDybhIIdfYLmLmGj_Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساپینتو: تاجرنیا به من گفت فتاحی می‌تواند کاری کند که داوران با استقلال مهربان‌تر باشند
⚽️
سرمربی سابق استقلال در گفت‌وگو با فارس: تابه‌حال مدیری به شهرت‌طلبی علی تاجرنیا ندیده‌ام.
⚽️
از روز اول تاجرنیا به رابطه من و مدیرعامل وقت آقای نظری جویباری حسادت می‌کرد…</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/461631" target="_blank">📅 21:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461630">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcc-DJHmKEB-8W9N6YSwo_MgqAGCxjGVcS161ORL_UV4f5eW5xWS5HNRE3zl-JE9eSsB_Vl-mYCCEcr9XqDubnT5QdMNce8XAVTL0kF2CtXbhSb-KaxSUudadrrZbcHtoOBpJq_NAnxzEcjzX6zemy9wAYaX7NvnzeRmzcWj5uXuZXwDrluaf0_CogFEJuOxDJs_zzqHhA1Q1U76m-kd_WSGKVsNxPUhStU90kpP8adEwNUsexlQIdnBvkNs8UeXrEuESgcJ6ZFYrTqfMnEbbzhHsVfEYmVgQ_SJHO54atJlnrTSqIs-9bRzdNCExWiiGxN33vXUMOGgk5_pD7F6IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسئله من و ساپینتو ربطی به رفتنم به رختکن نداشت فکر می‌کرد نمی‌توانم اخراجش کنم، همانجا عوضش کردم  سرپرست مدیرعاملی استقلال:
🎙
ساپینتو احساس می‌کرد خیلی جای پایش محکم است و آن نقطه‌ای است که می‌تواند مدیریت باشگاه را به چالش بکشد. من خیلی در قبالش صبور بودم.…</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/461630" target="_blank">📅 21:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461629">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجارهای کنترل‌شده در امیدیه
🔹
فرمانداری امیدیه: فردا از ساعت ۹  تا ۱۲ظهر انفجارات کنترل‌شده برای امحای مهمات برجامانده از جنگ در برخی نقاط شهرستان انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/461629" target="_blank">📅 21:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461628">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K06vVCD6NafBdToWGrzqVV_NU1rJFkXlDDiOAuntqJ1G_ovPdNKesCQBf6mbF0RFjabSfxtaO4Sa4KxA2TcycIYsEytBV5UukvNlC09aHMjSWKB9LyL7Mxy5NDJHoOTAvV4aiuZw-sDWLfsKWtQi8RViVQ5A_YTgBuu-xvVKgfZMpCyl78tZFp1p5wcaEbPi11DW2yiXMqHaLrMBgjA_hp1OtJ-w6v9YuyJUNnQxyy2B_fijbUDQSP8cBoGrp0z6SVSmAQzGG3PmLOSZZ-A3ED5Yh3vG81BSRXcXSe1MPp2d9g-1eLeb_3QlmCF6ZQnUGmfpI0YuQ-B8GPpFZ8WPng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو شورای عالی سیاسی یمن: هرگونه اقدام احمقانه علیه یمن با پاسخ مواجه خواهد شد؛ حتی اگر پیامدهای آن به سطح جهانی کشیده شود
🔹
محمدعلی الحوثی: منطقه در وضعیت بسیار متشنجی قرار دارد. هرکس بخواهد آتش جنگ را شعله‌ور کند، باید پیامدهای آن را نیز بپذیرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/461628" target="_blank">📅 21:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461627">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حملۀ موشکی یمن به عربستان
🔹
سازمان دفاع مدنی عربستان از به‌صدادرآمدن آژیرهای هشدار در أبها و‌ خمیس المشیط خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/461627" target="_blank">📅 21:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461626">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hY40_pAMEiwAIeulmQHX4oJ03GPcw0fhSjrmENJB4DED69VzG6fwAOcTXuUNTYYWha374CgY2AzgNxOB00NOrdi9WbdVp0rg7Pfdq6txyE9zFqOyRhBlfOYlDehi0HXch9-z0OQCnH-ZqBLqdNl9rqSKje_rfbP78g83Df0IdC2kWD734rEmNaxT6rSMGCoCx5Nwx8EayUCYQPI8e-ucAjEZfEgS_9Znw7Kd6X5jlfbsFRK0yVcA0hyNgfjRvduccAwylxZNUQRVHUUWRnM9KZXWn0hoIB5uPqN4O-uYJ1veRN-q9TVtBqsdWNL9r6HujjQ64-VJqeVj5GgOiS-aiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متفکرآزاد: دست برتر ایران در بازار انرژی نباید با پالس غلط دیپلماتیک تضعیف شود
🔹
عضو هیئت‌رئیسۀ مجلس: دشمن قصد دارد با فشار اقتصادی بر کشور، ثبات داخلی، امنیت عمومی و آرامش روانی جامعه ما را هدف قرار دهد، اما در مقابل، ما توانسته‌ایم با راهبردهای خود، دشمن…</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/461626" target="_blank">📅 21:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461625">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bf93b046.mp4?token=P2OQM9RAP4Nh2jw021AJPETMeA-JNVljN9FNqkd8SaRmlJuxES20zwg4YnFaef0WG5KgpKVeri1rrjUxNhzaZV-XRMLfMzqLm41gRlYkeFjcSiFgPKyo_YL_BcP5NH9Zy11XTheiqhKmORi4VsEewQWWV-tiCsJRTn5JKnfs6h-EQ7UQmt584BWeJOa-4ouU3RnJLd9iQAOElFiLvwat1W-PVLMSdwmKTG_gVj0iDCXXDXHCc0Sn1iTJM6Y5F5OST28kXsSDrQzyaoD0HTdKeVEoguRjAgr5lOcw1W6PfE5akm0o27R73hNlJP5R4U-Z0Z6wd1GpZ_aXc7mgh3W7yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bf93b046.mp4?token=P2OQM9RAP4Nh2jw021AJPETMeA-JNVljN9FNqkd8SaRmlJuxES20zwg4YnFaef0WG5KgpKVeri1rrjUxNhzaZV-XRMLfMzqLm41gRlYkeFjcSiFgPKyo_YL_BcP5NH9Zy11XTheiqhKmORi4VsEewQWWV-tiCsJRTn5JKnfs6h-EQ7UQmt584BWeJOa-4ouU3RnJLd9iQAOElFiLvwat1W-PVLMSdwmKTG_gVj0iDCXXDXHCc0Sn1iTJM6Y5F5OST28kXsSDrQzyaoD0HTdKeVEoguRjAgr5lOcw1W6PfE5akm0o27R73hNlJP5R4U-Z0Z6wd1GpZ_aXc7mgh3W7yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یاد امام و شهدا در شب ۱۹۶ ایستادگی مردم شهرکرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/461625" target="_blank">📅 21:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461624">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73b822623.mp4?token=L0-OC0_FfuscB_p5fREgsnre78zr4yex-HibGKWIUMePUjh-dzC5eo1GLUOPZsd4gi2Zh30_CEMbL_Z65UzcFUlVGIzqZtLIggKRHrYYGKY8_aNc7XrfLglTHr-Mv3Nn7-hIwV_SXfdJAI9HvTF3HcbyHVp8MZHJ8HYJUQTCW2kBx4GwXSe3VAb-8HLacLaSaVJ5iueJEMRUfaKtX5x9L-110StH1La27ld5x5FhMjCrxDEeQYE14AsD7ls-8xfYFemaNZSW4BC3AukFS7GOEM4rVbkgkVSn0wqnaatNolgK6Gbz8TL9o_-lHLVLh0aXPuYkGiQAaPgP9otNd6H-ulQpm3GO7bsNqrqANfOGTudHArthQoAOLTuTVNXIDlUiywmH8pa_laogiv6JlDHEowhrd8_JpaFsAUZ46bl96KsYtvUYN0duKO0V4q0y3zaBtJ0piZl9N6DrxEP3LGNgN4aHdXFq7TU_20Qkn-Zs5557YN2s-qgepwl8f_XEovrfwN7qbEejlB-wxveAixRbq0cvv-QDdbeTD_F9D89T9PMlQjIHWByI6W83aBXcjaJnJdBPM-QKpa-mDSOmYCFgzhrpfZNLb5yTENSioX_JtAz-hWPewucAdx4mfpJn6Bhs7Ia23Xio95Br0lJ73Xqy-MKKUaRbdHXXi6lT9IGLT1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73b822623.mp4?token=L0-OC0_FfuscB_p5fREgsnre78zr4yex-HibGKWIUMePUjh-dzC5eo1GLUOPZsd4gi2Zh30_CEMbL_Z65UzcFUlVGIzqZtLIggKRHrYYGKY8_aNc7XrfLglTHr-Mv3Nn7-hIwV_SXfdJAI9HvTF3HcbyHVp8MZHJ8HYJUQTCW2kBx4GwXSe3VAb-8HLacLaSaVJ5iueJEMRUfaKtX5x9L-110StH1La27ld5x5FhMjCrxDEeQYE14AsD7ls-8xfYFemaNZSW4BC3AukFS7GOEM4rVbkgkVSn0wqnaatNolgK6Gbz8TL9o_-lHLVLh0aXPuYkGiQAaPgP9otNd6H-ulQpm3GO7bsNqrqANfOGTudHArthQoAOLTuTVNXIDlUiywmH8pa_laogiv6JlDHEowhrd8_JpaFsAUZ46bl96KsYtvUYN0duKO0V4q0y3zaBtJ0piZl9N6DrxEP3LGNgN4aHdXFq7TU_20Qkn-Zs5557YN2s-qgepwl8f_XEovrfwN7qbEejlB-wxveAixRbq0cvv-QDdbeTD_F9D89T9PMlQjIHWByI6W83aBXcjaJnJdBPM-QKpa-mDSOmYCFgzhrpfZNLb5yTENSioX_JtAz-hWPewucAdx4mfpJn6Bhs7Ia23Xio95Br0lJ73Xqy-MKKUaRbdHXXi6lT9IGLT1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایرانی‌ها پیروزی یمن را جشن گرفتند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/461624" target="_blank">📅 21:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461623">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f45167d880.mp4?token=czU-EnCfmT7NEKfL2oxsi36jBhEqaWd8XGCQBny8RVdfdRxbgmhNYVBdd-Urpt2DDrF9JInTcMX6XhtEGwcRRm7yRnXDgViy3fbolApstiZED-SOpw9d3Xh5inyM7uNjGXR52pQPtFJHlkFhQsWF_asTxC96HJc2o44BKgCZ2gcHwQSwgy-TGUZMiWr-W9_sIbN_Qm2cgHj4WkQj6sFyBMLgLA9FmvcdfXcKF-d0XJ24_ZHrTd0gkZ0Xwt8uDdVW-O8W1f65avMWunDM_LBcKRAvQ7sDfIWzuQXVtmVt0myROue2HqKDlGJMA3N9grOSUOVTwhKCGG-7Xl87DUxKmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f45167d880.mp4?token=czU-EnCfmT7NEKfL2oxsi36jBhEqaWd8XGCQBny8RVdfdRxbgmhNYVBdd-Urpt2DDrF9JInTcMX6XhtEGwcRRm7yRnXDgViy3fbolApstiZED-SOpw9d3Xh5inyM7uNjGXR52pQPtFJHlkFhQsWF_asTxC96HJc2o44BKgCZ2gcHwQSwgy-TGUZMiWr-W9_sIbN_Qm2cgHj4WkQj6sFyBMLgLA9FmvcdfXcKF-d0XJ24_ZHrTd0gkZ0Xwt8uDdVW-O8W1f65avMWunDM_LBcKRAvQ7sDfIWzuQXVtmVt0myROue2HqKDlGJMA3N9grOSUOVTwhKCGG-7Xl87DUxKmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر میراث فرهنگی: برای تخریب پادگان روس‌ها شکایت قضایی انجام شده و تاکید ما این است که این بنای تاریخی به همان شکل سابق بازسازی شود
@Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/461623" target="_blank">📅 21:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461622">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b024849e91.mp4?token=USGQqln0gJ0frjMbf0BVGGhLAs3GE4PEd4JXCnurPLyi-t-QmNXEVWwReEZwjOSotW3HkdEiGPIDnSEf32VzPdqGENfd8Rfvkc2VwlS2xn2_9P9J_XN2uLKj4kVl7VhpR7xZWRh0ANFjA6l5xaPJp7UBHF90Ddv3ZAQn1YI4a7EYU0gQzGO3VdbQs2hyRNz7hoM6MSMcGBGDEgTbXEEn9UaVJbW7v6ZmqpiM2BHfYKSsqLxrT2bGbtHw3JTtTOq68Nv2_VfZiYBiIEqJyQog0_xxObv077_CoWD6OfUZ1ZNpEytqOIX9znhKNzMzgSqm7SdyEYoNK1dYUXkXiIuY8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b024849e91.mp4?token=USGQqln0gJ0frjMbf0BVGGhLAs3GE4PEd4JXCnurPLyi-t-QmNXEVWwReEZwjOSotW3HkdEiGPIDnSEf32VzPdqGENfd8Rfvkc2VwlS2xn2_9P9J_XN2uLKj4kVl7VhpR7xZWRh0ANFjA6l5xaPJp7UBHF90Ddv3ZAQn1YI4a7EYU0gQzGO3VdbQs2hyRNz7hoM6MSMcGBGDEgTbXEEn9UaVJbW7v6ZmqpiM2BHfYKSsqLxrT2bGbtHw3JTtTOq68Nv2_VfZiYBiIEqJyQog0_xxObv077_CoWD6OfUZ1ZNpEytqOIX9znhKNzMzgSqm7SdyEYoNK1dYUXkXiIuY8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشاهدۀ «هلیا» یوزپلنگ آسیایی و توله‌هایش در حیات‌وحش خراسان‌شمالی  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/461622" target="_blank">📅 21:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461621">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b13bb4a0b5.mp4?token=RDD3qry2T8TOHkBN1yJIDODyFCjph2rz_4KCiwv4wlO2nRwmsfG68cFml2Cm-1LoTFLSmoG4AR-59VkCnoxKIBADo8P0NUfwy52XWSEYS4Ltg2dcANJDP6tZVm8DOf-9GwN7vfKN0g-Hw92k-FcTZpJDSUA1BrKNHlpMzkgcYLhyd7cO6h4H7eAN9pRSdDuB7XbMLU4v3wpqhBqaYgQF3XdZ6-5pwptO61Zbt2rMLiVDfF5GjwDOUiU5wQeGEE9NGI0_nItGlvQE3-8CLxNx3GeIZa_HwKIsbV_HTJHl0cuCkOordHH7hdHWAIsGxGQkW397MCdd2wGzas0YeUDuhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b13bb4a0b5.mp4?token=RDD3qry2T8TOHkBN1yJIDODyFCjph2rz_4KCiwv4wlO2nRwmsfG68cFml2Cm-1LoTFLSmoG4AR-59VkCnoxKIBADo8P0NUfwy52XWSEYS4Ltg2dcANJDP6tZVm8DOf-9GwN7vfKN0g-Hw92k-FcTZpJDSUA1BrKNHlpMzkgcYLhyd7cO6h4H7eAN9pRSdDuB7XbMLU4v3wpqhBqaYgQF3XdZ6-5pwptO61Zbt2rMLiVDfF5GjwDOUiU5wQeGEE9NGI0_nItGlvQE3-8CLxNx3GeIZa_HwKIsbV_HTJHl0cuCkOordHH7hdHWAIsGxGQkW397MCdd2wGzas0YeUDuhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش تابستانی در ماهنشان استان زنجان سیلاب به‌راه انداخت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/461621" target="_blank">📅 21:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461620">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/946a6ff60e.mp4?token=H37B6HZgaT2d3lilYMBothajmgzMYz3YdRRarWLn501Jue_B7YSJcu4Z-H5NJ8aLEJN8mY0Mv6Kx4LwYLVdcA6M_TbrmbIrRj7vbU3PzE0TMW74Bkp5_KdbygbozUYlVpKppKzuTpQL3aP-5kfYokMXEVnBLY4VoiTw_dHyarxenN9GAdlEaGBjDkBNLxPP_teWIroCjiX2F2kRFKFEMApcuThWnGbViD36MXzaatPJ2vWUL5zLp4oxaCmQZWaAlWquY9AX3ENVQzWsfVRdr1Vuuu_XHl7SUfU3-HKD2y5eA7p7fpPpwDHigghSGTheSWzfCbQBV5NyqKfKCYyG2vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/946a6ff60e.mp4?token=H37B6HZgaT2d3lilYMBothajmgzMYz3YdRRarWLn501Jue_B7YSJcu4Z-H5NJ8aLEJN8mY0Mv6Kx4LwYLVdcA6M_TbrmbIrRj7vbU3PzE0TMW74Bkp5_KdbygbozUYlVpKppKzuTpQL3aP-5kfYokMXEVnBLY4VoiTw_dHyarxenN9GAdlEaGBjDkBNLxPP_teWIroCjiX2F2kRFKFEMApcuThWnGbViD36MXzaatPJ2vWUL5zLp4oxaCmQZWaAlWquY9AX3ENVQzWsfVRdr1Vuuu_XHl7SUfU3-HKD2y5eA7p7fpPpwDHigghSGTheSWzfCbQBV5NyqKfKCYyG2vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوخی ۱۸+ «شفرونی» و کنسرت «شادمهر» در تهران!
🔸
در فصل جدید «پشت صحنه» گپ‌وگفتی دوستانه داشتیم درباره خبرهای ترند روز؛ مثل کنسرت شادمهر عقیلی در تهران، شوخی جنسی و توقیف «شفرونی»، فحاشی خداداد عزیزی، قیمت بنزین و تنگه هرمز و...
🔗
نسخهٔ باکیفیت را در یوتیوب…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/461620" target="_blank">📅 20:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461619">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0befecda34.mp4?token=YEgihGBrxRXYnz6eWgBPvORQafX1eIL_3QYK692O1tiVRsqFrkMUGTwQpGdw-eBJ8vnicQQX_Llfpc9OpTQ1uCepRNDwWoyL7r50jkhbQHCH7Tgwm2hE2o4T_3A9nr8f5Egr3nv4GxAIkZnfAPN0gAs4QfUFKRerDO5LueJUiCOCl5U-sPhfGpnxvjO6hYQ6ut4Pb5bk7aeYtlYpTjWMp6HiEDgDFbEWxvfnuPVruzYgoaVxKZwDVJTeI7CFsIm0YKxZtnVvOdqPf2xRPeRZu_brNLi7n8CsiL0OK48Syn3YEsart81lzVkpb7Y7NCbMVBqlnnbo91n83E369y1IHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0befecda34.mp4?token=YEgihGBrxRXYnz6eWgBPvORQafX1eIL_3QYK692O1tiVRsqFrkMUGTwQpGdw-eBJ8vnicQQX_Llfpc9OpTQ1uCepRNDwWoyL7r50jkhbQHCH7Tgwm2hE2o4T_3A9nr8f5Egr3nv4GxAIkZnfAPN0gAs4QfUFKRerDO5LueJUiCOCl5U-sPhfGpnxvjO6hYQ6ut4Pb5bk7aeYtlYpTjWMp6HiEDgDFbEWxvfnuPVruzYgoaVxKZwDVJTeI7CFsIm0YKxZtnVvOdqPf2xRPeRZu_brNLi7n8CsiL0OK48Syn3YEsart81lzVkpb7Y7NCbMVBqlnnbo91n83E369y1IHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون رسانه‌ای انصارالله یمن: پیام‌هایی که سعودی‌ها برای مذاکره می‌فرستند ارزشی ندارد
🔹
رژیم سعودی چون بردۀ آمریکاست خوی پیمان‌شکنی پیدا کرده وهیچ توافقی با او ارزش ندارد.
🔹
ما تجربۀ زیادی دربارۀ مذاکره و وقت‌کشی در مذاکرات داریم.
🔹
تنها چیزی که می‌تواند…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/461619" target="_blank">📅 20:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461618">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20b7792acb.mp4?token=DDUGGbbq2iPOk6wOlOthHC0i6gLKjBIyrIdUqL9EHKTCITqdB8c3zjfoPQ4bYnRuZY7UZg3DViZIpJCw6AEV1DLuxSIcWB2YpHDJYz5Wmlz_18H-hJCA0yEYlcv_OgTqeA0AK3ZQ_439B3jgifJaJtpCGs-CT8rwn7be3d3B4TVQNxYaZZJRV6N7ylGVHNtOa4Wd0LcJUFlymzxvKB1HGkGkD-1ibFUBoiNbhRJmz45TvrpiCOPkZuutJCLtRWQGi4gHzWd7cZvJOlw9mJXodPm5GrF3Tm6uSZGgNGfyimZj4SVCiyVBZ26lGU_l1RSF-DNObh29eFxidRk7ZSL_Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20b7792acb.mp4?token=DDUGGbbq2iPOk6wOlOthHC0i6gLKjBIyrIdUqL9EHKTCITqdB8c3zjfoPQ4bYnRuZY7UZg3DViZIpJCw6AEV1DLuxSIcWB2YpHDJYz5Wmlz_18H-hJCA0yEYlcv_OgTqeA0AK3ZQ_439B3jgifJaJtpCGs-CT8rwn7be3d3B4TVQNxYaZZJRV6N7ylGVHNtOa4Wd0LcJUFlymzxvKB1HGkGkD-1ibFUBoiNbhRJmz45TvrpiCOPkZuutJCLtRWQGi4gHzWd7cZvJOlw9mJXodPm5GrF3Tm6uSZGgNGfyimZj4SVCiyVBZ26lGU_l1RSF-DNObh29eFxidRk7ZSL_Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت ابراهیم حاتمی‌کیا از جلسه سینماگران با حاج قاسم
🔹
حاتمی‌کیا: فیلم موسی(ع) را بعد از دیدن حاج‌قاسم قبول کردم؛ حاج قاسم سلیمانی نفس من را باز کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/461618" target="_blank">📅 20:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461617">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYlDJd6vwoAgG36-udSuFfw1zyS3szdbHYo4Udwe8mmTKqEFkYPjUAL_S_pCmjqMiq3mkl58tP4G5bwPglpp0eeORkNF1gzN4uVxTy6GsQExF0the4mAQazMqWSgDDNyw2bes6XuOdaCu6Xpipd10Im8IfzQKnfKcz2-zU-AJQJfSpbLHHLby0bBNwABlUPSWk6emepfxmm2hTVo-eIzMTxvcG78A1JOl_jg2Q4EdoM8xC41_lqO6Kz5svn4AF1tFLNfqANY66hOg6iqYei64Lt5iJnxj76XLJWR_RWCMJnCKoHnDSdRcbow9GNFVPo4yl1nD338JXSduEWMYagd-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ۲ تن از شهدای عملیات پاکسازی یک خانه تیمی در سراوان
🔹
میثاق ثانی و مهدی سرحدی در درگیری امروز با یک تیم تروریستی در سراوان به شهادت رسیدند. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/461617" target="_blank">📅 20:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461616">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5458242bfc.mp4?token=lxF4rzzz3EInT8riTNox8VnhNSh7H54DhZmY2Fv-5uDrbNvElE08Igg8v0FcbgbwZmoyaoAkUDWFZq1NXFnP5DO3Ayt_VrHpwei-y_AAzZJVNhUws_3fMo5b26o8rySbEA8CN-ey6al4Uhh8N5aYueYLYXU-_26PftRPwY5CpYRqsVBspr5k-W0v8Rp_QV54fK7MCKm5Iuy0U9mhbFj8IxtAOQSyC892Y1dXqbiGkUJ97zQoEtPjaJwlsr4Jl-NoQPQM4YGwxWr2FAaNuZEoYtdCVpfKQKoznO7GVhQJfRsbYiYmt4yIDL0tkoD6E4xV7YVYAQ0iDOcKfWpTI-GaKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5458242bfc.mp4?token=lxF4rzzz3EInT8riTNox8VnhNSh7H54DhZmY2Fv-5uDrbNvElE08Igg8v0FcbgbwZmoyaoAkUDWFZq1NXFnP5DO3Ayt_VrHpwei-y_AAzZJVNhUws_3fMo5b26o8rySbEA8CN-ey6al4Uhh8N5aYueYLYXU-_26PftRPwY5CpYRqsVBspr5k-W0v8Rp_QV54fK7MCKm5Iuy0U9mhbFj8IxtAOQSyC892Y1dXqbiGkUJ97zQoEtPjaJwlsr4Jl-NoQPQM4YGwxWr2FAaNuZEoYtdCVpfKQKoznO7GVhQJfRsbYiYmt4yIDL0tkoD6E4xV7YVYAQ0iDOcKfWpTI-GaKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای خسارات وارده به پالایشگاه جیزان شرکت آرامکوی عربستان در اثر حملات یمن را نشان می‌دهد  @Farsna</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/461616" target="_blank">📅 20:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461615">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drd4gD5K6L3ybcfeO5u3SgBPBuaBt2JVP2EWaZlwJBdtihZxSVQgBEx-WPL8MHKi7C7Axe2toUHzYGPIkINdNX5csDPT6Zf3urCbDCeMlmzKVHG7POzvT4EL115GBwI3lSsAuPWi2Qndy_-AcMUZjAn4P0WPZZ8MDpwWjYHekkjFc5XLCK3dsEXzqEBUme6-GBqXdm9bjgTG4sJsWRhaWRKCmN7YTjUc8tdtAlWD-TPbP6ZUnc0Htti4ML9eXRFO3TiS1ba9uq1Fszd3cFoH3GLLkYlwSvnXxw5zP3CSe9L_CnF6wJ0t8bai2JJa0m_mZCAmvMgwNsO-nnm8ZpbAtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
معاون رسانه‌ای انصارالله یمن: فکر نمی‌کنم سران پاکستان یا ترکیه آن‌قدر نادان باشند که وارد جنگ با یمن شوند
🔹
البته آن‌ها پیام‌هایی به ما داده‌اند که نمی‌خواهند در این موضوع دخالت کنند.
🔹
به هرحال ما به هرکسی در تجاوز به ما مشارکت کند پاسخ می‌دهیم و هرکس…</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/461615" target="_blank">📅 20:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461614">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f8403a0bc.mp4?token=l4PSsT1lscKNFWTQSsYqnOJ6wUV9QwQHKc6vrAXzR4H0y5GoHdZr29XxIE7wjc0fqCKQ9uD6KdYA95_Rl46e7LMkcDe_aEHFHFzfDt-Ipk_hJNK2bQ0dvAe6cBPzbQ_O5NCTh87JF-Tzqw_WuMMr8EWXrGYlpFjfe4u3r7JsK4R4IfJuoc8WNx7R2YyNoihT0V2eTZ3UyQriUM_HGS8TU16L4kGDbGjHGMPmkuEKGMqe9jcTezH6dD_HCRXx68qOfH6JiqjkEsynyBYN_NzzKBOiCPioC9yuxI7-ibBNyrICcOSo5SpAGxuBXqvkKH3qiW1adcXP5nwaQyeQ3Nq-xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f8403a0bc.mp4?token=l4PSsT1lscKNFWTQSsYqnOJ6wUV9QwQHKc6vrAXzR4H0y5GoHdZr29XxIE7wjc0fqCKQ9uD6KdYA95_Rl46e7LMkcDe_aEHFHFzfDt-Ipk_hJNK2bQ0dvAe6cBPzbQ_O5NCTh87JF-Tzqw_WuMMr8EWXrGYlpFjfe4u3r7JsK4R4IfJuoc8WNx7R2YyNoihT0V2eTZ3UyQriUM_HGS8TU16L4kGDbGjHGMPmkuEKGMqe9jcTezH6dD_HCRXx68qOfH6JiqjkEsynyBYN_NzzKBOiCPioC9yuxI7-ibBNyrICcOSo5SpAGxuBXqvkKH3qiW1adcXP5nwaQyeQ3Nq-xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون رسانه‌ای انصارالله یمن: برای همۀ جبهه‌ها در یمن برنامه داریم
🔹
هر شیطنت دوبارۀ عربستان در یمن باعث تصرف جبهه‌های دیگر در یمن به دست ما می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/461614" target="_blank">📅 20:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461613">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dce34d6f66.mp4?token=ILYX7yplM7pvwq_H_ESMA7UhQ3g-ctEsWXv3OU2h5uhfvAw-cGps-83QzcsQdfgZM0hIgfhuCmsDG_kU62wbsKhZp-6bI78s7W7zgKy8IAIwRecmDqW-oRy93SF4rwbWgIpm5bI0kDrL3Po64fTMfPjCzmqnBl7OjrFPXZ35NOWHckiU1nexmlLdGZ3KohSnayEKij4w5HgH1ZPhznDHhdUef1JIiMo4ZdAkUn7LVGvV_6dNXeeY_6YtYYu-fqiCsjn-Wmugy8cCdVlM5axMmF89IVRrjTL3zNMBTBwtZlQ3tflV1_XSo-Mza4QXgieco5QMGmx-3veY-A3znC_jag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dce34d6f66.mp4?token=ILYX7yplM7pvwq_H_ESMA7UhQ3g-ctEsWXv3OU2h5uhfvAw-cGps-83QzcsQdfgZM0hIgfhuCmsDG_kU62wbsKhZp-6bI78s7W7zgKy8IAIwRecmDqW-oRy93SF4rwbWgIpm5bI0kDrL3Po64fTMfPjCzmqnBl7OjrFPXZ35NOWHckiU1nexmlLdGZ3KohSnayEKij4w5HgH1ZPhznDHhdUef1JIiMo4ZdAkUn7LVGvV_6dNXeeY_6YtYYu-fqiCsjn-Wmugy8cCdVlM5axMmF89IVRrjTL3zNMBTBwtZlQ3tflV1_XSo-Mza4QXgieco5QMGmx-3veY-A3znC_jag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون رسانه‌ای انصارالله یمن: فکر نمی‌کنم سران پاکستان یا ترکیه آن‌قدر نادان باشند که وارد جنگ با یمن شوند
🔹
البته آن‌ها پیام‌هایی به ما داده‌اند که نمی‌خواهند در این موضوع دخالت کنند.
🔹
به هرحال ما به هرکسی در تجاوز به ما مشارکت کند پاسخ می‌دهیم و هرکس…</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/461613" target="_blank">📅 20:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461612">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bbpq0uPmrHUpUVgAn4LfhnNRDnmNX-0BbSyGhzkIybZvA1KXqT25PJe8bQkne1Am0isBgctJKByyEzZkbV_DtBD_R3NYmNR9skjTRtwipTl1I121QYZK_awjLARssbQ2VY7RaTwq6SpO-JOlUPziKgAd53cH6Xegb5FWZo00XXkc-gyXBaqdtub8dwsGnGdJSQoXuOvHIl3OkhmBHlyiEYkexAXRDOFj1yF9qDR2b-9StXob4p-Sfh75r93sD4pppwrzDkvyju0mQYGI93btVN4aAC_DYfLgkAA1BKKhoTFrF8rmzrpO9k5mm_-H5Fk7ei8zMR5wGhgeNt45KmTqbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متکی: ترامپ تنها ۵۳ روز فرصت دارد؛ نباید با صحبت در مورد گفت‌وگو و مذاکره به او پاس گل بدهیم
🔹
منوچهر متکی در صفحۀ خود در فارس تعاملی نوشت: هم‌اکنون در حساس‌ترین بازۀ زمانی جنگ ترکیبی آمریکا و رژیم صهیونیستی علیه کشورمان قرار داریم.
🔹
ترامپ در شرایطی که با…</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/461612" target="_blank">📅 20:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461611">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5474caacf.mp4?token=plqjH4cphHNc2T6902pfmYzTwCi4PWABhJV9aGbx4uKe7BaYDYPrEtmwTZ5Ypy39Cg4H5t3YseS-MaGw5wc-LsLCSRsywRvl_kW2sqED4UdBvY_4S3dKt4VQHBLABYMzPYtruNnQfPl9HTY4mCn-FJNHcwB6b6aBR51sgQ9UeZFuNvSNibdxJZuYy8avu8XXWrTO4sZ3PyuvIJvOJFrjei_3SB66kUXLOC-U6VR4tzIH0DxtLCnxsdMOnDBExq1BSZJ5P1pmcgT4nh-PKMFBJbgi28HPI1-LL0IvvIaqDx2jMisBLlKpKjoCjYHLyWSqmSow5cA7UVvmDCDhquKgmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5474caacf.mp4?token=plqjH4cphHNc2T6902pfmYzTwCi4PWABhJV9aGbx4uKe7BaYDYPrEtmwTZ5Ypy39Cg4H5t3YseS-MaGw5wc-LsLCSRsywRvl_kW2sqED4UdBvY_4S3dKt4VQHBLABYMzPYtruNnQfPl9HTY4mCn-FJNHcwB6b6aBR51sgQ9UeZFuNvSNibdxJZuYy8avu8XXWrTO4sZ3PyuvIJvOJFrjei_3SB66kUXLOC-U6VR4tzIH0DxtLCnxsdMOnDBExq1BSZJ5P1pmcgT4nh-PKMFBJbgi28HPI1-LL0IvvIaqDx2jMisBLlKpKjoCjYHLyWSqmSow5cA7UVvmDCDhquKgmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون رسانه‌ای انصارالله یمن: فکر نمی‌کنم سران پاکستان یا ترکیه آن‌قدر نادان باشند که وارد جنگ با یمن شوند
🔹
البته آن‌ها پیام‌هایی به ما داده‌اند که نمی‌خواهند در این موضوع دخالت کنند.
🔹
به هرحال ما به هرکسی در تجاوز به ما مشارکت کند پاسخ می‌دهیم و هرکس علیه ما اقدامی کند به سمت باخت می‌رود.
@Farsna</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/461611" target="_blank">📅 20:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461609">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LIJCWd40pAmvmprhTABsALsCTNfMXjisSB3dWmq8fEkFaWoOynffgTzFE28kVN0Ob6a3jhHktBdKHG9NhCVynR33Sr3Djb0paCBU-pxvGkDmIk56AJ7hL1EpujDjQMW0fMqdrqfV_pAJFQwuxncbe20nysttCdl0Am-28DY_coZQPhq6bzXj-7_Slu0llFfq4_QYztGmOm3tdZDhuqyN_44dAVh84hW05QHXUZOw7sDkS_V2T0Ix43nAA7jlR_PCbxB7m94sxYWh26btJFksClLEAIWa8_19p_YhWlCzNGidlpm_NGp7VRMy91SqKlWeewnYYaq-wjRPb8-BQSpGXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M6BM4C_WKJT8iALR51ZIydxcicwBonjdjEqsFBKrhS_sDD5NMYWjHPIXBRk8luWzrf6-i0lCvWSkuLGc3CJJH-KQGMLP-Mv8oLhjWeAaStuGor_woXY-RrGDR_2LXBJRdSsa53c1l0jU3vfzR1WrqEinhuYKWicGudIXkG8qbwHybsGyV10HkIj7HiqNQKA2Yh93Rr7yiJ2xHiycntG_TRHdZ_UbtpDZU4Z94TP-5aSPgCSzt7RlOPtcyl_VQS6A329cQ7rLx7piYuZUp58YPO-j-7uD2AtSDjgluxC_r7QULdLMmXP2GfBtIRVBnpyVtZN_VUAoUKcbLJmT6Wdpkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز تنها یک کشتی چینی از تنگۀ هرمز عبور کرد
🔹
اکانت رهیابی‌های دریایی، منچ اوسینت می‌گوید امروز فقط نفتکش چینی لیسا با سامانۀ ردیابی روشن در حال عبور از تنگۀ هرمز دیده شده است.
🔹
ساعاتی پیش ترامپ باز هم تکرار کرده بود که «ما تنگه را کنترل می‌کنیم و مین‌های دریایی را از آن خارج کردیم».
🔸
اوایل شهریورماه یک هفته بود که ترامپ و سنتکام از مین‌روبی کامل تنگه هرمز می‌گفتند و هشتم شهریور ماه آمریکا با حمله به لارک مدعی منهدم کردن راکت‌های پرتاب مین ایران شد اما فردای همان روز سپاه پاسداران از برخورد یک نفتکش با مین در کریدور جنوبی خبر داد.
@Farseconomy
-
Link</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/461609" target="_blank">📅 20:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461606">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTwnX0HgfPd2YvW2Nmz8R_RMTVMPWZ2E7O-gdU9-m_d4-shgRZANew3M04RZ55nUqbotqQWANLoia0LIqEjO6euxPo4zPyvjmn_i6pJgZ1eOwRHJB8X0pXqrdCZaZvLMQSbM9nfkCoSrI9c3gpTWWpJExfi-rabr-OAXw9q_pwoSpLUPicAQlkJMBePM3J5S1e8PjNwDRtprgVxqYgtMeTBpdcoyRDZcTcdaku1Dg-FIX1-gjj67_GF0dcfdmZr-az5AaM-6Zb0_Zwrc9fhHwgs3aeKFczkbCuquI6w6Vna1l8WbE1tkzUiGnBP8ZKLBP2nEA6Xyy90mQbAn4NYtcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اذعان صهیونیست‌ها به کمبود موشک‌های رهگیر دربرابر ایران
🔹
رئیس هیئت مدیره صنایع هوایی رژیم صهیونیستی اذعان کرد که در جنگ نامتقارن با ایران و شلیک انبوه موشک‌های بالستیک، این رژیم همواره با کمبود موشک‌های رهگیر مواجه خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/461606" target="_blank">📅 19:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461605">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/516f875777.mp4?token=ARQFc1oW62WjQofAig3U3iB2weygCn7Qy4TJfDn9zyFgE6Q7S_ucMapgT6Y95o7L2MnmFKh6eXXUs91xfEDd8K0qiLnMhmeozCcY9hOd02WndIma0sne16Hc8Fidg4PmZMH0IJ7g0Ma7Pm2w5JGky9w04E7m949PEUWW6brNNmkuTGoPAtM6Xe7NNH5AoKqZEZrcyG5qI5zpwdTQV_injxQ0Ufk5rlTSUXCKfhnNzC8SWq46nHbG5bSizqzUXr5SWTVqWYOm2z_Dz1e3BchHbqh98L-rWS_KcYSm1CO7fnghF-qz8DgcX5r44NRUx09rVOjR_TAgMAjkiDT40S84AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/516f875777.mp4?token=ARQFc1oW62WjQofAig3U3iB2weygCn7Qy4TJfDn9zyFgE6Q7S_ucMapgT6Y95o7L2MnmFKh6eXXUs91xfEDd8K0qiLnMhmeozCcY9hOd02WndIma0sne16Hc8Fidg4PmZMH0IJ7g0Ma7Pm2w5JGky9w04E7m949PEUWW6brNNmkuTGoPAtM6Xe7NNH5AoKqZEZrcyG5qI5zpwdTQV_injxQ0Ufk5rlTSUXCKfhnNzC8SWq46nHbG5bSizqzUXr5SWTVqWYOm2z_Dz1e3BchHbqh98L-rWS_KcYSm1CO7fnghF-qz8DgcX5r44NRUx09rVOjR_TAgMAjkiDT40S84AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا خانۀ ۸ گونه گربه‌سان وحشی ایران است
🔹
از دل کویر تا دامنه‌های جنگلی شاهرود زیستگاه‌هایی گسترده شکل گرفته که یوزپلنگ ایرانی، پلنگ ایرانی،گربه پالاس، کاراکال یا سیاه‌گوش، لینکس یا همان گربه دم کوتاه، گربه وحشی، گربه جنگلی و گربه شنی را در خود جای داده‌اند.
🔹
این تنوع کم‌نظیر، شاهرود را به یکی از مهم‌ترین پناهگاه‌های گربه‌سانان کشور تبدیل کرده است اما در این میان یوزپلنگ آسیایی به دلیل وضعیت بحرانی جمعیت، جایگاه ویژه‌ای در برنامه‌های حفاظتی دارد.
🔹
این گربه‌سان چابک بیشتر در دشت‌ها و مناطق باز زندگی می‌کند و کاهش زیستگاه، کمبود طعمه و تهدیدهای انسانی، بقای آن را با چالش روبه‌رو کرده است.
🔗
برای حفاظت پایدار از این گنجینۀ زیست‌محیطی چه باید کرد؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/461605" target="_blank">📅 19:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461604">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc4823cdb.mp4?token=oV9F7_NJQS3SV6sO5tKWlKeta3jq5JVyX-_2m_HrwxKCenDX22iNah6Y_vJt4SXZvoex5rjilTFHucybpxdmGAl-XPVwvCARh84_a2xPh22Fifyd2HLVoMOoZmnpGaF51BeIbF0RHNZbFrPDp7XTtpJ3O8xBZhklW1N5Z1ISdlLoIl-7ahsQMERPJk5xufz9eG3uAaqK2ysMDp_VKElRzp_2gxqWEQpo3ghkjp2GZPLSh_aDwp1pxUcd29a4eGKAp39oATZ1bqliqIslFm79p6dfmXu63cb4v4X9ns6e_cvc2M_B5CZRUhPUHjH1J68UISKcUme5AHRZh0sEmIs8tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc4823cdb.mp4?token=oV9F7_NJQS3SV6sO5tKWlKeta3jq5JVyX-_2m_HrwxKCenDX22iNah6Y_vJt4SXZvoex5rjilTFHucybpxdmGAl-XPVwvCARh84_a2xPh22Fifyd2HLVoMOoZmnpGaF51BeIbF0RHNZbFrPDp7XTtpJ3O8xBZhklW1N5Z1ISdlLoIl-7ahsQMERPJk5xufz9eG3uAaqK2ysMDp_VKElRzp_2gxqWEQpo3ghkjp2GZPLSh_aDwp1pxUcd29a4eGKAp39oATZ1bqliqIslFm79p6dfmXu63cb4v4X9ns6e_cvc2M_B5CZRUhPUHjH1J68UISKcUme5AHRZh0sEmIs8tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از انهدام ۶ مخزن نفتی آرامکو در ابهای عربستان  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/461604" target="_blank">📅 19:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461597">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aZQANRrhIW32sp-lO_V9FyKxabnPS3XH4wrBiWCrSDLWADchiXMxF5W9NwULW5XqMpiKGguvMpOEvyJ9WAwPAb5qKUglqyDirb2Wzcx33GHySHhioz353ZyoLNuA3E_N1A2S7kInr7nF7uvHagnn0Pz5wfyQHXJ5WCv8BImxgpFRpKjhfPwi2qIFlZaH0UezWUu4jE5opzZ0Mk226-j--ivNzkBYa5uEGej0lKzjal2Ll_Sn82r3Yo-xnPXZs2K9L_v6pnJfbwTGYotIOCc6WNEmSX81N6-zCrXti2fT_tRYJFWAbs01TVPdgoNG3pQi79kAYjcMcxfHzvlqooeaUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cThdJJ-eFFP5TlyCkupznOaXe6UVPLJZaInIPJAU70uJCe0Scja22gZAqB78kpEKCsLpmAF94LdYpeKoAn5i94eNvqr0znCaIm7X3PNh6-hP1tiGBc6zIxOQKNDm8oo1MAXhhlYNOrA9ALySp71pvzdqDOhTd1qUDgNUmUAMYiY2G7akeu7y2X0J2IVsT1MMOIwnB1fUZb1ae1J5OIFNPxdVRR5zgn_rGmX4x4uc2yJEen1iV7sw4BOKTdLHZL5WXN23HcTiBJD6n3xT_6Pb3johKa1MRJ5mfn2FdeksIJdgihL35PQ_9wvJqnEsrGg2Ke8pEL-KwiLmshdx5JeNIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e4bT9s9K3Ewy-jIK8-a7MzebXp7bSvh7psyxzk7362-76BDpsRRTDdElZa8ExjYaUtkjJSkhMoUuC_MAb1LKwzMs2i5BeDLN6uKXHKFKvmeMYEI4FOdenZaVHF0kGbQg8qu6hnOQzda8OD1JJlW5YIR6LAp1qk8RkxBJPt0A1M5lYWOywCdcPrvv_GvUx7GwTVrP7FgkUCWFsKmY4nIXnnqsF_UC0mrVThRWxI7lP9CWik74Sdch0tEw2qqvtdvnYnKNQSkwDVh5veIKiAwtTcRoF229Zx3f5vBLNsmSpczkKAtt14AaKOQzOolHTmCieQ1w4RvZr55FD4OGLLVTVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FG16jrYNxrpZ4KAK1YWb08bI52x1_fmDjBjQy13F1QauJgcYPCjHZpqMSeb3myOS39wU_rIJS9dKYpXhGeeioi5jaYbtWKXohI7pfolC5KrrOJRCSbq69dEyfryA6wXK0DnnRAl73E6MnZjGJH_bMsTMs_M0nT7pRw6v68DgdGGZRU-Mvserx8nP-QOMv2M7GNBjn4CB5sb7-NmR_v011AUlZNWA99jI8uu-SWClbArYYHH8Zd15vQXMdh6HsUOWn4S94T2gDBk18dDKq9h4k0mJvnS9fdCWneMKbok5cptrl9iDtNXNdq9A25RnZJbjYf7cM7yf67b3ZhRB-XBuUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H-Q98jYbKu1Qb1KxY0G9Ej-SdmsV_YKeGCPQ00ioS56sd88S8WsFDKFdalJ56TULJH92uFbeSVnoeXn1gfVamOX_ENLCVSOxOsjG3pPROo5WpshQoS6L6qUJKhbF3KDtaPG1E6YqJ7Lz4C93dp2U8ZEzv_Xk0yp5VOIDdzMPCY-DoJ_p1KPUkQVvOW6F1sBZztuEEqHEVye31syTAmCLOyeVM6ZcHrCItJwOPnhzGabpQa8bITO4fek1yvxY5cd6EcAl0M_dOzsdEeElnqcsVCgrls2OrjXylPiW8Ln0AOpfv3WafYe5OhyLi1JX1ZQobDWdv6tGCbez9B56meT5Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDYNON_-iZmK0lk-QnbLW4teMA5TFtDTqrck9eBVuIwy6N1dv0WnIDlozPmYAw8ch7hQW43yPe43nsUqklnthe9D-dfIXJA50lX16XwOFprCyRTpyouau_k9y7V8RnT6Dig-6BbZcIux955A5JpW1jt7h4lphIO0JAhKWbV00RADOFXpYHlWH8vgxu9Gpa9iiopbafK4AsF9aeM4QRhCA89PqnIB66-usymVwvP6eaS-fLkO8ZUh0Eqck0UyA8uT7QRgUS8GTDnOV7Od1dkOpkPhG_vypLlN7eSaRKjbb92jqZp_RS8lAzl-eN1XYBSl4RnXvBONxweTDzsPoqCCNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eu4UfaVTf_GYmzyzGFjOICje8SxHEE_2EZ2Lwjye6CM3fgayULtL6eAY7I2328NtmyIuPmABpTbF5m--sx_J3MG-RfKrOfup-uP9TPmsPkN-ys42L7cADX6vF7dc8nS1UlTAQYNqe4ar328DDbqOjVNk9Cq0HfojjYPK_HpBgJ5zGF00oqZ0XsiDPM8reUJndFWBQAKA74pahaJWZ0iGgmuOM0silCQZ81Fp3p13c7vOnSuM61lNenfhGMFKC4QbxUFTiTnrX85vFoPSPIIZz4ge_1G6SuoP9YMaTrkWBRbMTraailCeH6q9JrzahbmhsOBVyDUzrF7nTH_cQywfdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جنایت آمریکا در بندرعباس، از میناب تا کوهستک
عکس:
محمدمهدی دهقانی
@farsimages</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/461597" target="_blank">📅 19:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461596">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وحشت موسسۀ امنیتی اسرائیل از تغییر احتمالی دکترین هسته‌ای ایران
🔹
راز زمیت، موسسۀ مطالعات امنیت ملی اسرائیل معتقد است ایران برای دهه‌ها تلاش کرده تا به توانایی آستانه هسته‌ای دست یابد و درعین‌حال، از توسعه واقعی سلاح‌های هسته‌ای خودداری می‌کند. اما دو حمله آمریکا و اسرائیل، درخواست‌ها برای ارزیابی مجدد دکترین هسته‌ای را تقویت کرده است.
🔹
زمیت می‌گوید طرفداران تغییر سیاست، استدلال می‌کنند که فرسایش محور مقاومت، محدودیت‌های بازدارندگی موشکی و آسیب‌های وارده به برنامه هسته‌ای ثابت کرده است که تنها سلاح‌های هسته‌ای می‌توانند بقای رژیم را تضمین کرده و از حملات آینده جلوگیری کنند.
🔹
به گزارش این موسسه، این تصور در تهران ایجاد شده که دارایی استراتژیک اصلی این کشور لزوماً گزینه هسته‌ای نیست، بلکه کنترل آن بر تنگه هرمز است. این امر ایران را قادر می‌سازد تا در کنار قابلیت‌های نظامی متعارف خود در حوزه‌های موشکی و پهپادی، بر بازار جهانی انرژی تأثیر بگذارد و بازدارندگی ژئوپلیتیکی با اهمیت استراتژیک ایجاد کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/461596" target="_blank">📅 19:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461595">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/173f09546c.mp4?token=kqWUDATXqqnDYh1iqAtdWucWmNlCiR_jwAY3_xqRDyIGvPqHAmsLatdD54SgYP-V4Yk9XP8PwhGEerHlyUn3H3J2dQqeAMywcWbYFBfARYkv8DBZLtkNjWPGd2sKUsMB2urpqqNi0FWlinoJAoww8mQjYQ01L5OQPTU2IVzrIcAZZ_P71fHe-Z2cLdSM_4PqpAcRjGuRUVzuMLOz0FYP34V6cpt4cKzJTuiodnym2kAYsbDWqiKq9bauD86VSfH0tgfthrDU-t5kaYIR2rwu_SrruAfcAO5lfQkLI31XRZUwPRjAd0HLus0qJFRaQmGE9MK_glR9hZ8UQNWkb1l5HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/173f09546c.mp4?token=kqWUDATXqqnDYh1iqAtdWucWmNlCiR_jwAY3_xqRDyIGvPqHAmsLatdD54SgYP-V4Yk9XP8PwhGEerHlyUn3H3J2dQqeAMywcWbYFBfARYkv8DBZLtkNjWPGd2sKUsMB2urpqqNi0FWlinoJAoww8mQjYQ01L5OQPTU2IVzrIcAZZ_P71fHe-Z2cLdSM_4PqpAcRjGuRUVzuMLOz0FYP34V6cpt4cKzJTuiodnym2kAYsbDWqiKq9bauD86VSfH0tgfthrDU-t5kaYIR2rwu_SrruAfcAO5lfQkLI31XRZUwPRjAd0HLus0qJFRaQmGE9MK_glR9hZ8UQNWkb1l5HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از انهدام ۶ مخزن نفتی آرامکو در ابهای عربستان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/461595" target="_blank">📅 19:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461594">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKHpnfgCghFVG6z-d9RYVYfTwAU9oPta9xNNs6sMMAwQq8_UBmXD6yL3E5j2f1nLbeGLawap0REChFL08wG852fsUFF_0zj8igCWF0poLUyOXowWHYiiIm8rQI0Zxv-vfMv2WjHG0ZpgV2i4javQQUkxXs2AGYLQ1irX0z00f_5MHoBhgA3nNcL-3X4ElqooH94tiqEQl4mG9K28AWh7C_XPziiE60YPQApj77NAHF3Dz1EBpqmk2tsgt0GuPo30Cn09HMyvMLwcjdruzFFQ3zOJ9LKDLmFaH_3EgWp59yh3wl8kp4QOJj6G0RNdnLSDI0kGGBzQMRSA-McW3kf-Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
جبهۀ مقاومت در کنار ایران
@Farsna</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/461594" target="_blank">📅 19:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461593">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFMPrHvrROkty872bnpDyP6gHMOesApUWqR9X3OMmqNv_tTuV6ejz1IQssC_NXIZWr0F2E4PggJegM1QS3AcyZT0o6Cv-kf6-IlwJPeXxc-dsxq8718GID_tWafghGqWQMAuWT05vtmlj7udCjaNI7la9t7NiiiBUeQ-lynKwPUILRwULu73f3By4vVSMMBzp3qB0aFwSCLfCsdgdMe5-kvb3TcBsxwJrwXdsTykO7unGXyoX0gZIEWqL_ZxV9hDoKh1oBQIJCZFzowV16JI2WfPLe6GBtBOlBsP_Ctpi7x3wyoAg3YxecLEz9S8aOgIwHLgm5mMSr-SfHo7xfIOeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر خارجه: سران بریکس از درخواست الحاق ایران به سازمان تجارت جهانی حمایت قاطع کرده‌اند
🔹
غریب‎‌آبادی: این حمایت صریح در چارچوب کلی‌تر اصلاح و تقویت نظام تجارت چندجانبه و افزایش سهم جنوب جهانی در آن مطرح شده است.
🔹
محکومیت حمله به تأسیسات هسته‌ای صلح‌آمیز تحت پادمان، مخالفت با تحریم‌های یکجانبه، حمایت از عضویت ایران در سازمان تجارت جهانی و تأکید بر حاکمیت ملی کشورها و حمایت از فلسطین، از مهم‌ترین محورهای بیانیه پایانی هجدهمین اجلاس سران بریکس است که با مواضع جمهوری اسلامی ایران هم‌راستایی دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/461593" target="_blank">📅 19:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461588">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W1VjSDCTuI5MYSN6RV9gPgu5nTuxlgeBS2YgcGfrRH-wUX-JHDoITFkT2SpIif7kQTdmYTDV7PRFoohKMRg9aVEypmZuKviyOYk__4nT6zRrFpd951jvNEhm6CbRJa_tBZE-3oMy3h7YW2jD3AYbysKMzSQopLZjzWUm9HMrK55m4DS0i1QowJBcBRqwHSj8pLdKGtQ7U-O3Bc0oQDtCQbNXwN3ksBKIRm8civgLAhm-BR-o5UXoBdTua9EwPPouSGxskS8wB5b8keGZiI4eY5GOTjI-QVwJA5n4vw3VFyHqXDK8v0aPRlZ7hhBinl8l2G1JS66gAuAS60rQFTs1Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s5fOVXbgwc0OVR6BZhJ2McVxC4qnnRrGrvPTNXB5yfV1_C5GkWs-xeiEucdYNpjrb8IAUpM-F8wOs4Mw-9JJOqlm4_rS8QNopCAdCj8qEMOQhDHni1InknFBD64WnHmZVredXaDsAUY8Jh1qL49yRFUGzIfEctRiQHNH6euF9RRh8hnBxIcmu29w2TAc2YDxqeOCTbC5zasQjmPMj-eGO2DXtZPt7QjbJqFhVKzAXKeAmJHSLrzL3Etvu5PReR4s-nNv1dCJ0I3KJExEeZZeRU4TZX6EMP6Q7nMJaznrGzf3GemKJ5IQR3OsicCl6Im2HxalknMP4aLiglj2Qadbhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o6fICJT2qPwDaU8Fmf1Q1IIQknO5AWKXbyRQdeBkBa3tlTulBZKWd-wbqLP7XcZfjf6e5G45Q01iRVGqVUc-ngpEZqUjhczvqulJ9eO3MAkhjCpp3Z2UwZR38qOiIzKvkyUPTU_ac2RmN75DlbDs6zmbaNIGvSMkbzqc45aVhRTuGAaRCD2WEIwV0RCd2Weqm7wxHMALIuhLDeAg9uKOi3bk3vFmSrX97qXgXHvDvtQHJhB24zF6oSydSDzPSiupmhQE2-kf5LUgQWFcKbGSLiqTTd-EOAaEaf4KmH_hoHr86inDYK9MH2HQzkJJmTy61ahtNkK3Y07PGvWyf0glng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lYGMrkyqGhtq78GxEAScLXKY2-4ZR1aDu-M66ClQaoiuj7TKiIRhC1YlOc_EfrETiUysoQiJ6VWWSuTxGzlgwtu_B8zEgD_oCzmqm72Zv0P2TATrUNgxbQAkriyDspkOWKCTu699vAeVoKMbo74T9JehRa6kUqA_TrDUHWzR7AOOvhL9h8qxGNLyojgvgXFbj5XCQeU1QkiN_Aaucg9z2c_rs_UWvF9vHoKbWWk6Rv_Ln570orpqheOSsy3cqcdzwVKtbaXoh3eHX0XH6Ao8rtlEtNCJ80NlfskvVHNeDLwxpgFMfVhxelX1eBpxwjAxXc1k65MGjMShgENqNdFFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SurIrjYN1VcSlALSXn_5MxF6oejzFSQRA-_oBYsonnEM8lK1Y6Pyw_GAZ18RXOOfYcDSUdb0L72Taw6bq1upHM5a7i_d8DHKDFDXj6hKGbOewZfEym-Nj0v5HGgE7oiPnJxatf-NqSyLqOuwFi3HeocsLkCV9V8mUIDlI5vmUrDvf-2N7RlHNvjIg_-FTOTgxx9c7oB_1JnkVonV6Kmcj05kRplPwjT0OWkug2diXr1OPpU6nmUrEDYLlAt2H4WNvH2rv-h1CyPx_ioUrVhqDTQLf-s7laslJrGhBAeUpL_u3D3URRh_NYf_yHgrm7fyxJM3_b5soCYuOwietCDmXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⬇️
همایش هم‌اندیشی مدیران صف و ستاد بانک صادرات ایران برگزار شد
✅
تاکید بر ارتقای کیفی شاخص‌ها در بانک صادرات ایران/ افشین خانی: اعتماد پایدار مشتریان، پشتوانه اصلی توسعه است
💠
همایش هم‌اندیشی مدیران صف و ستاد بانک صادرات ایران با پیروی از شعار محوری «پیشرانی شعب، هوشمندی بانک؛ ارزش‌آفرینی پایدار» برگزار شد و راهکارهای عملیاتی برای توسعه محصولات مشتری‌مدار مورد تاکید قرار گرفت.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#اخبار_سایت
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/461588" target="_blank">📅 19:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461587">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اجرای ویدئو مپینگ بر دیوار ساختمان بانک ملی ایران، شعبه بازار تهران
به مناسبت نود و هشتمین سال تأسیس بانک ملی ایران</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farsna/461587" target="_blank">📅 19:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461586">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/461586" target="_blank">📅 19:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461585">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb1af6713.mp4?token=H-YJCQhVPUSvuN7-Xw8eEmCt8jZ2QRa1CLbCm3So7CsrcQLZlynjMtiTkqfI8Z1n7JjP9NOyFfXuzvH-e2YnRJ92MFl7I3uno25CtokUPtk2w5UFeTDv6N3HF2TYG1oCeQ3GAJrmxVPAc_xMURWPI6isi7Bwl_bPEqu7MzaSv0OwW1BKRgiw1p8eEYCZzc5kZUlDmaLh0G7sBav7l4AJSEij5iXeEwekB12C-7o_VtDslnQLSXPlSVsM22l6nmD6Ger7u58mrJQV7nqJrmpyTfMLrp8oD5RtbS0vhmQ_08ywgqB3QQfpb4oLmOPLekupLh1cxSwWDj96CQna5QxB6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb1af6713.mp4?token=H-YJCQhVPUSvuN7-Xw8eEmCt8jZ2QRa1CLbCm3So7CsrcQLZlynjMtiTkqfI8Z1n7JjP9NOyFfXuzvH-e2YnRJ92MFl7I3uno25CtokUPtk2w5UFeTDv6N3HF2TYG1oCeQ3GAJrmxVPAc_xMURWPI6isi7Bwl_bPEqu7MzaSv0OwW1BKRgiw1p8eEYCZzc5kZUlDmaLh0G7sBav7l4AJSEij5iXeEwekB12C-7o_VtDslnQLSXPlSVsM22l6nmD6Ger7u58mrJQV7nqJrmpyTfMLrp8oD5RtbS0vhmQ_08ywgqB3QQfpb4oLmOPLekupLh1cxSwWDj96CQna5QxB6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بزرگ‌ترین عملیات پرچم دروغین اسرائیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/461585" target="_blank">📅 19:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461584">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELDP1dXPLDa0Lc0hvmIlIVReFnkZsINwRW4Xoqq9flDym7aJQXfbzmNn7zXNsuQZ_P8tgh4Qo-ebaJedao5vZ5Gl8rxWow19rCd8SFEvVcyXif-24E5-edD-qeaJfEs-6bDHqX1oN9Zpd7anlXOHDB9OWUuc_yGBcvFHsZWj181ow9zEtLr7bX8ziExOsOabWelajX5w21TXTNMRpu1e-6fRdXyiohWauNrbbHKjP_qgGTOAIfILNUr1Im_nEwIOSspXFdjajqKhYnx30zCRKHQfGuz6wEK8sgtoI9RpvvlgRHAUERawcugorCNt79KfPYGZ7_S8LhRi-R1Ejyriew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندیشکده آمریکایی: جنگ با ایران معیشت مردم آمریکا را سخت کرد
🔹
کارشناس مسائل خاورمیانه در اندیشکده آمریکایی توضیح می‌دهد که جنگ علیه ایران، تقریباً تمام مناسبات داخلی و خارجی را در آمریکا تحت الشعاع قرار داده و با توجه به برتری میدانی ایران، بنابر دلایلی که برمی‌شمارد، نظم جهانی جدیدی که در حال شکل گرفتن است، خارج از دایره منافع و اراده واشنگتن، تعیین خواهد شد.
🔹
جان آلترمن معتقد است که جنگ علیه ایران، صرفاً یک منازعه نظامی یا ژئوپلیتیکی نیست، بلکه پیامدهای آن به شکل مستقیم به زندگی مردم و محاسبات اقتصادی و امنیتی کشورهای دیگر سرایت کرده است.
🔹
از نگاه او، تجربه کشورهایی مانند هند و امارات نشان می‌دهد که تغییرات ناشی از جنگ، از اختلال در اقتصاد و زنجیره تأمین گرفته تا افزایش هزینه‌های انرژی و تأثیر بر مناسبات امنیتی، باعث شده مردم و دولت‌ها نسبت به نحوه تأمین امنیت و رفاه خود تجدیدنظر کنند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/461584" target="_blank">📅 18:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461582">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‌  بقایی: هر کشوری که ناقضان حقوق بشردوستانه را در قلمرو خود شناسایی می‌کند، مطابق تعهدات بین‌المللی موظف است زمینۀ پاسخگویی و اجرای عدالت دربارۀ آنان را فراهم کند. @Farsna</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/461582" target="_blank">📅 18:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461581">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بقایی: پیگیر اجرای عدالت برای شهدای لامرد خواهیم بود
🔹
سخنگوی وزارت خارجه در نشست خبری در محل قتلگاه شهدای لامرد: در این که جنایت آمریکا یک جنایت جنگی است شکی نیست؛ تحقیقات نشان داده سلاح استفاده‌شده سلاح ممنوعه بوده و موشک خوشه‌ای که هر کدام حاوی ۱۸۰ هزار…</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/461581" target="_blank">📅 18:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461580">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۳۲.pdf</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/farsna/461580" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۳۱.pdf</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/461580" target="_blank">📅 18:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461579">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puafVb14JyZ5yY3Rd6gpPlT2f6ioJvnOcz3ll_05AiHbYQZIGZTZF6oqyi-DRHQa4BOhAb38rOiwCQndaDS-zVrQMId2gr7Jq7jyLUBYRrLr1oca4vM3WE4QB-nmqUdSFbshL9xBbDXITyydBzoccGUaW475k4B53bM0DIi4J75jFbMk6fQCq9e00jvA3k1xhVd_UWaAyyTg4g8r5yLRMbyu-tlwMoYK4Cl3L8uDSt2waOYVrjlpNuEyUXFhih-Hv1ls_uNvd6AlwovaNAFJtajfXNuZOEW6hpb89LQClq7__Ckk7a6K3A3TwxGSvv4hB34xt9SXfDr6aAlJVU2Meg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ هلاکت ۴ نفر از تروریست‌های وطن‌فروش در سراوان
🔹
قرارگاه قدس نیروی زمینی سپاه: درپی انهدام یک تیم تروریستی حرفه‌ای که قصد اجرای عملیات ترور در سراوان را داشت، ۴ نفر از این تروریست‌ها به‌هلاکت رسیدند.
🔹
همچنین تعدادی سلاح و مقادیری مهمات و مواد انفجاری از…</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/461579" target="_blank">📅 18:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461578">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pngbso5VdP5KP_61DFOFe22rfOKhFZK4-PWNzE6BkYIMcbANucSMftxhFWGDkaZf78qBAeahCj9n3iy4Q_6gPQ4GHtzZS_6ZRI4fga2XWyXsVn2DhYWMxSpmG0hpDU827naovktnkIBeT06C5Sog1_t--rGN_DZrGptt0zj_Tamxuj-oPsa6rUP-syeesIVcW2MG0lBpxTgdGlp7LOf02EHB5hD0lOpNSP9WYw1nJVqF8AiZ1d5Pz-g3kU0Ht7sZ5rz6fGJxyH8fu3TjQOwzRmg0jgd_ejDOYkLbX0i6hrZlc3eoxBH1HYTPe2iIREWsoWOSEw9C2dVZYMDIwqlwOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلی ۲۵ روزۀ لیگ برتر
🔹
پس از پایان مسابقات این هفته، لیگ برتر حدود ۲۵ روز تعطیل می‌شود. بخشی از این تعطیلی نسبتاً طولانی به دلیل همکاری باشگاه‌ها با تیم ملی امید است و بخش دیگر نیز مربوط به روزهای فیفاست که از ۳۰ شهریور تا ۱۴ مهر است.
🔸
تیم ملی در دو هفته روزهای فیفا قرار است ۳ بازی دوستانه با تیم‌های ازبکستان، روسیه و یک تیم غیر آسیایی انجام بدهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/461578" target="_blank">📅 18:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461571">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qxs7qGFA1kVEdIk5icQQ4OG-wtfI42S_u50y2IZ6bwDGQYPHf06esvYBMke10KuebYbOVzfB9N4st4FJ-eGRkuLTQiCPGTNLOuUSYpaWsv3pOpUHWH2ZR3mXMClFmOmJhgPA2G00leUW3EnsQ2mNY52kIIsnKQRZnzadjS1lk2SUTUmFhrJPmF1WyIFdS_q-mZZK9J6Exjlpk17vB4rp_lUCsRL9qjn673SlFYyzAs1LBbN1Pm9frCC5i2t29olQQ1zgw-tNQGh4NY437vR9-mypF--tHcjOD_-FO9S5FLRM0JwoBEjmOQATWPnFU6MGU5LON_i2khzFwpK8b9n0CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kwhl07bnNvIPS5YZ3miFCYLUJxRLndyxIbBUu_-qWYyuysBBSYyIRyYsjimiL-QEo56ETqsCBC1VZcAPuREaKilNew6zmpE2mV3-FmOYp7_XdoYIP2nH7twmcrl1yy20H2FB-ep7VBZ_VCPNI_l06FxaapimAdfe_XIc7wrXC9x2eebqiWGetRRzuXO0g5UR8-7FpYQ4EtCoM0x-dgndH_vS2bMU6UzbtXQpl5O4rtyF1yVUaXBc1zK3I_8o9ZGgLIxokj_91Zs-DnvqaRT7VIVKQtYyCqL_2yxOmyRAMSEpJ_lKkCWx7Abyiq4jZPVrSNfZoca_dFafcmiNactJWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cGujuCSQ6Ud7j3EAxE_my8n5Eszs_HzVODJmfs2aAflCKrU1BxCpOPS0E6jCmlUxHXIVZ9vp-YMbSb4QrRc1ql6XXvAFIBwS5mtHjbg3RrrUumQ4wxe2F_kAq99vGofsjlF2wGh5OtRt_vtep-DsAESNwTrtUKIli2PAnQFLjqy0o8Emfwf_NneXk7NPrAG7gzFrj724wGVJWblAqhwBIUmOlFmao5fyzuzbPjsvYm2-SHF-Q-n6GFk4a21SGeVhTB45ENmTDRPAntsXE5lCsoej05Z2vUU00R17KxuciKsEAVC0JXDJs0XXvAQjdOyqOLENKYvZcoGf06AXkxuttg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i37G55d6PLw_Wci-GXmj80YMXr3s5GylCSwP5Ua8LjoGqtpRV5nsINynIMkWteXC368y3ORtapriJB4Oj3lp-a0JllT7wgI3xdFrPSKbiUj-Vt_HFbgHv-5H1IpdmXFQv_ETK2g4TN4QrMdIL4zMj6cZmfzoUa7qxjVYV7z9J3BD7x3zPdNJZAQvJ11pUOmT30qqP9cZzq8t3sg-NzVWGAD8NauqaLCFlx98UwD1syTegn-IetCa3Mmer7ChHsoWTZmbAon2x48SQRa_CLC3Q5z9YznH8gj9danBaOhl_mIdszQVcf8lR0_BB4rO28kNX4CISRPtzCzTar3uYT9g2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LfZjLA0GnBpOymCyUvxZ-eNlN9ydvHxzWRRhFVhH3N3ZtqHsGsqG7uPkNgcJ1xYqB8IfjAS-LYMcoYNAbO9OVVjkdNJtnTOkIAg4chxpolLI015V9u35BKWIOkfT9VLT6Z9cg1A674j8oS96dQ1hjSjGZaw6aU4eH4NTlXNLfIV6G-Wp_GKvt68zmG3qsnuWP_cL19kPbj7mcBcCzb6iFSVJI0PAliMpTALgss8lN2vTd43cZ8MIuSUoqTqvhjoR3dKbtK42f-SN-j6zUP_xE33k_NkiniAaTYGJAycmM3ftAqpnV6fmP8_tDgVuzPq93MSkNd5WVmjtrInltR0e2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cc_-QW_4CwSky743miSlCuu81Qc1hLLb749IBeNNyZZ4g17bavHt-BjJZKsIbw6Bjs38VomcvveeYvbAaLgLuZtah1104BI8s33QENd8UL3i80aAY8_JsEsrvJbuYwo3RSm-ndy463CW-7Z9LoZN1peAeMf0KwUDl2k4mPLNAi1_222fd4urjpITkys5Id77hUPCEWdzRZCdyZa35p0lYxvavS-NiSR9mRuq10XdqtUXKtr7Bay5mkn_Rbyo5dfXkXwO3XXMxTPwtca5QDAzNNw9pSwIV-QbJRuJKoOkoAYLwEjzTbXb1jyyAP3cLz-1F8GlM3CbQZuY1YaZvGPU8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ACd6Atkv--g9L5owcZwdGcBx5XEBgF13Ke40uVODSe2TPV_2PGPkeKLvMQfdjO3CVy9kfWHC1j4aBkHHnkRBlJ23RYIOlyl7-hU9p3-cImBBVA66M2GQ1bzY4vfd57lvoQkSJvtXP0hk1cCkrCiuPqYtvXzx_-0EFzBCaMb_wo4Fjj6PPPYc0BxR3g4BpJw8ANFN7VZMQM_1LCgnD_lCOVaNHs0-Uhke2lZjdhaSKwKjX-bnbvX2WkTUjOYd08gKo7Em3MyEl6x8Lbe_Bm2yiqL3HTt0tCom4fZyIN9TbYP8Gite_t3PDNuO5vGk9ve5hoVKapu15zH2mqj_VyAPWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بقایی: پیگیر اجرای عدالت برای شهدای لامرد خواهیم بود
🔹
سخنگوی وزارت خارجه در نشست خبری در محل قتلگاه شهدای لامرد: در این که جنایت آمریکا یک جنایت جنگی است شکی نیست؛ تحقیقات نشان داده سلاح استفاده‌شده سلاح ممنوعه بوده و موشک خوشه‌ای که هر کدام حاوی ۱۸۰ هزار…</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/461571" target="_blank">📅 18:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461570">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqjVkrTjoEjPSQRzb6SZXozHonARmbjqo5wMBEtT7Z2Sm0vTH7ok384F6fAks54WnFQbZ3O1idT7yPsysLDfu2ki12irbCYHELZhxQCmMlRYoLajplrnfEOjQnvjDrXHNWa593SZUHgWvi7ZAK6iEGA1hLOVEMLPVyAbphC82-s3Z-Ho5HvE6YMv0LSNl5hWaizAbfl2V1RyOgsjKr1nlc_0uAA6xZiT2rgWr3lxpdUFDSE7ZAtcEqp35rWjVhh17KifOXRM6fkdWK1jxHug8p37axWutx6saBpkR6AWkQh2B7l4o2m-hCFeVFNLopfA_3CO1Z_xQf8bdppGsoY0LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاوروف: زلنسکی برای مذاکره با پوتین می‌تواند به مسکو بیاید
🔹
وزیر خارجه روسیه: آماده مذاکره با اوکراین هستیم اما روسیه در زمان مذاکره عملیات ویژه را متوقف نخواهد کرد.
🔹
رئیس‌جمهور اوکراین می‌تواند برای گفت‌وگو با پوتین به مسکو بیاید؛ این خودش یک حرکت بزرگ به نشانه حسن نیت از سوی ماست. چون زلنسکی فرمان ممنوعیت مذاکره با روسیه را لغو نکرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/461570" target="_blank">📅 18:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461568">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgL1bvv5mYxSKw6EPB0Dlp6L3bvzE4gBRBLaJJGiAn3Mt8mowXxJ3CfPLQLiWfiAdvz0DnN7LAVbary19SBXqxYovVC_3OScuhNmNtnz44NoSxXi6s33YsGX6RVQ6ZG55vWB_v1sVkzzjuhcRd8KM2Ac-NhRpu5dj6r3FZqTnFKm90N3lAdtwxXhmFXc1zqKOIxj0rWrYNk8MZJw89716KLbRCIdZzk1VMD836kx2DkivLxuIVyYwcNhsHn7BUtjSfGFAb8APVqA0rMEpq8vG4XQkpSEZ2AWr12uPkIti9pn42eDg3q1twtLABXeAiN_qAyK9Vkoa6RQ_CZWyFmyHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقایی: پیگیر اجرای عدالت برای شهدای لامرد خواهیم بود
🔹
سخنگوی وزارت خارجه در نشست خبری در محل قتلگاه شهدای لامرد: در این که جنایت آمریکا یک جنایت جنگی است شکی نیست؛ تحقیقات نشان داده سلاح استفاده‌شده سلاح ممنوعه بوده و موشک خوشه‌ای که هر کدام حاوی ۱۸۰ هزار ساچمه بوده و محل‌های مورد اصابت همه مسکونی و غیرنظامی بوده است.
🔹
چهار موشک در فاصله ۳۵ ثانیه شهر ۳۰ هزار نفری لامرد را داغدار کرد؛ ما به جد پیگیر عدالت خواهیم بود و از هر فرصتی برای تبیین این جنایت تلاش خواهیم کرد تا جامعه جهانی برای مطالبه عدالت برای شهدای لامرد با ما همراه شوند.
🔹
آوینا، شهید ۲  ساله این جنایت، نماد مظلومیت مردم ایران در جریان تجاوز آمریکا و رژیم صهیونیستی بود، ساچمه‌هایی که به بدن او اصابت کرده بود چنان عمیق بود که بدن او را پاره‌پاره کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/461568" target="_blank">📅 18:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461567">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18190f11ba.mp4?token=RM_8KpjN7YSzaCF2PgKdo8I-JG8dqf4H9FRd7Ss7pN1wmpgC6ciI8kOTCmPUwdKsI9gWgCP7EtrdWGW7zyxu7w1kWeegNuX8LMQBNhowXhGOOzUvlBS52H3OgbBW1SgH0nuN2mEqQMsMGxFLq8ZG83AQYwW0cEmC4_7Xf2fZoyjMXg0JclZevoAKdSg1dj_ckBHsd93S5PaRIHIjE4l65jjaAliMVNTts16u5YKQ3FNtj-aggE5ID23wCE2qCEeuMDX9fQ5EN-b93RpucViecEq8wPjebGJrSJfF3cbadGFmcffQncJv6Z0oeaybVf8dJKl4aafe5Ki4smvUGn8Pvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18190f11ba.mp4?token=RM_8KpjN7YSzaCF2PgKdo8I-JG8dqf4H9FRd7Ss7pN1wmpgC6ciI8kOTCmPUwdKsI9gWgCP7EtrdWGW7zyxu7w1kWeegNuX8LMQBNhowXhGOOzUvlBS52H3OgbBW1SgH0nuN2mEqQMsMGxFLq8ZG83AQYwW0cEmC4_7Xf2fZoyjMXg0JclZevoAKdSg1dj_ckBHsd93S5PaRIHIjE4l65jjaAliMVNTts16u5YKQ3FNtj-aggE5ID23wCE2qCEeuMDX9fQ5EN-b93RpucViecEq8wPjebGJrSJfF3cbadGFmcffQncJv6Z0oeaybVf8dJKl4aafe5Ki4smvUGn8Pvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کابوس نفتی عربستان به حقیقت پیوست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/461567" target="_blank">📅 17:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461566">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‌ هلاکت ۴ نفر از تروریست‌های وطن‌فروش در سراوان
🔹
قرارگاه قدس نیروی زمینی سپاه: درپی انهدام یک تیم تروریستی حرفه‌ای که قصد اجرای عملیات ترور در سراوان را داشت، ۴ نفر از این تروریست‌ها به‌هلاکت رسیدند.
🔹
همچنین تعدادی سلاح و مقادیری مهمات و مواد انفجاری از…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/461566" target="_blank">📅 17:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461565">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCfrvmdZgku0nerZd5jVEicEhrWB1H7Yjgb9RyLZdgjHwtPbpzJeQlmEOi7slwWE0qstDWXepeSLqDzFXJ-gFKQtK6NwGMZy0h11ZprAggOp1dRaVdTWXcXWkmtvgRxC07q2uHXlh8DGBrzWW6Xv3FhLKgoJNZeEmcdNxoU8usZe9av8vam79xdY8mhm23iHAjm3HnvCDqVlyVIMgoweWFHZbE6rQLuPZH62ZUz0mRRFt2wKcDTkNZwxV75VUaQZME5CgHvjBhSy6DJvJgXq8JXkyJ4x07QjTqwbsAt1R_1uCqVKXqSXJlxPbYkjbeyNg1vQf9Tx6O6M2c-VCvUFGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندر دیر آمادۀ ورود نخستین محموله خودرو از قطر
🔹
رئیس اداره بندر و دریانوردی دیر: بسترهای لازم برای ورود نخستین محموله خودرو از قطر فراهم شده و خودروها پس از ورود، تشریفات ترخیص قطعی یا ترانزیت را طی خواهند کرد.
🔹
همزمان، صادرات بندر دیر به بندر الرویس قطر پس از وقفه‌ای چندماهه دوباره به‌صورت منظم و روزانه از سر گرفته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/461565" target="_blank">📅 16:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461564">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🖼
سخنگوی سپاه: پیروزی‌های انصارالله در ساحل غربی، روایتی از یک پیروزی الهی و ثمرهٔ سال‌ها ایستادگی در سخت‌ترین میدان‌هاست.  @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/461564" target="_blank">📅 16:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461563">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شایعه توقف پروازها به عراق رد شد
🔹
سازمان هواپیمایی:  تمامی پروازهای کشور به مقاصد نجف و بغداد مطابق برنامه در حال انجام است.
🔸
پیشتر شایعاتی مبنی بر توقف پروازهای ایران به فرودگاه‌های عراق منتشر شده بود که سازمان هواپیمایی می‌گوید فرودگاه بصره، یک فرودگاه نظامی است و به دلایل مسائل داخلی عراق بسته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/461563" target="_blank">📅 16:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461562">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpdXG2Egyy1W2YTWpw5bI_h_fAvdqqvvLkefjcz84j6OHJAbjxk_0mj8BEbBSZIRYPM3q3hPLCCYjzmUmBv9DWemSiG6v9I5FpqfZxO1Yx7l_4Qi73cyi_wWRUWaHXprb81P6qc3FFO9102ysIvxP74q0fIrpd6la_uj5XlxUP_83ScXdEb2ysmhuaGlMn_ES9NjunnrY6aAJyLLcXeYma4-0ItLVdkLemeiYyA75yKOvJfuyFsujAsDcAvt3hiie2LlsID3VlLgJ4OFJz-BbTERzrGWWDNUkui2ASKNrr7HLn37MbTOTZgB4lL1QB2u5snHcruegQxrdn5dDYIAyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متکی: ترامپ تنها ۵۳ روز فرصت دارد؛ نباید با صحبت در مورد گفت‌وگو و مذاکره به او پاس گل بدهیم
🔹
منوچهر متکی در صفحۀ خود در فارس تعاملی نوشت: هم‌اکنون در حساس‌ترین بازۀ زمانی جنگ ترکیبی آمریکا و رژیم صهیونیستی علیه کشورمان قرار داریم.
🔹
ترامپ در شرایطی که با استیصال در جنگ نظامی، نگرانی از شکسته‌شدن محاصرۀ دریایی و ناامیدی از کارآمدی تحریم‌های اقتصادی روبه‌روست، تنها ۵۳ روز فرصت دارد تا فضای سیاسی آمریکا و نظرسنجی‌های مربوط به انتخابات کنگره را به نفع جمهوری‌خواهان تغییر دهد.
🔹
ترامپ با تلاش برای پایین‌نگه‌داشتن قیمت نفت و القای درجریان‌بودن مذاکره با ایران، درحال مدیریت افکار عمومی و نخبگان آمریکایی برای پیروزی در انتخابات کنگره در ۱۲ آبان است.
🔹
پیروزی متجاوزان در انتخابات آمریکا می‌تواند به معنای ورود به جنگی تمام‌عیار دیگر علیه کشورمان باشد، اگرچه نتیجه‌ای بهتر از دو جنگ قبلی نصیبشان نخواهد شد.
از آقایان قالیباف و عراقچی درخواست می‌کنم:
🔸
در ۵۳ روز پیشِ‌رو، به‌هیچ‌وجه از تعبیر «مذاکره» در سخنرانی‌ها و مصاحبه‌های خود استفاده نکنند.
🔸
هیچ گفت‌وگو و ملاقاتی با واسطه‌های رسمی (پاکستان ، قطر ،عمان) یا واسطه‌های غیررسمی دربارۀ جنگ و انتقال پیام به دولت آمریکا انجام نشود.
🔸
برگزاری نشست با کشورهای جنوبی خلیج‌فارس، به‌ویژه دربارۀ نظم منطقه‌ای، به پس از این بازۀ زمانی موکول شود؛ چراکه نتیجۀ جنگ، نظم آیندۀ منطقه را مشخص خواهد کرد.
🔹
ترامپ با اعلام منتفی‌شدن تفاهم‌نامه‌ای که خود امضا کرده بود، بهانۀ لازم را برای چنین تصمیمی فراهم کرده است. مراقب باشیم برخی به ترامپ پاس گل ندهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/461562" target="_blank">📅 16:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461560">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hupfm0BEykoAPyOLHWv_Wa1_2M-0TBnawA6aHqHfkmYibY-zTw6ypiIybzGg33WfWURUylOSZVuSMBgm759mXm1mCQuvL5xUN7SuBSoAsZPXMGDgpw-SBgbpWlUF0kswGLH3g4xPLOAMYXzTZpnCLG2kBgxaUQOYOAHsKD69PLXN-4uytV-Zj102Xy8vOqWegYlW-4MJkEwUUNSIW56X2jU7hxV6lMmljK8izyGlqNPB8cE1OZN1yFNa6vza2mAF_l9OxmPmD56Y6sjju8nJu34Dfx6KUs8un-GLbqsZ8SHRLi6BCU5y9eVFqZ7x4Zh5NMXXhw8KJuUecBnKLtcYNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hh4OOZJoBqBvq4RdRdtPPyhVS1dx1p5Yn-eqvrusNFV94G3OU3Qxhgt7pM-69zGAZqP6ZBPXiFsOLu9YPkFvoX5ugDdgKrYL7zsOBAFcw4q432MhDsn-oRVr6p5c96bcjcgin-oXhkLTXtYkIstlzPqTMfAWqM7udaKvoxR-glw5_zogOi-bMb7GobWeq1pqQePDy9XUNdv-giSnIJoGHqgbcybB_2AGKeN6TaV5tiHP6NNpk1iJnJyZ3K3Qb7voglI4GsK9HhhGhCSnRkjW6nerytdU7JwUlpviny9V_zVh5HQw6PvIYvHVmjypiywrxawREFn3bvvaJPpYKvUeaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گفت‌وگوی سرپایی عراقچی با همتای چینی در حاشیهٔ نشست بریکس در هند  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/461560" target="_blank">📅 16:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461559">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jj8DpQKMAf55PjJXZMBSBu3dlW2eizbzGO6eKesZPEicINHFGnDvlECDWwQ6BNPViJ0LilROH-K9ykwC0WOKuf8bcRYp1IwEMktkXHXSMTpXN2twaxzVERG8FJn0aYEGZonszvfDmanHeJRQue5TUTgswlUxRQDidvK9xn31QxXoFqQn9JNbY0C2MZaceNIKBFTcx8crogMkVr2KcZ3GyZDw0oqnno9eC960j4rGeZ_-t83AodQhFxa_fqjkxXJc89p7Zjj1Go30a2susevVXpuioH7paVn6MmfNBLzf4VWeNlBYC6gaF8A0ecighOPpbBk0cFJ4fYJoOwKI_jMQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترافیک سنگین ایستایی در جاده‌های شمال
🔹
پلیس راه استان مازندران: درحال حاضر ترافیک در محورهای هراز، کندوان، سوادکوه و بزرگراه‌های استان در مسیر رفت و برگشت به‌صورت پرحجم گزارش شده است.
🔹
در خروجی شهر مرزن‌آباد محور کندوان ترافیک ۷ کیلومتری ایستایی رخ داده و از حوالی ساعت ۲۰ تا ۲۱ مسیر شمال به جنوب محور کندوان محدودیت یک‌طرفه اجرا خواهد شد.
🔹
ساعت ۱۶ مسیر جنوب به شمال در آزادراه منطقه یک البرز به مازندران و پل‌زنگوله انسداد انجام شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/461559" target="_blank">📅 16:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461558">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/El53ks8LEPcw4MhOpkQvHy6d8W2EjM37lA48eSzRLl82CCb-b2lNQgVFQ3G8RnVS8onqojIqx_3yKPs2ZbDZOMXkr0iHK1WCf3BAF8BAMQ4ugT2AzA2Q7EPGuTigLFYY1GyfihS3ugi_iPMYKn4s23Ur_liPfnWtaX2Jc1m_CDFCZdiJhONKTBRhD74JMSSKBqibKyClfoEMuaYe4FNdVJyd64llasw2cgHWEkMhFtKru978o0XctKVVD9CmsjOiocjviLRmdp39IjGp4Lw0p33MFl-NXoCOe0ovDFpckKdzWaelxtWghMPWpHYik8lOU9FGBseMdHuLa5Zdavnm7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهم هزار پروژه‌ای همراه اول از بزرگ‌ترین افتتاح ارتباطی کشور
🔹
۷ هزار و ۹۴۷ پروژه ارتباطی در سراسر کشور با حضور رئیس‌جمهوری افتتاح شد که یک‌هزار و ۵۰ پروژه آن به همراه اول اختصاص داشت. این پروژه‌ها با هدف گسترش پوشش، افزایش سرعت و ظرفیت و تقویت پایداری شبکه اجرا شده‌اند.
🔹
راه‌اندازی ۸۳ سایت جدید ارتباطی و توسعه شبکه 5G و ظرفیت LTE در ۲۲ استان، به معنای تماس‌های پایدارتر، اینترنت سریع‌تر و دسترسی مطمئن‌تر مردم به آموزش مجازی، خدمات بانکی، سلامت دیجیتال، کسب‌وکارهای اینترنتی و دیگر خدمات آنلاین است.
🔹
افزایش ظرفیت شبکه، توسعه زیرساخت‌های انتقال و توزیع محتوا و ایجاد شبکه مدیریت بحران تهران نیز تاب‌آوری ارتباطات را در زمان افزایش مصرف یا وقوع بحران تقویت می‌کند.
🔹
همراه اول با اجرای این پروژه‌ها، توسعه ارتباطات پایدار را در نقاط مختلف کشور دنبال می‌کند، ارتباطی که امروز نقشی اساسی در زندگی روزمره، اشتغال، آموزش، اقتصاد و امنیت مردم دارد.
@mcinews</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/461558" target="_blank">📅 16:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461556">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IcAM2vBJ-l--xq7opzkSrOs9bRs2RC9ocoLFYPtNwW_11mYqFxsAvAmBPPGfpiHYSg5wNuI3c7ulKb0mu8I2L7dNP95W3RrBEP8_GbeCwWtU0lyjxG9lrNfp-Ucd5ON3aEKasUWlcK7kajNZpmXnifzD92JCWoqYhjJShlJupxPBzu09bDS83VwOxWTgLd4HNtlk1TdIwmK671hTXbvShmWJQDBJmsqtiwTQ-qJJVAbS2RDOv5VkJ_TIF3TzjGKGq99AaZqHHxxc-uniZ9IPwofxO8D0EFDe_fnmzibK0mm8JrcI2RYdfMDRX-SuyFD3_vWUIVj2CFfT1AaPvHL9Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iG_Plgbm53MJzfb1Xh2m4MNLWRYISQu6bUJQD4CoVYn-LscUwSLocsvV_C7DDTcCq1yCql_0OXOpK_37wGGjXcIgXykViDZelgNYR5WuWH52mQ4bbG51M3Uu0oqhAcPNkeGdd6rQ3FGQ2asuwBE3n_AFGKGcnhx-7uwHhQq3EZx_dJLVKsMfNriMjO4HszhSzz6EomK8VHbPwcDAK0xJGMA_DHJig436FklHEdYvcFHuaTQmLk5ON_UJitcS9j7SgIp3ZrQPQKjn1Ji5t9u6j0Lnt8FdHGANz353gIx5RTpCz7838zeTsLbXTa_0_xrtLCBFGr1AZ97bx246cAEdag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔸
نصب تجهیزات فرآیندی و سازه ۱۱۰تنی در ارتفاع ۷۰متری؛
🔰
پیشرفت فاز۳ تغلیظ مس سونگون به ۷۰درصد رسید
🔻
پروژه فاز۳ تغلیظ مجتمع مس سونگون با پیشرفت ۷۰درصدی، وارد مرحله مهمی از عملیات نصب تجهیزات و سازه‌های فرآیندی شده است؛ در این مرحله، مکانیزم‌های فلوتاسیون نصب شده و سازه ۱۱۰تنی پل گالری و بریج شماره۴ نیز در ارتفاع ۷۰متری با موفقیت جانمایی شده است.
🔹
عملیات نصب تجهیزات فرآیندی پروژه فاز۳ تغلیظ مس سونگون در حال پیشرفت است و تاکنون مکانیزم‌های مربوط به ۹ دستگاه تانک ۱۶۰ مترمکعبی Cleaner & Scavenger نصب شده است. براساس برنامه تأمین تجهیزات، ۲۰ دستگاه مکانیزم مربوط به تانک‌های رافر با ظرفیت ۳۰۰ مترمکعب و پنج دستگاه مکانیزم تانک‌های Recleaner با ظرفیت ۵۰ مترمکعب نیز در ادامه وارد مرحله نصب خواهند شد.
ادامه خبر در مس‌پرس:
https://mespress.ir/x6Tn
@mespress_ir</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/461556" target="_blank">📅 16:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461555">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/461555" target="_blank">📅 16:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461552">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WnOQ023jacLmquLBTDsObC6PgTrwqocIsApuKMNwG-nsMGi6iDUSEVUavm-Byc260177WT28DZnSwuuaChSY0k-IJQE9wXZcK4-IqjEcsibRrX5KNtzCCryZgGwi99etFgo-CZL6sKEP9OXubXWFLH79rlo3RYE5_h5etmcvFegq48cap0Ru8X2oshxobcoOawD2K0qvwDmf_iJ9UCO0eNd7Le_jUo91HecHX2tZ8MATApHYwZdxvfP3Di8Fxv4aVE9wTwGk5oWW_CyQSq72Cmi71fY5xldJzqZKgukK0dsgOhKejUHEbuwDfFUmvVtXnTpzR-7e0HzjNMX59gUzeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fj9LrGibFq0Mk1K8cKQm9WYNpoHEgTUg9nsZEDnvAqLg9-bWvv8K18Uze6yGs8euVHYoPav32ifdXDG-1fxXjOoRgFG-7yTl21h__KlJypYUj6NPQtc-OPNVHFroLl2MJDCBjaY0sb3jhymjdAodWsVOZylHyln2TeAtx0MgiL3_NAYKdITffOnDoEX61uD2KjtVcvEA2oSO3VEpnB3mG9ZQD7Dd8P4ooop4ThQ0wrteiwBVB51Ll-yxI2BUWpKmN2OQcYzU2gbNpO8fffZ9yXU6KLtFZPknFvMjr_-y0P4LuqqJrmeqQjrtbWWijHZ2dN5h_8oCNWYyLmIB3T2Cvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lyP1tFMt9w67ZSyrtHNQmHUP_87ddIjzhz80zezMU8Y_9PQHofLEdQxuq9yyuX6wyQZ7Jqbu8u4HkPMv6MgD_jrP0yZihEgeadUuw-V3QH2s_SZNBhRIEKbabTsHfQUzTnpLv-DcBCg0RbD9PNToy1XHBXqdlGGdlc25EmL5wK4wUfYjHBsVVfF50VuDe-ryPpOefp3O61d8CcoWWU_tGTsXj-BvYDfvBIOj2raXLjZmpB7AmYAVkuZRHbEBggnYfImCSxdwJnt7EwPxuc7uehaIvDgdYvnaEHRwKMuegyEIfbBJGJ0LQz6DGe6vENOJ0jAQ-kbUMvD4ueeSH4hkuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پزشکیان با خالد بن محمد بن زاید آل نهیان، ولیعهد امارات دیدار کرد.  @Farsna</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/461552" target="_blank">📅 16:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461551">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpqE-7akiv5V4Vt7lT6mXAVdl1KaSQilY5mdOoRmmTsadutz409nIKI23idfe5CTP9JjerCJhnsiXlKIYcq3bCQp1pVVnQzSThvTkmR2lhhizOw3ZmkRd1B-zfWz2WM84Wpg9f3wpiE9aI_R2J9U98aSKaB1KRsf4IvukLW7lfpLgoG_GL3xKzhVC_e9m3Kv0uEKYmOcfy6cW8LsXuPtFOBc1Vafb36MSBEM0bvtVVFyGvTbPrUD79GmZCxH3azPClo1LM7fIO5CJfkrnmXGDk37Adn3o3Iyd2KoqQCM0cIGyiDmNQUjtpU-b8K3007hgD2_W8Nq70cGjiZSloJREg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت اطلاعاتی آمریکا از عربستان در یمن
🔹
شبکۀ ای‌بی‌سی نیوز گزارش داد، دولت ترامپ در حال ارائۀ حمایت‌های قابل‌توجه اطلاعاتی و کمک در زمینۀ شناسایی و تعیین اهداف نظامی به عربستان سعودی است؛ اما فعلاً برنامه‌ای برای انجام حملات مستقیم علیه نیروهای انصارالله…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461551" target="_blank">📅 15:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461550">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38b2b245b.mp4?token=UocOr_GonLcZ4L7rWe-Kr_BvPTaF3KAyzHHrw-IAgZbi7nR_UEa7ZlfP_qb5lywRHH_cQD_K4dg0LbfN1G2KmhMvZ4JAtoXqv_gVS9MnK4t6aY9wtRPDKPMLgDCPLnsFYTnhOliHLDnj5ww_pKkUrCQPvJtIFDpH2T15BqW33S6ESUr11uExLcJlVpZ_L-dwSYxP1K5Spw_gEfOp60kQucmceLPZT8H5Z3xqrcLbm8GUPW1S-fC7F58BgpDto9lw3q-T1e56HK89YMuji5X1Zq7PtjUpcV07OQ-k4CZDIM-l5O4HbmLFQ6xAaSBDuj2xuy3ZEUAZT7KZCZqnEIn9dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38b2b245b.mp4?token=UocOr_GonLcZ4L7rWe-Kr_BvPTaF3KAyzHHrw-IAgZbi7nR_UEa7ZlfP_qb5lywRHH_cQD_K4dg0LbfN1G2KmhMvZ4JAtoXqv_gVS9MnK4t6aY9wtRPDKPMLgDCPLnsFYTnhOliHLDnj5ww_pKkUrCQPvJtIFDpH2T15BqW33S6ESUr11uExLcJlVpZ_L-dwSYxP1K5Spw_gEfOp60kQucmceLPZT8H5Z3xqrcLbm8GUPW1S-fC7F58BgpDto9lw3q-T1e56HK89YMuji5X1Zq7PtjUpcV07OQ-k4CZDIM-l5O4HbmLFQ6xAaSBDuj2xuy3ZEUAZT7KZCZqnEIn9dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرمربی و بازیکن خارجی که به استقلال نیامدند اما پول را می‌گیرند تاجرنیا: با کاریله و استراندبرگ تفاهم می‌کنیم  سرپرست مدیرعاملی استقلال:
🎙
کاریله از ما شکایت کرده. درخواست مالی او از ما زیاد نیست. می‌خواهیم با نصف مبلغی که می‌خواهد توافق کنیم. با استراندبرگ،…</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/461550" target="_blank">📅 15:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461549">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6db67df5f5.mp4?token=CrApSV1xgjgx5W0ZJesbRvdY_uubARUe0X28AxXkOiUGDVglifDibNi4WwxfyiV2BWfSfveDYCPFlYREYfBodisCYCopNOTOQD6hRdJ6PVHJwAKXnanMcpuxJhY-rsfk2SPzWX2maXt4azF4EgiDnMLn4cR6cFmXnEBe29Ln2xWLnlNVSO3yEJgVS0KpfiPQ_47LsV13KpDXGk2UOWnGKA2kQlQpYx4-cmbos2z6c6hcgIHPbFXrBJ3SlC6oJSGOaoY1K9Gn3viVcmc5_mCkg846tPnNj-KVv0ogIjvgqAZDrpFVIv-mi2dM4ufCGYZB5RPXPigetQWNAU3QYWpK_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6db67df5f5.mp4?token=CrApSV1xgjgx5W0ZJesbRvdY_uubARUe0X28AxXkOiUGDVglifDibNi4WwxfyiV2BWfSfveDYCPFlYREYfBodisCYCopNOTOQD6hRdJ6PVHJwAKXnanMcpuxJhY-rsfk2SPzWX2maXt4azF4EgiDnMLn4cR6cFmXnEBe29Ln2xWLnlNVSO3yEJgVS0KpfiPQ_47LsV13KpDXGk2UOWnGKA2kQlQpYx4-cmbos2z6c6hcgIHPbFXrBJ3SlC6oJSGOaoY1K9Gn3viVcmc5_mCkg846tPnNj-KVv0ogIjvgqAZDrpFVIv-mi2dM4ufCGYZB5RPXPigetQWNAU3QYWpK_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: در قضیهٔ تراستی‌ها و رفع تعهدات ارزیِ آن‌ها، پیگیری‌ها باید منظم و مستمر باشد
🔹
به‌هیچ‌وجه قابل‌قبول نیست که یک تراستی در ماه نخست ۱۰۰ میلیون یورو عدم رفع تعهد ارزی داشته باشد و عدم رفع تعهدات همین تراستی در ماه بعد ۱۵۰ میلیون یورو شود. از سوی دیگر،…</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/461549" target="_blank">📅 15:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461548">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3-d-uEZOnL1FTz95kLlzhJauRVcf24b8RrLWEDyIO-4DPmq5MuLDzbftV9k6WGeFpEYq5eaWoATX1XvAOPNKySsS5a2L5TpOK6TDJKU6OB69iTkzKYxhB4pxGWt_MrLrBlnOwnwTGuw8US-3EkG3oSkSvjR5Bv395uUu95axBtNqtUYB9uXbni17VMEIhg0Z4hfm-SE2rSPBQ7sHnt0sHzoFBAEc93mVzs0Nc0auYyG7V-9z-c0bMBwC-yTVPgkK0zQsF289o_1yBW6yIU_Vos1XbyNJdvpzkyyDgrMLMQz1rRXk6-AGUkHtUZHuSlUkFHCFbB3cnBsGgOQ-dnYDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکایت بنیاد آیت‌الله رئیسی از ادعاهای کذب یک بلاگر اقتصادی
🔹
بنیاد شهید آیت‌الله رئیسی از یک بلاگر اقتصادی به‌دلیل طرح ادعاهای کذب دربارهٔ رئیس‌جمهور شهید شکایت کرد.
🔹
این بلاگر مدعی شده بود در دولت شهید رئیسی از او خواسته شده مباحث اقتصادی را به رئیس‌جمهور…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461548" target="_blank">📅 15:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461545">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ic2N0EY1lTLk3XmORRCFfYvzEFNTU7dKLU0sSpuxFunUilKQHyt1itQVdA7TExURlOfHY5boKYQEDqU8kP9zbkTejXkM2axu77vPRCw4XgbxflIFhkiOZw6G_Bxzd1ojBuTk-GxjRsqPP6-1ADuYMCDEPZyQsAMnx2yE-5hKXaRZ-Efxtl2v1pDDdHuwVZiqUYVt7xZBQHOG5LElUp_gcq7z8fPQ2v6bYaClAJGWRvcQbBnzAPTaHVNmca78QgM0PNmY2QBQyXc_aT7qUwSdWVQFOC_7HZUwSpGySFksxv8sUArs-ma255RY3FZn4Fj0f6UFcATC33Tz19anDKStSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qdde5ZSa-KKkTqtjU5Fnufdr0rUYTHodv-veE6vHNZlZbwkjLGfQq6taw5IGKyky3im3wnaBcnKWrggp9boa2vyThGkVN0hILJb-QPNZ8rlZOGjAQadSQZrKYtIFujSEJuUHHoE0fyoAbuuIYKKLV6qO5sD5QtH9ND1PvmNNT2L5utms-jiaIiGhJkUn2jnALSxkQalYZY5q8p0x1jvDngEM_T7EoIG5-KokJIkfE-tHqNhwvSicN51V-sD6z_eKy3ELV_E7JyOjh88DIqVHHdYAqAqNT5Y8Si6pLMiWZ61UJkskU7B5Y3gWlVX-m42_XD6CTzPQc-uCle4NFn46jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h57LwVLFaEn0uMFOKUv9nAAycnWWdGtzGlvo0jAQLP3MI0ac1zOvwv_ZpNJVN7xlP2W748c6LkJK4CwGPNUJ-qq4f2_xVDQpVjgSxw-Azj4W861-n8-0g3tFLVOrQUb6WYydyBnYpfBzuQ0nSNBDkwuDzggfDgslitBrevn8we_Ewq6U_s_SUcvNXPI4I5rbF-RRL8HoleMgZwMY5GVKw3qCBYrqN_NUfJS3mHPVnrm_ZDpwAOfqeDmA3b0cmcxP2rEuct5eDTa9h5GA_DIr3O9_g0sTVDYXBSz7rr94HOibpQGndOi2m5uYiSABaiBig2aqKmBvm-qi8UE8kYIpUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گفت‌وگوی سرپایی عراقچی با همتای چینی در حاشیهٔ نشست بریکس در هند
@Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/461545" target="_blank">📅 15:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461544">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اجتماعی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-DPjZFGQTSpy6ddeyYr7yo621UXw3nFZ5VYxxrcI2dR15PKZUTPOM0UafORb7_zxPo0lcjyCQdOt26nMUdOM97VqtUbzCosZIerkDNFiCl1TCfOhix212U5AUvlv1VlfZXMA1BmnzggWFnLKeijcTjVJA4-FiehDn6qSF9abhuqDco2g1dDmEtGj-iL1a4pKaMIgsUSv-LbN9rqAM-k3C79VsNjJ_9wpqfaEAvrpna84HokHN42OEMlykicQg2KODYYVcKlCJVcU_rMkBl1D80hKWVgRfRuJLGCg2j255HMLlUx9JvH__0qjCmZDoWVGEQ4DY5EItCp7yg2NPVe4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال سیلاب، صاعقه و وزش باد شدید در ۸ استان کشور
🔹
سازمان مدیریت بحران از احتمال رگبار شدید، صاعقه، سیلاب و وزش باد شدید در آذربایجان‌شرقی، زنجان، قزوین، تهران، البرز، مازندران، گیلان و اردبیل در روزهای شنبه و یکشنبه خبر داد.
🔹
از تردد و توقف در حاشیهٔ رودخانه‌ها و مسیل‌ها خودداری کنید.
@Farssocial
-
Link</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/461544" target="_blank">📅 15:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461543">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fad3da36c.mp4?token=eAg8QFomTHlEapFr1wPJG152uH3cyYR6_yvCmkg2Fjt9fxFTEei6EMjxWb9gBnr0vfyRJe4pn-wPR31TL79nJRH1nzS4_KNb_WZ9fliiXozuIMKWIs0NpkNPUCUy6hnacOUJqZkZgNpwiceEeB2RlerxVPPRmVu-SGGmKOlpNvVFGU0eu4oSLzslX6DPXgTf9kuAXyGwv_ypYxUyTFoqtrDdJpD1i_ejEwOvOers-JSeptXm3OR_mqCXV9nGnyaHdbA2niTmF0Lt8iQL0vfDS6yWo_P2MUChvV1j_3aVA8BGiXYgBCTwxTwr4hSUrCj9oBRBZKhv-T2rBqvwalVukA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fad3da36c.mp4?token=eAg8QFomTHlEapFr1wPJG152uH3cyYR6_yvCmkg2Fjt9fxFTEei6EMjxWb9gBnr0vfyRJe4pn-wPR31TL79nJRH1nzS4_KNb_WZ9fliiXozuIMKWIs0NpkNPUCUy6hnacOUJqZkZgNpwiceEeB2RlerxVPPRmVu-SGGmKOlpNvVFGU0eu4oSLzslX6DPXgTf9kuAXyGwv_ypYxUyTFoqtrDdJpD1i_ejEwOvOers-JSeptXm3OR_mqCXV9nGnyaHdbA2niTmF0Lt8iQL0vfDS6yWo_P2MUChvV1j_3aVA8BGiXYgBCTwxTwr4hSUrCj9oBRBZKhv-T2rBqvwalVukA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارت‌های بازرگانی همچنان دست‌به‌دست می‌شوند
🔹
مشاهدات نشان می‌دهد یکی‌از فضاهایی که کارت‌های بازرگانی برای اجاره عرضه می‌شوند، آگهی‌های سکوهای رسمی فضای مجازی است.
🔸
این درحالی‌ست که به‌گفتهٔ دادستان تهران اجاره و خریدوفروش کارت‌های بازرگانی جرم است.
@Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/461543" target="_blank">📅 15:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461542">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf92b2ceaf.mp4?token=Reup1-tBUo3A5Mz2K4IgHD_0DyKplMZ1RKfFl3Mg91P85cYQPUj1OKPEsLx41x3ZQa8RRFGsRsYXA8414xuAbhc8dU5cUbAO1PrDA2bExpRaE3dR61IDjuBXRTbbD93x5i7fPEUQSIIQVinffIUcCpm7TTHT1YWJ026bHB-0UlEanVRQnAPf5ZBcmamV7Dq4zZLAxifXHH1hSxC4rGf3s1V-BrnuB29pPx174jzhXHqVPrKySXu1ui3UfirnkPJMr6ZO209UEkuGfnzU1DuasvH7dJK2r_N_HxZmv48aCJlZI2vEpMGg32oxEqrPxk60f6MYhw4OCkngfiZ4lbsXxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf92b2ceaf.mp4?token=Reup1-tBUo3A5Mz2K4IgHD_0DyKplMZ1RKfFl3Mg91P85cYQPUj1OKPEsLx41x3ZQa8RRFGsRsYXA8414xuAbhc8dU5cUbAO1PrDA2bExpRaE3dR61IDjuBXRTbbD93x5i7fPEUQSIIQVinffIUcCpm7TTHT1YWJ026bHB-0UlEanVRQnAPf5ZBcmamV7Dq4zZLAxifXHH1hSxC4rGf3s1V-BrnuB29pPx174jzhXHqVPrKySXu1ui3UfirnkPJMr6ZO209UEkuGfnzU1DuasvH7dJK2r_N_HxZmv48aCJlZI2vEpMGg32oxEqrPxk60f6MYhw4OCkngfiZ4lbsXxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جای نفت در جهان هرروز خالی‌تر می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/461542" target="_blank">📅 15:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461541">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d6e9ca6f.mp4?token=kZdry_XkfgljI5PlbE1NlK6UL2Fp7K0B4Lbga3nTwio2a0-uV9Sy6aveU8xcb0U5q6lXaUzh9cC8ls3OxPPdxjrWsxjefKrY9QYVADcQYUPu-ht1zswqdYMNIy-j54VHZmMNTeUletbjDKSsV0Es_9gtWi8wXsmufLvfAogb0zYiPKra25lyo56BLO7RiMDpcEx8yp_nFM06xxoLKiXKDSZcbZaYZEiX488MmFeETBVxls6vg-Ur0hG5MR1HYVvnR3S3lF-R5-y6cwv2hNTd-fXCvZr0vC3M1FNUHAtcKeLMTgS8GhFjIDYThTeulDBBgA7R990Nmqdyws2ywrMYHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d6e9ca6f.mp4?token=kZdry_XkfgljI5PlbE1NlK6UL2Fp7K0B4Lbga3nTwio2a0-uV9Sy6aveU8xcb0U5q6lXaUzh9cC8ls3OxPPdxjrWsxjefKrY9QYVADcQYUPu-ht1zswqdYMNIy-j54VHZmMNTeUletbjDKSsV0Es_9gtWi8wXsmufLvfAogb0zYiPKra25lyo56BLO7RiMDpcEx8yp_nFM06xxoLKiXKDSZcbZaYZEiX488MmFeETBVxls6vg-Ur0hG5MR1HYVvnR3S3lF-R5-y6cwv2hNTd-fXCvZr0vC3M1FNUHAtcKeLMTgS8GhFjIDYThTeulDBBgA7R990Nmqdyws2ywrMYHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه از صحنهٔ جنایات دشمن در لامرد بازدید کرد
@Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/461541" target="_blank">📅 14:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461534">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tzdq1X6x834RR4JfqdinnWoVVy_fRhKlhwnR9yxpsqD-ymCpydi2LpduD1ebWqQ28ehigGoKsko61IjYjHbMXxeGy4vcLiGE8u6yXTQhGlh-tHOpJgQlO3Mm_r5KnNhubzlXnxn5jk70VlQva0tMXmi4vIpE2Ku_v9ddnaMFL_VTo1pHni5k_wJ_jAx3Oh1SlzlD6qOeO2gnHqx-GuE9LusqF_g4EuMEwJlhj-wAY-bZV-3vOfa8D6gEQiaXLpnUCsPB5QcDl59bmJgX_uDtYgXrUll_3oSFS3uTamJ_VeAeMpXgxz2K8ntHr8bk1TOlPWCaU_CNSo3HUiogyvnhcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGwmLdcSrzzdsz8TikT6ZnL36ms3yG4EDKtK6e9wjamKpf_-tNAa3AaT88alhECoAX1r03kvA5mrx70FsFnycvSWzekzQBDGbCaj_h5xEIsE8aXYpH-jRuky9zSN4I5qVvwBOLPHkEIRTnOC99bp7Lc1CrfJDAF6teUx9-SIQvqwWg2JnO8DwSLu57ZXk1MdF1ITverLcDO9RPRjxrzu6mCJwao645xv4iWGfPnQe_Dr8_g1Q5uljHHAwbupPpm7kogIa_CGGdbpnF3QZdmwInL2KA8BHGYAdeCW-wSwZiqYY4Wlv7yutoaCE_mjeeFOQF-QuG1SnkhKUiku6AipVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SNjLyHdpSn27Z-1ytav_t88xMIxKFTF3qW-Z7ZSACvZj9_ku3f7vF9y2-JXRd2QaF48-5YnKW0ETXBkPrT6dDaAIaUGmLst8TvZT_NyS5dNfOlz0UCpDNK9ZBNcW_mVqvv43kryZ4n5jmBpoLq3K1m-dPDdMoDgcgTWZa1yhIiZpLJrJ8G49TQolU111e8J76eI-LH-6BVgOhdUU2Mx_1YSzN0Km22ytQlSm5yqIZCUv9T7FuLRD97Mu_shG7Emy-I7pQvdFukKLT_bTkEJijVVFRDmuTeSQkfxdTrwLtihyvXXPLoeh_Cj0h7bSk1ME62djo_nRyVIJTA0Zg3fiMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pJnhjzZrFvi-VqvF_fvRdhoERb3StJ35KEqYNHG40gSzWAADfNuHZGUONgcFBYuJ6WAXmjNVpytwwMIw1l8DV_L_QZ5_rU1y4aFWeAc2IeUx151nHqmoBW_Zg05-_kun-Zv-7dJTLDPuHtMr6qDLB2Dw61u5VOnJk8LYLJvwAWx7_CvyYtxJrPGrFxy3VMdtnwRuFFq2_SticzydMRGQhntlcckeSlV8JIPngYa1c9Xync3UjWj-BuO_VZyspBvmDN0WRRIWCIdPyIGTbI9-fEDdqOEDAY3xdrK1WIBsZHHq4-tDS0LYqxaQhmfX95TrYu8pRnFBekdJapFmnqAf0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKBBgjuxQx6qMmGkC0ZwEEm-fwwPwithvXAwNPCIg0bj7b_Lj-hthR8fMS71EMnLmfkGC9-NkZnI9ibhN7o4bcjUVV8oOv_4_jB_ZHx9tB_aHqbjmuQ7l0MsgsWxjf5ScphGJ3eUQ4z0prWdz8vweS-7dEfw_Y1ptaNMOf2TIK-A-yEi-I3AMdpMiLAondGfFvdsUcwp-l-0ZdsJHskbCxHnVdg909seGgTktxSNuGjjZFvk63HSzuOB0TZtLJFT3Xv3nRd1SaNmcomsmOhs1yEk5SmXIaAL2IRaaz5-89bLoegLhQgoYZQ9Hd0qW0l_R81YhAwii2GRIUDAaYa76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ithonNdV5B4atU8iyoaYQKVgn5PI9OsQ0b2dCeQawDeDWz4YsMe__13mIpO-NYylf6Q6Ef3fQbZ0hVDKoMStRuGqeV-XxpWWxWTQzaoNZ2LAzBkqBUWMXrBJK0eu4a5VJqLdxjdcXLy3Ht9agHOzdOS9uwP36dNA5mxDPLNe1b_IYImqU1Z3r4ouOY754gIQo1_Dcfaa2jnqFJxfDXuWAVYy6lKG-DuO6S0S4GnVyL1L6rU2vCNOSMwQYMSSaTU4FZmQ7qCxEsDacGa3EGq6pIaeELIaHbfglTHIWtBFSOHXbwhZmyyp8j9SEDktUqSwlaPqr_faBuGdDfZqjkpUYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A5yojMtn_huFUAIUqESMzsvUrsPFQVYfnu18pF4Nn5JUn4DYLWMY8btTq_4KrJP72xhVITYOVjCux2tc_xdhxhw68OU6berPZmY0TkTnLwJRkaKHk_kooRj0muKhL63i2t_sKZTvcpvvVqoaZr7uslg_PDwZiOgm7HivggVEi9BsZ67f94wJOJeKdhcc8pR_0ZSffBWRoEEX38Gbxfm3TeKBFdNbnL-59cP0NbjBnexNsI6ExBITRKi0hIboZhYMFpzlQVzVkwZBtgD94ru24ivwsGLKG6ms2NtWzP0c-qj7J8rmZbytdF_ZwiBmQ8136rBDZ9XJanXeEfnwlYTNrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نهمین جشنوارۀ انگور ارومیه
عکاس:
محمدمهدی فتحی
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/461534" target="_blank">📅 14:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461533">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a405ba0f.mp4?token=fuiRDikLcgh0EzJ7J30xhGjVDccLXcAdhlCnVB82BVM-8o-2DYU533tVfuyrkdW2QwJ1OeFkSoRNfTjRoWb5veoGCSVLXB5H08j9x7xto_M56MrKXR37ZE0MgpZW7Yd4LnunfhE4Wd19-Vs-rtP_WpzU2rYEr9KDi_p2JjUGBvlfzR67MYQQ8Yx5_X1eEy5O_L5IS3npqScSNoLmPydkkTJvaW_9Ijju60Kla3Z80IU3aIxFTErbpfgH2kyq37F_TDTt1piFBjj99ikoVMBi5ZYmjagzQ3r8ia7MJEhImUs8cjONZkqKoPKu1BdaB2WJg-wGg4_WxATNnt0BgLODhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a405ba0f.mp4?token=fuiRDikLcgh0EzJ7J30xhGjVDccLXcAdhlCnVB82BVM-8o-2DYU533tVfuyrkdW2QwJ1OeFkSoRNfTjRoWb5veoGCSVLXB5H08j9x7xto_M56MrKXR37ZE0MgpZW7Yd4LnunfhE4Wd19-Vs-rtP_WpzU2rYEr9KDi_p2JjUGBvlfzR67MYQQ8Yx5_X1eEy5O_L5IS3npqScSNoLmPydkkTJvaW_9Ijju60Kla3Z80IU3aIxFTErbpfgH2kyq37F_TDTt1piFBjj99ikoVMBi5ZYmjagzQ3r8ia7MJEhImUs8cjONZkqKoPKu1BdaB2WJg-wGg4_WxATNnt0BgLODhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسته‌شدن موقت مرزهای شلمچه و چذابه توسط کشور عراق
🔹
معاون استاندار خوزستان: بر اساس اعلام مقامات کشور عراق، از بامداد امروز مرزهای شلمچه و چذابه تا اطلاع ثانوی بسته شده‌اند و هیچ‌گونه تردد کالا و مسافر از این مرزها انجام نمی‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/461533" target="_blank">📅 14:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461532">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttucBcaIb6ULuEmmQlCcb5D3PCQBsDLsj08Bu99RyQlaLx9ma4f-INPOZYD1Gv9ExHNrNbh_C_OmrW0oFowXwMuBRJjCpcjgkYF3WDSCwtP8nq-WqJK7PmOweqwaVT1gDa8AKmgTCWITJSxe-NQ2fVrWt1dOrUJngwFZhRfOGPEoR-fAVfLjGtDq-92i0hRxJjUZlT7SEhqVqKeqJryKNU8GEo79vzx2Pu39nPnRslBkmOB4plJm_qEgOE-ZNAYJEbF5pcJMyypoe80BqZEA7rPAWHInK4ATdHIre1Nb4S-UUcah5ucRZXc9ZIwzHETEO0EQAaGZhK8nFLxqsorlqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پزشکیان با رئیس‌جمهور هند دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/461532" target="_blank">📅 14:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461531">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d6858133e.mp4?token=RAOrO_ouLuR8Ni5mE5FsDIqa1VR-JYiQfnKNxrrj_MiCCpxbQIge2bFleuoMEoTOgo6UrrvOpD2RgMAqt_IeVcrhDnrJDVsnMdoaVPJGIGt76s3Hm9a5_8OE8qmASTdsMtzMeakFPVudG75c1J_jKAh1AvqP42l1mWyvVpAiXhak0g6CT3Pke3HzHU8n_vP-XySj0Q9GFLVh3Nua3End-pvsQp7KUsNIe4elS8dho6-eC4R5v8WbT2LF9azN_H_3LbDKVdCPeP-GqvVguFO10srTr3JfHiZmiRA68Q0Og-eum6Pfc5iiBq0dQ3gD9SKx3K_vGJTPNli8OM0B1VmaLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d6858133e.mp4?token=RAOrO_ouLuR8Ni5mE5FsDIqa1VR-JYiQfnKNxrrj_MiCCpxbQIge2bFleuoMEoTOgo6UrrvOpD2RgMAqt_IeVcrhDnrJDVsnMdoaVPJGIGt76s3Hm9a5_8OE8qmASTdsMtzMeakFPVudG75c1J_jKAh1AvqP42l1mWyvVpAiXhak0g6CT3Pke3HzHU8n_vP-XySj0Q9GFLVh3Nua3End-pvsQp7KUsNIe4elS8dho6-eC4R5v8WbT2LF9azN_H_3LbDKVdCPeP-GqvVguFO10srTr3JfHiZmiRA68Q0Og-eum6Pfc5iiBq0dQ3gD9SKx3K_vGJTPNli8OM0B1VmaLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۲۰ مگاوات انرژی تجدید‌پذیر برق‌آبی به شبکهٔ برق تزریق شد
@Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/461531" target="_blank">📅 14:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461530">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff42263766.mp4?token=f97cSSyDhAq2QQwVG6ZAFV15risQZyhL_lvufLG91p91GTbtu6ImydmCJZKBrksdRJV4Tjnixgt9rur8FcIO0iB_rpvb0qi4fvl2aXVjHuXrITcjjycKsPzAXVzsUEABxehFz5KA_Wk99Itv8SMHmMoZ_QzmP70NzzWjFjyTP7UMLfDAQFvDkitrIjW20PFJiY6tcK7ifxK1O0dZfo897pj-oT576VlYG0MWdP0WmZ-zNQikqVaScOxnH-75J2xTOP8-FQrxep0U4TU4XISbOH8TKJw9_kurz495X8EP459UkM75tIjiyhX3fr_bGxEmRqxg75-L-hDyTv_6hyMkbxNlF63FoJYhhOC5zhVpqsdCSJqgsM4y-q7z4IwRx3JEa6Wy6JregrVS3qcDA1yFcGJcDt72WTZkwGNzpz_4LIEDRr_rqOoh3RnAsf91BmluCo2nt6Xu6Wie7PGkkuFYqx5hoiHyBWBLXTVO5qAL-OHwu9Y13CHbNPdfHbGJ7tMp_lLtER_MCirzEQ22AN6YMI5PUkr_GGYcq_Y6ESVY_XVicPBmVBubgek4zZqO55rhiBRCStdPL7cOa24t8OihH4s3zXHskINryKIaTu7pngexbG3T8ydtNnq1aoDeX8RYR8v8zYrchHBqOl-eMXnzUPG6QclHkSTLfpjZiVM7Bhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff42263766.mp4?token=f97cSSyDhAq2QQwVG6ZAFV15risQZyhL_lvufLG91p91GTbtu6ImydmCJZKBrksdRJV4Tjnixgt9rur8FcIO0iB_rpvb0qi4fvl2aXVjHuXrITcjjycKsPzAXVzsUEABxehFz5KA_Wk99Itv8SMHmMoZ_QzmP70NzzWjFjyTP7UMLfDAQFvDkitrIjW20PFJiY6tcK7ifxK1O0dZfo897pj-oT576VlYG0MWdP0WmZ-zNQikqVaScOxnH-75J2xTOP8-FQrxep0U4TU4XISbOH8TKJw9_kurz495X8EP459UkM75tIjiyhX3fr_bGxEmRqxg75-L-hDyTv_6hyMkbxNlF63FoJYhhOC5zhVpqsdCSJqgsM4y-q7z4IwRx3JEa6Wy6JregrVS3qcDA1yFcGJcDt72WTZkwGNzpz_4LIEDRr_rqOoh3RnAsf91BmluCo2nt6Xu6Wie7PGkkuFYqx5hoiHyBWBLXTVO5qAL-OHwu9Y13CHbNPdfHbGJ7tMp_lLtER_MCirzEQ22AN6YMI5PUkr_GGYcq_Y6ESVY_XVicPBmVBubgek4zZqO55rhiBRCStdPL7cOa24t8OihH4s3zXHskINryKIaTu7pngexbG3T8ydtNnq1aoDeX8RYR8v8zYrchHBqOl-eMXnzUPG6QclHkSTLfpjZiVM7Bhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: چندجانبه‌گرایی زمانی معنا دارد که همه در برابر قانون برابر باشند
🔹
حکمرانی جهانی زمانی مشروعیت خواهد داشت که صدای کشورهای درحال توسعه شنیده شود.
🔹
ما به‌دنبال جهانی هستیم که در آن قدرت جای قانون را نگیرد، تحریم جای همکاری را نگیرد، جنگ جای گفت‌وگو…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/461530" target="_blank">📅 14:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461527">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ae4DXayOGAePEDRhfOCXd4GbS-vhH6eiXYdx_Rg_xV49PSY_NeLuMWVbrD0DiUTi_o69zkptCFeGbHnRnz4wsud-5vhTUKAsTBvuHb60tIFEdB-3NpfLGvdIgvKwF5E7Qn1yBXtWBxVdlLVk2liyOHpo647wumFip6fBRbbuqvQ_A_TVOGId6r6idYH9zh0OFnp239AK6K4fSEcQ41wh6qQj43S2vLZnPf9eI062Cw3xZ6ygZ2dTWN34lsUd8ysEcrb3VSZWjfMyU0GwAksrkZCJBiyhHUdLXZjL_qLheLRG7sXYLrrU7iezMrAQNnAJfy5DZECYX5f2m9-EbEiaOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/brlQfW-nsGg9lm1Q5EPRnhlxfGaejMM9d9v0QMNv7arfkUwES_4S2fSL4M7oYFEMaiJNDdb--E4G2RBMEhANiU_nuWWn-YJGmBT79gFr0YnDN6f66Po3eA13I7NXBfdbV9p031z2V_BEg75ChG7CQMmvyJ18Tenc756882zlDMfO4xtFXy_3OdXSCh2iWjg_8aLmHTL3uE3K6DzJO3VRyTJMlVekdq9Uy6Jrn5NSh89q6Fgs4P3om1k-a0etz6g4bzkW-iIMC3WQvaLmc98uZudI5an3G2sJL7hJYuQY5jjyP1wPE2HV69UB8PxcnQM2OlSNWNJMGFTnMEdDt-qeZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">25 سال بعد از یازده سپتامبر؛ مردم دنیا درباره آن چه می‌گویند؟
🔹
در پی انتشار پستی از سوی پیت هگزث، وزیر جنگ آمریکا، که در آن مسلمانان و گروه‌های اسلام‌گرا مسئول حملات ۱۱ سپتامبر معرفی شده‌اند، شماری از کاربران با انتقاد از این روایت، تاکید کردند که این حادثه در چارچوب یک عملیات «پرچم دروغین» برای تحریک افکار عمومی آمریکا و جهان علیه کشورهای اسلامی و فراهم کردن زمینه جنگ‌های بعدی صورت گرفته است.
🔹
بخش دیگری از واکنش‌ها نیز به سابقه سیاست‌های آمریکا در قبال گروه‌های تروریستی اختصاص داشت. کاربران با اشاره به تاریخچه شکل‌گیری و گسترش القاعده و داعش، واشنگتن را به حمایت یا بهره‌برداری از گروه‌های مسلح برای پیشبرد اهداف خود در منطقه متهم کردند و مدعی شدند که آمریکا از تهدید گروه‌های تروریستی برای توجیه مداخلات نظامی خود در کشورهای اسلامی استفاده کرده است.
🔗
اظهارات کاربران در این باره را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/461527" target="_blank">📅 14:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461526">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7108374e6a.mp4?token=aEZYNxAhBYE4w9Ul6Y3Z9NEy2uS9NtwQNxibQ-NliXOFhG5vk_2faw2YWLXP39_X2sWSMUVEaWSb0OU-t58o-PYyKs68q95B4Jsn5X_qKOY25Ib0BGUK77vc_0F9GJE9CdaZLHURyHmNa8U5NVRa79uS0b4jY_qjk3hp6Am0DugAkumZA-Mo52EzW1Crbcz3HpbrLBF7sX9jIZCSzeJH9apoDMvn27WgOdlzn7P-dz6vjRzYNpUGTFqX4uV1s1bQJZSzLIAn7Qscfrne2uW_N4NxqFAC0J4RT6leGRn5GoqZNSWNBhOGVUnTpvSTsssVMx0KxPgwIPZvg8JEJ8T8ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7108374e6a.mp4?token=aEZYNxAhBYE4w9Ul6Y3Z9NEy2uS9NtwQNxibQ-NliXOFhG5vk_2faw2YWLXP39_X2sWSMUVEaWSb0OU-t58o-PYyKs68q95B4Jsn5X_qKOY25Ib0BGUK77vc_0F9GJE9CdaZLHURyHmNa8U5NVRa79uS0b4jY_qjk3hp6Am0DugAkumZA-Mo52EzW1Crbcz3HpbrLBF7sX9jIZCSzeJH9apoDMvn27WgOdlzn7P-dz6vjRzYNpUGTFqX4uV1s1bQJZSzLIAn7Qscfrne2uW_N4NxqFAC0J4RT6leGRn5GoqZNSWNBhOGVUnTpvSTsssVMx0KxPgwIPZvg8JEJ8T8ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: تاسیسات هسته‌ای صلح‌آمیز باید از حمله و تهدید مصون بمانند
🔹
مقابلۀ عملیاتی با تحریم‌های یک‌جانبه و ضدبشری اولویت اعضای بریکس است. بریکس باید صدای عدالت باشد.
🔹
اعضای بریکس موظف به ایستادگی در برابر عادی‌سازی حمله به زیرساخت‌های غیرنظامی و تأسیسات…</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/461526" target="_blank">📅 14:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461525">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bleGXamophasIwzTeCoxp4IXDHZSdGv_pHjUafrSWxqV_q2Qq8o39Fosatoph3VwokrPBMXBhUxtFGDhQ4oM8X5Ae95c_jw7uCwC04-1WJijHLe2RNzfNzXep1QICcZcMUiT4k1P8EZ6YzXOWVHEXmVvVlYlyRDrneR6NBrZQWaRfLA5CQZ27ALnfu1vynLvuTTQBzN_GBrSgCzjKN4WndfATl3IXiCDQGxdOjc0pb51vH_sT5bNh45ySIBE9eIfIiWqSGt6onLP8zYY-TuO26n3D-g8MipK91T-akd0JMerIL6OTkXkK7EVDHMRYg0FV6Dc61gmRz8kGIc9BSY2Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانشگاه‌ها می‌توانند تا ۲۵ درصد آموزش مجازی داشته باشند
🔹
معاون آموزشی وزیر علوم: برنامهٔ وزارت علوم برای نیمسال اول سال تحصیلی ۱۴۰۵-۱۴۰۶، برگزاری حضوری کلاس‌های دانشگاه‌هاست.
🔹
دانشگاه‌ها براساس آیین‌نامهٔ جدید می‌توانند تا ۲۵ درصد آموزش خود را به‌صورت مجازی برگزار کنند و آموزش ترکیبی نیز در دستور کار قرار گرفته است.
🔹
وزارت علوم برای اجرای تدریجی این شیوه، کلاس‌های نمونه‌ای را در برخی دانشگاه‌ها آماده کرده است.
عکس: اصغر خمسه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/461525" target="_blank">📅 13:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461524">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d0c57f91.mp4?token=E_NIJO93lG9yimD_HwtHCT4R-J2XBGg71ESLFHk-1jkatyjrbbGgsqY3eDerkNYuLvweEEv4Uw8cp7_GOn8y065IpaDAu3u7sHYJMhrs6r49rHWz2DQf4NZ1kL5WoqnPlYdaBtrouHstiiuuTUeBUUb5LF1DxEK08MQUpWxxj4GROp7W-zMXfZ8nhEcHjfgdGeqsenFiU6haOC0kLU5pYG0Kea3q4tWTLRtK550JWpsNGd1VTmV7EEn0219dP_Fi91IlJw4IDY9dZbb_rL3Fsfx2OYeXdXXpDsfJwAg6TeQrK0JpT74hqp0sijQV1nTHzC1PD41KDQD4-sO_dge64Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d0c57f91.mp4?token=E_NIJO93lG9yimD_HwtHCT4R-J2XBGg71ESLFHk-1jkatyjrbbGgsqY3eDerkNYuLvweEEv4Uw8cp7_GOn8y065IpaDAu3u7sHYJMhrs6r49rHWz2DQf4NZ1kL5WoqnPlYdaBtrouHstiiuuTUeBUUb5LF1DxEK08MQUpWxxj4GROp7W-zMXfZ8nhEcHjfgdGeqsenFiU6haOC0kLU5pYG0Kea3q4tWTLRtK550JWpsNGd1VTmV7EEn0219dP_Fi91IlJw4IDY9dZbb_rL3Fsfx2OYeXdXXpDsfJwAg6TeQrK0JpT74hqp0sijQV1nTHzC1PD41KDQD4-sO_dge64Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
پزشکیان در حاشیهٔ نشست بریکس در هند با نخست‌وزیر مالزی و رئیس‌جمهور اتیوپی دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/461524" target="_blank">📅 13:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461523">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szMxxNuTxrjWhBjTEhbm84SiHPF-_-aKKYyqn4mu_fUvCnhp7wFnpnjXlJU6JgtIMJmARZdKnhT0HZ4pFXyHlr3DnYDpiBAqiOJAGG8FfGaKpmuz1mce57pPEPYEGW906IEsC0jnU3EqbfhRhdnqIJpI5K8vc2-qDRKjw-ULYLTSyK7Mzfy48kkItf7CW7-TSeWHtS46HxLI3jnMc72TVkt6IMTvCWQjm0PoA1UmuZiK3XMNTN5WdhszYaxHHhBjRwGLfOD8v7t24mIqGvDUStn2aBrQT4gukRoUw4lVG8XHKk7-ow2XNoiIG0mVXp97KMCWQaM9IGJ5F_ZOot_yjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ: پوتین مایل به دستیابی به یک توافق است و اگر زلنسکی هم خواهان توافق باشد، خیلی عالی خواهد شد؛ مانع اصلی ۲ نفر هستند که از یکدیگر متنفرند.  @Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/461523" target="_blank">📅 13:49 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
