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
<p>@news_hut • 👥 228K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 01:38:00</div>
<hr>

<div class="tg-post" id="msg-65503">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/news_hut/65503" target="_blank">📅 00:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65502">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/news_hut/65502" target="_blank">📅 00:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65501">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/news_hut/65501" target="_blank">📅 00:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65498">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
مهدی خراتیان تحلیلگر اصولگرا: در ۱۸ و ۱۹ دی ۱۰۰ شهر یا سقوط کردند یا در آستانه سقوط بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/news_hut/65498" target="_blank">📅 00:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65497">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
♨️
🚀
خبرگزاری فارس: انصارالله یمن با پهپاد به سرزمین‌های اسرائیل حمله کرده
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/65497" target="_blank">📅 00:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65496">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🇺🇸
ترامپ به اکسیوس: ایران می‌خواهد به توافق برسد و این اتفاق می‌تواند به زودی رخ دهد
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/65496" target="_blank">📅 23:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65495">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/65495" target="_blank">📅 23:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65494">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/65494" target="_blank">📅 23:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65493">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
رئیس جمهور لبنان:
اگر حزب الله از تحویل سلاح خودداری کند، مردم از آن روی برمی گردانند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65493" target="_blank">📅 22:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65492">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
قالیباف:
هدف مذاکرات پایان جنگ و ایجاد امنیت پایدار است، نه عادی‌سازی روابط با آمریکا. ما نمی‌خواهیم از طریق تسلیم یا شعار پیشرفت کنیم؛ بلکه باید به دنبال پیروزی مهندسی‌شده با قدرت و عقلانیت ایرانی باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65492" target="_blank">📅 22:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65491">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
نتانیاهو به وزرای دولت خود:
ممکن است به چند دور (جنگ) دیگر با ایران بازگردیم، این پایان کار نیست
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65491" target="_blank">📅 22:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65490">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65490" target="_blank">📅 22:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65489">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNuSTVIh0pmAhVzvP4zKzP5-xSw5fAC4_X5fYEygP-UdJ9EVMO4dsaEdtplJsvXzpRhYIDvJuLAyUzmp3wmNygQlgEpo_-cQoQhQfVn3aGIHpAEiwaWDvJx32zMEWju7PQT2ZZzVY8X1kQlk9YDDx6ENJO0a3stMbIXK24_4vuDy7UuVEOFXfv1bE9X92lKrJyTUiSS3AYEvO89XxROH2NyUOv3k_16oPQnZM3xhGBNJt4HA9ahQ5ze_8fI2OspsEJwr2PvjUhovCyRjroYlIGaa3R8fjDz5Ool0b-BzKV6oGM7N6NAEpeq_yQD0yg_Rz9nl8yLUPHW17GIFOkoloQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
صابرین نیوز با انتشار ویدیویی از شاهنشاه آریامهر محمدرضا پهلوی سعی در مشروعیت بخشیدن به موضوع کمک به لبنان دارد
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65489" target="_blank">📅 21:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65488">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
مردم ایران بهتر از هر کسی می‌دونن که تا وقتی جمهوری اسلامی سر کاره، نه ایران روی آرامش می‌بینه و نه منطقه. صلح، امنیت و پیشرفت واقعی فقط زمانی به دست میاد که این حکومت دیگه بر سر کار نباشه.
راه‌حل، مذاکره با سپاه و مسئولان جمهوری اسلامی نیست، راه‌حل اینه که دنیا کنار مردم ایران بایسته و از تلاششون برای رسیدن به آزادی و پایان دادن به جمهوری اسلامی حمایت کنه
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65488" target="_blank">📅 21:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65487">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی :
این حکومت سال‌هاست مردم ایران رو گروگان خودش کرده و از جون و مالشون برای پیش بردن جنگ، ترور و بی‌ثباتی تو منطقه استفاده می‌کنه. توی این درگیری هم مثل همیشه، هر آسیبی که به زیرساخت‌های ایران یا مردم بی‌گناه وارد بشه، مسئولیتش با جمهوری اسلامیه. این رژیمه که کشور رو به این شرایط کشونده و هزینه تصمیماتش رو مردم عادی میدن
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65487" target="_blank">📅 21:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65486">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی :
جمهوری اسلامی باز هم برای حمایت از حزب‌الله ، کشور رو وارد یه درگیری نظامی دیگه کرده و بار دیگه نشون داده که منافع مردم ایران براش هیچ اهمیتی نداره
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65486" target="_blank">📅 21:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65485">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
ترامپ به کانال ۱۲ اسرائیل:
به نتانیاهو گفتم اگر جنگی تمام‌عیار علیه ایران آغاز کند، او را تنها خواهم گذاشت!
من دیشب از نتانیاهو خواستم که به حملات ایران پاسخ ندهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65485" target="_blank">📅 21:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65484">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
ترامپ :
اسرائیلی‌ها وقتی جنگنده‌هاشون تو مسیر ایران بودن، به ما خبر دادن.من هم سریع وارد عمل شدم و تلاش کردم ابعاد حمله محدودتر بشه!
همچنین پنج کشور منطقه با من تماس گرفتن و خواستن روی نتانیاهو فشار بیارم که حمله نکنه من هم با نتانیاهو صحبت کردم و اون در نهایت موافقت کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65484" target="_blank">📅 21:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65483">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
سازمان هواپیمایی کشور: حوزه هوایی کشور به وضعیت عادی خود بازگشته است و عملیات پروازی طبق اطلاعیه‌های پروازی صادر شده (NOTAM) از سر گرفته خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65483" target="_blank">📅 20:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65482">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65482" target="_blank">📅 20:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65481">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwDjw2avPqrTXE5-8i4ThobF_rej6WJvyGVrVKlSjBvHVdZ5QCV420cBaZM8VEWYm8rYwACbtoxSuQEFAAl1b-NTrZ6CtBPX6Mj_P4FdZllph2_hiGpZNxgiHEeKt4V1nIUhb79yp4C5k9EFporxFR7BlSsBCT-14_FfejWucQTG5GfleH7-pYruqA3bluwxB3da15cL-1ahF3HZYspYr0ISPmzJ9dCSAd0qscqoQ81F6ueoPCwDv1zaRM4nbEi9_4fHv6KBvCuS-X82WG0PB2AFBBbNrfx6Qt4W_B8tsu5nvo3T1GmyU2rUacHWts7EeagNZLsUVRX1rk6_HpxprQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
نیروهای ایالات متحده یک نفتکش بدون بار را در خلیج عمان، در 8 ژوئن، پس از اینکه کشتی با تلاش برای حرکت به سمت یک بندر ایرانی، تحریم‌های جاری علیه ایران را نقض کرد، از کار انداختند.
فرماندهی مرکزی ایالات متحده (CENTCOM) کشتی M/T Marivex با پرچو پالائو را زمانی که در حال عبور از آب‌های بین‌المللی در خلیج عمان به سمت ایران بود، از کار انداخت.
یک جنگنده F/A-18 سوپر هورنت از ناو هواپیمابر USS Abraham Lincoln (CVN 72) پس از اینکه خدمه از دستورات نیروهای ایالات متحده اطاعت نکردند، یک مهمات دقیق را به بخش‌های مهندسی و فرماندهی کشتی شلیک کرد.
ماری‌وکس دیگر به سمت ایران حرکت نمی‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65481" target="_blank">📅 20:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65480">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/65480" target="_blank">📅 20:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65479">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65479" target="_blank">📅 20:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65477">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
رادیو ارتش اسرائیل: ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند.
«این حمله گسترده انجام نشد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65477" target="_blank">📅 20:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65476">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
فیلد مارشال ، محسن رضایی:
ایران از غنی‌سازی کوتاه نمیاد و در موضوع آزاد کردن پول‌های بلوکه‌شده جدیه. اگه مذاکره نتیجه نده، محاصره دریایی رو تحمل نمیکنیم و اقدام نظامی انجام میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65476" target="_blank">📅 19:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65475">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
ارتش اسرائیل تعدادی از فرماندهان ارشد حماس را ترور کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65475" target="_blank">📅 19:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65474">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
نتانیاهو:ایران فکر می‌کرد می‌تواند به خاک ما حمله کند و ما واکنش نشان ندهیم، این اتفاق نه رخ داده نه رخ خواهد داد، دست کم تا زمانی که من مسئول باشم
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65474" target="_blank">📅 19:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65473">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXUcLTtt_6-u1bOwuEmDgqO3Fyr6h3XW-DaeucxiSlUlYfcbJJb-J1aLrQ0lTfHO1A0lvaW9yaul9SItp7Th3YQhJagO5QCm5jo-J7oaAiZTiA6zgdjg5enHRwlnB7Ew7oXAsha6QyizIyeqkM50GH1qlP04DUuwZP2m6VX8xdJbQD7LxKJjrlAc47cpbTt7FWw36Q29VXyvpEEfEbPP9rje6FVzJ9lusPC2oLYYTNyWQHRhfTgZT-CtYr-6phLkxN7_soHE7E7njgx6AHKUuLG7kffVqq9xtw_7MfwSPNvhYa-L--1YUIkswV9ZrWTxyT8NesYPkSb15OgYIa0uCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروی دفاعی اسرائیل (IDF) دستور تخلیه محله زقاق المفدی در صور در جنوب لبنان را صادر کرده و به ساکنان هشدار داده است که فوراً خانه‌های خود را ترک کرده و به شمال رودخانه زهرانی نقل مکان کنند، به دلیل حملات قریب‌الوقوع علیه حزب‌الله.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65473" target="_blank">📅 19:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65472">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
نتانیاهو:اگر رژیم جمهوری اسلامی اشتباه کند و حملات خود را علیه ما از سر بگیرد، ما به شدت پاسخ خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65472" target="_blank">📅 19:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65471">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
نتانیاهو در واکنش به اظهارات ترامپ: اسرائیل حق دفاع از خود را دارد
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65471" target="_blank">📅 19:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65470">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
نتانیاهو:اسرائیل فعلا از حمله به ایران خودداری می‌کند ولی ماموریت ما با حزب الله هنوز تموم نشده
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65470" target="_blank">📅 19:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65469">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc930bac93.mp4?token=VgKUq8-JYoQlHDlbPT85SSRO7nIx4CgvGgis1gi2fvSe_WWoakMDMIbXbu6AYOKXLNdH4vljthONWeGlhzWACNSHT4zdUmv7_ezO0aIs8Q-XGFS8rf3yBRc8sCDtPHtPb7qk0ZBsdHS8Nit20IL7aaq53x-_MNGBgyH1Cg7znw_I0jH9Oh-WgWv5X3VLLFU97Zx-FOfNzFnDSOtcd2zKDSR4I_asmBZT39KZpzMB9gZocMcvZp0zaiBnitHJnzSL_Wf46Ep01N7_eq10Xnzw_zAili1iF6L77bgdoGPlU1fdKzi7TROk4IaOxvfGlofAee7EJ5Lz1yB-wc_wYtPBvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc930bac93.mp4?token=VgKUq8-JYoQlHDlbPT85SSRO7nIx4CgvGgis1gi2fvSe_WWoakMDMIbXbu6AYOKXLNdH4vljthONWeGlhzWACNSHT4zdUmv7_ezO0aIs8Q-XGFS8rf3yBRc8sCDtPHtPb7qk0ZBsdHS8Nit20IL7aaq53x-_MNGBgyH1Cg7znw_I0jH9Oh-WgWv5X3VLLFU97Zx-FOfNzFnDSOtcd2zKDSR4I_asmBZT39KZpzMB9gZocMcvZp0zaiBnitHJnzSL_Wf46Ep01N7_eq10Xnzw_zAili1iF6L77bgdoGPlU1fdKzi7TROk4IaOxvfGlofAee7EJ5Lz1yB-wc_wYtPBvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو: ایران و حزب‌الله از همیشه ضعیف‌ترند و ما از همیشه قوی‌تر.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65469" target="_blank">📅 19:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65468">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
نتانیاهو:ایران معادلات را بر ما تحمیل نمی‌کند؛ پس از شلیک حزب‌الله به اسرائیل، به بیروت حمله کردیم؛ پس از حمله ایران به اسرائیل، به مناطق مختلف ایران حمله کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65468" target="_blank">📅 19:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65467">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
نتانیاهو:نظام ایران پس از پاسخ ما عقب‌نشینی کرد و اگر اشتباهش را تکرار کند با شدت پاسخ خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65467" target="_blank">📅 19:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65466">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو: تسویه حساب اسرائیل با حزب‌الله با قدرت ادامه پیدا خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65466" target="_blank">📅 18:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65465">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53d663dc6e.mp4?token=Fu5sprlGXP_NaRYBewypNk_qQYcd8F6_COae3sXkV-nT-c1Sa1niD6J7o2J9wHBxsUHHgCfssDU4-_X3jmsnTISuvML0XoeatwBwohwQ0uKTDOjM8XOvhKPirpgtZkkwDycz-etrqatjENQ128RgVMkIVl6beosFPbMxU-H3LGqSNijOujyY9uXiL7EQhOoccn8NslQuCI-NGoB2nKXC5pwuTm6oXT7Wo0wTEkwPlV4EgzToXSNN-SPENnb6jEj15cyzyRS9188B3ynivPkZYskYxMCgrqATHuGGCCqCf0zSatcD3AD_KbJTiRsGN_KbUPbmAgE_fHPeIuPds3K7FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53d663dc6e.mp4?token=Fu5sprlGXP_NaRYBewypNk_qQYcd8F6_COae3sXkV-nT-c1Sa1niD6J7o2J9wHBxsUHHgCfssDU4-_X3jmsnTISuvML0XoeatwBwohwQ0uKTDOjM8XOvhKPirpgtZkkwDycz-etrqatjENQ128RgVMkIVl6beosFPbMxU-H3LGqSNijOujyY9uXiL7EQhOoccn8NslQuCI-NGoB2nKXC5pwuTm6oXT7Wo0wTEkwPlV4EgzToXSNN-SPENnb6jEj15cyzyRS9188B3ynivPkZYskYxMCgrqATHuGGCCqCf0zSatcD3AD_KbJTiRsGN_KbUPbmAgE_fHPeIuPds3K7FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
سوخت رسان های آمریکا در فرودگاه بن گوریون اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65465" target="_blank">📅 18:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65464">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
بنیامین نتانیاهو تا دقایقی دیگر سخنرانی بسیار مهمی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65464" target="_blank">📅 18:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65463">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
وزیر دفاع اسرائیل، ایسرائیل کاتز:
وضعیت در ضاحیه بیروت همانند شهرک‌های شمالی است. هر حمله‌ای به شهرک‌های شمالی منجر به حمله‌ای در ضاحیه خواهد شد. ارتش اسرائیل به عملیات خود در لبنان علیه سازمان تروریستی حزب‌الله ادامه خواهد داد. ما تهدیدات ایران را به‌طور کامل رد می‌کنیم. هر تلاش ایرانی برای پیوند دادن لبنان و ایران و حمله به اسرائیل با نیروی عظیمی مواجه خواهد شد، همان‌طور که دیروز اتفاق افتاد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65463" target="_blank">📅 18:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65462">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3210944dde.mp4?token=LqOyMTmALf683jCigscgJDCu_hQwwxlzyH4ABGsFcmWFGEjmTC6T1iGvuEmZiYzDVC4UlWPu-plU-NuiPKGy4YXOY8osSQkD55ceXX6LNWfI8E2yHUCGerhowC0CcVISWEmeoWcbtOa2j_crnwgAoepJ9x6Oue6zIPWQKrxHCalGFIphzO0ZqcKk70Hg-mon6w2ozwBb9mZQyEtQCsSHEbZxUG0eWb6UqFnz0s88AVqaofwPO9bk6KPISQjC078fYiiKos7bNJjxIDjt1TTwhqlOAe0pUWNOv64Of1k-ccxs24__yLAm0ryPJpYQUK0_7Qomxw_ZV8LRVS3XSQJOsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3210944dde.mp4?token=LqOyMTmALf683jCigscgJDCu_hQwwxlzyH4ABGsFcmWFGEjmTC6T1iGvuEmZiYzDVC4UlWPu-plU-NuiPKGy4YXOY8osSQkD55ceXX6LNWfI8E2yHUCGerhowC0CcVISWEmeoWcbtOa2j_crnwgAoepJ9x6Oue6zIPWQKrxHCalGFIphzO0ZqcKk70Hg-mon6w2ozwBb9mZQyEtQCsSHEbZxUG0eWb6UqFnz0s88AVqaofwPO9bk6KPISQjC078fYiiKos7bNJjxIDjt1TTwhqlOAe0pUWNOv64Of1k-ccxs24__yLAm0ryPJpYQUK0_7Qomxw_ZV8LRVS3XSQJOsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو ای از اصابت پهباد به مواضع گروه های کرد در شمال عراق
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65462" target="_blank">📅 17:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65461">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
اسرائیل هیوم از منابع: هنوز هیچ محدودیتی برای فعالیت ارتش اسرائیل در حومه جنوبی بیروت وجود ندارد
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65461" target="_blank">📅 17:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65460">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65460" target="_blank">📅 16:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65459">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnWEQtCdgFYInPfBcemqse7uYgMjeDtWz8XpI3r_XuN2ZuSNV2lqq4RIf78CYFKaJs47Hw3hwKtgp80tUpdvFkmrpyLm33L_2Tp0tJeZOvW30XbRkFcljQJALwJpK4gPAd_ODz-k2w-5p68Ya8BQG612ZrZziLEteemhEU5NjGQNlthq6ISkfdmNVuVn0LO9GzLw8pQvJnqHSAPe6190a2K2sWgwze8di6rDeXlWaUy_U7W3oflBVGfqUkLMlHCMnkv0tGyB94g6b1V7RNyj-64pGCgmIASA9Jv6ujgB8nzYiOr540ykLirMMGhL33eowKR3oQg_OrmTErW0_7lKfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری دیگر از جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65459" target="_blank">📅 15:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65458">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7kjFsOSlvudLjrQRj3O7Q0gJ4178E0E49k1R5uZ8Gou62wUX5LhpgwNLEmBeZvK6xFuQnP9N55CtphDmdvhPmWVDVMvcXOolTeIKutmVpf7GMsDFv7Yh0Gl0lwyAzLuU2ACbvKobFDZZdyzjJLfLFHuPyEM7iqs7GzxtJi9KRsGPeuTTN8huzMExzutiIBj768ooR0_-A2j-we5FucP-p3haTl2XihRXfFKdObmxlR8hmXngy-PaaxFrm6uile0T4DuaIjQ1iPwDN259Ax6w0nZzwdEbnokFNcJIL3SG2umty-mFmssSlGqK8zQIM2p__PCk_NgGilTVG2NbWGHSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش ها حاکی از حملات مجدد اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65458" target="_blank">📅 15:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65457">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMNv4ysBae8bBTI5hjpRR0ty33AXtuxNUtmAfYn40nY4BLIw4edBdJHRZWaBkQL0O2vbTvEVzFNhOCP7j4YvyaG6Cabnmm9QVVTRia_tVstmP5l7xk5rMcNLnc9uP-hvB3qt_BHvB_qNyVaDKvqGALqXbXyIazSAH9M4vLz0PIcxBznj8mNdcGBSUPldpkUgRCqTdD2aA7LZ8E_C6kyfuwl6g5tXOAzOUv_o8ESuKEEyI2JM2KIhz5Hfw96hlxLnv75tCBEy-rR4DrGbhNd7pHTlEFG3sMIXYw_xfWpwuo4Q6c0KMQS_gn4qdZFfiMqvrIYkcPTn4ULJH7wQTn1bHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما پایان درگیری‌های دیشب و صبح امروز رو رسما اعلام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65457" target="_blank">📅 15:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65456">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇮🇷
فرماندهی قرارگاه خاتم الانبیا:توقف عملیات نیروهای مسلح را اعلام می کند. با تاکید بر اینکه در صورت ادامه حملات و اقدامات تجاوزکارانه از جمله در جنوب لبنان، اقدامات قوی‌تر، خشن‌تر و قاطع‌تر از گذشته در راه است
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65456" target="_blank">📅 15:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65452">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VoltcB2dRwVE0_h56r2I2vudF2mFPSxNUm1pnf00z5syucIxtDMsQoj9p0h7Z190ofC4I4LTV5GITIvfDQp7g5gq0pzsrsd4CmNB4zV2BVNzqKesxtXqhgNLIzNIIo6yiD0fq1C67jno5oylWwGoIkKxilY4RH0dW52GBt-SoWepOxY1iuzQHI3NE-ifRuKMN0zgv4rMbabM4Pcnqzqzk1QaXexdPxYllh842NAD39WOas_xq_xM-oAKNbin_llIgNBCWP67WiwF7T3QfRLWUbedZckgqe9iMvKAx5VCD4SPp_QqG_Jf1dDE_GFONBuceu0bZUS3IQFcqX_l9xiSEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FN22t3xj6yzPBzLB93OhDnAb29rwZmhJMHSB609aXahQ67hG4de6hjQ5SsDI_2PKz3hnD_FU_po2yTUWek7RaWmhJaZjMuGGh3fTTPkDaygcucWxVNr9cJX7Dx034yqZzRRWDyOOd5D0dZ56rdYTnHpzrluOz61T9FOwKONhhPHNHzN2YHEM_HN5BaiR3F85_nsmj_4hxM5PJ5AJTgd6LbJRAQuskBaLnN_ZP17PcKuz2SdpLg11Do1DUCqz3qGG1hhcN5iu8ZhN_VwNJ10J2zgcVWwOsf9g940baFmLvv7F3FdPGZ4jXpJ83uiGmS2FVS23bbLOPV1hSr_jh-k2TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kjAzZ-qn0i08yO5pcXCKk8XPg8r5Hvi_pv0KyncpfSVo1Cw2lOTfwteJZr765samUOlp28LbJOT33v9HoEngquS8UayJS1fD6rSBhzra-6S7mEf4BhJr-Q6Jta0XM4KcplEEi6T0S4hZ3k383U5Mu8RGsM-0w-VZFwWzud4gnpjzsdAXQQ77-91v1Lse85TBUasJqD0Y8tB2ZqucoGl9oQgkNms34Y5hfaLCqVNpZc8gIChC0axfXc09LwQpGbfR0sy9Hs0m1HLM5WFQasCFUUCPQm82ILREBzeZxEe11dA_GaOA7uQLd-LkiS4meGnqxUtlpbAb4Hf13SChB5wGlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0wAoZrZx-rsCyftKRq66dscVN67uix2mmx2xJLcnxkXbybxi2lA0bNfu_eOTafl6cW_fRAATR-nrRhqJqgD1jM8-hMHMkYrQdeC7OhfPj_8QZaNjEqObVnBTEsLk64yxQpkkaw66QuZNgrjC-xEuFFdExD6Vykz6Q9Hf1LpyvORsiZ4nQ2yFBTxQFBBKnm741FGk7qhHe41aGqn3XmBSSM7g3NFlSN4RTWxtB145_0KdmWxouemYacVQZQ9xCB6_nokIq9gfUdZDmOZkD63yFculVqonKSxd0kjF5iqivWfaJxPc5ENpLRZtm2Gzr3uWRaPu9skEGm-rVXD9MKw8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکاس
اسرائیلی
؛ رفته کنار یه پوستر موشک ایرانی که تو اریحا فرو رفته، وایساده و عکس گرفته
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65452" target="_blank">📅 14:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65451">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-text">سایت های شرطبندی به دنبال ترورش هستن ، به عشق مردم داره میگاعشون
⚡
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65451" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65450">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65450" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65449">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XD8cYoM2OEQ7nlgB0WI-GkTQ65gO-N_aVHncI7c98Bker6RQSOk1hDIHLDzhGPlvOXA4vDqAUTwYFB3qKWtonkPb8Qt83RCNOZsROXMnmjJjjnPvJwsNPkXUc8vQl0z_R5oMmNyFoC73V1zasOyxsHcN3ypo1w3P9OE1C5VGaKllp_em2tVsrLNXPHgM_RUpNl-iz6d75QVeTNANjb_7ZzbVxK4t76s2W0syXmqTLkyrStnJoqch5Aa2hieS9fqzDn3FOhYAVju1GPYbXCf0dTuzBEt6c1jVNBkBzn8_Yb-TJr7i3CHt2Uwcot3Zjxi94G6xyYu8L67_9lHmqM8bBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:هر دو طرف، اسرائیل و ایران، به دنبال برقراری آتش‌بس فوری هستند!
مذاکرات نهایی درباره «صلح» در حال پیشرفت است، مشروط بر اینکه جهل یا حماقت مانع آن نشود.
محاصره با قوت خود باقی خواهد ماند و با قدرت کامل اجرا می‌شود، تا زمانی که «توافق نهایی» حاصل شود.
اوضاع باید سریع پیش برود. از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65449" target="_blank">📅 14:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65448">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
یک کشتی هندی در دریای عمان هدف قرار گرفت و دچار آتش‌سوزی شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65448" target="_blank">📅 13:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65447">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNj8_LIdPZ3ag1tx0kSNrzNXDNkr-J7o2ZO2l-xnli5thK7pNvbnc1QpS6UbSjFPYLIGG8S5-yKw3_2RbyVeIp7yPliBfaO-LziSE9idnZcl1mSpy0SPt-qkyJiOZW-sIg8cZ_F8OljTJf41J3az_gekjFeTb0hoX20BAn0rrPunX1gAedV3BY__Mq1A-b0-Vy7-F-ZOaRZ9YDQDJDWIF9MwUfpAFsyYMe2OIR7da-OEgMk7XnTEijt7iLnS8QqpFEr-kSDf-Ca-1sQ-9XCwSMO3p6uD-2IV8nF1omOJ3N2-H-Pp4wAumEQE9SJAop5Z9Tp0Vf3XD6gbgWxMrsaJgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
دیلی میل| یک فوتبالیست بین‌المللی متهم شده که در یک هتل پنج‌ستاره در ترکیه تلاش کرده یک دختر ۱۴ ساله بریتانیایی را برای «بغل کردن» به پشت یک پرچین ببرد. پدر این دختر در گفت‌وگو با دیلی‌میل گفت که دخترش پس از این اتفاق دچار وحشت شده و در حالی که اشک می‌ریخته با خانواده تماس گرفته است. این حادثه زمانی رخ داد که او همراه خواهر ۱۰ ساله‌اش کنار استخر بود و والدینش حضور نداشتند. دختر ۱۴ ساله که از دیدن یک چهره مشهور هیجان‌زده شده بود، از بازیکن درخواست عکس کرد. پس از گرفتن عکس، بازیکن تلفن او را گرفت، اطلاعات اینستاگرام خود را وارد کرد و از طریق حساب دختر برای خودش پیام فرستاد تا ارتباط برقرار شود. به گفته دختر، پس از آنکه او سن خود را اعلام کرد، فوتبالیست او را هات خطاب کرد و درخواست بغل کردن داد. وقتی دختر مخالفت کرد، بازیکن اصرار کرد و از او خواست به پشت یک پرچین برود؛ جایی که به گفته او هیچ‌کس نمی‌توانست آن‌ها را ببیند. دختر که ترسیده بود، به او گفت پدرش در راه است. به گفته خانواده، بازیکن پس از شنیدن این موضوع به سمت دیگر استخر رفت و خود را پنهان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65447" target="_blank">📅 13:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65446">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
اخبار جنگو تو چنل دوممون پوشش میدیم عضو باشید
😉
✌🏼
@Futball
@Futball
@Futball
@Futball</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65446" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65445">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzIFQ91A74l6xRcbPkN5qTjm7Ec3FHYidA6FaA2I5s-CJgGmSpx20z56oKypxOK6wrF_1e9oT1JQgtnIeTl4r2OA6D1Vr99faUEth2wgxlyje1rqytrSbHdUGC-ogLC_jJf0V2momk1ftbDQG87q2GWC1TWYbjVqQzDO_KYfA7sPBDPpb_JDvjN0nV8jYHJybbyz7azksIl7OUfRSV7Sv6EK2xre1oX7ieZNjBJfR3icSLhytv90sgJqX7FICZ2-AZP7J0f6F8ISHfW3ZxDm81K_vnr-veEQ4L_Ao8bzXEV8IpwPnfLkTE8VnZV92SafQ9uWxz_kpA81DMb1GEOh5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65445" target="_blank">📅 13:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65444">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
مارکو روبیو:فقط کشورهای احمق وقتی به آنها شلیک می‌شود پاسخ نمی‌دهند
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65444" target="_blank">📅 13:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65443">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇮🇱
منابع اسرائیلی: حملات دیشب و امروز کاملا با اختیار و بدون دخالت نظر آمریکا بوده اما سنتکام در رهگیری موشک‌های ایرانی کمک داده
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65443" target="_blank">📅 12:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65442">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65442" target="_blank">📅 12:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65441">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb70e7631.mp4?token=rHoGH6F9KI7mPsjkWaMvjbX10xQBNOGY0nQ6QkfjtqCfValhLVqry_dCGaZpix9sml5byiFKxc0K4jeDO02OgSqUa51Frc_FH0nDsD_VtS-be6vPS-QOuw8dEcHDf4RDXTqTXrNPYtagHxO61qefE-s1GKuzJQhJbqJv6947JgRMGLSVJfJovzkSMdMpjYJ4NwxFdurzUd77G0XITJG8k8Bz3mpvIy2GtBSdUcbI4EIgJ5KlpaXtz2fV3eqU1bJ-gyPvw4KT0stZIKt0UHXn1snXwRhziXsp85DZqiYK9s7riVpNFzNje0aitFCSczmUO5Z656FaoKDxlJngXjbDw56Cow7V39VPw7-KLDV0QOL2sXxA0Jay6yg3QVSVFf-dp0YFSCHoKnssXiHQjUc8gajaz7WKS0ErYrG8A7OfSgf81G8-RMTdvjCEbaTclf_bhF_XxVKxvrG9m_Tj9tIL8894Sat7IgcPzqb4IrihQPo1bvzaKnB4fxddsfqGb_YeZyvA71TyodSXsW5zdXh9mWGHyu7J3Au070bhD1s1tT5dJWKO8iJOPfOooI6Qdg_0kl92TTYkzboJFUfM3PygF0kS79v5IieU3TWiki_cq4PDXRZwZiqTTHf3gsopYiO4AX1fKm7jo1hufRbVPhR2OJa0pE7HpSRq0j5p1sfpeBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb70e7631.mp4?token=rHoGH6F9KI7mPsjkWaMvjbX10xQBNOGY0nQ6QkfjtqCfValhLVqry_dCGaZpix9sml5byiFKxc0K4jeDO02OgSqUa51Frc_FH0nDsD_VtS-be6vPS-QOuw8dEcHDf4RDXTqTXrNPYtagHxO61qefE-s1GKuzJQhJbqJv6947JgRMGLSVJfJovzkSMdMpjYJ4NwxFdurzUd77G0XITJG8k8Bz3mpvIy2GtBSdUcbI4EIgJ5KlpaXtz2fV3eqU1bJ-gyPvw4KT0stZIKt0UHXn1snXwRhziXsp85DZqiYK9s7riVpNFzNje0aitFCSczmUO5Z656FaoKDxlJngXjbDw56Cow7V39VPw7-KLDV0QOL2sXxA0Jay6yg3QVSVFf-dp0YFSCHoKnssXiHQjUc8gajaz7WKS0ErYrG8A7OfSgf81G8-RMTdvjCEbaTclf_bhF_XxVKxvrG9m_Tj9tIL8894Sat7IgcPzqb4IrihQPo1bvzaKnB4fxddsfqGb_YeZyvA71TyodSXsW5zdXh9mWGHyu7J3Au070bhD1s1tT5dJWKO8iJOPfOooI6Qdg_0kl92TTYkzboJFUfM3PygF0kS79v5IieU3TWiki_cq4PDXRZwZiqTTHf3gsopYiO4AX1fKm7jo1hufRbVPhR2OJa0pE7HpSRq0j5p1sfpeBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
🇮🇷
حمله شدید پزشکیان به رسانه دیکتاتوری جبلی
: صداوسیما هر روز شعار می‌دهد اما باید واقعیت را هم بگوید
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65441" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65440">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65440" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65439">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZ1p-4botu-fCaOUjLNU_3IMJWTdEbT0Fhxu5dnt_Pr-AKxNqMsbQC6cn4datK5n75GBEUynIVEKGc0k4t4G7PBnfJx9jFtn3djYBFIQcHVz6u2JRBK0VvSklBD0qmf-xSnRl8_jWao-AIFN-Wv6oVypu8Lrgc6fiaCcUs29dxILjLlivpa9kneGEG25JWczWwsIv_IkIPU3DDUNr8djV5U-OI08xgfe5EPJXTAFDO-w_m3ix-9SBS5iEBqK5HOSXgRSXgTHK1lla2bKBkLfLOBx7YmSOFgjcylK81c1SDohR-QjMO5EEFmxMjVYeSZpax04h9W4GNnoCLH0m3i17w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65439" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65438">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری‌فارس: سپاه دیشب در حملات خودش از آخرین نسل موشک‌های خیبرشکن استفاده کرده و تونسته تلفات خیلی خوبی از دشمن بگیره!
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65438" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65437">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65437" target="_blank">📅 12:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65436">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b744fd7fb3.mp4?token=ZODW4-hURowo4qiEjEkyeTmycflRLHm0N651ZlZvHSd8QNnj16cM1zCbUjJAMGFkAT0jMvy7x4zhuPqXHNT06rRuqufz7oJQbDG_zo6KsbVybu6ASLByIgD9FS3waoDHYywG6JmOaWQ8K8ZwvdCbf0317qFmV-ao7Ob2Nu3KI12_Vz1muURVmG-6jk4wjOz10NVkH57g6jTuduINSazDkPiIoRz70xieLomTdeuHsI0t1UxXpa-dpVOo3iwRNlpwo54_nTvMnhiWtpTcRAhlNjNiXS-oCKAYrKhNFsnB7SfQpixqU8df0pW5aUYhFxxftgDrxlpRzWx_J_lEATFnKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b744fd7fb3.mp4?token=ZODW4-hURowo4qiEjEkyeTmycflRLHm0N651ZlZvHSd8QNnj16cM1zCbUjJAMGFkAT0jMvy7x4zhuPqXHNT06rRuqufz7oJQbDG_zo6KsbVybu6ASLByIgD9FS3waoDHYywG6JmOaWQ8K8ZwvdCbf0317qFmV-ao7Ob2Nu3KI12_Vz1muURVmG-6jk4wjOz10NVkH57g6jTuduINSazDkPiIoRz70xieLomTdeuHsI0t1UxXpa-dpVOo3iwRNlpwo54_nTvMnhiWtpTcRAhlNjNiXS-oCKAYrKhNFsnB7SfQpixqU8df0pW5aUYhFxxftgDrxlpRzWx_J_lEATFnKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو منتشر شده منتسب به آسمان یزد
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65436" target="_blank">📅 12:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65435">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDuhyYc3LOdly4vbiWTAkdtEsbb5em0fTayZ48nkMZ4L5Ng_XBJMryskrGGF--bguGIBDhiGxDPys7EcL8UxZdLUwcOzLiKVRhpA8lxdDZstryPOxc0uRhYxgmYCKY4UPj6tUmwQ3s4Hlv5ARvQ0_Zs32aLey0pNDzVtVtG4bRzv-N8s8suSh3PkNuTCV2sOlwGr4qXAPTPsQeZV6dysXMsMM-CVpM37PLCBfNGx-V-FVgQR0ArCy5WWn8DNOzJ94uIzgo3ddztmXa0BRYHc6FzztsQ8pGukC4U94Hx1AdBHLVsWPMFjVdcTVh9xoc_ue1ViSWbcyYLcV4yY_fdFYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
مشاهده ستون‌های دود از شرق تهران
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65435" target="_blank">📅 12:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65434">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
گزارش رسانه های اسرائیلی از هدف قرار گرفتن فرودگاه شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/65434" target="_blank">📅 12:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65433">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ اسرائیل: حمله به‌ نقاط مختلف ایران را آغاز کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/news_hut/65433" target="_blank">📅 11:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65432">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
صدای انفجار در اصفهان و همدان
@News_Hut</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/news_hut/65432" target="_blank">📅 11:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65431">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
گزارش ها از حمله به دانشگاه هوا فضای عاشورا
@News_Hut</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/news_hut/65431" target="_blank">📅 11:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65430">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
غرب تهران و کرج گزارش انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/news_hut/65430" target="_blank">📅 11:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65429">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
صدای انفجار های شدید در تهران
@News_Hut</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/news_hut/65429" target="_blank">📅 11:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65428">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 33K · <a href="https://t.me/news_hut/65428" target="_blank">📅 10:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65427">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/65427" target="_blank">📅 10:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65426">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
فرودگاه‌های غرب ایران کامل تعطیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65426" target="_blank">📅 10:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65425">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpABSCvP7lpibRUIuQtrR4A0RZt0rOJ6x1blHUZ5BJYqvjQBuCx_ZIM6OyeRR_P6emiU33zxsPn0wyyOD6tp2KW92mTcosYkNC1Gay0e29T0O_SvQr5yualIRzlwtpEFJAlX_e9Uu0CgJV82wr1L8W9xGzyGqNovZtCaVzo55zlNkO9y6wEza2CC7ThzNrJnX_YdEf60z5qNTnks78d-bZ3uAhq9EWzOOBbzD7OBXrfQBGpNIj2D61Zk83BfQUlX_8dXYdtUbxOKrWfgs0R2xV6-ouBHaH9dLhYcH5z-IwYcNgdvBSsR4U3cDlGzETATeQ83JfEIfuMQSjReLB-bmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توییت ایلان ماسک درمورد ایران: « تنگه هرمز به نام اهورا مزدا از زرتشتیان نام گذاری شده »
@News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/65425" target="_blank">📅 10:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65424">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFCK8dzOin7zlm2Q8L_5kBgLbSpy8_EVac2ai1hXwCF0DxC50mcj1fXblGPAGeWLtnYKeOLXQFDR8FdhjgbIpjJKiHvz8FFvKbwqn0sYV5F5gqYtVZOyf2o0LJrr03uhUrZ3WvIuVJaxPuLYjYPjHEPxCIGO63n9SNCM72Gc7C2KMIAn6_j3oVl1YjJilwmMNMERN4-TPtskgSN1uuk8P4ES7NoCbxf5L_bGBG_cBf5AMkb3H5o47xpyl6pmo-vDBy-SGJapK3oQte7GR0Ypyd9K1pL1-JcH1KwIB34zjedAvywY_VSy91epE9jzQKEs_Dlsq74KQIOaIE3RRYOvBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
حمله موشکی سپاه به مرکز انرژی اسرائیل در حیفا و ناصره
@News_Hut</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/news_hut/65424" target="_blank">📅 10:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65423">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56aa95f90.mp4?token=k2rF8Vcb8nidK9ur_yymjiVSkLgSRidreVvDvHXZVMcTQjbgQYrj9lmNif1c3JSqssYO8An1hVYCmyrwTcv8M2NR_E4Hrxmvj7jvtXNM7BLMcYqtHnp8X8prlBJu_Nh39IjbKbN-ZSFFORNpR4gA21EB1NdQ_ubCS4gDROb06V_w6LYQDGO_xt9GzLdkYGSzrMgQKmbqlxusmW0Q3TNlfyVMWKp94k9QiXhLDPonhtFsGyLRy-s094FPsld-Kt-Gk4G-gpGArVe4-RdgWS44Ug6s_ox_jG90QrR_i2db-vbkzswUNI1ymJq3wce49WGuZGjZWgnjs_vNRQ59jeRH8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56aa95f90.mp4?token=k2rF8Vcb8nidK9ur_yymjiVSkLgSRidreVvDvHXZVMcTQjbgQYrj9lmNif1c3JSqssYO8An1hVYCmyrwTcv8M2NR_E4Hrxmvj7jvtXNM7BLMcYqtHnp8X8prlBJu_Nh39IjbKbN-ZSFFORNpR4gA21EB1NdQ_ubCS4gDROb06V_w6LYQDGO_xt9GzLdkYGSzrMgQKmbqlxusmW0Q3TNlfyVMWKp94k9QiXhLDPonhtFsGyLRy-s094FPsld-Kt-Gk4G-gpGArVe4-RdgWS44Ug6s_ox_jG90QrR_i2db-vbkzswUNI1ymJq3wce49WGuZGjZWgnjs_vNRQ59jeRH8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
تصاویری از پرتاب موشک از ایران لحظاتی پیش
@News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/65423" target="_blank">📅 10:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65422">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
با اعلام انصارالله یمن تنگه باب‌المندب بسته شد
@News_Hut</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/news_hut/65422" target="_blank">📅 10:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65421">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
اسرائیل هیوم:
یک پایگاه آمریکایی در عربستان سعودی هدف قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/news_hut/65421" target="_blank">📅 10:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65420">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9d994e5a.mp4?token=bgDmQaCnLvSfowI5ZRVc4B0kxyhgTL8UigBZYBPbVKAkv3ggMH2t-qn2367AMgGRbYhEEROaySMF8WDN3cNbnoy3bY5Yk5jZ7GD_DSBrc-X0NYpmR444BcXRn-GiSwKg2v2MSyEy8LupaBhUUbv3eCNbAiSzBnko2ta5GbN_biB74u1snWlsnB1Str-hWiU4-DRFMJu32ejQL9Zgc6rjZ8cBnNEmcaYznjtaTZjaZUj6HacyMmy6epivqYNJ0UcR8XllnuTZKeDhGZQuU_RXjYS-nfUYwntG4LsxRr-xh-Wk1t6U0Rl91b6KaA7mfdqBHkhwLWfj1PR4oPwqUmu7uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9d994e5a.mp4?token=bgDmQaCnLvSfowI5ZRVc4B0kxyhgTL8UigBZYBPbVKAkv3ggMH2t-qn2367AMgGRbYhEEROaySMF8WDN3cNbnoy3bY5Yk5jZ7GD_DSBrc-X0NYpmR444BcXRn-GiSwKg2v2MSyEy8LupaBhUUbv3eCNbAiSzBnko2ta5GbN_biB74u1snWlsnB1Str-hWiU4-DRFMJu32ejQL9Zgc6rjZ8cBnNEmcaYznjtaTZjaZUj6HacyMmy6epivqYNJ0UcR8XllnuTZKeDhGZQuU_RXjYS-nfUYwntG4LsxRr-xh-Wk1t6U0Rl91b6KaA7mfdqBHkhwLWfj1PR4oPwqUmu7uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
با تایید اسرائیل، پتروشیمی ماهشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/news_hut/65420" target="_blank">📅 08:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65419">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
پرتاب موشک از ارومیه ، لرستان و اصفهان به سمت اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/news_hut/65419" target="_blank">📅 07:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65418">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووووری؛ انصارالله یمن از آغاز حملات به اسرائیل خبر داد  @News_Hut</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/news_hut/65418" target="_blank">📅 06:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65417">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووووری
؛ انصارالله یمن از آغاز حملات به اسرائیل خبر داد
@News_Hut</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/news_hut/65417" target="_blank">📅 06:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65415">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
با توجه به شرایط خاص مذاکراتی و همچنین آغاز جام‌جهانی، حملات ادامه دار نخواهد بود  @News_Hut</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/news_hut/65415" target="_blank">📅 05:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65414">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
با توجه به شرایط خاص مذاکراتی و همچنین آغاز جام‌جهانی، حملات ادامه دار نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/news_hut/65414" target="_blank">📅 05:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65413">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b906cb3be.mp4?token=X9f7XMYTi9WCMaTb7Dqpgz8v7nWQ_H2V0Qb1i-dZhR6z2NJGAc8Smr8oCCgc_gCVN76ylOpB4eGBL-RTbm2Zqh7nXc7uG44k9sGDTZURL_ZGWxwnOTUtOYyJ_RPvrtM7tSI00Aq5coD5-HhMeRroYWF7Qad0R40f5Wutsu4LRZ5TBVsaWlJfd1z8_IIGpZGP6369GaQRsymPBR_7cugCxjZWQwNatPOKS0k2PAl7dlZ-BquRh5ZhAJh_Sg654D8jAxDs1YAfDVCflUGfapwqeT7K1q6Nqu3sehmD-TqjFxaXFPLEC-ABVdgIu47ZxtUp1Sy0yBA8A2X8QGxA5hztog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b906cb3be.mp4?token=X9f7XMYTi9WCMaTb7Dqpgz8v7nWQ_H2V0Qb1i-dZhR6z2NJGAc8Smr8oCCgc_gCVN76ylOpB4eGBL-RTbm2Zqh7nXc7uG44k9sGDTZURL_ZGWxwnOTUtOYyJ_RPvrtM7tSI00Aq5coD5-HhMeRroYWF7Qad0R40f5Wutsu4LRZ5TBVsaWlJfd1z8_IIGpZGP6369GaQRsymPBR_7cugCxjZWQwNatPOKS0k2PAl7dlZ-BquRh5ZhAJh_Sg654D8jAxDs1YAfDVCflUGfapwqeT7K1q6Nqu3sehmD-TqjFxaXFPLEC-ABVdgIu47ZxtUp1Sy0yBA8A2X8QGxA5hztog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
💪
گزارش انفجار در ملارد
@News_Hut</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/news_hut/65413" target="_blank">📅 05:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65412">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
حملات به تهران  @News_Hut</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/news_hut/65412" target="_blank">📅 05:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65411">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyDGkVsByG14-VlAg2VOhS6rAb39SZLUkezwJ7DJt9IQ75MZbnd8HU7Fb9jCFf4UfrKhIroizFnZXN6gz17k7kbYu0LBLfJzlx78kQscoCdRYcLEbUC0LxI4H-h-2E5C3dbhZVeGLD1ambK2QLU82q9znHm91bOU4xouDtR0TcGGZesXdv9sK_F0W4tmFWUqr3hjXl0lPVv0ymrPA2kzKxMMiwyIhI7CFaNFn9bCY8nrZIrzG0RpXI94PG6S4VtCuCLoSc_dPJXNVoTqn4Ge8vP2VQgbqTEl36dEDK3L887rZybh8IHlqDoemv3qvH_UKSJ2ySsTHRgpVn_dtbw5IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات به کرمانشاه  @News_hut</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/news_hut/65411" target="_blank">📅 05:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65410">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFqeSNhYhZu2ANPF76J_-nDo_BiVdQUCKORllG9ZZVRQuyMcgM6CaegYeXnzGUaBmM9XAk4OpEGmbxHRoQ2oycdwcvbvcK6zsEYrsZTSzjk7BObJ3nR36rUjlmFJfPsSSxXCPHCBXypIw1E7HovO1ADkgCJ6-FYEuEmhoUvsd61UqLIsxFYVfQh2Jc4h0xgSEPWq3Y1HN-ySABy4ZI7zJMtXGDGxptywmhiFJkCM1lg1WOcjshhtCw3TlRSLWcDxA22OimRHNXXYiZBabZMQimTZmpFQafX3-LXFdssMHqS0ofNFx1r4DcLp4MbLtGJKQ9CgWWKcuag_GngQwTT1Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات به کرمانشاه  @News_hut</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/news_hut/65410" target="_blank">📅 05:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65409">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13951b2150.mp4?token=SiAf47ydCNhL7874EvG54vC-42nmSx-QnNfBuMpRcmvbpSPz7TzlMoIfanw0fAlb-eSAWpMzAiyF7DKdiPEGhVIgWOdQOa0PxsV1lpZet-JOtUK_qWR4hmeB7Fg9vA48iUq1pXI1klRHx10aouNFx5mBIVCr6QhKw48qgLNBNldc8arSMr6QAlUDjGWE383xlzXG_dH4e7VAlvHeRFQzEltrx6aDQC7CHBmgDdqE71K_J0Qo9cdwPuAhEEOYEF72a0omjlPIFbfCrbEg82NsNUpq4926eMg23EzYJuWXiuCS1EU-z_G-n0V3_SzxBFVm9VTkWf7lkByut90HHoBslA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13951b2150.mp4?token=SiAf47ydCNhL7874EvG54vC-42nmSx-QnNfBuMpRcmvbpSPz7TzlMoIfanw0fAlb-eSAWpMzAiyF7DKdiPEGhVIgWOdQOa0PxsV1lpZet-JOtUK_qWR4hmeB7Fg9vA48iUq1pXI1klRHx10aouNFx5mBIVCr6QhKw48qgLNBNldc8arSMr6QAlUDjGWE383xlzXG_dH4e7VAlvHeRFQzEltrx6aDQC7CHBmgDdqE71K_J0Qo9cdwPuAhEEOYEF72a0omjlPIFbfCrbEg82NsNUpq4926eMg23EzYJuWXiuCS1EU-z_G-n0V3_SzxBFVm9VTkWf7lkByut90HHoBslA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
انفجارهای متوالی در شهر اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/news_hut/65409" target="_blank">📅 05:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65408">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6wJdL9weWCGTwvi_ZPgjshXZHoOsrKc08Vkj5B_2OX3qCosbhynnqYkp4JKKSvw59z4FqpkeJczQl_sYpaKFhlZZlHuGYQtfy-mXVStUQM-aQgr1vDdFgQLJNvC2BtnHTxI69H9db9rTV9N0EB4dx_v90G-h2b3xAFZYCZx_mgq-mZJZPlw52zJcBUTNiiMIalt2WAOx6A9-8NDlmhkDAlmnZHtFOBN9qoR2gegTnESF4bi6x2IwiiBxFIAVJ9kN9WliciPdSG6kqiTyK7wF2Qjt-mRa1uh3yTkES0hkiyQnnad6l1g01iM_tkgFWedEqCJ4Kpaj5hYAJQ0_VHZqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇱
نیروی هوایی اسرائیل اندکی پیش به اهداف نظامی متعلق به رژیم  ایران در غرب و مرکز ایران حمله کرد  @News_Hut</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/news_hut/65408" target="_blank">📅 05:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65407">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mLgS5ttzWQQjecWpKZ0lgKRCykHZxQVdK6xKZo-fBJ8sW0wc77zISBatj7kOO7DYgdzb1rO8jDZBzxJpriChiAeLnYLIk78cTqsACtaVVG_CZZTT31kzgSGiexMGu2RJDG4KvWQSRzeN1DA8PHk6VF5Wgq3NF1aCOO9i4asE5AsAalQwvwo-7epqepBH9F5-OCx6JM0v5AiZZPGK4o9ND0GrGhuY4jYSTccbJnels9Ag7Td4_EbqPW6chdQBgsilQT4FYoQmX4TnSfchbdlyYqytC_KhUZTS9aODrB8wMJEHNQYjbgrR0vpJy75QzI0oU9PXzCQ9tuC9imJMqsgbEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇱
نیروی هوایی اسرائیل اندکی پیش به اهداف نظامی متعلق به رژیم  ایران در غرب و مرکز ایران حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/news_hut/65407" target="_blank">📅 05:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65401">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: نتانیاهو چاره‌ای جز پذیرش توافق با ایران نخواهد داشت.
@News_hut</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/news_hut/65401" target="_blank">📅 01:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65399">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
آغاز حملات اسرائیل به لبنان  @News_hut</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/news_hut/65399" target="_blank">📅 00:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65398">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
آغاز حملات اسرائیل به لبنان
@News_hut</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/news_hut/65398" target="_blank">📅 00:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65397">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل: رژیم ایران اشتباه بزرگی مرتکب شده، ما آماده‌ایم
@News_Hut</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/news_hut/65397" target="_blank">📅 00:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65396">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
ترامپ: نیازی به پاسخ نیست، صلح نزدیک است
@News_Hut</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/news_hut/65396" target="_blank">📅 23:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65395">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🇺🇸
🎙
ترامپ: به توافق با ایران نزدیک شده‌ایم و نمی‌خواهم اکنون در مذاکرات اختلال ایجاد کنم.   @News_hut</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/news_hut/65395" target="_blank">📅 23:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65394">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🇺🇸
🎙
ترامپ: به توافق با ایران نزدیک شده‌ایم و نمی‌خواهم اکنون در مذاکرات اختلال ایجاد کنم
.
@News_hut</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/news_hut/65394" target="_blank">📅 23:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65393">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید: ترامپ بهم گفت الان زنگ می‌زنم نتانیاهو و می‌گم به ایران حمله نکنه
@News_hut</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/news_hut/65393" target="_blank">📅 23:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65392">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: حملات اسرائیل به بیرون هماهنگ نشده بود؛ اصلا از این موضوع خوشحال نیستم
@News_Hut</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/news_hut/65392" target="_blank">📅 23:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65391">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید: احتمالا اسرائیل پاسخ خواهد داد  @News_Hut</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/news_hut/65391" target="_blank">📅 23:33 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
