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
<img src="https://cdn4.telesco.pe/file/qugs9vHqmldfcp9S95cqbvorrRk4umsmAm_OzXz444eBmQ-LWpEM2J54kyPZnniTfb84CN5mbw1Vd9QuZNcUV-IkwIpvQlatKJXAmrTEL_L6h4tyqRQZvinchGJNk9ZQ0h3AprpyKPACcJeOKdQhC5RDlJPSfggPkAEy4MBSUDMgFheCzAr_z9d6x5L4E91YjRu1D8VqfwmL9pIHGHc2I7QyK4nXCvQEvll8qpGQfmVr_8jHsrEgrLWKkp4UbZFSewyeO-tbVbTdDbc0PmyWBeUf4LIKDOpbSSE-4iXNGsSQTKgoZx1cMfr1S7bSQfeeDiCp2HKe287XC6X_g-TelQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 917K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 11:03:22</div>
<hr>

<div class="tg-post" id="msg-147164">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/061a97b263.mp4?token=TQQh-ygqK_TieWx2WVbW9_7F96uktNae7pfT2kvwW__siSISFJs7oerMUWePUrzhciW0zfP4-lbWPBZk5rhaPjY1jpiVErER2fpAfzvmcq2yLG4aF8sphhaSNln00wqI9uXN6OsKu4K8edQ0CSkSMUC-shFMhIN0ek0-ZiP9_GCzC5PSvLHGPqHiFxIwgWkfH-Lr7__n2aABuh3YGdvHe40wNV_RiwQ2iHqwikSMzpUdxTqRoZ7dz32SAhETyIJ0DX3mgizKM_OmAXz6cBeX5AfGVGEZZNpAEwqgphIt28csuy3k6Iz_wsc7lPho2exc04ZcpLaaLuczA9NcWVgSxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/061a97b263.mp4?token=TQQh-ygqK_TieWx2WVbW9_7F96uktNae7pfT2kvwW__siSISFJs7oerMUWePUrzhciW0zfP4-lbWPBZk5rhaPjY1jpiVErER2fpAfzvmcq2yLG4aF8sphhaSNln00wqI9uXN6OsKu4K8edQ0CSkSMUC-shFMhIN0ek0-ZiP9_GCzC5PSvLHGPqHiFxIwgWkfH-Lr7__n2aABuh3YGdvHe40wNV_RiwQ2iHqwikSMzpUdxTqRoZ7dz32SAhETyIJ0DX3mgizKM_OmAXz6cBeX5AfGVGEZZNpAEwqgphIt28csuy3k6Iz_wsc7lPho2exc04ZcpLaaLuczA9NcWVgSxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کوییک در نیشابور (خراسان رضوی ) توسط زمین بلعیده شد
🔴
در اتفاقی عجیب در خیابان فردوسی شمالی شهر نیشابور ، زمین دچار فرونشست و شکاف شد و یک خودروی سواری کوییک را بلعید
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/alonews/147164" target="_blank">📅 10:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147163">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
یدیعوت أحرونوت: از امارات خواسته شد که خبرها مبنی بر هشدار دادن این کشور به نتانیاهو در مورد عملیات ۷ اکتبر ۲۰۲۳ را تکذیب کند، اما امارات این خبر را تکذیب نکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/alonews/147163" target="_blank">📅 10:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147162">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
نیروی دریایی سپاه: اگه آمریکا مدعی کنترل تنگه هرمزه، یک شناور خودش رو تا فاصله ۱۰۰ کیلومتری نزدیک کنه ببینه میزنیمش یا نه
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/147162" target="_blank">📅 10:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147161">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmY-XxqDZALt4kbf_CnRTi-_r-Q8GHHHE-m6Pf7L7JnyWmJcSYIK6Tt04hvIXbFAa0nCL9EW6LVOUYyQvxk0U21RQWo3mk6w1xbDo6bCMv-slfhIvZMMfs0xEz4z5xLurBQHIkZeqXmWXBljY0zdX8-4tZNy8PtYcGExd8K9Q3YmPkS3As76Id-d02O3UFnG2fTji1Nu0gBg82nriPAGIaclwJgiJhH2JpPKQ3fuSICvJJHNxxMaL0dWUFfrVfd5W4BKl201c6XII-a2aaxqF8lENBR3BLN4Faqe-jh_5Qr9-AgNs6D333nDEwynWmhW8xAE6Fw2AmECXG4duKfDZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فایننشال تایمز: حوثی ها با کمک هوش مصنوعی تونستن موشک بسازن
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/147161" target="_blank">📅 10:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147160">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdQvRKSLtTaa0jRbraYv-9-YR42_v6sAciob_S1perbVsiPrl4PT41LIWrr_kWd7tjJWjtxI-DS2m84lRtt4niwYNKZZW5P5u6-iCdQLfIvHIgzvIvwh3KGe91QEqBUg82ZPjU-uB5oCuNCPPW1dgPrRn-zsrkO2uGiSH0tnX0yOfkIaajlBSn_10K0ZuvN8AP1cQtAF9f6OjaqPBKl1yXHwZnnhnmTLpUcE0sgGRC6oxFPUKZiIowVi3QUZ_SWJ53f9Fyw7fA99AvcAdjozcWhhO_vDqukvKhFoJUgLHHm2M2mppZ25TlivtZUPosPvh2OUcXyxu1r9EXKhtGN2cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال ۱۲اسرائیل: ترامپ به بن سلمان گفته مسئله شما با ایران به ما ربطی نداره و خودتون باید مشکل رو حل کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/147160" target="_blank">📅 10:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147159">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jqn-Af0m1FlGgLJL4Db0Rh6EBTvboWm3BMhxJXO_zsDOr2kakhD34gx7TfeK3O4Z_efpFnzuRF4H5p0jRhSxwUInthXkH7mc9T307qMEhJB7WG27UMExJrWRiYCVrIavqhNtJlIOKh5vzcmdZVp4Evu89fDzBNEU0LJk8CbyRbRJWzjDv0_MvOSQymio6BOg-vTytJUS1Bl9XKGtgZU6cxC_XHD-yFCMyDhlUzW1NX7ZTILN3MhF5iqYYY-kIlwHVhRpI_QyAVUfgbGrXarjsLpUSy5phFcnghCPxQ_S6xn4HMprhJxdd4Ee1gcJlQYsjT8wJMuSilIt1EdSb-r4ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ:از شروع جنگ علیه ایران درآمد روزانه سوپر تانکرها از ۲۱۸ هزار دلار به ۷۸۶ هزار دلار رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/147159" target="_blank">📅 10:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147158">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c022f89c72.mp4?token=njWddFmZMPx6ypGwTUC4KGvreCbqCjk7jQio83-f1rjbFHA8DVflFTs82WVBfdeXcVE5p-9lG43viC22LJxOA09GXgsHZrUxnRFM-rRCD4o9KXy4YtnB-LOZxqHphu4smFWn1Lhjr9RQYLehyG-ndJh1KtmFXogy607K-f0hlq8g4jH04hCTctXNzyWH5xAzxcOzyCaeCbmTOTrLdtJHnnVxC6hSN01Ol-pqYeeYsHcnvfY12PzqvhOks-T2f1CnFVEi5wsUtE2iPG6AEx5PLhnj22Oe92aVoyHwaR0oZZF4s81kq7Kx1www8bvJQu8MOrJlewCk7W42rnPnO-IlU7cqZaHopG39FgJFfheF3J6cI7bLkXsPqBMZwfukuNIT9ZOGsMHLmAbX7jfc0ClGgfQTrcOhk26IZ4c63d6pmZzUDpdWNFsV60uAkW3ClpcEP0vm2GpYxaaeYF3bFomF1P0juvzOyFGwUfNE3N19sM5GFUJVZ002nHinMW_vq-v-WC5hckN_3gVcbakceoVg2cB1z9qLxt5J_MOYlcQujAidwfstfc3P8XK78xw9pp--MEDg5xvkDlztzx0pFI7wOUZqaaRKr7BUhhddrLvvWlowcg19FRXZSpXckYSEXcvVHqjf2llmvlY1g41nbEpr2yEs2EiIIfuMcsS9NngjjuY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c022f89c72.mp4?token=njWddFmZMPx6ypGwTUC4KGvreCbqCjk7jQio83-f1rjbFHA8DVflFTs82WVBfdeXcVE5p-9lG43viC22LJxOA09GXgsHZrUxnRFM-rRCD4o9KXy4YtnB-LOZxqHphu4smFWn1Lhjr9RQYLehyG-ndJh1KtmFXogy607K-f0hlq8g4jH04hCTctXNzyWH5xAzxcOzyCaeCbmTOTrLdtJHnnVxC6hSN01Ol-pqYeeYsHcnvfY12PzqvhOks-T2f1CnFVEi5wsUtE2iPG6AEx5PLhnj22Oe92aVoyHwaR0oZZF4s81kq7Kx1www8bvJQu8MOrJlewCk7W42rnPnO-IlU7cqZaHopG39FgJFfheF3J6cI7bLkXsPqBMZwfukuNIT9ZOGsMHLmAbX7jfc0ClGgfQTrcOhk26IZ4c63d6pmZzUDpdWNFsV60uAkW3ClpcEP0vm2GpYxaaeYF3bFomF1P0juvzOyFGwUfNE3N19sM5GFUJVZ002nHinMW_vq-v-WC5hckN_3gVcbakceoVg2cB1z9qLxt5J_MOYlcQujAidwfstfc3P8XK78xw9pp--MEDg5xvkDlztzx0pFI7wOUZqaaRKr7BUhhddrLvvWlowcg19FRXZSpXckYSEXcvVHqjf2llmvlY1g41nbEpr2yEs2EiIIfuMcsS9NngjjuY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پخش زنده فاکس نیوز از به پرواز درآمدن جنگنده‌ها از ناو هواپیمابر یواس‌اس جورج واشینگتن در منطقه عملیاتی سنتکام
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/147158" target="_blank">📅 10:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147157">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/147157" target="_blank">📅 10:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147155">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QCEx7uOHq5YCxIdtB-cPuC4rHfoqQ7Os0Q2VXHn8lhfT9L9TvmEFx7YbfXaP6hmQbxzUWW1fbdI5srxVJ51rfAIM4TyyaYa26CG-1Com_cgSlxbEPda5G_zJkQPS7mfwDT4GbbK0fr3ePuWtCq7Eqgo2W_E4U210XTs_bAVfW8bXZWbfv3pe71PG1_JQUheGYYZfGijmbPDZvx9zB7WDDhbjQ_MqhcLkmZkdmMGrQYIZL0VbfksL2qUIsfu5lFTNJnr34hTV3zr8zHX1P8QL1xvysvhs5JoOkaSGRis98ighskH39U9T6vDj8tngXPmS8MzlmFc_fm0X--KyJgfYPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F0mKy1gG2SnNuEt81hkw4IghEocsSfuk_DmU2nZkrI0zSldmvYxzUv1I1vrD9jhT0vk7S-1WPHj3xqiZYOIaQovuv7v7rtOSaaNyoSfSuIMywYN3371KqHBcSKOOEYoYPun8-DIMSFcoJj-3zr20TInB5VR7BuZdNuqdW_aHsTNczUHDtsF7YtFKCAsSuJWjCvQJdsSQzN4-RzX-I57aTFLT6KuyVKOGzgofvHjSoel5yaB7JiCLYvnMHN2jWWgrlA6u6fYAj7CuScv2BQGmGYKmrmcyPk_X7dwF0rKL4u0fKp0GNfxZpZElLBpPKspfbkWsMw7T_oAapoinSTwbAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
مشاهداتی از هواپیماهای باری آمریکایی مدل C-5M Super Galaxy که تجهیزات را از پایگاه هوایی اینجرلیک به پایگاه سلطان در عربستان سعودی منتقل می‌کنند، ثبت شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/147155" target="_blank">📅 10:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147154">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">محدوده بهینه متناسب میشه   ۲۴۰ الی ۲۵۰ هزار تومن</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/147154" target="_blank">📅 10:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147153">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dbdf6ed674.mp4?token=GWzv5wQQLA5c4vuYw5tkZ4rGBeTZVUWBaKWzJN3r7yasaF8DJ5SrOIWCC8FravLIOLNAD_3E7PxJDWCk6jrrKrA4txNzs9RNAS7GvWGkl1yBrl9yrBPafY7xbJkiTnN_EhejafCUodC1RZMHZD_UMjgVgxPV4I6RcTZ7YB_1FH5lGsHBknaEjJoVcan8AHpkvswZZvAk8dct19qvd9xzBwcuOc88Rj0_nXPWVdbNoWP2IejT9rHuPsSOVKNnVUr4S_uK6FeBP1BqNd-dE6ifB986Y6TKWsklPaluuHZLhttNYtIB6CjuwsT2djvwY4AZA1jKV-flk48pCI9i2KjDbg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dbdf6ed674.mp4?token=GWzv5wQQLA5c4vuYw5tkZ4rGBeTZVUWBaKWzJN3r7yasaF8DJ5SrOIWCC8FravLIOLNAD_3E7PxJDWCk6jrrKrA4txNzs9RNAS7GvWGkl1yBrl9yrBPafY7xbJkiTnN_EhejafCUodC1RZMHZD_UMjgVgxPV4I6RcTZ7YB_1FH5lGsHBknaEjJoVcan8AHpkvswZZvAk8dct19qvd9xzBwcuOc88Rj0_nXPWVdbNoWP2IejT9rHuPsSOVKNnVUr4S_uK6FeBP1BqNd-dE6ifB986Y6TKWsklPaluuHZLhttNYtIB6CjuwsT2djvwY4AZA1jKV-flk48pCI9i2KjDbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروی دریایی اوکراین: یکی از شناورهای بدون‌سرنشین سطحی این کشور در دریای سیاه، یک پهپاد دریایی روسیه را منهدم کرده است؛ اوکراین این حادثه را نخستین درگیری ثبت‌شده میان دو شناور بدون‌سرنشین توصیف کرد.
🔴
مقام‌های اوکراینی گفتند این پهپاد روسی توسط شناور Sargan-3000 مجهز به یک سامانه تسلیحاتی کنترل از راه دور ۱۲.۷ میلی‌متری منهدم شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/147153" target="_blank">📅 10:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147152">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fff2b1172.mp4?token=NzlsxrVOrORQhcbKIYBUvnFfuCz-HjvRWR-xfF_78ZqdHd0fu9_kW0LN8VIpsFr_ykZLeYDOl09W5FHS9b45B0Qvv7594BbCuVgjg2W0P8C2VWAQDAg-ggkv5qxFRrI1tq8VVUTthjQ5gIqoLgPuulddrxllL7wrJQVxJpFYcIiqOMpwa0FUD1ReV_MV4rO_V5sKE87ecI64zttMtLOI63o5i4IUK0JlJnIZILe8ViN4rivBLcb5Y7GNkkLkAWykBHDhlLHwqdbhWgBpjc46FBjYaKBGxR4AVXnq_K211NJbnRU36Xw_5Z8plLfm_Z3ijZoa4dyInbCJreUyq0ulmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fff2b1172.mp4?token=NzlsxrVOrORQhcbKIYBUvnFfuCz-HjvRWR-xfF_78ZqdHd0fu9_kW0LN8VIpsFr_ykZLeYDOl09W5FHS9b45B0Qvv7594BbCuVgjg2W0P8C2VWAQDAg-ggkv5qxFRrI1tq8VVUTthjQ5gIqoLgPuulddrxllL7wrJQVxJpFYcIiqOMpwa0FUD1ReV_MV4rO_V5sKE87ecI64zttMtLOI63o5i4IUK0JlJnIZILe8ViN4rivBLcb5Y7GNkkLkAWykBHDhlLHwqdbhWgBpjc46FBjYaKBGxR4AVXnq_K211NJbnRU36Xw_5Z8plLfm_Z3ijZoa4dyInbCJreUyq0ulmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گفتگوی عراقچی با وزرای خارجه چین و روسیه در حاشیه نشست سران بریکس
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/147152" target="_blank">📅 09:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147151">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
پزشکیان: آمریکا در حال تبلیغات است؛ این فقط پروپاگانداست.
🔴
اگر ما به دنبال سلاح هسته‌ای بودیم، عضو پیمان منع گسترش سلاح‌های هسته‌ای (NPT) نمی‌شدیم. اکنون آنها به دنبال بهانه و دستاویز برای حمله به خاک ما هستند.
🔴
اینها دروغ است؛ دروغ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/147151" target="_blank">📅 09:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147150">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a4427753e.mp4?token=JMY2zgfetOieA2xb037YfpbgOujRYaC2-u8Lc15TMxeL6M-x3g18a4qiDa7UykJo6fV9l9IOdkLsb3oONIQmA5ZuM2SssDCpVFqxBz4kUknEgGtLIgddEdY32UIOdHjVttya9tATodk0iBxk0K4HYfpMWNynXLSGZbVhODdjyG6FYoSyvtIH7Hjg92uPjjY8MV3yk3DFe7mOL_ZROwzRZmv37vjwTqqMrSq1if9berWBcfyMBfmD4lo6sojhDM-_rHURDlCMkIogvEEa662h58jzhStshw11T0AbypxRBoN5RsxOpGxDwlBxI8ya2uI4lhFNt_NFJajGRPsr-439DIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a4427753e.mp4?token=JMY2zgfetOieA2xb037YfpbgOujRYaC2-u8Lc15TMxeL6M-x3g18a4qiDa7UykJo6fV9l9IOdkLsb3oONIQmA5ZuM2SssDCpVFqxBz4kUknEgGtLIgddEdY32UIOdHjVttya9tATodk0iBxk0K4HYfpMWNynXLSGZbVhODdjyG6FYoSyvtIH7Hjg92uPjjY8MV3yk3DFe7mOL_ZROwzRZmv37vjwTqqMrSq1if9berWBcfyMBfmD4lo6sojhDM-_rHURDlCMkIogvEEa662h58jzhStshw11T0AbypxRBoN5RsxOpGxDwlBxI8ya2uI4lhFNt_NFJajGRPsr-439DIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان درباره اظهارات دونالد ترامپ به تلویزیون هند گفت: ترامپ هر روز حرف متفاوتی می‌زند؛ یک روز می‌گوید می‌خواهد ایران را نابود کند و روز دیگر می‌گوید ما دوست ایران هستیم.
🔴
بنابراین واقعاً نمی‌دانیم کدام‌یک از اظهارات او را باید مبنا قرار دهیم و بر اساس کدام موضع پیش برویم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/alonews/147150" target="_blank">📅 09:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147149">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2474449779.mp4?token=EV2VKHUYZ9Zue0ERfhi4eEgJn11ffl0ddLz-qvilbtnHsBFPirx20XxsZrEI4k9pKkV6uWPEh64Vva3JCfbZDWp9qZIoRT40XaAF0f7Ofk9T1duL9BF5tu-ogR3chKI-vtBcLafyZ8PG_6Ms1VYqmldrIl04AJsUcpGMlHxbVDYXn1XJvxeQEyYoVTSdBjRdYNc8SrVudV2_0h7sGsP_UNOql1vgFSXjW9F1O8vXAHKUC4xjOdrrHEqI7xZbeY-uBBHiwZF9Qn_oRyhv6OtUECSEFbbNzmu2xBhRZ67KPn1wqEmqhL_X0CuPTDo6aCnRdcx_RGGozPk1FABUMp_8UnzRt_gpr11mbOZSBVzeOU7v7X7vVGIHt8VhYOBnp4fXHqpXiRX-x2BT-zp3QJ6KsvDe4tip-RU-9_jurIiisVKUOC18CE6Smpv2zDF0UD__BQy1yCTMfGhWRobiTFLirGoeA2NvwDo_zklwZMcVyevzPAuLMFPcN_IowU25yDAJzHaEYP7oZLKr8bSMYUToEbcdQyb5JDE8STfTiQpRIwgeB-HnB5TvDelxq3BsmdKBCd5bcxAbg6CXAMigKP9tC9TVikXCu6UKJKNyf1A7ZtipQNi9oq0TYdkx3Yj8rv7bkgtqqRjTxsCLk9JqJiZnDlvy9i9_KJoKMj4LolmZYBc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2474449779.mp4?token=EV2VKHUYZ9Zue0ERfhi4eEgJn11ffl0ddLz-qvilbtnHsBFPirx20XxsZrEI4k9pKkV6uWPEh64Vva3JCfbZDWp9qZIoRT40XaAF0f7Ofk9T1duL9BF5tu-ogR3chKI-vtBcLafyZ8PG_6Ms1VYqmldrIl04AJsUcpGMlHxbVDYXn1XJvxeQEyYoVTSdBjRdYNc8SrVudV2_0h7sGsP_UNOql1vgFSXjW9F1O8vXAHKUC4xjOdrrHEqI7xZbeY-uBBHiwZF9Qn_oRyhv6OtUECSEFbbNzmu2xBhRZ67KPn1wqEmqhL_X0CuPTDo6aCnRdcx_RGGozPk1FABUMp_8UnzRt_gpr11mbOZSBVzeOU7v7X7vVGIHt8VhYOBnp4fXHqpXiRX-x2BT-zp3QJ6KsvDe4tip-RU-9_jurIiisVKUOC18CE6Smpv2zDF0UD__BQy1yCTMfGhWRobiTFLirGoeA2NvwDo_zklwZMcVyevzPAuLMFPcN_IowU25yDAJzHaEYP7oZLKr8bSMYUToEbcdQyb5JDE8STfTiQpRIwgeB-HnB5TvDelxq3BsmdKBCd5bcxAbg6CXAMigKP9tC9TVikXCu6UKJKNyf1A7ZtipQNi9oq0TYdkx3Yj8rv7bkgtqqRjTxsCLk9JqJiZnDlvy9i9_KJoKMj4LolmZYBc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: ما با عربستان سعودی در جنگ نیستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/147149" target="_blank">📅 09:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147148">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
رسانه امنیتی عراق:  فعالیت تجاری در شلمچه از ساعت ۶ صبح دوشنبه ۱۴ سپتامبر از سر گرفته می‌شود. فعالیت تجاری در مندلی نیز از صبح سه‌شنبه ۱۵ سپتامبر و در الشیب از صبح پنجشنبه ۱۷ سپتامبر آغاز خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/147148" target="_blank">📅 09:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147147">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سخنگوی هیئت رئیسه مجلس: خروج از ان‌پی‌تی و تجدید نظر در دکترین هسته‌ای، آمریکا را سر جایش می‌نشاند؛ این امر کاملا سهل‌الوصول است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/147147" target="_blank">📅 09:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147146">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
آنتروپیک در گزارشی تازه درباره تهدیدهای رو‌به‌ظهور امنیت ملی مدعی شد که ایران از مدل‌های هوش مصنوعی توسعه‌یافته در آمریکا برای هدف‌ گرفتن کشتی‌های نیروی دریایی آمریکا در خاورمیانه استفاده کرده است.
🔴
بر پایه این ادعا، یک گروه وابسته به ایران با هدف ردیابی ناوهای آمریکایی و شناسایی نقاط ضعف در سامانه‌های ارتباطی، فرستنده‌های کشتی و هواپیما، عکس‌های نظامی و عکس‌های ماهواره‌ای جمع‌آوری کرده تا کشتی‌های جنگی آمریکایی را ردیابی کرده و به دنبال آسیب‌پذیری‌های موجود در ارتباطات آن‌ها باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/147146" target="_blank">📅 09:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147144">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OmTfqNoZxgL060dqUoEEh1oJqB3pkacY4LLsg3aOeDzWslTCW3eNK0yP88KCBIipF2MXBQWvUhbooh6x33MQ9SedoTMt7-8LHyAKrofJo4GnFtV2eBxCI9XUD9bOje7dat1IkAvYxLWDxg0i4V9HjZ4VQ0QkOO5M6FDlGQ_i3tmtBE-im6cuYG4bNKk4dayma0k0TYHR_me47KLLDesoyXYJPnVivl9Ae_5toNOQlZ334ddv7qdmVSv-JnREaU1VCOYXwPHAqBOGdHRMo7wpJaPuCVMuQueti0aPZo_-Km2aB1GouzpVexIudDVgNAPCCr66MJptCtAaNzqHmoNY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NNlv0hNSd-aBdumpmsnJ0RLSi5qNjtHeGIfT6fQyFoKhw5KBlpkLG5m6CKnQe3CuleUqKZ-B6x6OTv3JDMMf0TrYOAYbNQ6UOCuTVWksSBAn3vz9-PNk-iUpaVchQ39YI07aMW4KZzfXYc8QCk42cqgSIxDuZU6iobQRp4Z10oiDla78bi9wvdRUYO751tPi_t563vFVUBgQUfwmSGRVNz48wYG1rl9opPzmct1lNFHcSePyryQhOdBHmSJeFikmw17cBzibbtbFUgnGigEulNxfvuLHUD4UX26bA3N3ch1iVbNXudMZc1yx4ivFZRaW9G4R2GBnXDHzn5km1SI2aQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک هواپیمای سوخت‌رسان A330MRTT سعودی پس از پشتیبانی از عملیات بمباران در یمن، به فرودگاه ملک عبدالعزیز در جده بازمی‌گردد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/147144" target="_blank">📅 08:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147142">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rp9IQvveKK1x_p4Qpn_Ve1GlNooJFuGjme7i_1ykxJtBDX63FHmNNriXJ_GsYx1juykmWrxQMx-xgdRlfs4DB9PrPowIMwfrYpBdaSO5RIBpeiwT2ECmfukceVLCEsg-SYD5Mv-6cmOTLLwqLFEjmdgxVvR2RooqvapAQiulcV0fllwjqOt71bN6202Ydj40cQQD3CzAsS0Z61ycXq_KMPJcLQjvwNsKRckhLs-bNg-I_os7DX302qG8VAzua68CiiCle-8aG73uEPNFVvYaP0u7GuWePVla_GEZ6TnGFCDvKutxI9tE9_EYAsYaXrt61eI5HQFBqQsDesnOHd6UUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1a25b458.mp4?token=oA6uCahu8xN31nL_Hfa-xaHD3pi_w8AKOXNZM6Dos3HdYyKBU-gORgn_VNg7cjuHjkUkymlNf-P8rc398X49oFh8ZBKwcMxt00U89GcCFCoVzC-u9E2muSci_oM75iOtJ9lDnyS15F5jgr8J9tBIMUHgu0_l4-17NmtvvV9uHB0KgcMRYsdIaIZ9YgzNxMrW5DeYww3vssWh19qxG50t3g7ewEt9Z-Y-rkcacKyIDA9PPe1LCDvrhCLuNh2sGijFNwNeWCWxnWg283vAjXRfUsiq-gORxdGm4NYfKmrxLmgaeR5JPJmpWEnwsvJ75urmuT79Uy_m-d5NmQkMledd-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1a25b458.mp4?token=oA6uCahu8xN31nL_Hfa-xaHD3pi_w8AKOXNZM6Dos3HdYyKBU-gORgn_VNg7cjuHjkUkymlNf-P8rc398X49oFh8ZBKwcMxt00U89GcCFCoVzC-u9E2muSci_oM75iOtJ9lDnyS15F5jgr8J9tBIMUHgu0_l4-17NmtvvV9uHB0KgcMRYsdIaIZ9YgzNxMrW5DeYww3vssWh19qxG50t3g7ewEt9Z-Y-rkcacKyIDA9PPe1LCDvrhCLuNh2sGijFNwNeWCWxnWg283vAjXRfUsiq-gORxdGm4NYfKmrxLmgaeR5JPJmpWEnwsvJ75urmuT79Uy_m-d5NmQkMledd-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای اوکراینی شهر نیژنه کامسک، واقع در جمهوری تاتارستان روسیه، را هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/147142" target="_blank">📅 08:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147141">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
سه روز پیش، تعدادی زیادی از موشک‌های رهگیر پاتریوت PAC-3 از پایگاه هوایی مووافق سالتی در اردن پرتاب شدند و با موشک‌های بالستیک ایرانی که به سمت آن شلیک شده بودند، درگیر شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/147141" target="_blank">📅 08:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147140">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
به گفته شرکت اطلاعات دریایی امبری (Ambrey Intelligence)، یک نفتکش با پرچم پاناما «گزارش داده که هنگام حرکت به سمت داخل تنگه هرمز، بر اثر اصابت یک پرتابه ناشناس آسیب دیده است.»
🔴
امبری افزود، این نفتکش از طریق کانال ۱۶ رادیویی VHF پیام اضطراری (Mayday) مخابره کرده و اعلام کرده است که در پی این اصابت، از کار افتاده و قادر به ادامه حرکت نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/147140" target="_blank">📅 08:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147139">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
فرماندار شهرستان قشم، اعلام کرد: یک کشتی تجاری حدود ساعت ۵ صبح امروز در محدوده جزیره هنگام و ساحل شیب دراز جزیره قشم مورد اصابت قرار گرفته است.
🔴
او تاکید کرد: در این حادثه یک نفر کشته و سه نفر مجروح شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/147139" target="_blank">📅 08:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147138">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEZ43NV9ScHtk1sGeLFR4IolCbSGC4-Zn0f9L66LrJLoTUfHESHSHEMbReN7fEDfEUk8mG5KeSQ_zpxDA_8jTLDRJ43cqCKA80SD1a9p5sDD5oRFcN2NLEZT2gsYDzAPNGi1jUHI44tsRjZ5DPJPaeHUgUfRMMPvxVsBa-jcfqeUjfRrhYvpJ3dVhsrp5im_cKU7KLZz0wS013SRqlCZZi27kY5eFf1aSAXfN3G6-vJC3O3DmATqTdjG-IK2Fj9dxEDuVd6vjvAQD0W4gM0pcr_6mjdcwgJ5L_6VqkEEAIG_gRdJmta9oqmAgseyciZZK6OonT3sTz2BzMysWi5zRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: ایران تسلیم نمیشه؛ اگر جنگ میخوان با نیروهای نظامی شجاع ما روبه‌رو
بشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/147138" target="_blank">📅 08:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147137">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOwlpRpFsYiqRcrUa0NsMorWdhjBxLiv1NvRbC5WWIGlZpNaNmPEzIPsliAZzV5mRNoSP8HjtO-P6KxgHfyEY95z7_FoNsyqhLhNQbWSEyd4ly7vVdFCtrsLaZVbJ_ghjQHrLIY4-FF7ntUhie2IHtwgcJjwiieeIsyKzAcnmG9vKk8_hBOhEtzr5V-bBbQCNig4UKyYLQO8NncPmy2Yg1DLlZuX91p-sSg80JO7wp0broLFsLi7Jobbb4feRs3KnQqb-kPr3_2BhzfhI654v7BGZCkfvQ-3LKEATi4PzvoLOuCYznQ2PxGi2yWC8OVonoY1o6aSufPFZ0PCf3xX6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اتلانتیک
:
ترامپ یک تنگه دیگر(باب المندب) از دست داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147137" target="_blank">📅 07:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147136">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nct6loDjq8pkEhxhXxQaFInJJJFvGphq8oLsh9MwezMzE3TSEkj4zL5a99uxvQHC8xcmoUHtIuFnmlB5vo4C7cGg7jf9MfH9kYZ1ZLgGuY_zeBQaBstubGrKd6siz4iggdvYhtVQZlB_jNcMk9grfVajM4tnpjsUAhvhYQphsyHHr7A-z8ZeePwJZi48ALI_vgFz71E2zEgVFob2cI-LbIWHUJRrYKOvuBm2oR_aVbHxMT0DiWBa2dZmTx9vcaWKlWxqCOfsjDMRJuvflzcYFuBZxQJmi6cRHHAKUkbOrwVvbjg2Gqg9U6yCaVUCal3IIrkwE8h4qIjhAg22-aVJdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایستگاه پمپاژ نفتی عربستان جوری منهدم شده که تا 2029-2028 حتی قابلیت بازیابی اولیه هم نداره
🔴
خط لوله شرق به غرب هم منهدم شده در برخی نقاطش و عملا بارگیری جدید در ینبع فعلا نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/147136" target="_blank">📅 07:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147135">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLIT فیلترشکن هوشمند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-NYZ-T-Ugdz79Kg_bNB-8B5pF4ZluZRUgJVjaSOrHAuMuhN0FpyX5JIs2GHqfbLErNxL5jn5vWjjS0kOT-zT4NCYdIiXSOCLtvBxZcCbJmjvJailol4Juj07wnPDVi0By_CNuMEzKJ2yhTBjiqPfottqoG4s-CMirJMXPgh2mSuMIVy5hB2VNEDHOoqWqdsGgEKBsNTKa9NpHfswibEgfrenvn6HBs419LOkx4KDI1nmXNr_Np-VeG-XNcT_9r6CVMmBA6vNKTa_CYbWbo3q2Nk2fZusDJhEsOhc2kIf-QCUnzaeTPWJ5bQFCdlsIKxr9Dr0qB53M6PIrSU49svrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
قیمتارو شکوندیم!
ورود به ربات و دریافت ۲۰ هزار تومن هدیه
مولتی هوشمند
لیت
|
۳۰٪ تخفیف
۳۵+ لوکیشن • ۱۳۰+ لینک پرسرعت • IP ثابت
▶️
یوتوب
و
ساندکلاد
بدون تبلیغات
🔥
فیلیمو، فیلم‌نت و نماوا رایگان
🔥
آی‌پی ثابت برای ترید و اینستا و یوتوب
🎮
سرور
گیمینگ
پینگ بسیار پایین
🎁
کد تخفیف
:
LIT200K
اول رایگان تست کن، بعد انتخاب کن.
🔥
ربات تست رایگان و کانفیگ:
@
litvpn_bot
❤️
ربات مخصوص
همکاران
:
@litpanel_bot
❤️
پشتیبانی
۲۴ ساعته:
@mahan_lit
.</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/147135" target="_blank">📅 01:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147134">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
گزارشات تأیید نشده از شنیده شدن صدای انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/147134" target="_blank">📅 01:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147133">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
مصاحبه جدید هادی چوپان: هانی رامبد بهم خنجر زد. بهم گفت پشت ایران نباید باشی( منظورش جمهوری اسلامی و حکومته) ولی من قبول نکردم و اونم همکاریشو کامل باهام قطع کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/147133" target="_blank">📅 01:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147132">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
شاید باورتون نشه ولی تورم یمن تنها ۳درصد هست و تورم ایران ۱۵۰درصد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/147132" target="_blank">📅 01:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147131">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏
👈
علی قلهکی: طبق توافق احتمالی ایران و عمان بر سر تنگه هرمز، «مسیر ورودی به تنگه ۱۰۰ درصد در اختیار ایران» (مسیر شمالی) و «مسیر خروجی نیز ۲۵ درصد در آب ایران» است.  ‏
🔴
۷ شرط ایران برای بازکردن تنگه هرمز شامل «اتمام جنگ در همه جبهه‌ها» _غزه، لبنان و ایران_ ،…</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/alonews/147131" target="_blank">📅 00:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147130">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7nc06m6Rj0BlP78N0kFQ6mTsi36K_i4aoxz00MyCXpNYRH8G8chcJ922uZWZGVDBnWS_nnvdrMsbCAwbcRAdTcuAtynvcpPRBeIS5GUJQsrJqSCJESQEG3HoizXlcMlgTrtO-FE9Rj6IAntSVnahHLvnq9_Geb7d_ZnGwj1XVaKy9R767q4l1J4UDXOczCmDS9-j5BBF_kH0UDegRDVxtMpsMk13JEDyxKJ42xueRfyaPttm72TncvdlgzYjCZ5YnLMJ4iF5Bg2iFDhLETVC_7DJh6YRZbunSTidaLGEMbx1tEF3sSuzyWfagg95JeDkT_ltbebzjqH9fruVMI-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
علی قلهکی: طبق توافق احتمالی ایران و عمان بر سر تنگه هرمز، «مسیر ورودی به تنگه ۱۰۰ درصد در اختیار ایران» (مسیر شمالی) و «مسیر خروجی نیز ۲۵ درصد در آب ایران» است.
‏
🔴
۷ شرط ایران برای بازکردن تنگه هرمز شامل «اتمام جنگ در همه جبهه‌ها» _غزه، لبنان و ایران_ ، «رفع محاصره»، «آزادسازی بخش قابل توجهی از اموال بلوکه شده»، «لغو تحریم‌ها»، «مسیر ایرانی تنگه»، «قبول حقوق هسته‌ای ایران» (حقِ غنی‌سازی و عدم خروج ۴۰۰ کیلو اورانیوم۶۰٪) و ... است.
‏
🔴
«مذاکره ایران با آمریکا» کاملا متوقف شده و «توافق ایران و عمان بر سر تنگه»، مساله‌ای میان «تهران_مسقط» و کشورهای حوزه خلیج فارس است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/147130" target="_blank">📅 00:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147129">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsuVO-rexqAQZXnnM9xcsmqEVLU8M5bn0PD2yxXiAm1rvjbxyXG5LddFoqJ9cxLABGR7dO9zZbbZEkCExd9lZGXBeLGW9PnyVu9sok_UWOFBrEFgBhnCH8rfkMafu4ENo8OlW8Ch_DYEA5q31Wq1hHdYN9bDlhfmGc74AgrVxgT4PsEqDimFEzHO6oSPOtC7rAVj98BE3PTqBq-KOELuK8BnWE2CChtdas9T1SIQTgI0hErGEqNwEXc3qM2gzjyoSI3NeFucnuRbZ0AqC5Ve7mnbQDWp0_aroSq8leRrcHW-y-0u62Xd7CMO85Ut_UUG1g9L9HyHqjv7qcoHU6ldNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیمتی:
گرونیا بخاطر جنگه دیگه! طبیعیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/alonews/147129" target="_blank">📅 00:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147128">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1-l1DSS7ArpWFW73P6Es2BJQgiBwqAk87Ik4cYhdwucriS3RqlvJwFaB-ImxeSXxw1N_rOFgaJiEhMYDAkieL7i0FvcJIICZ1yQxj6NQThH83uYO9Dow9xrR_DWQahPqyMAgzCqgNuDF5uouMsa69IfrpdGP2IDGyEBU-dh9x7n1T9spX_-wolysXhyqW7vzW2wFXR14LuGWGbI82SMaTdghgHhGSs3nvNLZ5BkQVc9J5TE9r2XeJByPGPYhpdDn3eJrKAGGYTJYqiySnWsO5qaev6jd9JKNqFlGRt1l1CiHa-8EcSQkWTcjLFGkE7JrL9z1J-cAZvoFjKhwhizFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فووووووووری
/
کانال ۱۴ اسرائیل:
ایران برای خروج از npt و آزمایش بمب هسته‌ای آماده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/147128" target="_blank">📅 00:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147127">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
این وسط زن سابق سپهر حیدری وارد اونلی فنز شد تا عکس و ویدیو اشتراکی بفروشه
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/alonews/147127" target="_blank">📅 00:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147126">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PL8fo-GQUk6pvaCFLyCRsp-9b2lpmFFruQmwzdjWpI5doDOPi06SiCjR2La4QDVX2JnXNC4z5rxA-3ldQOyVECvm1fn0ZD1O3FzGYbpm2ayYQdBz4azVwAWT_b1S8ppF4YPx8jvM7j3NufAlxS4iR6tI90rFE0stAkOToawqza71yzj4VQnvpgCGxMDFkgoeL3hHkUX7psq10sAsncpEpMdH67Lsg8oGoUUlrYIpWCknCAqo50ih7otZz1XDXevndNjXrrk5z_STgls5jGLFLeJ1wregfHCGkog1ILXwZoEMfL-FqOgW0cSxlPY8_JLzZW5mnHL6e1XcwDdBm-VuvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این وسط زن سابق سپهر حیدری وارد اونلی فنز شد تا عکس و ویدیو اشتراکی بفروشه
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/alonews/147126" target="_blank">📅 23:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147125">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
وزیر خزانه‌داری ترکیه به شرکت‌ها درباره معامله با ایران هشدار داد
🔴
وزیر خزانه‌داری و دارایی ترکیه به شرکت‌ها و مؤسسات مالی این کشور درباره معاملاتی که ممکن است مشمول تحریم شوند هشدار داده است؛ موضعی که چند روز پس از تحریم یک بانک ترکیه و دو شرکت زیرمجموعه آن به دلیل ارتباط مالی با ایران اعلام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/147125" target="_blank">📅 23:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147124">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
چهار مورد از حملات توپخانه‌ای اسرائیل، منطقه "سربین" در جنوب لبنان را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/alonews/147124" target="_blank">📅 23:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147123">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ارتش عراق: اجازه نمی‌دهیم از خاک کشور برای حمله به کشورهای همسایه استفاده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/alonews/147123" target="_blank">📅 23:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147122">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری / گزارش شلیک موشک به سمت تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/147122" target="_blank">📅 23:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147121">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
سردار وحیدی: اسرائیل اگه جرات داره بدون اربابش وارد درگیری بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/alonews/147121" target="_blank">📅 23:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147120">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
آنتروپیک: هوش مصنوعی می‌تواند تا ۲۰۳۰ هم به رشد اقتصادی و هم بیکاری گسترده منجر شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/alonews/147120" target="_blank">📅 23:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147119">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e73c3932.mp4?token=epUGLg97a3KFMQP5IOf-LHrDu8QuzfL9IhGt1A2b9X7FIAiP6WCIaje3EnAStY8xMPjVkZlEz3N_Wt2AeGPRKkPLSp8LCqdAokeJb2WTWORSLaA3w6VjGC71yzDG6b_FYYIG-ZKc8R4Il1HX25wZE5WB9i8z4Y2bLpF-fmDaIq2IR4baP2e0oXaeRjgWnqY29mlkTWN_vCmEW6NhzJA5w4fNsikwbkhnf2dqI88dWrEIytJn67EmG_HPexcsIeyqD5fLOERHZFk5Er5wMKkYhPitJunQ6gT_tRJ8-dNXekCo_vfW9sls3t-2AUgEdyeO-t18gEoDB5wGj4PO4p7OaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e73c3932.mp4?token=epUGLg97a3KFMQP5IOf-LHrDu8QuzfL9IhGt1A2b9X7FIAiP6WCIaje3EnAStY8xMPjVkZlEz3N_Wt2AeGPRKkPLSp8LCqdAokeJb2WTWORSLaA3w6VjGC71yzDG6b_FYYIG-ZKc8R4Il1HX25wZE5WB9i8z4Y2bLpF-fmDaIq2IR4baP2e0oXaeRjgWnqY29mlkTWN_vCmEW6NhzJA5w4fNsikwbkhnf2dqI88dWrEIytJn67EmG_HPexcsIeyqD5fLOERHZFk5Er5wMKkYhPitJunQ6gT_tRJ8-dNXekCo_vfW9sls3t-2AUgEdyeO-t18gEoDB5wGj4PO4p7OaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه حمله اسرائیل به قنطره در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/alonews/147119" target="_blank">📅 22:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147118">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
برخی منابع خبری گزارش دادند ‌ داعش به یک مقر ارتش عراق در استان کرکوک حمله کردند
🔴
هنوز ارتش عراق به صورت رسمی این حمله را تأیید نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/alonews/147118" target="_blank">📅 22:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147117">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سقوط یک موشک در شهرستان الطوال، واقع در منطقه جازان، که منجر به زخمی شدن دو نفر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/147117" target="_blank">📅 22:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147116">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وزیر دارایی ترکیه: ترکیه به دلیل تحریم های جدید آمریکا پول واردات گاز از ایران را نمیتواند پرداخت کند، ایران تنها از این پول می‌تواند دارو بخرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/147116" target="_blank">📅 22:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147115">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
معاون سیاسی و امنیتی استانداری خوزستان از بازگشایی موقت و محدود مرزهای شلمچه و چذابه تا ساعت ۲۴ امشب برای عبور مسافرانی که در پشت مرزها باقی مانده‌اند، خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/alonews/147115" target="_blank">📅 22:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147114">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/319e8bb997.mp4?token=Q_pXX6b7VrHcqXJNnDKnB8C52iYC73sSyEbyeqUYYd1z3fHZEYOO0q7zD1-dQPoCo1kqsDnBckyfe58CT_DuJJuppcMcky0ohTQD6pYXwyJ67p8MmbFfh9FL4QDCbL4ToCNwNTu58XQdmAyonPQr5mzpNmpH8QqbKHlr7htXIHfYRb-sz4a2gdqN2YRmc9DXLA0Uk7JCbsFtW1SGlllSQZR0XEnQrCpKqrK7gDl7VWfuk_yma9F5bKRM360ULX1AZ1n1WuQH1tAkJxyI4YdQZK_MZSecRtALJPJn53Y91L4S7PAQPkDFJsNBzU8w6H7_JrcumfDbRI7iKUYx-4ge0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/319e8bb997.mp4?token=Q_pXX6b7VrHcqXJNnDKnB8C52iYC73sSyEbyeqUYYd1z3fHZEYOO0q7zD1-dQPoCo1kqsDnBckyfe58CT_DuJJuppcMcky0ohTQD6pYXwyJ67p8MmbFfh9FL4QDCbL4ToCNwNTu58XQdmAyonPQr5mzpNmpH8QqbKHlr7htXIHfYRb-sz4a2gdqN2YRmc9DXLA0Uk7JCbsFtW1SGlllSQZR0XEnQrCpKqrK7gDl7VWfuk_yma9F5bKRM360ULX1AZ1n1WuQH1tAkJxyI4YdQZK_MZSecRtALJPJn53Y91L4S7PAQPkDFJsNBzU8w6H7_JrcumfDbRI7iKUYx-4ge0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو مشهد یه کارگاه آموزشی گذاشتن واسه افراد بالای ۶۰ سال و کارش اینه به این افراد یاد میده چطور اسنپ بگیرن و بابت هر جلسه ۵۰۰ هزار تومن ازشون میگیرن
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/147114" target="_blank">📅 22:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147113">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
مقام ارشد ایرانی: دیدار رئیس‌جمهور با ولیعهد ابوظبی در فضایی آرام و سازنده برگزار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/147113" target="_blank">📅 22:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147112">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
بمباران توپخانه‌ای ارتش اسرائیل مناطق نباتیه الفوقا و الرشیدیه در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/147112" target="_blank">📅 22:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147111">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb519e251e.mp4?token=rzCH-kxVSLmwFGuLtNlINF-1zQVdyatvV6enuNDuAs44PlVP9vn0xyAoZyLn2VcHrhVyPq6OGPs-WOaULifdqkqjqTsbG7fMN9vh6c_lNdD_xYQ3BveBRkNxxqaU9tmVVt4z5MeLgr94_4_vDh3hNWCxbcNQjf_HBCnO_wpge10YClFidTAGlpsG0VPlpHfi9KLVGxVXnmd7K_t5vqwbR__YxYjZjjciI9zatqxXJhthYuHh04extKL4xw6e5PooRpnG8iE54tY366d30bKny5UFJSDzYmK6Ro2B14ZoDL19M3pWO7cNd-BAbRrFzjG0W6bLIIeYkZNgI4mWfYNr6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb519e251e.mp4?token=rzCH-kxVSLmwFGuLtNlINF-1zQVdyatvV6enuNDuAs44PlVP9vn0xyAoZyLn2VcHrhVyPq6OGPs-WOaULifdqkqjqTsbG7fMN9vh6c_lNdD_xYQ3BveBRkNxxqaU9tmVVt4z5MeLgr94_4_vDh3hNWCxbcNQjf_HBCnO_wpge10YClFidTAGlpsG0VPlpHfi9KLVGxVXnmd7K_t5vqwbR__YxYjZjjciI9zatqxXJhthYuHh04extKL4xw6e5PooRpnG8iE54tY366d30bKny5UFJSDzYmK6Ro2B14ZoDL19M3pWO7cNd-BAbRrFzjG0W6bLIIeYkZNgI4mWfYNr6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداوسیما: آقا مجتبی دستور بده توی 24 ساعت سلاح هسته‌ای میسازیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/alonews/147111" target="_blank">📅 21:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147110">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
عراق از کشف 47 پهپاد و 46 موشک و تجهیزات مرتبط در یک مکان متروکه در نزدیکی مرز با ایران خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/alonews/147110" target="_blank">📅 21:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147109">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوری / هشدارهای صوتی در شهر ابها و استان خمیس مشیت، واقع در جنوب عربستان سعودی
✅
@AloNewd</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/147109" target="_blank">📅 21:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147108">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری / هشدارهای صوتی در شهر ابها و استان خمیس مشیت، واقع در جنوب عربستان سعودی
✅
@AloNewd</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/147108" target="_blank">📅 21:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147107">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6A0E0ALRChb6Z5uDOgILdHejHF14S8KzAOKJcflAsFTfgfOnkPyu-y4mSIkiEfSYiJ6agsg_UoNosB4zABrrD46-mNvoLbTdhrFsgrBc3I6Tav-3ef9bbeWADtcP5S9u-f9JJ-NhEwjxRvCIZZhEhQM81THVuqd8cAICS2jVzgdn62NnSUofcI4hA6oiAWVZuwUcKiy1dTrn3xKFX2UPOJqJapOPHQvNtu4epYcSTodHvH9lA0T8nGcIW3n-blxMisrLkCkk_7dedE9cCnxtNz8s8Hw5T1I-ond9JqJeDlkgE5tUWyF0givrIE3X1f6QuCs1TekWeesM4JvHAMUxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایلان ماسک با دارینو آمودی، مدیرعامل آنتروپیک، موافق است که توسعه صنعت هوش مصنوعی باید کندتر شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/alonews/147107" target="_blank">📅 21:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147106">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6B3gEuBN32teMbrya2moLeF3DjeLy7BjsFvqZLG4H-SR9wTScQDJyjl2rwwlRZddF2u1uoNrPduWMI26PE0LYXZqgw2c1jUkQC46R7TgrcED690W1ehSh5zPNEa41qedVNeZMS2T59ewvc3Ip_cp3jBDR4HfuEHgfv1B1McQo05OTj42u58G9Ki6toVht0I7y4Z6Yk9HpDrtAfg-QKLeGtDRnAkaWtMYkw76k-_er16A2K9Bd3lzrhtxwFT8AnfWHONDriRgyLg1rDAVJOS41hHVm1dfjuA5nXv78AM_j148a9ZxNJQcqxtkoDKp4Ir28SXheEtWovASAifYHZi9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع عبری: بن سلمان به ایران پیغام داده که جلوی پیشروی یمنی‌ها را بگیرد و در عوض امتیازاتی به ایران خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/147106" target="_blank">📅 21:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147105">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
صمصامی، نماینده مجلس: بیش از 86 میلیون بشکه نفت کشور بدون اخذ تضمین و به صورت اعتباری به یک شخص واگذار شده و تنها 30 میلیون بشکه به خریدار نهایی منتقل و سرنوشت بیش از 56 میلیون بشکه نفت نامشخص است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/147105" target="_blank">📅 21:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147104">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
یحیی فست: جنگنده‌های سعودی در ۴۸ ساعت گذشته ۱۲۹ حمله هوایی انجام دادند / این حملات بدون پاسخ نخواهد ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/147104" target="_blank">📅 21:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147103">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vL5-QviGswh2tbUEV1G_oh7rHaIIrWCyO54PhYL1n9hPm_RjD2GSKwh9jNlR1tY4GeCG4zBw0wuRyDZFcmYVGdyJfQ8eS0OPZjMycNmzUH7pATfjAjnVvMBDXJyl_M0pD3NBYji6Cr6QHpjU6vpd_mU3cnXJJVX1yhojWdVkkOwqwdGzeS_y4dgBBLiSgtG8C9MH7GvfidMt2RZf-pJm6BL8f26FwH-_Pgjd_QfLjnnQdh2BMCNMEwg4bRmoaxT_vfZeA3k8Nmba-zqaePBTnuFN41i9Pb_mg-fg3Gm38tdVrmcXwN98Ek2oNjzzY4K8J-XLhb5NyaWX442RtpVLHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داماد روحانی:
پایداری‌ها تخم حسن رو هم نمیتونن بخورن
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/147103" target="_blank">📅 21:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147102">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
رئیس کمیته نظامی نیروهای مسلح یمن، (حوثی ها): اگر عربستان به سمت صلح شرافتمندانه حرکت و توافق تبادل اسرا را اجرا نکند، سرنوشتش تسلیم خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/147102" target="_blank">📅 21:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147101">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
کرملین: نگران وخامت اوضاع در خلیج فارس هستیم
🔴
به نظر می‌رسد که اوضاع به هیچ وجه تحت کنترل نیست
🔴
همچنین نگران وضعیت تنگه باب‌المندب هستیم؛ این وضعیت خطر تشدید تنش‌های عمده را به همراه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/147101" target="_blank">📅 20:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147100">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
فوری / منابع عربی: شلیک موشک به سوی تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/147100" target="_blank">📅 20:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147099">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
یک منبع وابسته به دولت صنعا: ۷۳ کشتی طی ۲ روز از باب‌المندب عبور کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/alonews/147099" target="_blank">📅 20:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147098">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
تسنیم: مسیر جنوبی که واشنگتن قصد دارد آن را باز کند، مسدود خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/147098" target="_blank">📅 20:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147097">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
انصارالله (حوثی‌ها) اعلام می‌کند ائتلاف سعودی‌رأس در ۴۸ ساعت گذشته ۱۲۹ حمله هوایی در سراسر یمن انجام داده است که هدف آن‌ها استان‌های تعز، مأرب، حدهیده، الجوف، صعدة، عمران و حجه بوده است.
🔴
آن‌ها میگویند این حملات توسط جنگنده‌های اف-۱۵ و تایفون که از پایگاه‌های ائتلاف در خمیس مشیت و طائف عملیات می‌کردند، انجام شده است.
🔴
این گروه هشدار داد که این حملات «بی‌مجازات نخواهد ماند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/147097" target="_blank">📅 20:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147096">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7775db9344.mp4?token=eLAEHiF4un0i9gDOph8KkpDIR4c7RvMKM0K1f48CvaiRrNAp_L2DtJA_rfCtBxt8Yxk_ckHBJgMuI55oShaLBnvPJ8ZQiUgovyk27WVMXgpW3bNBs1BrPGZi7HvYdn1yJxysMkn4-MFDCW2VYf9x56OpXhEADZv8IMKSRHlUNxS-VbJ4E11dNeg4We4Hx3OZzxvszhWVohwBMf_eqIK0FAepKTAQQsJlyVHe4iK77Td9_pqRZsSgePsfnMQyxFwfqcX-wagnXKxjZyoPXa-gDD3Zj7-B0hR4y8AG3zkLZCg8-xuPBIXZFLhxIduXPqPBIYJx8oi7RzVzelvvcm6bZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7775db9344.mp4?token=eLAEHiF4un0i9gDOph8KkpDIR4c7RvMKM0K1f48CvaiRrNAp_L2DtJA_rfCtBxt8Yxk_ckHBJgMuI55oShaLBnvPJ8ZQiUgovyk27WVMXgpW3bNBs1BrPGZi7HvYdn1yJxysMkn4-MFDCW2VYf9x56OpXhEADZv8IMKSRHlUNxS-VbJ4E11dNeg4We4Hx3OZzxvszhWVohwBMf_eqIK0FAepKTAQQsJlyVHe4iK77Td9_pqRZsSgePsfnMQyxFwfqcX-wagnXKxjZyoPXa-gDD3Zj7-B0hR4y8AG3zkLZCg8-xuPBIXZFLhxIduXPqPBIYJx8oi7RzVzelvvcm6bZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای دیروز نشان‌دهنده آسیب گسترده به پلنت عمده‌فروشی ابها آرامکو پس از حملات حوثی (انصارالله) است، به طوری که حداقل شش مخزن ذخیره نفت به طور کامل تخریب شده و هشت مخزن دیگر نیز آسیب‌های خفیف‌تری دیده‌اند.
🔴
احتمالاً این تأسیسات از کار افتاده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/147096" target="_blank">📅 20:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147095">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3V6srY_9R2wh5I-qXoyhfMrMjJSx3Lb_3ZmppuhWSdTjLlG8Gqww_TwbeEqg1O6n_m7HdCwenWVlFLaTJ8EHk-RumaKkeR2aHPLRp5c8QeNI6B6eUTXg-51rqYCs3M6IEziPe478-UuEcbi22F2Pkhn_vd3TGKk25afNe0DON-WsyGw82z8Qbe6m7D5Mt6KBIBDBmZwCkwm4tpJkNV61sOGw4vmYBfRBiAc9gw8SFNFBH9fOCiG1UdUCb-kpTr06T0cB9vknYFIFB7cDR7jzhZXwh_PfEShuxgqtXnTlYfCUg41QNrFe3Nr4TPRiv5YsJzh6DR-U0tFekstnuaBUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کنسول بازی ps5 pro به قیمت تقریبا ۳۰۰ میلیون تومن رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/147095" target="_blank">📅 20:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147094">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvC2v34xUR2sPqoFm87EV1NudbFLkwvYcMPg_qjVyZNK5lkYVKcT10K31dzSij-6uIT6Cv67S3Or9b_hP7QT3mFg96NGPslL0FOPMVfYYKaHLchBiAKegTD-xsUA64Z_BbobBhZhNXxf6AclBPRRsG3cQHkey34lmDZpTYO7CwwZOyuDmZr_g-CO8uHC1RQxEFW-R6PT6BDjgyzOkUuLwTBkaO3VpUVEieQlCEumdviyB7ecaKI3sZR0oDb5cFGpwx0wwgx6t2KUWeW2GdFUgAVLlhjCyPl3gMkhriHM_11YaUcCwZq-VDgC8ImhiVdNUsTAfKitQZmVBR-QqNeXCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: مذاکره متوقف شده است چیزی وجود ندارد که میانجیگر داشته باشد.
🔴
عاصم منیر هم جمع بندی ندارد که اگر وارد جنگ یمن شد، بتواند پیروز شود و پرتابه‌ای سمت تاسیسات حیاتی پاکستان نرود
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/147094" target="_blank">📅 20:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147093">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsOheG_CH0cx1cQOA9fF7cjyUN3kAdieyBbKZ6Bf7WVSnY7Bf_zf7UrQUIooNxXfGHHTwrNMGiHbzyR_QlZiSP913iqibqMyz8Jt-3JJ1ww9P2STprO5xauRBiQ2297D0KYZ4w8fhMDdJXiR4eqcnm3e86le032Ia9ZVyMa2loID7cm8e4W57QtKFZPEoDtHLbGjDa4r7NvTtir2y3g-V9HmOO6f0270M2Y13AvI0P8EparmfBIXaRfWjLzW6Y6a3KfaoCz1203IdRZs1lJBaMzkPsBRMntN2eaFpmACRdyG8oZWh4AsmiH0AVghe9ufGSph44zn_tWsLCnoGqkhoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه‌نویی: ماهی ۱۵ میلیارد حقوق میخوام
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/147093" target="_blank">📅 19:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147092">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJC2doB6dlZuVORM6iFtVh7RT6Ni28Ij9QJW7vSxzogohSwQxcGsOJBH0yloOxaOZq5Gy-4PD8wnT-YC55B_Ba0Jh80Mr8hChOWI_YoUnSJ0lgRWsMM3e24Xhbs9R1IazQ1jNNOZKdk4JhjTpcuW3xTdXy4wEImkyHxV7slYDu3gPmOIh4hpk4ATq1SshDpiBm5NsAARTUE3tD89seOABEjDy5Py3YVdsH1eyxdo4PZHbg6O27VxHJRzqydzWFIwQ8rgunMcM466wah-SicJJzYUDuT-EhmLgh_r0ZRF1fAmTvWLZjKAj_000aAYJG6dwIQRE9u5IrWuAZHaEDK-TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لباس‌ های نظامی و تصاویر به‌ دست‌آمده نشان می‌دهد که نیروهای ارتش عربستان سعودی حضور مستقیم و سازمان‌ یافته‌ای در بندر المخا یمن داشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/147092" target="_blank">📅 19:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147091">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
مهر به نقل از منبع آگاه: براساس گفت و گوهای فشرده فنی و دیپلماتیک میان ایران و عمان که در نهایت در اوایل شهریور ماه توافق نهایی حاصل شد، قرار است به زودی تفاهم میان تهران و مسقط با حضور وزرای خارجه کشورهای حاشیه خلیج منطقه اعلام شود.
🔴
این تفاهم صرفا میان ایران و عمان است و سایر کشورها فقط به این خاطر که در جریان جزئیات مسیر و ترتیبات تردد قرار گیرند در جلسه حضور خواهند داشت تا بصورت تلویحی عدم مخالفت آن‌ها نیز برای جامعه جهانی مشخص شود
🔴
در این تفاهم درباره جزئیات و مشخصات مسیرهای جدید ورود و خروج از تنگه میان ایران و عمان توافق انجام شده است. براساس این تفاهم، مسیر ورودی به خلیج فارس به صورت کامل در آب های سرزمینی ایران قرار دارد و بخشی از مسیر خروج از خلیج فارس نیز در آب های سرزمینی ایران قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/147091" target="_blank">📅 19:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147090">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiXqkkahq8ARme9bU02FTwBm3MkYbP2gjZhs6H1Y0kreJy8ZAV9Vc07XeIRS36QqEoF6thBPFFYK8BqhiiIN5D8x1XgWMv36RGQxkHcsw_SPoRvYWs1JmtgYGhGJRrM5YUjO6s2NIIsyoLYmBIWt5IHcVJnlt_Z8c7VWO5SbOVwIMpXhHmjIQxxCBXZUdKBeOkUblPwM2_MX4MTEJyWLX2yItSVoui7M99LXJfPCDp8GbNVR-zfhE2w1wfl8S44pVDXGXmrCGXACCLBSmPYtWW8oyOrwEuJ9aEImmUU-WtXoiB4CnXGhBK2qTNTDJ79BNmvOQ3_3Fs2IcR-cur3NsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترکیه شدیدا حملات پهپادی که از خاک عراق علیه عربستان سعودی انجام شد، محکوم کرد و حمایت خود را از حاکمیت و یکپارچگی قلمرو عربستان سعودی مجدداً تأیید نمود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/147090" target="_blank">📅 19:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147089">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوری/خبری مهم
👇
https://t.me/+4tCwpwOgY3gyNzU0
https://t.me/+4tCwpwOgY3gyNzU0</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/147089" target="_blank">📅 19:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147088">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/756c9e4032.mp4?token=oLyuCxXTnXSiQB67i6HZl7uEHCf_n4Un7uVwRoLpE1ypwx9QwBZyocNrDlMPO9rAnu6o6AQMs62pdkOd5XOXqSZ7NvVpPKNF43lzvH04UYrhvvX-8MhcbpuYmy3BfjVp2jXQrITxUWWZAs0SYXNUJHLdmAsErRIenFDIhDNgJFmTUqyCUZ9UtfvlSHPDw2EmgT3Hb3LyzRbjD1sPChJaYhlrDYvoZ7Zyb2ozHfg9AvmVSXmX_XMqV2qi-_uGMRgEzF_Em1iTalhkzKBcuyHsMuZKL26jeEn7fcKIYdjdZ2_wvQrYdCGz02vuyfHU_Bw2tQXeIlFmDvIy9NlBtwt9Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/756c9e4032.mp4?token=oLyuCxXTnXSiQB67i6HZl7uEHCf_n4Un7uVwRoLpE1ypwx9QwBZyocNrDlMPO9rAnu6o6AQMs62pdkOd5XOXqSZ7NvVpPKNF43lzvH04UYrhvvX-8MhcbpuYmy3BfjVp2jXQrITxUWWZAs0SYXNUJHLdmAsErRIenFDIhDNgJFmTUqyCUZ9UtfvlSHPDw2EmgT3Hb3LyzRbjD1sPChJaYhlrDYvoZ7Zyb2ozHfg9AvmVSXmX_XMqV2qi-_uGMRgEzF_Em1iTalhkzKBcuyHsMuZKL26jeEn7fcKIYdjdZ2_wvQrYdCGz02vuyfHU_Bw2tQXeIlFmDvIy9NlBtwt9Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور مالی اسرائیل، بزیل سموتریچ:
امروز، فلسطینیان در غزه هنوز به امید چسبیده‌اند که به‌نحوی همه‌چیز بازسازی خواهد شد و آن‌ها بازخواهند گشت.
🔴
آن‌ها باید درک کنند که چیزی برای جستجو در آنجا باقی نمانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/147088" target="_blank">📅 19:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147087">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ثبت احوال : همه کارت های ملی که تاریخ انقضای آنها رسیده تا پایان سال ۱۴۰۵ اعتبار دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/147087" target="_blank">📅 19:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147086">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
هواشناسی: درپی فعالیت سامانهٔ بارشی در بخش‌هایی از شمال‌غرب، سواحل دریای خزر و دامنه‌های البرز، امروز و فردا در این مناطق رگبار باران، رعدوبرق و وزش باد شدید موقت پیش‌بینی می‌شود.
🔴
همچنین در ۵ روز آینده، جنوب کرمان، جنوب سیستان‌وبلوچستان و ارتفاعات هرمزگان با رگبار، رعدوبرق و وزش باد شدید موقت مواجه خواهند بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/147086" target="_blank">📅 19:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147085">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از یک مقام ایرانی: ایران به دنبال وضع عوارض بر کشتی‌های عبوری از تنگه هرمز است و سلطان‌نشین عمان این درخواست را رد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/147085" target="_blank">📅 19:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147084">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏
👈
الجزیره:
یک منبع امریکایی گفت هرگونه توافقی که بین ایران و پادشاهی عمان امضا شود، از نظر ما هیچ اهمیتی ندارد.
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/147084" target="_blank">📅 19:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147083">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o1OdiR840Foxpkh8wdNbmzQVt39hPfaQGfVAnJBGqGOMkBJ5rFkPCEYg4oL7-CBLt97x328lLd5Q51-3lLbt1MEc9Dzne9neYXmNxdW-FGEbeto7ox-2gWEkNznrGpz0cecBnxcROh_7uNu3-cBeM1S6MKfR2VaKZHSaY-h16ag7bSLfvPN0HPLHjdZ_GO4svr9mmCVe3pLalCyrxepd5niAMklRQXnizbbBfaC_vaPncaEVr73AhxyX4VPkV4qUoEhGEvfMkdGa765fx9BPosKKW199TeYhiMNe5kSc0nQwAoGvU2GICSIFByV2stkWDb5ESmnzu6E3XT8hum3Iyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده آمریکا (سنتکام) اعلام کرد که در ۶۰ روز گذشته، ۱۰۰ کشتی تجاری را به عنوان بخشی از محاصره خود علیه بنادر ایران تغییر مسیر داده است. سنتکام همچنین اعلام کرد که هیچ کشتی‌ای از محاصره آن‌ها عبور نکرده است.
افزایش ۱ کشتی تغییرمسیرشده نسبت به به‌روزرسانی دیروز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/147083" target="_blank">📅 19:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147080">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ffVp37na_IhGnXchl6VAN80agciMWtbU0bDoBXguTnTQh10jkUnoyNmZPGlrPfQlY98mTPoNDdVq1muuHy6E6_6kZhobuDiWkqUsdjmvBaAxa_G1dM_mh2hUN1bnBNv0pTHBt_BgxGSDfyJ_ta_7xscP8HtYnV47i_AfydKokSN74H8clyysQxymx7MN21OnxttN7gOR8TUe-pIJv22ChmLvAPcF3EJjBZRH-a1q_2o6rMNmZqzg_dkm_XGaNGZuzQrc7iW81FLzRkrAkj6tRiuv9le727sdhDOjfUzWa0pPvsHIdjjSAEIDRwZmP4TWwKs7e8JddQa-WoAYIF2l0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3N8Wq2bmHocv_1yBql16__0BRgHjEoNHwRo_duS2MjSdRNVuVQmeuhvrhEKcrg_4YcMV_qQLXdmabxHT9ymee655W4tYmQRY3iTd5NS2V6KkQmu29C7B2eO0cOI7j2jxd2LUzJplpzzaw4Ns8orizdKc8v93kjKq01ZHVOKY6FSOgyrTLIdm3GbljC5OxXoXUUMTZo8svC-7aqQLI274Hq2BDbr_0fJ8rGyQlIrvZXeMD9rRsdhiF4u2L7Tzob1ixuYX5PwNnuAsfqAIlUfQ8yo3ElDkmrnGVgFVw9EvZaQb76IZXOPTQ2w0GLUVeHbtqZQFUR85S_TBMti4Gslxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CS9-ex7SB280bZpH3mQAR8XN2VPj9NkpLqc-ep6Db_THNLS0PVUuEXP7mJkVoC4hDZnacnZhXz34yNXgDhkLjQFsg2KumI2qFCMKBcjTRtmlf94p7JQOR2QuLXFrXrykQoRB7LF-uGf0KsJhYD5qvkC_fqMUELS5d67WriCQ7CL4Ls_KVYiejZBIJfTWAWAy-Uh_9d47S9ir9IA-fRBJm2yGo_5iw1UASpqNOV6nKvggJu623Hg9ox4WgabvapsTxf4AAOFgogK5QircqM9Q0GcobMZQWpGVRytr2qT3N_kH8NIe3GdWKp-5Tg78KPS1r6aHZd3cj0kFcYVOxWfcqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کشتی‌ها و نفتکش‌های آسیب‌دیده ایران در خلیج فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/147080" target="_blank">📅 18:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147079">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Re3JJBrXffJs8ljrJR7y0b6prrpaveLNhS8LSbo5m5qNNfWO4Ew7udbxNLQu4AD1psf_I8UXsVO9fH2z0z2PNjU-9LB-CSSztkCr4kdTQCB9D8gRni9CUdYCq-wvn5P29QXIrTFCqiGs7qsVvcIJEuqh9PjIkQAYCTbiOXJtVeY_KBarqFf1hVBGzEvFYvEka195ttAeQOTDegtqOoCQdbvCsTpuzMtOgZgxQ5cDTqKqf1ZVUWdDzZ5p8LynkzV5CZj_f236u8j4ObHUKU5eFEWpwvkLWf9JgAxBNfOj2plG8OqGyG9GV5gpkhZQClCTjJ5gJCQbz73ginJG9TLC1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
نفت برنت در پایان این هفته ۱۰۴ دلار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/147079" target="_blank">📅 18:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147078">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRgdZAdBV6-AHi2yvR1WmU_pgFxMsr-OX9f0kVBShMDdT3sU2mD8xhXc7YwLIU8_b-3mXna7sxYfP5Ow2ktnRJ96Zq8fn9QVakH9wDAqbS3WXBQ3qvQ25Tx-NQUB_fHhOR0hfGnpW3H6OO2Cb0g0WPEOszldblWKOhImpDdEh9mBDqeO_2UjP5VDf9Z5ZKJ-DhmfZm_71ke9rQJpr92_9S1WcJczJgQcFs8mPAmMkr-yom0rBLfp9RHj780McRBkT-ZeaQA3wesVybgaxwMJGtlYWgXOpnSFkASqMDNFxC_1ETmOyosgNLYi-yjlPHV9VB64gAVtxjdmhH-TmLfovQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لاوروف: روسیه آماده مذاکره با اوکراین است
🔴
وزیر خارجه روسیه گفت مسکو برای مذاکره جهت حل مناقشه کی‌یف آماده است اما عملیات ویژه نظامی را در طول این فرآیند متوقف نخواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/147078" target="_blank">📅 18:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147077">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6346739a2f.mp4?token=tEh5l8UztR-IovyOg9FXOez0GOM3ZCYn2H-PVRdRLxmU7GQ2hWPsc6k5kD5DbsGF00pCh9DbqgJ_uT-mUy4y6FDQ44nkIqsy5VQgcZ6roi1rAT4p8AGQdv3a21a8kOFg0KgWDWrS64NRZ1018agy-xjpLAZZdD05BY29kblAQ1br0CLfCYu4Tb8ua1SWotA2gKceZvXwiGuvwsLWxgjiMh0A63fVCwnfQOUITqN4ZZJsRGz29NCtpBKtBXQawP84bjemu-Sgnn6AdjUr0MO-WxCkq8BHY_gfpBhCpdrfHNRUaik2EPxkxmNH1ZcUAu_l8puJpQONFWjWJRmuNWSQAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6346739a2f.mp4?token=tEh5l8UztR-IovyOg9FXOez0GOM3ZCYn2H-PVRdRLxmU7GQ2hWPsc6k5kD5DbsGF00pCh9DbqgJ_uT-mUy4y6FDQ44nkIqsy5VQgcZ6roi1rAT4p8AGQdv3a21a8kOFg0KgWDWrS64NRZ1018agy-xjpLAZZdD05BY29kblAQ1br0CLfCYu4Tb8ua1SWotA2gKceZvXwiGuvwsLWxgjiMh0A63fVCwnfQOUITqN4ZZJsRGz29NCtpBKtBXQawP84bjemu-Sgnn6AdjUr0MO-WxCkq8BHY_gfpBhCpdrfHNRUaik2EPxkxmNH1ZcUAu_l8puJpQONFWjWJRmuNWSQAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری‌هایی بین نیروهای حوثی و نیروهای وفادار به عربستان سعودی در غرب شهر تعز رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/147077" target="_blank">📅 18:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147076">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4jID6MJrR9tAyzutHIibkdFyztaOOWHbukV4CZ0XSaz-AD435Z6d5OltRU7YRqXVJ_bsqwbsIIdPOustbsuzPqWT0FFvME0tfgM35LgObWnm_C0G7N85Y2xFbKONDIN2c7SRru6OwXRZN8IT8uj5UxCYDkikVDuSf74eLr-_LmCLpQFfm-koFH8ZhBOoBjxFRsgt8RVm4fmCvId2H-xYAFiTErjEsIvY9VXgAapmfeAtPDpXEDn1e9JuqEB-ECUhGq0a1ZLbat_BhZQ2cEQNxEvdtm4Lw-4IAsySb79U2-hpu6vINOsrMW7jrwULHg1YrdHWWuFwrSxjbwbt5tZkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طائب، رئیس بسیج: اسرائیل رو نابود میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/147076" target="_blank">📅 18:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147075">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLNEJJmcJqXHN5ENUBYjlcJCL6G2PVVzlHUQPfy0z6ECA8Fet3yB5O47jY4jRqXkuGDx_unEHWugD_Qz04vFPo_voTOlpVAOuO1KTMLzpvwiPlexb58E7ZkaX6jxoN-PRPZZoq18scs4BCL4IzKHH1UQFRurvWICEVuq_OpjUzd11niN-_eekWMGnE-_bYCBgh_7HWyKb6lcO-qnNu-ng9CNgpZwOdhislbk-xI3XnlWonFs79g3nqKXaFuE-fXRhW5K_U-vTrug-o52kLzxkXAWCbvrwUz3UX9ggXZx1zKFyno_ZoQRdyEfOKRbU3xEekjxvl1IbaGSVyIvj55O_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مقام ارشد ایرانی به رویترز:
جلسه‌ای که قرار بود روز دوشنبه برگزار شود، به درخواست عمان ترتیب داده شد. انتظار نمی‌رود که در این جلسه به توافقی برای باز کردن تنگه هرمز دست یابند. ایران به توافقی نیاز دارد که به آن اجازه دهد از کشتی‌های عبوری در این تنگه عوارض دریافت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/147075" target="_blank">📅 17:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147074">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سفارت ایالات متحده در امارات متحده عربی آمریکایی‌ها را به اعمال «احتیاط بیشتر» در اطراف اماکن یهودی و مرتبط با اسرائیل، از جمله اماکن عبادت، هشدار داد.
امارات متحده عربی همچنان در سطح ۳ «بازنگری در سفر» به دلیل تروریسم و تعارض مسلح قرار دارد.
این یک تهدید خاص و جدید نیست، بلکه یادآوری‌ای در میان ریسک‌های افزایش‌یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/147074" target="_blank">📅 17:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147073">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
بحرین اعلام کرد
تا زمانی که روابط دیپلماتیک با
تهران
برقرار نشود، از شرکت در هرگونه نشست با این کشور خودداری می‌کند و پیشنهاد عمان برای برگزاری نشست وزرای خلیج فارس و تهران در مورد تنگه هرمز را رد کرده است.
بحرین چهار شرط تعیین کرد: توقف حملات، پرداخت خسارت‌ها، احترام به حاکمیت و حل اختلافات از طریق قانون.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/147073" target="_blank">📅 17:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147072">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfzHhrXhsVzMaiP5aCCGzya6SQJB0ctObGFZ-5L_HvaTS7sseUmfDqb99CMpcjEQNSKU02D17su0umgmnlYjNbdFTr-jIW1J7uMpl8B7exj4KOUiep_4tYEceLGMLM7Vg9tWF98w-vizoCc9lNRiew7U32Iw-9r4s4pOXCRuf7mZCZkbX3a8DUNEnQiqtgSfJJKacDwccT2NatseTBSGobdujCl0qzfoxvYqJgky8Wr6h2kQJg3RBSsDChQsrBYctnyXfHcqn723MHnfLqeChSCP6yTPtmbQVmN2XrGAdpBanB2k4oZ-erDevsUVROSsB9Kme0qD0RitJToPtVUSIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای خرید آیفون ۱۸ پرو در هر کشور باید چند روز کار کرد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/147072" target="_blank">📅 17:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147071">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
رئیس‌جمهور چین، شی جین‌پینگ، پیشنهاد ایفای نقش در مذاکرات صلح میان آمریکا و ایران را مطرح کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/147071" target="_blank">📅 17:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147070">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea0cc24d7.mp4?token=TN0-wECzswp1BsNBfntli7cZQ4v3OYh9b-_wGVwN5FMDOGwfHMJfKqpDXN0qFsEh8lCE-i64lzRsUpUVRFPOlBxEjop1hXX_K6WskFs9S2fmQxjr4_PTmGdzu4E19UB_wS2dH1fsh21wFSPb8j4S8luxAdv74JQ7wnMb4P7WuGLbgzqHD-pOb6aGMKCtQzEg_Rx1D_lVEflr0JLkouGo5LzM_yM929810hSlnIFqmC5Lm4YGEDyYqGaqJagd6NUCIfowOXeDqY1d3CmNLeYC6m5qG-U_dbLwCHqg6wZmDciZD2nWBmjKOJ3JJSEuAtFDAULzxzH94hCUZYL1tA1PDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea0cc24d7.mp4?token=TN0-wECzswp1BsNBfntli7cZQ4v3OYh9b-_wGVwN5FMDOGwfHMJfKqpDXN0qFsEh8lCE-i64lzRsUpUVRFPOlBxEjop1hXX_K6WskFs9S2fmQxjr4_PTmGdzu4E19UB_wS2dH1fsh21wFSPb8j4S8luxAdv74JQ7wnMb4P7WuGLbgzqHD-pOb6aGMKCtQzEg_Rx1D_lVEflr0JLkouGo5LzM_yM929810hSlnIFqmC5Lm4YGEDyYqGaqJagd6NUCIfowOXeDqY1d3CmNLeYC6m5qG-U_dbLwCHqg6wZmDciZD2nWBmjKOJ3JJSEuAtFDAULzxzH94hCUZYL1tA1PDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روته، دبیرکل ناتو: روسیه متحمل تلفات بسیار سنگینی شده است که اکنون تخمین زده می‌شود بیش از ۴۰ هزار نفر در هر ماه یا به قتل برسند یا به شدت مجروح شوند.
🔴
لحظه‌ای در این مورد فکر کنید. بیش از ۴۰ هزار نفر. در هر ماه
🔴
با وجود این تلفات سنگین، پوتین هیچ تمایلی برای پایان دادن به جنگ نشان نمی‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/147070" target="_blank">📅 17:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147069">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwcfwBvG01lWq918J8Nh6Un8B0LL0EpAM43rJSMq1nrQwqmBNGZT-_FCBX0SRZoqppNDYBO8ookmfXt7YDojSsYS5eUZ2DE7xH-b_LV-3dsSJZ1mmQmVtoXqZ1U0rWYST9WpZ3Gv6MKq8MAjDM01PJ671ltioVXQSbKWR0AzZ-A0nkj3veUmHwoxgZXANBSocipYd0ASPHK4uoDuaHNk_YiXyk-SBzxHOw_mUmmFXEl4B23YczbCJgQqRdnjYzDcpHNwrWpEN1Vtiz5_iXj1eD82epyuQhhTDOg3d09syBZTfwdk6r0XsfynPpXCYjYFrjGOcx_x8ONqbJ7TsfEQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: ایالات متحده با یک چالش جدید مواجه است: اگر حوثی‌ها تنگه باب المندب را مسدود کنند، ضربه دیگری به اقتصاد جهانی وارد خواهد شد و 7 درصد دیگر از عرضه نفت جهانی و حدود 12 درصد از تجارت جهانی را محدود خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/147069" target="_blank">📅 17:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147068">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
فوری / بحرین اعلام کرد که در نشست ایران درباره تنگه هرمز شرکت نخواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/147068" target="_blank">📅 16:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147067">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
دولت عراق: نخست‌وزیر با درخواست ایران برای انجام تحقیقات مشترک درباره کشف سکوهای پرتاب پهپاد در مناطق مرزی موافقت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/147067" target="_blank">📅 16:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147066">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c66927e311.mp4?token=UG2Lf6H7u4gadW4ZVh1cy-0FYG2MTUOFK9HHxOid3PvxGLWhB3ND62rd184qM9m1xx-fH7JS3s12nhB5u34VJ8DsHHof_Tkil1fB5v9VX6ZcbKhJXur23Fe_5sVqi1FaLT1cxGIvYwlEeQ7BDDXWOj7AuLrSEHE-tdLmIfAqIlulGLi1Qgef2ezSLu2jF3Pkv2HMZrl2lH-vF9PDoCiiAm87N8_vZveVOggdMXe8v-CsWpKthJiQsASJmlvYeog-QgALYtg-BNVRYh5OtCYBAvsDXoy2thr3YX775Mj6BL9ilPEc3D9Fpr2cGL0Viud9xWTZmPSn5clyseTxIyM2SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c66927e311.mp4?token=UG2Lf6H7u4gadW4ZVh1cy-0FYG2MTUOFK9HHxOid3PvxGLWhB3ND62rd184qM9m1xx-fH7JS3s12nhB5u34VJ8DsHHof_Tkil1fB5v9VX6ZcbKhJXur23Fe_5sVqi1FaLT1cxGIvYwlEeQ7BDDXWOj7AuLrSEHE-tdLmIfAqIlulGLi1Qgef2ezSLu2jF3Pkv2HMZrl2lH-vF9PDoCiiAm87N8_vZveVOggdMXe8v-CsWpKthJiQsASJmlvYeog-QgALYtg-BNVRYh5OtCYBAvsDXoy2thr3YX775Mj6BL9ilPEc3D9Fpr2cGL0Viud9xWTZmPSn5clyseTxIyM2SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خودروهای زرهی متعلق به امارات تحت کنترل نیروهای حوثی یمنی قرار دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/147066" target="_blank">📅 16:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147065">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqO8v21gLR7V3u6VOuxUKqvq2CfTRgnY2ykA01WByzvQvrSZEmzbnK5jU6jh7u3CHol4N7bv7Q2b4RlPIFSUvvBQ91GmPOC7c0GwkUh8_5DI7-PckFIdBhNg2I6vMARmjeOxdarhyTm_mN1HV_kyzf8_oyCbpTQ49ezyb-7YPO5XpOi56ZvFPJxF42d3kjzS5H5tPWHjpRVeDSRDv5sn-bbTT1OA9tjkn8ji9bLgavjTom5Wcq6-TzJbZnW3Tvw5WPl62ywEzGCZZsdn1Y6W9bnb9_84wxObdh2c9LRo_kmWDtQ5C2-ArH8YfWYIC0iEXUHquCNCbUBUVgoW0n_KSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارسال مقالات علمی هم تحریم شد
🔴
معاون تحقیقات و فناوری وزیر بهداشت، با انتشار تصویری از صفحه محدودیت دسترسی شرکت Salesforce به دلیل قوانین تحریم‌های آمریکا، از ممانعت کاربران ایرانی از ارسال مقاله به یک مجله علمی خبر داد
🔴
در تصویر منتشرشده، نوشته شده که این شرکت برای رعایت قوانین و مقررات کنترل صادرات و تحریم‌های اقتصادی آمریکا، دسترسی کاربران از ایران و چند منطقه و کشور دیگر را به برخی خدمات خود پشتیبانی نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/147065" target="_blank">📅 16:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147064">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ: ناتو و اروپا در قبال ایران «بسیار ناامیدکننده» بوده‌اند!
🔴
ناتو نمی‌خواست در تنگه [هرمز] به ما کمک کند، با اینکه ما هیچ نفتی از این تنگه دریافت نمی‌کنیم
🔴
ما همه مین‌ها را از بین بردیم؛ دیگر هیچ مینی آنجا وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/147064" target="_blank">📅 16:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147063">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d0c57f91.mp4?token=Wq_cz9UwAzF27urSAqbu11BT7iZ4zfq5dVjU40_cTZRToP2n37yylwPV7DEcZPmwvXpQZ268CBd8usbwWd0VpX5A038GVv0_Vpv0HMTd_YtR9gBuJxGeR9YIokIxkHePj1TO-zc8sA_Ac9ArLr0itE3tnrWPJ3ighO3pOHUtm-YD8-TTG472tU1sEWto3wfAFIc25AFmdPGFcZl68T9zn27_OMV1r_GH0UWWPD3Osc9mgnAj75GpBRecoDIX9dFA3huRo7YFslqV_urrJ6byfggWQabEbP6Bq5I_17NyAKiGunfeL4irCVz2agXJi42wpSc3mI6g1ijYwgSiNsuH2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d0c57f91.mp4?token=Wq_cz9UwAzF27urSAqbu11BT7iZ4zfq5dVjU40_cTZRToP2n37yylwPV7DEcZPmwvXpQZ268CBd8usbwWd0VpX5A038GVv0_Vpv0HMTd_YtR9gBuJxGeR9YIokIxkHePj1TO-zc8sA_Ac9ArLr0itE3tnrWPJ3ighO3pOHUtm-YD8-TTG472tU1sEWto3wfAFIc25AFmdPGFcZl68T9zn27_OMV1r_GH0UWWPD3Osc9mgnAj75GpBRecoDIX9dFA3huRo7YFslqV_urrJ6byfggWQabEbP6Bq5I_17NyAKiGunfeL4irCVz2agXJi42wpSc3mI6g1ijYwgSiNsuH2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: تاسیسات هسته‌ای صلح‌آمیز باید از حمله و تهدید مصون بمانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/147063" target="_blank">📅 16:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147062">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
آرش اعلایی، خبرنگار اسبق اینترنشنال: عربستان تا ۱هفته دیگه شورتش پرچم میشه و آمریکا هم کلا منطقه رو بیخیال شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/147062" target="_blank">📅 16:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147061">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
کاخ کرملین: هنوز مشخص نیست که آیا پوتین در اجلاس سران گروه ۲۰ در میامی شرکت خواهد کرد یا خیر.
🔴
اگر زلنسکی واقعاً تمایل به ملاقات با پوتین دارد، می‌تواند به مسکو بیاید
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/147061" target="_blank">📅 16:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147060">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
دلار بزودی 300هزار میشه
⁉️
🔴
تحلیل ترسناک نوستراداموس ایرانی
👇
https://t.me/+WZbLEaPPJQUwZDU0
https://t.me/+WZbLEaPPJQUwZDU0</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/147060" target="_blank">📅 16:07 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
