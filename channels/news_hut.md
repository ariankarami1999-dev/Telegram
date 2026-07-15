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
<img src="https://cdn4.telesco.pe/file/HgkoQVlOyRrj3YgIiyBX1ZAUiF7bDbh8fW_S10At4-li5FNmrdSrgjlxr9heuiCmt-RiJmfAEuC_mJRkXfnL4sIDto9Gpak3xlBY9TSSDwv2vFO9dAKabIqBNsQAr3j7kp5jv_bsWQ3celvuTdUIWti89KTIj4G7HyCTPh21Jx4OP-TLyVWgqoZbfDTXuKUFDVJNCzT_GbA4m9eWSeL7WAxsMoFNw9sEcdYgTwgoZd6UETxmPp2uvIQxBJy5pbw8NjFUJudH_jiwBOdDhfEeHBWMPSWxlkoRHmXWLhrBTPncWLb-TF5dJXjKw2JTDA051HhJJh8RNNGz0eKidst52g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 171K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 23:34:48</div>
<hr>

<div class="tg-post" id="msg-68220">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">برق بعضی از مناطق اهواز قطع شده، خونه ها دارن می‌لرزن
😑
#hjAly‌</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/news_hut/68220" target="_blank">📅 23:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68219">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ
مادرقحبه‌ی هزارپدر
: ایرانیا خیلی دنبال توافقن می‌خوان جلسه بزارن
#hjAly‌</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/news_hut/68219" target="_blank">📅 23:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68218">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
گزارش ممبرا از اهواز:
اهواز قطع برق منطقه احداثی
@News_Hut</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/news_hut/68218" target="_blank">📅 23:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68217">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ممبرا از اهواز گزارش لحظه‌ای می‌دن، حداقل تا الان ۱۲ بار صدای انفجار شدید شنیده شده #hjAly‌</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/news_hut/68217" target="_blank">📅 23:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68216">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ead41427.mp4?token=BXYefYgXFBdFDIZqjlYtTx-7tTU1rKgQktPF2Jh4XL6errEDECK2LgR60Ju3uNZFp53gk0dgoQXICGc2aaF7enSVEe8ZdB-r4sAwsBSB6vTbgm7Cvq1EQyAK5creTCaLmuyX4VmI7jiM0jtdJkZ23RIn8zlwI_sO32JumG6VrbnBN7eSr03QN3GMKoXVTHGDUrH_XfPh3ZzAsnMWJfFjqmP6f6w48tOQM0-FI6qW4-IgE7GfAlmFVP3g749nlAxoUtaLGOOe-nOzmI1XzTVb-ZDnREqnVfd2ijfNVauA_sW0GsHmsnPr_7fz_JAXzTh1Tdmq3pHXG4Exn0KZzWiiEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ead41427.mp4?token=BXYefYgXFBdFDIZqjlYtTx-7tTU1rKgQktPF2Jh4XL6errEDECK2LgR60Ju3uNZFp53gk0dgoQXICGc2aaF7enSVEe8ZdB-r4sAwsBSB6vTbgm7Cvq1EQyAK5creTCaLmuyX4VmI7jiM0jtdJkZ23RIn8zlwI_sO32JumG6VrbnBN7eSr03QN3GMKoXVTHGDUrH_XfPh3ZzAsnMWJfFjqmP6f6w48tOQM0-FI6qW4-IgE7GfAlmFVP3g749nlAxoUtaLGOOe-nOzmI1XzTVb-ZDnREqnVfd2ijfNVauA_sW0GsHmsnPr_7fz_JAXzTh1Tdmq3pHXG4Exn0KZzWiiEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اهواز رو وحشتناک دارن میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/news_hut/68216" target="_blank">📅 23:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68215">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ممبرا از اهواز گزارش لحظه‌ای می‌دن، حداقل تا الان ۱۲ بار صدای انفجار شدید شنیده شده
#hjAly‌</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/news_hut/68215" target="_blank">📅 23:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68214">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
اهواز رو دارن میزنن همچنان
@News_Hut</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/news_hut/68214" target="_blank">📅 22:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68213">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
گزارش ممبرا:
مجدد انفجار در اهواز خیلییی شدید بود.
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/68213" target="_blank">📅 22:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68212">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuNlz9JoFGV16ojlrUBLMih6UUYa-igFsf2CLOyEB_0vmAxxyxrDzfCGpaUIyEhRc98Z_V2TXUWlGqHvyAteLTbrxG7Ue5RwCoXF8vwq_K9O-uooRcjoyfZw7Str2jr7RMUz_W8VTSRGJ1bGcBvbIC1_5R0Yb01y9IbYp5vTkqN5c1rWiWI6qZqrAgaNy6CSuDN7JA8TdzLnJ0urR78s3wVwsagLZlsjjgod3eSYeXb2jG1iWsRqaIlta-ABGjsz9oEQPzlUpbKpjk8FaHACKCeNusiChjp2slPdNSgdW1gVPcHaWtAfREmCBf7SNPoFwA8jVPyPkWbY3ODFo23LEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
ساعت ۳ بعدازظهر به وقت شرقی، نیروهای ایالات متحده امروز موج دوم حملات را علیه ایران آغاز کردند.
این حملات به توانایی‌های نظامی ایران که برای تهدید کشتی‌هایی که آزادانه از تنگه هرمز عبور می‌کنند، استفاده می‌شوند، هدف قرار گرفته‌اند؛ تنگه‌ای بین‌المللی که برای تجارت جهانی حیاتی است.
ارتش ایالات متحده در پی دستور فرمانده کل قوا، ایران را پاسخگو می‌داند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/68212" target="_blank">📅 22:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68211">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/68211" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68210">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
گویا انفجار ها خیلییی شدید بوده
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/68210" target="_blank">📅 22:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68209">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/68209" target="_blank">📅 22:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68208">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c19ec2f58.mp4?token=p6VXJ4-zzrVY-zm0ICLtxTQYSSorhkUWQDi7uGCIvYF_mVi1hJ7ScTzf8yZzu7BB1rH_SO5wRUSzKWWGchHP01YSUMQuC1LD6BAY1JdP8WEzJ4ChFD9NwAFC6vS528b7gu-hdu7jGTHIcFUkr5cZT50_NBIItCXO9x4ZRakji26FYRY0QdOeK9APj72nEunDFvI9p18ZGwdw4R56OmErwYO9BX8mU1Kx9NoiMAxDY7yQUu7LNDvwuXRt783e5JNtCHjbbP-BbGywaXlT4ADBWtHd5oQaVJq_7gUhQP_a1qvsEC19iFs4Snl4igHPUX7rwr7cbSWpfVA68O_yXf1Zbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c19ec2f58.mp4?token=p6VXJ4-zzrVY-zm0ICLtxTQYSSorhkUWQDi7uGCIvYF_mVi1hJ7ScTzf8yZzu7BB1rH_SO5wRUSzKWWGchHP01YSUMQuC1LD6BAY1JdP8WEzJ4ChFD9NwAFC6vS528b7gu-hdu7jGTHIcFUkr5cZT50_NBIItCXO9x4ZRakji26FYRY0QdOeK9APj72nEunDFvI9p18ZGwdw4R56OmErwYO9BX8mU1Kx9NoiMAxDY7yQUu7LNDvwuXRt783e5JNtCHjbbP-BbGywaXlT4ADBWtHd5oQaVJq_7gUhQP_a1qvsEC19iFs4Snl4igHPUX7rwr7cbSWpfVA68O_yXf1Zbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شلیک موشک از کویت
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/68208" target="_blank">📅 22:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68207">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
سه انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/68207" target="_blank">📅 22:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68206">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66f6a0a0f4.mp4?token=TAoOqeFrtmKl9VCFkAxxFR-MgWoUNg_iVwdjp4sEPf50-p9kUXQAn7SzRu9UUCpaTLC1hiHA6U1pCTLRoZI2MqVRegy9jf2ye8g9DVc3A6DemT4UkQAojxdTNnjszqszI4WvRFCoQPpxuZELEXk96XcO2av6FkSsPjE32bukkbw5LIzPFVgfw9HqgVcL_DqrTBiLT7qtv_ohKlzeqHlJUyxz6C179LtllGTleufowSWfuOpQtiNcGT6wDGNxkccyaDb9EDz9A7Ix-kD1XRMEje4TPNGgAxLxTyd5TqOZabRGFyy79UQlXcoUx3uX10AtDc1KspgcVGlxoShB2WAbIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66f6a0a0f4.mp4?token=TAoOqeFrtmKl9VCFkAxxFR-MgWoUNg_iVwdjp4sEPf50-p9kUXQAn7SzRu9UUCpaTLC1hiHA6U1pCTLRoZI2MqVRegy9jf2ye8g9DVc3A6DemT4UkQAojxdTNnjszqszI4WvRFCoQPpxuZELEXk96XcO2av6FkSsPjE32bukkbw5LIzPFVgfw9HqgVcL_DqrTBiLT7qtv_ohKlzeqHlJUyxz6C179LtllGTleufowSWfuOpQtiNcGT6wDGNxkccyaDb9EDz9A7Ix-kD1XRMEje4TPNGgAxLxTyd5TqOZabRGFyy79UQlXcoUx3uX10AtDc1KspgcVGlxoShB2WAbIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از کسی که در برنامه زنده می‌خواست شب‌پره بگیره چه انتظاری داشتید آخه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/68206" target="_blank">📅 22:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68205">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‼️
یه هموطن داشت از محل برخورد موشک ها به چابهار فیلمبرداری میکرد که یهو برج مراقبت دریایی رو زدن
‌
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/68205" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68204">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aw7DupfQUWDkcaODZFm5scztNGLM9ViPDog0In0jD0wLZ6b3O75MuB1i3NJmkSwTbtYOTi3SKcCmz-S408NSB9Xtz5BDnA1dO8IJCYa27mW2v_SwKxXlTSzaUeUoVZxbDM79f5CcMpCyY-KYZCA9vdyd2P7bXLF4jI9yTj_k2jYq4DBVvCeFVhVmKydN-YInqS0Tn8eW6La9HJY2uwCU0pBVdTfmRAb-Bf8Ci_zTw0zK0utVLJcoF3pa-cbKka98eNW9lRYl0t2gWIeHVLJz4ulm_8Jffl3QZmqjvRO4muGkSZ99QCXVmPUs9QFRiScunEFCKkMSNtGI1LvsSLehAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
امور کنسولی وزارت خارجه آمریکا تو ایکس، یه بار دیگه به شهروندانش یادآوری کرد که هشدار سطح 4 برای چند کشور از جمله ایران
🇮🇷
، عراق
🇮🇶
، لبنان
🇱🇧
و یمن
🇾🇪
صادر شده.
+هشدار سطح 4 به این معنیه که آمریکا از شهروندانش میخواد که به دلیل خطرناک بودن اوضاع، به این کشورها اصلا سفر نکنن و یا اگر اونجا هستن فورا ترک کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/68204" target="_blank">📅 21:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68203">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🇺🇸
فاکس نیوز به نقل از ترامپ:
حملات علیه ایران هفته آینده گسترش خواهد یافت، و خاورمیانه خود را برای اتفاقاتی که بعداً رخ خواهد داد، آماده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/68203" target="_blank">📅 21:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68201">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cVSfn_XvlnC_ZtYyf0AtY4WY75nP_VoM63fqFF69x9jcgdVim2fm1r2zMDyv8xKzbEXP-mrf7LjT3NEZ1dMskESAxKo-Su5Li-HBrafy2LRGjtCEkK_mrSr5NXVmo8tiVndss0mr7VZheVEVuO159C5LBlxV97ucpZ2UTG8qK_COnrjnnF0uOMk2qG5yafM5b4hY8PCsud5QPMMkqJoADak4U-JHV-jk-qfazn-T23rpilSE4qEXeHUNNN9tybipK02dfzDl5pC-bsioJ5AnwDQkkEzHRaXvNsNFI3j9-Z54NlMUP3-wFOrOSWTXvT5pgRJegHvlmcWKsvREY9-r4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lLQ08epN-3ZMZVK-vfhBxkbxW9uEDFEE0J7dWi_Bh3T0sDsRKLn0v4ecTqFgLATDeUyGqzHMzYR7iW9JwKdCmmA5nGQohc35U5NDab-K1xCZjCpIA5I9oepAesUXHnEypT4uIMjbIiuyJEkVVUisCvqK6ovsD7dPkQtyRMBaPkZz4nY7eXHaDBla54ivIFyCzX25sKzLvLp5slEYiT6CrubTgkXpx7tzb-jAiYzC95jVDaR6egv3ZXxW59qAepSHbs1K3MVUyHxE4Fvh8oPNxQ3KKnblFIrslHzUP-gmgUPqm4osTyWqg7G8uz_PzrTrY7PpUsArESiOLiJCRAWgOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ترکیب انگلیس و آرژانتین برای بازی امشب
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/68201" target="_blank">📅 21:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68200">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
قالیباف:
همزمان با درگیری‌ها، باید از ابزارهای دیپلماسی و مذاکره نیز استفاده کنیم، به گونه‌ای که منافع ملی را تأمین و تقویت کند.
همانطور که بارها تاکید کرده‌ام، مذاکره در این مرحله به معنای تسلیم یا ارائه امتیازات نیست، بلکه در کنار جنگ، بخشی از استراتژی مقاومت و حفظ منافع ملی است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/68200" target="_blank">📅 21:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68199">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
قالیباف:
برای ما مسجل است که انتقام خون آقای شهیدمان را به ثمر خواهیم نشاند
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/68199" target="_blank">📅 21:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68198">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
محمدباقر قالیباف:
تفاهم‌نامه وقتی معنا دارد که مفادش معتبر و در حال اجرا باشد. اگر ایران از آن سودی نبرد، دلیلی برای پایبندی وجود ندارد. ما بر اساس اصل «چشم در برابر چشم» عمل می‌کنیم و در برابر بدعهدی، متقابلاً واکنش نشان می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/68198" target="_blank">📅 21:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68197">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇷
قراره تا ساعات آینده ممدباقر بیانیه‌ای درباره جنگ و تحولات روز کشور منتشر کنه.  @News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/68197" target="_blank">📅 21:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68196">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dphn2DnH9W25DWJCYXVqqeuuOp-8z-N4u025chL7UR43TpeVo_DOmP--rW4ASSCqhNzLQkvviba9HpWzzqIjgYaLCkSt4g6tyzAdXWa3Kf_tEyUZHbdgWv08Fs4vSJsPN75NSDhDXW5aseN-OatfDI-Qfoq87glsMZb9lCgQG18MLUR6Dbxfl-3wsnptSooBNnsK4m-Hlqr5iFDRChCdOk5xAuf3PCbyTR-MDQpNWjFg1OEZduvMETlxM-aXyuF2PjcpR0KHod6eHa8nQSakogtD6HdBTOMUuEWIRM3yTlyeARWyAULk0aPR3aOfZdwXTkbWHP3BoD4EseZPbTXklA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر شهدای حمله آمریکا به پادگان ارتش در ‎بمپور.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/68196" target="_blank">📅 20:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68195">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bA5Qfs2l6M6qazajegQLIJt8j0RbAslwN8KQpwlQk4-zPlF6wGjQPysp8DWME2Y2jQlS5oOGyCQHivfhdXW0BMlxN458eZ5V0cpb6bB9xssOT_fzoJRWY6RQVfpLg2QnxdztvI1UfLtkKZPNS0LV992F_E_4U3BryETdsvCMWJUh9AjxgUL5Wkt5MKO3dbcx-O6HIzxepZRWouVphGSRJEoETMrjEUWpxiduMyUb6-vM4xmYMNcVXQjnB7PXXQbTZ-MFwT4Js4eIZDJ4yODnNvhfR4yU0Wo92s8Ob56-YnYtE6YbHlgcjlvehvNZn8mvUo4_w96JjD-aYwNpc9K5qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب عادل دو تا اسطوره‌ی تکرار نشدنی رو آورده، فوتبال ۳۶۰ رو از دست ندین،
کص‌خار میثاقی
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/68195" target="_blank">📅 20:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68193">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMreza</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nc3qM4PGSbBuBeFcjvw_8vtDQehcQPbZTUirAJchzp8GdLDzZSKe0vJX3-zCORf891y2EX0170_1L1SsxtDvJEEu8PUK_pI1HLGJmVX_wNO2lwN5LkWeGig3rjSvf4ElS4qf5UheLQZU7RT5fR3Mb_J4DB51rQT9QVoQ4HVfC0DLiref7WxxcJfadMfF-EZrHZciiDYp2aYZflVJvZ86O9AMwbgn2Dl-4y7t39WI89Zx7aRMIKnTlgFBdFg7PzSMjMNbYul4n1UNZz6D3yeRA_8kHAfELI1L9u36Z2_yg4Y4LX2U4GiOrXUjj2q7NxLayhcZ8rIa7wJ8FZmjzVjBGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ectU2xVd7ayyTy-EnoMcUHSb0zxDP1naMmD7M2Jkrmx00l2evBcX8XPqe1pKE020yaTkHAGBSCCGWwzf31gZ4jR4BaxwcWYLRAz1P32LlFZNSUZj9d0KSc-wCX6ZRGtUH8QI8-Kkej4Uz0UQkoNkOfUQew_MytwPoQUrUbUAgyieDFfntomnVRTG9kFYR71dIQrvnzSMkDQr2GqA-bxu8smRZ_s0u2ax35e1keIdsIjd6FzV3lJ8Tu0W8Swcz8lqMu1NvGILxf_twQ24UJJTrYmo_vrONcixjy7rnEYQPCEJi_bhOFz72iwiEA55TTkwS76LszYQPeSVEe7rG6Dj_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Siuuuuuuu
❌
Zhiuuuuuu
✅</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68193" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68192">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e6c5a6cd.mp4?token=T7IpgnlLqIhOkocAfwjGJZchgmWNKDD5gEtqVky0KSQSEuFKP4ipf1prCziIgbQItTLWK_paXXUov6rUH-PawJE0nWKm-bgud9VRPnK0dOxIrpBRoHcBTqhU6hSbm86zxWtxNLbHz2lJoC4X455M3QSzbxzFi7v9FqPk4IOFW0ITkqqtKRbNmskrj2sCmVrC6KzymQ87AnJFKT8F6dXQXzByiaa42Fx3ONSW8MiQVi4FQP4bh8kQZ4InkxcjyHlrvkEB8jzG__fOt2DtynsA_aMhL5LGw5sH38dU3-60291jCt9IiStOW2zIQqZURsGnwWgDbaSwpLdsx9mmNA7YAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e6c5a6cd.mp4?token=T7IpgnlLqIhOkocAfwjGJZchgmWNKDD5gEtqVky0KSQSEuFKP4ipf1prCziIgbQItTLWK_paXXUov6rUH-PawJE0nWKm-bgud9VRPnK0dOxIrpBRoHcBTqhU6hSbm86zxWtxNLbHz2lJoC4X455M3QSzbxzFi7v9FqPk4IOFW0ITkqqtKRbNmskrj2sCmVrC6KzymQ87AnJFKT8F6dXQXzByiaa42Fx3ONSW8MiQVi4FQP4bh8kQZ4InkxcjyHlrvkEB8jzG__fOt2DtynsA_aMhL5LGw5sH38dU3-60291jCt9IiStOW2zIQqZURsGnwWgDbaSwpLdsx9mmNA7YAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا صبح می‌شه به کریستیانو خامنه‌ای خندید ولی کانال زشت می‌شه پس بسه، فک می‌کنه کریس آمریکاییه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68192" target="_blank">📅 20:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68191">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKCjyaZ3tAuicWphURu6cp1IKQDs_OOd_iagHFjVGEh-4iyt_KoOYe1fKE-eS9mEwU61AToO-Jdiwjcl1FNeWY2H4ajCkswOMXRq4KpB4uVYCFAOQZtXZG2NNnrzAcqIoqtGj7cl5G8M3DgGv8dmoJHjGK54ZGIuBwOPI2_fFiZ6PTUNb0IkGDlVoCW0orpw8ansLUO7azQ9ke7lL9DaNDjaX9sdodaocrrYGkU02RRjBPDGB94vesDEsoLTsyRx3vNVaXWi2Vr18YD1m62cwh6GPHp81ysTuKJk6FeDU7mgztPlRYh6Ohx343DADtpmQamK1_COciPuztWWumUYtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستیانو خامنه‌ای کرایه اسنپ نداشت بره سازمان؟
😁
#hjAly‌</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/68191" target="_blank">📅 20:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68190">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرونالدو</strong></div>
<div class="tg-text">اخه من چکارم؟</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/68190" target="_blank">📅 20:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68189">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6P92hhrxQkOYWBEqxjmB-M792Jv6AIidCTHbPaliJGY6XXTSs83EbaNxcVl5fB51gorgEgLwGZVZ3dIPf0UANcz24_XeVC9S5zAAjC1ijXD7BxcnmZ0JHCi1fHRBSdmWoZCC529bC43VBcTvzw18W50PolGFIX6jr6cUvL2VRmkOQ_I9LJ9dCNFFvb9bVg3EAMKK7HqoWfHZq270Kohn18OAf1qyUlKUAUxwbRZLVQaQ-7XzMcg29T55oJRRX2NdfpYo_E1DdZdKWCk31ZtiGpmxcXsrXKGGg8lw5W061_eS7RLLQl8mpcZUzqmHX24-yAxKuwVxQP7ZAV0VNFHEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل بچه‌ شیعه‌ی آخوندپرست
🤯
🤯
🤯
🤯
:  #hjAly‌</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/68189" target="_blank">📅 19:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68188">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b2e5150b.mp4?token=rR1MGP30PYsobcIx_LNS9oBC80l0VhPAg87xqyQuSajQa5ltCfPERYL4Ya_I1VPsS77e-HdVCs2DrtBwoD4bQSruaN8EhhiuTQvbULEWmLMrx31UW-TYfH-ceIbSfFuT_OINL8YuUQ7CXia70VSNBaB54i0emdZvS-Z_infQiXnMCOjbE0f0VjR3bcki9A9uRBmcbShz6Lv4ivbm029i4QN7gg2doyGAMWCc4ZvaXXU3qUxblemcJTASwM2hxJ6nB1nBOttIPXQWblqG0j5EQa3Ywuv9Eb6Fqb4ol6ApKZtj1Fx-uS2XCAMg8sdTti9gbmuPDeRFgNYt8Dg_wceiSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b2e5150b.mp4?token=rR1MGP30PYsobcIx_LNS9oBC80l0VhPAg87xqyQuSajQa5ltCfPERYL4Ya_I1VPsS77e-HdVCs2DrtBwoD4bQSruaN8EhhiuTQvbULEWmLMrx31UW-TYfH-ceIbSfFuT_OINL8YuUQ7CXia70VSNBaB54i0emdZvS-Z_infQiXnMCOjbE0f0VjR3bcki9A9uRBmcbShz6Lv4ivbm029i4QN7gg2doyGAMWCc4ZvaXXU3qUxblemcJTASwM2hxJ6nB1nBOttIPXQWblqG0j5EQa3Ywuv9Eb6Fqb4ol6ApKZtj1Fx-uS2XCAMg8sdTti9gbmuPDeRFgNYt8Dg_wceiSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به یاد سربازان تیپ ۳۸۸ بمپور
💔
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/68188" target="_blank">📅 19:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68187">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پاساز علاءالدین خبری نیست، ویدیو های منتشر شده مربوط به‌ گذشته‌ست
#hjAly‌</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/68187" target="_blank">📅 19:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68186">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nh4N0EBDmiG-JAV0OEq_KfayGBaP06TQvm1SPKRV8MVswxjphf2cXlhMkzeS98X2wUzQ4mahOMbv4jfCrRozSCwGirCMNM4bScfdqUqoUerGFiWfovqFNGbk9bkBMzFbQSHJWYuadqDxWo9BhMngrePb4N-p9l1bfT6paMOHfhu2_bQ-5hbKurWw05w1G0BYok35nviWbMFqsUsthAK57j6L67zDrWo1N8vQExKCDhRs8xe4gUGSwWwGig9wusnPZEPDQ9QmLIOpRnewFUuTctxoIGEBDyUiIgnreL-_OqG2jPPmZ1884uatEf-faAUFaO5vOvO8K7dWd5U8B5YTfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:
❌
ادعا: رسانه‌های دولتی ایران مدعی هستند که نیروهای آمریکایی در تاریخ ۱۴ ژوئیه به یک انبار غیرنظامی گندم در هویزه حمله کرده‌اند. این ادعا نادرست است.
✔️
واقعیت: در تاریخ ۱۴ ژوئیه، نیروهای آمریکایی اهداف نظامی ایران را در بندرعباس، خورموج، اهواز، قشم، تنب، بوشهر و کوه استک هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را تضعیف کنند. در همین حال، ایران غیرنظامیان بی‌گناهی را که از این تنگه عبور می‌کنند و همچنین در کشورهای همسایه حوزه خلیج [فارس] حضور دارند، هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68186" target="_blank">📅 19:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68185">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJoX7c25sQwohtcTZQoTraiexe6a4WQOOhezvZ6YaSZFGc7vgMWpY_IIiTzJM-nqjIPay1Eua7DJiqkAVe5s-1X4dRzSSA7Ly0F7EPtGXjB3ofymnJw4DFj7d8C5DYwY0zw0PIaxlGLWFdZH3kCnREoaBhOgVqMOzQ3yHCiyABcPjdoV7ixDGt6MGGJGhuyh9BqIEiS5-DbzjaUKQ2cjgJkVgSH52Rb4dg40Ezt7HZvfX09pjlSxi4FbARj7Jgwamr0XqiTcBnj3coPExBZgQLVgsuD8UZhX2ugVvy2MnosLGNCMcUZGVmWZNqQ4Pmho58GhPIfznyrX50B4tFQ8Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قراره تا ساعات آینده ممدباقر بیانیه‌ای درباره جنگ و تحولات روز کشور منتشر کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/68185" target="_blank">📅 18:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68184">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQiiFWkztY3GJ4Vb1Cch7uTY2I-bg4hX1COiYatJUyZvzD-KIQwncMhMnXILV3mjlHjq0afaZgHhXWWS4cfe-qw4dl8Gz_Pr765SjjSru803VSwGCnh5aelQQe9vOPR3RKd8N_PAnBEE8yHN3CCHxmBlevEsxqO-WA4OXQ15M9ABp4fC6fh1L177V10GJHurWPX5YPSxPHuyoLpzQXuBczBUF132sLSyMVq8VverZuFpipDog8X7YTT7tXC770rpetyVzw684xAPzIn92LhrxAArRWXJsSxmBAxHfri3S840ZRcw9zt8RtnGw5GJfuvRlQHsdK-2DS3UZa1cC0c9Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
از زمان ازسرگیری محاصره دریایی بنادر ایران در ۱۷ ساعت گذشته، نیروهای آمریکایی مسیر دو کشتی تجاری را که قصد عبور از این محاصره را داشتند، تغییر داده‌اند. ارتش ایالات متحده همچنان هوشیار و آماده است تا از رعایت کامل مقررات اطمینان حاصل کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68184" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68183">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/68183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/68183" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68182">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-G8LGqqbkbNPaSFO5pT_kqnWhWgZPmXlvQFy56FneVMKvfQNETHHtxTTDxOOR0O6UFfYjnemwXVhcBxImmkn-shOrz_g6DRpCyql-uPetpbw4XfaVFt2shjyfy0Zvwn5fMss-9_qnkXrwtd0cAuyzSwsGqarE2kjk9Gv4zIdh6FHETmPBZHHh3z8DsWK-DPA6f_s8kwjG4XLQjkODCEXq4QnM58m9ruVTNWK3gYX5wwZ6WW97zU6rd972OnvejtOVZh5E4-RQTvoO3LnpiMpvoq7kZFlYTQ4Akct3pxYr0ndIHFErgJ1n4FeygOygC4crwAzO_sQ9xlU8IEbe9b8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
Stand for Victory |
مجموع کل جایزه  250,000€
🎁
جوایز برتر:
🥈
جای دوم — 33,000€
🥉
جای سوم — 20,000€
4️⃣
جای چهارم — 10,500€
5️⃣
جای پنجم — 8,000€
🏅
جایگاه 6 تا 10 — 4,000€ هر نفر
🎖
تا جایگاه 450 جایزه دریافت می‌کنند
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/68182" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68181">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
انفجار در جزیره هنگام
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/68181" target="_blank">📅 18:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68180">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/415d2aa12e.mp4?token=JBQkU_3vNKltDUHr_RKcsNzVXUJgB9ZpupXYznyT7Yhjdem0X0duegDVwEbl_vDr8KwtHPX5utexDeiQ1PVmm0O0JqBNcA1ItUbP8-nyvxBMttXQ3Q7iUaMNtdxr4e3DEXFKP_utRdvbktaUQM0j6mBSudH0ieFtjg-o3O1WaE0QZEYSK1DcPVcTBF-uWJ7jATSEVu3BXJ51Dh_4DS0ZLurbel-RntGvO0ycL7B4HnMNnwLZWQXe_F9XgssZsJuoUFKad_yLy49psh5TDovTX2njbohF7QYSEZVBe36KpEncPh576zO-KISZ1lYmWqePX9pdBrG2oM9V3G4__6YY6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/415d2aa12e.mp4?token=JBQkU_3vNKltDUHr_RKcsNzVXUJgB9ZpupXYznyT7Yhjdem0X0duegDVwEbl_vDr8KwtHPX5utexDeiQ1PVmm0O0JqBNcA1ItUbP8-nyvxBMttXQ3Q7iUaMNtdxr4e3DEXFKP_utRdvbktaUQM0j6mBSudH0ieFtjg-o3O1WaE0QZEYSK1DcPVcTBF-uWJ7jATSEVu3BXJ51Dh_4DS0ZLurbel-RntGvO0ycL7B4HnMNnwLZWQXe_F9XgssZsJuoUFKad_yLy49psh5TDovTX2njbohF7QYSEZVBe36KpEncPh576zO-KISZ1lYmWqePX9pdBrG2oM9V3G4__6YY6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
منوچهر متکی وزیر خارجه اسبق جمهوری اسلامی کاملا جدی اومده گفته:
باید به پایگاه های آمریکا در منطقه حمله زمینی کنیم و صدتا اسیر بگیریم ازشون و بیاریم ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/68180" target="_blank">📅 18:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68179">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1331c1b8f5.mp4?token=c-uTsU-WPI0tOl5U4RUllpgsQr2xXh3E5t1wrEVpX1xaHoIs74tRJ2pMusrfZKi_q6L0-nSD05ZRawYAbhDOgw9IGwJ4zlZFZ6iDEbM51hsuIl_F2Jkvr91HH96NDAX00aWxcKt2DVjff3HIUDdjNAi6sploGUz9Clt4HVigT5Fyg58jK2ZEngpLk-CbOH2k5qsflUoIfudonz-EMleDl4oB8KhVfMCa_7cqclrLBJSezmt1z_0-kQ0LR1hiD8q-RuIbz53yien37YgVmYkP70pNtp7UVzpUtbHEb1uNSHERmuVewVckrphjFH0drZIFffqeZK3fPFWA8qW2IuPdBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1331c1b8f5.mp4?token=c-uTsU-WPI0tOl5U4RUllpgsQr2xXh3E5t1wrEVpX1xaHoIs74tRJ2pMusrfZKi_q6L0-nSD05ZRawYAbhDOgw9IGwJ4zlZFZ6iDEbM51hsuIl_F2Jkvr91HH96NDAX00aWxcKt2DVjff3HIUDdjNAi6sploGUz9Clt4HVigT5Fyg58jK2ZEngpLk-CbOH2k5qsflUoIfudonz-EMleDl4oB8KhVfMCa_7cqclrLBJSezmt1z_0-kQ0LR1hiD8q-RuIbz53yien37YgVmYkP70pNtp7UVzpUtbHEb1uNSHERmuVewVckrphjFH0drZIFffqeZK3fPFWA8qW2IuPdBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمسخر لهستان و شوروی توسط چپ‌کش اعظم رونالد ریگان فقید:
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68179" target="_blank">📅 17:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68178">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f97b887b.mp4?token=QEjlU5hPZKdBeuXSB8uphi1S1pAWia22Xq6vNQ9mnybI005TmfDJMePda8X4rGDdYBr03SiCl3Ce9JS_sXn_Crnb7zI86pfyeR0CQQRQJf_cOQ6YZuc_X-69cjBs4PaKIP3yHyyj1VCoL5HbxBbKpt4z6PVDx2IJ0_Y7vB9RzTc7qq-5e-voU_T0BMhyrkDAMraRUtPkcymI5kAY5_dNByvzxWD4dvIkL2dP2G8ThQ4G6ugoQn6-KgSS8DEqsfhg5RyBZY1TZ2pjVBIUqLEK1RNyJIZa7c9yejI06lxd39_JH90Ikh645IMy6ymC9J0DPtXAsprbtxrLVRRLWm1Hag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f97b887b.mp4?token=QEjlU5hPZKdBeuXSB8uphi1S1pAWia22Xq6vNQ9mnybI005TmfDJMePda8X4rGDdYBr03SiCl3Ce9JS_sXn_Crnb7zI86pfyeR0CQQRQJf_cOQ6YZuc_X-69cjBs4PaKIP3yHyyj1VCoL5HbxBbKpt4z6PVDx2IJ0_Y7vB9RzTc7qq-5e-voU_T0BMhyrkDAMraRUtPkcymI5kAY5_dNByvzxWD4dvIkL2dP2G8ThQ4G6ugoQn6-KgSS8DEqsfhg5RyBZY1TZ2pjVBIUqLEK1RNyJIZa7c9yejI06lxd39_JH90Ikh645IMy6ymC9J0DPtXAsprbtxrLVRRLWm1Hag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از وایرال‌ترین ویدیو ها در 24ساعت اخیر در توییتر فارسی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68178" target="_blank">📅 17:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68174">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGr28b3BOyvRjmScFM980VhbnIAW3eSj9bt6IlfSFCADLGbmMZgj-GPF3aCZsQUCbieg456rx-dN9-o4vdVeDDzQaYotReO2U9dIwhnRylK1QxJQtZhiXfd3re-VTmOKvZoVpaXMQtnoLSGICHQOj3fxXUG6C_dnw4aPh35Ej4Zs26dDB6zzGmJivN20o0CsUaluzLzGhKEZcrb2ZJvXny9g5Y_2b43qtTpPotTNk6-jaRckgq99ofm5at-SiqjOza-lg7NvEdVTSeTQAtNTQXXa6Uc2yJEZTEJiWWlnYL74bOX_1zMV9njKJnTq5-QWnFB8CGMLx3KNwxy-svmgow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5effcc1b8.mp4?token=hqIQDXTbUBZeB19nl5ojkSZg-6Ep-VmwwtLEN50c7Nw_GtU4oc5SsgkUz5lFA8iOz-Nl8WCvJ70PQ4xmZ6eTdG3_o5YKeMdMQq-tb6x-t4n_0OLj8ntX_LvgDbjmkqBGdOUrGdXOjVR7WS4dz9XD8f0sXLUUdlOiYKcoo1DPm96C4gM-mzx31X7c4gP44ujKOGiyU8yApvK-c7zAEL08igJbEeMnxjiHaApyNjpdEVDEVOaHRWNUQJnzD1IKjnDJmuZz9sAU_9yaheSzhYmiKcKHhTBTBntkW23eBhx_E5ObkvDHCSnyksNdyTRLGyBfD6LAu-JUUU6ANMgRHqtAog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5effcc1b8.mp4?token=hqIQDXTbUBZeB19nl5ojkSZg-6Ep-VmwwtLEN50c7Nw_GtU4oc5SsgkUz5lFA8iOz-Nl8WCvJ70PQ4xmZ6eTdG3_o5YKeMdMQq-tb6x-t4n_0OLj8ntX_LvgDbjmkqBGdOUrGdXOjVR7WS4dz9XD8f0sXLUUdlOiYKcoo1DPm96C4gM-mzx31X7c4gP44ujKOGiyU8yApvK-c7zAEL08igJbEeMnxjiHaApyNjpdEVDEVOaHRWNUQJnzD1IKjnDJmuZz9sAU_9yaheSzhYmiKcKHhTBTBntkW23eBhx_E5ObkvDHCSnyksNdyTRLGyBfD6LAu-JUUU6ANMgRHqtAog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیوی منتشر شده از انفجار در چابهار صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68174" target="_blank">📅 16:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68173">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d7965cf40.mp4?token=umQJ3oXLIshB0RXIP3qTUr8pj43ISNjh0fwl_j6PuKaYp-H5Eu7Xllm_eA34JUNPxrwNaE_XDmAPNuItU04sc9dVkhHg9PnMrEaZ1YECdc5pBr03dB2kTqfibFtSdcAwUUYE6NsKhG0ElCAAH9r7CIXstMMs2ST6JWILtvKZ0S-lvy1Z5HlH78jE2EnowTVTE-KpX4yE-2k8DmZMhQi1fS8WfY7GnwosljfLYCsJ_OQaw_SjJOl3cSCPctOKti9wS33RxFwekx0jv_k25muZf9H9q3mcXCUnUnrktmdEmzJS98fjqq_r6P5WW4M6WrtMFHKzunR2JGSk359-Ca9FkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d7965cf40.mp4?token=umQJ3oXLIshB0RXIP3qTUr8pj43ISNjh0fwl_j6PuKaYp-H5Eu7Xllm_eA34JUNPxrwNaE_XDmAPNuItU04sc9dVkhHg9PnMrEaZ1YECdc5pBr03dB2kTqfibFtSdcAwUUYE6NsKhG0ElCAAH9r7CIXstMMs2ST6JWILtvKZ0S-lvy1Z5HlH78jE2EnowTVTE-KpX4yE-2k8DmZMhQi1fS8WfY7GnwosljfLYCsJ_OQaw_SjJOl3cSCPctOKti9wS33RxFwekx0jv_k25muZf9H9q3mcXCUnUnrktmdEmzJS98fjqq_r6P5WW4M6WrtMFHKzunR2JGSk359-Ca9FkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۷:۳۰ صبح به وقت شرقی روز ۱۵ ژوئیه، دور دیگری از حملات علیه ایران را به انجام رساند.
سنتکام در جریان این موج عملیاتی ۹۰ دقیقه‌ای، با استفاده از مهمات دقیق‌زن، سامانه‌های پدافند ساحلی و همچنین محل‌های نگهداری و سکوهای پرتاب موشک‌های کروز در جزیره تنب بزرگ را هدف قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68173" target="_blank">📅 15:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68172">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e23686eac2.mp4?token=hsyhkiuRfgScz0KTuIVevHcL_wnMqkjj1W5ULD7OWa0Gnplm6rE-Fr9fEKWpLgox501iDUFNbxRlpgTW6Txkg_VyEKWv6937CwK2Tr-N_T-8IaBNfCW7RMicGH4i8jqvJDVUusbW6Nci5iT4MSZHAPeFl31NUGPUe2jXgzxgurDK504Wgon3BTPCmAnaJCtLAfpOC8ll3FjQsXOs3GwC4zgtDWMnEHu3vL7W7-uug3uT9I-GPFEr7aZf_l7P78Zzl3wMVXFSgyIyQIu9P7s50Cx8loqZhd0ZeuPswPT5obv1yICPJ3QupcXywYLjyaSvCJZ6aA4PFh913MUdr-dP-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e23686eac2.mp4?token=hsyhkiuRfgScz0KTuIVevHcL_wnMqkjj1W5ULD7OWa0Gnplm6rE-Fr9fEKWpLgox501iDUFNbxRlpgTW6Txkg_VyEKWv6937CwK2Tr-N_T-8IaBNfCW7RMicGH4i8jqvJDVUusbW6Nci5iT4MSZHAPeFl31NUGPUe2jXgzxgurDK504Wgon3BTPCmAnaJCtLAfpOC8ll3FjQsXOs3GwC4zgtDWMnEHu3vL7W7-uug3uT9I-GPFEr7aZf_l7P78Zzl3wMVXFSgyIyQIu9P7s50Cx8loqZhd0ZeuPswPT5obv1yICPJ3QupcXywYLjyaSvCJZ6aA4PFh913MUdr-dP-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از جنایت ۱۸ و ۱۹ دی ماه؛
تا مدرسه میناب و پادگان بمپور؛
نام‌ها عوض می‌شوند
اما قاتل یکی‌ست:
جمهوری اسلامی؛
حکومتی که برای ماندن؛
ایران را می‌سوزاند
و جوانانش را قربانی می‌کند.
#hjAly‌
@News_Hut
|
@HutNewsPlus</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68172" target="_blank">📅 15:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68171">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YH2YB2xHWxPkLmVM5QmmIqa9C0SUNHL5X9GPnC4_A01lE8ccI5iOqnrfXyoYwjZy0TeAqDUW89PApUftrKvP9iyM6prqZVBa_gULQvvRshlogE7kHVlv6_pC10ztL0efZNKq3V8KI1MJFBM5nI9jCOrlVcu89CtK6w0uZT6LqexBENaWk49SHLzFkLaX-cv4B46jpcs5oPsBLDPS4BvN7n9BBx1kmCQ9TcwgnAwV6s1wDe7lxu4_krXeWNzwoidHvKlGa7K_Pq7twzNmMe73oI83d2l-AfxXF5SnbH9VSUioEQ_Hw6twq0uCWT2yJ7NRqN_mQdaatR0bHQBkvNxyKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری حامد‌لک:
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68171" target="_blank">📅 15:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68170">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpomXNHMu5uRliYHsBVxZfbl87ZUTR9b63lg8JUDf0smgewmpZRd7rGKmvWBwjIjDgHHat3f5YNLPkc0WG6PXDmhgRi7KzR3htuM0h_d1D44EteTqT6Cp6UzZB6f6vBHiFkn3V6JGwcrAbYkzeLI0nomBL9NY2UmnPDdr-FEcfhQEqts2GnJm3DrtpHbYntL8cphTyOwwD5WDmX17Sgsu282N45dXE0AUOrOgjhLbowdAAk95Empyxre16bzjQBjNdCgvGA1Miv_Gb3I2aad_cts67tyYI_45uJuATY1O0ndhYHl4NHGDBlVgt2kFgODaXoccwTp5G_3OQYmh3SrHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
چهارشنبه ۲۴ تیر ۱۴۰۵ جام جهانی ۲۰۲۶ مرحله نیمه‌نهایی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
- انگلیس - آرژانتین
🇦🇷
ساعت ۲۲:۳۰
ورزشگاه؛ مرسدس بنز آتلانتا
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68170" target="_blank">📅 14:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68169">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
پنج انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68169" target="_blank">📅 14:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68168">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">علاوه بر اینکه سوالات یکیه و باید همزمان امتحات گرفته شه، تسنیم اومده گفته فقط نهایی دوازدهمیا تو روز ۲۵ و ۲۷ لغو شده، این درحالیه که دوازدهمیا اصلا ۲۷‌ام امتحان ندارند و یازدهمیا دارن!  باید منتظر واکنش رسمی اموزش و پرورش باشید @News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68168" target="_blank">📅 14:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68167">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mob3k5bTCFsYS5Lw6jMlkYTV6BkVwbphH5EpTBWgk-b4FGqv1okbsDBGonMdia6sbs97Xb3Je-Z3KR6njnPU4D5eVlbtHFY_f0sBAcTmr60mcBiTdfy5_sFa7LMwUl3XgzZKBrchtGcTwUcVV5WpEwAUNnra-MeNM9-0StHsfm8dHOtxTwX7w13A94GZa8Cmvq4NXNF99eBVhySHgz50uPzuUYZGBCr05kd5KDdKyPfHokgy7j14RXjGWccxKChn4JSSoVkjkijq13vDq386TNNvRcZkzYDqI4EwSFsBxrIFdGOU4idXjdJFvlm02rUAbYkhNMMRL4x5vDHBrgYd5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطوری نهایی رو فقط برا چند منطقه لغو کردین، کاش این دو روز کل ایران رو لغو می‌کردین تا فاجعه‌ای دوباره مثل میناب رخ نده... #hjAly‌</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68167" target="_blank">📅 14:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68166">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce063673b4.mp4?token=AH8Lk3CASdrsqQsZSP4c9vbnpi_b36YB_ELZZm7ZSeGaD7Pf4dYr_KbrfUzzMhvT4r3j12-yscGz7R_vhtuB87KVDaW8633vRbZVVSPVqDcWbdM87M2xjtuo2OVpH8ww32bHOh_KvzzysOwjfQBfkeoE3B3m_yKiFaLMVMYkYOgzqGjSRGCamthaXhCN7jN8qE1AV4q3FpMzIFN4sH8byPJznMhu_ZSpGVs8zlkGa9KFEa-BgiICvwQ4QHA6neG3Ha2SPAHZyYC7oDnMHWc_nnoArNFAj5m9Es18I-MSpQ-H4lXLVQ6R8TJiEXbmechIwsPK5SvvDDX2bm5VXkOptg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce063673b4.mp4?token=AH8Lk3CASdrsqQsZSP4c9vbnpi_b36YB_ELZZm7ZSeGaD7Pf4dYr_KbrfUzzMhvT4r3j12-yscGz7R_vhtuB87KVDaW8633vRbZVVSPVqDcWbdM87M2xjtuo2OVpH8ww32bHOh_KvzzysOwjfQBfkeoE3B3m_yKiFaLMVMYkYOgzqGjSRGCamthaXhCN7jN8qE1AV4q3FpMzIFN4sH8byPJznMhu_ZSpGVs8zlkGa9KFEa-BgiICvwQ4QHA6neG3Ha2SPAHZyYC7oDnMHWc_nnoArNFAj5m9Es18I-MSpQ-H4lXLVQ6R8TJiEXbmechIwsPK5SvvDDX2bm5VXkOptg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خسارت وارد شده به یک دکل مخابراتی در بندرعباس پس از حمله آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68166" target="_blank">📅 14:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68165">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
#فوری؛ امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد.  وزارت آموزش و پرورش:  بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68165" target="_blank">📅 14:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68164">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
#فوری
؛ امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد.
وزارت آموزش و پرورش:
بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های تحصیلی پایه دوازدهم در روز پنجشنبه 25 تیر و شنبه 27 تیر لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68164" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68163">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKUCv1rRxOuiz01Kr69uQC2B_B9hJ5VtxSywmaqSEqBUZF-xyiOXBf_-D18jWufYP9cwwC-vVERQjDJXVu2ynwh8oYWxIDpKHlQghCn7IVjP54jqI0Rs6QigEjpQz2q9GDPnBWTQUTkakrpv4OSNoVzadxvTlwC8TaPlSVMC29Hn6gBDuS6mhfYrfxToSyY8OQBG1yYjL6nytRhGD45ad1vg5m_GA3DMi_qUEEI7B313saTGhMvMO45t9fl_r6Sbyj1Tr3ocbSy2tuwlci1L8t7gWWaNyK7noi0vHKI6Ukz4ZBjTPiIJ19zTRtHCB81dcd2CVn-t61RFKIedJhjJHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۶ صبح به وقت شرقی، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) موجی از حملات را علیه ایران آغاز کردند. هدف از این حملات، تضعیف هرچه بیشتر توانمندی‌های نظامی‌ای است که نیروهای ایرانی برای حمله به کشتی‌های تجاری در تنگه هرمز به کار گرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68163" target="_blank">📅 14:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68160">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IhWXKRVbuOP8NmGjFL0kOC8xIp4c7Z2srPkbvv33JxKW7pcmBMKQP4W2ApUDtQllGUdMTpnNPOv6Vw9-nRz4EK7bTGC2Oyk_1-v3Z52Y6QBk689V7rko_1IGSMGKRHxRjcXeOs2Qu_PFv2FT2u8iAa6TasvwnM8IGxeX7Ob5Nz6vmz0gMMFDQMqjZQFoRCFXlzbtN7_HJmLsSTKDZh4Dd76tFCsn8-KAmZLsdoDB4u_fjrNnFk7-gx1Az6F8vRh4NszPUgSHeG4rk_6M0jbObuoS0FNL_3nmSdOdPAIoWMskKgzjS4d68NNffgWZA7-pfuL8jCBA6tWvM-oaoFNelA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jO4LGZi9a3QtCyVCwijkdt2RNz5aRJgWERqYjV7MsfDOYG_KUBdAuo9TtbBjFwkOFbSbJhc4WjAHuTtaR0ZT8VYI4kEZycvdH4uWO6aw_yWfjXw8-9a4XjddhXDwgBaxz_k3KD5psCiJ93OMnIx6h6uroiCGB1VHyxL4uh674R36J6-c9EL-W050ixyCL5D4z8jDdBEGnGHr7CAE3fbE9-xYYy5zgOxPPdLgAg3SzNN2OlxQs-4vmYbHPXGXVZDfpcRt2qXJX1aCX-_vcIzmXhE92ZG5fircSCJXtSYbqkRSDZ8K3580YkC1O9oid-3QA5NYGDOwzmtGsRDAc7P2cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a57f3aee50.mp4?token=MQlMCNAZJh6lI4M_1cJueM-gCmH5kCEjW41KYjEAML01VQaaleMwOyDLkoC8sn5im1Hee_VoH0WJmtfAtVOjm5-63olAEAAB5w7pMCvcIAI37lXvrB2XzI3G5QGIyTjlAhmVFY5ZIKjagEQhM-jGsDdxPDg-tLeYR5OBLrsHCthbB9Wm7XWmQUUQl3_v6abvTk4UGdTn7_5Vb9M1GgndUcSlD3GqUOFM0CNFkFV-fU1YC4sQ-RVEXLzMVsIxh_R485QjvrKoi-PpVEXBFu7IPaFvfQGxui1wmnQjwH-t5hfyDN8odv3q93-c_Lk48r9JDYpTOH3ZM-QwLRdNLCGR3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a57f3aee50.mp4?token=MQlMCNAZJh6lI4M_1cJueM-gCmH5kCEjW41KYjEAML01VQaaleMwOyDLkoC8sn5im1Hee_VoH0WJmtfAtVOjm5-63olAEAAB5w7pMCvcIAI37lXvrB2XzI3G5QGIyTjlAhmVFY5ZIKjagEQhM-jGsDdxPDg-tLeYR5OBLrsHCthbB9Wm7XWmQUUQl3_v6abvTk4UGdTn7_5Vb9M1GgndUcSlD3GqUOFM0CNFkFV-fU1YC4sQ-RVEXLzMVsIxh_R485QjvrKoi-PpVEXBFu7IPaFvfQGxui1wmnQjwH-t5hfyDN8odv3q93-c_Lk48r9JDYpTOH3ZM-QwLRdNLCGR3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68160" target="_blank">📅 13:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68159">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psZNmj1XFI98zGF3IdfYiEPUG5PY1vUFVXJ5hAl56SXXlU7Wv2Tt2ekTNhpsPTTabnLXZhGFbl5PL5nBMq6egJhvTKMq1enE9-ZxSv3_cHWumjGBM_KFXcQadRUTk1pi_6ZOBp7gUyRD8vRqfXAULJ8-H4Wifz6vtbKLE9Ihu_kg5RZ2cIwubeyde7gzNXGEEzWXMCCuNL59azThuQtuBk_ZuQoHfXE2miPRgo2vUN9Z27EdAPOt9lRjzfzcO57nlQereaLITkbZrvcQT-o9SEoh2x_l0DLgP6vb6QkiqsHrBiyoD-6Iw8Y6Qq8GHxBQtnSO-eRngYZldyCOfNPrbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68159" target="_blank">📅 13:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68158">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZpJk8R4FLDNa2O9G0hBOcsFguyyag_OdNBp36YUW9nhJZIzLCQr5sTMT0iDeDa3MB8j70seN9P1fDs7YhNDgrCVkopcuw98E1M151M_RutKGfyyaUQoghFT7-Aqx2hN4WBjCVc5AVEa0zUyDe6nJbccX5umOd2XqmNHkek9EHUg8oK2BNu-mlrRSyWSz18EapTySNPHiDQLHKXaSydEPpsV3k_pZmkJ_8Px7sFKv1u0bZSQDb-fuNEsVDJUanH6huZ-Z9OgCVFn3mAqvTPE546q46qPr1wTgJCG99bHWLlkOKRAJmQi4zM3hhw0kjVdP82LuhOIkt0Qhk35FKeDnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرِ داریوش فرضیایی (عمو پورنگ)، بعد از تحمل یه دوره بیماری، تو سن 90 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68158" target="_blank">📅 13:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68157">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‼️
امریکن گات تلنت یا همون عصر جدید آمریکایی ها
یک شعبده بازی توش انجام شده که حسابی وایرال ‌شده
👀
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68157" target="_blank">📅 12:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68156">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcWim2hI8twcxhQiRQqZkFyj5K81P-xQfcl1SFkFlAJ3Uu8dDJAg3VbEjgJuNplHMirXPTP7yvu_j8iAj7lxWrhFKTlDEaO7ioKlx24dgLJdCYJLjvV9CafWfCPf0gTEnFFAly5EAMmkfS3rJkxv9R63MwMEreIYFbgt_QOMn1XVMuoxb92K_Z2-GHez0CFS96X8bFcpeVfsavDwE884nNsXqAPGiz2SrXNqYVAeWFQFdEERB0GdfzgbqCC9AoJRjDsgwgCqF_gy7mdifiklwNn9rBKR8fwx5dips4SoT1R_Xwvp5sb7S8MNsV2jMn-nYiV66TcEVLEqBDBEQiznjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ا
کسیوس:ترامپ در «اتاق وضعیت» جلسه‌ای درباره حملات جدید و گسترده علیه ایران برگزار کرد.
به گفته سه منبع آگاه، رئیس‌جمهور ترامپ روز سه‌شنبه جلسه‌ای را در «اتاق وضعیت» (Situation Room) برگزار کرد تا درباره یک عملیات تهاجمی گسترده علیه ایران گفتگو کند؛ عملیاتی که دامنه آن وسیع‌تر از حملات کنونی در اطراف تنگه هرمز خواهد بود.
به نظر می‌رسد ترامپ مایل است جنگ را تا حدی تشدید کند که خسارات کافی به بار آید و در نتیجه، حکومت ایران تنگه هرمز را باز کرده و خواسته‌های هسته‌ای ترامپ را بپذیرد.
ترامپ این نشست را در حالی برگزار کرد که ارتش آمریکا برای چهارمین روز پیاپی، حملاتی را در منطقه تنگه هرمز و در امتداد سواحل جنوبی ایران انجام می‌داد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68156" target="_blank">📅 11:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68154">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5c420396.mp4?token=eJZhu7Q5iNWyHMKInOj01_F_5MhfsEqJN-DkTO8JfWvujislM4q7Jo4F2dT2lVKJ__zxovxrGBlVF3moYsUmxR28Ud1orrGAWK_20orqa_jj27-WaV5db4ZwlsRelpJ2W25o09Kb_YP2ob4wW4EN6-bDTF2xeLzJnBgM4pNeRYle3cGl7QjUT3Q1r7OxPTaXg0C33DAOXjS1E1c3RI_5Fz0-dve4mLEYLVFr1wy0XhEmQWaePJDrBc3zYq6MJfE9BYU4yvq4B2AuonA_S9oP_JR1zh4NQUWWVZ9vI1Zpl98UtamKFJ9oraUnC5xq2eltRZVHL4EpLn4zze5BH1q3Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5c420396.mp4?token=eJZhu7Q5iNWyHMKInOj01_F_5MhfsEqJN-DkTO8JfWvujislM4q7Jo4F2dT2lVKJ__zxovxrGBlVF3moYsUmxR28Ud1orrGAWK_20orqa_jj27-WaV5db4ZwlsRelpJ2W25o09Kb_YP2ob4wW4EN6-bDTF2xeLzJnBgM4pNeRYle3cGl7QjUT3Q1r7OxPTaXg0C33DAOXjS1E1c3RI_5Fz0-dve4mLEYLVFr1wy0XhEmQWaePJDrBc3zYq6MJfE9BYU4yvq4B2AuonA_S9oP_JR1zh4NQUWWVZ9vI1Zpl98UtamKFJ9oraUnC5xq2eltRZVHL4EpLn4zze5BH1q3Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه برخورد پهپادشاهد ، به طور مستقیم به یک انبار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68154" target="_blank">📅 11:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68153">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ov-YuScIcRnUxO0ghnRpVgvQgooUX0Zo0i1qwn52PxiOfSG4VW8y8rIOhnu-j_Z9CprLn5AFXYOkXIW8-H7KeoOa9XCs-Yplt2FdK2dphTf7dj2im9_KpqOnyNgzP1gV9muAOhG3gclsx6EfSTgbipC0Ej58baj0XTgkT3fFMOgkV-jWiB1j2aV3ocL3eRJydxAyZp5jTIxuSNPet_8BUp5QezeLexSF2us96RXJ3eQOUL9G5u4XYDk4MtS6XsG2k7ajyo1cFueB0Y3mDEJaCN-xeze8JeHLyK0ODNGdGn7IiP3QQxuk8wmlOaJlhsTkJLwQr9xH40lb4EeEYG98KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل بچه‌ شیعه‌ی آخوندپرست
🤯
🤯
🤯
🤯
:
#hjAly‌</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68153" target="_blank">📅 10:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68152">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31c4cf4b27.mp4?token=bvA754kAGvrLimyw5vK3BscZ6IJlDw35mahZ8zWvXqysVq01BrO7uPId0ESHVeaQxKDZNvj56Xp7Ap-dJg-zkJDRIG7hh59wrAYv4FK-evfBq6B5hojAnte2vDtyN1PwAgKT1RWRaAiHY9yWgx6nyLvbkHKy71DzzN5A69QWQBTwL135o6wHCnZr9Rv8kueYpxq2ybcuddEyor98Z9d1jsr5B9EAqDTNGaqrXVTXu1R8xhpGBDhDWaDWN5BKaq8pXY019C4cbpGH6Xobyjf1Jfmsk96wcOdXMtDly5YnDu_OzFFvhPx1iKrmYHcnd4T_966T17m7jfqA2vw--FdIxVP-PDzBIJJwygXxsQuV2bEguqv21GxGdmYWiex9b_fjqPTTcCLEA6lennshRMLyO4PFggv33aWo7AsWpmQC7g_p7D9Q7V60XbHkEUV-CL0tmHQtNQyTG3ha6w4iuT7ViU2yuAw4sBn4GM2VE0fhCqppSW3LqF9jCJ7mAAw3gR7nrx2m5KjGM-YxGhrrP1tdnapc117RcrNl7Et8mn8R2-rgaf-MmPJLwJIEQTIndVvmfzqs0yH2U78SbxOitzp23gotc5PJysbj9TZmP6GpO9Zw15HQx11rbAbSmjqF38aXPF53ifMAymLsyy1FnuP0Xve6sU4fy_qG_bZfQNek10M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31c4cf4b27.mp4?token=bvA754kAGvrLimyw5vK3BscZ6IJlDw35mahZ8zWvXqysVq01BrO7uPId0ESHVeaQxKDZNvj56Xp7Ap-dJg-zkJDRIG7hh59wrAYv4FK-evfBq6B5hojAnte2vDtyN1PwAgKT1RWRaAiHY9yWgx6nyLvbkHKy71DzzN5A69QWQBTwL135o6wHCnZr9Rv8kueYpxq2ybcuddEyor98Z9d1jsr5B9EAqDTNGaqrXVTXu1R8xhpGBDhDWaDWN5BKaq8pXY019C4cbpGH6Xobyjf1Jfmsk96wcOdXMtDly5YnDu_OzFFvhPx1iKrmYHcnd4T_966T17m7jfqA2vw--FdIxVP-PDzBIJJwygXxsQuV2bEguqv21GxGdmYWiex9b_fjqPTTcCLEA6lennshRMLyO4PFggv33aWo7AsWpmQC7g_p7D9Q7V60XbHkEUV-CL0tmHQtNQyTG3ha6w4iuT7ViU2yuAw4sBn4GM2VE0fhCqppSW3LqF9jCJ7mAAw3gR7nrx2m5KjGM-YxGhrrP1tdnapc117RcrNl7Et8mn8R2-rgaf-MmPJLwJIEQTIndVvmfzqs0yH2U78SbxOitzp23gotc5PJysbj9TZmP6GpO9Zw15HQx11rbAbSmjqF38aXPF53ifMAymLsyy1FnuP0Xve6sU4fy_qG_bZfQNek10M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوندها عُمر طولانی دارند و بیشتر از عمر متوسط ایرانیان زندگی می‌کنند:
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68152" target="_blank">📅 10:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68151">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1084df804.mp4?token=Ns_huqDBRDRox042zHTLR5Y6_h8RUe6jmHhWlcQt4wkCqvj0Q9xYG6IkWz-HaSghI34ITO7WJGJ3vwQuphkyJYIezJSFv_8Ix268Wew9mzzf7fByxBMK5rAXKIjah-ItLq4PNx1Hhw4CybL5MDhHnLzHWbUPbl1onuDk6E0RKM7SsFT1h_oB5jnb0wzQeRHbFIrH8Ygb_FnKfp1uQ4EQwQQTDrCzADN8Y-NK0BNdAbN4Al26naXmd2JOc6IirBqFMKfpGS55ckH-AlHDN8iOM2dPa3Gjwou-zXOAcUx3nxLGhXoeCYv-Idkyhe9JVEjiky6iBM0ESPsvRD9XK9aaUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1084df804.mp4?token=Ns_huqDBRDRox042zHTLR5Y6_h8RUe6jmHhWlcQt4wkCqvj0Q9xYG6IkWz-HaSghI34ITO7WJGJ3vwQuphkyJYIezJSFv_8Ix268Wew9mzzf7fByxBMK5rAXKIjah-ItLq4PNx1Hhw4CybL5MDhHnLzHWbUPbl1onuDk6E0RKM7SsFT1h_oB5jnb0wzQeRHbFIrH8Ygb_FnKfp1uQ4EQwQQTDrCzADN8Y-NK0BNdAbN4Al26naXmd2JOc6IirBqFMKfpGS55ckH-AlHDN8iOM2dPa3Gjwou-zXOAcUx3nxLGhXoeCYv-Idkyhe9JVEjiky6iBM0ESPsvRD9XK9aaUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیش‌بینی پروفسور جیانگ از تهاجم زمینی به ایران
:
پروفسور «جیانگ» تحلیل‌گر سیاسی مشهور در گفتگو با «پیرز مورگان»، مجری معروف انگلیسی، پیش‌بینی می‌کند که «نیروهای زمینی» آمریکایی از اوایل ماه دسامبر در ایران مستقر خواهند شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68151" target="_blank">📅 10:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68150">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSblWoiyjNU1Kga-0LfRPTni2ZPEs-gur6MzrUq2s4YNeCVPPYUwku9zs_krCHf-E-gegpjQz8yihOktToz9FDC9JaCsfjXLlQVOA8l2u0PvWicISofUIulLV8NMuJ_xye8SZI6BRVUtD_xNxG5t4ITb7pKWp8OWBEx9J1Hs8hVQnr4Ea5gb1PskHeEr5_RRMixYlDNLyWE6FZreOOnXogNfCIUBWnTB3dpUNILxl6Hojs3AKQBOLWD-wuwuD1PbkzHIu-RV0tSzJdV2pcd0jGcBmk9Xtw-ApPRYf27wNIinnR4iUuV4MtrRhxrBTawjOEkw3fYZFVuxQi5gvNpCnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ترامپ: کوه کلنگ ممکن است یک هدف احتمالی برای یک ضربه بزرگ و سنگین، درست به درِ ورودی باشد.
کلنگ گزلا (یا کوه کلنگ) در استان اصفهان و در نزدیکی شهرستان نطنز واقع شده است.
روزنامه تلگراف پیشتر گزارش داده بود که تأسیسات تازه‌ای در مجاورت کارخانه هسته‌ای نطنز احداث شده است.
این مجموعه در عمق ۱۴۰ متری زمین و در دل کوهی به ارتفاع حدود ۱۶۰۰ متر، موسوم به کوه کلنگ گزلا یا همان کوه کلنگ قرار .
ارتفاع این کوه تقریباً دو برابر کوهی است که سایت هسته‌ای فردو در آن ساخته شده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68150" target="_blank">📅 09:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68149">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93235f7cc4.mp4?token=nSRZBNRGpArn-RcXSNODsIJwgcFhugneqlhGSoI4ox2hfLdgEoQV1KDhnxhfHt_iz4D6bsFrjuQNbPS2yEOzbift9GpBbDqBEdj56MKU8YwXHlaJrtEKLf7RWPFqD93vK8n_TXxFoO1AhRJTWJnyse2Fumye5htLOK4kWl9t4y2BGmz8vSx8wL2PHq32QuaEDLd3_H7Y2Ivp-nQP9PnSzYGim014ZQH_Y1sSb_YMczK7DlqlT0LNkLqmkRbhtQmy4wJNoo_dfT_6_6KvCww71fujm-UDDo6cndeQRaq6uCJvh33mvWXJrHDmg2-x7lSTAY33db4ARH8oOyWH2pWkiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93235f7cc4.mp4?token=nSRZBNRGpArn-RcXSNODsIJwgcFhugneqlhGSoI4ox2hfLdgEoQV1KDhnxhfHt_iz4D6bsFrjuQNbPS2yEOzbift9GpBbDqBEdj56MKU8YwXHlaJrtEKLf7RWPFqD93vK8n_TXxFoO1AhRJTWJnyse2Fumye5htLOK4kWl9t4y2BGmz8vSx8wL2PHq32QuaEDLd3_H7Y2Ivp-nQP9PnSzYGim014ZQH_Y1sSb_YMczK7DlqlT0LNkLqmkRbhtQmy4wJNoo_dfT_6_6KvCww71fujm-UDDo6cndeQRaq6uCJvh33mvWXJrHDmg2-x7lSTAY33db4ARH8oOyWH2pWkiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رسانه حال‌وش: شدت انفجار به قدری شدید بوده که در لحظه اول حداقل ۱۰ نفر کشته شده است  @News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68149" target="_blank">📅 03:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68148">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
تا این لحظه ۲۰ نفر زخمی و ۲ نفر کشته شده  @News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68148" target="_blank">📅 03:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68147">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
تلفات امشب نیروی نظامی در بمپور</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68147" target="_blank">📅 03:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68146">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
تا این لحظه ۲۰ نفر زخمی و ۲ نفر کشته شده
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68146" target="_blank">📅 03:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68144">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a28218ed6.mp4?token=ndaKY6w4Dy6hKxgLdpIAbGqAjhp5cC1DXXQkW185l4QNI6nwIz8hWAdmA25WeOtNi6N8Wa9RfjhbGwQopfqhJQ2U5X7RNHZt9lKqOtAaA3aCD20FW3uPCu8WpwbiMVWkpPPBvVqEppyKLoGrWu_Cxijggx6Hfj7QIlUFDlRTF3kgKuJp6WDOM9coPv5rY7RtNq3ICVp2flDOx9HqpZbBgwKC798cCiKZu0PdJiCNOivbBiBu5aj43HYzyQg0Q3GTTOa4lt9BEJNFjdJtrpFNCls-jmiI2x08rIP2XV8dsohjTdIG0aWVKPCCtlIHKbpH7QW_BJp61Rs2vdEZMYR7kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a28218ed6.mp4?token=ndaKY6w4Dy6hKxgLdpIAbGqAjhp5cC1DXXQkW185l4QNI6nwIz8hWAdmA25WeOtNi6N8Wa9RfjhbGwQopfqhJQ2U5X7RNHZt9lKqOtAaA3aCD20FW3uPCu8WpwbiMVWkpPPBvVqEppyKLoGrWu_Cxijggx6Hfj7QIlUFDlRTF3kgKuJp6WDOM9coPv5rY7RtNq3ICVp2flDOx9HqpZbBgwKC798cCiKZu0PdJiCNOivbBiBu5aj43HYzyQg0Q3GTTOa4lt9BEJNFjdJtrpFNCls-jmiI2x08rIP2XV8dsohjTdIG0aWVKPCCtlIHKbpH7QW_BJp61Rs2vdEZMYR7kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تلفات امشب نیروی نظامی در بمپور
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68144" target="_blank">📅 02:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68143">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حرفای امشب ترامپ رو گوش کردم، یجا گفت فعلا نمی‌خوام باهاشون مذاکره کنم، تهش گفت اگه تا هفته بعد نیان برا مذاکره پل و نیروگاه‌هاشونو می‌زنیم
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68143" target="_blank">📅 02:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68142">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">از تبریز دارن اردن رو می‌زنن، جالبه از پایتخت اردن تا مرز اسرائیل فقط ۵۰ کیلومتره، ببینید آخوندِ گنده‌گوز که ۵۰ ساله می‌گه اسرائیلو نابود می‌کنیم، امشب جرئت نداره ۵۰ کیلومتر موشکش رو اونور تر بزنه :))))
#hjAly‌</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68142" target="_blank">📅 02:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68141">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43530d8c1f.mp4?token=jrt4O3a8YM42PZ9biziLnzTHXcEc4ym0f4ktthkB7YccDqEfoc1AceKXujkYbLO9yqci9plRnxDwKr2SiQDf1GcwV1ZzUcpFzpiKMJcFtevrTin5uvVQ-o6dn6JlRJvqRoGS01dIPciSQ1_jEwqQibytCP5IJa5AQkN-bT2nyYo7gSpqYABX7bqfIhCX1b1QS-3GNYZKVQzKmJfUXO-4NRN5Z2Xku9xle66ymE-pEewXzO1Ik0jEnBKF3ygTI7RbaMqTd2UkDqD3EnzXEMJD90bvLwEH3awoS7lUbdW7Asx5ctjshIMvjdYQCuxv4EEX_97OnrBLR0KdmGyr94UAtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43530d8c1f.mp4?token=jrt4O3a8YM42PZ9biziLnzTHXcEc4ym0f4ktthkB7YccDqEfoc1AceKXujkYbLO9yqci9plRnxDwKr2SiQDf1GcwV1ZzUcpFzpiKMJcFtevrTin5uvVQ-o6dn6JlRJvqRoGS01dIPciSQ1_jEwqQibytCP5IJa5AQkN-bT2nyYo7gSpqYABX7bqfIhCX1b1QS-3GNYZKVQzKmJfUXO-4NRN5Z2Xku9xle66ymE-pEewXzO1Ik0jEnBKF3ygTI7RbaMqTd2UkDqD3EnzXEMJD90bvLwEH3awoS7lUbdW7Asx5ctjshIMvjdYQCuxv4EEX_97OnrBLR0KdmGyr94UAtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند اردن
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68141" target="_blank">📅 02:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68140">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/453748b7ef.mp4?token=rOBfVSMlXc1Q9e-WtmjbXmr3rgMJz7kjFPGXLFjPjBsZ8Z5jZ_loUT1FhrT2sbLjFRcKQqDBHfHN1kCXtZ8bJB00L7ODZv6bKoV_jQEX3DdEggK7GlzvLP54-bHtCsxz7IuG1hEHt4wwAv5I7oYvwwGbnQKpf_CPdl9Ol_3sTS3RAOqDySXqbz6DxhX28as3fET13C8SkUt398YrZNOidC9WDMCS7nQrEAij-W990_ooFsFjP6gOAtR3sXyKWNa-SopBLVdicjLI47eXlxUkJj5SxIBcb7FkA1xeGSXA0VHWLlcB46iQqv0aLWr1wm2lPgCuXTx5TaSNdnPSWCMs0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/453748b7ef.mp4?token=rOBfVSMlXc1Q9e-WtmjbXmr3rgMJz7kjFPGXLFjPjBsZ8Z5jZ_loUT1FhrT2sbLjFRcKQqDBHfHN1kCXtZ8bJB00L7ODZv6bKoV_jQEX3DdEggK7GlzvLP54-bHtCsxz7IuG1hEHt4wwAv5I7oYvwwGbnQKpf_CPdl9Ol_3sTS3RAOqDySXqbz6DxhX28as3fET13C8SkUt398YrZNOidC9WDMCS7nQrEAij-W990_ooFsFjP6gOAtR3sXyKWNa-SopBLVdicjLI47eXlxUkJj5SxIBcb7FkA1xeGSXA0VHWLlcB46iQqv0aLWr1wm2lPgCuXTx5TaSNdnPSWCMs0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ای دیگر از شلیک موشک‌های سپاه به سمت پایگاه های آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68140" target="_blank">📅 02:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68139">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1073ff30f0.mp4?token=lHch1VcQMOb6C00tkOie0mcH7YLTa4s3rQOw-UIxRPRFp3Xz1y27VOY61dHQ6EVA5Ustamk3stJv-K6OCXlVHU1YNuBvO85wH4Yxz7UNCi6kjISvOUOszlYIr5Q-kTs7vt-6tcrqD6FWPFYHfPv0xszac1lLCXMEgqPfwnV25S9Fnd-2H0WxvgV9CcE6dXoTpEZmwByR3R62i_nrcLHHboyd2QKshkHFnxyT-8JrajVFwXm51ogai5NBS6UUMA2LXp5VuKvVupoYAg128nmMwDIzq-0lgV_3w432726gdvDeWctSdPeBanLjnNolQTOuU41A5HaIomT3_TRyLEMFlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1073ff30f0.mp4?token=lHch1VcQMOb6C00tkOie0mcH7YLTa4s3rQOw-UIxRPRFp3Xz1y27VOY61dHQ6EVA5Ustamk3stJv-K6OCXlVHU1YNuBvO85wH4Yxz7UNCi6kjISvOUOszlYIr5Q-kTs7vt-6tcrqD6FWPFYHfPv0xszac1lLCXMEgqPfwnV25S9Fnd-2H0WxvgV9CcE6dXoTpEZmwByR3R62i_nrcLHHboyd2QKshkHFnxyT-8JrajVFwXm51ogai5NBS6UUMA2LXp5VuKvVupoYAg128nmMwDIzq-0lgV_3w432726gdvDeWctSdPeBanLjnNolQTOuU41A5HaIomT3_TRyLEMFlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68139" target="_blank">📅 02:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68138">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
💪
گزارش های اولیه از شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68138" target="_blank">📅 02:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68137">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682a3eeafc.mp4?token=miCNYWQuOId-W27lOWeUX_EGbU2WyqYy_pm-rqVnD23ogHV2DIhU4qiP0J4L6_LFemnXu4zNm40q74DEs0zGnrk5YyY1vvepjiiAPsvq8O8yKksq6jX0LqkA6w1vNqRi2t9ThedmmoXHME008XCmbUEbPZa__lpdatuPNSR8Pn45IpAhCMFjcKkPSpfZ5Ks7Ib8jKzurKjrSUpvDtawOCLqlLbRDugEKZ1YjTzmRiC_IcC1Bzxqe9a0hEfHS5hbXIuIssdXCCoOaqXiDE7Rl5kLvPJltemTxD-g-hxjjl50Rl-olSgsgbPN3CunnfbiPFp_MliY-gZ5-4pR8pQPvBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682a3eeafc.mp4?token=miCNYWQuOId-W27lOWeUX_EGbU2WyqYy_pm-rqVnD23ogHV2DIhU4qiP0J4L6_LFemnXu4zNm40q74DEs0zGnrk5YyY1vvepjiiAPsvq8O8yKksq6jX0LqkA6w1vNqRi2t9ThedmmoXHME008XCmbUEbPZa__lpdatuPNSR8Pn45IpAhCMFjcKkPSpfZ5Ks7Ib8jKzurKjrSUpvDtawOCLqlLbRDugEKZ1YjTzmRiC_IcC1Bzxqe9a0hEfHS5hbXIuIssdXCCoOaqXiDE7Rl5kLvPJltemTxD-g-hxjjl50Rl-olSgsgbPN3CunnfbiPFp_MliY-gZ5-4pR8pQPvBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری:
آیا همچنان قصد دارید جزیره خارگ را تصرف کنید؟
⏺
ترامپ:
خب، نمی‌توانم چنین چیزی به شما بگویم، چون اگر بگویم حماقت است. اما کار جالبی می‌شد و کمی هم خبرساز می‌شد.
⏺
مجری:
آیا احتمال عملیات زمینی را رد می‌کنید؟
⏺
ترامپ:
می‌گویم نه؛ البته اگر شرایط اقتضا کند [رد نمی‌کنم]. گاهی اوقات به عملیات زمینی نیاز است، اما ما افراد دیگری را داریم که عملیات زمینی را برایمان انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68137" target="_blank">📅 02:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68136">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25d7e536a1.mp4?token=Xp9L-SBXBa6iOqa4SYgMlKX14a4MK4gyv6_bWSTcBZ4kPCTgfQhP1zAlABAg862aFKD4kgYlkcR5ap7zs6DRB9y4h2vTj-7KkI3jdMRCcOsrc-VDmNR6Bx9Zmn2MT8lgN0WMcVzCk8NZjoluPIutCSncbJ6LK3LQub1DoKjCbFfvApl_7RJ9FzPKDOzSwy4mEvZNB7G6FwOo-e2JAiFHVX5JHv4IxvAK0BgA4RvzmKaQFa_vWjH6NTDv4rOQgMzBVK4qRZMJTIm4vc1dUpGWoQBJY3Gy5CufD9ogoI3T6BnGj6qlBv-WT0oU-T5z2k-UKguamBmHj4JeYyZur_K4og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25d7e536a1.mp4?token=Xp9L-SBXBa6iOqa4SYgMlKX14a4MK4gyv6_bWSTcBZ4kPCTgfQhP1zAlABAg862aFKD4kgYlkcR5ap7zs6DRB9y4h2vTj-7KkI3jdMRCcOsrc-VDmNR6Bx9Zmn2MT8lgN0WMcVzCk8NZjoluPIutCSncbJ6LK3LQub1DoKjCbFfvApl_7RJ9FzPKDOzSwy4mEvZNB7G6FwOo-e2JAiFHVX5JHv4IxvAK0BgA4RvzmKaQFa_vWjH6NTDv4rOQgMzBVK4qRZMJTIm4vc1dUpGWoQBJY3Gy5CufD9ogoI3T6BnGj6qlBv-WT0oU-T5z2k-UKguamBmHj4JeYyZur_K4og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما در حال رصد «کوه پیک‌اکس» هستیم، چرا که گزارش‌هایی مبنی بر وجود اندکی فعالیت در آنجا دریافت کرده‌ایم. ما دوربین‌هایی در اختیار داریم که قادرند نام و نشان شناسایی افراد را حتی از فضا تشخیص دهند؛ این دوربین‌ها تمام بخش‌های «پیک‌اکس» را پوشش می‌دهند. اگر آن‌ها کوچک‌ترین حرکتی انجام دهند، ما بی‌درنگ وارد عمل شده و هر اقدامی که لازم باشد را انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68136" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68135">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3f1669520.mp4?token=IPp9sAtoo7iXC_McETRd62kXnIhhbkHLKH8g-lHqVQZC7d0G-wzXmHvws0e1jTPan69XtQDwGIHwf8LFA3h1XexoJjjdbrDDWRUKjBpIVrdYm6KSxeC5HwsdZCVEy02Irc--5UiLiKsgFIFr3LE-_yVB24knNRlm8own9clw7gSZ2Se-C01MIZH6ocUphffUiPKJfhGrT0hT3bt6UcLG9NwPvzB_LnskwUNDNRbJGZm0GywPdGMRPVk4QBPMtPnW2ARUtI_o2UV48rFbhQl6dbt4XzwmP4miKrlfAnlF8jlgiB7nRgDIlKLfajwVySMbTJa4qRqGNX-RdyGOA6P_aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3f1669520.mp4?token=IPp9sAtoo7iXC_McETRd62kXnIhhbkHLKH8g-lHqVQZC7d0G-wzXmHvws0e1jTPan69XtQDwGIHwf8LFA3h1XexoJjjdbrDDWRUKjBpIVrdYm6KSxeC5HwsdZCVEy02Irc--5UiLiKsgFIFr3LE-_yVB24knNRlm8own9clw7gSZ2Se-C01MIZH6ocUphffUiPKJfhGrT0hT3bt6UcLG9NwPvzB_LnskwUNDNRbJGZm0GywPdGMRPVk4QBPMtPnW2ARUtI_o2UV48rFbhQl6dbt4XzwmP4miKrlfAnlF8jlgiB7nRgDIlKLfajwVySMbTJa4qRqGNX-RdyGOA6P_aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری:
«۱۰ فروند کشتی روز دوشنبه از تنگهٔ هرمز عبور کردند — کمتر از ۱۰ درصد چیزی که معمولاً از این آبراههٔ حیاتی عبور می‌کند. وقتی می‌گویید «تنگه باز است»، منظورتان چیست؟»
⏺
ترامپ:
«اگر مردم بخواهند از آن عبور کنند، باز است. ما آن را برای ایران باز نمی‌کنیم… الان باز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68135" target="_blank">📅 02:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68134">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
مجری فاکس : آیا انجام یک عملیات زمینی محدود را منتفی می‌دانید؟
ترامپ : «نه. گاهی اوقات به عملیات زمینی نیاز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68134" target="_blank">📅 01:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68133">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbabff277a.mp4?token=Y5-5iEJ-jB6ebbR2BL2HtxWJPrH38j-nSkY8aRPdfk9Q1WuzD_GCys5VUXvboatAK1IxWg93FXF_DotgLnQLBTjExXYmIicFFW1upxsAuF02BaXus6KmtMvlNT-CkOvFb08w84H6wIvgIw1clXNJPJiw3uxSau0pjK-iFpHoa6Wc5tbrnj8igHB7jKfBg78X7uMYfdv9O5QCzCG36JIk0Yt5jl2KKBAJkU8U6oBbR4QG-LPrmWy-EHNlB8LFrBnkCGALwosw2IbyXaAKC0UrLgYTrDjwXe9Bd7OLptWQRNl8LbkWBLgqgSUYOz6WJAdktc5uzEc5lmKxWfNZXh3K9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbabff277a.mp4?token=Y5-5iEJ-jB6ebbR2BL2HtxWJPrH38j-nSkY8aRPdfk9Q1WuzD_GCys5VUXvboatAK1IxWg93FXF_DotgLnQLBTjExXYmIicFFW1upxsAuF02BaXus6KmtMvlNT-CkOvFb08w84H6wIvgIw1clXNJPJiw3uxSau0pjK-iFpHoa6Wc5tbrnj8igHB7jKfBg78X7uMYfdv9O5QCzCG36JIk0Yt5jl2KKBAJkU8U6oBbR4QG-LPrmWy-EHNlB8LFrBnkCGALwosw2IbyXaAKC0UrLgYTrDjwXe9Bd7OLptWQRNl8LbkWBLgqgSUYOz6WJAdktc5uzEc5lmKxWfNZXh3K9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار:
آیا اطلاعات خاصی وجود داشت که باعث شد تصمیم به آغاز این عملیات بگیرید؟
⏺
ترامپ:
ما می‌دانستیم که آن‌ها خواهان سلاح هسته‌ای هستند.
⏺
خبرنگار:
آن‌ها می‌گفتند که خواهان سلاح هسته‌ای نیستند.
🔴
ترامپ:
هر چه می‌گویند دروغ است. آن‌ها دروغ می‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68133" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68132">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1f31387d.mp4?token=K3ZBjdQjkASc33qtn1QCdwkUPECkQ_dnxFYlFjFPtg8DkXroXXn7TmTiiafFq_LfoUGpbKhz7x1YtdKb5AsAtPGIS5LQ6tmWBOMeRFvDHBoLWnP3AJTFCIvBGGh3xAZk4d5Ip0vy1x0jAVXsrzEXSwpGpZG8mgHnbCRA42v5J4Z_8cZnRbX8Wz6WZutFFiNN-yMkS_PmnwvN29H1Z9TqMZ_LMKCdYq-03f0RBgwKO0hnU-RGYvUpLQknO25eBj-Yn4_vYFTxOCXsl1lp-HMDtUEZjV-fuRFrK2auVelbQyGSuiiTb-WsLW4lUA5pRw9d8RKduyzKMX7cr2y0ACGeiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1f31387d.mp4?token=K3ZBjdQjkASc33qtn1QCdwkUPECkQ_dnxFYlFjFPtg8DkXroXXn7TmTiiafFq_LfoUGpbKhz7x1YtdKb5AsAtPGIS5LQ6tmWBOMeRFvDHBoLWnP3AJTFCIvBGGh3xAZk4d5Ip0vy1x0jAVXsrzEXSwpGpZG8mgHnbCRA42v5J4Z_8cZnRbX8Wz6WZutFFiNN-yMkS_PmnwvN29H1Z9TqMZ_LMKCdYq-03f0RBgwKO0hnU-RGYvUpLQknO25eBj-Yn4_vYFTxOCXsl1lp-HMDtUEZjV-fuRFrK2auVelbQyGSuiiTb-WsLW4lUA5pRw9d8RKduyzKMX7cr2y0ACGeiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«همان‌طور که می‌دانید، ما پیش‌تر دو بار به جزیره خارگ حمله کرده‌ایم... اما در مورد تصرف آن، اگر بتوانیم توان آن‌ها را به اندازه‌ای کافی و عمیق تضعیف کنیم، این کار را انجام خواهم داد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68132" target="_blank">📅 01:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68131">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
حملات به ایران ادامه خواهند داشت تا زمانی که من بگویم کافیست.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68131" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68130">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f264ca5d25.mp4?token=leV6iY-BiGpIByQNPnO29QkPF2jpTM8N3DZHhOZe2laqS56cYNvHXdQIMawiHnWl4RClbwsrz_aN843Tb2dT-gB29R-ooGdZ0ISpa5tF3i6-pUzXLMkxj7g3P8mvbuBjJlfcMAJ916ZswsVvkrfpxYDfSauw6qBbgf7nw8IxXGoN_-wBqeOJ8ehm0m49IG5ooNt31G85Ff6st7S8x91P5KKnX5oS-bSdzYDdAjni1TvpgPEf7FNrSoMeC_4eS8Y8NpI7n8fVDS7kofKIqWOOcKsjsKJUH7BGrq8EUIWEQ9ZGvcwLniqWmbXQwMN4NphSWC0q_FWQYGsAaC2avfKovQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f264ca5d25.mp4?token=leV6iY-BiGpIByQNPnO29QkPF2jpTM8N3DZHhOZe2laqS56cYNvHXdQIMawiHnWl4RClbwsrz_aN843Tb2dT-gB29R-ooGdZ0ISpa5tF3i6-pUzXLMkxj7g3P8mvbuBjJlfcMAJ916ZswsVvkrfpxYDfSauw6qBbgf7nw8IxXGoN_-wBqeOJ8ehm0m49IG5ooNt31G85Ff6st7S8x91P5KKnX5oS-bSdzYDdAjni1TvpgPEf7FNrSoMeC_4eS8Y8NpI7n8fVDS7kofKIqWOOcKsjsKJUH7BGrq8EUIWEQ9ZGvcwLniqWmbXQwMN4NphSWC0q_FWQYGsAaC2avfKovQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«در نهایت، اهداف حوزه انرژی در ایران را هدف قرار خواهیم داد. نوبت به پل‌ها می‌رسد؛ هفته آینده سراغ آن‌ها می‌رویم. ما تمام نیروگاه‌هایشان را از کار خواهیم انداخت. تمام پل‌هایشان را نابود خواهیم کرد، مگر اینکه پای میز مذاکره بیایند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68130" target="_blank">📅 01:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68129">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36032be115.mp4?token=nNc9S1cIOKaIhe6A2g1JM8YlBi4MhJELa5FyIiyd5y6tL3InOpALdOe4UES_yHfzCbDkNVRyr84iVV0VmvIA51VHFxU-YrMPFpw1rm5FxQmNDZksJWLsIHa7IR_jGR9ezUYrU26r2Ag4rZTd1I4MkiD3KxVYYcGHp5-dEvB3l7oGBVwRwdwAybNIuDp_3KFyb-Rx3GwweQtKzqlJpPoPT_yT07KosjbyIho-U672FJdB-fFsq6MezEiLJN5MWXiVWM8r9UUHD_yZbFAjLcGOHEA_geYo39BoeMWGf3cuLvlKklYUYbFOHcrGXWWzfWGzgxSGp7BjuRnjv-JwrFQhvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36032be115.mp4?token=nNc9S1cIOKaIhe6A2g1JM8YlBi4MhJELa5FyIiyd5y6tL3InOpALdOe4UES_yHfzCbDkNVRyr84iVV0VmvIA51VHFxU-YrMPFpw1rm5FxQmNDZksJWLsIHa7IR_jGR9ezUYrU26r2Ag4rZTd1I4MkiD3KxVYYcGHp5-dEvB3l7oGBVwRwdwAybNIuDp_3KFyb-Rx3GwweQtKzqlJpPoPT_yT07KosjbyIho-U672FJdB-fFsq6MezEiLJN5MWXiVWM8r9UUHD_yZbFAjLcGOHEA_geYo39BoeMWGf3cuLvlKklYUYbFOHcrGXWWzfWGzgxSGp7BjuRnjv-JwrFQhvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار:
آیا جنگ با ایران از سر گرفته شده است؟
⏺
ترامپ:
خب، گمان می‌کنم بتوانید هر طور که می‌خواهید آن را تعریف کنید، اما قطعاً ما داریم ضربات بسیار سختی به آن‌ها وارد می‌کنیم. آن‌ها باید ضربه بخورند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68129" target="_blank">📅 01:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68128">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4323d3fd2.mp4?token=r_tpWmDvsnWLf72ETu7tlfI166Evv01-P-4yKu9B0jC0w-D9et14DSytq-3z1xVUWJldv4uIl34Ecu5n4ZGU4l2NwGgYlCYKLYxb6VAF_0TjLRud_lbNt0fBDwCO1wIHK5vei0uK-5L8ltGUSF8Yzu6YdQ-xQ-p2YRiusCXaNZCHSCP1gXYn7pO-EAz1RnvVzQpG-3p16FVqdd9dtT1RbnLUBNDn39vRr2xi6bnITg9OJt81nr_M6P1cRE1nJOzcxK3cjwftqqxY7e_jQmn-0dzOV6w-dsm8qTuI9SRv3BXRkXGxKE8NvB2PjrTZpeFNamdNynJcF4U71d_JsI2VTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4323d3fd2.mp4?token=r_tpWmDvsnWLf72ETu7tlfI166Evv01-P-4yKu9B0jC0w-D9et14DSytq-3z1xVUWJldv4uIl34Ecu5n4ZGU4l2NwGgYlCYKLYxb6VAF_0TjLRud_lbNt0fBDwCO1wIHK5vei0uK-5L8ltGUSF8Yzu6YdQ-xQ-p2YRiusCXaNZCHSCP1gXYn7pO-EAz1RnvVzQpG-3p16FVqdd9dtT1RbnLUBNDn39vRr2xi6bnITg9OJt81nr_M6P1cRE1nJOzcxK3cjwftqqxY7e_jQmn-0dzOV6w-dsm8qTuI9SRv3BXRkXGxKE8NvB2PjrTZpeFNamdNynJcF4U71d_JsI2VTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
‏ارتش جمهوری اسلامی:
در مرحله هفتم عملیات «صاعقه» محل استقرار جنگنده‌های اف ۱۸ و سایت نگهداری تجهیزات ارتش آمریکا در پایگاه الازرق اردن را هدف حملات قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68128" target="_blank">📅 01:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68127">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
حمله به جزیره هنگام
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68127" target="_blank">📅 01:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68126">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
بندرعباس و سیریک بوووم
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68126" target="_blank">📅 01:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68125">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddea8a9d1.mp4?token=rNLWwRr5QS1jiutBKxOQu7MSog7haj2Rd3M_1ie80pG6vQWR6JQtQDAJBCpam1PpxFjqfubm-d-dJkORYus9i9tu-A7UGEHUasWs7wf69e5-WK4zDbyxs8esPDpf9cN-JKYPONRH2Ezy4GxylmAqBbY74xLerUkPDdWm_KmFnm4glQZw8QM1F1tUHs4c4EYZCu5HpYaxnzHZXINrAkIo3Czp2khyWC-9mXBHJd6WlbNmf7fgUmYP6F3hlWMoOaRXAal0zXRinGJYke6pVjxzOwcAMa4Ml-dZUdAK05S2aXfpIYcUNa0Zmv9lEQvPGOr1NG0Iewn2c9rgBLpH54q_8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddea8a9d1.mp4?token=rNLWwRr5QS1jiutBKxOQu7MSog7haj2Rd3M_1ie80pG6vQWR6JQtQDAJBCpam1PpxFjqfubm-d-dJkORYus9i9tu-A7UGEHUasWs7wf69e5-WK4zDbyxs8esPDpf9cN-JKYPONRH2Ezy4GxylmAqBbY74xLerUkPDdWm_KmFnm4glQZw8QM1F1tUHs4c4EYZCu5HpYaxnzHZXINrAkIo3Czp2khyWC-9mXBHJd6WlbNmf7fgUmYP6F3hlWMoOaRXAal0zXRinGJYke6pVjxzOwcAMa4Ml-dZUdAK05S2aXfpIYcUNa0Zmv9lEQvPGOr1NG0Iewn2c9rgBLpH54q_8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
هم‌اکنون دارلین گراهام نوردون، خواهر لیندسی گراهام، در حال ادای سوگند برای گرفتن جای برادرش به عنوان سناتور کارولینای جنوبی است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68125" target="_blank">📅 00:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68124">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🏆
اسپانیا با پیروزی در برابر فرانسه راهی فینال جام‌جهانی 2026شد.  @News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68124" target="_blank">📅 00:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68123">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
انفجار چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68123" target="_blank">📅 00:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68122">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWI7jhHK13N2Y2AfIPE3Ku-6PaLKahwixXLQpGDWCSeJEa9FLsu-mgQ579eqoY3ugGc29CFvgrQ4SaHKrELgzyVjkozTxTeMMt9TPMKIspxM919J17C-L1cTf4V-qpYozmsiPoR6wwygKLvmiFiMqeXo0i5tMFb87I6htrYHArVbPyFzqI-Olx6ujEjbM4f6zkxbr_M_kANJ9-2LIoraFJXS9ILFwXEjtc60zaYPjm1L3R3UB0WGxc2Ff_3qrXTrqGjxT3EfdL-SJdpyAP7NdQGPTptnAY6zx6wDtE8jKQDoncX33-HDRoL7cSG7-jOvE5uDmNXZ-ZMa3qA6vYghrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپانیا با پیروزی در برابر فرانسه راهی فینال جام‌جهانی 2026شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68122" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68121">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a5f1d44f.mp4?token=KvW8EEuCA6j0B8rfB2DhqpEhKh6J98OWp99B8BB39-Cdza3Dw5D3rOrMJKm3ZLxPnfNDWlrccI7SCjgZYvvNYm9LYXNx9Cl1L04r0TnOqceKjRCx8ruzWVpylbyQl8tUxhdB0fIAPwgyvtkquOx6ZD43VtcQBoP_UYk9UEIzYoDR9ypKB-sDvIpk0bY8r3wNP71T143GDjQbadP4HGzjzN0e9C5V3558uGbusxfX3RDbbAbdSX9SCCPfkpwEQ9I1gBGPu1V_y9fwLmxJzDHvdDl90wy3pULGnEemqOEElMcG6hopbMW5KxUk1kjmWG0GTdJYmZHmWt2X3wAy7bGbuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a5f1d44f.mp4?token=KvW8EEuCA6j0B8rfB2DhqpEhKh6J98OWp99B8BB39-Cdza3Dw5D3rOrMJKm3ZLxPnfNDWlrccI7SCjgZYvvNYm9LYXNx9Cl1L04r0TnOqceKjRCx8ruzWVpylbyQl8tUxhdB0fIAPwgyvtkquOx6ZD43VtcQBoP_UYk9UEIzYoDR9ypKB-sDvIpk0bY8r3wNP71T143GDjQbadP4HGzjzN0e9C5V3558uGbusxfX3RDbbAbdSX9SCCPfkpwEQ9I1gBGPu1V_y9fwLmxJzDHvdDl90wy3pULGnEemqOEElMcG6hopbMW5KxUk1kjmWG0GTdJYmZHmWt2X3wAy7bGbuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران تنها جاییه که بتمن هم به گا میره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68121" target="_blank">📅 00:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68120">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1Lt3fbCf4pD9ShA2WTWXCnhjdmvR7vOBfVs1XGceospmtUqnxYu6SqCRABW5prQwzmYvj1AVz81SI4InNRjXg_y4ffOH-fAk2jNrxY-HeSnSFO2oYVYAjLWnUzpfFvX2aO30Xmh3_qjN1eSs5a6SfdbNWCSCA3fsmlvup6nB-1rH2AKmN4ARFoQcVVrDFUGy4bUQqQ8-9ysGaspslDwItBxuZoYzWVZFa3YYIIIfQwCjqoB8IQcXWFb9HndgUNZ81uIFCSlw7XIS4kOR8PDRowDOOo7EJD-9iTp-fsXlvysVF_uYzQSU1JiJuwnUOOKJfYQ-JMq7k2TUVA--IJLsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای ایالات متحده امروز ساعت ۱۶:۰۰ به وقت شرقی، محاصره دریایی شناورهایی را که به مقصد بنادر و مناطق ساحلی ایران و یا از مبدأ آن‌ها در تردد بودند، از سر گرفتند. در حال حاضر، بیش از ۲۰ فروند ناو جنگی نیروی دریایی ایالات متحده و صدها فروند هواپیمای نظامی در سراسر خاورمیانه مشغول فعالیت هستند. نیروهای آمریکایی همچنان هوشیار، دارای توان رزمی مرگبار و آماده‌به‌کار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68120" target="_blank">📅 23:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68119">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇪🇸
گل دوم اسپانیا به فرانسه توسط پدرو پورو</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68119" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68118">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c993da0a01.mp4?token=eoJtKC5CiAmulsDaHIbD2o26yfAOYnfKnZKk5P3iPEm4Gdc_a2L3dvjL4tqBxgW2t39NoXxfxsc-fE8KcqmuRZ0S0RzS19l_RBfADa-caxbMXUrN3sQBKFjXNhRbOKE-x47ZvkmLQcVDMoeM_eUUQTSbmrUiFZM9HX1RVPTzsA4xYpiUsHZrTGQzx3iMFs256TfV8PYn8ewu3nss-JsRJCSaedvwwFQeBdSPOPAHAKLR0lm6GfP-0fCmPEtyKfdYPwiUX8h-_5ZoO5iAWioC3d-XXMiZMnlpAe6L8FfWNZNKvS7fYSFRd1Avvu_LHMEvty46FkoBDF8IplBBNT7XLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c993da0a01.mp4?token=eoJtKC5CiAmulsDaHIbD2o26yfAOYnfKnZKk5P3iPEm4Gdc_a2L3dvjL4tqBxgW2t39NoXxfxsc-fE8KcqmuRZ0S0RzS19l_RBfADa-caxbMXUrN3sQBKFjXNhRbOKE-x47ZvkmLQcVDMoeM_eUUQTSbmrUiFZM9HX1RVPTzsA4xYpiUsHZrTGQzx3iMFs256TfV8PYn8ewu3nss-JsRJCSaedvwwFQeBdSPOPAHAKLR0lm6GfP-0fCmPEtyKfdYPwiUX8h-_5ZoO5iAWioC3d-XXMiZMnlpAe6L8FfWNZNKvS7fYSFRd1Avvu_LHMEvty46FkoBDF8IplBBNT7XLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
علی خامنه‌ای، (19 دی 1404):
ترامپ که با نخوت و غرور نشسته آنجا راجع به همه‌ی دنیا قضاوت میکند بداند که مستبدین و مستکبران عالم، از قبیل فرعون و نمرود وقتی که در اوج غرور بودند سرنگون شدند، این هم سرنگون خواهد شد.
⏺
🇺🇸
دونالد ترامپ، (10 اسفند 1404):
آیت‌الله خامنه‌ای ایز دد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68118" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68117">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
⭕️
محاصره دریایی علیه ایران آغاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68117" target="_blank">📅 23:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68114">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iHUgkO37r-AZjUjEcrsYlbnJhfWuwQifVhdgvvJRoq22W8P3oK1K9p-oXfuCDULXdEZN4kYX-ofc0fuqWH3h5m7kDkY77VteLJTKgfNO-x79YO776WRIlplo-3lP6Gs1z0qryjQQhx06ypOUEYSg-cLYApqeSyZf9k7XQqpJ6h7AN5y_W_HsaNlJ4o_5SOpwdlvQNaVA2ChE_qnYkL9Poz-S0wDwAN3e0lAd8L4fU5Xb39-08Lb03OSF07X7axhSNE36-1xzi4JFoWVulFPVfT5QEYEH0XBzNTvremnHYZyaPPAJv9Theam4M7P64oVoPX0PD-sLn1hhNwl2x7oVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQqbcg1wR3jm1zHrOf4oRInixzr1c4m6YxG75ZTI9yss-IVM3jSXFyy6EDQPzynQREOWASw_DFBbGmrqCJHXbmKw_hs-nj7c5Q92MqQNZzCc2txXUG45FDUsugrrJLXmpP1vrxZW09KwaLBC84Fs_8NQeSwyFrHNCm4bc3oN3LD2fHJ-axyX0sXE3rBrVkJcdZbvUAnHF0p28Ax7ZRVOBQc9q_S5-CDsZ5slOdy3_PnFJo1rRqHzn0wYb5vEa0fo7u1swP9WRz4QeDF71OLYHAqlIKfCPr7FvoS-VceM-w-NdfYGt_TjNzKgMyRoBkUICK5LDT2fAC3rPQvHU6KlTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تازه می‌خواستیم نودای نیلی افشارم بزاریم، پس هر وقت بابای مانی لفت داد می‌ذاریم #hjAly‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68114" target="_blank">📅 23:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68113">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
سیریک بیش از ده انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68113" target="_blank">📅 23:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68112">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
🚨
انفجارهای جدید در خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68112" target="_blank">📅 23:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68111">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
‼️
تصاویر جدید سپاه از حملات موشکی‌ش
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68111" target="_blank">📅 23:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68110">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ماشالاااا اسپانیاااا، اینا بیان فینال مسی راحت تر قهرمان می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68110" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
