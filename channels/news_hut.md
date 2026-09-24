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
<img src="https://cdn4.telesco.pe/file/hdrV6YhTaG3fbObnFoVwWOQcbpn2pSnz7kP9leXsXH0Qcg0znWe43TYQOx5Ljs7-qhiWJZQFsx3SNw6q7UsF2M-D_vVyGa5zJzh_jnGno238bl1tEyY4vL8M_Nuk606nHKwnkuDb4Hq_cxHwOkPnElC_joS5lO32q5P031YqL6NU26XWrRYtWELfacSkww775kKaSdYz0sDBBWq2PlXTKjE0ivLS1LNLYDQ0veo-m7S1VXQ8ZOqtl4_3_VHFFNkGixEtAOimlSm8OKh2uCTR41GihyVpKug3LpNDtpzkSZFAN9_CyhHTfxV5UznUsP0z6S-5K_6TOoE6inTTceKIng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 14:17:46</div>
<hr>

<div class="tg-post" id="msg-72169">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAGwXhtDlgzUiIgpEKR_YPVkOi2wQB3JL1pFxfwQOjwOkEOI-Ilfw71Q4p_WQaYaBu69BVPMP27t80DjfkJ_mRlvfoaY-4soWt9dDwMziGQ1umZgUYf51eSjOVAnne9CnKk7JLEIF0pHKMfL2rCTYhf4rZ-KX6i7DaVSz8M5SMCzrlo3oz3EKeJystCctFu5LxPZ_oZt6woO0FNFLRUPTWjmN8jf7K1NOOuvVHqooLyamMKpDBDl6KDs8lnFX-nV-h1wCHs-o4l2Q-C2tbFutW1-IKPhE-Ji_VP2YsoiId-butUXeniayZNWdn0cRtA9koVgNbIg0ZGs9tbr-6xB2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش ایسنا و به نقل از سازمان هواپیمایی کشوری ایران، تمامی پروازهای شرکت‌های هواپیمایی ایرانی به مقصد امارات از نیمه‌شب لغو شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/news_hut/72169" target="_blank">📅 13:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72168">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f0e98c345.mp4?token=AO51_RrWOgivMK4hdVmIsL4TKMrLqZskGenuROzJ4xaL9yCjf1kO0Xr2U2XWFNLkR9XX9LG8qlHvA9t_cDl80uTXwwKhgRhJPv9MwqO8k9brSC4V6Y8uOQAxzRBescVbUXI_gWf901dwk1LYhH0tMRBAcECIvLUT3y1kBZWaSufnNxbSDgSSE-Lu8Wq5NVJ50fVJkkuGJD2cJW60ixyg-jH24PhFpxpSBkwURcPf2S_gpMgSxQnX5VuDZMfXFKAOwHkbm3n8P-WFxFdF_1Q6SA_dpb3SX2D2uq0JDUDFxebQJEA_xb9P6o8TzyxbXZEWpbLR3WKuojtFDsaRmbNyP173xWHKkagPR7sklOC0-U5CBBDgH6656RUqoUISP259Fon7VGUGFpuqP9NM05T3ebxPpFM6dO9lBlqbIWm7YkqFp-_Hdo2Zl0H0Bo_MobfZwsYTzNqelBUb30rvpE1_g_GGfYPB8c8oXYLmyZYeIEiYT1kNp98UKXZ9ZIw3CFMbdydT4wuVqMSLh_mKEZN40sbLnAF8BmxtCvtuI2zr3A2_RG4eGFEI20rd2mpgEslo6x094lZ2hTqUzR-G3EeQYrP-P3afV-VHzltGnyfl04dUPA8WNE1guvmtHLX8YY8WHli1_gr1FfEgb4_cxctyqAFP73ud1O4PtvM4nLBEGzI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f0e98c345.mp4?token=AO51_RrWOgivMK4hdVmIsL4TKMrLqZskGenuROzJ4xaL9yCjf1kO0Xr2U2XWFNLkR9XX9LG8qlHvA9t_cDl80uTXwwKhgRhJPv9MwqO8k9brSC4V6Y8uOQAxzRBescVbUXI_gWf901dwk1LYhH0tMRBAcECIvLUT3y1kBZWaSufnNxbSDgSSE-Lu8Wq5NVJ50fVJkkuGJD2cJW60ixyg-jH24PhFpxpSBkwURcPf2S_gpMgSxQnX5VuDZMfXFKAOwHkbm3n8P-WFxFdF_1Q6SA_dpb3SX2D2uq0JDUDFxebQJEA_xb9P6o8TzyxbXZEWpbLR3WKuojtFDsaRmbNyP173xWHKkagPR7sklOC0-U5CBBDgH6656RUqoUISP259Fon7VGUGFpuqP9NM05T3ebxPpFM6dO9lBlqbIWm7YkqFp-_Hdo2Zl0H0Bo_MobfZwsYTzNqelBUb30rvpE1_g_GGfYPB8c8oXYLmyZYeIEiYT1kNp98UKXZ9ZIw3CFMbdydT4wuVqMSLh_mKEZN40sbLnAF8BmxtCvtuI2zr3A2_RG4eGFEI20rd2mpgEslo6x094lZ2hTqUzR-G3EeQYrP-P3afV-VHzltGnyfl04dUPA8WNE1guvmtHLX8YY8WHli1_gr1FfEgb4_cxctyqAFP73ud1O4PtvM4nLBEGzI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:جمهوری اسلامی در نهایت تسلیم خواهد شد.
نمی‌دانم یک هفته طول می‌کشد، یک ماه یا دو ماه، اما آن‌ها سرانجام تسلیم خواهند شد.
هدف در اینجا می‌تواند یکی از این سه حالت باشد:
اعضای رژیم به جان هم بیفتند؛
نوعی قیام مردمی در ایران شکل بگیرد؛
یا اینکه ایرانی‌ها را متقاعد کنیم که اگر خواهان توافق هستند، به آن پایبند بمانند.
این بار، اگر توافقی حاصل شود، تضمین می‌کنم که آن‌ها به آن پایبند خواهند ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/news_hut/72168" target="_blank">📅 13:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72167">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb27b8d8bc.mp4?token=VbF8QtOVr-jUZJIchRw-nV-2_NPYBIMvlzAXwT8UzWT3cTpNX2Xu2j-04fd2gSO2Ziu0sFOTnlR_N2nUJHgT6CfTFldJrkK7V5P74JpXNDvOwNf-YLBDQUY3Ftgex0WkjTQbGYC0fOG_0DSQVUa3vUHvUhzDb6QD-952ZKQxHslnwYSjl9Ua3cPADiCozNap-C5IU6mKdpO6upjhY8pnr234_mEct1V8m_BM9knSr5JnLzNtQ5kb6a_FsRWQgwCuQz-7q8oNOd9ICyo5qi2t76YN7UP1AcgN-kEeQIwF9C2FeRl4VDEaEiTNWk_yFy39S8RsKG1Ujoi_ZjyegBv87A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb27b8d8bc.mp4?token=VbF8QtOVr-jUZJIchRw-nV-2_NPYBIMvlzAXwT8UzWT3cTpNX2Xu2j-04fd2gSO2Ziu0sFOTnlR_N2nUJHgT6CfTFldJrkK7V5P74JpXNDvOwNf-YLBDQUY3Ftgex0WkjTQbGYC0fOG_0DSQVUa3vUHvUhzDb6QD-952ZKQxHslnwYSjl9Ua3cPADiCozNap-C5IU6mKdpO6upjhY8pnr234_mEct1V8m_BM9knSr5JnLzNtQ5kb6a_FsRWQgwCuQz-7q8oNOd9ICyo5qi2t76YN7UP1AcgN-kEeQIwF9C2FeRl4VDEaEiTNWk_yFy39S8RsKG1Ujoi_ZjyegBv87A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی دبیر شورای عالی امنیت ملی رسما فرودگاههای کشورهای همسایه را تهدید به موشک‌باران می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/news_hut/72167" target="_blank">📅 12:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72166">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd3cb8e2e.mp4?token=F8YSFgrhVwUNP9NQFtsiQGzbSdrUoS6GCSHAZp3tyrOVSMAvUJMWX5t92FAJ1v5Idhg8VP8o1Q91M3_VBRfkq6ZQn9zUvDZqS5jzHcABMh9t8Qlh15J3Sjiw0m2M9odQEz6iXLmdDJkY3epu4O72BG7CkFlKjs05zFxW3q9P8HVzgT6cHc9uGpBuwN6o2W8kTIwvi7ObUXOu0AsueGTbqign9vIMgK72u5d3E062eh2DhNL3tSWTU2JZBkR1UUt0W3EpM1KZiXZGLsbRMLmjdfefCEJMI7Z6zbL7H6cruxmsgtijVbOFyqU2JUn_5-AJkUop5dU_mkvOohbtEgAgHn_N9iBlADjdWozl2plaPkfnYzt-z78-XWfNPCXLTJDLLNPgCClJutRyD-3DAGOvTQ1TTDetETGDuiYc1OHShZQDmDKnmcKO5J-fRT4G2YbWOB72TFYXpKYjKcxZniQsgdRecZFKZTzE6UhrgSnPw-axux6Pk18PT0ibnoMrun4ABdGiXrWUggiIe748vMhaPAyQVtNx2kgVZYODsl48YN8KoFQ0tyjGK7Uqfys2JvZAtdKXYjqZpeFES2xJhIFap2HQj_a4wwt2GvWTmPqGLbmKtC3wndo2gHTAQAhx-WxU3sRgO7avP13segTlrba9S3-CP2lzq-zrHdsk2MGD9JE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd3cb8e2e.mp4?token=F8YSFgrhVwUNP9NQFtsiQGzbSdrUoS6GCSHAZp3tyrOVSMAvUJMWX5t92FAJ1v5Idhg8VP8o1Q91M3_VBRfkq6ZQn9zUvDZqS5jzHcABMh9t8Qlh15J3Sjiw0m2M9odQEz6iXLmdDJkY3epu4O72BG7CkFlKjs05zFxW3q9P8HVzgT6cHc9uGpBuwN6o2W8kTIwvi7ObUXOu0AsueGTbqign9vIMgK72u5d3E062eh2DhNL3tSWTU2JZBkR1UUt0W3EpM1KZiXZGLsbRMLmjdfefCEJMI7Z6zbL7H6cruxmsgtijVbOFyqU2JUn_5-AJkUop5dU_mkvOohbtEgAgHn_N9iBlADjdWozl2plaPkfnYzt-z78-XWfNPCXLTJDLLNPgCClJutRyD-3DAGOvTQ1TTDetETGDuiYc1OHShZQDmDKnmcKO5J-fRT4G2YbWOB72TFYXpKYjKcxZniQsgdRecZFKZTzE6UhrgSnPw-axux6Pk18PT0ibnoMrun4ABdGiXrWUggiIe748vMhaPAyQVtNx2kgVZYODsl48YN8KoFQ0tyjGK7Uqfys2JvZAtdKXYjqZpeFES2xJhIFap2HQj_a4wwt2GvWTmPqGLbmKtC3wndo2gHTAQAhx-WxU3sRgO7avP13segTlrba9S3-CP2lzq-zrHdsk2MGD9JE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«پرواز هواپیمایی وارش» از «تهران» به «دوشنبه» _پایتخت تاجیکستان_ از مرز هوایی لغو شد و به فرودگاه امام خمینی بازگشت.
این هواپیما سعی داشت از مسیر جایگزین و از سمت آذربایجان وارد تاجیکستان شود که مورد موافقت این کشور نیز قرار نگرفت
@News_Hut</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/news_hut/72166" target="_blank">📅 12:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72165">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/news_hut/72165" target="_blank">📅 12:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72164">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAwMfgMjEonGIajxScOGkVoWN7AKj6e0-dn-lklao6PrGQruqIe4tWJRJsGRjEZV-EIY6ksQWShQfKjWVbzk1X6FrxeJt5GjB8d72w-QFH-fMEJAcWuZG5cbO1oiyxqRJ9jJgXo7sJwFeK-ioUgBoLn6P_d17md5Rxn5yhBgR7FR8kSKzwhJI_WbYPwkzx-KwWbJ9lOJUA8K8ffafyoFfo0jSI3c63DcBvDPUEj5_XaAzJyhypG4TdITzWPTum8HQxkwYogTkXUvm9e2TUqxpnLb9dfM2wn0tkll1S1mJ6z4V7yaER_58tEJPCsFV-zi44ym_EBKtxPZBXNZo3OiXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آلمان
🆚
هلند
دانمارک
🆚
نروژ
ولز
🆚
پرتغال
اروگوئه
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
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/news_hut/72164" target="_blank">📅 12:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72163">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2bbdedf07b.mp4?token=EzvTNuRqbsErtQhLAQarbSXwihbqt3tBqZ4qNIFM-o9rQaa-j-0vMQw2jsgKEyzJn9GkACjwaaI8UeEINs9awPt8TrMTH4Rs7aSaMxUL0y1z7AT6qBZlBtxlwRwdYZQYtdQn-czFiDA1ScTen7C7xzn8Cbub_xgB6TAux387GVpkp7M-Z_tTH5Rr0zVlz-eYtRs_FADfc8DIeUx02DloRPgZ1VlU9x-Vo5Bfgk4BeqFDseGs7OEo8tTS0L9g9bsdaDmOaV_eGfPsRk0KAbEqfuO5iIMnewnzGX2oq4Pd67BNkbDee32hrvAHEFUZ-GCkiIR5q5MU5B-YoSwXqOMRfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2bbdedf07b.mp4?token=EzvTNuRqbsErtQhLAQarbSXwihbqt3tBqZ4qNIFM-o9rQaa-j-0vMQw2jsgKEyzJn9GkACjwaaI8UeEINs9awPt8TrMTH4Rs7aSaMxUL0y1z7AT6qBZlBtxlwRwdYZQYtdQn-czFiDA1ScTen7C7xzn8Cbub_xgB6TAux387GVpkp7M-Z_tTH5Rr0zVlz-eYtRs_FADfc8DIeUx02DloRPgZ1VlU9x-Vo5Bfgk4BeqFDseGs7OEo8tTS0L9g9bsdaDmOaV_eGfPsRk0KAbEqfuO5iIMnewnzGX2oq4Pd67BNkbDee32hrvAHEFUZ-GCkiIR5q5MU5B-YoSwXqOMRfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که یه پسر از روتینش قبل از رفتن به مدرسه منتشر کرده:
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/72163" target="_blank">📅 11:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72162">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa04cd3fe8.mp4?token=m8gxOTVduvxl-STCaot23Q5Cffh2AxIqSmuJ__2-dejxVU13AGAByzkwlcpOeAIEbqpbLFK0k3UKf60njn52aN8232IBBrqjD6M0xlVSf02jA626LF5PJAd34h1Hh_zsW0anq1QtCa0POsDG4ES_99oMrAVmEzLsZRNwucczt0x189B6TpmELbMtk91cS6h2M7-Ejp3qzDnqj-A2hgwXLPt2E_OrNgWnwW2Cg6eU5GF34j1Svnfn-XQhaKGsD3Qyo0_2BN65tnIGfXisnh4WhhcNF8QsUF-aYKWkkrgFQUAidsZvz3OwOQJj8mkdOYoAm7YMOD2kZE0hFIYxTm-ALLpU_KXZs4OhO-PWxCexF6WcRwI-ca-92A6oHLqLxXDewhCushSJwyT450-Z7L06a_M9NNaKDEqsLGyY6YjiAaUZoAZHZOYkTnUNT3CiFp15yKl2lh8R_DzL1IOX5xjXgVycuplFnOHEyA45SqyKWhj_zacbitZyW3rxnO3k1l_yoP7HJGHF4yr7UqgXm4YDgfZbjXt0TYNnNYxOgAOIvXDez4gGIhIhBhbpEeIbLNehNBkNkxIJZyFDzuigZfCkaJRJCiHVCy0PivJhd1K7rhPVbbnUA3FJDfRA6AhBNcG3drMOGCjujOguyLnrU-MBkpD1q18UBvXv0doF85hU2ZY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa04cd3fe8.mp4?token=m8gxOTVduvxl-STCaot23Q5Cffh2AxIqSmuJ__2-dejxVU13AGAByzkwlcpOeAIEbqpbLFK0k3UKf60njn52aN8232IBBrqjD6M0xlVSf02jA626LF5PJAd34h1Hh_zsW0anq1QtCa0POsDG4ES_99oMrAVmEzLsZRNwucczt0x189B6TpmELbMtk91cS6h2M7-Ejp3qzDnqj-A2hgwXLPt2E_OrNgWnwW2Cg6eU5GF34j1Svnfn-XQhaKGsD3Qyo0_2BN65tnIGfXisnh4WhhcNF8QsUF-aYKWkkrgFQUAidsZvz3OwOQJj8mkdOYoAm7YMOD2kZE0hFIYxTm-ALLpU_KXZs4OhO-PWxCexF6WcRwI-ca-92A6oHLqLxXDewhCushSJwyT450-Z7L06a_M9NNaKDEqsLGyY6YjiAaUZoAZHZOYkTnUNT3CiFp15yKl2lh8R_DzL1IOX5xjXgVycuplFnOHEyA45SqyKWhj_zacbitZyW3rxnO3k1l_yoP7HJGHF4yr7UqgXm4YDgfZbjXt0TYNnNYxOgAOIvXDez4gGIhIhBhbpEeIbLNehNBkNkxIJZyFDzuigZfCkaJRJCiHVCy0PivJhd1K7rhPVbbnUA3FJDfRA6AhBNcG3drMOGCjujOguyLnrU-MBkpD1q18UBvXv0doF85hU2ZY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدیداً دوست‌دخترای مردم دارن برای پارتنراشون آیفون 18 میخرن:
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/72162" target="_blank">📅 11:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72161">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دیروز صبح، تو یکی از مدرسه‌هایِ اندرزگو تهران، شروع سال تحصیلی رو اینجوری شروع کردن :
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/72161" target="_blank">📅 10:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72160">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c86f2846ed.mp4?token=sYL4nwFyiLBMP-_6YGtFMafTdYwj9o0wPxFAZJHGWDuLSTdtCaqwja6mCkrS2QJU1_sxzf7FNlASNh_QouT5HlhVq6n9BN6vZ6Z6kkLNFFGy8IXAa_suiAPIyvekPAJEds7NikmEGhxswzKheoyCGB8H2mdo-LuhdwZzD2y7A0Ty6jW_rL6fx2SCuwroBRjirSjZbY669sWDN68O8tpczosp04x8rE2PIuAk9RcJd4sDWN-Rd-ezIrqHZGAXHMigCruAFTuRFMGTgVU3kTTNooaTZRBaz9ozjAnpPhWW7eZ0uvYvHmbyC5MAV56PA4E4BvDUhJUfomE22gYl3A9mbw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c86f2846ed.mp4?token=sYL4nwFyiLBMP-_6YGtFMafTdYwj9o0wPxFAZJHGWDuLSTdtCaqwja6mCkrS2QJU1_sxzf7FNlASNh_QouT5HlhVq6n9BN6vZ6Z6kkLNFFGy8IXAa_suiAPIyvekPAJEds7NikmEGhxswzKheoyCGB8H2mdo-LuhdwZzD2y7A0Ty6jW_rL6fx2SCuwroBRjirSjZbY669sWDN68O8tpczosp04x8rE2PIuAk9RcJd4sDWN-Rd-ezIrqHZGAXHMigCruAFTuRFMGTgVU3kTTNooaTZRBaz9ozjAnpPhWW7eZ0uvYvHmbyC5MAV56PA4E4BvDUhJUfomE22gYl3A9mbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسره از خروس میترسید و رفیقاش گفتن اگه بتونی 10 ثانیه نگهش داری، بهت آیفون 18 پرومکس میدیم.
و در نهایت این شاهکار خلق شد:
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72160" target="_blank">📅 10:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72159">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/034c3c71b1.mp4?token=L2CUH0FXvygiC5e-Vf_Uq6xtwLKtu5PkmjntJI1n0GVFHDaF3EcyZ7b7XEwo_rYH9nKnZeuTxPB3K4Mqhd3h9u6aiuEsCVK4WfCtBJfsMNY_axDg9M4Lez_ghK_ssr2v-TggVGw0lqE_5Yj_KGC-JIGqDVO7NIaLC9A6NR0wPZrghGnaiCe9SwMRr9S9lk0p2NXV9OIBv38MY5bB0Qv5j9WeGowgTX5Rnsy-rkP6zR4Lte1_UnW5yiI5YbVt-DzyW9ILkD4yFPZpTQwa8VBfNRxMYvBzoVzIyeZ_RsSWBZUGPtLc-Juluae5aqLF7wxLMkinYEkHicfZy0P6zj2irg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/034c3c71b1.mp4?token=L2CUH0FXvygiC5e-Vf_Uq6xtwLKtu5PkmjntJI1n0GVFHDaF3EcyZ7b7XEwo_rYH9nKnZeuTxPB3K4Mqhd3h9u6aiuEsCVK4WfCtBJfsMNY_axDg9M4Lez_ghK_ssr2v-TggVGw0lqE_5Yj_KGC-JIGqDVO7NIaLC9A6NR0wPZrghGnaiCe9SwMRr9S9lk0p2NXV9OIBv38MY5bB0Qv5j9WeGowgTX5Rnsy-rkP6zR4Lte1_UnW5yiI5YbVt-DzyW9ILkD4yFPZpTQwa8VBfNRxMYvBzoVzIyeZ_RsSWBZUGPtLc-Juluae5aqLF7wxLMkinYEkHicfZy0P6zj2irg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم لحظه سقوط یک جت آموزشی RAF Hawk T2 اندکی پس از برخاستن از دره RAF در انگلیس امروز را نشان می‌دهد.
هر دو خلبان به سرعت بیرون پریدند و زنده ماندند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72159" target="_blank">📅 09:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72158">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04b2935ddd.mp4?token=ZLCnnv8-WCcZK2kkl1SYYIbaQL3uk6sJZnqTa2lES1AcDVwfpA51Ibl9C_EdSgE_Bg8K6NvCTF_o1DhEgoQeWsyHpfnjTdv266_Zfj3cBUpadq_jDEJvSIDlzkPfEjb25v4oyEdMQiiqbMkQ930_lOQQghiGEM25DO5WV6KKav8jVAo1rLhpeUiLfabl4VY1vRO6wgHk6p99AXfGNFA664c9P6IU_ZA6akv5foRxeQ66_9Bk4TltOw7suR6Ut08eWAIyXM-r5FJcDGK19Lda1yKJ-WsnFPSEniMs4iI_xSMYNErjsR_fxteE2Qe3niarsm0TsQv_BBaXxBQYGyc-KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04b2935ddd.mp4?token=ZLCnnv8-WCcZK2kkl1SYYIbaQL3uk6sJZnqTa2lES1AcDVwfpA51Ibl9C_EdSgE_Bg8K6NvCTF_o1DhEgoQeWsyHpfnjTdv266_Zfj3cBUpadq_jDEJvSIDlzkPfEjb25v4oyEdMQiiqbMkQ930_lOQQghiGEM25DO5WV6KKav8jVAo1rLhpeUiLfabl4VY1vRO6wgHk6p99AXfGNFA664c9P6IU_ZA6akv5foRxeQ66_9Bk4TltOw7suR6Ut08eWAIyXM-r5FJcDGK19Lda1yKJ-WsnFPSEniMs4iI_xSMYNErjsR_fxteE2Qe3niarsm0TsQv_BBaXxBQYGyc-KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تعجب از  عکس‌العمل بی‌تفاوت نماینده جمهوری اسلامی در سازمان ملل، به تهدیدات ترامپ در یک برنامه تلویزیونی
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/72158" target="_blank">📅 09:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72157">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad1a7d8580.mp4?token=nHvcKVMl6zb4I--8lDm8LUwPnjOM2iQ4w6v7YSTGgGdqtnXyZU2_Y57TpYCa9SPMLnIzmPAEGowIlIgGMLQOQnEmqB1dqHXd0hpLQUHo6K4CQsnpNdUHQphSQ-3unaILCEp8D_qJA1nj44EmuECdzvWw9kY6Je9py_s68qzIk8V1mXqvU_SLWd6O8iCNQyq9OKGuHuQvddFOh3s77pMYjtn3a-A61kgs4-Wl9qA7rQU7xva4Kc9ZZHtXqPSmn95ljfxjQGMJHWjwe3kcusGZRoyinMAkw2bMM3g07djkaFI5w072NjgOwHvUz0XM4LSQiIMzlQuJlsWXjmhf2uuaCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad1a7d8580.mp4?token=nHvcKVMl6zb4I--8lDm8LUwPnjOM2iQ4w6v7YSTGgGdqtnXyZU2_Y57TpYCa9SPMLnIzmPAEGowIlIgGMLQOQnEmqB1dqHXd0hpLQUHo6K4CQsnpNdUHQphSQ-3unaILCEp8D_qJA1nj44EmuECdzvWw9kY6Je9py_s68qzIk8V1mXqvU_SLWd6O8iCNQyq9OKGuHuQvddFOh3s77pMYjtn3a-A61kgs4-Wl9qA7rQU7xva4Kc9ZZHtXqPSmn95ljfxjQGMJHWjwe3kcusGZRoyinMAkw2bMM3g07djkaFI5w072NjgOwHvUz0XM4LSQiIMzlQuJlsWXjmhf2uuaCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
ممکن است به نفتکش‌ها حمله شود؛ اما بسیاری از آن‌ها به مسیر خود ادامه می‌دهند. آن‌ها صرفاً به حرکتشان ادامه می‌دهند.
ایرانی‌ها ممکن است ۳، ۴، ۵ یا ۶ پهپاد به سمت آن‌ها روانه کنند، اما نیروی دریایی قدرتمند ما مانع آن‌ها می‌شود.
با این حال، ما روزانه بین ۱۰، ۱۵ و گاهی ۱۷ میلیون بشکه نفت صادر می‌کنیم.
برای درک بهتر این ارقام باید گفت که پیش از آغاز درگیری‌ها، این میزان ۲۰ میلیون بشکه بود؛ ضمن اینکه احتمالاً ۳ میلیون بشکه دیگر نیز از طریق روش‌های جایگزین صادر می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72157" target="_blank">📅 07:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72156">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dfe7fd741.mp4?token=JAtMp7v3ySd6FfwnAE1CyHedbTmfb-ky-YDbZsG1TtmtVzQNi7J2S3lbLYeITlrulwBDptvX0RnziIlk8oh9CFaeWf9UaGLm4U4sd3ZM89xUTJCRqmvEN_r5UWiAAAdD9WOE9TIQOr5Ca0HwZA9urjNN1E1hJSBVCurGV_jIjbmQNwvDpp9uc5ph0HUvhzw_wcJFfellNWuUA0SKiIrmlkKQc1Pdn2mQ5W0o2Tu3KeJk02NVYYVSJpGHFcHndl4PE74bZUgYnG6wqcy2snQZ1w3GRLny6kBlH5wqU6dLfVcbLkoMwAxf5Az4t8-slHHAlpD-blZqIRsX54n6FxuXLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dfe7fd741.mp4?token=JAtMp7v3ySd6FfwnAE1CyHedbTmfb-ky-YDbZsG1TtmtVzQNi7J2S3lbLYeITlrulwBDptvX0RnziIlk8oh9CFaeWf9UaGLm4U4sd3ZM89xUTJCRqmvEN_r5UWiAAAdD9WOE9TIQOr5Ca0HwZA9urjNN1E1hJSBVCurGV_jIjbmQNwvDpp9uc5ph0HUvhzw_wcJFfellNWuUA0SKiIrmlkKQc1Pdn2mQ5W0o2Tu3KeJk02NVYYVSJpGHFcHndl4PE74bZUgYnG6wqcy2snQZ1w3GRLny6kBlH5wqU6dLfVcbLkoMwAxf5Az4t8-slHHAlpD-blZqIRsX54n6FxuXLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
احتمالاً بیش از ۸۰ یا ۹۰ درصد پروازهای خارجی از مبدأ ایران متوقف شده‌اند.
مطمئن نیستم نمایندگان ایران در سازمان ملل چگونه قرار است به کشورشان بازگردند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72156" target="_blank">📅 07:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72155">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72155" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72155" target="_blank">📅 01:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72154">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWBhKZ_QBQKomiZWBeNz0LmW4dWcDI6G9UWWYUY6GSuwcDOlziP-n5s1DraBSgWYGgsYho2I83ownXb5guY4mXLUaP2tBYx8RfUF9cF8Tms28s4dkL_4X3AQcAoz0FMCDzu99WK0_q8b-aL4pCoxwNULSkdx5mIOwQGqmvHUEgMQ5s9iLnxt5_K8RzK1oY6Nx8EGzqmEcgiCF2O8yrEEdYvZjjEghyxaBSPShmS6o3mCIFMsfWdjHTG1902uQ-UCqBdKAIfSuyPiJIeyfYNpx3JQUDhjCLcE25668mvWOs2_h1MFYG6CLm9RLAj-zhR574KGGvc-ot5_QfbvVUHzjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72154" target="_blank">📅 01:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72153">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c59219ac7.mp4?token=qJd6XqSvRUNpMH-SPVz2oMWOoMZnDf3eNKQJzB2YM3VQVMnhFr9t-cyhGNFEGy8j-XAnwowj_hkyd6oY9-89vlT0dkZWQnuV4g2yAuJ5qmbEra7Mp89Qh6RgQlOQ3iHd4HtylelPSO7fqONuhnF6UWCA4M6Pla8SjchEsDza7TWtFgb65GCjCxahLt3asA2htMJuzbThI93gdHUT6aHWIkj_KHvyNKAyP-wf_sYcSCE8Ruw0Lo3WaC9V3bXpyxsbU0aw8eSV7HPysJVrpV099Rf0wis8yOYzQBoYfcMYFzUoQv2bF5wyhw-0Hk2s-UKU3Sg0LpSiXJt1cyyDmQhkXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c59219ac7.mp4?token=qJd6XqSvRUNpMH-SPVz2oMWOoMZnDf3eNKQJzB2YM3VQVMnhFr9t-cyhGNFEGy8j-XAnwowj_hkyd6oY9-89vlT0dkZWQnuV4g2yAuJ5qmbEra7Mp89Qh6RgQlOQ3iHd4HtylelPSO7fqONuhnF6UWCA4M6Pla8SjchEsDza7TWtFgb65GCjCxahLt3asA2htMJuzbThI93gdHUT6aHWIkj_KHvyNKAyP-wf_sYcSCE8Ruw0Lo3WaC9V3bXpyxsbU0aw8eSV7HPysJVrpV099Rf0wis8yOYzQBoYfcMYFzUoQv2bF5wyhw-0Hk2s-UKU3Sg0LpSiXJt1cyyDmQhkXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فروند بمب‌افکن B-1 Lancer نیروی هوایی ایالات متحده، همزمان با استقبال پرزیدنت ترامپ از شی جین‌پینگ، رئیس‌جمهور چین، در واشنگتن، بر فراز این شهر پرواز کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72153" target="_blank">📅 01:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72152">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a5acb93e6.mp4?token=JoclJLIJySyKnrxy-QDSRZeOnLyyZ7WzyextMOOzBfs_2vDxoXZ5hZLU0T_QYA0RXXlqEg2NA5N3fhm1msFc3hOJ01f0vr5DA0K6pDcYkuXxsB8nvlKMMfi_JyMYmJxCtIzYjv9--36TbdKYUe9CiAA2G6PowHdM9MEpmcWFMqaZjn2aAc_4icQugi_mpZXv7d7isIpDH7j9nuva8AwU5CARMu5ICTIGutJ9PSauAMek6r5zcm8f3_0iYJ1Sv-_XNhsAx7EkEkzfhTAfYlh_KlTBuO-eTRW59YMA19TVCFAzI-dnJ9eF3xB6Injp8wHUlmwSDIw3hLall6DX_vwhvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a5acb93e6.mp4?token=JoclJLIJySyKnrxy-QDSRZeOnLyyZ7WzyextMOOzBfs_2vDxoXZ5hZLU0T_QYA0RXXlqEg2NA5N3fhm1msFc3hOJ01f0vr5DA0K6pDcYkuXxsB8nvlKMMfi_JyMYmJxCtIzYjv9--36TbdKYUe9CiAA2G6PowHdM9MEpmcWFMqaZjn2aAc_4icQugi_mpZXv7d7isIpDH7j9nuva8AwU5CARMu5ICTIGutJ9PSauAMek6r5zcm8f3_0iYJ1Sv-_XNhsAx7EkEkzfhTAfYlh_KlTBuO-eTRW59YMA19TVCFAzI-dnJ9eF3xB6Injp8wHUlmwSDIw3hLall6DX_vwhvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شنیده شدن صدای تیراندازی در جهاد‌آباد سراوان
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72152" target="_blank">📅 01:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72151">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4470cff685.mp4?token=dH_HPuYGrAuijIlt5SpGMeUwnvKPLzTXVnffXsruilWyUbr2z0T8VQI2QTOcTW8RZNbhc-gSnMm8D4jP9ihPe-zng-1DjOxNUHxrx_Vp9pNxcrKpxqBhWm8Z-5CJ8JUUoPojpCgE1B4R1faod3FeuV49jAHZgtW1KlMNbv1_jwyeoDNvOl8vfH2Vw3R6Gfo7Xy4hgOTKEgVYTH56FDQOv0HUguwzzw6H9Flv4YzxXc9coM6uMSMfrHqoEAh3gq5011SwW2MRsdRPm_qUWXwwQvWjNl9AAQ6_K9t5QmqtdpkVAamogcHpY7KEDZrz192didh2MOPyYO6qKhi6VciKmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4470cff685.mp4?token=dH_HPuYGrAuijIlt5SpGMeUwnvKPLzTXVnffXsruilWyUbr2z0T8VQI2QTOcTW8RZNbhc-gSnMm8D4jP9ihPe-zng-1DjOxNUHxrx_Vp9pNxcrKpxqBhWm8Z-5CJ8JUUoPojpCgE1B4R1faod3FeuV49jAHZgtW1KlMNbv1_jwyeoDNvOl8vfH2Vw3R6Gfo7Xy4hgOTKEgVYTH56FDQOv0HUguwzzw6H9Flv4YzxXc9coM6uMSMfrHqoEAh3gq5011SwW2MRsdRPm_qUWXwwQvWjNl9AAQ6_K9t5QmqtdpkVAamogcHpY7KEDZrz192didh2MOPyYO6qKhi6VciKmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شی جین‌پینگ رئیس جمهور چین وارد ایالات متحده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72151" target="_blank">📅 01:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72150">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رسانه‌ی حال‌وش :
دقایقی پیش تو محدوده‌ی جهادآبادِ سراوان تو سیستان و بلوچستان، درگیری مسلحانه‌ی سنگینی شکل گرفته به طوری که آرپی‌جی هم شلیک شده!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72150" target="_blank">📅 01:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72147">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d2cde76e35.mp4?token=GER1TuMtFghrH4wQ-cbWER4uUuZg5i_qtRJSvAoPJ1Zip6-ukseHf5688EkUO60r8ruuchHzgETS-DWRhkmnS3b1j7T8cRlozozZ_V_LOWWhvrYJCZKiAMWpyx-GabjqgRVAd0dX_TkMtqvAsTxA4DdkSN1P1QDzb020NMgnPzFYPs7JDmkFRLjzkr-w2ExQkycFqjzvdgIJaUY6t_es-EKdtz9pc8ZLepos4CXPVvlJr98Wdo0KsekHWmunmL6pjVxxjS4Q-aJQ9nI_9srXg9BJ9fpixN2YCzoqPneRm9ZF5jgpbSbww4zHdYPg3dO_bPR4hY6Dt-LCh4UM7qwC-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d2cde76e35.mp4?token=GER1TuMtFghrH4wQ-cbWER4uUuZg5i_qtRJSvAoPJ1Zip6-ukseHf5688EkUO60r8ruuchHzgETS-DWRhkmnS3b1j7T8cRlozozZ_V_LOWWhvrYJCZKiAMWpyx-GabjqgRVAd0dX_TkMtqvAsTxA4DdkSN1P1QDzb020NMgnPzFYPs7JDmkFRLjzkr-w2ExQkycFqjzvdgIJaUY6t_es-EKdtz9pc8ZLepos4CXPVvlJr98Wdo0KsekHWmunmL6pjVxxjS4Q-aJQ9nI_9srXg9BJ9fpixN2YCzoqPneRm9ZF5jgpbSbww4zHdYPg3dO_bPR4hY6Dt-LCh4UM7qwC-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«اتحادیه دریانوردان هند» (Forward Seamen's Union of India) خبر مرگ یک دریانورد هندی را بر اثر حمله نیروی دریایی سپاه پاسداران با دو موشک کروز ضدکشتی به عرشه C و موتورخانه کشتی فله‌بر «MV CAPE DAO» اعلام کرد.
کشتی «MV CAPE DAO» متعلق به شرکت «ForthMarin Corp Ltd» است که در امارات متحده عربی مستقر می‌باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72147" target="_blank">📅 23:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72146">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rp28E_J__NrOIiiZvkXUHr7YD5I2oiV4qrIYWVBeTLKOr8wJSfQXY0bykeex0Mo2qhjphzLgznT5DxsCadps-RMdDYpDdHPwSnuXgYV8TiBLxzOnsmQ5ZVFTtudP2-WBYxNjGipeEOCU-g157feGzfdEZmJVQKbRpu7gtFdx1cZ6GOruWJ6BrwHRFlNkMERSbzUfn_QVBqgmEyuCYux79eoPJmOHkpYfQAcbvBvbRdTw8NGv8jYY5FCQAj-MhmqylFvM6vEJ84aDFE5fOXxOK__9bS6NyViO8LZFi7P4F5Tp2lzpq8QMOWWZM1Mx0HmN8joNBK5TnpavPWfmJGm-pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار ظریفی فرمانده سپاه شهرستان سراوانِ سیستان و بلوچستان، توسط افراد مسلح ناشناس کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72146" target="_blank">📅 23:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72145">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/223e8fa625.mp4?token=uKTPb8sLwm2wzLev0EklKdPjcN2EaUqRfsHNLspVpVeR1JTmwa2Axw7X0rIHGxkbVbLLOW6NAkvFQUpCt9bsPkeyI0aZmkynEz1N9tNgD2LRVWYnMJXOJplo_rf0eTl7jWDPSXAMrMDpi-CUPH0rfD1DvGEphh9iVDJIGet7w5NofgWKvW7BcrGNqRSRicr29CKFieK914nz-P1riMHaUhtuqMi6O_b_Zs7XkZUi1eatC6J6v5Ezph2L-NXOn-Em3lqjCHfV9WWvS0ts4evC7qwpprDq-bFwm89cmUKNiXDypkTrs3rUzIBRQbh9UoG3YhXrDt3EuD1V52zcYa2vZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/223e8fa625.mp4?token=uKTPb8sLwm2wzLev0EklKdPjcN2EaUqRfsHNLspVpVeR1JTmwa2Axw7X0rIHGxkbVbLLOW6NAkvFQUpCt9bsPkeyI0aZmkynEz1N9tNgD2LRVWYnMJXOJplo_rf0eTl7jWDPSXAMrMDpi-CUPH0rfD1DvGEphh9iVDJIGet7w5NofgWKvW7BcrGNqRSRicr29CKFieK914nz-P1riMHaUhtuqMi6O_b_Zs7XkZUi1eatC6J6v5Ezph2L-NXOn-Em3lqjCHfV9WWvS0ts4evC7qwpprDq-bFwm89cmUKNiXDypkTrs3rUzIBRQbh9UoG3YhXrDt3EuD1V52zcYa2vZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواننده رپ آرمین رابر، برگزار کننده میتینگ های خیابانی رپ در اطراف تهران بازداشت شده است. او پیش تر نیز به دلیل اجرای قطعه آقازاده بازداشت و به حبس و جریمه نقدی محکوم شده بود...
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72145" target="_blank">📅 22:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72144">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تسنیم گرفت رو عراقچی:
تعامل عباس عراقچی، وزیر امور خارجه، با استیو ویتکاف، نماینده آمریکا، بدون مجوز یا هماهنگی با مقامات ذی‌ربط ایرانی، از جمله شورای عالی امنیت ملی، صورت گرفته است.
ادعاهایی مبنی بر اینکه این تعامل از پیش به تأیید نهادهای سیاست‌گذار ایران رسیده بوده، نادرست است.
بر این اساس ضروری است که آقای عراقچی درباره این اقدام غلط که مخالف مصالح و‌ منافع ملی است به نهادهای مربوط و ملت ایران پاسخگو باشد که با چه محاسبه‌ای این خطای بزرگ را مرتکب شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72144" target="_blank">📅 20:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72143">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d86a283f5.mp4?token=hoMFc582Lc5UqUg6oy_zrPi9gEuh4XyynJUeK1zS62dceXX15n60-3FDA2DMpha-An5aTCCuD8NUOoWq8vrYHsnQkesAXCGP3_tWZxlMYgADy-DlcdzQhSQlFzncj-xnr-td7LBjZa0Mahl4dKKZ6G3ArlmwlkKVYQiCWXPCfy3qw6n9GLLe_dY-0u3ItZJVwgO-6aA8d8m98vxesBR7J55kudxX4It11oAotpNnbwKCZk0SNKbuRhYfG-CcR1HuRGXuDkisNy-TcLMCSfA0gw3r1Hee6p82zWbafXN_27gHEXvZo3jETKeTGd4TaWsdCT76foKEByTR4fqHmbJ5bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d86a283f5.mp4?token=hoMFc582Lc5UqUg6oy_zrPi9gEuh4XyynJUeK1zS62dceXX15n60-3FDA2DMpha-An5aTCCuD8NUOoWq8vrYHsnQkesAXCGP3_tWZxlMYgADy-DlcdzQhSQlFzncj-xnr-td7LBjZa0Mahl4dKKZ6G3ArlmwlkKVYQiCWXPCfy3qw6n9GLLe_dY-0u3ItZJVwgO-6aA8d8m98vxesBR7J55kudxX4It11oAotpNnbwKCZk0SNKbuRhYfG-CcR1HuRGXuDkisNy-TcLMCSfA0gw3r1Hee6p82zWbafXN_27gHEXvZo3jETKeTGd4TaWsdCT76foKEByTR4fqHmbJ5bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنتاگون ۶ مورد دیگر از فایل هایی که در آن اشیا پرنده و ناشناس به اصطلاح UFO دیده میشه رو منتشر کرد که دو مورد اولی در خاورمیانه ثبت شده هست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72143" target="_blank">📅 20:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72142">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9819ac349a.mp4?token=LYffGtNxJCH9xFu8xlhBENBVsEKLRy4JOf7L6qLcibbhaeZyzzf-qFC3zq3chfYEMtRkiwDSragm7J-I4TKVo8eiIULgoWv-Pd2cPWH37tlr05Kl1gPhyyY22Kp6w8NUyDmsImGyFEIE9O_BCatPejRtV7jZchOgVhDoR2FQTuDbl87WeZUkgLEGiXWJSJhD36RiZ1Rr3Ttw-JIFZGXrfzEg047NXljArdtX5C40BDuUE5H87glYQVml9SZjgxouddTt4G_sOU0iIGs9-0vXYDc7n1J2nvD0-AZvK1swDsHRUHqN0XO_MfmfYdBrsVsGKzf6nSoYVps1XsXFyqtuNIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9819ac349a.mp4?token=LYffGtNxJCH9xFu8xlhBENBVsEKLRy4JOf7L6qLcibbhaeZyzzf-qFC3zq3chfYEMtRkiwDSragm7J-I4TKVo8eiIULgoWv-Pd2cPWH37tlr05Kl1gPhyyY22Kp6w8NUyDmsImGyFEIE9O_BCatPejRtV7jZchOgVhDoR2FQTuDbl87WeZUkgLEGiXWJSJhD36RiZ1Rr3Ttw-JIFZGXrfzEg047NXljArdtX5C40BDuUE5H87glYQVml9SZjgxouddTt4G_sOU0iIGs9-0vXYDc7n1J2nvD0-AZvK1swDsHRUHqN0XO_MfmfYdBrsVsGKzf6nSoYVps1XsXFyqtuNIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از هموطن‌ها رفته یه مرسدس بنز خریده؛
همه منتظر بودن از خریدش ذوق کنه ولی صحبت‌هایی که بعدش کرد، جالب بود :
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72142" target="_blank">📅 20:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72141">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اگه هنوز دنبال یه کانال و گروهِ «واقعی» برای پیش‌بینی می‌گردی، درست اومدی!
👑
✅
تحلیل‌های اختصاصی و رایگان
✅
ضریب‌های طلایی
✅
گروهِ فعال برای تبادل نظر  وقتت رو با کانال‌های فیک تلف نکن. حرفه‌ای شو و با ما همراه باش.
👇
[لینک کانال] https://t.me/+fyrt-rnxFjNjMmQ0…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72141" target="_blank">📅 20:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72140">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjbGHgNOOP3pCPUzWNZJ219IpfTIwYQQH-QHFNyYRdFAZpRlFs12nawubrqNqZWBLYrBXET7HwyximIB4RrzwORkm0V8U0rRnPvD17K9eMAmjE5OV-FLvnYrlxiz8gPE9IM9xbto_qlJruRDGqG9D9ktMEEwNCeAnLmfCOUE4_zkzpKYPeMr-JnYYfKBFYxB7lAcaA3fF6ruHobMIrTe6oWRwB9Tjl1ncKFTBWuj2lBVPy7MYiKrCbIcDSf9jTgd_rkfvEVqsqb42dpwAKzKcJZ-dokr2ChTGdfRqGlvWVQiHk1DibGmFm7kHJFSec8Q5SOnCsArilw7LYhzkEGTZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه هنوز دنبال یه کانال و گروهِ «واقعی» برای پیش‌بینی می‌گردی، درست اومدی!
👑
✅
تحلیل‌های اختصاصی و رایگان
✅
ضریب‌های طلایی
✅
گروهِ فعال برای تبادل نظر
وقتت رو با کانال‌های فیک تلف نکن. حرفه‌ای شو و با ما همراه باش.
👇
[
لینک کانال]
https://t.me/+fyrt-rnxFjNjMmQ0
[
لینک گروه
]
https://t.me/+jpSLBx8PcgBlMWI0
#TipsterPersian
#سود_تضمینی
#شرط_بندی_فوتبال
»</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72140" target="_blank">📅 20:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72139">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fa977cc40.mp4?token=H0rRRxVG5ndWb_ZYG0UlmxOpcQBUd_BnsD9WupEtx1E2BsDyo0KiyWYpdvtoWs7tRKDbVyrnTyCzjo1tTVxN4aMo5zedgBJPqO3uAB__8CTzM80iuzGbkho6PB0DYdU_Fcp1uhhTMjEvApXxdj5-D54MFyqo9n8AxeaOfOFuBXsi7k_-wztLMcTl-_X0oyagIULvuT1uEVUHqtnshvbAQiYltSeUwi1J0l6pYMsaQj0WYApXGQjhOXwtuloXjj9ID4q_fUf0G7ZHrXluZ8YnVpWTusWImHPEaeQoIICYGrhr6zKhm-2rTFyHmI8MqwuhqZbfe2C3t6fw5oWbQoS2JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fa977cc40.mp4?token=H0rRRxVG5ndWb_ZYG0UlmxOpcQBUd_BnsD9WupEtx1E2BsDyo0KiyWYpdvtoWs7tRKDbVyrnTyCzjo1tTVxN4aMo5zedgBJPqO3uAB__8CTzM80iuzGbkho6PB0DYdU_Fcp1uhhTMjEvApXxdj5-D54MFyqo9n8AxeaOfOFuBXsi7k_-wztLMcTl-_X0oyagIULvuT1uEVUHqtnshvbAQiYltSeUwi1J0l6pYMsaQj0WYApXGQjhOXwtuloXjj9ID4q_fUf0G7ZHrXluZ8YnVpWTusWImHPEaeQoIICYGrhr6zKhm-2rTFyHmI8MqwuhqZbfe2C3t6fw5oWbQoS2JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتظار می‌رود سخنرانی نتانیاهو در سازمان ملل به شدت بر ایران متمرکز باشد و به گفته‌ی ایدز، این سخنرانی حاوی «غافلگیری‌های» نامشخصی خواهد بود.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72139" target="_blank">📅 20:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72138">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پزشکیان:
تو منطقه هیچ کشوری به تنهایی امنیت نخواهد داشت، یا باهم امنیت رو می‌سازیم یا باهم تو ناامنی زندگی می‌کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72138" target="_blank">📅 20:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72137">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15be798879.mp4?token=TgpDA04sahQcKSdeaxJ1GOz-h0vbQJU9O5LStDnzSpRalTK_viUG-AShyKVO8FmydhpRSGjjaNcSuBMwdl0O9QKwQQLQZ8j0OxIlg7cBQTjy06fj111MgWnQp87rSQ4aqCxD1plcahS3QHBlfnKTJULJ17BpxVuCVr2CtiYPkw0uXcZKvFT6738peUyI9pBa91irIaLktW_uhNLUsPZVoXzsWXwwAQbRDWmKV4zA4ugEdfqWjJ_O2ZfxzXsVqS1qpyfE-eDo1WVSSK1X-Bm9pJibuRJBaEVJAeZpJypAD_YHHMwGqBC3LumyaetIiuFAfi1smW9g1DRfwqHQodww1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15be798879.mp4?token=TgpDA04sahQcKSdeaxJ1GOz-h0vbQJU9O5LStDnzSpRalTK_viUG-AShyKVO8FmydhpRSGjjaNcSuBMwdl0O9QKwQQLQZ8j0OxIlg7cBQTjy06fj111MgWnQp87rSQ4aqCxD1plcahS3QHBlfnKTJULJ17BpxVuCVr2CtiYPkw0uXcZKvFT6738peUyI9pBa91irIaLktW_uhNLUsPZVoXzsWXwwAQbRDWmKV4zA4ugEdfqWjJ_O2ZfxzXsVqS1qpyfE-eDo1WVSSK1X-Bm9pJibuRJBaEVJAeZpJypAD_YHHMwGqBC3LumyaetIiuFAfi1smW9g1DRfwqHQodww1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خانم معلم قبل از شروع مدارس، برگشته به اولیای دانش‌آموزا میگه؛
بعضی از دانش‌آموزا هستن که پدر، مادر یا هر دو رو ندارن ؛
پس وقتی میاید بچه‌تون رو از مدرسه بردارید انقد قربون صدقه‌ش نرید که دل اون بچه یتیم بشکنه، برید یه جای خلوت‌تر بهش ابراز محبت کنید
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72137" target="_blank">📅 20:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72136">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bcb578f315.mp4?token=Hz5EVYZ8NhDgAuMuA_B3w89SQOrLoxQLGfmuDTyiB0KMRT9AtDYTUE_7PvtqTNrCCrEtMgBs0uwe6H1o0t7RzTMLelhfcwE_6gWekrtKlWk-ml4jAufpwSLpBgaZv-zKmRsNDxvCbbR2BbkDTKqVEfU0nbtlSP1njprjYNtABt5c6P9YHWmh_BBgrme6nMmM8H_yyrSECOzfvt7n-cCsBwdnCd6TXsRBWQXR6GjmXqlkAc3mkHugogbtqA9CbV8WUuQakhm7tRCaHC3ow-D_cVfSJuVxR8foowejpnVQTAC2nTIXnROXTu0LAA42cms6KDdOgFAA1ywSApT36GjbgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bcb578f315.mp4?token=Hz5EVYZ8NhDgAuMuA_B3w89SQOrLoxQLGfmuDTyiB0KMRT9AtDYTUE_7PvtqTNrCCrEtMgBs0uwe6H1o0t7RzTMLelhfcwE_6gWekrtKlWk-ml4jAufpwSLpBgaZv-zKmRsNDxvCbbR2BbkDTKqVEfU0nbtlSP1njprjYNtABt5c6P9YHWmh_BBgrme6nMmM8H_yyrSECOzfvt7n-cCsBwdnCd6TXsRBWQXR6GjmXqlkAc3mkHugogbtqA9CbV8WUuQakhm7tRCaHC3ow-D_cVfSJuVxR8foowejpnVQTAC2nTIXnROXTu0LAA42cms6KDdOgFAA1ywSApT36GjbgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه زنه با شوهرش رفته بود خرید که شوهرش این حرکتو زد و آبرو برای زنش نذاشت :))
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72136" target="_blank">📅 19:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72135">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff0aa24390.mp4?token=kYjqYW4iGaKT2gSWiX-_Z07vntpo8MEsjsiXD4VzyOJHjX9lcE9DlH6fTtkbPkTxXei-wAZ-hOCDsRYHZq-TtuFwysR2UM_wjwZQziGz4zr_Acqc99pxDthzNyvR15v6ceD81CpjHPhDKBHg-h_wzFTlJB7VY7oGCbfCf3XyzyLkLxZO-9EQwD89YK9XDJHI5nmYJKY7LTlJj1cfPQeGmB0JqggZMsGnxkr5eB_ZSS7_Q0h0oZLhedbosfbke5nUG4caEC6EXx1xwp9nk0xGJAKKIv25uzmNpOsHtryT9CeiiiYknxZUYlfB8PUnlda3BgmMvuOhtXtynGChz5Ns9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff0aa24390.mp4?token=kYjqYW4iGaKT2gSWiX-_Z07vntpo8MEsjsiXD4VzyOJHjX9lcE9DlH6fTtkbPkTxXei-wAZ-hOCDsRYHZq-TtuFwysR2UM_wjwZQziGz4zr_Acqc99pxDthzNyvR15v6ceD81CpjHPhDKBHg-h_wzFTlJB7VY7oGCbfCf3XyzyLkLxZO-9EQwD89YK9XDJHI5nmYJKY7LTlJj1cfPQeGmB0JqggZMsGnxkr5eB_ZSS7_Q0h0oZLhedbosfbke5nUG4caEC6EXx1xwp9nk0xGJAKKIv25uzmNpOsHtryT9CeiiiYknxZUYlfB8PUnlda3BgmMvuOhtXtynGChz5Ns9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
آقای ترامپ و کسانی که به دنبال زورگویی به ما هستند، باید ایران را بشناسند:
اینکه ما آماده گفتگو، دیپلماسی و مذاکره هستیم، اما زبان زور را نمی‌پذیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72135" target="_blank">📅 18:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72134">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80dd97167.mp4?token=J4SEq7PbLv00nUiJStYQO_SwSbkrX0_Myzcj_pwucRBQyF24rdY_7qUY6ywvI_uyx2tI8IBloUoFkLjqQgnS7YOhZDi2lGdD3bBpkBBNxM4fHVY5PBnqJCnL2f6GIAWBWMLGdVI971KGbiB_k7kP-uH_yHSNv5AhMI7k72Ct1tKOwjIdyrqU-h-Q5pdqSaHgswdfqwSXYXtiUPJQs76w7xNyinXsabLcPtYtKaSVV_zULWzUj0ivw9e3kks-w_qJ1zsDAyoLJfE088qmE5NIzTOYE3oupw4bEPeEqCXiIgLjIOLQRPET2row-eXeCRQgYzaITI0n3oFM8dp0TzHvgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80dd97167.mp4?token=J4SEq7PbLv00nUiJStYQO_SwSbkrX0_Myzcj_pwucRBQyF24rdY_7qUY6ywvI_uyx2tI8IBloUoFkLjqQgnS7YOhZDi2lGdD3bBpkBBNxM4fHVY5PBnqJCnL2f6GIAWBWMLGdVI971KGbiB_k7kP-uH_yHSNv5AhMI7k72Ct1tKOwjIdyrqU-h-Q5pdqSaHgswdfqwSXYXtiUPJQs76w7xNyinXsabLcPtYtKaSVV_zULWzUj0ivw9e3kks-w_qJ1zsDAyoLJfE088qmE5NIzTOYE3oupw4bEPeEqCXiIgLjIOLQRPET2row-eXeCRQgYzaITI0n3oFM8dp0TzHvgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ترامپ باید بداند که مقاومت ملت ایران در برابر تحریم‌ها، افزایش فشارها و زورگویی‌ها، تنها بیشتر خواهد شد.
ما هرگز سر فرود نخواهیم آورد و زانو نخواهیم زد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72134" target="_blank">📅 18:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72133">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مسعود پزشکیان:
بمب‌های اتمی و هسته‌ای در اختیار رژیم اسرائیل است، اما از بازرسان خواسته می‌شود که به ایران بیایند.
اسرائیل بیش از ۷۰ هزار انسان بی‌گناه را در غزه به شکلی وحشیانه به قتل رسانده است، اما ایران در حالی که پای میز مذاکره بود، هدف بمباران قرار گرفت.
اسرائیل بمب و سلاح‌های کشتار جمعی در اختیار دارد، عضو «پیمان منع گسترش سلاح‌های هسته‌ای» (NPT) نیست و در طول حیات ننگین خود حتی اجازه یک مورد بازرسی را هم نداده است؛ با این حال، همه امکانات لازم در اختیارش قرار می‌گیرد تا بتواند هر پایتختی در منطقه را که بخواهد، بمباران کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72133" target="_blank">📅 18:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72132">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7f87b6f9.mp4?token=S4tkg25_hqH7qHwRRN3yrfNjtkbs5PfbM4GhLAVfQEYdak4yksJXrFsmkw0COpT83i8YkIkDbXux_ar6Wn4xlf86Ozz8mq1gZtYxGpcWHJ2epbfQbww62UNTfpcQ-k-GIyiyPsLTsr-WltoIIJcUzjpq-sm-_aG0OPHAadnyXQqEeBgmpkEH5VUEgZLJm2MlKtgJAPwvInTMPuhKNQ0fwwVWZOnbJKEmS7cA_wxrGw1Q1e8thl2BkSDfqqz8M1L5IRFvMZCLIPht6lDXmj-2zlWyeEwXkNIjGNT3DYuKOJ2VKOd3vabf6anA6RJOkWcPZ6dEX9arYrQ1xTFU7lcMioWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7f87b6f9.mp4?token=S4tkg25_hqH7qHwRRN3yrfNjtkbs5PfbM4GhLAVfQEYdak4yksJXrFsmkw0COpT83i8YkIkDbXux_ar6Wn4xlf86Ozz8mq1gZtYxGpcWHJ2epbfQbww62UNTfpcQ-k-GIyiyPsLTsr-WltoIIJcUzjpq-sm-_aG0OPHAadnyXQqEeBgmpkEH5VUEgZLJm2MlKtgJAPwvInTMPuhKNQ0fwwVWZOnbJKEmS7cA_wxrGw1Q1e8thl2BkSDfqqz8M1L5IRFvMZCLIPht6lDXmj-2zlWyeEwXkNIjGNT3DYuKOJ2VKOd3vabf6anA6RJOkWcPZ6dEX9arYrQ1xTFU7lcMioWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
مسائل منطقه‌ای ما باید در درون منطقه و به دست کشورهای منطقه حل‌وفصل شود، بدون آنکه به ابزاری در دست متجاوزان خارجی بدل گردد.
هیچ‌گونه رابطه‌ای با یک قدرت خارجی نباید به ابزاری برای تهدید کشورهای همسایه در منطقه تبدیل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72132" target="_blank">📅 18:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72131">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4be5f428e4.mp4?token=bn2BG0BUrPNkiQW9QKPhP-yBrAe_k4ViecPuDqyd2fNBM-TEq2c2oFUqs0ukNKmrP70hogGMPjf2SG5bi9Jj7z-FeT7_jXBlAdztJx4i_sCmt14vHL8q4GMqlrv0hArsqkT8L-p8t2WDuzWPrBgjJjuXfADZQeZ0VNPMELi6x8rPfEPmDvRBGSeBxAcAmJpJrDxBeuIno4MKTjIOmiomnDIRqu1BwrWCYQQtTN88tUhn1cvJvmNZv-XrSfrHXYapJcT0d-Bl67M_VF1z9gOqp65wNKCkEPN3LWDzgGE5vUNQXuKNGv6MHx8fWqdKql54IRuMibcfSrdp9BuCYt5oWxXZWbZ5OSsj0mZ9wTAxrcr-p6CuYFSuC5ZNYknQNJqsWCVjpsTMQGOfYRokaB_zat5_pHvnjuC32jSfckAF5gDOH8c_AwZPcsVNIdmWfdC-1IpOckIgdTQIgkRh0IlCft1fK0heQNfVPSdURbc-lfAcRCKzCDa6949ehsFSQQ2MmH2K8Kd69wt1dq-zBeT5krOBhuraMSL3ia6vLdevI062ih1zLvTBXEUnFL2F22qTRJmSHLFK4722aKEpuAldW4cEQD3i3BxjYu5k0fl8M6RYVzX-ouH0pbRTEk67iyldhWfaD5qoqtQOxH9Y7Gvy5buhDlcRH_V4SiWEQ0A4qbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4be5f428e4.mp4?token=bn2BG0BUrPNkiQW9QKPhP-yBrAe_k4ViecPuDqyd2fNBM-TEq2c2oFUqs0ukNKmrP70hogGMPjf2SG5bi9Jj7z-FeT7_jXBlAdztJx4i_sCmt14vHL8q4GMqlrv0hArsqkT8L-p8t2WDuzWPrBgjJjuXfADZQeZ0VNPMELi6x8rPfEPmDvRBGSeBxAcAmJpJrDxBeuIno4MKTjIOmiomnDIRqu1BwrWCYQQtTN88tUhn1cvJvmNZv-XrSfrHXYapJcT0d-Bl67M_VF1z9gOqp65wNKCkEPN3LWDzgGE5vUNQXuKNGv6MHx8fWqdKql54IRuMibcfSrdp9BuCYt5oWxXZWbZ5OSsj0mZ9wTAxrcr-p6CuYFSuC5ZNYknQNJqsWCVjpsTMQGOfYRokaB_zat5_pHvnjuC32jSfckAF5gDOH8c_AwZPcsVNIdmWfdC-1IpOckIgdTQIgkRh0IlCft1fK0heQNfVPSdURbc-lfAcRCKzCDa6949ehsFSQQ2MmH2K8Kd69wt1dq-zBeT5krOBhuraMSL3ia6vLdevI062ih1zLvTBXEUnFL2F22qTRJmSHLFK4722aKEpuAldW4cEQD3i3BxjYu5k0fl8M6RYVzX-ouH0pbRTEk67iyldhWfaD5qoqtQOxH9Y7Gvy5buhDlcRH_V4SiWEQ0A4qbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
ما سر خم نخواهیم کرد و از حقی که ذاتاً متعلق به ماست، دست نخواهیم کشید.
صریح می‌گوییم: نه سلاح هسته‌ای و نه هیچ‌گونه محدودیتی برای فناوری صلح‌آمیز هسته‌ای.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72131" target="_blank">📅 17:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72130">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2213909800.mp4?token=aspeWefB3P5X-aOThgkuWQbshzBruXHl3Fr5PyWbQDskPJakysnYzPWjkRNc444--yyJpCUcrTto_OgKq6auK7kCyEmVqsl9nQm_p4BRsfwbHuU8c0xYTi9k66dmvUI3QV-UHvewaCFmS8XYzyBrIB01e055hsmRazRTIL3ynzDsziomgA5P8FJManoTxF3GodY7UWk0Am24l6Cx_4qEF2fcq3TOV3j1bnfzwpyU-oOxhauXxosVMzou7EsnUTLv1mkt_T58gXnMdJeGGc1n6yPqUAVjABEiDCw_GNTDd4AWMrWyOKlYK46bH8VhyiZtSg2wuTKsCUqpXvaDQnh80YslDMnIPrOrHNEvRNgQ8lJ4KkEy67ofZPTivc7hRl_GPz_ZAINN2xY-06CdkP3PSy9V4TW91Naep9mYclOVxelsvhTwxtyEpwwCSamFmRPxmkCIH9G4XxZE-rA-iwry9zanagGoFZnbSmHB0v1sUNEYhJgG7LeIAhZEHnMAneZ9g26h_Is2pwDYHb1jQl9PgSQkAoTQtPLs8x56FHy3RKpg6d4UK98P0R8kRb2Dlv_rdbKESKzJp05aNoM0vwFJLS8eQD0Ir0hbWgbuPC41hiL-QRKvjJFFQZWH5_9jnLtb-apZzEtp0FeV4qpoA1xtgSnhMtmDlxWAYToi1lurXEM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2213909800.mp4?token=aspeWefB3P5X-aOThgkuWQbshzBruXHl3Fr5PyWbQDskPJakysnYzPWjkRNc444--yyJpCUcrTto_OgKq6auK7kCyEmVqsl9nQm_p4BRsfwbHuU8c0xYTi9k66dmvUI3QV-UHvewaCFmS8XYzyBrIB01e055hsmRazRTIL3ynzDsziomgA5P8FJManoTxF3GodY7UWk0Am24l6Cx_4qEF2fcq3TOV3j1bnfzwpyU-oOxhauXxosVMzou7EsnUTLv1mkt_T58gXnMdJeGGc1n6yPqUAVjABEiDCw_GNTDd4AWMrWyOKlYK46bH8VhyiZtSg2wuTKsCUqpXvaDQnh80YslDMnIPrOrHNEvRNgQ8lJ4KkEy67ofZPTivc7hRl_GPz_ZAINN2xY-06CdkP3PSy9V4TW91Naep9mYclOVxelsvhTwxtyEpwwCSamFmRPxmkCIH9G4XxZE-rA-iwry9zanagGoFZnbSmHB0v1sUNEYhJgG7LeIAhZEHnMAneZ9g26h_Is2pwDYHb1jQl9PgSQkAoTQtPLs8x56FHy3RKpg6d4UK98P0R8kRb2Dlv_rdbKESKzJp05aNoM0vwFJLS8eQD0Ir0hbWgbuPC41hiL-QRKvjJFFQZWH5_9jnLtb-apZzEtp0FeV4qpoA1xtgSnhMtmDlxWAYToi1lurXEM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ایران در دو قرن گذشته به هیچ کشور یا سرزمینی حمله نکرده، اما همواره با صلابت از خود دفاع کرده است.
با این حال، اکنون ما به ایجاد بی‌ثباتی در منطقه متهم می‌شویم و برچسب تروریست به ما می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72130" target="_blank">📅 17:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72129">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مسعود پزشکیان:
کسانی که خود تروریست هستند و تروریست‌ها را آموزش داده و از آن‌ها حمایت می‌کنند، ما را تروریست می‌خوانند. ما تنها از خود دفاع کرده‌ایم؛ ما تروریست نیستیم.
مردم بی‌گناه ما هدف حملات بزدلانه‌ای قرار گرفتند که بر کشورمان تحمیل شد. ما با نهایت قدرت از خود دفاع کردیم.
آمریکا و اسرائیل با پیشرفته‌ترین فناوری‌ها به ما حمله کردند. آن‌ها به ما ضربه زدند، اما ما سر تسلیم فرود نیاوردیم
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72129" target="_blank">📅 17:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72128">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baa7d4e9f3.mp4?token=H_e14HQRyA96Fw55oOJLI5ddWZgdRloUAyDiRH8Kp0j20mmypt81E3w3ZrCnVU2W5nWMpCyB4VK97I_A9YqfaDiMISUX-A5-XO8VM4dEfaPENU8p70g1WlAyI8aBLz2t72leDA6jvKIyk0Gv9OA51agl7Lr6zwLrwLpNaNWKYnFu8_vEfh1JgRpggqPNaqmybLsRgrysdeJLSQgUZn0gf2EfhkQrCm93hfE7RSZcbLNohdNkYwQ_YnczdUviVxi9loX6qNtUbldj72rSixOm1SyTkFYBhC2s7V_a0icwsmnZWjnlD6_OzG_vA0b6ozDIeTbSspjn_rUhNQokGe2CZjjOSin6lEuKVLFzV5uI-HYWGz4A0BR3Y1Y6Ld3t4t2v2kTIjWrd-TMJMIu_QXXJDDYPLldeyZ99l-ekePeuw-4cQ5bxWpOAhM-LTv4ZywEwPWKubdhfHVZu86yYMXiLboIJZvFjWziuKszeijRpGO8a_ZgseYtmvFXDG-tT8-xv4XXv4-9M-UJqcMYAQHJCSFfThB07ULwHqXlaA_yFQwZ5nILfdFs3t4x2HpBh5g6POR7cv523sXp5dshyHvcwBWxSOoWqsZpg8B4IccfBwIEYXT1JCEkVU6awD8Xfi5yFCHNzgx1k6uS_Ed87L19FK6GofxMaZ9KL_TYQa5UZIHU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baa7d4e9f3.mp4?token=H_e14HQRyA96Fw55oOJLI5ddWZgdRloUAyDiRH8Kp0j20mmypt81E3w3ZrCnVU2W5nWMpCyB4VK97I_A9YqfaDiMISUX-A5-XO8VM4dEfaPENU8p70g1WlAyI8aBLz2t72leDA6jvKIyk0Gv9OA51agl7Lr6zwLrwLpNaNWKYnFu8_vEfh1JgRpggqPNaqmybLsRgrysdeJLSQgUZn0gf2EfhkQrCm93hfE7RSZcbLNohdNkYwQ_YnczdUviVxi9loX6qNtUbldj72rSixOm1SyTkFYBhC2s7V_a0icwsmnZWjnlD6_OzG_vA0b6ozDIeTbSspjn_rUhNQokGe2CZjjOSin6lEuKVLFzV5uI-HYWGz4A0BR3Y1Y6Ld3t4t2v2kTIjWrd-TMJMIu_QXXJDDYPLldeyZ99l-ekePeuw-4cQ5bxWpOAhM-LTv4ZywEwPWKubdhfHVZu86yYMXiLboIJZvFjWziuKszeijRpGO8a_ZgseYtmvFXDG-tT8-xv4XXv4-9M-UJqcMYAQHJCSFfThB07ULwHqXlaA_yFQwZ5nILfdFs3t4x2HpBh5g6POR7cv523sXp5dshyHvcwBWxSOoWqsZpg8B4IccfBwIEYXT1JCEkVU6awD8Xfi5yFCHNzgx1k6uS_Ed87L19FK6GofxMaZ9KL_TYQa5UZIHU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
مردم بی‌گناه ما هدف حملات بزدلانه‌ای قرار گرفتند که بر کشورمان تحمیل شد. ما با تمام توان از خود دفاع کردیم.
آمریکا و اسرائیل با پیشرفته‌ترین فناوری‌ها به ما حمله کردند. آن‌ها به ما ضربه زدند، اما ما سر تسلیم فرود نیاوردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72128" target="_blank">📅 17:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72127">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مسعود پزشکیان:
دیروز ترامپ ما را تروریست خواند؛ در حالی که ما خود قربانی تروریسم بوده‌ایم.
من از ایرانی می‌آیم که در آن، رهبر عالی‌قدر ما بدون هیچ‌گونه مبنای قانونی یا دلیلی ترور شد.
من از ایرانی می‌آیم که در آن، مدرسه‌ای بمباران شد. این کودکان را می‌بینید؟ این کودکان بر اثر بمباران با تسلیحاتی که توسط آمریکا و اسرائیل به کار گرفته شده بود، جان باختند.
آن‌ها بی‌گناه بودند و هیچ جرمی مرتکب نشده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72127" target="_blank">📅 17:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72126">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aca1a8c79.mp4?token=YVutbI2gDJNNLI0acDkphDFBimg_lgH0wxcSu8tb00h3bL8e-vAt0svAg4cmDgSnz_Hj5aSilQY2bZJZq2FCkEBA6lUwdfT1Ld08vBieV-gyXC3ORagEGwsigCmTpV6wVvPk7Kqtn4z8vP1DI8ergy3T9W-E_UKkvaFBZINGzJNbh8mK6DFd9SYql7HDDvFIE4wUwZknRyPUEugXblM_a1yhuxhcyqUIpcweHe8BQNx61xdDER1zytqATsqzqQiiFc8ZwlzNjcCfWBISzaq78DPHFcMEk9ZzhBBL4KLak4OQIDG9xnYK4WPyWbWsskTeWZjzA-ekwhDysko6ut-OqZX5jLNB4i9fl45A3aIe1YlE-Sa_1hGXhkZ1J3w6RWxWs3n56z8h74GUum-0t-fBAl-qiq2YDO81A_VXulAcER2UfZ7rNvBCm7o7b-BOMsxNTQz3AY5WuzXCp0MZjYucw8k42XUREDLJ90iRK9LvGpCjDYTPdANW2f7GJCWVOjIOpACmkpnDMKkAdDeSNk0wFy7BvOfnEJn1XQwvhllyGRAdIivLd-1MjQDEicry3tlA6-wB0BT8tfhvH5bNHJZ93dJqk3pF-9Y09NaAIlaOfA62EwTPQdlK53-jtrLV_gpO8klsec48tcQ9UlpQp0oANeNO-nk-4M5NJQ4rTeT_Ms8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aca1a8c79.mp4?token=YVutbI2gDJNNLI0acDkphDFBimg_lgH0wxcSu8tb00h3bL8e-vAt0svAg4cmDgSnz_Hj5aSilQY2bZJZq2FCkEBA6lUwdfT1Ld08vBieV-gyXC3ORagEGwsigCmTpV6wVvPk7Kqtn4z8vP1DI8ergy3T9W-E_UKkvaFBZINGzJNbh8mK6DFd9SYql7HDDvFIE4wUwZknRyPUEugXblM_a1yhuxhcyqUIpcweHe8BQNx61xdDER1zytqATsqzqQiiFc8ZwlzNjcCfWBISzaq78DPHFcMEk9ZzhBBL4KLak4OQIDG9xnYK4WPyWbWsskTeWZjzA-ekwhDysko6ut-OqZX5jLNB4i9fl45A3aIe1YlE-Sa_1hGXhkZ1J3w6RWxWs3n56z8h74GUum-0t-fBAl-qiq2YDO81A_VXulAcER2UfZ7rNvBCm7o7b-BOMsxNTQz3AY5WuzXCp0MZjYucw8k42XUREDLJ90iRK9LvGpCjDYTPdANW2f7GJCWVOjIOpACmkpnDMKkAdDeSNk0wFy7BvOfnEJn1XQwvhllyGRAdIivLd-1MjQDEicry3tlA6-wB0BT8tfhvH5bNHJZ93dJqk3pF-9Y09NaAIlaOfA62EwTPQdlK53-jtrLV_gpO8klsec48tcQ9UlpQp0oANeNO-nk-4M5NJQ4rTeT_Ms8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت نمایندگی ایالات متحده هم‌زمان با سخنرانی رئیس‌جمهور ایران، پزشکیان، صحن مجمع عمومی سازمان ملل را ترک می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72126" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72125">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72125" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72125" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72124">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fx2DYuWlqMuAQtCBeOubxFEWpeJtZSbOs8iQP0QUEHyliHPeHVppX4sbCREJcGgB70V4e24J7fk8u1TAjDAWgNnxA-PSlVIdjjzvVhRZZYFdQ2gb6MNLKkx-XTnWG_sjrHIYZNqh1wMoxxZCdIcvtqHYPFTmTi_NBHUxIZSteeEOgRwxU2f4TXCwxcZqKgJeZbPpA5tcFKDUkbj57wezjusl-ofcs4jETgOwh1hbV7e3gea4JOugxwpyRTzd8HoXw-QiNhmp6KVjDcrr8xz6U3FaavYt6A1vPYlYVzHW4G5eX_lyd2s_qZSrpv_C1CLOQmE5Tq9ROIGXnTph6deQtg.jpg" alt="photo" loading="lazy"/></div>
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
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72124" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72123">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4142dc5d8.mp4?token=AUzWO-MHNxPB85zpxkaHLWuf9cfPne_1bBexUu2ZcB-QYnJMc-ecXmNPzpMPpQYb7VLX9WkfxulC71_3IpSE6nkwRNPneQlU61vhrt3ZA8X0Ue7u8FYcEiIxCDhUEiEoMXyq2Z0XM88u9AkCNEPfXlxkDtO_dxOOm9oCw3G1ZmCQXmtbv-paT6DZkIlpukZEX7FqNFcKjHLJQg3CkkPytveoAoeKjpWotpD6YWXASpJuGoq7HfgyM_Ap_VMl5Du9_I42zDyxYe7LQ53L9PNqAPv8Zjnm1szDAS7QqMJl7x58910gjB7ABiudQ0Z8GxWU-MzQDHInTluzd0FLuJgpjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4142dc5d8.mp4?token=AUzWO-MHNxPB85zpxkaHLWuf9cfPne_1bBexUu2ZcB-QYnJMc-ecXmNPzpMPpQYb7VLX9WkfxulC71_3IpSE6nkwRNPneQlU61vhrt3ZA8X0Ue7u8FYcEiIxCDhUEiEoMXyq2Z0XM88u9AkCNEPfXlxkDtO_dxOOm9oCw3G1ZmCQXmtbv-paT6DZkIlpukZEX7FqNFcKjHLJQg3CkkPytveoAoeKjpWotpD6YWXASpJuGoq7HfgyM_Ap_VMl5Du9_I42zDyxYe7LQ53L9PNqAPv8Zjnm1szDAS7QqMJl7x58910gjB7ABiudQ0Z8GxWU-MzQDHInTluzd0FLuJgpjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیمت کوکائین در تهران چند؟
پلیس مواد مخدر تهران بزرگ ، یک بار بزرگ کوکایین کلمبیایی را قبل از پخش در پایتخت ، کشف کرد .
این کوکایین ها بیش از ۵۵۰ میلیارد تومان ارزش گذاری شده است.
گویا داداشی ها سهم  مامورا رو ندادن اونا هم بار رو لو دادن
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72123" target="_blank">📅 17:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72122">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dadfb7a92.mp4?token=UcPI3jZfGo6jFbL2KJqjw--VGGxuwr8m1cASShNIOaLzfqjG_fufrDE_3idlHjOwjQFcxZwV6QvvzJ9JbV8ARlqJaFukf5O2-DDk-TZLGxqWiftMM6rUEQldp6QQOtfW4oquZ_otv14AB9ZXhhPIaOJge0_q-tl8vNmP1NFNRY8clNHBWK-cOp3uqJfArOqFJxWUauvFC7MsXfHgDxWpevGIt2fBa3Xi540f1sIPdcfrKnxtaDFVFlLwhpNXFcJPpDNihIeoGwdqQnexrHT6gutjNe7Yprs3KaCc0C_r3vFSuVrcFKo8Uf6nKDl9TwoZOZADEGYaTY_zqHMHNMta4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dadfb7a92.mp4?token=UcPI3jZfGo6jFbL2KJqjw--VGGxuwr8m1cASShNIOaLzfqjG_fufrDE_3idlHjOwjQFcxZwV6QvvzJ9JbV8ARlqJaFukf5O2-DDk-TZLGxqWiftMM6rUEQldp6QQOtfW4oquZ_otv14AB9ZXhhPIaOJge0_q-tl8vNmP1NFNRY8clNHBWK-cOp3uqJfArOqFJxWUauvFC7MsXfHgDxWpevGIt2fBa3Xi540f1sIPdcfrKnxtaDFVFlLwhpNXFcJPpDNihIeoGwdqQnexrHT6gutjNe7Yprs3KaCc0C_r3vFSuVrcFKo8Uf6nKDl9TwoZOZADEGYaTY_zqHMHNMta4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مادر توی کمد لباسای دخترش، کاستوم مخصوص سکس پیدا کرده، بعد دختره هم به این شکل مامانشو قانع کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72122" target="_blank">📅 17:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72121">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbrMcJTMWIPhl2hM2dWs-HcouQjV2v10ldKvxaXBuYZv6JBsdo4P-cSPgZd87pea4JyORG7toS8rtlBlSxI5Yyyf1SoVoBNgBP3dYBQyTjrhfdAKnuodBlRwaRqscwZKrX8oqc1z31kmM4VaIjwhUMqU4rL0S8U9ANEjSY_LoKE2afD3sc1hhrBJiNRMKAGAyDC0EipLhKOBbu5GXHMZrCX3ltuCyxFKYRLT-H4JnCtCtiYCOjFXklzBxvul73TmazfNi9ein6SRQ2mBs_RALv1JnY8dDeYXjIgRvKNFIkQxh7zuDgcG_zMUKKVcwOPjRSqhk9FCnLEOJzx2woH6hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که یک کشتی باری در تنگه هرمز هدف اصابت پرتابه‌ای ناشناس قرار گرفته است.
این کشتی دچار آتش‌سوزی شده و بر روی آب سرگردان است. خدمه کشتی تخلیه شده‌اند و گزارش‌هایی از دو مورد تلفات منتشر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72121" target="_blank">📅 16:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72119">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/056cf75693.mp4?token=tgX4WU_Zpm8NaC7dzTDqm9lZWziFR13F4Hn_x9yOILX3Nj-vwN86-4d7QLxa2eTBdQPWMm8FmYcLd5FmAfSgfZQKB2NrPeC7tuVqBh2skhYyUry2Z-tOkpYOSDZCVvH1Nunk9fCdliRbZxbEiMSmq5tgb1tJEGD4C7GuNHFFDTQXUxD0hqhrCyHgPEZvilxkHd2zGb_Tov5zmUQ40iinkRZnTV7ZfQFiPp810I2-rEeZ7RmPk1yjCkbxchYzSwJ4XLO2BZnNEVpfPYxhqp32ieFAgb1Jo5s3RoEoWCMIfNIT008LFhBDQqkj29sGClJ4hueXup_9jPDeCob48if1Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/056cf75693.mp4?token=tgX4WU_Zpm8NaC7dzTDqm9lZWziFR13F4Hn_x9yOILX3Nj-vwN86-4d7QLxa2eTBdQPWMm8FmYcLd5FmAfSgfZQKB2NrPeC7tuVqBh2skhYyUry2Z-tOkpYOSDZCVvH1Nunk9fCdliRbZxbEiMSmq5tgb1tJEGD4C7GuNHFFDTQXUxD0hqhrCyHgPEZvilxkHd2zGb_Tov5zmUQ40iinkRZnTV7ZfQFiPp810I2-rEeZ7RmPk1yjCkbxchYzSwJ4XLO2BZnNEVpfPYxhqp32ieFAgb1Jo5s3RoEoWCMIfNIT008LFhBDQqkj29sGClJ4hueXup_9jPDeCob48if1Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانیال عیوضی، مجروح کشتار کرج، پس از ماه‌ها تحمل درد و جراحات، در دی‌ماه ۱۴۰۴ ترکیه را به مقصد اروپا ترک کرد و امروز خود را به سازمان ملل رساند تا درباره مشاهداتش از کشتار و برخورد مأموران امنیتی جمهوری اسلامی شهادت دهد.
هیئت ایرانی تلاش کرد سخنان او را مغرضانه و تند جلوه دهد و مانع ادامه صحبت‌هایش شود؛ اما با دستور رئیس جلسه، عیوضی به سخنان خود ادامه داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72119" target="_blank">📅 15:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72118">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b96e8038a0.mp4?token=nFoXtfaocSZusUH5tUKJOUUXhK-kPdaAANdNgXN4FMh4KngUYm7y129EQdN7OKkDtzKu7AZyHHL6JFDm8HQ7asA6pzNqOnitbvC928G51YXRFtI-vfI8vWx5Ch4D6gTmI_Mfolf26HM_jYLwX4nWzN3VG0jTsFABNPQehgMNkvAYHiexXSCm-R9U8MLbRuUH0vPXb4KARlxQR4w_gnpmHhXgG1llCw1n8YEpL65cPArSCjUBzMU0jo6fnyluNVIXRrzfeLIqum-8I8jJCo339czbF-6dGFjSQLf5zra-bM3Ov7DP0jURYFcMRYngVgh-8BhLJB0TOqDwAHYhFtBffA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b96e8038a0.mp4?token=nFoXtfaocSZusUH5tUKJOUUXhK-kPdaAANdNgXN4FMh4KngUYm7y129EQdN7OKkDtzKu7AZyHHL6JFDm8HQ7asA6pzNqOnitbvC928G51YXRFtI-vfI8vWx5Ch4D6gTmI_Mfolf26HM_jYLwX4nWzN3VG0jTsFABNPQehgMNkvAYHiexXSCm-R9U8MLbRuUH0vPXb4KARlxQR4w_gnpmHhXgG1llCw1n8YEpL65cPArSCjUBzMU0jo6fnyluNVIXRrzfeLIqum-8I8jJCo339czbF-6dGFjSQLf5zra-bM3Ov7DP0jURYFcMRYngVgh-8BhLJB0TOqDwAHYhFtBffA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقرار پدافند هوایی روسیه وسط بزرگراه رو دریابید
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72118" target="_blank">📅 15:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72115">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fnWBrduQJJclkU9cEz3SC-9YvmgF8F1sX3u4Tfy1R8qCI7kBKC7r12zIrX9BM9wYiNx5xuEmoOhe2x742LvmIfRTYR1ADy-JJsTAWdXbLcjeOXHdgbpvorzreBLmbLAeY75_okVnx8nw4xgsM2zsP-B8YFGdos33orMWrlDZHu6_7pIXTLhKkhxr9sHTGS0_RBoUqtqs8clKpDHnObYFyoYlnShgvwCIJtGTs7MDC2QUOQZITdnfsDKuF96Zoh-zGbtUsiKs74LuYBV1VSkV2JjYJ9yTWXcomOQ81zKmx9T0xgR2IhDaGiUQp2jg-WL4PmGmuEtSF-pM_PEMGcLiag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dz3W6A-ZTCqQkmSU2Z24fOwdFy2Ho7Ywy3CXCYked3tKUVJeCxjC5fqeb9ugEdzihlFpjYDTvnC4G3qA2G3JIR83Oiol_wkWn3KlfwVl-6-n0L9WbWoY01wY5aayuzR1a3JnvDSfR1Hd4fSmuhaMYyHMokyhfppCHr5y8krqzfNq6rhy7kzj905nSUccDIbkZDWcl8nA0B7o2G-IfhgMtHgihWqn8QbmuecjYnv0ZzuPaOxNN-fUIJ0zVBNshHLhuWdYsFnba0RKmj4EF8uvGCrch11wjWDp3jJmG4iYHyUQ0ARvWF9WtMCpmWn3e0_V19D7Ed8N4dPdWocrhOLsyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ryL7UTjG-W6cL-zpiMV3KHOlzG-CN6m4o2aOYSkOSPWNtRBKLREsy4A9vb8esoiiBKgsTTWJDdltWAgxUpwGQ_7h6kdMrE9ZQJ1Mzu6m5ecw53inwPFGhBGK-RK8ExNO_jT-2tC-RwD3k3L-JCiTXNyyTOTRxkaYSGpdpFtZqdEOoKKkgeXt4iv9YrFwWmbx5evUlM2n43dDQKI1q_Yc871sN2AZ4eoiLuQq-0s8FBkLcrjnxvZ5bTE8kI1_HmUtxglSktrmAFNb7ohuX1qcbjvIt850BU3mFW5QtSLRKogXG5wOu9Mk-2jTLY7fPcJHR74ITA5tn4RFVZkDEmYGQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این بیلی آیلیش هم روز به روز داره خوشگل تر و جذاب تر میشه هرشاتی از خودش منتشر می‌کنه کلی لایک میگیره :)
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72115" target="_blank">📅 15:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72114">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تحریم‌های جدید آمریکا علیه بخش هوانوردی ایران، چندین کشور را بر آن داشته است تا پروازهای ایران را محدود کنند.
محدودیت‌های تأیید/گزارش‌شده:
🇬🇪
گرجستان — ممنوعیت کلیه پروازهای ایران از ۲۱ سپتامبر.
🇦🇿
آذربایجان — ممنوعیت فعالیت شرکت‌های هواپیمایی ایرانی از ۲۲ سپتامبر.
🇮🇶
عراق — تعلیق پروازهای ایران به بغداد؛ احتمال تغییر مسیر برخی پروازها به نجف.
🇴🇲
عمان — توقف پروازهای ایران به مسقط.
🇶🇦
قطر — گزارش‌هایی مبنی بر تعلیق پروازها از مبدأ ایران.
🇹🇷
ترکیه — اعمال محدودیت‌های عمده.
برخی مسیرها همچنان فعال هستند:
🇨🇳
چین
🇦🇲
ارمنستان
🇦🇪
دبی/امارات
🇮🇶
نجف
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72114" target="_blank">📅 14:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72113">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOqRVXWBUnhDIBRVdkTNXks57I47wEIUaoYgLBBXopjCGUUrROY9chsxy7de9YJHigC1-QLVFGemLpmnAK9yR6bwmC9RD8gRdAvkdBM_BXjhSm-k0sO8RcAtBx1JJZShRClDoQL__TLcmugRa39dzemEv78w4V92JP8pgyc8hk7CrQhxSjcajr5nyw8XNYTpJATu144WYVFZCv3GUtq6FXTBGV9vcDvxWll6jNOo2B4_hY7UFmQkNykDZKcIclOslmGCfpQmQ-H8t1bytXmiw7DNcNCSsLMeKGBeGTjMZUHiRtI2277EdmBcA1YD2mxqoLTPgalYce65kGllSWGAMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بازنشر کرد:«ائتلاف نتانیاهو در تازه‌ترین نظرسنجی انتخابات اسرائیل پیشتاز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72113" target="_blank">📅 13:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72112">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o41WVkUrMV0NYIMzN32HkhOnNAPKstV9wBnSpi1-ipBewjDhqDRIKtedVd8Q4VlU2kkP_AqutXRISG1g8REEidzgtpmYRdHtcAvpW2N8AKNUNsnNBxh_huNiXqAcdEvNAtmBRleShMwsCshA0XpPwNqZ6mukJF2-Z2ojuiu6dOjyTdpOTsievntGWRG46GobvZVIdxEhUStLsZ-cHBhEGE2UBoILTkT2HMhI4O4uh87YWHDOKwEYZcF2IkUm_lCZyQbWqCCG1K36Igmcp1doRab1OmQSf8fBgnEQTAuEoxiB9L3zER49SgBBasSA0IxCnQihkzseMGz5ONJsQWtGzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حال‌ و هوای یکی از دانش‌آموزان در جشن شروع سال تحصیلی جدید:
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72112" target="_blank">📅 13:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72111">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb3684649a.mp4?token=SdLpTA67p3-Wk1FVmURASrS1yVsLIkmSGz2dDbqEElAYNOZwKDqGVSG0SjAFmSVQ-4sx63yo_4D2eebHZOlyVfo1O-2OkBlmJxLxom8Q9vm4flkwQtkDiPrVl3vvBCZegylB4mRmSWyo7YEGo6olP8Fe68ebepToBS7ysXyrWq8bxKpeA3cvhdq6o8WeKs6uo6A6iWn1UFBJE2LhNCZAHe09fqhX4wCyEjB3LFS3VZ2IuSZwB6S68JbEgugpHfISbdv7-uxd20CAPCDaPgRnsvWOpbLHfFFHkMAmPA65FCvDGsUF1Dbw2xdnJnJ1TizNoRXqSaihpTCdDB0K4ynPJCst9mSAsJrtHBNSC-ASoM0Iwc3fiedOspM2iXbI-LgFnt79I8RkG3HrAi8BVm2Dv0oj0yNpO7eDX9R_elxM2U1g-4Ls_g7VnVKbop4baTTDUepuILkr5NSANHxX8mTBSvcehDhp87oBcbKjV9I8xi6lARwyBTgHL121ncyd46r1x9pWzvxPZljske8SxBe5aH1ZDfRYc1EyL8nLz14NMiAsg_SgBk9PW1qcDiHcVTVb_VF4Jhs_jbYln1bLiXJjh8ebV9JYSfUIow07Lxy_Esvm3IOyCkQK0PBVhrB3vboj7T-ciw5-NmGw90uNZzQMig7HFIodRFFxakqArJOqhZk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb3684649a.mp4?token=SdLpTA67p3-Wk1FVmURASrS1yVsLIkmSGz2dDbqEElAYNOZwKDqGVSG0SjAFmSVQ-4sx63yo_4D2eebHZOlyVfo1O-2OkBlmJxLxom8Q9vm4flkwQtkDiPrVl3vvBCZegylB4mRmSWyo7YEGo6olP8Fe68ebepToBS7ysXyrWq8bxKpeA3cvhdq6o8WeKs6uo6A6iWn1UFBJE2LhNCZAHe09fqhX4wCyEjB3LFS3VZ2IuSZwB6S68JbEgugpHfISbdv7-uxd20CAPCDaPgRnsvWOpbLHfFFHkMAmPA65FCvDGsUF1Dbw2xdnJnJ1TizNoRXqSaihpTCdDB0K4ynPJCst9mSAsJrtHBNSC-ASoM0Iwc3fiedOspM2iXbI-LgFnt79I8RkG3HrAi8BVm2Dv0oj0yNpO7eDX9R_elxM2U1g-4Ls_g7VnVKbop4baTTDUepuILkr5NSANHxX8mTBSvcehDhp87oBcbKjV9I8xi6lARwyBTgHL121ncyd46r1x9pWzvxPZljske8SxBe5aH1ZDfRYc1EyL8nLz14NMiAsg_SgBk9PW1qcDiHcVTVb_VF4Jhs_jbYln1bLiXJjh8ebV9JYSfUIow07Lxy_Esvm3IOyCkQK0PBVhrB3vboj7T-ciw5-NmGw90uNZzQMig7HFIodRFFxakqArJOqhZk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دنی دانون، سفیر اسرائیل در سازمان ملل:
ما می‌دانیم رهبران ایران کجا پنهان شده‌اند. ما می‌دانیم آن‌ها چه کار می‌کنند و چه می‌گویند.
به گمانم جانشان برایشان اهمیت دارد. آن‌ها دریافته‌اند که اگر به اسرائیل حمله کنند، تنها چند روز طول می‌کشد تا سراغشان برویم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72111" target="_blank">📅 12:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72110">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/402f33620e.mp4?token=Ci7i6iKrjCLK4oByHzhSHKb7oXQp3CwQHtuFDtZv-zeSTaw3Y83-9hBFN_wylu60NWWY-70XmSiavWPIhdxKE_4gQKcM-OcyqYhdkrmRblIxO1WDAJgKOSG8dcaTrrZGsA_EsYf0J0zf2PdhkYkcj4GYwUujbTuewGFCiVqH_ucVQYR4KPT9UdVVq5EHCDPVdu-kHxXE-mdJ1bPYQPxy9NUK2yY0FNIDopmLTjCQYlfugAljkDJo3PvkhZURMYTaU2ELOsVpXMHV9ijCq-LkpBE8Zvp9slfCtiIfofUVFFk0_Cef1_21KQ6r1MUIBYuCab7D99teDggGTAU3zQ61bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/402f33620e.mp4?token=Ci7i6iKrjCLK4oByHzhSHKb7oXQp3CwQHtuFDtZv-zeSTaw3Y83-9hBFN_wylu60NWWY-70XmSiavWPIhdxKE_4gQKcM-OcyqYhdkrmRblIxO1WDAJgKOSG8dcaTrrZGsA_EsYf0J0zf2PdhkYkcj4GYwUujbTuewGFCiVqH_ucVQYR4KPT9UdVVq5EHCDPVdu-kHxXE-mdJ1bPYQPxy9NUK2yY0FNIDopmLTjCQYlfugAljkDJo3PvkhZURMYTaU2ELOsVpXMHV9ijCq-LkpBE8Zvp9slfCtiIfofUVFFk0_Cef1_21KQ6r1MUIBYuCab7D99teDggGTAU3zQ61bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز یکم مهر ماه، بچه‌های میناب دیگه نیستن که برن مدرسه...
اما جاشون پیش خواهر برادرای بزرگترشون امنه
🤍
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72110" target="_blank">📅 11:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72109">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b92a5ff67f.mp4?token=PYO5fRxuAE6hPEE2DVgYzs-6FpL1qehUbHUvk26qwG0qwGyoB-iZnreNzDwx6Soh2ZrzSTlBr-jrbT1X0wD_cZkR70JU08SHCLUZZB9HgS2mjMKXjat6Xojv-Ii4ZWtEl8sZG6NVIal0TRVoAJZVZgNFlV83z2H0auwcEhdP0_ECpChoNPjDu87ZR5A94Kd9oYVAKnEmZvvVaEfUyodTX_V_c9vhgP8FCA1iFmb69iobKcXciO_1GGYg_c4hMWSqm9GNX1HeLHxSFabOfy7PvIG_rX-whqvwJyj8ARJFsNXwKWieelwUFzfb5ZbIbLBGIXXPRIdAtcPe1JgIuwt6N3HzT9r2W102mfpDICEwQR9zBJBeHoPztePilhsuOCNVv7kuqoBSxx0VDo8RvKscRC2rXvBHBbM7TEko9OvmgW2Q66wmJCP6DzJ2becDQADNnXDBgKMZr-ZyulFrzK2EbZRpfAm4i-iip0VvvRvV3J1tYx3CZC1STrPCzesuLtcWUSVvQ_Ehv7cIdSDCfWmbZlct44iI8j6DAo9BgT2btEDfbWTpalJdsSqbVgF4OQdyB5P00tYArfjODpGC0_2--dP6Vb307mxqGBLAO_TRPCkPpkNWcvvkkaa_Gdlbw9VnGWDSw4MKQDWbnniZdh1g5FlmEJ4iNgyzOq4ORruPNDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b92a5ff67f.mp4?token=PYO5fRxuAE6hPEE2DVgYzs-6FpL1qehUbHUvk26qwG0qwGyoB-iZnreNzDwx6Soh2ZrzSTlBr-jrbT1X0wD_cZkR70JU08SHCLUZZB9HgS2mjMKXjat6Xojv-Ii4ZWtEl8sZG6NVIal0TRVoAJZVZgNFlV83z2H0auwcEhdP0_ECpChoNPjDu87ZR5A94Kd9oYVAKnEmZvvVaEfUyodTX_V_c9vhgP8FCA1iFmb69iobKcXciO_1GGYg_c4hMWSqm9GNX1HeLHxSFabOfy7PvIG_rX-whqvwJyj8ARJFsNXwKWieelwUFzfb5ZbIbLBGIXXPRIdAtcPe1JgIuwt6N3HzT9r2W102mfpDICEwQR9zBJBeHoPztePilhsuOCNVv7kuqoBSxx0VDo8RvKscRC2rXvBHBbM7TEko9OvmgW2Q66wmJCP6DzJ2becDQADNnXDBgKMZr-ZyulFrzK2EbZRpfAm4i-iip0VvvRvV3J1tYx3CZC1STrPCzesuLtcWUSVvQ_Ehv7cIdSDCfWmbZlct44iI8j6DAo9BgT2btEDfbWTpalJdsSqbVgF4OQdyB5P00tYArfjODpGC0_2--dP6Vb307mxqGBLAO_TRPCkPpkNWcvvkkaa_Gdlbw9VnGWDSw4MKQDWbnniZdh1g5FlmEJ4iNgyzOq4ORruPNDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات روته دبیر کل ناتو درباره ایران:
چرا برای از بین بردن توانمندی هسته‌ای ایران، حضور ایالات متحده ضروری بود؟ چرا اکنون در ماجرای حوثی‌ها در دریای سرخ، همه نگاه‌ها به ایالات متحده دوخته شده است؟
زیرا اروپایی‌ها به نوعی از توانمندی کافی برای انجام این کار به تنهایی برخوردار نبودند. آنجا حیاط خلوت اروپا محسوب می‌شود، نه حیاط خلوت ایالات متحده.
در آینده، دستاوردِ داشتنِ یک ناتوی قوی‌تر این خواهد بود که اروپایی‌ها می‌توانند خودشان به امور حیاط خلوتشان رسیدگی کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72109" target="_blank">📅 11:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72108">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اظهارات روته دبیر‌کل ناتو درباره ایران:
می‌توان گفت که اجرای عملیات «Epic Fury» بدون بهره‌گیری از اروپا به عنوان سکویی برای اعمال قدرت ایالات متحده، غیرممکن می‌بود.
از ۲۸ فوریه سال جاری تاکنون، ۵۰۰۰ فروند هواپیما در پشتیبانی از عملیات «Epic Fury» از پایگاه‌های اروپایی به پرواز درآمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72108" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72107">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72107" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72107" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72106">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e20ctXbssOnUTHcNL1GUq2Kv3B05dhIppQS4XpO8O92HFYNQKmfNKSu1OYDqASGr4lnNKba26zeDm0wSY_SKQ-EJ81Jg0dGvFsKjvl3H5S4l6jOWzvjbq5BZ-W9pM-XJXvLa1DA9GrFr3OpBn-PUmxc0HZttQACHc9ThxcKMCgbLAVApvJFEqT15iGbe4KEGNOytnR2lDsNQ0uDnLeJJuVM3p6Nk7jIH5kco2V6gNPtkiNEP5szwuZc3aXJrEfYB6zwJ2u2R2ZK7qTSQTyS-QEk7j2pKZJbiJGdYZawyTZpJ-qg7rJAj-fQ6V-dsQtUGERw5UW2yL_li-TqTqtPBig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
هیجان مسابقات DOTA 2 را زنده در
TrexBet
دنبال کنید و با پیش‌بینی دقیق نتایج برنده شوید!
🦖
پوشش کامل تمام بازی‌های محبوب Esports:
‏CS2, DOTA 2, Valorant و ده‌ها گیم جذاب دیگر...
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72106" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72105">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">شلیک چندین موشک ضد کشتی به سمت شناورها در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72105" target="_blank">📅 11:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72104">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4629cd7c2a.mp4?token=h-lqsVYTpWPoLqYkvH2Ld69mhEovY0L4xcsh8nluRWv07XdxOy-egVp-kG7YCXohTF79YMqBHP1AwnhZa91fotqfek31RNzNf6cGcWTw-BJc0IpxXjgL-tMIwUkS30BQ7GDm_CXkdTNixatu55J98kX5Pw_nW3pBIwexrsOK5BZuOwkEhB2OweKTJxUbWndhnCFsgHau_b0bZY9hOOU9peyiJh5qxP51CGYGmHkzcjbfDfthsVoVDo1vhSnk9R8rnNHZCMDhQwmB1vA83prlt4iezoaLVade99EgWnInmyHrV_2zOldmeGmju9yWAvpZutx4c6Q9MoDlOkKv9iHWVJqucSDRc04-uu6imKHYUYEiPlck8JzKA_7gk_DgSI2XVQ5-FQMpTdT-oo8-dT9OagQEiNmuGtuCWHJ8PZl0SHAtqmvLJ7H-bUzHgSduP-iAVcFk1FyUVCrYfTJ1U_qsNh2U5hCgoetCwMVLn9vHpJcsDSW4djvPo8iynPuIwpl-h-gASYlK88IPRvge8pecO6SfByTuow55ZY29palfClVggoIw_MjeTw9zfeMVf5RPEKG4_8r5mI1Eu1nO6ksjGl9u-XwxRYRdKAXMG7pnSewE3DTgKMS0qwp1YjhPPkAev_plyDD8r2ppO4rFVFNxx_9BNtHPEfXa_A5g6USBnKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4629cd7c2a.mp4?token=h-lqsVYTpWPoLqYkvH2Ld69mhEovY0L4xcsh8nluRWv07XdxOy-egVp-kG7YCXohTF79YMqBHP1AwnhZa91fotqfek31RNzNf6cGcWTw-BJc0IpxXjgL-tMIwUkS30BQ7GDm_CXkdTNixatu55J98kX5Pw_nW3pBIwexrsOK5BZuOwkEhB2OweKTJxUbWndhnCFsgHau_b0bZY9hOOU9peyiJh5qxP51CGYGmHkzcjbfDfthsVoVDo1vhSnk9R8rnNHZCMDhQwmB1vA83prlt4iezoaLVade99EgWnInmyHrV_2zOldmeGmju9yWAvpZutx4c6Q9MoDlOkKv9iHWVJqucSDRc04-uu6imKHYUYEiPlck8JzKA_7gk_DgSI2XVQ5-FQMpTdT-oo8-dT9OagQEiNmuGtuCWHJ8PZl0SHAtqmvLJ7H-bUzHgSduP-iAVcFk1FyUVCrYfTJ1U_qsNh2U5hCgoetCwMVLn9vHpJcsDSW4djvPo8iynPuIwpl-h-gASYlK88IPRvge8pecO6SfByTuow55ZY29palfClVggoIw_MjeTw9zfeMVf5RPEKG4_8r5mI1Eu1nO6ksjGl9u-XwxRYRdKAXMG7pnSewE3DTgKMS0qwp1YjhPPkAev_plyDD8r2ppO4rFVFNxx_9BNtHPEfXa_A5g6USBnKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی:
تولید ناخالص داخلی ایران در سال ۱۹۷۸ دو برابر کره جنوبی بود. امروز، تولید ناخالص داخلی کره جنوبی پنج برابر ایران است.
وضعیت اقتصاد ایران قابل تداوم نیست؛ پایدار نیست و در آستانه انفجار قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72104" target="_blank">📅 11:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72103">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/582ee3d494.mp4?token=p0PODD_qtt8BHxDLXfRyizMh0LlCYR-C7PEqFbQvPm8_-WOu6F_np0zvMnCfQqwPNEp_JU9NGxIDZt1J28PwfTgmBoZvNV79uDnmcjAJGnAiC56OUuKElvKXiDG-c6hl81Qf44RW9oh69te24iV0uFxq-8m38TZZSTBjb27DO_sO_m3kvP2gXjmEIcD7S-FbQMydeiwC_Z5a2wncmkqQ-YIPsbhAeaFF8JL4mqE4KFO0XKJkvfBzCQyqbbAglvR6uSDFvbY1c9ShHs-5x14QnEWr1zMGmk0BNk8RNr_e6Xw9W76dG1LjaOU4WFC9wYKEpzvbEgVqwo3nHvwnlz-95w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/582ee3d494.mp4?token=p0PODD_qtt8BHxDLXfRyizMh0LlCYR-C7PEqFbQvPm8_-WOu6F_np0zvMnCfQqwPNEp_JU9NGxIDZt1J28PwfTgmBoZvNV79uDnmcjAJGnAiC56OUuKElvKXiDG-c6hl81Qf44RW9oh69te24iV0uFxq-8m38TZZSTBjb27DO_sO_m3kvP2gXjmEIcD7S-FbQMydeiwC_Z5a2wncmkqQ-YIPsbhAeaFF8JL4mqE4KFO0XKJkvfBzCQyqbbAglvR6uSDFvbY1c9ShHs-5x14QnEWr1zMGmk0BNk8RNr_e6Xw9W76dG1LjaOU4WFC9wYKEpzvbEgVqwo3nHvwnlz-95w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناوگان هواپیماهای باری نظامی، از جمله هواپیماهای «آنتونوف ۱۲۴» در حال فعالیت از فرودگاه لایپزیگ/هاله در آلمان مشاهده شده‌اند.
فرودگاه لایپزیگ/هاله یکی از مراکز مهم لجستیکی ناتو است که برای انتقال تجهیزات نظامی و محموله‌های فوق‌سنگین مورد استفاده قرار می‌گیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72103" target="_blank">📅 11:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72102">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c2bb73b79.mp4?token=GY9c-icAFpQxWYfaJuh4M79S6rqGSwXuaH7YFAU5lIdsUzK2DWNWsjBXD-U_03MDsCY104PVhLuklWYArUsVti75g3jyzis7K0SLjpd5JRhq5DW9_jGKx2sA6iDkFWNYJTPn0uuqdxvDBF1eDFItUZr4obJ3nQnZjIMhi2oNgJda-hxRWx0P2c1t917thRM0xxIaiWFddfE-_iIhep5t3V87nYo310CgaTglOEZK2qS37mfHN8kptGImCMGT9s1J5QVjmdVTZsqEVxwct2hGuFvM9HeL_FrJYs119My0Y985C2UTYKr_DynIYhm6-KwjsY3eUNOPuzRNBP6YOxnR_g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c2bb73b79.mp4?token=GY9c-icAFpQxWYfaJuh4M79S6rqGSwXuaH7YFAU5lIdsUzK2DWNWsjBXD-U_03MDsCY104PVhLuklWYArUsVti75g3jyzis7K0SLjpd5JRhq5DW9_jGKx2sA6iDkFWNYJTPn0uuqdxvDBF1eDFItUZr4obJ3nQnZjIMhi2oNgJda-hxRWx0P2c1t917thRM0xxIaiWFddfE-_iIhep5t3V87nYo310CgaTglOEZK2qS37mfHN8kptGImCMGT9s1J5QVjmdVTZsqEVxwct2hGuFvM9HeL_FrJYs119My0Y985C2UTYKr_DynIYhm6-KwjsY3eUNOPuzRNBP6YOxnR_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کم‌ کم ربات‌های جای انسان‌ها رو دارن میگیرن....
برای اولین بار تو تاریخ، یه مبارزه رسمی بین انسان و ربات برگزار شد؛ که در آخرش ربات با یه لگد سنگین حریفشو انداخت رو زمین و ناک اوتش کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72102" target="_blank">📅 10:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72101">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2331092d7.mp4?token=m9FO_U2rg7p2b6Plx9FuahW80JqHrawPXZAkY7QFOqF3dPXH4osSxjZ0K3Bv8efB01g-MTfmN0CrdgLTXHHeGL81ADWoEKudkn2ALD4Jnt4fveDmUd-SjOkIVm2JVVraS05r0zTSitOKgQohjluyktZt_0acTV4Gvk1SEWFZmIChP2EwDfEY5YBR8ZQvVhCc-khFJKsdu9CN1rm9bbv7rDJELEDp80QFLFhqgXYcUu6gFaq5P9G2Wz9qpOsgnR1pNTj4E0RMpZj0XzK3uSVeaferTC4pOJE39jHJm8UrScTOZfqhzR13pbba9Cq3JUcZhME538__MPUylgUZBRT_ew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2331092d7.mp4?token=m9FO_U2rg7p2b6Plx9FuahW80JqHrawPXZAkY7QFOqF3dPXH4osSxjZ0K3Bv8efB01g-MTfmN0CrdgLTXHHeGL81ADWoEKudkn2ALD4Jnt4fveDmUd-SjOkIVm2JVVraS05r0zTSitOKgQohjluyktZt_0acTV4Gvk1SEWFZmIChP2EwDfEY5YBR8ZQvVhCc-khFJKsdu9CN1rm9bbv7rDJELEDp80QFLFhqgXYcUu6gFaq5P9G2Wz9qpOsgnR1pNTj4E0RMpZj0XzK3uSVeaferTC4pOJE39jHJm8UrScTOZfqhzR13pbba9Cq3JUcZhME538__MPUylgUZBRT_ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لمس ممه‌های دوس دخترتون واقعا زندگی شمارو نجات میده! این یه شوخی جنسی نیست، از لحاظ علمی این موضوع کاملا ثابت شده و اینکار مثل معجزه عمل می‌کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72101" target="_blank">📅 09:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72100">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/575ce7dd12.mp4?token=YHcbc_UtqY0sGG6ITGU7AFfHc3m6M86cIMCY51B1d7FmYrA7h5rQQeadIzdEU7cjBaFV5kDtf9mvyM2RF7Vfs-N8YL1QJGS1QSjHnHjvYpLY3ML4UFNFx5t_svHrbkMhY_9blxm3guet2CtMulkCGvXojB1CgIzUUN3thtrAJOhJQ5zu8zo8Sht0sP_TwyGK-JvpIlwIDXp0569GMMAf9sCLQUnPZ3YrHBdKQqdatID-Q-I1BfeDpWyYsOTJgdA0_dOAB_MUiH0s8vBWoJQEIbQi52Kld889BZnFLqXVS5f-Ca6yhneNZCm86MABdFGLjWjFJ6-xZ6scx6a4QM_15g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/575ce7dd12.mp4?token=YHcbc_UtqY0sGG6ITGU7AFfHc3m6M86cIMCY51B1d7FmYrA7h5rQQeadIzdEU7cjBaFV5kDtf9mvyM2RF7Vfs-N8YL1QJGS1QSjHnHjvYpLY3ML4UFNFx5t_svHrbkMhY_9blxm3guet2CtMulkCGvXojB1CgIzUUN3thtrAJOhJQ5zu8zo8Sht0sP_TwyGK-JvpIlwIDXp0569GMMAf9sCLQUnPZ3YrHBdKQqdatID-Q-I1BfeDpWyYsOTJgdA0_dOAB_MUiH0s8vBWoJQEIbQi52Kld889BZnFLqXVS5f-Ca6yhneNZCm86MABdFGLjWjFJ6-xZ6scx6a4QM_15g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی مشهد یه خانم حامی حکومت تو اتوبوس، به یه دختر بخاطر حجاب حمله‌ور شد!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72100" target="_blank">📅 09:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72099">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad662c895d.mp4?token=a-QFfQJtdFHj9pTSyifVLm0yzg_kz0kUu3d6_v920WOek9lBHXv79GXlklJsdXYfUfP7-MwArq1HdAAAAEt_k-3IB0_wjzO028c39bdo0HT2WJa8IJMriA8kfUqnme2xY3y7963Q9PdM-tTZYxghzMMrVHrEOAwsfNbpGuThqSHK3nSPpUwaJE45EcC2YwQxcDViG60EPGQz3I8NC3orgeFOeYpic5-BzVoBwyWpIc-c6Jx-G4oEprRvGxXLDoBZb2a-yeE9e7EqNn9Gb8D5B3HpxFVdfPm-fff0PB5cYG-DAkY71Z5WIiZdHKdZFl9WLkEfaAXA7lAzYtCPCpXFPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad662c895d.mp4?token=a-QFfQJtdFHj9pTSyifVLm0yzg_kz0kUu3d6_v920WOek9lBHXv79GXlklJsdXYfUfP7-MwArq1HdAAAAEt_k-3IB0_wjzO028c39bdo0HT2WJa8IJMriA8kfUqnme2xY3y7963Q9PdM-tTZYxghzMMrVHrEOAwsfNbpGuThqSHK3nSPpUwaJE45EcC2YwQxcDViG60EPGQz3I8NC3orgeFOeYpic5-BzVoBwyWpIc-c6Jx-G4oEprRvGxXLDoBZb2a-yeE9e7EqNn9Gb8D5B3HpxFVdfPm-fff0PB5cYG-DAkY71Z5WIiZdHKdZFl9WLkEfaAXA7lAzYtCPCpXFPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی در استودیو فاکس‌نیوز با مارتا مک‌کالوم:
«وقتی من میلیون‌ها ایرانی را در ۳۱ استان کشور به آمدن به خیابان‌ها فراخواندم، آن‌ها به صورت میلیونی حاضر شدند و ضمن اعلام حمایت، شعار پایان دادن به این رژیم را سر دادند.
آن‌ها از تمامی اقشار جامعه ایران، اقوام، ادیان و گروه‌های اجتماعی گوناگون بودند؛
این جلوه‌ای عالی از اتحاد و تنوع است.
بنابراین، هر کس که ادعا می‌کند پس از ما ایران دچار جنگ داخلی خواهد شد [باید بداند که] عامل اصلی این تفرقه و اختلاف، همین رژیم است.
همه ایرانیان می‌دانند که این رژیم بذر دشمنی و خصومت را کاشته است.
اما ایرانیان دریافته‌اند که پس از دستیابی به آزادی، قادرند دوباره برخیزند؛ درست همان‌طور که قرن‌ها فارغ از تفاوت‌های قومی یا مذهبی، در صلح و آرامش در کنار یکدیگر زندگی کرده‌اند.
و انقلاب «شیر و خورشید» در راه است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72099" target="_blank">📅 07:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72098">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/686ffe220e.mp4?token=WOW302PjkdYQR7MnImWTJbJjskGAKZ2_02kqcNaBq8Rh1kHLD1lbzW6TJ0yTOkJa4foiIxeIBGpjhJD54LzhCvKp0paYOO4zJtqK6LPb8C3DljPsal8YIbCQBjz_C47F2hchPjsVfiqElPLaktfkBDy2OG-avUNch8EU1itFx_VmKVTtR_TIP42Jz1TIVuN8kA4Bm5ukYLBKKCq7jjsiFi6yPNkr5SXreZOwJMQmxihfgzoc-zQYqlfnhUKVQVnrpQ9HZtt905x4K0srD7585pRyP8TIzIz6HuIEkMWVS19daIjIZZDiL9NbESl62Y8RUOgsQw4vo2VMXeoutXIaPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/686ffe220e.mp4?token=WOW302PjkdYQR7MnImWTJbJjskGAKZ2_02kqcNaBq8Rh1kHLD1lbzW6TJ0yTOkJa4foiIxeIBGpjhJD54LzhCvKp0paYOO4zJtqK6LPb8C3DljPsal8YIbCQBjz_C47F2hchPjsVfiqElPLaktfkBDy2OG-avUNch8EU1itFx_VmKVTtR_TIP42Jz1TIVuN8kA4Bm5ukYLBKKCq7jjsiFi6yPNkr5SXreZOwJMQmxihfgzoc-zQYqlfnhUKVQVnrpQ9HZtt905x4K0srD7585pRyP8TIzIz6HuIEkMWVS19daIjIZZDiL9NbESl62Y8RUOgsQw4vo2VMXeoutXIaPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی در اجلاس سالانه «کنکوردیا» (Concordia)، پرسشی را مطرح کرد که دهه‌هاست در سیاست بین‌الملل نادیده گرفته شده است: چرا مردم ایران در کانون گفتگوها قرار ندارند؟
جمهوری اسلامی با مذاکرات بی‌پایان یا سیاست مماشات تغییر نخواهد کرد. ایرانیانی که به دست این رژیم قتل‌عام شدند، خواهان آزادی بودند، نه توافق هسته‌ای یا کنترل تنگه هرمز.
انتخاب روشن است: یا همچنان بر روی رژیمی سرمایه‌گذاری کنیم که عامل بی‌ثباتی و تروریسم است، و یا در کنار مردم ایران بایستیم؛ کسانی که شرکای طبیعی جهان آزاد برای ساختن آینده‌ای سرشار از صلح، امنیت و فرصت‌های اقتصادی بی‌سابقه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72098" target="_blank">📅 07:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72097">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivumGjCe3tak1qKCqCcrcktd0zIke2rtDt8d1LjEC99aDVPTU-QYHtZV8v3DGFahD7XmynyNAiIfFFCbf4JDi9hdPunVp7hN3MKzZp9B4CWj6F9xP9ceuQ1-MXxvtpzLfUGR3aO7z_Msp75EBAdkjo-iqplR3E0ZRQim8u16nHqtkQlyyQfwh_ylDVkj2zKvuPAeimJ4xZUJY1om8Ku5lJjMkmOgQPmJhRPLtGI-nSxTswK3IXptiUn9TiQOPQVQOvcvm65IeC7B0crsMNhdu2ZfWKuMYFXb80Z_0M64xsZq1x4plbfn_81W81MCh-eBPdS5yiATKxPftbKGtthbIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛یک منبع آمریکایی به العربیه:
آمریکا درخواست ایران برای رفع محاصره را نپذیرفت.
فرصت‌های دست‌یابی به توافق محدود است.
اختلافات و موانع بزرگی همچنان میان دو طرف وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72097" target="_blank">📅 07:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72096">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SApUqBDiHDXIYzTwsbldGF_xW9tlXdsWYEr9TIwHZXXYqm41a8iPVVDxF-qM7ibmamEfookEDIpdw6wLZuknuWQTCQPWkTvN6qvQodiBv6osptSioEp-iw71aiG1UX4lHO3cFQsKwINmuVvMpayZi9JvBA-uKI9NcpQERjFhqioOtjiMH9tbaS1nGmBxU9WKhJ2GzVih6IlXs9dZX6Sn-FoqMLn6eE0FOI8g3Fk2wlB7R22Z7FUGPVBV0fcruPlLwA9oUgkjhtj1piUU0yOVnPUO0znlajZwmfNAKcxwfm3q6PjJXVWWKyK-0Lw-i91b54J-GeL7MFZQ4lzAlGAWng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استیو ویتکاف:
امروز در حاشیه مجمع عمومی سازمان ملل، از طریق میانجی‌هایی که در طول روز میان دو طرف در رفت‌وآمد بودند، گفتگوهای مفصلی با هیئت ایرانی انجام دادیم.
آن‌ها یک دور از مذاکرات را با موفقیت به پایان رساندند؛ مذاکراتی که امیدواریم سازنده و نویدبخش باشد. میانجی‌ها به کار خود ادامه خواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72096" target="_blank">📅 06:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72095">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83dc83eba1.mp4?token=ZulvG9c29ShANOtQcEY7B6BcIzYrZuCdyXK0KyRUkAfCYb8knfaa83ls7TRtuLLblT239oXee9FhDREB1JxvpsfCcvFo3HDpt7svOg5tPqMb5pVMndLyIaW9VsWr3E0uknj-NH5bH10THrkgyyi3pjrUDU29hojt-b7Av7QO88KCSa8LeFEiYWOkxlKnrb0CBMxnASMeKMPbkmE3FU73-OFXoJtrhJJbQpCU249eTFJQlHXA9p-gNxDqVH1wo8oxWKaD84q_cNfsGljy6waAL0vr4867DAPJNJh2IgdFFvRPPYJ4PSx0fM6y0cwXKFlZ7ftFgSHHuD4KBt1YkXHc1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83dc83eba1.mp4?token=ZulvG9c29ShANOtQcEY7B6BcIzYrZuCdyXK0KyRUkAfCYb8knfaa83ls7TRtuLLblT239oXee9FhDREB1JxvpsfCcvFo3HDpt7svOg5tPqMb5pVMndLyIaW9VsWr3E0uknj-NH5bH10THrkgyyi3pjrUDU29hojt-b7Av7QO88KCSa8LeFEiYWOkxlKnrb0CBMxnASMeKMPbkmE3FU73-OFXoJtrhJJbQpCU249eTFJQlHXA9p-gNxDqVH1wo8oxWKaD84q_cNfsGljy6waAL0vr4867DAPJNJh2IgdFFvRPPYJ4PSx0fM6y0cwXKFlZ7ftFgSHHuD4KBt1YkXHc1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود هم رسید نیویورک
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72095" target="_blank">📅 06:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72094">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72094" target="_blank">📅 01:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72093">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72093" target="_blank">📅 01:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72092">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">صدای دوانفجار جدید در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72092" target="_blank">📅 01:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72091">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVe_7J0iNGJl3CBEwVLmkwkEiPGkiiIHAXC_szKT7sQNydrIz0Pzt5YnWfUd9NxhLjjABCvp6mluRoVhMVF70uJQtE3ia9ryKoWeRVsTXuFmBLI-T98SnW1sseWG24H2CIyfeVCpGiqlj49JxgxRLBU5sSn_YqnHB5-THkhe4m9LCRJ_O8WBLct9Wl4k9TB-cVRo35WGu1VlWcSbcZsQp5kSpC2Kck7rnpH4x_OaSt9Ecbs3iRURS3ccOSgFOq8heJXjMh1MiHSTtIXB1EvNXB6q1fSlz0hJjSDsNC3ZUqUHJhlqSDwfQyNfGUMaN21wnBlMmyN8wKQoyU6GrWj-aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای‌نت:
انتظار می‌رود سخنرانی نتانیاهو در سازمان ملل به شدت بر ایران متمرکز باشد و به گفته‌ی ایدز، این سخنرانی حاوی «غافلگیری‌های» نامشخصی خواهد بود.
هیئت نمایندگی اسرائیل همچنین خود را برای احتمال مزاحمت یا خروج هماهنگ‌شده در طول سخنرانی آماده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/72091" target="_blank">📅 01:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72090">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ایرنا: صدای انفجار در حوالی جزیره قشم به گوش رسید
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72090" target="_blank">📅 01:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72089">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3046a77aed.mp4?token=ZlYI2w9mQXBrhMTh-ZKP9DLIIYoxPARIIRhrFHfdG1J7q0Cap_oOSDhcBY6wheffHQPpThJfSH-GpoxVjvzhyptbdujf0BlP51T6Sfaca--A6I8mcSsKrypDXEGM19UML3DkBCtDptbczP-3xjMwIUieEN9a_x0BbLTe8n6pmKc_Er8KFFm9gLL5wFDpLSytVocAOmXF64Ay9U22JDc1U4qGKbQi9c0gF6yficm7Zaa5suFIiTs5pONdlvyMeNi7Ce48pfvMlqYjFnJ4Y7_2M8O7es05aIzjm9mzzazGZPdx7jMKGa0OouDmx-ADHjDY9iCCrG2wnczy3On2ARKJpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3046a77aed.mp4?token=ZlYI2w9mQXBrhMTh-ZKP9DLIIYoxPARIIRhrFHfdG1J7q0Cap_oOSDhcBY6wheffHQPpThJfSH-GpoxVjvzhyptbdujf0BlP51T6Sfaca--A6I8mcSsKrypDXEGM19UML3DkBCtDptbczP-3xjMwIUieEN9a_x0BbLTe8n6pmKc_Er8KFFm9gLL5wFDpLSytVocAOmXF64Ay9U22JDc1U4qGKbQi9c0gF6yficm7Zaa5suFIiTs5pONdlvyMeNi7Ce48pfvMlqYjFnJ4Y7_2M8O7es05aIzjm9mzzazGZPdx7jMKGa0OouDmx-ADHjDY9iCCrG2wnczy3On2ARKJpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت
ترامپ:
یا به توافق می‌رسیم، یا کار خیلی خیلی سریع تمام خواهد شد.
آن‌قدر سریع تمام می‌شود که سرتان گیج می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72089" target="_blank">📅 01:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72088">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LeMNJA42Ib5KM67lNB0Yv6-kYqodGb_kdfroephiA8RbpsQkxMZgQCJmeAlcAyP6hEwFmKC45QZI4STFd2oJkjIYic-qYn8Qk21Z62o8AWn8fjBJtxP8vAAHu3UOa7Pwl9_hbJdCqFOQ9BO86RWdAiOne8zWFV6H0WP7tWMN0bvNK1AtDTaI7h7VZbrHa9eG82BK057W3XJpJ4jY4KgE4mQ1lm3lgVW6uzZtjSBqm3036jH0rJcywnVXHocLwOWjCVQlG4WJmTJNofdl6TUOOxBhBr0R9NOm0cJ6c3hY0_nHP_CHsTpfIEinCCrvhHErnqEJ4RMYGvi4M7svldSFCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که تندروهای جمهوری اسلامی از پزشکیان تو نشست سازمان ملل دارن:
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72088" target="_blank">📅 01:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72087">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تابستون هم تموم شد و رسما وارد پاییز شدیم...
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72087" target="_blank">📅 00:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72086">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ساعت ۰۰:۴۷ بامداد چهارشنبه؛ یک انفجار در محدوده تنگه هرمز رُخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72086" target="_blank">📅 00:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72085">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a836832d.mp4?token=eq5KzSt-iUAOoB5Chipdo5JTLLDNBE4NZ-BQpYzaHiFFhh4B1VrwgPFCW5uABiGEKwOLNelejG-1_ze0UI9dG-7pTaRl1rxy0vIm0CzLGnuYgljmyZUFBRNcjCnDRdw3sR809YuHYHc9n_SpEmcU_Vxs9CbwjT9C_G10ZmxnBlG_JfVeBcJKkIkQpuZZc0huEG5JdA7VLd-Et4TDQXOK6muqjd6cgXaE1QDAY8o7vRY0VB8_OzBUScmQlGj9urprdFSxQUKoHsnkEC9fohWTSOOzTGo7S7798hdU9VYgnnnoJ0eQNNlxnRXjVCQOVQ-bMBmcJx7kXpbGYhJXeu2aJzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a836832d.mp4?token=eq5KzSt-iUAOoB5Chipdo5JTLLDNBE4NZ-BQpYzaHiFFhh4B1VrwgPFCW5uABiGEKwOLNelejG-1_ze0UI9dG-7pTaRl1rxy0vIm0CzLGnuYgljmyZUFBRNcjCnDRdw3sR809YuHYHc9n_SpEmcU_Vxs9CbwjT9C_G10ZmxnBlG_JfVeBcJKkIkQpuZZc0huEG5JdA7VLd-Et4TDQXOK6muqjd6cgXaE1QDAY8o7vRY0VB8_OzBUScmQlGj9urprdFSxQUKoHsnkEC9fohWTSOOzTGo7S7798hdU9VYgnnnoJ0eQNNlxnRXjVCQOVQ-bMBmcJx7kXpbGYhJXeu2aJzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
استیو و جرد امروز جلسه بسیار پرباری با میانجی‌های ایران داشتند. باید دید در ادامه چه پیش می‌آید.
به گمانم انگیزه و شتاب زیادی برای دستیابی آن‌ها به توافق وجود دارد؛ این همان چیزی است که از همه می‌شنویم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72085" target="_blank">📅 00:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72084">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e28a4d4c0.mp4?token=Xol9Xyq2m5pluoZIRqH1ClIvujksVrB7TshgQ7cWq3iO-L8bUYtBiAw6tkeiXxQGZ935fPXFPHrKDAfwEccDT_a-5ZYPfO9dtJjhlm2piDNLmF7IOyvso2aoE6U0_FEXMB0uOuDPGCf2XPkTJjidhp5dvVFlG9z5-PqfnTLEg0CSceSppiZikJuMoonY63eccedlIpzOra50NOmLfbfnubvRsiG2pS0VgQ40W_E6UJAcPEI6PpBW_VfJffo_pY4XED_D4kRjLoYiR2ebKuMXc1gcUpTx2wNfUg74lJArwnokQYn6II8TioFkI_kGFE5WMi7nuF7LocvnSFOSUns9-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e28a4d4c0.mp4?token=Xol9Xyq2m5pluoZIRqH1ClIvujksVrB7TshgQ7cWq3iO-L8bUYtBiAw6tkeiXxQGZ935fPXFPHrKDAfwEccDT_a-5ZYPfO9dtJjhlm2piDNLmF7IOyvso2aoE6U0_FEXMB0uOuDPGCf2XPkTJjidhp5dvVFlG9z5-PqfnTLEg0CSceSppiZikJuMoonY63eccedlIpzOra50NOmLfbfnubvRsiG2pS0VgQ40W_E6UJAcPEI6PpBW_VfJffo_pY4XED_D4kRjLoYiR2ebKuMXc1gcUpTx2wNfUg74lJArwnokQYn6II8TioFkI_kGFE5WMi7nuF7LocvnSFOSUns9-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
امیدوارم پیش از آنکه خیلی دیر شود، هرچه سریع‌تر کار درست را انجام دهند.
می‌دانید، زمانی فرا خواهد رسید که دیگر خیلی دیر شده باشد و ما دیگر فرصتی برای اینکه اجازه دهیم آن‌ها به عنوان یک ملت باقی بمانند، نخواهیم داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72084" target="_blank">📅 00:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72083">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تسنیم:
دیدار استیو ویتکوف، نماینده آمریکا، با عباس عراقچی، وزیر امور خارجه ایران، در حاشیه مجمع عمومی سازمان ملل متحد، پس از درخواست‌های مکرر طرف آمریکایی برگزار شد.
ایران اعلام کرد که از این جلسه برای بیان شرایط خود برای بازگشایی تنگه هرمز، از جمله لغو فوری محاصره دریایی، آزادسازی دارایی‌های مسدود شده ایران و پایان جنگ در همه جبهه‌ها، استفاده کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72083" target="_blank">📅 00:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72082">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a836832d.mp4?token=qqa1yCF7PU2N6zzTTQHH98WSGdSN5_0gfqDn3Ca8z77LzK-JxPKL7-r3vgnL8tYtYQwVR9M3H-rN_JSBKXzkDiy7GB_Lp4XUoJiEfxWaPZdFVuUb_Lj9YbxxBOQodOF_yMmKvIY-q8YMD1LFU0IuCQ6L3Df6eMkGbJtP2h3jiedqExIsRsvnnV31DrT4yh6Tlnf-uQwI73IVzZa-90x5VC_EILn-rk2KQnUfa_xlB7gEa7zPtSH1yFsTb79ETu-A91WfgBCCGsyO3vkrcuhO9j0hbFF84jJBMTSzhE5c5LCof6E8nfYCVs4uZDYodWXeKVwuKCQssx9PAb4CdfRdOjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a836832d.mp4?token=qqa1yCF7PU2N6zzTTQHH98WSGdSN5_0gfqDn3Ca8z77LzK-JxPKL7-r3vgnL8tYtYQwVR9M3H-rN_JSBKXzkDiy7GB_Lp4XUoJiEfxWaPZdFVuUb_Lj9YbxxBOQodOF_yMmKvIY-q8YMD1LFU0IuCQ6L3Df6eMkGbJtP2h3jiedqExIsRsvnnV31DrT4yh6Tlnf-uQwI73IVzZa-90x5VC_EILn-rk2KQnUfa_xlB7gEa7zPtSH1yFsTb79ETu-A91WfgBCCGsyO3vkrcuhO9j0hbFF84jJBMTSzhE5c5LCof6E8nfYCVs4uZDYodWXeKVwuKCQssx9PAb4CdfRdOjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
امروز یک نشست فوق‌العاده و مثبت بین کوشنر و ویتکاف با نمایندگان ایرانی داشتیم
واقعا در مسیر خوبی حرکت می‌کنیم اونا خیلی میخان توافق کنن اینو همه میگن
شتاب قابل توجهی برای مذاکره داشتیم
اقتصاد ایران رو منزوی کردیم اقتصاد اونارو نابود کردیم این خیلی خوبه
تنگه هرمز رو از مین ها پاکسازی کردیم و نفت جریان داره همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72082" target="_blank">📅 00:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72081">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4086006d.mp4?token=bIA8GPv9eKRUCnevjz8_3YMNM3Hide4buzxTBRSUu6-hXvT_BbQNJH-fGtV9tdh6LKAWEzB1l77B6fXB8Iwtfl6o_O2y8GUJNyNQ0ZBgJ-KKuWrXPkTrClJ_X3OKXvzbN_VBfvQ0OU64mZbL42K8U-xEkBIOo6giP6l153ipYAZemtdkvXYAKmjaepyNT5A7Na3Zsjz7one02ODFDQ9olSEzPopGPE_Jqtt2NJtAqOClc_XuxsSLJ9PzKAb-rAoZleG7WJ1whB0fCf32OqnWRNj3_Pw7ilS1jmeJCbnH2mFCQRTij4x3kGd2U6EjztcBxgr8Lm1Oilen4M-VhorDfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4086006d.mp4?token=bIA8GPv9eKRUCnevjz8_3YMNM3Hide4buzxTBRSUu6-hXvT_BbQNJH-fGtV9tdh6LKAWEzB1l77B6fXB8Iwtfl6o_O2y8GUJNyNQ0ZBgJ-KKuWrXPkTrClJ_X3OKXvzbN_VBfvQ0OU64mZbL42K8U-xEkBIOo6giP6l153ipYAZemtdkvXYAKmjaepyNT5A7Na3Zsjz7one02ODFDQ9olSEzPopGPE_Jqtt2NJtAqOClc_XuxsSLJ9PzKAb-rAoZleG7WJ1whB0fCf32OqnWRNj3_Pw7ilS1jmeJCbnH2mFCQRTij4x3kGd2U6EjztcBxgr8Lm1Oilen4M-VhorDfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداوسیما:
آمریکا داره آب خلیج فارس رو می‌ریزه تو امارات تا تنگه هرمز خشک بشه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72081" target="_blank">📅 23:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72080">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=NHaMKZUC5zEvBphrNerZOv3NbLzL756vK8FjizQ--1Yw_1DhpmSfes3374snRNvDk0XjxzBdH2Uyqe9LkqUm5qyJe3bxg4NDI0aGYxdOYCrQvN6r3gsdk6lUpcTqZTRCWUckqzmgSm3F-2bh501GCF2ouMpUXJUZyey2AkZYNm5BQtTKlaSCkTZhrN9mQcDSlAU5SPIuoHdkjiBiSlItmwp3k2zFM35b35Zws8j-yrF6bNa6YVmhntStRbg5nA3b4RHsVxAFse4NKiQlRLfZpvNCG1OplfaS4TFHP6Gp2fd3oY6ZfVXut4WvgmkBnPKEH9xM8xQJUdRwx7lwU6aaew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=NHaMKZUC5zEvBphrNerZOv3NbLzL756vK8FjizQ--1Yw_1DhpmSfes3374snRNvDk0XjxzBdH2Uyqe9LkqUm5qyJe3bxg4NDI0aGYxdOYCrQvN6r3gsdk6lUpcTqZTRCWUckqzmgSm3F-2bh501GCF2ouMpUXJUZyey2AkZYNm5BQtTKlaSCkTZhrN9mQcDSlAU5SPIuoHdkjiBiSlItmwp3k2zFM35b35Zws8j-yrF6bNa6YVmhntStRbg5nA3b4RHsVxAFse4NKiQlRLfZpvNCG1OplfaS4TFHP6Gp2fd3oY6ZfVXut4WvgmkBnPKEH9xM8xQJUdRwx7lwU6aaew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی آلمان یه دختر تریان (انسان‌های که فکر می‌کنن حیوانن) به یه خانم حمله می‌کنه و گازش می‌گیره، به پلیس اطلاع داده شد، هر چقدر از دختر اسم و فامیل پرسیدن فقط پارس کرد، پلیس هم اون رو برد مرکز نگهداری از حیوانات
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72080" target="_blank">📅 23:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72079">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/956bc67dd9.mp4?token=sIpcGbRRlLlR_NDiyCVQjjJxliNOvK7KFBMSR1nVdk-nztkXSfC6e7AUlRpmnfkREajI53awm5egmtRbzu-I-VahlU1TxKBMjQ57Cs7Sx4Cj7Gfq6njledDhOA6J0wt7ax8T0k20GJSPlkNO3fgKOPOs8Jg1S5Fa0e2US1s_YFCIbu_4AxxhADGaMNnMP7KFPUCPfOjOqi0dilYIqvZqPCCGAyATjnlBRsujpZpNkTF8rx79WSVT1MDUOlPlnRFgyVBeXQH8l8TwnfA7_NeUUvJC32ruquVhl133JPUkFn-tKFzJdz73EKoQrZAURSM7me-sMyuEfccedpDd69-clw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/956bc67dd9.mp4?token=sIpcGbRRlLlR_NDiyCVQjjJxliNOvK7KFBMSR1nVdk-nztkXSfC6e7AUlRpmnfkREajI53awm5egmtRbzu-I-VahlU1TxKBMjQ57Cs7Sx4Cj7Gfq6njledDhOA6J0wt7ax8T0k20GJSPlkNO3fgKOPOs8Jg1S5Fa0e2US1s_YFCIbu_4AxxhADGaMNnMP7KFPUCPfOjOqi0dilYIqvZqPCCGAyATjnlBRsujpZpNkTF8rx79WSVT1MDUOlPlnRFgyVBeXQH8l8TwnfA7_NeUUvJC32ruquVhl133JPUkFn-tKFzJdz73EKoQrZAURSM7me-sMyuEfccedpDd69-clw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی فروتن، عمو فیتیله‌ای:
این روزا وقتی دختر، پسرا میخوان باهم دوست بشن، خیلی برای همدیگه لاف میزنن!
معیار انتخابم که شده پول، قیافه، خوش گذرونی و... به نظرتون گند نزدیم به عشق و عاشقی؟
یه زمانی آدما دنبال کسی بودن که نه تنها حرفشون، بلکه سکوتشون هم بفهمه. به خودت احترام بذار و با هرکسی وارد رابطه نشو.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72079" target="_blank">📅 22:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72078">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">امیر قطر در مورد غزه:  اسرائیل به نوبه خود باید به تعهدات خود به طور کامل عمل کند: توقف قطعی عملیات، خروج از نوار غزه، لغو محاصره و ارسال بی‌قید و شرط کمک‌های بشردوستانه.  @News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72078" target="_blank">📅 21:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72077">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88614b72e8.mp4?token=avz4suPAcyHe5NSa58V-SF_SW6Kd02OSYZAEm3xdpb_O6FiQs_b4sXgjF9ER6FBJVJOGcxrkoGHKjCh8zmR9uvMQ-G7ZXO1xHq_81brNzlvzqXwIY06GYcdxqyomAzu_Xf-Fx73aNYo0UtvkqrTXfG68-WJkutvB1RXiTuMy2w9plsw7GERjVkUQLkFcNT8HWCdqb3CA3Z-EQGwsMM-D8SdsegZfxVOwi-BHRWGPYjcQZE7RHzqWawVZjNZjZy4iyAJ-wzmR3OeFoNTDHlO75BgBctNPbsgzfRA_NHeVAl3OTczmoi3o5yDRwtLmBh47Nv4IeOpakMX45t9IoqezMoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88614b72e8.mp4?token=avz4suPAcyHe5NSa58V-SF_SW6Kd02OSYZAEm3xdpb_O6FiQs_b4sXgjF9ER6FBJVJOGcxrkoGHKjCh8zmR9uvMQ-G7ZXO1xHq_81brNzlvzqXwIY06GYcdxqyomAzu_Xf-Fx73aNYo0UtvkqrTXfG68-WJkutvB1RXiTuMy2w9plsw7GERjVkUQLkFcNT8HWCdqb3CA3Z-EQGwsMM-D8SdsegZfxVOwi-BHRWGPYjcQZE7RHzqWawVZjNZjZy4iyAJ-wzmR3OeFoNTDHlO75BgBctNPbsgzfRA_NHeVAl3OTczmoi3o5yDRwtLmBh47Nv4IeOpakMX45t9IoqezMoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قطر در مورد غزه:
اسرائیل به نوبه خود باید به تعهدات خود به طور کامل عمل کند:
توقف قطعی عملیات، خروج از نوار غزه، لغو محاصره و ارسال بی‌قید و شرط کمک‌های بشردوستانه.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72077" target="_blank">📅 21:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72076">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9803dc4ebc.mp4?token=E-Ciyk5MZJDbK17xL4Fhv5KuyQHa_zsnjVr7vbDYkxvaA7rdbag3SA7HavpKmApurrFctw78n-1PplqbZOC7_XNZjuXvWC8wBpPflKHIUHZMEgFygbnV64pcb7yr6Ng-lfBjyUOm-yUnDLcakSJB8DsnhYcXP2dLUhHb54VL5jXlSZsSf_Guz-I4WcviSFcmtqYZWW7Oa5QaP40fclX3vLemWN6eRJMiA2e4U5IwxzqbK-ox1pT8h7XZjUTwpV2ktp1tOodiWHgVRV8veeKvvXEQa1YRbpDa90oxoRs3pxNTam5jZBg6UvharCdrikGdxx3t9lMK0VjEh28bWgJGtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9803dc4ebc.mp4?token=E-Ciyk5MZJDbK17xL4Fhv5KuyQHa_zsnjVr7vbDYkxvaA7rdbag3SA7HavpKmApurrFctw78n-1PplqbZOC7_XNZjuXvWC8wBpPflKHIUHZMEgFygbnV64pcb7yr6Ng-lfBjyUOm-yUnDLcakSJB8DsnhYcXP2dLUhHb54VL5jXlSZsSf_Guz-I4WcviSFcmtqYZWW7Oa5QaP40fclX3vLemWN6eRJMiA2e4U5IwxzqbK-ox1pT8h7XZjUTwpV2ktp1tOodiWHgVRV8veeKvvXEQa1YRbpDa90oxoRs3pxNTam5jZBg6UvharCdrikGdxx3t9lMK0VjEh28bWgJGtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها دیداری بسیار خوب و سازنده داشتند. دیدار دیگری نیز برای آینده‌ای بسیار نزدیک برنامه‌ریزی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72076" target="_blank">📅 21:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72075">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c847d96020.mp4?token=MyEBlFlotETLccJvNnBDVD4OPMN2tl0S098K8dOaz-lfmh6o30uV_hlpo-372zCbVLotf185eVuvbWzgeKrnyHQvEDfgDOejE2hlHKmZ95VUPPVE_j1kK75AdY2CBAt9wvU_CeANP6O0fPHvRRPe5rNeMtamZFfvDvKyv82abThUZGyEllRihAaslZOcz-Po0LaAh4tIbzG4EELj4ph6HRA3ZJ7Ytg9ce5gkrYaU3gHoQCJgbl0aTKXKvc-NsD7XtiiE_zh8arWJ2EDvIUBXGsa438Ct9pGm5XRaSpU3y-NpFqp1lTri1X6jzMtGOQNsptFdzvVlk_zorBjny8riFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c847d96020.mp4?token=MyEBlFlotETLccJvNnBDVD4OPMN2tl0S098K8dOaz-lfmh6o30uV_hlpo-372zCbVLotf185eVuvbWzgeKrnyHQvEDfgDOejE2hlHKmZ95VUPPVE_j1kK75AdY2CBAt9wvU_CeANP6O0fPHvRRPe5rNeMtamZFfvDvKyv82abThUZGyEllRihAaslZOcz-Po0LaAh4tIbzG4EELj4ph6HRA3ZJ7Ytg9ce5gkrYaU3gHoQCJgbl0aTKXKvc-NsD7XtiiE_zh8arWJ2EDvIUBXGsa438Ct9pGm5XRaSpU3y-NpFqp1lTri1X6jzMtGOQNsptFdzvVlk_zorBjny8riFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
امروز، حدود یک ساعت پیش، گفتگویی انجام شد. گفتگو بسیار خوب پیش رفت و یک ساعت پیش به پایان رسید.
این نشستی بود که سه ساعت به طول انجامید.
مسئله، عظمت — یا عظمتِ بالقوه — و یا نابودی است.
در یک حالت، صحبت از نابودی است؛ و گزینه دیگر، عظمتِ بالقوه است. [ایران] می‌تواند کشوری بزرگ باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72075" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72074">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e59383b3.mp4?token=uJdKmrFX1eE1JMyzeaY8Ap1yJYY4192uF-4yqypQwQN1xBlpnQMwEuHSAWJkrTOTGjZNrGYdj2UbU0l3MNw7PmtJAgtdte7A33LyzBdWrtpVgRZ1Hh23RuAipygeU0zC0x13CMqlbQ2shdaVdGaETT_1X9Jl2f08b5CGdI2xKMHdBZe8WGD3tWE1qaITSMPQ_czd5e__s0Z0qxDojmfS0y83K8fl-fkzEJASpsT8svlyzkgmKTJvNvGGZAR3un54YpBFvIMwrko0Mo0mWChx5G446Put9F-_31ZAiPlbvz2J9fZjebqstuuIC0djIH6qCsL0H6UOtegg_sF_dbhchQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e59383b3.mp4?token=uJdKmrFX1eE1JMyzeaY8Ap1yJYY4192uF-4yqypQwQN1xBlpnQMwEuHSAWJkrTOTGjZNrGYdj2UbU0l3MNw7PmtJAgtdte7A33LyzBdWrtpVgRZ1Hh23RuAipygeU0zC0x13CMqlbQ2shdaVdGaETT_1X9Jl2f08b5CGdI2xKMHdBZe8WGD3tWE1qaITSMPQ_czd5e__s0Z0qxDojmfS0y83K8fl-fkzEJASpsT8svlyzkgmKTJvNvGGZAR3un54YpBFvIMwrko0Mo0mWChx5G446Put9F-_31ZAiPlbvz2J9fZjebqstuuIC0djIH6qCsL0H6UOtegg_sF_dbhchQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به گفته خانم دکتر؛
مردهایی که به‌طور مداوم رابطه جنسی دارن، طول عمرشون تا 50 درصد افزایش پیدا می‌کنه و همچنین خطر ابتلا به بیماری‌های قلبی هم تا 45 درصد کاهش پیدا می‌کنه.
-در زنان هم باعث میشه سرطان سینه و کیست تخمدان نگیرین.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72074" target="_blank">📅 21:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72073">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc4e3a7b84.mp4?token=c8WaDN7SzbvjuqAoo9TFUJPqOzxhf93LGnMLzFieVi_CBPfuL8JIml1yiNmvKruc5_3xBB-_KlLuSjuDPNEjoUlUNGXskLByoIHdKXl9VwlbOHq6pZXqqbnreJD_7WZ9fh7QNTNzoVyCWcMAGghf0rQ5-KkNSeVP_ArnsEOgafr54qFarzgo6m0A0N8mHkGmU-x-WB0FQH3eSTfnRlqcgzNA5c5IandPnSVd7ExIDIjbhrTQ_Pf7LOLwuEcCg9oZLodX_NEcf535BMZXzJl5_wGiv5YE5VoQUFk8M8_q89dt-bwYwQsZWEWL8aIjQY0v5_9r3NtZ1Hx91CqXoVB2GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc4e3a7b84.mp4?token=c8WaDN7SzbvjuqAoo9TFUJPqOzxhf93LGnMLzFieVi_CBPfuL8JIml1yiNmvKruc5_3xBB-_KlLuSjuDPNEjoUlUNGXskLByoIHdKXl9VwlbOHq6pZXqqbnreJD_7WZ9fh7QNTNzoVyCWcMAGghf0rQ5-KkNSeVP_ArnsEOgafr54qFarzgo6m0A0N8mHkGmU-x-WB0FQH3eSTfnRlqcgzNA5c5IandPnSVd7ExIDIjbhrTQ_Pf7LOLwuEcCg9oZLodX_NEcf535BMZXzJl5_wGiv5YE5VoQUFk8M8_q89dt-bwYwQsZWEWL8aIjQY0v5_9r3NtZ1Hx91CqXoVB2GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: بانوی اول ما کجاست؟ یک جایی همین اطراف است.
ملانیا:
👋
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72073" target="_blank">📅 20:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72072">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اکسیوس:
چند کشور عربی در تلاش‌اند زمینه برگزاری یک دیدار سطح‌بالا میان دونالد ترامپ و مقام‌های ایرانی را در حاشیه مجمع عمومی سازمان ملل در نیویورک فراهم کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72072" target="_blank">📅 20:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72067">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/77b06fbdcc.mp4?token=ldp9zsmyKdwvhZAUH1cgif_RMBMi3Em1G6p34xr865_l2fiq_Ik1czyUdVx0jrkpLKlx4qeO2DMG7Ga_XmGjoQnTrmJNh8HK6fDyosZ7PntyX5AhIyi6kmwyE1r2ys7hxjG__Xz4ty6qBhICQd2HSSEfOGogymGkOwaQujyLh7YH2KpkV8GBCYtrC0nuDOzO9f_i5ntQKGV2T9S6-3FdjoYITzfclxuA0OueFVYCeHXrzA9XFnLeq0P948Lf6VXD0oNXFRmrnV2J3LbvYfcd0nSDJYGXTvJkXwGQTe7Zll4psJjFblZ1Vl7alv1h13UegRHyORzG9BC4mxpkaDfh2g" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/77b06fbdcc.mp4?token=ldp9zsmyKdwvhZAUH1cgif_RMBMi3Em1G6p34xr865_l2fiq_Ik1czyUdVx0jrkpLKlx4qeO2DMG7Ga_XmGjoQnTrmJNh8HK6fDyosZ7PntyX5AhIyi6kmwyE1r2ys7hxjG__Xz4ty6qBhICQd2HSSEfOGogymGkOwaQujyLh7YH2KpkV8GBCYtrC0nuDOzO9f_i5ntQKGV2T9S6-3FdjoYITzfclxuA0OueFVYCeHXrzA9XFnLeq0P948Lf6VXD0oNXFRmrnV2J3LbvYfcd0nSDJYGXTvJkXwGQTe7Zll4psJjFblZ1Vl7alv1h13UegRHyORzG9BC4mxpkaDfh2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی در پایانه لجستیکی شرکت «نووا پوشتا» (Nova Poshta) در حومه روستای اوساتوو (Usatovo) در منطقه اودسا اوکراین، پس از حمله موشکی.
علاوه بر این، ممکن است انبارهای متعلق به شرکت‌های دیگر در آن نزدیکی نیز دچار حریق شده باشند؛ چرا که مجموعه‌ای کامل از انبارها در آن منطقه قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72067" target="_blank">📅 20:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72066">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pV5sHTo5YGQdjUZdqcpLGuJRCzHnq_ucaFzUL57Yhkbs3bn9bODeifpbZn-KIKe2_R8mK5ZEfxHyRCbcqzudegJDKBm41Bser1MQEnf8IgJ10zfmuxzEQ6uc7MlpymEGsC2N1XoHwHcemkHMg96YaS_f9Bn-e5p3ZuyDQ5Ed5_AXHVPvQEsqEHiRteNkbYQniL5tH8HJtgzo9vYZIdohavs9bkHWQcE-SnGpZBFlHKObTx3bPV58b-BqgyLOLAxOLwyOVXTi6vDwH2XRJm_fp1zSzAqXY3c0gyUkMtPKyt8J6_9veeSLXMhXwhAyNhGjkftiFHiC6M450U9U0qtjEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهزاده رضا پهلوی وارد نیویورک شده است؛ ایشان قرار است در «اجلاس کونکوردیا» سخنرانی کرده و دیدارهای خصوصی با نمایندگان دیپلماتیک کشورهای حاضر در مجمع عمومی سازمان ملل متحد داشته باشد.
با این حساب دونالد ترامپ، بنیامین نتانیاهو، مسعود پزشکیان و شاهزاده رضاپهلوی هم‌زمان توی نیویورک هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72066" target="_blank">📅 19:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72065">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فعالیت مدارس استان هرمزگان ۲ هفته مجازی شد؛
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان از مجازی شدن فعالیت آموزشی تمامی مدارس استان در همه مقاطع تحصیلی از شنبه به مدت دو هفته، با هدف صیانت از سلامت دانش‌آموزان و حفظ کیفیت فرآیند آموزشی خبر داد!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72065" target="_blank">📅 19:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72064">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">در ۲۳ سپتامبر، فعالیت تمام شرکت‌های هواپیمایی ایران در سراسر جهان متوقف خواهد شد.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72064" target="_blank">📅 19:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72063">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079b2c614f.mp4?token=L54SlORX35vPcS4Ij5QBIVEpygn40I7DNmFhRZSiK3AqL05ub-LACUVMNsHdvhlLgdzHHKn6MHB58JoKb6U7pbc-5pVqYIsoEV0KEsQq5Y7SkTd13-T8O_98pjY5Z4Svc_hnzzpUMUq0KulF44jkqfW6PcRgMy2D2nTx5elRhDZO3LFF2u19Ju6JUPWCpFKFLl2qjgDj9NPK0t5l44EmjuyszeToYQy5J_col3xF2miFeLimO-Y2L_wd2Dx0gQicLY3CWrBYjxGKA-rMCPFh6l2ILWGnVjn_QSZSlnz3nkGlgpFsYNHrzFPcFl_7g9h-Q4LvKHTIMu-0cW0OqW1mlBu1x-RFjMjNP19bfNwqc5WZrbiVwe0I280CNXDNcsfZRHRHK659L9_tGLlTzqEnS2hsUzmIDbGn0Cnhhg4eGDzKYqEsBJ6j53xqCHL20hpxsE6YFgWeqaXbmCTlCYM8JFBGYMP7uQJOZdLfQZU2RqZBwq9rjzUYdDs3wkbhZrySEL7D7mDbxJQ9sUP-qdMDCAMQVONJarktF5L-fqobF5hO20S6880FvPKo09U2KN_lHVfi7B1qrVUtvd-t7UiMmeFoyAJwiBm3t1dDEy_846r-7Ej_moh1iRR_B4M5A-bdAk-F9NpKO5j3LoLeo2QAQaVNT3P1n60xY8ZBH6MYysw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079b2c614f.mp4?token=L54SlORX35vPcS4Ij5QBIVEpygn40I7DNmFhRZSiK3AqL05ub-LACUVMNsHdvhlLgdzHHKn6MHB58JoKb6U7pbc-5pVqYIsoEV0KEsQq5Y7SkTd13-T8O_98pjY5Z4Svc_hnzzpUMUq0KulF44jkqfW6PcRgMy2D2nTx5elRhDZO3LFF2u19Ju6JUPWCpFKFLl2qjgDj9NPK0t5l44EmjuyszeToYQy5J_col3xF2miFeLimO-Y2L_wd2Dx0gQicLY3CWrBYjxGKA-rMCPFh6l2ILWGnVjn_QSZSlnz3nkGlgpFsYNHrzFPcFl_7g9h-Q4LvKHTIMu-0cW0OqW1mlBu1x-RFjMjNP19bfNwqc5WZrbiVwe0I280CNXDNcsfZRHRHK659L9_tGLlTzqEnS2hsUzmIDbGn0Cnhhg4eGDzKYqEsBJ6j53xqCHL20hpxsE6YFgWeqaXbmCTlCYM8JFBGYMP7uQJOZdLfQZU2RqZBwq9rjzUYdDs3wkbhZrySEL7D7mDbxJQ9sUP-qdMDCAMQVONJarktF5L-fqobF5hO20S6880FvPKo09U2KN_lHVfi7B1qrVUtvd-t7UiMmeFoyAJwiBm3t1dDEy_846r-7Ej_moh1iRR_B4M5A-bdAk-F9NpKO5j3LoLeo2QAQaVNT3P1n60xY8ZBH6MYysw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر ترامپ درباره هوش مصنوعی:
هر کس در حوزه هوش مصنوعی پیروز شود — باید این نکته را به خاطر داشته باشید — و حالا می‌گویم هر کس در حوزه «هوش برتر» (SI) پیروز شود، برنده نهایی است.
آن‌ها همان گروهی هستند که پیروز می‌شوند.
و ما در حال حاضر با اختلاف زیادی نسبت به چین و سایر کشورها پیشتاز هستیم. ما این وضعیت را حفظ خواهیم کرد؛ مسیری بسیار مستقیم و موضعی بسیار قدرتمند را در پیش خواهیم گرفت.
من نمی‌خواهم مانع رشد پدیده‌ای شوم که ابعاد آن از انقلاب صنعتی هم فراتر خواهد رفت.
بسیاری می‌گویند این تحول حتی از انقلاب صنعتی یا خودِ اینترنت هم بزرگ‌تر خواهد بود. و ما بسیار محتاط عمل خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72063" target="_blank">📅 18:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72062">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36fc0e287a.mp4?token=l7YZn_djs_hNlXMlQ1YvetMSP0Hanvep3d-U7phrYcJzzfSxMrqmH6Ngi7Ka5G2XjldqO3ZioDbHoeTEeYje_l4_ukm2PB9EYXy9vW9sqLcoUrqnWtFjnxYL_ksXa10_3xVxT_v68uHo-OGx3BZxLaYfjO3DZnBzWu2tStZz8932z51O8KseOngoiVgmo-XPijcCvopn0WOZG-NuoVGgUwveN3jzU3b-ljdfAaevfBmjJbYNlHu2F3kCtd-o-ZMOzu7UmNJ1kM6lyZ7g7QE-Z-ugSTJ-NsOZxLwAs1-MeQWhkSjk1cNQNywBWOxjaa3NTKH2SlqEwWq26w-w8sAPS71gFofDyR4AU2NiH5YnEHnf_0-mCw8VOItrKfkgkfR1dpX-KPoLdsqlr_Fy3TvQH9PUOYIPlJ10YvP0V1ojQbhI1zSooucTDV5XHbc84p0KXXeFUfL9IEnDwfe-x4ykzVmRfUbbCMIhMHqAGuDJ7xE9NSlZeJ4x0HnvYaJeoRYO9nhuwdbgWf0Y6ulHmPm31II04j7SgnxC4zVJZQMcn9AOZkoVY70syZGnHePyO5coBTSJfYObB_m9gu0gGrEX9lI44YIfGFM_kS59xp8vp7HRraLsLSX-oS6BQbBuTysj2l9PpuN6x7SnWoe2e6fzE-Ofu7ygsEFEkvjkhC_XiBY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36fc0e287a.mp4?token=l7YZn_djs_hNlXMlQ1YvetMSP0Hanvep3d-U7phrYcJzzfSxMrqmH6Ngi7Ka5G2XjldqO3ZioDbHoeTEeYje_l4_ukm2PB9EYXy9vW9sqLcoUrqnWtFjnxYL_ksXa10_3xVxT_v68uHo-OGx3BZxLaYfjO3DZnBzWu2tStZz8932z51O8KseOngoiVgmo-XPijcCvopn0WOZG-NuoVGgUwveN3jzU3b-ljdfAaevfBmjJbYNlHu2F3kCtd-o-ZMOzu7UmNJ1kM6lyZ7g7QE-Z-ugSTJ-NsOZxLwAs1-MeQWhkSjk1cNQNywBWOxjaa3NTKH2SlqEwWq26w-w8sAPS71gFofDyR4AU2NiH5YnEHnf_0-mCw8VOItrKfkgkfR1dpX-KPoLdsqlr_Fy3TvQH9PUOYIPlJ10YvP0V1ojQbhI1zSooucTDV5XHbc84p0KXXeFUfL9IEnDwfe-x4ykzVmRfUbbCMIhMHqAGuDJ7xE9NSlZeJ4x0HnvYaJeoRYO9nhuwdbgWf0Y6ulHmPm31II04j7SgnxC4zVJZQMcn9AOZkoVY70syZGnHePyO5coBTSJfYObB_m9gu0gGrEX9lI44YIfGFM_kS59xp8vp7HRraLsLSX-oS6BQbBuTysj2l9PpuN6x7SnWoe2e6fzE-Ofu7ygsEFEkvjkhC_XiBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر ترامپ درباره هوش مصنوعی:
از این پس، تمام اسناد ایالات متحده — و به امید خدا اسناد سراسر جهان — تغییر خواهند کرد تا به جای واژه «مصنوعی» (Artificial)، از اصطلاح بسیار دقیق‌ترِ «اَبَر» (Super) استفاده شود.
به عبارت دیگر، به دنیای جدید «اَبَر-هوش» (Superintelligence) یا همان SI خوش آمدید.
باید دید این ایده چه بازخوردی خواهد داشت؛ هرچه باشد، خیلی بهتر به نظر می‌رسد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72062" target="_blank">📅 18:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72061">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6100a5cc1d.mp4?token=nOZEcJorciU1FL7suYQobLLzxoRFYr6lfuffIiG27omWxwSXkiYKVPHmFBFooPEBO2zzxkWTtQJ4uSMJQzLiWh5C_Jjs395W0E05SElxvUWp0X19czoOwkKY_FMJcPi4R6gR1QR6xqF0hR_oPhqX1CSnpwDLY4w6DN34CDh3UDHuOrs4zz_baBBSxOhxWh3W_ybc5te9jGFdM2GFk1BYVNfjcQa9FC3a3e_TGz4Sn_12BvOXXIlyjmLOpUqVdN-XYIVFLF1d-qiYNYbuwaCP7SXr3y82JqFuMFyGY3aE6mQASey6_IENkKJJE-bBM3RsGhCkVVnoEskoqmma1GA_Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6100a5cc1d.mp4?token=nOZEcJorciU1FL7suYQobLLzxoRFYr6lfuffIiG27omWxwSXkiYKVPHmFBFooPEBO2zzxkWTtQJ4uSMJQzLiWh5C_Jjs395W0E05SElxvUWp0X19czoOwkKY_FMJcPi4R6gR1QR6xqF0hR_oPhqX1CSnpwDLY4w6DN34CDh3UDHuOrs4zz_baBBSxOhxWh3W_ybc5te9jGFdM2GFk1BYVNfjcQa9FC3a3e_TGz4Sn_12BvOXXIlyjmLOpUqVdN-XYIVFLF1d-qiYNYbuwaCP7SXr3y82JqFuMFyGY3aE6mQASey6_IENkKJJE-bBM3RsGhCkVVnoEskoqmma1GA_Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ نام «هوش مصنوعی» (AI) را به «اَبَر‌هوش» (SI) تغییر می‌دهد.
او می‌گوید استفاده از واژه «مصنوعی» باعث می‌شود که هوش، «ساختگی» به نظر برسد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72061" target="_blank">📅 18:39 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
