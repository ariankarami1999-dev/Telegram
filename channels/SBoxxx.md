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
<img src="https://cdn4.telesco.pe/file/mjqRMi-zK8UxtwqMkJTFbJQHliahXgSxK6GfpYb5832WNcSZjqURITKCueugkGvumTmrO3Sj7wp51mRioBG02jYaux16ihUegOPI9t_NtRvK6eXh0J6QY4Au2tlOuKbjk3qYwEzTcWhET03QBwhNkub6PzRaMFa8slr3cOdpRvMIQYxgg8YuL8-Kk2B2ImbMK-L-du-XI9qOJD9798kTFAGHrylPlfpzNISoJ0mLQtQ2ydi_Z7d4w6jSw12aF_iOQDbeeUxS8jVxQdy96pFIXmDZO4dinWA3zoFCXXVqIcfj8e-DkX8ASFQOWQtPbrCi7ZLbmCLV9hZPaZwaKgj4Ug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.5K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 19:16:49</div>
<hr>

<div class="tg-post" id="msg-19964">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یک مقام ارشد ایرانی به خبرگزاری رویترز گفت که تهران از یک سیاست دفاعی به یک سیاست «کاملاً تهاجمی» روی می‌آورد و به ایالات متحده «چند هفته» فرصت می‌دهد تا توافق صلح را اجرا کند.
«تمام نهادهای ایرانی آماده‌اند تا در صورت شکست دیپلماسی، تنش‌ها را در تنگه هرمز و در سراسر منطقه افزایش دهند. ایران به طور نامحدود منتظر نخواهد ماند تا ایالات متحده به محاصره دریایی ادامه دهد.»</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SBoxxx/19964" target="_blank">📅 18:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19963">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یحیی سریع طی بیانیه‌ای اعلام کرد که انصارالله یک کشتی نظامی متعلق به سعودی را در دریای سرخ، در حوالی سواحل مخا همراه چهار شناور نظامی همراهی کننده آن، با استفاده از موشک بالستیک مورد هدف قرار دادند.   به گفته یحیی سریع اصابت موشک‌ها دقیق بوده و این عملیات…</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/19963" target="_blank">📅 15:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19962">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یحیی سریع طی بیانیه‌ای اعلام کرد که انصارالله یک کشتی نظامی متعلق به سعودی را در دریای سرخ، در حوالی سواحل مخا همراه چهار شناور نظامی همراهی کننده آن، با استفاده از موشک بالستیک مورد هدف قرار دادند.
به گفته یحیی سریع اصابت موشک‌ها دقیق بوده و این عملیات منجر به سوختن کامل کشتی و غرق شدن تعدادی از شناورها و سوختن بقیه شد.</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/19962" target="_blank">📅 15:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19961">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/19961" target="_blank">📅 15:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19960">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnmKk-8p9XYn4a8mAEf0ZYwLQUz6Ge2ymCPc0xDInReMJIn4NPe8nDtTV7It8xHTeJ0zu9urAtjtVyj1XMsCP3LqZt2zpmd6ZE69pUcXvfmrCMmlAIaGoLvyCkzN_RoxI9OHDXXbviqA-D91TJ1YDyqdpOfrx-4EobAJLaAmv4yqTYTrqQEulJb5YSuCg9-VMyrc9b3DD01THvQuBq7fQ3gH-QTHPFN_b6YaVgt7NT4KDr2Jn-39F2hWqT9lLnzOzph2Adg2kzuzMksIgEShxGhwsdakNvCNh8fpisPgXah_E-lp7bMU5DJq-ScfKI21N1CHStSuBGqUDkWyJm124w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ترامپ: اگر عمان سر راه قرار بگیرد، آن‌جا را شدیدا بمباران می‌کنیم.  او هشدار داد که عمان نباید در تلاش‌های ایالات متحده در مورد تنگه هرمز دخالت کند.</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/19960" target="_blank">📅 15:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19959">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔹
ترامپ: اگر عمان سر راه قرار بگیرد، آن‌جا را شدیدا بمباران می‌کنیم.
او هشدار داد که عمان نباید در تلاش‌های ایالات متحده در مورد تنگه هرمز دخالت کند.</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/19959" target="_blank">📅 15:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19958">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ به فاکس نیوز:  ایران باید پرچم سفید تسلیم را بالا ببرد. آنها پوکربازهای خوبی هستند، اما دارند می‌میرند.</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/19958" target="_blank">📅 14:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19957">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ درباره ایران:
ما یک کانال پشت پرده با سپاه پاسداران  ایران داریم. ما مستقیماً با مقامات سپاه صحبت می‌کنیم.</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/19957" target="_blank">📅 14:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19956">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ به فاکس نیوز:
ایران باید پرچم سفید تسلیم را بالا ببرد.
آنها پوکربازهای خوبی هستند، اما دارند می‌میرند.</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SBoxxx/19956" target="_blank">📅 14:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19955">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ایالات متحده و ایران بر تمدید آتش‌بس ۶۰ روزه توافق کردند
— العربیه</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SBoxxx/19955" target="_blank">📅 14:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19954">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">درباره اینکه چرا ایران مداوماً مواضع تجزیه طلبان را در کردستان عراق می زند، یک دلیلش این است که توان ترابری نیروی هوایی ارتش و سپاه در جریان جنگ 40-روزه بشدت آسیب دیده و در صورت ورود زمینی نیروهای شبه نظامی تجزیه طلب، کار پشتیبانی هوایی و لجستیکی بسیار دشوار خواهدبود.</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/19954" target="_blank">📅 14:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19953">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-text">لطفا یکی به نوید ممدزاده بگه
وقتی روی مواد هست
گوشی دست نگیره
مرسی
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SBoxxx/19953" target="_blank">📅 13:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19952">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPQVngRJRy6Guy2nWK3CCKmmkgWCpamprwYFvqlTPgRMSN51Kq5unVtZOIY9zKjzSTF6h4MBdfq0IWq5z6PPoZI-PBrudNK-Gqe_QAht6MWRtKRn2mX7A4aIaohIsn-2XyN59TCh2VBXHALRMe7s_KKBKzj4wc8GHUP0c995Vf5cI4Q4jW6vvCeWGBRAJOm9ZAJ-nWLJ9LQAyWxAgaIWGdxtfdK2pVR73WiSrnw1PV75L1eI3VhE8IPMn8-0ZLKhMT2EQJLqBjImAwXha7w_h6YUu4kXvi5B1V2HxNY5MV66loX50slzX5R_aeYWrw8ncRuU9KyoDXBcErYJLs8b0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً بالایی قرار دارد و افت قیمت طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/19952" target="_blank">📅 12:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19951">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDuslsSKZ2nhRAgakYMUvTMQP4WGI1cT4WiSosSTbUl7qA_WCrCE7zFSGRRokftV56lYkCjWHwTWrkyfYDVVAMXID1HBXhvMSpx2SKjPYceZbmUImJONFyBk6AXQOi40RA4DQkz7J0OKWYJ6zhjfaNjl4cg-yjlaSRxDTitfokxKe6PET8ztBlnX7qPKWmDgPnbESumBnaC_i-GP7P_kHAOvh9G1yU0owmg7g-c-Tgv5VEZRtFl6PbGmsQgQygJnmOEaSHwVzy7vCqJgn1LdizXMY3ZkAdNSwoIvNa-ZzzPxzNh7i9YmjzcLMxhAl1m4uVC_cqabvVQnHP2wel4LpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاهی به فیلم «رشته ها»!   امروز، ۶ اوت، سالروز بمباران اتمی هیروشیماست؛ روزی که در سال ۱۹۴۵ برای نخستین‌بار در تاریخ، یک سلاح هسته‌ای علیه یک شهر به کار گرفته شد و جهان وارد عصر جدیدی شد که در آن یک بحران نظامی می‌تواند، در صورت خروج از کنترل، به تهدیدی برای…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19951" target="_blank">📅 01:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19950">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Np-nQeOMT_qnK1xvp7MxALntaIxa2yrQlZ_666kg4wxQxVXvelcrFm0dKWwC6L8R7jX_FudlYUvqSk3qP0I8pKGZe8TmIKJ84TBmY6Mr6KdebwuTw1aLeX9BlBro2hPHkX50vPmwL8_V-uSDD3vJfm-bTympFpheuC5Bbz8UY-tCy4WAZZVLK2c-c0yciXjSuy20xjQ_DvFRR3zjKO1SnsvMkIwIMMCQVFUfY8C7Jx_U07vUvzEcperckFAJdW7OYi_wUrPVG6hHYEnHrOPrJeH-lPuSCL_oUJnAOhdBzNToEo43blYcrjl4r2OL8wIHye8zrKRT4hqijf28Tp_QxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ادامه برخوردهای نظامی میان ایران و اسرائیل بسیار محتمل است؟</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19950" target="_blank">📅 00:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19949">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/19949" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">چرا ادامه برخوردهای نظامی میان ایران و اسرائیل بسیار محتمل است؟</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/19949" target="_blank">📅 20:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19948">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/19948" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آیا به پایان رسیدن مهلت 60-روزه در فردا، لزوماً جنگ از سر گرفته می شود؟!</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/19948" target="_blank">📅 18:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19947">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بر اساس گزارش واشنگتن پست، کشورهای حاشیه خلیج فارس در حال بررسی امکان انتقال پایگاه‌های نظامی آمریکا از این مناطق هستند، زیرا اعتماد خود را به طور کامل نسبت به استراتژی جنگی دونالد ترامپ علیه ایران از دست داده‌اند.</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/19947" target="_blank">📅 15:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19946">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بر اساس گزارش واشنگتن پست، کشورهای حاشیه خلیج فارس در حال بررسی امکان انتقال پایگاه‌های نظامی آمریکا از این مناطق هستند، زیرا اعتماد خود را به طور کامل نسبت به استراتژی جنگی دونالد ترامپ علیه ایران از دست داده‌اند.</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/19946" target="_blank">📅 15:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19945">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">از فردا با حجم کاری کمتر فعالیت کانال از سر گرفته می شود.
سعی میکنم شاخص GRI دستکم بروزرسانی و ارائه بشود.</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/19945" target="_blank">📅 02:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19944">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مدتی نخواهم بود...</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/SBoxxx/19944" target="_blank">📅 16:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19943">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQQAm0zEygxWuO7-_vVWL-VkfqxRuFpr3uOI7dJglVQ7V-Be39vwAlK5Q3JVR66cNJe6dS9GZx9BxwRbVjUCOwHMir11RVpt-ALCBEjtJfJCOZ-Xr03ldaDH7xUv-P2F49171hGAb-OH_T704a-3qvQrJaqsJRWkMkpY_sVI8EaLU9coFvLzJbuDprJVBUDDGdeUQvhO4IJJq7VKZm-jSqR378oQwDKKJPcyNnkUW24OQroNUJ5mBW3acdM4X593h_CURV6WBbTxDvNzq1nX2ns6gbgrwJF6TI3PVOIAmKRyA0utm2JpDlSsvdDgdN3efC8aEetISze-8SPb-QNydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه به دنبال تایید ایالات متحده برای ارسال ذخیره‌ای بزرگ از سلاح‌های ساخت آمریکا به اوکراین است!
این بسته شامل موشک های اتکمز و ۴۷,۰۰۰ گلوله توپ خوشه ای است که به گفته منابع، ارزشی حدود ۲۵۶ میلیون دلار دارند.
واشنگتن آماده تایید این انتقال است، اما سازمان دیده‌بان حقوق بشر از کنگره می‌خواهد که جلوی آن را بگیرد و به خطراتی که سلاح‌های حاوی بمب‌های خوشه‌ای برای غیرنظامیان ایجاد می‌کنند، اشاره کرده است.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/SBoxxx/19943" target="_blank">📅 14:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19942">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">چقدر خوشحالم جای پاکستانی ها نیستم؛
فردای امضای پیمان دفاعی با عربستان، یمنی ها یک کشتی سعودی را زدند که در اثر آن چند پاکستانی کشته شدند!
الان هم سه روز است میگویند ایران و آمریکا دارند سازش می‌کنند اما ولی خب</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/SBoxxx/19942" target="_blank">📅 14:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19941">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سخنگوی وزارت امور خارجه پاکستان:   فرایند صلح گسترده‌تر بین آمریکا و ایران با مشکلاتی روبرو شده است و ما امیدواریم که دو طرف به گفت‌وگو بازگردند.   ما می‌توانیم توافق‌نامه همکاری را قبل از پایان مدت اعتبار آن تمدید کنیم.</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/SBoxxx/19941" target="_blank">📅 14:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19940">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">آذربایجان در پی دریافت کمک‌های ایالات متحده در زمینه فناوری‌های پیشرفته برای پاکسازی مین‌های زمینی است.
دهه‌ها درگیری این کشور را به شدت با مین‌ها و مهمات منفجر نشده آلوده کرده است.
باکو امیدوار است که روابط نزدیک‌تر با ایالات متحده بتواند تلاش‌های نقشه‌برداری و خنثی‌سازی مین‌ها را تسریع کرده و بازسازی پس از جنگ را پشتیبانی کند.
منبع: آکسیوس</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/SBoxxx/19940" target="_blank">📅 14:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19939">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سخنگوی وزارت امور خارجه پاکستان:
فرایند صلح گسترده‌تر بین آمریکا و ایران با مشکلاتی روبرو شده است و ما امیدواریم که دو طرف به گفت‌وگو بازگردند.
ما می‌توانیم توافق‌نامه همکاری را قبل از پایان مدت اعتبار آن تمدید کنیم.</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/SBoxxx/19939" target="_blank">📅 13:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19938">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اردوغان:  «توافق مکه» علیه هیچ کشوری نیست و تمام دولت‌ها می‌توانند به آن بپیوندند  نباید این توافق را به بعد نظامی محدود کرد، زیرا هدف اصلی آن تقویت بعد بازدارندگی و امنیتی است</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/SBoxxx/19938" target="_blank">📅 10:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19937">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حالا باید ببینیم ائتلاف «مکه» پاسخ می‌دهد یا صرفا برای دوشیدن گاو شیرده حجاز و نجد تشکیل شده.</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/SBoxxx/19937" target="_blank">📅 10:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19936">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حجم تحقیری که ترامپ به عنوان رییس جمهور آمریکا دارد می شود کم نظیر است!  پس از افشای داستان فرار ترامپ از ترکیه با یک هواپیمای فرعی — آن هم داخل کامیون کترینگ هواپیما ! — دیروز خبری منتشر شده که ترامپ حتی داخل زمین گلف خودش احساس امنیت ندارد و همانطور که در…</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SBoxxx/19936" target="_blank">📅 08:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19935">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">— کریس رایت، وزیر انرژی ایالات متحده:  به لطف تلاش‌های هماهنگ ارتش ایالات متحده و متحدان ما در خلیج، میانگین هفت‌روزه نفت خروجی از تنگه هرمز در حال حاضر به نزدیک ۹ میلیون بشکه در روز رسیده است.  وقتی این مقدار با ۵ تا ۷ میلیون بشکه اضافی در روز که از طریق…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/19935" target="_blank">📅 07:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19934">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxtcMiJE6jBRKThdjCdoL1VElR4kD0S-jLhRAWYlWCxopMY8E06lystrZ0RfOV2BVr3WD_cmjmwxJ-LH6P4n4klUdtorf7I-kh1g6U1EDo6YYauM3s-L9OR2XdgsWrxZ52cJyI4ZLrqqy_YH5sp6JwCF6IggoJdvpUVWn0WvaWOO4ovAeKyH3ka7Ua_b-vhR-RCOaIPftU9nE4Dt2Et7oNFqvqN-ZjGoVvQEi3aSUu3NmICcOr_opDUFERikqiSwevwR8fFcjlnxi1bcadiWQek4dNchWLY_wogEQPwOYWJpHKRSNNx6g_n-_EONdryCXkRi_FeIIY-_AaMaeWQ_BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— کریس رایت، وزیر انرژی ایالات متحده:
به لطف تلاش‌های هماهنگ ارتش ایالات متحده و متحدان ما در خلیج، میانگین هفت‌روزه نفت خروجی از تنگه هرمز در حال حاضر به نزدیک ۹ میلیون بشکه در روز رسیده است.
وقتی این مقدار با ۵ تا ۷ میلیون بشکه اضافی در روز که از طریق خطوط لوله و تأسیسات صادراتی تازه ارتقا یافته از منطقه خارج می‌شود، ترکیب شود، مجموع جریان‌های نفتی در حال حاضر به طور میانگین حدود ۱۵ میلیون بشکه در روز است.
فقط در روز یکشنبه، بیش از ۲۰ میلیون بشکه از منطقه خلیج عربی خارج شد که این رقم بالاتر از میانگین پیش از درگیری است.</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SBoxxx/19934" target="_blank">📅 07:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19933">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کوشش ژاپن در تقویت توان دفاعی  ژاپن با تأکید وزیر دفاع خود، شینجیرو کویزومی، بر لزوم تقویت و تحول توان نظامی این کشور با «حسی بی‌سابقه از فوریت و بحران» اصرار می‌ورزد. گزارش سالانه سفید دفاعی ژاپن، منتشرشده در ۴ اوت ۲۰۲۶، بار دیگر بر تهدیدات فزاینده چین، کره…</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SBoxxx/19933" target="_blank">📅 06:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19932">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">صدای انفجار در شمال غرب تهران</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SBoxxx/19932" target="_blank">📅 02:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19931">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">صدای انفجار در شمال غرب تهران</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/19931" target="_blank">📅 02:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19930">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">▶️
An oil spill has reportedly polluted a coastline on Iran's Qeshm Island.  @PressTV</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/19930" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19929">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPress TV</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de69aae9a6.mp4?token=Yxzx9AIPxGE1wXSQosTvEqIxziFvfrZboWlhpfVfoGqjqUKKkQ_Z9nWfenNGNPlAx06tJZ3utvKiCf6rEv4SkyZo43KyMm83pCn8U_X9aI02RBg3LQRXhR_-ngJ0c9vltn75A9cjNlDjF8BHxegJ2VlstWXkbwT8GVgtt3XLEzxZnPIuKBevW-7MuyVTW6KBe6a6SF-fQHuGY_7fVUvB-L9HQEVlFzsz7IxSCldOoVXvtILPrZa9ogYrLTyDvvdbLjW9Ezt5EmXJAejoE0ujYLiaNX9RG0JPZ8siNFW_AtdYikAjJw6FxaR3CwUR4oNApD1Uj3mp-DgNE30ZshJN7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de69aae9a6.mp4?token=Yxzx9AIPxGE1wXSQosTvEqIxziFvfrZboWlhpfVfoGqjqUKKkQ_Z9nWfenNGNPlAx06tJZ3utvKiCf6rEv4SkyZo43KyMm83pCn8U_X9aI02RBg3LQRXhR_-ngJ0c9vltn75A9cjNlDjF8BHxegJ2VlstWXkbwT8GVgtt3XLEzxZnPIuKBevW-7MuyVTW6KBe6a6SF-fQHuGY_7fVUvB-L9HQEVlFzsz7IxSCldOoVXvtILPrZa9ogYrLTyDvvdbLjW9Ezt5EmXJAejoE0ujYLiaNX9RG0JPZ8siNFW_AtdYikAjJw6FxaR3CwUR4oNApD1Uj3mp-DgNE30ZshJN7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
An oil spill has reportedly polluted a coastline on Iran's Qeshm Island.
@PressTV</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/19929" target="_blank">📅 02:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19928">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbOaxPexmySVGFKkOve0pQvp6mqjh9wxbZIGeWpFM1UO01OaRz9EpromZFfmuLtBmD9gRNEIttK6_uyhAtRTA4l3ydfdma-WGrKrKiMoHpQtWsrrSlgA41ATli5M5dgSx8QQvsP86LONz3NatZFzKwJJ5GkvLhRKuX3zstBtl9aAuhwrTYg0YRtijYeQs278kM_qwRradIG_U_PcYxO3cZgV6RIKxZbYWnufmQwKm6F1Uy44n1JCubDW-RrdMQGimiD1ITekaVLJgRwQCKhgmR12GTRdA-Ixja2rv1g5Gqa0dtKKgShB_O3slEom9-rEPNu9YTMjKKONZDoQdMdRLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19928" target="_blank">📅 02:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19927">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ:  ما میلیاردها و میلیاردها دلار از ونزوئلا می‌گیریم.  این اتفاق با ایران هم خواهد افتاد.</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/19927" target="_blank">📅 23:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19926">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">این ترکیب و چینش سیاسی و نظامی خبر از جنگی شدید می دهد.  تًن ماهی یادتان نرود.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/19926" target="_blank">📅 23:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19925">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اساساً به حمایت خاصی نرسید که برای خرید اقدام بشود.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/19925" target="_blank">📅 22:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19924">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5N9rpLf4l7y9Onf-9kOl2yv55Y_FVWPxStD49mxmT6uwNBQ7vjRgAG-8GDBEz7lr7538s6uP2PEo-4yr5iOdq2rh9ur-5GBhCRAgsaQ42tQoAtc_WeaK11xMrdMk9KjQaWSoaHy-hIUXL2nJpYueYltsDjPC_PcDjRA6YAA2Fghpy0nKAnQ0GSR6oH2QA15OsGEUX7fFRQuXJ8T_OSPhbH4kcuAXGhd2f-UzgrGpLdM6D0Znlv3DdrfER_kMxbb6oWBdFGQlhMHop9R8PevX6-s_lNYeoTlSTyDK6K7vtfPn-wMTR3b4D6Z4if855jhxJwudKkBPVVbp97r4fOLPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه ای قرار دارد. در چنین شرایطی سیگنال قوی خرید یا فروش صادر نمی شود و بهترین راهبرد از دید من خرید در سطوح حمایتی پایین تر است.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/19924" target="_blank">📅 22:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19923">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بازآرایی ساختار نظامی و امنیتی ایران؛ حرکت به سوی فرماندهی متمرکزتر و مقاوم‌تر   ایران پس از تجربه جنگ‌های ژوئن ۲۰۲۵ و بهار ۲۰۲۶ در حال بازطراحی بخش‌هایی از ساختار نظامی و امنیتی خود است؛ بازآرایی‌ای که به نظر می‌رسد مستقیماً از آسیب‌پذیری‌های آشکارشده در…</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/19923" target="_blank">📅 20:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19922">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گریدم به اسلام آباد و توافق ش. نفت را دریابید.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19922" target="_blank">📅 20:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19921">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی ایران:  پیام ایران روشن است: تنگه هرمز تا زمانی که آمریکا جنگ و محاصره را پایان ندهد، دارایی‌های مسدود شده ایران را آزاد نکند و به آتش‌بس در کل منطقه، از جمله لبنان و غزه، موافقت نکند، باز نخواهد شد.  تا زمانی که تمام…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19921" target="_blank">📅 20:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19920">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">محسن رضایی:   تمام توانم را برای افزایش قدرت ایران به کار خواهم گرفت</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/19920" target="_blank">📅 20:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19919">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این خواهرمیانه درست بشو نیست؛ ببینید کی گفتم.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19919" target="_blank">📅 20:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19918">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3df015c88.mp4?token=RQT1028ZyQUEfWBElefIerKDeR59upzFAH_2tWaejhdbaYinWVD3gKjcuPmVJmb-uegqzC6FoY0HiwtK7UBX98jJ65mHxu5ErHFZl_EKlEfp6LX9o1A4GBzZw1s9nRUxYRkGSKFe0CqoqgTQV_nBIwKqGzNCo28ftP8Z18gVy1z3OBNbvigWw6vAblLpQQC8DigyOJCt3qQCDxGrZSpUBgBzGOZpALkD_xN_HRsY04thfYw-5IgHgC4Wd7Go7KFzTj81FQ1eTevzhasPDla4KOyJdQVERMLWeBmDD-Uxpcz7xf7u8MIM7G89SiK_xpeLonQ8ptVSawloThktxARGww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3df015c88.mp4?token=RQT1028ZyQUEfWBElefIerKDeR59upzFAH_2tWaejhdbaYinWVD3gKjcuPmVJmb-uegqzC6FoY0HiwtK7UBX98jJ65mHxu5ErHFZl_EKlEfp6LX9o1A4GBzZw1s9nRUxYRkGSKFe0CqoqgTQV_nBIwKqGzNCo28ftP8Z18gVy1z3OBNbvigWw6vAblLpQQC8DigyOJCt3qQCDxGrZSpUBgBzGOZpALkD_xN_HRsY04thfYw-5IgHgC4Wd7Go7KFzTj81FQ1eTevzhasPDla4KOyJdQVERMLWeBmDD-Uxpcz7xf7u8MIM7G89SiK_xpeLonQ8ptVSawloThktxARGww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز زمینی بچه های تیم New Castle !  همه هم پنج سانت و ده سانت و …</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19918" target="_blank">📅 20:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19917">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حجم تحقیری که ترامپ به عنوان رییس جمهور آمریکا دارد می شود کم نظیر است!  پس از افشای داستان فرار ترامپ از ترکیه با یک هواپیمای فرعی — آن هم داخل کامیون کترینگ هواپیما ! — دیروز خبری منتشر شده که ترامپ حتی داخل زمین گلف خودش احساس امنیت ندارد و همانطور که در…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19917" target="_blank">📅 20:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19916">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ:   ایرانی‌ها با ما بازی می‌کنند، در اتاق‌های جلسات موافقت می‌کنند و در رسانه‌ها رد می‌کنند.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19916" target="_blank">📅 18:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19915">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ: ایالات متحده می‌تواند به زودی با قدرت بسیار زیاد به ایران حمله کند.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19915" target="_blank">📅 18:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19914">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNiBo_Ht3r2QxhJEGSU-VGDkgFQq17zg-oY9B6-gtkp2nSD5nnc9sJeM2j3Byn8VhNGIyrA4_McEKoQ6t0Mo5fOZDuwfy04FnmX8oiGxO4kq7NGGjTFbDM1WTrq7AbLRVKqj4MZ-_TH_a6Lk6JAP7z0OtWj2PO7H0dHX1mQY-uZaiPwgc3pI95p_WqMfRaPJ4tUy_GsDV9nxXwPG7lpPCWVmq2v4FeoS-HoBrdWVpjU2f5tcCYCxUFwnEjfT5oQeBxAeqjqUdUHyeAYiaO3M2NGIHPE_-caX87PjZn8bu_MU66Wxy3314lNcl7C0QY_StEY7jj-AsnpmuaiHtV951Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط کم‌سابقه قتل در آمریکا
داده‌های جدید مربوط به نیمه نخست سال ۲۰۲۶ تصویری کم‌سابقه از وضعیت امنیت شهری آمریکا ارائه می‌کنند. بر اساس داده‌های Major Cities Chiefs Association که در نمودار نیز منعکس شده، در شماری از شهرهای بزرگ آمریکا میزان قتل به‌شدت کاهش یافته است.
این کاهش‌ها صرفاً محدود به چند شهر نیست. تحلیل داده‌های MCCA نشان می‌دهد که قتل در مجموعه شهرهای بزرگ آمریکا در نیمه نخست ۲۰۲۶ نسبت به مدت مشابه سال قبل حدود ۱۷.۲ درصد کاهش یافته است؛ بنابراین با یک روند گسترده‌تر در سراسر کشور مواجه هستیم، نه صرفاً یک اتفاق محلی.
یکی از عواملی که می‌توان در این تحول مورد توجه قرار داد، تغییر شدید سیاست مهاجرتی دولت آمریکا تحت رهبری دونالد ترامپ است. دولت ترامپ از آغاز دوره دوم ریاست‌جمهوری خود سیاستی بسیار سختگیرانه‌تر در قبال ورود غیرقانونی، بازداشت و اخراج مهاجران غیرقانونی اتخاذ کرده است. بر اساس آمار ارائه‌شده از سوی کاخ سفید، دولت در کنار کاهش شدید عبورهای غیرقانونی از مرز جنوبی، تعداد اخراج‌ها و بازداشت‌های مهاجرتی را نیز افزایش داده است.
از منظر سیاسی، دولت ترامپ این سیاست را مستقیماً بخشی از برنامه بازگرداندن امنیت عمومی معرفی می‌کند. افزایش فعالیت ICE، تمرکز بر افراد دارای سابقه کیفری، مقابله با شبکه‌های تبهکاری و کارتل‌ها و کاهش شدید ورود غیرقانونی، همگی می‌توانند از دیدگاه دولت نوعی افزایش بازدارندگی ایجاد کنند. داده‌های موجود نیز نشان می‌دهد اجرای سیاست‌های مهاجرتی در دوره ترامپ به‌طور محسوسی تشدید شده است؛ برای مثال، یک تحلیل مبتنی بر داده‌های ICE نشان می‌دهد تعداد بازداشت‌های ICE در مقطعی از سال ۲۰۲۶ نسبت به نیمه دوم دوره بایدن چند برابر شده است.
با این حال، نباید از نمودار فوق یک رابطه علّی قطعی میان سیاست مهاجرتی ترامپ و کاهش قتل استخراج کرد. روند کاهش جرم پیش از آغاز دولت دوم ترامپ نیز شروع شده بود و خود آکسیوس نیز تأکید می‌کند که کاهش جرم در دوره پایانی دولت بایدن آغاز شده و سپس در دوره ترامپ ادامه یافته است. علاوه بر این، عوامل متعددی مانند افزایش یا بهبود عملکرد پلیس، تغییر الگوهای باندهای جنایتکار، وضعیت اقتصادی، کاهش خشونت پساکرونا و سیاست‌های محلی می‌توانند در این روند نقش داشته باشند.
با این وجود، از منظر سیاسی می‌توان استدلال کرد که سیاست «مرزهای بسته‌تر، اخراج سریع‌تر و برخورد سخت‌تر با مجرمان» یکی از مؤلفه‌های محیط امنیتی جدید آمریکا است. کاهش ۶۰ درصدی یا بیشتر قتل در چندین حوزه قضایی، همراه با افت ۱۷.۲ درصدی در شهرهای بزرگ، نشان می‌دهد که آمریکا در حال تجربه یک چرخش مهم در شاخص‌های خشونت شهری است. بنابراین، حتی اگر هنوز برای نسبت‌دادن این تحول به یک سیاست مشخص زود باشد، دولت ترامپ اکنون می‌تواند این آمار را به‌عنوان شواهدی از موفقیت رویکرد امنیت از طریق اعمال قانون و کنترل مهاجرت در برابر منتقدان خود مطرح کند.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/19914" target="_blank">📅 18:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19913">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ:
ایالات متحده می‌تواند به زودی با قدرت بسیار زیاد به ایران حمله کند.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19913" target="_blank">📅 18:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19912">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خواجه آصف وزیر دفاع پاکستان، گفته است که ایالات متحده و ایران به توافقی در مورد تنگه هرمز نزدیک می‌شوند، با وجود اینکه هر دو طرف اخیراً مواضع سخت‌تری را در مذاکرات اتخاذ کرده‌اند.  او گفت: "به نظر می‌رسد که اوضاع به نفع صلح پیش می‌رود."</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19912" target="_blank">📅 16:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19911">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">محسن رضایی:
تمام توانم را برای افزایش قدرت ایران به کار خواهم گرفت</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19911" target="_blank">📅 16:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19910">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خواجه آصف وزیر دفاع پاکستان، گفته است که ایالات متحده و ایران به توافقی در مورد تنگه هرمز نزدیک می‌شوند، با وجود اینکه هر دو طرف اخیراً مواضع سخت‌تری را در مذاکرات اتخاذ کرده‌اند.  او گفت: "به نظر می‌رسد که اوضاع به نفع صلح پیش می‌رود."</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19910" target="_blank">📅 16:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19909">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خواجه آصف وزیر دفاع پاکستان، گفته است که ایالات متحده و ایران به توافقی در مورد تنگه هرمز نزدیک می‌شوند، با وجود اینکه هر دو طرف اخیراً مواضع سخت‌تری را در مذاکرات اتخاذ کرده‌اند.
او گفت: "به نظر می‌رسد که اوضاع به نفع صلح پیش می‌رود."</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19909" target="_blank">📅 16:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19908">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یک نفت کش که قصد داشته محاصره دریایی آمریکایی را بشکند هدف آتش نیروهای آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19908" target="_blank">📅 16:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19907">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بازآرایی ساختار نظامی و امنیتی ایران؛ حرکت به سوی فرماندهی متمرکزتر و مقاوم‌تر
ایران پس از تجربه جنگ‌های ژوئن ۲۰۲۵ و بهار ۲۰۲۶ در حال بازطراحی بخش‌هایی از ساختار نظامی و امنیتی خود است؛ بازآرایی‌ای که به نظر می‌رسد مستقیماً از آسیب‌پذیری‌های آشکارشده در جریان حملات آمریکا و اسرائیل، به‌ویژه عملیات هدف‌گیری فرماندهان ارشد، ناشی شده باشد. مهم‌ترین تحول در این روند، تلاش برای ادغام ستاد کل نیروهای مسلح و ستاد مرکزی خاتم‌الانبیا است. ستاد کل مسئول سیاست‌گذاری و راهبرد نظامی و خاتم‌الانبیا مسئول فرماندهی عملیات مشترک در زمان جنگ است. جدایی این دو نهاد از سال ۲۰۱۶ یکی از منابع بالقوه موازی‌کاری در ساختار فرماندهی محسوب می‌شد و اکنون ادغام آنها می‌تواند با هدف ایجاد یک زنجیره فرماندهی کوتاه‌تر و منسجم‌تر انجام شود.
منطق این ادغام، صرفاً اداری نیست. ساختار جدید می‌تواند هماهنگی میان ارتش و سپاه را افزایش داده، کاغذبازی و بوروکراسی نهادی را کاهش دهد و سرعت تصمیم‌گیری در شرایط جنگی را بالا ببرد. اهمیت این مسئله پس از حملات «سر بریدن» بیشتر شده است؛ حملاتی که با حذف فرماندهان ارشد، توانایی ایران برای هماهنگی عملیات تلافی‌جویانه را مختل کردند. بنابراین، ایرلت ظاهراً در حال حرکت از مدلی است که در آن بخشی از ظرفیت فرماندهی به افراد و نهادهای متعدد وابسته است، به سوی ساختاری که بتواند حتی پس از حذف بخشی از رأس فرماندهی نیز به فعالیت خود ادامه دهد.
انتصابات جدید نیز همین جهت‌گیری را تقویت می‌کنند. علی عبداللهی علی‌آبادی در رأس ستاد کل قرار گرفته و هم‌زمان نقش او در خاتم‌الانبیا، وی را در مرکز ساختار فرماندهی مشترک قرار می‌دهد. سوابق او در سپاه، فرماندهی انتظامی، وزارت کشور و ساختار ستاد کل، ترکیبی از تجربه نظامی و امنیت داخلی را فراهم می‌کند. در کنار او، کیومرث حیدری، با سابقه فرماندهی نیروی زمینی ارتش و فعالیت در خاتم‌الانبیا، به لایه بالای ستاد کل اضافه شده است.
در سپاه نیز تثبیت احمد وحیدی در مقام فرمانده و انتصاب مصطفی ایزدی به‌عنوان معاون فرمانده، نشان‌دهنده بازسازی سریع زنجیره فرماندهی پس از ترور محمد پاک‌پور است. انتخاب ایزدی، که اخیراً مسئول حوزه سایبری و تهدیدات نوظهور خاتم‌الانبیا بوده، می‌تواند بیانگر اهمیت فزاینده جنگ مدرن، حوزه سایبری و تهدیدات نوظهور در معماری دفاعی جدید ایران باشد. انتصاب حسین طائب به فرماندهی بسیج نیز نشان می‌دهد که بازآرایی نظامی با لایه امنیت داخلی و بسیج اجتماعی پیوند خورده است.
در سطح امنیت ملی نیز تغییر دبیر شورای عالی امنیت ملی و جابه‌جایی مشاوران ارشد، بخشی از همین روند تمرکز قدرت و هماهنگ‌سازی ساختار تصمیم‌گیری است. در مجموع، تصویر ارائه‌شده در انتصابات اخیر حاکی از آن است که ایران پس از تجربه آسیب‌پذیری فرماندهی در جنگ‌های اخیر، در حال ایجاد ساختاری متمرکزتر، یکپارچه‌تر و کمتر وابسته به یک فرد یا نهاد منفرد است؛ ساختاری که هدف آن افزایش سرعت واکنش، هماهنگی ارتش و سپاه و حفظ تداوم فرماندهی در صورت تکرار حملات علیه رأس هرم نظامی است.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/19907" target="_blank">📅 16:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19906">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wh2Z5D564j-ubdA3aLEPA4bzKtKKsZ7mp90SBpOxuxlwN_IOOY7S1C0ZE2WtOhemlTGIeU-LyVca4Je-1cMUmbuMgu4o8-pIBVpYr_N_2tG7cydoGBnTHRKXBkrWECQUAQa7jiAMAigUDr9ED8VlJ1yqOqyR70oskpskM-J5jjr15HfIFXvLhnrC7Ih5iM5vVb3d-lE1s2AGIOT3Q-aeGr4vodXhFZ3cErFsBjr8AHkFCTxds_gPPC2WmUnDPXuZU6Oe9n2XwpQcT9bnC6IgqJFWCy0_OWPt8n25Sf26rF7fLM9FTP_eQ2uzqDLR-_QknAI-lAdRqxLo-PlIBdW3_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه درگیری های میان انصارالله و نیروهای دولت رسمی یمن</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/19906" target="_blank">📅 15:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19905">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845af07e2f.mp4?token=TDBno6PTFcv2H4abGPOByN20D_ahLmBIQgzA9FV6q2XvwcLBsn5Yt7Ihd9ZYvas41LMqQohDnX3DdFnywpK4cl_-eWrgFFeKKTi16t0cEbWo3q1TiU6QnCCt7gSZzwNxUw2xpuihtqTtBiYZFrfKGxp8-AkteiwGqivP8KDXZZZA2nGBEIOKG2juLJyFKv6ppDj6lLxhaIupId98QMdOOn6UKejM7aBFiPTcvDw2ctai2TzKNyEqAL0PbFpLnTTWqiQP95jkD7naNtyRUyqLPutfvFlJ_MEBwy5loUzzgytPq-Bsq3FXrT65O0uOfUl319LwIvmis5CAwgUBenlNKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845af07e2f.mp4?token=TDBno6PTFcv2H4abGPOByN20D_ahLmBIQgzA9FV6q2XvwcLBsn5Yt7Ihd9ZYvas41LMqQohDnX3DdFnywpK4cl_-eWrgFFeKKTi16t0cEbWo3q1TiU6QnCCt7gSZzwNxUw2xpuihtqTtBiYZFrfKGxp8-AkteiwGqivP8KDXZZZA2nGBEIOKG2juLJyFKv6ppDj6lLxhaIupId98QMdOOn6UKejM7aBFiPTcvDw2ctai2TzKNyEqAL0PbFpLnTTWqiQP95jkD7naNtyRUyqLPutfvFlJ_MEBwy5loUzzgytPq-Bsq3FXrT65O0uOfUl319LwIvmis5CAwgUBenlNKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر امنیت ملی اسرائیل بن گویر:  برای هر اشک یک مادر اسرائیلی، هزار مادر لبنانی باید بگریند. تمام لبنان باید بسوزد!</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/19905" target="_blank">📅 14:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19904">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">302.8 KB</div>
</div>
<a href="https://t.me/SBoxxx/19904" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 23</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/19904" target="_blank">📅 14:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19903">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">صد رحمت به جنگ (تحلیل ژئواکونومیک محاصره دریایی)  مجیدرضا حریری، رئیس اتاق بازرگانی ایران و چین، طی گفتگو با خبرآنلاین با تاکید بر ضرورت فوری پایان یافتن محاصره دریایی بنادر جنوبی ایران توسط سنتکام، گفته است: این محاصره باید پایان یابد؛ با مذاکره، خواهش، تهدید…</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/19903" target="_blank">📅 14:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19902">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آیا صادرات نفت ایران از مسیر ریلی می‌تواند جایگزین صادرات دریایی شود؟   در هفته‌های اخیر گزارش‌هایی منتشر شده مبنی بر اینکه ایران در حال بررسی استفاده از مسیرهای ریلی برای انتقال نفت خود به چین، به‌ویژه از طریق خاک افغانستان و آسیای مرکزی، است. این ایده در…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19902" target="_blank">📅 14:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19901">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 23</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19901" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 23
سه شنبه 11 آگوست 2026</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/19901" target="_blank">📅 13:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19900">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گزارشگر: گفتید این آخرین شانس ایران است. حالا چه؟  ترامپ: خواهید دید.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/19900" target="_blank">📅 11:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19899">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1_4_2arJkbndq-H0507J0O85z1Pvsb0vA1wMA88z3q3wKSTfohkHa2fqBXxiTgXoPPo2c_pFomDPPLL7V-Ttg78o4DbDhgBQqOCL1N4S1e0jdA6WnyhxDuGR8fpHX94LNaUqT37jybe85s8xKpmDmfmQZLxyd88bAlCRkmuwO4cBn10lhHKnC_H_6rHrb-lkm-depyNEOuVCIBIc1T4cISB1YAorzgJijwHmEC16TDhv8rMXFpdmkds2zMo9zQitueOiZVWiDO13qo1zdH0SG3eb2hv_ZvmImXDECurmBw8Ejq9_KuM5OOQgaEJfY1McxxA3_oOQvMNhVrZbnFNYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه ای قرار دارد. در چنین شرایطی سیگنال قوی خرید یا فروش صادر نمی شود و بهترین راهبرد از دید من خرید در سطوح حمایتی پایین تر است.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/19899" target="_blank">📅 11:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19898">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZ8oH1BD0pbK7_F-iP2BHLQY5PgWoFFdM4B8iX9iw0bRqGkvh2isn8Dz7upZCLblzSJbcjEZp3BmmNZ1mqkaAVMWqH_zjyAT_cSPsHesV2URJzcKRIaNKsyIbRYbGKhCppfglM-j4yHLjN2T3LFsnXfsbzapydvJVeq60eOOx61lr7t-f0o95qODiLWNm2_rXuGLXbGTpMMbssKEwgFy0-uCzFfu3sc7OK59zWExd7S6aQZG5ZnkGCZwHehTr718BnL7madZEMpXOW8vYaYIhvOLc6fT068f-sFoMaNseQlGXKZthpgsh2LisvkNWNK8Pbx8CfELFJyoI5kIVmJ-kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با برجسته کردن بیگانگی فرهنگی امثال این چپول عرب تبار با فرهنگ غربی غالب در آمریکا به دنبال کاهش امکان شکست جمهوریخواهان در انتخابات نوامبر است.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/19898" target="_blank">📅 11:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19897">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انزوای روزافزون در جهان   کاهش اهمیت راهبردی خاورمیانه برای واشنگتن و برونسپاری مدیریت خاورمیانه به اعراب مسلمان  قدرت گیری روزافزون ترکیه و محور اخوانی  نیاز به حضور مستقیم در بازی کریدورها</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19897" target="_blank">📅 11:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19895">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHXkzcJx1PQUET_mlfLoE7aNyIj2XXqa4TaX3rqlHWuSeeQU8jPG7En63Jf3w1ucWqz5whSn3mks5YNc-bPI4MUSQ3gBs9XJ99aLI32Ae4nLnH1b3iDNO1BwGc5Bt6GOne6Gxm3RGppfppPQP8qUaMJzQ-dgSO-USXXNWZxlmCrFgPAy4WV4XlcpcSHET-QGvJzHoUDdZQL7Dq-oFkKb5qOKvQvzyPcaGjaPFVVHGn4qV4c_o0n5UHqR0BRKiiujaTCwL7BqoiFYuh2eMQ8OSJmErI77gz2tDPjKmDGfK9cMnjkJTtQgovQ4C0p-lJSwXm5hKFCMbc8YGrfoCqGJDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sOTnxqrOFW5e4K8uZp4t4b1UGOS9CY2p61CHvcqewv4w-zE5g1zLZrCMSNu2eHD1moiwQweTz7ehwbbI_fw19pDXRkxcuXWlsS4IMntbAcTVZd3mPNbXbshDm9aFoIzY0uNHCoG1zZ56OxAjdAMfjIBvYuzxlB2ANIDa0an9WvB_43Oa0qL47X6Dk9MZDxTvQlQ1BADcNW575PtqbA9c8T-oao6i8gcRQ4ONV7ehU0dAJno2vOdd2rpoaKlYIsrWNwzCnJhtG4i8Iwd9PlotbQJk_YfEvFXVUJ6KjhZo-eaqH-vdQNCPH9hWI9rlvyO1VJv_PcnHDXSePYITRzFpzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گزارش واشنگتن پست، دونالد ترامپ، رئیس‌جمهور، ماه گذشته پس از نشست ناتو، به دلیل تهدید ترور از سوی ایران، به صورت مخفیانه با یک هواپیمای C-32A نیروی هوایی ایالات متحده از آنکارا، ترکیه، خارج شد، در حالی که کاخ سفید به صورت عمومی اعلام می‌کرد که او با هواپیمای…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19895" target="_blank">📅 11:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19894">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انصارالله یک کشتی تجاری عربستان را در باب المندب زد و ۳ نفر کشته شدند.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/19894" target="_blank">📅 10:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19893">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فعلاً 2 کشور در خواهرمیانه با ائتلاف «مکه» مخالف هستند: ایران و اسرائیل</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19893" target="_blank">📅 03:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19892">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">طبق گزارش واشنگتن پست، دونالد ترامپ، رئیس‌جمهور، ماه گذشته پس از نشست ناتو، به دلیل تهدید ترور از سوی ایران، به صورت مخفیانه با یک هواپیمای C-32A نیروی هوایی ایالات متحده از آنکارا، ترکیه، خارج شد، در حالی که کاخ سفید به صورت عمومی اعلام می‌کرد که او با هواپیمای…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/19892" target="_blank">📅 02:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19891">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zfy_kw6CwpyZyUC-7Pz5OTU8WKqiwNax4wWLijTujjcwuv35RGtwQwEoQ7Rg4hrD2A8w_nO4J0yyw4aHdk9yzAgfMJ75gtkNgzTrARSpf37BLwDTEl4WhthO83GE0UpWPH22Wt32Ihluo9L6YK8ypYmHVXMvAj0taBQ3Zd5vNCWgrJa5U56eJIAaTHk3yha_6WuI3lWzEJ2PQz7u7YIYKHrRwFGseHNec__J5w7uGkUMP46gy82EB9kJhlLUH3rMASRmG6yC3ay10xAPdlgM8HbUReUztWzWc7-Rtk7o7jnsJ45xUj2h6991GE--ltrUrBXUHgyxJF4OkGh5IeoYdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفته می‌شود ایران در جریان سفر ترامپ، رئیس‌جمهور آمریکا به ترکیه، تلاش کرده است او را ترور کند.  اطلاعات ارائه شده توسط یک منبع خارجی که به مقامات آمریکایی در مورد این توطئه ادعایی هشدار داده بود، باعث شد تا در آخرین لحظه، هواپیمای مورد استفاده رئیس‌جمهور…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/19891" target="_blank">📅 02:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19890">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPv_BIWpLbLZrlI5Wpug9ebSWAtM9NF3Jx01AR36yZm5zb9KrEzPfhudLIgyCXn7y-BcN4DHVqc_6zDJyXtFodsRzVYn9tn0C8kfcnbfCE_wOM6w-eUXeb5Rf3QlxsCw3GMGlU8swhHlQ7Aa7sFbqULBKjDem06kzYvOfasxiUOWVi5Ecp22ia948L1vwnSN9poj5O2MSoc3RG-fHPLr5Pej_sktggK2XWP2XJERQr5l7e6n3vk0fz96MrTSBbVsHE3H1ZVMezi1ufNysldPnqt4BwLwFanhTKvVEHU-ew4yBc3394LSd09pai_chpq7s6IFk_JT8zd0fUzLFwATUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلاً 2 کشور در خواهرمیانه با ائتلاف «مکه» مخالف هستند: ایران و اسرائیل</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/19890" target="_blank">📅 02:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19889">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQRAP251Os6lfDownToWaFRPoiw0UCvJ0fRgNr-1arTlt2vttPUTYbapNdFGTAKSEeAoX1k91vAzBkFYGb7FGf6HUmAnqZoyI50WsAYMNVVGsR_BmubNypHkfrQ59765_xmDwfLvm6MOwG_wT6WFggaVTb8b5upSg7F2RgWem4J92JeXfu9mXQSKkTKovvQJQEGIh-oGRqTyIQdsbHMD_ImHWp0XTdV2ydxLnbKJm6id-6hH-7g8txPDNQoL1P2Tvlnj24w9-7EGNFLrLHa7Ts_p2z-CGjc_MA3-IBzofgw3dGevONtI07lspk6RPL1U9jxWf2S_V0vBHoLxyZwMkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از زمان آغاز جنگ ، ایران بیش از ۲۰۰۰ حمله هوایی، موشکی و پهپادی در سراسر خاورمیانه انجام داده و حداقل ۲۰ سایت مورد استفاده ارتش ایالات متحده در هشت کشور را آسیب رسانده است.
این حملات تا ۱۳ میلیارد دلار خسارت به تجهیزات ایالات متحده و تأسیسات نظامی وارد کرده است.
بیش از ۴۲ هواپیمای نظامی ایالات متحده نیز آسیب دیده یا نابود شده‌اند، از جمله چندین فروند که در پایگاه‌های هوایی پارک شده بودند.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19889" target="_blank">📅 01:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19888">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e06c6847.mp4?token=VgwJXpxAm11XD4So9HCjHFP3fyEnjyKzrya4btjvB91nTIbv4JztnklX_9wnAxuAZ5Uwe2huTpgYZYiYupnS1ajckXZWQM6IQt-KRaMHIyoWbSoFDKj9TYfBQLtQRiu15TDUBijXyVq8rDjOfau_kYEr6uoE_E1bszsPnb1VWF6Ns5DdRrTzczHrCYVHX4rS77LtbeYH2Qkldv3l-Bex7i14r07bAojD-PGJyVuN4xIEHVBHpJXVpHToVDHqCzEhwUY9OvbJ-yiJwO7Qri3O1QdtKfHS6h6oOKRUqs7njey13GOwP_bzhvtQy1_WzUSLJSVDmKJxN6Qd_L2No1WeWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e06c6847.mp4?token=VgwJXpxAm11XD4So9HCjHFP3fyEnjyKzrya4btjvB91nTIbv4JztnklX_9wnAxuAZ5Uwe2huTpgYZYiYupnS1ajckXZWQM6IQt-KRaMHIyoWbSoFDKj9TYfBQLtQRiu15TDUBijXyVq8rDjOfau_kYEr6uoE_E1bszsPnb1VWF6Ns5DdRrTzczHrCYVHX4rS77LtbeYH2Qkldv3l-Bex7i14r07bAojD-PGJyVuN4xIEHVBHpJXVpHToVDHqCzEhwUY9OvbJ-yiJwO7Qri3O1QdtKfHS6h6oOKRUqs7njey13GOwP_bzhvtQy1_WzUSLJSVDmKJxN6Qd_L2No1WeWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز زمینی بچه های تیم New Castle !
همه هم پنج سانت و ده سانت و …</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19888" target="_blank">📅 01:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19887">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ درباره ایران:  آن‌ها می‌توانند دردسر درست کنند، اما ورشکسته هستند. پولی ندارند.  ایران کاملاً ورشکسته است. آن‌ها به سربازانشان حقوق نمی‌دهند.  تورم آن‌ها ۳۰۹ درصد است.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19887" target="_blank">📅 00:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19886">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گزارشگر: گفتید این آخرین شانس ایران است. حالا چه؟  ترامپ: خواهید دید.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19886" target="_blank">📅 23:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19885">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گزارشگر: گفتید این آخرین شانس ایران است. حالا چه؟
ترامپ: خواهید دید.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19885" target="_blank">📅 22:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19884">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ایران_تا_چه_اندازه_می‌تواند_تنگه_هرمز_را_به_یک_سلاح_ژئوپلیتیکی_تبدیل.pdf</div>
  <div class="tg-doc-extra">538.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/19884" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اسکات بسنت در مورد تنگه هرمز:  تنگه هرمز دیگر هرگز به وضع سابق خود باز نخواهد گشت، زیرا ایرانی‌ها از آن به عنوان یک گلوگاه استفاده کرده‌اند، یا تلاش کرده‌اند از آن به همین منظور استفاده کنند.  آنچه در 2 سال آینده شاهد خواهیم بود، این است که تنگه هرمز از اهمیت…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19884" target="_blank">📅 22:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19883">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Po5wSHU_rRoSrYd9wZl7_YCA8trnh8pwwJJokLv7XQ_QVgHr60KRXLLI804PJQNSZ3PaZ4ht4vL4PJRC-qGvKv2cAKGxYKvbIpCr-bfvYigzwg-ttXpsQUsHHMbGF5AGzUdbpYYj92HXub7eUHA9vaSiN6d-sFWLCYh9va36ltx-qt6eVI4b6muCE4619nW2SRyR2nSQY_NO709sJWx4VH4pPLlGLXsyks_SDKuzDsVrMSaPMknLVhf5JxdUj3ezOMkPvTp5aM3mMfcx_kFyRIDvmHS__tddvxrKCRy3rzcslXUi_TL_UdkdcT_lk-0LSh6cyIlwl0hlYMdPPQkYVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح پایینی است و لذا اصلاح های محتمل نزولی طلا خرید دارد.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19883" target="_blank">📅 21:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19882">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">302.5 KB</div>
