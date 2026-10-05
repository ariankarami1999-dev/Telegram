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
<img src="https://cdn4.telesco.pe/file/c93T5aOxeOxda--YV0PfwAmMI3VG90sNuUJQHGnLw0a18UJEdAHWL2-KsS5XoFBVRLuv0U3tXPbZ3W1KyoAbJAv45W3GL-YOXFXJwodMZTp9MmqbFTcJhXTvvTgVYGOXPTXF1LYFODHPXoF92Wd58sCCJAbICrfZZfdiC6vTEUGXtDIHRKsnGNfUNjTj4tqBe9pv_JW0qGioeLvCWtIXeDlFbUj-fpyBYI-bGSl8RaF4DectMLiDLRyUzBykr0Os8BB-SZ8ZtmrWepHEq76C4-5GjqjmOx89JniJ8STXEfFzKCLe6btcGwWuOzlJt3x5vYxQcyK5yI-Esy89vDgChg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 12:49:28</div>
<hr>

<div class="tg-post" id="msg-72766">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcebd0dcd.mp4?token=k-2Id1tcf-ZfXuYUkOisjW3bwvOLLctJEgvJCYpEr45l-oU4YvlNLWJz8IQAofNvKNQaEvkY75l2E93cAS204deasZUUVWqTCnlXW3v4XAdYH_wImLZh9vwXBW3E3GGlXGSQ9h6I8VxzfNy3XIsejo8IeU5ZImMmAgIOOhS-s5rayxCkmJq7Ez6LZujOxtnagM7igRHnsZYUPxeX7BPU-aq6RmzmayRoaPIhWGX8Zi6B9NG4tjlRSY6PT7ueeHC83P4PPVvNMTBS8WdiOnZra_GQ8YHK3W-MMvE-DukZiLV3CeUR5RaoS0jhIaAgyR39f_dWNmu_jkpq_h9H56f0ITDz3dm4_YUaWCXk8qDt6v_Uw9pXtSx5y7LhG0RuMHO5cdKIKxGAbL_YzCUIk_MSraUVkpouCs1bdcs96FWr1WMJlxlMUduQAWTyVr7rq80VjByCXqcy2Dd_6BVA9nYjNPdKCFlWov3Kk-3m6eBzhm9CvcC9oIRvU2Bj-RsePQOxL_4YQ40MURnvX_K2yuPqxIYIY7hgFP5TkSt7dDGJbXEvfKOdYFJYrmmbT28bTSQnQaLoNaDPEOHYC_lTtM0TuZTgpICmFVTaskly7DWbeICa6WcswS90iYDtY9vOWavbvzAKN0aayC0j2k9-mUfvMml33PHUdf3pvQaabcPjXVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcebd0dcd.mp4?token=k-2Id1tcf-ZfXuYUkOisjW3bwvOLLctJEgvJCYpEr45l-oU4YvlNLWJz8IQAofNvKNQaEvkY75l2E93cAS204deasZUUVWqTCnlXW3v4XAdYH_wImLZh9vwXBW3E3GGlXGSQ9h6I8VxzfNy3XIsejo8IeU5ZImMmAgIOOhS-s5rayxCkmJq7Ez6LZujOxtnagM7igRHnsZYUPxeX7BPU-aq6RmzmayRoaPIhWGX8Zi6B9NG4tjlRSY6PT7ueeHC83P4PPVvNMTBS8WdiOnZra_GQ8YHK3W-MMvE-DukZiLV3CeUR5RaoS0jhIaAgyR39f_dWNmu_jkpq_h9H56f0ITDz3dm4_YUaWCXk8qDt6v_Uw9pXtSx5y7LhG0RuMHO5cdKIKxGAbL_YzCUIk_MSraUVkpouCs1bdcs96FWr1WMJlxlMUduQAWTyVr7rq80VjByCXqcy2Dd_6BVA9nYjNPdKCFlWov3Kk-3m6eBzhm9CvcC9oIRvU2Bj-RsePQOxL_4YQ40MURnvX_K2yuPqxIYIY7hgFP5TkSt7dDGJbXEvfKOdYFJYrmmbT28bTSQnQaLoNaDPEOHYC_lTtM0TuZTgpICmFVTaskly7DWbeICa6WcswS90iYDtY9vOWavbvzAKN0aayC0j2k9-mUfvMml33PHUdf3pvQaabcPjXVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای دولتی یمن مورد حمایت عربستان سعودی اعلام کردند که کنترل تنگه باب‌المندب را به دست گرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/news_hut/72766" target="_blank">📅 12:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72765">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJhSF0WTFjDSw-qsT1mAfc8lv1zEf-5uuyDMKzK_ZYOTZuKU0XJ4nC1js-hYrUW6uYyheyekf0NxrKArVwDA8c7iHsP9fTON6_mKNdYZ6sfmnrp9-LVk66H16HfFrTbsMTw3DwvLCM8X5SiQ9KZO_5FncrCcJMqiN2VS4H-JjfBpwU9cjLCsb16FDnXX_RrfUXa0Sw9IxbcB-AqJSejChtgylQHYamiFAbnWv_fFm88W8Nr9mtWOMuJ0x92lPcQFcpJGOh5q2BqhvdaYMYzuFIQh-fNfjepF_Ebf3KzC1bCi50vTdJ8h-m2lDDIQnesShpcJPLeM5QYSawIi2ZLgUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علیرضا سپاهی به انفرادی منتقل شد؛ نگرانی از اجرای قریب‌الوقوع حکم اعدام</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/news_hut/72765" target="_blank">📅 11:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72761">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e88e1de928.mp4?token=qjpMpqqz_ESJJij021ppAFbdLUR2gRmv4eFjjRwsnwDgHN9_8-v4S6W1nN6_fyG54R9TRe8onYsgKxQwQB3zGoQqGOaI2sLXBUtHlVt8ijUk-JC7RBUuDK3TJIx9DNfcmf4hjMohzdjgFBjmV94eRQsQInLTiSs8bvVBKW3fhOInSWR50T3ZgiM6JVmkI7hs2-VOm-nbzuhpTxWFVLchy-gMS6lx4R9am8BS6Z55Kqu-kuBhEzZ7yBzbI111lZpZVsrwNgKFKxnH7KjMcttOMAlGPw4UDfaz7X1cKBAVBNRWRVt-YEw2nNy25toyqljpB0JkwxWeLK-ASPneeOJXhw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e88e1de928.mp4?token=qjpMpqqz_ESJJij021ppAFbdLUR2gRmv4eFjjRwsnwDgHN9_8-v4S6W1nN6_fyG54R9TRe8onYsgKxQwQB3zGoQqGOaI2sLXBUtHlVt8ijUk-JC7RBUuDK3TJIx9DNfcmf4hjMohzdjgFBjmV94eRQsQInLTiSs8bvVBKW3fhOInSWR50T3ZgiM6JVmkI7hs2-VOm-nbzuhpTxWFVLchy-gMS6lx4R9am8BS6Z55Kqu-kuBhEzZ7yBzbI111lZpZVsrwNgKFKxnH7KjMcttOMAlGPw4UDfaz7X1cKBAVBNRWRVt-YEw2nNy25toyqljpB0JkwxWeLK-ASPneeOJXhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت خیابان های فرانسه پس از اعتراضات گسترده دانش‌آموزان و دانشجویان به دلیل کمبود معلم و وضعیت بد مدارس
@News_Hut</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/news_hut/72761" target="_blank">📅 11:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72760">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72760" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/news_hut/72760" target="_blank">📅 11:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72759">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xw6CkUXNjem66GaqFwmAfT1ZZ-ZH1VeZ_nuk8MSVTdjzgCRhLN6OP_YxKLtaCeilv-dIlLEG5Wi99-ygVyfVQPrQn2pEsKuWGgTrnI9LDbTRVG8UYyNXUGWFmvfoh1ZTB-ihLNTNDkHS80rYEdSjFxJd9WVoSFsQ8Ys7OPonZijjDl287UjPSNDT34blPNFRWf5-pR4p9S3FvDiVNk3cHoTkt8wA8sTWjba7A6Fq_iM59a5Qkg5NfUV-yh4gDovyyRYlgQ7JaVMDcd2QH0UxxlIQ3P9kW626dwAE0rjZpwrvirEFugCLRtV3sT4bRElIY_trvmE-DEOhPDyMpB7AWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
بلژیک
🆚
فرانسه
ترکیه
🆚
ایتالیا
لهستان
🆚
بوسنی
سوئد
🆚
رومانی
نیوزیلند
🆚
ژاپن
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
http://T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/news_hut/72759" target="_blank">📅 11:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72758">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e436b8c05.mp4?token=O-u58gWVxJlswwmQfzmLaivc4__Q8uFQL2xuky_S33zUNtzXId3FNVICCmfrwH-j0LV81Fas3kw0edSkAgLpKWfCAxUqkC5WfINiss-E34W72Qquc5uG2lvbXFcznZ1UDJCGKl6LxgOGVM4U0Z2wFMu0Furwu9vrbsJ-dDLuE55lGl_wM-a8pt5ySCrLKR-jdEQMmJmhMA1yhJxehsfUR6PKFjL-reuwqPElXCGow60LF3VaUmJ6TEy5OjVOAqvQQoy0miSW7ZzEqCsY2iXhEkjPE1WQauy4qislSGGOhdQThFDlL9YxdYiOZhssG7T-KmmUWs1LkWCNkiYNP4Yx3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e436b8c05.mp4?token=O-u58gWVxJlswwmQfzmLaivc4__Q8uFQL2xuky_S33zUNtzXId3FNVICCmfrwH-j0LV81Fas3kw0edSkAgLpKWfCAxUqkC5WfINiss-E34W72Qquc5uG2lvbXFcznZ1UDJCGKl6LxgOGVM4U0Z2wFMu0Furwu9vrbsJ-dDLuE55lGl_wM-a8pt5ySCrLKR-jdEQMmJmhMA1yhJxehsfUR6PKFjL-reuwqPElXCGow60LF3VaUmJ6TEy5OjVOAqvQQoy0miSW7ZzEqCsY2iXhEkjPE1WQauy4qislSGGOhdQThFDlL9YxdYiOZhssG7T-KmmUWs1LkWCNkiYNP4Yx3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراد ویسی:
جنگی که توی راهه، آخرین جنگ ترامپ با جمهوری اسلامی خواهد بود!
اما به قدری این جنگ شدید و گسترده‌اس، که جنگ ۱۲ و ۴۰ روزه، پیشش یه شوخیه!
شدت بمبارون‌ها خیلی شدیدتر خواهد بود، کشورای بیشتری درگیر میشن و این نبرد آخره!
@News_Hut</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/news_hut/72758" target="_blank">📅 11:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72757">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf7a6e5830.mp4?token=AB6xWdRg0GEjHahQFkEUJECG5d07CrtRaQqfOkLq0q-WYsy66ogfAam5B_SWM2wKy13Woztzyzp_HDjxPBPWDAirZ13j0KbxUHRe7ihDq_LcnBAW4GVJy5rax5LpihY0xq_VQZLASnn1qNclOUcalog7l2d69Qj5bGgqnDA5-k4ljpVzheGDl6Zir-JbkskoY1big_oowJbHL5FPuzuPByqE4q3toJyE0J-sCMS8AkZQOtqlOWuqxtcR1lSl6xfdoPS85k_u7fck1RdZwjj_ZLJvoGRc6TKG2eybmctKp74foYvtib_lEauv9V4913RvRDr97Dk-lo5Qd44H7_X6Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf7a6e5830.mp4?token=AB6xWdRg0GEjHahQFkEUJECG5d07CrtRaQqfOkLq0q-WYsy66ogfAam5B_SWM2wKy13Woztzyzp_HDjxPBPWDAirZ13j0KbxUHRe7ihDq_LcnBAW4GVJy5rax5LpihY0xq_VQZLASnn1qNclOUcalog7l2d69Qj5bGgqnDA5-k4ljpVzheGDl6Zir-JbkskoY1big_oowJbHL5FPuzuPByqE4q3toJyE0J-sCMS8AkZQOtqlOWuqxtcR1lSl6xfdoPS85k_u7fck1RdZwjj_ZLJvoGRc6TKG2eybmctKp74foYvtib_lEauv9V4913RvRDr97Dk-lo5Qd44H7_X6Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره یه دختر تن فروش: یه دفعه یه سید بهم گفت بیا رابطه داشته باشیم، فقط تو زود بیا چون ممکنه خانمم بیاد خونه.
رفتیم تو اتاق و شروع کرد صیغه خوندن، هر چی قرآن، آیت الکرسی، تابلو و کتاب دعا بود برعکس کرد و گفت زشته، گناه داره.
یه دفعه وسط عملیات زنش اومد، گفت سید زودباش درو باز کن خیس شدم زیر بارون، سیدم بهم گفت تو فقط چادر بنداز سرت شروع کن نماز خوندن.
خانمش اومد به سید گفت این کیه؟ برگشت گفت این خانم مسافر بود، اومد گفت نمازم داره قضا میشه، میتونم خونه شما بخونم؟ منم آوردمش نماز بخونه.
آخرشم خانمش بهم چایی داد و کلی پذیرایی کرد و رفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/72757" target="_blank">📅 10:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72756">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de6e0dfa99.mp4?token=l797UBSuG6KtucbKU4UdWLe-pLAORH1CyGj5XilPD1iHqWM6WsxAkdPNDIgJalRE87Jn7ffiTjr-0BgPHkjGmfxzC1vlhhhOeobWLUVaM96vO18bdzENjmGK8CyNrDK4xzqvU4vIVC7rnuJrK25-sgh3VkisN66tibwElQgVFoEBCDDqWD4iIAHO3LS5Gxybcg1_8rCPJA5ur0FRSODzDoN5LSydgeS_VcxiKKSx71pvgDaXq6icVRLZNGazd5TZa1njm7tQTTij6ePPGnJjNLcuZQXIjo7DnTxgyExpsOGWNjJGdXpYBQnmHkpGLFp239uu_1IfHVWObwbrq9Dpsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de6e0dfa99.mp4?token=l797UBSuG6KtucbKU4UdWLe-pLAORH1CyGj5XilPD1iHqWM6WsxAkdPNDIgJalRE87Jn7ffiTjr-0BgPHkjGmfxzC1vlhhhOeobWLUVaM96vO18bdzENjmGK8CyNrDK4xzqvU4vIVC7rnuJrK25-sgh3VkisN66tibwElQgVFoEBCDDqWD4iIAHO3LS5Gxybcg1_8rCPJA5ur0FRSODzDoN5LSydgeS_VcxiKKSx71pvgDaXq6icVRLZNGazd5TZa1njm7tQTTij6ePPGnJjNLcuZQXIjo7DnTxgyExpsOGWNjJGdXpYBQnmHkpGLFp239uu_1IfHVWObwbrq9Dpsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه عراقی :
به حضرت عباس اگه بگن بین پسرات و جمهوری اسلامی یکیو حذف کن میگم بچه هامو حذف کنید تا فدای جمهوری اسلامی بشن
ایران از بچه هامم ارزش بیشتری داره
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/72756" target="_blank">📅 10:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72755">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaee08d663.mp4?token=iVUI0VNG2KhNlJ1aPIgNrmLuvPYmWCBY53LBE4rtW6trmoo2CrvCXAB4FHvv9pfUwwKNDbkiXZmkx4HrFOxAz-JHgkuuFjgJklqZ8qwYC8HKn5WLLKvvbd7_rPw3XqfsGb9MDOL_g6U2ecv2eEckl4SU95VmuHqQ5CaLTxiJI7LyE4aqDOVafsCfeOTTFnO4xf7E3vqYlVCuu9SgQ1H5fU2g-QuT0RnMzLFzwi1K8Z61AhyLvlmUcN3UulVTCnz6fUOe2J5oQDvGkeCQQggP7V3cN5NzaRbGs_fOijlXHT-_D_XbdHO5xgCB-aEssXq-rn9udBhMqNMOfK6wpUuhpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaee08d663.mp4?token=iVUI0VNG2KhNlJ1aPIgNrmLuvPYmWCBY53LBE4rtW6trmoo2CrvCXAB4FHvv9pfUwwKNDbkiXZmkx4HrFOxAz-JHgkuuFjgJklqZ8qwYC8HKn5WLLKvvbd7_rPw3XqfsGb9MDOL_g6U2ecv2eEckl4SU95VmuHqQ5CaLTxiJI7LyE4aqDOVafsCfeOTTFnO4xf7E3vqYlVCuu9SgQ1H5fU2g-QuT0RnMzLFzwi1K8Z61AhyLvlmUcN3UulVTCnz6fUOe2J5oQDvGkeCQQggP7V3cN5NzaRbGs_fOijlXHT-_D_XbdHO5xgCB-aEssXq-rn9udBhMqNMOfK6wpUuhpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار :
از آقا مجتبی (خامنه‌ای) چخبر؟
حداد عادل پدر زنِ مجتبی خامنه‌ای :
سلام میرسونن...انشاالله خوبن...همیشه...خوبن الحمدالله
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/72755" target="_blank">📅 09:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72754">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e173a359.mp4?token=ZvOwzhWY39NqcrmaHGRpUriCksjH3whGbIPwehwyAHejzf_n-lRQoS-7_IlBc5wPf4SOuioLWMstXbPZoC-cIhYIkpIK7_58lRIiI3W4eYxxpiNB-cy3PWNeHCAtns2Zq_d1Ajsj4NqHoyz9_Ppi89APfR40v4QMAAK8m_wwXcHEQPudqznI0lXnjHyD983nVTyi4pX3mZIjpNOEZ-U71c1HW0gIEqg5ZIOtXgJ7hnyAShe4NXlf_RzVFmAyo2h9hKwDr8ybMfxLZlr14xXaQdKnorftPc8O4fPaML1JitgqJB60jz3GmE80KlwSp1-Az-uWJwc7PtiagMkV8zVRfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e173a359.mp4?token=ZvOwzhWY39NqcrmaHGRpUriCksjH3whGbIPwehwyAHejzf_n-lRQoS-7_IlBc5wPf4SOuioLWMstXbPZoC-cIhYIkpIK7_58lRIiI3W4eYxxpiNB-cy3PWNeHCAtns2Zq_d1Ajsj4NqHoyz9_Ppi89APfR40v4QMAAK8m_wwXcHEQPudqznI0lXnjHyD983nVTyi4pX3mZIjpNOEZ-U71c1HW0gIEqg5ZIOtXgJ7hnyAShe4NXlf_RzVFmAyo2h9hKwDr8ybMfxLZlr14xXaQdKnorftPc8O4fPaML1JitgqJB60jz3GmE80KlwSp1-Az-uWJwc7PtiagMkV8zVRfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حاشیه ختم خواهر عباس عراقچی، وزیر اقتصاد از پاسخگویی درباره وضعیت فروپاشی اقتصادی و کاهش ارزش ریال فرار کرد و خبرنگاران را به همتی، رئیس بانک مرکزی، حواله داد و همتی هم بدون پاسخگویی فرار کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/72754" target="_blank">📅 09:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72753">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72753" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72753" target="_blank">📅 01:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72752">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgRFFF9ge51WhtLbY4AUlEEGhCf2dgWFIimV4ygWB8DIijq2fzOxb5_g-7LtNdHUzlBB5sGgmJHDc1CXIXKNry82f-HJ3Dcby5ecnZbn1luaAQwuVkg1-XIDMMPwilXuLwhVIHwLeMVKYPxaII2MI9lDSOdtbHTFJH1pUWUGG17SxdyWMnogGYTDsDkFR3E3bmETM3TYQYmh0Cgb1nppUPKkS6o3LKIONHXbQSzZ--5qdb_QbK-IxtK8Q6pnfAAib4icaDPBWszSFoRZnXzZeWjy_COzxurmCGJipdrKhAVUUHZYFrxc_9q0s0CS3eXNQQ0GwXG7GD1L8yJGohhR1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72752" target="_blank">📅 01:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72751">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eRdOOl77TKWmkDJnJU_8HBuYxUtcdwlSAtUY-jSANT5ZD8wgSZbYN2_avVJddwbicZXMOJtmZxcvoC9AmIJ7xpUyy7NmEH4lgP049aZFPCtyHsp3iI-CPo-yAEfbBUg2rwM1SQT-MQCPk0DMfalHys-zmHMHR6hBNlRafYYlGI5qQJt94nxzlyWpm1k-NQwWilJxIvs10kGjfqXKJMB4eKC8bWMyob0zcC8sfjQzfLiKD7FIQ6QK5AsEb4SLcAHPpCSvlV4DOjLrijzcQCrcFoEtL0TN5rokw2ALdoxo_qmF_gFzuF9OahFtUn6IYtgo96hGKXG6Uml3YNGtzftKKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال به نقل از مقامات آمریکایی گزارش داد که بمب‌افکن‌های راهبردی «بی-۱بی لنسر» (B-1B Lancer) در حال خروج از پایگاه نیروی هوایی سلطنتی بریتانیا در «فِیرفورد» (RAF Fairford) هستند؛ این اقدام به دلیل نگرانی‌های امنیتی و در پی دریافت اطلاعاتی مبنی بر وجود طرحی از سوی ایران برای حمله به این بمب‌افکن‌ها در پایگاه مذکور و کشتن کارکنان آن صورت می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72751" target="_blank">📅 01:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72749">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fEkqSz7pELekSwJePKV7c8qgstuSsnwA6IxKhbfYR938P5VxZG6IbLhJ1BpBz7snEjXhbg279MRStWBO2ZJmgcMXXZVqwNYVcTkz52XzdRo_ZdMRr6I55EC3W876GaT-LId_KVUonF1jxC47JTK7Fb4IBICx3ZqUHM5unHhEAMirXNY0P7ND3wR66rC3QuKIqB3G0yqoxM-N-9FcuMDkKROfNhZTNIABR7z_cp1NDNoLYswR8slCbKb88dWkWBqopKaWrZyi5ccHbZO12bB6M1vSvThIt6SWThEZOpE0BsgjHIUM7PJSNvBMcuApvDokVlGVuu7z8QYZGUGpY794Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5cef955dd4.mp4?token=g-PwHmlZ4TSxnq4lCXGEVcuAzhPxtXauLcy59Xsa6WtvUHh8iGkKFSyr9v7ISFWSSUIhbk_2FOaiuZ7jY6pamVkn5-15tDw9uEBc4e9-nduLJXjFhID567_VgPiwHjPEcTi05axqj77eOdZvUmpkWicqNhRKj_KTdz5Gww8OvtxOVYfXNZ7Z5_MJOvUHlUAaSaQ01g1shqHK0eTYzN3PgwzhWpxramG2QqRWrqmGwwhyfrHewxszOQMPe8UFj5sc3FktWapIvjCvWSTRtlEsaPun5x6HSbwqiYwze16hzuvKmozlGHpf07SQfrQt7SKVlffeZJYBFALDupJu2lATQg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5cef955dd4.mp4?token=g-PwHmlZ4TSxnq4lCXGEVcuAzhPxtXauLcy59Xsa6WtvUHh8iGkKFSyr9v7ISFWSSUIhbk_2FOaiuZ7jY6pamVkn5-15tDw9uEBc4e9-nduLJXjFhID567_VgPiwHjPEcTi05axqj77eOdZvUmpkWicqNhRKj_KTdz5Gww8OvtxOVYfXNZ7Z5_MJOvUHlUAaSaQ01g1shqHK0eTYzN3PgwzhWpxramG2QqRWrqmGwwhyfrHewxszOQMPe8UFj5sc3FktWapIvjCvWSTRtlEsaPun5x6HSbwqiYwze16hzuvKmozlGHpf07SQfrQt7SKVlffeZJYBFALDupJu2lATQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا سپاهی به انفرادی منتقل شد؛ نگرانی از اجرای قریب‌الوقوع حکم اعدام
علیرضا سپاهی، از معترضان بازداشت‌شده در جریان اعتراضات دی‌ماه ۱۴۰۴(پرونده میدان علیخانی اصفهان)، به سلول انفرادی زندان دستگرد اصفهان منتقل شده و خانواده او برای آخرین ملاقات فراخوانده شده‌اند.
وکیل علیرضا سپاهی نیز انتقال موکلش به انفرادی و اطلاع خانواده برای آخرین ملاقات را تأیید کرده است.
بر اساس گزارش ها دختری که عاشق علیرضا بوده گفته آرزو دارم باهاش ازدواج کنم و امشب در زندان خطبه عقدشون تلفنی خونده شده
💔
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72749" target="_blank">📅 01:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72748">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooWTBHIFLXd5l0a-tzgDQP3VfiF12oNbojkrxrzBHJ0fwSujPelNEX_CKaVbto5qogyoh3tcHnifR1IPlRCZL7twCOWMiU7GVsgY1m_W4S9L4p1Xk8QSyc1FUbv_Ad29M7PBDP4hbUOswB77gR0t4JlrBa4SBu8o2IGciaOUFFJV7baLQwsvaN8N_HQsNJVECBnQsn9lu-tRPkouz29IUMj8PNQgrVPsVoDVgQOpSbh1tRYbAKlYkMQQXjyKO0F1i74gJS4HUaRCvAujhi1EHV2WyYSKZSFd9-hvSNzCqyN_XHcG3ES0sK1QoUakTbsVw38GWf4iJWFlBfbdQ-SFIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید صفحه یوتیوب امیر تتلو:
امروز دادستان و رئیس کل دادگستری صحبت‌های خوبی با تتلو داشتن و اگه گزارش خوبی هم رد کنن، امیرتتلو فردا آزاد میشه و به استقبالش میریم!
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72748" target="_blank">📅 00:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72747">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">۱۰فروند از ۱۲ بمب‌افکن راهبردی B-1B Lancer نیروی هوایی ایالات متحده که در پایگاه «آر.ای.اف فیرفورد» (RAF Fairford) انگلستان مستقر بودند، در حال ترک این پایگاه و بازگشت به خاک اصلی آمریکا هستند. انتظار می‌رود دو فروند باقی‌مانده نیز امروز این پایگاه را ترک…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72747" target="_blank">📅 00:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72746">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec28377bbb.mp4?token=ebiJENrdneP_LFXYME4aUrILVngnO3i9sQ3A4WlT7_5yIuhMybEW3X5tloF4alBoVbeauRAMgL8pI8wV1d0-UBTQQDc2jI-WOIt1Ka4pulwOmQvpYncMMcQ2IHLt_7koo6EVZlZarfmTTHb2sg_4k_VNUAymuUROzy9IhO6Q3iHnIZYi8OXbzVNC1GwrC2_C7fhTF4P0GH8iLb8_Rbwdy6p9fXmm37jCDS8CqOaU8xgtuCqejGq1FOvoIeNJzJ6l6Vjhe_bX_cwHZV7Tacj3imMoPTgAiEqRWvwFUASg9HeHOGteGWKC8PTl8WwmcYwy1JqYgjrYLHM7uOFJ9evb4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec28377bbb.mp4?token=ebiJENrdneP_LFXYME4aUrILVngnO3i9sQ3A4WlT7_5yIuhMybEW3X5tloF4alBoVbeauRAMgL8pI8wV1d0-UBTQQDc2jI-WOIt1Ka4pulwOmQvpYncMMcQ2IHLt_7koo6EVZlZarfmTTHb2sg_4k_VNUAymuUROzy9IhO6Q3iHnIZYi8OXbzVNC1GwrC2_C7fhTF4P0GH8iLb8_Rbwdy6p9fXmm37jCDS8CqOaU8xgtuCqejGq1FOvoIeNJzJ6l6Vjhe_bX_cwHZV7Tacj3imMoPTgAiEqRWvwFUASg9HeHOGteGWKC8PTl8WwmcYwy1JqYgjrYLHM7uOFJ9evb4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای عجیب در تجمعات شبانه: حسن روحانی در یک سفر استانی دستور داد برای دستشویی‌اش کولر نصب کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72746" target="_blank">📅 23:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72745">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7673e09822.mp4?token=DcEm1MKiQ2qQbN2t3OGz3y-1Z_U2GH-knZZaKexBkj1RJyvqrMn39Ih-DarGsIuQYLgVMcyQVWzdOB-m_qA8OJJErlViR3XAcLaxpRjJgTpdUrOdlVYO_6pOFKkSegshRj1q01uBqGsTwot7tVftXY5bK1M0DRi6UdgJ1hyD6GmCEuDPl_aTjrDN5vJiPcLYqEyYP9730XCANvn1hh6rqnHHK1UIyyOS_dqjEPmDcaD5xsXi1NEjByqddJK5jvVF0MwJpyuTNs_UCKV1_ocRKMxdagUnStS8z53_lkalEoil_Kihu9Co2eN2_WcEEz0cHE8JiYOYBDCps3EIttNtKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7673e09822.mp4?token=DcEm1MKiQ2qQbN2t3OGz3y-1Z_U2GH-knZZaKexBkj1RJyvqrMn39Ih-DarGsIuQYLgVMcyQVWzdOB-m_qA8OJJErlViR3XAcLaxpRjJgTpdUrOdlVYO_6pOFKkSegshRj1q01uBqGsTwot7tVftXY5bK1M0DRi6UdgJ1hyD6GmCEuDPl_aTjrDN5vJiPcLYqEyYP9730XCANvn1hh6rqnHHK1UIyyOS_dqjEPmDcaD5xsXi1NEjByqddJK5jvVF0MwJpyuTNs_UCKV1_ocRKMxdagUnStS8z53_lkalEoil_Kihu9Co2eN2_WcEEz0cHE8JiYOYBDCps3EIttNtKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سیل اخیرِ گرگان، یه
موش
برای اینکه جونشو نجات بده، این شکلی داشت تلاش می‌کرد...!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72745" target="_blank">📅 23:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72744">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bffb33370b.mp4?token=OxXGjIolj5pSY-1ohqfLHeX7Q-Rx6TPWzsH7OeHTfCRuMNxWBpX8XljqA6QWo6CmB8b8tfbZqIL0TQdym_kqKJYjbxOqyivP-Htv8obNeywBbO0xWdO9_AKWWPfLHOV6I2qU7SKtm6tXDWLZ74ykrykC9rnXk6wZOXodoeeP768vLTI9mcJPPmogT1qZPlyWUThdpIFIfRuuMgmi9vcbFrDSD2NJHAbnmItrbeO3WcRCPnWLb_mPcxIK4yMI1Mk-8TIz9rrUASUDDVrPJi1g-J80aI0CmC9M-QaPX6QyubpQQNL-_6BJSh7lYFYpw6YEIlQlvp8FjNhWl9GhY4yjYYQjT2PZ4BZq66cY-p0h4CBSMZDyTE1XL1_j_aEK417cU5rpfTXyvIgFV4Gg_5aapGV_8TzOa0gfyigIGhiztC9U5PqdwcLx_YmiCbTg9y__tywCTP1FA7eDwOTQz4Gp72uRlV9b8tTDJZgBoQSsCeRM05SoJCaJiOhY9AvFKQzgUVY69t4fJ961n4-Kc26Xlo_oLTpGAporfestcN0fgd2i3pFf5ZrT-d7R_Bu2qGcwZsJ8tzPYDzh1YmcT7Qp4AQoBQilsVx6FYdj6KDfvQSPocD_TGgRwvrIum5joSeRQHOfRyFOdD9hHYFaoc_pO9rw6yvfBWh1HoglFrpeSjNU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bffb33370b.mp4?token=OxXGjIolj5pSY-1ohqfLHeX7Q-Rx6TPWzsH7OeHTfCRuMNxWBpX8XljqA6QWo6CmB8b8tfbZqIL0TQdym_kqKJYjbxOqyivP-Htv8obNeywBbO0xWdO9_AKWWPfLHOV6I2qU7SKtm6tXDWLZ74ykrykC9rnXk6wZOXodoeeP768vLTI9mcJPPmogT1qZPlyWUThdpIFIfRuuMgmi9vcbFrDSD2NJHAbnmItrbeO3WcRCPnWLb_mPcxIK4yMI1Mk-8TIz9rrUASUDDVrPJi1g-J80aI0CmC9M-QaPX6QyubpQQNL-_6BJSh7lYFYpw6YEIlQlvp8FjNhWl9GhY4yjYYQjT2PZ4BZq66cY-p0h4CBSMZDyTE1XL1_j_aEK417cU5rpfTXyvIgFV4Gg_5aapGV_8TzOa0gfyigIGhiztC9U5PqdwcLx_YmiCbTg9y__tywCTP1FA7eDwOTQz4Gp72uRlV9b8tTDJZgBoQSsCeRM05SoJCaJiOhY9AvFKQzgUVY69t4fJ961n4-Kc26Xlo_oLTpGAporfestcN0fgd2i3pFf5ZrT-d7R_Bu2qGcwZsJ8tzPYDzh1YmcT7Qp4AQoBQilsVx6FYdj6KDfvQSPocD_TGgRwvrIum5joSeRQHOfRyFOdD9hHYFaoc_pO9rw6yvfBWh1HoglFrpeSjNU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک جانفدایان در اصفهان، سازماندهی اراذل و اوباش با قمه و شمشیر و چاقو!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72744" target="_blank">📅 22:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72743">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzocfCyvuEquKTPBUucV8FJXLEuiN9R_F_vtd39tl3vVT32vbakSwsbtnr9KYpaBfcdRshetWYg9qmeFKLY_H3gTgChF_crMAhdb1QDXGiMURu4vybEaEmjKbt1P3OCmh4IxtukXe9F12w84zXYZAjQX_Ev6aPLj-5wXtevCZOrMHAYgxHgXr3fFddvhVNnqvsy8MZjajd7cqiAg3-LsCLIfowe0FUXk0bs12Fa_q7W20gGRl9AyoYSaD0EjfZQhYgkqzM5G6ESmGjcsfFUUL36FtkYd-JRjsEw-GBy_Go2xHZI0vaqoM9rQQF-PGP-0kt3P7Yjp28iY-cl2vnBmyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ تصویری از خود به همراه پنگوئن‌ها در گرینلند منتشر کرد.
پنگوئن‌ها در گرینلند زندگی نمی‌کنند
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72743" target="_blank">📅 21:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72742">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">شنیده شدن صدای انفجار در جزیره قشم   @News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72742" target="_blank">📅 21:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72741">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">شنیده شدن صدای انفجار در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72741" target="_blank">📅 21:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72740">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d25df363a1.mp4?token=XWCvx-Xoi3-zS9ih_J3fai8sUI20OCY39ChHsZOeaHEgO6eka2eko8V7_EBXisto2QD0oKPO__B4YM6CkUi44TuONnyrnQlXJSQHufK_LrS9F4n3nKhpKcsnU47b495j2sxCCAZutFL0ZYPn8bZew8nJ0aMRFm1ls3j1kp3lh2iyvHhtMwr1IHnqhY8PnE-VJAEgENp2toNGmqIBDAPYxNziaqOaWWL2Q9AIUKEkjF26-URe6w20lJclyozDbR-BcFuRrve7BhaDjREBTTsnhct3hd2blyhYP1Wa3IWixXYo-TIiojL47872L2ALr_VbQrrZEqr7aVAy3_jjq24wBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d25df363a1.mp4?token=XWCvx-Xoi3-zS9ih_J3fai8sUI20OCY39ChHsZOeaHEgO6eka2eko8V7_EBXisto2QD0oKPO__B4YM6CkUi44TuONnyrnQlXJSQHufK_LrS9F4n3nKhpKcsnU47b495j2sxCCAZutFL0ZYPn8bZew8nJ0aMRFm1ls3j1kp3lh2iyvHhtMwr1IHnqhY8PnE-VJAEgENp2toNGmqIBDAPYxNziaqOaWWL2Q9AIUKEkjF26-URe6w20lJclyozDbR-BcFuRrve7BhaDjREBTTsnhct3hd2blyhYP1Wa3IWixXYo-TIiojL47872L2ALr_VbQrrZEqr7aVAy3_jjq24wBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۰فروند از ۱۲ بمب‌افکن راهبردی B-1B Lancer نیروی هوایی ایالات متحده که در پایگاه «آر.ای.اف فیرفورد» (RAF Fairford) انگلستان مستقر بودند، در حال ترک این پایگاه و بازگشت به خاک اصلی آمریکا هستند. انتظار می‌رود دو فروند باقی‌مانده نیز امروز این پایگاه را ترک کنند؛ بدین ترتیب، دیگر هیچ بمب‌افکن راهبردی‌ای در «آر.ای.اف فیرفورد» حضور نخواهد داشت.
پنیک نکنید!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72740" target="_blank">📅 20:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72739">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtya6Sv8nW8oOKNRPoCxKGE8ezPZ8N26C6CMfmjKKKX-uRp243ep_2W40QUcRpDQqblExFlu7Ww0jK2z_N5n9tg7YoGbG5NmywpmID5wSkXnrx7xbm57nuzE3p_30A-hI8c2zkoHwofK68U4UWWh14s_QnY_OZ6OAEYkC5YWLYN9nr7-LjJ1dYFaUg34BXfWiLLEooGQrkwT6MWqRqDlogC2ojePMwg5mkoJ2tCCPl4H0_dPKuI-YltRG-QARHn5TYPPX_5mFDuoNpRnDEexYLdtuoD8LfcFPXakIrh_RtDPoVH_zixAERmjio3N_p3F0tPnrXYm7UPq1Qkkch9iAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی، استعفا داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72739" target="_blank">📅 20:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72736">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1dad032a8.mp4?token=gQcY2gMmK3zxiae8akzNTB2MzcIGsHW4v5lbppgtwkD7FixVu1HaVBcmlo76z21U26gWr79wfdtzIBm-TNnF48UbVtdb0hOc1hsqeNZ-DvfVnh1d3421nah00zgEUTjca69LeNxE8iCOa6GM_E48PovZF7Eq6DkJPKmhPhTvwnFD3pJtyZ4Ni8EWaSKX9dzyCmBstuoMRXeOyy_lUgR4VjA0xcljJ8cKgoDvJNAMcs0CtiZJUznKXgcoRfoWcecZ7nyrHHeancnxvearWpaPlEgPfe6l7M_lVn_UQlhTovppsCTnIlnm65jv0OhaMY6mdJggocjPB8Wk0b9sBPthmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1dad032a8.mp4?token=gQcY2gMmK3zxiae8akzNTB2MzcIGsHW4v5lbppgtwkD7FixVu1HaVBcmlo76z21U26gWr79wfdtzIBm-TNnF48UbVtdb0hOc1hsqeNZ-DvfVnh1d3421nah00zgEUTjca69LeNxE8iCOa6GM_E48PovZF7Eq6DkJPKmhPhTvwnFD3pJtyZ4Ni8EWaSKX9dzyCmBstuoMRXeOyy_lUgR4VjA0xcljJ8cKgoDvJNAMcs0CtiZJUznKXgcoRfoWcecZ7nyrHHeancnxvearWpaPlEgPfe6l7M_lVn_UQlhTovppsCTnIlnm65jv0OhaMY6mdJggocjPB8Wk0b9sBPthmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رتبه یک کنکور تجربی همین‌جوری داره بین موسسه‌های کنکوری دست به دست میشه و تو همشون میگه که من از بچگی اینجا بودم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72736" target="_blank">📅 20:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72735">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/112f06092b.mp4?token=aLSq3-monHuHXEztNh02HYJiOBQF4kXe_zEhwH_DGCB9Rx7b1rLKEapE1omAhuCTDC0zQe9N2ILg5klWwtnC-3bQfw3SlmIMTMrV0cBK1V9XTmz4_mjWnIh9mM9Ratc2c2GR5dGHLLAnfJ-eIKXVvnWfYmnzpp6tbzz8zkkg191vg_Th0LRLQjzMpXjLW1HgYNIlkoui9ygSHgWKq_7ev7YtwUIZ53lu8Z31QTkjpPMPNmI7kZCv5bkXb3_s70N8EQGwnbo18mWxttLG2Kkf6gBjrU9GlHt52R1S1qzEfulZFsTh-TznTQJMxLqSkeHQqOQlsmLFkzpWtYf-4eOK82Zm4Aw7PJxZf-Zy2dhdpb6ZRkV3eZG4zS19v7gMRwRK8F_7K6Xpw8ZbCpWUugCNQUAzhwXyGU34Ky278-QJ7nvCEDodvw09Er-JJTqxIxbxoeMnwdeWyak6IQtOLSmfqlHh32GjYeuKseT6RQAeOo95c0C_gMy1cD0SvOb3shqdLtmmt8qNbvRHWqTz03qRxbqFIT7AIqM-dYOFWixFFTTFX25wBwfHqkXzqp9iepC8tJQrqjsCmpDJMhL63s0AmF-F8mehskvNhe1DsIkwHgBVQPOn9kF9Yta3iVYXJly4SJwFyV8m6MKKbVjudp9Qeo5au3cExOQtjwpE8LENCM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/112f06092b.mp4?token=aLSq3-monHuHXEztNh02HYJiOBQF4kXe_zEhwH_DGCB9Rx7b1rLKEapE1omAhuCTDC0zQe9N2ILg5klWwtnC-3bQfw3SlmIMTMrV0cBK1V9XTmz4_mjWnIh9mM9Ratc2c2GR5dGHLLAnfJ-eIKXVvnWfYmnzpp6tbzz8zkkg191vg_Th0LRLQjzMpXjLW1HgYNIlkoui9ygSHgWKq_7ev7YtwUIZ53lu8Z31QTkjpPMPNmI7kZCv5bkXb3_s70N8EQGwnbo18mWxttLG2Kkf6gBjrU9GlHt52R1S1qzEfulZFsTh-TznTQJMxLqSkeHQqOQlsmLFkzpWtYf-4eOK82Zm4Aw7PJxZf-Zy2dhdpb6ZRkV3eZG4zS19v7gMRwRK8F_7K6Xpw8ZbCpWUugCNQUAzhwXyGU34Ky278-QJ7nvCEDodvw09Er-JJTqxIxbxoeMnwdeWyak6IQtOLSmfqlHh32GjYeuKseT6RQAeOo95c0C_gMy1cD0SvOb3shqdLtmmt8qNbvRHWqTz03qRxbqFIT7AIqM-dYOFWixFFTTFX25wBwfHqkXzqp9iepC8tJQrqjsCmpDJMhL63s0AmF-F8mehskvNhe1DsIkwHgBVQPOn9kF9Yta3iVYXJly4SJwFyV8m6MKKbVjudp9Qeo5au3cExOQtjwpE8LENCM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهنشاه محمدرضا پهلوی:
"همیشه تلاش میشود ایرانِ دوران من با بهترین دموکراسی‌های جهان مقایسه شود، ایرادی هم به آن ندارم.
اما درباره اینها (ج.ا) که چنین قتل‌عام میکنند همه می‌گویند بگذارید درک‌شان کنیم، بالاخره اسلام وضع ویژه‌ای دارد، در حالیکه آنچه اینها (ج.ا) می‌کنند، در تناقض با اسلام است.
حتی در لیبرال‌ترین محافل، دوران من با بی‌نقص‌ترین دموکراسی‌ها قیاس می‌شود اما به اینها که می‌رسد می‌گویند بگذارید درک‌شان کنیم، اجازه دهید با آنها دیالوگ برقرار کنیم.
این چیزی است که برای من قابل درک نیست."
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72735" target="_blank">📅 19:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72734">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe642fca6.mp4?token=JMUwzEqpJP2sjRCw8gpTtNU0lQIrjF0RK1mZSB2hVUhvqmDUPT9YZzOiBYWOdpPTH9pLNxfP9c9jA8Aw37hZH-mnQe5eZjmzx4X46CQB981xXTw2TF3PbmzxM01iWRE-Pq-KxuwCqiHyoIXA56j06n1Df2GYeFIxDQcWzBFleZ60hPGuUUQbZswZ6cqYaJoVYFqghiAbEGQKcGOho2Uptgjf9a2qtK6pmZHb9T-eQTjz5yPWOZXx7k_NL9UEls4zDjXcxRh-F2LGHGeunY7X7nBWpq2WuJYzymqHZsY5QbUjwLIVJF-spGIzKcgHydfKpceA7H6xmOD_JnAk9vtzxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe642fca6.mp4?token=JMUwzEqpJP2sjRCw8gpTtNU0lQIrjF0RK1mZSB2hVUhvqmDUPT9YZzOiBYWOdpPTH9pLNxfP9c9jA8Aw37hZH-mnQe5eZjmzx4X46CQB981xXTw2TF3PbmzxM01iWRE-Pq-KxuwCqiHyoIXA56j06n1Df2GYeFIxDQcWzBFleZ60hPGuUUQbZswZ6cqYaJoVYFqghiAbEGQKcGOho2Uptgjf9a2qtK6pmZHb9T-eQTjz5yPWOZXx7k_NL9UEls4zDjXcxRh-F2LGHGeunY7X7nBWpq2WuJYzymqHZsY5QbUjwLIVJF-spGIzKcgHydfKpceA7H6xmOD_JnAk9vtzxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگنده های عربستان سعودی مقر نیروهای خودی را بعد از اینکه به تصرف حوثی ها درآمد، در تعز یمن بمباران کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72734" target="_blank">📅 18:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72733">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMaIiBKSTuxI_lkeE_IMPfwdYsrXkMj24jsOTJGUQnFLhLZJHtvxLCldLSV1lGFAVOzJLizRJj1zv2TaSbDDSpfHO6TRosyFudDpCI-XQuqUkE2ZYXSC2BeiXSOAxLmq5C2xQ4qT-ammhEETs-UgieSDE4_XVtZthYULp7MUHWcCFVVcORiQR5oaM5qftE9QnOLDgzfNp8Sy7BqbKt2hE174Uo3kLfHZdKVq6Jug7NZ6jKzuyWTJNNicJa6q9V0nK4Bu8NskLdAZ55oQGO8q5x0H8OK_A5i7JU2w96fEUkUB2bSqzOaxLkGmkIKPRwEDDWyT29ERcHkcgK-QyGA0kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده با ارائه کمک‌های اطلاعاتی و پشتیبانی در تعیین اهداف، از عملیات تهاجمی تحت حمایت عربستان علیه حوثی‌ها پشتیبانی می‌کند، اما به‌طور مستقیم در نبرد مشارکت ندارد.
شاهزاده خالد بن سلمان، وزیر دفاع عربستان، از پیت هگسث، وزیر دفاع آمریکا، درخواست انجام حملات هوایی کرد؛ اما مقامات آمریکایی اعلام کردند که واشنگتن فعلاً قصد انجام «اقدام نظامی مستقیم» (عملیات کینتیک) را ندارد.
گزارش‌ها حاکی از آن است که فرماندهی مرکزی ایالات متحده (سنتکام) با انجام این حملات مخالف بوده و یمن را عاملی می‌داند که تمرکز آمریکا بر ایران را منحرف می‌کند.
@News_Hut
| Axios</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72733" target="_blank">📅 18:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72732">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9ee58a69b.mp4?token=ky5W8chamQ-L3pISWdRfsq0e6SFx5sRijDftivE5szc5UWB8RU6VmqgMj9PDhQopP9O7rxmrGXsE_6WOllqG6MBRta9qRtsVgeHVU1Jl8q9i-7cX19s6hF6oHqs_B5wO_2FtoIVV9Dvou5wIP-TzCkzzTBiE_O6VucgsbKiIINPbIs0XiNl1SNK5YO0V1uv9iQdgPu7cMNsbVlQ6e35D5t5J___ClMBjsOsVXl1s5GuSRQdbqeYFFKeKCBKlx0ggZ_X7rH8Sl-DpP7xLrsOsr7MorQRgcrnyhaOsiH8Mr2vldwdJ0i-VGRTIm1G6oLp_fSMxM9Vodfdcwk2bQh35Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9ee58a69b.mp4?token=ky5W8chamQ-L3pISWdRfsq0e6SFx5sRijDftivE5szc5UWB8RU6VmqgMj9PDhQopP9O7rxmrGXsE_6WOllqG6MBRta9qRtsVgeHVU1Jl8q9i-7cX19s6hF6oHqs_B5wO_2FtoIVV9Dvou5wIP-TzCkzzTBiE_O6VucgsbKiIINPbIs0XiNl1SNK5YO0V1uv9iQdgPu7cMNsbVlQ6e35D5t5J___ClMBjsOsVXl1s5GuSRQdbqeYFFKeKCBKlx0ggZ_X7rH8Sl-DpP7xLrsOsr7MorQRgcrnyhaOsiH8Mr2vldwdJ0i-VGRTIm1G6oLp_fSMxM9Vodfdcwk2bQh35Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش:
در جریان این جنگ به این نتیجه رسیدیم که قطعاً باید برد موشک‌های خود را به ۱۰۰۰ کیلومتر افزایش دهیم، زیرا دشمن در حال حاضر در فاصله‌ای دورتر از سواحل ما مستقر است.
اکنون در این مسیر گام برداشته‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72732" target="_blank">📅 18:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72731">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72731" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72731" target="_blank">📅 18:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72730">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmfhAOvNZ3y4hgDmuhzVNQGHuVtE0F1BzgNLEyT9B88KX9C4Lne-a1Pau_UR8ZgTwhMrtsl4GNDbPDMQJSjq4R7n6QN_Pn4On6fmRSefeuXJIOEC-5KU5cKRrqMHmwTVGhnwqSATyLXY5F65ChDTxzSbgoecqWj2DAgTAKE5JydIYuaybLpzKJiG066JO9jGoUV9XIOTgcv53kqQP8g5nYR4RW60tm4VCCXX8tkbdpMvKz4DRr5cO9pl5V76TVjViNzYmpCX7sDAaitsskQ8hCt9X7h10KTmtxWKPRIOPWPDNJdKmHP5FzZBzjWFFVnZs2kVukEZKQyoibHVkoy4YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز نروژ
🆚
پرتغال را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
نروژ: ۲ برد، ۳ شکست و ۸ گل زده
پرتغال: ۴ برد، ۱ شکست و ۹ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72730" target="_blank">📅 18:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72727">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKiY6TT2IDJd8flplMrcJ4tke_55_VYhDJyhAJiv9EGM6uHRC6tAcEil6vvWvti2gHjmKpT9f4U-gDVH98QIeew76AIuqWTImPwe4cupCrbIZCEa9DpqgFk9t1gTkGxYvFSqVf7FKvwo39PuTn58h7DqQ4nzp0ZzEEFE5tbL_iqxLp2EJv76sadlFQ2kIXEEaPR2WjQ7kQnylgXHiNDiN2XKZBYTWDvzS0X9RAWg-tTUuV7a4nLPbySVyrtYRADbXP6g8eJibKvIl4dUjIts9x4aSFt7lchP1gjpqHIqFp3Vt0cMWHuN_5WVASwKHcqK7WhlUs93ittqvYgW_n87qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0214da517f.mp4?token=g4OiLDJslw_z6Jh563mniWL6Y2jVGZrkNeKJGocK96RPjJFW6wQBdoh5sQhkuwgvi_hpZbBhq1vWHIFccqece32BoV3CUjldGOlGYtYDQp2Z2R5JcXbbIDF5bI4C2XZWUbf7UycrQsPSFA49b-9oc1FGQdgztW5elTnX6Yd8eXOHKeBRhgAjWMb6MfBvYmRlNQGC3R-Ny2mGAtw_SDmusiklwEoVG32aufw442qBQMZw5tBOycba49GuFyR8hl6AiGqQA9UGyy2_OFqr6u-GDL8WuICFpDagFdc-UTp8ClHYENTa2mBNYVluzxXol5zPklTk-x4vx_yfSBsS_8OY9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0214da517f.mp4?token=g4OiLDJslw_z6Jh563mniWL6Y2jVGZrkNeKJGocK96RPjJFW6wQBdoh5sQhkuwgvi_hpZbBhq1vWHIFccqece32BoV3CUjldGOlGYtYDQp2Z2R5JcXbbIDF5bI4C2XZWUbf7UycrQsPSFA49b-9oc1FGQdgztW5elTnX6Yd8eXOHKeBRhgAjWMb6MfBvYmRlNQGC3R-Ny2mGAtw_SDmusiklwEoVG32aufw442qBQMZw5tBOycba49GuFyR8hl6AiGqQA9UGyy2_OFqr6u-GDL8WuICFpDagFdc-UTp8ClHYENTa2mBNYVluzxXol5zPklTk-x4vx_yfSBsS_8OY9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به نظر می‌رسد نیروهای انصارالله موفق شده‌اند کنترل منطقه «البرقانی» در شمال «الصفیه» و در محور جنوبی تعز را به دست بگیرند.
در ویدئویی که منتشر شده، نیروهای حوثی هنگام ورود به خانه «سلطان البرکانی»، رئیس پارلمان شورای رهبری ریاست‌جمهوری یمن (PLC)، و تصرف آن دیده می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72727" target="_blank">📅 17:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72726">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9e96757a.mp4?token=RA0GFBiKm1R5n6Jv096LESY0XC71hFcWh2OXvptBlB9AU-K2D_d2_qH5Y3b9EW-uk7NFCSBPr5sWe-peKCnIQMUWucJNE32Yv44jmx2GjpSAy457pBaZxEGOecQ5_c4hvGMEYpQPJ-XTk_-4SF9XoOliRXBquEkJh8FSTXATM7AtZhh-sv6DUn-LoPKBA5ilvm6JX-upLgA72KUtJaFv87G15aUxj1AljDsilXtP5eosWhODQxNJcRMuMoSDsXgPy5GoUW_aiNk-66EeSFDdTJao75kjRiMCP7kNYfD9dwFCjyFEOEHsXNJws-_SNFuwiqWYRcpxvyhVpqJIbM4d1iu-1Q1SEWn3qsYBXrm6dJso5yQudljS6qk-UJJWzGg2auTta9-2wixwLTU_zmPh0lAq0WUIideMFQzZjxjMnQ3sjNMulWCyznfOVmQsh49ubIq01uQgHb9xrCXa1c-WDZ0vYwxvmpxxyn0n14EHIoLWfb5t5s9tGa9sbXunEA84uLgXY35Av931G7_r0nqOZHxR89bZ4tRf1DKX9C--pL_dAU82ZsvZsLizFdLZBHDIVNE3z0tIHXq2Vw0FflMrdmdnz7gY8rUnPbPPp6r9wMOqD98CLACqycrEADoYU7LHFjsgfLEuXPcakBxZqhZiQlHXQaUaNEegsM9Ry4_nqbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9e96757a.mp4?token=RA0GFBiKm1R5n6Jv096LESY0XC71hFcWh2OXvptBlB9AU-K2D_d2_qH5Y3b9EW-uk7NFCSBPr5sWe-peKCnIQMUWucJNE32Yv44jmx2GjpSAy457pBaZxEGOecQ5_c4hvGMEYpQPJ-XTk_-4SF9XoOliRXBquEkJh8FSTXATM7AtZhh-sv6DUn-LoPKBA5ilvm6JX-upLgA72KUtJaFv87G15aUxj1AljDsilXtP5eosWhODQxNJcRMuMoSDsXgPy5GoUW_aiNk-66EeSFDdTJao75kjRiMCP7kNYfD9dwFCjyFEOEHsXNJws-_SNFuwiqWYRcpxvyhVpqJIbM4d1iu-1Q1SEWn3qsYBXrm6dJso5yQudljS6qk-UJJWzGg2auTta9-2wixwLTU_zmPh0lAq0WUIideMFQzZjxjMnQ3sjNMulWCyznfOVmQsh49ubIq01uQgHb9xrCXa1c-WDZ0vYwxvmpxxyn0n14EHIoLWfb5t5s9tGa9sbXunEA84uLgXY35Av931G7_r0nqOZHxR89bZ4tRf1DKX9C--pL_dAU82ZsvZsLizFdLZBHDIVNE3z0tIHXq2Vw0FflMrdmdnz7gY8rUnPbPPp6r9wMOqD98CLACqycrEADoYU7LHFjsgfLEuXPcakBxZqhZiQlHXQaUaNEegsM9Ry4_nqbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛رشاد العلیمی، رئیس «شورای رهبری ریاست‌جمهوری» (PLC) یمن که مورد حمایت عربستان سعودی است، از آغاز عملیات نظامی تمام‌عیار در تمامی جبهه‌ها برای بازپس‌گیری مناطق تحت کنترل حوثی‌ها (انصارالله) و احیای حاکمیت این شورا در سراسر کشور خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72726" target="_blank">📅 17:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72725">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05733ed2f5.mp4?token=dSKijXYBdh_L-nvdaCfNu8jkQGPKLi_GJJR3dxeVVQQK7C3VlPYEaos6Hl4fpomGEFlbjZjuAvhu2OgwpqXTV_vQFUspDOeBTeMNUgySUgSf80JBFLLUmX1oB9Hrg2EDSCHCG6e9KB2JkRucM_Wk1mvIp2H5ZmdmGhjCCXZHffJw_OV_T7IFsWcbGA3CNIUuRWG4Ik6b0dMI4MrbBceYVrLFzc6CCng1oz0q5AR8vE4Ve2XBuMcN6he0A1xcdQF_iUaqT6W5hkoUNzytHQybdkiR8NTxDdonSL0LpEZX8WHeWco-qE9xTvwrAsnPVqWR6mMwk8ZN52Y28P5q3-Z6_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05733ed2f5.mp4?token=dSKijXYBdh_L-nvdaCfNu8jkQGPKLi_GJJR3dxeVVQQK7C3VlPYEaos6Hl4fpomGEFlbjZjuAvhu2OgwpqXTV_vQFUspDOeBTeMNUgySUgSf80JBFLLUmX1oB9Hrg2EDSCHCG6e9KB2JkRucM_Wk1mvIp2H5ZmdmGhjCCXZHffJw_OV_T7IFsWcbGA3CNIUuRWG4Ik6b0dMI4MrbBceYVrLFzc6CCng1oz0q5AR8vE4Ve2XBuMcN6he0A1xcdQF_iUaqT6W5hkoUNzytHQybdkiR8NTxDdonSL0LpEZX8WHeWco-qE9xTvwrAsnPVqWR6mMwk8ZN52Y28P5q3-Z6_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پای رپر ها هم به تجمعات شبانه باز شده:
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72725" target="_blank">📅 17:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72724">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f15ab8539d.mp4?token=nfmRDc3dIGpD-34BMjcOF5EE5Es3gb3fYE-bkKRiEEAUjFU7upHtP37UPpelAAMDCoB8zi6Zx_00VoLRDSHjzAvoDizk8_Su6xoPcYKGVEOQ7o6TP47ccuHpz9AetVQZKOLBNWsf8X6FOMPFBoIDUJicwCcfF7KcOHfwXZndWehKDirekSpigIOuyse7YJPHZmIgmVm3-ncgfxiWRO4tK5TGI9padL6e4DyZQCyvl_lxFWpSgpKXbxIUlB2lUHwBZK_PEOIYxuNNl4VkkXle0xbfABkhC6DC7Lk5G1Js-g8eXzKFMgOHsW7ZoYkjW2IAhqsRlOO3tDdwfiv91b_EHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f15ab8539d.mp4?token=nfmRDc3dIGpD-34BMjcOF5EE5Es3gb3fYE-bkKRiEEAUjFU7upHtP37UPpelAAMDCoB8zi6Zx_00VoLRDSHjzAvoDizk8_Su6xoPcYKGVEOQ7o6TP47ccuHpz9AetVQZKOLBNWsf8X6FOMPFBoIDUJicwCcfF7KcOHfwXZndWehKDirekSpigIOuyse7YJPHZmIgmVm3-ncgfxiWRO4tK5TGI9padL6e4DyZQCyvl_lxFWpSgpKXbxIUlB2lUHwBZK_PEOIYxuNNl4VkkXle0xbfABkhC6DC7Lk5G1Js-g8eXzKFMgOHsW7ZoYkjW2IAhqsRlOO3tDdwfiv91b_EHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه زنه داشت از حس و حالِ ناراحت پسرش تو روز اول مهر فیلم می‌گرفت که یهو یه مرده اومد و این شاهکار رو گفت:
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72724" target="_blank">📅 16:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72723">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5caffe71ff.mp4?token=W0eXrW397cAEdFgQ5Vi4-BM8pTI-qgnvAoo60G4O8UEX11czDrUioqxYI-Ui8hy7TMH4-oxx-E7FO9fH1pzxq8j-SHduZ_Ge-nkfB00i3_l86yKxfR3QlIsRpPIQ0AjEwvlayeqlaCbjw0h-oF9CcEcRixBMUGhA3y1g2ONmEqmhLKUutHxQ78SsSwsCpSmuU6-qhwgjNrVrQXhiycoi_i70jr6Z4zSJJVATuq8Ys_qmPEBymuDMpZPdTBMdG8MfgenJopgYSWMsD2iTrNzBa06GzxxIDIBkPYl_chYfVLOArrC576g7ukGWRndu3E2PMxbBuroLV-1XE96T4A_sbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5caffe71ff.mp4?token=W0eXrW397cAEdFgQ5Vi4-BM8pTI-qgnvAoo60G4O8UEX11czDrUioqxYI-Ui8hy7TMH4-oxx-E7FO9fH1pzxq8j-SHduZ_Ge-nkfB00i3_l86yKxfR3QlIsRpPIQ0AjEwvlayeqlaCbjw0h-oF9CcEcRixBMUGhA3y1g2ONmEqmhLKUutHxQ78SsSwsCpSmuU6-qhwgjNrVrQXhiycoi_i70jr6Z4zSJJVATuq8Ys_qmPEBymuDMpZPdTBMdG8MfgenJopgYSWMsD2iTrNzBa06GzxxIDIBkPYl_chYfVLOArrC576g7ukGWRndu3E2PMxbBuroLV-1XE96T4A_sbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو مکزیک  یه گزارشگر داشت از وضعیت خرابیِ کنار جاده گزارش تهیه میکرد که همون لحظه یه ماشین لیز میخوره و تصمیم میگیره گزارشگر و فیلمبردار رو با دیوار یکی کنه :
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72723" target="_blank">📅 15:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72722">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf8cf90e0c.mp4?token=FULAkLCUhMDIGOJXqoNXTEmABlDHsieOyyX0H4XTlCRnHs6YSNX01ZN0Ugrne2lWZnzlNFAWj9m8j442hXfV2WrpiawBWYCxl3786tMhdRqgLvYLvZOs0GVsInRpZmnIQLpSASMEEuPV1qAMVrehdSOZm7vhCPJBZD00476q39aabETZ5k-WtxIQuyY9_JsV-b1o8VAUh5emk8Sfr8KOBz2PMdS_to6oM7rTBh0QQ7Po1S2YoRiTV5ZuWs8mbB9-eU3I8LdPMpypZUSHimSD7jjla8QtxTLwoQ8WrHfYz3RxPOr1LanNyTWTil5guK4Gt-Y4Nw6OguEmfBV5LfRMKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf8cf90e0c.mp4?token=FULAkLCUhMDIGOJXqoNXTEmABlDHsieOyyX0H4XTlCRnHs6YSNX01ZN0Ugrne2lWZnzlNFAWj9m8j442hXfV2WrpiawBWYCxl3786tMhdRqgLvYLvZOs0GVsInRpZmnIQLpSASMEEuPV1qAMVrehdSOZm7vhCPJBZD00476q39aabETZ5k-WtxIQuyY9_JsV-b1o8VAUh5emk8Sfr8KOBz2PMdS_to6oM7rTBh0QQ7Po1S2YoRiTV5ZuWs8mbB9-eU3I8LdPMpypZUSHimSD7jjla8QtxTLwoQ8WrHfYz3RxPOr1LanNyTWTil5guK4Gt-Y4Nw6OguEmfBV5LfRMKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فریادهای مهدی کوچک‌زاده نماینده مجلس بر سر همتی رئیس بانک مرکزی؛
کوچک‌زاده:
مملکت را دارند به آمریکا میفروشند.
«به خدا اگر از جهنم به خاطر کوتاهی‌هایی که در حق شما مردم کردم نمی‌ترسیدم، امروز خودم را جلوی بانک مرکزی آتش می‌زدم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72722" target="_blank">📅 15:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72721">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d26538e463.mp4?token=D9uB1gCSBNFBu5nG40bctOEBot-D455vJ7Wm9G1fGbWYgtyfWpX45-RdUGrRnL2Evdx2DtJVVehAjaJkx-0TJPMtqaa6V36AKj5-HnsppF6lNbdazgxuZZQmQ2wLxojCLe_oGYMtOmdvqB7z3A9ZTrSR7kgh0B1aRVH_yLuaCV14xB_dobIY4BdWksJrntGeguc0WEpyfUHXnaT1TPil0u8MHuTshxFUrhXDXtj8zzX8Xj-kRcog6JiPBrsOy-D3vSJf1euq9uFFdeTYBZaP_aGsA0PqostVPggv5mS0Atpf5uo4VjIVwCdQszgW0WHDAypXDRkzXFGyxrvJ7No7AJYNzzoAPp_UDxGFpmyQy4tmljYH7g2SDELMtoXDRYkhmEIXZ7_M5sGiF1YAyQZCHpOKt_YQYpbRDK8zOoCxGd9pfIqV-BpDFrYljTXccmZSmBl9VLavG_WJI1wfIVBP8QgJMF8ic27R076x9ralB8UFREq11gYL1wgw-tycsFFiu3SwnVdPk0wKrfeq0lzpZYRBrilb8uX4kdP95gzlDJElz3kIZ2xRW-Eq_EQpHzEGp9hxoGYBbNVUTZ0xEzVlTNvzDHxb6pl_PGCUKhyl9GR5erSMd0WvJshnmYzNlz2lxM3JZYrQ2qiH0XsiQV4pDyzELS3S9BhoTPl6tjSbAXE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d26538e463.mp4?token=D9uB1gCSBNFBu5nG40bctOEBot-D455vJ7Wm9G1fGbWYgtyfWpX45-RdUGrRnL2Evdx2DtJVVehAjaJkx-0TJPMtqaa6V36AKj5-HnsppF6lNbdazgxuZZQmQ2wLxojCLe_oGYMtOmdvqB7z3A9ZTrSR7kgh0B1aRVH_yLuaCV14xB_dobIY4BdWksJrntGeguc0WEpyfUHXnaT1TPil0u8MHuTshxFUrhXDXtj8zzX8Xj-kRcog6JiPBrsOy-D3vSJf1euq9uFFdeTYBZaP_aGsA0PqostVPggv5mS0Atpf5uo4VjIVwCdQszgW0WHDAypXDRkzXFGyxrvJ7No7AJYNzzoAPp_UDxGFpmyQy4tmljYH7g2SDELMtoXDRYkhmEIXZ7_M5sGiF1YAyQZCHpOKt_YQYpbRDK8zOoCxGd9pfIqV-BpDFrYljTXccmZSmBl9VLavG_WJI1wfIVBP8QgJMF8ic27R076x9ralB8UFREq11gYL1wgw-tycsFFiu3SwnVdPk0wKrfeq0lzpZYRBrilb8uX4kdP95gzlDJElz3kIZ2xRW-Eq_EQpHzEGp9hxoGYBbNVUTZ0xEzVlTNvzDHxb6pl_PGCUKhyl9GR5erSMd0WvJshnmYzNlz2lxM3JZYrQ2qiH0XsiQV4pDyzELS3S9BhoTPl6tjSbAXE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
من با کیم جونگ‌اون، رهبر کره شمالی، رابطه بسیار خوبی دارم.
وقتی طرف مقابل ۱۱۲ موشک هسته‌ای در اختیار دارد، خوب است که با هم کنار بیاییم.
اما تفاوت اینجاست: ایران هرگز موشک هسته‌ای نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72721" target="_blank">📅 14:56 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72720">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe93c3478.mp4?token=T72jCJqrsADUEZqTwULK5ZD0COowyDiukez0jla8ySc5B6_rwMFlIxHSY4ewHN8R3uPU6eK8y0PT3PtCW3zpibz6BmfchTHWrBAqwK_qeJ5y4VWgWoaXGc86vdeSJbsjo30LxuUk1WtQBBEZFaBlSZNopsFjFY8V0e6j3_O-gFkgdNMuNwTSPlskzwcKT4L90h7e4A5seNDvu5DZPLKHS74mUDc_5VrLNpyjZlLizr8lOMwUjJsII4cMRAhez0EGH3Oo_Z2OJXAvxQqN25isD1zX502RPm9r0BGrCb3bqT8t43XC3sPjVQVGMVA2ZHXva9ERZnih0VNuSBxfRlZuZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe93c3478.mp4?token=T72jCJqrsADUEZqTwULK5ZD0COowyDiukez0jla8ySc5B6_rwMFlIxHSY4ewHN8R3uPU6eK8y0PT3PtCW3zpibz6BmfchTHWrBAqwK_qeJ5y4VWgWoaXGc86vdeSJbsjo30LxuUk1WtQBBEZFaBlSZNopsFjFY8V0e6j3_O-gFkgdNMuNwTSPlskzwcKT4L90h7e4A5seNDvu5DZPLKHS74mUDc_5VrLNpyjZlLizr8lOMwUjJsII4cMRAhez0EGH3Oo_Z2OJXAvxQqN25isD1zX502RPm9r0BGrCb3bqT8t43XC3sPjVQVGMVA2ZHXva9ERZnih0VNuSBxfRlZuZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل بقایی سخنگوی وزارت خارجه جمهوری اسلامی :
بحث‌ها پیرامون خروج از پیمان منع گسترش سلاح‌های هسته‌ای (NPT) در محافل سیاسی ایران بسیار جدی است و وزارت امور خارجه به تصمیم مراجع ذی‌صلاح پایبند است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72720" target="_blank">📅 14:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72719">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7872ea066a.mp4?token=iYq8N5b4eW5KDBJoI-ZA5gbVwkrNc5jA__1pWcYYu6DxyFN3NdpBqqwRn6v3OqvBIF6KGgwia5xKSC4to_1wXm5OmB5BFZXmmlT9eYQaJjA3hYE67-aN_2-o4N9zjp5uE1dfwC64cqKmoDkMU0wQHsueyzQSAleYV3CF0ydmlKpEQt91UPtgfE7zyTSIW3pRqQBgNplLj_NzINOXYcI_vsCoTVSKZHTysdRigM_pov4fPxJ4_TcceMvWEk7jrf1hxgZ7lFAHCj8wnK6STwCyAVNAt0KVxoG4_1fTCCvcJEIS1WAwHzGmRKd1-Z_3khhB7TNMd3J1IhqD0kIG73wyuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7872ea066a.mp4?token=iYq8N5b4eW5KDBJoI-ZA5gbVwkrNc5jA__1pWcYYu6DxyFN3NdpBqqwRn6v3OqvBIF6KGgwia5xKSC4to_1wXm5OmB5BFZXmmlT9eYQaJjA3hYE67-aN_2-o4N9zjp5uE1dfwC64cqKmoDkMU0wQHsueyzQSAleYV3CF0ydmlKpEQt91UPtgfE7zyTSIW3pRqQBgNplLj_NzINOXYcI_vsCoTVSKZHTysdRigM_pov4fPxJ4_TcceMvWEk7jrf1hxgZ7lFAHCj8wnK6STwCyAVNAt0KVxoG4_1fTCCvcJEIS1WAwHzGmRKd1-Z_3khhB7TNMd3J1IhqD0kIG73wyuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکشنبه ۱۲مهرماه۱۴۰۵؛آتش‌سوزی در پاساژ خلیج‌فارس عسلویه به دلایلی نامعلوم:
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72719" target="_blank">📅 14:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72718">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCPLOy53lURpS79SE3F25roJwEgfS0fBOMtLyeN2gzchjJjekUUdr6lRu350WPMkxllvVBraBbpMJeRPvnzO1itPuhH7sSq1qq-JosDgoOCnkhirLVerpnVxInB5esJZVCSqtJk4jC9aZEBubSiDXphFIcqL672Sfnc2962j6FZcJ98HbUUpC3OG0ULGc-ZN2XD0k5QZP1-wezCmun2-IaiGuW-fneljIGW1iEvWrINX4t6XWJmNFlrwXHmzY5---utXEo2-FboKma_q9B73QFSgJGHMblJ0PQcvK-whQvV2kQfIrcGAzS-ZgweV8rn3hf1pGYq0wP92fjpjw-eJcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز تهران _ نجف که قبل از محاصره هوایی حوالی ۱۲ تا ۱۹میلیون تومان بود ، دوباره برقرار شده اما بیش از دوبرابر رفته رو قیمت و شده ۳۰ تا ۳۸ میلیون!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72718" target="_blank">📅 13:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72717">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3330937cb2.mp4?token=ZxBjER1I0M1TDAflSPf0THukkJk-XCf6ahEoh0cXqgwsh-6ltovj9MdQg_UK6rufriY15sl_oqwLe8kLX0Fwv4SJx_yH7ixdy2uueoJhlxrLqmeRZlFrfaijbS6h6rcI_wV4ncLRQk0sTLyOR4yf2DZXLJ3OIBQy86-Q_36I2cXpZvbsoo720t_4BjxDC9lqkcckV7CFYodGXj1wiHHs-AdPUk6y747kGz8kHQx6_3y0IV5AySCgHyKbXgvyMiCcRWbLKBrwOMbfED0MspqEB4tiE9H5weH69P2xTL7T0gy6aLeG8Fwvtcz40R9pBAAYEqpEoVjMGk5lbcfTkytOnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3330937cb2.mp4?token=ZxBjER1I0M1TDAflSPf0THukkJk-XCf6ahEoh0cXqgwsh-6ltovj9MdQg_UK6rufriY15sl_oqwLe8kLX0Fwv4SJx_yH7ixdy2uueoJhlxrLqmeRZlFrfaijbS6h6rcI_wV4ncLRQk0sTLyOR4yf2DZXLJ3OIBQy86-Q_36I2cXpZvbsoo720t_4BjxDC9lqkcckV7CFYodGXj1wiHHs-AdPUk6y747kGz8kHQx6_3y0IV5AySCgHyKbXgvyMiCcRWbLKBrwOMbfED0MspqEB4tiE9H5weH69P2xTL7T0gy6aLeG8Fwvtcz40R9pBAAYEqpEoVjMGk5lbcfTkytOnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش روسیه به پل شمالی در کی‌یف حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72717" target="_blank">📅 13:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72716">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=B-Q1_Pis4uV5Nuoxe7-xdrKRztjMfPHmLVGgyAglrkMTg5piIHdNX3y1WBDEVLEY5Z57_5EJR-lXfShTkyFlPIB3ywris8OtG5kRz_sVLZzSz2Kdpbxg9b3o50jfj62rrdaDOejBR8ZYFTeFdoPUTCRS_Fw8840DXO0bNYPqnbJXFHyT9aeUNuIHkdqvzr-AOA9MoqD-AuQDKy2Ht1n6rO5yJpn2dhNCKWK1QNP9ye4DlLOWhc0_lCf1sAs9IcmPmHxtxf4OQF7xyTAXppt-4EcTQpdNb8Wla1JiipOEOUolNlklZYqpRx_aLCHkr01M67or10qOyJdauU0VBJoHTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=B-Q1_Pis4uV5Nuoxe7-xdrKRztjMfPHmLVGgyAglrkMTg5piIHdNX3y1WBDEVLEY5Z57_5EJR-lXfShTkyFlPIB3ywris8OtG5kRz_sVLZzSz2Kdpbxg9b3o50jfj62rrdaDOejBR8ZYFTeFdoPUTCRS_Fw8840DXO0bNYPqnbJXFHyT9aeUNuIHkdqvzr-AOA9MoqD-AuQDKy2Ht1n6rO5yJpn2dhNCKWK1QNP9ye4DlLOWhc0_lCf1sAs9IcmPmHxtxf4OQF7xyTAXppt-4EcTQpdNb8Wla1JiipOEOUolNlklZYqpRx_aLCHkr01M67or10qOyJdauU0VBJoHTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حرکتی شاهکار نگهبانای ی شرکت رفتن با سلاح برنو بالن هواشناسی رو زدن و بعد زنگ زدن به سپاه گفتن پهپاد آمریکایی رو زدیم بیاید همین الان جایزمونو بدید
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72716" target="_blank">📅 12:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72715">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دلار ۲۷۱.۰۰۰تومان
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72715" target="_blank">📅 12:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72714">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da8647691.mp4?token=eZ_ASjGCLX4LQWtYNm1k416h2WdWx5npCpQKgBrMmNITCMzt6cw25bYxoOTtuzrMK0aj0ttCzkHeDUE5WtP-CbPoe6s1peYVwSDK3okHlC_YEh3ttaKTrTlPnAJs2UQn7nF5Nq4O5gBjE6--lueGixQPIB44JClKM0HUrWf9BPKn14NhFUOjEsnxwDplQv0myFcX5j1524mQ5jF19vqQPIgGmIFXAZcH2ceLGF39MftQfnOSDEvboCfDrgn5ezXeKUOL9o1ZqSjVI1oMnwRvQz_flocLcqiPkmm-OJiIKWfggOgoGE_rMhGnggNu0O1abgnvOVVtkVeas-2lktXZIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da8647691.mp4?token=eZ_ASjGCLX4LQWtYNm1k416h2WdWx5npCpQKgBrMmNITCMzt6cw25bYxoOTtuzrMK0aj0ttCzkHeDUE5WtP-CbPoe6s1peYVwSDK3okHlC_YEh3ttaKTrTlPnAJs2UQn7nF5Nq4O5gBjE6--lueGixQPIB44JClKM0HUrWf9BPKn14NhFUOjEsnxwDplQv0myFcX5j1524mQ5jF19vqQPIgGmIFXAZcH2ceLGF39MftQfnOSDEvboCfDrgn5ezXeKUOL9o1ZqSjVI1oMnwRvQz_flocLcqiPkmm-OJiIKWfggOgoGE_rMhGnggNu0O1abgnvOVVtkVeas-2lktXZIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت بر سر قبر علی خامنه‌ای، علیه مسئولان نظام شعاردادند؛
«گرانی رو آوردن، سازش کنن با دشمن»
«مفسد اقتصادی، سرباز آمریکایی»
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72714" target="_blank">📅 11:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72713">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_iqKD-wjLWGS-SQ7bGGx_Ah0p7QH7PaytE9PWkZle4YVrgfWMwuB1Gkcd0oUBBaiGX-Jbg8r1atV1ixmu_CY6dTuxHsJusMk-vLksMtL93znJxjgLDANkiQEla3ZcaO05Y_fy_ImWmDecJ_R_T8HvBxhhIKFyM0DykGTz_JtVrxMHipo-TUw9bDUUUhlo7Hb6sYPiA6rQlcMNuuOdO8YJa-lVi1p7r67GagrjT2USjhWyu9YOLikD69mgvSmQJwUUAfAwd5OcKrW5diTlJEQZvyaoE4ab3tbgox7sFWn0ff1v8nr48AKLXs2V28QUNdXCVv6rqWJ0rwp-XaerIWMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش در داخل تنگه هرمز هدف یک پرتابه ناشناس قرار گرفته و موتورخانه آن آسیب دیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72713" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72712">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72712" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72711">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D39A8P8XQEKNzZV35sNMENVXRsTluE88SJ4V894Mew1s2xLELVR5VIYN_2Gw8r44MfgTmDjuwygpM8WhKIOZCdb1kzWwLQ_c9CkfawXn5EUelsi-G7rMICBVjxDDYB6qmgahvpUz0HAyo1dMH6NFAzmjuXGHH2JcMBd-2tdP3vLcVEdCL9os2ACMRGU4jeLotyrQRuux9-_E5ZqUkMY17TzRIyNZq0h0_gyMVtrCNYI7dfTGKeW8NMSbCnxs4X-sQaGGlLIsWkPQLGtflpbnk43qXwGFyJOCydxmdEsC6x1UxaiV0VZr74PFekBUiC-KeJtU4AEzkNYHWnqZdxuduQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آلمان
🆚
یونان
صربستان
🆚
هلند
نروژ
🆚
پرتغال
دانمارک
🆚
ولز
آفریقای جنوبی
🆚
مصر
مالی
🆚
مراکش
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72711" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72710">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50e9a4b7ef.mp4?token=nC8k65vIRt94dgecphu6mJmpw13d6dWU1Ke-MQmGE56PMpqVSdjiP6wBqNIPlJIeGwjn_cYISzN8uxP1wiGh4S4DEwM0nfV6oYrOfmjkyUS8u1DDyBezRxC8CCXVMDtEoDRu3JO-GaZwrKpgfcemv4Ryz5hdUISUygy-ygEFnJeCnJBvEa9w0IOHqjKnayJB-W0UF_dRdtBHDgV1IOcb_awQcQlPuBwkXfCxJqbep7zEXl3HOOyeK5eTsV7NLNX5TtyQtVJw_LkNF8pBzbcPO8YjsV6fwGjjUjXVLXbmtcWAJHA3yyJFgoVzwVJ2azbNqI58jntBIXFR0d8AcB25RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50e9a4b7ef.mp4?token=nC8k65vIRt94dgecphu6mJmpw13d6dWU1Ke-MQmGE56PMpqVSdjiP6wBqNIPlJIeGwjn_cYISzN8uxP1wiGh4S4DEwM0nfV6oYrOfmjkyUS8u1DDyBezRxC8CCXVMDtEoDRu3JO-GaZwrKpgfcemv4Ryz5hdUISUygy-ygEFnJeCnJBvEa9w0IOHqjKnayJB-W0UF_dRdtBHDgV1IOcb_awQcQlPuBwkXfCxJqbep7zEXl3HOOyeK5eTsV7NLNX5TtyQtVJw_LkNF8pBzbcPO8YjsV6fwGjjUjXVLXbmtcWAJHA3yyJFgoVzwVJ2azbNqI58jntBIXFR0d8AcB25RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بابایی، رئیس کمیسیون اجتماعی مجلس:
می‌خوایم حقوقِ کارمندان دولت رو 5 الی 10 میلیون تومن افزایش بدیم!
قراره «فوق‌العاده خاص کارکنان» تو کوتاه‌ترین زمان ممکن و با امتیاز 2 هزار تا 20 هزار واسه کارمندان اجرا بشه.
این افزایش از اول شهریور محاسبه میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72710" target="_blank">📅 11:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72709">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a343c0ae1.mp4?token=Ve4ubfZ19Yp6JjPbFIgXLLMH5O3jZ4w8bWXAzq4A-sP66cr4E4bX_d8TomOaBi06iZ-nIvlqNZq7moD9iBfoy7HM5A1WKdSxmqOxFA9R-WsNrgLnMy14R-F-tO0tGl2CrAyn7TAN4_qZAl91z0rCBNKgiwZRU9grvXyTk1Z3ZABAtGHHJCJkpl46bkJiwg_kNSDmNU8-9Y4bv5pjQwIrnAP6ELHk68HQ2e85G2aANVEQ8qT-hdTzl02MuPqukOyMPzgfFyPHdm3Xx1aJt1bJZBeYlmua9nymltADpR-tPZ67mTiyZcyXYSg51CAe74Xl1s4UAG4CVcbBpmUF6yNE9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a343c0ae1.mp4?token=Ve4ubfZ19Yp6JjPbFIgXLLMH5O3jZ4w8bWXAzq4A-sP66cr4E4bX_d8TomOaBi06iZ-nIvlqNZq7moD9iBfoy7HM5A1WKdSxmqOxFA9R-WsNrgLnMy14R-F-tO0tGl2CrAyn7TAN4_qZAl91z0rCBNKgiwZRU9grvXyTk1Z3ZABAtGHHJCJkpl46bkJiwg_kNSDmNU8-9Y4bv5pjQwIrnAP6ELHk68HQ2e85G2aANVEQ8qT-hdTzl02MuPqukOyMPzgfFyPHdm3Xx1aJt1bJZBeYlmua9nymltADpR-tPZ67mTiyZcyXYSg51CAe74Xl1s4UAG4CVcbBpmUF6yNE9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر خانوم 15 ساله به‌خاطر اینکه هر هفته پریود میشده به دکتر مراجعه میکنه تا بفهمه مشکلش چیه؛
بعد از اینکه معاینه میشه، دکترا متوجه میشن ایشون دو تا دهانه رحم و دو تا سوراخ واژن داره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72709" target="_blank">📅 11:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72708">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aed172c29.mp4?token=q3LeAGxhD6rMf823VPHTwF2JaCCAI3lbbf0l7kv6YFjpJ6s7Pju9rLKcz7bPOGqbie2xyK3lWu8yLt-PWGolXDAdH9w5OkSxIOefjqRgaRGR3qTkNsuKioTwaNsqPwN84wDqQ58aIpV9H3xPgSWlVCbkWmT5-3r-kwlKRci0gCVCMATR-NVCJZPEo9iPsgk9YOgEPHmA1aDsvN5Ep0EayToD_FQ6FrmG_PeEji2j8LO6XcSJwW7PPYiEoBYsIhsJDdGEa-uxdk4QmLx0WuwTQBROIBzyPseIzDne60ycz2Ucj4CONK9ZwbPRRstw-MEekLicxOdKcCf6FvvXvVErqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aed172c29.mp4?token=q3LeAGxhD6rMf823VPHTwF2JaCCAI3lbbf0l7kv6YFjpJ6s7Pju9rLKcz7bPOGqbie2xyK3lWu8yLt-PWGolXDAdH9w5OkSxIOefjqRgaRGR3qTkNsuKioTwaNsqPwN84wDqQ58aIpV9H3xPgSWlVCbkWmT5-3r-kwlKRci0gCVCMATR-NVCJZPEo9iPsgk9YOgEPHmA1aDsvN5Ep0EayToD_FQ6FrmG_PeEji2j8LO6XcSJwW7PPYiEoBYsIhsJDdGEa-uxdk4QmLx0WuwTQBROIBzyPseIzDne60ycz2Ucj4CONK9ZwbPRRstw-MEekLicxOdKcCf6FvvXvVErqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداوسیما:‌ حتی اگر بمب اتم بخوریم باز هم نابود نمی‌شویم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72708" target="_blank">📅 10:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72707">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9499513e9a.mp4?token=PPlte7_DnyYQn4-3Il81lcwVKo_TfOX4Z81CxklDtQS6T9evw6DUNsUd9ILdrp0DiBwGnOhhTewkg107VG5fHtXtILZwmI9BwN0c_ZBicWgx_cM1gWg7X6KJw_lcOMGU2XIw8H93fPQpDHT0LaYeCDPxBidUkvDUKYch1pidGH5Rz1t30O6zYxqeZZBQ62XiUUk03GtGA3absjWVlVjvk4u7sxtLAqqE30FDdfWCGe7kbJ8OxKMmNrLvBUSZevBLAlNTbdq4-4r78RnwfaZ6aBbgib224h_51lT11E4E_4j3850CFdms7cDxGMwFUYghnj9p7kQpZIJO4L9PNRa6DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9499513e9a.mp4?token=PPlte7_DnyYQn4-3Il81lcwVKo_TfOX4Z81CxklDtQS6T9evw6DUNsUd9ILdrp0DiBwGnOhhTewkg107VG5fHtXtILZwmI9BwN0c_ZBicWgx_cM1gWg7X6KJw_lcOMGU2XIw8H93fPQpDHT0LaYeCDPxBidUkvDUKYch1pidGH5Rz1t30O6zYxqeZZBQ62XiUUk03GtGA3absjWVlVjvk4u7sxtLAqqE30FDdfWCGe7kbJ8OxKMmNrLvBUSZevBLAlNTbdq4-4r78RnwfaZ6aBbgib224h_51lT11E4E_4j3850CFdms7cDxGMwFUYghnj9p7kQpZIJO4L9PNRa6DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه این مدرسه اس
پس ما کجا میرفتیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72707" target="_blank">📅 10:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72706">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8589525917.mp4?token=VDdGBR5S9V_8iu5WwwCpna3ipS6Vczh-t32m6QhBp9JitVqsLx_qADfeyb6zEsX3z7ssz1aY6y2WbXLWzk-7IIHdM8Hnk6alzpGv5MK0suB_Kwm1QFbUEkiUZG3L0Ld9I_25NbTbYtn8zYtwXBR9euVk9Bs_BPMpmQwrRDi3mbgFNK281rJB3UPC3_qPDwOEY0oM8r6gUtDmAITt85pPBq2DT2eXEvaHD7TfMEQi4AGLcOOP_iY8loLWtJo0eG4fbO6HqVBLrFtUJ1KfyJg0b3tSaHbgEZ1kXKHFA2PNXxPFGKG0VfpDG8YAqGexfVQS0SZDTbbW3M3hPUZeDUsubA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8589525917.mp4?token=VDdGBR5S9V_8iu5WwwCpna3ipS6Vczh-t32m6QhBp9JitVqsLx_qADfeyb6zEsX3z7ssz1aY6y2WbXLWzk-7IIHdM8Hnk6alzpGv5MK0suB_Kwm1QFbUEkiUZG3L0Ld9I_25NbTbYtn8zYtwXBR9euVk9Bs_BPMpmQwrRDi3mbgFNK281rJB3UPC3_qPDwOEY0oM8r6gUtDmAITt85pPBq2DT2eXEvaHD7TfMEQi4AGLcOOP_iY8loLWtJo0eG4fbO6HqVBLrFtUJ1KfyJg0b3tSaHbgEZ1kXKHFA2PNXxPFGKG0VfpDG8YAqGexfVQS0SZDTbbW3M3hPUZeDUsubA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در بخش‌هایی از کرج، از جمله باغستان و جهانشهر، روز شنبه ۱۱ مهرماه ۱۴۰۵، پس از بارش شدید باران سیل جاری شد و خسارات نسبتا زیادی به شهروندان وارد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72706" target="_blank">📅 09:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72705">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c198c4452e.mp4?token=bdkpJ6G7xkqMCq8-y5dH9W4GhRUg-OMly2tqNCDXIIWHOnYCvEJbeg1mDIts0Mak5MbzF-LvBzjHaNr-sErm3pQIqurHw4-G85xO7aiP-cvEX_hAinT72Fk37xi_E_a1ysNhyW2LwWQtnuEHsZCd04iJWOcdejk5NCVD9VLpIjgNsHSSpGptDHlhv9JiGPRFZ1zcwx-BLoDi6_mAG4dI2BXt9f3Y8S5zKHRTUcIjSX8y_qlNfFGi5eZ94DIYgeMPdYslFS6AwMoTu_fs879PJG_EYTnXQaOWD5SkgfTot5V13Vto6rD9Ojl9TAl6olUVjeYnAd5h9NZvyYy26dUnAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c198c4452e.mp4?token=bdkpJ6G7xkqMCq8-y5dH9W4GhRUg-OMly2tqNCDXIIWHOnYCvEJbeg1mDIts0Mak5MbzF-LvBzjHaNr-sErm3pQIqurHw4-G85xO7aiP-cvEX_hAinT72Fk37xi_E_a1ysNhyW2LwWQtnuEHsZCd04iJWOcdejk5NCVD9VLpIjgNsHSSpGptDHlhv9JiGPRFZ1zcwx-BLoDi6_mAG4dI2BXt9f3Y8S5zKHRTUcIjSX8y_qlNfFGi5eZ94DIYgeMPdYslFS6AwMoTu_fs879PJG_EYTnXQaOWD5SkgfTot5V13Vto6rD9Ojl9TAl6olUVjeYnAd5h9NZvyYy26dUnAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خراتیان، کارشناس صداوسیما: چین ارسال تصاویر ماهواره‌ای به ایران را متوقف کرده است!
مجری صداوسیما: چین به ایران گفته ابتدا مشکل خود را با آمریکایی‌ها حل کنید و بعد به سراغ ما بیایید
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72705" target="_blank">📅 09:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72704">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72704" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72704" target="_blank">📅 01:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72703">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwrudepY-jLEnOXFarY31KKnN2x3CpNb9TF00R0Zq6-_597tIyTJFFabTHp7BWB4GCKoIahjLV7Z4nrPkDev5Y4-TCxwto90tUmp5fCXckL0ZSxghrKJgkUoQ-erdo-lSGT6wVHlwuEA1wvbWSv5xB5Z7oNJ_o5ax4A3Rbd4zJRwZEP_idvdoO05dz9bNhuVONopIqD_I84N5oQcskbTMruBXbMXA0P485np8f3z8JaZz74edKbRBlQhy_qQ5bPBWqGjiGuaG2ShcZ3jc0oSzsODkgaZ1BN7Oc7VCznknspS9-E8LcTtoosawG6QMvNWZU4oJbpxKbSEqekAy1-UQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72703" target="_blank">📅 01:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72702">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2d851559.mp4?token=Qkf2igdCOAn-1QuMLtGFjYO_r8x0LuAW5QgMKgthnE35Dwe11gXL_0WkOkr71IcAyhkGaN4gGN-1tvnV0wShYzGmskbflkzoHACtd2IkTp0wmWfWYuNd7ZtdbWIJVKAE7d5vJnlDRc332V9JQ0Gd9m6SJiXNb_uSlr9zhkqBf1RYiPlvRRJlCYm_QZCFub74yxuX0rN7Zmrs37IcPov6Pwt9y9ogO9BN8tXGH0ZStU45sd60eXoXM2c3D74kKg5a8UZOUk7ChTP9KLt9_C4a1dh5MOSg-G2l6QUyCgtY44vIYafX9iCE9-cpTHf2sV3XPi4MaT7Yr47v17XRNEtwn7AaeIgIEr2hiMC9Q9oXITGs8kwNOIM0xLOSfz4HwydaxLB2KzGMuTTHqPIc5Ov1rWLGPoL0WrMUO0PWHb23pMbDPo_aK_mgibAvmVCGvqUVB6F5nesdDhIuUy-XX8vHO7lZZLWpBEQx6hXwIoui9nbX1Nh-wiWtQcqOxukyH83Xdwpm36jx6cruK-cNxvmI7lMfpTA2ro2elBbYIiLUpFubG96Q6LEBRlxixwagno5P02ASgHwAQThwQqDHCgAdR292NsW1WJCEd5kgZ1IMPxtyE9K9s5HEhQ1XtHm20x3g9WS27baVHhOugqyWy8xWsRNVmvQ8vwbseC1l2euTsZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2d851559.mp4?token=Qkf2igdCOAn-1QuMLtGFjYO_r8x0LuAW5QgMKgthnE35Dwe11gXL_0WkOkr71IcAyhkGaN4gGN-1tvnV0wShYzGmskbflkzoHACtd2IkTp0wmWfWYuNd7ZtdbWIJVKAE7d5vJnlDRc332V9JQ0Gd9m6SJiXNb_uSlr9zhkqBf1RYiPlvRRJlCYm_QZCFub74yxuX0rN7Zmrs37IcPov6Pwt9y9ogO9BN8tXGH0ZStU45sd60eXoXM2c3D74kKg5a8UZOUk7ChTP9KLt9_C4a1dh5MOSg-G2l6QUyCgtY44vIYafX9iCE9-cpTHf2sV3XPi4MaT7Yr47v17XRNEtwn7AaeIgIEr2hiMC9Q9oXITGs8kwNOIM0xLOSfz4HwydaxLB2KzGMuTTHqPIc5Ov1rWLGPoL0WrMUO0PWHb23pMbDPo_aK_mgibAvmVCGvqUVB6F5nesdDhIuUy-XX8vHO7lZZLWpBEQx6hXwIoui9nbX1Nh-wiWtQcqOxukyH83Xdwpm36jx6cruK-cNxvmI7lMfpTA2ro2elBbYIiLUpFubG96Q6LEBRlxixwagno5P02ASgHwAQThwQqDHCgAdR292NsW1WJCEd5kgZ1IMPxtyE9K9s5HEhQ1XtHm20x3g9WS27baVHhOugqyWy8xWsRNVmvQ8vwbseC1l2euTsZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفنگداران دریایی ایالات متحده در حال سوخت‌رسانی به یک فروند هواگرد «ام‌وی-۲۲ آسپری» (MV-22 Osprey) در خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72702" target="_blank">📅 01:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72701">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f216caf4ae.mp4?token=J85SsCmXrhrF0MSuQ3UcwgnIEm-kCmnDsNahqt9ne5qZRqvHEu8ASYwz_dx2egGXCwV0FaV_572EcMteeg_BF0afKqhPgNqrenkVobKFiGcF5C5ONVAmvWalFE7WNEsWjw_t2muqu4mPQAnsL39zTEVbp0mOti9dOOnMoQcFvbPQeRJhbJpOlzsMbySniHpeYj8XerHIixP0wqwWm_547db-JPOEF1y20qvVa3t7ivjoh5-sUGzqEv5LPP7vhoJIaB6jmbOBjahBfU4M3Id5_-pOCiVHe4uND79Xs2lk97w7_PB7iIh07jYyvvlr5NDFPgVM224rt7dOtN46ZG6DNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f216caf4ae.mp4?token=J85SsCmXrhrF0MSuQ3UcwgnIEm-kCmnDsNahqt9ne5qZRqvHEu8ASYwz_dx2egGXCwV0FaV_572EcMteeg_BF0afKqhPgNqrenkVobKFiGcF5C5ONVAmvWalFE7WNEsWjw_t2muqu4mPQAnsL39zTEVbp0mOti9dOOnMoQcFvbPQeRJhbJpOlzsMbySniHpeYj8XerHIixP0wqwWm_547db-JPOEF1y20qvVa3t7ivjoh5-sUGzqEv5LPP7vhoJIaB6jmbOBjahBfU4M3Id5_-pOCiVHe4uND79Xs2lk97w7_PB7iIh07jYyvvlr5NDFPgVM224rt7dOtN46ZG6DNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
ایران نمی‌تواند سلاح هسته‌ای داشته باشد. البته، همان‌طور که می‌دانید، ایران عملاً از هرگونه برنامه‌ای برای دستیابی به سلاح هسته‌ای دست کشیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72701" target="_blank">📅 00:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72700">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e33db7c818.mp4?token=qyWlK-FPJUoJK7yDIbzk6tg5crHckUPZZ6GQJPxouSFFqM9eir-Tt4le7n2v_c9LLq7jTHBqmIOH_ZXzfYVRjZsN-oanaporpn0PnCgEbdry5q1MhbgiqHEJ4H3-tz_xfWECx7EbjTimipZN1voMtl29OuGky6x3mAZq-uhGNgR8ZDWZQ3fFbl0ODlgAZ5ph3r_YOCu7B0TYyBHpnGXxI9gAm4mFIS5Wr0BuD-0CWx1rAA857NqjrmuKQtEXRFvbYYSdUuLESXDaD36zMu4fO5UNuIpuzATj6Wpr5XIgWhSl-pI7eeVGEG_t9XTz0rmBDdKSnX-vgTn9CtutAC556Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e33db7c818.mp4?token=qyWlK-FPJUoJK7yDIbzk6tg5crHckUPZZ6GQJPxouSFFqM9eir-Tt4le7n2v_c9LLq7jTHBqmIOH_ZXzfYVRjZsN-oanaporpn0PnCgEbdry5q1MhbgiqHEJ4H3-tz_xfWECx7EbjTimipZN1voMtl29OuGky6x3mAZq-uhGNgR8ZDWZQ3fFbl0ODlgAZ5ph3r_YOCu7B0TYyBHpnGXxI9gAm4mFIS5Wr0BuD-0CWx1rAA857NqjrmuKQtEXRFvbYYSdUuLESXDaD36zMu4fO5UNuIpuzATj6Wpr5XIgWhSl-pI7eeVGEG_t9XTz0rmBDdKSnX-vgTn9CtutAC556Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ترامپ: تصمیمی درباره ایران دارم که باید بگیرم. کار را یا به روشی آسان پیش می‌بریم یا به روشی دشوار.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72700" target="_blank">📅 00:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72699">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b62816af7e.mp4?token=t_GOkRBckZHSaqBLMjV7Ts1MrHPhMe2Cx0HvxJwaRFlbvrrbpNhv2a8uqZusbMEEmh9nfL4KkqmxjY4wMbQg__7Yee9fngPC3oVB_ZvvkWSalH5dNYzCgFXbpmbL8hK3SJWKVjfgSG5bdSkwAQUX0CMhGrHmqgxwR_H3Gkrzim2IyYghPUDRSUvebT1jHOh74MlwvA6fwtxftiB5r1EdDYZ_yXNQFoXr_PZaOJNgrHqojDOFA_pbek3BFLYlgX4M9uZdFa0Sde224BZG9Gw_gAW1MwKRnDmjsJW5vMGs91iEVRuFShEAkZN3jcjfRY2UgBh7Y7Nbf6rOYW5LohnDH02TMTJNPkuER9pgeoEM1Hea6_GCsY2YA5NiBmX7THmlvQtTFzDSTrsUsFhjTYFQ_AHo-XtqwtCpTpujqJaJKOCK3XkXU-q3vYDNuYU73tahjQGQHN2dd-OdDx4SGKbdIGlkLqb-JCcNsWwOn2XPJdqvu-KS32UKHJb6ZkeeWbIC5a3_f9_Arznon8XHdim3EJWIrzV9NtLJMGajGgSRVztlQa_-4Oj6xYw6suZhJzU_RLQLLVz5Z00aa6tE_stkhu5qbZPLDRA1TuhJpSs9aGCsX_rnogKmpsWgllz-x-cDaOLERk1ecQh-vLRsaooz_OTbrypKrmeQFsCbAjeMztM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b62816af7e.mp4?token=t_GOkRBckZHSaqBLMjV7Ts1MrHPhMe2Cx0HvxJwaRFlbvrrbpNhv2a8uqZusbMEEmh9nfL4KkqmxjY4wMbQg__7Yee9fngPC3oVB_ZvvkWSalH5dNYzCgFXbpmbL8hK3SJWKVjfgSG5bdSkwAQUX0CMhGrHmqgxwR_H3Gkrzim2IyYghPUDRSUvebT1jHOh74MlwvA6fwtxftiB5r1EdDYZ_yXNQFoXr_PZaOJNgrHqojDOFA_pbek3BFLYlgX4M9uZdFa0Sde224BZG9Gw_gAW1MwKRnDmjsJW5vMGs91iEVRuFShEAkZN3jcjfRY2UgBh7Y7Nbf6rOYW5LohnDH02TMTJNPkuER9pgeoEM1Hea6_GCsY2YA5NiBmX7THmlvQtTFzDSTrsUsFhjTYFQ_AHo-XtqwtCpTpujqJaJKOCK3XkXU-q3vYDNuYU73tahjQGQHN2dd-OdDx4SGKbdIGlkLqb-JCcNsWwOn2XPJdqvu-KS32UKHJb6ZkeeWbIC5a3_f9_Arznon8XHdim3EJWIrzV9NtLJMGajGgSRVztlQa_-4Oj6xYw6suZhJzU_RLQLLVz5Z00aa6tE_stkhu5qbZPLDRA1TuhJpSs9aGCsX_rnogKmpsWgllz-x-cDaOLERk1ecQh-vLRsaooz_OTbrypKrmeQFsCbAjeMztM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ، درباره ایران:
ما از همان ابتدا اعلام کرده‌ایم: ایران هرگز به بمب هسته‌ای دست نخواهد یافت؛ تمام. این موضوع، یک منافع حیاتی ملی برای ایالات متحده آمریکا محسوب می‌شود.
ما این مسئله را در جریان «عملیات پتک نیمه‌شب» (Midnight Hammer) به وضوح نشان دادیم و در «عملیات خشم عظیم» (Epic Fury) نیز آن را آشکار ساختیم.
ایران می‌خواهد با مسائلی همچون تنگه هرمز بازی درآورد؛ اما کنترل آن در دست آن‌ها نیست، بلکه در اختیار ماست.
آن‌ها عملاً هیچ چیزی به دست نیاورده‌اند؛ چرا که محاصره ما آهنین و نفوذناپذیر بوده است و ما هر شب تقریباً با همان ظرفیت‌های پیش از جنگ عمل می‌کنیم.
ما احساس می‌کنیم که در موضع بسیار قدرتمندی قرار داریم. ایران باید تصمیم درست را اتخاذ کند؛ در غیر این صورت، رئیس‌جمهور ترامپ تمامی گزینه‌های لازم را روی میز خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72699" target="_blank">📅 00:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72698">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6316faf3f3.mp4?token=RDUcMM6uXPk2SMzh9AQsmPISvDZQ4UyASRpqviKfT-xWFQyUWbnNpkDSxE6CD4UmT7jJikj3NfpYwGhQNGaDW-uAYkbyImOWjUQvlqNfMYu5VbTU5WMKTb5zngbETMw35WCFLnVb6kplTHIZRrWQCcJaYEBen9mBJ9VkPnyyUw0b1VqH_QWy_lRD43Eq2A2m9aGcR5wcu1K9aWUbA40isR348Wy8XuG8SV08vvb6UC3nTKvpXPMy_OWg1eK6jpfjsTCp2UK4uBoebG1ZitnhvHFGZCc4VlmxBB0azQ5pjGXi5W_obp_Ay8G2LzQn8rnBjbXe9NLzUf2BnCjWBJERpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6316faf3f3.mp4?token=RDUcMM6uXPk2SMzh9AQsmPISvDZQ4UyASRpqviKfT-xWFQyUWbnNpkDSxE6CD4UmT7jJikj3NfpYwGhQNGaDW-uAYkbyImOWjUQvlqNfMYu5VbTU5WMKTb5zngbETMw35WCFLnVb6kplTHIZRrWQCcJaYEBen9mBJ9VkPnyyUw0b1VqH_QWy_lRD43Eq2A2m9aGcR5wcu1K9aWUbA40isR348Wy8XuG8SV08vvb6UC3nTKvpXPMy_OWg1eK6jpfjsTCp2UK4uBoebG1ZitnhvHFGZCc4VlmxBB0azQ5pjGXi5W_obp_Ay8G2LzQn8rnBjbXe9NLzUf2BnCjWBJERpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدت زمان حضور رهبری تو جنگ:
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72698" target="_blank">📅 23:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72697">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e8309253.mp4?token=TjqmB8f5FNwrLOz5znzTGHOzcwa-Ien7HSqtQlxwyJLcACoPupc5RUG9IUC4vGI7Z-e1ilcRfCoVg2k-BLkq0jQJ-8ZbYv-RGC7pGgQ-y2E6Fe2BJRqsktwWXy3DDQh6c-3uj3ndYHR1cGzfR_keqpPcp3xWrQRedACMjVi8GRFa65VzBoE_CpwG3x9Zu6Eoh5RyBGvx281ibx3t3waj02Qe9SJqV1DnibfSZ-v_qEvqiBB_WeYOnC8MDh0WH7BjwHeanjBobQXCOOyri0aeg6QEdP0OI_xEFBT_ePNH7QhWiJosoFPGRKfwsGgUgdcW5Q7-VODOsC4xSLnSFYq6Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e8309253.mp4?token=TjqmB8f5FNwrLOz5znzTGHOzcwa-Ien7HSqtQlxwyJLcACoPupc5RUG9IUC4vGI7Z-e1ilcRfCoVg2k-BLkq0jQJ-8ZbYv-RGC7pGgQ-y2E6Fe2BJRqsktwWXy3DDQh6c-3uj3ndYHR1cGzfR_keqpPcp3xWrQRedACMjVi8GRFa65VzBoE_CpwG3x9Zu6Eoh5RyBGvx281ibx3t3waj02Qe9SJqV1DnibfSZ-v_qEvqiBB_WeYOnC8MDh0WH7BjwHeanjBobQXCOOyri0aeg6QEdP0OI_xEFBT_ePNH7QhWiJosoFPGRKfwsGgUgdcW5Q7-VODOsC4xSLnSFYq6Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#مهم
؛
سؤال: آیا ناو «یو‌اس‌اس روزولت» قرار است جایگزین یکی از دو ناوی شود که هم‌اکنون در آنجا حضور دارند، یا اینکه قرار است سه ناو در منطقه مستقر باشند؟
هگ‌ست: سؤال بجایی است، اما من هرگز به آن پاسخ نخواهم داد.
ترامپ گزینه‌هایی در اختیار خواهد داشت؛ بگذارید این‌طور بگویم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72697" target="_blank">📅 23:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72696">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e6961bcdd.mp4?token=NbBWH29tSO1G3xJgMq3CLth8BjF8idZnJ9lYxFBVJAUaiaIYK40mTXiHkbKSw7MLvGIMmmtGZhm_rswYQAEHwv1_15DbrrvUETr7bCM_yLCK432zoqV4ZCt7VmU69djD72jC9wK1PhhmDMgcIgioEmpoXlncdghrzFsd9Q0E6cja1lJGqUOqs11VajhYRqR-INASnlw90jpietw1mAe8GFsK0FBgYAk7eVJR9LaFr1WT0Pk6VoIwBnM5tKlCx68wXkHSjTanwmJzPDf6TKbyqO67wWryegxHke1lWSG0LdUt3ocrgDBHqFvTLoXT9YqLmVtJacWXgPjtyGu7IaThjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e6961bcdd.mp4?token=NbBWH29tSO1G3xJgMq3CLth8BjF8idZnJ9lYxFBVJAUaiaIYK40mTXiHkbKSw7MLvGIMmmtGZhm_rswYQAEHwv1_15DbrrvUETr7bCM_yLCK432zoqV4ZCt7VmU69djD72jC9wK1PhhmDMgcIgioEmpoXlncdghrzFsd9Q0E6cja1lJGqUOqs11VajhYRqR-INASnlw90jpietw1mAe8GFsK0FBgYAk7eVJR9LaFr1WT0Pk6VoIwBnM5tKlCx68wXkHSjTanwmJzPDf6TKbyqO67wWryegxHke1lWSG0LdUt3ocrgDBHqFvTLoXT9YqLmVtJacWXgPjtyGu7IaThjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز قبل تیک تاکرها باهم دعواشون میشه؛
چندتا دختر ریختن روی سر یه تیک تاکر به اسم ستایش و اینجوری همو کتک زدن:
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72696" target="_blank">📅 22:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72695">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4df7e241a.mp4?token=QBB3MukwJ7xhA2JYQOCD2QvjAi3mrNdry0ipUhKPA7nsqaUhTxV1sqHzo7hE-6NOo8eEdyKjgd4vFhGyxcSnF9dtwrc-EDTgBppLk-x6sVlphRo1fwq8ZstjHcrU2f-DshFWKjvLRoiKaY2i0dShkGrrNnplvN8lQat_2LjoLAxKY7buMMdyoyorh2dFkGvmLTdI2xoDGmafnfxCrLhBqhgbWTDt8Aqqm0cLslmj-jWrDdhwMoFcgxkvHcz6apDSldrIFeif0lz9WcZHeEkvtcN8MyLQ2oqsQRelT68fSWF_yZPXHGRezxEkVBHndASJ0ARuhtU2EynMp-DcPfqc_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4df7e241a.mp4?token=QBB3MukwJ7xhA2JYQOCD2QvjAi3mrNdry0ipUhKPA7nsqaUhTxV1sqHzo7hE-6NOo8eEdyKjgd4vFhGyxcSnF9dtwrc-EDTgBppLk-x6sVlphRo1fwq8ZstjHcrU2f-DshFWKjvLRoiKaY2i0dShkGrrNnplvN8lQat_2LjoLAxKY7buMMdyoyorh2dFkGvmLTdI2xoDGmafnfxCrLhBqhgbWTDt8Aqqm0cLslmj-jWrDdhwMoFcgxkvHcz6apDSldrIFeif0lz9WcZHeEkvtcN8MyLQ2oqsQRelT68fSWF_yZPXHGRezxEkVBHndASJ0ARuhtU2EynMp-DcPfqc_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه اخوند تو تجمعات شبانه: در پیروزی ما توی جنگ و ابرقدرتی ایران تو کل عالم شکی نیست؛ الان دعوا فقط سر میزان ابرقدرتی ماست!
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/72695" target="_blank">📅 21:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72694">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7af7d5f80.mp4?token=aHl6S4pNbDLc32Y5--gR6LmgZFJvpNR38KoxqvZ16zAkYIfNOEZ8PM7bGb7ctKIfzn0e863JVVm1kXfpSULcao1lzFDV6olwg6MEsPTBBVePMedC7CDf4RmOSlGdJbweNidZ67KySWp9fxGmBjsDb9sPNUwe_2QoV39SkGJ8E3118laV2mBp8LX9OycgOVfgSvDJ23BHUTtciAb9V1D986EpEvnMs20p3GrLXOhxwVzQ1j6ReT6iwZd1biqpGfEc4tqepf9l_6qNvOM2RimqieKx0bFnFb_o0qiO768lD4Arisx1fqNCeEfj_KG-n0tfJ2ciiqP2Bq9uI0lateWh9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7af7d5f80.mp4?token=aHl6S4pNbDLc32Y5--gR6LmgZFJvpNR38KoxqvZ16zAkYIfNOEZ8PM7bGb7ctKIfzn0e863JVVm1kXfpSULcao1lzFDV6olwg6MEsPTBBVePMedC7CDf4RmOSlGdJbweNidZ67KySWp9fxGmBjsDb9sPNUwe_2QoV39SkGJ8E3118laV2mBp8LX9OycgOVfgSvDJ23BHUTtciAb9V1D986EpEvnMs20p3GrLXOhxwVzQ1j6ReT6iwZd1biqpGfEc4tqepf9l_6qNvOM2RimqieKx0bFnFb_o0qiO768lD4Arisx1fqNCeEfj_KG-n0tfJ2ciiqP2Bq9uI0lateWh9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو بمب‌افکن راهبردی رادارگریز B-2 Spirit نیروی هوایی ایالات متحده بر فراز محل برگزاری مسابقه تیم‌های نیروی دریایی و نیروی هوایی در «کلرادو اسپرینگز» پرواز کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/72694" target="_blank">📅 21:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72693">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/24bef6628d.mp4?token=LS3IPS7-jmJx4HMAy2UJfMXKntDZFlRC97pqLtL1LeNXWRGmeAcl-0jK49olLnNEfkDgsj8vwrsECLplCoawFN1B0HgeYjEinA_kFf_3ZEob86m0AlmqpO7k-XLheZj-uVPFfwSbCw9VVwIse1Jr8Xy4_2ohicnXYw_pawO-nG6Uw64E10ng1ZhGaQVRAKhX7EIUR_7rcjmtnTcViHwXceDjI55VGMRLgmDvLe53jKFvMsZoOgzI0t6WJV_wt5ZR6i-YxUH-KU_jBa_0tRO9Axp2-0yKNvmp7BWXn2I5bXsVVKC7oC1q61-pRPfv1pdP4aurq4aqFed8xk2BThHZhg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/24bef6628d.mp4?token=LS3IPS7-jmJx4HMAy2UJfMXKntDZFlRC97pqLtL1LeNXWRGmeAcl-0jK49olLnNEfkDgsj8vwrsECLplCoawFN1B0HgeYjEinA_kFf_3ZEob86m0AlmqpO7k-XLheZj-uVPFfwSbCw9VVwIse1Jr8Xy4_2ohicnXYw_pawO-nG6Uw64E10ng1ZhGaQVRAKhX7EIUR_7rcjmtnTcViHwXceDjI55VGMRLgmDvLe53jKFvMsZoOgzI0t6WJV_wt5ZR6i-YxUH-KU_jBa_0tRO9Axp2-0yKNvmp7BWXn2I5bXsVVKC7oC1q61-pRPfv1pdP4aurq4aqFed8xk2BThHZhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از سیلاب شدید امروز عظیمیه کرج:
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/72693" target="_blank">📅 21:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72692">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">به گزارش نیویورک‌تایمز، مقامات بریتانیایی و آمریکایی معتقدند افرادی که در نزدیکی پایگاه نیروی هوایی سلطنتی «فیرفورد» (RAF Fairford) دستگیر شده‌اند، با عملیاتی تحت حمایت ایران — که یا به سپاه پاسداران و یا به یک مرکز فرماندهی نظامی دیگر در تهران مرتبط بوده…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72692" target="_blank">📅 20:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72691">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEh0hv17foYHdFOb3_agKl7iM3dW5Ge6FbSRnLvzckOyW4UpWLy7Gow9NUZg4yC_EAC3CXl5sgf3KVJD704VY0TfMuzov54_PHJJzzY2rpLnzXyfoXn-Z0-d0wCwB7K8gz3YWewuOORNh4b7KUFpWuBq-tQrNCW6AEGdQRPFfYQ_UtVlOIozfDAFgmgtt-jMmEI5DEKGQBtVdLOfzm3wgjEBHUhfReaD_TwkbxhQ-vttHlz_1yFZvShzbYsUre1CynOGCKv5Z2MnoANAnOiVmx_PqvPCF-NTS88FBzQPpBBKQjd6-CICVjuA7zLSo7HTby05kv-i87qhncpr9w8mgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش نیویورک‌تایمز، مقامات بریتانیایی و آمریکایی معتقدند افرادی که در نزدیکی پایگاه نیروی هوایی سلطنتی «فیرفورد» (RAF Fairford) دستگیر شده‌اند، با عملیاتی تحت حمایت ایران — که یا به سپاه پاسداران و یا به یک مرکز فرماندهی نظامی دیگر در تهران مرتبط بوده — در ارتباط بوده‌اند.
بازرسان در تلاش‌اند تا هویت فردی را که این افراد را به خدمت گرفته، شناسایی کنند؛ کسانی که یکی از مقامات آن‌ها را «افراد ساده‌لوح و بی‌خبر» توصیف کرده است.
با این حال، مقامات اذعان کرده‌اند که جزئیات مهمی از این توطئه ادعایی همچنان نامشخص است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72691" target="_blank">📅 20:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72690">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دونالد ترامپ به تمام شهروندان بزرگسال ایالات متحده وعده داد در صورتی که جمهوری‌خواهان در انتخابات مجلس‌نمایندگان و سنا پیروز شوند به آنها ۵۰۰۰دلار خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72690" target="_blank">📅 19:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72689">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a49047dbc.mp4?token=ahkT-ManuCFq5QfcC3BSLABI4JpOPWTpkfhFrp9s1z5NoxApNOmdE432D1DIBFremtuRB4x6k0TcQO0mOWteXy17-UQ2JcDuQxjIdzbLt0Ij3A8nLAi0f_zwmXmo85nYAZBUE04mnvuKnQmq6IDDmHceMZYLSmNDrNPiwZCFs5XGw_dvabYpEqs01WvRaOt8FDeoap5ou7rRvMoGUsVjMigqFG-2EucDv0T1ueTC8VZNw8ZeJs5ru3hXcxChpVu4vOpPnuFEU5R8ss36Z7iIQUtt7_6WOFtu0HVF-BJd5YO3gxgmcQ8RwEAeKjmRtBLgiCkERifyXnyCbZjX2TUPvXmzZ1txYr4-2S-PSk7iO85yFBiUluwvQJmT_c5tXm3i4P7oE4dpn3yahCiimm1TRxJ_ftrWWTfkQTEKwWcCZ1POd94cqKPS246IE11EOk2ZwcFYIAQdxz3iAJ4Gc-_L1-RTFEYJdtXVjOlj7vO56B8fdAuPphC4Bxri29bNtt5D4nIaOAu0lELB9FlNiuw9RUvo-E76cuvsf97GRqrTY4pNl3GhNRZ6z1dXpCNvYNiLsupI-8MMw42I83PgX4dWQQuK9t8BVTZRULPoYG7jXOVzfA0WMJnkmswFZmeLPQ6qbZShD54V6i5wcryVgC7_L7PY0MBsSFvGAlmM95hiMK8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a49047dbc.mp4?token=ahkT-ManuCFq5QfcC3BSLABI4JpOPWTpkfhFrp9s1z5NoxApNOmdE432D1DIBFremtuRB4x6k0TcQO0mOWteXy17-UQ2JcDuQxjIdzbLt0Ij3A8nLAi0f_zwmXmo85nYAZBUE04mnvuKnQmq6IDDmHceMZYLSmNDrNPiwZCFs5XGw_dvabYpEqs01WvRaOt8FDeoap5ou7rRvMoGUsVjMigqFG-2EucDv0T1ueTC8VZNw8ZeJs5ru3hXcxChpVu4vOpPnuFEU5R8ss36Z7iIQUtt7_6WOFtu0HVF-BJd5YO3gxgmcQ8RwEAeKjmRtBLgiCkERifyXnyCbZjX2TUPvXmzZ1txYr4-2S-PSk7iO85yFBiUluwvQJmT_c5tXm3i4P7oE4dpn3yahCiimm1TRxJ_ftrWWTfkQTEKwWcCZ1POd94cqKPS246IE11EOk2ZwcFYIAQdxz3iAJ4Gc-_L1-RTFEYJdtXVjOlj7vO56B8fdAuPphC4Bxri29bNtt5D4nIaOAu0lELB9FlNiuw9RUvo-E76cuvsf97GRqrTY4pNl3GhNRZ6z1dXpCNvYNiLsupI-8MMw42I83PgX4dWQQuK9t8BVTZRULPoYG7jXOVzfA0WMJnkmswFZmeLPQ6qbZShD54V6i5wcryVgC7_L7PY0MBsSFvGAlmM95hiMK8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ:
مرا بفرستید تا با «کت‌قرمزها» (نیروهای بریتانیا) بجنگم.
مرا بفرستید تا با کمونیست‌ها بجنگم.
مرا بفرستید تا با نازی‌ها بجنگم.
مرا بفرستید تا با اسلام‌گرایان بجنگم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72689" target="_blank">📅 19:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72688">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc7b08156.mp4?token=Mb24zS9s4HBBQyRZ-_6cPsPEdq_0zbj4xXwG3VXAW1GsdRIMJ5a3hXiGe8Y2mCNbgch_uz4_mQDcCySlHZ2iFLVbtuafaC8ktLik97fzh3QzAMwKCaaf3qOgbo2JmxNi88Xnj3aq9F6Z5m8AZRK2bSZ9iO0RT-C1VLMALhc9vr5yw3GYz_cqoagPDLVig0t1zIkUQuKQ03fpW0BWl-uTM-BmzD6912IAXhgE6Gyk6PXQFN0Qj7Y9IAg8lGj8yrYJZstJoUH_kDJGSDrdo1jGwOTLZ_I9352GI4oUy_O3d--KNm39ZCXciDWdPjrJxz7te2SxbrZC3va6dHGcvDuecA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc7b08156.mp4?token=Mb24zS9s4HBBQyRZ-_6cPsPEdq_0zbj4xXwG3VXAW1GsdRIMJ5a3hXiGe8Y2mCNbgch_uz4_mQDcCySlHZ2iFLVbtuafaC8ktLik97fzh3QzAMwKCaaf3qOgbo2JmxNi88Xnj3aq9F6Z5m8AZRK2bSZ9iO0RT-C1VLMALhc9vr5yw3GYz_cqoagPDLVig0t1zIkUQuKQ03fpW0BWl-uTM-BmzD6912IAXhgE6Gyk6PXQFN0Qj7Y9IAg8lGj8yrYJZstJoUH_kDJGSDrdo1jGwOTLZ_I9352GI4oUy_O3d--KNm39ZCXciDWdPjrJxz7te2SxbrZC3va6dHGcvDuecA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ:
اطلاعات نادرست، اطلاعات گمراه‌کننده و تبلیغات عامدانه‌ی بسیاری پیرامون ناو «یو‌اس‌اس آبراهام لینکلن» وجود داشت، اما ۸۰ درصد از کارکنان آن گروه ضربتِ ناو هواپیمابر، برای تمدید خدمت خود اعلام آمادگی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72688" target="_blank">📅 19:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72687">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee4b7ed20.mp4?token=MMGeEODfmoW2xl0Njiqc_45In5Kt-5TwpuxbS6MWnsZkQoat0Q4s0QHAqzHMegibc4T3PBR7YplKAbGJ2KOpI1yRqMTvctpMgr_Dud3-SXHnlXy9qGewharIv08iInZgZJIvWLEPc-O5Wy6fnDBR829JP9pEmQSD6kXaK2vSfoeWAsj_Qp-WZ5oy6a0gUpSCUsO05KD7N1fo2ekb04HiLJ2besXhdAgCKDuze0NpGRlHArkgF8qHZHbKeUc1g8CziexBFwL7I7SJmbam5Bx_pjd0MwKdxc6xfYv0h3yrH_h-XA21UfmdlS307vSqQSqVs2OhT7mplQkyI_V303MWLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee4b7ed20.mp4?token=MMGeEODfmoW2xl0Njiqc_45In5Kt-5TwpuxbS6MWnsZkQoat0Q4s0QHAqzHMegibc4T3PBR7YplKAbGJ2KOpI1yRqMTvctpMgr_Dud3-SXHnlXy9qGewharIv08iInZgZJIvWLEPc-O5Wy6fnDBR829JP9pEmQSD6kXaK2vSfoeWAsj_Qp-WZ5oy6a0gUpSCUsO05KD7N1fo2ekb04HiLJ2besXhdAgCKDuze0NpGRlHArkgF8qHZHbKeUc1g8CziexBFwL7I7SJmbam5Bx_pjd0MwKdxc6xfYv0h3yrH_h-XA21UfmdlS307vSqQSqVs2OhT7mplQkyI_V303MWLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست لحن و رفتار ترامپ رو تقلید کرد و چیزی رو که ترامپ هنگام پیشنهاد این سمت به او گفته بود بازگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72687" target="_blank">📅 18:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72685">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd7350ab9.mp4?token=TOUjL1_XcolVHH1KS81NpM2tLniGuOLo4UTDVhEBuYVr7CxFr6n7r2-wpRxwWqKIC7RUXbcSnUueyzfBvZIiHAQotvVkw371IK6Kg8yQ2ezNbE7zVquNR6eGNF3a-BqvZsU1bqxJCszQBvChvP_YT01u-kLmYXRyHYjDlsD-UeHDxRqV9ZNh0OpFSPF5D-UMOPnV4YT-SBMNdr0nMBfhaCIjTqEaFzjwC7gQXnjxChzz0LzsBnJLTM8v8_H3XmjPP5jvahs0HTWuTF4chFVUmkDF0iIlfcGSnf9_qZIO7K5S6e2cGLmIrOzq9yi04u-dMHt5SN2ql_aukm1SDfC_cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd7350ab9.mp4?token=TOUjL1_XcolVHH1KS81NpM2tLniGuOLo4UTDVhEBuYVr7CxFr6n7r2-wpRxwWqKIC7RUXbcSnUueyzfBvZIiHAQotvVkw371IK6Kg8yQ2ezNbE7zVquNR6eGNF3a-BqvZsU1bqxJCszQBvChvP_YT01u-kLmYXRyHYjDlsD-UeHDxRqV9ZNh0OpFSPF5D-UMOPnV4YT-SBMNdr0nMBfhaCIjTqEaFzjwC7gQXnjxChzz0LzsBnJLTM8v8_H3XmjPP5jvahs0HTWuTF4chFVUmkDF0iIlfcGSnf9_qZIO7K5S6e2cGLmIrOzq9yi04u-dMHt5SN2ql_aukm1SDfC_cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آب‌و‌هوای قم رو ببینید
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72685" target="_blank">📅 18:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72682">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UOyv_4JOlm5jNv11r4v79mBRTuTzLQPRw5b5pdC5n61K1EqIUIaYRyHDL9MpEHyqtMKICNQ6IKLGZ5QBwuA8qpogbv3C0wHJbYVB_iCRp6oOt3SuRnXR1IAq--S7MnT1ZrbwZTTKnyP5MoI5wT2iHgvo3C4GtUNvf0Kpuvq8FeIlE0HIht8o6L67va0ZfsidAmRt5-c5Q72rcBXbKKkx46Sr22ZBpb-GzqQYn7ocOF41A5mjAnR0pb2Pc9FusFUoGZG2q0zCLHafXuuXHdXUiCCC_EIUXkb5ELoQeArgDAv8bOu6gr8G5_gkikV1kR7EGwc6j3e0y14kfqFhTjmXig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZmiEWce444BZ_RUKXo2aBcu9Uszg0J-rIv2MmHA1F4iQtVIlAhmiqKCNLwku8rzQOk1LKt1ZdYTwtr6dS-LonU5vRnV1XEqRAKzM2RlRCIuXfDlazqmWRHGBS16mzpMlo3UAUjk1FR39KI1lLtESZL9DPDTmtl0H-XR6l6W6zV7_wG6D0X__QCWNRZVxDfwNeL6w_VO1Xwwj02M8VNAoxhMVYGMTpoKHkK0dvohvMN-QO5U9k0sIwGn3sN5PPN_k-O5fe2otmAj4aOFLR06vVF5_Oa7mqZTN8Vuxftr7hYEKVBiCnt7GI4MQW0_NQu_ghLN58yoIKfXrE5Gsot_LJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XgICukZNQLcYmCQgSRmS5WsKJB-kkCIXizoZMhK754B953n7CxRzyvL9dQVe5vQELCjYQ9RyOzfXQguQyZljZ0Bk1BtGorEN4uGCkFwH2UORaKL6-cS68Js2mnIm1YiTm1TAwfC293d6sqOBA7eYxZrStzQwqVcmrPX0DjyjJuF4B0H-7n8OdQtYwUUoFOeq9JX0SpdCh9n9SRH3_97fbH3N0hXBchBxEvFGwa7k0ZR98C9xUHiuSdxmVY7XVXkEmf8ySOjq2sfZLliM5VMrwaC3m-E__MdD5n4rqDhHVybI5cpiA1j2jNCYXIfppJBOIAGouBMcJ3A1TfCmeXn81w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایلیا هاشمی:
ساعت ۱۶:۳۵ شنبه؛ ابتدا صدای جنگنده در قشم شنیده شد و سپس یک جسم مشابه با بدنه موشک، داخل شهرک بوستان قشم
سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72682" target="_blank">📅 17:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72681">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72681" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72681" target="_blank">📅 17:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72680">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qs8rHd5pgqa8ckT03XdrzMRqZnkfQuzMzhYSLZsNb8HkpoyTBugCzNoWzmUg_smT57q6gtX0iz6YHyVJ0AdtetdFWu3sNbw_KkBsf5oL-T-wTEou6pfdmUjS1WHBfhznI4o8uKElCLMH5I9_gQzqYltKgQwOZBJ1GffKUlXH-5xNrZ85MYPXZWd8HS9TY1b86GPDGBnGBs70yRWnKPAoCOQ4j9lk3SDMmkQpSMhJmFDH1Ofy7-WOZXVS22yh-XX1YyWQm93kDPGX61hN2yzGUh7DpnPRE5jKbcsxB18ZmylHQuZU-qkhMJlUCiQFYCihPwb8Bw7sHvgOAkPNm20CyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز انگلیس
🆚
کرواسی را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
انگلیس: ۳ برد، ۲ شکست و ۱۳ گل زده
کرواسی: ۳ برد، ۲ شکست و ۷ کل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72680" target="_blank">📅 17:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72679">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4323337b42.mp4?token=hyWynBrXxz0xZXtcnnNam6ngZKXtikmnveC3U453A8IsOECu04QOVus7GVX6JubxbJf-qsg5_FcA8a4Q_lmYv0RGyNV-H6955pVYJxK8RR7f3W2AEn5UQojpqC6Hn5jdW5IAdgBwKC9JUHvcBdKLDYLl7lec8tq-z5fYTvXho_tGnY8redlp_ve9r-xMSiwCmo9vdyJM9TjruB08-WVN_GzlCvxldmP0DxHffAK2N44lRyr4BIkLO0phBbHU1Yxz7knUlga_twPIXChboXMU24SZu0C-ONY5RKsTQeELu0yqAiF8B1uPYQkmHoahU64Wa9QMu4XYXDidcSJCEuBemA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4323337b42.mp4?token=hyWynBrXxz0xZXtcnnNam6ngZKXtikmnveC3U453A8IsOECu04QOVus7GVX6JubxbJf-qsg5_FcA8a4Q_lmYv0RGyNV-H6955pVYJxK8RR7f3W2AEn5UQojpqC6Hn5jdW5IAdgBwKC9JUHvcBdKLDYLl7lec8tq-z5fYTvXho_tGnY8redlp_ve9r-xMSiwCmo9vdyJM9TjruB08-WVN_GzlCvxldmP0DxHffAK2N44lRyr4BIkLO0phBbHU1Yxz7knUlga_twPIXChboXMU24SZu0C-ONY5RKsTQeELu0yqAiF8B1uPYQkmHoahU64Wa9QMu4XYXDidcSJCEuBemA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن مرجانی، رئیس انجمن صنفی تولیدکنندگان شیرآلات ایران:
اگر این وضعیت اقتصادی دو ماه دیگ ادامه پیدا کنه
کل کارخانه‌های شیرآلات کاملا تعطیل میشن
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72679" target="_blank">📅 17:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72678">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ناو هواپیمابر USS George Washington  در حال انجام عملیات پرواز در آب‌های منطقه در خاورمیانه است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72678" target="_blank">📅 17:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72677">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c0fbd5c19.mp4?token=KYRZYMhIPyqVwvpo6ZNf0l1qhRL4pn4Qj2Lep69DP3V2YPndvOwlmFPK4zJ0YHJh4Asvsi3qz_IKJUFacoClyf_lwkY7WaLr3cZGX0sAQ1A_UWPIq42czav65VxSGa_7FRQkDfVJSrm9cbwGPzMAtkLEV4gYDr6YrtOjWkPwU8fu1k0e3ok5sg86VmQKNm8yMahWJvOP7pIhvQ99NebbSjuHF0RWeKvjAhgTwKP71Q_TTGUnpeX9TLX9vyFSvmp68z3aihkm_fCbv3PCgli4f4_OPdw_DtfLl7uvv9vcKJpCrGJ8M5RripjId7_ryC3XGvCnP7m-hCe88H1i-jWU5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c0fbd5c19.mp4?token=KYRZYMhIPyqVwvpo6ZNf0l1qhRL4pn4Qj2Lep69DP3V2YPndvOwlmFPK4zJ0YHJh4Asvsi3qz_IKJUFacoClyf_lwkY7WaLr3cZGX0sAQ1A_UWPIq42czav65VxSGa_7FRQkDfVJSrm9cbwGPzMAtkLEV4gYDr6YrtOjWkPwU8fu1k0e3ok5sg86VmQKNm8yMahWJvOP7pIhvQ99NebbSjuHF0RWeKvjAhgTwKP71Q_TTGUnpeX9TLX9vyFSvmp68z3aihkm_fCbv3PCgli4f4_OPdw_DtfLl7uvv9vcKJpCrGJ8M5RripjId7_ryC3XGvCnP7m-hCe88H1i-jWU5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا:
برای نخستین بار در تاریخ — از زمان آغاز استخراج و صدور نفت(ایران) — آن‌ها در هفته جاری هیچ نفتی روی آب (در حال حمل‌ونقل دریایی) نخواهند داشت.
آن‌ها هیچ درآمدی نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72677" target="_blank">📅 16:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72676">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">صدای انفجاری از سمت دریا در قشم شنیده شد.  @News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72676" target="_blank">📅 16:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72674">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4zLfD3Aaroflc8IMVCgpeFjD-4wzosqI3YC2q-scstCIlRTyyvG__PXYPYoKNbX1Dxx1DT8itYBsfMEEhDaBYUKA9WYU-P6w0CZfVZp-gWGuDvIn4Pvr0_PbmCcDgbsquMUnJFPpjztMFPRC3XGFONVA8SjcWe9bzddvxxSVHSvHYRBvPKLxG6M4_hTRwk81F_28UtFjq-yaNDqHDO5fecrsRp5TfYYZbD82UbhbTrL_GUQ1MgwZaWHE1dLtaFK3dldRnUXrN5wuSF6uizji6QMLws-Jxsp_mPFpGXlnsnRKJMJAw_ke688HsDK8YDW_eRyWTgj3nVrO5yooVIiRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOLf3j3HdEmeTjZ8FJmZWD8O3effD_QJNmMeBPLjCJKTSJ2pDjTQEgZEf6xvRkAUOUJ4VlrARYLv1X6I_ni8wXER9NvBPHU3SNgkbE-J1XUFr-34GpiDwwTrWWDV_FYQcTbgOX1Oz0bcd5f44El1R8eMO8fHukaOtECL1R4PpsvSfsLEVI5ei3EkCqni6jtG-ofzUcS6y-bUm7x_B3HGBnIqJZ1y1Ipiwvt2eeXgbe6DeneerS2mV3BbDm0z4-6J7U8ydYvaciIEGq1QySx3eYDKy-Ehch2sz_Flo6933PstyMoPuh6ViYxmORWkVEIyleO2UXDleuE31kTD4uLiQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمونه کار:)
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72674" target="_blank">📅 16:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72673">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIFqqPm0ZYhyemsoLSp0HPcs9kalLL_S1dYNJxUoa7j1JBTO7l9RlAWvrl1_5TPSbkh9Xv2O8SFHI9yhpySeA2X8hg6N1YnqVhQZqRb64Oq0oxtlORA1IhPN6q1L782OjU719L7UYDZ7DtCvvNWWAkKrwodf0xyyHdW1CFZxGTZ4cmtJI2jEh8NBcn61zV5_1mzvSfG_YANwBGrGYJTmEBAb6JeEKa43cmj10MEtSbfNcL3aj8gMYvLsa0g8_FJZWK24zL7DreGCbHZOC4_2mwzzCd0iHA6Wpag8TDL_q99w0kcqIwMFXM0Qu_y-tGPoAUd31mSpFXuLXUY4FN0Mqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به دانشکده 05 کرمان
✌️
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72673" target="_blank">📅 16:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72672">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">#فوری
؛نتایج اولیه کنکور ۱۴۰۵ اعلام شد!
با ورود به پنل شخصی خود در سایت سنجش میتونید کارنامتون رو مشاهده کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72672" target="_blank">📅 15:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72671">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c967ea5781.mp4?token=ncFpMcQTErmmQ61o4GTZbXDIDMYYgVHk8VAji5cg2ofGQ_VZLWq_IylcT8J-kHgPzeDxSHxHY1kbtVbmUI2weRKO7qY4e9B-K-c_Dm5XZV_BOCW4I-PyO5fSPqIf7uDZS1F283vD4D_nlfD6dVFmxmdBCjo05xFkY0HyJkTFba8zqHWoNquY8nXvGcCBTnqO9NeWLNNpdvzBYejWhbOgq4IASOPrmCkNtS9XBd1UTomtdLEsS2diorKBPLmqlMZ2uRODO9aPODzgx7OOjtuDl8XDyBi5Inx7wxRRNwCACoy7QSxFMPlOb7-pucJ6uB9uqq5gDsU3U6g1wHRkTK0WLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c967ea5781.mp4?token=ncFpMcQTErmmQ61o4GTZbXDIDMYYgVHk8VAji5cg2ofGQ_VZLWq_IylcT8J-kHgPzeDxSHxHY1kbtVbmUI2weRKO7qY4e9B-K-c_Dm5XZV_BOCW4I-PyO5fSPqIf7uDZS1F283vD4D_nlfD6dVFmxmdBCjo05xFkY0HyJkTFba8zqHWoNquY8nXvGcCBTnqO9NeWLNNpdvzBYejWhbOgq4IASOPrmCkNtS9XBd1UTomtdLEsS2diorKBPLmqlMZ2uRODO9aPODzgx7OOjtuDl8XDyBi5Inx7wxRRNwCACoy7QSxFMPlOb7-pucJ6uB9uqq5gDsU3U6g1wHRkTK0WLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسنت، وزیر خزانه‌داری آمریکا:
ما از این مناقشه با ایران عبور خواهیم کرد. به گمانم عرضه نفت بهبود خواهد یافت و قیمت‌ها به‌مراتب پایین‌تر خواهند آمد.
روند افزایش دستمزدها ادامه خواهد داشت، چرا که شاهد رنسانس (احیای) بخش تولید هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72671" target="_blank">📅 15:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72670">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">صدای انفجاری از سمت دریا در قشم شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72670" target="_blank">📅 15:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72669">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fafdeb0b.mp4?token=YeRTvW_oT-6bEmRuuLWx5Y2iA8a8ipvIecVSrb1QOYi6JS8HDYA35ZimjHLVlX2ORjSw4SOGNbLsGX0KRZ5e3h5a8ZCLK8JX-L0IxbpESlTOwW-hBKZi4BfAScWyPIKQEPG8iEjG7mQk6zPlqsfNqIWIxJclDVL6e7HJphrGQ-NN1fsSRPqoaRyEDijQbD7GzXMcvSiOgYVLIRt_WOyRiMfukeG_Ty0o_xXbhJzPDWIN1hZuFQ_64-QouBavwv9EUSD3pQur4Ceb54HWKSzLUSyAtc532T4Xxzu9w05Q9ILM0HHU4AE7IazT_ni-n9a5ijWUs4bz7DHgp7EjZULZhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fafdeb0b.mp4?token=YeRTvW_oT-6bEmRuuLWx5Y2iA8a8ipvIecVSrb1QOYi6JS8HDYA35ZimjHLVlX2ORjSw4SOGNbLsGX0KRZ5e3h5a8ZCLK8JX-L0IxbpESlTOwW-hBKZi4BfAScWyPIKQEPG8iEjG7mQk6zPlqsfNqIWIxJclDVL6e7HJphrGQ-NN1fsSRPqoaRyEDijQbD7GzXMcvSiOgYVLIRt_WOyRiMfukeG_Ty0o_xXbhJzPDWIN1hZuFQ_64-QouBavwv9EUSD3pQur4Ceb54HWKSzLUSyAtc532T4Xxzu9w05Q9ILM0HHU4AE7IazT_ni-n9a5ijWUs4bz7DHgp7EjZULZhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واژگونی ترسناک کمپرسی بر اثر ترمز بریدن در کازرون
💔
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72669" target="_blank">📅 14:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72668">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پشماتون بریزه!
ایران‌اینترنشنال در گزارشی درباره مهدی نادری جهرمی، رئیس هیئت‌مدیره شرکت تهران‌اینترنت و مؤسس و مالک اپلیکیشن هف‌هشتاد، ادعاهایی جنجالی درباره ارتباط او با شبکه‌ای مرتبط با موساد مطرح کرده است.
نادری جهرمی با نمایش چهره‌ای کاملاً همسو با جمهوری اسلامی و حضور در ساختارهای اقتصادی و تجاری، به تدریج به موقعیت‌های حساس دسترسی پیدا کرده است.
ارتباطات و فعالیت‌های او در حوزه‌های بانکی و مخابراتی، در اختیار شبکه‌ای قرار گرفته که با عملیات موساد در ایران مرتبط بوده است؛ از جمله انتقال اطلاعات، شنود و نقش در برخی عملیات اسرائیل در ایران.
این گزارش بر پایه اسناد تجاری و قضایی، مکاتبات بانکی، قراردادهای شرکتی و روایت فردی با نام «کیا» تهیه شده که ایران‌اینترنشنال او را مأمور سابق موساد معرفی می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72668" target="_blank">📅 14:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72665">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkU4lRyRyJBATypkNdpl5EnMM9pVvQWNTkqGPP8YKnp69hNBm1D8yu9wl9sxzuHlme811oNB5zG47929iUficMZWzXK9hJpZvO-kIOpuRiXQ32oqzwTGL3SCiLQ9Qd3Wc7xaf8aFeDsEEFYkMsd0RLvlVNRZUhsZ1GE5_OwtlqVnhsQcInbw6sPIBXMjHpKxMFqP-FDJT_aaBXSnM6t7MyBP2fJJZwYB4wpe_qFdxcau7nn9a21IkvJ_1ENJzVBvsNnYutMcJe3i-E9TQgriYDRwcChKnjlltVo5_2qN3Ak2cLl849JOs8TeET8BlYNjCKVMd8q5N_uVmtkQL9ik6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1908d250d4.mp4?token=doAOPoeJ3nf7SszYlKH1FcyRx_jBoOKNjD0cfUlfl0wuMEhLVHb0-QtghgHN-N33qEervE3RsTLgM0YuF79uBqTTNsCb2mmQCvdJBbNiIpUzWPHH4NPSYW5m6xvpWY6FqI5fADS8A_J8f-xt0ctXdewkcDbjrhAb01DIMrk1BT55vTun_b-CYEoynhjnv6V7YEsfVqWr6IczKrxGPzS0d2ULc1o_Y_PoU_PGRTAeMBbiXgLwskrfdsEXXvE0MOEO5sjTSlMdRanqsfH_TmMJYi_UaD1_yxYkx48y9Vpmmn8NQNNOlPhhn3dWrZQSDnzsZ5vZ_rFM_RwWtBR6wWjleg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1908d250d4.mp4?token=doAOPoeJ3nf7SszYlKH1FcyRx_jBoOKNjD0cfUlfl0wuMEhLVHb0-QtghgHN-N33qEervE3RsTLgM0YuF79uBqTTNsCb2mmQCvdJBbNiIpUzWPHH4NPSYW5m6xvpWY6FqI5fADS8A_J8f-xt0ctXdewkcDbjrhAb01DIMrk1BT55vTun_b-CYEoynhjnv6V7YEsfVqWr6IczKrxGPzS0d2ULc1o_Y_PoU_PGRTAeMBbiXgLwskrfdsEXXvE0MOEO5sjTSlMdRanqsfH_TmMJYi_UaD1_yxYkx48y9Vpmmn8NQNNOlPhhn3dWrZQSDnzsZ5vZ_rFM_RwWtBR6wWjleg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هزاران دانش‌آموز دبیرستانی فرانسوی به دلیل کمبود معلم، ازدحام بیش از حد و ساختمان‌های در حال فروریختن، مدارس سراسر کشور را محاصره کردند.
@News_Hut
| Clash Report</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72665" target="_blank">📅 13:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72661">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b9ce8d805.mp4?token=qmxLTOVLxrXGzRGXUtBcQu7o-Hv3lrwjoCqeSlcNWrgY7B-DxBXPemDGfwy-6iR8BQzAwmbyAqgi9TdWTCuRt4d8i6XqTYcKoh3fGPiMnlp3H-f96hW8xk4akYqGjVJvXJZkgaAQDEWcrE6sP8QbxLQtq-IMMmYIpoZEnfkLmoVtC9jrl7FKuVMdMpWH5pMXd6qbRaz4PxKqiOuMcN9QVvccuuLtNd9Z1lRE9XP6i6I_BQAi8yUR_jm4v4I1r-l5mGxqbQ5f-zoRSUy2hBBVSxQtKLHSih6nIRwWLBZtHIrG0-kVQ-8RW_2d9otmyrWw5W3r3vhDMkX2r-NiTXoDEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b9ce8d805.mp4?token=qmxLTOVLxrXGzRGXUtBcQu7o-Hv3lrwjoCqeSlcNWrgY7B-DxBXPemDGfwy-6iR8BQzAwmbyAqgi9TdWTCuRt4d8i6XqTYcKoh3fGPiMnlp3H-f96hW8xk4akYqGjVJvXJZkgaAQDEWcrE6sP8QbxLQtq-IMMmYIpoZEnfkLmoVtC9jrl7FKuVMdMpWH5pMXd6qbRaz4PxKqiOuMcN9QVvccuuLtNd9Z1lRE9XP6i6I_BQAi8yUR_jm4v4I1r-l5mGxqbQ5f-zoRSUy2hBBVSxQtKLHSih6nIRwWLBZtHIrG0-kVQ-8RW_2d9otmyrWw5W3r3vhDMkX2r-NiTXoDEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از انبارهای نفتی آرامکو در ریاض که هدف حملات موشکی حوثی های یمن قرار گرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72661" target="_blank">📅 12:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72659">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dSNNRqWbbTtLLnGV1jQij_fos8ihYPJjGNCPp2r8KyfnAXYxP3ElE-HdLpiU23VDCt0DRTNPCDd6kLh4q_cd83ZJbGT3JPGpRZjnFP1NhgR0zn94HytxwwnR8aMB8xmDAS4rSFpbC-3pRjDykTCtsxzuwWY49_7LYd6XYH2pSU3Jv7b7tGA7jN_4WIBHlFt6oivXAElkrqXJDbPQWM65cS2JnA3gzSvlp0zhy4ipj7XmFViTsxOw5IdtgE7Vfujtec9Vd00l-BntxxyHy975GgaREd_h2LnsbyCPq0_tM1t5VKq1WvWRIb2Layy0s1_2YBTqomeIN-jPl-EgQcZjmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cc83c2d7b4.mp4?token=RyLLjwHHTsUzn5x-LTYaFb6WOE79bpLJ15WzWxp-4MxrpnBUWHJD9nbzwkFoaKqB6Pob7XKCnjwiofMSUfxi-AG6gm0xwl7rbUKKu23vVgF_p_H1yBFvuJW0Hy2j7490lTcXa2fKQCgZeR6WliA4wn5Oi2GyovdVvW1oo3bvzWV-Cvs9lC5wEVbhpBeDlykWkHV2uWvTPXAyGwANH2h0-5dT1tBqBndwWHyTTqN7JsK-hd5KbyQywD8FmCGqIRNjm7i3u6e4mAUGraP9XuOWZnSpJykZ5R_RDOBQUQu3MWxjR4RyYT3or5MadsSOwnyGN2jsIDdH4_GQ_Nq0zTnWug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cc83c2d7b4.mp4?token=RyLLjwHHTsUzn5x-LTYaFb6WOE79bpLJ15WzWxp-4MxrpnBUWHJD9nbzwkFoaKqB6Pob7XKCnjwiofMSUfxi-AG6gm0xwl7rbUKKu23vVgF_p_H1yBFvuJW0Hy2j7490lTcXa2fKQCgZeR6WliA4wn5Oi2GyovdVvW1oo3bvzWV-Cvs9lC5wEVbhpBeDlykWkHV2uWvTPXAyGwANH2h0-5dT1tBqBndwWHyTTqN7JsK-hd5KbyQywD8FmCGqIRNjm7i3u6e4mAUGraP9XuOWZnSpJykZ5R_RDOBQUQu3MWxjR4RyYT3or5MadsSOwnyGN2jsIDdH4_GQ_Nq0zTnWug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی جنوبی ایالات متحده فیلمی از عملیات شناورهای جنگی آمریکایی Saronic Corsair نیروی دریایی ایالات متحده در پایگاه دریایی گوانتانامو بی، کوبا منتشر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72659" target="_blank">📅 12:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72658">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ:
باید با چه کسی طرف شوم.
کسی نیست که بتونم باهاش درباره ایران تعامل کنم. هیچ‌کس نمیخواد رئیس‌جمهور بشه.
من می‌پرسم: «در ایران با چه کسی صحبت کنم؟» تق‌تق(در میزنم)...اما کسی خونه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72658" target="_blank">📅 11:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72657">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72657" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72657" target="_blank">📅 11:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72656">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pw7nSXgIV9qaGyTxeO_kNfvt7Bpz7vjJAG5ZpbX2WED8rmg9tg2lxn-9KbByV_UkQAsLwYYrmKCkwHH7UIGSF8GgEg7ODoi4gwgw31Ne5-Ir6NW42ZmiHJcCOkW0ZpyTbpRL_ucrZHl45UNCOku4qeQgdN8oiZlYOH3kLprOMj3R_Ru7C1e-6eN0cCCfgJwnRy-dhJVzn7uLnBi6VsyT6_3gxGNzx7AUIQxP8Y-kCMZw3tJmRCPvfqPP33O4mhoHSChUVAClbjFupckbdSRVidY5jWst4zXjXUPoFBffOsHLpI8v4SoKGxAY_mw5yUJELDgaSOdvnkFeUC28x-lViA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
انگلیس
🆚
کرواسی
چک
🆚
اسپانیا
اسلوونی
🆚
سوئیس
لومتزانه
🆚
اینتر
یووه استابیا
🆚
لاتزیو
برزیل
🆚
هند
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72656" target="_blank">📅 11:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72655">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c533100ff9.mp4?token=rJIPQuYZuVBLsLmn1C-3cdD-yJzXOzohUzayt1WPeDAgyIxNV1vb72fq8UHCpqeNRFM2VXplwU3nKUBfrhtc-9tZGwwMsFVgrNWwUV73urgIzV6DdR1GUhNbGyDZ_tn4xSdbV7njQ9pTtL4OggNn-O0hYalACNF4gCDdM2sQAT23vkaJ-xUM9lT199KglzDiUV0xJnbHZRnIyXvspWWvuInF4qZehJM8VPR6TsbIlyY7PgPTfrIfl_6yDozYobsD4Y4jJJ-UNi6HJskvfOOJ3DPIaiTZw9hT_jcS1AO9eNX090l6R9NP4QN9eqadK3Sbv_Mo7j9NOnuqonFIjOSohA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c533100ff9.mp4?token=rJIPQuYZuVBLsLmn1C-3cdD-yJzXOzohUzayt1WPeDAgyIxNV1vb72fq8UHCpqeNRFM2VXplwU3nKUBfrhtc-9tZGwwMsFVgrNWwUV73urgIzV6DdR1GUhNbGyDZ_tn4xSdbV7njQ9pTtL4OggNn-O0hYalACNF4gCDdM2sQAT23vkaJ-xUM9lT199KglzDiUV0xJnbHZRnIyXvspWWvuInF4qZehJM8VPR6TsbIlyY7PgPTfrIfl_6yDozYobsD4Y4jJJ-UNi6HJskvfOOJ3DPIaiTZw9hT_jcS1AO9eNX090l6R9NP4QN9eqadK3Sbv_Mo7j9NOnuqonFIjOSohA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
گروهی از افراد را دیدم با عنوان «هم‌جنس‌گرایان حامی فلسطین». بیایید یک روز آن‌ها را برای مذاکره به آنجا بفرستیم.
دیگر هرگز آن‌ها را نخواهید دید. آنجا کارهایی با آنها می‌کنند که باورتان نمی‌شود
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72655" target="_blank">📅 11:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72654">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اسامی نفرات برتر آزمون سراسری ۱۴۰۵  @News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72654" target="_blank">📅 10:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72653">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I91KhrFy0dSSRtf-y0__sOAxLmTmvqNXFcl-L2HLZS3lspB3o8DWdKbpEG88Y_g6zw1rDkCRsQArl3wx55fW7aGyo9Wi7WsoRQRWyjHUhsT-57T1Bh_ZlG-cycitGL1SQPD829Z5bMhjabXZ7ID3C67WIoy9096vEFp4haPh_OvqRxnZRfLlA9qr1sGXJYBiPb7JfHct7vLZxDHYq-2inO-aItChSoYD7SxNVcjoBvrlv9vyijcWm6naOzL9qaWV3MMxsRn7kaIrcYtf9iYEPbIoVlVDjdKCFagHvuonF00Bfiv03m6jLFc2QRNsg3WaiS6EeuPAjcyKVp_kdLDa-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسامی نفرات برتر آزمون سراسری ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72653" target="_blank">📅 10:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72652">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نتایج کنکور سراسری برای عموم کنکوری ها فردا میاد!!
انتخاب رشته از دوشنبه ۱۳ مهر ماه تا ۱۶ مهر ماه ادامه خواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72652" target="_blank">📅 10:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72651">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMy5SXdSGp1Q1_6YnYRT24PzbGY6p5SZsASbTpcl24XYtcEwiA1JXq7Ea6vJVeH5-7XnChYRwhAyrIz5rfopzxNn14ASkklSwruQdyKqEAPHlsxrlDNC2gOtoon-rvAStXNk3wYJiOvfi8P8C14rSEB4g2AUVtxcIqAD4lZnQKI6A7-jBbDhTRxg1iOdQyXuYGoDF5ZRUHVeznPJerE69TYdlAqaRWMnVqxsmQgLa_HBFnHQtgLHeHb-PWu8xeF3C_hVtAUbHYtisyEird23MhIG7GbscNcuRq0ygieMIWkl2wc13Ui6tVqcBSWXSlQjDfPZUU3qZj95JntSEdKkdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست خبری سنجش تا دقایقی دیگر!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72651" target="_blank">📅 10:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72650">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XZ1fQEhWW_ZZkjCmkHtMQ17tZvqCLZ6dfzimmI7T0l-d1wXxu9Ogyl4hLv2F2atYswsmg1Cukcjo6raIaTcK4b0qAMSTPXnV7My3h9SZyG5_43ccMkKxg8KYn4XyXriArUiZGTzj8kD-u1GJxI9bihBpN7QD3zBiUeqQpyunKjB52sLRj9JAWNkChhg1q38i_cqJdEsU_3uZ75CpjSBP16OJqP3oDOENB1235RSO8_FjEUNgeQnvC-hfhXlVoM0FKdifbtyAPQaB-ZLBpX2qHI8EEH9kIURQ0FPyrmCcDKZG7GyD-l6TXtJF90vqQa0nAd22stCGjkSeATEvgvuuFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛ اکسیوس به نقل از سه مقام آمریکایی:
مقامات ارشد کابینه ایالات متحده در «کمپ دیوید» مریلند گرد هم آمدند تا درباره گام‌های بعدی در قبال ایران و انصارالله گفتگو کنند.
یک مقام آمریکایی اظهار داشت که در این جلسه تصمیماتی اتخاذ شد یا دست‌کم بحث‌های عمیقی پیرامون این موضوعات صورت گرفت.
ریاست این نشست بر عهده «جی. دی. ونس»، معاون رئیس‌جمهور بود.
«مارکو روبیو» (وزیر امور خارجه)، «پیت هگسث» (وزیر جنگ)، ژنرال «دن کین» (رئیس ستاد مشترک ارتش)، «جان رتکلیف» (رئیس سیا) و «استیو ویتکاف» (نماینده ویژه در امور خاورمیانه) نیز در این جلسه حضور داشتند.
آخرین باری که نشستی مشابه برگزار شد، به ژوئن ۲۰۲۵ و پیش از آغاز «جنگ دوازده‌روزه» توسط اسرائیل بازمی‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72650" target="_blank">📅 10:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72649">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f04d52dbe.mp4?token=EHgjd-CZh7fhikV1tTkSiEnxpnqMrFat76shkWQE5e7PtEjr1h7zqJ8opLPpzNCjgl1N3Hj1r0evRQCH5s8UZpN5SIc2zt4keVHf57linDgfoujUVhWdn-YsyJV_ahg9WrD4ffZzW5sdVkyt0PXk0QbWl1CV89-FTmvprS63udFfLRHdQcRwNphbR3eRK_m5L6V4EuGauvWT8AvZ75J7tbUZTvqy8_VRpQ0mtCb4GXwadDzh9cXlaGxbrfC4Kzd-nqbZqvRdJGvEEHNyoD0eW7xwrPo-FCHDp_KYOQ51gFtVqUqHc0Xp39LU9BVcJARoenlCKcMbWtzoyR82DJtrbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f04d52dbe.mp4?token=EHgjd-CZh7fhikV1tTkSiEnxpnqMrFat76shkWQE5e7PtEjr1h7zqJ8opLPpzNCjgl1N3Hj1r0evRQCH5s8UZpN5SIc2zt4keVHf57linDgfoujUVhWdn-YsyJV_ahg9WrD4ffZzW5sdVkyt0PXk0QbWl1CV89-FTmvprS63udFfLRHdQcRwNphbR3eRK_m5L6V4EuGauvWT8AvZ75J7tbUZTvqy8_VRpQ0mtCb4GXwadDzh9cXlaGxbrfC4Kzd-nqbZqvRdJGvEEHNyoD0eW7xwrPo-FCHDp_KYOQ51gFtVqUqHc0Xp39LU9BVcJARoenlCKcMbWtzoyR82DJtrbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ربات‌های چینی با لباس‌های سنتی عربستان، برای شهردار ریاض و سفیر چین رقص محلی اجرا می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72649" target="_blank">📅 09:24 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
