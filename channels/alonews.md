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
<img src="https://cdn4.telesco.pe/file/HbiJPHgh8EgU2Zts0MgY4Am5A4q2lA3Bo66oN18MP6dvk6RjduTNDr4x1JVFL6jbjjY92M5zZAzlPDhzZdjCKN4mxButPQ97NweqytTZiIH6C2Vkv-WYROn_yRjkup8zVODlJfnRtfupnD2jRxExyweSO7DqxfHxphjd5t3Crn2mlrg7hUc8a1UuEy4WgiyO0DAn6SrBtujUiBlP1zRRCdHr9Eq377-2YEpqITXeSWhhR5S-LNUbNnjglzsZ3c8TMqijdVPw-M39Rsszel7u48d1WhJdiA6q4Iv79LktDSwrvILR0F2R9khLTrR-UAEaqSmhYBg5YS0Dpdc3Yd-j5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 977K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 15:00:30</div>
<hr>

<div class="tg-post" id="msg-143892">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
پزشکیان: جنگ همیشه راه‌حل عبور از مشکلات نیست
🔴
گره‌ای که می‌توان با دست باز کرد را نباید با دندان باز کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/alonews/143892" target="_blank">📅 14:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143891">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
گفتگوی وزرای خارجه قطر و عربستان درباره تحولات منطقه‌ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/alonews/143891" target="_blank">📅 14:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143890">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
تانکر ترکرز: در خلیج عمان دست‌کم ۱۵ مجموعه عملیات انتقال کشتی‌به‌کشتی (STS) در حال انجام است.
🔴
ما ۲۵ میلیون بشکه نفت خام را شمارش کرده‌ایم؛ به‌علاوه مقداری محصولات پالایش‌شده نفتی.
🔴
این نفت تقریباً از تمام کشورهای منطقه، به‌جز ایران، منشأ گرفته است.
🔴
اکنون پنج مجموعه دیگر نیز پیدا کرده‌ایم و یکی از آن‌ها مشخصاً مربوط به گاز مایع نفتی (LPG) ایران بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/alonews/143890" target="_blank">📅 14:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143889">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
امید دانا:
اختلاف «علی کریمی» و «رضا پهلوی» از اونجایی شروع شد که علی کریمی گفته بود به ازای هر اعـدامی؛ ما هم یه قرآن میسوزونیم که رضا پهلوی خیلی به اسلام اعتقاد داره و با اینکار مخالفت کرد.
هرکسی که اسلام ستیز باشه رضا پهلوی بایکوتش میکنه و بهش فشار میاره. چون میگه ما با اسلام نمیجنگیم.
🔴
رضا پهلوی خودش تا سال ۲۰۰۹ اصلا دنبال تغییر جمهوری اسلامی نبود و دنبال این بود از طریق رفسنجانی و خاتمی توی حکومت اصلاحات به وجود بیاره. مدارکش هم موجوده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/143889" target="_blank">📅 14:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143887">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L157JAKXZgAE8LHNxpUmzyBRdYVEqtZdLiomC-C1GSQ6B8jWsnKsv7g2WniuttIBDSb48hz0gGOwkogSsK8ZzKkwmoaZB6DTf82ssYygmOPN-7YM6tI2TOyIyP-CncxqIltu6z7zN6X2foPWhdrUQQS4nzIufJqa4Z8ohn4k4LSWdloDYHQd0SErb5Ks_t90M92v6c0Ay2zmAbhayYvOpL7WsWeOTn6AgwSWcIyr__-mEAWF-zDpiPJ3JzuxMAJ-IELBm0DB-JiD4kzFVUhCTa5qO6fOOnf2AZZZZL8YRL8t4H6zkRhXe502vfxWu3oJxqeGF2cdqO0GSbfypCxdMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640fdccd62.mp4?token=eA6FY_j--bqubf_WKVyqQ-n5K4tUqNgRR7rKyIje3z02REpjZi7eWTnERI1S2aWHTLAbby5G8FoYYwRBYkJQN6AK21ru1FZCMlkFNEGK-bTlu_5rQE7mBZHkCNvDJ0lLh8iz9-AZBVlNA7xZSPecjPfN4bMQADGyzARClvCH-qdQAhksJ3EWr8j8MetOrF6Pe6GJ8JLc6X49bXNwoEO0WuNQV3v2USufDRwuq9hFBSIRufoCHGE8A5cOuscfwtday0FNoGOg4-V_3DtuSvf4JOFd6Yyl18h2LFARJIuMV6F8JnDn0i61QR2_vgr0laG7wJtNZXNgB0GtOJHDqnrA5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640fdccd62.mp4?token=eA6FY_j--bqubf_WKVyqQ-n5K4tUqNgRR7rKyIje3z02REpjZi7eWTnERI1S2aWHTLAbby5G8FoYYwRBYkJQN6AK21ru1FZCMlkFNEGK-bTlu_5rQE7mBZHkCNvDJ0lLh8iz9-AZBVlNA7xZSPecjPfN4bMQADGyzARClvCH-qdQAhksJ3EWr8j8MetOrF6Pe6GJ8JLc6X49bXNwoEO0WuNQV3v2USufDRwuq9hFBSIRufoCHGE8A5cOuscfwtday0FNoGOg4-V_3DtuSvf4JOFd6Yyl18h2LFARJIuMV6F8JnDn0i61QR2_vgr0laG7wJtNZXNgB0GtOJHDqnrA5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیشب ایرج مصداقی، عضو دفتر رضا پهلوی گفت که
امید نادان (دانا) به پیچِ 14 میلیونیِ علی کریمی دسترسی داره چون کسایی که علیه امید نادان (دانا) حرف میزنن رو بلاک کرده.
🔴
حالا علی کریمی استوری گذاشته که
ایرج مدل 57، مشاور آقای رضا پهلوی؛ اگر ثابت نکنی که پیج من دست هر کسی غیر از خود من باشه، خیلی بی ناموس و پیشرفی!
24 ساعت به اقای رضا پهلوی زمان میدم که در این مورد اظهار نظر کنه، در غیر اینصورت هر اتفاقی بیفته، گردن خودش و مشاوراشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/143887" target="_blank">📅 14:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143886">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHv_O1QFY-fAd1j1TYT23F7JZQ7OhScpnL2gHMfl9r4WIusETs6L5STK0UFrZGZxPd9njHuL4pJci05je2O5H_6Ilsh6qNA162s22n6o2-JuqtkfBqwl-Dhy4Fx39cNo1g4Df0dX7ERt0lTmk8YEsRZF1nnz0mkrwQ2fRqJKqvAeYg_cb4RXtqQ2Q3S6UrytS7VRyASIMAJtr3NTlHQVmLkQNrX9z-zeVbIC5qXJJ9GPmauctIzc1EfmU44SYvf-0FYaOiPMkwLDDIYedL_SIgEVVc8hROIca74xRc_dHXItnjX8ujx2oeBp5kAL9cMeB2JEdHuy_YLYKsJMQkv58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره: به نظر می‌رسد که واشنگتن ممکن است در متقاعد کردن کشورهای همسایه برای پیوستن به تحریم‌ها علیه تهران با مشکل مواجه شود.
‏
🔴
برخی گزارش‌ها حاکی از آن است که با ۱۶ کشور هم‌مرز با ایران تماس گرفته است - ۸ کشور از این میان، دشواری قطع روابط اقتصادی خود با ایران را به دلیل منافع در هم تنیده تأیید کرده‌اند - در حالی که ۸ کشور دیگر پاسخ داده‌اند که در حال بررسی این احتمال هستند، که می‌تواند به عنوان یک امتناع مودبانه تعبیر شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/143886" target="_blank">📅 14:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143885">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
به گفته برخی منابع: به نظر می‌رسد که واشنگتن در متقاعد کردن کشورهای همسایه برای مشارکت در تحریم‌های اعمال‌شده علیه تهران، با مشکلاتی روبرو است. برخی اطلاعات نشان می‌دهد که این کشور با 16 کشور همسایه ایران در تماس بوده است:
🔴
8 کشور تأکید کرده‌اند که به دلیل وابستگی‌های اقتصادی متقابل، قطع روابط اقتصادی با ایران برای آن‌ها دشوار است.
🔴
8 کشور دیگر نیز اعلام کرده‌اند که در حال بررسی امکان این موضوع هستند، که این می‌تواند به عنوان یک رد غیرمستقیم دیپلماتیک تلقی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/143885" target="_blank">📅 14:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143884">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHC2N7YDoB5icDYjgHRBTJeqpjcF5a0nG9RWz6za9rDq6OgD5S2F0yq8ifvYZA1mOXwDQrhKyXviRqIG7z1z5YoH5C_Rqkkjf-0PbAx244m_bvRkxTYyF3y6w1ABW7IpAK5znsV50VFwGvuagK0XtWy6W2O5VGNPaXhR9XO6ITtcq6I9ozfykhhWdFEj7k9AWA_yRho8CMnzVcv_LyOErZgnVkT8MKUsOERt9-ZL_g0XyZMFIPXZRbsxv0fjnGxZ4SgIqZjkNHOrZ42OIskb_A8lAwCcVMa-0xEcxi4oDj02PVJbb3jjJuAg0RnqBoRPD6xVBNlaAwQdJp8dTLmcwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلتفرم خرید آنلاین طلا میلی‌گلد، حدود ۳۰۰ کیلوگرم کسری طلا داره، یعنی طلاها رو فروخته ولی نگه نداشته. اگر توی این پلتفرم سرمایه‌گذاری کردین حتماً سرمایتون رو از اینجا خارج کنید.
#میلی
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/143884" target="_blank">📅 14:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143883">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739904d208.mp4?token=qyq0UD7N-xMOSK-H7ISJpHuO_iUPdP3NQ-iX8GPorlvSAubhP5JayBK8fhziuDofcb1BK128FR24UtVqH2mQokA2dNlrRFA8E2SxkhPzLXTgj9v9VIoU3gK_QX16RsQOCzVzbvJ7C0cDWcH5E-4TM0BZZjbK9UydwbPwQUJnVn1oN1QHt7SDeD4lcJHO30-vUMSELOzmnp7viucx9kW1VC3m0TJ1DXiXsAO0nHt9uJwJtMDoGu6YICXFk5-VZi0Ohw7ZyW9f4v_Q5rH9c4ImAej-d0WD5rnDHHEHfe3WPMLgxLNGYYPkZf_Mpk8dcbg9mhJ--zCj6jJ8FpZFGp3qRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739904d208.mp4?token=qyq0UD7N-xMOSK-H7ISJpHuO_iUPdP3NQ-iX8GPorlvSAubhP5JayBK8fhziuDofcb1BK128FR24UtVqH2mQokA2dNlrRFA8E2SxkhPzLXTgj9v9VIoU3gK_QX16RsQOCzVzbvJ7C0cDWcH5E-4TM0BZZjbK9UydwbPwQUJnVn1oN1QHt7SDeD4lcJHO30-vUMSELOzmnp7viucx9kW1VC3m0TJ1DXiXsAO0nHt9uJwJtMDoGu6YICXFk5-VZi0Ohw7ZyW9f4v_Q5rH9c4ImAej-d0WD5rnDHHEHfe3WPMLgxLNGYYPkZf_Mpk8dcbg9mhJ--zCj6jJ8FpZFGp3qRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به نظر میاد اگه حجاب داشته باشید دیگه رقص توی خیابون مشکلی نداره
🔴
البته هرشب شاهد رقص پرچم و میله هستیم و اونم مشکلی نداره
✅
@AloNews
|</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/143883" target="_blank">📅 14:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143882">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XP0TYmwB9oiKIpDS5asKoETmMc6DrRaPIc39x1Wjpc1R4WAz7oAAnFYGSbFzSbhxqm2wNPb4Gh8PxejqeYSVI60ZQhxL2BaG4fdAcbxp8Wb5zAoAhDGPetF0vi5AmmMzdCsUa1JQ8jlC7VWr82bSIVpiyap0U9NJIql5Z76p5yCG6gvOTIroBfTSAsDxtwbjiImJgURqq6p6MPo8jtKm1U6-8WQogZZFPjFHCwmmNd_b7gGsexUO1uaMBsh-2RiWzKnLQEdThBvJ4Z1VrI7gEJKHKkvUfwJZaQyJSnIT8RUzGUV2Ku6bZiqN5zP7acPbeZEuKQWuVbJw6B0OrSgTlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
قالیباف: مذاکره با قاتلان رهبر برام افتخار نیست و برعکس برام خیلی سخت و امتحانی سنگینه
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/143882" target="_blank">📅 14:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143881">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 250 میلیون
‼️
🔴
دلار به زودی 210 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/143881" target="_blank">📅 14:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143880">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رویترز:تحقیقات آمریکایی در مورد نفوذ به داده‌های مرتبط با ایران در یک شرکت که از ابزارهای آن برای تاسیسات آب استفاده می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/143880" target="_blank">📅 13:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143879">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12f4aaba6.mp4?token=vz9cRlwRxF0lCYB_zA4MgYhKIS1tUcIDbsnKkzWlch9jYtl7uF0_7T2xwoGpk1SXgfyvHh36QE-RJYZyTnnfMBvYnlkkpOB-C16zh322zbvFQ1auOZ3HdjwZCZFtbhQpTnY9uK6lmhYnYMsH3HiE2esAP6w_vdSH5F_wpN1kGOHZHDYxlXRmyiQ9TnhLfOnKcXznEi7j6rcXy4Vxx1Ypf8tJyArlkj9osAqnp-LxnYJzky-Vk5UMO7JNk8kJLfVXRRw0A1FoObAsnWjlZzy4YspYp8uAgrbA--RKwLFyr3iIKrQMHGRJ9YwgnoiUvHNIGx3Uzkoz5iHYfVP6tFhg1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12f4aaba6.mp4?token=vz9cRlwRxF0lCYB_zA4MgYhKIS1tUcIDbsnKkzWlch9jYtl7uF0_7T2xwoGpk1SXgfyvHh36QE-RJYZyTnnfMBvYnlkkpOB-C16zh322zbvFQ1auOZ3HdjwZCZFtbhQpTnY9uK6lmhYnYMsH3HiE2esAP6w_vdSH5F_wpN1kGOHZHDYxlXRmyiQ9TnhLfOnKcXznEi7j6rcXy4Vxx1Ypf8tJyArlkj9osAqnp-LxnYJzky-Vk5UMO7JNk8kJLfVXRRw0A1FoObAsnWjlZzy4YspYp8uAgrbA--RKwLFyr3iIKrQMHGRJ9YwgnoiUvHNIGx3Uzkoz5iHYfVP6tFhg1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یکی از حامیان حکومت: ارزش دلار هر روز داره بالاتر میره و پول ما بی ارزش میشه، اما این به نفع ماست!
🔴
اون فرد خارجی بیشتر محصولات مارو میخره، در نتیجه تولید بیشتر، بیکاری کمتر و تورم مهار میشه.
#کریه_المنظر
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/143879" target="_blank">📅 13:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143878">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8a6f01648.mp4?token=g1xkRFe69V2UjlTXW1aWBdVqGkSY9-NsWxNqbedKJENF_i_gLyw1on57Q8GrDFZfM0evG_77vRaY4_zK9SSNiqCAIrPG3Kqx1EoqUEUp0FZHkjcIk9u3s2isz56j4UztqS4BcI6bjxSh3S7XmuGiwpINK1qmfwworruKJsz9irLzljCRbuewMArJNYjrGkmsWv3ve1WZoDaFZV5oa95H72kz9rN_3LxB88Tx-mtdptwiZTgl_g2Pp1LwfdwT0TEqblZfaXhDFN99rzZ3yI39Z6EzdDdmc7ydePnONBRSdIpDWHZgOXGtnEhPKEqAoQomt4RlrfwBYVhXu8eUgepKug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8a6f01648.mp4?token=g1xkRFe69V2UjlTXW1aWBdVqGkSY9-NsWxNqbedKJENF_i_gLyw1on57Q8GrDFZfM0evG_77vRaY4_zK9SSNiqCAIrPG3Kqx1EoqUEUp0FZHkjcIk9u3s2isz56j4UztqS4BcI6bjxSh3S7XmuGiwpINK1qmfwworruKJsz9irLzljCRbuewMArJNYjrGkmsWv3ve1WZoDaFZV5oa95H72kz9rN_3LxB88Tx-mtdptwiZTgl_g2Pp1LwfdwT0TEqblZfaXhDFN99rzZ3yI39Z6EzdDdmc7ydePnONBRSdIpDWHZgOXGtnEhPKEqAoQomt4RlrfwBYVhXu8eUgepKug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فریاد «مرگ بر آمریکا و مرگ بر اسرائیل» در نشست علنی امروز مجلس!
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/143878" target="_blank">📅 13:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143877">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
قالیباف: مذاکره در نگاه این جانب، نه ارزش ذاتی دارد و نه تابو است؛ نه مطلقاً خیر است و نه مطلقاً شر. مذاکره هنگامی معنا می‌یابد که ابزار پیشبرد منافع ملی، احقاق حقوق ملت، رفع ظلم و تثبیت دستاوردهای مقاومت باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/143877" target="_blank">📅 13:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143876">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
پولیتیکو: جنگ ایران ذخایر تسلیحاتی آمریکا را تحت فشار گذاشته و استرالیا نگران شده است
🔴
به گزارش فرارو به نقل از پولیتیکو، کاهش ذخایر مهمات آمریکا در پی جنگ با ایران، نگرانی‌هایی را در استرالیا ایجاد کرده که برای دفاع از خود وابستگی زیادی به تسلیحات آمریکایی دارد.
🔴
کانبرا برای کاهش این وابستگی، برنامه ساخت صنایع موشکی داخلی را سرعت بخشیده و قرار است تولید محلی موشک‌های Naval Strike و Joint Strike از سال ۲۰۲۷ آغاز شود.
🔴
منتقدان اما می‌گویند استرالیا برای ایجاد توان تولید داخلی بسیار کند عمل کرده و همچنان به‌شدت به زنجیره تأمین تسلیحات آمریکا وابسته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/143876" target="_blank">📅 13:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143875">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ry3mHCcVJPERGpr9pee_GCv11k_jF-ZPmR7DKbJBuU-S0KtJ-MC0uY2FQAM7bzXbK-y_9u3u2h6bYyGiGB31TzoPHPINH_ixT3UJy1CF0zk8dCg7jrD4k2cdug6V1CwE0OlJUPM96y_ggdv4kJqjR7604lk1pwLwGmrqbcElp4mea1b9DvSvvcI9rpp2SO4SlYFp930Svq77CAR5j6vU_ooZcYHrAzMrUwZ3bczCo3bAFUFNXINbYdxRRZ3esoFR2FLuxWGmIhkFauOGuuSGsVAvlBcrOKws_eVlh2nsndQlPUn4D4bETKEfk8vLCawWGi1eUaIsUJhv6EVh3P4I2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله علی کریمی به طرفداران پهلوی
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/143875" target="_blank">📅 13:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143874">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=gqIiKcSj-RMa22PtLi_wnFCb7vEYK3R4jnHNAh28u6A8TgVGJF223RGCqhfjPN7MqjHB1H_QMMOb4TnwzPpqxkmOQBaWqTnMvqqXnXs_AxYUeWn5eo2oW4jTEkNPkV5uQX-IxaFYkxZoANSMfOPGimIJEVkZ3lNumIeapct5pHr4hoG1Lawpmuih-fK92sRSKFyUFXD4dhjMc3wBN8CUKa2IrofZc1LBNFBdras0AwoBsPb6LEEV9LJfjRb25cu14oi0RLMPsXVD5fPXmXAgO7hXGLZvh2neJ7uE_qWNVG-qfvHUxFpq-p1VIShoXTLVPtzEK0ITlm43Q0PlKqWwgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=gqIiKcSj-RMa22PtLi_wnFCb7vEYK3R4jnHNAh28u6A8TgVGJF223RGCqhfjPN7MqjHB1H_QMMOb4TnwzPpqxkmOQBaWqTnMvqqXnXs_AxYUeWn5eo2oW4jTEkNPkV5uQX-IxaFYkxZoANSMfOPGimIJEVkZ3lNumIeapct5pHr4hoG1Lawpmuih-fK92sRSKFyUFXD4dhjMc3wBN8CUKa2IrofZc1LBNFBdras0AwoBsPb6LEEV9LJfjRb25cu14oi0RLMPsXVD5fPXmXAgO7hXGLZvh2neJ7uE_qWNVG-qfvHUxFpq-p1VIShoXTLVPtzEK0ITlm43Q0PlKqWwgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداوسیما: تو جنگ اخیر ۱۰تا ژنرال اسرائیلی رو کشتیم اما به دلایل امنیتی خبرش رو نگفتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/143874" target="_blank">📅 13:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143873">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKHoBDMvLaBiTFLcuG9stGZ12BisB8T22WjccnLSkGNL21K6lbaINdLMEGKRvr732tXnGD4tVOoXYsurby3mQoLCWlInRDUm5VT4F5-bccNLHC70Udc074yzVgyTiB_zhwNCaNw3q5YvTTAwDYurLbT2fFU8UPxfms4937X39MF91OOLS5lazgxvh4H_ge8XJjjXqawSxr1-6KOcTInCJJqKpnWmYxhw4V-t8oWgd4ZK4ved26ccSUI2aENgmW_PbhkEC_U0JWrmxPMmi9jiezu3lcjMxEEzB-G7JOswyZOzwf-eF-v1mS_xl0C5qTI79lWn8OcXbUuljij8JRtnqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
بلومبرگ: به گزارش‌ها، آتش‌بس بین آمریکا و ایران در حال نزدیک شدن است
‏
🔴
بر اساس گزارش خبری که به منابع نظامی پاکستان و ایران استناد می‌کند، آمریکا و ایران به توافقی برای آتش‌بس دست یافته‌اند و انتظار می‌رود در روزهای آینده این موضوع اعلام شود.
‏
🔴
این توافق گزارش شده، شامل آزادی تردد در تنگه هرمز و از سرگیری مذاکرات تحت "مذکر اسلام‌آباد" است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/143873" target="_blank">📅 13:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143872">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
پزشکیان: بنای ما تفاهم و حل مسائل از طریق تعامل و مذاکره است
🔴
با تمهیداتی که بخش‌های اقتصادی دولت پیش‌بینی کرده، آمریکا کاری از پیش نخواهد برد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/143872" target="_blank">📅 13:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143871">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
قالیباف در دیدار با رئیس شورای عالی قضایی عراق: آمریکایی‌ها به وضوح شکست خوردند و همه دنیا بر این موضوع صحه گذاشتند؛ آن‌ها در اقدامات اقتصادی نیز شکست خواهند خورد
🔴
اگر اسرائیل در جنگ با ایران موفق می‌شد، به سراغ سایر کشورها می‌رفت
🔴
ایران در نظم منطقه‌ای می‌تواند نقش تعیین کننده‌ای داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/143871" target="_blank">📅 13:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143870">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
بلومبرگ: فشار اقتصادی ایالات متحده بر ایران، تأمین انرژی ترکیه را تهدید می‌کند. ایران در سال گذشته حدود ۱۳ درصد از گاز طبیعی ترکیه (۷.۷ میلیارد متر مکعب) را تأمین کرد و پس از روسیه، آذربایجان و ایالات متحده، در رتبه چهارم قرار گرفت.
🔴
وزیر خزانه‌داری، بسنت، از مجازات‌های اقتصادی برای تجارت با ایران پس از یک مهلت نامشخص هشدار داد و اشاره کرد که ترامپ با رهبران، احتمالاً از جمله اردوغان، در تماس است. تحلیلگران پیش‌بینی می‌کنند که ترکیه برای تضمین معاملات F-35/F-16 پیش از سفر اردوغان به واشنگتن، با ایالات متحده همسو خواهد شد.
🔴
اگر گاز ایران قطع شود، ترکیه واردات LNG (از جمله از ایالات متحده) را افزایش می‌دهد، تولید داخلی ساکارا را تقویت می‌کند و از تأمین جدید آذربایجانی از سال ۲۰۲۹ استفاده خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/143870" target="_blank">📅 13:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143869">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
بر اساس گزارش Reuters، صادرات گاز طبیعی مایع (LNG) قطر به دلیل مسدود شدن تنگه هرمز به‌شدت کاهش یافته و افت آن به حدود ٩٩ درصد رسیده است.
🔴
قطر تاکنون حدود ٢۴ میلیارد دلار از درآمد حاصل از فروش گاز را از دست داده است؛ در همین حال، افزایش صادرات LNG از ایالات متحده تا حدودی این کاهش را جبران کرده است.
🔴
هم‌زمان، ذخایر گاز در تأسیسات ذخیره‌سازی اروپا در پایین‌ترین سطح خود برای این مقطع از سال قرار دارند و این وضعیت خطر افزایش ناگهانی قیمت گاز پیش از آغاز فصل زمستان را افزایش داده‌است
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/143869" target="_blank">📅 13:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143868">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">امروز ۴تا تخم مرغ و یه سوسیس گرفتم ۵۰۰تومن و کلی خوشحالم
[اگه ناراحت باشم اعدامم میکنن]
🐸
🕺
🐸
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/143868" target="_blank">📅 12:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143867">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سخنگوی دولت: از من خواسته شد که پوششم را تغییر بدهم و چادر بپوشم، گفتم که حاضر نیستم و چادر سر نمی کنم!
🔴
از زمان دبیرستان روشنگر بودم و چادر اجباری بود و سر می‌کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/143867" target="_blank">📅 12:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143866">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1e3e3b651.mp4?token=YpmeysorVxQ3PdGjj7qfBZmhYFt-L17eS5Ot-rN3uUlKygP1kSBD5HEX0gOMEm9faDhJp7-FfMvDzpnaU_WLXXu_rPb7eW4ejc2PJ44hpmBZG5hAgCtaGYSNm9tG8fgwn2NH8a3E_pwTd3TWn0VyeUsOLmhcWGN1qCjk5W6VYnP8SHLS3Z47RkKdqzM9obvt6cJS_BR-p7x4T2-jroDRgx45tnEJHa8miNSMgaysFwHVLpQeDMbkjDVxPOPLuKiT-gMNu8iBQ1FwjdyT4zA_osMNGyzOM2SgxMUWYPvNDhHZHQSaa1F13u9YnwqZXg7k7YS67PuF-KCx9LooihsYbw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1e3e3b651.mp4?token=YpmeysorVxQ3PdGjj7qfBZmhYFt-L17eS5Ot-rN3uUlKygP1kSBD5HEX0gOMEm9faDhJp7-FfMvDzpnaU_WLXXu_rPb7eW4ejc2PJ44hpmBZG5hAgCtaGYSNm9tG8fgwn2NH8a3E_pwTd3TWn0VyeUsOLmhcWGN1qCjk5W6VYnP8SHLS3Z47RkKdqzM9obvt6cJS_BR-p7x4T2-jroDRgx45tnEJHa8miNSMgaysFwHVLpQeDMbkjDVxPOPLuKiT-gMNu8iBQ1FwjdyT4zA_osMNGyzOM2SgxMUWYPvNDhHZHQSaa1F13u9YnwqZXg7k7YS67PuF-KCx9LooihsYbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی دولت: از من خواسته شد که پوششم را تغییر بدهم و چادر بپوشم، گفتم که حاضر نیستم و چادر سر نمی کنم!
🔴
از زمان دبیرستان روشنگر بودم و چادر اجباری بود و سر می‌کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/143866" target="_blank">📅 12:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143865">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
همه کافه‌های پایین مجتمع ونک‌پارک امروز پلمب شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/143865" target="_blank">📅 12:51 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143864">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سخنگوی دولت:‌ مردم منتظر بهتر شدن وضع اقتصاد در سال آینده نباشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/143864" target="_blank">📅 12:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143862">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iiARmOUbJJ35kHVE6kGGbJU0tbditsvIBHYHlNSdJH0VOwAXlUQLRw-ysWC__jzDIGu2jBXk4sHAD4Gl9RZr7OCANfDKK24tEsTxNDLpDPY47Wf8_r_7gAUmFWwVCBOk2z4dY_qX3HkJaNDXaM3R6eaSdT449eSwvG9lP9XZDYruC-XdzzFfe4ZEX4y6EZaWZSldiSM2FLFigjS-CG_5mNODrcIMpRqYTwD_gwQ_6Ez89tSs5OruuZ2dkbEU0KiednQvqT1POOFN9Pt_QfEg5q9dI_-2sjJJ-_AUkn5qMAh1pZJKAa3DPelIezMfiLylRty-rxHEIgxLF_kyElMsfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c46o6oc7-7SqgSjS8rOiCIqyT1uQp9R_SmqytEKcvJZLRKBv2TZ081nNkJMRpxozj7dNtaOeQTtb99IkA7tUSXYWfzdRHX-siuSe16f2CNEgkqSIID7C5N6Wqhb8RIJcn4Y2gM0IHvVupBrXYiuUqk7tMsz3FI9IqGChp_dEtV6v-FkFv4ZzZ-40eASWaGJcEEzL1YAdTJQpWnfsIR8CjKpP0jetDrNCHr0tSGN7rm2coT14BA8cBg0Ki7-aURc3HvEnlYIFImrHXX0gnoeipa1h8KGpNx1XdwEaxf_mmR3ISaine8l2E_o5Fr1RQJPzLKOsX3PTtAX9ptDy1nNtBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
فوری/دولت ایالات متحده ویزای هادی چوپان رو به دلایل نامعلوم صادر نکرد
🔴
چادی در مسترالمپیا غایب است
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/143862" target="_blank">📅 12:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143861">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
نتانیاهو درباره ایران: می‌خواهم به شما بگویم: هنوز چالش‌های پیش رو داریم.
🔴
چالش ایران به پایان نرسیده است.
🔴
ما همچنین باید چالش در غزه، در لبنان و در سایر عرصه‌ها را به اتمام برسانیم و برای انجام آن عزم راسخ داریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/143861" target="_blank">📅 12:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143860">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17ef710e9.mp4?token=AJ7evRMs-YF83rE2D0iXBAoQzAvHAth3KO-EU187SSgjWqiI86gQxU2RXh20PGfnXekqSQ_dNppjuq6DvD_20CfSQWJ4r4shylRfp6gl4NPOG_Bd94QG2LZHfWOeZQjtkxSdqqi1lbMW_sIsB6jDb-xn7Bl3tBSWMS090awo2_gNcF5x0gfLAe9aLngxD4tnPTqY03EZUnC4lylXqhgSfFznKH1tXWulC7dyIxWI1DMwB0oVR15ZXAvn7lmUXsevwPBgy35B6Txtmf8A3gy_NMKlI0tcyOTM2ff0jsNtC8RWkPNVVACPANAzDsTonywCMNMH-8Rv-T4wWeeDxKMd_wddJYdo_eO0Iam5gdeAPofaZrLS0Oh8TbMl1sDaubWKx92bc-H2iGaIFT8sTJhx7NfwBeNLn6_QewmekwSmjM9HEVW2CieWeTYYxO5zVGCVxCxCmqRZZX48ygowghNkNDS-WzOdWYEVrt-xdTtl1Bi2b5aVqXv8mHY1wTG_Z6ImNujZuLIbzYCBmbmbQunWcl5S5Ii6gJf5JhSNa7pqgZ9EffWwZHh7RP-osKcvGYGqJozKhK5FCLpGpt-cz18Tz5-VIDDOzvIG7MQxyQe2Yv8rY-Kf4t4dIrStDuhXFn-wpdm6usrDhVzu-pLPHg5vL7c78Fwoy-5aW9lDcXZbqMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17ef710e9.mp4?token=AJ7evRMs-YF83rE2D0iXBAoQzAvHAth3KO-EU187SSgjWqiI86gQxU2RXh20PGfnXekqSQ_dNppjuq6DvD_20CfSQWJ4r4shylRfp6gl4NPOG_Bd94QG2LZHfWOeZQjtkxSdqqi1lbMW_sIsB6jDb-xn7Bl3tBSWMS090awo2_gNcF5x0gfLAe9aLngxD4tnPTqY03EZUnC4lylXqhgSfFznKH1tXWulC7dyIxWI1DMwB0oVR15ZXAvn7lmUXsevwPBgy35B6Txtmf8A3gy_NMKlI0tcyOTM2ff0jsNtC8RWkPNVVACPANAzDsTonywCMNMH-8Rv-T4wWeeDxKMd_wddJYdo_eO0Iam5gdeAPofaZrLS0Oh8TbMl1sDaubWKx92bc-H2iGaIFT8sTJhx7NfwBeNLn6_QewmekwSmjM9HEVW2CieWeTYYxO5zVGCVxCxCmqRZZX48ygowghNkNDS-WzOdWYEVrt-xdTtl1Bi2b5aVqXv8mHY1wTG_Z6ImNujZuLIbzYCBmbmbQunWcl5S5Ii6gJf5JhSNa7pqgZ9EffWwZHh7RP-osKcvGYGqJozKhK5FCLpGpt-cz18Tz5-VIDDOzvIG7MQxyQe2Yv8rY-Kf4t4dIrStDuhXFn-wpdm6usrDhVzu-pLPHg5vL7c78Fwoy-5aW9lDcXZbqMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو درباره ایران: و من به ترامپ گفتم که یک امکان سوم نیز وجود دارد: تشدید محاصره.
🔴
دیروز، او این تصمیم را به‌شدت، بسیار، بسیار، بسیار قوی تأیید کرد.
🔴
آنچه رئیس‌جمهور ترامپ دیروز انجام داد، تشدید محاصره علیه ایران بود — نه با تشدید محاصره خود ایران، بلکه با تشدید محاصره علیه کسانی که به این رژیم، این دیکتاتوری وحشتناک، کمک می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/143860" target="_blank">📅 12:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143859">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
نتانیاهو درباره ایران: به ترامپ گفتم: یکی از احتمالات، البته، این است که با ایران به توافق برسید — یک توافق خوب. ما اعتراضی به این موضوع نداریم.
🔴
فقط شک دارم که آیا می‌توانید با آن گروه آنجا، با آن وحشیان، به توافقی برسید. به شما می‌گویم، نمی‌توانید با آن‌ها به توافقی برسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/143859" target="_blank">📅 12:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143858">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f0422250.mp4?token=eYAX-JHJl7UyU5DH82JawWA3LPd8CAaVu5I1tcE_UJgjeUgSVCDrM_EJOcJs5IdF86wgAdGdzy6xXcM6cS8UGhZ_KOI2a1MQJOflfg298mdT3EwXfBblcp4VfMtdhhx8zcSqFe36o3x3BOn8GbA2wgATvxghijuituyFwfT4UyzQWDgONhPZdthtFuNaNAxnVPnIfFh1GfHFJea5IBRsFunV9dKIujHznFVVAR0VufCrOFBG0BV1Q9yGpkgfsCG0N5CGhL1pesPrutoYNE9aw0FbLhYLg_HYdp9ApwbjbyEJm6LARg4jRSTYc_W5FLvNejY5PZcModjAT7YyW2Jyvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f0422250.mp4?token=eYAX-JHJl7UyU5DH82JawWA3LPd8CAaVu5I1tcE_UJgjeUgSVCDrM_EJOcJs5IdF86wgAdGdzy6xXcM6cS8UGhZ_KOI2a1MQJOflfg298mdT3EwXfBblcp4VfMtdhhx8zcSqFe36o3x3BOn8GbA2wgATvxghijuituyFwfT4UyzQWDgONhPZdthtFuNaNAxnVPnIfFh1GfHFJea5IBRsFunV9dKIujHznFVVAR0VufCrOFBG0BV1Q9yGpkgfsCG0N5CGhL1pesPrutoYNE9aw0FbLhYLg_HYdp9ApwbjbyEJm6LARg4jRSTYc_W5FLvNejY5PZcModjAT7YyW2Jyvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: امروز، بسیاری از برادران و خواهران ما در سراسر جهان درک می‌کنند: این سرزمین ماست و سرزمین دیگری وجود ندارد.
🔴
و وقتی می‌گویم «سرزمین ما» — هر یهودی، هر زن یهودی — درها باز است.
🔴
ما در دولت اسرائیل، در قلب سرزمین اسرائیل، منتظر شما هستیم و شما زمینه را برای موج بسیار بزرگی از آلیاه که خواهد آمد، آماده می‌کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/143858" target="_blank">📅 12:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143857">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
نتانیاهو درباره طرح اوگاندا: هرزل طرح اوگاندا را پیشنهاد داد زیرا، مانند یک نبی واقعی نسل ما، درک می‌کرد که قرار است در اروپا چه اتفاقی بیفتد.
🔴
در اوگاندا، هرگز نمی‌توانستیم شور مردممان، چشم‌انداز نسل‌ها و آرزوی بزرگ بازگشت به صهیون و سرزمین اسرائیل را شکل دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/143857" target="_blank">📅 12:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143856">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c49c82616.mp4?token=L44K5Kt5_nVdH_ox8t9iv18PaF_RBe_N67-HTuIOpMevyqHysu-wMDF6tMppQIAPRCr3eh8dCyW3VTlWOvAKZHaDWXVvWonAsLCSsbh9yGm-opkck95en9UUGRVx42Bu6TzWEh1kPeEtq1C-ywG1f1a9zUMgK1JeTURHE5U3BPjI9ZHsBdio1OIR3IJXOsVNkxrG0ri_cyuHFcUSzhzzQ1K4P1mCaxhHTX_0wvbybCNCvME8t6y5uasxv1nP-hKbiE0ZPokpMwvWgtAxirbymRIDEV-6N_fDq0Tx8XDPd3Pl_eoL9uoRROq-5iDmuxlPtn36LxfxDWTNl4YpZujWpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c49c82616.mp4?token=L44K5Kt5_nVdH_ox8t9iv18PaF_RBe_N67-HTuIOpMevyqHysu-wMDF6tMppQIAPRCr3eh8dCyW3VTlWOvAKZHaDWXVvWonAsLCSsbh9yGm-opkck95en9UUGRVx42Bu6TzWEh1kPeEtq1C-ywG1f1a9zUMgK1JeTURHE5U3BPjI9ZHsBdio1OIR3IJXOsVNkxrG0ri_cyuHFcUSzhzzQ1K4P1mCaxhHTX_0wvbybCNCvME8t6y5uasxv1nP-hKbiE0ZPokpMwvWgtAxirbymRIDEV-6N_fDq0Tx8XDPd3Pl_eoL9uoRROq-5iDmuxlPtn36LxfxDWTNl4YpZujWpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی دولت: تا آخر شهریور هیچگونه تغییری در بنزین 1500 و 3000 تومانی نخواهیم داشت
‏
🔴
مهاجرانی: تولید داخل و ذخائر استراتژیک بنزین مناسبی داریم و جای نگرانی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/143856" target="_blank">📅 12:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143855">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ارتش: قطر از سرنوشت خلبانان ایرانی اعلام بی‌اطلاعی کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/143855" target="_blank">📅 12:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143854">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
نتانیاهو دربارهٔ شهرک‌سازی: واقعیت پیش چشم ما در حال تغییر است.
🔴
دیروز با وزیر دفاع و دبیر کابینه بودم و اولین چیزی که می‌خواستم ببینم یک نقشه بود.
🔴
وقتی نقشه را می‌بینم و نقاط، نقاط، نقاط، نقاط، نقاط را می‌بینم، می‌دانم که ما نه تنها وجود خود را در حال حاضر تضمین می‌کنیم؛ بلکه وجود ملت یهودی را در آینده تضمین می‌کنیم.
🔴
۱۶۰ ایستگاه پیشرو، ۱۰۴ جامعه که ما تأسیس و قانونی کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/143854" target="_blank">📅 12:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143853">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
رویترز: تقریبا نیمی از نفت جهان در سال ۲۰۲۶، از کشور‌هایی جریان می‌یابد که درگیر جنگ بوده‌اند
🔴
درگیری‌ها در خلیج فارس و اوکراین ظرفیت پالایش جهانی را حدود یک دهم کاهش داده
🔴
قیمت‌های بالای سوخت، به افزایش بدهی‌های آمریکا به ۴۰ تریلیون دلار منجر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/143853" target="_blank">📅 12:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143852">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
گاردین:پس از عملیات نظامی جسورانه برای ربودن رئیس جمهور ونزوئلا، نیکلاس مادورو، غرور ترامپ را فرا گرفت و او تصور کرد که پیروزی مشابه و سریعی در خاورمیانه در انتظارش است، اما این اقدام، زخم عمیقی بر حیثیت ملی آمریکا وارد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/143852" target="_blank">📅 12:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143851">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
نتانیاهو:
دستیابی به توافق با ایران ممکن نیست‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/143851" target="_blank">📅 12:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143849">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e47002c575.mp4?token=AXQJbfIAS4BCL0Wb2aU7GO_k8ES9CB0o8s3lEpWRBJJUTaYoYx0G1lZOnrBXKb3CFg34LX1EtTARhiRdXtJ4A6iet4BGSBt5aqlJZHtGynKCYZUZairVZE99Pj94Q7VLGszFoUGZ-P8lgU0yfYRMmxupiA-SIG2cl2n-SUemLq3HPq1UVT7zPtwvfYhkjZ4y9baGQ5_o_mK107Av9eZ8VX5FNSwOzDdNzBJT_MxxZck42Y0kAICP2IaDUk0VDOdBmdTR1uWMdWyLxmlH7KX0FXvga6-1wfn_VyBpGWkrgtBwdvZjwEKKcOiyZfbTFVAZIFGz2Cdc55qdX2KCpGBoIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e47002c575.mp4?token=AXQJbfIAS4BCL0Wb2aU7GO_k8ES9CB0o8s3lEpWRBJJUTaYoYx0G1lZOnrBXKb3CFg34LX1EtTARhiRdXtJ4A6iet4BGSBt5aqlJZHtGynKCYZUZairVZE99Pj94Q7VLGszFoUGZ-P8lgU0yfYRMmxupiA-SIG2cl2n-SUemLq3HPq1UVT7zPtwvfYhkjZ4y9baGQ5_o_mK107Av9eZ8VX5FNSwOzDdNzBJT_MxxZck42Y0kAICP2IaDUk0VDOdBmdTR1uWMdWyLxmlH7KX0FXvga6-1wfn_VyBpGWkrgtBwdvZjwEKKcOiyZfbTFVAZIFGz2Cdc55qdX2KCpGBoIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون حملات اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/143849" target="_blank">📅 11:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143848">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UI5leLsHi0nyTLm6EDwucFNcR8oNpWS3_UJh0w7WMtHDwQA3Pdy6ZTKPe8jj6MB4aE3K6MtjTp4gqce4zGiNe66gh9hD-OI7SJ6sP4hRcMy64Ty13eHdy4oJ7sb9-UK5isqIvfmx0lpEE2vFX4AsH16nKlbv9rDx5tXPdkiRH88K6MbJ1I_iBQmwIwOyAaY2SnGQZcULThw5q6B-w9WiBlxkS5NeMGo-JuV6z6SzDXlTzSwgkYOcAE1gTMcm9CN3wTd8bhRwXEbbyCnfWz93RaRReyHQsAsoPboAZ0m28PzNazpOZajnip-OkffLyeKouxMOHzcqk1iNRf-pynneQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دقایقی قبل زمین لرزه ای به بزرگی ۴ ریشتر در عمق ۷ کیلومتری زمین نوار مرزی کردستان را لرزاند.
🔴
کانون زمین لرزه مرز شهرستان های بانه، پینجوین و مریوان گزارش شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/143848" target="_blank">📅 11:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143847">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/630909b4ac.mp4?token=mzLDMlpGECghsNyJ5P06F2s7WTbB7k-g-5M2-IdAvPO55xbPfsJYHc2sErhtgM9I1Y9WgU6uwk0XdgQ-QcITuHNAXhAsUwemrl-hregXrzkXJxEB7VhfysXfZPnpcxSiCaA8Wu-aV8ubej-RbClKN3AKcnblm2iIt35kjkIU2dvLfFgGs_GK83aRWOzRbbaLK2Cwe3ttzuwZBTrNqo6bl3GBtpSRLCoIm7MUZXwgeHFl3FJcxSAEBNwUmYr7Bk95YHMW0q85boax8H_-QGPg_Nif6Y4EBYIaeanosK2F9AulCZx-DAS9b7jOGlx8vIWwEpTD_LGFLhEQSSrnWGnz_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/630909b4ac.mp4?token=mzLDMlpGECghsNyJ5P06F2s7WTbB7k-g-5M2-IdAvPO55xbPfsJYHc2sErhtgM9I1Y9WgU6uwk0XdgQ-QcITuHNAXhAsUwemrl-hregXrzkXJxEB7VhfysXfZPnpcxSiCaA8Wu-aV8ubej-RbClKN3AKcnblm2iIt35kjkIU2dvLfFgGs_GK83aRWOzRbbaLK2Cwe3ttzuwZBTrNqo6bl3GBtpSRLCoIm7MUZXwgeHFl3FJcxSAEBNwUmYr7Bk95YHMW0q85boax8H_-QGPg_Nif6Y4EBYIaeanosK2F9AulCZx-DAS9b7jOGlx8vIWwEpTD_LGFLhEQSSrnWGnz_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رکنا گزارش داده این فرد که بلاگر اینستاگرام هم بوده، عاشق ماشین‌های مدل بالا بوده و توی دیوار دنبال آگهی ماشین‌های گرون می‌گشته.
با صاحب ماشین قرار می‌ذاشته، می‌گفته یه دور تستش کنم و بعد با ماشین می‌رفته!
نکته عجیب ماجرا اینه که بعدش زنگ می‌زده و می‌گفته من دزد نیستم؛ چند روز با ماشینت دور دور می‌کنم و بعد سالم پسش میارم!
ظاهراً هدفش فقط لذت بردن از ماشین‌های مدل بالا بوده و بعد از چند روز هم ماشین رو سالم برمی‌گردونده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/143847" target="_blank">📅 11:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143846">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0f2625db.mp4?token=bZQ7QQHARTLsS1MVqY5T2vkZnIxV_ajtoy9clA48fToiz0bg2AMVixZa7M3fT3hq6gSNuRt3JcelM5ZJwtC7b4XWdrEP3nfIzxpZGo9IFUsGKAI_4qf886k8tiD7L0jF2sapxM3zExxGrsmxf9Jlm2AYffqutPyNah1VvoBMTkvjDRnITDvyaMkhG6gb9yKTA5Cna6KMWlofzEI1lVADfyXT6q3I-CQIxiAkp-LOweHo1EwVKlLPWQFmFYqWeFI1rRIVxoXJkXZecuylyMXCCDDgidjIVIbhL6alAmk1thm2nzQC141t3_37FEuwx1RdEqxXJyFLfQdWrikEW3c9Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0f2625db.mp4?token=bZQ7QQHARTLsS1MVqY5T2vkZnIxV_ajtoy9clA48fToiz0bg2AMVixZa7M3fT3hq6gSNuRt3JcelM5ZJwtC7b4XWdrEP3nfIzxpZGo9IFUsGKAI_4qf886k8tiD7L0jF2sapxM3zExxGrsmxf9Jlm2AYffqutPyNah1VvoBMTkvjDRnITDvyaMkhG6gb9yKTA5Cna6KMWlofzEI1lVADfyXT6q3I-CQIxiAkp-LOweHo1EwVKlLPWQFmFYqWeFI1rRIVxoXJkXZecuylyMXCCDDgidjIVIbhL6alAmk1thm2nzQC141t3_37FEuwx1RdEqxXJyFLfQdWrikEW3c9Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رفسنجانی در سال ۱۳۶۰:
پهلوی همه همت و دغدغه ش این بود که مردم خونه و ماشین خوب داشته باشن؛ زندگی خوبی داشته باشن و ارتباط ایران با کشورهای جهان خوب باشه ولی الان دیگه اینا ارزش نیست و برای کسی مهم نیست و مردم دنبال معنویاتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/143846" target="_blank">📅 11:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143845">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
فلاحت‌پیشه: هیئت پاکستانی بیش از اینکه به دنبال احیای تفاهم باشد، حامل تهدیدهای جدید آمریکا بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143845" target="_blank">📅 11:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143844">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
روزنامه هند اکسپرس: تحریم‌های جدید آمریکا میتواند صادرات هند به ایران را به شدت مختل کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/143844" target="_blank">📅 10:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143843">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bkg1s6niUYDWivwVjUcZEMmlK-zJmA01Ml0_UR5Xf5pLfxbjouoJcwebdumq7xfDTgxZCxbLrc2SW9J_qmd_GoJ-KwRyA9UPhQMj3OxaoVISq0VFH_sx63W1gUuxYRvEm3bboh0qSp460axOFsYwxT8n3lVgTkILlKvnmZuwZJzssVsdAPW9Scs9-umazwelFywUjw5BFLykB9AXkWl4vdXm3pYNDRnOOpN4B5jpZqC6PJISShH90w9t6OW5JrfHkbAKYG1AaVWkrdNjsuhJCXn2kZmutsPmbC6PMeWpZn8AYL0sBJhtlevWtcSMmmBVC6Sm24aJsc39_WQljQzr4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری خانعلی‌زاده، تحلیلگر کصخول، احمق و متوهم صدا و سیما بر مبنای یک توییت جعلی!
🔴
مارک کارنی، نخست‌وزیر کانادا در سخنرانی خود هیچ نامی از ایران نبرده.
🔴
پ.ن: البته مستمع‌های این نوع افراد هم همگی احمق هستن و استثنا نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/143843" target="_blank">📅 10:19 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143842">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6963f249.mp4?token=tkS719fV0koybNCjtZx0GuMozoeBzdI-sPgPizQLQMdEqLy_tu26go9TacVORdBD0Pjz9Hb5imxodqnwCxUj_sDmEBzx_fGgewT547M7kTbnDtnOPHQM8ZDYyZGvpW8bGyrTruwoElz9hz_EtCDTaqSXrEaoVm8hmnivSvGBnCPve3Xax8Ox-lGJmGutuvAqi63QcbZTal7MGfF50HdC-AcsR9tVvaf6TpadwpPkXR-IqdQIexfoczInHHUEgrJjtElpwQ9Uvlx_0DSuxOxbPMrM6JZ_0C9zbTMgwe1S8FtNny4rfVdy8-vFOCOvNy8BAoeZtPSNnwaIHj_NUfJ1tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6963f249.mp4?token=tkS719fV0koybNCjtZx0GuMozoeBzdI-sPgPizQLQMdEqLy_tu26go9TacVORdBD0Pjz9Hb5imxodqnwCxUj_sDmEBzx_fGgewT547M7kTbnDtnOPHQM8ZDYyZGvpW8bGyrTruwoElz9hz_EtCDTaqSXrEaoVm8hmnivSvGBnCPve3Xax8Ox-lGJmGutuvAqi63QcbZTal7MGfF50HdC-AcsR9tVvaf6TpadwpPkXR-IqdQIexfoczInHHUEgrJjtElpwQ9Uvlx_0DSuxOxbPMrM6JZ_0C9zbTMgwe1S8FtNny4rfVdy8-vFOCOvNy8BAoeZtPSNnwaIHj_NUfJ1tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز یادآور زادروز مردی است که نامش با شکوه و عظمت ایران گره خورده است؛
کوروش بزرگ
، بنیان‌گذار شاهنشاهی هخامنشی و یکی از بزرگ‌ترین فرمانروایان تاریخ.
🔴
از پاسارگاد تا گستره پهناور شاهنشاهی ایران، یادگار او روایتگر روزگاری است که ایران در اوج قدرت، تمدن و شکوه ایستاده بود.
🔴
زادروز کوروش بزرگ،پدر ایران و نماد شکوه شاهنشاهی ایران، خجسته باد.
پاینده ایران
✌️
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/alonews/143842" target="_blank">📅 10:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143841">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc01971222.mp4?token=vQLn-_NfeKkZjYwG4lDzvpuNElFy-mNcfaYLlEngWCzqMHKdoJOHqjmew_aVwGhGRNQNYIdj8GluCh6GHULP35PHXcYC86F2YSLUaNG95svTHhIWYgzcCFPwEHgGzmnP30iCDLXLbRCY4jysA6FfZtT-ewWiNbGmSpzKOTKCXMWAmqPWLN7nzUtbTQCaBsFYTmnxjGer2DrUF32-mYV-h2vRyshCEVuUYUw1SKhL-8NFDWV1jvBTNVcEoob_egFLzfNztFnOZsii8BKa1Y8Yf_B5kyO6VL4QIrY-Z2R2Xtv0gi42eU_YMGe1HgPljQWlBfrALnB55Th4OrUM_8uvYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc01971222.mp4?token=vQLn-_NfeKkZjYwG4lDzvpuNElFy-mNcfaYLlEngWCzqMHKdoJOHqjmew_aVwGhGRNQNYIdj8GluCh6GHULP35PHXcYC86F2YSLUaNG95svTHhIWYgzcCFPwEHgGzmnP30iCDLXLbRCY4jysA6FfZtT-ewWiNbGmSpzKOTKCXMWAmqPWLN7nzUtbTQCaBsFYTmnxjGer2DrUF32-mYV-h2vRyshCEVuUYUw1SKhL-8NFDWV1jvBTNVcEoob_egFLzfNztFnOZsii8BKa1Y8Yf_B5kyO6VL4QIrY-Z2R2Xtv0gi42eU_YMGe1HgPljQWlBfrALnB55Th4OrUM_8uvYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی دولت: انتشار اطلاعات میزان فقر مردم، نیاز به مجوز شورای عالی امنیت ملی دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/143841" target="_blank">📅 09:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143839">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وب سایت نیوزماکس:چند ماه پیش، پسر نتانیاهو، به طور مخفیانه از میامی تخلیه شد. این اقدام پس از آن انجام شد که یک گروه اطلاعاتی ایرانی که او را تحت نظر داشت، شناسایی شد. این موضوع در لحظات پایانی کشف گردید
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/143839" target="_blank">📅 09:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143838">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e47002c575.mp4?token=HXYF0b35raXopXTHpYACUTGjqc02YKKhQWmkZpvWpTLeXDe9n_AshQHRoaD8oj5WddIJRHSfSwbO7-EHX2yAzuK405CxRqjxfFt8fBkFk7hrskh8w854KAOYMFmciEj8-QdxwVTtN9RPjl0K4yhw86onhBvaemu0eFvY6O-NXdr60o_3-RYBkz1wf1BpUQ33TCYgEclzzfhz5RcoV9k9GBKj-8HXsxEdJ1vYfL3atcLWUv1FFsZk3w12EJNH07baQ4lmnnc4ZNG4uOXs-3NOWDWdgg0WOmmcOVyuIqEKyuwmingVFSzykwtJPaMibwkcnPRTkuP_NEtfrLElEcYEIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e47002c575.mp4?token=HXYF0b35raXopXTHpYACUTGjqc02YKKhQWmkZpvWpTLeXDe9n_AshQHRoaD8oj5WddIJRHSfSwbO7-EHX2yAzuK405CxRqjxfFt8fBkFk7hrskh8w854KAOYMFmciEj8-QdxwVTtN9RPjl0K4yhw86onhBvaemu0eFvY6O-NXdr60o_3-RYBkz1wf1BpUQ33TCYgEclzzfhz5RcoV9k9GBKj-8HXsxEdJ1vYfL3atcLWUv1FFsZk3w12EJNH07baQ4lmnnc4ZNG4uOXs-3NOWDWdgg0WOmmcOVyuIqEKyuwmingVFSzykwtJPaMibwkcnPRTkuP_NEtfrLElEcYEIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل
در تداوم حملات به جنوب لبنان ، اقدام به تخریب و انفجار در شهرک «مجدل زون» در جنوب لبنان کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/143838" target="_blank">📅 09:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143837">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
اکسیوس به نقل از یک منبع مطلع:
انتظار می‌رود استیو ویتکاف و جرد کوشنر، نمایندگان کاخ سفید که هدایت مذاکرات با ایران را بر عهده داشتند، امروز چهارشنبه از فرماندهی مرکزی آمریکا (سنتکام) بازدید کنند تا درباره وضعیت میدانی منطقه توجیه شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/143837" target="_blank">📅 09:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143836">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
آکسیوس: انتظار می‌رود سیاست افزایش فشار اقتصادی علیه ایران تا بعد از انتخابات میان‌دوره‌ای در آبان ادامه یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143836" target="_blank">📅 09:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143835">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUPDM7jW_ozL9pdG_3JCq62e2x6ZVFhlYtfYrxndSuYOIyKWzcbFEZcOi7C76p9KMHvR7k8qsyAaJMQiStV2TWO7PvXCZ2VRY3IIUdy9W53UovpcWu6rs1kHLA8xZIDDqAOzBFeBVpHQKPJ3gRyipg8QwHvGM5mZzS9GhPSIRrn7SStEdQroNrI4wwWTIKRxebhxaq-0BT04skp_dXNXynxov9TJJ-KujWoiypTB3PzKDIWgeP03rSQghckV3aqO8IyveEs8YBob9SWmOkI9JN4PiabhF7o19c-1LhT36fDCwNz5w6pUMTGJHANr1W1MJNcGXqLNNA_7PyJ14B2WZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکسی از سنگ مزار اکبر عبدی؛ آمدم، خندانم، رفتم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/143835" target="_blank">📅 09:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143834">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ارتش آمریکا: سقوط بالگرد بلک هاوک ایالات متحده با ۴ سرنشین؛ کسی آسیب ندید
🔴
این حادثه هوایی در جریان یک عملیات آموزشی رخ داد
🔴
بالگرد به طور کلی منهدم شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/alonews/143834" target="_blank">📅 09:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143833">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d702a3dbe.mp4?token=cGBDQ6lswduXNwm5wYVPfCreDNg4em_9wkICD6rLpMHlSb1XISQvkZTM-DrdwaGTlc_jRM5q8q7nxvm5ITnWZeqgMgU2E0feIvF9mYtnAy-HAmMbcILZEcugre4HxW9SHPBxzSbKBjpjRsT3GIIkBLPYt4bYreYceFtoCYfga8JTmFE87UQlEHK2RmVCjy70jiWexP58Y8VPii9JBwPgZGtG5nfyU5A9VTfBPTL_EVvg6fpzsC6OhNZeksBn7HZKP35k7uvahC0qAw5h1sx8P_bIiUvx_mCSI3wassytbXKUtxojwRLIpvQFqTO-7WkTDh9A_GI35qp8k2LGtT8FXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d702a3dbe.mp4?token=cGBDQ6lswduXNwm5wYVPfCreDNg4em_9wkICD6rLpMHlSb1XISQvkZTM-DrdwaGTlc_jRM5q8q7nxvm5ITnWZeqgMgU2E0feIvF9mYtnAy-HAmMbcILZEcugre4HxW9SHPBxzSbKBjpjRsT3GIIkBLPYt4bYreYceFtoCYfga8JTmFE87UQlEHK2RmVCjy70jiWexP58Y8VPii9JBwPgZGtG5nfyU5A9VTfBPTL_EVvg6fpzsC6OhNZeksBn7HZKP35k7uvahC0qAw5h1sx8P_bIiUvx_mCSI3wassytbXKUtxojwRLIpvQFqTO-7WkTDh9A_GI35qp8k2LGtT8FXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پالایشگاه نفت کستوو در منطقهٔ نیژنی نووگورود روسیه بامداد امروز هدف حملهٔ پهپادی قرار گرفت. در این حادثه دست‌کم یک نفر کشته و ۴ نفر زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143833" target="_blank">📅 09:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143832">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
رویترز خبر داد:کاهش ۲ درصدی قیمت نفت در پی مذاکرات ایران و عمان برای بازگشایی تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143832" target="_blank">📅 09:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143831">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAfT4cVMMvcpbguX0v2mH4cLDTYoCmjlq-WT6uV0iN_zHOalQpT9CgdezQLRXRfeu83vlG3sSSrKj19MSBYlvc3R6YhX074X324lLvBzT0yvIwk-n50ZxWUG2M_c21EfJbbntyMVfSZS_vzlBDnXfckV7lPZyYE1PqFM1PxjtwLg323B8cifb5Vt0Ujlc9CW0bvcC6cza2rpI1tG1eQ2C5y6ZbtyCc9Ol7RG9En2KslincXAbbccbc2gGbSfZnNuMbtjoKa_Jk3uGMpK06TqxTxyWvAgoN_tAD1t_1TXkzP8g-uoIvIu-1IzdcGC0PaCWF5dW8JvW9tCPAhixbEbMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
قیمت نفت برنت: ۸۶ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/alonews/143831" target="_blank">📅 09:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143830">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
دارلین گراهام، خواهر لیندزی گراهام، در دور دوم انتخابات مقدماتی جمهوری‌خواهان در کارولینای جنوبی، رالف نورمن را شکست داده است.
🔴
رقابت برای کرسی سابق گراهام در سنای این ایالت برگزار شده و دارلین گراهام توانسته نامزدی جمهوری‌خواهان را به دست آورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143830" target="_blank">📅 09:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143829">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وال‌استریت ژورنال: دولت ترامپ توافق هسته‌ای با عربستان سعودی را به کنگره ارائه کرده است
🔴
این رسانه مدعی شد تر‌امپ «پیمان ابراهیم» را پیش شرط جلو رفتن توافق هسته‌ای با عربستان سعودی می‌داند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/143829" target="_blank">📅 08:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143828">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
روزنامه کیهان: اعزام میانجی برای مذاکره، عملیات فریب است ؛ عاصم منیر هم مهره امریکاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143828" target="_blank">📅 08:51 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143827">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaLaA51qjvNVvu-5tn5yp_UYDBN4ErHi7oF1oR8fXruMqfD_HNMWiPrlj06HLsx5aDZI0Ew4SxuMX-AG18UR4MR0eE-Xjm-_vkOg3wKe_dcj7xnfQhEbOaVAzhC7f-k7X3lYFEGltqTN8R8E7VoBoS7-3o1i49EXw4AotQ8O7cY-5u-E_uJW6DNT94SAy8EWhe6v1QCO3MuLoYZ4BQryizRADy-SMR10SRCF6UlNRGnRiE7b3miY1FpPVIji66dAx1kt47ZajmXdng7tJAaKLz0yyip61xTDuGEUeavBfDRESZWJIHwOEINwypJ9elScAsFGrfp5sG3SSrbH5iYdFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حادثه آتش سوزی صبح امروز (چهارشنبه) بر اثر انفجار مخزن گاز کولر در بخش زایمان در بیمارستان دولتی "پیمز" رخ داده است.
🔴
در این حادثه دست کم ۱۵ نوزاد جان باخته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/143827" target="_blank">📅 08:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143826">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
رویترز: طی روز گذشته تنها پنج کشتی از تنگه هرمز عبور کرده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/143826" target="_blank">📅 08:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143822">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8797e2dce7.mp4?token=rPlFajeyJpj1v1qLkBuEJW_VTiA896uqhTuilG9Jcfy2DrOrjWI9JnhXcTQ_3Sti1GiLzf_6yarm8aLePwqsgHJdmLiN9khWe9Hq68xvQdfTT9i6Xng4SI5i60Hg_fBrGUtLrxH5zLBVWk7cA08SoaXxf37-TM4cYoZs8xb19XiWbxHgbmha5VAJU5Kvm4IAn_jXMze9J8dOgtHCRTk-9YQzm835SOZaJtPr2boKawoJV-yICL9Q2OSKQssVY0SCgY9FQTOmru7Bx--uYnWus0cnpgnCVmWcmKRS4VpAksDCSrQTnlVrdjqsWyTq31w422arv_EzXeBjWIMbgz-9Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8797e2dce7.mp4?token=rPlFajeyJpj1v1qLkBuEJW_VTiA896uqhTuilG9Jcfy2DrOrjWI9JnhXcTQ_3Sti1GiLzf_6yarm8aLePwqsgHJdmLiN9khWe9Hq68xvQdfTT9i6Xng4SI5i60Hg_fBrGUtLrxH5zLBVWk7cA08SoaXxf37-TM4cYoZs8xb19XiWbxHgbmha5VAJU5Kvm4IAn_jXMze9J8dOgtHCRTk-9YQzm835SOZaJtPr2boKawoJV-yICL9Q2OSKQssVY0SCgY9FQTOmru7Bx--uYnWus0cnpgnCVmWcmKRS4VpAksDCSrQTnlVrdjqsWyTq31w422arv_EzXeBjWIMbgz-9Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات پهپادی گسترده اوکراین به زیرساخت های روسیه در شب گذشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/143822" target="_blank">📅 08:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143821">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
فلاحت‌پیشه: هیئت پاکستانی بیشتر حامل تهدیدهای تازه آمریکا بود تا پیام احیای تفاهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/143821" target="_blank">📅 08:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143820">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
خبرگزاری ریانووستی:
واشنگتن و تهران بر سر آتش‌بس توافق کرده‌اند؛ منابعی در ایران و پاکستان این موضوع را اعلام کردند.
🔴
این آتش‌بس شامل آزادی کشتیرانی در تنگه هرمز خواهد بود.
🔴
انتظار می‌رود اعلام رسمی آتش‌بس طی روزهای آینده انجام شود.
🔴
پس از آن نیز مذاکرات و یک دور نشست‌های فنی برگزار خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/143820" target="_blank">📅 02:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143819">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
طبق گزارش ها، رئیس سازمان سیا یک ضرب الاجل جدی به پوتین در مورد ادامه جنگ و بسیج 500 هزار سرباز جدید برای حمله به پایتخت اوکراین داده است که می‌تواند منجر به ورود مستقیم ناتو و امریکا به جنگ با روسیه شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/143819" target="_blank">📅 02:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143818">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTkFGkh67zX84PWUhDqYH7g1OM5MLQosyi9rGw7rJsrkWI-roP_jrfTSoJEqXKrSUmO2Gj9hokGDXMpiAckTKwnua3HLQPZ_XIYJXkzJltnuM2JTuUgY0OLQNTDttAMLcz-7Zj7muIwAvmOnstsP5m1_WbP2Wln4sz1olxUe7uchDFo6Vz5x69FFQTQ5Q0U-sTS0wli-am4NMTZOP8dQVv_yufNDSgC0a0MeFXMdrhhUegItirQqoVDIprTEtCV9AcvHuZi31CAO2emYvMFtoAKu6-QSIfhY9s5n27R5KhDPh1zqGhQJP5ITJnMuhwK08lNCXAgweIdEqPDlfcGeUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان: باید بریم تو باسن چین
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/143818" target="_blank">📅 01:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143817">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mI_hb8QuiMbkmXQupuw3UAVle6CrmEtXWosfIuA1NMDY7Xb7OpTiUrqc8OSqxEZWMSmxUyBtK49jyCx-3LBM1Rv_7CRiiD6pbbwE2zEwSQR60oQ0Hb8Q23nhz1jnOwh9JaDrjCGMw1oAlow-jQ8U-MlIui82s2dxa-L0ie3Ekr403SNsYfIwLv9UExawIyBlHHAZ1FaoRZzEVoLdfqXlGRJhlxy8PN-6PqudqasEin9gELWpyye09N-voMIDswgTFgD4C9V1yUYQGRe9iiuzOPXroh2JiZShe5TYlnYyDp3MD1YO_D_2vsSh8tSsAYdIP9mALbBtbL-22-_AtnJqLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وام ازدواج ۳۰۰میلیون
🔴
یخچال ساید ۵۰۰میلیون
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/143817" target="_blank">📅 01:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143816">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی: ایران کنترل تنگه هرمز را از دست داده است و اکنون ما هستیم که آن را کنترل می کنیم.‌‌
🔴
ما در حال حاضر با ایران مذاکره نمی کنیم و فشار زیادی بر آن وارد می کنیم و این ممکن است ایران را به بازگشت به میز مذاکره سوق دهد.‌‌
🔴
برداشتن مین توسط نیروی دریایی آمریکا از هرمز یکی از برجسته‌ترین کارت‌های فشار ایران را خنثی کرد
🔴
محاصره، ایران را از درآمد محروم می کند و ما طی دو هفته اخیر تقریبا هیچ نفتکشی را در جزیره خارک کشف نکرده ایم.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/143816" target="_blank">📅 01:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143815">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
آکسیوس، به نقل از یک مقام آمریکایی: روبیو به تعدادی از همتایان خود توضیح داد که واشنگتن قصد ندارد به عملیات رزمی در مقیاس بزرگ بازگردد.‌‌
🔴
سیاست جدید در قبال ایران شامل پرهیز از اقدام نظامی در حال حاضر و افزایش فشار اقتصادی است‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/143815" target="_blank">📅 01:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143814">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f6e7d367.mp4?token=G8SWm4f_LF4oq7yf2PUgBsj9quypvH7iMbbGJ2b8nfKUF_Iij1DA-uAdIdMoHOdgQlkRZVwh6iNIr7uiDirM6MYG51YjcqerZTpjemq7TrW8j7rjpkdMaxSSGAcOl6EEp6vrpJg1Xi-QWgm84QJxKXx8DBS50Vd_P_3ejRW69SeTNOMm0xEWOx7_2wbhfTwhj_wHwVhst67qAwmZFJtad06zC8pZl0hxYjvkuWpzXzfMRCgWiyyJYnmT415pHwp2QMuwyYlBNOp_vHBc4_TenGBR-8FwEp_dGOW6PQCg_u5JHvgqgco83j76Qz6e7vgZ46kBcyBj0sa7MCNeNICW3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f6e7d367.mp4?token=G8SWm4f_LF4oq7yf2PUgBsj9quypvH7iMbbGJ2b8nfKUF_Iij1DA-uAdIdMoHOdgQlkRZVwh6iNIr7uiDirM6MYG51YjcqerZTpjemq7TrW8j7rjpkdMaxSSGAcOl6EEp6vrpJg1Xi-QWgm84QJxKXx8DBS50Vd_P_3ejRW69SeTNOMm0xEWOx7_2wbhfTwhj_wHwVhst67qAwmZFJtad06zC8pZl0hxYjvkuWpzXzfMRCgWiyyJYnmT415pHwp2QMuwyYlBNOp_vHBc4_TenGBR-8FwEp_dGOW6PQCg_u5JHvgqgco83j76Qz6e7vgZ46kBcyBj0sa7MCNeNICW3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل برای بار Nام تفاهم نامه اسلام آباد رو دایورت کرد و جنوب لبنان رو بمبارون میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/143814" target="_blank">📅 00:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143813">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
این جوان خوش زبان حرف دل ملت رو به تمام مسئولین زد
🔴
با هندزفری
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/143813" target="_blank">📅 00:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143812">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9d50449c0.mp4?token=r623jJlgas8OCEo3oEyDfgVlqYk3f1pFXUtmb1X_TfmC28JLsapXZi5oP1IHwVL12ZweCtAkU5MaH-PDO0F_D_GK6YjMYwT_mM4T1Ku_ga-u6hm89zyW6KzBbzm46hOIDdOpaGRa2aJi5NPY4jYtGaKIpzDj_t6_VyWI1n_49rYWB5F_YZpZe5AC0BtHLjBqHOvGmKT2AcoqZvTfZ3ycR_dOfDCfYIppmPQTb1lZ94wkDmHMEsVcBL2Oku7cxZEqdXKARZ9eicFpBIQtKB-KJvq_0wRnqPwMAlNWBNyomK6C8ah2FANoTiUsU3VBCZ0ELx7kweFjMVVuZs12wRz1hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9d50449c0.mp4?token=r623jJlgas8OCEo3oEyDfgVlqYk3f1pFXUtmb1X_TfmC28JLsapXZi5oP1IHwVL12ZweCtAkU5MaH-PDO0F_D_GK6YjMYwT_mM4T1Ku_ga-u6hm89zyW6KzBbzm46hOIDdOpaGRa2aJi5NPY4jYtGaKIpzDj_t6_VyWI1n_49rYWB5F_YZpZe5AC0BtHLjBqHOvGmKT2AcoqZvTfZ3ycR_dOfDCfYIppmPQTb1lZ94wkDmHMEsVcBL2Oku7cxZEqdXKARZ9eicFpBIQtKB-KJvq_0wRnqPwMAlNWBNyomK6C8ah2FANoTiUsU3VBCZ0ELx7kweFjMVVuZs12wRz1hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این پسره یادتونه موقع خواستگاری جوگیر و همه سرمایه‌اش رو مهر کرد؟ ۳ماه بعد ازدواج طلاق گرفتن و الان پسره هیچی نداره
🔴
قبل خواستگاری حتما
🧼
انجام بدید
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/143812" target="_blank">📅 00:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143811">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a931a5d6.mp4?token=XimXY99w-yaxvmKJ7DhN4TFm0V29k5-s1OACeX7XwC6QBSQ_Abal2TUYinebcRZgDmh4lSVTSTCuceQkWBL3datPxPWqCnr8VVF1qpl8Y_F5qJVyeTeflJG6BDr1YhK5W_vUpMGJlZ6K4-v0R35SWPZ-WPqqerHh92gAghqEl6TVXkW7BvPGc0C8mJ4s12EMHRPP3OY3CZYzSKriqOu_M74ZwiRGojV9xWgLce9o89uka8J-0a9qsuKYyWuSADWKB8_PyJxS6Ll_-Z_wMOwOrbxTev6fNUVUG5nzjTnqDTPlxkumW8-D5H0sXALGk1CQNrA55Lg3Px4vYhywtCFPXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a931a5d6.mp4?token=XimXY99w-yaxvmKJ7DhN4TFm0V29k5-s1OACeX7XwC6QBSQ_Abal2TUYinebcRZgDmh4lSVTSTCuceQkWBL3datPxPWqCnr8VVF1qpl8Y_F5qJVyeTeflJG6BDr1YhK5W_vUpMGJlZ6K4-v0R35SWPZ-WPqqerHh92gAghqEl6TVXkW7BvPGc0C8mJ4s12EMHRPP3OY3CZYzSKriqOu_M74ZwiRGojV9xWgLce9o89uka8J-0a9qsuKYyWuSADWKB8_PyJxS6Ll_-Z_wMOwOrbxTev6fNUVUG5nzjTnqDTPlxkumW8-D5H0sXALGk1CQNrA55Lg3Px4vYhywtCFPXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل چپ و راست داره لبنانو میزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/143811" target="_blank">📅 00:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143810">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9891eec9a5.mp4?token=BFT-x7nRBXDmylrugMKDN6xbLnzMaTgEi9TPu9DYGDBGYkrx1sOAwSbliI2SxfbMv4ILzEFzI_tw32JWkPetWtmTZmzuCsGmodqDQK8-oHIjC8K5kFrkTrKFLJoedsEpm_-fcyiFdAqU7zGQkMWobLXQz4JsFyKtMPORtcpLDN4NPPH_4I4chcM6dvUbndicFXeFpBsW0uWErz6sKMknkAP1z6YkY_soKyElSWyRhIuoCpheOeP-NrAS8DUItnCjz5NsPZn19R68Pqg24llCdECQcpyfHPRoJN2agwXV6nH2mSuaypCFVl8j4VcWcR88Xu2pGfOUYQqBBOol0qwGrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9891eec9a5.mp4?token=BFT-x7nRBXDmylrugMKDN6xbLnzMaTgEi9TPu9DYGDBGYkrx1sOAwSbliI2SxfbMv4ILzEFzI_tw32JWkPetWtmTZmzuCsGmodqDQK8-oHIjC8K5kFrkTrKFLJoedsEpm_-fcyiFdAqU7zGQkMWobLXQz4JsFyKtMPORtcpLDN4NPPH_4I4chcM6dvUbndicFXeFpBsW0uWErz6sKMknkAP1z6YkY_soKyElSWyRhIuoCpheOeP-NrAS8DUItnCjz5NsPZn19R68Pqg24llCdECQcpyfHPRoJN2agwXV6nH2mSuaypCFVl8j4VcWcR88Xu2pGfOUYQqBBOol0qwGrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دغدغه قشر عوضی جامعه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/143810" target="_blank">📅 00:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143809">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmFp3iTAxnPMjAnbOFwfxtnNQJyHWDxALzjdiag91e2LuZRRoQ_E-UMY-SjdctKr-hjNO9brBvCL1lWka_ns9Cp-yOlAEM5NI_68rkjllqZKUg3__gNm6OoXEA54W3FSQbUvQE5IVvEFyTVLWUvsISUP9ykPYe7MCybWwsjIod-_IvGMKSQ3xfAABb6mNFJrIi_acLMkNCusQyXeR9K-Pbh0R0BK3Lkb9sxX6bRbRHctYP8_74K6Ikaw_IiTqGf-RfmjXL8OSvVUqVJsdXXYZid2Em8YCEtxgI_Mc8Kko_ClsvvmdMDYJY5F7aJpgBiC1Pmd5YQCnOKhfP-LsEwa9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
عحیب اما واقعی
‼️
🔴
ویدیویی منشوری که آرام همسر سابق سپهر حیدری اسطوره پرسپولیس تو اونلی فنز خودش منتشر کرد
💢
💢
مشاهده بدون سانسور</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/143809" target="_blank">📅 00:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143808">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
الحدث به نقل از مسئول آمریکایی:
در حال حاضر هیچ مذاکره‌ای با ایران در جریان نیست
🔴
تمامی مین‌ها از منطقه خارج شده یا منفجر شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/143808" target="_blank">📅 00:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143807">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
غریب آبادی: دلیل عدم انتشار متن توافقات امروز ایران و عمان و انتشار یک بیانیه مطبوعاتی این است که ما هنوز تعهدی نداریم و این موضوع زود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/143807" target="_blank">📅 23:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143806">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be16072939.mp4?token=W1bQFzmh6VCcb_Kl0haoFQAo2KpGKPFx4Z4JJAVdkCdXixg5ulqohXfreHG_lNxZ7OiZUrs7awJ0HXfE5zaIDY_dhBg1UUhi_X8sNAjHxKIQFDjPXmQgWQpUWPWHH_reotR0NfKBAAQMcDRWqlMGThiKJqMdHfkT3jYCuGN4BHcgtEUZE0tnQPEEaKdqwPqsN4YT5eMz73LGYIfjXKNUcHimHv3FDJglagM_HX1LRKGZbfxNjWENMRsnPt7y7zpLv19TmowjuP0cTaXS6GMBuMtUukazvASaglfkSpok39KEh0wPsAyKObaR77nF1uY5YFnesk7YGS01SqeTZh6GRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be16072939.mp4?token=W1bQFzmh6VCcb_Kl0haoFQAo2KpGKPFx4Z4JJAVdkCdXixg5ulqohXfreHG_lNxZ7OiZUrs7awJ0HXfE5zaIDY_dhBg1UUhi_X8sNAjHxKIQFDjPXmQgWQpUWPWHH_reotR0NfKBAAQMcDRWqlMGThiKJqMdHfkT3jYCuGN4BHcgtEUZE0tnQPEEaKdqwPqsN4YT5eMz73LGYIfjXKNUcHimHv3FDJglagM_HX1LRKGZbfxNjWENMRsnPt7y7zpLv19TmowjuP0cTaXS6GMBuMtUukazvASaglfkSpok39KEh0wPsAyKObaR77nF1uY5YFnesk7YGS01SqeTZh6GRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
غریب‌آبادی : چرا باید همیشه ما منتظر بمانیم آمریکا حمله کند؟ ما می‌توانیم دست به اقدام پیش‌دستانه بزنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/143806" target="_blank">📅 23:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143805">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d4b6e4feb.mp4?token=svlthTpNyjS8QgA_iJCDWqFDdKBU2RNmg8Y4E0mJ22LojUGt91WIjBu0D9kJ-b8jCUDGmjSrLeJlHhXHRdyh8pmUbmSScPB3syNPjICjd74ynQatS8tUUTXUSlLNikXsr1P_lVaSdUwymhL0k_qm7X94q4ZDDHli62JilOZYrVgd3WOyDqZ55XjcrGDKsSj4ZL4zcsuubRE04Xb6eZF_cb6FBGzNAeeW4Kg5KShq6UFqrK6BL-W56jh48ILAuMYz-dnlqe-W59a4-Hd-52LkQ8aZVccNRgzIsSZ1aSuK3E3gaiQmjjHl9PcBdSJLmgUX-NLs45oskGMlvSp1gurxfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d4b6e4feb.mp4?token=svlthTpNyjS8QgA_iJCDWqFDdKBU2RNmg8Y4E0mJ22LojUGt91WIjBu0D9kJ-b8jCUDGmjSrLeJlHhXHRdyh8pmUbmSScPB3syNPjICjd74ynQatS8tUUTXUSlLNikXsr1P_lVaSdUwymhL0k_qm7X94q4ZDDHli62JilOZYrVgd3WOyDqZ55XjcrGDKsSj4ZL4zcsuubRE04Xb6eZF_cb6FBGzNAeeW4Kg5KShq6UFqrK6BL-W56jh48ILAuMYz-dnlqe-W59a4-Hd-52LkQ8aZVccNRgzIsSZ1aSuK3E3gaiQmjjHl9PcBdSJLmgUX-NLs45oskGMlvSp1gurxfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
غریب آبادی: طبق تفاهم‌نامه هیچ شناور نظامی اجازه عبور نخواهد داشت و تنها شناورهای تجاری امکان عبور از تنگه هرمز را خواهند داشت
🔴
معاون حقوقی و بین‌الملل وزارت امور خارجه: محاصره ما به ازای تنگه هرمز نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/143805" target="_blank">📅 23:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143804">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84226a08bf.mp4?token=Bv-8y4NC_e7lfa_BDAc2iRdgaDy2Kdi9qqRY9GaTNQzSy7AggD2USvmsNDmZauKGsnzmwm7wAySq9XcKYOf6M1sRqUe11eVfUSQcilzgASR6wLLo1nRrB18oCwyF0cyQwVFpZG1QTNPKoPFW8fj2OzTzElBCJx_mxfmeGFhzgbd7q_5s8S04cqG_Fd9DV95Sqt-lhMlS5JgwodZMOWzsf-5kT4_9HYKWVSAQIKgIyk1TJg1SCV0Tc0GoFodKMu2WPCIsGFC0DdRh5Fcb4gL_btB01RV0qVXMlbDoF83Neg3ZnSWX02wSnfiv2zikUSBq_6o8Uuq2M8Y0b7mQUxyQcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84226a08bf.mp4?token=Bv-8y4NC_e7lfa_BDAc2iRdgaDy2Kdi9qqRY9GaTNQzSy7AggD2USvmsNDmZauKGsnzmwm7wAySq9XcKYOf6M1sRqUe11eVfUSQcilzgASR6wLLo1nRrB18oCwyF0cyQwVFpZG1QTNPKoPFW8fj2OzTzElBCJx_mxfmeGFhzgbd7q_5s8S04cqG_Fd9DV95Sqt-lhMlS5JgwodZMOWzsf-5kT4_9HYKWVSAQIKgIyk1TJg1SCV0Tc0GoFodKMu2WPCIsGFC0DdRh5Fcb4gL_btB01RV0qVXMlbDoF83Neg3ZnSWX02wSnfiv2zikUSBq_6o8Uuq2M8Y0b7mQUxyQcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
غریب آبادی: بعد از توافقی ایران و عمان، مسیر جنوب بسته می‌شود / هرچند مسیر جنوب بواسطه خواست نیروهای مسلح شاهد عبور و مروری نبوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/143804" target="_blank">📅 23:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143803">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
گیدئون ساعر، وزیر امور خارجه اسرائیل، اعلام کرد که نمایندگان هلند فوراً از مرکز هماهنگی بین‌المللی غزه در کریات گات که تحت حمایت آمریکا قرار دارد، اخراج خواهند شد.
🔴
ساعر گفت این تصمیم با تأیید بنیامین نتانیاهو، نخست‌وزیر اسرائیل، و در واکنش به آنچه او مجموعه‌ای از «اقدامات ضداسرائیلی» از سوی دولت هلند توصیف کرد، اتخاذ شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/143803" target="_blank">📅 23:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143802">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4311254a.mp4?token=Y9XdyiROd9UD4Y_rJF14phf7440qvaHA7VFzHWM33e1YDt96jldNwVstPKd0oHYGx0ONVOl7lBrq-0UCeTI54o8X9Thhd7fUdv1JugCZ1DH1FhMAJcYxywYKpklZI1btN2eR-JNdvQFMFCwo14XLmV4yflXAOT7oP87jxYl_T0MtAW5wwDcEDN1xsp4VMSjXNnVMY-40G9ORShhFMgozy3vg9kd6eCbTuOfSGn4ac_wHCTR_5eKbmAacXQm56uYtD3oqKwGsaScWsywN4ltM8XTfDN_qYGLbvTMW2fIfUbghRU9CwocDFo4R1P_PCPbGBumUJ2lR50_tdoUqdW-GZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4311254a.mp4?token=Y9XdyiROd9UD4Y_rJF14phf7440qvaHA7VFzHWM33e1YDt96jldNwVstPKd0oHYGx0ONVOl7lBrq-0UCeTI54o8X9Thhd7fUdv1JugCZ1DH1FhMAJcYxywYKpklZI1btN2eR-JNdvQFMFCwo14XLmV4yflXAOT7oP87jxYl_T0MtAW5wwDcEDN1xsp4VMSjXNnVMY-40G9ORShhFMgozy3vg9kd6eCbTuOfSGn4ac_wHCTR_5eKbmAacXQm56uYtD3oqKwGsaScWsywN4ltM8XTfDN_qYGLbvTMW2fIfUbghRU9CwocDFo4R1P_PCPbGBumUJ2lR50_tdoUqdW-GZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
غریب آبادی: بر خلاف ادعای مقامات آمریکایی تنگه هرمز بدون ترتیبات ایرانی باز نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/143802" target="_blank">📅 23:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143801">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7553b9202e.mp4?token=kalufmxSPhSXra19GifOA7fMNANfSqvxtZb0W8yzd7ji4q6Qyl4qEvVmn6IZOXW8XYXGLpRg_UXA301pzhCg-e-Wi2-pCcXZqO02Ghq_5aInP2Dxy5rZyL8a9NImNAgCGVJRG1SeeQJ-YEvQ2elcN5KmYtqbeM1bcQRwmK1rXa-hydQrTTiJ2YlSxSxJmx9wKU5foOPnrGCv7-blc0N99EIl-nZa32aHHGBh1Qz8iUr7vXmJqQ8dwt0w2gFk-cJ4_6I-TAv646F8oEibwkZoHnIjecwkZ5FFnYQrfNJvClPwgAlkmfysxO_PaDPP7dtYIGlXIrOp9r2Dkms2XIIIVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7553b9202e.mp4?token=kalufmxSPhSXra19GifOA7fMNANfSqvxtZb0W8yzd7ji4q6Qyl4qEvVmn6IZOXW8XYXGLpRg_UXA301pzhCg-e-Wi2-pCcXZqO02Ghq_5aInP2Dxy5rZyL8a9NImNAgCGVJRG1SeeQJ-YEvQ2elcN5KmYtqbeM1bcQRwmK1rXa-hydQrTTiJ2YlSxSxJmx9wKU5foOPnrGCv7-blc0N99EIl-nZa32aHHGBh1Qz8iUr7vXmJqQ8dwt0w2gFk-cJ4_6I-TAv646F8oEibwkZoHnIjecwkZ5FFnYQrfNJvClPwgAlkmfysxO_PaDPP7dtYIGlXIrOp9r2Dkms2XIIIVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
غریب آبادی: در مذاکرات با عمان ستادکل نیروهای مسلح نقش اصلی را ایفاء می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/143801" target="_blank">📅 23:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143800">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
‌غریب‌آبادی: پیش از هر اقدامی برای بازگشایی تنگهٔ هرمز، آمریکا باید تمامی تعهدات نقض‌شده خود را به‌طور کامل اجرا کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/143800" target="_blank">📅 23:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143799">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‌
👈
غریب آبادی: انتظار داشتیم تا با کمک دوستان عمانی مسیر جنوب در تنگه هرمز را ببندیم اما فشارهای آمریکا مانع شد و ما مجبور به درگیری نظامی شدیم
🔴
در تفاهم با عمان مسیر ورود به تنگه کاملا در اختیار ماست و بخشی از مسیر خروج هم در آب‌های ایران قرار دارد؛ همچنین فاصلۀ ۲ مسیر زیاد نیست.
🔴
در تفاهم جدید عمان می‌پذیرد مسیر جنوبی را کاملا ببندد
🔴
البته درحال حاضر هم نیروهای مسلح ما اجازۀ عبور از مسیر جنوبی را نمی‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/143799" target="_blank">📅 23:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143797">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
غریب آبادی: تفاهم ایران و عمان معنای بازگشایی فوری تنگه از فردا نیست و این دو موضوع جداگانه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/143797" target="_blank">📅 23:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143796">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
غریب آبادی: طبق تفاهم‌نامه هیچ شناور نظامی اجازه عبور نخواهد داشت و تنها شناورهای تجاری امکان عبور از تنگه هرمز را خواهند داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/143796" target="_blank">📅 23:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143795">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
بحران بنزین شروع شد
‼️
‼️
خودتونو آماده کنید برای طوفان!
تحلیل ترسناک این پسره رو حتما ببینید
👇
https://t.me/+6PPyWURHtW5jN2M0
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/143795" target="_blank">📅 23:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143794">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYDkY4Ej_3LnxwAhl0cjI4dYzo05rD6Ehi5eB7KTR1Y2KGiRgJArmVN9v6OsqL98yTNdAGVZQ_ANuRpHE6i3h7p7thr3y2RNVgKO7w6jzj5b0Ca815CA-sp_CUU7W891Jehfrs-ThZm4M98H-Mm2DXOJCbXwaj6mXO0JaLrTRUWs00YV1rCgbBpnszKVpWrurN5uhx1G0l37VGgoKempaQwoF2g05CIV9GTZKiUcNhnjC0NRpm3jSbINl8tMfwWJ_fC7ek2-AmGQSmTMdlc8m5NXLFuwgsZxyXgcj2SpoHIcCyTQPKlDEmugtpxckvwYJ5GmqtFhzRGhah5lhhRabw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکر تراکرس: حدود ۲۵ میلیون بشکه نفت خام در خلیج عمان منتقل شده است و ۱۵ عملیات انتقال از کشتی به کشتی مشاهده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/143794" target="_blank">📅 23:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143793">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزیر نیرو: ایشالا با تدابیری که چیدیم تابستون بعدی برق کمتر قطع میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/143793" target="_blank">📅 23:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143792">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbRys_RCD18U64HIW_i-Wbj9zw9OI-g9JNTss0gyrpKcUbdRznPVQwgiDMBZVUygR8O4j26mayfVPRzYpv06kmp3u8kwmpY6T9TUeJJgQO6AHP969jhG6wq8I1ZZmKboefPamnsKCHeM6zGBDazngjDNecrJLrxG3pKsY22L5xdqHvoEep64mDtBXeZqrqgVBBbsES-vm0LimZzB0nVwRDqh1hGsrscfxiz7RRLpc5-4EeQKlUUP72X8lLXj8t4EB-o61131POVY5dpUK1WktwmBEOfYu6PZ3N0yH0Y1xDm40lshBn63NmX4JD95PlLgSuCnKMCNccERwZo_vMnX-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیام عراقچی پس از دیدار با واسطه‌های پاکستانی و عمانی
‏
🔴
تعهد ایران به صلح و ثبات، همراه با دیپلماسی استوار و مستمر با همسایگانمان دنبال می‌شود.  در گفت‌وگو‌ با میهمانان پاکستانی و عمانی، بر راه‌حل‌های منطقه‌ای تأکید شد.
‏
🔴
چارچوب پیشنهادی برای ایجاد یک کریدور جدید، مین‌روبی مشترک و مدیریت آتی تنگه هرمز، نمونه‌ای روشن از این رویکرد است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/143792" target="_blank">📅 22:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143791">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rl6xYDHMWkSTveZUdmXGvlhbrCSNeY8JXfx0eKQJKIZRoMBCirxqUan7VHiqDsFxpWVPwDWdfCN74ELlLAeAmcjl1I4NeR0oieb2Nrf9J-ZwSbgq09xegfNWi-h2qjtrel8D1vEcTji_nteDiN_mJL01wRX7VAS8Sz9ApfX5NIELqK4YoXShgwjOStlVZZBRYHzb9Si8UWAkZBOVyYtxE4Nd9yuaV_yoayv81yilWkZ50U7YstaOykPVCPeEJF2T2hODmzt1baVtCldqWu9i9keHXa4_TQhQc3yLgNvXXtxVcUCPJwG4cN72pVaGp0jbf4qNDoZwy3dMFw-prjxf-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ دستور داده است که پرچم‌های ایالات متحده از ساعت ۱۸:۰۰ امشب به مدت یک هفته به نیمه کشیده شوند تا به افتخار دولی پارتون
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/143791" target="_blank">📅 22:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143790">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
اتریش حجاب رو برای کل دختران زیر ۱۴ سال در مدرسه ممنوع کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/143790" target="_blank">📅 22:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143789">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rn8cB4r1eqR2aDZtnWHCFWrkHjz2gAbxAP71_2j4UkrKmnx0MuSUafz8qqzTELUGb6xjBt-VHpslC-evKOwjN_gGvk7PaZQx3qF9E3MlsdIskQMHR7zksAkr3pbhYzfJbPWYtpvx4LWmYc33F2lXxsfN7EEriUxb3rE0l1t5egq43qYEulxAQOFFNK8YSwuPFs3kTfx9Ega6ShKz1GAtxteIHBUFEWMbWGmz0T0MlBD2-pLxXoT--Nk0g9mfjspNxFXlpZJXKjnoKo_aa4V-M_YF9lnyAv_cVEE67k27uClGjDd16x5eretmjXAOe3N_DDlAdMmD1e1pf7VInm1u6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف به بسنت پاسخ داد: نمایش مضحکت، «روز پیروزی» نبود؛ «روز دلقک» بود!
🔴
اسکات بسنت که پیش‌تر ادعا کرده بود تحریم‌های جدید علیه ایران مانند «عملیات نورماندی (D-Day)» کوبنده و سرنوشت‌ساز خواهد بود، در نشست خبری دیروز وقتی با سؤال خبرنگاری درباره توخالی‌بودن این ادعا مواجه شد، دستپاچه پاسخ داد: مگر من می‌خواهم اقتصاد جهان را منفجر کنم؟!
🔴
محمدباقر قالیباف در واکنش به این عقب‌نشینی آشکار و تناقض‌گویی در شبکه ایکس نوشت:
این برنامه اصلاً شبیه عملیات نورماندی نبود؛ یک استندآپ مضحک در کلاب شبانه بود که در آن حتی دیالوگ‌های طنز خودت را هم فراموش کردی!
#روز_
🤡
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/143789" target="_blank">📅 22:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143788">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
رویترز به نقل از منابع هندی: رئیس‌جمهور چین ممکن است پس از سال‌ها برای نخستین‌بار به هند سفر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/143788" target="_blank">📅 22:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143787">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3cc1597a2.mp4?token=OMm76hL7Bhykmi5uzgcoohGLWl6ekqnsYEciTYsG42j8I7wBmteCz3bdwm02WiSxDaI3m6TOSJAzV3HNhuDHm9afFHwll-Mbx9pwLU0A4xlBL0t6Odxv8TFrktAB-zMyWwCcBsswrewVK-ciomZiRNOK7EVnIUVx_DMSTkui5LojqaJ3Pl-uHDPJpmWFh89ndobNHA3PehNPuKlxiMebFdp6uE1UC3q-ifs7ERs7EfoflvaniIWwpXevs32Ldvr53ZxI0DOIYvuUBO-VadG_z9MEtHkQp5NQQTaXVcjGElg60u38b2mcFdi-eEmlHvNZFve7BQlVme1rNDajUg5ynA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3cc1597a2.mp4?token=OMm76hL7Bhykmi5uzgcoohGLWl6ekqnsYEciTYsG42j8I7wBmteCz3bdwm02WiSxDaI3m6TOSJAzV3HNhuDHm9afFHwll-Mbx9pwLU0A4xlBL0t6Odxv8TFrktAB-zMyWwCcBsswrewVK-ciomZiRNOK7EVnIUVx_DMSTkui5LojqaJ3Pl-uHDPJpmWFh89ndobNHA3PehNPuKlxiMebFdp6uE1UC3q-ifs7ERs7EfoflvaniIWwpXevs32Ldvr53ZxI0DOIYvuUBO-VadG_z9MEtHkQp5NQQTaXVcjGElg60u38b2mcFdi-eEmlHvNZFve7BQlVme1rNDajUg5ynA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر نیرو: ما آن‌قدر نیروگاه داریم که حتی اگر دشمن تمام توان خود را به کار بگیرد، نمی‌تواند همهٔ نیروگاه‌های ما را هدف قرار دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/143787" target="_blank">📅 22:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143786">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k2JwhNPgd8k6YRGvOjUhOALNhEaFbXacmFlxoNt1FbTI7Z5DVYZk8xIRQqH1hlNWPkI241Rbr1pORGHZ9kTmNt1FRCyCyof39Le1r4qdEbeBAx979BjBCBkzUa_jz4YdR228yf6UczB4__Ia3Ig1gNs7X9yzdAK5IO6pHXTpxQAbHwwi1edKjQUDlOOx5oY8ZKwuudMmHZ9NSgTNrk2BNbZcYmy4g1dHY84eAVqM7NI55KGwN8-mecOhA8vlQ387okYHWtPVkBPC4ObrnOPJCt3Tvacty0m4lXEFvV-k3PoQuFREE62NSnqfjypXO_AtUFC2dbn4Rig21G_qdhXWww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دود بر فراز دره سالوکی پس از حمله هوایی اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/143786" target="_blank">📅 22:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143785">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
فایننشال تایمز: کشاورزان غلات آمریکا با تشدید هزینه‌ها بر اثر جنگ ایران، با بدترین بحران چند دهه اخیر روبه‌رو هستند
🔴
افزایش شدید قیمت گازوئیل و کود تولیدکنندگان غلات را تا مرز فروپاشی اقتصادی پیش برده
🔴
پیش‌بینی می‌شود کشاورزان طی دو سال آینده هیچ درآمدی نداشته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/143785" target="_blank">📅 22:21 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
