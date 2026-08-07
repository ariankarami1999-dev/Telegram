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
<img src="https://cdn4.telesco.pe/file/ICYkaumb8w3_U9X_1qVn2OL3pTmz1zkZx3yjQpajsGh2V2MwqnDbwr1eOvGQw3b-uEGXmtFekQCnfLIBfG48f0T1LVpI8Iz4PhUDDuQCKQlzUqiv33JODV_T4-Ur9TWhv_o4hm-jymhdUgKc1qcqrqUZYR4XsMLolhWrU-9PeB9ChQE6CIQ6ix1yHD0sl-Bllq1wNn2xP5jWQBduQyf0JyZD1jr255aqS9XVbxy4EkGAchxICSaigUM7CneSObeYoaqByeQvZ5DvN438nH3Q-bTKySqCA_pMa-hOohjINJjokuzEO2WCaeQwcWMp3FsadFhcinR4UhhmMGour3QZ4g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 446K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 23:14:41</div>
<hr>

<div class="tg-post" id="msg-20660">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6db8aff1a3.mp4?token=hGbZ5D2NQ4G4OYMGMh525o5LAPmhgVSO2u1ZnsSbnrQwLasXpRmLOFntumO2WnNVQzXndUii1_6wxm5iD4iKY1L2QrvbKoXByjRnFYvvsX_qmSTDUUkeVP4Zq8Ol2IB5T32F3_Xr5tG47bJz7DL_1a10MWbU04eab1DQStUcMOjqgu7AisOHjE1tDOKi3PgepMzCmXhnmQm9EHPOyr7QpjUw4YyfA4ct1YwLdNpLH9XBeVOaAbyy_mP3fvRxJCk5xmMhoEPyFw2RGZSXrfCCNAKNwsqm7aULMem1B4k_6rlnVc2ZJDq5c9SSSdYWRXq0FtG07W0mp-GCG2TZvaYVew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6db8aff1a3.mp4?token=hGbZ5D2NQ4G4OYMGMh525o5LAPmhgVSO2u1ZnsSbnrQwLasXpRmLOFntumO2WnNVQzXndUii1_6wxm5iD4iKY1L2QrvbKoXByjRnFYvvsX_qmSTDUUkeVP4Zq8Ol2IB5T32F3_Xr5tG47bJz7DL_1a10MWbU04eab1DQStUcMOjqgu7AisOHjE1tDOKi3PgepMzCmXhnmQm9EHPOyr7QpjUw4YyfA4ct1YwLdNpLH9XBeVOaAbyy_mP3fvRxJCk5xmMhoEPyFw2RGZSXrfCCNAKNwsqm7aULMem1B4k_6rlnVc2ZJDq5c9SSSdYWRXq0FtG07W0mp-GCG2TZvaYVew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به خبرنگاران و حاضران : اگر امکان داشته باشد، اگر بتوانید به سرعت از اینجا خارج شوید، من سپاسگزار خواهم بود، زیرا ما یک جنگ داریم که باید آن را به پایان برسانیم. این دلیل من برای خروج کمی زودتر است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/withyashar/20660" target="_blank">📅 22:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20659">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝓮𝓡𝓦𝓲𝓷🦅</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaeEhMo2nFHkzZ7HuVa0uShQT1KXZqDawQhP1kGAh9Ph69fdb-nJI5L5aq_neR_SBK6uWt8iAygf1NSTWO6wcbJwCUoyRv1QIqo-uxf20fh_o3FPAu2-Ns0_aG_7m6PKdTmOTefwxbDO7C_F52s97FQ8DjY3vuJuFem08g5isNKNvsVnQ7tb-1SRDCVm5AZ7eh3Kd8OGmape7wWVvzDBAPqT8DB700QF3tjvE-e67R6My43djZin1-Mb1qPTcnKWpE3W55MAxmVLb9wVUimLQE-PXdcem9euCDkS_oJqBioMRAgn_X9pR3Rp4CeFW9ybezKm-eo0LaSZG_et7_D5kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/withyashar/20659" target="_blank">📅 22:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20658">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nq57LsozvNL-RlHI__-KX76fFapqE65OSYZnxXiJqvg5Tt_mDaH9ruAjkmnoNEMIYwUtRdp12rfXyASPvNCmMQ5gxD59ic5kzQdRUUfqQR0GA4DI-bX4Qqg2bwT9x1TX8NPLR2UbRY5zm1pdpdI2HKTwHIx27cjnhQLrSmcZaSYdQxAeiBS3xAJi1eRu2a3i5BMQzwE3x77LebhkqVFomoGh5KSILDYNMsBcglRuOUmpNT_yg6P2up-njdU0cBiGPZHK8i-DC9h1o2_L4gkt1jShN9fWWHG9JJ9AsvjiLXvY11NbN04lI8U-eFEzggnrlHhpPg2coHN1837hEpkiyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ۳ سوخترسان از تل‌آویو بلند شدند و به سمت خلیج فارس می آیند. همچنین ۵ سوخترسان امریکایی و یک سوخترسان هم از کشورهای همسایه خلیج فارس در منطقه حضور قاطع دارد @WarRoom</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/20658" target="_blank">📅 22:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20657">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رسانه آمریکایی WIRED گزارش داده است که پنتاگون در آستانه امضای قراردادی چندصد میلیون‌دلاری با شرکت AeroVironment برای خرید حداکثر ۲۰ سامانه لیزری ضدپهپاد قرار دارد؛ رقم حدود ۴۰۰ میلیون دلار ولی هنوز رسماً تأیید نشده است. سلاح اصلی این برنامه E‑HEL(لیزر پرانرژی پایدار؛ سامانه‌ای برای سوزاندن و ازکارانداختن پهپادها با پرتو لیزر) است که برای انهدام پهپادهای کوچک، پهپادهای انتحاری و اهداف پرنده گروه‌های ۱ تا ۳ (رده‌بندی ارتش آمریکا بر اساس اندازه، وزن و برد پهپادها) طراحی شده است. نسخه پیشنهادی آن بر پایه سامانه LOCUST(سلاح لیزری متحرک برای مقابله با پهپادها) توسعه می‌یابد و روی خودروهای ISV(خودروی سبک تاکتیکی برای جابه‌جایی نیروهای پیاده) و JLTV (خودروی زرهی سبک چندمنظوره برای عملیات نظامی) نصب خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/20657" target="_blank">📅 22:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20656">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رویترز: ایالات متحده به فروش ۵۲۵۰ موشک دفاعی به بحرین، کویت، قطر و امارات متحده عربی موافقت داد.
این اقدام با هدف جبران کاهش ذخایر موشکی سیستم پاتریوت این کشورها انجام می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/20656" target="_blank">📅 21:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20655">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا: تحریم‌هایی علیه پلتفرم‌های خرید و فروش رمزارزها که از سپاه پاسداران پشتیبانی مالی می‌کنند، اعمال شد.
@WarRoom</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/20655" target="_blank">📅 21:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20654">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اتاق جنگ با یاشار : صدای گشت زنی جنگنده های جمهوری اسلامی در آسمان بندرعباس هم زمان با افزایش حضور سوخترسان ها و متقابلأ جنگنده های رادارگریز آمریکایی
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/20654" target="_blank">📅 21:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20653">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">شبکه CBS :  مجلس سنای آمریکا به طرح قانونی درباره تحریم‌های روسیه و ایران رای مثبت داد.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/20653" target="_blank">📅 21:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20652">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">راستی امشب به روال هر جمعه بیداریم و کشیک رو میدیم
😁</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/20652" target="_blank">📅 21:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20651">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/20651" target="_blank">📅 20:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20650">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromamir</strong></div>
<div class="tg-text">امشب بیدار بمون</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/20650" target="_blank">📅 20:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20649">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromamir</strong></div>
<div class="tg-text">داداش دعا نویسم گفت امشب جنگ خواهد شد</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/20649" target="_blank">📅 20:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20648">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbY0ECV0-PuvXFsfKxwe6VbYntU78-rrUlm9IY04XeSi0M8IePLjVdwH3KetXbSoRM5JWu4dcW6Gg87BP8HYFSXDHbfyMsRgTtQaShPpmIrFbFbKVcee_bAhibYMMa6La5N0sw7b-AAOj0VJ4pfambIsuPSHDOtEZp84dIeF1zRutsSOpwB4dO_VwljdXBx01xA6NVxYUGu22vvNW7bMMi73WcnqDhBkhubS73Dzf-8GpqXuavavHezClMdzSVZIjPELcava0YA6PDqCbTBX5bWnJvfrHa850-uFbqM2zO-uNh_-FnPtPWmK65mR3PHoDDbkjTJF7PKg0J8EavNJAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ۳ سوخترسان از تل‌آویو بلند شدند و به سمت خلیج فارس می آیند. همچنین ۵ سوخترسان امریکایی و یک سوخترسان هم از کشورهای همسایه خلیج فارس در منطقه حضور قاطع دارد
@WarRoom</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/20648" target="_blank">📅 20:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20647">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C93oQX6ZpW9Kt7XqQGTsUNGJ6yVQIdHcR6NgddLM0t9IojY5yfKEobTIAPS7ft7LdGJS7UO7q_dQHOtxbA2GkxHOlzJoHAGElKDgT4AkLiFT14OIZx7T3d1MAOChiMaSC29jQaSMN7SBshd4CMLoYHTx4WqU5E9TawEnfGikCsn1cc9nuC2kLi26iOLyWJRqJ0uDZpidoy5IqyO0LJ4mxbruwDea-DVh4XtIhL4tGuOYUB5rW0QnlyxGrQ1Tj9rsH94wCiNP8h2Z1LfLKlT0Nfb6f1navS-VuZeziH3SO82bdfigcQ7WqBx0FEmvG5pWZ7AEdbay8Y4KKOrXvDQ9pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : خدمه پروازی یک فروند هواپیمای سوخت‌رسان KC-135 نیروی هوایی ایالات متحده، در حال سوخت‌گیری یک فروند جنگنده رادارگریز F-35A در آسمان خاورمیانه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/20647" target="_blank">📅 20:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20646">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خزانه‌داری آمریکا: تنگه هرمز دیگر هرگز به وضع سابق خود باز نخواهد گشت
تنگه هرمز دیگر هرگز به وضع سابق خود باز نخواهد گشت، زیرا ایرانی‌ها از آن به عنوان یک گلوگاه استفاده کرده‌اند، یا تلاش کرده‌اند از آن به همین منظور استفاده کنند.آنچه در دو سال آینده شاهد خواهیم بود، این است که تنگه هرمز از اهمیت خود کم خواهد شد.این تنگه به یک آبراه معمولی تبدیل خواهد شد، و من معتقدم که بیش از ۵۰ یا ۷۰ درصد از انرژی که در حال حاضر از طریق این تنگه منتقل می‌شود، از طریق خطوط لوله زیرزمینی منتقل خواهد شد
‏در بیانیۀ وزارت خارجه آمریکا آمده: اقدامات ما شبکه‌ای از شرکت‌های مبادله مالی و شرکت‌های صوری که به ایران برای نقل و انتقال میلیون‌ها دلار پول کمک کرده‌اند را هدف قرار می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/20646" target="_blank">📅 20:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20645">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وزارت دفاع آمریکا پنجمین مجموعه از پرونده‌های مربوط به پدیده‌های ناشناس هوایی و بشقاب پرنده ها رو منتشر کرد در همین راستا شبکه خبری CBS دقایقی‌پیش مصاحبه انجام داده با «آوی لوئب» که ترامپ او را مأمور و نماینده تحقیق بر روی این پروژه کرده، از دست ندید.با زیرنویس فارسی
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/20645" target="_blank">📅 19:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20644">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سناتور جمهوری‌خواه تد کروز، درباره جمهوری اسلامی : اگر شما یک اسلام‌گرا هستید که از آمریکا متنفر است و سعی دارد ما را بکشد، من از اینکه شما یک کشور یا ملت را رهبری کنید و منابع لازم برای کشتن آمریکایی‌ها را داشته باشید حمایت نمی‌کنم؛ این جایی است که ما باید بر آن تمرکز کنیم؛ حال، چگونه فروپاشی حکومت را رقم بزنیم
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/20644" target="_blank">📅 18:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20643">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f88f7a5ccb.mp4?token=uz1gRiTWTe8W49p2V9Pop51y4zMJLwXIgQ2_227ckRyoq-Mgme2Ru0XPS7kPpRnkfFF7_vie6D2KxQyzYlI21V3DM2JTNMGmkvevAFXYePYd7jtoePFbwkB_7y_s9K86GXaVm6Mr_kB8WZBQ--__H2Xv3dFzdff1hYvZwXSLSu45sC5xN1MHFpTLpEczF-oSpijnvPbSjHLfIk8K7S9oMMwpSAixkFPMlTj9e0QzMJyQzZoL7fYqeStOinTW7DXQ3wiSd0jFQ4HLILjZfLybgBXu2AtCa7hO6vYap3zEOkgZDxJ0j58bgIS0XyvUj8WCx9tTl3CvQYY4Kz8hhr4MUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f88f7a5ccb.mp4?token=uz1gRiTWTe8W49p2V9Pop51y4zMJLwXIgQ2_227ckRyoq-Mgme2Ru0XPS7kPpRnkfFF7_vie6D2KxQyzYlI21V3DM2JTNMGmkvevAFXYePYd7jtoePFbwkB_7y_s9K86GXaVm6Mr_kB8WZBQ--__H2Xv3dFzdff1hYvZwXSLSu45sC5xN1MHFpTLpEczF-oSpijnvPbSjHLfIk8K7S9oMMwpSAixkFPMlTj9e0QzMJyQzZoL7fYqeStOinTW7DXQ3wiSd0jFQ4HLILjZfLybgBXu2AtCa7hO6vYap3zEOkgZDxJ0j58bgIS0XyvUj8WCx9tTl3CvQYY4Kz8hhr4MUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد شهباز شریف، نخست وزیر، محمد بن سلمان بن عبدالعزیز آل سعود، ولیعهد و نخست وزیر عربستان سعودی و رجب طیب اردوغان، رئیس جمهور ترکیه نماز جمعه را در قصر الصفا اقامه کردند. در این مراسم، محمد اسحاق دار، معاون نخست وزیر و وزیر امور خارجه، سناتور محمد اسحاق دار، فرمانده ارتش و رئیس نیروهای دفاعی، سپهبد سید عاصم منیر، و مقامات ارشد سعودی و ترکیه نیز حضور داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/20643" target="_blank">📅 18:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20642">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rp1K2WJaJc2K6QhSbrNNL6gNLmn9mJM0-AODeIciwjQxsjawfQqooRBoLR3j2Kc0QIb_JVyX8mpBa6Okb5jd3urfT_sUlKxmmwQi6rAP_XzsjU5xl507TrGdw68F1UidRpSMg4X01iM7W1Po7ER26UlqUMsHoJoQO017eFYbmxOGOTZV2BlrovslMAldimKcHIm-6oMR4I70yHU2puSV16HJBUrSge98aJT3jBan8RVn6kXRLS6wGuzXiTK2s50vi8jhOJxt84VAoh3UGqBisGgisIV_lp1oQ_rB3vJTL-ZKutgIcEljL8XCvee-TayfuV6zZToeGrkONpQ995znoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راستی امشب به روال هر جمعه بیداریم و کشیک رو میدیم
😁</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/20642" target="_blank">📅 18:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20641">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شبکه کان اسرائیل: ایران صدها موشک پدافندی دوش‌پرتاب از روسیه و چین دریافت کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20641" target="_blank">📅 17:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20640">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20640" target="_blank">📅 17:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20639">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRVFLQt_CfoOizKhzyx9128GLUV0NWnodM_xYdFL0KRVtmJfHsVs9hJDZbgV21kcuQYFz2E5F0Glh4l50TVDge_sE2-369P7blQwLa0ZV2XrrmaON1WCXMe0gbI2Pk78c7DHbgIc4uIbRbveLzBnogJ-sPFAXbViQwooEtuI5aeVlABBM4zLdc0E_CAzOZU81bOa9hWDcN_YA5icjh9X6wNTMVxfMJ-8tmH8pXVvEgBzIeUW-ygQjgtYoA0iMPod-otS6VN3ta5veZkkH_R8HAJRfP1PSocv-wRd4va8onCjCRY6Spp4SvXfT3fqIij7lsKUbQVKBY859WrYwXrDKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیت هگست وزیر جنگ متنی از مقاله که ترامپ هم دیروز آن را منتشر کرده بود منتشر کرد. این مقاله فقط دیدگاه نویسنده آن را بیان میکند نه یک گزارش خبری.  متن عکس : ترامپ در جنگ ایران پیروز شد پس این هم واقعیت؛ همان حقیقت تلخی که تردیدکنندگان دوست ندارند درباره‌اش…</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20639" target="_blank">📅 17:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20638">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏نیویورک تایمز: برنامه هسته‌ای رژیم کند شده اما متوقف نشده است
‏ بازرسان سازمان ملل برآورد می‌کنند رژیم همچنان ذخیره‌ای از اورانیوم نزدیک به درجه تسلیحاتی در اختیار دارد که برای ساخت سریع ۹ تا ۱۰ بمب هسته‌ای کافی است. داریل کیمبال، مدیر انجمن کنترل تسلیحات، گفت سیاست فشار حداکثری و اقدامات نظامی دولت پرزیدنت ترامپ نتوانسته توانمندی هسته‌ای رژیم را از میان ببرد. الی گرانمایه نیز هشدار داد در نبود نظارت بین‌المللی، رژیم می‌تواند ذخایر فعلی اورانیوم خود را به سرعت تا سطح مورد نیاز برای ساخت سلاح هسته‌ای غنی‌سازی کند.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20638" target="_blank">📅 17:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20637">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اینستاگرام رو  هر روز میززند و باز‌میکنم دیگه اعلام نمیکنم حتی ! الان برگشته
🤣
https://instagram.com/yashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20637" target="_blank">📅 17:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20636">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqOimgFFW4nMz8tJbDOn_fqrX4n6vaUcKs9RPSbfdsPM5PIa7hLMiY-aZ06TKfgs6xmDojXrHTz8hsC9FgORfK9sv2w4EOM67vGhswgWwTppFum6YqanhEvzpVXn7JTaIS-hhH1Hkg3Nepsz1ehsxhbaMM-ubvv-xQtE8U39_arOT7_fhuTxOEcGmRIoA-Q4DkC6rRfhTv3qxKzh9McZDYurCSYJgI5rNVQ0peges2g5Vj8nCqRTGDSMeMywWd6DFhwB-u7-RcKMpw8rPaAk_zrArNjIvlszF7rtYoZ6SgMVsw6SUvnnhBvLDOGeQkIxh0l4Cb9VJOkpLeo_R1dCpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیت هگست وزیر جنگ متنی از مقاله که ترامپ هم دیروز آن را منتشر کرده بود منتشر کرد. این مقاله فقط دیدگاه نویسنده آن را بیان میکند نه یک گزارش خبری.
متن عکس : ترامپ در جنگ ایران پیروز شد
پس این هم واقعیت؛ همان حقیقت تلخی که تردیدکنندگان دوست ندارند درباره‌اش صحبت کنند.اگر ترامپ در این جنگ در حال شکست بود، هیچ‌یک از این ابتکارها و تحولات در حال وقوع نبود. آنچه امروز شاهدش هستیم، افزایش نفوذ آمریکا، گسترش مشارکت‌های منطقه‌ای و شتاب گرفتن روندی است که ترامپ برای برقراری صلح و ثبات بلندمدت در خاورمیانه در نظر دارد. این‌ها نشانه‌های شکست نیست، بلکه نشانه‌های دگرگونی منطقه در مقیاسی بی‌سابقه هستند.
رسانه‌ها و تحلیلگران می‌توانند هر روایتی که می‌خواهند ارائه دهند، اما تاریخ‌نگاران خواهند نوشت که ترامپ تأثیرگذارترین عامل در بازآرایی خاورمیانه در دوران معاصر بوده است
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20636" target="_blank">📅 17:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20635">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">به گزارش فایننشال تایمز، به دلیل محاصره دریایی آمریکا، حداقل یک هفته است که هیچ نفتکشی در جزیره خارک، پایانه اصلی صادرات نفت ایران، بارگیری نکرده است.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20635" target="_blank">📅 16:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20634">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شبکه الجزیره گزارش داد نشست لبنان و اسرائیل با میانجی‌گری آمریکا در رم بدون هیچ پیشرفت ملموسی پایان یافت. اسرائیل با پیشنهاد عقب‌نشینی مرحله‌ای از جنوب لبنان مخالفت کرد و تأکید کرد تا زمانی که سازوکار قابل‌اعتمادی برای خلع سلاح و راستی‌آزمایی حزب‌الله ایجاد نشود، با خروج بیشتر نیروهایش موافقت نخواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20634" target="_blank">📅 14:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20633">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">«توافقنامه دفاعی مکه» رسما امضا شد : هر گونه حملهٔ مسلحانه به هر یک از کشورها، حمله به هر سه کشور محسوب می‌شود.
محمد بن سلمان، شهباز شریف و اردوغان توافقنامه دفاعی مشترک میان ترکیه، پاکستان و عربستان را امضا کردند.هدف این توافقنامه، تقویت بازدارندگی جمعی در برابر هر گونه اقدام تجاوزکارانه است
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20633" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20632">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0293ab00f0.mp4?token=hdqMgADVq0IK6BMh8-ECHAbMPyKRNPNW_FRz2r7giSiL8MuA7RwbUljJz4dIrmQadNMdBcptTxWYXx6ABg-q3ZXwCKfkqKZr1zww3oDMGhb9Wi2iCsLj8pY60BU1IwQDTr90D1PHfazvDS-xvm2dDRCjD-c180UkuQmvf4XrrvppiaDYM0xar4LrpAOulVzM77ZIsJ-H4mPMYhyfeqAqGgYz0ovUaO-gpq3OytZEwntodKCmo_R2HJPb7o2zP53RIHA5cSsS4_1yfu3L_4XCdgrY8p_pipPLjNJ5DBMMzwIfTEE0vu_cN8XzDnauMXaPLzP_2dAzK2qmLW0_EySbqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0293ab00f0.mp4?token=hdqMgADVq0IK6BMh8-ECHAbMPyKRNPNW_FRz2r7giSiL8MuA7RwbUljJz4dIrmQadNMdBcptTxWYXx6ABg-q3ZXwCKfkqKZr1zww3oDMGhb9Wi2iCsLj8pY60BU1IwQDTr90D1PHfazvDS-xvm2dDRCjD-c180UkuQmvf4XrrvppiaDYM0xar4LrpAOulVzM77ZIsJ-H4mPMYhyfeqAqGgYz0ovUaO-gpq3OytZEwntodKCmo_R2HJPb7o2zP53RIHA5cSsS4_1yfu3L_4XCdgrY8p_pipPLjNJ5DBMMzwIfTEE0vu_cN8XzDnauMXaPLzP_2dAzK2qmLW0_EySbqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
: فقط همین را می‌گویم؛ اگر اوضاع به همان سمت برود، آن‌ها این کشور را نابود خواهند کرد.
مجری
:شما دیروز، وقتی درباره نوادا صحبت می‌کردید، گفتید اگر اشتباه نکنم، ممکن است قیمت بنزین دوباره کمی بالا برود، و بعد گفتی…
ترامپ:
نه، نه. این فقط در صورتی است که مجبور شوم یک حمله دیگر انجام بدهم.
مجری:
یعنی…
ترامپ:
قیمت‌ها فقط در صورتی پایین می‌آید که به توافق برسیم. آن‌ها می‌خواهند توافق کنند
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20632" target="_blank">📅 13:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20631">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20631" target="_blank">📅 12:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20630">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پرات ریخت ؟
😈
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20630" target="_blank">📅 12:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20629">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20629" target="_blank">📅 12:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20628">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مجری : مردم میپرسند کی‌اینا میرن؟  نوستراداموس هم نتونست بگه! مانوک : انقلاب تقویم نداره … I LOVE YOU @WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20628" target="_blank">📅 12:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20627">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رویترز: نگرانی درباره تنگه هرمز قیمت نفت را افزایش داد
قیمت نفت امروز در پی افزایش نگرانی‌ها درباره شرایط بازگشایی تنگه هرمز بالا رفت؛ زیرا ایران با همکاری عمان پیشنهادهایی برای محدود کردن عبور برخی کشتی‌ها و جریمه ناقضان قوانین مطرح کرده است.
قیمت
نفت برنت
با افزایش
۸۵ سنت (۱.۰۳ درصد)
به
۸۳.۳۴ دلار در هر بشکه
رسید
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20627" target="_blank">📅 11:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20626">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0e767e0b.mp4?token=LAsSA0Oz2hcz0AfqQg99ANKH7xEfss9kTUHrEPIjrNs4pU7P3jn9xfbwwZPTmlLsxpAM-9WB2d_1ykcXaWaWr_AfbciVowcz9kn7whNoHcR_FhjRzS1HcIHhyhowGOL9sX70iVxGtofUWPZUNILVofrkkKIaJ040n-wAyME1-AaPBQUxMdrltiugtLkfgke5DuxRoR42nmrn-tRhSShqPrATpNV46fTAF-_8XrNQ9kC0XOiUce9Tj2FOLXVIZkAsjE8YrydTUse1Yub-dC-ygCPhYH_IhOfYZ9I_wm1SL-lKeKcQQFHJlj1klPBubDYUmG0i7tDHrLgkSnxi-Rm7FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0e767e0b.mp4?token=LAsSA0Oz2hcz0AfqQg99ANKH7xEfss9kTUHrEPIjrNs4pU7P3jn9xfbwwZPTmlLsxpAM-9WB2d_1ykcXaWaWr_AfbciVowcz9kn7whNoHcR_FhjRzS1HcIHhyhowGOL9sX70iVxGtofUWPZUNILVofrkkKIaJ040n-wAyME1-AaPBQUxMdrltiugtLkfgke5DuxRoR42nmrn-tRhSShqPrATpNV46fTAF-_8XrNQ9kC0XOiUce9Tj2FOLXVIZkAsjE8YrydTUse1Yub-dC-ygCPhYH_IhOfYZ9I_wm1SL-lKeKcQQFHJlj1klPBubDYUmG0i7tDHrLgkSnxi-Rm7FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : مردم میپرسند کی‌اینا میرن؟
نوستراداموس هم نتونست بگه!
مانوک : انقلاب تقویم نداره … I LOVE YOU
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20626" target="_blank">📅 11:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20625">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سی‌ان‌بی‌سی : به نظر می‌رسد توافق ترامپ در وضعیت وخیمی قرار دارد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20625" target="_blank">📅 11:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20624">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏خبرگزاری آناتولی به نقل از منابع امنیتی گزارش داد رجب طیب اردوغان، رییس‌جمهوری ترکیه، برای سفری یک‌روزه راهی عربستان سعودی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20624" target="_blank">📅 10:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20623">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8554GFHlVJfQOqK6vwgGvJnQD6uS3nsQ8ibUzQjHuisFqLTEnlH9W2ur69XWt-WVza20WDR3xTxz24rjpR2zIXnYQiQClmlTmjH2JUEZblzRrCvvxXpYkNop-lyscJeBIxPsZdjQQ3jeasioFDRBk3VQV8QjIMucIzhdZUuA-jIv04CrVcgc8jw5EKpEbfmJx6lEU2Kgt1MTO-x36n_-JN-iQoWuKOXu--pitWpOKhibiApOTrX-KcDTq8hHb4WcRI3V9SU6FjqgUoyNbI6mnyBnVf9xDNiCvxSznfDOZaJ7tqEFPxfn_CZBWtILFUBHFiHC5ugQALUzF51mbM5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏لکه های در تصویر منابع نفت و گاز در دریای کاسپین , طبق تقسیم‌بندی جدید بیشتر این منابع به کشورهای دیگه واگذار میشه
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20623" target="_blank">📅 10:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20622">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پس از آنکه وزارت حمل‌ونقل اسرائیل پارک کردن تعداد بیشتری از هواپیماهای سوخت‌رسان آمریکا در فرودگاه بن‌گوریون را ممنوع کرد، به آمریکا اعلام شد که هواپیماها باید در پایگاه‌های نظامی نیروی هوایی اسرائیل مستقر شوند، نه در فرودگاه غیرنظامی بن‌گوریون.شبکه i24News…</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20622" target="_blank">📅 09:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20621">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">instagram.com/Yashar – Ruhollah zam and Msoud Molavi @WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20621" target="_blank">📅 09:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20620">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d2de94a7.mp4?token=YmY3Ujx9A3lP0ULSwAWBGotaYQteniceyley0kjb0GquoGSVj_OsMwrUfjucWpynabZ7WkQaH3ZFdvwLBRtggVTOkYfhmDCmjFTv7rsFZse1-HGTWWt-xQGT8RUAqkJ3ZLgU_FZ0ZExLkbQ23tKJx0OicCK4Q_aJn6tei_hNN0MMi5sGpVW36KNyfi9nMoUaH0-BRRgeWv86pMl-_gBP6-0tEblr9f-7yqDukxGcgWe5v0nBMO9g6LEIeR1NTgHMS9SDVPa1_NvYllebbB5rhkdDPWJdt_vaNeFwL8PlzFYLYVLzwfTjXdmsHmlwN7cY9Zwt6uD8llw7SY-zQpSOV4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d2de94a7.mp4?token=YmY3Ujx9A3lP0ULSwAWBGotaYQteniceyley0kjb0GquoGSVj_OsMwrUfjucWpynabZ7WkQaH3ZFdvwLBRtggVTOkYfhmDCmjFTv7rsFZse1-HGTWWt-xQGT8RUAqkJ3ZLgU_FZ0ZExLkbQ23tKJx0OicCK4Q_aJn6tei_hNN0MMi5sGpVW36KNyfi9nMoUaH0-BRRgeWv86pMl-_gBP6-0tEblr9f-7yqDukxGcgWe5v0nBMO9g6LEIeR1NTgHMS9SDVPa1_NvYllebbB5rhkdDPWJdt_vaNeFwL8PlzFYLYVLzwfTjXdmsHmlwN7cY9Zwt6uD8llw7SY-zQpSOV4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز سی‌وچهارمین سالگرد درگذشت دکتر فریدون فرخزاد
۱۵ مهر ۱۳۱۵ متولد شد و در ۱۶ مرداد ۱۳۷۱ آسمانی…
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20620" target="_blank">📅 09:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20619">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مارک لوین : رژیم ایران باید نابود شود وگرنه این [وضعیت] هرگز متوقف نخواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20619" target="_blank">📅 01:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20618">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">العربیه : یک مقام ارشد سعودی می‌گوید چندین گزارش اطلاعاتی معتبر نشان می‌دهد که میان حوثی‌ها، شبه‌نظامیان عراقی و سپاه پاسداران انقلاب اسلامی ایران (IRGC) برای آماده‌سازی حملاتی علیه عربستان سعودی ائتلاف هماهنگ وجود دارد.
این مقام این گزارش‌ها را «تکان‌دهنده» توصیف کرد، زیرا در حالی منتشر شده‌اند که ریاض در تلاش برای کاهش تنش‌ها است و اعلام کرده بود مذاکرات به‌صورت مثبت در حال پیشرفت است.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20618" target="_blank">📅 00:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20617">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a684ce95a7.mp4?token=F0jmfkiDVm1q4HbJjmXKhdv1V8h6bdoo6mckSKnMm0KxM4vtS29WvEEsCRikKftGT-nNI9TIyL2O3L7OyPl4K2pt3v71W3RcClxsLG3VN03XMNWlVBDy6_XPyBS6vKIMXeEiiqEz7sVrh6DNJnr7KP_Am0wXP5_I8J5ibW1Wwz4kgc-9KjYXpWX5LnKJ7fwvXNloE8anM7Cqac6jOn8A5fqMEozeTMUlTLePPxMTL2OjT9kx-MnoxyoMRrvHKNST6ZaIzQwGqfUMx13d0RjfuPo7hOsmhkhmtQAlHQsb7kspDaULIEheMw6aUh_j5ujhL2257UggyPBTeEBmx7zOOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a684ce95a7.mp4?token=F0jmfkiDVm1q4HbJjmXKhdv1V8h6bdoo6mckSKnMm0KxM4vtS29WvEEsCRikKftGT-nNI9TIyL2O3L7OyPl4K2pt3v71W3RcClxsLG3VN03XMNWlVBDy6_XPyBS6vKIMXeEiiqEz7sVrh6DNJnr7KP_Am0wXP5_I8J5ibW1Wwz4kgc-9KjYXpWX5LnKJ7fwvXNloE8anM7Cqac6jOn8A5fqMEozeTMUlTLePPxMTL2OjT9kx-MnoxyoMRrvHKNST6ZaIzQwGqfUMx13d0RjfuPo7hOsmhkhmtQAlHQsb7kspDaULIEheMw6aUh_j5ujhL2257UggyPBTeEBmx7zOOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما در سراسر جهان مهمات داریم.
اگر زمانی به آنها نیاز پیدا کنیم، آنها را خواهیم گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20617" target="_blank">📅 00:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20616">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0117ccebfa.mp4?token=ERTw9z_2aHYaT587ljVk4xO3bFTEN0dwa5-PeqVHMy4O1nzy--hETwulhZytL4pgBMur-A0fLDhRbu_zplTaxdE2ghvWge95WBvidOCpHeI9Ad2qHr46Iz66DLyyrqwilOOXzgRrgN_0pOh5_bV5fQA0PQk4GcGkPmZuXfJ9jQ1Y6cAaXFJye0e1mY06K0ELqptjwprYw5ojVOKuj_KqVdtHniaxpDl-UN54mBjUVwdQZ3OAwPj6r1SSNLPBym8n9qnkRRIV_4Dlj9XmxYbhrVy8jRUdBwM5IxQ01LTpR0L-ISIwlLlzmgOo7FOrjK5PyHJeaWw9RZkX67BwFDAyHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0117ccebfa.mp4?token=ERTw9z_2aHYaT587ljVk4xO3bFTEN0dwa5-PeqVHMy4O1nzy--hETwulhZytL4pgBMur-A0fLDhRbu_zplTaxdE2ghvWge95WBvidOCpHeI9Ad2qHr46Iz66DLyyrqwilOOXzgRrgN_0pOh5_bV5fQA0PQk4GcGkPmZuXfJ9jQ1Y6cAaXFJye0e1mY06K0ELqptjwprYw5ojVOKuj_KqVdtHniaxpDl-UN54mBjUVwdQZ3OAwPj6r1SSNLPBym8n9qnkRRIV_4Dlj9XmxYbhrVy8jRUdBwM5IxQ01LTpR0L-ISIwlLlzmgOo7FOrjK5PyHJeaWw9RZkX67BwFDAyHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: گزارشی وجود دارد که می‌گوید شما به اهداکنندگان گفته‌اید که باید کاری کنند جی‌دی ونس انتخاب شود. آیا این حمایت رسمی شماست؟
ترامپ: نه. من فکر می‌کنم او عالی است، اما خیلی زود است.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20616" target="_blank">📅 00:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20615">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1081b3145.mp4?token=PjjrNjPR7x2gYA5l_T6z9eR7gTDu7M-j6ttZgE8HKOVMtN60n9djV-zjwFQ9KzBXr3aoyek9eK7kI6E6FOBPy62vTHw35gvyzqzBCz6t5bx-YNpTlCbrvmrZ1g_vnK-vewsSN-olueiGOPKzFc2bEs20f6NJKXwlCadj_eVFhlXNNb1buUtB_Q0q3cYFwkmTVk8OMWZZeOiZKSjMXu2o5cMHIubm_GVDwTdY1JjkY6hMky5nv2HdKurTX8FevrNsYZKIhR98NbBKYi79FIux8Jh54vdE27TMpuQE1oMCluRuWQVr4QOoifMc8FWcyR6zYRXvvtI6YJMwcLuoWgzPkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1081b3145.mp4?token=PjjrNjPR7x2gYA5l_T6z9eR7gTDu7M-j6ttZgE8HKOVMtN60n9djV-zjwFQ9KzBXr3aoyek9eK7kI6E6FOBPy62vTHw35gvyzqzBCz6t5bx-YNpTlCbrvmrZ1g_vnK-vewsSN-olueiGOPKzFc2bEs20f6NJKXwlCadj_eVFhlXNNb1buUtB_Q0q3cYFwkmTVk8OMWZZeOiZKSjMXu2o5cMHIubm_GVDwTdY1JjkY6hMky5nv2HdKurTX8FevrNsYZKIhR98NbBKYi79FIux8Jh54vdE27TMpuQE1oMCluRuWQVr4QOoifMc8FWcyR6zYRXvvtI6YJMwcLuoWgzPkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: فکر می‌کنم این جنگ خیلی زود به پایان خواهد رسید. به نظرم آنها دیگر نمی‌توانند مدت زیادی به این وضعیت ادامه دهند.
خبرنگار: آیا برای بازگشایی تنگه هرمز توافقی حاصل شده است؟
ترامپ: نمی‌خواهم بگویم که توافق انجام شده، اما در حال حاضر تا حدی باز است. ما کنترل تنگه را در اختیار داریم.
من در مذاکرات با ایران دخیل هستم. اوضاع به‌خوبی پیش می‌رود.
ممکن است به‌زودی توافقی حاصل شود.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20615" target="_blank">📅 00:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20614">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">محسن رضایی (محسن کج بند) دبیر شورای عالی امنیت ملی(جایگزین علی شمخانی) شد، اون سرش رفت اینم تهش میره @WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20614" target="_blank">📅 23:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20613">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تنگه دعوا شده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20613" target="_blank">📅 23:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20612">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آمریکا : اگر
هیچ‌یک از والدین شهروند یا گرین‌کارت‌دار نباشند
، دولت قصد دارد در برخی موارد دیگر به کودک متولدشده در آمریکا تابعیت خودکار ندهد. این سیاست به‌ویژه افرادی را هدف قرار می‌دهد که برای
«گردشگری زایمان» (Birth Tourism)
یا با اقامت موقت وارد آمریکا می‌شوند تا فرزندشان پاسپورت آمریکایی بگیرد
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20612" target="_blank">📅 23:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20611">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تنگه دعوا شده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20611" target="_blank">📅 23:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20610">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwolXaMNHmRlT8i8RDglx3R7KZWH6wq792Lin3p3FQYGWjGxp8lYo5w3xkzdmoiATPNOfgZPe9QgzNCJMDgl-hshBczwkpeCS8tsvcFjNtoR5s1WY2NQSvwukd0xBiFxdacrha37nc_YuwI5dImM9tgwm-6ynjns-dxXP-O5ltzz_yfW2Ov1EDqi1rvZv87LquXdAGK00nOoyUbR2z7eyKwH_J-wabG7XaD2-wYbk6e1nWVeRccOp8pAy58wxKog3oesnFvCVltreSEb-1f7ji5aKIirgibgx4NkJ3dMDCjP9c74rck38Wi8zbuU-TxvRj5g5FyHbrlmcTWb9n_L8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای هشدار زودهنگام E3B-Sentry با رادار AWACS هم اکنون در آسمان انجام مأموریت میکند. دوستان بسیاری اسکرین‌شات گرفته بودند که این هواپیما رفته، لازم به ذکر است چندین نسخه از این هواپیما در پایگاههای آمریکا در منطقه حضور دارند. ولی این هواپیمای به خصوص همچنان به مأموریت خود ادامه میدهد.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20610" target="_blank">📅 23:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20609">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏افشای تکان‌دهنده ژنرال جک کین :
‏"پاکستان و قطر بر سر منافع مشترکشان با جمهوری اسلامی، دولت ترامپ را درباره اهداف واقعی تهران فریب داده اند"
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20609" target="_blank">📅 23:39 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20608">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ایالات متحده، اقدام حوثی‌ها را که آن را "حمله ترسوانه" به نیروهای وفادار به عربستان سعودی توصیف کرده است، محکوم کرد و به خانواده‌های قربانیان تسلیت گفت. @WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20608" target="_blank">📅 23:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20607">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCVv3JeSxQ3as4qNmluLdrvhbF9qNguDyEg_aUzlV0CU2dB7Ir8R0F4dGQaNWAYFmewE09Slv9wdX0dUwnVVdVRJyMv_uacARrNRlrtffLB_XtiWUC1qyvTKZnYdW8bKFpYMreSiaH33EO3xtwkpuCzM8S0W7gMng2Wyz_3LnfKmtqUxdIRLwGR-XqJ7t6hZK0A4YrlH3eBWMomihBBansWYLFC3BLVmWlT-NC-sjuKvEf0RP_DjSCEyqwtF1jjBW955lIK-eyLTbScxDtwPcq3JPb52QVl6HEPqDM-CT-2e7yKVSTe1vT-NaEo0IESTVEVdmyqbs2zTv16dwsgM4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان ۴ دهه واردات نفت از عربستان؛ آمریکا به سراغ ونزوئلا رفت
برای نخستین‌بار از سال ۱۹۸۵، واردات نفت خام آمریکا از عربستان سعودی در ماه جولای به صفر رسید؛ تغییری بزرگ در نقشه انرژی جهان که پیامد مستقیم تنش‌های نظامی در خلیج‌فارس است.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20607" target="_blank">📅 23:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20606">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iev2o0wMjZQ-V4M0kyQ7J2N8029y8jvUD_kywhyxwDYZWMORgut0qYy8m5TTRgccxz-2WTAKDDZ2A5kHfFnCmIMPMLYrUgEVD0WG8u7RW1WEwnC_zJPFXssGuwXdNN1qaUVPTtvsJJvtsXNrXoQTbgiW8AcDKvNLFLKG2WZHFLUnmnxH8sncgoNHeQB5D8i_mIkPWHuUGq9-g9isxksxfJx6Jpo75uTgTyJ2mlW6ayEGU__HsfCKjs39l4oJwxp5d0Ay7RgR39hV8xOiRmAgRxdPvz4vxsfXBb793JHXD5tw8N1qKoq384I14eeZ9eBmTWZ_X4xc1Ga29m95JQejQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در لحظه گزارش شلیک موشک، حداقل دو نفتکش در حال عبور از تنگه هرمز از طریق کریدور تحت حمایت ایالات متحده بودند.
NISSOS KEA و NISSOS KEROS، هر دو قبل از نزدیک شدن به تنگه، سیستم شناسایی خودکار خود را خاموش کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20606" target="_blank">📅 23:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20605">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تسنیم
: منشأ صدای انفجار در قشم، هدف قرار دادن اهداف متخاصم بود
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20605" target="_blank">📅 23:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20604">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تایید نشده انگار از ارومیه موشک پرتاب شد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20604" target="_blank">📅 22:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20603">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">جنگ میشه ؟!</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20603" target="_blank">📅 22:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20602">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzRhzwsPvbHVwtdk9GD7XXdo8doiMurplnv5TUp6h7Nifo3i7CRPrDjM1hI111iueI3W8h8IBJqiYgESPRlBXPRwe0BxVpOdVJWl6hZ-ZoNgxDJHa_k1abDocMl_J7j-uddzPePSwgpaDg0QHCfFI_1YnLf7JKsMjXJ1O2Ugv75exUW0GmhK-mV2wKJiLkTl0wIXbEn0HZ4H3ZU6nEe8xO8_h8jhIbb70LQCmElQOQS8WrKVmS9gAyB8VoSruAoPFf_I9kVxDGi2X9j974sCt6y6rtXNFt4Eee2gMUSAEK6CbdIstsApw2WoNlmlLyMSAybKIcAVw1Yi6OsIsgtNZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون دود از پایگاه موشکی پارچین ، بی بی داره خنثی میکنه شاید براشون
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20602" target="_blank">📅 22:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20601">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20601" target="_blank">📅 22:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20600">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رویترز: طرح ایران برای تنگه هرمز نشدنی است، آمریکا اجازه نمی‌دهد!
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20600" target="_blank">📅 22:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20599">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اکسیوس : به گفته یک منبع آگاه آمریکایی، چند ساعت پیش ترامپ و محمد بن سلمان تلفنی با هم حرف زدند
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20599" target="_blank">📅 22:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20598">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وزیر انرژی اسرائیل (از مردان نیک روزگار): حتی اگر آمریکا و ایران به توافق برسند، اگر ایران برای احیای برنامه هسته‌ای یا توسعه برنامه موشکی خود اقدام کند، ما پاسخ خواهیم داد.
ما به هیچ توافقی که امنیت اسرائیل را کاملاً تضمین نکند، متعهد نیستیم
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20598" target="_blank">📅 22:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20597">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گزارش پرتاب چندین موشک/پهپاد از سیرجان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20597" target="_blank">📅 22:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20596">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گزارش های مردمی با سانسور : تنگه مال اقوام درجه اولشون نیست که شب خنثی سازی کنند
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20596" target="_blank">📅 22:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20595">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">قالیباف با صحبتهایی مانند آخرای شمخانی گفت:
حمله بزرگی در راه است... صبر کنید، نه، آن‌ها می‌خواهند مذاکره کنند. این دیپلماسی نمایشی است که بارها تکرار شده است.
استفاده از زور و تهدید، همراه با وعده‌های دروغین و اخبار جعلی، یک استراتژی شکست‌خورده است.
حقایق را بپذیرید و به تعهدات خود عمل کنید. ما به نمایش‌های بیشتر نیازی نداریم.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20595" target="_blank">📅 22:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20594">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گزارش مردمی : اطراف یا خود اسکله بهمن قشم رو ۲ بار زدن ۴ بار هم دروغه
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20594" target="_blank">📅 22:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20593">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بخشی از رسانه های رژیم : موشکی هشدار آمیز توسط نیروی دریایی سپاه پاسداران به سمت یک شناور متخلف در تنگه هرمز شلیک شد.
@WarRoom
بخشی دیگری از رسانه های رژیم: صداهای انفجار جزیره قشم مربوط به مهمات عمل نکرده زمان جنگه</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20593" target="_blank">📅 22:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20592">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یک صدای انفجار جدبد از دور در قشم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20592" target="_blank">📅 21:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20591">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20591" target="_blank">📅 21:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20587">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گزارش صدای ۲ انفجار‌ در قشم
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20587" target="_blank">📅 21:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20586">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Ruhollah zam and Msoud Molavi @WarRoom</div>
  <div class="tg-doc-extra">instagram.com/Yashar</div>
