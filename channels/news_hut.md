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
<img src="https://cdn4.telesco.pe/file/KGnE1t2xKdokcPy29rEPDZdGCJn6q0-XFabDxpFG2aC6HQqM3vCFGSXfwkza5tbNNxQG2nRFEcFscpWwkNqWVc7w1YPbb3xseiIZfsjCaxXwOJCc_BCg_7ozW62QhibYWMm7eR9HmjX6odoOA_oGagmTV4P_qVO3PJf5s2cVmxzqP6vokwDtfhauWvDVSMV_ePJQ40nbuPnVotSTYS1kMJpXl--OjAs4E6T3PXuqByGqKfy1dD9dbI8_75UZQUwSxHAeib8S29UpBcxnr0yljHEOezaEusCaDT1uUGFreSd78QuA1o7lfeZNeKEQd8p8eZhHVFp8G6wF_h6y_-53nw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 184K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 10:37:55</div>
<hr>

<div class="tg-post" id="msg-67768">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d25ed65b27.mp4?token=dHjK-0FjGkSjRGzR6s3ix21nG12llZ8YDtWRp61Fn4rTtIJF3NwzK6FQRXQ3bHBjg7EbgfUHynl8V5_t0C8_8OQPhtEVThWqyDHl0EN2peyjZgNSF8Uq2a5wnxjscwDn8BSQKzbK6fqnEnKHNHW0-Cxig7ZGI40-BQdBWnD6ETsmoDf_aVPnFHZdXUvp0CtgY4GfOLTxb1fLm0zYK1q1FHXk025jMxyLpskVGYA0uoIu9Ot76uArBZLiPp__a_dtnQ0_DluFMxYIbOyNucE7oxrU4_Dlb27xrV7FGMgE2Nz3JsaKupjp1V9giQ1KrTzy8TK789Lc7mKmYFikkbav2lul13qTGt9-82XsKp3rlpg-xWA8RN8uzCwFuOEvcplzK3fDl90xpMjw3b-SGWwwqLz_Vfg_JafOSPTciW6xStDz4Hy3spABP7Cc5g_Q8uCzvksA4DVip4Lq8pa90-i-UaQSSWM1K6zTbTos0Zlw5pn2-itWD72ArS75gAHXqhiUKj1yBp-kVLKLVQIsCes7zRr4WrvtSHTmzrxeQL3sGgwEgwdTszAaWrgOAlAczKVQ3DOiV3DDcMzuDpY22SCgKZgjgZdidvTIn1r8NZeckFsd1SobbXLu8u_0VU1tm7Njst6cCUeeFcO2oqMPcmyVDi76WzgzPWp-BsFX3YocQJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d25ed65b27.mp4?token=dHjK-0FjGkSjRGzR6s3ix21nG12llZ8YDtWRp61Fn4rTtIJF3NwzK6FQRXQ3bHBjg7EbgfUHynl8V5_t0C8_8OQPhtEVThWqyDHl0EN2peyjZgNSF8Uq2a5wnxjscwDn8BSQKzbK6fqnEnKHNHW0-Cxig7ZGI40-BQdBWnD6ETsmoDf_aVPnFHZdXUvp0CtgY4GfOLTxb1fLm0zYK1q1FHXk025jMxyLpskVGYA0uoIu9Ot76uArBZLiPp__a_dtnQ0_DluFMxYIbOyNucE7oxrU4_Dlb27xrV7FGMgE2Nz3JsaKupjp1V9giQ1KrTzy8TK789Lc7mKmYFikkbav2lul13qTGt9-82XsKp3rlpg-xWA8RN8uzCwFuOEvcplzK3fDl90xpMjw3b-SGWwwqLz_Vfg_JafOSPTciW6xStDz4Hy3spABP7Cc5g_Q8uCzvksA4DVip4Lq8pa90-i-UaQSSWM1K6zTbTos0Zlw5pn2-itWD72ArS75gAHXqhiUKj1yBp-kVLKLVQIsCes7zRr4WrvtSHTmzrxeQL3sGgwEgwdTszAaWrgOAlAczKVQ3DOiV3DDcMzuDpY22SCgKZgjgZdidvTIn1r8NZeckFsd1SobbXLu8u_0VU1tm7Njst6cCUeeFcO2oqMPcmyVDi76WzgzPWp-BsFX3YocQJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رحیمی (زاده ۱۳۰۰ تهران – درگذشته ۲۶ بهمن ۱۳۵۷ تهران) سپهبد نیروی زمینی شاهنشاهی، آخرین رئیس شهربانی و آخرین فرماندار نظامی تهران بعد از ارتشبد غلامعلی اویسی بود. وی از نخستین افرادی بود که پس از انقلاب ۱۳۵۷ ایران و در ۲۶ بهمن تیرباران شد
👑
@News_Hut</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/news_hut/67768" target="_blank">📅 10:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67767">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95215f1b5f.mp4?token=Ym2CFI4tJPHS3KUCrS7ZetP8StPGG_dyjlgeo5SWjmIav5wLs_Th7wOYx_aSl33sUOXbZ7kiRylVs0U4U-7dsWeCA-T1Rvdg-klyjF1aVzWOaZXTpnJYWjvKLYeLLHLwx9Y5_B9owZ2A8oI_gwwRvP4BbbG5SaYmmZmnzWSisIc-gZM49bczwLq8Tsy0Jn2PCJ6yicJtMwjh5MvsEYxUqO2_tbSlyFbu0HqiVoZFRpsJFRF7O_HC72lhJbq4X1o59Y-D7n5WOKyfRUFHnRQ3sitn4rmUBaDKz3B0jdEK1ToOXl5A0xCANUoNQY_urpvnUxGkAbU7AYj95cRpb0D-Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95215f1b5f.mp4?token=Ym2CFI4tJPHS3KUCrS7ZetP8StPGG_dyjlgeo5SWjmIav5wLs_Th7wOYx_aSl33sUOXbZ7kiRylVs0U4U-7dsWeCA-T1Rvdg-klyjF1aVzWOaZXTpnJYWjvKLYeLLHLwx9Y5_B9owZ2A8oI_gwwRvP4BbbG5SaYmmZmnzWSisIc-gZM49bczwLq8Tsy0Jn2PCJ6yicJtMwjh5MvsEYxUqO2_tbSlyFbu0HqiVoZFRpsJFRF7O_HC72lhJbq4X1o59Y-D7n5WOKyfRUFHnRQ3sitn4rmUBaDKz3B0jdEK1ToOXl5A0xCANUoNQY_urpvnUxGkAbU7AYj95cRpb0D-Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
انفجارهای دقایقی‌پیش در مناطقی از تهران بدلیل خنثی‌سازی مهمات عمل‌نکرده بوده است
@News_Hut</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/news_hut/67767" target="_blank">📅 10:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67766">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a14613e56.mp4?token=g1W5ScdiH_hxnzzciYg5un--bNl3aogHQ7I2-q1oBUqz2X-flJ691Vs7sLmaJvxptrCF3mP4UMKGxJpW735_Y4R3A-jxcVOp_tr3fx7XEGDz0qwXjONtO_yuStBaixkG9HNvqP507Bbi-cI176YnsivIQMwK4aFg6sAfSNK9-FDS3LpnF4ItH77_mThJBUZekId61yHc2oaYd81CyaqqSqlCnpEjYCu8hU8kstGw0QQz6oMYVgpswFQj3AQsNDVi3b4ab2Z3GqXce9Rv0gTkpu3tnmBc9a0ZtLXHjXzqKaPXc2oB1YIs_AOVyuQhi4idLmNUWUzG7MHqCHpa0dBLbmtnBs4kty_iJnWcSWi4NfzyhhDbxHMXKJg0UCMrX1P4j4yoScrILx-okH104CdiBRkvDQGItWcYt9x2k5717MYfBvpZ8mFi42iDCExJnH95O15K7kCbVSI4wPdJxyl8aeLfG-HIwMvpXZojZDDp7eCFlyjmMeCYrgRzEb11J3Y0nZ-8GRlXHhZfDNnFWo1FxvbownMTvDajbaWTC__S_d7Z9coWMbm5VXpi_XYxvvQKmxTnm_jBWzWW5l06snALZ_f_Y7b0BAeUmJhTTrYJvFnaL8g5hrA5MR3LvwnSBS3nHiStcqdzlCtcqtM_HXSuFHnuHrN1fe7emeZMtRweZFU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a14613e56.mp4?token=g1W5ScdiH_hxnzzciYg5un--bNl3aogHQ7I2-q1oBUqz2X-flJ691Vs7sLmaJvxptrCF3mP4UMKGxJpW735_Y4R3A-jxcVOp_tr3fx7XEGDz0qwXjONtO_yuStBaixkG9HNvqP507Bbi-cI176YnsivIQMwK4aFg6sAfSNK9-FDS3LpnF4ItH77_mThJBUZekId61yHc2oaYd81CyaqqSqlCnpEjYCu8hU8kstGw0QQz6oMYVgpswFQj3AQsNDVi3b4ab2Z3GqXce9Rv0gTkpu3tnmBc9a0ZtLXHjXzqKaPXc2oB1YIs_AOVyuQhi4idLmNUWUzG7MHqCHpa0dBLbmtnBs4kty_iJnWcSWi4NfzyhhDbxHMXKJg0UCMrX1P4j4yoScrILx-okH104CdiBRkvDQGItWcYt9x2k5717MYfBvpZ8mFi42iDCExJnH95O15K7kCbVSI4wPdJxyl8aeLfG-HIwMvpXZojZDDp7eCFlyjmMeCYrgRzEb11J3Y0nZ-8GRlXHhZfDNnFWo1FxvbownMTvDajbaWTC__S_d7Z9coWMbm5VXpi_XYxvvQKmxTnm_jBWzWW5l06snALZ_f_Y7b0BAeUmJhTTrYJvFnaL8g5hrA5MR3LvwnSBS3nHiStcqdzlCtcqtM_HXSuFHnuHrN1fe7emeZMtRweZFU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
سید علی خمینی، نوه خمینی:
«هر کسی که بخواهد برای دستیابی به صلح با آمریکا مذاکره کند، خائن است.
هر کسی که پیام‌های دوستی برای آن‌ها بفرستد، دهانی نجس دارد.
مشکل ما با آمریکا، مسئله امروز یا دیروز نیست؛ این مشکل دهه‌ها پیش شروع شد، زمانی که آن‌ها کودتا علیه ایران انجام دادند.
اما با آنچه اخیراً انجام دادند (ترور خامنه‌ای)، بذری از دشمنی کاشته‌اند که هرگز از بین نخواهد رفت.»
@News_Hut</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/news_hut/67766" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67765">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4qbZQo3jhbIaU1OOI5VnQJHx0goE6WC8pMr4WBKq8JKSnke6mUZyhIzIaJPvAoeu2TmAOd6e0kqQ0x_OSrJpsyEzEm7GEjO4YcsGyRPgkoKQwUaXfO-edtWDVyPx3AL5edQ5S0wf6_a0BmkmR9AzgUd5vLL55H9Tvr9cmKHHFlIYAywC6Ei4X8NEydywYmBkCG1zQvu78-jZvcQD-4VbjHYBpnbKp_wKsFq4jQbZn1iH-q-G5lGKH6g7N8ennWFYmFCJBcULn8TRd-VA5_FS_PhG_0r9A1XB1PFaplmBIAriKNMtPOMK_pnsNabzgjfRrNIE6TOgBcP5KfdaurXKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
فردی که «رهبر عالی» خوانده می‌شود، در حالی که رژیمش رو به فروپاشی است، در انزوا پنهان شده است.
وزارت خزانه‌داری همچنان از تمامی ابزارهای در دسترس خود برای منزوی کردن او و دیگر نخبگان رژیم از نظام مالی جهانی استفاده خواهد کرد.
ما این دارایی‌ها را برای مردم ایران حفظ خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/67765" target="_blank">📅 09:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67764">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/news_hut/67764" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🚀
🛡
ثبت نام آسان و سریع
✔️
📱
اپ
ل
یکیشن را روی موبایل اندروید خود
نصب کنید و بدون نیاز به
🔤
🔤
🔤
وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67764" target="_blank">📅 02:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67763">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/g3NsfmONA3q3f-gr-kLCDAnrh7AFM7sxuY6y4Oz70Cq6-qdN8Fn1h4jYXD_xXwk-8QP2aH55PEUev7MzDPufq7tr9mwnFvgcMvW4PjFx0lT_8wdQVUJEoxBvQAWO86MYZcn8XddhkOaqHVWIXgNV3ZhsTPYfMR0Sdq3IKC94ol5S7snmr1t9ol7WlPB6YeecwzX21pDOSimz5U25p2JMe7JOEyOXriMn2sRuZcHv8eGeMhHS_gdsoEfTPQ-gBaVxlYg6An8QhiiQZTg3ATVQNcb4yn7EWhp4j2wLKskWjI-e993i3nF4Iv13EDhNIx0IgcyDT1cRQxM2O0zEe6uEAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
قهرمان جام جهانی ۲۰۲۶ از نگاه شما کدام تیم است؟
✨
با پیشبینی قهرمان جام جهانی شانس چندین برابر شدن بردتو امتحان کن
🚀
💥
متنوع ترین آپشنهای پیشبینی در
لنزبت
😮
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
برای هر واریز
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
🏦
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از واریز
🔣
0️⃣
3️⃣
کش بک هفتگی
📇
امتیاز وفاداری با انواع هدایای نقدی   روزانه مخصوص کاربران فعال لنزبت
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
A19
📱
https://www.lenzbet1.living</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67763" target="_blank">📅 02:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67762">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUyaMGNNppORqfQYc7GdnjvzGYnI6nndRHdUiZC2hUQ1_6SdaKmIvbaQewO6B2ZqrL0s7GVJ7ZQooeadaR2mcr6rsr8ekIqon2ZynbbyY3UjsG_cay4-dmBZL00fQTtEZobzxHxexKZGLdZxm4UYFrxwzTd--429gztWvr5UH4B72xk-6ig2j2uP232_UPb_meS5QQwAqI9vg6XYqlYtLOosk_EnfGhyDn7RbaV2ojdXvB4RzBbOWLiBVj0RjOGD9pbRElTSF6s6AymqV4qLgeWNNtqz1iUrN0tZ0LPSs3U4ICL22wsM5KKrXWk_ydhR94o_Xj07zMDvk_CuykRjWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67762" target="_blank">📅 01:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67761">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
❌
یک مقام ارشد آمریکایی:
ایران‌ با عواقب وخیمی روبرو خواهند شد اگر از انتشار یک بیانیه عمومی فردا خودداری کنند که در آن اعلام شود تمام مسیرها در تنگه هرمز باز هستند.
اگر این موضع [آنها] فردا نباشد، روز خوبی برایشان نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67761" target="_blank">📅 00:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67760">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsiF_czdiv3P_s_KBm5wvDzdsO4Ki5s-i3HsWXIxZUReCNC99AGrQkQxYXp16EA5SFEMZKSbFKqZ_A3hpib4CRDsdZ9APVPqmpmNIIFxBfu0W0Bep7I5WbK0pOJqoPAS82u534NYQbLFMV9x9k-607rBtJZS44doOjZu9eYu40kYdxNIOei37rr9pz5xzblUfcdwrt756TtFT1dJSXt-BT3hXhIr58LdGE7-blJ06AyKj7831TqrHMLs5FEVqKDA74iHb2y2hsd7YLkQDXaUqOV1JnarwdmPMnSSfyntj27Nk3gcgCS5cQYd3xUdg4ZC-d64WLsgzbehuUBky3fWFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
به گفته مقامات آمریکایی، ایالات متحده به ایران تا روز شنبه مهلت داده است تا حملات در تنگه هرمز را علناً محکوم کند و باز بودن این تنگه را اعلام نماید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67760" target="_blank">📅 00:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67759">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کشوری غنی، اما مردمی فقیر
💔
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67759" target="_blank">📅 00:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67758">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
وزارت آموزش و پرورش:  ممکنه امتحانات نهایی به صورت داخلی برگزار بشه.  فردا در جلسه ای در موردش تصمیم گیری می کنیم.  @News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67758" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67757">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
وزارت آموزش و پرورش:
ممکنه امتحانات نهایی به صورت داخلی برگزار بشه.
فردا در جلسه ای در موردش تصمیم گیری می کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67757" target="_blank">📅 00:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67756">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/024bc9f4e4.mp4?token=cAgeY62QBhwzSWEWd6lvcBjH6tYUlse0F74HFGDi1QfNUwvk1ZSv7K7hFzmPVJdscEIESB9QE8J8GA9CkgUvg52F8_YEl8gwVQf_5pBtPW_C9l-CSVnuTu4pS3JLBpPnLx7bcHxzDf326vEHMa63mRJKKLLGS984giRT1DtiR05GEEibMNBEJ4ewNKvWbdXyadl0nEEMlzE4vZrdZOWa5ynMcPaQqUy2UqgKlh3ZDcB1GfRZMo6ofm4-C4SYN0-elCNTFUZq0adr-Tzu2gaJPWBAwLVac5O3aBaXNnwNX0Vhab-LMIywb0wzpIca8GXHUoi54EAlbZYPZv0bgOcKqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/024bc9f4e4.mp4?token=cAgeY62QBhwzSWEWd6lvcBjH6tYUlse0F74HFGDi1QfNUwvk1ZSv7K7hFzmPVJdscEIESB9QE8J8GA9CkgUvg52F8_YEl8gwVQf_5pBtPW_C9l-CSVnuTu4pS3JLBpPnLx7bcHxzDf326vEHMa63mRJKKLLGS984giRT1DtiR05GEEibMNBEJ4ewNKvWbdXyadl0nEEMlzE4vZrdZOWa5ynMcPaQqUy2UqgKlh3ZDcB1GfRZMo6ofm4-C4SYN0-elCNTFUZq0adr-Tzu2gaJPWBAwLVac5O3aBaXNnwNX0Vhab-LMIywb0wzpIca8GXHUoi54EAlbZYPZv0bgOcKqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت امور خارجه:
ایران اجازه بازرسی از تأسیسات آسیب دیده در اثر حملات آمریکا و اسرائیل را نخواهد داد و قطعنامه 2231 شورای امنیت سازمان ملل عملاً اعتبار قانونی خود را از دست داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67756" target="_blank">📅 00:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67753">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjWXpJrfEIYdzjudKjnBAw3XwumH2Jx-6Yh9BRDYf1g7QnfcPtN3aG0_YB2lgxyaaAt4jULCnpqppQFc2S1FHz5J-AjC6mvD4xLGdY2faO5GZ5WqMC9hiOGIKt6jzlaqPXgnA8YC7W05eRlJ2SqPMvcbOW3IsZk87RU4Byr8wmQ0gFmF4VdEvoVY3ERazBhWQ_tqV4V1_OQB_bavjjJki2L-Oy9L_tMQXPOvbu9t8n_Gw5XolhOVVXkRqkdNedOA5NaC6AVPVAQBxG9TZOCD0er-XV2RHfBW7Y9dJKNXCDntCEMXImfEs2AtC1IMfYjjkVu9Ot95KoPZzBAJQxRK0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LhHvZwXvtcW6rKnbVk8xW5gdzzZGV2uxGSkNCC4vgMevqm9cdgYLM8PRKCEn9mTI7GMVJI6Jo-kLAByELHzeMHmM85cdJxPtGl00PskrP5tJ00JUlp1W97YMZIWFyfoo0-J5FeDHXAOtIjD1XQPFIdsKn9pdTZfQLGe9nnGJwLL9cEw78ucccum6fSui9WfD3Ya2-me_7hOXCQ53szt8JdvndhQ2_x9qhnGnjvdsfzDiBnFb2Jg-sujLqTJpI0hPl3xYmdwBLvjLyB7ceo5DdL6hxN_Jyezy28AuiOZBucrDdaluIums6WhdYZe4xzg8TJQuLIsn_QummbBZdBM-cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONhfIFY-F4rSHol8RkawhITl7MiOpP3Lven9H7aTJdE9qDbTiOZ7Yfw_jeMfFRzGePMQ7y6O4GSuZXfc8aKn7tm06UG3ncWiaCy7f7yOKGs7c6C-ELadh96qMMOyn2hZ4BFna5aV8-W-XdkxGg-5NE3AopIJLWsTHWt96KpJLo_94O4BPQ1qZpvNtJ9YSH3EGwJg54FVS9fPXwT-Pqc0NkdeAxJXm_QI-sUYk4B8MnVhiYUG6ChRjFA4J_2HhqtpMco7p5JYyUk-mE8IssjVcIq2XaFLiZjjB3KdHkwEmcAcoTvwDGOE3mL08LKSzKgS4kJz1i16G1V7JdIst-nd8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⭕️
شبکه خبری CNN تصاویر ماهواره ای  ادعایی را منتشر کرده که نشان می‌دهد ایران در تلاش است تا تاسیسات هسته‌ای واقع در پارکچین را بازسازی کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67753" target="_blank">📅 23:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67752">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08e999307d.mp4?token=GAQNZFEO3exKfwA3IFl5Lj9bZh4JV1_iv5bxg_aougOqPBefCT78sp8aYfJBxpRD0LTQcucLSJkqB3ID0TRBVw5VQQwmSYiTWdXSM92i2oVxADfA3YdmJ3FfmPVcm7u0dw-OmcHpIz_QYXFlL72x1ZVzfAW1Wtuu3sLG6A8y0XtmxdEABiqzZ2lLrVedn7rOW7gkltq0uOwzHnj0rLsDUDSjPmQ8NXX5M9IScxlFfJvUiutIPqZonQqfrY69r-_DAbzXQBnZp4rhfeSYsjXUhNCvzRmIMAW_8JIee5HSX2Rix9RtbfCNDse4mZX_6bb5QOb2Cf6A_jt1vnJgRqBQiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08e999307d.mp4?token=GAQNZFEO3exKfwA3IFl5Lj9bZh4JV1_iv5bxg_aougOqPBefCT78sp8aYfJBxpRD0LTQcucLSJkqB3ID0TRBVw5VQQwmSYiTWdXSM92i2oVxADfA3YdmJ3FfmPVcm7u0dw-OmcHpIz_QYXFlL72x1ZVzfAW1Wtuu3sLG6A8y0XtmxdEABiqzZ2lLrVedn7rOW7gkltq0uOwzHnj0rLsDUDSjPmQ8NXX5M9IScxlFfJvUiutIPqZonQqfrY69r-_DAbzXQBnZp4rhfeSYsjXUhNCvzRmIMAW_8JIee5HSX2Rix9RtbfCNDse4mZX_6bb5QOb2Cf6A_jt1vnJgRqBQiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب ترامپ رو تو مشهد دار زدن بعدشم ماکتشو سوزوندن
گفتن خودشو که نمیتونیم بکشیم حداقل ماکتشو بکشیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67752" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67751">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtNa-OaHDVneW-ap5qGJ_0cE_rLc-1YWUY3cGMB-eMbfwBqOWtowJlpP1wWnbQn7m0ruQLq4mkF3HN9NYgkZ56Ljvq4XKEsbCQy68enGHO2fgQDfuYmC81qYXwOzmlVRwJ6WLPkOsKnh0vzfvCeXzCANWHz0j953z9AsyYXlFADjXtnaXCJbPY7XLPeMwSjjniSFEZv776L26nuWkH6XyMwrOo4_I0d-M4o5MSr9JBUbJIh8Sfrxl7Mgw0QWEm2gSzygGcMb_4a2WyDEOa8sh7WsmdrbFSA047sf6HchxdzcxpEfWzGSExeqxOpb4de3k5MqpHAq3_OaIVWoXqpskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قالیباف:
در جریان مذاکرات، به معاون رئیس‌جمهور آمریکا توضیح دادم که ما به شما اصلاً اعتماد نداریم.
به نظر من، تنها کسانی می‌توانند با ایالات متحده مذاکره کنند که برای جنگ آماده باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67751" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67750">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.  @bet_maxxx @bet_maxxx @bdt_maxxx</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67750" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67749">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromnegin</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAEiGawFGl7_cmbtzT2t9OdiKGks9L2_bEyp76OZSz_eAL5_X1o89IwLZ7BS9gelKsS1ph9FTZWISJCj_KMB66FFcX2c777m242SGXpouF2MFEGfT9AZbM4wTx2YOIm-mK5gsLRWCVEcNkZyB813odPoKCe4QxFTCXeF-tPrrcALMwcvD5vi1976ZXTCUxWu3pykYfhtM-V3X5MzoZQmHmw_722stBA37N_idq2j-b6KXKraL_Axmfb2HOi8vbYJMb2D3WXATAGmiU4oLEyADtu8fLoHlYJBQ50uN6x_Z6cqPV66UKkNXyD26pA3xPoWFXddECjyvIchcCjq3X-ZVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال
اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی
همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.
@bet_maxxx
@bet_maxxx
@bdt_maxxx</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67749" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67748">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad131e48f.mp4?token=U2IoC9J0w9VYyIMvBqheL51JrUCgnvtX5sYvyhUJSE63SQxkrToN8zb0KJiK41zIjNDBwnxUNRa17qxDmmWZv7HJwF6QQRR4PYORe3dFH5RJGt0833Fj6OUEBFbCCWRwtDxbW8bbu6aBtImj40uzMGBQyuJqDVSjXvf8SbWgpGHXmdtHRdHb58LtdDeiNcUeEOY-QKDhGdr0neWamPiIRN5aRF73lWmyT5kCYseinl2iLhq7C1OTBWINgN-R63gb4P3PqSooc6vayra73B3PIzBm0apmELCG6rSQSBSa9Ujm0mRH4J6djdK0M3WGvKrSbLuMRNv6X2OT95_AVw7rzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad131e48f.mp4?token=U2IoC9J0w9VYyIMvBqheL51JrUCgnvtX5sYvyhUJSE63SQxkrToN8zb0KJiK41zIjNDBwnxUNRa17qxDmmWZv7HJwF6QQRR4PYORe3dFH5RJGt0833Fj6OUEBFbCCWRwtDxbW8bbu6aBtImj40uzMGBQyuJqDVSjXvf8SbWgpGHXmdtHRdHb58LtdDeiNcUeEOY-QKDhGdr0neWamPiIRN5aRF73lWmyT5kCYseinl2iLhq7C1OTBWINgN-R63gb4P3PqSooc6vayra73B3PIzBm0apmELCG6rSQSBSa9Ujm0mRH4J6djdK0M3WGvKrSbLuMRNv6X2OT95_AVw7rzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رونالد ریگان چهلمین رئیس جمهور ایالات متحده آمریکا:
در این سخنرانی، ریگان با یک روایت طنزآمیز، دیدگاه خود درباره نقش دولت و مسئولیت فردی را بیان می‌کند؛ روایتی که سال‌هاست در مباحث سیاسی از آن یاد می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67748" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67747">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXb6QQGwU4YyxWrG_0PGLFXwU1i1QqgwksNtCStxLs-nE88Nw2wFxC3DE8UFMJNQGN__Xo7mhSTmfSLh-OvNFVuJUm4U2W7NZQRINMPVRR-FEYkuAWC7-WGEYRy51ZFEB_zjwaZX_Ampl3jza5YbjkwTDo2QfwqR1_AY8t6qcxmSHWS9V1_NM0qedeMn8z2szRa1XBKn54XUeV3bIyVkBwbhm7fOrsJOP7GmNU8Vm61WirsWQDQpBFhdpM6sNQN76nvMDyY_CicuNIR64gIQ7ngMa7_BC13xQ1irQ44-6lSl-n4C2OrTe0mBwi8kF-NEt4AQTqPZd7pht4AopZx3xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل هیوم: آمریکا و اسرائیل گزینه‌های براندازی جمهوری اسلامی را بررسی می‌کنند
روزنامه اسرائیل هیوم در گزارشی به نقل از منابع دیپلماتیک منطقه‌ای و غربی مدعی شد که ایالات متحده، اسرائیل و برخی کشورهای منطقه در حال بررسی راهکارهایی برای تضعیف و در نهایت براندازی جمهوری اسلامی هستند.
این گزارش همچنین ادعا می‌کند که در پی تشدید اختلافات داخلی در ایران، مسعود پزشکیان، رئیس‌جمهور، و عباس عراقچی، وزیر امور خارجه، با فشار فزاینده جریان‌های تندرو و فرماندهان سپاه پاسداران روبه‌رو شده‌اند و حتی احتمال کنار گذاشته شدن دولت پزشکیان مطرح شده است.
اسرائیل هیوم به نقل از منابع خود مدعی شده است که عباس عراقچی در تماس با میانجی‌ها اعلام کرده دولت ایران نتوانسته موافقت سپاه با مفاد تفاهم با آمریکا و توقف حملات به کشتی‌ها در تنگه هرمز را جلب کند.
این روزنامه همچنین مدعی است که یکی از گزینه‌های مورد بررسی واشینگتن و تل‌آویو، تشدید دوباره فشارهای اقتصادی و بازگرداندن کامل تحریم‌ها با هدف افزایش فشار بر رژیم ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67747" target="_blank">📅 21:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67746">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7q2YCcxvNz_Y7KJ48KJNysT7jB8z-GVSDxsaj-W6wO65DG58YifBhEKCoFhFBsE2yzSFGPNkWi-WAWA0iNPnPAo1NJP6YqmCfzjl3-SkofS_8wVPoBWMmzyeGWE-KOTK5NRSO_txYn-itZ31paHafTNeLe-K1ChXVR9KMdr27OkLiAKvNjS2PPoXQ2CRYPHsz0Jic1vGdRkhBAzLqube6Hu5vtogB3Z9R0vX-0Kd76ij__OawxgsWgX81EHX3rhynyf5BtXcxj5NCY6_RGvYhrFLkoZ2K5gPFkXKCe4kYLzeXYHS5jEcSrudhexgxbT2TsiQvFkpgsYymHqXDD3WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
باراک راوید:
بر اساس گفته‌های یک دیپلمات آگاه از این سفر، مذاکره‌کنندگان قطری با هماهنگی ایالات متحده، به ایران سفر کرده‌اند تا با مقامات ایرانی دیدار کنند و تلاش کنند تا تنش‌ها را کاهش داده و شرایط را برای از سرگیری مذاکرات فراهم کنند.
این دیپلمات گفت که جلسات بین مقامات قطری و ایرانی در تهران همچنان در حال برگزاری است، "اما واضح است که هر دو طرف تمایل دارند به توافق‌نامه اولیه بازگردند."
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67746" target="_blank">📅 20:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67745">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CS_TQaagjmgZ74AAKxBmXwXBOY_B9XsQSxFT-UjW4FPtLHToOLfKZFewi-1ZCEuHfpR0UHhFeAb9CJ-Hp8GLUGin_Wibbtqy1Tl6euJhzXNnDUV2vJ_YBpdENhXkXO8MES0W1E9Y89z0ocipwMHelmy77xBBs2xzxFcy3hP33m8SRyoaALyoSZE9hQsxINzar551KJafFvz9PwHVSkGjiGqDNxtzG9pqOcLXbeaIWc-zE_888v_jQbCV8fr7GGErTVbuaUc_6w5yhDcGVle4K76hQxShcpEn1mhoRO4Ltun92_VIjP7mWxdJKs30dpM0sfDXOOkvHJJF8TEOxeopUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ به «نیویورک پست» گفت که دستوراتی صادر کرده است مبنی بر اینکه اگر ایران در ترور او موفق شود، ایالات متحده باید «به‌معنای واقعی کلمه، آن‌ها را چنان بمباران کند که هرگز پیش از این ندیده باشند.» او افزود که «مدت‌هاست» نفر اولِ فهرست ترور ایران بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67745" target="_blank">📅 20:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67744">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlFjHt3CpjGUGeBUgZUvyFHYpw7ATB82ueqz01ucmFTAtoV7sRLsshKpWaFAoTpMb3rHUwbtKVsR02zziUdj4GesqDwhlLPaWGsXC3sh8SuMYs3u0fC4LDLtN3kgSJitfZtm_DhHiBWDSWgqTbWRLjtWFoaI5cYw9-44bY4tkgOhiPHHv-paKxaChmLoyZFdhsaBpq7lJG7GYjD9dqPgN3laco0-2oiMY3AS7IO9xTYRm79tUHkceNvhsz1bolkox6mzWePbWMmP2cmkXuZqmxladbyTdgIwMCVp4Su4SzN5hCa3mrW0dGU2n-azL5UL5aEo5DtsSEGKahhjInZJVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:
ترامپ و خبرگزاری آکسیوس را نادیده بگیرید. هیچ مذاکره‌ای تا زمانی که دولت ترامپ به تعهدات خود عمل نکند، صورت نخواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67744" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67743">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
آکسیوس:
پیش‌بینی می‌شود که ایالات متحده و ایران هفته آینده دور دیگری از مذاکرات را برگزار کنند، احتمالاً در سوئیس.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67743" target="_blank">📅 19:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67742">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=lse5m2fnsVw6J_fZPXGhh3aaYraSZTY-cbqBF7e9AxC9hal4xnqhaa2Rl2HHlpDqUeKEqBQVlXt9DOgan7-3Ak9XHHbR2uIlXRRbJOzN-J1rHNBl481AqfYVoWsvikuNiDgVOD-FZgO-Mdk4FOwzJFSNkKqHc55P4ZT9hpoQ7_cFt_QsP7MeQrjevhP5bKw9_wGGzeCUoiC8jPfXFJZD4MWeE_YipKfLxgX2bc7pT7MdOyaEEx2mAbevRMclOLCooiZB7yXTb2Uwx7N4aojgyXebL_kJ9nmrezgKCH51zkdvhnY2nErwB9UgpX-hEih6i45zqNNHm3dFtG99tJmGDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=lse5m2fnsVw6J_fZPXGhh3aaYraSZTY-cbqBF7e9AxC9hal4xnqhaa2Rl2HHlpDqUeKEqBQVlXt9DOgan7-3Ak9XHHbR2uIlXRRbJOzN-J1rHNBl481AqfYVoWsvikuNiDgVOD-FZgO-Mdk4FOwzJFSNkKqHc55P4ZT9hpoQ7_cFt_QsP7MeQrjevhP5bKw9_wGGzeCUoiC8jPfXFJZD4MWeE_YipKfLxgX2bc7pT7MdOyaEEx2mAbevRMclOLCooiZB7yXTb2Uwx7N4aojgyXebL_kJ9nmrezgKCH51zkdvhnY2nErwB9UgpX-hEih6i45zqNNHm3dFtG99tJmGDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آتش‌سوزی گسترده در مجموعه اکسین پلدختر در استان لرستان
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67742" target="_blank">📅 19:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67741">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMkfcvyDsBUPN3--kNHUkFhZWtMOvf2ANGSaL9_ToGoPvzoCP8m_7B8OPHT45NXqhKKHQb2esLBk4ZcK8lhQqS3SZqy59z30DYxFk8vUblaCnGOaad7WMwbyr-3G2ODAbJP6G_izRiK-S-Err-rd4rTBgVvNdoyUxEj1wvW0B-7EwJDtnWN3TfUyjSYvAZRmLqXlLFhIpZPvJ6BdwyL8cHWyQ5k1dKuKqEb8qacOavWVQiykBm47WP_s34kjG4lN2Ln0EH7GngaHA3bwLw0SR6pe7XESOsdGeZQcZ-lMNiuwrvYhee0OYSH9xq1ImZ-IrirQjJyh86GcCey7VzSqEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
انفجار در پالایشگاه نفت پلدختر در استان لرستان.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67741" target="_blank">📅 19:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67740">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmq_cpjtFCyH79CKMiYpsuJvRiBJGD4SwHCrp165iL1oIN3FWiCiTENDY54A94xR2OI_Pm8YGHzo0AQzxAoVXbA-wSH_gUTBkuCOoYOEmDnVblx7RsPwypGa4SbfzVXxwjGJfVBFDiWjUOxPw21Z3D7tx-fhV-3pezjATrYMCpe3cz4NKhnbCRBTniecM6IjiRVbVLI3QCFK95Nl-szslFEHfGnCKI9VYT-T9hCOYFs2DHyFjdxw8RGB4JZyRwDIgK8wKWMpRI9TcGUPYbeWuT0hF4-_quomS3BCVtchKm_d9W28D78OFLAE9QKc7owZqdYRmN2BJVMxdKS0T9-cGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بلند شدن دود در کنارک پس از وقوع دو انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67740" target="_blank">📅 19:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67739">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=QZG6tYrD9tBR3p_auyh1rMPdalTbT06ecE3JH8FklqjGyjAu6fOa35Bg5xftJyH4U-XTTV79otZk5VuxqWne4sqbO8hveygh3sPFblNO0-exjEK9kU5pV2DJzwsMmsx_Y_sZxmB-BLuRe3P2XjRBTeq34OzheT6B837e_oMYg5ePJSV3dybJz-d5r4nH88uCiq6QD4-8VQms6Ah6FDrwsD4Wd8Ctt64RD5HM8S7tCGYjxwcqYBJdSC2cTstNZLpISmt8AyKRmHwdXLRbjCtmmVKFWgcdLCIjxKAeGS5yyZZzUuDWruIT69X-Mxi3iTqnPwvmR_swRycISZqVM_VI-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=QZG6tYrD9tBR3p_auyh1rMPdalTbT06ecE3JH8FklqjGyjAu6fOa35Bg5xftJyH4U-XTTV79otZk5VuxqWne4sqbO8hveygh3sPFblNO0-exjEK9kU5pV2DJzwsMmsx_Y_sZxmB-BLuRe3P2XjRBTeq34OzheT6B837e_oMYg5ePJSV3dybJz-d5r4nH88uCiq6QD4-8VQms6Ah6FDrwsD4Wd8Ctt64RD5HM8S7tCGYjxwcqYBJdSC2cTstNZLpISmt8AyKRmHwdXLRbjCtmmVKFWgcdLCIjxKAeGS5yyZZzUuDWruIT69X-Mxi3iTqnPwvmR_swRycISZqVM_VI-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری صداسیما:
اگه خمینی و خامنه‌ای، زمان امام‌ها بودن، امام حسین شهید نمیشد، امام علی حاکم میشد و امام حسن هم صلح نمی‌کرد.
پیامبر خودش گفته؛ من مشتاق دیدن اینا بودم و حسرت دیدار اینارو داشتم
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67739" target="_blank">📅 18:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67738">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFw8s-btqeKCab6tRz-XQBnYvVZ7s0moytI2rRTiRj49HTvxbov-0vzoyT0kxy9v-KThAg4XRivloOk8b7AFAMJQ1oFmBCd071KfIxYI4yzfE8_m2235GUBGMaAlIZRCSjV9IcXhgvch3XZc2BR45GYGYJYYU76QY8hBDLtQm2FuxqJx6K8ExfQsL2Krs3Wt6MqlsTUo1h9C6RfEgRtlvMjaGGqIrnmxPrb1y0Vo9uCez8p6d937NCZ874abOcTgqsGaYc0fxJ_Waxer7-0uHoUq8tc36gM-qAxLCPDRqBDZ_q-57_e4Wa1nw0JkYPBE3DCKaqhP2wyiZWge9rIj8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران با ما تماس گرفت و خواستار ادامه "مذاکرات" شد. ما به این درخواست موافقت کردیم، اما ایالات متحده به طور واضح به آنها اعلام کرد که آتش‌بس به پایان رسیده است. از توجه شما به این موضوع سپاسگزارم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67738" target="_blank">📅 18:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67737">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/te0xciSNLkKifz8zgoUrisloh5_4nxqZRo0ViM1nijcjIeoMPU0AMRd8EK-tP5LeHo7I2GyrjIrUhjsa4kyivWonjdnkaACA8xnDDBMNxgxuoeDxdCNVc0fTc586P87Xku9vuqABu5Ju289YZPaPsV2-s9_iKgnudAx6FbGagUT27D27XV3ZvhaVpcRgh_z_9z_zyhOSpXg3FTnMCj1yOlsDQY_UZolXtOHT_6oJwHxvLCWQQ_mALnaqGBPKyOJNkl_sjsHa12MAbULbljsPLgaNxoNN8G_HZ7lMraUzJXjxMryhuZGk48ebKg63upOIzAq6MT1RJ6jM9tjcB8_1xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیروی دریایی ایالات متحده امروز حضور قابل توجهی در خلیج عمان دارد. یک ناو هواپیمابر و اسکورت آن (حداقل 3 ناو جنگی و یک تانکر سوخت) امروز در فاصله کمتر از 300 کیلومتر از سواحل ایران مشاهده شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67737" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67736">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=HSa7fqxfXGDYI1CpoUCHlN_K6aU9Yt04ytWmyK3PUMECTXOucdAJb35_g5uYmss0NEY9mMeei2_qW5ncRsUoB1Ra_2-QEaYfAM5Kn8_Rj3gHsvixnqa3uCK8rD-XNgDWQZLZOU457LVwKCDzM-x9G-5wFBOqKR-v31OvkiUjSyykkR6MdNosCCvApw33wL1ymzAyuAgep22wXGrhhN5JxK_ykpZe00bA4YbmHRBhrAHJAFrvW4nt48MhwWwpdMFmd4mOd4c1D-KHvEc2lnHO47UggWcknef37wJg9sC9LMR_znF5IBfkLMY4jlxFab73Ihs26PQ3nphS4yxpzBFBqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=HSa7fqxfXGDYI1CpoUCHlN_K6aU9Yt04ytWmyK3PUMECTXOucdAJb35_g5uYmss0NEY9mMeei2_qW5ncRsUoB1Ra_2-QEaYfAM5Kn8_Rj3gHsvixnqa3uCK8rD-XNgDWQZLZOU457LVwKCDzM-x9G-5wFBOqKR-v31OvkiUjSyykkR6MdNosCCvApw33wL1ymzAyuAgep22wXGrhhN5JxK_ykpZe00bA4YbmHRBhrAHJAFrvW4nt48MhwWwpdMFmd4mOd4c1D-KHvEc2lnHO47UggWcknef37wJg9sC9LMR_znF5IBfkLMY4jlxFab73Ihs26PQ3nphS4yxpzBFBqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو‌ ای از صحبت های چند روز اخیر ترامپ که در حال وایرال شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67736" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67735">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67735" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67735" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67734">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VgF3AnhqKGElbozckwu0_RazmCi2yGsgEcSjDQvE8k5-d5n0qpB-p-sD4dNAk7pUIX92vRfkct1Eb1BtRPEVS_FOy-Ik3blVwb7oOZ7DwxiZ3DfLAJD2SDVONKhJKzqmQtjpik3yui26vA364DGnl0D0qJ7Auiuzv0Cq6L6jUL52Gvb2bOpvaU3AxhuS_waGPwAXIcdke7bjeOTr96adqx0qgtVYalT528W5VUDel089c9pzR3PB0h312aNj6SWqzeVo135qJGGV8Sjoid6wYY8TS4LX7pj-geSPkalCi97NeBquu2FpPvkes7WdV8U3il8sJ8jzZQk_K4Y5W5irUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🆕
Link
🔜
MelBet1.net
✅
🆕
Link
🔜
MelBet1.net
✅</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67734" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67733">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d6c6e5dc.mp4?token=cV2qnNuMDCUM85w0wMCIFrtrPmI2B0QENYPd8Fi2-kuKsg8HNB4r0xEiIoUpTWrjEGmEXzSAQzMd3ZcfEAH1MEoc8Q-NR5I3XtLPrLEqa_wtYWMRGyoXIHZ91pt2gPTZx3GzXU1zVEAXDx2bxT6zKL2X93QnWYZLM1sch1oJA3xGinyMpzlu9b1_9T_esGmwDV9CysH3Ec3UEwjvA-mHpOcDnN92q2XmJ2lTZsrAaH4v4sqdq2Q1SRDMB5SUnvlYJa1kDllSjghCOQVuVv6XJOwWcPuJBk1AISmt7Uf937Cp9lhe6rlaSlp0ktJF6GwKBSmsEudM3dDaH3iDK6_A2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d6c6e5dc.mp4?token=cV2qnNuMDCUM85w0wMCIFrtrPmI2B0QENYPd8Fi2-kuKsg8HNB4r0xEiIoUpTWrjEGmEXzSAQzMd3ZcfEAH1MEoc8Q-NR5I3XtLPrLEqa_wtYWMRGyoXIHZ91pt2gPTZx3GzXU1zVEAXDx2bxT6zKL2X93QnWYZLM1sch1oJA3xGinyMpzlu9b1_9T_esGmwDV9CysH3Ec3UEwjvA-mHpOcDnN92q2XmJ2lTZsrAaH4v4sqdq2Q1SRDMB5SUnvlYJa1kDllSjghCOQVuVv6XJOwWcPuJBk1AISmt7Uf937Cp9lhe6rlaSlp0ktJF6GwKBSmsEudM3dDaH3iDK6_A2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇮🇷
علی خامنه‌ای،22مرداد1397:
به طور خلاصه در دو کلمه به ملت ایران
بگویم: جنگ نخواهد شد و مذاکره نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67733" target="_blank">📅 17:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67732">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkOew_xfJ5tJB2quQobMNECnRPQo2hHIsCHjfS8Tc_ppQTbxuOG0nFNd9DY5ZN6SuJbdQsAKuOPY1Z4ujz1U68qPbWGPgbpB-K_NOachG5g8DO2jIg-XKaEjkdGhhyz_Ww5XxK9pSxnqDVpZ_XqNakIVArhCNjumtVWKBL-XvwVsQoD6xyiB5Y3dO33_GJ_d1dWp7CfwgJPNL_12XML456mR10qRJsP3P-GhgP0s4rPzz3R3_BvFZybnRg7kgS0xC7a55rBrFBMDd2BoQcROrObSs7DL8l5PBt1bCZDbC2ghDwZcMbYrqG60ecMlLE-OyekSUfPLUR3zp9B1vD2AOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کارولین لیویت سخنگوی کاخ سفید :
جوون‌های نسل زِد که از وضعیت اقتصادی و زندگی در آمریکا گلایه دارن رو بفرستید ایران خیلی زود قدر آمریکا رو میدونن و زود برمیگردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67732" target="_blank">📅 16:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67730">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6poronblWN8zz9Y0wMPRsuIBgip8p_eBg-nwOghb7pSJiIR1JBKGE4oUM-4Q5iX-_aUgGtyNBxuZWdsmO-0ZxyP_cgI8f0OA5BoP9L2JipUuBcywIB1ZRvMhw3jirfiCjxABIRu36N2n7qF8qKhMUx5gsxgb1mwFNsXRyFmOa3FG38ZDsTsDOfJ7UH-WD9loW7AiNiDOBBo0pegqkTmYzlKNByz31kh7WcpdybVgu9yHE2Y1QpsZpV8Ojq4N_u_thdX3lzCPVH-eOWVXm3ajXVzVAxETqktoID2_fZ7h-JmPvRHySV0Wv8L2ilbze3rAMcxqkMZFu2kpV_-cljo2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1372691bce.mp4?token=REsO12_YoOo2e4hRH8NP1xMgt2_Jrz1yunSK3PxeO5PubtC8hcV-NaPjL-TbJvGeL-1wkSR29yyAY1WSPq6qLf2wBHVabH1jyQTuYdNJeihUFprRLZacQBvZTT9fagaQ_mIOKavrFyUYXPGtO2KABeHEZmjDan_tte1cBm7qrFekE7lZs7MQQUu3-fN1Wm2ij2KaUkMJcgrUlTQbGbFpusm0U5DSsC3Qj18wqKBdCJGCkhMDuHSgQeK7eDHlfft8fJ44azmT_R7AAR4LdosKOvF88AOtB5q9cRS-NyrbxgENo7G4-UDGXNML3bYxUcMi8sp0lceMR8zbe8ienuK9CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1372691bce.mp4?token=REsO12_YoOo2e4hRH8NP1xMgt2_Jrz1yunSK3PxeO5PubtC8hcV-NaPjL-TbJvGeL-1wkSR29yyAY1WSPq6qLf2wBHVabH1jyQTuYdNJeihUFprRLZacQBvZTT9fagaQ_mIOKavrFyUYXPGtO2KABeHEZmjDan_tte1cBm7qrFekE7lZs7MQQUu3-fN1Wm2ij2KaUkMJcgrUlTQbGbFpusm0U5DSsC3Qj18wqKBdCJGCkhMDuHSgQeK7eDHlfft8fJ44azmT_R7AAR4LdosKOvF88AOtB5q9cRS-NyrbxgENo7G4-UDGXNML3bYxUcMi8sp0lceMR8zbe8ienuK9CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گویا دیشب تندرو ها داشتن بر علیه تیم مذاکره‌کننده شعار«مذاکره با دشمن، خیانت است به میهن» میدادن که مهدی رسولی مداح حکومتی صداشون رو قطع میکنه و میگه بگید«حیدر،حیدر».
این حرکتش باعث واکنش تندرو ها توی فضای مجازی شده و گرفتن روش
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67730" target="_blank">📅 15:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67729">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LS4BbZDaE5PWHnvnyXH5gFPkNjG958F_qAUu5KYlUcjW_HC3RoEc-FshnWgRiaMEle8u56NdBXyEYE-wTvlpGtTPLexNjbVZf90KEN__XdLk7AjjzO8wLuxSZ1waUJTC9xCDHzuwRPGImFjQOoIwlj3H1cPA5EPE5gqJq91hPlN86HKj5Ij0GoftT2hTPHNjQy1IK0yXhdry0Lq6hYW2gF38MX4Fh9pugcAaakQXLtc-RsFCTrvX8o0j0C1_BK3F3XfOCdlpk_Ky7v6avpComZyDIXmIhuBzB5NszPS78La0zLz5sqTDf1GaOAajHg1G1TNdFGoL31gGpupaMkC0xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فرماندهی مرکزی ایالات متحده(سنتکام):
❌
ادعا: رسانه‌های دولتی ایران ادعا می‌کنند که عبور از تنگه هرمز تنها از طریق مسیرهایی که توسط ایران تعیین شده‌اند، مجاز است.
✅
واقعیت: ایران کنترل تنگه هرمز را در دست ندارد. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از 800 کشتی تجاری و 380 میلیون بشکه نفت خام از طریق این مسیر حیاتی تجاری بین‌المللی کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67729" target="_blank">📅 14:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67728">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GSINzXHWjiXBv9HILfg3vtgiwshkCcL90_R-gn5gS-vQije_M05oDf8vW25PoIQh-CyVJS709L-rusGHbyKOmdeKI3ttAyv8245QQ9LH52NR7DewseTjEf81RP1Qw3TbVMMR1uLlpwT0QEBn2SgqXDXhtocFQVPvOQ1exNWiNc7IbpeE0OnJCGjVJJgRnGKcRONjyhQD_5DB-0zgI_X19Exwe7cMlBM0_BdIC7OKZU4wE6Wr2BP62ZsAaU_3ZHR9-eZj4HqVOFeIUNDAnZB6yrdVky7pr3dNNRDHXO9I4j3_r96yhrhx08u01a51JazoueI4-MVfMwdnbW7n1LffDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام سازمان سنجش، رسما و شرعا امتحانات دانش آموزا، بدون هیچگونه تغییری و طبق برنامه، از ۲۱ تیر ماه آغاز میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67728" target="_blank">📅 14:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67727">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=MPL8vefYCEQbZ2Swx1BtSvEiVyaEAMxeyTip0G2WekbNWw5suAkGkL9RfQeWxokZY750OCsfFE2FfKVZr3462mnzOjHePUI4O42v76Yaxs8QwAD1HgM6dei50lyUUGrhyevy6S_wsB8E-MWX6qO0_LlS75iimThMyp4uSWpnBYQemSaQFIjmgL0hxBS2yEkzbAHXoiKkp5i0bZP5jhjstk_eSpmKJbVwWP8m4zItzYWa_mDIQNJ5u_4AoNwYv2UfjFdOq3Ql56gD3VlHrLm7Hi5YsCj-LfoT5w5fHfSCdfZOM0rk81brEdUYYF_6FNVPGYdTPUsaUxE_oHD2jQ2hfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=MPL8vefYCEQbZ2Swx1BtSvEiVyaEAMxeyTip0G2WekbNWw5suAkGkL9RfQeWxokZY750OCsfFE2FfKVZr3462mnzOjHePUI4O42v76Yaxs8QwAD1HgM6dei50lyUUGrhyevy6S_wsB8E-MWX6qO0_LlS75iimThMyp4uSWpnBYQemSaQFIjmgL0hxBS2yEkzbAHXoiKkp5i0bZP5jhjstk_eSpmKJbVwWP8m4zItzYWa_mDIQNJ5u_4AoNwYv2UfjFdOq3Ql56gD3VlHrLm7Hi5YsCj-LfoT5w5fHfSCdfZOM0rk81brEdUYYF_6FNVPGYdTPUsaUxE_oHD2jQ2hfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اکسِ تتلو تو زگیل ابدی با یکی دعواش شد؛
پسره هم وسط برنامه خیلی جدی بهش گفت "
برو بابا یه ملت روت شاشیدن
..."
+ ستاره همون دختریه که تتلو تو ترکیه روش شاشید!
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67727" target="_blank">📅 13:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67726">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIUaMabdmfcIw2yM88bB74Bs7u_0BGsD7ZUg0w7njFlEm_mEIlq7uuj0ZI1xTouB3ZB3Kpo9bnATUKBOheoRAz5HQuFlB9s1t1TZgAM4Wrqpf-_tV8RRcVZsRZTBMpNhq6xMFnEFXKmgwYQvw--IcSJLjC-9Xi5F78gtSui3rPtY-pLDDNZ8nI9e4oCJSaFmCFcgMH8vp0nzv9ji9TDWMhloRBbMbrsuv7WlDdaz64KRntChQf8x62VzdJiBS1zgLXIUhotorVKA2NSmhYqrlecT59S-2JM42J3xUrHrR5315SYhWjjoCYVAMXtEh16VftulVVXS527ePCLmt1YPNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
زیرنویس شبکه خبر:
آزمون‌های نهایی بدون تغییر و براساس برنامه ابلاغی از ۲۱ تیر آغاز می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67726" target="_blank">📅 12:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67725">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/606bce162e.mp4?token=MjMF8fACwKSr7-7xnwtjYzrcMhBATpXruoJrOFEsxvijebijVWyuNKXg8eCOwHFvvGJKf2DM226XS-KB3Nf6g-JMq9OtjhcnOAc1fesDS4N1UCo93RWXevC5rnOL6ea7RHZ9zpiTj7acNpuohf7BpURkcAdTFxwA6SdyJ-6tBbRIpEDSQU5gxKp6LNBgHTOWFSuOQ7IqUVzjuWb0Uh9JfJNys6bgnhQ4jzgB1Dhbkn1OL_69V7KabBBTdbI5ud8x_TgQY_TWET2-STXAR56_ShRiqbQ4JR2uUeIcV0kB5uNtnY6XYmtsSyjPCsSLG0bP46jmxWOs9uZ4WEPWTczjNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/606bce162e.mp4?token=MjMF8fACwKSr7-7xnwtjYzrcMhBATpXruoJrOFEsxvijebijVWyuNKXg8eCOwHFvvGJKf2DM226XS-KB3Nf6g-JMq9OtjhcnOAc1fesDS4N1UCo93RWXevC5rnOL6ea7RHZ9zpiTj7acNpuohf7BpURkcAdTFxwA6SdyJ-6tBbRIpEDSQU5gxKp6LNBgHTOWFSuOQ7IqUVzjuWb0Uh9JfJNys6bgnhQ4jzgB1Dhbkn1OL_69V7KabBBTdbI5ud8x_TgQY_TWET2-STXAR56_ShRiqbQ4JR2uUeIcV0kB5uNtnY6XYmtsSyjPCsSLG0bP46jmxWOs9uZ4WEPWTczjNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آمادگی مجری‌ صداوسیما برای ترور ترامپ؛
نگوزی‌ داداش.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/67725" target="_blank">📅 11:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67724">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
⁉️
تسنیم:
مراسم ترحیم امام مجاهد شهید از سوی رهبر معظم انقلاب اسلامی حضرت ‌آیت‌الله سید مجتبی خامنه‌ای جمعه ۱۹ تیر پس از نماز مغرب و عشاء در شبستان امام خمینی (ره) حرم حضرت معصومه (س) برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67724" target="_blank">📅 10:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67723">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‼️
یه ویدیویی از دعوای دوتا خانواده تو شمال که به صورت گروهی با هم درگیر میشن و همدیگه رو تا سرحد مرگ میزنن وایرال شده؛
حالا فکر می‌کنید دعوا سر چی بود؟
گویا یه خانواده داشتن از خیابون رد می‌شدن و هم‌زمان یه نفر هم با سگش از همون مسیر رد می‌شده.
یکی از افراد اون خانواده که از سگ می‌ترسیده، به سگ طرف مقابل یه لگد می‌زنه، بعدش دعوا انقدر بالا می‌گیره که همه با هم می‌افتن تو رودخونه و اونجا هم به جون هم می‌افتن و به این صورت همو میگیرن زیر چک و لگد :
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/67723" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67722">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
تماشا کنید: پهپادهای اوکراینی شب گذشته به ۱۴ شناور در دریای آزوف حمله کردند، که شامل ۱۲ تانکر، یک کشتی باری و یک یدک‌کش بود.
از جمله اهداف مورد حمله، تانکرهای روسی به نام‌های Chelsi-6، Aura، Sana-1، Ilya Repin، Venus-3 و Penelope، همچنین کشتی Mercury، تانکر Galasar Kamal که پرچم پاناما داشته و تحت تحریم قرار دارد، و یدک‌کش روسی به نام Alfeo به همراه بارج Aphrodite بودند. جزئیات مربوط به پنج شناور دیگر هنوز مشخص نشده است.
در طول ۹۶ ساعت گذشته، پهپادهای اوکراینی به ۳۵ شناوری که به "ناوگان سایه" روسیه مرتبط هستند، حمله کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/67722" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67721">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/67721" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67720">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I8GVgR-PkEaS2n0XV3T9bPfzcI6VgdvWANya3Wp1NhCNepDuAxS3trn2fQtixXr-rLwPl93WpI1WYfEN7GvrFK-cuJWhHetjAyUpzYZnhG3Yu16mqqw1Hhcx6Xrd46R59UTLMYJ4gOM997GNGsjXNw-XGHqU-5tc_UFgasNt_VbUR8fnjYktuJfCHSZ0BpN3wLmS9UsbWcmpxHlTXWnnahrEd3fXp8a6noB6lFoBB9jXsZvWAy3AdDsHX4tyYIItzh58zgCwqE1Sbftnue2bXcR8zvURvRRKrRaK9uaZsr0WXbH2nUQrVSHN8GQSm4pPYh0BqYytSB1F25eOE1zLqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/67720" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67719">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hthJuz1acMYBkql9tKSa6Q2nc3Z3bRuTV2ailtPFe-vpDES6FFeEEKipT69YKuCTQb5nA-rKAVBuoZzOejYSsE5ZLszf5d-9L1mS0dYuy6PvBkEYE19Hcc85XlPlRqaU19F8KLRpe1gPxnMo6m_AXAqsix5mEeSsK4NX-YIfLs3dvCkt-1t6NgNkKyxY7mt7MaQ_eHsSW-0oURnJMOew6tvKqv1rJH114HW-cB1ipMtSjqPsI99Sib7EHei5AykLpSWtAMtLJSCIn4D7Km2DL5eY3dLhOg55psb5cgduFpmXnNiDqDm1R5fayb8QmssZ94wJc0p66V0DGREhj7mswA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وال‌استریت ژورنال:
اسرائیل اخیراً اطلاعاتی را با ایالات متحده به اشتراک گذاشته است که نشان می‌دهد ایران در حال بررسی طرحی جدید برای ترور رئیس‌جمهور دونالد ترامپ، بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/67719" target="_blank">📅 01:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67718">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
صابرین نیوز:
سخنگوی انتظامی استانداری خراسان رضوی اعلام کرد که درگیری مسلحانه‌ای در منطقه "بلوار سرافراز" در شهر مشهد رخ داده است که در نتیجه آن، دو نفر جان خود را از دست دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/67718" target="_blank">📅 00:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67717">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‼️
خبرگزاری فارس:
41تا43میلیون نفر در تشییع جنازه علی خامنه‌ای حضور داشتن
😆
@News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/67717" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67716">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند. افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.  @News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/67716" target="_blank">📅 00:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67714">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Zqh2u2MWL5OdhI1DkvbCyqZmUeummAAD6QfYkd0Y-N6DEYhodQKkVpGCxKoClDfNCRbo3uKyW6kVFYVFi90ckp2yFZ1XgXb1Dv2-Lzb0iZwTqaXhIdMWIakdnxiWwNGVliKmm4upnKjN-R18xEKAN_USAYdONj2e4sHWggVm8-7D3dVBek4UIq8Ds4szrXiBZmuLXyYNDoRpjzP_FM7x8p0_m3_0J1NkIWp22PqiHSuM8VBVhaGvfP1Y_XVtSQkhz3_0lAAKGOesEE2kN2XSu7ev-unSuKweNveEJj4LKXC_D7Rt5ekzyHnOaMEsL2LDtDCapH9ylSnn7qVctLGxzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gcOnc00i4StZlqZmhiE82MhTIxjYnzNenyASWmH6AoiBAOmGBSZSMLgB30am2E_tV8jmjqpcw4NHeSxP8CCsfJf1dmXPwwuC9K1A_Ql-gvcXg1zWdrs8-QKfOZqawSw-WJU0cbWSp8rXQKfXurjA01JCT1uTntiICWVhMAZjVbPWgrvscb_s-qgq7geVbsyZ7v9AAaWoLtcJWcu-MXTZ_QxR6UMfir14iuSqXrr8N4Xy3OCnmOc9PyzVZqBvAHA_SHlD8YU-4oF6yf7PfHACCA17HAZ9lQNNj-bMrJY3kAqDHAzkpTNwMxE5cTShU0b_yuT8vp-yp_SCyE1BBVFSUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚠️
اولین تصاویر از حمله مسلحانه به ایست بازرسی اطراف حرم در حین مراسم علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/news_hut/67714" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67713">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQI8HQ736dwu4YzTIX8MZA8BOW_IPr7nWWC_TB27Rxguu_0Bs6DAgcA48XdGycbonD9tM19z9Z5rGfVqIm6t5_iFdkkEWqI5eMN-Qb6xJHiqb-Izqrcl_OtMCgYxkECGjAwmT6-VuBO_j7AYNrn9Mb2w2rRJGYsPz2rc5DkUeI2ZCPS51DIkEINQxaBCeBYOjV-3vwT0YriEeq16bN_tPXhHOs6obDmp5rzirKaMZBghjzBMWpJYw3x6UMdr7swpD7lGMX6aNtRZUqDOYiZ1gTei1QcO9vQ-Ns4LsLZEylQz4wCgyaXy79uWIw-stoODHDWogvkSWoKvzodLzezV8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند.
افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/67713" target="_blank">📅 00:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67712">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diXekfTSR3Cb3gsk-1BNRrJV8_jvWXaGUYxynfqFutPkv8ksUBwd8kASbCIYNFEsVOSKO1SF8NQK8fdqusQVA8MmKBDmgdIdl0V8pMS6IYqJytzoTOC9QMtK09cupTljl5h10SwVMwGysPu_qfcEdTNMlk1jDhpn3JZjNggZ-j1FYjvz8T7TeeeAJjUPYqGl7oWh8GxDskj4NqNFWuqbB1bzFsTZgC8A7frXtYqVz9d6iGMvioHBWp2-BijI0_xtAkULGdVA97r-9eH8aAzInZQoWesF5TcQvSTWNlrb63cks_9hiIzLIuV5pf8Y83ro_llnfKIpOB3NqdP9sNPIFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.  @News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/67712" target="_blank">📅 00:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67711">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.
@News_Hut</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/67711" target="_blank">📅 00:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67710">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
❌
گزارش های تایید نشده از شنیده شدن صدای تیراندازی اطراف حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/news_hut/67710" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67709">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=Ebq4Jf05oI-WFhtAskRiP85VR_xkgruJwDbFhgor-hPFcdfI76Xowc-FWRxrFhsuHLUeB3MRURcqbv76HC4VMHnNcfbR2aFqV7-gpTisU7Pr7gerVP5ej_lICacqSfLCJ3ZMxCO0zfSpzsdRFZy3O5wFXZETom9qdeoUOUBwVlPQT9OsuVmY9lHPuo_mbuAAScdafutpWa-jJMkP5nkh1BonGprg1SbgkF3hit_QdqqN-XbOoiDMVigfhaEtU52YwyMVL14Ndm9Wk9b-22AxapqOF3AbgCgwbm4_fhwp_5_A2xrzb0gb5RwmU3OKJK2mySDpyO81tjn_NgszjXCmRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=Ebq4Jf05oI-WFhtAskRiP85VR_xkgruJwDbFhgor-hPFcdfI76Xowc-FWRxrFhsuHLUeB3MRURcqbv76HC4VMHnNcfbR2aFqV7-gpTisU7Pr7gerVP5ej_lICacqSfLCJ3ZMxCO0zfSpzsdRFZy3O5wFXZETom9qdeoUOUBwVlPQT9OsuVmY9lHPuo_mbuAAScdafutpWa-jJMkP5nkh1BonGprg1SbgkF3hit_QdqqN-XbOoiDMVigfhaEtU52YwyMVL14Ndm9Wk9b-22AxapqOF3AbgCgwbm4_fhwp_5_A2xrzb0gb5RwmU3OKJK2mySDpyO81tjn_NgszjXCmRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امشب تو مراسم تشییع تو مشهد؛
یه مرده داشت شعار میداد (به احتمال زیاد علیه توافق و سازشگرها) که یکی اومد بالاسرش و رسما دهنش رو بست!
@News_Hut</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/news_hut/67709" target="_blank">📅 23:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67707">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
خبرگزاری ایرنا:
یه پایگاه نظامی تو حومه شهر بوشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/67707" target="_blank">📅 23:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67706">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvbulXdp1amR37b0viV7-U3QZQ2MtrvHDMskIl0HyY-9Eg_UAzpxYDFDVHEEG8YfhnWgg9Hv6taTKq7Cn3lnBoOFcRcViYP1poDo84T8y1eHO0OUH6jERjwSZXj_Zd9WaVwqlHAcXiHfP3wdPkjcuPKQ-zNmb9dUZSVHyZlzIdqygbNMgVCtfuQDnzdcFeAPysnniCLnhamC2wyUifE1w_8Qwiu6acfGiNLN2f3RTwiTqdDZdKGouHFQRzoQxa10UhaWsqB_fQdF4pKpa3lmKMe6hMbFg4bPVoBQ1luFbcWamx53MRpMky_gfZVDYguEh_6QClM3wo5tXdC-qy7LWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون درخواست زیاد بود دایرکت رو خالی کردم تو ربات ۳ تا پک شد، کلیک کنید
💦
😁
🔞
🔗
دانلود پک اول
🔞
🔗
دانلود پک دوم
🔞
🔗
دانلود پک سوم  @News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/67706" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67705">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خب دیگه بسه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/67705" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67704">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1OTsxLhZR56U4ZQPhII7ByljNYLrLZ2ZC5av-yZBSXv2rnI4Fzw0QgvgwDYyAuA46JZ4JbMabmRKTsPSLoUh7V68CtTte4VtqbNsGOL1AXWtMv03sK_x7PmWMvql8rC3VWFIJB070vRxSjpN24C_6KN7pct7KN5McrwhvF7rxIUhfpgf5fDgJhNJxRLNGK10GfBWgVD-1ZANmMhcJ0FrMJ428Dls77gqLkx9WYr1bftU_hSUlQ5wof6yGguavUDFWhiyvJqO25wwFurfGD4w5JHk51B8W_soFcj8NVs3yMdcbNixU_o_MCw-Yexw8pSgu4vvJE9fkArdIizWcNN1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به بریم برا دعوا #hjAly‌</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/67704" target="_blank">📅 22:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67703">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCbkskLV33ho3CxS_sz4NkT9VJfrwO44dnO1U-CvP3h34A1_6t7L5BlhZtehX6GTxhjKe-enO4bROQoAzMom09lktDjjyb3Z7enf4BsiZ0-Bsh87prR3ASZquusQzZstjh0O95cZvrNWfR0gMtML1fwB6fyWzhPk_wcU_pninXpjTHrzeQrOcXPiQjQH1atKzw619lvf3zp8DWFFaJ9j9zEe_sMV77n6iRMCGcxObPlZQreoDhQ4sHPFmIrBCmBDXu9okmbAqoVFH30o3QSNGBZ5BdvPGbeSxf0sZbSC5-6kfi4xIcT_ETFYBJtD_v8OAz9_MBs3Ae2vVWjLA9WWDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67703" target="_blank">📅 22:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67702">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67702" target="_blank">📅 22:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67701">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
نایا: ممکنه حملات امشب کار کویت و بحرین باشه  @News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/67701" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67700">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست  @News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/67700" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67699">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/67699" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67698">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8e18_g6NL8cGeeEOEmnj4q06CzEA-DJMoaBo1E4kVEczhipt12UGYweBjW3UM4F0nYjglet3IyH2K7N67AfdCC7RRLsFmLABY-nV0JKJjNaBLTxrn3csedO407CiV3-641OAJNxXT7io--ySDA1ah-BOTrFjmIThnxZ5ei2dMGY8hxFs8cUw7QNTcxdydHkmEJggjXYodpRjGZoE1i4zgDmaL60sY5VrdCK0XoG3sUDSPfUQfFl07DNGY2mNTIOJpIW7Ogqym0y1-v1LUDx28k7g1rFPjMIxS1Cq-gkvaaf9tUjNEHO6aqFKh-4_G-nkBZLBtf7Cwnlv_ns2l7LFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آماده‌سازی قبر علی خامنه‌ای در مشهد
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/67698" target="_blank">📅 22:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67697">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=lTP3wd-AlZ-SKKOBlBBZv2FwSemHiZ24RV3BoVRLLLVxZAcbnHaOhWKIlyESybCwveifE69rQi8JxljuqZeaRKGBWg6PYQLfQ36pCZYtFpjw6-Gk29mK1SgBUVGPHWrGj64rTJiE1EPA0O-OBMD5JwNuFabhYuJ282EIqPMcpjOk3u5Govr3ktkuW_hVAzb7Ztb8Uycdj5osiOdYk1n5OoPlauVW-CmeyaI0J8iNho81Z-QI6gXSuJ6Gmnu5Z93oskOWxmGWo3wgg6YNYp_lF1yqNeo_Se4BT2NqcyTTzZyM2bdhFqL23550jpD5gh2CPEjOS2z4P2hdDQZqfUDwUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=lTP3wd-AlZ-SKKOBlBBZv2FwSemHiZ24RV3BoVRLLLVxZAcbnHaOhWKIlyESybCwveifE69rQi8JxljuqZeaRKGBWg6PYQLfQ36pCZYtFpjw6-Gk29mK1SgBUVGPHWrGj64rTJiE1EPA0O-OBMD5JwNuFabhYuJ282EIqPMcpjOk3u5Govr3ktkuW_hVAzb7Ztb8Uycdj5osiOdYk1n5OoPlauVW-CmeyaI0J8iNho81Z-QI6gXSuJ6Gmnu5Z93oskOWxmGWo3wgg6YNYp_lF1yqNeo_Se4BT2NqcyTTzZyM2bdhFqL23550jpD5gh2CPEjOS2z4P2hdDQZqfUDwUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‏
حمله سنگین آمریکا به چابهار/ صابرین نیوز
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67697" target="_blank">📅 22:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67696">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67696" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67695">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=B1BF777Mja2sBGSXF0oTsjdIcspZPoSUewcZRL2HWwAFAqY-j9S7kszDSTTvYqrzpWhS9KRL4VBCCWycdasYo9HfozzCsPbyyikQyccb9UJHYVo1NRbEMZtIrjli7D1LofaKlsa_iv5F1hCkl5x2pN78zxFPT0KtNh7d_lAsB7k6mc89uPC1kqr0r4yMXSwPC5-UJLNatlJjaMX2LlasuFOP_7BPKR5pl6RfpcYwYgbUfQAVsB3iks3GXCtNSAxGGBQvYpuZBHhupC4zfW0xUIHfp1j5xZ4Q6pE5iudY92BwkW9B-LB9fNdFoaTyajf6v7gzd8Y6BeV3W3RzqDU16A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=B1BF777Mja2sBGSXF0oTsjdIcspZPoSUewcZRL2HWwAFAqY-j9S7kszDSTTvYqrzpWhS9KRL4VBCCWycdasYo9HfozzCsPbyyikQyccb9UJHYVo1NRbEMZtIrjli7D1LofaKlsa_iv5F1hCkl5x2pN78zxFPT0KtNh7d_lAsB7k6mc89uPC1kqr0r4yMXSwPC5-UJLNatlJjaMX2LlasuFOP_7BPKR5pl6RfpcYwYgbUfQAVsB3iks3GXCtNSAxGGBQvYpuZBHhupC4zfW0xUIHfp1j5xZ4Q6pE5iudY92BwkW9B-LB9fNdFoaTyajf6v7gzd8Y6BeV3W3RzqDU16A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
مصطفی خامنه‌ای در شهر مشهد بر جنازه پدرش نماز خواند
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/67695" target="_blank">📅 21:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67694">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=EcZ7RLH_xDe1AWYHI1AWHozgA-rorjLxrZgTQFFdCEaqGdDZw73AeZp9xnc1jtQNGTVeqmQ5d_Y4ytS68fRhlOI7KBhU7zoyj68PV8k2WzLSFOuGoYryjHbDJLUqtUGVJgerFSgYHOaWlI8tfq-KIblQwtVl1kkn4Y1bkxXgvTbMY3URlC2aDoQ4IFRMmjOyGQyJRbXxF6VeLdN2k-JVshcB_emknr3I7O8bpq227GcRmFA4j-6LWz47QeQeNdIP0xi8uJ8szFZKGBKXSGKFMJQ4W30ANJDYXYXZBeX_JLFdVTrjquJFQjLrMcv81aPxeVEWPGAlbknbSDszTiQUzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=EcZ7RLH_xDe1AWYHI1AWHozgA-rorjLxrZgTQFFdCEaqGdDZw73AeZp9xnc1jtQNGTVeqmQ5d_Y4ytS68fRhlOI7KBhU7zoyj68PV8k2WzLSFOuGoYryjHbDJLUqtUGVJgerFSgYHOaWlI8tfq-KIblQwtVl1kkn4Y1bkxXgvTbMY3URlC2aDoQ4IFRMmjOyGQyJRbXxF6VeLdN2k-JVshcB_emknr3I7O8bpq227GcRmFA4j-6LWz47QeQeNdIP0xi8uJ8szFZKGBKXSGKFMJQ4W30ANJDYXYXZBeX_JLFdVTrjquJFQjLrMcv81aPxeVEWPGAlbknbSDszTiQUzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
همزمان با اقامه نماز تشییع در مشهد٫ حملات به جنوب ایران شروع شده است
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67694" target="_blank">📅 21:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67692">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZqePEYvPRmcfQK3IbVTVavbM2-X3uJnY6GBk1p3i56R7IURTJDKVv9jMv1ZfrYqiVVjDvOISOZmgvukjtIRZkiHGfkwCqNEMo5R_Mwgq248LuQDeDDttjq5S4XinIyKtv6R8_WZuzT58ciYMksMDLSCvty6Ae6gu8Vr6MLBtBhfipAS-7JOjL-EWLXoK2nZDpKosoMHlI2_zqUZaUJ7uC76MqeYtr6TOZ4IrFAWqw0ui-Tq_TniZShRdTLJ-zYN-mfIKYETBHCnubfFOh7UGlKcVRB_CrGJ8JViKjZmOFJ-WOJoRe4lokT5WyJC3Gi8gBBCoYKcTxKUmtuQqDhm_tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t7tYyAZ_oeTWREKefC8mMPkMZH-SWeQym86MVvW8Z7RypuGjx1YPAP-4qeJYpfONvCjfbPRdDz6223sgjpYSezIDLAazz0t8Vabwl_ruvyqloGMj7lXWzqgFyJ3kuQjj8TLpB0gPE8S69_07cbGJVMm75IzOR618OyAKM8IHEkZl7q4lScBEc9e1BpdKDsuRYada7H1Z_9a1Qb3Na0YOGKB1phCACDG5Thpv0G2utkkGrCOybKeSnuLrbZyjv7NptDgNU-uvoCyOR5h7lftNHR2Nx1DQTdKwHsCZjiqzOd0f8bQbn4_BmH4sYrMYllrlXwi3e-sOn9AIxJKBnmYEQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
هواپیماهای آمریکایی که قابلیت سوخت‌گیری در هوا را دارند، از تل‌آویو به سمت عراق پرواز کردند. همچنین، هواپیماهای دیگری که قابلیت سوخت‌گیری در هوا را دارند، همراه با یک هواپیمای هشداردهنده، در حال پرواز بر فراز خلیج فارس بودند. این اتفاق همزمان با صدای انفجارهایی در جنوب رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67692" target="_blank">📅 21:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67691">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
جنوبیارو روزا گرما میزنه
شبا سنتکام
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67691" target="_blank">📅 21:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67690">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67690" target="_blank">📅 21:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67689">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از وقوع انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67689" target="_blank">📅 21:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67688">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67688" target="_blank">📅 21:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67687">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f6598797.mp4?token=kiGyJsujZFtTD-lED5sVXamVbWHvpfl3e94d91-yqmm9RcA6KtmKu1_bHW02JEUzJWduD1FE7fJTLZixiX__hxaAZ5F8Bb6gmDF15Q5jpvDeTWqGyHx7RuBhxXyRU3k_Mz28GsmusPszukJdBbQIIwqXGAhONJBa9_bzX_itr17mZDrDtOFSwGrpVuMYIhuqr6FjpZSgxlfC6kd3W_nVGbIyWeCtLEToo6ezchRifkAaAzt-G6fWh2Y9mFiY98uUrGgBlNYWTcZmFzJuzKkKeyG3RibLrYuqPMnEyf-R3Nvzrcmd7sO_DzMtZaSTsgsZ2CubeyARWDpNG4Z2qR1lxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f6598797.mp4?token=kiGyJsujZFtTD-lED5sVXamVbWHvpfl3e94d91-yqmm9RcA6KtmKu1_bHW02JEUzJWduD1FE7fJTLZixiX__hxaAZ5F8Bb6gmDF15Q5jpvDeTWqGyHx7RuBhxXyRU3k_Mz28GsmusPszukJdBbQIIwqXGAhONJBa9_bzX_itr17mZDrDtOFSwGrpVuMYIhuqr6FjpZSgxlfC6kd3W_nVGbIyWeCtLEToo6ezchRifkAaAzt-G6fWh2Y9mFiY98uUrGgBlNYWTcZmFzJuzKkKeyG3RibLrYuqPMnEyf-R3Nvzrcmd7sO_DzMtZaSTsgsZ2CubeyARWDpNG4Z2qR1lxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به آسمان چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67687" target="_blank">📅 21:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67686">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
‌ کان نیوز :
مقامات ارشد اسرائیل تمایل دارند تا مجوز لازم را از رئیس‌جمهور ترامپ برای از سرگیری حملات اسرائیل علیه ایران دریافت کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67686" target="_blank">📅 21:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67685">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
❌
گزارش هااز وقوع انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67685" target="_blank">📅 21:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67684">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
شاهزاده رضا پهلوی: شش ماه پیش، دقیقاً همین شب‌ها، کل ایران خاموش شد و تو تاریکی فرو رفت. ولی حتی اون تاریکی هم نتونست مردم رو خونه نگه داره
به هم‌میهنانم گفتم آنچه شما در ۱۸ و ۱۹ دی‌ماه آغاز کردید، مسیری بازگشت‌ناپذیره. ما با هم جایگاه شایسته کشورمان در جهان را بازپس خواهیم گرفت، عزت ملی خود را احیا خواهیم کرد و یاد قهرمانان‌مان را با ساختن ایرانی آزاد زنده نگه خواهیم داشت.
اکنون زمان آن است که درنگ کنیم، دوباره نیرو بگیریم، و بار دیگر خود را وقف پیروزی کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67684" target="_blank">📅 21:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67683">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=bFpa2EP4BleukpJDMVe0YearqDGWnBkfbGwJ5SyswxGNol81hNfNFRvXRoX2nWyPXlIPDpyN43ISO5yfPszQkRFy6IaE2m32PcDPQcvUGMkFva3vnBSsQFz3nolnoVY7jiL-dtwATcEJqrQ0dPON2sbl4E9_k_bmVgIdNKbQZwXR6cRvAN8dk65lSLetfbulK8bpSLS1XO1Lt-RA-3xDlPweEZelNqmQq6-9RYmYr4RDTM-QOcqalThFpbFllKqcZL2A7Lm3uEXobyZQHBi3jYqlV8CwLF5gpu9h2JEtDngTRCs47-zXV845jq-WXLQzQa7MgE2ua8hwjj3cl3R33w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=bFpa2EP4BleukpJDMVe0YearqDGWnBkfbGwJ5SyswxGNol81hNfNFRvXRoX2nWyPXlIPDpyN43ISO5yfPszQkRFy6IaE2m32PcDPQcvUGMkFva3vnBSsQFz3nolnoVY7jiL-dtwATcEJqrQ0dPON2sbl4E9_k_bmVgIdNKbQZwXR6cRvAN8dk65lSLetfbulK8bpSLS1XO1Lt-RA-3xDlPweEZelNqmQq6-9RYmYr4RDTM-QOcqalThFpbFllKqcZL2A7Lm3uEXobyZQHBi3jYqlV8CwLF5gpu9h2JEtDngTRCs47-zXV845jq-WXLQzQa7MgE2ua8hwjj3cl3R33w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر اسرائیل، نتانیاهو، درباره ایران:
ما به ایران آسیب زده‌ایم و این تهدید هسته‌ای را از بین برده‌ایم.
این مثل این است که سرطان را از بدن خودتان خارج می‌کنید. اگر سرطان را خارج نکنید، خواهید مرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67683" target="_blank">📅 21:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67682">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8WL4hv9y77LhlLZKcnmcL0RSS4GC_xu8OB6k8YHSavOknPeI5Ku7upqIhRfJa0mMbwWQNzHlaHf4wtobuU1NLMy_Fc88T7T3OI7eG7XVm9Hma1Zau8Gnqce1FNq2vWauoJpdiVmkaqE9af7_TcamGUqFMpNwYSahFeL0ZCegvyVUNOmRt18X2i0Sx15oKBEd9hdr0aXL3w7l7Fsthg-lTg4k1_7gXOD0IsvOFcN-kELajeqD7MtjpxQr0Q60apioDlvo8XrI5tBxyEjs5tXJq9cwVfkPKvLYGOvabQlW4M1PMD73kkyw6rPjPei6gNhj6faKXm9pX_0fxr9bRBlpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو، درباره ایران:
خاورمیانه در سال گذشته شاهد فعالیت‌های بی‌سابقه‌ای بوده است، به ویژه دو عملیات موفقیت‌آمیزی که ما علیه ایران آغاز کردیم.
اگر ما اقدام نمی‌کردیم، ایران به سلاح‌های هسته‌ای مجهز می‌شد.
رژیم تروریستی ایران ضربه سختی خورده است و سیاست ما کاملاً روشن است: چه توافقی وجود داشته باشد و چه نداشته باشد، ایران به سلاح‌های هسته‌ای دست نخواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67682" target="_blank">📅 20:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67681">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6Fl70bfJm3UohueF4_2CrYnrILJO5z8eo8iYK6Ai2wuozVCdrRBnJKDREg0HRwZvNkDTBc9Gi3pzCBZnsGcwl4UPBs0H4JuB8cyFwaidKNqqNi2XZqs_bAhHSNTSqrjrzYsIwRF-L-nQIW9v4VJdDlCY9qovECMbC1lAFPs6yspLlSvrUpc6MhdR2HI83GMm0BSfkI5tf39v2GRwscXxBuEc_HSMZ5Z3TwoQd8yq6mcOgZesz1JBZvX6wNW8TtrEIurdInvk9Um-t4R2Ddcyk_cHhF18rxeiNM_enay9ywZ5MZUZ8jqHLFhTkwssftbV_XYtPEFOvCzRZgSSTM2eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید به نقل از مقام آمریکایی:
این تشدید تنش‌ها می‌تواند یک یا دو روز، یک هفته یا یک ماه طول بکشد، بسته به اینکه آیا ایران به حملات خود علیه کشتی‌ها در تنگه هرمز ادامه می‌دهد یا خیر
"ما قصد داریم آن‌ها را کمی تحت فشار قرار دهیم تا متوجه شوند که ما شوخی نمی‌کنیم."
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67681" target="_blank">📅 19:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67680">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDQCBG2R2aTfPRm3UOZSNxOcu0VVcajM1mMQr9S8pjwZE4PllcIKJXfFMcSJlLGmAUE59Jm4hA2yGE-reIi7FsTxtOIgZoPRvGr35vNRiYKJQ772J3HApg-fOJVpTJc58kmvs1pnLjribh_bya20Ta64G1_QTPY4UDMZ6mx8ogEbGfy4-O_9io5p9iFXx2D6nxczr73eEKLrKvOhUo9nN1IKHeORexQEPh1ID1_1CjVYI5r__gpHa9V8Xh3Ba62awvapTsnzqA_akwPKM5ldb94VKkAUxictv6XC6SdOpSoS-FacTF1z08kNPbEkIiAMgbsf6IQYeN9NsK2slyUvkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇮🇱
کانال 14 اسرائیل :
🏴
علی خامنه‌ای حدود 600 میلیارد دلار ثروت داشت؛
رهبر سابق ایران، علی خامنه‌ای، در حالی که تظاهر می‌کرد مثل فقرا زندگی میکنه، املاکی تو ترکیه، کوبا، مکزیک، ونزوئلا، سوریه، دبی، بریتانیا، روسیه، عراق، ارمنستان و صربستان داشت. همچنین مالک چندین هتل تو اسپانیا بود.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67680" target="_blank">📅 18:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67679">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bd409d64e.mp4?token=XroF8TTk1QlCD1OZLUeDMOkVdBd6ah0zzs90lQX_bliN6_eQ6VeCLHpxXsbCthuYbn0j7CG8qxetgYSrd8kliIEq_tG89JKTzL0urPvvnY6cy3sYaAD8p3suO8GCee87YMso2c7rWcj-QXUsWTAgCUdbCi06HcY_NJDh1lL8AlZu7QpT4s5VEGOHEPYCILBEPWNe8byYxIgHEcye1EUleTPW1DyHKc5ScQCW5WiNHxcVHBPXI7S0ZmlzM176ysDtXf566-feP4_M80l2WPCDhriuOgJrpXRZoU0c7jED8HO8Aiz_y3Uc4gNQwwP2QNW_8cN9vF00BQSlJms8M1VZPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bd409d64e.mp4?token=XroF8TTk1QlCD1OZLUeDMOkVdBd6ah0zzs90lQX_bliN6_eQ6VeCLHpxXsbCthuYbn0j7CG8qxetgYSrd8kliIEq_tG89JKTzL0urPvvnY6cy3sYaAD8p3suO8GCee87YMso2c7rWcj-QXUsWTAgCUdbCi06HcY_NJDh1lL8AlZu7QpT4s5VEGOHEPYCILBEPWNe8byYxIgHEcye1EUleTPW1DyHKc5ScQCW5WiNHxcVHBPXI7S0ZmlzM176ysDtXf566-feP4_M80l2WPCDhriuOgJrpXRZoU0c7jED8HO8Aiz_y3Uc4gNQwwP2QNW_8cN9vF00BQSlJms8M1VZPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
علی خامنه‌ای در حسینیه امام خمینی، پیش از بمباران توسط آمریکا و اسرائیل:
آمریکا هیچ غلطی نمی‌تواند بکند (23 اردیبهشت 1393)
اسرائیل هیچ غلطی نمی‌تواند بکند (18 خرداد 1395)
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67679" target="_blank">📅 18:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67678">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/277d837de0.mp4?token=hPmI7VkPpl7X80Hpd8qTdtqVMxPpMZhglg-GvoSsqPRCflqDh1uG6tZsoO9Ry5NrqJqkR_tld9aSBWIIzKVwo8JCNvJWkQ3zDgFMg4mVkuSL6D1vMbXHX8Dl37m7HEELIJYIMLKS20hBBEG4jSIb6HJhGVtjm2lETUdGP5981mTyhDjVK8jbo2MlK_ROMKLXPG_38LQLBSMhEr0arSbBvUHxeZVrHwTMZyx3L2QVry99J892sEvXXbSwezmatvDSG6ng3VwIuGGTke4uQrdmt19Z2aHqMrOmCSIg5WXIngdM-qjsgKk81zeTwBeYswyuUoUlO3IVxlyj0KjgfoXs7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/277d837de0.mp4?token=hPmI7VkPpl7X80Hpd8qTdtqVMxPpMZhglg-GvoSsqPRCflqDh1uG6tZsoO9Ry5NrqJqkR_tld9aSBWIIzKVwo8JCNvJWkQ3zDgFMg4mVkuSL6D1vMbXHX8Dl37m7HEELIJYIMLKS20hBBEG4jSIb6HJhGVtjm2lETUdGP5981mTyhDjVK8jbo2MlK_ROMKLXPG_38LQLBSMhEr0arSbBvUHxeZVrHwTMZyx3L2QVry99J892sEvXXbSwezmatvDSG6ng3VwIuGGTke4uQrdmt19Z2aHqMrOmCSIg5WXIngdM-qjsgKk81zeTwBeYswyuUoUlO3IVxlyj0KjgfoXs7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دیده شده در آذربایجان غربی.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67678" target="_blank">📅 17:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67677">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54718627b7.mp4?token=jakC6h5W2NlPNaA4rxuNENFKKn6VqN1EwXs7ABZROFSdQwZV5Gk1g_9CA8HRhM43riwUpKvYl9_j3kD4r5TWf384bJSNsj3x0vM09izXhQox9ZVfMKfcz0duvluJ4NBVK1VhfVFJsGS4TFKZmdSil1zf203IjRnuHi-erQsEnyqIVt11uFgoI0ht67UWgiqYsrL6lpnYA6GNTkFB7CcO5yVq9_4W9DAo5zAO49e0dq-DTbU9Bd4Vje7EnZX_k6u9KZ3ggiISBAMpCc1b1fAToDy7UKp7B47vQerSwzIhrz7rgoV0NqMHQn0NhsUKRcosFvZ5HkC5eEwjZlrtcsvwOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54718627b7.mp4?token=jakC6h5W2NlPNaA4rxuNENFKKn6VqN1EwXs7ABZROFSdQwZV5Gk1g_9CA8HRhM43riwUpKvYl9_j3kD4r5TWf384bJSNsj3x0vM09izXhQox9ZVfMKfcz0duvluJ4NBVK1VhfVFJsGS4TFKZmdSil1zf203IjRnuHi-erQsEnyqIVt11uFgoI0ht67UWgiqYsrL6lpnYA6GNTkFB7CcO5yVq9_4W9DAo5zAO49e0dq-DTbU9Bd4Vje7EnZX_k6u9KZ3ggiISBAMpCc1b1fAToDy7UKp7B47vQerSwzIhrz7rgoV0NqMHQn0NhsUKRcosFvZ5HkC5eEwjZlrtcsvwOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدئو جدید از حملات سنگین دیشب آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67677" target="_blank">📅 17:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67676">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑬𝑵𝑨𝒀𝑳</strong></div>
<div class="tg-text">دختر خانومای عزیز در این شرایط باید ترمز بگیرید که ایشون فکر کنن ترسیدید بعدش گاز بدید بیاید اینه بغل ایشون رو با مشت بشکنید
اگرم امکان خراب شدن ناخوناتون وجود داره سعی کنید با پا بشکونید
بعدش تلاش کنید فرار کنید اگرم نمیتونین یه اسپری فلفل بزارید داخل کیفتون بزنید بغل پیاده شد خواست دعوا کنه بزنین نوش جان کنه بعدش راحت برید</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67676" target="_blank">📅 16:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67675">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03400665ec.mp4?token=ilv-2qColnMb2RclkvsLNd8okddq1v9Yrc9ETBVtVmXJJEHHexX9KwnABb7tD-zF6K-24Qfyfpjg5OD8bjK55eqGUPhKmHtFI2qj0QTEZCqj7wDfp-05L7sMNA23qWgoCBtOH46E-HMZWUYtYubc7_IXHliDpS5INHnYrxO4R2Vnlmc8wFGVmUUhhjcUe54L1lTXRseauYuxWx6HZeKc2RTDGvy-_WcqgzDIC1n0GYNhWw5hRQpRkkBbo9MWwH9E11TbvJloQGqN-V8v2R8XpWtmr35jOKThhwWruNH8ospkfpYUuwJdTSe1-fer-w7I32gE3_MkbZtSL544rvqhUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03400665ec.mp4?token=ilv-2qColnMb2RclkvsLNd8okddq1v9Yrc9ETBVtVmXJJEHHexX9KwnABb7tD-zF6K-24Qfyfpjg5OD8bjK55eqGUPhKmHtFI2qj0QTEZCqj7wDfp-05L7sMNA23qWgoCBtOH46E-HMZWUYtYubc7_IXHliDpS5INHnYrxO4R2Vnlmc8wFGVmUUhhjcUe54L1lTXRseauYuxWx6HZeKc2RTDGvy-_WcqgzDIC1n0GYNhWw5hRQpRkkBbo9MWwH9E11TbvJloQGqN-V8v2R8XpWtmr35jOKThhwWruNH8ospkfpYUuwJdTSe1-fer-w7I32gE3_MkbZtSL544rvqhUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر داشت از موتور سواریش فیلم می‌گرفت، که یه حرومزاده دلقک این بلا رو سرش آورد!
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67675" target="_blank">📅 16:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67674">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkB3LBMe0R91s3oe0fqIGU7oc7G0C72S8sXOzHdEcrJH1TbOlong7eRmMUPOtsW9l16mViyE1DE6_SlyFgsnJCEtVcQm04fiWJqJBd99VSL4p0HkHODcJv5r8_Yvtt-O5qZvNMSBLxh6u8-hmSYN-BMbCWKoS0AdaxcN30h1ENwcjERlw7sTEAvhB822XmXz4_wdl3aDSyDx2IsjmJzuUB9KifyIcKTzo2uSPHMg2-Hl0bgCvBIZmEJScry-YRBNMXP5RVoKavPUTkPhzUf9-_VpMd1ARUsXebtQYnHgPcLk8paHYJiHT4uiBEIOkgV2rh7N3GkJxNTm-ORK-_9oyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هم اکنون گزارش زنده ترامپ از وضعیت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/67674" target="_blank">📅 15:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67673">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=HArM0mJaL6SuSpQ_mqpE_G5mxM1nra0QCFaBlCrsCsKz-UAwmK04-Hk7U4m7XonqZZ7JBgG9bLRxET3U8FnKtBcCteIk6DlNOBPqvNnNS3b7vucaP3aRFghX6UAFypFA65Tncn58Vafitn6kKpNoN20xJupbrSypSF5G8LFdgpQlgzJ_Qya3egDA8b6EJy8NrFuvJnqIUQKZlcTngJGg83H8w6ln6uTVCzmwGuttSdOAWq-rGHhL0WJmzDd7pnqZqZV45572TW2wQDdAs9AVa5zekGFNKVRIO2mwIjfXAnE0PSaaZYYnP80GhHCkbVuwVjIPhAzlzRZ-aW0kZWtVnIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=HArM0mJaL6SuSpQ_mqpE_G5mxM1nra0QCFaBlCrsCsKz-UAwmK04-Hk7U4m7XonqZZ7JBgG9bLRxET3U8FnKtBcCteIk6DlNOBPqvNnNS3b7vucaP3aRFghX6UAFypFA65Tncn58Vafitn6kKpNoN20xJupbrSypSF5G8LFdgpQlgzJ_Qya3egDA8b6EJy8NrFuvJnqIUQKZlcTngJGg83H8w6ln6uTVCzmwGuttSdOAWq-rGHhL0WJmzDd7pnqZqZV45572TW2wQDdAs9AVa5zekGFNKVRIO2mwIjfXAnE0PSaaZYYnP80GhHCkbVuwVjIPhAzlzRZ-aW0kZWtVnIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
اسکله بنود بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/67673" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67672">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67672" target="_blank">📅 14:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67671">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
فعال شدن آژیر های خطر در پایگاه آمریکایی "ویکتوریا" در نزدیکی فرودگاه بغداد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67671" target="_blank">📅 14:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67669">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HCFnl8FGdXEUocWHTMnzTi7kXsxffuU_f2YC9WOzBwHA1_y8foUU08RKEiKBp6XaVs15xu_4Ztm8G3vn3XvsXQJKq94-yV37sGgDpK5kHnaEx--N4R_HIi6lb3UxU6wu_Ci9o25GKC8P0n0L9jsrn6AegpRSRUQNWGeDHJBxXiEIc8nCcDwJU9qG1PpZ7G7zwtCG-foYzUh101hYLd9SBqQ3p_qUWpXjAeXGmWZaIz7hpTs9w5cjHz-p1YFH61SLtHglRjEZoGo95A2Rxf1OjZQ_82iuvWZZfDS6G01U8mhemqfDxPx6LKf6ybiltUgVfig94O6J_JFHhF7vBYvfWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gnb4DNA6D6p3qgNBrZutL8Eb6gO7byRIJoNxQQ3SZ-0YUUifB_N2BHssuz9oFmKujihqFAzc_a1ptZFQCJIJVXDWQ4Y5nDP7kmeoWbKshcjkoM0s6qOtAes_pSbEId9CxhHOxbwIP4nDp9DA7VQaIfXhAgMVZFYruK32E4sFVh_mue10qFSVCXcp1aDXlij-h7mTNfoaQa9NCtqiX0o7_7Rj2D3Gqer6Z0PLAhAMV6WTZUsmcBjBEbWoyYz5gp3RpruSrObJoOoMBosyC8wiHweM2Tq5fGrbixPec2g6Ignc20hhyjRDmkwnQ3Twh1t_mCKMQp7jjuaHSE5-Y00G_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
اسکله بنود شهرستان عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/67669" target="_blank">📅 14:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67668">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLE0k7wymDu0coZYllyu6rCR3zRzvQ3KWYEKR9sCY6psl_mlA97Fz9CC_kuGoD6FHouoILHx5J3Zl3acfY3R0KHS1Uzi2-phtnAFynAPoDSq3fI-psFDzUIZ47ugmv1SD6Jf8Tn4Q9-qMjhb-_Cfh7DEKBA4IbCCNY3lfwMqyLfbUWfNQkULYHWgrZzyhOKEq766GehbDZ8Cc3CmuMokrnRhNMGE-dYQSA92iRahkgnMhifwUprzGwwgdrtgyU5E5ORsymQIbBeIKLQvs2Y83JtHz1fAFbINPZuZpmEYeLMT3bWC1OInWpX9sWrCf24zi4-YR_9OMrOfektG___mlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67668" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67667">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان  @News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67667" target="_blank">📅 14:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67666">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTvA61GtLvCe7MIsHi5a1NwUV8QyrxOcxW-GY_bpk8zysdfUbbvxQGdLDtlbdPq1HGC207574wTEsIstGHJImVyq0WGI8xBWRrXEVP-CcyN4yyW6aZ1MeiM1eF_BjGzT5E0CyQMho5NEPlzZbDksr4fCTbtPJaZjY-NFHCb2WWcpxBG3UYhVAeDNUJEH_6D-ZhLptD6FAfe2jaGmoq7C-orArFpmglyBirXj9dbc2UseHIeq0auhwOPdGl2bYT4IXXxN1JpaJD0AfYwv0iOza4X3XxgWM0r-dQafT15ppsU7SyUKyXmZkJiZZxM8LQjfOpla-Tjmn2c127XGDMRx0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تانکر ترکرز: ‏
تهران، در انتظار ازسرگیری احتمالی قریب‌الوقوع محاصره دریایی نیروی دریایی آمریکا، در یک شب بیش از ۱۰ میلیون بشکه نفت خام و نفت کوره را بارگیری و ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67666" target="_blank">📅 14:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67665">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67665" target="_blank">📅 14:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67664">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=jvfFS-oUi4Ng-wJjYhUvfowkCgwkoyeuVnaELckXGHiKKn-FCr0JPfkJA9kVMtUxnLPW_ltNsY-OJn4B6zTBY6_iICvFVkBmHw7Rc6Uz0UDSyb8W68Ge9M3MoVQcJVUMT6Cl9vKeqUC5YltOMG_v5FpBgu8fKGi8hAwiGw7rLQXD7F5EkDK42HO1Og25dIBXl8nFFGPbxQJXKk05yqHMsEjqZebLVHGbjG-tmXs7HZQQgmp3Cy0ZIms7DfxPH3N1_NHDem7WDGun7zb6JZCWBlUIF2I5639y7DdJpCsMME6rBuqwUiYFuaf4As3Vs3MgGmQ0t6Vs1TA7i8R3P4dYiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=jvfFS-oUi4Ng-wJjYhUvfowkCgwkoyeuVnaELckXGHiKKn-FCr0JPfkJA9kVMtUxnLPW_ltNsY-OJn4B6zTBY6_iICvFVkBmHw7Rc6Uz0UDSyb8W68Ge9M3MoVQcJVUMT6Cl9vKeqUC5YltOMG_v5FpBgu8fKGi8hAwiGw7rLQXD7F5EkDK42HO1Og25dIBXl8nFFGPbxQJXKk05yqHMsEjqZebLVHGbjG-tmXs7HZQQgmp3Cy0ZIms7DfxPH3N1_NHDem7WDGun7zb6JZCWBlUIF2I5639y7DdJpCsMME6rBuqwUiYFuaf4As3Vs3MgGmQ0t6Vs1TA7i8R3P4dYiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فعال‌سازی سامانه‌های پدافند هوایی در اردن و به صدا درآمدن آژیرهای هشدار.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67664" target="_blank">📅 14:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67663">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67663" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67662">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=J6h5HTnvAoS2Hznj2kF-B__Mx6Wcac6RsQp204HkhAJOFm4ddCspDSBTNNVz_n3NleWSJ0wD3RN5O3h5zCglcy-POwOwLpHRzc0jZNdFjOxXEoTMjBBrUfq9IjZKlNilHlbXn99uYIgTi3oqedPRpP46s_4HnnrDuwhtnAw9tg2l6WEgc9pKZaEGAbWjoVLPC8DIiqRp8RUGJnT6W2roAVq8HPaikNW8b25r79AAqcDyquICoQHbC2XNg4Ouxnq3ujRwv8VrwPXj-BN7nWkG5z_4xG6826KLr9hrohmgJ2nzO1qkAgYnBROL7JjZ_25LxkWdrajT9bC-DtW838t2W36ysONF6d21agMGzxT1poWl9Jmi7GQocLe6cTr5_pxSTVxMvW_wtiPu75rsgDrQwbWwOSY-xNnh8rLVXG8MSvVn8WsMyo12lXKG5r0fYhxz0IeGf05vMsrvLOb8VON51NuLBBRYjlaaZ5ds-rjSBQkUPyV0tH4q-DPJgDG1qnI_2m8dilOyNJYAT-ohaYyRHoLIrqyBxvzCkh5jF_CYKtIvXIEFIjR02Wx1pDak4Tud2B_fKiu0QDZWYZSKM12uEkKHdxUZ7UnicOrXkjMppi1f3FL__ElbF_kn7gbFXpUTJQCkUNsmn-UC_uoLC_I5NM9Ph9L1I_wWPcUJgEmvBWI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=J6h5HTnvAoS2Hznj2kF-B__Mx6Wcac6RsQp204HkhAJOFm4ddCspDSBTNNVz_n3NleWSJ0wD3RN5O3h5zCglcy-POwOwLpHRzc0jZNdFjOxXEoTMjBBrUfq9IjZKlNilHlbXn99uYIgTi3oqedPRpP46s_4HnnrDuwhtnAw9tg2l6WEgc9pKZaEGAbWjoVLPC8DIiqRp8RUGJnT6W2roAVq8HPaikNW8b25r79AAqcDyquICoQHbC2XNg4Ouxnq3ujRwv8VrwPXj-BN7nWkG5z_4xG6826KLr9hrohmgJ2nzO1qkAgYnBROL7JjZ_25LxkWdrajT9bC-DtW838t2W36ysONF6d21agMGzxT1poWl9Jmi7GQocLe6cTr5_pxSTVxMvW_wtiPu75rsgDrQwbWwOSY-xNnh8rLVXG8MSvVn8WsMyo12lXKG5r0fYhxz0IeGf05vMsrvLOb8VON51NuLBBRYjlaaZ5ds-rjSBQkUPyV0tH4q-DPJgDG1qnI_2m8dilOyNJYAT-ohaYyRHoLIrqyBxvzCkh5jF_CYKtIvXIEFIjR02Wx1pDak4Tud2B_fKiu0QDZWYZSKM12uEkKHdxUZ7UnicOrXkjMppi1f3FL__ElbF_kn7gbFXpUTJQCkUNsmn-UC_uoLC_I5NM9Ph9L1I_wWPcUJgEmvBWI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67662" target="_blank">📅 14:18 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
