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
<img src="https://cdn4.telesco.pe/file/lHjXCm15g_ZmsLKrDgTkaWYaGBNyXs7AkZgnlAReowFgaE8j5-_foP-Zb5nOI2M8kn4_jQT1y_AkoFHK9SSf2l64Sa7T3oa-4V6GjjKJjJ4VcWzteSxTYNwIPvHpJC7iDtf2d951up25tbnbxihuU4uMRS1w-Uhpx4GplZyCUnWuCqUeJ7tFHr21JtF4xh-hhkK6eTWSnJHhXrAJjO-L--4x_13_fsKz2-jRtqZfS6fQ_1DmF9fDEupHC229Ox7Qa3ZX_Z42Xvy_emzrjg-Ihgf3UbbJI9bDy-AmeqL0akYb9dV9hM3-CzNYlBhbSXqO5zTFlrIcNhMJt2NbZL5Rjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 225K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 08:27:04</div>
<hr>

<div class="tg-post" id="msg-65977">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65977" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/65977" target="_blank">📅 01:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65976">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v40moqvDum03zP1sf_FbmkGfu5JVDQ9ccbXCthljkUPkD10MyY7ejKA9Dgkazxh8Th0_hHrgaHk-PGR4iq5GtwAJlbA24Ih3AZokPbGa_H1dkcCBM_HiRgDYrSCM37ioAZKannMGaDebb30jZ8Hng8hx2p9bUaBFyt9CaKPQbwvAuWBVkH0r6ecewES99vz93XVf6fTHg3_Be1vnNRHTD4nB3vP9vAYXE8gDNc7FGtsKfcjQUCTfvgoqnX0tXSJr3BcmJNvQEl7f8XdkSqPy0H5eB4NQTw4aA3CzwgUu1IQLkJdWEmkB62FKXpCMnYAzLSR4wwpiTzSrcQixXK-35Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/65976" target="_blank">📅 01:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65975">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0jP8KhJBZRBxIWgiJCitIPGFLP1A9AO8jynkDDCSVgV8j6QEfrybIKGBqn1MBCRLyrKS8_WqulIOKYADns8JVNTcS4TP56dBz0MgEMYnVQdo6fWrPpqdwJ9oCLmryC-rNaaAYk4qS579jr6LDGo3YecILyhoWeytbj2FvLavakmXv4ESif9FVP2RUqMV5KvwIYSRbpD2o4ATfuxGEMS7KNHI3HHinu8423YBwMbd7CeAt9OkgMFpTb8apXKn1arYacMYYcBMLsCeyla6a4LvFmJ8vFlrHJywmygeI6hOMAJ6OmQbzW4-rf7Zy84HCtclyDSNtWEZK6fJnobXyTDvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تندروها گرفتن رو قالیباف
😂
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/65975" target="_blank">📅 01:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65974">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
سپاه:
کشتی هایی سعی کردند بدون مجوز از تنگه هرمز عبور کنند و مورد هدف قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/65974" target="_blank">📅 01:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65973">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/penif8J2yA6SXYhV4CY5yipu0kA7lOuwbi9NjBgJrKojASl_myC7K3q1GVVsK8yOHJQ8VQVIo6ChSDx6c696ouyI33heVB4LXJe07nKf-qdNN3W7Cr2c8f90ZRFjvnOi_KkqNz13rFq3T5F4hYhaX6__IE6A2AGcl9LaOFUb8y-YdxBwp4T2wvtvQZCGVIt9x6lcmpE3JBaEpsZ91EzxgelwyzDE4MBcwyiUoL9gD5mqCUxBkiDbIVh_7ahQZ2Lp2pMFyL0AcW8a4HDyc8Pk3SB2bk8XjtJzMJOIMNg1v43FU3J8PUOysZ7ve41G5mofcFPgyQ0vn4luNfj8lSyjOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برزیل
🇧🇷
-
🇲🇦
مراکش
🏆
جام جهانی ۲۰۲۶ - گروه C
⏰
بامداد یکشنبه ساعت ۰۱:۳۰
🏟
ورزشگاه متلایف
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
- برزیل پرافتخارترین تیم جام جهانی با
۵
قهرمانی است و در همه ادوار جام حضور داشته است.
- برزیل در جام جهانی ۲۰۲۲ از گروه خود صعود کرد و در مرحله
یک‌چهارم‌نهایی
در مقابل کرواسی شکست خورد.
- مراکش در شش دوره جام جهانی حضور داشته و بهترین عملکرد این تیم کسب مقام
چهارمی
در ۲۰۲۲ می‌باشد.
- مراکش در جام جهانی ۲۰۲۲ با حذف اسپانیا و پرتغال به
نیمه‌نهایی
رسید و یک شگفتی بزرگ خلق کرد.
🧠
اگر دنبال جبرانید، یعنی از مسیر تحلیل خارج شده‌اید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/65973" target="_blank">📅 01:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65972">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
نایا خبرگزاری عراق: شنیده شدن صدای انفجار در قشم و سیریک  @News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/65972" target="_blank">📅 00:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65971">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
نایا خبرگزاری عراق: شنیده شدن صدای انفجار در قشم و سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65971" target="_blank">📅 00:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65970">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f73bf5f98.mp4?token=o4FQ1pMI9-jYmkkBniyqYi7oBdy3CTom-Dzv5OKi6YF_07CR2U8KczPiN7uGSuLJIvbzorZmbxbPrbnF058DiH0f0V5sL_gZZQOXVivvJ-A_0SsYjruGKBvwHfsWNbdbmbnGbkYor7j4HUkWl5VCjI2wv_RE_Et1IGzCZL1fVxRZ1_nIYeniXN7CR1HlKr72N2iEuPbLtg_m8odNHs4hSs0XrH2xCx9JMDzn2GTaL02a4y7rMu-SutG17DsU9LxH0txJLUafhsuRhIpaSZ4SBY4ch17Ltf4FVXrLChBiAYhMTkpadR2UadSFhWLBudoP7oz0aEhO_yhWsZqnVYmYJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f73bf5f98.mp4?token=o4FQ1pMI9-jYmkkBniyqYi7oBdy3CTom-Dzv5OKi6YF_07CR2U8KczPiN7uGSuLJIvbzorZmbxbPrbnF058DiH0f0V5sL_gZZQOXVivvJ-A_0SsYjruGKBvwHfsWNbdbmbnGbkYor7j4HUkWl5VCjI2wv_RE_Et1IGzCZL1fVxRZ1_nIYeniXN7CR1HlKr72N2iEuPbLtg_m8odNHs4hSs0XrH2xCx9JMDzn2GTaL02a4y7rMu-SutG17DsU9LxH0txJLUafhsuRhIpaSZ4SBY4ch17Ltf4FVXrLChBiAYhMTkpadR2UadSFhWLBudoP7oz0aEhO_yhWsZqnVYmYJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صدا سیما: هک تصویر انفجار اتمی در تلویزیون، سیگنال آمریکا بود
!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65970" target="_blank">📅 00:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65969">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060800d75a.mp4?token=MPwswvn0dhBAkEIELp3SRecbcsXPd-uUHI5yGKCjzrYYhpYdONyikpB8paa-clDz3iYfM0pEzazrb-BDcXEzmD8k919lc2MYX4ZJk-1Dv0V3wuWm4pj4vnvxxpWaWiqGBj2I2g9H9cnCqXxrUGJM-VFFb3kq2nrkOftg1jaFYOGUAh7T7OoEz0abUfPmLn6tFbfFjXyI7KrLI9qorAueeGV95TFaDzzEUUJMjIaHxsKJZ2R1YmFT0XKqMgGyiRajm62RuDnfV5b0FGRH7NXynrfPNGwtvQPA5eFauDs9BY9pNm1Ev6N-JWif4ZU_i39jVq4OmgGRiDHHuD9UeUMu9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060800d75a.mp4?token=MPwswvn0dhBAkEIELp3SRecbcsXPd-uUHI5yGKCjzrYYhpYdONyikpB8paa-clDz3iYfM0pEzazrb-BDcXEzmD8k919lc2MYX4ZJk-1Dv0V3wuWm4pj4vnvxxpWaWiqGBj2I2g9H9cnCqXxrUGJM-VFFb3kq2nrkOftg1jaFYOGUAh7T7OoEz0abUfPmLn6tFbfFjXyI7KrLI9qorAueeGV95TFaDzzEUUJMjIaHxsKJZ2R1YmFT0XKqMgGyiRajm62RuDnfV5b0FGRH7NXynrfPNGwtvQPA5eFauDs9BY9pNm1Ev6N-JWif4ZU_i39jVq4OmgGRiDHHuD9UeUMu9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
گفتگوی عراقچی هم اکنون شروع شد.  @News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65969" target="_blank">📅 23:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65968">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
عراقچی:
محاصره دریایی آمریکا اولین چیزی است که در این توافق به آن اشاره و تاکید شده است که باید رفع شود
دارایی‌های مسدود شده طبق یادداشت تفاهم اگر امضا شود، آزاد خواهد شد
هیچ‌یک از دارایی‌های ما نمی‌تواند مجددا مسدود بماند
برای جبران خسارت ایران طرح بازسازی در نظر گرفته شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65968" target="_blank">📅 23:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65967">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
عراقچی:
به زودی ایران و عمان بیانیه ای مشترک در رابطه با تنگه هرمز منتشر خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65967" target="_blank">📅 23:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65966">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
عراقچی:
به طور قطع تنگه هرمز به شرایط قبل از جنگ باز نخواهد گشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65966" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65965">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
عراقچی:
پایان جنگ در توافق همچنین به معنای خروج اسرائیل از مناطق اشغالی در جنوب لبنان است و ما این موضوع را صراحتاً به طرف مقابل اعلام کرده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65965" target="_blank">📅 23:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65964">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmhRk2NC8w0HBaCKgdLjcWuyfGqYriB3tPF6FXi0uivKzx_1EVxIycVlmv8z4fZHQi4GktOAatiV8OkmaQrPnzlcuFg4nfLVQq3nE4-V6HNVRxRWUrU5uPvfey6nJg9sCojtxkoN-fZbQo3Iai58TMF10TaNpEge0DWXJr_55WCBVABYV8N_xqCvCUcmV5tpNAZ7MsoevIwWbTq6fwKf7O4S8AssDYUrccrlcBlP1OeJHpve7wz0rLHY18w-fkscBOjXiAwspL30XFp2QFYv3F4291X71wbV2v43VLXurAe4XNL-a0Xfv-B5iP6wg8rpnquGQ9ZkyOxxgGtfMyugGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
تعهداتی که داده شده باید حفظ شود. نه اگر و نه اما و نه بهانه‌ای. برای معامله نزدیک پیش رو، راه دیگری وجود ندارد.
هر چه بکاری، همان را درو می‌کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65964" target="_blank">📅 22:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65963">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‌
🚨
🚨
عراقچی:
نتیجهٔ تفاهم یک یادداشت ۱۴ ماده‌ای است و وقتی نهایی شد تک‌تک آن را به مردم می‌گوییم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65963" target="_blank">📅 22:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65962">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
عراقچی:
ما پیروز میدان هستیم؛ مقامات خارجی به من می‌گویند که ایران را این‌گونه نشناخته بودند و ایرانی‌ها شگفتی آفریدند و با قدرت بیشتری از جنگ بیرون آمدند
من می‌توانم اسم ببرم که کدام مقامات این حرف‌ها را زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65962" target="_blank">📅 22:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65961">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‌
🚨
🚨
عراقچی:
هیچ دوگانگی بین میدان و دیپلماسی وجود ندارد و هردو در یک‌راستا حرکت می‌کنند
به این ۲ رکن، رسانه و خیابان‌ هم این‌بار اضافه شد و ۴ رکن باهم در یک‌سو حرکت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65961" target="_blank">📅 22:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65960">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‌
🚨
🚨
عراقچی:
همهٔ ما مدیون تک‌تک نیروهای مسلح هستیم.
همین‌طور ما مدیون مردمی هستیم که ما را تنها نگذاشتند و هرشب در خیابان‌ها هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65960" target="_blank">📅 22:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65959">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
عراقچی:
دشمن تصور می‌کرد که بعد از جنگ ۱۲ روزه، در جنگ ۴۰ روزه می‌تواند ایران را تسلیم کند اما با مقاومت جانانهٔ مردم و نیروهای مسلح ایران مواجه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65959" target="_blank">📅 22:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65958">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
#فوری: طبق اعلام زیرنویس شبکه خبر ، عراقچی تا دقایقی دیگر مهمان این شبکه خواهد بود  @News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65958" target="_blank">📅 22:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65957">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
خبرگزاری تسنیم وابسته به سپاه؛
حزب‌الله: لبنان نیز شامل آتش بس میان ایران و آمریکا است
«حسین الحاج حسن» نماینده فراکسیون حزب‌الله:
بر اساس آنچه از سوی مقامات ایرانی به روشنی به ما ابلاغ شده، لبنان نیز شامل آتش بس است.
بر اساس آنچه مقامات ایرانی به ما ابلاغ کرده اند، اسرائیل از خاک لبنان بر اساس این توافق عقب نشینی خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65957" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65956">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 450 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری عالی
✅
مناسب برای گیم و استفاده روزمره
✅
تحویل فوری
✅
تست رایگان قبل از خرید
❗️
پشتیبانی 24 ساعته
📣
کانال رضایت مشتری @kavianivpn  جهت خرید اشتراک پیام بدید
⬇️
…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/65956" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65955">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaAjDeg3R5YznOoKDA0d_rbnSXmAsyEb8nBvWGg6M2XG9nEXfUa3XCFc4YQTqZl5dDYvHfTQ1BDUjwJUha_BIczlMSZGYm-jzUhzG69Vd6ZZRG6S7N1bRa3uFdtcR6NsNt5UX5D-wMBKT2J0VM5PTpFvJk5SWah5E8QCH-ExD7Ke-4jZlsI5Ho6pwy5ffDFuboj2FmDtUyjdQXhiRHxg9q1Uw1htvc6XgJ3xQ3lLYkkaPoLc_ysRdGrfpS6KL_SXYZqIaZ79rEpWeQ_ihD_PQg8bOE9efL4idzkneg3vbgMR1HP675oiwSWRWCRxf8UZxm1GzBlt4bjuWb5w898cXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 450 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری عالی
✅
مناسب برای گیم و استفاده روزمره
✅
تحویل فوری
✅
تست رایگان قبل از خرید
❗️
پشتیبانی 24 ساعته
📣
کانال رضایت مشتری
@kavianivpn
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65955" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65954">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
کانال 12 اسرائیل :
توافق قطعی است و این به نتانیاهو اعلام شده.
ترامپ از ایران خواسته به صورت علنی درباره توافق شفاف سازی کنه و هشدار داده انجام ندادن این کار پیامد هایی رو به همراه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65954" target="_blank">📅 22:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65953">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
رویترز: امارات ۳ میلیارد دلار از دارایی های ایران را آزاد و به آنها تحویل داده، این اقدام تضمینی بوده در ازای اینکه دیگر به این کشور حمله نشود
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65953" target="_blank">📅 22:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65952">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbHp6XkTGiNtRNgqa8r2TaYoHaMIOoExRcPFbSUbKIw_JrjtPZi6YOdRJgGsLFab7Bhu4og9oKYccNlm-PZrATgP8JOytOEmyX8Yaea39d5mnmTSReXKo351WHKacwPG60Dwpd6G-ZouE9lr_IuFUQRik6t1VOsJ9-CMlehu5s-DL9qu_S-Z_2WHtetkEE5IgziF5BvrzIh_VYlfpb8DpdtU73mK14nicWoAucnOpIwt25-HlI6mxnUC8E3IP0zLpoOVDGPKIdIeqRQWVf2AmDr1NO4lio1hdzMeqrljFfMVySthLCW74qlBbNcq5AdxFJPoEcby1LiYNu92Obb4aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#
فوری
: طبق اعلام زیرنویس شبکه خبر ، عراقچی تا دقایقی دیگر مهمان این شبکه خواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65952" target="_blank">📅 22:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65951">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/US0XaTz1RPxKnSnS4mffWihQvGGwyvHVoIeZK14ws9-esqyB00kKn5fvQy2Bw1Kp_524kj0estH8rkl2OgR1AjpGDLv4UQeITQNnrZpWcZqZL46ZsWfvygPdF3z9F0bsWaNDE8uY1BLV8WT7QtMPHnpshSCqWCfvIg3v1p0g2igwuHsCKOaY28qsRg3BKW5OhP1Q2Q1GH88t--DV7jTw7YGNjTj_5Z_cJRu-nkmbn39DApQB7WT-A_uSWQX7kHf4ZwUcrenc5RxioybIx0AKgzPUwwamBLPj9MDGiI7FeqhY_0aLdNeFitB6thzkwotYCeyDidUWD8hib1acZlE_nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا به شیرمردان سپاه اسلام و حضرت آیت‌الله العظمی سید شیرمردان حاج آقا مجتبی حسینی خامنه‌ای، خوب دارین کیر می‌کنید ترامپ زن کصه‌رو #hjAly‌</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65951" target="_blank">📅 21:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65950">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHlwQxF_Vqsl0YtcxnHNAFcKxJqJFawv5PT_fnMEMp3LkL8wCzMboNBay97cb-6yBWMdyUbgEpiu5MkS9Nee3c5iqQkmcWiMYCbBIMqrS3BNn57rG_R7rxDXeJiPoJjA4VZy2RYw10kTg6OoB29Rd-BsUq_k8V7OsIB0k8cnAyHqsjF2lbU5i-n4w92_-qcZJg6i2Swb__SIp3X2H8gt-6sHLFEGJZ7saapwTsSdprPzizuP4Yqvmp5dak1NW7-jg4PeZlwGmU3EA6Esgx2kxM9dS-sbHWiivBqGglpyLSPxTXcWC-BJEnQDO9p3ZBqKFvAgQAbjL4FF3gacP0e_zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ثابتی نماینده مجلس:
طبق اطلاعاتی که به دستم رسیده توافق احتمالی بدتر از برجام است.
نه احتمال جنگ را از بین میبرد و نه گشایش اقتصادی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65950" target="_blank">📅 21:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65949">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
الحدث:
وزیر خارجه پاکستان امشب عازم ژنو میشود
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65949" target="_blank">📅 21:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65948">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🤖
رایگان پیشبینی کن؛ جایزه ببر
🍸
درسته! کاملاً رایگان می‌تونید برنده بشید؛ فقط با پیش‌بینی بازی‌های فوتبال، بصورت کاملاااااا رایگان میتونید برنده جوایز ما باشید
💸
جوایز هفتگی پیشبینی رایگان
🥇
نفر اول ۱۵ میلیون
🥈
نفر دوم ۱۰ میلیون
🥉
نفر سوم ۵ میلیون
🛫
…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65948" target="_blank">📅 21:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65946">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kwt5oNeFK9uD--4YpgpZ546iXIsxFdFDZqC3TKcPwvU8yiLv3yCf8Tx0SPsPfOfZaNZ6L9LIRMNoaczXxWyp2PXi_f5xwgm1xe4L5OI-Aczlgi98OmU4ohF1LtQqr1S4DNhGZjU3AKJkuctVPOQUlKumOwmnUD0uHwv2wpEi6Fjt0tlp61jXv72doEPJfB9V7_Wh_-C03hTkl3oROWH9j8G7kyW9qny3uDtM6_FoJtLUn4I31qhJwhhQO9Lzvh_IzblZwJ7dLr8JvmK4N1djS0dzb6CrK49R1h0ZBtfrJFDKEsn3_CmtIYqWh2eLZqNZJmKU65YX4hEW3XEyr6qUkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
رایگان پیشبینی کن؛ جایزه ببر
🍸
درسته! کاملاً رایگان می‌تونید برنده بشید؛ فقط با پیش‌بینی بازی‌های فوتبال، بصورت کاملاااااا رایگان میتونید برنده جوایز ما باشید
💸
جوایز
هفتگی
پیشبینی رایگان
🥇
نفر اول ۱۵ میلیون
🥈
نفر دوم ۱۰ میلیون
🥉
نفر سوم ۵ میلیون
🛫
نفر چهارم تا هشتم ۲ میلیون میلیون
📈
۵ نفر از اعضا به قید قرعه ۲ میلیون
🏆
فقط پیش‌بینی کن و برنده شو
👇
➡️
@PishWin_Bot
➡️
@PishWin_Bot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65946" target="_blank">📅 21:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65945">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e7da6863b.mp4?token=MFczX-bXjhKdigFEjMSBbXRRUnc833jChYZjx1QG90H6jkHaoEiP50GOnetvQDCIUhiogo6cX8-44Cf9sushSLSoaelekZ8zBFfKHELp7VJ4klPMVr9cLA6lXtbbgXfz04yqzz1hoM3nYdc6FDUjhYDTx-asWlZAcZuvT82cKlFqxzEUYWhvnxwlw3rYtuQiWIwY3Y3Sc1-ilzmwRs9l4m_9gePnJlkCMgFnVKS0j3wkbRrczAfcKkLF-rEPJrm9kzx5w6_jCK-nFj8RNL8OXW3JXx9B_WjCiPf2Z5fm-ZVheeMIrVXnAvRkwcYHEDBndl8mX8cr_SoIjv-raD0Ccw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e7da6863b.mp4?token=MFczX-bXjhKdigFEjMSBbXRRUnc833jChYZjx1QG90H6jkHaoEiP50GOnetvQDCIUhiogo6cX8-44Cf9sushSLSoaelekZ8zBFfKHELp7VJ4klPMVr9cLA6lXtbbgXfz04yqzz1hoM3nYdc6FDUjhYDTx-asWlZAcZuvT82cKlFqxzEUYWhvnxwlw3rYtuQiWIwY3Y3Sc1-ilzmwRs9l4m_9gePnJlkCMgFnVKS0j3wkbRrczAfcKkLF-rEPJrm9kzx5w6_jCK-nFj8RNL8OXW3JXx9B_WjCiPf2Z5fm-ZVheeMIrVXnAvRkwcYHEDBndl8mX8cr_SoIjv-raD0Ccw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شهباز شریف:   در بحبوحه تلاش‌های میانجیگری فشرده پاکستان، ما کاملاً از کمپین بی‌وقفه اطلاعات نادرست که توسط کسانی که می‌خواهند توافق صلح را خراب کنند، به راه افتاده است، آگاه هستیم. گذشته از این سر و صداها، می‌توانیم تأیید کنیم که متن نهایی و مورد توافق…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/65945" target="_blank">📅 20:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65944">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lM87V-ek0ebXGMBLYyCwfz8RfmppnOcK07cbGZl663mMp7X7TTTIMytbJIo8qOnDwdInaEDr8uv2ji0sx4WY0OFaH77KgRaN-LLf1LNQ-m1tbsRsNsJ27hz0rsjwWWgtlj1O0nlZ7ebX6HoTrgyUn7re91vb5rUzlBjKOAnYvRvIvbp0W__Txnds-LJNJxv3lr_2hOTmmv-ZdMCUScr3Awnhxr9lnMY8s0WTue3BQfUqDOSe6NSoBtG2Jh6RWwqdb8tn0DeOBlNt8LJXlMhfS0Xys8C3nsrSVhtgK41EU-0wE5A_rzygskWGrnnx_phtmBdF_HSRtnvg0D9fE75HBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهباز شریف:
در بحبوحه تلاش‌های میانجیگری فشرده پاکستان، ما کاملاً از کمپین بی‌وقفه اطلاعات نادرست که توسط کسانی که می‌خواهند توافق صلح را خراب کنند، به راه افتاده است، آگاه هستیم. گذشته از این سر و صداها، می‌توانیم تأیید کنیم که متن نهایی و مورد توافق توافق صلح حاصل شده است و پاکستان اکنون از نزدیک با هر دو طرف برای نهایی کردن مراحل بعدی همکاری می‌کند. صلح هرگز تا این حد نزدیک نبوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65944" target="_blank">📅 20:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65943">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58b6a7c560.mp4?token=nbG0Oymmfzulz_6Q4mboysczj1ZPQmXBuw9pTAZRPfbVcBcGzwkW-Nfblulw6JnnNR2O5l9E9lJ6z4EolBHA5g9FdR-90DJ6OrMtlVsNIF32ivWqRRcXyjmBuRGf6xcxvvTFnUuRDazsLniK_BlKM98QGKbESpXNbQcUVOk-Iiy_sr8YBH6UF8Zj_e746jhm_HzNwaJGuK8XzGDrFRZ0keWR14XnGcb-_JFARpFOG78aN4wpYEUGsFNVr_E1XIF-pTsDByP9jwk9Sifmhnc3UNYJTnH5IThKbSXrNAKOS9R3C2ypRAqRdvHx8ak_PkcdrfZday3oxOhq9nUdKG1JNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58b6a7c560.mp4?token=nbG0Oymmfzulz_6Q4mboysczj1ZPQmXBuw9pTAZRPfbVcBcGzwkW-Nfblulw6JnnNR2O5l9E9lJ6z4EolBHA5g9FdR-90DJ6OrMtlVsNIF32ivWqRRcXyjmBuRGf6xcxvvTFnUuRDazsLniK_BlKM98QGKbESpXNbQcUVOk-Iiy_sr8YBH6UF8Zj_e746jhm_HzNwaJGuK8XzGDrFRZ0keWR14XnGcb-_JFARpFOG78aN4wpYEUGsFNVr_E1XIF-pTsDByP9jwk9Sifmhnc3UNYJTnH5IThKbSXrNAKOS9R3C2ypRAqRdvHx8ak_PkcdrfZday3oxOhq9nUdKG1JNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از مراسم دیشب افتتاحیه جام جهانی
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65943" target="_blank">📅 20:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65942">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPLZyoIZMAUh3ZyE6j24AW4faOFUCOins-xd3nPrwZN8K6UYVCNDBiKQ3b9qgnPzUQw6WqRc9_Av7nP-4wXwk4nHUxOGnjjhhJKSwIL-v2A9dVljPPOdfMU49MubZbkjY81rffKjN1TAbXIetu55Fe-eIH7hN00ZXNi1mvt8hqYZaCWuUwt2kPoptVteyQu03QOteH8OlPapQCKFPD4UZT4PQQvBO0BqiSa9wNJqdX75U3M_zsT9cXHBmwsdtCNCe4Y0E1K3nr5ICUliesvfQI3zNGc4TgXLc1NQNiJEMolJM3WPfMj-_7qJLkVMumNhWKVYvjYbFkhntbgXujSeEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندزی گراهام:
ایده یک صندوق بازسازی ۳۰۰ میلیارد دلاری، با توجه به اینکه چه کسی مسئول ایران است، به نظر می‌رسد بی‌معنی باشد. این شبیه طرح مارشال برای آلمان با وجود نازی‌ها در قدرت خواهد بود. آن زمان این ایده خوبی نبود و هر صندوق بازسازی که به نفع این رژیم تروریستی باشد، اکنون ایده خوبی نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/65942" target="_blank">📅 20:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65941">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65941" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65941" target="_blank">📅 20:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65940">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/samNzQYV8ACxELDw41PWpWpmwzcAumlSLJOUvL44FugvICzXxxOwfEyontXBpZXr1cKtrB3KBui8JUOVRV5of7DQUDjMbQbskVSNRfvCsw3uush4TyBqjyZ4dF44NtLoCtfVPUvLAxMZ3nljtqqHwM2BRXXV053a1eVwEihTkLbMeA3GpeA5ao33KLUMtQjaIvVG0b1HmHaTRVdWzf9Dmem9OdsFL21_7QRH9kwJAuKtUcp9IjM2rqi2XryvUzvu_lK9JklygbqteQ6BLlo1WJ1Hu2-92fhQb7tPYhpwwVwgn0RnvlT4j9fem_Jk3tjaHrgwxV-d_U7tmNepsI5Htg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65940" target="_blank">📅 20:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65939">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWF1BgZHEUIoWJfDrKFzSx5AHYSE-em1f7htRV-l5gSsPGD98C0m0BwcYBfvWc7U78LCLyutSieTabXq5POxZ2rqWWwKH7W-pozzgewL3flMD0iZWCDg47t2G2-Zn5dqxaNnLdVfZG5NOIcUCn2dJPFcN8Dp8DRm-_VwWySGxLWSHebB3h75m-mCMUY0pZTvAfTAfa5OCvaD_0tw3GxQ6IT_cSfUtc7PDq_6UiqkuHXiQKNn8kZlIo_r8fno6PxLWUUjKkXTxr63VWhL0__384dKDykM1UY4DIW3Mjcd_IglWKqZ-snmw_GQuF9DAyMIecfwMMtI8FINzOhZEQP8SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سنتکام:
ناوهای جنگی و دارایی های هوایی نیروی دریایی ایالات متحده همچنان به گشت زنی در آب های منطقه ای ادامه میدهند و محاصره علیه ایران را اجرا میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65939" target="_blank">📅 19:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65937">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f3347ca6.mp4?token=WPWvHwwkApJ8xo2rJLJnmK4BvShpVr1YV8-ZD09Kq9VotQLRj07b5SVUswRDWZazZJeNCDposMhNiA2o_vN8nQ78F6RIwomJ5yxc3uwqEnSu560ttmL0Kb48eGTrOChc8xSGjNmWycBCYsZnMpTZYGCYvlQJzvbTcKn16YEJayy-1HJf15Q1gefkzrja6bIpa4qN7M8Na27qLxtRR6uGdZQfHIuWE60XPcBZxo_tPo1sDfj6H_5je4AWYAEsBRFmRY6ZG893E7YhJBTup-C4MeOtMRkq6jqBVB4Xl53RQkw1LZp8ab06W5iaP_dkYrCmtooAkiQgYBYnVcT-SgF1Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f3347ca6.mp4?token=WPWvHwwkApJ8xo2rJLJnmK4BvShpVr1YV8-ZD09Kq9VotQLRj07b5SVUswRDWZazZJeNCDposMhNiA2o_vN8nQ78F6RIwomJ5yxc3uwqEnSu560ttmL0Kb48eGTrOChc8xSGjNmWycBCYsZnMpTZYGCYvlQJzvbTcKn16YEJayy-1HJf15Q1gefkzrja6bIpa4qN7M8Na27qLxtRR6uGdZQfHIuWE60XPcBZxo_tPo1sDfj6H_5je4AWYAEsBRFmRY6ZG893E7YhJBTup-C4MeOtMRkq6jqBVB4Xl53RQkw1LZp8ab06W5iaP_dkYrCmtooAkiQgYBYnVcT-SgF1Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی قبل از جنگ ۱۲ روزه و ۴۰ روزه:
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65937" target="_blank">📅 19:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65936">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBR3Mv8gxLa2XDq0227rnYIRlCHGt-5wtZwWO5yEAn5FAtjd4iV3uEPPMikl8-UKhA3_JG09CY3bHBQsbLSWz0hhkcqMqeo0UWuvPvWCd7hweitkNIBVb3eQ1Hj7_3foYZec7LUk-x9nkClhHmMAeXNE1zBQOa5G9k9pu9BQOAFVG5RN5oeGHB2ZygUbJlKbXZODlKTHussD9xe2DOho-Z_ooCwdKpE_dYkusYdp2xtA-IoHf1RzkFFGrjZzR1jE2Pa3halvrj7qEvxpy4bHLX9WN--CeL1Uv_ZOgqF_DZrjAQ4h2BWrwisq-S95OGjrIYT-bwU8gpT4Ppfb96NvbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: تفاهم‌نامه اسلام‌آباد هرگز تا این حد نزدیک نبوده است. تا زمان نهایی شدن آن، رسانه‌ها باید از گمانه‌زنی در مورد محتوای آن خودداری کنند  @News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65936" target="_blank">📅 19:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65935">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
جی‌دی ونس:
اولاً، ایرانیان هیچ وجه نقدی دریافت نمی‌کنند و هیچ وجهی صرفاً برای امضای یک توافق یا حضور در یک جلسه آزاد نمی‌شود. این توافق به گونه‌ای طراحی شده است که نگرانی‌های ایالات متحده و متحدانش اولویت داشته باشد، و اگر جمهوری اسلامی ایران تعهدات خود را انجام دهد، فواید اقتصادی به آن‌ها و کل منطقه سرازیر خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65935" target="_blank">📅 18:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65934">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تا دیدن اعصاب ترامپ تخمی شده عراقچی یه توییت زد گفت رسانه ها چیزی در مورد جزئیات توافق نگید :)))) #hjAly‌</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65934" target="_blank">📅 18:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65933">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
ترامپ:   شرایطی که ایران به رسانه‌های دروغگو فاش کرده است هیچ ارتباطی با شرایط توافق شده کتبی ندارد. آنچه گفتند، از جمله بیانیه ضعیف و تأسف‌بارشان درباره وجود توافق، هیچ ربطی به حقیقت ندارد. افرادی بسیار ناصادق در برخورد با آنها هستند. هیچ چیزی به نام…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65933" target="_blank">📅 18:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65931">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Td1OzV3FCtfgO8wvODLeNHi5vkap-zwLxw5jgh-Gv5MzuiGrbwdw4odAzDZubdGMUl9BvNNjOlaRB_bid-M1moK4FXMbYJTK9kPpLaYI7e8MiAI9G59KtjsLjS96W_xHtu7zTJSdNumnni3HkVYi3IsCMxGqdIqIY_nzzexLyC0N-vYPrfzgf14kV2GoTGzOhOy-u0V3G3SePS0HhOwVSoJI5TEmHp-9rsoyn6fuR_XI3EuK9Dj1wrpUVQhDlKEjdEaJVefYxjHEKhZ5Cpmpokrn1qU4MWA5pwJeJzXTakoR_NE4GMuN7gXXKIOuhkuZ8YipSTxaHOqYxu4BmxECIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vHTPNnsMfdMsWNKSVqqJo9DrbSl6t3eSeKbhiPPIrW9spG6Jo1ArrNwzjNHmly9nfCfmUoztftO-7L8WXcxfEJgFmgxXRDNayBaWCVMtNCq0qjm92kmCfYIjdGfS35rtnknk6p7-hC8kJVoiv7mGBXRPSHFkD6PuVK4KwYBmwXDEYPq3mgq4by0eWqaeNpmDlUnFt1EUha3-kDhK4BhoFRwcMeaPeI8nPMeVe_w8tIEN26PCSLwaMg9W_N06OyvOzVaVqlZSDAxED6oGsDPlUt3WyIJAiJY0Ex4hu6xEINZMZEUXhMFAIS8HH2ioJx9og_J5M_FUzFkkhSiSPnbzhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
برنامه امتحانات نهایی پایه های یازدهم و دوازدهم منتشر شد.
شروع امتحانات از ۱۳و۱۴تیر
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65931" target="_blank">📅 17:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65930">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c65a1f96.mp4?token=PnxoUqS5nUy8fTVXErNQUw0jmh6ZqpMPtnOxGo28bq6veY_NUe7HKMqbf0K4R7KNACZiz2DeDx-rcUVTkVanDo05nlTcAdYtwm6swDI5QIVCSE4AJyNkb3vNnVsQrzyixBoxsy_2L_s1krr57CCKMD5tJX5I9cXJ1jLrhc-VY-P_RaWGstkXvo3HD7qSQXrlg8a1zyPrGyEY3xVHNltpB5Il95BqtQL1wfJqpy2euyeL1iWiKYGktUBdYZKZtbgK_Lpo4nSMD3NJkOCsZG-PCGDnSFsgWXhiMxk3E_13pPYE0EoC8M05XUDZV0KobumshyTL5pmleLPjoIBd2oZ7rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c65a1f96.mp4?token=PnxoUqS5nUy8fTVXErNQUw0jmh6ZqpMPtnOxGo28bq6veY_NUe7HKMqbf0K4R7KNACZiz2DeDx-rcUVTkVanDo05nlTcAdYtwm6swDI5QIVCSE4AJyNkb3vNnVsQrzyixBoxsy_2L_s1krr57CCKMD5tJX5I9cXJ1jLrhc-VY-P_RaWGstkXvo3HD7qSQXrlg8a1zyPrGyEY3xVHNltpB5Il95BqtQL1wfJqpy2euyeL1iWiKYGktUBdYZKZtbgK_Lpo4nSMD3NJkOCsZG-PCGDnSFsgWXhiMxk3E_13pPYE0EoC8M05XUDZV0KobumshyTL5pmleLPjoIBd2oZ7rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین طهلیل ویدیویی بنده از شرایط خاص منطقه برای عزیزایی که تو دایرکت درخواست داشتن
🙏
🙏
🙏
#hjAly‌</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65930" target="_blank">📅 17:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65929">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6007e01a82.mp4?token=s9fpfh0gTMGTx6x9fY2UUV7SplKt0DBaooWiE7BdkODFzrHyi-0ubUSl2qxeWe0x8PYAsGAFbW2-pQEjl7YYwS6cvbgc6juEf6DJlkeu5SEgUKEu-Tj6lNhqKcFDot0q7hyKgWA-4FXCKH9PAi0zErEDpccJnw4Nju-UaLbGFvg7uik7PrBYh-LbX6GoSVAK3HCkzWigfXsRFzEy-CizOYSlYQdsO0PwO2lA9NA9VnSkz_JnGYZQVz6bqoK10ZsPl-IGfAtu9jyVSivGicHtiE1B4svQuBqlUH893bvmdbwCoYgJNpYO9iaobP0MukYVf9gRdtpKQ2sQBVd7eWpy9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6007e01a82.mp4?token=s9fpfh0gTMGTx6x9fY2UUV7SplKt0DBaooWiE7BdkODFzrHyi-0ubUSl2qxeWe0x8PYAsGAFbW2-pQEjl7YYwS6cvbgc6juEf6DJlkeu5SEgUKEu-Tj6lNhqKcFDot0q7hyKgWA-4FXCKH9PAi0zErEDpccJnw4Nju-UaLbGFvg7uik7PrBYh-LbX6GoSVAK3HCkzWigfXsRFzEy-CizOYSlYQdsO0PwO2lA9NA9VnSkz_JnGYZQVz6bqoK10ZsPl-IGfAtu9jyVSivGicHtiE1B4svQuBqlUH893bvmdbwCoYgJNpYO9iaobP0MukYVf9gRdtpKQ2sQBVd7eWpy9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه ای ۶سال قبل:
هیچ پیام مستقیمی برای ترامپ ندارم چون اون رو شایسته مبادله پیام هم نمیدونم.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65929" target="_blank">📅 17:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65928">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
ترامپ:   شرایطی که ایران به رسانه‌های دروغگو فاش کرده است هیچ ارتباطی با شرایط توافق شده کتبی ندارد. آنچه گفتند، از جمله بیانیه ضعیف و تأسف‌بارشان درباره وجود توافق، هیچ ربطی به حقیقت ندارد. افرادی بسیار ناصادق در برخورد با آنها هستند. هیچ چیزی به نام…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65928" target="_blank">📅 17:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65927">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‼️
ایرنامتنی رو منتشر کرده و گفته تفاهم نامه پایان جنگ دربرگیرنده این مسائل و موضوعات است:  ۱. موضوع هسته‌ای دست‌نخورده باقی می‌ماند هیچ توافقی در مورد پرونده هسته‌ای در تفاهم‌نامه فعلی انجام نمی‌شود و ایران هیچ تعهد جدیدی نمی‌دهد. گفت‌وگوهای هسته‌ای در مهلت…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65927" target="_blank">📅 17:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65926">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzS-2HsZ2fdjpd7_9DginWWtw_4VU5BeN0ECveJT2Y9MvoKFWbbKivUp5R2AOSIVrtvRYVuBBEwjLOn9YdYPfDvSt1h--R1i_CmEhWLoh0S1ouK96fLFUxZtarDocK5jRWZN39KXSS4JwTQ2zVLRzwy0873zcMoTQzguTWbsSv97Z7Zgv5xcRn0mjIF-Xc52tCunRLJX36qk7ag34yu-hw8w1CQxb3PMrtNVKw5AFon8Xc5C5B2YjEBOEbO8SzoYDgOjli2Q5aIgW01To7v8sXwZMSFJJAmki4N5_SkV5kCNj_5rEWDU-7Zr_ff8D7KBk7741rGcBGHV9v71Pn2fzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پلاکاردی عجیب در تجمعات شبانه
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65926" target="_blank">📅 17:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65925">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMDsx-12BYH9nAGjM9RHEtQ-szDLHmquCrWIWv4Dm8rWzCCKRaYKBJl0ggT9hA_ap15LKgXmEqr9gAWoLGcweXwhK2PkUY0jEErIKzQto6KXflSCtGR4EyS-fS6ix7mWJWfNxKub7YQ6OS3y9_FOwKt9LdtybIfWM2NSd1Vt7ascNvxiOS8kpMEyiRehypD8d3PEpHNEALBVpiolino_lu9r01-JD2kxKpYSo2Ff7lixpVoKDW9TUAe41sf8gWfdAD4A8xhx_1Cbh9PLMUw7UVEbZXxpHc3KKFxg_8-5sC3bHCWwjmIwn6yW051MsafnJoafv9xYKR_MfAg-THqTrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤡
ترامپ در سال 2049:
ایرانی‌ها هر لحظه ممکن است توافقی را امضا کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65925" target="_blank">📅 17:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65924">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tD3wIiWv_q9qCeveZ8y4ga3Nwkvspc-SHLvBGHxDCVjRFWZNUBb8r8drGCMcaIzI2fgs64nYnz6HoDmwVu-OhEViVjf3FRSL1D7hLOamUZz9RWGASWb6lNhqAzhdTceli7zLwfoZwL8UJvlUC8TVMgfY_2IPp9FVAaYH8WPW5AakmCbGv87RjNWY0CvFNzlccVhkdNYspljwPBF0sjpS66im3JB31u8DilU08zNo0Aw2TTRvRTqQW5Spctou0l6mNyzBeU5nuHcveZqpbSyXNI0jmPWs2cuCiiC0dw2RRGtFl4GfoTQH7cMrugLbkoCfm0A4DpCrEo_ub2Etwny3CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
مرندی، عضو تیم مذاکره‌کننده: یکشنبه در ژنو اتفاقی نمی‌افتد
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65924" target="_blank">📅 16:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65923">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f5e54d8d.mp4?token=FByCdIp4D9fS2Ol4J2Pft_c38D9hKKjXcIBUVjWXobQCm-Uf69q97CRuLuXRnKYnGP17XWMOG44aR2BxTZlBtIHBfiomp26NUB1_n2nWURFwd8AuP00qekj0IYcaNsQNdd2JKxYDM5i8WF-QTFxF--vT0uO6JNObHlwTJcO5V4zjYnUfqR7UBbflYQKz0MrkK5OzMGBfdHhliyhqWwucAL7AXbUplw_-iYecDhqeFrt84xLdZN1Datcrr9n43-WlEJZyOTY6_quHCVsYk96vS1IVrN7j3V5dY3W__UiASsOx-O8kkCHWrEZ7wSMjSAykyxHndUb7AaMJcegD9POVN2Q2EllUiwKUbHsWVvKjaS8T1fcFYvZ1-lu3pTwmxVotbb4t16vm7PvE86x1ojqQwgXwbSW1QjsK_vmr1tpTUyFlGGAtT82Pm5Cf57mJv-E6mZioh-XmYmef_6L5aTg0sVEU7qf6BT6kVFHqZeukcm7KNA90xm8RKXhygvkRi92gNVObmvQKXOHh4y-o2EWha64BFmZeSS3w1KgdRAVrinsoz_ik8p11L51gCXkxIvlWzr1B6lSpKiwVRuOVVtpDpf89aiUTqbsruq2vkYJwVxJUdw2dTjcvB8oSXqXhTrvv30APpkQarF2XlgbGRpc9ZtYLUbh0Gy0mtxK7X4DUDak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f5e54d8d.mp4?token=FByCdIp4D9fS2Ol4J2Pft_c38D9hKKjXcIBUVjWXobQCm-Uf69q97CRuLuXRnKYnGP17XWMOG44aR2BxTZlBtIHBfiomp26NUB1_n2nWURFwd8AuP00qekj0IYcaNsQNdd2JKxYDM5i8WF-QTFxF--vT0uO6JNObHlwTJcO5V4zjYnUfqR7UBbflYQKz0MrkK5OzMGBfdHhliyhqWwucAL7AXbUplw_-iYecDhqeFrt84xLdZN1Datcrr9n43-WlEJZyOTY6_quHCVsYk96vS1IVrN7j3V5dY3W__UiASsOx-O8kkCHWrEZ7wSMjSAykyxHndUb7AaMJcegD9POVN2Q2EllUiwKUbHsWVvKjaS8T1fcFYvZ1-lu3pTwmxVotbb4t16vm7PvE86x1ojqQwgXwbSW1QjsK_vmr1tpTUyFlGGAtT82Pm5Cf57mJv-E6mZioh-XmYmef_6L5aTg0sVEU7qf6BT6kVFHqZeukcm7KNA90xm8RKXhygvkRi92gNVObmvQKXOHh4y-o2EWha64BFmZeSS3w1KgdRAVrinsoz_ik8p11L51gCXkxIvlWzr1B6lSpKiwVRuOVVtpDpf89aiUTqbsruq2vkYJwVxJUdw2dTjcvB8oSXqXhTrvv30APpkQarF2XlgbGRpc9ZtYLUbh0Gy0mtxK7X4DUDak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هگست وزیر جنگ آمریکا امروز ۴۴تا پرس سینه زد
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65923" target="_blank">📅 15:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65922">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‼️
خاورمیانه در این مدت
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65922" target="_blank">📅 15:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65921">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‼️
ایرنامتنی رو منتشر کرده و گفته تفاهم نامه پایان جنگ دربرگیرنده این مسائل و موضوعات است:
۱. موضوع هسته‌ای دست‌نخورده باقی می‌ماند
هیچ توافقی در مورد پرونده هسته‌ای در تفاهم‌نامه فعلی انجام نمی‌شود و ایران هیچ تعهد جدیدی نمی‌دهد. گفت‌وگوهای هسته‌ای در مهلت ۶۰ روزه پس از امضا انجام خواهد شد.
۲. تنگه هرمز؛ نه واگذاری، نه نقش آمریکا
ایران هیچ تعهدی در مورد واگذاری مدیریت تنگه هرمز نمی‌دهد. آینده اداره تنگه در چارچوب یک امر منطقه‌ای و از طریق گفت‌وگو و تصمیم گیری مشترک تهران با عمان حل و فصل می‌شود.
۳. پایان قاطع جنگ در تمام جبهه‌ها، از جمله لبنان
هدف اصلی تفاهم‌نامه، پایان جنگ در تمامی جبهه‌های منطقه است. آمریکا تعهد می‌دهد که اسرائیل را وادار به پایان جنگ در لبنان کند و عبارت «تمدید آتش‌بس» در متن جایی ندارد.
۴. آزادی دارایی‌های مسدودشده با ساز و کار مشخص
بخشی از دارایی‌های مسدودشده بلافاصله پس از امضا و بقیه به تدریج در طول مذاکرات آزاد خواهند شد. تهران تضمین‌های روشنی بر اساس ساز و کارهای مورد نظر خود دریافت کرده است.
۵. غرامت جنگ در دستور کار
خسارات وارده به ایران در تجاوز آمریکا و اسرائیل از جمله موارد مورد اشاره در تفاهم‌نامه است. ساز و کار اجرایی دریافت غرامت در مذاکرات ۶۰ روزه پس از امضا مورد توافق قرار خواهد گرفت.
۶. جزییات رفع تحریم‌های اولیه و ثانویه؛
موضوع مورد بحث در توافق نهایی
رفع تمامی تحریم‌های آمریکا و قطعنامه‌های بین‌المللی در مهلت ۶۰ روزه مذاکرات هسته‌ای بررسی می‌شود.
۷. سه موضوع و ۶۰ روز برای توافق نهایی
در مذاکرات ۶۰ روزه تنها سه موضوع بررسی می‌شود: استمرار برنامه صلح‌آمیز هسته‌ای، رفع تحریم‌های یکجانبه آمریکا، و ساز و کار جبران خسارات. هیچ موضوع دیگری در از جمله توانمندی موشکی ایران، دستور کار نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65921" target="_blank">📅 14:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65920">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه:
متن توافق پایان درگیری میان ایران و آمریکا تقریبا نهایی شده و منتظر تایید نهادهای مربوطه هستیم.
متن نهایی تا زمان پذیرش قطعی آن توسط دو طرف منتشر نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65920" target="_blank">📅 14:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65918">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hGd_KOorBVO8TzY83Mx4mZ16son15TTJy2wXzXIWGxST491KqgGeguHM0smYP6pgAI3AmPrmZm4NSAtiQgY5ZSUej9PYkQRmZUjmyzsUy7aURcFp06lWvF6ZH9l0ao_tLVfU9hJ3GIbzObmt9rpD-pvHfS1zyqd545LbnCcx0CAwU4EXeqAg-7h4oEtUfCl8EfzJF52pfEVXlye9oBBFfvqsyUperEy0O27qOfpb1ZTQt0KsRgjdFBTb-AmtC2-UWNoMxm_PWagIZ4JRlljGjpL9C3NsOK_xGVwAO8HdJ9S3uw4UNO-qWuOBIWacMqTckLCll6SdduR0laWw1eJuoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uk2A3x_RMqijw-bomTHuPMCg4oVNomOsI60cOsq-le3ihEa4Tin0BXLmTrS-3D17VQfYPKmbzfEmROr-98AJS9Ol-HfpwwEN_be4aRaDj7R3MpUCPmxTNTfxiKoctlNqfYre6oYkYtaCyzjCZTajxb_-G09LLTYTomIdLt5nxHnnkj58ufFbWuqq7_PaDtvt0SY4-ggZ5NYai39loR0XLOrb-RknB5c6v0lkykn_4i7XkUaTcjorwvsf-5PO4ojCOc5tk-UyS0MmsriZIEHTqsI1rWOnlSRgGNCeiFVxX9pjODI5G1O0VnzOLDyB6bKKvLEcVJuntQvw4DkJoqNOYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تصویری که یک پرستوی نظام در تجمعات شبانه از خودش منتشر کرده درحالی که چاک سینش پیداست.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65918" target="_blank">📅 14:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65917">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aed65f61d.mp4?token=Sl2HLCWn_Q0iZPF8xuV89z2aQFF6mXZnVtHdJTvGJQjLCiqLukMuhIVVU0kUHZe5gtDECaOCRVU8kagzcTjPCBV8-gzNOckMOqCvGL_aEadpC7g2CRUNtiD5J9ffE480iDR7jl9igsNC9IWpjF_gBHKIQweJBafqSMXaCnpMSjp7T0ILl9xYahqogtd_oCLH7fSfx1NK-gYlJPrDUjvlBEoOn2kJMWMyHZPgJT2F1FTvOVCeG8D_NdcWYzHLtmImQeJIATPXkkG8nE5RqhT63VHYayHaA0D9G3IdbsrMWbO_nNfaqon6rS-YCGPkgpdSN50jIa-musk9Ad10e2GB2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aed65f61d.mp4?token=Sl2HLCWn_Q0iZPF8xuV89z2aQFF6mXZnVtHdJTvGJQjLCiqLukMuhIVVU0kUHZe5gtDECaOCRVU8kagzcTjPCBV8-gzNOckMOqCvGL_aEadpC7g2CRUNtiD5J9ffE480iDR7jl9igsNC9IWpjF_gBHKIQweJBafqSMXaCnpMSjp7T0ILl9xYahqogtd_oCLH7fSfx1NK-gYlJPrDUjvlBEoOn2kJMWMyHZPgJT2F1FTvOVCeG8D_NdcWYzHLtmImQeJIATPXkkG8nE5RqhT63VHYayHaA0D9G3IdbsrMWbO_nNfaqon6rS-YCGPkgpdSN50jIa-musk9Ad10e2GB2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وزیر ارتباطات: بستن اینترنت امنیت نمی‌آورد. وقتی اینترنت قطع بود، وزیر اطلاعات، لاریجانی، رییس اطلاعات سپاه و بقیه ترور شدند. با بستن اینترنت، جوانان نخبه مهاجرت می‌کنند و این ضد امنیتی است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65917" target="_blank">📅 13:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65916">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‼️
ترامپ از زمان شروع جنگ ۳۹بار گفته با جمهوری اسلامی به توافق میرسه
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65916" target="_blank">📅 13:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65915">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30551bbbff.mp4?token=OVkXKVZuNYg0QV_jR1Q_sCvVT2KDgdh0Vv6u5DSvYjrZqweF2WxN82lmk8KvDlt-p6nwwsqZCevzXseZco88ZH6ZMMPQcbGqo_ekmgg76yLDTlyjMY4cXTbrgg-ZQNw-mGP6yyeA4UHt0o75NobtAECqxfugwGeZdqASWhQLm9sBtO2zG2TplWWuRcLSwEuFNYSRtqnjxTXGLL3kDEwwYGxq7EOMEyVd-H5WXuCOrlGWlbfDuiIYAUheeO-krDoPdM7RGxAuOLgrMBUBlwDGXOkC0XiT5VMX3B9EFylEc982nXU5_Gc0L905dN6ZHgFYB0CcwsAmHPTEk638aRpgPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30551bbbff.mp4?token=OVkXKVZuNYg0QV_jR1Q_sCvVT2KDgdh0Vv6u5DSvYjrZqweF2WxN82lmk8KvDlt-p6nwwsqZCevzXseZco88ZH6ZMMPQcbGqo_ekmgg76yLDTlyjMY4cXTbrgg-ZQNw-mGP6yyeA4UHt0o75NobtAECqxfugwGeZdqASWhQLm9sBtO2zG2TplWWuRcLSwEuFNYSRtqnjxTXGLL3kDEwwYGxq7EOMEyVd-H5WXuCOrlGWlbfDuiIYAUheeO-krDoPdM7RGxAuOLgrMBUBlwDGXOkC0XiT5VMX3B9EFylEc982nXU5_Gc0L905dN6ZHgFYB0CcwsAmHPTEk638aRpgPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آتش بس در خاورمیانه:
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65915" target="_blank">📅 13:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65914">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65914" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65914" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65913">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=PuseyD-LcV-sO8PdCKuDupl65x_jIodgJLoqQP87Ij5vnX7J3wD-hPA7nAZOF_wJxfVI8oStnFjFFXayvdqpOJ9gkRPpsvTGg1no2NnR8Oj0MA2yRxqaDUbuhw7AUD_uyubCgQq_9Hsy4ilw0BBipddId0rchSDZp_SyesW4Npm30sOgAfTAbbtwrRg-B54oXbVDJv5VzvhaWCJvZKhE31f2JTnuDuZ6HeeJCqk8TeeIXGeZ0d1PSXmFl0YtBZzIOTDemeJIyADtkRCB1JedUqnwJaL-UqRCpbUB3zGa_W6WoNSg_Of32BNOLS177XHa4UCm9KHhzWNSETOdKrk7ZQR-GmBK7g6zr-OteRiwWUxaM42t-laTrgmZAVENb9ndiqMtpcNolXeMhsXz_Mxxundasa_qYqA6xiPGQ8SByne2OWanwIKuVLZGbIHc0zIgc-Bfy9NA8vOJdFjOAhqvVtTIFbAy8no0MFsj0FPPvTxZKZra98_32tUeMTKv-z9iX4-Y1azgagXmQTjWQd4aguBEgH0yh6jnwzLe7qxCdS66fZWYYyk7b8nGp3yUjfkbgYMGQdwh3NCGOyuV_FH4KB2rUIHZkPGdcAG1esf-WSgGQN-voIBIAv4GrD7MgH62BnDFrgxKrrgxx8ahl2s2jx_dvibFF_H_5CK0Sjk7-RU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=PuseyD-LcV-sO8PdCKuDupl65x_jIodgJLoqQP87Ij5vnX7J3wD-hPA7nAZOF_wJxfVI8oStnFjFFXayvdqpOJ9gkRPpsvTGg1no2NnR8Oj0MA2yRxqaDUbuhw7AUD_uyubCgQq_9Hsy4ilw0BBipddId0rchSDZp_SyesW4Npm30sOgAfTAbbtwrRg-B54oXbVDJv5VzvhaWCJvZKhE31f2JTnuDuZ6HeeJCqk8TeeIXGeZ0d1PSXmFl0YtBZzIOTDemeJIyADtkRCB1JedUqnwJaL-UqRCpbUB3zGa_W6WoNSg_Of32BNOLS177XHa4UCm9KHhzWNSETOdKrk7ZQR-GmBK7g6zr-OteRiwWUxaM42t-laTrgmZAVENb9ndiqMtpcNolXeMhsXz_Mxxundasa_qYqA6xiPGQ8SByne2OWanwIKuVLZGbIHc0zIgc-Bfy9NA8vOJdFjOAhqvVtTIFbAy8no0MFsj0FPPvTxZKZra98_32tUeMTKv-z9iX4-Y1azgagXmQTjWQd4aguBEgH0yh6jnwzLe7qxCdS66fZWYYyk7b8nGp3yUjfkbgYMGQdwh3NCGOyuV_FH4KB2rUIHZkPGdcAG1esf-WSgGQN-voIBIAv4GrD7MgH62BnDFrgxKrrgxx8ahl2s2jx_dvibFF_H_5CK0Sjk7-RU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65913" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65912">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
کانال۱۲اسرائیل:
مذاکرات نهایی آمریکا و جمهوری اسلامی در مورد برنامه هسته ای و مسائل اقتصادی است و برنامه موشکی در آن جایی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65912" target="_blank">📅 12:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65911">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
یه‌یارو بیکاری بلند شده تمام اسکناس‌های کشورای مختلف دنیا رو جمع کرده و باهاش ویدیو ساخته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65911" target="_blank">📅 12:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65910">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
رهبران قطر،امارات و پاکستان کسانی بودند که مانع حمله دیروز ترامپ به ایران شدند.
سران این کشور ها به ترامپ وعده دادند که توافقی اولیه با جمهوری اسلامی دردسترس است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65910" target="_blank">📅 12:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65909">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9247426e69.mp4?token=IP_6mcOHwaPepKqzsD6w5H03cP1IClICF3A8Ip7pt3cEKtFa2OrDtbfUE5FnPKj3FU1SDdqy3tPmR4fJ67lnMcDSN-h99TyrRB_mIf4CVKA0eV-MmrDlhpZN5q3H692jysI7TkzV2mgbESFaWWBKNEy93K8VqfTI6ko2clhOzEUilhSendpdu_1Q9Z_1B5gIugn1gG6sHJ_xcvKV1JxxXW6Awbj4spMH3cIOkqRf_dE18I5PkXY9mZvwdZK3Edzom0CX_ftJsq6eUcbdkK5dY9R-4mQx96mOI1PMB3tT45A04cNCNdGcBZI5ytlResEY_NVnrYXZlv0fFtdJ3LDyIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9247426e69.mp4?token=IP_6mcOHwaPepKqzsD6w5H03cP1IClICF3A8Ip7pt3cEKtFa2OrDtbfUE5FnPKj3FU1SDdqy3tPmR4fJ67lnMcDSN-h99TyrRB_mIf4CVKA0eV-MmrDlhpZN5q3H692jysI7TkzV2mgbESFaWWBKNEy93K8VqfTI6ko2clhOzEUilhSendpdu_1Q9Z_1B5gIugn1gG6sHJ_xcvKV1JxxXW6Awbj4spMH3cIOkqRf_dE18I5PkXY9mZvwdZK3Edzom0CX_ftJsq6eUcbdkK5dY9R-4mQx96mOI1PMB3tT45A04cNCNdGcBZI5ytlResEY_NVnrYXZlv0fFtdJ3LDyIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو یکی از کشورهای آمریکایی پلیس به یه زن مشکوک میشه که ازش اسلحه بگیره. تهش طی تحقیقات زیاد متوجه میشن اسلحه رو تو واژن خودش مخفی کرده و با تهدید پلیس مجبور‌ به تحویل میشه
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65909" target="_blank">📅 11:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65908">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
خبرگزاری حکومتی مهر:
جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا
جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا منتشر شد. این تفاهم شامل تعهد آمریکا به رفع تحریم ها، خروج نیروهایش از اطراف ایران، رفع محاصره دریایی، بازگشایی تنگه هرمز، لغو تحریم های نفتی، و پول های بلوکه شده ایران است.  آمریکا موظف است طرح بازسازی اقتصاد ایران را ارائه دهد و در حالی مذاکره نهایی میان دو کشور باید در مسایل هسته ای و اقتصادی انجام شود، بدون بحث درباره برنامه موشکی ایران. این پیش‌نویس نیازمند نهایی شدن در نهادهای مربوطه است
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65908" target="_blank">📅 11:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65907">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
باراک راوید:
یک دیپلمات از یکی از کشورهای میانجی که بندهای متن فعلی را با من بررسی کرد، گفت که «ایالات متحده و ایران در مورد متن توافق به توافق رسیده‌اند»، اما اذعان کرد که هنوز تأیید نهایی لازم است. با این حال، هواپیماهای نیروی هوایی ایالات متحده دیشب با تجهیزاتی به مقصد اروپا به پرواز درآمدند تا برای احتمال سفر معاون رئیس جمهور ونس به مراسم امضای توافق در ژنو در روزهای آینده آماده شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65907" target="_blank">📅 10:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65906">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
⭕️
توافق قریب‌الوقوع جمهوری اسلامی و آمریکا بزودی در ژنو امضا خواهد شد و به‌نام توافق "اسلام‌آباد" نامگذاری می‌شود. طی این توافق یک آتش‌بس ۶۰ روزه که لبنان هم شامل شود، شکل گرفته و ایران می‌تواند با پول‌های بلوکه‌شده خود کالاهای بشردوستانه تهیه کند
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65906" target="_blank">📅 10:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65905">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/215d29fff2.mp4?token=F7Vb8v0R2MSOlpEkww5Awv4RG0R9cGA-WAaFazD39S4M8WxK9IxKfJ5mKDgICz6AytJHjY1KDC8qeUppps98t7NJ9NNBvw1Qztj3_BBmDsyi_b1ugLj5Y_uSJincXmB2D6cf0Pma8rrJ_lvb9KgjViAIro8f5WT78xwheSh3KF6UEhKkJ1aoxcydE5-1ifcHDg1UJA87MGoxLMXWxHJXOZyUcW5tAarBY6SM8h5GH8RdcVh6hrSzSU2AEQ65ZjgeyNRX2bFdGuS6pbfu4RVfLog3z5xS2rs4TUSnGjNxkrRBcYDotTORnM3T9GJyK6Y_jX8yZHVHVAO6jE0uuXYjmpJpaaTyvNDFYKo7tvX7CX1eh2kxVkAYpSMAKbDY3uGMU9VKHM29V3DaqNuEo1Jf97vRZUMYn5BV4uywbtdMZyG8x6zRPcgXFi7mAkRLfw2etb9YGaxdSKUMAJ49yr0TPXAvTllzz5Ldzd9l01PMVwtRFFShgZIs_vtFgmli4vsZM9K4UiaIHKYIO3zJRfUlyLb41-GwykiKGXWbsqNFQg1BKFH_5vFVbMnXriwn14PhGJt5EEDXOXn7n61fgJ3pu8-1JJg9Z8rJFmF_9stFHrtXI9GsTQOzbPBpQo9HsAKZ1qlDIFIFVOgO0ICSjF2gRPK6eD1ZDfhZkrzqX_5ZE8o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/215d29fff2.mp4?token=F7Vb8v0R2MSOlpEkww5Awv4RG0R9cGA-WAaFazD39S4M8WxK9IxKfJ5mKDgICz6AytJHjY1KDC8qeUppps98t7NJ9NNBvw1Qztj3_BBmDsyi_b1ugLj5Y_uSJincXmB2D6cf0Pma8rrJ_lvb9KgjViAIro8f5WT78xwheSh3KF6UEhKkJ1aoxcydE5-1ifcHDg1UJA87MGoxLMXWxHJXOZyUcW5tAarBY6SM8h5GH8RdcVh6hrSzSU2AEQ65ZjgeyNRX2bFdGuS6pbfu4RVfLog3z5xS2rs4TUSnGjNxkrRBcYDotTORnM3T9GJyK6Y_jX8yZHVHVAO6jE0uuXYjmpJpaaTyvNDFYKo7tvX7CX1eh2kxVkAYpSMAKbDY3uGMU9VKHM29V3DaqNuEo1Jf97vRZUMYn5BV4uywbtdMZyG8x6zRPcgXFi7mAkRLfw2etb9YGaxdSKUMAJ49yr0TPXAvTllzz5Ldzd9l01PMVwtRFFShgZIs_vtFgmli4vsZM9K4UiaIHKYIO3zJRfUlyLb41-GwykiKGXWbsqNFQg1BKFH_5vFVbMnXriwn14PhGJt5EEDXOXn7n61fgJ3pu8-1JJg9Z8rJFmF_9stFHrtXI9GsTQOzbPBpQo9HsAKZ1qlDIFIFVOgO0ICSjF2gRPK6eD1ZDfhZkrzqX_5ZE8o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه خبر:
با صراحت میگویم بخش عمده ای از شروط ده‌گانه در توافق وجود ندارد
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65905" target="_blank">📅 09:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65904">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6afe375b.mp4?token=CyXbSpaWrCtasIcZh2DDzRBRXfnyFQWdG1-c4EABXSPkAsConqZskmWAVlH4vLGlwXA-UJTo7pEkOcCn2zwJqMsO_jl-fo9GIT_kDJawCm_Mm8qLTVOADlP19wLPxQ8n4UhaL3o67AaUf4ee9L0sa00b36DOL2aRmizomgXe0wmrvXZ61zah7UYcxVZpjvrgOlCwQOksJpmPFXb0EnbqIdsFJ3UXX-WZ1ScIwjF4znCZICk41i10YZPotSMVzcYc7eTB6BxXdGAdd_wepkxMLGPu5uAAOm9jWcb-yJstDfl0bu-8ttYOh9OMW9ayR05a5otPBE5_zdFNS8qDFUxXPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6afe375b.mp4?token=CyXbSpaWrCtasIcZh2DDzRBRXfnyFQWdG1-c4EABXSPkAsConqZskmWAVlH4vLGlwXA-UJTo7pEkOcCn2zwJqMsO_jl-fo9GIT_kDJawCm_Mm8qLTVOADlP19wLPxQ8n4UhaL3o67AaUf4ee9L0sa00b36DOL2aRmizomgXe0wmrvXZ61zah7UYcxVZpjvrgOlCwQOksJpmPFXb0EnbqIdsFJ3UXX-WZ1ScIwjF4znCZICk41i10YZPotSMVzcYc7eTB6BxXdGAdd_wepkxMLGPu5uAAOm9jWcb-yJstDfl0bu-8ttYOh9OMW9ayR05a5otPBE5_zdFNS8qDFUxXPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گفته شده ترامپ بعد دیدن این ویدیو تصمیم گرفته که توافق کنه
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65904" target="_blank">📅 09:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65903">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRCYDtV5O8L5Q6I2RWtWBTIJFo2nvH5Ux2bOUOGlLXgrIHfGr6VXZ6XgYiHxkAG4JRJhODxhEv4X3MHtJbYvhtsQSXjczqj1YUUXJz6lUBKdK-hmb-Q60ZYalBb8Rg7CMd9Pow5__WqmdKFa_2Rf96-ghoXUT-Ke6MzYRz3ncDQ5NjbhCrCd3B30I2ZfWNyfxQdCdRTKml8FZPVrmG1eHTfnNuGqRGZgYAxtDpjmETVR6rJvODrIfRAky0_rilLCjnHIYD4f0W0bDAuA1h4tCwVbyB5aNFEkZTnGOL9Ter8TLFWKRoxzg5FeKjdkib4cpIoTSEnDD8HVJMJuRb4-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک لوین:
اگر همه این دولت‌ها با این توافق موافقت کرده‌اند، شگفت‌انگیز است که چگونه همه این دولت‌ها به این سرعت امضا کردند در حالی که ما اعلام می‌کردیم که در اسرع وقت بمباران خواهیم کرد.از آنجایی که این توافق انجام شده است، آیا می‌توانیم آن را ببینیم؟
در این توافق چه چیزی هست؟میتوانیم آن را ببینیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65903" target="_blank">📅 04:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65902">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4jx-bRXTBSzfgU3HVzi7q3zd5vrqaxDTPaZgeP4zbvyIscHPm8gU9HYHLuwuyEnHKOY_rSc20KlrF9nE4oGBr7rZWFMV5BujG-CX1VV-jCcGPOs1CDNCGMWofuLMum-odAYjj20wu4w_mS7qJhDLcvj9Jr43uNNLoBSIKVI4KjDGLWUm1yvB0Q1RPV71AH0a6g_uWM3WT2uby-CdkqBSug1h05GU0K13JpJ5xRkdu6orR_BcZ2M9HyMVn-VIvSGacf-fNKzmUYgAsjLhrfva-uAWhXNO5J8WZZpP0w0zl6na8-VS-v_3Fj_qj8hToFNbWckGE0ujXARUcfL8y3czQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دقایقی پیش زلزله ۳/۱ ریشتر در پردیس تهران به‌ وقوع پیوست
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65902" target="_blank">📅 04:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65901">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
رئیس‌جمهور ترامپ درباره ایران:
ما با ایران توافق کردیم. معامله بزرگی انجام دادیم. هیچ سلاح هسته‌ای وجود نخواهد داشت.
مردم خیلی زود به خانه‌هایشان بازخواهند گشت. تقریباً همه چیز تکمیل شده است. ما هر آنچه می‌خواستیم را به دست آوردیم.
نکته مهم این است که هیچ سلاح هسته‌ای در ایران وجود نخواهد داشت. یعنی نه توسعه یافته و نه خریداری شده.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65901" target="_blank">📅 03:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65899">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78687e07ef.mp4?token=GeS1-ozcAI1hLPc6p77TydleoffI73t3ZDFHYI-wmlZN3orvH1llyoa9mslxuKIfo_4uQyG7Oqkjuo2Nvp5GxtRtbD13iEcVx8YaGs--k6oJIChbTAUAqv9vSEF-gag4u7XGBCXWtW1szAQXp5YRphr79N5kbKD93g2cA_dZ3GfDWc6aCWVmLvkctM2siZmPznYUGVTWU6FVs-hHZk3OdZkkSXt-T8z3LhqHLMPSDl4Jqt7hn48wXgOvcI_o2o2iUkSvpltDxcFXTyUqFfqD4g3ZG1-m_85Msu1rur5Y_9Y1CsLdNdUB94HM8_wIpr3ZkBV27MiKVCzYX0pDauBhlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78687e07ef.mp4?token=GeS1-ozcAI1hLPc6p77TydleoffI73t3ZDFHYI-wmlZN3orvH1llyoa9mslxuKIfo_4uQyG7Oqkjuo2Nvp5GxtRtbD13iEcVx8YaGs--k6oJIChbTAUAqv9vSEF-gag4u7XGBCXWtW1szAQXp5YRphr79N5kbKD93g2cA_dZ3GfDWc6aCWVmLvkctM2siZmPznYUGVTWU6FVs-hHZk3OdZkkSXt-T8z3LhqHLMPSDl4Jqt7hn48wXgOvcI_o2o2iUkSvpltDxcFXTyUqFfqD4g3ZG1-m_85Msu1rur5Y_9Y1CsLdNdUB94HM8_wIpr3ZkBV27MiKVCzYX0pDauBhlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ درباره ایران:
امروز جنگ با ایران را به پایان رساندیم و آنها موافقت کردند که هرگز سلاح هسته‌ای نداشته باشند، چیزی که ما بر آن تأکید داشتیم. این هدف اصلی بود. این ۹۵٪ از موضوع بود و آنها این کار را به قدرتمندترین شکل ممکن انجام دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65899" target="_blank">📅 03:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65898">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65898" target="_blank">📅 01:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65897">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MotJEqai5VfqYijov1SFbiDuxTSZIWtA8OjucqOnjtMGHn-0uweTb9TGWEUEuspxsbUJeXJRSCfjzBlyfTJ3_kZ8epTPqOhD0GBBqAnGek_v8FH4D3GsmVLfiFRlvwKM51O0JdCLmcxjlmMRGCIwvN4_3dX0sAQayO131Yw77_YjC23aM3WcV7KAN3Zs_olAnmVL8eyhsNr9RcEuXuj3Ga3YCSxMmFLBKQes4JKMU-z8EJ62TV2CbN5Bcm_LymYEKiuaEM_DOQg-gPgkBePJkf_0DsZqsMjRlPm2XeJc2n7C5dzrC29AMklX9VqMyfK2zZGRZv337kWuCDNCZe7a-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65897" target="_blank">📅 01:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65896">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
صداوسیما:
شنیده شدن صدای دو انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65896" target="_blank">📅 01:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65895">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSvkumHxuEv8XxuPhMSGvGezs7fsNYbnNzWKg8Id7wqsG5FqRIA_Nz4wik25arON4ouHPA4AcFTlNVZaxmLscld-Y3rBu5ShZzK_Z4pJmVs3iWtJmi6_p5yJLpse0stiL-b2T9jruM7KZTzRh6P0JFZhh1sVSRGD-chbvHhRZ4UvnYr2NuK_aU3WLHQbUxY82jsHG6N-rMwry84qnyX9c2OBLcEmWIkIcFDo6FkqXYfY-G8L7OtsMjQjfvXZ9eOYuWEy5VSTUqAPnPxMSRh4zpu4Buuk3gP0Vi4PpNSRELah54zJvS8FMicJnCJdLi48uJXX84AnYe6qzIwGZsWyWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اعلام کد اضطراری یک F35 در آسمان امارات
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65895" target="_blank">📅 01:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65894">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دیگه نمی‌زنن
😭
#hjAly‌</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65894" target="_blank">📅 01:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65893">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
فعالیت سوخت رسان های آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65893" target="_blank">📅 01:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65892">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
مهر:
هنوز از ماهیت و علت این انفجار اطلاعات دقیقی در دست نیست، اما با توجه به دستورالعمل‌های مربوط به بسته بودن تنگه هرمز، این وضعیت احتمالی می‌تواند در همین راستا باشد
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65892" target="_blank">📅 01:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65891">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
گزارش هایی تایید نشده از انفجار در گناوه
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65891" target="_blank">📅 01:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65890">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
منابع محلی در سیریک صدای انفجار شنیده اند اما هنوز علت این انفجار ها مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65890" target="_blank">📅 00:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65889">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvznYP9KZsS7Ng2Cox_Xxsfxa0lMMzqihRLyBoY9cST_NL0sAUGBCjevfRKqAot6tiwTUuJkeEmgTsmUkgzWPWNuRHMMeJRY7McXWq44SNQF6wJ86iBVVkhG8Imqdmr-oqQ44ooSwrw5WdNWxa4WRLpfFVbduhKm9OKQO4Z41n7cxiIo_UYea0hXoh2bI6je-wvlt2_TddePxZn-JV-eF-qjcTgkHt11gqAGtbwdP_UHFev6NITYlQDJXBydLVioL7w_ilhqI-qdumWksNN5W0mFqqB0tdcWxHCPdLE6NxJGhSiIbMzsm3EidbkUgwmbezE7UanUoT4pClOVB2595g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💥
تنها یک پست از ترامپ امروز 1.3 تریلیون دلار به ارزش بازار سهام ایالات متحده اضافه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65889" target="_blank">📅 00:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65888">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐀𝐌𝐈𝐑 𝐌𝐀𝐒𝐎𝐔𝐃</strong></div>
<div class="tg-text">الان یعنی با قاتل
حضرت سید علی خامنه‌ای
💔
، قاتل خانواده‌ی رهبر جدیدمون
💔
قاتل سردار سلیمانی
💔
، قاتل سید مقاومت حسن نصرالله
💔
، قاتل شهید فقید اسماعیل هنیه
💔
، قاتل دانشمندمون محسن فخری‌زاده
💔
، قاتل سردار حسین سلامی
💔
، قاتل سردار محمد باقری غلامعلی رشید
💔
، قاتل سردار موشکیمون امیرعلی حاجی‌زاده
💔
، قاتل شهید فریدون عباسی
💔
، قاتل شهیپ محمدمهدی طهرانچی
💔
، قاتل سرلشکر شهید احمدرضا ذوالفقاری
💔
، قاتل سید امیرحسین فقهی
💔
، قاتل شهید اکبر مطلبی‌زاده
💔
، قاتل سردار سرافراز عزیزمون علی شمخانی
💔
، قاتل فرمانده بی‌بدیلمون محمد پاکپور
💔
، قاتل سرلشکر عبدالرحیم موسوی
💔
، قاتل سرتیپ عزیز نصیری‌زاده
💔
، قاتل عزیز اطلاعاتیمون اسماعیل خطیب
💔
، قاتل شهیدان غلامرضا سلیمانی
💔
و مجید خادمی
💔
، قاتل سردار سرافرازی که بر بستن تنگه اصرار داشت یعنی شهید علیرضا تنگسیری
💔
، قاتل رئیس جمهور آینده شهید بزرگوار علی لاریجانی
💔
، و قاتل شهیدان دیگر مانند محمد کاظمی
💔
، حسن محقق
💔
، داوود شیخیان
💔
، محمدباقر طاهرپور
💔
، بهنام رضایی
💔
، اسماعیل احمدی
💔
، علی‌محمد نائینی
💔
، مهدی رستمی شمستان
💔
، سعید برجی
💔
و منصور صفارپور
💔
توافق کردن؟</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65888" target="_blank">📅 00:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65887">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما به نقل از سخنگوی وزارت خارجه:
قطر و پاکستان به‌عنوان میانجی‌ها فعال هستند
وضعیت مذاکرات از ابتدا برای ما روشن بود و بخش عمده متن نهایی شده بود اما آمریکایی ها مواضع خود را تغییر می دادند.
ایران ثابت کرده است که در آنچه را به عنوان خط قرمز معین کرده است مماشاتی ندارد.
مواردی که درباره توافق مطرح می‌شود گمانه‌زنی است و موضوعی نهایی نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65887" target="_blank">📅 23:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65886">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjJowvuPbqZzIp7vYTKfcmvkzlF3fuvgUZZgRbqk2uTc9tpb_8YBQJcrEu3XWorsjExY5qh56GO0YByOJz-7RSL7_fXab_GP6ztYrzU6JGGGhbFDIi-ZkBU7sTCv9IT6nXc6KBt0YePloVQ41r9H5k09GnNVlnihJw3tHv5A2RYfHPFLHhpFHg6hY2OqpZPxZjScpjO4SvyJ7hAoZYrGGdypvXuu7E_OSjgJdnE25gtj8UCFHo52UO5rEN-qsCu8JOJNnwFZSDE61EjFJc3LTD-3WAumqNGv1Fe1QlwcFKP8IFRBn8Zid6bKGEBk50KZn3pvUtCKPlg-11VTVV4R9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
دفتر نتانیاهو:   رئیس جمهور ترامپ با نخست وزیر نتانیاهو در مورد نهایی شدن یادداشت تفاهم با ایران برای ورود به مذاکرات صحبت کرد. اگرچه اسرائیل طرف این یادداشت تفاهم نیست،نخست وزیر از تعهد رئیس جمهور ترامپ برای اطمینان از اینکه توافق نهایی که در پایان مذاکرات…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65886" target="_blank">📅 23:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65885">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:  رهبر جمهوری اسلامی با امضای یک توافق موافقت کرده.  @News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65885" target="_blank">📅 23:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65884">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
دفتر نتانیاهو:
رئیس جمهور ترامپ با نخست وزیر نتانیاهو در مورد نهایی شدن یادداشت تفاهم با ایران برای ورود به مذاکرات صحبت کرد.
اگرچه اسرائیل طرف این یادداشت تفاهم نیست،نخست وزیر از تعهد رئیس جمهور ترامپ برای اطمینان از اینکه توافق نهایی که در پایان مذاکرات شامل حذف مواد غنی شده،برچیدن زیرساخت‌های غنی سازی،محدودیت تولید و برد موشک و توقف حمایت ایران از گروه‌های تروریستی وابسته به آن در منطقه باشد، ابراز قدردانی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65884" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65883">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: بعد از توافق سریع محاصره رو بر می‌دارم
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65883" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65882">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
رهبر جمهوری اسلامی با امضای یک توافق موافقت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65882" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65881">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛ نورالدین الدغیر خبرنگار الجزیره در تهران:
دیگر همه چیز قطعی و تمام شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65881" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65880">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇷
#فوووری: ترامپ: به من اطلاع داده‌اند که رهبر ایران توافق صلح را تایید کرده است  @News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65880" target="_blank">📅 23:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65879">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/352ca9d87d.mp4?token=q7AbB7tuij9_5Pk3wlQkHwxa5UOu4-15LqtqfFaNUjMz_Qs6lHFR6zf62wxRVcR1lobb1nY426Y1H0ZmKkqRYQ500tVqxrCZ_WkgzvI1oPjs1Q3kL2CpU35hY8swGHya8PeGkgmQ-H506vr5_Owd67BDgybIZAbjwnrwVzLdWjSXDSTWXa5zJ63nMA9qaPmd7yn1z5FiHLzuNkGTsHCZuimrXMOW93p0hi7ZfKsBF_FytriwDlRQjER53Vnd--LCCR-TEMzPASQDkzAu6wI0lp_HVSs6uD1OfRDlwR2jOox7KmbR6W0DQvlY5MPfafaDQI1LLivJnSbI7JRf9bQL9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/352ca9d87d.mp4?token=q7AbB7tuij9_5Pk3wlQkHwxa5UOu4-15LqtqfFaNUjMz_Qs6lHFR6zf62wxRVcR1lobb1nY426Y1H0ZmKkqRYQ500tVqxrCZ_WkgzvI1oPjs1Q3kL2CpU35hY8swGHya8PeGkgmQ-H506vr5_Owd67BDgybIZAbjwnrwVzLdWjSXDSTWXa5zJ63nMA9qaPmd7yn1z5FiHLzuNkGTsHCZuimrXMOW93p0hi7ZfKsBF_FytriwDlRQjER53Vnd--LCCR-TEMzPASQDkzAu6wI0lp_HVSs6uD1OfRDlwR2jOox7KmbR6W0DQvlY5MPfafaDQI1LLivJnSbI7JRf9bQL9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇷
#فوووری
: ترامپ: به من اطلاع داده‌اند که رهبر ایران توافق صلح را تایید کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65879" target="_blank">📅 23:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65878">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1ce54a8a4.mp4?token=WAhfvzzjs7IBo9r5dakJ-_N1HtRCItn3wRKtTBeUwAt7LGiVT1sXOE4UG_1wIqIg9mia8ws8Wbf9bfgiiCy74SAe-FPQQC1r0TfRMqmZt31t8A7s-dFj1lgWhiVWb74odR9h8RyV9Sg8R2HFF8rfklYqLsE2eTCfZgiwBvSgugV9IoM00aB5k0YCmjDyZiYPOtpTZ3ruM9y9oGhIDcRtbOMOFHej3tBP0Aruvc9_RnUlGlDyz1wWgsMsYlL-0yyIFnURsCLfOinS4MgNH_9ZBR8XxQmr98ja2y1S5u8CZ9FI7YGnw0fmoiP4VYLTUD2fWRqDQ-vRbDvw_9xMeoMPtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1ce54a8a4.mp4?token=WAhfvzzjs7IBo9r5dakJ-_N1HtRCItn3wRKtTBeUwAt7LGiVT1sXOE4UG_1wIqIg9mia8ws8Wbf9bfgiiCy74SAe-FPQQC1r0TfRMqmZt31t8A7s-dFj1lgWhiVWb74odR9h8RyV9Sg8R2HFF8rfklYqLsE2eTCfZgiwBvSgugV9IoM00aB5k0YCmjDyZiYPOtpTZ3ruM9y9oGhIDcRtbOMOFHej3tBP0Aruvc9_RnUlGlDyz1wWgsMsYlL-0yyIFnURsCLfOinS4MgNH_9ZBR8XxQmr98ja2y1S5u8CZ9FI7YGnw0fmoiP4VYLTUD2fWRqDQ-vRbDvw_9xMeoMPtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیرِ واشنگتن #hjAly‌</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65878" target="_blank">📅 23:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65877">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
منابع شبکه العربیه: طبق توافق، آمریکا تحریم‌ها را کاهش می‌دهد و محاصره را برمی‌دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65877" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65876">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MomvYnj_x1KRGqzVPIqd16LnY7eXIuGNNHby1-2RH4KovdMKfAZmIrQqzZwh_6GMpO-zRg8mXi0e0GVqXM6wAElUkUhU1vMLGatKfH9XO2KrRLoJJM0sBC8P74SByEBB3UGQPoZOZKmuvuXvQrur72dnntqWOrhps_cVuSXYZhaxhPG3DfaZf-h5RAvQWEL-RzM3OBEQiWSm1E2Cohk3ahI8R3nnQkkeqr18j8PjQybrt98fU7EpxmcevdQbTd1bioxdqhsmkXuh5drrNh-qDlT3Lj5_qXmB0_rbxAXZi5UCBTagp8t-91VL5ux7OmTGIL5_tuEttTPoMKRhS1VIWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیرِ واشنگتن
#hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65876" target="_blank">📅 23:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65875">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e445beba9.mp4?token=d0mGiZfpEhEbQ1GHhwTmgry4Ax_pxTsrTN1K80u1hDjBMghMR2jGJ0tQJrdRbz_QuWYF7FhYJyUJdYABrFDKhNfkM4NcP8KD1ZCMTiHwhnYDa4npiAh3E4aVhZLZxenJUEJDeBRX13OQ-IzM19y-1sBuhhmjKJuzL7IZpt5svdCg8u22j7rOXq9zWd1QjtxXPJrAK7A5KFEMXItIqPoGRaVLyC1bcClewgc4tLLOLlJDL9vePCTjJUAJ8m-Ugqnv_4xCV5HS71s-lyh707-AlJCOBAklO7TIOnKUmpa1JKa2FfvJxU_l1gE3x7jK-uSK1Jd8-sQB4KU5w6tzpoaFqwsDfVepFrNTm0hpIuIveaVh_qL5i93EfEkxxBEWtmG3RCcedE_ZJIw7fnqPMYNMPKyhszLXy9_c9bfsChq1FytFn2B4BKKUiIuWis-doIHulMBxeINenHyfadnRg-kFmD89MaGj6u1ooqtt2wNNhkFHptiel_aJE0Wz1CBxb2KED1zHHvvADEaPegYNbS3-kwmpwSoYaBNbiWOzuOy547OCvjGIZJnVWDTdI-cb8Nddu52XNA7d4zcj7atoLib7KoYdzkYybAt5MYGvEhWDVZdl5aSxwctmLUOgNe2NtrHxyT0TD6ZLT02WSN0zB-BsEepbgOouBzRCfcHBcD7IjBU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e445beba9.mp4?token=d0mGiZfpEhEbQ1GHhwTmgry4Ax_pxTsrTN1K80u1hDjBMghMR2jGJ0tQJrdRbz_QuWYF7FhYJyUJdYABrFDKhNfkM4NcP8KD1ZCMTiHwhnYDa4npiAh3E4aVhZLZxenJUEJDeBRX13OQ-IzM19y-1sBuhhmjKJuzL7IZpt5svdCg8u22j7rOXq9zWd1QjtxXPJrAK7A5KFEMXItIqPoGRaVLyC1bcClewgc4tLLOLlJDL9vePCTjJUAJ8m-Ugqnv_4xCV5HS71s-lyh707-AlJCOBAklO7TIOnKUmpa1JKa2FfvJxU_l1gE3x7jK-uSK1Jd8-sQB4KU5w6tzpoaFqwsDfVepFrNTm0hpIuIveaVh_qL5i93EfEkxxBEWtmG3RCcedE_ZJIw7fnqPMYNMPKyhszLXy9_c9bfsChq1FytFn2B4BKKUiIuWis-doIHulMBxeINenHyfadnRg-kFmD89MaGj6u1ooqtt2wNNhkFHptiel_aJE0Wz1CBxb2KED1zHHvvADEaPegYNbS3-kwmpwSoYaBNbiWOzuOy547OCvjGIZJnVWDTdI-cb8Nddu52XNA7d4zcj7atoLib7KoYdzkYybAt5MYGvEhWDVZdl5aSxwctmLUOgNe2NtrHxyT0TD6ZLT02WSN0zB-BsEepbgOouBzRCfcHBcD7IjBU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره جمهوري اسلامي:
ما توافقی داریم که ایران هرگز سلاح هسته‌ای نخواهد داشت، که این کل هدفی بود که باید از آن عبور کنیم تا به این برسیم.
اما ما به زودی امضایی داریم و اسناد تقریباً در شکل نهایی هستند. بنابراین خواهیم دید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65875" target="_blank">📅 23:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65874">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
دونالد ترامپ: در مراسم امضای توافق حضور نخواهم داشت و جی‌دی‌ونس قرار است عازم اروپا شود  @News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65874" target="_blank">📅 23:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65873">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLyiPIJAbKi3yGSGUyItLUbyNo3wP8uvzUec4pm8mVZFJN9MIFx_WhwvgOCz0elXKVbQWP-B8EYU1XslZg469tAEpcPbU1moRxT2glTsWow6NxeviM6_jpN6_hQKvSds19tE6gzLjg1VLZzIaCuaGDVVHdMiff15thqv21L2XDSWlrm2LndPz0Hfev-gGxOvaMbU3rVA1t0QVGfYBeUDonH89OJNJ17NbJP3gt863gzxmZT5eKmdN4rPFp9zGr1bIBaoo7WtURJdjFzJtCN2SefJGj389t22fhFH4A-t57sMbOsOjsZ56sn3oleKMDo69iUu9U7FJERZrBemqHopwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آره داش آخوند های حرومی تسلیم شدند هفته دیگه جشن آزادیه
🤡
🤡
🤡
#hjAly‌</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65873" target="_blank">📅 23:06 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
