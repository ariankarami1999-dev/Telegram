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
<img src="https://cdn4.telesco.pe/file/qj2z_LIJ9KATlMPj7pry0Pnn1SfbZ2jHkyQxAypfrH6NzFRfQZ4_Jjc2h0AZl9ijfheSneknI7j_VT5lA4lxvzVta0vnSycXceblP6G60uAgKd21SzZpn9k08clo2VqOhfsjQrVLbnstYa4mshxcpwYdfemONtY_t-Txyog0LfRHvUSrJ2p79QUo7TeTEP_IGg1E1Iv4uv-LuS5tX38sv3VDCqoxVSKBpZYLSY2qpnbXslDN_vzVCS5gbH6tSwmoymxInYUdPE7JCutYaqjihcXP_jm51LZOsG06YiiXkYW4F9KjVUTbA5DhgBbLwqvjiOjdHFXLzh7ZHlBRrg1asA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 227K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 10:00:44</div>
<hr>

<div class="tg-post" id="msg-65508">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
🚨
🚨
ترامپ درباره ایران: ما هر چیزی را که برای تخریب وجود داشت، نابود کردیم!
@News_Hut</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/news_hut/65508" target="_blank">📅 09:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65507">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8bb28ac6.mp4?token=V2dz-pwYT9q2ABqzyU_k513A7fqrsbEsukPhC1eGZ3cS3uVq8Q-NcN4lOaU8ro_JCFELVzGi1Sy8Gl2BPDLwqoEwU1C6YqnXamv1IFkJHCiOxlQwe-mtq4thcml_QD98fvouctcePtbE5Tv4TSr143HAH5DVfeUUc1LfwTB01rvKW8wVgwl9kK2DIdkby0bRL3EzaAxG3kxrBq-TNqhHK6aVpiGqtTs-xYShCnrz8tlqWObibvyw-k55iLOhu8sSVboRos6Jdc7VU7Srr6o4Cxs2OeynTxpjICW-9NH7DXeIlWhqfNKhnQa9bRomBCuh_6e69tNQ2GU2WsqmA0_UGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8bb28ac6.mp4?token=V2dz-pwYT9q2ABqzyU_k513A7fqrsbEsukPhC1eGZ3cS3uVq8Q-NcN4lOaU8ro_JCFELVzGi1Sy8Gl2BPDLwqoEwU1C6YqnXamv1IFkJHCiOxlQwe-mtq4thcml_QD98fvouctcePtbE5Tv4TSr143HAH5DVfeUUc1LfwTB01rvKW8wVgwl9kK2DIdkby0bRL3EzaAxG3kxrBq-TNqhHK6aVpiGqtTs-xYShCnrz8tlqWObibvyw-k55iLOhu8sSVboRos6Jdc7VU7Srr6o4Cxs2OeynTxpjICW-9NH7DXeIlWhqfNKhnQa9bRomBCuh_6e69tNQ2GU2WsqmA0_UGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
چندین حمله اسرائیلی در جنوب لبنان، در مناطق اطراف صور گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/news_hut/65507" target="_blank">📅 09:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65506">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
🚨
🚨
مقام ایرانی به الجزیره:
واشنگتن در پیش نویس یادداشت تفاهم تغییر ایجاد کرد و این موضوع غیرقابل قبول است.
@News_Hut</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/news_hut/65506" target="_blank">📅 09:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65505">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
طبق گزارش
نیویورک تایمز
، یک بالگرد آپاچی ارتش آمریکا در نزدیکی تنگه هرمز سقوط کرد اما هر دو خدمه آن به سلامت به محل امن منتقل شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/news_hut/65505" target="_blank">📅 09:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65504">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6179637bd4.mp4?token=Pu_FcKCoMln7WykV5NehLYQZgjslVLaGMgIEtKTjmu6GSme19WYv06pnnoD5DidILAQDEOLV3ojE0CoUWclT0JDX6T8D0QxePbqlVdeZbN8-xbjAJtwbEb67AV9sdwDGYFMDHrf97XgmLTYJyJSA-524CclstgUIcQ-jrwve676zZIH01ZcIXDXufkmpy12s47OnBxY9OlCCYtA6w8NFztu9Sho72Tr4cvONBkq5PsjZyw5y6qGfDZRac0VsRhAA-qcFQWiVDuKRwEOqrarvliEJht8l4D9ry7d9bRYjX1bj1HxiHUrCex19_HjsYDsvcW4FqRdYdaIJlNiuP9GQwDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6179637bd4.mp4?token=Pu_FcKCoMln7WykV5NehLYQZgjslVLaGMgIEtKTjmu6GSme19WYv06pnnoD5DidILAQDEOLV3ojE0CoUWclT0JDX6T8D0QxePbqlVdeZbN8-xbjAJtwbEb67AV9sdwDGYFMDHrf97XgmLTYJyJSA-524CclstgUIcQ-jrwve676zZIH01ZcIXDXufkmpy12s47OnBxY9OlCCYtA6w8NFztu9Sho72Tr4cvONBkq5PsjZyw5y6qGfDZRac0VsRhAA-qcFQWiVDuKRwEOqrarvliEJht8l4D9ry7d9bRYjX1bj1HxiHUrCex19_HjsYDsvcW4FqRdYdaIJlNiuP9GQwDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
یک کارشناس حکومتی در صداوسیمای جمهوری اسلامی: آمریکا در جنگ ۴۰ روزه بیش از ۷ تا ۸ هزار زخمی و دست‌کم هزار کشته داشته! کشته گرفتن از آمریکایی‌ها و اسرائیلی‌ها برای جمهوری اسلامی کار سختی نیست و ما به درخواست کشورهای منطقه خویشتنداری کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/news_hut/65504" target="_blank">📅 09:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65503">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65503" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/65503" target="_blank">📅 00:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65502">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xl_w1VD1DaW77JMNunrqIT0K9vP82awwDEe8hgGP7aSgju4vJQyVuHxL3BGZlC4tYaN1kZb5YCCA-G0Vo9x8utxWYFT4_GuNTts8lr3kAA2yB70qp5U4TG6AbtPtPC302HL1oss0sqsfNdkGY7l225HzAQ3lNNtNt2Y8RSmD8MZqCECDmYZqO87mOFMR76inVf9cORi2edxmTHcOpQ6tmj0VIojIZDtiZvF-AUX0lE5oQqfz6QhxQpwiaUdbcccz6MyowljgvRvHutzzxbyUpBOHwX6l7ox0D-nLULKIRb5RZL27dUCPhpq22s6jmy9PuLKguziVbmqRUszW83iyOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/65502" target="_blank">📅 00:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65501">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObgvNFLHgKauRL7QVCRBnWQkOSbRDc_wdnKMov500lMvE85YWfWqxKsGIEwaQXi0QqN43-NEuVa73iitn-Hu5fMPrjXd5IxVgy_3xU4yfQdT9yGWadNGyOnLOOA2-fyGA1VOm4x7Vpmg6HpL6F7c8NEDazBTMPOUV4rAZlAhcDqT9xpMPapezeyVps50xlitCz2NELcNkdiKO3TgzrK0pVa32Feddsg6ZFyeVCvSxntebEKf3i5mqBnfOHXXVs9EFC9luiZ_gqUO-bq-GJu3o8CUFbLOdT_2S9R5SnWSqofpkkdxoWdpsRwFpfuAcB5Z46rPlpDs1Slzb-MkXMODzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
اونایی که
۵ ماه
پیش وارد شدن الان
۲.۵ برابر پولشون سود
دریافت کردن
دو فرصت
ویژه
در
سرآوا
برای شما فراهم شده که با بازدهی فوق‌العاده می‌تونه مسیر جدیدی به سوی
ثروت
براتون باز کنه
✅
اگه توام‌ دنبال یه‌راه میگردی تا بتونی درامد خودتو داشته باشی به خانواده سرآوا ملحق شو:
@Sarava_Finance</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/65501" target="_blank">📅 00:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65498">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
مهدی خراتیان تحلیلگر اصولگرا: در ۱۸ و ۱۹ دی ۱۰۰ شهر یا سقوط کردند یا در آستانه سقوط بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/65498" target="_blank">📅 00:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65497">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
♨️
🚀
خبرگزاری فارس: انصارالله یمن با پهپاد به سرزمین‌های اسرائیل حمله کرده
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65497" target="_blank">📅 00:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65496">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🇺🇸
ترامپ به اکسیوس: ایران می‌خواهد به توافق برسد و این اتفاق می‌تواند به زودی رخ دهد
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65496" target="_blank">📅 23:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65495">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7093313be4.mp4?token=Bic9MZSzWRs9BDkiX_VpCNLTzDr5QIsk-x2g5a8_0S17YJ09HoK3xOtzLzPqTQuoWMUoypOQROq40I56HAPVJ0-iUkQDIQPF6LlVs_LlpoBKRrrMAigcGV-uz1JVwTyvUBeKSVX2kmG4lUMjocCg6-5DBwQQpW65Fo1Vw7N9qgtWvEKppsYZ-fa6ZFk2K3k_rMTyonkRKZTmiGLwlbf3x6YcisTSmCqB5LsHJlUBAdj-hCKISlpPJ8kA6pzU25YW80CRJGE2zsoTGdw-YY9WitA_KsPX4RzONIX7KDd90H16-PRZUIXgCuCgK7GMDpU4mXv-tOUQMUVrOyv1roA96Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7093313be4.mp4?token=Bic9MZSzWRs9BDkiX_VpCNLTzDr5QIsk-x2g5a8_0S17YJ09HoK3xOtzLzPqTQuoWMUoypOQROq40I56HAPVJ0-iUkQDIQPF6LlVs_LlpoBKRrrMAigcGV-uz1JVwTyvUBeKSVX2kmG4lUMjocCg6-5DBwQQpW65Fo1Vw7N9qgtWvEKppsYZ-fa6ZFk2K3k_rMTyonkRKZTmiGLwlbf3x6YcisTSmCqB5LsHJlUBAdj-hCKISlpPJ8kA6pzU25YW80CRJGE2zsoTGdw-YY9WitA_KsPX4RzONIX7KDd90H16-PRZUIXgCuCgK7GMDpU4mXv-tOUQMUVrOyv1roA96Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سپاه پاسداران حملات موشکی و پهپادی به پایگاه‌های آمریکایی و گروه‌ های کرد در نزدیکی سوران، استان اربیل، کردستان عراق انجام داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65495" target="_blank">📅 23:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65494">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2a7fe1ed4.mp4?token=Acq7Bfyg0oHtMdSdwJ6Zx1ZM9wssohnfczktIbhuYnh8yw5VuCpZ79AePtGD_a95iCE9NZS8tGb3FEkg-t7VJ-PmbkuFKOCnVUgNnBilfKlR8wSICzl6enCOe89j1RpvyQn5vyMaTr1pP9CnGB0l3jfKtmlpIG0d6B5fSQ2puCk8l4Hn6fRtAbN0U4WyueLxytAZVXwtr2n9oKgilL_g0vq1LMf6gTPab0V6EQ1g33MRbU6hhBk4jspkv2HfRgQCxkmZa5d4G0FMafdGqmUFzz_CY8OgYBbAdv7G9jLPWm2USuvDbAHJGbSLq1N1nPOoWwsJ7Vt7kH9TXehu5AGUCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2a7fe1ed4.mp4?token=Acq7Bfyg0oHtMdSdwJ6Zx1ZM9wssohnfczktIbhuYnh8yw5VuCpZ79AePtGD_a95iCE9NZS8tGb3FEkg-t7VJ-PmbkuFKOCnVUgNnBilfKlR8wSICzl6enCOe89j1RpvyQn5vyMaTr1pP9CnGB0l3jfKtmlpIG0d6B5fSQ2puCk8l4Hn6fRtAbN0U4WyueLxytAZVXwtr2n9oKgilL_g0vq1LMf6gTPab0V6EQ1g33MRbU6hhBk4jspkv2HfRgQCxkmZa5d4G0FMafdGqmUFzz_CY8OgYBbAdv7G9jLPWm2USuvDbAHJGbSLq1N1nPOoWwsJ7Vt7kH9TXehu5AGUCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
رژیم جمهوری اسلامی با موشک به کردستان عراق حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65494" target="_blank">📅 23:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65493">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
رئیس جمهور لبنان:
اگر حزب الله از تحویل سلاح خودداری کند، مردم از آن روی برمی گردانند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65493" target="_blank">📅 22:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65492">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
قالیباف:
هدف مذاکرات پایان جنگ و ایجاد امنیت پایدار است، نه عادی‌سازی روابط با آمریکا. ما نمی‌خواهیم از طریق تسلیم یا شعار پیشرفت کنیم؛ بلکه باید به دنبال پیروزی مهندسی‌شده با قدرت و عقلانیت ایرانی باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65492" target="_blank">📅 22:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65491">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
نتانیاهو به وزرای دولت خود:
ممکن است به چند دور (جنگ) دیگر با ایران بازگردیم، این پایان کار نیست
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65491" target="_blank">📅 22:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65490">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnriTGykiDe0B7te9kmZl4FGkMnpoWRRvDHsETggA1AukC4lJR_B2x6sSF0zyWMARy3EdTzxqf014_Ro_ZlHCOQre5-LIE_Do-EBofq8j7oAoAc2iiMIAj_xedu1pVp9SSLFBW3BPjSojr-AasSetxyzU00qbo-86JXtw8rpka7nTow-n5azuU0GuS7mVpbA-ySIWm1YBLdMUIp7c7tZcRKQXnUnmdpOq13vv6F3X80E9YCF2dC5f0hUS4HbCkminqobZCczigLeR7nS6zMRYsZzvpd4JGm11DTIB8RIIxTnFV1d3n3udu7BRT2NOCGm-UQf4rYu8TN8ykgBE9buzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرژانتین
🇦🇷
-
🇮🇸
ایسلند
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
بامداد چهارشنبه ساعت ۰۴:۳۰
🏟
ورزشگاه جردن-هیر
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
آرژانتین در
۱۰
دیدار اخیر خود،
هشت
برد و
یک
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
ایسلند در
۱۰
دیدار اخیر خود،
دو
برد و
سه
تساوی کسب کرده و در
پنج
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر آرژانتین
۲
.
۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر ایسلند
۳
.
۵
گل در هر بازی بوده است.
🧠
وقتی نتیجه از تصمیم مهم‌تر شد، تفریح تمام شده است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65490" target="_blank">📅 22:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65489">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNuSTVIh0pmAhVzvP4zKzP5-xSw5fAC4_X5fYEygP-UdJ9EVMO4dsaEdtplJsvXzpRhYIDvJuLAyUzmp3wmNygQlgEpo_-cQoQhQfVn3aGIHpAEiwaWDvJx32zMEWju7PQT2ZZzVY8X1kQlk9YDDx6ENJO0a3stMbIXK24_4vuDy7UuVEOFXfv1bE9X92lKrJyTUiSS3AYEvO89XxROH2NyUOv3k_16oPQnZM3xhGBNJt4HA9ahQ5ze_8fI2OspsEJwr2PvjUhovCyRjroYlIGaa3R8fjDz5Ool0b-BzKV6oGM7N6NAEpeq_yQD0yg_Rz9nl8yLUPHW17GIFOkoloQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
صابرین نیوز با انتشار ویدیویی از شاهنشاه آریامهر محمدرضا پهلوی سعی در مشروعیت بخشیدن به موضوع کمک به لبنان دارد
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65489" target="_blank">📅 21:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65488">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
مردم ایران بهتر از هر کسی می‌دونن که تا وقتی جمهوری اسلامی سر کاره، نه ایران روی آرامش می‌بینه و نه منطقه. صلح، امنیت و پیشرفت واقعی فقط زمانی به دست میاد که این حکومت دیگه بر سر کار نباشه.
راه‌حل، مذاکره با سپاه و مسئولان جمهوری اسلامی نیست، راه‌حل اینه که دنیا کنار مردم ایران بایسته و از تلاششون برای رسیدن به آزادی و پایان دادن به جمهوری اسلامی حمایت کنه
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65488" target="_blank">📅 21:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65487">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی :
این حکومت سال‌هاست مردم ایران رو گروگان خودش کرده و از جون و مالشون برای پیش بردن جنگ، ترور و بی‌ثباتی تو منطقه استفاده می‌کنه. توی این درگیری هم مثل همیشه، هر آسیبی که به زیرساخت‌های ایران یا مردم بی‌گناه وارد بشه، مسئولیتش با جمهوری اسلامیه. این رژیمه که کشور رو به این شرایط کشونده و هزینه تصمیماتش رو مردم عادی میدن
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65487" target="_blank">📅 21:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65486">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی :
جمهوری اسلامی باز هم برای حمایت از حزب‌الله ، کشور رو وارد یه درگیری نظامی دیگه کرده و بار دیگه نشون داده که منافع مردم ایران براش هیچ اهمیتی نداره
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65486" target="_blank">📅 21:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65485">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
ترامپ به کانال ۱۲ اسرائیل:
به نتانیاهو گفتم اگر جنگی تمام‌عیار علیه ایران آغاز کند، او را تنها خواهم گذاشت!
من دیشب از نتانیاهو خواستم که به حملات ایران پاسخ ندهد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65485" target="_blank">📅 21:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65484">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
ترامپ :
اسرائیلی‌ها وقتی جنگنده‌هاشون تو مسیر ایران بودن، به ما خبر دادن.من هم سریع وارد عمل شدم و تلاش کردم ابعاد حمله محدودتر بشه!
همچنین پنج کشور منطقه با من تماس گرفتن و خواستن روی نتانیاهو فشار بیارم که حمله نکنه من هم با نتانیاهو صحبت کردم و اون در نهایت موافقت کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65484" target="_blank">📅 21:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65483">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
سازمان هواپیمایی کشور: حوزه هوایی کشور به وضعیت عادی خود بازگشته است و عملیات پروازی طبق اطلاعیه‌های پروازی صادر شده (NOTAM) از سر گرفته خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65483" target="_blank">📅 20:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65482">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/103c84b28e.mp4?token=H3eySMJY9kf-Xp4IlP9KLJbXLyBMhQ9ttmiQvGbObdYF1m_iVlIuQ-8aYYA_zcomvUmiSaU4Gb5mM5pSPAJ-452_GOBwneLqlYxZ3zb14_-yEYPQ6U1ALNFiHbrJj_lrFhxEtAqHOZkQ323SeAroCpR7-SMIcrWRmk1RXINzficLQcjiEwIWZ2TZ-9zEskFEnPPfc_t2_7ER0-H6ORvdP5YgatSdmMap4TymsTj9D8OyKTQw729vSjGDeI9SL972-v6zw87XXLNKKtJPQiMF8ufZU5L3-EqVAAV6O1xq9A5nRt3A9x9yFD00vB0f1ukXhyv-GklsJ1J0HeoFFuH0tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/103c84b28e.mp4?token=H3eySMJY9kf-Xp4IlP9KLJbXLyBMhQ9ttmiQvGbObdYF1m_iVlIuQ-8aYYA_zcomvUmiSaU4Gb5mM5pSPAJ-452_GOBwneLqlYxZ3zb14_-yEYPQ6U1ALNFiHbrJj_lrFhxEtAqHOZkQ323SeAroCpR7-SMIcrWRmk1RXINzficLQcjiEwIWZ2TZ-9zEskFEnPPfc_t2_7ER0-H6ORvdP5YgatSdmMap4TymsTj9D8OyKTQw729vSjGDeI9SL972-v6zw87XXLNKKtJPQiMF8ufZU5L3-EqVAAV6O1xq9A5nRt3A9x9yFD00vB0f1ukXhyv-GklsJ1J0HeoFFuH0tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فیلمی از کشتی M/T Marivex که امروز صبح گرفته شده، پس از آنکه توسط نیروهای آمریکایی به دلیل ادعای تلاش برای شکستن محاصره دریایی ایالات متحده علیه ایران، از کار افتاده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65482" target="_blank">📅 20:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65481">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siRTzi9QhaKPhnknUxg1hWAcBHMwbmSHlZGNiSrZSA1LvklX7SEM0atrovw7tJHQU20tuGLs4Q5zlW8YyYS8B34ALOgf8nP1gExn7AP-zCMjE4HKLsrm4YSK83EAWyREzmAlP5YMpFsPIuVg6JfJuZ2QCkWCHlImzyQCLyJ9U1nITzkcB98S4UHU_6NKdeZkQVI8IHdQNqzQqwOkhWJEzMmiJDu7Zrsisg7yTFUPB4tPVbX9TXCiNr_uU-FZ_AjHOUXxMPelTqVDeFyM_h9Mb-sPdrXaYA8aCqhVx_SKjU6Wmpp58RYVkUsen3ncQkmmDWi9tcYQnxH6bNiIp3gdgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
نیروهای ایالات متحده یک نفتکش بدون بار را در خلیج عمان، در 8 ژوئن، پس از اینکه کشتی با تلاش برای حرکت به سمت یک بندر ایرانی، تحریم‌های جاری علیه ایران را نقض کرد، از کار انداختند.
فرماندهی مرکزی ایالات متحده (CENTCOM) کشتی M/T Marivex با پرچو پالائو را زمانی که در حال عبور از آب‌های بین‌المللی در خلیج عمان به سمت ایران بود، از کار انداخت.
یک جنگنده F/A-18 سوپر هورنت از ناو هواپیمابر USS Abraham Lincoln (CVN 72) پس از اینکه خدمه از دستورات نیروهای ایالات متحده اطاعت نکردند، یک مهمات دقیق را به بخش‌های مهندسی و فرماندهی کشتی شلیک کرد.
ماری‌وکس دیگر به سمت ایران حرکت نمی‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65481" target="_blank">📅 20:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65480">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65480" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65480" target="_blank">📅 20:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65479">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONvhrWNAk8sa-RB2kEclmNyU2gE6IX5E6BviLPbz2-gHTOWam6QM_F72_ONcJ8fT5Bueu3NAvJ60wGtjpHsiMAvi6La-luuXEPwNwX8dPLCO2prtYNz43QrEFdwm3GIAbIwu0wmCULU_qlwjQ_kw5iDoZlFq_UsrSY7K0CVIxrgvrWrW5vuDcA-R0Tn4vPZkeK7b5cN5kKdCOnARU3qnIC03k5qUgJhy0W8HdNx60uqajxWwy_hm5OvNegA1xDiBecZq05fwqcc1vJfj0E4CybFF5q0ZgSgn80JxgiWVbOLATjvntznr8jsiMm1fWKbmyQcwrlZlRZEDx9AivzPXSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌇
بونوس‌های شبانه از 1xBet
🌒
هر چهارشنبه و پنج‌شنبه از ساعت ۶ عصر تا ۱۱:۵۹ شب، برای واریزهای 5.50€+، 50 اسپین رایگان در بازی
👑
Crown Coins
👑
اهدا میشه!
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65479" target="_blank">📅 20:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65477">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
رادیو ارتش اسرائیل: ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند.
«این حمله گسترده انجام نشد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65477" target="_blank">📅 20:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65476">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
فیلد مارشال ، محسن رضایی:
ایران از غنی‌سازی کوتاه نمیاد و در موضوع آزاد کردن پول‌های بلوکه‌شده جدیه. اگه مذاکره نتیجه نده، محاصره دریایی رو تحمل نمیکنیم و اقدام نظامی انجام میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65476" target="_blank">📅 19:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65475">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
ارتش اسرائیل تعدادی از فرماندهان ارشد حماس را ترور کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65475" target="_blank">📅 19:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65474">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
نتانیاهو:ایران فکر می‌کرد می‌تواند به خاک ما حمله کند و ما واکنش نشان ندهیم، این اتفاق نه رخ داده نه رخ خواهد داد، دست کم تا زمانی که من مسئول باشم
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65474" target="_blank">📅 19:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65473">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9oPGGo_HD1aR6AdlSFNA5C-GlgLmQ7hgs3LpAPBenYtlrn1xfnRbM4OOwcCLh1sCq3WuKE4zQdlxXZTwBvZ4KiKOoSHndDLsXe1HIYcGdZvFNC4ZwHtWivyDeso-Q6YEK8kAzQEnWuAT6NDgzKgxvtiuG5NjE_hPSfb0DjsNwfXtg2jNcp6x1DcS6BMB0A_o8-ULzFL6uPxAnWgTXXLRCyeEtYAoHx71hVnXG_z53px-YuWppvhBnYDjP3Q2XClHajsxtLtkeTsHZNDdarRwuA21pI6zesBMFVpHYLHlYKrUnGDh8p1n5VCA_CTERqE2HV4ausEheRJsYHw-enQJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروی دفاعی اسرائیل (IDF) دستور تخلیه محله زقاق المفدی در صور در جنوب لبنان را صادر کرده و به ساکنان هشدار داده است که فوراً خانه‌های خود را ترک کرده و به شمال رودخانه زهرانی نقل مکان کنند، به دلیل حملات قریب‌الوقوع علیه حزب‌الله.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65473" target="_blank">📅 19:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65472">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
نتانیاهو:اگر رژیم جمهوری اسلامی اشتباه کند و حملات خود را علیه ما از سر بگیرد، ما به شدت پاسخ خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65472" target="_blank">📅 19:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65471">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
نتانیاهو در واکنش به اظهارات ترامپ: اسرائیل حق دفاع از خود را دارد
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65471" target="_blank">📅 19:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65470">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
نتانیاهو:اسرائیل فعلا از حمله به ایران خودداری می‌کند ولی ماموریت ما با حزب الله هنوز تموم نشده
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65470" target="_blank">📅 19:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65469">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc930bac93.mp4?token=CIweL4AXfRigoJoKNKBnHdVjdOVAKXPtccdPXKtksP1CPZrPkIsOOpM4wdwOHHAl4eFJxLjKjvRekVVTJ6E3jDgjNDTvJX5QoH86sv-SBGVp3qUTgzbRFGRVD50ddD9tK8i8E4TO5j9n2GJyNxY1HHZdfKX0xHu_mHRkqSqMhb8PjSxepeGsM4aIyGaEyjEbFvywUMBCBZr3jEOP2SCEwRMJvpTEuB519T911zlswNM3dXCm5rzKvyHeFrFRYjS2r6uY8gffcQG5GUvVlFDprAuBAoVO-FvMkJD_nTrFRkO0H6n0yivsvW2EUE8oIGuH6q9uPSQf-7H7YRaXhhVkTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc930bac93.mp4?token=CIweL4AXfRigoJoKNKBnHdVjdOVAKXPtccdPXKtksP1CPZrPkIsOOpM4wdwOHHAl4eFJxLjKjvRekVVTJ6E3jDgjNDTvJX5QoH86sv-SBGVp3qUTgzbRFGRVD50ddD9tK8i8E4TO5j9n2GJyNxY1HHZdfKX0xHu_mHRkqSqMhb8PjSxepeGsM4aIyGaEyjEbFvywUMBCBZr3jEOP2SCEwRMJvpTEuB519T911zlswNM3dXCm5rzKvyHeFrFRYjS2r6uY8gffcQG5GUvVlFDprAuBAoVO-FvMkJD_nTrFRkO0H6n0yivsvW2EUE8oIGuH6q9uPSQf-7H7YRaXhhVkTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو: ایران و حزب‌الله از همیشه ضعیف‌ترند و ما از همیشه قوی‌تر.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65469" target="_blank">📅 19:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65468">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
نتانیاهو:ایران معادلات را بر ما تحمیل نمی‌کند؛ پس از شلیک حزب‌الله به اسرائیل، به بیروت حمله کردیم؛ پس از حمله ایران به اسرائیل، به مناطق مختلف ایران حمله کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65468" target="_blank">📅 19:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65467">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
نتانیاهو:نظام ایران پس از پاسخ ما عقب‌نشینی کرد و اگر اشتباهش را تکرار کند با شدت پاسخ خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65467" target="_blank">📅 19:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65466">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو: تسویه حساب اسرائیل با حزب‌الله با قدرت ادامه پیدا خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65466" target="_blank">📅 18:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65465">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53d663dc6e.mp4?token=G8KiogrlgsTRiwzwkE4_jADmxzUXcbyacfGBne7FPcbTUM8hCIxV6-R3Q62eBJBPGcfmabvvA-PQnKQP2VTioONSBOT4DWb-gQOs4Rcw-_nWWV4pIIqVGfJ_IxDG84SbUo1vNqYwe2_mi4o_ms1lLWC_OwgCmb2bJd5fZZSVOxZ2rksZ1dff5wLhlKhxicjivj7JF9DOuDVULJAEKrVLvnk3j9H3XaaK4w4BEuysgv6-zbvh8M9rty8HQKSOMJJrz5VJFMVSBuy1WbaO48GH2JLIUJ9_qjyNBaTx4yT95SUezv7wWQc_m9JPKGr2Lg52s53DSTB69owtx5KG5jM-og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53d663dc6e.mp4?token=G8KiogrlgsTRiwzwkE4_jADmxzUXcbyacfGBne7FPcbTUM8hCIxV6-R3Q62eBJBPGcfmabvvA-PQnKQP2VTioONSBOT4DWb-gQOs4Rcw-_nWWV4pIIqVGfJ_IxDG84SbUo1vNqYwe2_mi4o_ms1lLWC_OwgCmb2bJd5fZZSVOxZ2rksZ1dff5wLhlKhxicjivj7JF9DOuDVULJAEKrVLvnk3j9H3XaaK4w4BEuysgv6-zbvh8M9rty8HQKSOMJJrz5VJFMVSBuy1WbaO48GH2JLIUJ9_qjyNBaTx4yT95SUezv7wWQc_m9JPKGr2Lg52s53DSTB69owtx5KG5jM-og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
سوخت رسان های آمریکا در فرودگاه بن گوریون اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65465" target="_blank">📅 18:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65464">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
بنیامین نتانیاهو تا دقایقی دیگر سخنرانی بسیار مهمی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65464" target="_blank">📅 18:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65463">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
وزیر دفاع اسرائیل، ایسرائیل کاتز:
وضعیت در ضاحیه بیروت همانند شهرک‌های شمالی است. هر حمله‌ای به شهرک‌های شمالی منجر به حمله‌ای در ضاحیه خواهد شد. ارتش اسرائیل به عملیات خود در لبنان علیه سازمان تروریستی حزب‌الله ادامه خواهد داد. ما تهدیدات ایران را به‌طور کامل رد می‌کنیم. هر تلاش ایرانی برای پیوند دادن لبنان و ایران و حمله به اسرائیل با نیروی عظیمی مواجه خواهد شد، همان‌طور که دیروز اتفاق افتاد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65463" target="_blank">📅 18:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65462">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3210944dde.mp4?token=cHBiJnkL-nFkBXmCGjsBqruV0Kj18H0W26q7jlhmn8PBXoi-euqfjE1HAx7fxHG25bXDSrjNCccGavBSKM01ANZ3pF8ESUP3Y87GFH0GRYCnqf8UkHr5FfcvPugy5j9i2FhIocmh7IinqswPu2a2V1VpjY3lGAapDidOleL1ALk_fr8zzWB4K1FvJs-FvUgUKr479QKHfu7-Sge7Ok5BGze9TTVQqBXihfxYvngNzcESWWYxkCh-rzWFu0gVPvrOy5LUYkHL9JaOpgfatCiAMgRn2WR7MBjmmNLR_X-N4pDBLQuIq3FDl0oY79Rwn_rAR1e-bsTZAheHnXMbPHGw7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3210944dde.mp4?token=cHBiJnkL-nFkBXmCGjsBqruV0Kj18H0W26q7jlhmn8PBXoi-euqfjE1HAx7fxHG25bXDSrjNCccGavBSKM01ANZ3pF8ESUP3Y87GFH0GRYCnqf8UkHr5FfcvPugy5j9i2FhIocmh7IinqswPu2a2V1VpjY3lGAapDidOleL1ALk_fr8zzWB4K1FvJs-FvUgUKr479QKHfu7-Sge7Ok5BGze9TTVQqBXihfxYvngNzcESWWYxkCh-rzWFu0gVPvrOy5LUYkHL9JaOpgfatCiAMgRn2WR7MBjmmNLR_X-N4pDBLQuIq3FDl0oY79Rwn_rAR1e-bsTZAheHnXMbPHGw7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو ای از اصابت پهباد به مواضع گروه های کرد در شمال عراق
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65462" target="_blank">📅 17:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65461">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
اسرائیل هیوم از منابع: هنوز هیچ محدودیتی برای فعالیت ارتش اسرائیل در حومه جنوبی بیروت وجود ندارد
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65461" target="_blank">📅 17:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65460">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc72e760f.mp4?token=HGNaLrWp2NgwV02F3f2xjZU_X8AZgxhSSXKVm1m44YKz871mcs9adVF9l7Rkv-dNbIKxodv5ZLlAtHmmDfycDZMwdrQxQuN5fLSFAfnPkKfAquj6ALhK8-wiTGaCAM7lUA-mStEkCYTCQOnbwudQ6Srqcw-S0mZzwQTQMpXhl1tns_1rDDZ35KqlbYixs1SIE5t1n6zsofbCf0te4fvbhzPGwPQvKVXgd2Fdf9vgIkK-87HwBhMgFzOtv_A4rgu177sRMhn9ITLDLKdqAbJCjPmLr9MFc7zMuY201yOfrd5VqUBXeOOQ9s0iNQO3mGKj67xWVKf-PbHFZy-P7Ehtkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc72e760f.mp4?token=HGNaLrWp2NgwV02F3f2xjZU_X8AZgxhSSXKVm1m44YKz871mcs9adVF9l7Rkv-dNbIKxodv5ZLlAtHmmDfycDZMwdrQxQuN5fLSFAfnPkKfAquj6ALhK8-wiTGaCAM7lUA-mStEkCYTCQOnbwudQ6Srqcw-S0mZzwQTQMpXhl1tns_1rDDZ35KqlbYixs1SIE5t1n6zsofbCf0te4fvbhzPGwPQvKVXgd2Fdf9vgIkK-87HwBhMgFzOtv_A4rgu177sRMhn9ITLDLKdqAbJCjPmLr9MFc7zMuY201yOfrd5VqUBXeOOQ9s0iNQO3mGKj67xWVKf-PbHFZy-P7Ehtkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیویی کوتاه از حملات امروز اسرائیل به اهدافی مشخص شده در ایران
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65460" target="_blank">📅 16:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65459">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsZqiKPF0DOvf6i4oM1dDcPM_p5_o_0pJR3_89uVlgg7-x3nIvFcbo1oYVCDVvYTulAnjr17796eRRh9I6mqGQm8yXDbWUE-K02KBSg36E3EjxF_qNdQLWCigJWULGUKxTIhDkFM-Q86lyQxT6B_f1qbpu9oA_wBomjzx2JZTXXJ3oJr-UtRZVZNBomGJci3q75FLKaI3ri77jG_pXhAZ0lOR7_X2TypjB8tS_bd5a-OWlPTX2KMhZEQRdl33EcJE8n3Pm9_7zYo0sVDtHfgI9qaHXUEq8uHUmh1OY49A3UCpOF0sxglvdte6fLG7Gv0vUQRTlei5cXvxtxYJphBgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری دیگر از جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65459" target="_blank">📅 15:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65458">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDLJvw5_--D2erm7AxmmCtD9yh29EYoBmpm2bcrKwVlI_OHOVdqwpw2xGyG8aq5xNP9l7i7jPlVq1IKIA1n5u-W-glEqT27oRbKg8UZZSgMIQy1xkJ1AvJ1cX7RSBraelyI76lWICDHIMbEkc_GcwcOqRMw79EGSi08kkY7ZFgm7MeLc3PlER8cxrQP5p7XMIbmJ9Wn6m2jRBt9L1Sd0t1rKPPdcziB4OX7kDOfBopls69Hr5ul1pLkxyhSq6RkrG8E0OSo0ql-znmVM3LsCrAl_m1E8ukuecwNtN8qweb4_9M_2Kgs3xoNyY50bupePHakp5keywI2nsGwpT7Eeiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش ها حاکی از حملات مجدد اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65458" target="_blank">📅 15:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65457">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfQ1p7d8fSF6GIcRe4r6SR8tIFbE9yOYnvmOb2S6s7yoisMLgqeihYzjgceHxYQWbtVlX4I02sASPa7bumJmGFld1b8xOGP9Pvz8zyGwK_oNSgYoErkvvg2jx6UD4lfsCPueVqIteR1FRVBslYqdSyeX1NwcrywDjUEZ7DfWPLi1gmamP5pdLDTjNkZKpzzqDNtz5_XDLqzT1W_4MLgK3Z_F3wCDpUDLxLQCQfaAFpUjeBTT1iCbd9yBc7eWcuyWm4OZBYwVqn6Dtr9rg-kRJq1dTqDIIoLIUNyuxGShPNtjgWRcDmQfwru4nORTksEbBpQMq5G3oSyd65qMvcNmhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما پایان درگیری‌های دیشب و صبح امروز رو رسما اعلام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65457" target="_blank">📅 15:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65456">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🇮🇷
فرماندهی قرارگاه خاتم الانبیا:توقف عملیات نیروهای مسلح را اعلام می کند. با تاکید بر اینکه در صورت ادامه حملات و اقدامات تجاوزکارانه از جمله در جنوب لبنان، اقدامات قوی‌تر، خشن‌تر و قاطع‌تر از گذشته در راه است
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65456" target="_blank">📅 15:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65452">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lZJ18oAR95s4IFnUKEufWgvA_hsRlpQ75B-w3x3q_zu_epPnN5rXeO9RBxGbKl6WmvBSY186JXCAvbxML_ShE0UHxCZxGNf7H9pFxfakaj4cu_qkMI6-yEeNwRpb_nLl8dgqwrl0qelPj0lJcIGvhig7qOgAODk3l9Wz04XL4ce9zvjX2cvEOEk3cGIEGDzKYo8Vy_yHZlTjVGs438SUcP84-jhkuly3sgjpJysWXEogxHItGS4qy3skn41fKcsuKoHunXkRULI35gnaQZ3iCPfoT7xoYl93vBs5eRaXLivzRCuynRYmU6uMrIvO88wRtqMh108S9rxRasAKJdacxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YzkSMyJnNJUl8AXB1SSbH6h-rS6SjMSzRvGvUZjyp0yF3LhvB8yR6IZfj6bJHVUlndC6WHqHkYVPietM19wpEkOGWhhkqe6CQRgLQnfwBJcDL8lptonto9POpf32QyGJaW8pR9522py7M4hnQqOL8EoL2_FOcEtxJPTyygcFrSstLUhkUnbhTXv7dZLeFv9KU4A5TRJmdpKnrYhDSNHwlWXCs1JUDpk96s1zdm_VzI1dTbLrSxjgPRx6yq9IXpq3B_BxHUWi91fKRAqDmxvBhJQac9yw2m8Pb5zhbzVgWM2iydZmsGLhZJjwVuKpzEjRH7Ot0Pzqob0oH5aaedojmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kjAzZ-qn0i08yO5pcXCKk8XPg8r5Hvi_pv0KyncpfSVo1Cw2lOTfwteJZr765samUOlp28LbJOT33v9HoEngquS8UayJS1fD6rSBhzra-6S7mEf4BhJr-Q6Jta0XM4KcplEEi6T0S4hZ3k383U5Mu8RGsM-0w-VZFwWzud4gnpjzsdAXQQ77-91v1Lse85TBUasJqD0Y8tB2ZqucoGl9oQgkNms34Y5hfaLCqVNpZc8gIChC0axfXc09LwQpGbfR0sy9Hs0m1HLM5WFQasCFUUCPQm82ILREBzeZxEe11dA_GaOA7uQLd-LkiS4meGnqxUtlpbAb4Hf13SChB5wGlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0wAoZrZx-rsCyftKRq66dscVN67uix2mmx2xJLcnxkXbybxi2lA0bNfu_eOTafl6cW_fRAATR-nrRhqJqgD1jM8-hMHMkYrQdeC7OhfPj_8QZaNjEqObVnBTEsLk64yxQpkkaw66QuZNgrjC-xEuFFdExD6Vykz6Q9Hf1LpyvORsiZ4nQ2yFBTxQFBBKnm741FGk7qhHe41aGqn3XmBSSM7g3NFlSN4RTWxtB145_0KdmWxouemYacVQZQ9xCB6_nokIq9gfUdZDmOZkD63yFculVqonKSxd0kjF5iqivWfaJxPc5ENpLRZtm2Gzr3uWRaPu9skEGm-rVXD9MKw8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکاس
اسرائیلی
؛ رفته کنار یه پوستر موشک ایرانی که تو اریحا فرو رفته، وایساده و عکس گرفته
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65452" target="_blank">📅 14:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65451">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-text">سایت های شرطبندی به دنبال ترورش هستن ، به عشق مردم داره میگاعشون
⚡
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65451" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65450">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sf7gLoue2fl_hMpIhShAdDhetERg00nT_ylh5E21oeurHPvqK-Kq8_8m6v_Uxo3muWR8Y3yJ8Sevy2mq6P9nSeVEUQrUJFZnXP6bklz0UBCWJrml8Z-0NZEO57ydU4WHSyPyt5VWUq6tBZLAyS6Bx7810K9sFr47hN6QFpfxoaq3Zs_K5j3rIvfadyk97K9lEQfsK_u-AIpJ_Fkpt4Ec73CzDXnICDMnIiocxZ5l5Nb4uqaJvxsgiZfokXnobyI-iAB4_gkGy9hT96d9wnmtwMaNDMEWjjJ9SkK93vIn2Lyehb1v6_aOUiKK277DrSfmnqMZEFjG9uIOXEIHaHqS6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبانی
🆘
کامل در لینک زیر باز شده است، برای دریافت آن کلیک کنید و عضو شوید
👇
👇
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
1 دقیقه لینک را لغو می کنم
❌
❌
❌
سریع بپیوندید
🖱
سریع بپیوندید
🎧
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65450" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65449">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVZdwBxVqIkFiDrfMAVEV2t_LML0_5ULCdpy58EwbswPpwcu_tu2K461MMLdkda_Ay7fOA7JirA1wl1vuhl2uNf9C8OQjq8PmKmx0cj41u_WBsTnpE7_w5RkKEsWBusW5a8dlVgZ5ir20ZrtgRYsghsYMMAMH_fjRo3NlaW21erjcNhs8TGFuZod1M86083TwMozqS7waE6TsPoJr-bzRuukynsB3cjsN8_mTItXPUpCbMyQNhmkDYCN9PMp1NmpfUEy0BQyF89QTXbLw6wBQkLovVgIPSsLwSTdUoeqVHd_qNrOqrjtENT-imMrC2UBHWDWdZqOP6uXpaQKFqjOFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:هر دو طرف، اسرائیل و ایران، به دنبال برقراری آتش‌بس فوری هستند!
مذاکرات نهایی درباره «صلح» در حال پیشرفت است، مشروط بر اینکه جهل یا حماقت مانع آن نشود.
محاصره با قوت خود باقی خواهد ماند و با قدرت کامل اجرا می‌شود، تا زمانی که «توافق نهایی» حاصل شود.
اوضاع باید سریع پیش برود. از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65449" target="_blank">📅 14:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65448">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
یک کشتی هندی در دریای عمان هدف قرار گرفت و دچار آتش‌سوزی شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65448" target="_blank">📅 13:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65447">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icKh3bKzA1VZedGSUHksClFnhvrX2OSgrx6mjSQ1BrCcdwUN3hhT5Usfzm36xfiZQPa01U5231ZBqpOrjKamPQ4lPfqdf-WMG7cSQ9LDU2e5sHj3AuhYmnLbGXaalMxqvn_RSLPO3cJJL2VcqAg7g5JCzXmExOoBzf7D-VmAU4qzLUKZKrNtjiyQa8ZvQZO6j2qqcFaUfVqYVvZBvGua7_KgZYgQGLeNpwBG1JxjqomQ_iwpLz-xA0j7cme4pLHET9-Mv4JiRoWKhK5bv8kwTYZaxkKsvPSSd6buNALmBxNjPb3dZihV0mMS_wKq3U4i3i4YzrosDDGarPefYzQWdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
دیلی میل| یک فوتبالیست بین‌المللی متهم شده که در یک هتل پنج‌ستاره در ترکیه تلاش کرده یک دختر ۱۴ ساله بریتانیایی را برای «بغل کردن» به پشت یک پرچین ببرد. پدر این دختر در گفت‌وگو با دیلی‌میل گفت که دخترش پس از این اتفاق دچار وحشت شده و در حالی که اشک می‌ریخته با خانواده تماس گرفته است. این حادثه زمانی رخ داد که او همراه خواهر ۱۰ ساله‌اش کنار استخر بود و والدینش حضور نداشتند. دختر ۱۴ ساله که از دیدن یک چهره مشهور هیجان‌زده شده بود، از بازیکن درخواست عکس کرد. پس از گرفتن عکس، بازیکن تلفن او را گرفت، اطلاعات اینستاگرام خود را وارد کرد و از طریق حساب دختر برای خودش پیام فرستاد تا ارتباط برقرار شود. به گفته دختر، پس از آنکه او سن خود را اعلام کرد، فوتبالیست او را هات خطاب کرد و درخواست بغل کردن داد. وقتی دختر مخالفت کرد، بازیکن اصرار کرد و از او خواست به پشت یک پرچین برود؛ جایی که به گفته او هیچ‌کس نمی‌توانست آن‌ها را ببیند. دختر که ترسیده بود، به او گفت پدرش در راه است. به گفته خانواده، بازیکن پس از شنیدن این موضوع به سمت دیگر استخر رفت و خود را پنهان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65447" target="_blank">📅 13:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65446">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
اخبار جنگو تو چنل دوممون پوشش میدیم عضو باشید
😉
✌🏼
@Futball
@Futball
@Futball
@Futball</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65446" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65445">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBv41z6wxFpryMoEYXPQPQlFPnE1RulesfpR_8_vrRRG_po26slqwFvefi-ORIgRs-YhL9luNOiHqUDUybyCZ6EHcIBT3h1k2fkXv91H8AF2LYFimX8B6Lwm_b88uJ1WmjMaVWZesY6Lwxl052gAdFQNbi55X8UYc2swjhilK9dXDq7T04z4OFIUWUYszA2jtf0AmTnXKhzpAex4tac6UsNBR_WixlKO2Y7VV7CE-U19jX0iageIfFtJxS4AaIObWI-MP2Ew5TesBFzYQbW5k3Q0bnUarcN6kd3VN_Sk1g2DOfqUyQryhsHW5hT3OYjh3PlRSQI0tXapmLgID4RAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65445" target="_blank">📅 13:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65444">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
مارکو روبیو:فقط کشورهای احمق وقتی به آنها شلیک می‌شود پاسخ نمی‌دهند
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65444" target="_blank">📅 13:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65443">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🇮🇱
منابع اسرائیلی: حملات دیشب و امروز کاملا با اختیار و بدون دخالت نظر آمریکا بوده اما سنتکام در رهگیری موشک‌های ایرانی کمک داده
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65443" target="_blank">📅 12:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65442">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8c5e38e196.mp4?token=lBVHEDHcMKotLLANHAUsuBKqjV75zInL1d2cfzFksy05_T03D8lp1wugs7aDe6wZNwAbq9ie67MI4-eRSZd3SMeK8ndcY9c6UjmYr7-9gSz-iS6q0yyq1Z8tJaVQwNQgEJINnPRyDXlNmgcapgnP6l4F8KYwIoWxn564ZLQAgDg0PjAX7apIn_c8OKbIXklLYBDIWZK_vVG989j5dJ12OIAR1GZjiOtLEdsKK29lPkkKMjlu1c1ylsTPDZbgRFdcOa3ZqkNdOBJbfTrK7wMl0oh83E0qJ5OvhfFCf2Fhn4rtI4Hf-tZ2IH4OKXqTa0UDVvEG6bt3Jatf-tJ3htQgvA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8c5e38e196.mp4?token=lBVHEDHcMKotLLANHAUsuBKqjV75zInL1d2cfzFksy05_T03D8lp1wugs7aDe6wZNwAbq9ie67MI4-eRSZd3SMeK8ndcY9c6UjmYr7-9gSz-iS6q0yyq1Z8tJaVQwNQgEJINnPRyDXlNmgcapgnP6l4F8KYwIoWxn564ZLQAgDg0PjAX7apIn_c8OKbIXklLYBDIWZK_vVG989j5dJ12OIAR1GZjiOtLEdsKK29lPkkKMjlu1c1ylsTPDZbgRFdcOa3ZqkNdOBJbfTrK7wMl0oh83E0qJ5OvhfFCf2Fhn4rtI4Hf-tZ2IH4OKXqTa0UDVvEG6bt3Jatf-tJ3htQgvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
‼️
‼️
‼️
بدون شرح:
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65442" target="_blank">📅 12:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65441">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb70e7631.mp4?token=Lqi8qAjiPpfr_BcbEwdcgm22lEB15hIJE3Ja6ka0lW0itrnIo47q2CQAJ6CRILEipZWYW_y0-QKwobgvbBQOXSy3rWe-QWklFHO7GTgGxpVJX4sXIn8TRXpUNr4BfmMlG8GRIZbQPKWLaDhpmOaYzWRcd7oN25__aFg2KxFhE7LRkthA7MMqCcBCz9tyTymMTIXoKe1iNPk2LeTgrHBYCoTImhNhRk7PtnrgaFN6OAPK__KIx1LQGrI1TG6uE_af2B9I639xtcM3PoQS8Q91sEPoWH6T1GGtDsiuvbAaPF4I3eVix4CPOKn7VOVlrsM5zkSKj_rcPP3-401_nNeKr1Memx_GF7rw5Q5RK-RyGTOPBeuok1foXvzOSpP1Wx7u7KHgp8E_HBHJ3kSWBAEQ2__jCeuldSxR4kxp83wFzL-sfJ68DXnnGKQkJnuV3dmWfdxVORNe2C_etFeDvKYovOeZBh-ibu1mtfRwwWMiaGQ9BxgSbPGO2Mu6AZ5A4kq0ZSavGGK0Do9UU2ApYyAGeAdB3XvvtHiDd43pxcyHyPSX17zYCgmy4NBQ7fpPjvbWW5nXhUznMFlk2Sk3jTZyq63EzUcLkUPUU9uhdKNSonDZq_EnR8RNcD7uxkx4i7y1f1uZ8NhwiVzs-7AA1Ka6ilt1FxY3UswqmtctpLzBo0c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb70e7631.mp4?token=Lqi8qAjiPpfr_BcbEwdcgm22lEB15hIJE3Ja6ka0lW0itrnIo47q2CQAJ6CRILEipZWYW_y0-QKwobgvbBQOXSy3rWe-QWklFHO7GTgGxpVJX4sXIn8TRXpUNr4BfmMlG8GRIZbQPKWLaDhpmOaYzWRcd7oN25__aFg2KxFhE7LRkthA7MMqCcBCz9tyTymMTIXoKe1iNPk2LeTgrHBYCoTImhNhRk7PtnrgaFN6OAPK__KIx1LQGrI1TG6uE_af2B9I639xtcM3PoQS8Q91sEPoWH6T1GGtDsiuvbAaPF4I3eVix4CPOKn7VOVlrsM5zkSKj_rcPP3-401_nNeKr1Memx_GF7rw5Q5RK-RyGTOPBeuok1foXvzOSpP1Wx7u7KHgp8E_HBHJ3kSWBAEQ2__jCeuldSxR4kxp83wFzL-sfJ68DXnnGKQkJnuV3dmWfdxVORNe2C_etFeDvKYovOeZBh-ibu1mtfRwwWMiaGQ9BxgSbPGO2Mu6AZ5A4kq0ZSavGGK0Do9UU2ApYyAGeAdB3XvvtHiDd43pxcyHyPSX17zYCgmy4NBQ7fpPjvbWW5nXhUznMFlk2Sk3jTZyq63EzUcLkUPUU9uhdKNSonDZq_EnR8RNcD7uxkx4i7y1f1uZ8NhwiVzs-7AA1Ka6ilt1FxY3UswqmtctpLzBo0c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
🇮🇷
حمله شدید پزشکیان به رسانه دیکتاتوری جبلی
: صداوسیما هر روز شعار می‌دهد اما باید واقعیت را هم بگوید
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65441" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65440">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65440" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65440" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65439">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nedH-HWagVY0rY8swrLe79iOQEnX8W5yDOPRCDRS7i5YEVoX0dnkQXC1I_b_p5huEVJ95YyVcS3_KXz5UpERRoVXz40ZmcW4ILssFfPhz1ZSxW4HPpm02YbJ1nmnfFU8tf_S-_2kyC0VQd7DVmDN6jMfyBYQa_yOn3XTBGYSWpI9AnYyiktl5uSMxd01apPBLkEoqmSz1Zdrn7LmxcuTf_jTpBgPby3PQ8hEUU07UMbef6GcXqFwZHxZQzoKYdWA_zGnUQ0TGKkMsTBUEbWnNxmsihJCR3-xIS8wrqhGeimVb7vbAlyPQ3wjMYNEjyrHEzqnpKd6VLAc33d6qgNgFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65439" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65438">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری‌فارس: سپاه دیشب در حملات خودش از آخرین نسل موشک‌های خیبرشکن استفاده کرده و تونسته تلفات خیلی خوبی از دشمن بگیره!
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65438" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65437">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8792984a2f.mov?token=tl7T0cq1VHB3nb81XKFClP0-jR4be1hoSCrftPuX-rBHOzDiTq0dhphA3ivFuqsz2jWLGOCgnDVAvpXqaBy9m5K8E9HtuCHzU2qKdiP-5iq4oxSu-bPljPCQT5fhF5AkDgqOITG7V6BULWKFEHMMOPE88zc_m49LmB3gzi95lmvbO2iR7ZO5gXPWzGjcYkf4ApJk4FvFUJbW01ajHNdssiyb7O9rJmTUyX7EIfKReH0fo0qzfl-_v7b5-Cpl4dxZbze9r13B0gW5bKTh33aPI_gxYsPIOYvH5d3OLxN9N-FXj2nusHrk4CHviFHOv8x6Hgo4DBGc35cDZeZ8hnyIunnKkkHdLPNbLCyu_BVyFR8GpfiQXIVvI6dxFrVlhsUXjKgww6XTJ8yXJbq98uRc4K0gTDaFSRoubLtTfuhWPr5KreodO7r9uFM07jx5zXxu1-vYKLSvbffrb4Yt-jpZCQYWt9JQQQ8ZEacqSGDh0QIsdSXUsOMvW-OkXkf9Hep9fSazjKalWyZxtCoAgaKBtLdbLQKt61JV_DEtiK3IjU_p0EAqsl_nbCTwljDPeKQ_am-DI1tSl39PRCh5-CUJTYtky3ksjvH2lixF0GyJ_hI2vM25xTQCf0TWDL43JZMNgB0rdVkqSKiSSHyRRKoJ2XUGftFjmCCccmu1pcKQVZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8792984a2f.mov?token=tl7T0cq1VHB3nb81XKFClP0-jR4be1hoSCrftPuX-rBHOzDiTq0dhphA3ivFuqsz2jWLGOCgnDVAvpXqaBy9m5K8E9HtuCHzU2qKdiP-5iq4oxSu-bPljPCQT5fhF5AkDgqOITG7V6BULWKFEHMMOPE88zc_m49LmB3gzi95lmvbO2iR7ZO5gXPWzGjcYkf4ApJk4FvFUJbW01ajHNdssiyb7O9rJmTUyX7EIfKReH0fo0qzfl-_v7b5-Cpl4dxZbze9r13B0gW5bKTh33aPI_gxYsPIOYvH5d3OLxN9N-FXj2nusHrk4CHviFHOv8x6Hgo4DBGc35cDZeZ8hnyIunnKkkHdLPNbLCyu_BVyFR8GpfiQXIVvI6dxFrVlhsUXjKgww6XTJ8yXJbq98uRc4K0gTDaFSRoubLtTfuhWPr5KreodO7r9uFM07jx5zXxu1-vYKLSvbffrb4Yt-jpZCQYWt9JQQQ8ZEacqSGDh0QIsdSXUsOMvW-OkXkf9Hep9fSazjKalWyZxtCoAgaKBtLdbLQKt61JV_DEtiK3IjU_p0EAqsl_nbCTwljDPeKQ_am-DI1tSl39PRCh5-CUJTYtky3ksjvH2lixF0GyJ_hI2vM25xTQCf0TWDL43JZMNgB0rdVkqSKiSSHyRRKoJ2XUGftFjmCCccmu1pcKQVZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فیلم دوربین مداربسته از لحظه حمله‌ور شدن الهه و شهربانو منصوریان به حوزه ریاست فدراسیون ووشو و شکستن دوربین مداربسته و درب اتاق رئیس برای ورود به اتاق ریاست
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65437" target="_blank">📅 12:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65436">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b744fd7fb3.mp4?token=saCO4Jy1tMY_l_pc4J8i3EQwXwB4U6kDfT9B37vpuXFMj6jOUi8LXCDfk__Nm2Q8bHYQSBl4dwyZ6vunG03rPEB3zNbgaBbThO8-UXUihlkmxCznCY-2DC3zqv_NtNfxoMUViPDr82DNVHXXu2iJAXvVixuK74mZIYhFvz8vr3S68Ja_OTAjszlWXt951MfYCq_OIFqdrkGVKa9OdL7wc7QOI-HaKqXJuiG1IVhXEAFdrdFm3ribptvt24YbXeubq8-pz-2axhNbBBOLbP4kYqDHMA8ftQ0nR6cAXCQarcEBqeKEqAPghGEE2kjxyWRIg4SeyBJcaD0hNY4zgJStQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b744fd7fb3.mp4?token=saCO4Jy1tMY_l_pc4J8i3EQwXwB4U6kDfT9B37vpuXFMj6jOUi8LXCDfk__Nm2Q8bHYQSBl4dwyZ6vunG03rPEB3zNbgaBbThO8-UXUihlkmxCznCY-2DC3zqv_NtNfxoMUViPDr82DNVHXXu2iJAXvVixuK74mZIYhFvz8vr3S68Ja_OTAjszlWXt951MfYCq_OIFqdrkGVKa9OdL7wc7QOI-HaKqXJuiG1IVhXEAFdrdFm3ribptvt24YbXeubq8-pz-2axhNbBBOLbP4kYqDHMA8ftQ0nR6cAXCQarcEBqeKEqAPghGEE2kjxyWRIg4SeyBJcaD0hNY4zgJStQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو منتشر شده منتسب به آسمان یزد
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65436" target="_blank">📅 12:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65435">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPwVHScDEe2t3QO8rYIMO-ddVKZTnYEJlLEUC-tyNRYnSqGhHeaGlhovuerrIJ4FPHsTkVKcJeaPTdehrVR-EivUzbPFOBHSVwV6YAYlihjE1YcPds1y2WayUfs7Ej5xYNN0qF7mJPtF0oay3EWf9W4GWYbDQqNryMuffFfjCG-5YewcLrUi8qAiBQH5TWwwthEwPL_V24ykv4FyK26ik72Fz0Tm2qmgJIu5zMm5PW4BM2Oe52ZNzvfARdkXUGKF2I3DkAsMw8dNbo6JrvYN2sIHUv3HwMliGTaCVfhUO9_5kfuLDixisAg8_w9kg63vVsSnw0dyC-wZH9MULN049A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
مشاهده ستون‌های دود از شرق تهران
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65435" target="_blank">📅 12:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65434">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
گزارش رسانه های اسرائیلی از هدف قرار گرفتن فرودگاه شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/65434" target="_blank">📅 12:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65433">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ اسرائیل: حمله به‌ نقاط مختلف ایران را آغاز کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/news_hut/65433" target="_blank">📅 11:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65432">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
صدای انفجار در اصفهان و همدان
@News_Hut</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/news_hut/65432" target="_blank">📅 11:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65431">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
گزارش ها از حمله به دانشگاه هوا فضای عاشورا
@News_Hut</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/news_hut/65431" target="_blank">📅 11:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65430">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
غرب تهران و کرج گزارش انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/news_hut/65430" target="_blank">📅 11:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65429">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
صدای انفجار های شدید در تهران
@News_Hut</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/news_hut/65429" target="_blank">📅 11:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65428">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8514d8db20.mp4?token=N8FlRE1RWh_idE2kYAuE-sy9qE0ZYLtmI5aFwUFdZ9zBSXmmKDojafLgG0D_OLR3CnN5iS3Th8tnXjtMzsyZ5yGc5mpk1L63AmmlJHHYVGgyK9SJwNcHXg1mn-imWBhuCDrLNNzvBkR9sc51uJ2bQADz09hgsl8Ub6WpAvgFnIIAVR2-yqccNIaccXY9jqxnecdWDWwFybj8HH3a19M0iGhZI3IGk93oe1UJW0fxahO6KG6QbjxUfk0VA9_sp0GhYTUdXDuYzP4JsUY6FdRBCltb5Gl3Yo4dvGzKF4oeMrWxMceXtWEOxNwsHNeNLm4Di0t-CP6Ors2QuLj04U1MHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8514d8db20.mp4?token=N8FlRE1RWh_idE2kYAuE-sy9qE0ZYLtmI5aFwUFdZ9zBSXmmKDojafLgG0D_OLR3CnN5iS3Th8tnXjtMzsyZ5yGc5mpk1L63AmmlJHHYVGgyK9SJwNcHXg1mn-imWBhuCDrLNNzvBkR9sc51uJ2bQADz09hgsl8Ub6WpAvgFnIIAVR2-yqccNIaccXY9jqxnecdWDWwFybj8HH3a19M0iGhZI3IGk93oe1UJW0fxahO6KG6QbjxUfk0VA9_sp0GhYTUdXDuYzP4JsUY6FdRBCltb5Gl3Yo4dvGzKF4oeMrWxMceXtWEOxNwsHNeNLm4Di0t-CP6Ors2QuLj04U1MHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
در ادامه اوضاع بگایی آسیا، تو فیلیپین زلزله 8.2 ریشتری اومده و تلفات نسبتا زیادی تا الان داده!!
@News_Hut</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/news_hut/65428" target="_blank">📅 10:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65427">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b691d50ba0.mp4?token=YT_8whCjd2tSgIuSg_OVw1ESztavqAXqJCvyaFGuDqFQJRYe1BoQKPGQrVLbTFXfNvyBzwVKHiqGcaVB0dwTO2ssN5VMDsYr7AUKgmm8rE1YxvEE9xBafUM3hSWq7Ox3zk_RhqVEj4t8kJca55HefzTwXBe-pAov4YbE9Mu1deUMDq9g15ARmHsD2g9vO9aCuFYClb2vikOMVV9M4Rvn5nQ5FduMEO8MsEfc3gxHHo-_6iA1YNjfnOBpuToiOmadrHguzAuXdflwaWHaA9hKyU7gNDAixTa7b6YHbVe4-uxqgL1j-EjZDlc27kktCaNhI1uRZvOzyTI1Fq_k8Y8S4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b691d50ba0.mp4?token=YT_8whCjd2tSgIuSg_OVw1ESztavqAXqJCvyaFGuDqFQJRYe1BoQKPGQrVLbTFXfNvyBzwVKHiqGcaVB0dwTO2ssN5VMDsYr7AUKgmm8rE1YxvEE9xBafUM3hSWq7Ox3zk_RhqVEj4t8kJca55HefzTwXBe-pAov4YbE9Mu1deUMDq9g15ARmHsD2g9vO9aCuFYClb2vikOMVV9M4Rvn5nQ5FduMEO8MsEfc3gxHHo-_6iA1YNjfnOBpuToiOmadrHguzAuXdflwaWHaA9hKyU7gNDAixTa7b6YHbVe4-uxqgL1j-EjZDlc27kktCaNhI1uRZvOzyTI1Fq_k8Y8S4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
لحظه اعلام خبر حمله موشکی به اسرائیل و واکنش هواداران جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/news_hut/65427" target="_blank">📅 10:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65426">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
فرودگاه‌های غرب ایران کامل تعطیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65426" target="_blank">📅 10:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65425">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EokxFpUbDVfh6I7yCSpAJAVdORsgX6lefHulaIEt9Y1wHGJ7AnIH6D6hzq6XdPprHqnyF3nR3BjK-x5MQWApXAEGh51UrR2zgi_AhC6LQqLiiuPig8fjHJWEPsZiJAHhlAhFFjLgzuqU_tKf82DlX8YZw6xN3Nh3nbrfhiq9heQyVI5H2gVrSPZQJ0QZzDu0oWa7mV6X-JA82hZBttUCP6KlE4QVjr2xMxNWi28rILPsOMPrFr2zssi1piMKESsBMjgJPo3NQVYj8tDoxq3ccIbt6FGToWs2phhbrNK7zdJ9VpDZdmcqL_cGk-d-VSMaWq6GBneVUeaXsp9xHyZMIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توییت ایلان ماسک درمورد ایران: « تنگه هرمز به نام اهورا مزدا از زرتشتیان نام گذاری شده »
@News_Hut</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/news_hut/65425" target="_blank">📅 10:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65424">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRmk9wHv2Y2kdTCFgChCbBQZiBNKdGj-qdiNz6Ma-dWeYfwcsSS5HkM4Yx2fTtgf7G0VUHZSHgijQs5Nfcieuaa69iZ5fWLxmrQcPMkgLe7_BV6w9VdBY8DqD6ldzXs-d2cPXVlCrIsOb_07HukdvGqveArSjxRbOCSx6b4oQt6OjTmokbr0hdkZdr5gJxR5bnHJybClLHy0b0DZLPj6svaZbceF6YdT81WgLV2jjFZu0IxZaXoIJfy5SQamDrv-HgkCSk9NrfaJlll6N3sjo6cyQXH5dHtkdm11bQk1hI48uFRtMtiWu6_li4dotdfkHiPzNJrqTUkPFnlax_1SXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
حمله موشکی سپاه به مرکز انرژی اسرائیل در حیفا و ناصره
@News_Hut</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/news_hut/65424" target="_blank">📅 10:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65423">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56aa95f90.mp4?token=RcuwT8LD0Qr5tTNE2DTGImsug1G55JCAeUBpIafSKJoX65cDJSU3oHi7tr0OjUsTPsTyqrXC-01Bkwdnv4HKAhu5PvCP3hVZ9hdQkk_MRn616_JzVL9c5vUOh2hGO1nywA9tmwrIBoZvkBNclh2uPt0jSbFEQos7RTFfICbNuC2_yQx_QVQHQaLoBnoVVBbM858xhoaqPUKo1EYkL2uKoFeyJmgtvCnDOsyTOFVkUG_bS6XbPzgn54IaSo_gfLJd6utfDBKBGB_m61Uv4bLv2NCtdgQwCp4-X6sZoxP2SlB-MIGjN4PrhsyY1nMN-q3Nw0PKxivW1NQwOHf3ykI_Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56aa95f90.mp4?token=RcuwT8LD0Qr5tTNE2DTGImsug1G55JCAeUBpIafSKJoX65cDJSU3oHi7tr0OjUsTPsTyqrXC-01Bkwdnv4HKAhu5PvCP3hVZ9hdQkk_MRn616_JzVL9c5vUOh2hGO1nywA9tmwrIBoZvkBNclh2uPt0jSbFEQos7RTFfICbNuC2_yQx_QVQHQaLoBnoVVBbM858xhoaqPUKo1EYkL2uKoFeyJmgtvCnDOsyTOFVkUG_bS6XbPzgn54IaSo_gfLJd6utfDBKBGB_m61Uv4bLv2NCtdgQwCp4-X6sZoxP2SlB-MIGjN4PrhsyY1nMN-q3Nw0PKxivW1NQwOHf3ykI_Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
تصاویری از پرتاب موشک از ایران لحظاتی پیش
@News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/65423" target="_blank">📅 10:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65422">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
با اعلام انصارالله یمن تنگه باب‌المندب بسته شد
@News_Hut</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/news_hut/65422" target="_blank">📅 10:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65421">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
اسرائیل هیوم:
یک پایگاه آمریکایی در عربستان سعودی هدف قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/news_hut/65421" target="_blank">📅 10:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65420">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9d994e5a.mp4?token=NwWz2c_8zztb16eZTXbLFc2Lb_46Kc_blx_AYr-70jVlQlRvQfclacqsvNNAQ0r8orW1ZY0Z61OgbTy3bCiZ_C0bxLIlV9eRYE-eM87x30KaPQ4bI8CTOcF63fxHNC3U-816G_0P7JgYv97ZRPxzLyFZFqSlTwVzQkvnGz7A8knhpUMbsK4FeLJ-TQXVSeCC3fsW1bv7wED3mPw97Bnw5Bk_17sa24TJIKzUbW_Va1IfbdRIdT9jxyLHxikpVfLLcKkN-87jjr_rI42sW5430_sYl05vZn2vzOUSiG0JVVyB5V2vyN4qbJk90Mm4UdRaCljiNy-hMwLlz92jPSXrxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9d994e5a.mp4?token=NwWz2c_8zztb16eZTXbLFc2Lb_46Kc_blx_AYr-70jVlQlRvQfclacqsvNNAQ0r8orW1ZY0Z61OgbTy3bCiZ_C0bxLIlV9eRYE-eM87x30KaPQ4bI8CTOcF63fxHNC3U-816G_0P7JgYv97ZRPxzLyFZFqSlTwVzQkvnGz7A8knhpUMbsK4FeLJ-TQXVSeCC3fsW1bv7wED3mPw97Bnw5Bk_17sa24TJIKzUbW_Va1IfbdRIdT9jxyLHxikpVfLLcKkN-87jjr_rI42sW5430_sYl05vZn2vzOUSiG0JVVyB5V2vyN4qbJk90Mm4UdRaCljiNy-hMwLlz92jPSXrxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
با تایید اسرائیل، پتروشیمی ماهشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/news_hut/65420" target="_blank">📅 08:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65419">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
پرتاب موشک از ارومیه ، لرستان و اصفهان به سمت اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/news_hut/65419" target="_blank">📅 07:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65418">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووووری؛ انصارالله یمن از آغاز حملات به اسرائیل خبر داد  @News_Hut</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/news_hut/65418" target="_blank">📅 06:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65417">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووووری
؛ انصارالله یمن از آغاز حملات به اسرائیل خبر داد
@News_Hut</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/news_hut/65417" target="_blank">📅 06:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65415">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
با توجه به شرایط خاص مذاکراتی و همچنین آغاز جام‌جهانی، حملات ادامه دار نخواهد بود  @News_Hut</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/news_hut/65415" target="_blank">📅 05:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65414">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
با توجه به شرایط خاص مذاکراتی و همچنین آغاز جام‌جهانی، حملات ادامه دار نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/news_hut/65414" target="_blank">📅 05:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65413">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b906cb3be.mp4?token=A3Z7EIal3y10Dz53Z8NSQR5dAMYVdfqmwKmmfnC78Ei0qflD3LEKdHRkH2_iLVMo-byJhJoIqWHv8lrGKi2lvduWJtQSjV9cdHTTkI_ESMTorz916RjlSPKc6_fde0TrrvKU-JQdcsgN8jyg2uFW0JWMoNIU1dxw06ENiHO5zu-Dr6HBj196hMPdtOG4IsvpRwoT0zX3j3QDTGA8pdM7d2PK8raa5UpPezLo93JYQaEui-yLz0Zz8g1oPzEmexaxTN9xhjkbMbn3-QvdYvpjgxnNrxUJZGK7QL1tj_W4A5Z2RYM4al3C-yQrvSo2VTSIHNyKqI57g-cjyeYIRK74tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b906cb3be.mp4?token=A3Z7EIal3y10Dz53Z8NSQR5dAMYVdfqmwKmmfnC78Ei0qflD3LEKdHRkH2_iLVMo-byJhJoIqWHv8lrGKi2lvduWJtQSjV9cdHTTkI_ESMTorz916RjlSPKc6_fde0TrrvKU-JQdcsgN8jyg2uFW0JWMoNIU1dxw06ENiHO5zu-Dr6HBj196hMPdtOG4IsvpRwoT0zX3j3QDTGA8pdM7d2PK8raa5UpPezLo93JYQaEui-yLz0Zz8g1oPzEmexaxTN9xhjkbMbn3-QvdYvpjgxnNrxUJZGK7QL1tj_W4A5Z2RYM4al3C-yQrvSo2VTSIHNyKqI57g-cjyeYIRK74tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
💪
گزارش انفجار در ملارد
@News_Hut</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/news_hut/65413" target="_blank">📅 05:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65412">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
حملات به تهران  @News_Hut</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/news_hut/65412" target="_blank">📅 05:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65411">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mprFH6nh6is94lsezPEOUxMrgbTIaCV7IO3G0I3qQb3rOlwz2AFoacWkBjPUVEtS5-IRQGHYmCYC9nuyp4AhnafXD0avt_xbyEAbIdYZ8Z5lFXMvq7r4eapAJnWHh293bxYlakjBhXRR5BaDNbFJE-zz0kYojZ_WWOhWgDHcqjHz81vWBcV3YqC9ElxtQgXZ7JXMAFlMO1tUMJej2m0KpbltJBPvlAdRUzKwCj4mEajNjvHUduQy-dUXTG_h2BBhEm_WBN_zHoqDJ9g2cT5xYe6jPHbAnEPPsm-jEQknVjxtNXqjFoJcFimZfg19eUjO_FrzlwvDT-OhtprnLq1uWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات به کرمانشاه  @News_hut</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/news_hut/65411" target="_blank">📅 05:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65410">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EigotLkWcRVW1LWqQg6EmLso2g4R45j9fncGNCK2wjFmBeKaRpATo1lzLG1HekLjwtyT7-0-GGoD1VkvD0IFkCE91GdKz4w0csCV2y8Y3iW3WMWPfa4YqenAf_iqlPnCRF4-lXRHXR6wTfrRHCk-EPj5t71Ei_CQElDqd9bqEFA8gU139uLRQXGkbSNV4-0GzjIfhzrnVL_kRWXyW4QQz_8mW-uuRr4OzoyW_nKK-8Jt943TUuQDgfcVM0NEK99vedqc_--hAQDz_dIbLwtd51M8TJZs7uqbxj8sscvGv3n6QcA7J2sQKUzm1PRB9D20pjX169c7sWSugM-QGm7RYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات به کرمانشاه  @News_hut</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/news_hut/65410" target="_blank">📅 05:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65409">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13951b2150.mp4?token=GObMjhFXUkRszATl05DsIQb6j3aF6ncgDD90gn6AbkqCy5ZthawsbP1lb1zXoJcsPyCfDlHTcRYzIc7F5ZwJbL_vMvG7U9AcLYYMtgWJZIxy6Xiq4GAAi24vkLfkqPBFZ4wXcDezV8dWdJuhVvvdy9e13M34QFlni4qPq1DdQQUZlqJyoTTa6SdV91sA9qeL-xQKS37TvJySsOvPng7ikcz9c1MASE8Y6ZSVorKeSKRFjkA0ubxWjtPHNOiDlH1OkH_yS2lvMFI09JPUyvcTivKNQ8EyVQO1o72QSILdvyTCVv7RUgYtl9oHTqFy-4Dj0-cOnCE4wTRjI4XMJnDfXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13951b2150.mp4?token=GObMjhFXUkRszATl05DsIQb6j3aF6ncgDD90gn6AbkqCy5ZthawsbP1lb1zXoJcsPyCfDlHTcRYzIc7F5ZwJbL_vMvG7U9AcLYYMtgWJZIxy6Xiq4GAAi24vkLfkqPBFZ4wXcDezV8dWdJuhVvvdy9e13M34QFlni4qPq1DdQQUZlqJyoTTa6SdV91sA9qeL-xQKS37TvJySsOvPng7ikcz9c1MASE8Y6ZSVorKeSKRFjkA0ubxWjtPHNOiDlH1OkH_yS2lvMFI09JPUyvcTivKNQ8EyVQO1o72QSILdvyTCVv7RUgYtl9oHTqFy-4Dj0-cOnCE4wTRjI4XMJnDfXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
انفجارهای متوالی در شهر اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/news_hut/65409" target="_blank">📅 05:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65408">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEFyJ07G6KEIDYeg5oIWADuLLspwbGTBgUHNEfhQjVz6rIorhA8fMBOyXAGofPv5RlKNgmXbP75GWPhhgGmBpQ6Yhhp9_hw7WKp4qAXL2TNwiLYVB1QJ6tyyEgfgvfKXqPg-KwIkhp5DERqXjWjtVfWrWL44URiN98DqYKuRVjHwGmzOWMn50ME7UUQg7jvz6dRTIXsGmLc7UeJHx38jdXceXFLVjspuasJ_PB4VZi2_F5Qrm3wTLoZkrtgyJvGcvuRpdT7vXcnTusrR6V8k083nuMvM815VaJKKCbfzijBS890SLybCEYTO4Iwyhz5BlX4A44lyVAosO-jp_HD7XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇱
نیروی هوایی اسرائیل اندکی پیش به اهداف نظامی متعلق به رژیم  ایران در غرب و مرکز ایران حمله کرد  @News_Hut</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/news_hut/65408" target="_blank">📅 05:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65407">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y5IdT4IWDV0GsQMmaOPjVgiTNDKHkn_kRiHNHoEHlXGPCkkcPDaNsFe4k2COa4uiWGH-GUC0F1dvk1OSjf-r5zhgFE9Xt3qBaHjxCE3RR8g061yrLNQ4egXBCQk-mfdzXVAgjHKFicB64KlZdRG9tpPo44XOmOEXkcsspY5O1DE5ZGDVnuL12-LTC7JtOKKwcVjOMMpqDHz_NHWKdTILFeQT0zzodh1Um9XKVTPf-Kp_QX0yy6-UdpZ2Ftp4APDT0i0aYICgF0kDp_TvLdwfKwK7zDVo63V3GUaifvwxorHkGoGE5iEVCD1QNsVSchGF9V2ZqMqzr6lsyAgM_pZ6iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇱
نیروی هوایی اسرائیل اندکی پیش به اهداف نظامی متعلق به رژیم  ایران در غرب و مرکز ایران حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/news_hut/65407" target="_blank">📅 05:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65401">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: نتانیاهو چاره‌ای جز پذیرش توافق با ایران نخواهد داشت.
@News_hut</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/news_hut/65401" target="_blank">📅 01:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65399">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
آغاز حملات اسرائیل به لبنان  @News_hut</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/news_hut/65399" target="_blank">📅 00:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65398">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
آغاز حملات اسرائیل به لبنان
@News_hut</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/news_hut/65398" target="_blank">📅 00:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65397">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل: رژیم ایران اشتباه بزرگی مرتکب شده، ما آماده‌ایم
@News_Hut</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/news_hut/65397" target="_blank">📅 00:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65396">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
ترامپ: نیازی به پاسخ نیست، صلح نزدیک است
@News_Hut</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/news_hut/65396" target="_blank">📅 23:53 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
