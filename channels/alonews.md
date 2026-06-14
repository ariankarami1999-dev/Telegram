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
<img src="https://cdn4.telesco.pe/file/uCVdvWSDkQODwAOmJb-g6QbP0m0HQFHmxtnM6sCoAA1bxKjjXG_8093pOXGRdESjfMyLPAkoII7rPicFnG47zm36b6gTLarRFlm7iR5yWABDvznaYOVpu5x_2nTR7zftdIO_xuuoC9laJM3mOXa2x8OTVsEzVlGQrz9GH2BIHJqNZVik2dmKNHlfJVHVgaRW6hY75H45lXh8Hl4g8M_M6WfKJOiJDxBsPAqLQrHDiXRW-MbYiHNJxKlXia4hr2FnVxOZwKqOPZzSsJ4Lr8qaTxiRe-l7WQZbVjGgcXNGS0zLQIlpAP7H6gqRk7Unwn4JBx_9Neo7Vg-G9UIlXGBBPA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 978K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 01:32:36</div>
<hr>

<div class="tg-post" id="msg-128050">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1c79ffcd9.mp4?token=UyTwgfNQw96hQIsgL8ZdC2pimHRtJFDg55sC0nx4lk0E7QKM21sVoqsFWOrr35UE4ihU6daw1V6ZVKxws6CE61ao2qDY1BHOAwh7_OtgI4tmGAeoVu0SzmOHclXSMI22k_14103IFnbS93SLsz5AltvnqRl5dBV96dgZj0hEMwYFQtSJVkfKPs_AU4DBcSLDHxD_5iG8Ske-vZza2vp1sthraGf6Na_4ES5K2Mp1VOawwrVsSuY59ZOhrs2BLSCbRuLAQKECTrFQjbuBGG3L7XuKpdFQqlFm_Iz9pIQna4apcfOfYxE6pQKW8IdN82U7w9gMUGN97anRB25I0G0HGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1c79ffcd9.mp4?token=UyTwgfNQw96hQIsgL8ZdC2pimHRtJFDg55sC0nx4lk0E7QKM21sVoqsFWOrr35UE4ihU6daw1V6ZVKxws6CE61ao2qDY1BHOAwh7_OtgI4tmGAeoVu0SzmOHclXSMI22k_14103IFnbS93SLsz5AltvnqRl5dBV96dgZj0hEMwYFQtSJVkfKPs_AU4DBcSLDHxD_5iG8Ske-vZza2vp1sthraGf6Na_4ES5K2Mp1VOawwrVsSuY59ZOhrs2BLSCbRuLAQKECTrFQjbuBGG3L7XuKpdFQqlFm_Iz9pIQna4apcfOfYxE6pQKW8IdN82U7w9gMUGN97anRB25I0G0HGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برخی کانالای انقلابی در ایتا نوشتند که این جام زهر نبود بلکه بشکه زهر بود
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/alonews/128050" target="_blank">📅 01:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128049">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a32b55890.mp4?token=XqfggPgx4ihN2LNA_XmQHmQgIT9NV9V_dBoefUihaznDz16kYSu1mQ_z7SQiv7qLwZF8kLVVWmjtlX0ZpJn3SYMgd66DkcbUCvUS6umWSePEtaZXOEi4lyB2Fnmde1mXJi6DpVnd-SWvw7mHQWoODuOxGNn4_deSz-_G9OJesLzAZhz6GMZIpwOGnApSuio9DYh-kKeB2K4cDxXY3eYRQhTx5aOIPxhLaf7Lu2-kJ2RTcGsSPLw-9abbKk-5OS4AAwrj_SsBuiUAJ8wpfSbJoaMm14Fl_3drNzFWKXyXR5Vfj7FPIARYoy2na5Nd3Nwi1GIS-aQ-meRSZfaoBqzW2Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a32b55890.mp4?token=XqfggPgx4ihN2LNA_XmQHmQgIT9NV9V_dBoefUihaznDz16kYSu1mQ_z7SQiv7qLwZF8kLVVWmjtlX0ZpJn3SYMgd66DkcbUCvUS6umWSePEtaZXOEi4lyB2Fnmde1mXJi6DpVnd-SWvw7mHQWoODuOxGNn4_deSz-_G9OJesLzAZhz6GMZIpwOGnApSuio9DYh-kKeB2K4cDxXY3eYRQhTx5aOIPxhLaf7Lu2-kJ2RTcGsSPLw-9abbKk-5OS4AAwrj_SsBuiUAJ8wpfSbJoaMm14Fl_3drNzFWKXyXR5Vfj7FPIARYoy2na5Nd3Nwi1GIS-aQ-meRSZfaoBqzW2Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/128049" target="_blank">📅 01:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128048">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
غریب‌آبادی، معاون وزیر خارجه:
متن یادداشت تفاهم نهایی شده و امضای رسمی‌یادداشت تفاهم اسلام آباد روز جمعه در سوئیس انجام خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/128048" target="_blank">📅 01:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128047">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">«تو رستمِ تهمتنی»</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/alonews/128047" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">😐
😐
😐
😐
😐
✏️
✏️
✏️
✏️
✏️</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/128047" target="_blank">📅 01:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128046">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
برخی کانالای انقلابی در ایتا نوشتند که این جام زهر نبود بلکه بشکه زهر بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/128046" target="_blank">📅 01:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128045">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
خیلیا میگن حالا چی میشه؟ هیچی ۶۰روز قراره سر مسئله هسته‌ای مذاکره کنن و احتمال قوی توافق بشه، چرا؟ چون اورانیوما قراره تحویل داده بشه فقط بحث نیابتی‌ها و رفع تحریما هست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/128045" target="_blank">📅 01:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128044">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIIh36E5Lcml2UK-nKKyZZkCVUkHrSe8-MYoSwN1d26CUZaU62EMTNypiX8NJLK1iK0YHARI7JluboV-O6qxFQfZj-yAk8g7PIhb4o5bMzjf_kUdJLBFnVO-I6-r-p0b615ilPacaTJj9ieLurT98psj0acaJ-i3BCQ7CdAKFO7r8baq3Wm1b5dEfeTuMkqff3pDL3R_PYWuQlrVk5MZHHYA5aPPJHoERXRpvEXB7CZB2CLleKNjenrkVydeN-cHqHMYlLztvofnRxNi48r6tDzJYuuOjAFQsXrqGwbx0gecMJ7xGXzEWpunHERDUi6yeagit-N1E2j-1xnwOHlj5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کریپتو و طلا صعودی شد/نفت کاهشی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/128044" target="_blank">📅 01:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128043">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTtG8vy6qgfO1imbvMp-bGHoDlayEPe45VScAZvj5fSvcB4Wv0dqA5q9K97oka53PU15NLl31Jg9ydq-sfDuJDc-ShysRw-z7O0072ecKgESpRYI14uocUnFEeCx8K4G3IfZ75MmljnCrzl6K7xtRkcj6EDVj1w5qtJEaKnFB_xD5ihyqQS0U6rUEgaEArimi8uDgauX941z1vJUETJmIOpS4PVKl2mvmTxHZvk8ubmg005a9SnH35ymB27jwZ7uZkaQkx_dxpxF-wmEr0wvropy-pZXyquBQcF9FvON_U_v1wOe3jA2mGa24rmUGMEx7GBBA6ht1OL2zX3m3Rpc6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت گروه‌های انقلابی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/128043" target="_blank">📅 01:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128042">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
به همه طرفداران جمهوری اسلامی، استعمار شدنتون رو توسط کشوری که 47 سال مرگ بهش فرستادین تبریک میگیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/128042" target="_blank">📅 01:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128040">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
منابع حکومتی: بعد از هشدار قالیباف، ترامپ ترسید و محاصره رو یکجا برداشت، برای همین انتقام حمله به لبنان رو ول کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/128040" target="_blank">📅 01:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128039">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQ_pJ2K8kUBsrAbfXHBGkOeBSmngJZl4UkOvl2iE5xxgWwZ2HdeS9cT9YeStKnrEJ6jmW7eS_rVT_DhoIsbXkyQG1W4i0tKbvle6jVGwOBlyR5R4SSB_y9j236CtNNdL8dH-C8igY1J--_blLTVqqwGr0SnvY6VH0QFU8BJ_RXMKjTNZbyIRhvEYISlcysPgasB8oEssGO9o3jqTl3jQiY8gnWQMIJZljRI87lcoH6BJeIKL5Y5Ivb0K0WlhBIUZoRvNzxzmYM1G0SBIIC-Kf9kHTft3ULHjYjCRgsysbBz48BOmW6seqsGzFGlNUMFa98FzA87hQu8O1NXmWTcgEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدا و سیما: عقب نشینی حقیرانه ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/128039" target="_blank">📅 01:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128038">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5391f1a037.mp4?token=OebIQsGOSZwGvcVCjxhPK1Ylg5I3J2dzwENHMrJYv0rJxTbzUt7HsCemRt6ySg1i3_ADTZQftFOarBGfVw5CIbwh72eezzeruh90_lwvENJfgCb7TyX-tKjraMLp6WFHug7vkozXu2NIvBGiTzyD5tmfrX9qFD9yQDM2k-iZhFlnXecdTzW3p0156o2hOxMtDywJuMkqN9dnLLhTzMc8nZMyjWbQ2as3yXKNlciLE064dXMdOynPseneAFIfBKzYu_l-D-YuEeNHKvOQ7OVY2d9aBxM0ApSEM4Q1NF0qY4x4z4hj-7q1K-HcmxYmEMnOvbibIijSwL7bDBJEDrkStw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5391f1a037.mp4?token=OebIQsGOSZwGvcVCjxhPK1Ylg5I3J2dzwENHMrJYv0rJxTbzUt7HsCemRt6ySg1i3_ADTZQftFOarBGfVw5CIbwh72eezzeruh90_lwvENJfgCb7TyX-tKjraMLp6WFHug7vkozXu2NIvBGiTzyD5tmfrX9qFD9yQDM2k-iZhFlnXecdTzW3p0156o2hOxMtDywJuMkqN9dnLLhTzMc8nZMyjWbQ2as3yXKNlciLE064dXMdOynPseneAFIfBKzYu_l-D-YuEeNHKvOQ7OVY2d9aBxM0ApSEM4Q1NF0qY4x4z4hj-7q1K-HcmxYmEMnOvbibIijSwL7bDBJEDrkStw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/ ولایتی: فرمان صادر شد؛ لانچرها آماده پرتاب میشوند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/128038" target="_blank">📅 01:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128037">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
فارس: مسئولان قراره بیان صحبت کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/128037" target="_blank">📅 01:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128036">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
به همه طرفداران جمهوری اسلامی، استعمار شدنتون رو توسط کشوری که 47 سال مرگ بهش فرستادین تبریک میگیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/128036" target="_blank">📅 01:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128035">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
مجری صدا و سیما:
پیروزی رو به ملت تبریک میگم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/128035" target="_blank">📅 01:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128034">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
راستی ۱ساعت قبل از اعلام رسمی، توافق توسط منابع الونیوز در کانال اعلام شد
🙂
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/128034" target="_blank">📅 01:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128033">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmh357DrJvv-yAPE5YhcRk0f6FqLqeccI73x6_PnIpvAu70ouozr1aSU_9gNtzZ0HpuNbX7eK9h3Kz2wxmV0E0ixtym9spyy6Ebrpr924PqPwE-iVXY-VrXmgWNuXD6iyOHaE8MxvC_jB6hsndtvFV3oAwMwazdmMgz5EQA3YF13iE9K4j-A4kNvFP6mkBfqfNCd1iZlfp9fyYGGZeH6x2SjKVuROjwMtu6v_-NjTg95YMJcmgkzfgjHwV6UNCVeFiF1ktNp_BaIT1lDIlujfOh40T__BxBz2ss_8kPzUBCO4UdD7yGoObth4xnWRsrdioNdVeuAkIldTRghlqwiOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حاج حسین توام خسته نباشی
😘
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/128033" target="_blank">📅 01:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128032">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfPMmq9qOSovcx7qbbmvwRm3TN_EW0uC25lOuugkjKTEd9Hh43cEg14-etSIU5JwFs2deVxs8JdJ2trPSXPLaLC3npemuO6DtX2ZM3EG5S-7TBELDLU-80l4wnfu37B0Z5Ji-g8n-ivhVjvxCcG6KBsVdgZdrICwT3VruULtt9grAMhOzca2aUK2_3UuHxGoYMu6D0bQwNdxVlo8wpcf6AxeG-P7yhMKWmL1206EQ9g6KkdD4V-ix49lWh1aD9eVJTQCv9_IlC2AtH3h2kqNmUG8hI33dZjkgg0liD09qfTu5snZntOmPvwargWUnMN8gRBmWtObbMkAHjpeZrF8Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از همین تریبون به این عزیزان هم خسته نباشید میگیم
❤️
برید خونه حالا
😂
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/128032" target="_blank">📅 01:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128031">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0Q6wET1s7QtAFBqLSaKAW9AYudAC6-LCy4wb8ckqyjDHZR4nqGPOL5L9iSsKcW0gZDzYRTsAGFB6b1URiBQ4b2h_wCSWilv47mvNZ6_13X8mi4a-gzPKln16qChXAtOyEjvuI2seKDGo7nhXGzAiYPvhRO33jtaTEVC6EKR5uvrBpOnra1N5Dwa-DGkFqwuq6XWHGQGpf2Z6mYa7OMCWGS4iaHdbJ8LAftKtkbtM0ZHYitmOqGDOLYmcOT15MGAJL7w-C_Diuu_zwk9U9b2cajGV1E-NxDsSBMWvJG797yTbsNgVwOpWA5ot7Y0ZPHq9xqlIlG_ur_FpEjCwZW1Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دکتر
ترامپ:
توافق با جمهوری اسلامی ایران نهایی شد. به همه تبریک می‌گویم! بدین‌وسیله من به طور کامل اجازه بازگشایی بدون عوارض تنگه هرمز را می‌دهم و همزمان اجازه رفع فوری محاصره دریایی ایالات متحده را صادر می‌کنم. کشتی‌های صلح، موتورهای خود را روشن کنید. بگذارید نفت جریان یابد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/128031" target="_blank">📅 01:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128030">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ترامپ: توافق انجام شد، تبریک به همه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/128030" target="_blank">📅 01:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128029">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXKqt8N95ZWwSWNdbiryfBHj-Z7ocVxfDLCCNdeUVtxn07v7lge0iX6Ueb_PIl6F8XXAbpQ3gHmko2Ue2Tm-SjfOqxh8KpEwQYiYne8yrmgRX08YYyKDNelvtj9GuWiGjX2LLLCmWVc3dlsIJ--UY8IWBJGc-NQLUACP9yJpJ1G5nfu06f5E6mUSVwL5BixKyUH2f4U1i79_pIBIoj1u_5SN1GMHCfMVIbp5A8IHqSQkHaE3Ib1LAPs4HF2L2uy6kZt_J4bPirUN45-M2vPOwWBQuo_5KrF1-fePhJR5p3lY9RVx7Z7QeiNMKg4ZVSNPccXDVut4aeTrkiEG79_Aig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#انتقام_سخت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/128029" target="_blank">📅 01:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128028">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjCaBlj4vFq41cPc4gRcm_Go1wi0yFcRLSFYAacwzxJytsZsDlnU8jt9FOnnHjCkNTTWcB0g1hbxzwYa1X6ZcNL3jBOtoWEP68aJemem28L47Ir7gazoYmn_nIAxRTEpYyvoPxebk-_q1Hg6AL7-QZWre7r-tTfKXbhdmtoVkQ2aYxQ1EwgRVCnt4yBVQgB2uK8MbTg-T2GxVn1dzvkmxUDKyffY-S3oq4J_c8Vn0bDS-jIoNrrEqeTH6DWA-FA9ln0R8L_cd9C-74N7nzXksut5YA7tWT-BImQPtOEgO4RY_zsyqch6LPYmTs0dsLgXj1rd1WPSqZ89XSOGQE8S5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه خبر هم توافق پایان جنگ بین ایران و آمریکا رو زیرنویس کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/128028" target="_blank">📅 00:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128027">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
از صبح توئیت و .. که میزنیم میزنیم، نگو منظورشون امضا بود نه حمله
😂
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/128027" target="_blank">📅 00:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128026">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
رسایی: توافق با قاتل رهبر را
#نمی‌پذیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/128026" target="_blank">📅 00:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128025">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
خب حملات موشکی هم انجام نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/128025" target="_blank">📅 00:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128024">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-5PqgBl62Kwi0jokWPK6EF4E6xwkASYmfuFn-QysXp4TYNO-Bq3Gt4BeGgniOKtnyhVmnUSkc35-3_UES25zLTwNVhQUFFyDejx9JTToJODy8xzrAwBsvw_w_A0TDDLAHRWoWzFTHT_Dqpz5S-U8jvTy_7rVjS8nczJy2p1100AKDpg0dOKDPb1TKcNga4MSTlPSgMuKllueg7TeeFtcPbcMpWP8euAsclprzCTZdGqqInAUJIHRwRPAkV05XtVdGqV1odkSL-dM2XIkKPDUY6C8l9fy9gbKgTRLJU9J2dCroaHnukcuOD627DW1R6gdrKmRSxHFBrBP7kSAAJ0rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست‌وزیر پاکستان:
پس از گفت‌وگوهای فشرده،
خرسندیم اعلام کنیم که توافق صلح بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شده است
. هر دو طرف پایان فوری و دائمی عملیات نظامی در همه جبهه‌ها، از جمله در لبنان را اعلام کرده‌اند.
🔴
مراسم رسمی امضای توافق روز جمعه، ۱۹ ژوئن در سوئیس برگزار خواهد شد.
🔴
ما از ایالات متحده آمریکا و جمهوری اسلامی ایران به خاطر تعهدشان به یافتن راه‌حلی دیپلماتیک برای درگیری تشکر می‌کنیم. همچنین قدردانی صمیمانه خود را از برادرانمان در این تلاش میانجی‌گرانه، رهبری بزرگ دولت قطر، برای حمایتشان در دستیابی به این توافق ابراز می‌داریم. به‌ویژه از رهبری دوراندیش پادشاهی عربستان سعودی و جمهوری ترکیه به خاطر کمک‌های عظیمشان در این زمینه سپاسگزارم.
🔴
اکنون که توافق امضا شده است
، میانجی‌گران مجموعه‌ای از جلسات را در این هفته تسهیل خواهند کرد. این گفت‌وگوهای پیش از اجرا، پایه‌گذار مذاکرات فنی و مراسم رسمی امضای توافق خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/128024" target="_blank">📅 00:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128023">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فووووووووووری/توافق رسمی شد
🔴
پایان جنگ اعلام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/128023" target="_blank">📅 00:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128022">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ: ایران در توافق پول نمی گیرد اما احتمالا تحریم ها از آن برداشته می شود و خواهیم دید که آنها چگونه رفتار خواهند کرد‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/128022" target="_blank">📅 00:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128021">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ترامپ: «بعداً مسائل هسته‌ای را حل می‌کنیم» و افزود که «هیچ عجله‌ای نیست» و می‌توان ظرف یک یا دو ماه آینده به آن پرداخت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/128021" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128020">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: از دید آمریکا علی خامنه‌ای مانع توافق بود که حذف شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/128020" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128019">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ترامپ: رهبران فعلی ایران بسیار منطقی تر از رهبران قبلی هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/128019" target="_blank">📅 00:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128018">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترامپ: توافق ما شامل تعهد ایران به نداشتن سلاح اتمی و باز کردن تنگه هرمز است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/128018" target="_blank">📅 00:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128017">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوری/ترامپ: امضای توافق احتمالا توسط خودم انجام خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/128017" target="_blank">📅 00:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128016">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فوری/ترامپ:
علاقه‌ای به تغییر رژیم در ایران نداشته و ندارم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/128016" target="_blank">📅 00:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128015">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوری/ترامپ: بزودی یک بیانیه خواهم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/128015" target="_blank">📅 00:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128014">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLKtisQELaAh3bwUo0P9CtVNGaL21zWXwyJRiNfbDZmlEAuDwPTTT8FS1zuPNvUVegovL9Bbcd6CGQI48kSUSCe6x4j-68RRQeA3pOR7wtmQfY154T1-NarsLwou_w3odeZiGrxmnqnm-x2ZGKRu_NPp40MqIe3mut9MSdRxOySNYjmiozUZJZGsl5cSHwLRo3AvS_ANMJpxOuS5TBkuVuvD2sHuUNmXrqgNT8Xej0MMitYiUD6922HHDv4cD9fe4fKOUjXuzI4CqE4glxTZH_8fAMbql9hnkaNJfcOOj8QTQBIcsjRi2uso1Isjfl_Ve3MNg4qVU_t_XG2PxAnWRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت وزیر کشور پاکستان:
الله اکبر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/128014" target="_blank">📅 00:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128012">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
حسین پاک، خبرنگار صداوسیما در لبنان:
امشب به صورت همزمان ایران، یمن و حزب‌الله به حمله اسرائیل به ضاحیه پاسخ می‌دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/128012" target="_blank">📅 00:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128011">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsR4SfTQF4fm0sd3iLSqpXtEvoP2GHdncG-fZotS7UGRoYHy2VjDvX347WJ1AWvDosJdL2qha74wHnP5cpd4ZS5MZj_TQvQFtllxWGrdBdp1tM8_jNvF7dh2a0Rcl6orwmnW5640Ni5YYrdhbFoZiPgfjccoTieMz_iM_Cghiehvll7Idj0LnBjxrPbbVlQPBeTuQYfFLP3JZ2p8KLHX4DJBuoS5FREtcTuFQcCQFmyQHToBUWxXVSMW-fhh9aP7W38CaqSHhLOuVpNf1MYj3o4ivOzNDntqbJGb1e6jivdllWW2nalp_tYydhRZGXzVuQDhOFFNH62f6I46RXiWtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:ایران هرگز سلاح هسته ای نخواهد داشت و تنگه هرمز به زودی برای تجارت باز خواهد شد!!!‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/128011" target="_blank">📅 00:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128010">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e23a8dc55d.mp4?token=pjU4kXC9dtjfvQj5s7GE49s_a0ELWv7cHfnjRRnRQcq9qTd0pCyWuqa0um_CAJANe2pwAI1uyiM-MmC46LGCrdXJ6ALMVYtu6_yRYDlhr20MMLzfN4p4luG5MEKfYC08rTZJAaBJFhAMACwncHSrGVfkCgU00nEDZ_FZcP0S9UPAtQA1hO9ROQRrHmX7jXCH6CrfmTbfBbD85wkI249Kpo81RrxQRDT6ADz_FkRiR1Wma2Euj3saLJZ4Cer_j5qluQGk97JOlCUEVZfrWSsNaGi9-h_rAjNI0vQKL7xR-BWVDsNJmAtNLVPCSS3cS4IOdox3Q9uPAJlafFRdgC3N8Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e23a8dc55d.mp4?token=pjU4kXC9dtjfvQj5s7GE49s_a0ELWv7cHfnjRRnRQcq9qTd0pCyWuqa0um_CAJANe2pwAI1uyiM-MmC46LGCrdXJ6ALMVYtu6_yRYDlhr20MMLzfN4p4luG5MEKfYC08rTZJAaBJFhAMACwncHSrGVfkCgU00nEDZ_FZcP0S9UPAtQA1hO9ROQRrHmX7jXCH6CrfmTbfBbD85wkI249Kpo81RrxQRDT6ADz_FkRiR1Wma2Euj3saLJZ4Cer_j5qluQGk97JOlCUEVZfrWSsNaGi9-h_rAjNI0vQKL7xR-BWVDsNJmAtNLVPCSS3cS4IOdox3Q9uPAJlafFRdgC3N8Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تجمع ۲۰۰ ۳۰۰نفره امشب جلوی وزارت خارجه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/128010" target="_blank">📅 00:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128009">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ot07Wv_X4i2Db-dkx3lAdtCKWDVYlUUktyFOLbJ9fFJoUfMX3bm0fQrWL7a_yuBJi1uIh5SLPMcOyEK-CAJZDXvmlQ69RDT4UqqRq5dDQzq37mD5pxV70HY7gyHKV55SbO0LtXwwSuQhZePP9tMadDrg8G35z8LhUmP1nkBNT75iPPSlKqkvZcAuxPDGIMGw-LZScNsc8GV07Ww1zueiI9rM_RZS-HOnvPsGXa3ERPVnxLtaNbcebJ6dkoF1TCgjAdLmFAHhqq1NtetbaYE99lWSPw3lIicVJbQIphMex2NYdWmz01eg6B5cmchQo5OmG1x9bnif8l9_L0Js6XKTmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فارس:
دکمه جلیلی فعلا زده نشده و همچنان سرکاره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/128009" target="_blank">📅 00:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128008">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdH9rIoKtEvxYPWzhrg4xgVIqgcMhORLbapeyup_OerWMXnGROxOGcuiyreb1njUiU1iCBljANtdhHW4iThp5dL4E-C5h4nIML-g_i6Jc_OHE06PBhzjfpaua_SYvAzYGBwZA-O97Hw-vlTqbfZd0o48kNfC5HA_mwefmhVOEau6-HZX4JVrPFf1N30hzWB7Cq_cUyS2kP8L6vXvvCtl53G7Q82bdwKSTXcBpRU7eIlZHcxBPBZet97dqjgXys7pGGjakdK-dULQ0xOyZvv769UZ-IltlXxCvByPccenzOKNM_EI6ooFawme3uw02-FyxtyH84HirhjxNT3y9cnDgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : جک رید، سناتور رود آیلند، گفته توافقی که الان بستیم از توافق زمان اوباما هم بدتره
-  به نظر من یا داره عمداً دروغ میگه یا اصلاً نمی‌فهمه موضوع چیه
- توافق اوباما عملاً راه رو برای رسیدن ایران به سلاح هسته‌ای باز می‌کرد و کلی پول هم بهشون می‌رسوند؛
- یکی از بدترین و احمقانه‌ترین توافق‌هایی که آمریکا تا حالا بسته بود
اما توافقی که ما الان انجام دادیم دقیقاً برعکسه؛ مثل یه دیوار محکم جلوی هرگونه دسترسی ایران به سلاح هسته‌ای رو می‌گیره
-  مقایسه کردن این دو تا اصلاً منطقی نیست. جک رید باید پاسخگو باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/128008" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128006">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
سی‌ان‌ان: یک منبع اسرائیلی گفت: نتانیاهو به دنبال دیدار فوری با ترامپ است
🔴
این منبع افزود: نتانیاهو تلاش می‌کند پس از بازگشت ترامپ از نشست جی‌۷ در اروپا، آخر هفته آینده یا اندکی پس از آن، دیداری ترتیب دهد.
🔴
ترامپ روز یکشنبه پس از آنکه ارتش اسرائیل، بیروت را هدف قرار داد، به شدت اسرائیل را سرزنش کرد و گفت حمله به پایتخت لبنان «نباید اتفاق می‌افتاد».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/128006" target="_blank">📅 23:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128005">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
یک دیپلمات مطلع به سی‌ان‌ان گفت: مذاکره‌کنندگان قطری هنوز در تهران هستند تا اطمینان حاصل کنند که مذاکرات در مسیر خود باقی می‌ماند.
🔴
به گفته این منبع، مذاکره‌کنندگان قطری با هماهنگی ایالات متحده در پایتخت ایران به سر می‌برند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/128005" target="_blank">📅 23:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128004">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
صدا و سیما: امشب رزمندگان اسلام، اسرائیل رو بمبارون میکنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/128004" target="_blank">📅 23:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128003">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
یک منبع امنیتی اسرائیلی گفته است که نخست‌وزیر بنیامین نتانیاهو انتظار داشت حمله به بیروت باعث تشدید تنش‌ها و به شکست کشاندن دیپلماسی شود، اما مذاکرات با وجود این حادثه ادامه یافته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/128003" target="_blank">📅 23:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128002">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0466bd76.mp4?token=lAwKsan_lt1BDSIAYuZ44XYx3__u43ylkMBP0p5Lkmioqlk7H_845GamIAjFYdN4U71bLO_xE5mvbUKfYa9X7a5LlQqjJSTyedWG0ExhIxms4MS8evBqw5i4JMDd3QH0kuXExJ6hNpMJeYQTjxDATmhQXqRt9izddDKj3p6KJArTulhk6wKrqmc3jcOs_qp6hwc5c9aoExkPS9Kybrb3TV8KRhKOrrwe-OQO07ufEZsIw61L-zkpyrTXdFRUn37fWO6rTbfNSQA4RJGyB5exTMYGTk3Mg_NbRgNaSUF5jmcHWmOMiPaQimwr7bQyT2Rzlr67mWPuzczWhJvyF_0M-XON36_lHnzzU4TkJMKGtyQaNrrpqZav_XADOjlB6knz6AxJjHkndXLw3lWmDx6dP70SzeIt1mtDx7tLMohARvA4ystv3ZLHvvgrPti-DNzFm_-PedQWg-zpMQ-K4DIZM7P3wpkWF2EBPon-nHLVy8_75kkpKFc0sqLrnNAPEGuP0MVVG0Ip7-AwzqGdthS0qmIt0Q8ieOeRZvg7IAQhCZGL_IAlXsO7wnbLqxOpRu1aVbSO2qSlqe0fiiL1-UnoYrjVxco50qiZw6d86MeWCyHxgJ2PND9jsVkmjLftvMYH7iqh5NeZyVemu1wicxqWZs7iUYnLE27nJCHf9yKnEU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0466bd76.mp4?token=lAwKsan_lt1BDSIAYuZ44XYx3__u43ylkMBP0p5Lkmioqlk7H_845GamIAjFYdN4U71bLO_xE5mvbUKfYa9X7a5LlQqjJSTyedWG0ExhIxms4MS8evBqw5i4JMDd3QH0kuXExJ6hNpMJeYQTjxDATmhQXqRt9izddDKj3p6KJArTulhk6wKrqmc3jcOs_qp6hwc5c9aoExkPS9Kybrb3TV8KRhKOrrwe-OQO07ufEZsIw61L-zkpyrTXdFRUn37fWO6rTbfNSQA4RJGyB5exTMYGTk3Mg_NbRgNaSUF5jmcHWmOMiPaQimwr7bQyT2Rzlr67mWPuzczWhJvyF_0M-XON36_lHnzzU4TkJMKGtyQaNrrpqZav_XADOjlB6knz6AxJjHkndXLw3lWmDx6dP70SzeIt1mtDx7tLMohARvA4ystv3ZLHvvgrPti-DNzFm_-PedQWg-zpMQ-K4DIZM7P3wpkWF2EBPon-nHLVy8_75kkpKFc0sqLrnNAPEGuP0MVVG0Ip7-AwzqGdthS0qmIt0Q8ieOeRZvg7IAQhCZGL_IAlXsO7wnbLqxOpRu1aVbSO2qSlqe0fiiL1-UnoYrjVxco50qiZw6d86MeWCyHxgJ2PND9jsVkmjLftvMYH7iqh5NeZyVemu1wicxqWZs7iUYnLE27nJCHf9yKnEU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس شبکه افق: امام شهید ما خونش را برای اورانیوم گذاشت ولی امروز مسئولین جلسه می‌گذارند و می‌گویند اورانیوم به درد نمی‌خورد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/128002" target="_blank">📅 23:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128001">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚀
Exo VPN | سریع، پایدار و بدون تبلیغات
✅
اتصال سریع و پایدار
✅
سرورهای متعدد جهانی
✅
حفظ حریم خصوصی
✅
کاملاً رایگان و بدون تبلیغات
📌
دانلود از گوگل پلی: https://play.google.com/store/apps/details?id=exo.vpn.app
📣
کانال رسمی: @exovpn_dl</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/128001" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128000">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crpeHZNiImB1FnbaGEax-0TmE67nLVUTjJL69dRtGymKa_c2RzuyfzZKBJi9Nt5D9m9zYEvc_LX6dDCi_s_GJiAm1_XKPtL4k6y8b9Rv5t_mWOKPUwcHgFEiCvLiGvh_vSIY4P2Vy_aQdeW-TNVKloZlCBKAlpUV15IiHJRV9dOzRb9R8_c0C5LkgHnT2XAslRJ1wUP6fiy181Jd21CMkbBLSlAgTXM9QXeLwYYpjOnDp1gxOHRhyd05UoMl1Y97il97wqwTBHoPrzkeuoioXA3uOVyUD-rcOO5eHlkSUg3n7rBGIZ3tV2E9_ZWpnyvH_QoM2oMFqp9mCawg85-zJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Exo VPN | سریع، پایدار و بدون تبلیغات
✅
اتصال سریع و پایدار
✅
سرورهای متعدد جهانی
✅
حفظ حریم خصوصی
✅
کاملاً رایگان و بدون تبلیغات
📌
دانلود از گوگل پلی:
https://play.google.com/store/apps/details?id=exo.vpn.app
📣
کانال رسمی:
@exovpn_dl</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/128000" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127999">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
اختلال گسترده در سامانه‌های جی‌پی‌اس سراسر اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/127999" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127998">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
منابع میگن که جمهوری‌اسلامی قصد داشته حمله موشکی رو شب انجام بده، احتمالاً هم‌زمان با پخش اصلی تلویزیونی، اما اونو چندین بار پس از دریافت پیام‌های مستقیم از ترامپ به تعویق انداخته.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/127998" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127997">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nq3HSaaKMylh_lypJUa9u31aUpbGnVb7AXuRF5_QqrRx-LZtn8Xg4cwbB4XUFx9bb6Yy73uLogkhP2bogndtPl_JjJk0UhsOsI05IbkVLXo31Re9Aym3-CCprlSZZUrzODD6B59IocGWctTxfyCEztqBIhJwt0bhOucQ6zfvZrVry-ND6kUXe8Zx-Q4KCyPgf3QAiCMu6_-PgiW88G1ybSZM40T8c3CvnLe8E3cSew79LBqi-nXTZzo9kRwt-MJYZDm4zZ6axroB3PLb2t-JhNGTVnWGFKNC9Jwkdu7Ol1L0-ion50SEr6-o-f3Ubml3__u-b-VyVKSijpwz1HB5ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
/
ولایتی: فرمان صادر شد؛ لانچرها آماده پرتاب میشوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/127997" target="_blank">📅 23:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127996">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a893cd483.mp4?token=bBA2ZjgFoBzHvo4XjzbZe7Y8ZGVVM161oZc1vJX_jfA-i_OIFP245d1JjaErtx-hQ_5Ys93F3CP6HzLIeGTYpX3HYGzoB-K1B7L914k2fmq81krDg6Qbkb8eMgnuASgrs1Pbwow-mZHZnH0-rlIxa3tWToPH6gIZWXkzPIDneMrEK1lWtj05ATRoK3SIFspWOXUl9VyRUwB6ugG6OT8eLK6onYuq-ht7XcjSTGurkVXB8nBJcWRuNwG7nY0DmFvTL5-Tq2292IzGcPFjHCr0X7gtDOmSo0FFQahkLICEtIDlk4Gof7-G3v7cyPE3lXrZ3QpDRIiPxV04vMGxlpjBQSNDZZbCYK0zBkHDyMnh59_ZDTj-C1T3IRmslTFRgB0JGVXBpZsWk3oaV6Z4IUPuJxVeUZPe1edRJ-5qJZAD-h7eqJQV1PfDP6VIZMq9wAKzHB5jSh25mhxHPmBJ4PyjQn-M5-KzaMYaBW_l39BABdLQBQt7xjszTwzK5zi8GkrDaM7f7j6KUYyoeu3CwVJ8CX1NqFVSmPab00VaUzdNsSK6DyZj4ZZCh9BFDfWBcRbBSRum0rl4CzBwLXfRJLQTIoGm6ufm2wXrSSBeIPHx3viBxMmLQrXmLYL93mU5NwtwXQiZ0t2yOQJyBEv2jVxZL_mp00BbEL62cU-6WfnlRQk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a893cd483.mp4?token=bBA2ZjgFoBzHvo4XjzbZe7Y8ZGVVM161oZc1vJX_jfA-i_OIFP245d1JjaErtx-hQ_5Ys93F3CP6HzLIeGTYpX3HYGzoB-K1B7L914k2fmq81krDg6Qbkb8eMgnuASgrs1Pbwow-mZHZnH0-rlIxa3tWToPH6gIZWXkzPIDneMrEK1lWtj05ATRoK3SIFspWOXUl9VyRUwB6ugG6OT8eLK6onYuq-ht7XcjSTGurkVXB8nBJcWRuNwG7nY0DmFvTL5-Tq2292IzGcPFjHCr0X7gtDOmSo0FFQahkLICEtIDlk4Gof7-G3v7cyPE3lXrZ3QpDRIiPxV04vMGxlpjBQSNDZZbCYK0zBkHDyMnh59_ZDTj-C1T3IRmslTFRgB0JGVXBpZsWk3oaV6Z4IUPuJxVeUZPe1edRJ-5qJZAD-h7eqJQV1PfDP6VIZMq9wAKzHB5jSh25mhxHPmBJ4PyjQn-M5-KzaMYaBW_l39BABdLQBQt7xjszTwzK5zi8GkrDaM7f7j6KUYyoeu3CwVJ8CX1NqFVSmPab00VaUzdNsSK6DyZj4ZZCh9BFDfWBcRbBSRum0rl4CzBwLXfRJLQTIoGm6ufm2wXrSSBeIPHx3viBxMmLQrXmLYL93mU5NwtwXQiZ0t2yOQJyBEv2jVxZL_mp00BbEL62cU-6WfnlRQk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چرا چپ ها از ‎شاه متنفر هستند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/127996" target="_blank">📅 23:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127995">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سه ساعت از زمانی که ترامپ گفت توافق ظرف دو ساعت دیگه انجام می‌شه گذشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/127995" target="_blank">📅 23:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127994">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سه انفجار مهیب در شهرک الطیری در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/127994" target="_blank">📅 23:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127993">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وای نت: ممکن است ترامپ در حال آماده‌سازی برای برداشتن فوری محاصره دریایی آمریکا بر بنادر ایران باشد تا از هرگونه حمله ایرانی به اسرائیل جلوگیری کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/127993" target="_blank">📅 23:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127992">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMuonh0ITgXUKRw-SfNubdcJUGytC69wHSFHg2oswTaLDQSeOENWvNLBlcf0cCnJxGQoCrNl3wzqnPssYlVF9a7DBr_-C-iIBJiIVVP1LJdWMwXFSr8EVUGRNWBiH07We9AaGWg1iW3q6hOYPEiBP-gCmURzHy_IP8TZ8p5XKu4abRAw-Fkri-kOdOvQsU1ES3ECGfKy0Q08PcCetKxrtfyJcWBi2mrl-4JyylQ4oyldXksVaX0a9iYmzNHx9Ln7QX3EmM-8eWbTiR8sSmttWIefq7a7y_sOIIeT2p2nW9UjWJ2m4OEofgwBYTEZ9hoR3WRbY99eOwJff3lEs0T7-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه
وزارت امور خارجه درباره تداوم حملات اسرائیل در حمله به ضاحیه بیروت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/127992" target="_blank">📅 23:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127990">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fQZLKLoVuBYKMpauxS6KZ4bca71KjB3reyT7OMLZpijdAN1eh8Eas4-S141qDrR6tSn1i_pQSd3KsI1pyHmNGDJjUTVwArOIYG_IbmSGrDVahpLZomaTTCa-WGDWMwIxplMT2gdSTh2_qBUimuk5mHq63ZGtoooNCv64HslhImcS6SpsgTrZikjTK4df347JE1CGzWzJBrnEONedKzXPb9sC2DUkwH7CJZhHjig5Iq1OZxdy27pOhqHtRlw0tgRS66K69gFC_3m0w3kaIoS19uomN3sskfWNdwrrLxVMMRlN8dfHeXn4lgpEV9BRlt1W04MdZbGnLyPSoroXIfVijQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bm-f4cKepB0ybtBlM2C7jgLPTBy-bHscesG3p8iY0b-zDK6ko3QPgGZ6D1ZVnakDTstSmg66odEnDLDw0ccasq5YmTMn6geswwcKeh-JAJSgE3NTg18sp1IREMjkv2V5RTr8N_PyJYG6AGeKypKH8qK1iQTEu-vA0X7s-2GYpdWI3PpmOgDt-2_TYghZvo-cT6lZDOd8ecrKiPKFOFAvJ6mIUMj-ERapi-bunBF-lxxThttr2iGBFRZhqh1V6OrlxIOKFtSJuJsymUGPF5CVi8Xw-EPfWJZV39iJHVsM2AEVBPhKQ_s8662azz0m7v1UX98nIIqhCfQAw01-Kd9w-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
صحنه‌های باورنکردنی از پالایشگاه نووکویبیشف در منطقه سامارا روسیه از دید یک پهپاد FP-1 اوکراینی در جریان حمله در ۱۰ ژوئن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/127990" target="_blank">📅 23:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127989">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjdFUsIbFqFOFY1ZlEQB3Jt-R8qEeSZK78q_ThB4y8oOJt7OE_2fChu5urGGgV9WwugHHpNm2McndgAbJMwQmhEUolwhWDXkorjpS08BMuPWP_dVLSQjsvzbAfKuZ64wiCxpCma7qLI0f4NGdahuWQX3WVBpJmJtBMcyydiC0CGNlTAnfep4Et56Y-3Fjm03qx-LMW8_cCC40fgX5k0TDDwM6wIOnm4Vq0gV3AVQmUtc47T2M3jMNvdPlgQweTJzt2xtuL1LCd054r7zdoCA2jLyrWWWCe_oEfQP_Lt8IF5-Ta-WWMnAFZ9niqrDsZtQvD2z2poJSRPkMd8wVGFENw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق تصوير فلايت رادار، به دلیل احتمال پاسخ تلاویو ،هواپيماهاى مسافربرى از فرودگاه هاى تهران نقل مكان شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/127989" target="_blank">📅 23:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127988">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سخنگوی سازمان هواپیمایی کشور: هیچ نوتام جدیدی درباره محدودیت‌های پروازی در فضای هوایی کشور صادر نشده و امشب اصلا پروازی برنامه‌ریزی نشده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/127988" target="_blank">📅 23:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127987">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
راشاتودی: ورود اضطراری «جی دی ونس» به کاخ سفید همزمان با اوج‌گیری تنش‌ها در منطقه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/127987" target="_blank">📅 23:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127986">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
کابینه اسرائیل: اگر ایران حمله کند، ما نیز حمله خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/127986" target="_blank">📅 23:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127985">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbab1c8b8.mp4?token=hAbpUIpSbycYSB-m8hqX0HWzsfY0gp86csvq2uZPjBQ3HVFBBUIGWU3oV6sQrex3WbALuhS64H15qkTBn0oD8mkzN4MjhBVekHNm1H13xBQZLmmYaF5g44qYMCE_X8oIfJOB9tR7-EnrFqDWLJI0gxxUR3ugLTa5JMNZ4Hlqp0T12cT9O3lgj8dqXAMFJAbltZGZrvVVPV8ZX9hIQY2xhqc68S3IOKgguVM_Soi1szjzgCoSMvD8RmL40QJMY2on_mOCAOQGhC9f9U1PW0OvYfxSoNUrfkPLcX6IwVOdWXVvQozcY-JwBJAUU2u34MCC13uwJNL7cx0nTVpzB26uAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbab1c8b8.mp4?token=hAbpUIpSbycYSB-m8hqX0HWzsfY0gp86csvq2uZPjBQ3HVFBBUIGWU3oV6sQrex3WbALuhS64H15qkTBn0oD8mkzN4MjhBVekHNm1H13xBQZLmmYaF5g44qYMCE_X8oIfJOB9tR7-EnrFqDWLJI0gxxUR3ugLTa5JMNZ4Hlqp0T12cT9O3lgj8dqXAMFJAbltZGZrvVVPV8ZX9hIQY2xhqc68S3IOKgguVM_Soi1szjzgCoSMvD8RmL40QJMY2on_mOCAOQGhC9f9U1PW0OvYfxSoNUrfkPLcX6IwVOdWXVvQozcY-JwBJAUU2u34MCC13uwJNL7cx0nTVpzB26uAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
ترامپ نسبت به کاندیداتوری من برای ریاست‌جمهوری سال ۲۰۲۸ نظر مثبت یا منفی ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/127985" target="_blank">📅 22:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127984">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
مخابرات: تماس های تلفن ثابت رو از امروز برای مردم رایگان کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/127984" target="_blank">📅 22:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127983">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری/مخبر عضو مجمع تشخیص مصلحت: در دفاع از لبنان، با هیچ‌کس خوش‌وبش نداریم و درسی پشیمان‌کننده به متجاوزان خواهیم داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/127983" target="_blank">📅 22:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127982">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
تسنیم: لغو پروازهای غرب کشور تا اطلاع ثانوی
🔴
پروازهای فرودگاه‌های غرب کشور تا اطلاع ثانوی لغو شده است. این تصمیم در پی شرایط موجود اتخاذ شده است
🔴
پیگیری‌ها نشان می‌دهد تاکنون نوتام (اطلاعیه هوانوردی) رسمی در این خصوص صادر نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/127982" target="_blank">📅 22:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127981">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
هاآرتص: نتانیاهو به ترامپ
نه
گفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/127981" target="_blank">📅 22:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127980">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFjvpphii4keeirmuKwZShicVCX3fohBjw35pYhQDGf1V_uMBokm0PzSXhWdzvqB1ONyq5wLekZnHgg1mEkZ6z1jZBxeB4-uv-4h0ynSRsujRfjz4Qt0YUYxfs6jZcNSb7sUgMoNHNu4Rwo1TaqDgmJQ2fZz-o-OmWxAb07RcV_yBEPbt68WuJlZCyFh_Gfa7AKwFxGGfbsAoDq2_JuvzStKxxY4bK8lCD08IGau5Kz7aWd-EZNpzCXLPYjouYPTBYLxSFieuaGNfYYg84wmDkU9TQ6ALmX5ps_1NQetoX0YBRJ1TnyB1UuvuqL3Z0ppaniyiEXYAYjH0HBPjNp46g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: هرگز نمی‌توانند هیچ بخشی از ارکان مقاومت را تک‌وتنها گیر بیاورند
🔴
مجاهدت‌های رزمندگان لبنان و دیپلماسی مقتدرانه جمهوری اسلامی ایران حاکمیت و تمامیت ارضی لبنان عزیز را تضمین می‌کند و بساط دیوانه‌بازی و جنگ‌افروزی رژیم اسرائیل را برهم خواهد زد، بچرخ تا بچرخیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/127980" target="_blank">📅 22:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127979">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
طبق اخبار رسانه ایی که درحال پخش است، بنظر می‌رسد ایران و اسرائیل درخواست خویشتن‌داری از جانب آمریکا را رد کرده و آماده درگیری احتمالی می‌شوند. باید منتظر ماند و دید که چه خواهد شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/127979" target="_blank">📅 22:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127978">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
یمن: نتانیاهو بدون چراغ سبز آمریکا، دست به حماقت نمی‌زند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/127978" target="_blank">📅 22:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127977">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJCAZDALVGAtAAYDIIBZMcWTG4EKlZdICEiKRci6WADOHtlS1zLp4zm-lUA4sidJgO2zkGDwe2XMm_V8QSSR4lc7qM8D22bwkB0DF_WrYGneFNwdXrqyTerHr63V5f24YUflSk7iT4RkmMzs7ahOriyV73o9cJvFkzu4rD98YlUZ9KQNmkguQo2umdJgswgAb3jQ3PB4y_UnR4q6sO2Yl6qOdmT3DvN5b9POlY3HBioVsWS4O2_HZ_DjWPSGTV3Ybox1Gg25DB6skHpuO7EKHeFjRDAryRPNFpvkrHueHtpP0iSFnMXhHK7Ta0o9fadUGEhnfoLefmIkXPM6tQPlrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به نظر فضای هوایی ایران بسته شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/127977" target="_blank">📅 21:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127976">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ از نخست‌وزیر اسرائیل نتانیاهو خواسته است که آتش‌بس در لبنان را اعلام کند و شروع به عقب‌نشینی نیروهای ارتش اسرائیل نماید، اما نتانیاهو هر دو درخواست را رد کرده است، طبق گزارش وای نت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/127976" target="_blank">📅 21:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127975">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
یک منبع غربی به کانال ۱۲ اسرائیل گفت که ایران هنوز در حال بررسی پیشنهاد رئیس‌جمهور ترامپ است که شامل پول برای عدم پاسخ به حمله اسرائیل در بیروت می‌باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/127975" target="_blank">📅 21:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127974">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
کانال ۱۲ عبری:ایران درخواست ترامپ را رد کرد و تأکید کرد: به بمباران بیروت پاسخ خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/127974" target="_blank">📅 21:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127973">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وزیر علوم: از 13 تا 20 تیرماه هیچ آزمونی در کشور برگزار نمی‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/127973" target="_blank">📅 21:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127972">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
فوری / یدیعوت آحارونوت: ایران خبر درخواست ترامپ برای عدم حمله به اسرائیل در ازای مزایا در توافق را رد کرده و گفته است که به اسرائیل پاسخ خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/127972" target="_blank">📅 21:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127971">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
یارون آبراهام خبرنگار اسرائیلی: ارزیابی اسرائیل این است که ترامپ به زودی امتیازی به ایران خواهد داد، در ازای عدم انتقام‌گیری ایران بابت حمله اسرائیل به ضاحیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/127971" target="_blank">📅 21:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127970">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ارتش فرانسه: ناو شارل دوگل در خاورمیانه می‌ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/127970" target="_blank">📅 21:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127969">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59cf18c21.mp4?token=k3-1wcpM3nbOPJ9YYocATqeMVnOtFBZjAoLkHh-M3WeNffWabFKg10ZnAxXd_EhwCFjtrghtd-RVVtIueaTb8Ck2nda9bN-ePFxihOM1OkuvPua-3Pg5-mgraZPP0u63k0IUOsrW2JilompawzYEs-w_YECzdf7B_e6jk7w8p6tzIyBmVDmOBByd4gVOTl5LfHsh7S8r-U0YTwVjdFU84P8GarGLUv4tdx61IQ8X7T1oaMPT-xSc12UahywxjAwGWmEnv1ljDtFB-iooNCwaAzDGFjD2VF5Nm3epNgK13VGjtIMyaQa1qG_IP0yYZLcROvLkfa2cYswAVyOK3BhSRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59cf18c21.mp4?token=k3-1wcpM3nbOPJ9YYocATqeMVnOtFBZjAoLkHh-M3WeNffWabFKg10ZnAxXd_EhwCFjtrghtd-RVVtIueaTb8Ck2nda9bN-ePFxihOM1OkuvPua-3Pg5-mgraZPP0u63k0IUOsrW2JilompawzYEs-w_YECzdf7B_e6jk7w8p6tzIyBmVDmOBByd4gVOTl5LfHsh7S8r-U0YTwVjdFU84P8GarGLUv4tdx61IQ8X7T1oaMPT-xSc12UahywxjAwGWmEnv1ljDtFB-iooNCwaAzDGFjD2VF5Nm3epNgK13VGjtIMyaQa1qG_IP0yYZLcROvLkfa2cYswAVyOK3BhSRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درخواست اعدام عراقچی توسط تجمع کنندگان تندرو:
🔴
عراقچی بی غیرت اعدام باید گردد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/127969" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127968">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فووری/ دبیر شورای‌ عالی امنیت ملی:
پاسخ ایران به اسرائیل در راه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/127968" target="_blank">📅 21:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127967">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سنتکام : مسیر ۱۴۲ تا کشتی تجاری که تغییر دادیم؛ ۹ تا کشتی که همکاری نکردن رو متوقف یا از کار انداختیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/127967" target="_blank">📅 21:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127966">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
کانال ۱۲عبری: مقامات اسرائیلی ارزیابی می‌کنند که  ترامپ به زودی پیشنهادی به ایران ارائه خواهد داد تا در ازای اجتناب از واکنش به حمله بیروت، امتیازی بدهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/127966" target="_blank">📅 21:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127965">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
طبق گزارشات اختلال هر ۴ بانک که مورد حمله سایبری قرار گرفته بودند، رفع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/127965" target="_blank">📅 20:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127964">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
اسرائیل سطح هشدار را افزایش داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/127964" target="_blank">📅 20:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127963">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
دو سرباز ارتش اسرائیل در جنوب لبنان بر اثر آتش حزب‌الله زخمی شدند — یکی با جراحات متوسط و دیگری با جراحات خفیف — گزارش کانال ۱۴
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/127963" target="_blank">📅 20:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127962">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سخنگوی فدراسیون فوتبال: روادید تیم ملی ایران در آمریکا ساعتی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/127962" target="_blank">📅 20:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127961">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
لارنس نورمن خبرنگار وال استریت ژورنال: در عرض دو هفته، ترامپ از این موضع که «لبنان از موضوع ایران جداست» به این موضع رسیده که «لبنان مرتبط است اما اسرائیل حق پاسخگویی دارد» و بعد به این موضع که «لبنان مرتبط است ولی من فکر نمی‌کنم اسرائیل حق پاسخگویی داشته باشد چون باید توافق را منعقد کنیم»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/127961" target="_blank">📅 20:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127960">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbvfarZulYnMP-sf8cFvf_oRGC00041o0RBWZinC11BKFGCT0AAdbMEqj32EnE3ChVd5ABsdGk2TlKgaR9Nl_2aA9r55a9p6XtMxm1AhCza-kUctbsGTvymkoqdnMj7EyY1cxmZD4fLZ5Y22MUwJi_Ss3nUPMMJ6NN_WfZ4u8xKN2bFdJ6UCUsf9OEoVHaoVrEmqXTHE3OgzUBJVzJJ8eFVySeQuP2Fg7zx05xrZpdA7OgEph4APZXOng3c9LDgJmvj_MJmjvhoQr4cAvbLaeJSZmV29KHhxgkmDS4Gdpo3PHY6Ueumrm2xjPC8RXjKENPUqkCxZipfvAQRvmocWaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خضریان، نماینده مجلس: ارتباط واتساپی عراقچی با ویتکاف باید کاملاً قطع شود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/127960" target="_blank">📅 20:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127959">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فوری / الحدث : هئیت قطری هم اکنون به سمت اسلام آباد در حرکت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/127959" target="_blank">📅 20:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127958">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سفیر امریکا در سازمان ملل،مایک والتز: ایرانی‌ها مذاکره‌کنندگانی فوق‌العاده سرسخت هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/127958" target="_blank">📅 20:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127957">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سرلشکر عبداللهی: فرزندان ملت در نیروهای مسلح «دست به ماشه» آماده شلیک به قلب دشمن هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/127957" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127956">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ترامپ به اکسیوس: توافق به نفع اسرائیل خواهد بود زیرا مانع از دستیابی ایران به سلاح هسته‌ای می‌شود و این کشور را ملزم به از بین بردن مواد هسته‌ای می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/127956" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127955">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKpV8G300tig1RQQD6VpU0hFjokkPf412CtJNb7k1t-kAE1f1auFk3rv3BbUdgKLzTV_Y8IbKod46HGF3y5HGomutB62EglvazTzfX7EeghOpDu0hwB-rzciSRTMmmmHNkgRmH5Cie-9jc80Pd5mIMyXgSlqnz07RQMafmDC3MqzDu7M48H6447pGA6IamrTfhRpnUxSFOF6NUtRcUDh8QnsEx4nM0oNKvch79jy3zyaWqPTlSlAzMhiJnTisOlEyLfRSyREhomxVK_ScIfy7BD4DpuRFKyA6gukWagm89CXV8uMpewVwwxu4qBTa-IaVi9cIPKLwGdlZa3dX7Cf_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/رئیس کمیسیون امنیت ملی مجلس: پاسخ به حمله امروز اسرائیل توسط جبهه مقاومت قطعی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/127955" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127954">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZgNLidj0XwMaYxF8CCrtPzLWNI8vARocozmggnB3bCfKhcEuUlqgHPciwF8ZaxziIheGO1NXDYQ0OLcEzAFaQA_GaLxA_HM1kXjaNdz8TWPreyhTFcKYPyeJbNb2cTRGTb9M2R7eRkQEsa6jijtDFZej6pVqFP_d_8e8vLvqb0zBwT7iSTn6Ge6rM17kbm4tl039N9KdFdq5udCNN7JMu9TnGGwoTH4ifOikgGVXxMOMj62bvfprd9yrHC83FuGUP_CHFinxy2_cPoZg-qYr8SyknH9Dov4KY21i4MVTriBKmwTaHHKqfvvv3w9YsaZDNqbfcu0u9MRxefOFeXMXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر امنیت داخلی اسرائیل، بن گویر :
آقای نخست‌وزیر، قوی باش و نترس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/127954" target="_blank">📅 20:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127953">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: طبق برآورد ارتش، ایران به حمله در ضاحیه بیروت پاسخ نخواهد داد.دو جنگنده چهار بمب دقیق را در حمله به ضاحیه رها کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/127953" target="_blank">📅 20:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127951">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
فوری / ترامپ به فاکس نیوز:  اگر توافق امشب امضا شود، فوراً دستور لغو محاصره دریایی ایران را خواهم داد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/127951" target="_blank">📅 20:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127950">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
فوری / ترامپ به فاکس نیوز:
اگر توافق امشب امضا شود، فوراً دستور لغو محاصره دریایی ایران را خواهم داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/127950" target="_blank">📅 20:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127949">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ترامپ درمورد حمله اسرائیل به بیروت: واقعا من را عصبانی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/127949" target="_blank">📅 19:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127948">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
پزشکیان: من پیش‌تر هم گفته‌ام و امروز مجدداً تأکید می‌کنم که متأسفم کشورهای همسایه در معرض پیامدهای اقدامات نظامی قرار گرفته‌اند.
🔴
البته عملیات ما به پایگاه‌های آمریکا در خاک این کشورها هدف قرار داده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/127948" target="_blank">📅 19:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127947">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ترامپ می‌گوید از ایران خواهد خواست که در پی حملات اسرائیل به لبنان، با حملات موشکی پاسخ ندهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/127947" target="_blank">📅 19:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127946">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ پس از حمله به لبنان با نتانیاهو تماس گرفت و به او گفت: «داری چیکار می‌کنی؟!»
🔴
ترامپ به نتانیاهو گفت که هیچ حمله دیگری به لبنان انجام ندهد و هشدار داد که این حملات می‌تواند توافق را به خطر بیندازد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/127946" target="_blank">📅 19:46 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
