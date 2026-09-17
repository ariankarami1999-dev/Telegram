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
<img src="https://cdn4.telesco.pe/file/tecJTruiXiy5IwUOpV9OAVtCL2OtqO_FGAyrgw4wuTaP9DfGFit6YvYRFmGh1cTmUhOYUPiGJSMnFob09nbOHGdlY7dt9z44PtDwp-D_3cWRPvzxGeqaQXw6k6shHsFrj28mJU-4aqRevT112nOVufHftKZ5ppBeL5mNqiTMqwudQL_Lt3D-3bNt5n7vvhYpnRdJNTtvfohpmTTtCqmAf4TvQNIFHV7wAQBwCRr4miq96rHDOhtSrJrRzZCwFW_b5lT64rzFUh_d7Pmrhu5zlBWhpdl9YsKHc0VqRdkiNj0Al2wKcM_2LuHq6zPoCZ6FfWQlQlq44wMATpgIjp8AVQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 106K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 07:40:32</div>
<hr>

<div class="tg-post" id="msg-71750">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65c03c4e5b.mp4?token=EtJOUDquzH6_xnY14pXeg1a5QGhrHH2r5wUW-Uwefm-yXerAVpooFiIs7FPAsIOFHWfzZSJ4lNk9_Tbd1wvROAVnJLzdQVOGyoKstBj8dM98bFaeSAK6_MYyQyme_jro1heXei8MhF6ReV9BGP6hZv7jWjS9TWPXSwLRTqCPD7gKaACmds6gC5Am3HaGHrBBRHlV1SYy4kQAWdNpiCrFU_YZedJxNS-A7iXIe46P3aRm0kSHKmShAZrmZ0uI3Dm6cSawOzYVqMJ33PxK_F00JIkeTwxNvsFj24zzMzrLRHH7q12PaoKWbVMK-Cvvo344a3_swLh4y7N0Nf5ZEicQjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65c03c4e5b.mp4?token=EtJOUDquzH6_xnY14pXeg1a5QGhrHH2r5wUW-Uwefm-yXerAVpooFiIs7FPAsIOFHWfzZSJ4lNk9_Tbd1wvROAVnJLzdQVOGyoKstBj8dM98bFaeSAK6_MYyQyme_jro1heXei8MhF6ReV9BGP6hZv7jWjS9TWPXSwLRTqCPD7gKaACmds6gC5Am3HaGHrBBRHlV1SYy4kQAWdNpiCrFU_YZedJxNS-A7iXIe46P3aRm0kSHKmShAZrmZ0uI3Dm6cSawOzYVqMJ33PxK_F00JIkeTwxNvsFj24zzMzrLRHH7q12PaoKWbVMK-Cvvo344a3_swLh4y7N0Nf5ZEicQjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا قبول دارید که آن‌ها به خاطر جنگ در ایران، نرخ‌ها را بالا می‌برند تا قیمت‌ها را پایین بیاورند؟
ترامپ: نه، آن‌ها نرخ‌ها را بالا می‌برند تا عملکرد ترامپ تا حد ممکن بد به نظر برسد. مشکل آن‌ها این است که ما بهترین اقتصاد تاریخ را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/news_hut/71750" target="_blank">📅 07:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71749">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad35ceb68.mp4?token=QbzkGb98kB_zHD6kYsYugXZtd72nwsNZ4y6CfR71gB76lat7D8lBg4cElu2DS-ssORo8AH5f39v2ZEONsUrZQWGVDDQ-qTRGGy-RVXhT3nK1Pf_IwDPUyhdMz4LhSI6-fJemM0Xagch5aJpkrtYU4oBwplHVzrBQ8FA78irxozsjiz3Sbcbu2ARRkjElngZBiQACsQRH0Y9lNchtlGowmSOOM99DDOeJi5XPaNY7p4RSq7K9C2sTBLoy8DMSccFDMOVBo9ZNvhmM5PxAIMQbfBq9_dciLIqMvSjvriDEO7FU5PGtIpFIh2tTaMtw_04QT8fg62kek1Ju6vjlRHt9hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad35ceb68.mp4?token=QbzkGb98kB_zHD6kYsYugXZtd72nwsNZ4y6CfR71gB76lat7D8lBg4cElu2DS-ssORo8AH5f39v2ZEONsUrZQWGVDDQ-qTRGGy-RVXhT3nK1Pf_IwDPUyhdMz4LhSI6-fJemM0Xagch5aJpkrtYU4oBwplHVzrBQ8FA78irxozsjiz3Sbcbu2ARRkjElngZBiQACsQRH0Y9lNchtlGowmSOOM99DDOeJi5XPaNY7p4RSq7K9C2sTBLoy8DMSccFDMOVBo9ZNvhmM5PxAIMQbfBq9_dciLIqMvSjvriDEO7FU5PGtIpFIh2tTaMtw_04QT8fg62kek1Ju6vjlRHt9hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: امیدواریم که به پایان ماجرای جنگ با ایران نزدیک شده باشیم. ایران خواهان دستیابی به توافق است.
خبرنگار: آیا مستقیماً از آن‌ها خبری دریافت کرده‌اید؟
ترامپ: بله.
@News_Hut</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/news_hut/71749" target="_blank">📅 07:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71748">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/news_hut/71748" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71747">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uwpWSAQaqKz5WgJlRrxug1TGwVjpRdLWXQDaepaN_UD_H60nGLOLnUOJkej2mp8Hr7lPDLQlKx90VP11YigIRNZL5vn1HZMFdU8B-VpeCakr1Xy5b50balhjJlCjWlTQTbikwF4USv376-bulfpNybIRp6EENRLvGK-HK6s9he8Xgf6eOHs4FNBhGbT9OmgirlQzXrCgL19GgxLt7EfCN98aZnDMkQyVhtG_Qc5gMUDitBLYSH9G1KEia07rVTgjXfJVbAgSgl7xr_CqQwbNh676QEM9gz995I4AvgPRDrYw_nw8R9-Ln0XQpL7oWponSW8u6bLegXi-Ll_qbLfKYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/news_hut/71747" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71746">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef2cf6cff.mp4?token=hEwv_Qzyw7444A_YH2BZZijpmXs67JtuvkHBlUVG5GxbwbwxGG0KtJMcnUTfiMWWYKcCgnT50Pn0mhfVkpM7aFMSmj2svAiBuUSeAtZ7vLZVeKVhlE2IQ6mV46GhbRXV-ROwwbS5i4bzkNkD-WsfOqPokrd2A3hlO3I4DEIcHL-moWGb2Q_1X0WsBLUyBBEui_7DN_5DE0K_CCXoaL3frU3q4mITwrDWHdnvjT1f93FqrJA2SrZvsDx_ghiycMvPsryRcUpkCgmoqSjV9cH1nxa--hUegIlJJo5CtuAaxE_hlRhUsO_c-NwFzZ3PSDXt5h22zVE3__egqqYTBTygwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef2cf6cff.mp4?token=hEwv_Qzyw7444A_YH2BZZijpmXs67JtuvkHBlUVG5GxbwbwxGG0KtJMcnUTfiMWWYKcCgnT50Pn0mhfVkpM7aFMSmj2svAiBuUSeAtZ7vLZVeKVhlE2IQ6mV46GhbRXV-ROwwbS5i4bzkNkD-WsfOqPokrd2A3hlO3I4DEIcHL-moWGb2Q_1X0WsBLUyBBEui_7DN_5DE0K_CCXoaL3frU3q4mITwrDWHdnvjT1f93FqrJA2SrZvsDx_ghiycMvPsryRcUpkCgmoqSjV9cH1nxa--hUegIlJJo5CtuAaxE_hlRhUsO_c-NwFzZ3PSDXt5h22zVE3__egqqYTBTygwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواضع حوثی‌ها و تجهیزات نظامی آنها بار دیگر در مناطق خط مقدم شمالی استان تعز و اطراف المخا هدف حملات قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/news_hut/71746" target="_blank">📅 01:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71745">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd261e6ac4.mp4?token=rigTkHFkbmeEhC_XxdF9NTGAshucOCP7f0C_gRUJC5pv2Bhbe_VHYhCPnKFqhpJ1mhmbaJ844NI6kbQ-EQls8KsSwayFtH83yzEoF7xoc-hUfG_MOqH4VB5b5tLqkF-qyrOkOfgMy6oqLKV0fsAi8R23spX8sUXMBhkuRH1VjN6KBAI80M-KLLxJJy8IMrQ4wODWWuMEhYX1QoDkv3oh6dxnxUYx2cwKZVoFjJilaGqM1duxg8BcU5tSf_hfE-v1eWW3DLLcgbKtHoRPZyKTlp4vGpjm-YDmvbYjK3nLCKTwuXrrPrdK6Bq9YxjNsbMXyPKrM0YEgcr7UV5qiO31uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd261e6ac4.mp4?token=rigTkHFkbmeEhC_XxdF9NTGAshucOCP7f0C_gRUJC5pv2Bhbe_VHYhCPnKFqhpJ1mhmbaJ844NI6kbQ-EQls8KsSwayFtH83yzEoF7xoc-hUfG_MOqH4VB5b5tLqkF-qyrOkOfgMy6oqLKV0fsAi8R23spX8sUXMBhkuRH1VjN6KBAI80M-KLLxJJy8IMrQ4wODWWuMEhYX1QoDkv3oh6dxnxUYx2cwKZVoFjJilaGqM1duxg8BcU5tSf_hfE-v1eWW3DLLcgbKtHoRPZyKTlp4vGpjm-YDmvbYjK3nLCKTwuXrrPrdK6Bq9YxjNsbMXyPKrM0YEgcr7UV5qiO31uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پسر از همه شانسش یک‌جا  استفاده کرد...
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/71745" target="_blank">📅 23:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71744">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1b9a723e6.mp4?token=ZjoZ_KcJNv5nkrSeCmBDv5CN6difjTqVS5Mr7i5Evm90mipVBUXZYNPqM5dDfOWFqyQ_-b3fBZRYoJA5C0lu9gQhwa1U2gbRGO-LTySrT12mh9P2bDIpte89wXjhbQ5oKMLWbhIjO5rR3LUP6z31kV2aeizHxi9bqlLeb7uxRuAHSHIDX3rupwiAGvGWP2sfc5Dr3eLy_ioG97wVkXRDDKtk5x3yLWOfCnkHh_Syie0MKesh9L0st6Jw328ypl7jroQQsT8N9G93bpbjyWnbsujBj3bt2VD3nOJLXxPRJO3QGp4A9ERYukN4fG4r3FHk6bsxQ0lAkZ5FWp_Rh5ZWeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1b9a723e6.mp4?token=ZjoZ_KcJNv5nkrSeCmBDv5CN6difjTqVS5Mr7i5Evm90mipVBUXZYNPqM5dDfOWFqyQ_-b3fBZRYoJA5C0lu9gQhwa1U2gbRGO-LTySrT12mh9P2bDIpte89wXjhbQ5oKMLWbhIjO5rR3LUP6z31kV2aeizHxi9bqlLeb7uxRuAHSHIDX3rupwiAGvGWP2sfc5Dr3eLy_ioG97wVkXRDDKtk5x3yLWOfCnkHh_Syie0MKesh9L0st6Jw328ypl7jroQQsT8N9G93bpbjyWnbsujBj3bt2VD3nOJLXxPRJO3QGp4A9ERYukN4fG4r3FHk6bsxQ0lAkZ5FWp_Rh5ZWeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نکته‌ای جالب درباره جنگنده سعودی که در مأرب یمن سرنگون شد:
شماره سریال (5529) روی دم هواپیما قابل مشاهده است که تأیید می‌کند این پرنده، مدل بسیار پیشرفته F-15SA ساخت آمریکا با ارزشی بیش از ۱۱۰ میلیون دلار است.
این هواپیما دو‌سرنشینه است؛ بدین معنا که شمار پرسنل اسیر یا کشته‌شده شامل دو خلبان می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/71744" target="_blank">📅 23:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71743">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb7be6388.mp4?token=i153gskJwT4AWFMJ3VU9hKpPReRJMIEhsfDfpTILfxcQlfmnDO8UQHMdj_6EXlRNeGyCzuJcKg62pVMkndScsK_eqSPymfRc5j9hczJFwjukTnikaNdMgXCn17x8BaJk46yIdTVtUWHFUWE8dQKF6RcJZfAdnJykRoaHH2c7gFs3Hb6OXD8zxJggMbvbVj-IH1dIv-3evn-Kr8FYn5unSxxa-Xa9EGZsTElYZc6tlNjrwZRM9E96w0IY4ElNKomi5xhzXR4g31X62HT02GiJQLodeYXgrLmi7zONuMC3PkzCHN8rU90IIMj0VGdFzfsBDXAlux3ioxepX4W6zhGdPlnKLlmiWzvHivdSCNEMB83XZnRMaQTT5I81QNubCxdIhVPwDGUhFRrxtd4qCoVzhbgE51UTQXfOH88rbWZTv9x6pDn7aenCxE3AVe10K-dxG1_surmNRDAlvEJ2MIorSMxES7pXfyfL9URlr9YTZub8wCj-MgL5gBX2YxS7ZfCFnCREWSWquP-20j_n6Y93Coh-1JadCPONIR_K2XqvubtRgQmWlKB74CgspSw4upnQ71obuSaAw6LueSYD5cfYUSAoRHuBVuz1j17kY4hd78TPnq06tPnS-NBmwLr1HexFjIlEW18RSZXpOjZ6Uv9cPKiknj7F8yvycIA6KTBm4eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb7be6388.mp4?token=i153gskJwT4AWFMJ3VU9hKpPReRJMIEhsfDfpTILfxcQlfmnDO8UQHMdj_6EXlRNeGyCzuJcKg62pVMkndScsK_eqSPymfRc5j9hczJFwjukTnikaNdMgXCn17x8BaJk46yIdTVtUWHFUWE8dQKF6RcJZfAdnJykRoaHH2c7gFs3Hb6OXD8zxJggMbvbVj-IH1dIv-3evn-Kr8FYn5unSxxa-Xa9EGZsTElYZc6tlNjrwZRM9E96w0IY4ElNKomi5xhzXR4g31X62HT02GiJQLodeYXgrLmi7zONuMC3PkzCHN8rU90IIMj0VGdFzfsBDXAlux3ioxepX4W6zhGdPlnKLlmiWzvHivdSCNEMB83XZnRMaQTT5I81QNubCxdIhVPwDGUhFRrxtd4qCoVzhbgE51UTQXfOH88rbWZTv9x6pDn7aenCxE3AVe10K-dxG1_surmNRDAlvEJ2MIorSMxES7pXfyfL9URlr9YTZub8wCj-MgL5gBX2YxS7ZfCFnCREWSWquP-20j_n6Y93Coh-1JadCPONIR_K2XqvubtRgQmWlKB74CgspSw4upnQ71obuSaAw6LueSYD5cfYUSAoRHuBVuz1j17kY4hd78TPnq06tPnS-NBmwLr1HexFjIlEW18RSZXpOjZ6Uv9cPKiknj7F8yvycIA6KTBm4eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش خبرنگار فاکس‌نیوز از روی عرشه ناو هواپیمابر جورج واشنگتن؛
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71743" target="_blank">📅 22:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71742">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مجری از خلبان آمریکایی میپرسه چی بهت کمک کرد با اون وضعیت از کوه بالابری؟
میگه هیچوقت اجازه نده کمبود انگیزه باعث بشه از تلویزیون جمهوری اسلامی سر دراری:))
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71742" target="_blank">📅 21:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71741">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60ea75ad1d.mp4?token=Mo0WCNF3Ahte5P2Nd9hNBi9L9diC7_c7TQpwusMr4NehkSmJOVva2bewzlG-gev_oYgCiTHacdCcvBLUut0ypdwP6iNMCYxpvmfC6fXyVW9KIvBIYQSn3SFwjP6RcDULbF4PK5xEgjQvVQrhldUyHKAEw3AHolqQtZYQMLp5mcF2MDbOyEH_lb-XXRg3VtEK59Uhjub5ALFV0Q5DPzWeygRev_5545yBaKyxryuYCxtDPlS-6U-F7mZWMoIX5-yXFjW02nZbPDYfNn3c2vZ9crjRdi5hEqz2yAJ5ylFaPxNldCkcEg6WAHEif34orkbRVqVVTaOtY1EQiaIX6fV8NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60ea75ad1d.mp4?token=Mo0WCNF3Ahte5P2Nd9hNBi9L9diC7_c7TQpwusMr4NehkSmJOVva2bewzlG-gev_oYgCiTHacdCcvBLUut0ypdwP6iNMCYxpvmfC6fXyVW9KIvBIYQSn3SFwjP6RcDULbF4PK5xEgjQvVQrhldUyHKAEw3AHolqQtZYQMLp5mcF2MDbOyEH_lb-XXRg3VtEK59Uhjub5ALFV0Q5DPzWeygRev_5545yBaKyxryuYCxtDPlS-6U-F7mZWMoIX5-yXFjW02nZbPDYfNn3c2vZ9crjRdi5hEqz2yAJ5ylFaPxNldCkcEg6WAHEif34orkbRVqVVTaOtY1EQiaIX6fV8NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاله مرزبان بعد از دریافت جایزه بهترین بازیگر زن در جشنواره ونیز، جایزه‌ش رو به زنان ایران تقدیم کرد و گفت :
میدونیم که سخت ترین دوران زندگیمونو تجربه میکنیم ولی نباید ناامید بشیم
یه روز امیدوارم رویای مردممون برای آزادی و آینده بهتر به حقیقت برسه
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71741" target="_blank">📅 20:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71740">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2env_GZjwfKzR0en6Xu2ebrFjjiIOgU4vIdt6DxOJoLDJIpiOZ6Xh9zaEegL9FDDoAmB98RMhwSx2V67bbj-V2S_0zYybJEYaz3UwjJndO4aR_lBHmYZRwxD394hkaU7YxYwkFgD4cLqWR60PPAXUXdyUVu0Q1V1YxqhYt_m-bY5kgT2aNODcqpaH78iYnoP2hz0rzOSgJYAaSoNEwI0R3BGW2kUWBiU_SlAPnkMWDqF5oUZPLqKYQJIbR0qhnMwPKQLkkLfvMVl5a7RDBvTmvOCVa5IJkWllbQVDFibWQ-JuJVhfH1nKUdzPNi-FlSPIaGXI6iVAuNS7j0Ocks6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعالیت گسترده ترابری نیروی هوایی آمریکا و جابه‌جایی مهمات میان پایگاه‌های این کشور در اروپا و خاورمیانه امروز!
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71740" target="_blank">📅 20:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71739">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وزارت نیرو از پایان قطعی‌های برق خبر داد؛
مصطفی رجبی مشهدی، سرپرست معاونت برق و انرژی وزارت نیرو:
خاموشی‌ها از هفته گذشته به پایان رسید، امسال ۱۴ درصد برق بیشتری به صنایع انرژی‌بر کشور اختصاص داده شد!
بیناموسا میگن دیگه خاموشی نداریم اما هرروز داره برق میره
😐
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71739" target="_blank">📅 19:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71738">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iACmsZGePxlMo6MJDj5T7fx5ol983vfyU7BTB5bMidZSn8kkVpe1SR3oDskotu5bBJKW-xuApcLOk5kxEMBzz6uo3jUxs4A2NWd8B_SHJkk2GXGgPu8W46Yr-ruuHEENgv6aFX7wg5Mo1FoW5QN74wl5CTsOyCk4NW4V543oL9cjccLDmxra_zASTPrO-Yi7WxTeUHXuGqiO9rJ6sDiTIVmqhB9Peh_lD-Knu0VTkWvJJ9nPa8RDuU7oD0SDuEQjn7Wg9Z-KjGQXBkWdsXZEf5pgO0D06xaeL1_EAYuGAz3UK_lgdwiqwKrqj2e3_vlCbiqiplzsiQsZO-qA0lSa9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور، به «نیویورک پست» گفت که مناقشه میان ایالات متحده و ایران ممکن است ظرف چند ماه آینده وارد «مرحله‌ای بسیار متفاوت» شود؛ او با ترامپ هم‌نظر بود که این جنگ می‌تواند «بلافاصله پس از» انتخابات میان‌دوره‌ای به پایان برسد.
ونس اظهار داشت که تردد در تنگه هرمز به «بیش از ۵۰ درصد» سطح عادی بازگشته است و استدلال کرد که ایالات متحده دیگر دست به عملیات‌های تهاجمی نمی‌زند، در حالی که ایران همچنان به حملات گاه‌به‌گاه علیه کشتی‌های تجاری ادامه می‌دهد.
ونس گفت: «این ماجرا در واقع دو مرحله دارد و مرحله اول به پایان رسیده است.» او هدف اولیه را نابودی برنامه هسته‌ای، توان نظامی متعارف و قدرت اعمال نفوذ (توانِ قدرت‌نمایی) ایران توصیف کرد.
وی افزود که مرحله دوم، جلوگیری از بازسازی آن توانمندی‌ها توسط ایران و در عین حال حفظ ثبات جهانی است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71738" target="_blank">📅 19:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71735">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/apeV68qyoOPErigKe1NMJMej3K0Yh50RufINYjmJtPhcg0cXBSqZcowkCZE89x3Xc994LzbfxyZMRF54m2QP-X76H9jIa3Wnw2TZFF5N7wUvWM7JrCDxq96b2Wd6bOZW7DXifZ2V1bxzvLcOvYMgICPnWooMyd8iIYyWueIcsrDAauSYbNtiKhb2F-JyxVdTQruK4NxoWN5dZcQ7_sdI49Jm10J7lbka_ZxAfFgVttAkl3rSR-ru8J-qnuvmggJ5zB729mMcHFUXZGE6dbIm69RtCQoYO3S738W0xr8_IcPPhFg4gL7L41wn5wUZXswSvInj6JdEz1c62bfTTek81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bao42zozIJkvHyZ7ixLEXhZkDiNUx900lxwTti4d48fe7uL2TaUdwGfah029mmbGsufxHiyiqkPwQpiHIQhwBNlMwKg-IQfOWx_IXT3YXpCEM5EDh5q-DM6_m_dH8vu2t6-YWMgk4G6C2Y7cagfzg98Y8S80O23tkLTD0ZiZY-zUogYWtVvYyrzngOD87DRDNch2PARuANp0FEzHaS900sqq7w32yfV02fYha-8rQy1OzzhqmW3UEglebZPA9V7bZxEuboS2XwQs2SvEVgK_i43CuMG-jq_q_eWnOSgRlGzQSW41jjTfSuoPrdVuRDqMecwGpf8eteB0dkbSLBGvoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حوثی‌های یمن تصاویری منتشر کردند که مدعی‌اند سرنگونی و لاشه یک جنگنده اف-۱۵ عربستان سعودی در استان مأرب را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71735" target="_blank">📅 18:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71734">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f8c75931.mp4?token=AKZfWx21y1b_e_aiGXF9F2JxZCX701qpe94jSgNXqFH3jb4Bt-mLZ2i5WtM_BY2EcoUWbDf3FSuqY73NmixV2Q5pV48Rn8iC6YKDX0pnf4TKCuSkYwz-iSYoc-L3I39D-Lav3C0aaCTtg6PVNN3uiYYqGULR5jqY2zDTDcvJS-ZT2KAWxT8t3TzRkTDcHw6_KHlhqqftDUgDBRFYvDSoZd_sBB_7og3HGQo5yQJMskKDNcpo8D8ws7i-xgGe68-C9rS6TeBeDaXuO1CLcz6PM7Kli8SrTwIrczlVZfOoMilzR-iKAe4lMlJtvroDEN0vVcEh8I6dRPphe4lnZU5tHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f8c75931.mp4?token=AKZfWx21y1b_e_aiGXF9F2JxZCX701qpe94jSgNXqFH3jb4Bt-mLZ2i5WtM_BY2EcoUWbDf3FSuqY73NmixV2Q5pV48Rn8iC6YKDX0pnf4TKCuSkYwz-iSYoc-L3I39D-Lav3C0aaCTtg6PVNN3uiYYqGULR5jqY2zDTDcvJS-ZT2KAWxT8t3TzRkTDcHw6_KHlhqqftDUgDBRFYvDSoZd_sBB_7og3HGQo5yQJMskKDNcpo8D8ws7i-xgGe68-C9rS6TeBeDaXuO1CLcz6PM7Kli8SrTwIrczlVZfOoMilzR-iKAe4lMlJtvroDEN0vVcEh8I6dRPphe4lnZU5tHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی تهران یه کافه مذهبی به اسم ام‌البنین افتتاح شده و مخصوص آدمای مذهبیه و ورود افراد غیرمذهبی به اونجا ممنوعه.
شنبه هر هفته هم سفره‌ ام‌البنین دارن!
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71734" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71733">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71733" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71733" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71732">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQNJ-__BaFbRmtpxOCXAxwsj6x2wM_2-gjM7DfHO-djrfGDAvltkzmHYTHZvChJ-bZBsD3m6dOrQesm8oQ5CVFbPfFZ_A6FFqyx8swNYYHHcIfVeI7gnJ53eH3ISQyu35gKwZTbjc1dbFUFbJmXAu6WzI0LBty2sGK2j6mhcfv4EstwU7vDt64Rzeq_VzAoiNHlvkv9h_5VkQ4urs8gunSO_T8VLP2uR1w8UZtel_9i2Q34aJUemsGS_iOC1JZG-N0V9BkDWeYOQVrmwc28zjJov85PvEIg-NQbJDDfCMj8gPX9PeGRJKjX2zIZdRAoSQIva3XlgoQy7lythOMNeJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
راسینگ سانتاندر
🆚
بارسلونا
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
راسینگ سانتاندر: ۲ برد، ۲ تساوی، ۲ شکست و ۹ گل زده
⚽️
بارسلونا: ۵ برد و ۲۱ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71732" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71731">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534f93c783.mp4?token=o_cS7KaDC9YXlOb4-vOTogvNUZKBfOm-cpIGJeQ1GeA1LelSxxy9V9xqxKlimNb7IEeiVJe4tP8ZCtx1JC6WMPLkwwmWV99si4RH1EIP551bDA-9nQIl_bbgkW5m6aN41gLjC5aDCVi2-nWYHfIl6IoKalqtkf7yz-vU3Kmi-U_Euava0jNF5RE9LOtxH4m5c2ST_Y7_aJaejTTSqMwayC6mjPhITAqt0SePaBm69Ppns78ujQCc-ZNmFmdwNDYbfHjNq5OhcwQk6llobctgY_FdzOJM6Eveai8zbWR8Pkfld6YyiHsq7H2G9s6UWjVuK7IlcHqQPescZuvbDjOgMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534f93c783.mp4?token=o_cS7KaDC9YXlOb4-vOTogvNUZKBfOm-cpIGJeQ1GeA1LelSxxy9V9xqxKlimNb7IEeiVJe4tP8ZCtx1JC6WMPLkwwmWV99si4RH1EIP551bDA-9nQIl_bbgkW5m6aN41gLjC5aDCVi2-nWYHfIl6IoKalqtkf7yz-vU3Kmi-U_Euava0jNF5RE9LOtxH4m5c2ST_Y7_aJaejTTSqMwayC6mjPhITAqt0SePaBm69Ppns78ujQCc-ZNmFmdwNDYbfHjNq5OhcwQk6llobctgY_FdzOJM6Eveai8zbWR8Pkfld6YyiHsq7H2G9s6UWjVuK7IlcHqQPescZuvbDjOgMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این کلیپ تاریخی که چند نفر میخواستن با برنو، سوخت رسان و جنگنده بزنن
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71731" target="_blank">📅 17:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71730">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فاکس‌نیوز:
یک کشتی طرف قرارداد ایالات متحده در نزدیکی تنگه هرمز هدف حمله‌ای از سوی ایران قرار گرفت که در آن از چهار پهپاد و دست‌کم یک موشک استفاده شده بود.
این حمله منجر به جراحات جزئی، از جمله عوارض ناشی از استنشاق دود، شد.
تعدادی از کارکنان آمریکایی در این کشتی حضور داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71730" target="_blank">📅 17:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71729">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeJwKBecWeh-UZwLT6BEjC324XgvPJgR3qIp8uMjdRgHoDH2XQsEM5OAe7zBAyFrQSzCwS4C6HAVNGw_2fMgAUrLJrW2q28W6pTvlSoKfNIuPDTQPnio79lk1NBmE7MzbDA-_DoWGmyJNOgeia5oiWlN-mNAXARO4vt4CD0F2GsZHnrV0j5dr6tgrblDb2SN84rGPcSxGHypbViDOzUQuCD6pqvyb_Ui6JAuWDNPY3RBk50oi4ScvW4LKMKJgA-GB5ItOM7apdJk9YA8ynMxWkQV658OtR4hglDk9jLNaR4eJif-y08b5o0bo7bbJozSW79bQrciicsukMu17rVyFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شده در تجمعات شبانه:
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71729" target="_blank">📅 17:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71728">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2421361f81.mp4?token=gFv5jUUJWZIdH8dUnBpJul7WIEB8uIuc3gZtfTrMsUUq-M4TXb8mxbHUlW5yXQb57A6lwoglsJY7UNFX1cCo9L8uTy8Uhukx75azNJvWls2priRcv8Q6ex4pt28z9sLO9gLYTlHrUae9FiQ6nZoFMH9qHa-jhsiAUrJBYKEbQJ9IszAy55FG0TojQqcQZRj1bw-x8sAQCRcg4ZI8-qoadGrfSR49VG9cDQaE5yEntvjzIcpfIqhxbBpXE8MWcJEPy39A9bYhU584QPKd7q4j2wh5ae09IrqBiinH9aHz7CzPLZQ3T7xn9mNMX29gmeYc6NovxB07-KoDdRaqP6HhSo4-8F9aLqeYTCgy_7Z295A14pZW0cMrj75bBQgtEll7U91WW8wDDCyZBB6HkZilzDH-8gsLDqcABgpl_SfgPTYqu8Sddac4Ha-8zVsLDUDDvxFivYLpTFurlehLjceZ1Lv0nX38IjG1CWTOimTChaWpCxn75d_N3-HG8wZ_YekGCjUHpNqA7aE9bdlevRgh3QVU5XTtotQqUoEV0_Dv-5liJRvxuIg25x1wPUutxwklGU3LVnU3bVNNtRkOdKjgcID_66AkQsnx9f2Dqo8VOJy4UT8GXKFb0uxPzGnMA3r7Uiup0LUceGlzQ3mVySLXZH1ZANLLITxnjalNdhCn5SU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2421361f81.mp4?token=gFv5jUUJWZIdH8dUnBpJul7WIEB8uIuc3gZtfTrMsUUq-M4TXb8mxbHUlW5yXQb57A6lwoglsJY7UNFX1cCo9L8uTy8Uhukx75azNJvWls2priRcv8Q6ex4pt28z9sLO9gLYTlHrUae9FiQ6nZoFMH9qHa-jhsiAUrJBYKEbQJ9IszAy55FG0TojQqcQZRj1bw-x8sAQCRcg4ZI8-qoadGrfSR49VG9cDQaE5yEntvjzIcpfIqhxbBpXE8MWcJEPy39A9bYhU584QPKd7q4j2wh5ae09IrqBiinH9aHz7CzPLZQ3T7xn9mNMX29gmeYc6NovxB07-KoDdRaqP6HhSo4-8F9aLqeYTCgy_7Z295A14pZW0cMrj75bBQgtEll7U91WW8wDDCyZBB6HkZilzDH-8gsLDqcABgpl_SfgPTYqu8Sddac4Ha-8zVsLDUDDvxFivYLpTFurlehLjceZ1Lv0nX38IjG1CWTOimTChaWpCxn75d_N3-HG8wZ_YekGCjUHpNqA7aE9bdlevRgh3QVU5XTtotQqUoEV0_Dv-5liJRvxuIg25x1wPUutxwklGU3LVnU3bVNNtRkOdKjgcID_66AkQsnx9f2Dqo8VOJy4UT8GXKFb0uxPzGnMA3r7Uiup0LUceGlzQ3mVySLXZH1ZANLLITxnjalNdhCn5SU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیویس کیس سخنگوی سابق نخست‌وزیر اسرائیل:
دیکتاتورهای ایران ظرف چند هفته سقوط خواهند کرد؛
دو هفته، سه روز، شش ساعت و چهارده دقیقه دقیقاً
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71728" target="_blank">📅 16:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71727">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de91f58f7a.mp4?token=JGO-D1d0QwL0Ygm-mf8L70_3J3zTx-KI4MY8AHlQiCJ-eblWFca0Awad4oQRQN9ibHSa9SAcuD9lHrjQG5FiDfTXiOmJqyK_aigtl4mENPfp11-1cWY5AYSFx-BZkeSde7K_s-tjl4J0YqPN6f--OE3oNAf2KX1khC6uG3hGMSJtY6jdupxsxfTFMDjcUrMncT2NrWiKHTNcXcm48Jyhc3AEJmtbanRTi31le2Cy8WhnLfbSEkQw6B_mOEG1pvtN2XGamLYwSTrHrjLYbBNnycflEEs9ExP7PFnOBShatUzTxj4RqTZiJaAP8tYvnrF3Ud-k2Jiiri_3nSNZG3QX6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de91f58f7a.mp4?token=JGO-D1d0QwL0Ygm-mf8L70_3J3zTx-KI4MY8AHlQiCJ-eblWFca0Awad4oQRQN9ibHSa9SAcuD9lHrjQG5FiDfTXiOmJqyK_aigtl4mENPfp11-1cWY5AYSFx-BZkeSde7K_s-tjl4J0YqPN6f--OE3oNAf2KX1khC6uG3hGMSJtY6jdupxsxfTFMDjcUrMncT2NrWiKHTNcXcm48Jyhc3AEJmtbanRTi31le2Cy8WhnLfbSEkQw6B_mOEG1pvtN2XGamLYwSTrHrjLYbBNnycflEEs9ExP7PFnOBShatUzTxj4RqTZiJaAP8tYvnrF3Ud-k2Jiiri_3nSNZG3QX6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلیپ دعوای این دو تا بچه گربه خیلی وایرال شده، از بس کوچولو ان، دستاشون به همدیگه نمیرسه و رو هوا همدیگرو کتک میزنن :))
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71727" target="_blank">📅 16:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71726">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f04518ba.mp4?token=hdecSHLXWph5asYGUquJMQv-QJe_0fDYlGtEEsBoRWX8RjJuhMJxKfFMjAapkWmVbt7BNvSUHe8VkSxLGP3ksaAQipN103kvpeMGDADGIhKyObFLSKTpDy3XXYqfHfEa3TB6BiH-TAQA8Pks0PMKPjjyZgKVmwX7LrQmcEQCzNqInv0RMmYL_-dvzWB7SwOyzxiK-9GJCMOdpRbsp_Wd3MgJogpT74NMZFDfUnTPjrpuZYemyG3scwyvDnVDRZKRScVN42abuK9maBaSbKMyF1VyeUHf9qdjMn9F4tPmWyZIqoBIuAWx-GZ9qIfdp4yjK7k8P7Qqo4T40MJRZtlGoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f04518ba.mp4?token=hdecSHLXWph5asYGUquJMQv-QJe_0fDYlGtEEsBoRWX8RjJuhMJxKfFMjAapkWmVbt7BNvSUHe8VkSxLGP3ksaAQipN103kvpeMGDADGIhKyObFLSKTpDy3XXYqfHfEa3TB6BiH-TAQA8Pks0PMKPjjyZgKVmwX7LrQmcEQCzNqInv0RMmYL_-dvzWB7SwOyzxiK-9GJCMOdpRbsp_Wd3MgJogpT74NMZFDfUnTPjrpuZYemyG3scwyvDnVDRZKRScVN42abuK9maBaSbKMyF1VyeUHf9qdjMn9F4tPmWyZIqoBIuAWx-GZ9qIfdp4yjK7k8P7Qqo4T40MJRZtlGoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه رستوران تو آمریکا باز شده که تم بیمارستانی داره و تمام‌ کارکنانش کاستوم دکتری و پرستاری پوشیدن و اگه غذاتونو کامل نخورید باید براشون قمبل کنید تا خانوم دکتر بیاد شلاقتون بزنه...
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71726" target="_blank">📅 15:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71725">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c76d3eade.mp4?token=BrSwmY1tzPnuiEbR4HPZJyXs2VkPR4WgsIjVkZmCXt2d7M-KBt_Sjt2LzE9UGbnkFxwAobWnQPCURgKz71vBdjeSb7TUo1NbmxJLsLFuzTnIyQACdzub9ak3qB4GnTTYvJYMRsIZnSIO3C4YoLTwwhGDNPfz00ubTaQfHV61YD9IgRxa7hHOjgSKn2uQ4Oww6sgu08VN3ZfYTfCVU6ZoyZeGkYMx6CrYH_grvHSHKTaNsKtmHlQwuQI5ilqgJkOsaOcmP8B2oNmOHeUhaFcUMaNRcDw5FcsEGHtXfj1Y0SbRdyJxC8sr-fZY8Hs6ail-dybcUFfM-JMre0BjKbjo8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c76d3eade.mp4?token=BrSwmY1tzPnuiEbR4HPZJyXs2VkPR4WgsIjVkZmCXt2d7M-KBt_Sjt2LzE9UGbnkFxwAobWnQPCURgKz71vBdjeSb7TUo1NbmxJLsLFuzTnIyQACdzub9ak3qB4GnTTYvJYMRsIZnSIO3C4YoLTwwhGDNPfz00ubTaQfHV61YD9IgRxa7hHOjgSKn2uQ4Oww6sgu08VN3ZfYTfCVU6ZoyZeGkYMx6CrYH_grvHSHKTaNsKtmHlQwuQI5ilqgJkOsaOcmP8B2oNmOHeUhaFcUMaNRcDw5FcsEGHtXfj1Y0SbRdyJxC8sr-fZY8Hs6ail-dybcUFfM-JMre0BjKbjo8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله افراد لباس شخصی و آتش به اختیار به یک رستوران در رشت به نام « سحرخیزان » و تخریب رستوران به بهانه حجاب⁩⁩
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71725" target="_blank">📅 15:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71724">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBircfuAO4fQzHEkv24keVbIIcFATHGqTWbWSmqiLimpf-nUCUNF1FdALPIMHo7DzlwkBW-SI_RzTFkVT0pZ0wCaQ-jgJDToLG0ZuUn3kw8zLvbMgTdThKbXtZpL7YGu6dgsmKPLTg09N2aLCHuN1oqGgDq4iFx94IJI3k97oCByNF9cf30_vt2d5myiAKSmknUxgnLZ1c-mHZZFdetTsD_2SW1bxtCUv3QCo4cJDD0N7q7Bb3OL6QWKg1UieZhKysyYZApxUiRlmiq24XJkce0w2aaRNVwjPnV7jqwmX3g57ODiLOwnBwOZkocaIZ-CRGkVhjn4xYifna887_UD1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب حوثی های یمن به مکه مکرمه حمله کردند؛  سامانه‌پاتریوت شیطان‌بزرگ مانع شد خانه‌خدا توسط حوثی‌ها نابود شود!  @News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71724" target="_blank">📅 14:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71723">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b212130ba.mp4?token=oPY3whaWuoxiLL4qg8vdKDKG13Xz8p-FTXQdJ9Y5uTCCsTTmy-axF9Lcg00Xr1nPWFxJww1nNmqOylKYCFSdS14sxcL7bhZXfP92gjYE8EnJZ7KeLt1li3OCkIGT4hty7d8U-koRnC_ByoMwxvt3xBCflI01yOuuBxBFy8L4d8FjlvYRAsk27ALfvb0z2ALa80tNfn3VIZZlktjmn8PCGhosMoTc8aPyAK8qPKbv626pIlfioCovZE7oMqYtT8OYDKSMivljM8QOdPk1iU160MQJE5Uf4Tk2U9V30FnESEov01zy4r6f1WaGN8kTigXa6UsBFYaFPov9JrETMSkHyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b212130ba.mp4?token=oPY3whaWuoxiLL4qg8vdKDKG13Xz8p-FTXQdJ9Y5uTCCsTTmy-axF9Lcg00Xr1nPWFxJww1nNmqOylKYCFSdS14sxcL7bhZXfP92gjYE8EnJZ7KeLt1li3OCkIGT4hty7d8U-koRnC_ByoMwxvt3xBCflI01yOuuBxBFy8L4d8FjlvYRAsk27ALfvb0z2ALa80tNfn3VIZZlktjmn8PCGhosMoTc8aPyAK8qPKbv626pIlfioCovZE7oMqYtT8OYDKSMivljM8QOdPk1iU160MQJE5Uf4Tk2U9V30FnESEov01zy4r6f1WaGN8kTigXa6UsBFYaFPov9JrETMSkHyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب حوثی های یمن به مکه مکرمه حمله کردند؛
سامانه‌پاتریوت شیطان‌بزرگ مانع شد
خانه‌خدا توسط حوثی‌ها نابود شود!
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71723" target="_blank">📅 14:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71719">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z7dNxcSUyAkuiFcY9FYd2jAisy2gWE0Q7zbHqy08JDZ9jNr0NrX5oqNr8hivlhLDAEnK5PZ4DLUx_wc1794ttfcE_ElbhpholqwmDs-RlISj8DljEfA8AUWeYBf1MOl80q_93GeqvchdugMsCk_Abc0zCfHtIP8VHmqeeCxF1H_WO6d6a4P1S5oCvqWfmFj7_6G6rf35vZcgv_Sllv60PGEwA-u6knU_rCOdtOqPfNN-xPeMS0H-njZy0R7eXOlRg19pP8MrQyedYhvUdBcCYZQhpEeW0qSgC-MGfyBF_L-xcuCR6iMC4MRuGnOPtDupjHEdLQ7x1GrzflJwVwmBjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pW12F1okZyW41x2Th-2ai8PNirE9wBFFzGg-OAtL-sPXxIrneESWx3FFXZ0RDtGXajS13sCCSKmx66pDp2MTcBG5s7y0PBEYC2J3tw9hU0eK0s5lz96-BI9X3iBI3nKwvFDkypNRZNy9ot6nU2Geqg7eIOTxMUeyTH2X6C2DhBzU2xDugEcMx9fKo6mw5Q9rRsqJFerGDXdVs4KvSow2I0-7TH6WOvtz48hUIh9UvHjb8Fu4gDozknrXqOee8p14PhXoKtPdsDs4FpXYu_EHLrcmNpsRClJQabwXo-aZkfsEX3EHptrZLhMDrTGluK9izfRZWfhHTu7I3Ps6HTYE0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BSqxL8dyUaTmptnwg16rHmEiMOLdUc2vVPewk1MDC3TqFVm_MOuxqTCBNfm2wTUqkkCrChL6Ae1wWXztAb2aGXrKBpy43oCTB5vqG-OkZakmGZ7C-183lOWlRiONpnjMecVGMsKILQLaDxE7irT7rwuq5-0MOqnKg4LEaA00obz3v7nCbgk_V8aVMyxmYnUFtztv1pDQryYyW6mhHQW140mHE5K0JtS0PAp_JFZCRa7G3tlJjFmMtFWq9TSwQgPDWYzg9uAW0bpITSb6kvpMkYvL-uVfOjptRmBwSbMhM3vYvvnSq1R5D6vLda5iT4f8Wo-nOf1Jt32wvg7qMJtwYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B0c61SOWqDCkBmcaRRtko9loo1qi-BSuTDp10wsgn0cUGceoZAeVLtpoyJFTS8PYw507aXUmArOOHSqCVhHwMg2IdE8HS7KinFmQt1Rt2v4lzMy94ZwIayjvtAGR31p3j1FbfPxv40iPL8OFUgFeQa9fsHvHjAbCzKb69Snpq9sV9shYJUMMyQx5itmZUsU3zrA3t7vajPZ0rnbyBpmLgUrh7nwTRQGTJcXiSIDncD81jiL1Lx4FdcOSLaLmh5dL0hDpfbXliHgJ8EXLiyeV1qjv48ZB9zVr_T1jmVZa128Lprp7SrvKZriUFbuTOY3NzSWQyFuymIjbwYn2pwKe2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس‌های اختصاصی که توسط سی‌بی‌اس نیوز به دست آمده، خسارات گسترده‌ای را در چندین موضع نظامی ایالات متحده در خاورمیانه پس از حملات موشکی و پهپادی ایران نشان می‌دهد.
این تصاویر که توسط اعضای فعال ارتش که ناشناس هستند، ارائه شده است، ساختمان‌ها، وسایل نقلیه و تجهیزات تخریب‌شده را در پایگاه‌هایی در عربستان سعودی و کویت نشان می‌دهد.
در پایگاه هوایی شاهزاده سلطان در عربستان سعودی، یک هواپیمای بوئینگ E-3 Sentry مورد اصابت قرار گرفت و قسمت دم آن جدا شد.
در کمپ بورینگ و کمپ عریفجان در کویت، عکس‌ها نشان دهنده پادگان‌ها، تریلرها و وسایل نقلیه آسیب‌دیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71719" target="_blank">📅 14:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71718">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEh69QbmQAAmj8xjUZ2MJMfJ3sO3POPO5BE0lVrOfzWc1p-ZwnoiMXV_-Ib4KL-YwGkSVxZCajgcBpfJjSyImLLxflynnwbtp6THm2XHcH8oNZ8-iliSXgA7leb9CxOm71_6JsB4E0ZRT7JrZze_SJrPWxGYhlBzP4g6JSWby9SxpQX_lM3HsAykJcCnrFJSxSDs2J9au7MdY1YuRSOTBJw-myMs1W05bQ4uidWsEY-vSDaHRq2XjsMh39W7dKUKcjF28UwNmYCrDQUw4EdauzKb9qpU5oqzzUnm_tvJnkeam6L7yBSBOb2ZydzS1EP150Sf7nD_ztMce8PJHjtobw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که دوران قطعی اینترنت خیلی فراگیر شد اطلاعات کاربرانش در دارک وب، به فروش گذاشته است
این اپلیکیشن اطلاعات حساس مثل کارت بانکی و ولت و پسورد و… رو از گوشی کاربران جمع آوری می‌کرده، که در فایل فروش هم این اطلاعات موجود است
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71718" target="_blank">📅 13:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71714">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a175287c.mp4?token=SUGZVbGQ6JPPfd7F0CrQDeTuI5G9AYzN5mpbS-nHBud4jmgkOeiX_7eJEMQN64zwYMbP2UiZv2XsCcDlWMCx1B2bvrJ6NohNq9aALEGwbv49sXVjJnLb1RVfmuBMclZMJXGB-1mL6_0YVMtJYYZHj7Ufstq8_uiaCd_0mK-UqzZfG3jToPG726Ujwf4Pzh-oUvNUdSfJ9jNN6RtUxPAt3V1dMfMOQOzQfMo5pzMzEd_oha3Rz4PUnSEF4TwtvLMLHtUhT86z8DzMHPMeCaxcfEVekbKtTeF-r-4yajiKPANE_Cdm7BpjbYD6CG4AMDGZgw8Llf54tSOaCkE2NV1sAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a175287c.mp4?token=SUGZVbGQ6JPPfd7F0CrQDeTuI5G9AYzN5mpbS-nHBud4jmgkOeiX_7eJEMQN64zwYMbP2UiZv2XsCcDlWMCx1B2bvrJ6NohNq9aALEGwbv49sXVjJnLb1RVfmuBMclZMJXGB-1mL6_0YVMtJYYZHj7Ufstq8_uiaCd_0mK-UqzZfG3jToPG726Ujwf4Pzh-oUvNUdSfJ9jNN6RtUxPAt3V1dMfMOQOzQfMo5pzMzEd_oha3Rz4PUnSEF4TwtvLMLHtUhT86z8DzMHPMeCaxcfEVekbKtTeF-r-4yajiKPANE_Cdm7BpjbYD6CG4AMDGZgw8Llf54tSOaCkE2NV1sAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
:ویدیو هایی از اعتصاب عمومی در سنندج،سقز،دیواندره و دیگر شهرهای استان کردستان به مناسبت چهارمین سالگرد قتل مهسا(ژینا)امینی به دست حکومت آغاز شده است.
همچنین ویدیو هایی از شهرستان پیرانشهر در استان آذربایجان غربی رسیده که نشان می‌دهد بازاریان دست به اعتصاب زده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71714" target="_blank">📅 12:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71713">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یه پسر ۱۴ ساله با یه دختر ۱۳ ساله وارد رابطه شده و ا‌ومده پیش دکتر میگه من پرده اینو زدم و گشاد شده؛
حالا اومد پیش دکتر ازمایش بده ببینه این دختره قبلا رابطه جنسی داشته یا نه.
سن رابطه جنسی تو ایران داره به ۱۲ سال میرسه!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71713" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71712">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71712" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71711">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZF7dBHFCxJAjsa1Fuyb_AwSNAGvtgka92vvYt2iJ7D72kpgMv-xsjq6q_OCMd6G1TH5CXnwnede3-yKEIS0lHSqgm3iBk5ysmRxsFtelDZXDvHYsKPW2RhxtXdvzzOFUeL2mybwy4ry1rEQcPKi32gFmRWSIhjx7_weu5XV703Tu9ZxpN2e-6Vvs9rT9luhCYZB33HM6IE1Q6fPPbXU0N3govsR7Spwh3vhDYWfTG9ayWmhpC_R0n3hx-LPcUbNU2W05jZ9E0pY_4tVEqwtEcD4EH3Pf-cYejWfpY6oNNSh8snFbVbjDXgGfsIQIvoTs_BRYoHe-Uyr0jxMvkS-h6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
جدال جذاب لیگ اروپا!
نبرد هیجان انگیز
⚽️
بنفیکا
🆚
میلان
⚽️
را در
TrexBet
پیش‌‌بینی کنید!
📉
نگاهی به ۵ تقابل اخیر دو تیم:
⚽️
بنفیکا: ۵ برد و ۱۵ گل زده
⚽️
میلان: ۳ برد، ۲ تساوی و ۱۱ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71711" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71710">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEc_qQDBfY1wYSpfA0lHZSpOtsSyD-uX5IBstxtjbLipgXHArxbdrfXaO_Qb4DpV9Y6208ljnP8qkT2V5_q-0Z7o2atmnnJ21ltkkuR4gNjheYgGI_r9xJrfXqLyWaQXC5EBT3NZ1CN_Sar5adwPZi3RRU4YW4FQVLQdk4NzatZgpI73GWyxAbe-Gh1RZPbfo2gSynMSmWED9zB-TAB2LJPmPJ-2P3hm6-284ds0GjqcAQHEAKQRiy4cOSnHaxeFhP9_wdvhe0yAsjiL4B3KQ6qVzgWTEIPkbFVlz7nLqj_q4CZPhZ6dpyk0c9rpjdBT7n3HarCsFTOkgGTgq7ZkOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده برای اولین بار تأیید کرد که سلاح‌هایی در مدار دارد.
مینک، وزیر نیروی هوایی:
ایالات متحده اکنون سلاح‌های کنترل فضایی در مدار دارد که قادر به دفاع از نیروی مشترک در برابر اقدامات خصمانه دشمن هستند.
از بیان نوع، تعداد یا زمان پرتاب آنها خودداری کرد.
نیروی فضایی می‌گوید که می‌توان از آنها برای "اختلال، تخریب و حتی تخریب" به صورت تهاجمی یا دفاعی استفاده کرد.
کارشناسان فکر می‌کنند که به احتمال زیاد، پارازیت‌اندازهای فضایی یا جنگ الکترونیکی - سلاح‌های جنبشی - مشکلات مربوط به زباله‌های فضایی را ایجاد می‌کنند.
این به دهه‌ها ابهام رسمی پایان می‌دهد.
اولین نقاشی نیروی فضایی به معنای واقعی کلمه یک هواپیمای فضایی را در حال نابودی یک ماهواره متخاصم نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71710" target="_blank">📅 11:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71709">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26353c8137.mp4?token=FyJQaCIsn4Dg7zcG7s_S0d5FuR6-dVA72hRu6zZsLCnbk-tqvK9dsXhkCTYoEiVUtEHvgHjsQy6cE5BpiYoJZwTLv4J04y2R9rL8GkxNeDJah-zxPokHBPMPdqKVYlYjGCdDFzc1Fos2GpFwoB20bk_p14sA3Py6yYzLS4QtQJKAe99Fh1Y-3PoBjo7fb-RB624PxUZhFvZMOShn_BFUUvfB5kloNwSHrBXn1T1L76swI5eEOr7yovfYXuoKMsJAjXkExpkDArb8MyYuKH4v0MiOMX2OAyOPSPlI8B-tCK_Z0Pvg_mGhJ6-z4kzPwsfAlvFPZgrSKD-gKMTEG1lozw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26353c8137.mp4?token=FyJQaCIsn4Dg7zcG7s_S0d5FuR6-dVA72hRu6zZsLCnbk-tqvK9dsXhkCTYoEiVUtEHvgHjsQy6cE5BpiYoJZwTLv4J04y2R9rL8GkxNeDJah-zxPokHBPMPdqKVYlYjGCdDFzc1Fos2GpFwoB20bk_p14sA3Py6yYzLS4QtQJKAe99Fh1Y-3PoBjo7fb-RB624PxUZhFvZMOShn_BFUUvfB5kloNwSHrBXn1T1L76swI5eEOr7yovfYXuoKMsJAjXkExpkDArb8MyYuKH4v0MiOMX2OAyOPSPlI8B-tCK_Z0Pvg_mGhJ6-z4kzPwsfAlvFPZgrSKD-gKMTEG1lozw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک دانش‌آموز دختر برزیلی بعد از اینکه نمره‌ی خوبی تو امتحانش نگرفت با چاقو به معلمش حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71709" target="_blank">📅 10:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71708">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f46fce321.mp4?token=W6VZRQ2huGJY5ovGjcj7dWkiH4X0gdmJNQjHzv58BiOsCZjMmBjI5IhAl8dpRWGP3DKtUmo2RPbCd9-MX8y0SY4FseFw6bEGful_zom5MiSwtuQtlV7dKwlm6tnt5LgP0msMhqEs_fgG_wjwBR5ysFB5iCPOGw7UaVmfe6BVuZFTj3nPp_waU3Je1gv_s6OguEyVafhkcqmuabALB1CeZmKZvtXD4_S_nbHOlvxCQhhWykEEAZjJRVH7YCF6noecnINfz3VF8eKx9Q1HKcJdVVQvtqTX8qbd30tSkzHLuzPgKD8ntvv_Z1OKWZeHDFvxhl09rV-mYtqhdVOtiJIuSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f46fce321.mp4?token=W6VZRQ2huGJY5ovGjcj7dWkiH4X0gdmJNQjHzv58BiOsCZjMmBjI5IhAl8dpRWGP3DKtUmo2RPbCd9-MX8y0SY4FseFw6bEGful_zom5MiSwtuQtlV7dKwlm6tnt5LgP0msMhqEs_fgG_wjwBR5ysFB5iCPOGw7UaVmfe6BVuZFTj3nPp_waU3Je1gv_s6OguEyVafhkcqmuabALB1CeZmKZvtXD4_S_nbHOlvxCQhhWykEEAZjJRVH7YCF6noecnINfz3VF8eKx9Q1HKcJdVVQvtqTX8qbd30tSkzHLuzPgKD8ntvv_Z1OKWZeHDFvxhl09rV-mYtqhdVOtiJIuSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گفته خانم دکتر(روانشناس بالینی)؛
خودارضایی نه تنها ضرری نداره بلکه خودارضایی یه چیز سالم و بی‌ضرره که به عملکرد ذهن و مغز کمک میکنه، باعث کاهش استرس میشه و حتی به رابطه شما کمک میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71708" target="_blank">📅 10:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71704">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-Dt_l5x6Xm8CyBL6sB1fk6cKhuaQjXD6OXuxBZ0ZFtgAECWQU6NwFm5RyVU05BNR_y_4lv1qAgOFj4vvaMZHt5hh-c90EQLxQ9q_wcwq7yn4if94S-dF6w0cvGUv90OiZJO3gdCZS5ZNfBofGeD5bzv25bnO3f8JQkrn7ZvjFjQrM3tTgd9jj9nUpOwsmdzjWp4_wxDtVkR4lAx71zx9AGWhxWmUcCiP1ERLoBBOoYN5TNTC9-aQZyBf_yaK_9FKy4cLwB33xlm3HNBrKrcLynnqKFe3b8YTEuBp7CvaQnzFr2zCI5cKDjkSbzAGC8eN6mqa6_Fy9lF9L3MUpAZJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97e620d35.mp4?token=vUa5J3I_tZe3R2sBn4ReJXiRqSXlI2opmrySEWPBOpT6MOrmoEzSOn21EK6hWbTeyTczlIgD78__Bmyes8v800aMATQPV43VXAwF8eoFtD23cUXwlxGQ9z3pG3GSSOd-hL67gVOKrUfuQxQgFZhSFedNaAXSGYti0Hrr5V7hn5O9NziXFSGxrxtHT8JOpWzac5cYgouiNz8-CL_HrM3y8NosLyZzhE1ERD_Atve2rRhO_MoPa1YsJSNafvNPIhXh64HeQH46HpE9Id9qygmM-ucS-4ouqtDbHONcCvPLZwIMlyECgti7rsj1gox2n1xQl4FtFjt6xvhnycZUaBxpEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97e620d35.mp4?token=vUa5J3I_tZe3R2sBn4ReJXiRqSXlI2opmrySEWPBOpT6MOrmoEzSOn21EK6hWbTeyTczlIgD78__Bmyes8v800aMATQPV43VXAwF8eoFtD23cUXwlxGQ9z3pG3GSSOd-hL67gVOKrUfuQxQgFZhSFedNaAXSGYti0Hrr5V7hn5O9NziXFSGxrxtHT8JOpWzac5cYgouiNz8-CL_HrM3y8NosLyZzhE1ERD_Atve2rRhO_MoPa1YsJSNafvNPIhXh64HeQH46HpE9Id9qygmM-ucS-4ouqtDbHONcCvPLZwIMlyECgti7rsj1gox2n1xQl4FtFjt6xvhnycZUaBxpEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر تیک تاکر به اسم فاطمه تاجیک دیشب توسط چندتا دختر که میگفتن عکساشونو گذاشته چنلش خفت شده و خودشو دوست پسرشو کتک زدن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71704" target="_blank">📅 09:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71703">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8MW1WgvJakMA3NFzJfGzDmsq0NL6R2imBG1Yu1x9XEaWYpRmBRM6LFtZSBCyEgbnVWTXIjQvPYgxwRzm95qULsa-WOz_OTbeT9uwbDPrB3XS6x9peLfMFVRIV4XQqQG-aV7ezeVSQ05bwMhCiQC0jxqgmeX2yX9KJzb12nvkFifhNQcwEkFGaJ0C6dd6Bt7WUv8WPEKE67Tkfqygi8fix1bvy4Tc03Av5xPtkAPFZ8HPgykKHev-844RX3gvHeBrbpsq-_Ke6eDwbcg9spZ7rGn5I7K9zrmytYxZV6hEro6KRXTEuXjXLh5KxtO3wAnGReVfEAhIZV1ByfUOwlq2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس:
فرماندهان ارشد نظامی ایالات متحده، اسرائیل و هشت کشور عربی هفته گذشته در آلمان دیداری محرمانه برای گفتگو درباره جنگ با ایران و امنیت منطقه برگزار کردند.
این نشست که به میزبانی «سنتکام» (فرماندهی مرکزی ایالات متحده) برگزار شد، با حضور فرماندهان نظامی اسرائیل، عربستان سعودی، امارات متحده عربی، بحرین، کویت، قطر، اردن و مصر همراه بود.
دریاسالار برد کوپر ضمن تأکید بر تداوم حضور نیروهای آمریکایی در منطقه با وجود حملات ایران، شرکت‌کنندگان را در جریان برنامه‌هایی برای گسترش تردد کشتی‌ها در تنگه هرمز قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71703" target="_blank">📅 09:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71702">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71702" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71702" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71701">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ht013ER3f2KVA58T0W089JROWPh8tIEhbfyJ-kRNtGruEWMGVAwQPX6SR999SztWSn9AhpZfCdBLkacGcIv6ofwZ6tJf2WAFPyIaakxTecvpJ-c0rBo-ZJrz9HNMYtzCryrN40GBzVwT--JXU77asSjtEBprrcHjbMijszIdR74q3HyPHPriNF6FANePT25u2K6h3_ZkWjaRmsaHGV2zuNYzTN0qAz3O7nvobI_6N808CzQ3cOUCM_6a2Y6sLee8DPo1m5StpM5CkvEXPUEbF23goPBxpwD7rZAs5zRrH-q-qgjcP6rjLCPUGR-QUb_KrIwHBwne09KvC52VbfHzgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71701" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71700">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
⭕️
گزارش‌ها از شنیده شدن صدای انفجار در قشم  @News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71700" target="_blank">📅 01:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71699">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
⭕️
گزارش‌ها از شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71699" target="_blank">📅 01:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71698">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhcK-09PxDxFc61gg-EPSpyjQQ_zcgxvNaFHl5Kfn_x2X6Srx0xT61YdZG5-nqf1VLKYT0ttWCd12uy6S6LISdN9Ma-cidfm66ht9K916WXkLJxLGUJqYE8uAsoNFEJpP_Wt2YpkjoYy-biEEpjl3GmfVo_wnANNC_cABfnEndJOXIUjEAFHBTA5z7LRDy5FGMu5QNKpeDCXbSCfVgGaW8Rw1xvY_PS3C-q2zL1asHSDjinwMZvUdFPDAtRnHvpg_ZFPz_ydui4NfCKJ-HoX0yKCA71o60Ph3SetBnQHXcMVkGnab-iLS8YVbqYqigcuUVxD_2GfKJnDNpJ_sRNrXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری آلمان (DPA) مدعی است که حوثی‌های یمن اکنون در تنگه باب‌المندب مین‌های دریایی کار گذاشته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71698" target="_blank">📅 01:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71697">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/307693b5b3.mp4?token=N7nkDtB6mqAYIu5eMGPg4ACowDr2Wsuf9qzZg3BtVkLlTWmiSLk4cNAAK4nkRXP7I-DFuo8eTdstzOv4olwyNo7ZEaYoTP0S0QNs8jlnN25VAsCr92GSYTAt-fF6FwY3JYstekO0h6dm8tZBLrdbOFfY_CwKAfPcRZl-CDo3c3JRX8Nbx7fJPY45y2CiT916l2EgQA9M7ziJSphvnw4FfZMvMkCMY_qtRx5hbvix2YL8B0quXnkqZzuYkuTFcwmsWPmKaud1qZ26CynZyW1oSfUH3uNEA__qez1O_MibQb3hw9wN8LStLHrlwO3P3Km2XajGahRHrF3tv3gK73XxGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/307693b5b3.mp4?token=N7nkDtB6mqAYIu5eMGPg4ACowDr2Wsuf9qzZg3BtVkLlTWmiSLk4cNAAK4nkRXP7I-DFuo8eTdstzOv4olwyNo7ZEaYoTP0S0QNs8jlnN25VAsCr92GSYTAt-fF6FwY3JYstekO0h6dm8tZBLrdbOFfY_CwKAfPcRZl-CDo3c3JRX8Nbx7fJPY45y2CiT916l2EgQA9M7ziJSphvnw4FfZMvMkCMY_qtRx5hbvix2YL8B0quXnkqZzuYkuTFcwmsWPmKaud1qZ26CynZyW1oSfUH3uNEA__qez1O_MibQb3hw9wN8LStLHrlwO3P3Km2XajGahRHrF3tv3gK73XxGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان آمریکا به‌تازگی طرح استیضاح دونالد ترامپ را که توسط «اَل گرین» (نماینده دموکرات از تگزاس) ارائه شده بود، با رأی قاطع و سنگین ۲۳۲ به ۱۴۷ رد کرد.
بخش بزرگی از دموکرات‌های مجلس به این طرحِ پوچ و بی‌معنی رأی منفی دادند، چرا که اَل گرین خودسرانه عمل کرده بود و آن‌ها می‌دانستند که این قطعنامه به جایی نخواهد رسید
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71697" target="_blank">📅 01:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71696">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ونس امشب گفت که تو ماه‌های آینده، جنگ وارد مراحل جدیدی می‌شه؛
اما در شرایط فعلی همه‌ی تحلیلگرهای نظامی معتقدند که بخاطر انتخابات میان‌دوره‌ای، جنگی گسترده از آمریکا نمی‌بینم.
اما یه نکته‌ای اینجا وجود داره، انتخابات سنا و مجلس نمایندگان آمریکا  نوامبر ۲۰۲۶ (۱۲ آبان) برگزار می‌شه ولی نمایندگان انتخابی، با ۶۱ روز فاصله به سر کار میان، یعنی از ۱۲ آبان ۱۴۰۵ تا ۱۳ دی ۱۴۰۵، سنا و مجلس نمایندگان با همون اعضای قبلی ادامه می‌دن و می‌تونن قانون تصویب کنند؛ بنابراین از لحاظ تئوری، بهترین زمان برای حملات دوباره‌ی آمریکا همین دو ماهه (در صورتی که دموکرات ها پیروز بشن)
ولی یادمون نره که ترامپ یکی از غیرقابل پیش‌بینی ترین سیاستمدار های دنیاست
#hjAly‌</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71696" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71695">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdTvEhCDLi-0ifOcEL__U6IMzikHCgIKk5WZo_S0mk0kIQ9o5eEphYG183R8HtxbBbTeQd6MrxsHFwMGnKbSnF1aJE34jwM-6TPIlr0pot9xvJNfz3QKgAdxuvz_QQksC9m-H3H18QzTaHjm4zA8TKd_F5gmP643qem1ZmgHujpCWBgxk5nLgTeKcqCmcg8dRYzZKR9MenVf79coXUk5YCT9v4NdnXwojpiNHOSKRVQkn7_iD9C5wfDPYp7JlWPX1zm91O-4nszp0zvIPJFFj0DUughYkJrAyUzpJPx8I_ihNxRRo_YRRSSQRS6LEZv8Z42rVwBgLKxHk5z7mb0XQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایلیا هاشمی:  امروز صبح به برخی اماکن حساس دولتی در تهران دستور تخلیه دادند و چند ساعت بعد جنگنده در آسمان غرب و جنوب غرب ایران مشاهده شد، اما ناگهان همه چیز به حالت طبیعی بازگشت. مشخص نیست چه شد، شاید یک حمله نظامی به اهدافی در پایتخت که لو رفت و در آخرین…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71695" target="_blank">📅 00:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71694">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ایلیا هاشمی:
امروز صبح به برخی اماکن حساس دولتی در تهران دستور تخلیه دادند و چند ساعت بعد جنگنده در آسمان غرب و جنوب غرب ایران مشاهده شد، اما ناگهان همه چیز به حالت طبیعی بازگشت.
مشخص نیست چه شد، شاید یک حمله نظامی به اهدافی در پایتخت که لو رفت و در آخرین لحظه لغو شد؟ یا مسئله‌ای دیگر…
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71694" target="_blank">📅 23:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71693">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad7ec7235a.mp4?token=roIxfHPDo6yNg109eaxyv8VpMa406J4fctQHgykcKDckv9lbyC4U6vO5oGmUsc4e082_QXfY-02T-KiE9RZpUoYbmiFka_DBDgRBOIT57bAzar354GR4PmgbKFImHSvzl5aQzIP3DU5CoRPc8AgQ0uz0GfMnuQDnm8sFq9to-m77CL5ePB4U-quUR5AUvaIURp6oh8AWWuhwHbaC0dS7EPRSS4FknixYvGblvnEBjewem2gomRU50EqcghvS3ppbvQXzvaJYX4TiiLph127_A6vnbU2WXKJ4O0dvvW5jt5oscYcM59eu2ZXbJu8atxg86QyyTbN9FlfxM0PC1utMUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad7ec7235a.mp4?token=roIxfHPDo6yNg109eaxyv8VpMa406J4fctQHgykcKDckv9lbyC4U6vO5oGmUsc4e082_QXfY-02T-KiE9RZpUoYbmiFka_DBDgRBOIT57bAzar354GR4PmgbKFImHSvzl5aQzIP3DU5CoRPc8AgQ0uz0GfMnuQDnm8sFq9to-m77CL5ePB4U-quUR5AUvaIURp6oh8AWWuhwHbaC0dS7EPRSS4FknixYvGblvnEBjewem2gomRU50EqcghvS3ppbvQXzvaJYX4TiiLph127_A6vnbU2WXKJ4O0dvvW5jt5oscYcM59eu2ZXbJu8atxg86QyyTbN9FlfxM0PC1utMUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سریع‌القلم:
آمریکایی‌ها بعد از انتخابات کنگره به سراغ عملیات نظامی علیه ایران می‌آیند چه دموکرات ها پیروز شوند چه جمهوری خواهان!
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71693" target="_blank">📅 23:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71692">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71692" target="_blank">📅 23:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71691">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71691" target="_blank">📅 23:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71690">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a06568e4fb.mp4?token=eVSywkqBHan2iqmZ4wf_0FK8oFghPGaYscywq4tkDbChTEn0ji-PGE6H7fTIP-8A1JNEmMplSkO95YAJHIYn29m8RwzRIt-b2sbxUQqSHZdS82d6Sqn1CN60oFJors2a2tfXkpBsq0V3PL24xcGgjviOPQb5SNZIA3anYzyYzLz8-biBXhtIEBLQ8C_XA-tpJHtnZYxVn8rW691tLNeOPeuYIOzM1I9NxjikvCvOujOHZbBu7BeS_h7_hc4l4T7uX9xFtYDWjcznaX-OraCHaT2RKwD5Cx72hWJRzJhwxrHlkce7DCskkm0k9yMbyUgXwECNid7AZ2RCG6d47aV5Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a06568e4fb.mp4?token=eVSywkqBHan2iqmZ4wf_0FK8oFghPGaYscywq4tkDbChTEn0ji-PGE6H7fTIP-8A1JNEmMplSkO95YAJHIYn29m8RwzRIt-b2sbxUQqSHZdS82d6Sqn1CN60oFJors2a2tfXkpBsq0V3PL24xcGgjviOPQb5SNZIA3anYzyYzLz8-biBXhtIEBLQ8C_XA-tpJHtnZYxVn8rW691tLNeOPeuYIOzM1I9NxjikvCvOujOHZbBu7BeS_h7_hc4l4T7uX9xFtYDWjcznaX-OraCHaT2RKwD5Cx72hWJRzJhwxrHlkce7DCskkm0k9yMbyUgXwECNid7AZ2RCG6d47aV5Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتای جنجالی یه
جنده
: دختری که ادعا می‌کنه باکره‌اس، دقیقا به چی افتخار می‌کنه؟
تو قطعا ایراد داری، مگه میشه یه نفر با کسی رابطه نداشته باشه؟ آقایون حتی توی سوراخ موش هم فرو میکنن، اونوقت تورو نکردن!؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71690" target="_blank">📅 23:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71689">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/626fac3cc3.mp4?token=GWuh9KB6DXevoHrJeEbgW6gnYUu4hDhHHKuuG446qst-Borj8J4YCvUV1LcUJkdkwZspxqp11cdO8AWuYNFTKsQ0eycQSLDMwAnkmYVFeZ9kwimEozfCq-lDBrcggvq1vPiah_TndWm8crAQ9w9SW6i0I3EVwAGr3kp0F5TSfQ12-5WB86idPaVNStEO8t_a2NkA2wVm7oKSJ8XBYViAEWQhmLnM0ng306oYHP2HTGxSY6hJJlrESpfu_IAhZuyuyIfLQ9Tj-0wcVBDNZr_ZPjNwuVMGP2VcZ9awmBcsDiOhWBVreYc3Th59JMRcm-Qt2jntjNtVZGPhUv48dJb1aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/626fac3cc3.mp4?token=GWuh9KB6DXevoHrJeEbgW6gnYUu4hDhHHKuuG446qst-Borj8J4YCvUV1LcUJkdkwZspxqp11cdO8AWuYNFTKsQ0eycQSLDMwAnkmYVFeZ9kwimEozfCq-lDBrcggvq1vPiah_TndWm8crAQ9w9SW6i0I3EVwAGr3kp0F5TSfQ12-5WB86idPaVNStEO8t_a2NkA2wVm7oKSJ8XBYViAEWQhmLnM0ng306oYHP2HTGxSY6hJJlrESpfu_IAhZuyuyIfLQ9Tj-0wcVBDNZr_ZPjNwuVMGP2VcZ9awmBcsDiOhWBVreYc3Th59JMRcm-Qt2jntjNtVZGPhUv48dJb1aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به تازگی توی ایران یه تور راه اندازی شده به اسم «هیلینگ آب دریا» ، این شکلیه که میرین کنار ساحل و تا جایی که میتونین باید گریه کنین.
برای شرکت در این تور هم میلیونی باید پول بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71689" target="_blank">📅 22:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71688">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ائتلاف نیروهای سیاسی کردستان با انتشار بیانیه‌ای مشترک، برای(فردا) روز چهارشنبه ۲۵ شهریور ۱۴۰۵ (۱۶ سپتامبر ۲۰۲۶) فراخوان اعتصاب عمومی صادر کرده است. این فراخوان هم‌زمان با چهارمین سالگرد ژینا (مهسا) امینی و آغاز اعتراضات «زن، زندگی، آزادی» اعلام شده است.
در این بیانیه از بازاریان، اصناف، کارگران و دیگر اقشار جامعه خواسته شده است با تعطیلی مغازه‌ها و بازارها و خودداری از حضور در محل کار، در این اعتصاب مشارکت کنند. صادرکنندگان فراخوان، وضعیت اقتصادی، فقر، گرانی، بیکاری و همچنین آنچه تشدید فشارهای امنیتی و صدور احکام سنگین می‌دانند را از دلایل این اقدام عنوان کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71688" target="_blank">📅 22:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71687">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/265561794f.mp4?token=om9MhAJRJIpL0gBT4iaOxLU_UfTAAW0dWrmc7fqtSSf0sEsnR9RJiJW2RejvEjqbtaKjp4JFDNRV3aR2l3K-sHolc2HbcR9nLf8N8Pfssbk99WjvyulkYlMY6PVquiLSp3_pxJkBHABfYloZdguE4HOASao7O7oDSssOl3C7lKFIk8aOigv67-T64FpdqJfucow5AXn3HRctWEcvQXOkq-v6-saDjOzZSUqSq2-Oa4hWhRUIyJEC0yy03ufUYZL7OaOdaNqDLNU7e4mj_gAsbzA-sZmN0fo_WfBXYsSU1ZKa7I14tru7rRxfkpqggOcBKUAR5ZS_oM3PNv-JZXAanQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/265561794f.mp4?token=om9MhAJRJIpL0gBT4iaOxLU_UfTAAW0dWrmc7fqtSSf0sEsnR9RJiJW2RejvEjqbtaKjp4JFDNRV3aR2l3K-sHolc2HbcR9nLf8N8Pfssbk99WjvyulkYlMY6PVquiLSp3_pxJkBHABfYloZdguE4HOASao7O7oDSssOl3C7lKFIk8aOigv67-T64FpdqJfucow5AXn3HRctWEcvQXOkq-v6-saDjOzZSUqSq2-Oa4hWhRUIyJEC0yy03ufUYZL7OaOdaNqDLNU7e4mj_gAsbzA-sZmN0fo_WfBXYsSU1ZKa7I14tru7rRxfkpqggOcBKUAR5ZS_oM3PNv-JZXAanQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهاجرانی سخنگوی دولت :
امیدواریم نیازی به تغییر سهمیه‌های اول و دوم بنزین نداشته باشیم؛ ولی اگه بخواهیم گرون یا کمش کنیم حتما شما مردم را در جریان خواهیم گذاشت و بدون اطلاع‌رسانی کاری نمیکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71687" target="_blank">📅 21:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71686">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">شنیده شدن صدای دو انفجار از سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71686" target="_blank">📅 21:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71685">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/61894edf33.mp4?token=Knc60rcyQFhdRHzEli7Ipao7CMB2KlikfTMOT_8EBvVfIswh_aCRdwlVaAU9uYYU7vqqHBXHOojhuwOd8xdZrs4NkBAUigtzNEbaHS_AQOowneqxEN7GOUCUaGmowgq5CR4W6Hud2V-7y-5AeGck5HJY0XH66SmMZnznUk28BEVcHzpiZ2Z0R-is60mPkirb_8maNrbHnwU6SM13Be7_gnBI7osLjph4_HneZshLh7jAEtsEtUs7vp_upmuOw6I4ky2ksM3_xn382PEB_x3kRyL4NikpS0fJyAqzCQxTrlVPgv0R8Evl_4cA6_nKN6OEBuaHxH6an9EdnUo_ZV_kLg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/61894edf33.mp4?token=Knc60rcyQFhdRHzEli7Ipao7CMB2KlikfTMOT_8EBvVfIswh_aCRdwlVaAU9uYYU7vqqHBXHOojhuwOd8xdZrs4NkBAUigtzNEbaHS_AQOowneqxEN7GOUCUaGmowgq5CR4W6Hud2V-7y-5AeGck5HJY0XH66SmMZnznUk28BEVcHzpiZ2Z0R-is60mPkirb_8maNrbHnwU6SM13Be7_gnBI7osLjph4_HneZshLh7jAEtsEtUs7vp_upmuOw6I4ky2ksM3_xn382PEB_x3kRyL4NikpS0fJyAqzCQxTrlVPgv0R8Evl_4cA6_nKN6OEBuaHxH6an9EdnUo_ZV_kLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش، هواپیمای تهاجمی A-10C Thunderbolt II نیروی هوایی ایالات متحده، مواضع داعش را در نزدیکی «جبل‌العمور» در شرق استان حمص (مرکز سوریه) هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71685" target="_blank">📅 21:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71684">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoCJ9_3oMFnJXhwhYH3OZSOeuu2ZkkMWC2MTSx3Tp8is6zsWO7jSiagbS2b8xF17H-BsV-GRK5pTRvFrY1Xbn24jsnUC80624I2tRSbT0___LajDNAJTEfpbvvoT3pVRF0d8ofoloY2vI-tjpBUAFjAfDTQ9cOWtSgCUDiJeLmVtOjCrmNQhdPbLAieDSdeGvsan4S3nNDNTDYP156_lz7gvr0D1RU8Vm6OoPZqoWj2jrdKkDwMLstsQ4ygopj7xyOofLAnsS27wqCBBl6pciWdIRjOzhAgDJB4Q-ArdmcRj1dMhV19Bk2DN6BBvZh074IHTRXBxtj9AF2m9hFqgXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن پست:
دولت ترامپ در حال تدارک فروش ۴۰ هزار بمب سنگین (از انواع MK-84 و BLU-117 با وزن ۲۰۰۰ پوند) به ارزش ۲.۸ میلیارد دلار به اسرائیل است؛ این بزرگترین معامله تسلیحاتی از این دست در سال‌های اخیر محسوب می‌شود که هزینه آن از محل پول مالیات‌دهندگان آمریکایی تأمین می‌گردد.
این‌ها همان بمب‌هایی هستند که بایدن پیش‌تر به دلیل نگرانی‌ از تلفات غیرنظامیان، ارسال آن‌ها را به‌طور موقت متوقف کرده بود.
این قرارداد برای تصویب به کنگره ارجاع می‌شود و می‌تواند آزمونی برای دموکرات‌ها باشد؛ چرا که در ماه ژوئیه، بیش از ۱۰۰ نماینده دموکرات مجلس نمایندگان به کاهش کمک‌ها به اسرائیل رأی داده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71684" target="_blank">📅 20:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71683">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6afc5269.mp4?token=heIM0XqtUAqFHlgryN9at5KnJOg4OxGBBUGlEgatbFt0eokZzexYVnje4lEbcQPd8kWQgqOoXcumYktv_WueYuN9G10XL7qIHNOzZmxgQfd7zQnrAJcubVqjze7cfc48QRg4VTPs58ngHu8hEicx0ehoJCGDa4VihoaYqjVXUU6hp_sDW317LRaM7GGTJ5duDJg3LGiEnGtBOtfb68L81pnqtLNNqgCFUbiMriLPTgTJYvAm6SyGbEWQS-zkJPh5gUwS1LjLuE2uDbNiU9lL2rWMSBzOVxXoAoKcLj15OrZ7TTqO5n9szAQF4WEB-6kAkrmwJ22chmBQirK2WrTsjzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6afc5269.mp4?token=heIM0XqtUAqFHlgryN9at5KnJOg4OxGBBUGlEgatbFt0eokZzexYVnje4lEbcQPd8kWQgqOoXcumYktv_WueYuN9G10XL7qIHNOzZmxgQfd7zQnrAJcubVqjze7cfc48QRg4VTPs58ngHu8hEicx0ehoJCGDa4VihoaYqjVXUU6hp_sDW317LRaM7GGTJ5duDJg3LGiEnGtBOtfb68L81pnqtLNNqgCFUbiMriLPTgTJYvAm6SyGbEWQS-zkJPh5gUwS1LjLuE2uDbNiU9lL2rWMSBzOVxXoAoKcLj15OrZ7TTqO5n9szAQF4WEB-6kAkrmwJ22chmBQirK2WrTsjzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران تصاویری از نفتکش «ال‌گایا» (EL GAIA) پس از اصابت به آن در بخش جنوبی تنگه هرمز منتشر کرد.
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که ایران ماه گذشته با موشک و در پایان هفته جاری نیز با پهپاد به این نفتکش حمله کرده است؛
در مقابل، ایران مدعی است که این شناور پس از ورود به «منطقه ممنوعه» در بخش جنوبی تنگه، با یک مین دریایی برخورد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71683" target="_blank">📅 20:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71682">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cc9cce711.mp4?token=pvj2JYAm5JEkvoAro3_eBmgYfBalV_iCZ-VBRQ8HBCBZz4Xgq7_UhpnzFnXQ9uGdICVC9lWFJhCBqFHt_pTADUHUQ2jUqoZe5S8_orN34AQEvWWokZVHAumrSj9QGj2IbAXcL0LOWdsnl3YizjlI92c3ervHS3DDQ9c9IHqnQ6weve2uHkoxA_Qy66dQm8Yd0JunVvcSEB7QcTM9tuSYHnw57fNNSWDU08wWE_BhHp4zwX0Ip45P4C9h43XGg457GLzqf8wbEAq84ruTnMPQC7Wv6am1es6t74uHS0MM9WutS0ahFvz1EorDilpFQ4rmzocAQDtG8lw8hPLyGK0fbLAZ2Ig7jcvFVGDb6afJlBhV4yjbiBXaB43u_oH4jhghSeLt_YfOVLoOoSfBARwQYjlcIdJiBSbSwyUnNJVruHKoUuFIE9MFtbWRpRcajc2lQn50JFQXkFpJkk_Tihpg3kSktwIDM_swHaMbIlL3SJ9u9k_yj6xSrpj_njqbhd91nWxWS-P7tbMoBxQfzCDb5N4PoIovy6k0t1-_81dZjr2TMdXhxPCuHKzHs7FCuxKWwlByjRD8Hz99NcKX8vq4_hhGoy1AdrexdtEmtHsdb0NmkW9X_UWlQkJ6hkwiWThP0HzEJ1aAP98X_TXjQLdjzDwMTWxtRX0irfcwAsKTowU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cc9cce711.mp4?token=pvj2JYAm5JEkvoAro3_eBmgYfBalV_iCZ-VBRQ8HBCBZz4Xgq7_UhpnzFnXQ9uGdICVC9lWFJhCBqFHt_pTADUHUQ2jUqoZe5S8_orN34AQEvWWokZVHAumrSj9QGj2IbAXcL0LOWdsnl3YizjlI92c3ervHS3DDQ9c9IHqnQ6weve2uHkoxA_Qy66dQm8Yd0JunVvcSEB7QcTM9tuSYHnw57fNNSWDU08wWE_BhHp4zwX0Ip45P4C9h43XGg457GLzqf8wbEAq84ruTnMPQC7Wv6am1es6t74uHS0MM9WutS0ahFvz1EorDilpFQ4rmzocAQDtG8lw8hPLyGK0fbLAZ2Ig7jcvFVGDb6afJlBhV4yjbiBXaB43u_oH4jhghSeLt_YfOVLoOoSfBARwQYjlcIdJiBSbSwyUnNJVruHKoUuFIE9MFtbWRpRcajc2lQn50JFQXkFpJkk_Tihpg3kSktwIDM_swHaMbIlL3SJ9u9k_yj6xSrpj_njqbhd91nWxWS-P7tbMoBxQfzCDb5N4PoIovy6k0t1-_81dZjr2TMdXhxPCuHKzHs7FCuxKWwlByjRD8Hz99NcKX8vq4_hhGoy1AdrexdtEmtHsdb0NmkW9X_UWlQkJ6hkwiWThP0HzEJ1aAP98X_TXjQLdjzDwMTWxtRX0irfcwAsKTowU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
تنها کافی است به سخنان رئیس‌جمهور، رئیس مجلس و رئیس بانک مرکزی ایران اشاره کنم که اذعان داشته‌اند اقتصاد کشور در وضعیتی بسیار وخیم و بحرانی قرار دارد؛ هشداری که خطاب به هم‌قطاران تندروی آن‌ها در سپاه پاسداران و همچنین مردم ایران بیان شده است.
ما شاهد سقوط ارزش پول ملی و تورم سرسام‌آور بوده‌ایم؛
و در کمال ناباوری، کشوری که سومین ذخایر بزرگ انرژی جهان را در اختیار دارد، اکنون با قطعی برق سه تا چهار ساعته مواجه است.
این وضعیت اسفبار اقتصادی ناشی از تحریم‌هاست؛ ترکیبی از تحریم‌ها و اقداماتی که ما طی ماه‌های گذشته برای شناسایی و مسدودسازی مسیرهای مالی و سیستم‌های پرداخت آن‌ها انجام داده‌ایم و در حال اعمال فشار شدید بر آن‌ها هستیم.
به باور من، واکنش‌های تند و خشونت‌آمیزی که اکنون از سوی آن‌ها شاهد هستیم، درست مانند رفتار حیوانی زخمی است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71682" target="_blank">📅 19:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71681">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d47763dcd.mp4?token=TfnrQTMQAS1lYaJcL5RYDmwKq95ji3IFdeEf37HzO1kkpWQa07xidozCbMKOiZa_Ep-LhzWFt8FeMzyXKkTf8Go-3fsL1m3L37xyULWq3Gb0Sxw6L3y16SzMf4IMcNPHT3c4NzvgNMnOZMANndsmC1-CpzfDzHozYOw0jgCmQTx8ZD7kYzBSSOp6EkM2QC7m0TEXOLQxfs8O5AhBjDbuxy_8y3k2FHVEJ35TjXRl0ph93ZbuJClVcS7YZU5nfDZnCYuWzLJvZppBRAdFpJ2e5ySkpeS-AxClnxK9cHH0J3BRBjyLl6ZPYSxgOT_JARFYZouQL4wbuCw_TtMdID91kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d47763dcd.mp4?token=TfnrQTMQAS1lYaJcL5RYDmwKq95ji3IFdeEf37HzO1kkpWQa07xidozCbMKOiZa_Ep-LhzWFt8FeMzyXKkTf8Go-3fsL1m3L37xyULWq3Gb0Sxw6L3y16SzMf4IMcNPHT3c4NzvgNMnOZMANndsmC1-CpzfDzHozYOw0jgCmQTx8ZD7kYzBSSOp6EkM2QC7m0TEXOLQxfs8O5AhBjDbuxy_8y3k2FHVEJ35TjXRl0ph93ZbuJClVcS7YZU5nfDZnCYuWzLJvZppBRAdFpJ2e5ySkpeS-AxClnxK9cHH0J3BRBjyLl6ZPYSxgOT_JARFYZouQL4wbuCw_TtMdID91kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر، آتش‌سوزی‌های گسترده در تأسیسات ذخیره‌سازی «آرامکو» در «ابها» واقع در جنوب غربی عربستان سعودی را پس از حملات پهپادی و موشکی حوثی‌ها نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71681" target="_blank">📅 18:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71680">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
لحظاتی قبل یک پهپاد دیگر از نوع MQ-1 متعلق به آمریکا بر فراز تنگه هرمز با استفاده از یک سیستم پدافند هوایی متعلق به نیروی قدس سپاه پاسداران انقلاب اسلامی سرنگون شد.
این سومین پهبادی است که سپاه مدعی سرنگونی آن در روز جاری شده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71680" target="_blank">📅 18:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71679">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8132b94509.mp4?token=gMg2sVg5XBBvwvzPO-0cmGsuKOGRxtR_6iPiGDTnODjES7hZVzn7ExmbKHpLLuEVF43ix-4n9n4KN5LMpXZ6wU60mUHurUqD6JbgT-aoVb4RrQaE2_zv6DbJ7K-NmWozwskru-ql5Nfwdkk1GSGD5a_5UdMGVdpubEVgdzs-DkyyI2JwFKCgdFR9SeyQpyO337ZsAhRpYikPxhDEiXbDSxOGQkBFBMINYbOtFLZX7xdL0DMqlP_zZSI5FBaEdVxE9zohp-5wwF9iXxdUou-APrAmg0k82_m0g2iMXsv2lf46YYe9ZB0tTotTiYnb2yWmOvQaoAW9JyDRPlqv1DhtGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8132b94509.mp4?token=gMg2sVg5XBBvwvzPO-0cmGsuKOGRxtR_6iPiGDTnODjES7hZVzn7ExmbKHpLLuEVF43ix-4n9n4KN5LMpXZ6wU60mUHurUqD6JbgT-aoVb4RrQaE2_zv6DbJ7K-NmWozwskru-ql5Nfwdkk1GSGD5a_5UdMGVdpubEVgdzs-DkyyI2JwFKCgdFR9SeyQpyO337ZsAhRpYikPxhDEiXbDSxOGQkBFBMINYbOtFLZX7xdL0DMqlP_zZSI5FBaEdVxE9zohp-5wwF9iXxdUou-APrAmg0k82_m0g2iMXsv2lf46YYe9ZB0tTotTiYnb2yWmOvQaoAW9JyDRPlqv1DhtGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از پروازهای داخلی(کرمانشاه به مشهد)دچار سانحه شده و بخشی از کابین دچار شکستگی و اسیب میشه، خوشبختانه مسافران این پرواز سالم به مقصد رسیدند. جزییات دقیق این پرواز و نقص فنی هنوز مشخص نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71679" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71678">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71678" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71678" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71677">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wi2DdOV2MQYiVbIVAoqo7kyz_UsMnZ16PqmFJ2VaYzsuhSg2G6h9xlWDEdjXRutXaYlkbt5gu_JPwCPRY5GCDm5T6RUuxT69-MCf9IfgffPCRDiVp7V9TPkzEJ3vOQ-_Guiboe7AfMcqJzGcnLjeogrMblNV1Kdu9DNWNlJI6olG44gTyQ7bv35cyiY7yrXU9t5sd88RmrWGGHVRpFogWSVBiARAFljsLCwxTVMKfAD9WJ13S6m5ymsLdro5EcgCN_cNrL7FAKm3u2bpAVVNwRvUpbt3d2l8lAmrRg2bdKTlglScHV4UYqA9I4agzlE4Qy6uaN2gNz93PnKU3emyxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
تاتنهام
🆚
لیورپول
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
تاتنهام: ۱ برد، ۲ تساوی، ۲ شکست و ۵ گل زده
⚽️
لیورپول: ۲ برد، ۳ تساوی و ۸ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71677" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71676">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea966d07eb.mp4?token=XPQ5raW0rRm5qOhgCc_ZqP7h5PUjHrWQlbQzpZpEdlmvF7LwJtjWDXj19aUoq81WJULRe0DFumDrK_xIw4aXvErRtStSSdSQMJ26x195UEJuCCgRiDEIybFPOgaOoRf6LMNKlxRQtoIcLSEM68dBr-56IR2isWImf2RbaBmJZ408H5Oa64qdyWaBCHn_ovz7TOJaNWaSkkGIFwHGjNN_4DEQR8KbKLzi6hYhPCiTeeVo2hwbV82w7GVh_xdh6oro7Mr8AGvs1tthcUN9xmeOnr0y3ZSPpjYwjIHCechREXjGAMsy0zq_R4G7AarTD60Ca-SeYoDDFIIgNYnW34JR2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea966d07eb.mp4?token=XPQ5raW0rRm5qOhgCc_ZqP7h5PUjHrWQlbQzpZpEdlmvF7LwJtjWDXj19aUoq81WJULRe0DFumDrK_xIw4aXvErRtStSSdSQMJ26x195UEJuCCgRiDEIybFPOgaOoRf6LMNKlxRQtoIcLSEM68dBr-56IR2isWImf2RbaBmJZ408H5Oa64qdyWaBCHn_ovz7TOJaNWaSkkGIFwHGjNN_4DEQR8KbKLzi6hYhPCiTeeVo2hwbV82w7GVh_xdh6oro7Mr8AGvs1tthcUN9xmeOnr0y3ZSPpjYwjIHCechREXjGAMsy0zq_R4G7AarTD60Ca-SeYoDDFIIgNYnW34JR2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛
بسنت درباره ایران:
ترامپ در حال اقدام علیه رژیمی است که خود را وقف شعار «مرگ بر آمریکا» کرده و برای تحقق همین هدف به دنبال دستیابی به سلاح‌های هسته‌ای است؛
اقداماتی که رؤسای جمهور پیشین مدت‌ها از انجام آن طفره می‌رفتند.
تحت رهبری او،آمریکا دیگر تهدید ایران را مدیریت نمی‌کند؛ ما در حال پایان دادن به آن هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71676" target="_blank">📅 18:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71675">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3hlUjjR0AqvydK3vlRc5VfVf4roL98K8xhP5um9V-8DgrhECp-dQ0CnDG7DTTCUaQPo_7W9Yh0HBPgxkfsY3aJ0FKrsielQTXH0nFSIXbb76grfhVaxpWCrisIHoeoPfSvWDZdgBNVl3qCCSGu-gGOQ1TzwZUZzuBBFunse8KAhS_y3K1CXPFD6pNn7ZyLFgH57xvtai2t96mmLe7DjhwKuzuWM1mG5U7ENV8pfcxwXsDToLfp1FfxEv59AgPpBy4vl6WVG9RALnDKuXw6xK-BrC8-N6JWWD2jIY78q8aM1DynXIj60A9YdY0dzsy1IRQ_EaN3aRjt_4J91Cn0LNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس:حمله پهبادی ارتش آمریکا به دو قایق در حوالی بندرکرگان در آب های خلیج‌فارس. تعدادی از صیادان مفقود شدند و عملیات جست‌وجو و امدادرسانی آغاز شده.   @News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71675" target="_blank">📅 17:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71674">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4824aba9.mp4?token=P6zgHLoc9V2FLRPb14CCiBm0B4LJf5gWBypRH1pYjV8t9d85ciWDpe50Cfm9giMyULdlNPNYJnNp1Ori50NmkeSifRgolzknzbERluPt9eBCVv2p_Wl0OM6_B7Hxg62BtQGWNvL-WU0Oq1zGHANF9Ys6SdyetVSZpJ1-HmJId0yB5y91pipPfMVRED_kroJmhhwS_b5YrytmcLEJay36ocbnTJXRst_FSSFtqgsoScpRdfVPWA3W_KVm_ZdZNTKuD5sbSvlCWCEAzBuD_maX3kZM7kSlAf8I0aLjkBqvnjgUxHN4gx3bplePHursCkgHbjk2qdB4XzeZDOmxhzFizA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4824aba9.mp4?token=P6zgHLoc9V2FLRPb14CCiBm0B4LJf5gWBypRH1pYjV8t9d85ciWDpe50Cfm9giMyULdlNPNYJnNp1Ori50NmkeSifRgolzknzbERluPt9eBCVv2p_Wl0OM6_B7Hxg62BtQGWNvL-WU0Oq1zGHANF9Ys6SdyetVSZpJ1-HmJId0yB5y91pipPfMVRED_kroJmhhwS_b5YrytmcLEJay36ocbnTJXRst_FSSFtqgsoScpRdfVPWA3W_KVm_ZdZNTKuD5sbSvlCWCEAzBuD_maX3kZM7kSlAf8I0aLjkBqvnjgUxHN4gx3bplePHursCkgHbjk2qdB4XzeZDOmxhzFizA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو سی‌و‌سه پُل اصفهان، یه پسر نوجوون اومد مثلا یه حرکت نمایشی بزنه و از یه ارتفاع نسبتا بلند بپره پایین که فرود ناموفقی داشت و با سر رفت تو زمین...
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71674" target="_blank">📅 17:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71673">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b63b29bdd.mp4?token=o9P3dunrTRKcc3FvmrOlsrbPyYHWM6FDNagkHH8kD89no9YmYYTUjWQlOJpcRLUqHImlW_eeV1QK8IaIJHSnBg1jsLwc6dEyHtTpb-xPv7N2XE42UUVjDoKsc_dIaE4-bNAZoxekcZx9-gTlKGoaHjA6_0vmX74l_VUSd4d2vu324ehQd1R2soJ7P0Yk4W9MLYlSYUyWlkaoeZrwWwF7SX4zjmlrnoa9lpmYeibjhJWgTfBKIZzgZYccATIqLs45cuoeWUqV3oSWIAu-gBUw8d_prfptf8cVUPrnIGWvJBx_gvK7ikjST3qp4GgyVf7ybAA27tFVO4dOqt85TTlupw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b63b29bdd.mp4?token=o9P3dunrTRKcc3FvmrOlsrbPyYHWM6FDNagkHH8kD89no9YmYYTUjWQlOJpcRLUqHImlW_eeV1QK8IaIJHSnBg1jsLwc6dEyHtTpb-xPv7N2XE42UUVjDoKsc_dIaE4-bNAZoxekcZx9-gTlKGoaHjA6_0vmX74l_VUSd4d2vu324ehQd1R2soJ7P0Yk4W9MLYlSYUyWlkaoeZrwWwF7SX4zjmlrnoa9lpmYeibjhJWgTfBKIZzgZYccATIqLs45cuoeWUqV3oSWIAu-gBUw8d_prfptf8cVUPrnIGWvJBx_gvK7ikjST3qp4GgyVf7ybAA27tFVO4dOqt85TTlupw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن هاشمی: من خبر دارم مسئولین در هر دو جنگ از تونل‌های مترو به عنوان دفتر کار استفاده کردند
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71673" target="_blank">📅 16:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71672">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نفتالی بنت درباره ایران:
این رژیم فاسد و پوسیده است؛ همچون درختی که از درون دچار پوسیدگی شده و سرانجام فرو خواهد ریخت.
در مورد این درخت پوسیده، می‌توانیم اینجا و آنجا حفاری‌هایی انجام دهیم. منظورم صرفاً اقدامات نظامی (کینتیک) نیست.
صحبت من درباره اقدامات اقتصادی، کارهایی که نمی‌خواهم نامی از آن‌ها ببرم، و همچنین تقویت معترضان داخلی و تقویت دشمنانِ این رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71672" target="_blank">📅 15:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71671">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afac6b01df.mp4?token=Glg8L6yTI9KpPns-TLWlbWjGrwWye6KVxPMikx-RxttrrikxgZLrxGSETD-5C_V4u1F-shLK5tO78nXiW-CXtYKn7B3LG34HvHKYIAlT6LH0wxCebbk0anviC8zRKgpkZ7D_wCAAzhi5IYuZ5353yfjgNNiFYR00m10gWqy8Xwf3_o9qPmlud8xMDDe91gGLGQP7C2JFrQejZIC2r6tYXtQWDcmolqliUP8E3izBShuLuWqMZ1Hoiyb8fIBbbhGFtih6qFzoPgpnbxw_AbrEqqs_krXCyBqPriirkIe0f7qvD31AhQVf_8CBR93wcHZA2tnPc6AWh9iqEKRiNok8ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afac6b01df.mp4?token=Glg8L6yTI9KpPns-TLWlbWjGrwWye6KVxPMikx-RxttrrikxgZLrxGSETD-5C_V4u1F-shLK5tO78nXiW-CXtYKn7B3LG34HvHKYIAlT6LH0wxCebbk0anviC8zRKgpkZ7D_wCAAzhi5IYuZ5353yfjgNNiFYR00m10gWqy8Xwf3_o9qPmlud8xMDDe91gGLGQP7C2JFrQejZIC2r6tYXtQWDcmolqliUP8E3izBShuLuWqMZ1Hoiyb8fIBbbhGFtih6qFzoPgpnbxw_AbrEqqs_krXCyBqPriirkIe0f7qvD31AhQVf_8CBR93wcHZA2tnPc6AWh9iqEKRiNok8ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌ های این خانم به‌شدت وایرال شده و دخترا هم خیلی بهش انتقاد کردن:
اگه یه مرد، دارایی های خودش رو به نام خانومش بزنه، اون زندگی رو با دستای خودش نابود کرده.
آقایون اگه ۵ تا خونه هم به نامشون باشه، هیچوقت تو دعوا خانوم‌ خودشون رو بیرون نمیکنن
ولی اگه خانوما یه چیزی به نامشون باشه به این موضوع فکر میکنن که میتونن بدون اون آقا ادامه بدن.
من خودم خانواده‌هایی دیدم که به دخترشون میگفتن تو که ماشین و خونه به نامت زده دیگه احتیاجی بهش نداری، خودت برو زندگی کن.
خانوما اصلا جنبه‌‌ی اینکه چیزی به نامشون باشه رو ندارن، اون اگه بخواد زندگی کنه با یدونه سکه هم زندگیش رو میکنه، آقایون بفهمید من دارم چی میگم...
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71671" target="_blank">📅 15:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71670">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5632e037a5.mp4?token=IXjl-2EmHN3fRfBPcCE_ULX7TsHj9T3P_TROaDi2OBGQIGS6AeoZwNDEWT7SzX0h4xzMn0r9E3Ip-DELQi1iN5oufkv8hF2VVBsG-mEEpEwd5PW1RkR777Qid8k4a0dspoNPHdUpMIiIMHyS9BJDiU5OSwa-hjp28zJb9XTGes8b3YRH4yaQGHPvt7Hech-eahXqccwnN22HRkabByqK5uOB-RHM6JT_ZWJbj33FfQtKEGP92WUgb6jvoePpk3hFSb-jBsV50tM6f1_So_z2uI6akaZGqOitO-D5jeVd0PLoI1BuOVfdI1pMb90rTDbN-bV7zStunCewjkp0VsJ7LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5632e037a5.mp4?token=IXjl-2EmHN3fRfBPcCE_ULX7TsHj9T3P_TROaDi2OBGQIGS6AeoZwNDEWT7SzX0h4xzMn0r9E3Ip-DELQi1iN5oufkv8hF2VVBsG-mEEpEwd5PW1RkR777Qid8k4a0dspoNPHdUpMIiIMHyS9BJDiU5OSwa-hjp28zJb9XTGes8b3YRH4yaQGHPvt7Hech-eahXqccwnN22HRkabByqK5uOB-RHM6JT_ZWJbj33FfQtKEGP92WUgb6jvoePpk3hFSb-jBsV50tM6f1_So_z2uI6akaZGqOitO-D5jeVd0PLoI1BuOVfdI1pMb90rTDbN-bV7zStunCewjkp0VsJ7LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیراندازی نیروهای انتظامی به سمت بالگردآمریکایی در جریان عملیات نجات خلبان مفقودی آمریکا در روز روشن
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71670" target="_blank">📅 15:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71669">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada1fff69c.mp4?token=t2cJexAe4lGTG7kqzkGSbT-6fDqq6auY6ansybXbv03q0Arkti0a9OPi-g_YjurMFOjelw0zi5v2G3VCyIPZgGOtEH-rL-MRppglSkzCUOxP60QasHyHnPEpNUYVwARxqGTxxM7uE5tLDolwv3tMwgohEUHkfSfeWfeTr1Y0qBrESeLlr1JU-dOowyHOvwxObGKnEbvx6rApcp390Uq00g7jH96pNa56_3ddpHG8t_BTwxBJOm2GYnT7z-6wypzYjwbmAbVMM6t-DUt5YfZ0S60N3LOSdBV7u4rPSiXRY61tgKTd2aIs2C_MYDKJcg2MDUv6zzuLq0TdJwfPuSxCpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada1fff69c.mp4?token=t2cJexAe4lGTG7kqzkGSbT-6fDqq6auY6ansybXbv03q0Arkti0a9OPi-g_YjurMFOjelw0zi5v2G3VCyIPZgGOtEH-rL-MRppglSkzCUOxP60QasHyHnPEpNUYVwARxqGTxxM7uE5tLDolwv3tMwgohEUHkfSfeWfeTr1Y0qBrESeLlr1JU-dOowyHOvwxObGKnEbvx6rApcp390Uq00g7jH96pNa56_3ddpHG8t_BTwxBJOm2GYnT7z-6wypzYjwbmAbVMM6t-DUt5YfZ0S60N3LOSdBV7u4rPSiXRY61tgKTd2aIs2C_MYDKJcg2MDUv6zzuLq0TdJwfPuSxCpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادر زنِ مجتبی خامنه‌ای:
مجتبی خامنه‌ای با همسرش سریال " فرار از زندان " رو مفصل نشستن دیدن و درباره اتفاقاتی که داخل سریال افتاده بود هم صحبت میکردن.
یه بار تو یه جمعی گوشی یکی زنگ خورد، من گفتم این چه آهنگیه دیگه؟ که یهو مجتبی گفتش این آهنگِ یکی از فیلم‌های کریستوفر نولانه دیگه، چطوری نمیشناسیش؟
‌
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71669" target="_blank">📅 14:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71668">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sB5p8Srbl89CSCOTJMAysmWB8-2XJ1Jud2RBulESIPDo7CpDiAcLwir2P33LgHG96c5Do78PIJgkFj4MQJNt6mtsqF42n5mbemfxmw5eVkz50DHBN4xtsMTdBev429Hau7F-o4ok3IOctkCu8NqLOipdQy6MAUJ7DOgECYArpPIR7UMGMgqCVq7qLK2rp_lEgeMMC7qVv1i3drnnKWn8VLdNTtxGAIegDGwVNy9fYwsNGOHvwECulbxevDhfkNIU_rWaF8O2SzoNknkPzmVtHl8egFABh0j-EzB7nF_p_XHYDexqgz9BXSj3FAtvu0QIYZ7o4ssVc-5VcQXcngEacA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی قلهکی:
«نشست عمان» با حضور کشورهای خلیج فارس برای تثبیتِ مسیر تنگه هرمز، با نقش‌آفرینیِ جدیِ آمریکا و برخی از کشورهای حوزه خلیج فارس فعلا لغو شد
عربستان» به بهانه اصابت خط لوله‌اش و درخواستی که از پاکستانی‌ها داشته تا ایران را راضی کنند که به انصارلله بگوید از فتوحاتِ جدید عقب نشینی کند، «بحرین» بابتِ ناراحتی از جنگ رمضان و پرتابه‌‌های متعددی که بخاطر میزبانی از زیرساخت‌های نظامیِ آمریکا در خاکِ کشورش دریافت کرده و «امارات» هم بابتِ اُفت جایگاش در آینده‌‌ی منطقه در صورتی که مسیر جدید تنگه تثبیت شود، در نشستِ مهمِ عمان شرکت نکرده و کارشکنی کردند!
ولی بازیگرِ اصلیِ لغوِ این نشست، آمریکاست!
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71668" target="_blank">📅 13:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71667">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">حملات موشکی/پهبادی حوثی های یمن به مکه، طائف و جده عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71667" target="_blank">📅 12:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71666">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NA-36pHY59n-sagd0Dge7kBbIAAf7gKemqcMO744kRq1j9nAazdpaaeGOzPytn_hrw6cYd15uDEutccfvOwnQcSjuUBqB-M0NSkW7urJykK-4Ebiug4PF9XU798TY--Ajxkk5qaMEKdVArrjpo33S2GN2sc7BMCEZf6BinCIHLvssBhBDY1adrIG5Fk-ioEyeiQeY4CmNwKY0Pqpf_fN_jaKPVnaAwZq-3kAEVJTYh1QeV9eVhpVAAwBiSxR8F16bdHWINIHHvdoSAioA_zFxZN1tZLhNyXjUDKbyCbmm_UOm_RG0aIdgPOi4swcqG37Tsydhd-PXJeXVHlMY5e19Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) :
گزارشی با تأخیر زمانی درباره وقوع حادثه‌ای در تنگه هرمز دریافت کرده است.
یک منبع موثق گزارش داده است که شناوری مورد اصابت یک پرتابه ناشناس قرار گرفته است.
هیچ‌گونه خسارت یا پیامد زیست‌محیطی گزارش نشده و مقامات در حال بررسی موضوع هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71666" target="_blank">📅 12:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71665">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee29acd4a8.mp4?token=JDHo9i8lWlvlg5yQgY6DKL0sdGkxWpFMnPNiP9lTJLs2Y7PmPR_sOExuXowd-rTFINwkxC1qXm-nQ-Haf-alBCXmzqSLEUorLtT58_ntQSyDNXHByqPI-gn-MZzt90GFUmX804NVE9iRE0qkPrECkM5inw7BFVhHL6tSren5i-UscKwDD5-o5lYAmOXsFIbPmw-PpjGHPCQmie1QOTNHbVApV3gYnDrc93hWJjOmZNL4B8EEc4AiK6H3CRCtKLQm6gpkk-eAqV92-6-U-cYvUOG0LfLjLOSuEzrGyPjUN-JOPJwnDwGkOPSMJpx4UbC3mIRBQpVNHFiyIi4Yqa4TOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee29acd4a8.mp4?token=JDHo9i8lWlvlg5yQgY6DKL0sdGkxWpFMnPNiP9lTJLs2Y7PmPR_sOExuXowd-rTFINwkxC1qXm-nQ-Haf-alBCXmzqSLEUorLtT58_ntQSyDNXHByqPI-gn-MZzt90GFUmX804NVE9iRE0qkPrECkM5inw7BFVhHL6tSren5i-UscKwDD5-o5lYAmOXsFIbPmw-PpjGHPCQmie1QOTNHbVApV3gYnDrc93hWJjOmZNL4B8EEc4AiK6H3CRCtKLQm6gpkk-eAqV92-6-U-cYvUOG0LfLjLOSuEzrGyPjUN-JOPJwnDwGkOPSMJpx4UbC3mIRBQpVNHFiyIi4Yqa4TOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبه ناو سپاه با عنوان «رودکی» که در جنگ ۴۰ روزه منهدم شد در حال غرق شدن است. این کشتی تجاری بود اما به نظامی تغییر کاربری داد و گفته شد هلی‌کوپتربر است اما هدف حمله قرار گرفت و نابود شد.
در جریان جنگ ۴۰ روزه تقریبا تمام شبه ناوهای سـ.ـپاه و ارتش از بین رفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71665" target="_blank">📅 12:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71664">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71664" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71664" target="_blank">📅 12:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71663">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rw2I9WbhdYQqUUzPeLpLrsvdVLbZfOInXw57a9JuCrtAsGova9RCAEGx_Ik40g1XhaYevLOjFZ2_u4mFJSIsK1qL7090kvpKRaCCXYDEwyB7cLZI5MLrJyZOrO3qXTp_VCeH9B4ZASlzFI8dHaK0Wq0aAZA7sP7Nqo2Yb4nY9wa1IYHUeTwYcclt3yNhDMHKv8ef7jDWgwbHemYnVnJTAQ4G9glxlJ44wBwmlZUo3DYNTGry32N3Encf5xgSe0M_1Hzw9P-pMBn4s5Q6XWXod5logl28wjr3dfbNF0LNGl_YYVq8Uwn_QfgQo23tuieedvCRtN-ZWArsqi5IAzUiLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
رئال مادرید
🆚
الچه
⚽️
را در TrexBet پیش‌بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
رئال مادرید: ۴ برد، ۱ شکست و ۱۴ گل زده
⚽️
الچه: ۲ تساوی، ۳ شکست و ۶ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71663" target="_blank">📅 12:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71662">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JqAdf8NW_oYK-O1mjdCbT3GxFmbDuE9VCQD9OKQanqyqtyiVMMXvht-HZG1TU71A_4B3BfiHyAWXiKM6cXWmgP1DG51X2v0WCHzYF7c-RBuDtEO1uH1x0Gvlyy477COaAxFOY4eqpwTEeUNOO1Ww3Ju-RkHkMWV2UcH70M-Vj8E8VnJa9HxBAv95ViD_ssM59qN5bq9fVY-L3G7iz1nSuokRH__RPJJf_lesdwKpFaeZKpa2uHdaSPtfcnF8unKrxgHuEE0C0pstnRz5OEhd-DUWWGsE1nHR-hf-JwZTjdPNjZdp25_KuMiV_IGcErSw3LjCidoR4IJJ45lyjS6XVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند هواپیمای دولتی ایران با شناسه پروازی «IRAN06» از تهران پرواز کرده و بر فراز ریاض، عربستان سعودی مشاهده شده است
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71662" target="_blank">📅 11:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71661">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2f2bddd6.mp4?token=vUVneVPHmlG7wivWpVTAqj8DUfR-_7jxZjSCCLfQ8jBE1BPnk5dPg9P4aamLMrvfdkbkhicrxFbVqAz1Ptjq7KZh2fBDDf2xLafsqXCyuLKYWCHJuhIN5lS410GFLNNfGdIIG-BqqvHvlFfPROBTRg622f4FssyV49AE6SAityMFatvCtl8PWKsg7MzI__MeJ9nkJMpGyDLP554CF3pdUGC83TQPjw5Zn6wEU1siu8pN7VVFMajaISnDjCqR_XQDFU1XuegkMSVk8ygbnhsX1v3HXzy-CQSvflo_8mGVqZ2GYr0j5cuV_QdUVc0vYX1X22tfAkWSDmapSl7SEpOcNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2f2bddd6.mp4?token=vUVneVPHmlG7wivWpVTAqj8DUfR-_7jxZjSCCLfQ8jBE1BPnk5dPg9P4aamLMrvfdkbkhicrxFbVqAz1Ptjq7KZh2fBDDf2xLafsqXCyuLKYWCHJuhIN5lS410GFLNNfGdIIG-BqqvHvlFfPROBTRg622f4FssyV49AE6SAityMFatvCtl8PWKsg7MzI__MeJ9nkJMpGyDLP554CF3pdUGC83TQPjw5Zn6wEU1siu8pN7VVFMajaISnDjCqR_XQDFU1XuegkMSVk8ygbnhsX1v3HXzy-CQSvflo_8mGVqZ2GYr0j5cuV_QdUVc0vYX1X22tfAkWSDmapSl7SEpOcNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری: آیا قرار است همه ما تا ۱۰ سال دیگر بمیریم یا نه؟ موضوع بحث همین است.
ایلان ماسک: خب، متأسفم که باید این را بگویم، اما همه ما خواهیم مرد.
مجری: می‌شود یک بازه زمانی مشخص کنید؟
ایلان ماسک: بله، نرخ مرگ‌ومیر همچنان ثابت و ۱۰۰ درصد است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71661" target="_blank">📅 11:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71659">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🎙
صحبت های این خانم درباره سگش:
خرج ماهانه سگم حدود سیصد/چهارصد میلیون تومنه
😳
روتین روزانش صبح حدوداً ساعت ۱۰ بیدار می‌شه، یعنی صبح همه رو بیدار می‌کنه. بعد تا ساعت یازده که می‌شه، یه مربی شخصی داره که میاد می‌بردش یه جا مثل فضای باشگاه.
بعد هم که ساعت سه و چهار غذاشون رو می‌خوره. پوستش حساسه و یه سری شامپوهای خاص داره که ما همیشه می‌زنیم.
شب‌ها من یه دور پیاده‌روی می‌برمش و بعد هم شامشون رو خودم می‌دم.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71659" target="_blank">📅 11:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71658">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ea33bdfd.mp4?token=FeogsizQtfPnQxGKGDWJvgeXqY1fD1EMK-LWpIAe4zW8cOSmLlD833JacWi485vZV8VZ5reaTl0cpK71TwbYd9icrKENCqLShbBP6f13KK81FRYpp_CgR4BqS1B8aMQd3b621H5kzyQm14HZHOWQpsJCOWAaYCgZw597zhuGkgWKb_N2ZG2rEJnSD34req-dXum7E3vjZiznwkXv5_DINsK-RnMg4roT_ADDpeWONm1vnu47KToesU9KFOZiDmuqe47pcfMLYitvruCo2nGcp6vzUBwFPd5OXrR9OAWAYeI62Frp6aMviDRMCM3uPMhY6kEdDj6qsL--Pv5JEKkW6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ea33bdfd.mp4?token=FeogsizQtfPnQxGKGDWJvgeXqY1fD1EMK-LWpIAe4zW8cOSmLlD833JacWi485vZV8VZ5reaTl0cpK71TwbYd9icrKENCqLShbBP6f13KK81FRYpp_CgR4BqS1B8aMQd3b621H5kzyQm14HZHOWQpsJCOWAaYCgZw597zhuGkgWKb_N2ZG2rEJnSD34req-dXum7E3vjZiznwkXv5_DINsK-RnMg4roT_ADDpeWONm1vnu47KToesU9KFOZiDmuqe47pcfMLYitvruCo2nGcp6vzUBwFPd5OXrR9OAWAYeI62Frp6aMviDRMCM3uPMhY6kEdDj6qsL--Pv5JEKkW6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارهای عجیب علیه روحانی در تجمعات شبانه
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71658" target="_blank">📅 11:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71657">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دوباره آمار مبتلایان به کرونا تو کشور داره می‌ره بالا، خیلی مراقبت کنید
من خودمم دو روزه به شکل عجیبی گلو دردم
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71657" target="_blank">📅 10:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71656">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/840407be05.mp4?token=gg9DUC3DZA2BRqX6YknwlgtDMSfSwwYzyZtkV6B-Fi9R0LHJ5nuzj4ibMpefzTC_1-afgnTi0lInlsVfanOWF5InA1VlT93qBmsIuuZP5L6S6VZAOzAJahGfdbW7NDhYDoT_mcAiGg84_b64AS2OhB2I4YdFBPHWUZZytVFO3sPEjpeC2R40vxZYNGH4CFFzSOIagwxXja3a5BPqDreWQV6ibp5GZKpPu4n6cloSp71U2Gj3cCdDgZPAUCpJwWxRpEt9X58tW32LpnkVXVfItDrdcNjUKFgy4x7S5NhcfSupsGktCP09c88b9u4DikRmIPOesCJKToJFZzjmMIi7Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/840407be05.mp4?token=gg9DUC3DZA2BRqX6YknwlgtDMSfSwwYzyZtkV6B-Fi9R0LHJ5nuzj4ibMpefzTC_1-afgnTi0lInlsVfanOWF5InA1VlT93qBmsIuuZP5L6S6VZAOzAJahGfdbW7NDhYDoT_mcAiGg84_b64AS2OhB2I4YdFBPHWUZZytVFO3sPEjpeC2R40vxZYNGH4CFFzSOIagwxXja3a5BPqDreWQV6ibp5GZKpPu4n6cloSp71U2Gj3cCdDgZPAUCpJwWxRpEt9X58tW32LpnkVXVfItDrdcNjUKFgy4x7S5NhcfSupsGktCP09c88b9u4DikRmIPOesCJKToJFZzjmMIi7Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلار شده 240 تومن؛
همون لحظه صداوسیما:
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71656" target="_blank">📅 10:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71653">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a54c7cbd.mp4?token=WO9SRS5AHcqGY8l3X-N0H48TTOraB6JzTBHpkSway6vwoxcmyAog_bx0XiENUINtlgEl7qMchWISj1mxfvZ7-A1YSj1ITaBSp8JArW7yRJffI6NxSznc9v5_CHF2yTQouP-tSEAnFu53UoPma_QRrrXsWn0cZ3OFN4kKURROOvgnTGNmO0u4lpIquFh0F6_nVYP-LcJrRKN5SSHYTYj07Z_ThzSHlegaQOEGJYImVTjCR3E7ORdVbuITUmcap1onVicP82zgVzDFt7xzUVkmrq1qZz7t48b12KwitN6V9Y111tSMqrsm_z8tdj82xFu_GcFWa6AgppiFiP6w6MC2xZ1EbGkJGouETyBnt0lUd4G2tfW65qfwAI3B6HaDMzdazhw_GVf7PDRYFC1i8bqSjmFOgha9pilo6zeuVkHpMJgumNoTSzjzPSArQdx1onW1gTlINS4QINYIL381QXe7EV11Jm0lm0oCd9T4-00eH5nLxGWACoit4XwY0aHIxl5728B2U-v4sSf3um6Rz4AwfbtesWKvb7L92r1VIr9srLgeXQazjYKLAkhbSwPnECze4fF9uxGGEeBmiFWzZkr7_pAQMyqfBXJCMTZIQ-6FeBeeUtn7vz0QQMIGo1wSTkILVA5Afmm4kYugD0EU4HNW0pD75g4R6si6F0EFzY-kmyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a54c7cbd.mp4?token=WO9SRS5AHcqGY8l3X-N0H48TTOraB6JzTBHpkSway6vwoxcmyAog_bx0XiENUINtlgEl7qMchWISj1mxfvZ7-A1YSj1ITaBSp8JArW7yRJffI6NxSznc9v5_CHF2yTQouP-tSEAnFu53UoPma_QRrrXsWn0cZ3OFN4kKURROOvgnTGNmO0u4lpIquFh0F6_nVYP-LcJrRKN5SSHYTYj07Z_ThzSHlegaQOEGJYImVTjCR3E7ORdVbuITUmcap1onVicP82zgVzDFt7xzUVkmrq1qZz7t48b12KwitN6V9Y111tSMqrsm_z8tdj82xFu_GcFWa6AgppiFiP6w6MC2xZ1EbGkJGouETyBnt0lUd4G2tfW65qfwAI3B6HaDMzdazhw_GVf7PDRYFC1i8bqSjmFOgha9pilo6zeuVkHpMJgumNoTSzjzPSArQdx1onW1gTlINS4QINYIL381QXe7EV11Jm0lm0oCd9T4-00eH5nLxGWACoit4XwY0aHIxl5728B2U-v4sSf3um6Rz4AwfbtesWKvb7L92r1VIr9srLgeXQazjYKLAkhbSwPnECze4fF9uxGGEeBmiFWzZkr7_pAQMyqfBXJCMTZIQ-6FeBeeUtn7vz0QQMIGo1wSTkILVA5Afmm4kYugD0EU4HNW0pD75g4R6si6F0EFzY-kmyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوهای این خانم معلم برزیلی مهربان و زحمتکش بخاطر سبک خاص تدریسش حسابی وایرال شده:
تو یکی از ویدیوهاش که حسابی هم وایرال شده به یه دانش آموز فوت فتیشش که درسشو خوب بلد بوده به عنوان جایزه اجازه داده پاهاشو لیس بزنه…
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71653" target="_blank">📅 10:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71652">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20f71ea40a.mp4?token=s0Q8AP9OlFjCpEQjZhnisWOpwQnzFpKovK9L651AaVsCvyM2qM5eeKAdTm-hJt686AvRF9nxd5McccZv4d3pacwu54lY9UYVx0U_K264xnk7uxtS3FdJdnOtbJAnwdokOGSs4woH2MVcSs88DWqoQPaaalVJaE_ueaFlitbPcL8GURAtKr1er5eQr4mcQYnWy7zpIZF7Aw8sBwnobkolTHuP42lD79APSZTDKwRI8sJLaPdOXoIxVywLVqtq1zO8dIPeD8j1X1H4705yauLf6EX0lhmq5jAvZ748sJrxgeDnE4AJgeEn41p-Ag-ZH9V-IIJ0aLNirG3pI4rolbX55g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20f71ea40a.mp4?token=s0Q8AP9OlFjCpEQjZhnisWOpwQnzFpKovK9L651AaVsCvyM2qM5eeKAdTm-hJt686AvRF9nxd5McccZv4d3pacwu54lY9UYVx0U_K264xnk7uxtS3FdJdnOtbJAnwdokOGSs4woH2MVcSs88DWqoQPaaalVJaE_ueaFlitbPcL8GURAtKr1er5eQr4mcQYnWy7zpIZF7Aw8sBwnobkolTHuP42lD79APSZTDKwRI8sJLaPdOXoIxVywLVqtq1zO8dIPeD8j1X1H4705yauLf6EX0lhmq5jAvZ748sJrxgeDnE4AJgeEn41p-Ag-ZH9V-IIJ0aLNirG3pI4rolbX55g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوستاد خوش‌چشم، کارشناس صداوسیما:
در عرض ۴ ماه موشکی ساختیم که هنوز اندیشکده‌ها و رسانه‌های غربی موندن که سیستمش چیه. موشکی که بدون نیاز به ماهواره، ناو در حال حرکت رو پیدا میکنه و دنبالش میره.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71652" target="_blank">📅 09:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71651">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/168229fd60.mp4?token=a71Pz4T8sWfA1XpO_hypGEYo1gF0bhttOxGP0Hnum8RnDk92OZ-rMGs0zr1Hh0apzutZ9v0CUyF2A97rUrFJ0spkcy_tOL4oKABopoKtV5y3UtXjhU9YHkXrUL3GlgF2f1sPfKrPj8a7ksLPSGy_gLWPmSlB8d7ETj9mNeexPzTgCobmDB_Xl4Ms5anI1vbioynvapzH3zF74jhnRmaw_rdwWFssSDShqB78S2RfB9ZFXkVUtCTknTSOacp_X_C6lUTNIN_Vju-bUmpSOQGqMiZaxegoAJsW6wjSrjF9ooaaYMCn9EEZXCv2IpkgcLh99xLfwPkm-bGFF_zMQgPnEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/168229fd60.mp4?token=a71Pz4T8sWfA1XpO_hypGEYo1gF0bhttOxGP0Hnum8RnDk92OZ-rMGs0zr1Hh0apzutZ9v0CUyF2A97rUrFJ0spkcy_tOL4oKABopoKtV5y3UtXjhU9YHkXrUL3GlgF2f1sPfKrPj8a7ksLPSGy_gLWPmSlB8d7ETj9mNeexPzTgCobmDB_Xl4Ms5anI1vbioynvapzH3zF74jhnRmaw_rdwWFssSDShqB78S2RfB9ZFXkVUtCTknTSOacp_X_C6lUTNIN_Vju-bUmpSOQGqMiZaxegoAJsW6wjSrjF9ooaaYMCn9EEZXCv2IpkgcLh99xLfwPkm-bGFF_zMQgPnEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواب رییس کمیسیون امنیت ملی به روحانی:
اون روزایی که تصمیمات غلط میگرفتن اون زمان دنبال رفراندوم نبودن بلکه دنبال حاشیه بودن
اکثریت مجلس خواستار برخورد قانونی با روحانی هستیم و این تقاضا رو ارسال کردیم
قرار نیست یکی تو گذشته مقامی داشته الان از عدل الهی و کشوری مصونیت داشته باشه
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71651" target="_blank">📅 09:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71648">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8b5c1f510.mp4?token=Kp6zTb7wlT82fchK00YVYWKI24EvrO89jSslRV3lWdjIjz0UP8rg2KFooCitqvEcqhBPr39RAF5ldsxIv49X-0G9ICakwqSX5tJN1LSCj-uvd5Kthrqy9sZHIP-StyEX6KBSf5g1Cy73D84PCuCCjbG00ZCQd5guVeG4LjRaFt7XZjEX8uTcWIpPp8NFaJr1gNeyzgAzsIx9NR06e6GW1M8F9eljOupjYC08y43wqjrRolsoYYgv_ZrYXItByWZQGbBKdfJiYOv5ecCT3c7mSNGEcZ63mnEQGHawgdHAaqeWR-ctIcaAwfVjgQjU_WsP3oEOFjFV7y_wwrFB4PXYdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8b5c1f510.mp4?token=Kp6zTb7wlT82fchK00YVYWKI24EvrO89jSslRV3lWdjIjz0UP8rg2KFooCitqvEcqhBPr39RAF5ldsxIv49X-0G9ICakwqSX5tJN1LSCj-uvd5Kthrqy9sZHIP-StyEX6KBSf5g1Cy73D84PCuCCjbG00ZCQd5guVeG4LjRaFt7XZjEX8uTcWIpPp8NFaJr1gNeyzgAzsIx9NR06e6GW1M8F9eljOupjYC08y43wqjrRolsoYYgv_ZrYXItByWZQGbBKdfJiYOv5ecCT3c7mSNGEcZ63mnEQGHawgdHAaqeWR-ctIcaAwfVjgQjU_WsP3oEOFjFV7y_wwrFB4PXYdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل یک عملیات ترور علیه یک فرمانده حماس در غزه انجام داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71648" target="_blank">📅 00:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71647">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7qZs_5PbcaOuDWI2gtZP9qj8k-3OZ6TNDJNluEZM1gkpvdsh_3hx8desr1gdyCpww7eK9hBxjYHOTo6IC1FL3qIb2M7Seg-wVow6TA_-2oYfVycROT_Me0Z2OgPsUTiOu2nTPvjOY4RLjG2cn34kzcgAoYtCw4n8DK-VayLSdIiae9nEJK2nDWOjGmikuNOnLRLzfxt1Brab5FRw7A6s8ii1QFMOWwd-P9vKwE1fW7EmfLTdW35icdRpNLTi8ZJd6pDI5x62uvBYXJVlPURfdumc729Q4y4d6VVsekjaqKVdjYUsoSEp3tZDBDscFaJEOqdhhOALc18qoHSOTJMlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:
با سیگنال‌های متناقض رئیس‌جمهور آمریکا حواستان پرت نشود؛ از «مذاکره نمی‌کنیم» تا «برای گفت‌وگو آماده‌ایم». معادلات مربوط به نفت و تنگه‌ها تغییر کرده است. دست و پا زدن برای کنترل تبعات، جلوی آنچه در‌راه است را نخواهد گرفت.
تا زمانی که شروط ایران محقق نشود، هیچ مذاکره‌ای در کار نخواهد بود. تمام.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71647" target="_blank">📅 00:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71646">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فارس:حمله پهبادی ارتش آمریکا به دو قایق در حوالی بندرکرگان در آب های خلیج‌فارس.
تعدادی از صیادان مفقود شدند و عملیات جست‌وجو و امدادرسانی آغاز شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71646" target="_blank">📅 23:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71645">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAHLBRF-D1PQJlIuh3LKhZRzBcY3GD4OHQmU9UePLHMxsn5anlC-BY6O1wbSlwDKEt8wyRmFyn_27IQF1rqFjgSRCSj1iUmZ9rU2R5FCPirtmihWBrRcIjt37VaYhmRpuKIzKixjvkhuw7XhcZ25TGWjCKpdXkgcuphfiFFbclP5vsgTszxewHVwAblYwSj6kO_QPN9Vy8ICWSPUHb5DEwk5PpblNAlBPKmtDjD-FEJGlYmXL3XAIpOeTbfkMmxsMDTx7MwGZifoY4PLgqC0PFRoCu3J4TpB3XuOOZtJRSd7R-_mfIKB_gAgUk6D3_O5iJYlMV0d_yPeEq1Mp4pqOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
ماه گذشته، نفتکش «ال‌گایا» با پرچم پاناما هدف اصابت موشک ایرانی قرار گرفت و از کار افتاد. آخر هفته گذشته، در حالی که این کشتی در آب‌های ساحلی عمان لنگر انداخته بود، ایران بار دیگر با استفاده از پهپاد به آن حمله کرد.
این نفتکش هم‌اکنون توسط یکی از شرکای منطقه‌ای در حال یدک‌کشی است. ادعای کذب سپاه پاسداران، نمونه‌ای دیگر از دروغ‌پردازی‌ها و تلاش‌های این نهاد برای ارعاب و ایجاد مانع در مسیر تردد کشتی‌های تجاری در این تنگه(هرمز) است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71645" target="_blank">📅 23:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71644">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دیروز در بروجرد گروهی از معتادا در اعتراض به شرایط بد کمپ از اونجا فرار کردن و با این کار انعطاف و آمادگی بدنی بالای خودشونو نشون دادن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71644" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71643">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71643" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71642">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71642" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71641">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ya0Eso9x98s9vt--IgQOSDtB65VH1FjkgWJDX0tedQVBANJpmqpZvWgGwbxW3-9mvz0vGisuhy_qyVfOSB29b1uuXyRvdENiq5RTJNdQSJ5G48FQhhIsbgF9Cq_RnyXkm7SYeBlh6B1xbNz0eu7tYqW0FlseOZW440S3BL-dTGMAYHrywQzWm22YEJX4x_vqppw2qqcr9rKzSlMElEn5LQXCeSG6NWguLB9QzsbZuotICpf615msdgf8UNgpgJe33O_8nXVgMJc4Zv5aVJKqzSjYh8p-qwSPbhlY6UNFOR9axmDFmWF9-DIXQVQSSoFi6e1bzQ3kdF7HUtaU4eARdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران:
نفت‌کش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در جنوب تنگه هرمز، با یک مین دریایی برخورد کرده است.
تلاش‌ها برای مهار آتش بی‌نتیجه ماند و تمام بدنه نفت‌کش در شعله‌های آتش می‌سوزد.
سپاه پاسداران اعلام کرد که پیش‌تر درباره خطرات این مسیر غیرقانونی هشدار داده بود و تأکید کرد که تنگه هرمز «همچنان بسته و تحت کنترل هوشمند ماست.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71641" target="_blank">📅 22:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71640">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d776b60914.mp4?token=YEHruz6bGD2qj9XegqgebVkfR0BtepXLg0FiLa-llmYnHdiSIHDr6DYRlJcvymvdYigMYMDNqoaLPgpFDGYhUTpPZ6o8WnlnW2EjLm1MLT7ULynT46k4JyeVzxGdV1-Z2v15-Y4DHtKYS_ishiOS-6g_kgGK6h8Z4s_bjZJXWbc0FFQOlKwDVH92UipATlRr-4E3-29jShbu1jDQZiH2MtczYmQjP8oidHfH1IhOojWRhwO1uBmzEhyCs5R-7x_XCFWiiRO3lTIdalgsaxi4sVNjSHcu6xoQ3jSr130xGeUXL-ESqhfl2mmFwDFl4KtudyQPUDHu0tBvPeSFNN9ehw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d776b60914.mp4?token=YEHruz6bGD2qj9XegqgebVkfR0BtepXLg0FiLa-llmYnHdiSIHDr6DYRlJcvymvdYigMYMDNqoaLPgpFDGYhUTpPZ6o8WnlnW2EjLm1MLT7ULynT46k4JyeVzxGdV1-Z2v15-Y4DHtKYS_ishiOS-6g_kgGK6h8Z4s_bjZJXWbc0FFQOlKwDVH92UipATlRr-4E3-29jShbu1jDQZiH2MtczYmQjP8oidHfH1IhOojWRhwO1uBmzEhyCs5R-7x_XCFWiiRO3lTIdalgsaxi4sVNjSHcu6xoQ3jSr130xGeUXL-ESqhfl2mmFwDFl4KtudyQPUDHu0tBvPeSFNN9ehw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای یه آخوند درباره سرگرمی های روزمره :
سودوکو بازی نکنید اعدادی که کنار هم قرار میگیرن یه رمزه یه چیز نهفته رو آزاد میکنه
فضای سیاه سفید تخته و شطرنج هم شدیدا جذب کننده اجنه هستش
🎙
مجری:
اونوقت بگو هیچی بازی نکنیم دیگه
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71640" target="_blank">📅 22:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71636">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T6Ui-QROHeyams5oaPGBr7ABoiACn3qr6rDBA8paFj7lzlP9-14ljofcCK_5iKhRCJ3_sB5ItMikr4qF7qIMbmdDxb0M_1XOvmEpQgAf7gFX0MdyyqcOPZ7w-uKRpEKUoN9pn37gZw1EVedTgP57ZbCaPU_UuRuQyc3k1sdXtKT8pGabCntQl4yZ9MOFTLlsuKWXqMiZC1jD-l1hErXyNDnClm_ggiD1RWP_dOmJTeetFv62b77CnRb_hZ_9nmCoyVw7IwAiNYyQ9BqhU0KDtYyXrY9oan-sMQq3RtiEMqdfsN_PDDH-ncXFzEJ1DKRLOgZwwOB9eJAPLSQ00W43Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ObvxYiq8bEwOb8-fdNIhc1_aD5_wBMntKYIMD83T69KoJaMNmyJFT84e2PL7vpnitMIVqBqIYTl4w6mzheZIleRcwWik28vUvba_qTdB6CiYWDa7rU9An-CfbovKdie2GOrQBbR-8-Jfxq0BvLDgHhrzebI8S0GXtKkChyCREvEtiQrxTfGw5CHswwp6P2z8GNPzTdgZJhV2qgEBp8ThgTBYRta3LWAVbH-HLlcDURM80tTXl_ww0bwbg_c1oK_aAIr1N6EzdBW7AweK9S7LdrqNIY1UGmGSZ8klPs7b1HfSeN_KlHsSPPH0ybA0Y76P133LBecTDx409VnB1hL-5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیامکی که داره برای مردم ارسال میشه، از فردا رسما جانفداها برای شرکت در دوره‌های نظامی و امدادی، اعزام میشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71636" target="_blank">📅 22:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71635">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f9266483.mp4?token=Ygdspm2F_C7bV6NkF26X8FazZyUG3Js5_5QgndVC2suSUFbLgpRgwSY_qAFE8sMQc0WerJzJ4pKOviZUsRA_O1ZiWXYaWvDObf1O8_RZkU9SWzbPkj9BzMZgYoB63DbRyzb66p0gYGNdU4gcsl8AhHkdgOBaIV6JA_uo1-CPmBnSQ59pnHywSUNB7eCA3JbjIAQdBRXTFOpjMgAeq7D0tkWx8MCISShnl31NbukNfjpyTo6G-hKvXkgpzleGyMAnd5RNqrcAwq1QK_aF-sfnbfQoOCmbJad-0761KnAXqyUFvbzGNPvI-rZhUJ9xRqEEHmq2-X9gNmDAUo-dNPp6CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f9266483.mp4?token=Ygdspm2F_C7bV6NkF26X8FazZyUG3Js5_5QgndVC2suSUFbLgpRgwSY_qAFE8sMQc0WerJzJ4pKOviZUsRA_O1ZiWXYaWvDObf1O8_RZkU9SWzbPkj9BzMZgYoB63DbRyzb66p0gYGNdU4gcsl8AhHkdgOBaIV6JA_uo1-CPmBnSQ59pnHywSUNB7eCA3JbjIAQdBRXTFOpjMgAeq7D0tkWx8MCISShnl31NbukNfjpyTo6G-hKvXkgpzleGyMAnd5RNqrcAwq1QK_aF-sfnbfQoOCmbJad-0761KnAXqyUFvbzGNPvI-rZhUJ9xRqEEHmq2-X9gNmDAUo-dNPp6CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
سیاست ما روشن است: ما به نابودی زیرساخت‌های تروریستی در «منطقه امنیتی» لبنان و رفع هرگونه تهدید علیه دولت اسرائیل ادامه خواهیم داد.
به دشمنانمان می‌گویم: اگر تا به حال درس نگرفته‌اید و تصمیم دارید دوباره به ما حمله کنید، ضربات سنگین‌تری متحمل خواهید شد.
هنوز کارهای ناتمامی باقی مانده است و به یاری خداوند، آن‌ها را به سرانجام خواهیم رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71635" target="_blank">📅 22:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71634">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaasXlrYqUk7r84GSO8uZypmz07qii-lWerlC1UyaBuzSZMgNNFW64bz_XntBZpMLIeG-r1dt2lnBiCf2hXiVX7sz_MIUqIEAWNdvstX0w6ww4n2Uuqv6JtuxgAGmi5uJzgLraLeCvTEhve_kFg7mHY69-NT5U_sFcjMkC1RGhKDKEkrAAm85VExXgYTpkO-5HvC-U-N1BnHRld2_Gswq7gd4n-Ytx5P8jAag2JJ4mFfjcy8G9rywBDtmAUxzbPKW2q_JvDbW4gqV6c_nF7cejNAoy2PoDQwNtPh-QoMu1AMSgo_iV8uuWhDD7jfxe-PnwAMxO6b9_Bgax9t_Lxrig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
❌
🇮🇷
اسکات بسنت وزیر خزانه‌داری آمریکا:
وزارت خزانه‌داری «عملیات طرد اقتصادی» (Operation Economic Outcast) را با هدف قطع تمامی شریان‌های حیاتی مالی رژیم ایران و حامیان آن آغاز کرده است. به همین دلیل، من فراخوان جدیدی صادر کردم تا افشاگران اطلاعات خود را درباره کسانی که اقدامات تروریستی ایران را تسهیل می‌کنند، ارائه دهند.
خطاب به هر کسی در سراسر جهان که اطلاعاتی درباره این شریان‌های مالی دارد: این فرصت شماست. اگر اطلاعاتی قابل‌استفاده برای وزارت خزانه‌داری دارید، ممکن است واجد شرایط دریافت پاداش باشید؛ فارغ از اینکه کجا زندگی می‌کنید یا چه کسی حقوق شما را پرداخت می‌کند. اگر چیزی دیدید، اطلاع دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71634" target="_blank">📅 21:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71633">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdfmX0lo2vMOYEGYYNTcphRFQhhTCTOmOqYc7q0v4kx5C5ehZx2SZVYPBI7DDVtraBSgcvj_JXj37thLeLLrBwXuIGWdsNKCxHY0LkQxM7-r8jrIrhSHt4u7tcnbD2ftNhy-a2hmx8XVTyWssHjuPKNtzzwYVoZPFtB_HnXmyqBde5DLT3yvcp0c3nhnoh9d28-ZA0j1zPvV2Rqipv4-EsYVoMhOmxPLyVbMyZx4XksW4v5it8MdyapKFtcmS21PRHsZ7VmNPMyAkddZOmCjHa1HJJ01sl7SiCJNNWeqitqYZf-cRIUFLuTi3iUSwm3TvL3ERT0HJd6X8JX0XCQllg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
نفت در حال عبور از تنگه هرمز است.
کشورهای جهان — که هیچ‌گونه کمکی به ما نکرده‌اند — باید پس از پایان یافتن این غائله و فتنه‌انگیزیِ ساختگی، هزینه‌های ایالات متحده آمریکا را جبران کنند؛ و قطعاً چنین خواهند کرد.
ما این کار را بسیار بیشتر به خاطر دیگران انجام می‌دهیم تا به خاطر خودمان، و نسل‌هاست که چنین رویه‌ای داشته‌ایم!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71633" target="_blank">📅 20:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71632">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X22D0-EyPa5pO-XUOWfFW1vTggb7EMJGKv47RxKA8onE7qA6njUyUtXMScqj2-Y6Onng1JzQIwrdbXwchcAyU5Ph3RQwEWSwQ_dLqbtPj-qj52wv_hRN3oQF-y3HkS4nAEX7wvZ8G0H0nXjlScLF4VX93plYN5ZIK902bB4i54InZ9V0NjlEOEHReTmckGtuAOoQXsJ4uHmkNblTHA1MuirH6xobu9ySKR_VO66R9-jlxx40_E3Gn_boIKLBwUIp1R_yMCPkwPx6xAPuResJuSsipGErh60Sl4RNz-2bGMb2GH8LnfskGFM8eYB-ZB7k4K4Ux7dCgNM5i6cfauPRrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
امیدوارم همه متوجه باشند که افزایش قیمت‌ها در سراسر آمریکا ناشی از عملکرد «جو بایدنِ خواب‌آلود» و دولت او بوده است، نه «ترامپ».
حتی قیمت نفت در دوران بایدن بالاتر از سطح فعلی بود، حال آنکه ما مانع از دستیابی ایران به سلاح هسته‌ای شده بودیم!
به‌جز نفت که فعلاً وضعیتی متفاوت دارد، قیمت‌ها به‌شدت در حال کاهش هستند؛ قیمت نفت نیز به‌محض پایان یافتن درگیری نظامی با ایران — که زمان زیادی هم تا آن نمانده — به‌شدت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71632" target="_blank">📅 20:08 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
