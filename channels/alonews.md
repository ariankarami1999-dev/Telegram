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
<img src="https://cdn4.telesco.pe/file/gpgC7JP2ulAj13MLrXj5_iMYk0R6E2sfXqQmrBryg-Moud7_cW5P-adcM1F2PovnVR2fkS9QSNIzK7nNWCJRt1H4vBg4luNd7PxbbfwEmse8AlwHjbOZepFM_Uxw7qK02po_2PCnZcnFu9NDnGtwiXTBV2KRrn7TFnymmrokhtSimxXYwPxeGml6XxbXLPcZM3ouOXjzrlIYIXF-d4gN6C4em_vCwoC81tNBaJ_O3-bDfEY4x9iKkRU8U2J_lvymcr_QL6cbBTPLzoaULpDaMWjQGoueFhYKkSCL0h5X_d5BARCvexvZJU5FoWdXBcyxFdwk91UCL_7sZ5U4fmRxQg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 977K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 12:20:57</div>
<hr>

<div class="tg-post" id="msg-128165">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from112222</strong></div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/128165" target="_blank">📅 12:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128164">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVarzesh+plus | جام جهانی با ورزش پلاس(K_B9)</strong></div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/128164" target="_blank">📅 12:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128163">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
پزشکیان: زیر بار زور نمیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/128163" target="_blank">📅 12:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128162">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل، کاتز : قرار نیست از لُبنان عقب‌نشینی کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/128162" target="_blank">📅 12:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128161">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
العربیه به نقل از منابع آگاه: آمریکا بر اساس این توافق متعهد می‌شود عملیات نظامی را در تمامی جبهه‌ها متوقف کند.
🔴
تعهد آمریکا به توقف عملیات نظامی شامل جبهه لبنان نیز می‌شود.
🔴
آمریکا بر اساس این توافق متعهد به رفع محاصره ایران است.
🔴
توافق بر رفع تدریجی تحریم‌های آمریکا و سازمان ملل علیه ایران انجام شده است.
🔴
ایران بر اساس این توافق متعهد می‌شود تنگه هرمز را ظرف ۳۰ روز باز کند.
🔴
ایران بر اساس این توافق متعهد می‌شود از تولید یا دستیابی به سلاح‌های هسته‌ای خودداری کند.
🔴
مذاکرات [اتمی] طی ۶۰ روز انجام خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/128161" target="_blank">📅 11:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128160">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d904eacc8.mp4?token=hjzpLzIpXN02onplQRXCuAdjtBqT_UMzVn2O_mwFKRQiE-b8XNSsW85hRUJ0I7sTBWxFCNVj1q5YzX6v3ieQcsFhuyHxLeJnICclLtj77FZcLsNkO-JX3NBrXTh9Ayz7CRaF07gUvdGwkqTEAijxxyJs0_pGhSM-2hOo63INKk7Bl9idJf6OML_uCABU1Koiw_BwQI8vqISqzQb0I7KC29WlAZJxRS8-kXzOK_PeS81Xq088oitGPJTxZLRaV2ECeWRYfDHRq6g6mAdvN60nAhmkWbqaxKe6P5UFWZby9gwQTkygwP-qYttlm7LIQYV9JRahA5ZaWKDW_PuMdx62KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d904eacc8.mp4?token=hjzpLzIpXN02onplQRXCuAdjtBqT_UMzVn2O_mwFKRQiE-b8XNSsW85hRUJ0I7sTBWxFCNVj1q5YzX6v3ieQcsFhuyHxLeJnICclLtj77FZcLsNkO-JX3NBrXTh9Ayz7CRaF07gUvdGwkqTEAijxxyJs0_pGhSM-2hOo63INKk7Bl9idJf6OML_uCABU1Koiw_BwQI8vqISqzQb0I7KC29WlAZJxRS8-kXzOK_PeS81Xq088oitGPJTxZLRaV2ECeWRYfDHRq6g6mAdvN60nAhmkWbqaxKe6P5UFWZby9gwQTkygwP-qYttlm7LIQYV9JRahA5ZaWKDW_PuMdx62KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آخرشم هچی که هچی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/128160" target="_blank">📅 11:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128159">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
الجزیره: شهباز شریف شخصاً در مراسم امضای توافق شرکت خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/128159" target="_blank">📅 11:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128158">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
یه سریا باید از امشب شام درست کنن دیگه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/128158" target="_blank">📅 11:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128157">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">میدان با تو خیابان با ما</div>
  <div class="tg-doc-extra">کربلایی حسین طاهری</div>
