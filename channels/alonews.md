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
<img src="https://cdn4.telesco.pe/file/bwzWoeNmdeEjwCxKik2NSpr3oUcLFZ6tAhxG0mlJL0KVCPRIldBauPe2Rr-IsBg72NfzSCSRwc6HJHJjGEiBCDklW2-ImQeDk4NOSc8FyYJmhnypxrf7HiQm7QTscl8NKKTlhkboKyo0TjrJmLNYz29VXIenynyNz5E0OLJfY0A5Xv0dLdvNBnJdyqxoi149nrvf7H-qNGV2C5bRYyhKgZfIBJf8ccFwe8hIWxXV-XC_Kq6J9R1VHyo3nhla37uaEboG7qhX_Zssu1vryPBOXUoLagvqBvQxk6HuL7a2xFdkPEh6HMlvwrEs2F2wmuPtAg57UQ8NsVgL5eZFD2XfNA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 981K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-02 19:34:25</div>
<hr>

<div class="tg-post" id="msg-143570">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kA8d-0TiwmzFM59YZeiVA2amg2IeA291KxnDnqnqyiPrwxadDSa5DWRsuJ41QlWco2FrSQ7pvbcFCnRtY2PV_dNFgUsY7Z0GZ-ETe7Bpu5VchalFhsgwRT7_c0BD331axxzPsFMDOTqETl4qRexW7f3z8Z4XX6t2Ca1TMCLv9lbLy2K5Ycjz637Lj-NCWYNYsv039g6OYREwBRT45iFlRELS01MC23nO9QemxDcX5eMz3G9Nvu7P0yGYgIXz5A8OrH8sMBTlDIvWAegrvfYsMy2udGSysoIO3xfbnRj-_Zn44IWdOPBsNyz1Xgghg5z_daUKFJMehx-bIn3Dxq6Nhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان، عصر امروز با محمدباقر قالیباف، رئیس مجلس دیدار و گفتگو کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/alonews/143570" target="_blank">📅 19:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143569">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
الجزیره، با استناد به یک منبع نظامی یمن، گزارش می‌دهد که انصارالله یک کاروان نظامی متعلق به نیروهای سپاه کشور در مناطق العبر و الوادیه را هدف قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/alonews/143569" target="_blank">📅 19:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143568">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
معاون اول رئیس‌جمهور: آقای قالیباف قول داده طرح مقابله با نفوذ را از دستورکار مجلس خارج کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/143568" target="_blank">📅 19:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143567">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
الجزیره به نقل از منابع آگاه: ترامپ هفته گذشته با فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان، تماس تلفنی برقرار کرد.
🔴
ترامپ در گفت‌وگو با فیلد مارشال منیر درباره موضوع ایران رایزنی کرد و از او خواست از نفوذ پاکستان برای ازسرگیری مذاکرات استفاده کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/143567" target="_blank">📅 19:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143566">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
آذر منصوری، رئیس جبهه اصلاحات: آقای سقاب اصفهانی نگران خرد شدن شیشه‌هایتان‌ نباشید و عاملان قاچاق سوخت را معرفی کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/143566" target="_blank">📅 19:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143565">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c0d58c62c.mp4?token=VRCeR2ruvs3l-68khBWC2cv-oBo0Yi944iei18-wx5h_3OT0GHV7_vgy35nlLV6VJDOQDtHOXovhruRdnK1-GkN_3owFHMtq_Vd9As0fgUWAVUtWSsqverQEMRfyYYpJOADGN5kgJ5IjF0y36r_L-o-yBi3qB0SieM4EFfeNk4ISJ0SJ26TIoXe_uttz7xUF8XfaNc9ySI-jD4U6b70ZZwrBFiz4dZJ6dNIr7c4VxWV4-NGCVlaY7tKqAT7wsGFhkf3dsx1n6B0TrOOAjSqTNypgxHVmeNQnZHY5nMaOy5hyHTxFUXNFcl_Cm0cAJvTvzFSqimFVkKZkHvxyDk-q5T5CD-sVD2fDZ-znS2_p9maXp6NeQD-VhYv7Cpiu-lf3ZoMvaI7f9p26ksRFls3nMpD6NK5-MUde0WhTf_c3E5ifmsCrPaEuelS526p-6IMe1Ma_u5yNOK8c4897-xNlQsuf69tNsSz0JeHeaoWmx4aexnJLChhufNpueF42mS03Pw7WsZwsVU3WDT-8w9KvdLRlg2YnbfDwtGRFjHUnCuLqp8OEwKhHFoTLD5wsgr7x2aJbBxW7ded2TtLDyr02GdtFsa74zLcz0_5PWpEGPr_R4CTPqsb4SFrk0I7uhlK4OBcrH1hc3ijSVsgoPH0ynTwHH9NQqLerFy_X0L5jsB4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c0d58c62c.mp4?token=VRCeR2ruvs3l-68khBWC2cv-oBo0Yi944iei18-wx5h_3OT0GHV7_vgy35nlLV6VJDOQDtHOXovhruRdnK1-GkN_3owFHMtq_Vd9As0fgUWAVUtWSsqverQEMRfyYYpJOADGN5kgJ5IjF0y36r_L-o-yBi3qB0SieM4EFfeNk4ISJ0SJ26TIoXe_uttz7xUF8XfaNc9ySI-jD4U6b70ZZwrBFiz4dZJ6dNIr7c4VxWV4-NGCVlaY7tKqAT7wsGFhkf3dsx1n6B0TrOOAjSqTNypgxHVmeNQnZHY5nMaOy5hyHTxFUXNFcl_Cm0cAJvTvzFSqimFVkKZkHvxyDk-q5T5CD-sVD2fDZ-znS2_p9maXp6NeQD-VhYv7Cpiu-lf3ZoMvaI7f9p26ksRFls3nMpD6NK5-MUde0WhTf_c3E5ifmsCrPaEuelS526p-6IMe1Ma_u5yNOK8c4897-xNlQsuf69tNsSz0JeHeaoWmx4aexnJLChhufNpueF42mS03Pw7WsZwsVU3WDT-8w9KvdLRlg2YnbfDwtGRFjHUnCuLqp8OEwKhHFoTLD5wsgr7x2aJbBxW7ded2TtLDyr02GdtFsa74zLcz0_5PWpEGPr_R4CTPqsb4SFrk0I7uhlK4OBcrH1hc3ijSVsgoPH0ynTwHH9NQqLerFy_X0L5jsB4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عوستاد ... چشم:
محسن رضایی حریف ترامپ میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/143565" target="_blank">📅 19:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143564">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
حملات هوایی اسرائیل به جنوب لبنان همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/143564" target="_blank">📅 18:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143563">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
اداره ملی استاندارد افغانستان مدعی شد ۱۳۹ تن کالای ایرانی شامل مصالح ساختمانی و دیگر اقلام، پس از بررسی‌های فنی به دلیل «عدم تطابق با استانداردهای داخلی» اجازه ورود به بازار افغانستان را پیدا نکرده و به کشور مبدأ بازگردانده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/143563" target="_blank">📅 18:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143562">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwgyZLknMYPjDyPU_NQR9isI6zdDOovRm6q1ywWPnmck-nJ11n7cpbTN5zaldgI9otrTd52VsFjaUgUm4RFzYsdV68wEehgxh8e5Nf7ySB2BGXNXP_52oQLKhCCx4WHZdDJ9yaXaWMA4uatSmXIUzke1Sw1ccBbjDW5AnprmfdPj78b5tyBFHyT1yT-ydc2XwlhNpSwhyUNDRuRMUP0S_rCef6FYsGauteV-CKxKjyGZ9rqIlZYP5SJN6XXpaRZxNzGW_gkyrGCVLKFRrIwbvYVX7zfcJE7Uc4ottSvwpQbVPgW6AJuL8zJG4L0bItJtIyboeg-Wx7-CWgJ3LKPV6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دوگ فورد، وزیر اِنتاریوی کانادا، به خبرگزاری آسوشیتد پرس گفت که رونالد ریگان به‌خاطر سیاست‌های تجاری ترامپ «دارد استفراغ می‌کند»
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/143562" target="_blank">📅 18:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143561">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سخنگوی سپاه در واکنش به جنگ اقتصادی آمریکا: جای هیچ نگرانی نیست برای هر اقدام آمریکا سناریو داریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/143561" target="_blank">📅 18:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143560">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBZfzLCytRQ45xDjQ1hWJIX58lYIUX0GryFdmYUUiriIJhNDM4-eheryUS9J7IsNlVOLKIdrqqpTi_u_ScxgOHsp9U526sCjBgxwu4HO-Nv1jgQskQU3Ae3BT2c6L0Rl5k-1m70PLTlmjiSolGCh92dH6K0fvboskDMHI8Vd25oOtvD_MyEVjwcFU8MrMFzq4algJ7bU3Z4mmq29Mi1zJ5I1_WFRw1nhD7WaeQMFkX9NkuuVAEXKjeoYDVXuCg7HlzxQ5D2qBagxB2Qm-hvVHVw1dDvkxU7yD0yDHdpAoVGjvhdZT8wnmQlgR1_XXTNJCxPkRJfs3GqNcavjMqQQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مکرون قانونی را امضا کرده است که استفاده از تلفن‌های همراه در دبیرستان‌ها را ممنوع می‌کند.
🔴
بر اساس گفته‌های او، این اقدام به «
بازگرداندن آرامش به فرآیند یادگیری
» کمک خواهد کرد. ممنوعیت استفاده از تلفن‌های همراه در مدارس متوسطه از سپتامبر ۲۰۲۵ در حال اجرا است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/143560" target="_blank">📅 18:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143559">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dR-NdoVn-d2JWVXIuDISsXtQLVbg8qOnZxR4Ngr9P3OC9z2U_OFxnRgd4tTWOBM1le2kN-w1fC2FEUs4OIoEY38cqEfweJvcJXS2Wl_907Lf8qJ29IjuVUdrxWkn3u4rpEgoHCDtrt0CXHHhE6CHEBqhwdqt2GQHkgDR2-0fuH1UbRmlR3TD1FAxtITJmSTfUq08EVr5k9___U93LZvjypvddodJB8vEyM4upEByMX1qy2iVBJsmDp-KQNpRaHBhhKFv1u_K6RD5JAG3kHPu73L2MAQS-F27nHrREl0PQIMs4f-t5_NdkE-URLFm8qMthK16zHdkypApo0MRiZ6l4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: «مدیران خودرو» بابت هر خودروی وارداتی، به طور میانگین ۴۷۰۰ دلار گران‌‌تر حساب کرده/ ارزی که «مدیران خودرو» طی ۵ سال از بانک مرکزی دریافت نموده، با ارزشِ کُل شرکتِ اصلی چینی (چری) برابری می‌کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/143559" target="_blank">📅 18:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143558">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سخنگوی سپاه در واکنش به جنگ اقتصادی آمریکا: جای هیچ نگرانی نیست برای هر اقدام آمریکا سناریو داریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/143558" target="_blank">📅 18:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143557">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed7c35d2e7.mp4?token=JvpzChnshqaH24miP5VdEhKI-QhP6UQaoFnsYsV5P7eF5tRUb2OF-RIkLnQMtnJznh-HuUIgqorHYoYNIIm4WE_RuTvI945SbY0aYaSC6jnKe4boKy3rpIx736DmxRwLlg2j-Njx73JQM9w1YZ0t_m5nKOJNX5GUsT_ZRhDDD36JJGi5BFvZyQPc7UZZVb-YrP06cZy2RjIliY5ryfCScrNR8HLuQLzu7rMR73evkNnjzetZulOOTIdw9yJYLJhEPKpIh7ScB-mqdD3t4_XyXFQhk1tYTSxPITpGmioF6kXk753LeDnt1hT8Nm0DEwVLY6PDhsiwZu6_j9AWnMDPCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed7c35d2e7.mp4?token=JvpzChnshqaH24miP5VdEhKI-QhP6UQaoFnsYsV5P7eF5tRUb2OF-RIkLnQMtnJznh-HuUIgqorHYoYNIIm4WE_RuTvI945SbY0aYaSC6jnKe4boKy3rpIx736DmxRwLlg2j-Njx73JQM9w1YZ0t_m5nKOJNX5GUsT_ZRhDDD36JJGi5BFvZyQPc7UZZVb-YrP06cZy2RjIliY5ryfCScrNR8HLuQLzu7rMR73evkNnjzetZulOOTIdw9yJYLJhEPKpIh7ScB-mqdD3t4_XyXFQhk1tYTSxPITpGmioF6kXk753LeDnt1hT8Nm0DEwVLY6PDhsiwZu6_j9AWnMDPCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بعد از حمله حوثی‌های یمن، انبار‌ سلاح ارتش عربستان و نیروهای وابسته در گذرگاه ودیعه در آتش می‌سوزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/143557" target="_blank">📅 18:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143556">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
یمن: یک کشتی سعودی را با بالستیک هدف قرار دادیم
🔴
نیروهای مسلح یمن: نفتکش امزان متعلق به دشمن سعودی را در نزدیکی بندر ینبع با موشک بالستیک هدف قرار گرفت که منجر به آتش‌سوزی در کشتی و فرار تعدادی از کشتی‌های دیگر حاضر در منطقه شد.
🔴
این عملیات در چارچوب تصمیم نیروهای مسلح مبنی بر ممنوعیت تردد دریایی برای دشمن سعودی و تثبیت معادله محاصره دربرابر محاصره انجام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/143556" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143555">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: وزیر امور خارجه تأکید کرد که گفت‌وگو، دیپلماسی و اجرای تفاهم‌نامه، راه تحقق ثبات پایدار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/143555" target="_blank">📅 18:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143554">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
دلار به ۲۰۰ هزار تومان رسید؛
🔴
از ثبات ۷ تومانی و قدرت ریال در دوران پهلوی، تا سقوط بی‌سابقه و نابودی معیشت در قهقرای رژیم جمهوری اسلامی.
🤔
یک مشت حرام زاده دزد زندگی چند نسل رو از بین بردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/143554" target="_blank">📅 18:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143553">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
شرکت ملی حمل‌ونقل دریایی عربستان سعودی اعلام کرد که کشتی امزان، متعلق به این شرکت، در دریای سرخ هدف حمله قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/143553" target="_blank">📅 18:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143552">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
خبرنگار الجزیره: جنگنده‌های اسرائیلی ۲ حملهٔ هوایی به شهرک المنصوری و مناطق اطراف آن در شهرستان صور، واقع در جنوب لبنان، انجام دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/143552" target="_blank">📅 18:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143551">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
رویترز: ایران ۴۵ نفتکش را به‌دلیل نقض مقررات عبور از هرمز در فهرست سیاه قرار داد؛ این کشتی‌ها ممکن است جریمه یا توقیف شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/143551" target="_blank">📅 18:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143550">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
رویترز به نقل از یک منبع گزارش داد:
وزارت خزانه‌داری آمریکا قصد دارد دامنه تحریم‌های ثانویه علیه کشورها و نهادهایی را که با ایران تجارت می‌کنند، گسترش دهد و فعالیت در برخی بخش‌های اقتصاد ایران را هدف قرار دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/143550" target="_blank">📅 18:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143548">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kmnGQOWC5YPQxyKOoR0phZT551j5Tg8UgQkqv_U_xHpAIdbGNRWHExQ3bvkFIByGktLmFBOm5AiuEfVjRfBEru0f0KVG0V4Bc5hCeUjWIZUQlE8zJqCJgk0DdfixSuCIqEc6nF3XO-z3o2y3cA52e0QSwtiIX6OpK2aaMcZh2YJPtvwfxwBg1eXQdsXOPJcWHdmgs1y7MqKDxYVTWCRyeDhNoHEiBWaOwwKxGyH_f6CqnDXxO7ddx04FIQdPyWcHhZFs5l8DpZUng6kSK-t8byVAocRgImjT24KJyY0lNuE_zOkSuaYoNdsb-7L23rtsbK83FUVOudWl6mu1MErpXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1SvJKcqOJcAEMfP6TJuqi_93OstEXF3VY50DmV3MHwTYTbunNWRrS0aWV_AcO2UPOWQWcHfLgkDkfySxsjubpJQgQo0Cicxdqg8CjaoKBoa2GPwEjffqEtwWKPBqSMytHGu0EWK15_IAprVV49LXL44RZY8rE2k4-IN_KOMjdhGAmTNvtBG5RxTVLiW1wx_Cwc9of1uLFRN5yX_9Po061tey6hxe6xgFTGqRux_zSfTcY7xtzNaIPglmni8l3KXlnEJ3BCNYTvK6MhEWRFf6-vCWcikEShrI8gnDYMLlqHntdBk6vBqt_Pa-m9DYPwZLgTE2snxuv6RrOf949YzpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جهش قیمت‌ موبایل
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/143548" target="_blank">📅 17:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143547">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otpffSDHGOO8vF8tAOgVK_BRkt3YPvmR5uf8gPNPMheJkEeKJPOy3P7OgmXnTUYKgi3nv1h9STuqPW4i7CSDJPI5xuvSzhZEM9YABORxxfrKiFdnb2LbPwRAVoZJJyxGwu9gcbr8TQxrJ8gmNpzae28KO2a4rIE7HOhrlDhsw_8JZvcRJqCqR5eeyrFB80yVs96ElQXafTjatHWxcTU5o7d013CfDxCXWJijb7FmGBkyx585c4zYXnekoWIPYxh97aU97xu6RRrx0V_cabX2wxmkSlICRxeFimJfqj8ntYFdbJzczEN2kTiW6c-AORN9ixGDT0B8_zoZZ0i-g7YwcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی خطاب به بسنت: ایران نیابتی‌هایتان را نابود می‌کند و اقتصادتان را به زانو درمی‌آورد. شما و آن فرعون، به‌خاطر اینکه مردم آمریکا را گرفتار این همه رنج و بدبختی کرده‌اید، از سوی خود مردم آمریکا نفرین خواهید شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/143547" target="_blank">📅 17:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143546">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3dnEo89qDUF6inpzN_J-dEyVjQalAlFXAA9Qbc02YYAYlQ_LUhu6sL6H_QdF2Y8UlHrVZyMy6gPDFuy_5CgSfm6MrZCmg330Wy-lTI5u_8c0lEkv8dq8gkNkAaf5EXS55F5V1APkVZ-BodwtNcjCAyQ6U6571KnBUAYYuQlJZTU8RAUgEGdRQiB-Ldx1hSRWE3j_h94aLTM7azju1NUs5l1adCXt2qdOqKkorUWbuxgFq38nEe8rbxbp6iGKe__qd20VoeocnEBP376-mCKGa9O3oQEnO9GN-bZt-XAM7467HljttqrTKnCV9QcYb8W9cHWbj581ogzJrNEHtCzrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لقب مجری شبکه سه برای محسن رضایی: «سرلشکر فیلدمارشال»
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/143546" target="_blank">📅 17:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143545">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/280cc51c55.mp4?token=BDDgQCR4KBNFYaLAvYNrqlla9aZXo7IilCbw8OaJshscQU9qG5ybEvQ83w8N3MX1gX-8VywVtbATTjbjh8bDYkjKvUx5MyWYo1ip4BrfhKE2zf7dh2YH9ojVogqFtniGDHpbs6mHUuLQF6HGi1DxmisHVGZeEZY6uEN0j4AunBn_AlRosxlwhebLMTDLNlc3NrW97qfyq0SC6uH-iF4U-33HvQiI1yndKdXk7SEA85tEPP-miC9mZqQRxVetw6FC-Xi4IOOnlrBjFQSA8Q9YuLwSStvEnlVNGikOuamwnzXAWP_W37PEDBDjirdK8wW1Nx5dSyqI2d-Xf7_DPwsGmq3ryVN8amiRrnNVT_ebcVjCSRLZH7L2lDZI3VRkFPVH-3_mGZqPowDoQQ-CHdjFWQWvbTaDCSgbUOnnv3HVKdWv3Ct4LxeYoVVkMc43o2-umFLaKv7lam2p3CP5r-Je3HVrBDzVcA3_6VjxEm5vNfuwOwLQW8myq4VFkkSJGXVCjbWU4EpCgSi8Sc6IcogIcSd40tbENWgBXqm1ZvC3c69nw_2d6XDHLhDFm-hA5x7mZ_qvp6vx8QnmZWP1LYCSQi4PMQwlG6Aif-9eZA-GP4P3o9thq6lRRJ3sT1jDrMS1bCOATXYx-k9K4dFe_Rl6FLKGdSyUvTOnT41queF0uzo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/280cc51c55.mp4?token=BDDgQCR4KBNFYaLAvYNrqlla9aZXo7IilCbw8OaJshscQU9qG5ybEvQ83w8N3MX1gX-8VywVtbATTjbjh8bDYkjKvUx5MyWYo1ip4BrfhKE2zf7dh2YH9ojVogqFtniGDHpbs6mHUuLQF6HGi1DxmisHVGZeEZY6uEN0j4AunBn_AlRosxlwhebLMTDLNlc3NrW97qfyq0SC6uH-iF4U-33HvQiI1yndKdXk7SEA85tEPP-miC9mZqQRxVetw6FC-Xi4IOOnlrBjFQSA8Q9YuLwSStvEnlVNGikOuamwnzXAWP_W37PEDBDjirdK8wW1Nx5dSyqI2d-Xf7_DPwsGmq3ryVN8amiRrnNVT_ebcVjCSRLZH7L2lDZI3VRkFPVH-3_mGZqPowDoQQ-CHdjFWQWvbTaDCSgbUOnnv3HVKdWv3Ct4LxeYoVVkMc43o2-umFLaKv7lam2p3CP5r-Je3HVrBDzVcA3_6VjxEm5vNfuwOwLQW8myq4VFkkSJGXVCjbWU4EpCgSi8Sc6IcogIcSd40tbENWgBXqm1ZvC3c69nw_2d6XDHLhDFm-hA5x7mZ_qvp6vx8QnmZWP1LYCSQi4PMQwlG6Aif-9eZA-GP4P3o9thq6lRRJ3sT1jDrMS1bCOATXYx-k9K4dFe_Rl6FLKGdSyUvTOnT41queF0uzo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لقب مجری شبکه سه برای محسن رضایی: «سرلشکر فیلدمارشال»
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/143545" target="_blank">📅 17:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143544">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ad49a3037.mp4?token=CbEttH_FOHGM4Yta5VHiRwdErfdp6mK9nBJTk2RLdbCrRu4wramKR4PrQHE2HN6xXq_IQy6WmiwcXzkm4iBXvhQikrSf7VSaPZ9RfPBTosW92majf7vQ9KzlZe4phcCQAe3gCbIlM0OHu5ZpMt9FSsXx39h3TKKg_0rtLgqyPzguTOpzNLZEhTY-v88NDdtsq0U-ZVxwWa02Rq9qJv3vJSiAqyludUCE2ebMENWKVVqElsbNxTWKZfsfg43Agacs5eRSBnCB0ydDC2PfR_yrmIn9Ku8RcBU5IAgq5NpUSh1c5mC1wYdyzV3u0bLr3VIdSLKtROGcfwd8Qh0kxsSTXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ad49a3037.mp4?token=CbEttH_FOHGM4Yta5VHiRwdErfdp6mK9nBJTk2RLdbCrRu4wramKR4PrQHE2HN6xXq_IQy6WmiwcXzkm4iBXvhQikrSf7VSaPZ9RfPBTosW92majf7vQ9KzlZe4phcCQAe3gCbIlM0OHu5ZpMt9FSsXx39h3TKKg_0rtLgqyPzguTOpzNLZEhTY-v88NDdtsq0U-ZVxwWa02Rq9qJv3vJSiAqyludUCE2ebMENWKVVqElsbNxTWKZfsfg43Agacs5eRSBnCB0ydDC2PfR_yrmIn9Ku8RcBU5IAgq5NpUSh1c5mC1wYdyzV3u0bLr3VIdSLKtROGcfwd8Qh0kxsSTXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوثکام (SOUTHCOM) اعلام کرد که نیروی مشترک مأموریت‌های نیمکره غربی آن، در روز یکشنبه به یک کشتی مشکوک به قاچاق مواد مخدر در اقیانوس آرام شرقی حمله کرد.
دو نفر از مظنونان «تروریست‌های مواد مخدر» کشته شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/143544" target="_blank">📅 17:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143543">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3b8e92ec8.mp4?token=ErzWFHGce0Jf7ChPMJm6Dcl0rRwoofkTycxgsC3LR-OzJhgfIbJOQoBOIAQuU2MPb_ZTRuphPKqOeRq16B7MK15PbMXGgktAjfFAGb9MiL1ct3I33uts62Hmg_mdKrXjqSKTW-B0pvuWoz0yNfxOpMpHiyaJ837WSYHJzqxsWb37uNV-XRlODWCEsqdKb7tYECksWaGZgkW26wIdUbmQUbCD1I3IksmngZoRLlfJwoq2JsuqIZLHRrA89-PwcGYlQ0L5S2beU0BhLKoxOJFKn4Tpt_5B-xc7Qm5iGQnvVKtmSGJwC9vteOvdLFlgbci8-lZkMQYlgkXGRxc8lojPeX3pCD1S60ueIScAfbUjTEliXMLmeT88vpqUlcBXDT9yRu5u4Mw5ovpAPQH1U9nFS_iOIJvzdDZEYAp4xAAold4h2glYBC5jB-MeASWmkRlB6DvnfHbMD5yDdpbSMn1C5nyRIo58k2ijmEPbgBsj0F32xn88Vc_YjWGj7_NaTGII9uQv88MgqDwNzW93B3GMzgwD6Xo19lE3-72PGgxtem2Pl9XbfROjOPJC6GdyHcurGkA_Q7xwGPlOgbVUoGmmMaJlW8xt2o8xdci1FrTXdz1UzkfndiRUPia4ScmqjIkyBYJBJNdqdqcjfbFm4OmtYfQ-QuuB97LVy-lVnLdqETY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3b8e92ec8.mp4?token=ErzWFHGce0Jf7ChPMJm6Dcl0rRwoofkTycxgsC3LR-OzJhgfIbJOQoBOIAQuU2MPb_ZTRuphPKqOeRq16B7MK15PbMXGgktAjfFAGb9MiL1ct3I33uts62Hmg_mdKrXjqSKTW-B0pvuWoz0yNfxOpMpHiyaJ837WSYHJzqxsWb37uNV-XRlODWCEsqdKb7tYECksWaGZgkW26wIdUbmQUbCD1I3IksmngZoRLlfJwoq2JsuqIZLHRrA89-PwcGYlQ0L5S2beU0BhLKoxOJFKn4Tpt_5B-xc7Qm5iGQnvVKtmSGJwC9vteOvdLFlgbci8-lZkMQYlgkXGRxc8lojPeX3pCD1S60ueIScAfbUjTEliXMLmeT88vpqUlcBXDT9yRu5u4Mw5ovpAPQH1U9nFS_iOIJvzdDZEYAp4xAAold4h2glYBC5jB-MeASWmkRlB6DvnfHbMD5yDdpbSMn1C5nyRIo58k2ijmEPbgBsj0F32xn88Vc_YjWGj7_NaTGII9uQv88MgqDwNzW93B3GMzgwD6Xo19lE3-72PGgxtem2Pl9XbfROjOPJC6GdyHcurGkA_Q7xwGPlOgbVUoGmmMaJlW8xt2o8xdci1FrTXdz1UzkfndiRUPia4ScmqjIkyBYJBJNdqdqcjfbFm4OmtYfQ-QuuB97LVy-lVnLdqETY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عده‌ای امروز مقابل استانداری اصفهان تجمع کردن و گفتن با بی حجابی برخورد بشه
🔴
پ.ن: نظرتون راجع به اینا چیه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/143543" target="_blank">📅 17:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143542">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سپاه:
از این پیج هم رد میشیم و به قله میرسیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/143542" target="_blank">📅 17:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143541">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd22d38c95.mp4?token=v1-_sPDux1LUzuMJbZAsqkDVfwQXxwYulQcVUF9UC5XThdkdfViqPWmd9NLiPHTLCcuVUOxvjIX-_HF1fBQx3vfPZvzSUdvoG0Lx5v9O6zXE7jYRTwxE9Qyx4PR3wW85IpQfAov_VdCDExGnaeGJoG-EBEEBghSRL1Y6Qm5Cxx3uTC4idZBGsgYIqPK3kcBbX1CVYxs3nEAnqxhF5s5U8DzuolybHGYWyjzxKrKtJ9yg1oEKWPvRCpXC8HRruZOk58Rv2MnRPmIbvt5__KOsqZkvXbA9UcQiTSZWoENO205vxXT6luZpnFWH8iLG__j7GF5OpFkwS47y3RIcL9Wlakaw6ozY-PK7ilYy7Vp71S-zTFivUzVpuPVp_2Mii5Ef9cQSrXuFu7h5aQzP1yGv3T-vyKJl4bjUpcCyjDXmQ8dnwgOBcZ_2DtNl0uXpdBKPilK5Mz6k9CxkAQVxHXeGOPeleZMhFdHwNauot83_xwnDmretN5QITWf2sJOwJTzIhOjmXCUuU_U22p9ANr94j73vOuWWKz9GJbw6KVXcwlgfSbysYq3CPF2v0zNhqcPBZzDVNmtl2_qHJlYNbo_PpUEoOQvoZEfGzcKsAZx_dpSzIA_2mdddz3H9Toe6DQfxzN-2BVL3YNMT_Chj4O4qn9hmkjsSe3_9kc8QVcHxYlc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd22d38c95.mp4?token=v1-_sPDux1LUzuMJbZAsqkDVfwQXxwYulQcVUF9UC5XThdkdfViqPWmd9NLiPHTLCcuVUOxvjIX-_HF1fBQx3vfPZvzSUdvoG0Lx5v9O6zXE7jYRTwxE9Qyx4PR3wW85IpQfAov_VdCDExGnaeGJoG-EBEEBghSRL1Y6Qm5Cxx3uTC4idZBGsgYIqPK3kcBbX1CVYxs3nEAnqxhF5s5U8DzuolybHGYWyjzxKrKtJ9yg1oEKWPvRCpXC8HRruZOk58Rv2MnRPmIbvt5__KOsqZkvXbA9UcQiTSZWoENO205vxXT6luZpnFWH8iLG__j7GF5OpFkwS47y3RIcL9Wlakaw6ozY-PK7ilYy7Vp71S-zTFivUzVpuPVp_2Mii5Ef9cQSrXuFu7h5aQzP1yGv3T-vyKJl4bjUpcCyjDXmQ8dnwgOBcZ_2DtNl0uXpdBKPilK5Mz6k9CxkAQVxHXeGOPeleZMhFdHwNauot83_xwnDmretN5QITWf2sJOwJTzIhOjmXCUuU_U22p9ANr94j73vOuWWKz9GJbw6KVXcwlgfSbysYq3CPF2v0zNhqcPBZzDVNmtl2_qHJlYNbo_PpUEoOQvoZEfGzcKsAZx_dpSzIA_2mdddz3H9Toe6DQfxzN-2BVL3YNMT_Chj4O4qn9hmkjsSe3_9kc8QVcHxYlc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دوست پسر دختر رضا رشیدپور: مردم دلار ۱۹۰تومنی هم براشون مهم نیست اما دلار ۲۰۰میشه همه استوری میزارن
🔴
پ.ن: جوابتون به این
کصکش
چیه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/143541" target="_blank">📅 16:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143540">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsMQcDW0NpXkry3GQCvzIuAzAI3ZiXLiHPejNgT71FrNYQ-HLvleZK0OQVI1dajbz8f3m_fDBdflhBwcOnko3VnXFsEpmBbIy6KAW32tYTXl_TjrVYiAynUVDs00sVeF9O0aUZeOB1QIp5GabLbJbmsN2fqhI07P2UFHRoh3-8ifGeWBg0GEZLKgnxVsTLjSy5c9Wanh5OtWcv0X6gOilkaVPxVO5Gqsa3ZC3PQBwA_8s_3ZeM7DZCX1NICe_G-Edsbr1kJgnJUocTlX34ZvoCTg_VaudtnBGMlRJ4VgFBSMyPZ64q0AX_dGGJNsNBxaKnjYPzveC0_NQxRLtZiigA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی:
مقصر گرونیا همتی هست
🔴
پ.ن: کصخول فرض کردی ملتو؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143540" target="_blank">📅 16:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143539">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpK2aTtxLQpGWZ9TsDgswxB9BfaC9hHqHQ2XV0ujVWAhkEfjyx85YgHecML-ANi854ENeubuUYHVAe_2VeArV28K2CvTxhnAdi1HULRhWddbRvJ4SSkuZFFV45xPYVKPE5gV8Hz-uSOWxlK1Ly7J0wuobSiPIH8V01HryPPG0rQW54Vj8xovMT6kF8-6eRRfL5iFrmIEOCv2OvMI0P1Y0iDaz-2UwzYiaAqvmsbxbiYYQIGx08eNk8zG94ZueNz7fqDnVSOnvhhhLYyEpr2nGAn12ZmG5J_1iT3WXWlcypdU7ggschvE-Ty9LQm9qyYIYg4_LLnSvZciJf_yMxjGWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: ممد سامتینگ(قالیباف) گفت ما گشنه‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143539" target="_blank">📅 16:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143538">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRBeHGygpBUZh3Qrw0iUXLIoLqYSehsPwmiEvLuPClijFfTIT6a_RdaVMlXft2UcCKHwgqkwuq2G4zLrjwJJfOirGX-9udIZbU-6LF4_YqEF5ENdxC8g6ek5QPfcqXtSpXNQa__-QmANDHR-lNcGIqY5ayCuEPVwc2W_7h4SFl7CsEgiK3GvnVIEIZAVM_edWBH0wn2YZFwWZmOaF7GfQwjASTeZMIUDflsAJE1cy307RhitkXiSPuRDJ_6Lw7qkZVjLxD-q9fjtoi7vBlml1yzxiELc1A4JceN4nVdZDOcQfJtJUMz-gYJJfkvdgLUz34d1f9_ub64Y8c6uWamQmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
ایران به طور کامل در حال فروپاشی است!!!‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143538" target="_blank">📅 16:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143537">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=kCfyDikUCt_pc9B5ZUC9CoKluvnoNFgDh5BQw_NWPVTC6lQRgSMbZkq4dkUORih8OTlswwN9EWk64KMYK-Mcb0K61tPVhL1q_QOr37Fncx7vxxVw6yXpxuzDBp2j-hbO-1-PwsKAc2Zj152gIdtBomdgdshp4ifPrdOztEpQaIbTg8IfH_OR5OPdK_Bwdqh0-am3mmF0JDozcZJKTDLggPSE8FD7_7bQdbSFe7-7nOb1wQboyisa2JpQX8DzMdg9z3VdcHP3e0KKUZMmUC-1PI6w3SZnGGF1llS_9eS1VeAMummY-Nz5OAgT71lxIkUEzXNw6oFBuwVufXzV_roE_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=kCfyDikUCt_pc9B5ZUC9CoKluvnoNFgDh5BQw_NWPVTC6lQRgSMbZkq4dkUORih8OTlswwN9EWk64KMYK-Mcb0K61tPVhL1q_QOr37Fncx7vxxVw6yXpxuzDBp2j-hbO-1-PwsKAc2Zj152gIdtBomdgdshp4ifPrdOztEpQaIbTg8IfH_OR5OPdK_Bwdqh0-am3mmF0JDozcZJKTDLggPSE8FD7_7bQdbSFe7-7nOb1wQboyisa2JpQX8DzMdg9z3VdcHP3e0KKUZMmUC-1PI6w3SZnGGF1llS_9eS1VeAMummY-Nz5OAgT71lxIkUEzXNw6oFBuwVufXzV_roE_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هر گرم طلای ۱۸عیار 22,900,000
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143537" target="_blank">📅 16:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143536">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/16a65d9f01.mp4?token=X0K1GxoETofhCh7RcRRBM_gDPh3A58AwiiN-rX5lb5HdGZwVn-XjVlYfTirr3a_4RqXVJS22hX4ZVtKqz7-_Lj1DPUtKCvuiqFHzVURVuwfDC4zFDdkF29BaGdfktYZ-RD8pThs1yHdlRS4QhVaIWeRMLEhEOB5W9982y_KuR3NJLtpzLdk1mSUlv10Hstyor29JQbLNPihRnta8lfSnRC2P5zPEUbjpDJdO3MRT0xzMUD26bTSviYqd3lNfQDNK7bh9heL8uQG4DhvmaGshh4hu53Tz-YyF5kbKQXFLgcWK8PepjuXl2DVqXvyf7S5nLaYuEsVhx94prJ7HACGXdw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/16a65d9f01.mp4?token=X0K1GxoETofhCh7RcRRBM_gDPh3A58AwiiN-rX5lb5HdGZwVn-XjVlYfTirr3a_4RqXVJS22hX4ZVtKqz7-_Lj1DPUtKCvuiqFHzVURVuwfDC4zFDdkF29BaGdfktYZ-RD8pThs1yHdlRS4QhVaIWeRMLEhEOB5W9982y_KuR3NJLtpzLdk1mSUlv10Hstyor29JQbLNPihRnta8lfSnRC2P5zPEUbjpDJdO3MRT0xzMUD26bTSviYqd3lNfQDNK7bh9heL8uQG4DhvmaGshh4hu53Tz-YyF5kbKQXFLgcWK8PepjuXl2DVqXvyf7S5nLaYuEsVhx94prJ7HACGXdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به تازگی توی بالاشهر تهران، یه رستوران ساختن مخصوص شوگر مامیا.
خانمای میانسال جا افتاده و پولدار اینجا جمع میشن و پسرای جوون و خوشتیپ هم میرن اینجا، تا برا خودشون شوگرمامی پیدا کنن.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143536" target="_blank">📅 16:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143535">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔥
🔥
⭕️
یک هفته پیش دلار 200  تومن رو پیشبینی کردیم و کسی باور نکرد!
و دلار امروز به 200 تومن رسید
.
ریزش مجدد تا 155 تومن را اطلاع دادیم باز توجه نکردید.
دیر نشـده هنوز،  بیا اینجا
👇
پیشبینی های ماه آینده رو اینجا میزارم.
👇
👇
👇
مجدد نوسانات چشمگیری از دلار داریم
😳
https://t.me/+eonSdwsppnIxMGE0
https://t.me/+eonSdwsppnIxMGE0
کاملا محرمانه(ارز
ودلار )همگی سریع واردشید
⭕️</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143535" target="_blank">📅 16:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143534">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIotExb1QuvWZ3RuJG6JhVOFfQWXNCN5kBI3fZezm6LcoGsEO5BUguTr7TYwOsbtxTrT7f61IRnIOD4YveFUhfOxzCI3rc4xEvIxQUBpzYOsphiJeRN8RswMRQgO48qdd3HbqFFA5qM8qByF32wvbj1L8HcdwXzy4zPfoO6Zy6YUYo6vlSdV4IWBLxf0w9H8uZAjyJ9DSbQUwfXieE-kXpet0e-fBq_wyba4Tr2Itit1ziVW0zDm2m1FkWU35X7PYwoXig5SGFnHrSZ0-JQndewgJ6un_B3HadKiwwvLpmb5j4NyMoMGq6LrOca_RubgU0jKeevL5BiB_H60xWzOHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند نفتکش با مالکیت نامشخص در غرب بندر ینبع در فاصله بیش از ۱۰۰۰ کیلو متری از یمن هدف اصابت پرتابه انصار الله قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143534" target="_blank">📅 15:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143533">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
اختلال شدید GPS در تهران؛ مسیریاب‌ها دچار مشکل شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143533" target="_blank">📅 15:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143531">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
رانش زمین در محل دفن زباله در کوناکری، پایتخت گینه، باعث کشته شدن 31 نفر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143531" target="_blank">📅 15:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143530">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zd5kFnI7JOQZJlQI3ifyYeNeuCaEadqfap_6pEsLfiSTK2Ts4QwT0eLhlZqgaNSceOXRFVTdbU4qGn3Hv-HFz46AUn53C-8tY9MO6pB6ObEHn9Z76mByX1rbhmhAGpLGe7hrD0BdeMU1lMFYr1Je36z7fbkyHcDnbcNUL2aOl38F2angFK_FP4AyIhRLMiB5Y3qwxXoPNy27LRqtX0EeFCs0EHHNrTa5TexxHvl3cGQXzk3h7awu6_Pb0MDwbjsjwzS2C4Yj1hiiBRbSx2Mb3eoc79nv8uoAcLkZ4ZJkIesiQ9ng_73m61_AGHkDjnZMaZ3xX_H1tfw64sVSDEvB5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آصف شیبانی، وزیر خارجه سوریه:
دفاع از حقوق مردم ما و ادامه کار برای بازپس‌گیری کامل و بدون کاستی آن‌ها در تمامی عرصه‌ها، وظیفه‌ای مقدس است که با اولین فریاد آزادی آغاز شد و بازتاب آن هنوز محو نشده است و تا آنچه شایسته مردم سوریه و جایگاه تمدنی و تاریخی آن‌هاست، ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143530" target="_blank">📅 15:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143529">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiM1rWpyPMdzyDYkFLiFqGbhjl1q3PiaIkH0NMP5Y5fDcgdZfsGNfKRKD0iGQNlqovkBv0tm7Z9kFH7KFQ7fGYBuz_UwL-Dd3nArpETG-dn44Wa9BVi5dpb7FvLZTJP1O2zvHDig9YegTFF29QtXY3IykrmqH7JWRsb7OjRHdBoKzhKM7eKxvkCBRq7c_SURCMX-kcgvArT8EMj-eL5eq-DjXpUgQNRvYP_Y1es7A3nHOjkhY-djjP1tNm60e3tFnjUV_zFxRYkK6wukUT4V8XUn93PMlKbLOh7ZBZpzYr9uyPzhCUd95aLWNmRTcYCFw6D5hMCwHQj7nNOkOJht5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنگنده های اسرائیل لحظاتی پیش دو حمله هوایی به المنصوری در جنوب لبنان انجام دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143529" target="_blank">📅 15:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143528">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
مرضیه دستجردی دبیر ستاد ملی جمعیت: حدود ۱۳ تا ۱۴ میلیون زن و مرد مجرد در سن باروری در کشور داریم که نیاز به حمایت جدی برای ازدواج دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143528" target="_blank">📅 15:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143527">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJo8E5NwoxohEe7Opx9QfBFdndTy0pYCzxYKThIdYzs8az4DzxlQkjOndxrTB7eSk4vsvAR2ZL-72bJ_FL0fk9rgjMNyPFBwSWvwEntH4_MS5XKQTVcL4DaTocjaXssE1rvrnQjthneReXIlfJhwp2U_e-VoDe3kCqxAznvSJ-KuafOZfkF_WILNgFrHyd7lk3-Ee4ktxjiLTsl-8qZiHvJDqUeOOdPpwZQbNZ-52HqCNnryK7lNA7S6VDUTS3sZTxYniknoJdw0y19BTaIs-BRn8c4DJSikwnnWgELmW20PuES73kDY4DljiiNcAO-0pB2jXo0ALg0tnzo6_v5h_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قطع برق کمیسیون انرژی مجلس هنگام بررسی علل خاموشی‌های اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143527" target="_blank">📅 15:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143526">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ارتش اسرائیل از ترور دو تن از نیروهای جنبش حماس در منطقه دیر البلح در مرکز نوار غزه خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143526" target="_blank">📅 15:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143525">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZIF-dEGMNuT3sW2tjL5guhB-7--4HuNHNlEE2bzbkGtS1F-PcxC0l3SvBFFAoApRwIr1sgGfCttZC6MlQM3EUhkeLZLCGQO5dkfOEMhLFqsOs4Nx7OfOkQNFAc7cxEO8Kt9JLkWhIV48F7yBc-bjRKe8jeBFq6xtbQMjxVW6HePS4lrGWimkeOFxTmwe6mcAcmdw1oAQ2iAIpHD92Nis1B8HRUSr49kVoNXpuFleogtfHPXBEaoQr9uxgquCf8yYgGd-V8Yq865JEXemKYtmU_cYZpNJMUwpGY3m82JVFMkiMKMFxa10naqksr5-HKXxmh_VFqTrmNsdtfoAtExrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: آمریکا را دوباره گرسنه کنید!
🔴
نمی‌توانید شکست‌ها را با ادعاهای دروغین پنهان کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/143525" target="_blank">📅 15:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143524">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
همتی: قیمت دلار در روزهای آینده کاهش خواهد یافت
🔴
تهدید تحریم ۱۰۰ درصدی ایران رجزخوانی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/143524" target="_blank">📅 14:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143523">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
مدیر اکتشاف شرکت ملی نفت : میدان گازی تازه‌کشف‌شده به‌تنهایی می‌تواند تا ۱۵ سال گاز کشور را تامین کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/143523" target="_blank">📅 14:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143522">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
دیده بان ایران: زنی که می‌ گوید همسرش دیپلمات ارشد وزارت خارجه بوده و در یکی از کشورهای اروپایی مستقر است، در حالی که او را ممنوع الخروج کرده، نه راه تمدید پاسپورت را باز می کند نه راه طلاق را به او می‌دهد
‏
🔴
این زن تهدید کرده در صورت ادامه این وضعیت، نام این دیپلمات را فاش می کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/143522" target="_blank">📅 14:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143521">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7420f2b14d.mp4?token=ZaQziG0d37I-lWR_dtlf2zC4h4Cy2wXBiQEwFbXoKQk19bY1_NE6yerVgymdQRzvEpAMu8IJk0P6rMIYmzNZu5S96hdGj95a0wSGUqjcifyFj3gVTP3Tss-09_R_rKIMr8fNRPJivsVfiXKwlolwYIohUTHsxHFkVLl6lSv0hlmqyeMDp0D3WDBsfHz-T3X1DUKLDhKfJDwxAxQ8WzeezOccrnqk0kfs7nqSqcdWX19lP-E0d0VceUfBpWjLg3uJor9M_Bu2WskPWLgm_NE3cdfitmK_u8MxpjStp05WCu--drI920qhwxLa6d3GHmlbzJnq6rrWlbAhlkT85t5-gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7420f2b14d.mp4?token=ZaQziG0d37I-lWR_dtlf2zC4h4Cy2wXBiQEwFbXoKQk19bY1_NE6yerVgymdQRzvEpAMu8IJk0P6rMIYmzNZu5S96hdGj95a0wSGUqjcifyFj3gVTP3Tss-09_R_rKIMr8fNRPJivsVfiXKwlolwYIohUTHsxHFkVLl6lSv0hlmqyeMDp0D3WDBsfHz-T3X1DUKLDhKfJDwxAxQ8WzeezOccrnqk0kfs7nqSqcdWX19lP-E0d0VceUfBpWjLg3uJor9M_Bu2WskPWLgm_NE3cdfitmK_u8MxpjStp05WCu--drI920qhwxLa6d3GHmlbzJnq6rrWlbAhlkT85t5-gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: وظیفۀ ما خدمت به مردم با هر گرایشی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/143521" target="_blank">📅 14:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143519">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bb7af662b.mp4?token=L8d473MvzfRK5xRdDcg7QvWljOAvOe-evTN_Q2GwhCG0MaFrEG-iO6j6ATNwDGANFauTXMVVzfuJwlKQpa94P_tSyZXpl_e0aK728s-HZ-bZCzlUEf_IZD3EHFfs0m_4TSD6jomvpdDnCBSK72paGXAXZ4VLm9wLo43PiXzoukGm9fmysrR2QNcoRjxDadGETn_Ry2Q69jQGoiDvRctk8hSpzapTVAv_ouZ0SAGWjr1y_vDiJmyZRtlsMVbfwJQzLiZIApWonbLjDx9lGOWcPtQmHwIAHBnL_TBLY0h9uuHO38WsC6gKg0VLkHcQz2AYKI0LlJ6wKd67SbZq3h7YNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bb7af662b.mp4?token=L8d473MvzfRK5xRdDcg7QvWljOAvOe-evTN_Q2GwhCG0MaFrEG-iO6j6ATNwDGANFauTXMVVzfuJwlKQpa94P_tSyZXpl_e0aK728s-HZ-bZCzlUEf_IZD3EHFfs0m_4TSD6jomvpdDnCBSK72paGXAXZ4VLm9wLo43PiXzoukGm9fmysrR2QNcoRjxDadGETn_Ry2Q69jQGoiDvRctk8hSpzapTVAv_ouZ0SAGWjr1y_vDiJmyZRtlsMVbfwJQzLiZIApWonbLjDx9lGOWcPtQmHwIAHBnL_TBLY0h9uuHO38WsC6gKg0VLkHcQz2AYKI0LlJ6wKd67SbZq3h7YNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دوباره حمله روسیه به فروشگاه ها در اودسا
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/143519" target="_blank">📅 14:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143518">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏
👈
زمین‌لرزه‌ای به‌بزرگی ۳.۴ ریشتر در عمق ۸ کیلومتری زمین، پل‌ سفید مازندران را لرزاند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/143518" target="_blank">📅 14:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143517">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lH1VLpA40sQhfBUVmvJgrBoqOVpsUsEsXuatCd8PnR_Ah7tGnPPWQeE6V7mRR0dIFxoCyfPKKTdopugvrfwce4zGKtiuFFM2EnysYIRWQDhgKo6iKLT-4ZXQEsTg9A1j8giVxjKU__3yjHXUtgRFYY7rueqbnVOPj8D3tsp7-TOE11F30a1ZIHeFnJbb6O6Uf6Zqq2nHDkmY4t9JkFcJG6bFNxGFwliZ76QB-HehMQ90LPATpqHSVFTcEEL_efmEpCgeP3_UZlSI8wSy-U3WorXs7A8NX6ZWuwTlfYBV3lYf3H2A5uURTD4Gf3J0DtK7Iif9_19NdGHH--cv-mZD5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هر قطعه قبر به ۱ میلیارد تومن رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/143517" target="_blank">📅 14:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143516">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏
👈
اژه‌ای: درباره اصلاح قیمت بنزین اختلاف‌نظر وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/143516" target="_blank">📅 14:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143515">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
انفجاری در نزدیکی اداره منطقه در شهر پالمیرا سوریه رخ داد و گزارش‌هایی از کشته و زخمی شدن چندین نفر منتشر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/143515" target="_blank">📅 14:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143514">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
هیمتی: بالا رفتن قیمت‌ها در بازار ارز براساس هجمه‌های تبلیغاتی و جوسازی آمریکایی‌هاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/143514" target="_blank">📅 13:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143513">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
رئیس کمیسیون اروپایی اعلام کرد که ۶.۱ میلیارد یوروی دیگر در سیستم‌های دفاع موشکی، مهمات و تجهیزات راداری که اوکراین به طور فوری به آنها نیاز دارد، سرمایه‌گذاری خواهد شد.
🔴
به گفته کمیسیون اروپایی این تعهد علاوه بر طرح‌های تدارکاتی مصوب قبلی به ارزش مجموع ۱۶ میلیارد یورو است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/143513" target="_blank">📅 13:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143512">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9XoQ5mAfhp5I2RsoLyFYFJdI-AytaNlI1qhTFT7ZlVGL6X1-oyM3joyFNlnuhf8JcyZZ3gE9Vg9R_UJFW9y6O5727ZDh-HUe8m8jhDqwjCGNho99oJlCeOqQ1UYWD8rosJ7svquLBMTtqg5mSAEt3OLzlyFHobrSmZpbcxvDwAaWE37-Mg4BBAstCdY8dt6B03ZYQdiWfPdRXI3Hsre-sdXa9-DZQrPAD6orIqvPavyQac1i7DVyOQNlKlZwxVV2ri5UW8Jsw-1lURcjGALZNjWucCTm-LYupr2XfqN740YKugQDKeSNJu-snsan70ftse3YnNBMZ5drJGKvKg4rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاشینیان: ارمنستان به‌زودی روند درخواست عضویت در اتحادیه اروپا را آغاز خواهد کرد
🔴
ارمنستان قصد دارد در آینده نزدیک روند درخواست عضویت در اتحادیه اروپا را آغاز کند.
🔴
به گفته نخست‌وزیر، ایروان آماده است تا روند رسمی پیوستن به اتحادیه اروپا را آغاز کند و پس از فراهم شدن مقدمات لازم، این موضوع می‌تواند به همه‌پرسی گذاشته شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/143512" target="_blank">📅 13:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143511">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u86l2HZnxDAsGDCvEBmSvjaSXVngqNPEzBr0Y-siZ2Pz0xQIO--mtcWfqZgGEjvPq5WCO88j7gmpIp7q6GMiEtN2B7cPtZd2-wHXNNVEPX8eIbc5hGN3NspnrG8DSc70oYKw8SeT1gkst7S7YFdOn2qkQlMrk_-jH4AgCDrS8_3JPl14gpUGxF2pwR_QQqI_-9Ry-w_PdP89N8zIynh9rk7S2uWtPN6XK4LW5FB7jsonmR_ZEo_bFn6OhVyRFCg9mLf4e1W8zQ2YLR4fdY-i0d1ANKvWU8IlTXW-nmGsABKne_NcUb6qp3F4IlNuyZ2HHnQuV9ti7cZMtnctMRSFeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهر: ترور یک بسیجی اهل سنت در زاهدان
‌
🔴
یک بسیجی اهل سنت به نام «نادر سارانی سخی» توسط گروهی مسلح در شهر زاهدان ترور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/143511" target="_blank">📅 13:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143510">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
رویترز به نقل از یک منبع پاکستانی: واشنگتن از عاصم منیر خواسته بود تا از نفوذ پاکستان برای بازگرداندن ایران به میز مذاکره استفاده کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/143510" target="_blank">📅 13:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143509">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=APsVT_AGDOiZ1paZ_SnZS2nUio_EMW41N-DQYGNLwlW-UXhLCVHRPlVv5NxmQgI1BXYeZW62-HTJB2UxFosn_vQJIRx_NzJsp6uuvTIn2JIFpuO3v06IqDh7O-ZpzWQPIEU4CJ47Y1wa2M2uVEcdApOe_xVrgpAdJh-k_BYPIGSXTw5HBz4ga3BliWRK3KEfou4VffRSMYXl4P5xPoalYiSOCLZ92IAFnl2wNIQJg4AlUVHupgGUkfQeQZdefMQoSqBIsniU2UeCZBIrQZ0mNsXmYEu92VQkNbPaTVwctFLJxj9nNDNWjmn2vP3KiTiLwNz79Y-SDkRV0ccvzoyQ-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=APsVT_AGDOiZ1paZ_SnZS2nUio_EMW41N-DQYGNLwlW-UXhLCVHRPlVv5NxmQgI1BXYeZW62-HTJB2UxFosn_vQJIRx_NzJsp6uuvTIn2JIFpuO3v06IqDh7O-ZpzWQPIEU4CJ47Y1wa2M2uVEcdApOe_xVrgpAdJh-k_BYPIGSXTw5HBz4ga3BliWRK3KEfou4VffRSMYXl4P5xPoalYiSOCLZ92IAFnl2wNIQJg4AlUVHupgGUkfQeQZdefMQoSqBIsniU2UeCZBIrQZ0mNsXmYEu92VQkNbPaTVwctFLJxj9nNDNWjmn2vP3KiTiLwNz79Y-SDkRV0ccvzoyQ-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دلار در بازار آزاد 204000تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/143509" target="_blank">📅 13:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143508">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
دلار هم اکنون 203,000 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/143508" target="_blank">📅 13:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143507">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d7c61107.mp4?token=iffoE6emBTgY6rRrUijep2PNLNbjs1JCq-BZEurVJJfB69AThI0W83-2Ln537G22RvV-I0V8qHOHY3h-qZbTwVKC2X42K-nbSPmWriKEh2uBXneD3wRWyRjsv8z5M_XBz5KepfkeZIgHsbjFGPRwYBaYwp9pco3r5HoIee0aNbCFeVCi6S0dTMpCSPxm_f3moI1mTxvaa4vbfrZK2jTRxTXl4MjFtKFFoty4nRFbDhe1BUgGPZQjw_c23zHVnrQnjinXbyOz5pLqTE6KEbgHHhke4fhqTTH6xoXV17HMmGrz6caQsANCnFywngsvUlhUU1I6yNburgPTdvLShgA-HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d7c61107.mp4?token=iffoE6emBTgY6rRrUijep2PNLNbjs1JCq-BZEurVJJfB69AThI0W83-2Ln537G22RvV-I0V8qHOHY3h-qZbTwVKC2X42K-nbSPmWriKEh2uBXneD3wRWyRjsv8z5M_XBz5KepfkeZIgHsbjFGPRwYBaYwp9pco3r5HoIee0aNbCFeVCi6S0dTMpCSPxm_f3moI1mTxvaa4vbfrZK2jTRxTXl4MjFtKFFoty4nRFbDhe1BUgGPZQjw_c23zHVnrQnjinXbyOz5pLqTE6KEbgHHhke4fhqTTH6xoXV17HMmGrz6caQsANCnFywngsvUlhUU1I6yNburgPTdvLShgA-HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو توی کمپین انتخاباتی به‌سر میبره و شماره خودشو منتشر کرد و گفت هرکی دوست داره بهم زنگ بزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/143507" target="_blank">📅 12:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143506">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
رئیس ستاد نیروی هوایی اسرائیل:
ما در تمام جبهه‌ها در حالت آماده‌باش و آمادگی بالا باقی خواهیم ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/143506" target="_blank">📅 12:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143505">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ارتش پاکستان: سفر عاصم منیر به تهران در راستای ارتقای صلح و ثبات منطقه‌ای است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/143505" target="_blank">📅 12:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143504">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awhe4GwSoQdCPwbBhI8bYQkXenppDEMIIqtWVJK0Gcp3_HWcuTe2SHmDdUrKq4EVTPYHLSlTQw-M-SpPtaEI_gZifhrzxlvbt2l5vjpi46_Zk_tWhxvRD_lO2CSpDDA9WaDpiyL_yY2E78HT-Ge9GsNgYlauH_zUY2hAuNQyx5zKK5QJmXMAfmK77QQtVu55v7Ot-iRiqxVsy1KMCL0fdIp6g72AxCdRN6160ht6kc56Yimaj85jUAXJu2BizPTco8qSwISX6nXtx6Wv84ZQOPS9rzz025cnmKZNW_a-ur_wnmsLIe-oA44Q-a1b3qdmZ7voCR-lT6Pe1i6Rpum4nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوش‌چشم، کارشناس صدا و سیما: ارتش آمریکا به زودی بخش‌هایی از عمان را اشغال می‌کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/143504" target="_blank">📅 12:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143503">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a6d46d5c3.mp4?token=tSTdazu74dhK51sID7eIbiV8wlUTJH7sipSi_583j7Xc_C4mqMibKXnYBB4PTD1u6-TDni2DGPkKg3j74MUt0zRkXqYVWtOoaZfthv3Az1c6wGaBWjjPyerzUxdwW9EAW57Tig25_DQZVuPxSBmhVcjWW6yv4DdvSyGH8fet3_wI5EDBWogId4SNBXTBrDP9fBG89RcR_Ocn692uVObbOjI412yLcHZ5FFHD5r9MoycX0i1anVBfWngSs5EJcAa57KbmvsL9Lu6Ogjk9UhA3hq--G7PS_bHgSigkjONYkZA9lvTrgSks9Kc4Jsmwnk07xiVkZakef6rNcbZs1oxUsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a6d46d5c3.mp4?token=tSTdazu74dhK51sID7eIbiV8wlUTJH7sipSi_583j7Xc_C4mqMibKXnYBB4PTD1u6-TDni2DGPkKg3j74MUt0zRkXqYVWtOoaZfthv3Az1c6wGaBWjjPyerzUxdwW9EAW57Tig25_DQZVuPxSBmhVcjWW6yv4DdvSyGH8fet3_wI5EDBWogId4SNBXTBrDP9fBG89RcR_Ocn692uVObbOjI412yLcHZ5FFHD5r9MoycX0i1anVBfWngSs5EJcAa57KbmvsL9Lu6Ogjk9UhA3hq--G7PS_bHgSigkjONYkZA9lvTrgSks9Kc4Jsmwnk07xiVkZakef6rNcbZs1oxUsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکندر مومنی، وزیر کشور در فرودگاه از عاصم منیر، فرمانده ارتش و محسن نقوی، وزیر کشور پاکستان استقبال کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/143503" target="_blank">📅 12:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143502">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
تسنیم : عاصم منیر فرمانده ارتش پاکستان دقایقی پیش برای دیدار و گفتگو با مقامات کشورمان وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/143502" target="_blank">📅 12:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143501">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
تسنیم : عاصم منیر فرمانده ارتش پاکستان دقایقی پیش برای دیدار و گفتگو با مقامات کشورمان وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/143501" target="_blank">📅 12:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143500">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
دلار هم اکنون 203,000 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/143500" target="_blank">📅 12:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143499">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6zzBS_nhzGiqVeJ0NKeZQu7C2Zc7Zu4EM1R5_wlSS67dWDV-yUqINhutEai1lLG7JMy8h9v54t4AHcN9KLFeXVWLr3-1ODUwYlPGBM08gwBMzgUrSjRJk79HYtM6uJPweTEUeP4EZ7jak83EiIx_60J42Tqp9nA41K_0NlnJEkjgMMbYA5SKXSCCkjLYfr6me7wX2_9fylPR25kTWT_8ab6Mf9Y22tq5zHeeVkfA-4WIpkP7aw-MkT063CL3xZDFwmLklBerb8MTAv3ujsnJEYmockRUEt-Sx8E62wFQA96cwcNPUzPIC6AN4hsU-axC24VrY4yAZFrB3w3HFZRKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازنشر سخنان قالیباف توسط ترامپ با عنوان «ما گرسنه هستیم و توان ایستادگی نداریم»
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/143499" target="_blank">📅 12:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143498">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فووووری / رویترز : فرمانده ارتش پاکستان پس از تماس تلفنی با ترامپ سفر خود به ایران را لغو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/143498" target="_blank">📅 11:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143497">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فووووری / رویترز : فرمانده ارتش پاکستان پس از تماس تلفنی با ترامپ سفر خود به ایران را لغو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/143497" target="_blank">📅 11:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143496">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83496bb820.mp4?token=b5v0L8zPNINxeu03B9tEpjJ4EvCk0X6w40qBE0Up7_FiAlsG5mbLyPP1aA4AxtrfKHJs_0wXOkQm3G8K3rgBS20ideIx8HKSo_96RZmQdksLzBSDk6eceQ5vYQL1Ue3VZZp4Wx2MsHb_KXw4qHHobM2ly99x-D0EpIsWiW_r5PpexX86J2bGRHSBbEe7MlL0hzHwQuKUilMcN0eRLyffIRDbZi_rB8ybhjVsN1LrVPxGio0BlSZW_0a2j24APFW3YfwKeFeFqtOFkU5vtWzmOGyhznaEXL_RsqfXiAo-hlQkaORONPep79GeR6MTapSGf3ydTRucHm_e9oVjeYT2jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83496bb820.mp4?token=b5v0L8zPNINxeu03B9tEpjJ4EvCk0X6w40qBE0Up7_FiAlsG5mbLyPP1aA4AxtrfKHJs_0wXOkQm3G8K3rgBS20ideIx8HKSo_96RZmQdksLzBSDk6eceQ5vYQL1Ue3VZZp4Wx2MsHb_KXw4qHHobM2ly99x-D0EpIsWiW_r5PpexX86J2bGRHSBbEe7MlL0hzHwQuKUilMcN0eRLyffIRDbZi_rB8ybhjVsN1LrVPxGio0BlSZW_0a2j24APFW3YfwKeFeFqtOFkU5vtWzmOGyhznaEXL_RsqfXiAo-hlQkaORONPep79GeR6MTapSGf3ydTRucHm_e9oVjeYT2jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
سقاب اصفهانی معاون رئیس‌جمهور: هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌هایم را خرد می‌کنند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/143496" target="_blank">📅 11:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143495">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
بقایی: ما از قدیم شطرنج باز بودیم، در سالای اخیر پوکر باز هم شدیم، الان هم مدتیه که ترکیبی بازی می‌ کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/143495" target="_blank">📅 11:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143494">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ca4bf0018.mp4?token=pcDy3ZLYYdUiwxpoe8ZPC_hCqI6RYHlAWyB3eungaJvpXdLFq3VAxKr2kVvWzMBsqLkEati6YFyAU9xKgXAUw5phFj5guh8pYAftwEZ-3OAbJHLhDuXPBzWlnG_cSs4dWDYnmNgyjdFXBN5qOx_SY1UdpLrvoAve7Cr2pmankeejUcjIHpal2uo-2gibOk5q1xn6nj9wOqwAFo8dDp2MgYr11io686hj5KmlnawcrufPQ_j5yKpPnEVbb_KmPkWR69JkyqQrrRE-2UxEHQNT-lVTtMhRyZ-c5AjE7Eprj5rYqMm2DR9bNL1N4D3Og-3tYKSmVwqcLN-iq3NHoF8Dhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ca4bf0018.mp4?token=pcDy3ZLYYdUiwxpoe8ZPC_hCqI6RYHlAWyB3eungaJvpXdLFq3VAxKr2kVvWzMBsqLkEati6YFyAU9xKgXAUw5phFj5guh8pYAftwEZ-3OAbJHLhDuXPBzWlnG_cSs4dWDYnmNgyjdFXBN5qOx_SY1UdpLrvoAve7Cr2pmankeejUcjIHpal2uo-2gibOk5q1xn6nj9wOqwAFo8dDp2MgYr11io686hj5KmlnawcrufPQ_j5yKpPnEVbb_KmPkWR69JkyqQrrRE-2UxEHQNT-lVTtMhRyZ-c5AjE7Eprj5rYqMm2DR9bNL1N4D3Og-3tYKSmVwqcLN-iq3NHoF8Dhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه در واکنش به خبر عبور روزانه چند میلیون بشکه نفت از تنگهٔ هرمز
:
جنگ روانی
آمریکاست و صحت نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/143494" target="_blank">📅 11:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143493">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRoxMlV9UNTMCRpPM9zqm-ZM2GiW485-8l5THJo8KFPyCDr-wGMyb8K0UzQ6BwyosCRPDVa07tnaqhb7Tsvly61FjjjyDP9XKxqf3GJiv02PtRIz9P20a2V5LWi49UpHXrssx4HNV4JXvuy1Pc2ddGPh6HudsT2sfmdxm8XyaI5BWLRfFQtfWDwiBAq6zqUXAPqptbM5hOOV6t1x810Ax4BvLUsEzot2Udk4KpUkVlpAv1a_2bmxPHPZ6Tfb1qn6aIpacvwm5mLfTw1SgpWB7hGy6VHGLZGkhXWR-9Mwftr9R9CVTFU_SmFYxC7dvzH4jFTimlR1byYKwLf06QLCTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدا و سیما: ذخایر نفت خام آمریکا تنها برای ۴۱ روز دیگر باقی مانده است که پایین‌ترین سطح در نیم قرن اخیر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/143493" target="_blank">📅 11:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143492">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه درمورد گزارش‌های مربوط به خروج هواپیماهای سوخت‌رسان آمریکایی از بلغارستان: در مورد بلغارستان ما مواضعمان را از قبل اعلام کرده بودیم. ما هم شنیدیم که چند فروند هواپیمای سوخت‌رسان «کی‌سی-۱۳۵» (KC-135) بلغارستان را ترک کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143492" target="_blank">📅 11:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143491">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فوری / سازمان عملیات تجارت دریایی بریتانیا (UKMTO): گزارشی از وقوع یک حادثه در فاصله ۶۳ مایل دریایی در غرب شهر ینبع، عربستان سعودی، دریافت شده است.
🔴
یک نفتکش در غرب ینبع بر اثر اصابت یک پرتابه ناشناس آسیب دید که در پی آن آتش‌سوزی رخ داد، اما هیچ‌یک از اعضای خدمه نفتکش زخمی نشدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/143491" target="_blank">📅 11:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143490">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه درمورد گزارش‌های مربوط به خروج هواپیماهای سوخت‌رسان آمریکایی از بلغارستان: در مورد بلغارستان ما مواضعمان را از قبل اعلام کرده بودیم. ما هم شنیدیم که چند فروند هواپیمای سوخت‌رسان «کی‌سی-۱۳۵» (KC-135) بلغارستان را ترک کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/143490" target="_blank">📅 11:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143489">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وزارت خارجه چین درباره اعمال تحریم‌های آمریکا علیه ایران
🔴
تحریم‌ها و تاکتیک‌های فشار به حل مشکلات کمک نمی‌کنند.
🔴
پکن از آمریکا و ایران می‌خواهد با عقلانیت عمل کرده و خویشتن‌داری کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/143489" target="_blank">📅 11:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143488">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1beabef1e6.mp4?token=GPeVGWBJpr7mcK7x5ezwQ4ydwqIF6GN90Ce311dUv2NceOpaSpjGMJwAG8XUHlzKDQ2ZhjHWna8fGXgyb1ka7d_OMJqa1ors--lLro_nRj2HCInbs3UMxgj8vod_YgVWabb_XpkcZFK2Iz-Xxe6Tfhr9C4WGbcMZTWJgf-DBqJNf4YDJRnG4jBY_nc-NH0j_-9mnVCptv5dU6ejPj6Vqwc6CP8NCNtD2m1GdeEtmdBpO3avJp9JcV8THWYyFTdJQbqNsCR4FMagHM2TVynIs-6efk6yKbb1m48trwKuLuPjS6FPIL3J7FORsE2pDDrA_6DtVXqf99mQXUS2a5KRraQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1beabef1e6.mp4?token=GPeVGWBJpr7mcK7x5ezwQ4ydwqIF6GN90Ce311dUv2NceOpaSpjGMJwAG8XUHlzKDQ2ZhjHWna8fGXgyb1ka7d_OMJqa1ors--lLro_nRj2HCInbs3UMxgj8vod_YgVWabb_XpkcZFK2Iz-Xxe6Tfhr9C4WGbcMZTWJgf-DBqJNf4YDJRnG4jBY_nc-NH0j_-9mnVCptv5dU6ejPj6Vqwc6CP8NCNtD2m1GdeEtmdBpO3avJp9JcV8THWYyFTdJQbqNsCR4FMagHM2TVynIs-6efk6yKbb1m48trwKuLuPjS6FPIL3J7FORsE2pDDrA_6DtVXqf99mQXUS2a5KRraQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی پربازدید از وضعیت ترافیک تهران و موتور سوارهایش!
‏
🔴
برخی این وضع را با ترافیک بمبئی مقایسه کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/143488" target="_blank">📅 10:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143487">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7737782734.mp4?token=Zw7WyaEITx4M3u6t4cXrKq9oCvw4VVPCJiX5DJFU5KPfHCuA2xc3xFBDO2SMlK8X8_XLcQ91BtYjpHyKklugBCwybfxFX-IG6vIU9rvrxb6fwlc1Bynu9PdMsEqmtSNQArdR84S9ab3GN_I_eubeK7JZ9WeMGfhD2GejCXfehuGr4RhHAKHClVr_4iMZs1uQVvQtKaj6zaGzljtfNIyj_My0UVH1jFwLkIkgobPi269zo1-gckPXDo103JYJfM5nHfN9Ge4Ux24dDQIIsZiKipIw4k5yME4g7XuBL3Sr9MSTp4s3QpOKVCeZPIQ8uIC5hymSqQ-A307K0bzTeGLRSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7737782734.mp4?token=Zw7WyaEITx4M3u6t4cXrKq9oCvw4VVPCJiX5DJFU5KPfHCuA2xc3xFBDO2SMlK8X8_XLcQ91BtYjpHyKklugBCwybfxFX-IG6vIU9rvrxb6fwlc1Bynu9PdMsEqmtSNQArdR84S9ab3GN_I_eubeK7JZ9WeMGfhD2GejCXfehuGr4RhHAKHClVr_4iMZs1uQVvQtKaj6zaGzljtfNIyj_My0UVH1jFwLkIkgobPi269zo1-gckPXDo103JYJfM5nHfN9Ge4Ux24dDQIIsZiKipIw4k5yME4g7XuBL3Sr9MSTp4s3QpOKVCeZPIQ8uIC5hymSqQ-A307K0bzTeGLRSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: پهپادهای دریایی ما در حال کار هستند. روسیه ناوگان داشت. حال دارد به آهن‌آلات تبدیل می‌شود.
🔴
اما ما باید بیشتر غرق کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143487" target="_blank">📅 10:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143486">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f6d9ec24.mp4?token=cbj81piovdY42Nt1U8lNp3f3VNN4qbUMJJmIqslxGbKiFEuFVAW6cf3e5aYPmj96mvaC5RwSrT1W0WC3VICaztq8buv60cPgudFOQw6wMVszUY15L8pYPC-MZrTynnfLjzidW8wdksdn_PJX0Msr_nNAMHlwOf3NyiS9pQh_m1C96N-7dKzXP8QqXp3Zmssc5Qfx9bY8MWZbZdMwbGoMuhldmKPa3yw-x6ZfjNCVreVQWG8x7FPg9k7VYmB3wufVLH5HAnEse_79_d_yxCvrH5BKEgZeKmZ2WGSPWQu_g5BuMY9vZx8ZMJaR0RIKtv6_cA-D1vdMs_WMqnVvUvLvB3lYEu1U8fOS26tfDHkzNHzw3eSSzkwy9j-j-zspdTXK_-lJmtJfNkBLF6r_9DygB859VgeORhCm7aTtstKOeZ2dZdyJK_Cg3enuR-4uH3rNR4_A3KxtaEj0zzLOCRdk0SCIrPhUDBrqHF2IcTJDNWu0ZpBoUyVzsgz7LuNSJ5DChH0ymBoUvf83JOiFm4OY0XeK_gJJ6JqOCHKjo1DbNgYbsCgnyh0LdvqSULc-CVaOj3jS4pHJnQKPGuKQhrAt-1A1xmJdMR57H68l52RvlfplrSmPg996h2cwTHYjUAdrgFg2ZmmxDRkBTVxX8dXMvsykfnv_eJk7oCpawbVw2pk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f6d9ec24.mp4?token=cbj81piovdY42Nt1U8lNp3f3VNN4qbUMJJmIqslxGbKiFEuFVAW6cf3e5aYPmj96mvaC5RwSrT1W0WC3VICaztq8buv60cPgudFOQw6wMVszUY15L8pYPC-MZrTynnfLjzidW8wdksdn_PJX0Msr_nNAMHlwOf3NyiS9pQh_m1C96N-7dKzXP8QqXp3Zmssc5Qfx9bY8MWZbZdMwbGoMuhldmKPa3yw-x6ZfjNCVreVQWG8x7FPg9k7VYmB3wufVLH5HAnEse_79_d_yxCvrH5BKEgZeKmZ2WGSPWQu_g5BuMY9vZx8ZMJaR0RIKtv6_cA-D1vdMs_WMqnVvUvLvB3lYEu1U8fOS26tfDHkzNHzw3eSSzkwy9j-j-zspdTXK_-lJmtJfNkBLF6r_9DygB859VgeORhCm7aTtstKOeZ2dZdyJK_Cg3enuR-4uH3rNR4_A3KxtaEj0zzLOCRdk0SCIrPhUDBrqHF2IcTJDNWu0ZpBoUyVzsgz7LuNSJ5DChH0ymBoUvf83JOiFm4OY0XeK_gJJ6JqOCHKjo1DbNgYbsCgnyh0LdvqSULc-CVaOj3jS4pHJnQKPGuKQhrAt-1A1xmJdMR57H68l52RvlfplrSmPg996h2cwTHYjUAdrgFg2ZmmxDRkBTVxX8dXMvsykfnv_eJk7oCpawbVw2pk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی درباره پوتین: چین دیگر نمی‌تواند در حالی که کسی با لباس ملوانی و کلاه نظامی، با تلفظ بد برخی کلمات، درباره حمله هسته‌ای صحبت می‌کند، ساکت بماند.
🔴
چین باید واکنش نشان دهد. باید این شور را خنک کند. چین باید با روشن کردن این موضوع که هیچ دیکتاتوری حق تهدید سیاره با کلاهک‌های هسته‌ای قدیمی خود را ندارد، نشان دهد که جاه‌طلبی دارد تا یکی از رهبران جهان باشد — نه فقط از نظر اقتصادی و فناوری، بلکه از نظر تمدنی نیز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/143486" target="_blank">📅 10:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143485">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
رئیس اتحادیه طلا و جواهر: برای خرید یا فروش طلا عجله نکنید چون احتمال کاهش قیمت وجود داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143485" target="_blank">📅 10:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143484">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tg8NtKYN3ZCS8wK7aBzUKTlI1XQF38pCot0u1KcqrbdorjM1-WwdqtM-muoKP90OOi5cGl7bNZjRODSDRW1fsFpLhAtSuISCCLmKJYqLIoh7cU1ijXoeEiSfh9xW61Yu07x4fzaYs6NnAa2OklbiVWJS7r4jEw_6XwJGKmY2aE2OTNP8trWAyk3OVtsl5iUETj5tiJFIl7WKG5Ft-04Gzf6n_Ip8zu8nZPouiYC7acZBLYEktgzNQTYY7WmTrO9_lg-2nBBTbXZewa9pvWtZ4e2wUCjGWX30R97tfhIfSfhaErQfcc7uUW8cY1g-LJopX30B8cnX3fDuy9xQCrqtbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت جهانی اونس طلا دوباره افزایش یافت و از ۴۶۵۰ دلار فراتر رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/143484" target="_blank">📅 10:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143483">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
جیمز روبینز، پژوهشگر ارشد شورای سیاست خارجی آمریکا: تلاش ترامپ برای کاهش تنش با کیم جونگ اون، به همکاری کره شمالی با ایران در پرونده هسته‌ای مرتبط است
🔴
رئیس‌جمهور آمریکا امیدوار است که مانع انتقال فناوری از کره شمالی به ایران شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/143483" target="_blank">📅 10:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143482">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
رئیس دفتر رئیس‌جمهور: کاهش سهمیه‌های بنزین قطعی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/143482" target="_blank">📅 10:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143481">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AciPGEmr7G8x9kNmK2HhvW9SEtev130yRchGVo8E-rmT3ZdUJvv5E7_qUBJRzluIxrNVOwvB9Sl3J015ZBuEXJjTfQZH7DJ0Ufijjf8aOFjqN3GXcDGRLpCAVqt8RKz09xYJ3fkhTiBITA0W9i1Ke-L3XiowEEAFm8lYZxjjcQbsKQZRMnvNjpgsj8AeQbx257bKC8IFX6k9jDzZInFJgRZcEpic9Gq2LH80-ZkQRAWnmBPCLZx1eIqfjTzu1XNxPHnkxxc6PIqElyqeX_4tfMT-r59ddS7tZj88WoZ3JqRl0_PT0D1YNx4Ss_xKWu6FHjfXqw2Be2wVUwrNRkAQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: ایران «تنشِ نظامی و اقتصادی» جدید را «گسترده» و «تلاش برای بقا» می‌بیند؛ پس ممکن است دست به هر اقدامی بزند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/143481" target="_blank">📅 09:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143480">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5sj1xar6eFiRl4kiFnFFLeel8qPEn14bxlSW_FWbGTM5VevA0dzpEpiurRWTAXCZiPHykjgJXmaMPvSDbcqx_4yxc4kmpl62iF8jyqNAuu22N9iQ4F-8b1RnAlPSQIojNjKDTjnYtqH4c7KEu92pnfBnMh5cZJMLCO9TWBrPyJdlMyTE-VILJrUXL3pmYC2MmSbIuWp3MgAQBEodYTX4RCVQsCSEjK-YTRSBYOv9-04kCwmOBSL-kfO2gMn0opxC4R8LIwmrFlgKLcG_yd1NWeYqbDjBpxZvvAbMud6MWdW6_DHfCEMXHlOylL6rhfh4q3ym7Dy_OuXvCY1-vkXtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نشریه FT : وزیر خزانه‌داری ایالات متحده، اسکات بسنت، می‌گوید واشنگتن در حال ورود به «مرحله پایانی» در برابر ایران است و در حال آماده‌سازی تحریم‌های گسترده برای قطع باقی‌مانده پیوندهای مالی و تجاری تهران است.
🔴
او هشدار داد که کشورها و شرکت‌هایی که همچنان از ایران حمایت می‌کنند، ممکن است با مجازات‌های اقتصادی ایالات متحده نیز مواجه شوند، در حالی که دولت ترامپ به دنبال ایزوله‌سازی بیشتر و تضعیف اقتصاد ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/143480" target="_blank">📅 09:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143478">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99d1804edf.mp4?token=HL79ekHWxp5TxJ38adoyu_UBYGQi2ioiD-UzanK7NsVnpvkohtPHdF6XjovVXjhbAh_ejP-bISGGoxNx3_BhQwTZ99GfFHJ5Ll-XEwLuoMjcXeBoakRCbFmWScOarzukyIWC4kl2xcQDIdpqybiRYlUE_WYGsA3sKAmwtHdIs_mR0_F-XdpD1li9ryypTnnVWce8IxEsvrlp_HNgcRu629PidlnMXQ_x_TVKzpt6ZZar0Ls2ApausVCk8K_VRLjR8PiBPGLSyE4bleQUjpn8_iKiwSaFJQJeyAy1EshGWUFZoy2GhVtcoUDWDqSuIZfChIzY_XSXXjNg5aY_AYn-Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99d1804edf.mp4?token=HL79ekHWxp5TxJ38adoyu_UBYGQi2ioiD-UzanK7NsVnpvkohtPHdF6XjovVXjhbAh_ejP-bISGGoxNx3_BhQwTZ99GfFHJ5Ll-XEwLuoMjcXeBoakRCbFmWScOarzukyIWC4kl2xcQDIdpqybiRYlUE_WYGsA3sKAmwtHdIs_mR0_F-XdpD1li9ryypTnnVWce8IxEsvrlp_HNgcRu629PidlnMXQ_x_TVKzpt6ZZar0Ls2ApausVCk8K_VRLjR8PiBPGLSyE4bleQUjpn8_iKiwSaFJQJeyAy1EshGWUFZoy2GhVtcoUDWDqSuIZfChIzY_XSXXjNg5aY_AYn-Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای اوکراینی شب گذشته سه مرکز لجستیکی شرکت Ozon را در مناطق مختلف روسیه مورد هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/143478" target="_blank">📅 09:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143477">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfCb5vrPHkPrxhem5W7Xqy13YHB2mDQlwJTiLDm6J3TrcfvOjSx5U2vJDZHQBVLeLragVUbGnO-U2a20r-Qwxa2n5DhGwCNYEaHvciUiel3Gc-_pkYF4SIc44lv0Wxf_XyQg_Wh-EwD55u0h056Fckf_flVTEF9rxDH0A1yEZtR5GokX3ZwKf5dqMiDhNoD16cfkK7CdbX52Z2epayCZjJMd5nx7PMgOTu3wwBUSrOO5vmRTs9P1mmgywXBZ8MvLc9F0dZoMmnSgGR5qx2BDI_ZEjRRkIfmN_-g2TtuVOp7gOQDG6A9IGtnK2OWZc6sOAZKgGFLs-v0QJpRuMmzqVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کیفیت هوای امروز پایتخت روی عدد ۱۰۱ و در وضعیت ناسالم برای گروه‌های حساس قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/143477" target="_blank">📅 09:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143476">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ونس: هدف نخست و اساسی ما از حضور در خاورمیانه، جلوگیری از دستیابی ایران به سلاح هسته‌ای است؛ فشارهای شدید علیه تهران هم در همین راستا است
🔴
تلاش می‌کنیم مانع وقوع بحران انرژی‌ای شویم که ایرانی‌ها در پی ایجاد آن هستند
🔴
یکی از قدرتمندترین ابزارهایی که در اختیار داریم، الزام ایران به پرداخت هزینه برای تلاشی‌هایی است که جهت خفه کردن تجارت نفت و گاز می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/143476" target="_blank">📅 09:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143475">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
عاصم منیر راهی ایران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/143475" target="_blank">📅 09:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143474">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
در سه ماه اخیر، ۳۰ نفر در سواحل مازندران بر اثر غرق‌شدگی جان باختند که بیشتر موارد به بی‌احتیاطی و نادیده گرفتن هشدارهای ایمنی مربوط بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/143474" target="_blank">📅 08:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143472">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abdfbf705a.mp4?token=mgI28P2GmV0E_foshGPKMn1Hz5qD8m1EuzFKvP-Mu_oirqoal_fZro3zoxug_eYt4hbpfFG6pifo1diiWhVNEGuxb8hcft63hRvMAY8lcZsefEMGZlVNO2Wwjh_M68M7qbDsWlI8ils2us7Ll1lQKNhpWXlh-gaV_0_qwNtwqiCegRjQ9yZfxpTRjctbYQUnGA-lHSvLvV4tf6h56FtRFWyeg_Lyme0b84Qqi-VXh7ogukfo08j_7uUwiZCgdyVN3iT5X63pYvlrTgiSI1I17aovr4aMOUx4lBvqkgqft1NT-6cW_DZpisFpWMyzZnMjKkXS87xKRaFlHC2tIXauqoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abdfbf705a.mp4?token=mgI28P2GmV0E_foshGPKMn1Hz5qD8m1EuzFKvP-Mu_oirqoal_fZro3zoxug_eYt4hbpfFG6pifo1diiWhVNEGuxb8hcft63hRvMAY8lcZsefEMGZlVNO2Wwjh_M68M7qbDsWlI8ils2us7Ll1lQKNhpWXlh-gaV_0_qwNtwqiCegRjQ9yZfxpTRjctbYQUnGA-lHSvLvV4tf6h56FtRFWyeg_Lyme0b84Qqi-VXh7ogukfo08j_7uUwiZCgdyVN3iT5X63pYvlrTgiSI1I17aovr4aMOUx4lBvqkgqft1NT-6cW_DZpisFpWMyzZnMjKkXS87xKRaFlHC2tIXauqoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بمب‌افکن‌های استراتژیک آمریکا آنقدر از ارتفاع کم بر فراز واشنگتن دی‌سی پرواز کردند که آژیر خودروها به صدا درآمد.
🔴
یک فروند B-1B لنسر، یک B-2 اسپیریت و یک B-52 استراتوفورترس در آرایش پروازی به همراه F-35ها و F-22ها بر فراز نشنال مال پرواز کردند. این نمایش هوایی بخشی از جشن‌های ۲۵۰ سالگی آمریکا بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/143472" target="_blank">📅 08:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143471">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
رویترز به نقل از داده‌های کشتیرانی: کمتر از ۲۰ کشتی باری طی دو روز از هرمز عبور کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/143471" target="_blank">📅 08:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143470">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKgAEMOQOgn3vrtt6RePNDHKXUtHBbZPmungoKJbB0DSPy2HtT_gm7hgQhKBDDJthZyrxRhfNF-DrVek7zafNKRcofpmlPYFlv4ewRdgcqYdyhd_fKShFCd8dn65MLtHwXeWHTTzgWGS3qjdrf3aW4ytaEgtTCQ7D5h08kAS0HQ4klp9S5_MjZHgu7UWfU91gm70LqcZh-BagyZ4iUoZgkv2B4DU_6wKZHtTZD_Z7-9j1e8zJ8RrwS2hNX-GBlDNt9yADNNoGbmConvs130B3kK6Ia8YRf0Unvupab7uSyX3RsEsG3kP_HKZ9xrs6YzzTm1IeSONgaTpq5n55zHseg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تلگراف : ایران تهدید کرده است که در صورت راه‌اندازی کمپین «دی-دی اقتصادی» توسط دونالد ترامپ برای وادار کردن تهران به پذیرش توافقی برای پایان دادن به جنگ، به کسب‌وکارهای آمریکایی حمله کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/143470" target="_blank">📅 08:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143469">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وزیر خارجه عمان فردا (سه‌شنبه) به ایران سفر می کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/143469" target="_blank">📅 08:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143468">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
اطلاعات: هزینه‌ها دلاری است، حقوق مردم ریالی
🔴
روزنامه اطلاعات در گزارشی از «تناقض دلار-ریال» در اقتصاد ایران انتقاد کرده و نوشته بسیاری از کالاها و خدمات، از انرژی و خودرو تا دارو، مسکن و مواد غذایی، با معیار قیمت‌های جهانی و نرخ دلار سنجیده می‌شوند؛ در حالی که درآمد بخش بزرگی از مردم همچنان ریالی است.
🔴
این روزنامه می‌نویسد در برخی صنایع، مواد اولیه با هزینه‌های ریالی یا یارانه‌ای تأمین می‌شود اما محصول نهایی با قیمت جهانی و دلار آزاد به بازار می‌رسد.
🔴
اطلاعات پرسیده است چرا هنگام افزایش قیمت‌ها منطق «آزادسازی و نرخ جهانی» حاکم است، اما وقتی نوبت به حقوق و دستمزد می‌رسد، همان منطق کنار گذاشته می‌شود؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/143468" target="_blank">📅 08:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143467">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f800119c93.mp4?token=oqR_PqIMQfu41dbi_ItuB5KKjKJTLu3OHTBZ2lkTl3a0j9rMbeHgQo6jKenIaAweOklWc-pmCcSJFu-BoFQ9IqAhtfiopnJ7aEtPB54LRlt7NlgWaaiLOLsI4SEaFjvNa67wCAV75TTMF2db3M5DfXxzFbB3btK1eAa6Ut5AeKUllwfmkJTeAGHhbDpkIhuHv_U3Z4TzQvORpOMOKDXxTcu3FxUvLR4wjxFHHjloxD45CATphfQ01C3mY-nkMuNoEG2RnZCYI5Kyfe0J8RAUjOviRjLMGo90--ZaXUwUHNtrbtsL3aOv8hNK1dfsOWn0-q3ZG6Y5yLAYWVtAf0GvvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f800119c93.mp4?token=oqR_PqIMQfu41dbi_ItuB5KKjKJTLu3OHTBZ2lkTl3a0j9rMbeHgQo6jKenIaAweOklWc-pmCcSJFu-BoFQ9IqAhtfiopnJ7aEtPB54LRlt7NlgWaaiLOLsI4SEaFjvNa67wCAV75TTMF2db3M5DfXxzFbB3btK1eAa6Ut5AeKUllwfmkJTeAGHhbDpkIhuHv_U3Z4TzQvORpOMOKDXxTcu3FxUvLR4wjxFHHjloxD45CATphfQ01C3mY-nkMuNoEG2RnZCYI5Kyfe0J8RAUjOviRjLMGo90--ZaXUwUHNtrbtsL3aOv8hNK1dfsOWn0-q3ZG6Y5yLAYWVtAf0GvvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اگر ایران سلاح هسته‌ای داشت، کل منطقه خاورمیانه به طور کامل نابود می‌شد / اسرائیل که قطعاً همون اول نابود می‌شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/143467" target="_blank">📅 08:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143466">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وزیر نیرو: خواستم یه خبر خوب بدم به مردم عزیزمون اونم اینه که از هفته بعد قطعی برق نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/143466" target="_blank">📅 02:22 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
