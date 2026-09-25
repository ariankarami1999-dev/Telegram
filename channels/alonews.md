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
<img src="https://cdn4.telesco.pe/file/jBi5S9davFQ3OZbsy6ezOQHvkkB_7_q58CsS9y4LcnZYjfJr66v6ioNHBi1fXKPEyIaN0TVoKTxgtYqzaNpzGCjuaSnrEQhGFHMDOkK9p-WD9GR6eWXvIfHXVymADfFQRKiz80Va4QscDO7D5jdtezieTOm-VqE3_QSpe4yiL_w4-Zsys2n3Tt5h5H3qGTCbT6Al_cMAKVa36xk64h4XuoZluQ16ptBktPJy5ZRFaefDsRoNH5h25g8Pt_tpqKSE7X6Elr9UfurzN133uv6zbGeeMwiCJJnr2j1m-msDpW_EPCe1YDYLv8A-Pn0tj36hYwQZMJmMI3aWOhoo9x6WZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.02M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 15:32:00</div>
<hr>

<div class="tg-post" id="msg-149345">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">📌
دلار امریکا در تایم فریم روزانه و هفتگی کاملا ساختار صعودی دارد
🕯
🔔
بعد از شکست سقف کانال صعودی در صورت تثبیت میتواند تا ۲۹۰ هزار تومن صعود کند !</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/alonews/149345" target="_blank">📅 15:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149344">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqdTSGHUdQ_quWOCx1emSXZ7u7_qckIi_j126AlNsMcW6MMa1MVvnUxJMpJDGJTPN8AzLwg45xnvxB0iwIHIHKhfbYYJmYqmPo_27VwkCRazoL_O3fYnNCOizlBOWOiZrQ1mkWdkidwX1W10ASlL7VpUZWJ14O6PF_bMoWQPkhDQ-NTsAD8B8kn9JRZmF_gDSGIVHYxGfmzOZ_LfiBUq4cfvHiDbX7ku6pxP9xVhGB4S3eCZ7Q7y8Fj1ra9FES0PYzMaH01_UF3Z8LKgoUAkWRMzeotBhjOxmjI19K8C4ZAbznT2GZ7eqan05YrKCp8xMlLmB5N_Tsq3mVSMJ591qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل اعلام کرد که یک موشک رهگیری را به سمت یک "هدف هوایی مشکوک" شلیک کرده است که در آسمان جنوب لبنان شناسایی شده بود، منطقه‌ای که نیروهای اسرائیلی در آن حضور دارند.
🔴
نیروی نظامی در حال بررسی این حادثه است. هیچ آژیر خطر در شمال اسرائیل به صدا در نیامد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/149344" target="_blank">📅 15:16 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149343">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
سی‌ان‌ان: براساس ارزیابی‌های اطلاعاتی آمریکا ارائه تصاویر ماهواره‌ای و پشتیبانی اطلاعاتی چین به ایران کمک کرده تا کشتی‌ها را در تنگه هرمز تهدید کند و حملات دقیق‌تری را علیه پایگاه‌های آمریکا در خاورمیانه انجام دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/149343" target="_blank">📅 15:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149342">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac39b5acea.mp4?token=jPg1ICyq39sXaSLrdZPXrBTdv3D-wJ96vIIEypc4Q-sonccNgPmxfcXPLzgseIcGVZPMC1rzK9JVLi11KCUxPg7F4SRYcGAjtTIoCrf_YfeJZ0mRI0czlGDe3ajhgwFz7VsJxIdQBggPGzichI7Mvt7hrmCa1yTGuJ-hnGUZ77NSDb18y50NteMLc0wqbNinypuDAqB7Bho0hNqDbGJJdcvOKBj5f0BE0472jEKF_GoQTuaRhg76T3njrbikDORQsbpmmp1J0Svi7oDmiwXOqjWFV3QGK-EBOKhP8Tx0nY9mVfSN83GxbH9MkaO_ePcDGRxX16hR54wbK-kFbm1sOKNsUsaqhAoADufT6WnCC31WBG9LzxBOhpgQ7ty9CDQavujWL5AsJEwDeWXYCYvIhUcEmia59ip8LoN5R-t5EMyTaA2pD9THdxposndAM1qtZsdZ7_wAcnvHHWNubZSGukk0ky676Bs_d-I9ZM9vLvO62Wt499assCRrr4Z_0keT7iTspN1R8Ief9U8LDIY-8KmtvbcNzcatoY9nmEPL7rVjmpxbc5En9WPNqdaFPXtwrnkZ9aecEOhTPNwdp_-RyQKJgu4605TtMSywfM4nQcWjyjDB-wr-QmLdVfdku2K58LzTonoF0U1ehRTThIQWTG-zAXz48VvVhcOMR1MRFew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac39b5acea.mp4?token=jPg1ICyq39sXaSLrdZPXrBTdv3D-wJ96vIIEypc4Q-sonccNgPmxfcXPLzgseIcGVZPMC1rzK9JVLi11KCUxPg7F4SRYcGAjtTIoCrf_YfeJZ0mRI0czlGDe3ajhgwFz7VsJxIdQBggPGzichI7Mvt7hrmCa1yTGuJ-hnGUZ77NSDb18y50NteMLc0wqbNinypuDAqB7Bho0hNqDbGJJdcvOKBj5f0BE0472jEKF_GoQTuaRhg76T3njrbikDORQsbpmmp1J0Svi7oDmiwXOqjWFV3QGK-EBOKhP8Tx0nY9mVfSN83GxbH9MkaO_ePcDGRxX16hR54wbK-kFbm1sOKNsUsaqhAoADufT6WnCC31WBG9LzxBOhpgQ7ty9CDQavujWL5AsJEwDeWXYCYvIhUcEmia59ip8LoN5R-t5EMyTaA2pD9THdxposndAM1qtZsdZ7_wAcnvHHWNubZSGukk0ky676Bs_d-I9ZM9vLvO62Wt499assCRrr4Z_0keT7iTspN1R8Ief9U8LDIY-8KmtvbcNzcatoY9nmEPL7rVjmpxbc5En9WPNqdaFPXtwrnkZ9aecEOhTPNwdp_-RyQKJgu4605TtMSywfM4nQcWjyjDB-wr-QmLdVfdku2K58LzTonoF0U1ehRTThIQWTG-zAXz48VvVhcOMR1MRFew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرهنگ زشت آمریکا بجای خمس دادن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/149342" target="_blank">📅 15:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149341">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
چقدر گفتیم از عراقیای جاکش برادر در نمیاد؟ عراق حریم هواییش رو ایران رو بسته
🔴
حالا باز بمالاش بیان بمالن
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/149341" target="_blank">📅 15:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149340">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
رئیس شرکت آرامکو: شرایط فعلی انرژی وخیم است و در بدترین وضعیت قرار دارد.
🔴
وضعیت انرژی وخیم‌تر هم خواهد شد زیرا اختلال بسیار گسترده است و تنها به یک منطقه محدود نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/149340" target="_blank">📅 14:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149339">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5xrb5nDFbN1OdyWi9r7vu-dBluBVC8Aa-ONMny9W3tJOqb2bQxAkBXfU9bIOZKWBM7UJbIBOke5xZNDSIz4GLf7Ga9xuL7XvrH70TheCpYWyq5gGsJ2P7xaiO5G6Ye5UQRLedMJqgof5AYxPUrMdT4kjjiMwRkPqJW8_SxK6hoNd8DUPQufi1U8xUg3n2grMnGYIrmWZaJy8k4W3fjPmDYZSqgOE3eSLHYfOq9x8Twkxt8V_NEYT4t1g8kjSADHS-MlopbGFmEdYc2-dUiQhcgw2ACbPeGzOf4R7t0dSrgnRjp3DsgpYS18mwLlgi7Yp49rhBsUGQzbQFblwmf-2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
مخبر: پرواز در منطقه یا برای همه آزاد است یا برای هیچ‌کس
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/alonews/149339" target="_blank">📅 14:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149338">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
امام جمعه قم : برخورد قاطع قانونی و امنیتی با بی حجاب ها ضرورت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/149338" target="_blank">📅 14:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149337">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAbjwWkmBGZVRd-Fpfhpk7ef87PJjgmkPCH_JL4TqUOsFPfAEY26vIaeMqme1LEe8A0AhXpbqo2QUniB0iZvzYwHlZXDfDpnzjyTTswxm_6jmwU_2Q-tXZRIXblKypWi2JeM8pt2hCdeq8KUIr-mLYNWY1ofroFHu9trydboZQt70lOLYwwJo6KGoQ4qq0yAcDGOb_U0DY4_aWoWoRrM57OOW3bUf8zz-RbDbNYl6AYkzX162jHQmf18zYG88yar47VK_xDnhMKQO_vLVLNVtxMkYsu_F0HV2mgqCb364lsd5n2S2m4A78K6gKsBpW9RwKkc0cqHFi6hXLFkWOeBDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعال شدن سامان پدافند هوایی در منطقه انگشت جلیل در شمال اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/149337" target="_blank">📅 14:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149336">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e88ddfa546.mp4?token=kwG6ueJ-WWAxgjWmb0Mfnb-aAbWnrqebn4HXwCu5H4XznjFsbsyQnirdDnncvLR0UPC0Q5B1r-NdQqYJI9BTzmKQyLqFoYCEVfx2_SEEXpfDggcAxuBs0JFcb1ZKGVY8Kof8QOVTMwbIMjaRT4ocRcVAC3VsDa3_7pK8DV_DP9vDWrhPU5YhCT3RoKjxVUzFMXaHj-Lk3Qgp32HvFakUvrW0B-IwJA_IgRKszIyAAKgA0XptEJFeog9vUoesS5BBszIo7dGnaloi_IwTy8FWu1SxScQh60pocWrGeP2HCsmZCtGtcdUM9Gg3Klq-1-znlcg0rNhkCQErYgYmrSWqsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e88ddfa546.mp4?token=kwG6ueJ-WWAxgjWmb0Mfnb-aAbWnrqebn4HXwCu5H4XznjFsbsyQnirdDnncvLR0UPC0Q5B1r-NdQqYJI9BTzmKQyLqFoYCEVfx2_SEEXpfDggcAxuBs0JFcb1ZKGVY8Kof8QOVTMwbIMjaRT4ocRcVAC3VsDa3_7pK8DV_DP9vDWrhPU5YhCT3RoKjxVUzFMXaHj-Lk3Qgp32HvFakUvrW0B-IwJA_IgRKszIyAAKgA0XptEJFeog9vUoesS5BBszIo7dGnaloi_IwTy8FWu1SxScQh60pocWrGeP2HCsmZCtGtcdUM9Gg3Klq-1-znlcg0rNhkCQErYgYmrSWqsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صدا و سیما : وقت حمله به فرودگاه‌ها‌ی منطقه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/149336" target="_blank">📅 14:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149335">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gT--kNQOAtNpKGD4MnSfuSAxWreq8wF7PzmAuvrLL7B22g03AU1QArkfGkGfs8MEVh5tqbQCOl5FAAfNCe4W4eCewUdNghQODUGPQbp1UH2Y-121unvfrSPj5pBI_l6cFYDLppurW3GcH2TrMSkcJi3wkzypmuoL7hXRw8O9us2SixsJWd9CKa60JGGc3aTXMpqfwvvFYP0SKr9ZOyA4__TjEejz4iwasnAqJRHGLc1H8BHtHoWOe0EupeGUcDlgjNbT4v3nME7vzgJXRydso_aKXgygRQgDsI5SZBbeUFtXTIKkf4fT5j6mXcHY8jQyXbaMiQ-O1G3sk8yrme5jxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا استاد گودرزی رو مجدد سوار ماشین کردن و بردن جلوی خونش پیاده کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/149335" target="_blank">📅 14:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149334">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 250 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/149334" target="_blank">📅 14:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149333">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70490f2ce8.mp4?token=Wnd13wlLEfBFgOHrlUs7_8rrilHvFJqudrbkNapyP5ZlcJcIZ66vcFgyoL4_DrzZWY52XcF0OL8e6oZKPgMCvkZbfm2d-5A1R60WzBTAnxxpDvPYfgSLOXIHsyJ_pxcH81hS8sUANgU9L8MBCLaLUvbCGwzkablKJKpkSh90_V9Onrn0rJnado7G9eVgAJHJLtw6eRW-t9JdIt8XC7e-d_Nntqcvqvm2hwbfYF975z7bnNqSDIL0grX_Ewf6wmolVdGbNsTOwjMm7KmZCnC0Y9-u3aGntTDPXoppBeKMyQCIeFK10avK4gF89wKtA_rBJxMVTSK5d23PHl93iuxghjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70490f2ce8.mp4?token=Wnd13wlLEfBFgOHrlUs7_8rrilHvFJqudrbkNapyP5ZlcJcIZ66vcFgyoL4_DrzZWY52XcF0OL8e6oZKPgMCvkZbfm2d-5A1R60WzBTAnxxpDvPYfgSLOXIHsyJ_pxcH81hS8sUANgU9L8MBCLaLUvbCGwzkablKJKpkSh90_V9Onrn0rJnado7G9eVgAJHJLtw6eRW-t9JdIt8XC7e-d_Nntqcvqvm2hwbfYF975z7bnNqSDIL0grX_Ewf6wmolVdGbNsTOwjMm7KmZCnC0Y9-u3aGntTDPXoppBeKMyQCIeFK10avK4gF89wKtA_rBJxMVTSK5d23PHl93iuxghjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده ایران در سازمان ملل خواستار بررسی اخراج اسرائیل از سازمان ملل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/149333" target="_blank">📅 14:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149332">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
نیروهای امنیتی پاکستان، تلاش گروه طالبان افغانستان برای نفوذ به منطقه مرزی گلستان را روز جمعه دفع کردند و چندین تن از نیروهای طالبان را به هلاکت رساندند. این خبر را خبرگزاری رویترز گزارش داد.
🔴
منابع امنیتی پاکستان اعلام کردند که درگیری‌های پراکنده همچنان ادامه دارد و نیروها در حالت آماده‌باش کامل قرار دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/149332" target="_blank">📅 14:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149331">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MITzrdF1f0M7QpdKzP25PoiLG2uJvJam8YMNE4U3ApnjzItZoyzCfTJYMrsjvkEf8dN0jj81Q_Zas2_VhAjon3EbEI0Z7tVk__sJqKnqIsOOMLNRtipcum_sQ7jsDWL1lco88OxJTP2UKGp4nGaMw5PyagmFFalhUuassAfRE-XfgitYc9z8n0EN7hiJvuMqiDqCtIAO1lyeXS22UIwfmC5DQu6UZNOdXFjGWkQDuE0K1gLgx58oPQARCrpJRQxh-P6M070E03okTECXlQ3IJwqDb21FLBFseCw82y344dq2CMLbmSYbU7yjx6V2TsBMx9rM6ZpwisDmK2u4rCdQlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای دولتی ترکیه و پاکستان در ریاض فرود می‌آیند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/149331" target="_blank">📅 14:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149330">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7D2ON0JAQY3eNpnTROAxh0oIw5xMBr9b-fiTx_wZYjgn-tnKhFZwNChqHm4VwtfGzHHz7HFFl5CYGcI-AFG6-tUJ8Earri-Vw-SULgc4pjf59J6fvqnxD5NBJRh24S214oYq-AK52k-TzE8NDgcl7FsSlduw-k2CPKGXi3mDg0QdbUa03V8m_wfDivUjr3UXP-i3CaugWXEx9kjNKZIPbLwH70jfQ1Yvtfwjg-n3MRtG857ZdSkzrT0hc81tnS-zujPBFpuXcAZX-58jlm3qMTgwFRmEhSaDP3x1qbZOn1vc0o2eBixYmM7CLXYxOWZ-i653AY0YBelZJ8mnQhkNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس اسبق فدراسیون بوکس ناطق نوری درگذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/149330" target="_blank">📅 14:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149329">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff29e8be2f.mp4?token=Qsy5BfRZws3YgxKltDIwSqoGa3xPGVib-XeS1exP1kJFHAlzVY7fTNQNO4tD-qfyk33RClKy1Hj9nrcPlsuNFTKOGSlxWPVYHZheT-CewdSEbENMHFgKriEe37ye-QhgM5y6biXAa17hCna0UmUVsZF7yPrkZJDyTiGmkFK07k3O6ZiWjrXlNUt-kcKc1CtZ8Vjp5HUXYrKrI5unQSKd3zuuNZCXxMGuuWrkdk44IABhiC_LQDvrTglJG1Ntq0NTu0VT9V1rb5oI4D-QrTcu5jeDpBKZWZr1rOCh9LzKeJe8as5XvYSml-5kcOIIE3rum46-NqFGIpvrnBKTu_wqpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff29e8be2f.mp4?token=Qsy5BfRZws3YgxKltDIwSqoGa3xPGVib-XeS1exP1kJFHAlzVY7fTNQNO4tD-qfyk33RClKy1Hj9nrcPlsuNFTKOGSlxWPVYHZheT-CewdSEbENMHFgKriEe37ye-QhgM5y6biXAa17hCna0UmUVsZF7yPrkZJDyTiGmkFK07k3O6ZiWjrXlNUt-kcKc1CtZ8Vjp5HUXYrKrI5unQSKd3zuuNZCXxMGuuWrkdk44IABhiC_LQDvrTglJG1Ntq0NTu0VT9V1rb5oI4D-QrTcu5jeDpBKZWZr1rOCh9LzKeJe8as5XvYSml-5kcOIIE3rum46-NqFGIpvrnBKTu_wqpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موج جدید افغانی‌هایی که از راه‌های سخت در حال ورود به خاک ایران هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/149329" target="_blank">📅 13:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149328">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال: میانجی‌هایی از جمله قطر در حال فشار آوردن برای برگزاری دور جدیدی از مذاکرات بین ایران و آمریکا در اوایل هفته آینده در عمان هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/149328" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149327">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
رویترز: فرودگاه‌های اربیل و سلیمانیه در عراق، پروازها به ایران و از ایران را از امروز به حالت تعلیق درآوردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/149327" target="_blank">📅 13:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149326">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a5891d8cd.mp4?token=IJ1_e3XTd4taBsV2mqkf_mb9kyLHOn53HcNoyJpK7r7vB1nR0rRcJNYfl7JVIhzAiFxlw7kKqFu2cPCGlxvuZiQ5CQTFtUJl-PtXVw9U_nrCIMJLZur9OwyOhIZbUkHuSCytfrMWGz9dDYs9YgK2dayX8m3EvuuHe8Huf5j3LLAWwzl4UkdLGsuD4VENEvbovLkaTFH_ioB1hGZkO0H0hcmtTFjmdp0M4XqLXQjKNUK8MstMs0qjX30uRegn4C5JMG_hDy1t0DD8G8YqOVESsiszgEyyY2qZ30_Khm7u5NsSSESrANNFW40g2262WcsygBUdnQAKCxh7Dbjlltd_kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a5891d8cd.mp4?token=IJ1_e3XTd4taBsV2mqkf_mb9kyLHOn53HcNoyJpK7r7vB1nR0rRcJNYfl7JVIhzAiFxlw7kKqFu2cPCGlxvuZiQ5CQTFtUJl-PtXVw9U_nrCIMJLZur9OwyOhIZbUkHuSCytfrMWGz9dDYs9YgK2dayX8m3EvuuHe8Huf5j3LLAWwzl4UkdLGsuD4VENEvbovLkaTFH_ioB1hGZkO0H0hcmtTFjmdp0M4XqLXQjKNUK8MstMs0qjX30uRegn4C5JMG_hDy1t0DD8G8YqOVESsiszgEyyY2qZ30_Khm7u5NsSSESrANNFW40g2262WcsygBUdnQAKCxh7Dbjlltd_kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تمرین ارتش آلمان  توی خیابان های هامبورگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/149326" target="_blank">📅 13:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149325">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
حذف ۵۰۰ میلیون دلار از ارز ترجیحی دارو؛ احتمال افزایش هزینه درمان
🔴
رئیس سازمان غذا و دارو از حذف ۵۰۰ میلیون دلار از منابع ارز ترجیحی دارو خبر داد.
🔴
به گفته او، کاهش این منابع می‌تواند هزینه تأمین و تولید دارو را افزایش داده و فشار بیشتری بر بیمه‌ها وارد کند؛ موضوعی که در صورت جبران نشدن، ممکن است سهم پرداختی بیماران و هزینه درمان خانوارها را افزایش دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/149325" target="_blank">📅 13:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149324">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
کرملین: پوتین و ترامپ درباره احتمال دیدار روسیه، آمریکا و اوکراین گفتگو کردند، اما هنوز جزئیات خاصی ارائه نشده است.
🔴
نشست سه جانبه آمریکا، روسیه و اوکراین به زودی برگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/149324" target="_blank">📅 13:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149323">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
صادرات نفت ایران به چین از حدود ۱ تا ۱.۵ میلیون بشکه در روز پیش از جنگ، با کاهش ۹۲ تا ۹۵ درصدی، به حدود ۸۰ هزار بشکه در روز رسیده است.
🔴
بر اساس این گزارش، پکن بخشی از نیاز نفتی خود را با واردات از عراق، امارات، برزیل و کانادا جبران می‌کند؛ موضوعی که یکی از منابع مهم درآمد ارزی تهران را تحت فشار قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/149323" target="_blank">📅 13:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149322">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">💥
💥
💥
اماده ادامه حرکت و رشد وحشتناک طلا باشید!!
💥
💥
💥
‼️
طلای گرمی 27 میلیون به زودی دیده خواهد شد !
‼️
⚠️
تحلیل ها نشان از این دارن که ساختار انس در یک فشردگی قرار گرفته و به زودی این رنج به بالا شکسته خواهد شد و طلای گرمی ۲۷ میلیون دور از انتظار نیست.  #طلا #تحلیل‌طلا</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/149322" target="_blank">📅 13:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149321">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
به گزارش بلومبرگ، تایوان یک طرح اولیه برای راه‌اندازی مجدد یکی از نیروگاه‌های هسته‌ای متوقف‌شده خود را تأیید کرده است.
🔴
این تصمیم در چارچوب بازنگری سیاست‌های انرژی تایوان و تلاش برای تقویت امنیت تأمین برق و کاهش فشار بر شبکه انرژی این جزیره مطرح شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/149321" target="_blank">📅 13:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149320">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
حمله با چاقو به دو کارشناس اورژانس ۱۱۵ شیراز حین مأموریت
🔴
دو کارشناس اورژانس ۱۱۵ شیراز بامداد امروز، سوم مهرماه، حین انجام مأموریت از سوی همراهان یک بیمار با سلاح سرد مورد حمله قرار گرفتند
🔴
در جریان این حادثه، یکی از کارشناسان از ناحیه پهلو و سر و کارشناس دیگر از ناحیه قفسه سینه و دست دچار جراحت شدید شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/149320" target="_blank">📅 13:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149319">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzmRcJ-yETmTe-EAsZonDLMLvux-p0TiuRMbw9RrNcf6xX74kzRMa7AkjsHSIJ45vOUi6NOgH27uBul2K2sZPExI79YDzF4Sr8XRNOQqbN9s3eT8kMo4xeEib5PXLJh5isazbSOGeWb6Y7vHONS8d4KF9z5BO9HCDVkTfRjjcJL276quTVH9CIELhQhU4r53Hi1fBQm9RNarHZuoXM5ZTGNLAjBiaKQwVzrXcUusrpmBsy8KwI-6O9F0wwD38sBmjkU-m2_n1UvGL2SDYVll4X1aKkIij_NGaPKbtOu9fJBnr93r97nNxj7uYNZ1l0KVF_McoaqHhNkEYke_GAT10A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فهرست کشورهایی که نمایندگان آنها، هنگام سخنرانی نتانیاهو در سازمان ملل متحد، سالن را ترک کردند
✅
@AloNewd</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/149319" target="_blank">📅 13:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149318">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سخنگوی سپاه : در صورت خطای محاسباتی دشمن از تسلیحات جدیدی استفاده خواهیم کرد که تا کنون استفاده نکردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/149318" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149317">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b29702822d.mp4?token=fgD7JGq2r0Btq4Mb9TOtsSzl9dY94dfPKoHmTOBgB6o_S1l3B1a91RuRi0BSxOL73-OvnB_UumjHhLm-Ao2Ct9o-k4R30AYnGAERJJfFMzk6tTmDkz2gdZnDBs2s-ZnRgLBERfrKB6PPCGJGd9Zp2_GpoXxM9HscEeeDRsTXeAyiYklvlwM7HwMRt7o3a8yD1O-tQ-lWGocQAkNslCyASwpJoTvds0S_m9dYj1DqnlQECeUt-os4xZS2-IjoLIjzK_LyXv9ABNwoZd0sdwf2Yh6kB4aouW_kjuHfiYYlGRz5xgxU_cuFfXOuXet8Ee1H-2GE-hiC71bCdujai0ToTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b29702822d.mp4?token=fgD7JGq2r0Btq4Mb9TOtsSzl9dY94dfPKoHmTOBgB6o_S1l3B1a91RuRi0BSxOL73-OvnB_UumjHhLm-Ao2Ct9o-k4R30AYnGAERJJfFMzk6tTmDkz2gdZnDBs2s-ZnRgLBERfrKB6PPCGJGd9Zp2_GpoXxM9HscEeeDRsTXeAyiYklvlwM7HwMRt7o3a8yD1O-tQ-lWGocQAkNslCyASwpJoTvds0S_m9dYj1DqnlQECeUt-os4xZS2-IjoLIjzK_LyXv9ABNwoZd0sdwf2Yh6kB4aouW_kjuHfiYYlGRz5xgxU_cuFfXOuXet8Ee1H-2GE-hiC71bCdujai0ToTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهدی مطهرنیا: دستاوردهای رضا شاه رو نمیشه نادیده گرفت و مرد بزرگی بود
🔴
شما تو این نیم قرن چه کردید؟ فقط بنگاه دین باز کردید و ضد دین عمل کردید
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/149317" target="_blank">📅 12:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149316">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
زلنسکی، رئیس‌جمهور اوکراین: «ترامپ در آخرین دیدارمان گفت: اوکراین مجوز تولید موشک‌های پاتریوت را دریافت خواهد کرد.»
✅
@AloNewd</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/149316" target="_blank">📅 12:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149315">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOYTx_JShe__RtKm_wrdynJ-_o_yWAGNHxZtv59uG8yrqOl7Uw4EwrpZ3MUV3hcf_HCV0VbYJlfwIyikXGyCbsUsxbxl5QIavaEPU3oo3m_UEpII5OxIlg4Rcel4rOJ4PQjhV2e7YvV4BaR3D1uj5y7Jnn800lZRCMEpOA5rcNxmwrTmL6X0Lq1kkv-ZLZJ5JxGVDMtzfuUluViqAW1724Yv4GzVOwQH5ZYcmJILnKcgnp4CoNgfz33zJtowbzbHtutc6kWGZUFzH4D2G9Q7LUz_sGUTe5-fR0nYg3InCeaDjpmM8ErvDY6zfIIsvx7npupvs55Q3j3MlQZ-lwUkXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه‌نویی بعد باخت به ازبکستان: به امت مبعوث در خیابان قبطه میخورم کاش منم الان اونجا بودم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/149315" target="_blank">📅 12:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149314">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDfwFzD4pE_6lJHTptpITBUI4F2_xHSAiBFDveHoETf3iPy9HgLtHH231p3bO5mPffhKECgp1jqm7qz_SJ21pe0DbkN3HWDX2thT2In2tjGi2QstOXoz85-9dgh613TIXKY4faPUTfzVcLZJwwCLyIKp80P87gmHUfDFjJGwauLXR59KueYHFuGX7I6vd496lnNBrQU8zmDsmsr6g_6QMYCHKX7EboTaK5ODNV2mUbOqTnxkvLu5N_ODVDdZNTt7jvHb40jcj6uYUdKFZvD3LIo0GMwZsDEgbhOBFjPR4JeYh_e2PYQS5ewQtNLYbBvBWLtf5yOfERdmJLDco0HhTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: چین پولمون رو نمیده
🔴
پ.ن: اونوقت امت معکوس میگن باید تا سانتی متر آخر تو باسن چین فرو بریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/149314" target="_blank">📅 12:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149313">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
اورشلیم پست به نقل از یک مسئول اسرائیلی: اطلاعات اسرائیل، تلاش ایران برای احیا و فعال‌سازی مجدد برنامه هسته‌ای خود در تاسیسات "کوه کلنگ" را رصد کرده است
🔴
اگر تهران از هر یک از "خطوط قرمز" عبور کند، ما مجدداً به هدف قرار دادن تاسیسات هسته‌ای و هر مکان مرتبط با آن خواهیم پرداخت، چه با مشارکت ایالات متحده و چه بدون آن."
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/149313" target="_blank">📅 12:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149312">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
درگیری‌های شدیدی بین نیروهای مسلح حوثی و نیروهای وفادار به عربستان سعودی در مناطق کوهستانی کهبوب و جبهه الأغبره، بین استان‌های تعز و لحج، رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149312" target="_blank">📅 12:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149311">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به‌بزرگی ۴ ریشتر در عمق ۸ کیلومتری، سفیددشت اصفهان را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/149311" target="_blank">📅 12:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149310">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMSpyFBW42e5jHmm-yJx5teBr0lw55-cgFF0EQR80crsUTxVTUmeqyGqVde-6SnNPe0FRcKKFaH36Lx7cU6C9Lr6vOqd3rt4ACILf91f-V8QVVwy-4pHvQzseApdxxmzRfj6KMGFCB7Tuj4FDlFNo7ecpjRK5z5f64OKO8mB-E_HKq9rFicBDo8wXrl5pvRLDqgRbyHTRVOpdEJBr9QlQuhh8S2kxEO4S1St4TH6Sao-vVZIvGvaOdebreWtcj9Cl7U7tP4D_1C-TSBLmotQBHNp31IWTT-shk_qTlxkgttHyxLPno4UYNjp5OY7_tVuVjAQZVdYR4-eTm0m6_iG6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو اندونزی این مرد ۴۵ ساله بخاطر اینکه هر روز زن همسایشون بهش میگفت چرا ازدواج نمیکنی اونو با شلیک گلوله به قتل رسوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/149310" target="_blank">📅 12:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149309">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e294a0242.mp4?token=Qfy--nBMvkLeYiFyxxKiHbeTVeNZ1CSMgBWf4QVF8PuENB0wLB1l9E5pKUcUGRTDQDNyLsFNrGxKmyI3sroHzwntsKjV8xqOvp3giOXHBin4T4Q23BwSuQPnt2gj_o9xAthGOYTVp4wrdEoHuKIczgTecQOj0T82wqYQTp35GBOaOrUGIaw3osjjFjNy3S3BOT2ug1SHSwDSx8ogxJ5LChaNgOvO4vE9lk2ZHmT2HG6eJjU3m4XyuaatgNLFsXOkQfuzX2Gn5m0CEBfN9dphF2JXzi-26C3irxSANr1o4an8RCLWVVE9pCHjbnLM4hwX0hsSr5VgvgTXW7wXQKcC3YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e294a0242.mp4?token=Qfy--nBMvkLeYiFyxxKiHbeTVeNZ1CSMgBWf4QVF8PuENB0wLB1l9E5pKUcUGRTDQDNyLsFNrGxKmyI3sroHzwntsKjV8xqOvp3giOXHBin4T4Q23BwSuQPnt2gj_o9xAthGOYTVp4wrdEoHuKIczgTecQOj0T82wqYQTp35GBOaOrUGIaw3osjjFjNy3S3BOT2ug1SHSwDSx8ogxJ5LChaNgOvO4vE9lk2ZHmT2HG6eJjU3m4XyuaatgNLFsXOkQfuzX2Gn5m0CEBfN9dphF2JXzi-26C3irxSANr1o4an8RCLWVVE9pCHjbnLM4hwX0hsSr5VgvgTXW7wXQKcC3YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یکی از دو برادر قهرمان کاراته پس از ورود به ایران
🔴
‏ مرتضی نعمتی: برای گرفتن معافیت، تظاهر به داشتن اختلالات روانی کردم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/149309" target="_blank">📅 12:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149308">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
لبنان اعلام کرد که واشنگتن وعده داده است برای ایجاد یک منطقه آزمایشی جدید در کفر تِبنیت و علی‌الطاهر فشار دیپلماتیک وارد کند و از این طرح حمایت کند.
🔴
بر اساس این طرح، نیروهای اسرائیلی از این مناطق عقب‌نشینی خواهند کرد و پس از آن، ارتش لبنان وارد منطقه شده و در آن مستقر خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/149308" target="_blank">📅 12:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149307">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2853b5ece7.mp4?token=RUGAVOEz8Te6VrSh2kZPLKYRIAlfuiPxgdSdwtfIcJkMJGRGorATrPxy1NJKLxnW6Do-Ne-8ibUsfncfAvqXXOk4btyGJF1Lyt2HnWrgvRyYLs1ce6svleftfqAKx1pyutFY6wtTqBy_SqcEjHLJTy-wTgezbNIOB4E4X3mxXLZvqJKeN3B1I0md4YAxWAefXBV0MwGkJroZaiqWvfiRg0yXZ6gzy8Daok01fVt6GkX5oG3GoslEIJQk6UaxQqa7p4zHHkVbZLdxzAR4jccOa4GBL7CQyxwoJB0PjQNeBa6PX7JhLlPmG7_G-Wobv1CUBb2XBC2PnbBuWfPhIzo5hiRp1yBiZFHNneVo9zHdpI4z2BBqI0maUnh7yi0Zhd_XKXf_kzudVwDIKGELOSB2x2Ic6PxHbaeRbGcEJljLrcRO3nYwjaMgtSOljeyhQy87RGjRAjRDWsSF1cc03jR6iOtzUhv5p4DhZqtmDbFuPe17clcIe9k9BVC18e435Ad6q1lEqx7DfTYkTOJF7jn5acwk65DDJaKftOrCGggWe86VOSIoGJRBLVmHkb95D8S6OnT0cD3qWSHxbh6_IJ5klfCDFNr2G-PwDXD6qP0fvReYt16xkzcVQZ1eINt-MOpQFZZ70AbqGq5LP9XEYpagU0nW1DOti0ZKMAyNXNOSIIs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2853b5ece7.mp4?token=RUGAVOEz8Te6VrSh2kZPLKYRIAlfuiPxgdSdwtfIcJkMJGRGorATrPxy1NJKLxnW6Do-Ne-8ibUsfncfAvqXXOk4btyGJF1Lyt2HnWrgvRyYLs1ce6svleftfqAKx1pyutFY6wtTqBy_SqcEjHLJTy-wTgezbNIOB4E4X3mxXLZvqJKeN3B1I0md4YAxWAefXBV0MwGkJroZaiqWvfiRg0yXZ6gzy8Daok01fVt6GkX5oG3GoslEIJQk6UaxQqa7p4zHHkVbZLdxzAR4jccOa4GBL7CQyxwoJB0PjQNeBa6PX7JhLlPmG7_G-Wobv1CUBb2XBC2PnbBuWfPhIzo5hiRp1yBiZFHNneVo9zHdpI4z2BBqI0maUnh7yi0Zhd_XKXf_kzudVwDIKGELOSB2x2Ic6PxHbaeRbGcEJljLrcRO3nYwjaMgtSOljeyhQy87RGjRAjRDWsSF1cc03jR6iOtzUhv5p4DhZqtmDbFuPe17clcIe9k9BVC18e435Ad6q1lEqx7DfTYkTOJF7jn5acwk65DDJaKftOrCGggWe86VOSIoGJRBLVmHkb95D8S6OnT0cD3qWSHxbh6_IJ5klfCDFNr2G-PwDXD6qP0fvReYt16xkzcVQZ1eINt-MOpQFZZ70AbqGq5LP9XEYpagU0nW1DOti0ZKMAyNXNOSIIs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
دیروز تو تهران 96امین سالگرد تاسیس پادساهی سعودی جشن گرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/149307" target="_blank">📅 12:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149306">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
یحیی Fast سخنگوی نظامی حوثی‌ها: نیروهای یمنی هدف قرار دادن سایت‌های حساس متعلق به عربستان سعودی را آغاز کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149306" target="_blank">📅 11:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149305">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/el8hRdcnwJbg9A8jo8MpXID4HWdG4VDdVZfPU8rv_YCf-ys9rIFNt1xOXxcdzHB1N9N1h0wg5DIXIQcPq1SK0-DFIG5dBoQoBS8VEBe6fQAAKnG8mSWnJovOPZD4bCZhldlMNrh-5B5g4wgtYFy3YRGr1F3-A_G1KosBNbwMuut1cp-JSh8vN3ySmdFaSNEbOI63wT7bDtYzwRfueZN9_gW10djrfCl4QvDggImIJs2pc7-P9MueeeBxCE4QXHCxawsfDQfFAQHoMRAc2FDHEoQTkgwzzp4TQI05o7NDNQ0WPe0_zHLjN-_xdzJ9kx_ksW6zWdlk-kW8cJpIeyn-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بخشایش اردستانی، نماینده مجلس: «یه خبر خوب دارم؛ موفق شدیم از کره شمالی بمب اتم بخریم و الان بمب اتم داریم! اینو یه منبع عربی بهم گفته.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/149305" target="_blank">📅 11:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149304">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
صدا و سیما: روزای خوبی تو راهه، تحمل کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/149304" target="_blank">📅 11:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149303">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وال‌استریت ژورنال: محمد بن سلمان خواستار تداوم محاصره دریایی ایران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/149303" target="_blank">📅 11:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149302">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe717fd2fe.mp4?token=Gg0ejVxHvGMh4TsS2-Vb2_x15pHJV7gruLDe3_93o59ajio7LE6rXDDeeyCuzZMIIdcjN7Z1RyUE5RokTGd4C7GEYezJS612ZlZgjjYO4JtINVjjei_fcYmDjKkWhClFECiA-SyXy7m4EWK5KvNBbz2yr8UcyvNpoLinMUmm7MGpdxt1O1fHfh6WFZ-XvZU71jytItel9hG33c_KIPNe4hHFBKbCrIUqrEFE2K3KW24a_nCkNXm8a53biVMI6Ldn3H9ijNkA5-8ppnSgMwp-E8cuWjtUomUb63PPE1wWV8t4zg5OZzOPn25_ipmSofLt3RVDgqS69VymMngQ5hb1BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe717fd2fe.mp4?token=Gg0ejVxHvGMh4TsS2-Vb2_x15pHJV7gruLDe3_93o59ajio7LE6rXDDeeyCuzZMIIdcjN7Z1RyUE5RokTGd4C7GEYezJS612ZlZgjjYO4JtINVjjei_fcYmDjKkWhClFECiA-SyXy7m4EWK5KvNBbz2yr8UcyvNpoLinMUmm7MGpdxt1O1fHfh6WFZ-XvZU71jytItel9hG33c_KIPNe4hHFBKbCrIUqrEFE2K3KW24a_nCkNXm8a53biVMI6Ldn3H9ijNkA5-8ppnSgMwp-E8cuWjtUomUb63PPE1wWV8t4zg5OZzOPn25_ipmSofLt3RVDgqS69VymMngQ5hb1BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز 25 September، روزِ فرزند دختره.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/149302" target="_blank">📅 11:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149301">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
هادی چوپان: من حکومتی نیستم و وطن پرستم، اونایی که به من حمله میکنن خائن وطنفروش هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149301" target="_blank">📅 11:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149300">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
فرودگاه بین‌المللی نجف هم اعلام کرد که از ساعت ۲ بامداد ۳ اکتبر، تمامی پروازها به مقصد ایران و از ایران به حالت تعلیق درمی‌آیند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/149300" target="_blank">📅 11:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149299">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ms9shjIbj5Eh6VCx6ouYSN_xWSUw_DZh9H0uj6X3Aun6-HotYAGUmTOsQAZvihLYp_6eKuRUkHYpXb2QUvoK7R1MUDM2gfMg5K_YST6Qqcc6wmj9PTMU7dn2UE0XQ3Vry4rsC9e87gNPGAdNGIBTuxlYgrreJdFy3mYi0uus8G2iE5Ei_bDMVJ5I_fqqOZxXsUoxVTOYjERvOPhtAF8qei1qWO-__6bK5GgSqkEhYg_gj6speMCrV00UgB1aGUPKImud971mYt5arJ9kRLr5bqedhZDHAbOPQdDtCV6y5K7-FjxHFtMNi7CRGl9ONDzDrSbbLLRcI_3WfhIDanQPEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آقای پزشکیان مگه گفته نشد که اون حرامزاده‌‌هایی که با گلوله تو ۱۸ و ۱۹ دی مردم رو کشتن عوامل موساد بودن؟ چرا از جوانان کشته شده، تو سازمان ملل نگفتید؟ اما از غزه‌ای ها که هیچ ربطی به ایران ندارند و به یه ور ملت هم‌نیستن گفتید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149299" target="_blank">📅 11:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149298">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S65kDzXex1t3pJonloYpirXSC02n167OnnTBB2ChNVSiHIV-WEx_pj05AbUCsNDicba6pB_BDq-BuSSZooxnL_K1YflU0735sYw9tf_JrygkLm_P0bbD4YQ0Q8cxuQdR5R5XiGmuozmu2AYnfIHihpbLdTl9QTEEsrnN81Pyb4IyrP3eoGJ1V_wpzNIcmcj-AAru__SR30oD-Q0sfMFFXcn7Uhvk4RDoiAjJptZTh1F87GJsdSeQduOBAEkhTM-qAUCd7j6_sL4E6hz0QsDY6zqsfizwL6KrLJoigohULkufGcP3esKGwIAHSYkgLTcSkHrJW__pZfryAV3WROyHmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هادی چوپان: من حکومتی نیستم و وطن پرستم، اونایی که به من حمله میکنن خائن وطنفروش هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/149298" target="_blank">📅 11:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149297">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YYcQoYu0mQf0XOI9NDX9WrjA15dKzvdnuMP_IrBwF1-oh5QmG6QR2SWr0peu4y4Sdn6QWCTmXX1lyn1sCZLG38yIq1dhAv5Q1-SHHW7hCxY8odNXbeeSZnbGWPB-5MrNn6i3MhJ6CkZeCRhRht-RqXeD5Btv2w1F1PiP8W2nwprPWlfSk5hF4IeGaSkFhI8Ey68q_JdrTaxi-T8UtWxrcES5PkqAtZpZuMSnvckRw25ULfMsa4KHprYv_BGVIPT-i6tDom7nZV6Fom0Xbuc7aIjXC23VDeRSy_0pqqWkChkGJPlucQ8CUGEFCdx8DvUu-dgJ0D9ZK6Mxpx5EXq4k1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خارجه اسرائیل درباره قطع روابط دیپلماتیک کلمبیا با ایران: «از کلمبیا و رهبری عبدلا اسپرئیلا، رئیس‌جمهور این کشور، به‌دلیل قطع روابط دیپلماتیک با رژیم ایران تقدیر می‌کنم.
🔴
این اقدام، موضعی روشن در برابر تروریسم، نارکوتروریسم و جاه‌طلبی‌های هسته‌ای خطرناک ایران است.
🔴
جهان آزاد باید در برابر جمهوری اسلامی متحد بایستد.
✅
@AloNwws</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/149297" target="_blank">📅 11:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149296">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
رضایی کوچی، رییس کمیسیون عمران مجلس: اگر کشورهای همسایه پروازهای ایران را محدود کنند، ما نیز پروازهای آنها را محدود خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/149296" target="_blank">📅 11:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149295">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
رئیس ستاد ارتش ترکیه راهی عربستان می‌شود
🔴
وزارت دفاع ترکیه اعلام رئیس ستاد ارتش این کشور، برای شرکت در نشست رؤسای ستاد ارتش ترکیه، عربستان و پاکستان به عربستان سعودی سفر خواهد کرد.
🔴
این نشست در چارچوب «توافق دفاع مشترک مکه» و همزمان با تشدید حملات یمن به عربستان برگزار می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149295" target="_blank">📅 11:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149294">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
رویترز: با وجود استقبال پرزرق و برق دونالد ترامپ، رئیس جمهور آمریکا از شی جین پینگ، رئیس جمهور چین، دیدار سران دو کشور هیچ نشانه‌ای از پیشرفت در مسائل حساسی مانند هوش مصنوعی، تجارت، تایوان و جنگ ایران نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149294" target="_blank">📅 11:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149293">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
یک مقام کاخ سفید: مذاکرات مثبت و سازنده‌ای از طریق میانجی‌ها در جریان است
‏
🔴
در واکنش به اظهارات عباس عراقچی، وزیر امور خارجه ایران، یک مقام کاخ سفید به CNN گفت مذاکراتی مثبت و سازنده از طریق میانجی‌ها درباره ایران در جریان است.
‏
🔴
این مقام افزود که آمریکا عجله‌ای برای دستیابی به توافق ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/149293" target="_blank">📅 11:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149292">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19e0a352e6.mp4?token=ksyJHNgvZwv71ofcDaicyqnxDPmSdxdwDaU-52d0IOcT_9mYDmHv6_WituvAHG8aoVGnVbWuXQkXAxhCPwjM_6ssbZqZugrwxq3TDsZ5Qf9OVADYQsC4ORCTYMBpsxH1eCRfpH9s7xlOBpDlidobnyBCbw1G2w2kJ6YPPedcjOOETxrm1B08M1WH4NvdOGMNiz-iwuNFRz6yr1NwaBt2JM5m1WIn_eeH173KWX2a_JLojYrfZPk-x-0GlDF3PBmQrVXz_yj2sRzNXuoVo7lHBLtqNqoUfzxtpkQvEg3YCnFW5fIDI1azB2LTIFHYL3SCUCiuxnESPJlC1PwhKNSDIiibrl62vMk5yoDdXq5oOqrwIDS-ZsC9HKESLm-OYtxbPMIEXkZZd6_0RRM0aCPdIe0KrQheH74ey6tknYGG6sqZOesNe87midpCbUd5ZiXf6iwL0gtOMP2cNcFdN0F4q9yED7cY5YU061ooBYxnzORjrXy0b2legcjiEQn_jXJH_ZaMnF24PVmZT6I9k6KkOFWePodEL4vQvOOVlFrtXm0vrfoxrMn9fiUxOeox4x9y_3zsuRIfbiFb47yrCLFZIh51ITq3_graNO0R3tMAUQ8MP6avcnujv5oZirmkE6wYGeR972qw86nQo_1dowxouIX3fLfY8OvfyW-u8Iz3_W0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19e0a352e6.mp4?token=ksyJHNgvZwv71ofcDaicyqnxDPmSdxdwDaU-52d0IOcT_9mYDmHv6_WituvAHG8aoVGnVbWuXQkXAxhCPwjM_6ssbZqZugrwxq3TDsZ5Qf9OVADYQsC4ORCTYMBpsxH1eCRfpH9s7xlOBpDlidobnyBCbw1G2w2kJ6YPPedcjOOETxrm1B08M1WH4NvdOGMNiz-iwuNFRz6yr1NwaBt2JM5m1WIn_eeH173KWX2a_JLojYrfZPk-x-0GlDF3PBmQrVXz_yj2sRzNXuoVo7lHBLtqNqoUfzxtpkQvEg3YCnFW5fIDI1azB2LTIFHYL3SCUCiuxnESPJlC1PwhKNSDIiibrl62vMk5yoDdXq5oOqrwIDS-ZsC9HKESLm-OYtxbPMIEXkZZd6_0RRM0aCPdIe0KrQheH74ey6tknYGG6sqZOesNe87midpCbUd5ZiXf6iwL0gtOMP2cNcFdN0F4q9yED7cY5YU061ooBYxnzORjrXy0b2legcjiEQn_jXJH_ZaMnF24PVmZT6I9k6KkOFWePodEL4vQvOOVlFrtXm0vrfoxrMn9fiUxOeox4x9y_3zsuRIfbiFb47yrCLFZIh51ITq3_graNO0R3tMAUQ8MP6avcnujv5oZirmkE6wYGeR972qw86nQo_1dowxouIX3fLfY8OvfyW-u8Iz3_W0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هیئت اسرائیلی در سالن سازمان ملل حضور یافت و بررسی کرد که کدام هیئت‌های دیپلماتیک در جریان سخنرانی نتانیاهو سالن را ترک کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/149292" target="_blank">📅 10:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149291">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECpreRyUX5ze-qaWn5dRwH0_8hA6sYc56RigW_z0NpSS1ute2CQBhxXBLDNt2mTxFULJZK93NLCY7hjh0omTKe8MVGYoX9hpL06R9BPjfeKpdP2YNUbUW6TDmccyugoZtooNGIJTM9ObaEj1Gd9T_YGquIyLlWgIxKfttNRQhzK1HYKzjZfVhf5daPiKiybCgd6zJBrTkJmccE6k5h2NOOPnOY-l0qy0KS3gShJuFPkUIJF_sf9moT1uVxQmrJhKKXZkQ4H2sBBoUGPoaIQ2VC0nKav8hgNl5F871YiTwTOVfCOvUNtl8k2fifTQx4WT2fvb-N6S4l5wB14DrOfcrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی به آمریکایی‌ها: ترک کردن رو خوب تمرین کنید چون باید منطقه رو ترک کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/149291" target="_blank">📅 10:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149290">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
رویترز: مفتی اعظم عربستان از نیروهای نظامی خواست برای فدا کردن جان خود در جنگ با حوثی‌ها آماده باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/149290" target="_blank">📅 10:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149289">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
وال استریت ژورنال: عربستان سعودی و امارات متحده عربی خواستار تشدید محاصره دریایی تهران شده‌اند، در حالی که قطر و عمان تلاش می‌کنند تا زمینه را برای دور جدیدی از مذاکرات بین ایالات متحده و ایران، احتمالاً این هفته در مسقط، فراهم کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149289" target="_blank">📅 10:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149288">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
معاون آزمون‌های سازمان سنجش آموزش کشور: نتایج نهایی آزمون کارشناسی ارشد اواخر مهر یا اوایل آبان اعلام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149288" target="_blank">📅 10:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149287">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcfe0a5cbf.mp4?token=mhS893I1yLT9Zru2seDMUPDio-JLW83VeLHRpUy4tbMYbT3A65oUE-1A6J2-cx980YAIGIrqq2L59r0WXorGKoVScL7FBdrbOZPGkwgVifhBAks7ueXUAxtb-97kMlhSFm7USr7Q2xQGHHK26K5GFN2WjxGv3lYbFzn_jdu3wv9roR72rIL8UVd75zG4OvjzurZtsMLLVnB5pg5-4ufqGeJH__sGrqH9beod8DFbSqzsB3HQGk6VMXKVXcCa9DimLBq4MWE6xoYboffuG2kpsZnwJ7aXuwej1C9aXJ3KoIwmT4YJGImVoh1qZxARVJ5c6aneWvkuilKDM_7BgSwnwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcfe0a5cbf.mp4?token=mhS893I1yLT9Zru2seDMUPDio-JLW83VeLHRpUy4tbMYbT3A65oUE-1A6J2-cx980YAIGIrqq2L59r0WXorGKoVScL7FBdrbOZPGkwgVifhBAks7ueXUAxtb-97kMlhSFm7USr7Q2xQGHHK26K5GFN2WjxGv3lYbFzn_jdu3wv9roR72rIL8UVd75zG4OvjzurZtsMLLVnB5pg5-4ufqGeJH__sGrqH9beod8DFbSqzsB3HQGk6VMXKVXcCa9DimLBq4MWE6xoYboffuG2kpsZnwJ7aXuwej1C9aXJ3KoIwmT4YJGImVoh1qZxARVJ5c6aneWvkuilKDM_7BgSwnwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شی جین‌پینگ خطاب به ترامپ: «دوستی میان مردم چین و آمریکا آرمانی ارزشمند و سرشار از چشم‌اندازهای امیدوارکننده است. بیایید دست در دست یکدیگر بگذاریم و شانه‌به‌شانه پیش برویم.
🔴
با هم، گل‌های زیبای دوستی چین و آمریکا را پرورش دهیم و با هم، فصل جدیدی در روابط دوستانه دو کشور رقم بزنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/149287" target="_blank">📅 10:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149286">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
هواشناسی: جمعه و شنبه برای برخی نواحی در استان‌های گیلان، مازندران و گلستان در بعضی ساعات بارش پراکنده پیش‌بینی می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149286" target="_blank">📅 09:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149285">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
رویترز: قیمت نفت خام آمریکا با ۲ درصد کاهش به ۹۲.۶۵ دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149285" target="_blank">📅 09:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149284">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ادعای بخشایش‌اردستانی: ایران از کره‌شمالی سلاح هسته‌ای خریده است
🔴
احمد بخشایش‌اردستانی، عضو کمیسیون امنیت ملی مجلس، مدعی شد شنیده است ایران از کره‌شمالی سلاح هسته‌ای خریداری کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/149284" target="_blank">📅 09:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149283">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
دیدار و گفتگوی نخست وزیر قطر با پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149283" target="_blank">📅 09:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149282">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
نیویورک‌تایمز درباره طرح ۷ روزه ایران برای پایان جنگ
🔴
نیویورک‌تایمز درباره طرح جدید و شروط ایران برای بازگشایی تنگه هرمز به سلسله گام‌های زیر اشاره کرد:
🔴
توقف تمام درگیری‌ها به مدت ۷ روز، از جمله در لبنان
🔴
آزادسازی بیش از ۱۲ میلیارد دلار از دارایی‌های مسدودشده ایران
🔴
لغو تحریم‌های نفتی ایران و محاصره دریایی
🔴
بازگشایی تنگه هرمز در روز هفتم
🔴
آغاز فوری مذاکرات جامع درباره برنامه هسته‌ای ایران، بدون انتظار ۶۰ روزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/149282" target="_blank">📅 09:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149281">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
نفتکش‌های ایرانی توقیف شده شناسایی شدند
🔴
۳ نفتکش حامل محمولۀ ۶۰۰ میلیون دلاری منتسب به ایران که به ادعای تانکر ترکرز توسط آمریکا ربوده شده‌اند، شناسایی شدند.
🔴
این سه نفتکش در اردیبهشت امسال واقع در دریای عمان ربوده شده‌اند.
🔴
بر این مبنا نفتکش مجستیک ایکس و تیفانی در سواحل شمالی برزیل هستند و نفتکش لنور به تازگی دماغۀ امید نیک را دور زده و به اقیانوس اطلس جنوبی رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/149281" target="_blank">📅 09:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149280">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
وزارت امور خارجه عربستان سعودی:
عربستان سعودی، ترکیه و پاکستان جلسه‌ای فوری بین روسای ستادهای ارتش برگزار خواهند کرد تا درباره حمایت ریاض بر اساس توافقنامه دفاع مشترک بحث و تبادل نظر کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149280" target="_blank">📅 08:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149279">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
کلمبیا روابط دیپلماتیک خود با ایران را قطع کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149279" target="_blank">📅 08:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149278">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAsUYUflsUaQV-Rjibx5gqIao6E5NuM3CgE4eS5JzespcZ7xFNJhS8-Gq7b8we9r23HaSNQ5W_r9gYx-FxCjQJXPId5TONUgL_W9CSCsRWeXkhw3QqrNESSEIHkjm_dA_opL3WTVJQ8RdMNYR-EQPjydVmDzr9dVQ6sEMSfKuRgwkQJMK0tUEdsYm5FpUsu7sn5f-NQ45_TevYwAsBdWUKpTncoxKLQ3BssKIMpNVATjsJnWMWFUjnIEpSlH_IFZ8MNZJOofevmmouocIQcKC8xs4eZH-O4j-ug6gHCgK9GH0XNwYTKnHbYS_W5G0LRSFTe4aWIsd0kNrTOsHWdrAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: اگر اقدامِ موثری برای جلوگیری از ایجاد «محاصره‌ی هوایی» بر آسمانِ اطراف ایران نشود، آمریکا وارد فازِ اخلال در «مرزهای زمینی» خواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149278" target="_blank">📅 08:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149277">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ: ما نماینده دو سیستم متفاوت با چین هستیم، اما روابط ما در بهترین حالت خود قرار دارد.
🔴
رئیس جمهور چین: ما با رئیس جمهور ترامپ در مورد تعدادی از مسائل به درک مشترکی رسیده‌ایم
🔴
در جریان سفر ترامپ به چین، ما توافق کردیم که یک رابطه سازنده و از نظر استراتژیک پایدار بین دو کشور ایجاد کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149277" target="_blank">📅 08:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149276">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ان‌بی‌سی به نقل از عراقچی: طرحی از طریق میانجی‌ها به مقام‌های آمریکایی ارائه شده که در صورت پذیرش، تنگه هرمز در پایان هفت روز باز خواهد شد و مذاکرات از سر گرفته می‌شود
🔴
این طرح می‌تواند به‌محض موافقت آمریکا آغاز شود
🔴
یکی از شروط این طرح، موافقت آمریکا با مسیر عبور دریایی از تنگه هرمز است که میان ایران و عمان بر سر آن توافق شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/149276" target="_blank">📅 08:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149274">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
بسیجی‌ها قراره امروز مانور موتوری داشته باشن تا مردم رو بترسونن
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/149274" target="_blank">📅 08:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149273">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
پزشکیان در مصاحبه با فاکس‌نیوز:
ما اورانیوم غنی‌شده با غلظت ۶۰ درصد را در چارچوب قوانین بین‌المللی و پیمان منع گسترش سلاح‌های هسته‌ای (NPT) کنار خواهیم گذاشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/149273" target="_blank">📅 07:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149272">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efefaab11b.mp4?token=sdTsFadiTPdlScWtiaJzGRxnOXbSa6XSc9CLfO3OdM5VotZMOrwL92NbzjGLInCmL6_LtjwaxhFu0xLjSpheiyfZJv4kgS3JFipRU_PlFG2xXpvMjv_-OkTGLLeZ-AHfBffZtVOw6aZdCdLyVo_FI8sZqQg5F71S3bnr_BEEDl9ujg3VL2mh1YH1PkwiPhe9NkFM3ycX5sBkfMuSaosjMP-tqcXwDNoH0wHX2AhcuMUM7ODpWzaW7ue9dWveKqzjBKBYjTDLOsJjetKB1uNKLdTDFV0EEQUGzxfkL_yflBKxtlx926efhg4DACLareBnmb_MTutU5w5iy3mCLbB-qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efefaab11b.mp4?token=sdTsFadiTPdlScWtiaJzGRxnOXbSa6XSc9CLfO3OdM5VotZMOrwL92NbzjGLInCmL6_LtjwaxhFu0xLjSpheiyfZJv4kgS3JFipRU_PlFG2xXpvMjv_-OkTGLLeZ-AHfBffZtVOw6aZdCdLyVo_FI8sZqQg5F71S3bnr_BEEDl9ujg3VL2mh1YH1PkwiPhe9NkFM3ycX5sBkfMuSaosjMP-tqcXwDNoH0wHX2AhcuMUM7ODpWzaW7ue9dWveKqzjBKBYjTDLOsJjetKB1uNKLdTDFV0EEQUGzxfkL_yflBKxtlx926efhg4DACLareBnmb_MTutU5w5iy3mCLbB-qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری فاکس‌نیوز: آژانس بین‌المللی انرژی اتمی می‌گوید شما ۴۴۰ کیلوگرم اورانیوم غنی‌شده تا سطح ۶۰ درصد در اختیار دارید. این اورانیوم کجاست؟
🔴
پزشکیان: آمریکا مدام می‌گوید ما همه‌چیز را نابود کرده‌ایم. خب، این ادعا یا درست است یا نادرست؛ کدام‌یک است؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/149272" target="_blank">📅 07:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149271">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4c8deae6.mp4?token=DdaaI0D-10_DEyvCo4sYLRAclgm_h_veXLeF5x4iWo5gyy-5OmOQggSppnSlCOFYFzXgbjNtv36MvwiDt5ISMjGfhc4RZNsfJZHQCh3i4L-qv_dmqcskpOaTmOx50a4kYOhlAS5VsgAsHzJk-7hESEzKAoRIvyyANlXeiafXcxB7zjGmHg1PZQ5Hyy4AAy7bQ4XGQH9in0laQ1IxnYMtY2Ik7TAtxbcyFe6AuPTZF4AQXM4insHwI2bTlA7UZLdlSo50l9do_FLRl8L-7lt7atwohd92gINCq0ydvJEOlej1Bz0WBNxGa6mVQAXKaZd1RjWuZI2tPD71oGv1thWbmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4c8deae6.mp4?token=DdaaI0D-10_DEyvCo4sYLRAclgm_h_veXLeF5x4iWo5gyy-5OmOQggSppnSlCOFYFzXgbjNtv36MvwiDt5ISMjGfhc4RZNsfJZHQCh3i4L-qv_dmqcskpOaTmOx50a4kYOhlAS5VsgAsHzJk-7hESEzKAoRIvyyANlXeiafXcxB7zjGmHg1PZQ5Hyy4AAy7bQ4XGQH9in0laQ1IxnYMtY2Ik7TAtxbcyFe6AuPTZF4AQXM4insHwI2bTlA7UZLdlSo50l9do_FLRl8L-7lt7atwohd92gINCq0ydvJEOlej1Bz0WBNxGa6mVQAXKaZd1RjWuZI2tPD71oGv1thWbmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادعای مسعود پزشکیان:
هر کسی که بخواهد اعتراض کند، کاملاً حق این کار را دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/149271" target="_blank">📅 07:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149270">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=Ui1ib7TAkNqdgmTM8s76Wsp5my0WWwcgzjLIl9lb1DaFA6EdxdL5h0N9H95EiQm19NYfhUKg51ymhNn_Q73sCdVnLO_Qwakas6iariR16qokOa9_BnPRfFOTTgBrBEzggXIrWqmyDNiqsDK0jArwQ3V7pCOYJT-r4_jvm0abJpopGhEm9WPj31UtU2hVz6H59BzP4A9K_m9TeDuOSs5nULyVaCqTMYKRYeAzrWuAVYO0lCoe9bgrP_JRE5Z5IojSaK3_LVN84uOYaS5ibVd3ruy7bDmaPpnFTCdDIRvNLwXBVscJzUO9A6i4lHHzWrmuU61AogUFr3ewshAFH3R1Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=Ui1ib7TAkNqdgmTM8s76Wsp5my0WWwcgzjLIl9lb1DaFA6EdxdL5h0N9H95EiQm19NYfhUKg51ymhNn_Q73sCdVnLO_Qwakas6iariR16qokOa9_BnPRfFOTTgBrBEzggXIrWqmyDNiqsDK0jArwQ3V7pCOYJT-r4_jvm0abJpopGhEm9WPj31UtU2hVz6H59BzP4A9K_m9TeDuOSs5nULyVaCqTMYKRYeAzrWuAVYO0lCoe9bgrP_JRE5Z5IojSaK3_LVN84uOYaS5ibVd3ruy7bDmaPpnFTCdDIRvNLwXBVscJzUO9A6i4lHHzWrmuU61AogUFr3ewshAFH3R1Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
پزشکیان: ما هرگز به مردم خودمان حمله نخواهیم کرد.
🔴
برت بایر از فاکس نیوز : اما شما این کار را کردید.
🔴
پزشکیان: نه، نه. چه کسی اقدامات تروریستی علیه ما انجام داد؟ چه کسی به مدارس ما حمله کرد؟
🔴
بایر: من متوجه هستم، اما در تاریخ‌های ۸ و ۹ ژانویه، شما قطعاً نیروهای امنیتی داشتید که به شهروندان ایرانی حمله کردند و آنها را کشتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/149270" target="_blank">📅 07:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149269">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPAYONET | VPN |</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcBEOeaOm7Nppf6bMP5wm2DE_OCwDYpFkEEjHgWwBAIe6POGL6i6iyjJ_Z37N-J2tWKyGnPu9BGB1fSFD3n5f-XZiySeqX_vsLOHJGd1IxcaEQt3SzUaOw5yvMv_ovwYUD5-1YslO7Jjwxsc3Hqz047c_5bCQVKJnWboKfrZHiN6_3BgUnnG7CgOqtfrVxeN4TCf7p4vAdcN-IDM-YpzU9sHw8M3LaA0vxhckfnsYzmakn_XKb17OcagH4IP9RKK9vah52Z96ENZzWSRwKxcWB5nv3fYg7daB3YjAANNUIwpr7zPweueio96HwxZzHnBG8MBM6In8U1nmAYM0f7Tnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
کانفیگ v2ray نامحدود | چند کاربره
🦋
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
📍
نامحدود _ PLUS
⚡
:
🇩🇪
🇫🇷
🇮🇹
🇸🇪
🇦🇹
🇦🇿
🇵🇱
🇹🇷
🇺🇦
🇦🇱
🇦🇩
🇫🇮
🇳🇱
🇺🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇲
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
برای اولین بار در ایران
👑
کانفیگ ها بدون تبلیغات هستن
🚫
تمامی لوکیشن ها قابل استفاده در جمنای
✅
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
☄️
مناسب شرایط جنگی و اختلالات
💬
پشتیبانی تا آخرین لحظه اشتراک
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
👾
نامحدود تک کاربره  | 79 تومان
💵
👾
نامحدود دو کاربره  | 99 تومان
💵
👾
نامحدود سه کاربره  | 119 تومان
💵
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
خرید و تست رایگان از ربات
⬇️
BOT
🤖
@Payonetvpn_bot
ID
✅
@payonet_supp
❤️
CHANNEL
🫡
@payonetvpn
🔺</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/alonews/149269" target="_blank">📅 01:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149268">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
پزشکیان: ما به هیچ وجه قصد ترور ترامپ و یا هیچ یک از اعضای خانواده‌ش رو نداشتیم و این پُرپَکانی یهودی‌هاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/149268" target="_blank">📅 01:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149267">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4218edcc4.mp4?token=ubg8lebY2zhJlAKyK_p4Z8WHr9ghTrwMD2O5chENHcd-xyc94tOXEwR7IxA1suoTQj7iNjA2uqZW2Q7fCrsqqtXNBU69_YbYei8cJiwaj1BmzHVQjPSnrLee3JaIFvME27RLcz_pgXv7cR2cnKqLmQ33MJg0f0ynXE86hrZNfKt3oY_gK6xQzWMUsil1eQldozYlEgfb90IkJT_u-HalSSMrYb6zF9vTWFlj8JBG3nUL3lxhcCR8UiKxMDDHiSc00MBrDe47vEFQoh6p_NToFf-qfMX8lp9ChjhteKoHWN3A_vRhgdLHwe605EJgND8Ztbx5ung_m6pab_Dl3kJodw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4218edcc4.mp4?token=ubg8lebY2zhJlAKyK_p4Z8WHr9ghTrwMD2O5chENHcd-xyc94tOXEwR7IxA1suoTQj7iNjA2uqZW2Q7fCrsqqtXNBU69_YbYei8cJiwaj1BmzHVQjPSnrLee3JaIFvME27RLcz_pgXv7cR2cnKqLmQ33MJg0f0ynXE86hrZNfKt3oY_gK6xQzWMUsil1eQldozYlEgfb90IkJT_u-HalSSMrYb6zF9vTWFlj8JBG3nUL3lxhcCR8UiKxMDDHiSc00MBrDe47vEFQoh6p_NToFf-qfMX8lp9ChjhteKoHWN3A_vRhgdLHwe605EJgND8Ztbx5ung_m6pab_Dl3kJodw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پدر کودک خردسال خود را به دلیل فقر به عقد یک پیرمرد دراورد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/149267" target="_blank">📅 01:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149266">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d77207c734.mp4?token=ZUG632P1v28A86zoGuQxQg1DoQyOM5p553Y67lEuuUKezSaYwdNM9zKNz6frPEjdoTNlqG3Ptb0ufDeso-OSly9Dyrf3ji9ZLa-X_u2UnhEeDDQ60XfXkdvzLd2CXKo2wp4F8zLF2P3VqpwwwdXAOw1kxZSiv86GIQKCq1nE7BoKshI-HRbHsmzYzM8iiJDBRDVQQO36e5BE9vNxJWJhCm-2rnHsPUENAtatt8yxtBre66AsaVoqZqzP7Shaiz7xNjVjcLmdSZrDXCp3lCbW3JgluLhUlWvv-zXqLWFVCQ2m_lbQ9HyRUlhHhvwdXWDf62dRWO0pwQh9duJ5lfNPEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d77207c734.mp4?token=ZUG632P1v28A86zoGuQxQg1DoQyOM5p553Y67lEuuUKezSaYwdNM9zKNz6frPEjdoTNlqG3Ptb0ufDeso-OSly9Dyrf3ji9ZLa-X_u2UnhEeDDQ60XfXkdvzLd2CXKo2wp4F8zLF2P3VqpwwwdXAOw1kxZSiv86GIQKCq1nE7BoKshI-HRbHsmzYzM8iiJDBRDVQQO36e5BE9vNxJWJhCm-2rnHsPUENAtatt8yxtBre66AsaVoqZqzP7Shaiz7xNjVjcLmdSZrDXCp3lCbW3JgluLhUlWvv-zXqLWFVCQ2m_lbQ9HyRUlhHhvwdXWDf62dRWO0pwQh9duJ5lfNPEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جررررررررر
🤣
سفیر اسرائیل رفته استارلینک رو تحویل نماینده ج.ا بده نماینده ج.ا هم عین دخترا قهر کرده و اونور رو نگاه میکنه
😂
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/alonews/149266" target="_blank">📅 01:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149265">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rprBs1BXjdSZFukA8N4bo4LjkphTmuKcFemhULfoxACCCSWlg8bWiyxvkwxrZxgKomxRv3eRyXpAmh9AkRL1I514TA7v--bXmENW1Qpty65J_4xYtlH1yQ7YQO5T72KRhwF_bLnh9Wi7KCMKGJ8TOX0D6MNYcesOzwNy0jXlFGmoFlmFpFxbcnpbk87ENymREemrJhpunw4okAP_-Tq8aq3SNVVWb6AIHwEGUQk2j64480gVx84e8_yWDVK41gLafFSLMRIrIAmLBzgppZmxRQOSTe7e1BSWyA0HrkshVOQtc8UJukk5g9C5iGuElVEakvUviP3GTFw8L9gkTXShJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: آماده هستیم تا قبل از انتخابات آمریکا، توافق را انجام دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/alonews/149265" target="_blank">📅 01:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149264">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
پزشکیان: آماده هستیم تا قبل از انتخابات آمریکا، توافق را انجام دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/alonews/149264" target="_blank">📅 01:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149263">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
فرودگاه بین‌المللی نجف در عراق، تمامی پروازهای رفت و برگشت به ایران را، از روز پنجشنبه، ۲۴ سپتامبر، تا اطلاع بعدی، لغو کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/alonews/149263" target="_blank">📅 00:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149262">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
پزشکیان به فاکس: ۷ساعت با مجتبی صحبت کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/149262" target="_blank">📅 00:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149261">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0973ebac78.mp4?token=OUxHo87Q90V-m7t46xTzvPgsVPNJAt8pDrnuzMIAChbydEJ4mbxqctXmxHra734Sdhgy9Pw9o8iylEjdtF4W4k6DG_MnyNxSEE-GqI_-Vg80WuCvQhyPDw4Aosri9exxRHbbSx8M9wuipDnEG_V88aHqoQmIizsGB1XIJxhMQFgWehPbxUmeZ7ppsbrWNChmmyZTBi_BgvMmuz5BwRN-1zGBx101opMWjRcr7TJsiq_H1hpaKzwPQCuOzjqBOaDZR2sf3fKxiEPXx89q-z1G4u9dqh2ygTIRX4finHmUKU9zon_UbRUl_COcl767lnqyvre1ScgwpbF0mu-7xlkl6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0973ebac78.mp4?token=OUxHo87Q90V-m7t46xTzvPgsVPNJAt8pDrnuzMIAChbydEJ4mbxqctXmxHra734Sdhgy9Pw9o8iylEjdtF4W4k6DG_MnyNxSEE-GqI_-Vg80WuCvQhyPDw4Aosri9exxRHbbSx8M9wuipDnEG_V88aHqoQmIizsGB1XIJxhMQFgWehPbxUmeZ7ppsbrWNChmmyZTBi_BgvMmuz5BwRN-1zGBx101opMWjRcr7TJsiq_H1hpaKzwPQCuOzjqBOaDZR2sf3fKxiEPXx89q-z1G4u9dqh2ygTIRX4finHmUKU9zon_UbRUl_COcl767lnqyvre1ScgwpbF0mu-7xlkl6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بریت بایر از فاکس‌نیوز:
چرا ویدیویی از سخنرانی رهبر معظم در پیشگاه مردم، در مورد این جنگ، یا حتی خطاب به پرزیدنت ترامپ ندیده‌ایم؟
🔴
رئیس‌جمهور پزشکیان:
خب، این فرآیندی است که در جامعه ما ایجاد شده است، یعنی فقدان امنیت که توسط اقدامات مهاجمان ایجاد شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/alonews/149261" target="_blank">📅 00:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149260">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60aba8f435.mp4?token=h06JZWWxkNQWEnN_xPttJaxnGfMFNmMrCto5HaksWJiiLcLVvf498PEM17nplnKyf95-3fWQmbZ1jUS21HVG0KmWfr2KxuFdMcUevp0fPGyh26QMKGQynKtrsSrQxLlqRabiZ_hh8maW2zhCxr2OcQNalslmn0TQ21CD5T5nntMXEK0mCbrubmFfHmlXrT6PAVU0hM1pK0rOqtjK3BwNzoDb-NmxSvKeRY3rWUMIl4TnzPAh-HWwRQYr7Ts8_qFGJzjI04Fg1yd1oYc1Hh0y_Z79SVpdBZrkrCoAchFJPJ3ARyknXgHFjt7pExqi2jTuNiTjeVma7kMXdRAH_8PTPUX22qlKGiR1PuIBozXKoJJMqn0Bbv9xx10Lv4tGpJhpOjijN2JV32xFIfVnLlQgQprqOjJDPlCef7QfIm58I8Rql4Qy5WmZGI33jJx9Ay7eIi-r-zntgTIyLEIUErd31DLc2sCGhrk_9FSayhRvhIfPk_VyDgaPlDJ1dyO-LTA1e9wF2mQDu5tfi7mJshKILOihPCE-Y8vqi3phZg8SRRfD0NwY4pULcDS3RSgVNuz3n_tMya180sm8H_gQR8TfVaKNT4krf3w_yqatdIC1ia1Z0eYc_hoezuz5keiht2Tv37j-wpwtsnUhW9FCzOonK9-EyDAaAl2ctidcSGBN0sY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60aba8f435.mp4?token=h06JZWWxkNQWEnN_xPttJaxnGfMFNmMrCto5HaksWJiiLcLVvf498PEM17nplnKyf95-3fWQmbZ1jUS21HVG0KmWfr2KxuFdMcUevp0fPGyh26QMKGQynKtrsSrQxLlqRabiZ_hh8maW2zhCxr2OcQNalslmn0TQ21CD5T5nntMXEK0mCbrubmFfHmlXrT6PAVU0hM1pK0rOqtjK3BwNzoDb-NmxSvKeRY3rWUMIl4TnzPAh-HWwRQYr7Ts8_qFGJzjI04Fg1yd1oYc1Hh0y_Z79SVpdBZrkrCoAchFJPJ3ARyknXgHFjt7pExqi2jTuNiTjeVma7kMXdRAH_8PTPUX22qlKGiR1PuIBozXKoJJMqn0Bbv9xx10Lv4tGpJhpOjijN2JV32xFIfVnLlQgQprqOjJDPlCef7QfIm58I8Rql4Qy5WmZGI33jJx9Ay7eIi-r-zntgTIyLEIUErd31DLc2sCGhrk_9FSayhRvhIfPk_VyDgaPlDJ1dyO-LTA1e9wF2mQDu5tfi7mJshKILOihPCE-Y8vqi3phZg8SRRfD0NwY4pULcDS3RSgVNuz3n_tMya180sm8H_gQR8TfVaKNT4krf3w_yqatdIC1ia1Z0eYc_hoezuz5keiht2Tv37j-wpwtsnUhW9FCzOonK9-EyDAaAl2ctidcSGBN0sY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برت بایر از فاکس‌نیوز
: آیا مجتبی خامنه‌ای سالمه؟ آیا توانایی اداره کشور رو دارد؟
🔴
رئیس‌جمهور پزشکیان
: کاملاً. به‌طور کامل.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/149260" target="_blank">📅 00:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149259">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/alonews/149259" target="_blank">📅 00:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149258">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/alonews/149258" target="_blank">📅 00:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149257">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
ان‌بی‌سی به نقل از رئیس‌جمهور ایران: دولت ما پذیرای بازرسی از تأسیسات هسته‌ای خود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/149257" target="_blank">📅 00:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149256">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
دیدار پزشکیان با خبرنگاران رسانه های  آمریکایی رویترز، آکسیوس، فاکس نیوز، وال استریت ژورنال، نیویورک تایمز، سی ان ان، سی بی اس
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/alonews/149256" target="_blank">📅 00:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149255">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc2e185a7f.mp4?token=C8cOmL39H04HJszm8ZCehELZgX4FXjdRDAu66-cSke3tMfhvmEy_zjnbqClVNUrc7FciUpPxv1zoQBjBHYPquT_BB6lJ2cESobaBEZMz0wbmhptzi2zzzLrhFFupkoHpOclMSDraB9chK2zXHszy52D1Rzqsi5neRSdMRxgbQNdCq0yljO2hgy6Odr7cRRkIr5a1WLQUuvHEDCoGJmzmQVJFnmoPGXIDRFUuCxAd9YhvOnXtF2agKygr4VtkNCU6ATG0EqFYSWmKJ9YpSbKx5trMfBhK_rw1DImaL41-b-_SeRie24Eac0K4AIZZwScbCr-MVl4Yrw7yjUe9uP8cWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc2e185a7f.mp4?token=C8cOmL39H04HJszm8ZCehELZgX4FXjdRDAu66-cSke3tMfhvmEy_zjnbqClVNUrc7FciUpPxv1zoQBjBHYPquT_BB6lJ2cESobaBEZMz0wbmhptzi2zzzLrhFFupkoHpOclMSDraB9chK2zXHszy52D1Rzqsi5neRSdMRxgbQNdCq0yljO2hgy6Odr7cRRkIr5a1WLQUuvHEDCoGJmzmQVJFnmoPGXIDRFUuCxAd9YhvOnXtF2agKygr4VtkNCU6ATG0EqFYSWmKJ9YpSbKx5trMfBhK_rw1DImaL41-b-_SeRie24Eac0K4AIZZwScbCr-MVl4Yrw7yjUe9uP8cWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش پاکستان تصاویری را منتشر کرد که نشان‌دهنده حملات آن‌ها به زیرساخت‌ها و پایگاه‌هایی بود که توسط ارتش طالبان اداره می‌شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/149255" target="_blank">📅 00:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149254">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erST_9RMW0yquf5P1yNUUn5cINF4f0WOkBrKk5Pi25vBnndZ9EkzBcxwlFSkKSSSYn798HpojkgvHfzdYCriB1B6scyNrNRSIVsmEyBLfN1-Kis13ugFdeM-irdkgk_uS5NZbfJ-mGlUGSEl2RoCtgsZ_kczMm0W9NIlOWsTLNZ45UC30rVE76S8jiMgIAk8LI6_1_E1QxZVUsGjvUWc8WvQ9WTzwVFqdEk-zYZZAZZE7mndsmXt-dQTfK2ceAfVeOts1P1j95F-Nm37HM-vd0KdJhJGXc9rJi8CvkadLnhqiwrA6Xar31fz-4DUF91uKFowzXx27HCvPIBE-yHH2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار پزشکیان با خبرنگاران رسانه های  آمریکایی رویترز، آکسیوس، فاکس نیوز، وال استریت ژورنال، نیویورک تایمز، سی ان ان، سی بی اس
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/149254" target="_blank">📅 00:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149253">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
غریب‌آبادی:
اروپا جواب جنایاتش رو می‌گیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/149253" target="_blank">📅 00:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149252">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D99wl-XaKA9U4iqkoUWcb0N4pUfTasdDEr4iEBt8zAwSwMtGCOIf8klc1n7OUczgoCGxhkEu2wGQPIHpIsnhblkzSaeix2WR9BcPPTqb-55Rzfj_fXvz70gSPgIUd_nJ_emQ-Yky-2X_fmL9KO1lCMoA7naQ0f_fKzz-WZiWMr5WKmPnT4vKf-vZxk6AB-3sgiGulOqCSL3DXgvLwxA29-XOcd0kWZLiD2kAzn5y4Fulq4z6UxutpI7X-M7Ih4sdRfAT4QJ7U-KLM-PvZEsI6MhZd8-5pCIoLipYr0JLyEqYZtlJlGK16iKdLB7P7MDBpat8VVtwfX_B-hxR59mpkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای پشتیبانی سریع (RSF) که از سوی امارات متحده عربی حمایت می‌شوند، اعلام کردند که یک پهپاد بایراکتار ساخت ترکیه را که توسط ارتش سودان در منطقه النیل آبی در سودان مورد استفاده قرار می‌گرفت، سرنگون کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/149252" target="_blank">📅 23:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149251">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb872c593e.mp4?token=L4LA9E09bu026tah9K0brQHwOW7jYtfFwTtvVvoYNUXMpTrkL_EVSEa3z4l1klskeBIJqVkEBNdjBXzXpTwAkzNmz8j48vSEQF-BfhreB4RD8fq5SLCrvsjfj0Kpb6LBoXCTOPe4SLcN5ZtgFUUZCbKwW2QS_zAqvwCup_OnMAPeFFTCGWhVpOD9dw9ImJe67-CSSa-ORhGDKXTczi4anMOfOjnJwgt_j8Ui1yZZiwCdXpBAuC4jf9ozHIGk-kQPWOPKQWXKtS1OG-GwDE0XmDVN3p1gjevHxj1pUuywuBYPaQJ0f6rs-4JLKQTGZeeXYuXW35UNipJ4DJCSPid0NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb872c593e.mp4?token=L4LA9E09bu026tah9K0brQHwOW7jYtfFwTtvVvoYNUXMpTrkL_EVSEa3z4l1klskeBIJqVkEBNdjBXzXpTwAkzNmz8j48vSEQF-BfhreB4RD8fq5SLCrvsjfj0Kpb6LBoXCTOPe4SLcN5ZtgFUUZCbKwW2QS_zAqvwCup_OnMAPeFFTCGWhVpOD9dw9ImJe67-CSSa-ORhGDKXTczi4anMOfOjnJwgt_j8Ui1yZZiwCdXpBAuC4jf9ozHIGk-kQPWOPKQWXKtS1OG-GwDE0XmDVN3p1gjevHxj1pUuywuBYPaQJ0f6rs-4JLKQTGZeeXYuXW35UNipJ4DJCSPid0NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور صربستان، وُچیچ، شخصاً در سخنرانی نتانیاهو در مجمع عمومی سازمان ملل حضور یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/149251" target="_blank">📅 23:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149250">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
امانوئل ماکرون، رئیس‌جمهور فرانسه، گفت که روسیه ممکن است در حال آماده‌سازی برای اعزام حدود 300 هزار سرباز دیگر باشد.
🔴
او این سناریو را بر اساس اطلاعاتی که از سوی سرویس‌های اطلاعاتی اروپا، آمریکا و اوکراین به اشتراک گذاشته شده، قابل اعتماد توصیف کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/149250" target="_blank">📅 23:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149249">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
رئیس‌جمهور فرانسه، مکرون، در مورد تهدید ترامپ برای ممنوع‌سازی صادرات دیزل ایالات متحده: هرگز با دونالد ترامپ تضمینی وجود ندارد. هرگز.
🔴
او یک ممنوعیت احتمالی را «فاجعه‌بار» می‌نامد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/149249" target="_blank">📅 23:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149248">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76e544f54d.mp4?token=ETzcO1Hx5k9Wv-ud9HHNzRk34g-cCjQrP3AKHtr0AbwcFpN48Bu9syQX92cryizkH_q3vBXknk6q6p7aGzdb4bcl_MIsJNTbVdesxdiJoije1D4CZC08tsnYAmujwwQpiaY9Py-5gOLHcd-SP8tOacYS0AFv1RqwJ-WloH9cZ-ZrUNBSLinErFKlFAss4I8noSmzJ4LxMbgfEpenp5mdr0TKD1lSwO_Un8g8vBbJzD_QLKZFul4FPCXx-5pjzuO0eyn5Ia5FYsMRKpzJOsJIO6E2OcqfjgkBqrxC7XOVxxav1MJlnP4DZsuolxTkWP_D_UxhuKviwQEHHLwUkFZoQXpgvVKfVmF0f7CfJwVDz71fi7k_f7KQfx2KOBjXc_NG-y0Y0VfqEAEarDEW0bI8_ruKuhl2s1WDzuHdsDE9a6V0wc9B3gn8auoe7FxAvJoAf9Xwwsih55j_cWbKUOW8Y9jFrzHm0437dOcwaRZE7z2HorodDyFS3yQUhcXph_JiRwRbLAcVJ6L6k4hnBhNLfMBbVYWem7zSIyy6b-9iczrbhQhBXZe1keiuGca0IFvSRSkVEbXQPX2qtfhriA1HDY8ICPzYpVS9e5RtF4Cr3kTp8IoPhTbV66rwcnfuPRAj3qcpoCZRaqP3DOko9G89nx9NKFOZWl463rgi5v4__Hc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76e544f54d.mp4?token=ETzcO1Hx5k9Wv-ud9HHNzRk34g-cCjQrP3AKHtr0AbwcFpN48Bu9syQX92cryizkH_q3vBXknk6q6p7aGzdb4bcl_MIsJNTbVdesxdiJoije1D4CZC08tsnYAmujwwQpiaY9Py-5gOLHcd-SP8tOacYS0AFv1RqwJ-WloH9cZ-ZrUNBSLinErFKlFAss4I8noSmzJ4LxMbgfEpenp5mdr0TKD1lSwO_Un8g8vBbJzD_QLKZFul4FPCXx-5pjzuO0eyn5Ia5FYsMRKpzJOsJIO6E2OcqfjgkBqrxC7XOVxxav1MJlnP4DZsuolxTkWP_D_UxhuKviwQEHHLwUkFZoQXpgvVKfVmF0f7CfJwVDz71fi7k_f7KQfx2KOBjXc_NG-y0Y0VfqEAEarDEW0bI8_ruKuhl2s1WDzuHdsDE9a6V0wc9B3gn8auoe7FxAvJoAf9Xwwsih55j_cWbKUOW8Y9jFrzHm0437dOcwaRZE7z2HorodDyFS3yQUhcXph_JiRwRbLAcVJ6L6k4hnBhNLfMBbVYWem7zSIyy6b-9iczrbhQhBXZe1keiuGca0IFvSRSkVEbXQPX2qtfhriA1HDY8ICPzYpVS9e5RtF4Cr3kTp8IoPhTbV66rwcnfuPRAj3qcpoCZRaqP3DOko9G89nx9NKFOZWl463rgi5v4__Hc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تاکر کارلسون: قطری‌ها به ترامپ یک هواپیما دادند. و این کار چه چیزی برایشان به ارمغان آورد؟ هیچ‌چیز.
🔴
ایالات متحده از قطر دفاع نکرد. ایالات متحده باتری‌های تاد را از خلیج فارس به اسرائیل منتقل کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/alonews/149248" target="_blank">📅 23:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149247">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5c5d8dde.mp4?token=EjJBTp2HgE1bQffD59roDg0rFdScTxgOYIJoI3etrCYD1v-qi7kBsSCjsorphbbC6cMQQyLaghxPNMDgjf6hEWRUPcKTvnySYRTcb8mccqpazr1VYK5WpxXAT1AJoXoo-PdeuicRt71vWysrPmaNI1SODVXx1-9WfytYCDWFfLj9gmhXe_axmMXeahTWDCWGM2k6heTTC1xzw2h9vl4kdkt-h2UaM79mevV9Xy-3JpVG31WmJcMhwcrIAeMkLEeLvDAXr0Q55Dk5k9sBUHNZyGLDDetiPgqdglHQPZiomG-iHX5lHdv-cjIWuVnZH1GRHaTq5C0lKw-lkaYgQIT6Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5c5d8dde.mp4?token=EjJBTp2HgE1bQffD59roDg0rFdScTxgOYIJoI3etrCYD1v-qi7kBsSCjsorphbbC6cMQQyLaghxPNMDgjf6hEWRUPcKTvnySYRTcb8mccqpazr1VYK5WpxXAT1AJoXoo-PdeuicRt71vWysrPmaNI1SODVXx1-9WfytYCDWFfLj9gmhXe_axmMXeahTWDCWGM2k6heTTC1xzw2h9vl4kdkt-h2UaM79mevV9Xy-3JpVG31WmJcMhwcrIAeMkLEeLvDAXr0Q55Dk5k9sBUHNZyGLDDetiPgqdglHQPZiomG-iHX5lHdv-cjIWuVnZH1GRHaTq5C0lKw-lkaYgQIT6Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار و گفت‌وگوی عراقچی و وزیر امور خارجه اسپانیا در حاشیه نشست مجمع عمومی سازمان ملل متحد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/149247" target="_blank">📅 23:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149246">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
گروسی: برای حل دیپلماتیک موضوع هسته‌ای ایران با همه طرف‌ها همکاری می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/149246" target="_blank">📅 23:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149245">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
بغداد: آمریکا پایگاه «ویکتوریا» را به عراق تحویل داد
🔴
تحویل این سایت، بخشی از اقدامات مربوط به پایان مأموریت ائتلاف بین‌المللی ایالات متحده در عراق است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/149245" target="_blank">📅 23:14 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
