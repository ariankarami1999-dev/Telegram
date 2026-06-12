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
<img src="https://cdn5.telesco.pe/file/P2ymGHLTTkdP_Bi-MM9NL9MDiT5EHM2bwmhdYCkHi1VH-DXdnrojM9IKr4N0J9mcNRxNVkqCwxO77hn2X451mj735ZS9uA_FXYZhBDm2I3InKo6Kb4jOUk9lv-dfkV5FpqH0TftS6vJc-MSn1tDSjdFbm0_-h-DAgJpVwcUbzb7YYj0zs0XoNvabOt4qcDl9lHWVxsX2MLSvMuELz1iSQcgXGtbz2iDt-8Z4wr8OGKgmXlPEyAf71JbLyZjTjm5rMWB8Y2e6MQj-Yv7kS2ORvRcQyJJ4kAdl3c0q6NiwAD56Qj_-4OE5sbtyf0hbQZ4leu9V-Kv083BSrsmO3qqRog.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 421K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 14:17:28</div>
<hr>

<div class="tg-post" id="msg-92304">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
فوووووری؛ سخنگوی وزارت خارجه: متن توافق‌نامه ایران و آمریکا تقریباً نهایی شده و منتظر تایید نهایی نهادهای تصمیم‌گیر هستیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/92304" target="_blank">📅 14:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92303">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLEO2bMxvV4yKZSrWcgKPciWavEf7f4v-p0xC3zuj99iMHI-JlO_YGSwwkH3HidABH_P-_toad9YQVyLsRoa5fi4ReTeidbFkz56uQM3M1lZNr2Z0TzNDp06jdjlRM4Pwt2NBB3QB5z9ViK1OOEeYbsEqFsJwBie6ddHajAyXmgxZNIkEelTdiRsfEV_EUYTkuF_N4ohYwss_GDvPaFHu28fvN7DcvnF_kAUwbbwU3-ZM4jxKOA-qgDUcP95pG7fR7Kuj6jJckZ5gvKNMQA5Mi7aT-N6-YwWTZhbSnLL11G8tBHJbFD0J3fuwoE1WPSzePIwvktIsbPRtBRjXb8xjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎙
🇫🇷
عثمان دمبله:
مسی حتی در سن ۳۸ سالگی هم متوقف کردنش سخته و با تمام اطمینان میگم، لیونل مسی میتونه دوباره جام جهانی رو فتح کنه
🔥
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/Futball180TV/92303" target="_blank">📅 14:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92302">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‼️
👀
🏆
رسانه‌های جهان مدعی شدند که دیشب تو مراسم افتتاحیه جام‌جهانی اصلا شکیرا نخونده و بدلش بوده که اومده رو استیج.
❌
این ویدیو هم تحلیلی هست و حسابی وایرال شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/92302" target="_blank">📅 14:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92301">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNh4fxX1oJtoXFRLtfRJLWWSeXKyVAoUqy4CL_BQmHwZfwOpJ99BZ6qfDV3jNJvsDzTMecWjksrRSjSCNuuYlKyho-3rTTJZZhKpV8HFMKFOi1lrmMBI2RLzF8jlYu6ucmOvgs4zt8B3z-71g7blcWNuGAHFaS41FWrdfrhlVZ_9lA6EA1OCgadquyLGd4kWscJRfdo-uPtXaCduR2pgx8PG97PtUR2NdqUwNxwYij8J6KIiDHWl5V5se9UJFZ1LUC4ouT-spjrjNpqruq_LO4bdWsAMnpLgYU9G7if_v9tL2MzVBeFMF_GTmA9beoBtBlOS0a3aEuQzmD5lfzl-PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🎙
🇪🇸
اشلوتلبرگ مدافع تیم‌ملی آلمان و تیم فوتبال دورتمند: رئال‌مادرید؟ بله خب یه سری موارد هست اما باید بگم توجه من تماما برای جام‌جهانی هست و سایر موارد به وقتش رخ میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92301" target="_blank">📅 13:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92300">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOJx-JFnGohka4f28XsL5ybhv4IpsU0xoLL7LNuC_XvNMY-0rezWzXzFlBvN478Gyl19_0WbQCUPnV8NUlKvItdzQsRSAl3fcM9-sNGWifmKTDJJfZ_rFM4Vlkv4DcoH7D_gtkC9aaPrm_adzRVXH6Ff5miiZiu0YICxlJE6zIo-r2eOR0pXqw-EpdAI9zZcMpO5ql82E-bBukpV_5jyIsn1a3MOs-qlArn48_sBhzB4iW-tfwqUFlus99j845BsGvwNF09N9Hvui0QcZQmlx6tOXyEVMDhJLx1cOuLrc0lMifCBw34DW95u8JVz40M4rsYtwHSrNdNfjTNxk-kEdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: منچستریونایتد درحال مذاکره فشرده با وستهام برای جذب متئوس فرناندز هست. رقم درخواست وستهام ۸۵ میلیون یورو هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/92300" target="_blank">📅 13:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92299">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQekX7UMNpnEXSfobuyDhNGk1t1MArx5s6k8NxfqB5wBz2d0lWylnV57yHS1tBmXjdBS-yeTJAS_ZUnebL5RdMW3d-bUqpyaayiPH1x0JESp7egg93Ega9cxphWkregoDmMIbYmQ0TsfGW224segaytzlnzxGWLLGDOoaUsAtnLdpoQ3evgYQVsDS0eU-D9yuEaVUNibHaDU_xhH5OXX0-RJBEJCS_iOZRS0yb6fhng7vz3I55D5RYWMP43nav0otsS_rQauPGoJZdKLS47t25pMUwisa1ZcgVSUSQKFUwv-Bd8EoEN16Y7fcrdsEJKsbsPm2OJnlXfWQyL2aA2Lnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
🇲🇽
🇿🇦
یورگن‌کلوپ راجب افتتاحیه جام‌جهانی: عن‌ترین بازی که میشد دید رو به نمایش گذاشتن‌. هر دو تیم فاجعه بودن و حیف وقتی که برا این بازی گذاشتم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/92299" target="_blank">📅 13:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92298">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULFCfAYBIVMZrbI3EGerCdS3JXC3TPHcvcBu1vQAImSIFYsgECUJiyn6-VSKF9dA-27TAy4VpK6LJxr5ZaddSRUCwDMWmIvGd2GrSHffLaQsNzHiqnkrsct9GHJojADtJGbfI650-OfHgX8bdsfS-eQxgLt44TchNYdLIOnK5OB1dK92K0dmsMztIyEiqZz5HbetyR-ttRwczfRDHP8ff0gAZ_EQm9iv4qOVCYI1QOFhKCjGwOtABYMMiWiA_6Zjq1cn-w2kK5GB1eoSgteaL9qcNmwabSmbNn8Cjycnl9AUIm2aj39OC_2lh4hQgjRSH_KK1_dvJH3EatE6XgBWjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
‌دومین جام اروپایی پاریسن ژرمن توی موزه این باشگاه قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/92298" target="_blank">📅 13:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92297">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0wfkoy8iqW3vwytoPigRzZz9JRh34Cdh4SHOulvqkt7OfOlAQPZMhgPy7YXdrjpbQDcOG6HNElfreMVUXbFrhQdBfJrvE2oW_re2Y8tRE1rButantp_6hxInLsJRYNJtjA28fadyPGYDjm1yfqVaWlGAZj4wtaRxF9H4ehN9ZMMFcp2FvjqNyrqmQE7JIZRDmbsx3nspHspY8WssPq9k_ltk81N_JeA_tRjxSc-UPEQoCnhU3WN-FI86kFEn4qPXLYZiSSjZCP96VWMFGsYfWX2Uj3ZH040qid3ZvS5R_l3EU8G2Y1TlrZtMuM8-OIQXdYksQh1qzPqhva18pJB1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آیا هنوز هم باخت در فینال قطر تو رو آزار میده؟
‏
🗣
دمبله:
نه، اما بدون شک ناامیدی بزرگی بود، با این حال، چهار سال از آن زمان گذشته، ‏خیلی چیزها در تیم ملی فرانسه تغییر کرده و فکر می‌کنم همین موضوع تا حدی درباره تیم ملی آرژانتین هم صدق میکنه. ‏البته آنچه اتفاق افتاد هنوز در ذهن ما حضور دارد، اما به ما انگیزه اضافی می‌دهد تا در این جام جهانی عملکرد بهتری ارائه دهیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/92297" target="_blank">📅 13:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92296">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf5acf7f96.mp4?token=GOfJNLNTyuj4k9XwrgEyYb8Nld4WptUaP4MoMiR36aiv1QIMKRxcV3MMN9PEemdm-fR4Ok2VKXwAwERdiIha4x8EFiylmJVoRRPpZ3_019NTL-vj9Igs3gfrIINuaekopwYYW_xTBWtjSKgWJWYqjnDAMRQbYfeyuVAKNfJZZgfN8SOKPkCy00v-p5r9CO75lRtcFUDuBLmnccg6mswuDm9U55UQrNdJ6OfB7rSFV8JHg9M8wU_F3OVTGGSeR1ka0K_rZkNnmeNkunN_VpEqRMZVQWw0eja-eZ4ijffBJfnYEk-5_lvwoW-9F8ot6aiskUKdfetW0juOH_T5P9vBwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf5acf7f96.mp4?token=GOfJNLNTyuj4k9XwrgEyYb8Nld4WptUaP4MoMiR36aiv1QIMKRxcV3MMN9PEemdm-fR4Ok2VKXwAwERdiIha4x8EFiylmJVoRRPpZ3_019NTL-vj9Igs3gfrIINuaekopwYYW_xTBWtjSKgWJWYqjnDAMRQbYfeyuVAKNfJZZgfN8SOKPkCy00v-p5r9CO75lRtcFUDuBLmnccg6mswuDm9U55UQrNdJ6OfB7rSFV8JHg9M8wU_F3OVTGGSeR1ka0K_rZkNnmeNkunN_VpEqRMZVQWw0eja-eZ4ijffBJfnYEk-5_lvwoW-9F8ot6aiskUKdfetW0juOH_T5P9vBwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🏆
🇰🇷
کره جنوبی هم‌ اولین بازیش رو برد تا هیونگ‌‌ میونگ-بو یه نفس راحت هم بکشه. این مدافع اسطوره‌ای در جام جهانی ۲۰۱۴ هم سرمربی تیم بود ولی حتی یک بازی رو هم نبرد، رنک فیفای کره رو به ۶۹ رسوند و خیلی زود اخراج شد. حالا با کلی حاشیه برگشته و فعلا تو اولین قدم چک رو ۲-۱ برد تا قدم بزرگی به سمت صعود از گروه برداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/92296" target="_blank">📅 13:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92295">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYdMWrqQDBKK0xdSKIJM_TC1bacpzRpAahdO7GWMpDkfunZBfRLT3PK30IX1KGKaHtlLvt-RDhnr8QTrpqL81UJyiLQ3tcozoJE-WeGaeroEqnpsvSybs2OvK6nYvMEn4_1ODTuOt3yUXA8gjbrQ8NkT6yaZ9hZ9JhacP1EgNWMugCfFfRXJW9VdQOGLTDlNNzLrRAPq0YAuA-_QzfebKuQ7taTb_2KWp90Lkitz2oHx4xJUfmsuj-yi0-wsDRoeOBm2EZszIlYfEsDXDCpvOqsCgNuqwqql_Y67EX-eV3XxhuhBaXhIxZZoSQh3OSziE2ValCTrWlSoWZW55ArfaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توخل اجازه داد همسر و پارتنر های بازیکن های‌ انگلیس تو هتل کنارشون باشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/92295" target="_blank">📅 13:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92294">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5962002c79.mp4?token=uGTxAV1D4h5SOpJE-tW8VchcxmCLnxArupeD-l8-3p9NXMB_sFeEj-eewespBTLkhtuSOs8eKmKVrbRqYplDeYYrqwiOZ8jxQUZcL0i1Y33POKOkw1LMTACdwo-A2DI21E8cb71GUhb5XeiLbxeeO-ZERBawUZXOKB3bZieCHyUwswVsVJajILbMz8czzQVgeO4AbyV29obCbNbPU5Z6cTi6fXcR5nGOcyv2B4l6npxKzd0sR1hcqxWQY0V_mygD_XfTVKdYdjPC0KvHoKPY65gtcNEkeKkFL5301mZ92TKDoa08oLEvHC6tGckveid9-R60Gm-nDDjyBYLSo5W_Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5962002c79.mp4?token=uGTxAV1D4h5SOpJE-tW8VchcxmCLnxArupeD-l8-3p9NXMB_sFeEj-eewespBTLkhtuSOs8eKmKVrbRqYplDeYYrqwiOZ8jxQUZcL0i1Y33POKOkw1LMTACdwo-A2DI21E8cb71GUhb5XeiLbxeeO-ZERBawUZXOKB3bZieCHyUwswVsVJajILbMz8czzQVgeO4AbyV29obCbNbPU5Z6cTi6fXcR5nGOcyv2B4l6npxKzd0sR1hcqxWQY0V_mygD_XfTVKdYdjPC0KvHoKPY65gtcNEkeKkFL5301mZ92TKDoa08oLEvHC6tGckveid9-R60Gm-nDDjyBYLSo5W_Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
خبرنگار کره‌ای در حین مصاحبه دیشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/92294" target="_blank">📅 13:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92293">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/92293" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/92293" target="_blank">📅 13:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92292">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=s8YoPYIQ1bo5SO0Xk4jvWMj1RDO0Ms3GKYhsjFc_p57lLqmbZX8fwHWX-fOKzJqafzOlUSkIaEGFZB6m-iU6fbxAmcLhgpdGEw3XCPJA_npq8Iyy3O9H2zi4zp8k7TlL5hdLCp8r-K_HxlvgCAFCWwn0D4NNudcUTKCx8equNT1cqaUKPuhuio-PAzwSARUBXMZpksM21g_jKwcFSQkOHoEZApudF1f07Qbv90LvjLEBmyB0smyDG1AcvfrC95V1G0u3Ppa1KVyxkJtU-NEC-0Pca0phgnRzMvPGnzBbBzaD75wt0AeOdzPcDGdum_kPwzfvQ-BTTcsacRYHFZi8EhWALTxB8BG8MIR_ZPgly_aiGUH1GhS5mIZgHzqwbyDqNGHXZecsRaIXdI0z31pppEUVZ5ZSN_1h4JRgzeqZwqGUZOPUgbzBUD6Gt_Ud5yHdodlX6IAjLclWSmiXD2fwr0Dtq_vb2UxkIuii3v30vn54zqYgZSVInnxNv0yfB9pi8jgjjL_cOK5BAAf5R3AYlO4wkq8kqYlK9neIiSGdUz_bL5o7yex0lqbGfaQcDOyNQI-c4rw1U9Z0EBklOkxELMaog7eWhf_N7WAe1HcgJQKbwQ9xAFXCx4hy-I-dgPTiBSH2GDWn3CAWtpIk7hW328wst5I3amBU8i71JzlfQ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=s8YoPYIQ1bo5SO0Xk4jvWMj1RDO0Ms3GKYhsjFc_p57lLqmbZX8fwHWX-fOKzJqafzOlUSkIaEGFZB6m-iU6fbxAmcLhgpdGEw3XCPJA_npq8Iyy3O9H2zi4zp8k7TlL5hdLCp8r-K_HxlvgCAFCWwn0D4NNudcUTKCx8equNT1cqaUKPuhuio-PAzwSARUBXMZpksM21g_jKwcFSQkOHoEZApudF1f07Qbv90LvjLEBmyB0smyDG1AcvfrC95V1G0u3Ppa1KVyxkJtU-NEC-0Pca0phgnRzMvPGnzBbBzaD75wt0AeOdzPcDGdum_kPwzfvQ-BTTcsacRYHFZi8EhWALTxB8BG8MIR_ZPgly_aiGUH1GhS5mIZgHzqwbyDqNGHXZecsRaIXdI0z31pppEUVZ5ZSN_1h4JRgzeqZwqGUZOPUgbzBUD6Gt_Ud5yHdodlX6IAjLclWSmiXD2fwr0Dtq_vb2UxkIuii3v30vn54zqYgZSVInnxNv0yfB9pi8jgjjL_cOK5BAAf5R3AYlO4wkq8kqYlK9neIiSGdUz_bL5o7yex0lqbGfaQcDOyNQI-c4rw1U9Z0EBklOkxELMaog7eWhf_N7WAe1HcgJQKbwQ9xAFXCx4hy-I-dgPTiBSH2GDWn3CAWtpIk7hW328wst5I3amBU8i71JzlfQ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/92292" target="_blank">📅 13:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92291">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6KsU1MMWHMKKjO7uQA3bQG2fo8pvzM4OZoohoX6ZIlxMRLt-TrRfBXTWYSbm3bgHQ0edTMDbiMF_vhnn-IYPlT19oibdA_cy7TEtRHVCtYb7DO0PssK4-XxjrAOcxSCec5FKoQQrzSYS-7r-PyuAhD8CdDXR-j5IaDQQ3E0tvaxq8TtLmW2mYYY4Q-Ue_66N4ksReB0G-UimjSPnB4MEIBkJLzZodJXe1yV-paIWIqhrJan7ICCawsMTqozce52SSShWiWOvYjQL2jCQSHaUZXwRGBb9LOVptUhoS5eMnJ_fifiYJAsiLAuecXDm7xJEsakv5Yu_VZzbPNu3TTcvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کیلیان امباپه در جام‌جهانی
:
14 بازی
12گل زده
3 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/92291" target="_blank">📅 12:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92290">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c18ef9a2.mp4?token=kPoNQU3W5W1w81Q1_usSyURDUaerwvxjA5qELHqFX6yaFu1kCVL3lItT9Brp2labUqMiQ9K0pI_wcEOamEj8-b_6MWtUt1k3jYzL3AAAkU0rli1qqGaIohtdOf8oheiLFgPH2MEYUQFXC87ie15UrVtZ8nc8cR3oJ9hypvl-LnkDq_vMlQ65qtNyCGPu7IcbdZmBN0p2k_atROw0_c1444vvKPFJrS-7h_7zRQzS42oYcnyQ0e_06aJUrmZgJtjgq5JTHV4yhR8yaQ_6oaMt7LtQcExrrDEoC95qnxf6YWBuQm83nYEuJ_jVkcpOZlCcWytfS3w1OS0t_I0LTpwtPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c18ef9a2.mp4?token=kPoNQU3W5W1w81Q1_usSyURDUaerwvxjA5qELHqFX6yaFu1kCVL3lItT9Brp2labUqMiQ9K0pI_wcEOamEj8-b_6MWtUt1k3jYzL3AAAkU0rli1qqGaIohtdOf8oheiLFgPH2MEYUQFXC87ie15UrVtZ8nc8cR3oJ9hypvl-LnkDq_vMlQ65qtNyCGPu7IcbdZmBN0p2k_atROw0_c1444vvKPFJrS-7h_7zRQzS42oYcnyQ0e_06aJUrmZgJtjgq5JTHV4yhR8yaQ_6oaMt7LtQcExrrDEoC95qnxf6YWBuQm83nYEuJ_jVkcpOZlCcWytfS3w1OS0t_I0LTpwtPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب بعد بازی افتتاحیه جام جهانی، یه ویژه برنامه تو کشور آفریقای جنوبی برگزار شد که کارشناس‌هاشون در واکنش به بازی ضعیف تیم‌ملی کشورشون سکوت کردن و چیزی نگفتن؛ خوراکِ میمه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/92290" target="_blank">📅 12:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92289">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4813f4b6ed.mp4?token=MSeBa6jTrR-0bwHbJV4HICkvT2AX5qbGvYPbeN53b0q78S0h04LSF7CCmMQq7W8SXqfHrTN4pu13n-ksoPI2RGMh9qorp5YVq6Vx4RyM6UrhbNLIGaXR4jut4K2qVxx3p9wJMjkT42NBBG4vEyJGL3OK81r2LNaIePB7uXzf4oCqCwV4XNtx6jpDvMqGIunAaN0HNNo0MGSHBD-j8TTRRhO9_FUk6qtgDEyxOHkKienSX4fAjXYjjw2BeqSeaERI4qF1ubUQFl_txveShADUuGsQGxIMSnt92JZA1XDmHlSjuguSNYIPBgh-Yosxhule3Xnm8ZBMt2mv6SKpZ3IsUm2WzPilt4-NFQvJR0ESfMuDPpVy0nRwM9L2FEgW43VKWJ-grvp3tf4Ly3R3d8a5vDWb-38s9ymvhgQvrdyVlvXXwz1aDN2_ixEJABA_RrQPTdAocktqoJttNUhdDk7slVqcnDIm1wWTcy0zJW6zNIcObKamfmzMhMtULhh1W-giQWm6W_7svo2TwM0PiL-wMowZ4BkWfoGHypxYz_S50RuHPetLjBMc7LRoF9cF0ddhTiHhqS8u9RP6rOM8jKSL-DSchijUbax3-jJ71lpLj3AVojlXllbpTAwVOQiu1uqo-VmLTWoxSqRk2DoVVA6qoaoLdwh2zn02epqIu1ekVwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4813f4b6ed.mp4?token=MSeBa6jTrR-0bwHbJV4HICkvT2AX5qbGvYPbeN53b0q78S0h04LSF7CCmMQq7W8SXqfHrTN4pu13n-ksoPI2RGMh9qorp5YVq6Vx4RyM6UrhbNLIGaXR4jut4K2qVxx3p9wJMjkT42NBBG4vEyJGL3OK81r2LNaIePB7uXzf4oCqCwV4XNtx6jpDvMqGIunAaN0HNNo0MGSHBD-j8TTRRhO9_FUk6qtgDEyxOHkKienSX4fAjXYjjw2BeqSeaERI4qF1ubUQFl_txveShADUuGsQGxIMSnt92JZA1XDmHlSjuguSNYIPBgh-Yosxhule3Xnm8ZBMt2mv6SKpZ3IsUm2WzPilt4-NFQvJR0ESfMuDPpVy0nRwM9L2FEgW43VKWJ-grvp3tf4Ly3R3d8a5vDWb-38s9ymvhgQvrdyVlvXXwz1aDN2_ixEJABA_RrQPTdAocktqoJttNUhdDk7slVqcnDIm1wWTcy0zJW6zNIcObKamfmzMhMtULhh1W-giQWm6W_7svo2TwM0PiL-wMowZ4BkWfoGHypxYz_S50RuHPetLjBMc7LRoF9cF0ddhTiHhqS8u9RP6rOM8jKSL-DSchijUbax3-jJ71lpLj3AVojlXllbpTAwVOQiu1uqo-VmLTWoxSqRk2DoVVA6qoaoLdwh2zn02epqIu1ekVwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماجرای بازداشت شیث رضایی از زبان نیکبخت واحدی بدلیل شوخی خرکی وحشتناک حین پرواز!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/92289" target="_blank">📅 12:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92288">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8m1uxyfh-NDw58Gx1GCgXfX1F7-aR5J-dtlWTH0TxqLzViJLYF5hYrtAhoXiyC9oBlooYkbZv0m1KT07wcNvZN748H2PZ0ksRSPnibZOnHbXWP8Rqz7mR1rE42furJQDoy2mIUqNA6rWM_VF_2P7bxJ0oKWFwh9JVy_7KHz1QhC_uHoxTneUnmHp1CqYWjkTwdD8O_DC7d7MtEBBrlXm5WAJ6hTVNdmUlvZ9xKP7ng0LS6gDYpr0nTYjmgddpVltr6kyjQm7M3st2m_MWlsWVvQOuIJawP-whkcVVeLQlASHjiQ1I4jRbm7xY5Xp4wbMjsKXRBQkRmVavkMejXaDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یواخیم لو:
- من طرفدار این نسخه از جام جهانی نیستم. همیشه گفته‌ام که فکر می‌کنم سیستم ۳۲ تیمی خوب بود.»
- با تمام احترامی که برای کشورهای کوچک که گاهی اوقات می‌خواهند در جام جهانی شرکت کنند قائل هستم، اما به نظر من کمی زیاده‌روی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/92288" target="_blank">📅 12:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92287">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4x-15aguZSe6iegwGrO6Pt6xRCar920R9obF8lk4-LkQh2xkrSzhlAFNLXYAEoKE1KQaBxxamLphYYKbJ7lTFt1XZhRsfj6v8bVLmsywUMgRO1undEU48Bc4aLOGw9JLlC3fFZUDusoJ-TrcQ_-ocML1vYBJFJVDbcRhkujh5XZHUmGbrsmKEvKjXeyc52Bkh7ZUQt9DWh6E9GX3X1-l23dtH2Jwcn2rWf2YWE50QW9nMWxXqrA7wPnaBSzywnhFKKuwRkEC2xRGs_g_hDHzR9XYhwhVpIhN6we_5GP-RaKMtesorDdqVGLOd1jxxNBuRoZ9k7NbjcRFou8mNjNTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
پیش‌بینی‌های استیون جرارد برای جام جهانی ۲۰۲۶:
⚽️
آقای گل جام جهانی؟ «آلوارز»
🧤
دستکش طلایی؟ «مارتینز»
🎖
بهترین بازیکن مسابقات؟ «مسی»
🏅
بهترین بازیکن جوان؟ «یامال»
⚽️
تیمی که همه را شگفت‌زده خواهد کرد؟ «اروگوئه»
🏆
قهرمان جام جهانی؟ «فرانسه»
🥇
چه کسی توپ طلایی را خواهد برد؟ «هری کین، امیدوارم»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/92287" target="_blank">📅 12:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92286">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQizVkZyPOqpIr_kZW7R0A4_AF1RWuoyyc2fQR4GrGcy0UoihE3rYDgjetp7isXJihOQDkMlS9Bz2rexxkVXN6ctMMRK-wxfrnm4jBt3TVoAowdWm3EXVmAkZ4E4zCTCAH_XLyOePA0K2h_L1HZfZBTlOQwmEJVjNBDRR3qiZErpwmBn0Q3KCtBDuzuL6TSCwznIhxq9pmQ3Z3Qc2Mi-WkwkFEr63XQUhCpF3NdILeBUkB0kXY6WhNYmlaJc-YUMvW_6fS4jqi4D9QkkLpXSQ2uXPaK7wItd8c4BfsdH4Epu8HxVm63VVlw0J9DDuLO6RK9OQqhulo15eFhShM2ZpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
#فوووووووری
پس از موفقیت مراسم افتتاحیه جام جهانی ۲۰۲۶، فیفا در حال بررسی تکرار همین ایده در تمامی مسابقات آینده جام‌جهانی است!!!
برنامه احتمالی فیفا شامل برگزاری مراسم افتتاحیه‌ای به مدت ۹۰ دقیقه با حضور تعدادی از هنرمندان و نمایش سرگرم‌کننده پیش از شروع بازی‌ها است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/92286" target="_blank">📅 12:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92285">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKPtMn3dfM-OC0PkqqE8DklgeLW4kvNuuYyEVOpFFpYlxIKVdCGITVqQ6N1SPF2aNwz8Y3ygIKypek5iwsb1twai5YRwfvr3gc2bx-njRFC7r8EdKEq_z6tRYv6V8uCsZEk8G4StlBTVYaOqMGz3Ent9sD9NqL8kXDZoLK8mOwdoYzf6BwP6WHOqc9crj_b658fIhkJP4hYJgvYXICw_SPUz3XTdqhF-41lAMgwcc2VN0BGQmop9WXEZul9o6Tk6TiC2IhKrwKES_aqIPtFnaqyNmgKb9lDnjizKzvTZEnp_2XkEMnnlkVSPhQ7LWwXdeN9bUPx_gV4PwsI3XcxS0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
عثمان دمبله [
🇫🇷
]:
‏«من از کودکی ارتباط قوی با باشگاه بارسلونا داشتم اما با توجه به آنچه در چند سال گذشته تجربه کرده‌ام، فکر می‌کنم تصمیم درستی برای ترک آن گرفته‌ام.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/92285" target="_blank">📅 12:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92284">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40bfdb027a.mp4?token=ZrF8QJvMBJg0iO6PGEIvY4VWFTqQ2VscTzoPgCZJjOEgvfDfhUp8PTDf1kZopC3KgttyCxX7OabLkm5QumzaRQhKVSQm4TbJuGk-iMIaMFzIKNXEU2sLaT3_rkYTxg5CCnbF0Rrtm7L9MjnfUcgimEk_QFDeaVFVjUC51PcG-abtruFUVEOuRIm8NSyi-n8a5eQeAtQGyQycBWKYmW4G8MGQr8FAO1SmC6PcTnZwDktzIrZy8-32WcMZtTAOqfl7nN8mqBFGAW20Mc0LgerNDKEV-5P-9s-VTmfRNqMOJVdRy9-2nhAOyH1iQ6WBoaeQWGhG0i6ZgcKa7HSKFB995w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40bfdb027a.mp4?token=ZrF8QJvMBJg0iO6PGEIvY4VWFTqQ2VscTzoPgCZJjOEgvfDfhUp8PTDf1kZopC3KgttyCxX7OabLkm5QumzaRQhKVSQm4TbJuGk-iMIaMFzIKNXEU2sLaT3_rkYTxg5CCnbF0Rrtm7L9MjnfUcgimEk_QFDeaVFVjUC51PcG-abtruFUVEOuRIm8NSyi-n8a5eQeAtQGyQycBWKYmW4G8MGQr8FAO1SmC6PcTnZwDktzIrZy8-32WcMZtTAOqfl7nN8mqBFGAW20Mc0LgerNDKEV-5P-9s-VTmfRNqMOJVdRy9-2nhAOyH1iQ6WBoaeQWGhG0i6ZgcKa7HSKFB995w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇨🇿
🇰🇷
هایلایت بازی جمهوری‌چک و کره‌جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/92284" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92283">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ae4e3b947.mp4?token=EZAiaFFozhGXvjnYsv36fHv6bNF7I8BVmj665tjs4B-yR-yj1p9w2Rv8FFEsxnD7_ZR9x2lJylDEQBsulP8YmlB_D_b7l7SzoH_dPoHyX5GsPmehq2XK7gzjBnUdvFYdx2jNN3euUcAOXwRC-9ICk53KgYOU4cPH0s_TcV0T5OE4h-v-TvdXfEDRXNdnEC0naCAQ4xozVTeUchSey3kOKzUhUn6YkyOMI7ewPTZAAVEdBY2L14BnzGxReqAwFXy3jQCi3youG1vZfI5xTbmTRF_sv4tZcwojoDczpVGiNZipc0Nivo8CoPh1xZj2ELbrwHluK4AqAJ6qYBwqLLxUxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ae4e3b947.mp4?token=EZAiaFFozhGXvjnYsv36fHv6bNF7I8BVmj665tjs4B-yR-yj1p9w2Rv8FFEsxnD7_ZR9x2lJylDEQBsulP8YmlB_D_b7l7SzoH_dPoHyX5GsPmehq2XK7gzjBnUdvFYdx2jNN3euUcAOXwRC-9ICk53KgYOU4cPH0s_TcV0T5OE4h-v-TvdXfEDRXNdnEC0naCAQ4xozVTeUchSey3kOKzUhUn6YkyOMI7ewPTZAAVEdBY2L14BnzGxReqAwFXy3jQCi3youG1vZfI5xTbmTRF_sv4tZcwojoDczpVGiNZipc0Nivo8CoPh1xZj2ELbrwHluK4AqAJ6qYBwqLLxUxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
زمین‌خوردن عجیب فرد حمل‌کننده پرچم آفریقای جنوبی در مراسم‌افتتاحیه دیشب
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/92283" target="_blank">📅 11:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92281">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhzGASRsYSNCf3hqoyTOvzBjVhYitIUH2zX-6C_LsjPOuEEsTTaqldfK9Par8AK3qDcn1x6kPc0Nl4mk4ka68rAkl8137a_M85gns77AUPWhGJ1ByCLFHEX8N0AHhHz1PuTRoQmD5TPyDlMQam_3iSMXrlDD3gmrHqA3wD5680hkYLUf9gbJ8Q-wkXuzDKiZQEFN1sKJLxHC_qfeLUnds1riVX8rlPFuyJojoMhfAUEi5ypT7uwbka70E5I7kznHquBGJ52bDa71MsGSqY-MgdsizPid4Zyj2oE0k703WuOTTYSbSnbi7OIVeEoLvAcWeHOBGe04XfSV-sE_kRlR7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇳🇴
فدراسیون‌فوتبال نروژ: بدلیل اینکه ممکنه شرایط غذایی آمریکا به بازیکنان ما سازگار نباشه، با خودمون
۳۰۰ کیلو ماهی، ۶۰۰۰ پرتقال، ۱۱۶ کیلو پنیر و همچنین سه تا از بهترین سرآشپزهای کشور
رو‌ برای تامین غذای اعضای تیم به ایالات متحده برده‌ایم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/92281" target="_blank">📅 11:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92280">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avEQwvFK850pdOcOkQpevnYGI75brF3R3vGx5kw0qvzmUFsdjzGY6qlS1HIgcsT7QmIs4RF0e8Ka7mKH2g1tPUGtCU4qK0HCks4Z8qIwlWSm9B8K9q1jxiNOzLYY44PZV_8ernEZHWLqtXIoQvl6TYxe-Q7GJl66LSTp3PRIiIqxLYu-PW4BKFCRh6Eetaa9E9EgMcP5ZqVZiLacQcoVwSaPQdm57w-VsMQOhpRhhg8VMBwJCrJdxP3IZpf1hUJyTqy4Pce9afcgqpLN2AhIRcreKmkPLvqoZe39hBq8g-yfS6yEf7hswMyhZ41IoXvm2MBrefLZI-jmOR7Fbqav1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🎙
🇪🇸
کوکوریا مدافع‌تیم‌ملی اسپانیا: اگه قهرمان جام‌جهانی بشیم، عکس دلافوئنته سرمربی تیم رو روی بدنم تتو میکنم
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/92280" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92279">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a39aa059d6.mp4?token=VI9mnR0NS8sJKTSplsWqhIw1y5sjBkHsFOz_WZBMj7lB_GxSi17qBEE0p0b_uq-fmCTcdGjblQioFhb0yXmFzYJ7-SBPrUr3mkaWhqnNHYi7ftL0-3UyW5cHnAkXvm6cZ1ZLoLNOAM2BdriX3u_GAbqnRcWKUFxyRuMee-E7Ip_6Q2BRpwAwvmObcqAMCTm5HRCEyQ-NnK86k5m5rFilmpsyTIb8tu4rTlKDez1jJ7zUQVrWzXothL1o3aLhUKkupF6pZktsT0yI7XWnDSsS2IdVPN57ABeNEskUplBK51X-ZpKLeCNSyDgCZG6J4hb-qrSwzcqPGWIOs4Z-jhsecV0sg-Q1qt71I03kLoP6maEqtrkfL0suEEoh4CpxOZ6nCN27_2jCrrmKl2VMm7LrojapB9qwtriAzpoP6se-Uv9ELlZUPY7J3x8pf-1_eJ1fSJ_3mWYgtGg4frMGAPlK_QyDNADZXwA-nTbFJblwpfb5rdLdC4Wo07VCftLZdCUQ2y5ArQHZOt2dvv9bcwMNcnTtZNIR-W-8IvXoTR6-GLJt1VKt_4eKQyM4orgtL1OIC6XIht62TZV8lFKAIze-VH50OeMZACzch_FZjlveQ6Y0-BqCIHcl1y_3fGSr490xNu5-6Hc7g5ZKORpyfGYTy_yNl260nw-abfle6OgwIvo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a39aa059d6.mp4?token=VI9mnR0NS8sJKTSplsWqhIw1y5sjBkHsFOz_WZBMj7lB_GxSi17qBEE0p0b_uq-fmCTcdGjblQioFhb0yXmFzYJ7-SBPrUr3mkaWhqnNHYi7ftL0-3UyW5cHnAkXvm6cZ1ZLoLNOAM2BdriX3u_GAbqnRcWKUFxyRuMee-E7Ip_6Q2BRpwAwvmObcqAMCTm5HRCEyQ-NnK86k5m5rFilmpsyTIb8tu4rTlKDez1jJ7zUQVrWzXothL1o3aLhUKkupF6pZktsT0yI7XWnDSsS2IdVPN57ABeNEskUplBK51X-ZpKLeCNSyDgCZG6J4hb-qrSwzcqPGWIOs4Z-jhsecV0sg-Q1qt71I03kLoP6maEqtrkfL0suEEoh4CpxOZ6nCN27_2jCrrmKl2VMm7LrojapB9qwtriAzpoP6se-Uv9ELlZUPY7J3x8pf-1_eJ1fSJ_3mWYgtGg4frMGAPlK_QyDNADZXwA-nTbFJblwpfb5rdLdC4Wo07VCftLZdCUQ2y5ArQHZOt2dvv9bcwMNcnTtZNIR-W-8IvXoTR6-GLJt1VKt_4eKQyM4orgtL1OIC6XIht62TZV8lFKAIze-VH50OeMZACzch_FZjlveQ6Y0-BqCIHcl1y_3fGSr490xNu5-6Hc7g5ZKORpyfGYTy_yNl260nw-abfle6OgwIvo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🙂
💥
نظرات فوق‌العاده هوادار معروف پرسپولیس نسبت به بازیکنان تیم‌ملی قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/92279" target="_blank">📅 11:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92278">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ki6sEEDwS4I47DkSxtHVytUBJR6h_fAPlFSeo802y6tqeINm4gHX5Ka_oFyNdAChvq35vtg-IXk_AAl0plLJwkC9Tldj-W-tdHtrDghczqtMM506cQnK--339qQ9DuVv274eYlGi4r0f_8eG8khkO_cdRqsKI1xk7LxV-2aKu_WbKAq0STXihAFa7z_FvZf1iaJ-J75ITUOzpfSC0owJgyMHFKeG3ArUvzv5wca2WO8YVm5NcSd0xVipRuP5-9yj73zo2ob958l8MmmPjOaz_STNSDDITaWEhLzy1kIW9PFMyyHH4inLDWKQxMEIyYUYiJE5sNb__mtz79AWjExnzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
از هواداران خوب و دوست داشتنی کره ببینیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/92278" target="_blank">📅 11:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92277">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbpCIzdYwBJQawhKbE9wYoG81STnGK1QhJePaFxWCckyknPOHohDiWZLuN1MiYnF7xXHMUhm-xUVQAZm6HFljd1VL2wkNzoxFXrSwRbhmCMewao22Z6TfaZAA0iqH1K0dFio5FcaZ9pGv6tkRDuOY1E6MKwAoNztenYM9VM6uv53tw7tZmlJ7ejXjHboV_ujFEoutHn0bT588hT0k-1QLOcj57NubpP6tl-CNq4DCBg1KlK5NXta0JUwzqKfCoO7KYG_CnoEQpAZwRQX5lXfcB09_s664gTV2twmdrpbfKwcbo5-7hnkqhNx733_FQ_Gy6NTxuRlPLXliNroIxArFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئال مادرید موفق شد قرارداد برناردو سیلوا رو فقط در ۳۶ ساعت نهایی کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/92277" target="_blank">📅 11:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92276">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvCb4udLqb-nsKGDBWTh_g42dYla7azJygKQ-YjSukXVGkQhHUk2NQdnwLNCXiA0RROsTyR6VeMuwDIvrWYix0RI_rz4wE4Wy_aL-U2a9wn8noyLjExXFNvbIrBdsS1_2XroNiW0ckvwbMAIe6Dwv45H9zEhr-Or8g73hqaKHgdvsyBRtJEvakohNCmiiqexK3UcegNyjfoS2L4s-4bf9Y-oa8NRMwm_DYjTFZreSyrltkjWNBp6tRNQtyfLWb_1C37NrFQE_FO85uu_QE28mmgBLRtvVc4p64vsRFGG3NyiCc-m-vJ3JagBz1SC_vPF_0iZohnLWN2kxkgPDTdJPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزبان دوست داشتنی
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/92276" target="_blank">📅 11:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92275">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">▶️
یه‌یارو بیکاری بلند شده تمام اسکناس‌های کشورای مختلف دنیا رو جمع کرده و باهاش ویدیو ساخته. هرچند احتمالا پاره شده ولی کارش دیدنیه
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/92275" target="_blank">📅 11:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92274">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
❌
🏆
🇩🇪
هوادار ۸۰ ساله کشور آلمان شب‌گذشته در حین مراسم افتتاحیه جام‌جهانی دچار سکته قلبی شد و درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/92274" target="_blank">📅 10:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92273">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMR5xeiuSEnDUIX_xr3nDIDAzaUs5VaOSVBKcSBtT87t-G4qjW6fOXpRGfhoi3UCodGRx9aW2ZSdDMs-glC-rLa4eM_5o4Q5N5iI0DvWkraVV5EeRO_o5nHPdkeyOWWs35jAkyj-Ebfr_RB7bEfxSiGCFqKIaDoWtQri6fadTCaMqLQL_cgELquOo4-FgG-GiUh6UJY4pLp5oZYqx_QH51GPSu1exQxycd3Dh6LrZpNIHet0V05d2Ps5n1bs0kminXtNSuUxZ1Ytwyu96T-XIStHqKBMpFR3o3BEgK6Wxi9YicS8ExxeAFFoCSZc_Vva5ELkpqHIkpmSwiqhYlg4KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
ژست‌نیوکاسل در مراسم‌ فتوشات جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/92273" target="_blank">📅 10:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92272">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAT2t_-azDXrPuBEd0qe-UUZVGzMTdicsv6mcQQJMfTpAVlb6k0c15GzlksTxtf54Vi2Zt4dBIIdP0vj1WCt3oRjEFlVzZNEXxOzwLhV0cPRGKB2GfkDc0c4jfwJu-CwaUe6fbZyiR1rYhiUbFb1Btt99_NSO0j_eUd6MXqoRzZfbSaVUfujOZ8hT_415Erc49DeE5ltzGdqwnCpYlJ-sezOuEx5541rkq0HLgRbr-cNKBprEHu3t2DIdADc7S0TfT7yNBtbS23b95HK0kzU2OHemvZG3F-IiN5I-bJcUV87Ge3D4RwEIB-wPGQ-5IsdT9OMhgWJEU_ulLpIkDdQDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنت ماکسیمین که یه زمانی وینگر تاپی بود و حتی میتونست تو تیمای بهتر بازی کنه با انتخاب اشتباه و رفتن به عربستان افت شدیدی کرد و حالا با اعلام رومانو به شارلوت آمریکا پیوست
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/92272" target="_blank">📅 10:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92271">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfXMENq5UL6-TNJpqY4DjkHoy2pmbYJez5GHXiGB4g2qzPG8bF2TK2O-tk3Hcck2N3oQrSB4AFEUMsSPxSIie7hRsLcecelzzdM-laF1ABwjvo-sHSNnjk3X4lpU_xREhGqnbqqBDapn6whlGvQ4KoXH8VWMAi7LhzAEWRiIdIQ7GktS0NiXo-pWF6Ob4lnUvrAfdAi6nocjNFikiCswARvJHC3HErOvfwgBIkust5K8i769NKs15aYKYlyWCXf4ddr534Jq94h3-go5W0iDx-N9gIQObFhcIdmqXoujPJOSlXekUMYBbSKdT8dQ7uql7XB6tolbejWycLevcnEBdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
دی مارزیو:
🇮🇹
یان اوبلاک گزینه جایگزین یوونتوس در صورت شکست معامله امیلیانو مارتینز است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/92271" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92270">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/663a1bd7f6.mp4?token=lOwF2-2aKm6oNIAj-FnENKIzijUaqzOmdIfNAYgYPuuAokVyJubdUHGiAHg3yb5CcYPHJI4clfKjQNKsh4NIRz-rSVXwo5MjPAVTH508O8xxvlVyAcRebLpgiO7AEtJ1DQbAfLtq-UBw2a26UNk1dC_zPFXl8Btmze49nwtIY5-MEiKIe8eh7DaJl7GWSIKxUzAUCvNN7yaB14CFIbpJ8laJj7v9G8_rDXADUGbN444qPUYcJ-13QfOMrQXfw19yLG-ryrCw3CyUnCPrj71S7LCVaT3IUqEc2Bb1-RMH1NTswJpDtB_y_oWMJBGT1TID3uTtZJIqFVF_5DJHFQFz1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/663a1bd7f6.mp4?token=lOwF2-2aKm6oNIAj-FnENKIzijUaqzOmdIfNAYgYPuuAokVyJubdUHGiAHg3yb5CcYPHJI4clfKjQNKsh4NIRz-rSVXwo5MjPAVTH508O8xxvlVyAcRebLpgiO7AEtJ1DQbAfLtq-UBw2a26UNk1dC_zPFXl8Btmze49nwtIY5-MEiKIe8eh7DaJl7GWSIKxUzAUCvNN7yaB14CFIbpJ8laJj7v9G8_rDXADUGbN444qPUYcJ-13QfOMrQXfw19yLG-ryrCw3CyUnCPrj71S7LCVaT3IUqEc2Bb1-RMH1NTswJpDtB_y_oWMJBGT1TID3uTtZJIqFVF_5DJHFQFz1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنده‌خدا عادل فردوسی‌پور پشماش از خوشگلی دیبالا دیشب ریخته بود
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/92270" target="_blank">📅 10:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92269">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba32797a6d.mp4?token=u-38Mk4cBKGKL9NNXmJy3rqLG2TQg5DGXMbKXDc_SOkNsYxZanBzGu6bDQyKfEthxriTDi5HuQqMCVZ01u-oR5WCm25kb3ocSjflutjW6_S5AnK6pVmo4-2gq4WJa83UB67lQKyjHibayXPscike50jOXpKtUcQr5zufPbj-5aD5UTFv8TWATcNtcCLCQgGMCrjaRcj9bi7uqMf0yY3KPI0f7swLKCmk6PXFxSNexlG6OJOfZrxb_OqaTbw2URlyxd5EabdJs1ImWC8rS4KFLqrJ3EE3ft-w9HQYhIbf4SYUUi2ArkmDA52Bldf7q2Xl2qfG8F9CmT_QOmvcpYOsyozFaEWiUSLu13rJ7anjbec1fnc2ogNup2AhvhK1N5MbYbASHUYz29cO_HHSot8yfeQ97NpqBIabLz3UQ-o1QWk0z_L6YcrZuFJNZdxj2g1Aln4SW_Rgeutx49EKtuYnk-iKUXGwHQSaN6zwZPL0XQynjJp88m9NdrkO0KD6s-YYB0e-m03fJ8aPllskpaPyvXERE0vqBJTGA7e4qTDORTXDkEmWOEOUz-dhVv7YiRjvaksFIauZP3UlTjH3mI9oSA0hd3w0ATVax24_aoF2Y7svYx0wQtqbeEXuRQbhH0BgYJr_HFWD-oZDR72xUz2LSIqt4Jv5rOrx8aB7xszU4KM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba32797a6d.mp4?token=u-38Mk4cBKGKL9NNXmJy3rqLG2TQg5DGXMbKXDc_SOkNsYxZanBzGu6bDQyKfEthxriTDi5HuQqMCVZ01u-oR5WCm25kb3ocSjflutjW6_S5AnK6pVmo4-2gq4WJa83UB67lQKyjHibayXPscike50jOXpKtUcQr5zufPbj-5aD5UTFv8TWATcNtcCLCQgGMCrjaRcj9bi7uqMf0yY3KPI0f7swLKCmk6PXFxSNexlG6OJOfZrxb_OqaTbw2URlyxd5EabdJs1ImWC8rS4KFLqrJ3EE3ft-w9HQYhIbf4SYUUi2ArkmDA52Bldf7q2Xl2qfG8F9CmT_QOmvcpYOsyozFaEWiUSLu13rJ7anjbec1fnc2ogNup2AhvhK1N5MbYbASHUYz29cO_HHSot8yfeQ97NpqBIabLz3UQ-o1QWk0z_L6YcrZuFJNZdxj2g1Aln4SW_Rgeutx49EKtuYnk-iKUXGwHQSaN6zwZPL0XQynjJp88m9NdrkO0KD6s-YYB0e-m03fJ8aPllskpaPyvXERE0vqBJTGA7e4qTDORTXDkEmWOEOUz-dhVv7YiRjvaksFIauZP3UlTjH3mI9oSA0hd3w0ATVax24_aoF2Y7svYx0wQtqbeEXuRQbhH0BgYJr_HFWD-oZDR72xUz2LSIqt4Jv5rOrx8aB7xszU4KM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🔥
🇧🇷
از هواداران آبادانی تیم‌ملی برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/92269" target="_blank">📅 10:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92268">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947a269dae.mp4?token=gkpKQpH7iS5yOQ_SkdfG1KxqErJ3uPi6hUaLqDTuxNPjzfAAe93K-5R5G5slgrVQeBaGW36qAU4umW8YGT2K3jfIp0LAJ35Cu_EwSVGvrkjgQgKWBQwydf-DawoG-gcZrg4lty2EXEf5D4M9bza0dXbkZmMt3qJDYEwL_VsmBTr5jc75SyL4u9rR_UKLpF2ECIWnl8cI7L3cqgN_joVOrOeer8BtF0Xt8BHdaztMh8AGb34EsFQBjdNQsEMKcU3MEIPVLnMeMkCX8oQipaAgqvSWZb6rcueqIGKnKb5VtZs9RxWMNZ8cX0iPyAcNDjIpxgboSAkGcf0yMIF5mWQd9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947a269dae.mp4?token=gkpKQpH7iS5yOQ_SkdfG1KxqErJ3uPi6hUaLqDTuxNPjzfAAe93K-5R5G5slgrVQeBaGW36qAU4umW8YGT2K3jfIp0LAJ35Cu_EwSVGvrkjgQgKWBQwydf-DawoG-gcZrg4lty2EXEf5D4M9bza0dXbkZmMt3qJDYEwL_VsmBTr5jc75SyL4u9rR_UKLpF2ECIWnl8cI7L3cqgN_joVOrOeer8BtF0Xt8BHdaztMh8AGb34EsFQBjdNQsEMKcU3MEIPVLnMeMkCX8oQipaAgqvSWZb6rcueqIGKnKb5VtZs9RxWMNZ8cX0iPyAcNDjIpxgboSAkGcf0yMIF5mWQd9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل فردوسی‌پور: مسی یا مارادونا؟
💭
پائولو دیبالا: چون مسی رو دیدم میگم مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/92268" target="_blank">📅 09:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92267">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/723b6b4949.mp4?token=ccfVXytDuhM7QWl9itbHIOq_Hy9u2l-pfARopI1THtTJ7ePdAyo6F_f7TsUl5TzYAcsffKjViofKoguVSV4p2XcP2tDnFxV1CtQUwJ89lMEMfE8UDf5TdbYFr0GXN75KxGqamEDd_YL5UGhUwoalJxWwpqDIOwPZasjOmeiOh2R4ONaH-efaHsLyQSIifUf1VLOgNXgbq0rNUV4z-se70ZMjCyrJPec3_rNcXprimuaFFS5aUbPfEmvKYEb6My7xizyc1MVqjOSqlRFO7-dQ_P1EXWta6wtX6jOmb6_grsxtkZooIaQ4Q18-4hjM3YVgBFOF9T5GZqgRXuyf0zD924WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/723b6b4949.mp4?token=ccfVXytDuhM7QWl9itbHIOq_Hy9u2l-pfARopI1THtTJ7ePdAyo6F_f7TsUl5TzYAcsffKjViofKoguVSV4p2XcP2tDnFxV1CtQUwJ89lMEMfE8UDf5TdbYFr0GXN75KxGqamEDd_YL5UGhUwoalJxWwpqDIOwPZasjOmeiOh2R4ONaH-efaHsLyQSIifUf1VLOgNXgbq0rNUV4z-se70ZMjCyrJPec3_rNcXprimuaFFS5aUbPfEmvKYEb6My7xizyc1MVqjOSqlRFO7-dQ_P1EXWta6wtX6jOmb6_grsxtkZooIaQ4Q18-4hjM3YVgBFOF9T5GZqgRXuyf0zD924WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
پیرترین تیم‌ملی تاریخ جمهوری اسلامی در مسابقات جام‌جهانی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/92267" target="_blank">📅 09:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92266">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1977ba4486.mp4?token=iFxyVjJ8LhUAdrB0_TQmMJ4NPusoDPGnPQkzUlZXXYL9o8RyRHqY7AqjlrMEFDyIK_M75qzP-MN42iv0Yau6idLs9_WxPkfZB9nbIHG1_mghIsoKbwzM6K94W3J5vOWdB38DusiHNQJVAR-9wcxAaEnwyt4ndqReDZ8fjVQpOluJhfTsVu0rpYQ0bMagDJBeGkFdiqDTA9c3tmmHssR6DrwG5k8z9uMIlPPdIKLsUXO9H-PgHzz7njam9MOlajGJJGaXH1SdChc34SYxtjhIcRBaFRb9-7Y3ZU7UilDVW-hQ7cEV_FeSJwY-Uzu2-l3-R5FnBgxHexQQW-tKj1z_UJsmgNezzEExHZy-5Oymd71c3sRXEmThG41jNa9Wjo0S-VRfTC07xBRBQCuB9Z4pjqcuIBp-vDOIHo4YE2QjzxdWzhouKyqw-MoSfmGDMUkqM7MbCX0FJH_Swn1noi3pG3ndEqxWM9wj4ywm0h7Xku5FycBsZpxlB-TGnfKkrxY6wbBcov2xGgXa11wYqXSiCh-0ZoDKLgVhnXozgNM9SO-a167sRm_PC6lEJ_AuunjnMsu6_MthNTLofWhdORHuj6qRwKs9y6Ar283uFqc875kYDkho4q9uNC8T0DgJFGl1L5XzUyq5QXC8sAbmn4JrcDyorpx54StK47LhDnxAmis" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1977ba4486.mp4?token=iFxyVjJ8LhUAdrB0_TQmMJ4NPusoDPGnPQkzUlZXXYL9o8RyRHqY7AqjlrMEFDyIK_M75qzP-MN42iv0Yau6idLs9_WxPkfZB9nbIHG1_mghIsoKbwzM6K94W3J5vOWdB38DusiHNQJVAR-9wcxAaEnwyt4ndqReDZ8fjVQpOluJhfTsVu0rpYQ0bMagDJBeGkFdiqDTA9c3tmmHssR6DrwG5k8z9uMIlPPdIKLsUXO9H-PgHzz7njam9MOlajGJJGaXH1SdChc34SYxtjhIcRBaFRb9-7Y3ZU7UilDVW-hQ7cEV_FeSJwY-Uzu2-l3-R5FnBgxHexQQW-tKj1z_UJsmgNezzEExHZy-5Oymd71c3sRXEmThG41jNa9Wjo0S-VRfTC07xBRBQCuB9Z4pjqcuIBp-vDOIHo4YE2QjzxdWzhouKyqw-MoSfmGDMUkqM7MbCX0FJH_Swn1noi3pG3ndEqxWM9wj4ywm0h7Xku5FycBsZpxlB-TGnfKkrxY6wbBcov2xGgXa11wYqXSiCh-0ZoDKLgVhnXozgNM9SO-a167sRm_PC6lEJ_AuunjnMsu6_MthNTLofWhdORHuj6qRwKs9y6Ar283uFqc875kYDkho4q9uNC8T0DgJFGl1L5XzUyq5QXC8sAbmn4JrcDyorpx54StK47LhDnxAmis" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیو‌ دیدنی از تمامی‌توپ‌های جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/92266" target="_blank">📅 09:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92265">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tngpXLABaNncR0LK8WeFR25BXk3b-JrOhnHh8vgkaLrKfSI6BK5swv6q1DSnWjF16yNtadKLFnWW01NpGbv7ch1_DYEwkYNIETQ3c8dgFUg-h53nUbnxqb8xkE2eiMEgqteXxt3Z38VB17GlcQ-0qNOVsGWemRi5De63WOexI_JUCi9gRwJqGA7HUVsq09HbYsHofZ_DBgozm53L-044L78kgnLQdtOm5E3NrJgZJ0Gvr7UPXOgUumdDvGCCNvIL8KdMJFtwVxrqcOh3ZI-Pu_XYKskEHgl-TJSRX49cgtnHtp2eXhVVYkfXgtTbTRH3dtT8Up0kGy69JXVzuJjCCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
🇨🇿
44985 نفر از نزدیک بازی کره و چک رو تماشا کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/92265" target="_blank">📅 07:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92264">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🇰🇷
کره جنوبی به 8 امین برد تاریخ خودش تو جام جهانی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/92264" target="_blank">📅 07:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92263">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPuHzCg3A7vN11pVmVSu6VGtb_MzmGcXmzR2hRZ7CpTSV630TWV9wYUKH0qn5wW1XadAHPMhKa76-5_QWifr3Rxk5IyH2D3LtwO9JNvT11vq7vUeB3LBSmDIIKPvknH52bj46QupQMRZFXwNhGEQPUjyxA6AkZjiO1zpRJGjnVIQcwcsKzxkBrDbCUOcTLaqjMVAPopSiXTfPFpl8wbqqiuAjOof6m0Tr-oWA5aThJudTyImL8hkNka9EdquqISiZsmOa-Z8a5a3J7BEi_DMbb-NbODaFKxg1LZr9AcNZTLjYWBFy4jkWWuIbjzrEogt5buEiA0QX-1_Yn77M7KOLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
عملکرد فوق‌العاده هوانگ ستاره کره در مقابل جمهوری چک:
93 بار لمس توپ
1 گل
1پاس گل
2 دریبل موفق
2نبرد هوایی موفق
کسب نمره 8.9‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/92263" target="_blank">📅 07:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92262">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WHBBBc8LQONfpCmWjWPxHnL_a6lhNPtul5Zr8zx68SJW4X3QT7jWmXi7AFD5lL9_8DuDmW1mKpzSGRbsEDDzcCfUXaDGtfopnyR35sNdfbin4hB8elf-HRTClkpLj4jaTLUcoG6nY4xpp9CNZHL-22VHjQP1Y6cc1gK2-Y3pfIqJDYVf1Ju4yd4dylAu9hnleok1i_ff4t5nic3i6RzKZBXW-68MuTSuth_rvuIxehlutS9WQNVAdxSwig9LHijoBc9lcgRishmLAvLuxu0z2msV6jOOIhZUkzuHRdnVl6UNZJ5GirfeA5vKcLtOyOb9KTO_JX0glT4fsFaV3uL5LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇰🇷
کره جنوبی به 8 امین برد تاریخ خودش تو جام جهانی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/92262" target="_blank">📅 07:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92261">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spT24A3leudT8F-OExS21-5XdoFYOYXVx-6IT4olvm7yO8WeEQg1E1BaqFi8D-70SvQYuwY52zq8UJt-zj5dteDslMdBSzpJD9qXPyhlOiA8q4AHVJ4niy-hOzY8rbOpfS3E5S4yKR4VzquDTciknFDc-oCBI6Nl4mh0m6HOsbAR1o3e_vffKLilU7QzmfRdRUmGQlgXCEY_BZUXc35jfL_TmK9LmbhQv6Pu6W7OPUNc-5tMlC3ejiVI3xPhIMPtrWdZku7GdNk9eMQJ8SB_0OZLtu0F3Wo7EP-Hp4QBHTUfCwNdmtVRnfpU-fSb_JMpiWIOj6kR-EJGvZkcJNzuAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه A پس از پایان هفته اول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/92261" target="_blank">📅 07:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92260">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDUElVT61D82-H_dhDuCnEgeKR1Six-sO2fCzH0bbkVR701toChh0YIXwsvDTM3vRrlH142fjxC7IHnP9dN0BHPbqwez1wV11AEbpWZq3V5s33H6waFX-NQYnZDfeUECqz4Nlxqg2F-GbNfooE7fx5nkAy6n-7dnJZOSc4TmZjXfdngpdumGlpFnTkfyQcyTaXkoPLU4YsW3soMzbov9kEXlmnetgbyBb5r7kic4vVHHZYgTwemzG3ghJCEaUEWX-USgp9u1yRa2bAREMwVUSyPDBckWL0s6LwuZz0N51aKz0jp6NN6hVWE3xFLqoaK15vf9lEmBhdXfb8CEk--4xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان بازی | اولین کامبک جام رقم خورد
🇰🇷
کره‌جنوبی 2 -
🇨🇿
چک 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/92260" target="_blank">📅 07:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92259">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گلر کره چه توپی رو گرفت</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/92259" target="_blank">📅 07:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92258">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">۶ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/92258" target="_blank">📅 07:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92257">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNvWElA3CpU4Av4JR_XrLwlKaCf5M-T_V5J8rGVCp5zJPAX8dzo52kTjcc2daujXwZmOAG2DlOlnp6Vk49hzOG2Wk7YGC1Yza3UhnQVuyMtpaNdodP-wxxV2vh0-LUq6sHccARu83nLKeoTJxilPqOusYCSsv47HWa1d6dCdY_6mBD3ODc2wOo1YGffVQPkxP5Ve42QC7p5EbGAE3RCkcX4O3k8nUiF5mfNy5OlrBlmfyk_isKUT8lENa7kDlics4S18D908Eb6DZN_mDcE_MyFBbm5rphZ9LrhzXyzVvFFoE0Ut4Dc4TafL5biRlXrzzWsMZ5vbvXBLyI4wVTtIrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاول ندود، اسطوره فوتبال چک تو ورزشگاه ناراحته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/92257" target="_blank">📅 07:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92256">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گل دوم کره به چک
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/92256" target="_blank">📅 07:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92255">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کره دومیم زد
🔥</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/92255" target="_blank">📅 07:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92254">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دو تا تیم رفتن واسه کولینگ بریک</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/92254" target="_blank">📅 06:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92253">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گل مساوی کره جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/92253" target="_blank">📅 06:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92252">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کره گل مساوی رو زدددد</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/92252" target="_blank">📅 06:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92251">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
گل اول چک به کره‌جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/92251" target="_blank">📅 06:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92250">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">چک گل اول بازی رو میزنه</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/92250" target="_blank">📅 06:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92249">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/92249" target="_blank">📅 06:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92248">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFXw4pU1s7_SoFFMQy-NH3Q9suXbUhwyG2DpzJ7ACTP-4dNq-Qh3KuUBmcQCHgMpizX9Yu_wa0lVYfrlLXDdBRON0TdsK7-z1cTCUlU10I5Du0v2cNmUGqsNkeBXbcQc2g6C640J3kHpSHju-MjOH4h1LZXc8_8ZcG4u6E02Qp-_wrmfmpYLV2DX6kf0-bU1DyE0r0wWGdrXn4txVFaxPx30m6_P0VgvVfkfDztMBNPM6B-6yKvBfEk6vXFTSMd3kxEKooZmifYcfg40cMaxTljDv3JLIs8efwKCWcm5TfJwTX7aafU_L_1YUHM32XosmBUA0tThHSs5XlEftrBy1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سون این توپو گل نکرد
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/92248" target="_blank">📅 06:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92247">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سون قبل بازی یه دست زده وگرنه طبیعی نیست این همه اشتباهش</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/92247" target="_blank">📅 06:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92246">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بازیکنای کره چجوری این توپو گل نکردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/92246" target="_blank">📅 06:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92245">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7U7T7L97aJ7GwiIBS4Z5fTmFwwYEecQ6p-HJGQ8db_5iZSBfuWlPYiXB45-6IMfZZWK94936ouu5osaqiPRQXLMXIW_A66-vsT5FwJyKT6AeWVlpQr4wJR6cUZEVJEd-lMc7g9pRAkWHCuf_xLSmntCU13fwteHBYhQEeAjfie-w_Vj65sa5T0bGSDBKyTiudseZyEjjZbs71j0DwSOoXgtqE1yFoDWEinlanffoYHEKYWzs1tKHsXj5WVM7ve-OePfPTusdaRma-XALOL1vc-dKAopuRjoYwbVw03t_MehcUvaRUMG5rp-Q0B69alMzFF6xlshoCapru6Dg7ur-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇿
میروسلاو کوبیک سرمربی چک تاریخ ساز شد و با 74 سال سن به مسن ترین مربی تاریخ جام جهانی تبدیل شد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/92245" target="_blank">📅 06:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92244">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نیمه دوم بازی شروع شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/92244" target="_blank">📅 06:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92243">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQxNIIZ6kBhfGCrkkjGvCMNl8XG6DFDVx5Dug44bRxWArezuydbxnQQibkBqcqdVwCx2UwiO7NwgwoBX1Ps0vKOjLiGArIi0l_FHwtRuRHyLXCeKOM0mZxy-imdevFGl73XGX8Wm45uKHVWTcRa0mc0BT-ZxzOKuWRk0FXGGXc30vPBvpGomMuP1TeiDwuEVJFlmIOizVNJI_bgMZbHZTtFFqjH0ZFc_lNNYxrrWHyoF5lwj24gX66o0kqITbV4jcnRJOznCh6t7krXYScdKbE99e5np_nXlGbhq5jvSq87J0ICgsHy3OVOmvtJQvGgVgJlEg22yAVa6aRwPrcussQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این جام جهانی بوی خون میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/92243" target="_blank">📅 06:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92242">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6lIQcGidjhzA8GsTMYdGB5zMad6Y6Yv1JI8-O7pbxAh_13pww41J3QXVpsQGPX81A7P3rwy7umVhrSibgB7pnMVFgJzs1cfu5Ip0PVHwXUYDIJV-yk-XWaDcVR2vPj_kw91U6YT51gjg0YJTCJ-l_0WRZg1vc8Nf7orjdMQhe4cnZ-7CtILtr4cp3uo4qNzjDUPWS6XcuPj6QiPkF-Xt9kIrcyOah3zCATY8RWwVFhGZid4boI0Cord1J2mxJtd7lfcPQRZKa7wWTFq57XoYq6ZIKdnJYZt7TrHQtk3gWb6pNdNJXVoR5NJN-ZBMm0H5W8vh6QzU5dYeb0WRIB1PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو کشور کره‌جنوبی همه lee یا kim هستن مگه اینکه خلافش ثابت بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/92242" target="_blank">📅 05:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92239">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ozIl3qsDuR0xUn4YIbxku9zDog8FC3LSA8m4vxLx7iPQgkc436tCGjGMGDU4uYtigH_nl426016t9nfguZO0iAZILd9nTRlFVGRHtmdk_O63Q_t_7ez4IuADbXRyISiEOZS7dL8OQ-gL1ciJkhV3eiVLkYFC_TWjo9jNz5y5kkSaUqAHNcRjVRSe4wdg2wLYkzckUqoksKrTqMtdF4MVQz5dMzpEDxY7RGvgSN2TuMO1spK8fkIUEaYiQhgIs4fuEslddUDOjuachXlwNIJHhhyJJRDUomJ8xJ5z4jQhVxpytGNd_nqe3dSo4SldAiTYlnliEZEvLGo9Q0A6SrqZiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mRXb1fM9wEhRGSrO5iEayl9zpJsofiejF8Ogz1fLK0svlCAnSRFcoqI0CvWJbbYxlc_3yvNycEB8J17pZSGYcqtTCwyR2BfX_0bViP5TKRja9LKD6Fk60H8gDLoIqTJJVkZnAP7rexbeOxtG1UFiduE6d3xrva0FVjnIoHkzzbJFTYUmWSXuj22dh06SVSDUgUJDa9_FDj9tKq2wfkBW65drPcfaGrJT3hRBV3r7wCyJ0kHicDs--zI0yP7yYiqgJ1Y0PtUQ3aaPmpstBlh4Og_YnjF56Oo0WnthMxPGunFPYDAd-nV8LHriBv0j-DEnefDC1wNCkvUve8P0jXaY6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b2i-6ge01gF74lwCE7V0c_WRETGjRnpwRqMcRwZDjNDotxQgX_skLf_amZtVcVbiku7fJMmVRgRoKIa3_WRsEzlMJQ4PAxI_jxh2fud-W6emtbmNlZenJPDubMCgaiamuv7Kz84Z19NGFhUt48thsppDbuZMpIl8b_PQBAovLxZbWNIGZlyBrQpJnaPNli2sIuZpxIFjfcKL7qlahLkY-jG-YNKWMmRPD2xhTd6dcWBAKbdBND5rEBHLpngP7OANXpyihJEIPnN9g_snewd-LIK1i8cWShr5cTvMnOGuh5s0ZUcGUvBZNEnx59HuWclOBH24yKIqeLtD1PMjJpc3PA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇽
شنیدم که خیلیاتون بعد از بازی دیشب طرفدار سفت و سخت مکزیک شدید.
😘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/92239" target="_blank">📅 05:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92238">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خود مردم چک و کره‌جنوبی این ساعت از خواب بیدار نمیشن بازی تیمشونو ببینن.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/92238" target="_blank">📅 05:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92237">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خب بازی شروع شد.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/92237" target="_blank">📅 05:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92236">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9BIuIwb0HgFHon1lbiGc_yVgMgF0GWToBPRnG1iRAkAmH_JkJX9xo3L61RI5FtgD_xxMyLqU6itJFUVhJbzK7MaST2idZvL6ErZ_Lzz6g8hZqLlw8HHI5pZdMbZuaUAC_UsiMS2K_FLN_JMsiACNhKf-R1QRpWDkXzoWlr-lwJqJIHmgL0L3bhx_H_cbaXhTI9phu7pkxnN6kvJcWQqO0QcFdaK-H3dOUSxU9sUPlx8J4niPrQDkK5BEscyTkvkHl34SVKduShC413d9vcpJc6BKe1wzQb2dmYaKYyKaoUaIpO-rQwn7_UkTFCZbZRT6a62OZS5rpSk_a_i3Jke5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابهت میپاچه از این نما
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/92236" target="_blank">📅 05:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92235">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sl1oGP-7enJ5n87dI6CyKZQy8T0N7yBDW0z_JCM4y8vrNxQvKqDTzl1FrMM4UN9EoTAp4deA3SpaVfSz-vDDUyiwj0ziTRPDXj8TSuaxdHAYDZw7l4FF1r_75Mke58CLiemOoTHo7khEF8tRdnU7u2FaGLquUKAFa8uOzzORfv9VN7AJ69_gZ0pQiKLd5sc7SW19DROwYUYoD5c8UI7mSxXil_nLMfmz6SjSHVmpY8-vW_K8OHArsLvTesDUOjPpxH2Z5tRFDgeCbD5KOrxa0x2yjpCRnI6WnUs5GnU9PVJzwvyuO3TdjMIVXzYfU3KA_uZyau11zTZsVIrkGJIxYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فورییییی
از رومانو:
⚪️
انتقال رودری به رئال مادرید در این تابستون منتفی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/92235" target="_blank">📅 05:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92233">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YEAr-Z_-cTBk1W6yYQDmuAIAXobMTBpOQdHYzlVFdjnTu_tBlBPFapOu8UE2uUa56P0qvJ7Tdbb5jIu0ELXBU5y-ycJ1ytIRotw5Sp4PF9-bHiWYYNWBKfWdPxnbuCaf5byBMT_13tfPy2DkqLDuaAJaajcs-UxHn-7NTwluq5ZHZ61BFDDNLneIAAtOgx7Iry0t3DbDk3RVSRABu12nEHliq8E28ElFBtiyKCUQHmoyVmHd5LK4DBaU68dbeY27w_akzs_ZxmsDv71zpktgtBBbFNNMhbwtbzkod3NRAtd9mxgmZnlQ5cH3pY3LYXg91fBmRhQs5BQgibNghgQsVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2wV0K1AH0TR9yjjqkCS-v_cVjqrGB7JwkOWsR539EguWj4Cb9J3v2h58QJGVtp0TveJVVf9nJSHJk4XE-Qk4HNHH11cveoZuC04XHSn5Yp0KUPxvwqopesu2DTFYeEyfXtfhnaiTTjqqKTiySbyCQ7CUoWwNPyEJvad38tbpOjrJaE2pywEFd6D04fm5VLwx2aZKLUps-7ONJ78g5NLozBWeenp17Yeg2CBSmGw3d6kZ1zCHxrJ0mZo481wrrK6EVUNjvx3Bsguii2C8v7iV-s5_T9DhRYzKQc1dbGkH49eDzBFbJiSLJkeWotTDaq0mcUN95PMaerjlTW7qqby9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مجری محبوب ما
حاجی خانوم دلیتا
😘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/92233" target="_blank">📅 04:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92232">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAz-ztEIyTL5q3kJkSAoj9WlSywsREp62Ptqny37oIpBSo835TEmvuGBbgy5GBgNL2OT0-IuAO_a6XZz_pOSXhx4ijfCsGDVPSMkmIK8tgtBGdRlY5Wyxuc6Ze8Oau299zae_CLyq6jXzP2C1cvBfkwrcIJ-eQPo-EoGUMdq6xrlvzLvXEqKfKWuwoEzG001q5h0hIbAl9fOrRZeIwJqED5JDXIP3y1pu7dox5i0_NKdzs8cC_aW2zXAlKLIhKp7ep3Vm9lNZFGx5NIOtN6r-ud06g-ZoxDjMpU97IQS2QZfRFmMAfzauoQTEAXSPOXZfqQbBcjd289eutWHDLN-fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇨🇿
🇰🇷
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|ترکیب جمهوری‌چک و کره‌جنوبی؛ ساعت 05:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/92232" target="_blank">📅 04:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92231">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lm5yHf-_ELgLbQ3C745UKYpoPMvImsG_2v_E4SfoaH67JIBKIpaeqqdkiB93yY6IFlazjc6rwfOa2ydC2EOsCS2phLvvGcbS32m8eKqV_PCzM_hdQCk00gJX3pZAYJFkfcirlSIpM60y0RZ5LBTm-Mude0AKh-U538GC_N9jLZjvelb9smbjjmkt3nOyPxUb3ou3RijCbjFuWjgUBqZnrNXcMX85h21heUJYdnI8uo-2wDHqAh6RNF7m-fDJ4vpYtZXOXMgDfpeSBMO42kL04V_harNlI6wbHstuHAzbbGCZEOOarIUxf8vDB3-pPlak3UJ5vx2PBbY8vPKLHTL0BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
🏆
🇫🇷
شات‌رسمی جام‌جهانی دیکتاتور فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/92231" target="_blank">📅 04:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92230">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/To7SrGkZNToHzfGPKF7DpydkNipTuUKwv5aoYnkLy291nq3FDcWQAlwWNGScVdUk-uoCs1-QMnf0xkmDGgE-j3jcn0RISXNLnzY-GdSkjJtwRlUBJ_HwFlkeZYAPITJEeJ14KlLsHbIQFHIcWECLUUiOtAC5RnA70G7ph8xWvgFFny8Dnku08fWohRGn1-8qH5sYgkuaiBdfIDtFmbJ0hDIPyQp_hW8bd2O5rus8-5j-yPtfxuwKJ7puiFppN8xVaBI15D-cgq4s03hQZ1ZxGLpPMzUs36a1roHVkZ2TLwmNIYn0bXhsmHTaQISvTVfXykO4dUOWasqSXpiAeyGDXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🙈
🇳🇱
وضعیت شکم عرق خوری ممفیس‌ دیپای‌ در تمرین امروز تیم‌ملی هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/92230" target="_blank">📅 03:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92229">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5j35NsEPaxxkInBmxTEEcVLcl8Wn_IKa0I8y-ZkAqYG4miQ22Eubv8rM8TWaCO3ZN6LqoesgeI2hYnTzneLPhNh8hU1YMthf8WGqIz8Hd4EkSDWpv_vEef7-wBc3X8Wk5RiGzTJepJQ93F64tfz2c2UbhgGZH-Q1HgeFEA65jNR1LQJPyH5IMhohUeLYU-mEOJaAC0Vs9JvoivpCnWIiqpd1F3UO1qxRaw1WmJjKpTM3oKtpXtHxPEpvPXeWfHmI673t3xoqNqmYUDzuI-flPz2cA7KEicuKLexlzQG3WqimVMurwYY6RN5fgEsln2bKwLPL260qfI8Frv4qmdcSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇯🇵
واتارو اندو کاپیتان تیم‌ملی ژاپن که بدلیل مصدومیت امروز از لیست سامورایی‌ها برای جام‌جهانی خط خورد، از دنیای فوتبال خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/92229" target="_blank">📅 03:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92227">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZiEJtI2LVRgXJWWiqffRzWe67aHAtTLr7ahIBqFaT8p9360uAm8HuWIXsjAaH8X8wakfnUCSQyPMqjcUrSThWkCn83g1hfbu6U6xFB9wtdAaxX3Pkp7PfBIfVnZGof1UUSJokf3_vT10O3C_yubixge9o0wsH_YtRQasixYPRmjFBw339JhUg47BaNOzCr8QAmjZL3DhrQNojFBWReXn-1al7AUd8X1ndo_sPHmrqUEKigNeYVJwo8E9EJB56W5p0Rvfcx2P4DR65viBKGf4Jk8OCDCM32exQME_s9GE9x9waiY6QqRiOIiBHME4tXuDhts8r8SX3tkqF6pF4m_uQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZzMxJNL2i7BLDj0sSNesPo4teSz1ruyvKNNaCzdWgtezKp0ppoqkyihseecOsWcnDCpbYc5xlpP7di-ESFjD598pd_QTkcnB0OiGrBcYCaehDy0iaBMTOdlMzSGlKNGu796cPsJV4IMMyD01CXkGIfKOGes4ljNtaxD4d6xsX3ZKWGNfVwL0f9x2-zBjKIT-Iwzlo06SfRQb5pAB4fapMDs_nnNXTRhpBib8eSZaF3eeWZNl37sM5dl3D0vHwmEXUQUONx8kF5Sk9-ov6-_iJf_RUsb32KEFX2nSEgzuPR_BMQR_MjdVSWspgSHl67XiXnmgIgCLuPCxTJr1XPTH_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇿
🇰🇷
استادیوم گوادالاخارا آماده میزبانی از بازی کره‌جنوبی و جمهوری چک.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/92227" target="_blank">📅 03:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92226">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/09e8c7b7d0.mp4?token=fp3nX3OMVs5TxfMC8oVMZ4dWKUrE6m0DnuoH8FxFTeTt2QUm4WC07zGgEHJK4fZHG1I_pUvzzbByECuV27tYM1urBVsXxdkqJmxKJyso2XOpYA9RCZ5XIMCBEQETcWqLJ52T4AAVrg0lpm4g55n1MwekyQO9IDLnZuMJhGjUcDjYs1SOvPoVkT36ub5tCBnbVgG7dIrNwazMPXP2b_5Puy729tiVgpOjwUeESg7WbG6FoZGuu7lpXU51n_-5i0i3WU7g1Gsj-QeNes_z9RHsXQXdms3sbYDuxNDl2ww4bObSeYD4TTKaZlbRHZtdS1YBmDs83jY1dTTSDtU3YImo1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/09e8c7b7d0.mp4?token=fp3nX3OMVs5TxfMC8oVMZ4dWKUrE6m0DnuoH8FxFTeTt2QUm4WC07zGgEHJK4fZHG1I_pUvzzbByECuV27tYM1urBVsXxdkqJmxKJyso2XOpYA9RCZ5XIMCBEQETcWqLJ52T4AAVrg0lpm4g55n1MwekyQO9IDLnZuMJhGjUcDjYs1SOvPoVkT36ub5tCBnbVgG7dIrNwazMPXP2b_5Puy729tiVgpOjwUeESg7WbG6FoZGuu7lpXU51n_-5i0i3WU7g1Gsj-QeNes_z9RHsXQXdms3sbYDuxNDl2ww4bObSeYD4TTKaZlbRHZtdS1YBmDs83jY1dTTSDtU3YImo1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
ترامپ:
امروز جنگ با ایران را پایان دادیم. و آن‌ها موافقت کرده‌اند که هرگز سلاح هسته‌ای نداشته باشند. چیزی که ما روی آن اصرار داشتیم. این کل هدف بود. این ۹۵٪ ماجرا بود و آن‌ها این کار را به قدرتمندترین شکل ممکن انجام دادند.  پس فقط می‌خواهم از همه تشکر کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/92226" target="_blank">📅 03:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92225">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59c15527fd.mp4?token=qODs0a47UyeEvI2ImjHGglvEyUgJCG4oED6aMrVxgfEVTzHkKRJwDRtK4jt4QZxna1ZClsKbOR0TQ6oI1sWtdg_-20fxyrvhxCm0nmQJ-h6WFsqnY-N2JGH4Arc8rehUoYJdwZhsKU11VwMX81qB1Lhct8LZ6gB1lmJ45z-RPmHU7H8Td1XDLzSmnKfskERzcVihF_fX0l855dXxBV_Hm6tFuljb2ug40nflxTySRRHYeRoS_gqs9zPn4Pehi-yVBnxzI8S0WHpepsCw-iK8MqRG6sbYNqkHQqKO0vaaRdyyb2wpQ7c5pNtJTjVPSvnQdnp4CeTaB6Bip7qQKYeyrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59c15527fd.mp4?token=qODs0a47UyeEvI2ImjHGglvEyUgJCG4oED6aMrVxgfEVTzHkKRJwDRtK4jt4QZxna1ZClsKbOR0TQ6oI1sWtdg_-20fxyrvhxCm0nmQJ-h6WFsqnY-N2JGH4Arc8rehUoYJdwZhsKU11VwMX81qB1Lhct8LZ6gB1lmJ45z-RPmHU7H8Td1XDLzSmnKfskERzcVihF_fX0l855dXxBV_Hm6tFuljb2ug40nflxTySRRHYeRoS_gqs9zPn4Pehi-yVBnxzI8S0WHpepsCw-iK8MqRG6sbYNqkHQqKO0vaaRdyyb2wpQ7c5pNtJTjVPSvnQdnp4CeTaB6Bip7qQKYeyrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
🏆
پشماممممم؛ این یارو که می‌بینید حدود ۱۷ ساعت قبل ینی قبل شروع جام‌جهانی از نتایج بازی‌های هفته‌اول گروهی جام‌جهانی پیش‌بینی‌ کرده و ادعا کرده همش درست از آب در میاد. نتیجه بازی اولش که مکزیک بوده درست از آب دراومده. ببینیم در ادامه چی میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/92225" target="_blank">📅 03:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92224">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEh7KFfMrPv1Z5dFE-NMbeqlTbsEH4UOM96tsSqNutdp23IqjgmyeOzJjz6E9rHbEK811o8s_KaxA1AFj21iXvh27fi0Dw9s1uaVVG8orNdRAqx18IFVWOpksTTv3i7nCHcM4IrNbpqYlqy2n6dOsQwadBl6sS0pyRjnpydDB8xLvKGjL5OWhlsZsTQjZ5h4JSUz1ljo_RzVe_bpNXuW3VnEMOY-xOW8YR1qHmLzyD-yZdZEgjbTpp1v4VyJBt7y4pn9imB0jnpMFOiI_1RQ8D9NnvqKeCf3zmGOentZlwid__iXZWl02tok9HZD6BP6mXdC38ObEFdRWCvJP1TGzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
❌
#فووووری
؛ تالیافیکو مدافع چپ تیم‌ملی آرژانتین بدلیل مصدومیت حداقل ۳ بازی اول جام‌جهانی رو‌ از دست داد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/92224" target="_blank">📅 02:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92223">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8KpbXWNkern8J2CNvnbXCI9SHFu9wUSx0qxKr--9PQZfYNK8uMJqSjD2e87NkKCdN1fTa7scq4MV3l1V4bcTdDXacb5crSR7kwYCybaftWbY2u5puOSVghK9tm9bKYbsij8WDVB-B99BnWXFQ_1zuZhot3sQesnZBxZCPFRKxTGZ3CTTg5vbQHP12hB_kK3_kiYOMKa8gpMTFY2do0HrrDHGOfT5E5homGrQVN6IfJBNMnHiKkmYDw_FYTvDlUhNm6Y3t-iEX963BB5VgjIBechOZGAcfM34lO3VijLytMXOTWYD6IidxDZdwLSas2fsT1Ad_dxB6MdW7DEtM-nRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🙂
🏆
نواک جوکوویچ: بنظرم فینال بین پرتغال و مکزیک برگزار میشه و جام برای پرتغاله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/92223" target="_blank">📅 02:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92222">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35ed8d7a65.mp4?token=JLgPdBnBe1XWa6HhRCmbyelgHR2ZctguQZN-OZOQJ9AoyUqjKl3EZ07iLas3GZzUKNPm1_5jttLM1DIH3XulFKB2jjkiYMguJ6Vqykia8coFjcJU88xM2VmNQmY5ZBDotLZWAg4852gfVZeWw75qrxy8khhdyScyGf-7C7XJ7jA8aJFyk-1t0UASgGoIRy-VYI4V36jbnZuHoO9ElyY9fEvQgjEbSRCkX6j82-DPw5nioIdC-E9SOXxZwXroaovbSVsywthJoG9Wp3M91ZUGkhs2Jtt0vZGG2nmODC11rBbf9dHOyQkrtpMb9339clRMTBkKgzRa9JyaILdbxvDheYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35ed8d7a65.mp4?token=JLgPdBnBe1XWa6HhRCmbyelgHR2ZctguQZN-OZOQJ9AoyUqjKl3EZ07iLas3GZzUKNPm1_5jttLM1DIH3XulFKB2jjkiYMguJ6Vqykia8coFjcJU88xM2VmNQmY5ZBDotLZWAg4852gfVZeWw75qrxy8khhdyScyGf-7C7XJ7jA8aJFyk-1t0UASgGoIRy-VYI4V36jbnZuHoO9ElyY9fEvQgjEbSRCkX6j82-DPw5nioIdC-E9SOXxZwXroaovbSVsywthJoG9Wp3M91ZUGkhs2Jtt0vZGG2nmODC11rBbf9dHOyQkrtpMb9339clRMTBkKgzRa9JyaILdbxvDheYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مصاحبه ابوطالب‌حسینی با طرفدار معروف پرسپولیس. عالی تعریف میکنه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/92222" target="_blank">📅 02:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92221">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/92221" target="_blank">📅 02:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92220">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HA_HhoRAG7yxvOyy1q00K7zXbh2j41GZPN8fLhtSzdY9KDMujZ23ETnZ1Di4cj2PuERRC9Jo3qak2iT3tQNgRGz2zCdS4nC399IEduunstmHQyDxZ7zFQy1v3NdUmVY64X2KnoiYOgFk8XpSaw_h67PxfjGIqkEUp_fMHEYt2wEmB8Ihgy7HH3UJszk0tp7fFu51KvxGi3IoLMWhuAZLYrPIEVSGs2PtHCeWXdi6mOd_FHoFNg11je8RZiyNVCxeEucrOzBR3p0svlNEX9xHNB-MeTEY75990seChBF-dhPLnJdvSgJDC1t0LMqspdmUZyvwT5_B-EC3dwsmuhgl9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/92220" target="_blank">📅 02:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92219">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2kzAdwpH5L0wqK5Cx4SxMdjwE92W8LkFsekvasPgufkYTN_FOPHBSK6GLR9YtpP2u3j1bDKcBOlwffvrYN_Tc7bWNqzv75dVOCcWvARb-Oep6RmJtvpSbRvKgmtOF747MeqyT9HE7m3a_9ZZneywMlZjl3HOMj1j2I7pL8FoGOipu39yiv_m52dW2XKuZws8nJOA-s_nx2d0o3mYyuN8mJdp_dDH4ShOl_-DmNshxFjaqk-cYM0ahhz8WtbE8QO-4JPjdtWEcb6z7dBTv_ezuY7MYaAJzurl6H4FwIXnWoGuaj_QCEAqUS1mxE9i7tFSp4OVQQFMRDk8Cp04JZYcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اوچوا دروازبان مکزیک:
امیدوارم در فینال با اسپانیا روبرو شویم
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/92219" target="_blank">📅 01:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92218">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
فوووریی فارس :
دقایقی قبل ارتش ایران اجازه عبور یک نفتکش متخلف که بدون هماهنگی وارد محدوده تنگه هرمز شده بود رو نداد و همزمان سه انفجار هم در سیریک رخ داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/92218" target="_blank">📅 01:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92217">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5FSPjo_RgBeuC3eaR5Fde7DYih2snp_HmmJSRwXY_Pi32jq81wTwhdAgoCLYDkHUSEqUDNqagedCkwx76AmIF2wI_FwRcmMxQq9g9gl4g9l6wbsngXahF13yp-QKIkEQcJpv8HTcUsJdQcEV8gEfwQQGMTySvpVLKyGGEejw5unLYbkP9ZJ64jxhUQLYGs0XqBrNkn-JGOx0oG4LE8YZj3pQT6NooDumN3Q-d-4cd6zn22Lza8R5rs2PNSAYyHCu89OJAoRIvXa4ZyWO_GEPe0icDHNMonvsbGAAaowsUm-iJB0gkVDgtnEsQUl8raRnHXXz0kVjj7xux-9njmwcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سه انتقال برای رئال مادرید در این تابستان تا این لحظه به همراه انتصاب ژوزه مورینیو:
✅
دنزل دومفریز
✅
ابراهیما کوناته
✅
برناردو سیلوا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/92217" target="_blank">📅 01:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92215">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJ52jvxU2E2Y7MWiNqjvsCGZvSa9JSzpjJuGN7WchZgGGZ4NcJSBOnwno27B_SSj9rB_JrmtVGKoXlSlW7WM2WCAsjhSQ1XLgh8CmFU31C4hXUIsJQJrQSCtJgj7AOefQriG7RcaS0nBntHn4RvlZgiLvoTeMipVt46X6Wp7bSNzftDfcs7p6Q3g6oxPeZ_wupHB6izIA-DC9WBWJ0chJh6ui_pqJaBLHWz6DoRWCdtUnD-XYxXbjGAPjaJA-oDjSJk7mDtkvfB57Oig44W_duwvwWh3_AnKSneFwTDkxveabanK6raHsHmC9rE_ZYxKgpg83JuH56ohodltMPnBnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/diHxLmrm17S4hkQr9x5-kYWYFE6YyAMpKCA0aCy4HsCLPWjMQREAIAetg8WvUD5pWHLvM19iJ8D6x-4UcYwIiCiZEqv2nkcPGz9X1BDhUlOrFzSGlHSaJzUNS231ZckfdKAgyEiBrX_A8B6rM3cmBBIMU12MQ3VcTV1uNg8SF1rarzU5uNFJu9Zmu2zyz_kmfIzHyu1CZWqjdBxgT0hgEQY4081-WshWpzLGFVL-i26HP4FZxOa9SZKWJabwR1oNwpxvyzHnn7pcUZKvWnS4pT9vpKg5XFxvHKUjkEu32KVUvBN-1d1-hr2CktgIiIcuASoTQ2KyUqDDtfuMvuMAsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
آبولای پرتغال:
🔻
در محل تمرینات پرتغال در میامی سه تمساح دیده شده. زمین تمرین پرتغال در کنار یک دریاچه قرار دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/92215" target="_blank">📅 01:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92211">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d5BaCYl0RNNGwTDqkn3p1pLCWTQ094V4fnkTICwy7cXhZDmtyo3nhbyDO34r-nQOpDgiFtXi8U0LprQEKIhkiGMgtzdOU1lXieSMm24Ygmu4c7I-SjzSkU-hRBq3w1uZMzeSfkqjja1OMyfJ0hdiAe_ng26zJ4e1I7gD4FrHzIo65aQeEGVQJUFAYHRBtDJjLTR8I8t_2A8oi8vAyNX8glP5q2OkT7wehRsHKwjwAgOmr2IvOJ8aaeAyy3soMctIEx5ju96j3xWyJ9wJZU8St3GrBOaBls0L_1lZK1vpBS02vOMKkXxMLfy1xy9ez9WJeRdKGCTA2YrnNu567ki0oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g_TlxZgnkOe3l2zg3HotanPbtiulExxSz1xhG98WuSHO6qgrlYdmVxHtop6ZWS4NEWqGuFcBaaHon_1TEBOm8OFEfP82tXx621WzgruZ8u0hmwWLWRtat83ZFg3CNRpeqfUCMlX07V2wEsS5oaoERvqSNng8iRgUWpucfR5B-lVGO81qNDL2y19ROPsExpxnZZ-4pflrolt__V1RchoOGYX1egyRqxFhEwcHj3iWW9axaIZlgBzNL00f-yptKTDYzD92ULW3ZvR8o_pH2UyDHUN5z_6mJZv66pxWARAgLfo3geYx1wBjzVSnaUsNbguUvb1aqS_G_4GT7T32knTt0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S1YsfGYO_LpLnmS-OCw4oznS-wZ_QC_7W6SvP1RQTaSKzNTdBdT_B-7BC7OzDdvigkKFCc5_3N_7flV2IYUqv1S6zlt4YykXZRUpBJLGbt4RvCv8KZyOtyt3xl7i2J1H2Fs1nF9DgeUXiPtRki35Wl6JNmtSCuq9-0eesiIOJsfn1tw4NOisYb7mpoStSkpmk51T7lnycmcgIn7R4b8EyPVTmMcqUuXEE6raMzReOoDqG-yyHycrFFN3PyHJfcJMo3PWuTJ9d_jwKgYGc0pOAI2tXp3-VtPOHHu7J8SjoSO2mVxMacVKl_Tax9d6bpsi08HQdQG10AwXE6xvBuJaRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q-_LIy_g1Bxq054BjYrpu7cZgGP7mAtX0i5-wxBrLxJhppBoNSKphm8_b7cZ3R9tLbyOsEBq26NGSMjWPOIoMyQfFBTTphUPhLDuBW1k9m3ar2OpU6Whc5MjN3dT6eNYgzYiBoZqvMZ8KyzbW3NBPRI2iZHjShs8V51jEugF4bgWhru7TjxNjU0-g5hUOC3hBTjjxhWifif80ycxvkOsxHJXymvoGOt7H-5Koqqa09VIrFxKXkEDBsyNr60FEW8RbFY7USGvmkaLwm8guXtlwjKfD6ijdJo4ZRTL5v8Lr277nJoMzKeM2r5RXKGJUG8gWxSsPJkLL7rOfFcCF6FkhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تیم ملی فقط مکزیک
😘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/92211" target="_blank">📅 01:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92210">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgivcoRuMgeD9DEcFQF0ZnORMhUuoYG5m8oc3JStB6JV_tqeMGvpnbSwZTemesuvTC_yH5jmF_YOnal19odB-aez145gzJ5qdtWg8ntizLjOhQ3IrOt_ltyDqNiKwf3UEz2-kZ_N261bteOVIve3T8gmKkMqWWy03RM7uKciAwXc5-II7CI6tEgl0nocJj7bPCEP4_lT_jM3BZKrb6wWDrjrpQLwh6_r-TYU0OStKII-joVphyaQIPe52FDHsD0Y2atcLrnmB8kckvdDMICi5zax8ZVZcXnTogOU7jbV0HS_j5gvyv2OJgEuPZ8RrhIYQRro--_NlNaO0NgnfobEOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فووورییی رومانو: برناردو سیلوا به رئال مادرید به عنوان بازیکن آزاد، 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/92210" target="_blank">📅 01:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92209">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhcUlOzyhoCxPCfbCvteTsNpsYfOp_nlzhZqGqZZSpnZ0YsAOyvnvuXBPgIHXnTmGwh_xL5Ji9T-_OytLZC-oWWaGS3VonI6UEDfI6j-vJ6fQLAuwVb-71j_72DrjHFkVPRofduzocgmWUjtQnNh-OIIIOHTFEtMy-WvRORoZeD98PZa2GHyAbEjgx0UwMZH4QbBgavdTTIJTBM1dHe-vkJKAd38_r0KM8CnaZojKcix9AZeU_LILKty4RnIpm9QUt_xtwUY2zimn22zdcmRui-jVogSHqgFKS95-nSZ6LzEFpEe28_qNvmS_LcZ_t-0GUUNPN9qVe5BRNfOTM7d6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه:
اگر قرار باشد بدون اینکه هیچ گلی بزنم قهرمان جهان شویم؟ من فوراً و بدون تردید موافقت میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/92209" target="_blank">📅 01:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92208">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
فووورییی رومانو: برناردو سیلوا به رئال مادرید به عنوان بازیکن آزاد، 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/92208" target="_blank">📅 01:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92207">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1TqtR1_9_FPNb0s5l11vMRQQI9wxFYiXRq3rtwJhbp5KRQdUyswpbrESNlQx5yJ3Vvmr2b2FEZJhMc6KFMSBDY6OpUjnLKi5b6P8bbUGuifWUAVxh1PwyNziUFVMMRCoVo3aFeABFx6tBJNzaCGgwnuzzpkCdylvswyFG6eYpThd969NGkuXboOj-iRc2uJNcWaKj3IdlfgismjgMhcbaXYeGVkMpOSrWxKAc6xiSRYVipFldpD6PkHYPXo2Clec_eixUR9r5ZpROmjq9ohqmjkLm15MQwPyOPCG716Qx-CYb9naXNeiCwdyO8NLf76gHYMwBQxxMKRRiik0vlmDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📔
رومانو:
🏆
برناردو سیلوا به رئال؛ 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊 بزودی!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/92207" target="_blank">📅 01:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92206">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
هم اکنون؛ شنیده شدن صدای امضای توافق در سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/92206" target="_blank">📅 01:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92205">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLeIsVFg1IDVJF7NYZT-6eBYDkJIOwa6elgXd0eHnUCNvaAIAoCEKxCmVQvRc4Ny99P6WnMdA0k7b2nf0r3ojFSg5_zMZ88mTwumotpdp1bxdteKe7Snvcc0FyjjQdqzcg3LTAiFSHZPYEHirKc6Ka_xIMp_7SfnZgGT8BF8DdpNWB8K3FnOcYMWZBZGBoLrT43UuWxN3xiugMberVD9ihydLFeGLKovh2Qukt5Dcq6IKlHO2-HdAA4mKld9_s2GE6x0vGDNkjy5AEdPvrzJyPb9lKp9dE7A6jJ-HQZUZzWx8j1wPTofqzUhMgSH-c2pRcwZK2KS-VGAIwckmjb0rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🏆
بهترین بازیکن دیدار افتتاحیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/92205" target="_blank">📅 01:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92204">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dbae198e1.mp4?token=RXCTIcJ7WGGTkitP2vrL5VQwC_HbJWhqjXUtFAwYvujQjNdmP9CmGol4CtK6UzoKoN1AqjJ_G9VG-kTPwlM4cj-QDFveoZo6LUw_dBXryRdx0IpoJ8WgPwAAGflW9IW0DwgY4faKAJM7leYfQHc-T8hPZGtEmSndTg9DGJuZSYHrEIPLgrsebMyXcjCMxIrHJBm_1_8ynTkIBcQKhrN8z9a74o0qeVTORf3PgW_FbDwWidIJmaQtkzV0ypk7SbN4aFbjiDknTzjl05GBqe3dG_sOvs-BCu3KAprrZcb2s29-UymgFexfmc4K491Vfr2vwkyt0X6ovYpUjYw_fufZag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dbae198e1.mp4?token=RXCTIcJ7WGGTkitP2vrL5VQwC_HbJWhqjXUtFAwYvujQjNdmP9CmGol4CtK6UzoKoN1AqjJ_G9VG-kTPwlM4cj-QDFveoZo6LUw_dBXryRdx0IpoJ8WgPwAAGflW9IW0DwgY4faKAJM7leYfQHc-T8hPZGtEmSndTg9DGJuZSYHrEIPLgrsebMyXcjCMxIrHJBm_1_8ynTkIBcQKhrN8z9a74o0qeVTORf3PgW_FbDwWidIJmaQtkzV0ypk7SbN4aFbjiDknTzjl05GBqe3dG_sOvs-BCu3KAprrZcb2s29-UymgFexfmc4K491Vfr2vwkyt0X6ovYpUjYw_fufZag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بارساییا وقتی میفهمن تو یه بازی داور ۳ تا کارت قرمز داده ولی اون بازیکنا اسمشون آرائوخو کوبارسی گارسیا نبود
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/92204" target="_blank">📅 01:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92203">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
هم اکنون؛
شنیده شدن صدای امضای توافق در سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/92203" target="_blank">📅 01:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92201">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efd5005212.mp4?token=muNI-LU-f49i9rgne5iqDugxzFwB5BxGK-BbGAq2KEYIOZr82HXUjBFRnWF27ybzc-F_Y3KzgCNX8aoMIwFn5AWgn7isuiXEUDg2ucBdk93PhXh2--Oi6AF8f2J-xiMlLchbA04GM780dmwJAJmmyPpaQk6NmSs8ZPdUzZSTuGPrJuzm43gf6UJoSKmWGzTiCvuUOVfNsFjaHPDTMvhMerPSniXbyBA_wj2KUraAHpkXQyxDkNfSCagK-j_bNGFBsyANQAtuoIXjU-NmXar0TnSIbd3FmpxF_aJBr1FgkfMHE8ozSsE6erqyISOa-UeEy1o9q3_mFr3T4Av3BEq9rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efd5005212.mp4?token=muNI-LU-f49i9rgne5iqDugxzFwB5BxGK-BbGAq2KEYIOZr82HXUjBFRnWF27ybzc-F_Y3KzgCNX8aoMIwFn5AWgn7isuiXEUDg2ucBdk93PhXh2--Oi6AF8f2J-xiMlLchbA04GM780dmwJAJmmyPpaQk6NmSs8ZPdUzZSTuGPrJuzm43gf6UJoSKmWGzTiCvuUOVfNsFjaHPDTMvhMerPSniXbyBA_wj2KUraAHpkXQyxDkNfSCagK-j_bNGFBsyANQAtuoIXjU-NmXar0TnSIbd3FmpxF_aJBr1FgkfMHE8ozSsE6erqyISOa-UeEy1o9q3_mFr3T4Av3BEq9rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇦🇷
لحظه دعوت سنسی به تیم ملی آرژانتین درحالی که توی تعطیلات بود. سنسی بعد از مصدومیت بلاردی به تیم ملی دعوت شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/92201" target="_blank">📅 00:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92200">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7T_oTcxl0Kd0pQJofXrC8xQkqtxUSx7tN2xcDdaSLBUG0FPcp2Ql2ht_1Qdz5ehRWlY_Seiq3ECh064Ps9OQV9QPxPxOOMa8r5UXLPyDC5_mxraqTye9xJzb843PW7yZHtE6sxt54-I2E42g1ZB47wrHKmH8z3nGGzWvtyzSewBgpEVlrORnoFqIq4DeqDSB3-VQCQAKcH-i-B02nEV_cWNbAOFVdJ39vYGAe9pQHgqoTMlFV3bb7hKwtQkcq4tKXAlmV02XvNLpAxcm4ptUnLv-MKWy-fm9iyuZrl0_xVUxQvonkRkXJwUvhgYXUmc-sQoo2awpaJY8v8z03yEdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع قدرتمند مستر شت‌هول در دیدار افتتاحیه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/92200" target="_blank">📅 00:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92199">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTnt98y-UTDi3G3PeVSVWPHEACfMVq2g58sqyptjnitTBcUwKHv_3_SjlHmq6KQuok-JgoOFQQ8WVbMSn8hl5deFf2c29vztnjSB3hzty_oo3y9YyHOiZd0ogcLId3qeyV6DHRKaHEjibdV6FRihhaQbTnF7WF-K3E7iC9ReL8fWA-kGGyO2Xa2zcGS5ZvPDGYap07II3jha-yASHRz6KQFu-u9gX3yiitl9VwqbghZwneAXgMO5nNmU9NVKXILLgtCl-3qo8hYPvOotSqFwSvp7Asvy4BbH8Z51YoVs1EoEunL0hI8S7U1XAGuYOWonQLH5WoXfLoiW1YRN8QkVzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری:
رودرا خبرنگار پرتغالی: برناردو سیلوا تست‌های پزشکی رئال مادرید رو با موفقیت پشت سر گذاشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/92199" target="_blank">📅 00:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92198">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOtVkG5vnUTW4KLess1StgSmNGqJtbJpij9DSJ2MQMuT3TGQApFYlIDr6dLu0qKMlGVjk4DhV7TtgYw7sB2k9wDKWfOkyOTnzW-SQy_Vow9PbYfokUiuqo2XQ50F4a53RiFuNuX7XdIUuIXQat_-b7xOXzVCIqlGZrNOhXl7BJv9YYa34JvGqsz-_2gowXtJrM5uAynpa0hn54kcRTKwz-VvsJd_jeFcUjYXLA59cGpVGSdE-nlQnjEn-4leiU0KWNeGQltLKpqO7syjimpF7wNGBTpcmkC13DpRmACOgzYZqUkQNVWTSLRViXU5Zj-cRZHFoJ0E9LJzxqLKC8OEdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
مکزیکی‌ها بعد بازی بیرون ورزشگاه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/92198" target="_blank">📅 00:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92197">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kW7zw0PK0RJuldGtdxUAZfsYTW1_ZwZmV_lkaDAXmlBbUrZuVrtB7nGCreA_Gp_-bww4Hp-yzvv0Ov44QWX4EYccelG9fn0s2C8Ls7Qj0bPeksi9qz5UxW0eqTVps4wkks2VdiXjKfqrc-Jd1zpz4ow1zLUy-cvmK4tvoe55emeIxiAWq7mmlDJCxa-J11c4hm9GksS4-d3AkfWEUUiDG-Tpd5WDsmIpodTDnYdDATTTnqeJLxBYxMfhsK0lWvZItK-MEC01jrkYOwa9eI5Fpl_ihRkbvudad1b249Zj7c604IsdFoqLJPdpvipxdvp8FRvfWud0oWkXMii4sT8oRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
جوانترین بازیکنان تاریخ جام‌جهانی:
۱۷ سال و ۴۱ روز —
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نورمن وایتساید
۱۷ سال و ۹۹ روز —
🇨🇲
ساموئل اتوئو
۱۷ سال و ۱۰۱ روز —
🇳🇬
فیمی اوبابونمی
۱۷ سال و ۱۸۵ روز —
🇨🇲
سالومون اولمپی
۱۷ سال و ۲۳۵ روز —
🇧🇷
ادیسون پله
💥
۱۷ سال و ۲۴۰ روز —
🇲🇽
گیلبرتو مورا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/92197" target="_blank">📅 00:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92196">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyIlqW8ixWEJ3t-j0kRO47J2vuxjjtufc_tocLO_lKCyEQWn_y_M8psqS9o6zStnnCc8KqkjsDfYxmOKny68B20nkEWCHldlDvN2Kr-JBgkx6LX5i8Rg4yqx6ucR6XV7RIgJr4cqdvQ573X6a7wisR__ypZuDHfgypFcZzYwlzZLvGOSBuIYIfMuRZnfT_hkVzNr5OsNKp0UH5k1sf2SI-iXjwCUbAFr07ofVRsyuw5yJTqooj2pi4qAC2p7w_3X_qaVJlCE9nIudEqxhLCczm6CJ3J6K2F23PZjhu8zd0Rr2RSTywTELEKra8Zzyav1iQ3abeKKxf0pPeRwo2JRfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇽
بهترین گلزنان تاریخ تیم ملی مکزیک :
۵۲ گل — خاویر هرناندز
۴۶ گل — خارید بورگتی
۴۶ گل — رائول خیمنز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/92196" target="_blank">📅 00:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92194">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dbae198e1.mp4?token=QX0uEC-DGf0tBKI18bh46bswh5-qha9lWXKnJnrUIFnTMJH83pVU1CRMQXgDe-rQ_e7QX9VBB__FwH6MwdaK9SivQb5ugQKHldVq0yaOfocDXAjd3Gt1h9O7n7C9cnI4KABTEAwlRCVknZpikGGGhe4zfENGIsc4ky4Wu6z941q5N_ObRErJKaskB7EumrXw4UapTnzTfN1qn8KHvviBZllDPZ7YJiBKreg4Jt8F_5VnPThfDIFs4S1hdsDs8Xxb5tTeQMvPW_pX-CPeTX_zIltFYgUzPAfPKC4fc2qxStTsLIBEBR7ZJus6obvlqcPRZ01uBQ7lzueM5PSWxhcBTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dbae198e1.mp4?token=QX0uEC-DGf0tBKI18bh46bswh5-qha9lWXKnJnrUIFnTMJH83pVU1CRMQXgDe-rQ_e7QX9VBB__FwH6MwdaK9SivQb5ugQKHldVq0yaOfocDXAjd3Gt1h9O7n7C9cnI4KABTEAwlRCVknZpikGGGhe4zfENGIsc4ky4Wu6z941q5N_ObRErJKaskB7EumrXw4UapTnzTfN1qn8KHvviBZllDPZ7YJiBKreg4Jt8F_5VnPThfDIFs4S1hdsDs8Xxb5tTeQMvPW_pX-CPeTX_zIltFYgUzPAfPKC4fc2qxStTsLIBEBR7ZJus6obvlqcPRZ01uBQ7lzueM5PSWxhcBTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میم جدید
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/92194" target="_blank">📅 00:38 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
