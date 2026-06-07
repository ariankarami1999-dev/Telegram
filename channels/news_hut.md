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
<img src="https://cdn4.telesco.pe/file/jwa-aGPNbzZ3bHB-Hhx__1Av4pwuR4mBTOGMKUVXnD3aZd0dNnj4uY4FQDnzBeYn7aplP0jhUpfHIrWY85IuIl0ph8s7h9Ka9KrOulKjt_qgl4nGo9rzNwmCUOQmRMxTFdCrFMbX8tvI0kv2--qiMuKeriVBoHynElbGYS1KOsZbXOuvny7cWIHeeqLNRDoFboiuy5JjKVmcDE1RqOuuN2dp3Fz9VA8di6p3xAGBBJEPvLnzY1ZVlYrJjAIPUyIW8Q_4Mo8jiOUgI93DyfL9TmXxepE6i-HjhxWhy6l1JBoYVT4X-Adifqa5nLHPtfMk09u3oJYSs-TlqcFdopoVPQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 228K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 00:13:13</div>
<hr>

<div class="tg-post" id="msg-65397">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل: رژیم ایران اشتباه بزرگی مرتکب شده، ما آماده‌ایم
@News_Hut</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/news_hut/65397" target="_blank">📅 00:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65396">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
ترامپ: نیازی به پاسخ نیست، صلح نزدیک است
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/65396" target="_blank">📅 23:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65395">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🇺🇸
🎙
ترامپ: به توافق با ایران نزدیک شده‌ایم و نمی‌خواهم اکنون در مذاکرات اختلال ایجاد کنم.   @News_hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/65395" target="_blank">📅 23:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65394">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🇺🇸
🎙
ترامپ: به توافق با ایران نزدیک شده‌ایم و نمی‌خواهم اکنون در مذاکرات اختلال ایجاد کنم
.
@News_hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/65394" target="_blank">📅 23:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65393">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید: ترامپ بهم گفت الان زنگ می‌زنم نتانیاهو و می‌گم به ایران حمله نکنه
@News_hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65393" target="_blank">📅 23:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65392">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: حملات اسرائیل به بیرون هماهنگ نشده بود؛ اصلا از این موضوع خوشحال نیستم
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65392" target="_blank">📅 23:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65391">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید: احتمالا اسرائیل پاسخ خواهد داد  @News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65391" target="_blank">📅 23:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65390">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید: احتمالا اسرائیل پاسخ خواهد داد
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65390" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65389">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
📰
فاکس‌نیوز به نقل از ترامپ: چیزی که به ایران پیشنهاد می‌دهم؛ موشک‌ها را شلیک کردید دیگه کافیه به میز مذاکره برگردید و معامله کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65389" target="_blank">📅 23:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65388">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ارتش اسرائیل: تموم شد بیاین بیرون
😐
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65388" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65387">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
ارتش اسرائیل: تمامی موشک ها رهگیری شدند  @News_hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65387" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65386">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ارتش اسرائیل: تموم شد بیاین بیرون
😐
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65386" target="_blank">📅 23:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65385">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
ارتش اسرائیل: تمامی موشک ها رهگیری شدند
@News_hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65385" target="_blank">📅 23:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65384">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
وزیر امنیت اسرائیل: امشب تهران باید بسوزد!
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65384" target="_blank">📅 23:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65383">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d76423eea.mp4?token=RJcCouP5LnDHhDYDYYA5TbmQ6xs-uujq3K4d3h0NfVkADxYGUxhsBzTRl1YYvQqXmr1mPJm_WZMpTZkUZgehZiLkZ_EmDS3JHngLkk-vgh7hbqq6seOACY2-rFfzhgWM2YSwg4H5aWo4K9cwDN5XLlIw4LlRM9JtFuINop7d4KeuhRL0FWxu1gMamJ3hykujbvIPEzUsYFdndyLUx6CQCvKJYk_sLsIZ4HvwGpRjial8iA_ItVJgKz8bq8UKuAhYy55ZwWxIgMz8GNzVs6L-C-HWA_HJKmm_lVG5AkQx_14iaAvmmWmTtERK5nMjm29rZhIB7d-Xu5DlN0RdTLmnIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d76423eea.mp4?token=RJcCouP5LnDHhDYDYYA5TbmQ6xs-uujq3K4d3h0NfVkADxYGUxhsBzTRl1YYvQqXmr1mPJm_WZMpTZkUZgehZiLkZ_EmDS3JHngLkk-vgh7hbqq6seOACY2-rFfzhgWM2YSwg4H5aWo4K9cwDN5XLlIw4LlRM9JtFuINop7d4KeuhRL0FWxu1gMamJ3hykujbvIPEzUsYFdndyLUx6CQCvKJYk_sLsIZ4HvwGpRjial8iA_ItVJgKz8bq8UKuAhYy55ZwWxIgMz8GNzVs6L-C-HWA_HJKmm_lVG5AkQx_14iaAvmmWmTtERK5nMjm29rZhIB7d-Xu5DlN0RdTLmnIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات جدید از اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65383" target="_blank">📅 22:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65382">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kw8wSP1u3_p1uEFWfeqAGQaAqJpKH7EXvvqvxTdJbKP3CmayTOLHeI063mMw4B1vM_IxAOHeutSJBMkJTi8ziSTYilsoP1r5VvQGgX9IstJ1iWCEEPtD6BG6c-EMkyMmuOs74B5jIGQrsiE_JUrCmmfo-2WkywT-8q4eNAGkaGmzrR4XKrV-xV5uY4pvIV7zh2hz62-2NHZO6tNT-CfBDH6sqtvW43kivxL5nqzeVsDZ_1Bj2DfviAluC3jCGh3e14Xdnxu7rm5vlktj6P7NZepJuG6bo3S5xtdrWkfUUFH0kl-SvZoTZYk8xgXXGkDBprYHYor9zOmXmKRg-ZcD-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی سپاه به اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65382" target="_blank">📅 22:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65381">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
📰
#فووووری؛ خبر اختصاصی ایران‌اینترنشنال: سپاه پاسداران آماده‌ی حمله به اسرائیل است  @News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65381" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65380">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
گزارش غیررسمی پرتاب موشک از کرمانشاه
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65380" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65379">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
📰
#فووووری
؛ خبر اختصاصی ایران‌اینترنشنال: سپاه پاسداران آماده‌ی حمله به اسرائیل است
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65379" target="_blank">📅 22:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65378">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/asIWLaRYKIGB9o-HlE598HXYic5Kr-QCwYY-ma49XFGxXARMqinI5nw3oImDSPzk6ohprb7BqLOe3j3VW4N4LSzGMtJJA73Bw3Mg5vA2y51XcVE0Up3iQ3uDOyJaZk4eFoKNady72dvKuaE22bRTa_fZ1mfYhLP2OLZM5xersFMG3VjQkou-EwZvRYBDxIZ8xX5I-luHhxFgZ4hGPb_vov962dNYpBF807UWi4ZyVgcztKFGFHHIh0SR3f89ynf-fBysPnslp4UyuGokliuHz7bkiJ7Q4RvswXpMa9x-1JiBZhxNKabe4Qb_uT9kWDLkDk3h3zd01EEp-P5ibD3IkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پرواز تهران به استانبول به دلیل حملات احتمالی ٫ مجبور به بازگشت اضطراری
به تهران شد
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65378" target="_blank">📅 22:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65377">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65377" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65377" target="_blank">📅 22:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65376">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrcdozbgLgRVPwmrKw7yPJRryJYtCN4AG6hOjGo5TvF5Kk0zI523szeZphkEpuYDFmEwEYnhVxoGyMB5zmeXhCmXVZxdhAv5Hs9ZM7KqfaSSrYZrNDf2GDrhQS03VlhHvEmC7m_78lATaNev2tTmQshVmD9fQrMgZsOgQZfhKeq-efakOqrkRorUbVubuz3Eor4KfsL3ddamdUk4IDOc9KKPpi3XO3MGMRTNp8C08pZff1V6m_hgG3NL3vsGtQPKJzpBOpP3rWByhmE9eJRk-rPyD5vxABzk02SeNz0-U2ImEU3KOwN3tOOIaHdjthGie-sLiE6PnQIhI4g1vhWf3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65376" target="_blank">📅 22:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65375">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BeRbT08Jv8TY8FCnEasfbu_g3V1TJW83rt5vqVyXucTUolAYWzTH1FCzVpW77RZqdFZrl1PJppKzW5TBbwdxxn4Fjy_JvrF6YnnB1QIFLLeGOV7IM-Qu-tF7KZcedeEMSqPAzbfdo112BE94lfFPhnWRdClu9mFe8GxaCvusE4VKMwjpapjtgkFnNcJ-GXS_Bh_Et_wVgTOPSV5sqa8HQVvnZe3y3nFRoU7GiLAFzLtXMFrzYSuOdIA8HzTrLNBRgXH9Ua9SOIEpqDOhXlqltusa_R7CRdqED2gnaXEqyP0TrOvjCJcQ-H1wzCR3D0XJdTG_vhvXVh4iERR8Xv7GJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
د اتلتیک: نزدیک محل اقامت تیم انگلیس درگیری مسلحانه ای رخ داده و 9 نفر زخمی شدن!
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65375" target="_blank">📅 21:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65374">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پشمامممممم؛ اریکسن وسط بازی دانمارک دوباره قلبش گرفت و سکته کرده
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65374" target="_blank">📅 21:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65373">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQKn-GtgpxrpooK3bz7_xDEL6emhBwaDP2_5aO_2LoK1m0dhR9mvPQQUSCcS-xk4oXCQZqT48P4sjLmd43cIgVbJkPGNkX2Y_ipSIl_a7N_E5_kJbXgQUELVfCkmQ1jFlqrKZjPntsFe6sycPAWPTi7qMbR-IhI3AAcqjFa34reXsdowJ8jQDwtL-Zc4fubwlMVsabwh1VKpnSr_W9e5ik429JcC_b9JMDjy8n7Pp7jNaZuP_9KuR5q0GOmx6ViROLAUCGpKX13sJUTk568Ub1uNsapWZxhT6dM7Q34Oy5HhlpY6ifdHWiMXrwk8siS3OyaEwzZ7en_vDMttmAWN5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ: ۱۰۰ روز از آغاز جنگ توسط واشنگتن و اسرائیل گذشته و به نظر می‌رسه تلاش‌های ایران و آمریکا برای دستیابی به یک توافق موقت جهت پایان دادن به درگیری‌ها با پیشرفت ناچیزی همراه بوده است.
همزمان، وقوع حملات جدید، فشار مضاعفی را بر آتش‌بس شکننده فعلی وارد کرده و دستیابی به صلح را دور از دسترس نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/65373" target="_blank">📅 18:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65372">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دونالد ترامپ در گفت‌وگو با شبکه ان‌بی‌سی نیوز گفت که اصراری ندارد لبنان در توافق کوتاه‌مدت میان واشینگتن و تهران گنجانده شود.
‏ترامپ گفت که به‌عنوان بخشی از هرگونه توافق، دارایی‌های مسدودشده ایران را از ابتدا آزاد نخواهد کرد و هیچ تحریمی را نیز پیشاپیش لغو نخواهد کرد.
‏ترامپ در پاسخ به این پرسش که آیا این اقدامات پس از توافق انجام خواهد شد، گفت: بله، بعد از آن. اگر رفتار مناسبی داشته باشند و به تعهدات خود عمل کنند، آن وقت گفت‌وگو را آغاز می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65372" target="_blank">📅 17:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65371">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65371" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65371" target="_blank">📅 17:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65370">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qabe7FDBti2E5ig5tLeUb4N7t9uwa-iCrIjYF5VrkpjsNjDKpDg5PUnAAF3qkFWf7FQ8_9Rk0cDikujZRqMCWWETfkZ5AH9pe2doEA3eB7y04-ypH--D4udA8MsanosqzzTChup2pjv5nfD5oPiOU8v1BB3gEnRv2ULS7jfr9TxFgF_YCddmGuwcBOHYmM9FYYeZ_Yg8fSyHI8L0PH4xvxMqdkV7Xlo7awZDn97r5ulDd3OA0h3MJ3esh_5u5UnCWaXkzEvkoJnSv5Y7lmxs56bzNf3QfwufCKwaEp32_EEZL_BVdTyRAkdxe90kjwJk4yUHb1hAXtt2Hu9t4JCH2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤼
روی مبارزات با 1xBet شرط ببندید و شرط بندی رایگان تا سقف 100USD دریافت کنید!
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65370" target="_blank">📅 17:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65369">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: احتمالا بدونیم مجتبی خامنه‌ای کجاست؛ اون از پدرش عاقل تره!
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65369" target="_blank">📅 17:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65368">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
صدا و سیما: منتظر واکنش قرارگاه خاتم باشید  @News_hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65368" target="_blank">📅 16:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65367">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
محسن رضایی یک‌هفته قبل: اگه اسرائیل به ضاحیه بیروت حمله می‌کرد، آماده بودیم شمال اسرائیل رو تبدیل به جهنم کنیم   @News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65367" target="_blank">📅 16:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65366">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‼️
محسن رضایی یک‌هفته قبل: اگه اسرائیل به ضاحیه بیروت حمله می‌کرد، آماده بودیم شمال اسرائیل رو تبدیل به جهنم کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65366" target="_blank">📅 16:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65365">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون ضاحیه بیروت  @News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65365" target="_blank">📅 16:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65364">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L-lBQICoFGusAqBroZXCDf2DJPGS7MY0VmrhQsyHHIGqa8oXQIY-A5YhCHUUlohaL8UDQwX98D4fDvNRwkJBaaLPF7vd9rpm2QfpfKAUK6O4rtgcPJVBANxSbhSpaRJqeE0mvCv0SVeDY0dRYr2MXsUpQF8Uyd2uqimZHmo7DbwA4XczpIvqeYlzKhhdj2OOa0NjCaOn32Y-vlk44KgP6OGveIM8FYIt6EI2rcVQVXrS0V4UeJYYC4e3zmWe0z3AYfyrXaFGYOiRyXWynBvZde9LbAycvPr_PWLO7L6XLyknZcKMb_VJnOvgCsRe8p97LLzcZVcvZQPi2Lhg7h8Jiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون ضاحیه بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65364" target="_blank">📅 16:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65363">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛ اسرائیل رسماً به ضاحیه بیروت حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65363" target="_blank">📅 16:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65362">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGL_RAkMaJtjoxyZmNig6Ye5rFK70-BEFwc7P0BTfWOskwaSrsuNfMyg_3GMXb1ZH4aOyGN9PRF61EhVYXklbrPzaD23J0lpTOmoQPDEZIks_d156KO-eMGtwPCoW12nCx8QbG0VS_DgXgeQkDt37otinKYOF30TlIBeGMQra9OMnXm1zrzqZsnv_iwkjaIypOSWrNaWwYYoGM5kdNoAfLzlFu0E6sF2gPVqJoK1PYjDmZJSyqi0JfZutng4pxmAjsXXrcANbyvaderA_QqnDkUrlbAzfHkc3bnjkD_nSpKpD6uhifwMQmkDlPFap1YYQ3815Z3GqOmr8VUAwMo1Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وکیل امیر تتلو:
توبه «تتلو» از سوی دادگاه پذیرفته و برای طی مراحل نهایی پرونده به رییس قوه‌ قضائیه ارسال شد، ولی هنوز تصمیم نهایی اتخاذ نشده
اینکه موکلم برای ماه محرم درخواست مرخصی کرده تا بیرون از زندان مداحی کند، حقیقت ندارد
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65362" target="_blank">📅 13:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65361">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55cb33d933.mp4?token=bMlkyRnoIi7-41K95GCjFhYyNYgFKnuqtUkn1Ionse66VTW2MEAccDqvakRiapZiNMQFgUxiv1ROQ3yEp2NaF27ucAMwE4a_M2I7naAGxVLpOKfu5Iye6bbO3UI7E6y5ik57S-9MmJW8e-YSAaTk54k1EWyj6DXtBX6twW1gXU_gKqjlIC3vrpkj3eJOIcexrspVlOjM3ImMpdZHv3NEY6dZogGdNM6iR46Xbx49rG5IsqqQnYelIJH15EAvVgyFpuv2u3pIWqC7ZxuFdbJYflmo-zQWHv_yIOCVW4VfP16yst1XYhVkPEQQTJ2rrORio05ru9nH-083A306rKUMhHgeMQ7xJ_W3fvG46JWE5GD6eprZXMBc9IUoUtbCMfLw5yZsllI8dF8y8tUgHLGLa7-5nBwvidTVvscA7I6kYUKAFvqEvn9v93ShJVr37E8e5ynrcJtW875RLIUfNB4NhyZyZlZq-6nBilkd5Gb13crqhMNWl19_nz8nKQpGgm6DcBBs1LaLY6fWLipPIBHC8aTQDJqQOINzBkhGctyBKN5HFSdNCA0EVXPzUm5biu69z5T1-HZEkVprIcJvExt3KCt5DPxHzAFwrrTx5_NOvx_2QbLbS81r-ZwaJXmL0lENAYA0HDoSUY4TAx-pOUscEkW_kLJvRJT3nh_4zS7fxe0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55cb33d933.mp4?token=bMlkyRnoIi7-41K95GCjFhYyNYgFKnuqtUkn1Ionse66VTW2MEAccDqvakRiapZiNMQFgUxiv1ROQ3yEp2NaF27ucAMwE4a_M2I7naAGxVLpOKfu5Iye6bbO3UI7E6y5ik57S-9MmJW8e-YSAaTk54k1EWyj6DXtBX6twW1gXU_gKqjlIC3vrpkj3eJOIcexrspVlOjM3ImMpdZHv3NEY6dZogGdNM6iR46Xbx49rG5IsqqQnYelIJH15EAvVgyFpuv2u3pIWqC7ZxuFdbJYflmo-zQWHv_yIOCVW4VfP16yst1XYhVkPEQQTJ2rrORio05ru9nH-083A306rKUMhHgeMQ7xJ_W3fvG46JWE5GD6eprZXMBc9IUoUtbCMfLw5yZsllI8dF8y8tUgHLGLa7-5nBwvidTVvscA7I6kYUKAFvqEvn9v93ShJVr37E8e5ynrcJtW875RLIUfNB4NhyZyZlZq-6nBilkd5Gb13crqhMNWl19_nz8nKQpGgm6DcBBs1LaLY6fWLipPIBHC8aTQDJqQOINzBkhGctyBKN5HFSdNCA0EVXPzUm5biu69z5T1-HZEkVprIcJvExt3KCt5DPxHzAFwrrTx5_NOvx_2QbLbS81r-ZwaJXmL0lENAYA0HDoSUY4TAx-pOUscEkW_kLJvRJT3nh_4zS7fxe0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با زنده شدن دوباره دریاچه ارومیه هزاران فلامینگو مهاجر بعد از سال‌ها دوباره به دریاچه برگشتن
😍
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65361" target="_blank">📅 11:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65360">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZcZVouJ1EXlnQooayhyo-dh32Hga9Xef7_WZip0rghbA1FAiIG_UwqBWdsdA9B9j53OImfpgpIYIyTtFTJdG_IORHuOOYrmQRAvu2k8r4p_Od4DQGu1Lg2nPQLhc4dWhVyS39727HP4h7QSzGiPQDG_GDPBPX9B4pCRvlDbao_k0_a7DWvbJZF38O33HYTokYHNaFfh90UekH4bbr4k0y1OnL7jtYkH9nGicrCcmvg2fOxLxDGpPFAN4hp7Bzzi-0t4qRQim2GrpQWrgRiaDNXvjKNB9FZCOLGxv-TrXV0zuEjeguGPbEvl0bIBJvrBWjbFqP3whZ_Q8bULmt9p_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز خوبه خدارشکر بعد از این دوتا پویان مختاری هم برگرده جمع نخبگان جمع میشه
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65360" target="_blank">📅 10:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65359">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeyjHQcS3AIAizuoXx7Q3KkvRkcUoIa6RoOsxrV8qmr8NUlzgI6bh6QzDSt45ESwoH9swmkFieDwHVkte49BntsCccEU8ckEhMd_kwMR-ToM01p-Xp8dvVXOnQNoiQLf8hmTTIZdftxTtdYgX0qLvgtWroBVMcDQ_zPzgYseRRNEoxFYbuqQpCVeldaL9TVYzLuB2fwllE9YeLJBtHmiHbbv2YbX2NgfQxThpmqky0o5ScqI5c7Cb5j_87jsKfquH7f7jAluU56XChls_HC6W8zENra8HUNqz5a7IbhGGRWrXam8gVkrZOLVkk0B8D1C9i3h5j5erPktttrec88uhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش یک میلیون تومن وجه رایج مملکت از سال 97 تا کنون
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65359" target="_blank">📅 10:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65358">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884f21c214.mp4?token=OkY78PLRtalNJtF9GaIRck8lWV6GN6aeaPArpAoqIEvTKDYEMr55uCfXWOZEI1I5udO02_cXZdBP07IUfIsW0PDLwHeA8IcE8mMmcP410-7F9RMBOrYUaWO33pyNe_toNNmzs-M_KQlq7FYmUeJhRoYKxAU8QizcTPQi2IF0iL2k7KpXVayjsHBmGNS0McbDZf3YZi9YFtcfHhfamN2kf9istQVgKJz6GP6YHTLwqoA9yExf1-SVqUacGu-aJNLzDV6PpN0v1lK3wTyibnF2faGdfLqhz8fYMr6bXyHEiqQT-gBHwn11nzgva-WTxm-td2gM133CewD-xRaU8Fi2og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884f21c214.mp4?token=OkY78PLRtalNJtF9GaIRck8lWV6GN6aeaPArpAoqIEvTKDYEMr55uCfXWOZEI1I5udO02_cXZdBP07IUfIsW0PDLwHeA8IcE8mMmcP410-7F9RMBOrYUaWO33pyNe_toNNmzs-M_KQlq7FYmUeJhRoYKxAU8QizcTPQi2IF0iL2k7KpXVayjsHBmGNS0McbDZf3YZi9YFtcfHhfamN2kf9istQVgKJz6GP6YHTLwqoA9yExf1-SVqUacGu-aJNLzDV6PpN0v1lK3wTyibnF2faGdfLqhz8fYMr6bXyHEiqQT-gBHwn11nzgva-WTxm-td2gM133CewD-xRaU8Fi2og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از طرفدارای حکومت تو تجمعات: ما تقریبا یک ماهه تو خونه دیگه غذا درست نمیکنیم و طوری شده فقط میایم اینجا میخوریم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65358" target="_blank">📅 10:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65357">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🌐
آفر ویژه سرویس های VIP
✔️
🙂
Standard PLAN :
🔸
10 GB
➡️
90 T$
🔸
20 GB
➡️
160 T$
🔸
30 GB
➡️
240 T$
🔸
40 GB
➡️
310 T$
🔸
50 GB
➡️
390 T$
حجم های بالاتر از 70GB  گیگی 6,500 هزار تومن
💵
نامحدود PLAN :
🔸
ایرانسل و رایتل
➡️
450 T
🔸
همه اوپراتورها
➡️
730 T
⭐️
تضمین کیفیت تا آخرین روز
🖥
⭐️
تضمین اتصال پایدار
💯
⭐️
تضمین قیمت منصفانه
💵
⭐️
پشتیبانی سریع و واقعی ۲۴ ساعته
🔜
⭐️
مخصوص نت بین المللی
🔒
🔖
قیمت همکاری همین آفره
💎
🔴
@MAMADXVM
CH :
@proo_V2rayng
CH اعتماد :
@prooo_V2rayng</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65357" target="_blank">📅 00:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65356">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65356" target="_blank">📅 00:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65355">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SXp9G0EKJC-BLnbTuy8vJzRKToFs4Ls_FtYkvQfk9gA32tdNxCRpkEjNfvNL7b1lt7kK8Ndl_L27u_MUGvJMMOMP2kIk7zvmCovc7A5OWx_L5Jb89C-8fkTeKwyi8YzLqI0tswZijLt5BDWbFzytBxj06pUd9FENYcTImM92b7mHlmbhuCJAWDKV3UZrOHYny9BdqO5Xw0YYGgUwCb3OxELnNehQSZbB5JV6WQOYEik9LmrC56cJkYOLH1WflSJywRuf_YC3YUkyjRCKIMHUXlcs2lod8B2WSBG85m8KYttI9RRwWvBSVMkxrZe2JqX1b76XLsPggfgH5TgSdkFfrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65355" target="_blank">📅 00:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65353">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf1fba69e.mp4?token=MG_n8Cziboqot1P9iGnLyti5AQ5d7htzwu3dL_f6TJ2RWwngfnOIJaz-seX1pfnoIarRlELAtqzNs1y8Fq_sP0CnMIhZxjcC-LhWNOFpBAt1ORFrDB5upoTYk5WnahnMPvop-mK2kKdMqnQtMEpayAqaYHdbowbIM11XHc-xr-GM1UKfYR_PHIXbTRSezYQ_g2vGJJ8X2JCDr5yTgH9HWKk6PUpNlxXLVoem1gFn4URG5yL1eGB30PMG_U0VzYfDGXd3Ewf1LWanyjaN1N8rqJblqaDGr6160Ve5_eDAc7anpfvTMuuzM23bCYNMKPMu-15BQFUFdR2G3pY46duphQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf1fba69e.mp4?token=MG_n8Cziboqot1P9iGnLyti5AQ5d7htzwu3dL_f6TJ2RWwngfnOIJaz-seX1pfnoIarRlELAtqzNs1y8Fq_sP0CnMIhZxjcC-LhWNOFpBAt1ORFrDB5upoTYk5WnahnMPvop-mK2kKdMqnQtMEpayAqaYHdbowbIM11XHc-xr-GM1UKfYR_PHIXbTRSezYQ_g2vGJJ8X2JCDr5yTgH9HWKk6PUpNlxXLVoem1gFn4URG5yL1eGB30PMG_U0VzYfDGXd3Ewf1LWanyjaN1N8rqJblqaDGr6160Ve5_eDAc7anpfvTMuuzM23bCYNMKPMu-15BQFUFdR2G3pY46duphQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نیکزاد، نایب رییس مجلس: تنگه هرمز طبق قانون مجلس به حالت قبل برنخواهد گشت، تنگه هرمز برای ما از بمب اتم مهم‌تر است
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65353" target="_blank">📅 22:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65352">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
صدای انفجار در جزیره خارگ
تسنیم: خنثی سازی مهمات عمل نکرده دوران جنگه
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65352" target="_blank">📅 21:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65351">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUMxhnTvDhtm0ivbcbf-N56WREyVG8ez-wHCqfTCsiJ6U3VFlUeMY2pI_a6-s5GwUJmobbA0aXUU-O_86J1sTcNRcVjGCkriJtnQ6Vdbm4fxKRbajj9aa1UQKrko5_GCdzUn7zQ_P12S8RwTotVS8aom6pCTrugLCmuUsU_EkdRK3uAng8QsV9coCy-Ze9EWkh72imPKAQ2TY48WICCUqz6Cw0DP8beXMZfxXsVH8mxYHI2CCb5B7NscmtrNPHCe4Y2fm3JCJRJqXClrorIsO1wUV2apKSUiK3T6QU5fJlxszuxL52SogEHQJaLKNYYus-Go3D-sCi5o2_FGEMSWfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ تو تروث‌سوشال: کتابخانه باراک حسین اوباما، در ۱۰ سال، وقتی کاملا به بلوغ رسید!
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65351" target="_blank">📅 21:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65350">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/457010896e.mp4?token=OT5WUnev7vnyrKhFBTb3krxnoF8DVASluZecr6fVeHpl73SeMh6Bh6RbKjMWKZScCJ34LJs3MPk_EtZwHBF0c-AJk_3n5CRV5_0fqXNiGTj3UtgPAjHy5xdhvVXtOJ1O_Bg07_6FTwkpMCCNbiUEByyHATI12ngxuNbUhnxQX3bUcEhQOuC58B88T-Dh1WHFg6yWuiWi2VvPWJdREybdAvrLomLm8WxTwY-MaddvMHqNbmS5yTk_srfn7t3BI70fzfYTofkfrE3eyhkhvOIapchbWKzzrMX13o4-oefMLjIAyx_dWA2TF0L0DreWAn9J4K0obMTZ-G3c972WdqzoOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/457010896e.mp4?token=OT5WUnev7vnyrKhFBTb3krxnoF8DVASluZecr6fVeHpl73SeMh6Bh6RbKjMWKZScCJ34LJs3MPk_EtZwHBF0c-AJk_3n5CRV5_0fqXNiGTj3UtgPAjHy5xdhvVXtOJ1O_Bg07_6FTwkpMCCNbiUEByyHATI12ngxuNbUhnxQX3bUcEhQOuC58B88T-Dh1WHFg6yWuiWi2VvPWJdREybdAvrLomLm8WxTwY-MaddvMHqNbmS5yTk_srfn7t3BI70fzfYTofkfrE3eyhkhvOIapchbWKzzrMX13o4-oefMLjIAyx_dWA2TF0L0DreWAn9J4K0obMTZ-G3c972WdqzoOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با وجود مثلا وجود اتش‌بس ارتش اسرائیل اعلام کرد که در طول آخر هفته به حدود ۱۵۰ موقعیت زیرساختی حزب‌الله تو جنوب لبنان حمله کرده
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65350" target="_blank">📅 21:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65349">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65349" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65349" target="_blank">📅 21:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65348">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9RgEsnc4CnN72HtgIeOwpr9kL2HPa8GxUMtz-BON0E49guIY5JYtxUsvxa3SxWgZvaMaK1z76NJ9HuCI0XJwCm735nG5S1rmoAMNwWdWpUoOq1Wq3B7Sj-qJVsi-UdvulYiuVfv314wy_jAx_PmqXIq3PJkE1tfoyXz0grPA1XhxqctiCiErX6UfzQC0h4YBNg6OyxTbL7YLodwXbvB0MSWRI1WvE8QSzOUTjwAU3L35dNW0KHVIxQXkaDjFLD2uDH49QSavye_h5sbMQo4NW8l2QW1Xbk_5Y4JCBy_BKShR8tmqypuiEHDV4VELMSKifqp8xdacy-p_I66P_vZGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65348" target="_blank">📅 21:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65347">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6388d22ab.mp4?token=ShjjyDfJurZugzhKLrsaNi0GlWsf2IcKhsSeup5kP5Hsm7ERt3ctTr7laUfSP4cFkb0UuT1DH0K4Rwz88qyXvGWaz5ILtfjtMAsTWybMduDuvwh5W2n3XJYDsQnuco9Cqt8Tcu1G6aqtB50X2PN0E06DcdfMfRp3CthnVmIdWoGRMGYcqv2yMyem-NkSCdFzXTpkVtp_0cO3fsXPSotuOK4pyZsM8wcleT5Rz2Ta9fhORuQYQY_iNhvbhh-K7iPPc8C_LICPTD_zfeTvEmHpRrs6AkSpszrY_Q5t58BJ6ZFOI3220ys3YIDYA14DpJw4Lodz-21LYua18zuD752CoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6388d22ab.mp4?token=ShjjyDfJurZugzhKLrsaNi0GlWsf2IcKhsSeup5kP5Hsm7ERt3ctTr7laUfSP4cFkb0UuT1DH0K4Rwz88qyXvGWaz5ILtfjtMAsTWybMduDuvwh5W2n3XJYDsQnuco9Cqt8Tcu1G6aqtB50X2PN0E06DcdfMfRp3CthnVmIdWoGRMGYcqv2yMyem-NkSCdFzXTpkVtp_0cO3fsXPSotuOK4pyZsM8wcleT5Rz2Ta9fhORuQYQY_iNhvbhh-K7iPPc8C_LICPTD_zfeTvEmHpRrs6AkSpszrY_Q5t58BJ6ZFOI3220ys3YIDYA14DpJw4Lodz-21LYua18zuD752CoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پخش دیشب برنامه «خیابون انقلاب» بخاطر این حرفا لغو شد.
ما اسرائیل رو تهدید کردیم اگه کوچیک ترین خطایی کنه میزنیمش، الان لبنان رو با خاک یکسان کرده و ما هیچ کاری نمی کنیم.
ما همش الکی تهدید میکنیم اگه فلان کارو کنن مام فلان کارو میکنیم، خب چیشد پس؟ یه بار به دشمن نشون بدین که ترسو نیستین.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65347" target="_blank">📅 19:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65346">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajeqP4vCw0aNHWvZ6DhpXoVBbIo2c3XmsbA_WTmjU3-UFppNbuoC4miLYEe53GiB91r9OewSX0rSYJD2wY6h8pDV_ZRnCkcJYjtojCVSy8bDjjtvfJEVcrTQHhevb77v5NBSPDaRMjczIw5lVJwW2x6eu_f_zXBswbxF_kunDyqDqOrHDW0cpXpuqSBHB3Z9gzW9niu_zfF6UsOqUDnjpLd_CRZZCaA2DcXDyf-Qzb3IB-TvAPwoBA_bc29FP2F9DkWYJuEHrMkIWCsnp5UAfRdeBFLmxir3QpiZFJBKYMF122nIpXiYUo8V80H6l1jzOqeJ-dzsY3Nv2yYqkO6UuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام وزارت آموزش و پرورش رسما امتحانات نهایی پایه‌های یازدهم و دوازدهم، به صورت نهایی و حضوری از تاریخ ۱۳ تیر برگزار خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65346" target="_blank">📅 17:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65345">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f4e56d3b.mp4?token=niS-Dg2gLhk6pbg1J6adWkg4U936N57oSsUKTo_TZtrkWA3Uts0qOo59H85W3yhqkVzL-SSMVWJsUZal2CKeaHfgAG59mH_rVWK-90Up_tXadPfSY3SrWiZwVCXLqNS9hK-wm5-nNw-8MSGRB2cx3tU8HtDQBAmOb3FyujexUoX4IVXpZ4YLEiB9mpH7Or6MQoEbbbkFPEzZZNqysdmqjlEPrQKNPjPq6Ag8UTEv3M4TnV7kmPVWDgG91Z4idMrCr2qyyB7DCea5tZeTz8KQLfw_jH0n5AOdZzprMFmmBARNCrIwhv4xyL7O3AyKfN_SQOZ06ko6wAu1crXHPCOtGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f4e56d3b.mp4?token=niS-Dg2gLhk6pbg1J6adWkg4U936N57oSsUKTo_TZtrkWA3Uts0qOo59H85W3yhqkVzL-SSMVWJsUZal2CKeaHfgAG59mH_rVWK-90Up_tXadPfSY3SrWiZwVCXLqNS9hK-wm5-nNw-8MSGRB2cx3tU8HtDQBAmOb3FyujexUoX4IVXpZ4YLEiB9mpH7Or6MQoEbbbkFPEzZZNqysdmqjlEPrQKNPjPq6Ag8UTEv3M4TnV7kmPVWDgG91Z4idMrCr2qyyB7DCea5tZeTz8KQLfw_jH0n5AOdZzprMFmmBARNCrIwhv4xyL7O3AyKfN_SQOZ06ko6wAu1crXHPCOtGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این وسط یه آتش‌فشان تو هاوایی امریکا به شکلی آخرالزمانی فوران کرد
الانه که تسلیم تیتر بزنه کائنات انتقام مارو از امریکا گرفت
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65345" target="_blank">📅 16:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65344">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxT-8KtoXiBrrAS0xxSS5-SJILyYGItI4TKYmxVfSfYfm-HdDXSItxylTp32oIUtvHu53We9rp-2kyvR15glss0H2QEhpQ5lCCX7LSUEMu2AsEmUWQK6Va-8_8IYCvmxFwQhFJRK1a4mcuTSo_1kr0vDJNGigzEA-QssVcgXxHdVetGRztns-N6-q0qX2H7-MLyU1cPbytmJLYwPwYgoDOXcPeJaanFG7ShasvytnIdClr72Fne9DgYuU7BYZ9BcP07G_ICxEar-VkWEyxd0yYPxMCwv0KibsKKK6ySwFlX_xRGBuCENyhS2kiy_Dt4TFD2kjs9VAejkCwf2G2NIGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جمهوری اسلامی پاکستان به دلیل فراخوان اعتراضات مردمی اینترنت منطقه کشمیر رو قطع کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65344" target="_blank">📅 15:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65343">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01c119656.mp4?token=Ns8juhD5eO3NWFQRo89lJ_zL1twKlS1Q6XbMuP3d-F3Bv8nmk--8VbyQlwPmgFpEs-27mK1HQAJW3gSsRQRfldZ0zr5wXfxXzY9swIWZr95-N9-NECjEJlV5rAR7fADsB-CcjM52SLVEviMEJGe8i7815Fls3lnRItqgRo2daHuGAXWdcqe5QH6IIJ4Ktp1thr6FIRxrUcyeRN8W41f6a7IUEclsQ0aIIA_ycS1wbAyMtQa2PfobI1zrFxiMbXoLKB-ljzVRBQayzUnjTB6m2E-eDmiYo-CwOP976uhFJxlxqN2xNCm8XMy9TyJ0vxOuUbUbgt9CcnYgsk6Qk9CogA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01c119656.mp4?token=Ns8juhD5eO3NWFQRo89lJ_zL1twKlS1Q6XbMuP3d-F3Bv8nmk--8VbyQlwPmgFpEs-27mK1HQAJW3gSsRQRfldZ0zr5wXfxXzY9swIWZr95-N9-NECjEJlV5rAR7fADsB-CcjM52SLVEviMEJGe8i7815Fls3lnRItqgRo2daHuGAXWdcqe5QH6IIJ4Ktp1thr6FIRxrUcyeRN8W41f6a7IUEclsQ0aIIA_ycS1wbAyMtQa2PfobI1zrFxiMbXoLKB-ljzVRBQayzUnjTB6m2E-eDmiYo-CwOP976uhFJxlxqN2xNCm8XMy9TyJ0vxOuUbUbgt9CcnYgsk6Qk9CogA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام ویدئوهای حمله به سایت‌های رادار ساحلی‌ایران در سیریک و جزیره قشم را منتشر و اعلام کرد حملات تلافی‌جویانه ایران به بحرین و کویت رهگیری شده است
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65343" target="_blank">📅 14:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65339">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nswO1eX9wDHrzVyLmD-9FfOFZ4Idj8w6Pbw4X28EK7vccTxSAteqXlvb0i_7XAAQfEIPkblYO8Y6jM8RrRSMkNgH1qsS4fADZlRfrcnw8sG0RFbbDSfAK68xU3VSADwK3-YSX7giXcTLu5rygha4xessEZrLdO6HTjA2eSMcJQ-lq4h9QpAmbBZvH-CNOlKTDlbm8YYR-L7_xd7laKSxIk-HLisQFTSNVQORKUVgMlZ5oMhu7ki7leIOPJLuAz9pAY20frsyyq7c9JpNT1uK_EWJcFR0eSE5ikNHXJYxAfYIjDFGMI7b6E36XTuxkhV83T007sljuUTgfhNyULp7oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YooIbm3BYdtSEfZ83smw3zm-BOZ9QFYx4Amracq0sM8j33LaXM4uSF2FJVUISUrUeW3thJdCufkneQid3i2JVDuFnsutSY5P71uIk0VraEx0d2PYZrI_C7ePSgpmbJEqwmTDmAUbl7gfGWDa9gUoO_mPU0orXvLxBdY2cIvGHl1tj6HSlgm2pxG5Kes33iWXa9xFhfT5ZpijyM3qCkEEGF8z8RtyeCpUQy9Wa13OYzJccT8z_5uwArN8_Eb7FxABA4qmlmOan0Ci1df78YCgDOyG9wVGLqvrPpOAPD6W6AXeZjMMUGwzWxNipchjOuLTPFl7hXm-GsPa5h-rvaR5YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KqtqjNFYHdCsKy8tGuU5rHXe_SOjHT3WXOqSGMLlkZktDRwPW-LDu3TQ3HbDz0LUmr7opTFFtbXGasMK4jxt3nDpKIFcwvLGcGhuDmq-CbCQrOuIctXmNG_8LzG9A8FtiedQ9blV_QOdLAZPHbYU47zB-c8FcgE7fpcCPyEi45FCzMWMFMMlapzr9Me-UIZhv1PpmDOtBMZ1EJLoO4LPe6SJXX4-SfuEA6WXuGI61cTsSZRHx8WXZ-f46rJZ3J4Aw7H2Enf_VZrYc_ia1zFsyxvYYjXIoxJPS6T7XQnWdMKcgNVU4mFHtqGoScxu34I5bopjXdTuwvu6MGLm7R2Chg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65aa546373.mp4?token=v-GQiFnUQcfE14iuHMgKK_wpmkdqEC-GPFGiO3IUYKM1tDG4_k4C7UMpF8QsFOA_vYEyERYt-pQHa8kRGSD_DSLqsoJsg-O94r6CY11UUfEOBCx5TUJ4w6lW7QcwPf-2ZoDFBwpjhWvVvtg7rJFzIpPhOljbUkOQG3yfPf2yLDv9mq-C_8WKjrVdrDTCSA3xtyBBx-6_btOQqMfjARUIbwuvhLv0yQ3OSIZyWW1OPMIACj3SewmFOiTAdAtarDoPaAP1cSGh8g_tdbfjPykqEUi3rdkJceQ_sCu0W-_Nq3ba4hU3Quk9t-jBkrpG8eBXpEK-u4kiP0JSeYFQoY6iLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65aa546373.mp4?token=v-GQiFnUQcfE14iuHMgKK_wpmkdqEC-GPFGiO3IUYKM1tDG4_k4C7UMpF8QsFOA_vYEyERYt-pQHa8kRGSD_DSLqsoJsg-O94r6CY11UUfEOBCx5TUJ4w6lW7QcwPf-2ZoDFBwpjhWvVvtg7rJFzIpPhOljbUkOQG3yfPf2yLDv9mq-C_8WKjrVdrDTCSA3xtyBBx-6_btOQqMfjARUIbwuvhLv0yQ3OSIZyWW1OPMIACj3SewmFOiTAdAtarDoPaAP1cSGh8g_tdbfjPykqEUi3rdkJceQ_sCu0W-_Nq3ba4hU3Quk9t-jBkrpG8eBXpEK-u4kiP0JSeYFQoY6iLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بعد از درگیری های دیشب سپاه با چندین پهپاد و موشک به بحرین و کویت حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65339" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65338">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIamXerxess</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65338" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65338" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65337">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIamXerxess</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpLF-BCPTsZ6Hv031v98edu4eCFAUq5qNHAO2nU4bERy2kyp9WZTnO4uiaRaVkZIrx7TZKGxBSiwhRWWXnF64WqGC8x3t4DpW1rC3f04o4h5E6V98Fcx9IxYwPb_BR2cpr1R00ln7SaIj-Du_IzPiyg2XYnUcRYsrGJ0llTFO-us0a3tnfNHgyVCZKs9HYWt8pUtb1uHHuYeKAzNB4R4qHEOR1tcxXEaf4p_LCNr6G9BiZnb9cFnzpyYOcZrgf6QItTm-MNxdlk6rOZxZMQ6YpU4drEYYpWLvKZgPzje7-QgVn-TeWVmVa72Kv8m1JIJU-tTUgnpAC7DhN0WGoL2pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥊
پیش بینی بدون ریسک بر مبارزه
Muhammad
🥊
Bonfim
🥊
🔸
اگر پیش‌بینی شما اشتباه باشد، یک کد شرط رایگان تا سقف 100$ دریافت خواهید کرد!
🎁
💥
با پیش‌بینی بدون ریسک در هر حالتی برنده باشید.
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65337" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65336">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L4Yi8CJqad9BIa7r3bmt2kGSp8IB-Ll_no2Ex-IKIlF8hL082n2KbiGI0T5jfiNjv3wJuPU5W6LHunTCYTJdCHJ_IjMTdkn03_StIP-IeQA3zS_DBhX34AI-VHitHst1EO8-uhj3BMXbLT6VTKYhOoVmnz-N6rIidQ_JGvwDJZrwxpopj8Oc5HyiMHWsYSQy5ocp2OKp0BB2qPhjxfvouU0iRIEP5T4jyaJvuNrR3CiGzTALdjYnMaDpaH4M1BAqtdGVi50drPkU3PwxjIchWYVLUCqh76fd1CLmMMS8nVcfJkkSACklwT1W5caxbQYzSQrsIrf3tVS10shFhzO-Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
بیانیه فرماندهی مرکزی ایالات متحده(سنتکام) درباره اتفاقات و درگیری‌های دیشب:
چند لحظه پیش، نیروهای سنتکام چهار پهپاد حمله یک‌طرفه ایرانی که به سمت تنگه هرمز پرتاب شده بودند را سرنگون کردند. پهپادهای حمله‌ای تهدیدی فوری برای ترافیک دریایی منطقه ایجاد کرده بودند. نیروهای ایالات متحده پس از آن برای دفاع در برابر حملات بیشتر، سایت‌های راداری نظارتی ساحلی ایران در خارک و در جزیره قشم را هدف قرار دادند.
نیروهای آمریکایی همچنان هوشیار هستند و برای پاسخ به تهاجم بی‌دلیل ایران در دفاع از خود آماده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65336" target="_blank">📅 11:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65335">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLCEleOToGKV_BDQHbfwa22pudP1LxBRstlZtUwIVmUvXpd1Tu9lwDC9RS19kTSKqk0NrZK09DP4i9QiIMd_8m1tXGZ2C9FwOF8eizX9Wn2BBaBjL-jfEVohhnijAMpF7zb8V46bGWxGuGMsQc3SSu-wtaevIn5He9T80VlMO-gUL8crqEgnpWAI5xHBazlArdypfCet9sDBe9Cj_wfZ8OVkS-TqPbhhj6lbENvqEpgzd87w2gAxuvs2614b5hvfuYHmTk8arlyIa3-RBKzhfUnb3pq0WeqNCDTq2645MO_8pYsCoq_2KiU9wm9iUk6LSChz5zYat47EFVcFWkRM-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم خمینی در سال ۱۴۰۴ Vs مراسم خمینی در سال ۱۴۰۵
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65335" target="_blank">📅 10:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65334">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887b98bc21.mp4?token=mq_9pwGwbO92I2DotbxBrnBj8ItjeEjgvx72MvlEfIQVr8GpckWGg692kO04oVucb9GaG0Bi7JQBpP_ZwJgndGzgQiWCbC5OwZhzE88TTd-HDrHEglUr25QSvNcZcJF-AUjwWyousUPdN40YA95KmgWBkwsc5ZA6SXq4FgFKT0IKoLfv4y_moRigKd1Pd4V7LwZHb0FuLgngGzX1eCmKoTmAegNhIFyRQKeObGCB1tA595evb33BUrE2-EHuTDmUiglyxverv_G5o3LxcaPj8m1vbF7epHP-FdOgwv5134g0V8KhiyI3I39ACFF0hAhucOOR39aHazLeRCT-Kzh_VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887b98bc21.mp4?token=mq_9pwGwbO92I2DotbxBrnBj8ItjeEjgvx72MvlEfIQVr8GpckWGg692kO04oVucb9GaG0Bi7JQBpP_ZwJgndGzgQiWCbC5OwZhzE88TTd-HDrHEglUr25QSvNcZcJF-AUjwWyousUPdN40YA95KmgWBkwsc5ZA6SXq4FgFKT0IKoLfv4y_moRigKd1Pd4V7LwZHb0FuLgngGzX1eCmKoTmAegNhIFyRQKeObGCB1tA595evb33BUrE2-EHuTDmUiglyxverv_G5o3LxcaPj8m1vbF7epHP-FdOgwv5134g0V8KhiyI3I39ACFF0hAhucOOR39aHazLeRCT-Kzh_VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: ایران با آمریکا به توافق نرسیده است چون رهبرانش «قوی» و «مغرور» هستند اما «آنها چاره‌ای ندارند.»
کمی زمان می‌برد. شما درباره ۴۷ سال فرار از هر کاری که می‌خواستند صحبت می‌کنید.
یعنی، این باید مدت‌ها پیش انجام می‌شد. این باید توسط رؤسای جمهور دیگر یا کشورهای دیگر انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65334" target="_blank">📅 09:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65333">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65333" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65332">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=Dbw7iHrqsd8RBJpET48xfIyfaZl8Y9b1jW8oKeyFTbgdohltmFKeIgW7JPmLp5FQaJyt7gFqw5FABk3WgEM_zODTtjC_dX6Zeatogt9FGcWSw3rD9SzpLSF6u2v-xYSSQa8TJq6qcOWXWQEjOYyWbSLrfFLsz3N2TJ49vJg3nbAtSokKS-YaYjxuWnCysp13LVq2et0a0pQ0Nn0WKe-SLSVBUhHixJo9iNBTQuwnLVyzN6avseppuBQXQ83EwzHmqvOtCzg6EoJOD24ncoq9L_NoIFQs5kdquRfUqo9mdBbtxL5XMiKrI4odN273l-7-qmNr0pMspC6YN16_74AEDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=Dbw7iHrqsd8RBJpET48xfIyfaZl8Y9b1jW8oKeyFTbgdohltmFKeIgW7JPmLp5FQaJyt7gFqw5FABk3WgEM_zODTtjC_dX6Zeatogt9FGcWSw3rD9SzpLSF6u2v-xYSSQa8TJq6qcOWXWQEjOYyWbSLrfFLsz3N2TJ49vJg3nbAtSokKS-YaYjxuWnCysp13LVq2et0a0pQ0Nn0WKe-SLSVBUhHixJo9iNBTQuwnLVyzN6avseppuBQXQ83EwzHmqvOtCzg6EoJOD24ncoq9L_NoIFQs5kdquRfUqo9mdBbtxL5XMiKrI4odN273l-7-qmNr0pMspC6YN16_74AEDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
🎯
همین حالا عضو شو و شروع کن
👇
e15
https://t.me/+6ckCmywafrxiYzk0
https://t.me/+6ckCmywafrxiYzk0</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65332" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65331">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgiPGw21D98Lzu5hco4JT5iX6nv4e4HRcGAT4Xc8zTLYBFsH1sVeH0vGZLE3AHnYuNsiPz0r4lBwPJJAgiTksdYSAmBIz5R4HwLeSu7dqegY4hb5jgizLxSjS6i0XEKHHW8UzMz0cHkGBsMEmGCRAwFrGky7qJZGs61KeLeAzggo6HsgPwxva-KIf5OdEZgv1x5Vjhnymtu0RN8y9k-dZ3zi-Q3exXKzfvXor59vnakPHyhlssy1Tt2E2Fi8yDoKmHDsYjIjyiPXP36Obe7cMSV-06qskSCq9xI_eILesX-Rref_ftEbUGgcx0voP-2_hUGLkQ0-jhwrs2d-funtAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برزیل
🇧🇷
-
🇪🇬
مصر
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
بامداد یکشنبه ساعت ۰۱:۳۰
🏟
ورزشگاه کلیولند براونز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
برزیل در
۱۰
دیدار اخیر خود،
شش
برد و
یک
تساوی کسب کرده و در
سه
بازی شکست خورده است.
✅
مصر در
۱۰
دیدار اخیر خود،
پنج
برد و
چهار
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر برزیل
۳.۴
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر مصر
۱
.
۹
گل در هر بازی بوده
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب :
۱.۱۹
🧠
اگر مجبور به پنهان‌کاری شدید، مسیر اشتباه است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65331" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65330">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇺🇸
ترامپ:
ما خیلی سریع از ایران خارج خواهیم شد، و این خروج به هر شکلی که باشد، چه به صورت یک توافقنامه و چه به روش بسیار سخت، بسیار قوی خواهد بود. روش بسیار سخت شاید آسان‌تر باشد.
اما ما خارج خواهیم شد، و قیمت کودهای شما به شدت کاهش خواهد یافت، درست مانند چهار ماه پیش. قیمت کودهای شما کاهش یافته است.
انرژی، نفت و گاز شما همگی به شدت کاهش خواهند یافت. و صادقانه بگویم، فکر می‌کردم قیمت‌ها خیلی بالاتر برود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65330" target="_blank">📅 00:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65329">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
🇺🇸
ترامپ:  ما یک سلاح هسته‌ای را از بین بردیم. این قرار بود کشوری توانمند باشد که حضور هسته‌ای داشته باشد. ما تا حد زیادی این کار را تمام کرده‌ایم. به هر طریقی، این کار تمام شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65329" target="_blank">📅 00:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65328">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdccc3a3f6.mp4?token=KpEydD-cmyupTErtXiXGHfTvbPZSVrlvDd6JhNYCY8W-OttafmUQiTmsDavUzawC3IAexlY5nvNgSYSCGrqJBrOZG7wA5BwGopRgWIHlAQpjJ_MHHVZfdkbhTS1BaQS9XA8pEZQqL-TV7lbTxs0EgttqLnbAw1PPNQYWUeeYkdYc37HpWQ4rsejtU05m60VdEk1LbtxnD-Hzav_Qr0_jG1fzbzSvJIwnlN3yf5ceNnPaqGAU-2i9hY4sXQg2MWBSHHVapVL3tIxqLiVYL1mTAsWep42uDDWJL3yH3sSiHf42FNW_uZt4N0czKiySKBFM0JiK9V0UXjzk4Cj1nLoB_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdccc3a3f6.mp4?token=KpEydD-cmyupTErtXiXGHfTvbPZSVrlvDd6JhNYCY8W-OttafmUQiTmsDavUzawC3IAexlY5nvNgSYSCGrqJBrOZG7wA5BwGopRgWIHlAQpjJ_MHHVZfdkbhTS1BaQS9XA8pEZQqL-TV7lbTxs0EgttqLnbAw1PPNQYWUeeYkdYc37HpWQ4rsejtU05m60VdEk1LbtxnD-Hzav_Qr0_jG1fzbzSvJIwnlN3yf5ceNnPaqGAU-2i9hY4sXQg2MWBSHHVapVL3tIxqLiVYL1mTAsWep42uDDWJL3yH3sSiHf42FNW_uZt4N0czKiySKBFM0JiK9V0UXjzk4Cj1nLoB_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ:
ما یک سلاح هسته‌ای را از بین بردیم. این قرار بود کشوری توانمند باشد که حضور هسته‌ای داشته باشد.
ما تا حد زیادی این کار را تمام کرده‌ایم. به هر طریقی، این کار تمام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65328" target="_blank">📅 00:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65327">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecba9ea726.mp4?token=R6zTlBYJkCmcvRIcFwUHOhJl49hibTcb2uYqqTbWp2JpDgjVj6IyEqWz4oNWtjxFeLjdcUKyA1YiChdCkHOTqR6JA2TjCx5Ys5UFEEz6BAW1DXwApPwI4lU-7dn59ze3Jdv6fseyLU1olSf30DvcfY5XJcWpsfC3TDkTO23qdRbPI3No41_darT-MtvAHGLyJGP3uFnrqUAFAi0DeIH-ufGv8qDpIaT4O8I0ykj2VwY5V96zE03dIiJ-ViwXhnEoKZi4dj5N53b0qdA_Wgk9ZeyoVmcTQj3z37-P59IQzH0gwCg89QcaAE4vBxaw5iLU3CSBIoUiWLU8cCA6sGQCeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecba9ea726.mp4?token=R6zTlBYJkCmcvRIcFwUHOhJl49hibTcb2uYqqTbWp2JpDgjVj6IyEqWz4oNWtjxFeLjdcUKyA1YiChdCkHOTqR6JA2TjCx5Ys5UFEEz6BAW1DXwApPwI4lU-7dn59ze3Jdv6fseyLU1olSf30DvcfY5XJcWpsfC3TDkTO23qdRbPI3No41_darT-MtvAHGLyJGP3uFnrqUAFAi0DeIH-ufGv8qDpIaT4O8I0ykj2VwY5V96zE03dIiJ-ViwXhnEoKZi4dj5N53b0qdA_Wgk9ZeyoVmcTQj3z37-P59IQzH0gwCg89QcaAE4vBxaw5iLU3CSBIoUiWLU8cCA6sGQCeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
مقدار زیادی نفت وارد کشور ما می‌شود و مقدار زیادی نفت وارد جهان می‌شود که مردم حتی از آن خبر ندارند. و به همین دلیل است که قیمت هر بشکه نفت ۹۷ دلار است نه ۳۰۰ دلار.
وقتی کل این موضوع (ایران) حل شود، نباید زمان زیادی ببرد — به هر حال، این کار انجام خواهد شد.
وقتی همه چیز حل شود، قیمت نفت ممکن است حتی از قبل هم پایین‌تر بیاید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65327" target="_blank">📅 22:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65326">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">«منبع ایرانی: ادعای العربیه مبنی بر موافقت تهران با انتقال ذخایر اورانیوم به کشوری ثالث کذب است
یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایران روز جمعه گزارش یک رسانه سعودی مبنی بر موافقت تهران با انتقال بخشی از ذخایر اورانیوم غنی‌شده خود به کشوری ثالث را رد کرد و آن را نادرست خواند.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65326" target="_blank">📅 22:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65323">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v61d4WX91HsA8qanu2vvBbDpY-cmM-6-mPSLA1jkoYgkBzDN6ETt-Le8eobyXkQSY6Q52BwYRvIT0PEtT_u98kAynDEqO0wujg8nklDKNCYkwTZC5Dtfga1G30jqvfVVS9oTj7XXS6ThcAan4fLXgS6Ytlw_jT4YLjbAAalPaN-K1Q_aMC3BtKFpio7yMlXZUqQVqnIU5bmjIeIJyJ-YtOCGftLvvu8zO1zz5UfDfHLX9aqkTBdMV1dGLquJWDcHOkoZBiEpMBEHlmattmrkoQ8GercR5fTVXUWEGUROtahujuFhUb81TkZ4WGJbwJmOTAI5ziH13CVE6G6HM5aUag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
صحبت‌های جوزف عون، رئیس جمهور لبنان بر علیه نعیم قاسم، حزب‌الله، ایران، اسرائیل و امریکا:
به نعیم قاسم(دبیرکل حزب‌الله) می‌گویم مردم لبنان، مردم شما نیستند. شما نماینده مردم لبنان نیستید. مردم لبنان از جنگ بین اسرائیل و حزب الله به ستوه آمده‌اند. دشمنی بین اسرائیل و لبنان باید یک بار برای همیشه پایان یابد!
ایران لبنان را به عنوان اهرم چانه‌زنی در مذاکرات خود با ایالات متحده استفاده می‌کند. این غیرقابل قبول است.
حزب‌ الله باید بفهمد که راه دیگری جز نشستن و گفتگو وجود ندارد. هیچ راه دیگری برای حل این مشکل و نجات آنچه باقی مانده نیست، جز از طریق مذاکره و دیپلماسی.
خطاب به اسرائیل، از جنگ از سال ۱۹۴۸ خسته نشده‌اید؟ واقعاً می‌ خواهید در صلح زندگی کنید؟ بیایید بنشینیم و صحبت کنیم
ما آماده‌ایم. ما مایل هستیم. ما متعهدیم. آیا شما هستید؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65323" target="_blank">📅 21:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65322">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwpbcgoS21sGasqCFWEPAS1r_wwYz77t0pKJOM5FJDG7aT-3hMW3pNielLa35pyk2rQVgq7sWxYttpYOzLa9MXoUEy0i-mf-lj8ABXFC_qgQ0xcnDczng1DF6wuiqbysSIj1X574_atc1NnTXTZUmcicqDYTJF3t7ZSIUuAOXeF3KQnnD2gCCa_ZvByCsNEuTFUptVsGRMOX17qumNOgvyxbxnZ8Hf1mU177xNFkg5u0V4aOUYWrMP19_FbYKSI-iGsk278dtr5Vs67Evs-rwmT_GKgZD6iyMxu32jiXhEgrvbubqQ7DMIn9Tr4EREtStPbKGrbc3JT2z4qSDAY0yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پلی مارکت: صادرات نفت ایران به کمترین حد خودش در ۶ سال اخیر رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65322" target="_blank">📅 20:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65321">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=UrHdjIFFA6qFY9ydTaPHFXlw-dM5rFeEniQEiMDfcvpBD0imXv6ZvOabREeQj816MLoMUTPxa_X5fShhvHvxxp8i6EVAIya1dg8TvI7N4qnsGebEUpx2DiZUCoHKzZ5Iz8AX2Kv-L0n4EIzzXEpOdMzszQ05DKpf0QCwLK9SKWWqIXE8LZQ69lGqk6t2Gv0VFyjxQ_Zkl50rHwpr_YjrlXZnaXqlsrB5lB7PuxLtVTG-yQWUzrY-sO5gS-grCeEkifOs5uNHO3Nx5SVaagLyCsMsHV58LDsUftoheuz3YInhWZFXbrfP2164reNZ828mQ8O6jlbKJEShVgvemmi8VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=UrHdjIFFA6qFY9ydTaPHFXlw-dM5rFeEniQEiMDfcvpBD0imXv6ZvOabREeQj816MLoMUTPxa_X5fShhvHvxxp8i6EVAIya1dg8TvI7N4qnsGebEUpx2DiZUCoHKzZ5Iz8AX2Kv-L0n4EIzzXEpOdMzszQ05DKpf0QCwLK9SKWWqIXE8LZQ69lGqk6t2Gv0VFyjxQ_Zkl50rHwpr_YjrlXZnaXqlsrB5lB7PuxLtVTG-yQWUzrY-sO5gS-grCeEkifOs5uNHO3Nx5SVaagLyCsMsHV58LDsUftoheuz3YInhWZFXbrfP2164reNZ828mQ8O6jlbKJEShVgvemmi8VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ثابتی: قالیباف تو مذاکرات اختیارات تام نداره و پیشنهاد پزشکیان بوده. تو مذاکرات اسلام‌آباد اشتباهاتی خلاف خط قرمز رهبری شکل گرفته که باعث شده هیئت تذکر بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65321" target="_blank">📅 20:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65319">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=QSqGZIfooz-rH8C-7DnN3-sFDiJXYyXzp8BUDuL7GDVYeNCLxJhnwYIIZWodfqLO5cqrM1Mm5Dn1_oalsY4AFLlIdOJtVs4MU7qelyWRApqH7_NeaDIgKPUO3cBdwAVN_5tfZq_Hju6xW2BKJlnIzetYw_LAoP7BiYu6ipA7gh0alUqN4p5-l8I_bQdwemBycGEhw6QDVzvLNljAu3zuCmQss-_Ns09qT8H3sdF6Eka7xIYBiBFGr-UOoxU5XUCOqQ5-LI8gOd_dzhor_2euAovufghDJvy8YTDODlJXQmBZwP0MeDsW5jUfk0XNObuI3heJ0ZJlX7v3Vv0q9beBzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=QSqGZIfooz-rH8C-7DnN3-sFDiJXYyXzp8BUDuL7GDVYeNCLxJhnwYIIZWodfqLO5cqrM1Mm5Dn1_oalsY4AFLlIdOJtVs4MU7qelyWRApqH7_NeaDIgKPUO3cBdwAVN_5tfZq_Hju6xW2BKJlnIzetYw_LAoP7BiYu6ipA7gh0alUqN4p5-l8I_bQdwemBycGEhw6QDVzvLNljAu3zuCmQss-_Ns09qT8H3sdF6Eka7xIYBiBFGr-UOoxU5XUCOqQ5-LI8gOd_dzhor_2euAovufghDJvy8YTDODlJXQmBZwP0MeDsW5jUfk0XNObuI3heJ0ZJlX7v3Vv0q9beBzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شهروند کفن‌پوش اصفهانی خطاب به مسئولان: من رو با همین لباس ببرین توی دولت قول میدم همه مشکلات رو حل میکنم؛ تورم، گرونی، همه رو حل می‌کنم
از پزشکیان هم میخوام حمایتم کنه مگه خودش نگفت هر کی میتونه مشکلاتو حل کنه بیاد؟ تو رو خدا اجازه بدین من بیام.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65319" target="_blank">📅 17:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65315">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MuxbGv8dOe_Rvrqa9G7vGTuj8YOlCkGLAi7N94E314M51VAjiy74n8W-nYsE2TVnLuz5iRJsDrMCTs71Kanntdgy8rLMuoM7M5BZBWLTvvfFG0M1yNlc6ZxDoKWUB1U_s22EspZNHM69CFzSp5Wi3Vxf6rWrg-4n3p8dv__UTBHbaareI6HhegC0SYf5ZBKtEUN1jN-D_vpzcpTSIqKtNZN3P-e0LQrbEyN21CTpFSjCtPtSY3mRoNRk0xPUBXwgIIv8zUbcWIu4_Jalbw2bL-dNZM2Bc8zfsQW9wkMECz3NJCCc1yAZoYil22EG1aYWroV3Dxeuk8myK6QcV54pWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Dl-1pq8oLuooHLd2YBoXyxDCfbmIuW3qjO9F1v-6wnVvtjBG4OjCF-ur-oSA5JCAeIe8w0MoeSFfFBo-XWIpvMxU9VeLczNvMqWAqC_Bctf3w0n6TXnwHgMjBv3bvPyD03rsWbOad3Sd52o4fOompWvlT69mWIxVhT_RPJ5ZZf3gsAo7KW90kagnnfwMLLSV9vTMj83XCZi7wwbPdSM3RxdD9qjsponryl-jSYTz7Cg4RbHw9DUHnz9iIcJTHjaS6ZvwI3paoUZuGwudymRW51ItOUQd5QHMUWvLpplF1t5mzdfGOZNghxW77c1nWVae3Ffbj6g0vaxTOcYN6DJAPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JL_vC1v9ZAh05MiIfJJogTm-YBCfxth-I9zFJOC-hwwjihbRHp8AlPzKOUXZONljhvUwf2kex6QxFo0SVfJ0LBWDfBg10m3TjjRXLFW9KGf1SNuUi9lGKhZNEhCIIxkcLtBNuEh2LCjDLFgVTnUHsQO3WfMJneFFZLsjhjol_yEsWYp3F7DaY8jWmuz1CgmIovNr8i7EFsGBTXH1UnFE-vbISTHr_vXE4GwP0lWZxxjkkfUHrZuSSjDUP43WPsNBAbH5yAg2tXGNzAAhVQgL83XD9oPsUxhLfxoe31zVK1zU7bajQBvvXii8Jgxj5G1myBTj9O0_WAp5PWyMjgLakA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
فرماندهی-اقیانوس آرام ایالات متحده (INDOPACOM) اعلام کرد که یک کشتی بی‌تابعیت تحریم‌شده متعلق به ناوگان سایه ایران را توقیف کرده است
در طول شب، نیروهای ایالات متحده عملیات بازدارندگی دریایی و حق بازدید و سوار شدن به کشتی تحریم‌شده بی‌تابعیت MT DAVINA را در اقیانوس هند در منطقه مسئولیت INDOPACOM انجام دادند.
ما ادامه اجرای جهانی دریایی برای مختل کردن شبکه‌های غیرقانونی و بازداشت کشتی‌هایی که حمایت مادی به ایران ارائه می‌دهند، هر کجا که عملیات کنند، را ادامه خواهیم داد.
آب‌های بین‌المللی نمی‌توانند به عنوان سپری برای بازیگران تحریم‌شده استفاده شوند. وزارت جنگ ادامه خواهد داد تا عملیات غیرقانونی و کشتی‌های آن‌ها را در حوزه دریایی از آزادی مانور محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65315" target="_blank">📅 16:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65314">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYJs8VIdQfU1lANMDjaCk3WzB0oJy8P5Uvc04e1yAXukDdk8CsOMGGC0vYgkOH_ajEQtClp_rHSQTl33C6lPgUxS0N5_W5van0iVxAk_0XZUlTrH1GCqHGhqBpPr_7RVYdqkDhMpTX6P57YHt9YtgkZKzS8hX5pWRa-uCz2C0WXIXH-JNY0iA44cEaU1dnxPPsWlN3xYi48On0-HDG8PhJSnvoRCqnnkzEudfRm14G2o0US__pAChOawWF7brpzVsW2GqoVU7UtaQ5mIXOhZ1vjLcg6SPYon4VGCJTz4WsxCOZTnRs1ccpQU7-_07r1QkGxyAHDjUquogXhJcCTZnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
خبرگزاری العربیه : ایران رسما به پاکستان اعلام کرده که با انتقال بخشی از ذخایر اورانیوم غنی شده به یک کشور ثالث که مورد توافق هر دو طرف (ایران و آمریکا) باشد موافقت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65314" target="_blank">📅 15:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65313">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=lM0rCb0QraGv5jSnDDOkvFlYegTpCWTKqPpi0r22RkixT82f7HSRwbk-qJLf5YHL865ktO0C3FDKUrXGzD3pRPyeP0Hx4MH28fJctWRvobdPqMN0Z2SybskVB-SI5Kz-FkZQtXB3kP_DkpHf6psXxCLx4kf9OqMw6iDoZWtedlmNeae29Vs1e_QcF6fhDZlgFojquRqYopqSy0cSrTuxHwFabqBHEfeklxkiIDUKDssH8n-TTEdVEw3hwsQoqAuRU1Kx7FGS4u1FDM6BNUhALt2E1562ngJVfc9YBlRdmtplTKpk_wp-s64Hz4rgmVRGEqCA3T7vTc-tkILNZT0PKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=lM0rCb0QraGv5jSnDDOkvFlYegTpCWTKqPpi0r22RkixT82f7HSRwbk-qJLf5YHL865ktO0C3FDKUrXGzD3pRPyeP0Hx4MH28fJctWRvobdPqMN0Z2SybskVB-SI5Kz-FkZQtXB3kP_DkpHf6psXxCLx4kf9OqMw6iDoZWtedlmNeae29Vs1e_QcF6fhDZlgFojquRqYopqSy0cSrTuxHwFabqBHEfeklxkiIDUKDssH8n-TTEdVEw3hwsQoqAuRU1Kx7FGS4u1FDM6BNUhALt2E1562ngJVfc9YBlRdmtplTKpk_wp-s64Hz4rgmVRGEqCA3T7vTc-tkILNZT0PKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیصر خواننده لس‌انجلسی برای خوشحالی عرزشی‌ها پیک میبره بالا
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65313" target="_blank">📅 14:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65312">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/js7yW7Dcx0QDf79n8QO93ngzmZZRrxixCq7elfKvoAVnkJRDa6m5FrGl2RZ3adiFSlIjpX6eQETDzLCQFfq-DQ0pHMePWR5ofg-wUZGccnG1QyNcpZLBEJG2zoelE_IuLgwX-1l29dtDJp908D0kYXUZkXmUjTllNhkJdWT0pt0nTRKxf2pKzOPxdbt1eLss8rW94P1tNjbkkkTR2tpQCUaEAMbXF_JH3n1OM8g0TE4NLFNG7AVUSbLZ0tkD116tXe2ZhLtlw5eskPKXJo8RF7ucsy_iUUHwN5csHCEGvfJy16J45fvfdsfjq60zO-UoysuabN-zbO4Tyon8LqAu3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت‌کوین رسما به زیر ۶۲٬۰۰۰ دلار سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65312" target="_blank">📅 13:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65309">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=jPZroGzblhwIU-4MnpUlBkAT5pxHCD0oxAyrR137m2YvcIm9f8OCMRt_JfTAJQ0mVBMCDKJggbxIO86SSd707fBco1qddstrcUamQJNJDti-hs5ZQ9LJeOy052wOBfqOHVe2fcQB5NsA9G5_HsmeU6XFfVc9i1xmD-39hl1o1KQRIlPqFo337yE9MPHLz-hEFQJFCbS2o5NWuX8zwry-4b4I0OQ2moMXmDq5mUoxYEbb1xDYnG9Z7uALixUqbW35POS9jE4hnC0F1AhjNZXcmgjYUc0WVRrvMSUTc0tm1_VYdcFQ5bpKR9dKJEa2kTPUdbmNYVpy8rLW-GAvTXs3fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=jPZroGzblhwIU-4MnpUlBkAT5pxHCD0oxAyrR137m2YvcIm9f8OCMRt_JfTAJQ0mVBMCDKJggbxIO86SSd707fBco1qddstrcUamQJNJDti-hs5ZQ9LJeOy052wOBfqOHVe2fcQB5NsA9G5_HsmeU6XFfVc9i1xmD-39hl1o1KQRIlPqFo337yE9MPHLz-hEFQJFCbS2o5NWuX8zwry-4b4I0OQ2moMXmDq5mUoxYEbb1xDYnG9Z7uALixUqbW35POS9jE4hnC0F1AhjNZXcmgjYUc0WVRrvMSUTc0tm1_VYdcFQ5bpKR9dKJEa2kTPUdbmNYVpy8rLW-GAvTXs3fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مداحی محمدرضا هلالی مداح حکومتی با زبان چینی برای عید غدیر!!!
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65309" target="_blank">📅 13:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65308">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=FedcA6exNdoU5AH-xSBWltAEVToFLei1Vf0lMRpUlUpq8UimAseJ3d614XgpiM8IFyPo8O5ZH2F-CwogsXVFydchi82MUIpFf49GV3Sj16MEFwsomwKHrzEloEBTsiPRLuMl01ZaMD9TNBNPAWDnqWe4Owa_IhzJnn5rD-7A7b_oWHS9yQSTYYbVSVko0gbetTyOxWgA6UcVjqaN0o4XjY2OwPgokEre-VFZHrgkPHjXI52jpJy6bP6jpz47nc8_JwXYBUXx2ZEAjnQwYgVYt1fE-lqTwlh2_Dnm6CMYMJnlOhaxXwJgEr90TJqZ8i0qxTGEZAZtvhoPsDv85TqGGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=FedcA6exNdoU5AH-xSBWltAEVToFLei1Vf0lMRpUlUpq8UimAseJ3d614XgpiM8IFyPo8O5ZH2F-CwogsXVFydchi82MUIpFf49GV3Sj16MEFwsomwKHrzEloEBTsiPRLuMl01ZaMD9TNBNPAWDnqWe4Owa_IhzJnn5rD-7A7b_oWHS9yQSTYYbVSVko0gbetTyOxWgA6UcVjqaN0o4XjY2OwPgokEre-VFZHrgkPHjXI52jpJy6bP6jpz47nc8_JwXYBUXx2ZEAjnQwYgVYt1fE-lqTwlh2_Dnm6CMYMJnlOhaxXwJgEr90TJqZ8i0qxTGEZAZtvhoPsDv85TqGGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: عملیات خشم حماسی پدر، همسر و فرزند مجتبی خامنه‌ای را کشت.
🇺🇸
ترامپ: من فرد مورد علاقه او نیستم، اما احتمالاً او یک حرفه‌ای هست
در برخی زمینه‌ها آوازه خوبی داره، برخی‌ ازش بد میگن اما خب درباره من هم بد میگن!
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65308" target="_blank">📅 09:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65307">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پرسرعت وصله
👌
👌</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65307" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65306">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.2.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/news_hut/65306" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
بهترین فیلترشکن حال حاضر ایران
👉
💎
با همه نت ها پرسرعت کار میکنه بدون محدودیت
💎
👌
پیشنهاد ما دانلود این فیلترشکنه
🔧
لینک دانلود داخلی با نت ملی با سرعت بالا
👇
https://uploadb.com/plx39j7b72sy/Barko__v2.2.apk.html</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65306" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65305">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=YI0wnFeKyDzbQxo8xG5PnzOPGTtBN37-s1mZ72AQpUXHoPKb6muJBYmFxeH8Jb4plLZOG37ErQpBshXDpAONgbR8zyS-2Vp-a2qeKJ6T15J53dho4kTKoIy4CkwY1cdrNExHJdUlKiC2tNndFTV_5YXiRVzcrRGyLhLkmAy3N7p8yxxQs2xsqr18QaZwtI6eW3dYviXvhOCe89tlSS1D4LixxnyQgvulKB4-SZ1h3PicymZWhirWJnB2IOy0i5NRHH-oIg9kMwRQTBJruJCI93vXp22seLx9fvicIueTBbkcyF85bfi_OTpeWM_Tn474ue82V8EZVVXSlPKbwK1UcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=YI0wnFeKyDzbQxo8xG5PnzOPGTtBN37-s1mZ72AQpUXHoPKb6muJBYmFxeH8Jb4plLZOG37ErQpBshXDpAONgbR8zyS-2Vp-a2qeKJ6T15J53dho4kTKoIy4CkwY1cdrNExHJdUlKiC2tNndFTV_5YXiRVzcrRGyLhLkmAy3N7p8yxxQs2xsqr18QaZwtI6eW3dYviXvhOCe89tlSS1D4LixxnyQgvulKB4-SZ1h3PicymZWhirWJnB2IOy0i5NRHH-oIg9kMwRQTBJruJCI93vXp22seLx9fvicIueTBbkcyF85bfi_OTpeWM_Tn474ue82V8EZVVXSlPKbwK1UcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم. من محترمانه رفتار می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65305" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65304">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=oC_76TmCbO3sKbcOEe9qRpChptqjQBaMWoyXqZEYA9WCbHjEoSMzJOmEuT6CbPMl_F85rfJiojTO6YSHPE2eTSus1MW59ynobqDrCbayZT5AGKah8OAwpGoMuoZD2J89VNjiBdUusHJ3sywr-5_srOev01JUu8hWKCkVIDyTSP_mKMB-33gF7tw13ysheZQtZ90EzjA2Y-bzFm0a0rwVytLEfxhJ3KGwi2VDPu49CbqqYjPHkX8q4-o1kV--MJsYkIp2i12Fu-5B5veKMpYOfiLQmJ8YDNHVFYZOWADjcLPYbn1i4QfjKQWy3_QNKssxTI3iB6rRUOC_mpO7V7fu_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=oC_76TmCbO3sKbcOEe9qRpChptqjQBaMWoyXqZEYA9WCbHjEoSMzJOmEuT6CbPMl_F85rfJiojTO6YSHPE2eTSus1MW59ynobqDrCbayZT5AGKah8OAwpGoMuoZD2J89VNjiBdUusHJ3sywr-5_srOev01JUu8hWKCkVIDyTSP_mKMB-33gF7tw13ysheZQtZ90EzjA2Y-bzFm0a0rwVytLEfxhJ3KGwi2VDPu49CbqqYjPHkX8q4-o1kV--MJsYkIp2i12Fu-5B5veKMpYOfiLQmJ8YDNHVFYZOWADjcLPYbn1i4QfjKQWy3_QNKssxTI3iB6rRUOC_mpO7V7fu_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره ایران: تمام ۱۵۹ کشتی آن‌ها در کف اقیانوس قرار دارند. ما در واقع از آن‌ها در آنجا عکس گرفتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65304" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65303">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=mo-xJWH-G3j_N8Slbv2PjcFYZjbweCz2yaKKs1MV53b9tUgTUIhJBB6YnlMZ3SZ7HSftJRs65i9isxBmWgZO4clZ3Z-tehY0cwn28ZvnPFALCSyZ5cVmUj35caRuWHP6p2EFTfzo5vW0Q7yFekuVekBtLrNWIEuol8KWuWFvyupif7VtTYKUUKRhOsuvmjiX9Q6VNdJOTNL3zg0OuyAzPdxBPnPDdsQV8KNhdI9f8OaO0C6Z8rvZJ4JbSjqefcO9gm4RXw6mxf8NpngjGRDjTvzAISJnQR6ukYYZ6L3pIcYasf8J39A5A05oq6OBndBB_MRuA6TltCJ1Big5ysqmZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=mo-xJWH-G3j_N8Slbv2PjcFYZjbweCz2yaKKs1MV53b9tUgTUIhJBB6YnlMZ3SZ7HSftJRs65i9isxBmWgZO4clZ3Z-tehY0cwn28ZvnPFALCSyZ5cVmUj35caRuWHP6p2EFTfzo5vW0Q7yFekuVekBtLrNWIEuol8KWuWFvyupif7VtTYKUUKRhOsuvmjiX9Q6VNdJOTNL3zg0OuyAzPdxBPnPDdsQV8KNhdI9f8OaO0C6Z8rvZJ4JbSjqefcO9gm4RXw6mxf8NpngjGRDjTvzAISJnQR6ukYYZ6L3pIcYasf8J39A5A05oq6OBndBB_MRuA6TltCJ1Big5ysqmZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: حزب‌الله هیچ چیزی را رد نکرد. آنها با ما تماس گرفتند و گفتند، «چطور است که متوقف شویم؟»
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65303" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65302">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=JVHVJ-uj_tLFe1lcrLT0D8VA4xG1zMWmHAucdIcsGGjBmsr4os0nnVJdqGpLnk3MsNXOzKfylEwOd7sbq2xGLDuxkNTE3XDMm-p6wvitcGRF84N61yiLokSTBBhycx97suWQx8mpHeWLMmAWBZv9rCZyPBKwmFnmuHyQYmD-rLE_UST-Iv9l3pzyhzbTm0ET8B9PvB9kmvCjpqsT836pYYmm5TnN_q8EOE_dBKjko8EZpRsybsEZWdjl8bV7XU4xYgq9X2zOFNEdOGsebsUtoUAPvcOoTtFJoZcL5W4qZuZoswXf69-kUqPcyXi-KPm37KQ_D-d7AZwTDfX8G7rkrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=JVHVJ-uj_tLFe1lcrLT0D8VA4xG1zMWmHAucdIcsGGjBmsr4os0nnVJdqGpLnk3MsNXOzKfylEwOd7sbq2xGLDuxkNTE3XDMm-p6wvitcGRF84N61yiLokSTBBhycx97suWQx8mpHeWLMmAWBZv9rCZyPBKwmFnmuHyQYmD-rLE_UST-Iv9l3pzyhzbTm0ET8B9PvB9kmvCjpqsT836pYYmm5TnN_q8EOE_dBKjko8EZpRsybsEZWdjl8bV7XU4xYgq9X2zOFNEdOGsebsUtoUAPvcOoTtFJoZcL5W4qZuZoswXf69-kUqPcyXi-KPm37KQ_D-d7AZwTDfX8G7rkrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من تا الان به هشت جنگ پایان دادم و به‌زودی یه جنگ نهم هم تموم میشه
شاید حتی بشه دهمین جنگ. فکر نمی‌کنم هیچ رئیس‌جمهوری تا حالا حتی یه جنگ رو هم تموم کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65302" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65301">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQyOYYob1XfoaARrj7bvkfWOxdJgpLz89o-fqGff06Gp7aVlPrac_bW2u9INSSLYFNNw2apy-lFcB2-gOVQCy1AP6T8TWDDGAoyHsJ3uXoCo3-BUsLAh9gtGkJeb8Ud_SjLx9vfkNjcpTYlL7pZgUmbv30cH_HgR0XIvYt4M0LSiEVP_qtJRhkxj3P83StTxf4mK6ZBkQf61Jwh4eBMpE3bn3TatZkYUNRxrRkYQisybg-tjVbcFNLdlO6l106jj8U1VjMMREXNbIiHUppbZdwO7pv-pfvIwfe3nStZR_vMrab7ieyPKiRUmSrGp8LzMQRzo2vLsofDo4cuskX5zGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورم نقطه به نقطه سالانه برخی اقلام اعلامی مرکز آمار: از ۴۳٠ درصد تا ۱٠٠ درصد
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65301" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65300">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hkpyx92WlgP131n_BK3xdMMRryyScLtyYlVMfEq1a8TepqdRBqecZDkX6sU1mVbUSeA6eohnIQL9rYl0EG1VWGIkjVicgBwj2HzVzvkEFkQkZRV009eKrIKpTBFxYY24RGQilEOaV6049qerDMp9Y3WqAImuuonfLKlyerH5HUj4Y_7W2JNxZ5p779_17eTwXOE275JLTlO9WzIjLkYMWBCjLYO2UdPDaLezp-V8gmoz1mCMe3gInDb2uYm--ju2E_ZYvlzlIH3EVsFJD8uyN1Tb7uu1P8JJFBYDIdULHIuw1nnfohXlu4fBi5szynjLTPWc-stolaut7p7YAdxbZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇨🇱
شیلی
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
شنبه ساعت ۲۱:۱۵
🏟
ورزشگاه ملی لیسبون
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در ۱۰ دیدار اخیر خود، شش برد و سه تساوی کسب کرده و در یک بازی شکست خورده است.
✅
شیلی در ۱۰ دیدار اخیر خود، چهار برد و دو تساوی کسب کرده و در چهار بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پرتغال  ۳.۶ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر شیلی  ۲.۵ گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: نتیجه مسابقه: پرتغال - ضریب: ۱.۲۰
🧠
پیش‌بینی آگاهانه، تمرین شناخت خود است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65300" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65299">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Da6WKr5ujcX2N5HCNPjO3izvQgJOPuVyTqTfQBvIqhabeQ2t8lAM2LiKBLjB_alPxMbMpMyItrtlNZ8JrUPdiNHqFm-p7_noTAsav1LL0gViOY2admjRRhbIAS-8o1I-bMsWjrL07z0t0gSVDskcWTTb-i8YUZE7rruhVPBJmYlP9JYwkPRVcLM6BJ72sXP9QyWsf7Mnpl9TcRvMvMn-xLrIo56no5uVCpIzOgVkS_A8uTG43DYO4vZY-LTz5YjnqtOdu5hrq6hGS5YdYEkOooSBN1oDOMb4WhGWjoakYOXB6oVZQQ-ZM00JowmvoSSZZOtsJy7-7lSJqpibOeVbJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن های chatgpt، grok و deepseek رفع فیلتر شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65299" target="_blank">📅 22:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65298">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=QTQpreYAOzJ3tSFEIl-BJ-s0EWeKBNKx7OxfKymgH_iOfD5IZ7VbG_G2Ej7BP2sSw7_HXCnn_5taDNM1ghdsbPaelQzTfwYucIOiGEJHRWxV3YjffZctAQ0tEe6kgVMOy3NOl3_2J13sIrqgbFY4YoyB-Mrp-Az2BLEk488MT9hc8ZQgy7bmr_e_jkDBOiwad4QXQ81knt0Af77bVY_zaNep-1JbPYP1S287OoZHRao-XvIou1I0N23DvhbIBn03H4wADLRzzuoZLjnHBcPe1RezsfldqVWcvXkB5WWai0G4eA3_mV8Ozv7il_ilSRVDF2bG_B445jfKQ6hP22qXOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=QTQpreYAOzJ3tSFEIl-BJ-s0EWeKBNKx7OxfKymgH_iOfD5IZ7VbG_G2Ej7BP2sSw7_HXCnn_5taDNM1ghdsbPaelQzTfwYucIOiGEJHRWxV3YjffZctAQ0tEe6kgVMOy3NOl3_2J13sIrqgbFY4YoyB-Mrp-Az2BLEk488MT9hc8ZQgy7bmr_e_jkDBOiwad4QXQ81knt0Af77bVY_zaNep-1JbPYP1S287OoZHRao-XvIou1I0N23DvhbIBn03H4wADLRzzuoZLjnHBcPe1RezsfldqVWcvXkB5WWai0G4eA3_mV8Ozv7il_ilSRVDF2bG_B445jfKQ6hP22qXOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روز اول جنگ مجری صداوسیما حواسش نبود میکروفونش بازه، میگه همه گذاشتن فرار کردن، هیچکس نمونده
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65298" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65297">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65297" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65296">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EU3UEUEHtYzrmo-8ww5KuEoNcBymGuFh9KJkSKaKyamDfi-o3K2seG0EItl_M9wPfcU2GLsjE1lwgdEN09qNGksSInGQ0pDuKRvGhQ0GX0ZhWdwZeBgKLb5xtG-u8IRkYuYqJTDjqSY73u_Ajo3qmj_FzYnaAsFDSaN5Oip9TrtQlKig4N1yUyMH3C62jRf-aq4MzkqElEQ_as2IY4Hx_PrTT2ESAoPuxAUKNxZS_XJiBDCOU3_9dh-dN8fcqz2vCREOf8a8ooM5QT0x_UwdjEwEYJDE-mkhjDdFPVGfij_4_z8YCQSImHB2sqJfJk6ALflUH0BvcYBBjwhjrCEGyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران ، انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
14
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65296" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65295">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ:
ایران موافقت کرده اورانیوم ها تو خاک خودش از بین بره
📌
با این حساب ترامپ از یکی دیگه از خواسته هاش که دریافت اورانیوم توسط آمریکا بوده هم کوتاه اومده
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65295" target="_blank">📅 18:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65294">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyIUn02YDEpN7Qv9OlCxsIngmefEReChxzde3UyrBbRo6736VNV7u8MvtXOnmJGlwgAnzm3iXMC-OeiBbllmZ-qc11p_-9QNZRta_ZlNsWxVozl1nJVnhrX0Di0GEZlJvZuboGLV8hg8YtOQaUuufXsXmEbBNKI6rsFsVRNHPPY-CuHRtowNrOTqE5KVZsTbc2Wxl_XSFHAanvmDWdmLxX4C_sNohbz2ek95knr39jprpYhnBuP42irWPrGp-ZMU-udP8bJWKtu0ox2XY8Hya2RMxN7vfZRhgw2y4eRlg4gsmv82txof40DXhR62Q6DDeqayjFVhEmKlS6CZvLNe7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: ترامپ به طور خصوصی به دستیاراش گفته که در صورت کشته شدن نیروهای آمریکایی توسط تهران، آتش‌بس با ایران رو تموم و جنگ رو شروع کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65294" target="_blank">📅 17:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65293">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkUOV5_zrfgkiB9VX8F5BXX6LdH8k0UVLHsjnb9aKBUgw27hm00YnREnVWGtMmndtsCQ8lmMYCs7De5SdQJXnziQ62cyXPpxXfmMGhtVEI3iCsTMape7LQOFiFcqhLQgT3qGZTU59CVBkUn7lFdjudHiHa_r-DTaVwzxrvUBGCBgdCcVPS8KcV9tJLi9n1ToMiEXRpw0hv_Afw_6ezfBtuXen6W800Cb2XeO7vLq82MxNVZZNfFVmEyzLwucZtFKnHHJjFDuPW6vVJeBI3annIYzN8-AnWbCiCwOPbMODjxnWTvWS7haOGkmIgv0C8u9DxidKf8Ji5dYmf8Pes2mCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65293" target="_blank">📅 16:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65292">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=ligPkncBPHlTd4rqrIx3rKSMXAHXj3OeYI2u0aeaFhqYZie2U33CsTKejVzIaA_hsy7EcwylSdo34-sOcXAq6EHZmyXeoKky5cgPLIgkoAF1Mx4zNCow2QTueFH0oFgk9AbSU5tRh-PXHAG3RLVhhC01Q-ko7XdsJBUetdvqnwlDmqzD8l-fKruuCd3xQk2wGPxpTuJAofBQuxmECW1msncprygInIEj3HJMl4EXSX8dW8CkE9IKdg8_ODQXbx1buVMwHdnGNaU-FicqhisTDGwi1Ab0IP_kfNi7i1tGNko4RYN1-cBYIXsyq9xbvOq3-3wBpJbOO36VECIKQvdPig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=ligPkncBPHlTd4rqrIx3rKSMXAHXj3OeYI2u0aeaFhqYZie2U33CsTKejVzIaA_hsy7EcwylSdo34-sOcXAq6EHZmyXeoKky5cgPLIgkoAF1Mx4zNCow2QTueFH0oFgk9AbSU5tRh-PXHAG3RLVhhC01Q-ko7XdsJBUetdvqnwlDmqzD8l-fKruuCd3xQk2wGPxpTuJAofBQuxmECW1msncprygInIEj3HJMl4EXSX8dW8CkE9IKdg8_ODQXbx1buVMwHdnGNaU-FicqhisTDGwi1Ab0IP_kfNi7i1tGNko4RYN1-cBYIXsyq9xbvOq3-3wBpJbOO36VECIKQvdPig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با اینکه آتش‌بس تو اسرائیل و لبنان اعلام شده امروز جنگنده‌های اسرائیلی اهدافی تو تبنین و حاروف تو جنوب لبنان رو منهدم کردند
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65292" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65291">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=a3zawT4j2dLjpuiGly_ukz0ceqO7KzPwT4uRzFVPM9iVq8j9HEt0gIJNFOnCECD-0Nb50DXQBnP6ND9Kck0_JbJts7FBkI1_hAZK_ES_IYDDxlzr-QC3THQGup_O0h_nj4E7Nmu1bUNaR9rxu0cvaX8GGEo2dU8PWNkN9WOqhIHrd7-iliF4xqGOCZlNzjp7Adf0gSrjulsekLvkD8VunzWli6W5yOwg9qRTkoU7Zp399Pmauqd8cZXYHGz7A8kWFQG-3qlOMdGPnKUChbT9Z0AmeCD6-t3hSsvevBbq6eW4biHWpr207QDWu41OmEgkEtPtNLL9o-JlgY_DzsGDzEstoDwDisZ78ofs2b_qB38R7uuSHGVmDZssqHvzQbEtIdGVc-qNyDJWLpSeBLkRPgk06YQGibHAF0_55bNekq9OL0624AdaGLkNOuO57vpDUrlx1pokpfUOx1NZpoyku3VcC4f2BO7wt7S6Wv0uai_E_q100cYb6G5WEUBMgSR4BuJzkuVFPd51BQ7oZqdVnZtSmIm8OD0ttUAxMne2M_2p1M43ELoBNDynXO7_PzTdIAJvFX7Pd6knC2Ky_JiGjtdYuhwrjPLerQLE6pzEnyRzrkDYLKyElF8BsDPJjfetjflcetNyfVPW0cUOfxXNYqruGE1A3v4OVrXmF678U4o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=a3zawT4j2dLjpuiGly_ukz0ceqO7KzPwT4uRzFVPM9iVq8j9HEt0gIJNFOnCECD-0Nb50DXQBnP6ND9Kck0_JbJts7FBkI1_hAZK_ES_IYDDxlzr-QC3THQGup_O0h_nj4E7Nmu1bUNaR9rxu0cvaX8GGEo2dU8PWNkN9WOqhIHrd7-iliF4xqGOCZlNzjp7Adf0gSrjulsekLvkD8VunzWli6W5yOwg9qRTkoU7Zp399Pmauqd8cZXYHGz7A8kWFQG-3qlOMdGPnKUChbT9Z0AmeCD6-t3hSsvevBbq6eW4biHWpr207QDWu41OmEgkEtPtNLL9o-JlgY_DzsGDzEstoDwDisZ78ofs2b_qB38R7uuSHGVmDZssqHvzQbEtIdGVc-qNyDJWLpSeBLkRPgk06YQGibHAF0_55bNekq9OL0624AdaGLkNOuO57vpDUrlx1pokpfUOx1NZpoyku3VcC4f2BO7wt7S6Wv0uai_E_q100cYb6G5WEUBMgSR4BuJzkuVFPd51BQ7oZqdVnZtSmIm8OD0ttUAxMne2M_2p1M43ELoBNDynXO7_PzTdIAJvFX7Pd6knC2Ky_JiGjtdYuhwrjPLerQLE6pzEnyRzrkDYLKyElF8BsDPJjfetjflcetNyfVPW0cUOfxXNYqruGE1A3v4OVrXmF678U4o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
فیلم جدید و ویرال شده از حمله هوایی آمریکا به پل B1 در کرج
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65291" target="_blank">📅 15:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65290">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/damHXSulTMlFkbuwPKB2HaUsvnxqMCIn1G287KT7rt_QNyFUprpTwZvhjXiAm5An0Dg1Lv399Fe2fITU-CWiBiV3dgwLfmtXvc4vPwNaujENwjX69HN42v_o3eYLZdIT6tHh_sYo3K3nWuFiqflZ6zl12t8MdZ8HeClwJAnXKTD_KS2xN6YMA0laRt3QhbZAKAZVJ-eRHq-mU6_7j_tedbDcCpSWLX9CvZEO3B6xejQyNvLBrIUMjlpOvpwVKLn1lOmafkihp2B0YReM23lBr_aOT3TaMposwkid2_3CDpOTClUNFb4D61DQOBgL7SD9BLvTBKH4yn1bdv5BDLVGvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تو ۲۴ ساعت گذشته بیش از ۲۰۰ میلیارد دلار از ارزش بازار رمز‌ارزها ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65290" target="_blank">📅 14:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65289">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65289" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🔵
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65289" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65288">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65288" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65287">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f7496394.mp4?token=Rkh8zV5kIMbXfaTQi54c7oaUqhxUHDW8DLzMTHNSLFVByTUfxco0UQBjrR7Omo_2-eNpMhra-9thuVWw467BXVaGK8Bn74LFI3Vc57j_Q4_UFBY_ApKBfvfZcpj3oAJFSBZURzAtoUpu1jmB_SIjjE6CAZz1eboVoEW67h0gh3zbzejfwNGAvqDdoS0RLGkjplCamtxup04msXhyCAqvVktniKufu_mTY8o_FPb9s7gP1lgHdOVV5k35UWvqOBFBRWzsRpd8UtHH_w9Acwe8IUYZ8We_XHe8OjloXzKuo1ldYTl0OKZMQnZvPy5c5da4WhIUltBrj-nP6cjKpgcBWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f7496394.mp4?token=Rkh8zV5kIMbXfaTQi54c7oaUqhxUHDW8DLzMTHNSLFVByTUfxco0UQBjrR7Omo_2-eNpMhra-9thuVWw467BXVaGK8Bn74LFI3Vc57j_Q4_UFBY_ApKBfvfZcpj3oAJFSBZURzAtoUpu1jmB_SIjjE6CAZz1eboVoEW67h0gh3zbzejfwNGAvqDdoS0RLGkjplCamtxup04msXhyCAqvVktniKufu_mTY8o_FPb9s7gP1lgHdOVV5k35UWvqOBFBRWzsRpd8UtHH_w9Acwe8IUYZ8We_XHe8OjloXzKuo1ldYTl0OKZMQnZvPy5c5da4WhIUltBrj-nP6cjKpgcBWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئویی آخرالزمانی از بمباران پایگاه چهارم شکاری دزفول در یک فروردین که به تازگی وایرال شده!!
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65287" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65286">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfRb48XX8BMRepEBgM8PiiqFLdy97OwJX4pbfoR93ARxl50bv_K85zm7zMYIvHOlhool3u56ZLj_Jk5H3lUHEJwipg2QZUlVEIGYg4HhSWw7jdqWhYJhSyyCTN5svweparQjGvx_DA4nZZdm20rvH1muyslLFjM_JzHrisghfT8fLNhTLcFARFzKIZUhM2z69INDABYdmXqOnZ4wl23eoh2JOGelX2hlC7vS1VhPGHxXUGFDVyoD_F2qrmKCORx2i1UEI8TjoX99K6Zzf_1s1zw8HW-Eaf9GpH4Lj_gFAGJTPd1UFRL_m8hdWXQEgSo9hRtaznsS9juXIdmYyYkdGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال دن کین، رئیس ستاد ارتش امریکا برای اولین بار به کاراکاس پایتخت ونزوئلا سفر کرد و نشون میده روابط دو کشور بعد از افتتاح سفارت داره بهتر و بهتر میشه
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65286" target="_blank">📅 10:22 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
