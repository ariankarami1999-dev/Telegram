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
<img src="https://cdn4.telesco.pe/file/U7qvtq72NWbF3y0_-ZK86TGkaJa0r0jGvHfUpRDvlKwJ_7PCf6nBuwVaOkyDPOl77B7Xdvror99B8W0BummUJVxpgwKMoMzZt5g7Y3zHf_MspIdZXxnM7iqXbCyZ01D8jRHjOVpdj29mSQHn5h9UNYEXzWuKd485g5F4ZQCOXtCTVjBrznmJ0ciJcCiT36aSpE3QYEFTGZsBnnkvPaPr6_JtCDptZZGZBJzHzIVihMAluzuIuPd6XDhI5gYC6y23C5t1bU077zL1CYstXH_T0eBiEKNjxw695y6CC4IDBSs9dp0vPkzIVzPLf3WoiO4soPEFN057piWRWF4gQZftmA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 958K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 14:14:35</div>
<hr>

<div class="tg-post" id="msg-129350">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
منابع پاکستانی: سوئیس ظرف دو روز آینده میزبان مذاکرات ایران و آمریکا خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/alonews/129350" target="_blank">📅 14:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129349">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ظاهرا دیشب دوباره اسرائیل تو جنوب لبنان تلفات داده و حداقل ۱۰ نظامی زخمی و یک نفر کشته شده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/129349" target="_blank">📅 13:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129348">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
نیویورک تایمز:  مقامات غربی از نتانیاهو خواسته‌اند حملات به لبنان را متوقف کند تا ایران نتواند خروج از مذاکرات را توجیه کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/129348" target="_blank">📅 13:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129347">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
منابع العربیه: وزیر کشور پاکستان پیام‌هایی دربارهٔ مذاکرات مرتبط با لبنان را به تهران منتقل خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/129347" target="_blank">📅 13:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129346">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
روزنامه واشنگتن پست با استناد به داده‌های شرکت تحلیل اطلاعاتی کپلر گزارش داد که دست‌کم ۲۵ فروند کشتی پس از امضای تفاهمنامه حل و فصل بین آمریکا و ایران، از تنگه هرمز عبور کرده‌اند.
🔴
طبق گزارش این روزنامه، طی پنج روز گذشته حدود ۱۸ میلیون بشکه نفت از بنادر و اسکله‌های ایران خارج شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/129346" target="_blank">📅 13:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129345">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از یک مقام نظامی اسرائیلی: حزب‌الله لبنان شب گذشته بیش از ۵۰ موشک به سمت نیروهای اسرائیلی در جنوب لبنان شلیک کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/129345" target="_blank">📅 13:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129344">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ان‌بی‌سی به نقل از آژانس اطلاعات آمریکا: حملات اسرائیل در لبنان ممکن است توافق صلح بین واشنگتن و تهران را به خطر بیندازد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/129344" target="_blank">📅 13:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129343">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ED17ggJ2Anu_5nDHYpKFHjMn-3l0F1VtAj2bQ9ChVUZpKL4mL803IB2uuIoQg5ox2-Cr8Vrp0XO0OXssoxx4s_Zs2hD3FAEq9CRU5oO6qVJPWJQsAauIA0HCPAGBgqnOsk8at-2SdNsIvg4K2Lep-MYjap-nuMwtlSBrZ-lXpdMnqBn-EWeFHtCKeiQ2vps4KzAX3qRMqFTmcmjvoyUY1B-iW_OSPD25pDTPwTpQaN_pi3E2vFDXPa3bHT1fARbANu3LpIda9z29DWI7l4f5lXS7ZFqROijrx6raiLpi0O0-4wo5x1mNDx8Cw1Hca2ZdZHO_lwOUM980eHpI6Pb2Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتقاد تند حمید رسایی به بسته بودن مجلس شورای اسلامی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/129343" target="_blank">📅 12:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129341">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سخنگوی وزارت کشور: اینکه بگوییم صفر تا صد تورم و گرانی‌ها متوجه دولت است، دقیق نیست؛ برخی افزایش قیمت‌ها تبعات شرایط اقتصادی کشور و جنگ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/129341" target="_blank">📅 12:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129340">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
رئیس سازمان سنجش: کنکور سراسری در ۲۹ و ۳۰ مردادماه برگزار می‌شود و هیچ تغییری در زمان آن وجود ندارد.
🔴
نتایج نهایی کنکور در ٢ سناریو اعلام می‌شود: یا نیمه اول آذرماه بر اساس مصوبه فعلی و يا در نیمه اول آبان ماه اعلام می‌شود.
🔴
ايجاد سهميه براى خسارت ديده‌های جنگ انجام خواهد شد و نتیجه پس از جمع‌بندی به شورای عالی انقلاب فرهنگی ارائه خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/129340" target="_blank">📅 12:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129339">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ان‌بی‌سی به نقل از آژانس اطلاعات آمریکا: حملات اسرائیل در لبنان ممکن است توافق صلح بین واشنگتن و تهران را به خطر بیندازد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/129339" target="_blank">📅 12:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129338">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
پزشکیان: حل مسائل مردم مهم‌ترین راهبرد پیشگیری از آسیب‌های اجتماعی است
🔴
شایسته نظام اسلامی نیست که مسائل و مشکلات معیشتی، اجتماعی و درمانی افراد از نگاه مسئولان پنهان بماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/129338" target="_blank">📅 12:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129337">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
روزنامه‌نگار نیویورک‌تایمز: کانال ۱۴ اسرائیل که بلندگوی رسانه‌ای نتانیاهو است، از زشت‌ترین الفاظ برای ترامپ استفاده می‌کند
🔴
قبلا رویکرد این کانال نسبت به ترامپ چاپلوسانه بود اما با انتشار خبر توافق با ایران همه چیز یک‌شبه دگرگون شد
🔴
این شبکه اکنون، او را «دونالد حسین ترامپ» می‌نامد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/129337" target="_blank">📅 12:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129336">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gemJZnXYK0FoeOwwK-LXX8tizw48aFgVIbVFYuBrtM6LF_PIpFaWf-GUdIkntdmKdKJ7zm0cmvlnF-8-Opqo6LR3lqLnrKmLPqSdp8kIbH7EDREGJvFU35I4dJfOBR8i-WwEEcDoNAiOG0TINAjiHgLAVfpU1_w8QmNPCJzcbwcY_7NT8WQ11vySw5wQxVwfreppoF8jpdsrOLx5RsV7n4u-EkgNTNAEwAnFr2_oWmv8aZ3ASZipglWkCIYFqWCjXjV16l2H4XgUOmmDy-AH_pNnjCOsLY-7bfi72Ty_JisvGD2XoJr2gUxXup8HBUfNvuMCslbVD3VRwbHS0qYJaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر کشور پاکستان وارد مشهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/129336" target="_blank">📅 12:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129335">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
اینترنشنال: دانش آموزا قیام کردن
😐
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/129335" target="_blank">📅 12:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129334">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1e6e4d20.mp4?token=Q7_fwmF-i4bnF-s4OFPZvPtx_vI0dHai54Jyekn-aXOvYe_dDxGg6ee6IGv36qbJFgG5DNY-c_WPYUoJzhZAbBxjlJIcaNpttXl12K0qDtqmcpZ7g2Bk--vTLBM_cFNWAdVx6d_5UDGexLVb6nOGPeb5voHzC6aFGOMLkmcxxltKie7Qe9tuxOKm7PHfd1dqmRkYzToM9qWqCoE4BW3IgDrlzzRnFlj-MI-Rwqdkb9Vy5bTcKqWJNlukdxvcHV64lq1jZou0aqRaLp5M1bOWIEyh5ajlxNYUh78l3yA6fZILmIpRFzQr14p3EDd8T4bPGD4aXT5ueip9wBLdnmyW5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1e6e4d20.mp4?token=Q7_fwmF-i4bnF-s4OFPZvPtx_vI0dHai54Jyekn-aXOvYe_dDxGg6ee6IGv36qbJFgG5DNY-c_WPYUoJzhZAbBxjlJIcaNpttXl12K0qDtqmcpZ7g2Bk--vTLBM_cFNWAdVx6d_5UDGexLVb6nOGPeb5voHzC6aFGOMLkmcxxltKie7Qe9tuxOKm7PHfd1dqmRkYzToM9qWqCoE4BW3IgDrlzzRnFlj-MI-Rwqdkb9Vy5bTcKqWJNlukdxvcHV64lq1jZou0aqRaLp5M1bOWIEyh5ajlxNYUh78l3yA6fZILmIpRFzQr14p3EDd8T4bPGD4aXT5ueip9wBLdnmyW5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تجمع دانش آموزان شیراز در اعتراض به برنامه فشرده امتحانات نهایی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/129334" target="_blank">📅 12:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129333">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
تصویری از تجمع دانش‌آموزان
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/129333" target="_blank">📅 12:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129328">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
یکی نوشته بود بجای کافه رفتن خب درس میخوندید
نظرتون؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/129328" target="_blank">📅 12:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129327">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhBhQYuvfKh9ffcaclmizwv82wxQWHitFMUbXIsdbvSVWUK0AJRUFjDqekQhQ-g4oSd9qNY7mY0c11z5Xzq9fdrf-zp7UPHMwn52VYAb1tcWhi-cObrwRVRwuU3dkCUlE3NWfzE-YHzZ5sp0UQ7aD6GKx6phdp0rCjqbQrVWvyZCBARsRZF0awjWCMvSuLemmzwIf4hlOwGWpzhovCcnKgaW786JyZqoKy0RQV5DDER5dDJLiZZBpAVqPXfi0EJlgW_Y1MpwHrxFv3NiunbK_PXVTmwtJTNjSxCm664KnqAPjp3mWLkKD3eyYlNLL13UUCq64C_-cyMszBmqLUZDOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از تجمع دانش‌آموزان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/129327" target="_blank">📅 12:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129322">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eda31ed24.mp4?token=e3Wc-cZivxFW3iFoEo2nzR6hvNIXFk54VbIPb45JtIR3pd78GO15QZP69TneejJyQZxSoafZcHdBx0TpfVg1aSGS4Bf7JXotMYexDrTrL1nFP1ozJ_Fejts8noLNjxXjQ6Mx3MvcwdFoc4acTkmFFyizb3JhSB2i9nPgUGmwsuaTjvvDCigjXPDLgS8yStYPY_uXEvjMcFsjpibSSehskV6nIkMjDxsz9u8hK5yrzT6PHKq-WaTN__sBHai86YoXLQP89qXC87k4Fq6QJUf8afyhEhyeBbu1MUC2m-Go6-q_vSjt93wD3p-PKAZC4DuxUVUJ4hvH9Szv-Rn-8hvjiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eda31ed24.mp4?token=e3Wc-cZivxFW3iFoEo2nzR6hvNIXFk54VbIPb45JtIR3pd78GO15QZP69TneejJyQZxSoafZcHdBx0TpfVg1aSGS4Bf7JXotMYexDrTrL1nFP1ozJ_Fejts8noLNjxXjQ6Mx3MvcwdFoc4acTkmFFyizb3JhSB2i9nPgUGmwsuaTjvvDCigjXPDLgS8yStYPY_uXEvjMcFsjpibSSehskV6nIkMjDxsz9u8hK5yrzT6PHKq-WaTN__sBHai86YoXLQP89qXC87k4Fq6QJUf8afyhEhyeBbu1MUC2m-Go6-q_vSjt93wD3p-PKAZC4DuxUVUJ4hvH9Szv-Rn-8hvjiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از تجمع دانش آموزان یازدهمی و دوازدهمی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/129322" target="_blank">📅 12:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129321">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
فوری / خبرنگار الحدث: یک هیئت عالیرتبه آمریکایی وارد سوئیس شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/129321" target="_blank">📅 12:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129313">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GjZbXvwqMqtRd6YR7N-dQQXBWsoFY8vHZLQwqbHtIa8BXIX-Yu-mNyCH8hVqmqSDcE4iIBg3u2ddld8ZHMe8fihsGndytrjjqyebdrjd3RKrl6w0WL_BxizQTk1WV7uYAUQF8ifjd68mzpyGzLBP_AOwD4Xs1qHRW5mR8kOm5To4Dcw-Z-8eqEAWdPIb3KGXeBMHrM_FI_JuEGyogRgGEFuin3rPHFEDvUKxF9r-J6Hfkrku8sMFCYSg-AzTEDBQbuWwOjGzxr3VWtfzrCXjOHtjDrqdz9I0wdcbmqBaRvTr9mtIyMbvUlKbSwfaZMMFDw804W8QfcVBtUKhDrm_1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W7834rQKe0RDLUItCwhiojzwqC9ToERCJuWxhMpCW9hL0jfwgEeZuXPlUHd_DtaTnqS9wKjYkb9RbkJ1EV3Zz4bHpr3qymYsLTk72P1wol42TlIZsxli7lUW8QwwMYyJvg4bfWyBBZnPnR2lj-n9fbb8Pk3dL3u1_6w5GJAjEBAwhPYN7cAksH0rPIUEAnDqidCKDpgS2vb2s8NRFHk_b47xw-lYm5v-DZdQc0PrbFC6bv_3fxLAG3Wdp-LRNOWIdH_88RHXxeZb8hKd0Eqk8EWXUVZhCYaqWPFXrz4UFYf-6dbwHwbzYLhurN5a3vCNaw3mOPbhxCv0B0taW_1EZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D84bb4G1DaYVsx5pDoAi1_6iLfh1YrtMI0Uel-vYLviQFOYkuYqjuHb9QTRl1WjaKTQSpRg_K-YloJvEmb70IysidW6VI--U5348GXRg6sNKkQHX0h-1vBlM7-12yc8csmt8buHymrCOrLjGhqUPhnvF4kWn6hjniJjhZ8wN1B-GpaxXRX4JPXmkDj5-cpQpmxJBSYlvlfwNbgG_sSpmYQatRZHHc_Gzsp5PFPzWIaNVD86MHKwWB092NRhh8JVV52FY__cvdqJCu7XhxMEaEpzf0OrEsvBe82cGv5xWZS7MFSCtEoL2IzOrQn7hgWh3EW-yJNle9vyjzhIwg5E15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ExnvkNoM0uK1tsE2vHxOaZfnOkHQCP5fX77IzzSuyaEMJEusa6bN1AhMNqvZbg4E_YdkgXQhUW2aYL2JGfcBH8gqZykFOsm8iJjn9vS9RtQ7B6F8ufORz_ZMm8PF2wEE47QvZi0P5QSw_I4Wfqy1ripOvKQwltmIgjw088KhCqS2pMq3-JZMCibC9zDCmtpp27ukxP2V1hzin1C0NOvDbiLpa4Pf_3mCgGQZ4tmRTW902w9w_yxosx6y7VoReXytL9Zftphd7uCALrRb1au2yf_HOy4yw4mstGUF7lAfTicSRV-3h_ns6f_G_yee1YPN3c6dUxW9gAhqc2aaJM7PBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lCwpv4QAS4Ioh6Ok4mza_UtiN15j0AprgYk4KNwRJBbj9Td7LjCAKqooGP9G6LiT8bokZaX6VlqGqYmFHHSWpTXnYwF13Zv5rmaXfiS7DoXigvGs8zo-SQsE-pTwysdPIKt_0TeZdaAUXMGqrFTbsR0sjxKPaq0cUS-JRay9jW1zEKYk_kQm4Fe9kXvCzTogSEXco5v9rVfINSZzL9bnWOFmraXQBJaQGvbZa1pTLPsD2NgIckEpFj5DpYx6rKhEtI6BXnMxnbiXCpzPelt3ggBzzB6qt9T68vqb1BffZ0_j5I9wh--EvDGFflY2ErL7JdqaBXAOWPe9y5xsX5F1bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mCpVRBWPu4yI_gIMzlokpA2QAotEWOfdFpwAYJP7VBdtvaVTrSkM3bU_Sk-m8a1b3MPJHiW3i-EDmJdJYZBbLS0PxWXrXbve6UVME8FVdQ3ytV6LVTvGZLAZLRHRcVpZtM2zcR9ebzytNwbCC8MQ7GKghR3s6ziC1DYstlAT1bNUhCI8QNgvZ0DdmB4ITjlG8IIeHBRGZQePSSvNzqWe1c06sV85_5jkUUMWqeqlav8_0JYrs47iDqbvOzvbbzsh9bu2tfdidukL3C4NtWLFRECvUvjHUnksEezcD8Mj-OfW59_szkSpB6NDvhd7QlqX7y7ytU8Tv3bWIahFXwE7lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/axdZf6Cm2iPV3Aob105DXL81ZSi4XuqUKsOEiNoracX77InE7mUcnNxeBmkeSwSWw1Wlc6gTCnLEd2UrpjetvN_WboQ9RHZ0v8N2FCQn78pziHm2_ev2aX5uUrL9ztX5TeiZ6LQ5dLMbZmjlNFEBOHm3c2wzcKs2BTmgRqPOW2OR8pn2NDXWek0V4Z1MONY8469fxuKvZMCkSxa_2uKMII6WTWZXhAFfEC0kWjFtA7AgCq_GhLSoRiDrRcrVAcoZ2NizyIaWCOVP7XrivEdbGfaUWd0Pg5Jf2kU75NjER0PBXWtS82IiJBsxVFuZbl6Qebl0Mf0IH7XVIWXlfgafzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1368546d7.mp4?token=sJcQMme38K_zWmEblRsHtvgxG_NkbRR-GZhwyyoJmXwHSYxecG_wiU7wAVLoqLXBwUG6HXZnnIkyaU8L8tBNQimdpzbMlosJg9QBE9HTL40o9uFYXJt9KaS797jJT_hr5Ge6y-bYX2I3k44T7tnWJBUEWwzAf_2mlxcFK1phCFVV1fc7QbyOdwPn2-wNkE3pFVGb0rhPStDuUtBle_1MrOnsZRK1WwzN9S2MHXvgkhAhiSt54sXbLm_a4ZjSyraqt98IL7SCVRlqE4Le-BrsGHGIm1wS_eXOqze2gonTLIVFCb3bjgVxdX3jY6hjVeBLqzqWuAeFlkKEcVXn7dMogg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1368546d7.mp4?token=sJcQMme38K_zWmEblRsHtvgxG_NkbRR-GZhwyyoJmXwHSYxecG_wiU7wAVLoqLXBwUG6HXZnnIkyaU8L8tBNQimdpzbMlosJg9QBE9HTL40o9uFYXJt9KaS797jJT_hr5Ge6y-bYX2I3k44T7tnWJBUEWwzAf_2mlxcFK1phCFVV1fc7QbyOdwPn2-wNkE3pFVGb0rhPStDuUtBle_1MrOnsZRK1WwzN9S2MHXvgkhAhiSt54sXbLm_a4ZjSyraqt98IL7SCVRlqE4Le-BrsGHGIm1wS_eXOqze2gonTLIVFCb3bjgVxdX3jY6hjVeBLqzqWuAeFlkKEcVXn7dMogg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل بیش از
۱۰۰
هدف، تو جنوب لُبنان رو زد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/129313" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129312">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3530192cd5.mp4?token=kkQ4KyLTjfhCYqoJRN-Xft3GB9hJVHgJoisMQu4k__OOMJzhE3aCzkzD86NPAl24mw1m3RP1OH776ED0r_VEh7c6Sk6l05G7CoxXkF1TbgsOEJGEbzjL8wu8qwR3fOLlHBx8PhSAzk4loYV85RpsMdJpa1F2O_XnZZk3sL746cDsIRYO0F5sqY3anKu6oT5q1bDUAnfrP7RDDbH2Ts9P0XoImWCyfY0BtS0junUjNVEYNmJmCZihGVbKObZPADXnCrf-Fa0zX5fLpI3uIMaKg-0bbV_N2P_3Jfu9fBvY5gWcRSPTPZ0N-RvyU92kUoZFJS-xQdfzQd8IgJ_r_pLNpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3530192cd5.mp4?token=kkQ4KyLTjfhCYqoJRN-Xft3GB9hJVHgJoisMQu4k__OOMJzhE3aCzkzD86NPAl24mw1m3RP1OH776ED0r_VEh7c6Sk6l05G7CoxXkF1TbgsOEJGEbzjL8wu8qwR3fOLlHBx8PhSAzk4loYV85RpsMdJpa1F2O_XnZZk3sL746cDsIRYO0F5sqY3anKu6oT5q1bDUAnfrP7RDDbH2Ts9P0XoImWCyfY0BtS0junUjNVEYNmJmCZihGVbKObZPADXnCrf-Fa0zX5fLpI3uIMaKg-0bbV_N2P_3Jfu9fBvY5gWcRSPTPZ0N-RvyU92kUoZFJS-xQdfzQd8IgJ_r_pLNpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله به شهر نبطیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/129312" target="_blank">📅 11:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129311">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFSmpW3dAp3Y_R4TA3S_DJ36O4D29Q2wr4cbidNgtTYsusroXweE3EMFOnsjdMhlqBJ96aFBlkBVYkTQXevst9phycJKqFCIyYtxwnH-yDJg9IGMlzrWJjGpDdGNg1o5-OSUfa316N-PYqiWanWmNvSW90mdAadSES18oaegeJZITLc0AW8au3KLzJAqwsoppDT6Erjl2IoRndBWT4hO2wXV4l41T3V7okFpLDL8uVE11aPCmvuzlBZueN9MtfeiSXaspdmX6-3uQW7eGdf0SId-fkEHoYKld_2MEEe--G5Ta1_aT4e9JfJ0JxRvInv_eDQtEQ6QSIABDwN6qZsE4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با افزایش ۱۸ برابری حجم آب دریاچه ارومیه، آرتمیا دوباره شکوفا شده و فلامینگوها بار دیگر به این زیست‌بوم بازگشته‌اند
🔴
پیش‌بینی می‌شود امسال بیش از ۶ هزار فلامینگو در دریاچه ارومیه و تالاب‌های اطراف آن فرود بیایند؛ برخی از آنها حتی آشیانه‌سازی و جوجه‌آوری را آغاز کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/129311" target="_blank">📅 11:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129310">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7sp73zrJQijTFSrHng368fsGRKD8K_Jho__IGTJkELCbv9uVg4XkEda3fpazJKZ2-6DPYnaI0WqrVaucmqCTGABRH5rExjkOLTFLn3lJFJYACOXDcpYCh8YnxIAycnFLjEmaEk0paRXCMzSkE1IniPmZlbXQq4ajQMJiuNy_Sr0_vT_GB3lslxqeXXKSpAMQcIARsKaZPiePffZADwhI0mkkDswC0PsbDMAaDzF-ZorA1xM2JCY_qIl8sML627y0loK-3QtQ8Yep3CrkhQLo70peHY0d36v9_0ulCnjB9VorSb2m82fdOv_KOxZkUM45gCpiYrsXQcX9nkVIzzylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم:
قدرت داره از غرب به شرق منتقل میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/129310" target="_blank">📅 11:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129309">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
جک کین، مقام سابق نظامی آمریکا:
احتمالا در نهایت با ایران به توافقی دست پیدا نخواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/129309" target="_blank">📅 11:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129308">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">محرم امسال یه فرق بزرگ داره
امسال حدود ۴۰هزار زینب داریم که داغدار قتل عزیزش است
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/129308" target="_blank">📅 11:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129307">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
دولت عراق به‌طور رسمی مجوز فعالیت استارلینک را صادر کرد تا سرویس اینترنت ماهواره‌ای اسپیس‌ایکس بتواند خدمات خود را در این کشور ارائه دهد
🔴
مقام‌های عراقی این تصمیم را گامی مهم برای توسعه زیرساخت دیجیتال، گسترش اینترنت پرسرعت و پوشش مناطق محروم و دورافتاده عنوان کرده‌اند؛ مناطقی که هنوز دسترسی مناسبی به شبکه‌های ثابت و فیبر نوری ندارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/129307" target="_blank">📅 11:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129305">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
نتانیاهو: ما در حال محکم‌تر کردن در دست گرفتن حماس در غزه هستیم، جایی که بیش از ۶۰ درصد از قلمرو نوار را در اختیار داریم.
🔴
و در لبنان، ما تهدید یک تهاجم زمینی علیه جوامع ما را پس زدیم و توان موشکی حزب‌الله را شکستیم.
🔴
هنوز کار بیشتری برای انجام دادن در هر دو مکان وجود دارد.
🔴
ما باید منافع امنیتی خود را به قاطعیت حفظ کنیم در حالی که ارتباط مهم با دوستان آمریکایی خود را نیز حفظ می‌کنیم.
🔴
ما ادامه خواهیم داد تا مسیر خود را با خرد و قضاوت سالم طی کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/129305" target="_blank">📅 11:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129303">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a4e4cf8f9.mp4?token=Ob0ZQ7FZTx_lsKXJZHb9owauh84bmO2El7-wcLiduGydN9orqaMWh0SolEj0hZTfs2T_fB0qtnFHxRHUoH0jjUFCl3yd1cHjC7B36LAenzVQfG6ef-XYRQE2vRnLcj8oHiFF3vRREXVwILp93M0xh1OOER4dGrdn6ZcMYTYBQtCSg--WYjoE76OMvCLnrGsfZ8PNwqjXCAfBSDDwI34uFZju4TTHEPvxergZ5KM7kN2E4xQbHIBv6dejFeUoc1A-9QbH6Eh07W57mNri4wuYEKCSgIaWL01lh3t90mnHXT6yww_ynqpBBckfNqqeKo8iAguEJ6MOHrK6PVaFr9ueHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a4e4cf8f9.mp4?token=Ob0ZQ7FZTx_lsKXJZHb9owauh84bmO2El7-wcLiduGydN9orqaMWh0SolEj0hZTfs2T_fB0qtnFHxRHUoH0jjUFCl3yd1cHjC7B36LAenzVQfG6ef-XYRQE2vRnLcj8oHiFF3vRREXVwILp93M0xh1OOER4dGrdn6ZcMYTYBQtCSg--WYjoE76OMvCLnrGsfZ8PNwqjXCAfBSDDwI34uFZju4TTHEPvxergZ5KM7kN2E4xQbHIBv6dejFeUoc1A-9QbH6Eh07W57mNri4wuYEKCSgIaWL01lh3t90mnHXT6yww_ynqpBBckfNqqeKo8iAguEJ6MOHrK6PVaFr9ueHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: مسیر ما هزاران سال پیش آغاز شد و با کمک خداوند تا ابد ادامه خواهد یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/129303" target="_blank">📅 11:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129302">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67043be620.mp4?token=D_Pb8PjMbjdLMh6J0oLWReplXAgfvu-LLNRpNCOs5FphhlgW1eAHFjdZS9QjQu7GNeH18tznhyAhBgE8sRQSKzP80ecjwCjq2cQn996Z9X5_PoBQMjwVhXeohzA3EuqH_nOvB1iKLURQNFzgrSb6KbbcXLLRcCpWo_8R3IXqHxTZD7UeDz2hR5hGYK2zjJXaMA8f9yAJ7DbNorpULyQGT8Dbj9PDcubEZbroHdBuZ6ZxF9XDhAyvWbIb8BFCGofKKoGjCc81IElg_hi4gjykqeqfnfpi9tqXqakhi1OXPOLvu3hheLAMTPo1wjRgNOGomgRa_UqsyGnol5VNuykn_IXxsV5p4-ctywRuiH9z37yLKGoI9hGeJnlP8k075xSUJ8eLPAZy5EI1165mDagmWlQ3O2EHuD4Va44y9dfoW3lk4OtN_HN61Pw8Jr59s9x-_j3ao38qSjA1xO6tNaoaffySgkyf1vKpC56bXkkIZ3qiheWWKz0yTDzNZfmnOLZlnrTJwsoLvM1Mgf9tFi45BZ78B91EhBpGk6wU41bH1VEMAYUDSc7NEK4gwL0ZTzYbArpQp_pdAMOw7PkbVs0dCJfdIWWAA-QChkpDnDmOLwoDEMxd-atQ6n1SKMWgNonrOMl2Oet-Hv9Lnu1kEk4HbI9dutq7q0UVG-gL23t7xKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67043be620.mp4?token=D_Pb8PjMbjdLMh6J0oLWReplXAgfvu-LLNRpNCOs5FphhlgW1eAHFjdZS9QjQu7GNeH18tznhyAhBgE8sRQSKzP80ecjwCjq2cQn996Z9X5_PoBQMjwVhXeohzA3EuqH_nOvB1iKLURQNFzgrSb6KbbcXLLRcCpWo_8R3IXqHxTZD7UeDz2hR5hGYK2zjJXaMA8f9yAJ7DbNorpULyQGT8Dbj9PDcubEZbroHdBuZ6ZxF9XDhAyvWbIb8BFCGofKKoGjCc81IElg_hi4gjykqeqfnfpi9tqXqakhi1OXPOLvu3hheLAMTPo1wjRgNOGomgRa_UqsyGnol5VNuykn_IXxsV5p4-ctywRuiH9z37yLKGoI9hGeJnlP8k075xSUJ8eLPAZy5EI1165mDagmWlQ3O2EHuD4Va44y9dfoW3lk4OtN_HN61Pw8Jr59s9x-_j3ao38qSjA1xO6tNaoaffySgkyf1vKpC56bXkkIZ3qiheWWKz0yTDzNZfmnOLZlnrTJwsoLvM1Mgf9tFi45BZ78B91EhBpGk6wU41bH1VEMAYUDSc7NEK4gwL0ZTzYbArpQp_pdAMOw7PkbVs0dCJfdIWWAA-QChkpDnDmOLwoDEMxd-atQ6n1SKMWgNonrOMl2Oet-Hv9Lnu1kEk4HbI9dutq7q0UVG-gL23t7xKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: مردم اسرائیل به خانه بازگشته‌اند و مردم اسرائیل برای همیشه در اینجا خواهند ماند.
🔴
زیرا این سرزمین ماست. متعلق به ماست.
🔴
ما بازگشته‌ایم، به جایی که از آن آمده‌ایم بازگشته‌ایم، به مسیری که پدران ما در آن گام برداشتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/129302" target="_blank">📅 10:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129301">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
خبرگزاری دولت: وزیر کشور پاکستان برای دیدار با مسئولان بلند پایه ایرانی، عازم‌ تهران شد
🔴
او در این سفر «پیش‌برد مذاکرات» را پیگیری خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/129301" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129300">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
رئیس‌جمهور ازبکستان خطاب به پزشکیان: یادداشت تفاهم امضا شده، نمادی روشن از اراده برای تعامل سازنده و احترام متقابل است
🔴
این گام مهم موجب کاهش تشنج در منطقه، ایجاد زیر بنای پیشرفت و گسترش همکاری‌های اقتصادی و بازرگانی خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/129300" target="_blank">📅 10:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129299">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d84fa59c.mp4?token=aCAtpba7dB_2AOCuGIYq0mxBzcRGs5XrKRo6uP7ODePuTWOT0gPg75BKnkbzN2NCu_FgpwNoBqANwdmJn4KwzVlsfgZ4LFKW_hqIMFikJ04JsXHMts-bXjZkSURvpJgaxkWdbEoxJihLrLupCt4l0v8EtpVRkGyIsPcB0juYAWaI5rs0Kq_iHUTLcgvTGYk6QlGv9Rd4lcsavvVHgWc0eGjqpKoLk1TWf6lY5rALuni0GPKQjfnw8aerLSq19LCZcO2vvU7gnpKkd2tXigwOIp3qkJgdSRwbk-Fc-KbZMQhi2jrHyoGVW89KSQ3OhuxjroaiWXJkw3T2JhJ1tKeugg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d84fa59c.mp4?token=aCAtpba7dB_2AOCuGIYq0mxBzcRGs5XrKRo6uP7ODePuTWOT0gPg75BKnkbzN2NCu_FgpwNoBqANwdmJn4KwzVlsfgZ4LFKW_hqIMFikJ04JsXHMts-bXjZkSURvpJgaxkWdbEoxJihLrLupCt4l0v8EtpVRkGyIsPcB0juYAWaI5rs0Kq_iHUTLcgvTGYk6QlGv9Rd4lcsavvVHgWc0eGjqpKoLk1TWf6lY5rALuni0GPKQjfnw8aerLSq19LCZcO2vvU7gnpKkd2tXigwOIp3qkJgdSRwbk-Fc-KbZMQhi2jrHyoGVW89KSQ3OhuxjroaiWXJkw3T2JhJ1tKeugg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس: در سیستم‌های پاکستان و قطر، آن‌ها دقیقاً دارای اصلاحیه اول و آزادی مطبوعات نیستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/129299" target="_blank">📅 10:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129298">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وزیر کشور پاکستان عازم تهران شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129298" target="_blank">📅 10:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129297">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سخنگوی دولت: تفاهم در این مرحله، هنر تبدیل جنگ سخت به نبرد سیاسی و راهبری چالش‌های سخت با مدیریت عقلانی منافع است
🔴
هرجا باب گفت‌وگو گشوده شده، امکان یافتن راه‌حل نیز فراهم آمده
🔴
تفاهم به معنای پایان مسیر نیست؛ بلکه آغاز مرحله‌ای تازه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129297" target="_blank">📅 10:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129296">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ: اوباما تمام پول ما را به مردم بخشید. او صدها میلیارد دلار به ایران بخشید.
🔴
من پولی به ایران نمی‌دهم. من به ایران پولی نمی‌دهم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129296" target="_blank">📅 10:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129295">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f72466c840.mp4?token=WKCOzrDWh8-WoVtXKCP4wTOGX-lTlb8_4S77CETYVhFt9Cwbc6HNBd9hqFPNBc110SW8mup-LDAKHaUl0BCM-vxq5ouzZw-vm9GEigUwjuFNr9p3coxVTJBEBBGjdvJLhGPqLPetf0hJ8nb2HK5r1D_2HniePm7JM9IBI4llaULpChQsL70Y14Si2vwePT35CigG73PTNquGPR3FdjTIYY89gcUrxvi6sdxB3IFr0XqPNSXsIG2sUp3YZEQ6SJQHgq5ZXykgxPCrZmnHdRs4jmTKXeYrqsV32EAZ7YB6TjlSttzVSldUamlqR5ZMwpEKT8OMTia4mFTnOeyMQTzVzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f72466c840.mp4?token=WKCOzrDWh8-WoVtXKCP4wTOGX-lTlb8_4S77CETYVhFt9Cwbc6HNBd9hqFPNBc110SW8mup-LDAKHaUl0BCM-vxq5ouzZw-vm9GEigUwjuFNr9p3coxVTJBEBBGjdvJLhGPqLPetf0hJ8nb2HK5r1D_2HniePm7JM9IBI4llaULpChQsL70Y14Si2vwePT35CigG73PTNquGPR3FdjTIYY89gcUrxvi6sdxB3IFr0XqPNSXsIG2sUp3YZEQ6SJQHgq5ZXykgxPCrZmnHdRs4jmTKXeYrqsV32EAZ7YB6TjlSttzVSldUamlqR5ZMwpEKT8OMTia4mFTnOeyMQTzVzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کشتن قاسم سلیمانی: می‌دانید سلیمانی قصد چه کاری را داشت؟ او می‌خواست پنج پایگاه نظامی ما را منفجر کند.
🔴
من او را یک هفته قبل از آن حمله به دست آوردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129295" target="_blank">📅 10:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129294">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20faee2d60.mp4?token=giVYIAKGSM_-c2U9GBQE24MCpsvEYF33rUWgAmUWZTDzbhcsEJ9BztQQJ3CguIwTpzQGs97BWSaUiIbxKBDQQl7zfGPA_bgBUQiSoj0SVcvfaSx3tYzJTAsoEbfRMlnFwgugaFu3Pp8862b0VKFpi0_aFShfDvVC8q748AYiLp5br45Mwz_095uUVWxnuAffIaeMLkoPYkf7bQR42vRSifp-5PEePuoPrAACTr-Y_JN8IakTrKZwkvJTYineNR6tL0YjxqQNiucX-3P8a7YZS3NlaENgc9oPA0cD9WoB9ehfWL4FZxqDg9TvXgO9sxp7fLEEduJwu-IgwXkixyPz9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20faee2d60.mp4?token=giVYIAKGSM_-c2U9GBQE24MCpsvEYF33rUWgAmUWZTDzbhcsEJ9BztQQJ3CguIwTpzQGs97BWSaUiIbxKBDQQl7zfGPA_bgBUQiSoj0SVcvfaSx3tYzJTAsoEbfRMlnFwgugaFu3Pp8862b0VKFpi0_aFShfDvVC8q748AYiLp5br45Mwz_095uUVWxnuAffIaeMLkoPYkf7bQR42vRSifp-5PEePuoPrAACTr-Y_JN8IakTrKZwkvJTYineNR6tL0YjxqQNiucX-3P8a7YZS3NlaENgc9oPA0cD9WoB9ehfWL4FZxqDg9TvXgO9sxp7fLEEduJwu-IgwXkixyPz9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد کشتن قاسم سلیمانی: کشتن سلیمانی یکی از بزرگترین لحظات در تاریخ خاورمیانه بود، زیرا او ترسناک‌ترین مرد در ۱۰۰ سال گذشته بود.
🔴
حتی آیت‌الله‌ها از سلیمانی می‌ترسیدند. آن‌ها همگی از سلیمانی می‌ترسیدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/129294" target="_blank">📅 10:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129293">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfaa82c92.mp4?token=oGZta9aHOpr63hj2x3wyQ_eoXF9KQpMoww6a1Eu-SCN7jObQLRnbUFmRe-gjTl8DRNco07CC1CWpPxuD-bKaZFY2TF0d4YOf7iS37yFtTViQskBQtDB8u1KvJMEh0fZ-CP3z--i218riJpjTbwS--kH76BokNpHgiXkoN-ywSomCJYtlU4ADXpgSVFCPMWrAwrl-1Sh8Rr8xz-LVApf5u-ti5afO8eWVIztg8Q1oJu-YIWRfkd3Ug7L2h480RGXDtA7bHAw5Mj9Vti_wNh0NyXEKv8pSeBR7dSHFzwj93LGhuKF0_F1nxRBwgcb7ND-TiLj37YnYcAZsxouCVeYWbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfaa82c92.mp4?token=oGZta9aHOpr63hj2x3wyQ_eoXF9KQpMoww6a1Eu-SCN7jObQLRnbUFmRe-gjTl8DRNco07CC1CWpPxuD-bKaZFY2TF0d4YOf7iS37yFtTViQskBQtDB8u1KvJMEh0fZ-CP3z--i218riJpjTbwS--kH76BokNpHgiXkoN-ywSomCJYtlU4ADXpgSVFCPMWrAwrl-1Sh8Rr8xz-LVApf5u-ti5afO8eWVIztg8Q1oJu-YIWRfkd3Ug7L2h480RGXDtA7bHAw5Mj9Vti_wNh0NyXEKv8pSeBR7dSHFzwj93LGhuKF0_F1nxRBwgcb7ND-TiLj37YnYcAZsxouCVeYWbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره قاسم سلیمانی: وقتی سربازانی را می‌بینید که بدون پا، بدون دست و با چهره‌ای نابود شده راه می‌روند، ۹۶.۲ درصد آن‌ها از ایران آمده‌اند.
🔴
از سوی سلیمانی بود. این سلاح مورد علاقه او بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/129293" target="_blank">📅 10:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129292">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
الجزیره: ۴ حمله جدید اسرائیل به جنوب لبنان
🔴
۴ حمله هوایی به شهر النبطیه و شهرک النبطیه الفوقا در جنوب لبنان صورت گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/129292" target="_blank">📅 10:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129291">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ در مورد جنگ اوکراین: وقتی جنگ اوکراین شروع شد، پوتین صدها تانک داشت که در حال حرکت به سمت یک بزرگراه بودند. یک بزرگراه بتنی، بسیار خوب، محکم مثل سنگ، درست به سمت کی‌یف.
🔴
او می‌توانست در سه ساعت آنجا باشد، با سرعت ۵۱ مایل در ساعت که حدود حداکثر سرعت برای یک تانک است. آن خط بزرگ تانک‌ها را به یاد دارید؟
🔴
و آن‌ها ژنرالی داشتند که احتمالاً دیگر در میان ما نیست. او تصمیم گرفت به جای رفتن مستقیم به سمت کی‌یف و پایان دادن به جنگ در روز اول، از طریق زمین‌های کشاورزی و از میان گل و لای عبور کند.
🔴
و چند روز قبل طوفان بارانی بی‌سابقه‌ای رخ داده بود و آن تانک‌ها در آن گل گیر کردند.
🔴
و من به آن‌ها جاویلین‌ها دادم و آن‌ها تانک‌ها را نابود کردند. من این را قبل از وقوع این اتفاق گفتم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/129291" target="_blank">📅 10:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129290">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIgDrtE3G--ymz9tDtnVzLCqNHmmHhLK2ofhISqgxeRypN3k_LhKUAfILPdK3efwGd6uJDBBl3DpyxUdigyxqjNYYcCi1WZMqm4KWVCsQb2aY2K_wk3AGP06cU_Fm9u2os_iLnA9CEkTiAv5pb0FxG558TjS1tIZYLy24udL9w5FiLAzSu80hQImeOFIs3RRIi-fv2sqfnN-r9sdM8olUfhuFtT50bK9po9NOoM1OZJTS8W0OwH55F9RpLDtCE6EEmnWTI_kcCQrbd0uHHwls61VRngwXkul8YSPmg2GQD2AI4aXqILIG4bFG6F85yQ38fi2npwU-DaoMOhaEYv_Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تیتر یادداشت جدید نشریه فارن افرز:
«ایران در جنگ پیروز شد اما ممکن است صلح را ببازد»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/129290" target="_blank">📅 09:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129289">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J__AUQPpr0iFCzgRhKzrL9PbJ_sidOL2HoOPxwwIo4mrCuwp2i8Wov8kss3Hc60KzGaHnWjZS8CwkC3WJTzcWGvk7zdmskH63JBB217MQWykh9SoCrjDcw7OtUYdG_v2BL4wh8RgcS0W7TewkNPHz3_lWNHTUZ2b9t9JxKpzBEtS05tMTusKn40VLCU6jDj9MOfh49R7DjznctiYnQpOP9PowCI9fzQJZ2ttT7uNMahnAlyrV0XJJI1OKe6RSpAWhER_SJyqHTGdNnH9O8vON1aBQarqa-7U5FVabu3mLo4or08-iDEwDhOOKvLlEUkwxjtfx36xjQS8EhqpeSg50Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره: یک منبع به من تأیید کرد که تاکنون، خط اعتباری که به تهران اجازه دسترسی به دارایی‌های مسدود شده‌اش را می‌دهد، همانطور که در یادداشت تفاهم تصریح شده است، فعال نشده است.
🔴
ایران معتقد است که ادامه دور بعدی مذاکرات ۶۰ روزه مستلزم اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ یادداشت تفاهم است.
🔴
تلاش‌های دیپلماتیک از طریق واسطه‌ها همچنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/129289" target="_blank">📅 09:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129288">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
معاریو:توافق میان ایالات متحده و ایران و اظهارات رئیس‌جمهور آمریکا، دونالد ترامپ، از جمله انتقادهای تند او از نخست‌وزیر بنیامین نتانیاهو و درخواست آمریکا برای خروج از جنوب لبنان، نگرانی‌های جدی‌ای را در میان افکار عمومی اسرائیل برانگیخته است.
🔴
۶۳ درصد از اسرائیلی‌ها در پی تحولات بین‌المللی اخیر مرتبط با این توافق، نسبت به آینده اسرائیل ابراز نگرانی کرده‌اند.
🔴
این نتایج در نظرسنجی‌ای که روزنامه «معاریو» با همکاری مؤسسه «پانل فور آل» به ریاست دکتر مناحیم لازار انجام داده، به دست آمده است.
🔴
این نظرسنجی همچنین نشان می‌دهد که تنها ۳۱ درصد از اسرائیلی‌ها نسبت به آینده کشور نگران نیستند، در حالی که ۶ درصد دیگر در این باره نظری ندارند.
🔴
تحلیل داده‌ها نشان می‌دهد که اکثریت قاطع، یعنی ۷۸ درصد از رأی‌دهندگان احزاب مخالف، درباره آینده اسرائیل نگران هستند.
این درصد شامل رأی‌دهندگان احزاب عربی نیز می‌شود.
🔴
با اینکه اکثریت اندکی از رأی‌دهندگان احزاب ائتلاف حاکم (۵۱ درصد) احساس نگرانی نمی‌کنند، اما بخش قابل‌توجهی از آنان (۴۴ درصد) از آینده اسرائیل هراس دارند. ۷ درصد دیگر نیز موضع مشخصی ندارند.
🔴
دکتر لازار معتقد است که این داده‌ها نشان‌دهنده نگرانی‌های جدی در میان بخش‌های گسترده‌ای از جامعه درباره آینده کشور در پی عملیات «غرش شیر» و پیامدهای آن است.
🔴
به باور او، این نگرانی‌ها احتمالاً در هفته جاری و پس از انتشار چهارده بند توافق هسته‌ای میان آمریکا و ایران افزایش یافته است.
🔴
این موضوع در شرایطی مطرح می‌شود که دونالد ترامپ اعلام کرده است ایران حق دارد موشک‌های بالستیک در اختیار داشته باشد. همچنین معادله جدیدی در لبنان شکل گرفته است؛ وضعیتی که در آن این نگرانی وجود دارد که اسرائیل مجبور شود تا مرزهای بین‌المللی عقب‌نشینی کند، توان بازدارندگی‌اش به‌شدت آسیب ببیند و یک معادله جدید در منطقه ایجاد شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/129288" target="_blank">📅 09:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129287">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وال‌استریت ژورنال: آمریکا و قطر در حال برنامه‌ریزی برای آزادسازی 6 میلیارد دلار از دارایی‌های ایران در قطر جهت خرید کالاهای بشردوستانه هستند، این در حالی است که ایران برای توافق نهایی صلح، خواستار آزادسازی 24 میلیارد دلار از اموال بلوکه‌شده خود شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/129287" target="_blank">📅 09:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129286">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77bc3683da.mp4?token=pF_4UkKo5wGgvCchWMJYFJJ4TIMU-1hsZA5daAFwAJTL-VWfxqYxoulkyxlIPwQ4nr3ojPs1Lo1kQ2Pnh3jAOf8Sx0cek8h5hUDvmrdh-t_9wi7zcGn3rwt3w_9iZCy2MebuQ6JKpCeJu_kresi-ccg8bBwe_FdTtnXDUjpWH_CsrrO4waE9Bs4Isa-N-BXzOfISV0lcrBYSqCKCmRHfB33qcuEO_Ka3ISYY97e6uivE8U3z2lt-2_f2bg7-VtdKr_er9btQV5VA3JCyuhDs-rSlKkCiw4m_8e_kAYUSIb4lGIk0W0FjMavCj5iqIP1VM3X0VvTgYC83dWhZsJRIbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77bc3683da.mp4?token=pF_4UkKo5wGgvCchWMJYFJJ4TIMU-1hsZA5daAFwAJTL-VWfxqYxoulkyxlIPwQ4nr3ojPs1Lo1kQ2Pnh3jAOf8Sx0cek8h5hUDvmrdh-t_9wi7zcGn3rwt3w_9iZCy2MebuQ6JKpCeJu_kresi-ccg8bBwe_FdTtnXDUjpWH_CsrrO4waE9Bs4Isa-N-BXzOfISV0lcrBYSqCKCmRHfB33qcuEO_Ka3ISYY97e6uivE8U3z2lt-2_f2bg7-VtdKr_er9btQV5VA3JCyuhDs-rSlKkCiw4m_8e_kAYUSIb4lGIk0W0FjMavCj5iqIP1VM3X0VvTgYC83dWhZsJRIbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از شب گذشته تا امروز صبح، ارتش اسرائیل حملات پهپادی و موشکی گسترده‌ای در جنوب لبنان انجام دادن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/129286" target="_blank">📅 09:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129282">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZCyfMCqCHUU4py-h3ol8MBhl2t8D1VR5YqosbbZ7bLcaX2MHrx-oObnzWRZqP6_dimq-VfgrHEINrGqO3g7j_SjbXYW3I12h4TEZuqPUrRzLLj-xXebgkfRvSyJQMkzoA20CUTL2HqmhJn4UEl8K0gO3k--f0DJShniNmFgW_dtp0UGRtqzva1Zc4hKgnlKKH_8RO_0sX3VXlwEZGIewGV1xFAsM5ThzXweUM95didWUlgG1pWmzqh0GNRTdpG40su6erio8sTOiuK1YzffZHH63_6l2kES1VGUnLaSpOnlgxUhxbYmrTUPcwHIeV4k1Bg1XPqlvaGaWz_WK9HnosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pj_JmlHKWyvGYEwIVNvfCF7KAXDB2jOca4fazEYve9XnZa9bCjyl35t1p3LDJ1W7f9m2yeLIbyjEGOS5g-WSIfw6uYfheTcOCgPmxMHIpzT8SGi2YdAsPUzPggHXCv85TOcLDtQQKoWKVEwW5NgRVnRK3ereytV5yGKy3kyyhf41Ki6tEZIgQVZXpojjqWJpjIb34hnMrWwkupOMSQ8psKBBDH2LMOTPUdb5idKgrM2vq1mgx9h7KPwR2EPNld75zMKm9hq5sUONY-A2VlwTzVuDBM6WZ4j5pnc0AJ4aNf0oyQXJkQCYdQZbT5qo-iPZg8r07hT0u58FZgGsOT0BVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h0FTEDeYG9Fk9s-Q6U0AVXvU5Js8n1skzWNrTdb9marrUYUhJqUoosfHcGe8FkJCEY9CQg4RwjmbMcgih-kHc7Lf7T4wdo3v88apfrerphCDmmcc2Ioz9zNOUxHWoRDFdr90-LoXMGovQzx_3ETVQutbu2xdhNkv8Fqsr74ypCjAReLsYCCp3fe2ocurG6_AvH2YBzJD84xqv08dNxH8GUyD-I1yogs97lUVMWXQRd7ykv9tcI1hKCbY-lo504ZSAVhX4Pf_ewb76kY84P9FFgit06YOpiVi2pcXXFaR4T9MRe8acjXXJUsIeVi7tWzz-jNbpih_bRPJPbWiHIlecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C0UXxiETYbQZtrnOk3BhkQMcban_N_K5cxrFRFofvHlC6WGRgrtKKATFpvXaARCZSYxISl22Odonto6yVz_Vg1_4cOcMqNjJ0RlBECHkRxeuQblS9WOhW_00ayuo5UL9eIgz-_m2B3kIeVAW4XJngOAive4WBQ9TZKDV0VC8zWlGEGGdSyo8r-bcX-Y4pUih8vHlZQJ9WgkuapPhy0o5FD63qkYvV60ar_xO5s_t8FnYoaT9EKiBXZwcV0AH-WgABoDYIQXPYFHNp5Vyel1aPLcId-OJu2zczElk2Ng3RfKieU2GvY-oZ7zWu62uQrbRREjSqFejpG_JiySzbrkSww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات صبحگاهی ارتش اسرائيل در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/129282" target="_blank">📅 09:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129280">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jHD0f_sV5umJNg7NmjQb4WwJBw0cwQCnDHxHg9Ii7wi_g8I_IcJnOSYQINkMANAdu7I5I9gc2H2B7UNd1J7yypXzUe_jqQ3RV6mrxbc_OS0UNk5zzKvi50P0eFGM4F-8G8vo1OptwvIlW09S1B1iIY4KShz2gw8KwAQzPcFA-yFh9iGPKYikOirVrCpjGOQjgpwtJMglVk3nkd7KQl12i0vPQ_LLW2_qV-wXNoPkgLU6dMTQeovCRArL26SqpKgSVSADC34mqKZ_PiMPUevMo0J6oWyqG1zTskkmaiDaQLKUSwXM9zDR0e-Ll2slpwB1eHOYWWZnabJn8HE38q_9wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SpFR2gYbDt3E04AURGD7ZiT3H8s1SLEoG3Iwm3FVnx593IDwwlkgHMYF3RvQriReNoWlVBh-jMDDzTI35tW2kRWvqa-PjRx4-PugDvFxGNyPXU1yWKSB80PBkSsutZtuC_PSG6W_y1yQ-grcU7Ffd2MdkswF5ZHajpbJoB5WQFHMzeVvzo14lY-2djEIai9z5BawjZkDHzVk1e9jEWCAR2Zj7NmpDzxpIA4l4uwuvRP9Vv9IeAGqIoINjS8MY-fSv_42q3IjLjkDg3pFgjgiKtZFeBCxg2BY6W7UCaHO1oUZVJDrqRFkDUTDr6_hJZz-gLH7ojPIvLXgZYCjRuFavg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بمب های فسفری که دیشب اسرائیل بر علیه حزب الله استفاده کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/129280" target="_blank">📅 09:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129279">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سپاه: احتمال شنیده‌ شدن صدای انفجار کنترل شده در محدوده‌ جنوب اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129279" target="_blank">📅 09:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129278">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوری / آکسیوس: عباس عراقچی، وزیر امور خارجه ایران، در حال برنامه‌ ریزی برای سفر به سوئیس است و این تصمیم هنوز قطعی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/129278" target="_blank">📅 09:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129277">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
قائم‌پناه: دارایی‌های بلوکه‌شده ایران به صورت کامل و تدریجی آزاد می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/129277" target="_blank">📅 09:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129276">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
به گزارش رویترز، در نتیجه لغو تحریم‌های ایران، سپاه پاسداران آماده است تا از نظر دسترسی به صندوق بازسازی بالقوه ۳۰۰ میلیارد دلاری، «برد بزرگی» کسب کند، ضمن اینکه از محل معافیت از تحریم‌های فروش نفت نیز درآمد کسب خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/129276" target="_blank">📅 09:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129275">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ونس: بین ترامپ و نتانیاهو درباره چگونگی دقیق پایان دادن به جنگ با ایران، اختلاف نظر‌هایی وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/129275" target="_blank">📅 09:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129274">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فوری/ ونس: خروج اسرائیل از لبنان بخشی از مذاکرات با ایران نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/129274" target="_blank">📅 09:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129273">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
منابع خبری صبح امروز از حمله هوایی اسرائیل به یک ساختمان مسکونی در مرکز شهر غزه خبر دادند که در این حمله ۳نفر کشته شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129273" target="_blank">📅 08:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129272">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JOLimSlVR7F9qDWyP4bl60aIZf6sBpPxnbsXNBJk9KBFd9-Pd80rPQAKG0dWKIv56OOmScOx3j17OL_BdRqnnKM3xK5TVxzPgjq1XCuFkhEUy-NhjdTlz_Wadmcs9jtY06-xWbiX_jrOJX4I8TL-uTL4JryDPrSKmNBlMvYLXz_TI8UovbENer-0k1IfN_8Q13oSn6Mp7GJoZogziPntcSYYqmbXQBS1mqdJUf1bQbq7UjUG8TCoN7j9fR7Rm86-BNSRC_CbLuqKfu9D_obUYvgLVypgPiuk0VIeIVWqlqRp2kHYmbwM5iu1fzc1BPLW5aYLXXSUstB5qzVNQ6V7CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیشب ائتلاف بین‌المللی به رهبری آمریکا، یک موتورسیکلت را در استان ادلب در شمال غرب سوریه هدف قرار داده بود. گفته می شود این موتورسیکلت توسط مقامات ارشد حزب اسلامی ترکستان اداره می شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/alonews/129272" target="_blank">📅 08:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129271">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
خبرنگار الجزیره از حمله هوایی اسرائیل به شهر کفر رومان در جنوب لبنان خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/129271" target="_blank">📅 08:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129270">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249ce5af71.mp4?token=PrV3lHT-uFZOZenJWLBmYZz4Espr0rmFZyzvtKJSgP1IouR8pK2JKG1G998_aCS-ZMr_8I0DQ8ybGq-RYI24Gz6WIAed49z0G3VnqVI7LOUsY3LtQqUY0ZJFUSHug5DG5o1kuKylSkjsckBlgxJZgBvBSK0bOk9RKzPVHo7g42M7dwvRvP_gF8pX2P2G5PH5Up2rwXtBB0XabA7gZtwdb8g7zc09QbPC_GarAORqtEg-BePLrnp49mo4H17J7EDLDrCncCX6xJBqobwKiDmplsGj5Rkll1jP-7C8oJ-sqjeXt5ryqwztQGjB1DSpLbQsxNVwAIhm-MSOpR-O08_tkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249ce5af71.mp4?token=PrV3lHT-uFZOZenJWLBmYZz4Espr0rmFZyzvtKJSgP1IouR8pK2JKG1G998_aCS-ZMr_8I0DQ8ybGq-RYI24Gz6WIAed49z0G3VnqVI7LOUsY3LtQqUY0ZJFUSHug5DG5o1kuKylSkjsckBlgxJZgBvBSK0bOk9RKzPVHo7g42M7dwvRvP_gF8pX2P2G5PH5Up2rwXtBB0XabA7gZtwdb8g7zc09QbPC_GarAORqtEg-BePLrnp49mo4H17J7EDLDrCncCX6xJBqobwKiDmplsGj5Rkll1jP-7C8oJ-sqjeXt5ryqwztQGjB1DSpLbQsxNVwAIhm-MSOpR-O08_tkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی گسترده در فلوریدا
🔴
آتش‌سوزی‌های گسترده در منطقه اورگلیدز در جنوب ایالت فلوریدا از اواسط ژوئن تاکنون حدود ۸ هزار هکتار، از اراضی این منطقه را در بر گرفته است
🔴
گسترش دود غلیظ ناشی از این آتش‌سوزی‌ها تا مناطق مسکونی اطراف نیز رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/alonews/129270" target="_blank">📅 08:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129269">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WDoNpVFtpSh2oSyYP3uyuZQ8GpZ6fkTjA9LVMVls9W0SdrhmGwUSCxNQUsfbDBUWgDpxgBFN1oa0JBGkn0MWdUjHjM3M2zUEcAnLVZMsV86HnCNsVRGDdBxBVzCqbI_68fwAJytADlS1shDv-__IipR0gAOwoc-5hNtYYH905M7mkkj2Fooy587UVzmK_BjYO43coItO5QbIc86Fm_zzRdkzPLR_Nz24pyioSYEV7sKfpvJXPpqrGGzOsoplvbkgcc4IWo6h9UbzeY2dW4_xjZ2jF-rN1llTZt9LML87cUa0ROlPAdEoNja6_NIw0D94JZdUyim19gdLw3TBYJvEkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه‌ای نزدیک به میریام ادلسون، «اسرائیل هیوم»، از توافق ترامپ با ایران به‌شدت انتقاد کرده و آن را «خیانت به اسرائیل» دانسته است
🔴
ادلسون یکی از مهم‌ترین حامیان مالی ترامپ و تاثیرگذار بر سیاست‌های او در قبال اسرائیل است. این انتقاد به‌عنوان پیام فشار از سوی او تعبیر می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129269" target="_blank">📅 08:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129268">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
هاآرتص: نتانیاهو وارد «روزهای پایانی سیاسی» شده و این وضعیت می‌تواند برای اسرائیل خطرناک باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/129268" target="_blank">📅 08:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129267">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rz7HEDvms3tfhn3GhROn6K-Ldg29kV49Xmzw0uZzarXtelduO3pNmetE_wUWbumX5myxnBE_CzJQYPFpOM65-_T0skPc76NeD9q1icAIHibyOLGXOIe3DGd9b0GVTbeg1JVRMUQ51zJdAd5fZdLkVjIiDC1BIJ1q4zZFGsbX-tUyZQ8oU6RjFf1zvtmxi4itKiQ9qQ1NaETk_027zdrffOOMUDmHZ2IU37-_J2K_2vKvcqsWxjiPfmTxGdHYKjvbvFG_DNd2GkluvF2iTP0MssuPrHuQ4cMZp0N7cGtH5DEKPhTSBZVaw9kxC_5C1BcEQ9GxQdKFN6b9k7w4FUiXYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حرکت 10 نفتکش ایرانی به نام های؛ دیونا، قهرمان، سونیا، دورنا، آمبر، خندان، برف، هدی، استارلا و دریا عمیق به طرف چین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/129267" target="_blank">📅 01:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129266">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSN3luxOsvGbqBH1sPlkGfh4nJJxDLzrDo5lOz2uJwIdaeUSZyv3c698mY9MFGB_i2ddg-xh0yqZJwMuB5v7zv-EgD5LL6rjSv5dHL-T4zDyE2DvTrQZIEc4T1eAy9vG1CDsKnwOv9FAPsFV2fThDOkJxOgJ4k-9XbUR1-X0MPxfr_ReTTONa-3eDd0XdXAqcLv4AxuWtZ3OgdaalOudSvRpr1rMCMrqq__6wr-EDPylrYdl4gszCBKl9iOB2m3MQUd1DQ5RoelTapuhrWK_NLRh37Srf9fyKodRK8zD0fH_CypioE6k1Odxve0KYK4mlyREUoAUpj3EdzJ70jjdGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی :
دشمن اگه غلطی کرد باید تنگه رو ببندیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/129266" target="_blank">📅 01:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129265">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtMKm_-2Wblvw_2FVVHfIT3DX4H-wROQrvjHVjAFqX_fhQkYn3ke42P3Z5yrAKqrk8D4lZdAk8fsf6NLNRLk-tBQxWuY32cvB02crax2OGrpoXUGIje72pWLsjTIC73af50z0GFSHqLfMzmwCj7jCXY6Ya7-ofB7RMrDuSXE1J4Sf-YJpp8DtHYj6SnPseA6O-fhj4D25-lxWBBSOIbeI8RTZbyGKobfbEEFuvHA7t2lsvYEq35jOsYlqersiOvNKfLsyuexsxuqGvthoi2kjLmjgC8X4rjZg_qwRIo77-WfvEyODCTIAV2jc2uPURFi-xpYbBuk380X_3cWDof9Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی آمریکا هم به عنوان دومین تیم به مرحله حذفی جام جهانی ۲۰۲۶ صعود کرد!
آمریکا 2_ استرالیا 0
@AloSport</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/129265" target="_blank">📅 01:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129263">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dda595df5.mp4?token=OB1zjNAuMWyrAGA4yoc3oz3oXo0y46p6CHbwSfyvgSfJcXgZSo-MTeP5zCr6g_fV_qqf7WesO8oWIuPGGOHkKkd3lpEAta8E5fFF_U-KJDMfAYZfXKdCdwfDKkzsMnCSCln4GaWAiHuubDZiKQojW8iMlGkmVQER3hCHM5QSqmHHv4Urq467qrjY_hf4dFF7eaiDJpinl-euhKyxHG6Lg1mQU8sr4nIMDYbjdLirOSD0lmTT1fn2VzOtNiKqjpDYeC3giEUbVB7fbR2Pfk6X8Y30m0ND-icEtFvGK4RciDN5LKnoc9z3sJ0CpB9rYm6J2QBNKWQAZ-Ta2N7xtHDu6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dda595df5.mp4?token=OB1zjNAuMWyrAGA4yoc3oz3oXo0y46p6CHbwSfyvgSfJcXgZSo-MTeP5zCr6g_fV_qqf7WesO8oWIuPGGOHkKkd3lpEAta8E5fFF_U-KJDMfAYZfXKdCdwfDKkzsMnCSCln4GaWAiHuubDZiKQojW8iMlGkmVQER3hCHM5QSqmHHv4Urq467qrjY_hf4dFF7eaiDJpinl-euhKyxHG6Lg1mQU8sr4nIMDYbjdLirOSD0lmTT1fn2VzOtNiKqjpDYeC3giEUbVB7fbR2Pfk6X8Y30m0ND-icEtFvGK4RciDN5LKnoc9z3sJ0CpB9rYm6J2QBNKWQAZ-Ta2N7xtHDu6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون درگیری‌های سنگین بین نیروهای اسرائیل و حزب‌الله تو لُبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/129263" target="_blank">📅 00:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129262">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78535e623.mp4?token=CoUxV78672lQp0UMLXD1ceq0S7nPFHYLBkF12m7n70OAkH2OTKjwe5fd2KYS2CIkJNubY33n35TWwpNEBmOh30M7pbz-AEJqXnq1VydAERbTATE1-odqq-dul54gGHhsXIFX7BpjPlGZfSRKYNdCAbiqlRxovcrgrjz28gND4ww_YmYx6G5wI5u_Xkty8D9q-nHI2SfvnhHuzIH-cXq_VQjXSuBAHoIsULTX4tEnv2ZcRGGqMIrgkgyVeT9Yc3XngB6arak6DPJbdVkedQomGxKbztZEoMbBWWY1af39h6qCiu9LfFPMQVpP4FXC_84Eyf7t329kmtVwzBuenr3ECA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78535e623.mp4?token=CoUxV78672lQp0UMLXD1ceq0S7nPFHYLBkF12m7n70OAkH2OTKjwe5fd2KYS2CIkJNubY33n35TWwpNEBmOh30M7pbz-AEJqXnq1VydAERbTATE1-odqq-dul54gGHhsXIFX7BpjPlGZfSRKYNdCAbiqlRxovcrgrjz28gND4ww_YmYx6G5wI5u_Xkty8D9q-nHI2SfvnhHuzIH-cXq_VQjXSuBAHoIsULTX4tEnv2ZcRGGqMIrgkgyVeT9Yc3XngB6arak6DPJbdVkedQomGxKbztZEoMbBWWY1af39h6qCiu9LfFPMQVpP4FXC_84Eyf7t329kmtVwzBuenr3ECA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک مداح دوزاری، پزشکیان را تهدید کرد
🔴
پ.ن: مداح‌های بیسواد و کودن چندسالی هست که تو تمام مسائل اعم از سیاسی، اقتصادی و اجتماعی نظر میدهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/129262" target="_blank">📅 00:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129261">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c909e237b.mp4?token=mLbJt9rhaYzHcQMFMjCEv71xlPuB1roYfuEUGfBN1d3mNoIEPL1imbbgPjHp6Zl9oZ4F5dy-iJqDLFscY40NOJQp5SxSJoCouwAUErF_1x9DTmS_BBDjM-tsdTtKBDqzOZu1aAa0qzmeMkArENPK3A3RQNqUYk0jUp5K0A_l_5qosFxF6IXGB_-i0g88Csbq1HSPf4-fUremtO_Msd99HhhBbz0N94Qk9EuU7jORd8KuAHW9RuBC7EIhcIP0FM8-QLV38bQGiivPg3Zt3GLV4raCwoUP1z538k-MVp-a1vz9alSJ1zMlslIUBXy4cw4-5tEXLUz_cmEKXkkHZAZM_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c909e237b.mp4?token=mLbJt9rhaYzHcQMFMjCEv71xlPuB1roYfuEUGfBN1d3mNoIEPL1imbbgPjHp6Zl9oZ4F5dy-iJqDLFscY40NOJQp5SxSJoCouwAUErF_1x9DTmS_BBDjM-tsdTtKBDqzOZu1aAa0qzmeMkArENPK3A3RQNqUYk0jUp5K0A_l_5qosFxF6IXGB_-i0g88Csbq1HSPf4-fUremtO_Msd99HhhBbz0N94Qk9EuU7jORd8KuAHW9RuBC7EIhcIP0FM8-QLV38bQGiivPg3Zt3GLV4raCwoUP1z538k-MVp-a1vz9alSJ1zMlslIUBXy4cw4-5tEXLUz_cmEKXkkHZAZM_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برنی مورنو، سناتور آمریکایی: لغو تحریم نفت ایران به نفع آمریکاست چون چین پول بیشتری می‌پردازد
🔴
«ما اکنون به آنها اجازه می‌دهیم که نفت خود را بفروشند. این چه فایده‌ای دارد؟ این به نفع آمریکایی‌ها خواهد بود. این باعث کاهش قیمت نفت می‌شود.
🔴
و چین را مجبور به پرداخت هزینه بیشتر برای نفت می‌کند! و همچنین متوجه می‌شود چه کسانی نفت چین را می‌خرند. بنابراین ما را در موقعیت عالی، یک مذاکره عالی قرار می‌دهد و در نهایت، من به رئیس‌جمهور ترامپ اعتماد دارم که تصمیمات درست را می‌گیرد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/129261" target="_blank">📅 00:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129260">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ترامپ: ما رابطهٔ بسیار خوبی با اسرائیل داریم؛ نتانیاهو یک جنگجو است
🔴
اسرائیلی‌ها باید از نتانیاهو قدردانی کنند، چون او واقعا کارش را انجام داد. ما واقعا در کنار اسرائیل به سختی مبارزه کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/129260" target="_blank">📅 00:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129258">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ درباره اوکراین: خیلی چیزها توسط بایدن به اوکراین داده شد. آنها باید هزینه‌اش را بپردازند، اما این در برنامه‌هایشان نبود.
🔴
هیچ‌کس از آنها نخواست که پرداخت کنند. من گفتم، چرا پرداخت نکردید؟ آنها گفتند، هیچ‌کس از ما نخواست، آقا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/129258" target="_blank">📅 00:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129257">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ درباره حمله دوباره به ایران:
به یاد داشته باشید، اگر این کار را انجام دهیم، ناگهان نفت به سرعت از تنگه خارج نخواهد شد.
🔴
افرادی که مالک کشتی‌های میلیارد دلاری هستند، دوست ندارند موشک‌ها بالای سرشان پرواز کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/129257" target="_blank">📅 23:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129256">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd6c2692d6.mp4?token=qOI0mKHebv50MNfeuJaZCCdU5eFFE_CGQoK2M9S7mlxNQHW3MMDJP5pHHffre6fqaqYInA2tuq_7o120zcXAdfEDYg0NVsmLGX-zXzhwLw6lMEhdkF5CTYQvhLYc0qup0nmByLzdX0sFlp5sdsnIs2FnT0o-oh99NGgLAThNDb_pStKAPbxbbZmSFzFWUFA-2tsy_tJOBlymnPMGnE5NggVUm-A7fMtBs7Ly8oxA-utdk4CwpTrZLgNgocSJoAcBY7aWePJWNM1NiM7jQepyQzeh981HZIhhXtafW12osf8Ul9QF9cbGn8tnVMmvEK58KrImSZs4OWCuSeFiuF-x0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd6c2692d6.mp4?token=qOI0mKHebv50MNfeuJaZCCdU5eFFE_CGQoK2M9S7mlxNQHW3MMDJP5pHHffre6fqaqYInA2tuq_7o120zcXAdfEDYg0NVsmLGX-zXzhwLw6lMEhdkF5CTYQvhLYc0qup0nmByLzdX0sFlp5sdsnIs2FnT0o-oh99NGgLAThNDb_pStKAPbxbbZmSFzFWUFA-2tsy_tJOBlymnPMGnE5NggVUm-A7fMtBs7Ly8oxA-utdk4CwpTrZLgNgocSJoAcBY7aWePJWNM1NiM7jQepyQzeh981HZIhhXtafW12osf8Ul9QF9cbGn8tnVMmvEK58KrImSZs4OWCuSeFiuF-x0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: پیت هگستث یک فرد ذاتاً بااستعداد است. او نمی‌داند چگونه ببازد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/129256" target="_blank">📅 23:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129255">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3Xic07cEuimZ1auMyYz3FEVNfkuSYLFOtRIoy6Q7FgzQSjyDCdBqisPr8qXYQO_23hwkpiH-JfciHLxkNBoqkGA7Nn4KNlKiWUph3b1NwHemXBBMnnKi4n4oy70fnwV62HOWtWunPIx5k1ecHP_qdCNc5JTIVZts0JnBIObnPjOoeBqipnhfqf3tMoJvdwzq5iWENj0VDqeQOyvzY1y19xC02CIAtTBI1cxqnicy2_wo1iMYuXrmDJQqYh9MVDAntWqJSR74BtnpiyZ99Bs_SL4ahcd9Cv6E3Pyz18v3k4-EGj7i0N4nW6HgBUefslfk9YWZiQyy_TBXLSCbw0s1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی: ایران به نقض تفاهمنامه پاسخی بازدارنده خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/129255" target="_blank">📅 23:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129254">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ اعلام کرد: جنگنده فوق پیشرفته F47 برای ارتش آمریکا در حال ساخت است، پیشرفته ترین هواپیمای جنگی در تاریخ بشر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/129254" target="_blank">📅 23:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129253">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
صدای چندین انفجار در استان ادلب سوریه شنیده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/129253" target="_blank">📅 23:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129252">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tM5kTzDibRCwsBr4Ofokspl7pqq-cmV6O0-zpM3jt7fdjSc8r8uayzbsuExDmG6Zn1G7Q1EtRFJyif9AqAFIcDidXZhJCVcULD_DV5o5b-zcPhDl1fdEVXKO79SyzJpQoMiUbVxYJY5QUtkzvsub24tA3sDdQnYlxuFryiNRvrqPtT5XLhTp0IIvR6yDJWQsO_m2AMlb4g_aF2EhWMT6fkK2IOosRyLGVE13gfz6VWA2j7eFVsxiBmO1dwhO4HCCR6ameLKslUvR5yA7VLQtOpl7dMvIvxSWj7Z87QPTqNT2AoxjPcba5TGOPFYM0uDcJO-YRknn3SzPqiUrurrGgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای زمینی ارتش دفاعی اسرائیل بار دیگر در تلاش برای پیشروی به سمت علی الطاهر، جنوب شرقی نابتیه هستند. حزب‌الله یک بمب کنار جاده‌ای را علیه نیروهای اسرائیلی که قصد نفوذ به این منطقه را داشتند، منفجر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/129252" target="_blank">📅 23:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129251">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d97f24c8e.mp4?token=aZqr5P-qJDv6qZlv7wU6kXTTlfAWUlNp93FATZJq10PJvSdCczARTU55m8a5rIYD4JcGIL8QKBrZWe4qdEAv33hkxOqITazVrXg47LbXXCU7pSxlBl_iggtk_BSk0D7yWHqupGoF54J6RPbGSWwNO0aysltlOcyX7EkKlJ-_a6ms0nM5UeIoADEzb6WDMmZHF-BgeOVPbPisw37r8XmEATmuKhypXIvwk77VvATXuPOMmUM9dkTtyyMQTA2IZuHzSCic7Yo4zpeT6bagiqBD7F2pjXDBhq9v9W5PdHgOW7DPwbfARLCaRl3RSgOdfbyUnrsF234jHF-OTX7YyK5PiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d97f24c8e.mp4?token=aZqr5P-qJDv6qZlv7wU6kXTTlfAWUlNp93FATZJq10PJvSdCczARTU55m8a5rIYD4JcGIL8QKBrZWe4qdEAv33hkxOqITazVrXg47LbXXCU7pSxlBl_iggtk_BSk0D7yWHqupGoF54J6RPbGSWwNO0aysltlOcyX7EkKlJ-_a6ms0nM5UeIoADEzb6WDMmZHF-BgeOVPbPisw37r8XmEATmuKhypXIvwk77VvATXuPOMmUM9dkTtyyMQTA2IZuHzSCic7Yo4zpeT6bagiqBD7F2pjXDBhq9v9W5PdHgOW7DPwbfARLCaRl3RSgOdfbyUnrsF234jHF-OTX7YyK5PiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما سفرهای زیادی انجام می‌دهیم. به ترکیه خواهیم رفت.
🔴
در مقطعی، برای یک کنفرانس بزرگ به چین باز خواهیم گشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/129251" target="_blank">📅 23:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129250">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
شورای اروپا: آماده حمایت از اجرای توافق ایران و آمریکا هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/129250" target="_blank">📅 23:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129249">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ: اگر با ایران به توافق نرسیم، کارهایی خواهیم کرد که آنها را خوشحال نکند، اما فکر نمی‌کنم این کار را بکنیم.
🔴
توافق هسته‌ای ۲۰۱۵ با ایران یک فاجعه بود
🔴
من با رهبر جدید ایران صحبت نکرده‌ام، اما او شجاعت خاصی دارد.
🔴
من از موضع قدرت مذاکره کردم چون نیروی دریایی و هوایی ایران نابود شده است.
🔴
کشتی‌ها به طور بی‌سابقه‌ای در حال عبور از تنگه هرمز هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/129249" target="_blank">📅 23:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129248">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ: حدود ۷۰۰ کشتی از تنگه هرمز عبور می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/129248" target="_blank">📅 23:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129247">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uy5Enhbekz090Z8pm91dmc07b44IzCt1pm6pV6pyeqd9lP9qkcKuI1YEGyjpCdkOaJFYvV1ZG58JNgfhOSA-5ygFvMSf1EAWWZWJrZMcE_hNVJvOtXIs8uly3_zqTeQ7mvFmZjQY07QL60aN5NyNYfsY2hbuvoC6FaUXwGaM4KvF8NHQR2Xw2OmX4oj5Z7OQfxCzJsAS06cGCNJbnJQBgEpr_WsoJbCk0ZnKpSaLelU75pfB5azxfTYleuxsWIlidlgvZy_mxorpPqumWUP4IQprYml2wIvVxCUMk_VlTZX1VgcYQg5Nwtwy2lsPoOC1SfUx_8yWksc-F66rzBBN9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از هدیه قطر رونمایی کرد!
🔴
ترامپ در پایگاه نیروی هوایی اندروز از یک هواپیمای موقت جدید ریاست‌جمهوری رونمایی کرد؛ یک جت لوکس که توسط قطر اهدا و عبارت «ایالات متحده آمریکا» بر روی آن درج شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/129247" target="_blank">📅 23:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129246">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ: کشتی‌ها دارند از تنگه هرمز خارج می‌شوند و نفت صادر می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/129246" target="_blank">📅 23:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129245">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
رئیس اتحادیه املاک: نرخ مجاز افزایش اجاره ۲۷ درصد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/129245" target="_blank">📅 23:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129244">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
سناتور آمریکایی تد کروز: دادن میلیاردها دلار به حکومت ایران که شعار مرگ بر آمریکا سر می‌دهد، ایده بدی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/129244" target="_blank">📅 23:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129243">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04b39ccf54.mp4?token=nHiYG0L90CAGXEhS1kO9C-7cBOnpOIOJezrW-a2yRsLdy4VYt3t5RVJduoemzsU30VpDWg13xoYqsJtgxqc74nebw94MBLpxoe9t-bllOkm-wBs8mX9MBcNDEPu9ccsUAiB35Q7itD8pGont7XQoshxcAcj42SjJnC3YKt0FtxkhcQFhuKGXQyZ_rJDh4arZgazzb5L5J3gcfV6DikVtf6Op9-wv53CPmNNELQzn7HZa5ytZGd85dFG40szu9w5g8atlkAOzJWsW1hgayHyZBNN9C_HDzUbk2f6v7cHG2MyxwNWtKdCjeJoIE_nN7ZxxIl6avD2c2uUqVmxy-F59Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04b39ccf54.mp4?token=nHiYG0L90CAGXEhS1kO9C-7cBOnpOIOJezrW-a2yRsLdy4VYt3t5RVJduoemzsU30VpDWg13xoYqsJtgxqc74nebw94MBLpxoe9t-bllOkm-wBs8mX9MBcNDEPu9ccsUAiB35Q7itD8pGont7XQoshxcAcj42SjJnC3YKt0FtxkhcQFhuKGXQyZ_rJDh4arZgazzb5L5J3gcfV6DikVtf6Op9-wv53CPmNNELQzn7HZa5ytZGd85dFG40szu9w5g8atlkAOzJWsW1hgayHyZBNN9C_HDzUbk2f6v7cHG2MyxwNWtKdCjeJoIE_nN7ZxxIl6avD2c2uUqVmxy-F59Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه ای که ترامپ وارد نشست گروه هفت شد و با شوخی خود "من رئیس هستم" جو سنگین نشست رو شکست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/129243" target="_blank">📅 23:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129242">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc24435ec.mp4?token=T7SB8KzccNymOjAv08aCV4dLfhWHd6jveDMudqszwI2N1h7qIjK3swf8JTfDBO3rus4bG2EkxxDe5d7PUJPQri7DfFvfBNLbQcJrUJVVZxhOCFE90dOMnxLuQ0gRF0mPruBOGAFakTOooCH17Nzw0hP7ip1dmUU8OCZRnfHX54Vvu-sRCiYCBMU6tBPRZa2ChwPmQEArGLzPM0InF6oYrUhzzylnPAI2ZPVnoq_x8A5sqo5VnTBN-kmelZlCBc_Ww1Cj6TWKTlrUfYI6ij5wyG9WPgNEBSzNGQkhbJ4rVx8lbBYXEXdfGkPN1jwmbIqeJBKcmDthow3_qlyO61KGBoolO4kjXzQRpp1PGgiIzf14wNV4H6sMEJV7sBr4IXQtsW77iK5v_NVfJCyDi2K_U9TEStjJEE1zrQAOuzPCsfr4wP6Cqq3dOjza8FdJaUnbo2GsM5XwNQEPD_si0y7WoIYjnzjF8OI8ViNaznjfIUiJDvAl8YxcblOeacUnKV8PIr_oAiqUKIXAgzYdEOfytV0TeYasxs0QnoHZmRKO9cIsAqK9oKriY0UBumANJJRNgb4IlK9BqwCXcb6santHsXj7yh3Gm8B4yodkiVO9Y97iptZ7YmadRboPCgMEjD_EGoy1uKVIMnOFC0rcGJ1xTNs560UFwK2QH-uHevBSdz0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc24435ec.mp4?token=T7SB8KzccNymOjAv08aCV4dLfhWHd6jveDMudqszwI2N1h7qIjK3swf8JTfDBO3rus4bG2EkxxDe5d7PUJPQri7DfFvfBNLbQcJrUJVVZxhOCFE90dOMnxLuQ0gRF0mPruBOGAFakTOooCH17Nzw0hP7ip1dmUU8OCZRnfHX54Vvu-sRCiYCBMU6tBPRZa2ChwPmQEArGLzPM0InF6oYrUhzzylnPAI2ZPVnoq_x8A5sqo5VnTBN-kmelZlCBc_Ww1Cj6TWKTlrUfYI6ij5wyG9WPgNEBSzNGQkhbJ4rVx8lbBYXEXdfGkPN1jwmbIqeJBKcmDthow3_qlyO61KGBoolO4kjXzQRpp1PGgiIzf14wNV4H6sMEJV7sBr4IXQtsW77iK5v_NVfJCyDi2K_U9TEStjJEE1zrQAOuzPCsfr4wP6Cqq3dOjza8FdJaUnbo2GsM5XwNQEPD_si0y7WoIYjnzjF8OI8ViNaznjfIUiJDvAl8YxcblOeacUnKV8PIr_oAiqUKIXAgzYdEOfytV0TeYasxs0QnoHZmRKO9cIsAqK9oKriY0UBumANJJRNgb4IlK9BqwCXcb6santHsXj7yh3Gm8B4yodkiVO9Y97iptZ7YmadRboPCgMEjD_EGoy1uKVIMnOFC0rcGJ1xTNs560UFwK2QH-uHevBSdz0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: اگر لوکاشنکو می‌گوید که نمی‌خواهد به این جنگ کشیده شود، باید حداقل با مردم خودش صادق باشد.
🔴
زیرا او کسی نیست که بتواند به جنگ کشیده شود. کشوری است که او در آن زندگی می‌کند که می‌تواند توسط روسیه به جنگ کشیده شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/129242" target="_blank">📅 23:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129241">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_fuDWopiZBLOJ6JGJnJfy7SXZgI4XYGbf8kJnTPIbKx_0Tc08CmdsXy9Cc3q_aN1w9QQ9z6aq2C0iMJVYnOMHnfDwKjFYxms-xs5Iu72LlLDksHyKty9awRezoefTayhB3UNoka0Lysoyz84c2ZrbOSffag4PnAb4LeErtTwwaMNVeoe_p_KTk0HcRMFl0SEq0ZqRPeyHHPAMCk6YP5iCJ1Y1vFUzGXqsTBWDRmhIYILMEkCZ9vnBxAwwYyw7715Jc3dMXppXiik4J-zmLD7rULn0jk4RiMj11aZU7YgOdyrFa4fIDXM4Rvmv-lvAY2UwneLqVzYF3whS4Dn-2c8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرزیدنت ترامپ با انتشار نظرسنجی ای نوشت: توافقی بسیار محبوب، به جز برایِ فیک نیوز ها و شریک آنها، دوموکرات ها!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/129241" target="_blank">📅 23:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129240">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
العربیه: ولیعهد عربستان سعودی یک تماس تلفنی از سوی نخست‌وزیر پاکستان دریافت کرد.
🔴
شهباز شریف از محمد بن سلمان، ولیعهد عربستان سعودی، به‌خاطر تلاش‌هایش برای حمایت از دستیابی به یک یادداشت تفاهم میان آمریکا و ایران تشکر کرد.
🔴
ولیعهد عربستان سعودی از دستیابی به توافق میان آمریکا و ایران استقبال کرد
🔴
شاهزاده محمد بن سلمان به شهباز شریف تأکید کرد که عربستان سعودی امیدوار است آمریکا و ایران به یک توافق دائمی دست یابند
🔴
ولیعهد عربستان سعودی تأکید کرد که این کشور خواهان دستیابی آمریکا و ایران به توافقی دائمی است که ثبات منطقه را تقویت کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/129240" target="_blank">📅 22:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129239">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkHcQjksKe-FajKxcJpQsK6UqrqGnQwUPyH8QTjDKkE_H1Jbamjr1qIECynXsUjjrxcwj4vPcWd319iLktCvw5NJsoGWGE7P3LbJAAMOKq4tgVuUEHZVD6xx1j3h8j17EZfXyRX8PIAcMHBe4BRoOcge81TQ_fRGNUhKrmkNPWjvWFdyBP5HOqFPT-MTmD-ONag8gfgihJIe9Nv59et8OyVbLPUyeQucr-8DucWQbrpV8Olue9mnkc6dae0FjMLHl5MRWYQoQ0ZCpBHejapjccX4pibL12zYTgTqbPDtFDT5EbEqTz6ajmSUy-RhelYQiMcdbQYZgPbBYUJq1uDoAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خارجه انگلیس: درخواست "به آتش کشیدن تمام لبنان" یک بیانیه وحشتناک و نفرت‌انگیز از یک وزیر اسرائیلی (بن‌گویر) است که به درستی توسط دولت بریتانیا تحریم شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/129239" target="_blank">📅 22:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129238">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
فیلد  مارشال ، محسن رضایی: جبهه مقاومت از همه کشورهای منطقه دفاع می‌کند علی الخصوص کشورهای همسایه فلسطین و اگر جبهه مقاومت نبود این کشورها به اشغال اسرائیل در می‌آمدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129238" target="_blank">📅 22:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129237">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8ef44e0f4.mp4?token=FfPfsflBLTtEQlVmL3FHTpCaJ0xEuzjmRWIBXvrDPCQ34Uk7v12TuIq1A7Pm7-B57eLT6LTqnb0TL5-Q-c3CtLXdNQv_6nXfLEC8u6ylA-R1Ad0nMm7OY0sWRN_Bma4QNowslxoAwYokQYbW86S39XIqoAe5yG0e6HOvpajuQxIoZf4zYtExU90BGTc81wvoLfW03XipO80ocxd6hCHbdsNCBYv97Pw6MU3T3UgHfUOrVzodkep1L1ky8YGbO876CCwM6rs4_sycZEMWS7W_td0Cfa2EJRHqkMBwuefgOk-NHBQnYz2fTHTrP2noJeR_AZclPC2aC6oPYydKukVcuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8ef44e0f4.mp4?token=FfPfsflBLTtEQlVmL3FHTpCaJ0xEuzjmRWIBXvrDPCQ34Uk7v12TuIq1A7Pm7-B57eLT6LTqnb0TL5-Q-c3CtLXdNQv_6nXfLEC8u6ylA-R1Ad0nMm7OY0sWRN_Bma4QNowslxoAwYokQYbW86S39XIqoAe5yG0e6HOvpajuQxIoZf4zYtExU90BGTc81wvoLfW03XipO80ocxd6hCHbdsNCBYv97Pw6MU3T3UgHfUOrVzodkep1L1ky8YGbO876CCwM6rs4_sycZEMWS7W_td0Cfa2EJRHqkMBwuefgOk-NHBQnYz2fTHTrP2noJeR_AZclPC2aC6oPYydKukVcuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ درباره ونزوئلا و کوبا: ونزوئلا نفت دارد. کوبا ندارد. کوبا املاک زیبایی و سواحل خوبی دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/129237" target="_blank">📅 22:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129236">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c77fc55c.mp4?token=acomnC-PjyPsvwbcqJQfLV-kG4Mt7_G_BAEhlgwS_ynlMOwF1Ti6jnFOe3FIllOjA1p5oUdqsl3u2_mR7O42yHj25eJOmy9HIfEz6IRFIr8-nGTe_ktRmod8Yw6a3u8fWSVRZXkrJspBet8d72RpcBjzFYDzRJgPhWEgBJhgtoN-ru19at5qZ3BxYdem9ZsLN6ftyRo3xsZ1votlXn9Q2q7asfgNU9r25k4sq2xWUmECU-6pE31RF8BqYL4h2ODU2pprgEZ-Wgp75MBma9QMm7WVCq6DUUX0CXUVZRHzAsU4ANnFvnV8UVpQZPy9lijUkV2iQjvFL8VDp9NuNYVMQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c77fc55c.mp4?token=acomnC-PjyPsvwbcqJQfLV-kG4Mt7_G_BAEhlgwS_ynlMOwF1Ti6jnFOe3FIllOjA1p5oUdqsl3u2_mR7O42yHj25eJOmy9HIfEz6IRFIr8-nGTe_ktRmod8Yw6a3u8fWSVRZXkrJspBet8d72RpcBjzFYDzRJgPhWEgBJhgtoN-ru19at5qZ3BxYdem9ZsLN6ftyRo3xsZ1votlXn9Q2q7asfgNU9r25k4sq2xWUmECU-6pE31RF8BqYL4h2ODU2pprgEZ-Wgp75MBma9QMm7WVCq6DUUX0CXUVZRHzAsU4ANnFvnV8UVpQZPy9lijUkV2iQjvFL8VDp9NuNYVMQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ: من اعداد نظرسنجی عالی دارم.
🔴
من هر نامزدی که دارند را با ۲۵ امتیاز شکست می‌دهم
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/129236" target="_blank">📅 22:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129235">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزارت امور خارجه ایالات متحده می‌گوید که «گفت و گوهایی» درباره برگزاری مذاکرات با ایران در واشنگتن دی‌سی از ۲۳ تا ۲۵ ژوئن داشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/129235" target="_blank">📅 22:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129234">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ترامپ : تجهیزات دفاعی و این چیزها رو داشتن
🔴
ولی هفته قبل نمی‌تونستن ببینن، یه شب ۲۵ تا کشتی داشتیم، یه شب ۲۲ تا، یه شب ۱۹ تا
🔴
یه شب ۲۱ تا هر شب همین‌طور… همه اینا. برای همین مردم می‌گفتن : این نفت از کجا میاد؟ کسی خبر نداشت
🔴
ما ساعت ۱ نصف شب حرکت می‌کردیم، همه‌جا چراغ خاموش. و نیروی دریایی‌مون هم فقط نفت می اورد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/129234" target="_blank">📅 22:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129233">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507cc3233d.mp4?token=sBeJF2b2fxdSNmLoqJI1tarOhaz5GOCf5k1WHLzXffmO2Tae5agBkCw4Zut_SiidkfAE6MV-5nW-2XONHzYgMxmr14rJSniS6pDSMRTnxrxb3-MVrtUySaHpLEUJl85Z8E5-3wDEDYOLtX-9kqyXQ57GzIWdp1jBMfCAQt0kJOZbLWmONkBYlAZnF0jg3RmNT5o2IxTvhRi7i1SPOo9wEn-lQ_r5MjPddx7UNDobFMEd069H5sYcHNmzbkb-sZkhcVjQ7OxRLszuPnaL9-vEr8RSPm0CTCamOBXixftZPYSwBUufao-JoNKEym_XUmhFhdR4JUxcKah_OT3DPn8kJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507cc3233d.mp4?token=sBeJF2b2fxdSNmLoqJI1tarOhaz5GOCf5k1WHLzXffmO2Tae5agBkCw4Zut_SiidkfAE6MV-5nW-2XONHzYgMxmr14rJSniS6pDSMRTnxrxb3-MVrtUySaHpLEUJl85Z8E5-3wDEDYOLtX-9kqyXQ57GzIWdp1jBMfCAQt0kJOZbLWmONkBYlAZnF0jg3RmNT5o2IxTvhRi7i1SPOo9wEn-lQ_r5MjPddx7UNDobFMEd069H5sYcHNmzbkb-sZkhcVjQ7OxRLszuPnaL9-vEr8RSPm0CTCamOBXixftZPYSwBUufao-JoNKEym_XUmhFhdR4JUxcKah_OT3DPn8kJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره بایدن: مردی داشتیم که نمی‌توانست از یک پله هواپیما بالا برود و من نمی‌خواهم در این مورد صحبت کنم، زیرا اگر کمی لنگ بزنم، خواهند گفت: «آها، این فاجعه است.»
🔴
خوب، ممکن است اتفاق بیفتد.
🔴
اما نمی‌توانید هر بار که روی صحنه می‌روید لنگ بزنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/129233" target="_blank">📅 22:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129232">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا: روبیو به جوزف عون تأکید کرد که ضروری است حزب‌الله خلع سلاح شود و دولت کنترل خود را گسترش دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/129232" target="_blank">📅 22:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129231">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ درباره تنگه هرمز: ما الان تنگه هرمز را کاملاً بسته داشتیم.
🔴
همه جای آن مین‌گذاری می‌شد، و موشک‌هایی بر فراز کشتی‌های میلیارد دلاری پرواز می‌کردند. آن کشتی‌ها هرگز حرکت نمی‌کردند.
🔴
ما برای ماه‌ها نفت نداشتیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/129231" target="_blank">📅 22:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129230">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
هم اکنون پرواز بیش از 9 هواپیمای سوخت رسان آمریکایی بر فراز تنگه هرمز و خلیج فارس.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129230" target="_blank">📅 22:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129229">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ: طولانی‌ شدن جنگ علیه ایران، جهان را با رکود مواجه می‌ساخت
🔴
طولانی شدن جنگ علیه ایران برای جلب رضایت تندروها در آمریکا، ممکن بود به رکود جهانی منجر شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/129229" target="_blank">📅 22:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129228">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5a5d29a6e.mp4?token=IqrTcUgrP7WpoJsY1KvM5P20mgwU88wLDgRTehbRqEiJrpBsmnT55fH8hoOWzbiV7zvluMWMjEKtgESNQXRwZ_zM8bt5IMBRHKzgeAqveewbmanDuLgtI3zlY1QkgLbOZoo07MD-a04AZytCouUuoI0eOMTURRwWJuk1bqbBG-8tEq83CIR0loRvVP_igafpi2L5_d3_dDB0G16xKX9BlGdBp8AjXnpRuN5L96ulroUt3ucVxSMXiFyo2cA7Ggqe4kySaCHxmDN2YO00uMULqo8GelLXky-EK35V5XbLYjgzDgY60J58k5bCdLEDPXoQobNoJbUwL5k1XzdxHO324w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5a5d29a6e.mp4?token=IqrTcUgrP7WpoJsY1KvM5P20mgwU88wLDgRTehbRqEiJrpBsmnT55fH8hoOWzbiV7zvluMWMjEKtgESNQXRwZ_zM8bt5IMBRHKzgeAqveewbmanDuLgtI3zlY1QkgLbOZoo07MD-a04AZytCouUuoI0eOMTURRwWJuk1bqbBG-8tEq83CIR0loRvVP_igafpi2L5_d3_dDB0G16xKX9BlGdBp8AjXnpRuN5L96ulroUt3ucVxSMXiFyo2cA7Ggqe4kySaCHxmDN2YO00uMULqo8GelLXky-EK35V5XbLYjgzDgY60J58k5bCdLEDPXoQobNoJbUwL5k1XzdxHO324w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک کاپوتو از اکسیوس: این چه تغییر رژیمی است که‌ انجام داده اید؟ شما خامنه‌ای جونیور (جوان) را همچنان در ایران دارید.
🔴
ترامپ
: خامنه‌ای جونیور با پدرش متفاوت است. آن‌ها افراد متفاوتی هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/129228" target="_blank">📅 22:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129227">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b8850d1df.mp4?token=PWmgK8QyQ8hfIffG4_BRog8Z1g_7yqOGlSz7QSV-VIHbyahPoslWEbEvzuMiR1ZEGtjvRnlXBu2MJo7Coq-L_9x92-PBxgmkKsgj5DTYiB1g2vJUzT_9vFLGrgb7k12N9yk9lfX8fBNd5qgqEqxh0ZMKOd7nyz6uC7KguzRyqVkNPvCw-57aOxwSfNNhKcLIriqeql0DMxG1JwHT9AEDQkPc2WHYYYz8FZup4XOz0RevkbxRQlArbQRFH4lK2N93vtlSyxwuJEAxM4ebLekXAEXAiwrTqhnWHPUZNg4l2YQ4yFjoIqCmbkScm00t5FFIwfzLKSbU0vN2qwKkDtjDkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b8850d1df.mp4?token=PWmgK8QyQ8hfIffG4_BRog8Z1g_7yqOGlSz7QSV-VIHbyahPoslWEbEvzuMiR1ZEGtjvRnlXBu2MJo7Coq-L_9x92-PBxgmkKsgj5DTYiB1g2vJUzT_9vFLGrgb7k12N9yk9lfX8fBNd5qgqEqxh0ZMKOd7nyz6uC7KguzRyqVkNPvCw-57aOxwSfNNhKcLIriqeql0DMxG1JwHT9AEDQkPc2WHYYYz8FZup4XOz0RevkbxRQlArbQRFH4lK2N93vtlSyxwuJEAxM4ebLekXAEXAiwrTqhnWHPUZNg4l2YQ4yFjoIqCmbkScm00t5FFIwfzLKSbU0vN2qwKkDtjDkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره حمله به پل B1: من بزرگترین پل آن‌ها را نابود کردم چون دیر در یک جلسه حاضر شدند. آن‌ها گفتند که کار خیلی خوبی نبود.
🔴
آن پل، [همانند] پل جورج واشنگتن آن‌ها بود. آن را در سه دقیقه پاک کردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129227" target="_blank">📅 22:20 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