</div>
<a href="https://t.me/withyashar/20586" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">صحبتهای افشا شده از مسعود مولوی با روح‌الله زم در مورد اسرار سیاست و پیشبینی جنگ ایران و آمریکا.
‏این صحبتها اولین بار چند روز پس از ترور مسعود مولوی در ۲۳ آبان ۱۳۹۸ پخش شد. همچنین روح‌الله زم در مهر ۱۳۹۸ توسط جمهوری اسلامی ربوده و یک سال بعد حکمش اجرا شد.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20586" target="_blank">📅 21:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20585">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گزارش حمله سپاه به اربیل عراق
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20585" target="_blank">📅 21:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20584">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شاهزاده رضا پهلوی : جمهوری اسلامی تو شرایط ضعف و بحران مشروعیت، قصد اجرای کنوانسیون آکتائو (رژیم حقوقی دریای کاسپین) رو داره. این کار بدون اراده ملت و تضمین کامل حقوق تاریخی ایران، تهدیدی جدی علیه منافع ملیه. معاهدات 1921 و 1940 و اعلامیه آلماتی، حقوق مشترک و نیاز به توافق همه کشورهای ساحلی را تأکید کردن. اما کنوانسیون آکتائو با اجازه توافق‌های دوجانبه و چندجانبه، اصل اجماع رو دور می‌زنه و جایگاه ایران روتضعیف می‌کنه.
این اقدام از موضع ضعف و مغایر منافع ملی است. حقوق ایران تو دریای کاسپین قابل معامله نیست و هر تصمیمی بدون رضایت ملت، نامشروع و قابل بازخواست خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20584" target="_blank">📅 21:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20583">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کانال ۱۲: رئیس سازمان موساد دو رئیس بخش را به دلیل شکست در تلاش برای تغییر رژیم در ایران، برکنار کرد
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20583" target="_blank">📅 21:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20582">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2eQ5NqUVnemCZtOX9DamBmG-K2NI-xd4uiV_U2PF0r-h7xJuAGJ73xqvgUO9k-j7W_lMPxUCUbkn5QUIiNCrqeL11HHYkMQBF0VB0jWQk1aAbQkE5u5dJCqtpw5Wtkl31T42PIa3gvFKoohB164Nok4BZFsiNtEJwXaoR7YMzZvZ45ViQqvSSbFNuQ8aoQn-fvrTMH4fU0t9PEs4iExCbR-ByP7PL7otKDY6GuSwb2K0oMFPl90WQPrK8XDc71o6tBsdcN3JZkK2bMl8wwVgn_v2dK-gLEhJUCgsdJT5g8sQ5wIkcaFf3FsvkRCc46Co_SEOGTTf1ijL3otYWRHLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های جعلی، مثل همیشه، در حال انتشار شایعاتی دروغین و کاملاً بی‌اساس هستند. من از عملکرد پیت هگست کاملاً راضی و خوشحال هستم. همه چیز فوق‌العاده بوده است، از جمله حمله ما به ونزوئلا که در کمتر از یک روز به نتیجه رسید و به ما امکان داد یکی از خطرناک‌ترین جنایتکاران جهان، نیکلاس مادورو، را به دست عدالت بسپاریم. همچنین در مورد ایران نیز همه چیز به‌خوبی پیش می‌رود؛ کشوری که برای این هدف که هرگز به سلاح هسته‌ای دست پیدا نکند، به‌شدت تضعیف شده است. پیت در میان نیروهای نظامی احترام بسیار زیادی دارد و اصلاحات بزرگی انجام داده است؛ از جمله حذف برنامه‌های DEI (تنوع، برابری و شمول) و افزایش جذب نیرو به بالاترین سطح تاریخی. این شایعه را روزنامه واشنگتن کام‌پست، که یکی از بدترین رسانه‌های این حوزه است، منتشر کرده؛ آن هم با وجود اینکه ما به آنها گفته بودیم گزارششان کاملاً دروغ است. در واقع، من واقعاً معتقدم این نوع «خبررسانی» جعلی، مصداق خیانت است!
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20582" target="_blank">📅 20:35 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20581">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">توپ در زمین آمریکا است,ترامپ باید تصمیم بگیرد
الجزیره : در خصوص مذاکرات باید گفت که به نظر می‌رسد توپ از زمین ایران و عمان خارج شده و به زمین آمریکا افتاده است. اکنون چشم‌ها به رئیس‌جمهور ترامپ است تا در مورد جزئیات باقی‌مانده و تعهدات آمریکا تصمیم بگیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20581" target="_blank">📅 20:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20580">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9djB6wgXxdBUllWBeFO5aPIpxjAa5_mHsBTlVnXAJYqf3VpTAjtRQ4KD0Oa9_6K7F51nqc1ZmkDJ-OfvR3JqaLy0Uqb0s1vZ1ko7S9Fp4oZH1NHiiiccVMv71oaMgimw_MCFg9m6yEMCTLhPo8iXIG4xIoExuqikCIi7aqXiGOxrrlHRdOf-aFGsADz0z7q9juGeNqNM2afEjnzC_UPSpgQce1cvqLs48PPTBRSbnVv6W7jFKNVTZX_rnlv5vq_f9K5EXIX6Uod-2HhTlRbSP8Z8ZK-X8tE0o_T8atZSoDvHo2nz0JXcHyAJhWxmXRQWAJ6b-9cEyzvio7XEaFt1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمب‌افکن مخوف B-1b از فیرفورد بلند
شد تمرین کرد و با توجه به الگو احتمالأ سوختگیری هوایی هم امتحانی انجام داد ،  حسابی خودشو گرم کرد و آماده شد و دوباره به مبدأ برگشت
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20580" target="_blank">📅 19:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20579">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">محسن رضایی (محسن کج بند) دبیر شورای عالی امنیت ملی(جایگزین علی شمخانی) شد، اون سرش رفت اینم تهش میره @WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20579" target="_blank">📅 19:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20578">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رسانه های رژیم : طبق چارچوب مذاکرات میان ایران و عمان که نهایی نشده است ، در مرحله نخست کشتی‌های ورودی از کریدور شمالی تنگه هرمز در نزدیکی ساحل ایران و کشتی‌های خروجی از کریدور جنوبی نزدیک ساحل عمان عبور خواهند کرد. پس از پایان این دوره، تردد از هر دو کریدور متوقف شده و همه کشتی‌ها از کریدور میانی عبور می‌کنند؛ به‌گونه‌ای که ورود کشتی‌ها تحت مدیریت ایران و خروج آنها با مدیریت مشترک ایران و عمان انجام خواهد شد. همچنین هزینه عبور به‌صورت بهای خدماتی مانند سوخت‌گیری، بیمه، خدمات محیط‌زیستی و سایر خدمات تعیین می‌شود و ادعای دریافت تعرفه ثابت ۳ یا ۷ درصد از ارزش محموله‌ها تکذیب شده است. بر اساس این گزارش، عبور کشتی‌های آمریکایی و اسرائیلی از تنگه هرمز نیز ممنوع خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20578" target="_blank">📅 19:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20577">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کانال ۱۲ : نیروی هوایی ایالات متحده تخلیه بخشی از سوخت‌رسان‌ها در فرودگاه بن گوریون را آغاز کرده است @WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20577" target="_blank">📅 19:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20576">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuTnL0xrexuZWzUX8NkqQK0JWNujEgdtTZlQHNrGEU2IrNV41HVJzkhxCAg790lB7hbH2tZef82wAWo9s704F3KLfJZqV81ESQkQz7RtsFztZM3NbAmY1BVa3sS56q0SFjy6AdrLmL8sawoiIRK-7u9U6tJz-QVXXFpNBdxxfYy3qAcQiOOohOGQQCsn83J_Ved2FEbUswv2kcAk90-0jiLhrcIrORzNZcAO2auUKXLWZhN1Af5SmT7faGztCdzeX87kraHRwfD6Gjei4SxgNKdp6lbH6J9sIxySBP4PQ2V4MdEh1OrmRe0rr5z5QGyqOf3Wieq2gJTeEZXZfkzcZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی (محسن کج بند) دبیر شورای عالی امنیت ملی(جایگزین علی شمخانی) شد، اون سرش رفت اینم تهش میره
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20576" target="_blank">📅 19:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20575">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تعدادی از نیروهای عربستان سعودی کشته و زخمی شدند، پس از آنکه یک موشک شلیک شده از یمن مستقیماً به پایگاه‌های نیروهای تیپ واکنش سریع اصابت کرد. @WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20575" target="_blank">📅 18:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20574">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ان‌بی‌سی نیوز: پنتاگون جلسه اضطراری برای تأمین تسلیحات برگزار می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20574" target="_blank">📅 17:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20573">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حسین شریعتمداری نماینده ولی فقیه و مدیرمسئول روزنامه کیهان : باز شدن تنگه هرمز یعنی باز کردن راه فرار دشمن و از دست دادن یکی از مهم‌ترین اهرم‌های فشار جمهوری اسلامی.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20573" target="_blank">📅 17:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20572">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خبرگزاری رویترز : هنوز درباره نحوه اجرای «کنترل» ایران بر تنگه هرمز توافق نهایی حاصل نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20572" target="_blank">📅 16:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20571">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54aca75746.mp4?token=rsHnq2oFJYgLpz-0u6vEa583awixj-0R63ePtj8xfgGuOveGtHXTIxSVJ-r4dnakbXBBumpSNB1yitORzzLQN2dkvGEpjDgfjP0pvsNW7RWYc33MUV307INFSkG47scR9DtP8aq84r_6Rcjjo9qd-shuN3sLvE8280gLP3bcTSjC1RHP6RLgTnZUee9w3yL2m3WPEHXbQeOYsEG_OjcVYZYMJ0XBKzo7sSlkO_K_N69q1OCVKwcYZpXHMTznRpA_bQ2OPAi2XAI7d_hG5dwsicEC3dg87deyyxTNR0LdlLtHxZOHZzjk5-YxWCCbfIwiBcCfVkOpeiFO72oiS0cIOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54aca75746.mp4?token=rsHnq2oFJYgLpz-0u6vEa583awixj-0R63ePtj8xfgGuOveGtHXTIxSVJ-r4dnakbXBBumpSNB1yitORzzLQN2dkvGEpjDgfjP0pvsNW7RWYc33MUV307INFSkG47scR9DtP8aq84r_6Rcjjo9qd-shuN3sLvE8280gLP3bcTSjC1RHP6RLgTnZUee9w3yL2m3WPEHXbQeOYsEG_OjcVYZYMJ0XBKzo7sSlkO_K_N69q1OCVKwcYZpXHMTznRpA_bQ2OPAi2XAI7d_hG5dwsicEC3dg87deyyxTNR0LdlLtHxZOHZzjk5-YxWCCbfIwiBcCfVkOpeiFO72oiS0cIOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مجری: آیا هنوز معتقدید که نوعی تغییر رژیم در ایران امکان‌پذیر است؟
‏مایک پمپئو: 100٪
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20571" target="_blank">📅 16:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20570">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">منابعی از گروه تروریستی حوثی های یمن به رسانه های رژیم اعلام کردند تا دقایقی دیگر، نیروهای مسلح ما با انتشار بیانیه‌ای از یک عملیات نظامی گسترده و ویژه خبر خواهند داد.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20570" target="_blank">📅 16:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20569">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کویت با استناد به امنیت ملی، دستور تعطیلی فوری تنها مدرسه خصوصی ایرانی خود را صادر کرد
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20569" target="_blank">📅 15:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20568">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b68ab7702.mp4?token=qlig2vivaXWs3VTXqO-31kpYr1FipiwkbnYS0OFQEykDvIvqYJx40EKvmMnNkwG3hlphRQg3Gzj75mVRZaYURoLjm-N-DRithhlcSP59wMSqNwxz4s5oVm5M6wCzTb_ltjHSsBkKYqg8k5uIHlQP4jBCVLgApTviQIdEFWpcKBy6yGVVoLfaECiGuOEu1X1KuS4EDzjvdCOt_Ke8IOFftr6zyFaHqS0xZH2KPfppn3f6Q_NxFarzwQGP7BAoSSPuwfr7Dyjo75SCn2ai9iom11ahN0Uv6_-svFeKo0eBzRfXPQzrMrL7v2BAiXHgnDK2ScWXAUHZkuebJ7QFkRpW9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b68ab7702.mp4?token=qlig2vivaXWs3VTXqO-31kpYr1FipiwkbnYS0OFQEykDvIvqYJx40EKvmMnNkwG3hlphRQg3Gzj75mVRZaYURoLjm-N-DRithhlcSP59wMSqNwxz4s5oVm5M6wCzTb_ltjHSsBkKYqg8k5uIHlQP4jBCVLgApTviQIdEFWpcKBy6yGVVoLfaECiGuOEu1X1KuS4EDzjvdCOt_Ke8IOFftr6zyFaHqS0xZH2KPfppn3f6Q_NxFarzwQGP7BAoSSPuwfr7Dyjo75SCn2ai9iom11ahN0Uv6_-svFeKo0eBzRfXPQzrMrL7v2BAiXHgnDK2ScWXAUHZkuebJ7QFkRpW9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مایک جانسون، رئیس جمهوری‌خواه مجلس نمایندگان آمریکا، گفت:
‏«ما در انتخابات میان‌دوره‌ای پیروز خواهیم شد؛ چه مسئله رژیم تروریستی جمهوری اسلامی را پیش از انتخابات حل کرده باشیم و چه نکرده باشیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20568" target="_blank">📅 15:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20567">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">جروزالیم پست: اتهام جاسوسی به نفع ایران به دو زوج اهل عسقلان وارد شد.
این زوج، اقدام به تصویربرداری از مکان‌های حساس، از جمله بندر ایلات و کوه هرتزل کرده بودند و همچنین خانه‌های افراد امنیتی را تحت نظارت قرار داده بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20567" target="_blank">📅 14:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20566">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6MaxBqM9EpWLU0H5w_JnOV7pTTne_kp4wWCjNec7lGLZpp0hSLSrLtflQV3Molr5JGc3zOQgh2822XyMy1UwgM78Aqn5RH_XYbuYq_46x_jitVCo0Th0WwH8VAsutd1_gDh2dp-U07_-2eRYjiwhdBOjZiT0Q0YkiMvodF3ygK6KcJUDb_Rg1IZbEOORi7Njzrn8D2RLs84rt0tDNnYgScr_Qe2n5uPEj4Ys0u7MmQRZUc_WSKiSbdkJLu2CNfcKaGr-OiNZ1t9sjm0tbMjWldzQZ6gXrZGsaZbXkszsQMBgYp6qAxkfapK1YqCmUPFcXtAnxI31P2KN5MnutsjXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۲ : نیروی هوایی ایالات متحده تخلیه بخشی از سوخت‌رسان‌ها در فرودگاه بن گوریون را آغاز کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20566" target="_blank">📅 14:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20565">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حکومت ایران عوارض ۷٪ را بر تمام کشتی‌های تجاری عبوری از تنگه هرمز اعلام کرده است , این امر برای ایران ۳۸۵ میلیون دلار خالص روزانه یا بیش از ۱۰۰ میلیارد دلار خالص سالانه با حجم ترافیک پیش از جنگ ایجاد می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20565" target="_blank">📅 14:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20564">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کمیسر عالی حقوق بشر سازمان ملل می‌گوید ایران از ماه مارس حداقل ۵۶ نفر را اعدام کرده است - افزایش چشمگیری نسبت به ۱۵ مورد تخمینی در مدت مشابه سال گذشته.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20564" target="_blank">📅 13:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20563">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏واشینگتن پست گزارش داد که دونالد ترامپ، رییس‌جمهوری آمریکا، در دیداری خصوصی با حامیان مالی خود گفته است: در نهایت، باید جی‌دی را انتخاب کنیم. این اظهارنظر نشانه‌ای از احتمال حمایت او از جی‌دی ونس در انتخابات ریاست‌جمهوری ۲۰۲۸ است.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20563" target="_blank">📅 13:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20562">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حوثی های یمن موشک شلیک کردند  @WarRoom
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20562" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20561">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">عبدال السید در انتخابات مقدماتی دموکرات‌ها برای کرسی سنای میشیگان پیروز شد. او در ماه نوامبر با مایک راجرز، نماینده پیشین جمهوری‌خواه، رقابت می‌کند و در صورت پیروزی، نخستین سناتور مسلمان تاریخ آمریکا خواهد شد @WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20561" target="_blank">📅 12:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20560">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حوثی های یمن موشک شلیک کردند
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20560" target="_blank">📅 11:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20559">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یاشار : امروز سنای آمریکا قرار است ساعت
۱۰:۳۰ صبح به وقت شرق آمریکا
، برابر با
۱۸:۳۰ به وقت تهران
، درباره لایحه
CLARITY Act
رأی‌گیری کند. این لایحه با هدف ایجاد چارچوب قانونی شفاف برای بازار ارزهای دیجیتال تدوین شده و از مهم‌ترین قوانین تاریخ صنعت کریپتو به شمار می‌رود. در صورت تصویب، بسیاری از تحلیلگران انتظار دارند بیت‌کوین در کوتاه‌مدت بین
۳ تا ۸ درصد
رشد کند و آلت‌کوین‌ها نیز افزایش بیشتری را تجربه کنند. در صورت رد شدن، احتمال اصلاح
۵ تا ۱۰ درصدی
قیمت بیت‌کوین وجود دارد، هرچند شدت واکنش بازار به ادامه مذاکرات بستگی خواهد داشت. با توجه به وضعیت فعلی مذاکرات، احتمال پیشبرد این لایحه حدود
۵۵ تا ۶۵ درصد
و احتمال شکست آن
۳۵ تا ۴۵ درصد
برآورد می‌شود، اما هنوز اختلافات سیاسی بر سر برخی بندهای آن به‌طور کامل برطرف نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20559" target="_blank">📅 10:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20558">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPPSkNJ5WYGQm2ekmGnlDZb3OLTjmhjh64n8S2-o4C2nmOcuqUPt0cJ2_-xnCkVDPkHrkIZ_Sc4RDtA1zoMUw9oXcpbAKBwilb7HHM2gLsljNamvhqQnidPFeRYzff6lwKEwCTQQlKfYkz_kcfzT7Q_Rmrtfwy5A8X4S3JPqdBzJLbpvnoOJxAL_lSnQmM_3neLtDXs5fmfFOYsnhYqbaE33ouxNMmFfAk5jKFpVOLce-b4WmdTSvWxj7PvIF8bHMTpH-liaY1p8BfumTzRPSkp5S4Fc9pOX2ZsG4aB6a1-OT9iNd4bqHqRmlYb7yu2M4Qm9t56X2kDkgqXWzypR5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایالات متحده مقادیر عظیمی «مهمات»، به ویژه از انواع خاص، دارد. علاوه بر این، مقادیر زیادی از آنها در صورت نیاز تولید و به ما ارسال می‌شود. شرکت‌های دفاعی در حال ساخت بیشترین تعداد کارخانه و تأسیسات در تاریخ کشورمان هستند. «افشاگران» این اظهارات…</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20558" target="_blank">📅 10:03 · 15 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
