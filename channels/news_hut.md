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
<img src="https://cdn4.telesco.pe/file/IvaKxBN-zZxyCfl2FOU1o9F0aINk4HkmGt05XuIpiB4Vxbd3US_fomo3SCuFk8ncD5fqw_PTPrJncuyfuBg6xCxsjyBwQ61ExvYtiXEmCOj4OFKzcLcmMOX01QKvu-E1ogSAD7Z0PCGCX3YIAGHZjmfwKLj0PMjfrpi5W_k_jXRoUFcCxyCI6J1ll-F39rM45nk39o-PqSvpl8eeHVudI3WIG3iVaGHEEchM05Y0tmiTou8X_wVxJg9iR6v3-22r0wLS90-aIoOXKR24rnyTp-jr7Pp_n9sGk9BvKgiBmFB7iH_ovzlkid7b8kUdMyKPHvo1w0A3K44K8hvnYSfVrQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 119K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-29 09:23:42</div>
<hr>

<div class="tg-post" id="msg-70309">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pawFlE9o-kPTZYgNFkHW6t71wd_LrjUYdqHNjkFNEHeX-UYwhrpHhycodq32n5qlvj4IWPMNH8WGqtaPg2XQ54Y5EKeIvgCZGWva0LblzNXB7Aic766h-rvAZ2Jd6rJhqClsQBcrwv9pkbHTABioOeE4RsDbZzCf0VRztG2OxNbwqd8hJJtccPT7dVbtXEYoclEs69vK3iqi_ELYMOMLhFx_Ie8-P9WpFGJqwAmb25TeXO2T08atVx6AFYGqW9wOxQ0j1pYwmvEXlQYTSz7kIPlRuEC1yR4BBL_cSiv6-lt9QGyE78aDPsEB0hRL00njdCHAdmqhZLsOV84JB926KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/esZIlzrzhq3lmOeWuSSnNCAcMSS_lbY-1zN-TeaMUq2-eWRN0qMEyuy1_3tXu_DwmL7THQRMErfJoTJcbDyuHwVszkwAOjh6hwpWK9tte1PWPEOjw8rOKdd0qo3tVkp5syKFD4gSlfaHff0RhhxC642tLXfEVXkcfs8P3J5TIzefQb19Xn0ucHzeOkiW8GYkfjP8ddkjq8pEDIEyF5G_YZfpB2-KTvMqi514H9DLg0TO1-_MYGnSCeQywsi1uEaKt043ja_L0XBb_qTNLqNss0IZsnJYJHVFwBU-XhB6zglD6xsYnIZHD8JlAa1T-olHl633mI0ooeZfkq_yY5_3Ow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e1fd6dc78.mp4?token=svnBGdX4pFM-ewj0gDyN2AnidDK5G_8ndt8Hi9Rgpt_MQyHBxEO2ojBtTvWJ8IoUGAytAXhSErgo26GHccPDWizUoXIPtPIZwRilvwef8IHsA7foYD5tOay1wP4iSTuvLXWVz_c1yaieA1uZmY2tQ4nfp9ON5PUqJ1Rfejb-SSfClxqp2NydoXNhfwmw3Wu0Z8-vRfdqqJ1GOLOQxWxK3P5EDSyEAENakDWeHzXwazUSFBw2FUArG0eNGncSGnyZDfYjhQfiGC5IxVo9EF8OTX2quYeb_45p0TbmwCe8_QLXdbF-iYcC2MHy5npcV6fM-oNZuwPvljc-vZnC57sGUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e1fd6dc78.mp4?token=svnBGdX4pFM-ewj0gDyN2AnidDK5G_8ndt8Hi9Rgpt_MQyHBxEO2ojBtTvWJ8IoUGAytAXhSErgo26GHccPDWizUoXIPtPIZwRilvwef8IHsA7foYD5tOay1wP4iSTuvLXWVz_c1yaieA1uZmY2tQ4nfp9ON5PUqJ1Rfejb-SSfClxqp2NydoXNhfwmw3Wu0Z8-vRfdqqJ1GOLOQxWxK3P5EDSyEAENakDWeHzXwazUSFBw2FUArG0eNGncSGnyZDfYjhQfiGC5IxVo9EF8OTX2quYeb_45p0TbmwCe8_QLXdbF-iYcC2MHy5npcV6fM-oNZuwPvljc-vZnC57sGUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ظاهرا علی خامنه‌ای به یه شاعر سفارش داده که یه شعر تولید کنه که خامنه‌ای بعنوان سروده‌ خودش منتشر کنه، شاعر هم یه شعر کرده تو پاچش که اگه حروف اول مصرع‌ها رو به هم بچسبونی میشه:
"من علی خامنه‌ای زاده شیطانم"
🔴
حالا رسانه های حکومتی تازه متوجه گاف شدن و دارن شعر رو از سایتا پاک میکنن
👅
@News_Hut</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/news_hut/70309" target="_blank">📅 09:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70308">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDMUAbiYOanEajcXFexkpykpYb-Rw_GyOpiaxgtyQ1zlJEU9WI1_Ay4styo4l1TXUXN5RJHpwOLjVrhzTSDG0Sdswz0fvXlXD-rUXwxPr6QCBShUAoDAicKTj0dTzEUQ52azt0woi1xspLX2dS88N5pk0DB0TtnXkn3nCl0LimBguNtU3u_xJ1aBvQ3jT3vax5DKRPQCjPEjINDtzPf04GsSjzRxkZXSrBVk6mSdb5yu_GPLVJ_POWO-Ry8e4VJFZrcPR8ZM8tPchif9FQeMrorgqr1O4kXBYK_qMJ70UIZtznSvUZAo1DR5PTnHvfL9bK1YMyP5ullwaRQdf-su1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
🇺🇸
#فوری
؛ترامپ درباره‌ایران:هیچ‌کس به اندازه من به جمهوری اسلامی ایران فرصت دستیابی به توافق نداده است. اما متأسفانه برای آن‌ها، این فرصت از دست رفت.
از این رو، امروز من خبر از اجرای «ویرانگرترین عملیات اقتصادی تاریخ علیه یک کشور» می‌دهم!
این اقدام، مصداق جنگ اقتصادی و انزوا در ابعادی بی‌سابقه خواهد بود.
نیروی دریایی‌شان از میان رفته، نیروی هوایی‌شان نابود شده، کارخانه‌های نظامی‌شان به تلی از خاکستر بدل گشته، ارزش پول ملی‌شان از بین رفته و کشورشان در آستانه فروپاشی کامل قرار دارد.
همچنین امروز اعلام می‌کنم هر کشوری که به مؤسسات مالی، شرکت‌های تجاری، فرودگاه‌ها یا نهادهای دولتی خود اجازه دهد تا هرگونه شریان حیاتی برای ایران فراهم کنند، خود با پیامدهای اقتصادی سهمگینی روبرو خواهد شد.
قاچاق نفت، خطوط سوآپ (معاوضه)، انتقال پول نقد، صرافی‌ها، ثبت کشتی‌ها و شرکت‌های پوششی؛ همه این فعالیت‌ها باید همین حالا متوقف شوند. شما خود می‌دانید که چه کسانی هستید.
این یک «روز سرنوشت‌ساز اقتصادی» (D-Day اقتصادی) خواهد بود و ما نیازمند آنیم که تمامی متحدانمان در کنار ایالات متحده آمریکا بایستند تا تهدید ایران را منزوی و خنثی کنند.
این دیوانگان در تنگنا گرفتار شده‌اند و این اقدامات تاریخی، آن‌ها و توانایی‌شان در گسترش تروریسم در سراسر جهان را فلج خواهد کرد.
ایران هرگز به سلاح هسته‌ای دست نخواهد
یافت.
از توجه شما به این موضوع سپاسگزارم. رئیس‌جمهور دونالد جی. ترامپ.
@News_Hut</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/news_hut/70308" target="_blank">📅 08:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70307">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔥
امشب چه تیمی می‌درخشه؟
⚽
کدوم بازی گل‌دار می‌شه؟
📊
کدوم تیم ارزش اعتماد بیشتری داره؟  ما بازی‌ها رو قبل از شروع، با آمار و تحلیل بررسی می‌کنیم؛ نه با شانس و حدس!
📌
برای دنبال‌کردن تحلیل‌های روزانه فوتبال عضو شو:
🔗
https://t.me/+nbm7Tb2pz8VjMDlk</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/70307" target="_blank">📅 02:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70306">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=YpOH_eOFflf2ZrmdDfwWC8aZCILQByoLzGN82bUZWgqJr-QTPkDpvbb9aRvFMpsMY6nWUcn8rLBbSu4gRKicgjPwC8V9cmDWLgxg4jHO45OsXft6O-85X_5H8OTYc3bl0Ll4jgeM_Xymp7CQYnihiK-eQkHy8PFNszHVLiyxWdnJ-XMBC1K5v892w4KhXMWxSUNY749QGxn84BuE-kdg8TSjT4Rt0A9wAFul0EVouIk6OzulT27CAuo7Abw0TfWP1SiVNJSTsZQHrRAPo8Hx-ZwtOwa_xne0JrRhdKPQwodVNYWoZDMCCRcBsfFbtgON085OLyQuVicdHD1ZMTT42g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=YpOH_eOFflf2ZrmdDfwWC8aZCILQByoLzGN82bUZWgqJr-QTPkDpvbb9aRvFMpsMY6nWUcn8rLBbSu4gRKicgjPwC8V9cmDWLgxg4jHO45OsXft6O-85X_5H8OTYc3bl0Ll4jgeM_Xymp7CQYnihiK-eQkHy8PFNszHVLiyxWdnJ-XMBC1K5v892w4KhXMWxSUNY749QGxn84BuE-kdg8TSjT4Rt0A9wAFul0EVouIk6OzulT27CAuo7Abw0TfWP1SiVNJSTsZQHrRAPo8Hx-ZwtOwa_xne0JrRhdKPQwodVNYWoZDMCCRcBsfFbtgON085OLyQuVicdHD1ZMTT42g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
امشب چه تیمی می‌درخشه؟
⚽
کدوم بازی گل‌دار می‌شه؟
📊
کدوم تیم ارزش اعتماد بیشتری داره؟
ما بازی‌ها رو قبل از شروع، با آمار و تحلیل بررسی می‌کنیم؛ نه با شانس و حدس!
📌
برای دنبال‌کردن تحلیل‌های روزانه فوتبال عضو شو:
🔗
https://t.me/+nbm7Tb2pz8VjMDlk</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/70306" target="_blank">📅 02:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70302">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c25635056.mp4?token=UwDOQd1dPcD9X4f83Dn8rADRIhW24HK4woksg0Qy-Zoo2YHiWyYSRgACrkiNiDQGNx0rBb79v6YtCl7pqXgiQgDHcKycL-7i7kMElIKwB5XwSfQa35_bQm8l5gIP24IERTK3bkXx9e0hRbsMRlK3-8m1L2kUiChNo6JfY95Vn2GvzOUyskS7g8ia27qB3UHYfYZXukM_ljN0Y1k-5yfajDUt5VFUwzxMm_5RW7VZSNx-ZqDpytQgNdX7YHfuWSyEtoQNMgmegE7D3OS0nbycyolwRZniSNkiniZGDKGWHQh_jqm9d_fk56QnNf7Gp8DrU5O0QZ27qrWm4Mch2rk5dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c25635056.mp4?token=UwDOQd1dPcD9X4f83Dn8rADRIhW24HK4woksg0Qy-Zoo2YHiWyYSRgACrkiNiDQGNx0rBb79v6YtCl7pqXgiQgDHcKycL-7i7kMElIKwB5XwSfQa35_bQm8l5gIP24IERTK3bkXx9e0hRbsMRlK3-8m1L2kUiChNo6JfY95Vn2GvzOUyskS7g8ia27qB3UHYfYZXukM_ljN0Y1k-5yfajDUt5VFUwzxMm_5RW7VZSNx-ZqDpytQgNdX7YHfuWSyEtoQNMgmegE7D3OS0nbycyolwRZniSNkiniZGDKGWHQh_jqm9d_fk56QnNf7Gp8DrU5O0QZ27qrWm4Mch2rk5dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
حمله موشکی گسترده روسیه علیه کیف در حال انجام است
؛
بیش از ۲۵ موشک، از جمله موشک‌های اسکندر-ام، موشک‌های کره شمالی KN-۲۳ و زیرکون، به سمت کیف شلیک شده‌اند.
هفت بمب‌افکن استراتژیک Tu-۹۵MS و دو بمب‌افکن استراتژیک Tu-۱۶۰ در حال حاضر در هوا هستند و انتظار می‌رود به زودی موشک‌های Kh-۱۰۱ را شلیک کنند. همچنین انتظار می‌رود موشک‌های کروز کالیبر به زودی وارد حریم هوایی اوکراین شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/70302" target="_blank">📅 01:17 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70301">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/443c91ecee.mp4?token=NaSLNBA099G9NC8-zX-8OrXnkVnzQWdW7LVPW5OhFxLylzEj6GdM_VBzW_PfHfnb4GwkHMl19LGABDPJovKdS3G4aT8ZYY6K8XxakvDwpEC9jO8C-1Xckep_cHRnjbTNvSr98VeSBBdlVK23e2d7Eup5X9GVNKKvRrRFbo4NjXOzM3NaEtaMCNnNO_hfO6SdIW4Kk1ySwHOpxPkrQSAeUD3sq-cjsiWDsd8nIqBANZGX-246smFIVGD0I73LySKqgHMKAGIiO7aT4Kt487bmK3AHTj69qqCl5VQdYFllw_6JdH4zwCpU2bLD3b3Q0TZ9N1Khvu3u-tpiwevJdtD0NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/443c91ecee.mp4?token=NaSLNBA099G9NC8-zX-8OrXnkVnzQWdW7LVPW5OhFxLylzEj6GdM_VBzW_PfHfnb4GwkHMl19LGABDPJovKdS3G4aT8ZYY6K8XxakvDwpEC9jO8C-1Xckep_cHRnjbTNvSr98VeSBBdlVK23e2d7Eup5X9GVNKKvRrRFbo4NjXOzM3NaEtaMCNnNO_hfO6SdIW4Kk1ySwHOpxPkrQSAeUD3sq-cjsiWDsd8nIqBANZGX-246smFIVGD0I73LySKqgHMKAGIiO7aT4Kt487bmK3AHTj69qqCl5VQdYFllw_6JdH4zwCpU2bLD3b3Q0TZ9N1Khvu3u-tpiwevJdtD0NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
تصاویری از یک سرباز اوکراینی که با استفاده از تیربار MG 3 (ارائه‌شده توسط آلمان)، یک پهپاد تهاجمی روسیِ در حال نزدیک‌شدن را از فاصله‌ای بسیار نزدیک سرنگون می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/70301" target="_blank">📅 01:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70300">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvHqkLrLPsaq-0I55yQaGmIf2b9G0CRLQZQs1NSGyE8AnOcR1-tgiSe3Wxa8SizPp-XTphMurxM1-dr0JGcmJMhsQGsZEs485jpkVZ34swlpsdhDu--deJ3FHNXwZpj5iYr1h1ccmbXsgFM-LTpI3w906u-T25fiZoIHkgln_cURX4COjw0O0OY050Fb6lvnF0fSvWPNBWk5CQH8GMvftozM82D_IunvCqf1c1FNqTtFS6wLoQGRcWryvwxqS3hU_IbCcNhGUeF0NYTu5CL7jYzy3yAWHUMI346Bau1MQDSno3GXAtYc6hKgVKoJgqVGeq8nr97M2CjqtP0BGI7w2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
علی قلهکی:
اگر آمریکا بتواند مسیر جنوبی تنگه هرمز در آب‌های عمان را برای عبور کشتی‌ها آماده و امن کند و انتقال نفت را از این مسیر انجام دهد، اهرم فشار تنگه هرمز تا حد زیادی کم‌اثر خواهد شد.
در این صورت، به گفته قهلکی، آمریکا ممکن است دیگر نیازی به رفع محاصره، لغو تحریم‌ها یا آزادسازی منابع مالی ایران نداشته باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/70300" target="_blank">📅 00:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70299">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfynEtdNFS28mvTTpa3Mc-paZYBILB35SnauP79jOPkwqdZj8skcW5qR_BASD5eijo4VBAo0n-MeQm_rs1KQm-eTNT9zOYaOdpB8DXN2JB7zPPpRFiGXcKjwCDRMSzXbhPh0Z5sirpLy-yKhZf2PkG3XY3E3eeqEJg7a8TR7GzdZVw2cBB8w23P9B7OvnQ2nRLZbbATOf3cL0OvwQx7xZ8CLwV2smx6e4KtYPc_DGRsD6Cp8nrnYl6furPIXT8Ohm4cyVp5lMxFZT4dpls3p9Twgz0VULUYEGYZiLYlqeUsYwyWB6lXTw0QQlgu-QHRpyIwZa9BihVevIfzD9GcEHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هم قیمت بنزین تا ماه بعد و هم قیمت دلار و ماشین ایرانی رو تا اخر شهریور ماه گفته؛ این کانال تمام پیشبینی ها همراه تاریخ وقوع رو میگه:
👈
مشاهده بدون سانسور</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/70299" target="_blank">📅 00:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70298">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YK0Jeqk99_bW7cLNxCG9CdvNWxNBUOUQVVwGI1F4u8KSZNF8E6ea6M5k9MSUnsrvnu7ElS-tvEwPhLX233br8ekO_DqshlbDvafZS07nwhOtaQ3-KnbXAP3KS-AvfAm5llZex-WHuAIwZEu8mv1MV7xGQni5hiG2D2tUcCTekh52AkMkC6FQl9DsHgg8Pkh1eYkPDBq3GFm7O86abGHzTI1QUINNZ12sz_UbZnCaA5-KenBM13T1JVaaIWNwbWMhgR2Ugkd43fecMNZBvq1WsCfEJITWordEzpFSXFmUZVpYPZj2y4g1XqN-VvdeBP9Rb2AsB6cEYn5GN-Gci-9IDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
📰
اکسیوس: ارتش ایالات متحده بی‌سروصدا یک کریدور کشتیرانی در بخش جنوبی تنگه هرمز ایجاد کرده است که به ۱۵ تا ۲۰ نفتکش اجازه می‌دهد هر شب در امتداد سواحل عمان وارد خلیج‌فارس شده و از آن خارج شوند.
مقامات آمریکایی می‌گویند که این عملیات اکنون امکان جابه‌جایی روزانه نزدیک به ۱۰ میلیون بشکه نفت را فراهم کرده است — که تقریباً معادل نیمی از حجم پیش از آغاز جنگ است — و در برخی شب‌ها میزان نفت منتقل‌شده به ۱۵ تا ۲۰ میلیون بشکه می‌رسد.
ایالات متحده هماهنگی‌های لازم را هم برای نفتکش‌های پر (در حال خروج از خلیج فارس) و هم برای شناورهای خالی (در حال ورود برای بارگیری نفت از امارات، بحرین و کویت) انجام می‌دهد. کشتی‌ها در قالب گروه‌های زمان‌بندی‌شده و تحت پوشش هوایی آمریکا حرکت می‌کنند و جنگنده‌ها برای رصد پهپادها و موشک‌های کروز ایران، عملیات پایش را انجام می‌دهند.
نیروهای آمریکایی تاکنون بارها حملات ایران را دفع کرده‌اند؛ از جمله در شامگاه دوشنبه که هشت پهپاد و دو موشک کروز را رهگیری و سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/70298" target="_blank">📅 00:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70297">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a5dabd912.mp4?token=XOKBrE8AYN2VU5BqG2JZkVR_U5PDc47CEFtRB517NVpzNr6ZORy8NYZiVh526zNtp9lbVrsLfD2Hp_sgBU9PUQR-K0BzGggPItdVfJqkMT8TqgcN_AvRB8HhvhykOvMieL74AJCcjuZdnKmxoqV9yRsbGSNXwuL5IMibn5qlptXrsJ-toatyUXU9rkb2Jal6di8WpFbUeW-9_MX1A0qiIJVAKKY5wp0UKByAAqcC6g77H-vEp8hzrWmRT7NvI5BeqO2v53lY-MRz4O7e761gZj-mgcun8zn3NKJmNrQXoNVUx5vA2wSbkxcxchJafigIRtV6Yq7BmFfAZearFtXHUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a5dabd912.mp4?token=XOKBrE8AYN2VU5BqG2JZkVR_U5PDc47CEFtRB517NVpzNr6ZORy8NYZiVh526zNtp9lbVrsLfD2Hp_sgBU9PUQR-K0BzGggPItdVfJqkMT8TqgcN_AvRB8HhvhykOvMieL74AJCcjuZdnKmxoqV9yRsbGSNXwuL5IMibn5qlptXrsJ-toatyUXU9rkb2Jal6di8WpFbUeW-9_MX1A0qiIJVAKKY5wp0UKByAAqcC6g77H-vEp8hzrWmRT7NvI5BeqO2v53lY-MRz4O7e761gZj-mgcun8zn3NKJmNrQXoNVUx5vA2wSbkxcxchJafigIRtV6Yq7BmFfAZearFtXHUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ما مواردی داریم که می‌توانیم ایران را بابت آن‌ها تحریم کنیم. ما تحریم‌های بسیار سخت‌گیرانه‌ای در اختیار داریم و خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70297" target="_blank">📅 23:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70296">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf1eb3322.mp4?token=laL_2Sv-AP-0sMXFCcZJ-m1ysT2gfh8SqF1nToyvJgykUWFLZqZ9L9IyyDWorZy9NtOyVD_RrXgY739diINoaA-43JNw7AfF8HqbxutFGfJ52K_2_Gmh_mHBDizBf4vTDpLOUMXeirHukGlSAOpE5oGmyIKvQJ8_wov-7-pxxpjKVt4hAHis4NaDd8QKgCPF8Zy0q5TXYRQvgp_kVfHZwuNZ11nPSWydJrgaAVUuYfQwW2Ro_h2lyHVzLE3HtjUTZgIcWkweuNnkuLA_lTn2AhZPqTq_oUC1NbAguYA2mvjKT56TXSLb-C1u7BezQF3lYQQ2REhVX8kpZeztvHVqZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf1eb3322.mp4?token=laL_2Sv-AP-0sMXFCcZJ-m1ysT2gfh8SqF1nToyvJgykUWFLZqZ9L9IyyDWorZy9NtOyVD_RrXgY739diINoaA-43JNw7AfF8HqbxutFGfJ52K_2_Gmh_mHBDizBf4vTDpLOUMXeirHukGlSAOpE5oGmyIKvQJ8_wov-7-pxxpjKVt4hAHis4NaDd8QKgCPF8Zy0q5TXYRQvgp_kVfHZwuNZ11nPSWydJrgaAVUuYfQwW2Ro_h2lyHVzLE3HtjUTZgIcWkweuNnkuLA_lTn2AhZPqTq_oUC1NbAguYA2mvjKT56TXSLb-C1u7BezQF3lYQQ2REhVX8kpZeztvHVqZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
سیدمحمد خاتمی:
فرصتی که در تفاهم‌نامه ایجاد شده اگر از دست بدهیم دچار مشکلات عجیب می‌شویم
تفاهم‌نامه نظیر ندارد
بعد از جنگ‌جهانی دوم هیچ سندی که به امضای رئیس جمهور آمریکا رسیده باشد اینقدر امتیاز به طرف مقابل نداده
ما در موضع عزت به این‌ تفاهم‌نامه رسیدیم
دست آقای پزشکیان را می‌بوسم که شجاعانه و فداکارانه این تفاهم‌نامه را امضا کرد
تقدیر می‌کنم از شعام که رای دادند و رهبری که تایید کردند
هر گامی که به سوی رفع جنگ و برداشتن محدودیت برای ایران و باز شدن راه به سوی آینده باشد را باید تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/70296" target="_blank">📅 23:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70295">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utjoBOrRXikos6DaEBKNCb2J-ame8eB27UUhxrwGGHQR4ORyXysxWWkSHIrQPO7SCH2LwtQnCWx5s431hGl74qxqIF1IrFMZkMgBb_vTgcbcMY7tignRTPDJk5IyZsNSKf3-idMYCoCi7iLJUNQA0AQVnPWNnEiiGHC0CBFX5q0mkvmTgYY_AgtJCig_H6nw0GblEUuNITMp49ALF0_R67tphWeSenaR5dxph3TrAQpPsb9ERoPVqycS6fBDLZ9XFta67wrazpwKEzHum54YBTIgO5-rbKyIa1DS4YVS_bmnM2SreGM_mxS4MMZLjp_xcu2klCHfBQh3JvBkgrs6CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
قالیباف در جواب ترامپ با کل‌ش تنگه هرمزو بست.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/70295" target="_blank">📅 22:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70294">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44e544df4f.mp4?token=Nxq9Gs8GIFucSwKAib5CWeOX2cxpC2jo1a8TVxxSp4TN9Kyv4lxfNB1nJia52eX4gkTSzKSOqj1hNd2bjr6xAunofbSE39hDAMMmFXsF8EoDrnxp_Ew1ry2l09LPeCfSfHikXTf5EwpgpwAPmOxzKZFyKcq_xq-692vTcZdBDp0RiEUC3s1CgqNnGkmSR1CWmTDX_K3AKxRYoN0bQwuorL-5U74Rkca2JVxMfVpi_U_nJtRjKg38IxLWugiwM06yNLveSi8XAWAq2tG_Q-CeXdU_cR6lfPtZuAzj2F9_WB7Vut6nHNZJ1ORXOcYhp3vyGowj0q5XSI9nP-DKa1Zg6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44e544df4f.mp4?token=Nxq9Gs8GIFucSwKAib5CWeOX2cxpC2jo1a8TVxxSp4TN9Kyv4lxfNB1nJia52eX4gkTSzKSOqj1hNd2bjr6xAunofbSE39hDAMMmFXsF8EoDrnxp_Ew1ry2l09LPeCfSfHikXTf5EwpgpwAPmOxzKZFyKcq_xq-692vTcZdBDp0RiEUC3s1CgqNnGkmSR1CWmTDX_K3AKxRYoN0bQwuorL-5U74Rkca2JVxMfVpi_U_nJtRjKg38IxLWugiwM06yNLveSi8XAWAq2tG_Q-CeXdU_cR6lfPtZuAzj2F9_WB7Vut6nHNZJ1ORXOcYhp3vyGowj0q5XSI9nP-DKa1Zg6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
قرار نیست بی‌نقص باشد، اما حجم عظیمی از نفت در حال عرضه است؛ خیلی زیاد.
همه شگفت‌زده‌اند.
🎙
خبرنگار: آیا مذاکرات با ایران را از سر خواهید گرفت؟
🇺🇸
ترامپ:
شاید زمانی این کار را بکنم، اما در حال حاضر وضعیت بسیار خوب است. با این حال، شاید زمانی این اتفاق بیفتد.
🇺🇸
ترامپ در ادامه:
ایران نمی‌تواند سلاح هسته‌ای داشته باشد. می‌دانید چرا؟ چون از آن استفاده خواهند کرد.
ما اجازه نخواهیم داد که از آن استفاده کنند.
مردم در حال یافتن جایگزین‌هایی برای هرمز هستند. شما این جایگزین‌ها را می‌شناسید: تگزاس، آلاسکا، لوئیزیانا.
مردم برای تأمین نفت به ایالات متحده روی می‌آورند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70294" target="_blank">📅 21:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70293">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f23583ef9.mp4?token=ats3KiBfEyt4hk6Qo3cI8TJxlXWUw11xf2-RzMCMJzJvrhCpsrep7Ejy569dE81pV2oPBMHFWOfG5HraXVKn_38k7QsEFxDWPEvQ_ysbQAAEp_CvvQxgKU2HmRt0QLNaOaF8B0BhTP24yjA2nKXMdPgCzC7zjozYpewB9i1BfKWvhpwL0uSNVoV1wsh7z5gYKQ3T-HQeAbZUFnGVCh2iNcr7hF8yl6iNQffbXA3v1Rer0h9QZ-kquJxgTBjmlLrjb-FFNfp2Iw4fUDroxGAiw7M-PlCBCa8w10eFKZ6rmbdjB67yGJbAZT7mDRVNZgfkLUCBkSgRXTbYn6GBvz9KFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f23583ef9.mp4?token=ats3KiBfEyt4hk6Qo3cI8TJxlXWUw11xf2-RzMCMJzJvrhCpsrep7Ejy569dE81pV2oPBMHFWOfG5HraXVKn_38k7QsEFxDWPEvQ_ysbQAAEp_CvvQxgKU2HmRt0QLNaOaF8B0BhTP24yjA2nKXMdPgCzC7zjozYpewB9i1BfKWvhpwL0uSNVoV1wsh7z5gYKQ3T-HQeAbZUFnGVCh2iNcr7hF8yl6iNQffbXA3v1Rer0h9QZ-kquJxgTBjmlLrjb-FFNfp2Iw4fUDroxGAiw7M-PlCBCa8w10eFKZ6rmbdjB67yGJbAZT7mDRVNZgfkLUCBkSgRXTbYn6GBvz9KFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عبدالملکی، وزیر اسبق کار در دولت سیزدهم:
به عنوان عضو تیم اقتصادی دولت رئیسی می‌گویم گرانی‌ها یک درصد هم به جنگ مربوط نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70293" target="_blank">📅 21:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70292">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0460292f9.mp4?token=Ixqv8cvtCRFJ3JrdW9MHs42FaAMkgMZ0CwwNz_g-8Yt_g3eQm7XojNi_V5kCef2NZnZyF0VgC-yVomYKMriNUeJ54PB-0o-ID0FkzFGtqfU8TrjyQuBzTQmPOYn1rrYc4ysrdmPpK0iNL86LVHgd4h5Dt9V8zQGhJpSbt38dLL5OWkAO2rsKEkOA2AHfetkIwsSyaokMpe4fBz-cQ1gIC_tdbVjqQCpcdI60_x9eXIia6MceK71qem2TcmMv9BoivPgC7AJbY47ldnGklX4aNJgn2HSx4mUQTFx9wRAACKwg0uf0usQ5RcQQdjwgsfZJKkkTLLShgKSa19Ko9Hc_qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0460292f9.mp4?token=Ixqv8cvtCRFJ3JrdW9MHs42FaAMkgMZ0CwwNz_g-8Yt_g3eQm7XojNi_V5kCef2NZnZyF0VgC-yVomYKMriNUeJ54PB-0o-ID0FkzFGtqfU8TrjyQuBzTQmPOYn1rrYc4ysrdmPpK0iNL86LVHgd4h5Dt9V8zQGhJpSbt38dLL5OWkAO2rsKEkOA2AHfetkIwsSyaokMpe4fBz-cQ1gIC_tdbVjqQCpcdI60_x9eXIia6MceK71qem2TcmMv9BoivPgC7AJbY47ldnGklX4aNJgn2HSx4mUQTFx9wRAACKwg0uf0usQ5RcQQdjwgsfZJKkkTLLShgKSa19Ko9Hc_qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بزرگترین هواپیمای برقی جهان برای اولین بار به پرواز درآمد
:
شرکت سوئدی-آمریکایی Heart Aerospace با موفقیت هواپیمای X1، یک هواپیمای تمام برقی با طول بال 32 متر و وزن بیش از 11 تن رو آزمایش کرد.
این پرواز در شهر نیویورک انجام شد، 27 دقیقه طول کشید و به ارتفاع تقریبی 335 متر رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70292" target="_blank">📅 20:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70289">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bZ4-zjZry4qV3FOxFxRdTXRJ7a5fjv9TpQccQ6AD-dD3dV7_pcASvcAuaCLF5TRzYedKK05Kh1TIEcjATyCalEBslLeUruEd3I-oW5gIeOhu2KptaDebJMYYoHrT-v12slBvjJcX0Y2NcUr9Bley04tVOoX76RrFWMaTEbXSUlidTIX-lxfLItkjP0bzQ6qEn_qW-6vaoGF4PpEXImZN1pTQOznRFohLuqW1y0nYpsJ0ADcCrqAJ84TOPr_ajpaEkE58QOW2npOxFqp3KBewWWGaqVlStJwx3WIN2Fet0YtXgY1UmrfGOXHK0M3cZcCY_cbcH4qovuCzdeRY0AwH3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DotXp8ACX-qAfXa3wNpnawTN7lt1CCFwe0vTvEyeZWhxJ6O2VZKUm3SrCkINZsallpb8QMifN8B5-x9L1jQpITMfrGgKrAK1P7M9tb9-_nvwDb3yS7YENo71kXF0i8PiNHV4gcR2ef66Xa1WG5wxVYfmscYMa3iy5TCeAdzDMwwXHAwzxdYcsWmlzUQ1UTuGqHy81XGRLyNkhko-UYcsZIIDIPratJWNfXNQgh1aV55d9DH3EtAUtXmFYBHxspfELYev5KqnK19o2r2oSVrIR3UBMuiLLUco3xWqqaeeDKSM_3DYlUGGR9wetN9xgw2deKNBuxfL-y13rzdoKgKaeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f8537b12e.mp4?token=r7WsS5_UzEOIsMa_K6FOhUleHa-E33JoD8678Mf3br6W8mWQbFQvGK0RGle38y09lXcAGe-Ip-y7eUiz5DRhbkz9PH0R22m5pvv4Mj91KJ-iR4hvlVPpA_IRUKkmUj0bP0vS5Hh8yiVSkn1au94eo9cylHOc--8SKnir0rzC0Xt2Ss23dAlmWCkBnt9siX6Q39DJrFJrfon667lfkEX3AeqnfjToNWvC1L4KmFp0dacz1DUXVIFf4bAT_AccGgqCvbhscdOrWv7R_jYjoe6NMMiLx27uROxR44tx-V7ovn1GOJc-jZ3d9loSPiuA5d75iamCifGLMWEwU5NaJmig2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f8537b12e.mp4?token=r7WsS5_UzEOIsMa_K6FOhUleHa-E33JoD8678Mf3br6W8mWQbFQvGK0RGle38y09lXcAGe-Ip-y7eUiz5DRhbkz9PH0R22m5pvv4Mj91KJ-iR4hvlVPpA_IRUKkmUj0bP0vS5Hh8yiVSkn1au94eo9cylHOc--8SKnir0rzC0Xt2Ss23dAlmWCkBnt9siX6Q39DJrFJrfon667lfkEX3AeqnfjToNWvC1L4KmFp0dacz1DUXVIFf4bAT_AccGgqCvbhscdOrWv7R_jYjoe6NMMiLx27uROxR44tx-V7ovn1GOJc-jZ3d9loSPiuA5d75iamCifGLMWEwU5NaJmig2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ پسر ایرانی برای سوپرایز کردن دوست دخترش، عکس چشاشو رو گردنش تتو کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70289" target="_blank">📅 19:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70288">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/322a5e809d.mp4?token=QL-94FFVSeQ4bAneXTQrRc1Pa1hW6bxZfv3oRkDnS4Wl6y0KJYdHbeDO2fuZVyGIYGRh9fVKbdrhcB6yWGe7VGbEvU3TFmuotlBjysi1Mp-r21_66lK11pOkXBdnsjjgOTGczUvi58w2EPpsPzSfEGM9YnPuzhMT2qmWn2xmNjTeob8KtsS1gb21bxbWEdx2MP5jMXqksSVesgJvoCHiTnsQw4vLxfjZ7ycke1rZu_lg4ijqxlobIweAiXs2oAV-AJYAOtR0UI3Z4okeJymoAX_uC8A89ObTc9hrzJ8UFItQ-Ckw_QzvEI5pyWZd4PwF8tKTmdjd8T7LiArXyTYUGjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/322a5e809d.mp4?token=QL-94FFVSeQ4bAneXTQrRc1Pa1hW6bxZfv3oRkDnS4Wl6y0KJYdHbeDO2fuZVyGIYGRh9fVKbdrhcB6yWGe7VGbEvU3TFmuotlBjysi1Mp-r21_66lK11pOkXBdnsjjgOTGczUvi58w2EPpsPzSfEGM9YnPuzhMT2qmWn2xmNjTeob8KtsS1gb21bxbWEdx2MP5jMXqksSVesgJvoCHiTnsQw4vLxfjZ7ycke1rZu_lg4ijqxlobIweAiXs2oAV-AJYAOtR0UI3Z4okeJymoAX_uC8A89ObTc9hrzJ8UFItQ-Ckw_QzvEI5pyWZd4PwF8tKTmdjd8T7LiArXyTYUGjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ماجرای پیشنهاد قرار گذاشتن از طرف‌ دونالد ترامپ به بازیگر هالیوودی سلماهایک از زبان بازیگر:
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70288" target="_blank">📅 19:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70287">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇷
قالیباف: مقاومت تنها راه پیروزی است و اگر آمادۀ جنگ نباشیم مذاکره هم ثمری نخواهد داشت
؛
از دولت و ملت عراق برای تشییع میلیونی رهبر شهید انقلاب کمال قدردانی را دارم همچنین از میزبانی شایسته ملت و دولت عراق از زائران اربعین حسینی تشکر می‌کنم.
مقصر تمامی مسائل و بحران‌های منطقه آمریکای جنایتکار و دخالت های آنهاست. همچنین غده سرطانی اسرائیل که توسط انگلیس در منطقه ما نهاده شد این خسارت‌ها را به بار آورد.
ملت ایران با مقاومت و وفاداری، با نیروهای نظامی و درایت فرماندهی کل قوا هیمنۀ آمریکا را شکسته و آنها را پشیمان کردند تا جایی که امروز آمریکا که در استیصال به سر می برد، هم با خروج از جنگ دچار بی اعتباری می‌شود و هم با ادامۀ آن ده‌ها مشکل برای خود ایجاد می کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70287" target="_blank">📅 18:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70286">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/680c5f174f.mp4?token=pfxKXjGdAeE9DkiLnaNHapuNQUMzwEmWWgN9rjvtJr7H6tmEnbaLimnX7J54gHc3k9raA2_AIKCw9E4EFy_2NFpVEOFKkGFAf4pQh6mrN5P9cTK6JJ7kABSbcauqBDs0iCd-m2e9jxXAMTIeg80fUV4bVS5YFzyRBhFHiM14oaYDgXzMqAz5bJSLUDPCFyUqE2vOEoEqERY_dw08kDrnUbiEA8SpNCBUrAle8iEiNv8cY4HCHg4ALyTuaefhhNL1Dgj-k8Dj5Lv-B6XyikFtvU6HN2AxYpiN9JffrAcXFS4paFNc9yjdsDJ1qSLKOmQ5Y3H0BRbO30vmbD9Zmi9UAwCUPPLlEOG084qsfTNE5z0jCwS1g9lm_ATeUQMnKyn4OhhefrC7D3X26Zf1iVuBDjBQjez8c3U6N81-thg6f3j_zXLoQip2F3O33TUeUr49dy2RRSkrgZFsll4xJTuNFuLD2yBRE3HrdivThRDu4nbrv4yVW1DtmBpt1GKlX-4S1757aGZFH7q38bDFp4vf7UTstSAyODM4VCxJDUUhtjwnBSahRQ-FL6lr6J8LrStrxUNW7iQl1Bm1cO7WbSayleH1wUtLx9JZRNg7yxxhOlgTbSBYolNEIDoKSEsfkGGeNikAPcep-8TLsqWJA7XHNZDKHmkrNlkM3NEPT1DxbPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/680c5f174f.mp4?token=pfxKXjGdAeE9DkiLnaNHapuNQUMzwEmWWgN9rjvtJr7H6tmEnbaLimnX7J54gHc3k9raA2_AIKCw9E4EFy_2NFpVEOFKkGFAf4pQh6mrN5P9cTK6JJ7kABSbcauqBDs0iCd-m2e9jxXAMTIeg80fUV4bVS5YFzyRBhFHiM14oaYDgXzMqAz5bJSLUDPCFyUqE2vOEoEqERY_dw08kDrnUbiEA8SpNCBUrAle8iEiNv8cY4HCHg4ALyTuaefhhNL1Dgj-k8Dj5Lv-B6XyikFtvU6HN2AxYpiN9JffrAcXFS4paFNc9yjdsDJ1qSLKOmQ5Y3H0BRbO30vmbD9Zmi9UAwCUPPLlEOG084qsfTNE5z0jCwS1g9lm_ATeUQMnKyn4OhhefrC7D3X26Zf1iVuBDjBQjez8c3U6N81-thg6f3j_zXLoQip2F3O33TUeUr49dy2RRSkrgZFsll4xJTuNFuLD2yBRE3HrdivThRDu4nbrv4yVW1DtmBpt1GKlX-4S1757aGZFH7q38bDFp4vf7UTstSAyODM4VCxJDUUhtjwnBSahRQ-FL6lr6J8LrStrxUNW7iQl1Bm1cO7WbSayleH1wUtLx9JZRNg7yxxhOlgTbSBYolNEIDoKSEsfkGGeNikAPcep-8TLsqWJA7XHNZDKHmkrNlkM3NEPT1DxbPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
چگونگی تولید برق با اورانیوم:
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/70286" target="_blank">📅 18:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70285">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">💎
برداشت بدون محدودیت داره حتی ۱۰ میلیارد تومان هم برنده بشی بدون دردسر برداشت میکنی.
✅
🎁
برای مبالغ بالا ۱۰۰۰۰ دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ ۱۰۰۰ دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/70285" target="_blank">📅 18:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70284">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari (3).apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/70284" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر WEPARI
😀
😃
😄
😁
🔥
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 120% اولین واریز
‼️
🔥
بونوس برای 4 واریز اول
‼️
⚽️
بونوس ورزشی هر دوشنبه و چهار شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🔥
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
📌
آموزش نصب برای IOS
g28
✔
https://t.me/WePariFarsi</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/70284" target="_blank">📅 18:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70283">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇱
نفتالی بنت رقیب نتانیاهو:
باید مطمئن بشیم رژیم ایران قبل سقوط هسته ای نباشه
هرچی در اختیار داشته باشیم از جمله بمب برای فروپاشی آیت الله ها استفاده خواهم کرد
شوروی بدون بمباران سقوط کرد آمریکا فشار آورد و اونا سقوط کردن
رژیم ایران از درون پوسیده و به سقوطش سرعت خواهیم داد
حزب الله یعنی ایران حماس یعنی ایران تروریست یعنی ایران
هر بازوی تروریستی ایران اقدامی در خاک اسرائیل انجام بده جوابش در ایرانه
اقدامات موثری انجام خواهم داد
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/70283" target="_blank">📅 18:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70282">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65db328cdd.mp4?token=hMCnU7onHETLSNXweyugVwYom725BEmj_nmZSBTdzm6Xgt7wY6n82WRVWciDzw__e3G6-4e1qKCEjH893ry9n-1c2xICBGv-y4D8Xc9ZC4narn07-K2AKVSy8z6sFcs9MkiSLziRhLjbZIW81QZJ-rfS5SaTZmX29Uc6jhfU8bEz-qkDTBIxALlpzSs3yYGYnU2amumApMbhDBFs_bFQLb19hsCgFABStR4Gi4rBlRipreDu-ty1o1_JPimIc2ENOuMLOtLiqT7HyRFD1CjYB7dCm4krMAh2H25_kCicKze5j5ke7dej8VMomlui3UQe3YQTl3v3ZmH2oYSuyEFbwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65db328cdd.mp4?token=hMCnU7onHETLSNXweyugVwYom725BEmj_nmZSBTdzm6Xgt7wY6n82WRVWciDzw__e3G6-4e1qKCEjH893ry9n-1c2xICBGv-y4D8Xc9ZC4narn07-K2AKVSy8z6sFcs9MkiSLziRhLjbZIW81QZJ-rfS5SaTZmX29Uc6jhfU8bEz-qkDTBIxALlpzSs3yYGYnU2amumApMbhDBFs_bFQLb19hsCgFABStR4Gi4rBlRipreDu-ty1o1_JPimIc2ENOuMLOtLiqT7HyRFD1CjYB7dCm4krMAh2H25_kCicKze5j5ke7dej8VMomlui3UQe3YQTl3v3ZmH2oYSuyEFbwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه نفر می‌خواسته از یه دختر دزدی کنه، وقتی دختره مقاومت کرده این بلا رو سرش آورده.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70282" target="_blank">📅 17:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70280">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/orfusFCfAAf0i2E8GO4Ei_ryJAVSBHcvsVoXHKoKNztXan5VLsjL1JMTSuZeSbGwhYyh7ATPKGlEuAw_lKBkcYMdx6NsxhyRrYul925jSIk1NwZk3RvvdY_2lBPZRil3A9i72QvRRdZ30m3R7zZeKHEewBuQ590kGksmVMLfaqx5BwQwoQJPhlQ8eNmVm-2Y-A9H8LAOptNY2XoCJJa7cj1VaGZEfEGRJiMkYfrhtYrBlRoV_tUsReUOOoxYs57XwdwIV4Gfl6upyfxf003A6jiP_0IJRSytENVw_bjCfeCXIrPV-_TiCY9S4E62v9jPxAKsZBUENfDkri6ZXA3B9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q_hxHauLi723Mp3XzCAZ4SVvNX9odMILdatBC68hFzpRybIsACq3kISC23te3esRxUWj3QhF_Jil2FtGnOvwfEnjBpIIjCBaHqheO_jKj3UZph_dQzO9oO8VwlK12TShe5CJl26Aq3yS18tbxbLMsxcBd8-tlk_ABGrFPjXX0VkqV-NfogOqvhp_pXg2Abc0x54NpmK5ZQKpKHHXpnd2FJ9696mALR_Oarq-kDz2GbT3As_UK0ynyzNJwGAWn4qrniJ3wgjpN7gIuq0GUwvjGeaGMJviahYUpUNSlBCKHgkmrKmWgq_9ZXkTccQ_gdUy4JOc9xWzyK_nGGK08CxloQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
روبرتو کارلوس، اسطوره فوتبال برزیل مسلمان شد و با یه دختر به اسم سهیلا ازدواج کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70280" target="_blank">📅 17:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70279">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0a5de821a.mp4?token=oSX33jrssz31db64Z5B3d7_ecijaKUPGdkILp7WkVlxsKU7C4IhoOsvoF029hS8ziTpvoin_Sdha-Vi6pnMpEoQLgKa3nC86TOmHKu1Pmploi2eTY5l6xlV96veu_B7XHoh30-2BP5iHPP4uB6l0KvMEv56fZd0Yy9C3mu41DtWdVKmQ_vWZfEHXKKAdoOBCsYf0xFODyhJFXOgVf41JbsbAtbAWdoOqCSSUho7ghqOrv93JWcE4AttuKEcwYb-hB5fAMb2jxvRPSSafbnDYdsGPitp3VfKm4vBhecBQ6NSl56T-oD321wRLZj7KNEdzV_CMFLjJXR6yjwd6uwd2ORbAg5RBaOKA82KaMWAlLB08elWhMRaf_lbyyLOPG2qFXFlPJGfA4qhxZUf7k3WVY75ZKSue2xTlV9Aprj2xGU9h47bpsKaPAo6IkUvdHl7kRr_JnsBmYatmImOhGKD83hFa6tF9QDrxBjxYMAAC4kL-qIr-oK3nSdkbG4WiSR4EFJ40T1I8OhnyrRig47JHexrx9IzC1x3kjuES6qsp4-6gkqdyMZojV5G_cRAK0edJWVPi9oMSf6qsSdjzcfBVaLmYyJUrLv9W77PdVyZ_3bVgNA6ApxqCDmxdKlwTAd5rxcNI2TRbzvzjJ-cc152FA-wTJvowLEv1T2D1rThvB1M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0a5de821a.mp4?token=oSX33jrssz31db64Z5B3d7_ecijaKUPGdkILp7WkVlxsKU7C4IhoOsvoF029hS8ziTpvoin_Sdha-Vi6pnMpEoQLgKa3nC86TOmHKu1Pmploi2eTY5l6xlV96veu_B7XHoh30-2BP5iHPP4uB6l0KvMEv56fZd0Yy9C3mu41DtWdVKmQ_vWZfEHXKKAdoOBCsYf0xFODyhJFXOgVf41JbsbAtbAWdoOqCSSUho7ghqOrv93JWcE4AttuKEcwYb-hB5fAMb2jxvRPSSafbnDYdsGPitp3VfKm4vBhecBQ6NSl56T-oD321wRLZj7KNEdzV_CMFLjJXR6yjwd6uwd2ORbAg5RBaOKA82KaMWAlLB08elWhMRaf_lbyyLOPG2qFXFlPJGfA4qhxZUf7k3WVY75ZKSue2xTlV9Aprj2xGU9h47bpsKaPAo6IkUvdHl7kRr_JnsBmYatmImOhGKD83hFa6tF9QDrxBjxYMAAC4kL-qIr-oK3nSdkbG4WiSR4EFJ40T1I8OhnyrRig47JHexrx9IzC1x3kjuES6qsp4-6gkqdyMZojV5G_cRAK0edJWVPi9oMSf6qsSdjzcfBVaLmYyJUrLv9W77PdVyZ_3bVgNA6ApxqCDmxdKlwTAd5rxcNI2TRbzvzjJ-cc152FA-wTJvowLEv1T2D1rThvB1M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو بازار تهران مغازه نیم متری رو 15 میلیارد فروختن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70279" target="_blank">📅 16:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70278">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⏸
نگاهی به تحلیل زنده‌یاد مانوک خدابخشیان درباره نتانیاهو(حدود ۸سال قبل)؛
از استراتژی‌های اطلاعاتی و ضد‌اطلاعاتی تا نفوذ در عمق برنامه هسته‌ای جمهوری اسلامی و دسترسی به اطلاعاتی که قرار بود محرمانه بمانند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70278" target="_blank">📅 16:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70277">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgtGDhWKXG1sEkp3WGxxavjSezesO8YioXPGLfbISm9jWJxIzoR1MZv71krZPXEkzFn5iteFajNmsK8GuCky89zZA6LECCSU2Xld720wqZuGuOrVUjRO5928n9D5xyUmT-ypD7x7c_KFe0bvr5Xpg4UfQtpkg3ApbCKLF434fIDhsG7P7VpMHgkFYIXATzxXLsXsKt_iKTkxfZr0CMJx9ruOvJ7GxuCLjQl_OmC4KgJXfJ4oVPNZShVyCWWgjPiCcPVZilW5Sup1PrejBQEULDS5yNyxxMoSTkVcQlK2lSszp3S9_XYoExji5XMcFi5l-UsYnaZEKt54kZlqV77W4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
یاسر جبرائیلی:
کرمان، عملیات فریب بود.
بنزین: فعلا ۳۰ هزار تومان!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70277" target="_blank">📅 15:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70276">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029120d212.mp4?token=XKOqCluICKhqiU3cVDV8HahYV752BKF5ESgdmybL1eXzfkQZYx6s0s2wPEoyJHwdZc2EQMcTU2jggjkDlDzBg5M569Fczxl7dn7LaGY1tkGIcJcdaH2lPYceMGE8OLfhmTItGB7Kl3bcZ9xbWj7ujrrADn-nFBvV818MI_rQ5QS5gWXocSj29RN9Mwxzs6FVxE7lEB7chWX3vD9IONKJwMOKEgqqx4l2lUXLJMxdO55MkjMsMoVh1YJjm0m7P21M0-PufMqYUVPGwAP3vVEHEv5zb8by5nB_FHLzN2Hf24E_4M_ifJOfW4Qim4hY8RSfhJp5-i5tYKsFPo3sdZ809F2g7GVVAiDqvtNzL0lj0nXHGTRxvuvYd4880YH6QgEgUh6QqyXc69Qe3P0CUfKt3YTnWkARpeJyftJtWP8IcTOeeDBPs34ltTtgtYSfzMptn5GblVHnsBewBe72oqX76SR47su-kVwnxYBigLx8IhseMptF6Vj_Bv04Qrbz7BnhI3nZjSeKxdaZ4-dbt_61J8Xh6W1n6HFgTuoO46HxXMhibwJEyP27PDrP49RF33J7AEE-75SIqtv72eJwh_r9SUHnYOeX9oE7nNEK4HIw2tJkDnik9q3P1Ij7gAXL9G-ScYccUiNWFR9M6UBjl_QqCWB2cZF3u-y0QTCZVXjJkz0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029120d212.mp4?token=XKOqCluICKhqiU3cVDV8HahYV752BKF5ESgdmybL1eXzfkQZYx6s0s2wPEoyJHwdZc2EQMcTU2jggjkDlDzBg5M569Fczxl7dn7LaGY1tkGIcJcdaH2lPYceMGE8OLfhmTItGB7Kl3bcZ9xbWj7ujrrADn-nFBvV818MI_rQ5QS5gWXocSj29RN9Mwxzs6FVxE7lEB7chWX3vD9IONKJwMOKEgqqx4l2lUXLJMxdO55MkjMsMoVh1YJjm0m7P21M0-PufMqYUVPGwAP3vVEHEv5zb8by5nB_FHLzN2Hf24E_4M_ifJOfW4Qim4hY8RSfhJp5-i5tYKsFPo3sdZ809F2g7GVVAiDqvtNzL0lj0nXHGTRxvuvYd4880YH6QgEgUh6QqyXc69Qe3P0CUfKt3YTnWkARpeJyftJtWP8IcTOeeDBPs34ltTtgtYSfzMptn5GblVHnsBewBe72oqX76SR47su-kVwnxYBigLx8IhseMptF6Vj_Bv04Qrbz7BnhI3nZjSeKxdaZ4-dbt_61J8Xh6W1n6HFgTuoO46HxXMhibwJEyP27PDrP49RF33J7AEE-75SIqtv72eJwh_r9SUHnYOeX9oE7nNEK4HIw2tJkDnik9q3P1Ij7gAXL9G-ScYccUiNWFR9M6UBjl_QqCWB2cZF3u-y0QTCZVXjJkz0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند شب پیش تو یکی از محله‌های تهران یکی از هموطنامون یادش میره که آیفون خونشو درست بزاره سرجاش و الان یه محل بخاطر این حواس پرتیش خواب از سرشون پریده:
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70276" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70275">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6a9c2f6f7.mp4?token=CIHdD6jjc2lBiJRZW-w-ZQarzWavP-jPgs_ShGt18HKTH0EfafubY8-b15J-svmE6hA_4ovhePC4cyfb8jkoWszhfcIlRsX3EBqdUKBEw6y9yh61U2y092c_wAUg7kamkl3m5kNPpCMtvILcNkDS1EyuPfshf3kppSajmE38liM_PlpSTHeMB2DRhSeh6X6gtDJnJlGUxFVoRHf9AyjBtXvH60Nbk46-fb_u1j-Gr24W9hQId-HRO2_e7ppGPJemfyrGWorRYLVcJPHRRWlmVq0LUkav7Xhd0z4DcooZg6p-mu6L81TMD_QCOmDSW1kikmSAtQhbmng4FbdUGkZelQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6a9c2f6f7.mp4?token=CIHdD6jjc2lBiJRZW-w-ZQarzWavP-jPgs_ShGt18HKTH0EfafubY8-b15J-svmE6hA_4ovhePC4cyfb8jkoWszhfcIlRsX3EBqdUKBEw6y9yh61U2y092c_wAUg7kamkl3m5kNPpCMtvILcNkDS1EyuPfshf3kppSajmE38liM_PlpSTHeMB2DRhSeh6X6gtDJnJlGUxFVoRHf9AyjBtXvH60Nbk46-fb_u1j-Gr24W9hQId-HRO2_e7ppGPJemfyrGWorRYLVcJPHRRWlmVq0LUkav7Xhd0z4DcooZg6p-mu6L81TMD_QCOmDSW1kikmSAtQhbmng4FbdUGkZelQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
واکنش سرهنگ سعید راستی به ویدیویی که از او در اعتراضات دی‌ماه منتشر شد:
تو جمهوری اسلامی اگه دیدید دارن یکی رو می‌زنن و تخریبش می‌کنن، بدونید اون طرف کارشو درست انجام داده؛
تو 32 سال گذشته کار من فقط مبارزه با ارازل و اوباش بوده و غیر ازاین نبوده.
تو فضای مجازی اومدن با استفاده از هوش مصنوعی یه کلیپ از من ساختن که توش با مردم درگیر هستم؛ در حالی که اون کلیپ اصلاً مربوط به من نیست و سر من رو با سر یه شخص دیگه جابه‌جا کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70275" target="_blank">📅 14:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70271">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uw_g8Ingc-2FJ7SBV4KAGyV_zJGhYlXezAXhPpSewWokMnCMtlylyi-SA083_NzLkWy1FSSSyzL5cMYSVZEB7Cqv51rhtU1CFpLxPTy8KPzjQtG2Aqtra39iKZUV4692z7_CCVXb0jvOeCI5eG0hRxwLy2qE3BVkPNylalZn87oHoTF8ZNh86R-sKih24ekQF_7-RlvVIlyjMBBVZ2yXos4g6biZTQno_Eo9yfJVc2BzD3Do8Lsmt36L1f9KQN06Gpkn9b0wuYncf7LQY9l4DHNZCYAtP2uKBbdkVVX_NxTl_5KIgo5IC06LLa6bAltTn7Kbgb9an7TUc4o1evjJjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ev7dsKLwKCcqv9wFxpbyP53g_y7A30mGsGlF85ZEqJQRqVoHkAQNCNwu-NbnM5XgMDw8aRGCESOPOdyCR5R6jUJWuAVaD1K1ZHYpJDiLGAfqyWUT4ps1OJGdFnkUpYwqXe_ryO-t42-Lqw-6FBffQYVjA0EA6gif81Wibuh6q6jOcZMnDQhuoCXYK7VH_ILRnd07pufK2rbrY_3D63OxTK_8oJ_eYkNZ667IW_RxX4brI3E75UcpCdrsh_KuZ2t_EwIyoXSRpWDT9OK_FbsW8Sq254aQtoG2Ggd1NFmcmz306EH24LcxYnTnBVAmtYhhW-v7mUXCnrsNuzjDYaVRfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc313b331.mp4?token=jpBxeH3PBOdRewc1HqF2YX-t73y42pf3aN_Y7pwAwuQjEqAPCUFL9cbkT8cfE_AFjoMeJmklh6Es1ShJ-nrYNiaurQP2MtHUB2dSrsatSlnnPHb5o0ktXAdrzz1JW8by-MYxYaPVVVVvT2ZukpQJX3ObMG_Xrtx225oW4jp8zUvzHHxaE7o5HkiLnO4QJjZMv6weEQ8lv8EOFLx2JtVf3uj03wgAQTAZUul4nTBd2LXtbYz-oZBjBGP2KboB-_OP9C0sS7v_4R2quu_k5uc-DCzkgFjHlxTecP1Bc3wl3ldYIgcsnjTfPJLE9PUJBzv1ylH44ysEMIpLlydOdsfskg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc313b331.mp4?token=jpBxeH3PBOdRewc1HqF2YX-t73y42pf3aN_Y7pwAwuQjEqAPCUFL9cbkT8cfE_AFjoMeJmklh6Es1ShJ-nrYNiaurQP2MtHUB2dSrsatSlnnPHb5o0ktXAdrzz1JW8by-MYxYaPVVVVvT2ZukpQJX3ObMG_Xrtx225oW4jp8zUvzHHxaE7o5HkiLnO4QJjZMv6weEQ8lv8EOFLx2JtVf3uj03wgAQTAZUul4nTBd2LXtbYz-oZBjBGP2KboB-_OP9C0sS7v_4R2quu_k5uc-DCzkgFjHlxTecP1Bc3wl3ldYIgcsnjTfPJLE9PUJBzv1ylH44ysEMIpLlydOdsfskg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
امروز تولد جاویدنام مهرداد مشتاقی 27ساله‌ از اراک دانشجوی رشته معماری بود.
رتبه 200 کنکور سراسری
مهرداد 19دی تو اعتراضات اراک با گلوله جنگی از ناحیه سر مجروح و به بیمارستان منتقل میشه تو بیمارستان عمل میشه ولی به‌ دلیل مرگ مغزی جونشو از دست میده.
روحش شاد و یادش گرامی
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70271" target="_blank">📅 13:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70270">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kO6z-07wCTeb0CAXqySzTocLU3uzrpTE0BH7yEUcZs3DzGh_-CnKtYU6arhjrVkyXLaELof5FwgEdCAijO4eY0gkgJGdIsVC6ymneyB-Zl-UNdAWJKWDDQ_YaPK9BQqJjZ1H8zXWBr-EemH5p72WVwvuDsYxWLWkPLORxc3B95WUnYWY0OA4Ei6SYGoxTyM-Gbkeae-9UyJ3wDM0n4VGCxUPvQNrBgWf6l2W8oNjcLIKg7KVwHirR1xbHJYvcwoKdtHPQVXJ6jr3HAiZ52lrk7U3bshx0gc1229N95zNasX7OacCmwSuqOxjOI-_Oo1vuc_x9JNf4g33fPdAWI6dVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری جدید رضا علیپور : جنوب لبنان که چیزی نیست تمام دنیا فدای یک وجب از خاک ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70270" target="_blank">📅 13:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70269">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCoX1FeFwLB1bCX1mlS1OONkUagRgaWc7znB03h8UVukZfCyV2NT-YwhCgCzMSDTQ9BiuxUvgi-yglDmCskbJThKhnA9_F5dicwXvHzwjfU3pVK47UzMM7fY322ntZqYVwznxe77S9UwchuOQloUMgTzK3FXgm5dIzVcrxR6PYRqj_E08Xb2VNkry9iVSJlz7SdEh2T4fhL_uaEHWx6SbCp5POM7sZ5UC1y6FeyuT6Nyr1vU6Ze3Zm0YRSjZv0tbrR_Q6mTSEevaHDT8y1QIz4UnS6z9tOdx8yyngLl2JaDLJK1_Ov-WrITU96ALdKzbF4YPrQLCnZZRMX44oKCzHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فایشنال تایمز:
ایران در صورت تشدید جنگ از سوی واشنگتن، حمله به تأسیسات نظامی آمریکا در اروپا را مد نظر دارد.
اهداف احتمالی شامل پایگاه‌هایی در بلغارستان و قبرس و همچنین کابل‌های زیردریایی در تنگه هرمز است.
مقامات ایرانی به‌طور فزاینده‌ای وقوع درگیری مجدد را اجتناب‌ناپذیر می‌دانند و هشدار می‌دهند که حمله به زیرساخت‌های حیاتی ایران می‌تواند دامنه جنگ را به فراتر از خاورمیانه بکشاند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70269" target="_blank">📅 12:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70268">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04bfbcb6f8.mp4?token=bOWNAnIPvnQjMxaUZZGJTOCdLJx_kf5BOHHJDreiTjuedUb7cPrcOJykPs7R2n1bENW5LfoJSC6VRz--RKKwRZIDjokpQS2DwGgQ-Lfa7-2XvCcUrnRNPRcrdaotAWSpzBKsgpOvtE2XAepPRu2oxWng9wxD_UwDeFnGxhEBD0xC7bJ3mYXq9mEHHodahWhtggQGgul6rkD4i6_tUYzeoceJi5GGART03JYyl39uCuCo3r8wV4in2a_olpfmVqxPxFyNoRMktVM2ovMj_uxRoTJjdN3U6BcayVsbEj6tZZ_tE_BRo_LOMJkeo8zqFkDpeJASMknTAFx4f5bUub-_og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04bfbcb6f8.mp4?token=bOWNAnIPvnQjMxaUZZGJTOCdLJx_kf5BOHHJDreiTjuedUb7cPrcOJykPs7R2n1bENW5LfoJSC6VRz--RKKwRZIDjokpQS2DwGgQ-Lfa7-2XvCcUrnRNPRcrdaotAWSpzBKsgpOvtE2XAepPRu2oxWng9wxD_UwDeFnGxhEBD0xC7bJ3mYXq9mEHHodahWhtggQGgul6rkD4i6_tUYzeoceJi5GGART03JYyl39uCuCo3r8wV4in2a_olpfmVqxPxFyNoRMktVM2ovMj_uxRoTJjdN3U6BcayVsbEj6tZZ_tE_BRo_LOMJkeo8zqFkDpeJASMknTAFx4f5bUub-_og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جنسیس مدل 2013 در امارات: ۵۰۰ میلیون تومن
ارزان‌تر از پراید در ایران...
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70268" target="_blank">📅 12:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70267">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/news_hut/70267" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/70267" target="_blank">📅 12:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70266">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcaGJqR_Cw29mcEIkD0aSDDotcSYqeM0vrPvC8PQax-Lx08ZvOrljJNJIDbTFVCM1OAyhtYrXn0Il-2lsfWVdEMfOFp4rNy8PlVXPa-Tw-j0sE05wxuIA-UHmwWKsDGMjwFRw1QA6RN7URVnp96BazIkWgv7VoA7LbLRS6H6aBqoenjAluRNktJR4fgHZignfkfjGVPhA9XnyRONU9LPO9cCPuuehIa1387ReO4xfu95s4swtjhXzs0QvITky03h8hLG69YEbdd2NMd_3WzXYkQczuqByKrRgLDCcgH-xCRPtj_a7BcrOrv5kv6aUpGM1clcBXBIgy73YAkoGiduYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سایت جهانی  و معتبر
#Melbet
🔴
بازی های مهم 27 مرداد
🆗
ثبت نام آسان و سریع کلیک کنید
🆗
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
پخش زنده ی تمام مسابقات
✅
درگاه اختصاصی برای کاربران
👍
پشتیبانی 24 ساعته فارسی
🎟
Promo Code: MELBET90
🇩🇪
دانلود اپلیکیشن MELBET
📱
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r28
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/70266" target="_blank">📅 12:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70264">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/daabc799fd.mp4?token=pmHAINNGB5QVw_i2LoDNGzkXjH7M_zIa0I6FfhXoZHgZky0cNEDFqMV5fcul0dDawf0shfGKbh-ODlzAnNc8LZUZHW62cqsiPa2ZDUusz1Y1C2nFzP-nfmW2sd-iWPpr7y7Jd-bES9RwtI8ObKahI76mtFNutE4iUnTroYTsRkyHHDQVEMBAvzKu5VmoVBAuy7bRMkXXrP2nOcXhZBwe_2VrENSxVpmExrZiFMQIOpVv-mOUHItLtmpXkJILH_KoCKDktLUhxMtNFb4xyXTavr2ZJ1yyswvMaJZ2uXapj0V_M7r1uXW276HWpfANGAsAI6FsfYN-xEzRNxUBYpCWFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/daabc799fd.mp4?token=pmHAINNGB5QVw_i2LoDNGzkXjH7M_zIa0I6FfhXoZHgZky0cNEDFqMV5fcul0dDawf0shfGKbh-ODlzAnNc8LZUZHW62cqsiPa2ZDUusz1Y1C2nFzP-nfmW2sd-iWPpr7y7Jd-bES9RwtI8ObKahI76mtFNutE4iUnTroYTsRkyHHDQVEMBAvzKu5VmoVBAuy7bRMkXXrP2nOcXhZBwe_2VrENSxVpmExrZiFMQIOpVv-mOUHItLtmpXkJILH_KoCKDktLUhxMtNFb4xyXTavr2ZJ1yyswvMaJZ2uXapj0V_M7r1uXW276HWpfANGAsAI6FsfYN-xEzRNxUBYpCWFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی وایرال شده از بازار پروانه تهران:
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70264" target="_blank">📅 12:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70263">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6847afc8b4.mp4?token=Ddz1RCXbJVI-19JqKqtJDFlIDurID940_-hc78ENIHg38d4c7Zj0A1_TO4UzGTR0uC1xtmolpSbmyj4VE8Lc1cWi_UQghFhv42MX6jWBhQBK7nSkJ4iXJCFKZ5lUqV4Bo4G-4nkvhmYshbjp6Esw-YYheoXOTj6VgKtjjfG0XhDCTb1o0Dax1YiqRlwrIQFVOHfxjbXB7pt40dTslR7tpbgoYxtqdVWG3_LUW0Wn0HOE4w2CT_6go85ctSUEAhIyM4dk2RHJIcEopAZMrSA5grwrfoZW37k7ByDO0Sil2eHCLeOzEp05FHgEJgehe5dwgwO-XaXZTK1tguIKaEVNXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6847afc8b4.mp4?token=Ddz1RCXbJVI-19JqKqtJDFlIDurID940_-hc78ENIHg38d4c7Zj0A1_TO4UzGTR0uC1xtmolpSbmyj4VE8Lc1cWi_UQghFhv42MX6jWBhQBK7nSkJ4iXJCFKZ5lUqV4Bo4G-4nkvhmYshbjp6Esw-YYheoXOTj6VgKtjjfG0XhDCTb1o0Dax1YiqRlwrIQFVOHfxjbXB7pt40dTslR7tpbgoYxtqdVWG3_LUW0Wn0HOE4w2CT_6go85ctSUEAhIyM4dk2RHJIcEopAZMrSA5grwrfoZW37k7ByDO0Sil2eHCLeOzEp05FHgEJgehe5dwgwO-XaXZTK1tguIKaEVNXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
محسن‌ رضایی:
محاصره دریایی ادامه پیدا کند از NPT خارج می‌شویم.
خودتان میدانید این یعنی چه!
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70263" target="_blank">📅 11:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70260">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eee9c1ee83.mp4?token=jtHBX1A3kizpl6vsO8QAPKSzxAoK7RudrBj2AWMrjPp0Vwqtmr2urYrGkHjAj-nwOSQW98EbWiMp-4mlg25ZqKbDvhqZ33E5lapadw7PZrUqfQM_f7vwSw_vxEZbe94fuQumAAm6x-lD4p22G_RdSDcXbFn2IJMJhbuL9-CKlKCgvc003_CM59gv6N695lQ9x-zECdaHORz8jhQaI4UiEDb7TBoDLrmwn-tPRqMVOaBALnmkAeO8dAw8tImrN9J5T2AkCeFDjHbcIO_7bUOn_p-C08Gi-ZX4DNNqvlzF94O2MngKSwxIIUc0oTTixPCmg7qB6SbLEQfDorDUOhQ7fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eee9c1ee83.mp4?token=jtHBX1A3kizpl6vsO8QAPKSzxAoK7RudrBj2AWMrjPp0Vwqtmr2urYrGkHjAj-nwOSQW98EbWiMp-4mlg25ZqKbDvhqZ33E5lapadw7PZrUqfQM_f7vwSw_vxEZbe94fuQumAAm6x-lD4p22G_RdSDcXbFn2IJMJhbuL9-CKlKCgvc003_CM59gv6N695lQ9x-zECdaHORz8jhQaI4UiEDb7TBoDLrmwn-tPRqMVOaBALnmkAeO8dAw8tImrN9J5T2AkCeFDjHbcIO_7bUOn_p-C08Gi-ZX4DNNqvlzF94O2MngKSwxIIUc0oTTixPCmg7qB6SbLEQfDorDUOhQ7fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
جدیداً تو روسیه گزارش‌هایی منتشر شده که بعضی از دخترها به‌صورت گروهی دنبال پسرها می‌افتن تا حتی برای یک شب هم که شده باهاشون وارد رابطه بشن!
گفته میشه؛ بیشتر این دخترها از قشر مرفه جامعه‌ان و اگه از پسری خوششون بیاد، حتی ممکنه چندنفری با یک پسر وارد رابطه بشن!
تا الان چند مورد آزار و سوءاستفاده جنسی از مردان توسط زنان هم به پلیس روسیه گزارش شده.
ظاهراً پسرهای بااصالت روس و همین‌طور خارجی‌ها، مخصوصاً آسیایی‌ها، بین بعضی از زنان ثروتمند روس طرفدار زیادی دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70260" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70259">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c416662f.mp4?token=nhHJjl4TmfwucAAO-kBIbWmax75M-GgoE2xlEGeWIA_tGpa-XdAEk7CSVQMFGq4psa1gxEawIHJLeOvE1aE20H6Wy9vgCB0AP5WAwX8bsjqrOBB46u0lGRm3EowLR8o4U2Yun8oU1xHTy95P7lxRkNil3XMsg82lR725IDzA-Q1pisVMZkX_jgoMQx4GuN7ekkhC9e8dxERHgzRZ52QYmIeYzIHbQUxJZnP1BPXnqzvFhikQ4lZPMNZnipYG4uUilQwNzYuBRMbXLlsuL4bdyATC3ElzIDVMYWqseY6vnBMQ_xfywVra4qfX78WS557BZz2RlYjvmO8tSMZFVXyv3gBxySIl97Krc9pNaWCwrc3cwsO8s3apMXx_cCokPDYw7psIXDWezThTBicXnljxEQFU8LYmoqL08e0_5j1M8_dNgl8r_dU34cZ9l9INddUbMRbGoJBI_GCVXw1e26HNxKwZwPMr3np04UhLTjyGik3oZkhE-IsQHevgyF54-6Jr5OSbplUMr7uMxV3WcOrvyiSiOoKn7ju-1quElAL2mvNtyZa_5AoV-cez0ss0XE23WrDlk6mBq9QLh2xBN0K44rxQpjsG5rQHCK4MPjlIEaMJPAj6vnLbudLfJn58iESXSFkfynJ2uQiLaEjag8lGAqapFvC8Tjq9IlyXc-70cR8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c416662f.mp4?token=nhHJjl4TmfwucAAO-kBIbWmax75M-GgoE2xlEGeWIA_tGpa-XdAEk7CSVQMFGq4psa1gxEawIHJLeOvE1aE20H6Wy9vgCB0AP5WAwX8bsjqrOBB46u0lGRm3EowLR8o4U2Yun8oU1xHTy95P7lxRkNil3XMsg82lR725IDzA-Q1pisVMZkX_jgoMQx4GuN7ekkhC9e8dxERHgzRZ52QYmIeYzIHbQUxJZnP1BPXnqzvFhikQ4lZPMNZnipYG4uUilQwNzYuBRMbXLlsuL4bdyATC3ElzIDVMYWqseY6vnBMQ_xfywVra4qfX78WS557BZz2RlYjvmO8tSMZFVXyv3gBxySIl97Krc9pNaWCwrc3cwsO8s3apMXx_cCokPDYw7psIXDWezThTBicXnljxEQFU8LYmoqL08e0_5j1M8_dNgl8r_dU34cZ9l9INddUbMRbGoJBI_GCVXw1e26HNxKwZwPMr3np04UhLTjyGik3oZkhE-IsQHevgyF54-6Jr5OSbplUMr7uMxV3WcOrvyiSiOoKn7ju-1quElAL2mvNtyZa_5AoV-cez0ss0XE23WrDlk6mBq9QLh2xBN0K44rxQpjsG5rQHCK4MPjlIEaMJPAj6vnLbudLfJn58iESXSFkfynJ2uQiLaEjag8lGAqapFvC8Tjq9IlyXc-70cR8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
ویدیو وایرال شده از کسی که کره‌خر خونگی داره!
به گفته صاحابش این خر گرون ترین پنیر رو میخوره که کیلویی 100 میلیون تومنه!
حتی برای خرش موزیک میزاره
خرش رو هم مث بچه ها پوشک میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70259" target="_blank">📅 10:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70258">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⚠️
امام جمعه حاجی آباد بندرعباس به خاطر افشاگری علیه مسئولین شهر به دادگاه کشیده شده و اون رو مجبور به عذرخواهی کردن
حالا اومده عذرخواهی کرده
این نوع عذرخواهی جالبه:
من از بانک های رباخوار و از قاضی ظالم  مسولین بی کفایت عذرخواهی می کنم
من از روحانیون ساکت که منفعت خود را مصلحت اسلام می دانند عذر می خواهم
ما گوسفندان از گرگ های درنده عذر می خواهیم اگر گوشتی به تن نداریم
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70258" target="_blank">📅 09:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70257">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbcd685b37.mp4?token=gYaacj8Tu_JerIt4mqP03-l16TIFN1LqoBu5d7QTW5wXelixobCSQzX2SEhtXE8ZPBxSxyjxlmxJz83W3tTXYnjQoA5ZTYI6rJ0WK0zmR7pK-xB3JdtDtEPCXCMpll9LCx-FJ-Fed3HcS-ZU_ivUehZRC02SmeaN1hDAGSzEBqAiDcVgLZxe3-9INyqkbx6IuyQdj91hgYIrY3JFMkCayVbZX2qWCP7jnlAtBanNeltcemaM81XYSL1Yhi0hq3lXiXVNst_AH8cxkRAHjQtICFV3oSTENEK923pzFFYRtIgqW0On2XOzIkiFGM_Z9Z_Jf9uff3ruza9ysVB0k87EWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbcd685b37.mp4?token=gYaacj8Tu_JerIt4mqP03-l16TIFN1LqoBu5d7QTW5wXelixobCSQzX2SEhtXE8ZPBxSxyjxlmxJz83W3tTXYnjQoA5ZTYI6rJ0WK0zmR7pK-xB3JdtDtEPCXCMpll9LCx-FJ-Fed3HcS-ZU_ivUehZRC02SmeaN1hDAGSzEBqAiDcVgLZxe3-9INyqkbx6IuyQdj91hgYIrY3JFMkCayVbZX2qWCP7jnlAtBanNeltcemaM81XYSL1Yhi0hq3lXiXVNst_AH8cxkRAHjQtICFV3oSTENEK923pzFFYRtIgqW0On2XOzIkiFGM_Z9Z_Jf9uff3ruza9ysVB0k87EWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی :
رابطه ما تو این دوره با کردستان عراق و جمهوری آذربایجان خیلی خوب شده؛
می‌دونید چرا؟ چون پزشکیان هم ترکی بلده هم کردی، زنگ میزنه با زبون خودشون باهاشون چاق سلامتی میکنه، اونا هم خیلی خوششون میاد!
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70257" target="_blank">📅 09:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70256">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f6a81c93a.mp4?token=qRjNu4-zcY3dHfRKa5SPkHmms7cHnGAQnCa1iFckiOrvtmItVx7hXMqg1WUt8X7J24-sbQrc-1r0vmvH9T29nFQ1Q2ai-RM6gvGT34Fb5gG4qSx6GOkGoHuUilIec53BAEBFybiMVQf5hyb5YGTO82Xh50CUZiUqllIo0Ns0R6YtNDL4U1XI9oHRSqmobMD-1jx2MUBtHL51mc0MHCcSQna8TJ9NlZT2NJqgHfZf9AyTuIzLXMLMIDYew3UA3TwfZEsdcg8modtR1H6CTeuYBIwJgycTvwHCEBVe6imPzRKZDKncPkdn_j5xWuszqehz5iffTYbiuMsnOnVmsmbMLg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f6a81c93a.mp4?token=qRjNu4-zcY3dHfRKa5SPkHmms7cHnGAQnCa1iFckiOrvtmItVx7hXMqg1WUt8X7J24-sbQrc-1r0vmvH9T29nFQ1Q2ai-RM6gvGT34Fb5gG4qSx6GOkGoHuUilIec53BAEBFybiMVQf5hyb5YGTO82Xh50CUZiUqllIo0Ns0R6YtNDL4U1XI9oHRSqmobMD-1jx2MUBtHL51mc0MHCcSQna8TJ9NlZT2NJqgHfZf9AyTuIzLXMLMIDYew3UA3TwfZEsdcg8modtR1H6CTeuYBIwJgycTvwHCEBVe6imPzRKZDKncPkdn_j5xWuszqehz5iffTYbiuMsnOnVmsmbMLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دیشب میدان شهرداری گرگان در آتش سوخت و صدها نفر کسب و کارشون آتیش گرفت و نابود شد!
حالا دلیل اینکه آتش نشانی دیر رسید به محل چی بود؟ بخاطر موکب‌ها و تجمعات شبانه تو ترافیک گیر کردن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70256" target="_blank">📅 09:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70255">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⚽️
فوتبال فقط ۹۰ دقیقه دویدن توی زمین نیست!  پشت هر گل، یک تفکر تاکتیکی و پشت هر باخت، یک اشتباه پنهان وجود داره!  اگه تو هم عاشق فوتبالی و دوست داری مسابقات رو مثل یک کارشناس حرفه‌ای ببینی، جای تو اینجاست!
👇
🔥
در کانال ما چه خبره؟
✅
تحلیل موشکافانه و تاکتیکی…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70255" target="_blank">📅 02:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70254">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=sdIkKBuWmTWlG0QcUbDkRKPYssWiJ1BCFzmwI8DkG1uuQ31VabmwtKNfsQHGS-SeymcXVj4erM5lJjxWI0YOQVjyJoijmFinNCw9nnTHg-W12oWu71m57pucXW2uvN1Q_zpP9aNKpKkU7h0qQtpZdNeLo-s61Ig0ZYVfy9Qzl7LCoIUC-iACJPkLNQYw2JED7YqlLIscVlwDo8g0lzYHM-6y4u3lD66GQxUOrzN03qh9SiqoqWGqclz8quJfnPrlC2nd-eLSJ7RImZRf8Jn8MW1E3IDBlxrefHRjxo3wfhlfKTmFiP6SQxyxF6JtZgTwWk9_QNtKNhlBiCp9x1CDrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=sdIkKBuWmTWlG0QcUbDkRKPYssWiJ1BCFzmwI8DkG1uuQ31VabmwtKNfsQHGS-SeymcXVj4erM5lJjxWI0YOQVjyJoijmFinNCw9nnTHg-W12oWu71m57pucXW2uvN1Q_zpP9aNKpKkU7h0qQtpZdNeLo-s61Ig0ZYVfy9Qzl7LCoIUC-iACJPkLNQYw2JED7YqlLIscVlwDo8g0lzYHM-6y4u3lD66GQxUOrzN03qh9SiqoqWGqclz8quJfnPrlC2nd-eLSJ7RImZRf8Jn8MW1E3IDBlxrefHRjxo3wfhlfKTmFiP6SQxyxF6JtZgTwWk9_QNtKNhlBiCp9x1CDrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
فوتبال فقط ۹۰ دقیقه دویدن توی زمین نیست!
پشت هر گل، یک تفکر تاکتیکی و پشت هر باخت، یک اشتباه پنهان وجود داره!
اگه تو هم عاشق فوتبالی و دوست داری مسابقات رو مثل یک کارشناس حرفه‌ای ببینی، جای تو اینجاست!
👇
🔥
در کانال ما چه خبره؟
✅
تحلیل موشکافانه و تاکتیکی بازی‌های مهم ایران و اروپا
✅
بررسی ترکیب تیم‌ها قبل از شروع مسابقه
✅
پوشش حواشی داغ و اخبار نقل و انتقالات
✅
پیش‌بینی‌ها و فکت‌های جذاب فوتبالی که هیچ‌جا نخوندی!
دیگه فقط بیننده نباش، فوتبال رو عمیق‌تر بفهم!
👁‍🗨
👇
عضویت در کانال:
https://t.me/+nbm7Tb2pz8VjMDlk
https://t.me/+nbm7Tb2pz8VjMDlk</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70254" target="_blank">📅 02:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70253">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCQW-ugEiXm_moGA_-uLyBBOJo2VYFk4fy4zquX6FjuHgTMfKaXtxm5gIx-9DF7Ej-Tu9s00SxyxveZHL6dBgIs2IS7Rnh2qM1BURPyInVSdjbQmu1IIcI_hH1GyA30sBGslaAGqFM5Rd1vQzBFhqmBL7kLnLNFIHMlSsWNOWfaRZPsmmKzXV-x42GvqLZlGoCglUJsxxEQqcXk-W5Rc-VvEE5AXZ89nvcpb31rIgJr34YUSHYRBjJ5LICq3N08tmXpnRPecXNsOGtccDj1bmRKx9rjjKBHuQBqfcAPwTR75IH2hfWPe0Efb1ELj4LtvztAA_IBzdydNuS-xNDv4uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه خواهر جاوید نام امیرکیادربندسری به خاطر سوگ از دست دادن برادرش نتونست دووم بیاره و دیشب سکته کرد.
روحشان شاد و یادشان گرامی
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70253" target="_blank">📅 01:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70252">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lr_A0iJqxszxYvUB68nu2q7n9dRFYvxLvApOSg2Jc62XtpMgidmif31pQyu2fAMZlkw7V7EFbn5AY_ewXEVNhEox7Kp_WrJCYbDuJOiOUgLb391L73EwIJWnw96AYS55QDy6w5THOG_u5JMV3YzOnDNpaTfHzKOEv14j0CtsKH13FFWw5QWgUWBsa2hzH1zQYduNzADR9ZBgJkk93n8ahC7vfYKBZ2D6Zys5axA2wYqETLNE0E30c4aBJwpwS4pamg50sko95eeSQUsF32w6IWwPMS4O7Q5nEhSjR-DHz28Ke78u0Sv60BgCOdEUFWplfKheRrij6oPaK8cZv4lTSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇺🇸
سی‌ان‌ان:
دونالد ترامپ به فرستادگان ارشد خود دستور داده است تا مذاکرات با ایران را متوقف کنند؛ اقدامی که نشان‌دهنده تغییری عمده در راهبرد دولت او در قبال تهران است.
بر این اساس، کاخ سفید دیگر به دنبال «ضربه زدن فوری و شدید به ایران» نیست، بلکه قصد دارد با اعمال فشار مداوم اقتصادی و نظامی، رویکردی بلندمدت را برای «خفه کردن» این کشور در پیش گیرد تا زمانی که ایران شرایط ترامپ را بپذیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/70252" target="_blank">📅 00:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70250">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6093565f3b.mp4?token=IWtCPQHcKtuODwHJ7yE_Gopk8ooYImZjSFjDZLpRZGOurrkbd3WE5J_TV-tuPFGD3roDfpphHPwKWXj3z3rWTXpGOXX-KW8juzQ0ZdtZhDYPFOQFUNALmbzWkWApAsr8B4HfKT06bwN8XMl42gvCko7t9qss1OpmWvB0F9bnETXEMB0Qbs2rUw5HXKKC8XgvT0JTiUZJDZau8yMF1eOo8Md9nlpZlUseT_CmOr6glggTgOtxpEAAFpdgGk-MJ1lk335LiGaNs42XXB-dMvQ3UTS70EluoLqGhwofh_CSnflNH07IMY7bZZc1aLH6hPXuRmtrG1qAdm-IbG-WkGlJ7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6093565f3b.mp4?token=IWtCPQHcKtuODwHJ7yE_Gopk8ooYImZjSFjDZLpRZGOurrkbd3WE5J_TV-tuPFGD3roDfpphHPwKWXj3z3rWTXpGOXX-KW8juzQ0ZdtZhDYPFOQFUNALmbzWkWApAsr8B4HfKT06bwN8XMl42gvCko7t9qss1OpmWvB0F9bnETXEMB0Qbs2rUw5HXKKC8XgvT0JTiUZJDZau8yMF1eOo8Md9nlpZlUseT_CmOr6glggTgOtxpEAAFpdgGk-MJ1lk335LiGaNs42XXB-dMvQ3UTS70EluoLqGhwofh_CSnflNH07IMY7bZZc1aLH6hPXuRmtrG1qAdm-IbG-WkGlJ7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل اسکادران ۱۹۰ بالگردهای آپاچی خود را به‌طور دائم از پایگاه هوایی «رامون» در صحرای نگو به پایگاه «رمات دیوید» در نزدیکی حیفا منتقل کرد و بدین ترتیب حدود ۱۵ فروند بالگرد AH-64A را به شمال انتقال داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/70250" target="_blank">📅 23:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70249">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28b668f3c8.mp4?token=bWoGJ57w-931Aq0qAJjugJMWyelmb_a2cieunAw_7CpgPM2cG5nhuoc-Iz_yWPioegzIg1qXfS5LTUOUW6HSwD_fj-ZfE7HAGQTfDBLdM0sbZDShv_0a62IhsI0t4oz9vzXWP_ylwmGE7uzKjc6uBHJzMWs-7VnJ5VVOrYb20ylC9Vj3qefH8fG1b7oIErTx4-G3I2S4gBDVwZWuLXKp5szLPyGcNbU5aJebErF67f33bez4dYfW2fhbTkNKVBNLCHiu7EfqRK8n9ltaSJOYR-dvCxalwFRHkZ8NfdnX6IvOyeqOyQttsg0n_xcFPmpH4FyGKCba-VjvBg9DBcXm1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28b668f3c8.mp4?token=bWoGJ57w-931Aq0qAJjugJMWyelmb_a2cieunAw_7CpgPM2cG5nhuoc-Iz_yWPioegzIg1qXfS5LTUOUW6HSwD_fj-ZfE7HAGQTfDBLdM0sbZDShv_0a62IhsI0t4oz9vzXWP_ylwmGE7uzKjc6uBHJzMWs-7VnJ5VVOrYb20ylC9Vj3qefH8fG1b7oIErTx4-G3I2S4gBDVwZWuLXKp5szLPyGcNbU5aJebErF67f33bez4dYfW2fhbTkNKVBNLCHiu7EfqRK8n9ltaSJOYR-dvCxalwFRHkZ8NfdnX6IvOyeqOyQttsg0n_xcFPmpH4FyGKCba-VjvBg9DBcXm1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طرف با قلیون رفته وسط دریا با یه دست داره شنا میکنه و قلیون میکشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/70249" target="_blank">📅 23:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70248">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTUfjqdyV4Xt11z4zl97RsJx7ehCES6NOEay9d-fA9iWw7IgTNFumGhYMjx9tgIacyKogRRPGLKSDvTZdl6RCcdv_A909Gfq16NFmmap0VYgSPgDTSodvbxOV0qfMU2lZJUyAtVWM2HWW8l8ga_827xhAEc-8LXuBBzpmZHmY-Yvpere5RCrc_H_sXL9sbeDvaLtjtlQYioMajHN2azuJmS5oXGayTawe6_IHhNjbu_0c4FwwdTcXZqjvk_XTJmtRdqGetAzwyPx7aHXaa98GzeXMxucxebSY92qG_47WWx2z-7M7z_MWnSy3VwJ0Ol2BDSy1YX-O-Y-30vHx9ciGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی:
شکاف میان ناتوانی آمریکا در بازگشایی تنگه هرمز و ادعای مالکیت آن بر این تنگه، از فاصله ۷ هزار مایلی میان واشنگتن و خودِ تنگه نیز بیشتر است.
به نظمِ پساآمریکایی در خلیج فارس خوش‌آمدید.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/70248" target="_blank">📅 22:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70247">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8ogJFOB0QS-IyFxTACtNt1jA6zOpi1CPRVTL26U9QGWsBZaM0XUh6hh6Gd7VhglpAIBFL7Xn2-iG94cTt8jDkrJS-DhsxI2kBffgEdMln5o8vEZ0Ti_0r5BJdxYuykB3BoBuo0S2KvJ49ky_K3ugw83FzbUZHoadp7-5LuZjTNzNZwQc6DyHun_SXqFqX3o92NzoLB65hI0aoROBv0fI_2vpLNpSjzQUfzQhojuGTWUbJJnIva6hi5hlcsZChij98HQCAVuU9tnyc2_PeCHWI5tC4feuPbp9RbYeXz2Gs6Nk2xzH8BgsZms8j8pw3GUmMExJ4AZslAJ8gxDZ18CfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نرخ های جدید کارمزد خدمات بانکی در سال ۱۴۰۵:
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70247" target="_blank">📅 21:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70246">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C72gwD6f-zwu16VkjGGophfDm4cZhQRXoYa2fTh1t9umJ0cEg-v-xFniJsN_EBRjvvcg10u67WrFJY57xqt9h9UJQqX5V22dEF9G9l3A4yNp_hXd7Cx2uoSsAXlGzjvGmujBEXs8M0go3ifZvjzgVjNYevlzbdxT-j95OaT5jelV8I57QDJK5MBQLFHtFzqfQgWr_Inhr1Ibw3HUCD6_oPI2_PshAXWg8YfmkykQrOfRmvKzC56jyK8pLNk1r6bc4Pb3-dnWYVbqpmnMOEsWdxN01aPxfz7LX2rYlx_y5L5X7bXGfNHarUiTf2a_cqWekG8igzocqqxYevfmCQAOTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
آمریکایی‌ها تصور می‌کنند که با اعمال فشار شدیدتر بر ایران، می‌توانند امتیازاتی به دست آورند که هرگز بخشی از توافق نبوده‌اند.
بِسِنت و هگسِت اصلاً در حد و اندازه‌ی این کار نیستند.
دیگر منتظر نباشید که این گروهِ دلقک‌مآب خرگوشی از کلاهشان بیرون بیاورند و گندی را که خودتان زده‌اید، جمع‌وجور کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70246" target="_blank">📅 21:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70245">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df1fa3ba9c.mp4?token=tzvSCDh-ePC0sNIcEi18IGOpDV_KPMx7zOmEQND8bnGMAbSUwZ3JuQ1uBe2q6A_2Kk3zUyzm1A0jP06yIt1Bj-7fagzBHIBcFNU0SgY-lML9JkWiBhACSmIqXGNUn-ZGqXcTOV8n8D1U7mxSgUVDMBMCqnm-FQgm-TXOPplRZHe-hyKmeQePOATC90lyMuhRBdRe06ya4DezKAaiUBMc5AU8JOEUATvMW3zcWD-VbsWldodawQclZM_3Gok_LaUnXqPQurKPrI9p0xbqpUmq4FJHdeh9EbKOSzZrkxZJfWOMvoYBg7gg0BHHfptMg0HK68mWO8G3nwEKelQI8ZwQEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df1fa3ba9c.mp4?token=tzvSCDh-ePC0sNIcEi18IGOpDV_KPMx7zOmEQND8bnGMAbSUwZ3JuQ1uBe2q6A_2Kk3zUyzm1A0jP06yIt1Bj-7fagzBHIBcFNU0SgY-lML9JkWiBhACSmIqXGNUn-ZGqXcTOV8n8D1U7mxSgUVDMBMCqnm-FQgm-TXOPplRZHe-hyKmeQePOATC90lyMuhRBdRe06ya4DezKAaiUBMc5AU8JOEUATvMW3zcWD-VbsWldodawQclZM_3Gok_LaUnXqPQurKPrI9p0xbqpUmq4FJHdeh9EbKOSzZrkxZJfWOMvoYBg7gg0BHHfptMg0HK68mWO8G3nwEKelQI8ZwQEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخشی از مصاحبه اختصاصی دیوید فراست، با محمدرضا شاه پهلوی در سال1978
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70245" target="_blank">📅 20:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70244">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxHQnEZQ9xacjN6q7Q8ok4V4qJoV33D2wBn6VCnUCJFh1jZeAaPsLlibTvNQ7w4_rAE60lUF5dF-V-XDZUxVEt_pyTVt2wtqwW2hg8IDw-VLP3YeXxyV_hCBhKG3xvHDHm-GgJ2WpoDU8YXwwIg5QNc_YMvhlWtHfLGbO7YwhVg1oAXnMXh3J64E3gDRIxNVdJ0vjxTaLLUFiWCIXssO-PegWrH9CFqPJWfrUHDW0cmb11hk-l02SjFL7mYgcUv3q4ARpz26bUqBJ2jj7v71dW-z_q3Hil9ahnYqn3Cwq4KwZ04HTiemFxtx6c4zgVbPRdTkL70qyy2XZ9zZMWCsjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فعال شدن آلارم موشکی در امارات  @News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70244" target="_blank">📅 20:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70243">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNxDkY1QYgBgPOmvIzPutXx2Ve8Jy17cmksZcu0GePdNyQ8sYsIcBwSasH-OoAUVAMX5EA_0cpl5qIdHdx3YSBDvkorVGbp0XN0GwWV77Umojue-yONlucHy4jitdXFm9Bmozt1CPElBeSk34YbdPDVidhyKEO9FSXUryH3u-YAaBDFJoEcadk2sEISPaaTROqiaPBWHN3zpp0huIcDCDeGLc6It2yAVJVlosAfPzf4QDsaClb-ZtvtVRKUagD3UMQVydO9M6fvAuWeeNBE4A1sKvKlag-ZNthTPmw01SWVOBqgBCMi6QUOClBHEJVWim0zshUl-MPr7KJDvSD72PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مهلت ۶۰ روزه تمام شد؛ ایران و آمریکا در برزخ جنگ و توافق:
خبرنگار الجزیره می‌گوید مهلت ۶۰ روزه تفاهم‌نامه ایران و آمریکا به پایان رسیده، اما نه مذاکرات واقعی به نتیجه رسیده و نه جنگ تمام‌عیار از سر گرفته شده است؛ در این مدت، پیام‌ها و درگیری‌های محدود ادامه داشته‌اند.
به گفته مقام‌های ایرانی، این مهلت صرفاً برای مذاکرات توافق نهایی بوده و به معنای آتش‌بس یا پایان جنگ در همه جبهه‌ها، از جمله لبنان، نبوده است.
هم‌زمان، ترامپ از تمدید این مهلت سخن نمی‌گوید و مواضع تندی علیه ایران مطرح کرده؛ وضعیتی که به نوشته خبرنگار الجزیره، چشم‌انداز رسیدن دو طرف به توافق را مبهم‌تر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70243" target="_blank">📅 19:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70242">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2983ea6f26.mp4?token=tGJqA_t5WzTIfIM32IhEsS9MmNLowD3nTvEnr3ZHtA5HWwq8eIJOCG-U9MlG3w92J72XeK_RSIdkjeR9_L_cmo-yj686Y4vXBgMgbVrYZWcV_zvopnLBR-XfyYkegs-xMux_2YbRwenXIO-YvJBHNTKirwlOQGy03BI03Rz5rnc_PKDPMfLuSYHTaDaIHct9BQC6gCuuwRjsY9upZ0pCbBuZWemVphJCLupQ2BHcLJyIqi9f6il5OH7HFFMgS5rIwRoK2ggkFfkeZk-OV0dOfv7TrNYID9wcWEbTaXBEkeCoV5a-p2BL_SFYRzaa9ZMjDGtfVcpZ0yHc6GrO1n1NGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2983ea6f26.mp4?token=tGJqA_t5WzTIfIM32IhEsS9MmNLowD3nTvEnr3ZHtA5HWwq8eIJOCG-U9MlG3w92J72XeK_RSIdkjeR9_L_cmo-yj686Y4vXBgMgbVrYZWcV_zvopnLBR-XfyYkegs-xMux_2YbRwenXIO-YvJBHNTKirwlOQGy03BI03Rz5rnc_PKDPMfLuSYHTaDaIHct9BQC6gCuuwRjsY9upZ0pCbBuZWemVphJCLupQ2BHcLJyIqi9f6il5OH7HFFMgS5rIwRoK2ggkFfkeZk-OV0dOfv7TrNYID9wcWEbTaXBEkeCoV5a-p2BL_SFYRzaa9ZMjDGtfVcpZ0yHc6GrO1n1NGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇩🇪
اولین جنگنده F-35A آلمان مراحل مونتاژ نهایی را پشت سر گذاشته و در تأسیسات «لاکهید مارتین» در «فورت‌ورث»، وارد مرحله تکمیل نهایی شامل رنگ‌آمیزی و اعمال پوشش رادارگریز شده است.
مراسم رونمایی برای ۱۸ سپتامبر برنامه‌ریزی شده و انتظار می‌رود نخستین پرواز آن در اواخر سال ۲۰۲۶ انجام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70242" target="_blank">📅 19:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70241">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/news_hut/70241" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70241" target="_blank">📅 19:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70240">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqYlShgYhaWl1bjoXjLLogSFTEXbmOvHuEY3J-vEI3huewF1txKEp9VxEu5Bw2ELcSfrKrJ52THvlf_WSddXlnzTlOwoanuqbq6H-hfEjoFzmlRLLaMqHi6BhkcY_owRnODH8U_mq4f7crXXw3rZ6vmHmAD2IFUl04_dtQMd7EbilVlrVOEphuBxzV3XvPmb06MoAm8uOkKU5zm04jPX6S-Xpa80dQAuaR05XVXgHsIEq99q2JZ1GM8sBqoPRGTT-ljNg2VnkKnV2GwIMjTR1eHRjEMLvy_bmWGlAyyn2FsrZ88aWN3O_79Mvmgm2o02fSDADk88-6x1FNM8wbmfJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سایت جهانی  و معتبر
#Melbet
🔴
بازی های مهم 27 مرداد
🆗
ثبت نام آسان و سریع کلیک کنید
🆗
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
پخش زنده ی تمام مسابقات
✅
درگاه اختصاصی برای کاربران
👍
پشتیبانی 24 ساعته فارسی
🎟
Promo Code: MELBET90
🇩🇪
دانلود اپلیکیشن MELBET
📱
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
g27
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70240" target="_blank">📅 19:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70239">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9tg3qwxr3mUZB73UwlKqSYr3XXDCXrn4Ui35BoVAcwoSDatXwB5wD7IGgPvGU6oA7DWsplV9ywz1m_GjFCoFgehs2BaU8Ud-icxhxHhjFb9YcHws5J7yt1zvJYz9EK--m8GywCZgTAu2Jn7g0z0wlwcHihPo8JD8p_luptF9FWlKIGnGBpEexGOLJG0SwxQUWA3W8RBkFOEXo3udA2pu4yiuERvWc3i8XO7RNqfqynsj1W4W1qPHZIkA5YqtVEJ6MBvFCPR74h5x4bOkMKiPo5eM73DkfkbfPIiVSbp45uBx_EBM4JZDGh_S3jMIvOgQ0QUd-8T_oJBXjq6KicvpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فعال شدن آلارم موشکی در امارات
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70239" target="_blank">📅 19:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70238">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2f073a154.mp4?token=lortKJ8LFsQidBdl-l9CqjRy2e8sqUlxsaKO7Z9Oy7KXo43-sv6M0rZWrOlFBLbNMt1XJhU59VQjhze2YWPsABHwoiRSlMJZ9PCzmdGqsKCCrDSkB_T4gMbPB7hlC0RyP--MHoKabIaTgsS9i_nqO9fSZgaNoSwUkHTFd1BuG56_O4_OeuovJppEbXVW5eSqpf-ki9W6mAYHFVTGbo_ztkK6F6Jbesavi3zKTyTvYYnI3uTEFEIXrMvAjuKmO5df4k6zE5rVSIpnmDQmXPAu2UwFENGVCTJC40I68_HY2TUXa6neAircgJGxAXW5-CfKGppP0wZd1WVtqqHNQo4Fvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2f073a154.mp4?token=lortKJ8LFsQidBdl-l9CqjRy2e8sqUlxsaKO7Z9Oy7KXo43-sv6M0rZWrOlFBLbNMt1XJhU59VQjhze2YWPsABHwoiRSlMJZ9PCzmdGqsKCCrDSkB_T4gMbPB7hlC0RyP--MHoKabIaTgsS9i_nqO9fSZgaNoSwUkHTFd1BuG56_O4_OeuovJppEbXVW5eSqpf-ki9W6mAYHFVTGbo_ztkK6F6Jbesavi3zKTyTvYYnI3uTEFEIXrMvAjuKmO5df4k6zE5rVSIpnmDQmXPAu2UwFENGVCTJC40I68_HY2TUXa6neAircgJGxAXW5-CfKGppP0wZd1WVtqqHNQo4Fvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان خیلی جدی: در به در دنبال یکی میگردم مشکلات مردمو حل کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70238" target="_blank">📅 18:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70237">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aQ7xdU-V4JHrNWVL6Ohgc28p9oO57ncyaBW6A-tJtgOSOPjG2WuO0LCoxajjTSSK2tr7Vq_gsgFkVDQz1_MtV2u-NHUPmF9j1WruLrX1JvMnArt7S7qTaKNCLqzM7dovS2bCtIKyBbmSw2fM8mgFA6P-bC5JGxnrU2eFep2umvefHmmcQuAIHL6SlFSYtM5GnzCJrlppPHfbBJFr2d-3jTcG4nQkjx7B7iX0-Fbw0khQV79PObR5-xnP3Trxx5rXu87rhIHYVsjuby23FvSJjanZzCMT9VG5nTklmUMOYP-FOUxst_pXZX4GHQ0nSyuZz4PzgnIOawXIyfZKdX1exg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
هیچ مذاکره یا گفت‌وگویی با جمهوری اسلامی ایران در جریان نیست و هیچ مذاکره یا گفت‌وگویی نیز برنامه‌ریزی نشده است.
محاصره دریایی همچنان با تمام قدرت برقرار است.
تنگه هرمز باز و فعال است.
همه مین‌های دریایی جمع‌آوری یا منفجر شده‌اند.
از توجه شما به این موضوع متشکرم!
رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70237" target="_blank">📅 18:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70236">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe8b4bd45.mp4?token=gWj189jn5czlhtuGzdU52CpbYTKPgASF8mZiJkOhvtAUXNZvijjl6T9_vV2BsPRwqhU3OU7Y-N0la3XL4YyQkZmQY5JkNTXfSZvdfERrQ8F28ncFly_tIfHLBVFp4y2zT2bNiKlrDcVQrnJ-agP1vaCS5meKckBN7SKy0kgm0Uwvt0aUWgQLOvCYiVzsvx1RNJHEF35D5JWWT8ExcY37d4J-wWAQAV9yoyT2k33AtHfr7mJlhW1JRG6H5_sGp-0-fHCsC610jStg5tyFsyeWygGeO2-AH8vS5FVLss9miBk9wsP2eV0IxA6tG7HRCY4pQw4nZehR1UhmZRI0UOiDzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe8b4bd45.mp4?token=gWj189jn5czlhtuGzdU52CpbYTKPgASF8mZiJkOhvtAUXNZvijjl6T9_vV2BsPRwqhU3OU7Y-N0la3XL4YyQkZmQY5JkNTXfSZvdfERrQ8F28ncFly_tIfHLBVFp4y2zT2bNiKlrDcVQrnJ-agP1vaCS5meKckBN7SKy0kgm0Uwvt0aUWgQLOvCYiVzsvx1RNJHEF35D5JWWT8ExcY37d4J-wWAQAV9yoyT2k33AtHfr7mJlhW1JRG6H5_sGp-0-fHCsC610jStg5tyFsyeWygGeO2-AH8vS5FVLss9miBk9wsP2eV0IxA6tG7HRCY4pQw4nZehR1UhmZRI0UOiDzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همینطور که قالیباف داشت از دستاورداش توی لبنان می‌گفت ،
شبکه خبر هم با زیرنویس جواب شو داد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70236" target="_blank">📅 17:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70235">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53bff1d789.mp4?token=uhlrYmH_kXl5em-wFBzuZXwrpfNHzN0Ylmenpn0EcFTlFhBaX772-pVjoznawPRldcUHUkU5mUcRha9vpOntLxAve4p_zj9LUVbqctrdyBGrtqR7qRhzEk9WX5qow54Txg1SGtWlbWvkmWNwlcAJFXf5m4x39vJmU1lZb1wW9qVCeT6CZatfD29CEj6iDMRZsmCI1hYHK60GiB-GHihfKpuqjAfnmUFt-2ebntwaVKdDHGDPI9T3aQvdzRnEu5EVZQ4j91WEgtYR-2SEHfihPhM2z55-JjHuGiBBeYh_NKoaxfL8y4NZZPSgkUOA4epAlBMVTTwhviLGDnRAnjfHiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53bff1d789.mp4?token=uhlrYmH_kXl5em-wFBzuZXwrpfNHzN0Ylmenpn0EcFTlFhBaX772-pVjoznawPRldcUHUkU5mUcRha9vpOntLxAve4p_zj9LUVbqctrdyBGrtqR7qRhzEk9WX5qow54Txg1SGtWlbWvkmWNwlcAJFXf5m4x39vJmU1lZb1wW9qVCeT6CZatfD29CEj6iDMRZsmCI1hYHK60GiB-GHihfKpuqjAfnmUFt-2ebntwaVKdDHGDPI9T3aQvdzRnEu5EVZQ4j91WEgtYR-2SEHfihPhM2z55-JjHuGiBBeYh_NKoaxfL8y4NZZPSgkUOA4epAlBMVTTwhviLGDnRAnjfHiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرواز هواپیما C-295W آمریکا در ارتفاع پایین برفراز اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70235" target="_blank">📅 16:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70233">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ac96569c1.mp4?token=vGbm8dMmlj1BxA3P8AgHG9zHtQXwh75VynkCsNQXUFYQwdEucxR4zgbV3KWBtZv-_VasAXhZrOiVoIwYQ4cgTBeKSbZvTme7gZ2pOc8kurh89aC5KOMhI9Y4uM1etCBBpY29zRU2iAfVHC5ndVU3cz35YI-eUb_0NVW3KtV-lG5I3BQLrCXCukB92JZ2erC4sq8C4pHviaRK9CVl8JwC527hivLx-3WglwKNgk0yzPJMov_p5oFMhTUKdiNguiPSZgxmeDKYUxB75EwkEzvpnfvP2GuYwH5tlitZdmLp6H-YrNq2Paa8mCNXqPauZBU7dh0wNFPwts5lr-XIaqajpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ac96569c1.mp4?token=vGbm8dMmlj1BxA3P8AgHG9zHtQXwh75VynkCsNQXUFYQwdEucxR4zgbV3KWBtZv-_VasAXhZrOiVoIwYQ4cgTBeKSbZvTme7gZ2pOc8kurh89aC5KOMhI9Y4uM1etCBBpY29zRU2iAfVHC5ndVU3cz35YI-eUb_0NVW3KtV-lG5I3BQLrCXCukB92JZ2erC4sq8C4pHviaRK9CVl8JwC527hivLx-3WglwKNgk0yzPJMov_p5oFMhTUKdiNguiPSZgxmeDKYUxB75EwkEzvpnfvP2GuYwH5tlitZdmLp6H-YrNq2Paa8mCNXqPauZBU7dh0wNFPwts5lr-XIaqajpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
هنگ سوم عملیات ویژه اوکراین، شهرک آندریوکا-کلوتسوو در منطقه دونتسک را آزاد کرد و تقریباً 30 سرباز روسی را به اسارت گرفت.
کسانی که به مقاومت ادامه دادند، کشته شدند.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70233" target="_blank">📅 16:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70232">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEAbKWIIJh_Wb_nkTZVfPIs8YehN8XJY_bhbLF37B9Oah2Kk64YwxmVn1M_NIC2VPwYhYsIYjsSELKFhUc7jMauS4aInTKquckogrLGo9siptZTweJerT9_Sro5M0ioH7Ma_XdIhRDvnSlXOt_0jFjJo16cEqmunJHPQqTdslBDcoZXFb58gF3PoPrXC_XrMMi-R0cYlJ5ISpLdrtA8N_d_8sa4o2MakkeyLsiLQgn0WdlDhf1djZrQF3rViq-M1f3ZRwq5TULspkBWwel9DcKNWTPoy2z0TxVX-WugjJi1V-lpjeeuwRpz2aiRK9CuCc2NnDgkFZE0xtklxITmzwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
معاون وزیرخارجه جمهوری اسلامی:
همانطور که ترامپ نام خلیج همیشگی فارس را به صورت صحیح نوشت، به زودی توهمش درخصوص تنگه هرمز یا اصلاح می شود یا توهمات این متوهم را اصلاح خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70232" target="_blank">📅 15:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70231">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-0dHcU_SX9Tyz41wDjwSbsqC-x25NsVHPc1ojNKTiawxB-xO-z1K03i2p_Sc6gIN3_RvBoD48T5reu_MblCLNLVPocFYRyGsJ-Jvb0UdJTl648vwSH8G2Uu6LzWGQ85RR4ftgrBheh08bjgXK6w2X3i9U59K1y_pRyVcokH2S9a-PBZbGrQWMg2qFqh9_6vBih7ZJyzZsSkzg9n6BZ3St3cuv3DCNETOy6TWy5mkVRuJduKBmXsdUD90iwYpKEsl4-TBz-TSERMkkQXBg3sF6GWKagj_lgTh4J61cy8QhMA6KKXgmz6Foq523a0g6D21zY9WHUi4tCq_sGiywrJjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇺🇸
پست جدید املاکی در تروث سوشال:
تنگه هرمز قلمرو جدید ایالات متحده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70231" target="_blank">📅 14:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70230">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06cc678393.mp4?token=ikuoD_-ycaaCsuJlH-1itM_Fn5ngpxh29K0nCsh8aDHRdLmyiK_x4BAEEYkYqLBf26mV3q5UC7yXJ-W5-vTR-x7Fm2Rc7wFqJN-o-X1zG2LH_L9FgAckQewFIgeYhUv2S9ZcerorNUGycehr8AmIEtIrqM9b-AEHtoMBoqRKj-b324qvBqBb6v3gdjNFqasBAqJNjbDZcnt9OL6w-yCWufF0ST5rWvE_2GnGJu_SG0d53Embsg2yzqJzCFRAZsB-hcBrOH1A0oZgZy6mutSqq0P3zbnKDtkYJTuJ-jd9mVUsxeanx_Z3Q_gWm0OJ-6JRHaVlCc6oKJMPyZPXfBfEEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06cc678393.mp4?token=ikuoD_-ycaaCsuJlH-1itM_Fn5ngpxh29K0nCsh8aDHRdLmyiK_x4BAEEYkYqLBf26mV3q5UC7yXJ-W5-vTR-x7Fm2Rc7wFqJN-o-X1zG2LH_L9FgAckQewFIgeYhUv2S9ZcerorNUGycehr8AmIEtIrqM9b-AEHtoMBoqRKj-b324qvBqBb6v3gdjNFqasBAqJNjbDZcnt9OL6w-yCWufF0ST5rWvE_2GnGJu_SG0d53Embsg2yzqJzCFRAZsB-hcBrOH1A0oZgZy6mutSqq0P3zbnKDtkYJTuJ-jd9mVUsxeanx_Z3Q_gWm0OJ-6JRHaVlCc6oKJMPyZPXfBfEEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جعفرپور، مدیرعامل مخابرات:
قراره فیبر نوری کاملا جایگزین کابل مسی بشه که اینطوری سرعت اینترنت ثابت تا 80 برابر بیشتر میشه...
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70230" target="_blank">📅 14:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70229">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6829188988.mp4?token=ZGXuVBZUz9800uwQRJrvUPQ7pAJES6K7FvMXPZOluafOX1GaFnAFaZtb33r9AiP-XdxP2RfZ1hc_6jRwJot307azaYhdgJQjsVszt2F4p1T_SX4xllQD2vkh3kIGYsBwLqZwAqQ8GAsixTkq6Wn4w7-AA7QsMfmU02U8e6KuwiMU2gsShFaUXpsv5A8gfCWi3t3K7faDECPnt2kv7NzJzGOof2ahHo1V_wiDQRZitQovg-MGY68sXm7SuGbzlat4_YafrThz_67jk2cKWpR5KHoyQJTX89JiycnTPyCtEWTAPC85mBpjmjJgMUkpoZk9eZgIsdlxuRqjrS1vW10j7K1NLtMRNIt8yQctO0N5tB0NpKFgrbeBhFtD7JoqO2VO1jshzwJiHKHqJVBJG3vkVy-JDt1k2jRFSGmnpvZuIHC-kromMnejSa59irNHIf1XK4ueqxIrV7lrfXOkUWBemjt9VelCBMooy-m_t1i0FcmJc1fzOXrIcdFKC8Q4nIsOMpcvpHOtLGlmQuutepqU2lj-tcrj5JTSZSFBksNnfq3AXw4Gack9TODyYLLSOgbSb59Hua5uczDC8SK3gqwdTyRApCtOxwAhnMkYSDdxZKNLAYoSAPp-smg8_PGljomIOjdqu3foVQrZLjJsWQPo7AyX6UhXcJO8vbkxPURGvFI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6829188988.mp4?token=ZGXuVBZUz9800uwQRJrvUPQ7pAJES6K7FvMXPZOluafOX1GaFnAFaZtb33r9AiP-XdxP2RfZ1hc_6jRwJot307azaYhdgJQjsVszt2F4p1T_SX4xllQD2vkh3kIGYsBwLqZwAqQ8GAsixTkq6Wn4w7-AA7QsMfmU02U8e6KuwiMU2gsShFaUXpsv5A8gfCWi3t3K7faDECPnt2kv7NzJzGOof2ahHo1V_wiDQRZitQovg-MGY68sXm7SuGbzlat4_YafrThz_67jk2cKWpR5KHoyQJTX89JiycnTPyCtEWTAPC85mBpjmjJgMUkpoZk9eZgIsdlxuRqjrS1vW10j7K1NLtMRNIt8yQctO0N5tB0NpKFgrbeBhFtD7JoqO2VO1jshzwJiHKHqJVBJG3vkVy-JDt1k2jRFSGmnpvZuIHC-kromMnejSa59irNHIf1XK4ueqxIrV7lrfXOkUWBemjt9VelCBMooy-m_t1i0FcmJc1fzOXrIcdFKC8Q4nIsOMpcvpHOtLGlmQuutepqU2lj-tcrj5JTSZSFBksNnfq3AXw4Gack9TODyYLLSOgbSb59Hua5uczDC8SK3gqwdTyRApCtOxwAhnMkYSDdxZKNLAYoSAPp-smg8_PGljomIOjdqu3foVQrZLjJsWQPo7AyX6UhXcJO8vbkxPURGvFI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف:
هرفردی که با تصمیمات خود باعث نارضایتی مردم بشه از دشمن هست و تغییر شیوه کالابرگ حتما در دستور کار قرار میگیره
ما خودمون نیز در میدان مشکلات اقتصادی درگیر هستیم و راحت ننشستیم
نیروهای نظامی با اقتدار مجتبی خامنه‌ای تودهنی بزرگی به دشمن زدند که همه تعجب کرد
دشمن از روی استیصال اومد مذاکره و مجدد شکست خورد
خیابان محل میتینگ های انتخاباتی و برخی کارهای غیراخلاقی به اسم تجمعات نیست
تا رفع محاصره و آزادی پول ها و رفع تحریم های نفت و پایان تهدید و توقف کل عملیات ها در سرتاسر جبهه مقاومت تنگه هرمز باز نمیشه
تفاهم نامه باعث شد تاب آوری مردم بالا بره و از نظر نظامی خودمونو بازسازی کنیم
افزایش قیمت بنزین تدبیر نیست آقایان دشمن بر آشوب و اغتشاش از روی بنزین حساب کرده مواظب باشید
صداوسیما دیگر قدرت سابق رو نداره و عملا در رسانه شکست خورده حساب میشیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70229" target="_blank">📅 13:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70228">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fcfe671f.mp4?token=V0LGCEuSNomQdCYmddthQdn5CZWiGZMI6Xa4tAmqS9gdPF5C0laJQTC7ZFQ0yQlRRpDYy1m0TAin_U1rPwVoccASPaFcKWM9y3cvDqmx44iNkVzJiWbehkB2cDuJvjnurHvSbvAH4osF0_fQJcKfnjfMVhYWvkiClZnM6CHuzbTIP5FsA2Tn_EmxxajRl8PLDLbYrq7H3Sf0t0-95DpcWXGrkjhvUsvU5jeqBfOjFKsh6D5CSqmKb-hfG7tUvWI46ijyF5REvGWgUSBOp-K-XwutAHpfRxcXp2FoBoQj11lwexFEq2-CW2kRki6dUSMCfDtS7qA6mKrZX4WHsevREA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fcfe671f.mp4?token=V0LGCEuSNomQdCYmddthQdn5CZWiGZMI6Xa4tAmqS9gdPF5C0laJQTC7ZFQ0yQlRRpDYy1m0TAin_U1rPwVoccASPaFcKWM9y3cvDqmx44iNkVzJiWbehkB2cDuJvjnurHvSbvAH4osF0_fQJcKfnjfMVhYWvkiClZnM6CHuzbTIP5FsA2Tn_EmxxajRl8PLDLbYrq7H3Sf0t0-95DpcWXGrkjhvUsvU5jeqBfOjFKsh6D5CSqmKb-hfG7tUvWI46ijyF5REvGWgUSBOp-K-XwutAHpfRxcXp2FoBoQj11lwexFEq2-CW2kRki6dUSMCfDtS7qA6mKrZX4WHsevREA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تفاوت وحشتناک قیمت گوشی ها در عرض یک سال:
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70228" target="_blank">📅 13:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70227">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5264a79fd5.mp4?token=KMd7H1uwEwYfRla40skhpcRoId351u6f450wGT9IZBi6OE0UxP0gxq18I3B6V06881Q_KFzHjUQfgcjreasNV8XSUxpSW5wRYwCP69Qvu0e6OY03GGXWlpI1hV21pViL3K7Scz3zlgSWDWG-y0dMQePZLewJS7knnffwJZyh4aPUa6jsQLMHsHwFHLHOoZrzU_Yik9CkgVY912DovWTSeVZUkZzoy-gDkAiRskQqCWlmKYWQ5LXMErqgPgucdAHCYku312tLHPPQmu_29QOdDrEYVAMYvI3CAumIPxHeOSYCi22x31lX39gUS1UDJkLD_xU8eR84gAjfpbx3_kBhrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5264a79fd5.mp4?token=KMd7H1uwEwYfRla40skhpcRoId351u6f450wGT9IZBi6OE0UxP0gxq18I3B6V06881Q_KFzHjUQfgcjreasNV8XSUxpSW5wRYwCP69Qvu0e6OY03GGXWlpI1hV21pViL3K7Scz3zlgSWDWG-y0dMQePZLewJS7knnffwJZyh4aPUa6jsQLMHsHwFHLHOoZrzU_Yik9CkgVY912DovWTSeVZUkZzoy-gDkAiRskQqCWlmKYWQ5LXMErqgPgucdAHCYku312tLHPPQmu_29QOdDrEYVAMYvI3CAumIPxHeOSYCi22x31lX39gUS1UDJkLD_xU8eR84gAjfpbx3_kBhrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
محمد‌باقر قالیباف:
قبل از رفع محاصره، آزادی اموال بلوکه شده، رفع تحریم نفت و پایان تهدید و عملیات نظامی در همه جبهه ها و دیگر شروط تفاهم نامه، تنگه هرمز باز نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70227" target="_blank">📅 12:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70226">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90eeeac0ea.mp4?token=fQTbBRIhv8jdvoyYK5yA4KuAnR0YRvQrU-yfnf3uQ40sYP1JR9cJUNB1R0ua3lgoaCx8fDXhbWML2oGUrCMWaP7q1FDDtyW0r_i2QmOnu9bnQ6IyIHVEoJstBHFkaQrtw8nRf4sanUpwscrPtXiejyb9lufLu47Kghmh9fH_9OtEM31eOtEhgXx9wSPl8O1vH67nu_HI5TjmN3qL1mydyZQZOWXZgd4lppdkom8fZ64u-5llMeK9F0mobXEQ4-KSdn-kXBvfzUDFkDLj8vsHiBYvKmeEEbXQ9cTkdPKGXq5qsWmuX4sHpxSQ3rl9bow-CmtIoI2Ka7iOA_dcmIUWhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90eeeac0ea.mp4?token=fQTbBRIhv8jdvoyYK5yA4KuAnR0YRvQrU-yfnf3uQ40sYP1JR9cJUNB1R0ua3lgoaCx8fDXhbWML2oGUrCMWaP7q1FDDtyW0r_i2QmOnu9bnQ6IyIHVEoJstBHFkaQrtw8nRf4sanUpwscrPtXiejyb9lufLu47Kghmh9fH_9OtEM31eOtEhgXx9wSPl8O1vH67nu_HI5TjmN3qL1mydyZQZOWXZgd4lppdkom8fZ64u-5llMeK9F0mobXEQ4-KSdn-kXBvfzUDFkDLj8vsHiBYvKmeEEbXQ9cTkdPKGXq5qsWmuX4sHpxSQ3rl9bow-CmtIoI2Ka7iOA_dcmIUWhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو هند چون یه گاو از طریق ترانسفورماتور دچار برق زدگی شده مردم با چوب دارن ترانسفورماتور رو میزنن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70226" target="_blank">📅 12:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70225">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/70225" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70225" target="_blank">📅 12:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70224">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=CcR4wqit_Sj032Jo72TO2poNR6xgrJJ3naR7rxhH0oJUEHAH2e1eno8utB-zlqFu-HYbU8nAS1UYly3NPR-6DD7ApkjgiZxOJVnlZjJ42ETIHENEy3kGLT9rxaHMZmeo2z2e7eksGtc-Qp5WMYo-jTRYXJ2PLcaiLuFCQGfkdfS4rBA2L0pspb2GHmmdCjWz9Nmnw8Y7cwSdDAGqvNoAbMcdpm9yuME00dpxkNA4Zb8OuwMd-wKoXJlM_elI-W-Z2zbdVJxEERXfrWXH8bu7N64b0ZXR02UyJqfPUTgL3wyJtfRkxLu9-t4-lrpUHwbcsHWEefHj2_0-YcF3wmbvew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=CcR4wqit_Sj032Jo72TO2poNR6xgrJJ3naR7rxhH0oJUEHAH2e1eno8utB-zlqFu-HYbU8nAS1UYly3NPR-6DD7ApkjgiZxOJVnlZjJ42ETIHENEy3kGLT9rxaHMZmeo2z2e7eksGtc-Qp5WMYo-jTRYXJ2PLcaiLuFCQGfkdfS4rBA2L0pspb2GHmmdCjWz9Nmnw8Y7cwSdDAGqvNoAbMcdpm9yuME00dpxkNA4Zb8OuwMd-wKoXJlM_elI-W-Z2zbdVJxEERXfrWXH8bu7N64b0ZXR02UyJqfPUTgL3wyJtfRkxLu9-t4-lrpUHwbcsHWEefHj2_0-YcF3wmbvew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
😅
😂
😆
:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r27
@betinjabet</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70224" target="_blank">📅 12:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70223">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89c5472e37.mp4?token=Z0h-9JLUwqLyVxAA1L_kEzK2iCULfOBo2a6LA1DbUQ3lD09Hb_0h9UzW7xL0kXGah9hmvjiNQ5qORd5O6saMrCh5BJjMpCRa5h9RMx5L8Icb0jlsKBBBjCATIKWduFNEOnmA_dpBKStTmWKCslMAfnzGwxEyDLjdQhjLkfe_MCe1GK9vOE3BT3H5pT10H62R4ww1jlvfrnlAXw0pBHQp00KoPuAVmCrMRkMBTrSZ-WM_9O5kEKMZdP8_7EWXoR7-OLKIlnAKfRHxqtorsvMcUNK9saA7EUgnK4enN-mQ457uLW336SYQV1D3A79fONA9fR6z0GelZkrxHcf0QBHPQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89c5472e37.mp4?token=Z0h-9JLUwqLyVxAA1L_kEzK2iCULfOBo2a6LA1DbUQ3lD09Hb_0h9UzW7xL0kXGah9hmvjiNQ5qORd5O6saMrCh5BJjMpCRa5h9RMx5L8Icb0jlsKBBBjCATIKWduFNEOnmA_dpBKStTmWKCslMAfnzGwxEyDLjdQhjLkfe_MCe1GK9vOE3BT3H5pT10H62R4ww1jlvfrnlAXw0pBHQp00KoPuAVmCrMRkMBTrSZ-WM_9O5kEKMZdP8_7EWXoR7-OLKIlnAKfRHxqtorsvMcUNK9saA7EUgnK4enN-mQ457uLW336SYQV1D3A79fONA9fR6z0GelZkrxHcf0QBHPQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دکتر فلاح نژاد: امشب یه دختری دوس پسرشو آورد پیشمون که گوشش کنده شده بود؛
گوشش تو دست دختره بود،گفتیم جریان چیه؟
😟
گفت دوس پسرم به حرفام گوش نمیکرد اعصابم خرد شدن گوششو گاز گرفتم از جا کندمش بعد دیدم حالش بده آوردمش بیمارستان.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70223" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70222">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9e0c9bd0.mp4?token=RkJ9jYyD5GgWmMNMXVbhIUUGprnPdr9M-i_cj9YGfb3hNViq61GFuux-a47GZSCUZeBeNFzsrDhjsN6Thoud758WoOWsffS0ByQ2LmplWgjP9355FhTWsNUxruVwELJecMoT_RJofUAMY9QgOMbDDKVArYhoMWo46-zHTRJBDCtmGFviV2uux529CvuUthr5ltb0OZKyA-6X2ppVjqmZZ2n3DOg2EO7SvVFjuALzgX16XwxfS4PqAK2yodROJix-3D60dQnZgn_vqwCgXNxUczGrsEGCG2Bp1qgBF6fY-KTFZ1bX8aCRxjf48Q_t4dwKM_Lt8F5lZnyLIZBl2B5ypw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9e0c9bd0.mp4?token=RkJ9jYyD5GgWmMNMXVbhIUUGprnPdr9M-i_cj9YGfb3hNViq61GFuux-a47GZSCUZeBeNFzsrDhjsN6Thoud758WoOWsffS0ByQ2LmplWgjP9355FhTWsNUxruVwELJecMoT_RJofUAMY9QgOMbDDKVArYhoMWo46-zHTRJBDCtmGFviV2uux529CvuUthr5ltb0OZKyA-6X2ppVjqmZZ2n3DOg2EO7SvVFjuALzgX16XwxfS4PqAK2yodROJix-3D60dQnZgn_vqwCgXNxUczGrsEGCG2Bp1qgBF6fY-KTFZ1bX8aCRxjf48Q_t4dwKM_Lt8F5lZnyLIZBl2B5ypw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی الیگودرز لرستان اومدن کف رودخونه شهر رو اسفالت کردن!!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70222" target="_blank">📅 11:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70221">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e66075a5.mp4?token=YkDSxpQUtJsYBCoJvu4YGXNQMs5wSGsEI62FSmzkYiM6G79lj3bFvnlIaRVJ4hA4mF1e3LXHJlEZqvpfi7IKfOm6HAvODUlkGUra7SmWT7Ofi_chcvQGww4WdkLzoaQTDfGXCsAvhtQDVQR92UkboAnkILzDqXDI4G1SIcqoz-qqLJ1e9qZT9Q8QlLIIbUKyhb7MHo1FC-YFucaebFOtlJwNpsUIpcnG4fksQB-x3iIldb1eth4XK3OO4pg1a28xWhHBVAve5XaRr7ZGSOp6o684FMSr8Bh5f_ai-0xb65eqng2q25HGJuCR29XiH-QFmLLI6ufCfuHz9Dg0_S1a8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e66075a5.mp4?token=YkDSxpQUtJsYBCoJvu4YGXNQMs5wSGsEI62FSmzkYiM6G79lj3bFvnlIaRVJ4hA4mF1e3LXHJlEZqvpfi7IKfOm6HAvODUlkGUra7SmWT7Ofi_chcvQGww4WdkLzoaQTDfGXCsAvhtQDVQR92UkboAnkILzDqXDI4G1SIcqoz-qqLJ1e9qZT9Q8QlLIIbUKyhb7MHo1FC-YFucaebFOtlJwNpsUIpcnG4fksQB-x3iIldb1eth4XK3OO4pg1a28xWhHBVAve5XaRr7ZGSOp6o684FMSr8Bh5f_ai-0xb65eqng2q25HGJuCR29XiH-QFmLLI6ufCfuHz9Dg0_S1a8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ایرانی های حاضر در ترکیه:
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70221" target="_blank">📅 11:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70220">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a948c02f.mp4?token=N0flmHDFNqUNEpZK6UQ6Hy1wmsp-Ttjyi6wHTKtybZ0WH3ZIQS_EY00iepGNQ9E2v3Sm0pFIkjcXQK4Ni38HQ0bW0gAdpjRlnG889z04Uuz5UizZA4brWRrQ2gHmSJw5ndx5Z0AG6tJY5v4ozdMjFLE9_QiKLkVLrdGrr6IOyZk9EOArqC_msatU-ZTXXWoALJsGh6MazDCerZFpYe1t8wBKp9jq8QMTdGBL8hBIj88nhqRhkCdlITw9NmkDe2HkocvNstriG_NXpE3Q182-B7S-92BUE0IfrsAzc2zlfmlmWIFnBYumqzIA8DJoOWIVcTT8SgHF4JGgoLTmERlFtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a948c02f.mp4?token=N0flmHDFNqUNEpZK6UQ6Hy1wmsp-Ttjyi6wHTKtybZ0WH3ZIQS_EY00iepGNQ9E2v3Sm0pFIkjcXQK4Ni38HQ0bW0gAdpjRlnG889z04Uuz5UizZA4brWRrQ2gHmSJw5ndx5Z0AG6tJY5v4ozdMjFLE9_QiKLkVLrdGrr6IOyZk9EOArqC_msatU-ZTXXWoALJsGh6MazDCerZFpYe1t8wBKp9jq8QMTdGBL8hBIj88nhqRhkCdlITw9NmkDe2HkocvNstriG_NXpE3Q182-B7S-92BUE0IfrsAzc2zlfmlmWIFnBYumqzIA8DJoOWIVcTT8SgHF4JGgoLTmERlFtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇯🇵
وقتی میگن ژاپن تو یه جهان دیگست یعنی این ؛
اومدن خیلی جدی یه سوتینی ساختن برای خانما که تو تابستون بپوشن و با خیال آسوده برن بیرون تا گرمشون نشه یه وقت
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70220" target="_blank">📅 10:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70219">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4716008946.mp4?token=NOhu7k0k2mxxS91zLpyFewBl10QYVFIF5km_MHe6k9XoEuPlwNL6meZifUcwaHpo7JIy5re7toVixQZpL4oN0Tl0upqjx3fK3NBEDAyPYZ_7-9HeuhhPH6t6kBR9EuFL7o5L8BC2h7HGKhBZlAE7Z-0W3G26qCNSggIEtaAihIqAvrKpdhVDo7tgXOPi84Pk8KMh_ZNC6HubrMQeL9FkLUSk6rxdOtrpbomWGbBqsf-vDM077UQxG0HgexWIa0ntqI2Y0SiUJqhA4VtpJiGRnEboVo31noPdulb6AwmWE5wL1iIfJz8kPJJGjSQvBnDvsiWhQoEeKb7_XtBsUBK6pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4716008946.mp4?token=NOhu7k0k2mxxS91zLpyFewBl10QYVFIF5km_MHe6k9XoEuPlwNL6meZifUcwaHpo7JIy5re7toVixQZpL4oN0Tl0upqjx3fK3NBEDAyPYZ_7-9HeuhhPH6t6kBR9EuFL7o5L8BC2h7HGKhBZlAE7Z-0W3G26qCNSggIEtaAihIqAvrKpdhVDo7tgXOPi84Pk8KMh_ZNC6HubrMQeL9FkLUSk6rxdOtrpbomWGbBqsf-vDM077UQxG0HgexWIa0ntqI2Y0SiUJqhA4VtpJiGRnEboVo31noPdulb6AwmWE5wL1iIfJz8kPJJGjSQvBnDvsiWhQoEeKb7_XtBsUBK6pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلاغ کینه‌ای؛ سه سال است که دست از سر این پیرمرد برنمی‌دارد.
یک ماجرای عجیب که این روزها در فضای مجازی دست‌به‌دست می‌شود؛ پیرمردی ایرانی ظاهراً نزدیک به سه سال است با یک کلاغ سمج حسابی مشکل شخصی پیدا کرده
طبق روایت منتشرشده، ماجرا از زمانی شروع شد که پیرمرد یک جوجه‌کلاغ افتاده از لانه را برداشت. از آن روز به بعد، کلاغ‌ها هر بار او را می‌بینند به سمتش شیرجه می‌زنند و سر و کله‌اش را هدف می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70219" target="_blank">📅 10:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70218">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uflAbnx1y7453Le2fMaGhvGQBxSKp-QIs6CHF6YuFvoYGM56vbngi6kpaH8JRh8mKQSuqVZHFfqHrBWxhNb329mpO-GFNlSiv7CgRkQva68u1EM0nEBuEdnqpkkGHahS7jwUPduBHCi1HYnkCXzBNdrVejyDr3zke1m6wvXO4nLcSRXedvoLhHrQyOilpehWefYi4uD2BUK2uB-MbVwXAJ3X80gCykhCJwmY4-drq6a3Q02P-LBLzwRDWPzAbAF3qjbVZS_Uc8fCfoshvWIO-VlLeq2Zi7jXoNjW6MDt_2eebMgSp0MzirZODqipLzFbfpqTYxVaqoGYLKLW4jFoOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ساعاتی پیش سپاه‌پاسداران به یک کشتی در حال عبور از تنگه‌هرمز حمله کرد:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارش داد که یک کشتی هنگام عبور از تنگه هرمز در مسیر خروج، مورد اصابت یک پرتابه قرار گرفته است.
این برخورد به موتورخانه کشتی آسیب رسانده و منجر به تلفات جانی برای یکی از خدمه شده است؛ سایر خدمه نیز تحت امدادرسانی گارد ساحلی عمان قرار دارند.
تاکنون هیچ‌گونه پیامد زیست‌محیطی گزارش نشده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70218" target="_blank">📅 09:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70217">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e635bc1048.mp4?token=kLIabfGPzzsTs_IDhLWzi_THo6PdMn0pdA_EUKh2_Zfoap6aXFXak9bSlkpVF3gLHpbnwJt86QeHlkWKqukOibMzvgIF2IlbcS7Nm7ORYJB50SihK674lrSC4J1via2kuiF95Ts0TmbAvluEbzc08TpCl29hw1DtsnUbkIZkMb4-LDxRJLewn1vdY9ri7aLsfuANo-lAt9awDF2-i0XGPpZKz8kGR72ZlU9hSYjVe4JHa_Utp5ecRjHGX7n6e1xm1cqRVx6k5yaNhE7JjmdH7NqxK8259G2ZWUxqG84Fh4DiDea3LaxDXLlUV2aYXBsPRa2as6ZxMas-5plrwlNBpYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e635bc1048.mp4?token=kLIabfGPzzsTs_IDhLWzi_THo6PdMn0pdA_EUKh2_Zfoap6aXFXak9bSlkpVF3gLHpbnwJt86QeHlkWKqukOibMzvgIF2IlbcS7Nm7ORYJB50SihK674lrSC4J1via2kuiF95Ts0TmbAvluEbzc08TpCl29hw1DtsnUbkIZkMb4-LDxRJLewn1vdY9ri7aLsfuANo-lAt9awDF2-i0XGPpZKz8kGR72ZlU9hSYjVe4JHa_Utp5ecRjHGX7n6e1xm1cqRVx6k5yaNhE7JjmdH7NqxK8259G2ZWUxqG84Fh4DiDea3LaxDXLlUV2aYXBsPRa2as6ZxMas-5plrwlNBpYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بخشی از صحبتای دیشب ترامپ با خبرنگاران درباره ایران به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70217" target="_blank">📅 09:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70216">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31325063ce.mp4?token=gTLZmbpYg2MNTDWz3Bpp6bSS1rZwyzFjfpbqoiBJnXwHHFPufM87wke5Jn5WwdxXOGfN5xK57n_tE8mA5ZQJcT_Tp0UoZgPj0EV4Z6R5Zt1k0KDZdroS2HtL016xnqTCZ_nbqaDwFrfuIcMuMExeEo0aUt_M8X6LOCMlYQ0-rmPlmImDJomKGAkBGf5wfzFC4eyv-MlRbFrTwPuwlsgjr6qzIYKtzh5Vw6LzTrFsiT5q7oScbqCue0uMTHaD0iE-4i4cV7mAhz0JjbimAm3LPLtSMlNOszw4Vgu9TXXGEPnwKgVNmv1YiKjNSQUKF7Se1_30DjrrKqVx7HvyCDP0Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31325063ce.mp4?token=gTLZmbpYg2MNTDWz3Bpp6bSS1rZwyzFjfpbqoiBJnXwHHFPufM87wke5Jn5WwdxXOGfN5xK57n_tE8mA5ZQJcT_Tp0UoZgPj0EV4Z6R5Zt1k0KDZdroS2HtL016xnqTCZ_nbqaDwFrfuIcMuMExeEo0aUt_M8X6LOCMlYQ0-rmPlmImDJomKGAkBGf5wfzFC4eyv-MlRbFrTwPuwlsgjr6qzIYKtzh5Vw6LzTrFsiT5q7oScbqCue0uMTHaD0iE-4i4cV7mAhz0JjbimAm3LPLtSMlNOszw4Vgu9TXXGEPnwKgVNmv1YiKjNSQUKF7Se1_30DjrrKqVx7HvyCDP0Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
📰
گزارشی از مجتبی پورمحسن:
همزمان با تایید تماس محرمانه دولت آمریکا با فرمانده کل سپاه‌، ترامپ، در پایان مهلت ۶۰ روزه برای توافق، از تهران خواست تسلیم شود.
اما وب‌سایت اسرائیلی وای‌نت، با انتشار جزئیات تازه از زندگی مخفیانه مجتبی خامنه‌ای، از تسلط سپاه بر جمهوری اسلامی خبر داده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70216" target="_blank">📅 08:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70215">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70215" target="_blank">📅 01:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70214">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=HWt7Oc8jhrPDj3Sy3KfQ1IEAE7ve5iz0aY7aqipFcMp-jIyN7556EBccIUzZZ6a0d0iJ81U2MfyQeDRcV6a3kIN5Nhc28FRVibSBP5bdEMSBib2IGRuaoG-ePcU4tbNkHJy8jSlzZ6E_mqqytPia_QO9Cmg0XqBYqyzBWSpTg88z3UQl7PJ8DfnruCK8RMfFAV4c6qojs3NccoTvI2zZ1tpHmt3W4KJwVinxwKpo5g_immQS6QesUBvtWEpYiikj7i3fxTtSoNElMDCMFi5rWg2xIIS4NFu8u2eDL_NnbSUtwN-hRVm_UNZ5DTViKmR9JtrNbqsUZub1cgIOEI4lrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=HWt7Oc8jhrPDj3Sy3KfQ1IEAE7ve5iz0aY7aqipFcMp-jIyN7556EBccIUzZZ6a0d0iJ81U2MfyQeDRcV6a3kIN5Nhc28FRVibSBP5bdEMSBib2IGRuaoG-ePcU4tbNkHJy8jSlzZ6E_mqqytPia_QO9Cmg0XqBYqyzBWSpTg88z3UQl7PJ8DfnruCK8RMfFAV4c6qojs3NccoTvI2zZ1tpHmt3W4KJwVinxwKpo5g_immQS6QesUBvtWEpYiikj7i3fxTtSoNElMDCMFi5rWg2xIIS4NFu8u2eDL_NnbSUtwN-hRVm_UNZ5DTViKmR9JtrNbqsUZub1cgIOEI4lrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a26
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70214" target="_blank">📅 01:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70213">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jevSCfgFRkPryKERbo450GBZuYHLb-EO8-QV47Fb_qC63TIcAZkc3Kfdpwnfd6bcuWAh11CXjkVjbZcjmqgmUFUEji5dUKJloCDFAJSBkRI4peHi9AiYfqNkjpLVXuRU6mFNq_5UzJsOHK_gtKmFTbHD_YzKs7tqhK0MauPk0HKaacWhdnkhy42Te-cZpmJZrM0swq6_HccU6Yw-xcNeb9TBIrgV0psh5kYrZG0VubYfuHX8cbJEJG9R41IdrcjgtYNA-gfcPv4QAhdk64WmCPi8kEZ7Y3Om6qLyuJtzGgs8AoPt-oSjZjW6q1eaDqQuNNueHT6bdgsbOk0Xtnwgyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست جدید املاکی در تروث سوشال:
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70213" target="_blank">📅 01:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70212">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7cb5678c.mp4?token=UpZbSPwUMU-o4jHMBNJY03uwJ5QpOX1ssG3t87Opu_Ple7xbfBPppAF9jFXpqd4GjRnTy7xrNDNU7WYJ8aIoHHZEsL4ldXkQjDNTGMHwsYTMBJyPdexdFQMtkhx9vwTBx3q-hp3acPXp98kIw3WE3c9V_YI4hpeVQtEMsjdgQCRptiihe9ZWppKHB0vUu1KfWYXOjqrrlOw2tK4j68FNqZAkXG1prENi67L1UpbgwupOh2gVYlRXVcokcglX5PuFrdC5dltUTjIF5wd5EN5DLwFEVCWltOIl5DH3gNDPETtKggcMbIPHjKY8WWblYmOnoyI8peklmjwPnhnMbuxsiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7cb5678c.mp4?token=UpZbSPwUMU-o4jHMBNJY03uwJ5QpOX1ssG3t87Opu_Ple7xbfBPppAF9jFXpqd4GjRnTy7xrNDNU7WYJ8aIoHHZEsL4ldXkQjDNTGMHwsYTMBJyPdexdFQMtkhx9vwTBx3q-hp3acPXp98kIw3WE3c9V_YI4hpeVQtEMsjdgQCRptiihe9ZWppKHB0vUu1KfWYXOjqrrlOw2tK4j68FNqZAkXG1prENi67L1UpbgwupOh2gVYlRXVcokcglX5PuFrdC5dltUTjIF5wd5EN5DLwFEVCWltOIl5DH3gNDPETtKggcMbIPHjKY8WWblYmOnoyI8peklmjwPnhnMbuxsiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🇺🇸
جرد کوشنر درباره ایران :
ترامپ فعلاً فشار اقتصادی رو بیشتر کرده
اگه ایران حاضر بشه توافقی رو که درباره کنار گذاشتن توان ساخت سلاح هسته‌ای داریم جلو می‌بریم، نهایی کنه، ترامپ حاضره یه توافق خوب به نفع مردم ایران ببنده
ولی فعلاً ایران دنبال انجام کاری که از نظر ما منطقی باشه نیست
الان آمریکا با بخش‌های مختلف دولت ایران خیلی جدی و بیشتر از همیشه در ارتباطه و گفت‌وگوهای خوبی هم داشتیم
البته بعد از این همه سال، اعتماد زیادی بین دو طرف نیست.
ایران داره جدی مذاکره میکنه و این مثبته، ولی هنوز به نتیجه نرسیدیم.
ترامپ هم عجله‌ای نداره و وقتی توافق درست آماده بشه، می‌ره سراغش
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/70212" target="_blank">📅 00:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70211">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c20632f388.mp4?token=S48qb0uD3ssp4M3QTUFswMHsd5C5TDz_AoIRrdNUiQLyxqhq31hyhHvWP2IUkiGBiaPiZcR0JgmHChS6TfhxhCYuYFQ3Dcv8C2lUtn1nX213BXJ6ejdvu36vPC2p8d9vrHh2fQxkncikJW06vWv5EmRDiV9uXQ24Dwd9N_Q1boPPvO3G9SEsJkzmxvuryRJpPm1NqKF5NAbCCoDRn86gllHqx77wfbVC29wXtbetp4vZG5EMcsZxIXRbt3-Ay8LTNFlcDGQnk_ugNi0Bomu1-xlEbO7dpiEHzHZUZLnJA9fFq5EQWJpG_iW3CVJBCrH6eNBHUqrvj8HjSrO2sWFHIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c20632f388.mp4?token=S48qb0uD3ssp4M3QTUFswMHsd5C5TDz_AoIRrdNUiQLyxqhq31hyhHvWP2IUkiGBiaPiZcR0JgmHChS6TfhxhCYuYFQ3Dcv8C2lUtn1nX213BXJ6ejdvu36vPC2p8d9vrHh2fQxkncikJW06vWv5EmRDiV9uXQ24Dwd9N_Q1boPPvO3G9SEsJkzmxvuryRJpPm1NqKF5NAbCCoDRn86gllHqx77wfbVC29wXtbetp4vZG5EMcsZxIXRbt3-Ay8LTNFlcDGQnk_ugNi0Bomu1-xlEbO7dpiEHzHZUZLnJA9fFq5EQWJpG_iW3CVJBCrH6eNBHUqrvj8HjSrO2sWFHIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
موسوی، نماینده مجلس : بنزین ما اصلا هم ارزون نیست؛
اگر حداقل حقوق مارو در نظر بگیرید، برخلاف حرفایی که گفته میشه ما بنزین ارزونی نداریم.
ما با حداقل حقوق، میتونیم 130 گالن بنزین 3 هزارتومنی بزنیم، ولی یه نفر تو آمریکا با حداقل حقوقش میتونه 750 الی 800 گالن بنزین بخره.
ما اقتصادی داریم که طرف یخچالش خراب میشه، میره زیر خط فقر.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/70211" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70210">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7953006a94.mp4?token=OVzB66zfSyGS5BjkFXbc_5Bvvc3OZFquugXOIDhL3WXW4FVAE97BeJiQBjG5i42SOLDFslWOe8ANd3JOxX2lBsF1qhZ7lvwLKm1PA_NNxHkqLWLZRzF9ElQj8nrYU2QUVmXkL3QANYcA55Z3aV7MGj86mzRz4rMUvYNrdVZNOn16wsp0R6GHWp45upFl0KckNkynbZUJ3rA4DNqhkj5J8TsbaciqzWb_6nB0WbWBXNVuMnhNnurmaQcLsuo6nau3y_QX_rep4qPLBp9XBNNnyjC4BHHgcwgPJmDnFtMh1WPoIICRDDL7utUHNO9I1XJVyebasxhIKS5pCyoh1ntK-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7953006a94.mp4?token=OVzB66zfSyGS5BjkFXbc_5Bvvc3OZFquugXOIDhL3WXW4FVAE97BeJiQBjG5i42SOLDFslWOe8ANd3JOxX2lBsF1qhZ7lvwLKm1PA_NNxHkqLWLZRzF9ElQj8nrYU2QUVmXkL3QANYcA55Z3aV7MGj86mzRz4rMUvYNrdVZNOn16wsp0R6GHWp45upFl0KckNkynbZUJ3rA4DNqhkj5J8TsbaciqzWb_6nB0WbWBXNVuMnhNnurmaQcLsuo6nau3y_QX_rep4qPLBp9XBNNnyjC4BHHgcwgPJmDnFtMh1WPoIICRDDL7utUHNO9I1XJVyebasxhIKS5pCyoh1ntK-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
منوچهر متکی، نماینده مجلس:
درباره احتمال جنگ زمینی با آمریکا گفت در چنین نبردی «جنازه» نیروهای آمریکایی نیز به خانواده‌هایشان نخواهد رسید.
تصرف یک پایگاه آمریکا در عراق، کویت یا بحرین می‌تواند سرنوشت جنگ را تعیین کند و به آن پایان دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/70210" target="_blank">📅 23:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70209">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa369bc00a.mp4?token=ZO0dV76p2oOm7ovFBeHBH3SKVW8i0tAbX5Y-B0wujVi3iyPPZ263GNmhCFMdAr7hK28FgIkZg6CbXMEu8WvLFH8ItQBoPuQn6CaEt_JYSrlg6Y9c9EvcaIpULMAYWckyZt01MyXn0VL7O2rE9VummRjKfGW7bjc87zpyoCGWqW2_C1V0cGVUYGJBiMrUhAPHUake3UeWqJ8wtUxw6jJdFJtZjquGGcv7w6NvTjdX4BaoBv8PdeWeWZIV7labwCQ7gCIdV6pbG8DxgmLA2rwHZ_oVNypNgj9088lG8qGGx6LtvyHUoQ62AcBmRU7U4qh-RXpavI0AYo57UXSUFnFQAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa369bc00a.mp4?token=ZO0dV76p2oOm7ovFBeHBH3SKVW8i0tAbX5Y-B0wujVi3iyPPZ263GNmhCFMdAr7hK28FgIkZg6CbXMEu8WvLFH8ItQBoPuQn6CaEt_JYSrlg6Y9c9EvcaIpULMAYWckyZt01MyXn0VL7O2rE9VummRjKfGW7bjc87zpyoCGWqW2_C1V0cGVUYGJBiMrUhAPHUake3UeWqJ8wtUxw6jJdFJtZjquGGcv7w6NvTjdX4BaoBv8PdeWeWZIV7labwCQ7gCIdV6pbG8DxgmLA2rwHZ_oVNypNgj9088lG8qGGx6LtvyHUoQ62AcBmRU7U4qh-RXpavI0AYo57UXSUFnFQAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری لفظی ترامپ با خبرنگار سی‌ان‌ان:
🇺🇸
ترامپ: ساکت، ساکت، ساکت. خیلی بی‌ادب هستی. ساکت. از کدام رسانه هستی؟
🎙
خبرنگار: من از سی‌ان‌ان هستم.
🇺🇸
ترامپ: شما «فیک نیوز» هستید. ساکت باش، ساکت باش، ساکت باش. تو یک خبرنگار جعلی هستی.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/70209" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70208">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9432d377e1.mp4?token=hGjdCk4jsdqfQweArQJevQ3EWtvYMV4odD4_H2py8iyLRRzxcIDCtAeCLDaL7f9HVI1GlMtixaB5Nk-bztx6mcezHtcI033N8qSaJ54bvklwtBrxXdy3BJaQnbymzDZNYisaN1KBAXYY5vO9JTwW3ano7b_PAE2oX88aDnrF7ThDDi-Aj7RKVo_hFaVu1tU9A9C2r4_vP9Oy-xs6NRup_AUnOVXmtbA38YrVu_DMzCIqNlQOIa4IV096zXl3lMrmGNM0h3JF6rHYOnzaFxppzxsig29XiCa_JB5Dq-CuJlh3odBNnpM_c6Us2O-HXBaEt0s0nexjuCVl1wUKz9NILA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9432d377e1.mp4?token=hGjdCk4jsdqfQweArQJevQ3EWtvYMV4odD4_H2py8iyLRRzxcIDCtAeCLDaL7f9HVI1GlMtixaB5Nk-bztx6mcezHtcI033N8qSaJ54bvklwtBrxXdy3BJaQnbymzDZNYisaN1KBAXYY5vO9JTwW3ano7b_PAE2oX88aDnrF7ThDDi-Aj7RKVo_hFaVu1tU9A9C2r4_vP9Oy-xs6NRup_AUnOVXmtbA38YrVu_DMzCIqNlQOIa4IV096zXl3lMrmGNM0h3JF6rHYOnzaFxppzxsig29XiCa_JB5Dq-CuJlh3odBNnpM_c6Us2O-HXBaEt0s0nexjuCVl1wUKz9NILA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ:ایالات متحده به دنبال تمدید یادداشت تفاهم با ایران نیست.
ایران در مخمصه‌ای بزرگ گرفتار شده است. وضعیت کشورشان آشفته و نابسامان است.
ارتش آن‌ها به‌طور کامل شکست خورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/70208" target="_blank">📅 22:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70207">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ae2f33929.mp4?token=DVuX_4YHXwCc-kcX9wtKN21z5JpU_iwBWrIwsmHVHAj4rn9LvmbnbiP2Cu7VvzorWDXgmXiJ_RZEdXHl10OShOdUnetb0uZNp1qCV2Aa5EojPzHElh_xUe7kR6bH7XX1sO4BjzlpYVvdaNt2Vz2dLd1p3oelsusVJqQRrH3WntFvCy3JOd2ireM6ok8YDDW9J0aM8URdkqSuxZ_ToVzaUJH9xD30Gaj83Opdb9OuP4o96Y982CVfNAXWtX3hD6H2-HLozP7d8igraQ0OtwzC2IW0BZjgPDQBzbkZFtojsAvZpFwWrihD4rMGSxZ8ikaCSVX_EiWglbfkGBYqXY0JRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ae2f33929.mp4?token=DVuX_4YHXwCc-kcX9wtKN21z5JpU_iwBWrIwsmHVHAj4rn9LvmbnbiP2Cu7VvzorWDXgmXiJ_RZEdXHl10OShOdUnetb0uZNp1qCV2Aa5EojPzHElh_xUe7kR6bH7XX1sO4BjzlpYVvdaNt2Vz2dLd1p3oelsusVJqQRrH3WntFvCy3JOd2ireM6ok8YDDW9J0aM8URdkqSuxZ_ToVzaUJH9xD30Gaj83Opdb9OuP4o96Y982CVfNAXWtX3hD6H2-HLozP7d8igraQ0OtwzC2IW0BZjgPDQBzbkZFtojsAvZpFwWrihD4rMGSxZ8ikaCSVX_EiWglbfkGBYqXY0JRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: شما گفتید اگر عمان مانع بازگشایی تنگه هرمز شود، آنجا را به شدت بمباران خواهید کرد. آیا می‌توان گفت که صبرتان در قبال عمان — که یک شریک راهبردی است — لبریز شده است؟
⏺
🇺🇸
ترامپ: فکر نمی‌کنم رفتارشان خیلی خوب بوده باشد، اما ما خیلی راحت از پسِ آن‌ها برمی‌آییم؛ درست مثل کارهای دیگر.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/70207" target="_blank">📅 21:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70206">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9810e545.mp4?token=Z10WHANRq2hOQIq6tCjRQL3i2CzUDLKy3yj3Y5J3C1PwuirB_jz4Kxd4QbeFF645NFWtfALNRT6807Oi_2qjmAEsFF8NtfT_AuQLcHTxUX0SdBJaNI38uf3tFHbL37nasJJFEQo3pw4i9z5OsELF8ECBfHNT4hciZ7bqbwVKM817CPxh4nQKFBuiSqMjmZzo7rG-Dt-AQ1oNHlWtCQ7j9eQ1PoSVX3k-Inw6isfwIsopXIMD0UGFiS0cx2XxBslsaM5ODPVhHc5RjDgKY0spDQG6RiHgYxY9MJATBbOxduj4i1EcRAYNHHXlNDXuVjtJ32-YOuMRDiOpTS5FXSj_qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9810e545.mp4?token=Z10WHANRq2hOQIq6tCjRQL3i2CzUDLKy3yj3Y5J3C1PwuirB_jz4Kxd4QbeFF645NFWtfALNRT6807Oi_2qjmAEsFF8NtfT_AuQLcHTxUX0SdBJaNI38uf3tFHbL37nasJJFEQo3pw4i9z5OsELF8ECBfHNT4hciZ7bqbwVKM817CPxh4nQKFBuiSqMjmZzo7rG-Dt-AQ1oNHlWtCQ7j9eQ1PoSVX3k-Inw6isfwIsopXIMD0UGFiS0cx2XxBslsaM5ODPVhHc5RjDgKY0spDQG6RiHgYxY9MJATBbOxduj4i1EcRAYNHHXlNDXuVjtJ32-YOuMRDiOpTS5FXSj_qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: اعتبار تفاهم‌نامه امروز به پایان می‌رسد. آیا به دستیابی به توافق با ایران نزدیک‌تر شده‌اید؟
🇺🇸
ترامپ: بیایید ابتدا کارمان را با رایدر  تمام کنیم؛ بعد که تمام شد، به چند تا از آن سؤال‌ها پاسخ می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/70206" target="_blank">📅 21:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70205">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4e1ff391.mp4?token=mDfjr-Un_zN7JC7D27Ia9j5bS58kl0k433OPkbKz0aDXrOyb3vvGSLOa9UdynONXObchvYNVJnZ0h172lWS3VVXuUlWngwUqODVzPOfUIPLOby69O4XKM-L1oF22le1syUytsl4V4z_xt7pEUIBUYIfmTaFkhf5cAClpIWJ_vooVwG66OWAexGbH700SCHbqhCX12jLjfA0H14fojy93FJhNjItWTwD74dJXbrHORde7jdTl3edLSodnaSS1YhTjBMiKaqIA5TahgjRNOlbLZsVHCMBqJDZN4PnHFfY-bEawGKcUhV8lWcQrdLp3OM7fquyNSFQzmefqsWnNRgHsaC6TXu1vpDNIyucwCXrlNpUVHYislUJMV8oWO608vLIUhnsy4sbKqpuXvWFFubaClNyO2zBSVgGhN3knk7dMtW8HBBckS5jfbcvtyCEmRFnESSrqGJbbeJAvbenoTCU2zq8nNjUmPsda0FRJgJEcQYdUTsU_9YG_LDC__thbNKRuJfa7B-_YSvL7O0ezlOLCF4eT43ohNonuRnFZRBZvVYgDXhIILwL3GiOz1I9RnqTe037Pw3E7e9kw8NFZm4F-KT1uDm5yNT3rGkz-2Lt8xHoIHbt56P9WyA2WFYiynPuvWJTMhCH1Mx77HmW5DSFOkhvEwTGsp3xiMWBUhtlFWDs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4e1ff391.mp4?token=mDfjr-Un_zN7JC7D27Ia9j5bS58kl0k433OPkbKz0aDXrOyb3vvGSLOa9UdynONXObchvYNVJnZ0h172lWS3VVXuUlWngwUqODVzPOfUIPLOby69O4XKM-L1oF22le1syUytsl4V4z_xt7pEUIBUYIfmTaFkhf5cAClpIWJ_vooVwG66OWAexGbH700SCHbqhCX12jLjfA0H14fojy93FJhNjItWTwD74dJXbrHORde7jdTl3edLSodnaSS1YhTjBMiKaqIA5TahgjRNOlbLZsVHCMBqJDZN4PnHFfY-bEawGKcUhV8lWcQrdLp3OM7fquyNSFQzmefqsWnNRgHsaC6TXu1vpDNIyucwCXrlNpUVHYislUJMV8oWO608vLIUhnsy4sbKqpuXvWFFubaClNyO2zBSVgGhN3knk7dMtW8HBBckS5jfbcvtyCEmRFnESSrqGJbbeJAvbenoTCU2zq8nNjUmPsda0FRJgJEcQYdUTsU_9YG_LDC__thbNKRuJfa7B-_YSvL7O0ezlOLCF4eT43ohNonuRnFZRBZvVYgDXhIILwL3GiOz1I9RnqTe037Pw3E7e9kw8NFZm4F-KT1uDm5yNT3rGkz-2Lt8xHoIHbt56P9WyA2WFYiynPuvWJTMhCH1Mx77HmW5DSFOkhvEwTGsp3xiMWBUhtlFWDs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دختره ول‌کن رامین‌رضاییان نیست و یه ویدیو پر کرده و حسابی گرفته رو رامین:
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/70205" target="_blank">📅 21:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70204">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/485f8430bb.mp4?token=jtjCOxZyLjoLHogTCOPGHE5buXC_yHh0wAXrZ_yohmsWlyBdjnD6VsHhabg0EzEQVRNvEL27Ku_hjsSbngt0PszMMT8VOwNxFNXRHfjvvLxtkt6TjLy9iVE6VitTlmY53aWbmI-saBVKXRbZn9XnHTJGduOH0zyF-4iX6LByXNo77evB1qOvM5lctXrsiE_5RRKjhQn4oH58ZYUN5O8FanHEVGZHLOq9VYEH06hlxKycag_UIaqPfGl8CNVoo1Ruzx2ajx4fYNJ5mDws8Of_mCFgi6YLEgpTHEkuyzkhcNBC74weySNDemXHNMEpLdL-DLxSa7zPogsLyC2D67s-rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/485f8430bb.mp4?token=jtjCOxZyLjoLHogTCOPGHE5buXC_yHh0wAXrZ_yohmsWlyBdjnD6VsHhabg0EzEQVRNvEL27Ku_hjsSbngt0PszMMT8VOwNxFNXRHfjvvLxtkt6TjLy9iVE6VitTlmY53aWbmI-saBVKXRbZn9XnHTJGduOH0zyF-4iX6LByXNo77evB1qOvM5lctXrsiE_5RRKjhQn4oH58ZYUN5O8FanHEVGZHLOq9VYEH06hlxKycag_UIaqPfGl8CNVoo1Ruzx2ajx4fYNJ5mDws8Of_mCFgi6YLEgpTHEkuyzkhcNBC74weySNDemXHNMEpLdL-DLxSa7zPogsLyC2D67s-rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
صداوسیما اومده یه برنامه ساخته به اسم«با عرض معذرت»که محتواش تمسخر ترامپ و کابینه دولتش هست و قراره از اواخر مردادماه پخش بشه
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70204" target="_blank">📅 20:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70203">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🇮🇷
فارس:
یک نفتکش اماراتی در نزدیکی قشم توقیف شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70203" target="_blank">📅 20:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70202">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf270f369e.mp4?token=P20GQhhapPj7ku-6Z70t1FZ5PtKFi82l69omDfsXa5tThAULkhFS2bYfB2qtJ2g7yRYCvhIMRg3G_Hfoq3oROmvMdSZlsdkRMBxagOYc9JbtNVycYZ0ndhUOYTR2__BZcPfN_cov9dnfuq6TIrnLHpzSwac3GE9DafFWxu_ybPfMv0EFUFWxMw4PPQ-hTSU9HKBo0EWK1XT8Yq1hMTVgVDO6cAIJrkgMbXuwfOBRr8BVjtD8ghgo0tSqixiAcrDZyquj1qj254oTDLT4-n2X7GXSAo4DbaFEGtZvD-YxvrrA5HjMKCIZ-hrpACc_NuksaUq5e72Zue_2rNxOngCMyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf270f369e.mp4?token=P20GQhhapPj7ku-6Z70t1FZ5PtKFi82l69omDfsXa5tThAULkhFS2bYfB2qtJ2g7yRYCvhIMRg3G_Hfoq3oROmvMdSZlsdkRMBxagOYc9JbtNVycYZ0ndhUOYTR2__BZcPfN_cov9dnfuq6TIrnLHpzSwac3GE9DafFWxu_ybPfMv0EFUFWxMw4PPQ-hTSU9HKBo0EWK1XT8Yq1hMTVgVDO6cAIJrkgMbXuwfOBRr8BVjtD8ghgo0tSqixiAcrDZyquj1qj254oTDLT4-n2X7GXSAo4DbaFEGtZvD-YxvrrA5HjMKCIZ-hrpACc_NuksaUq5e72Zue_2rNxOngCMyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
جمهوری اسلامی، شروع کرده هر کسی که جاوید شاه میگه یا به مسئولین توهین می‌کنه رو بازداشت کردن!
یه نفرو دستگیر کردن، حالا جرمش چی بوده؟ توی کامنت اینستا به مسئولین فحش داده
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70202" target="_blank">📅 20:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70200">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BEzSvxnynKCMxgLjD-0G78KxBuNnoEqxIMZJ8rV4HiUvp1mpU_hRiXxL2PGxIXobZvb1QESt1SF8g9b_eJm6nrRjdvKkCuAXNHh24LAEdjMVVgtdibFkUMEH8FGah4kCMom5eCGe9OO34N2G9P2DIBCKuMz0gBiTzpbaV6MVkQN2Mbfzhf5nIeji2uLE6KcdKTCOFTZH7jzFFxPCipSiHbkxoSlfBYe3X7Uioqer1qicEQ4y7ooKdyxFK3JMU-iLN7Ploxd2At8I7X4bGn-F7_RPiQAsrCxDPM6ataSFc2m37XvZBsQi9xOo4xuWkxROrQJYpuszUvYBG984boU-Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MPh1MHakvyStxjzvwpHBXnfpfQ9P-gcS-ZgsDAkrK_uLVig9-Z50JU3pO_V4zcKDVPSrjHFK-t4Fn6TG1QFHCqZEAOvTaWXJtc9Qt0FR29GMddAy26-D9MvVK91WuxluthTcg8qMQ1oMDieIgBOLi0nFpa70uQ6-h5CY3zaYZYDA9TK_dlI198ojdxjxS88zDUSofzspTG-w55XcsZafwQPQn8q0-rYB92TDe6GJ1Ym1WlaLfNKFqpnsR1_HfBr2xx7bFTd1C8JgcgqJnkxjZOTCI9mFtGt4Gog__C20mnynmBOCNrNtNJxQcCZMTUhHFZIJ-gN50qFHMIunIFVK_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
استوری های جدید گوهر فرشاد و افشاگری های جدید از رامین
رضاییان
:
جول فرشاد: رامین ازم میخواست تیری سام بزنیم.
رامین ازم درخواست محتوای جنسی میکرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70200" target="_blank">📅 19:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70199">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7157f499e9.mp4?token=nEt9Lga63qgLx2rnGaUCMZ1srOXCQpm6IKEV7wKgqZZoqPE44GIlKmg1_YENM3oKgP070kDOHEGaptWt89NPYBTQc-IGfDQYbGILaCeqLnBzajhuQ3n8wnafIzs6JZog-23BG0KD588kT8Ur8rN2EmixFRPculql8WjSeG-fBSU1Emmkkj4v3m9fkQETQXLfo6hoYls0gLUsGfzRTXv62kMro0WWowGRby0ECczwXLZ81PP9g_vLRKwhYIZVcJd0-f_r7BSo38JTVNwZSfUyCrD404RINrrPBjZM9RvsWGTAM27a-B8SiKORe9kJHBcKPbtua8VDKsolG9cxQPhURA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7157f499e9.mp4?token=nEt9Lga63qgLx2rnGaUCMZ1srOXCQpm6IKEV7wKgqZZoqPE44GIlKmg1_YENM3oKgP070kDOHEGaptWt89NPYBTQc-IGfDQYbGILaCeqLnBzajhuQ3n8wnafIzs6JZog-23BG0KD588kT8Ur8rN2EmixFRPculql8WjSeG-fBSU1Emmkkj4v3m9fkQETQXLfo6hoYls0gLUsGfzRTXv62kMro0WWowGRby0ECczwXLZ81PP9g_vLRKwhYIZVcJd0-f_r7BSo38JTVNwZSfUyCrD404RINrrPBjZM9RvsWGTAM27a-B8SiKORe9kJHBcKPbtua8VDKsolG9cxQPhURA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
فرمانده کل ارتش:
«اخراج ایالات متحده محقق شده است و آن‌ها دیگر اجازه ورود به خلیج فارس، دریای عمان و تنگه هرمز را ندارند. همگان باید بدانند که پایگاه‌های آمریکا به هیچ وجه قادر به بازگشت به وضعیت پیشین خود نیستند و ایران هرگز اجازه چنین اتفاقی را نخواهد داد.
تنگه هرمزِ مقدس، یک ظرفیت ژئوپلیتیکِ خدادادی برای ملت ایران است و این اهرم قدرت هرگز به وضعیت سابق بازنخواهد گشت. یکی از میراث‌های رئیس‌جمهور آمریکا، فعال‌سازی همین ظرفیتِ تنگه هرمز بود.
ما از وجود این ظرفیت آگاه بودیم، اما بدون این نبرد، آن ظرفیت فعال نمی‌شد. هر هزینه‌ای که در این مسیر متحمل شویم ارزشمند است و ما تحت فرمان فرماندهی معظم کل قوا، با تمام توان از این ظرفیت حراست خواهیم کرد. این اهرم قدرت، یکی از پیش‌شرط‌های پایان دادن به جنگ به گونه‌ای است که سایه جنگ را از سر ایران دور کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70199" target="_blank">📅 18:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70198">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">معتبرترین سایت بین المللی شرط بندی که به ایرانیا خدمات میده
✅
وقتش رسیده قید سایتا ایرانی بزنی و توی سایت بین المللی فعالیت کنی
⚠️
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70198" target="_blank">📅 18:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70197">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRnK7o6RJ4mUFtyKhdXxJDnh4IqSu2d3Qj5WojqbsbNLAckhkzqT4PgRB0Fi9ZzJJrvMpLYnKXn8cpAuZKTumkO3uQNvNdAwy8QGMoUoLGKNLuvNg3i1xc5SGCBu-APdvkHisIFqHrROsDYT8I3u49N3sxag5Zdnf8Zx9TXXBRc1TCbSEOCLI6idRr24HD4KnFK-DldDo7_cyno6Ji4ejnGOClfTMn3ByHYCIZ8Ot_Bt1TXP9-vJrauxNLzIBd73IIco_ShFYZ7BJz8CJUfh76cHgtQA-dsBS1tfOalWdjvqUCMM925_QSuYKr-tQQ8uDnSFwUZ_MS1OkbPYcm-Pfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g26
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70197" target="_blank">📅 18:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70196">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYqSglVq2G_DUzOVI6wstw-vpBkYBhPyvvQwECF9ljBZ3dGJdT4duDqtk3av_rC-YpwYJ_nD4XHuQAIEPsoOJdh8lU5bYgDjLhrZ4BOkQBYQXpBXtFbko-Y7iI13uzHpafY5Xzqtzof2ZhY2mZeqgPMn6UDX0A263YlNImDvyWgWaHJyzpfXDgnGvqq8f2F7098SF95H8Bm1c_vQWyxaTYu4ZuF1SetbRtTDKbBzvQDv87_IhMq6pVpU6vtdI-1HR2dfRLSdomJAqk6fJUlRoK6XyULy2Rpsos13JVkGgXPxidahPzUoUjyjDfQNgDXEAsllmXrSIsFBQvdoYGKHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
رویترز: ضرب‌الاجل ایران به ایالات متحده؛
ایران به ایالات متحده اولتیماتوم داده است؛ یا به دیپلماسی جدی بازگردید و محاصره دریایی را لغو کنید، و یا با گسترش دامنه جنگ مواجه خواهید شد.
به گزارش رویترز، این ضرب‌الاجل — که گفته می‌شود حداکثر چند هفته مهلت دارد — از طریق پاکستان و قطر به اطلاع ایالات متحده رسانده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70196" target="_blank">📅 18:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70195">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2af0d57a79.mp4?token=rjdOfSHpaWaV0c6xQBLOcOAb3KOa5eSRGz3fh94K9nkuFejGEaEqhAfcnQyUo0_BSPOuo9wrTdJfPrEdY3G0qiA4J9GcldCDJcidF4hiZodWCKxBBiPhT1M7Hh7haC-bM1xJkTAjBNuqxfJ9tXEjZci56QIDOMuRHh_m7u_0_sIMUFHIruZmkPB5eMMr-wKrv6FhlfvtDBC28wGWk-haPaETMxrJQjc3iOkOpTKk4geglxvBgwMg40mMNxqc_FI0uJ5SCeIY0Pqthjiw69XmUksuBxBDjENW0MCK3LM8u4ZEHdTHj8KCz_EBHwYsXkGpmD1fNfpVHzfRHsveHp_Esw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2af0d57a79.mp4?token=rjdOfSHpaWaV0c6xQBLOcOAb3KOa5eSRGz3fh94K9nkuFejGEaEqhAfcnQyUo0_BSPOuo9wrTdJfPrEdY3G0qiA4J9GcldCDJcidF4hiZodWCKxBBiPhT1M7Hh7haC-bM1xJkTAjBNuqxfJ9tXEjZci56QIDOMuRHh_m7u_0_sIMUFHIruZmkPB5eMMr-wKrv6FhlfvtDBC28wGWk-haPaETMxrJQjc3iOkOpTKk4geglxvBgwMg40mMNxqc_FI0uJ5SCeIY0Pqthjiw69XmUksuBxBDjENW0MCK3LM8u4ZEHdTHj8KCz_EBHwYsXkGpmD1fNfpVHzfRHsveHp_Esw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اخیراً عرزشی‌ها این فیلم رو با موضوع «فیلم لو رفته از نشست مجتبی خامنه‌ای و پزشکیان» به مغز نداشته بقیه عرزشیا قالب کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70195" target="_blank">📅 17:25 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