</div>
<a href="https://t.me/SBoxxx/19882" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 22</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19882" target="_blank">📅 21:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19881">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آمریکا پس از سوگند یاد کردن آبلاردو د لا اسپریلا، که با حمایت ترامپ به عنوان رئیس‌جمهور انتخاب شد، متعهد به ارائه یک میلیارد دلار کمک به کلمبیا شده است.  او وعده «جنگ تمام‌عیار» علیه تروریسم مواد مخدر، سرکوب نظامی سخت‌گیرانه‌تر علیه گروه‌های مسلح و روابط امنیتی…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19881" target="_blank">📅 20:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19880">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ:
🔹
من متوجه شدم که نمایندگان جمهوری اسلامی ایران درخواست غرامت برای خساراتی که در طول درگیری نظامی پنج ماه گذشته به آنها وارد شده است، دارند (درگیری که به این دلیل آغاز شد که "آنها نباید سلاح هسته‌ای داشته باشند"). با این حال، این موضوع در هیچ یک از…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19880" target="_blank">📅 20:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19879">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">شرایط ایران برای باز کردن تنگه هرمز</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19879" target="_blank">📅 20:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19878">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔖
واشنگتن پست :
پنتاگون به مدیران صنایع دفاعی ۲۱ روز فرصت داد تا طرحی برای تولید سریع تسلیحات ارائه کنند</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19878" target="_blank">📅 18:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19877">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VI9tJOpOxglNfrArPxinIQqpxm9RMVopeZtdJik15haItIh-YhiQkSAaSa8-MySxFTGI0sPkid88C090UbBwv2IvIrLBbm1tNCoXGk74S4UIQsg594moEX0w2f9EABi7_j5jXgH7talFY606GfVhwK6Nw3eJry4da-8UAu7jQPO41cFtnXwae6SHnRU6eTNA05qZ4Lfp2rlnbhCfLTW6xmT7Nti5lj5ezXfS8PeqASIMQcH8poAt6IqHWl8XP2fQM7day7vzhDQChFjmMuaDQe9GsSEek0hFKKQ3G_U3wTBkrMHm6u7BlfzIblDcvXJDKJDGNy7XmvaBLaNeptG8-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
قانون «لیندسی گراهام»؛ تشدید فشار بر روسیه و ایران و آغاز یک جنگ اقتصادی با پیامدهای جهانی
قانون لیندسی گراهام با هدف تشدید فشار اقتصادی بر روسیه و ایران، تحریم‌ها را فراتر از کشورهای هدف برده و خریداران انرژی آنها، به‌ویژه چین و هند، را نیز تحت فشار قرار می‌دهد.
اجرای این سیاست می‌تواند جریان تجارت انرژی، قیمت نفت، تورم، نرخ بهره، دلار و بازارهای جهانی را تحت تأثیر قرار دهد و تحریم‌ها را به ابزاری برای شکل‌گیری یک جنگ اقتصادی گسترده‌تر تبدیل کند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19877" target="_blank">📅 16:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19876">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-5VXZnn42Q4aIicg4jSp3YcVp5FIBtR4mWvXhGW_Wt1ZXiffW4drgpyRHrA6BtFcks7EqYxQ0geJnGHoocwh3ryeZlEkpRPIxsMUhS_S-scOnM9DnwQtmMPPIclbOpWyycs_IZEf6HjVKiizzTjN2m3ShXreheGks2vkhFLk26-3LEioQ2Y1fSOYs23MUWzkbyOwjP-FyfuvutcXspTMPmevGEcukp2-M4yYpiGoqz6C6s4CR8V2WRwP4p9-H5BlOcU1NubPb2ipcA4UgpnZYqX85H5oMH3Gt7SZ8pIBj8_VcS7f2r1yok0A4YwibOmMvVwBx1BF6q_6UMfsLB6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان:  علم را اگر بتوانیم توسعه بدهیم نیازی به نفت و گاز نداریم. ﻿</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19876" target="_blank">📅 16:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19875">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 22</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19875" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 22
دوشنبه 10 آگوست 2026</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19875" target="_blank">📅 14:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19874">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">— وزارت کشور عراق:
«هر پهپادی که بدون مجوزهای لازم پرتاب شود، به عنوان عملی تروریستی تلقی خواهد شد».</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19874" target="_blank">📅 13:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19873">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19873" target="_blank">📅 13:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19872">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فعلاً 2 کشور در خواهرمیانه با ائتلاف «مکه» مخالف هستند: ایران و اسرائیل</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19872" target="_blank">📅 12:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19871">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مایک والتز، سفیر ایالات متحده در سازمان ملل:  "عربستان سعودی، ترکیه، پاکستان و احتمالاً مصر در حال تلاش برای تشکیل یک ائتلاف دفاعی برای مقابله با ایران هستند."</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19871" target="_blank">📅 12:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19870">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6D2-UyWtjYmSb8GrG44jPbdtr8aLvMAdpVsXhWY6VVrbrM3J0P418_HG7A0w_bF17zGGwM703zfNA3wd5A52UfRWZp7IseP1_yQd4yB8ojoeuErmX9yWmFtR_f11Fn98SXbXU7bcF7PdmR829jfxRcnNfro0Xw-NcWYG0hLWx-cplBBINj0T9WIYK901YBoLD8Fyd_OQW0a6EWvANNi7MbnoeIzkzJFrM835QnBH9KbJ_5rReQWsZL1MSQfjjcnP_UJGBACK6UDtnEqIpm98UYppvmKe2k4JQRe5T1ti-SvXYnGv2NIHwTV1OIV0WqRI5bLifsY6pqD7rrfiUt-HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل جدیدترین و پیشرفته‌ترین زیردریایی خود را از آلمان تحویل گرفت
شرکت آلمانی
ThyssenKrupp Marine Systems (TKMS)
در اواخر ژوئیه ۲۰۲۶ زیردریایی جدید اسرائیل،
INS Drakon
، را در شهر کیل تحویل نیروی دریایی اسرائیل داد. این زیردریایی، ششمین فروند از خانواده
Dolphin
و سومین نمونه از نسل ارتقایافته
Dolphin II
در ناوگان زیرسطحی اسرائیل محسوب می‌شود.
دراگون با طول حدود
۷۳ متر
و جابه‌جایی بیش از
۲ هزار تن
، بزرگ‌ترین زیردریایی ساخته‌شده برای نیروی دریایی اسرائیل تاکنون است. این زیردریایی توسط شرکت آلمانی TKMS ساخته شده و از سامانه پیشران مستقل از هوا (
AIP
) بهره می‌برد؛ قابلیتی که امکان ماندگاری طولانی‌تر در زیر آب و انجام مأموریت‌های پنهانی در فواصل دور را فراهم می‌کند.
ارزش این زیردریایی در منابع مختلف حدود
۵۰۰ میلیون یورو
برآورد شده است. طراحی پیشرفته، برد عملیاتی بالا، سامانه‌های شناسایی مدرن و ظرفیت حمل تسلیحات مختلف، INS Drakon را به یکی از مهم‌ترین عناصر قدرت دریایی اسرائیل تبدیل می‌کند.
ورود این زیردریایی به ناوگان اسرائیل تنها یک ارتقای فنی نیست، بلکه پیامی راهبردی درباره حفظ برتری دریایی این کشور در محیط امنیتی متغیر خاورمیانه و شرق مدیترانه محسوب می‌شود.
در سال‌های اخیر، افزایش حضور نظامی ترکیه در شرق مدیترانه، توسعه نیروی دریایی این کشور، برنامه‌های مربوط به زیردریایی‌های جدید و رقابت بر سر نفوذ منطقه‌ای، اهمیت توان زیرسطحی اسرائیل را افزایش داده است. زیردریایی‌هایی مانند
INS Drakon
به اسرائیل امکان می‌دهند تا یک ظرفیت پنهان، دوربرد و مقاوم برای جمع‌آوری اطلاعات، عملیات دریایی و ایجاد
بازدارندگی در برابر رقبای منطقه‌ای حفظ کند.
اگرچه اسرائیل و ترکیه در مقاطع مختلف روابط امنیتی و نظامی داشته‌اند، اما اختلافات ژئوپلیتیکی دو کشور در موضوعاتی مانند شرق مدیترانه، منابع انرژی دریایی، سوریه و نفوذ منطقه‌ای، باعث شده است که هر دو طرف به تقویت توان نظامی و دریایی خود ادامه دهند.
تحویل
INS Drakon
را می‌توان بخشی از راهبرد بلندمدت اسرائیل برای حفظ برتری کیفی در حوزه دریایی و تضمین آزادی عمل در یکی از حساس‌ترین مناطق ژئوپلیتیکی جهان دانست؛ منطقه‌ای که رقابت قدرت‌های منطقه‌ای در آن به‌طور فزاینده‌ای در حال افزایش است.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19870" target="_blank">📅 12:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19869">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزیر امور دیاسپورای اسرائیل، چیکلی:  اتحادیه مکه یک تحول بسیار خطرناک و نگران‌کننده است.  عربستان سعودی اساساً روی دیوار نشسته بود. آن‌ها قبلاً یک توافق دفاعی با پاکستان داشتند، اما به محض اینکه با ترکیه‌ای‌ها که در تقابل مستقیم با ما هستند و این تقابل می‌تواند…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19869" target="_blank">📅 12:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19868">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بقائی:
بازگشایی تنگه هرمز به لغو محاصره دریایی آمریکا مشروط شد</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19868" target="_blank">📅 11:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19867">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTOMipMdvLO7xXO0TtgTpssZXSUbTBgyIalI9ZWAazVSRnFdUSjCTckQb6fTu1c9NvkIHfTf18uV_nvWlQhptv-kQarTIOUB0GL-V7mS-zyg7RFUSKJdjnecgaON4BXFPLUd1NmOI85hj-5U07IJDwK_j_Nyg8wAr4O5wyd7uDeaCHmvxfJDJOg2RAdleqh-FqikQNjHYEZXbmyR7O9KuVhi9MRoZKKH8QD4TpWfuo-WHwZN2F6KMB2dnIs_-szduUdxUG5bqhxpbx4F9PYAVr3g_6B-zTKst-i3ydMX1DX2vUl2LG8ECpWx4-8g3ukeyJ9W-r6Pq4QZntjddpS72g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح پایینی است و لذا اصلاح های محتمل نزولی طلا خرید دارد.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19867" target="_blank">📅 11:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19866">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f33-ZzbwutiXwvwsfJ1CUgkYESn8B0GbR3C7sk0SoUW4Uh9c_-1lkkIdXut0AnbFrb1-eNENtIsZ1bNycajxP10nqGAALiIPUL7xitQ9no4ZMPbelFXxzM10-P5RW4hJv-tF6dxxKhfNGDvpKPdgAhuf9-prOxq_SqX1neC2A5ZcGApG7NjedhBw8jCoVOZX0waZtRXQ6WhnvQlfGoxFrNlQjURhhSaD10MXD1Zmg3-V39Uug-M6jbqTRJGoHZtR56kVABlSjR_AEYIIt1v13wBzimbncc3hFED0SJ6R2b4_exG96Z8tgXx4vH7o2nAXpOu89YMT64xcNuu_k3jmeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بشکه تاپاله
که گازشو لیلاز خورده
آبشو میثاقی
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/19866" target="_blank">📅 10:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19865">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سرنگونی یک پهپاد ناشناس در جنوب کشور توسط پدافند</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/19865" target="_blank">📅 03:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19864">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">احتمال پیوستن مصر به توافقنامه سه جانبه عربستان، ترکیه و پاکستان   «هاکان فیدان» وزیر خارجه ترکیه مدعی شد که مصر ممکن است به این توافقنامه مشترک به محض حل و فصل برخی مسائل فنی بپیوندد.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/19864" target="_blank">📅 02:09 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
