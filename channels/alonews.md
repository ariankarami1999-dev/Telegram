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
<img src="https://cdn4.telesco.pe/file/LxLGU3_Qfon5Z0btmDbTYLDm1CaXXLiNwU4BCrQ3EWPJgBbf2_M0RKSINAoKabXP_m1bYkXdaK9d7f9XGLAXYSeIPYcXfTL7QyF9JZcqDw_wuU8D5sCCfd2grUBgrRsGM9KzdBIaPOZc34FpSfThquZRx9ePRaqA6oY-Omi7F0f45pPNDVpZNmwoTjWz6SJfoSflxG6inVZnuiLBoGSpr88YSh7FuEHKa64e2SJajcLgn1fGI4GpLk6TXeKOruxt-QcZAdkgxLweI5u8bnBMrYRHLzMjn9bPIR9LRLppxz_EYDC2KU3VVrqceWJGYPzjeMd3c_JufbuVnOfOnfTaQg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.02M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 21:14:38</div>
<hr>

<div class="tg-post" id="msg-149913">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: نتانیاهو در سفر به امارات نه فقط با مقامات این کشور بلکه با نمایندگانی از سایر کشورهای عربی دیدار کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/alonews/149913" target="_blank">📅 21:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149912">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
فوری / فعالیت‌های پدافند هوایی در منطقه کریات شمونا، در شمال اسرائیل و در امتداد مرز اسرائیل و لبنان، مشاهده شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/149912" target="_blank">📅 21:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149911">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
مطابق گزارش خبرنگار شبکه الحدث در پاکستان، به گفته منابع، ایران با توقف فعالیت‌های غنی‌سازی موافقت کرده است، در ازای آن، تحریم‌های ایالات متحده علیه ایران کاهش خواهد یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/149911" target="_blank">📅 20:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149910">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
یک مقام آمریکایی در گفتگو با سی‌ان‌ان:
مذاکرات مثبت و سازنده‌ای را از طریق میانجی‌ها با ایران دنبال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/149910" target="_blank">📅 20:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149909">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
عضو هیئت رئیسه مجلس: ما قدرت چهارم جهان نیستیم، قدرت اول جهانیم و تنگه هرمز هم ناموسمونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/149909" target="_blank">📅 20:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149908">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
حوثی‌ها (انصارالله) اعلام کردند که عربستان سعودی در ۲۴ ساعت گذشته، ۳۸ حمله هوایی و موشکی انجام داده است. این حملات با استفاده از هواپیماهای F-15 و تایفون از پایگاه‌های هوایی خمیس مشیت و طائف، و همچنین موشک‌هایی که از مناطق نجران و جیزان شلیک شده‌اند، صورت گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/149908" target="_blank">📅 20:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149907">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4HsMC4zqk5VAjuzuOUEiKYuwesENWZnBgVNSclD9USAxjMJ-K-IEumsqN4WH7H9x7OJBDLxZ87DIlDLAI3vpvNoAvPx_VmCvDOSIQqoodEHh3cmB-2hW4mrJkflbKOtJOzRJVgTAsycRa8ce5zQ9LKq-hilzCDUkTh8SKTAwkk_Dop9yR1eE1FuPZobeAiuAEi14tXqwFcRqUG9krvUR3iQ0PN-OLrCr9EMTAOKgg4YSIpz4Leb_XgZ3i2vaDH9wdbSjS-uNjgz97i-nOlb-kzxSE6Wti_HQlEiXv9mzbBpzNDgf0TtgrzZkXpL_LTAj6VIaHM9IP6KnB4k65IG7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۴درصد کاهش فوری قیمت نفت در کمتر از  ۳۰ دقیقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/149907" target="_blank">📅 20:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149906">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXDiI45UcXWhcqGf-gaSCmBpZqK1rPcxSIhznS9as72DsTvYMzp419DOEUvSRS_U0V5ztRoAuoV-4NJLBx-MJ9rv0dQWvMTQ7EKnrxsheRlsAu0HjzTpeVZxWVXKDsapPh21jXEV-Gj8RiW_rpNynrxWAtbBwKsOa1ar37W_unW9-cRgmR8Y3kDGO2ux2VzDYSxK-G1auQrGUnkfDCGHDfrzptcjI8aju6-Zl0rSntkLpDSaGAuj7ZfZoJbtuQ0zWg2cWrneZ7JtlmQXlfB7AeUgcYH5R4UTE5KW3eRtz09FUSCn0D5kvNIkb3RBDHy3W9ias8L7MvwHqR6gN7h2wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابراهیم رضایی عضو کمیسیون امنیت ملی مجلس: مستعمره‌های آمریکا در منطقه که این روزها برای شعله‌ورتر شدن جنگ فشار می‌آورند، مراقب باشند که در جنگ بعدی کاخ‌هایشان هم هدف مشروع است.
🔴
‌خبر داریم که برای جنگ مجدد فشار می‌آورند و هزینه‌هایش را متقبل شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/149906" target="_blank">📅 20:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149905">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
یک فروند هواپیما بوئینگ متعلق به شرکت هوایی کاسپین، به دلیل بدهی سه میلیون یورویی در فرودگاه استانبول توقیف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/149905" target="_blank">📅 20:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149904">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
فوری / مقام آمریکایی به باراک راوید: ترامپ آماده کاهش تحریم‌ها و آزادسازی منابع مسدودشده ایران است
🔴
یک مقام آمریکایی به باراک راوید گفت: «دونالد ترامپ آماده است در ازای پیشرفت ملموس در موضوع هسته‌ای، تحریم‌های ایران را کاهش دهد و منابع مالی مسدودشده این کشور را آزاد کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/149904" target="_blank">📅 20:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149903">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eb86933aa.mp4?token=O2vHHic8uf8WBtQo4b4YxF_0O1MXK1jAuMahBZ-CXT-7RkTijWKA5qSlKQG8uNNA6NCekKGxTw7wurZZYg6o57r70_RrxujPwFGbboi6PPD7vFTjHPeH2Ihc4zdzskeqgabyZ5D6TRgiMM8RDjI_bZCjij033hB5bwAOibfFYjcrrhpk0EwpoONccnl3zYuWXXzfHuQ0jTpp7aEfRM7vhwVmSrtWbpopkIfLYHf2wPEdcAJGAbANusK3Y822ZsrBHNfYMtWUXtDStHMGSur6uFhfqdJVQvj0M7RYF9mYrW3g1nBWgjclEgl3QHft8QyudfKEVUCeh86fGDQlXKUGxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eb86933aa.mp4?token=O2vHHic8uf8WBtQo4b4YxF_0O1MXK1jAuMahBZ-CXT-7RkTijWKA5qSlKQG8uNNA6NCekKGxTw7wurZZYg6o57r70_RrxujPwFGbboi6PPD7vFTjHPeH2Ihc4zdzskeqgabyZ5D6TRgiMM8RDjI_bZCjij033hB5bwAOibfFYjcrrhpk0EwpoONccnl3zYuWXXzfHuQ0jTpp7aEfRM7vhwVmSrtWbpopkIfLYHf2wPEdcAJGAbANusK3Y822ZsrBHNfYMtWUXtDStHMGSur6uFhfqdJVQvj0M7RYF9mYrW3g1nBWgjclEgl3QHft8QyudfKEVUCeh86fGDQlXKUGxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">*خدمات اداری خانم احمدی*
✅
صدور انواع مدارک قانونی
✅
کارت پایان خدمت
✅
مدارک تحصیلی دیپلم تا دکترا
جهت هماهنگی واتساپ پیام بدین
👇🏻
👇🏻
https://wa.me/+989931139419
شماره تماس:
09931134919
ایدی تلگرام
@ahmadi_p0099
https://t.me/+otKVayh3TIgzZGFk</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/149903" target="_blank">📅 20:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149901">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
مقام آمریکایی به آکسیوس:
بدون پرداختن به مسئله هسته‌ای ایران هیچگونه توافقی در کار نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/149901" target="_blank">📅 19:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149900">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
العربیه به نقل از منابع آگاه: امروز مذاکرات غیرمستقیم میان آمریکا و ایران با میانجی‌گری قطر و پاکستان برگزار می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/149900" target="_blank">📅 19:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149899">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری / برخی منابع عربی مدعی شلیک موشک‌ از خاک ایران شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/149899" target="_blank">📅 19:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149898">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFGDyKFKHZPaV9Yg5sBonOI-MDiszWYLM4-Ohz505SqBcAa9Wj0dUTq8ddCkjFduXAG0SI3MFMmmtr-5gmtU2L2NpeNqft88pnvhIIbIkBn7nz3FMalQmT5wk49ISMxE6DLFnQyDMNVtMU25qfSq8VIN3q9CQniyMe8RmvBCYmDArD0t5XVuxojH3yv1VxHyiiDOpUnzwBI8UQyTfQrAbJF5MlLDFFENB05pAfihSRgvOgkXOOtRG_G_YhAz8VNyoHEMOYyhYo48MdbYuqZgdeMAdDoxad0sKuZ1bsssAwYSwXXlANAzMQBw6YYSj1ftA3kPoZSt17cUdKKW3TZswA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت جدید خاویر بلاس، ستون نویس مشهور بلومبرگ: صادرات نفت خام از عربستان سعودی، عراق، کویت، امارات متحده عربی، بحرین و قطر (از طریق تمام مسیرها) با هزینه‌های هنگفت و با کمک نیروی دریایی ایالات متحده، به حدود ۸۰ درصد سطح پیش از جنگ رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/149898" target="_blank">📅 19:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149897">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">میانجی‌ها امروز یا فردا مذاکرات جداگانه‌ای با آمریکا و ایران تو نیویورک برگزار می‌کنن ولی بعید میدونم اتفاق خاصی بیافته  @shahab_gold_trading</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/149897" target="_blank">📅 19:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149896">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
رویترز: در چارچوب دیدار شی و ترامپ، چین و آمریکا بر سر کاهش تعرفه ۶۰ میلیارد دلاری کالا توافق کردند
🔴
چین و آمریکا توافق کرده‌اند تعرفه‌های اعمال‌شده بر کالاهای وارداتی به ارزش ۶۰ میلیارد دلار از یکدیگر را کاهش دهند؛ اقدامی که طیف گسترده‌ای از محصولات کشاورزی آمریکا و کالاهای مصرفی و خانگی چین را دربرمی‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149896" target="_blank">📅 19:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149895">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
رسانه‌های سعودی: امروز مذاکرات غیرمستقیم آمریکا و ایران با میانجی‌گری قطر و پاکستان برگزار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/149895" target="_blank">📅 19:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149894">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IThnmCfew2bpEshRSMLhnjzHxQYAoBBFCAhjK5tqeqPptHcmXa7Myz4Erg1eDxM_gcphTJJSF9FxJs8L_iSXzc5wlLY1JTRXAuWhKw5wRoRf2nU_vNrVsoNPCywnUHTD5RvrzindlqKbHNtadcgBGAunow3IqDAaj25ynPS4fWGfysDIqpo6DG6ZNrv83XTlT8Ck7KwyccsruTekXCTSdrYFz-gfwDQcVjqE5EAXwtJVkaizjmPI_aDlwpdSS4v3ay4juyBXUzb1JJAbt2gZd4Vm46yp4qNsdvrfAfXiLM4wkN0LlIEF6atIsLetrwFlcmGJHr5i4LAJVyavb8VNJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز امنیت دولت لهستان در منطقه لوبلین، در شرق این کشور، هشدار حمله هوایی صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/149894" target="_blank">📅 19:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149893">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
هم اکنون دیدار عراقچی با میانجی‌های‌‌ قطری
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/149893" target="_blank">📅 19:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149892">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ایران رسماً از محدودیت پروازها به ایکائو شکایت کرد
🔴
رئیس سازمان هواپیمایی کشوری: ایران با هماهنگی وزارت امور خارجه، اعتراض رسمی خود به محدودیت‌های اعمال‌شده علیه صنعت هوانوردی کشور را به سازمان بین‌المللی هوانوردی کشوری (ایکائو) ارسال کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/149892" target="_blank">📅 19:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149891">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fl675tpzapdALl09SpKMjn7jKhJGXix9NNONeA4gq-HmXeUjMUqlT1SU25LWMu9myCFiBwRlVVtCgK8Adikm9MLKNRSOrhMGRWWySOpscFs1Cc27TpyJcoV6gmepk4ecvZzi48Dqx4swsxjBrB0JA_HONrG_4zs1WWDEeNm9MXCIljTwdkg8ECGBPou7oPxJw5GS0WScyh2jpOoXmVQbUu5ucF7vRjr24EbJ5QFJlHMZ2B2vFePYRtLkWiOne4rr4nIFLzZfppIelb1upUbk3crOUPgKnWoLknUf9b_NIMtdrR7eJVuRPgwunqEnnCn39p-5ZorOAm0_n6gtC1CXSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر هوایی از غزه قبل و بعد از ۷ اکتبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/149891" target="_blank">📅 18:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149888">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z2Z2LFRn7wCkrNaMsdIjL19o1UbGHAQBDAYzJh16d0-eg687iuiShzXAJSuITw7OplLGwlhID66_Uf2Lv3ZhIDI9idaq2fhU3J0n1OFu0UqNtW-QmRpzeZUqvBiOl2NrXzNdwceSBLuZtqerDWAv4LgWI-OjCHy9r6q-AGJCYO27nj1pbzItROlUFBJmW3tpxwdMjE5qsW5DEignByN82mH2vPORoCPJE9UAKc5dz1ez5EV55xeG1ZBTFi5YGiT5j8S3e9_fpGnhLV8cuVRf75KgLjGgo5ByykHKavjv6k_lrTSSn9Xbjv45QgcmGOIQIMI6XSLO9onZokVFnHOwoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P1Z7FlFoHINfUvVf_ZcTk_fwhlt9uR5MuvxFcLqz8gmlDCfN7weY5FZvMSyayNz7xBV-3Wstg_1SfdjstUuLmg5aAzIeiqLDOJwNkPusuo5OUC4I3p5a1md5ZnYaSBl3TVUc5VEP6UqIUWpqv1xd2x_QpxqK-o6nLJIxcz9kXC4dhhR7BSug8EzIDBzOUNvh9tyR5xEbsdRklz3XX1ZKj-GOGg89VsjnbbCFZIwFgFOnSqL_SHo-FD7pUErjZVVNWpVIJh1yryuUc5DE0alUCHYOLWFjpd4QTa1b4FEOyku5IJc3Qdz6bCl1wZBZDUGh69e8T-TpMz7Aeu5l8NVNqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8eZX-LVUQaXli7gPQFGFWNsrz2DR9f9-130ChdOoMaPoFnVQgozfD7nD1ZIzoeE92we-mWFztvFR0Zpoh4vISTEv8KuUuIEq_mIqBsbmbTuaPpdzEQA73dGIjTwtB2LzJNpdBFTUH1UWbG1hA5251Lu0vo-3xADaAmMB5hqtUGD_0o3mE1jrFTDYE7ASQ9OkGFZFp_SE9EGSxvb7AJOKjoJNy-Srj6U6M-G-v2xaGpsJM4ytGbRYTlJ4fOn91EqFtwcDPMyv2bvqsyucQZ21V8QO-OEZZsTdQfIE4OnI7NktEiBgpSfHf_dB7Gf_UBQUplz8JQ38VK1VTyd9FHlOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات هوایی اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149888" target="_blank">📅 18:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149887">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvnmW2-MSkA8MNHnYfIwuD6nPqxjV1QtXEgYB4Gk9J8S2qf9O45pM2_LMYpRk35YXWs2mEgxkjmlvF0kW_TuFtIIZVCrkkOsrtM2A5NmOvJC1G6BTo3Oype4nmeyLtcfOkMR8r8mTc2saZg8sRnWT7En4joLANybiM16sEjQ4uNN7RD-7DUPxcwWQ_67AByG2Q__nWpCuzPVfzMNTCzP8nA94q7Wt7Q2fkHkhfMB5-C_5p-onRbV-q-MOMg0I5oqm1NdxftusHI-9Q8wE4hqebri--PEZQPLe-W9igt33tod4tyoVnTuea3TxZc41-yNculb3mbyK3cwKaZnYLAtPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نواف سلام، نخست‌وزیر لبنان، در واشنگتن با مارکو روبیو، وزیر خارجه آمریکا دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149887" target="_blank">📅 18:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149883">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hoM3Hi3ARFS1PSPmD-ihtUzmbk0_-fLED2y-gwedoBKavCdZ-Mi9mrBpPOYTOVt1lZvZ0hh3zR45kuK3Jv4QoIN1G7z5JpVSz-pEDL4kZ30y4Cf0W56OQ1x6kahVukbQZgLE5er0Ja6LsXEjEayniF1_7q9RjrIBFQkSfb0OrS_uLFEOFqHeeqUK0RD5u4YaFcmnuNTTEFTVoTZRRdZElXylZTqAiVzbhnGp6uXUQZny2JVUs6QfI69Clg-MJQm6h1djxyEGAKPwvnh7H7K-5uUKoP0jo_Jt0OACyOkNzhfqrQCrqXex-pyc-fEhkybU1kGbWDggP_E0NHJIPbyY3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W_HqvR-mLbimLEMHefdIRWMdjZ0H22sD1UtgwsyPUtZSqpFOVcnvO2k8q0qpVaY4qsplRfhBnKnx5TaE0yai6OykOuFglWDwR-AMJacIto4jrdMekSOYxXQ84xKpWuKe9e6zI2LMkYFhGQxnnt8AEiAXTOylwgYYYAugU2SKTCA-5pZd6dqe3yMajT88vqMBSm3Wyw8Kjz2M5BUK2YhN_Lag2EdkZyb-1nZ9o33828XsXL9XSHWTSF0w1FQeErRMOI32Flz8OmUwpPEMxAPrUCNzf6vLyOWVBfWBfO4s7mu8w-f2exQ3tguSi-40MEDlUag0vOqGVr7gJuZNq8Y6nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rdx521EaT8wbMnVqWGVLzlkdcVPcxxskiOuivGums605BZcPhJDFZSDHCU3zioxR-5Vw435mqedUJwky1BH3otWATaN6B_mHqMTQzQJWLmDzPrgE8_8cdSDyWR0nNoA23zmimXee0-t4SJqLk1FfYVKRsnnrIjlMw740-h4tKQcJdZt3UlBq5inteyJEJK3ODJdkFglyYGHtaeUGrKZl8nhmdYU2LBve6aGL9H-JkKGyCWfaBdcWEMQkwroi9vUOmAzty32lmQcJJKoSSQ8c2PTkW0wjfMC79vCTIZZEmI0rdv3WywSL-ztM28Or9Pj-QSRfYQy-YRU4XibpHD0yQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T9eRFX6iquoq3feCaAeXA777mvwvTecSFvWwWEd0SahwAnGtLktxQVOEJBiMmZJui3Bf7CwcFueVHIttcsCCiugDSoOb9RLznAM61y-aT0iRiXuEpY0zqYcMiZX_34ddXYwRhnSRQZUexmN_wp9Q1FzDALIO7nNO2pRXjHuJC798HnL6QXWzo5783NonyesYaGByThTpltLOH8qSEMmkSgvdT2MNSvRaQagigDitJbQvanCYjPdUGr3lt5jVxeAJvCwGgcCuWfVIIa5_RSC39xU9LQn3XzRzLOt7jrpsOOduc3NMvE_jwZDz7ua63wol-wUNXzNmP26MAu7nvLOQZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بلومبرگ: خط لوله شرق به غرب عربستان سعودی در حال حاضر روزانه حدود ۳.۵ میلیون بشکه نفت انتقال می‌دهد که حدود ۲ میلیون بشکه آن در داخل کشور مصرف می‌شود و حدود ۱.۵ میلیون بشکه برای صادرات باقی می‌ماند
🔴
این وضعیت باعث کاهش بارگیری نفتکش‌های سعودی شده و امروز تنها ۳ نفتکش بارگیری شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149883" target="_blank">📅 18:16 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149882">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">به نظر میرسه قطر داره به ایران فشار میاره تا امتیازات هسته‌ای رو هم داخل پیشنهاد به آمریکا جا بده تا بلکه ترامپ راضی بشه و توافق صورت بگیره  بازارها خیلی متشنج شده  بیینیم میتونن کنترلش کنن   @shahab_gold_trading</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/149882" target="_blank">📅 18:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149881">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce0f9e6ce.mp4?token=Yp6xnI1EuGj7N_EVxJldn8PWGHGdB_rQ3pJKR3kJXRnRV5iR4Jl-w7JMWxuYyZKd7xd3qewIkJQSnaBl3dMVj758NCCbY-wGaipOA3ZlCyVcgCjk17SUBpfyhKhspqiUbo-9yxtVzUTr9T9Bjq1Ydu_rsVCvQum8mEYULfyVBCqWSAiTMiabkp9C-YDowjXXIz8QjrYklFmiUDjG4r5-763Ku6wERP4qDNhVwCmiTlpXC0dCkE7BU4kLoA9Bi-ZZPdinzzMM414ltOzEvixku_L3CjUNt9KKZyTmnzZ0_NVYP3dA2XYHltJwdD5EARUbJPu2gBV4BU09Gi6HuTvsL6yWd2S1Dl3xxQ5CsKbdtcTykgpm1H-8SEjHvN4CW6bBW9LiO-0W8yxrcEC_KIy3KXvPQMUdl9xmbCyau6EPHkcsuYKnqk2dQgk5tKD9bZUqnKdjL_vQf053o8ubDFNwrin5TOZvRuy3rz9g2UJ1e_b9qy5MLLsH-FnHqkoL6lwuP7hxycqyY1-NeXUTdvGAXtvwHh4jKh9hV_0q5-s9UF-Jms0LoOzc4qwLGrnQCm3LJefH3QyyKHlV4W3loJS83sY1y2BtYjscsFNnKF3SCfJN3vuScKl4ASZz6WJRypCMHR5RhQcPZg3351xdXHdTKniE4bZ2qIzPFXtUfs-83Uo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce0f9e6ce.mp4?token=Yp6xnI1EuGj7N_EVxJldn8PWGHGdB_rQ3pJKR3kJXRnRV5iR4Jl-w7JMWxuYyZKd7xd3qewIkJQSnaBl3dMVj758NCCbY-wGaipOA3ZlCyVcgCjk17SUBpfyhKhspqiUbo-9yxtVzUTr9T9Bjq1Ydu_rsVCvQum8mEYULfyVBCqWSAiTMiabkp9C-YDowjXXIz8QjrYklFmiUDjG4r5-763Ku6wERP4qDNhVwCmiTlpXC0dCkE7BU4kLoA9Bi-ZZPdinzzMM414ltOzEvixku_L3CjUNt9KKZyTmnzZ0_NVYP3dA2XYHltJwdD5EARUbJPu2gBV4BU09Gi6HuTvsL6yWd2S1Dl3xxQ5CsKbdtcTykgpm1H-8SEjHvN4CW6bBW9LiO-0W8yxrcEC_KIy3KXvPQMUdl9xmbCyau6EPHkcsuYKnqk2dQgk5tKD9bZUqnKdjL_vQf053o8ubDFNwrin5TOZvRuy3rz9g2UJ1e_b9qy5MLLsH-FnHqkoL6lwuP7hxycqyY1-NeXUTdvGAXtvwHh4jKh9hV_0q5-s9UF-Jms0LoOzc4qwLGrnQCm3LJefH3QyyKHlV4W3loJS83sY1y2BtYjscsFNnKF3SCfJN3vuScKl4ASZz6WJRypCMHR5RhQcPZg3351xdXHdTKniE4bZ2qIzPFXtUfs-83Uo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چندین فروند F-22 raptor در راه پایگاه های بریتانیا هستند که احتمالا برای انجام فعالیت در خاورمیانه مستقر میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149881" target="_blank">📅 18:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149880">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
دیوید پردو، سفیر آمریکا در چین: ترامپ در جریان دیدار با شی جین‌پینگ از او درباره خرید تسلیحات آمریکایی پرسیده است.
🔴
با این حال، واشنگتن هرگونه پیشنهاد یا برنامه رسمی برای فروش تسلیحات به چین را رد کرده است.
🔴
همزمان، یک بسته تسلیحاتی ۱۴ میلیارد دلاری برای تایوان همچنان در حالت تعلیق قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149880" target="_blank">📅 18:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149879">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03bde46572.mp4?token=dZBCHLGOFhM7X-tUkkEX8ifyir303GfrHChgwQ_7CmELG0zNafx_HvGbtoek3FG8NlLhJkYq834pf4E3yw7LKxJDUmOsrzlazFH-SmmD4Rnsx2ujPB5uagt0sXE0VI2t61tFcLLBqYfjSOZWUu772nB6ZyQadoH5CmG4-U-ghijv9Hl2TAt6bUgOwJqF37BNYHqVWDzvzMcJMx2lTs36W3UcqelCLW4O7DskcUivf1KyVk5P-tJW2OzaFtLwJcL6Iw1zlhYtEfyQIAnDkOqBYE4Oa8ZveCdSN4LGsn_BT3YC8e2DzofHJ42B1qsk0KtKDjs3Cee9qk-PvnZnlnBsCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03bde46572.mp4?token=dZBCHLGOFhM7X-tUkkEX8ifyir303GfrHChgwQ_7CmELG0zNafx_HvGbtoek3FG8NlLhJkYq834pf4E3yw7LKxJDUmOsrzlazFH-SmmD4Rnsx2ujPB5uagt0sXE0VI2t61tFcLLBqYfjSOZWUu772nB6ZyQadoH5CmG4-U-ghijv9Hl2TAt6bUgOwJqF37BNYHqVWDzvzMcJMx2lTs36W3UcqelCLW4O7DskcUivf1KyVk5P-tJW2OzaFtLwJcL6Iw1zlhYtEfyQIAnDkOqBYE4Oa8ZveCdSN4LGsn_BT3YC8e2DzofHJ42B1qsk0KtKDjs3Cee9qk-PvnZnlnBsCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کالاس، رئیس سیاست خارجی اتحادیه اروپا: اقدامات خرابکارانه، آتش‌سوزی‌ها و نقض حریم هوایی که روسیه مرتکب می‌شود، همچنان ادامه دارد.
🔴
از سوی اتحادیه اروپا، تحریم‌ها علیه مجرمان و اخراج دیپلمات‌های روسی، اثرگذار است. اما ما باید بررسی کنیم که چه کارهای دیگری می‌توانیم انجام دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149879" target="_blank">📅 17:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149878">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
رویترز به نقل از منبع آگاه: میانجی‌ها امروز یا فردا در نیویورک، مذاکرات جداگانه‌ای با آمریکا و ایران برگزار خواهند کرد.
🔴
عباس عراقچی و میانجی‌ها در نیویورک می‌مانند تا مذاکرات را احیا کنند
🔴
مذاکرات در نیویورک بر نسخه‌ای اصلاح‌شده از آخرین پیشنهاد ایران متمرکز خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149878" target="_blank">📅 17:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149877">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s96_4QNrVRTeVbctaiIxPEaUwHWEIIgoI4OmWaUtZbFPFYL-zRBvBPpMVC8A68nkyzWDweHRgYOUDDuQqVKgt80PTTCqZgsvfp8qTGzrZF8SGVKKB3wijAyb9BpgV-T79Kvmq1FctH0y8_1qF25Wh0k8U_q48XgvpZEtOMpC08ZKvPYOQBb3ZsVjmvjCevdCgwNOk0pebaVdvQN-Xo39kjMc7A8IsjDcLdrg9xnWl3sKkj1z-u3eW3Npx0XCoCE1fuC2U1F100pne7MrePVxNXdupYxRAjDKdNG10mKfwr3in3DgK-2hgSRDN2dSy2BQSBKcuJZQR6oYp8k7dPsvjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی: امارات نباید زمانی که اوضاع از هم می‌پاشد، شکایتی داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149877" target="_blank">📅 17:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149876">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
رویترز:  میانجی‌ها امروز یا فردا در نیویورک، مذاکرات جداگانه‌ای با آمریکا و ایران برگزار خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149876" target="_blank">📅 17:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149875">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijNrpecv65Be_cGPBMUauVw-tojjy3tznz9IlmUZ3YK2oCrrO-OvNHun6Uz_By-GDrhFBRRYR1zkArbSlqHJDS70rTF3wS8c8Wm3FoYQHWb9mrqe5vxvO_tJLx5fXkyvTJZe8pVO0lCZg0H5w3FakRI2n3oMl7w18xtEUFClhwj0ULkioy5UJqoUCv9Pfcz31Q1CVWSB18OFnCxbHiCi3ikyrFqiLKTXMgUJXIqG82IsXh3t6EEuxDTKzC3DIXYUSIYOpMSYVhzMplIYzzfoiGgHqMYR98cr9-IpD7iGJTliy0elQ4wE4LY7ZLwQqskKzOHN-L3RtXAqj7KSwZW1iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ریال ایران به پایین‌ترین سطح تاریخی خود رسید
🔴
ریال ایران به رکورد جدیدی در برابر دلار رسید؛ قیمت دلار در بازار آزاد از ۲۴۰ هزار تومان عبور کرده و حدود ۲۴۳ تا ۲۴۴ هزار تومان معامله می‌شود.
🔴
ارزش ریال طی یک سال بیش از نصف شده و قیمت دلار از حدود ۱۱۱ هزار تومان در یک سال قبل به سطح فعلی رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149875" target="_blank">📅 17:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149874">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9798ee16b7.mp4?token=Z_SIeJf9r2W3ypvCFdazeSZw9805Y2icd3GjZJ2cVRJCvY9JSd0iFUHstcaoj07j_iuNeH8K0VPfaSL_gfb6rQ21Nn8SeLngySLl44faWfzFbTX6AiNUsTfgLEsLCY7u5u8RRGLx1nMz1gBkYYpr83kWCMLza3gw48xi2rIqXdnVtzGc2rkji7zjOEGE8rwL2GkatoZikXof9PC6wHQVgiVmfRPBJMo9BufjPOlHLFCUKJCrwDjBWqdSjibLOtNiLVDKAkckE9Wj_5W26FFP8CaK28m-RfSufkFlTYLRQTYPOm0nbyHPbvZymCjiu_YM9h6DX6iSS57Z3xWOr2ylmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9798ee16b7.mp4?token=Z_SIeJf9r2W3ypvCFdazeSZw9805Y2icd3GjZJ2cVRJCvY9JSd0iFUHstcaoj07j_iuNeH8K0VPfaSL_gfb6rQ21Nn8SeLngySLl44faWfzFbTX6AiNUsTfgLEsLCY7u5u8RRGLx1nMz1gBkYYpr83kWCMLza3gw48xi2rIqXdnVtzGc2rkji7zjOEGE8rwL2GkatoZikXof9PC6wHQVgiVmfRPBJMo9BufjPOlHLFCUKJCrwDjBWqdSjibLOtNiLVDKAkckE9Wj_5W26FFP8CaK28m-RfSufkFlTYLRQTYPOm0nbyHPbvZymCjiu_YM9h6DX6iSS57Z3xWOr2ylmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپاد اوکراینی در تعقیب یک سوخو-۳۰ در کریمه چند ثانیه دیر رسید
🔴
یک پهپاد اوکراینی تلاش کرد یک جنگنده سوخو-۳۰اس‌ام را هنگام برخاستن از فرودگاهی در کریمه هدف قرار دهد، اما تنها چند ثانیه دیر رسید.
🔴
خلبانان جنگنده خوش‌شانس بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149874" target="_blank">📅 17:19 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149873">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfLQY7JEX5GVHgnLmfsn8blldiEoEjsz7PuXdeVHrWQhZ9wbD9g20RtaLEkce8ZCTiTcorq6z4eSCTO02qC_6Tas8UT213SeYoulTqg0tfCNWRq9TNsjRpzP93PmR1URL3SqcNBgI51RmUhR7Yz7m5b6RlZtFsd4jCO74KDVJ4POieMEZ0MPYSrG84iNzwnC_znMvfXWUNBNWMFfZ2LaOmXUpHGDAMhYO9VHG4ZkCjbE4K2wTHj8qtHJtI3lU4M7b4sDNBnEcMhEqoVP_gfb0iM7kOiqm2BR9GMExwRiA1r2uHpft6WX9bnwi_f9jVeKvFc9ZEjngm5YWzb6MpoMDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اروپا درباره واکنش در سطح ناتو به جنگ ترکیبی روسیه بحث می‌کند
🔴
اتحادیه اروپا در حال بررسی یک پیشنهاد امنیتی اضطراری است که واکنش کشورهای عضو به خرابکاری‌ها، حملات سایبری و ورود پهپادها به حریم هوایی را هماهنگ کند.
🔴
این بحث در حالی انجام می‌شود که کشورهای اروپایی در حال بررسی این موضوع هستند که آیا اقدامات فعلی برای بازدارندگی روسیه کافی است یا نه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/149873" target="_blank">📅 17:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149872">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
مجید شاکری، مشاور قالیباف: هر کس بگوید ایران تفاهم‌نامه اسلام آباد را به هم زد بی شرف است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/149872" target="_blank">📅 17:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149871">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
دلار 244هزار تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149871" target="_blank">📅 17:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149870">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ثابتی: حق حمید نیست زندان بره
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/149870" target="_blank">📅 16:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149869">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGqN-TzbyYzszOakZ07wZVUd14d96-5i3B1VtTntLDTWrGTe3zIbnW_-ByRDKdn5fhFHo46mm9fyWoI3wKJVOqyhbAZJF_Js2SeOXPg2DTIP3zTOpr4tlZuMM-k1v-zwMG1hyoAh4AWqBuzznun9aRDWdO1pGeJOGZKzDYmAFfth9-cPUkWtGreWiaNq0o0v5tnMJzT9eaShWIyp0xxfVy_imTuhRoAgky_8DPm1YHeHtijSqsWt1PPdihEnnqE4TydY5jZEWsUodyyZfIcvoMz2XTKMsgfdz7AH_5PyI7m0Du-SLRQ_Tyc66pqkWmRB-OhGFcW5sCS02E9y2cbrcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: حق حمید نیست زندان بره
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/149869" target="_blank">📅 16:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149868">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuG1ewAREr8DFzMsNy54iuTUdLEir02Mm1KW2JoTnlVFG0eV9ZkcvaS8_X0Nz4EGimSutjZpACDuq5v3CUIYN-9JXwyGulVaLbuODGOeZhqu-saRIkCw7F6nh70VbOROLzk9dVhIRtTmIfhh8rlhBlpp51I9TZ_BvdBCxJRj1waFYqWFtYe2lUjja8W9NBXBtCcz87c9crnoez3061ngOiOydApwc5vvylj_SBm_perAmm7qeRo0EVWQeWhc4vb0JmHoL3iL577z9XNhPycF_W5D20gTv0BZIVLhNDDyT9_VT1lesvy6WKFcFTkciOaE8VJCAmZUlWA1-UQ0uw792g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بهمن بابازاده، خبرنگار حوزه موسیقی: حالا که بیژن حضورش تو ایران رو تکذیب کرد، منم مستندات رفت و آمد ۲ ماه اخیرش رو ساعت ۹ امشب منتشر میکنم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/149868" target="_blank">📅 16:19 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149867">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‏
👈
یاسر حجاج، سفیر عراق در ایران: فرودگاه نجف از ۲۴ ساعت آینده‌ برای پروازهای ایرانی باز خواهد شد.
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149867" target="_blank">📅 16:16 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149866">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwPMui_7WKOG6hSpjZ8vfqFFERuNdCEMLWxigOIDOu--8Dlx-reW7tuKTTmquXOnM0AAhKA1hfvFiLfP9Iu8egGIE8EX5me6Tpeo5SZUJUiMTpO8L0eEARHBJyYj-kRsip4SBakulTh9A9WZBIZTpRlyXCsjSlLSLGICPywGtyT1aHY_k4RDuUsObMkf-DZMSo7ZbcMcaArYHhexio0RBuSXGimkv7MZFL2Np0AZ1dkizeKB_xb7m1P32zCY22t4NGLgc4PQoDB3YUKtuum4OajKrbr8UfQsjy_IoEHvpU_lWWPPLg4ORFWaXqvT7soil7dYsCIADA5gF29qxJk6Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار دوربینی(حسن زاده):
اولین نفری که موقع بمباران بیت رهبری در موقعیت حاضر شد من بودم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/149866" target="_blank">📅 16:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149865">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اگه نمیدونید طلا و دلار بخرید یا بفروشید حتما اینجارو داشته باشید تا ضرر نکنید
👇
https://t.me/shahab_gold_trading
https://t.me/shahab_gold_trading</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149865" target="_blank">📅 16:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149864">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
دقایقی پیش 6 فروند جنگنده f35 آمریکایی به همراه 4 هواپیمای سوخت رسان از خاک آمریکا به سمت خاورمیانه به پرواز درآمدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/149864" target="_blank">📅 16:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149863">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
شعارهایی که دانشجوها دادن:
گرانی، تورم، بلای جان مردم
بیگاری، بیکاری، حجاب زن اجباری
دانشگاه پولکی، نمی‌خوایم نمی‌خوایم
با رتبه‌های عالی، تو خوابگاه پوشالی
🔴
در نهایت بسیج سعی کرد تو اعتراض بچه‌ها دخالت کنه و ادعا کردن میخوان گفتگو کنن، اما یه شخصی که در صف بسیجی‌ها بود، دانشجو هارو تهدید کرد که تو گونی میکنتشون. اونام در جواب گفتن:
🔴
گفتگوی تو گونی، نمی‌خوایم نمی‌خوایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149863" target="_blank">📅 16:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149860">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3de8da7ba2.mp4?token=dPiLMNeTmWgp4xX69vRg5Crc4KIBHKgIJwgZReHPg9eElxKfgUPhQzlXIotbKAJeCpKZsKOm82O8XiEkYMG23aYRVWTA9jtR8ETxIH4vR-31Sf13PPuxkG85Qh6r57R5dyWM3-r1mE3GkSiuRw_Fel_3G2VII2-S5N6wg81ewNCpWzL3x-cq3AQ9DcgMYMpZ0dR7NE52QfS-1Z64z2TIY6bwrv1GrfG3yewI9nShCh8Mcq4cB6TiqHGS1S_PDUqgMRTlcFiDxZRrHBZRS0ojIWE5QweUYxHa2Ce8c9Utr7v30GdOCZS_LsfTZGzANm8JESZF2h5sw61LrTXU8cPg-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3de8da7ba2.mp4?token=dPiLMNeTmWgp4xX69vRg5Crc4KIBHKgIJwgZReHPg9eElxKfgUPhQzlXIotbKAJeCpKZsKOm82O8XiEkYMG23aYRVWTA9jtR8ETxIH4vR-31Sf13PPuxkG85Qh6r57R5dyWM3-r1mE3GkSiuRw_Fel_3G2VII2-S5N6wg81ewNCpWzL3x-cq3AQ9DcgMYMpZ0dR7NE52QfS-1Z64z2TIY6bwrv1GrfG3yewI9nShCh8Mcq4cB6TiqHGS1S_PDUqgMRTlcFiDxZRrHBZRS0ojIWE5QweUYxHa2Ce8c9Utr7v30GdOCZS_LsfTZGzANm8JESZF2h5sw61LrTXU8cPg-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراض دانشجویان امروز در دانشگاه علامه طباطبایی در واکنش به گرانی، حجاب  و سایر مطالبات برگزار شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/149860" target="_blank">📅 15:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149859">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UEKDl-GWPihIOLHVA8c4K9CmwkxqLTEfOfQFF9KNhFfj7DR_60LhCs54g5VgnDUx6Erw1s224C6dQ-q_aLlFR8UBpnijuOJnfnu2yRyd7boCDvuoSmyIpDVNMfQifpcUccP3H1Q91fgvZ87ZTtGAIaz8xRyz3LZW2WWoBLnikpBsJK60B_K4zXoj_WH7HquhKmEzwcVTWHWm682x8FjIvZINlUAHV-dsyb65BFip1-xTcPpnUUXidsXiDM05huWsQgvGGwNrFF99XpD_KbP646-iegOw8u1Z7xRBOhfEO3kiA9q6A3WZ1yPHc-b9oD1fS1b4gqp84WF9ju9bk3NPsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام در پاسخ به دریادار سیاری:
ایران نیروی دریایی ندارد، زیرا نیروهای آمریکایی آن را غرق کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/149859" target="_blank">📅 15:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149858">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
رویترز:
میانجی‌ها امروز یا فردا در نیویورک، مذاکرات جداگانه‌ای با آمریکا و ایران برگزار خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149858" target="_blank">📅 15:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149857">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRboOJQi5U1ySlOAWxxrOc4S9h7SsSMuQSMr2ILbZPk_exsOYZBM5C2yaiVyFwWchU420HsShZmP7SrVZNQ4wM41WC-I8HYwMXuJ-eUp-Jtml_B5pZ06KROHEtMHt4dY-r6VJ8sOMpwaUTJ5fnvlbIn2hkYqwqxLTKex5fm5s1mHEiei2YsOXDbAhAQgdks-wURMDPSZjvnD-oQUTlShmdlT7zH1h7p4DsY3CPgOVt7gHM0hqVyz1UBimxCYc1NFxZigj7ViYrStu7S5YBxB-CEK92u2CNjsC3IYmVAc1Jc6BPmUjuJEPtooHPpDxb2dYCupXslsjLFrcrfpKc8vAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناو هواپیمابر تئودور روزولت در خاورمیانه مستقر شد
🔴
ناو هواپیمابر «تئودور روزولت» نیروی دریایی آمریکا روز یکشنبه از سن‌دیگو عازم غرب آسیا شد؛ مأموریتی که ممکن است به دلیل کمبود ناوهای جنگی، طولانی‌تر از مدت معمول باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/149857" target="_blank">📅 15:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149856">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dfa657f59.mp4?token=ryddDQJ2ySyIzxG79_Km1PkfEq2P7IUQvKPl4qhtugjo50XxFddxrxUvtJ8jGS1bi4DV9vJ3kOXk42U-scLByz0fTpqbomn0jLqaAhD0CRRJchdrfmtQai9U3yNXnNFLdPoB_1t7krDZMcChCMtCb3IRfk6fW0_DuszdjnuOde_dPlWsTPTOOiP2wP_EZSNFSPvlB3as0LLv7Pbh_Zj46zEvyDdOhrE5N_yFpEdLCgp8OZsb6rcQOgHk1nwypUXujYxIrDGuSYI8Og2sVM4exqtzgHoj3wH8MglJAtGG2Rk4p0TxNrnadJxivVtg-ufjocUSmhZfIPW4kAG-7X7ccA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dfa657f59.mp4?token=ryddDQJ2ySyIzxG79_Km1PkfEq2P7IUQvKPl4qhtugjo50XxFddxrxUvtJ8jGS1bi4DV9vJ3kOXk42U-scLByz0fTpqbomn0jLqaAhD0CRRJchdrfmtQai9U3yNXnNFLdPoB_1t7krDZMcChCMtCb3IRfk6fW0_DuszdjnuOde_dPlWsTPTOOiP2wP_EZSNFSPvlB3as0LLv7Pbh_Zj46zEvyDdOhrE5N_yFpEdLCgp8OZsb6rcQOgHk1nwypUXujYxIrDGuSYI8Og2sVM4exqtzgHoj3wH8MglJAtGG2Rk4p0TxNrnadJxivVtg-ufjocUSmhZfIPW4kAG-7X7ccA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو وایرال شده از حسین طاهری یمنی‌ها که اخیرا خیلی معروف شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/149856" target="_blank">📅 15:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149855">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">میلی گلد ورشکسته شد
‼️
بار ها توی پیام ها اشاره کردم که به ابشده فروش های انلاین اعتماد نکنید  حتما اگر ابشده میخوایید بخرید فیزیکی باشه و همونجا تحویل بگیرید  یا طلای مستعمل با درصد پایین بخرید برای سرمایه گذاری  به هیچ کدوم از پلتفرم های فروش طلای انلاین…</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/149855" target="_blank">📅 15:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149854">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
مجری تلوزیون: مردم‌ میگن مقاومت از ما میدان با شما، مردم میگن میدونیم شرایط فعلی بخاطر نامردی آمریکاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/149854" target="_blank">📅 15:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149853">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lu4LgrIru4jGCmKpBEARSSw_Ur1lOm8WiejAgjDZeaK2PlZyRT5KDkt83fa8pV7JsLGmixi95uLsu0QV_-K3rvUlWaaGHr6Lz5aDEGRtTGuIi5rkme2OHINQy-cGikK5E1V8lfsbNEFg7JYDCIhtr6WJopGb2WTYmNlEGBSKSDBnCPSB8ac5ktqGerknxV1bofyH-lolizd8DMGZJ1aYCmgzxvGnxw3E901adx65GDxozs90WlsDYlRQ6RABH_IyMsjzy87WJ6iSiDnFz3DvwY0L178JdaSYVHbjKYQUKh8e1vyJPJrClxkecc4cBMmL7EN0-j5Qqg--xgTGcVnrjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زین واکر بازیگر دو رگه ایرانی آمریکایی و برنده جایزه نخل طلایی اعلام کرد بزودی به ایران خواهد آمد و یک جانفدا میشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/149853" target="_blank">📅 15:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149852">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
یک هواپیمای سوخت‌رسان سعودی در حال بازگشت به پایگاه هوایی خود در جده در منطقه مکه پس از پایان حملات به یمن رصد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/149852" target="_blank">📅 14:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149851">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترکیه تودی : پرواز های ایران به ترکیه و بالعکس از اوایل اکتبر متوقف میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/149851" target="_blank">📅 14:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149850">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
مجتبی خامنه‌ای: بر اساس محاسبات الهی، ایران قدرت اوّل جهان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/alonews/149850" target="_blank">📅 14:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149849">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
دلار 244,000 تومان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/149849" target="_blank">📅 14:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149848">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
بیژن مرتضوی وارد ایران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/149848" target="_blank">📅 13:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149847">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
اژه ای: بساط برهنگی باید جمع شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/149847" target="_blank">📅 13:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149846">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دلار رفت بالای 245 هزار تومن  یکی عراقچی رو برگردونه
😁
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/149846" target="_blank">📅 13:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149845">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2ZnWnZyNFwOPaQm_AskaGOSfn7HfbIwgCa8qksLrZ8uk2QdgoIunc6pp7D6otWxDLRAT2u_UoDXDOip3e7QNnNdIEOim6X4mLxChs24WWKiXSeEnhGMQcV3dbTc6u-EzAIOMTsgAmu2eKP5CiFTUn3B6yGgRb0QgkPDKI1eAhbRUnH8vUGrFnek5RXYWYbGr2wvsoaMS0x-_tWTThBFy3ujpfP54_yiEddRfIiwUnxtg8IegwwaGRPwEy12QXQAhyT2lcT2AVGMY6dqsEa0WB6blrf3ZRXVd1uOpUj_Q-2UQlqivRfTlcpRqo2tS5EW2Tk27krl_fx9P4oHJj2a3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت ۱۰۸ دلار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/149845" target="_blank">📅 13:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149844">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
بیانیه جدید مجتبی خامنه ای تاساعاتی دیگر منتشر خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/149844" target="_blank">📅 13:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149843">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
فعالیت هواپیماهای ترابری ایران در فرودگاه بین‌المللی مهرآباد تهران: طی چند ساعت گذشته، یک فروند C-130 هرکولس نیروی هوایی ارتش و یک فروند Il-76 متعلق به نیروی هوایی ارتش یا نیروی هوافضای سپاه در این فرودگاه به زمین نشسته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/149843" target="_blank">📅 13:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149842">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9Fue_cYFVE5JgUjTknrk2ND6abxhXWkxVCdPs99gG3r0IDa7rR-blaS8vwGnIevGmBychu0Sa7Uglx7TDosevJ_tURlmrZzNS5e6OEsEkIEoNxnfK8ykLUtWUa7lE0LKyjwvYZGM7W40ZWhCVdkq3deKZBCnuQZ8ewAiRZK4xicXH3WuTalE8ukT05werhRruLevzqdxi7CXumVhLR7I5qivTnOgLfvpwmcp9yYiVSth4XE96QMbP2T5PUFymMacAcQp067l_eqOPN19oR3rnm0VLSo69LC-Nr6h-SGYnIrCWn2oGMNbm26132NguXQIM0ku5UohK-fdf1Ows7-FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حجم آب دریاچه ارومیه با افزایش حدود 9 برابری نسبت به پارسال به 2.52 میلیارد مترمکعب رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/149842" target="_blank">📅 13:16 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149841">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bebdd4e5.mp4?token=gWVSw05zl7aok2jOEyiGzOy_PsLM2syDZzxMFSTXeOq8id7oF0bCXrRiLdnbAtbi2c6rpi2wMocfWDrB6toTwqblCUkIBoS0rHxmoazdwp1e8pun3q9ZEdT4ERYnW6IYsUNOUCr7hIzQS4B5JCbFHdbUQ6QOsp23fC4504QJhYszSdtmw_MHOtpHdy9mrWS2pa-TI4BdkMFs2cVIMrxjPHfeQpc5PMXHIr8ZQKH5o3MMMehyygY-PeQZ-MSxzRs1lvvrujxEzHzZsors_CtFE9LsJBH5pn2VCTtrVE6_Bk6lESVX19Df9zW5maMbjVAi2WV2S5-hJly53QVv3ZKvDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bebdd4e5.mp4?token=gWVSw05zl7aok2jOEyiGzOy_PsLM2syDZzxMFSTXeOq8id7oF0bCXrRiLdnbAtbi2c6rpi2wMocfWDrB6toTwqblCUkIBoS0rHxmoazdwp1e8pun3q9ZEdT4ERYnW6IYsUNOUCr7hIzQS4B5JCbFHdbUQ6QOsp23fC4504QJhYszSdtmw_MHOtpHdy9mrWS2pa-TI4BdkMFs2cVIMrxjPHfeQpc5PMXHIr8ZQKH5o3MMMehyygY-PeQZ-MSxzRs1lvvrujxEzHzZsors_CtFE9LsJBH5pn2VCTtrVE6_Bk6lESVX19Df9zW5maMbjVAi2WV2S5-hJly53QVv3ZKvDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آماده سازی روانی برای جنگ سوم ؟
🔴
بیش از ۵٠٠ بیلبورد دیجیتال در نیویورک با موضوع خطرات ایران هسته‌ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/149841" target="_blank">📅 13:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149840">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f40e6d7ad.mp4?token=jzubuGFMWcpDjz28V5d0r106nb895St1Uy3RgfOHZ7pYXTZjZfe8AWpS7A3s2MRf9ZSmWKkMdFkerw0SpCGshPygSUTaU6iYvj_r0MNuA1tSQIKczWPSPzxAovlPXHIWTg4n_8sjOt0zJYSSJnHc6ul3vI8h9q8-ANEG23lS4khGG5-798SF9chbzMwcnAPfKFrr-w1XeTRp-_DdfJ639Wo7usCEMwEe7N0Unn0HICfRM5Ao_CI3oLKg3oQDVF-oMQw0kPRKlYE-OitnG3qEpyWrk67gyzqkKdV-8BvlSAfgcO32lpvkt3bAuqUSBzxQ5xKDXhJ8JK3Thh29OHXveA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f40e6d7ad.mp4?token=jzubuGFMWcpDjz28V5d0r106nb895St1Uy3RgfOHZ7pYXTZjZfe8AWpS7A3s2MRf9ZSmWKkMdFkerw0SpCGshPygSUTaU6iYvj_r0MNuA1tSQIKczWPSPzxAovlPXHIWTg4n_8sjOt0zJYSSJnHc6ul3vI8h9q8-ANEG23lS4khGG5-798SF9chbzMwcnAPfKFrr-w1XeTRp-_DdfJ639Wo7usCEMwEe7N0Unn0HICfRM5Ao_CI3oLKg3oQDVF-oMQw0kPRKlYE-OitnG3qEpyWrk67gyzqkKdV-8BvlSAfgcO32lpvkt3bAuqUSBzxQ5xKDXhJ8JK3Thh29OHXveA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسن روحانی: سوییس و چین برای مردم پناهگاه اتمی دارند؛ اگر کوه‌های تهران مجهز به پناهگاه بود، چه می‌شد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/149840" target="_blank">📅 12:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149839">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9511f67559.mp4?token=CYuBcji8wvkcps_eBnFrqStkF-Eg7kaGdqVvqEZ8WNSqKJI2HqP5nHmHtE7TCk3tKw-EDYjdXHquyrg6ITf2HeUx_owK5tSuKgHU9MHUrhTfjPPIeYGjEW4jW1E2A1hQ_7flDmjctLNzFiFC1spNjepLQgPI2UQaaxhwpRz2XA1Vq-sAs__HVpOZ96-jwkIgyzP8PUQMcBwfUMUL9txs_L9Wl0BEn1dP1FSCQNaxagiUuY1_MCnCkCu13Uzgnf5NwjZVSLhQjaNBN0RnbneTUMGv8Y6-dAYo-PeorptI_DsCyZ7enTizejLIWjWozo2L2OopYlvdbShnmTdx4G8FzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9511f67559.mp4?token=CYuBcji8wvkcps_eBnFrqStkF-Eg7kaGdqVvqEZ8WNSqKJI2HqP5nHmHtE7TCk3tKw-EDYjdXHquyrg6ITf2HeUx_owK5tSuKgHU9MHUrhTfjPPIeYGjEW4jW1E2A1hQ_7flDmjctLNzFiFC1spNjepLQgPI2UQaaxhwpRz2XA1Vq-sAs__HVpOZ96-jwkIgyzP8PUQMcBwfUMUL9txs_L9Wl0BEn1dP1FSCQNaxagiUuY1_MCnCkCu13Uzgnf5NwjZVSLhQjaNBN0RnbneTUMGv8Y6-dAYo-PeorptI_DsCyZ7enTizejLIWjWozo2L2OopYlvdbShnmTdx4G8FzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت خارجه چین درباره کوبا: «صرف‌نظر از اینکه چشم‌انداز بین‌المللی چگونه تغییر کند، چین قاطعانه از کوبا در پیگیری مسیر توسعه سوسیالیستی متناسب با شرایط ملی این کشور حمایت خواهد کرد و از حفاظت از حاکمیت ملی کوبا و مخالفت با مداخله خارجی نیز قاطعانه حمایت می‌کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/149839" target="_blank">📅 12:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149838">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
نخست‌وزیر عراق: نیرو‌های آمریکایی به طور کامل از عراق خارج شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/149838" target="_blank">📅 12:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149837">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0_dJQ-f_W9B9eki9kOVYxsL4NtYDdDdo_BVFZW96H8OP79aJTZDznx9rP9Ayttqn3sn0UXNa1T6ELe-CGKBvqlRMzVvpTE3rtiiLRbHVKXIEao8mzN-DJ3WshD6gvI5Q77AGTE1qN3ADlWgRh1YUhtoPbbuPbBrZiSSaA2Z-wevQe8kdzhdZF3fsSKZVVlOqIftlRk5TW0aAUwTbJMTB72IMIJJppxxpbSO8nItLGHpZ6FOie5YzEi6XlVbaMavO46wEGDrP4B1yvwR3LyVRD4UXBCCtf-mdaIXfJpscqhkfJU4aCjApGFAA0Lk1LZEr6avbQC--liXo4Voz2Czsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رکورد تاریخی نقدینگی در جهان
🔴
حجم پول ۴ غول اقتصادی دنیا از ۱۰۳ تریلیون دلار گذشت.
🔴
تزریق پیوسته پول در ۱۰ ماه اخیر یعنی تقویت سوخت طلا و بازارهای مالی، همراه با هشدار روشن تورم جهانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/149837" target="_blank">📅 12:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149836">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSKxqzRfx2jAsGkUZTlSA7JWlshbfFuAGb3qlcsec9IFickjkt4UWkKE7FBqQmnAR_VX9Qp1ZY6t24b5--PS-_8xf8TV4QdomSzEzSPlUymsjnb_i8urwZvvRyPoD_4O-q1uFnKrK0tTrtD9vL2DWhcgxHXiSTMvXirn1Z_mttbRxaVe5riT1yvJ_X0yitvRSpm7C77y7v-25oqRLfuO14UUqw61VyhDlxcfh_CncLGfuRc604H4O_dyayfU1KJ-tcc20Vc760TbCb_YgbrLX1-QmUgP41tSi-c7dqraLVKZ6MDgVqfKbOQxVPJYvuz1q_ZE13Furj554o3hcSw6hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای حوثی در جبهه "الأغبرة" در منطقه "المضاربة" واقع در استان لحج، پیشروی می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/149836" target="_blank">📅 12:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149835">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✅
هشدار جدی به خریداران نقره و مس در اپلیکیشن‌ها !  بزودی اداره مالیات به سراغ شما می‌آید...
💠
قانون‌گذار فقط معاملات انواع شمش طلا و انواع حواله‌‌های كاغذی يا الكترونیکی دارای پشتوانه ۱۰۰ درصد طلا را معاف از مالیات ارزش افزوده دانسته است
💠
ضمنا این پلتفرم‌ها…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/149835" target="_blank">📅 12:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149834">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74d9df52eb.mp4?token=VCrANnPPh_2uVp9rMjA15zx8miUm0BbeVQVZ_kOhux2z5E9u0gJ7PFPLpXZdSJh1L4dCajzcK4UyvWoD0P4Rnq_qk4DakUsXtLUKLpBvDYu2J_iPtR8IkSTeKHk__nqXZ_gsZcnzb3_-Qt6u1WzLFKWe2U31cELeLbUtK0l7zXzj4DtpP4-XKNV4860i5kz9xtl_IzO_hm0S3ieeUgLI9b0NTvpMPZbPOLWdbZygPc2SApcnnK52L7hL9D9fkDM2wM93X2YeMa9l9f09jJN9YPAMR6-EHcEqHZISD2d44r5FuSJke2Xx8DFULAKYKd8--s1JfmzRFXLvaYjj9gTw6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74d9df52eb.mp4?token=VCrANnPPh_2uVp9rMjA15zx8miUm0BbeVQVZ_kOhux2z5E9u0gJ7PFPLpXZdSJh1L4dCajzcK4UyvWoD0P4Rnq_qk4DakUsXtLUKLpBvDYu2J_iPtR8IkSTeKHk__nqXZ_gsZcnzb3_-Qt6u1WzLFKWe2U31cELeLbUtK0l7zXzj4DtpP4-XKNV4860i5kz9xtl_IzO_hm0S3ieeUgLI9b0NTvpMPZbPOLWdbZygPc2SApcnnK52L7hL9D9fkDM2wM93X2YeMa9l9f09jJN9YPAMR6-EHcEqHZISD2d44r5FuSJke2Xx8DFULAKYKd8--s1JfmzRFXLvaYjj9gTw6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کایا کالاس، مسئول سیاست خارجی اتحادیه اروپا: «ما در اطلاعات و ارزیابی‌های اطلاعاتی می‌بینیم که روسیه در حال برنامه‌ریزی برای اقدامات خرابکارانه بیشتر و حتی حمله به دموکراسی‌های ما است؛ اقداماتی با هدف ایجاد شکاف در جوامع ما و ترساندن مردم و دولت‌ها برای جلوگیری از ادامه کمک به اوکراین.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/149834" target="_blank">📅 12:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149832">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d16XKnaJUWzr3or63-y4LjhFUAMvDBXij0DQzFFYz2v1y4D4EOhjXpekNoT5gxy_iyE2_cHbbUTYa2d85wpR54OnIFP3xXSqzjf-crdAiWyulTGyJ_odgOpvWl6M72_Tg1aMNDwj2EeBsUawoBQc6-ScjNCz9fwTZe_3yVUWcUYe0WkZPIj7K2vAQsmRBvSrpbXk9PHpdZQbIxXnUV3rip2q1xMlvyhwtmUtCLZWs4AYN8idpgvijT6qkbXsj_j8QOy5mDGATG5PJpJ6YHXZVsETB_DrHXMoE-plQATEGWVZcRBUmUZPYOic2A7NHrvBtQ8MPxuyN1JsvfbS8Rvhrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZDEopvYkwacK0p5ZRcTTUk6nIRiuRWmISpKtYGji2V4t7FKC-gWtEbqRNY8LcOsaf9T2tDIUpTQpi1kjNW9pJSybGErCuF-WO-gUgIupjHLjoFmNA0BNtiri_FFbDPUqszmgMnHkkUNkkn-bLU6rFg2JcjPZaNu7jFhT55hIXEDzYpCqLUO_MqtlI33gkinH5WUJD2rtkSTLR1bUio4GpRMgxSwhzXlpuJk49Wky_FA1BhtiPOjJjDdZmfqesI0KkkS_KqC34VluLnl6yQMENKJ5Hnd4haRfeIny4CKUJhAW-c0j9BKXHT8Q584GwHRZUHub5UGG3OU2nXiZdDhhZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از زوطر شرقیه در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/149832" target="_blank">📅 12:19 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149831">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04b4864699.mp4?token=KgvCYLEYzk4290dyqtjsygVW7uK7n3KOQ4yPuXPYEfmogWC5bJsA_nk78FVP_7nUPdZlLDmb1q8c4pp5rczu0-VCMt497qUEf-wUOhKWcQKJqjbce8LkTwQyl5S0ai2jFcA6WgvREPg4oP_fScRYw9H7G0Z9_bB_wVAotHdDCNrmS10HfLbkYCzPr6YnRiSiRJD9FFG9ZDvjP_UKKN1kQb0_pCNQR5AlklgetZEis_oAfqs_6GF7ZML9qiLiosUI1tajYC7rGlX7gYPEixOnMIQvSDzSBZ6sYd1i_zkZPcrne7QsCz1nL2iPbKRZAZ0wMzu58DNzG2DFSmks33a-kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04b4864699.mp4?token=KgvCYLEYzk4290dyqtjsygVW7uK7n3KOQ4yPuXPYEfmogWC5bJsA_nk78FVP_7nUPdZlLDmb1q8c4pp5rczu0-VCMt497qUEf-wUOhKWcQKJqjbce8LkTwQyl5S0ai2jFcA6WgvREPg4oP_fScRYw9H7G0Z9_bB_wVAotHdDCNrmS10HfLbkYCzPr6YnRiSiRJD9FFG9ZDvjP_UKKN1kQb0_pCNQR5AlklgetZEis_oAfqs_6GF7ZML9qiLiosUI1tajYC7rGlX7gYPEixOnMIQvSDzSBZ6sYd1i_zkZPcrne7QsCz1nL2iPbKRZAZ0wMzu58DNzG2DFSmks33a-kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیوید پردو، سفیر آمریکا در چین:
«ما قرار نیست در دنیایی زندگی کنیم که برای انجام تجارت به شیوه‌ای که می‌خواهیم، مجبور باشیم برای جلب رضایت چین سر فرود بیاوریم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149831" target="_blank">📅 12:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149830">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">طلای 30میلیونی
‼️
با توجه به خارج شدن قیمت از مثلث  عملا اماده پرواز شده و با توجه به قیمت دلار داره به سمت بالا حرکت میکنه  فقط تنها دلیل حرکت اهسته طلای ایران، ریزش انس جهانیه وگرنه قیمتش باید با سرعت بیشتری حرکت کنه   @shahab_gold_trading</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/149830" target="_blank">📅 11:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149829">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_cY8qeMA7JG_2mW_JakBVw68YPp96kEg1_WhCJeuSMhzCILYYJhuYqp5XaZT8TgJ5ctvzUkkMwvo1-hhznYdvdQ-091QXj3p3VdySnTwOOp5GQ_mE3vYopUT5HrXJlo3f7O63tpHi20MuAwhGZrWuZ4jHhIXAI-pwWBgVf7CXfuB5kbRcAyJ3AjCubjQ0BSoo-NbD-tdU46Z7Bms9owToAuh3GBp9DY3jKo8zgfZM82DK8cE-nZtTiTNTXFcbgJu9XKIhhEMve2tYplcO0UHPXWq4A20oMyJIBzpsn0aCRihDV3OOEJQA8yXaO5wuiAIU_abDKu0aOPyvhewkl91A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاسخ مدیرعامل خبرگزاری قوه قضاییه به رسایی: وقتی قانون سراغشان می‌رود؛ می‌شود مصداق بارز بی‌عدالتی
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/149829" target="_blank">📅 11:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149828">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل به نقل از مقامات:
دیدار ۴ ساعته نتانیاهو و بن‌زاید در سفر یک روزه نخست‌وزیر اسرائیل به امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149828" target="_blank">📅 11:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149827">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وزیر دفاع انگلیس: احتمال دست داشتن ایران در حادثه دستگیری پنج نفر [با مواد منفجره] در نزدیکی پایگاه آمریکایی فیرفورد؟ هرگونه گمانه‌زنی در این مورد بسیار نابخردانه خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/149827" target="_blank">📅 11:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149826">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
واشنگتن: به‌زودی ساخت سفارتخانه دائمی آمریکا در قدس آغاز می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/149826" target="_blank">📅 11:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149825">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hov08h5gQaIou0X-xElDJIj7Om0RMktbUdcrYW6qtoCmZhNLdUnGBbaUrP1gQ7FV6Mav7uAod0ofZohSgjRiK462goDQF-Z8ipSkBvsG3H7Ytr1fuICl6b7O5U2bbt41uCrtZ0iagWko9j8Z8r-bh-7CThoSzaIfaZowvZfYfqiUbZDUatonRx7aVSuzbU3uAYwmfb95szP7xJQP696RoECbceM-iuaUY21WtlTBwDYs7CXfgSebJY51geyRcDDcRi995Rdfn_2aur5Hf5Pv0xb986CoiaFCCVGpjTBxShsUto76eHcn1v9dmK7K66tfvFJqsgumv6xbM7gZjdm9lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت جهانی اونس طلا ۱۵۰ دلار کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/149825" target="_blank">📅 11:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149824">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b519bfb392.mp4?token=KnD0u_-FqRo53FHuuDGanrOoneLvDNNB_hKjh-c6f19y4hYANSHPBOwKEnDbjZxR0OzJb7bO4ygL_81YaakdQMkM0ZqmWXFZmVS84BBIlDBzxojtKTbaAIGcBK2QIFLdJTGV0qaNFtWd-W9cl_udl0f6h6ZEgSCPLXYJxuymj-zq5lwLkym8qIg3mTmJF9lwdrVM0BGLXB1_xsX6joaOT7Lty5OGz9dXXc1DaZMtFZX1zj7mT-cteWCp7ZvjClQiOh2NDp8FqurD5w4GYhU8iPc-KTNjFqulf06HdXRrfAYZBMpzDWk6VLYDoONfj7jEZlNxZVNpzZ53mG3YKphrnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b519bfb392.mp4?token=KnD0u_-FqRo53FHuuDGanrOoneLvDNNB_hKjh-c6f19y4hYANSHPBOwKEnDbjZxR0OzJb7bO4ygL_81YaakdQMkM0ZqmWXFZmVS84BBIlDBzxojtKTbaAIGcBK2QIFLdJTGV0qaNFtWd-W9cl_udl0f6h6ZEgSCPLXYJxuymj-zq5lwLkym8qIg3mTmJF9lwdrVM0BGLXB1_xsX6joaOT7Lty5OGz9dXXc1DaZMtFZX1zj7mT-cteWCp7ZvjClQiOh2NDp8FqurD5w4GYhU8iPc-KTNjFqulf06HdXRrfAYZBMpzDWk6VLYDoONfj7jEZlNxZVNpzZ53mG3YKphrnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیوید پردو، سفیر آمریکا در چین: «ترامپ همچنان می‌گوید: «ما به کشورهای دیگر در سراسر جهان تسلیحات می‌فروشیم.»
🔴
او حتی در مقطعی از شی جین‌پینگ پرسید که آیا مایل است مقداری از این تسلیحات را خریداری کند؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/149824" target="_blank">📅 11:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149823">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/647255f9b3.mp4?token=CuRrXGFx-uVeyfTsGp0bHqP8oyzeieKskQS3b6VtvXcOm4daVpDG0nCr4KdUdldCLpV2MvMxzfdAwWFw-F8vuZPk24V8FReSeBu7I-gkUhO7xF3xk8EC4rTFptkCbMXzt5EOzkvZwrJgOfGblWjdjT44bxsyQveYDSCNeIEyjZYIrFp0Igzzie-3DUr4e2f2qJrGRkRXf_FX950qLbqu8cIxX69_-UfvnlxgkuY_WGIsMYeQAxO8XaoLv0vWvpZ9oSyb9mMRHNM2ZUAvFkrMcvZQ6Fx26ZG1FAo0L0Bj7FDrqNcxOSLz0LxeAwRKU6AC97L0kaBdiByjVmWW45xnpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/647255f9b3.mp4?token=CuRrXGFx-uVeyfTsGp0bHqP8oyzeieKskQS3b6VtvXcOm4daVpDG0nCr4KdUdldCLpV2MvMxzfdAwWFw-F8vuZPk24V8FReSeBu7I-gkUhO7xF3xk8EC4rTFptkCbMXzt5EOzkvZwrJgOfGblWjdjT44bxsyQveYDSCNeIEyjZYIrFp0Igzzie-3DUr4e2f2qJrGRkRXf_FX950qLbqu8cIxX69_-UfvnlxgkuY_WGIsMYeQAxO8XaoLv0vWvpZ9oSyb9mMRHNM2ZUAvFkrMcvZQ6Fx26ZG1FAo0L0Bj7FDrqNcxOSLz0LxeAwRKU6AC97L0kaBdiByjVmWW45xnpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیوید پردو، سفیر آمریکا در چین:
«دونالد ترامپ، رئیس‌جمهور آمریکا، در موضوع تایوان به‌اندازه‌ای که من تاکنون از هر رئیس‌جمهوری دیده‌ام، موضعی قوی دارد.
🔴
ترامپ تاکنون ۵۰ درصد بیشتر از هر رئیس‌جمهور دیگری از سال ۱۹۷۹ به تایوان تسلیحات فروخته است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149823" target="_blank">📅 11:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149822">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeugbvtQ88rG1TYayN01m3ydgowCqGz5KhJDmy01a6tJWoKhrdEfqE0aQe0A1Iuv9IG27x7Kn-KK9EWP8WDy8350L0PQ-WvqaDXgrsCAT5GsVc-KW-f3n7m5x3Z28HQqCa5QbXSvR5I7OcxGAAUWJuRt0Xhpo0U7z7WPAlCxwm-RzhVKKSqbVUunrNhibEeN660Hkgc_8VYU6gCPvhXvDRSEV24WsRvwagn_9hC5DBmbNS7ZL4fCzjirKcri5j3QCl93hC2bOWCZDeoW2UToE6xe3HUM_83NAB1CI2KFmhihVJewmNqPFEH20ExylUBjc-qrw4ULm584ZL5TTy6mmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیژن مرتضوی وارد ایران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149822" target="_blank">📅 11:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149821">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0f86249bb.mp4?token=TUzaPuVsK9PUXbpkbmq3yTXf_252jC6l660vQGLqZCTx6a1kFEL7Hz3IuJDx_RvVoyA2Zh3sfkgTz-njdmgRpIVV66kMMvMIWaCQh9hp5vy787sK9fcsHc_XIK6oZA-1r7IL-yPtjGFGshXWZ9aK0qpgooQmAyf_JsRJiIsviPR6Wq4x0SDFeiKoHWDbKJVzaj8QRMinqcpy7N5YPfnML5m8XTIlIC3G425QAXXvXotQ_VpWDT6vcQ0vviezW42N26S9NJLcBogL0rmQXzvga05Z-4HDjmkNpklSmi92KCpcacEIsoYlgVhjFFXeI0TLWICceRYBDSscgV9Tb5OZoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0f86249bb.mp4?token=TUzaPuVsK9PUXbpkbmq3yTXf_252jC6l660vQGLqZCTx6a1kFEL7Hz3IuJDx_RvVoyA2Zh3sfkgTz-njdmgRpIVV66kMMvMIWaCQh9hp5vy787sK9fcsHc_XIK6oZA-1r7IL-yPtjGFGshXWZ9aK0qpgooQmAyf_JsRJiIsviPR6Wq4x0SDFeiKoHWDbKJVzaj8QRMinqcpy7N5YPfnML5m8XTIlIC3G425QAXXvXotQ_VpWDT6vcQ0vviezW42N26S9NJLcBogL0rmQXzvga05Z-4HDjmkNpklSmi92KCpcacEIsoYlgVhjFFXeI0TLWICceRYBDSscgV9Tb5OZoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیوید پردو، سفیر آمریکا در چین: «دونالد ترامپ به‌صراحت اعلام کرده است که هرگونه کمک چین به ایران — چه در قالب اطلاعات، قطعات یا تجهیزات نظامی مستقیم — کاملاً غیرقابل‌قبول خواهد بود.
🔴
شی جین‌پینگ به او اطمینان داده است که تغییراتی در این زمینه انجام شده و موضوع در حال بررسی است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149821" target="_blank">📅 11:19 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149820">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eea1b3b65.mp4?token=IhM9mgcC7PQpZobkCRLgdlACrrqNHNPv6mSmxKX1k4cq6DsnQjP-nnuS1jvK0tw478fVovWQMZEwP7NpRfh4MeCxV2rgBRZjr2-ITu9N93KO6F399AljvAK8rz25GAf1FrS9aq6r6-mzUHuLRiKkv5YopmMJDzg8e4Xb1qRnzCVhqFd7xhC4UIYv1tJ1y9lEqy4pB1u4qQ7Gqf7xuMuCO8eLVzTI0FxFJlRhESf4oP6tv64eGq5gRpUuvk7pzLw70Qpaji_BOr3MhmsV_Xhb51VLesNlOgmc1s0M65aXSe5OxPfs8OiLWPT8txqDtDexoY6dJRoZxMUeyTnlAw9X1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eea1b3b65.mp4?token=IhM9mgcC7PQpZobkCRLgdlACrrqNHNPv6mSmxKX1k4cq6DsnQjP-nnuS1jvK0tw478fVovWQMZEwP7NpRfh4MeCxV2rgBRZjr2-ITu9N93KO6F399AljvAK8rz25GAf1FrS9aq6r6-mzUHuLRiKkv5YopmMJDzg8e4Xb1qRnzCVhqFd7xhC4UIYv1tJ1y9lEqy4pB1u4qQ7Gqf7xuMuCO8eLVzTI0FxFJlRhESf4oP6tv64eGq5gRpUuvk7pzLw70Qpaji_BOr3MhmsV_Xhb51VLesNlOgmc1s0M65aXSe5OxPfs8OiLWPT8txqDtDexoY6dJRoZxMUeyTnlAw9X1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیوید پردو، سفیر آمریکا در چین:
«شی جین‌پینگ در ماه مه موافقت کرد و اینجا نیز بر آن تأکید کرد که چین از دستیابی ایران به سلاح هسته‌ای حمایت نمی‌کند. این موضوع بسیار مهم است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149820" target="_blank">📅 11:19 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149819">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وزیر دفاع بریتانیا:سریعاً و بدون بررسی دقیق، ایران را متهم کردن به دست داشتن در حادثه امنیتی داخل پایگاه هوایی ویرفورد، کار عاقلانه‌ای نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149819" target="_blank">📅 11:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149818">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یکی جلوی دلار رو بگیره
‼️
تتر از ۲۴۲تومن هم عبور کرد</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149818" target="_blank">📅 11:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149817">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ir8MCdPrD2-tM3Xe-jUDefi6UJp4GykCWw5F2oxDlxn62lS3l8NIFuTISjbLSVkwz_xbDcQFwUl8f8hYLT2m7DEu3ZRBOUmnJLS1qqV-rpmDBktHHoruvN2v0eI02lOfgFeTY6xZP0J3xPcX56GWVI7qNs5NcWiTip0Q0K1DHyhqTUUnzw93kktTDYvP_gyGlpavxTyCbAMNsy_GmxD0-7DuO0d6bIS12-eFCg9vJ6c0qDGMomth-R_PoEkdGMumhnZtg1zpInV35m1U2Bqat2HoSWxhJoEenAu3T3K0JT2nsmo1L1yzJRPsAxyQnxwXuNHFkhwfWS0W_0lixITGYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محسن رضایی: فرصت آخرو به آمریکا دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/149817" target="_blank">📅 11:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149816">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIFU7JoEjsj7oiJ7uEkmzWF4TeBdqFLvVV_hTlkiYiB-Y1ir7SBhyjzVcgAk9kDBkZcfqd6UDDX_47Mbsvs7xgVxEPqQizqeR5ZBhH5lymft4lkmeVOAhya03Q0YfNpv-S85jUkGA6qkW6f6eTSCYqrrVWT5yvSQ7rHWJFTwOXsLYcbeLqY7Qtf_yKamB-toNKP-hUghjJc8rxmZXAFlAJ501TeoPLGARVQWaJmA4-xjAamXBrdOHEWbFxehzr4zmtvG7NnDe0E4l7RoC1iwE-_QiScNoMzEVblEn26CjuUghS3lB-JxuoVHTwYTO8fNmxTYNjh1uSDMiozVN6JmtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت ایران در زیمبابوه: تنگه ترامپ باز است، اما تنگه هرمز نه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149816" target="_blank">📅 11:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149815">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
بانک مرکزی: صدور چک رمزدار از فردا (سه‌شنبه، هفتم مهرماه) در شبکه بانکی ممنوع می‌شود. بانک‌ها از این تاریخ موظفند برای مشتریان خود به جای چک رمزدار، چک تضمین‌شده صادر کنند
‏
🔴
تبادل و واگذاری چک‌های رمزدار موجود تا ابتدای دی ‌ماه ادامه خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/149815" target="_blank">📅 10:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149814">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
الشرق الاوسط به نقل از منبع دولتی عراق: آمریکا به عراق درباره نقض تحریم هوایی اعمال شده علیه ایران، هشدار جدی و مستقیم داده
🔴
واشنگتن گفته ممکن است اقدامات تنبیهی آن، هر نهاد یا فرودگاهی که پرواز‌های ایران را تسهیل می‌کند را هم شامل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149814" target="_blank">📅 10:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149813">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بوی جنگ به مشام میرسه! ایران شاید پیش دستی کنه.....  @shahab_gold_trading</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149813" target="_blank">📅 10:39 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149812">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
رویترز: صادرات نفت خاورمیانه با بالا رفتن تعداد محموله‌های صادراتی عربستان، دوباره افزایش یافت
🔴
صادرات نفت در مهر ماه به ۱۲.۸ میلیون بشکه در روز افزایش یافته؛ با این حال، این رقم همچنان بسیار پایین‌تر از ۱۸.۸ میلیون بشکه در روزهای پیش از آغاز جنگ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149812" target="_blank">📅 10:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149811">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgM34FPvvxBPvhNPiGoa6K5e1Cut4KFhFjyK-UYGcHoIOk1ovjtEbd2NE_zTkfycRvRgjBWLBOTu60lOJMIoZ3ZFTfTjB0MEBXB2rac_v_VSnToEJ2mHZffFRDICaf2a930KK6OhRXk8MUMAj4rVr4eKCFTZi1ChFprAbg-6MoimphqU8cWZ_FCUbku3Xym1Dy2cOQ6Fcdj-uEYH5vo7c_yvt-OsI54XyQY6HliRru_yFRf5fRiO1n1jJCGctpyCdVCUAVdF36D86LjFDDuN6fqzy_zoZuhgOfgXkEZLddCjL13BJJ5LwbN-fxe24yTCekmi6Vik1BFWfEFkfLAElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تتر ۲۴۰ هزار تومان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149811" target="_blank">📅 10:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149810">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
دونالد ترامپ: «به‌جز نفت که قیمت آن از دوران دولت بایدن پایین‌تر است، همه‌چیز در حال کاهش است و دیگر لازم نیست نگران سلاح‌های هسته‌ای ایران باشیم، چون آنها به‌طور کامل از بین رفته‌اند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149810" target="_blank">📅 10:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149809">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a7312bfe.mp4?token=SYmD4CeTrYXGJGVAjDvrAyJjagNSWGtdeVsFNXlp8mCsR575O2ncKRR0nRF4eIuWLxsV6l3lK_6VTuY6TOUCXMUSp2YtImbHTLtw6kle0JbeABiHoes5mNo1Eq_yay_ZGh5VTa_h3Je7qs70aagnICP6L8zoMFu-Mqa2asTDhVtLJdxojamxqLi09XBMxEPah67YzkRzsAl5NgVQflmp47pxZkgfNRW54_bFGlJD5fjMifIIHrBojJXhDzumFi3Qe8gPEORfwCxLCf-2CL4bqNsu3yB6RtKpgYRexfjZ59e93-OVX5UGWVoKb_Sg08pZGcUkmyNIzrD89jC2g3tcHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a7312bfe.mp4?token=SYmD4CeTrYXGJGVAjDvrAyJjagNSWGtdeVsFNXlp8mCsR575O2ncKRR0nRF4eIuWLxsV6l3lK_6VTuY6TOUCXMUSp2YtImbHTLtw6kle0JbeABiHoes5mNo1Eq_yay_ZGh5VTa_h3Je7qs70aagnICP6L8zoMFu-Mqa2asTDhVtLJdxojamxqLi09XBMxEPah67YzkRzsAl5NgVQflmp47pxZkgfNRW54_bFGlJD5fjMifIIHrBojJXhDzumFi3Qe8gPEORfwCxLCf-2CL4bqNsu3yB6RtKpgYRexfjZ59e93-OVX5UGWVoKb_Sg08pZGcUkmyNIzrD89jC2g3tcHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره حادثه پایگاه RAF Fairford: «ما همه‌چیز را درباره آنها می‌دانیم و خیلی زود درباره این موضوع خواهید شنید. گرفتیم‌شان!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149809" target="_blank">📅 10:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149808">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a96eb2ec.mp4?token=tKBGA7OalTA3LpEFvMtj_GFZtcDURh7JokaNk_uKUyuPGdHeTS_kx6i1-8_tShlICTUtVp6MINU4J8kaRpwv4L3pOosz6ZkM4SJy1TYTIgHdIGBVh1VnkmNyeTYAxHka4S5aAGTxJOtExvURuC_uf34MTOHKgB5CIhyunpaOlCIP84rsTbXKaYpT3-0cF6drF6aTXtOPhzeSRsxBB5H6_uDJBb16JMYRQJbsvo8G0K5hOI3BtUfPutE-pAOOPWUpVGBfNJof_VMJYgWg3zB4-N_v4Cn0vSp_jnNKb5fH4uLH_JFhLxd4XZlTzd8KspdHWpdamJFJi95ocFG7rd88gkGhlRgfCj7pxcsbbDGvhQKj0x4IdWKHtfY9Kcfj0GesbHIbWWkcij9rfFQjLkvwx-bRfa0Q218Vx8qt-qltE6kD95FVEmc6-lTMAsut_Iwv6C30aBYqgVVPZ3f92b1A00ltXRPxc_nF_RBgyStPqKeM55XXZ4-SqSjcgGW8fhvtUkBJjaRabQj_nAPZiUkx8tMQ8QtULH0eczhgdd1BNVWv06NVxike0ezFDrQJPd7ibKovE-nfJeix3gtXVEmt9D5HQ5PeWE_LD9Fs020XO70azIPPyvOaug4DCuvS92bKn5goFvB-gM7dUTyHSVpB8YhWdEoJiZ0t46Q-aW1B7DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a96eb2ec.mp4?token=tKBGA7OalTA3LpEFvMtj_GFZtcDURh7JokaNk_uKUyuPGdHeTS_kx6i1-8_tShlICTUtVp6MINU4J8kaRpwv4L3pOosz6ZkM4SJy1TYTIgHdIGBVh1VnkmNyeTYAxHka4S5aAGTxJOtExvURuC_uf34MTOHKgB5CIhyunpaOlCIP84rsTbXKaYpT3-0cF6drF6aTXtOPhzeSRsxBB5H6_uDJBb16JMYRQJbsvo8G0K5hOI3BtUfPutE-pAOOPWUpVGBfNJof_VMJYgWg3zB4-N_v4Cn0vSp_jnNKb5fH4uLH_JFhLxd4XZlTzd8KspdHWpdamJFJi95ocFG7rd88gkGhlRgfCj7pxcsbbDGvhQKj0x4IdWKHtfY9Kcfj0GesbHIbWWkcij9rfFQjLkvwx-bRfa0Q218Vx8qt-qltE6kD95FVEmc6-lTMAsut_Iwv6C30aBYqgVVPZ3f92b1A00ltXRPxc_nF_RBgyStPqKeM55XXZ4-SqSjcgGW8fhvtUkBJjaRabQj_nAPZiUkx8tMQ8QtULH0eczhgdd1BNVWv06NVxike0ezFDrQJPd7ibKovE-nfJeix3gtXVEmt9D5HQ5PeWE_LD9Fs020XO70azIPPyvOaug4DCuvS92bKn5goFvB-gM7dUTyHSVpB8YhWdEoJiZ0t46Q-aW1B7DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ:«کشور ما در حال پیروزی است
🔴
دیدار بسیار خوبی با رئیس‌جمهور شی جین‌پینگ داشتیم که مدت زیادی طول کشید؛ در واقع اگر حساب کنید، حدود
دو روز
ادامه داشت.
🔴
ما پیشرفت چشمگیری داشتیم. سه روز گذشته واقعاً فوق‌العاده بوده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149808" target="_blank">📅 10:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149807">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5KK_Vy0SmZPht0n5dyuYDtzlKKlfkoueKQ0sbiKFF30AqndapggciRcY5YOkQ-P36GLTpkNpnHMZ6WCBwwh0tQMgZY7H_bz1lLJiE3qdbYNyizgUWtKpfywwPRH2C46eqIklie1B0ZAKxxRaUF9tNoWDuakjQNwVs2Lr5eAN3uH1xEIVeOntxtHXlsOsaJ9u2ZzD6GIbuovjrDMcCa_b7f4x8u2-RFRqi32rW3dWA5TbU4tfmirVlqv2x2b65TmnecBuYMseq-T1RPFljTduT3eyuJ0ryz-eIHiqnasOr42jOl21qU32DbSSpolHij-VfhU3tGL8wQI5iNpNiiZtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور محسن رضایی: چرا به امارات حمله نمی کنید ؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149807" target="_blank">📅 10:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149806">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XqiQMLMSmZF7Ytlcy7hVNDLMLm8JorRUmtdx4ymKe91oLXq20t644aYbZD9loA-utWGpc4QBP0HlaQeliIJDwFhrG3uHWXA59u7N9QvUZ4xIiyjR40hZX6Ji1ILs8wXVyymt3drVoDS6Glu1Mmbef3Fz7-jbrJXBrf0ln0yJTaBg7g7mW6lyNScWFof-LnUmHoT-wOthJVcUkLFJVPG7LRG7TCQ6TY5FlQS0l_-es4YdcS2th_AtuIgJBcuxwpL57mfG5PNDd62CUZOVPzTvDB1hjZgjV0Mxn8vSCfzQ57gU1HMkAEzgaYF_bghkSi3kfiqUMakomlMfKEBeVEdu-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو حمله هوایی نیروی هوایی اسرائیل منطقه وادی زبقین در جنوب لبنان را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/149806" target="_blank">📅 09:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149805">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
کانال 13 اسرائیل: مقامات ارشد اسرائیلی که از جزئیات سفر نتانیاهو به امارات متحده عربی اطلاع دارند گفتند که این دیدار با رئیس‌جمهور امارات حدود شش ساعت به طول انجامید و تمرکز اصلی آن بر روی جنگ آتی با ایران بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/149805" target="_blank">📅 09:43 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
