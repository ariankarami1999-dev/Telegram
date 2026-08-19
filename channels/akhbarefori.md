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
<img src="https://cdn4.telesco.pe/file/OaEZLafXy-CIBO_p8ktSRZ6anGhBcNNoXmZeA9oefFnC02loEluXwo2Q_0FQ2RJDOR9U60pGL4IuUSuG7ABH8kaGg6kUj63O0xVHXz0Zc2bLcMtGSDu8AnUMUOCfuNZHmmYGDaDraEqnr7Wc6yRJf8ws2WcUy1_Dec_xiPfZtBfwnrqHNvXuCzm89D6gqICNoDzSrLeLq1fqosAbLDwPLSbtbBr6SlAsQe8f6D16GOxCOIWQCjtEH36aiPHrTVljIeZRenkmrcgnk9srSTW0THMB5Qtr9y-MFtt7xkwog1ZKTjm1oRowYXgV1tlpbtxQRMPw4NFC91LWOlwXfChlhQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.08M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 21:50:23</div>
<hr>

<div class="tg-post" id="msg-682639">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkD8U28s3gR891eauOwdQY2-YMfKcwn8OmG1TtgsS3xh3EESfYG9EMP7eMYjzenCpkWkWO-1zSfrszFa5qswwL7YoMZAuhrvQMcVqdTQmkWeANjaCEuVFiFtYh8ugAknkNd_sGFoEVrWL919bGrsjq2in3H_e4s9ucOyG33qYNUXkGZ28pmcF6MNxc3UFMu5I0QnNhQZthN4AtlWoDm5m8zF1I6UyLsh2sHKxTENKugueQHlregW_LS_-jdanx_OXN_N2LPH4P6QW7Qctp6U1GgcVlDco1LpsdkHtzw08SIKHE8UhtWr90P5DcKEOxAxYqFSujgVOj6PNofeTIfMDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل چهارم پرسپولیس به استقلال خوزستان توسط شهرآبادی در دقیقۀ ۹۳
🔹
پرسپولیس ۴ _ ۱ استقلال خوزستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/akhbarefori/682639" target="_blank">📅 21:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682638">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ارتش تروریست آمریکا از ادامه تعرض به کشتی‌های مربوط به ایران خبر داد
سازمان تروریستی ستاد فرماندهی مرکزی ایالات متحده دقایقی پیش در خصوص محاصره دریایی علیه ایران ادعا کرده است:
🔹
از زمان آغاز تحریم‌ها علیه ایران، ۶۵ کشتی تجاری را منحرف، ۳ کشتی را از کار انداخته و ۲ کشتی را توقیف کرده‌ایم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/682638" target="_blank">📅 21:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682637">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
اذعان وقیحانه نفتالی بنت بر تداوم مسیر جنایت و اشغالگری: تا خلع سلاح کامل حماس از «خط زرد» عقب‌نشینی نمی‌کنیم
نخست‌وزیر پیشین رژیم صهیونیستی:
🔹
تا زمانی که حماس کاملاً خلع سلاح نشود، حتی یک میلی‌متر از «خط زرد» عقب‌نشینی نخواهیم کرد.
🔹
آزادی عمل امنیتی خود را در سراسر غزه حفظ می‌کنیم.
🔹
قطر و ترکیه حماس را تقویت می‌کنند؛ باید مصر جایگزین آن‌ها در مدیریت غزه شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/akhbarefori/682637" target="_blank">📅 21:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682636">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
زمین‌لرزه‌ای به بزرگی ۴.۲ ریشتر، شامگاه امروز حوالی شهرستان گیلان‌غرب در مرز استان‌های کرمانشاه و ایلام را لرزاند
🔹
تاکنون گزارشی از خسارت‌های احتمالی این زمین‌لرزه اعلام نشده است.
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/akhbarefori/682636" target="_blank">📅 21:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682635">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f21674bfd7.mp4?token=JZcq84SogyS9wwyFUIdmKjWwKh-K3kQJ2ahKOXQ8icIeBBzImblHcuuIx7pPNrOcgtzunBgxJPqTjFRAA5AyCe4OoQEHJARnUatXcarVhHvmye_50ZyNT1-kbHvePars-llesTHghWjSM3sH7CeknHPKeCqotTBa4rvS9fej110VFnk0ZKVuGhKLS78VDN09yvMNVriA7huGwaNI2yJ9-r7ox9U1u2OF5ywBUs6NppmpFGgKAtvyx6hEXQyTlulgxtu_3GOnvD5S0AdYwHtNIfEX76dshBljMF556m-P2yaeglccsrEbwZ88F_8TWvqXGzoG8D7h_jEIT0zP3gomcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f21674bfd7.mp4?token=JZcq84SogyS9wwyFUIdmKjWwKh-K3kQJ2ahKOXQ8icIeBBzImblHcuuIx7pPNrOcgtzunBgxJPqTjFRAA5AyCe4OoQEHJARnUatXcarVhHvmye_50ZyNT1-kbHvePars-llesTHghWjSM3sH7CeknHPKeCqotTBa4rvS9fej110VFnk0ZKVuGhKLS78VDN09yvMNVriA7huGwaNI2yJ9-r7ox9U1u2OF5ywBUs6NppmpFGgKAtvyx6hEXQyTlulgxtu_3GOnvD5S0AdYwHtNIfEX76dshBljMF556m-P2yaeglccsrEbwZ88F_8TWvqXGzoG8D7h_jEIT0zP3gomcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یحیی سریع: نیروهای مسلح ۹ عملیات موشکی و پهپادی علیه تأسیسات نفتی عربستان انجام دادند
سخنگوی نیروهای مسلح یمن:
🔹
از ۲۰ ژوئیه تا ۱۹ اوت، نیروهای یمن با هدف‌گیری مستقیم ۸ نفتکش (۵ مورد در دریای سرخ و ۳ مورد در خلیج عدن و دریای عرب) و مجبور کردن ۴۸ نفتکش دیگر به تغییر مسیر و بازگشت، عملاً محاصره دریایی عربستان را اجرایی کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/akhbarefori/682635" target="_blank">📅 21:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682634">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
پزشکیان: مذاکره به معنای تسلیم نیست؛ ملت ایران و نیروهای مسلح با ایستادگی در برابر حملات، دنیا را شگفت‌زده کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/akhbarefori/682634" target="_blank">📅 21:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682633">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09e5061375.mp4?token=D1Ohnc1Dmv4ImSJtys_sYWpscwF_CaUjmqLdJ2IGVoE6GTv_QuHP6SvYazfoQkCYl0UbrSP-8Uk_vqrY8C8yjMx6fMaSsDdzYh7DRjHYpT2oELMXRlfoUQNrvtuE05ZsfLrOHM_A3nxUXVdCGEwTKkKfGuCy4GN7IB_Win6qm6dOWxwz1BUwMH03hqQX-ZCgSjdqU4n5yfulTuEuBnmqK1nQMM08p5UZZBdZ0Qk6OY56TfBc1IJhHGljzJj06VQYeXDe1R9b7rpBVpOhAoaX8RZVVKTui1d9NusvXpPE1S2Ow6scl0GCKsLqaSfR5MWJvJ9esxpRuVDWTeBmvEeugg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09e5061375.mp4?token=D1Ohnc1Dmv4ImSJtys_sYWpscwF_CaUjmqLdJ2IGVoE6GTv_QuHP6SvYazfoQkCYl0UbrSP-8Uk_vqrY8C8yjMx6fMaSsDdzYh7DRjHYpT2oELMXRlfoUQNrvtuE05ZsfLrOHM_A3nxUXVdCGEwTKkKfGuCy4GN7IB_Win6qm6dOWxwz1BUwMH03hqQX-ZCgSjdqU4n5yfulTuEuBnmqK1nQMM08p5UZZBdZ0Qk6OY56TfBc1IJhHGljzJj06VQYeXDe1R9b7rpBVpOhAoaX8RZVVKTui1d9NusvXpPE1S2Ow6scl0GCKsLqaSfR5MWJvJ9esxpRuVDWTeBmvEeugg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول استقلال خوزستان به پرسپولیس در دقیقۀ ۶۴
🔹
پرسپولیس ۳ _ ۱ استقلال خوزستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/682633" target="_blank">📅 21:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682632">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfnNJQoDVuW7kpgjbzVdAqf5EKj6HfEevoRRlfgC5LStgRsxR9hu-OXfGGLZay4d3x3nYKknQMvlURAdOXafMB2QVenjXXtfIw1lQmLlNHqVBUiqXaVvEw9hJRMCptVMczEV_-FWEba_surnNS4jpOhBT8_XWbaOdi7Vwu8PkZ4x0FoSUxYwWlzjaCO1sPMLN1Opmp4yheuvUuXq8wi2H8LjkmEYu6VR6bXOSpLwPMRTlPJ4uP4JKjaLVE0leacVGK4hLkmo1hIergsqgQB8l4WtYOMn4pz8eNHosFJGqSB7SRcPl_8Ffcd8Urbnz3IoyRiZa4FORB-iKe2SgVMfjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمسخر رویای ترامپ درباره تنگه هرمز توسط استاد دانشگاه استنفورد
مایکل مک‌فال سفیر پیشین آمریکا در روسیه در واکنش به رویاپردازی‌های ترامپ و تغییر نام تنگه هرمز روی نقشه به عنوان یکی از دارایی‌های آمریکا:
🔹
این دیگر واقعاً دیوانه‌وار است!
🔹
ما دیگر کشوری جدی نیستیم؛ چه رسد به اینکه قدرتی بزرگ و مورد احترام در جهان باشیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/682632" target="_blank">📅 21:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682631">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83e3a6112e.mp4?token=SkTU7H-NIID6aWzUSVg24xFO9-nEOUQIBEoOu0AijPB2lEqZN-5mPh-X-ytDuXWyOtKwsljVLKC51sdXMewZn8QTlpHxwdSDKZKvoUs-fiFqoz5Z4I-GLfTwPq3fAwB1Foa9gip4JRL90ch1jr0YX-JI3O7CUNsWAKj8Yi-0Z3p7ozhtZpML6Ruj7RIy9smjsubRB2SzbA2Ors6r3W8kkXEZsLzitiu9kVLDHm2GKsrztUpkF8JTc1JuAT95b8vOCjJvPk0gFmVrL9WQRP7Tim2YMF3g9sB6IzNmOGqvsaSGfi95SB0fQGVMHat_wVC9V78V40JDJaNxjG2F-aI37YsJwHQjC6sK4o8ewnX7_zkxpO_IdAd9wDkWpmNsrAsW3GEpbt8l-Q3PGOPwHs7zeChbtASmO4eQbd9U81J290tuuiaYPhwPHGASyOjO5u9AM15lKyYJH7RPXPktNeleKIbinl0gbsWvsmer_935CywBWoDHy_ZNeMEi2nx0R2Z2cfaK518FVLhiP2JlWbQXc7NRefzbEWOvmtugpt57csnLAZu94KYhXhWYnGPXe6HTgyZT3MUhqdw4HPkJSq-6269jSTUUP77AybhSp7SLTswqOVIA1RgPFBZB4qXpyEq9sf7rLh1p6klAMi2uMugZKCzTvbI5pg1KJXbouNBX244" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83e3a6112e.mp4?token=SkTU7H-NIID6aWzUSVg24xFO9-nEOUQIBEoOu0AijPB2lEqZN-5mPh-X-ytDuXWyOtKwsljVLKC51sdXMewZn8QTlpHxwdSDKZKvoUs-fiFqoz5Z4I-GLfTwPq3fAwB1Foa9gip4JRL90ch1jr0YX-JI3O7CUNsWAKj8Yi-0Z3p7ozhtZpML6Ruj7RIy9smjsubRB2SzbA2Ors6r3W8kkXEZsLzitiu9kVLDHm2GKsrztUpkF8JTc1JuAT95b8vOCjJvPk0gFmVrL9WQRP7Tim2YMF3g9sB6IzNmOGqvsaSGfi95SB0fQGVMHat_wVC9V78V40JDJaNxjG2F-aI37YsJwHQjC6sK4o8ewnX7_zkxpO_IdAd9wDkWpmNsrAsW3GEpbt8l-Q3PGOPwHs7zeChbtASmO4eQbd9U81J290tuuiaYPhwPHGASyOjO5u9AM15lKyYJH7RPXPktNeleKIbinl0gbsWvsmer_935CywBWoDHy_ZNeMEi2nx0R2Z2cfaK518FVLhiP2JlWbQXc7NRefzbEWOvmtugpt57csnLAZu94KYhXhWYnGPXe6HTgyZT3MUhqdw4HPkJSq-6269jSTUUP77AybhSp7SLTswqOVIA1RgPFBZB4qXpyEq9sf7rLh1p6klAMi2uMugZKCzTvbI5pg1KJXbouNBX244" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توصیه پدرانه رهبر شهید به جوانان و نوجوانان کشور: از کنکور نترسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/akhbarefori/682631" target="_blank">📅 21:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682630">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
پاکستان کاردار آمریکا را احضار کرد
🔹
وزارت امور خارجه پاکستان در اقدامی دیپلماتیک، کاردار سفارت آمریکا در اسلام‌آباد را برای ابلاغ اعتراض رسمی دولت این کشور به اظهارات مقامات آمریکایی فراخواند.
🔹
این احضار در پی توصیف «جیمز وکر»، سفیر آمریکا در هند، صورت گرفت که در اظهاراتی جنجالی، منطقه کشمیر را «بخشی از خاک هند» خوانده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/682630" target="_blank">📅 21:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682629">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxZMQbAdrjedR0wHsFrm-Y8AHgMFj9Kr1WKZfM-On0L3D9KxfzEAuqWQwnaal_CqL0Stj-rnbXmsEoWzMrHGoPQnFxn2gJPkEUB4Crtt8OXXfkFYJFKenuKsvSh-XfHidd5JhPyzzojAkhDbZfv-IK3ulglF2maK8RXmGv0SkL0bwcOvrQktxCtEKf-ZrHLlQhCoxcnKgHI5ElLRJsAC9MwQK0Jehi3Qd3dOfUXjveqU0JCLEh0zLvFsAFGjPH9naw1mNCT7lYb7s69pAYbDvhk2t9QlB-6eevS1tOgMV-q1ajdP8qBwz00hKPHYxqJHMjVy_jIuuvRiUMU-uJQRdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس معناداری که قاليباف منتشر کرد
🔹
رئیس مجلس با انتشار تصویری در اکانت خود به زیاده‌خواهی آمریکایی‌ها در خلیج فارس واکنش نشان داد.
🔹
این تصویر که قابی از نقشه خلیج‌فارس و تنگه هرمز را نشان می‌دهد، به‌نوعی بیانگر تسلط ایرانی‌ها بر تنگۀ هرمز و خلیج‌فارس است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/682629" target="_blank">📅 21:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682628">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ادعای فرستادهٔ ترامپ در امور سوریه: دیروز یک قدم با درگیری ترکیه و اسرائیل فاصله داشتیم!  توماس باراک، نمایندهٔ ویژهٔ رئیس‌جمهور آمریکا در امور سوریه:
🔹
ما دیروز تنها یک قدم با رویارویی نظامی مستقیم میان ترکیه و اسرائیل فاصله داشتیم. حملهٔ هوایی اسرائیل…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/682628" target="_blank">📅 21:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682627">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRDcBGnqkSgBv5tFHdraDDIfwgcjLokrvZd2QcN_GMP4ued3L1v5HOireifcBViC5mtzubZIDlz61GRLaj42-PLJdhXKo5RK0kfRc3tIivHu4ZwZ8TcltcTIotjAGC18Ue8J1JfWGEmZQ1MI3NwzTjI_4CTFofv02c4o8pIP9IECI_5TmmuTIkD5mRjSYbvg-uDxcASxDPnwwqHjwkqkgXtXbQVaXHmUsAI30iLtFJMjcFsqryv75U8EHlIwlBws8pUkivvwcQI8AUCYv-ttgJ1ut2saf7XP_nDxTXvtbcmfNLOCYAul07-wFARv-2KM4qDy0g_ptTWC11LpoezIGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۷۳ سال پس از یک خیانت به مردم / پشت پرده حادثه ای که باعث جنگ ایران و آمریکا تا امروز شد
🔹
چرا ۲۸ مرداد رخ داد؟ آیا این حادثه ضروری بود یا امکانی؟ آیا اگر مصدق و شاه اقدامات مرتکب شده را مرتکب نمی شدند، این کودتا رخ می داد؟
داستان روزی را بخوانید که آمریکا را از چشم ایرانی‌ها انداخت
👇
khabarfoori.com/fa/tiny/news-3238697</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/682627" target="_blank">📅 21:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682626">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1473988dd2.mp4?token=c6js8eLl_b1eCPaOAHpZE9Ica9KFISYC1yuyd8oSwAbaFQkLGD-4pQitNmD9349FNqMZDkxLGMG8_tFSrlYM-FAaiNv3n5AuuqL8epX4Z-c0duf-WIT4ambj3ny_uEePamZnTGWq61RydrOAcoAyKpuExQKOXtTUE_svjocRxI2ehthOuqn_HtjVsqMJ1P7P7H7_iBjRf9YCAr30BX21aqjaRMjDelmLV3P7BznNBxrij7L3vfgcX-hZXiOgZUNGElA6z-oYyACTEKmp05OjFNGDqXBel-lTlRvJjoAfvXQOyh5nEewyfXUHiUWY9HzMrM9veNqXyU54kfQlECH5kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1473988dd2.mp4?token=c6js8eLl_b1eCPaOAHpZE9Ica9KFISYC1yuyd8oSwAbaFQkLGD-4pQitNmD9349FNqMZDkxLGMG8_tFSrlYM-FAaiNv3n5AuuqL8epX4Z-c0duf-WIT4ambj3ny_uEePamZnTGWq61RydrOAcoAyKpuExQKOXtTUE_svjocRxI2ehthOuqn_HtjVsqMJ1P7P7H7_iBjRf9YCAr30BX21aqjaRMjDelmLV3P7BznNBxrij7L3vfgcX-hZXiOgZUNGElA6z-oYyACTEKmp05OjFNGDqXBel-lTlRvJjoAfvXQOyh5nEewyfXUHiUWY9HzMrM9veNqXyU54kfQlECH5kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم پرسپولیس توسط سرگیف
🔹
پرسپولیس ۳ _ ۰ استقلال خوزستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/682626" target="_blank">📅 21:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682625">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اقدام غیراخلاقی برخی شرکت‌های پیمانکاری: مزایای کارگران را به عنوان سود خودشان دریافت می‌کنند
هاشم خنفری پورجعفری، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
بین یک میلیون و ۳۰۰ هزار تا یک میلیون و ۵۰۰ هزار نیروی شرکتی پیمانکاری در کشور داریم که بخشی از آنها از طریق شرکت‌های پیمانکاری با دستگاه‌های دولتی همکاری می‌کنند و ساماندهی وضعیت آنها در حال پیگیری است.
🔹
شرکت‌های پیمانکاری حداقل حدود ۱۰ درصد از مزایای نیروهای شرکتی را به عنوان سود خود دریافت می‌کنند و این مبلغ می‌تواند به جای واسطه‌ها به رفاهیات و مزایای کارگران اختصاص پیدا کند.
🔹
در برخی قراردادها پیمانکار برای اینکه در مناقصه برنده شود قیمت پایین‌تری پیشنهاد می‌دهد و بعد مجبور می‌شود از مزایا، اضافه‌کاری و رفاهیات کارگران کم کند تا قرارداد برایش صرفه اقتصادی داشته باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/682625" target="_blank">📅 21:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682624">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d27502e1.mp4?token=IYnRWi1ZZxNRo8aNtirULQzCKyXmGIfco9BArnmEpkiHoKNcB8r0QoMOP3gfS9QyOu3I6lzxVuH8Om_g2aTbFqfbOrTA_WqiH7F2ys3_kCwMCMaET22fo8SbMkNDl3wH3ExCBtUrJ1GI17A-J5ByHxffHAZ53eD08VdHDvRwevDZGXdE5Zrx2GEAAo9Ez1Xf7LngMXgCP4JHxTOV9oHpgmAs9LfCE8RJPc9ivr87T1cP_noRIbPbFqzUtxy62hoEjmT8EverUpo-iFTj48LHSLpLugvK3Ziy-TgHd5tURXnylhmBteK6m_SwzApUOnB-IUYz1fYlY5dGwp-idr9Nng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d27502e1.mp4?token=IYnRWi1ZZxNRo8aNtirULQzCKyXmGIfco9BArnmEpkiHoKNcB8r0QoMOP3gfS9QyOu3I6lzxVuH8Om_g2aTbFqfbOrTA_WqiH7F2ys3_kCwMCMaET22fo8SbMkNDl3wH3ExCBtUrJ1GI17A-J5ByHxffHAZ53eD08VdHDvRwevDZGXdE5Zrx2GEAAo9Ez1Xf7LngMXgCP4JHxTOV9oHpgmAs9LfCE8RJPc9ivr87T1cP_noRIbPbFqzUtxy62hoEjmT8EverUpo-iFTj48LHSLpLugvK3Ziy-TgHd5tURXnylhmBteK6m_SwzApUOnB-IUYz1fYlY5dGwp-idr9Nng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط مارشال‌های آمریکا از بالکن به پایین حین تمرین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/682624" target="_blank">📅 20:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682622">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baXxBzg8LtfYFVJ0m9CdaKa60LfgCQZeIXLl6F4CjdSe-LPUOObS6vGXqa50MMEyA9g6M33kd703NLwYDsPh3SUkwmSU8CTbrvy1x2KGYxzKUGpXF67TE7tyhvtvz9QhkHN5uRdEjmYsiLnejkgBHGfOB1Y4kV_FKwdlmT4HOR-QL0LrDgL4-CEIPH55fuxSOgJyLBqCOeF5cxPVdBGxofLkto4iRkGaLJ6DOuHXYeD1sTxYymRHYoUmL3uuMYF22WgRy5gOBoW8LyzM-fFOjhqRNUTgPZ7aKaf-qaMnkRxajlFTWlFkd0QK4wAlaCWbyfq256O5Mh_lCwj8Hhud3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد ‌عجیب ارزش بیت‌کوین
🔹
فقط در ۵۰ دقیقه  ۴,۴۰۰ دلار جهش کرد و برای اولین بار در بیش از ۲ ماه گذشته به سقف ۶۹,۷۰۰ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/682622" target="_blank">📅 20:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682620">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4752033f1.mp4?token=E546ABjEc_ZGR6LLB4FEwHQG5rGCzAk4NWKS9SsrH3xlCluBABX3DfF6LMbjRwjsItJkHTq8UqMDpblkbwuzftqti-xvNti3lrKAciIq8jZpDdB2VFXgZzNgIErYPFchVC7aTi7FUcB1EyqkdPMrhFuAM9rJ8PgldY9covCTpxy2-wH58urS7bGTAMc3GPbFg1rk3XLON060IhSiWxPOSOzrvD_XYmTrhJ-XGAUaS_jrqvGGMNkvZhXP_PWxCWkhvrqT_Rj1GU_1-krOZNblgNCdeyAvAqCO7PiV-63dHQTSoyPDtZqJ2PMNzDioLdORbPoqQ5pkChRlFjmRSOfonA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4752033f1.mp4?token=E546ABjEc_ZGR6LLB4FEwHQG5rGCzAk4NWKS9SsrH3xlCluBABX3DfF6LMbjRwjsItJkHTq8UqMDpblkbwuzftqti-xvNti3lrKAciIq8jZpDdB2VFXgZzNgIErYPFchVC7aTi7FUcB1EyqkdPMrhFuAM9rJ8PgldY9covCTpxy2-wH58urS7bGTAMc3GPbFg1rk3XLON060IhSiWxPOSOzrvD_XYmTrhJ-XGAUaS_jrqvGGMNkvZhXP_PWxCWkhvrqT_Rj1GU_1-krOZNblgNCdeyAvAqCO7PiV-63dHQTSoyPDtZqJ2PMNzDioLdORbPoqQ5pkChRlFjmRSOfonA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم پرسپولیس به استقلال خوزستان توسط علیپور در دقیقۀ ۲۰
🔹
پرسپولیس ۲ - ۰ استقلال خوزستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/682620" target="_blank">📅 20:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682619">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryjjUPqw-VKFeLulTvmXf6XXvroQPrUh_3xvQAtXKDbNTvxVBBCcD2OA90E5ydfklets81EgVPn-tsRzn9WUuqVPrpaf3FCpxtQ5jOEJoq25SndZa4CJv9YleziSngJOshoVJNwmZLkzpRNvUDmxUr8R1BOpWUz-odOG5l-VZsQSfILS7slqcKSdvyOjdpABZlPneO9gc7HC4iurgySUIx-l_UfAxGDE36HgAxTcQEDQvP53UO-FbIMg8_ShynJWcD4fgIZE87eNDGq8XpzC4A6t-hVfRXQSYjoDbGPOAsIXTyNGK-P6flVaSZwJejHQQwGeuhRw6nOi2X9nQtPLsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«گنجینه نوین» اقتصادنوین؛ اولین تلاقی هنر و اقتصاد در ۵۰ سال اخیر
🔹
همزمان با بیست‌وپنجمین سالگرد تأسیس بانک اقتصادنوین، نمایشگاه «گنجینه نوین؛ گزیده آثار گالری نوین» در موزه هنرهای معاصر تهران برگزار شد.
🔹
در سال ۱۳۷۶ خرید آثار هنری توسط وزارتخانه‌ها و بانک‌ها ممنوع بود و این ممنوعیت در سال ۱۳۷۷ با تلاش‌های انجام‌شده برداشته شد.
🔹
در اوایل دهه ۸۰، بانک اقتصادنوین که نخستین بانک خصوصی کشور بود، اولین مجموعه‌ای بود که به شکل جدی به خرید و حمایت از آثار هنری روی آورد⁦.⁩
🔹
در این مراسم با حضور یدالله کابلی، چهره ماندگار خط شکسته ایران، فریدون فرمان‌آرا و علی موسوی‌زاده، قائم‌مقام بانک اقتصادنوین، از اثر خوشنویسی کابلی با عنوان «با شما نوینیم» رونمایی شد؛ اثری که یدالله کابلی آن را برای بانک اقتصادنوین خلق کرده است⁦.⁩
⁦
اطلاعات بیشتر:
https://www.enbank.ir/s/mfa9py</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/682619" target="_blank">📅 20:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682618">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9956a46472.mp4?token=BaaI3VohrflnTr3DpUCMvWnebbkkVmqpYunLIz5xsRVd45oZdnJGMna_pDJwjYLStwI5EOH-Ubl25KBew9latQH03-_fK9ARjnFGFmAKNQlhIbsSDQtXogXs3dy1biifcPrtTfkDGSEl0Cb2mucXpuv5henElmPlI69IEq5F8vpxRVgcZESUXsbuGM2BA2r10JOdUQjG8JBL9JkZ4eovIsbVGNpJ-8cLLeu0H0VpKK2kxcEdM9MgqWtbdjjaEmiofdrmkoO-kDuPr6ZZ5u4srmOMDr2krM09RpXs9P9DazAWXE-mLAD-nWlcsEAdaLnc9oHUONvFxbnpGYDKDz6SkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9956a46472.mp4?token=BaaI3VohrflnTr3DpUCMvWnebbkkVmqpYunLIz5xsRVd45oZdnJGMna_pDJwjYLStwI5EOH-Ubl25KBew9latQH03-_fK9ARjnFGFmAKNQlhIbsSDQtXogXs3dy1biifcPrtTfkDGSEl0Cb2mucXpuv5henElmPlI69IEq5F8vpxRVgcZESUXsbuGM2BA2r10JOdUQjG8JBL9JkZ4eovIsbVGNpJ-8cLLeu0H0VpKK2kxcEdM9MgqWtbdjjaEmiofdrmkoO-kDuPr6ZZ5u4srmOMDr2krM09RpXs9P9DazAWXE-mLAD-nWlcsEAdaLnc9oHUONvFxbnpGYDKDz6SkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیدمحمد خاتمی: ما در خطیرترین موقعیتی هستیم که جامعه و اسلام و ایران با آن روبرو بوده و ریشه‌اش در انقلاب اسلامی است
🔹
انقلاب اسلامی چه کسی آن را قبول داشته باشد چه نداشته باشد، چه بگوییم به اهدافش رسیده یا نرسیده، چه بگوییم از جهت خودش انحرافاتی پیدا کرده یا نکرده بزرگترین حادثه‌ای بود که در قرن گذشته در دنیا رخ داد و نه تنها وضع ایران و معادلاتی که در منطقه بود، بلکه معادلات جهان را عوض کرد.
🔹
مهمترین جلوه آن جنگ تحمیلی بود که آن را ناکام کردیم ولی دشمنی‌ها برداشته نشد و تحریم‌ها و توطئه‌ها ادامه پیدا کرد تا جنگ ۱۲ روزه و جنگ رمضان رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/682618" target="_blank">📅 20:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682617">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
قالیباف: هدف آمریکا چپاول کشورهای خلیج فارس است.
🔹
مصر از برقراری تماس‌های دیپلماتیک با ایران برای کاهش تنش خبر داد
🔹
ارتش رژیم جنایتکار صهیونیستی مدعی شهید شدن چند فرمانده حماس در حمله هوایی به غزه شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/682617" target="_blank">📅 20:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682616">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df2fc0de27.mp4?token=LiMQWfNUolZ6Z1ffrW7gTQ9mPLJXIdb8lnG7UywRN5nZm9Pe8qD0uhEtaoFV6CUDN3UP11Kw0kB-VBKhW_f-_BgiJEpQlpYKa7hLZmgSt2KMAznnT6Sywemo_99IKi-sW1zilMcMyTDzn09yZiBkyDhGvXX1SarNkZ02HqNzl-mOO9ICp6qpaQZraTtpwhrwUsQpZ26t9SqCQYErnYIelrfFqVc_exhwr7iFV4SJ5E5FZnWJzJPJr3NLkG5_LGMevT0rPMiMJW-ImgTBk928BwwgdZaly9584uKQOA5s-lzLH1wQv3uK-Kvt3_JwtR66MaG4y8uZORw40dEUyPzsmIqSkxwDMx9Hbq6ePiVO9cw-ReyQ7kwqoYEOuJ6g3nX284Y8noVs-LoQmVVgAhpmuUaU6ulO0VHQsNOlTob16rgUPqUUCkVgyhYRdXNRts6mHQwQjlb89dtHV_YKp77Znzosfnab2oaoZaO9sumkL7q8e0zC44Q_otOLEenMcyf-1aUTli0mo1oAZi_kJge9Vt4r13jIvxfsQT_8MkzWcLAy9oxR651HHzoPIs351cANSirLuTSHTTh_ldAboA2qMZNuzV-FvSeEH62lkKvfrFao9Gtz3bFS-07B_WI1IGzsDvlNiwGKUpOJmmScSUvEWYNQvqHb4kAgAZUZrOKdgLo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df2fc0de27.mp4?token=LiMQWfNUolZ6Z1ffrW7gTQ9mPLJXIdb8lnG7UywRN5nZm9Pe8qD0uhEtaoFV6CUDN3UP11Kw0kB-VBKhW_f-_BgiJEpQlpYKa7hLZmgSt2KMAznnT6Sywemo_99IKi-sW1zilMcMyTDzn09yZiBkyDhGvXX1SarNkZ02HqNzl-mOO9ICp6qpaQZraTtpwhrwUsQpZ26t9SqCQYErnYIelrfFqVc_exhwr7iFV4SJ5E5FZnWJzJPJr3NLkG5_LGMevT0rPMiMJW-ImgTBk928BwwgdZaly9584uKQOA5s-lzLH1wQv3uK-Kvt3_JwtR66MaG4y8uZORw40dEUyPzsmIqSkxwDMx9Hbq6ePiVO9cw-ReyQ7kwqoYEOuJ6g3nX284Y8noVs-LoQmVVgAhpmuUaU6ulO0VHQsNOlTob16rgUPqUUCkVgyhYRdXNRts6mHQwQjlb89dtHV_YKp77Znzosfnab2oaoZaO9sumkL7q8e0zC44Q_otOLEenMcyf-1aUTli0mo1oAZi_kJge9Vt4r13jIvxfsQT_8MkzWcLAy9oxR651HHzoPIs351cANSirLuTSHTTh_ldAboA2qMZNuzV-FvSeEH62lkKvfrFao9Gtz3bFS-07B_WI1IGzsDvlNiwGKUpOJmmScSUvEWYNQvqHb4kAgAZUZrOKdgLo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیت‌الله اعرافی: ملت ما پای انتقام خون امام شهید ایستاده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/682616" target="_blank">📅 20:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682615">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHSeiO1cq7eNelX6nBDvmskxa8bPqUbdH4pannIyftP-dV9ldiGWljd1D2nooDFQCXIzTSpICUa0ZRtX2j6nNGyC4Q5wqHJacc32aZDzRqDFATlRhNIdJPJuRbrKWV69Ny2NES8JSDgfP-lpLMZgoZo88Dup5F9WZGMA7u8PAwHo-MijcbErmXMNHVO08qPvdfozdDWCeS0eX3SFLHjtTllXR4LzFR9BMzTBNcNstoamfPc7GhRMENv5Ovl57LCdLbB3QwtWam8v-OZTcVm2PMG4JDtvY0UTr-19jHB41a37iZLALPUbil6kLBAlLANUta7XqmnwiPC2XJdh7CpuLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزهای حساس پیش‌رو؛ راهبرد جدید ایران چیست؟
🔹
به نظر می‌رسد رویارویی ترکیبی میان ایران و محور مقاومت از یک سو، و آمریکا و رژیم اسرائیل از سوی دیگر، نه تنها اجتناب‌ناپذیر، که در آستانه وقوع است.
تحلیلی دراین‌باره را در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3238994</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/682615" target="_blank">📅 20:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682614">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2978f5f65.mp4?token=rzHjBGvR-TcYa2ApRfbRHN3FXXGRthKhTKWDrd76td3VOsgNJUfjOHjz7EnAKSR-BvDzVhAPZcAexcmzzrgmkN1S79XCQYe11X0pzLp0-wyRF18WCNhIXHl6FdNMbCrVpheYYIcjSaHoZJOi5lIKrJAz3DUFZS5NC7uut0B7bS7bcS7fkId07xry-_uHrLEx7eCNlobPrRiyUou72Ep2Ooas7D3NXUsVAQ4iRfeFXGDTRu74SdibQoRW7cRepbJf6kAJpWFv0_VGBTrYUvthtEKwYvLSaLOiZkuUOT3NUXRqIVmxFBOx_MOyPaun2z64NwV7WEnoS_VKsj0IxJgA3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2978f5f65.mp4?token=rzHjBGvR-TcYa2ApRfbRHN3FXXGRthKhTKWDrd76td3VOsgNJUfjOHjz7EnAKSR-BvDzVhAPZcAexcmzzrgmkN1S79XCQYe11X0pzLp0-wyRF18WCNhIXHl6FdNMbCrVpheYYIcjSaHoZJOi5lIKrJAz3DUFZS5NC7uut0B7bS7bcS7fkId07xry-_uHrLEx7eCNlobPrRiyUou72Ep2Ooas7D3NXUsVAQ4iRfeFXGDTRu74SdibQoRW7cRepbJf6kAJpWFv0_VGBTrYUvthtEKwYvLSaLOiZkuUOT3NUXRqIVmxFBOx_MOyPaun2z64NwV7WEnoS_VKsj0IxJgA3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتابک، وزیر صمت: در دی ماه پارسال دو روز پس از جلسه رئیس‌جمهور با اصناف، بازار آرام شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/682614" target="_blank">📅 20:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682613">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
نرخ بیکاری پایتخت به ۱۰.۶ درصد رسید
🔹
بررسی داده‌های بهار ۱۴۰۵ در مقایسه با مدت مشابه سال گذشته نشان می‌دهد نرخ بیکاری در سه استان بیش از ۴ واحد درصد افزایش یافته است.
🔹
خراسان رضوی با رشد ۴.۸ واحد درصدی در صدر قرار دارد و پس از آن هرمزگان با ۴.۱ واحد درصد ایستاده است. در این میان، تهران نیز با افزایش ۴.۲ واحد درصدی نرخ بیکاری، یکی از مهم‌ترین تغییرات را ثبت کرده است.
🔹
نرخ بیکاری پایتخت از حدود ۶ درصد در بهار سال گذشته به ۱۰.۶ درصد در بهار امسال رسیده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/682613" target="_blank">📅 20:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682612">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf711e498.mp4?token=gu828OLsjCe_F39aXNQzaTJFEGtkfv9zQl7ueAZR_6C7gmEH5_IY2PwtaYAnuK-UEfVlhoACnJrCjJ6HZDFJKpxAZP9ybnJ_HcsljFo9S7yXh8GIcKqE2uwk8DveYsEDawOpx0vs4W5TWQzunyRR-kcvYmxelzYIVPoLdPrid1f9PnhqmQScmIZ3E47wNAMZDq3NTHHQQEGAzwjetvabRonDhXP2QjhjnW3V5-_hkL9MpwTWsa76UK5lvf9LP_StlPbgQ-sYGv9yyPQ4k__PbSMfyn4HgZSA7mU4gQm75uMsvUKr3EKDnUNx6Koz6jZ-ueRhPo1UpzcTgBGUwq67Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf711e498.mp4?token=gu828OLsjCe_F39aXNQzaTJFEGtkfv9zQl7ueAZR_6C7gmEH5_IY2PwtaYAnuK-UEfVlhoACnJrCjJ6HZDFJKpxAZP9ybnJ_HcsljFo9S7yXh8GIcKqE2uwk8DveYsEDawOpx0vs4W5TWQzunyRR-kcvYmxelzYIVPoLdPrid1f9PnhqmQScmIZ3E47wNAMZDq3NTHHQQEGAzwjetvabRonDhXP2QjhjnW3V5-_hkL9MpwTWsa76UK5lvf9LP_StlPbgQ-sYGv9yyPQ4k__PbSMfyn4HgZSA7mU4gQm75uMsvUKr3EKDnUNx6Koz6jZ-ueRhPo1UpzcTgBGUwq67Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاوت نوستالژیک و معروف تیتراژ سریال یوسف پیامبر توسط استاد کریم منصوری در محفل اربعین قرآنی‌ترین رهبر جهان اسلام در مشهد مقدس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/682612" target="_blank">📅 20:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682611">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a325a235c2.mp4?token=iS-mCArSZO44ZMoBe5Yby9gjaJB9XH8OSNm9J5SG_Wb3-7T5nhiYJbKrHLH6dGIigw4gd_KmFo6igd-acFy5MBCSyIpr3LA9q6kmMNniec-_qmaY4YzUfbO7uGoyZndopTs-xWo6FhnO2vO_A_D8S-2UAoZPjB7OqKYwcDhxMJ6tauwwXp24PHLUAfVu8xQtLQWFNOpbrbWWZD6AoJkzGTJqcfqmBdvKs5VCKyute1QxzGpBUvynJTH7Le5ZapDz8k44Fzan2M3i16B5_R40Kvi9yFS45XagtVWHjGwSYtrnvjXbMbbkATBIG65Mqm62iBzjI0qIc87UKqy6XOpuKHOL3dLStMIvMh0r2wdKAkAb61imhDHuGgE1r0bc-sZ7qqjjq6_1e_5C3BT7EbY4EwSWxZRSqgeH9HxAuKCMrEMBJNeHl3xWmNNcpCGr_EDl9k5fuxkGtNgaevSQstdqEHazsnjcN9xkomoPQVd02gt3NHG6znFjWxPIM_JrYWPzcH4Y_U55x9CIK0lCPx9Sc6WaNY-svhef6izk2Zz3EbPyR5M6e_9jL0rnnqY7vgt_Vh2Ac28-XXdL9WYme_QqQtZFLBxEqISTmdkYLghiNtWKuAx2y_y2DBeIOLICQrL36jfggqn4cz1_lcySvwDM-FTxjGhKVkRNsZP7mWgjisk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a325a235c2.mp4?token=iS-mCArSZO44ZMoBe5Yby9gjaJB9XH8OSNm9J5SG_Wb3-7T5nhiYJbKrHLH6dGIigw4gd_KmFo6igd-acFy5MBCSyIpr3LA9q6kmMNniec-_qmaY4YzUfbO7uGoyZndopTs-xWo6FhnO2vO_A_D8S-2UAoZPjB7OqKYwcDhxMJ6tauwwXp24PHLUAfVu8xQtLQWFNOpbrbWWZD6AoJkzGTJqcfqmBdvKs5VCKyute1QxzGpBUvynJTH7Le5ZapDz8k44Fzan2M3i16B5_R40Kvi9yFS45XagtVWHjGwSYtrnvjXbMbbkATBIG65Mqm62iBzjI0qIc87UKqy6XOpuKHOL3dLStMIvMh0r2wdKAkAb61imhDHuGgE1r0bc-sZ7qqjjq6_1e_5C3BT7EbY4EwSWxZRSqgeH9HxAuKCMrEMBJNeHl3xWmNNcpCGr_EDl9k5fuxkGtNgaevSQstdqEHazsnjcN9xkomoPQVd02gt3NHG6znFjWxPIM_JrYWPzcH4Y_U55x9CIK0lCPx9Sc6WaNY-svhef6izk2Zz3EbPyR5M6e_9jL0rnnqY7vgt_Vh2Ac28-XXdL9WYme_QqQtZFLBxEqISTmdkYLghiNtWKuAx2y_y2DBeIOLICQrL36jfggqn4cz1_lcySvwDM-FTxjGhKVkRNsZP7mWgjisk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک راه ساده و اثرگذار برای موفقیت مالی
🔹
فکر می‌کنی برای ثروتمند شدن، فقط باید پول بیشتری داشته باشی؟ شاید نه… شاید چیزی که از پول هم باارزش‌تره، سال‌هایی باشه که داری از دست میدی.
یک عدد ساده می‌تونه نشونت بده چرا شروع کردنِ زودتر، گاهی تفاوت بین سرمایه داشتن و ثروت ساختنه.
🔹
در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/682611" target="_blank">📅 20:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682610">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/182eb48064.mp4?token=Pe0QPUJVNLObMFf_zudRJEpl98BP88Rcb7Xy5BkMZimDRhfqlJ1nHUzUIKqNLRyBXaBpevp-KR4-kaV3zobHUh8azglo6-tuB_WFjqunaK_FVwj35Irgnv2TH8ikWdyd_PhU977X3nr7b8uJ9iQS0RV8FsnXQcVHd0Eo_4oyze9pkAT0YnkLNy0zGZuBXF2DaLqo730y-Xzd-XNefsJC-Cnd1NrSUFL79AfmQeQx6D1hr-Hw_qpHa2ypuHvx8sMnyjnxJrTyFC0DDM7y39ivk4iCOuRX7mn1AAXb0IpY0pWqQqfhpO34A7Dg90kcc-Iswu8QI1JhL-ZogeatFlilRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/182eb48064.mp4?token=Pe0QPUJVNLObMFf_zudRJEpl98BP88Rcb7Xy5BkMZimDRhfqlJ1nHUzUIKqNLRyBXaBpevp-KR4-kaV3zobHUh8azglo6-tuB_WFjqunaK_FVwj35Irgnv2TH8ikWdyd_PhU977X3nr7b8uJ9iQS0RV8FsnXQcVHd0Eo_4oyze9pkAT0YnkLNy0zGZuBXF2DaLqo730y-Xzd-XNefsJC-Cnd1NrSUFL79AfmQeQx6D1hr-Hw_qpHa2ypuHvx8sMnyjnxJrTyFC0DDM7y39ivk4iCOuRX7mn1AAXb0IpY0pWqQqfhpO34A7Dg90kcc-Iswu8QI1JhL-ZogeatFlilRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چنگال فقط برای غذا نیست! این ترفندها رو ببین
🤯
🍴
#ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/682610" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682609">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
شبکه عبری: ایرانی‌ها درس سختی به ترامپ دادند
🔹
«گیل تماری»، تحلیلگر روابط خارجی شبکه ۱۳ اسرائیل در برنامه‌ای اعلام کرد ۶۰ روز از زمانی که ترامپ خودکار معروف خود را برداشت و یادداشت تفاهم با ایران را در کمال افتخار و غرور امضا کرد، می‌گذرد و این به مثابه نشانه آغاز مرحله‌ای از مذاکرات برای حل نهایی برنامه هسته‌ای، موشک‌های بالستیک و نیروهای همسوی با ایران در منطقه بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/682609" target="_blank">📅 20:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682608">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be64cd3c87.mp4?token=qGXct9cT04XDULYpY9Fp5rZdFyGsAggJRFY5j1noaDQHna9fPb36_HRRLT1dPUpC8pXt0sq7PmhM1Qopsp22gU7OCy4xRqvzlk_lU5XYFHITOAkIz4wRq_bThT_7tbeet37twlppboeG5s9EOp7v3VBvP3ubDKUCssir6HnSso1W2ewOJB6_ttwV1cTX_bQs0mKl73CrjmcTrmKlzUhv9xw_Z1ngy9qIun4ZjhiMTNlkoSx1tWlCK_-tH82y_p8TL6uTTuRsXvCqT3x8zEijBBkefWEb23smY3v2P9vsU_BcNSpMmvwwU3dj1Y77ESpti0fifXXpQgd_e-NBLVDgWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be64cd3c87.mp4?token=qGXct9cT04XDULYpY9Fp5rZdFyGsAggJRFY5j1noaDQHna9fPb36_HRRLT1dPUpC8pXt0sq7PmhM1Qopsp22gU7OCy4xRqvzlk_lU5XYFHITOAkIz4wRq_bThT_7tbeet37twlppboeG5s9EOp7v3VBvP3ubDKUCssir6HnSso1W2ewOJB6_ttwV1cTX_bQs0mKl73CrjmcTrmKlzUhv9xw_Z1ngy9qIun4ZjhiMTNlkoSx1tWlCK_-tH82y_p8TL6uTTuRsXvCqT3x8zEijBBkefWEb23smY3v2P9vsU_BcNSpMmvwwU3dj1Y77ESpti0fifXXpQgd_e-NBLVDgWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر صمت: رئیس‌جمهور تکلیف کردند که برق صنایع قطع نشود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/682608" target="_blank">📅 19:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682607">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc02b7aa5.mp4?token=KNWn_cUbc0uBHYyWt5uOTkgMSQ0XYeLmUqsyeYATq1U0am9fD_VQBqMb8flLfrva7BdkFr01srigVz_5xPdBgRO7fTIAK5Lw7nHKExVGTA_3TRpIO4tKJeQHihCgLH89g_cqPl02tc1wm6bfoWzYcSqOQviVZ9NG3Fb5lbEu-K5PixMBvQgEkN-Ov6QrCF761k_Kzj0fdxlIVdn7AN9mmqj-NNP4MAVzJtdngsEsGdmdFnsT_7CeWWRVGN4Rhv8s_gA2w8vUl2s-7MRbRJT9Z8nwLOA_ICwyNmeLzRoVO4-mEzBofUF4vqT_Q1Vl6aIXUJqAUFYJMXCVnVBPdD4rjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc02b7aa5.mp4?token=KNWn_cUbc0uBHYyWt5uOTkgMSQ0XYeLmUqsyeYATq1U0am9fD_VQBqMb8flLfrva7BdkFr01srigVz_5xPdBgRO7fTIAK5Lw7nHKExVGTA_3TRpIO4tKJeQHihCgLH89g_cqPl02tc1wm6bfoWzYcSqOQviVZ9NG3Fb5lbEu-K5PixMBvQgEkN-Ov6QrCF761k_Kzj0fdxlIVdn7AN9mmqj-NNP4MAVzJtdngsEsGdmdFnsT_7CeWWRVGN4Rhv8s_gA2w8vUl2s-7MRbRJT9Z8nwLOA_ICwyNmeLzRoVO4-mEzBofUF4vqT_Q1Vl6aIXUJqAUFYJMXCVnVBPdD4rjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول پرسپولیس به استقلال خوزستان توسط محمد خدابنده‌لو
🔹
پرسپولیس۱ _ ۰ استقلال خوزستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/682607" target="_blank">📅 19:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682606">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keRF6AU0nUms0uF5NiB1ebG9owV_1BNociDw8cIcnd2g7ccJxYWwQrKevOpVnzPCMOR9d2uI8OOOhrcYne7niBbdffl18gjjVPvda-s1FuBHa9dLmIrpq9Bri8UVrYYXsloPydwmikdRDgiYtjN8qvqpBkjdqUaFDe1pS9bIBslY4MQsTl3BTDVrr1rlafgDMaPrPoj82aMrx4aLWPL5yOrtE1xp6TDGBwwHkVZnrNxKORp0iCGZASo_Om1soTba_BqZVnFQnIbYGcB3J1fmup99hD2RPLO_F-kJSsvLhP6S3Izv6WAcx95wnEDKnTjueYNUxei8pQvbjmKvsQoMig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نظرسنجی‌های آمریکا علیه جنگ ایران متحد شدند
🔹
به‌گزارش پایگاه نظرسنجی‌های معتبر، ۱۰ مؤسسه سرشناس در بازه تیر تا مرداد ۱۴۰۵ افکار عمومی آمریکا را درباره جنگ با ایران سنجیده‌اند.
آخرین نظرسنجی هر مؤسسه به تفکیک:
🔹
ایپسوس (رویترز) – ۱۴ تا ۱۷ مرداد: ۳۴ درصد حمایت در برابر ۶۱ درصد مخالفت (اختلاف منفی ۲۷ درصد)
🔹
آر‌ام‌جی ریسرچ (نیوز سرویس ناپولیتن) – ۵ تا ۶ مرداد: ۴۰ درصد حمایت در برابر ۴۹ درصد مخالفت (منفی ۹ درصد)
🔹
دانشگاه کوئینیپیاک – ۱ تا ۵ مرداد: ۳۴ درصد حمایت در برابر ۶۰ درصد مخالفت (منفی ۲۶ درصد)
🔹
گزارش‌های راسموسن – ۱ تا ۶ مرداد: ۳۵ درصد حمایت در برابر ۵۴ درصد مخالفت (منفی ۱۹ درصد)
🔹
ای‌پی نورک – ۱ تا ۵ مرداد: ۳۳ درصد حمایت در برابر ۶۴ درصد مخالفت (منفی ۳۱ درصد)
🔹
گروه استراتژی جهانی / جی‌بی‌ای‌او (پیمایشگر) – ۱ تا ۵ مرداد: ۴۱ درصد حمایت در برابر ۵۲ درصد مخالفت (منفی ۱۱ درصد)
🔹
یوگاو (سی‌بی‌اس نیوز) – ۳۱ تیر تا ۲ مرداد: ۳۹ درصد حمایت در برابر ۶۱ درصد مخالفت (منفی ۲۲ درصد)/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/682606" target="_blank">📅 19:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682605">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ebbb18e20.mp4?token=OUdLLIy8twkH_GUK84Q16akaP6NkCo3m6UQv6HE6cf2ojocksC9pgrTcUG3AKB3EQI9hmpGDVb9XwmsmH0xYImxBeszviAXhVmj-R5Q2_Q0tkQNNkIAYrUmfCiaZ4MIOWIvQi4XICE0nLIxzgcnQdi65HMeBRx6mahmHGmjqbqKj2zEwqKJtevdP5NdH9SSYlQZtec2GH7MYwGjEfyeK7qUTTqZvFmshIbuYGMY-wESPhKbixEQOaAGuXeEC51AfPXaColPmJlb5GMV80X9EHBBCdGSJMWNzVa8dbCdrKlK13CocIPZ7G2TB0zvIqbbKnuMmKF-G4SEq0p9Vwv9ZaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ebbb18e20.mp4?token=OUdLLIy8twkH_GUK84Q16akaP6NkCo3m6UQv6HE6cf2ojocksC9pgrTcUG3AKB3EQI9hmpGDVb9XwmsmH0xYImxBeszviAXhVmj-R5Q2_Q0tkQNNkIAYrUmfCiaZ4MIOWIvQi4XICE0nLIxzgcnQdi65HMeBRx6mahmHGmjqbqKj2zEwqKJtevdP5NdH9SSYlQZtec2GH7MYwGjEfyeK7qUTTqZvFmshIbuYGMY-wESPhKbixEQOaAGuXeEC51AfPXaColPmJlb5GMV80X9EHBBCdGSJMWNzVa8dbCdrKlK13CocIPZ7G2TB0zvIqbbKnuMmKF-G4SEq0p9Vwv9ZaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر صمت: رئیس‌جمهور تکلیف کردند که برق صنایع قطع نشود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/682605" target="_blank">📅 19:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682604">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
پولیتیکو: در حالی که واشنگتن منتظر تسلیم تهران است، مقام‌های پیشین و کارشناسان آمریکایی معتقدند ایران برای حفظ مواضع خود در مذاکرات، در برابر فشار اقتصادی مقاومت خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/682604" target="_blank">📅 19:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682603">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d693137e12.mp4?token=U_tIAJofyok2NqQhsM7FnB8E2eS6MCwnTx_dPgsY6An7qE2VpWw0OBPeeCvnLZu3Cg_S_WRovDKv7ik2uRHlFe-CXf9_eCHuW1OEmKvZVsa5HyPi03_RJpvc6bijsBj6sIf0ECv_mUUK_G2mDuWesaPSJPa2OLGTojUSuExEfp0fSI2roankRKc-LKAVhyHxDAcPg9TMJxktvRm6AhKG3UNROmIsHG_gefdxj6pi1KDR7hK9vqL5nKv6Rmq7YqXOFKc22LBoYSPgY_ulXabmK6Qcftx6SmCzZ15tVZtPLEb9uzrImyTG-X2XrunumTBlqja9Krrr8tp6PjiEG2tSfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d693137e12.mp4?token=U_tIAJofyok2NqQhsM7FnB8E2eS6MCwnTx_dPgsY6An7qE2VpWw0OBPeeCvnLZu3Cg_S_WRovDKv7ik2uRHlFe-CXf9_eCHuW1OEmKvZVsa5HyPi03_RJpvc6bijsBj6sIf0ECv_mUUK_G2mDuWesaPSJPa2OLGTojUSuExEfp0fSI2roankRKc-LKAVhyHxDAcPg9TMJxktvRm6AhKG3UNROmIsHG_gefdxj6pi1KDR7hK9vqL5nKv6Rmq7YqXOFKc22LBoYSPgY_ulXabmK6Qcftx6SmCzZ15tVZtPLEb9uzrImyTG-X2XrunumTBlqja9Krrr8tp6PjiEG2tSfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: ایران نمی‌تواند سلاح هسته‌ای داشته باشد. می‌دانید چرا؟ چون از آن استفاده خواهد کرد و ما اجازه نمی‌دهیم از آن استفاده کنند  ترامپ:
🔹
مردم در حال پیدا کردن جایگزین‌هایی برای تنگه هرمز هستند. می‌دانید جایگزین‌ها کجاست: تگزاس، آلاسکا، لوئیزیانا.…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/682603" target="_blank">📅 19:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682602">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ترامپ متوهم ادعا کرد ایالات متحده «مالک» تنگه هرمز است #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/682602" target="_blank">📅 19:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682601">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d09Sk2KJI2JcfUS8X_HJ8l8HKyUI-aLOWJX5rNWWkaIEbrkpXVm1YeBG4qF917fysXbYnRj1MEepM6UKUU3GggTCcdjHDUTjOwxJF86bZatdA0MRSrcKjOvOcNnjJrAhERblWblu4NWNP7oOEEkAgpUK4zytN4CXKh25sCGieBN8yzc02ZGNgVmiGDMi9rwYWzWsk5McfRApxe7jnNDGSLQijuL3hUHNwTLGUm6yBBO3AL_ZODC6oiX3W7N-JD7xNvZLX6a0OImsBrhcqZqz5_u7wKAJs0ON8-cSqdRYmNrXaVY22jKW2MIqWFURIEdNKqYSDJEFN1AuQLBFn_kWVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه نگران‌کننده ریاض برای ضربه زدن به تنگه هرمز/ این کریدور خطرناک به دنبال تغییر نتیجه جنگ با آمریکا است/ موشک‌های ایران، آماده حمله به عربستان؟
🔹
مسیر عمان _ عربستان می‌تواند تحت تاثیر تهدیدات موشکی ایران و یمن قرار بگیرد و به خصوص اگر لوله نفتی از این کریدور عبور کند، در مقابل حملات احتمالی جبهه مقاومت ضعیف خواهد بود.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3237668</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/682601" target="_blank">📅 19:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682600">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09320f13e.mp4?token=W-XdIaWTPrcOKXE_PXbe1opTTe3QqlfCQQ2RK-wHYrDZY52lJsFc1p4-vkWztzqHf5NNrIcEspEU215hobLO3sIkoqcAFrMbQ9XI4i21RfelYEUjDtr91Pdb4jv-oP9GkZ2yAfDvnlSB3dgxylC0HUvNQ4zd9zplzbDMLv4phiO41jGHYnss5TvXzL0Aww_yNZMJOV58ZB-jUVHFV137-RCd72ia0IyPue_xXXzbTkVi8Z7iyjyNXvqecZs8xN0dgjz5qK18OQXZnPDrboIx-aFE1UWbAnF9jJwfWtglDWWihc7Ivcl1khz9VHZMv4lJnNJvI5JjD1VPiZ72-3XuYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09320f13e.mp4?token=W-XdIaWTPrcOKXE_PXbe1opTTe3QqlfCQQ2RK-wHYrDZY52lJsFc1p4-vkWztzqHf5NNrIcEspEU215hobLO3sIkoqcAFrMbQ9XI4i21RfelYEUjDtr91Pdb4jv-oP9GkZ2yAfDvnlSB3dgxylC0HUvNQ4zd9zplzbDMLv4phiO41jGHYnss5TvXzL0Aww_yNZMJOV58ZB-jUVHFV137-RCd72ia0IyPue_xXXzbTkVi8Z7iyjyNXvqecZs8xN0dgjz5qK18OQXZnPDrboIx-aFE1UWbAnF9jJwfWtglDWWihc7Ivcl1khz9VHZMv4lJnNJvI5JjD1VPiZ72-3XuYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول پرسپولیس به استقلال خوزستان توسط محمد خدابنده‌لو
🔹
پرسپولیس۱ _ ۰ استقلال خوزستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/682600" target="_blank">📅 19:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682599">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6372ce8aa3.mp4?token=HxXOOcyyrdqSHbLHpAFqcaP-lH_4mjRlWjKaYaPle2omRUvs92TZuf6zBInVysshffVE9DoupO2mvXKrnKAKdOAIJTKfDs7KGBCUZl-LSiSqv0NC7iPS1Bt_oQkdNenxgx_1kPDzpCvMZSLIZPQPbtlMAxeWBDKSiSdNHK1SyNULloOdDTPbpJfh4-yVNgsrs3ujnGwylcJdJdUnJ5rQMDdzB7uIx1-zhCxBBhuSftGT8oxU9EBM0bXZISac-zswbXAyKbv6Zp1To7zu5xG1_P-0CXVcyV8ZvmGFCuaJCggwG_jLfSom4XZUAtc79hrubiwZLyAtcomIKOVZgnHihQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6372ce8aa3.mp4?token=HxXOOcyyrdqSHbLHpAFqcaP-lH_4mjRlWjKaYaPle2omRUvs92TZuf6zBInVysshffVE9DoupO2mvXKrnKAKdOAIJTKfDs7KGBCUZl-LSiSqv0NC7iPS1Bt_oQkdNenxgx_1kPDzpCvMZSLIZPQPbtlMAxeWBDKSiSdNHK1SyNULloOdDTPbpJfh4-yVNgsrs3ujnGwylcJdJdUnJ5rQMDdzB7uIx1-zhCxBBhuSftGT8oxU9EBM0bXZISac-zswbXAyKbv6Zp1To7zu5xG1_P-0CXVcyV8ZvmGFCuaJCggwG_jLfSom4XZUAtc79hrubiwZLyAtcomIKOVZgnHihQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت‌های شما از دلایل تجرد | چرا ازدواج نمی‌کنیم؟
🔹
صداهایی از جنس واقعیت؛ روایت بدون واسطه مخاطبان خبرفوری از موانع اقتصادی و چالش‌های پیش‌روی ازدواج.
🔸
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/682599" target="_blank">📅 19:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682598">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
تحریم جدید انگلیس علیه ایران
🔹
انگلیس در ادامه سیاست‌های خصمانه خود علیه تهران، فهرست جدیدی از تحریم‌های ادعایی علیه اشخاص و نهادهای منتسب به ایران وضع کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/682598" target="_blank">📅 19:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682597">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/986c023d1c.mp4?token=hggb37AO_2o26Oz2Fo_2wOchq0mF8FpC2p1qudBrDOv_3aSRMC6zc1XkzzoFZxIYI7uwbt-iKqMllaLUPRsg0GCsdeSz-yuLdQMXvLyhH2iWCqz88zv4qVlZZVkCNN-O8Zd-GL2lAUU58pujQByD5GNDtj3cYzp0O3xm7gQQ-_nWZDJYfvLZC8t1ofozKVWGZaVX2P77f1FMNij9zYugIcja8r6Qla-KgplJYycUk_2_2qxFGkIQemUgY8KbReMhZ6yFT-vKs4lfYxUK83UrJCBswqiDniMjQ1CiC5SYFQ-_TsOkwoEN48WgZMm5CLDKWxIUi03AiUfAQjDqaVTdM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/986c023d1c.mp4?token=hggb37AO_2o26Oz2Fo_2wOchq0mF8FpC2p1qudBrDOv_3aSRMC6zc1XkzzoFZxIYI7uwbt-iKqMllaLUPRsg0GCsdeSz-yuLdQMXvLyhH2iWCqz88zv4qVlZZVkCNN-O8Zd-GL2lAUU58pujQByD5GNDtj3cYzp0O3xm7gQQ-_nWZDJYfvLZC8t1ofozKVWGZaVX2P77f1FMNij9zYugIcja8r6Qla-KgplJYycUk_2_2qxFGkIQemUgY8KbReMhZ6yFT-vKs4lfYxUK83UrJCBswqiDniMjQ1CiC5SYFQ-_TsOkwoEN48WgZMm5CLDKWxIUi03AiUfAQjDqaVTdM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: آیا مذاکرات با ایران را از سر خواهید گرفت؟  ترامپ:
🔹
شاید در مقطعی، اما در حال حاضر اوضاع خیلی خوب است. البته شاید در مقطعی.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/682597" target="_blank">📅 19:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682596">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9b48893c3.mp4?token=JXqVPnW0gO2IDc4BZHi-uQuV_jjbRGUJ4KsyB90xXAXoGrzdD4HXd0sL3pPv1G8kEP0na463nLT-JkB2l9FWprsKxlx0dDNHSySqwdoWCW66LlHQ-ib1TOXwIYcRGDZTLWs5Qe_jq4P_iS_4AjwO2LxygYPHQufjvDS6-lTm38qbes5_JlgrPzckCR0XoAU0DsGrceDkBJT8ILrhnAW1krf-unP6UKqi-EaimeM53-PWV5hjf47_nBCLWqfarNGvmCpaxB-7Ut_fv54aewYBXPJtXxwhpksqLABTVKotiAH-ducE3ITVHy4Uy7-u_bbFrw9fKLbO1kKE664K4Ik3fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9b48893c3.mp4?token=JXqVPnW0gO2IDc4BZHi-uQuV_jjbRGUJ4KsyB90xXAXoGrzdD4HXd0sL3pPv1G8kEP0na463nLT-JkB2l9FWprsKxlx0dDNHSySqwdoWCW66LlHQ-ib1TOXwIYcRGDZTLWs5Qe_jq4P_iS_4AjwO2LxygYPHQufjvDS6-lTm38qbes5_JlgrPzckCR0XoAU0DsGrceDkBJT8ILrhnAW1krf-unP6UKqi-EaimeM53-PWV5hjf47_nBCLWqfarNGvmCpaxB-7Ut_fv54aewYBXPJtXxwhpksqLABTVKotiAH-ducE3ITVHy4Uy7-u_bbFrw9fKLbO1kKE664K4Ik3fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علت
صدای تق تق انگشت چیه؟
🔹
صدا تق تق انگشت از ترکیدن حباب‌های گاز توی مایع مفصلی به وجود میاد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/682596" target="_blank">📅 19:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682595">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b47477531.mp4?token=PS0qMfjZWCAMSYnYQf7ZH8QHBK2Mv74Gi7qqnQTxfcukf6Z9Zdib4s4jKMeucJG4hIcvYo9V2T2fKw4MsEhRaZ_tKQop9wUZKu-r_DODUUFvr5FhTgWEmLa_jXsTR3x1QPavrbVdf0_un1sUJjahYPvD5OtK7Vly6KosiBjCwbqFopl2dsV1wa1ulu50kKwrrAVwAQIL6M-kvo_Mdj9r6LVw07aF7gIDbT-Yt4UoBiROEKyrmFo7MHx2Yqm1XsJMinRnNOVrqOKtUS-4XZ16NIKFj2gk8LHgg-z1UC5nWIdfWjG2Yvm5ErT5eYBJxO2uTOEgbeEqZyyB2BnkUxBDCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b47477531.mp4?token=PS0qMfjZWCAMSYnYQf7ZH8QHBK2Mv74Gi7qqnQTxfcukf6Z9Zdib4s4jKMeucJG4hIcvYo9V2T2fKw4MsEhRaZ_tKQop9wUZKu-r_DODUUFvr5FhTgWEmLa_jXsTR3x1QPavrbVdf0_un1sUJjahYPvD5OtK7Vly6KosiBjCwbqFopl2dsV1wa1ulu50kKwrrAVwAQIL6M-kvo_Mdj9r6LVw07aF7gIDbT-Yt4UoBiROEKyrmFo7MHx2Yqm1XsJMinRnNOVrqOKtUS-4XZ16NIKFj2gk8LHgg-z1UC5nWIdfWjG2Yvm5ErT5eYBJxO2uTOEgbeEqZyyB2BnkUxBDCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هجوم اوباش با سلاح سرد به ورزشکاران در بهارستان
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/682595" target="_blank">📅 19:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682594">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f019dbda2e.mp4?token=otwwwRGOzND_I39wOVK7E3mr3H7DhCikDZT7icxBvsF-uDohehksyySkc9zPgS9Op3L8GJD6Lkw83ZPksC4sIUQ6H2mQLMjtvazFf-9riB9w6OI83mgumOsw_FWBiYf_Z_EUFiZBOpmTct1RQN--0riycwyHkvZr6E2JkB0acQp6oP85cs2OMMHTt0qBfuowrV5_H2m5Y8Bm3tDYXO4Cm18SS-5UzR1eNn195OhV9F5EbHJAYW8bQojt4d0xlEkjSegL3wOYQGHNBQ28gDv2qZfzghbH5uNyQT1_A2Y7pwAUpu6pu3p5FllSC7Vt2JV2voTnkU5IOfxo4TsvDgbBrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f019dbda2e.mp4?token=otwwwRGOzND_I39wOVK7E3mr3H7DhCikDZT7icxBvsF-uDohehksyySkc9zPgS9Op3L8GJD6Lkw83ZPksC4sIUQ6H2mQLMjtvazFf-9riB9w6OI83mgumOsw_FWBiYf_Z_EUFiZBOpmTct1RQN--0riycwyHkvZr6E2JkB0acQp6oP85cs2OMMHTt0qBfuowrV5_H2m5Y8Bm3tDYXO4Cm18SS-5UzR1eNn195OhV9F5EbHJAYW8bQojt4d0xlEkjSegL3wOYQGHNBQ28gDv2qZfzghbH5uNyQT1_A2Y7pwAUpu6pu3p5FllSC7Vt2JV2voTnkU5IOfxo4TsvDgbBrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: آیا مذاکرات با ایران را از سر خواهید گرفت؟
ترامپ:
🔹
شاید در مقطعی، اما در حال حاضر اوضاع خیلی خوب است. البته شاید در مقطعی.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/682594" target="_blank">📅 19:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682593">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHaSvAHI-cghvuQvZNeduwFxmCS54NGbD6yPEl5yHGf-BkKWRjcDGKUoFdL-6I31ke37SjTubyeyYE72nmXB8m0KY6iDXGZxfAPgEY4CpPT-mAu_e9hJLnyKH77LwnRKOV9hzEeRB9degHgH4jHGEg7ONVoFKlXM7-mbTUEF2iBRUJTL5jMg0D91Cok_GsDNLLa6eY0AYlpRJFai8lyXXK43QRP-2V0zwubWhSmXAnAJkVRKbrWNud3NQ4nmwayLAclkMffBJWPxfqe6ji1TDPDhOpDzwvBV582-Wnns2sXENdrY_xAyhJN62hGjOpYT7snMyvoQaYU0ftUbBkNd0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عبور نفتکش تحت تحریم آمریکا از محاصره
🔹
پایش‌های ماهواره‌ای نشان می‌دهد که نفتکش چینی «مایتی نویگیتور» حامل ال‌پی‌جی که تحت تحریم آمریکاست، از سنگاپور بازگشته و امروز از تنگه هرمز عبور کرده است.
🔹
ترامپ یک هفته پیش در تروث سوشال نوشت، همه می‌گویند محاصره ما دیوار آهنین است و ایران هیچ کاری از دستش برنمی‌آید؛ او روز گذشته هم گفت، تنگه هرمز باز است و محاصره به قوت خود باقی‌ست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/682593" target="_blank">📅 19:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682592">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfqO_IPYPqpjv6EdwoUQFZc9iblQLwJMEn0ZGFpliC6tnryC5hUx5xkTWHF4wVpi76KLNM9wQxINHdccENJdGNHx80CBDrJoeDFFCFw31CyaCs15-rNEQzfqiyUFv-qEIuZSIVBIjkC4xd85QzEoZW5A5uwmVgYHqVrkKG9ozxJjiCCnD8JpwAZM7HhNkClY30HWwq8Mm8pqNHaRce-ybOma4jYinu8qZPbcp83U0ObtRS6yIGzilnfRrndeOQxOSW3IrAlyNqAIfFapwgwdX75LSKP63lCtbzovf7i_WiAMdLF7LiO4D4x8VVErG-qXa17WRf7vS7WoMyCrFGeL9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طول خطوط متروی کلان‌شهرهای جهان
🔸
پکن با ۹۰۹ کیلومتر خط فعال، طولانی‌ترین شبکه متروی جهان را در اختیار دارد. همچنین ۹ شهر از ۱۰ شهر دارای طولانی‌ترین شبکه‌های مترو جهان، در چین قرار دارند.
🔸
متروی تهران با ۳۱۰ کیلومتر خط فعال، در رتبه هفتم این فهرست و بالاتر از مادرید و پاریس قرار دارد و طولانی‌ترین شبکه متروی منطقه را به خود اختصاص داده است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/682592" target="_blank">📅 19:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682591">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
جزئیات نسخه جدید مصوبه مجلس: اگر فعالیت در فضای مجازی و حوزه‌های فرهنگی، احکام دینی را زیر سوال ببرد یا تصویری ناروا از جامعه و دستاوردهای انقلاب نشان دهد، منتشر کننده به جزای نقدی معادل هزینه‌های تولید اثر محکوم می‌شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/682591" target="_blank">📅 19:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682590">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
راه حل اتحادیه نان برای جلوگیری از گرانی: نانوایی‌های گران‌فروش پلمپ خواهند شد!
محمد سلیمانی، رئیس اتحادیه نان سنگک:
🔹
نان سنگک ۱۰۰ هزار تومانی در نانوایان غیر مجاز دیده می‌شود؛ قیمت مصوب ۱۵/۵۰۰ هزار تومان است؛ کنجدی ۲۰ هزار تومان ودو رو کنجد ۲۵ هزارتومان است. نرخ آزاد نان ساده  ۳۸ هزارتومان و کنجدی دو رو ۵۰ هزارتومان است.  نانوایی‌هایی که قیمتی بالاتر از داشته باشند، طبق ماده ۲۷ بعد از دادن اخطار، پلمپ خواهند شد./ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/682590" target="_blank">📅 19:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682589">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a0283ff87.mp4?token=a6c85VY40QxfTv-njEVP3ZjRxX9B1vl9LCZSOD8N_w9NnOK3wu6rtJm11FoM_mQL38nooaLvaZVFFfnc0Xt1I6wkCMPmgQ6hPHYhFPHJIQuk9TOf2nblScfcZcgzFy3zA3dUptiVzjNs0Xssxdi5HqJnqb-VolNVs-9RbukmZ2iSXZh3qeaDpnRKijKvi0mILyv0eFSxlXOABZYlz1TUbUR7zmCY5Wi_elVSZkvnubr-W_rGaQstGLlrpVdktPJLX-lg7kSCQ_pNn7TpMasHhGCV9M_3jJuiQn7zAQEc42BBK4oKbMzH0ukWbT61-t6NYS7OenctXusrFVhd8O3M4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a0283ff87.mp4?token=a6c85VY40QxfTv-njEVP3ZjRxX9B1vl9LCZSOD8N_w9NnOK3wu6rtJm11FoM_mQL38nooaLvaZVFFfnc0Xt1I6wkCMPmgQ6hPHYhFPHJIQuk9TOf2nblScfcZcgzFy3zA3dUptiVzjNs0Xssxdi5HqJnqb-VolNVs-9RbukmZ2iSXZh3qeaDpnRKijKvi0mILyv0eFSxlXOABZYlz1TUbUR7zmCY5Wi_elVSZkvnubr-W_rGaQstGLlrpVdktPJLX-lg7kSCQ_pNn7TpMasHhGCV9M_3jJuiQn7zAQEc42BBK4oKbMzH0ukWbT61-t6NYS7OenctXusrFVhd8O3M4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاگرس؛ پوشاک آقایان و بانوان
پوشاک زاگرس با اعتماد بیش از ۱۰۰۰ سازمان معتبر آماده ارائه جامع‌ترین راهکارهای سازمانی است:
🔹
فرم اداری: طراحی یکپارچه منطبق با هویت برند شما.
🔹
شخصی‌دوزی صنعتی: دوخت سفارشی با متد روز ویژه مدیران.
🔹
بن‌کارت و هدیه: انتخاب آزادانه پرسنل از شعب سراسر کشور.
🔹
تامین سریع: ارسال فوری سفارشات عمده از انبار مرکزی.
📥
دریافت کاتالوگ:
🔗
https://zgrs.ir/zbcatalog
📞
مشاوره و فروش سازمانی: 02143064444
🌐
https://zgrs.ir/zo</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/682589" target="_blank">📅 19:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682588">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2577bb6fd9.mp4?token=ansQJ0IN0UbIpckIklH0ahOm8oBkHJY0Q1wmYrUjBcVdZ-GrPuJUe3en6ML-8DQ-LVoSu3rO4QDQwqJljDk8VqSdfGjKwlhKWDx5Tg8A7FY9cteKkSmKa4aCsY7dMVN7PJkoffo07KJozjf9OyyegnfZqm7z_KocReNu17llrOekd7wxFhWzNTArdKr4C8ivy63llI_YqEyosY4UcRRHNUt82pO09H4ntfA-VjeU2g80qry9STkDkHDi-7pI9xrSCc3yuOOaVVdQegYWeBJlefMiEv5yRDGzu0xvxv7NElmuiiSjdot1IbMZYUiyXcTUE2n2gR77ZdyP3MxFiiL3Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2577bb6fd9.mp4?token=ansQJ0IN0UbIpckIklH0ahOm8oBkHJY0Q1wmYrUjBcVdZ-GrPuJUe3en6ML-8DQ-LVoSu3rO4QDQwqJljDk8VqSdfGjKwlhKWDx5Tg8A7FY9cteKkSmKa4aCsY7dMVN7PJkoffo07KJozjf9OyyegnfZqm7z_KocReNu17llrOekd7wxFhWzNTArdKr4C8ivy63llI_YqEyosY4UcRRHNUt82pO09H4ntfA-VjeU2g80qry9STkDkHDi-7pI9xrSCc3yuOOaVVdQegYWeBJlefMiEv5yRDGzu0xvxv7NElmuiiSjdot1IbMZYUiyXcTUE2n2gR77ZdyP3MxFiiL3Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هزینه جنگ ترامپ و نتانیاهو از جیب شهروندان آمریکایی
سی‌ان‌ان:
🔹
به لطف جنگ غیرقانونی ترامپ علیه ایران، قیمت بنزین ۳۰ درصد، قیمت گازوئیل ۴۸ درصد و سوخت جت ۷۳ درصد افزایش یافته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/682588" target="_blank">📅 18:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682586">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
مصوبه مجلس: کلیه فعالیت‌ها و ارتباطات افراد با اشخاص خارجی باید در چارچوب قانون جدید صورت پذیرد  مصوبات تازه مجلس:
🔹
هرگونه فعالیت یا ارتباط اشخاص ایرانی یا خارجی که منجر به نقض وحدت ملی و موازین اسلامی شود، ممنوع است.
🔹
هر تبعه ایرانی که اقدام به اخذ هر…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/682586" target="_blank">📅 18:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682585">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
مصوبه
مجلس: کلیه فعالیت‌ها و ارتباطات افراد با اشخاص خارجی باید در چارچوب قانون جدید صورت پذیرد
مصوبات تازه مجلس:
🔹
هرگونه فعالیت یا ارتباط اشخاص ایرانی یا خارجی که منجر به نقض وحدت ملی و موازین اسلامی شود، ممنوع است.
🔹
هر تبعه ایرانی که اقدام به
اخذ هر نوع اقامت دائم
در کشور دیگر نماید، از اشتغال در تمامی مشاغل و سمت‌های دولتی و عمومی، محروم خواهد شد.
🔹
۶ ماه تا ۲ سال زندان یا جریمه ۸۰ میلیونی برای
مصاحبه اتباع ایرانی با رسانه‌ها یا انسان‌ رسانه‌های تحت مالکیت یا مدیریت کارگزاران مرتبط با دولت متخاصم یا دولت خارجی
که هدف تأثیرگذاری مخرب دارد./ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/682585" target="_blank">📅 18:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682584">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b6fd8084a.mp4?token=FAacDMgBuL5MF8KrVHZrdHMU4pqaTVBQCDeQJ6zXF8tXior0PCI25cxwi_Tb_zcEZmzVieoExtKeQGMz-g3Pkn7DDXkDw6eoUdCmPyGeAITiJmq8LnZPELuAJR7m1Qcy5HG9g_i2dH2dv8xK4GzKR1YTKiq2DQrL_wO1jNp5X9aM0-Wvsf_2Go2ROjc3_TOgFpvb8CUTahGneTdIJfKhVWvW4n01C0KISjlt9hJ49CcUWWpzSDaStcU_nfUCvVFBr_O7nHHHWSCHF7n9VBQ7M9UArg80lNiaaPbXAcrH-AKsoMwhyM-LWYoMdPgiMHtEUqIbzK3CAXtCmxmGlePokw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b6fd8084a.mp4?token=FAacDMgBuL5MF8KrVHZrdHMU4pqaTVBQCDeQJ6zXF8tXior0PCI25cxwi_Tb_zcEZmzVieoExtKeQGMz-g3Pkn7DDXkDw6eoUdCmPyGeAITiJmq8LnZPELuAJR7m1Qcy5HG9g_i2dH2dv8xK4GzKR1YTKiq2DQrL_wO1jNp5X9aM0-Wvsf_2Go2ROjc3_TOgFpvb8CUTahGneTdIJfKhVWvW4n01C0KISjlt9hJ49CcUWWpzSDaStcU_nfUCvVFBr_O7nHHHWSCHF7n9VBQ7M9UArg80lNiaaPbXAcrH-AKsoMwhyM-LWYoMdPgiMHtEUqIbzK3CAXtCmxmGlePokw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۶ ابرغذا برای افزایش طبیعی انرژی روزانه شما
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/682584" target="_blank">📅 18:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682583">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
موج جدید آلودگی نفتی در سوزای قشم مشاهده شد!
سازمان حفاظت محیط‌زیست کشور:
🔹
طی روزهای گذشته با تلاش محیط‌زیست استان هرمزگان و سایر دستگاه‌های اجرایی و همراهی ارزشمند مردم، بخش قابل‌توجهی از آلودگی نفتی جمع‌آوری شد اما به تازگی با موج دیگری از آلودگی مواجه شدیم که آثار آن به‌وضوح در ساحل مشهود است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/682583" target="_blank">📅 18:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682581">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
یوسفی، نماینده مجلس: دلیل مصرف ۱۳۰ میلیون لیتر بنزین در روز، کیفیت پایین خودروی داخلی حتی مدل صفر آن است.
🔹
وزیر خارجه قطر در دیدار با رئیس دفتر سیاسی حماس خواستار فشار جهانی بر اسرائیل شد.
🔹
شهادت و زخمی شدن ۴ لبنانی در تله انفجاری رژیم صهیونیستی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/682581" target="_blank">📅 18:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682580">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Op_3BH4p7ohTLC7Pc7wgcjhSZsVzdRX7Ey4SvgO1VMi8FbYcY1Z2ZjILq0Zf_v1F7xNiQAB2JQkD3rZVHoThqN94widO5V9q56AjFzD4oSJPdMkJBgmhaMUxO95YuOIxhJfRAPV5Q_tRCgDv_kqT4OfpOZqqMQ0NUyP9MoT9SlACNLjEYamruCC_LjJJBTb86j1pzYjDGhfOMfVWBWJmeNWWdB2X7dxzkHwAyXv-WqLCEryT--aeVOqI3ne-utovMRHjoXYR1ziORRb4iNyJoG7_1YHYte50kaiYmtS8pVBjqFZdcf1ze_jalYMJwTyXnVL3YtJ52QPx-yGA7Bp6rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غذاهای مفید برای مغز
🧠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/682580" target="_blank">📅 18:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682579">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsWnnk8UscITDUEZ8WvkM7K1p2EHpmjRdl1K_S1UtXf1ctwS52USJaSiy96F-4WIn6T9knQPX0L7_LTYT0T9B15LGNVsGY5h-46Vm9CIafTlcmNWebD2RRm_0s1naXbyLiK8Y8YOGcOvhuX0wQXWyS50ECoGs7LbjYdTkcmmXFhHw74e6BuBQmYA8RWGSWm9b414H7sfga_jIdOsMlTFvo8TG5aWt2S5761iapQhwysYpWfzCljs9rz8WsQjzI_DG8i2HU-WJVSb7mWwgP9abA1xe59cf1vJoB4wa6-DtMHZb7KUIX3CmCb65924xbNJ4N0MdwcDtFU7Lt2iTEAstQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بدهی آمریکا این هفته از مرز ۴۰ تریلیون دلار عبور می‌کند
🔹
بدهی ملی آمریکا احتمالاً همین هفته از ۴۰ تریلیون دلار عبور خواهد کرد؛ رقمی که چند ماه زودتر از پیش‌بینی‌های قبلی محقق می‌شود. به نوشته واشنگتن‌پست، کاهش درآمدهای دولت، از جمله به‌دلیل لغو تعرفه‌های تجاری دونالد ترامپ، وزارت خزانه‌داری آمریکا را ناچار کرده است برای پرداخت هزینه‌های جاری، سریع‌تر وام بگیرد.
🔹
هزینه سالانه بهره این بدهی نیز امسال از یک تریلیون دلار فراتر می‌رود؛ رقمی تقریباً برابر با بودجه پنتاگون.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/682579" target="_blank">📅 18:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682578">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc0df9e73b.mp4?token=ZxWlUR7a6qC_jNeO9LqbiY_Op-DxlCCCBSm39hlTBRyoRguYd369jMEcKXR3fHFStd8KIgvE5ZVLjIghCebYqQ_ibLMwIsiJDz5aR_PLKli5OGr5xbvZpbeRGsu8p7yqYPY8VSExL83JiBM6clXId8SeVjQP5Vvc1QDAUrzzPPzIwgJBB_5k7UjWaS2Z_rhpE0x9bkRNDXXdeitaK1SJ_spB54WKVhTD4mc6_fnostqyIoB818MuQRVtyy81QW1rV0iUPaCfqlj3HV9BAwNH9m9mO6LNNc2fGkDU_TzmJMqu8F8rnKJIy4TMZBwSgvBJCgCFpcIuQld9D0Uzx6tAyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc0df9e73b.mp4?token=ZxWlUR7a6qC_jNeO9LqbiY_Op-DxlCCCBSm39hlTBRyoRguYd369jMEcKXR3fHFStd8KIgvE5ZVLjIghCebYqQ_ibLMwIsiJDz5aR_PLKli5OGr5xbvZpbeRGsu8p7yqYPY8VSExL83JiBM6clXId8SeVjQP5Vvc1QDAUrzzPPzIwgJBB_5k7UjWaS2Z_rhpE0x9bkRNDXXdeitaK1SJ_spB54WKVhTD4mc6_fnostqyIoB818MuQRVtyy81QW1rV0iUPaCfqlj3HV9BAwNH9m9mO6LNNc2fGkDU_TzmJMqu8F8rnKJIy4TMZBwSgvBJCgCFpcIuQld9D0Uzx6tAyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نفتالی بنت، نخست‌وزیر سابق رژیم‌صهیونسیتی: ما ایالات متحده و جهان را از دست داده‌ایم
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/682578" target="_blank">📅 18:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682577">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epno5QGT94LJ8AsJcOFeDx3IFZO-vhsPErXeam_ZvCyxsPoWtKD8wF_5ogRYMJ_m6kwN3_xg2CLIbPv52TVcCApyAay450V0eIvu7R55uAZTKO6qLUuDCocSeA45hwH6qV7OJC4tEK-3eXl0zU7lwS2iLRmfGbskzwVvbLs4T_JSTYpSHJFTQHGxv2K8LDZlAsJ-81hAvZGVIM9pCVpWbSlkeOa3wWCOf9i4jCJszPXs5iI7KwMo3_kjMXfXmI8oqsiRTeQpPW9HtBve93iY3XeqDRr328vsbdky0x-2uXlPGvZVHlmebutNEtZO533jJPafkvcUajBlSFyfpFTeTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دانشمندی که نامش با پزشکی، شیمی و جست‌وجوی حقیقت درآمیخته است؛ زکریای رازی
🔹
محمد بن زکریای رازی، از بزرگ‌ترین دانشمندان ایرانی، تنها یک پزشک برجسته نبود؛ او در شیمی، داروسازی و علوم تجربی نیز آثار مهمی بر جای گذاشت. نگاه دقیق و تجربه‌گرایانه او به بیماری‌ها،…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/682577" target="_blank">📅 18:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682576">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVR8T2sFqbzUPz-jZF_rXrVrHURDjAUvf4T-ua6_sgqLDu6bd_DF9H7VAhcNGemmepD2Gl7g-hf4eUNgkbvmDetJSI4MRLhIAHIvPoDFeZymA0ZRbtfT1z5NqMawkH8IHQIadld9fRdqp8Sxb-V-Z3TC3pLsxkVXgOeWc_k-3YvwJifjmLMd_s2DA9x1fIjYA4z3wwgD091e5VB2UF-qkztlmiRfEDK202PTTarsR4NL15c4jqCZIJarfh4opoopKzew8BaXKieHR_HLfKc4QPN4pebmyCDx2lXWX0QiEwALx9e9oiMgoa60rlreJVf1fYy6UGyd9Gpf9RkROPoSPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
دفینه در صدر صندوق‌های طلای بازار
🔰
صندوق طلای دفینه با ثبت بازدهی ۴.۴۲ درصدی ارزش خالص دارایی‌ها (NAV) در یک ماه، در صدر صندوق‌های طلای بازار قرار گرفت؛
عملکردی که با توجه به سابقه کوتاه فعالیت این صندوق، توجه‌ها را به روند عملکرد آن جلب کرده است.
📎
مشاهده خبر
🔘
روابط عمومی هلدینگ مالی و سرمایه‌گذاری سینا
🔘
🌐
سایت
📲
بله
📲
ایتا
📲
تلگرام</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/682576" target="_blank">📅 18:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682575">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4_UE4D1kdpGOvl17BnpZ_ULcInS5n_tAE05p0ryk4aCtbqczmiPU_GLJac9M1ibNwp-cE-m4APTPeV-WUbKcRmoQ9SSib_Wgqs_W2onuzF8jiQMNQ_f7PEFpXKEmoGL52jSUEDLUWHxtzr4WZdZ8KFPDaMQScMfqQqqwAlEx7UVjoW-92wthxv4o46oYinjPNWPkq3s1otZkj3CcnXC4ulywwujV5qnqnzr4cMKBfrChb9LWvUrvGhc6uNhpfDTmK3t7qexQCfmJyrWthSOQQq_498MlALm2ffNK34d_Za552mb2iYXB9P0q9cu9VPq7GO7MCbB8oa7yU8NYwgwAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چاقی؛ بیماری مزمن یا ویژگی ظاهری؟
🔹
انجمن پزشکی آمریکا (AMA) در سال ۲۰۱۳ چاقی را به عنوان یک بیماری معرفی کرد. چاقی توسط چندین سازمان معتبر از جمله انجمن پزشکی آمریکا و مرکز کنترل و پیشگیری بیماری های آمریکا (CDC) به‌عنوان یک بیماری مزمن به رسمیت شناخته شده است.
🔹
تاکنون درمان چاقی در نظر افراد طاقت‌فرسا بوده و عوارض چاقی مانند بیماری‌های قلبی-عروقی و دیابت درمان این بیماری را سخت‌تر نیز کرده است. با این وجود با دردسترس قرار گرفتن راهکارهای نوین و ‌روز دنیا برای درمان چاقی مانند داروی تیرزپاتاید (Tirzepatide) داروسازی دکتر عبیدی با نام تجاری زیکورپا (
®
ZCorpa) و داروی سماگلوتاید (Semaglutide) کوبل دارو با نام تجاری ولوریتا (
®
Velorita)، مسیر درمان این بیماری در ایران نیز هموارتر شده است.
برای مطالعه متن کامل این خبر روی لینک زیر کلیک کنید:
https://abidipharma.com/health-items/obesity-chronic-disease/?utm_source=telegram&utm_medium=post&utm_campaign=pr</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/682575" target="_blank">📅 18:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682573">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7oW5WZQlAgktqkQ52Gx1wjR7dAUoxtjoSPwIjZ8ABTDkZMRNcqpvCkJ7ufzeK5H2BbYlKQJbnGHGkP7I0uKMAqXqnaEG1x0NxcRfKj63g119DFrx5fD7wQWnb-nVM75DXMaCWZMGpjvo4skLt-AvB0BwB-f-P7xmi2KbMoBygibzDpaw_fStwKC6_vc5VkKHxGLSqTNSRz8lau6q-fbxL5tIKFrGXFsbNP1pVVpWsE3x1L9bk40Yj5rI1q8kwnH_Ps-9fslqhP4eEtApi9oW4_L4UZdl3PbIGR8Hw8iy56XIkE7IEnsLPHY-outqg0w4oWpe0bKKfJBsvnfC911Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا کتاب‌خوانی از سبد فرهنگی مردم فاصله گرفت؟
🔸
در این نظرسنجی بیش از ۲۲ هزار نفر شرکت کردند که سهم روبیکا ۵۲، بله حدود ۲۹ و تلگرام ۱۹ درصد بوده است.
🔸
بیش از نیمی از شرکت‌کنندگان، جایگزینی شبکه‌های اجتماعی، ۱۵% ضعف در فرهنگ‌سازی و ۱۳% هم افزایش قیمت کتاب را از عوامل اصلی کاهش تمایل مردم به خواندن کتاب دانسته‌اند.
🔸
کاهش تمایل به کتاب‌خوانی تنها به گرانی کتاب وابسته نیست و عواملی مانند تغییر سبک مصرف محتوا و همچنین ضعف فرهنگ و عادت مطالعه، تأثیر مستقیمی بر این روند دارند.
@amarfact</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/682573" target="_blank">📅 17:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682572">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزارت صمت: محدودیت برق صنایع به یک روز کاهش یافت
.
🔹
وزارت علوم برگزاری دوره‌های کوتاه‌‍مدت با عناوین MBA و DBA را ممنوع کرد.
🔹
هیوا سیفی‌زاده، خواننده عمارت روبرو به چهار سال حبس تعزیزی محکوم شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/682572" target="_blank">📅 17:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682571">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzX-Q59MbHVBZApHGH3JamWq9aOeg_jD-d0gPCU0Ss_51Ftrc9aRZztVCbnEakSScTIPfEXaFRAATAw7G5Mf-NEue3g5DOefd5s5eYWXKYBjJ80ZjGVCLMVyc1O47-Bi6vpKzak2wu8_vjWIb9hD078oE3kWZ9Mv3eD1YLUJCMPKFKneyFNH7675fiQNMZiFN6sXFJjgSFSUxJumBfMfA61mOVr-icwTL69KnSjWwGTpzo_eXKX_5BWUcED02v2xP1jPxubBgXPACie1ucU7UaPyqunpGHPPDxPX7Xei4u7_BfgakBmOB-QoTdsgxswxd9KdmRXVVaXpKpKRpHQrcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصرف سالانه بنزین، در خودروهای جهان/ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/682571" target="_blank">📅 17:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682570">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ef4TRkO4qA29NXCLdB29hs-T9OFbNFbFHtQhuqcQbLAbVJhEPLaiIAcPbGl3JgBl2G_QbcP2Sd1u0QnD7gugdRve-3CjZ4toIxPTXc4TqAkw02EBo6NuYsCPsNKUx50SymSM7zCrjLJJTvQCoJ2Azvgq4gmC4jkoR9sqyZ_qb3mPlWb_Rx6GNxdQiKs22fvYAhNX4FYfQ6b-dyr4qn-8GA0Ynlp1nNChHxDiXcT2ccR36Z_aAzpsZEUo3pkA4_0GyHTcRBUPljhdElUvxN7aBTR_1OmS7BCvD9CN6BpXRkTo3ooXSphL3qhIIIrnS4dCi-Vh988s4jnQUDIOhvZlbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش صد دلاری قیمت انس جهانی طلا در دقایق اخیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/682570" target="_blank">📅 17:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682569">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjQNtYzF8We33ZF5Fy-tV9yNePJj7-E-oZHRDSs30oKN08j4rV0BsVQHWfGBpTuA8ZSaAsGP2CQjLNvLeDjAhtJwWC8pnfVBG9S1lMpMACErcevklw9q6qqXbU3sdeFfucLQ5PLY9p6f1m2f67UxM9GCIKLjEG-TkHbpIZQ8_8fAzjcNL4FNnXWYdSuozAiegTpgmTmrUALMA5J_BkEMnTQ-Z0DDd_Lqxip_Slh0sL-IaZOwXjjvN2wg_ELtIv0h7dB82a-hpK8k-pBdpcU8HsnXxok657A_hS_zmTDtytxL3LswVRYHTqNIk62zPObwUnxuMC4ZQyB8xwJTbi-vmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار قاآنی: غاصبان فلسطین در سرزمین‌های اشغالی دچار «سرطان اجتماعی» شده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/682569" target="_blank">📅 17:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682567">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFlOPvKyEMYILR4DJymeXj1e9mWrQbP1s_YnVdPptRQDLtmAg6-VYvYttyCyJdpN5Yp1G068eel3KjcpkmiMDDWi8laaMdcuClp-jApgWPDjk3tyWsA2witvGq9PHdo8Kr8ipmdozTIZtpcIR7wx95IR6_94PZPSRKlqKGPgvq-iffQe84qoGDUJUrcGh8Tty-Hxh0fChYn7AB_XVLyr1IFCmmqo55B7Au5whJvL8MI6ZYzZpF10lUQAA6m6sjFUy5fMiHBXwHEJlA6eNZLGe7Hi8V1nOfffHidKvuAC-INKShDGGF68LrYUf_OdfUPx1twgWjcVr4pQauQjWU6rWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e4f881dba.mp4?token=oU4CyWqsvJZ7AGhZT94XSt0dJhEh_AfW0YLUCjj3LC_39Alf5WPJwXQLDCMc4CuYIJlBNsK72jqqSjP9c8BBA7mLNlIBSZ_zv6gNtF01kRILceQdx0pgru_2VgWkoXyRxd_rWRThSp-KdIMlSuv5GsObi9SSYwRLw_NQ94Tj5xpHM2Qf33vMyExZHVyjU0W7NT-Vj2hV99T42vaLzxf65Q-vGEnC_VYlA9BiXRg9w2C0GF_mwr1xk9EA8s-rggHFMQaepYkuuIFSKSssSyOXu2ajbh1USOwiQCp6lVYCdvgBS-iRTmExJYLnydOYKWvsovp3un_Y6wAFtPy9C-yzdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e4f881dba.mp4?token=oU4CyWqsvJZ7AGhZT94XSt0dJhEh_AfW0YLUCjj3LC_39Alf5WPJwXQLDCMc4CuYIJlBNsK72jqqSjP9c8BBA7mLNlIBSZ_zv6gNtF01kRILceQdx0pgru_2VgWkoXyRxd_rWRThSp-KdIMlSuv5GsObi9SSYwRLw_NQ94Tj5xpHM2Qf33vMyExZHVyjU0W7NT-Vj2hV99T42vaLzxf65Q-vGEnC_VYlA9BiXRg9w2C0GF_mwr1xk9EA8s-rggHFMQaepYkuuIFSKSssSyOXu2ajbh1USOwiQCp6lVYCdvgBS-iRTmExJYLnydOYKWvsovp3un_Y6wAFtPy9C-yzdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ستاره بایرن و ابتلا به بیماری «صرع»/ موسیالا فوتبال را کنار نمی‌گذارد
🔹
بعد از بروز دو تشنج برای جمال موسیالا در طول کمتر از یک هفته، پزشکان معتقدند ستاره بایرن‌مونیخ مبتلا به بیماری صرع است، اما می‌تواند به فوتبال در سطح حرفه‌ای ادامه بدهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/682567" target="_blank">📅 17:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682565">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd0f7c4a9e.mp4?token=JU78C5xqJQoKL72ROsJj_2MhGjVNgj3pla0h5z0sd0RazQ-o7PDW-CWV_bcwcLhjp5hb1koVPVmN-y-_RZtaZPz0-ELcKzkududbWGBLZ8J51oeCa25FAd0BgY_pioYE1jC8348vaQhEV72PDll3jUaBu_2ggtmt-a_eVIFa9_5PSIUxzYM_hOE4fzu7KO8XDpi_6Iqf1G-bsqZhP2L1TbkiLUZcTbsRvV1N-A1PvLla2kvmMeGDtqo2oDNkm4X3h1-kd78OUQyKNz71kYqNuhoHCV5N7MbnVKfBscUzNKkaomBgARCW3Z0Lr5SX-XwXlvVO3GU8OzObll2aycUPwwubZEjB1WYGDGuqwXnUuG9SwwZOVAkaucruoOUO4Uwx__yu6AJgJ2m1NoXEc2e1rcg_w-DQC0tvS8_b9C00xLhRXO6xAb04wL2sUFjjSt9La6D9TEBUSXFvuEAY0dQGHcttA5F9nUk2qXOtoG3hSGQZyFG8SGcoRKY3-rwilVZ6blp2AQ55hCyUcWepSN0Kfz6WOco3KR-MMdcnVKkDCmcx1z8uF081vCid8e9_RtPBLJM9drSrvWQiGkY1Sn084h6H20HBDg2MqdMuy0-fiwQmQ7-DYOxvHluAIwH-cRmqKTJOPScaJCZ1tVE4qPIh9ALGuWLHyzN9nyTYQzd7xIU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd0f7c4a9e.mp4?token=JU78C5xqJQoKL72ROsJj_2MhGjVNgj3pla0h5z0sd0RazQ-o7PDW-CWV_bcwcLhjp5hb1koVPVmN-y-_RZtaZPz0-ELcKzkududbWGBLZ8J51oeCa25FAd0BgY_pioYE1jC8348vaQhEV72PDll3jUaBu_2ggtmt-a_eVIFa9_5PSIUxzYM_hOE4fzu7KO8XDpi_6Iqf1G-bsqZhP2L1TbkiLUZcTbsRvV1N-A1PvLla2kvmMeGDtqo2oDNkm4X3h1-kd78OUQyKNz71kYqNuhoHCV5N7MbnVKfBscUzNKkaomBgARCW3Z0Lr5SX-XwXlvVO3GU8OzObll2aycUPwwubZEjB1WYGDGuqwXnUuG9SwwZOVAkaucruoOUO4Uwx__yu6AJgJ2m1NoXEc2e1rcg_w-DQC0tvS8_b9C00xLhRXO6xAb04wL2sUFjjSt9La6D9TEBUSXFvuEAY0dQGHcttA5F9nUk2qXOtoG3hSGQZyFG8SGcoRKY3-rwilVZ6blp2AQ55hCyUcWepSN0Kfz6WOco3KR-MMdcnVKkDCmcx1z8uF081vCid8e9_RtPBLJM9drSrvWQiGkY1Sn084h6H20HBDg2MqdMuy0-fiwQmQ7-DYOxvHluAIwH-cRmqKTJOPScaJCZ1tVE4qPIh9ALGuWLHyzN9nyTYQzd7xIU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تغییر چهره بازیگران «متهم گریخت» بعد از دو دهه
🍿
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/682565" target="_blank">📅 17:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682564">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی فیلیمو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0gFeszLMuD-s4yrx_BDN1lsnPn3eowWZb1nxKaKkpPfVuOXvhAHYKm2k86P6aCEREHC0zAg6837u4kflWKCzgAybtEsOgqKEQ5Bluqo11dAILOCxyfxCrQuui2V-C6aBdZyDuyyek2LWBzOw0KlOECaevRuO47k9UL9PRf6ACOnPq5gsRRMypVxdBB7wHsGbgbfetb2NzPJzI6LezDhQh23A4DsOoEHw3QFvjG293GyPG1xtNoFYEJEfLR1Sk2Fppk-jVraWojCe6eZhHyBupNqxeMXBiKI6V9uJ7rCNWpf6C6aagXXxozoNgCGMKFymU2KvhtBPEYmaGQX1SO4ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تماشای سریال، هرجایی غیر از فیلیمو، کنکل
❌
📺
بعد از مدت‌ها انتظار٬ سریال محبوب
#کنکل
در
#فیلیمو
منتشر شد
علاوه بر کنکل،
#شفرونی
،
#بدنام
،
#زن_و_بچه
و هزاران فیلم و سریال، در دنیای تماشایی فیلیمو وجود داره
👍
🎁
همین حالا روی لینک زیر کلیک کن و تا ۵۰٪ تخفیف، برای خرید و یا تمدید اشتراک فیلیمو بگیر
🎁
➡️
r.filimo.com/TSalesummer
@filimo</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/682564" target="_blank">📅 17:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682563">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ce4d02ef.mp4?token=aA-OLFCgg1PZ7A-Ta8n3z7AK5vAnKQTPypDWCywBtBkBDHaBAMNhJb2YGbM6cYAoo3m01iE2LQRfhA1b08FTQCUUe97h0MomX1_F0Oms8ZsI7I4OrlKoJJYTH9L_q7s4t2-ycCpsg--y6rE9vbqAQdIB2aarrIPMFtL5o1C3BIENNs45Vt4u9E3hQB_mCrgI8GtqYm_3VP3cTNYXzpWJkdH5kz8_zocEGam5Uynr55255zzoBvJ8XUr8aqD2n9NUsuoQIkGhklJq3eyOuszRT1WfpsO14rptFyJAe7kipfMSkoNloJiyAO02X-NDw5nfbD0taa8U4G9WkacSsXa9Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ce4d02ef.mp4?token=aA-OLFCgg1PZ7A-Ta8n3z7AK5vAnKQTPypDWCywBtBkBDHaBAMNhJb2YGbM6cYAoo3m01iE2LQRfhA1b08FTQCUUe97h0MomX1_F0Oms8ZsI7I4OrlKoJJYTH9L_q7s4t2-ycCpsg--y6rE9vbqAQdIB2aarrIPMFtL5o1C3BIENNs45Vt4u9E3hQB_mCrgI8GtqYm_3VP3cTNYXzpWJkdH5kz8_zocEGam5Uynr55255zzoBvJ8XUr8aqD2n9NUsuoQIkGhklJq3eyOuszRT1WfpsO14rptFyJAe7kipfMSkoNloJiyAO02X-NDw5nfbD0taa8U4G9WkacSsXa9Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ارتش اسرائیل: یک فرمانده گروه در شاخه نظامی حماس را در منطقه النصیرات در مرکز نوار غزه هدف قرار دادیم
🔹
یک فرمانده حماس و شماری از همکاران او را در محله‌های الدرج و التفاح هدف قرار دادیم.
🔹
حماس ادعاهای ارتش اشغالگر درباره هدف قرار دادن فرماندهان مقاومت در مرکز شهر غزه را رد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/682563" target="_blank">📅 16:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682562">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcHZ-NnVc3szA0uDR-fXLT-spPPnpMWQ5MDDcVpCliEedL4BtVtDO_INFTJnuwukdkHQPcSL60rfvyugPHrQNGAsxJVXid_ohmIPofDe72CrefcUV1qQVwUDwsYrE7MN4goRJXQ8GYQFmwjy1ZL5QxQd4V8mH6TfRldENhPLlvMOQRvgK1kL4J-BHKJqGMif7JSsZr_ef9Jx4pTPQPWpr475uk-Ahhhd30y0zfttICqiefO3AS3_1GC3HTKF8Fu-mcUOy4We8kpx8_-cjh5LXOpQMVwvhj_P4ruH58kYCIl6t0hwdkkf2-nzXvyxivFB-nRWO-xs25hboT8HumH6hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قلمرو جدید ایران
🔹
دونالد ترامپ در ادامه مواضع جنجالی اخیر خود، در پستی نوشت تنگه هرمز؛ قلمرو جدید آمریکا. ادعایی که بیش از هر چیز، بیانگر رویکرد مداخله‌جویانه و نگاه توسعه‌طلبانه او به مناطق راهبردی جهان است. چنین تفکری، در صورت تبدیل‌شدن به سیاست عملی،…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/682562" target="_blank">📅 16:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682561">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کارگروه ویژۀ بنزین در مجلس تشکیل شد.
🔹
پرداخت حقوق مردادماه بازنشستگان تامین اجتماعی از ظهر فردا آغاز می‌شود.
🔹
قالیباف در دیدار با همتای عراقی: امریکا عامل بروز ناامنی در منطقه و اخلال در مسیر عادی تجارت است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/682561" target="_blank">📅 16:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682560">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ade319937f.mp4?token=uLcAWtRK_EN9yS_tksFFP0G8G8oix9cQRTBhla6ksRII9fWiOo2eAeUHPkvhvaJDbZVUU24lT3lqYcHb-zHL6PGEBzsbhFZGlOCjMxvTO4koiiSOmIwm2WWH4EB3kNyDAWB26tCUoAy6LtQpkE3Pxb6mq6pp9a-_1zxitKEGNeprZoMO7yM_WZRlPotJNnexTBf9zNxZssI2Sdzo8T21fCpDkh3zoQb_JLKUUiGqfKVkEGrP3NK3Dvwpv4XiCpDz5FYYMuOBF4xo7yZGhvzD3-c1UUTnVUmpR-ezxqwVDLDPgIHYIjNE-zgoWWTId2czKrKh7Sd6TAxKFgBwRXGVlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ade319937f.mp4?token=uLcAWtRK_EN9yS_tksFFP0G8G8oix9cQRTBhla6ksRII9fWiOo2eAeUHPkvhvaJDbZVUU24lT3lqYcHb-zHL6PGEBzsbhFZGlOCjMxvTO4koiiSOmIwm2WWH4EB3kNyDAWB26tCUoAy6LtQpkE3Pxb6mq6pp9a-_1zxitKEGNeprZoMO7yM_WZRlPotJNnexTBf9zNxZssI2Sdzo8T21fCpDkh3zoQb_JLKUUiGqfKVkEGrP3NK3Dvwpv4XiCpDz5FYYMuOBF4xo7yZGhvzD3-c1UUTnVUmpR-ezxqwVDLDPgIHYIjNE-zgoWWTId2czKrKh7Sd6TAxKFgBwRXGVlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی از کوه دماوند و کوهنوردها که باتوم را از ترس صاعقه در کوه رها کرده‌اند!
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/682560" target="_blank">📅 16:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682558">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-9gMqYwH_SepfTthhmX_O74JfRuG-pUfH6R2aRVPMkYqfm9m7mNbVcRfnvnoIyHeetuXFEeMzL8ZxbHr4ZLyLrmQ5tYA1g9BVvxeXyFlFMlK8l-_DhGsYbLPyuWZzSe2xQY6Xpbqwf8M-ke0Nm74NVBjho20lMRRc9ejRI3XcMiJMvZ4PeiCGzwjPyVibPjJ9ijG0ms2uzfhRK-2noQo8jvnkVLD-ljVh_5Pt4hJ2_cnWj2QDXIQDcQ6GroUftY9g_kDWKhrorFkmt1LGNNX3bCepT5z62HX-msPgkMdXFvH6nwB4sFvTfiJpU1dRpCAoq7Ru8K5k1fZmwalbceJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سالگرد عروج عارف بزرگ شیعه؛ آیت‌الله سیدعلی قاضی طباطبایی(ره)
🔹
امروز ۶ ربیع الاول سالروز وفات فقیه عارف میرزا علی آقا قاضی طباطبایی تبریزی است، او از برجسته‌ترین استادان اخلاق و عرفان نجف بود. همچنین در فقه، اصول، حدیث و تفسیر مهارت داشت، به تربیت شاگردان و آموزش سیر و سلوک می‌پرداخت و بزرگانی چون علامه طباطبایی در مکتب او پرورش یافتند.
🔹
آیت‌الله قاضی در ۶ ربیع‌الاول ۱۳۶۶ قمری دار فانی را وداع گفت و در وادی‌السلام نجف، در نزدیکی مقام حضرت ولی‌عصر(عج)، به خاک سپرده شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/682558" target="_blank">📅 16:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682557">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDU_L5TOXyyW1a5V704cmCBBQNsRlUAmZHTe1J-RhrOpA2rfx-53ssumTybJYcrzFds7kw5XX3wRaZpi51GL_kfLz5mpM5cbdmQu7nnDPLAcdcR62bfBKmMHAEZQY5JizLomVb8I45t7InU_vPU7vr9LQp22Y1QRpEX_zQYvcJnaPRAjlb8aDSkl_hHd_SLXOW2BQ6zYuKrFXRcHfWpXv3XMFC9suKjOTiL2UAYKsqUlT5eMfu7KvXFThtQ39Kwj-gKKWePJoNvN0Nqee0xxKtMkHzFJYa5dDoE84-FMl6_iHAf0nKEJy1nAjnjdyp3gVBMDcMu9n115HCbMobLcyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیاده‌گویی ترامپ قمارباز در تروث سوشال: تنگه هرمز؛ قلمرو جدید ایالات متحده #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/682557" target="_blank">📅 16:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682556">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1284b39cc0.mp4?token=Oe-Dvvhip7WTqs1-mTP0V6DPFSDEWElOPur_IlQnjoTkf4VhB9Of6bKFwjMiAO0Xu4oWlSWrcMBCgelHN6y_1zFELbUtRClHONjpqOt_h_2a99gq8zsUQJJnUjBtNTfIIKt3yu0Z2vMI98igV5sOMlmn8QgDZPJ5jwyaSjHRre3lYUVLhxADCb5n3wnmjxwAUSR6u3rXKVj00rDfM8fuy7PV5mynKhYC2LBqDM-Qdp5MLDerPSI2wyGtVEY0_WTyttPO8JLayB5J2ZeE49GPzlf2GJP_RG2WGjStPKOGg8YP0GdUh2XLuBi8ICi3AESo5DE18etW1e5zyJRzkeWeNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1284b39cc0.mp4?token=Oe-Dvvhip7WTqs1-mTP0V6DPFSDEWElOPur_IlQnjoTkf4VhB9Of6bKFwjMiAO0Xu4oWlSWrcMBCgelHN6y_1zFELbUtRClHONjpqOt_h_2a99gq8zsUQJJnUjBtNTfIIKt3yu0Z2vMI98igV5sOMlmn8QgDZPJ5jwyaSjHRre3lYUVLhxADCb5n3wnmjxwAUSR6u3rXKVj00rDfM8fuy7PV5mynKhYC2LBqDM-Qdp5MLDerPSI2wyGtVEY0_WTyttPO8JLayB5J2ZeE49GPzlf2GJP_RG2WGjStPKOGg8YP0GdUh2XLuBi8ICi3AESo5DE18etW1e5zyJRzkeWeNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودنویس مغناطیسی؛ ترکیب نوآوری و طراحی
🖋
🔹
این خودنویس شفاف با سازوکاری مغناطیسی، بدون نیاز به تعویض دستی جوهر دوباره پر می‌شود و نمونه‌ای جالب از مهندسی در ابزارهای روزمره است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/682556" target="_blank">📅 16:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682555">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
آسوشیتدپرس: آمریکا معتقد است عمان در مذاکرات با ایران امتیازات زیادی داده است
منابع مطلع به آسوشیتدپرس:
🔹
دولت ترامپ معتقد است عمان در مذاکرات با ایران درباره مدیریت تنگه هرمز بیش از حد امتیاز داده است.
🔹
واشنگتن به‌ویژه با توافق‌های مربوط به کنترل مشترک تردد در هرمز و دریافت عوارض از کشتی‌ها مخالف است و خواستار موضع سختگیرانه‌تر عمان در برابر ایران شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/682555" target="_blank">📅 16:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682554">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
سخنگوی نیروهای مسلح یمن: ما به قدرتی رسیده‌ایم که معادلات را تعیین می‌کنیم و با کمک خداوند موفق به تحمیل ۳ معادله به دشمن سعودی شده‌ایم
🔹
معادلهٔ اول: محاصره؛ به این معنا که ما دشمن را در محاصره‌ای محکم قرار داده‌ایم که هیچ کشتی‌ای نمی‌تواند از آن عبور…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/682554" target="_blank">📅 16:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682553">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9gFWIJrmLop-riZ_ZyBXQI_g2rV_Hu5pGDeYJbTNGBpi-lkTAp6Diwfpp9aK7TCPS8Q2IRC-JWcIQvghHCg175-a3Sq9-7TxcXyfLmWPxXlf9l_bpkW-470qgv__GKjkfjr2QJ2N5pME8yvWSBjDMSmrHsnnY4q6A3NWf3CzbnOrOa2Wj4qMDJDIEACLyrAwzfAQjNMTtznZppq9t7g0aIK_IWuSijTK5goUDmHlTBDMJZ10mx0sIaz0v1n7cox6-zwKVgEj2bQFMTO8l_81IZCwjmgYfCyxbu_aRdaViJVoOsU3wJHxjGMQH5ax1xM_fZvCWSth5li80HhePIhSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درسهای فردریک کبیر / فرمانروایی که توانست کشورش را تبدیل به امپراتوری کند
🔹
راز قدرت فردریک در اجرای گام به گام اصلاحات اجتماعی، نظامی و اقتصادی در سایه اقتدارعقلانی نظامی بود. او حاکم مقتدری بود که در عین اقتدار به دنبال اصلاحات روشنفکرانه بود. فردریک از روشنگران حمایت می کرد اما شورش را تاب نمی آورد، عاشق نوآوری های نظامی بود اما با تنبلی در ارتش و خروج از نظم پولادین سخت برخورد می کرد، دوستدار اقتصاد جدید و انقلاب در کشاورزی بود اما سخت جلوی تغییرات طبقاتی می ایستاد.
گزارش تاریخی خبرفوری را اینجا کلیک کنید
👇
khabarfoori.com/fa/tiny/news-3238189</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/682553" target="_blank">📅 16:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682552">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvTtNGmZTscUHJAEnOhIw7C8lrUYeUXyv6f3Pt0OVFCmqp_CwJFRKf_pSp1S5wGK-kSjGKC0gnthiu-kAM4-ss6p5zJmYIebVFq0o1j44WLRJSFxw3vud7iXaBlN5G8CYqU0XknGMqVxpepCwZnvgeBbOYfypTu907AkGQZOd7BvfcYRripxmtgqXsQcFPay1KnTuVnHTBhVJUciRxscw4Xwl2qeRGqxIQyJ_hYiIJO_PHRLUJYMtLaJITVgzBHnM0KYN7Aq4g2SkL_3vtJFB6a_dORBR7-K7ofzNNjMMxvbAlwLIObYToSe87TESYOtu83_blciS4ksC_QXHrbWBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نرخ‌های جدید کارمزد خدمات بانکی در سال ۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/682552" target="_blank">📅 16:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682551">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
سخنگوی نیروهای مسلح یمن: ما به قدرتی رسیده‌ایم که معادلات را تعیین می‌کنیم و با کمک خداوند موفق به تحمیل ۳ معادله به دشمن سعودی شده‌ایم
🔹
معادلهٔ اول: محاصره؛ به این معنا که ما دشمن را در محاصره‌ای محکم قرار داده‌ایم که هیچ کشتی‌ای نمی‌تواند از آن عبور کند.
🔹
معادلهٔ دوم: هدف‌قراردادن هرگونه تجمع نیروهای سعودی، در هر مکانی که باشند.
🔹
معادلهٔ سوم: حفظ حاکمیت یمن و مقابله با هرگونه نفوذ دشمن.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/682551" target="_blank">📅 16:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682550">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fe5969bde.mp4?token=aT3pagw8HNlfKeTjxieBxl4Pz3qa_3s-CAlV7JSzX-aAXUmj82NDFz7Fo4gq51TQih8W5j24qcmtS6j-MhL3T_cpWfrVx0WVxZVJCpJkgcYMb0wxPwq7mlUKhAe-ZdsU3I1LaAXK0Bhrp6NyI-w0HXzuP7xBpwPEh960iQVVhyw3V2l9JVWeKaSVFxex9PsLo3FvXyzZr1qBnIqrI_Cz8XSnLW1JBVhv-kvnN_xjcRxaQYIwSvJYD6ZwyqV5KVpD-QXlJnyRZCJaIvK09icS1dvH0nG1Hvi7Kyo-DnyQKNH5B2kbybE8gvgsBqbE9sJAgeP8s1glEa3kH-6I7v6dDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fe5969bde.mp4?token=aT3pagw8HNlfKeTjxieBxl4Pz3qa_3s-CAlV7JSzX-aAXUmj82NDFz7Fo4gq51TQih8W5j24qcmtS6j-MhL3T_cpWfrVx0WVxZVJCpJkgcYMb0wxPwq7mlUKhAe-ZdsU3I1LaAXK0Bhrp6NyI-w0HXzuP7xBpwPEh960iQVVhyw3V2l9JVWeKaSVFxex9PsLo3FvXyzZr1qBnIqrI_Cz8XSnLW1JBVhv-kvnN_xjcRxaQYIwSvJYD6ZwyqV5KVpD-QXlJnyRZCJaIvK09icS1dvH0nG1Hvi7Kyo-DnyQKNH5B2kbybE8gvgsBqbE9sJAgeP8s1glEa3kH-6I7v6dDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه تلخ انفجار تجمع گاز و سوختگی آتش‌نشان‌ها در مهاباد
#اخبار_کردستان
در فضای مجازی
👇
@Akhbarkordestan</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/682550" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682549">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a99cd2a4e.mp4?token=j770pPEwvoQsRNT6wftd4Jiiz3T_l6Fx1CcPV27OI0NrCMJYN1sANI5zSwsQ2_hXl95XWLOKYpXRDnxczc_Jfnc2Kcwk9xVH6iLy1qYdJ2bDuf1JXkHlYjghh4xxV1ULoHcEVS8KlvFUW6aPm5qGv6vLAj_6h1bLIOHiw19ILufAYy3Wm8hKWRH-FLewTQm6QnT6V8VsJ2vJHnL05tBcj3h3Xa3wzBxH0e1fJDOsMjloETR5_ouM5wvagti7qrukJ6gPuLr9IdSq1twgoyHazm4ko7Oa3oP53tExKgyvroHdeBFk_9R1jbE9La3ilxopahT3L00io3LiP9vC4t_l5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a99cd2a4e.mp4?token=j770pPEwvoQsRNT6wftd4Jiiz3T_l6Fx1CcPV27OI0NrCMJYN1sANI5zSwsQ2_hXl95XWLOKYpXRDnxczc_Jfnc2Kcwk9xVH6iLy1qYdJ2bDuf1JXkHlYjghh4xxV1ULoHcEVS8KlvFUW6aPm5qGv6vLAj_6h1bLIOHiw19ILufAYy3Wm8hKWRH-FLewTQm6QnT6V8VsJ2vJHnL05tBcj3h3Xa3wzBxH0e1fJDOsMjloETR5_ouM5wvagti7qrukJ6gPuLr9IdSq1twgoyHazm4ko7Oa3oP53tExKgyvroHdeBFk_9R1jbE9La3ilxopahT3L00io3LiP9vC4t_l5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁨
♦️
سوال‌ همیشگی اینه! طلا بخریم یا دلار؟؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/682549" target="_blank">📅 16:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682548">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
اردوغان: تنها راه حل درگیری میان آمریکا و ایران مذاکره است.
🔹
امشب، آخرین مهلت ثبت‌نام آزمون ارشد علوم پزشکی است.
🔹
بغداد از تهران برای استثنا قائل شدن در صادرات نفت از تنگه هرمز برای این کشور درخواست کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/682548" target="_blank">📅 16:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682547">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQgJnf9TIy9_0FqVMLqFUV4AWy6nRuh_53JSRFpvBvXivuNTd_NLzBpL0ukV84zjxJC_ibBzufvGDTacICXRsFWMqtdaJ6uZCboA5OMng72xnYkccZ1OOWBN5mQSRDTwZYmCUfkdrHjIY8VL1L32W2YENUfv4PolDSHgD7plQNULiJbY1m-6mAXNW0I4RnsA8ofZzFZCRaZyA6gRSOAMRalG2Z2DwlPsIhgFuSk-irCO-XZt2wMeLtceQMpqlS1gqVDWhLdwkoJQJRJz0p3tt0hYjSDBRGIork2Aqn6u_JkFYrapEeU59DQfBpnrart4XBGPgjIJavtwptSjVuEcBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دشت دریاسر، مازندران
🇮🇷
🔹
پوریا فرج‌پور
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/682547" target="_blank">📅 15:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682546">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qhbs9CDmxMGv3WzqrIN66Ah-A0Sevb5Wj0J1oKLIO-ugOsU5LDAvM28vKA5RJfbjiDN89nhMqX_oi5SxHT3pYkhcJaAJvQFG_aWUTurOz8aH36qCuU5CcAfFLzQCesEUTlZXB8NtOxh0nzDSz2Bp3q2jyieD5ZjK7FAt79xklVHErHaTxIWVylJIkspCA26co2nkdCePZzYxCAfiQIUNaD88FhdyMg0dx25jze8P7Mwu3QnEnYouvhDEd0jXDNOa_DDwzTX7mtWeZdfiCUJ_OaX-9XoyiWiuyTU2cD7UGnPD100egR8Cm_6fwbN4dlgRBnpYeCkw2oA1FC3UfO0jeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو شرط ضروری برای صدور مجوز سقط قانونی
🔸
سالانه حدود ۱۱ هزار درخواست سقط جنین قانونی برای بررسی و صدور مجوز به سازمان پزشکی قانونی کشور ارائه می‌شود.
🔸
برای سقط قانونی، بارداری باید کمتر از ۱۸ هفته و پنج روز باشد و سن جنین نیز با سونوگرافی اوایل بارداری تأیید شود.
@amarfact</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/682546" target="_blank">📅 15:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682545">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
مصوبۀ حمایت از خریداران خودرو باطل شد
سخنگوی شورای رقابت:
🔹
دیوان عدالت اداری مصوبه ۴۷۳ شورای رقابت را که برای حمایت از خریداران خودرو در سال ۱۴۰۰ تصویب شده بود، باطل کرد.
🔹
بر اساس این مصوبه، پیش‌پرداخت خودرو در قراردادها مشمول افزایش قیمت نمی‌شد و فقط مبلغ باقی‌مانده تغییر می‌کرد؛ اما با لغو آن، در صورت افزایش قیمت خودرو، کل مبلغ قرارداد می‌تواند مشمول افزایش قیمت شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/682545" target="_blank">📅 15:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682544">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBlyxtuDvp4ttuOXA_sMQ0Ya27YPmdFzZudXV78DKZVGYCmK3yCsE2E0HJk7BuY9t9aqeUkjwtprX---6ZiVQ0V1WLJvseGQO_QL63YJr39Y84gIZMxvaunNpYa7JA7P1wo18PTlXX550Z1UI5HzovRZ_ukXOzbXnfajEIgsc1Crockmlh4ovLHN7yNAJuwEoVX6X-welaY9TCOON7SNifJk9KMiG76hQeozoN4KtzJ2RiSS-qETgqykMIYsWoMAaGd2REwtQofJQKZJXvyShdw67GqIfCFuGYEiuzKRA0TKdRUhzmFNAt1m57AxR9_93FjxlGjlf70vucnAnHFTJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا رادارهای آماده فرار می‌سازد
🔹
پس از آنکه ایران در جریان جنگ، پایگاه‌ها و تجهیزات نظامی آمریکا در منطقه از جمله رادار AN/TPY-۲ در اردن را هدف قرار داد، واشنگتن به‌دنبال نسل تازه‌ای از رادارهاست که ظرف چند ساعت مستقر و در چند دقیقه جمع‌آوری شوند تا پیش از رسیدن آتش دشمن از محل بگریزند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/682544" target="_blank">📅 15:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682543">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc6cb8826.mp4?token=D6kcUBnr64eBxGlO7ipR95bw2IZrOPJmrHMQz_mVY8zFxiM1EdrHvzdKZDvFTGZaBtmVAMD3WLmkpHb6e4yH9sjgNxWmIGU6nuxO7EphqKEiuhnHy9Wobqr4pTcgXMlPQp4xShDDHu9YaHkqqd_6VOJgsYBjLb6zAxjES55Mv-bj51JKncYFMEf90C9QfRuVvOR960GNMjRRpC34Na4_0oYlz_bMHH_LcDRm7nl35fK1M3BeMZivCExR09_uS_ELXWaTE0leGk8FzFm2CndEVmhBUKhNfid0d_K_wS4PwzrhH5LsbH_jO52FuDiTuTCy7qtou2eKzSKqwY8LgI2VAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc6cb8826.mp4?token=D6kcUBnr64eBxGlO7ipR95bw2IZrOPJmrHMQz_mVY8zFxiM1EdrHvzdKZDvFTGZaBtmVAMD3WLmkpHb6e4yH9sjgNxWmIGU6nuxO7EphqKEiuhnHy9Wobqr4pTcgXMlPQp4xShDDHu9YaHkqqd_6VOJgsYBjLb6zAxjES55Mv-bj51JKncYFMEf90C9QfRuVvOR960GNMjRRpC34Na4_0oYlz_bMHH_LcDRm7nl35fK1M3BeMZivCExR09_uS_ELXWaTE0leGk8FzFm2CndEVmhBUKhNfid0d_K_wS4PwzrhH5LsbH_jO52FuDiTuTCy7qtou2eKzSKqwY8LgI2VAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا آیت‌الله سید مجتبی خامنه‌ای در همه پیام‌هایشان از نقش مردم حرف می‌زنند؟/
تلویزیون اینترنتی مدار
تماشای کامل این گفتگو در
👇
https://youtu.be/1mRMJX8Ack4?si=Y_ZOwFaceXt2tW1k
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/682543" target="_blank">📅 15:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682542">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
مصوبه تازه مجلس؛ حبس برای ارتباط با رسانه‌ها و نهادهای خارجی
🔹
مجلس با ۱۸۳ رأی موافق طرح مقابله با نفوذ سرویس‌های اطلاعاتی و نهادهای بیگانه را تصویب کرد.
🔹
طبق این طرح، مصاحبه یا ارتباط با رسانه‌های آمریکایی و صهیونیستی یا رسانه‌های تأمین‌شده توسط آنها می‌تواند…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/682542" target="_blank">📅 15:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682541">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf54f0cb2b.mp4?token=eZgvdbgXKuDNRSoWB0WKTWCUX8xhV7Fa-yfeVVXWq1PQLHbr744CIYatyKfnUYIFA9jzQ3t1_LVRkx6l-gZNAlgFXsotiOx5Y4IAOevxOqXPfXQ_o8VnGYZojTgBYuK3eyykR3zuELLqUWmPHe-MegHzW5Jv7zoAjF6jD5OktSDJ_h8Qsc76cb5YbAd3TcrkeRQuE9mYFppIVIgL6EaR_a8lZ4caftyu2ar1wKr24ZJ5pVTVzv4Gl57xbUFO1X6z0mj15SgS6VeMj637A2HvaHO-LoeWn5qfY7INw7k8VoDSzLak2MYy9unYu5MekPew44wO9EwcZXIaeJRidaHoug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf54f0cb2b.mp4?token=eZgvdbgXKuDNRSoWB0WKTWCUX8xhV7Fa-yfeVVXWq1PQLHbr744CIYatyKfnUYIFA9jzQ3t1_LVRkx6l-gZNAlgFXsotiOx5Y4IAOevxOqXPfXQ_o8VnGYZojTgBYuK3eyykR3zuELLqUWmPHe-MegHzW5Jv7zoAjF6jD5OktSDJ_h8Qsc76cb5YbAd3TcrkeRQuE9mYFppIVIgL6EaR_a8lZ4caftyu2ar1wKr24ZJ5pVTVzv4Gl57xbUFO1X6z0mj15SgS6VeMj637A2HvaHO-LoeWn5qfY7INw7k8VoDSzLak2MYy9unYu5MekPew44wO9EwcZXIaeJRidaHoug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران من، تو را نمی‌شود دید و عاشق نشد؛ هر گوشه‌ات، شعری‌ست که قلبم از بر دارد
🤍
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/682541" target="_blank">📅 15:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682540">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3919778d6.mp4?token=FqHyHng46SnXiIjM5UvJphcRdiLvBaSmuKapXEX0o0YKsO29Pfww5S895NeT9UVZxk9w6UAqJf_zdNcPa6wMhnB8sJWOwYNVVtRhpHGZtFClO0UR0gG674DOUjvT2i86_tN8AOuo96lyQllBoXxbC8sG8EMmaGFPRzWbNSeNCyUh6uKxky2JAaDRu46P3qMd6nilq1nEsWzLCYI2cqc4d-3aJywOzLRbujBG0ZC1Zvd7SnCiSER3XdF-P8gOzglKmLeETHJlmmoMIMdQMNoZWu-NTsk53kFxSNm5hM27AQh4uwxQJzYjsEnR12l_fjXV5zmyhQDN1JXRD60jbAuLuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3919778d6.mp4?token=FqHyHng46SnXiIjM5UvJphcRdiLvBaSmuKapXEX0o0YKsO29Pfww5S895NeT9UVZxk9w6UAqJf_zdNcPa6wMhnB8sJWOwYNVVtRhpHGZtFClO0UR0gG674DOUjvT2i86_tN8AOuo96lyQllBoXxbC8sG8EMmaGFPRzWbNSeNCyUh6uKxky2JAaDRu46P3qMd6nilq1nEsWzLCYI2cqc4d-3aJywOzLRbujBG0ZC1Zvd7SnCiSER3XdF-P8gOzglKmLeETHJlmmoMIMdQMNoZWu-NTsk53kFxSNm5hM27AQh4uwxQJzYjsEnR12l_fjXV5zmyhQDN1JXRD60jbAuLuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض به جنایت‌های اسرائیل در قلب تل‌آویو
🔹
اعضای حزب عربی «حدش» در تل‌آویو با اجرای یک تجمع اعتراضی، نسبت به جنگ غزه و جنایات اسرائیل در کرانه باختری اعتراض کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/682540" target="_blank">📅 15:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682539">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سهم مردم از واگذاری ایران‌خودرو چه بود؟
🔹
خودرونامه: از تغییر مدیریت ایران‌خودرو با عنوان واگذاری به بخش خصوصی، انتظار می‌رفت مسیر این خودروساز به‌طور ملموس تغییر کند؛ اما پرسش اینجاست: خروجی این تغییر برای مصرف‌کننده چه بوده است؟
🔹
محصول جدید و متفاوت کجاست؟
🔹
آیا مصرف کننده در برابر پولی که می‌پردازد واقعا خودروی باکیفیت، ایمن و با امکانات دریافت میکند؟
🔹
خرابی و مراجعات گارانتی چقدر کاهش یافته؟
🔹
رضایت مشتری و کیفیت خدمات پس از فروش چه تغییری کرده؟ و مهم‌تر از همه، چرا کارنامه‌ای شفاف و عددی از این شاخص‌ها منتشر نمی‌شود؟
🔹
اگر واگذاری ایران‌خودرو یک تجربه موفق بوده، اکنون زمان انتشار یک گزارش قابل سنجش از عملکرد پیش و پس از واگذاری است؛ گزارشی که نشان دهد سهم مصرف‌کننده از این تغییر دقیقاً چه بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/682539" target="_blank">📅 15:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682535">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N0GkH1yptd1YwWuFKM8FzkWuAPdhvvp5Eqf25ASje3r5FM2dQ_6HkyKcbhQGnKMIYfTwgHapOc2XRM1PHT0ZfT5CUOxat9OeHj9NF1Uo2jv413AR117dcb2UpLEAEWYia-uqQ0MueLYgir5wYGBKefH45VFuk4RfUcXf35m-SL8qrDgntqPB2nzC9OPP_fg3WxAvbiHsJZuLxQVNpxJHtinBV21ragNs66ZY24Xdi-Oz0IHi6tbWw0hq7le8DNqQPPHYdYhcqwbRATyzytgjAbtfzEitlbXlcnNW3b6IuL1elNa-HnBnp3gdkhW7C6Gz9PFyt7xNXyfQGguOMF_9aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RtVS7MeZr4puQOHAopH7RoPKwip2HtP2Po-dt35trJ07XQHHdmRM9CYJOZCc1wXOfN7PbkZ3WhbI5IAYUdGhwmr-Xto4U8HD3A1EzTB9hrfgrwInZq7NzZnlJjwKuEUzc1YtyNwirZacLWTi3xje0JwSiqon58978pGJZR4D--sAUlzITeh6wdWhzoQNc7vwvxTmqFvnikvIELzgT-ipgE-uyCwNkVMM0S0AcUuNaMMSeoZzNHK9zU7p5dZMi9a1X_jLw9Z5Ok47oDQ3O-E1iiYy2DrYWlOLGX8B8w3HgC3MpK9yu9DcxOhXe12Jap5hNKeiVUrmgVcQC_bHTIL1UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uRXkr70ceJcTCwj_lChVMLKBgKcXUs5YAf_ucuTiCAF_YnHA8mqe7P3yu15NSC53rI_rZc-TytF0kfBwMqfWndFfZ4hd34kZCvPKJKcpRXjRp-a0hxJUM_DO_pxMANQLGDD-XeAS0sIOZT3BqZ5G_mB-krdVK9eo2ZfEAhfRFrOYF0X8BsSkWGsxRD2tOocEBs2y09Hxog_HcupB62DtymEQK4d3LKZO3Gwmf1qYCYxmgYvK-1fzaYN42v5VARG-LkDpdCqS45yTo4HdKkJsiCebOfJKB5Dg7CxohTrgeaN_yg1OgYz3UacgKgla6pCspWAB3F3RotUBEnzzTLdo2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OCYh30m-HRW4bjSLKejE5JFCohqssG1VjWQHrMkmvE0IQWKoYtSIBiy7l65kxk9_35XXIzzYXvIkyiQpQAjL4UUiWqG4lzc3Mgnv3VUgk8f-nKzTounCUnoRjTKHdyJ_uOpS59KfOarrR1GBxxR1-KO9B1sNXxlDEBuyTyp18WC1Cmsw9RbCOT4lIGQvydKXfOlaCT1If8TWDk-bfH708HAjGisuvebdSzjBL38EdKptKjdDJbBTVVWziA0go0keUGjagEWwhsx_HPLlUVtmgI3ngnUP11zccff_IbqM8TSWa2RUS3pq3aKf8a9928WpxnPj_FfzL6xsY0dCkr8Y8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رفاقت طوطی با گله کرکس‌ها!
🦜
🔹
ماجرا وقتی عجیب‌تر میشه که بدونید این ماکائو بعد از از دست دادن جفتش، نه‌تنها گله خودش رو ترک کرد، بلکه غذای مورد علاقه‌اش رو هم تغییر داد تا کنار کرکس‌ها بمونه.
🔹
باورکردنی نیست ولی ازش یه فیلم گرفتن که در حال دعوا برای سهمش از یه ماهی مرده هست!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/682535" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682534">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYfKGKQ0_uLxatcvapQoOR2WLXsqSXGwJc8uMYVC9LhnuHft8yjAi5a9ntZrNgf6rygyCq3I95HMou_qejvaIygpVyHoLO3n-ZYV-PzJj45fWIY36Y5YWg-I60ZfLv7m0f5qQTvUj-QFDUkQYPoJI62dvm7u2Nla2R58rl2Z2x8NsHKTgWL1MFQilVxgbeVYJJRj29X0Fm1rB2Ts__wyLjt9MWxMU7XL3Es5roNjntqdFB5Qc_h_eDysarb2QOzfVJJ5wYNFxwoz8NgoTv1FCjdtIyeEwNmsnAai2ANzv1kN0ZZanmIOgz7gAESZN-uk1YeaPtLxKhXxEV2_It9PRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف خطاب به حاج قاسم و ابومهدی: بدانید که تا به نتیجه رساندن آرمان‌های شما از پا نخواهیم نشست
🔹
در جنگ رمضان قدرت مقاومت ایران را درک کردند/مقاومت از مرزهای ایران و عراق و منطقه فراتر رفته و جهانی شده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/682534" target="_blank">📅 14:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682533">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851bc2ea30.mp4?token=c3eXxNaL8e3Vos28tTwx_l12Es-C7dgnKea8cTjtcF8n_WRIMMseAqz053aFL05jIJgNIlfvOUmZWZSVZv5RQ5eGJUvd_OCnE0QA71yLg1547FJO2Vetc1J420uJ_U1qrAvP9pRjb4yHVvQvepB1BM8aD2bByQ41xrygNj08gl2yIcVWzzFmln2y4-TowQTwJBbZ1JCLZY5HDkdR2JcRq-1ZzLWLxenBfSVvL7uQfm0Li0pHi3NFIXUIqjv_FbJJ7scrDv_Ts0K4boGGJ9om8-7YJtU0ir1y4aRbiUy7Wia8VUlvIGdhdU8m90NaAOKrQoydnekiRIH6zm572M-n_j6o7XZAsyrKFBknugZ7A3kN54Ikpd6vkrc4QdXUYoMo-Lj_gOOq60ckuCoA5NUrgjCKnCee53n0H3j1bFWV2hMx-RdAQCHu6pENO7b3fYaJxsS-H6NW-UsJ0ETnxNcul5LXlPKxVof8HeTcU0meXFpsU0sNLFOj17nEIVPFmFXooj05W8PNJlLBWLaaIXSSSGopVTkmTRn_BKFKeMcvDreu9qT3M4vPwoSRLDFS249uEZFaAw6ezUEeZMryY-LIO7CLIDO9F_qtVR7VwyNhQRAheJZtmbO6XNsAZKGCqbpmuu76KCT9b7PMCstZ6Y88lr40H_EqxJKL_jhSu0HH-SU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851bc2ea30.mp4?token=c3eXxNaL8e3Vos28tTwx_l12Es-C7dgnKea8cTjtcF8n_WRIMMseAqz053aFL05jIJgNIlfvOUmZWZSVZv5RQ5eGJUvd_OCnE0QA71yLg1547FJO2Vetc1J420uJ_U1qrAvP9pRjb4yHVvQvepB1BM8aD2bByQ41xrygNj08gl2yIcVWzzFmln2y4-TowQTwJBbZ1JCLZY5HDkdR2JcRq-1ZzLWLxenBfSVvL7uQfm0Li0pHi3NFIXUIqjv_FbJJ7scrDv_Ts0K4boGGJ9om8-7YJtU0ir1y4aRbiUy7Wia8VUlvIGdhdU8m90NaAOKrQoydnekiRIH6zm572M-n_j6o7XZAsyrKFBknugZ7A3kN54Ikpd6vkrc4QdXUYoMo-Lj_gOOq60ckuCoA5NUrgjCKnCee53n0H3j1bFWV2hMx-RdAQCHu6pENO7b3fYaJxsS-H6NW-UsJ0ETnxNcul5LXlPKxVof8HeTcU0meXFpsU0sNLFOj17nEIVPFmFXooj05W8PNJlLBWLaaIXSSSGopVTkmTRn_BKFKeMcvDreu9qT3M4vPwoSRLDFS249uEZFaAw6ezUEeZMryY-LIO7CLIDO9F_qtVR7VwyNhQRAheJZtmbO6XNsAZKGCqbpmuu76KCT9b7PMCstZ6Y88lr40H_EqxJKL_jhSu0HH-SU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اجرای آتشین ارکستر دانمارکی با فلفل‌های تند
🌶
🔹
نوازندگان ارکستر مجلسی ملی دانمارک پیش از اجرای یک قطعه کلاسیک، فلفل‌های فوق‌تند گوست‌پپر و کارولینا ریپر خوردند و با وجود اشک و سرفه، اجرا را تا پایان ادامه دادند؛ ویدئوی این چالش عجیب در فضای مجازی وایرال شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/682533" target="_blank">📅 14:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682532">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZNHbWTtDUz6TBL4UIxB4zAfys0GYnlV-S5HIeDwf3qHfWWBZn6JQu9ndcvJNRUU0nBmloOzuwOREN5PtK8TsHhOX0JkV5s94rVA-N_xjYA1mk16AT3RgP01hKCC5OYq3HXTsLM3QLnl11zopzenq3vGZ7Bay5lyuHTozF8bb1TgxDjogBRzd-arlJgTS5Em0-zQD5kFBbSu6x0d7aLj9WK0jxuJYFbu2IR3lnMUD85pisAJn9BQ3AXQ4m3Q0w0Aeb8tRIYpZBuowDadSbfubZbJIyA-6bLPVkF-ZB0qjeGi3xOyq3h4DZ2G6pZ-k75ZvyAWIKHQ-mDYB94NQTLzTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرانسه از اخراج دو کارمند سفارت ایران در این کشور خبر داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/682532" target="_blank">📅 14:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682528">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b644451e1.mp4?token=oDK58xGTiK8RcaekNOrbvLg4b4xyXZn3V0EgyHB3PQeokqyxz90yw8oti-BN6uT1r8fF1EajbwZKZKwpK2huxJ9FgAePCM0VXK-dVCakrEAObjXqJb58R1sW7amFIFHM9fL8XNgmS8c_7xBOJmgLATw-TpJYZtqdQMep35YePD5RV0x3crEIeNXAeLUf9TVlXWVZEBRXxwa6LVrcASv41e0vdxSDU1szheUYotXsPkCMPmVB02-1796qSyZzZZxU-IOjLfueRxHSDb8UTUtzsEFk_FL9iIEhNqrBpmjZeXYSebwVKiqmLY-g0rdCGagdLCva5uMGr4-53JdnFwDTjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b644451e1.mp4?token=oDK58xGTiK8RcaekNOrbvLg4b4xyXZn3V0EgyHB3PQeokqyxz90yw8oti-BN6uT1r8fF1EajbwZKZKwpK2huxJ9FgAePCM0VXK-dVCakrEAObjXqJb58R1sW7amFIFHM9fL8XNgmS8c_7xBOJmgLATw-TpJYZtqdQMep35YePD5RV0x3crEIeNXAeLUf9TVlXWVZEBRXxwa6LVrcASv41e0vdxSDU1szheUYotXsPkCMPmVB02-1796qSyZzZZxU-IOjLfueRxHSDb8UTUtzsEFk_FL9iIEhNqrBpmjZeXYSebwVKiqmLY-g0rdCGagdLCva5uMGr4-53JdnFwDTjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استودلاگیل؛ شاهکار طبیعی ایسلند
🔹
دره استودلاگیل در ایسلند با ستون‌های عظیم بازالتی خود، یکی از شگفت‌انگیزترین مناظر طبیعی این کشور به‌شمار می‌رود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/682528" target="_blank">📅 14:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682521">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZmUXvu2n-HNFALRtM2xpatAPycpjPYAibvtSXX8jSTmD9e3sNjP3pZxVGPDWVc5mu6ESgERTnDSfObDIyG2yvc3KGP4D4SiBkNPvvQfdQn8miUoI9w3s2Hu8LSVYLuqxeHGEABMyErM-iOVCcjCYkjB9EVJAZm3YOurphHW-MTHjfolqwXmOs0fWGCDoM7cnTt6IR5bAibeeSogOjY15Bqz3I6y-3HYpMSqo-rimnNSlTkBbsYyuuO6WQc-7Hpho1bsk14ku1Er4v7TXQ3F4bk5QFVkux6LF7LuQIFTxPGcYYomisUygC4LYJNuNPRTaC1RlDkpnUZS23HOJ9g-V8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PDY5ipFYq0UmR9BIMObYD_eSBmcW5E13Uzs7LQkDAO_O18l6ezd6IpfzAlHaeaVWEL1XBrQMt1tOTaYSuHkV3aTEJWvxLduK1t6SQjJdkTsn97mYVe2ymNSgx0BX0dGDaYDv4A7WJN0jSmsTxhzzmPNj5h34N5TesiYqfnI5fNeOeFZLN4Uy5EBOuot0_4QhhFX7WkovxLSlUNYX94Di__QvE0TFtzkq4TgnHc1bryBqXqXSyXT_FoEe40hFLS96cS79asSKl2q4ec7SsbUHxqBdtJks3PrpustBEyw67LTYgrGd2KGnQFdOp9i43b7HPyckzsVVBaPiSV2_sTiyyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mfbr1i4NJzm09-OxP_MFMnV2AgjaXmfFn23SvVqT_59rbm8t27lrzxwj3RFXXJBLF5bVZQ9t79inVUFK7etpW2VVkt743mgNKAYkgLtZlNk3CcDnrCdNsQqHi14TglJ7WelqEQmotH7TIHrLyjGZDC3g0SW0JmLj5tvEeYNSZwC2Y4Pi9mHbb0gKXKXLD1INtxaczYL-RUXRxtS4T6JRhiCVYef6bXIBM-uT5h4Cwe9JLptd5F9anjz2KGpy5SDCNK_WXh1NOZrbXGiJQM973EK3dZvKeqWfiK0R8ewXjXLhwd6IFxKds4TVpeh_cAgATmuqp57F-POKBE-hOMQozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlDPPY59N1VzwjDhhifejbRvCUYHLbZQYDn7y8KBFF8hLkTQYN1uLTiUREeTqmudTURmZzOOJ6UD4Ma2wdJORrn8iotNJWgVuL78yAX05aCFnp4K7PlZxE6T75lSxjjeWNTnILzgxz0oUyyJJbPrXqtsgWTQbCpWGmvNpw09SxLZdvH1u75aiYc--pu7bjd3t-nr_i9Ycg1nXmJy7vLuONdc63DUx_179oPJ0LaQnSuRouzFzZ3hCkXR9MdNQO8YQa8Od3SNq6iFBBCyTZuOy7zg-2RRu-FsSZT6TvnPVFaNNFV9G0Khdaat9xlhJh-LmPvlig6RkFrPPjdJWTY56g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s21rTIpr-9g5gag6FPTMfQAfFa9gzR2CI9q6sypTCzX9ru-KAAsbPldS61cU0J5P_5Qpx4yV8T45h319r3xHUzQLuSnxTfB__92IbD2qJRVXr3NFz2tnbntoGiSMLsdk6yLdtAHfSsLaXQJS5xCjmNbvtbbLEWN-8fBA09sdwmpHujxPSsVOT0MRbYbTL-wTUkxLZnhcJYOCjtPFyO7h3AgDEPXnA0pu3dh1gYImS3wGWKQrRg8yDNpMlcGlrpcj1Hg6EeVOYQPK9oJN3vIkehlR9cjiPyhr0HDxMs_V1EpVfEVID7SvhNtbIUW-U7XTv6Dqur1ppMVAQrwykdCdnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خیلی راحت ‌و آسون تی‌شرت‌هایی که دوست نداری رو تبدیل به شلوارک کن
🤩
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/682521" target="_blank">📅 14:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682518">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/682518" target="_blank">📅 13:42 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
