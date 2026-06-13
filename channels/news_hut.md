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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 03:43:59</div>
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
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/news_hut/65977" target="_blank">📅 01:17 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/news_hut/65976" target="_blank">📅 01:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65975">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0jP8KhJBZRBxIWgiJCitIPGFLP1A9AO8jynkDDCSVgV8j6QEfrybIKGBqn1MBCRLyrKS8_WqulIOKYADns8JVNTcS4TP56dBz0MgEMYnVQdo6fWrPpqdwJ9oCLmryC-rNaaAYk4qS579jr6LDGo3YecILyhoWeytbj2FvLavakmXv4ESif9FVP2RUqMV5KvwIYSRbpD2o4ATfuxGEMS7KNHI3HHinu8423YBwMbd7CeAt9OkgMFpTb8apXKn1arYacMYYcBMLsCeyla6a4LvFmJ8vFlrHJywmygeI6hOMAJ6OmQbzW4-rf7Zy84HCtclyDSNtWEZK6fJnobXyTDvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تندروها گرفتن رو قالیباف
😂
@News_Hut</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/news_hut/65975" target="_blank">📅 01:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65974">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
سپاه:
کشتی هایی سعی کردند بدون مجوز از تنگه هرمز عبور کنند و مورد هدف قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/news_hut/65974" target="_blank">📅 01:06 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/news_hut/65973" target="_blank">📅 01:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65972">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
نایا خبرگزاری عراق: شنیده شدن صدای انفجار در قشم و سیریک  @News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/65972" target="_blank">📅 00:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65971">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
نایا خبرگزاری عراق: شنیده شدن صدای انفجار در قشم و سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/65971" target="_blank">📅 00:21 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/65970" target="_blank">📅 00:20 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65969" target="_blank">📅 23:24 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65968" target="_blank">📅 23:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65967">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
عراقچی:
به زودی ایران و عمان بیانیه ای مشترک در رابطه با تنگه هرمز منتشر خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65967" target="_blank">📅 23:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65966">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
عراقچی:
به طور قطع تنگه هرمز به شرایط قبل از جنگ باز نخواهد گشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65966" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65965">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
عراقچی:
پایان جنگ در توافق همچنین به معنای خروج اسرائیل از مناطق اشغالی در جنوب لبنان است و ما این موضوع را صراحتاً به طرف مقابل اعلام کرده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65965" target="_blank">📅 23:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65964">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmhRk2NC8w0HBaCKgdLjcWuyfGqYriB3tPF6FXi0uivKzx_1EVxIycVlmv8z4fZHQi4GktOAatiV8OkmaQrPnzlcuFg4nfLVQq3nE4-V6HNVRxRWUrU5uPvfey6nJg9sCojtxkoN-fZbQo3Iai58TMF10TaNpEge0DWXJr_55WCBVABYV8N_xqCvCUcmV5tpNAZ7MsoevIwWbTq6fwKf7O4S8AssDYUrccrlcBlP1OeJHpve7wz0rLHY18w-fkscBOjXiAwspL30XFp2QFYv3F4291X71wbV2v43VLXurAe4XNL-a0Xfv-B5iP6wg8rpnquGQ9ZkyOxxgGtfMyugGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
تعهداتی که داده شده باید حفظ شود. نه اگر و نه اما و نه بهانه‌ای. برای معامله نزدیک پیش رو، راه دیگری وجود ندارد.
هر چه بکاری، همان را درو می‌کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65964" target="_blank">📅 22:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65963">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‌
🚨
🚨
عراقچی:
نتیجهٔ تفاهم یک یادداشت ۱۴ ماده‌ای است و وقتی نهایی شد تک‌تک آن را به مردم می‌گوییم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65963" target="_blank">📅 22:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65962">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
عراقچی:
ما پیروز میدان هستیم؛ مقامات خارجی به من می‌گویند که ایران را این‌گونه نشناخته بودند و ایرانی‌ها شگفتی آفریدند و با قدرت بیشتری از جنگ بیرون آمدند
من می‌توانم اسم ببرم که کدام مقامات این حرف‌ها را زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65962" target="_blank">📅 22:42 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65961" target="_blank">📅 22:39 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65960" target="_blank">📅 22:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65959">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
عراقچی:
دشمن تصور می‌کرد که بعد از جنگ ۱۲ روزه، در جنگ ۴۰ روزه می‌تواند ایران را تسلیم کند اما با مقاومت جانانهٔ مردم و نیروهای مسلح ایران مواجه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65959" target="_blank">📅 22:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65958">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
#فوری: طبق اعلام زیرنویس شبکه خبر ، عراقچی تا دقایقی دیگر مهمان این شبکه خواهد بود  @News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65958" target="_blank">📅 22:32 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65957" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/65956" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65955">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9YbW_w_xK9D19ZQEzwyPHp10TFfoRC6lefA9yimeBGGuYYje8V2mRVw0MfFXcLA23P1uxoXyymuX_vZcef39IbvHrEy7Ks9DOBmBmGJionTkGM8BioxKLRK9UDS1uh300r2s24NACLhf0sLqNQlC1Gexie5NcW-kK6dBs88ZRIXMfJoGYot3Rz-XKd6D_QbA43cFteF48PpGpl6WSpNePchxpe3KGDQbboQ2lu77iPyI104u3yzdvTx0jrIygXCMl52glDJzM0COt1NfrCaAmwdv3EpXUInpjJKMsqzYzf9YWbOj-Nfeu0PnIBS37fcvwPdUtWZIbMR1Fxtn6FFFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65955" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65954">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
کانال 12 اسرائیل :
توافق قطعی است و این به نتانیاهو اعلام شده.
ترامپ از ایران خواسته به صورت علنی درباره توافق شفاف سازی کنه و هشدار داده انجام ندادن این کار پیامد هایی رو به همراه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65954" target="_blank">📅 22:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65953">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
رویترز: امارات ۳ میلیارد دلار از دارایی های ایران را آزاد و به آنها تحویل داده، این اقدام تضمینی بوده در ازای اینکه دیگر به این کشور حمله نشود
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65953" target="_blank">📅 22:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65952">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nu8yG4rUfCx3YntLOhRAuriJw0rk3t2jNg1lrEcuKk7A1NVpMUA9xY256ZL22-3nPRxwOso5CeHtHEuXZ68vmclhbwMWNZHPuowjTRNUVwG5SB105cvKr055z2rMuPwNtUQMJcVpb-VYUfquNQ6lYeXI8ExlmMZJV-T7trpWpMk4JjJ-bGVv9yshvqt8LLMngedI6llDD-64mNEn8ATWRKO6rCY8KgjEH7aE4tBlHlvVF1L0pIk8fGGg6FZJ7tAUEqncAQdMUcL-rm_BcR7UTqk6cV1id3oMsFvK0KXWiWRohiYWKDr6cmuxMsWrPhvPiJaUUE6BHEc_rTsVGXFlsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#
فوری
: طبق اعلام زیرنویس شبکه خبر ، عراقچی تا دقایقی دیگر مهمان این شبکه خواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65952" target="_blank">📅 22:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65951">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmcFuz9GPyguD91iLSJ4l9vywYw3ANJ8rFLtYIsg-Vrqr32MAYE6mAzAvYFso7HcCDxFxUFFc_74kFnoxCJUSfgvVI_WytS7dC6O_Ir2ltZ2rBhuXROSbEaErTfKvLt6Kh3oXJ4aQOgusXt9xdB1ic5NUWNvX_RzeO9ibkuDpIRNQiYIL1c4t13z5gW8SqZ00WRdye6CVqMHmGKs5e6os6V-Hn9KteO2nAhTyZMQJXG3kDLeBXmLNFdVkRFGakagMS7L2U49JGtj1_qATkqNsJDIAIuKREdg-Fkzw0evnBaQHHogtNcBNTgl8muy7UF_3MWWfbKQOOr1eZJybg55fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا به شیرمردان سپاه اسلام و حضرت آیت‌الله العظمی سید شیرمردان حاج آقا مجتبی حسینی خامنه‌ای، خوب دارین کیر می‌کنید ترامپ زن کصه‌رو #hjAly‌</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65951" target="_blank">📅 21:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65950">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHlwQxF_Vqsl0YtcxnHNAFcKxJqJFawv5PT_fnMEMp3LkL8wCzMboNBay97cb-6yBWMdyUbgEpiu5MkS9Nee3c5iqQkmcWiMYCbBIMqrS3BNn57rG_R7rxDXeJiPoJjA4VZy2RYw10kTg6OoB29Rd-BsUq_k8V7OsIB0k8cnAyHqsjF2lbU5i-n4w92_-qcZJg6i2Swb__SIp3X2H8gt-6sHLFEGJZ7saapwTsSdprPzizuP4Yqvmp5dak1NW7-jg4PeZlwGmU3EA6Esgx2kxM9dS-sbHWiivBqGglpyLSPxTXcWC-BJEnQDO9p3ZBqKFvAgQAbjL4FF3gacP0e_zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ثابتی نماینده مجلس:
طبق اطلاعاتی که به دستم رسیده توافق احتمالی بدتر از برجام است.
نه احتمال جنگ را از بین میبرد و نه گشایش اقتصادی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65950" target="_blank">📅 21:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65949">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
الحدث:
وزیر خارجه پاکستان امشب عازم ژنو میشود
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65949" target="_blank">📅 21:15 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65948" target="_blank">📅 21:11 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65946" target="_blank">📅 21:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65945">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e7da6863b.mp4?token=OwWmCLLc4AgM7UpmtIunX8bROhMS8u68ZXnP-wD6VU6VndeNthNN5eMy1j6P5kTFRNWuBwhuv1HTGc_3gnSnzuwwACuqvCp8RR020P2tAn4maq4cq98vyVxisKstZd5xKyf_0fVvWWwdZhiv5VmE5BbU6kyBRYAOb2MvJTZsnWW8vkcxJxpZ8tgIK60E5gEBRfn82slejpnS21DeF4wTubNIdDS033jsQ_lb3TVthSjSPouH7p-IWGkr3AjSw3b8DQmTE6bmPvy1Eb2jw1G-WUoSxH4QSE4GwKM3ABNYE9Xx5HJEGhs-R7VZJvlufT4xfAzfjolCj7PRcqbSs0-Iag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e7da6863b.mp4?token=OwWmCLLc4AgM7UpmtIunX8bROhMS8u68ZXnP-wD6VU6VndeNthNN5eMy1j6P5kTFRNWuBwhuv1HTGc_3gnSnzuwwACuqvCp8RR020P2tAn4maq4cq98vyVxisKstZd5xKyf_0fVvWWwdZhiv5VmE5BbU6kyBRYAOb2MvJTZsnWW8vkcxJxpZ8tgIK60E5gEBRfn82slejpnS21DeF4wTubNIdDS033jsQ_lb3TVthSjSPouH7p-IWGkr3AjSw3b8DQmTE6bmPvy1Eb2jw1G-WUoSxH4QSE4GwKM3ABNYE9Xx5HJEGhs-R7VZJvlufT4xfAzfjolCj7PRcqbSs0-Iag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شهباز شریف:   در بحبوحه تلاش‌های میانجیگری فشرده پاکستان، ما کاملاً از کمپین بی‌وقفه اطلاعات نادرست که توسط کسانی که می‌خواهند توافق صلح را خراب کنند، به راه افتاده است، آگاه هستیم. گذشته از این سر و صداها، می‌توانیم تأیید کنیم که متن نهایی و مورد توافق…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/65945" target="_blank">📅 20:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65944">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVHpBXo4DLuq-qNomU3VvbYdzSRb1tZhkxwh_MJHwRlvTsqzD-Ieyqu4g7Rj0UJ7iqR6u9-4Bnge-gU74yhG1j6nXhzCWcWufchNP3a31A--ND8mL5cMaP6ZiBas8KFMIjMkHBi6lClZjH4Jkg_-U0dj9OIkRNnRaBcouQfukl1Xqp2ylg4hOrBRYuEObUUrYSKwqtafInP7YY3VzIr5iQ1iMUaAIpA-IfSbOGdDPgFwP2sxPRtbh96VHhw7Coi-zMnzLLO7oDM38HVGXmeA-D33yxMtcaYn2879REw1C1jJbROsgfqhm7ofDXsBXd9rue8IuzTi0-5OQDyscpYDFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهباز شریف:
در بحبوحه تلاش‌های میانجیگری فشرده پاکستان، ما کاملاً از کمپین بی‌وقفه اطلاعات نادرست که توسط کسانی که می‌خواهند توافق صلح را خراب کنند، به راه افتاده است، آگاه هستیم. گذشته از این سر و صداها، می‌توانیم تأیید کنیم که متن نهایی و مورد توافق توافق صلح حاصل شده است و پاکستان اکنون از نزدیک با هر دو طرف برای نهایی کردن مراحل بعدی همکاری می‌کند. صلح هرگز تا این حد نزدیک نبوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/65944" target="_blank">📅 20:40 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/65943" target="_blank">📅 20:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65942">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZ1RCzmTs-FcRd7mbFrTT4fCXp1uU67AiqEV5DWmiN9gse247_hFP_gaaYLX6gJNRaqq0Xt5rNswUgy3bF_mdipzVRwfc-ZOD0k9LRg_bM3czD2aYi_Hv_26GIzyel-Bdm2C-r4CCM2zS1g_xdrm6bjVShdmNlKRALSghs7b9XpT7ZElQjqFoiwV-Hm3tt08iHjaUBLBoSqD3BA_EMRqBk1hgEgk87T-oDnUGDRxwnL8kHr8PkM43-sFXlvCUNfo785bYQqE-KUjfdbj-oQvG34bKSAX4mgW11qlZZ3J9oRtXRmxRBdOg975n3MvhCx57y4_l_kKWFI0D2rJw4OmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندزی گراهام:
ایده یک صندوق بازسازی ۳۰۰ میلیارد دلاری، با توجه به اینکه چه کسی مسئول ایران است، به نظر می‌رسد بی‌معنی باشد. این شبیه طرح مارشال برای آلمان با وجود نازی‌ها در قدرت خواهد بود. آن زمان این ایده خوبی نبود و هر صندوق بازسازی که به نفع این رژیم تروریستی باشد، اکنون ایده خوبی نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/65942" target="_blank">📅 20:16 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65941" target="_blank">📅 20:16 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65940" target="_blank">📅 20:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65939">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oujOM9tE_s8MDhmD8jfsEjObMj-8P8jPbFTs2igpms3I5Blh7dAtEEWJfBStFjgFcc8qGIaoqoJqZAGdIHItVLx2mJ8liJR3NPCjYuqf0aBYap7fJ5KjiPjcyyE_RoNo10YvZdz9tpr2XdK2syhE-zUmyjNPtR-hUz2FeirxXT_K_0pXzRIqQq1-uDKrHyRE1KltYLHnuqJVdI7vpkqiIt6li5a34MBKy99EAdpLpPSVEP61TLlmdrUCvIIVsnNXtbH5aqJay8F-83foW1eSUQxDj3EdxvQoONgz7rE-Yw4rOsqxpcUdgW8GyTYrlgRieiXCfqPOHzvJPB0X2J3leg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سنتکام:
ناوهای جنگی و دارایی های هوایی نیروی دریایی ایالات متحده همچنان به گشت زنی در آب های منطقه ای ادامه میدهند و محاصره علیه ایران را اجرا میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65939" target="_blank">📅 19:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65937">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f3347ca6.mp4?token=gqrpGCYTwbHXr755tqNulWdTzXfMER1kiLuRhNZIMtazagw6oR6LmCuabAnL4TL2ZOsO1OWzELlGYXtdoAvg-qP0CUmsAVJ417kRcTBbvFdX9fiP31WRcDI4EZfHimUsRroU-3TqNTbg7ZjaIoXzq2a-m2wpuuRgERzOPdqHnOzDFysnjQ_FRvK833B9xEwYnanOlJyhkcwJyZq3Cnh2wALskWG6bfo0bxZnnssXlXXits7hQHzZT3Th8QkU8bDcYQlXhuUl1bJM-NAkwbkfD3WPALufCj_nRaN2Qy7YydbxvOeyUU2Q4MTnU8Ay1yrou_LdtEhgZldmle0P6PEemw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f3347ca6.mp4?token=gqrpGCYTwbHXr755tqNulWdTzXfMER1kiLuRhNZIMtazagw6oR6LmCuabAnL4TL2ZOsO1OWzELlGYXtdoAvg-qP0CUmsAVJ417kRcTBbvFdX9fiP31WRcDI4EZfHimUsRroU-3TqNTbg7ZjaIoXzq2a-m2wpuuRgERzOPdqHnOzDFysnjQ_FRvK833B9xEwYnanOlJyhkcwJyZq3Cnh2wALskWG6bfo0bxZnnssXlXXits7hQHzZT3Th8QkU8bDcYQlXhuUl1bJM-NAkwbkfD3WPALufCj_nRaN2Qy7YydbxvOeyUU2Q4MTnU8Ay1yrou_LdtEhgZldmle0P6PEemw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی قبل از جنگ ۱۲ روزه و ۴۰ روزه:
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65937" target="_blank">📅 19:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65936">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gI7shHJDCXge3eFqBHAw44OP0CHP8nphkjI2PKoSedoascBW7ZhHr8EvD4Yzq7YAituchejgRoJ634xGGBBiGInIhvc4kia_W2sVBI703P0DNxpdHnMTpbK22n2sLGWGg6AQHk-XCrshLTUcM8CAp3HhE0fw52JSqmqdXtfQHSJkn4tKgubrYMqyeizY1UuTFfZrlb6FlKDvpSgAyyVzRrBiZ55lnXNjVQFJdzPIZbD27FutIJBDdO3G76Vx5S0EOim-DiC8P8kBGAIR8JXlKp25dS0SGYrK7EatSbJ6CGVfj_AgK63wzYz52Wzm6s6mykRRpADpeQR8UjE8W4Rihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: تفاهم‌نامه اسلام‌آباد هرگز تا این حد نزدیک نبوده است. تا زمان نهایی شدن آن، رسانه‌ها باید از گمانه‌زنی در مورد محتوای آن خودداری کنند  @News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65936" target="_blank">📅 19:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65935">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
جی‌دی ونس:
اولاً، ایرانیان هیچ وجه نقدی دریافت نمی‌کنند و هیچ وجهی صرفاً برای امضای یک توافق یا حضور در یک جلسه آزاد نمی‌شود. این توافق به گونه‌ای طراحی شده است که نگرانی‌های ایالات متحده و متحدانش اولویت داشته باشد، و اگر جمهوری اسلامی ایران تعهدات خود را انجام دهد، فواید اقتصادی به آن‌ها و کل منطقه سرازیر خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65935" target="_blank">📅 18:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65934">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تا دیدن اعصاب ترامپ تخمی شده عراقچی یه توییت زد گفت رسانه ها چیزی در مورد جزئیات توافق نگید :)))) #hjAly‌</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65934" target="_blank">📅 18:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65933">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
ترامپ:   شرایطی که ایران به رسانه‌های دروغگو فاش کرده است هیچ ارتباطی با شرایط توافق شده کتبی ندارد. آنچه گفتند، از جمله بیانیه ضعیف و تأسف‌بارشان درباره وجود توافق، هیچ ربطی به حقیقت ندارد. افرادی بسیار ناصادق در برخورد با آنها هستند. هیچ چیزی به نام…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65933" target="_blank">📅 18:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65931">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-1pIGIJo-rT8sJOFp4Hs7pI16xzSVXV00i5qQgHMBS8qkuLVd-HmcyXz9lEFLl2RIwDKr-h9afFyEgaypFGBuF7095kucPw-kCpBeEq4PRLyzXAyEhOxUKD5piuBmhe-b3RGwhKMqW2_44EBFMVs-C4M-LlhEFddUhSLivNVq2f-lDlptBwKF3DXrMjDmwG7Wu7b_aWib5hMsowFpPW_WGskF84G2dWNXhk78IBzVAfodIC9iU0q-JAsn31UAcne1_xcB9vzYYi8IQUbyVKlkUC4s5lt9rbsQxFvRQp65kB7_c_ca54xKdSumYGMMweqL16Fi96KguEG5A4fMLC3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BjBx_i-GLaGVL2LBNDckhYKICMRP2Qi-y3sYKh0UtAV2q6B_IWZoiIPKfTdhB99R7MmMxo7TRVGJHiU9636egytmfQ7g5D2AWtAuXID4r6qQZ8LIq3PE7UlIg4mP3iVW-I-VvInFO3pwTXGs2_FVQ5vYlvP5tPPKp9hoR8POjDt2p9V_35YB3Tmi1KofEoDX2WqTX6XUUklCtlb--nLQKj8Fkg84t7MxvknlfXosBUhmBzNuqNyvCVwNZc1wVMgY9NNLuBQbosLz2nFyxfwd0V0LrFG9znLgZ4bBU-LdGFZVPYok3AZTEcxnOwgHBitDoFs4O_o6pYs1pcPYWO5cPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
برنامه امتحانات نهایی پایه های یازدهم و دوازدهم منتشر شد.
شروع امتحانات از ۱۳و۱۴تیر
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65931" target="_blank">📅 17:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65930">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c65a1f96.mp4?token=bi54Q0r-40p4gf0L6DxE39m3AmKCFhHrXZDu7NpsZjPb8cxtYxelRxqdqqq48uWwtwrXz1jAcy8AHPTaPuQNzXnHQX9WMX7G_Q_pYBbBTWOYIhbKM3i3YmmCj63sA519O9ktyvQlVNDQqU5XhsnjQpQt3QihJhLgm8HRVixwkOADnnxGxz46MsXuzF4Pt6TQ-h1T4qKJNM3kgKTGjYC6QhFGctC5twKFg1UrBIb_2cdWK6wLCUtg6PJeHKMqu-ogTkrKiuV0VtSG8JU8MPzBgZi71UCnY7dGt_wxvZmvZ9wEGl1FpEHOO-3cRL9DQ9TKEe8_V-MvIYJEMREf5a9Wzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c65a1f96.mp4?token=bi54Q0r-40p4gf0L6DxE39m3AmKCFhHrXZDu7NpsZjPb8cxtYxelRxqdqqq48uWwtwrXz1jAcy8AHPTaPuQNzXnHQX9WMX7G_Q_pYBbBTWOYIhbKM3i3YmmCj63sA519O9ktyvQlVNDQqU5XhsnjQpQt3QihJhLgm8HRVixwkOADnnxGxz46MsXuzF4Pt6TQ-h1T4qKJNM3kgKTGjYC6QhFGctC5twKFg1UrBIb_2cdWK6wLCUtg6PJeHKMqu-ogTkrKiuV0VtSG8JU8MPzBgZi71UCnY7dGt_wxvZmvZ9wEGl1FpEHOO-3cRL9DQ9TKEe8_V-MvIYJEMREf5a9Wzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین طهلیل ویدیویی بنده از شرایط خاص منطقه برای عزیزایی که تو دایرکت درخواست داشتن
🙏
🙏
🙏
#hjAly‌</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65930" target="_blank">📅 17:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65929">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6007e01a82.mp4?token=LCNmPyPZ68inCAezB_hgbPSsSn7ARWhMwrTr3Rtg9e6ywGJAdOFN1zKWY7hL6Bygte3ODEwz97kmJYSkjB3zWLe5qyr1kQ5kB_ovPBXUpiS8saGAgezLzfzN3v2uZEvU-Tf2PNL_hQRF5jfUPZ52kCCAf1Dfw_9nUXv4WXFts2D6h55cFihbyc7aC65O1RmZJc94nW1T5tc5ZXn0OHk72jyN2yLmHpDSlpZI1EKuaKmHKbFmkpOlAeiwNk6m4v0xXJ1cvbablB_BYS6ua65amahteEJK570WXp_nSBOgf2T5gDvepWhCtocV0x45VE3lTPVUOu5WXkMEtFGsv1d39Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6007e01a82.mp4?token=LCNmPyPZ68inCAezB_hgbPSsSn7ARWhMwrTr3Rtg9e6ywGJAdOFN1zKWY7hL6Bygte3ODEwz97kmJYSkjB3zWLe5qyr1kQ5kB_ovPBXUpiS8saGAgezLzfzN3v2uZEvU-Tf2PNL_hQRF5jfUPZ52kCCAf1Dfw_9nUXv4WXFts2D6h55cFihbyc7aC65O1RmZJc94nW1T5tc5ZXn0OHk72jyN2yLmHpDSlpZI1EKuaKmHKbFmkpOlAeiwNk6m4v0xXJ1cvbablB_BYS6ua65amahteEJK570WXp_nSBOgf2T5gDvepWhCtocV0x45VE3lTPVUOu5WXkMEtFGsv1d39Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه ای ۶سال قبل:
هیچ پیام مستقیمی برای ترامپ ندارم چون اون رو شایسته مبادله پیام هم نمیدونم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65929" target="_blank">📅 17:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65928">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
ترامپ:   شرایطی که ایران به رسانه‌های دروغگو فاش کرده است هیچ ارتباطی با شرایط توافق شده کتبی ندارد. آنچه گفتند، از جمله بیانیه ضعیف و تأسف‌بارشان درباره وجود توافق، هیچ ربطی به حقیقت ندارد. افرادی بسیار ناصادق در برخورد با آنها هستند. هیچ چیزی به نام…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65928" target="_blank">📅 17:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65927">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‼️
ایرنامتنی رو منتشر کرده و گفته تفاهم نامه پایان جنگ دربرگیرنده این مسائل و موضوعات است:  ۱. موضوع هسته‌ای دست‌نخورده باقی می‌ماند هیچ توافقی در مورد پرونده هسته‌ای در تفاهم‌نامه فعلی انجام نمی‌شود و ایران هیچ تعهد جدیدی نمی‌دهد. گفت‌وگوهای هسته‌ای در مهلت…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65927" target="_blank">📅 17:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65926">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIHWYavKfK2dpn_KAtmhBmvxkdh9_jEfWS9owfo-3w9llHp2HHN5P__KWstpc4f0mLL7MkSKf_GsLbIxdBUrqVkF_azrm8eMX1A2wzlT2PoLyXElar1nWwHZfsuEJbiLAxd0sDsKPs8VwnJNvJy58GjPBo9feMHUIZIT6wp02GKuVI9BjObIdIHvZhp3E2wZAmySW1sFwbyq1P2QdTP5u269By54ncgYggrprSA0IXHzqXzw7QV-BmuWdqLqEfyegb4XLgJan31yze0yuiv3rOIQvpU-qE6maXdHowdtlzN5djm_vaAOZp-HVx1hnqqZkNgPvs6XxwBNmGCVO9Fbpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پلاکاردی عجیب در تجمعات شبانه
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65926" target="_blank">📅 17:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65925">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8O85gzfOfB_QwOZZJYLz4-96inoB4bHiABek5V-7CaI5HWFapxQD5QjR3PxG1t_4UWwJp2iQyG2xhjdggaIY27nlq8oGgbBkqQRrigaoU7uGqvTCq9OpGMaC1TEy4Si6fJRzgVhqpqVRfpzcOozdaXRN_GVogec40cdWu8jnbCEFk27swSDXyMKRQBIW67Rg3Xgrc7GOgDqXfbTQ-SBvGyinf1vWxcjyJxKMw5Pdhv2gmDiSwx9N6LylnESQ5pUocEfQtFAAIdaRNmmIBySvo9EnV_VeQAPBUXdYa8OSChKoP2N8Oe9liQjZTUpMxtwOz0K1EYaHxKocHc4eEb0WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤡
ترامپ در سال 2049:
ایرانی‌ها هر لحظه ممکن است توافقی را امضا کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65925" target="_blank">📅 17:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65924">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXxkPlwWypCOSnXq-UCtMmeatdIQJbCN4mN1uwPiWJAbTu-et6OIMfkDHDq4N8s2EsVEYWxDWwt1l4ADZd4UX4u4iPCreIFxaka6cURKzxGzRwHq1syS3Q8UDbCAIY53eYkXWXSwipXaNbb1J9uLaLfdtsRVRgvzFznNnmKsvktnDylKGkWRsVrB-e6P2SE5pxAe5zKoLNHEh4RAS4kRVxwRuNn0qmshMk1mq7hpXfa2fQIslES2Fo0BwS9qkpHyqJqxHY-aDPtDyF8oOEjusEaVsNcCnlg1sRzK5PrPUTOOtNaj4P7NfYKrIEIdWVA_X4goRKvXw3vuL0dbdA8T-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
مرندی، عضو تیم مذاکره‌کننده: یکشنبه در ژنو اتفاقی نمی‌افتد
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65924" target="_blank">📅 16:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65923">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f5e54d8d.mp4?token=QoPp8IGnvXTWin18bsWuaUU_HSqpFhdpn-TNxi5j90un7D55UhPsGm4gxDwaWA0f9Y30z_i5R-ntdOKOehnu2LYzaUPZyNazfbHSvFnjrFYEmGhNuTAhp5Iwu_IxRrFw4upRCHFpy0OA052sser5UhcSXVhjLhA4uvsLwzrrkhopstXVchfT4rVFIC5YwsRgUGMhz5DMhrOXiOlLAVeBd5jDct2YGSJM-0TRkhCdnjhVTbIPJJW106hqx8izthGbffQXKwsti_w7hfj0COwFfnehksAj79RAC6wNvxZdcyADnnjymY2F5DLmDbzzIO-Pr0FyDi0iJBM0d4dOy5X7JmD58rZWLDVpkyY_G5gtUMYO8czabJFXEBEbd7YLhJTMrs03Kpb-5hmhFr7Td8jNjwAKwx8mpsGJLm-3aM9Y6V-uXvjkPynr7NahMM9coxLJF1q7ByToBb-y8_PbMvXcYCNO7elx_zauJ99ta0DsY3wNu9557-xgfwkhdd5KWrkQ134Q0QUlUuRLZqr11kMOH6UltV1qMaPer3KWUkRTPm_YOrn6QwtmeJonx_M6aLj_6W8GALjKsV1nDZl7qQIzwM1jFnJcHpvDKcxyvlYichzRibTgic3yK5k2KivgOk96tR7JG7M0G03qppswSDR4cH2evyq1auYAooy3HR7e4QY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f5e54d8d.mp4?token=QoPp8IGnvXTWin18bsWuaUU_HSqpFhdpn-TNxi5j90un7D55UhPsGm4gxDwaWA0f9Y30z_i5R-ntdOKOehnu2LYzaUPZyNazfbHSvFnjrFYEmGhNuTAhp5Iwu_IxRrFw4upRCHFpy0OA052sser5UhcSXVhjLhA4uvsLwzrrkhopstXVchfT4rVFIC5YwsRgUGMhz5DMhrOXiOlLAVeBd5jDct2YGSJM-0TRkhCdnjhVTbIPJJW106hqx8izthGbffQXKwsti_w7hfj0COwFfnehksAj79RAC6wNvxZdcyADnnjymY2F5DLmDbzzIO-Pr0FyDi0iJBM0d4dOy5X7JmD58rZWLDVpkyY_G5gtUMYO8czabJFXEBEbd7YLhJTMrs03Kpb-5hmhFr7Td8jNjwAKwx8mpsGJLm-3aM9Y6V-uXvjkPynr7NahMM9coxLJF1q7ByToBb-y8_PbMvXcYCNO7elx_zauJ99ta0DsY3wNu9557-xgfwkhdd5KWrkQ134Q0QUlUuRLZqr11kMOH6UltV1qMaPer3KWUkRTPm_YOrn6QwtmeJonx_M6aLj_6W8GALjKsV1nDZl7qQIzwM1jFnJcHpvDKcxyvlYichzRibTgic3yK5k2KivgOk96tR7JG7M0G03qppswSDR4cH2evyq1auYAooy3HR7e4QY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هگست وزیر جنگ آمریکا امروز ۴۴تا پرس سینه زد
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65923" target="_blank">📅 15:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65922">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‼️
خاورمیانه در این مدت
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65922" target="_blank">📅 15:15 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65921" target="_blank">📅 14:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65920">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه:
متن توافق پایان درگیری میان ایران و آمریکا تقریبا نهایی شده و منتظر تایید نهادهای مربوطه هستیم.
متن نهایی تا زمان پذیرش قطعی آن توسط دو طرف منتشر نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65920" target="_blank">📅 14:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65918">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rF-C37qc3axViLhyYC7x46ad0clOcYlQ7MKmfhhzswFn33ghnH7xiEjeZ-uZrjsca13aMAJrdhkNEEc2f0EAEvxUm9D-o0D5JNqtfShDMISTjU0qNXGbOTNw9Jpz9SpbUI2P1WU3C-A5GSNNiJ4f9TybpSZoSLaWCLy28U6VQEs37FIILAUU0k4KSroKv04S0P3o-3f0ilkQvkE3vjPwXcwWWIJ9IViYXE3pUjJDXryIcD4tY4NeXjJqQZ16jasq3wbePbYtDNFrXIiqMRIE2J4QwJYpVZfBm7wBHCVH4VhsRC062ogRjzateuIbZ9dq2vuTBuJ_aibeiPBwdNUmkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lg7YmHqnOTRcmvlQ0yOBOK95NEqi409lb3W5G9RbEzfsm8rUFH3EwSpMKH7aOIIoIvumL4vVBvCdYIVgSnmCz2godQeOLRipDHQLgSmooe5wW94p84GaXX_uyTRjOaK5S0RLo44_WMjjNq_ZVkpZxLjG8CuTexx3U6amzksawiV7Gcl6sUS9ILVIvqD_OUGUKg3_MVHKLpk_eiVRYSCMLH4Y33_1Cs6PHTPMGYKq6rCbtvMYfrHY0Jb98fnZomARMOky2qbt6MeytdIRxdTEgipDjlquDR3BviwYsK6dYJLpD5ZrLTIc7VlNKH64unawm7iZDmYrm1Pjj5D3wqg0JQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تصویری که یک پرستوی نظام در تجمعات شبانه از خودش منتشر کرده درحالی که چاک سینش پیداست.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65918" target="_blank">📅 14:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65917">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aed65f61d.mp4?token=eMAi9-CexRuGvNT-6KmIqusrV97ytz5x8iySr0hXNSAweGP_f-WWhN9pfvJUHXZaF5QfwqQcrfMoa8CkZQ4gLpyxMkKmVNBBiinCyhKpX2sUMMoOdYrZZczEAMr9bjseVcAcnRrAY-Y6xA6Ug_JbCFwhPKERtlamnXH-iO3cuIRuAFMX3kiYGgblA2WXJC6Bf5xG6sgNBkvvTD49-dy_e96G0CrKTEwNSQEA_bK61qo06Nxscp7tDJdtR9czWxheeCr2styVOTe3_xe4eDIYBrJfWN1v6Ce9dmc_nYkIUYzB8l0TLQ-iFd4FPY-p9q-rAbzD6ZekuwaajC5it8N5Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aed65f61d.mp4?token=eMAi9-CexRuGvNT-6KmIqusrV97ytz5x8iySr0hXNSAweGP_f-WWhN9pfvJUHXZaF5QfwqQcrfMoa8CkZQ4gLpyxMkKmVNBBiinCyhKpX2sUMMoOdYrZZczEAMr9bjseVcAcnRrAY-Y6xA6Ug_JbCFwhPKERtlamnXH-iO3cuIRuAFMX3kiYGgblA2WXJC6Bf5xG6sgNBkvvTD49-dy_e96G0CrKTEwNSQEA_bK61qo06Nxscp7tDJdtR9czWxheeCr2styVOTe3_xe4eDIYBrJfWN1v6Ce9dmc_nYkIUYzB8l0TLQ-iFd4FPY-p9q-rAbzD6ZekuwaajC5it8N5Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وزیر ارتباطات: بستن اینترنت امنیت نمی‌آورد. وقتی اینترنت قطع بود، وزیر اطلاعات، لاریجانی، رییس اطلاعات سپاه و بقیه ترور شدند. با بستن اینترنت، جوانان نخبه مهاجرت می‌کنند و این ضد امنیتی است.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65917" target="_blank">📅 13:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65916">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‼️
ترامپ از زمان شروع جنگ ۳۹بار گفته با جمهوری اسلامی به توافق میرسه
.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65916" target="_blank">📅 13:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65915">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30551bbbff.mp4?token=sWpHGggIkSo75SLkM9KQU1ohe5fn0Ez7XejsHIXOBTPudcegQw7ZcsdyBR9GD-SWeW5klSFoP0Xe5bEXZKQBPLqi1xApWNPBi8t80JHyqNgy_YBw7i3XQEhTB6ZIPhuu8_fcQKPfznp-N23cA3aL4i0Q8FLt8CL6BQFqRekX4lEX0G3Fm6w9O8bro95px854zwKapNCE2edojR8RHYQqYiFF2DOSDdvCYAKVbDpqfBXW7bN7ndPIuPkJEdc5v6U1ElnNN34cpRFEPLVUZTcJBeJ3CReeBTPsCijc_1pZfztbMltDjhSmdM5uYTy7WylWOSNaKCrvsky_qT2n_vz-jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30551bbbff.mp4?token=sWpHGggIkSo75SLkM9KQU1ohe5fn0Ez7XejsHIXOBTPudcegQw7ZcsdyBR9GD-SWeW5klSFoP0Xe5bEXZKQBPLqi1xApWNPBi8t80JHyqNgy_YBw7i3XQEhTB6ZIPhuu8_fcQKPfznp-N23cA3aL4i0Q8FLt8CL6BQFqRekX4lEX0G3Fm6w9O8bro95px854zwKapNCE2edojR8RHYQqYiFF2DOSDdvCYAKVbDpqfBXW7bN7ndPIuPkJEdc5v6U1ElnNN34cpRFEPLVUZTcJBeJ3CReeBTPsCijc_1pZfztbMltDjhSmdM5uYTy7WylWOSNaKCrvsky_qT2n_vz-jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آتش بس در خاورمیانه:
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65915" target="_blank">📅 13:01 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65914" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65913">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=fHmbjSNOKLziDl5E4hYOhE_B0TRAfYeRFBjQ9rbdJqVAEzqyMlXkawhhCDJDj-HOwxgCp1dXbBK8nwRd3aK-lB93lIZXI41iv1F40NK5Tqh5WIS3DpkLJctidFhLjOEZm4bL44lQA2yC9-FKNtZyz506tL-gGj5NTabkMyscC5sAWsONlBYrvnk2Bnkx2X2eAReUZx-F34REdqlsb8Ufttc-VCG1jHO_RPnB6bR2CH7CPFf8RLV0TQCEHYaCO9sNo_0jGA8wCAjAmgH2w5qFKT_1Rx6vJ3ZASPELGdPB-zde32S1JMmLZsie6IjT-IsZGsRlkJCwwgl0KMR3WloG0bX_Bub1Dt_2TwpmyF3Po0RfieUSINkzzAE3KyBPggz79O1YsBZmZz1RoeVz-pLr1i5bmT8y78cx6mSZ65uT6DvH9XW_0P3YZzv0_2pkTtoE4JCf1-OKo37qC-ygieAqyKHmf68lk3qKGVbDyJJxybOmAE1D5zz5gFa_1CuvfC9OCPkg3A4dd1oySSC_SwKrtriCzWnRM7sVeseZ54D6WPrjJH0wKKDWe5mghZnRhHC28ZKmSF3tYE1Bo1lk6D-ziX98ZUIBpYuoDI4GYCVfrGse3tPJjhEr8H9vli4OG2tewJi9bgUcnvCpdoaMPskeUf4G82V-6hWuNAc96PdTC7k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=fHmbjSNOKLziDl5E4hYOhE_B0TRAfYeRFBjQ9rbdJqVAEzqyMlXkawhhCDJDj-HOwxgCp1dXbBK8nwRd3aK-lB93lIZXI41iv1F40NK5Tqh5WIS3DpkLJctidFhLjOEZm4bL44lQA2yC9-FKNtZyz506tL-gGj5NTabkMyscC5sAWsONlBYrvnk2Bnkx2X2eAReUZx-F34REdqlsb8Ufttc-VCG1jHO_RPnB6bR2CH7CPFf8RLV0TQCEHYaCO9sNo_0jGA8wCAjAmgH2w5qFKT_1Rx6vJ3ZASPELGdPB-zde32S1JMmLZsie6IjT-IsZGsRlkJCwwgl0KMR3WloG0bX_Bub1Dt_2TwpmyF3Po0RfieUSINkzzAE3KyBPggz79O1YsBZmZz1RoeVz-pLr1i5bmT8y78cx6mSZ65uT6DvH9XW_0P3YZzv0_2pkTtoE4JCf1-OKo37qC-ygieAqyKHmf68lk3qKGVbDyJJxybOmAE1D5zz5gFa_1CuvfC9OCPkg3A4dd1oySSC_SwKrtriCzWnRM7sVeseZ54D6WPrjJH0wKKDWe5mghZnRhHC28ZKmSF3tYE1Bo1lk6D-ziX98ZUIBpYuoDI4GYCVfrGse3tPJjhEr8H9vli4OG2tewJi9bgUcnvCpdoaMPskeUf4G82V-6hWuNAc96PdTC7k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65913" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65912">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
کانال۱۲اسرائیل:
مذاکرات نهایی آمریکا و جمهوری اسلامی در مورد برنامه هسته ای و مسائل اقتصادی است و برنامه موشکی در آن جایی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65912" target="_blank">📅 12:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65911">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
یه‌یارو بیکاری بلند شده تمام اسکناس‌های کشورای مختلف دنیا رو جمع کرده و باهاش ویدیو ساخته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65911" target="_blank">📅 12:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65910">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
رهبران قطر،امارات و پاکستان کسانی بودند که مانع حمله دیروز ترامپ به ایران شدند.
سران این کشور ها به ترامپ وعده دادند که توافقی اولیه با جمهوری اسلامی دردسترس است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65910" target="_blank">📅 12:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65909">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9247426e69.mp4?token=ApVtfSa0LlFnUBs3xroho8guOx_5odDBcSOfBxZNgMlhc6pGq7JidbrZw2fNZPa7r5SPmk3a-Pnubc3ukLHWG3e-3Qea2LCSOU4VFF4vy1aDuqkjZDQPxJx0jvS-AdnKOKI7I-JLyHFAsvuqgSdn588nHZOjiwBIWHfuEdDVoKgexNeGLLE8X-DDMlFmFR2GVGuO2I2JVkw3l4Xi_jxzw_TSdMH-q9tQA-jJmRhLkgrYkhG2t4vtlzoZmYiiIaNCdmeY6508RmDU0cOYYiX3qo_a3zpo2LqOZbDarBMRlD6Xd5NX4nUnsq7VQqcI1IluPetWOk2I8f5elHCDvhok4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9247426e69.mp4?token=ApVtfSa0LlFnUBs3xroho8guOx_5odDBcSOfBxZNgMlhc6pGq7JidbrZw2fNZPa7r5SPmk3a-Pnubc3ukLHWG3e-3Qea2LCSOU4VFF4vy1aDuqkjZDQPxJx0jvS-AdnKOKI7I-JLyHFAsvuqgSdn588nHZOjiwBIWHfuEdDVoKgexNeGLLE8X-DDMlFmFR2GVGuO2I2JVkw3l4Xi_jxzw_TSdMH-q9tQA-jJmRhLkgrYkhG2t4vtlzoZmYiiIaNCdmeY6508RmDU0cOYYiX3qo_a3zpo2LqOZbDarBMRlD6Xd5NX4nUnsq7VQqcI1IluPetWOk2I8f5elHCDvhok4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو یکی از کشورهای آمریکایی پلیس به یه زن مشکوک میشه که ازش اسلحه بگیره. تهش طی تحقیقات زیاد متوجه میشن اسلحه رو تو واژن خودش مخفی کرده و با تهدید پلیس مجبور‌ به تحویل میشه
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65909" target="_blank">📅 11:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65908">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
خبرگزاری حکومتی مهر:
جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا
جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا منتشر شد. این تفاهم شامل تعهد آمریکا به رفع تحریم ها، خروج نیروهایش از اطراف ایران، رفع محاصره دریایی، بازگشایی تنگه هرمز، لغو تحریم های نفتی، و پول های بلوکه شده ایران است.  آمریکا موظف است طرح بازسازی اقتصاد ایران را ارائه دهد و در حالی مذاکره نهایی میان دو کشور باید در مسایل هسته ای و اقتصادی انجام شود، بدون بحث درباره برنامه موشکی ایران. این پیش‌نویس نیازمند نهایی شدن در نهادهای مربوطه است
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65908" target="_blank">📅 11:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65907">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
باراک راوید:
یک دیپلمات از یکی از کشورهای میانجی که بندهای متن فعلی را با من بررسی کرد، گفت که «ایالات متحده و ایران در مورد متن توافق به توافق رسیده‌اند»، اما اذعان کرد که هنوز تأیید نهایی لازم است. با این حال، هواپیماهای نیروی هوایی ایالات متحده دیشب با تجهیزاتی به مقصد اروپا به پرواز درآمدند تا برای احتمال سفر معاون رئیس جمهور ونس به مراسم امضای توافق در ژنو در روزهای آینده آماده شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65907" target="_blank">📅 10:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65906">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
⭕️
توافق قریب‌الوقوع جمهوری اسلامی و آمریکا بزودی در ژنو امضا خواهد شد و به‌نام توافق "اسلام‌آباد" نامگذاری می‌شود. طی این توافق یک آتش‌بس ۶۰ روزه که لبنان هم شامل شود، شکل گرفته و ایران می‌تواند با پول‌های بلوکه‌شده خود کالاهای بشردوستانه تهیه کند
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65906" target="_blank">📅 10:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65905">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/215d29fff2.mp4?token=u8LCDbr9j4Q7mYIohBgprHMnmA77aygNfaYkmrFQKVFYO_lRi_PLcmYHJcpIHZb42eThn20ssYANX1M75q3CnarFpvmJLDdWh4MZd-QWaXfsw1FYTc1oqs0iIns9GZf4F8dggSf7AaKw5Q_Yqy6QIrU8PamK1bAwtNESaol4JbRe8SnUM2Kc945U1hA0y-amnLFWmX4dqSFlrWXE-5xvWW-q4gyckrWTrOnvKYHGCutmQorzvVA4bER5cnkd8-gHpLuIVADEYk1rI7j6MeUBbF4N2nyirl90ozE48KocQPgFs60conzWDez-jqVxwmIscAp2J9bCRE8CMSBURYmikRR7uj2fFovBmBZQkZj9nS6Ll-1UwcGFTkPWgsgBinUVs_9nTOlJp8OIegEe4K7G9A5iy4TNOUuBG1WHLJSvP9A3rqcT1Rygb64qWoKYHbByNaGyPFyTQmAtaB5oeUsBPyYlN_XZeEZgvSYgdJRor2ScvUPMrLzXcjUyOHiEY9wgB14yNg8xvEMf6I1MOVJQNGbKutAVoyRC6V2_JNcO0UB1eay9txifpZpROchbyh9usAXizgzIWuQobQ1KI1XpfJWDHWppcD_3oM1HDYWq6HgSU7KVIHIrwbPsORAFDeL72-sobgqBovlN389hzC0E7_Y8-_ouu-b07jE4z64OR4M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/215d29fff2.mp4?token=u8LCDbr9j4Q7mYIohBgprHMnmA77aygNfaYkmrFQKVFYO_lRi_PLcmYHJcpIHZb42eThn20ssYANX1M75q3CnarFpvmJLDdWh4MZd-QWaXfsw1FYTc1oqs0iIns9GZf4F8dggSf7AaKw5Q_Yqy6QIrU8PamK1bAwtNESaol4JbRe8SnUM2Kc945U1hA0y-amnLFWmX4dqSFlrWXE-5xvWW-q4gyckrWTrOnvKYHGCutmQorzvVA4bER5cnkd8-gHpLuIVADEYk1rI7j6MeUBbF4N2nyirl90ozE48KocQPgFs60conzWDez-jqVxwmIscAp2J9bCRE8CMSBURYmikRR7uj2fFovBmBZQkZj9nS6Ll-1UwcGFTkPWgsgBinUVs_9nTOlJp8OIegEe4K7G9A5iy4TNOUuBG1WHLJSvP9A3rqcT1Rygb64qWoKYHbByNaGyPFyTQmAtaB5oeUsBPyYlN_XZeEZgvSYgdJRor2ScvUPMrLzXcjUyOHiEY9wgB14yNg8xvEMf6I1MOVJQNGbKutAVoyRC6V2_JNcO0UB1eay9txifpZpROchbyh9usAXizgzIWuQobQ1KI1XpfJWDHWppcD_3oM1HDYWq6HgSU7KVIHIrwbPsORAFDeL72-sobgqBovlN389hzC0E7_Y8-_ouu-b07jE4z64OR4M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه خبر:
با صراحت میگویم بخش عمده ای از شروط ده‌گانه در توافق وجود ندارد
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65905" target="_blank">📅 09:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65904">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6afe375b.mp4?token=vkKGDCWzLk-sSqluXtfqGoFbP2ZkcaZhXIHkAJGD0ourix6gz-GigREn91t1tNiJ95rS3sl6-0muweq1OSsMSMg0ctVnYKzJ1kzvuoUxFQENrNN_51KGk-snUIazlU-7Ifccmqy0wcW6_-qcGkYcqK2R5KzJyl4uO0QVzPYJvXRhGtG1Y9YtddP2YaXooY6DzDBBWuWulaXvH6vtU9nR1a27QQ-5X4D7nDKy-d_meACk-YsBTnUUHURTB0RvjCQlwTRRru9EFaUCWXo-a7m5vOjyPLmx1SA-PotGAskW2DCrqiyt8LycKyaVvAmBDizyUuxGyJtkAE-SVuhHCLdE0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6afe375b.mp4?token=vkKGDCWzLk-sSqluXtfqGoFbP2ZkcaZhXIHkAJGD0ourix6gz-GigREn91t1tNiJ95rS3sl6-0muweq1OSsMSMg0ctVnYKzJ1kzvuoUxFQENrNN_51KGk-snUIazlU-7Ifccmqy0wcW6_-qcGkYcqK2R5KzJyl4uO0QVzPYJvXRhGtG1Y9YtddP2YaXooY6DzDBBWuWulaXvH6vtU9nR1a27QQ-5X4D7nDKy-d_meACk-YsBTnUUHURTB0RvjCQlwTRRru9EFaUCWXo-a7m5vOjyPLmx1SA-PotGAskW2DCrqiyt8LycKyaVvAmBDizyUuxGyJtkAE-SVuhHCLdE0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گفته شده ترامپ بعد دیدن این ویدیو تصمیم گرفته که توافق کنه
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65904" target="_blank">📅 09:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65903">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0auxZR6F2XShr1W8NGysaoLY3e0jckgpwEzXUgLo2430sVLN_WEOHOSOGuzl1D-oJbWWZu-1Rfz9nGdHArBTZEp1r2eLIBmW5yeZ5r4w9YWUaqwWRLlGsayPJxAvfG3PIAZ5LQbFv6fMv5z5cClR6ZzMloOaZWz0wuIoFRvkYMZRv3c7BWbBA_uYDyU6gVB9nMTgxvlj179KI1E362Y4h_5XDlwCofkp1SrLvrA4WeOpl32RNVua7bA0YnbiyExT9MEXYYoSTPNGgfHdWDlejY_z4gC2o-L_cV7h-mKCVt4yvaOrXRkoXcCv0-9fcIanjmNxDgM50b3wtEcxq00IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک لوین:
اگر همه این دولت‌ها با این توافق موافقت کرده‌اند، شگفت‌انگیز است که چگونه همه این دولت‌ها به این سرعت امضا کردند در حالی که ما اعلام می‌کردیم که در اسرع وقت بمباران خواهیم کرد.از آنجایی که این توافق انجام شده است، آیا می‌توانیم آن را ببینیم؟
در این توافق چه چیزی هست؟میتوانیم آن را ببینیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65903" target="_blank">📅 04:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65902">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ffn1RRd3Oq8eVDw6EvGbAqWEnQ0ikG5GX8BtOVOxPzPQLdWBZkVV7XoUlG0sf9CLsf4SyMKEHTOfJrtH8ENkuM_fk6t8KiRf8Elj4JOPuB_3nkyL69UTyEtb9trBdAd6f84x97Y2drHr-ct99BtZtvW5mPgfMQZxjHcinOlyYWae0JwmD5VV5_rM0Z3fBtE88Oroy_ks7sQGXQUM_mE0mvb572uUs6EAe8IR6V-e4G5f-D9czPIT9-LOI87RGl4wKoGvpgI33m7bFpybA4Hn1izhERks0iHA2HpTsHBdQUmR1vMbVrsXg54hbDNvrEzqn4PBplUDsI5uz4i_EI9BOA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/78687e07ef.mp4?token=EnOF9DzRCDOlUocOjGFnxkiCRiANl86FvlwSPpisc1pB1pu3l1n8-lvdiQslXpBJHbtVw7eU2Klz1_VwehgzWAAAT7qptppHo4hh1d1Cimb441TfVAw9vGPnGXCRptwvfPNUxl-MLuaoKRxcUraU7IexUWLctf1xn1eTAjOsBF5JYuUSr79y_LZ57KgUH8HIB6u8Sk84mXB39ZH-1eGS9g-5B3Cw8JtE7znIwdq6tkjXJMizdShIziXnRREzXpVmPk0jNJSjDKxgJ3iXkCyzHXRM_U-fYw0OlafmHjAmg2lPh5GpK63lDv5Nsp7BIOotaCkwEWbEv3KxyHVZi0xBOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78687e07ef.mp4?token=EnOF9DzRCDOlUocOjGFnxkiCRiANl86FvlwSPpisc1pB1pu3l1n8-lvdiQslXpBJHbtVw7eU2Klz1_VwehgzWAAAT7qptppHo4hh1d1Cimb441TfVAw9vGPnGXCRptwvfPNUxl-MLuaoKRxcUraU7IexUWLctf1xn1eTAjOsBF5JYuUSr79y_LZ57KgUH8HIB6u8Sk84mXB39ZH-1eGS9g-5B3Cw8JtE7znIwdq6tkjXJMizdShIziXnRREzXpVmPk0jNJSjDKxgJ3iXkCyzHXRM_U-fYw0OlafmHjAmg2lPh5GpK63lDv5Nsp7BIOotaCkwEWbEv3KxyHVZi0xBOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i-lFbJA9ZbDWecIL66aTC_FT4qALrBdthc90q6PTgURQVTdQiDN7kaMx4RqwDuLUZLKfUsxbebMuPW4aUhyQbW9V8INGpMyRwCauGKSFJM66w0GmfYuJQL0YKVx9TSzY8QgQ2yB3LjPlKk2wpqxPcwop9QrHFr9dCCAAq4f59Dp3ioBmhsiTClSB-FSnXxNq4BMMy3uCLohgLCrPGFEF6fdsiFQrIiKmcWLoUZ8CcCBN-MMi-Zhe9LwSbuNKJQX27MZhmq2CMsJ9TunM7hLw7e2ZQ32b_eXAfI2ObchkDAvhRQi5lQImr4UfR3ECrf-cc-8IyjDSQfEdO0luvWpg0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMlTa-sSBw9OeNIXlF6VF27Ao6NyzTcntgt7nbUrqFPaDqRWkCRWe39m3KM5HOdu9aid3dg0A6CtHCMGBPw_fyyQoIBNfVeRkSSHSP8PS5FvNBMI6lbdtK-ciK17ngNtoivEylS9zWNRPOKC4JniLJbEMJag5_xfwZUkrjMjyF3u72mW3moX4RvxaMiPPXLfbDbOCEw3PoZSKmWUO54SkV4t9iKRWeMXiCbT6T_DJ9USe2jx_DKYezPVpWOEnWdEceEV1YSEr7EP8RXxewXdGJORFSXq0CBWvTc7sbapN8vl0j0dtPjuZaUQrO7tCl2wMZ9V7kv1gp8yWK098bgZHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اعلام کد اضطراری یک F35 در آسمان امارات
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65895" target="_blank">📅 01:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65894">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دیگه نمی‌زنن
😭
#hjAly‌</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65894" target="_blank">📅 01:19 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65892" target="_blank">📅 01:08 · 22 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGufwfvjOtUArNlldO1MiwbNsjUlLe8aHxdCcCNi7_qAcga5Gvl10h59rrlDEcMfpClScewR1W63IrnUxYIR2sR1VJAokfYSLC5oBy68hCqTM81m8wWYmURV30ahyF7qUf7eiIrRH26nmdIPwHrzSsv-91pW1FgSAMzglJOWnm1OH8g4hYOEeWjqgybzsxODnpt7kl3MzuYRJsh2V9NBZGUMaBr_DRbM0zVNRDlwUSVlx0PwqQAwn1GtPBrstCgDbOPy6VLm8F4VU0w08128yrjEUBXOGEE9BAQhKR-TryxLXg_nGA2SXqNMrklBGzN9EBSfD9vLs6KhgPBNS3JC_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65881" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/352ca9d87d.mp4?token=l6bQU842pGfQSDp_K85JRDLltF3mcv7LQvX0Ihu4yJUbT4erF80xo73sDuyw9qVOaYnTpHjKle6Lu9mghKzqj9a8aVZKo9IBaJA5eXJdlTCgpC5L-XPUyHf1gnwZAmmVZGmd4fyl5v1nz-IiRtPzcINjDgIoeQOPLfl2lxTxR8NtACdtRsAfleB-tyRBw_MGjES6OqHX3APKYVw3ZZIArnhHRmHT2ydP0VYwe5jgOzIQ8gBfgYDxdBeH66VuGnGOYDvAG24wDUbeb82J2_pNV4x3eczf7ZODCBhHVI5AFneX_ZvIZ879kKwKskvEOlQjrCZibMaMcY09F2OaymZhFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/352ca9d87d.mp4?token=l6bQU842pGfQSDp_K85JRDLltF3mcv7LQvX0Ihu4yJUbT4erF80xo73sDuyw9qVOaYnTpHjKle6Lu9mghKzqj9a8aVZKo9IBaJA5eXJdlTCgpC5L-XPUyHf1gnwZAmmVZGmd4fyl5v1nz-IiRtPzcINjDgIoeQOPLfl2lxTxR8NtACdtRsAfleB-tyRBw_MGjES6OqHX3APKYVw3ZZIArnhHRmHT2ydP0VYwe5jgOzIQ8gBfgYDxdBeH66VuGnGOYDvAG24wDUbeb82J2_pNV4x3eczf7ZODCBhHVI5AFneX_ZvIZ879kKwKskvEOlQjrCZibMaMcY09F2OaymZhFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/e1ce54a8a4.mp4?token=qWoIJHHH0JJNbIU_DHsEvyJJOQFz0HzhVEiA5u3poaq__tINvIgbI8acDYoJw2P_xzP_CycobCgURTkJI8fhqpyZH-PevTl3SrmKvT_KsI5I_Jo7wJfuS1DCN3xhtJLqFDk5pvIO1q2YQw3YHFdvXwve044ymPXb1isb0_BsxNF4OFR6tYKqlxWAtP5y5UBFcUk4HU6t505kB3B7bFlyZi0KL31-Uz6BOE3Lm15Qh10Bvvlmp8wHPq5WnVivp-WqGyAK2oEAiiRLU-Q7rMVd1VqsECNIi4J6YxE0GKgphOlFUNShODXLEIJZP-h3w6Zri-5G7Kg1oWCOpoH2k5FYEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1ce54a8a4.mp4?token=qWoIJHHH0JJNbIU_DHsEvyJJOQFz0HzhVEiA5u3poaq__tINvIgbI8acDYoJw2P_xzP_CycobCgURTkJI8fhqpyZH-PevTl3SrmKvT_KsI5I_Jo7wJfuS1DCN3xhtJLqFDk5pvIO1q2YQw3YHFdvXwve044ymPXb1isb0_BsxNF4OFR6tYKqlxWAtP5y5UBFcUk4HU6t505kB3B7bFlyZi0KL31-Uz6BOE3Lm15Qh10Bvvlmp8wHPq5WnVivp-WqGyAK2oEAiiRLU-Q7rMVd1VqsECNIi4J6YxE0GKgphOlFUNShODXLEIJZP-h3w6Zri-5G7Kg1oWCOpoH2k5FYEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-dMiUFVqZxlPGS9weMN5RRqeTP-teylK7Eh0mgZcMXXaYGeQPVNbVRwKMqyrQD3N9u9totKqkBaXnbrzj30B292-SwNXzz7rLjdyOu9wHNeXwcV3f-1bL3YU1KMGSLonslaLczzLadKg8imQXLofJWyZkQpKigSAvryzzwJTSqGIMxwMOYT912O8KSRx3vb0agOQ-0_l_yV89SAU6FSWf-sywhXfWRHxifdhYgXvgk6EWYQ70TfADUu_iD9-C8fD3lOadvaV1dFdr-ibyvTeNI9X7TjpFzQPKSayI7O9UcvJgTfu5U6jOBgtFwdnRhsWWqJI17X8s3sxLPwb6Tcww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیرِ واشنگتن
#hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65876" target="_blank">📅 23:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65875">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e445beba9.mp4?token=BeLN2z68ZL4Buiyfi82UFwr3BSVqomj_PwdHn2EMzf1WBWG65JZR4aIxsqvuNsIzdWApjfEBAs9cGgNrdBPOK-tunKj8lGiA-XPoHX4LzoWkDB6AaDStfjHsVyX2EQPkjQQbY2KqNKCl-jPJ3jzVe4x82heg2QpcN7C-L8PFNeUDRlZGMn5tunGGGFBd9j4nBvFCDAqjZXV_d5vJFwgVWryjVIJ2m92AyXWRk6iGaT0n-4rzOG5AY_SAH_F8wMA26ayE2OQ9uM8zvttFuLEqVfCvk5fGkwwC3xoV-HFH9spsepw1cLWsS8WvngK3ql2Kcz6tqJ8Cvu2LnTsttOgNrLxH8VATX_IIo8hPz1sX0vbxRkOE55qySN7DCxTg18GBcH9cD4mVX-JFUWh3WGUphHiynI4e23275_f0rxQRPQYvC97n1jSt9zZU68eNgGYLmLH2rB5XJCxYaGDpDnCll01nKmKAz_o9GkQBtaae73ORVpHzO0_wgnYCcrHI7jNRp4nN8hEz0Dy1_fH-RgwgFPgubbWE3orZ-DtLiOpkVnJwfv2ut2c7LFlBBf4H4nBIPDZbBbW3Y0VOajORpMZzyDhxLFDZEPdzNuwzZFFgO0KqAqLC_rxhpBU1lB2aOU9bze4N5wM7D45bRq4LLL828QjIiHdE3o9cqmmkPNjyDGo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e445beba9.mp4?token=BeLN2z68ZL4Buiyfi82UFwr3BSVqomj_PwdHn2EMzf1WBWG65JZR4aIxsqvuNsIzdWApjfEBAs9cGgNrdBPOK-tunKj8lGiA-XPoHX4LzoWkDB6AaDStfjHsVyX2EQPkjQQbY2KqNKCl-jPJ3jzVe4x82heg2QpcN7C-L8PFNeUDRlZGMn5tunGGGFBd9j4nBvFCDAqjZXV_d5vJFwgVWryjVIJ2m92AyXWRk6iGaT0n-4rzOG5AY_SAH_F8wMA26ayE2OQ9uM8zvttFuLEqVfCvk5fGkwwC3xoV-HFH9spsepw1cLWsS8WvngK3ql2Kcz6tqJ8Cvu2LnTsttOgNrLxH8VATX_IIo8hPz1sX0vbxRkOE55qySN7DCxTg18GBcH9cD4mVX-JFUWh3WGUphHiynI4e23275_f0rxQRPQYvC97n1jSt9zZU68eNgGYLmLH2rB5XJCxYaGDpDnCll01nKmKAz_o9GkQBtaae73ORVpHzO0_wgnYCcrHI7jNRp4nN8hEz0Dy1_fH-RgwgFPgubbWE3orZ-DtLiOpkVnJwfv2ut2c7LFlBBf4H4nBIPDZbBbW3Y0VOajORpMZzyDhxLFDZEPdzNuwzZFFgO0KqAqLC_rxhpBU1lB2aOU9bze4N5wM7D45bRq4LLL828QjIiHdE3o9cqmmkPNjyDGo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKeHfSvp1NwA_AxTdqNQulzQAM8AA_XNvGvWwI_Hprc9Ic_m15iT4yOxqSemtLBEpjr3434ntNw5yFsDZCuATYaXlCF4yjLB9H5fm89--5syKu3g_ygSmd90jf5TRSW-g_U7JH7fPDuPxmNx461sQXkXv5otJ1AukcNzVyOREXS6A4Sz7gz7N8XuwjcS8yhlz-goGpC85X4uyxzHMccUNxwevF3P4OVTZMcNWV_Z3MIWeQOF1OcBu2U9k4kW5STk9t81G2YE6blYMCnuZ7mZT0Tad2dg0zwdWDQfLqMaEhNAKaQfT5FVVnflObbajrDeu9EmIwK-DCBog7GbAai__A.jpg" alt="photo" loading="lazy"/></div>
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
