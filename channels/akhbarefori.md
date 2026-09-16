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
<img src="https://cdn4.telesco.pe/file/FIXAL94d67otrcg8al9JeVjYlStH4suVu0r5XETLbJi8FwmuwZqNN3_IpLUuGWr2IbZxXmy-EI9H5YVvn3XSI86dvx9Mr5XHRirG9Zr2D-GUbOmRBjhFVkahDMsIp8xzh5VMdM9MrhtxnBL9IPBFnt3lp4IJzxY9zd8JDfhi7MhdUuizq4SQxFY40YTaQNRcYNGmXVOg3KSJDEPqq2QYf3W_vZNp_INN2c66pn8vI5Zt6dTWBsnZUFhFfYAd9ErQ8iUyjLuAcoJ9sXr4uHIB9R4RTErnF3gAr0fM7piI3sU7c05OHww-jPnUvSuCEjYt-86IjHR_CVgN7xQAZozeaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.1M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 22:28:37</div>
<hr>

<div class="tg-post" id="msg-690477">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkz7wpQ-Ltd19HpDRPrVSN1WivisIhw4gp9bzc6Jj0ClwsK0XjgP2jx8xkwoDZdmCMYa6Ge0TEdGPBWUFXuuMVNOJSOitEHZTNhZJnsMf0HQ8f_U4jgZMnILlB5YvKCwDbYj8Ltcq4zfYgG-yhPdU0OUMXKFB4gsRNkJitPp2ad8xYE4ZNAQYg_xPXIQQWfm3zqqYij6YLplWiXWRdJo39AZWmTGSFoV50Ec037ZqTpZ4KOjRbsj0zUko4cZX7Fac8Qo__vrC3nbPhMbFZKbDtQAaN_NWQYRxXUzAv2fV6ZVopxTK9IZ_cseLQ5m1A1DKqusKYQT5v0VG2FbmoJicg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک‌های مرکزی عربستان، قطر، عمان، بحرین و امارات متحده عربی، نرخ بهره را به میزان ۲۵ واحد درصد افزایش دادند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/690477" target="_blank">📅 22:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690476">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
بانک‌های مرکزی عربستان، قطر، عمان، بحرین و امارات متحده عربی، نرخ بهره را به میزان ۲۵ واحد درصد افزایش دادند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/akhbarefori/690476" target="_blank">📅 22:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690474">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کاهش ۷.۹ درصدی حیوان‌گزیدگی در کشور
قباد مرادی، رئیس مرکز مدیریت بیماری‌های واگیر وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
در پنج‌ماهه نخست سال ۱۴۰۵، تعداد موارد حیوان‌گزیدگی در کشور ۱۸۰ هزار و ۹۲۲ مورد بوده که نسبت به مدت مشابه در سال گذشته ۷.۹ درصد کاهش داشته است.
🔹
در این مدت استان‌های تهران با ۲۷ هزار و ۲۳۰ مورد، فارس با ۱۴ هزار و ۸۷۱ مورد و اصفهان با ۱۳ هزار و ۷۷۸ مورد، بیشترین موارد حیوان‌گزیدگی را به خود اختصاص داده‌اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/akhbarefori/690474" target="_blank">📅 22:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690473">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
واشنگتن پست: آمریکا به اسرائیل چهل هزار بمب ۲۰۰۰ پوندی می‌دهد!
🔹
این اقدام بزرگ‌ترین فروش از  این نوع مهمات در سال‌های اخیر خواهد بود.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/akhbarefori/690473" target="_blank">📅 22:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690472">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
فعالیت تجاری در مرز چذابه روز پنجشنبه از سر گرفته می‌شود/ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/690472" target="_blank">📅 22:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690471">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادعای مضحک ونس: تا زمانی که ایران به هدف قرار دادن کشتی‌ها ادامه می‌دهد، خروج آمریکا از منطقه ناگزیر به معنای بحران انرژی جهانی خواهد بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/690471" target="_blank">📅 22:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690470">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUs8N_CtCXKEOm1t56bkZ9qxIAbJ1_6Yj__tM_8kqF1gFgIh86UlOaBftnlDeVS0Bi-HxptMxF3WCuk8ihAY48UiJ7mtAAaucRjjP3JZ0ztR70JbQN5cnhn_pr2Nf6lGSA861ZGLWWNxr1Lqpy0m2FRgPgQyElixJ03OIwiAMRkX_kbDTdN4Rg7zGAZf5_g0OSrlKLSDF6zJV3omjdX5ktmH6i5Tx9lGUwnv5fvwX_-NTqW6YTrUZdDv8KnfP8vHdISA1lbnEY9msnAWZHg8PYdOPf5Sgqw1GhdcF-jyLDJf0K5Z48jWHqrnsQ2zrrPoJobhbHcuMy2g9czPzPoEqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استرس چطور در بدن ما ظاهر میشه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/690470" target="_blank">📅 22:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690469">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نخستین صندوق سرمایه‌گذاری ارزی کشور با نام «مانا ملت» آغاز به کار کرد
یکی از چالش‌های اقتصاد ایران، نبود ابزارهای شفاف برای سرمایه‌گذاری و به‌کارگیری منابع ارزی است.
در همین راستا، آیین آغاز پذیره‌نویسی نخستین صندوق سرمایه‌گذاری ارزی کشور با نام «مانا ملت» در ساختمان مرکزی سازمان بورس برگزار شد. صندوقی با ضمانت نقدشوندگی بانک ملت که تحت نظارت بانک مرکزی و سازمان بورس فعالیت می‌کند.
در این مراسم، وزیر اقتصاد، رئیس سازمان بورس، مدیرعامل بانک ملت و جمعی از مدیران و مسئولان اقتصادی حضور داشتند و درباره اهداف و سازوکار این صندوق توضیح دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/690469" target="_blank">📅 22:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690468">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CA8LqHUHgcXSipCmxs798Y21hQ0xvuMPbMVVPXCJUFD0G6fCBcponCPz43wHu6SOqJHTjfIMfhjW-hE-KvraWDoEJCfYT6rxcYKjba96vEtOSjHyzFeGEUKwzV4GdXgwJ94lsBw4Dr0NjGatQybAld1SlDmZV3Mc9bfATWFgByPDwm5AS21kFfAZcnQgGg5IbzP0jsEBdvyFvyzoxDEUIQ0ZQKpNhP-Qv-D8JTf-W5nYvA5xarA86qB_cjCf_OCsVObJWjWUp73W2CU_9uE-YoAHdJB-DxiLDo0-l7gS4Hp9YEgJlKzMYgjj9NbMd4B2w6QOYyvMWQVroFJE5zH8tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧥
کاپشن مردانه مدل Ferrari
🏎
🔥
مشکی طوسی | مشکی زرد
✔️
رویه سه‌لایه مموری
✔️
داخل پشم‌شیشه
✔️
فری‌سایز، مناسب
L و XL
✔️
قد کاپشن ۷۸ سانتی‌متر
✔️
ضمانت تعویض و بازگشت تا ۷۲ ساعت
🔴
قیمت: 2,380,000 تومان
رنگ مشکی زرد
https://memarket24.ir/product/brief/63704/180124/
رنگ مشکی طوسی
https://memarket24.ir/product/brief/63705/180124/</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/690468" target="_blank">📅 22:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690467">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qA5RJU96dHIZK6GduFfLmFB17yzR2hIBrZ1NTwdfcbm7oV_6t3yUX12REn1c3wSP5zl1T8AfsZiQO0ULQu_Crws6vlA5O6u72qlFqGtvQDa3G_Z5wQ393TA633K-p6Ffl5lDz255wIbqKpv0GTcV0MCi-0TLkNKTV1x9UL-qiqUJkleO3BkLvXy38SmNcEgumWEhSSfNuNIrl8WcYBPrILj_rU09y0xJ7vuG96cC1uwOjBjyoMHaySnADRwxdcZHoWeTbot2D1lAy-uxt8QsQIgzTMtFXACi_xRLdN43LAl2z0bcjN_ZpyqKCVyZWJRtIw8tk_WlQ0cxF3KvWon8eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر شهید انقلاب: دفاع مقدّس، ملّت ایران را عزیز کرد، روح معنوی را در کشور ترویج کرد. ۱۴۰۳/۰۷/۰۴
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/690467" target="_blank">📅 21:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690466">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ادعای سخنگوی‌سنتکام: ما بیش از ۱۰۰ کشتی را که سعی در شکستن محاصره تنگه هرمز داشتند، تغییر مسیر دادیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/690466" target="_blank">📅 21:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690465">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
انجمن صنایع آرایشی و بهداشتی: میزان تقاضای محصولات آرایشی و بهداشتی، نسبت به سال‌های گذشته اندکی کاهش یافته است
علیرضا کیانی، رئیس انجمن صنایع شوینده، بهداشتی و آرایشی در
#گفتگو
با خبرفوری:
🔹
امسال صادرات محصولات شوینده با محدودیت‌های زیادی مواجه شده و سیاست‌های تصفیه ارزی، رفع تعهد ارزی و سایر قوانین صادراتی کشور از جمله موانع موجود در این مسیر هستند.
🔹
با وجود این محدودیت‌ها، احتمال جبران کاهش صادرات محصولات شوینده تا پایان سال وجود دارد.
🔹
تقاضا نسبت به سال گذشته تغییر چندانی نداشته، اما میزان تقاضا در محصولات آرایشی و بهداشتی، نسبت به سال‌های گذشته اندکی کاهش یافته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/690465" target="_blank">📅 21:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690464">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b0e77466.mp4?token=upFyIVbKIKVBris5R4C1ylEF5A7IWT23wHIVM_8wzuTJHWpL9jM3Fwk8DUKidr6gozbeFgCEcuItSl3APVbzLvri8A5oawtzfamDEX67f2knKdKaysrYFI-KQmRHeqZcr0KlKS7ncwSPDL2bcH3jXCx7aBZ7BbEyh21oWLW1v3BJb103cYLCJ1Y9dZhxFoN6zGwVr9nlJmnXoS6uz7tn1fCmTSTp8xVZKoWvJ-XTHnPqdCuH0esB0UYuaW1g2qhrClcbJKnfBp69rIDiyXLnKZ2V9V2c0Li8Yd-ym9zuEvcyRPMte9Rg0ZYMUnBidERzZe7vUQsFLtO_1jhTZo3H2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b0e77466.mp4?token=upFyIVbKIKVBris5R4C1ylEF5A7IWT23wHIVM_8wzuTJHWpL9jM3Fwk8DUKidr6gozbeFgCEcuItSl3APVbzLvri8A5oawtzfamDEX67f2knKdKaysrYFI-KQmRHeqZcr0KlKS7ncwSPDL2bcH3jXCx7aBZ7BbEyh21oWLW1v3BJb103cYLCJ1Y9dZhxFoN6zGwVr9nlJmnXoS6uz7tn1fCmTSTp8xVZKoWvJ-XTHnPqdCuH0esB0UYuaW1g2qhrClcbJKnfBp69rIDiyXLnKZ2V9V2c0Li8Yd-ym9zuEvcyRPMte9Rg0ZYMUnBidERzZe7vUQsFLtO_1jhTZo3H2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زارع، سخنگوی ستاد مردمی «جان‌فدای ایران»: ورود جان‌فداها به پرونده ناترازی انرژی؛ عملیات ملی در راه است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/690464" target="_blank">📅 21:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690463">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNVG2BCagJdEb7A6gZKKKwrMAn00J7qgkEttj2CHDwG6EY-0mKwuns5oZKsOTaNbqYxalNb_byi7uv7KcQ5uuJa0y4BauQjcZqL9qTYsNntFw7hHIs7h69ij7PTkjk13YCxtP_beBTnrG2syaZWY5Z1Fj5glCx8s97RHY1HWmW7QwDk61MEIat_XGAubcU2x-cvmRKuUj75_UzdQcTbuOKIdBKqylk2jVi_s3Q2ZONJkJiw43Ksaq6auvRLP0s7oAmAAKuv3DVkT2TKi3vdqoHlHdIhQOsVBm8sy_qtKj5YnByE9WSW25QTEQPaTcAGDF6NLhoD-iJZvLNAJo_MF-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت کاربر یمنی: جنیفر لوپز در حال رقص در استان مکه در ۱۹ آوریل ۲۰۲۵. ظاهراً تقدس مکه در آن زمان نقض نشده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/690463" target="_blank">📅 21:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690453">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qm57s9pIRHicC5_-nyb4rqwEDAklOqC6QVJQjnw8Lariu6GtsIGURzfYDTSDCPzU-8_us0PW-zz64z79TucHszEjmyEIUeLecI1MKE2lp5DeTJgFVwjjJYWQjp1PK77W9I_Kh65GdeHK5SKAa2eB0nURXlHPvwcsTxFn-_0QP1dBTRd-pvbobUQqcX8GV8OpE1jQsThZenHNY2ehVHTyqMsYYon0_GIKd9gJXQ4iu4fr57K4cPJWJPC6T26FqSQjNcYzZIfvzJyQWU_aB8d9QUtyHUsA4JnnHXZDK6yiS7TgvBJRmXwe5tj78E5GlndZen3Qeud9GzmBbBbclunwmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQRN1lWFH7wrOLMVopWpHSEDv90Ksm2QuuHUHBBPV5Tm9pyJGpfgXMqaeOUeoz6TBPPT7akOrbbr8TZeziYlo1kJIAV25yG2DbcG6dV9cf5B8uEXmwTo0xczfx_lK-aJFlR_vq6F6MLF0TWz7-UXydy8y3xk5277cX-g1ukfkDBNQKQJQ9MUMrQyd10SfFl7k4Ue6q2Cpv9zGTfMFHDfanmgL1KDNnStz0lwBsfg5xVJwbuZwiT7Sn8uJGJJXB0rfVDt_GFfnHCXEH9XWiBsEeBExBcGmP8j_p_Hi-Ck-UxOoaWA5gUiq2e9CmyPTAiUQkkfrE0HF-BIV6F3vgo3KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oXhYWPXGMZzy7f6xuJqQSI87R73Ikg5wf6eWm4HWe_UPfnNpIQOPbaoIOPvIg-VBHS3nBNJvkfW5ld54vzeCopJyclSY13imAND5hRwZ2rDlbXSF9R1eFkb0GvncYDlLxa8p6GH5-QCAw1XacJD2p_3K-zS91ROCsALODysBy1zTTgZm-XB-trt7sCEL2v7_duhK_dSGQmigMUGWphAcDsnvQKzWBCG-gAzAvQ1MUykMyIxgIYCjti_aXdJ5Fn0pd2EVW3tofDkiobb2h8gIObYUWyUJ052WDoaJStVP4zaNIns9T4FJO8waeFJEk1jqL3kG1NMzI1QxKUuiNcLi_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pOHfF9r4clL4HvVG8P718vte4TC7rGWlZ4l0cYkJ2xcilKW6Dn1EPTHeZxly0AX5rshmV06VDIVBDkbrTywtk9NvvCgMCdpNJDpGAu5Ok0fNkmUHG5G0fasIufR1fFEIOBzoqT9fpZNAwxD7O1lCDEPVcncD7qM5oansq-bXp87sWgkNFBFn6a9zay7EIh0Rqrr6X3Shnlj5pyeM7Xrz9aPYIW-p4MwJUe-OV40dP-6iZKiaSZpeTD42r7EMPu7c1baDKng5BnSJXB-gPNy-A8M7uGXJm_Clg66jlR6m5qw76lA34dG8YKvknHZNsQpw8j2z2hPZ1fzhgKA5TjChng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mRmwwe38auteoLHyN370qzvBhRMp24d46ySYJZBsHsxcydgEvc_PNvVN--YodM3woP2PNn-qPl5cyhNaPBg1Dll1JAoaHxmDWVab0h8wyyfSZ1uAO3aet7nTS1ZwbgFHVtIFuEo_TxcOS89SmkHP7eEaPsG_R55zOYsWtVLNbMWXHNmss6GCEzKmlFVwKvpz-fjoDTpAW2DwUyKDjwffn6lWK55nr_yrMoIP0GydKVAmXgOJHS9K962UB6L8s8eV9IDJf-vF0JdiLlUA9NSNsJsqQpmE7AjsCBa3V_yNBX3QE7iCpZ2DLJKvTmnYYHx2VyTUa4XE7t-PRXx9S90pvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ijy7VNwgVnBZk3O4sE4zU2zg84WVYHQk0-JARtUSsHph0azRjHhP_d4E78HEpuBI9m-9U2xMyWF_xqwEAFF9oT3MW4zpwRitXqhbHewdemu6yePrjIh3qIqNmvK7f816wjmibAhQLUdqh1FAJKL6Ir37w0R5TSVTTrwp8s9QBnILpLB-32FF1ISqS0n3LVN_qPpa3IuO_srMo-CUQIFHk19SvD2WFDf570B55EK3gcm-V1ly4F8kmpJ0KzoViOdSdIPVF3pZNFevMP6u0a-W1frnhHzV__9x97iOF1V2wfARqkrMWeKILo1DIiTraKPY83YyaGTCF4V-DxmpHqtjTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BrxyDjGUlZZtNjJw2Qkz3wE-H2lKP_ziFGtFCS64Dr67Q9S-3W3GnC8QKZK7isRJWt4kX1TdvYLLpJPqO-kbeAzIVZXTZVw7EW5f0MEXMurLvmLLq0KMpc6e-eOQ1FOkm85UEiRMQnkajcvVr8waGNC2uBweXsjHbYMFigo7wtiVCBFCtSwvIRSjCpHAGUhROe_TD1u8QXqpad4USqHe9I1APymnEqD82hKzfblbLGPxuZRHg_qvffYZ5mOBeb_YKvX_deYUhDxWy-v1CQZJ436IWcyMRhN5aFZZGSvkV0XtE35VWoNMwT4BhfU8_GfGMeLeHuLuZs4fxCOrctla2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/REn7AKq3BM0W1XBvJBtxdLbUlDE3QYTDlhPLxPY632hPnDI8slNppSHIVpT6qyTQDIdOhH6bDAJg6NbcM6bdlHhDYoHPLjSZtfBiOyoacDvx6_kVGAPSKEErgqmxQWhApjA7wgcIy7yX5ub4lcdA5p6QImk54P-L0peGuzBiWCM_-Tj1w3Jsowd1tuHnqygrRDixuFQxdukpSERuw4nwmGV1hRDuzDJfwwL9qx4MeSSv9kE-Xi5UrKCdghAOH-Nm9Dgsg0x-pLc0zwBHBM5BHt64z4dILfn15WQhO8KOad7ma1Vgzwi1-N8HmG7vTPS6rfHtjIbvjanDD99QabMkpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzOGZ6Tt0QNeP8OLIsgfs3Fp5zn7hfH_W5q19WZr79I8Qi3RRl4aQiFMeqyDZyWwLgqQrTW-ce6S7CXHxn5163ZM1ypl9Y0NSHTgN8-x-2MnDRvnGBMe0jngq3EUcvGjTeNuKMWSYYMgDKeFURiqsrWAMQWkrsigumVAvshM8djG0JgDgEajnXgCSXa45uGJ0cI16oEE9fIKYEfDEM4ejEQML4248e5WPIv4oujQokkVTHzic4u-NF1K3_Pf_G4qmG8K9CgAd-FP-gNsilP5iwgkiTmqGj0XWW9fY0dra0PV5ubCVUC50IX7Zv00K09vDquIdU5ZUSZ-FHhwptO8bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
سال‌ها همراهی، سال‌ها صبر، و سرانجام شهادت
💫
⚡️
در پنجاهمین  قرار با خانواده‌های آسمانی، میهمان جانباز شهید مهدی سورچی بودیم.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/690453" target="_blank">📅 21:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690452">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
هیئت اعزامی دفتر حضرت آیت‌الله سیستانی در سفر به ایران، از اختصاص و توزیع ۱۱ میلیون دلار کمک مالی میان ۳۶۰۰ خانواده آسیب‌دیده از «جنگ رمضان» خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/690452" target="_blank">📅 21:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690451">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
معاون رئیس‌جمهور: لایحه حجاب، همه نظامات کشور را بهم می‌ریخت/ باید کاری کنیم که باحجاب و بی‌حجاب، برادر و خواهر هم بمانند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/690451" target="_blank">📅 21:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690450">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJxX2IBowRKw11pXnyaP1jgm2w2mt1Ic92FicLUTdHiFUkHP22IPq20f6Lx9KCm9wzPp1aCQ-XDRlP-hGa-uXFTZ6eWnXPR6ExKd37-ScP0KpXWc4wf6AC_cB1vTjlQfLbRF9YkfM-FLC6zSg2W2XoVrbi6IVGUcvFMPSNkgcWfxMwS4qxyJrEkiotLU0fRm8ChdXoYFz0fserh5gIFG3V6fHqd3DQKZKgKI_S_jZ6rTshtiJVjvos_Fg_EpUCyD3X_sOga5YrbM-1vBTdnBTp-3kd1yg2cjyG5CGqg1lkLJ93viaR6ReiZAYiiE59RomSvmMQQ5K-rWX10fXBWn4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار فعال سیاسی ژئوپلیتیکی: جهان فکر می‌کرد ایران در عرض چند روز سقوط خواهد کرد، حالا ۲۰۰ روز است که استوار ایستاده است. دعا می‌کنم برای پایان این جنگ علیه ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/690450" target="_blank">📅 21:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690449">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
گچ شرق؛ ایستادگی پای تولید برای مردم و ایران
امید یعقوبی؛ مدیرعامل کارخانه گچ ماشینی شرق و دبیر انجمن گچ استان خراسان:
🔹
با وجود شرایط دشوار روزهای جنگ، کارخانه گچ شرق با تلاش و حضور مضاعف کارکنان، بدون توقف به تولید ادامه داد که این تداوم تولید و حفظ نیروی انسانی در چنین شرایطی، گچ ماشینی شرق را به یکی از نمونه‌های قابل‌توجه در مسیر پایداری تولید و مایه افتخار صنعت کشور تبدیل کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/690449" target="_blank">📅 21:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690446">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K-bHxN1jPEUe-zoSY96lxLLHYRAlRcPc98Qe_LdJSIl1oU5w-GiJKYe1UXA9qzoP5R8O_nhpszbdaXqcrWf3rne1msXAub1m0c0qWJw-dwXzQgTJpHj4kIeA6CO1VZUZzl0GkWw78OGcg_8klBSRoNkr0iMz7eb5T9G9W1Mrp1egimG7sQsd-h15Ehumn6d3OciiUdwdjZ5K44i2y9YxUVLg9J0ivaXfSCQyJrczYuIMgJUvy-e6gwsDwxZ4nHVZudcqdz1dDzHOreZC_-fDI_ZloNh4k_zBTDq4Pud6xZVLBYhzj_-xbW2FNw0t9xmMpH4yt9Xt_wYqh4XiYO3XZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vu-KDTwibkhJqkWc3aK8WdartsAhoym_w_yEWte00ozOsscXs-oDYWxK9_AKnlHoaLCOccUxYU1V_XPyUQMxQuK426f2ESLrq_6Om0qcPviiw1cCuQu_EHHjZ62Sh0LmOYOcOOuOrsfeS7mXkcwWPtX2v3ExSEu0dwXKiVKJELKRqffp-f9NWoNlBUPzp-K-kyalYwVOvyHv2GHd3Dk9UJs_sRGi9WqZCMXGTq2IAmVckI6hr9GLMXyxwiczuuODFdJeu_Q6T0nN0xv9G59QjEe60ALtXxoxRR_8RG-oAlVq3eodiJVErpShDQknfYTsrgCi4QArRRw221_iAuUMrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-6CPZRLdohlIK4x7IzGIhsbsFRny1imMcZuMt-b7YBe0DWkC9pb3ZlGBhk2Ey5_LEZ2lFZlEB0Gy1YRLciL18nBbukFM5-WADFGgNPGtPv2cTnRgsXrsBWEbOFMiItvXv6deRr9uu12i4rZOVyjsM_IsLJMVUudlJCHUaHKWX_BkfpJM2kJzRSZrEI5A4a0vouTNWda8eCuZEh6r4QV--wrBCl3_LNHtH6o7KOKIjvfvh7b2sX1uRNA4VzVmrrVPskE7W0EuuSJAC0du2UyJ8RnnW_I1ltdUAmAyQCBwCLcm0SCysbw-BKdm5Z0i-e_4q3CM0XxGLFC7NsOsJ5_9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگه باید تا آخر ماه پروپوزالت رو تحویل بدی، این ابزارهای هوش مصنوعی رو از دست نده/ مخصوص دانشجوهایی که هنوز با پایان‌نامه درگیرن
📖
#هوش_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/690446" target="_blank">📅 21:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690445">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
تصاویری کامل از لحظه رهگیری و سقوط جنگنده عربستانی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/690445" target="_blank">📅 20:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690443">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pDqO83M383qCHkTVP14m2fdJ-No4CuhjcFyD700B7_X5OKw6f5Mo1RPQVOtCB9ufZz3hSc7W3ikvxWx0Vj6zaj0ZHcoRzufdgblY4hiFp-me2E3hWAXMLVzdgkDOiOCrMOGgM56dRNLbxioUJtmsBOhauCqCs25YrQ9OCi6NrMy5G05sfVlHLDFz16nOSvBk5o56ZKIqpS67km-KQyUhZbuatKkzkho9gZoACunfqiCF6YQLyOralTeuSdLOs04zp-nE_Xo4cjjFmP2LGqm-SXMAQj18p9CaYsCyn_UPhm4sBAXWSA-tonYepFuifX_pKO1YKXszxQs6ZljleQedeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rgnDV0o8VvZ0lxjX8RDYzjgqWPP1BLai6-LAxmNDYgWLwaMpSfMD_S1M0zYRJMp4yyS7kPe0Xu0RqnuT3oqWGb7OOyz7FFf5Y791zfjY_FXqRqQSaoqZvDNY1DlyAzSwN__u2EbZho37bEUy2ce79qfkPZHvAx2IHYKtHdcmOdVA6Db89ad5wdbvdY3bqZR5mEb8LC9DlTtRqLAV3YD8CMcNArSwePf3Vzp3Kruhs1XKqSUa0H0M48moun-4QMzf0RLxkQrmk0Phzf-UrI4moUep7xL195VM13p53-QYQjHsLkkfcmHP5h473s3q0zLz7dsIm9mEutCviZnqvKBvfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نام چهار تراستی بزرگ ایران منتشر شد
🔹
حسین شمخانی
🔹
روح‌الله رضوی
🔹
علی بایندریان
🔹
محمدهادی مؤمنین/همشهری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/690443" target="_blank">📅 20:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690442">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/528eb714d0.mp4?token=N7hBOgVcX73sdlu-PgMWONspmj8sTTr9VS-Kzm3S5UP4L2Nek-VKBIAlaV7sFwX8mdtNMSFwk4BiGfPBZ_kvPsSHWe9ok42YXlWkPjzsmSKLzRUccm0NuoRf9uv17OWceCQO3Jr0I-E9XcgHBak_J4i1iaRLyycqTHz93WvYDyIVwr00Nhe-uO_GyUdCuiytTKDhwp5jzoc_FS9fO5WpjydsaB9fBPlo0tw_3EaCWzAhwL8a0yc-qutKonQvHawZn7BIbRGD41KtGyBn3o_kP_j-wyRQSPAufQnkAd8Q9XsqQzcCOh5BwRUh4at20vRsQedzPm_Wl5GQqQhxGstvAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/528eb714d0.mp4?token=N7hBOgVcX73sdlu-PgMWONspmj8sTTr9VS-Kzm3S5UP4L2Nek-VKBIAlaV7sFwX8mdtNMSFwk4BiGfPBZ_kvPsSHWe9ok42YXlWkPjzsmSKLzRUccm0NuoRf9uv17OWceCQO3Jr0I-E9XcgHBak_J4i1iaRLyycqTHz93WvYDyIVwr00Nhe-uO_GyUdCuiytTKDhwp5jzoc_FS9fO5WpjydsaB9fBPlo0tw_3EaCWzAhwL8a0yc-qutKonQvHawZn7BIbRGD41KtGyBn3o_kP_j-wyRQSPAufQnkAd8Q9XsqQzcCOh5BwRUh4at20vRsQedzPm_Wl5GQqQhxGstvAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زارع، سخنگوی ستاد مردمی «جان‌فدای ایران»: بعید می‌دانم حتی سازمان‌های امنیتی در جنگ‌ها این‌قدر مورد حمله سایبری قرار بگیرند که به حمدالله هیچ‌کدام از این حملات هم به نتیجه نرسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/690442" target="_blank">📅 20:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690441">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4246385ee0.mp4?token=R-KysYCgMEgiVMNx6oKy1Sin4vtqOUpStdQX7L0BoQpBp8hCaaWfMfhD4ayyzbWiLuc9QMROIIA0gz-UcEW28RIaIshxJkG3EeJBmSLxlzxKpNL1IzuClTQnZQowDf3MNNxJAgODzusmoNYcJrJB4iTBeR7GTGeRJhFPrM1ED4ZeC4g5oUsKxJKrBz1FRb6Xfy2ImhFq8r_mrBGKqdTb8nWNO_taxawWr7wqWnHtiUPHTPABN2M6YxgUR-F2zrdNHp1xSI6IIrhySd5pkuE-fQYakAWTMBw8q78fmP9L9DrHr_eAMzDpqX1MzKl_C6AWXFTHJ3eCHYeTEJmkXhUvaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4246385ee0.mp4?token=R-KysYCgMEgiVMNx6oKy1Sin4vtqOUpStdQX7L0BoQpBp8hCaaWfMfhD4ayyzbWiLuc9QMROIIA0gz-UcEW28RIaIshxJkG3EeJBmSLxlzxKpNL1IzuClTQnZQowDf3MNNxJAgODzusmoNYcJrJB4iTBeR7GTGeRJhFPrM1ED4ZeC4g5oUsKxJKrBz1FRb6Xfy2ImhFq8r_mrBGKqdTb8nWNO_taxawWr7wqWnHtiUPHTPABN2M6YxgUR-F2zrdNHp1xSI6IIrhySd5pkuE-fQYakAWTMBw8q78fmP9L9DrHr_eAMzDpqX1MzKl_C6AWXFTHJ3eCHYeTEJmkXhUvaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون رئیس‌جمهور: لایحه حجاب، همه نظامات کشور را بهم می‌ریخت/ باید کاری کنیم که باحجاب و بی‌حجاب، برادر و خواهر هم بمانند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/690441" target="_blank">📅 20:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690435">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dPS3HyAUdUzDfgMqHFr0rRkPa4HweA2HdMEJmHvwqNH4VWW6UzHoiziIfraJQLYAayZqAbkN15bDhvZeQ-VbwE7FlnHsoLyHb4CQIF0rAhAjkwLOeHgsbdnIC-bFNo3KQtERv9IK-73O--xQHHkX9VbqWGbbJiTlTsfoaMeydYuDAQ7unTd_V45jB_DzGSwGqo7ps2krKi7oX2-ue74V7s4thX5YzpYI5XxCnXJIbewxBXUcNMmkhXdqe6ZEX4EuvOsi0mztWNmhR57YJDp4rwv_-kec4CpiBKQoIeRxJTMFaJe1GwaiOn5ZziwqM8s4PtRI7Ff1YgfxvqH12wwW-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJP7xE-NMDt850Pft7qByqv1xK0xy_vPatCXp3IU1Uer4TFyJYB8KKmXsv8K7xCVCVssSgaKM1apdcGwWoxrP-IQEfitGfzbYes1V-OpLbGpKymXzPcCxVPx9s9UrTRosd9JupKj5SDhhH7V21qVmSTZNBZmrHw2B0hc4snNefSezQbtAQghq5VNii8kHdCkbmx2bhJ5KZMPUYgUXpcKvdNWVXia1P6eEyWIMWkweUtCPFDh-_kNYWZD-N6E4CzuYh515pt51vdSgvzWJbiCPyyv2Au8kNluVOuvtrGefurpHsp45toTvLoJ_Q4xdItDNczjEG7xnH883a30aW-qwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qHxpwJ7QRFyejWLaldwPJ4z2ZOVaHNBCA92s7Q7We12pnBo84pJuoXwmIxOf3kG4C9rSfd7SxwiP0wpEAsCrPMehzCeMdahBgPNe53ystDY9RKRC1twAmkzb6h-QJnNHGw_8JYFXixT-Gle3Q9EtdeOBXMuMCflCafoQKXhcp56sM4W4JLtCgZ4G24X-G57FgShrFfP6vbpIe_lsmOGLub6wKwtkGmQv7XEUKQWFVtFW6Ax-9w0pRdyYZnUPD3Lo5QcWrEbN74tsYZ-BzwQTSIF2e_qBJLIOGcDCucDgEBwVWQzflikHEAv-QU4ubfYZa3qEm5p_sAunWePS9wQ0lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HD1zHZZok1LnPbAl5FGwJXNrWzbfPz0KxuSg0_RunfRMIp7Bc9-N29NJ4josBoyJGlomICmxXwVBOH3Z4KrNkOTjLOVtLRyGGmYZIT4-YzAZTd6uKRca-UkkP1eytZVlYzrsV_-H3IW0DQxyeb4WF8hK4AtLETeEtL1jPgVYSojzfrCWPELm8jYuW7Ig7CV8VMM4pw1Nu8XWbV5rsrtTih_uK6Lsm0kf2bb8ZPk6jt4rkJiEQIN7fXtmQ6ilmPYpvnIwFFxd3lrHjw-zol4Gr_J1a7oxyXX4LjyN9i9XWdPHd6AWUY1ENiWLW1RyBnVS4spBzaP-CuDcbyBP4kAVbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SnLVqka1E09-nVZIcGEnhna8C2zXV0V8Q34SEZMNWlEqs2aZCBLpwNoRMg73Xc7uWIgEZO-94_Dr1H_PqIb9AraV3tuIxVpyhM2u3Czq8POK8FEwcXftQYDCHjjVUzme8Qitm53FpYjjPE7mgBnyLtrffLlbWIFYYKOCjSxgPJOm6tDOekCQAv-NwhU0xulT4WjYVhCs_PQe9C8w0C4lsjU_q8pgNh-OHpWHdC4nqEzVEiW-JHU-PDX8fnjxfT-SkUgXKDI8P1NPI40anG7f7ZwtFcEkIHHdRy4XxMvTVoXb4cdfcoLqS_POn6cITsUhFCOaz5Lbe4VHBapKKYMBAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gwZUONOWulAnhj4cT-O5fG7czdHCnWTyQ-brTL1CDLsZqBA9pKmeHlv442ojiRhHGrUZbW5JWv1erHRIU3r2MVK8JiLE1nq8YCC_UO74UpQ6xN9_5wCixbN3uhJvEKtSt7ORdPuBGeZj18Xq91YgoeN2kwnc-X24ZuhdXmqD1Kn8z2ugaywwaNDI8VKBAGeSl2A0gA8cX_TjbM4YWP49Sp4dhXsWLOs2BmnNwZY6SLfKv2EBNef6BbAxeVu7ceoG9zS1iF3viN2xp0s3pEksl0-wFS6f2o0eIP0CgyURaZYuCN3I5_LDwiNjA93q2weO8VgmUn0924739IwPf808Ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
وقتی رسانه‌های انگلیسی از حمله‌ها می‌نویسند؛ روایت جنگ از نگاه دیگران
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/690435" target="_blank">📅 20:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690434">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8da786da29.mp4?token=YV02ZE4-pbLkA7wE2mEgMh5mY96V_WtSzMkgcjjKN9WLkwAHKtdQwKEFNZgkE87nDsQKTeMrq8g3x00hgLMauIF9fIvLVId1V9NFLh9pj3sjcyzhUPH4q-N7FgbaVWji2OoPTvsSqK2u8zK7-pcqUroaAsBI_N_l7Ow_GVoXESekZPIN5dWd4Cl39nu111V7umKEWQ1VZMbiCQfwaw4yLLNs8atVNNWqJKTxA-cMfX8mFgV4EkYBPOZct6N5dmCvy9Z8jNRhMiPdukosanB0v1EbzmLB1Uv8iU4ZZb9XIZKtczFqrcWao0pgieWeuVU0ZGv04Nve2h5NHhPgE0h4fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8da786da29.mp4?token=YV02ZE4-pbLkA7wE2mEgMh5mY96V_WtSzMkgcjjKN9WLkwAHKtdQwKEFNZgkE87nDsQKTeMrq8g3x00hgLMauIF9fIvLVId1V9NFLh9pj3sjcyzhUPH4q-N7FgbaVWji2OoPTvsSqK2u8zK7-pcqUroaAsBI_N_l7Ow_GVoXESekZPIN5dWd4Cl39nu111V7umKEWQ1VZMbiCQfwaw4yLLNs8atVNNWqJKTxA-cMfX8mFgV4EkYBPOZct6N5dmCvy9Z8jNRhMiPdukosanB0v1EbzmLB1Uv8iU4ZZb9XIZKtczFqrcWao0pgieWeuVU0ZGv04Nve2h5NHhPgE0h4fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درآمد گران‌کردن بنزین، معادل فقط ۱ ساعت یارانه پرداختی دولت!/ تلویزیون اینترنتی‌مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/690434" target="_blank">📅 20:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690433">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
قالیباف: ببینم فدرال رزرو با بالا بردن نرخ بهره می‌تواند تنگه هرمز را باز کند یا یک بشکه نفت بیشتر تولید کند؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/690433" target="_blank">📅 20:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690432">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
جانشین رئیس سازمان نظام وظیفه: بیرانوند از یکم مهر باید در اختیار یکی از تیم‌های نظامی قرار بگیرد؛ البته پرونده ایشان در حال رسیدگی است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/690432" target="_blank">📅 20:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690431">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpoeDsVs18MYto4jVKJ8D18pmJ2CvEpUyCzXuGq4DptA2SDBufC_0k6KEBamsYkCAsSAfwp-KPvc9xyZUHiA-M57R1bOYNFQiTb1nfJsrNGD6XZoTLq3ho0Z8Qk0ktZU_giKdXvBX_OBLdliLrq1mFLhn3BoBA38uzHiq2w1dRxvI1CNkxjG2oqjuuQtnlVBXyAfN5Euo3oe7DFSwZ6Jp5KC_omiqNPH81gVRuw9G1Dt7N2MRxY3zOFf8cPa4-xmcu6HPlnuiYTsqImF8CeUI7UjRRDLnDBp1kPjkIM1J0zh-VpteVwKmnv0wIOszBcJPV2EIwEM0Jo4LipKGMC3BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت گازوئیل در آلمان به ۲.۸۰ یورو در هر لیتر رسید
🔹
با احتساب هر لیتر ۶۴۴ هزار تومان، پر کردن یک باک ۶۰ لیتری حدود
۳۸ میلیون‌ تومان
در آلمان هزینه دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/690431" target="_blank">📅 20:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690430">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9DwgU042tw1bQ_lIStAn15OLGLG7HCNUo5I9wBn_EKlXDSCoUAP9Wa3LEe5K1eykbYXAst0sNXPC9iGLGiOrKMVcOQncByZ7Utq40PuT_KBSm6yDwA8kcjWK21N4SQqlr4Je_flwnNBhXWVksOzj4ccZkItZAPojingnjZcdEPfs6RUKkmuh8NHNdfphyrCrKWpsMyY0oPjxgvPUAZbZkX8J1F3fsPdEBBxyQAEkZAvL4YrvFP1yCt5CEBy5PltYMdRpjRUrjujSup0WWZHKwpvpHElbRTQ2BKyn5cpPUE4aACT6AaR5ocLE3aQhtMYnqnqkF4FTmtkFP6prh2Idw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی نیروهای مسلح یمن: تأسیسات آرامکو در ینبع و پایگاه خمیس‌مشیط را هدف حمله قرار دادیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/690430" target="_blank">📅 20:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690429">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/610438ef31.mp4?token=sod0Yix7DyiQlDJcrLGHsXaxv5LaPhzADNq6W9kMT1Gjfimy-16blmUYyZZP43UX_5-zpc93DTL2XbULPH9u9R_QbIBT9V6jTNo2DJFn2DcJa8kfOBRA53zJwcgYmZ9oqFylidqjOGY52AzmPqJRyLTEnaJAjjOl2iHBXraEb5kdG4V8L9iLncdHzNhyfws7PAO94HWuUFVetJ9TCfM6JxvrxXVyHg1vR9LYQygt3CjDh7X-AOnqhvTGkzDS178dqxSbnWj5gQLe0dj9E2REYtZJaZ3ijO5SOsseRG98OVnpMy9pDZ4GogJLdnD9yzHhpIZmHRJzYHyZ5Uq22sMEAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/610438ef31.mp4?token=sod0Yix7DyiQlDJcrLGHsXaxv5LaPhzADNq6W9kMT1Gjfimy-16blmUYyZZP43UX_5-zpc93DTL2XbULPH9u9R_QbIBT9V6jTNo2DJFn2DcJa8kfOBRA53zJwcgYmZ9oqFylidqjOGY52AzmPqJRyLTEnaJAjjOl2iHBXraEb5kdG4V8L9iLncdHzNhyfws7PAO94HWuUFVetJ9TCfM6JxvrxXVyHg1vR9LYQygt3CjDh7X-AOnqhvTGkzDS178dqxSbnWj5gQLe0dj9E2REYtZJaZ3ijO5SOsseRG98OVnpMy9pDZ4GogJLdnD9yzHhpIZmHRJzYHyZ5Uq22sMEAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف
سفیر اسرائیل: به دنبال فراهم کردن آشوب مسلحانه در ایرانیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/690429" target="_blank">📅 20:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690428">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUQJas1rq_87vBsvLguLoOP4fu8uzDQpXaoLVoMJgI33fi_uAO6-qT5KHRzllIf_eM2DL3VGX0V65JrXIUOpeTzU2A2TELGVu7O4s4qKL241enT0dY3-aMO47GPKNA_GFtWRu1bGTgT9xzB43f1Kc_TZ3XrwhIp7oiuLWJDJjM7IcS7_DbzK1F3w5W7rLqJ3Fi9KtJ9XGzCyt6j4bens60dHMEkT_MNw2-pcNS4zjuR8t7hGS_APzbSqZims-6vRGI4VpiJfvu9w91GEPzYcs_Ee_Y33CygkDvGZmvdVpwQO29arPF5xEn3D6P4o87KUFMqJxfYq_tGdVCk5oLnRzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز پذیره نویسی نخستین صندوق ارزی كشور از سوی بانك ملت و با حضور وزیر اقتصاد
🔹
آیین آغاز پذیره نویسی نخستین صندوق سرمایه گذاری ارزی کشور با حضور سیدعلی مدنی زاده وزیر امور اقتصادی و دارایی، فرشید فرخ نژاد مدیرعامل بانک ملت و حجت الله صیدی رییس سازمان بورس و اوراق بهادار برگزار شد و بدین ترتیب صندوق ارزی "مانا ملت" با هدف فراهم کردن بستری شفاف، امن و قابل اعتماد برای سرمایه گذاری دارندگان ارز و تبدیل منابع ارزی راکد به منابع مولد و درآمدزا، وارد چرخه اقتصادی کشور شد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/690428" target="_blank">📅 20:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690427">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
رویترز: هزینه جنگ ایران برای آمریکا به ۳۸ میلیارد دلار رسید؛ پیش‌بینی افزایش ۳ میلیارد دلاری در هر ماه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/690427" target="_blank">📅 20:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690426">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtg1rfgRJXAhz86ToRX-kgVc38XCat2grAjWtSSBcASc2v7Qk5revl8wxT1s0AB5NJCFP_TsYzwKz2R80CdZZEuekagPTJ0zQRYB6EzdGSKm1RlwQEdEQbHdw3ko4unNYVGx0jXHDEo0r79FGLy_VEVeLrHuOfXQ1i-gIli3wbfJ0RuZuIUr0AdS0J4_eqtJpKF7pIUpC7viwi59GBu5ShJlSX02Ht-uW38vnONe4skzkRTnwldL0oHQ7m5XEYRlXRBk6HrljxESgPKp-Tq3YgY4FPuYg5EeAIe7UvrBc9D8s11RxfhaiPZzrpmsmiKJRkJQP2P--0z4Of9q4cXOuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترفندهایی که ممکنه به درد خیلی‌ها بخوره #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/690426" target="_blank">📅 20:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690425">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
کاتز، وزیر جنگ اسرائیل مدعی شد: ارتش اسرائیل آماده است تا به محض صدور دستور، حماس را نابود کرده و کار را یکسره کند، تا بتوانیم طرح کوچ [ساکنان] را نیز اجرا کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/690425" target="_blank">📅 20:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690423">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBhnEruzPkSwA_24RSBchM8cfo4w_T5S52nyHh90bVyF_qh3U2acftfBpNN1HazrWm-2rrqdL9VwT0DKPdVzPE4Rd3ObwgFZ6hyDO2P_8V5lUt-oujTZzIYGFb5rJXUSU3NuuNHvwIsG05CT-Ma9uZuU-yKysEHCuKtqGKtqSMl1EoUI6N4Goss_Cdu6ASmONJs30ndMuINSF5Og6jf9sZ2w4DWim0oZnmGmw2iCnBpKkrC6k1Y7ylDvKVvEKLMUOnsjrcyuh6HMHc0-aurQTWWvqn8O2huqevmbL_PLw0jO3jl-UWOnVkK-Nn3Tt621kZ94-Q922_AzOSa60A_oRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لاشه جنگنده شکار شده توسط یمن، از نوع F-۱۵SA است که جزو پیشرفته‌ترین و مدرن‌ترین جنگنده‌های عملیاتی نیروی هوایی عربستان محسوب می‌شود. ارزش تقریبی این جنگنده مدرن بیش از ۱۱۰ میلیون دلار برآورد می‌شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/690423" target="_blank">📅 19:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690422">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/131e70f8fc.mp4?token=SY1vNU3pT5-bjwK_YdK9ZNnyGvQUpv5ObeOLWlQk_CHTsSg3AwTopyQiU-ZV-GxR0JExlZOHnRwdUVXbhNRFOKJc4wbsqj1N6Vvl1LoPOYVkzxhL09O1ONcdzFjRHDX8x5OH3wdwxfqc28lqj8oTxdUwZ4EHYjAqkMLc7eQib9T8dN3YeDWeaVGxvLYcvHok28UlAjTaZ-QHtfd9e3hXxddLvjrLJ4cGWWhmjIVj8w9DHl62g58xQZ10hXVukj6CLUt6L8GIlCi8vKa7pW8xd9FueUz18pk_NKVpI-5ldFntPlan3QB0oKKHab5cdiYelSg0WofoiO-zIwH8yyElPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/131e70f8fc.mp4?token=SY1vNU3pT5-bjwK_YdK9ZNnyGvQUpv5ObeOLWlQk_CHTsSg3AwTopyQiU-ZV-GxR0JExlZOHnRwdUVXbhNRFOKJc4wbsqj1N6Vvl1LoPOYVkzxhL09O1ONcdzFjRHDX8x5OH3wdwxfqc28lqj8oTxdUwZ4EHYjAqkMLc7eQib9T8dN3YeDWeaVGxvLYcvHok28UlAjTaZ-QHtfd9e3hXxddLvjrLJ4cGWWhmjIVj8w9DHl62g58xQZ10hXVukj6CLUt6L8GIlCi8vKa7pW8xd9FueUz18pk_NKVpI-5ldFntPlan3QB0oKKHab5cdiYelSg0WofoiO-zIwH8yyElPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زارع، سخنگوی ستاد مردمی «جان‌فدای ایران»: آموزش نظامی برای آقایان و بانوان پیش‌بینی شده و ظرفیت اولیه ۱۰۰۰ گردان، در کمتر از ۱۰۰ دقیقه پس از آغاز ثبت‌نام تکمیل شد. ثبت‌نام‌های بعدی در فهرست انتظار قرار گرفتند تا در صورت ایجاد ظرفیت جدید، اطلاع‌رسانی شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/690422" target="_blank">📅 19:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690421">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea211cc01.mp4?token=jhAo2JZc-ETVNrLI2XTKfNH-crPvTnB8GK2XRfjpzJAIXjW_44SiwewV93uDJ53zndjt5p6uminz6A1UIv9s905Yeu1cRQ9E4xy9Db6E7Ux2dvRv5QlR3RlqrV6PXtQ1DgBplpLrPOzFlEwsQ-3gT4t6y8f_W_3nPDuFcQy8lBEKlrC4HX2CTd0Z9nBC-XBLxFpk9rV2zydKqemMuq_Rwo47DaaMumQdPEkJX1b2M5W5AI-kiiKYPCwaFoKbhVncwZUamobmfBL4OwMmCcSZqdZ3Ig3rM2JUuBqrQziNaL43-UJ35pfHBMcJ_9JDoRbl-_-HXHkxLmIe0iqgtPk7mCI7Aro9VlT6Si8CVfBfa4sOklKmOysHja0zofaZbDaDX7ph9LuxPyaoZQzzzJ0HmerpPAvY_OE06ZKmsLYy_boaH54DoGTC3-PKPevKxf5ZHS1O24s3mm0uk1vF-JLy6AIND1Bx0JrRzhEwy5kJKqTeyIU_j_jBZ_yS3lQziRuQ2tEearVupXjmW8R88seH2rggkuhVYFzzHExYJtNAHVhtAN7TXVdthJwOB_YIuwlhN39sxES7HraDi6tRMdV7yujX4VyAkX1MqZ0O5CKgn2owa5Y4OGWFp_onFNySqOmqu5sImhN1M0TftktLonVUOewjKdK6jpUVSR5ZQ7rRxJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea211cc01.mp4?token=jhAo2JZc-ETVNrLI2XTKfNH-crPvTnB8GK2XRfjpzJAIXjW_44SiwewV93uDJ53zndjt5p6uminz6A1UIv9s905Yeu1cRQ9E4xy9Db6E7Ux2dvRv5QlR3RlqrV6PXtQ1DgBplpLrPOzFlEwsQ-3gT4t6y8f_W_3nPDuFcQy8lBEKlrC4HX2CTd0Z9nBC-XBLxFpk9rV2zydKqemMuq_Rwo47DaaMumQdPEkJX1b2M5W5AI-kiiKYPCwaFoKbhVncwZUamobmfBL4OwMmCcSZqdZ3Ig3rM2JUuBqrQziNaL43-UJ35pfHBMcJ_9JDoRbl-_-HXHkxLmIe0iqgtPk7mCI7Aro9VlT6Si8CVfBfa4sOklKmOysHja0zofaZbDaDX7ph9LuxPyaoZQzzzJ0HmerpPAvY_OE06ZKmsLYy_boaH54DoGTC3-PKPevKxf5ZHS1O24s3mm0uk1vF-JLy6AIND1Bx0JrRzhEwy5kJKqTeyIU_j_jBZ_yS3lQziRuQ2tEearVupXjmW8R88seH2rggkuhVYFzzHExYJtNAHVhtAN7TXVdthJwOB_YIuwlhN39sxES7HraDi6tRMdV7yujX4VyAkX1MqZ0O5CKgn2owa5Y4OGWFp_onFNySqOmqu5sImhN1M0TftktLonVUOewjKdK6jpUVSR5ZQ7rRxJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آمارهای توهمی دولت ترامپ درباره تنگه هرمز ادامه دارد
🔹
وزیر انرژی آمریکا امروز چهارشنبه مدعی شد که روز گذشته ۱۸ میلیون بشکه نفت از تنگه هرمز عبور کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/690421" target="_blank">📅 19:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690419">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
اظهارات جانب‌دارانه گوترش، دبیرکل سازمان ملل: ما حملات انصارالله به عربستان و بستن تنگه باب‌المندب را مغایر قوانین بین‌المللی می‌دانیم و محکوم می‌کنیم!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/690419" target="_blank">📅 19:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690417">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZ-iocmpcgLqHSpU3X2PFUVRp1fDWaVpFQn9WVH5LvJXBhegjZ8OE9NCVxW6ST4SEjSc2mFIrE3FhCcmJV6tbMP3Ieczw1r0xemP4L9zljtoDh-x3bEZanS82Imx1n2WnSWuOTyWDTRW91daQbN-NJhqyNAuI2_aTTW7ejZC1gsVFfaG7EAxSCui0vaE0qcR8WLg8ewY_S_UDVaJFZ_aBKpJmdYOv3-aq76Jd9mAjhP9iJBb5A3Bvr728w_XHmHiqtc7gbAwHe_k56zcrGyQos0g1VWMofkPsjU_oLysbWKzrjZMpoELHSVSISdIZP0ssN8Dag2YqTMd2e9uRIbRqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی سپاه: آمریکا به ویرایش تصاویر و ساختن روایت‌هایی به سبک هالیوود عادت دارد
سردار محبی:
🔹
بد نیست نگاهی هم به لاشۀ آن جنگندۀ اف ۱۵ که در ایران هدف قرار گرفته بود بیندازیم که قطعات آن با فرغون جمع‌آوری شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/690417" target="_blank">📅 19:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690416">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5afd9da57c.mp4?token=E7R5IwzUK-l_ngMgY1zplCd8yFCPBTavRQWdpfGeM0St-1k0guDVbaccx3J2KuE2n8JtkpSZt24rggNGtuROaobHZkAbMroH_6_ise4tfbWZwneR7Utw0LGJtzJFFIZaYRkk42g5N3HZUTlA0z7K3G_AWd1Xu0-NLOCyC95zaTzAugD_R5laTwnSrsLxgcoQl06ACtLraatc7HWoC86DJ0-qeNFGYZaIqexzkvh-eur-THE70qOMcdQSn35gFD9lofx-fz7spsaEc7EXLJy3kUJgIMLh6sGC5JZqzUhyMdw5S4xhg0wT4igaHyTQvHegtppKWupU8uN-SJEQK2VoSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5afd9da57c.mp4?token=E7R5IwzUK-l_ngMgY1zplCd8yFCPBTavRQWdpfGeM0St-1k0guDVbaccx3J2KuE2n8JtkpSZt24rggNGtuROaobHZkAbMroH_6_ise4tfbWZwneR7Utw0LGJtzJFFIZaYRkk42g5N3HZUTlA0z7K3G_AWd1Xu0-NLOCyC95zaTzAugD_R5laTwnSrsLxgcoQl06ACtLraatc7HWoC86DJ0-qeNFGYZaIqexzkvh-eur-THE70qOMcdQSn35gFD9lofx-fz7spsaEc7EXLJy3kUJgIMLh6sGC5JZqzUhyMdw5S4xhg0wT4igaHyTQvHegtppKWupU8uN-SJEQK2VoSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پوشش زنده حادثه، خودش به حادثه تبدیل شد!/ بالگرد شبکه NBC هنگام پوشش حادثه اتوبوس در لس‌آنجلس سقوط کرد و ۳ نفر را کشت؛ در حادثه اصلی اتوبوس هم ۲ نفر جان باخته بودند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/690416" target="_blank">📅 19:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690415">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه صنایع پتروشیمی خلیج فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qr42Jn5NQGEbvQ5GPOPj9bKNpCsL6OSU1ySQTzc-OOdekXcNgo5YiiMZzuGjfXs9OP6yvxSJ2I8pLYkD2B3a5ChrL9RCo9JDx36EvUWS2giJ8p-YTdmD3feyjT7Hr0gBbc4cg43kc8Y811ASbARzavLhOLpOhCJ9eM2pS02KAL82S9TO_hVQTJX4flxnEBsK372ULJFIRIeAmjfSPsm9s44SRphwQz-R9Vx9xtLn2BKSJLsU36Cn0kFiCXNhvHN7ETueJK7paeVIa8ZtolXhhs9AvbF7S-p7kJX-E0M7A6tz02WjFZpE7szTutBdCb2o0o-Ui4RoE1_yYWiBqcqTYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش مجمع سالیانه شرکت صنایع پتروشیمی خلیج‌فارس؛
راهبرد جدید هلدینگ خلیج‌فارس پس از جنگ/ رکورد تولید باوجود جنگ/رشد سود خالص شرکت صنایع ونروشیمی‌خلیج‌فارس به ۱۸۷ همت/ فارس ۶۰ تومان سود تقسیم کرد
🔸
شریعتمداری، مدیرعامل گروه صنایع پتروشیمی خلیج فارس:
🔹
۱۹ پروژه با ظرفیت اسمی مجموع ۹.۲ میلیون تن در سبد سرمایه‌گذاری هلدینگ قرار دارد که مجموع سرمایه‌گذاری موردنیاز آن‌ها ۸.۸ میلیارد یورو و ۴۴۰ همت برآورد شده است.
🔹
طرح‌های فاقد اولویت متوقف یا از برنامه اجرایی خارج می‌شوند تا بودجه و منابع در اختیار پروژه‌هایی قرار گیرد که اولویت بالاتری دارند.
🔹
افزایش بهره‌وری و استفاده کامل‌تر از ظرفیت کارخانه‌های موجود یکی از محورهای توسعه هلدینگ است.
🔹
افزایش سرمایه ۷۵ همتی هلدینگ در آینده نزدیک انجام می‌شود.
🔹
طرح‌های توسعه هلدینگ تاکنون عمدتاً از محل منابع داخلی و سود انباشته تأمین مالی شده و افزایش سرمایه از محل آورده نقدی سهامداران، به‌ویژه سهامداران عدالت، مطالبه نشده است.
🔹
سود خالص تلفیقی هلدینگ با رشد ۱۱ درصدی از ۱۵۷ همت به ۱۷۵ همت رسیده است.
🔹
سود خالص شرکت اصلی نیز از ۱۲۷ همت به ۱۸۷ همت افزایش یافت.
🔹
باوجود جنگ و از دست رفتن۸۵۰ هزار تن محصول، موفق به تولید ۲۷.۳میلیون تن محصول شدیم که نسبت به سال قبل افزایش داشت و رکورد جدید تولید است.
🔹
هلدینگ امکان تولید یک میلیون و ۵۰۰ هزار تن بیشتر را نیز داشت، اما تولید این میزان محصول از نظر اقتصادی حدود ۹۰ همت زیان به مجموعه تحمیل می‌کرد.
🔹
فارس در مجموع ۷۹ درصد ظرفیت اسمی و ۹۱ درصد برنامه تولید خود را محقق کرده است.
🔹
جنگ ۱۲روزه و ۴۰ روزه نشانه‌ای از ضرورت افزایش تاب‌آوری هلدینگ بود و گروه صنایع پتروشیمی خلیج فارس در حال کاهش وابستگی به واحدهای تک‌محصولی و متنوع‌کردن منابع تولید و درآمد است.
🔹
مسیرهای صادرات زمینی برای فروش محصولات به پنج کشور همسایه و انتقال کالا از خاک کشورهای مجاور نیز گسترش خواهد یافت.
🔹
ارزش ساخت داخل در سال ۱۴۰۴ حدود ۹ همت بوده و پیش‌بینی شده این رقم به ۱۱ همت افزایش یابد.
🔗
متن کامل را
اینجا
بخوانید
🌐
@PGPIC1</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/690415" target="_blank">📅 19:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690414">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
توافق ایران و ترکیه برای فعال‌سازی مرز جدید در منطقه سلماس
وزیر کشور:
🔹
در حال حاضر سه مرز فعال داریم و مقرر شد یک مرز دیگر نیز در منطقه سلماس فعال شود.
🔹
دو طرف باید مقدمات و زیرساخت‌های لازم را فراهم کنند که این کار آغاز شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/690414" target="_blank">📅 19:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690413">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
سپاه تهران: ستون دود در اطراف دماوند ناشی از امحای کنترل‌شده مهمات عمل‌نکرده در حومه شهر است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/690413" target="_blank">📅 19:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690412">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d9d9fde84.mp4?token=uFukK-f2pCw5U6I_xTA7KITY8jZl2T6lRvmjemO2ANgj2cz14Jwfwn4SdaTFB0rD04ebY12HP4f0FJgGHXx3SGspyCFUO3np_aSCvFQQ41aRQD3vWZT9Juil7MC7v9YtVReVk2XhT6e9ew97___bXm6hmE3uhX9r7Qj9aUBRo9SRWEsyU8rQjdj5NAfhEHzDMjsDBE7iT1bSvnczxS8m1RikHclyxmnFRD6RDZdc37csIPsOLYUSyOSasFFyYAXkcnTIhzFe3lAbWJyy-DMEeXCZzShJ4D4-6p_HHohEEKvVhRxvUn3Fq9LsNpQ0E3M2mnXUgEEH3iEedwQydLioszYDOhBCAjgUbn4bdbgG6XltykIQv-DzSM74R_Htz4XbLAonjZY8in_j3Ov98EsgEOCe_ZKiMdRpAtt6sb-UFzCW3EA8Q8jWN4FQKH4Kx1t7Wif0eGQ2RpNqjvfA_88JRK4LRfMjLLB67asNJUGS54V-lpG4_T_tR1kUP2DzeZjcEPHUh1hYsGkOru930f5x5RF6n0Zk3gJDJPJIIcEdd3oyiE0iYLYCvaTfLzg83xlKocsq-CYwbc_39T9sYmJoGQAUWCwicBeo0fXO9iViSjwHlZNYVUHm8_5QhQ9PZIkCrd2JbWulUZ0Fz7Ep7gat_A8qTlczD8FtS08lGCsr624" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d9d9fde84.mp4?token=uFukK-f2pCw5U6I_xTA7KITY8jZl2T6lRvmjemO2ANgj2cz14Jwfwn4SdaTFB0rD04ebY12HP4f0FJgGHXx3SGspyCFUO3np_aSCvFQQ41aRQD3vWZT9Juil7MC7v9YtVReVk2XhT6e9ew97___bXm6hmE3uhX9r7Qj9aUBRo9SRWEsyU8rQjdj5NAfhEHzDMjsDBE7iT1bSvnczxS8m1RikHclyxmnFRD6RDZdc37csIPsOLYUSyOSasFFyYAXkcnTIhzFe3lAbWJyy-DMEeXCZzShJ4D4-6p_HHohEEKvVhRxvUn3Fq9LsNpQ0E3M2mnXUgEEH3iEedwQydLioszYDOhBCAjgUbn4bdbgG6XltykIQv-DzSM74R_Htz4XbLAonjZY8in_j3Ov98EsgEOCe_ZKiMdRpAtt6sb-UFzCW3EA8Q8jWN4FQKH4Kx1t7Wif0eGQ2RpNqjvfA_88JRK4LRfMjLLB67asNJUGS54V-lpG4_T_tR1kUP2DzeZjcEPHUh1hYsGkOru930f5x5RF6n0Zk3gJDJPJIIcEdd3oyiE0iYLYCvaTfLzg83xlKocsq-CYwbc_39T9sYmJoGQAUWCwicBeo0fXO9iViSjwHlZNYVUHm8_5QhQ9PZIkCrd2JbWulUZ0Fz7Ep7gat_A8qTlczD8FtS08lGCsr624" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهم‌ترین گلوگاه‌های کشور پس از جنگ تحمیلی سوم و راهکار مدیریت آن/ تلویزیون‌اینترنتی‌مدار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/690412" target="_blank">📅 19:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690411">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
رویترز: بارگیری نفت در بندر اصلی ینبع که در دریای سرخ واقع در عربستان سعودی قرار دارد، متوقف شده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/690411" target="_blank">📅 19:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690410">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13720a4145.mp4?token=DK9Qgv8h2zq8ytc3iFj8Mmh7emlDxr48jUgyeF923ORq8dPo5oZFCHpEKI-Hs8WTAOuSJoZ2TIhSCkM0FK-AZNnYxLHnNHn0Sym5cdmMwkHbDUYRj4hgoUlMcJZNtB1YUTCW03Qo-C-nOO598ZXhkrN3XLKfoDHTYPYE1ndsQ9Cyc53bZ6dOdj21p_qspUqSuB4N4Y1JJeGndrs0xdUhjDRxot5terc3FzjtoUHRt1fz4nzPTEMjHFmQN-JvJ9w1EFADFSKLRljg7J7-QM1NoQxcA9e8nq5alnaJXuubT4TJSl-lHWgFNQFYYxvezRXv-esoCbTiMD2jC0z6IjCidA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13720a4145.mp4?token=DK9Qgv8h2zq8ytc3iFj8Mmh7emlDxr48jUgyeF923ORq8dPo5oZFCHpEKI-Hs8WTAOuSJoZ2TIhSCkM0FK-AZNnYxLHnNHn0Sym5cdmMwkHbDUYRj4hgoUlMcJZNtB1YUTCW03Qo-C-nOO598ZXhkrN3XLKfoDHTYPYE1ndsQ9Cyc53bZ6dOdj21p_qspUqSuB4N4Y1JJeGndrs0xdUhjDRxot5terc3FzjtoUHRt1fz4nzPTEMjHFmQN-JvJ9w1EFADFSKLRljg7J7-QM1NoQxcA9e8nq5alnaJXuubT4TJSl-lHWgFNQFYYxvezRXv-esoCbTiMD2jC0z6IjCidA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳۱ میلیون ایرانی در «جان‌فدای ایران»؛ مشارکت جوانان و تنوع حوزه‌های داوطلبی
زارع، سخنگوی ستاد مردمی «جان‌فدای ایران»:
🔹
از میان ۳۱ میلیون شرکت‌کننده، ۳۲ درصد بانوان و ۶۸ درصد آقایان بودند و بیش از ۶۰ درصد زیر ۴۶ سال سن داشتند. داوطلبان نیز آمادگی خود را در حوزه‌های نظامی و امنیتی، امداد و نجات، خدمات اجتماعی، فرهنگی و رسانه‌ای و پشتیبانی مالی اعلام کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/690410" target="_blank">📅 19:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690409">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36d6fe4ecb.mp4?token=e0wW5ssFK2yUDEWHf0Zlaf-2vRc5UjJezXkglIZ8-tBvxL4dFItuPuOeJ4K6RA83eL4IOqgkbwSgWZ82VdWDhiZUHZgqyiGls31reYVwAkxdJKij1lvg__uvZWDmgYdkCfXOKhQ1CrGqrvZzh6mBw9--JFDiXN_9UgcKZpWSF2ln3DyVuG6a0nulUuWmfqBLW-3qzWiNiq7zNREZUSdZVl4sB46gZTPIrmxMqoxRmssAqRZaDZsDdXAL8lIaESu_2FHHnWZK3aYYEjHyQO35xuEJMy1Tf-4j5LWjzAzPXVIAJlqSWNW5ztaTT4fWzvUDQr3DkP_i7tTOdPNsjHPVrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36d6fe4ecb.mp4?token=e0wW5ssFK2yUDEWHf0Zlaf-2vRc5UjJezXkglIZ8-tBvxL4dFItuPuOeJ4K6RA83eL4IOqgkbwSgWZ82VdWDhiZUHZgqyiGls31reYVwAkxdJKij1lvg__uvZWDmgYdkCfXOKhQ1CrGqrvZzh6mBw9--JFDiXN_9UgcKZpWSF2ln3DyVuG6a0nulUuWmfqBLW-3qzWiNiq7zNREZUSdZVl4sB46gZTPIrmxMqoxRmssAqRZaDZsDdXAL8lIaESu_2FHHnWZK3aYYEjHyQO35xuEJMy1Tf-4j5LWjzAzPXVIAJlqSWNW5ztaTT4fWzvUDQr3DkP_i7tTOdPNsjHPVrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنترل ارتفاعات راهبردی باب المندب به دست انصارالله یمن افتاد ⁣
🔹
در ادامه پیشروی‌های منحصربه فرد نیروهای مسلح یمن، کنترل ارتفاعات مهم و راهبردی مشرف بر تنگه باب‌المندب به دست این نیروها افتاد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/690409" target="_blank">📅 18:59 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690408">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pl-wjeg98FeCW5maTDCjMo8MWx73vGmzfNJSP2-g8DPZkyVsMDfqrX0gM4JkKOY0eKxP_GEIgojQTq6XUKizQa_buGJghb1MLdUOx8YISh3y3VPzjKsKn7G3o1BWxZmq6OnvifGJHvpmHYOq3gkHaNvooJHLjAa3qzBjiG0ZmufGC-3L4pu5a5ctjqReQnKysU5zdhy1mOPJsNwh2cLkGCpJynNAA4MhMpV8KpDHoGHzSgjBHv91bNRnKjQcNe5L5RJhErSTqgHcW_HYEMD_2LlEjdIIU_GV4zaUG6-ezMZWkjPnqBzSg6g6vY3f064lvJt9xRtRGOL2RTXY93UQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: ریسک تنگه هرمز بر نرخ تورم آمریکا اثرگذار است
قالیباف با اشاره به تصمیم فدرال رزرو:
🔹
افزایش یا کاهش نرخ بهره به‌تنهایی نمی‌تواند تورم آمریکا را مهار کند؛ زیرا انتظارات تورمی تحت تأثیر بسته بودن گلوگاه‌های انرژی، به‌ویژه تنگه هرمز و باب‌المندب، قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/690408" target="_blank">📅 18:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690406">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e330b6f59.mp4?token=Jr-6yolciv37cAMBX9G-eyQzHIV_teqwPHpyy93yKAO2EWa0JmUebiK8xOyqlZ2XVtpKO04OiewLbmsCD7dEJ3xl17zL1ihb72tGaP_ytTamMU561TzUmkK5IYPn8tYN5qLx9rKO1Tm0bfvOT1F2oV4rIjDQkDGz_nvJ4X30bUPJJ7rcvFcwAoxuT7v8DlyuxMWPxpSxIiGYoONoFEi0AJ7C4ONXwYL0kz6cnCaFjx0eKOl8npoBBNqe_hswiY1GWFOKOMSwyrcklMWfAQaGqJ7dz56EzKo35rdeM6iLvOZmPFIn1EdVMu-deooTUgFgJqEAdr0HGBYzyORKskDcfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e330b6f59.mp4?token=Jr-6yolciv37cAMBX9G-eyQzHIV_teqwPHpyy93yKAO2EWa0JmUebiK8xOyqlZ2XVtpKO04OiewLbmsCD7dEJ3xl17zL1ihb72tGaP_ytTamMU561TzUmkK5IYPn8tYN5qLx9rKO1Tm0bfvOT1F2oV4rIjDQkDGz_nvJ4X30bUPJJ7rcvFcwAoxuT7v8DlyuxMWPxpSxIiGYoONoFEi0AJ7C4ONXwYL0kz6cnCaFjx0eKOl8npoBBNqe_hswiY1GWFOKOMSwyrcklMWfAQaGqJ7dz56EzKo35rdeM6iLvOZmPFIn1EdVMu-deooTUgFgJqEAdr0HGBYzyORKskDcfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زارع، سخنگوی ستاد مردمی «جان‌فدای ایران»: ۲۷ درصد از جان فدایان اعلام کرده‌اند که حاضرند روزانه چند ساعت را به این پویش اختصاص دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/690406" target="_blank">📅 18:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690405">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
وزارت نیرو از پایان قطعی‌های برق خبر داد
مصطفی رجبی مشهدی، سرپرست معاونت برق و انرژی وزارت نیرو در
#گفتگو
با خبرفوری:
🔹
خاموشی‌ها از هفته گذشته به پایان رسید، امسال ۱۴ درصد برق بیشتری به صنایع انرژی‌بر کشور اختصاص داده شد.
🔹
پس از پنج ماه کار مداوم نیروگاه‌های حرارتی، بیش از هزار مگاوات از نیروگاه‌ها برای انجام تعمیرات اساسی از مدار خارج شده‌اند تا با آمادگی حداکثری به مدار تولید بازگردند.
🔹
ظرفیت نیروگاه‌های تجدیدپذیر خورشیدی اکنون حدود ۶ هزار مگاوات است و امیدواریم تا پایان سال به ۱۲ هزار مگاوات برسد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/690405" target="_blank">📅 18:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690404">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
نماینده پارلمان کره جنوبی: ترامپ می‌خواهد ما را هم تبدیل به بازنده کند ، در نهایت این ما هستیم که در تقابل مستقیم با ایران تنها می‌مانیم و تاوانش را می‌دهیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/690404" target="_blank">📅 18:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690403">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLssUNmIHf02-rptoV_D6rdGPw1fF1lAAefMsc9erL1pRQDI-6Jbb0SqzWktwrA4uWLw1nr2bSpiGsvkZoMaSvM-Pp4Mmxz5fGR4RDcQQnJtn0QXrZwKKwVPle5fhO8zUZ8dnSB7Lr5ERzWJZ9XCB_gDBCJYZjlsW5ubTFjFwfdevfZ4DpluUP88rbpg5cZfR-venYMTpsAQ4bARnw4y3jR5vJ_EvQP6orLOI8XX1-AyfENgwSxXGZ76D0ojX5JDFXmYLO51Xu33wlEB6AU93qc8FqEaWT0LWzbjPOOCcwDurqNSZwx0y97fVwiPRHf1W3DlhAtUsmEvZUroaq3kYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا سپاه شرکت آمازون را در بحرین هدف قرار داد؟
🔹
سپاه پاسداران انقلاب اسلامی شرکت آمازون را در بحرین مورد هدف قرار داد. این شرکت چه اهمیت نظامی دارد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/690403" target="_blank">📅 18:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690402">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a063d53ac0.mp4?token=cPWVX2SZKGOdRM8O9EPFNsdG1VmerqR7SFzKEbVFF2iD8ur46y9J_XUMI3ucFEbZGWET4eAZcKcpCMh3AOsFESWbB8c9ZTgvmuskN2yo8rvYi7G0-zHk3Vx22a4aGDof25dplBUhlqemqGryJ8nhFe5OFhooWYNNJfgpGPbqC85Px1-WAMBRq89VT6S2SAllNiGWDZgzg2CrxJYGxA2sfAUBxJ23kHtyogLTXeI7_SIa8UGWwowFum4QHPMpiiF_iRfb6c8_AGkSam05v1wRtggPIepVjRkE5a6XLPHTSwWU4tCZW8BeisJM7zpkJ2w60dfpIeEmTRQDbrMiMKEFkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a063d53ac0.mp4?token=cPWVX2SZKGOdRM8O9EPFNsdG1VmerqR7SFzKEbVFF2iD8ur46y9J_XUMI3ucFEbZGWET4eAZcKcpCMh3AOsFESWbB8c9ZTgvmuskN2yo8rvYi7G0-zHk3Vx22a4aGDof25dplBUhlqemqGryJ8nhFe5OFhooWYNNJfgpGPbqC85Px1-WAMBRq89VT6S2SAllNiGWDZgzg2CrxJYGxA2sfAUBxJ23kHtyogLTXeI7_SIa8UGWwowFum4QHPMpiiF_iRfb6c8_AGkSam05v1wRtggPIepVjRkE5a6XLPHTSwWU4tCZW8BeisJM7zpkJ2w60dfpIeEmTRQDbrMiMKEFkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در زبان انگلیسی کجا باید از the استفاده کنیم؟ #زبان_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/690402" target="_blank">📅 18:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690401">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
یارانه شهریورماه دهک‌های اول تا سوم واریز شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/690401" target="_blank">📅 18:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690400">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18cfd2ee59.mp4?token=rHZ43Vzpnd4yTS1mE46tPrnVbmJmt5-G1ssYfU8frnKNMqXvXzFSuebmpX7XofpbB9UgsyhOsMJVLkI2K6LZo3sSoAkjbIPvlVm4WGftilLyDEZi_inir0iTDvdbyy3wf0MJAwc15F5rc_H9YqjVD0SHjvV2oecOw8V8eph8QfGk-YKIgojnO7v5hS6b0B0vi8RH97HirlQEV2nHVEONQijAluhzi8w3hnoaWIlFzqmrQzScIH56YURiOq9pPXvgfZx1LDYEriQejS1utt0s7H_mUit7L0VneKUhdL-8jwSKlC7VHxWrvhQjR-uqr4XNJf3h2Nhss4ceMiCO6KKbb7Mgi40sjGzkBqtXer2OVEFXKbvXAPqoMCua_6qmNG6ZWX2HGOTAaJO3aPHroAn1CUxXuZgiCFi3l0qSSSWsNA8BPWeJLbYKq31krIjnt4gukW6wNZ6QIfUS-N46byOqjQFWxVhE3djej0erzsvRdAaOlRTKdIQKBwpHaEtBMGytyhCtirMNxh0CSF9sqtnU_Bs2UlZnxxgUJY6-LTS4FyYAeGFlPrdcunbmViO66nS3I83lGPrHWPsfSX06PS2AkqVFqwX-hcIFvbcXlchZB5R4OrEnKZj3osR_5bTBzanDPrQkUGx4LJABF52UC4IJs0lOhTUIG9jRGqJQAf27XWY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18cfd2ee59.mp4?token=rHZ43Vzpnd4yTS1mE46tPrnVbmJmt5-G1ssYfU8frnKNMqXvXzFSuebmpX7XofpbB9UgsyhOsMJVLkI2K6LZo3sSoAkjbIPvlVm4WGftilLyDEZi_inir0iTDvdbyy3wf0MJAwc15F5rc_H9YqjVD0SHjvV2oecOw8V8eph8QfGk-YKIgojnO7v5hS6b0B0vi8RH97HirlQEV2nHVEONQijAluhzi8w3hnoaWIlFzqmrQzScIH56YURiOq9pPXvgfZx1LDYEriQejS1utt0s7H_mUit7L0VneKUhdL-8jwSKlC7VHxWrvhQjR-uqr4XNJf3h2Nhss4ceMiCO6KKbb7Mgi40sjGzkBqtXer2OVEFXKbvXAPqoMCua_6qmNG6ZWX2HGOTAaJO3aPHroAn1CUxXuZgiCFi3l0qSSSWsNA8BPWeJLbYKq31krIjnt4gukW6wNZ6QIfUS-N46byOqjQFWxVhE3djej0erzsvRdAaOlRTKdIQKBwpHaEtBMGytyhCtirMNxh0CSF9sqtnU_Bs2UlZnxxgUJY6-LTS4FyYAeGFlPrdcunbmViO66nS3I83lGPrHWPsfSX06PS2AkqVFqwX-hcIFvbcXlchZB5R4OrEnKZj3osR_5bTBzanDPrQkUGx4LJABF52UC4IJs0lOhTUIG9jRGqJQAf27XWY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جهت آشنایی و کسب اطلاعات کامل از حساب معاملاتی شیلد zorafx وارد کانال زیر شوید.
https://t.me/zorafx_broker</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/690400" target="_blank">📅 18:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690399">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fc89fd892.mp4?token=IqnMHqrUCQGYZFgzYT1QVlDE0jqK92dHWvdCJFkJglyROW7jJvj0nHJCuU6MSvDalCZ-XJL0qg1N4EhFzzrTNT6affo6Xlg2nPl_QCewiU1ktJGWxU0mqWrkUJdgDfmeBHzmWCklWI1usm1RLyKpahKRBW89R1exiQVbgPvCPQ-gaGPVvQYZc3_eEZC2lBVvujrIHHTLMdzwPiWndylSwcEq4c3z4CuPrgbYn1vSxmsV3d2CIV2P-Kmlu_EbH7VdmPMbR5ciwcYXMHsCzOdOOW05PRIKXtS7zejp_s9MUnM5nLgzTfs0w4CTTCKm9Bg5HE6Mm9xVMIHBeuprEqedUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fc89fd892.mp4?token=IqnMHqrUCQGYZFgzYT1QVlDE0jqK92dHWvdCJFkJglyROW7jJvj0nHJCuU6MSvDalCZ-XJL0qg1N4EhFzzrTNT6affo6Xlg2nPl_QCewiU1ktJGWxU0mqWrkUJdgDfmeBHzmWCklWI1usm1RLyKpahKRBW89R1exiQVbgPvCPQ-gaGPVvQYZc3_eEZC2lBVvujrIHHTLMdzwPiWndylSwcEq4c3z4CuPrgbYn1vSxmsV3d2CIV2P-Kmlu_EbH7VdmPMbR5ciwcYXMHsCzOdOOW05PRIKXtS7zejp_s9MUnM5nLgzTfs0w4CTTCKm9Bg5HE6Mm9xVMIHBeuprEqedUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری: آیا شما به اندازه‌ای شجاع هستید که یک جدول زمانی برای کاهش قیمت انرژی ارائه دهید؟
🔹
وزیر انرژی آمریکا: من قطعاً نمی‌توانم رفتار ایران را پیش‌بینی کنم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/690399" target="_blank">📅 18:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690397">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هشدار درباره کمبود تجهیزات پزشکی در هفته‌های آینده؛ ۳۰۰ همت اعتبار ریالی برای جبران این کمبود نیاز است
علیرضا چیذری، رئیس انجمن صنفی تولید، تأمین، توزیع و صادرکنندگان تجهیزات پزشکی و دارویی در
#گفتگو
با خبرفوری:
🔹
بیشترین کمبود تجهیزات پزشکی مربوط به اقلام مصرفی و قطعات یدکی از جمله برخی شنت‌های مغزی، سمعک، کتترهای خاص و محصولات وارداتی دیالیزی است.
🔹
اگر کمبودی در برخی اقلام احساس نمی‌شود به‌دلیل وجود ذخایر در ته انبارهاست اما با ادامه این روند، در ماه‌ها و حتی هفته‌های آینده احتمال بروز کمبودهای جدی وجود دارد.
🔹
برای جبران این وضعیت با ملاک قرار دادن قیمت‌های سال گذشته، حدود ۲۵۰ تا ۳۰۰ همت اعتبار ریالی نیاز است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/690397" target="_blank">📅 18:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690393">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M8nZGcynN513N9AkZub3xO_s0dlKQxmjpsU4dtLd-JPlRcgJc8rUpNFxqmPlqxTwuqiwbFe0kzT_tRQvwa1cu_InJCTgqlNnetETO2EHN-HbvBMEEdWHjq9M64tffhQG7sVl7oHJPi0b1fasHn4aF3BGzu6T22kTGdqdJUXmnXR0EoXl8cjTwteoMjwEdTPnE3Y333C_2dudLMnXUYGsF9iiJRAThIzr21ZF37iKLK_fXRma_p3OONyCA-ZR6qTuVCuV1QXjxNgXE4q_T3qGDumYsqYuUfD6UJj4ZcFPpiubJMqXTXmkDY5J_b6x-P7QoI-mL7zxaLDXcO0v5f3kpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QFiH5NY5l9Z9ZuVl7iEUp8Rh7tlImyd5VXPNgmzGLyW0FNC5BnSm7uqGppp5lazDS9nLdZTUH_GJEDTFTaLVx2xGT_18zcNacbYQ4dbQJyCL0hIPkNZHafSpU4nlKns9T96wXa7HPYGkOc6rnjmq95Mm9Gcwltk5unpjTV0Z1pcYDGhh-RBkzrJkhoeMwRU_bKQpTHLhS6talo5AtD0VLC07IPdhyRXeM8oQehhbPY1jFquoUkvZcoySOSm3bILXEgIVrxyQ1ZvRXZMPCJPYVFRFYKUylzftdyNxgYuyK7p2YQqURwSIV3AtCeXkQwKMayhzIj0JPW00WRJzh62Wew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ul4Jd6e1Pj5zXfGM3oeI87Fh09YyQAwO7mgOQcHdlZ2ta6Rbsht0gVVDMbrGQLXtUCb5Vk7ufm97znexnA5ri_DKD_EqI6NKMVBXLVU_mSl4IyNSo5-1OpRhamFIJf8A75Ky32iGiqV-mk5GPf4n1X-ECpKbTU4Cmrausq75b_MIjK_za-7tjE4Q8wGf4zrEncMDk58TbdxQ8gNtwKOtYRhUefNWLKhXwqrYI4jLlBBTHynOMefdwDGfmzVigzMpidFf0onkSCJx8hSzQyj2B0cL9yRcMqkBPItKKlD6VFUzu62gpYdi192oVtlReWlUWEcSFRzHEkKMJmJEFU3JcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Es6KxV_JlMMvE_TrdjMz_qz4DJkYz8S0-vpvxW6QxO9Qo0YwF7ODVyHvJANBIgi48Axdz1nCRHmme2hbIoczNwhArP_UHjP9wF4u27M9Axgx3W96B8y1uOXEvj2FlG9yTKl80K7GWZcZz7RPXbRXRbUpK3-CGiJve8jOwTJeNWQWYD0J47-a9_8lq3iPcXV_LMQhFxFAA_XIwKiEU4hrMw3CXfNpxpoHHi3b6F2bj9DCnN7xxwVh9m-jJcewZ8VvTpq37DFRH0XRMkA_lCfKMlPDONBmOIKoDU2cTSx3i0z4ARisBBQOcpHG3f7vHKq7KJrUnKgKuT03qKSNc39PXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری کامل از لحظه رهگیری و سقوط جنگنده عربستانی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/690393" target="_blank">📅 17:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690392">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
تصاویری از لحظه سرنگونی یک جنگنده F-۱۵ سعودی توسط انصارالله
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/690392" target="_blank">📅 17:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690390">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVh1MOCr2DZsH0tD4VWvToLDHVjjOQI2BmroTytAO_IYYkCRKsgYIuihJr6wP7hS5vt60_WeNnoCs9c7FNb2-AnJANFUrVW55OcEQyKON9qJnQjTomUPDkj9uWH3Xp9vRKKbjzopQ8L4mkMgKN2O9wVy9XKqfcBjDXj7z39Jz4bMGUva-Dob_mHEEYQLXXKUQtNQnU44aFe4ronbBduEjNPYixJI-REEX2fdwL_AG5cjpNamWPLUgcJgjAEMCF-jMnWhb0VgHO7BjW_TEic6TXOtyNPE6UQYYNUJqN9ROj2xJFhXEJohGMans3MOHc0sm4Lfi951VLME6ufdpM5Mtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیشترین بازدهی یک‌ساله صندوق‌های سهامی
🔹
بررسی بازدهی یک‌ساله صندوق‌های سهامی نشان می‌دهد صندوق سهامدار با ثبت بازدهی ۲۳۱.۵۴ درصدی در صدر این فهرست قرار گرفته است.
🔹
پس از آن، صندوق رشدی کیان با ۲۰۹.۷۱ درصد، صندوق مانا با ۱۹۹.۴۷ درصد، صندوق ثنا با ۱۹۶.۲۰ درصد و صندوق زرین با ۱۹۱.۴۴ درصد قرار دارند./ تیتر تجارت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/690390" target="_blank">📅 17:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690389">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
هواپیمایی ماهان پروازهای بین‌المللی خود در مسیرهای ترکیه و عمان را تا اطلاع ثانوی تعلیق کرد
🔹
بر اساس بخشنامه‌های ابلاغ‌شده، مسیر تهران-مسقط از ۲۶ شهریور و مسیرهای تهران-استانبول و تهران-آنکارا از ۳۰ شهریور لغو می‌شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/690389" target="_blank">📅 17:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690388">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRf9i_-bGMJ7o72Wd92jDTsjmENKoNmmuZ5fJsWd0WEbU5PiNis3ldXCWDu96G97DOfYDwpvoM2DUuNeIgXB9xifL8-oyE50IADA6rT6u0dZJQO7WMTHZ8stuv4wgcJIDVdGbm-gk82LFJcUw62a2U3Iu5dpDVCMXMTkeX7RedJtbARC234vo7TiFKW4kDufQWyf4R1XiVyJ9CeTPnQ_-thjZiaFfrGu-T11w7mQCZcZcDr3BHGX0VQZctJGCaHRyZ_kFNLp4FBKTQj0LHmD3O82wHVFByGL2z8sQwRUzSnWro9jTN6e-6iFNXwiNDSVYUp7POJ2bUxTgHZ87m5HSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انواع کشتی‌ها و محموله‌های آن‌ها
🔹
در صنعت کشتیرانی، کشتی‌ها متناسب با نوع بار طراحی می‌شوند؛ بر همین اساس، کشتی‌های تانکر برای جابه‌جایی نفت، فرآورده‌های نفتی، گاز مایع و مواد شیمیایی به کار می‌روند.
🔹
کشتی‌های کانتینری و عمومی کالاهای مصرفی، صنعتی و دسته‌بندی‌شده را حمل می‌کنند، در حالی که کشتی‌های فله‌بر ویژه جابه‌جایی غلات و زغال‌سنگ هستند.
🔹
کشتی‌های رو-رو نیز برای حمل وسایل نقلیه و تجهیزات سنگین مانند خودرو، اتوبوس و تریلی استفاده می‌شوند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/690388" target="_blank">📅 17:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690387">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhlRWpqLRZeiut9alSZs62Nwnwe3zmV-Jp8fnre2CZaKb1txkYnJIAt0v1ldP9BWDxm94FCHDbXE-y93AHn7aLNr6OEE3hRQiB3Xiu6mRWIIK6Mvvqvi4iVZASe8uE_oKHwNwy8lmNIr-DJMKqd9VvWDj4rBOkMRbRiWpBJWPe1ZaF30Ca8ja5jc5HINXzqN0Uhh_CzB9MbhGIBtqABeEN9LrPdHwafJnAz3KpC1ukeYbatwPkNXlin-rkFtiBy6pBXZgsv4a-hk19lStlEAV4-lmLXUrZCKJ1zbDY4udPCHnZvl961eOPZECKFlfAZmWVk-gZASoIx7rKo5v7WOkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صدر اعظم آلمان نمی‌تواند از جنگ و جنایت حمایت کند و همزمان خود را قهرمان صلح و معلم اخلاق معرفی کند
اسماعیل بقائی سخنگوی وزارت امور خارجه:
🔹
«صدراعظم آلمان از «جنگ» ایران، «برنامه هسته‌ای نظامی» آن و «نیابتی‌های» ایران سخن می‌گوید.
🔹
این، یک روایت کاملا تحریف‌شده است. این آمریکا و رژیم صهیونیستی بود، نه ایران، که جنگ تجاوزکارانه را آغاز کرد. آلمان حتی از حداقل شجاعت اخلاقی لازم برای محکوم کردن این عمل تجاوز هم برخوردار نبود.
🔹
آلمان نمی‌تواند آشکارا از کار کثیف» پشتیبانی کند و سپس خود را قهرمان صلح و معلم اخلاق جا بزند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/690387" target="_blank">📅 17:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690386">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
وزارت خارجه سوئد در راستای اعلام حمایت خود از اسرائیل، یکی از کارمندان سفارت ایران در استکهلم را اخراج کرده و سفیر ایران را نیز به وزارت خارجه احضار کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/690386" target="_blank">📅 17:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690385">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
سیستان‌وبلوچستان در صدر هزینه بنزین؛ قزوین در انتهای جدول
🔹
بررسی میانگین مخارج سالانه بنزین در استان‌های کشور، اختلاف قابل‌توجهی میان الگوی مصرف و هزینه‌کرد خانوارها نشان می‌دهد.
🔹
بر اساس گزارش سازمان برنامه و بودجه، سیستان‌وبلوچستان، بوشهر و هرمزگان بالاترین میانگین مخارج سالانه بنزین را به خود اختصاص داده‌اند؛ در مقابل، قزوین، قم و کرمانشاه در پایین‌ترین سطوح این رتبه‌بندی قرار گرفته‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/690385" target="_blank">📅 17:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690384">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f889f99f36.mp4?token=QyPxn-ki6jcBbchySIXBc5wcCVTXcU-NDMvxA6XRTMeRUB4zIQLqyCQDGpH_1EHrwDHOQlGg9Sg0RGxEG5niW06XT_4TdENn-FFmIQJha-ZyvsyRwlSh-a3J9OCnMBzefS9FS7Lo3KUK7bXSk4Ra7YOxf4WErSc48XlV6268Gs31rzm1o9oN2nNWwz0rbiCWfod8bdzmTysjFSdDQw3u8ap2kLjUA4tJmwQxJjiSOGyZ61g2I-lsoNxnnniPihJsK7iyI2iwtCecuiBZh5sPKKdNFdTLuNlHAS4ZeO7lrpQGvox1Kb6Vyl3Zf8Vou-hNvH_gsVip_Tsph7NGJJVdVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f889f99f36.mp4?token=QyPxn-ki6jcBbchySIXBc5wcCVTXcU-NDMvxA6XRTMeRUB4zIQLqyCQDGpH_1EHrwDHOQlGg9Sg0RGxEG5niW06XT_4TdENn-FFmIQJha-ZyvsyRwlSh-a3J9OCnMBzefS9FS7Lo3KUK7bXSk4Ra7YOxf4WErSc48XlV6268Gs31rzm1o9oN2nNWwz0rbiCWfod8bdzmTysjFSdDQw3u8ap2kLjUA4tJmwQxJjiSOGyZ61g2I-lsoNxnnniPihJsK7iyI2iwtCecuiBZh5sPKKdNFdTLuNlHAS4ZeO7lrpQGvox1Kb6Vyl3Zf8Vou-hNvH_gsVip_Tsph7NGJJVdVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر درد کمر، علت یکسانی نداره؛ محل درد می‌تونه سرنخ مهمی درباره عامل ایجادکننده اون باشه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/690384" target="_blank">📅 17:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690383">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dfd7aae45f.mp4?token=vTV6gJgsNfCZE3gSyJCh1U4fJoPeqU15ZC6GiTVdIV-gXEJSLGpNkrAuIg_RYzCuvPqOXvaqG4kt3UilHN4IBcjVkiXOr8Yv_ERPxew7-jIas-GQWdP2dckoljRgYHuvtrBWHWjOPly30P4cQRL5J4dM9HMTPeKK_opm0kg8oZs40yQkbKhbpCjVx1fGDCltAGYMvHlEJ-3Nsow1jjb8uuiYiQGjhbk_Sb3BOG3_75dXyrWxguQFBWlSrHFq6C00EbxRTg4s1LuEEW85lkvR4v7HZnRzcUvVe_I1o_AmPl0okhD708EFe5Xb9fzkAMk7GsGaICOwP6W-kVWdZ0c4qg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dfd7aae45f.mp4?token=vTV6gJgsNfCZE3gSyJCh1U4fJoPeqU15ZC6GiTVdIV-gXEJSLGpNkrAuIg_RYzCuvPqOXvaqG4kt3UilHN4IBcjVkiXOr8Yv_ERPxew7-jIas-GQWdP2dckoljRgYHuvtrBWHWjOPly30P4cQRL5J4dM9HMTPeKK_opm0kg8oZs40yQkbKhbpCjVx1fGDCltAGYMvHlEJ-3Nsow1jjb8uuiYiQGjhbk_Sb3BOG3_75dXyrWxguQFBWlSrHFq6C00EbxRTg4s1LuEEW85lkvR4v7HZnRzcUvVe_I1o_AmPl0okhD708EFe5Xb9fzkAMk7GsGaICOwP6W-kVWdZ0c4qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اطلاعیه انصارالله یمن: اخبار منتشر شده در خصوص حمله به جده و مکه را قویا تکذیب می‌کنیم/ هیچ ارتباطی بین انصارالله و انفجارهایی ادعایی در جده و مکه وجود ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/690383" target="_blank">📅 17:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690381">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNobitex | نوبیتکس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vitrq0d7joF0IIaFah6du_LASE0aOsAWTiQ9MZ7s38aYUUHc9mvr17dhcHoGFKFcJi43U64FZtDMt_bFFFdTE8dgYVQ8eqwmtuFHYNC_yFFBo2UtNVaT00iCeCuySHgUd0sBig_vLMAAxBdYUmlmfk_i6wh14D7sl0no00Qe4QGzbvDSolaT95rGLIXwRwaGfPIYMiXfqxw2uhvUsxPWLqm5cLr6AJXNeH-j3quokiGg3_ZdKW1jva5kkCyyQbcvmDfDAHogX2mahRUrhUquH2oTCiiyDOy3qb6EXSokYa1X0g2k-dXVX_W3yp9wUqT8A1yoQqzfYt-XoO3JSYqTtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
مهم‌ترین سیگنال بازارهای مالی؛ چهارشنبه‌شب
این روزها تاثیر اخبار اقتصادی کاملا مشخص است. مثلا خبر افزایش بازخرید اوراق کافی بود تا طلا در یک روز بیشتر از ۳٪ رشد کند و بیت ‌کوین هم تا ۸۰٬۰۰۰ دلار افزایش یابد.
داده‌های بازار کار امیدها به کاهش نرخ بهره را تقویت کرد، اما عواملی مثل رشد دوباره تورم و سخنرانی کوین وارش در جکسون هول،
احتمال افزایش نرخ بهره را در پایان تابستان ۲۰۲۶ به ۹۰٪ رساند!
حالا سؤال این است؛ بازارهایی که اول ۲۰۲۶ منتظر کاهش نرخ بهره بودند، با افزایش آن چه می‌کنند؟
نوبیتکس یک سال است که رویدادهای فدرال رزرو را همراه با کارشناسان و فعالان بازارهای مالی در قالب برنامه «Federal Effect» پوشش می‌دهد.
موضوعات مورد بررسی در «فدرال افکت» نوبیتکس:
🔴
پوشش زنده اعلام نرخ بهره و سخنرانی رئیس فد
📄
بررسی تغییرات بیانیه و مسیر آینده نرخ بهره
📊
تحلیل اثر تصمیم فد بر دلار، طلا، بیت‌کوین، سهام و بازار ایران
🗓️
چهارشنبه ۲۵ شهریور، ساعت ۲۱
:۰۰
🔗
این ایونت را می‌توانید به‌صورت زنده از
مجله نوبیتکس
و شبکه‌های اجتماعی نوبیتکس تماشا کنید:
📹
یوتیوب فدرال افکت
💖
آپارات نوبیتکس
⭐
تلگرام نوبیتکس
🌐
اینستاگرام نوبیتکس
💜
@NobitexMarket</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/690381" target="_blank">📅 17:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690380">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
بلومبرگ:  عربستان پس از تعطیلی خط لوله نفت خود، فروش فوری و نقدی نفت خام خارج از تنگه هرمز را افزایش داده
🔹
شرکت آرامکو این هفته حدود ۲۰ میلیون بشکه نفت خام به پالایشگاه‌های آسیایی فروخته؛ خریداران می‌توانند این محموله‌ها را در خارج از تنگه هرمز تحویل بگیرند.…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/690380" target="_blank">📅 16:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690379">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
حمله ایران به کشتی آمریکایی در اوایل هفته جاری
ادعای فاکس‌نیوز:
🔹
اوایل هفته جاری، یک کشتی آمریکایی با ۴ پهپاد و دست‌کم یک موشک ایرانی هدف قرار گرفت و تعدادی از سرنشینان آن مجروح شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/690379" target="_blank">📅 16:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690378">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a34ddfbf.mp4?token=dJWqjbHGu_WYx1TD3b0mPaIj7Av6YPUbkxsiRPi5NkbfOFdypBcmiNftGssrFftur27Iba-o4pOPYfVXbEd_v72BXmavr2yQS0ZEyZIBhM90FZWLQa8T-3_eEEf-xPK6LoqqPFkHHSeCAmnKzsCGRvoHTG7gBGSA3Lo-eENXtFpzjw2N6T3fT_QYWRfPy0Ri90rEYAiCayUnIudkpzM9HcmMISXMyToz8jOGPRqrypa2VgWez-Wc09h3PgsX6TGKvR5XrkRSLY8GU2X-zBE5rFUIQdbm_SpS8dkgyfB3tGtPueTW8o3PtRBl6-gmfNiSx_5wVvbO9gwRrsDvO_9Wdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a34ddfbf.mp4?token=dJWqjbHGu_WYx1TD3b0mPaIj7Av6YPUbkxsiRPi5NkbfOFdypBcmiNftGssrFftur27Iba-o4pOPYfVXbEd_v72BXmavr2yQS0ZEyZIBhM90FZWLQa8T-3_eEEf-xPK6LoqqPFkHHSeCAmnKzsCGRvoHTG7gBGSA3Lo-eENXtFpzjw2N6T3fT_QYWRfPy0Ri90rEYAiCayUnIudkpzM9HcmMISXMyToz8jOGPRqrypa2VgWez-Wc09h3PgsX6TGKvR5XrkRSLY8GU2X-zBE5rFUIQdbm_SpS8dkgyfB3tGtPueTW8o3PtRBl6-gmfNiSx_5wVvbO9gwRrsDvO_9Wdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فورد پهن؛ ابتکار جالب یک صنعتگر
🔹
یک صنعتگر با جوش دادن دو خودروی «فستیوا» به یکدیگر، عریض‌ترین فورد جهان را ساخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/690378" target="_blank">📅 16:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690377">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyklLUuc2iVkn4rs5hlfRDAcmZ4rsXYLTpcqXTcQCqyHcx_xNQjojgql_4s-DK1kDtUI89anp8E841-uof_D2cEBlRw8jsM47ilgaYU68NSSV407E1ONkbWrmoOtG1T3PcVARE7f25rJMTe60eW10ds-_tua7b1x3e2U_cgICrAQlIRKLp5FfAdf6wgUW3oF8lL7N96dZEOkHVXl4OxQPxdJTnkTuEm1QOsoZMeMY1TBOXEMQaKeaIplnmI1L3VkO6QRT8DLahQUt08JLDFK264Ue5iyJAnNdYKWvCEdEdzapSK8rB7dciV9kvJtZjoeL3esS-jVrzWRel6zOlsufA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کارشناس آمریکایی: تحریم‌های جدید علیه ایران بی‌اثر و بی‌اهمیت‌اند
برت اریکسون، کارشناس آمریکایی حوزه ژئوپلیتیک:
🔹
تحریم‌های جدید آمریکا علیه ایران بی‌اهمیت و بی‌اثر هستند و طرح پرسر‌وصدای این اقدامات از سوی دولت ترامپ برای من به‌عنوان یک آمریکایی شرم‌آور است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/690377" target="_blank">📅 16:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690376">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjAh1rBsV7qxcQkvbfWz2uXCrGDKicq1BCgWpq7hKX3Xwdx0gGO6Q2-YAamJEJVcSRRnIukewwstiyTaR5WC6z_HmrsWN5VV2YbS1pbYusU7z_xbWxp9qNAdosyJL7y2F9vf3tKJ3WOz20Yl-G2AfRqK-5DvjQsF48oEem5B1YangUsrN0Sa0sW6q28D46gZVfenX1xVHk5j1tClmb-MTggd2RoXNMqYLBGtvIDEaoCGzyxi7JfesGqocyRRftkxZFNZXPH28BYlfd084r3NcmrfpYltldrBAuYQ_BMeV8pTz9BEPxm8v8IoE-YNW3kw7ljeQ5guavJQQTOADkRbJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا طرح کالابرگ توانسته نیازهای واقعی خانوارها را تامین کند؟
🔹
نتایج جدیدترین نظرسنجی متا درباره تجربه استفاده از کالابرگ، نشان می‌دهد که
بیش از نیمی
از ایرانیان، معتقدند اعتبار یک میلیونی، کمتر از مصرف معمول هر فرد است.
🔹
همچنین،
۴۱٪
از مردم اعلام کرده‌اند که فهرست کالاهای مشمول،
با نیازهای اصلی خانوار هم‌خوانی کمی دارد و نیاز به بازنگری جدی دارد
@metaacenter
#کالابرگ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/690376" target="_blank">📅 16:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690375">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdzg8CUoPrUr77RT9FSawbF16_B9QZfW0SVLnrAbHAsaxQ4SGxQ2gmWW2-4UF618FYzzYyEi5ljiGH3tg8Xyp9N1d8_UXj2Z3eGB9YrfxAvyidtsE4FnRc6UGd9u1XZa1ftkON4WWkonS6A9b8uWw-eWeGNMDiP1DyeXqICvsm9VM7osj-EUpgFSjvL4HUDEw16xIU9X8xlDtSViEVcCE4AK24KTeROCxcn18ugIPOZ6xLXMMUlEvyvyiFxZlnm4KxrOamBnTFH9WmbVruaSxzX771-G_Ldb6LpaiWOuQAfLsIJFvoXWdWd7g990udLuaruI9uh48LaO3snUNvvObQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کرونا از آستانه هشدار بالا گذشت
🔹
مرکز مدیریت بیماری‌های واگیر وزارت بهداشت از افزایش درصد مثبت کووید-۱۹ نسبت به هفته قبل خبر داد.
🔹
درصد مثبت‌شدن آزمایش‌های کرونا به ۱۱.۷ درصد رسید.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/690375" target="_blank">📅 16:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690374">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
در تازه
‌
ترین جنایت رژیم غاصب صهیونیستی به مناطقی از غزه، تعداد زیادی از افراد عادی در زیرآوار به جا مانده از حملات هوایی گرفتار شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/690374" target="_blank">📅 16:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690373">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: مهم‌ترین سرمایه امنیت ملی ایران مردم ایران هستند که در لحظه خطر، به چیزی جز میهن نمی‌اندیشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/690373" target="_blank">📅 16:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690372">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb5f8539c.mp4?token=cuSCrYbGGJg6fGuLUoI6v1Q_3V5KLexBHfNoMYlJeUJFE1DoYTIjF-eA_ESKZgAnDGI_m6V3mBHWB_U4SqtQqdvSrKnqQl4Ii6LrXcNg4sXHFhsUhcwQmjhxQgRR5yOHAEY6oLiayCoqekiiXUfXS5e5Xmuyvj_iUjZpPEq6l-Qy6Jp_f16VqNoBX_CNTQ4yvHSwzm5-7Hrn1-wNu5elXVGJMQb85W0Ch9hmgDZ_s6Ybo-6GXFRydxJ6NL53QOaonSM6XNN-8U-Calwv4hRJ5Cg-AeL-aITbCJx2Li8jpT5Z3HcG8jcQ4aToq4d6DOUsPcLduwNaU5Ws2RurFeU9zpRFrQiYrEb9R1Uva7PsqM8cyHmqOgxYn0vhq0HoOgzpG9NN4aGVEAScLKdDAXHU5KsEp7V1QD79X95ktEB-gKRS2AUyX9WYlLOZW20C4PoVfDF1gE0jYb_vHKAweAjG0pZpi61Ug_z0DUrg0G_iCEenRYGy0dnr7Cup5XfvpbDSNDLAmJpIfE4nhuFj4CkfcKQmXXppIM4d-w_buvBLd7_z_RLkSir637rqCaPgUwMnyudnJ87l-YZ7iT66bKZ1-ZKvWHP1Jtd_32JUGFs3suQoeCEkeRjiyS2K-vcS9cTuDk38DQcSCXYLbq0n8clg3ZNWfc3TmRniXkV87eA8Tpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb5f8539c.mp4?token=cuSCrYbGGJg6fGuLUoI6v1Q_3V5KLexBHfNoMYlJeUJFE1DoYTIjF-eA_ESKZgAnDGI_m6V3mBHWB_U4SqtQqdvSrKnqQl4Ii6LrXcNg4sXHFhsUhcwQmjhxQgRR5yOHAEY6oLiayCoqekiiXUfXS5e5Xmuyvj_iUjZpPEq6l-Qy6Jp_f16VqNoBX_CNTQ4yvHSwzm5-7Hrn1-wNu5elXVGJMQb85W0Ch9hmgDZ_s6Ybo-6GXFRydxJ6NL53QOaonSM6XNN-8U-Calwv4hRJ5Cg-AeL-aITbCJx2Li8jpT5Z3HcG8jcQ4aToq4d6DOUsPcLduwNaU5Ws2RurFeU9zpRFrQiYrEb9R1Uva7PsqM8cyHmqOgxYn0vhq0HoOgzpG9NN4aGVEAScLKdDAXHU5KsEp7V1QD79X95ktEB-gKRS2AUyX9WYlLOZW20C4PoVfDF1gE0jYb_vHKAweAjG0pZpi61Ug_z0DUrg0G_iCEenRYGy0dnr7Cup5XfvpbDSNDLAmJpIfE4nhuFj4CkfcKQmXXppIM4d-w_buvBLd7_z_RLkSir637rqCaPgUwMnyudnJ87l-YZ7iT66bKZ1-ZKvWHP1Jtd_32JUGFs3suQoeCEkeRjiyS2K-vcS9cTuDk38DQcSCXYLbq0n8clg3ZNWfc3TmRniXkV87eA8Tpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران به ۹ جنگنده آمریکایی در اردن آسیب وارد کرد/«سی‌بی‌اس» گزارش داد در پی حمله به پایگاه موفق‌السلطی، ۹ هواپیمای نظامی آمریکا هدف قرار گرفته و آسیب دیده‌اند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/690372" target="_blank">📅 16:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690371">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
آسوشیتدپرس: تعمیر خط لوله عربستان سه تا پنج هفته طول می‌کشد
🔹
خط لوله نفتی حیاتی عربستان سعودی که مورد حمله پهپادی قرار گرفته تا زمان تعمیر خسارت، عمدتا برای هفته‌ها از سرویس خارج خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/690371" target="_blank">📅 16:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690370">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTsMvuHHcNPxeN-nsgU5BEAramY1Th0NM8Yxy6A3z7psg7crJGzJ5SItrN72i3AMKBd4DCoNydA94YSPTkbm2IDcxdEYAZcpAU4DBrRklvNQ19Y168LEIzXUPmnw9ZNqdZaEMZcUO-HXMdV8DP73rNLJbXv_C7t36v51dKOQBs8EvWcD4EXg5h0NMqPzTs2NAXmx053GrBB-3II8JRSigiblo5ijLX6ynBRgwyasM8_s3tfPw4F_KFeHlQM7-MFsnIxIvZhhJwNvn0MLNXSFRyk-N70H-OPcMTmQWbyOxsLn93cfsH0lc7mEgCI95ZPXc09vuo346AD1yX_IMzF_vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حقوق در ترازوی طلا | پس‌انداز «گرمی»، سقوط «کیلویی» | با یک ماه حقوق ۲۰ سال پیش چند گرم طلا می‌شد خرید؟
🔹
حدود ربع قرن پیش، کارگری که دستمزد حداقلی می‌گرفت، می‌توانست با حقوق ماهانه‌اش ده گرم طلا بخرد؛ دارایی‌ای که سپرِ آینده خانواده‌اش بود. امروز، در سال ۱۴۰۴، همان حقوق به‌سختی یک گرم طلا می‌شود. این عدد ساده، شاید گویاترین تصویر از فرسایش قدرت خرید میلیون‌ها ایرانی در دو دهه گذشته باشد.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3245634</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/690370" target="_blank">📅 16:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690369">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hf6vilVo9dykOc4LOB7NaxgnECtnWyBrw28CAFM6gjNi33v0kQXqp6-Hnp1cItGADfSnk4l-f_ZR_PMIAnaNhuvdKSNHNI4_G7ymk0RV13kEEuH_E8keTqeoQ9bdk_y2px-CJh2Q3HKo2L5dvvZ7yuOkoMf9La1neDRZ_aVbZKQ_PMMeu32yuWJj_MJHpk_JTp8d-8SGFK_FQqxWjsNSfrk11iErBlMzbU8DwLN6Pv7lVIPKNvcll0qWO_Z_Dt_sytCcAHdZwUIai1NxWluxYKQrPV29NQeXkdAP9MW65tHB4LUJSZ6Ns8P-k9iGWJ-UDmlmvLo2295Ix4kCbdp_XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توزیع سهمیه‌ای اقلام مصرفی خودرو
قطعات وارداتی شامل:
کیت‌کلاچ، لنت‌ترمز‌،شمع،وایرشمع،تسمه تایم،تسمه دینام و...
مختص خودروهای داخلی
شروع طرح: چهارشنبه ۲۵ شهریورماه
ثبت سفارش با محدودیت کد‌ملی
تحویل رایگان از ۱ تا ۳ روز کاری از طریق پست
💳
امکان دریافت نقدی و اقساطی
🌐
متقاضیان گرامی جهت کسب اطلاعات بیشتر و درخواست اقلام می‌توانند به وب‌سایت ایرانکو مراجعه نمایند:
www.iranko.ir
.</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/690369" target="_blank">📅 16:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690365">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
اکثریت آمریکایی‌ها ترامپ را فردی فاسد خطرناک می‌دانند
🔹
طبق نظرسنجی سپتامبر اکونومیست و YouGov، تنها ۱۸٪ از آمریکایی‌ها ترامپ را «با ثبات» و ۱۴٪ او را «تفرقه‌افکن نیست» توصیف کرده‌اند.
🔹
این نظرسنجی همچنین نشان می‌دهد صفاتی مانند «فاسد»، «بی‌رحم» و «نژادپرست» از جمله توصیف‌های مطرح‌شده درباره ترامپ هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/690365" target="_blank">📅 15:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690364">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05f05bf09f.mp4?token=LIRop9X3xZ50rcthPIo2ucCSh1OYcGczl1ulcnTHcu8di9MQCuj9ei4lw647dMi5dfCvEH7_QEDq18kugCv9x1-mxUSYWoxX2szLLorvgbak3VDLwF9v8LM_vug7WmES846YawQODljHNKEv_vm7RgORUX8F5jEGekERhO5tBxtOzlrsXNpzlKzgxW0viVQpyP09_JBNf0mP_V_AOsZ1MbvYf0qLmOcKA0tvGBMdj1L29ArPH829qRK63c_n39BhJDziYYfKkYUaGUOWOXfOB5zU9KJQlnQOchu44sQzIpWUsqf-DeacaG-wpj-w-RsW3wJh9pHr9UOQw6fMGFqebw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05f05bf09f.mp4?token=LIRop9X3xZ50rcthPIo2ucCSh1OYcGczl1ulcnTHcu8di9MQCuj9ei4lw647dMi5dfCvEH7_QEDq18kugCv9x1-mxUSYWoxX2szLLorvgbak3VDLwF9v8LM_vug7WmES846YawQODljHNKEv_vm7RgORUX8F5jEGekERhO5tBxtOzlrsXNpzlKzgxW0viVQpyP09_JBNf0mP_V_AOsZ1MbvYf0qLmOcKA0tvGBMdj1L29ArPH829qRK63c_n39BhJDziYYfKkYUaGUOWOXfOB5zU9KJQlnQOchu44sQzIpWUsqf-DeacaG-wpj-w-RsW3wJh9pHr9UOQw6fMGFqebw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عصبانیت CR7؛ کشتی کریستیانو رونالدو با مدافع العین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/690364" target="_blank">📅 15:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690363">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
وزارت آموزش و‌ پرورش از افزایش بیش از ۵۰ تخصص جدید در رشته‌های کار و دانش و فنی‌حرفه‌ای خبر داد
مصطفی آذرکیش، معاون آموزش متوسطه وزارت آموزش و پرورش در
#گفتگو
با خبرفوری:
🔹
پارسال در شاخه فنی‌وحرفه‌ای بیش از ۲۴ رشته به‌روزآوری شد و در شاخه کاردانش نیز بیش از ۳۰ رشته جدید یا به‌روزآوری‌شده به تصویب رسید.
🔹
در سال پیش‌رو نیز ایجاد رشته‌های جدید در دستور کار قرار دارد و این رشته‌ها با توجه به نیاز بازار کار و با تعامل دستگاه متولی مهارت، بخش خصوصی و مؤسسات تولیدی و خدماتی طراحی می‌شوند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/690363" target="_blank">📅 15:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690362">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgvAiK_x-U0ZoZ_cXTUeYAsx4z3M5MeTNdSAN_9b9JGf_Hvg3HluCJhteBUsS3XGwVoZXSdv5gu5fJtMw99VRu77KYq2gEl4zZtYaAkJtEmehjU06jkojuUKr1Qi7mzGTcic6a8pkf8mDhI1VJ0c2V6UHE1NK2MtADi2a006BurBM1oMn0MeKFNy8zCqFqHFOg71qTqtzsAHb6KY1W95mpDeZUuFISI-JbnpnZiPTL6bTD9ldSghGICozjVIAxosmLaYOtUOf5ln-Paz8hpdIv3Rl6sv8KluS38bjBKC7wTNCIm1IgK5GQXgkGZK4X2y6bKnRtUPuYhj-aAnlhjKqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شمارش معکوس برای بازگشت پل شور به مدار تردد؛ پیشرفت ۹۲ درصدی با تلاش ۶ اکیپ اجرایی
🔹
مدیرکل راهداری و حمل‌ونقل جاده‌ای استان هرمزگان از پیشرفت ۹۲ درصدی عملیات بازسازی پل شور در کیلومتر ۳۶ محور بندرعباس - حاجی‌آباد خبر داد و گفت: با فعالیت ۶ اکیپ اجرایی و انجام بتن‌ریزی، بازسازی این پل در مراحل پایانی قرار دارد.
🔹
عباس شرفی با اشاره به تخریب کامل دهانه‌های سوم و چهارم پل دوم شور در این محور، افزود: با اجرای روند بی‌وقفه بازسازی این پل، هم‌اکنون پایه‌های آن آماده شده و پس از تکمیل تیرها در کارگاه، نصب آن‌ها در محل پروژه انجام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/690362" target="_blank">📅 15:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690361">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
کانال ۱۵ عبری: بن سلمان خود را در برابر حملات انصارالله تنها می‌بیند؛ در حالی که تأسیسات انرژی عربستان هر روز منفجر می‌شوند، آمریکا و اروپا هیچ کمکی نمی‌کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/690361" target="_blank">📅 15:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690359">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
سخنگوی نیروهای مسلح یمن: تأسیسات آرامکو در ینبع و پایگاه خمیس‌مشیط را هدف حمله قرار دادیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/690359" target="_blank">📅 15:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690358">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c22bf042b3.mp4?token=WHQjtTquJ7dSI0CiglVvcmCHgMlk_d1I9NsEmi3wYw75CKckJQpOchxpJzkFYmsijKjvdF_jen6PwniLtkqO5ZY1iczK2f8cokC6uP6sij1PXAetv2bCM08fhrxPQLU5TkP7oDYesGVC70baLLrhnytwsbQ6zxt4odQuSwJJZSIVmco_SV6pT5ju5FxMc_AX9SqhVMt9tgIf5t4qUrBbfP4y9CP7PP_dghIIyMZdIuLnY-VxEtkOqzl72uJDseAwSt4ltnSRBM8g0uHds5ZQ4uFap135a5kTZMYVgRm4MDQBMPjoTS97AGk7VgXhLdMpkJ8sBulzLwiYLGnwKDEjIj9QP4f2HUAZN768eRa-ranw-yncO6bllIb9FPTRRuncB5LmHqAQ9aHJydVjWodJiRQYLK-AItuzYsXXI85z690oltmGZKfXMwSN5ST14OuaSgtvjF0UPWBQxm27ZcoYsor-ojhQqkAOIeUqvBAwTDECXoS_HSuFUSIzCMjEOf0ur2Mg8CvTAMWlyJqAPtC-uapZVNZ8RJHxjxPYiwkxngwVOdfEDD6yy9xAFFNu9XbxlZlZi4M-tCtNXLiFheiS2r6__Vch3sj-Da6bwdQaqPIph78iCtb4OmW3E7SeM84AZXRbHfER_ncmvTKDL3jiPTVN-F2adcxYZtEJRgLW52o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c22bf042b3.mp4?token=WHQjtTquJ7dSI0CiglVvcmCHgMlk_d1I9NsEmi3wYw75CKckJQpOchxpJzkFYmsijKjvdF_jen6PwniLtkqO5ZY1iczK2f8cokC6uP6sij1PXAetv2bCM08fhrxPQLU5TkP7oDYesGVC70baLLrhnytwsbQ6zxt4odQuSwJJZSIVmco_SV6pT5ju5FxMc_AX9SqhVMt9tgIf5t4qUrBbfP4y9CP7PP_dghIIyMZdIuLnY-VxEtkOqzl72uJDseAwSt4ltnSRBM8g0uHds5ZQ4uFap135a5kTZMYVgRm4MDQBMPjoTS97AGk7VgXhLdMpkJ8sBulzLwiYLGnwKDEjIj9QP4f2HUAZN768eRa-ranw-yncO6bllIb9FPTRRuncB5LmHqAQ9aHJydVjWodJiRQYLK-AItuzYsXXI85z690oltmGZKfXMwSN5ST14OuaSgtvjF0UPWBQxm27ZcoYsor-ojhQqkAOIeUqvBAwTDECXoS_HSuFUSIzCMjEOf0ur2Mg8CvTAMWlyJqAPtC-uapZVNZ8RJHxjxPYiwkxngwVOdfEDD6yy9xAFFNu9XbxlZlZi4M-tCtNXLiFheiS2r6__Vch3sj-Da6bwdQaqPIph78iCtb4OmW3E7SeM84AZXRbHfER_ncmvTKDL3jiPTVN-F2adcxYZtEJRgLW52o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی یک تکه شیشه زیر پوست گیر می‌کند چه اتفاقی می‌افتد؟
🤯
#حواست_هست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/690358" target="_blank">📅 15:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690357">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ریابکوف، معاون وزیر خارجه روسیه: ایران و امارات به لطف قدرت بریکس موفق به حل اختلافاتشان شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/690357" target="_blank">📅 15:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690356">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ارز برای دارو نیست، اما بعضی چهره‌ها می‌خواهند واردات لوازم خانگی را آزاد کنند! / به نام برندهای کره‌ای، به کام اجناس بی‌کیفیت ته‌لنجی!
🔹
وزارت بهداشت می‌گوید کرونا از مرحله هشدار بالا عبور کرده، ولی اگر سری به داروخانه‌ها بزنید، نه خبری از واکسن کرونا هست، نه حتی واکسن آنفلوآنزا! اما انگار ارز کافی برای لوازم خانگی پیدا می شود!
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3245540</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/690356" target="_blank">📅 14:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690355">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ادعای رویترز : مقامات آمریکایی اوایل این هفته در عمان با حوثی‌ها دیدار کردند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/690355" target="_blank">📅 14:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690354">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e768c522.mp4?token=E7cL7Jv7vkazeh0z5G8VEqRcaqMoI2Sufpvo695PqB2GCAQDYfYZ5T-W2klvgX-PsKFjJjI_EUufHyp0AKiu60VX1YtvdpEMC6wPEROQtjb9NhjmuDTR_5H2rn1r5YwQO1i6mXwUaZNtEv6l6HV_XbfogK8LHxWqm9E_nY7qk-0u783VMeurP4apKjae2Swl7vdAzMN0QMyjg5hZT1bQ4ACj9FY8Do1mxnxqFrto2tk6RXEyoJDyeBlUXKmF24Z9ttQO5F8rnro-vPwLGCBaFbPL8PiKjRQdsTQn9O3gBeZcK0R8yW2fze0IwjT9UIOdB2veaA7t3H4LOIworoltbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e768c522.mp4?token=E7cL7Jv7vkazeh0z5G8VEqRcaqMoI2Sufpvo695PqB2GCAQDYfYZ5T-W2klvgX-PsKFjJjI_EUufHyp0AKiu60VX1YtvdpEMC6wPEROQtjb9NhjmuDTR_5H2rn1r5YwQO1i6mXwUaZNtEv6l6HV_XbfogK8LHxWqm9E_nY7qk-0u783VMeurP4apKjae2Swl7vdAzMN0QMyjg5hZT1bQ4ACj9FY8Do1mxnxqFrto2tk6RXEyoJDyeBlUXKmF24Z9ttQO5F8rnro-vPwLGCBaFbPL8PiKjRQdsTQn9O3gBeZcK0R8yW2fze0IwjT9UIOdB2veaA7t3H4LOIworoltbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی ۱۰ سال قبل مرحوم علامه علی کورانی رحمت الله علیه
قبل از ظهور
۱.سقوط سوریه
۲. اختلافات داخل ایران
۳.پیروزی یمن</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/690354" target="_blank">📅 14:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690353">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3905d8108d.mp4?token=PHPLoaaWjK2MBiDbeGu6vRHACgYTSJ54wGydPbQ_PxAFvlhKC9UE5snkbD1DuixySClcq-aXQcWGXnGTH8AbriweHPjGs_7AnwBe_Coy3kDAZUUN6eQZaB5nu01o2dCk_My5G96HZ5lTUrU_CQUPxyMgVsxuVDjGJfcII2cRNT5Fn0umRprjFVLgJNGXfj0QIMPMJDX33Ht6tdIQKs-G5pvNi0nR0aEeOcvbvJvdRSGpCdcaK5iHgHwOoLKKkOhXuUIlMHtE54lpt_uPCjWRcyilhaPdIfL3FA6nXfpSxYkX_ZxJo6C65Gkofrp1t8ug8EC3mJvrPaSFNnmdJZPiZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3905d8108d.mp4?token=PHPLoaaWjK2MBiDbeGu6vRHACgYTSJ54wGydPbQ_PxAFvlhKC9UE5snkbD1DuixySClcq-aXQcWGXnGTH8AbriweHPjGs_7AnwBe_Coy3kDAZUUN6eQZaB5nu01o2dCk_My5G96HZ5lTUrU_CQUPxyMgVsxuVDjGJfcII2cRNT5Fn0umRprjFVLgJNGXfj0QIMPMJDX33Ht6tdIQKs-G5pvNi0nR0aEeOcvbvJvdRSGpCdcaK5iHgHwOoLKKkOhXuUIlMHtE54lpt_uPCjWRcyilhaPdIfL3FA6nXfpSxYkX_ZxJo6C65Gkofrp1t8ug8EC3mJvrPaSFNnmdJZPiZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صورت‌های مالی فارس تایید شد/ تقسیم سود سهام ۶۰ تومانی به ازای هر سهم
🔹
صورت‌های مالی سالانه شرکت صنایع پتروشیمی خلیج‌فارس برای سال مالی منتهی به ۳۱ خرداد ۱۴۰۵ با نظر اکثریت به  تصویب مجمع رسید.
🔹
مجمع فارس همچنین به ازای هر سهم پرداخت ۶۰ تومان سود تصویب کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/690353" target="_blank">📅 14:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690352">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
رئیس‌جمهور: برای صیانت از معیشت اقشار کم‌برخوردار در مورد کالابرگ تصمیم قطعی گرفته شده و اعلام خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/690352" target="_blank">📅 14:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690351">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5b7f01aee.mp4?token=koKBz5mHHwUavMu0C-q5uonoFEHktzp31trxr7S6jgBtksem7rXN9xHec7rcHxlAcwquH2XRt2tKWOhGfuHAzsT8_CyUBF2u7YEcQ67J-h1eNTKt4wF0CN2ZNJ-SRctVanI9SWZFSdU31l1eNW8d-63tU_WPLy48Fix5wG1wmEwY4v1tDu_qktXPk9r3up-fwvu16f4doZHsnwO5g4CBbnTVaQzOgIIYqnW-AA4Y2o_4pyLsIiXhBdnrV_IqjDP1Zs78qHk3xuOyARG5rggeKX22yupVbredV3ByeNwwU7U1yldaBT029ujkEAjFyAg-R7twfr3guOxEMuZoeBfYpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5b7f01aee.mp4?token=koKBz5mHHwUavMu0C-q5uonoFEHktzp31trxr7S6jgBtksem7rXN9xHec7rcHxlAcwquH2XRt2tKWOhGfuHAzsT8_CyUBF2u7YEcQ67J-h1eNTKt4wF0CN2ZNJ-SRctVanI9SWZFSdU31l1eNW8d-63tU_WPLy48Fix5wG1wmEwY4v1tDu_qktXPk9r3up-fwvu16f4doZHsnwO5g4CBbnTVaQzOgIIYqnW-AA4Y2o_4pyLsIiXhBdnrV_IqjDP1Zs78qHk3xuOyARG5rggeKX22yupVbredV3ByeNwwU7U1yldaBT029ujkEAjFyAg-R7twfr3guOxEMuZoeBfYpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عضو ارشد انصارالله در واکنش به خبر سرنگونی اف-۱۵ سعودی‌ها: دیگر بدبختی‌ها به‌ صورت جداگانه بر سر دشمن سعودی نازل نمی‌شوند؛ یکی پس‌ از دیگری به‌ سراغ او می‌آیند
🔹
رسانه‌های خبری از سرنگونی جنگنده F۱۵ عربستان توسط نیروهای ارتش یمن (انصارالله) خبر دادند
🇮🇷
…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/690351" target="_blank">📅 14:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690350">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ادعای رویترز : مقامات آمریکایی اوایل این هفته در عمان با حوثی‌ها دیدار کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/690350" target="_blank">📅 14:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690349">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUfcRg7gHpJBwrwJdfV8CHt6zmxBgufPyBC9RK20uq87TX3zsmx3KoVkM97z0luiVObmyZU_U0R99b59D45-rkYJgyqmSBaw9ZHCl6OPZ7DDpHPM_28qLYlCtvaMtM1NqqXrX0mKWlBta750VynwmEb31S6JApgzAYqL_2EzM6N9xC8IahH83Knn9V0qdM_o-oX56KseSBiUasvK0MWjmN7ZlHOvZTPhYz7PegOCWZDI-xbTt9o_HS1Zh8Zta1JBt5klek7IlSwBGJeq3Xb5j_wRIKdNYgHlG7SXHX0pihj76ioryx-h8mtvxZXx3w4K9zVOCd4qILD4ZS1SOeSZfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند ۱۰ ساله بارش در ایران
🔹
آمار مرکز ملی خشکسالی نشان می‌دهد  بارش‌های کشور پس از اوج‌گیری در سال‌های ۹۷ و ۹۸، وارد دوره‌ای خشک و کم‌بارش شده است.
🔹
میانگین بارش سالانه کشور از اوج ۲۹۱.۶ میلی‌متر در سال ۱۳۹۷ به ۱۹۴.۵ میلی‌متر در سال ۱۴۰۴ رسیده است.
🔹
در این بازه ۱۰ ساله، بیشترین افت بارش با ۳۶.۶- درصد در سال ۱۳۹۶ و بیشترین رشد با ۲۴.۱+ درصد در سال ۱۳۹۷ ثبت شده است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/690349" target="_blank">📅 14:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690348">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/191ba4e16b.mp4?token=UBVdpfpjBiixybgUfYXn6kXR51kttL1UH17oM37HmeMMidvUmZe9Zj5vqvBTHz5VAVvGvR5VCbwirUFqJLICpH-UiSDz88Nd1heFV0_sesKC6XLCHnWd2BfeltCw8yYEg7Cr93FflPapPXwN8fTLVkHUJUcdkgEhEA8k_HleGbNTwqM0QSkfGXhSl07Kw3fxDwrEQXWzWk2mWgKN-FT_4sfgew-dTvIfCli2hrjVw5153u3ig85afOXiDIZ9A-jGWi3wZ7u_zx7goOadRpy01z4ehZ69-u9NfSyJshViNTECYx9cwv1zwIkdzj6MKdoms3xRIaAmxv9c5ExCpO8u1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/191ba4e16b.mp4?token=UBVdpfpjBiixybgUfYXn6kXR51kttL1UH17oM37HmeMMidvUmZe9Zj5vqvBTHz5VAVvGvR5VCbwirUFqJLICpH-UiSDz88Nd1heFV0_sesKC6XLCHnWd2BfeltCw8yYEg7Cr93FflPapPXwN8fTLVkHUJUcdkgEhEA8k_HleGbNTwqM0QSkfGXhSl07Kw3fxDwrEQXWzWk2mWgKN-FT_4sfgew-dTvIfCli2hrjVw5153u3ig85afOXiDIZ9A-jGWi3wZ7u_zx7goOadRpy01z4ehZ69-u9NfSyJshViNTECYx9cwv1zwIkdzj6MKdoms3xRIaAmxv9c5ExCpO8u1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با همین گل‌های‌ ریز می‌تونی جیب‌هات رو خوشگل کنی
🌼
#فوری_استایل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/690348" target="_blank">📅 14:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690347">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d9b3c3589.mp4?token=AGSwEXMDyDZdiZngtCp57rPDf-CQBBJQ-yNuXrd9U9gL6M9IWEOoQYsq1tq_OyBcPaTKQDv-UTlSPDeLWrHRq_hVHXnDGxlNWzLD7nrvatXuGAiCAFj-0V05ZipVe-Y4XBjH5ywQEQOjsdjbrJo-DGTIdw0D39P3yQwdUmVXZH9yVnkP5YDqh9pYrRtv62HoMOoymKZCW3fqCFtUh5oKA1bvd3lrFM1JtwACuSNO4So-1TIzzOpARh-n68GoYzmVWFaTqN4OUB5mG9OvtpU_aEsFGItF4p3M-fdSX7_CG21OSdaCZK7QMdLo3Nfu6mQl7TSE9KLeH_jO20vcMwUv4lMx2uDDbtNYElNxM-3WGbXyUzxRw6dHFs14gYsjbHUK_fq1RO5f9tyOJWLOvz4E9mSP9uavPz1RjvM_Vl2vi_zlrGxkijOqkpXiYBWjHOTgTDR9eR8EcRfb0hQudoZrJNYzn-VPaqIglE8DaofXXCc1gVw9ZtM8aSJfqNgnwj1AuxzhhyDAGWTuubW0YNzzuYPeeKJ1FCNtOQJsdKHu0vVHKQr55RJ_gDKmbpYDTXPwO5CoJGJI2Z43Dzo6XDtZQaGr9Kc14ahypkqnHfSPryoLWSulNY6NZRya0L9hGVFdh-hoK6weytHFdE7B-ps0OD1DtfEx7Nisjb2qr5OEsXM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d9b3c3589.mp4?token=AGSwEXMDyDZdiZngtCp57rPDf-CQBBJQ-yNuXrd9U9gL6M9IWEOoQYsq1tq_OyBcPaTKQDv-UTlSPDeLWrHRq_hVHXnDGxlNWzLD7nrvatXuGAiCAFj-0V05ZipVe-Y4XBjH5ywQEQOjsdjbrJo-DGTIdw0D39P3yQwdUmVXZH9yVnkP5YDqh9pYrRtv62HoMOoymKZCW3fqCFtUh5oKA1bvd3lrFM1JtwACuSNO4So-1TIzzOpARh-n68GoYzmVWFaTqN4OUB5mG9OvtpU_aEsFGItF4p3M-fdSX7_CG21OSdaCZK7QMdLo3Nfu6mQl7TSE9KLeH_jO20vcMwUv4lMx2uDDbtNYElNxM-3WGbXyUzxRw6dHFs14gYsjbHUK_fq1RO5f9tyOJWLOvz4E9mSP9uavPz1RjvM_Vl2vi_zlrGxkijOqkpXiYBWjHOTgTDR9eR8EcRfb0hQudoZrJNYzn-VPaqIglE8DaofXXCc1gVw9ZtM8aSJfqNgnwj1AuxzhhyDAGWTuubW0YNzzuYPeeKJ1FCNtOQJsdKHu0vVHKQr55RJ_gDKmbpYDTXPwO5CoJGJI2Z43Dzo6XDtZQaGr9Kc14ahypkqnHfSPryoLWSulNY6NZRya0L9hGVFdh-hoK6weytHFdE7B-ps0OD1DtfEx7Nisjb2qr5OEsXM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تغییرات بزرگ سیستم عامل جدید آیفون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/690347" target="_blank">📅 14:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690346">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تاکنون طرحی در خصوص خروج از NPT در مجلس تنظیم نشده است
محمدرضا محسنی ثانی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
با توجه به اقداماتی که علیه ایران در موضوع هسته‌ای انجام شده، از جمله فعال‌شدن مکانیسم ماشه و ممانعت از حضور هیئت ایرانی در وین، عملاً اعتبار NPT از بین رفته و دیگر چیزی به نام NPT برای ایران مطرح نیست.
🔹
ایران همکاری‌های خود با آژانس بین‌المللی انرژی اتمی را نیز بر اساس مصوبه مجلس متوقف کرده است.
🔹
در کمیسیون امنیت ملی به‌صورت غیررسمی درباره خروج ایران از NPT بحث‌هایی انجام شده اما تاکنون طرح یا لایحه‌ای در این زمینه تنظیم نشده و در صورت تصمیم برای خروج، تصمیم نهایی با مجلس خواهد بود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/690346" target="_blank">📅 14:07 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