</div>
<a href="https://t.me/alonews/128157" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">😐
😐
😐
😐
🖋
🖋
🖋
🖋
🖋
🔖
🔖</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/128157" target="_blank">📅 11:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128156">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
قیمت دلار 163,500
🔴
طلای ۱۸ عیار 17,000,000
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/128156" target="_blank">📅 11:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128155">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3880986582.mp4?token=aqG9gJxDWCKItE34Wv30ZQDX7g9it-H-4ZmKQji1RdDFEMMyoLuMW6NfLAyAyIHVviLPsGodOK9U2b2pnbQxa5kw7TF3KwXKZ8jyqHz2ry-48F_lDMurjsCJRLIaE3in202yP0v-1vzZa7dlx_MNe0vDt9lrbyG8SPZO9ZjHLbyvSJ4_LLYp6hLrvNzL6sW1zIfoHQXnhRU1dRRSAsGjBfSjvi12FbUc2ic-MHS8iaXyCiD-QOHQRjcYmpzPGZXglSQT_ABWaZ3sPXsKkHDn9roiEEzghdcChUJFMss0sS4fjgJ57dbXkK-IMtiW3XPFV-T6QZxb6RSbNJidoKRP1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3880986582.mp4?token=aqG9gJxDWCKItE34Wv30ZQDX7g9it-H-4ZmKQji1RdDFEMMyoLuMW6NfLAyAyIHVviLPsGodOK9U2b2pnbQxa5kw7TF3KwXKZ8jyqHz2ry-48F_lDMurjsCJRLIaE3in202yP0v-1vzZa7dlx_MNe0vDt9lrbyG8SPZO9ZjHLbyvSJ4_LLYp6hLrvNzL6sW1zIfoHQXnhRU1dRRSAsGjBfSjvi12FbUc2ic-MHS8iaXyCiD-QOHQRjcYmpzPGZXglSQT_ABWaZ3sPXsKkHDn9roiEEzghdcChUJFMss0sS4fjgJ57dbXkK-IMtiW3XPFV-T6QZxb6RSbNJidoKRP1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما سرود پیروزی پخش کرد :
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/128155" target="_blank">📅 11:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128154">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: حدود ۱۰ ساعت از اعلام توافق بین واشنگتن و تهران می‌گذرد اما نتانیاهو هنوز در سکوت به سر می برد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/128154" target="_blank">📅 11:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128153">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزارت خارجه کویت: از توافق میان ایالات متحده و ایران استقبال می‌کنیم و از نقش پاکستان و قطر که در دستیابی به آن نقش داشته‌اند، قدردانی می‌کنیم.
🔴
امیدواریم این تفاهم، حسن همجواری و عدم مداخله در امور داخلی کشورها را تقویت کند.
🔴
از همه طرف‌ها می‌خواهیم با روحیه‌ای مثبت و سازنده در مذاکرات آینده مشارکت کنند تا ثبات تقویت شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/128153" target="_blank">📅 11:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128152">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39f0972d8b.mp4?token=rmFuDvPls5RDpTq_WVYfGg1GEf-uICITIYP_2wuoUH77N6LUvjZHtb1aokRatEvP1R8EUWKcST1bX3Fhk7_-k9JYVEvKYqgquJcM3nGi36yvFh7hr-VS5XCTvymglAquwK4FBzBd5TRkw8nD2mRASjPMBAYA4GAzUKIyg7grNnJUoC3PO853sM19uNSL2cFTKGW44o8INJZtue7Tk2qjAe3rLRnv8piNLywJbxqGKRxoYuBKihrIEpxZaineRxGmKwwquWDSZv2c71BFGFLHxIHgP8Nl3_CUnJDuH2QyOIf_5Twuvo5FMATffe62KXjIlptLpiyddonwenbTfWBzgTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39f0972d8b.mp4?token=rmFuDvPls5RDpTq_WVYfGg1GEf-uICITIYP_2wuoUH77N6LUvjZHtb1aokRatEvP1R8EUWKcST1bX3Fhk7_-k9JYVEvKYqgquJcM3nGi36yvFh7hr-VS5XCTvymglAquwK4FBzBd5TRkw8nD2mRASjPMBAYA4GAzUKIyg7grNnJUoC3PO853sM19uNSL2cFTKGW44o8INJZtue7Tk2qjAe3rLRnv8piNLywJbxqGKRxoYuBKihrIEpxZaineRxGmKwwquWDSZv2c71BFGFLHxIHgP8Nl3_CUnJDuH2QyOIf_5Twuvo5FMATffe62KXjIlptLpiyddonwenbTfWBzgTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوش‌چشم تحلیلگر ارشد صداوسیما:
من تعهد می‌دم ترامپ به شهباز شریف گفته حرف من دیگه خریدار نداره، بیا توییت بزن بگو توافق نهایی شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/128152" target="_blank">📅 11:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128151">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
رسایی: اینترنت رو قطع کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/128151" target="_blank">📅 11:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128149">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
خوارج برای امشب فراخوان دادن که همگی بریزن تو خیابون، تازه میگن مجتبی زنده نیست!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/128149" target="_blank">📅 11:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128148">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nM9ttbrYNTTNckAPSWcTLU3IVsD0gA0SFmlNcabBdP7WQMwUMF-sdqe4KazspUIFIFb5ZHfKuqgAdp3kQ42CJ6u5rb30IBCW62ddKo7q05kKGFLdo8eFTbvMSE2uTFEsduHAecoxNkCNcuUhWhiznWgz-1EFl0QlkkuuicNcnt-FHmtJxPDcXtdLUZaKjU1fkv5LrKtjDB0kQcWQiDr4z_1NDDAQ0kKqEkmHgEG_IAJEWMjN6gzQHliLTc-IvqpemFYDx7E5JW1a0UiatMYvFLFMqUF2rw-Pe9AoUZSotZL012cg1GL6ltH05LAtgX8SRPYA7YljZIpaF_iK3hDDXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوارج برای امشب فراخوان دادن که همگی بریزن تو خیابون، تازه میگن مجتبی زنده نیست!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/128148" target="_blank">📅 11:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128147">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dx1BPUCVEOtQ9JButpSrd8LV04KKDh30UuX5uMS2zCiloOsZaWkitrP23KRkmGSGHXCa97heAtW4ZBJOypwdtQUC8FjV0DZxAryR8jVzF5VR0OgH6Ehp1_SiYOudye3dsXwBIYgilcfOKA-ltdMMb8uFh_j2bl4CNNOuXSsg4MaS59RkMZ0PLEC0mXdIENhTvlO6N1h5vmg1fZrTLcQsDJKq8Hu6T5KVYH7179Jy33OSQJuacUAfXwByOwqclQAeXqsWeRfsU3RFrrDLR5D8BkPf4k35VnNju9cHDqtEUQ7SLnFPYPHwjAiRM8nHC2Juza3JBojpCWOtLxMqmCpsow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیده شده در مینی تجمعات
🔴
آمریکا انتقام هلیکوپترش رو گرفت اما ما انتقام رهبرمون رو نگرفتیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/128147" target="_blank">📅 11:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128146">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgVwPoYS3b2qDtos7MCSF37xHewH3b6Iy3kBUGhpvGxcyBG0oeSiZT3hgKjhUpF69ifRJK9DE7boeAF4mMofUuns7c1v2N-2ekRAZ4rWuUcnUhUY5ANXHsRUmKE3yoMTUHUvGJqHhdS22zh2ATjf7BWfvu8BAR2O9M3ct1rhXCYeJO6dpq-8Idt0-FeEYt26l3KCnXk7NBrbGXU9Jv9JSPLvDC-tmmWpy3Fx4Wjm9qwk7kVBrQXnfudxpgtx9lCFKM9aRuDV-ms3aJ3bLv9NQXwsN1K6WyclsMQatu3XHSwfx0_KxoXrgPlWM-uxxlPXwmRS3842-aEzZxOC7qiKkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فواد ایزدی: جمهوری اسلامی الان یک ابرقدرت فرامنطقه‌ای هست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/128146" target="_blank">📅 11:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128145">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
نخست وزیر پاکستان: پیروزی برای صلح، موفقیتی برای دیپلماسی و رد جنگ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/128145" target="_blank">📅 11:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128144">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
نخست وزیر پاکستان: به رئیس جمهور آمریکا، رهبر ایران و رئیس جمهور ایران به خاطر دستیابی به توافق در یک دوره دشوار تبریک می‌گویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/128144" target="_blank">📅 11:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128143">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
عراقچی: واشنگتن مسئول اجرای توافق است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/128143" target="_blank">📅 11:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128142">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
پیت هگست: نیروهای آمریکایی توی منطقه باقی میمونن و اگر ایران به تعهدات خودش عمل نکنه، محاصره دوباره اعمال میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/128142" target="_blank">📅 11:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128141">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oewStBZHNutKCY1MeZY6CXTmmG1ph3pqNClEKkv6DDHVArtuG1z0Ozcd3KN2XeC50zXLU8cytY36VGFR9fjyVcmowD6SqJHb3I8xti-at6Ee6HsKPvdQua4H4DE6x26yL6R9_-aUqQrL65OlsLdQXIO3D281GjoiZrxdZHPbqwUO_MveY7X1vY-DXym2ljV22HVI-bUW6in_OUq-DQ-a2l8l3eGosfarBSfvBcD2JL8opy-t83bCg6UMerCmqgeuaapj-ygAHGd3gJ11PWeVHlYh27D3USM3CCd_jPjGRNmMHXK1dxD97mDKLY6ePF_1epPaYUlV_8uzzjVD8Uyn7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت وارد کانال ۷۰ دلار شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/128141" target="_blank">📅 11:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128140">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767073432d.mp4?token=RbklgoeREO-UZJlctb20Tw-yqYdabgzmXSnV_TgH2QmAW1ZvpMk6w4F8lFCFHZMnXPtMvWN9O4S_FJGk1BSkv0pQUAcCy_avpjPKYWjy-NPAhiGJh-xtOi44KzPu7JA2twJOyqsb4b3Qrau0TlP0KPOgCmnOZjLZ8W73XAefcN2JirsapL1k-c_4jPV1wqagmIIc9vif_lKproU-S4Lyhf7GQdAeskBCbK_wQntF7CGPWZGj2W9hAocDCRqihgsmqgejmiHFKxdQi6uwAcCV1MzNYsY8mIcJ_dJYBoR9KrlqPn_5R5VxeBNDlDbp2i3vb_r8RHw9gemkNPo7n2EdWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767073432d.mp4?token=RbklgoeREO-UZJlctb20Tw-yqYdabgzmXSnV_TgH2QmAW1ZvpMk6w4F8lFCFHZMnXPtMvWN9O4S_FJGk1BSkv0pQUAcCy_avpjPKYWjy-NPAhiGJh-xtOi44KzPu7JA2twJOyqsb4b3Qrau0TlP0KPOgCmnOZjLZ8W73XAefcN2JirsapL1k-c_4jPV1wqagmIIc9vif_lKproU-S4Lyhf7GQdAeskBCbK_wQntF7CGPWZGj2W9hAocDCRqihgsmqgejmiHFKxdQi6uwAcCV1MzNYsY8mIcJ_dJYBoR9KrlqPn_5R5VxeBNDlDbp2i3vb_r8RHw9gemkNPo7n2EdWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جشن و خوشحالی مردم جنوب لبنان در پی اعلام توافق پایان جنگ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/128140" target="_blank">📅 11:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128139">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
الاخبار: ترامپ مجبور شد امتیازات زیادی در پرونده لبنان به ایران بدهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/128139" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128138">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
گفتگوی تلفنی عراقچی با وزرای امور خارجه ترکیه، عراق و مصر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/128138" target="_blank">📅 11:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128137">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
وزارت خارجه عربستان: ما از آغاز مذاکرات تفصیلی میان آمریکا و ایران طی ۶۰ روز آینده استقبال می‌کنیم.
🔴
بر اهمیت بازگرداندن امنیت و آزادی کشتیرانی در تنگه هرمز تأکید می‌کنیم
🔴
امیدواریم که امنیت و صلحی محقق شود که امنیت منطقه و جهان را تقویت کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/128137" target="_blank">📅 10:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128136">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سی‌بی‌اس: رشد قابل توجه بورس‌های آسیا و جهش معاملات آتی «وال‌استریت» در پی توافق ایران و آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/128136" target="_blank">📅 10:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128134">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/alUMUt5IEEx27cJ6uPgwzJYn6oHG6pY91VUhMP5OOHrGUpnwr-hJAQPwlirewWlFi6f-HI1KGngto2AXGaLd61ZLbK88GldlrCH_r4TqVS84A7HfQYkZOuQrkflRZU2rynQgff2i-zEivlRQChPllvt6EfexwOWXp4F1N5zMBx4F9OIA1s7DbfEAaQicaB57JLFoVQGVEQmBXLdY1_a4CwxtMwTDQCBNqkYYv-5WM7XmESZtRZInuSgX-wj6UMomiXd_R62RLkkFC8R0xyGDxUmyuUHajYfTs-eDmHpZulB1fWnMekDAncTw9LaY1Xp7hj8nPB1wLbk4K_WsRUNVSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jo-LBsS4j0JyuSq2ZABtaimARfgE-iXFu754jR0UxnlV0fQVB4HNwT2tEgePyTTsI67NKs-qmRzst6KLSRg-62le5qtuFw0TaEDPXdra14Gg4raT7KbEUW_wxdQCI4xcsXqlaULloIhL2Xhp2ZAPc5fHkYMAUfTYHHW86lmVNurToEm9JvALLU9VND4h8EE5q4GNi9SkrpiqatWnSJue1FMVu0UTAMRus0MQT51qOVyQ45N28JeEw4tzm2cFkG_HvNjlbA9qUhdK7NxqyVH8LVut9NwX7CKoYoCVyaK6x9MfioeILk5p0kG5PVY9V5CHRX5NwsXn1elqne8sU1khEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله اسرائیل به الخیام جنوب لبنان!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/128134" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128133">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
لاپید، نخست‌وزیر اسبق اسرائیل: هنوز باید امیدوار بود گزارش‌های منتشرشده درباره توافق با ایران نادرست باشند، اما اگر درست باشند، با یکی از شوکه‌کننده‌ترین شکست‌ها در سیاست خارجی و امنیتی اسرائیل روبه‌رو هستیم؛ شکستی که کاملاً به نام نتانیاهو ثبت خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/128133" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128132">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
بنی گانتس، نخست وزیر پیشین اسرائیل
توافق با ایران یک شکست راهبردی است و نباید با محدود کردن آزادی عمل اسرائیل در لبنان موافقت شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128132" target="_blank">📅 10:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128131">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
شرکت ملی خدمات انفورماتیک دیشب از رفع اختلال خدمات مبتنی‌بر کارت ۴ بانک ملی، تجارت، صادرات و توسعه صادرات خبر داده بود.
🔴
بررسی‌های خبرنگار فارس و گزارش کاربران نشان می‌دهد در حال حاضر همچنان اختلال خدمات غیرحضوری و اینترنتی این بانک‌ها برقرار است.
🔴
این در حالی است که این بانک‌ها در اطلاعیه‌های جداگانه نیز از رفع اختلال تمامی خدمات کارتی از جمله سامانه‌های اینترنتی و موبایل بانک خبر داده بودند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128131" target="_blank">📅 10:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128127">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qSmiZH9xyFeRWpoMjho7fTuOJ3YWf-j1IZ1t20wstLSKp7bQg2ablqTyhefNTAYSC82REeWEXE4CAULWlDFftqvJBJYcuBeCnlHr2skpr1bTzMlBi2d3RDzdk6wxg5ggL43nCbApVuHebXxCa1Sv3_3QQrXfFclrcehDQNaPJSgXau7KWMQOHSsyPl2ZTCIrWGyHaAw4l9theyYMshlFOneON5fnhoJX-CDZPaHDuvhKvUSeg5JJpNYTHsUBVkVFLYNnGbD77Dz_NgRV7O5KBEodlN7sTM9p_NVvhT_70Iyafs6FBTRnWbtgHsroVmTiQHkP68NdxpzGibBXes43CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s791b9IuRWpwxBO6S_N2JdC5X4q0saFyCwGhZK3tdFyTWOCOT2fYjJm2fqZzS8P-j0ea6qtjdCtpqHArwI355-DiF8d0pTjpaoQLtsqscs-lgsDYy30rfsHMYzm73EDs5dg6IgNbZUbgxRLHwkpBryh_gE1wVJNjxHp8NrD1E0PgJpxImT1U6wUiGQo-roBzXBf2oKfi4rFt1bH8KSJBqWXxWGZCBUv5pt0WY6JFe6F9r7ofxOdQpWjNfgEPi9JHqFdPKlCdRAz_vvRZHqg7HBVTDqIFmNxFlyOOFQIaIRj6WofRW_fovb43C3UbZkwxQZUmC8e9uppeQXEwfyaBIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SWBuj3qo1D0bxsBwRHMQlIDxmSV5rUIweo2wYE7fF-Qm_nQyM2wZlSlXucY6BAAWaNxbYCN86dfLRwWIvjTyVCofWQd_TzrDPeGczJ2aXrnURVL9DcFKZTj6OsO8kCZBhMQMDjxCQR0u91EUayqTmXNbUgncixNZV4lPnZZ_mmeqfYUuGyVyfuWf49JaoiXn28ClLPiFDFYtmCMVUOnAxafwM5x6Qb9xg8rsTuOBx9quFB4zl1q51ANk3ftwwvmHHDz-UvMnhypy7sn-bap5V22S6C1RKVOFs74w8Hd9TgdOVog_zqLHIw-4Ce5qDu2APyNNxxHXAAqiZ7bXJrdMgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e011b2203.mp4?token=iL5XIZ7zUgBChVjFTF7RM54zaHn17u0rrS66-pV-Rj7YhKD4cuJu_hDDaNIiW2ls9md7_3R0ZFNB1CMm2gzY92c5dKiUexWakJTE7tewCgJiAGy7xz6bRFbqG9BDp_ujUAWoR19zRF-k_1tCgCGcMnSUBHAhgf407hb4o969IBgJen0VSkP0X5wdlaI10lZh_QPs4d1_BBBdpa-_U_mRsbCb9cEXt33dpztGNDA1m9kqDtG4hgTU55UBorCcBvSKRgq8nVkfF173KWGWRgTj_N12NRQyAVN19wnOKhEOim1ZEI-ARuXD4UrNgahtHF1ZyeyyGaihOLBf1DBgrgRRVGZgQR-hxLEL1y1T1lwcKGVKk3jc7SvDFlBxA0JrZsM25rzGrD5x1-_wEaqTrLlDWrn-ZuRcjh6MsglUBC02FnTCr4-e--JZkLXM4Wk-ye9G01xGdTH7LIsQ8vHAzPxxFnk9avx_BrT6A-o-DiwuEtQcfqwEc-gLiN5FjUtFtqb7bTO5CC8X2WEghXIRGVDAZmGaFqaa-4NkFo5MDAGwWPrXslz_pLjGfKoWPkt0QHCJrPP1VvAShMBHX8QQAula7WRq4UF21aUr5Z8xyzvpD483j5jlVKIjgFpIvof4ot01_Abmows63nsnUhlBi4-4R05DtgeD14jJ6E_ek662jwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e011b2203.mp4?token=iL5XIZ7zUgBChVjFTF7RM54zaHn17u0rrS66-pV-Rj7YhKD4cuJu_hDDaNIiW2ls9md7_3R0ZFNB1CMm2gzY92c5dKiUexWakJTE7tewCgJiAGy7xz6bRFbqG9BDp_ujUAWoR19zRF-k_1tCgCGcMnSUBHAhgf407hb4o969IBgJen0VSkP0X5wdlaI10lZh_QPs4d1_BBBdpa-_U_mRsbCb9cEXt33dpztGNDA1m9kqDtG4hgTU55UBorCcBvSKRgq8nVkfF173KWGWRgTj_N12NRQyAVN19wnOKhEOim1ZEI-ARuXD4UrNgahtHF1ZyeyyGaihOLBf1DBgrgRRVGZgQR-hxLEL1y1T1lwcKGVKk3jc7SvDFlBxA0JrZsM25rzGrD5x1-_wEaqTrLlDWrn-ZuRcjh6MsglUBC02FnTCr4-e--JZkLXM4Wk-ye9G01xGdTH7LIsQ8vHAzPxxFnk9avx_BrT6A-o-DiwuEtQcfqwEc-gLiN5FjUtFtqb7bTO5CC8X2WEghXIRGVDAZmGaFqaa-4NkFo5MDAGwWPrXslz_pLjGfKoWPkt0QHCJrPP1VvAShMBHX8QQAula7WRq4UF21aUr5Z8xyzvpD483j5jlVKIjgFpIvof4ot01_Abmows63nsnUhlBi4-4R05DtgeD14jJ6E_ek662jwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم‌های اضافی از لاورای پیچرسک کیف پس از حمله اخیر روسیه به کیف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128127" target="_blank">📅 10:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128126">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل به‌نقل از یه مقام ارشد:
توافقی که داره صورت میگیره فاجعه‌بارترین توافق تاریخه. از نخست وزیر گرفته تا رئیس ستاد ارتش کل غیر از این فکر نمیکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/128126" target="_blank">📅 10:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128125">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
رئیس کمیسیون اروپا: توافق میان آمریکا و ایران باید به بازگشایی تنگه هرمز منجر شود و مسیر را برای مذاکرات گسترده‌تر درباره صلح باز کند. این توافق باید به برنامه‌های هسته‌ای و موشک‌های بالستیک ایران پایان دهد.
🔴
توافق باید به فعالیت‌های بی‌ثبات‌کننده ایران در منطقه را پایان دهد و تا زمانی که لبنان درگیر بحران باشد، صلح در خاورمیانه محقق نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128125" target="_blank">📅 10:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128124">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
وزیر امور خارجه فرانسه: ما خواهان برقراری آتش‌بس در همه جبهه‌ها هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/128124" target="_blank">📅 10:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128123">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/459a20a0de.mp4?token=DgWn76uV6_WYsjAZrbcKd4HX86nVYiPf0O-ePgWHlfg79DAAIlnXcGMvvHcXOMXhKEH1G-PCtTO7eVmPxDhxg7A8PJomt7j4Y3HgX_qNKvkKCSE-lrxQmPXMYNTDgN9TLqW66Rbe_WIvUn9KGXHUcsygHKx8AukbyUWr5Z7jiTq8JdUm5IjJ9XTl7kGwN8dmXyav2HM64VuAR6ERJLFcFoKy8laL_XPBH-7JhfusBmdJth6_HYJFa39d2MHjdD4REpRLgY2L7NODWFBnvYzUkakTZ1XdZRWumvvozPjnPyjd2ZvxIowTsuEQQZJPPTB5udo5czdladfqaiYWEK2CSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/459a20a0de.mp4?token=DgWn76uV6_WYsjAZrbcKd4HX86nVYiPf0O-ePgWHlfg79DAAIlnXcGMvvHcXOMXhKEH1G-PCtTO7eVmPxDhxg7A8PJomt7j4Y3HgX_qNKvkKCSE-lrxQmPXMYNTDgN9TLqW66Rbe_WIvUn9KGXHUcsygHKx8AukbyUWr5Z7jiTq8JdUm5IjJ9XTl7kGwN8dmXyav2HM64VuAR6ERJLFcFoKy8laL_XPBH-7JhfusBmdJth6_HYJFa39d2MHjdD4REpRLgY2L7NODWFBnvYzUkakTZ1XdZRWumvvozPjnPyjd2ZvxIowTsuEQQZJPPTB5udo5czdladfqaiYWEK2CSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخستین شناوری که پس از اعلام توافق صلح میان ایالات متحده و جمهوری اسلامی ایران از تنگه هرمز عبور کرد، نفتکش گاز طبیعی مایع (LNG) با پرچم مالت به نام “دیشا” (Disha) است که از طرح تفکیک ترافیک دریایی ایران استفاده کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/128123" target="_blank">📅 09:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128122">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
کایا کالاس، مسئول سیاست خارجی اتحادیه اروپا: ایالات متحده و ایران از دستیابی به توافقی برای پایان دادن به جنگ و بازگشایی تنگه هرمز خبر داده‌اند.
🔴
این توافق یک گشایش احتمالی محسوب می‌شود، زیرا زمینه لازم را برای انجام مذاکرات عمیق درباره برنامه هسته‌ای ایران و دیگر مسائل حیاتی فراهم می‌کند.
🔴
انتظار می‌رود این توافق، در صورت اجرا، به کاهش بحران جهانی انرژی کمک کند.
🔴
من طی روزهای گذشته با همتایان خود در ایران و کشورهای خلیج گفت‌وگو کرده‌ام و وزرای خارجه اتحادیه امروز درباره راه‌های مشارکت مؤثر در مرحله بعد بحث خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/128122" target="_blank">📅 09:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128121">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
شاخص کل بورس تهران امروز دوشنبه ۲۵ خرداد ۱۴۰۵ در ۵ دقیقه ابتدای معاملات، با افزایش ۱۱۱ هزار واحدی، معادل ۲.۳ درصد رشد کرد و به محدوده ۴ میلیون و ۹۲۹ هزار و ۵۳۱ واحد رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128121" target="_blank">📅 09:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128120">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
بن گویر: توافق ترامپ الزام‌آور نیست؛ اسرائیل کشور مستقل است
🔴
ایتامار بن گویر، وزیر امنیت ملی اسرائیل، می‌گوید توافق ترامپ «ما را ملزم نمی‌کند»، اسرائیل «یک کشور مستقل و دارای حاکمیت» است و تابع ایالات متحده نیست.
🔴
بن گویر می‌گوید اسرائیل نباید چیزی کمتر از خلع سلاح حزب‌الله را بپذیرد، نباید از هیچ سرزمینی که توسط نیروهای اسرائیلی تصرف و پاکسازی شده است، عقب‌نشینی کند و نباید در پاسخ به آتش‌سوزی به سمت اسرائیل سکوت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/128120" target="_blank">📅 09:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128119">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
رابرت مالی، مذاکره‌کننده سابق آمریکا و نماینده ویژه در امور ایران:
🔴
«این تفاهم‌نامه یک دستاورد مهم و خوشایند است، زیرا تنگه هرمز را دوباره باز می‌کند؛ گذرگاهی که بسته شدن آن هزینه‌های ویرانگری را بر میلیون‌ها نفر در سراسر جهان تحمیل کرد. اما این تفاهم‌نامه همچنین محکومیتی روشن و قاطع علیه جنگی است که پیش از آن رخ داد، زیرا مهم‌ترین دستاورد آن بازگشایی آبراهی است که تنها به دلیل همان جنگ بسته شده بود.
🔴
در مورد مسائلی که پس از این تفاهم‌نامه باید حل‌وفصل شوند ــ از جمله سرنوشت برنامه هسته‌ای ایران، وضعیت اورانیوم غنی‌شده و دامنه کاهش تحریم‌ها ــ تقریباً به‌طور قطع به آینده موکول خواهند شد و حل آن‌ها احتمالاً دشوارتر از قبل از جنگ خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/128119" target="_blank">📅 09:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128118">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLurIVdIXxFSfMcAoKbRxLTzvDTCaRyqH89Gu0Q3A82yUqVk1v32vR4MFLkHMUtJBnD6b6TWE7supNcFbvYNM6ifVxgXAvF-kqw8dz6P7sfJv9OwIcIiDD4XZLlxXmEPJBkRJLRNKz6pWvD-gawlGf_Ap91ZDBL206WLj-dWSuaX88oVS-lzJ04Z5PfOs7NwGIp31ztFzzsdubQU1xrxo5KaFqkW3Tl4Pj_F-dS0ZdZSlEy-awH3VwSX9kunYfbCO_E_fCNjm8ebCn_FKMq6CU2gXnQabEG5UgRQpFrEdW5XCIRchfMFNXwUHEuq9tbrh_fj-HoVjTCGLa6eeN9acg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بهروز رضوی از چندی پیش در بخش مراقبت‌های ویژه بیمارستانی در کرج بستری بود و ساعت ۲۳ شامگاه گذشته یکشنبه ۲۴ خرداد ماه در همین بیمارستان دار فانی را وداع گفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/128118" target="_blank">📅 09:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128117">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وزیر خارجه اسپانیا: از اعلام تفاهم میان ایالات متحده و ایران استقبال می‌کنم و تلاش‌های میانجی‌ها را ارزشمند می‌دانم.
🔴
آزادی و امنیت کشتیرانی در تنگه هرمز دو موضوع حیاتی هستند.
🔴
گفتگو و مذاکره می‌تواند مسائل باقی‌مانده را حل‌وفصل کرده و آتش‌بس را، از جمله در لبنان تضمین کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/128117" target="_blank">📅 09:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128116">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
رودز، معاون سابق مشاور امنیت ملی اوباما: این توافق یک آبراه را باز می‌کند که پیش از جنگ نیز باز بود و مذاکرات هسته‌ای را آغاز می‌کند که از آنچه ترامپ پیش از جنگ دنبال می‌کرد، بسیار محدودتر است.
🔴
همه این‌ها با هزینه‌ای سرسام‌آور برای کل جهان انجام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/128116" target="_blank">📅 09:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128115">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb518487dc.mp4?token=ri_BZKF1i72x-9JZQIgTYrDnvolBXnQoRw2YPbXVF3OF7-C8BzZIROcOW0o2oXBzBElECvO48-ZwR8z56pAXpJXIdn7AJOjqpsOl5rzzF5G5XVB5aKmhPsZakOEglGDNbfpP8Z7cewJ61oVjNl5p9k9W5zxZadb95nnpUjIQi_1vpzBvdXV73c-Ti72JzPTK-Xofi3-HTD7wCDiAvcUum8Pr1NKyvE3hEb_ShBLlHJx1wG0b5PPgUVKzigk2vQg72939zd63kIPjoQPwbDYwzKyOsWuLyHcumCRKvetxmphfKxnRBL9Do-Re_BHUq9uaVKlVV6gCAedUrwbAa9-J5jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb518487dc.mp4?token=ri_BZKF1i72x-9JZQIgTYrDnvolBXnQoRw2YPbXVF3OF7-C8BzZIROcOW0o2oXBzBElECvO48-ZwR8z56pAXpJXIdn7AJOjqpsOl5rzzF5G5XVB5aKmhPsZakOEglGDNbfpP8Z7cewJ61oVjNl5p9k9W5zxZadb95nnpUjIQi_1vpzBvdXV73c-Ti72JzPTK-Xofi3-HTD7wCDiAvcUum8Pr1NKyvE3hEb_ShBLlHJx1wG0b5PPgUVKzigk2vQg72939zd63kIPjoQPwbDYwzKyOsWuLyHcumCRKvetxmphfKxnRBL9Do-Re_BHUq9uaVKlVV6gCAedUrwbAa9-J5jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مرضیه وحید دستجردی، دبیر ستاد ملی جمعیت: اگر با همین دست فرمان پیش برویم؛ در سال ۱۴۳۰ سالمندترین کشور منطقه خواهیم بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/128115" target="_blank">📅 08:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128114">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار کنترل شده در محدوده مبارکه اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/128114" target="_blank">📅 08:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128113">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c778099306.mp4?token=o6alLavPEzoxMom5xySlM2XsyB6Cdj0aDUlgMjbChYdUYpYvA4sQTM-0XHR4kFXzGUDTU4AC0cJAlHtBmKqWp8sfjpL_S6taBT5baTBq7OMTkcy2QyzJtQ04eFi0Mo20XkQTjeXGUeLzkVFlhk_AZeW-c0kATG6KUrU8fKGUWUps80PNqdt7PcgmBw9yX3jjJmtFIKFm88nesk80hP3wlwKWn7GfB_8AH5qKgT3mVnNi_L6FlN433w7SW_MQ5WKEA-yi1je7DcVhK7AvWy6Ur_KEPQswGxrsedxAKBoIgpyPdTvnqdktZxVWtL_Ihz5nCdjNrG8fY6PelPcKBtlErg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c778099306.mp4?token=o6alLavPEzoxMom5xySlM2XsyB6Cdj0aDUlgMjbChYdUYpYvA4sQTM-0XHR4kFXzGUDTU4AC0cJAlHtBmKqWp8sfjpL_S6taBT5baTBq7OMTkcy2QyzJtQ04eFi0Mo20XkQTjeXGUeLzkVFlhk_AZeW-c0kATG6KUrU8fKGUWUps80PNqdt7PcgmBw9yX3jjJmtFIKFm88nesk80hP3wlwKWn7GfB_8AH5qKgT3mVnNi_L6FlN433w7SW_MQ5WKEA-yi1je7DcVhK7AvWy6Ur_KEPQswGxrsedxAKBoIgpyPdTvnqdktZxVWtL_Ihz5nCdjNrG8fY6PelPcKBtlErg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ساکنان در حال بازگشت به خرابی‌های ایجاد شده در منطقه نابتیه در جنوب لبنان هستند که بر اثر حملات اسرائیل به وجود آمده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/128113" target="_blank">📅 08:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128110">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nXuOZ7kTRijVBYWUdr8wAYVPI3XHv6mAUSkRWDlHADQMmSCskS1DK0B5WQKvyhemlAsKqHUsgVKkXg-O8Orq_pSu8fJSaYmms3Qej_EXwqrQqz27rTReEyxGG-K1UuoiFNuORE_HBnRyHGWv3gvU8IgLYEMkGkZciR0QyJQxMYzypWJQBOlTr43yzeZeIGgMPQdmyk4DAfWqhCgdctOPicIVGLe3JE3RDAJPoZItJD5qXqr9CM8ffzPZjCTbzyEAZ__tcv6M_XeUFmeKE5dk6fEFRtmQ_DQtako-814_VmzjYkEWU3CLUXvga6kOVRfIMLd2dBD5DOyuE2vrdfnRUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b9qlxhl37GdrCExuWyVFCd53Zj0PBSY_FmKh5ybemcUnxpwuRGIw--eTJ9aMmWKRW34s_uY5bpMh2fF0cs04QkGZ55qAsjca72_iIw-1XiB8G2ej6kjDYFsVAC94haJ32KUca8DfSIwqlPcbfjg3zzWSqDkwN2CieRmlWHRuVQIQG_NEHiHeyARZYWWpacvFEP8gGpK4mnRcNOuW290stjdS49VftsHDWomnqAlEG-15CfpetDGeZRGU5VNOmGrNjEGn7yvBOn945TcOk2KLaKdrqiZZnuwcc9MOt_f6yGAcYtJjLL7srw_EzEDN-i3-AFT0PMYHsYm53yJYjok88w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8242749f2d.mp4?token=td_IfQQkshxqgHFIF7QiqWlLHjFDDPp-quRKpYWVB7_PPqKRwcy95FVgdHHk4R6b75c9UdpX6LMFhutTm4pkx3OhEYua9W8O7xzZM7nPN3yjJWrEOfInasr8FZhuLIp0xoSJ0t_EF2BZt4QxG188c91CQJzRyO6xS-zMmoxyDaXrIohC40V2uvY3JsjzV-GIsPBB_vcqJmcEPlJcqujEbyLvxQFk_yedbDgaKYFsZ1azrfi1dWuRxLuRYfmsvV-Gw0l_kUD4kfWaegD1DxPOfz9eVzAYrAETwFGcMOyn98vUZisOYx1qGnNHNhc74PBMxaQqBrabLWBa8J7LX0jsHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8242749f2d.mp4?token=td_IfQQkshxqgHFIF7QiqWlLHjFDDPp-quRKpYWVB7_PPqKRwcy95FVgdHHk4R6b75c9UdpX6LMFhutTm4pkx3OhEYua9W8O7xzZM7nPN3yjJWrEOfInasr8FZhuLIp0xoSJ0t_EF2BZt4QxG188c91CQJzRyO6xS-zMmoxyDaXrIohC40V2uvY3JsjzV-GIsPBB_vcqJmcEPlJcqujEbyLvxQFk_yedbDgaKYFsZ1azrfi1dWuRxLuRYfmsvV-Gw0l_kUD4kfWaegD1DxPOfz9eVzAYrAETwFGcMOyn98vUZisOYx1qGnNHNhc74PBMxaQqBrabLWBa8J7LX0jsHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لاورای پیچرسک کیف، یکی از مهم‌ترین نمادهای مذهبی و فرهنگی اوکراین، در جریان حمله شبانه روسیه به کیف دچار آتش‌سوزی شد.
🔴
هنوز مشخص نیست که آیا این صومعه به طور مستقیم هدف قرار گرفته یا توسط بقایای موشک‌ها/پهپادهای رهگیری شده آسیب دیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128110" target="_blank">📅 08:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128109">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
بازارهای سهام آسیایی در روز دوشنبه پس از اعلام توافقی برای پایان جنگ ایران، جهش کردند.
🔴
شاخص نیکی ۲۲۵ ژاپن ۵.۵٪ افزایش یافت، در حالی که شاخص کوسپی کره جنوبی تا ۵.۷٪ رشد کرد.
🔴
شاخص تایکس تایوان تا ۲.۷٪ افزایش یافت، شاخص ASX 200 استرالیا حدود ۱.۵٪ بالا رفت و شاخص هنگ سنگ هنگ کنگ ابتدا حدود ۱٪ افزایش یافت اما سپس بخشی از سود خود را از دست داد.
🔴
آینده‌های سهام آمریکا نیز پیشرفت کردند، با افزایش ۱٪ در آینده‌های S&P 500، رشد ۱.۸٪ در آینده‌های نزدک و افزایش ۰.۸٪ در آینده‌های داو جونز.
🔴
در همین حال، قیمت نفت خام برنت حدود ۴.۵٪ کاهش یافت و به زیر ۸۳.۴۰ دلار در هر بشکه رسید، زیرا نگرانی‌ها درباره اختلالات در تنگه هرمز کاهش یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/128109" target="_blank">📅 08:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128108">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
وزیرخارجه پاکستان: از هر تلاشی برای تثبیت توافق ایران و آمریکا حمایت می کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/128108" target="_blank">📅 08:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128107">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
صدراعظم آلمان: از توافق میان آمریکا و ایران استقبال می‌کنم؛ این توافق یک دستاورد مهم دیپلماتیک است.
🔴
این توافق راه را برای اقتصادی جهانی پویا‌تر و خاورمیانه‌ای امن‌تر هموار می‌کند.
🔴
اجرای قاطعانه و مصمم آن اهمیت زیادی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/128107" target="_blank">📅 08:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128106">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از مقام‌های ایرانی گزارش داد که محمدباقر قالیباف و عباس عراقچی برای امضای توافق راهی ژنو خواهند شد.
🔴
به گفته این مقامات، ایران عمداً تا پس از نیمه‌شب به وقت محلی صبر کرد تا امضای توافق با سالروز تولد دونالد ترامپ هم‌زمان نشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/128106" target="_blank">📅 08:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128105">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
فاکس نیوز: میانجی‌گران قطری پس از ۱۷ ساعت مذاکرات فشرده، تهران را ترک کردند
🔴
یک دیپلمات به فاکس نیوز گفت: «توافق حاصل شده است و جلسات مقدماتی جداگانه با هر یک از طرفین این هفته در دوحه برگزار خواهد شد، پیش از امضای رسمی در سوئیس و آغاز گفت‌وگوهای فنی.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/128105" target="_blank">📅 08:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128104">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
معاریو : نتانیاهو به ترامپ گفته که اسرائیل نیروهای دفاعی خود را از لبنان خارج نخواهد کرد و خود را ملزم به رعایت این بخش از توافق نمی‌داند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128104" target="_blank">📅 08:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128103">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سی‌ان‌ان: ترامپ از حملات اسرائیل به لبنان به‌شدت خشمگین بود و در تماس تلفنی با نتانیاهو از الفاظ رکیک استفاده کرد.
🔴
روزنامه معاریو به نقل از یک منبع آگاه گزارش داد که تماس تلفنی روز یکشنبه میان نتانیاهو و ترامپ با تنش همراه بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128103" target="_blank">📅 08:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128102">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4b244R6rIUHVY8rt2JjqQ_T3S4Gwm6Hp4FJ3JnTq__44DgHvMryoGZp-fdazrYWEXPLuFoJWyTc3Iuh0ud3ajk97Zu4HVLhcRkDNnlak2I7JUrOkiQYl8YEPa0HjWOmc5xCzymhbA5XxQMQLlYF2qis6dcTzDdshCU1XvhZ8BNQ_padcBkXqxrnKGNVLoM2x7akNHIeRvyF8-9Jy9sKj5Q-91GtHqaBbCMlPfxWPBWDTqGBfKeyeTEKxIx3dQzVEHE8sanpfutm1s1gCkOZfrzI77oN_7WFU8bVWn2r2Elam65-r7I6PkTaRgUzhyAYxW6JCuuPvxODUlyUo7PLbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت فعلا روی محدوده ۸۳ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/128102" target="_blank">📅 08:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128101">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNdc78zgeK5_j-LbEL6j1xHDgC4ZmIziDwzorb2LD-IYcIUCojC1M9G_CBn6dbDfFMiDEsbOY14zNRXcLMLEARzK1Zxs83K2kpLPzih9doRybgQeriVrTbgXAPvudZSrXNyIm9gW9SRh_sxm_FN3E6u2mGbkmI4qN0f0ZqVuvnyC711nPllZQgLwKkkGzzgpVhCRsOE6EOvG5J9ZWsr4z066q9qSCJ1cP2x16wx2g6mCzOw11SbYYTqarGQFinfySUyoBZZTyNTcQhB0ieLJubu9PeVFnc6WhvtJiQV_3elPUNoOp9KWEkAv0R05id7xqVmtNDohb9SkHrWRfHu-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لیندسی گراهام: از شنیدن توافق با ایران برای باز شدن تنگه هرمز خوشحالم
🔴
طبق قانون ما، هرگونه توافق هسته‌ای با ایران برای بررسی و رأی‌گیری به کنگره ارسال خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/128101" target="_blank">📅 08:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128099">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
پرزیدنت پزشکیان: نظر یک گروه خاص(تندروها) مهم نیست و نظر همه مردم مهمه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/128099" target="_blank">📅 03:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128098">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ترامپ: توافق هسته ای شکست بخورد، حملات نظامی را از سر خواهیم گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/128098" target="_blank">📅 03:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128097">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ترامپ حق غنی سازی ایران را پذیرفت
🔴
ترامپ در گفت و گو با نیویورک تایمز مدعی شد: ایران برای همیشه به غنی‌سازی در سطوح پایین که تحت هیچ شرایطی نمی‌تواند برای اهداف نظامی استفاده شود، محدود خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/128097" target="_blank">📅 03:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128096">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
نیویورک تایمز: تهران نهایی کردن توافق را تا بعد از نیمه‌شب به وقت محلی به تعویق انداخت تا از همزمانی این لحظه تاریخی با تولد رئیس‌جمهور ترامپ در روز یکشنبه جلوگیری کند
🔴
اختلاف زمانی هفت و نیم ساعته به هر دو کشور ایران و آمریکا اجازه داد تا جدول زمانی مورد نظر خود را حفظ کنند، به طوری که ترامپ گفت توافق در روز یکشنبه نهایی شده در حالی که مقامات ایرانی تأکید داشتند که این توافق در روز بعد به پایان رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/128096" target="_blank">📅 03:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128095">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCvoVqC6LEpD8dg8MS-ZSyASjwnFxtdNTnkMBklOSt1dQxacau88YbLi82tAqRpGShbizvEKR8FdfGsDztXHwEH8Dw2nYaWWhSxeDca2vYxRmPmjqWszlave4eNFx0CYQcemD5U0ksDxidfR9cFlOmlIrqutYQT-5eBbrSanfZrki98wSSlLYxGE1QX5TI7z4FEsx9f_rRbZ82kd6HCT5LCS0CDcPorGLJcfUyh2P00iVkcLZu7q4PIqzPwwBaclD-20TJgdg-Mwje9WEOEfT4JlSEtzQwvCGoM1bWDRtmaKvUpbwEjWN7cEfmETROof_TnAniJeE-ortYWeppcF0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرزیدنت ترامپ به نیویورک تایمز:
نتانیاهو فرد بسیار نمک نشناسی است. او باید به شدت از ما بابت انجام این کار سپاسگزار باشد.
زیرا اگر ایران سلاح هسته‌ای داشت، اسرائیل دو ساعت هم دوام نمی‌آورد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/128095" target="_blank">📅 02:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128094">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">غریب آبادی
انقدرخودکار دزدید
که تفاهم نامه رو الکترونیکی امضا میکنند
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/128094" target="_blank">📅 02:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128093">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ea240da54.mp4?token=SzFeY3CO7ZZ8u1E2TUzM6De_V1zz9yV-_3RcspsulcNEuFHr5WJ8DuOVmDpijof_rhklz30C0h5sz10c5hxJq-TfuJVxd3DPMSJ_9bb87n-rXO89lQlD6VAT8r8h-VTBRM8LtMU9IqolAG00jnFmqQfhZ659W42xl4YfrUVzZGOpT7IPu4zarv2yOP1r9-V8lbnuMtYZLSqCNN8qj06RrJUuRlmkCIgh_PHZUow8A4Db4xGF_N5z0Th7UmN6dQ2BZdLla0JWEgL_aBktWb9wRIrCeGitVwpqfKCM5ITv_BoksecPhag_BTqPAuCAyI2_spLLRI3tENYR9FuBcwi5ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ea240da54.mp4?token=SzFeY3CO7ZZ8u1E2TUzM6De_V1zz9yV-_3RcspsulcNEuFHr5WJ8DuOVmDpijof_rhklz30C0h5sz10c5hxJq-TfuJVxd3DPMSJ_9bb87n-rXO89lQlD6VAT8r8h-VTBRM8LtMU9IqolAG00jnFmqQfhZ659W42xl4YfrUVzZGOpT7IPu4zarv2yOP1r9-V8lbnuMtYZLSqCNN8qj06RrJUuRlmkCIgh_PHZUow8A4Db4xGF_N5z0Th7UmN6dQ2BZdLla0JWEgL_aBktWb9wRIrCeGitVwpqfKCM5ITv_BoksecPhag_BTqPAuCAyI2_spLLRI3tENYR9FuBcwi5ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/128093" target="_blank">📅 02:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128092">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
قالیباف
🤝
ونس در ژنو
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/128092" target="_blank">📅 02:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128088">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sfytKp6dQYbcBvy5wtjCUgMPX01qbphiix6UZErSgYVzCJ0iY99I0-JVV7EBugC3q9a2S8QG8fitMOPBuidLiZW8PqrMXNSQbLjXl74w0Ji0JA2mliJOJG9BG3HzENRLpoEF4VuIxUMhN4JQUXXpETvrdo74ahsElPLoQuikD2rAutWT-JsSnhy4hWNOh02OrN4BdxxwYPFvKFRFfBEapjWPoaaWuHj2-usYvS8bgCYmimKUxID2aVs7D6JIx9152MJwPNCajyJBBezGojEqExgjeAxagV1MmGgBRljY-My-p_9U8VbLP8fi1VLm7bDpaUrqlHxnwswSIK87m4Slmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NMaiNLFXwwWHgnEbdPhDLA-AK7YW1xHocbDmlXaJeG3vtg_LgGchVmy6BLesCiqzSoYO3c_B_dLCbERPx_D2kynLcmKmKcjxEDI1ZJxvxtgxH4gs2OjMSmv-brBYQHSf3NqdN8SjRrpwhamdKG3Fc2JAf5JIIcsx02qkGKbo9FHsKuA7qLPoJokH8DGWnI5e8i47Vtd4NKQHOuxa_KBA12YQvjeGkLvYlnEEbpXEHXOsBexWK679KPd8aShrJt2IKxiDLprBUaJ2-eHl5Flvh-sxVsyJm-38Qp5mQdovP4PWsiKF9JvV6MgrFRwq38KHicWLWiGgC2yWwpeezGjwWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VtvQV_FcLpYV7ZpzhArAcpJOY40E3OMPkzTTVsH62KBJ40IBVizwBdsxLQ1qceyub1DLmD1p0epoSVwQUsMkO4SJqLh_36Rwe9lW6x8E9eTGVGPqW-DTmjmVZiEZdQid56kE6R-_6kkLl_w_Iy5LtawhZ2GteVS745mTuuuTfSEVzJeGwHZbQ5xC4UymHxQn0lfKNssP9As5O-XVnR1JNWX7tmKEDjraquN4gwOayG8MEXQe63ZDiRIlc-g54V_ZiHOxF1F8-U8hFf5C-bJiiTsM1rlWpabCOgvDWvrgIjz0bw3vdB8mpzSumMQICgS_SUvDanrAoVxd0CRzbJTVjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fFYbeBzxmPfI6el5qQENM-Z2QAGlzBIly8ltEdIMcnkOCcy5DVjZKScMTM6rCIb6HelWF68CjFfHmbZqOVnWM7ikaHDWsnoNtShgm_iMz4mmUdhgO9IV3PCB44fBY2FuInHTFGnhj6JIXQpq3OBljDV6BcyFQHsaGWj0_ViSxfAnGlXF1kqHZBCmHmlErcPx68OP5v8HREQbkfBMUxJN1ZD0DX35IgEv_Zpy9x3I85SVX_VS1tW7YmOp_4bVOBbJpCKdK4KKd0IJOYMEv504mZEAHt6-XiWu_q709HTXbBRxZlqnpn2HWuNis2Qj_mUs63x3z_Qkn_QL64y0VsmuFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کانال تلگرامی اسرائیلی با بیش از ۱۸۰ هزار عضو در سوگ و خشم:
🔴
«خدا ترامپ را لعنت کند.»
🔴
«اولین جنگ در تاریخ اسرائیل که ما باختیم.»
🔴
«باید واقعیت را بپذیریم: ایرانیان به آمریکا درس دادند.»
🔴
«امیدوارم تا ده سال دیگر به احمق‌های آمریکایی وابسته نباشیم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/128088" target="_blank">📅 02:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128086">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رسایی: اینترنت رو قطع کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/128086" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128085">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فوری و رسمی/هم اکنون محاصره دریایی آمریکا علیه ایران کاملا برداشته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/128085" target="_blank">📅 02:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128084">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
انگلیس، آلمان، فرانسه: آماده لغو تحریم های ایران هستیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/128084" target="_blank">📅 02:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128083">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
بیانیه دبیرخانه شورای عالی امنیت ملی درباره توافق پایان جنگ
میان ایران و آمریکا
بسم الله الرحمن الرحیم
به اطلاع ملت شریف ایران می رساند:
🔴
جمهوری اسلامی ایران در پرتو راهبری رهبر شهید خویش، تفوق خود در برابر دشمن امریکایی صهیونی را تکمیل کرده و ذیل تدابیر رهبری عالی قدر نظام (حفظه الله تعالی)، حمایت های آحاد مردم و تلاش مجاهدانه رزمندگان اسلام، به دنبال یک دوره مذاکرات دشوار و فشرده چند ماهه، و بر اساس مصوبه شورایعالی امنیت ملی، متن یادداشت تفاهم در خصوص مذاکرات پایان جنگ (مذاکرات اسلام آباد) را میان ایران و امریکا در شامگاه 24 خرداد ماه، نهایی کرد.
🔴
بر اساس توافقات انجام شده، جنگ و عملیات نظامی در تمامی جبهه ها از جمله لبنان از امشب به صورت فوری و دائمی پایان یافته و به علاوه، محاصره دریایی علیه ایران بلافاصله و به طور کامل خاتمه می‌یابد.
🔴
امضای این یادداشت تفاهم در روز جمعه 29 خرداد به طور رسمی انجام خواهد شد.
🔴
مذاکرات برای توافق نهایی، به پس از اجرای تعهدات طرف مقابل وفق یادداشت تفاهم موکول خواهد شد. جمهوری اسلامی ایران از تلاش های جمهوری اسلامی پاکستان و دولت قطر قدردانی می کند.
🔴
والسلام علیکم و رحمت الله و برکاته
دبیرخانه شورای عالی امنیت ملی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/128083" target="_blank">📅 02:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128082">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
انگلیس، آلمان، فرانسه: آماده لغو تحریم های ایران هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/128082" target="_blank">📅 02:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128081">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gQZvOWEghYtC_FQxKG-YD5ilmuZsfbbeqJ2KGfsGQdss_VSlrVGKEagLT7_8KhnqvLkMigzOFShBgQ1mC8biEnJOauRiuOg6BJ2nzQ-xkkv5qbXAimD8qRmz5Kn8OzH3tpzlVAxvxZAmQ64brMRn7GIzkXmBaWk0LLEeRSrP8HWIus8GcuJAH54H-UtRBPfyZdaS_ISJV5ubf1bwI97uQuhvV_t0PIDy8Cx5qcR5lJmFq0GBU5kSd7qHn-m66MtSfb2-CLEYc62XdE0gU39FdXCJXF7XKYPHoOH75UChhf7qcHHFTdBl5fRoIHQIhSWkk20cpjQC4kTuSP9lJh700g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏عایشه قذافی، دختر معمر قذافی در کتابش: به پدرم گفتن موشک و برنامه هسته‌ای رو بذار کنار تا درهای رفاه و آسایش به روی لیبی باز بشه.
🔴
پدرم همین کارو کرد، اما ناتو شروع به بمباران لیبی کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/128081" target="_blank">📅 02:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128080">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2af3a0e9b.mp4?token=r_r5yAb21sTCSsI4lmzpkiis7RbkUtCmn8T2KfUAxa0YjVtynh4Zbt30Q7S2UU-3y9Mvv8wt_MZYk_rRG7GL5nwQzEwwjYmc-9YQWooboGKEFwDDfkyFexjfqQSaulWaHUfdBXS7FcvJnECfaHZbz727sf_cpO6aSfyk3a5YalC-OYkSsGPQPfzroxB5m5ctXPFLyLJgGpavJNcUBvHx5ja1-zLQpNl4I_im0mRI1APGS4DoHlGme9uIxLyMWWWVx_plKvOCYHiCaQjNktb7ptU95Stg5uo3qUy4czHGE7AtGg6-BBHKevDExaCe_v5rrHirTR81uV6hiHj19wCF7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2af3a0e9b.mp4?token=r_r5yAb21sTCSsI4lmzpkiis7RbkUtCmn8T2KfUAxa0YjVtynh4Zbt30Q7S2UU-3y9Mvv8wt_MZYk_rRG7GL5nwQzEwwjYmc-9YQWooboGKEFwDDfkyFexjfqQSaulWaHUfdBXS7FcvJnECfaHZbz727sf_cpO6aSfyk3a5YalC-OYkSsGPQPfzroxB5m5ctXPFLyLJgGpavJNcUBvHx5ja1-zLQpNl4I_im0mRI1APGS4DoHlGme9uIxLyMWWWVx_plKvOCYHiCaQjNktb7ptU95Stg5uo3qUy4czHGE7AtGg6-BBHKevDExaCe_v5rrHirTR81uV6hiHj19wCF7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس:
بعد از حمله اسرائیلی‌ها به بیروت، ما شواهد زیادی دیدیم که نشان می‌داد ایرانی‌ها قصد دارند تعداد زیادی موشک به سمت اسرائیلی‌ها پرتاب کنند.
🔴
با ارتباطی که با آنها داشتیم...
آنها به ما اطمینان دادند که قرار نیست به اسرائیلی‌ها پاسخ دهند. آنها قرار است توافق‌نامه را امضا کنند و به صلح برسند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/128080" target="_blank">📅 02:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128079">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
تسنیم:
تنگه هرمز را بازگشایی می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/128079" target="_blank">📅 02:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128078">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23da8e0c62.mp4?token=IY57hjC38mDLvfjemnTyjoDIGXvG6jBztUT-9q0YhscBsMLYhDrrTl3hfkjt2Oap8Wyf2fDZpAGS4sYsqR812gUTo2bMHIp6KO0zD41ngN_Uc6O0awdO8wv8VnBuNxOsbi2P8BM_lLyD-B6mHNsCfuKyVPf_3jAWcPiC7wEaYNLBCRO9LR6YkTSvhNMCE1NC_NzNCFYQS2fgHWAqM0HZ1Mbc2XikjvdZ27DWpjZ6gLeh1JOyAHAcNUHtHkek-BltJskIq-Gvww4cNAMiTAUiXdi95mhPGjYdzNi1bBid7v3SmlavVLbAaJmD8Jspgl4CGiNHZ2yo2M1q0ywYNzIiE0P6jcjS6elbrrJ1fnRmxXyOcz_sc1UdWIHd30ezQ-C8oF9E3BOW0f6Sz2bufCQT7PlQiSG-CH9QozByNeawvhiFej5SwFJeHhGftLD5wbf6zCKYKTm2rlExSaxKCROISpZBDXz74igqr6GJmoLsVaaetamzBzd-FtVaEZySOCKtqf8AO0DdFjP4wrANi76MpEfUNh-5-uBuzlJUz7kNe1OWeLHl0FeR2_mIVrz_P8XqbDPXA_OA7Th8QWjE5AbuhN58dTii9i6LfV41XBUa5NOtFUXrQdr_SFS5RWhKu9_MFLCpkASB3udO942mZE6ExW9yYboZcr2Xky5PkiSQUYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23da8e0c62.mp4?token=IY57hjC38mDLvfjemnTyjoDIGXvG6jBztUT-9q0YhscBsMLYhDrrTl3hfkjt2Oap8Wyf2fDZpAGS4sYsqR812gUTo2bMHIp6KO0zD41ngN_Uc6O0awdO8wv8VnBuNxOsbi2P8BM_lLyD-B6mHNsCfuKyVPf_3jAWcPiC7wEaYNLBCRO9LR6YkTSvhNMCE1NC_NzNCFYQS2fgHWAqM0HZ1Mbc2XikjvdZ27DWpjZ6gLeh1JOyAHAcNUHtHkek-BltJskIq-Gvww4cNAMiTAUiXdi95mhPGjYdzNi1bBid7v3SmlavVLbAaJmD8Jspgl4CGiNHZ2yo2M1q0ywYNzIiE0P6jcjS6elbrrJ1fnRmxXyOcz_sc1UdWIHd30ezQ-C8oF9E3BOW0f6Sz2bufCQT7PlQiSG-CH9QozByNeawvhiFej5SwFJeHhGftLD5wbf6zCKYKTm2rlExSaxKCROISpZBDXz74igqr6GJmoLsVaaetamzBzd-FtVaEZySOCKtqf8AO0DdFjP4wrANi76MpEfUNh-5-uBuzlJUz7kNe1OWeLHl0FeR2_mIVrz_P8XqbDPXA_OA7Th8QWjE5AbuhN58dTii9i6LfV41XBUa5NOtFUXrQdr_SFS5RWhKu9_MFLCpkASB3udO942mZE6ExW9yYboZcr2Xky5PkiSQUYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما سرود پیروزی پخش کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/128078" target="_blank">📅 02:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128077">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا
جزییات این پیش‌نویس به شرح ذیل است:
۱- توقف دائمی و فوری جنگ در همه جبهه ها از جمله لبنان
۲- تعهد آمریکا به عدم مداخله در امور داخلی ایران و احترام به حاکمیت جمهوری اسلامی ایران.
۳- رفع کامل محاصره دریایی ظرف ۳۰ روز
۴- تعهد آمریکا به خروج نیروهایش از پیرامون ایران
۵- بازگشایی تنگه هرمز ظرف ۳۰ روز با ترتیبات ایرانی
۶- تعلیق تحریم های فروش نفت، محصولات پتروشیمی و مشتقات و دسترسی کامل ایران به منابع مالی آن.
۷- لزوم ارائه طرح های بازسازی ایران حداقل به مبلغ ۳۰۰ میلیارد دلار توسط آمریکا و متحدانش
۸- ۶۰ روز مذاکره برای رسیدن به توافق نهایی مبتنی بر موضوعات هسته ای و لغو کامل تحریم های اولیه، ثانویه، آمریکا و قطعنامه های شورای امنیت سازمان ملل و شورای حکام آژانس بین المللی انرژی اتمی
۹- تکرار تعهد ایران در پیمان ان پی تی مبنی بر عدم تولید سلاح هسته ای
۱۰- در دوره مذاکرات آمریکا متعهد شده به نیروهای خود در منطقه اضافه نمی کند و تحریم جدیدی هم وضع نخواهد کرد.
۱۱- آزادسازی ۲۴ میلیارد دلار پول های بلوکه شده ایران در دوره ۶۰ روزه مذاکرات نهایی. نیمی از این مبلغ قبل از شروع مذاکرات باید در دسترس ایران قرار گیرد.
۱۲- تشکیل سازوکار نظارتی برای اجرایی کردن توافق.
۱۳- توافق نامه نهایی توسط قطعنامه شورای امنیت سازمان ملل به تایید می رسد.
۱۴- مذاکره نهایی قبل از آزادسازی نیمی از پول های بلوکه شده ایران، تعلیق تحریم های نفتی ایران و رفع محاصره دریایی آغاز نمی شود و توافق نهایی صرفا در موضوع سرنوشت مواد غنی شده و غنی سازی، رفع تحریم ها، برنامه بازسازی اقتصاد ایران انجام می شود و بحث درباره برنامه موشکی ایران و حمایت از گروه های مقاومت به صورت قطعی از دستور کار خارج شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/128077" target="_blank">📅 02:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128076">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
جزئیاتی از یادداشت تفاهم ایران و آمریکا
🔴
در جزئیات یادداشت تفاهم ایران و آمریکا این گونه که پاکستان مدعی است بر لغو تحریم‌های ایران تاکید شده است.
🔴
طبق گفته پاکستان، آزادسازی بخشی از دارایی‌های مسدود شده ایران از ۲۸ میلیارد دلار، بین ۱۰ تا ۱۴ میلیارد دلار آزاد خواهد شد.
🔴
طبق گزارش المحور نیوز، آتش‌بس کامل در تمام مناطق و خروج اشغالگران صهیونیست از جنوب لبنان اعلام شده است.
🔴
همچنین به پرونده اورانیوم غنی سازی شده اشاره و آمده است اورانیوم و همچنین تأسیسات هسته‌ای ایران در ایران باقی خواهد ماند.
🔴
طبق این جزئیات، یک صندوق غرامت ۳۰۰ میلیارد دلاری برای ایران تأسیس خواهد شد. تحریم‌های آمریکا علیه ایران لغو خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/128076" target="_blank">📅 02:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128075">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
توافق جمهوری اسلامی با پیمان ابراهیم رو پشت دست در نظر بگیرید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/128075" target="_blank">📅 02:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128074">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
یک سوال از فروشندگان و واردکنندگان حلال خور و مسئولین با کفایت:
اجناس وارداتی که به بهانه محاصره قیمتشان تا سه برابر افزایش یافته بود به قیمت قبل باز خواهد گشت؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/128074" target="_blank">📅 02:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128073">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
طبق یادداشت تفاهم بین آمریکا و ایران، پس از توافق نهایی نیروهای آمریکایی باید از محیط پیرامونی ایران خارج شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/128073" target="_blank">📅 02:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128072">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17b2b37789.mp4?token=QRHqCfKC2eUZnzyHvhsCnM2sds5oCV9QvCmVkCPLmMqWWdibWlmwihupwn0N5dNi0w_vNigcAMAuSRWk1MqR472ozuXgwSyXW0RUw7jIlK87j4Gb5UOT9DWbZrs1qmYuOjVQ_jIIWZa5WcnrIwhYl74kn02sprljctBQKkquKzvm6JjEPW2hPogter3H2EmmgcB5znl_qsC5qB6WRA_0PaKz9SS_kmp8DNfSsA8JbbHQ8u3PGEqi0FLVpytmVtbdwx97Ad5CI3nidmnUF9W-9d7JxJI_3d10BVRqUb-ycd7u1M2DzPPwmLMRCzdyzzy_75XJVAX7JcGpip8I4_saaK6sda2Kc-a6ESgyflAM2INTKO6ABTRo9hBwxq4_0LwcyYuVkd8d5so45-KOTUToztKyaCZYlgs1jTP_RxGWlKE0puSWsuJzBT4R5OijDwoH3gN1NrE1VCP7_NPXW1pkoA01KvtqsmXoJ3hdXCy8jVqkaDg9bHjiV4kgPVtuBp2HoBhJy0Y4qOzRd4xQ410vPNS_3Zbgfd6vFfhS8qWW1KLsoL5Xq1CMboCUnQMkBtND-4LyN9iDdAOLW1KvgyQopNH-B83mEVOirt3Frl9xC7TjBzPDzbVrAh6d_dGY0stbIZku-wMyCKVa8VIgL8mmvO7qhzxnVM_A30wbuNNcyYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17b2b37789.mp4?token=QRHqCfKC2eUZnzyHvhsCnM2sds5oCV9QvCmVkCPLmMqWWdibWlmwihupwn0N5dNi0w_vNigcAMAuSRWk1MqR472ozuXgwSyXW0RUw7jIlK87j4Gb5UOT9DWbZrs1qmYuOjVQ_jIIWZa5WcnrIwhYl74kn02sprljctBQKkquKzvm6JjEPW2hPogter3H2EmmgcB5znl_qsC5qB6WRA_0PaKz9SS_kmp8DNfSsA8JbbHQ8u3PGEqi0FLVpytmVtbdwx97Ad5CI3nidmnUF9W-9d7JxJI_3d10BVRqUb-ycd7u1M2DzPPwmLMRCzdyzzy_75XJVAX7JcGpip8I4_saaK6sda2Kc-a6ESgyflAM2INTKO6ABTRo9hBwxq4_0LwcyYuVkd8d5so45-KOTUToztKyaCZYlgs1jTP_RxGWlKE0puSWsuJzBT4R5OijDwoH3gN1NrE1VCP7_NPXW1pkoA01KvtqsmXoJ3hdXCy8jVqkaDg9bHjiV4kgPVtuBp2HoBhJy0Y4qOzRd4xQ410vPNS_3Zbgfd6vFfhS8qWW1KLsoL5Xq1CMboCUnQMkBtND-4LyN9iDdAOLW1KvgyQopNH-B83mEVOirt3Frl9xC7TjBzPDzbVrAh6d_dGY0stbIZku-wMyCKVa8VIgL8mmvO7qhzxnVM_A30wbuNNcyYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس، معاون رئیس‌جمهور:
اگر ایرانیان به این توافق پایبند باشند، این موضوع خاورمیانه را برای ۵۰ سال آینده به‌طور بنیادین دگرگون خواهد کرد.
این منطقه را برای سرمایه‌گذاری جذاب‌تر خواهد کرد. این منطقه از جهان در تمام طول زندگی من و حتی پیش از آن، وضعیت بسیار نابسامانی داشته است.
آنچه رئیس‌جمهور ترامپ واقعاً ما را به انجام آن واداشته است، قطعاً حذف تهدید هسته‌ای ایران است — که این کار انجام شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/128072" target="_blank">📅 02:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128071">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266e92cbb8.mp4?token=m-9uOak1c8w7j9lCPXIvPQMfccbHZyBdkuK-cQ1fB2Uliqjl2xh13KdYFxxn1dVOMtYmRP7znQARF42q_oiQq9cKqZ_kq3VvuPZhutnXdsNnhWTWmeX_gM9a6c-rceDENka4Pr6lBBrVNBtJfIU3PtvTzN0OAGVDnrc3kwfI3aBdDTO07rByvEOEY0VOHgE35haHHPMs2TUFbFII4mlZ2jVgYonlCRK9IulM329jIveMk75rrVCLMHWDVaChNyEKZ7KP_njs5hpdft3r3HSzFgDdZPKOyQY-LZrahPP1B5-4R5AFUfGTMxzUQv0QSc1TI4B4J7D5Tc1WmGTck_1usw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266e92cbb8.mp4?token=m-9uOak1c8w7j9lCPXIvPQMfccbHZyBdkuK-cQ1fB2Uliqjl2xh13KdYFxxn1dVOMtYmRP7znQARF42q_oiQq9cKqZ_kq3VvuPZhutnXdsNnhWTWmeX_gM9a6c-rceDENka4Pr6lBBrVNBtJfIU3PtvTzN0OAGVDnrc3kwfI3aBdDTO07rByvEOEY0VOHgE35haHHPMs2TUFbFII4mlZ2jVgYonlCRK9IulM329jIveMk75rrVCLMHWDVaChNyEKZ7KP_njs5hpdft3r3HSzFgDdZPKOyQY-LZrahPP1B5-4R5AFUfGTMxzUQv0QSc1TI4B4J7D5Tc1WmGTck_1usw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جشن آتش‌بس توسط مردم لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/128071" target="_blank">📅 02:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128070">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
آزاد سازی قدس دیگه کنسله
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/128070" target="_blank">📅 02:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128069">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
طبق یک بند از یادداشت تفاهم بین ایران و آمریکا، پول های بلوک شده ایران طی ۶۰ روز باید آزاد شود
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/128069" target="_blank">📅 02:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128068">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3MpJNp3ko453q6g2J5tjwIpuF1u0YPBRUgU8o86Qs31YrfCmE0HhhuS9IGRE2BrrvLvY6CWih-B5HAFMLRfpjsN6APjwtPNrQ6IIjAia2d4Z9zqTRjIniMxpaYQH1kRinfKBEm7ajN5UrFzqfsiF-jiA1AXrigDmbQawpGKYo2RqX5XkvEyAxE-a8knjMp4XKqvEBqqr-ko6SX-rhDkeuK62xHOwbtLl7Q5qiBUh0Re1YhbiOvEr3cjAEeQBcRY8fiUlJF3AbVmD4YwuMmLXOUXT5_VAXpV4N189rlGqqMez3RueBRRfBUu7McpXR3DoKpgXedbEQ4H7dTdvgQsDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مخاطب اینترنشنال:
آقای ترامپ ما کشته ندادیم که توافق کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/128068" target="_blank">📅 02:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128067">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
شعار مرگ بر آمریکا دیگه کنسله
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/128067" target="_blank">📅 02:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128066">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuqhKe7KJDEjFadP_wQCIa4zxfPGSzT9_0VK2UpTwMe1nrLBvBJIM-mmeHcRDa7q0TZn2R2w0sIWhz8ddDi_LSsnkfu_RE3t6U1tGFKsJq9F5-ciSGz2HtwD0Ma1N3GdRulGOnMqDwu_O3U_nAD5fz9pKpferIqPDT2-89BEmy3C8HgJ8L_Qd7T9naeqOXeM4Qp5rFQVshHEPnFtBixZTRkDfQe_IRa4BX5pcYyED8bBxp-6OxYlm5qZ-Z2uzlAcPinM9Ab2joNla140uUAtLA-iyrTDCsYPhSBvw4zcMMfPE94zt6mNtNkSg_hz8Y7bRNHLotp7I3yfW48Em0gjjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
این توافق بزرگ، صلح و امنیت رو برای سراسر منطقه به ارمغان خواهد آورد. بسیاری از رؤسای‌جمهور تلاش کردن با ایران صلح کنند، اما همگی پیش از من شکست خوردن.
🔴
رهبران منطقه برای نخستین بار، رئیس‌جمهوری رو یافتن که میتونه به آنان در دستیابی به صلحی واقعی کمک کنه. با بازگشایی تنگه هرمز پس از امضای توافق در روز جمعه، به‌منظور رفع موانع مورد نظر من، نفت دوباره از هر دو سو برای منطقه و جهان جریان خواهد یافت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/128066" target="_blank">📅 02:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128065">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
طبق یک بند از یادداشت تفاهم بین ایران و آمریکا، پول های بلوک شده ایران طی ۶۰ روز باید آزاد شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/128065" target="_blank">📅 02:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128064">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1Rtx6AHYpQRuRr3K4bcXEueQWVB1uhohbFXivHbD70NO726YRuxv1nNrcClRBRXUcJzUXvWyJliCrEFCd9f4GE5LU4b6n_sTMpDGGf7cacPyFNO1oiE7Nn99IWbgrUK6Fqoj5oiVccidMSF4g5AYq8UFfhkAa-BYPBtGNadWN4mdDx3KQMC_aQAQMxLkBieYRdCdJJL1-FJKzUdxtkJYKdlmRaENTs4XUgnz8x-pWNcqdRdbiRCDY508jqryMx8tZtMbN5Al3XEIgzOTp2j1wAiiaRFu24HJmQOI-XqtPmQEtDrZqVfna_QrST6DMl6Zp9Gm4SeCgKdBmn-5Y6rXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر منتشر شده در ایتا و روبیکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/128064" target="_blank">📅 02:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128063">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ادعای معاریو:
نتانیاهو به ترامپ گفت که اسرائیل خود را ملزم به رعایت بخش مربوط به لبنان در توافق پیشنهادی آمریکا و ایران نمی‌داند.
🔴
بر اساس منابع اسرائیلی، اسرائیل قصد دارد نیروهای خود را در لبنان نگه دارد، عملیات علیه حزب‌الله را ادامه دهد و در صورت نیاز به حملات پاسخ دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/128063" target="_blank">📅 01:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128062">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vll9jdX9y6Fia7H3zNCJ31TMqkDiu4P08acI8m6QMEjyJUdddK-ScIPaDg2fEpARNJW-3NsXsNovpd391dpkIA73sd-bx5pxUUJOF7lo9lmpoJwEYDrsL7VToEr8YceSTyMCF6sa77tMDZnUrlKJyJsTP8bP-cziwVRDr8l_QvUyLrs7OeCYSnVHolpginDArCS5w4_xmx7-Jd5cUkt0MwmRbzXiREONfMOtPeDaZr8you9FCLZ371Vmp8uLy_2TRLbGfVGPzCDxey0LNmKp281tFAns7pTMsZotR5sCruAGupvjDmtIO-66mh0lmH7XIDz42dtyjkROI4OPKLYYLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا به جاهایی که غذا و نوشیدنی رایگان تو تجمعات میدادن گفتن جمع کنید برید مهمونی تعطیله
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/128062" target="_blank">📅 01:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128061">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/702066bd6d.mp4?token=YSG510wDo9TnT-l-XFiSVzEY9dxy5lGw1kRTO3_mIsNN4NpVOoexfSy_6dVVKmJxYnUGyGg9QAQAy2RFdGZg-oSk1vsIwBvwKoormNL3pcflyF4EfaIRT0I-hxtYwg5kmaISJd5x-HW30cQ7dSGq7ttTqLZWiHfQJmQDqKwDwXd9Lx0I-oC6h0nQlxZWdNPCuAObTYbi9rUO9vVN5uaSAN-m7qvZzZQ9-d7o7aUIf41zucfSDjQvAeUVlW6tNiGzaFEdfXBNmUvWWk3Ry3UMkK2i8mYCMmgPTBEKnNaUuy5Gvu-SCt7VpmDw6eJiKEKdTJSvpiSs3WGzsNlosZmUgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/702066bd6d.mp4?token=YSG510wDo9TnT-l-XFiSVzEY9dxy5lGw1kRTO3_mIsNN4NpVOoexfSy_6dVVKmJxYnUGyGg9QAQAy2RFdGZg-oSk1vsIwBvwKoormNL3pcflyF4EfaIRT0I-hxtYwg5kmaISJd5x-HW30cQ7dSGq7ttTqLZWiHfQJmQDqKwDwXd9Lx0I-oC6h0nQlxZWdNPCuAObTYbi9rUO9vVN5uaSAN-m7qvZzZQ9-d7o7aUIf41zucfSDjQvAeUVlW6tNiGzaFEdfXBNmUvWWk3Ry3UMkK2i8mYCMmgPTBEKnNaUuy5Gvu-SCt7VpmDw6eJiKEKdTJSvpiSs3WGzsNlosZmUgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون رئیس جمهور جی دی ونس:
من قطعاً قصد دارم برای امضای توافق در سوئیس آنجا باشم، اما ممکن است خود رئیس جمهور ترامپ نیز آنجا باشد. ما این موضوع را حل خواهیم کرد.
🔴
فکر می‌کنم می‌توانیم با اطمینان بگوییم که ایران هرگز سلاح هسته‌ای نخواهد داشت.
🔴
ما کارهای زیادی برای انجام دادن داریم، اما امشب یک پیروزی بزرگ به دست آوردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/128061" target="_blank">📅 01:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128060">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXgRCJDxFJtH2-Rk5NGiyAEjnexo6E8xoFRre5VwRlbMjhiHHueqLfP3ryQrw0SruH6IUPD9ZYljXEKmaacseOTRl9lVlZED594bSjsUNWYVlI69gXbCGMXDgwDWoZCEOV0AZTfEcDPVWJIaT7scsJDH50fwYkwrQj4KJ2BGN47bAVGhJr-RHhOjCuQGlnCrNRt9tcUWd5TyCxyyQDWcXFtwNvA9swFd2vGL5kzLodEXL8XMf55eQF4US_AMVkLbOe-SRw-aFc1USvdyqRYBBItzr20M6o2c8fvggRSFAzZ1WxDnHfyWdelZRJO-NkABkYzJeABR-eO1b-RhF1RHiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت تتر که بعد از خبر توافق از ۱۷۵ به ۱۶۳ رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/128060" target="_blank">📅 01:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128059">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IL3n0wVhLExcuAebnGGip0lBo2QomzSHGUhT7vGh6pMCSiIgU1flAX0qs7BqdLbOssaysH375U5Y9airR73qyNtdYlOw9VqIAONt-CkLJ9jvCFkwE7GvPClxggRo2Nk1XFJR2Z4ZqTUR_-IWgVqljHrCX_W02HKKX5DV0M2IcnaE6aWLd7-c1a4M5ytu-CbIxillUq0fuNARFAXa2voIs2JoUNiDRdAoaWwODedGL8tlwKu3npvmpQ8KFRUCBIW9EQ1sKrEQViKeBnVsMcyPDWeiRKrdcl3Xk7qj4C0UOvSIK3nKhUTSRwlNZKH8U7WY1qF4pFgI6xZCIyZY4ofeJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شب‌های ایتا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/128059" target="_blank">📅 01:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128058">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
توافقی که جمهوری اسلامی با دشمن 47 ساله خودش انجام داد، امضا سقوط خودش رو زد. بماند به یادگار
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/128058" target="_blank">📅 01:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128057">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkeXqlfyHOLmdFA2KL98L8fFVeiHNUUgxXQHhLpDOrLG5_OMNADiT3pWoNNK5t9G4Hzs1NJ9PGO1Zg7grnYTI8tu0otqoWDE8tirxgig2jABCQY8xgDxVbxpMD4Um1B21p7b5rtJViVdMxHWXLTTNoqVVAh0s6c81fV0-qhu7mDI-3mz2aGYXD-OS2u2Xi1EDnPrGWf_VQCgtK5uIbWWJ2JvXDhuYK8XoqnceQxCSQF3JIVYyCeMH6GP4FiZvLEbkGPt7pUBEZNzqPdGhHzPdq6Yf1VdKexLhOVYILBi5l_d2DgDoQ7uqCkNvYem9NuhMirb0g7VhSlDa7U1hzuPkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیافه مجری شبکه خبر هنگام اعلام توافق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/128057" target="_blank">📅 01:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128056">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/244bb5263b.mp4?token=id-4MCSrZlJ99DoTuGjhkRWw-OyNw-GfBzrDj9nwrajk6SBZTxgJzNcpDLIYh1ZJGdZsQOpq-xRlJ5FV-82ijgYAYJcSjVC_LH2UnCP7W2vM1K9OZheSxpyEt7x9sCSmte3SGyZuZR0zJnATRS9dtKgDr5uk4bf4vB91Dvm1trUxxWt9vCob2IzLetE9b-OBWqXxUjGM0RVxdmc6vFFHAl5vZk1Bv1-bogVAAS3Nph4aV3KAEZWlOG_kH1b4r4aYwFsdYSGJREwSrBsgA8cB5DTPMyK9n8E_cMnuiR1UsxGwZiOcPgTPU2rNAkOtOvLrVkjtwDjxAl5v2rbL7K6tkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/244bb5263b.mp4?token=id-4MCSrZlJ99DoTuGjhkRWw-OyNw-GfBzrDj9nwrajk6SBZTxgJzNcpDLIYh1ZJGdZsQOpq-xRlJ5FV-82ijgYAYJcSjVC_LH2UnCP7W2vM1K9OZheSxpyEt7x9sCSmte3SGyZuZR0zJnATRS9dtKgDr5uk4bf4vB91Dvm1trUxxWt9vCob2IzLetE9b-OBWqXxUjGM0RVxdmc6vFFHAl5vZk1Bv1-bogVAAS3Nph4aV3KAEZWlOG_kH1b4r4aYwFsdYSGJREwSrBsgA8cB5DTPMyK9n8E_cMnuiR1UsxGwZiOcPgTPU2rNAkOtOvLrVkjtwDjxAl5v2rbL7K6tkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مصاحبه ونس با فاکس‌نیوز پس از اعلام رسمی توافق ایران و آمریکا: حالا امیدواریم دوران جدیدی با ایرانی‌ها آغاز شود! این برای مردم آمریکا اتفاق بزرگی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/128056" target="_blank">📅 01:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128055">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb0ba1bd70.mp4?token=mrOorrTImt1aZnffk_aiZvWRg-49ULfe-QbvCtlGeY4_wpF7nuGgjaJfIv_NtzOqjRu2xRUvuWUaJ3JeSIXoyfjO6r2lnQkDMM_he-I_PQjTIENJbeWAbB8eb3CzhEpzm_-3SVvme2c3u5O1IYVhjc5tG1IrRsWIsfJs9fsYxkkr6Pae2zd3eqHIpacnQ7z7ClAwzEONIYaf0gUqfvrIFIbAiDTQHC91j2MmKf9HJL79gmyS1LCfBYziRyi1Dj1ME1RMbTeoL94WFvlEJoZFCllZ09FOhlS3NdSXSZGrzAWa5JTgen-FI1d-OfK8N3poJ9QBDMBR8bBYO-mU39z6SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb0ba1bd70.mp4?token=mrOorrTImt1aZnffk_aiZvWRg-49ULfe-QbvCtlGeY4_wpF7nuGgjaJfIv_NtzOqjRu2xRUvuWUaJ3JeSIXoyfjO6r2lnQkDMM_he-I_PQjTIENJbeWAbB8eb3CzhEpzm_-3SVvme2c3u5O1IYVhjc5tG1IrRsWIsfJs9fsYxkkr6Pae2zd3eqHIpacnQ7z7ClAwzEONIYaf0gUqfvrIFIbAiDTQHC91j2MmKf9HJL79gmyS1LCfBYziRyi1Dj1ME1RMbTeoL94WFvlEJoZFCllZ09FOhlS3NdSXSZGrzAWa5JTgen-FI1d-OfK8N3poJ9QBDMBR8bBYO-mU39z6SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آیت الله خامنه‌ای 11 روز قبل از ترور:
کسی مثل من با کسی مثل یزید بیعت نمیکنه: ملت ماهم بیعت نمیکنه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/128055" target="_blank">📅 01:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128054">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وضعیت عرزشیا هم اکنون
😂
[@AloTweet]</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/128054" target="_blank">📅 01:42 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
