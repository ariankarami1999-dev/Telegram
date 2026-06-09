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
<img src="https://cdn4.telesco.pe/file/ke3b3Gc471rX_h0QW-7LvCQQIhGdjPTTFbT9vtWB-DVPMhbzrA_OG7pX3TxZoD5X9oSv8QZX08TOIblWwfUkBhCNPxfOcP_QNoL5QIFWFJ1jA65qG9oiXk4bQgj56OsJJ9Ve-UraBGRC--1hu0jT0SjtvXkoMh63rKTXfiQ1-b6NotS6pE84nyHVC9JIF_GeHEtzy8ZgtQacCd0I8cpCQHwNAJDjesPJl76r_ifUpMbhGhTJEjTAQsxvuYkqvCuFA-MhGoyfLEeHmCBGkWOsTJpaQi19Y8ygkBFhCbLFin_yV4Fv2yqWtI-kOWTg4h6ybrqZYIQwC5Icfh2bhzMgEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 169K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 13:59:26</div>
<hr>

<div class="tg-post" id="msg-23047">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2qe33IPj1kC7tjToouMyU-j_R7N0pq7ASENWGUfNcHrtpIbHaql1HPUdtBG8mcWlXTUZhC1t7GZaKeizMYvXSBAwJM4XaXRPBr89Vx8UMAPmzBT0RlIoJuPCaL6kSW5Hk9sJbizY1H3m_RwZrHviEzQ5YOdg52xs2LwDQzxf5QpKPOBYiP7iuAsUOvD2tLT6emHl3krhMEuyBZTuKd4fnhvgAqXKLQMuWr8Do2dLYiubRcQXv-sOayI7WiSLvekNyNV0mSddN5YSgjEYYqbAx-C8gFH_hyMT1hXsvzUEzgaRrMteZI22dpugQm-OCAa5ISnuWa77q9u2uXvwPvfJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛
باشگاه استقلال مبلغ رضایت نامه عارف آقاسی مدافع 28 ساله‌خود را 80 میلیارد تومان اعلام کرده. گفتنیه باشگاه تراکتور به دنبال جذب این بازیکن هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/persiana_Soccer/23047" target="_blank">📅 13:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23046">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMLc16rviNJ38l7Q40CCFvHXoVtGlwHt8iixuLDaUHv2ULvIFOAepM-jpZYRBDrno41t-bUYskQZf9e-V8t_A5cTl0f8uXSJmInT1eDG1yiLQpYWP3gZyEgIzNFFz4ZpiCMeGFKaZkMnCCfauvQEeodkqzusiJfJYI48JixwF4FrskME_oSl5APEu10fz5St2tY08_ps3uW3L1COXTF_2MTu50K97XD5PNAPwBPHB9t4oq9G_s7aW1TFDFET7gU9jc5digrLZOS-ftIXYaJWboU1zUnOgniHHo95usdaLwOBV3XxL42Dn-P0Zr5PMzM4L_4C4L9RZKiKSqbDtsFw8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ‏گویا پیام‌رسان واتساپ در برخی نقاط کشور رفع فیلتر شد. از یوتیوب، توییتر یا تلگرام به عنوان هدف احتمالی بعدی نام برده می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/23046" target="_blank">📅 13:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23045">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef75c0b0e.mp4?token=krlPoOcEYfklLDQ8a60NUu2DbF1fgL0a_h-FvqAJGI7LHemY8nGyB8x9Pj1Rp6xN8LaI8zyM9c5K99RMqcmT_jmcR9rxkXAIZzee6wzLv2ejiVJGxCCPsT5SQKr2Vxc7OrcSeA-sO3ngGPooZPP9RrYcP0AeZkVJZyPbQ6JHXXjcJC4wk7c5zlVpM0PzUMoJo06VTlaVSeV3O_gcC5ghNEm_LLFFywzATkXYPRwsAZSJY1D3pVy-Ugpip1oyEOL4XyCAu-zuueMzwkIYY3spdIaoqQ2i3aj5HkwEbGsLJZSTaePlMmoKgNGstCMH-l6ii-H6OEHRlQU1nr-BsKZKnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef75c0b0e.mp4?token=krlPoOcEYfklLDQ8a60NUu2DbF1fgL0a_h-FvqAJGI7LHemY8nGyB8x9Pj1Rp6xN8LaI8zyM9c5K99RMqcmT_jmcR9rxkXAIZzee6wzLv2ejiVJGxCCPsT5SQKr2Vxc7OrcSeA-sO3ngGPooZPP9RrYcP0AeZkVJZyPbQ6JHXXjcJC4wk7c5zlVpM0PzUMoJo06VTlaVSeV3O_gcC5ghNEm_LLFFywzATkXYPRwsAZSJY1D3pVy-Ugpip1oyEOL4XyCAu-zuueMzwkIYY3spdIaoqQ2i3aj5HkwEbGsLJZSTaePlMmoKgNGstCMH-l6ii-H6OEHRlQU1nr-BsKZKnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
انتخاب آنتونیو رودیگر و لروی سانه بین کریس رونالدو و لیونل مسی دو اسطوره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/23045" target="_blank">📅 13:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23044">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmbZLcXnc3z2dLT-Nj6eeDUZehMj7eOWysATl40qXTdtUMuEK6LldRKd68uyPC62jvU0gMx3dMhETN_D6HpWA4kImZZlfnhuV6KNLcSqckBH0AfNvgfcipwCeFom6AO2gkq4HZ9KhjTzQkwZmLmZHJhbZq45G3YCMQltClXRv52vrHd5yWbQPrGrl_XPc23p8GHX7UMhTSt2kEgZOrJsKpUb-V9W22ZKT0bb7njaaGFooNPuGJGkV5PfCx1Jsemy6BE96BU2G8cu88u9YOQZpfIILB0TJx4PXoyABBRnxp0gx-1IUdpwd8nnk4ye5ZEf_NqGSX1s6H-HoBNAs6lnnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: خوزه مورینیو از فلورنتینو پرز خواسته هرچه سریع تر از بین یوشکو گواردیول و ریکاردو کالافیوری یکی رو قطعی جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/23044" target="_blank">📅 13:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23043">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAQ7DVWmQi-xpsbtMiqYZk7vvo06l3WF-hO2OxCSZUsoOAMXZES_B6esQWVo3rSB_c-C-5EqQia9s8RwZOFBSAJ9EJxGSbzJ54Zfb_Nqm3r9szzl51VoFu0CCPWfLNvpJXm4CrCBYV6fmiFEi0RVyRHeth1gy3YDV6-lNeyjekjjfS9XIuvrQXyNSUMqf7lKbKXSNqFy2qldWBsaZw0ksc-Bqf0u8Lgq5307wCUrpxhvXAbR4vVKMBZiTcjO7QekkFZ0uROCECJbhEtES3MmwZGLnlHzJNm3XvpiqqJvPgAjE_64Q_aaK6cOJxBf30TgLWp8ADRYoCTJx6OEvNK2zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تمامی‌قهرمانان‌ادوارمختلف‌جام‌جهانی؛ برزیل همچنان پرافتخارترین تیم تاریخ جام جهانی فوتبال است و با ۵ عنوان قهرمانی صدرنشین است. پس از این تیم ایتالیا و آلمان با ۴ قهرمانی در رده های دوم قرار دارند و آرژانتین با ۳ قهرمانی در جایگاه بعدی قرار گرفته است. جای…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/23043" target="_blank">📅 12:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23042">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LknVww9Df7rY128ET6TqIfQcmYZG8CeKReUxUjUjVHQwccTEgj3L94ETjWuHk2MvvQuTTrkMR9Sichg33SU5OzzxXJB--T1e7VH3qGK5UKkJlYEco5Aa2au7ahzOg3noMV0CRBHyg9ixn5XJ6UJBpLB6NHcUTuVa-u66WrQYDDnnXWyKSkUO-wFkoL44hIJCOjFfYuecHNd5_p7ZrOWg0jpx8jmWt9z-TgwkAkOKMsYHqSnmo5lYDwThrBbolRGxmHPMcHyOGVBY_xUYKMQLlliSGa-Keg_1E-KIIHVGjZiOE3UDGkQki9xHZ2bcGCUdhqVc86K4zKGfbfBFQnAT0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تمامی‌قهرمانان‌ادوارمختلف‌جام‌جهانی؛ برزیل همچنان پرافتخارترین تیم تاریخ جام جهانی فوتبال است و با ۵ عنوان قهرمانی صدرنشین است. پس از این تیم ایتالیا و آلمان با ۴ قهرمانی در رده های دوم قرار دارند و آرژانتین با ۳ قهرمانی در جایگاه بعدی قرار گرفته است. جای…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/23042" target="_blank">📅 12:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23041">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXWBv2UqgRD1JqoB54itNYpcBzCKDZD2JrGGPysBj3g6FTMCHFChL9N8LkLIIatpMDWAODsAcoSIplMhS6UCcr6QPnGqGxQ0lGk4zcom8UTzO4fsBpgowC_vh4fcpDhvp5MMETBuX4jd4E0LzRqEUT8UfOPMsjkShAnwlJsY3thvoAg6OjnpY5nKA3CRkFH1NHWsTLmU3K5yOxGODO_y3BmNjbOlDRrG-3wSUWKqtEYnY8sDTLFZSrb22eFxdadANeKBrenb971w13mQoA_zMZs6jnxMbGp9B1QpogVp8Rf_ASTfKCP3Smzd8t9UnhjRXphUWFQEfo8HY8jloUqPBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/23041" target="_blank">📅 12:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23040">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiWqMVfXBMKmOjRFgaJLfLdkqWw6Wm4RWeVZ_ALp-cEli-bSfSUVUshIv94mHqGimVJP8jKIwXleknD967Woe1hyKDZX7EnWdDz3tuYZ_BXiZYOGYtjmxzn-XiN0GYGBewRBB9-KtByaAkE6qB8dz3mXP_1b51QVlw9vHfqbFx8Ucb8h2qwa51uGqviVydxsSguzJU-PyODWVkucq-XEYyUR-RAOs6lWKAKc6HINLtSZyWTODgkarbQBS02oPYVZC2n78L3dXlIUY2yXGbt3BJhLfxyYeBTWqvVuF0q6MOII95R80Mk9OJEwL9KtRLpLlLS0HtIv23Bl8DE7N4Ti3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ ایجنت کسری طاهری به مدیران باشگاه روبین‌کازان‌اعلام‌کرده که این بازیکن برنامه‌ای برای بازگشت به لیگ روسیه نداره و قصد داره ادامه فوتبالش رو در لیگ برتر بگذرونه. باشگاه روسی‌ هم اعلام کرده هرباشگاهی یک‌میلیون دلار پرداخت کنه رضایت نامه طاهری رو…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/23040" target="_blank">📅 12:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23039">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4860b42130.mp4?token=Lmnm8DG2TunWKJ7frftE_hO1vaDOeWq3EY_8kMlvD01Geypzz4_DuKUy_w_EtauNWP_ZwSk3RGpDn9Jpvic5_o5Hq3x6BW_832YD2KBFDjW6EPh5B70PlmxSVAMNeordSCz3HfYwkx-rG-aeX5s_aQU8evxWnnNy7XpwzqUvnNaulUD21Vfi1-imaWPEaMJbz6QRdhuOankSyP2ZPmFhT2vetXGrK6nq5LIofqK0v9rHR1rpZXmQhKx9WVruJDWLzmeqiV-U1utp2bEqiimBEIxSf5b-UdHsFfM6nVYMscK2WY-E2tYiVoyCO-RL96PPipcRX8qBOPQBlmk55fIW8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4860b42130.mp4?token=Lmnm8DG2TunWKJ7frftE_hO1vaDOeWq3EY_8kMlvD01Geypzz4_DuKUy_w_EtauNWP_ZwSk3RGpDn9Jpvic5_o5Hq3x6BW_832YD2KBFDjW6EPh5B70PlmxSVAMNeordSCz3HfYwkx-rG-aeX5s_aQU8evxWnnNy7XpwzqUvnNaulUD21Vfi1-imaWPEaMJbz6QRdhuOankSyP2ZPmFhT2vetXGrK6nq5LIofqK0v9rHR1rpZXmQhKx9WVruJDWLzmeqiV-U1utp2bEqiimBEIxSf5b-UdHsFfM6nVYMscK2WY-E2tYiVoyCO-RL96PPipcRX8qBOPQBlmk55fIW8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویژه برنامه جام جهانی با گذر زمان؛
از عادل به یک مجری وسطی بازی بدرد نخور رسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/persiana_Soccer/23039" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23038">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjGtL0dw4cwnA9p6SsJt2nUOaDD6H9hzuL5uzG7f_Vqk3p2-3o5Zi0DS0WyLFcJu-4UDCvVCU23pNqNYuWoqfEc8EtV32N_mKMQPXpGj9kPvtl06YqZcgM_XBIk1A4--ObTsaKkp7nFXHvhxG9MRvZTNHkPm-CZGvflZSOJm1_RTIXa-kRIPz8wodLZltj86gcaLFRP7f6auYu7h7KIeEdc2NatF356sIhQiqc9Lge5WFkNy2AluaNH1uwCraa9zOadZ3LREZU_v2Jos8y19Girm94iwkwo6Jt7hYG2Ef4JkLVs_0qSqrCs8P-oSXmwG-8oWCeMMu9XqlIA_AD4GHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تیم‌های ملی رکوردار بیشترین تعداد پیروزی در تاریخ رقابت های جام جهانی؛ برزیل در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/23038" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23037">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0yGhn08Hof9fUgq2T1Y1QvlT8-WHWP7jAfSWd6BgmuWe33ZfHAYRS-OD8x53O62nkoh0vkEEDoLMhfLRAjK_3qDx1rfCocLpWgjzWllZbmJcRQJXezlHaG9jZofN3AwtFOMS__nr2CTPIIewtE1Oo07p1beeejOHw4BZQXh_bObOONKEp2oYEd5eiBVSfBc0jspAGHKfavVK-R0duaO7teComT9cN3NdJcLKg0vpxUaPedS21LSIKfDwQcYIKihcFKHv0bhO3ChACbY9dbGtIiqFIVd3vXkPt6URqW--JHhZAWX-4YA2fI_ygwxtjuVEXItjUCHr0eGElwngjEUbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد.
معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس‌اضافه‌به‌ازای اولین واریز
💰
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا er19
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/23037" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23036">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M43gtN222JpIanS2WYvTfdFpKaH2Qfnb094ZReo3HaRzNiKkboo1kcqn8OciXCg3yUdxWJdge20OrEwTzR7JloGKYvUl7Oi0JrAybae9btGhDjQd_TlTEhzKh0UwHIKgUPZ7IlGjrGjr4c75llOQbznaCqf3CTjkAoGxk72jNG6RDdvtO66QqcAqQYinZzybrEUYvZ_WD2I3F8s-Cjc5fwPyjtD31AJXf7gP7QxGlRtJ0kYBkOVYokO9mkhZWYyFyiLkL9RNQEn7TChIiOV--trHIyaggYyJCwB_HxlXE4DnycjcOCtNxOov-PSpKj6t6GD_6DXwvaGaCMcLDAHh2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/23036" target="_blank">📅 10:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23035">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3RhCZ9anrdLFf2QfGWe7b8PVRe2TfBA0iajAPjBJMyxNb8Q8xBAS2VglrY_fWAIYyzawB93o_CrI3v6R77k_-0c-ZutdKECHcx9nizigLzlQ2QJ_-rxbOe09TqCSGPJA4GpTVR1mXQKj3ECqb2hLl2aFGe6IrvE-I3H5RP6y_38UeYC0vnFB-9tA_a7YlhSloJIGBApeRc4hucXuj_6DAogg_BjevkBG0ewGtZxHl7uAQagtIEpSOe-DHMUxIaVcri9CJ0t9zeSd7o0UBfS6R6mVr10tsJ1tWH_0Ffe4XzaYiZYlzIYrDufpmQuhDBh14UtawRKC3GLARurPaFisw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/23035" target="_blank">📅 09:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23034">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCaXGm5RyyCJFbozdJzf6XSutEqafz7ppi7FdWipmRZhhD3LLsSUbbhNaaPo5d006GrZB_8B3-ytGVqne4RqxzA3Ahq9l2IF_aMI2MTEujgQ_M4j8dbTpVs3pRFECOIESwBLcFsvs6iplRcND884S692Hag55rXuYXwlTLyOY3Lbx63Drq3p1QmLoUdcfuRNFUHhRi9bjTmjulzoNSMA_5UelRULfX0gLebYXxQHvPg8B1ioaJ0S1Kos7egWYEc4HU2ZKpzKbRocvpE3HlLJhbwjoqgPYrg2Wb71gsIIl9l5Nih4OrZjrQ9E5ibv-rVHkCwEo4BWfwQEoOLBMd5tWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|دیمارتزیو:
فرانک کسیه پیشنهاد تمدید قرارداد 12 میلیون‌ یورویی الاهلی رو رد کرده و میخوادبه‌رقابت‌های‌سری‌آ ایتالیا برگرده‌. یوونتوس علاقمند به عقد قراردادی سه ساله با این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/23034" target="_blank">📅 09:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23033">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j16g0JHaoOcYGUS5ejxQOtefppzEGSTnXQqHWfmZEdVEitKzM389Bm4py03I0_F7OHXtr7eTqNdF6M2bMS2rB4wYPfH1-bke_MVVx3YKj7AhvLGVRJuBqVq7RWWiJHo3lYGRVo9aAbx3dlK_b6mBAsLyAlnzAbJJvesFpnXRwz6XAaWSkRVnwWMpfyEgIDlQgHk4-LlaMmPxYNTdJG8J13XpaXu4dphr4e76w6yPh0KOmO48culHhCarxX3w4xkBXMrA0ksxIWC3t5xiP4jH7bSBNzWTqv50t3Qlgvt3kIRs7Z6a5w34gsPnzImleBgJpHZyoV-49vo39uVt614rLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/23033" target="_blank">📅 09:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23032">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9BKKOWpPrn0xAlsesRggXa368rH6NB0TYvs-xbbBtuskhCQQ320xD143xHSPLhb_l7khi--qLKQiQolgX4vA50CfuoZQ4-gVFZe3aBMh9ZSUocqJhb_8N2ZdcnrgY-RQp-e56j216roi5zCOoo2UdCxYILu94BMgFVw2VUy3tfFB6FjM1cy2bp1VYXVeSlCLfOuEr4UwblwiCp5iyFZom4MI2PEQ3jOrawdhsjQ0q0LXqZzh3Hvo7Aiu1HAXuP2KhFxNL2HxQnmyDeIolWzi74x6nOABjfr0GJFhhXGNsaWqgWO4HRLJw8ok9eE9_mVUXBYlEPuswR2WDaEIT0p2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/23032" target="_blank">📅 01:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23031">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8torLvQiBYaqHZl_jscxmntEGCy1ZQo9aEZzY7xgEnl5YHJMWanMlFwCAAI1UJwFgxtZJXQ3o8FNH_xw2dgk96R6iHXYrQvHBaFijywN0A7cfwFHNQLC830FJanb9xAxckhiXtuC4h8bYf6UBlw29LKDqNfqyACzC-7UBLk934nOwUpvo168oRe6Muxj8UOWMslaRVgx2SP8bL0cPHA5ElrwPBGqVjBXu87PLcXXDpzrOxDvrtFr5RbB6zNzS0pZr6baXHdyl0VAKORE17KD7CZOTdp4raGaay6IlWonSGY59KFJs8vQ9-hspl7V19y88swlKzzzd-pcHNMZCHT5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه ‌‌‌دیدارهای ‌‌‌امروز؛
نبرد تدارکاتی ماتادورها مقابل تیم ملی پرو در صبح امروز در فاصله تنها 48 ساعت تا شروع بزرگ ترین تورنمت تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/23031" target="_blank">📅 01:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23030">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_sEoDag8A7Srtv4-x_Zupv-hN0AWk1OiNpIp5FUZSMvbmpYzJCChRZY2dIsdfw1T9g6ehXyi-iJMLDuBjjeOtNkJzTGSVYKkOT_LKlEUm5S1ReDIRkwv8rti39Ta8N29nSIczH8LGWztRhoKdh8ZBUEMCYDrMrQgKkiUkpEk4Nyn7p1_0naIhQhfbX7WwY-2V1WSS9_RNlqcxAktJUXqJzWxJyVxQiMsk5jHpN91zZcb1s3AoIKBizltrAzh6j8XWvNEBnj504dmyrSyiV8m3W1CE8VZRjqFFwDgdqw4oRgmBf1p74PE38ah7cdgFDRY-BDcTANofr3jr-dAAuoqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌دیروز؛
ازبردسخت‌هلندی‌ها مقابل ازبکستان تا برتری خروس‌ها در شب هتریک اولیسه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/23030" target="_blank">📅 01:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23029">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb89dc70af.mp4?token=KMZTRbMbN9JpUT-mrybGjjQtoL6wqI1iZwND5fgqFLx-R7Hw7IC619dj9x0Zf8_7JlxInOfLHsaNsDFkcL8IGk5LAcWyeAD0qD0EvxjBiwEm8PDgrLMw7icdXbPk5ne4i4R2BJ_DFiM7PCoXXfMUxGsQpoQ7y3qRHa30OvnQuPPRg5kbi4r1kJHDo9m46eo_hoXRB5SamKGXQTxkbaUNCsBY76SMtq7twwsyVHN1Iu0fIMeK7ggHLGLDTOC7ErjLEPX0nMP_tBGDEFosM6sPrnxh4zS8B-uqvCBFsI-95BvAwbWTHmpVPFwXIJRQJktGRt6L2PvwmpcmyR-PLfS87g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb89dc70af.mp4?token=KMZTRbMbN9JpUT-mrybGjjQtoL6wqI1iZwND5fgqFLx-R7Hw7IC619dj9x0Zf8_7JlxInOfLHsaNsDFkcL8IGk5LAcWyeAD0qD0EvxjBiwEm8PDgrLMw7icdXbPk5ne4i4R2BJ_DFiM7PCoXXfMUxGsQpoQ7y3qRHa30OvnQuPPRg5kbi4r1kJHDo9m46eo_hoXRB5SamKGXQTxkbaUNCsBY76SMtq7twwsyVHN1Iu0fIMeK7ggHLGLDTOC7ErjLEPX0nMP_tBGDEFosM6sPrnxh4zS8B-uqvCBFsI-95BvAwbWTHmpVPFwXIJRQJktGRt6L2PvwmpcmyR-PLfS87g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/23029" target="_blank">📅 00:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23028">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbZ3T09J7RaB3T8BV9VqRFWhAsQumkN6Gu6TWNXNSQvYna7iJ_tHKmehuW4wNSPzmg0gImO3dleXj1lLgB_kK6jUiQw4eiwx2tjN181mo6BDLXa8640ypwIjaYRoPsoixwkFtUQ5VYjyg4Yh3Sa7o6tlX27fSVH8cZk7hXup9D_iHj6qKa0ZPKRySY4xoCSRDZMPHyPz9leqm1psqAIe2Zvm70V0vImzBIcTMVZNA5CvDg3tYcaU-d8xgt5iCysHLcgbJFFzkjnhJm_k9h29EKgacrzXQ_v8XXmkL3gznfpw-Vqls-iwue_bFPRSymELrBNg_--oDgpzBHFYieXXkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا:
فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/23028" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23027">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91f877f10f.mp4?token=X8hJYnzePk4xaM8jHdZKzjvCJk_FvLOOVungrXR5MhB9nu_Y1AipTMBo7SO6iDSHyfst7YuoUq2p2DoQiQJurdmVpjLeHTWEmVrVa78tyiVIa1YgnXXOFHzuM8CIPeHCKFIwQHw8eqWHiLf5lTsxWcJTuMnucDSjvu89hLYIB1k-eR2_rECYDe_1paq16dvLBHmuTpZ7EoUfLIBDCd1ZNgvTPpAI0HQIbohzVUCc0eD7RTsvhDLQBGHXRmSuh4mI-kusCwXS6w4tECAVT2QXgt2QR_6XlDnKjLejsIry6aJTgG5jONKm_W4qXUbUHfnJ_4ZrWsQJNDI8_FGVQS_jnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91f877f10f.mp4?token=X8hJYnzePk4xaM8jHdZKzjvCJk_FvLOOVungrXR5MhB9nu_Y1AipTMBo7SO6iDSHyfst7YuoUq2p2DoQiQJurdmVpjLeHTWEmVrVa78tyiVIa1YgnXXOFHzuM8CIPeHCKFIwQHw8eqWHiLf5lTsxWcJTuMnucDSjvu89hLYIB1k-eR2_rECYDe_1paq16dvLBHmuTpZ7EoUfLIBDCd1ZNgvTPpAI0HQIbohzVUCc0eD7RTsvhDLQBGHXRmSuh4mI-kusCwXS6w4tECAVT2QXgt2QR_6XlDnKjLejsIry6aJTgG5jONKm_W4qXUbUHfnJ_4ZrWsQJNDI8_FGVQS_jnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
باتاییدرامون‌آلوارز؛
مورینیو سرمربی فصل جدید رئال‌ مادرید برای کنترل‌کامل رختکن تیم رئال، پپه رو بعنوان دستیار خودش انتخاب کرده تا بتونه حواشی بازیکن های داخل رختکن رو کنترل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/23027" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23025">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=lJ__Ac87F3B9yXCcq5bl_hOm5tlczZA9ab0hex773P4jvYDxtXYNSXDRAYd5XYf22b28UtdbBmoRFY6fqHSV_kbqlUsOwgZFE8PM8qY7J6L4BBLkwzkeeO7417RVyYxHc0KHH-QAMRMI_b3PxCZcWgcjgunmGgoGDcJAuGlSqlZGiqZmqWNZlp-ZVSpiojypwJw4OC5ylaElTCXF0Y3ggK8WZHmHDsdBhDXMvbE3T98NqzFOsmTcW1nTcZhKMcgvcwbQG2sf-n4mX3ylyDqnfU5_j-qEvTy7YCKQo7HCcNNBEBxA4oByqDyeThOQVXOY0cOsqhKGx102hqN3O23-yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=lJ__Ac87F3B9yXCcq5bl_hOm5tlczZA9ab0hex773P4jvYDxtXYNSXDRAYd5XYf22b28UtdbBmoRFY6fqHSV_kbqlUsOwgZFE8PM8qY7J6L4BBLkwzkeeO7417RVyYxHc0KHH-QAMRMI_b3PxCZcWgcjgunmGgoGDcJAuGlSqlZGiqZmqWNZlp-ZVSpiojypwJw4OC5ylaElTCXF0Y3ggK8WZHmHDsdBhDXMvbE3T98NqzFOsmTcW1nTcZhKMcgvcwbQG2sf-n4mX3ylyDqnfU5_j-qEvTy7YCKQo7HCcNNBEBxA4oByqDyeThOQVXOY0cOsqhKGx102hqN3O23-yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
خوزه فلیکس: فلورنتینو پرز در کنار اینکه 150 میلیون یورو برای جذب مایکل اولیسه کنار گداشته؛ 150 میلیون یورو برای جذب یک فوق ستاره دیگهه کنار گذاشته. پرز میخواد این پنجره دو فوق ستاره به‌ارزش 300 میلیون یورو برای مورینیو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/23025" target="_blank">📅 00:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23024">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=Ha-ANJEzsPqUnyH8xRDjXq41zqJxGxt6zQYh8dFLtKmcmJXcxJnEcrXu5JVlVpi6nz2Y_dx5cxNIG4yk2cCrisyWZ4JkhIYfa_duePkp10hI_yN0BT2k8uT49_j0ANtXoT6aJZZLutyvMGe0ehSBSflDa3RFi6_00eFMjMYHcgw6ATf_ugGok3B2vcJuGzZFg1DhIcJKyN8Ut_kHM_y8-B5bMpyL2zHkEOSG7ljfFkyfeM0ocd9jolUs8DmT6WN-gp_1X5NLRa5Ep-HRXdD4k7W8v1RgKSQarGmUyuEG6XNjatNu9B0R5W0dt5qD3mO69F_iqUUShQKSgq-YBE59FlYF4zZdijW-MbAnv_a76BCaOkxixhOPnVxtwVnKHwYLPBPohQjGgcRPyCO1JxTiPNaZCSdxsme9ID3rz8DE0r7bNYuskZshbd7gFmUdasQMhCnCgq4-AnlAbAoJ2EjRo-WYa-Ez3YOVtCEpZvfLbuthvnnXJMEVFXAYyUlBH9d5B36-9J14jN0JpiItbkgGFDGf-YFL6cV4BkfejtdnAAb_cFXicyuVLHNS0jBNaBx3JPEZtfp4yj9bP1d5d_c1rvQvi-cCIRmnMZl2byzPMLH1h38NbT2YbfbMa5RJlJR4Kl9U9nvFNP90tqcVqHEadfwwEwl_B14N-bzmbzR5hA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=Ha-ANJEzsPqUnyH8xRDjXq41zqJxGxt6zQYh8dFLtKmcmJXcxJnEcrXu5JVlVpi6nz2Y_dx5cxNIG4yk2cCrisyWZ4JkhIYfa_duePkp10hI_yN0BT2k8uT49_j0ANtXoT6aJZZLutyvMGe0ehSBSflDa3RFi6_00eFMjMYHcgw6ATf_ugGok3B2vcJuGzZFg1DhIcJKyN8Ut_kHM_y8-B5bMpyL2zHkEOSG7ljfFkyfeM0ocd9jolUs8DmT6WN-gp_1X5NLRa5Ep-HRXdD4k7W8v1RgKSQarGmUyuEG6XNjatNu9B0R5W0dt5qD3mO69F_iqUUShQKSgq-YBE59FlYF4zZdijW-MbAnv_a76BCaOkxixhOPnVxtwVnKHwYLPBPohQjGgcRPyCO1JxTiPNaZCSdxsme9ID3rz8DE0r7bNYuskZshbd7gFmUdasQMhCnCgq4-AnlAbAoJ2EjRo-WYa-Ez3YOVtCEpZvfLbuthvnnXJMEVFXAYyUlBH9d5B36-9J14jN0JpiItbkgGFDGf-YFL6cV4BkfejtdnAAb_cFXicyuVLHNS0jBNaBx3JPEZtfp4yj9bP1d5d_c1rvQvi-cCIRmnMZl2byzPMLH1h38NbT2YbfbMa5RJlJR4Kl9U9nvFNP90tqcVqHEadfwwEwl_B14N-bzmbzR5hA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیوخفن‌ببینید اززوج‌های‌مخوف‌حاضر در جام جهانی؛ مراحل‌حذفی‌قراره‌بازی‌های‌جذابی رو ببینیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/23024" target="_blank">📅 00:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23023">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7x35l6y5pb0X2_VWxkRrS4PLf1cj3T3NUx-f_DbQdYR_0V_9CTTC5AfFlP7srTCCm66AqK6TMlAHG8xVU6yyWtlPJd6jfFByKCkAIha2rIS4v2Ne2-_KqWtQ7_fJBBZeGeDqWh38SJ6AjbODc0uxvPvHBU8V4VTh2tHZ8CAn-TnLK25hrMiE7mndThessg7MK1Nr5QcVM-oheJMaqAmZ9ZMQ2AnvyQ_ZzljpbM4YZ_s9OGeWKieZea-MU9LpEmFWdBeG34oPQNKuNdFDKBKxHsBvmz1CwdacUE5UQdxlm4QZwq7bMKQ0MZPGqj8hvI9WwYRePoiAjWhkMEZm2uKgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جام‌جهانی‌فوتبال‌قراره از 21 خرداد شروع بشه. لیگ‌ملت‌های‌والیبال هم از 22 خرداد شروع خواهد شد؛ برنامه‌دیدارهای‌هفته‌اول لیگ ملت‌های والیبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23023" target="_blank">📅 22:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23022">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9su5uUHDZv13ifItH1MDNVxbIL_cyTcbJeIlOkLKhembWD_c0KG3ip0A-EE2Ddp2XUfAPoxj3vPXdU6HleHZXQsqaQEquL-NmYJQj_CYul2R_CCpqZZ9egRjo4jdCbJUVyx0ePYHitVIZtruhz0hvgI1WCKIwNOGGCKQ9rhnkrVENGZRbGoC6qJmwxd334shEssEyPWepPntnbxwEqvh4SPFzDlpZ8lLFt0MfHMode3veECCEmX1mqZcpdp-PdZMIZ6vA4TA6S-VDsupv1Wb3B3O8_PG_3XTn7Wj_PovkjBcul-77EfID_3UxXWAEImEZ7GjkRcBWibHWHmvL9TWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23022" target="_blank">📅 22:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23021">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eI6dAyJ9M5RdZkvu6C5YI30L1Auv-9-ljqz_BDCa718dqgTxb3bpdfUoOhsAwrEQPDeMAURwnXhh4aRzgdFW-V9dtnM1fEOTsj1XXXbiJ7XFWOhLMJUrfsUKaGvm4BVkVlGuODUH7JYdMiAwBHodTcOtQgHYKZ7Yb-8v-ROJ0q3PvIe916pNUlL9F1vnXrxqEQQt47w1vonc0p1wBpd0ma99q5lRR1yA4koyUFScMpBNhcn9_iC_8ivOGqI9mC2aA7_An4msxJNv6EELI_18RDV8sWEOKhddZKtYo1e0BIbIjgV01nbMaMXA0pGzndJRpD9C6_qogCatjnAaAMw-qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23021" target="_blank">📅 22:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23020">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f3b11f90.mp4?token=My_O1A98D8LJ0ezyM2yD4fgc9PL4SKLsKbbnkCaw6sfq5wgpBI3jTAjKM_P2qE_jA-Qjcu-GgDpQ7BrCdG9i-t0q6lsLfPYXEbdIKyz83FS0sLZVBol3gFPzr3hQVdmQi-scG0ItdlRue9dbQ0IaRM_E8IVMMzldydNg2vAdeyZzLkvS1iPfntVFJRcJBCsVyUjEtPpziLSHQ0nTnCxC7wgbPl_lMZcvfyeKwQ_i5QJzsZRcQSUiEGuvTKTzgUosR7Sodwff2N3o8ZcWQDHqDAuP9msmFX_iwJptRmOvubZlOl7KzlbaEyWwE66sirV99nMowAUtUAmTZgiQcHaBQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f3b11f90.mp4?token=My_O1A98D8LJ0ezyM2yD4fgc9PL4SKLsKbbnkCaw6sfq5wgpBI3jTAjKM_P2qE_jA-Qjcu-GgDpQ7BrCdG9i-t0q6lsLfPYXEbdIKyz83FS0sLZVBol3gFPzr3hQVdmQi-scG0ItdlRue9dbQ0IaRM_E8IVMMzldydNg2vAdeyZzLkvS1iPfntVFJRcJBCsVyUjEtPpziLSHQ0nTnCxC7wgbPl_lMZcvfyeKwQ_i5QJzsZRcQSUiEGuvTKTzgUosR7Sodwff2N3o8ZcWQDHqDAuP9msmFX_iwJptRmOvubZlOl7KzlbaEyWwE66sirV99nMowAUtUAmTZgiQcHaBQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی‌پرشیانا توسط علی تاجرنیا رئیس هیات مدیره استقلال: وکلای ما خبرهای بسیار خوبی درخصوص‌پنجره‌باشگاه به ما دادند و تا هفته آینده پنجره نقل و انتقالاتی باشگاه باز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23020" target="_blank">📅 22:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23019">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoOk__lUQxzF-um1A9asGb1MxMX9ZaLYYwi1BF3LHS8dy9SQFoMZ4xAoISnnAKgUqHFHx2MLDKMmYw6HuwAXprR9p5W3Rl1tvJ-Fv8GTpe55_xlSLW_Kz7B7PwcOHd4DiDLj1tX0dg8Imv-bIT3cWI8L6aJ-x2qeEhn6wRG242j4KTDkXUH62XZsZ1tPUfYWZmvGcWIuc_1yrtvajLeOTQeeFyWC7AvioyP0KXWLmEUcLFFGfUI-ApGNLo7UARu-BG6q4aiy_N9QZxW_siLvTJUAZWlHhPZP2av9_O5PNSbkoDD9QeRePFI0t3SJZOWKavDdGRcOp-B6SfiI8Kzyxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛نشریه‌مارکا: فلورنتینو پرز عزمش رو برای جذب خولیان آلوارز در همین تابستون جزم کرده و میخواد بزودی 150 میلیون یورو به حساب باشگاه‌اتلتیکومادرید پرداخت کنه و این فوق ستاره آرژانتینی رو از چنگ فلیک و آبی اناری‌ها در بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23019" target="_blank">📅 22:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23018">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdfUg5RoYL6e8f1KTqwO37rEo5oo6OScHpvuIytu7FraghLeCOJq8Pm3lCEGQ1RaBKivPw3Afrm8tLO6OaDqTZNjSCHG8ErETLiRYPFyG__f4tsmKGU1Ta0NtBzQWyRRWq8CzSpWhQQ-4ifP47V9Fy6LSK7ELY6_2X7GAZB7qm5fv5OxdlBM2xKCgSfYNZITTKwyBkAwX4BmTvPV3o_4er8Y57ZZeXyEfib78IEPffpYU9ZCIh7czJHat9UqMdWX_peylJeKJpi-3lzsBAaa_g2DsGdlU7T3_gH14eaP6TuIcw0AspiaXA94wHWkfVs7sjfI2Ci-dL4xxfouHWWP1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی اسطوره‌داوری ایران در اعتراض به کشتار بیش از ۵۰ هزار نفر توسط نیروی سرکوب جمهوری اسلامی در جریان انقلاب ملی ایرانیان، با بازنشر یک‌ویدیونوشت: «برای بقای کثیف خودتون، جون عزیزانمونو بلعیدید. قرار ما با شما؛ نه دادگاه، نه‌بخشش. رقص و پایکوبی روی…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23018" target="_blank">📅 21:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23017">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2huXpSMcXWKFDAAzzYxHQ58XrtJRGCTwwPlZnTq4wIlmaN82YeSBUApT0Z8CFqEqQlSSPeoC2TN6neS2Dtoni4Z6Cipjm_HxdnSHGsr0v4qudEwpA35MJ_64KL-jaDyKXzBzL332qGz4EHW-tGVL3EHKPsv4MklDPUos7rT90rwJUbzHHIV1lDBsFvGfGo7NLNf8oEEhNI2reNoYSlQ94BOBNZP2U5XB58c8ZNeAtaSMyqJBzGUUaWXVwF5D7P-1Hz3LUAiRVscO122_FtlfmB5J1ZZ8vwbVd4urKMp2xN0_djcINopcnmUdtVH5RfIAcdqx1JUmClZV9bgUUY2Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇦🇷
جدول رکورداران کسب بیشترین تعداد جام دربین‌بازیکنان؛ لیونل‌مسی بااختلاف درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23017" target="_blank">📅 21:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23016">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Icg5iHs-Bt91nXWzbCzbgfCIIgt6Y0fID3paa5J2UGA9oU7fDio_IPudUSJ1s9aRALB97TE6PYPy2mZzncRbfrZFqfvDE1ndlK0R14H6BsHeIN2xVLPzwJRvoPahr6tjKJC4mT1RcIuGByJrz6xirPxMfn276cRYWhuI1XoXnhfExldTDy2CD6gbZUF7vMdmoSDLpyLdaPb9QxWpfKdoN7bCcWZi-PXL2PNKMkvboUGtQ7O4oPSZC_YeqZn-QPiDv_fcNBMo5n-Q9QfFCQRcXXLbIiIpjEF8OMJr_wf6IHZ_rwALxQ-NIdpmp4kkJe8r8EiEE_0s4Aw2zh3p66q8mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23016" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23015">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUfjAwQVnfGH6n1sndLkaMXF3ChyJ06e-NWHunuQnS7yYtUs-E6BCxNixMfMqh7V84vh9Df7Hf4M7bWG2fFSJdxL-04d7q6SfY-H1RunXT3ziYDd6-_w0JZ387xO2QhRqQbO00tpm2TzOjSqOs4wl_mS2KbNdLj5JwHtIITYQ4InNQ7BT9l4pDLxnqeA0YMMaBrBTQISbOjkh-JtVQXiXr7V3CNX1V7d30qnLhKk5UCFIOY34FEDXt7RRfD3ZQAQChV_hfYPvDWWAo93C5v2sU6HJUCxTVH1-KWtjfF_IdqaYSZYZNKXHkARZXw8SxzP8xeuW_t_hVRvyMFAigAkEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23015" target="_blank">📅 20:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23014">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=DppUm95xTTqmLmn5RGd19EbS5_CF3GZ8HAG3g6HZN-QX53SyRlbIdnXJHpc0QvWhkWSGb22l03Pjb2gL4BkeyGIPsWj2m3PYeSikUPJlFxMV14An0WKahzjcGVrEzQ3DrU-n1HJ-8KmdH-h9E4-6YH1EuXnKrkEMoYnxrfrASLDF28lBNo6JPHVz1xuV66lFUDK8ZaN6habY13qnWpe6FC-TKQd_pXkwvFd0n6iPkXDrkh1JNw4Jw_FPftVMVtoZFzxBzljUCCWAObG4g_qguKnYHlwKfcGIv7TS_3Z26rAvG2OKC4sS-mO8deU_Los_op3oL3LMf2gbvgQR2b86Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=DppUm95xTTqmLmn5RGd19EbS5_CF3GZ8HAG3g6HZN-QX53SyRlbIdnXJHpc0QvWhkWSGb22l03Pjb2gL4BkeyGIPsWj2m3PYeSikUPJlFxMV14An0WKahzjcGVrEzQ3DrU-n1HJ-8KmdH-h9E4-6YH1EuXnKrkEMoYnxrfrASLDF28lBNo6JPHVz1xuV66lFUDK8ZaN6habY13qnWpe6FC-TKQd_pXkwvFd0n6iPkXDrkh1JNw4Jw_FPftVMVtoZFzxBzljUCCWAObG4g_qguKnYHlwKfcGIv7TS_3Z26rAvG2OKC4sS-mO8deU_Los_op3oL3LMf2gbvgQR2b86Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ما
مردمی بودیم
عاشق فوتبال، تو فوتبال هیچ دستاوردی نداشتیم ولی باز هم عاشقانه دنبال کننده بودیم و دل‌کنده‌نمیشدیم‌حتی وقتی هربار بعد از یک شکست‌جمله‌کلیشه‌ای "این باخت چیزی از ارزش‌های تیم ما کم نکرد" میشینیدیم. بامردم ایران که در جام‌ جهانی 2018 روسیه بابت خراب کردن اون موقع طلایی مقابل پرتغال اشک ریختن چیکار کردین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23014" target="_blank">📅 20:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23013">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI2jzO_6c5VZgFdSNKiw0SN-ZKtpKSZwApDsv3F4vzLWxwc1HzG3ewPtQ474rJyzgn_okS12CNw5OlFDjkNuL9qF1ByncVOqKMxPDCV0wuXQXPmvoWPYoGyKFaMbk46T03dL1qqPMqIRVxZT0ulWANb4zgXEuXBDveh0uwYZF1_jv11dtvkTya6TUL27a5SwyOvbIx5Z49pS7pbVDtFMzNwyKDa0BSehhJaRR--WWkt8-QUMSB8FZ2AqCEP0QOZtNkljws1In3fFUb-Ig-IVC8Ydv01RkB4VVtw8_b7NzhkXqPGU8Foc6lcQR10FRzJd93q2fvicN4SwTLYWTDMuYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23013" target="_blank">📅 20:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23012">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbAp2fx5XydXLenPLnJGUwURU4GAFzyVfJiJ4Qw6qhvw4S6WGlxJinZCOj3AlwD9CbRFWGFwK4z9449QmAxwJ5rGmu7qIsV7FDKFMSF8_jhxRZlSYiWmWhJLCXmpzlShvMXF0gWXwPo0aGkrUG9cg1aiNQHnhjoJPN1Dy64c8ZVEe4GQ55sJq0kCYsQaQK_iZIxl1KNqSe8kGt52hNcuyMdJpcoebXYykCJ3oaujk-KCQMVBNQqF7p20rG0m6mc0fD8gmNkCxRy57W-F9aHJCgR6KZbp7PfIimn26D55Q89oIrOljVB-CtHv6d6mqwskKulQppmOcDIAuAqqbaWfRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23012" target="_blank">📅 20:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23011">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29259cd165.mp4?token=ZYfbd6WAKNoKX2tFYdr_GzatVai4Cms4reWyQy1RHkY-V1z4BpiW-X_oZaik3uWPUgBUdMcQ8cN-6r1xIzcAAXKzbfjniyOVyyPq8_2K9gyBZeGpwd2uUmlq8hKf-dxDObmQN8y9z1YWM5B4TKisbR20mfEFg-AmplWp-jg4zopxN8hWLM7TX-M-nTj4ccFRuYGxqMpDWpRzbHjYVmHfNlKyAWyUE1aO42tNJ2H_Kwgze5C3eira4VYPfRPybhD4u0QWHvBEuY4rwzlO8TfmxHJpffGv9W5GL-PUtvhLP7xCScZLUQYlNr5uRkrXJ3NanOALvW9vkUs-wPcauW9V-5-FUCNvvV_PttDE4hyjfqvNq90AQW4oH8bIy5AmWu82KCpXDIR_Hyns7IkF7kK79yrckKqHdoTKIV-Co02HuvXUHEZ3oBYN8ailK7XgUXqgXgwggMmM3YpHkEKSkrpZldTgpFLk2qylT7eGcoh9EEsZqnzllgjJt8XpXHkLPJP8HMSPucjFrrqN-Iqu-7f3uf4IpnXrSL97muAydG4c_gjpu3_zu2gIxK3qlMuDFu5apnROg0F-aQphfoKq00Iysr3rUBdGC4NGytzkOQxKr3BGtWKw7fsNef7MuuR6ZQgyHR4OkT39IiwSRMpVafAWRXwGzymqzW2CMReEfGBUr9M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29259cd165.mp4?token=ZYfbd6WAKNoKX2tFYdr_GzatVai4Cms4reWyQy1RHkY-V1z4BpiW-X_oZaik3uWPUgBUdMcQ8cN-6r1xIzcAAXKzbfjniyOVyyPq8_2K9gyBZeGpwd2uUmlq8hKf-dxDObmQN8y9z1YWM5B4TKisbR20mfEFg-AmplWp-jg4zopxN8hWLM7TX-M-nTj4ccFRuYGxqMpDWpRzbHjYVmHfNlKyAWyUE1aO42tNJ2H_Kwgze5C3eira4VYPfRPybhD4u0QWHvBEuY4rwzlO8TfmxHJpffGv9W5GL-PUtvhLP7xCScZLUQYlNr5uRkrXJ3NanOALvW9vkUs-wPcauW9V-5-FUCNvvV_PttDE4hyjfqvNq90AQW4oH8bIy5AmWu82KCpXDIR_Hyns7IkF7kK79yrckKqHdoTKIV-Co02HuvXUHEZ3oBYN8ailK7XgUXqgXgwggMmM3YpHkEKSkrpZldTgpFLk2qylT7eGcoh9EEsZqnzllgjJt8XpXHkLPJP8HMSPucjFrrqN-Iqu-7f3uf4IpnXrSL97muAydG4c_gjpu3_zu2gIxK3qlMuDFu5apnROg0F-aQphfoKq00Iysr3rUBdGC4NGytzkOQxKr3BGtWKw7fsNef7MuuR6ZQgyHR4OkT39IiwSRMpVafAWRXwGzymqzW2CMReEfGBUr9M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23011" target="_blank">📅 20:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23010">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSJKLV6lbYF_xHhhH2wwqQA8RdnJvfmkGliNDhAaT52Oq3ldJM119rK6DmsQD5iPpIFywPJSJEPGVyUEYMTcXLGxyEyUIcgZlzxal5keG49JoUGsZcCXNPnqa-vgNh2_8n6ZqBIR_JCKGwz6imHeHanvKJzGgidmhaFf5P34g2yj1coCGPjvy0NhMZSbLSCsqH4Ecw-Ybqcsk9lAKkuYrGf5e1eyKmBwq_zugRLWZigkQssr1wZNF8x1tAd5avxP0jqAJyq-440T_eLTZQfqhLuL5acqYI8YMAzyUi_YsPhmX9yF9QwhNZYmm6a-c4qxVFYiAFIQp5UC1EtgsDddEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23010" target="_blank">📅 20:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23009">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j92rMftzWhqto5RtBsyTKgz74zgizpLk37Oij546OmIFGfIjbLBBg6P_DXosVfLirQcI8MaFJvCXi0JNJnaw3xkVq83TZ_kmIPSNYjsA_TvRvZRv2gRWnvXlIF93scfW_MDJBZSsTwVtAq9Y3-aGSmyJMiLdnecNc5gDo2jRhu_W982N755GIbXHXfWH87f18_r-S5YxlqKKOIPS-NkKbd75VQmHAo4zReldfeqx2OVOgqORy-Z-laABJK3ianeEjh0HeYrsala8_4GYZivMXiRRUF0fXFtpsXBAiu-hlnOWP3ueeSWRqXiwDP1Yiq_FWTHDEQaY1RjSzGg6i6iT5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
لیست ورودی و خروجی مدنظر اوسمار ویرا برای فصل اینده رقابت‌ها به دستمون رسیده و بزودی کامل پوشش‌خواهیم‌داد. علت اینکه یه چند روز صبر کردیم این بود که همه دوستان عزیز کانال به اینترنت دسترسی پیداکنند. ویو کانال قبل‌جنگ 65 70 کا بود الان با وجود اینکه نت وصله…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23009" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23008">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc2809ee8.mp4?token=slROzlJYtpUqsKLSw5S7llqc9ebP8-YPX9UbNBrD26krcTg8lm9umE2q0R6QbsoVS8Ua8Fh5UQFMur8u8Hjf3h8wM9Nek2D_pTbdSYvSBdTLwFPfUOfGHw8W5bqwgyvrUFH7Jrq558QeXX3C1_ggllO16Kr-0xnkpwieeXL6TY-Uq2ea766zSZnpIxS3ys34ZbALZqcosXDy-vcr-okytqZE0UeFNYHWohEUJWwu2z6tagek1BECJlFOG8Q5_23AaRtb9O5I22OhxzfJr7L2QvX1Y45v_my8Jmk9EECShTpR0bb-GuFAXBePC9MP8E41C8Jd6fbHvR6sb3Df3rvhcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc2809ee8.mp4?token=slROzlJYtpUqsKLSw5S7llqc9ebP8-YPX9UbNBrD26krcTg8lm9umE2q0R6QbsoVS8Ua8Fh5UQFMur8u8Hjf3h8wM9Nek2D_pTbdSYvSBdTLwFPfUOfGHw8W5bqwgyvrUFH7Jrq558QeXX3C1_ggllO16Kr-0xnkpwieeXL6TY-Uq2ea766zSZnpIxS3ys34ZbALZqcosXDy-vcr-okytqZE0UeFNYHWohEUJWwu2z6tagek1BECJlFOG8Q5_23AaRtb9O5I22OhxzfJr7L2QvX1Y45v_my8Jmk9EECShTpR0bb-GuFAXBePC9MP8E41C8Jd6fbHvR6sb3Df3rvhcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کواراتسخلیا و کول پالمر تا میتوما و فرمین لوپز؛ 30 غایب بزرگ جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23008" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23006">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIB_6bRdrvpyZ7Z49kskxzqa5E-y31-OnMISlBpEq_rO90nN_8-fgoA-kYPtP4ZZ_gZHAKFrkctsq8AAKR6lq8ghlulLdtX0R6tli4t3BxMFIRl-oZ3f_z6Gg-EjQcUBputmc7lvtQdU90m_nig6DJ9keqQwbF6ZoAUxXlSId-fKD_mXSJBQpJ_YWXMB0SanLL5zz7nPxn0s8nZddQ_qq2E1cn2YL1B6v7oa2ENHhjpwTL801S8e6SLxWvvplRd2AL37J_fUY71ErFcjACqGkl7eH6zatUOGpRdRB1w7c11D7CTOj7QxYEI08ROjC1Jz91ibLjm_lsuvQAEog9Vhcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دبل اولیویه ژیرو ستاره39ساله لیل در بازی شب گذشته این‌تیم‌درلوشامپیونه؛ ژیرو در این دیدار نمره 9.0 دریافت کرد و بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23006" target="_blank">📅 18:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23005">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiEFI69UkyialnEvwgqA7HUeyldxMovLhzZQ2MYPEV3parpgrhf88mb6HT6_dF0bLUgWR3U8sKDOHsqnCVqbmP2UBwP3wO-Wu0gSGiILdS_fvn33zLXuK6RBDllQxczfM-B5UAd3gCTmTw6wvV29WGBGfix-upVmaIHNALWJvqn7woffoMN3A1i4-ZAC2iqa-3byGRJ0zT_BkAuqNTJNgQosDtSeAtlmo2vOmZAUZh-lWTEEBLzv-v-kCG6YQxV9NSMVn66TlsPS5CwP3nv1T_865lg98BVM49KCBQeCgTcrnMADLKkgPw7yDt__NpPn392MYeaVeDU_hjyyKMBm-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه رسمی فیفا: دیدار دو تیم ایران
🆚
مصر قطعا دیدارافتخارهمجنسگرایان‌خواهدبود و به هیچ عنوان این رویدادلغونخواهدشد.  دراین دیدار ارزش های همجنسگرایی را به جهان نشان خواهیم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23005" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23004">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=uYOb8V8ykTkFYb7fudbXUP-4Ug5IAC5OGwLzFEOFkGgUYGrH29lEfP1LvFUPJX93bjZaOpmumn1QYp1aKjG0mVVXFO0JlEra8r4qEaEaFV6DYkIJPQjUSeLVbGrWvOrYThzHBMy_rpv9q_OMcYckWAr1SseGFrwCyib5wyxbGTIRc1hvN8T4P8P2bQzEtz35bPLI-t_1AXzlh-oKW8kifAn_VRNTU6WT0Q472-RkxRhubX8SySOuobdLdJuN4UpA_pf05T4zpSNXqUl2egwajVmjC1I3DFp7CyPhhLzlQpxCqdbk8dnPdP2lL14SIVVYkTeoID3-AN1sKXU0iNwskHkpGMa4sJkQJp-rn4zaMrFvwKTL78LkTjJ2ylDsWZN6TlxPFya8nzmKkZtmOr65q0ILVrEKX4kKFifXWmzPxDyO4zhLfKVlrQhv3Hq-8Mnfq3tB5Y-m82wNWq9ZoXogFiPm09-DcSePkE9SYupoiPVKcl6TPj0CARiCiiM3qMFeiziDKefp5F4_xjTem_GpS9X1h_3z21yFFeJepdfIxfoc9uE5tHzyv3K-PTkZahk9GrpTIHYn2ejxjO_9lomd5Dg7t9wo_EUeEYvrjrqCoULbtRk3iPRA-RY6j6KJCHdxo4CBfclgPaCTC0EqINpE8zHEsx05kr2NG23NdDuaP44" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=uYOb8V8ykTkFYb7fudbXUP-4Ug5IAC5OGwLzFEOFkGgUYGrH29lEfP1LvFUPJX93bjZaOpmumn1QYp1aKjG0mVVXFO0JlEra8r4qEaEaFV6DYkIJPQjUSeLVbGrWvOrYThzHBMy_rpv9q_OMcYckWAr1SseGFrwCyib5wyxbGTIRc1hvN8T4P8P2bQzEtz35bPLI-t_1AXzlh-oKW8kifAn_VRNTU6WT0Q472-RkxRhubX8SySOuobdLdJuN4UpA_pf05T4zpSNXqUl2egwajVmjC1I3DFp7CyPhhLzlQpxCqdbk8dnPdP2lL14SIVVYkTeoID3-AN1sKXU0iNwskHkpGMa4sJkQJp-rn4zaMrFvwKTL78LkTjJ2ylDsWZN6TlxPFya8nzmKkZtmOr65q0ILVrEKX4kKFifXWmzPxDyO4zhLfKVlrQhv3Hq-8Mnfq3tB5Y-m82wNWq9ZoXogFiPm09-DcSePkE9SYupoiPVKcl6TPj0CARiCiiM3qMFeiziDKefp5F4_xjTem_GpS9X1h_3z21yFFeJepdfIxfoc9uE5tHzyv3K-PTkZahk9GrpTIHYn2ejxjO_9lomd5Dg7t9wo_EUeEYvrjrqCoULbtRk3iPRA-RY6j6KJCHdxo4CBfclgPaCTC0EqINpE8zHEsx05kr2NG23NdDuaP44" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیووک اوریگی مهاجم31ساله سابق لیورپول ساعتی‌قبل‌خیلی‌زود از دنیای‌فوتبال خداحافظی کرد. اوریگی با اون گل تاریخی‌اش به بارسا راه قهرمانی لیورپولِ مدل یورگن کلوپ در UCL رو هموار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23004" target="_blank">📅 18:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23003">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=MFnA422eOOtdAMZjS6ACyAWClynrnKu4Hsrqx81IUR4x1YJgA4vgHeKctqEB40qG7iUl-QUPzNVfX5D8udyKqanwX6f9cZjywEusZ4Xtn-rN5nHQS2sO94BesSH6dPwNEUJzM1Mcj2ksDExHWrACD-EGGXUsP5PU_SWG-2E_T6V300Cdb_b9s-A5DNT40BR1rwIshx2DFFkG_X79B5r8SWXoBb66KZDvXsaTSnYefFiZNjViuF3thvXg1Bk9NYsDJRdEZHSch9YF7J7NRCvsecDVx-nKH-HLe_Ogl1gyFaqUQlIPKOUUr3S1ap20c7JC5l05jlT9w8xfZEN0IJvraw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=MFnA422eOOtdAMZjS6ACyAWClynrnKu4Hsrqx81IUR4x1YJgA4vgHeKctqEB40qG7iUl-QUPzNVfX5D8udyKqanwX6f9cZjywEusZ4Xtn-rN5nHQS2sO94BesSH6dPwNEUJzM1Mcj2ksDExHWrACD-EGGXUsP5PU_SWG-2E_T6V300Cdb_b9s-A5DNT40BR1rwIshx2DFFkG_X79B5r8SWXoBb66KZDvXsaTSnYefFiZNjViuF3thvXg1Bk9NYsDJRdEZHSch9YF7J7NRCvsecDVx-nKH-HLe_Ogl1gyFaqUQlIPKOUUr3S1ap20c7JC5l05jlT9w8xfZEN0IJvraw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
رحمان عموزاد شب گذشته در حالی که مسابقه اش‌رو 8 بر 0 از حریف‌بلعارستانی‌خود عقب بود در نهایت با یک کامبک تاریخی 17 بر 10 پیروز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23003" target="_blank">📅 17:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23002">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C78TFYd9rWRqQpFCr69_irg2Qds5CNDPufoEEAa3yBqY25PJQsNE9NQeQ6w-wHVWQsm-UAE157a3-2KCOBI69K9djyhoItu9VJys51tt9UhI55ght7DL7bTMLMB2sW-A9g40UCIHUjDXbzUMKTQ5_eElKo2IcE1q-wEeMifvGlBsgw-5-UJ1wBpFi7pGWGd2mkwRPTeoivOlfladsejjf9ytQqmO_3yt8XZGjCQptM3EvyneWtAF1lwYj386TKStaRuKACfwkJYIxdiCkng2oKVFYTHXjJVKqyme6iSU4czhNEiiqLxpSlHnZPZjPu-mXMeaoY6yOsU-u-FkrZj79w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
پُردرامدترین بازیکنان حاضر در جام جهانی 2026؛
کریس رونالدو با اختلاف در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23002" target="_blank">📅 17:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23001">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUS5oQvLBGceHA7-JkT_PpMcZv5HTPD-aVRYQiExPia6TKm1_y5Fo9_yJgmygzeDqF1K0udac9Vor1hiYk8GC1pIX1jIjo41MxqD1FoMQxdimIzYiOHEnCOsq-EyeW4w-xxP77giE3HMc88oREtkHtNGF2LgBZ3-J2XCDwNzQgQ3mpHX7tJDWdPsdHKYpnGHpqZZ2h2iNKbo_usSbo6EHIO4lcCprOl05wlSszh7c4Kw6X2NnPldzn7eeLcdvOn8Jqtl_loH0e0yBI3Y3Kfavb5yY2OtFFTyeIxgsPnu2Z88qpbmBov0zmXkiLMSAdByswlPD9aIPT6AFr0IeGkj0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌پرسپولیس‌بزودی‌باانتشار بیانیه‌ای جدایی مجتبی فخریان و یاسین سلمانی رو اعلام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23001" target="_blank">📅 17:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23000">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S41UrDQ07KVKIe1R_PNXGjy3e6Mw11N1SquGuNSRNcmuUwgeRxi07rTS4JCvXJHbMqopLIvM3oZ9o3rFtPjSpAj7iyw1fOUJ1zHx4jRTbfbsIBiIohM4bZdogfAV1vzUjjwkacEdUuPqSiQAKV-M4k71izTH2nuE8UXQbqBspiKmlCQuzKfIkFLT5qZtY9aDNG-4GJ82L4ZpLm8ziZheal4143-J0TT2uL8WI3d2miHbusar2uxWw_Stq311sat8eL430WbQgJ9DUyWBsGI6GoCBEjgehltF1CbxCTKz_O9iz0edacyXBZuxNX0a70IBozgy40bNMxEEKjYV3BMYUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در این تیم، همیشه جایی برای پیرمردها هست؛
ایران و پاناما پیرترین تیم‌های جام جهانی ۲۰۲۶
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23000" target="_blank">📅 16:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22999">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvhFn_ILQc21JtcMMfQVw99qCmzukuy2V9Xxi7UmTeQ6vKlSorAhVQwUFIg5nWQH60j3Y6JPtkpfShbbJpQPjGY_pjM8Dh11oy3Cdo-0f6WlOrzRKu-HQxDsFCGrES0oXYTwR9FsnJ-HW255dEN-EjeKQ1J5Szh14CpKpxnBirw8l_lW3cYwpC2motMLMJvDdyR6yqQCxF9BGr048UDB2Ik9ArqMbziNQOUrxD7CtIUxmkSKNGdIuNMmUZgFhZjha1u9rf6iPwwgAkpUnytu19nbwygHiHxqkbKrPQjNeb-METxr_YC4kuVQlAmArU5GUHQms4LjR5AzfDW_pjBvMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22999" target="_blank">📅 15:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22998">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vO8sn_K9qwbdoRJzkx_X2Ztm2RWDPyURedD9CADqWJrrxmBDP97tkrB7qGrLzJt98exMsEtgoBIQB5DSBrB-rh2Vq7lEPoiB-Ns_atxDunzlxssswtmhu16171KiTginoogIuICS1pyAcSjDI6tpznT78lZ8KrM6NXEU9lwXg_Bj_AHo-MHEM3zvfxsemuFoI7VaDkwojHV1nvEWlCNCyClbHZ4HLp01byXLoKgsAxn5AGjXI96_x0CFSZmcoqZElfuwQ7tzc2NxUTthIGOC_C9iEbWghsgAWpjQUgaG1aZEWzRr1ugxZkclMHwKri8apw67omD6QN7_WvnSHq3pTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22998" target="_blank">📅 15:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22997">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORwP3nJiaoZQ5niOsQoucBH5gknjjjXMxpjrIqpWmisG4OoaRhLJ8eBgyoIQeowpB3Nif2ZhpRCqXz3P5ttcTzT8wJTLAYsWr46s9z4LKJ6lvdi23RVOfVou8GQx406urxVuGlYdNsMz5YMpTf3y-pM4LOxDai9cMrYfcYEN_HSGwp_Prs3FLoHNCXztL1jEVMysuATotoz3245xOmPKvX8UuBqu7d_8_d05r0ozr3WUO5TrrE6bbQJ4c5z3J7P6Uy_UCEQFH4h7TO5tRCbwSzBungsQfKqy9uTJnwqbGXEkwacVQeRoHykWxMlbVrOFVnNA8XLxan2WvJTD-iG70g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#تکمیلی؛ رئیس‌اتلتیکومادرید: هر باشگاهی خولیان آلوارز رو میخواهد باید 150 میلیون یورو به حساب باشگاه ما واریز کند. نماینده آلوارز به ما گفته که اولویت او پیوستن به باشگاه بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22997" target="_blank">📅 15:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22996">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=sfYUwqNR91NdQIRCynvm6gAunBXG_hw_1r1O3-qoXR_8gzAelf9gURjIzf8vTex_8BL3xovlIMQKp_VrdpqatSvMDFjUFo-NI2AwQH8_DNO5NakFQ1kYwdL86Q5v3bAi2UEpT5lLw2UlnYQCqfwNvfo2KGkNZWrk3uSatfJ9WqmDPXTYAedKOw5U12ne7tfRL3jPKLhHBUPIYOE-Jf5-Skb_p4FaeDazQ5bzNEMqTbo_a9aBacWwtOjCPeCWJKPWj7rRuwPSJuiYPz4w0W0ERyOP3GEn7niq0TOLKSwNB3u63hWZubPgY4f5xHeoCTrX5tlmnNe2FuMzCdPn2lkDGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=sfYUwqNR91NdQIRCynvm6gAunBXG_hw_1r1O3-qoXR_8gzAelf9gURjIzf8vTex_8BL3xovlIMQKp_VrdpqatSvMDFjUFo-NI2AwQH8_DNO5NakFQ1kYwdL86Q5v3bAi2UEpT5lLw2UlnYQCqfwNvfo2KGkNZWrk3uSatfJ9WqmDPXTYAedKOw5U12ne7tfRL3jPKLhHBUPIYOE-Jf5-Skb_p4FaeDazQ5bzNEMqTbo_a9aBacWwtOjCPeCWJKPWj7rRuwPSJuiYPz4w0W0ERyOP3GEn7niq0TOLKSwNB3u63hWZubPgY4f5xHeoCTrX5tlmnNe2FuMzCdPn2lkDGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین‌یامال ستاره تیم‌ملی اسپانیا و بارسلونا درباره دلیل بستن باند روی دستش در حین بازی‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22996" target="_blank">📅 15:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22995">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2XSOMDKcVLbx66J7XDQrPjtCV9_n2dK6peynWqnq51uFCBS7O3eiy-i_U12cu1wcj5_kgANUjG3_wJCOkyKQzGGpUnWFHCCm5MzfAa10o9U6YMNdpoFxrHWzclgPSEFyvTdgFUn2aVhku-ntmQoDaoBNjEdQcYg8McxYL4WMo7nV9PVGv5kyCiaHrHdpzCNUxUn6MYII1k6AM7Y7VIO8I0O6e08beNeM6f5dKRKz7VnrtjxnDdoRN5Ks1H_7A5-AJaIPDj-31dS1f_G4OQa9PPB57J0FF_otY7U9tzwULvRSs0xM_1YjZHnd6rEbp4Eh7sMLUzizO2V3t9_arBSEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نقل و انتقالات تابستانی امسال برخلاف تصورات بخاطر بحران‌ مالی‌ باشگاه‌ها؛ بمب های بسیاری زیادی ترکونده خواهدشد. هم پرسپولیس هم استقلال و هم تراکتور و سپاهان خرید های خفنی خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/22995" target="_blank">📅 14:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22994">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=WtR5qmCipJKsQnPoUku5TNLmeRbh7zpAUjFeaz-SnnNaTissCLJ7XQQn38ySTv9_WQCm1hj1vZ7OUw8VjUsOdCcWTWg4ytoG9qVGss4kcMVUr60Q2edDFQNhBoeeGHzdhSs1PZgeC-Khk7Sd7JNqhvIUUX33PzNvFrw27UPRVwrUqudQLYvt71ZqPnEoLt_t-w9uWvoSbk5rcqKthKXlvLLXfCfVxO7nk5psA2ntXQWlino1fLYNS7JS3j58GuIkxFI4hBCyKxPYpsZQ3qGJFghyruRL9u7eLLxWIMdPlOigdYmas_2H6W3l6ZESRJEgnDrKk2clHmrjJDSjP9y3Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=WtR5qmCipJKsQnPoUku5TNLmeRbh7zpAUjFeaz-SnnNaTissCLJ7XQQn38ySTv9_WQCm1hj1vZ7OUw8VjUsOdCcWTWg4ytoG9qVGss4kcMVUr60Q2edDFQNhBoeeGHzdhSs1PZgeC-Khk7Sd7JNqhvIUUX33PzNvFrw27UPRVwrUqudQLYvt71ZqPnEoLt_t-w9uWvoSbk5rcqKthKXlvLLXfCfVxO7nk5psA2ntXQWlino1fLYNS7JS3j58GuIkxFI4hBCyKxPYpsZQ3qGJFghyruRL9u7eLLxWIMdPlOigdYmas_2H6W3l6ZESRJEgnDrKk2clHmrjJDSjP9y3Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بازیکنای تیم ملی فرانسه بعد دیدن اون عکس و ژست سمی رایان چرکی اداشو درمیارن
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/22994" target="_blank">📅 13:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22993">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngi4Rx47xpCh4X3w8MmcBW-5cdvXp7hwsPojwWrrgjY17Tiw7vh4XEUdqwTTsYEYMSg5cNTSq-dYr49mGVbYd76bJDOAzrX3kpPGRZt6dJWzmI167Xx1IqUrGadUlPbW6_4NvDguaOJpPL0Hk8uqdpjupzE-RuWUriT3r4cfzb61Kd9bTQLoX9dho1pyJjIXL4UjbuADXp9AwaFt03CEEvS642pidLEFhYQ7gKT-bZOC64kjD7UyW_G9SOfHmvWVVo-5f-oaTHW6sg7ny6ZIOTuI5BUSiUC4m9zd4k4lkRrYxLTCO5xc-fitoEqwevfzzDab9NkbPwdd1ibyIzyLbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/22993" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22992">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jebjfQgowjYaUlnDVwrqSHyRYcpFq47tdLK6nMW04h6Y1ixCPbsaF-GFNrYRuIaCmEqI_mAP7C4zY71FNFM8hKwVVxagNtjtsILGChMXT1m5puT5W96Sndm13W1yPt2nRhF9eXN6wWAcN3Y9WJNnxhJylIWOrrhyRH7xfRdp8ZnYWHRyM0N0ZvqfnxG67OPspG7PhngnqFFkYakz8vkzxMeAVJOq7jtbrmU574JXqADffbpPkMbzSGbYx5pLwNV2ZAWKFZpNs1RkTlkjaxwNqhvP8ZJWl5zF1bypEIGjL_dv6sdJ1_HWmyuKVPMyFpCjKeIfmnOPMHHudcC11sUkNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/22992" target="_blank">📅 13:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22991">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=Ij_DNiyZ5I5_2nhzwq4noBHFxpPoFgB-cak931odW8NU1twOS-kW543I1ghBhVAAMA-m9iPgCRPzhG08el12Mc4GcIXjFDlR987k2l6HsTTZnqNKoc17mxVJwL8JBF5pjQfuVNreACSBB6ISCdUkiCP3CIwx2QdPMLWxzwUpXHD_WudUcwlFj6VzY47QMIJerBs5UOL7OaXdRwsTc1nktoMSNAskktfJsWKX_flSEXdF4CRp6r8BRionIWj38paSU6m3V-Y3ou_YNe3jz3Zuhs-OQfGnGsT52HIMSjeG6x_fbegS3kUCLEM89-xOGAt-VYmQO84x3tvWmdzJVcYdPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=Ij_DNiyZ5I5_2nhzwq4noBHFxpPoFgB-cak931odW8NU1twOS-kW543I1ghBhVAAMA-m9iPgCRPzhG08el12Mc4GcIXjFDlR987k2l6HsTTZnqNKoc17mxVJwL8JBF5pjQfuVNreACSBB6ISCdUkiCP3CIwx2QdPMLWxzwUpXHD_WudUcwlFj6VzY47QMIJerBs5UOL7OaXdRwsTc1nktoMSNAskktfJsWKX_flSEXdF4CRp6r8BRionIWj38paSU6m3V-Y3ou_YNe3jz3Zuhs-OQfGnGsT52HIMSjeG6x_fbegS3kUCLEM89-xOGAt-VYmQO84x3tvWmdzJVcYdPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرد البرز که بهترین خط دفاعی لیگ یک را دارد و هیچوقت دریک دیدار ۲ گل دریافت نکرده بود. اما فرزاد حسین خانی با چای نبات و شاگردانش در مس کرمان موفق شد در ورزشگاه خانگی فرد البرز به این تیم ۲ گل بزند و ۳ یا ۴ گل هم ۱۰۰ درصدی هم نزدند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/22991" target="_blank">📅 12:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22989">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2Zxafp0aj00c3DBRiKmPH0bA0gVozL4MLHs21FjFp9ZSouVbOG6LvY7Dq-tFWv6Z4yWaI9wcj2tx2jbA7dwhEhdh04UsfkOdJfBGwoAjIpvBkFuQrw4BijINBbsAlgKApFLu67m9jd8SKjfVHVWsP8vQJa9pTQVQDnbG8OHPPRT-iwu3SGiw46PqCSLTytHj6HBdiQzp_RFryuJ4wsCupX4pWGtkHVEQCffwuA0UUsY0I0PStXIoEC1WMR4Qs0G5p__nS89mj_A_MmOrCeKLHL1KpnRbah2GfIDiQEYlEI-kal6Q_wraXjgY3840e9oaOpe6XrNjMDv0ihSAttePw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه‌اتفاق‌خاصی‌رخ‌ندهد؛ اوسمار ویرا برزیلی چهارشنبه یااواخر همین‌هفته‌وارد تهران خواهد شد تا برنامه‌های‌آماده‌سازی‌پرسپولیس‌را از نزدیک دنبال‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/22989" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22988">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sm9AO2RFlxjmFEZoYn6_dFWVAqSFEzoEVyr4VnpK-itatjNQj2dUcHVohj3xCwWw3HdCd6zM3JO1QF9zvMv7IMgo6BBKGlPPax90jTbjjUasVpVPF9OSyhkHXMkprRF20ZSKF-76-1QD2VPe1ltsTQqlYLTF6U3Ey6uSd-biU9_gYwe6W558-Swn9EUkJHL80Il7NC2pSDgN5UpumWcCmJ6Q_mBMC9J1oQvHqMVsB92lqDJGkXei3OsgYUE9BOCgJl_EOo79UTDsnnjaAcWJJn0FTzuhhwXn5bMkTgxyKoyufHIqs6bqAkhZ5SJCCZYtTTbfIskX3fBxA7GG7luaOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌ اخباردریافتی‌رسانه پرشیانا؛ بعد از مطرح شدن نام جواد نکونام بعنوان سرمربی جدید گل گهر سیرجان؛ مهدی تارتار از مدیریت این باشگاه دلخور شده و به دنبال جدایی از این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/22988" target="_blank">📅 11:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22987">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c19cf6b3c.mp4?token=VY5XdXL5BNs8xx0H6CMTqBvOqzoqNXCilJ3XwnRarV0rODVYne3_SmO7A1V9ZuQQOyk0d1hjID1nXqe-4o46xMXCg6kUDsbTcCIZxwgkoviZDvlhoTclWrDazHf0_-X481NriRjFmhMJrrMmGX5IYcs_wDUx6DLH6dUjP7L7w7LRq3O9MP0QE_DtqpM7WaqaYFBCfOe4j5dcfZE0KhOR9_GcMupOmUqQUYNTLETpei1uDTx9qXvTOT1OjmcFC0d5KWb0gkSpqounposJ737Gbu0XECGTOQkeGJdmcxVMva5Ln1aXzmkgDqs2fgiY7E0LgpvN_2bjGlIfE1NrnsH0BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c19cf6b3c.mp4?token=VY5XdXL5BNs8xx0H6CMTqBvOqzoqNXCilJ3XwnRarV0rODVYne3_SmO7A1V9ZuQQOyk0d1hjID1nXqe-4o46xMXCg6kUDsbTcCIZxwgkoviZDvlhoTclWrDazHf0_-X481NriRjFmhMJrrMmGX5IYcs_wDUx6DLH6dUjP7L7w7LRq3O9MP0QE_DtqpM7WaqaYFBCfOe4j5dcfZE0KhOR9_GcMupOmUqQUYNTLETpei1uDTx9qXvTOT1OjmcFC0d5KWb0gkSpqounposJ737Gbu0XECGTOQkeGJdmcxVMva5Ln1aXzmkgDqs2fgiY7E0LgpvN_2bjGlIfE1NrnsH0BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نه‌داداش جبر جغرافیایی توی پیشرفت آدما اصلا تاثیر نداره؛ محمدصلاح اگه تو مازندران بدنیا میومد:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22987" target="_blank">📅 10:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22986">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=SHEaDDpyv64sRMJu1HzqSbqHvf1Lpf5pdZTd9OYQZJk1uglD9_wYo5VoGT_JUv2dOd9Z5y9oXKIz3WqctGJPEhvP-u_N1oizU6LG0xqVmsnl5ahnPQHyzmUu6uink-UY75-v2XaFzRlS0i0jxRruP6oSi5O-d5pItIOihfjUHecmUaKKnPkHL7sjGcolHYgObhVlGa8kdyeoSUGf8_XSPNneCxLZRuD1dJChmrMtbe1XxvYkZkLoAhtkx6sCox9D0TG4SsDiQwSahPdPO9hItz7UZPo2wS2jB6b4zUS6MjzVoJs7-TvsYCxBpq2rDpNPS_Jh4iE19473Go-333w2JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=SHEaDDpyv64sRMJu1HzqSbqHvf1Lpf5pdZTd9OYQZJk1uglD9_wYo5VoGT_JUv2dOd9Z5y9oXKIz3WqctGJPEhvP-u_N1oizU6LG0xqVmsnl5ahnPQHyzmUu6uink-UY75-v2XaFzRlS0i0jxRruP6oSi5O-d5pItIOihfjUHecmUaKKnPkHL7sjGcolHYgObhVlGa8kdyeoSUGf8_XSPNneCxLZRuD1dJChmrMtbe1XxvYkZkLoAhtkx6sCox9D0TG4SsDiQwSahPdPO9hItz7UZPo2wS2jB6b4zUS6MjzVoJs7-TvsYCxBpq2rDpNPS_Jh4iE19473Go-333w2JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ
؛
مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/22986" target="_blank">📅 10:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22984">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_WURKYkKsI-ve_V1pObFT0QyszY-ZmFpc6j0btWXYjjkDFq-EFrK1E093J57SBH-EfLt4lQuTI-GPw62XEVR_eK_ron5X55EWwLTbRgT61Lta5Jpt17OuS--MruDbuSptx7WtQWj6A8KUyWtNyrZumuGwVeHZr7Qfs4nMOg7bi6q_1tqAGC8vat0-HK1UTfAKqJ9nJJorBB163AHmd6lLztWcblNsF3yCq3sLUYgfqigRCEee2KP555KaN5IjLV0OgwlddUiY-HP96VPkUGJKy-hUDSD-Xvg159sg6kqUg0B07w_VggpDLPoBaV-eRWqfpA3LhOjx6c7an6IeEQCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K9zbtubfmLAq_CeJXbWTJ0OT1MnXNq7086RtWrIu2H0FZoHfUu3UmA6MCglYDveINdhf0bbC-lRbRo3aYBrd0MRP-K13sUP3YnyZDd22MrWtdOld8_Q4nqwLzL9LnHPbxxg3O0qXAwU77Pa47xvxpvRfPdRbqh6ZDrWhR5wlYCIyzJw3MwF5ghyqlzn1IUrQj3tWwipJaTdBS3v30SHO8sd2ZoTLRm9Cwl6wzxKwygDqWOXv5WkZ1FpjGq_P30NzGGwB2Cb70mI7BaIKb7_q346dHqaNk0hj7LcRSjSdB1Fa6jhjDJkd6UspONzSBG3Rd3Z8l4KpQTS6uxXwNf5zqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بماند به یادگار؛ یه ریاضی‌ دان آلمانی به نام Joachim Klement که قهرمان سه جام جهانی اخیر را با مدل خود درست پیش‌ بینی کرده، معتقده قهرمان جام جهانی ۲۰۲۶ هلنده.  مدل او که عواملی مانند تولید ناخالص داخلی، جمعیت، فرهنگ و رتبه‌بندی را در نظر می‌گیرد سناریوی…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22984" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22983">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa0118288.mp4?token=eBvWible--L59gMK6DGWBtEcTMoz2zKMYRBDGRVhGdMatFz8XatvxT9eNmdbH755LWdoZHm2Nk8uveu6vjuR8kjeDDL3t7OQKk5WoosPmfoCda01Ihl4j42llnQFP2PWojd9WO3Sr0-cIXnSADzq4pf9W4h3CftNyjpbyP7a07hpvAP_cYgm6Rdb0te0t_2taNivQSgdGXYTnH4KmgW4B_Wen2Jpfle0-ejbhrBayPLZrdGGwyFpa2fOEhKSw20YaFyO2xpgGMulsgvrQcj3CwKnMxeqsLzcbOkclaH54HthzTgJceaxoIc2Ae4rmSsk_R0zICeozfskjQ56DKngaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa0118288.mp4?token=eBvWible--L59gMK6DGWBtEcTMoz2zKMYRBDGRVhGdMatFz8XatvxT9eNmdbH755LWdoZHm2Nk8uveu6vjuR8kjeDDL3t7OQKk5WoosPmfoCda01Ihl4j42llnQFP2PWojd9WO3Sr0-cIXnSADzq4pf9W4h3CftNyjpbyP7a07hpvAP_cYgm6Rdb0te0t_2taNivQSgdGXYTnH4KmgW4B_Wen2Jpfle0-ejbhrBayPLZrdGGwyFpa2fOEhKSw20YaFyO2xpgGMulsgvrQcj3CwKnMxeqsLzcbOkclaH54HthzTgJceaxoIc2Ae4rmSsk_R0zICeozfskjQ56DKngaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نشریه ESPN: بازی دوتیم ایران - مصر در جام جهانی به احتمال فراوان بازی حمایت از همجنسگرا ها خواهد بود و فیفا نظرش رو تغییر نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22983" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22981">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-8YFQndHzv1QIfdGct1gl9YvyAyCrJJxz4jz3l4IoAMX3BgjmWIv6Ndw6EkavBiNBDD5AVRwAs7BBa4BMRWf4d5h1EuPC4nmWnIRvlg23i1b8Ob_gRv_05Vo0fJbo8T__MqVTwalhjqzIWgtUs6rWkbUjrLo0NmifeDUNjHC0dd-_48QDQJFBzfwHacVJOmZx8MVfC3upF52b3livaIUxKRmYxg68X95wQlmSTBJ1fsAX-xXMTpX7ZbA1kMJDqljmavZtEn_5FqYD_C9Pl2w2n5C0kne1Zt0IiqHMIqV6N4R6Ns70ETxULQeM_UuEtdRfBPOANpr8sNBCQAG0_B9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22981" target="_blank">📅 10:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22980">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3vfJxLTlgNAF0IIw62A4FFAmXU2-8eD3P5RrlQbxFX5uexR-ZhIoM7ysBj-aj6aMqNWuaC88JWpjgNc4HxTHfZw9V8mnO5DxhZ0vVYkCYLSJGM8r6MZn8dQbuwS1tiQ-OqkdwNbsLmxL_qBIsuaM2aQpYADN459NAF44nHWIfyRDywrxidm0mGqwQTvNaWyz-kALVhfvJc4emOPMjxEFfmyqCxq10OQ8vCHESkjjLmJEPuP6m-5ZXhF67luNMwzMG_xUsxbTl-_1F37QjkBowZLExlprOtcnHNC61exnDXegIdRrG6teXCnZsdPwVyNvzkgMC3s1D1aySlMPTUhQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌انتقالات
|موندو:
مارک‌کوکوریا به سران چلسی گفته که دراین‌تابستون‌میخواد از این تیم جدا شه. اولویت‌او بازگشت به بارساست. چلسی برای این انتقال حدود 50 میلیون یورو از بارسا میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/22980" target="_blank">📅 09:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22979">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fixqFT1m4tBODJ7hXfPJoxNHiXgyaRzf3BL4_GQAne4leHkRZbyLIcCbxUTKKHGs6lgY0GIu4rj0xNgnuG-AKZm96bYFcg6AsU9LSFuXl_4FQ3miiZnCRg4Yo4fIIpPX4ZrhhIKNyRT38WTlAWIh2Dsa4LHyF2JUKmSEuTrM_QbaU3Z3Td71-mUo0NAZNrEhLkwOitqQFr8e_6SKkb4Rby2i3UdBleS8wIQVDR8AaXDd1di8Su8vo4aZX7uiPfT2diCvJjU80jQGRNAVQM5yQaI0UluMQa2t4Fkan2ZXGvosKtt-S_q3imaY6yH4DnGXcHhpthbagXgHD7328716Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تموم شبکه‌ های ماهواره ای مختلف که قراره رقابت‌های جام جهانی رو با کیفیت پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/22979" target="_blank">📅 09:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22978">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsGVTGJaDA4bFEWKlcbpXSZz2dxtPrIBamC1n58B01_zQedHwMPPf_tVa9fc9wfr9pUQjM3YmfTbcgTyAaWyYDgSph5hgFGHic4aMHRl-2Wbx4wGgUjtyDQmq2QXhjKzju6qqsAKEej4T2ZogXSLRkJTQccDMKjQ5lkz7xZVjfIay6g8DMRbsVn740SrJD3akhGxnFRE9C7UezyXWDEEDA4q-SNE5W0eqJDyVW-xyF0LS_TRNq4vnuBTT8uAYG7mIHyg5sbUh96W_imc8i0CpfF7T8v9O3zT3A61DyXXDjtz31G_7EEv21bxsxrJUX35B5sUhCkkW_4CVGMBaQ2ynA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/22978" target="_blank">📅 02:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22977">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlHTSCNMjPpY1fSeLM0Sn1HXdQt7n93wru-SfIrb4HGjvExogwk7y6N2cYXjMzNJCxAHZOPh7vqiM3OWlMhPrAu-g1LNWPsCOXYmIHlxEP7UnUwvoe6Xk1BrYwnH11Qk9ZjN5-d9T9H724_xj9rdw-vQDXAr4KvK5syH8cy-NzmnLPJZVzOJqc4B9Pr3U3dVs_j0KNCT4k92qyu5ag07yP_fzIYT2B_KOvrtgKQFBG9018ld9ercLWklPcu3xEqJ_xm5GrGrWEVRLgrHMLUzjsoqvEHbPUVVUP6eWKat_2DjoXPLDaWsE7Sz2TKtpuLmKAa3Sb9VxkYKXRZLwp2-zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/22977" target="_blank">📅 01:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22976">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nn1T4xl65vCxBb3e-e186QhP85x0EchOFk10HOu4sG2gnIKoN0M9dkbKg9bgnNQS_-zyEGNGFm8CTUWUxBU2vPMYfXEDbXU_xNBf2yYUGn7XnAZm5nPEwzTYFHynhCtiOi4AMOMxpmgbaxpNs1lEebugJQRmMzHbbHaLEfchzFDfStWmeoZMGQEHtgIFdr0jxpOEZCgqCuQZXZ8N15w0iefY10KRG3NKk77m5x7s6PSHBr_sj50r_aZqWl9sldQwuZsw7MfDAxyecDSqL1cjAPkrznWuLP9X1aR3XkWfv5cN_bJUPvdgOc_kj--SwXj3_EnHGQFdiBtk8MAoNnQbLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛پرسپولیسی‌های‌حاضر دراردوی تیم ملی از آریا یوسفی مدافع‌راست سپاهان خواسته‌ اند که برای فصل بعد راهی این تیم شود. یوسفی از پرسپولیس آفر قابل توجهی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/22976" target="_blank">📅 01:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22974">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqZRxTjPMsIHs0DKYu2b_gYtu-Kuou4jPOB7u25P3rVYoW1JBSMxj5BgieIRtw9z4wNDAKudIRWLiZ0lwcJnfUW2bDr89CWM-wdkIrIZuffVEblatmolRiktE9DvD8h5_UuU7KfIm3gZEcYw-giEiFOpp8ChD7f7iLKyDzOR_oeTLA3-3vNRC-p47rf7E_V4PIXxAQrlEvPq-tphzP1bwwSI48Z8wy75kGOqrYj4BQr5n81pHuzDx3lEVSC8rpkITVJGYPdW2G2fUhTZPGbl87xwmWdYapq-ZcyOD70GTTIoE_MF8oPgCcwosIF-ii49ab8k9fd5T47OaW5usaCWMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
از دوئل تدارکاتی شاگردان کومان و کاناوارو تا آخرین بازی فرانسوی‌ها پیش‌ از سفر به کشور آمریکا و جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22974" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22973">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oW8WQ4NonAcjKcSSTz2JRJ_KqhgF616yDF4eIYs1BcpTi5SwronvEDMQwCXXgamIrE0lJwpxOMECvJXtqHhAbsHR9LwcmTLdW8W-sRgSZch6noywYAHUug00bYP-IkUnM7Q8SBzOKV8VnwKnonQcuzrpbiLX7dS162foa2-83hv-mWvN-y_86aDVQdFCpcFkJAU3DlgSjb5wVctZKVVblvoKI4qnIK9Ap9IDtJShHA8JZu_vfHyvNEWGTmQHyA4c7T-X5gDEI-fRnJulcgtkRx6aDNG5-horQ5Efy9S5rWGpv_nd81D3KM7qbJY4p35ulQ64ymqLSu_817GI3bqYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از برد آرژانتینی‌ها در شب‌‌استراحت‌مسی‌تاتساوی درجدال نروژ و مراکش
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22973" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22972">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1TbfTr8RvLJtijMzLyfY3N-K2HQO6Yccp_gz2FnNcpUpnwj17rCUR3-U6GgCzqCUeICI2xDmOyf6VhLAcwRHKphUHW9W1WOAwtrsWp6WNEfjT7KEPtWiFKlc7oHyz3m7t8d9zOUYiHNUCvbcEGwXgKXIUktO5axXQy5h9Y35bsbsb-M3QTfG1Y0wZpIOqvrFUFWsCWdOMf_LkXsD_AWIPoJ3N9P9UTsK3De_l0Vlp4C-F1KqYYmiiVyaz8aM6LsCqzlwEhyovtmks3GBYepMROsU28UyzSacn9hH3E2SqZVtcKcoi4cksHlqhbQZwnbR-YcKqyXaFHqPu7ZmFLHaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوشش‌کامل‌اخبار جنگ در کانال مردمی مجله 21؛ نمیدونم چرا سرنوشت ماها اینجوریه. انگار نباید آب خوش از گلومون پایین بره. امیدواریم که حداقل نت‌ ها باز قطع نشه که هم اخبار داغ نقل و انتقالات تیما رو بزاریم و هم برای جام جهانی دور هم باشیم بازی هارو پوشش بدیم…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22972" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22971">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a6fa71d1.mp4?token=vfxCYzFnvrlkOTnu7fL9nh1UvaI4BAgc-6CvDZUxoRS9lQqTx5WbSXDaVE9rrVKYjlj4IwLOj4nXrPmizGhRvrAdUDpFY4W0YSWKEkNyaiIHM95WucSN1VEl0_a_fzyoZfDFTYiWmTQQleWwve536xlNouNx-qNoDY_fBouovL_Ceco8PhRnQUo_P2dfG0AMSfV7K-L4JoypeG-hDmevjUu3-TKWuVKabhML7Fw-IoG9nJHjMNDrf9Mg0ryiyC7v2JsrtjTH6u2Jj3fmxZQM6sGhMRBsMmDwOYUT0GKbds_Dtozcvhd8d_LIHzSpAmIBKn-1UIkv0FzTE5DZIvB6-I9leR1ma5uNig50kpkbny-D4HbkDd6W6E5Xzh0syzGDdlY9xfLyWoimJmALjGrZm5FtflIRTInsvNTsa1piVeH9dtRNrUqtyC1m-KyuI7KPNPTH5JmkqJHVY6g3RA7tq0fN6a-slV2YMrmmxPmghGQ74k46xC2AEu2J9bKt-Uq3Rot4h4zaUn46jppgbRqPGWhLYQ-s5lrYl2h_GHNtVuk5sMY5Tx_h2EoyyhFEfQjkMrrYIkjo98uKQ-k5uLQKYgWBoFMq9GDAtMr0qelZtjJfVbSzvgCuB-2fDdVYB-j5Yr05xsaA3QgE8jqn_KiqsEkrw-xR9VT-buoDctcZB7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a6fa71d1.mp4?token=vfxCYzFnvrlkOTnu7fL9nh1UvaI4BAgc-6CvDZUxoRS9lQqTx5WbSXDaVE9rrVKYjlj4IwLOj4nXrPmizGhRvrAdUDpFY4W0YSWKEkNyaiIHM95WucSN1VEl0_a_fzyoZfDFTYiWmTQQleWwve536xlNouNx-qNoDY_fBouovL_Ceco8PhRnQUo_P2dfG0AMSfV7K-L4JoypeG-hDmevjUu3-TKWuVKabhML7Fw-IoG9nJHjMNDrf9Mg0ryiyC7v2JsrtjTH6u2Jj3fmxZQM6sGhMRBsMmDwOYUT0GKbds_Dtozcvhd8d_LIHzSpAmIBKn-1UIkv0FzTE5DZIvB6-I9leR1ma5uNig50kpkbny-D4HbkDd6W6E5Xzh0syzGDdlY9xfLyWoimJmALjGrZm5FtflIRTInsvNTsa1piVeH9dtRNrUqtyC1m-KyuI7KPNPTH5JmkqJHVY6g3RA7tq0fN6a-slV2YMrmmxPmghGQ74k46xC2AEu2J9bKt-Uq3Rot4h4zaUn46jppgbRqPGWhLYQ-s5lrYl2h_GHNtVuk5sMY5Tx_h2EoyyhFEfQjkMrrYIkjo98uKQ-k5uLQKYgWBoFMq9GDAtMr0qelZtjJfVbSzvgCuB-2fDdVYB-j5Yr05xsaA3QgE8jqn_KiqsEkrw-xR9VT-buoDctcZB7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کواراتسخلیا و کول پالمر تا میتوما و فرمین لوپز؛ 30 غایب بزرگ جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22971" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22970">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32598b0bc1.mp4?token=cjEu9eZUYRt5Y-Rlj8IF0J0VCtZgsWatXCqUTym5kgieMJ5PGpMjMBmhPPj_y29X5HEz6RyCmIJwYJKaRJr8XuX8zaH-dV5Fas1_-Q6uGY5lvYQqai0L-pWrByPAnbqQlRlQWKcD_rA8vuGP9iO1Knrn-mFOWWrtz_umWCclyjjdb1c2O7VZ7vLZQJ8YM2-vHOc43vBvCNhhBrgKsD2zWoMISI19EVJlUbSPJQPAdyK6xDS_G4Pz85FqR3eiIF6BrZ9DmE3wo8JAexRW0aWXyIIgWfR_GgyeJzA-W1JPgJ_Tg-7z6JjbttaL5fJSsi_yV75GIUfcPRw9hdXiGV-O_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32598b0bc1.mp4?token=cjEu9eZUYRt5Y-Rlj8IF0J0VCtZgsWatXCqUTym5kgieMJ5PGpMjMBmhPPj_y29X5HEz6RyCmIJwYJKaRJr8XuX8zaH-dV5Fas1_-Q6uGY5lvYQqai0L-pWrByPAnbqQlRlQWKcD_rA8vuGP9iO1Knrn-mFOWWrtz_umWCclyjjdb1c2O7VZ7vLZQJ8YM2-vHOc43vBvCNhhBrgKsD2zWoMISI19EVJlUbSPJQPAdyK6xDS_G4Pz85FqR3eiIF6BrZ9DmE3wo8JAexRW0aWXyIIgWfR_GgyeJzA-W1JPgJ_Tg-7z6JjbttaL5fJSsi_yV75GIUfcPRw9hdXiGV-O_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ایکرکاسیاس گلراسبق رئال‌مادرید در مصاحبه با روماریو: «مسی خواب‌وخوراک‌رو ازم گرفته بود.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22970" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22968">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/haPDukJPBqgh2U1_JPium_o4YNw5PLx-Y8sOsoCYFSrVaBiW8aGK-JXESJZdaCbqeCcKr7J53-bp25bSnmCyUhO35u-mpxoCgWrSJmO5sJv4yM0wG0vWyiCaES8W-FKwwdaqDLXiV7Pmv0_z1RkFSm6p9UnLJXt7R-0WlW8-h8auWNWV_KFm12GXNewyWS5GwYPuPheGFecyyPoL9oRZGYapiw2G4TmgElXGAWJDGm9uylEKFQJRSY5fLri3asz1RGR_LrWyfgpYV3Z4IUQpx7LYaxmkkm5Qw46mEFG3kAlW9fjJoQYZXpG3XY2ByGlCZ6O8ve--fvjwheX6B5TfLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای رسانه‌های روسیه‌ای: دو باشگاه ایرانی خواستار برای جذب کسری طاهری ستاره 20 ساله روبین کازان روسیه به این باشگاه نامه زده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/22968" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22967">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca6abec005.mp4?token=CSPdWMechjmMGy6R5xjlHqMaXC9dGTvyUlrV6h5er2-d5sXcZ7GZw8nb6ECCdoBVECaYZQELrfV9gVIB8iW9DWATcp63rK4rHP_CPMJVjeE6RbE64ueHLwOAIt0w5_5A-XMCgxS6EZR4BPYQCop_cR_RHAyVbjsfPJFZ5Fj3zEmfWAMHa6bpMPHvOYPuwigktpTWvSYVPjX-ywckNAfxTzhFDTKFUGjBXDchRMRVPYhl1hf-iiYgExoWRBiWfrcOwB7x7HwN7DZL0Esa9uZzF8g6R86EWNr8SPnkRmAbRyiRvcj2I_eJZSKOtRClJL8yHjlXm2sBgmNRjGUJdCo-Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca6abec005.mp4?token=CSPdWMechjmMGy6R5xjlHqMaXC9dGTvyUlrV6h5er2-d5sXcZ7GZw8nb6ECCdoBVECaYZQELrfV9gVIB8iW9DWATcp63rK4rHP_CPMJVjeE6RbE64ueHLwOAIt0w5_5A-XMCgxS6EZR4BPYQCop_cR_RHAyVbjsfPJFZ5Fj3zEmfWAMHa6bpMPHvOYPuwigktpTWvSYVPjX-ywckNAfxTzhFDTKFUGjBXDchRMRVPYhl1hf-iiYgExoWRBiWfrcOwB7x7HwN7DZL0Esa9uZzF8g6R86EWNr8SPnkRmAbRyiRvcj2I_eJZSKOtRClJL8yHjlXm2sBgmNRjGUJdCo-Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🇵🇹
امسال مدعی ترین پرتغال رو پس از سال‌ ها در جام جهانی داریم اما جای یه نفر خیلی خالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/22967" target="_blank">📅 00:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22966">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REmvtDfpRlfRLQZG0u0OAkmZvLZGWc4P7azcNYUv_Ju6fGmUvuevX6RmW9hGoqA8uErayCFVMyReaWXXlW2SdZs3Lx0BNnEpVReWKojs8ErRUjBBT9l3v00cNraOEpZrhX__p69-1sacBCeY0TaADtoWP7IZiUH8p0ciE_xc_vftoSRA2882TjB7m4z4uJVfn9tJYEeRqQieCfr57QlBqFBwETx5iIAGKIFe7nRYtiti5EiQYkk5QtPEQszWU0Z3HTIvhHdTDa9sbPboEUaFnStVinOYka_Icc6myaHuk5ZVcovSuvKtW9jf4BHNtfpXMbrmP1Q-gNWz1LVDGtrbXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/22966" target="_blank">📅 23:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22965">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouw681L4AE30Qi-n0t7s8WYnZ_-yFq2m2e3R2WpG4fM0wGrxnjmdKSuKEMlsS-YdOVdN4ewgVfq_t56VcTNSqr4mXf4jgYJD91U4QRCdXeMmE7uJwVoUrieKkSxFsLH9FMdl5whr-vl80F3gZIBlfGuMWnPZYQdhmB4Llz6TzjtYudY946EWx5XTac9rzHuj0kq8xkvD0OhzmK6TkKAN5FBXTvfSVZ-_NPjEyHrdZJx9iGYdgfDbaYyQQGgpFjpc7AiRuPOXlj_C-V7JrUC8sqR7AOu6lu7g_qhl3RPnWaRvLtTbo7UiCu9kEh1uKNRgc8XefndaTcnpTO6LWuNQyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوشش‌کامل‌اخبار جنگ در کانال مردمی مجله 21؛ نمیدونم چرا سرنوشت ماها اینجوریه. انگار نباید آب خوش از گلومون پایین بره. امیدواریم که حداقل نت‌ ها باز قطع نشه که هم اخبار داغ نقل و انتقالات تیما رو بزاریم و هم برای جام جهانی دور هم باشیم بازی هارو پوشش بدیم…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/22965" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22964">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eaff3256e.mp4?token=dBxDPrtb4kTY5b_pHQwSirOy1A4y6fmFfYYCOr1ZE1QYC_bEdMDTvsEsSTRc4ENs89j8CsOGJ7T057BPMDUI6uhuZ3rzCMQF4XCT6nvI8uTDnQcpDRvb5iNSLHiy_bEVMqlRJ0s0kElhkxMYhKOyLlgQJTG-O0XaVTGVSFbCeMah-0DtJKGj0SNyHIyoGxvTlsSRnrk5SMmfgwGfjtba7ClmxP-D-2j2_0P3bbT9-0rvfSZ-0po4vUZ-MRC4HBktEnlxFQ2B3O5jKvz86x9TtgWtO4aBKkEDtGX2DBffe1Ji3il9iP6xbRrcRT-OZavPaysXQawlvWJSiYN97cK6SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eaff3256e.mp4?token=dBxDPrtb4kTY5b_pHQwSirOy1A4y6fmFfYYCOr1ZE1QYC_bEdMDTvsEsSTRc4ENs89j8CsOGJ7T057BPMDUI6uhuZ3rzCMQF4XCT6nvI8uTDnQcpDRvb5iNSLHiy_bEVMqlRJ0s0kElhkxMYhKOyLlgQJTG-O0XaVTGVSFbCeMah-0DtJKGj0SNyHIyoGxvTlsSRnrk5SMmfgwGfjtba7ClmxP-D-2j2_0P3bbT9-0rvfSZ-0po4vUZ-MRC4HBktEnlxFQ2B3O5jKvz86x9TtgWtO4aBKkEDtGX2DBffe1Ji3il9iP6xbRrcRT-OZavPaysXQawlvWJSiYN97cK6SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/22964" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22963">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇱
🚨
شمال اسرائیل آژیر ها روشن شد دوباره  موشک ها از تبریز و کرمانشاه ارسال شد</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/22963" target="_blank">📅 23:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22962">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4Ijqz2jl8rcorXygbRDI40U4-OPM7rVT8lkXylASrqlAin4Q2EL9n-XFMXDsZctS0TPfX3kstx1k-F3QWFaR3deQo_OstfindFNpu0htgYuvsIiDmvFX7nQGquReQkT-EpZeXnyRuC5mvgzYBZmvxSJNbZmteag5e-7ZvYqL0Yr9_Zm4id67C4dRfySyHZJNyIeDgI5djyRvW7-klbcECn7425QdrpUFDcCwq1IqmyVBloPnUnN8J8lTIMtg2FeiX3C-HOHykPmQiwm6SC8RmCx4XOJKJN3p9rcDBjIucyR-A9ITCemvNIyMRC_wTemy7GSN9GqLm5jn1eNQlaPpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اتحادیه‌فوتبال دانمارک رسما اعلام کرد کریستین اریکسن هوشیاره و تحت شرایط خوبی قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/22962" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22961">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxzQEl4KxHAHI8aMlynlyQ0PzFtpGz9Ci9TKX7A8sSSoSjln3D1hYZOvXGRFun4b0BSA2JFvL9VdbQL2oWhyjAKzasuYfSRr_ckIWsSHU3OqQQCvBnEu5eYeGHMsoHxHiJPjxXpYg_AquvLtZIGS3jPWBFBYwNhMnEdHdp6M5yDXCIqfqWA5eN_c5pQHjXvDIs2cVc2qAW9dyWf9mXwoVJdOkAURR8LcIylDSdRPrwkro6yVGcbs3yofgW9v10Ui1LRRiofWy6pOd5fDXSD0dXPOTz_nYD7c69FOFko4zRB7hmfSDfAPYRKWauwiFXwPl0C2-S8_wZnCO4iNsGt7EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/22961" target="_blank">📅 22:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22960">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pS3MfKmEppXhGPouQmpEg3wPP3G5g5WPGbveaRstx_DMgeuOxaH4yrwMxallWslZXeASM1Rn6l8RYqA21NWX6We0RpdiNQZMtwW1bJQkI8JvTiqjZ-CEYPnjwhpZ09c_nXOoi125Uj8dpWhWFux5lSOSlf-noXi_hDrSWHELhH8oS6MUcErvvhZeSlADYIW_skNpH3nAaUdyq_04ot_LR0xw8oo1ZNetHiKXGTTZbUEJUoB7EuSeqVYSHbCOvQts1OsVrDHvDYuG4XGueC2s1tg2Yfu_mirIEiOSuv0MfAP808Y5JPuJlFzyFqXSnk7bYZJ1VmllT_aq0n05scGu6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری
؛ شنیده‌میشود محمد عباس زاده مهاجم سابق پرسپولیس، فولاد، نساجی و تراکتور به دلیل مشکل قلبی از دنیای فوتبال خداحافظی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/22960" target="_blank">📅 22:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22959">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NX0joFRII-9s2p82ZVgF8AzpNIOzdDZgTWtSLUeJu7U0vV3P6W8Zb-q8oM_R1KtorFNQs67Q-1rBtdc-DipNe12Pry1xGt52O07RmJvNaZl7Yq6PIyme9rucYlR1JFex2MdMZ5qqHUivXtlSTr6sTuMhL3YOg_nPmKryQNYMeuNyXCrLf0kPOJhgJJTgwiSc8jHvE7lZaH6bWIhbwa_fHm40Y6_i0yEuTjIMy-1vN4ZWuqwkvxeChTK9M6dI5lOk-n-QfY8b1vSNtg07NJrMyLsM6jR83-K7f7M9NRN2I3ev7cETt0Wkc73JXJKOix_SZu-1DsvcQMqFB6vaj_RbzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فوری؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22959" target="_blank">📅 22:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22958">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bffa01c1d.mp4?token=AAgz3_Ye1RYv9Hoa3BQWvzG-NfSr0WkcPqVwyIe1heIHmP_Hj9XDmP5f3-3ELey9i4kUmH0VA9UTeINV0cA0EymFNHbltyaOnglZJd5k7Fu4QC6Tr_DIOLgMaeM1RKkF9bZUJZqPIXxJxxvspq2qotosMbcXirh_BWjpOPizIfLR2PNs3FoIzIoBcUl0XcTajUL9t_n-uK3p0YvzUJT0M0qO4ZIX4Fd45UAEcylP3--IgOz-nfqz2DUtO9Kdejy4_0zW-g1_v4UygecOEw8H7J1slDZWvVA6wIjyGFyN0QUyJrMQPPx7Ht1U3dZxWZgq8uWYE5xxEyjUaBUYWp1bOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bffa01c1d.mp4?token=AAgz3_Ye1RYv9Hoa3BQWvzG-NfSr0WkcPqVwyIe1heIHmP_Hj9XDmP5f3-3ELey9i4kUmH0VA9UTeINV0cA0EymFNHbltyaOnglZJd5k7Fu4QC6Tr_DIOLgMaeM1RKkF9bZUJZqPIXxJxxvspq2qotosMbcXirh_BWjpOPizIfLR2PNs3FoIzIoBcUl0XcTajUL9t_n-uK3p0YvzUJT0M0qO4ZIX4Fd45UAEcylP3--IgOz-nfqz2DUtO9Kdejy4_0zW-g1_v4UygecOEw8H7J1slDZWvVA6wIjyGFyN0QUyJrMQPPx7Ht1U3dZxWZgq8uWYE5xxEyjUaBUYWp1bOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#فوری؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22958" target="_blank">📅 22:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22957">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmJBLlOIH5no0_BauHFsAQjuQYgZgzrY-MKzK9TnNeHMPzhFCtpBLqzhTNVlb85EnudQToLSfLgRroyTlLxkmvhhsHsU1f8HlrjJQDsUDCnOS_isvWiubz_ZZ-fuiXZEsLzcO5PP2VfitZhUdwBlLPnf50y1CWWyDCU8-JPYxkdaw0J54UOOGbImr5R8Pr9yGZ8_lNuEkFqQEEaxAuZ82JHvCA4PTk9ZiUzfvx-XTD1ISB55sn5lFcOa4vntNS9jOs_Bj5gkTiBNpgeLLcTFKKcmBfyfyhrHZh3qshLCnRGray0G9z1-kD0fJg4w5HVtOps04CBczjtQPq8pYSkZAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ به‌احتمال فراوان آنتونیو آدان راهی لیگ امارات خواهدشد. او دو آفر از باشگاه‌ های اماراتی‌دریافت‌کرده.همانطور در روزهای‌قبل خبر دادیم جدایی آدان از استقلال قطعی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22957" target="_blank">📅 21:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22956">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1b174faf.mp4?token=qOFd8jztwtXJBm0EQf24VpAfMS1xM5TmKF-ScDUlDjQwTBe97eHuwV__03KoOb3gex2XESOZA5Bk2yJzcQs7mqhF5XpMtTRQ5nlsjcutShxb5OJTYKDCFp6sOkhwMAY7UfgzZJbojAvF90QmqINa6UUP8gBiPeDxVU9Ncol3DfIzaUQ8Wqe52uRceUNF0jBn5gnICaA4sh5U4XkXdlhQZT3HS4tf5blAD6vw0D7KEGPhchcI-L8Kqf21W55mwgpzhhIFnitF7pKAaDUwlmMFAQBpX_mL5jD26Eoo_GD6YYXyV35LQRZYKq-jZ3Q7EFRKzJflgKAqjy_PTA4YHlGEkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1b174faf.mp4?token=qOFd8jztwtXJBm0EQf24VpAfMS1xM5TmKF-ScDUlDjQwTBe97eHuwV__03KoOb3gex2XESOZA5Bk2yJzcQs7mqhF5XpMtTRQ5nlsjcutShxb5OJTYKDCFp6sOkhwMAY7UfgzZJbojAvF90QmqINa6UUP8gBiPeDxVU9Ncol3DfIzaUQ8Wqe52uRceUNF0jBn5gnICaA4sh5U4XkXdlhQZT3HS4tf5blAD6vw0D7KEGPhchcI-L8Kqf21W55mwgpzhhIFnitF7pKAaDUwlmMFAQBpX_mL5jD26Eoo_GD6YYXyV35LQRZYKq-jZ3Q7EFRKzJflgKAqjy_PTA4YHlGEkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#فوری
؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22956" target="_blank">📅 21:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22955">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfJ3GcEX-6TxpMgqYZOjZSYy3AMjxiGgEDuRrYhIAsBM4xvTXkWwph5z7YuiDksYzNuzhMPGAR1tLaHMkOUA4I4m2SauHHbHV5H_Xrfr2anoq-D2BbTYyZ1cOyu24JNJ-uPBD71caln7p00gwddCefv386tP6YB2Cx2BrkIo9YPRPL3hYlHGBybCN-jPJlPRsg7ApCPqWdXdwdIPc-p2vR4JzxwSA_PXDtQC8pgxQyEyqYKyfr0QJ6bZ-ZmXe686SpxmygBoujUH4ldkOugH1GxXJ7fYtyJw6mYVLLJ_nZeprDAgUugflyICUn3R1bvH-F_WxQdFVHoHSJzXu5ASbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ کادناسر: بعیده که‌سرانPSG ویتینیا یا ژائو نوس رو با رقم 150 میلیون یورو بفروشند. برای هرکدوم از این دو نفر حداقل 200M€ میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22955" target="_blank">📅 21:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22953">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vsks9m1SWwx9mlambdXgyjyMhwQDwl6r81BvAhOvudy9uINYI3ChVVyJzJ--WxK3-QIOdpw2RxWX4LaXC0FT1-h47CYrujgfDTFBWUUNuRnC7ggeT2WtC5GgAE2WiCVvHEADGOM_hOB6IoFfWNJgbVnHTaHWHsxfzHViFpBosI0nQkEMjF_I1XUbOow8rS7AqvDHWZstqQposZbe48_IAbz4jcqvgjAd7q1aCjU2pUKpRyOrqy0VYsEAqbhN8_jPPkxbsAgBSiQn955BpZykgO0uPt3SIjOjlBf0zgCdlcs5aWsAK9m10H3UdMAyOkDKNfHjm6QhVnM9rvjUZNqjKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FcK8qhfaukzyo8vgiJpATszN4v9xqh3JKy_T_ArRbSsbls-7m6OUHsir-xIeMoxkARot69lWYn1rZSS06J3ARNwA0oIVWwFrAKh7TOQk-ddfGPeQA4Cr-FsehOzpVvsU9HtyxBj2snL7BRJ-5ONp2wNn77Y7WWQhWbZHOwnj-1VfheIJwZ5Sk-N36UI4dAigpf-e4vyjb3qt_omHfE2oSHTwLirrs3Idai88eKGaw-3P0-qGNJ6AWPANb3PMxWJP6anK-cOq8nHuy48WaFLQpe_gbkmQYtgzSRv1wmsbm3yyLhcv4np3NbZae9_XArorwhpqAkRTRVWd0K-bOvgFvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22953" target="_blank">📅 21:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22952">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hihml5shnjbdeq0OvqdhFdf_wzJNfy90r7htD2qwFkCxVp3GMTdH-otaiEigqknHJC-lL6C3mM1SYVf6kKsHhkAzQcs7qONScRblzvBeZoW6pNQVymWcu5qlGhlzJml73tEEFBBLBdJJa-9xYsKx8-IEhftKRGe-GuyVt4aaT66AdgeJGHMV_J9Ke5U3ovo3noA97LiPDJjUbZlPqP4K8C69Lb1FkOl3OtBtvWbbJpQGz6Disq0Ly8UErFqZadiZ8MqFrOQk9H_qQt82bccNi5s9Rz2MD4h3wgvTLPH6qf7wm2vY4qN7GXTuOZGSLv4OXUbFnqWPitEK8eCXrawr_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
حواشی‌ دیدارآینده ایران
🆚
مصر در رقابت‌ های جام جهانی 2026 از نگاه هوش مصنوعی ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22952" target="_blank">📅 21:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22951">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=nqjZ7vD3vMwTwwwgOVrDMXi9OLVrZWrWWO9_H9DJ1eOPZqRE4rLG2lSeOOXfPLgNlZDfWiT93bLuUdl2AQ4iktiH9LzJ_byakksfZRuq67Jv1N3H95o9LBys1U7CDan6VNHmkxW60XPIJYRaYe-ErVu3vD7lY2jwgxJ9GwEwoEYAw7yRJyXj1iBKzTOptcR_tOt_B06Io2FB498U6h97KVD-7ubk6AoxbKp-mQ3qGQXcM4rEVuL8-9uK6evrxNePEZJ0xNs_waks0WQ6-j2fTydT4SR3NLbU-IWtIfczVy2VmoVsw3tHbGP2p4kf7lA17CZI6G79kHM0k3dbVYJU9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=nqjZ7vD3vMwTwwwgOVrDMXi9OLVrZWrWWO9_H9DJ1eOPZqRE4rLG2lSeOOXfPLgNlZDfWiT93bLuUdl2AQ4iktiH9LzJ_byakksfZRuq67Jv1N3H95o9LBys1U7CDan6VNHmkxW60XPIJYRaYe-ErVu3vD7lY2jwgxJ9GwEwoEYAw7yRJyXj1iBKzTOptcR_tOt_B06Io2FB498U6h97KVD-7ubk6AoxbKp-mQ3qGQXcM4rEVuL8-9uK6evrxNePEZJ0xNs_waks0WQ6-j2fTydT4SR3NLbU-IWtIfczVy2VmoVsw3tHbGP2p4kf7lA17CZI6G79kHM0k3dbVYJU9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تیکه‌های سنگین ابوطالب حسینی به تاج رئیس فدراسیون فوتبال درباره عدم صادر شدن ویزاش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22951" target="_blank">📅 20:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22950">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PocLAQ6IBBrZgknA6tFL9T1AeFO1CSIZthQlWTg5VQZXtvMEFsZGLU2CbEWPUjVfKgbUewPXsMEMOirYwnz76_EDdDlDJN-oRcP1lHRKTxpGqnRnfsE_2TpF2snIg0qHW5ZPoq80M8Io9y2cPRDN1x3pwgFcbU7vTv4jYuvPQouZxwGlH97dqWo4JghfMihPaEYaivl34f0P8olPYEgNaMiU1dCCrPhCtdHQkXQvvZsKhtDP_IDPyg--Vh0Vnt466HMcS3prr0L_4B0ivAaQQX6bcojBECdeO3WkpUHskxEBqiKFF4WgDEpmb43biIrJ4qJdBFiTZqeAQPVxOk6oRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌فعلی‌آبی‌پوشان موافقت خود را با پذیزفتن دستیاری دراگان اسکوچیچ درصورت عقد قرارداد با استقلال به علی تاجرنیا اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22950" target="_blank">📅 20:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22949">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNOJP7opGlPw35-AHPRpN5aiRjwKCbiAqQf3snmFM_P1HEnlNaiadxjpFPqhDTbFAMhduBIeq-2wh-EmOID09b-ZG5UdQP-4yK0rD_0spYQrmuQ_d_m2rnDPAzOoA0qrpCB80-5UACS3Im6Zn3d46k7X-d7OO1i3cHf0oo6drpew2eBrBxePXTZs-ckuCZiV6wvXggMprmPRo0JezcN27s7sqDgcHb1ovEX7jPHvy7Mr7Y_J29u1fWxRazxGc2R5DbBwvg2UCf-0dL6T_J_pYNYhgFnbxDTpTonyvvsWI1UbfZi47wUtmc6hGRvY-r6ShVyx8gk3LqSjN_Ix9RTJ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛ اگه کریس رونالدو در جام جهانی 2026 موفق به گلزنی شود؛ به مسن ترین بازیکن تاریخ این رقابت ها تبدیل خواهد شد که گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22949" target="_blank">📅 19:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22948">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDgeQZZI_Yy30C5EcBN3xEqLonsOa3YVv22GI0F-prQtq19EhV3G5Y824N0e-Eyskk3elckTOZ_WLntIbCf2YqWDAv6f6cbvZjwuGwHZMw9jVNr4cfYJqNGwRViTkOubQ7DpdtuHi41pW73ADgKAMN2LbODmBhj21UrKcHcvcfsb8lrSYpHc2jf7T6JRg2dCZrqmzAi2tQEs2MDI3_XiaWLFbtSi_9lWIglMD-dWZh8SNAxiO0IIEhoy8JG6BZL0-nBFt79WPi7bT9MtANEyKW9-eZIEdgV8LC74F6GdMrJSwPI8ha1prq_VGZH08tEeh4wL1MXkoDooX3w1TRqFzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22948" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22947">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c78767e61.mp4?token=anJ7J6CnWWJSsCh1mCiXC0fvtas75A1H_c0Dq7jFzgdUuN7PbE9xPQYgtt3rcyaak64lduUz9td5ouvCVuU2rZmhwlM3WqePWqFdXar6LDmT2QAi5ekMb-NBHg9v-Ej3Q8i0zNdSz0KqvJr6yQt90BUM0F6P39laYhLxy3lOCbJP27fHheEx5CxOA1l3mQ1X5APcH0vDqP34U7JpgX8wrwXH3RLLptJ66VoD_Z2OiKUa7KJSiz1arHUiYtlZcpC-sIHBlsEZcbQJWcPD8YPX5A17D6RDlYNPKjDeSY8JevonoTk58bK6ZBA_6-SzXD6JVBQgIKnwL_2iZFBJcnliFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c78767e61.mp4?token=anJ7J6CnWWJSsCh1mCiXC0fvtas75A1H_c0Dq7jFzgdUuN7PbE9xPQYgtt3rcyaak64lduUz9td5ouvCVuU2rZmhwlM3WqePWqFdXar6LDmT2QAi5ekMb-NBHg9v-Ej3Q8i0zNdSz0KqvJr6yQt90BUM0F6P39laYhLxy3lOCbJP27fHheEx5CxOA1l3mQ1X5APcH0vDqP34U7JpgX8wrwXH3RLLptJ66VoD_Z2OiKUa7KJSiz1arHUiYtlZcpC-sIHBlsEZcbQJWcPD8YPX5A17D6RDlYNPKjDeSY8JevonoTk58bK6ZBA_6-SzXD6JVBQgIKnwL_2iZFBJcnliFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
آقای‌ممفیس‌دپای‌هستن مهاجم هلندی اسبق بارسا منچستر و اتلتیکو که داخل و بیرون زمین می‌نوازد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22947" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22945">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrQj24iNWA8FLJTGRpXLg1jQv7xYo4xCW0a-765I3H1sPG1fgjqjEsgE_CSAWd3uVo_L5AEbW1Fh8PkBNIHm3X8NfQTmvXC9cdTjGHZ_ktK3fHNiNu2ufV3Qi7XE7j70U8ZLvT9QWNfcB82Oh0FR9nf3BURb69h8cXB_qqstDzTLLML8WPwlJZsKeOClQxXlZ4QFGloTBHIwgs12CRsUXbjwGooh-K2XIQS0Mbikb5P9P3oXmKz1pYqHJ4kMbZ9Kt7OJQyjZlmTy1AcJtAIyagJuomf2kWmCpLe59ScQnNAHW-t38RmJDRB0e3ovGwTxeZGuYEvZHGdoLAXujME3yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22945" target="_blank">📅 18:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22944">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7i1E6VbTYn2PQqze6M5x3K2aGCdU_rUpHmXz1qoXKSJKiRjE49TJ8UR10I4OZ-Pu6F9K_428MlXVDFlDJfWaaTr8AplHvb9Lu1OxszvL_1mOiwUVA3PEoT7303jfTj8pYl1bxBtiFV2OypQ9QOeYYXSkwduu4u57y-zbTjYWspwEsriWLEcS_P4H3xnoQHHJPlnBqbzKK7_T3p8-ch-n-cE4bACku8X5uwGoNJlZfWQ6O9qaHwlFBaioBAuw6tMWlqtniq0pWdlRJv_Lwmc53s0ebGhs-Tu_ofIpDBM6Ck9PNfW0OsPJzzl21IzZMH1H_ZAfCiAPcBYsOWoc226FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: منتظرحمله‌این هفته فلورنتینو پرز برای نهایی کردن قرار داد مایکل اولیسه از بایرن مونیخ باشید. پرز قصد داره به هر قیمتی که شده فوق‌ستاره‌فرانسوی باواریایی‌ها رو جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22944" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22943">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsggqUYE7CwxKvSfRNv90sONrc8SzXx6QkzB7BLdEms1u5S2n41ccdivU09Hkt9FHnnrl5AgWsSo3X7khoWYKyo3w7r4LCnk7O_ol77KOJTHkAJs_rqw7j4Ltd_q1gOa3JTPRQmibBIk34JCfMM36KGE2NURMiOCFWLJVmqT6zOU2P0h2VgiJEGxfKe97xZSZM796HVfU2ORYFzqed2aSV6y-9IsG7ahKdL8SxCBovJOB-J0zQCPg48n4Rbbc0aH9GZCW-wPA22p6zE3qOGeRof3m3CofpyT-CaUKukFulWXLp8Xy5i_GKRvwa7Bzb2FXibSIvOiZC9ouK1LzRrVpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22943" target="_blank">📅 18:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22942">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=VN-yjE5UqJhu_xulHnfJ8YhLPG6x8jOTRtaUjn_lGPP-7AJs6AgifBwdteGjy84P-5R8YZXfFM7SmxpqIbQGe0-DBIIfruTzZsO_zLoZE5JLsyQfRc33Nqyn2NXCXrWyxn78OAtM9MDnO0AwURsM8XJf0pYwm4csdaYySmjGUSVmZuWZ-a2HKp0wflTteZNVASXtLfP1ODUK-WW9V1NkHYaLkQAAhYKEfiUMQDEqiwz0DaAMiDuy9OecnOTeIm_f9MgRxgtK3aUX69NWpKt-oQ_yxDeBqBdT_9nobYrVjCh-TE5zMyd04_H06X0gaTO2siFeXpKo0Jj_D9tXyifOjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=VN-yjE5UqJhu_xulHnfJ8YhLPG6x8jOTRtaUjn_lGPP-7AJs6AgifBwdteGjy84P-5R8YZXfFM7SmxpqIbQGe0-DBIIfruTzZsO_zLoZE5JLsyQfRc33Nqyn2NXCXrWyxn78OAtM9MDnO0AwURsM8XJf0pYwm4csdaYySmjGUSVmZuWZ-a2HKp0wflTteZNVASXtLfP1ODUK-WW9V1NkHYaLkQAAhYKEfiUMQDEqiwz0DaAMiDuy9OecnOTeIm_f9MgRxgtK3aUX69NWpKt-oQ_yxDeBqBdT_9nobYrVjCh-TE5zMyd04_H06X0gaTO2siFeXpKo0Jj_D9tXyifOjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظاتی‌از مسابقه‌کاراته‌معلولین؛ این چه حرکتی بود تو زدی آخه؟ چرا از روی‌ویلچره انداختیش پایین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22942" target="_blank">📅 17:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22941">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvLlDvFgRjmvZSCiPYFAsCHozdnTc9AZC3tDinERuOXoSKExcAGAbN8Eu6JC8dUsXl7ZMEx6cYW3Tlye6MJW1HXJUisNZ3UfIVZ9kb4_8ZzZ0Ms2XRUt_2uAkFPCBqLux7irYIvebLpTE8HI74jI1xmVDPEVFu164qb7iBY5ovVg9wIoGZisvy2pheYMLU-whjSFgwIXm0RQF6nxq-Y257rA4-FWpDFDtpTbXrxNTtm3UjNWb8GNiGQZ4_gry5ory7RwMPyphG_8Mzz24x9nfTHsSQwXI0tQI7md8AejgQhCtcbrRXJaSHz8VRfrGlmiLgVMiNGxV6B5gZgOyaDRYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22941" target="_blank">📅 17:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22940">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCy9yuraoWoyQMRn9Lm4nQKeym_sggSY04BZkhFAuTPgDuFV10pk9UuTJKzZ2EK7R1hI2gCk5bBr42OAyUcZkMK5TpYY3ItRQqmngXuHxADnH14GQKIicV701zcGZNtrrMDWN4oogXUbfbcHpHwWs46TbscxPfDB8Cb8J-7X8DCCTfs3KMlGsVJTYWfRQkjteed_MCeiK_CPTxmwgy0tiDlsyZ4HyybsCz-UzQbDZaZdpwmblgknCGxxn91fXTEy5g14ZYtvllxe8X-aW9QRxdEmq9I_7QcsqNk_oY1aDPb7kQFkK2lf654hEJ6syYBTBzNLiJxnDZVTdFffPKciwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ مدیریت باشگاه استقلال به دراگان اسکوچیچ پیشنهادداده‌که تنها دستیاری ایرانی‌اش در فصل آینده سهراب بختیاری‌زاده باشد که درصورتیکه جنگ پیش آمد و اسکوچیچ مجبور به ترک ایران شد بختیاری زاده سکان هدایت تیم رو بر عهده بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22940" target="_blank">📅 17:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22939">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoU3H9amMDNl2z4tURYX8cFyO3m5w-FfUyJXSgAT4qv1jRxJOh9K_jPqxmTAcFKBOhIRUp6kgYCe4xIqIT_pFGD0rQapEIngfEFp0AemuEwT9FMvdgLUSxKVKagkJdC5sKoF1J5ajwYJtn3IkazxSKl_GTh26lwAkygldPSUFkRM7WEUp-to-QuccwZr28izKmIxy2M4IxHnmpPOud57wNvnP0bhqEYpZwB6uWIxjGerd7J-8DVOpMmdybGXQc3ysYgWj0X1xSjzHBkpS2WCCTqTwxQVrggmW14z2GajtDcnVS-iCZlQK7FrIXblJjZlQ2YSUg3bsDLqZjESSydggw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌ های رسانه پرشیانا؛ باشگاه پرسپولیس در تلاشه که مجوز فعالیت افشین پیروانی در لیگ برتر رو از نهادهای ذیربط بگیره و در فصل جدید رقابت‌ها به نیمکت سرخپوشان برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22939" target="_blank">📅 17:15 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
