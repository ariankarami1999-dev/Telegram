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
<img src="https://cdn4.telesco.pe/file/urFNX22FrJggyHxBjMD_j3Q5_l4L9NJN-jTYlsscJc-qppcgHVp1kf3V9evIbNGSonmr3J-lHWW7WWWJPuv4vu6zJqLDu7n1lIKqf-vbsYcUeeCrW0ij3gZOsWV_g2fyFuWfQrOtSHC7haPFQxeAc7-XfP2425_R3UDDia49UkIU45rnOZVgE3YO4mH8hsk8lhssIfPHktJY0CPN_AMNdoK9PeyJK1sAZyKaNtQMIDSugDIP8Fra94gsXNZZt3UYqo1_EW_8IQWbq5jKyaG0g0sn4CKZeRO6gWOeWtNZDUdc4QCVPIj_v0afBfT8_jM35yDv8dFJTZH3eUzfnS_ETA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 902K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 13:09:42</div>
<hr>

<div class="tg-post" id="msg-124118">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2f74ae093.mp4?token=TUnopWGGBv9LmE4-Bq3fzm96Vkb0GYCENfTW1sjaRAc6T0IfjIWtjgAAScYyHSvFyk2JG6DJXYyPDZKUzuSkrtoCe55D7XMXcl4pzyNdS1HfO5IZ_pdkpUCo-tlG9b_QX7NPISyUkYtD7RHyxD32x4Y_c5kspo_Y7Q9YkAqqg5VCTddKn7nczatXgIxwMsmC2VpwD0iLsP4Gnp1fFXF4ZkI43QR31LEVpoGI_eQq8mDAXwTbBZaFt5vF_ZZ34G23oKmFlMDjpJovho3DVLEsnwDJV1GL3zdG__KYYr0IBXLEbzVkybd6CA5Ta1TdwSmojbTQhfGDXI74-RKflnw88Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2f74ae093.mp4?token=TUnopWGGBv9LmE4-Bq3fzm96Vkb0GYCENfTW1sjaRAc6T0IfjIWtjgAAScYyHSvFyk2JG6DJXYyPDZKUzuSkrtoCe55D7XMXcl4pzyNdS1HfO5IZ_pdkpUCo-tlG9b_QX7NPISyUkYtD7RHyxD32x4Y_c5kspo_Y7Q9YkAqqg5VCTddKn7nczatXgIxwMsmC2VpwD0iLsP4Gnp1fFXF4ZkI43QR31LEVpoGI_eQq8mDAXwTbBZaFt5vF_ZZ34G23oKmFlMDjpJovho3DVLEsnwDJV1GL3zdG__KYYr0IBXLEbzVkybd6CA5Ta1TdwSmojbTQhfGDXI74-RKflnw88Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
الحدث: صحنه های آوارگی به سمت منطقه شرق بیروت پس از تهدید نخست وزیر نتانیاهو به حمله در ضاحیه جنوبی بیروت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/alonews/124118" target="_blank">📅 12:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124117">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPyU6MB6w7e6S5BtE9l5o5OQ3ZEaApLmQCs2zfy3AAaLDKuXU5C8V5-WJVnsFNF5x_f2ikqptapWw6uiUEn3NgpuzJwGcaOQTwyXuGoUYsEmIWmlQaLIFxF7jXN9SzPXVFd2aUa9YHVEtmfLbW9WfKKc-GUX7aNqYgJ1U8-X64BRaapKwks3-V-hyuFp1ulVE_l9nib6bVWwMGz3OQPh-iPbYVTL_UezLU2ZHpJG9PVFqqQA0S8kmfh69LpEn9TjzbmxkRrp4Jh9H6rNcPO7MnT_C3aHR_GzYOCvxU-zO_s8qSlawoKUFegkGQ4Megj2NrcJ_9p9Saqs2NTUML7R-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمدباقر قالیباف:
محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش بس است و هر گزینه ای بهایی دارد که پرداخت خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/124117" target="_blank">📅 12:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124116">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zp1hPIDieYr_-7rEA6MfYHygsQHV_BtVFzFBWI3CernC5oxnBp82Eky-P5n8sxO_aXq5uOE94g4YJldKpUTXsCGUF-m_F-mULk3kqejOuFXEkeR7qbquLUbx2WHczWgp2lVJ21zfibwQx1DzzS82Cr1-K9S1M4mzZVnIvz2Jyfej23l8ce_dA8GbmqqfvsjAMEVmG7gufNYyDSzd5tRPAvyPnismoWNRdMNbbZyo_cnkqzqz1DWFS38rwFxvQKIEOKPJ0tKbxksLsOh0W5oKL0nlizVg97OedsDXj-fy-K_Sjlc1M8VZnTg9bIJ_yAF6_aEI1YC70BRi9wB2ddbiSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه‌های عربی از قبل دوربین‌های واید رو توی ضاحیه کار گذاشتن
🔴
منتظرن حملات شروع بشه تا همه‌چیز رو ضبط کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/124116" target="_blank">📅 12:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124115">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
قیمت دلار آزاد امروز دوشنبه ۱۱ خرداد ۱۴۰۵ با افزایش به ۱۷۳,۰۳۰ تومان رسید؛ دلار حواله‌ای نیز ۱۴۷,۰۸۸ تومان شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/124115" target="_blank">📅 12:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124114">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
قیمت سکه امامی امروز دوشنبه ۱۱ خرداد ۱۴۰۵ با افزایش به ۱۸۳ میلیون و ۵۰۰ هزار تومان، نیم‌سکه ۹۳ میلیون تومان، ربع‌سکه ۵۳ میلیون تومان و سکه گرمی ۲۷ میلیون تومان رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/124114" target="_blank">📅 12:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124113">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: انتخاب آقای قالیباف به‌عنوان نماینده ویژه، در پیشبرد همه جانبه رابطه ایران و چین مهم و مثبت است
🔴
هرگونه اقدام ناتو در خلیج فارس، منجر به پیچیده تر شدن اوضاع خواهد شد
🔴
آخرین وضعیت تفاهم پایان جنگ این است که تبادل پیام ادامه دارد و به جمع‌بندی نرسیده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/124113" target="_blank">📅 12:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124112">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b8e4fd8f.mp4?token=Io8bURXUdRF8AsEjblGb8ImRBEWZi924LTqVuxrb5yFXHBMuKSbb97ql-eS-cdOZ7F-_KJ71uzlzjLY3uUR2exN_PxSRn4jDCGM8FwPaUYCLy3UAUQKJNKFmlWDi_SCp0xz_aZ7PTbI9t4lJa5wIWSp3jbEgFdJlUQuXtuBbaCXmKwekfXY8GFLsh58Vvus8b3hm0VRrUVbQM6VETRMaJQ56kCtY20ss5DLJcdFLcwJZHXAPjETSBT_wsPT_pv44pE9uFHsOhInZYx0H5a5pfJdgqZYAf1lBqChBiYyA_DMCR5Z9PX-51NoRujGpfpDNzng9_516OZkBEliMI6OXMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b8e4fd8f.mp4?token=Io8bURXUdRF8AsEjblGb8ImRBEWZi924LTqVuxrb5yFXHBMuKSbb97ql-eS-cdOZ7F-_KJ71uzlzjLY3uUR2exN_PxSRn4jDCGM8FwPaUYCLy3UAUQKJNKFmlWDi_SCp0xz_aZ7PTbI9t4lJa5wIWSp3jbEgFdJlUQuXtuBbaCXmKwekfXY8GFLsh58Vvus8b3hm0VRrUVbQM6VETRMaJQ56kCtY20ss5DLJcdFLcwJZHXAPjETSBT_wsPT_pv44pE9uFHsOhInZYx0H5a5pfJdgqZYAf1lBqChBiYyA_DMCR5Z9PX-51NoRujGpfpDNzng9_516OZkBEliMI6OXMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سپاه صبح امروز با این موشک به یک پایگاه آمریکایی در کویت حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/alonews/124112" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124111">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNhuXonTKqwxN3toTvYRqWZ2hwmrEAjST5SXQJMZSafalYrLwBsjpxRVg-av-S__lBvOP1X4vj-bL6wNbIYlhrG-UfqcHvkapcWsAafIipyCnYUZDbov7LNtLo94OSMNX2JMUr61GxbC2Wymg0pJsWPCK7VOyGpuagI1q86H609WP3LKkhaUATFAw9bEyYOtuK5Y4t6-NwyoKBi7bBxPCzKMhIk7_4pOr32AmLG2FY0MaS4bcCoxMmdm3FCvMSE9l87mpZrOGNIrBh9MdpnI2w5VekcKzzca5ibVhY7FY4yIpBlfTyXmU-F3AtQnqVuZ4-A1b73wQaiWsmoNuTDkvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
موجودی نفت خام ژاپن از مارس تاکنون حدود ۷۰ تا ۱۰۰ میلیون بشکه کاهش یافته است که بزرگ‌ترین کاهش در تاریخ این کشور محسوب می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/124111" target="_blank">📅 11:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124110">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
طبق گزارش کانال ۱۴ اسرائیل، انتظار می‌رود ارتش اسرائیل به زودی دستور تخلیه در حومه‌های جنوبی بیروت صادر کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124110" target="_blank">📅 11:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124109">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
وزیر جنگ ایالات متحده، پیت هگزت: آنچه در بودجه سال ۲۰۲۷ رئیس‌جمهور ترامپ خواهید دید، سرمایه‌گذاری ۵۶ میلیارد دلاری در تسلط بر پهپادها است
🔴
ما همچنان از آنچه اوکراین در میدان نبرد انجام داده است، می‌آموزیم. ما چیزهای زیادی از اوکراین و نحوه عملکرد آنها یاد گرفته‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124109" target="_blank">📅 11:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124108">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مواضع متناقض آمریکایی‌ها دلیل طولانی‌شدن روند دستیابی به تفاهم است
🔴
کویت هنوز امکان دسترسی کنسولی سفارت به ۴ شهروند دستگیرشدهٔ ایرانی را ایجاد نکرده است
🔴
اجازه‌دادن به طرف‌های متجاوز برای اقدام علیه ایران از سوی دولت‌های منطقه، آن‌ها را کنار طرف‌های متجاوز خواهد نشاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/124108" target="_blank">📅 11:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124106">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePepZZYDEnhin8pHAcLZH9EUVUmRBLcJf7z5-nnjvJg0FqyqqDvk4IMSnlyermLPC5DPM-4g-UyAK2dv2TmkKb_xr_QdRmLgBhGCXSgbGutfaTwfwQCJgQ-_ACrVNQJ9GgpQ-pY4mcmEMfNxs-DHWuxbM0fBcpM969VFKRLDCBKCzHaXUaUvcMb_barynWSuSbHoMRh75WCuI7G4fWfhqOz03OVhcv43SMe-PlRYjcaZ-IUF4a9WBHyS7UAAWnQAApwJuBX0CZTPQzT8txy1-L0JC2-aVcY4Cj4sf1p-TfdlUtPtKNFFWAiUwDHYBjxXMqwEVBEcYHe3SbakX1s9YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به نیوزویک: مردم ایران از من تشکر میکنند چون بجای یکبار، دوبار رژیم رو عوض کردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124106" target="_blank">📅 11:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124105">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUtt9vuXKgvyKj3EiC0eBBWczpJTT4HprVfq9nULuP4O7hgx0o3jxXGmHGS1SNhxk5kkorqpdv9Ad29qS4eklyoxnjDuOg-IA5sUy5CFviQ86GfiaC79pWxBbKy9vcuqn0LOF6l4-AJCOhfLJyne73wDOFbO7vkkEmpQTrtBRQrhFPONBFllcIr1FILXIJ1eWwlq4mdHidzsJWcdqfFgKIdI1Wyz-PdiXbRBDoXoDnehdFfMPBrWBmQf3_r20AE1x8ORtc14QdBeVQ5vhMgr5vSnL30b50GCKu3w5cppNLboGb40jVCl8JkH_fUGnkBoAMQpCcG6BvMnV_ZOWhvoYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بی‌سی: تصاویر ماهواره‌ای نشان می‌دهد حملات ایران از آغاز جنگ به ۲۰ سایت نظامی آمریکا آسیب زده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124105" target="_blank">📅 11:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124104">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sS8RjXfLNZEnpX0PYr7RzVCNuVjSqRjL_dGZGRZk0ZX5kzsp9Ow80x0F_oANmeukHzfTNmgrXVs3qONMn7Zhf6tJgbrVnqWUCJIasiJEcPBEZn_7v4aD-GScndAdY2El_ytue-TBnl2_g3OmqlOSD4zxQW-wpH0npnQCCP1bFJYHQ0T2SzDxhGswpi6HNn_ucmHJ2ZhGj9JJO8TQoAGcflukbKUMC-4-21RM-4xxHqlHuSPPPhkXw8ia1_-dic8_JaT0GiJ84zagorDzUF3g5S0uJP7dzJHVVM0JivIX9IpDHTpRNF5lm_lsiDvoZeYR8NU20fuFVNiZFbTlWUndwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسین طاهری مداح: اگه دارید مذاکره میکنید بیایید بگید تا تکلیفمون رو بدونیم که ۹۰روزه تو خیابونیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124104" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124103">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/032ec01199.mp4?token=nIpBXjLE1tqkvQscGayckNPPG9VFgLQFI03Q5FlSM8sTVWwyk7NodA6MGe7SXm_JtgIoAfz-QT8RQRVoLMBKJOEtqmO_IDOsjblpNXw-ltqE5Z5tXsUbSwKGfr7tiTr5gHaTAql3XQhy9uXc5ZX2FI4HA5Ds-sFQoCw3ZP5Pmmm0xbR3W6aJyfg1nBfkVw07xl0B_n32o2KcaNKveMYjaRzMfY4B6Sy-VJRYNHRWdGrFSLpdVSkIkLImHgTfFSrBdozc3_OLE523umMcNPbwWpCXSvn-PHXOoVlLm6alPOIkXqKsFMYIptj4wOB_Re7y0LJeNnwopDlsFRbkBjsugA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/032ec01199.mp4?token=nIpBXjLE1tqkvQscGayckNPPG9VFgLQFI03Q5FlSM8sTVWwyk7NodA6MGe7SXm_JtgIoAfz-QT8RQRVoLMBKJOEtqmO_IDOsjblpNXw-ltqE5Z5tXsUbSwKGfr7tiTr5gHaTAql3XQhy9uXc5ZX2FI4HA5Ds-sFQoCw3ZP5Pmmm0xbR3W6aJyfg1nBfkVw07xl0B_n32o2KcaNKveMYjaRzMfY4B6Sy-VJRYNHRWdGrFSLpdVSkIkLImHgTfFSrBdozc3_OLE523umMcNPbwWpCXSvn-PHXOoVlLm6alPOIkXqKsFMYIptj4wOB_Re7y0LJeNnwopDlsFRbkBjsugA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مکرون:نیروی دریایی فرانسه صبح دیروز یک نفتکش جدید تحت تحریم‌های بین‌المللی را که از روسیه آمده بود، متوقف کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124103" target="_blank">📅 11:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124102">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
بقایی: آتش بس در لبنان بخش لاینفک هرگونه توافق و خاتمه جنگ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124102" target="_blank">📅 10:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124101">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سپاه استان اصفهان: ‌انفجارهای کنترل‌شده مرتبط با مهمات عمل‌نکرده در جنگ توسط تیم‌های فنی در محدوده جنوب شهر اصفهان در محدوده بهارستان تا ساعت ۱۳ روز جاری انجام می‌شود، لذا صداهای شنیده‌شده جای نگرانی ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/124101" target="_blank">📅 10:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124100">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
بی‌بی‌سی: در حالی که کاخ سفید بارها ادعا کرده که توان نظامی ایران تقریباً به‌طور کامل از بین رفته است، تحلیلگران می‌گویند خسارت‌های مشاهده‌شده در تأسیسات آمریکا نشان می‌دهد حملات متقابل تهران دقیق‌تر و گسترده‌تر از آن چیزی بوده که مقام‌های آمریکایی پیش‌تر اذعان کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124100" target="_blank">📅 10:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124099">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
سنتکام: در پایان این هفته، در عملیاتی کاملاً دفاعی، به چندین مواضع جمهوری‌اسلامی در قشم حمله شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/124099" target="_blank">📅 10:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124098">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
نتانیاهو:
به ارتش دستور داده‌ام ضاحیهٔ جنوبی بیروت را هدف حمله قرار دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/124098" target="_blank">📅 10:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124097">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
بلومبرگ: گلدمن ساکس ریسک‌های دوطرفه‌ای را برای قیمت نفت پیش‌بینی می‌کند، زیرا رکود در تقاضا با کاهش عرضه ناشی از جنگ ایران در خاورمیانه رقابت می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124097" target="_blank">📅 10:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124096">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
یمت نفت صعودی شد
🔴
قیمت آتی نفت خام آمریکا ۲ دلار و ۲۹ سنت معادل ۲.۶۲ درصد افزایش یافت و به ۸۹ دلار و ۶۵ سنت در هر بشکه رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124096" target="_blank">📅 10:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124095">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
فوری / گزارش انفجار از بندرعباس
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/124095" target="_blank">📅 10:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124094">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FNV93iVQ6rBbIBns8UGF85l_e7ioF7s0YrZzBhrgQoz3Etz679rS4z1H0j-CBc8FDKrjEIrPvEEHyz85rXXi54K6i2dKwalFd0BqslgX_2DaYrR6IWEUiEdvMp8bRYJQsK4CL8_E3o-zd1WH12B0TVWW7CRF7TbzyeQzwBia8RWz7OQ3juAFx52e20v4_FkwCslzmtJ7AVneysyJDQt69swIEIspE0t5lRhD1d2Y8obFHwidgycJTDGZcuzlILXZvERUpOo0yhi09H9WMW4jXSeG2aZq2i0piW9Qkx5Xhh98TuFwUPqSgoTIBhOC1P63N4tS8avt-jsrEgpN-GPFyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇦🇷
👤
تصویری از هواپیمای تیم ملی آرژانتین با شماره کاپیتان لیونل مسی
@AloSport</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124094" target="_blank">📅 10:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124093">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سخنگوی هیأت رئیسه مجلس: هیأت رئیسه مجلس، تصمیم مثبت و موافق خود را برای برگزاری جلسات به‌صورت رسمی و فعال‌سازی چرخۀ قانون‌گذاری اتخاذ کرده است.
🔴
مسیر هماهنگی‌ها و مقدمات لازم در حال انجام است و به‌زودی جلسات رسمی صحن همچون گذشته، با دستور کار مشخص برای قانون‌گذاری برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124093" target="_blank">📅 10:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124092">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1NRz3H8sQD0L-gNoGqNugMw5PlXT8u6YQczHVBheT0EpwXxIS1uxyvirktKffn6AxhaM05OyTvb7ldAxJHZqIL7onomJovk8PmmCrxxnj1BjuZZuwtOvJEzTARKIV5N3OUkM0-hfckEQn6zAQnJyZ2qKzyv1S4ZEKgzdU3oWcDxQY8s1BAtkyykMqa-eUJwHb254Vw7XPICBWyOJmuxu9NZ4VNKOiDqtPK_HNXPLnZcz-QrKKq4GY85tNMzQ_BOW5eN9EuPtuppOYfpvwiIigf0ScAPv_t7yf1KoK96GFPb4WkHSTlhxt5n_6kr4GHTzmtm3q73IDhBOWJR4qDgog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حاج علی دبیر:
یه مشت آش و لاش مخالف حکومت هستن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124092" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124091">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQ7g1GBtVDHgRHcaz3bbVSAusMdortbxW8NvVSNiGFc1uxqehzmqPfUM5qyw8TdroyCckUfdSVI6UzveBpb38kpYoveopWtj4dcrSx3mXRzJ8vN9l53_OB8YOBclsWp_3pO2qg5xdVKWEYoi3lRHMMmS3GCUdlxp2jMWveTqlEZnGUJyL9zxHDDB20bgajQ7ex74soKQlLQ3yhqKzV_IxCcjqXWfNnz6K7DZ57qqEAOKDuu4DjTOzF9eCyXfzjg0SD_vuhyYZKc_HdbRMbAdpI07x2HX6h2UPnRYucgWG0FzawzdVkczQoucjvyHoPgLIthJP6JrZnPgGb3SzOr1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازدهی بازارهای ایران در یک سال گذشته: طلا اول شد، پژو ۲۰۷ دوم، دلار سوم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124091" target="_blank">📅 10:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124090">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
کانال ۱۴ عبری: امروز رأی‌گیری برای انحلال کنست  انجام خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124090" target="_blank">📅 09:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124089">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سی‌ان‌ان‌: دور دوم انتخابات ریاست‌جمهوری در کلمبیا، دو بینش سیاسی کاملاً متضاد را به مصاف یکدیگر خواهد فرستاد
🔴
«اسپریلا» که در دور اول بیشترین آرا را کسب کرد، به طور مثبت از ترامپ صحبت کرده؛ این انتخابات نیز مهم است، زیرا می‌تواند روابط کلمبیا با واشنگتن را شکل دهد
🔴
با توجه به نقش کلمبیا در مبارزه با قاچاق مواد مخدر، نتیجه این انتخابات در آمریکا تحت نظارت دقیق قرار خواهد گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124089" target="_blank">📅 09:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124088">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c15xJcEMIOo39tGBBaB918hXtPzdcS7Zr_9NR9x3NNBgR_KUEU6b-gbJGRI6b1fzJhQu2fYfiPTjItZEOM0iaku2Lk9ysvA1HWKrJXPRhVRgCqjCWlJkTculpZ_6zq_WOeqwM9QI8AtsuGZDC_38H7OL_8i7eTGuG3EHXHzbhMYq_-zxHqaijn6NXnBfK2F8oT2eUIJGgX7mE7zsbNryDgbY9lc1Jp1I5bH-gZJKDCPRtR8gwkHUOgDwdxGYzaGS7ygRqsjwAZbJhgcCDGuC3QeY23p0kTcogNWfaC2GaR2IwNLOn4TyyfgwltgWm7uJMR4F7mgzQYFLLRrM1_xWYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اقتصاد چین در سه دهه اخیر پیچیده‌تر شده و رتبه آن در شاخص پیچیدگی اقتصادی افزایش پیدا کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124088" target="_blank">📅 09:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124086">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nWIbVqGKHekxTM_5bYSzmURiZGQvzaHySBn35iQKItrg1mAIcInN58PbZiT-v_gAlWPCk7RaczXAeyJ14hpA7ovnRtC9vzF_FGnReGk25qxX7v_V7gh9PvatSiFNtU8VcU7bUg6EamNOTLVvw34YNpaCojcBnU7cq4QrfdMRcLj95AsayH5o27tQnEtlBlGDm7vZmvieaOUwQFZAe1OWo_2MHilgxS1ZLe1TWTZeub0ig9jZZgb76AoIfOR-t56vecxe5oYXs9ZprwWSf9eteneVDUE2gaUtu3QbQhMreh_KPo0sPY6tIiQuzEClEMlYRSG8jfmbKn1U-hCOysa5kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/R8D7ZAbMLl7zvCpHjAFEDp5DP5VvjCkVlt9csF7JQzjQtyuKQ_JMvm5WvxMNoj9KZtSYNs-9h8xZaIDQvul24ZiutTuKBNKZfaoyCzNO4dWLvSFfyPPiii0Mpgzc2E-y5h-AC31dqP-wwDa1Xt_ru1gQE-NZwBwQyTHHcEY20y-infPhu1JsUPG8xyeceJjcZJGi5fagz69GDY-WJ1wh8u2pTrieke2NOg5UColNQJMYuP3zxf8mSvFvdjGmhmhtR7EI_rPHNpEP1WZ8B0WvDItEXxBx8NAQViRgYEPwnCyNXZZ2lW4ry9AiM_Uf0ppAxXMS79X4sPox-7R8mfKiNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره ای دو روز پیش ، نشان میدهد که یک نفتکش 252 متری توسط 4 قایق تندرو مورد حمله قرار گرفته است.به نظر این نفتکش به صورت مسکوت توسط نیروی دریایی آمریکا اسکورت شده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124086" target="_blank">📅 09:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124085">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbfTBLOGYTUdFGdLhOJYTuPBan3rRzG_t9RHq6yzF7BvU5oKCElivLU7caZvcrjH1f-yKCJOSrBEL5VujiLEaP2KD4bt30VqJdZmZf2CuPKDwW_e-i7LVgNm8q-nhuQbFaQq2L5qcGf6ZRG-xQSPAb9CJIManBJG70rrqigh0p7C_BA7f0GGNEPsbbUrjNKahS1qWLjama2xSLviad9yxlDVnwCG16S6nVL5PIu_9NUloQm3HFxgiHxPvOrd4x_q90kf1ey3e4rQBbKbI2-hlbWh4LXnU1JkFKxaTblYmfZYc7ZraRAXJG9EPdGFoMhZUXnnCsoA8m__YOmz0KV6FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تسلط چین بر مواد معدنی کم‌یاب در سال‌های آتی به کندی کاهش پیدا می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124085" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124084">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوری / گزارش انفجار از بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124084" target="_blank">📅 09:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124083">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJTzH4td__ZmrG3WHMTWOypXNw-_KBjQ-1rSQ5Ux270VO3R2ujAz4qtez8CcCgnvaP0zAfQidf2vaxj_EcbSWlWBrC6HEUCXIcw-4Le3hfF0jPTr4uMRxPvrwx1YuWyVU7hswyLKx8BghF1yy4rLtDdZ-da6OFQLSHkcgCZr8Tm2-aaRoNbgan3M_HjV3bqXvsHB6rAOtLaoXgJhXu8wLiqisUHm8VD6v_vWWHhR1LE7_0jdXWGjnjPTFMjwx_hRIdP4-grhySsNN5QA95V8ErYZUTHJ-UMlTxqJ6GlzWvgaA7nvoLEZE476v7o_LUfs57ToAcybTdkhzwIE0_KaWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس جمهور لبنان: ما با گام‌های استوار به سمت احیای کشور و بازسازی نهادهای آن حرکت می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124083" target="_blank">📅 09:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124082">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
عضو کمیسیون انرژی مجلس : افزایش قیمت بنزین در مجلس مطرح نشده/ نیروهای تعدیل شده پتروشیمی‌ها به‌زودی به کار برمی‌گردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124082" target="_blank">📅 09:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124081">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ارتش اسرائیل: به ساکنان شهرهای ملیخ و کفرهونه در شهرستان جزین در جنوب لبنان هشدار تخلیه داده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124081" target="_blank">📅 09:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124080">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
جوزف عون: لبنان با تجاوز وحشیانه و محکوم‌شده‌ی اسرائیل مواجه است و ما با گام‌هایی سنگین به سمت بازسازی دولت پیش می‌رویم.
🔴
ما در مسیر کار برای پایان دادن به رنج لبنانی‌ها به‌طور کلی و جنوبی‌ها به‌طور خاص، و نیز پایان دادن به عذاب‌های آن‌ها ادامه می‌دهیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124080" target="_blank">📅 09:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124079">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e2880bbc.mp4?token=IVGl0_Do-0E40bRK_QwQBSd7tMqvLUVyrPX3qfjz3TjKP0DB-uapbU8PaeOITryKa3s2utA3xTb7kKWOUyzUKxoc4fM1686fXx6_gqJIcJPmKdoWjpOzUCWmY3KtumuaTeNb6jkCn6ftKtZnd9TzsHIvoeU0iupyoOG5W8UTbQ843f1YLqGOZ9L5ZmO6JRnKxmtT7D8sBWAoboQ6R_Gxw7mgDktogsJoF0yVV2WNS8_5V604ZExXZDM4rg6CBZkvt-uPDWeo2IndK6PqAADDK9DOOGa7wdo5CqJGAtbsKch7H0KXpmXH9v-Zw0GrrWPeRyH0gbDZx24KJHK_kIlf3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e2880bbc.mp4?token=IVGl0_Do-0E40bRK_QwQBSd7tMqvLUVyrPX3qfjz3TjKP0DB-uapbU8PaeOITryKa3s2utA3xTb7kKWOUyzUKxoc4fM1686fXx6_gqJIcJPmKdoWjpOzUCWmY3KtumuaTeNb6jkCn6ftKtZnd9TzsHIvoeU0iupyoOG5W8UTbQ843f1YLqGOZ9L5ZmO6JRnKxmtT7D8sBWAoboQ6R_Gxw7mgDktogsJoF0yVV2WNS8_5V604ZExXZDM4rg6CBZkvt-uPDWeo2IndK6PqAADDK9DOOGa7wdo5CqJGAtbsKch7H0KXpmXH9v-Zw0GrrWPeRyH0gbDZx24KJHK_kIlf3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی که نشان می‌دهد نگهبانان مرزی اوکراین یک پهپاد روسی Geran-2 را در نزدیکی چرنهئف با سلاح‌های سبک در فاصله‌ای نزدیک سرنگون می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124079" target="_blank">📅 09:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124078">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سنتکام: فرماندهی مرکزی ایالات متحده حملات دفاعی را علیه سامانه‌های رادار و سایت‌های فرماندهی و کنترل پهپادهای ایران در گوروک و جزیره قشم در این آخر هفته انجام داد.
🔴
این حملات در پاسخ به اقدامات ایران از جمله سرنگونی یک فروند پهپاد ام‌کیو-۱ آمریکایی که بر فراز آبهای بین‌المللی عملیات می‌کرد، صورت گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124078" target="_blank">📅 09:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124077">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqXAiz9WQOJ7vYqS02Uf1C31DoSCHkxXnVhFT8YrBGAtDy-M7YKlDdbA3_zSspktEf78KPHgXR5CZ_MSOaeT1JdRRtcqnmZI93Ics4l88ljyTNO9uxFKjvEFUCcIMWOtTwBgR7zmVPoY0qRaVEnOyPEyPQ3xmko6auRutZswghGw7u7EP5DcNtaHUjV51paEPtLFvARNCYkgvsB6kJFCz69psXTUsNqDt7BQwRtJp5yLhxA1S7qOUq-HXHPDQt31jxU9se5gZjs3JVuvAvNVGeAl1z5vbS8Xx5WHHKPhVx3GpB-ajQjL7Fl_ZBbSlseXYHl__Ssx9u8b9eqLeg6cZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: «ایران واقعاً می‌خواهد به یک توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
🔴
اما آیا دموکرات‌ها و جمهوری‌خواهانِ به‌ظاهر میهن‌پرست نمی‌فهمند که وقتی افراد سیاسیِ فرصت‌طلب، به شکلی بی‌سابقه و بارها و بارها به‌طور منفی اظهار نظر می‌کنند و می‌گویند که باید سریع‌تر عمل کنم، یا آهسته‌تر عمل کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست وظیفه‌ام و مذاکره کردن برای من بسیار دشوارتر می‌شود؟
🔴
فقط آرام بنشینید و آسوده باشید؛ در نهایت همه‌چیز به‌خوبی پیش خواهد رفت، همیشه همین‌طور می‌شود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124077" target="_blank">📅 09:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124076">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ثبت نام مصاحبه آزمون دکتری تخصصی دانشگاه آزاد اسلامی تا شنبه ۱۶خرداد تمدید شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124076" target="_blank">📅 09:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124075">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJpZGmNoP3UzIDGAEeAfXTn37LSGCzX5NPUmlTM8M25OM5A_8WYBOQveOL22qjibRffskRY0_SpiUx5FXWrvSZYyo_jdbpo6CpvLQuUVPwy9ETWi5tdvbR4vMiYlH94_IN4aw1BHR2qjXGGAAKkLHfSQo4N3mvhzQvBlQFdDmBYLxmLY1uBC8bLMt8lJfjC3hXrtGS_REJGHmdhPdvJ2lgfvvkzIT15R2970OCUiiW2H_1xRnYHsMha0r2WOIl0EF81yiIA5eu052rVFWx0aoM9Ve3gWXu4_Uu06k5vnHPgWRuPNKugmWIQ0dKsnMl_r9klh-KjJ6mQ18paCb0rBVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: آمریکا در هفته های گذشته موفق شده ۷۰ کشتی را از تنگه هرمز عبور دهد.
🔴
عبور کشتی ها با پشتیبانی نیروی دریایی آمریکا و خاموش کردن جی پی اس در نزدیکی حریم دریایی عمان انجام شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/alonews/124075" target="_blank">📅 08:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124074">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از مقامات آمریکایی: واشنگتن معتقد است که خطرات ناشی از ایران برای دریانوردی در تنگه هرمز اغراق‌آمیز است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/124074" target="_blank">📅 08:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124073">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841be8439d.mp4?token=E_xmT1crRC8rBTHjRmeamp_C4xhUC0NUzPbBczO09PRwQ671bTBFgShr67gDGFrdkkPd2M962XTsYugTM0EA-9DreWzkg5oaPIKaNefqlK2yPAfeX4ZaHZsMIoIJ_P82nkuQ4TkLMF4hwXuxQfDg33lmrQWZXrqybI4ITr4z8zexQE6fO6NXBsrczvsJOnhRLCzSk0YAy4oxLR_e2VNYJ1xPccDQmp0soJfncXTTsSuzSh8MtLp4HqGOPCbrP8EbUP5SP2zK6xdPak2KlYV15jbB7DdJyntVMWhmsJoUfx4prsh8FlcIyY-fytDk-Pp-FedwxtH8aT08sUsEAKgjwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841be8439d.mp4?token=E_xmT1crRC8rBTHjRmeamp_C4xhUC0NUzPbBczO09PRwQ671bTBFgShr67gDGFrdkkPd2M962XTsYugTM0EA-9DreWzkg5oaPIKaNefqlK2yPAfeX4ZaHZsMIoIJ_P82nkuQ4TkLMF4hwXuxQfDg33lmrQWZXrqybI4ITr4z8zexQE6fO6NXBsrczvsJOnhRLCzSk0YAy4oxLR_e2VNYJ1xPccDQmp0soJfncXTTsSuzSh8MtLp4HqGOPCbrP8EbUP5SP2zK6xdPak2KlYV15jbB7DdJyntVMWhmsJoUfx4prsh8FlcIyY-fytDk-Pp-FedwxtH8aT08sUsEAKgjwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شلیک موشک از خوزستان به سمت پایگاه آمریکا در کویت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124073" target="_blank">📅 08:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124072">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
آکسیوس به نقل از مقام‌های اسرائیلی: اسرائیل از دولت ترامپ خواست مجوز اجرای حملات گسترده در بیروت را صادر کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/alonews/124072" target="_blank">📅 08:48 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124071">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
اکسیوس: آخرین تلاش‌های ایالات متحده برای برقراری آتش‌بس در لبنان با شکست مواجه شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124071" target="_blank">📅 08:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124070">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ارتش کویت ساعتی پیش: پدافند هوایی «در حال مقابله با حملات موشکی و پهپادی» است
🔴
اگر صدای انفجار شنیده شود، ناشی از برخورد پدافند هوایی به پرتابه‌ها است.
🔴
به محض دریافت اطلاعات بیشتر، برای شما خواهیم آورد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/alonews/124070" target="_blank">📅 08:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124069">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا در واکنش به گزارش اخیر سی‌ان‌ان ادعا کرد که توافق با ایران به وضوح بیان می‌کند که ایران سلاح هسته‌ای نخواهد داشت و جزئیات گسترده‌ای از جنبه‌های مختلف مرتبط با پرونده هسته‌ای را بررسی می‌کند.
🔴
ترامپ رسانه‌هایی مانند سی‌ان‌ان را «دروغین» و «فاجعه رسانه‌ای» خواند و گفت که حتی با تغییر مالکیت جدید، احتمالاً هرگز بهتر نخواهند شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/124069" target="_blank">📅 08:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124068">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
فیلد مارشال ،محسن رضایی:
با ادامه محاصره دریایی و مطرح کردن خواسته‌های بیش از حد در مذاکرات،
ترامپ‌بار دیگر ثابت کرده است که تمایلی به مذاکره و توافق ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/alonews/124068" target="_blank">📅 08:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124067">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_d7OLPo1IKrEacIxaPGHwbel2IT7jx6OeNGkCtU-JsRLcUEJf-w3zAGMgvn4CVjbv3Mm_Bm-anNYAXZ_7v9JJZzE5CBydXKgG-uh5ttYiKXo5LE73ynO73Romy3J7Tw6wloAZ8poqp3T_DeiFrJJFZqVGz86hkazhVt2Hm1KNSo3xzY1JXd4A20xNWcDLgqawlCBx027akIRvlbMEq9D_-XDJ037ZQyT_RBtU-utMOyJ4UILBHGjJOxXFrpwN2Mekorao0r33RPzD-dRFN249DqMAYItVTvYFsblhCrkAu9pFLl8uXhiterkH_4shN9rZT0z2ApjON5Gy-QwS9PHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری ‌CNN اعلام کرد که ایران اکنون 50 ورودی از 69 ورودی تونلی را که توسط ایالات متحده آمریکا و اسرائیل در 18 تأسیسات موشکی زیرزمینی مورد اصابت قرار گرفته بود، باز کرده است
🔴
تصویر متعلق به یک پایگاه موشکی در دزفول است که چهار ورودی از پنج ورودی آن باز شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/124067" target="_blank">📅 00:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124065">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SGfKgFN0Po3sjzNOH1fLJiZPkfi9UOMKCJm15Dds72KjQ4VPyByYH_sp3ut_hiX_cQWPa_BTM2qro2vnDMEgZKezTHvXW8FaYPfzudQrd-ldG-sARYQrHrd5589fZFdqC4v3gYJu-apbP89wu-RbSfmen4jmKdf1u0PEQftVt0Y-cUXJ0YjWoxuyS4s5FM7NeIw9jixfqzVScUGx30bOIHgdM1fQvilhU30hfepphIbtKDMB6yd84Xmcdvmit5ShbcpR1gQrDRjl5RI6UIexacQ2ASK8G3qwD2GyHi2nPo67V47bz1lX9tWlr1uLXuQGF-gkv5A9gcRlG0h2QJFH7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tz_9QT8D4bjy2nTfhXqzaIRAUbNDCNv3hVN_Daeyrkq1ms13nIH-RLzmYEMjz7weW2h6KeCebK0uJcJXTxA261RAkoLQB6ndL57FJfhtUx4BfqjsQRQ9ounVp7cACQn__R2OrvraHAVS3S41igk2krrYWaWmExIlIKCH-RVZb4VC7SZifa_v25D5G7dUvTLehj-6vXsAionEgp4-aQlXC98krZrPvX7wlYGL0F9Cr0oMkkU5TUxi1gihN1xWtCQiozp2-b7no_jx99bJH9e3ZDQyLVXaqId2nSX9yC-KoqORfhL_TJiSWiQK0lp8Jmd54-RGc_urNhAgxnt1XK1zhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
رژه روز اسرائیل در نیویورک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/124065" target="_blank">📅 00:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124064">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d26430ec32.mp4?token=XyBbNMg0k_juENm6SuKlZayb9Dw9KSIzwzmSkQm-yCzkSVIYhqu7U3PyzRZ1LLw7ir5VT4U1UqesX3WWnDWu7rApG1ZPmIrECwQUVNGvfYoaEUFSIZeoP5mlDLoTXNCnwCn5EWP2qktKf0F0lf24PInMaQ0hQRLVpTe9vIBG2JAP66HIhf-XRHr8-2llxritbPbS3H09WLVYGRO3BUgHjIdb_s6MX7iLNMkJhdE4Rv2cGHAYNPsI3gfn5WmCPZqRTYjRi48xRSafyJIFPJigaEysQejzq4Tk4UfbpZ0k3F4vkAItmZ12HKOUhXbZKLe94j28HSljMWKKAmHWMerOew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d26430ec32.mp4?token=XyBbNMg0k_juENm6SuKlZayb9Dw9KSIzwzmSkQm-yCzkSVIYhqu7U3PyzRZ1LLw7ir5VT4U1UqesX3WWnDWu7rApG1ZPmIrECwQUVNGvfYoaEUFSIZeoP5mlDLoTXNCnwCn5EWP2qktKf0F0lf24PInMaQ0hQRLVpTe9vIBG2JAP66HIhf-XRHr8-2llxritbPbS3H09WLVYGRO3BUgHjIdb_s6MX7iLNMkJhdE4Rv2cGHAYNPsI3gfn5WmCPZqRTYjRi48xRSafyJIFPJigaEysQejzq4Tk4UfbpZ0k3F4vkAItmZ12HKOUhXbZKLe94j28HSljMWKKAmHWMerOew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این 2 دقیقه رو حتما یه جا سیو کنین و یا بفرستین پیوی رفیقتون که گمش نکنین! هر بار این کلیپ رو باز کنین مو به تنتون سیخ میشه که طی این چند سال چه اتفاقی افتاده!
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/124064" target="_blank">📅 00:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124063">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d653bc80.mp4?token=B2MLw4E5u1xQjMt9NWNddwCDmtQUPgPkiOqT6h7iSRnpfVYUizhbASzsoL4dKx3nXUxMl7HmUc6PLs1qvFfwyKttH5biWi3K9iCI_ZUfZ_SDbyNw3XZqo_cpiz98EIwrnXRev0wnSRZH1c2OPxCgPUfnW7EvXSbYwGWbHa4UtodvhwdBE3zJqoo21enS3IsJ-NXxCc1n53BTL02qRe3pVRqUSXw3Wr-v5z_6R-JPSLISxvW5cmUAafzBmBdUXgSMAs7xBGVJRSU_a1f9-3cpWb3uSeSezCYgCcf5u6NM5BNZkwupwNiXo1rh3SMijOzdRtcuzWWPpcb6Jsp9b-LfKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d653bc80.mp4?token=B2MLw4E5u1xQjMt9NWNddwCDmtQUPgPkiOqT6h7iSRnpfVYUizhbASzsoL4dKx3nXUxMl7HmUc6PLs1qvFfwyKttH5biWi3K9iCI_ZUfZ_SDbyNw3XZqo_cpiz98EIwrnXRev0wnSRZH1c2OPxCgPUfnW7EvXSbYwGWbHa4UtodvhwdBE3zJqoo21enS3IsJ-NXxCc1n53BTL02qRe3pVRqUSXw3Wr-v5z_6R-JPSLISxvW5cmUAafzBmBdUXgSMAs7xBGVJRSU_a1f9-3cpWb3uSeSezCYgCcf5u6NM5BNZkwupwNiXo1rh3SMijOzdRtcuzWWPpcb6Jsp9b-LfKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مسعود پیاهو، کسی که ویدیوی مرد نشسته مقابل موتوسواران یگان‌ویژه در خیابان جمهوری تهران را منتشر کرد، به ۱۰ سال زندان محکوم شد.
🔴
ویدیوی این مرد که در دومین روز اعتراضات دی‌ماه ۱۴۰۴ منتشر شد، به سرعت وایرال و به یکی از نمادهای اعتراضات تبدیل شد.
🤔
دم از عدل علی میزنن ولی به معاویه گفتن زکی
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/124063" target="_blank">📅 00:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124062">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6v4tZACRPCJ_MqQOh2BE2WahPVH0hf4K2bFQMjNOTTV92L7icpguCNLiGD1JirTBlB9kcAh1lBCIHtqPDIlwbgAzhMHGkbSFRojbiLSd8za_bTB5EaOWN3Eck8Xs6Rfps2sy72BlS4r-Q88_TO2VBSh_Z3daTyjVATlsw4WvLtPFYHMiDipmjeLeHa88SM7CYf4yHzL5pjfx4aRSmjwngvScF3m5_P3X2tvYAkm2P_wUCo9Eb_cViq5XIgE1kqISdaOUTkagykTEXhG4K8RiHPK8Kkj-NNyTr54-HawUpQhyLMepwE9-dqw7-a5epK2FSwNpfflOuK3uQsnwTGqMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حمله شدید عارف غلامی، بازیکن استقلال به محمدحسین میثاقی
@AloSport</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/124062" target="_blank">📅 00:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124061">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
نبیه بری، رئیس مجلس لبنان : اعلام کرده که خلع سلاح حزب‌الله را تضمین می‌کند و قول آن را می‌دهد اگر اسرائیلی‌ها حملاتشان را متوقف کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/124061" target="_blank">📅 00:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124060">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyYvTlHT0LgNTtn3H5ifers6h_uXt_fFTvgncCsfWOD0ogA2Vf8ixj32aH8hTZsbpzimBGiLZ3DelhZXu-cFl5QnzAOsWPt2CsbwIQO-cQNKMChCk5VK9aaYWESxrRS6XbO9Q4nS2fn0_jwy2EZqQzpawUvGqwtH68Vq97R6moj7ZKdQ_L7q-a5y74Cld9zSOa7GYfuL3CVBg71l68J6nCyojJ3nkVmkGAXikc71k1zwNMN9oEbQ1Gj7t_FCF4CMPR7s3uCfPMXbWvBNAPdJZrwCwwpcjohSxjYScgaL6Ez1UYrBcgW59w5V7wz4hixIB0qTQf4f9W1NwO0eUXLl2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین تعدادی پهپاد انتحاری به سمت روسیه پرتاب کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/124060" target="_blank">📅 00:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124059">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxv_IVMIrcQyyRKgk4lKQbKo0JUtto8mGfmVTsb7Fv4hnsG29sAmTRMjbQI67v7UrPVeS2w5WWP5aNm13UVzVBOxxPE5vLzuJbulKDnwsyzkWLfxdXQd-xYobBvgcF_NenO58GyHB21mAoFOtjKeaCxZNzyTEEvKJdJKiZDs35-wjl6ZxdleSN49Ci-MOposhANuIgl7XwHkPNzId6ZPdrs9ZZ2gzAG6dyXLBBsthctag8taHp_cFxTeo_utYTMdqStSqC-6tUATAnXUyBGswODQo7ezF92YR5ydNnhUGgmul4Cm3Ky9RnZQ9qaZDgotkhAmjjyTzktleMCLN9skUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی: اگر نتانیاهو در جنوب لبنان متوقف نشود، اقتصاد آمریکا در ماه ژوئن فرو می‌پاشد، زمان در حال تمام شدن است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/124059" target="_blank">📅 23:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124058">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
شبکه خبری المیادین گزارش داد صدای چند انفجار در مرکز منطقه کردستان عراق شنیده شده است.
🔴
هنوز علت انفجارها مشخص نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/124058" target="_blank">📅 23:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124057">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTXVNW2SAjwyTHtBH6WRVOaosdaQMgg_khdDDvhQyX3DnZYeYxSzjjf3uQCpsSGljFUrKQSglQx07uSiRYGPp0eUNmsMSwrUN68F8Jg5qw0_TqYUjSR7aBlPgbKM0qY5Rw2AksJsr-Ck7F_TOS0wKNiVY4Q5ob8XgnNRMhgVfId4AI4B6-V2Zwwx19Mm8GwIY9S-faoToLSpHF3JwOgNr6x1uJMqb3bdU0c042sbvQcpIy8L2pUiFHxum8Vfw4t2gK6lSshU5a4e70H85C32cLn7LlJAce789o8DdiCpt0kMkV7gTBLqVjMEifUnz4VoDWN7jH5t1zEjeeVyiD7E-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکرترکرز: چهار نفتکش ایرانی با محموله ۷ میلیون بشکه‌ای ظاهراً به ایران بازگردانده شدند
🔴
بر اساس یک تحلیل تصویری، ۴ نفتکش شرکت ملی نفتکش ایران با مجموع ۷ میلیون بشکه نفت خام در ۲ تا ۳ روز گذشته ظاهراً برای خروج از آب‌های ایران حرکت کرده‌اند، اما به احتمال زیاد مسیرشان تغییر کرده و به داخل بازگشته‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/124057" target="_blank">📅 23:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124056">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
انفجار گاز در مجتمع مسکونی فاز یک اندیشه با ۴ مصدوم؛ احتمال افزایش مصدومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/124056" target="_blank">📅 23:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124055">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ماکرون: ایران و آمریکا باید فورا به توافق برسند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/124055" target="_blank">📅 23:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124054">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5SpUgCX4vw4-NfhOUpCwlsfo5orqC8FX7tbe0WzciNtRcpLmB2VRCCqzvEXRB5UnMqoQbOIGCL6p12WP8htTdTEAz2wwX9efModMnvvvt9kB57xWWsgIVq7SG1oTLj8_tKGONZd7Jd-r2qcVhzKN-73azafkSqdqtrE4V2k_MARAdbQZnld38ujmEtqchsrCQqKK5A_YBm33qpKN6o_WxLBag8noHOFs3k-FcM-pNb-z6PyFnrbTfnm2AOXWxQ7LGLW34L72rb13Bu7P7aKB0IjW2Om6kVX_DnE25Jj_k4bANT-Bx-5tqusXTvPge_zR2-MxW_1_ht1vcHu50XYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: سه ماه پس از آغاز جنگ ایران، تقریباً غیرممکن شده است که روحیه صعودی که بازارهای جهانی را برای دارایی‌های پرریسک هدایت می‌کند، کاهش یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/124054" target="_blank">📅 23:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124053">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHPDzGBAXx6ZhwpARsHORZ3i3euFfGJ3XFZIJiRlRcOMiJ3Wvh971N9UUPpUYAHcGclFtL8CrGdQYglJMINwgaOq41kUCevLGrhVCEdu4g3gdrmWLYtHIv0hs8bmpZiiJzA_JO46cyflyTZv8PBXWBS0LoNYZqOa0oULg-L8F4XbuNXJ9QXHp0ldtlXIxyJwPDf1YXyt2pv7acSI857f3BiPVUP78rAVYElo8C4Ztt7JOiAqwuu5PIGlKXBExXyKmfZFhrcYuY9qeWsS-2A5187Ga2zehcxCdxgzrxcQdfJR0x9A841UxPuQBZkvrZ9e-S50u7l9L0uqHTiDMJ0kAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت تانکر های سوخت رسان آمریکایی در خلیج فارس
🔴
همچنین آواکس E3 نیز بلند شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/124053" target="_blank">📅 23:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124052">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وزیر خارجه آلمان: پیشروی مداوم ارتش اسرائیل در جنوب لبنان نگرانی عمیقی ایجاد کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/124052" target="_blank">📅 23:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124051">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: به ساعت صفر برسیم حتما نظامیان ما اقدام خواهند کرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/124051" target="_blank">📅 23:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124050">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس: ما هیچ تعهدی در موضوع هسته‌ای در مقابل طرف آمریکایی نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/124050" target="_blank">📅 23:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124049">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ایالات متحده شهروندان و شرکت‌های خود را از استفاده از خدمات ایران برای تأمین امنیت عبور از تنگه هرمز منع کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/124049" target="_blank">📅 23:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124048">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
وزارت خارجه قطر: دولت قطر استمرار تجاوزات اسرائیل علیه لبنان و گسترش نفوذ زمینی آن در جنوب این کشور را محکوم می‌کند.
🔴
ما از جامعه بین‌المللی می‌خواهیم که مقامات اشغالگر اسرائیل را ملزم به توقف تجاوزات خود علیه لبنان کند.
🔴
ما بر موضع ثابت دولت قطر در قبال لبنان، وحدت، حاکمیت و تمامیت ارضی آن، و حمایت کامل ما از تمامی تلاشهایی که ثبات و شکوفایی لبنان را تقویت میکند، تأکید می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/124048" target="_blank">📅 23:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124047">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3wirrJXcU_Beql_MUcYepdVjWP7RxzjZhRFxEKEsU3LxNZ7KXJxMqed320lhFuTpC_tiRSmQAddY_HvbwGpgq8UiDUvZeOXIwNvHOGS6BPUMOVWFfjBW_EMSdZV4Bx649AXANxP4IaXbhbAodwH9IYhdOpRBD8dGInr9YEjPgdtb2dD6-70m5e42yr5d6Pg5xCGy993qlYWz012C5I5Qu-6leRIsykEXqfnc2KoZa20idt3pNDXtfwErv8HHeL7WZ1cROJmY9Jzwmenh047eEU3KvypgshKOYZgDE1clDWU4og50NZX-E5jMr91JmbjeeQ1Wlv4KjNHQokBlywbsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فارن افرز: «ایالات متحده با این فرض که قدرت آتش برتر و قابلیت‌های تکنولوژیکی‌اش می‌تواند یک پیروزی سریع را رقم بزند (و از تکرار باتلاق‌های گذشته جلوگیری کند)»، در ایران «به بن‌بست رسید».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/124047" target="_blank">📅 23:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124046">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mcio1xduzhbPHgp3j8fixlUBowbsOAJ1x0uX_hE5eyhyLex_PDIWEaAfWrNhgl4ChAaaOHtL1HVWSxoHqBRUMgLv2tz-FWVD7Az3et11aD7WxzROoVEOM2b4C8nMff2pt7xITrW2RHpOoCiknFqmTT4B_vaKCTYynIdRdgscfOwrhwpwfjPDKo2SRRLAX173x9m0jDCGSs5fP6YcHPkG2lteSD7L9w3NTL9rRpxxufZn-aGI7Duiy8tb5QcFY6y1EnNoIvvLdiGaYc16q8lzzPkwzJCKK44KWu1NIMVwSwU16y0paxuhfJfi_RMkIj0BZGi6qQJzZeW9Y7pldmoeMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/124046" target="_blank">📅 23:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124045">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_QmhmLMeyjq9e_Z9sDtcY-0FQeDKGvSQ6n_npJ5vyFKHkHX2QhRF1HuG8rY8q98S1U9IHozYsvXsSXDrO6tbYt8TtSg2Xvc340a328_PgYPc2-zNruq7-6EIYM3-yvPrXwLnJFHFiur_HB9iRbN86-VypCZGxMsmZSQGSwowwacf2QvbAFqmVfgFnz5Jf7FjAL6CPM1IzyDkv_PwRLGYpG5d5pzMWJrycea1bcqDy8YiiKTCwHv2pDnMdtEeGFxG8u53MOMpREz2gmKeGINgACOdhZxTrK2RqEwMf4DtVy_9g82QwdIXb_PIBGTTQl2jkAig2kBEfrzG1-uCp3iWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/124045" target="_blank">📅 23:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124044">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qot7dal1QR3k0LkwA99N7qr6-NSueiryWwDkt5ke0lgFyOUvq33TsxlA6O6tkdl3taF50dFBHjavI8RhRZcAXIkT_PN1DfBP-7STl1urepw6OvtMPmr-IPoxFv6dzvlwTSDrtIUhJeMBTroM2AJEcSyCdK4kXWh9PRHB8oQbDhq2nudOM57NYDDitRRGKKhg-DyC_IjvSUqax6--eZDzIuYEn8a3sg0m_vxO7R3etpTO0D7FbOk3I4WBAczQJUtyyDlueojbwR3-qWNTP904QvXsuK2OTzoAmEwuqfaE7pmiloHbVvmdXIMBdbLDVT8Sona7qYlpZo9j7EYxDyNZCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات هوایی اسرائیل به عرب‌ سلیم در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/124044" target="_blank">📅 23:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124043">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc40eaf31.mp4?token=EItsxmUcWBPdAO81WeLu-cjgs78tBsrCxlVEGQMPLX9AyuPYDbgGHI9QAIDSnD0rfynXM5u4OhlI1XYewwHqBwpetgiLIgPOPrgqkwy6R7umUd2SH3MAlW12ECu3bcPxs7DXTgUS6V_2P0h7VvuQ8JU9fSHg-Lb_79v-XpAN2TN5fL6R-feMwOi9gKoRjSrbgKEmovzLlm4lsLGf7ILiydTZw5hZOnaoKHMqPOn1pJhu3_4KOFSGqoATNXIlJsZAT_10SL2Ai2Vm0EBBSVwbAM9R017z5txeeKENlrAd-uQJJu1p0-ZROfkrIC6HX-NPBeU9Y0qEao6XkxBEBnDtqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc40eaf31.mp4?token=EItsxmUcWBPdAO81WeLu-cjgs78tBsrCxlVEGQMPLX9AyuPYDbgGHI9QAIDSnD0rfynXM5u4OhlI1XYewwHqBwpetgiLIgPOPrgqkwy6R7umUd2SH3MAlW12ECu3bcPxs7DXTgUS6V_2P0h7VvuQ8JU9fSHg-Lb_79v-XpAN2TN5fL6R-feMwOi9gKoRjSrbgKEmovzLlm4lsLGf7ILiydTZw5hZOnaoKHMqPOn1pJhu3_4KOFSGqoATNXIlJsZAT_10SL2Ai2Vm0EBBSVwbAM9R017z5txeeKENlrAd-uQJJu1p0-ZROfkrIC6HX-NPBeU9Y0qEao6XkxBEBnDtqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ی اصابت پهپاد انتحاری حزب‌الله لبنان به خوابگاه نظامیان اسرائیلی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/124043" target="_blank">📅 22:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124042">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d568308de.mp4?token=WMJ8y-G-LdEKVH2NLGsJAbLaAGv-Rka3L6Gf3c1lx8y0J3CeOE5FVBZ7SMmexITtjIOi8Kzu1pKHfla7RcuH77s7Z3oKQOtQDwN4obkBtjYYa3E-zpId58yIhC5Ie7pReMClhU2n-V4lo0zeeNUClRVUWjGBlRCxUmx_dpQwFT1Hj88564jr1gG1sWh56-BrTcWJWRGBRKxhzuointGTQ7X45lS6yERJm1R_jDpTrvTSYx-uKP89nQMTnBT6Pymr8noMIJcijUYbbocu5QaFuZ2V5PSTjMLBlYePOvUjx4aI1Hy27xnxGsuFoNKxKAjP540DH1Ux1j9IiwSjcFLdsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d568308de.mp4?token=WMJ8y-G-LdEKVH2NLGsJAbLaAGv-Rka3L6Gf3c1lx8y0J3CeOE5FVBZ7SMmexITtjIOi8Kzu1pKHfla7RcuH77s7Z3oKQOtQDwN4obkBtjYYa3E-zpId58yIhC5Ie7pReMClhU2n-V4lo0zeeNUClRVUWjGBlRCxUmx_dpQwFT1Hj88564jr1gG1sWh56-BrTcWJWRGBRKxhzuointGTQ7X45lS6yERJm1R_jDpTrvTSYx-uKP89nQMTnBT6Pymr8noMIJcijUYbbocu5QaFuZ2V5PSTjMLBlYePOvUjx4aI1Hy27xnxGsuFoNKxKAjP540DH1Ux1j9IiwSjcFLdsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امنیت ملی اسرائیل بن گویر : من نماینده از جانب تمام اسرائیل هستم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/124042" target="_blank">📅 22:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124041">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
تسنیم به نقل از یک منبع آگاه: ایران اصلاحیه‌های جدید درباره متن تفاهم احتمالی اعمال خواهد کرد
🔴
تبادل متن‌ها ادامه دارد و ایران نیز قاعدتاً اصلاحیه‌های خود را درباره متن اعمال خواهد کرد و هنوز هیچ چیز نهایی نیست.
🔴
ملاک برای ایران متنی است که خودمان قبول داشته باشیم و اعمال اصلاحیه از ناحیه ترامپ به معنای پذیرش آنها توسط ایران نیست.
🔴
ایران برای وضعیت عدم تفاهم نیز کاملاً آمادگی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/124041" target="_blank">📅 22:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124040">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
بانک مرکزی: رقم وام ازدواج مشابه سال ۱۴۰۴ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/124040" target="_blank">📅 22:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124039">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ade6a1991.mp4?token=GF2bCRRt_AGEleAkCAroaxikj1aQDac00hccXqjDHWe_5w0jc9MIzIrWB-4Jpvn7YaFj6iZQLSDP1mOhYyDbQBNHFDwKbaNpoFOoswsoqk_mEgCoswd0vq6ZNGZbEkfmqOc3QlsvYxrBSPK9tozORMwGJwVkgvxKlkB5HIqI3Z6qj5Vj9LvWv5z2AFNO67QW1jbDNOkBA6Uu_QEdJYNOFkQBuvoURshWXZ-eZFqlLu-VywE1YOnAbT_cW9CLP0P2WOzgy285BiPsp14rmagYCMea-rjw6sEbTq0GxMPXuKJsAQwp6ydyR7KG5frFvSc1bK8WTEsJY97Q-SvFOSqsXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ade6a1991.mp4?token=GF2bCRRt_AGEleAkCAroaxikj1aQDac00hccXqjDHWe_5w0jc9MIzIrWB-4Jpvn7YaFj6iZQLSDP1mOhYyDbQBNHFDwKbaNpoFOoswsoqk_mEgCoswd0vq6ZNGZbEkfmqOc3QlsvYxrBSPK9tozORMwGJwVkgvxKlkB5HIqI3Z6qj5Vj9LvWv5z2AFNO67QW1jbDNOkBA6Uu_QEdJYNOFkQBuvoURshWXZ-eZFqlLu-VywE1YOnAbT_cW9CLP0P2WOzgy285BiPsp14rmagYCMea-rjw6sEbTq0GxMPXuKJsAQwp6ydyR7KG5frFvSc1bK8WTEsJY97Q-SvFOSqsXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بن گویر وزیر امنیت ملی اسرائیل:  نصرالله دیگر در میان ما نیست، و این تصادفی نیست. و هزاران عضو حزب‌الله دیگر در میان ما نیستند، و این تصادفی نیست.
🔴
و با این حال، این کافی نیست. ما پیروزی را به دست نیاورده‌ایم.
🔴
ما باید ادامه دهیم، و ادامه دهیم، و ادامه دهیم. ما نباید متوقف شویم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/124039" target="_blank">📅 22:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124038">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
رئیس‌جمهور سوریه با ترامپ تماس تلفنی داشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/124038" target="_blank">📅 22:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124037">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
حمله به کشتی حامل مس در تنگه هرمز
🔴
در پی درگیری‌های اخیر در تنگه هرمز، یک کشتی خارجی که حامل مس بود، مورد هدف قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/124037" target="_blank">📅 22:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124036">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⭕️
الونیوز فقط در تلگرام و توییتر (X) فعال هستش
🔴
سایر شبکه های اجتماعی چه داخلی چه خارجی که با نام الونیوز فعالیت می‌کنند مرتبط به ما نیست و پیشنهاد میکنم که لفت بدید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/124036" target="_blank">📅 22:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124035">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=SmXtEw-LldJSyCyCVnPLRfgMXQmWZEbUEccF3_yYhmb3WwdYm7KSEEkcUyH6lpBoY2FNarZDSx2n6Bf9lNoSqav3OseO-HlKh17v03QvYiIS6swKQyfsd8y0KUPmVQxjG2vgw4cG5Oy-n6WBxRxzDLIqi9RWy_NJNT_yfkezj9pyQIgzmd2NapwZQinay6hlV0jhw-jRObCajTysHN88Nznsh6HOmF4vEV8s3bcWaHRCDukaCB5sCfb_orFslQF3OaQzi0pNIKY5bRwwc_9clt3xen0jTAVS4BS0UWXaQot4MWdJDt7c8iv2OfRlUhLEBFtoEUTSUbHXACl8VvG3aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=SmXtEw-LldJSyCyCVnPLRfgMXQmWZEbUEccF3_yYhmb3WwdYm7KSEEkcUyH6lpBoY2FNarZDSx2n6Bf9lNoSqav3OseO-HlKh17v03QvYiIS6swKQyfsd8y0KUPmVQxjG2vgw4cG5Oy-n6WBxRxzDLIqi9RWy_NJNT_yfkezj9pyQIgzmd2NapwZQinay6hlV0jhw-jRObCajTysHN88Nznsh6HOmF4vEV8s3bcWaHRCDukaCB5sCfb_orFslQF3OaQzi0pNIKY5bRwwc_9clt3xen0jTAVS4BS0UWXaQot4MWdJDt7c8iv2OfRlUhLEBFtoEUTSUbHXACl8VvG3aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محمد‌جواد ظریف در پاسخ به سؤال میگن شما پشت پرده مذاکرات هستید، گفت:
🔴
من اصلأ هیچکاره ‌ام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/124035" target="_blank">📅 22:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124033">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!  @Netaazaadbot @NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/124033" target="_blank">📅 22:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124032">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cYKEvbcjnQ4PqxXoOAWn-05BJ2n4UGdAxeL_Bia6BrXR_fcJNbLbvRKo-z_G7m77wads0Ip22jYWrtzWgQYR1WBB6dgW_YmGJloJ3kfnKTW-x9TKA04wMn2bqfklOoSRBTPBrG41RCrC_0SJtM-ckb5gil3eoe9tFh0qw1l6JG5XQpWFeS7T4CI0BF3A13jEfB0A5KZV_Lv4IktQ__2SDhKerwKOT720ib5b_UEGexCI8f8BMEj1BAn-kc8YIep38dvpV3d0GmIkcxrY2iLMhooxx2dLqurU3rzKDOR1JGvpfiFOk-c_385upe_Cr3S7po9m2jM02IjuFl39RVEprg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!
@Netaazaadbot
@NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا حتی در ساعات شلوغ
@Netaazaadbot
@NetAazaadBot
💎
کیفیتی که بعد از استفاده متوجه تفاوتش میشی!
📩
برای خرید و دریافت سرویس استارت رو بزن
✅</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/124032" target="_blank">📅 22:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124031">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
وزیر نیرو: شاهد کاهش ۱۰ تا ۱۵ درصدی مصرف آب توسط مردم‌ هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/124031" target="_blank">📅 22:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124030">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDn7BvXZmY_00QW4uM9J9AYXmWLbDgiznJ-zO8nTtAETaUU4FN5K75ic1I4_Nea-BwNoVGbPxD3irR3v8cXNDMbBQvwZwmRJ3-MkQ3wM0I-eGyf38UGKNYMBrcdvwa_qc4YPXjt7VRVxlhCZai37fGARcZkSt37ADUNg9CHVpY9e0bqNFZKFMLccxiyE0qHXezooa2MD9-2Ng6uWcBfVkLFeDtQ5uCptsd5903HGneumvC0toqXBmQv5VOH2rGCzvTBTPZGI1WI6572KvjsnM28bHwpkn-tPUyUSJbW1Z432YcBn_X38HPoZUyQ0HMW_r6YzVqvAjfRM-R5AIQZz-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دادستانی بحرین، روز یکشنبه دهم خرداد ماه، اعلام کرد در چارچوب تحقیقات مربوط به آنچه «تشکیلات مرتبط با سپاه پاسداران ایران» خوانده شده، اموال و دارایی‌های اعضای این گروه توقیف و حساب‌های بانکی آنها مسدود شده است.
🔴
به گزارش رسانه‌های بحرینی، رئیس دادسرای جرایم تروریستی این کشور گفت تحقیقات نشان داده اعضای این تشکیلات به جمع‌آوری منابع مالی و انتقال بخشی از آن به خارج از بحرین اقدام کرده‌اند.
🔴
دادستانی بحرین افزود، در جریان بازرسی‌ها، اسناد و مدارکی مرتبط با فعالیت‌های مالی این گروه کشف شده و بر همین اساس دستور توقیف اموال و مسدودسازی حساب‌های بانکی افراد تحت تعقیب صادر شده است.
🔴
مقام‌های بحرینی همچنین اعلام کردند تحقیقات درباره این پرونده همچنان ادامه دارد و اقدامات قانونی علیه متهمان در دست پیگیری است.
🔴
بحرین پیش‌تر از بازداشت ده‌ها نفر در ارتباط با تشکیلاتی مرتبط با سپاه پاسداران ایران خبر داده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/124030" target="_blank">📅 22:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124029">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
زلنسکی: فکر می‌کنم امشب یا فردا شب از طرف روسیه یک حمله بزرگ با استفاده از پهپادها، موشکهای کروز و موشکهای بالستیک خواهیم داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/124029" target="_blank">📅 22:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124028">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnuCpEbZ-AVBNkuiBlQkOBAZv6RJbtLijUlyLxnKj_X9qNyxQWrZT-7TnUCOY-sLMn5z6yGTRIzMqOlSGvEWujaTb3GNdc1y_j1NCETwjwoMmE4WZgxCStZDdowz57ZSUlgfWLsiopIqvOd4OFx-SUcTnXM964KEF6hmUIM3Cy6W_MwvJ1WCDk_5QQFcYjJJlS-G2mCUsRbXNQ8LwwSAdgtx6xRBfw1zY2ecuqfcyPF19rE6PAwXD1uKiLm97TBrpwBhatkVo9KEsuyo6lUJmKltQje7jyiPjETNZlgxMJbU4VaYHXE4jC39TBx-BwknHptiFy8jBGTXVDLA1_m-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سرپرست وزارت دفاع: دست ما روی ماشه قرار دارد و شگفتانه‌های جدیدی نیز در راه است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/124028" target="_blank">📅 22:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124027">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">💔
روز ۱۸ دی بهرام زاهدی ۴۲ ساله و مجتبی قربانی ۳۳ ساله بر سر کوچه‌ای در دروازه لاکان رشت ایستاده بودند و تنها تماشا می‌کردند که ناگهان هدف رگبار حرام زاده های عرزشی قرار گرفتند.
🤔
شما حرام زاده های عرزشی تروریست هایی هستید که این جنایت رو انجام دادید و از شما…</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/124027" target="_blank">📅 22:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124026">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
به گزارش کانال ۱۲ اسرائیل، اسرائیل درخواست‌های رسمی خود را برای تأیید گسترش عملیات نظامی به بیروت، از جمله حملات هوایی احتمالی، به ایالات متحده ارائه کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/124026" target="_blank">📅 22:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124025">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
به گفته منابع محلی، حداقل دو جت جنگنده نیروی هوایی ایران در حال انجام تمرینات آموزشی معمول بودند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/124025" target="_blank">📅 22:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124024">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
پزشکیان در جلسه امروز دولت: یا با قدرت ادامه می‌دهم یا شهید می‌شوم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/124024" target="_blank">📅 21:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124023">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
چین از یک الگوریتم جدید هوش مصنوعی برای هدایت دسته‌های پهپادی رونمایی کرده که ادعا می‌شود حتی در شرایط اخلال شدید الکترونیکی، قطع ارتباطات و محدود شدن دید نیز قادر به شناسایی و انهدام اهداف است
🔴
بر اساس ادعای پژوهشگران، این فناوری در شبیه‌سازی‌ها به «نرخ موفقیت ۱۰۰ درصدی» در انهدام اهداف دست یافته است؛ هرچند کارشناسان تأکید دارند عملکرد در میدان نبرد واقعی به دلیل عواملی مانند آب‌وهوا، فریب، آسیب‌دیدگی حسگرها و جنگ الکترونیک می‌تواند متفاوت باشد.
🔴
هدف اصلی این سامانه حفظ توان عملیاتی دسته‌های پهپادی در محیط‌های فاقد GPS و تحت اخلال شدید ارتباطی است؛ شرایطی که در جنگ‌های اخیر به‌ویژه در اوکراین به یکی از چالش‌های اصلی پهپادها تبدیل شده است.
🔴
این فناوری بخشی از رقابت فزاینده میان چین، آمریکا، روسیه و کشورهای عضو ناتو برای توسعه سامانه‌های رزمی خودمختار و دسته‌های پهپادی مبتنی بر هوش مصنوعی به شمار می‌رود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/124023" target="_blank">📅 21:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124019">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/99a9772ea2.mp4?token=kMzFo1q_kw8iG-VgKiV2wFacuDZ3YghOclEBJ90DgzKiBKcHQCh1m-P5G6XybsKJW5sPlvWcVRkoPtfMONCm96-sdeTYkm9JDxo6SZXC7jXX1fcCPuYBdX-VkleQQ8iBUpXEVMyn1M-cdNi6Bwfv6M3KV711RAzksyHEwISOlAuvmDxAhzLN2AWNhNnTbLzIVmoye8w_HJHrjBiS8v_sR1eVvKT7Lg7GmcJyKkWp3EYCh8rvTcC164fK9SQ4R0TSP62s9tvy3vneTfo00x5YTL0okYu94URPSP1H_65xIFFTVU9DoPiJOJUPXrLtjVF5pUFzsLdZ80_C1GaZO0SbFg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/99a9772ea2.mp4?token=kMzFo1q_kw8iG-VgKiV2wFacuDZ3YghOclEBJ90DgzKiBKcHQCh1m-P5G6XybsKJW5sPlvWcVRkoPtfMONCm96-sdeTYkm9JDxo6SZXC7jXX1fcCPuYBdX-VkleQQ8iBUpXEVMyn1M-cdNi6Bwfv6M3KV711RAzksyHEwISOlAuvmDxAhzLN2AWNhNnTbLzIVmoye8w_HJHrjBiS8v_sR1eVvKT7Lg7GmcJyKkWp3EYCh8rvTcC164fK9SQ4R0TSP62s9tvy3vneTfo00x5YTL0okYu94URPSP1H_65xIFFTVU9DoPiJOJUPXrLtjVF5pUFzsLdZ80_C1GaZO0SbFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت جت جنگنده ناشناس نیروی هوایی بر فراز کرج، استان البرز، شمال ایران.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/124019" target="_blank">📅 21:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124018">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
دود مشاهده شده در اتوبان ستاری مربوط به حریق در انبار کالا بود
🔴
سخنگوی سازمان آتش نشانی: حریق مربوط به یک ساختمان دو طبقه بوده که در طبقه همکف آن پارکینگ را به انباری کالا تبدیل کرده بودند و دچار حریق شده بود.
🔴
این حادثه مصدومیت و تلفات جانی نداشته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/124018" target="_blank">📅 21:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124017">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
گزارش ها از پرواز جت های جنگی ارتش بر فراز آسمان تهران و کرج.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/124017" target="_blank">📅 21:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124016">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
عراقچی: ویزای تیم ملی فوتبال ظرف یک تا دو روز آینده صادر می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/124016" target="_blank">📅 21:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124015">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
نتانیاهو، در مورد گسترش حمله لبنان امشب تشکلیل جلسه میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/124015" target="_blank">📅 21:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124014">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67d8007820.mp4?token=BLL28qWZFZ1PMs6sH-JKm4QGCZh4GCh2QcBebvwks3Rc1vtiArf4_U8ObNoUgsNkZwz9b92rGlB0rQyVYdLRRqh-C6Bkab2tTAVr9We0f0YRC3QEFFApdYP6yTBAQBdU3s8ID04MG_tZLaEYhcr5UQxX9itFZZ9AJv3OGsr_BQXh-VTKM1ZnXmc2gi1bnLC7aqsHUXjj935i-ww9YXPKE6quSBeZVf_tpGYyu0vMJM7OWhS7p3hRoqpPyYbCxYVCmjd_j_5N3KrbFr90TpiXzf9X3IbfHbnG8thpqWKXNphKRQ_mgIDjHJNA848D6lyQTBYd21GptbFdjcLzuHEsEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67d8007820.mp4?token=BLL28qWZFZ1PMs6sH-JKm4QGCZh4GCh2QcBebvwks3Rc1vtiArf4_U8ObNoUgsNkZwz9b92rGlB0rQyVYdLRRqh-C6Bkab2tTAVr9We0f0YRC3QEFFApdYP6yTBAQBdU3s8ID04MG_tZLaEYhcr5UQxX9itFZZ9AJv3OGsr_BQXh-VTKM1ZnXmc2gi1bnLC7aqsHUXjj935i-ww9YXPKE6quSBeZVf_tpGYyu0vMJM7OWhS7p3hRoqpPyYbCxYVCmjd_j_5N3KrbFr90TpiXzf9X3IbfHbnG8thpqWKXNphKRQ_mgIDjHJNA848D6lyQTBYd21GptbFdjcLzuHEsEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: پیش‌بینیتون از نتایج تیم ملی تو جام جهانی چیه
🔴
پزشکیان: مهم نیس تلاششونو بکنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/124014" target="_blank">📅 21:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124013">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
کانال ۱۵  عبری: گسترش عملیات اسرائیل در لبنان با هماهنگی دولت آمریکا انجام شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/124013" target="_blank">📅 21:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124012">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50386848ef.mp4?token=OdhBO3PcRx5brXTEHcovCIxFQdBEAgUpxYzSHC1zxQ7NFlNhpbQVRdXdudrT5h70Hi6P5PtX6MPfqtFkqxg48j5nRY7LJCgU-T35rDePE3jIBNco_uUwaO7zBDNYWBTZKiz01u3UBNgT_xSZH_lxGNyLO-GZARBREVp1QrR0lJDLkJTrdcdmVoZMcx6ALF8KYRwiQcY-fFgKJx_0mdKaUMuX7RAycDVbrQg_Ej6VQlG8xx5cJKGNP7OaOcve-rRRlNh8ZMDMQsnSEZS3J2w5RQL16Fnr_arAz8EiFE1-LiLcVRz9imUqi1DDAI7lr2lN9G_zCjOJDFK7NyJGDCcfVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50386848ef.mp4?token=OdhBO3PcRx5brXTEHcovCIxFQdBEAgUpxYzSHC1zxQ7NFlNhpbQVRdXdudrT5h70Hi6P5PtX6MPfqtFkqxg48j5nRY7LJCgU-T35rDePE3jIBNco_uUwaO7zBDNYWBTZKiz01u3UBNgT_xSZH_lxGNyLO-GZARBREVp1QrR0lJDLkJTrdcdmVoZMcx6ALF8KYRwiQcY-fFgKJx_0mdKaUMuX7RAycDVbrQg_Ej6VQlG8xx5cJKGNP7OaOcve-rRRlNh8ZMDMQsnSEZS3J2w5RQL16Fnr_arAz8EiFE1-LiLcVRz9imUqi1DDAI7lr2lN9G_zCjOJDFK7NyJGDCcfVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
روز ۱۸ دی بهرام زاهدی ۴۲ ساله و مجتبی قربانی ۳۳ ساله بر سر کوچه‌ای در دروازه لاکان رشت ایستاده بودند و تنها تماشا می‌کردند که ناگهان هدف رگبار حرام زاده های عرزشی قرار گرفتند.
🤔
شما حرام زاده های عرزشی تروریست هایی هستید که این جنایت رو انجام دادید و از شما حرام زاده تر کسانی هستند که این اتفاقات را می‌بیند و همچنان از شما قاتلان حمایت می‌کند.
🔴
اگر آخرتی باشد قطعا شما در قعر جهنم هستید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/124012" target="_blank">📅 21:28 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
