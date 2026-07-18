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
<img src="https://cdn4.telesco.pe/file/uajieOeGUUNjUJaVJZb2sxNf628ksEd69WIa4YSpNsCcfs9b9TwFxkYZpQNJUIpS8eVmwJTOCQvDj-t4RkrIOGDnNkm6GMw23uK1TyxprNS6_4FOs52RiQTSGYqcosWqzCElTfufXnhdzJcteiDG08HdFMr78duF1kP0plU9-2TQIY5gndXe4uGfRCoGpxNk-XwIMJBG0CfgEZPq0fBG37qaMsntzGyesvdFBrmH3TEJjAiHE0E-MEjvBCpP5vHJUYhqet4DyEiYLLZPf2WeXhJj_Fy_CzJ8lhbFX2ylRan7tDujSpJBbcjOB6-isltdOpMzD1YC62kVg6wNXIZl1Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 165K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 14:57:31</div>
<hr>

<div class="tg-post" id="msg-68449">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5326ecb6.mp4?token=qR2AdzxB4UHHW_DJKgXAONvVMG_sJvsgLLa83aRa_khSSg4ltbJmqXDgNS9lJATVvjJKN6rcwKQ4mFkOnLwEW58-C9pXs814aKUtM-CdLCwJoJrhDsXiG-ssnM3BTxs34tGaf6joSU3ng1xvWr3gRcHIMN93qy7nkDQQShpUI0iqZQOBgR_WUGTs_--pkx9MY8xcm5kjyVMCGndm3gTh-Zarq9NVxH5aZbfNukdIC35ETCQeLmC-h4akF2cuBEyvNn_mCjxb3870IWxcdn7iKvOwTyRvvEFZSHPUgEHoiUc6dCHRbpFUMzCdxVxdcB3VuxNIFuryxX3hRKR7UyPEPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5326ecb6.mp4?token=qR2AdzxB4UHHW_DJKgXAONvVMG_sJvsgLLa83aRa_khSSg4ltbJmqXDgNS9lJATVvjJKN6rcwKQ4mFkOnLwEW58-C9pXs814aKUtM-CdLCwJoJrhDsXiG-ssnM3BTxs34tGaf6joSU3ng1xvWr3gRcHIMN93qy7nkDQQShpUI0iqZQOBgR_WUGTs_--pkx9MY8xcm5kjyVMCGndm3gTh-Zarq9NVxH5aZbfNukdIC35ETCQeLmC-h4akF2cuBEyvNn_mCjxb3870IWxcdn7iKvOwTyRvvEFZSHPUgEHoiUc6dCHRbpFUMzCdxVxdcB3VuxNIFuryxX3hRKR7UyPEPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
واسه دومین بار طی دو روز گذشته، جمهوری اسلامی به نیروگاه برق و تأسیسات آب‌شیرین‌کن تو کویت حمله کرد و باعث آتش‌سوزی شد.
کویت حدود 90 درصد آب آشامیدنیش رو از طریق آب‌شیرین‌کن‌ها تأمین میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/news_hut/68449" target="_blank">📅 14:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68448">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtavAkhN2b_CCSb3_DPpvyzdbOXvGSNZR3wuE3c9C5x7snQs0iBRNqp5-pKxdCD8d4Bn0NCLfD1O88U3LCjDPYEqzMamL-eG7YmmuoY0HgITsbxjaM1KGBV1BkGUpWCOqFHdbpsvGwmT0FIexJp1iNK2F8mWeoDc-xlk2F5AMBQR6VjaQu8w3pRb3SfewBXxQjfdSIq4jPZBxsV2McJCFE7cIx2pyMjLyOaXCrcOoJTiX2YMyR3TU2FQjMOsrk6HEyoDL9px9LmXVrgxdFDYJ4TjYj6OlJlywIEp8CWmUuR1tPS7usOjJ-CXw65Qb9PoKrf8ILgSLuoTakPbT67jqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/news_hut/68448" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68447">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/news_hut/68447" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68446">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=MODN-zNr1_v5OkM0Q_HAFdt8kQCK3a2DHitIyHfOlgIkIb3Hbo2oSzo4euNJx3rr9YG_0G6mmsNAI7RpDNsfx03XfFgnYE115pIe5LM2kns35OK-cg4Dh--WzEzQJ7K9xQ7O91CM-bv84VwtE6IeiFO6-pvwL1blffhIGuygKwS2xJH_Tuffzl_MCKExTpQEU60o9L8T540fvGBMuFnioVeHFL-5Mq8ATzshFkU2uOTCBD5jC0dUBpy6Mq9TMITKchnnG2zCgYHYD7SekClMHDY_M2vsQ4mOSsSCMy9YlaoxybUjL06r0FmRzHxef93OKdF5uOA6OxGELI2-jFXIYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=MODN-zNr1_v5OkM0Q_HAFdt8kQCK3a2DHitIyHfOlgIkIb3Hbo2oSzo4euNJx3rr9YG_0G6mmsNAI7RpDNsfx03XfFgnYE115pIe5LM2kns35OK-cg4Dh--WzEzQJ7K9xQ7O91CM-bv84VwtE6IeiFO6-pvwL1blffhIGuygKwS2xJH_Tuffzl_MCKExTpQEU60o9L8T540fvGBMuFnioVeHFL-5Mq8ATzshFkU2uOTCBD5jC0dUBpy6Mq9TMITKchnnG2zCgYHYD7SekClMHDY_M2vsQ4mOSsSCMy9YlaoxybUjL06r0FmRzHxef93OKdF5uOA6OxGELI2-jFXIYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/news_hut/68446" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68445">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⏺
وزارت نفت کویت:
خسارات مالی سنگین در پی حمله‌ به یک تأسیسات نفتی‌مان رخ داده.
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/68445" target="_blank">📅 13:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68443">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41aabd1106.mp4?token=cvekvGmDT8lWFOC2mEvOate1vDAcAmd0NGUw1dHgizMSL7HzitlNixfybgm5ze__-IpPChAgm5ZmcFiB5PgdeZbXGTZ6mCOq7WQz4zS-wBtdjoYXW7LaRCFhTTbMf-3oDzK7iwaHqQ9dFBKnhK2DQpSV7vhcKddxEmX-_hfYLUdqBm_b-nQbA7FrgnMCTpV5oLMU5_ffSqmPExVVHwHzD-GJ50vwHOsyVzDu0TVtFeYI4PocaobpSMLxTkMX353KjtsiUPJUNzzARYxLtxQ0dGdXHMcj3UflGnDG5U3q2xNU2H0QF1ym9MOM7_XVXsYb7xvbchdPnqt0UTvFYMoOhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41aabd1106.mp4?token=cvekvGmDT8lWFOC2mEvOate1vDAcAmd0NGUw1dHgizMSL7HzitlNixfybgm5ze__-IpPChAgm5ZmcFiB5PgdeZbXGTZ6mCOq7WQz4zS-wBtdjoYXW7LaRCFhTTbMf-3oDzK7iwaHqQ9dFBKnhK2DQpSV7vhcKddxEmX-_hfYLUdqBm_b-nQbA7FrgnMCTpV5oLMU5_ffSqmPExVVHwHzD-GJ50vwHOsyVzDu0TVtFeYI4PocaobpSMLxTkMX353KjtsiUPJUNzzARYxLtxQ0dGdXHMcj3UflGnDG5U3q2xNU2H0QF1ym9MOM7_XVXsYb7xvbchdPnqt0UTvFYMoOhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
موج جدید حملات موشکی و پهبادی سپاه پاسداران به سمت اهداف آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/68443" target="_blank">📅 13:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68442">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cc8bace1d.mp4?token=R89GC-7XD5J8M5eFeaHee2W0hv9G6wtHP9QDxeRQhyc82eTNYsqwfURB-fFhdi2sj3ZicgcqLfBY-gDmAG2c1niPbe6q6Btf2mgWxCargVosh8Z9U_7_MgfgcnG9dxwVvmWJdlukpqJZZ2qrzOY6PmK8GWCwOxmXtEYEdO3YcBphuyRoAXuw48CV04cNpuf2aMIoH86-kbYtURl6LhYkGd-jduTQYu8rGiNbs6ATy5KRpYeIWbsIGQB6fWcyFICMKHBF42k2ZOwrj789AQpWkrW7LGTmvPMLVZz8buO9v9-ugRFKYCsbgVeNPQ2tj_q74axlYTV5Vkd1vrs_05tfyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cc8bace1d.mp4?token=R89GC-7XD5J8M5eFeaHee2W0hv9G6wtHP9QDxeRQhyc82eTNYsqwfURB-fFhdi2sj3ZicgcqLfBY-gDmAG2c1niPbe6q6Btf2mgWxCargVosh8Z9U_7_MgfgcnG9dxwVvmWJdlukpqJZZ2qrzOY6PmK8GWCwOxmXtEYEdO3YcBphuyRoAXuw48CV04cNpuf2aMIoH86-kbYtURl6LhYkGd-jduTQYu8rGiNbs6ATy5KRpYeIWbsIGQB6fWcyFICMKHBF42k2ZOwrj789AQpWkrW7LGTmvPMLVZz8buO9v9-ugRFKYCsbgVeNPQ2tj_q74axlYTV5Vkd1vrs_05tfyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپهبد خلبان نادر جهانبانی؛ میخواهم شاهد پرواز گلوله ها باشم
🫡
نادر جهانبانی (۲۷ فروردین ۱۳۰۷ – ۲۲ اسفند ۱۳۵۷) سپهبد خلبان نیروی هوایی شاهنشاهی ایران و معاون فرماندهی معروف به ژنرال چشم‌آبی بود.
وی بنیان‌گذار و سرپرست تیم آکروجت تاج طلایی است. از او به عنوان یکی از بهترین و برجسته‌ترین خلبانان عصر خود نام می‌برند.
نادر جهانبانی دانش‌آموختهٔ دانشگاه خلبانی نیروی هوایی روسیه و آموزش‌دیدهٔ دوره‌های خلبانی جنگنده‌های جت از آلمان بود.
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/68442" target="_blank">📅 13:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68438">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc56ea3cff.mp4?token=NYDR5zuOTD1j9ovORlJbryCDYkqBSsQGE8YVI5qKKR4ecENzFBVG-0VD5Ow-4ysuzd_De05Udmw3GXhOtYtkN20ytPtWgk0N8BwpFuVdjiRL9AkUdodaJGw1abiwqVLcN9otZ9Gps1t5cPbQy7aGiPxNDksakK_leE3j1UNQDETOxov_Rw1WQ7E1gKTNJtyqqYjjEkb1aj1q7EgPr5zqjpH35n_vjhwzuvft6F-KZnm8y6lwizJD71cIOOlM2GWxhz3WNrgrwDWXfbt26GvBJeC0w-_CxsTtPREnFYCTXGkV5eTAJg68gcCEwrGXWdWu-j2P3yrzNey3WzjvFXrMcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc56ea3cff.mp4?token=NYDR5zuOTD1j9ovORlJbryCDYkqBSsQGE8YVI5qKKR4ecENzFBVG-0VD5Ow-4ysuzd_De05Udmw3GXhOtYtkN20ytPtWgk0N8BwpFuVdjiRL9AkUdodaJGw1abiwqVLcN9otZ9Gps1t5cPbQy7aGiPxNDksakK_leE3j1UNQDETOxov_Rw1WQ7E1gKTNJtyqqYjjEkb1aj1q7EgPr5zqjpH35n_vjhwzuvft6F-KZnm8y6lwizJD71cIOOlM2GWxhz3WNrgrwDWXfbt26GvBJeC0w-_CxsTtPREnFYCTXGkV5eTAJg68gcCEwrGXWdWu-j2P3yrzNey3WzjvFXrMcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
🇷🇺
حجم آتش‌سوزی در مسکو پایتخت روسیه بعد از حملات پهبادی اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/68438" target="_blank">📅 13:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68437">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe648570f6.mp4?token=B9YNq7SYqG7HnW1UaZY73mLaG1oweqpTWCCeNdasrTE0EPnez4KGICwcB5m1ya0wBE1TpFUjD9w2vHctuDVMcdJu4DnBN_cxgbRpy1nHmKHbZdDaZ1T_Ql1a8j8RL1catVne-XTs6UGcxdb4WYys2Q5u81tXUX80nXw3dXPmmmbSLTApEpYc8eNoUKvOSEbHMH4jwDuh1IoUNTzUcZJoXLXz4j_gKt7JeWr7urOsuvdYjMLL7fpcxhqrFc7rvL3gdmLYKfSrA15zzN9yp8kvcc-z41pEBq64xer2qWsgsHtZqmfWAM1ycGUQ-L2LDoMphpfaUocxFYOBQbBvd2Yjchk1ELnAROJ4_U5Z9UT2KUadBIB1CNkH9FYgWEGuEPT8kpL5-xuCPSEYyeWt6Q9HbodapVTFTILm8e-hpe5aXJa_UznV3o8f2Hozh8QQ_xfFc_uqGD6VoT_Jy56t0ad07fyE-DhpearmL8EjutD0wDYblFKDozMGbSFa02EUQPcx-8ch2sO_wPELSVbAnK24jD91X3qPmrsSNBirERkG1YHRHqzBsUha79B7YPoVdTdzZU29c2pZebBdYdQMxsVaNMw_RssG4ySAZ6DrhHltrLWGhKZMKJa3AnOn8c2z73SzpA12-QPuUokCEGufcGTKl9xMu4OA18VGZDD_e5lmtg0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe648570f6.mp4?token=B9YNq7SYqG7HnW1UaZY73mLaG1oweqpTWCCeNdasrTE0EPnez4KGICwcB5m1ya0wBE1TpFUjD9w2vHctuDVMcdJu4DnBN_cxgbRpy1nHmKHbZdDaZ1T_Ql1a8j8RL1catVne-XTs6UGcxdb4WYys2Q5u81tXUX80nXw3dXPmmmbSLTApEpYc8eNoUKvOSEbHMH4jwDuh1IoUNTzUcZJoXLXz4j_gKt7JeWr7urOsuvdYjMLL7fpcxhqrFc7rvL3gdmLYKfSrA15zzN9yp8kvcc-z41pEBq64xer2qWsgsHtZqmfWAM1ycGUQ-L2LDoMphpfaUocxFYOBQbBvd2Yjchk1ELnAROJ4_U5Z9UT2KUadBIB1CNkH9FYgWEGuEPT8kpL5-xuCPSEYyeWt6Q9HbodapVTFTILm8e-hpe5aXJa_UznV3o8f2Hozh8QQ_xfFc_uqGD6VoT_Jy56t0ad07fyE-DhpearmL8EjutD0wDYblFKDozMGbSFa02EUQPcx-8ch2sO_wPELSVbAnK24jD91X3qPmrsSNBirERkG1YHRHqzBsUha79B7YPoVdTdzZU29c2pZebBdYdQMxsVaNMw_RssG4ySAZ6DrhHltrLWGhKZMKJa3AnOn8c2z73SzpA12-QPuUokCEGufcGTKl9xMu4OA18VGZDD_e5lmtg0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
حاضری به عنوان یه جان‌فدا، بخاطر مملکتت، بخاطرآب و خاکت بری بجنگی و از مملکتت دفاع کنی؟
🇮🇷
جان‌فدا : آره، من بخاطر مملکتم جان میدم.
🎙
خب الان بیاین امضا و اثر انگشت بزنیم که بریم خط مقدم جنگ.
🇮🇷
جان‌فدا : من بخاطر مملکتم جان میدم، ولی الان کار دارم، شما برید من بعداً میام.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/68437" target="_blank">📅 12:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68427">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V7BVlUA8Eam1yHTSz_ICmqDPmEgeNDAuVTbcqU3xLvmMo-rAMwg15KwNGxj0j9zVAkn-D6vh5NRH0Lu84vf7pDNsQwiwcY52lTuihzV5rOfM9Izol8L1rGOSsbmQqtpuH-q9X5eo2Kim62cwNFW08Yf1-tFKSPTKEtwdCvrLB1-CoQXvx4ZEVuSZUDql7WdXiNoHTfoZLxBAXXpuNdYQPHV2ASdP7eBuRsvJLLEAzdlIZILw6BKsq-UalyEoqXd52jTFCcQHrN8QoOsaKvgNhoOgb5FuMTjHrjBZXaOcRttLUy4eAKvcbuu7RCbeW8g8CFHp2xjMm4sfpCx7tl4gUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JMeNRZMKmdsZb_ExCKl6Z2pgucjKdIrzC23aVd7Lg16ipJiIaZaxsHWfJpHoMiI5r1HTj71c4fddEKV46XKX4_5G8TGRHw0MKS1rbp-B9SmSyk2kvcilc8pZLJMAILJNFmfLC7Dg-p02ZWev8YZtvghFI9YTE2KE0o23DxQ-CiclCaHWpYuGyUvi3ZTMQYtMPM3lSBBkTPTGZgKm2olFKYxy22ZDjVbw0FxDkG8kZu0CNvZBPUQnQXZYVhPp-cEMsrwaDKm4qdl5PWpNX5_nViHd9PO2wDcOFEXH9cPqwNaPNiNnX-W7xEPJIpPcVRBSgsLXQD6Xb5jraEcBDr0mEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oXlHzIOtycVEuzMaSyfjhTQ_k0vkOM397zePhw6u_lbEw6m_jlTRAiLMkW-D9VTW5GEG1xUnCnowrGUGD2tMzz9STfNzbX42lNPsmMi68hMJKTVIbk6NhNETndSaLzKQXjhbjf6z7ifIIoK__uSrTELnJWfK0ljB9qoIOLGfgDxIWKJcym1Zk8nSpEFTlR43HVfa2EIfmt9zYbo45PCVlqMoTit3RcaJvsG0fLU4e90Sb_vs_005FEDk9SHz9fEh6cYO-LowPT6dJQmSH3nWVmlF8bxRjbJAldcRtheadU8V56BLy0L7tKgOpSO5C5l-f0hGK_0DCIVQTGi--i5SVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DAHwWZcGQk9bTEPIAfKPO3pOndfQQwHEouwbOs6WPYwahNTkINmELN1cbqQaE7BT8UbCMaAS3wMzWBhNo8rZQjVR3BVuzRNCPNKEuRb7hB0OHc4-lI5_g3NSpLcHRjQqhXnjIuyQpRGwzpQK4z7RTeoOYr0hM91kIHzhLrVH6ugo05QGxZ2mjgDH5Ahw4D1NAPiJS_mOnvHIiNFoliLQmPRBCdX5NIYG50M7LHzlFRGJSdrbV23MK27soloafsPzsgtaPQcL9NMl3nSMC7Gs6lwAova0R-1gvYuxAqyiz0Axqj2GQyWgkp8KTZgxTzO_NaiHZ2ALJCDIRZMp38aBzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/el8YWblstOLTJChyvfOcg93SjeaCVsL_hZRF93qlInHSjDF0fptgLupC8aPPGy--pvq4yMMNt3TVLZajI_6yt_-wk-NSATPV6TWcYhXswi46Nme-BZADsVxVaJ5XdJmABjXGfI50wRV9gKeYt7j-u2Jb_4utMKk83udfpY1dQdtGJtlvwHNqnPSA2gWHSnWKtjErk3QV5W8ZMiINvrZOj5rv_6AUE6t-7frPqi4hNne08EXa3qIqSu9klgShUCuTGPWNpvurBVXik2LBuRJ3xzUXjbGOOyEmGh2LFyOeILZNsUw640yF2G5gX2vyEz5cXqKxTru8ZTpFDCLKl6zcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p4uTcxfBc32O5E4ovfMEV48s-U0QFHiUX6aMXqb2qzTZa_mEeOhYCz_5_XIybc8hwMwHTjH2-1H0ajk6tOXt3Tec2iNxxKxpehJy5L_CZWRNNSHohzfLp8UEVFk3CdZZOOiQ9gOCfoNtRvwbuMant9GigFICOf31d73Y0dAM2yNv6-Ws2VGa5lZGhaCzNXFxXapAAHoAPuc9fQyMi6xZYGEL3IITyyZONuxrV793sFNzD0i9VKDHU8skrau22kuYM8QGFcwiMsyKauyEtiaL1Rk5fd86mekrjAu5TVQH4U_CZYUgCQIiyyTM5D4TCut0Jm-yHgGMZNEPgvUdMUEVdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HknV2wLCJujUnJVmpYoZ0Cdk2P2e6ApZeryo-x0Wig7eu1a_8DzdIvNuZiq8n5DCPujmVn01O1X5Q8SVn1qzgxKkHfHp13eN2Ft0OntLkunNGHeuSk32EaTGB8VgonZJBELeKNnfLzogCfGqYA0d38skzHzMDfp-zLxwzIaydse9YmHnIRzNqfBBxNoqAcozvxw40z7eBPH4LjBlp-guxd5a-QhkLAmi1YSHnjTwMeiyt9znTYnq52aC27OIh-ZOm0u73a5zSNBow4h85VWWCuD-mocDW2Ad_0_Ut0WxqnNhwQGZZhJEwvxZ9ajXiHj3s6z6TtyvL1rOYr_4EpjSSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHfd_Q6YNJP1grjpJv5GKYLKv2JcpWdEfV1g-3V7WNoatHRXzM8PF6IsVM3OYuTbgzNHVbD-eKE3FcTDZCAN-DLM1_bN0g7HCeLPraSarEtyRdiVLlCVptpqAtzV4dBamRp9T4LG2XmS7bJN6erHaxbWt2EeoZcczktfqUrqibUGoJysfYqS6tB299qXg8UpcOL53MOf71XeH_E1Qy1IZNZOrSlnJN_CW65AMCqxvq2MeBeKpWPm46CuBzSdj-uXYOCVbjs9z997NmcmPoCD1KUDhw-7rEAoiPU1ky35lCxnN_24AMn6nHj8SySwgnHeDQ8DZEkKPKgn48-dUPWewA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ld_XHD-1Tx6e-hHC2j1Wn4orUZ2s2nX3uzqOkzLTu7gac-AZC1wbuhCbpMiNYgeWG2f_gKP5v9bqsx_iHg9Vb6i16L9iNEjQnr68-lAB6IlxbaNekjNdD7Zwe_kchic7zdUqKHf5k-p-JS5EBI0O25MVD9jTQneQQcEz31gZ2i8Rtm9DvKeaJsJaMe5iwWzF0_xaoN-wAD-lCMmlQ0_7O0cQ6LiTf8kUcjCsV86qZodepeXLLHy6HMJV_JPmxQ1qEmTpdWpLNBXstkto7Puyo9GbwlQsPHsLKfkF44e6vhgqugjyTdyNZaDsbsOKhqhXCeHAHr4slDXtH2YJhXeVxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tM-LWNTjnmcyuKiYgL5dsoS4G-ezxUb2ZLdLJk-UR5GEP2PWjbVRMnEKk5zuvCfulzlh-3xWBhi6eRS495rLoJEUUQb8kHDOEG9fXF4l59RkpNvvI8q95Ya-tmpo8ZU2wR8RvAztmFYmglnTDZpgrpg4uy0wRI4eDSsPL1rx6w5Lw3s6wFidrT5I3iUOM0Hjmaf3X3iqI9A-tXbegRRpF5KCoASuwgZqOr4BldazmQaLDSQDPP8AU-O4pWClKgTIkjMxU_Pkg2PJlPNeRw7TLerShNKE5ziFP99Nv2IyKZjrpl_OBQYp-re-eQ1HuNZoS9gOs699yISU9uC7EWXxsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
آب‌شیرین‌كن  بونجی جاسك تخریب شده
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/68427" target="_blank">📅 12:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68426">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcefe98033.mp4?token=U678mtnjpYhnDxITe_nlWXbxOpzsBA2MfWjzwuqUZsoEpbxbZ4s4cr5mymMZ3OxeTMCiQMYHC3Qa5ykrzI5kxgWdKfe10-nHAbDqlL5SYIPAkux87QuRM_bzkorGEUIm2kIwjrySaw1ogmptoewXLW2oifP9HLYWTRSVn6UQmL40zk6WSCM2uj8XROnt5XfWEb_kefglsTyHqYHkhxv_cQ8DLMkWX2cFvITonm4dFf-BM__vdekZ-54ax6kNrCd_Y6HLOQEjsMcSPZFcI568P4fpW91sTDDPpKj3Nx9_ufrXwG1xFOq_S-ivEdhCLEsjuZGPlnZTvZFCeNRR1Tuu8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcefe98033.mp4?token=U678mtnjpYhnDxITe_nlWXbxOpzsBA2MfWjzwuqUZsoEpbxbZ4s4cr5mymMZ3OxeTMCiQMYHC3Qa5ykrzI5kxgWdKfe10-nHAbDqlL5SYIPAkux87QuRM_bzkorGEUIm2kIwjrySaw1ogmptoewXLW2oifP9HLYWTRSVn6UQmL40zk6WSCM2uj8XROnt5XfWEb_kefglsTyHqYHkhxv_cQ8DLMkWX2cFvITonm4dFf-BM__vdekZ-54ax6kNrCd_Y6HLOQEjsMcSPZFcI568P4fpW91sTDDPpKj3Nx9_ufrXwG1xFOq_S-ivEdhCLEsjuZGPlnZTvZFCeNRR1Tuu8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تونل گلوگاه، در حملات شب گذشته آمریکا آسیب جدی دید.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/68426" target="_blank">📅 11:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68425">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/68425" target="_blank">📅 11:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68424">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_96pDYZGhZR0ITprECR3ImzDL78_ua437n8LpgrZTMdTmQm0kJXWDej3KN1q2Gm7zWgkAeu0vAqKAH0lpRdAVQNAi_CCWHoZ367EZ2qPuitPg5dM13FU0ICzgTKZgi8qwcQpxPEgEony4KoKgaXK2TShe4cyMU-yo3rNNM9vedYJcV_BMXgnJBlRZkRywfrO4zN1VUCOsGdC3ZqYyfWBECdyHvUslpPtojMNHelIG7v8xBCxZVnpDYXCDKYEpDDtmLrgeBxIMTctQEFW7TMSFbwTbX-G435LTLfZKh1KXTJ2EzIiP8NMSY7m28-vkgTAGCMRc8Zxh1nmbA2yW9Urw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی است که دو نفت‌کش در تنگه هرمز، پس از برخورد با مین در این آبراه بین‌المللی، منفجر شده‌اند.
✔️
واقعیت: این ادعا نیز مانند بیشتر ادعاهای سپاه پاسداران، نادرست است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68424" target="_blank">📅 10:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68423">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a18b81da85.mp4?token=p3ETIpwli41cvTPRpZ44-935-Y3h2mBUjCFa0M-lgm--BFUOkcxSIde-JIU-oYNbJJT6KaofhYbrdy_qVlugeT04jmnhoBUSkkdOEpOE5Jee7wj_bQyXx78lHGj8xwT-UxJOTcuej88gMlm-14ySMtFaOAEpxPqQbnIOmaIorLVzGPteJmS7FZbb7mJXu9HVOKnG-jtSA0ewO_0ODFsyzZcQPbV_LW9dD3qfBKfsklJUqync9APVVb3TyF3h7yGOWqjOjkCEkCMWc-iCKfel1Y979xMiJ5E2hugGjVqno6VwQw4iCXSk0cdIeQNbTsYvDDZEI4tU6xJa5L9x18NlEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a18b81da85.mp4?token=p3ETIpwli41cvTPRpZ44-935-Y3h2mBUjCFa0M-lgm--BFUOkcxSIde-JIU-oYNbJJT6KaofhYbrdy_qVlugeT04jmnhoBUSkkdOEpOE5Jee7wj_bQyXx78lHGj8xwT-UxJOTcuej88gMlm-14ySMtFaOAEpxPqQbnIOmaIorLVzGPteJmS7FZbb7mJXu9HVOKnG-jtSA0ewO_0ODFsyzZcQPbV_LW9dD3qfBKfsklJUqync9APVVb3TyF3h7yGOWqjOjkCEkCMWc-iCKfel1Y979xMiJ5E2hugGjVqno6VwQw4iCXSk0cdIeQNbTsYvDDZEI4tU6xJa5L9x18NlEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه حامیان حکومت در تجمعات شبانه:
اشکال نداره زیرساخت مارو بزنن، مام زیرساخت اونا رو می‌زنیم.
بچه‌های فلسطینی چی بگن، ۸ ساله دارن میجنگن، مگه خون ما رنگی تر از اوناست؟
اگه تو این جنگ نابود هم بشیم اشکال نداره، لااقل ایستاده مردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68423" target="_blank">📅 10:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68422">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvkmt0_TMWg8rsDElOiwNohIXRSROaSvufFjHaiHfn7DIpLMndd9LKrCNPUJNxUyKvQIHWcrQ_XKgipXogJ8g2eXHj101_j62lx3Nj-lIk44gSdihueI_v5Ka8vsB5jHgkaC4v1FqmaLEy49bcFjrnIBaIN1HTH4SwRp7DipNbT9usbtSCnu0pl6g_CcBajJ2OPFAYxEVqYs1QF7HYMgIS1rZ3Q-JlVKTVorHOdSBYfhlo7-oAz-i_5MBLHUktMu2RvS0ADXTBx9swtF--_UEEJRBUnbFgZkxjPFIt6scW5Wfur3VaylYUPGjSQRPm8vu40MV8Xt40Uug_7TFgYvtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اکسیوس:سه مقام آمریکایی و اسرائیلی اعلام کردند که دولت ترامپ به اسرائیل اطلاع داده است که در آستانه احتمال گسترش عملیات نظامی علیه ایران، ده‌ها فروند هواپیمای سوخت‌رسان دیگر به این کشور اعزام می‌کند.
پس از آنکه روز سه‌شنبه چندین طرح نظامی جدید در جلسه «اتاق وضعیت» (Situation Room) به رئیس‌جمهور ترامپ ارائه شد، او در حال بررسی یک عملیات تهاجمی گسترده علیه ایران است؛ عملیاتی که دامنه آن وسیع‌تر از حملات کنونی در اطراف تنگه هرمز خواهد بود.
از جمله گزینه‌های در دست بررسی می‌توان به:
⏺
بمباران تأسیسات زیرساختی ایران مانند نیروگاه‌های برق،
⏺
انجام حملات بیشتر به تأسیسات هسته‌ای ایران با هدف مدفون کردن عمیق‌تر اورانیوم غنی‌شده این کشور، و بمباران تأسیسات زیرزمینی «کوه پیک‌اکس» (Pickaxe Mountain) اشاره کرد که گمان می‌رود مرکزی در حال ساخت باشد.
ترامپ هنوز تصمیم نهایی را نگرفته است، اما به نظر می‌رسد مایل است با تشدید درگیری و وارد کردن خساراتی سنگین، حکومت ایران را وادار به بازگشایی تنگه هرمز و پذیرش شرایط هسته‌ای ترامپ کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68422" target="_blank">📅 09:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68421">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68421" target="_blank">📅 03:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68420">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdujzBKrPQ-ebTwAzXCI55txLFvdyQtktHJcXwTIV_YwLYgVk9070Y2MOo6duk4aC5RYRIy4DSf2JKsdRAfhgZHhWje7tGkfGlo-rK2-X6mCteJZA1CcbDPRcnNh0rL1QhiTBL4TuwokaVzyNmrgDl5Dqdnxvy-7CvHZgxVMciJp5G9MdXt-K2Ice7K3HE6TS7Dwenku-fm68of_EwCzdcxVS2GYRkHgv0QpriIKpCq0d2F8IGZx9Ta0qLChvS20YzWHBTueuNjpFIR5_CktCL_ZeQsTkO2XbvnVP5UPAAP8R1BWpvAeC9-WfOh2EbuHZ4JTp3NTvSlXkkIs8MRHgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68420" target="_blank">📅 03:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68419">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در جزیره لارک
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68419" target="_blank">📅 03:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68418">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKBbY5FZTcTIu2NAf1k6IfOSagNZrk_ZmJZ51LIMN-sU2xg2RR2sAanDMPWoAHJj3oovHqlvS1S-EzE-bU1AiRepAvsK3oprN9B3AJkeuYK9_TQ3p87gNatZOl4AuxaZYJx6JqhIoKIENGOvgCMx3RFE1qI_Dju0-LHUvRhFr4QsABn6r0GeaeExxYab18vPRUPXyALdzI04GQUyOmtfhyRa2S-pqIBgfV6IKAvH6rVdm-OFbaxDh-vMy5105CGT7VGsArM1FzPRQ-1TFZur4TDKC50RkjdLbAJvnfGjs8J--gUcJMxX_h3A06b4_WJTIvgvmBC-cL2Z1ClnV_KK-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
۳ نفر در اثر حمله به پل بندرعباس_رودان کشته شده
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68418" target="_blank">📅 02:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68417">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
⭕️
باراک راوید به نقل از مقام ارشد آمریکایی:    ایران یک موشک بالستیک به سمت پایگاهی آمریکایی در عربستان سعودی شلیک کرد.   اهمیت موضوع: این نخستین حمله مستقیم ایران به عربستان سعودی در حدود چهار ماه گذشته است.  @News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68417" target="_blank">📅 02:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68416">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJTuNbx62ngLDNEa9KSYfyeUEMz6mY9-86EeHM12SC_jtUe71S53xhYxk2zpaFW1xvtXdU84CI-wvTTnOH3epI6x9nRlQV-RC1hw4QRQXsswfm-uyMKBgzKdtnIXlSqN7B9NoMsp9kZDwNH6cCZFfvC5DcvLIfPdcfO3YTVVoUclFpPZzSqLV-uU-mNiVO8mrQs4mE_TEdpCv79palcsWDG2L8m_pPQvezs0d79qTjmmhVQdD80Y9N2uL756hl8z3wPRgJggxmCCAKW0XoT2hzCTT8mmVcrLt4hGsegEhqRZNwfHmK7gKXscM0L-p2a_yQEXG00150W3MewDilLiHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
باراک راوید به نقل از مقام ارشد آمریکایی:
ایران یک موشک بالستیک به سمت پایگاهی آمریکایی در عربستان سعودی شلیک کرد.
اهمیت موضوع: این نخستین حمله مستقیم ایران به عربستان سعودی در حدود چهار ماه گذشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68416" target="_blank">📅 02:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68415">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⏺
رویترز:پاکستان به جمهوری اسلامی درباره حملات حوثی ها به عربستان هشدار داده و این اقدام را تعرض به خاک خود تلقی کرده است.  حملات این هفته حوثی‌های یمن - که هم‌پیمان ایران هستند - به عربستان سعودی، موجب نارضایتی پاکستان شده و این کشور را در معرض خطر کشیده شدن…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68415" target="_blank">📅 02:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68414">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
فارس به نقل از منابع عربی:
حملۀ گسترده موشکی و پهپادی علیه منافع و پایگاه‌های آمریکایی در عربستان سعودی در حال انجام است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68414" target="_blank">📅 02:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68413">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4391e385.mp4?token=ao1R0LB14Pej-43CsrPuCVWlKnGGr3suvqUKsxfk8sfdHcT1LgFNtJ3JRGKXhg_CrcIjmyYVr8HZhNiyVqNYa5-DGhA0tIKBpY4eSV8oCfbPuV84fgEjZOozsGaBdQN-GjARJzwcRkkvOOSRvBfQh5yhfrqaUHynP18mX-x6c8oGH6qS9rOKP-TumnvyveLZkTShqcDE5e2Ap1HQLyannXvRyxosZwpK8gi5krcwu9yxZzNd_BeEkgXhPQ_D8Zq1xufV2sbSQio5Dsj6PaTpxCSEaS6EgWMG39-ivBtYBi6pVFezZ_OVJfqxE7a7fJ4t-6AjkVQr2dvVvmXqbXkiIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4391e385.mp4?token=ao1R0LB14Pej-43CsrPuCVWlKnGGr3suvqUKsxfk8sfdHcT1LgFNtJ3JRGKXhg_CrcIjmyYVr8HZhNiyVqNYa5-DGhA0tIKBpY4eSV8oCfbPuV84fgEjZOozsGaBdQN-GjARJzwcRkkvOOSRvBfQh5yhfrqaUHynP18mX-x6c8oGH6qS9rOKP-TumnvyveLZkTShqcDE5e2Ap1HQLyannXvRyxosZwpK8gi5krcwu9yxZzNd_BeEkgXhPQ_D8Zq1xufV2sbSQio5Dsj6PaTpxCSEaS6EgWMG39-ivBtYBi6pVFezZ_OVJfqxE7a7fJ4t-6AjkVQr2dvVvmXqbXkiIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پل مسیر بندرعباس رودان
بعد از ایست بازرسی چغازردی حوالی روستای سرزه پس از حمله آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68413" target="_blank">📅 02:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68412">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irW0hKNNq6oAk6w357ss7B5Vv5aeXANbwrFxxEGAs4yB-3KRnyOG0xHG1YW2rJs2pUIUmhGQLHHgJa60WEDEU_eZ7fYwrDhqt8U4pgAe3e6CnTrel7NWz1xAkyoNWQu9l2ox1AMvO481xVuM8nwh3nqbj6HjM30FZoiICb-2rBgMK3_F9fsOH2ITiajyyMIcHoQ7H5u7siQtJ2-D3YGm2S-Lt1izfgREks1Q_BpYeRvtgTyf8HrKo3UfR5EpIer1j3xG98bNthe792gBl4ITyqiWQSQIjmu1KH-vNcp9qAVUcsCvShzTazsVAStxLDCIFwhgtkVtuil_xcpUjr2ZBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژیرهای هشدار در شهر الخرج، واقع در عربستان سعودی، به صدا درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68412" target="_blank">📅 02:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68411">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acuoHeJoYrcXy_osv6Bue_O8-grhTRCDDdsQuPXQHlvNBs1XQxJVxYDU6t7vYn_eDuGsysPAm5_3INnMI35FGq-JB1fYV4ovKMv_4vDyyDPuXUlwXT2XQc5MhRLY95SCkYC_jQIgVRV-S3ovyM2Fj7KAlm3a1En83R_uoqMd4x9z-LrnGOZPyCYekLdLW7WevmPr5ffQJjjro6dqNYwE4bMwIFTaosvPPf9z3wQU5MJ1vZDQQsN98aprB1c7bHvjlIJxgWiY3Z5zxQEdndxS2KhC_x3eUZacjKaYMBJgOiJoyV27xHUGYXtWLVcfOlsajmwC_pc1C-p-mx9kB10rHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پل سه‌راه‌ میناب به‌سمت رودان
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68411" target="_blank">📅 02:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68409">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QQrKnasOPEXdy5BDxe8PrhSOAbahGHmMI4Ngh7eoEQwmgATe8bgaUxjh8pFis3kqPvV2DuN5Ak0wNoAM9spLyQWRY0ubRbNMGEqABZ0PfcnjZp44bGTYPwuc4g_yaper_3H32hWFm7erwOXjErInSPZ1hFxPSo4OkOyRoOgvxA5vMtLW0V90CvQb3LzcZQMpLbMO-i_n5S30gHXZd2lIJ_23--QzwRGcTqaSkM_N_QgaFeQ7h_j1H_qGNG6PaFd-P3lY5V_MKau0zQmgdwWIFx3__A_ny7CIpfnVLcArI5AdCOey4HqLfv25CsqWNQehECYoxYWxhrWxD9rhZxySaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PJ30ZUmJBd52avBJX0gZmm67nRyULAc8vwyvKLZiNNbZ7vAcgJ5i_rIB0TsjHUA2BtS4toqVjjyzInXS3aNYze0n2Y1Vj0P0DcJQM8B6mJRYlTVmbzdJDH34jJHaezR_FoomrfJitBYoWFFJxZp8dboXW5jxurh3UUGuBo_Zkbuk1MibjmT6eqS97FzJK-6RP6gXuccE6bCsxw2RM9oOsoPgPhqMLYOVt6iad_tfWDTYaV4sVvqV2mzR-D0R_BsRVxihkyzcQFy8MfPOW5A2v5YRb9WhRoxcoDT_NLUzxL2A5e5QacYXo3vtcd_S1zw7CkgtEvwh8ta750zFP8TEMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ارسالی از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68409" target="_blank">📅 02:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68408">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db5043a70.mp4?token=WBgAwtmT2z_RZ0LSOwDVpb5rlRiURGE36AR6Fn9OZ3fBx_TNCAgImQK9X8GMEEc4pLGuZEx7Jit34Tvh7zPA4Yrc2qUiujcMNc4fCFpw0d5y8Ffx8vpX3TWO2qCNv-umzRKLoJAyCvOn2sJkKGOouqfSx9ptOVf1kSxSuYrJr9heVkJjE2IXeEk0AZxxXYF6ioAqYOuV4Y32xe6wx_YO3DaPlxtiw3_GDdzcnMdrsQJQbIZjgAoNIO_PfzKu_YAA3MYquIMrJ0o-b6b_GgGz2OF_-MJOr5ZfNIouQigP6FWFxWQjBztAszoWOtaiGcAnP6LeH2PQhWqAV8pMdAGw1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db5043a70.mp4?token=WBgAwtmT2z_RZ0LSOwDVpb5rlRiURGE36AR6Fn9OZ3fBx_TNCAgImQK9X8GMEEc4pLGuZEx7Jit34Tvh7zPA4Yrc2qUiujcMNc4fCFpw0d5y8Ffx8vpX3TWO2qCNv-umzRKLoJAyCvOn2sJkKGOouqfSx9ptOVf1kSxSuYrJr9heVkJjE2IXeEk0AZxxXYF6ioAqYOuV4Y32xe6wx_YO3DaPlxtiw3_GDdzcnMdrsQJQbIZjgAoNIO_PfzKu_YAA3MYquIMrJ0o-b6b_GgGz2OF_-MJOr5ZfNIouQigP6FWFxWQjBztAszoWOtaiGcAnP6LeH2PQhWqAV8pMdAGw1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک به سمت پایگاه های آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68408" target="_blank">📅 02:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68407">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:
دو انفجار در خرم آباد شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68407" target="_blank">📅 02:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68406">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:
از تبریز موشک شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68406" target="_blank">📅 02:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68405">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f8e07bfa.mp4?token=hp-EdZSKwKuZ7nwdTA-IqET7QqywB6tZbbIcUJHyUPWDwpUKwIKJ2L-XFrD28cHuh7-l9tOgzGAwjb9DCMRH8uCPZJVI4u9VfRk0no1WSSAGVnUmDVos2I_7BrkNzYGZXkyGdHuyRCxHyv253Nrz5cNNSLBgPQpFKRC18vxVHtzQtO3NNedpnVyC8j79kg8RbP3rDOIsyJcR9uuDCdqqR9iPH00Pn6T_JrAENzjYE3qA6JtnofufutHnlJjsHdpULbhBWqa4noD70UAbUvsoKqBGcgZrAFkEnpTh8qHLyse5cwHJhG3qYIOCpf72Zsp5AsEEoLANWb1Pc7SOWgyzCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f8e07bfa.mp4?token=hp-EdZSKwKuZ7nwdTA-IqET7QqywB6tZbbIcUJHyUPWDwpUKwIKJ2L-XFrD28cHuh7-l9tOgzGAwjb9DCMRH8uCPZJVI4u9VfRk0no1WSSAGVnUmDVos2I_7BrkNzYGZXkyGdHuyRCxHyv253Nrz5cNNSLBgPQpFKRC18vxVHtzQtO3NNedpnVyC8j79kg8RbP3rDOIsyJcR9uuDCdqqR9iPH00Pn6T_JrAENzjYE3qA6JtnofufutHnlJjsHdpULbhBWqa4noD70UAbUvsoKqBGcgZrAFkEnpTh8qHLyse5cwHJhG3qYIOCpf72Zsp5AsEEoLANWb1Pc7SOWgyzCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
گویا پل یا پل‌های دیگری در میان راه استان کرمان به استان هرمزگان هدف حملات هوایی آمریکا قرار گرفتند:
پل گلوگاه بعد گنو بندرعباس و سرزه جاده رودان'
صدای ویدیو: راننده‌های سیرجانی اصلا سمت بندر نیایید ... پل بعد گلوگاه رو زدند همه ایستادند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68405" target="_blank">📅 02:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68404">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68404" target="_blank">📅 02:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68403">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
منابع داخلی:
چند محور مواصلاتی هرمزگان در پی حملات آمریکا مسدود شد
؛
⏺
بر اساس اعلام منابع رسمی، تونل شهید میرزایی در محور بندرعباس ـ حاجی‌آباد در هر دو مسیر رفت و برگشت به دلیل حملات دشمن تا اطلاع ثانوی مسدود شده است.
⏺
همچنین پل «شور» هدف حمله قرار گرفته است.
⏺
بر پایه این گزارش، پل محور رفت در مسیر سه‌راهی میناب به سمت رودان، پس از دوراهی سرزه، نیز مورد حمله دشمن قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68403" target="_blank">📅 02:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68402">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwmSj62jiiqA8sG2SA5dVqIcyMcqqqClEQUsi2DqAamVFqsg1aalsK6VABIxwx9gyiPxMAdN4UwXLqkHejpOYdhy4AHDBqlwP1MrPcb4fgQBTqqsBwSgQHT8LluRtoS97JsDN-30XWDrM_ylX7cz7kbFV4CfuWNxV91Le3GMCS_O7eXUrDphX8tXTUoP_g4L0zePACdTJ7eO2PwEekZ-ovDY_44snxtGBZzcOQnOyXgpWLVTb6eaE_0Zqr2wAFNyEixZAn-sXlZ4CqeyYPLnfErqCl34XvtbMbIXSagMFsTHKmKQ6Wg4sMfTBwr_AJrXt7le_jJtMvPfn6iC8pTyfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
پل مسیر بندرعباس رودان هدف قرار گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68402" target="_blank">📅 01:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68401">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871564b347.mp4?token=aQMTG7LHqf7muRCzHz7mzeEWC8lX-ZXrmRc-sb41uGdq08DbaggkhnJaeMm68_I58uOUNZ_Rc9oyoseFoLOK2isGIyId9TmpsrikWOx4uqivpNwzLDGcZZjkOSUDLtdCtFw7FdlBMZFA1ngbPVM5cpyJ4Jj8MAfxGSSaG6I1WIzb8k7uhenAlppOoNPuCJujm84pVCxDqTNa9F4l29RZRizx5e72l3tzAEaKxOzBQF-DO2hbNMG0XweRtVxz7vnr1BB9S0gOKLHR9qUh_UJzOmkGKGRlb-2f2x_YfyMQvmJnxYf2q0Kk75myPF8ytSYM5FFcuywut0TWbBNY_K38Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871564b347.mp4?token=aQMTG7LHqf7muRCzHz7mzeEWC8lX-ZXrmRc-sb41uGdq08DbaggkhnJaeMm68_I58uOUNZ_Rc9oyoseFoLOK2isGIyId9TmpsrikWOx4uqivpNwzLDGcZZjkOSUDLtdCtFw7FdlBMZFA1ngbPVM5cpyJ4Jj8MAfxGSSaG6I1WIzb8k7uhenAlppOoNPuCJujm84pVCxDqTNa9F4l29RZRizx5e72l3tzAEaKxOzBQF-DO2hbNMG0XweRtVxz7vnr1BB9S0gOKLHR9qUh_UJzOmkGKGRlb-2f2x_YfyMQvmJnxYf2q0Kk75myPF8ytSYM5FFcuywut0TWbBNY_K38Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره پسرش بارون:
پسر بسیار قدبلندم، بارون. بارون عاشق فوتبال است و یک بازیکن خوب فوتبال است.
نمی‌دانم، سرعتش... من گفتم، وقتی یک بازیکن از اسپانیا، آرژانتین یا فرانسه از کنار شما رد می‌شود، بارون، چه اتفاقی می‌افتد؟""چه اتفاقی می‌افتد، بارون؟"
او گفت: "بابا، من یک توپ‌گیر خیلی خوب هستم!"
من گفتم: "اما بارون، اگر او سریع‌تر باشد، چه کار می‌کنی؟"
او گفت: "بابا، او هرگز از کنار من رد نمی‌شود!"
"من گفتم: "اما اگر این اتفاق بیفتد؟" و او نمی‌خواست به این سوال پاسخ دهد.
به نظر من، سرعت در این ورزش بسیار مهم است، شما موافقید؟"
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68401" target="_blank">📅 01:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68400">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
تسنیم:
حملات مجدد دشمن آمریکایی به اهواز، لار، یزد و چند شهر ایران
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68400" target="_blank">📅 01:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68399">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a69d92f06.mp4?token=kACtIKrvWbhSsw4xhig-YxB4OnYpmjxthFlI6E-wq6UrQbe7pjFva1M0ZuzxdwWjboB_3P88FFsiS2_Xch_k_q_VSluN8fKaEXRFPr2uyE_WLDqmJWptdC5JdXzIZ_-bMhfKI3tGkZlSNJAcQjQy9TPR_Hj8DU2Pq0p7vXbbgSZ8t1AJpWgSpcBMm4JS5_9zr-cJQFzC3CLRzQcS92jzzcCzxo0UA3mXm_pJ1Ck0IwS_n9Lt0pYVoWO49pdO94jTUxyksVhQei3OAKWTc6BeT3PaQOZZGkiQYPaVpSdoghAp9F9le-FKouEcwB-hnrUFFhR-1_7gBuZeq1CJGfDnYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a69d92f06.mp4?token=kACtIKrvWbhSsw4xhig-YxB4OnYpmjxthFlI6E-wq6UrQbe7pjFva1M0ZuzxdwWjboB_3P88FFsiS2_Xch_k_q_VSluN8fKaEXRFPr2uyE_WLDqmJWptdC5JdXzIZ_-bMhfKI3tGkZlSNJAcQjQy9TPR_Hj8DU2Pq0p7vXbbgSZ8t1AJpWgSpcBMm4JS5_9zr-cJQFzC3CLRzQcS92jzzcCzxo0UA3mXm_pJ1Ck0IwS_n9Lt0pYVoWO49pdO94jTUxyksVhQei3OAKWTc6BeT3PaQOZZGkiQYPaVpSdoghAp9F9le-FKouEcwB-hnrUFFhR-1_7gBuZeq1CJGfDnYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
دموکرات ها در انتخابات تقلب کردند، و من چه چیزی نصیبم شد؟ جام جهانی نصیبم شد. المپیک نصیبم شد و آن‌ها را به اینجا آوردم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68399" target="_blank">📅 01:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68398">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در لار
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68398" target="_blank">📅 01:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68397">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
دو فروند کشتی نفت‌کش با عبور از مسیر مین‌گذاری‌شده جنوب تنگه هرمز منفجر و دچار حریق گسترده شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68397" target="_blank">📅 01:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68396">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08d972ece2.mp4?token=OYWeKiIQHJ_gpNQmWQkaLkli6bn0DTqDK7NnsHITOj7tK-tROCLu4mOjOQ_iJPpqAMZPpchDTFIORilt263U7XY3G_HRpciBVga1gUnnt7Aw4vmcJ5u42yLkQ2G-awdd4zl5mybwjbefg6Bk58J2KRI_n2iTDckPYB6c9-2mk4rEN9mVg43HfQ-imnOqI4W_brrkgpUSx6HMXzR9EijhTm2kvKEaWEf_nhAiFpJLTOR1So8ZcnoEtDyOf8b61fUXN2UvocSw40a46zTg0l2syKJQRyf0kYh7ofoROj8n-KHiYa0CHw9B1G5iumuzooJ4s0vby53SBRveDmiLPZ44oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08d972ece2.mp4?token=OYWeKiIQHJ_gpNQmWQkaLkli6bn0DTqDK7NnsHITOj7tK-tROCLu4mOjOQ_iJPpqAMZPpchDTFIORilt263U7XY3G_HRpciBVga1gUnnt7Aw4vmcJ5u42yLkQ2G-awdd4zl5mybwjbefg6Bk58J2KRI_n2iTDckPYB6c9-2mk4rEN9mVg43HfQ-imnOqI4W_brrkgpUSx6HMXzR9EijhTm2kvKEaWEf_nhAiFpJLTOR1So8ZcnoEtDyOf8b61fUXN2UvocSw40a46zTg0l2syKJQRyf0kYh7ofoROj8n-KHiYa0CHw9B1G5iumuzooJ4s0vby53SBRveDmiLPZ44oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به یزد صدای جنگنده
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68396" target="_blank">📅 01:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68395">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خفه شو کصکش
#hjAly‌</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68395" target="_blank">📅 01:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68394">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇺🇸
ترامپ: هری‌کین هم خوبه ولی ممکنه تو پست اشتباهی بازی کنه
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68394" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68393">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇺🇸
ترامپ: مسی خیلی خفنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68393" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68392">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇺🇸
ترامپ: رونالدو مرد بزرگیه
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68392" target="_blank">📅 01:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68391">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68391" target="_blank">📅 01:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68390">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
بندرعباس رو شدید دارن میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68390" target="_blank">📅 01:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68389">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
مجدد انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68389" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68388">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1504ff042f.mp4?token=D5g4GzLox8lBSfkT_nYo7rDEnwwZvJ3NhwyemURbkrHnboMlOPL0_iec1zKi0MLEcqK9Lm3TvVk-8RaXPMom2i_TjedPOdifx2NZsrOgdUwOm7Yzd583hebhWye6GPWyqXKunXkGrq5HxiQIedBG2Ir34hDvU8GI_lfWjc1HNv52_hWVXYK3IYMTN6r8NKgqKk0gCRNLVj0sSwK3MJijiyCEtEPi7Cg5R4k_qCnPSjiC_QtEVmocLlamyRQ38Dvi5ZS7Iq5lvyYBank14C9O57YO2nnA9mvw_ugFP5f9emqwLsfwDEU742lMXWMbSI4iQ00DpeCxB328YJdT3pmRTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1504ff042f.mp4?token=D5g4GzLox8lBSfkT_nYo7rDEnwwZvJ3NhwyemURbkrHnboMlOPL0_iec1zKi0MLEcqK9Lm3TvVk-8RaXPMom2i_TjedPOdifx2NZsrOgdUwOm7Yzd583hebhWye6GPWyqXKunXkGrq5HxiQIedBG2Ir34hDvU8GI_lfWjc1HNv52_hWVXYK3IYMTN6r8NKgqKk0gCRNLVj0sSwK3MJijiyCEtEPi7Cg5R4k_qCnPSjiC_QtEVmocLlamyRQ38Dvi5ZS7Iq5lvyYBank14C9O57YO2nnA9mvw_ugFP5f9emqwLsfwDEU742lMXWMbSI4iQ00DpeCxB328YJdT3pmRTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما ۵ دقیقه بعد از حمله به شهر های مختلف ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68388" target="_blank">📅 01:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68387">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
دقایقی قبل آمریکا به نقاطی در داراب حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68387" target="_blank">📅 01:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68386">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
فارس:
لحظاتی قبل یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی دریایی سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور در آسمان بوشهر رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68386" target="_blank">📅 01:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68385">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c7dd90f1.mp4?token=mss_nlKIwBJPAjYA7hGDMU7vjqAfHN__COE4RRCg1m8X_lU3EUq1ZASVBfOJElbyrGOifwXT0GLQQSXTVNWkHg0GGDyy0YXEb36-ePcnUO8yAKT7llldxHcTd9HEkPoXNw6lvIXHIXh75sD74jVeJHhpaQXKR3F7BGX3pGxu6w73jXENX0HEq8FoDIG7R66ZM7NlUEJrX_5jgm0d0ddxcOtcsMBQsuXFN7lTg_vKzRiaHpPt840a6vbObsM4VGl1bnpH2h3FKvlO_RGKoxPHEpnpVlT01wLtl-F9yNtmttzYPwSuMRio2DiJ2mLh6Sia_Q0ZHr8SdmV-qPlekzelqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c7dd90f1.mp4?token=mss_nlKIwBJPAjYA7hGDMU7vjqAfHN__COE4RRCg1m8X_lU3EUq1ZASVBfOJElbyrGOifwXT0GLQQSXTVNWkHg0GGDyy0YXEb36-ePcnUO8yAKT7llldxHcTd9HEkPoXNw6lvIXHIXh75sD74jVeJHhpaQXKR3F7BGX3pGxu6w73jXENX0HEq8FoDIG7R66ZM7NlUEJrX_5jgm0d0ddxcOtcsMBQsuXFN7lTg_vKzRiaHpPt840a6vbObsM4VGl1bnpH2h3FKvlO_RGKoxPHEpnpVlT01wLtl-F9yNtmttzYPwSuMRio2DiJ2mLh6Sia_Q0ZHr8SdmV-qPlekzelqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به لار
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68385" target="_blank">📅 00:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68384">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
معاون استانداری خوزستان:
دقایقی پیش نقاطی در اطراف شهر اهواز توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68384" target="_blank">📅 00:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68383">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=FMPG0lguTT2LfhmxjuEQ10mn-Ctpq6uWVvphFG0bzh66KtiUwAtQK6CVtveNFm8L5KT_ZGRWbdfGteiGyBgWvriC-uD1wRbu9D8BwLfRYpSG4MYcFjz6j5-3HILNczDW2EOQ_8geEPprfB7yP7CIoAs6sjJ5fLd1x4fH-66BaRdF7462NhClkGYvB0yi4MyLOO66J3X-7FyK6lRyWjLJ_SUq0IeMWUqpgvgWUi-I7_U60xOE5VvlnoSyeXPLgXCrHtaO1GzxcRUKgrPVnZyXMKcpIe0cFIzlXqCQMhHgG6B9gedw1HYxBPAEOjlI39e-9gP9FzhXLxIcperjG2DCTA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=FMPG0lguTT2LfhmxjuEQ10mn-Ctpq6uWVvphFG0bzh66KtiUwAtQK6CVtveNFm8L5KT_ZGRWbdfGteiGyBgWvriC-uD1wRbu9D8BwLfRYpSG4MYcFjz6j5-3HILNczDW2EOQ_8geEPprfB7yP7CIoAs6sjJ5fLd1x4fH-66BaRdF7462NhClkGYvB0yi4MyLOO66J3X-7FyK6lRyWjLJ_SUq0IeMWUqpgvgWUi-I7_U60xOE5VvlnoSyeXPLgXCrHtaO1GzxcRUKgrPVnZyXMKcpIe0cFIzlXqCQMhHgG6B9gedw1HYxBPAEOjlI39e-9gP9FzhXLxIcperjG2DCTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات آمریکا به سایت موشکی یزد
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68383" target="_blank">📅 00:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68382">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ممکنه امشب، سخت‌ترین شب برای جنوب باشه
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68382" target="_blank">📅 00:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68381">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از چندین انفجار در یزد
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68381" target="_blank">📅 00:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68380">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428210a926.mp4?token=Pr7wAcQ5wuNqewOXToEXJHpfbKu5KUrjrn2udTmVctTAoLOzS64_GvuGU_kngt_EuhTtj4T3Oj_DGJaWyfJNbyz1R3qJgOmCuvtBM7vAk6GNlV0Ut2J4agP_4PLTM8iINUf2HJ21fC0MsXmiF9hxcaytjMicOJ4_oqG3G84RiKwDGxAayuryVzqlGGDmGfolHsMTwlbMUnI_PPTyrp87OQgtO0ItwXuPBUitLitI9lbfYDX4rlmFWazOvdBJDVz2rj-337S9ZRTFHbMYrt3zYxlKDD_5E4hIMrDnxlgcNOg0Av6tklGH-iCPSsGRsWYxTMvmDUbctnlWAq6lS1A_iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428210a926.mp4?token=Pr7wAcQ5wuNqewOXToEXJHpfbKu5KUrjrn2udTmVctTAoLOzS64_GvuGU_kngt_EuhTtj4T3Oj_DGJaWyfJNbyz1R3qJgOmCuvtBM7vAk6GNlV0Ut2J4agP_4PLTM8iINUf2HJ21fC0MsXmiF9hxcaytjMicOJ4_oqG3G84RiKwDGxAayuryVzqlGGDmGfolHsMTwlbMUnI_PPTyrp87OQgtO0ItwXuPBUitLitI9lbfYDX4rlmFWazOvdBJDVz2rj-337S9ZRTFHbMYrt3zYxlKDD_5E4hIMrDnxlgcNOg0Av6tklGH-iCPSsGRsWYxTMvmDUbctnlWAq6lS1A_iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتسب به حمله آمریکا به لارستان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68380" target="_blank">📅 00:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68379">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
گزارش ها از انفجار در لارستان استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68379" target="_blank">📅 00:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68378">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
انفجارر
بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68378" target="_blank">📅 23:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68377">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
سیریک و اهواز انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68377" target="_blank">📅 23:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68376">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
قشم رو وحشتناک زدن
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68376" target="_blank">📅 23:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68375">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
دو انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68375" target="_blank">📅 23:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68374">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68374" target="_blank">📅 23:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68373">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
انفجار ها در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68373" target="_blank">📅 23:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68372">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyEx90SaynfjDVaW-_la9528X-98vj5HyZx5idUSmrZU7uz4AZvt1pxCRobYadoRHtds4_NzWXqAR5S2Pkn6_XCEOmpsIggjfW4qwCyqfgzldbQEsMIwx9KpmkgZFQrOsDISnY6850O63h9gm0bDjzALhKcnPhgprm2osvsX2GBQZPcTXVVZnxrxEHVu0TpoCVgzJh2OTlabZkxo58TqGGUwrFAH_FhOOaRvWncWOtzTBXQHoAx98sZ8C65XvOB2gg67sGWg9iD8TvWL1d8d29ffGPTo5VWwbowY2S-jrO1imXJsBJMG6sO0pv7IovKUNrY2B2nEtONhfbfAHutGzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
سنتکام امروز ساعت ۳ بعدازظهر (به وقت شرقی) و برای هفتمین شب پیاپی، دور جدیدی از حملات را علیه ایران آغاز کرد. این حملات با هدف تداوم تضعیف توانمندی‌های نظامی ایران و بنا بر دستور فرمانده کل انجام می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68372" target="_blank">📅 23:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68371">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
با اعلام سنتکام دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68371" target="_blank">📅 23:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68370">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‼️
عجیب اما واقعی، حمله‌ی گداوند به علی‌آقا دایی:</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68370" target="_blank">📅 23:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68368">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJzD4aRQ7kkwcgWkIGI78xbrQadz3cKJ0I77ZdoW71jRDVvL0srtYWV_wSRdi8bWxACwPm62LQ9nJqBh7U8OpIEWgoTOl0s6a_dMkrjcewVgqrmQ7d59vk_8eBRkXVT0stYQUrwqyNGmCkTsito0rIcd7T7pd05PC7sW9zKIhPDnh7B9HGsBO3XcTOh4z1wDtrnS9E1KhnVae1B8pc4p_59buJkFKgVcHAsNwY8tpguZwqjS6_vmVxxrb4DJTG66cN2QnAplGjAMsmRxduAofWIa_B4DmYYJKSlB1vD5J6cDxSbYnXuRFAjDVRYI6QzBcIxdNCmFh79uPtoQhWBTCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IyGidXffuWhIgLsmKsm_-amrVYOwmUn87SWfUNdN2JHasU8bIRQoVtTBNaUZQ1I1Han7h7wVbRo5N0ZeJ_5nEjCj9ePJgq_kGFxGM9UuCPOXeyXG01Zb0ugbXtI0niWMXs__LRnOv7SeYiFbw5YITNjGgk8vtuiqHtWnkoYdV_--6ABI6EG8rbUkk5VKhjZdFcJQjapsMGffPBu4UmIOXisI9eQxyoBKL300RmcMpqo5AixZwlvZ4BgxC705bMtoWRzH2P7FcK6zqce3nqMRw-RoiMxwlnLQqQXc2FX4mO9AUodGhKZlo6nYEkT6PehfvqX65yU551ywIZuAD_eI-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
عجیب اما واقعی، حمله‌ی گداوند به علی‌آقا دایی:
علی دایی رانتیه و آرزوی بمباران ایران رو داره
!!!
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68368" target="_blank">📅 23:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68367">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2add3c110a.mp4?token=K75jwSK9RG-Fjfim2YqQ4O3jvUY8CaW1HsRlQ5tpJnUNJ39PMhVT3IYfEcdyNPsRCE10k_cz3bbJA-1_JzQzigWmzvMiJYjwQOllTV4Xxt8k1bVPNflIl_7_n8UMIr1E3m6bt24T1zsv3xZuUlbv9ZPIAK0SLR0sdZnJKq7PwWY-jXzcYJRHEKoE6TpcDVRlPUviRk-h5yXUiTerXNWetXUZgCZCT6Q6-UJWpIdgmYCuhTTKBDlWTVKS_9_4OIm_UzZhzDzHdK0OEo5KUgt-k1dJ5aDgnSFZvtp2GUQ8xjPv6AjkxdGDYGnOZxP-hnORO_5q-9k07fJihcW3Rkcm2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2add3c110a.mp4?token=K75jwSK9RG-Fjfim2YqQ4O3jvUY8CaW1HsRlQ5tpJnUNJ39PMhVT3IYfEcdyNPsRCE10k_cz3bbJA-1_JzQzigWmzvMiJYjwQOllTV4Xxt8k1bVPNflIl_7_n8UMIr1E3m6bt24T1zsv3xZuUlbv9ZPIAK0SLR0sdZnJKq7PwWY-jXzcYJRHEKoE6TpcDVRlPUviRk-h5yXUiTerXNWetXUZgCZCT6Q6-UJWpIdgmYCuhTTKBDlWTVKS_9_4OIm_UzZhzDzHdK0OEo5KUgt-k1dJ5aDgnSFZvtp2GUQ8xjPv6AjkxdGDYGnOZxP-hnORO_5q-9k07fJihcW3Rkcm2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
آرش اعلایی به جی دی ونس گفت مادرجنده
😂
:
جی دی ونس یک مادری داشته که هروئینی بوده و مدت بسیار زیادی به مواد مخدر اعتیاد داشته
مادرش پشت سرهم مجبور بوده از یک خونه به خونه دیگه بره
جی دی ونس یک کتاب داره که توش نوشته چندتا دوست پسر مامانش داشته و چطوری دوست پسراشو میاورده خونه و چقدر کمبود داشته
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68367" target="_blank">📅 22:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68366">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767b27f10a.mp4?token=Z0nx3hzUOU4SuID2gcKmOxYzoNbHi-HR8reuQmPRif2_ZdcP6gxSXh9hEKgJZKBu6TCPzZ6g48JLu5qZKAUwDzWZWpOVDpGBIgW4yypnS9uEK4-kOZy_XlJatfLv_1HVZoco_Ls6u2kv-BHCUNQC-uT59yWClFeOE6i03FmwsPo_bzcFyJZZlcIAOvlvZH97aWNQ7Ag6auwycpdkrXteo0ppHco3iZYmyYFsUxsU-MK70MShYm7v_P9oWMDKiZmJTGFLeSk5mGs6ILI6YIQ1Xb1TkgpnQIxWFh_99S3ydMvGcYlIZxQb7UKV02UgR8KLozFaEkCrx6YchDk7xjB9RbGt8T5VSiVzGHeAP0T-5HUszjHOhRLCYVnqWgcJWIbnvSMqpZe5forw5o-pkGwefUvI8jxjOx8QGkBzK6i-MzIHJKrqzCz5myRBnigSL82KsyS_4D4wIFDRRAXS3tuXLiLyIHRKMfw4yrmEcMPlHgG8KAoees3AZKAfGlaRRRXht-u9fQ3FIqpyE1IZBxV2b52SMc3mN9M9iG2j9wNooDFj4KUTLcACKXZ74DOqBedwnNf8d69GZo1_tdTpBfXOXjnla9S883zV99ySSAHJrDsu2NZJ3qpCAu2VtFpjROoNDD54Gfy1Kdt3UrswITwN8h3JE8vDkOAiAYc48YEIq50" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767b27f10a.mp4?token=Z0nx3hzUOU4SuID2gcKmOxYzoNbHi-HR8reuQmPRif2_ZdcP6gxSXh9hEKgJZKBu6TCPzZ6g48JLu5qZKAUwDzWZWpOVDpGBIgW4yypnS9uEK4-kOZy_XlJatfLv_1HVZoco_Ls6u2kv-BHCUNQC-uT59yWClFeOE6i03FmwsPo_bzcFyJZZlcIAOvlvZH97aWNQ7Ag6auwycpdkrXteo0ppHco3iZYmyYFsUxsU-MK70MShYm7v_P9oWMDKiZmJTGFLeSk5mGs6ILI6YIQ1Xb1TkgpnQIxWFh_99S3ydMvGcYlIZxQb7UKV02UgR8KLozFaEkCrx6YchDk7xjB9RbGt8T5VSiVzGHeAP0T-5HUszjHOhRLCYVnqWgcJWIbnvSMqpZe5forw5o-pkGwefUvI8jxjOx8QGkBzK6i-MzIHJKrqzCz5myRBnigSL82KsyS_4D4wIFDRRAXS3tuXLiLyIHRKMfw4yrmEcMPlHgG8KAoees3AZKAfGlaRRRXht-u9fQ3FIqpyE1IZBxV2b52SMc3mN9M9iG2j9wNooDFj4KUTLcACKXZ74DOqBedwnNf8d69GZo1_tdTpBfXOXjnla9S883zV99ySSAHJrDsu2NZJ3qpCAu2VtFpjROoNDD54Gfy1Kdt3UrswITwN8h3JE8vDkOAiAYc48YEIq50" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ای که گفته میشه مربوط به کشتی تایلندی هست که مورداصابت قرار گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68366" target="_blank">📅 22:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68365">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🇮🇷
یک کشتی تایلندی در تنگه هرمز هدف حمله سپاه پاسداران قرار گرفت.  @News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68365" target="_blank">📅 21:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68364">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🇮🇷
یک کشتی تایلندی در تنگه هرمز هدف حمله سپاه پاسداران قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68364" target="_blank">📅 21:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68361">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b42e3ed3a4.mp4?token=BP7JHe2kI0jtEGqvit6aMMrOTwHa-EgLYO3D7PaHkU_JFKwUj52DH5grB4KPmB1_iq0dfdn6xHlJHNuGu4rZMI2YltI91xfbGo1eYa7YM3f2I9XzTF7lysk-LBCwRF1wlWMv67LzpSg8mK9bfioyYwLlciFxd_Bz3O6eUyhz6LwUyjrmoaCni7W_EMuoezkD9XpUcXTQV9U6wQO_jsfQGQcP9lVKHL3zfkP2aPPFb5WTA3aCywKS60HxjMEoq6dmepVx8BfGSrQ74EU2mDEAdV_d2tIdDOK__l4UejotaL_ASDDj0rWiBwQ3Ek4p5IpiNUbZDpmpqNn-5DEe9Vnafw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b42e3ed3a4.mp4?token=BP7JHe2kI0jtEGqvit6aMMrOTwHa-EgLYO3D7PaHkU_JFKwUj52DH5grB4KPmB1_iq0dfdn6xHlJHNuGu4rZMI2YltI91xfbGo1eYa7YM3f2I9XzTF7lysk-LBCwRF1wlWMv67LzpSg8mK9bfioyYwLlciFxd_Bz3O6eUyhz6LwUyjrmoaCni7W_EMuoezkD9XpUcXTQV9U6wQO_jsfQGQcP9lVKHL3zfkP2aPPFb5WTA3aCywKS60HxjMEoq6dmepVx8BfGSrQ74EU2mDEAdV_d2tIdDOK__l4UejotaL_ASDDj0rWiBwQ3Ek4p5IpiNUbZDpmpqNn-5DEe9Vnafw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت اقلیم کردستان پس از حملات جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68361" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68360">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
📣
اولین واریز خود را با هدیه 100%
تا سقف 100 میلیون ریال
دریافت کنید و شانس برد خود را افزایش دهید!
🌍
پشتیبانی از
ارزهای دیجیتال
برای کاربرانی که به دنبال روشی سریع و آسان برای تراکنش هستند.
✅
قابلیت پیشبینی در لحظه
و استفاده از استراتژی‌های متنوع برای بردهای بیشتر
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68360" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68359">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQ4BpMO0xyBPRanBauXDDj6AJTx0t0UIhEx7jHdhmO1i4dHEeVXrWzyTMvoGwFuuUBglBQ5x85XsxSpwmdnKBjuV9GU5banyVBV9zudRwOJGFdswBozPOnz9nu0rb071JAuoTUxkZUguO3HszOt3Msp2Z_20zqi-wYN87pq-bi2RzSx9SqozafcKt8CNviRqHDPM6EvE5VBCzqgQRCTORoTVNBEO_iIEHO-Eeveu4BNexOkcaxtNECX5UFHP5D30WQ5L3BYfEqyG5UYz7zR0B9fBlmQNTLcNn-VOqCCQ_vxMR-VGko1GmTTw91eIQvR5dLGfH3Po6vQsO16U_AMj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🏐
والیبال لیگ ملت‌‌ها
🏐
ایران
🇮🇷
-
🇸🇮
اسلوونی
⏰
شروع بازی ساعت 21:30
✔️
امکان شرط بندی با مبلغ نامحدود
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.100.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68359" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68358">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4YlbkSxd_4qt-wLhMSBb1rm1iKnN6cWEM3-fR3Ql5dNtmo-ugIGV3bgpAwZbGDE45MSfKGcFyqmMZVStazQ1jbM_8JbvA20F-h289_vES0E3a4HC446v95Te4dvqDQE3KAyiXkIHqysALmlM6ibVINA-ElVFREs3EeJEehW5eCtd-m5SRj-ivROO2joZodo15HtbA-khirKebddTmkYZ62NUra3_A7_PGjYUu99dVTycACnpBHCgngT0vDb850_kIC61l1EDumVOl9CI9P16uvlwYmvlh54duhuHbbmKsyZzkZ_c5seA7pK34PN1kB479XvQcbfv5832N_8xR9sTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تعداد بیشتری از جنگنده‌های آمریکایی مدل F-16 که از اروپا به این منطقه اعزام شده‌اند، با پشتیبانی هواپیماهای تانکردار KC-135، در حال استقرار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68358" target="_blank">📅 21:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68357">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45585f31bc.mp4?token=E4t6LU4cNrqr3BeryLU6mbTq37VXcMmxCy-bAGasljdu5TDCfzPH1mFmbW9FRvFq89VblqIveZxJ3E48ce6pVJZ4B0JmPun4BA5YG-9rLcO3AqBU2hn-bN6yYBjo_bHIptu4bcJGwxoYzf9zCfmarewL2VwnV5ENVgf-eUsStyZ_nDOmOvjeSttsDfrhvSUdAc9SDmzqIf4wGEZc5lbRyJatuvc8vXWnCU-KBzGxM6oXiLnRPQTejDqCQKijYSRnsZYNGwAJ9FNsakfUn4LIToA6r3crzQesBKRRuIPqjh9Ge9ajiKomTL_y8yFt0LalR-BcRmuYmMSvHPwDiSikAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45585f31bc.mp4?token=E4t6LU4cNrqr3BeryLU6mbTq37VXcMmxCy-bAGasljdu5TDCfzPH1mFmbW9FRvFq89VblqIveZxJ3E48ce6pVJZ4B0JmPun4BA5YG-9rLcO3AqBU2hn-bN6yYBjo_bHIptu4bcJGwxoYzf9zCfmarewL2VwnV5ENVgf-eUsStyZ_nDOmOvjeSttsDfrhvSUdAc9SDmzqIf4wGEZc5lbRyJatuvc8vXWnCU-KBzGxM6oXiLnRPQTejDqCQKijYSRnsZYNGwAJ9FNsakfUn4LIToA6r3crzQesBKRRuIPqjh9Ge9ajiKomTL_y8yFt0LalR-BcRmuYmMSvHPwDiSikAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترافیک تنگه هرمز در ۱۶ جولای به کمترین میزان در طول سه هفته گذشته رسید و تنها هشت کشتی از این مسیر عبور کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68357" target="_blank">📅 20:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68356">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
تعداد قابل توجهی سوخترسان در حال اعزام به خاورمیانه است</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68356" target="_blank">📅 20:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68355">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ab397d50.mp4?token=JUus4ju4kSrhXwa1wV4KM9rdQKd6HdS5w2zRzTmZi60gC3g2FqIJr0TvN0opUwzVvpbau8zczr7_zxd1GfODv3ADYc8327fhaODREYTztnpcjZi0gcV40GB2P-CMPf_yIuMHKTVtOTdRwBX77RA0cL-Vq4qEcyG5bPcBXeWUEGyJ9PwbDKngSE_1e58gsZ5BKlkjvVZzBSNBUZj8WAq2QvKyn4IemzmXSMZHzkQLOURuLHGVastD74r1sgh6sycRqm-vefNv-iJRJudA2erDOq-RHcHK_aQCJwUvztQSHJaWzZn-zjd45bWw8hr9H_pwtPcmQmwRbeJsLc8KGI3R1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ab397d50.mp4?token=JUus4ju4kSrhXwa1wV4KM9rdQKd6HdS5w2zRzTmZi60gC3g2FqIJr0TvN0opUwzVvpbau8zczr7_zxd1GfODv3ADYc8327fhaODREYTztnpcjZi0gcV40GB2P-CMPf_yIuMHKTVtOTdRwBX77RA0cL-Vq4qEcyG5bPcBXeWUEGyJ9PwbDKngSE_1e58gsZ5BKlkjvVZzBSNBUZj8WAq2QvKyn4IemzmXSMZHzkQLOURuLHGVastD74r1sgh6sycRqm-vefNv-iJRJudA2erDOq-RHcHK_aQCJwUvztQSHJaWzZn-zjd45bWw8hr9H_pwtPcmQmwRbeJsLc8KGI3R1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماهیگیران ایرانی یک پهپاد انتحاری آمریکایی مدل "لوکاس" را که سقوط کرده بود، از تنگه هرمز خارج کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68355" target="_blank">📅 19:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68354">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_P8kp4DSVnLRd9VHIbe2BJmtn0IDlrUxMDOBjKux_A_iqY5X_LyCkbKClhLu8IulG97dQgpCwJFg_r7QzNh8oG8FKgBE_pqv-YssF1q3vihk6Hf1rBE6fyHGDzTetOb6EI-7TtUqvcuzQLTMhjW2yeLyauhyubUqXe-DWqlQsqEc0gOF59zhGjZQ6QeaE1p1CgNIKY6Hn5TuGsjpuMv9yzqdq-Rfr8-kdKZzAEHPYn6Izq6KFOeLkVW6FYx1MnZHNEseX3HOEGrQrRZ4bm7n_vF07U5pWRIqsbOE14wTGAZacmNzfenBIvX5t069sD6WY6vuuuSFCAUlaqGRBAoyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
رویترز:پاکستان به جمهوری اسلامی درباره حملات حوثی ها به عربستان هشدار داده و این اقدام را تعرض به خاک خود تلقی کرده است.
حملات این هفته حوثی‌های یمن - که هم‌پیمان ایران هستند - به عربستان سعودی، موجب نارضایتی پاکستان شده و این کشور را در معرض خطر کشیده شدن به این مناقشه قرار داده است؛
امری که می‌تواند نقش احتمالی آینده اسلام‌آباد به عنوان میانجی میان ایالات متحده و ایران را پیچیده سازد.
پاکستان که دارای تسلیحات هسته‌ای است و ماه گذشته در دستیابی به توافقی موقت در مناقشه میان واشنگتن و تهران نقش میانجی را ایفا کرد، سال گذشته یک توافق‌نامه دفاعی متقابل با عربستان سعودی امضا نمود و هزاران سرباز پاکستانی به همراه یک اسکادران از هواپیماهای جنگنده به این پادشاهی اعزام شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68354" target="_blank">📅 19:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68353">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPsQyKFaUfHPL_25N0lFDuYUxpLqUe7cItBgk4V9Z7r4W7h5hPEb9CYELlMG5BvfyOmizkStofic14Vxbfukh7jySp1BqXB2qqTZ6WFXRKXgzQ2tLHL-Z5CC8wwvfF6Fio70xQ29BBWYvXdCM3PEvA-1oxGXNQ3BzpvvUqsQtY_82KmTNoWntbpGMLE4uPPzK87Xl6TLubRSm9PHFBfT5wirX7DYekigSVKjuPZ8cix2pE9-Y5taIyjfKsebu-fAIgdxYCN45mgQCEYqjyxZdNpMX4bGMUB-PkZGfmJhPXgMTo1Nd4M9GrENIN9813uXZHcWoWZL-WcgInci31X5-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
❌
ادعا: نیروهای ایرانی مدعی‌اند که به پایگاه «التنف» در سوریه حمله کرده و در جریان آن، نیروهای آمریکایی را اسیر یا کشته‌اند. این ادعا نادرست است.
✔️
واقعیت: اخیراً هیچ‌یک از نیروهای آمریکایی در این منطقه کشته یا اسیر نشده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68353" target="_blank">📅 18:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68352">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3270052e5.mp4?token=NepA_-bQAEqgvY5y54B4s08QagwhNNlb8bmlhBGse3RAJ7JKbVfkWoEVJgOwWP-cDBpr-26KqJsxrEyB6q3NvkY4USQmlOcZvbIfZ67FaiNYl-V5bncPTJ1-4btOuaM99gWNaAM09R8vsgsClDerlL4HyBmajWDnxFZf8bBx0MRtkyk0QJclo5W2f_t3yAL5ySvzBHZKXy1HpT4uy60I3A7pOwy_AJdfTvB8fYLoRiXKEQqS6vAYT_HNknnBhFO4pv8UjqpsbknFrP1-73-sPnFd0rkKs_w_tr0RdFu-HDGPi39hYLWFmOdkAZiHIiWRuhsRxj_t8x662JN7LEFV0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3270052e5.mp4?token=NepA_-bQAEqgvY5y54B4s08QagwhNNlb8bmlhBGse3RAJ7JKbVfkWoEVJgOwWP-cDBpr-26KqJsxrEyB6q3NvkY4USQmlOcZvbIfZ67FaiNYl-V5bncPTJ1-4btOuaM99gWNaAM09R8vsgsClDerlL4HyBmajWDnxFZf8bBx0MRtkyk0QJclo5W2f_t3yAL5ySvzBHZKXy1HpT4uy60I3A7pOwy_AJdfTvB8fYLoRiXKEQqS6vAYT_HNknnBhFO4pv8UjqpsbknFrP1-73-sPnFd0rkKs_w_tr0RdFu-HDGPi39hYLWFmOdkAZiHIiWRuhsRxj_t8x662JN7LEFV0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
در ۱۶ ژوئیه، نیروهای ایالات متحده با موفقیت برج نظارتی بندر شهید کلانتری چابهار را منهدم کردند؛
سازه‌ای که بخشی از شبکه نظارت دریایی در امتداد سواحل ایران در دریای عمان بود و دهه‌ها توسط سپاه پاسداران انقلاب اسلامی برای ردیابی و هدف قرار دادن کشتی‌های تجاری در حال عبور از تنگه هرمز مورد استفاده قرار می‌گرفت.
انهدام این برج، مستقیماً توانایی سپاه پاسداران را برای هماهنگی حملات علیه خدمه غیرنظامی و بی‌گناه کاهش می‌دهد.
علاوه بر این، این اقدام از آزادی کشتیرانی در آب‌های منطقه برای تمامی شناورها محافظت می‌کند، مگر کشتی‌هایی که قصد نقض محاصره دریایی جاری ایالات متحده علیه ایران را داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68352" target="_blank">📅 18:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68351">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c7b1cdf5.mp4?token=cyPWiTnXWBGvWjqCxJOyCs-FPanJy5oMWHX1weMSuV1F8P4r8ui8GEdoW2_iOipxtnCSh_rlcGH51SE84G0P3HtDi8-jGxSJgWRmll3StQuJaX1sDE22T6eAR1cd4AtMGM-KiCNY9mSQNeBGvx7W96iCpgkDHC2jlNLuVlFM8CI2XBkACrBsA3eOO2B4V6VbblX0cWDZJ2iIXIkZqLKTWFwas-IMxsTUY26tAY6lbXOnzLPVczSiyImNUE5NrxTxwSX0fOVh6SCQ-tIh9ItU0nQldL9Ubv7BdHyaYSBKxoidw_3F3Jvz-40JEgjh8vrBuaP-L6TgbQB4Aik-2mvmVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c7b1cdf5.mp4?token=cyPWiTnXWBGvWjqCxJOyCs-FPanJy5oMWHX1weMSuV1F8P4r8ui8GEdoW2_iOipxtnCSh_rlcGH51SE84G0P3HtDi8-jGxSJgWRmll3StQuJaX1sDE22T6eAR1cd4AtMGM-KiCNY9mSQNeBGvx7W96iCpgkDHC2jlNLuVlFM8CI2XBkACrBsA3eOO2B4V6VbblX0cWDZJ2iIXIkZqLKTWFwas-IMxsTUY26tAY6lbXOnzLPVczSiyImNUE5NrxTxwSX0fOVh6SCQ-tIh9ItU0nQldL9Ubv7BdHyaYSBKxoidw_3F3Jvz-40JEgjh8vrBuaP-L6TgbQB4Aik-2mvmVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی باقری کنی، معاون امنیت ملی دبیر شورای عالی امنیت ملی:
برای آنکه رهبران آمریکا و رژیم صهیونیستی از وجود اراده جدی برای مجازات خود آگاه شوند، سریال «مختارنامه» را تماشا کنند
😶
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68351" target="_blank">📅 17:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68350">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9bbf6c87.mp4?token=UBQY4yi3IVez_JkHH5CTC7-LAuN0o5eW1VmkhI9QxgRluWraDZ7IoZOXhLuk0dh6GhfAYKFrBngdTQjXhouM48JBCr-vcMEtii1U6R3X94kozUoASyMwi_DoRSTzVyaqJIeVPUNWreEo3HZaOMm6qRzH7dmChCddMy7-CxVmK4fS5AIgUHH13ReYhazL1O_lnDsPg8ZkhnM71qUTtJwmqwFvM71R8NwsIUusb6GYGC6fTk9X6oJOo1FCJRkR65tzF9UOB91eRYKq04FjKwle5IcpWH7dSR7YAhkf1hBhBhS3hyK3vqMh0ufaqe1urCMNHhYJQ2Bzvwnk3WegUJOOVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9bbf6c87.mp4?token=UBQY4yi3IVez_JkHH5CTC7-LAuN0o5eW1VmkhI9QxgRluWraDZ7IoZOXhLuk0dh6GhfAYKFrBngdTQjXhouM48JBCr-vcMEtii1U6R3X94kozUoASyMwi_DoRSTzVyaqJIeVPUNWreEo3HZaOMm6qRzH7dmChCddMy7-CxVmK4fS5AIgUHH13ReYhazL1O_lnDsPg8ZkhnM71qUTtJwmqwFvM71R8NwsIUusb6GYGC6fTk9X6oJOo1FCJRkR65tzF9UOB91eRYKq04FjKwle5IcpWH7dSR7YAhkf1hBhBhS3hyK3vqMh0ufaqe1urCMNHhYJQ2Bzvwnk3WegUJOOVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هم‌اکنون وضعیت پل کهورستان
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68350" target="_blank">📅 17:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68348">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UkZEfzXDpGmKP0IWYJasU1Jr4mPs3pEprzoGjYPzOJVvJI7dRfRra0tyJ0QMYrBiFBWylrmgq2m2-g_XvEITQcosARxFA6f08DvZCiKIoKhVxXuDeE6s6D8sVYOG3dVBb2XINwEOz3pJfrVNnqxbRMlL-Ne4mESRcIk2aMZyVkVc14cijJHHHuSWrSsHBo_1ghTmIzCMY6zz1Yy_LYHJbuRGCXWPYa4moPyyKD8CwPARR-mYC3G-khG8SS3e9Jwm6tRM8AmpazQdh7sxTHDyerSbaDpyZiXBWlcfqUPoSPSc6zbON11SghjooNVOpm9iRiMhb6M2tMx6wlKORT1geg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WZ6caiseyDpPfpFx2rAl34ivahSC16owirmbLO7wbDLHUZZb_dIRkTHEKIo3mI9ZonPH0BXSJf4Yu9c7eB4sUUa7rbx-GdSxuDGhtpM0vuTUH89QmOGk6PKpVRKPs0-Cw0rjfqwMvRYSKUM8kvvOM8LVxBpH0-_Spn-Yc-WKvNL-wy9vJ3A_RkURssaSv-vLlxfhEgu4UdWjP03C_yNN9uRbtq_lQzZcxPiR6IidePaquLB5Cbwtoq7lL6VVtX8FilLI45Zi2vxw6zIpkZk5Rvn7ln9JTN4TDRgxz07uTOGmb0H4_c_JZsIItSjT5BD2URttIHkbwyFuFhoja5q4cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدون شرح.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68348" target="_blank">📅 16:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68347">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAAHP8RaucLpGO7FJcMBaESdhwAT7_vg8GuUrXaPo6hzqmHz6WbVEbn_b4_FTBFQwBXk7jCkbVdXe9ADKpBaFZgETa4kEfYd8n6mgyP0sSXLKlUzE1RHAdjOqgxfR6iAUWrAQ0EoQ9b3btw858h75ySlH5kLLzq2I21cDKveFxdYOq87eSs0g7s4kQP4MJwuOHEv_1XBGIzHGejdVw1fdfa_uJEre2XeQMwfAVGaumrLRDBUi4WNvWrp1vaI3si9i9rX7X1H2XMn2zs5akpE6bjUfj08DDf9bQx14uJY7_zHQrOv0zDA-qDp3_Zqzxsz4VOhcn4m-mS58W3714eYQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سید مجید موسوی:
حملات موثر و هدفمند تا زمانی که صلح به سواحل جنوبی و تنگه هرمز برگرده ، ادامه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68347" target="_blank">📅 16:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68346">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqtBpkwB43W8AxBHCL8XuNGVcmPnKIdHbmhzNQY_CJbhbi0VRTDPjlQGVnkXm5KM4-7wyDnEFb_rKgSAe8Q12vUrXCucD9Pwg21xld-X4qBv-7heBl2tFQdGPusBrE8nl9UVn28nHfWmlddPHZ55zncJ-Cpd65d0uLZOpEr0mfdCWTGRPzNaV87YXn2fe1JLDLzidCHU_lWWUilbRIdaRMFB80Vxo9NYHBRDv3H8pb9Tyfk3Oe02evLw6wVRw58wI0BzLKMstKRipF-m6HDdHLkKQItPtyqghHImD2m4phiSlQ7tDzogJGTceMzG8f87pnAgyvPyd6eeAiqHyfOeEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از قوی شدن احتمال حمله زمینی امریکا؛
بسیجی ها توی گوگل لغو عضویت در پویش جان فدا رو سرچ کردن و این جمله جزو بیشترین سرچی های یکی دو روز اخیر گوگل بوده
🤣
🤣
عرزشی فقط زورش به مردم بی دفاع خودش میرسه تا اسم امریکا اومد وسط همه از ترس ریدن به خودشون
😂
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/68346" target="_blank">📅 15:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68345">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCzM1jtWH0YEwERumhxy7IsmgHTscFjYr52EQYKV2VGUxJhP7-f6S9X2duKwYXh4j0tZsecVJyZI9fo1D20tm5q_CMpUfUMGjkJrYpC9pRQvq46yzjo09A6F87OWVh2VXSawYRQ8lUKr_VhypMkpUJEyFuI4IjF0_PMLBuOSlLP4bOktPeCZk1L3_pOClP4JC5TGOmmtSrC6tKYpg1khrJn9RgisvtPItx8W1HjWq1-8lfftKqY4J6K_s2R8NqPYYxSyZPzgVGKoifgNyygccsbyqNtt8Pmin6RYLNxcmQFVV1o90l8LvW66vJ0DzJn30PZqsA649aZMJogoRFsV9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
همچنان آمریکا در حال انتقال تجهیزات و مهمات جنگی به خاورمیانه
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68345" target="_blank">📅 15:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68344">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=N_2Bqm-RhFywBrXbV_xj_dWrYevZ9HYY2t6E0as2pbw8840CS385Ok3h3sjRJ2Gj8Qiqe98CtVhotWPc5p-R00ZuNks5Lti1RD1k6m8pE21U4yYLw_j4hp6vBY90hB6b1-TPVBMmykc_YRj-ObJs7s7-TVqS8ItqiHnpJdl0VIt-2xv_oWLfSE3KvXM74vDMO37xj_j-SEHh8F3QgMMt9V7cjRXjXIOMwTiUSoEbBtQogiK0pYXsMquFMxkPjWqVNp2_dI3NHTeOYGyFtnyfTDUMXbmdK3QLiafXL6zF6Be5fo-oyjOoK7X5YNz04QGlvGpqWwD9E3S22u-pIxrRSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=N_2Bqm-RhFywBrXbV_xj_dWrYevZ9HYY2t6E0as2pbw8840CS385Ok3h3sjRJ2Gj8Qiqe98CtVhotWPc5p-R00ZuNks5Lti1RD1k6m8pE21U4yYLw_j4hp6vBY90hB6b1-TPVBMmykc_YRj-ObJs7s7-TVqS8ItqiHnpJdl0VIt-2xv_oWLfSE3KvXM74vDMO37xj_j-SEHh8F3QgMMt9V7cjRXjXIOMwTiUSoEbBtQogiK0pYXsMquFMxkPjWqVNp2_dI3NHTeOYGyFtnyfTDUMXbmdK3QLiafXL6zF6Be5fo-oyjOoK7X5YNz04QGlvGpqWwD9E3S22u-pIxrRSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی، تحلیلگر ارشد اینترنشنال :
اگه حکومت تو 18 و 19 دی مردم رو با اسلحه قتل عام نمی‌کرد، مردم خواستار کمک بین‌المللی نمیشدن و الان بچه‌های میناب هم زنده بودن؛
الان هم اگه سپاه تو تنگه هرمز به کشتی‌ها حمله نمی‌کرد، سرباز‌های جنوب کشته نمیشدن.
جنگ طلبی سپاه داره کشور رو نابود میکنه وگرنه ما کشور ثروتمندی داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68344" target="_blank">📅 14:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68343">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
در یک حمله غافلگیرانه به پایگاه آمریکا در العدید قطر یک سامانه راداری بردبلند و چندین فروند سوخت‌رسان آمریکا به طور کامل منهدم و به چندین فروند دیگر آسیب جدی وارد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68343" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68342">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✅
تسویه فوری جوایز
💥
آپشن های متنوع پیشبینی
💥
کش‌ اوت تا دقیقه 90
🎡
یک فلک متفاوت، هیجانی فراتر از همیشه!
با هر چرخش، همیشه برنده‌ هستید!
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68342" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68341">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZgxhDBrWWu6NcT-sRtMiZLCiSU2Yh1W6wBi_wQPfbJ5Ohe1B5oWJk4CsARli0-n2b-IJ_-PY1N1e0XAMQTiQya3Gb_rHbB7JqWqozytSnnU4f9pCDGdJJHIs4vr1G2px5MEjItMD-f90B1yQx5xxmN-hOs7Qa9ES0_K85itnVoTukvw4qnC7bqqYYyRr-5g-nuU8xyHAeH0_C870PgbUueo46yrtes5BPavOFS-F30k6I-A7ftXTAm6L9AQ7X15KY1zl36B6q0xqHR3Bmx9IQq3A9qb-1_v654oRA4uwkSEhSs23EZdHYJEYTByblIGrYQGuKSphD9VNxYXLTMvXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🎁
جمعه و‌ دوشنبه‌ های فوتبالی با بانس 100% میکس ورزشی تا سقف 30 میلیون ریال
🔒
واریز و برداشت با سریع ترین و امن‌ ترین درگاه مستقیم
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68341" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68340">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6f934d59.mp4?token=Des9XarV8sLDF9d_cTLJXFbEPITdGTqLWQpdLY7Qxf4sw3Jk_BObxpGY2TLVg3nG6UXgZKZOeX_8D4nUlSJSHXCJEvyvw9p-K2HGzKVGxUGUhaPTLQkFuTE55MVHn2A8_BDZY2119zbOmU1UUk3g4ys57zduv3v7j1rShhrLJaLI44sdWM4AS7gSjaxVprURL7xwU2KtferAHDNjFBcQ-xsh9k-dHwbbeBnkIDK1Wuq3AZoNhiZ4wb7FjXZ4mIKk52zYrycRCGzp-Dg-22ftdAlJDSJOXLhJA2B5O0rPHwMu_yqFEuAgVbcgEv3dC9x8n3L5vMqA4jFPc4HHiTRkyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6f934d59.mp4?token=Des9XarV8sLDF9d_cTLJXFbEPITdGTqLWQpdLY7Qxf4sw3Jk_BObxpGY2TLVg3nG6UXgZKZOeX_8D4nUlSJSHXCJEvyvw9p-K2HGzKVGxUGUhaPTLQkFuTE55MVHn2A8_BDZY2119zbOmU1UUk3g4ys57zduv3v7j1rShhrLJaLI44sdWM4AS7gSjaxVprURL7xwU2KtferAHDNjFBcQ-xsh9k-dHwbbeBnkIDK1Wuq3AZoNhiZ4wb7FjXZ4mIKk52zYrycRCGzp-Dg-22ftdAlJDSJOXLhJA2B5O0rPHwMu_yqFEuAgVbcgEv3dC9x8n3L5vMqA4jFPc4HHiTRkyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی مطهرنیا در برنامه «با ضیا» به بررسی برخی سناریوهای احتمالی در تنش میان ایران و آمریکا پرداخت و از احتمال حمله زمینی و نیز مطرح بودن سناریوهای دیگر سخن گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68340" target="_blank">📅 13:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68339">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e12e57fa87.mp4?token=V6fNWgd59MsFe2gw2XxFmtCp1RU9W4loEkxtosi7XJD38lRMA4w6Qy0Bm6_lGD6maT3eZGuSCy2s97o4lQ89oaK_nuTA_blhjPiiJgnDSvRe81H5c9fbTQAjksYukRFHKvuSNQT8MGUqK0YLkJvbpHTDhz-54TSkEgAM58L2bLjMYMjwpuD2gd1-zoW9iu1_PQWKbqkPnoh4-jOTwY9F6YPa2gZNS_rD5YyLrdamGynNS8JEGLM2MHRDW5c4qk0KUnxWzVlqwOf2MtXbF2HDV09n4H08ZFVt4jMlmTRchEfiJb-DEwx5sgIs4fi0EBd3232q8_2cfNxyEDx-fQ0MGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e12e57fa87.mp4?token=V6fNWgd59MsFe2gw2XxFmtCp1RU9W4loEkxtosi7XJD38lRMA4w6Qy0Bm6_lGD6maT3eZGuSCy2s97o4lQ89oaK_nuTA_blhjPiiJgnDSvRe81H5c9fbTQAjksYukRFHKvuSNQT8MGUqK0YLkJvbpHTDhz-54TSkEgAM58L2bLjMYMjwpuD2gd1-zoW9iu1_PQWKbqkPnoh4-jOTwY9F6YPa2gZNS_rD5YyLrdamGynNS8JEGLM2MHRDW5c4qk0KUnxWzVlqwOf2MtXbF2HDV09n4H08ZFVt4jMlmTRchEfiJb-DEwx5sgIs4fi0EBd3232q8_2cfNxyEDx-fQ0MGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسلیت به بلاگر های چابهاری!
برج کنترل دریایی کاملاً فروریخت دیگه نمی‌تونید باهاش ویو جمع کنید
🙁
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68339" target="_blank">📅 13:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68338">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8FggjHAfRnktCP02QFMzmPs11Svg45iytYFxrj6MnyEj2bRPehSFXM6boHb2gJX7zz-egCVXIhDFZB2TEVJ61r6IgSII-yOjvN2E-VPQZ333oLwlwJYSbNaQqqOCmVzIpcz89qSS_C5qudJkDG1SSql2sbJznKKRwsrYTP1oiJfKgB90b7pzfu5yAzC2VLa_BIqUXNF0qv-8DWa_f4-FshsXYX5nVDqf7MvoGvGnbUAdQZu8infclD4OJ-ioj_PPh4RV41J0Uwt8ffwOpt9lLEHpob471FxjdvsVVS15pGsSB-tcQ0miUJkeQzjAKJN6NayaF_uqAGDnSah7SJ-9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دقایقی پیش یک فروند نفتکش که قصد عبور از آبهای عمان را داشته است مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68338" target="_blank">📅 12:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68336">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIwTyB9xDiBb3SdoMJC8uR7yKWK5X4TSGi0MdT33Ce9ewXmB4EiVinHUIWC4CxRItXV5hGWIKVyG1CegIzKWnnSggbEMLseBxfMnE3R4jDGsY_PPv_r9LwfqQMpYUvweEjrXPkjQ-1HuANsWvTxBag1lncFK2m1ATsHgAg7YCB6unWmBw-SvcgnfrEXn7e2D4xOyOOgxAUOhuAxLtjpKSLzh6X1o6_l4cZQbbnT_gsr-1D5C38TOMw2SgdXAg_bdqriq2fTjuufcLE3BfwNLqdhLBfEDxyeyB9Uy4xwxho2FYw9-7H4grpn61r5v92HcrxBUwMmvG1XRqaBEyYJgfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzx2fO6HgvnzwOSwjrLtr-x3h8OpULp45Dr_DphRA4kBxkq_514izC44o4p2PgHu6IYx1UXowjOpAZuilbhyXfemPYPlgvQqkf84Iik8Jbh_DH6P6vgcNgRwjyEjaRrtF1AfsUOGuD0u0mVlL4hsORdSWI9NSAHRzs4Kol95YkvTjqFPmbxSa1175fu3t1w7eXvha3fieCUoFoNYCSTnrj1_vIu4dQh4eBD-G2Fr8BhTHs5UBjqG0JZzHGgxW1cWbDfuuBr2iG_RFugpN1-8lATcK77oLFQJuXUHJqLHlmVeiFnyua-aQPirV2VRy4XsD7oEEkhpHFPj3t5qiQQGwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
هگست وزیر جنگ آمریکا لحظه سقوط برج مراقبت دریایی چابهار را در صفحه توئیتر خود بازنشر کرد!
الان فقط یه خاطره از این برج مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68336" target="_blank">📅 12:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68335">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
استانداری هرمزگان: در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.
کدام پل‌ها مورد حمله قرار گرفتند؟
⏺
پل گریوه؛ مسیر بندرعباس، خمیر، لار
⏺
پل بعد از روستای لاتیدان (کلمتلی)؛ مسیر برگشت بندرعباس، خمیر، لار
⏺
دو پل مسیر کهورستان، لار
⏺
پل نیمه‌کاره؛ محور بندر خمیر، کشار، بندرعباس
⏺
پل روستای مارو شهرستان خمیر
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68335" target="_blank">📅 11:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68333">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ff7cn3GDt6p_Ed6prQ9VUk-3Jr-B1XCEkV2LlmDRaVnTbykHIt6ocAoD_gey0CLyJNjoQOE2UfNewkvidP7RfIfjVmU3jOjQGw9G9QHdqbogc_OzathdReaFsCvx_po0k_AobJAPtiRd_Tls_CbqCXVCtpoeNgOkfFWYrqPhyFh3ubYRrng5L9IP19lfR5ws04SoSziMZ5Tbp3rtaVXoK_fvprb6ZKTYkUbZWLN1Pw1WlMO8FH86SG5GvJd7z35r9NsOZldDxQk0urJlvIhFCsouzlDg222cWR3vcTS7ltwKTmtR8Zb6raTtqEWF7_bcjCpf3sCGVC50ww-mmz72Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YfnNYnQkTP1HOxj7YuwU2f2BT2ZuySIerZNw3x8iFcOMMffPfvvRPdt-Haabkt7G2VZvteqoZn6Kb2bQ5CWGByQFp4RIFzfwLNGu_fY_K_RZXArxuXRPPyAL3KEeg4UG6jAV4JzhJv9CFHWya2UdYeNTmeQycHzCgBUOeU5aLSiOv0HBU6EWQbfvfBqSY84BzeFZNcF_m3Bk9s038n1_wFWvstvZW5Do4SPgxZSsMj9Cy6n72dNe35aBo5eN5K8vNYWFYXCb03qkU0KETvo6a9hPYf2XkBr1xXc-AJTWVYUyfOPw9VZJxMOu0QKkDmAcAcWuGwXZ4NUPOPC_yX0MWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
ما برای آقای فغانی عزیز اين چهره محبوب ملت‌ ایران آرزوی سلامتی و موفقیت‌روزافزون داریم
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68333" target="_blank">📅 11:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68332">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b51a5dfa4.mp4?token=iUGNsf0p62YQ5KKax2DbYj1n0lXsDQErhYb2eBSn82iq7gKVt30HjXwmNgHvG-ak15mbTDzH5r1SdytjO8sX4nW3fPQulavI7yX9g2sLg2SVfv_mMUGDLgbfjbIt6ilfI3kJ2tLZXif-zblj-WVdRWoP9TYCyetODXRHKZyQyX4bq6bj-DAKgWyZOMn61iBnZmFT-1HgmVT5iPNpkGNJv207g2Whje1bsuZni1ZV_qkmi3kzEfzX1IS31ZCYnqgXWFARY3u1l7HvF55fUI_Hgp-GcbNKne5Zc-FQw_6b0qSkNpWtCJeIUQ-y-WjqZ8LbOsoJY-5yVdY3DQ5MUUpvDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b51a5dfa4.mp4?token=iUGNsf0p62YQ5KKax2DbYj1n0lXsDQErhYb2eBSn82iq7gKVt30HjXwmNgHvG-ak15mbTDzH5r1SdytjO8sX4nW3fPQulavI7yX9g2sLg2SVfv_mMUGDLgbfjbIt6ilfI3kJ2tLZXif-zblj-WVdRWoP9TYCyetODXRHKZyQyX4bq6bj-DAKgWyZOMn61iBnZmFT-1HgmVT5iPNpkGNJv207g2Whje1bsuZni1ZV_qkmi3kzEfzX1IS31ZCYnqgXWFARY3u1l7HvF55fUI_Hgp-GcbNKne5Zc-FQw_6b0qSkNpWtCJeIUQ-y-WjqZ8LbOsoJY-5yVdY3DQ5MUUpvDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
وضعیت پل کهورستان در محور بندرعباس شیراز بعد از حمله دیشب.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68332" target="_blank">📅 10:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68331">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxTqtPWbh0IXN1ct5IzGiI4e5m1-r0andqkvULEh-ludDoNm_NWU_Pv-x0_T7LqC4zcMJTFIi0_pNStsgSmAY2qNPngvGsdbN4GxBC9OBtVDLyjSVhw-fhFgn_eO3-trLF2qacQqIXF95CTSVX9ieqkqsF5aKUftG93_VLApxtA3pKGw9dsrEy8v29GjO1uVq3JuDZ_1okswjcZXy5ZiD5DxV9vEGsrMEMn5AABMC9WYRkDNcUi6a7MlHK1nFH6O7GFRIb_KQauiIjmmT5Q_jtwJJoHOsBSZ2zK0HiiNmxtvoJPYVNdF3nCQJcwM7Xcmo05SdV4zydhZHrcMKkSaOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وال استریت ژورنال:
به گفته یک مقام ارشد آمریکایی، ایالات متحده روز پنجشنبه چندین پل را در ایران هدف قرار داد؛ اقدامی که با هدف قطع مسیرهای تدارکاتی به یک شهر بندری و پایگاه دریایی در تنگه هرمز صورت گرفت—مراکزی که ایران از آن‌ها برای حمله به کشتی‌ها و اعمال قدرت استفاده می‌کند.
بر اساس گزارش سازمان صداوسیمای جمهوری اسلامی ایران (IRIB)، در طول شب پنجشنبه چندین حمله به پل‌ها در داخل و اطراف شهر بندری بندرعباس گزارش شد و بزرگراه‌های متصل‌کننده بندرعباس به استان‌های همجوار مسدود اعلام شدند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68331" target="_blank">📅 10:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68330">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e60e986837.mp4?token=r_ZCFExcMajI9oosiRQKWUCFlagNcGZMHTZ0jJIwcwZEIPpdDh69053fJjn37YIGi41DY5WiTRQVkjXYwVsuzqiKeFTc8ReGRLHm-YqHDC_PGcEcKVfUtxBSgsEaz93mHjp_LfViT_Czohc-horRwEuCQAZsdFx5vBz0IVtPEdk4_IYTkcaNMnWqpz9UzLoT30330IaNT4XnU59_Wvqr1xcbo3AfyNGVk1dKIVTWgIWlgUBd4Bo-l0uDAV75gmZnZ0eXH-ue2ofFDp8tIVo0Amk3E6ql8osuH1KwpjzYeLb1FuM-ytQzqyyzAfu1q9CZjc7gnwhABTrDVcz6iWmNcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e60e986837.mp4?token=r_ZCFExcMajI9oosiRQKWUCFlagNcGZMHTZ0jJIwcwZEIPpdDh69053fJjn37YIGi41DY5WiTRQVkjXYwVsuzqiKeFTc8ReGRLHm-YqHDC_PGcEcKVfUtxBSgsEaz93mHjp_LfViT_Czohc-horRwEuCQAZsdFx5vBz0IVtPEdk4_IYTkcaNMnWqpz9UzLoT30330IaNT4XnU59_Wvqr1xcbo3AfyNGVk1dKIVTWgIWlgUBd4Bo-l0uDAV75gmZnZ0eXH-ue2ofFDp8tIVo0Amk3E6ql8osuH1KwpjzYeLb1FuM-ytQzqyyzAfu1q9CZjc7gnwhABTrDVcz6iWmNcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدباقر قالیباف، تیر 1403:
ما غنی‌سازی را بیست درصد کردیم جنگ شد؟ شصت درصد کردیم جنگ شد؟
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68330" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
