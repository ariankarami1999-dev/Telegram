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
<img src="https://cdn4.telesco.pe/file/ullXou7PZ7gIyA9p8zaw5DYdgTi3Xo5EuYh2MZD2vyKidwaewUA_vFUQKaFdLyWSRxODIjVDPJbAGhiXHP1Em3LGlCp_iJEN0OcC6RU--gEtElNuiitTMlyv89E1X8UCo_6fQaFV_OLOqc22UA9V5DXeC8JAIIeAKMlJ1OatSHRzJngEY4ykkirGfP3Tztti8uoG7K5AZs0tstkXdx1_RhIlKZu7baQN5uMQOE39NKvpIgocpwoDXmp2Pfjd5azLYNvrtDVet1TjDZyXidt6PfWjVLYxXHNHfGcXeCto4PDTKUXn0Y36BlgPj7dQeqAd-fno43mkrxZ-YCEFcI8JHg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.05M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 12:53:12</div>
<hr>

<div class="tg-post" id="msg-652484">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSB7iQwb3wWhgGewd6KwWjWfQkovoSdbSjxC-_hzJug9ABQeXfhAwhsGAc6e54vbOVbA8sVrtev0V5mwQySFkzvCS_kMJg4EE3J32vFKP9wU_HIwSoWmEfN9P0ciWynZQBeI9Bw2liDA6W47uRg0iDy5mvdYKZQ_NRjhm7lXRm6MJrjy0fLC9oZuHfaDxSYjwBJQsXwB2G1bVO3WNv8MXZ4YyVX6MWkT87eyXvfc6RMTGVspAdowdCRpA882GoV_h5aMrxS1PrZrbxo7Mo5flrrsl_J5VtyxgrnX5aZbb8hvtPkpPBGaQb_lX8Arv37KpKqmxRtmWax09MddILuj6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خسارت‌های جنگ به واحدهای مسکونی و تجاری تهران
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 386 · <a href="https://t.me/akhbarefori/652484" target="_blank">📅 12:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652483">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGQvS0nHVoSIPkCTrLAxexCgMHpictzsYnbR09FoPwhcfqG3ghtEhfkxEfl_oIX_fMAbFO60ZqFlUfYgKOw1lawtSzmHNlPqthBRHt54ynPPrffQ0tjb6iuUn8HlxTS2ewFtXguUdChly7mJiFtZHLXaYNCpsAqhR8EfJKW-LCrriMM3wdV0ZxyQxohI_7Vt-pzQykWWpWsv5Ib4F4ffQGyfaTE1JzyT1ho6tWb0Qp77Ar22SlIssjtJWfhg_P0-0cKhopWM9vTuVVD4EBfkI6RYmdmPEjNDTZ9xuNX4gFGLu1zfijm1SQpjYrIwZB80mepX3HVK_MaljX-UxMa1FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش نگرانی در اسرائیل از جنگ فرسایشی با حزب‌الله
🔹
در میان نظامیان و شهرک‌نشینان صهیونیست، پرسش‌ها درباره‌ فایده‌مند بودن ادامه‌ جنگ با حزب‌الله، با توجه به وضعیت فرسایشی فزاینده‌ای که نیروهای اشغالگر با آن روبرو هستند و موفقیت حزب‌الله در تحمیل معادلات میدانی جدید در جبهه شمالی، در حال افزایش است.
🔹
به‌ویژه پس از انتشار فیلم‌های ویدئویی که توسط دوربین‌های پهپادهای تهاجمی مقاومت گرفته شده و هدف‌گیری دقیق مواضع، خودروها و سربازان اشغالگر را نشان می‌دهد؛ عملیات مقاومت به محور اصلی بحث‌ها در داخل اراضی اشغالی تبدیل شده است.
🔹
این فیلم‌ها به شدت گرفتن احساس خشم و سرخوردگی در میان محافل نظامی و شهرک‌نشینان کمک کرده است، ضمن اینکه انتقادها از ناتوانی کابینه و ارتش در متوقف ساختن این فرسایش مداوم که نیروهای اشغالگر از نظر تلفات انسانی و تجهیزات متحمل می‌شوند، در حال افزایش است؛ واقعیتی که رسانه‌ها و محافل مختلف اسرائیلی نیز به آن اذعان دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 451 · <a href="https://t.me/akhbarefori/652483" target="_blank">📅 12:49 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652482">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cr5sg3lLBq5uxsAClsIwJL2ts0KmHnUdGn2S5a3Ba9jgCPITiw5rjD33YbQqr8OTmCVMzzgLNgFi5wApCQ6Iy7oyUqRh43PMrryXPQlyAMUkQtktdZiKkY4EVkLuWA0xRu7d61PFUMMOKzHFdzrDvQfuhspKBjJL1eEv2qYqBsFVSqFjmoLeBbqxEY0U9QX9cb2-wYs7493qySNL21XJ4YtmLSDuryphWO71t5Iog1X5A7ezCw1lxm07oirYZGJkvyL0QJry0SucVfRM1peUZx-1MykyOLfgjrBkMPvjVC-YY8UOOC0T4BBvRA4Zs8HMEp7GDRb_eQ-4lCjlGmCwIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش بی‌سابقه ذخایر نفتی آمریکا؛ سریع‌ترین افت تاریخ ثبت شد
🔹
ذخایر راهبردی نفت آمریکا (SPR) در هفته گذشته با کاهش ۸.۶ میلیون بشکه‌ای مواجه شد. این رقم بزرگ‌ترین افت هفتگی ثبت‌ شده تاکنون است.
🔹
با این کاهش، مجموع افت به ۳۱ میلیون بشکه رسیده است؛ سطحی که ذخایر را به پایین‌ترین میزان از اکتبر ۲۰۲۴ رسانده است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/akhbarefori/652482" target="_blank">📅 12:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652481">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjW8Uk53yGuaZfpSqu0t8H3DJWXNlHrV5dbbwDh2pxRCuO0PRHXzT_wgjhYnMjoZt919wrILHlXBN18BwOSdJZArT7HO1FJxOWeGbHfWlIt0sLBzhUG1xx7sn_X3Car9zuy_f6JHnVeT5rXbjv2M2t_iLxUPUWfc_JIy950u9aLfdtAPtxcDnAE8GQeuE4hNhRghFcAz4iDOT0b7UKigqR4zx8VtLZX3CM1CresReBwowKcXZlhatqkJDADBtKEwFQyQPwkZ00tLr7GPRk_MAn3OED2ZeNXuwYjr8-cf7thq2PsRkYWyxwYeKsneSKLJg4hmf_KmV6DsPh9YoFYJsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلومبرگ: انسداد تنگه هرمز زنجیره‌های تأمین جهانی «تراشه» را مختل کرده و ممکن است خطوط تولید تلفن‌های هوشمند را متوقف کند
🔹
بحران در تنگه هرمز اکنون به قلب صنعت فناوری نفوذ کرده و باعث اختلال شدید در حمل‌ونقل مواد خام حیاتی برای تولید نیمه‌رسانه‌ها شده است.
🔹
این بن‌بست لجستیکی، تولیدکنندگان بزرگ را مجبور کرده تا با صرف هزینه‌های گزاف، مسیرهای جایگزین هوایی را انتخاب کنند که ظرفیت آن‌ها برای پاسخگویی به حجم تقاضای بازار کافی نیست.
🔹
کمبود مواد اولیه ناشی از بسته شدن تنگه هرمز، منجر به طولانی شدن زمان تحویل تجهیزات الکترونیکی و افزایش قیمت‌ها در بازارهای جهانی شده است.
🔹
غول‌های فناوری هشدار می‌دهند که اگر این وضعیت بیش از چند هفته دیگر ادامه یابد، خطوط تولید گوشی‌های هوشمند و خودروهای برقی در سراسر جهان با توقف‌های مقطعی روبه‌رو خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/akhbarefori/652481" target="_blank">📅 12:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652480">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaeI4ZM1VyrY_iipAcacwKtIzXJ01b53NoEiXXEdpibKGHV3woqLJlvOLJ6Id3PzIp8kC7JEvEJfld8UVknamMCkMBtg_3XhuyQPR74ZCMoYDrrnUQ4EDjWUefgtqWWfs0AMmDx_GlICd5SxDYn_qEO8-1V8kvRe2bGAMixnT2qWXl98-8RdgQZuUONiqt4KdzLZKq3ZPy2EqVfCvZ7ovjCd4Y2skLmTLXwxgGDvrwbznBQllTDFZhVS7R6MVgAXu6epIVHIvdNzShSMuQBrzY_Lzv46VKIBM195ytAePIiSyfpa5rF_IXviJS1BcS7QP8uGf08axFT0nbAXxEXCug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از صدای انفجار تا سکوت سردخانه؛ روایتی از امداد و نجات در مدرسه میناب
🔹
امدادگران هلال احمر، جزو نخستین نفراتی بودند که خود را به مدرسه شجره طیبه میناب رساندند و تلاش آن‌ها برای نجات جان‌ انسان‌ها در این مدرسه جاودانه شد.
🔹
مدرسه شجره طیبه در میناب، که زمانی مملو از صدای دانش‌آموزان و انرژیِ یادگیری بود، اکنون به تلی از آوار و سنگ‌های شکسته تبدیل شده است.
🔹
سنگ‌ها و آجرهایی که خاطرات بسیاری را به قلب ظاهراً نفوذناپذیرشان سپرده‌اند. صحنه ویرانی این مدرسه نه تنها تلخ و غم‌انگیز، بلکه آمیخته‌ای از درد و بیداری است.
🔹
کلاس‌هایی که روزگاری مرکز علم و دانش بودند، اکنون زیر آوار فرو رفته‌اند و سکوتی فریادگونه فضا را پر کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/akhbarefori/652480" target="_blank">📅 12:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652479">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85704039ec.mp4?token=YmmBZV692WAF-7jAAZlYnBBiqInA7F7MmzByEbR3dV1IitPWHB1cTpM5qhtYlsi7gtuRuHR6aYpjBj7DG7K5H4vMPI5tNMvAHD_UoY7Qb2P_KC0VwA7Y7b5J2HalsojAhGLuibyH5zG67iK2D3nMr7wZSlymVDI5ohfOUYXUU-IVxYieqfwGIZA4qqS8u79ZB_fS6gUzmHh2xS2GYSjcJWqTUJwgou74J0jOxd6tR7fARHUskQDgO7Q7vId_-A1tKg_l0i2emEoNW4MGwRofUKABBKBrFTgBOv0-8N0tW-deHT-9zlxZQfFoLKVNz5udP8nVuntrFCE2qSw40h8KYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85704039ec.mp4?token=YmmBZV692WAF-7jAAZlYnBBiqInA7F7MmzByEbR3dV1IitPWHB1cTpM5qhtYlsi7gtuRuHR6aYpjBj7DG7K5H4vMPI5tNMvAHD_UoY7Qb2P_KC0VwA7Y7b5J2HalsojAhGLuibyH5zG67iK2D3nMr7wZSlymVDI5ohfOUYXUU-IVxYieqfwGIZA4qqS8u79ZB_fS6gUzmHh2xS2GYSjcJWqTUJwgou74J0jOxd6tR7fARHUskQDgO7Q7vId_-A1tKg_l0i2emEoNW4MGwRofUKABBKBrFTgBOv0-8N0tW-deHT-9zlxZQfFoLKVNz5udP8nVuntrFCE2qSw40h8KYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکید عضو کمیسیون کشاورزی بر پرداخت سریع مطالبات گندمکاران
🔹
رفیعی: مبلغ اختصاص یافته برای گندم و نان نباید در جای دیگری هزینه شود.
🔹
اگر دولت در پرداخت پول گندم به کشاورزان بدقولی کند؛ مسیر مصرف گندم تغییر می کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/akhbarefori/652479" target="_blank">📅 12:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652478">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
محدودیت‌های شدید ایرانی‌ها در امارات؛ عراق جایگزین جبل‌علی شد!
فرشید فرزانگان، عضو کمیسیون تسهیل تجارت و توسعه صادرات اتاق تهران در
#گفتگو
با خبرفوری:
🔹
گزارش‌های میدانی از محدودیت برای ایرانی‌ها در امارات حکایت دارد؛ از تمدید نشدن ویزا و اقامت تا محدودیت حساب‌های بانکی و کند شدن فعالیت شرکت‌ها.
🔹
با وجود نامشخص بودن آمار کالاهای مانده در جبل‌علی، مسیر عراق برای انتقال کالا فعال شده اما زمان‌برتر و پرهزینه‌تر است. معمولا مسیرهای جایگزین برای ورود کالاهایی که در جبل علی هستند به کشور، هند، پاکستان و عراق است.
@TV_Fori</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/akhbarefori/652478" target="_blank">📅 12:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652477">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vD_D6_rgYqOXyjesOx3zv3nY0u9rRkAFAqURpsfUdkO5RcBYIIMvrIWMN-cjTTFXrut0FEYlfaKypPG-YoF7hdzyhczIZSSUj-bC_4Mm45P-Qc8ip0egK6VZfTSsdW5cv_NIxYSyw4w8Gpn7WpIXz3BipN1jBgne9Rc-b-NgXh45TLc2ScWv9OlngsQlUsCox6b8leDV7BQ4k0srXzHvc8BYrZxt5JvueXPVeiLcpXPG-Y0aQIIw3cpYya0WlypERPgcqyHZKVR8H1h1jAhUr_U151EIvJrmTaG-sij4w0fms9GIQHpGbZZZRYjswkpFQ-SnA-Ql4LGBtyV631vJrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گندم به بازار سیاه رفت!
🔹
رئیس بنیاد ملی گندم‌کاران: در حالی که وضعیت تولید گندم امسال بهتر از پارسال ارزیابی شده تا امروز یک میلیون و ۴۰۰ هزار تن از کشاورزان خریداری شده که نسبت به پارسال ۲۸۰ هزار تن کمتر خریداری شده.
🔹
کارشناس کشاورزی ابراهیم مرادزاده علاقه نداشتن کشاورزان برای فروش گندم به دولت را هشداری برای مصرف گندم در خوراک دام می‌داند.
🔹
اکنون قیمت هر کیلو ذرت دامی در بازار آزاد اگر پیدا شود ۶۰ هزار و قیمت گندم ۴۹ هزار است و مرغدار گندم ارزان را جایگزین ذرت گران به‌عنوان خوراک مرغ می‌کند.
🔹
رئیس بنیاد ملی گندم‌کاران می‌گوید دولت پس از ۴۵ روز هنوز ریالی به کشاروزی نداده و انگیزۀ آنها را برای فروش به دلال بیشتر و احتمال ورود گندم به چرخۀ خوراک دام و تهدید خودکفایی را افزایش داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/akhbarefori/652477" target="_blank">📅 12:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652476">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca50329bf.mp4?token=QmMB7uK80TH1EBeXCXwcNO7ss9oKoITHMXSDSQYftodA4y90pubcxfYlIDcHcJxkejsfR0a64xo-_rgoculoXJ3iHBANstjDETeJcTRfhElq0kAVJEIrDS8Z6iuS9GM3nlOFP5sr5LYF74xI71gHsnO-BscDByAKXfrZ8fSzB5NAGw7cJA9U5uH2Vk4T--unhLjzZtfnBT7xOOM6UstirutUFsJViHIEIXzLhF9AjbAfDcSwRNzz5P6-gK1bOub18UPJtw0L3xcT85UX4efQGqRpig0p4BK_xyqR-8mj2IALGH_FDRwxveaNMW_Epw4k8XRsjl_ag-oNlJZFfVXsLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca50329bf.mp4?token=QmMB7uK80TH1EBeXCXwcNO7ss9oKoITHMXSDSQYftodA4y90pubcxfYlIDcHcJxkejsfR0a64xo-_rgoculoXJ3iHBANstjDETeJcTRfhElq0kAVJEIrDS8Z6iuS9GM3nlOFP5sr5LYF74xI71gHsnO-BscDByAKXfrZ8fSzB5NAGw7cJA9U5uH2Vk4T--unhLjzZtfnBT7xOOM6UstirutUFsJViHIEIXzLhF9AjbAfDcSwRNzz5P6-gK1bOub18UPJtw0L3xcT85UX4efQGqRpig0p4BK_xyqR-8mj2IALGH_FDRwxveaNMW_Epw4k8XRsjl_ag-oNlJZFfVXsLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خنثی‌سازی صدها اقدام خرابکارانه و حمایت دولت از کارگران آسیب‌دیده
🔹
سخنگوی وزارت کشور : با تسلط کامل نیروهای امنیتی، انتظامی و اطلاعاتی و همکاری مردم، صدها مورد اقدام خرابکارانه و تلاش برای نفوذ یا انتقال تجهیزات مخرب به کشور در همان مراحل اولیه شناسایی و خنثی شده است.
🔹
دولت برای حمایت از کارگران، پرداخت تسهیلات به کارگاه‌ها، تأمین مواد اولیه، واردات اقلام مورد نیاز و اجرای بیمه بیکاری را در دستور کار قرار داده تا از بیکاری گسترده جلوگیری شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/akhbarefori/652476" target="_blank">📅 11:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652475">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/040c9dda98.mp4?token=imKA2-p6FSI4sABn-gstcVk_uTsw0KCMLMEhjaxyF64dnqtHqZDeHFgI5zpCERleTspvFu6Pvh6FphYtHa_UqL10cLSpathaBnAmlr5g-9Xrx1k0h9KK7GiaiUa3rTe8RF3hb_GuMW5cWwlbhIxU-FUzaOn73JGIx-x3WbWqCz6FYtBel1QFLUochI7VKsBW7N7Eqb_A9LTQQV3v3f1tVcriJ9q0nFizaQexLhilGt1JaYKNnXadhvyVvx1D9h8RGUiC7Zbu8rHQMgKsrYChtin0D7a3OXq4MkYFvSblCMajLG3T5JQ8GbLlnnGv-nA6YcT6mvO8DHcniM5SHOSvFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/040c9dda98.mp4?token=imKA2-p6FSI4sABn-gstcVk_uTsw0KCMLMEhjaxyF64dnqtHqZDeHFgI5zpCERleTspvFu6Pvh6FphYtHa_UqL10cLSpathaBnAmlr5g-9Xrx1k0h9KK7GiaiUa3rTe8RF3hb_GuMW5cWwlbhIxU-FUzaOn73JGIx-x3WbWqCz6FYtBel1QFLUochI7VKsBW7N7Eqb_A9LTQQV3v3f1tVcriJ9q0nFizaQexLhilGt1JaYKNnXadhvyVvx1D9h8RGUiC7Zbu8rHQMgKsrYChtin0D7a3OXq4MkYFvSblCMajLG3T5JQ8GbLlnnGv-nA6YcT6mvO8DHcniM5SHOSvFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرتضوی: شهید رئیسی ایران قوی را در سایۀ اجرای عدالت اجتماعی تعریف کرده بودند
🔹
وزیر رفاه دولت سیزدهم: اولین دستوری که آیت‌الله رئیسی به من دادند موضوع کالابرگ بود. به من گفتتند به هر شکل ممکن باید این کار عملیاتی و اجرایی شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/akhbarefori/652475" target="_blank">📅 11:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652474">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npV_eu7pM_xshIEayPIToU3jaSJvF5skfMQCGrUGptX6cehFi2z7iVTO8vu2WyGPDMaWMNWPa5MTlHByDBgurYZ5rTUDmVqee7yzP1815WBwYNPYsHBevGnMh95rZmCTBYjzgaEuzqNS4i8Dv2S_kKNDQj0Bq0RjsdzLNxLoDuQo58ZbjfAb5EcV_X5W9rd91gbNCyy5eVR1JrCtQm4hCQ862eDLIPkWKyspiA923lolEQ28ppCr2zPRcLN-rvik6EmZM8HrqXiH-F-8Mk0dLhCYY6AdkLJp2t81rS2O6B4wUiZzc04UtmywQs1zHQAn24N9PmaxgbTw0VSKLZu-YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یارانه کتاب به عموم مردم تعلق می‌گیرد
🔹
مدیر اجرایی هفتمین نمایشگاه مجازی کتاب گفت: امسال نحوه اختصاص یارانه تفاوت یافته است و یارانه برای عموم مردم تعلق می‌گیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/akhbarefori/652474" target="_blank">📅 11:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652473">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrAAojBIkcxP8tBFB6JVkGcr1B6vfnYDMLonxveWQtkSla2sSYcJ75gS8e4yHT9zsdQKdVCzwewY790NYjHjRIGeheVKd-itTkAVAld5tGaTodyoinEYJA0fh9JYMdPaeJeVf8O5PTvNGb70wwyYsIyHk9Z0Id7BsSfYwaiyZqwHx_Qj79EWRiob9B9ss8kiiEDMbohcjHmlij7nDB5f7OLAnPmHVG7K_90rGqonvV5h-XICyn3J-_IGDMmwAH6UgUtbRh2hLGBLAJctu1XK2yvHmRVPYSSt1O1eZbAlV2nufKE-Gk8i4l5PsmQyvgWYVyD2lNnJiFIdsSNv9RYlwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نه_به_پلاستیک، فقط با انتخاب‌های بهتر
🔹
چند جایگزین ساده، تفاوتی بزرگ ایجاد می‌کند   شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/akhbarefori/652473" target="_blank">📅 11:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652472">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3205d7f0e4.mp4?token=IDrDvccCmVfvGnefvCyhqOzTX4lYjyrgu2rBbR6O_ANTKT68fhmWDcplWQILMOVFWGWXKLfGbOpm0Ny1p3ckL_DR-tt8wRp5ww9RQIpb1n-kLI3x6j9BN2xlTddNembHhW-XSuBHMrC60PnAitdYbEdi4lZ50mvn6OP1PaVl_-lx0GWbEZfN2KqBj1LWEev75avlbtysBPaZ8L2jtucM3P_PmlbnAtGnpacSjaAJa1CJ0RHHb3e_vxtgi6xe3c3c_lnrGKG9XlgWLUSL6XGtYwBsRDtxwZxe-Z-RB07XZYz4Bhluh1yFhp0v86FQCxtOaFGjSwgwUL1FgDmbhq8alw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3205d7f0e4.mp4?token=IDrDvccCmVfvGnefvCyhqOzTX4lYjyrgu2rBbR6O_ANTKT68fhmWDcplWQILMOVFWGWXKLfGbOpm0Ny1p3ckL_DR-tt8wRp5ww9RQIpb1n-kLI3x6j9BN2xlTddNembHhW-XSuBHMrC60PnAitdYbEdi4lZ50mvn6OP1PaVl_-lx0GWbEZfN2KqBj1LWEev75avlbtysBPaZ8L2jtucM3P_PmlbnAtGnpacSjaAJa1CJ0RHHb3e_vxtgi6xe3c3c_lnrGKG9XlgWLUSL6XGtYwBsRDtxwZxe-Z-RB07XZYz4Bhluh1yFhp0v86FQCxtOaFGjSwgwUL1FgDmbhq8alw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت کشور: سیاست رسمی نظام و وزارت کشور جلوگیری قاطع از هر اقدامی است که باعث اخلال در انسجام شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/akhbarefori/652472" target="_blank">📅 11:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652471">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
رژیم صهیونیستی درصدد جذب مزدوران برای جبران کمبود نیرو
🔹
مقام ارشد سابق دولتی رژیم صهیونیستی: ارتش به شدت با کمبود نیرو مواجه است. حدود ۱۵۰۰۰ سرباز کم دارد که حداقل ۹۰۰۰ نفر از آنها باید آماده جنگ باشند. جذب ۱۲۰۰۰ سرباز مزدور در ازای دستمزدی سخاوتمندانه ایده خوبی است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/akhbarefori/652471" target="_blank">📅 11:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652470">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88ff319359.mp4?token=MT_0pZtcRx1LBY4lent8dDRzSJ5h0ZA22zrO3-DsxyGBrxJHb72VaKXRN_xAJf-SuZx6YUfxx0lAErj6HhnhLlMyzXrcoQ-HuL03itbWk_u2ixaATrLuZ5W_Upf7ftDllJO0szfJ2AY0I3NG-qkv1C9Xmb8GY1ZZ2Kmkv_LXrtVgT0gXssDuPCqbc660imoMhpaxLnrIzatMlckNaVlm2x2jUZKhLVgtINdrBFAkz84diU1E8Yk0QOW5T2LNXMwWX0HW30uFE2eYXkVPrrRNNMXBme7tn4NJ4eC6_Zbb0aWEUzUaMJieQPkqUDxc7jVDj1U06rOrdwZhoRc5W_2XKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88ff319359.mp4?token=MT_0pZtcRx1LBY4lent8dDRzSJ5h0ZA22zrO3-DsxyGBrxJHb72VaKXRN_xAJf-SuZx6YUfxx0lAErj6HhnhLlMyzXrcoQ-HuL03itbWk_u2ixaATrLuZ5W_Upf7ftDllJO0szfJ2AY0I3NG-qkv1C9Xmb8GY1ZZ2Kmkv_LXrtVgT0gXssDuPCqbc660imoMhpaxLnrIzatMlckNaVlm2x2jUZKhLVgtINdrBFAkz84diU1E8Yk0QOW5T2LNXMwWX0HW30uFE2eYXkVPrrRNNMXBme7tn4NJ4eC6_Zbb0aWEUzUaMJieQPkqUDxc7jVDj1U06rOrdwZhoRc5W_2XKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور خانم مجری شبکه سه با اسلحه روی آنتن زنده تلویزیون
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/akhbarefori/652470" target="_blank">📅 11:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652469">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c603726281.mp4?token=AfpMitdNTetR13U1sLGxyWBtlBxYHyOO7bOB4Z3othKjvUQ6dMBlymb7QfIcS-L2zRSpMXU4R6uDcD93mzofeEvlyXex9rfMovpJ0ns7IoBtM9VwM3otB_iWPoax37ike_pX_6YkmsfvmsBRNhfTA4cZaP7R1dA11e-DpDxA3DP0u_b5V_7_x5xAwG3a3c8KyGHVRh59QNrmR998azGj0RMhW8pCkSJVLRxhhramgaxDGhXdQ-GBMTstDmux2wF3ELkpXxMbSxTETpLdvB19z0HOfqHiP54flDZFCJ_uowTQFGie11NY2CkZtQB9HAX1dF2XOa4qA6kJN6713TMXkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c603726281.mp4?token=AfpMitdNTetR13U1sLGxyWBtlBxYHyOO7bOB4Z3othKjvUQ6dMBlymb7QfIcS-L2zRSpMXU4R6uDcD93mzofeEvlyXex9rfMovpJ0ns7IoBtM9VwM3otB_iWPoax37ike_pX_6YkmsfvmsBRNhfTA4cZaP7R1dA11e-DpDxA3DP0u_b5V_7_x5xAwG3a3c8KyGHVRh59QNrmR998azGj0RMhW8pCkSJVLRxhhramgaxDGhXdQ-GBMTstDmux2wF3ELkpXxMbSxTETpLdvB19z0HOfqHiP54flDZFCJ_uowTQFGie11NY2CkZtQB9HAX1dF2XOa4qA6kJN6713TMXkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت کشور: ما در همه زمینه‌ها آماده‌ایم؛ هم برای جنگ و هم برای پشتیبانی از رزمندگان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/akhbarefori/652469" target="_blank">📅 11:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652468">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BX_TK1u-HMdOCzw3lcJnSuxkuPVyBh3IsD9KA9pRuIC3dBdkFJhBDxIDR4N1QPkEQlaGOShYlNmYWONcaJDcKikj7bsIbKLJN5HfP9q0XAP1hpcWYJi9nvy86WLBAc2j4dU4F1bcQ3tj1jRQA41rAXJNDEXampYwgF6YKXjGF8RtSYwyphN-728pDN6JCSLAXh4J6LyhBvTdcVp2SPtQJAWdNqeSIIQccU3AN5XRVJSPSRRnXRgQ33tS3F8kBFJ2bNpqYUCCQiYd_iEsx1kTnTLMjqt98GjumErh33lud3UbHHIANTNTeIsQ1u8tJP5TINeZRnsX29xUtroDBBIaVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میدل ایست آی: چرا اسرائیل در ایران دانشگاه‌‌ها را بمباران و در آمریکا دانشگاه‌ها را خفه می‌کند؟
🔹
کارزار اسرائیل علیه آموزش عالی که بسیاری از محققان آن را «آموزش‌کشی» می‌نامند، بازتاب‌دهنده تاریخچه طولانی خصومت اسرائیل با هر فرهنگ آکادمیکی است که نتواند بر آن سلطه یابد.
🔹
هدف قرار دادن مراکز علمی در ایران و تلاش برای خفه کردن صدای منتقدان در دانشگاه‌های آمریکا، بخشی از یک راهبرد سیستماتیک برای از بین بردن نهادهای تولید دانش مستقل است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/akhbarefori/652468" target="_blank">📅 11:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652467">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52b2ab860.mp4?token=fZrh616lLbI9PkT9XmSJARUx26gcuJqH2HESPZehcb6cYcNZ1O83uAKXSiRPrKiLbe4sVQhApR1idnL9vXLoXXmntOwGMoPezgDMSYESQlTdzQDL76nN6cLNJ4i_LH4vOk_NKta1vTF-kSL5oOumVk6SvvpJ7PXM6O-_zK14bq-hUbuih2LCAhNerAdQcVJx_RKa30dz2OJG0t3Bm0q8cU-U0wN8ZodmHev6_sjZ1H_NIfTDbJI2ojbjDvGdodw-W8KRfIMNsCErFMyImWkcoJ2nQbPlVN8caJzNRTaM7s71TzR1TxjsV3W_Xf5ztspfZs_tTpC9nCZOYmoro_nyAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52b2ab860.mp4?token=fZrh616lLbI9PkT9XmSJARUx26gcuJqH2HESPZehcb6cYcNZ1O83uAKXSiRPrKiLbe4sVQhApR1idnL9vXLoXXmntOwGMoPezgDMSYESQlTdzQDL76nN6cLNJ4i_LH4vOk_NKta1vTF-kSL5oOumVk6SvvpJ7PXM6O-_zK14bq-hUbuih2LCAhNerAdQcVJx_RKa30dz2OJG0t3Bm0q8cU-U0wN8ZodmHev6_sjZ1H_NIfTDbJI2ojbjDvGdodw-W8KRfIMNsCErFMyImWkcoJ2nQbPlVN8caJzNRTaM7s71TzR1TxjsV3W_Xf5ztspfZs_tTpC9nCZOYmoro_nyAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون سیاسی وزیر کشور: مردم به شایعات و اخبار توجه نکنند منتظریم جنگ تمام شود تا تقویم انتخابات را اعلام کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/akhbarefori/652467" target="_blank">📅 10:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652464">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dRYoo4RpbfqVBSY6C2NcI-oL-BNFw5nPMYpdjqdGOh4QNk79kK16JuWIhQPWLid6gg6iWY_gVOASJfzm-eT5yyAjKBzk5g_Q5RrXtYoCXXYZLZQhX0pWTsFbG9ZhNiQ3tplMnqZtGt1pX7U8i6Q4i6rvavx1pETxdm95NWGBS0icNNqCwVJ_gAyITv4sEnkTM_53SD7nO_QHVSJUbpPJGdrxelUQWgdeD2r-ElIJOZlHWiZ3CYwVdGPPqh0YopANeP4Cr1TYUTmH-6oDTEbjGkZ-o9PtiPvOqNh7m589rzlRhd8rsoZYfv9olcsYsqOc8Ea7-fU-d6ZqoGC83IKH9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jOxZAlDXYVqLDmbbEdJs6JQW3hja4zuRjYV0TjP5ATyvQCazCThXb5XE-AH0kLhd7d-wf6_8kyPGc_5jWWolU_hUGl2cjrBsfcaCW8hLUE9IwT-_zJoEGyHwGG6g5Elnh9ZytsPLbY3jk_upBbFNZP4QsZxZOPLYS-RmFFEybJ8BmDipfucKPhjlccaP2EHJ9-AVc5cecMTuoc9vQdPdxbmOqxaIB2LD7DYznBYom8IWkL7xvxwr-78AwAoajweUF4Pj9tfNJPG5-bezSyNxgN5yxhhlrqpMksuGgBdBMKrv7DZwEV0PHCxcTgMJGPYszMAT7WIqHk5KpwKJDqv2Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HwORLid2RMgpPU_A3XjHq7A6z5uoDIkFJ3W4kHhpP8RSG81iDprbbxgTh3JVSmsWsImJNSghquQmsbn4GtJIOPG2sUO1sXgpHBjxTzyevhI0Rt9K3LS5G8J0hJwAc9uv5P0KPeq_0jufdwfD862J52B9wCtvv1OI5T2s-OjnnUxvlDJ9WDzGqn3WjQLLgnETU-tjJ2bjAZYd5-YekKwsvrUPfsGqABk6sqPXPlFNPbCyjoCRPmsT95S7ox-YHEGbA9tH177p9PsUxKhLEu_TcOFK4PbCouSyn7AM4WOtRiW8sn9d_jpUCpNdStZnTlqMV4KHtRZNrUJvJo6OG9US-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آمریکا: عضو ارشد کتائب حزب‌الله دستگیر شد
🔹
وزارت دادگستری آمریکا اعلام کرد که عضو ارشد کتائب حزب‌الله عراق محمد باقر سعد داوود الساعدی دستگیر و به ایالات متحده منتقل شد.
🔹
آمریکایی‌ها، این شهروند عراقی را به فعالیت به عنوان «یکی از عوامل سپاه پاسداران» و «حمایت از تروریسم» متهم کردند.
🔹
طبق روایت دادگستری آمریکا، این شهرند عراقی پس از انتقال به ایالات متحده، در دادگاه فدرال منهتن حاضر شد و دستور بازداشت تا زمان محاکمه را دریافت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/akhbarefori/652464" target="_blank">📅 10:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652463">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lD-WriWsqNbMpAKHgGXVbJK8GxcJDU1ED9V-5tlCFAA205m7qEbvFiEVZfCHJs1jBoeW7XlxGyiA-tga17SOt0sCg99s93jHB9jOCfuEzao0GDAPVoHmbCdxAjmxzBpUwhZNC4kGVnQxiMdxF98RSLUvdbzqZkoUqWFsPVg-KlMYxbtBOXdZ8yLU9HtKBCC3iHtSNYk_8Fo0bPc0lhxPWs-ofRMgpImmkFJmHwryjTMLK1uKPN9RHJgJF5ilCcrmHWZkVij8XKoSB5XacUWmTOp4yR9mk3hG2MjvTKAntrNlZq8OWCKeyUiAi0qM-l1DGf1U459Rufxg4T7oTvKhkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقدیر پزشکیان از مواضع پاپ؛ با مطالبات غیرقانونی آمریکا مقابله شود
🔹
رئیس‌جمهور ضمن قدردانی از مواضع اخلاقی پاپ در قبال تجاوزات اخیر به ایران، خواستار مقابله کشورهای جهان با مطالبات غیرقانونی و سیاست‌های ماجراجویانه و خطرناک آمریکا شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/akhbarefori/652463" target="_blank">📅 09:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652462">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bi1z5hInxNUct2fHhZtKSOLufzVvfTH6qigFlkkVo1gDFnctjWLa-OttlWrSjv8E-70oieIOrkXH4dVubHKshmyJkJxTxqsNoETXbHaHIiawl5J2JCYzQZOSjN4iAIHl4JKSz0micguOTFodTR04bvAGsPpbYkqwe5iKVdMCevVYuqniNzlU3ZkfaIMDUOPlNuzXCKzLwb4Lqq7NNNa_npp366DGIY-MwOz6g5kpcHs0wRmdtNVmL7wEPP52XACsryTO0uZwLLQb3Cc93tOZNmHzdsgSnUKvxBcufKalVMTJe9R87wuSN0WkZpBqD0sXCQWBJcwz6J_GNxTjbEtfnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نه_به_پلاستیک؛ برای زمینی که هنوز خانه ماست  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/akhbarefori/652462" target="_blank">📅 09:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652461">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73c957ae27.mp4?token=GJV5V_LiZfoNm7Kw33tfz0Hu67oLQVNBY31ZW2SN22uRUnDdBPdvaffXTa8o3PwXpKn4ruR1FrCGz_pQRssyij_A_yXPI8i7HQ49hS698mHASsbomcFixR77Xt0okBQfWDwVDMLb4bwKpqaAhBWwQ_wnukBLUQFgzRZqarUHeMraLbgigT7gcUjy7i4RcqHy3l0gU_nixY-rPA8Qq0SxCnxEAlWB2P1kVAUqBc5hoEFQ975eSZhwSnDMsovrUKDxNYwHb0HJYlDfasblpqn-Sl57sc1_AH2bxO02IxSLvLv8IYGJpsCWgW7FjQ9YG8_UKcQ3550YbgwKCMWgINe6jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73c957ae27.mp4?token=GJV5V_LiZfoNm7Kw33tfz0Hu67oLQVNBY31ZW2SN22uRUnDdBPdvaffXTa8o3PwXpKn4ruR1FrCGz_pQRssyij_A_yXPI8i7HQ49hS698mHASsbomcFixR77Xt0okBQfWDwVDMLb4bwKpqaAhBWwQ_wnukBLUQFgzRZqarUHeMraLbgigT7gcUjy7i4RcqHy3l0gU_nixY-rPA8Qq0SxCnxEAlWB2P1kVAUqBc5hoEFQ975eSZhwSnDMsovrUKDxNYwHb0HJYlDfasblpqn-Sl57sc1_AH2bxO02IxSLvLv8IYGJpsCWgW7FjQ9YG8_UKcQ3550YbgwKCMWgINe6jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یاد کودکان میناب در نشست بریکس و دهلی نو؛ هشدار درباره تسری جنایت‌ها در صورت بی‌تفاوتی
🔹
در سخنرانی‌های عراقچی در نشست وزرای خارجه بریکس، هشدار داده شد اگر جهان و اعضای بریکس در برابر نسل‌کشی و جنایات آمریکا بی‌تفاوت بمانند، این جنایت به سایر کشورها تسری می‌یابد و تبعات جدی برای آینده خواهد داشت.
🔹
در سفارت ایران در دهلی نو نیز با حضور بیش از ۵۰ رسانه هندی و بین‌المللی، تصاویر کودکان میناب نمایش داده شد و یادشان زنده نگه داشته شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/akhbarefori/652461" target="_blank">📅 09:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652460">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fl4qoQfNc-pQt-x31kd70bLTLnOwUl237VlJbjCspV5FGQRmFrHzX0Rv5j3rzQrlGB2JpWEgclv_1ocKNyV4O9QQY-mfPy_o3l9ElkYoE97sHaRi0f12RLJ0QuKdva-M8jULn1bs0uDsg2OGhbNgzOzgyaFVH4nKfLIWQItXzRJVLQfN9Wkq94u7x45kDZeey2iSbXdY6OhV5ceqad83fPHeQYK2wGtEbZGFytiW_eeVxb-lrWHlf7J5XWGQ60oQQgxUkEgOVT7iUH_cVAb2aBkZIDjaQ_jpqFsXoEAHPltdJ22dsYdyoCdjAoDjVmhAjPUEd4dS5qCg-dsVuXqXCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ مدعی کشتن مرد شماره ۲ داعش شد
🔹
رئیس‌جمهور آمریکا، بامداد امروز از کشته شدن فعال‌ترین تروریست جهان به نام «ابوبلال المینوکی»، نفر دوم داعش در سطح بین‌المللی، خبر داد.
🔹
ترامپ در پیام خود مدعی شد که این عملیات به فرمان مستقیم او و با مشارکت «نیروهای دلاور آمریکایی و نیروهای مسلح نیجریه» انجام شده است.
🔹
رئیس‌جمهور آمریکا در ادامه بار دیگر با تلاش برای پررنگ کردن نقش آمریکا در این عملیات نوشت که که المینوکی گمان می‌کرده می‌تواند در آفریقا پنهان شود، اما از وجود منابع اطلاعاتی آمریکا که تمام تحرکات او را زیر نظر داشتند، بی‌خبر بوده است. ترامپ در این باره نوشت: «نمی‌دانست که ما منابعی داریم که ما را در جریان کارهایش نگه می‌داشتند.»
🔹
ترامپ در پایان پیام خود از همکاری دولت نیجریه در این عملیات قدردانی کرد و نوشت: «از دولت نیجریه برای همکاری شما در این عملیات سپاسگزارم. خداوند آمریکا را حفظ کند!»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/akhbarefori/652460" target="_blank">📅 09:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652459">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o22e6TiQUPY3U4nz2BRrBHA-jfU9ozFpY7ToZRN9aRHISgFhXHcBtjlwy1HOUDNDoiJpwatEv9T4_q_fx8p62u4VHEHv6aSUD6WwhAzqKjh81FdA0VAAYZ9Amyib4fy5-wTSZRdq1ZxZ8I0-Tf0q5g6l8IyRBpbAcsZHtCUVDvRJi3KedccWr0bCBUhf4e8MYeN311pwT8t0EnLMRg8_FoZxUlemTAzm1ekZHYhIWw9GszLG2oXQctS3n7JafVzANgWiP6TwYfH4iM_eSu0EfggyJqBcjLFumvItCQEJDaoaqpjbHha42_xuwiNxPpdqAkt5RUkcguXY9zfILjpckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمام گمرک‌های عراق به‌روی ایران باز شد
🔹
بیش از یک ماه از محاصرۀ دریایی آمریکا می‌گذرد، تجارت ریلی ایران و چین سه برابر شده، پاکستان یک مسیر ترانزیتی جدید با ایران راه‌اندازی کرده و مجوز عبور کالاهای کشورهای ثالث از طریق خاک این کشور به مقصد ایران را می‌دهد.
🔹
حالا نخست‌وزیر عراق هم به تمام گمرک‌های این کشور دستور داد تا جریان ترانزیت کالا میان ایران و عراق فعال شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/akhbarefori/652459" target="_blank">📅 07:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652458">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWqFKN1hANTiGtCOE5TvhIKN2wJFBNwETXbaij1AA0mVFVjJCwKyjjfutS3oCa9-b25vrdT5HwDrHs9qKqMp_sqZqyAa6H6W-4jspoNYIjCN4Zxt3mQrNyCisZKjAsLuVWp84LhCwky4HnoCk9QqJQKPf5HPQA8lyVO72dtgUsbWcvTdhPjtV9yq3yggZkixPDFbHF3NL-e0zL5r4GTjttU9KAJXZUlH26KgUlVqzmNUEr-mCKTXqvyG_qrIUfdI2FVqJrnXmjlUm5_JOAO2vGcTH7xMcm2fYvgU_rtqwpNxM40rAMKxkUyk_ECaUoyymFCJwa40P2KA2N6fiaUvnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفیر ایران: درخواست اول ما از آمریکا پایان جنگ در کل منطقه است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/akhbarefori/652458" target="_blank">📅 05:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652457">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnLN2meLsSG-ECGHEw0dC32CmQ-xal04bn3cLDXSJlYqJyeI2Yj1XCuQczh0VJIsxOl0Us47BiFUEBDT6w1G2fFyXD_Gtv9iEWrqs-GpbGO2pi-uZ4SQVguTXLAiZqAcBjWqOLRt-bsHPLZF-luuyDTRspDvcIPW9dGeb6NECK0JXJnVVbLzU9o4aBkYrLdmMa7N7svr2cW7UkuAPtc1rp9uE4_b0JZvCbU5budkvrgZTD8O72OWrmBnDKJrAcho0RiiqOFCutzhTGh6EG6PWqMT0DELti8GSmG8eU8OQucXPT2Rt3Higlk4pm6sOrIlR44YHfddulKwTyBpKKx60Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاکید پاپ بر ناعادلانه‌بودن تجاوز نظامی آمریکا علیه ایران
🔹
پاپ لئو چهاردهم رهبر کاتولیک‌های جهان در اظهاراتی با تاکید بر لزوم بازگشت آمریکا و ایران به میز مذاکره، گفت: تجاوز علیه ایران عادلانه نیست.
🔹
این جنگ در حال گسترش است و جز بحران در حوزه‌های اقتصاد و انرژی برای جهان چیزی به همراه ندارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/652457" target="_blank">📅 04:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652456">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtKjEm3KX0w7Te-5orQzpBKMcmCi9dP5YBriJ69CsB8Y7U2cjN5dAELSgjY94t0cWgSC0bs4pmy5ZvCCUoCHWo5v-n4JKHCEemBRD4E2Y0LqlSWr_H3EnoJsWn2UDg6uMMfzL4xHcDj3pJwous808ejQS31V7mjZG87L7tKyrZx3VqyXEpJUuHaoa6I5gqbUyamw2TVXu2hMTooEO8f-7Dn9MJQOWS4YE9SiuGaBpUYZwuHNbZ6nOqzIxUjYkqlwjYAsbEx5KljxgLwZep0iQab-FkdIJpbOJrQtQzHI63DPuVzAt1FZQJZgj98dWbeO7eW3yWedIj3SIU0mgrrGWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر کاتولیک‌های جهان از آمریکایی‌ها خواست تا با کنگره تماس بگیرند و قانون‌گذاران را برای پایان دادن به جنگ ایران تحت فشار بگذارند
🔹
تریتا پارسی، معاون اندیشکده کوئینسی: فوری! پاپ لئو چهاردهم جنگ ایران را ناعادلانه دانست.
🔹
او گفت این جنگ «هیچ مشکلی را حل نمی‌کند» و تنها باعث گسترش نفرت بیشتر می‌شود.
🔹
وی در ادامه از آمریکایی‌ها خواست تا با کنگره تماس بگیرند و قانون‌گذاران را برای پایان دادن به جنگ و تلاش در جهت برقراری صلح تحت فشار بگذارند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/652456" target="_blank">📅 01:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652455">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGHsmG6fe57ECRNVKrz7tFy49dNE5oQeq8OTINJ3Zqn-4tzu1eWV3kL3_0fWy22TSzVRPNTSEqOBSulzArFC9x864qVSbsjiNENZ9JtDzRKxq4mNscuiehIMI5vO1sar9yCvn8qEn3DDqNkQpMzCpt9BuXQBzNzTKg8SnWj61IrGhlDTqmc87h9RYGJQzvRzH02CJn1lvLM-aQS5ethtkEl2HL2iI4cY6KS_ciehE8Ty1tkKrU9knymLgyNNEs0P0iq1g0nv0V9fIEXOj2BATR8lc3bRThbfwCfWC5Uv4BpLhNJs9cd3muZrxZj3qVVr17B-xz2f85K2d8YAXQe1Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بسته بودن تنگۀ هرمز برق کوبا را قطع کرد
🔹
صدها نفر از مردم کوبا با حضور در خیابان‌ها و روشن کردن آتش نسبت به قطعی گسترده و سراسری برق تجمع اعتراضی برپا کردند.
🔹
کمبود سوخت عامل اصلی قطعی برق در کوباست که به خاطر جنگ آمریکا و اسرائیل علیه ایران تشدید شده است.
🔹
وزیر انرژی کوبا می‌گوید، ذخایر سوختی که روسیه به این کشور اهدا کرده بود تمام شده است. وی آمریکا را به خاطر بسته ماندن تنگۀ هرمز سرزنش و تاکید کرد که قطع جریان نفت ضررهای زیادی به کوبا وارد کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/652455" target="_blank">📅 01:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652454">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: دو مقام خاورمیانه‌ای ادعا کردند که آمریکا و اسرائیل در حال آماده‌سازی گسترده برای احتمال ازسرگیری حملات علیه ایران هستند؛ آماده‌سازی‌ای که بزرگ‌ترین سطح از زمان آتش‌بس محسوب می‌شود؛ این حمله ممکن است از هفته آینده آغاز شود
🔹
مقام‌های نظامی آمریکا به‌طور غیررسمی می‌گویند پیروزی در حملات جدید بسیار دشوار است، زیرا ایران بخش زیادی از توان موشکی و زیرزمینی خود را بازیابی کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/652454" target="_blank">📅 00:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652453">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lx--FyJnXBcKu3SLj2agxdYNOWhRfp0AD6nxsHpU7Sywve68LrXYXxl8w903YOTVBOxcVFeXasWvikA58L_uoSme5MDggGmBa0cj_9SlPa-PLbgR-jDPtatdGj7ZKVNWRU1eFMscJC7eqWEObMPk36SHV_6mDItPjv7ImHqfSzVtvMwylRonlFCtatvjQgjGH-EqFJH-SpAFDsLjVNU2-IewoZ-kDmU9x-br4Na_IZebYyRt9NRt4NXCOu8fzp0xRvKiJIUdM_ghc49bl02ZxqOa9YM4TXhxFvnNJ7vWMs8FZozuIzaHzCF4_Fu-QhDURdaN2VPsSeZt7nqH6fo8aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران: هیأت حاکمه‌ آمریکا شریک جرم اسرائیل در نسل‌کشی هستند
🔹
وزارت امور خارجه ایران امشب در بیانیه‌ای به مناسبت روز نکبت با تأکید بر حق بنیادین مردم فلسطین برای مقاومت علیه اشغالگری و مردود خواندن هر طرحی که متضمن کوچاندن اجباری مردم غزه و کرانه باختری از سرزمینشان باشد، اعلام کرد: هیأت حاکمه‌های آمریکا شریک جرم و همدست قطعی اسرائیل در نسل‌کشی فلسطینی‌ها به شمار می‌آیند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/652453" target="_blank">📅 23:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652452">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5dYE83DsAUEo6_DZ5Ck89K5x4-uqw7vgDWILPr1OxEjQtAAsSQwD3q0QRkt6ozbAeoSBGP6XmVeFCYM7pz4Bbq8UHa0DtW9-hKilnnucI90RnswlcvH8JzGbaGIdGvy7OHGiv_9oeyIrs0Jo1c59AVkIR3GZdYb23nIG3QIjkYk48fk7njWU-eb5UV0DWDZYDXCvAgxMi9Grk1yfIpEQxnjzLaSMBLPmnZliQParq9Nx7jrZcafxGxKAC436O0bpIzRIbPHgkTkl8YxvfMASiRR3gGgjGXigLeQ3GUJ4iBHeU6Rb3DMH4mCeG-EfwTqnCHDFPswfQr7fFt_g65mtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاهنامهِ ایران
رهبر انقلاب:
🔹
ملت عزیز ایران در دفاع مقدس سوم نیز ثابت کردند که داستانهای اسطوره ای فردوسی واقعیت زندگی و شخصیت قهرمانانه آنان بوده و مفاهیم انسان ساز سلحشورانه و قرآنی شاهنامه همه اقوام و اقشار ایران را در حفظ هویت اصالت و استقلال خود و مبارزه با ضحاک وشان متجاوز همدل و همراه می‌کند.
🔹
ویژه‌نامه جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/652452" target="_blank">📅 23:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652451">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhtmYwTBLYK2NDa9DskaTjtryHaE_hK-tuwWF0gusyA2d7IXlfj1bLhqt-RS-yuA3BpDEwWLNxsu0KNQDyYLZ_SRukV49SfIVomIO3YxAsgiIwOL1m4IPBeZUm6EiF6cgCeRh54x7nZaFNgKbte0A2LxFBhFIrSRovZcQATzthwPdbEhqono4C6PeNBhuj14Pqwo9QeIWqzT7wkVCWsA8R--75CcDtGrRJtAYP1BE9B9nSwORy5cy29Q7VWlzpveA1dLspDdjbggioemBqa4k1e09O7gIPtFp0h9D3dTZvAclD7ghcUgtHABM9cA7kn-jKECEddXGlox9m1sJpi81Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕
*بیش از ٪۲۰ کاهش وزن با داروی جدید داروسازی دکتر عبیدی*
⭕
بیش از ٪۲۰ کاهش وزن با داروی جدید داروسازی دکتر عبیدی
اپلیکیشن تخصصی «مان» با همکاری داروسازی دکتر عبیدی، با استفاده از دارودرمانی زیر نظر پزشک و ارائه روش های ساده برای بهبود کیفیت زندگی، توانسته برای بیماران خود بیش از ۲۰٪ کاهش وزن به همراه داشته باشد.
آمپول لاغری زیکورپا (ZCorpa) به‌صورت تزریق زیرجلدی هفته‌ای یک بار استفاده می‌شود و مصرف آن باید همراه با رژیم غذایی کم‌کالری ، ورزش منظم و زیر نظر پزشک باشد تا نتایج مؤثر و پایدار حاصل شود.
📌
فرآیند درمان به صورت کاملا آنلاین در اپلیکیشن «مان» و تجویز دارو تنها با تشخیص و تجویز پزشک انجام خواهد شد.
🔻
مشاوره رایگان پزشکی</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/akhbarefori/652451" target="_blank">📅 23:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652450">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔹
در لابلای اخبار، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
بن‌بست تازه در مذاکرات اسلام‌آباد؛ آمریکا پیشنهاد ایران را رد کرد
👇
khabarfoori.com/fa/tiny/news-3215084
🔹
ترامپ رسماً اعلام کرد: یک دور دیگر از عملیات نظامی آمریکا در ایران در راه است
👇
khabarfoori.com/fa/tiny/news-3215168
🔹
آمریکا برای این زن در ایران ۲۰۰ هزار دلار پاداش تعیین کرد
👇
khabarfoori.com/fa/tiny/news-3215122
🔹
بحران در بازار مسکن؛ ۱۰۰ درصد افزایش قیمت، ۴۰ درصد کاهش فروش!
👇
khabarfoori.com/fa/tiny/news-3213856
🔹
علائم عجیب و هشدار دهنده آخرالزمان | وقتی شوهر به مرد غریبه پول می دهد تا با زنش زنا کند!
👇
khabarfoori.com/fa/tiny/news-3214791
🔹
ویدئوهای جنجالی را در آپارات خبرفوری کلیک کنید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/akhbarefori/652450" target="_blank">📅 23:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652449">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXX-PeVjjHOZQyvwUfIEaVL0_2upK_6vQtSdhxRLokO1R03SUnELfG5Yyf-K77jAKcAvrWb4BIY4-FM0MAXhRpS90EvubqzsZsdm26vix-EbHBNoXccREpgF7aHjp4xy32IjSWmc12ZKe8zLDGh3Qweo0DzEvGpITRuzTo7yul7n1Rdk8YBSthD1J31uGEf0lSNd1ZKX8no1v11OSJF2ErLnAb29-PPHyaTX1of32InpA5Wvf-Wc4FS3JEHjd1WeKyi-0YDA2AADV68krpKzURPj46pUMsk_2wLhQzpN0syEJMmc-P-K8RXlSNgHbW1J_bxSdQF2BUmjFDrdwuMQ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برگزاری دومین نشست مجازی مجلس با حضور وزیر تعاون
🔹
«گودرزی» سخنگوی هیئت رئیسه مجلس: دومین جلسه مجازی صحن مجلس با حضور وزیر تعاون روز یکشنبه ۲۷ اردیبهشت ماه برگزار می‌شود.
🔹
دومین جلسه مجازی صحن مجلس با محوریت مشکلات معیشتی مردم و پیگیری اقدامات حمایتی از جمله کالابرگ برگزار خواهد شد.
🔹
قرار است در خصوص تأمین کالاهای اساسی مردم و کاهش فشار بر دهک‌های پایین از جمله کارگران و خانواده های فاقد درآمد و جامعه هدف نهادهای حمایتی بحث و گفتگو شده و تصمیمات مقتضی اتخاذ گردد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/akhbarefori/652449" target="_blank">📅 23:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652448">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651e0e3dcc.mp4?token=VRR609CrXDyRk8digRryLgzVM1BOXjy3RtdNhj_iKfQB_hL7lzGq55m_ZbVhQQp1UbBQgUdxF6NFDYUueq9delKlmRDuzaDyS4-nbagEvPFGyNYq0elNXrc87AM-mdrAUegN05ckZkQRjABtiwWToqJZEj64Ti0cZGwu_7yNX2Iz8h7Lw8fbY5o05f2xLwzfFHbMviEwzX6N6dfi2sFi6gp88mtJTNoWgKvNepVp5QbY6aMmMkv8Iw-VZdhDm0Dl_cRb63Fmk3RlhRB589oid1OMCsnVdbGZorEkXwvB1_P3pgobfW7G0M2sBHFFTmEnUA5wfYBjHMLVqHXKV8Pbmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651e0e3dcc.mp4?token=VRR609CrXDyRk8digRryLgzVM1BOXjy3RtdNhj_iKfQB_hL7lzGq55m_ZbVhQQp1UbBQgUdxF6NFDYUueq9delKlmRDuzaDyS4-nbagEvPFGyNYq0elNXrc87AM-mdrAUegN05ckZkQRjABtiwWToqJZEj64Ti0cZGwu_7yNX2Iz8h7Lw8fbY5o05f2xLwzfFHbMviEwzX6N6dfi2sFi6gp88mtJTNoWgKvNepVp5QbY6aMmMkv8Iw-VZdhDm0Dl_cRb63Fmk3RlhRB589oid1OMCsnVdbGZorEkXwvB1_P3pgobfW7G0M2sBHFFTmEnUA5wfYBjHMLVqHXKV8Pbmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
داستان خلق درفش کاویانی ...
نسخه کامل را اینجا ببینید
👇
https://youtu.be/YrDeYT6DO1Y?si=2RpPQjKDe8vTJ-4g
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/akhbarefori/652448" target="_blank">📅 23:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652447">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b883Ha5bmZfkF2TCi31pTggomuQcoxjA6Jrrau0y_FMg6o1zH2paJA3qzF_nIoRK6K-gIxyI88rHsvdY8zqKy78UXlMKHZ-Fw9xJYd12W-QmmEnC3OypYTcseXHtVrkiHzN-j9R1N7D0TSK4jPVa0K-yFoNrfxvL6jFs6mJFnH-Y5Lv-yFfT0uLy9Ng4pijTkfeJjNDxzPaGB26KXvuFQnYRa3icOm7uLUI6jlSFhSs66TFS0J0CKAaOXEP6erSGh8HY2peKGQs0yP025mjN6FJ8qg4tzhfC2hXUpSfvdGfTXgSJMqR3ucdx5dy4rqkkrET0tMnshUYWkq3b94iDtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستاوردهای چینی
🔹
سفر دونالد ترامپ به چین تقریباً هیچ دستاورد قابل‌توجهی نداشت، از عدم توافق برای تحریم نفت ایران و فشار به ایران درباره تنگه هرمز، تا بن‌بست در موضوع تعرفه‌های تجاری و تایوان.
🔹
تنها گفتگوهای اولیه درباره هوش مصنوعی صورت گرفت و خرید هواپیماهای بوئینگ هم کمتر از انتظار، با ۲۰۰ فروند در مقابل وعده ۵۰۰ فروند ترامپ نهایی شد.
🔹
هفتصدوپنجاهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori
,</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/akhbarefori/652447" target="_blank">📅 23:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652446">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyAG89BVuSoGB4YJ0PVQA2xsR0rKZXXrypLYnm6g3aHlI_yvP5dNNvV4nNWxfYJ-WDW_NlX9NA1p-ZYxgYzaiLagK9YSAi7dcglLEsbY1wRiWVKaTCDyGkT_lpu_vxeAxhdfWIo_arbmOUwIfyvG2q0zPAGENSCUJ-BMA-ycbKpdPR8F4KLcVZwvtwnPh8DnRFZ_0_-Rb5-7Q3l_Dzme-mw99dWS8zGkH_ZV3R8XK_lowaeKIAdYiMQFuTg6AEs66jFltRDN-hhUrZc24YaCVbEEf-AZ-727kIYsSBtKkyTsOTdaLT1AdjKlEvSc9Q6nb-WxYsAJk5d1xpgsu3CpmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت خارجه به مناسبت «روز نکبت»:
🔹
هفتاد و هشت‌سال پیش در چنین روزی، مهیب‌ترین تراژدی انسانی و اخلاقی دوران معاصر با اعلام تاسیس موجودیت جعلی صهیونیستی در سرزمین تاریخی فلسطین شکل گرفتکه پیامدهای‌ فاجعه‌بار آن در منطقه غرب آسیا و در سراسر جهان مشاهده می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/akhbarefori/652446" target="_blank">📅 23:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652445">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2iPCVfeBF0cQWXFq33Y5nrrQKsO48gGlmULuf90muCpkdU3coFou8BtmbMWNmNIROuKwFtSu30gsIO8ys78QjOERAvF3xWiiFAhtGcADb996vat-obasuSsuNPK-MZFMHC-NbWNazmCFw5qgxkXgh9Uet-9K4d6vQZKe4ACMll91hwfu3NfhWL_pwnRW847NWuiVYt3h7AwbGIGxzuMUn2Q5_etYqDHlVRDB1lRDCWW3pO-huLHon8QTrnnnzFR-36u_7oRSDP3m3DNxJ_vMxDlof9sptRng9UGvueU74JnO7jyPIoQ_AMxVS9zqM57PDCq-3BeR1KDEWd77qpNMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتراض مردم انگلیس به استفاده از پایگاه هوایی بریتانیا در جنگ علیه ایران
🔹
تظاهرات‌کنندگان با تجمع مقابل پایگاه هوایی بریتانیا، خواستار توقف استفاده از این تأسیسات برای عملیات علیه ایران و خروج نیروهای آمریکا شدند.
🔹
معترضان با بنرهای «جنگ با ایران را متوقف کنید» و «آمریکا از پایگاه‌های بریتانیا بیرون برود»، سیاست‌های ترامپ را «مرگبار» نامیدند.
🔹
این تجمع پی گزارش‌ها مبنی بر پرواز هواپیماهای جاسوسی برای پشتیبانی از عملیات در خلیج فارس شکل گرفت.
🔹
سازمان‌دهندگان اعلام کردند این آغاز موجی گسترده است. آن‌ها معتقدند هزینه‌های این درگیری فراتر از توان جامعه است و لندن باید به جای همراهی نظامی، نقش میانجی‌گرانه ایفا کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/akhbarefori/652445" target="_blank">📅 23:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652444">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961e48dba0.mp4?token=BLZ7nKyDAwFaV5CFZv0-sruNj9_30JXJK07aJSTC-29jNCD7U9w1oa2rkkmB0qZFBX7eAzGkKOpbk0nBwS6ShHsxfwI09VfwoxR5WLXHpMNZae5hqlurFCZHVMLczoUvRCX4fXhcAYqd1k1fxKhW1sm-l9ouJbsf35MjAc0wW_hf_-AQOso87dl3Dp-pKA1Pi3FF_ZbNr2wBjP9ecKTLxCp1pXTqctJqKoWNbY6gvXHvqArHScm6w4iBOm6BKUhQnUmeuYAVZ2XnqE5rdYGSl6am3snjiMfb37kcZpQon6SucDP2wVGGPo_5rUoJvHg8V9znTuIkTr-x1npHOFWVxms6HoEXEhoNzyisVfkfSl2SQPx4LYci3ZgxDHH5frd83SaYFn093OqQlQQXqFL7AD5u__ssbxjHW3Ofw8o5_W6cg6pZtJpfDD8tkYXKj-uTYHserSxQlBpPvSS5t2CPe1T7UT3LjTp0UtD0ZyMxa8ifgH6Fz8ulr9VZx7vwUREwIMSBmVTJrFVHFX5KnZ10NxQOwSFsAgLdFMSOfHvzDKH-XwJBkaFfuUYcdn-7bUivagpEMtVUItjwTquK-wL9dIY5kd2uRKjExyuL1Z7AJMj4UJaViHnyvjEuHFpOiMcGSXHK_WGIb2nrNCpEQpJSZSveajbjLk24FbhYPvlddRI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961e48dba0.mp4?token=BLZ7nKyDAwFaV5CFZv0-sruNj9_30JXJK07aJSTC-29jNCD7U9w1oa2rkkmB0qZFBX7eAzGkKOpbk0nBwS6ShHsxfwI09VfwoxR5WLXHpMNZae5hqlurFCZHVMLczoUvRCX4fXhcAYqd1k1fxKhW1sm-l9ouJbsf35MjAc0wW_hf_-AQOso87dl3Dp-pKA1Pi3FF_ZbNr2wBjP9ecKTLxCp1pXTqctJqKoWNbY6gvXHvqArHScm6w4iBOm6BKUhQnUmeuYAVZ2XnqE5rdYGSl6am3snjiMfb37kcZpQon6SucDP2wVGGPo_5rUoJvHg8V9znTuIkTr-x1npHOFWVxms6HoEXEhoNzyisVfkfSl2SQPx4LYci3ZgxDHH5frd83SaYFn093OqQlQQXqFL7AD5u__ssbxjHW3Ofw8o5_W6cg6pZtJpfDD8tkYXKj-uTYHserSxQlBpPvSS5t2CPe1T7UT3LjTp0UtD0ZyMxa8ifgH6Fz8ulr9VZx7vwUREwIMSBmVTJrFVHFX5KnZ10NxQOwSFsAgLdFMSOfHvzDKH-XwJBkaFfuUYcdn-7bUivagpEMtVUItjwTquK-wL9dIY5kd2uRKjExyuL1Z7AJMj4UJaViHnyvjEuHFpOiMcGSXHK_WGIb2nrNCpEQpJSZSveajbjLk24FbhYPvlddRI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«ناوگان پشه‌ای» ایران بلای جان ناوهای آمریکایی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/akhbarefori/652444" target="_blank">📅 22:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652443">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLM1ZiyJgTgig9olTMWAwPOKnlrDM4vPrc4Esa0jdxGy5_xXEnzwc5w6MJhRuQRPH4YAt1oLSYHhgh_Qe3F2m08Y-0bqT3WhYuYCK0nVrnSyRYQXXKDRf9Dprw-arJCOMWgNNz19j19ib0XlDeHQWZd8c4SQ-_K20WD2r4MUyyIA12oloVx1gJCO8KUJvxsSCSPIYsHB4hOk-k6Z2KZY36Y-qjSmZfEjXqnJPv_INRUXeJhQlijAEyKX6fuIZYGvFvbC-AJdn3k1gbjOSxjbVcz60io0ZYEo9G3J6DDYFZLx5XYRLvwjJQdMQGxGgylcDAH6rOKMh3Q8W3SXtS4jkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زندگی تسلیم نمی‌شود
🔹
حتی در باغچه‌ای از پلاستیک، طبیعت هنوز تلاش می‌کند نفس بکشد.  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/akhbarefori/652443" target="_blank">📅 22:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652442">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b036fe427e.mp4?token=YKThofcT86ryQ-JNoYdrlTDxKaNDIB9LyIHnLG2fMGVb2RwbZGvXphHc6YAeco7y7ZItJq06LP2QEOGmWTDikmVjwW_-TcZkDUijncwH6qd2TR2jv-Km09SeGY40-GEino06I3kFELGfPlZTZ6Uz8ovr0AHBe6vQW6lBhD94GCgUZZIvL9hhCehQM0VYaOGLOG6S9Lvsn_Du-UwRfTrtTJE3nQpF5s0sNDoRHbFWY9ZwQ2dtKzk8X7fbe7vEnraJEbrZVbuorY3-91heLvtL4JM72Qcam2R-9bVCqK05j7-AOun54qHkbaymsW8j-W78q3IIzrOGJWDG94fkevgdLH29FXJ5U0Jd9cq_uVCjhcSM8Xr11wYTz1tjblA80x9_mfX-Yxg-NA6mich7kKTb-Cfr28pfn0YRshs5F9e-6CgEQ8kFeiw9AJEyCOunoNpoVZvOeppEJwoBRh4seep-_uHdP4JwGglTrHacjS9YNZEb_h9-niH4qhsQQ48TcCWMEC_5S_ahjzYFG1UGLGoGBjAWvw5jLmhh8973l7Lkgjl4bYo1i5dELLKtBU-QnlLaQQz2MjsjGhqRNXgHVF2bhe5VcgmSKZTxoNXS3HRZXfO9D_yZFbYgVwZ9vX4pmWOQekPFP2EuiFfNOT6oe352-1d6CVVXkDafK0LxNugmWIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b036fe427e.mp4?token=YKThofcT86ryQ-JNoYdrlTDxKaNDIB9LyIHnLG2fMGVb2RwbZGvXphHc6YAeco7y7ZItJq06LP2QEOGmWTDikmVjwW_-TcZkDUijncwH6qd2TR2jv-Km09SeGY40-GEino06I3kFELGfPlZTZ6Uz8ovr0AHBe6vQW6lBhD94GCgUZZIvL9hhCehQM0VYaOGLOG6S9Lvsn_Du-UwRfTrtTJE3nQpF5s0sNDoRHbFWY9ZwQ2dtKzk8X7fbe7vEnraJEbrZVbuorY3-91heLvtL4JM72Qcam2R-9bVCqK05j7-AOun54qHkbaymsW8j-W78q3IIzrOGJWDG94fkevgdLH29FXJ5U0Jd9cq_uVCjhcSM8Xr11wYTz1tjblA80x9_mfX-Yxg-NA6mich7kKTb-Cfr28pfn0YRshs5F9e-6CgEQ8kFeiw9AJEyCOunoNpoVZvOeppEJwoBRh4seep-_uHdP4JwGglTrHacjS9YNZEb_h9-niH4qhsQQ48TcCWMEC_5S_ahjzYFG1UGLGoGBjAWvw5jLmhh8973l7Lkgjl4bYo1i5dELLKtBU-QnlLaQQz2MjsjGhqRNXgHVF2bhe5VcgmSKZTxoNXS3HRZXfO9D_yZFbYgVwZ9vX4pmWOQekPFP2EuiFfNOT6oe352-1d6CVVXkDafK0LxNugmWIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس مسائل بین‌الملل: نباید اعمال مدیریت ایران بر تنگه هرمز را به کسب درآمد تقلیل دهیم/ باید از تنگه هرمز برای تأمین منافع ملی استفاده کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/akhbarefori/652442" target="_blank">📅 22:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652441">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556fbab204.mp4?token=TdIQD_phuypLkXKSAoJ_fkEFcUHJjqudZok7EtZ6sdBs6_6zhzc3CIy46U0-4LMEokpV_wpThuiwkSLMIL8feSS9mpH-q9eLIVPT8ZtmgcqW3YPyTWPtd8i_weYjPSEqpSVEyaW9nnmwdIUVOpE2xXl_EmuDd4neFB4rfzRCXiWvuKIgfUG8ePH4WdAxPJXkBFYBhyoJqQRXV3T05Mln-Z332D89nGhS7ntjI1FFpathnW6SISWRsO2CZXQd_Gtxq4cAzIoBK9MPQ8JZhwfxc-K00MFmuyaqft5-PiTfdyb1xSFp4sikdD5qRoVJnZCKGPsR67zL1L6MMYLLpRhGNEiRO63WinjjJwXOJka_4HJxGlLEVxBgBBfWYPLwVp6HOAVOoSg8_uxPpSTX2Z_TjiWH7qFjTBq8pfiFqRu_EIRywpq4NuwqP81xK-9SZbOzibWsm1Iem6ro2YXAZ3GcEtPCOtTOWTqHBHyB-LTttTDupMo5cGnWIcdYerY6GlUk8VEX4eKDbQ0ldo5WI_Wb41jkA9GzUMHW8Dy7pGnWVdfmaJ9tyMl8oSOFDWZpg8uHBwb1HABTFnVmd7DPtPTe5GL1U5-LcUXXdvfahilgb2jKT5Un2eWCvpVORt5ZXmo5VcHU4FkZe5RjfBYqhlF2pfFoEEln-zx82NmseZVDPIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556fbab204.mp4?token=TdIQD_phuypLkXKSAoJ_fkEFcUHJjqudZok7EtZ6sdBs6_6zhzc3CIy46U0-4LMEokpV_wpThuiwkSLMIL8feSS9mpH-q9eLIVPT8ZtmgcqW3YPyTWPtd8i_weYjPSEqpSVEyaW9nnmwdIUVOpE2xXl_EmuDd4neFB4rfzRCXiWvuKIgfUG8ePH4WdAxPJXkBFYBhyoJqQRXV3T05Mln-Z332D89nGhS7ntjI1FFpathnW6SISWRsO2CZXQd_Gtxq4cAzIoBK9MPQ8JZhwfxc-K00MFmuyaqft5-PiTfdyb1xSFp4sikdD5qRoVJnZCKGPsR67zL1L6MMYLLpRhGNEiRO63WinjjJwXOJka_4HJxGlLEVxBgBBfWYPLwVp6HOAVOoSg8_uxPpSTX2Z_TjiWH7qFjTBq8pfiFqRu_EIRywpq4NuwqP81xK-9SZbOzibWsm1Iem6ro2YXAZ3GcEtPCOtTOWTqHBHyB-LTttTDupMo5cGnWIcdYerY6GlUk8VEX4eKDbQ0ldo5WI_Wb41jkA9GzUMHW8Dy7pGnWVdfmaJ9tyMl8oSOFDWZpg8uHBwb1HABTFnVmd7DPtPTe5GL1U5-LcUXXdvfahilgb2jKT5Un2eWCvpVORt5ZXmo5VcHU4FkZe5RjfBYqhlF2pfFoEEln-zx82NmseZVDPIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از دعوت به حمله مسلحانه تا دفاع از عاملان قتل در رسانه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/akhbarefori/652441" target="_blank">📅 22:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652440">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e6f50fde5.mp4?token=Eyk6r0ufSLHxy_JjRDw49J7_R5SZC-IzTZoNmIo32v9C92S5oWDiN-x30Yj3vbKNRFvn_oXhlk9k4wVAxpbnGjTf8FNw64sqBW-7lhXvD--qqjEr3LSrVZo0J0TGfD2qCKdeB11ZaRXe7Zfr-aTUlxD1mp1VfuciUR31i4tPEBgnLmO9iarfQWM_OJfAnQ4GZuOTZAanWk0YHrpbUTgPY0aUrME3kbpUCSKj2XGilDNyJRASboyy26Zbr9iNH0aWaJoURv0Cq6CKCoFI99FuTbGTIO7gpBw1SQ1nq1oRCXRM44kePECQwvNekeye-pVOVqHYIxxZq7iKjQsMvVEHAYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e6f50fde5.mp4?token=Eyk6r0ufSLHxy_JjRDw49J7_R5SZC-IzTZoNmIo32v9C92S5oWDiN-x30Yj3vbKNRFvn_oXhlk9k4wVAxpbnGjTf8FNw64sqBW-7lhXvD--qqjEr3LSrVZo0J0TGfD2qCKdeB11ZaRXe7Zfr-aTUlxD1mp1VfuciUR31i4tPEBgnLmO9iarfQWM_OJfAnQ4GZuOTZAanWk0YHrpbUTgPY0aUrME3kbpUCSKj2XGilDNyJRASboyy26Zbr9iNH0aWaJoURv0Cq6CKCoFI99FuTbGTIO7gpBw1SQ1nq1oRCXRM44kePECQwvNekeye-pVOVqHYIxxZq7iKjQsMvVEHAYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: ایران منتظر کوچک‌ترین حماقت آمریکایی‌ها است/ ترامپ لات کوچه خلوت است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/akhbarefori/652440" target="_blank">📅 22:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652439">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd37f5ac2f.mp4?token=IDUTFVCKOE68ri7rn6nHbIhgugWlTi9JdGhyGfUpqyOXFb77HaBLYvPkv8pUnEjUd3q8aS_f9zeNv2YkJVkKiWq3_0SQgJsFcOuWoZYW2WAn-vmH31sFoqncx6EMRY-bX-Izg-8FkkpjgxMMIsJv5TRkkoHOSa3RzhHOLYaElDov1WueKGVa1bDEVe6cxQWNmIeuAELTUg2sTfxab5MUpdlr_pXP48rGi9s3-7OJDGA7QOQuRtG-zg4tN_Gtsb5SOJQP5Q6h2ts2fp_5gzUjh_gOXrInhiHasGY7c4xO8PRXdkz2t8uoXN-I8587tXUKrjHsqquyErV2K-4g-3AlEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd37f5ac2f.mp4?token=IDUTFVCKOE68ri7rn6nHbIhgugWlTi9JdGhyGfUpqyOXFb77HaBLYvPkv8pUnEjUd3q8aS_f9zeNv2YkJVkKiWq3_0SQgJsFcOuWoZYW2WAn-vmH31sFoqncx6EMRY-bX-Izg-8FkkpjgxMMIsJv5TRkkoHOSa3RzhHOLYaElDov1WueKGVa1bDEVe6cxQWNmIeuAELTUg2sTfxab5MUpdlr_pXP48rGi9s3-7OJDGA7QOQuRtG-zg4tN_Gtsb5SOJQP5Q6h2ts2fp_5gzUjh_gOXrInhiHasGY7c4xO8PRXdkz2t8uoXN-I8587tXUKrjHsqquyErV2K-4g-3AlEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجاوزات وحشیانه رژیم‌صهیونیستی به مناطق مسکونی غزه در شامگاه جمعه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/akhbarefori/652439" target="_blank">📅 22:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652438">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه_جلسه 49</div>
</div>
<a href="https://t.me/akhbarefori/652438" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه چهل‌ونهم
رائفی‌پور:
🔹
0:10:40 داشتن حب و دوستی نسبت به اهل بیت از اصول و پایه دین است
🔹
0:15:06 نشانه های آشکار از شیعیان واقعی
🔹
0:27:10 فاسقین چه کسانی هستند؟
🔹
0:34:00 وصیت پیامبر به اباذر در مورد حمد خداوند نسبت به اولین نعمت ها
🔹
0:42:30 تمام شدن حجت به همه مردم در آخرالزمان
🔹
0:49:00 بشارتی که خداوند به مؤمنان داده است
🔹
1:06:50 بزرگ‌ترین نوع کفر و شرک در آخرالزمان
🔹
1:23:30 چرا اکثر انسان‌ها ایمان نمی‌آورند
🔹
1:46:50 راه مستقیم چیست؟
#دعای_ندبه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/akhbarefori/652438" target="_blank">📅 22:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652436">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Subw7rmskg3UTdK3xIASfCNRSYiA-arSi6MXgGEOdPaY7j8LsnzrA50h-7HRjKT9YRjzqN26w0ZaObMhr66WyFSVdPeAhUfMtjXCohdVI7UXXG_oOJiJWkY-Y1PlCY1I9jZ5KYf5bIJLZN1oaE6StD3fjBLXQOWa9MHKhg5rkZ4xZqHf9ClLz1evbMly_kYNVAn7IuvcJaeZjfzNjNoj7H0pU9LhF0TtR9Zwtsb7lPtkn7WD5Tkr_ixeSe7UWcVYiY-ZFFDPtY8cpfPcIZco67YbzB4wt5ahLpJ2HQaiYYjGWexc5W9u6CVa7RJ4s9oLl7iLZ0u8Xwuu_n0gm_Dckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIesWeCe2Q3VQpbnkj6a599LNzQ5i2uXd8V9NK3cjUYxFcereDNW8MByMSV-msz3WO1kap0qwqI4TO3XagAtygSpGV1PuftYbJDs3ZwwLvo-PVCGrXI4SQRV5rUd2z4squPKcNpZZxf2DqRnbZWhBCDtlASRECx952moeAjoHQxr2-up4CZamFK616qfGfR4xriSnIyCE_gDMToTyxWpgtftoSide1kaNBmlJYbSo2cIfIdweeKntD4Bgfs8kz2EkVWQjRoxB0Ws-0kHcf7B5tMK_6EKRWxnABLNh_SKARQ2XsF-Jbvzzfo0y6Z4tLth0BtCOrBXvhSqVMCrl1fRCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رژیم صهیونیستی دستور تخلیه برای مناطقی در شهر صور (جنوب لبنان) صادر کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/akhbarefori/652436" target="_blank">📅 22:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652435">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0fc19884e.mp4?token=vk0HN-xb4liTA_3PbwpJQ1scHMmNLUN_JkBLf0l3nc20IVjLwSxNv6f6ovsgadt0dRPNxVF31IA9GbWxFfMPOIZqNrk748Sw7C-GSvJCMDAFJML-cvhWhlz6_oRZYkFKzoI4IBsPtAg1whO5R43n8l3gOHXA09WeD68NoDE526wqdsxxHAJ3DLhVlyzFJ0QdaOmeef5Fe-0XHS0A1ARAmNb6Amk5EFufcjLL8fbMKuOkK7Ef4GJsLXKK7MwbulwR4ZtNXp6B0ZyLF7uXos_JcnDWjPG1DqiMGnSFLMWvAWtv59xQENb3comfN4DDKNqFvzcr_4tWyVAKeidm63R7Tqim9XzM7YexonEkXb5gq01p_bg278kNYtQv0lYxXBVLc4-z1JaF1B_BL4AMsihuWpR_ggSXqU5iUJlfOhj8sJLDVjmWU7Csz3bH0gSy1dqFYHAHWc2EmWeOFlNDJxffkVMo6kNDilS-l5ZYmE2YIglNmxwvfW_UwbaOTONjcN1uAapFgXwVBCVokorcilkNxs_MlRbPUnkYEuXx-v7hMNqYOY8JlLzhcVhPA9V4DP07xFyPIlnBaBJPjqdIwOwqUSvjJc_OZV_y7MmasxkgQFCA0eyYyDQE5T1-Wgx2UTxHZumate_v0fhWUiPoZLmbNPNUDfLTSMxOMp_1HmhfxVs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0fc19884e.mp4?token=vk0HN-xb4liTA_3PbwpJQ1scHMmNLUN_JkBLf0l3nc20IVjLwSxNv6f6ovsgadt0dRPNxVF31IA9GbWxFfMPOIZqNrk748Sw7C-GSvJCMDAFJML-cvhWhlz6_oRZYkFKzoI4IBsPtAg1whO5R43n8l3gOHXA09WeD68NoDE526wqdsxxHAJ3DLhVlyzFJ0QdaOmeef5Fe-0XHS0A1ARAmNb6Amk5EFufcjLL8fbMKuOkK7Ef4GJsLXKK7MwbulwR4ZtNXp6B0ZyLF7uXos_JcnDWjPG1DqiMGnSFLMWvAWtv59xQENb3comfN4DDKNqFvzcr_4tWyVAKeidm63R7Tqim9XzM7YexonEkXb5gq01p_bg278kNYtQv0lYxXBVLc4-z1JaF1B_BL4AMsihuWpR_ggSXqU5iUJlfOhj8sJLDVjmWU7Csz3bH0gSy1dqFYHAHWc2EmWeOFlNDJxffkVMo6kNDilS-l5ZYmE2YIglNmxwvfW_UwbaOTONjcN1uAapFgXwVBCVokorcilkNxs_MlRbPUnkYEuXx-v7hMNqYOY8JlLzhcVhPA9V4DP07xFyPIlnBaBJPjqdIwOwqUSvjJc_OZV_y7MmasxkgQFCA0eyYyDQE5T1-Wgx2UTxHZumate_v0fhWUiPoZLmbNPNUDfLTSMxOMp_1HmhfxVs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازی با خون
🔹
سناریوی چند مرحله‌ای برای تجزیه ایران از دعوت به حمله مسلحانه تا دفاع از عاملان قتل در قاب رسانه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/akhbarefori/652435" target="_blank">📅 22:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652434">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAi485fnKMuW3gcVkJclpgiDUC6sLlpJ7OFZd4tvR1Rk_HXnlzphLe7IcbYmHTgMrjpUp_rJyUQpePdN_7M4chGZGrUp4yl9rZeHmKWZGiF64aGEsI1zcYjl2x1DpmgvLoR6cMxHaSkQnYegKp1ami-W-szW9OYiBVOY37VGbLufVm6-T7fHS2jCH_kwdJnarWclbJwycH64PKWLjgntkVR6TErXinsAOX2nG5AEqGLxo3DkxjJgwIgy1vFr0dg_KRCthlnAQ9t3JjONAPF5jM3-VesB2YdGR1ADE_InBdQsNgdSF2lBE2hMcZ55OA5zSaBBqyXJMnMexqwiwduh5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: وظیفه خود به عنوان حافظ امنیت تنگه هرمز را انجام می‌دهیم
🔹
وزیر امور خارجه درباره دیدار امروزش با همتای هندی گفت که ایران همواره وظیفه تاریخی خود را به‌عنوان حافظ امنیت در تنگه هرمز انجام خواهد داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/akhbarefori/652434" target="_blank">📅 22:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652433">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
آتش‌بس بین لبنان و اسرائیل برای ۴۵ روز تمدید شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/akhbarefori/652433" target="_blank">📅 21:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652432">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Blf3FuhUyXJEeMWSVEpxJMakunpv1cs92fzLShVW2OEmQ1H9Y-tyXIBDgs5lz-SPx-BcEel16XlFl52_illTuv94PUJxmyepcAf9vTgV-lQVgmXI2-UCqeWxaRHnrKnyNLVj10cMLOQbPPS0OBpe-LJw_41JVUjJOAIysUOPk-zZzM92Nxld7t8SplE3ikGWfBW0LwbNFBPTJdWJdqjdpumbWBbZ8JOQ7tqu25243Nsn5OAP-ejGQDpcFw-fft8FVQwlRFXH-J-eYo-1W2laVUEnliIfsKYSYLAK_hnFH39RyXos3Bpq5fAQhbQ3aXT1d-mi-pyfxIiTaQHAtt8WhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حملات عربستان و امارات به ایران چه تغییری ایجاد می‌کند؟ | نتیجه خودشیرینی برای پنتاگون چیست؟
🔹
نزدیک به سه دهه است که مقام‌های پنتاگون در دولت‌های مختلف آمریکا تلاش کرده‌اند کشورهای ثروتمند عربی حاشیه خلیج فارس را متقاعد کنند که توان نظامی خود را گسترش دهند و در برابر تهدیدات همسایگان قدرتمندشان، نقش فعال‌تری ایفا کنند.
ترجمه گزارش المانیتور را در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3215165</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/akhbarefori/652432" target="_blank">📅 21:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652431">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwJHf6VSavGqp6YqD1fBQ3aWvit411dg9UfTXWS_bGrVkqcqOTiejYGqxCgiIh5MupM_m3DUMg4ZC9BCJv62hmUr3qpAr2IuuNF-qtF-mVqt2lnjxDtFP-SPsIstdFzsN3DjafS8Bc0GIxKeFJLpXXNh3FpzOVJJoaSGdRlpJLICHXCCf6wj8XXROzPXN72U2SotUELwgsQBUWF2IHX6Sn5eMMhRJ20qH3PCURMem-12OGMZCzgC_JrwgF3xsavdU1KwyAp0WoKBEj138Neo6g9WkP2iokjlXYzuh3Iee6QCVcBN7uELD7FjVKOiJeNy3QOAEzwwMOZ92NtRlTcg7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعیین جایزه ۲۰۰ هزار دلاری توسط FBI برای کسب اطلاع از افسر سابق نیروی هوایی آمریکا که به ایران پیوسته و اطلاعات نظامی حیاتی را لو داده است
🔹
شبکه فاکس‌نیوز گزارش داده است:
🔹
«مونیکا ویت» متخصص سابق نیروی هوایی ظاهراً از سال ۲۰۱۳ فرار کرده و اطلاعات طبقه‌بندی شده دفاع ملی را در اختیار تهران قرار داده است.
🔹
او متهم است با استفاده از دسترسی‌های امنیتی خود، هویت همکاران سابق و جزئیات پروژه‌های حساس اطلاعاتی آمریکا را به مأموران ایرانی لو داده است.
🔹
مقامات امنیتی آمریکا معتقدند ویت پس از خروج از کشور، همکاری نزدیکی با نهادهای اطلاعاتی ایران آغاز کرده و در عملیات‌های سایبری علیه پرسنل نظامی آمریکا نقش داشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/akhbarefori/652431" target="_blank">📅 21:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652430">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
نتانیاهو به گسترش اشغال غزه تا ۶۰ درصد اعتراف کرد
🔹
نخست وزیر رژیم صهیونیستی به نقض طرح آتش‌بس ترامپ برای نوار غزه و گسترش مساحت سرزمین اشغالی به ۶۰ درصد اعتراف کرد.
🔹
این درصد بزرگتر از آن چیزی است که در توافق آتش‌بس منعقد شده با میانجیگری ایالات متحده، که در اکتبر ۲۰۲۵ به اجرا درآمد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/akhbarefori/652430" target="_blank">📅 21:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652429">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ادعای ترامپ: من تاب‌آوری ایران را دست کم نگرفتم
🔹
ما پل‌ها و نیروگاه‌های ایران را نجات دادیم و می‌توانیم همه آنها را فقط در عرض دو روز به طور کامل نابود کنیم.
🔹
من تاب‌آوری ایران را دست کم نگرفتم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/652429" target="_blank">📅 21:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652428">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mci7kc_YJlnOnxjCpSA7AmBDY_67ArRWyXzB47yORCXFygCf211MGcTNB7MnDe83lmA5G0otGciZL4uhvCjCBcbc7Kr_wEuhnrvz1snU3_IUkYfXDWx1TpZR10bEqXgkr7bx0CgeF9gJFFHwfuN68kmmJh27c2Jy3LqNZTA0XlyNBiY6wLwoMAUlBUtiTw3h7TdVUk-bQ7rtX3KYTkZYcJfl56JQjLCe7cFVc-g-VjnlC-NVPMIkOPC6_apgJLkEjcA3QvXXLl7nuaoHCwPOJaPpbWgUkyqHN5aM7uJVfppX7ALh53AggoibNIm_X3KFRXdUggVIE75zrMOvh11o_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جانسون: عملیات خشم حماسی به پایان رسیده است
🔹
رئیس جمهوری‌خواه مجلس نمایندگان آمریکا: عملیات «خشم حماسی» آمریکا علیه ایران به پایان رسیده و ایالات متحده هم‌اکنون به دنبال بازگشایی تنگه هرمز است.
🔹
دولت آمریکا در حال حاضر به جای اقدام نظامی، در حال مذاکره با ایران است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/652428" target="_blank">📅 21:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652427">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAfwM45XsH7SW9GKG_aT5qPT4cfB1cbFIMvOMsg-lNlrIoun9wDyDSCAGzJTStIuXRCs2n21ZK1aXmVCa2mrCmXfSGLSQL8bUzCGXube8uwwy_JQxEEV_o5_NWwDrkDymhcF-3Vk2Wqd6J4aav77eciVFHNRfJTYOsirScqOL8_q1AqjY3LjXLY3XuDVyGPJc9kj5CoYpsByfMdxy-ptrGZ7YFgHfy9Vhwf5zUiQkJ8PfBY72NnGiBQqokYSKyRsB7NoCiMlQlFzmsyJAFjZFJeKeInxThpjpA2F6FlTF7qVurRa4IjR69lLexyMYx3JHk1RmuKhid1rwWgm-oC7Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکونومیست: قیمت نفت به‌زودی ممکن است به شکل تکان‌دهنده‌ای افزایش یابد
🔹
بزرگ‌ترین شوک عرضه در تاریخ نفت به‌سرعت در حال بزرگ‌تر شدن است؛ حدود ۲ میلیارد بشکه یا ۵ درصد از عرضه سالانه نفت جهان به دلیل بسته شدن تنگه هرمز از دست رفته است.
🔹
به زودی ذخایر خصوصی در کشورهای ثروتمند شروع به اتمام می‌کنند و قیمت‌ها می‌توانند به شکل تکان‌دهنده‌ای افزایش یابند که ابتدا فرآورده‌های پالایش‌شده آسیب خواهند دید.
🔹
خطر دیگر این است که ترامپ کنترل خود را از دست بدهد؛ در صورت اجرای ممنوعیت صادرات توسط دولت ترامپ هم قیمت‌های جهانی به.سرعت افزایش خواهد یافت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/akhbarefori/652427" target="_blank">📅 21:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652426">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ادعای نتانیاهو و کاتز: ارتش اسرائیل فرمانده گردان قسام عزالدین الحداد را در غزه ترور کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/akhbarefori/652426" target="_blank">📅 20:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652425">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7NkECgrIT_XNJem_rBsqJFc9UkRf31_RitYnjBmCuSqbWeebsdb27hctKcqFxLMFDbCHIkMyTGV_KsBhBkcsXVOyt8lVKB2CKAU18AYl8GB8VCcnpCIQnH61zLCVU3prEH-e4DHs9EU0CwfkuJw4GKSYxv_REQsJFdV-3i-TAXl2SkYSS7azSSBGgUEd4p-CHfaTdtpRf_1G6MOAPkR0UVxRLYzoHZL2F3vpot8_jqr65LeBPrJRp1KJjLbU1f_RUc1AOyqG7sjpKeMTs8oDqhAYfkHX6ZCas2EEHv-psmBRtJIaKiN-v8Z6PVepBV5VfdrWc0XxV6m-UeNgf9dtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش بهای نفت و سایه رکود بر اروپا در پی تشدید تنش‌ها با ایران
الجزيره:
🔹
سپاه پاسداران اعلام کرد از عصر چهارشنبه تنها ۳۰ کشتی از تنگه هرمز عبور کرده‌اند؛ در حالی‌که پیش از جنگ روزانه حدود ۱۴۰ کشتی از این مسیر عبور می‌کردند.
🔹
هم‌زمان با بی‌نتیجه ماندن نشست پکن، قیمت نفت بالا رفت و بورس‌های اروپا نیز در میان نگرانی از بحران انرژی و رکود سقوط کردند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/652425" target="_blank">📅 20:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652424">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPRdGIGrxRyl5uFiinWLQaFmSEZcTr9XR9zbCUylYW5vDFXEzJo9rcYojnWA-SAyKS2P167WP0sceHlXsuJe8NoPRQaD6cOicJLZeW_WVxIg0awwkygkbuk96Qtf640Tq5tHj7JDjT62luxRm-p0iXGLHOHogCZZI_IlKDAU7FIgkmrFxWCJL80q4EUzXlmOprQK_dxOny2dxBmDlf2k7JpQKTcX5NaVaTIpKKCvJHq0WqqISkg6YVWgjIBJ4zmPcjxrhfwfEwoV5YyizrpiXZVna-rnNTbU4hCc1GEdyTO9xzvQsh2pZM5I8U66vjyMhF7hrs6GePrPyoe9qnKtzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا برای این زن در ایران ۲۰۰ هزار دلار پاداش تعیین کرد
شرح ماجرا را در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3215122</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/652424" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652423">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e91b011a6.mp4?token=NFJ_AQ4kzJ5RyiwXqX_wjf1pdj1t-RfVL1dAko8hM5Ca9uBHELEOMpGhPz06mI1x7N0vlBFr0JObRIHZik37zRiE9HrId3kkyK3lb29S0qI-UnrzIxZvHQrcrGVtlhhnPkI9Hr9aJZW4YSBY-iuaidtWNQxMLOxU8k5UgfnMipAFG3rqSstr8ueqBd5GC0wC6smxavqYeqVI0hlltsZlk-HgnnarOiYRFuNcMQPCSRUu-0f3gyzeCMgTMg0CxnDQ7eJT8pOkXSn6kdKQGbSNulIasnK6kSqWwHLlqLO1rpIX2SkUjoxfENNRammk8kQ_CoclfK4G18LsqfdTkQAaPyfgZEwNPny69AWJ9NiwiIbO7f0abQ9Q03CYyG5VZxmhUSyl870W4WWhNcz0Sjd1_8oRGe7Is97-w8pMv8PDhrdHom55VPfJsGgnyV6JcVOB6J8rBHq1y64N6IuC33RRNTC7h-jLJqA69H0ULrBzHBukMKLMd15igFA5fAgGRjYfZLhKntvNaL2-X3X-OqEjovSdvIUHdn5sYCmxYgpvH6StcWWn_hgWYNAb6yCfV1XEMs0HlMPahA9tz5h6wgBZ1wKXb1ZhSMCVjfHYK4pQ9pB1El4z0gvoVg2ju0_8cgLnxGgqXr2YLZuJYDHvWSLOoFjUd0v_gG2RK1w_uvhJKdU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e91b011a6.mp4?token=NFJ_AQ4kzJ5RyiwXqX_wjf1pdj1t-RfVL1dAko8hM5Ca9uBHELEOMpGhPz06mI1x7N0vlBFr0JObRIHZik37zRiE9HrId3kkyK3lb29S0qI-UnrzIxZvHQrcrGVtlhhnPkI9Hr9aJZW4YSBY-iuaidtWNQxMLOxU8k5UgfnMipAFG3rqSstr8ueqBd5GC0wC6smxavqYeqVI0hlltsZlk-HgnnarOiYRFuNcMQPCSRUu-0f3gyzeCMgTMg0CxnDQ7eJT8pOkXSn6kdKQGbSNulIasnK6kSqWwHLlqLO1rpIX2SkUjoxfENNRammk8kQ_CoclfK4G18LsqfdTkQAaPyfgZEwNPny69AWJ9NiwiIbO7f0abQ9Q03CYyG5VZxmhUSyl870W4WWhNcz0Sjd1_8oRGe7Is97-w8pMv8PDhrdHom55VPfJsGgnyV6JcVOB6J8rBHq1y64N6IuC33RRNTC7h-jLJqA69H0ULrBzHBukMKLMd15igFA5fAgGRjYfZLhKntvNaL2-X3X-OqEjovSdvIUHdn5sYCmxYgpvH6StcWWn_hgWYNAb6yCfV1XEMs0HlMPahA9tz5h6wgBZ1wKXb1ZhSMCVjfHYK4pQ9pB1El4z0gvoVg2ju0_8cgLnxGgqXr2YLZuJYDHvWSLOoFjUd0v_gG2RK1w_uvhJKdU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستگیری شبکۀ مرتبط با موساد در اردبیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/652423" target="_blank">📅 19:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652422">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
بن‌بست جنگ ایران؛ ترامپ دست به دامان کنگره شد
فکت‌چک:
🔹
رئیس‌جمهور آمریکا پیشنهاد تعلیق موقت مالیات فدرال بر بنزین را داده است. این امر قیمت بنزین را حدود ۱۸.۴ سنت در هر گالن و قیمت گازوئیل را حدود ۲۴.۴ سنت در هر گالن کاهش می‌دهد.
🔹
اما این طرح نیاز به تأیید کنگره دارد و هنوز مشخص نیست که آیا حمایت دو حزبی کافی برای تبدیل آن به قانون وجود دارد یا خیر.
🔹
کارشناسان می‌گویند که حذف مالیات بنزین، حتی به طور موقت، می‌تواند به افزایش بیشتر قیمت‌ها نسبت به حالت عادی کمک کند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/652422" target="_blank">📅 19:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652421">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scu2T8mav7ogX-tt1VLbXAojNQSiKppZ8dXoW6Ov2_drPSPx1gbY_cTef4aoDfe0v-Y3ykoBhvMjMSvCrAdTo_uXoJlRb-8bvQ6jLi6vEwQC9VySrqTfBRMH9LM6sVM2uuehQTgVnB0MvMyJevab8ySHf7MA9qw5i7dwpdACENwRtKl_3t4A2PDnAmUjfESA0e-fjSTI89goEyn7HlTTmXzF7Q6zAjajOqdCpE0GVzoU6cV6x89brGHEP0uy_4dyrr0VMUfPSV_NoOyKilPDs6FWvbBLqOrnPepryVOv2itPKNBprOzRHjUJfpwE555siw-sBbX4ssPXmPnsZr7tkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا ایلان ماسک در عکس یادگاری چهره‌اش را تغییر داد؟ | هراس از اسکن چهره + ویدئو
🔹
در جریان سفر رسمی دونالد ترامپ به چین تصاویری ازایلان ماسک در کنار تیم کوک منتشر شد که در آن ماسک هنگام عکس گرفتن، حالت‌های اغراق‌آمیز و طنزآمیز به چهره‌اش می‌داد.
بیشتر بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3215173</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/652421" target="_blank">📅 19:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652420">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
یورونیوز: ایران به دنبال اعمال عوارض بر کابل‌های اینترنتی هرمز است
یورونیوز:
🔹
ایران به دنبال اعمال عوارض بر کابل‌های اینترنتی هرمز به عنوان اهرم جدیدی علیه غرب است
🔹
رسانه‌های پرنفوذ ایران از تهران خواسته‌اند تا بر کابل‌های زیردریایی از طریق تنگه هرمز عوارض وضع کند و ترافیک جهانی داده‌ها را رصد کند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/akhbarefori/652420" target="_blank">📅 19:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652419">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a02fdd912.mp4?token=pmwBKyKUzYUwTLIKL_-4LDVGzafIPW6qSyaqPZGcmOODf39F3ObhOzanM0hvEtbJdZEwJJ1oSyQZj7PfqFI-2kSOLv1vabSgYR6KZAckOh-BMHiMDrK2XEyZmO2lNdN1QRkZ82LPT4aIGNFULMI4-XP00G11qzKNimHtCXVUlDHS0amqIsFyTNCvYFIW40-FL6CvKRVhfJaO2UTdSX2-m0ywbU-KMyJlqxLct-ZCMttx8_IM26zaS4cqYG0NYbu6zglsOaw5H42HkpY3Y-5IEGRRy3Ad_WInv1ximD9K-EMc675SkgNWzwaE30mJoBVDpDLGIa75XEBAHPdThN4NZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a02fdd912.mp4?token=pmwBKyKUzYUwTLIKL_-4LDVGzafIPW6qSyaqPZGcmOODf39F3ObhOzanM0hvEtbJdZEwJJ1oSyQZj7PfqFI-2kSOLv1vabSgYR6KZAckOh-BMHiMDrK2XEyZmO2lNdN1QRkZ82LPT4aIGNFULMI4-XP00G11qzKNimHtCXVUlDHS0amqIsFyTNCvYFIW40-FL6CvKRVhfJaO2UTdSX2-m0ywbU-KMyJlqxLct-ZCMttx8_IM26zaS4cqYG0NYbu6zglsOaw5H42HkpY3Y-5IEGRRy3Ad_WInv1ximD9K-EMc675SkgNWzwaE30mJoBVDpDLGIa75XEBAHPdThN4NZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع آتش‌‌‌سوزی در پتخ‌تیکوا در شرق تل‌آویو اشغالی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/akhbarefori/652419" target="_blank">📅 19:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652418">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f0c9844d7.mp4?token=JMqoHvxVazyoriqJBuX09yrFUzoIezzezUXGSNB6K6OD3V3df2AlZRM3vraz-NVdRRZxAY9cgGXdKoxAL3yAw8GS2SebI4UxL6zAtk8QPAU0TJ4gT_MMHx3ZmekiM1HuethTabfwfutrmWDrzFSK3pcgkmUeJmxc72nrV_Dk9uHhmtGDGQj-sA18DJ9EXUZj71YR7WZ5DX1zWWK-ABcokIZ_8KgXzXgBRCuToJ00530QyVW7T4xjalC5aIJF3GECwIiT6yxO34XkifHbkyfvfGoIpwGmtX8ObOOyfXj1BaaAWb_h8lbKZ8iqJVVQBetoQXouqH087Bi5mrN4PBCw4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f0c9844d7.mp4?token=JMqoHvxVazyoriqJBuX09yrFUzoIezzezUXGSNB6K6OD3V3df2AlZRM3vraz-NVdRRZxAY9cgGXdKoxAL3yAw8GS2SebI4UxL6zAtk8QPAU0TJ4gT_MMHx3ZmekiM1HuethTabfwfutrmWDrzFSK3pcgkmUeJmxc72nrV_Dk9uHhmtGDGQj-sA18DJ9EXUZj71YR7WZ5DX1zWWK-ABcokIZ_8KgXzXgBRCuToJ00530QyVW7T4xjalC5aIJF3GECwIiT6yxO34XkifHbkyfvfGoIpwGmtX8ObOOyfXj1BaaAWb_h8lbKZ8iqJVVQBetoQXouqH087Bi5mrN4PBCw4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قهرمانی که ۳۰ سال برای ایران جنگید!
@TV_Fori</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/akhbarefori/652418" target="_blank">📅 19:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652417">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlOTUWI5O9TAivPHbuwRwZA3c2dxKfkmLWqFRCUWupPhy7ntSulG2G2c8rHHoT1snUhj3nml6UyiRqTx00KWmgXNbZWQH0k49ylNz0W9RbDYgPwxCPpuByfeZWGq4fKxdSAm2Az6u1L2k421w50YfyNFjwBIiURYhR4cT3tXptaC0FAPhBfGsd5GQXIgjRabffNdiPc1T2PstFMCMQEKz5QhJ2xIORAbZFvTLglcyMovJaKzna3V5cmC9YsJNJYLKQLjAMmr8mYXk0MhiNQ7d3deD6cOk-xS7PSgrs_ai1cxEuO4xsyEuE_DbBfrbxqQrOyNY9DtiegBNkz9hSjp7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میز کار هم می‌تواند سبز باشد
🔹
هر انتخاب آگاهانه در محل کار، قدمی برای آینده‌ای پاک‌تر است  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/akhbarefori/652417" target="_blank">📅 19:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652414">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJCjQ32AZ5XlW1Ho2CLwbX1cSLWs1MnrRndWtq1ILYC7eHOE59s-iyC3xVvvsM-0ss5xlfT3odkCaUws8-a080YEf5VFqr8oPtuyZVmWWCtPj64_t92lAf0hFqhXeEQ8ZDdTnXZsDxaGRvxt8W7tE_JczSl7D9tHIVxNF7-KibGM9uz7AqK5P4WqI409eicpH_0M6E6dwi4tugoACM9usaAQdmrLuAt3wSMi9zCvd10u_DRV_8lHea0vnO6GCc1jU8HcirKaOT_xDKC0rcSeSDI5ExW11EIrHl4NT-WMpZegZxXzLrdTx-aVOVPNqDk_J743d_dUSSgI6mYcJX-rOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: با شکست دیپلماسی، ترامپ با مجموعه‌ای از «گزینه‌های بد» در قبال ایران روبه‌روست
🔹
ترامپ در میان توقف مذاکرات صلح ایران، با افزایش فشارهای داخلی و بالا رفتن مخاطرات ژئوپلیتیک مواجه است.
🔹
گزینه‌های تداوم درگیری نظامی، پذیرش ایران هسته‌ای یا عقب‌نشینی از مواضع قبلی، همگی گزینه‌هایی هستند که نفوذ آمریکا در منطقه را به چالش می‌کشند.
🔹
نارضایتی‌های فزاینده در داخل آمریکا نسبت به هزینه‌های جنگ، مانور سیاسی او را بیش از پیش محدود کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/akhbarefori/652414" target="_blank">📅 18:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652413">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vR1KuiH7TJp-7d4xrIUOGkrCxuBwAEQGX-7Q1A0h66MOoTi8M6kf0skhv9fGv3NZGRt4DoNHAjPIjIqzYKMQD0gh8hILOgm6qnXiTebbB9Jg2bSR6k9NT-c4_emS5-aJtZoHqV70Sg4VBrwQeRDZ-PkSTjAI_z0ehw6KfaqahuLEs_a-QdqLUH_4XilaAUjxdFNEPP-4-zjOA0RjaytRYBIyQcaxeY_i1SFwcEcBlSHRJFmI1Lu1LzIUFuuUVg6M4M46VrAM_emSr6t5x-uF6VazsjG2v_JM_cQkBaovmXtrXLTM20DYiCxQYNB0J6DQ6kYkk8eVET9l9XwGXEEanQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ تاکنون از چین در مورد ایران چه چیزی به دست آورده است؟
🔹
این که دونالد ترامپ، رئیس‌جمهور آمریکا، بتواند همتای چینی خود را متقاعد کند تا برای پایان دادن به جنگ آمریکا با ایران کمک کند، انتظار بالایی بود؛ جنگی که بازارهای جهانی انرژی را دچار آشفتگی کرده است.
ترجمه گزارش سی‌ان‌ان را در وبسایت خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3215152</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/akhbarefori/652413" target="_blank">📅 18:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652412">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23e9f34e9d.mp4?token=upSS34nkM1lmSQQgLwcmyZPPwzuLXGWeiv5F_smEd1D3dWu3XeNluVSVMwtBtC6Jr30Q9GdmrADg8KqKFlQzquKbZm2hhpzK3ZIgCeiZKk581lIm54Hkv400ESDN8C2DoPvKMiVdjEabCMs5icayHp2knG3PFDEow--WPXvrVzy5q75Xgnnju7rh6myEmRcX2KHGdDSaHEpCQgQIv_EbvUA4FwdCIfkURTugoWHoxpWMbS82tr3swcFYzVMsZ_axGLtaMzwr9fg6danQeqWPLl9LY5sdMUva50xDS_DnjUKpr7et5Y07lFXxozRwnm7TzoQqgxclybZAvLe0ru1YuS84UlwsvhaURlN1DovvpNL9DcmnNbhWQkg9y-49tQ0XU10lX69y-AAjPkYze4YHmPeIwb3Xops4vCdIO6q9t1yPESBb8wpyT4dHkQsWcTVO245eusXnIAqQBlbv3c5glaVNeRrU93mmUg7aOUIv2GDAgRK2XGp3xwogWPTm7prCiB9ntmb89Or6wpvPBBKG4BKc4q6Hcqxd3IZrQL5GbYw0tA49SJn1NRu4Xrc6ldOqwA-Rk3NA5UlwF6buj3n1H3_LhWqrvC8jVphNVG6YXf0nPcRf9fJrSM7VtNkT045NNGBlxtRg8JNK--kXSBVHejfx-3sAcMXI1p-sN-fSLos" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23e9f34e9d.mp4?token=upSS34nkM1lmSQQgLwcmyZPPwzuLXGWeiv5F_smEd1D3dWu3XeNluVSVMwtBtC6Jr30Q9GdmrADg8KqKFlQzquKbZm2hhpzK3ZIgCeiZKk581lIm54Hkv400ESDN8C2DoPvKMiVdjEabCMs5icayHp2knG3PFDEow--WPXvrVzy5q75Xgnnju7rh6myEmRcX2KHGdDSaHEpCQgQIv_EbvUA4FwdCIfkURTugoWHoxpWMbS82tr3swcFYzVMsZ_axGLtaMzwr9fg6danQeqWPLl9LY5sdMUva50xDS_DnjUKpr7et5Y07lFXxozRwnm7TzoQqgxclybZAvLe0ru1YuS84UlwsvhaURlN1DovvpNL9DcmnNbhWQkg9y-49tQ0XU10lX69y-AAjPkYze4YHmPeIwb3Xops4vCdIO6q9t1yPESBb8wpyT4dHkQsWcTVO245eusXnIAqQBlbv3c5glaVNeRrU93mmUg7aOUIv2GDAgRK2XGp3xwogWPTm7prCiB9ntmb89Or6wpvPBBKG4BKc4q6Hcqxd3IZrQL5GbYw0tA49SJn1NRu4Xrc6ldOqwA-Rk3NA5UlwF6buj3n1H3_LhWqrvC8jVphNVG6YXf0nPcRf9fJrSM7VtNkT045NNGBlxtRg8JNK--kXSBVHejfx-3sAcMXI1p-sN-fSLos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آمریکا: درباره بمباران ۲۲ مدرسه در ایران تحقیق نکرده‌ایم
🔹
- سناتور آمریکایی: اگر به ایرانی‌ها هشدار داده شده بود چطور ۲۲ مدرسه را بمباران کردیم؟
🔹
- فرمانده سنتکام: هیچ نشانه‌‌ای در دست نداریم که این چیزی که شما گفتید را تأیید کند.
🔹
-سناتور آمریکایی: چند مدرسه را بمباران کرده‌ایم؟
🔹
-فرمانده سنتکام: درباره یک مورد مربوط به تلفات غیرنظامیان تحقیقات در حال انجام است.
🔹
-سناتور آمریکایی: پس این اطلاعات علنی مبنی بر اینکه ۲۲ مدرسه و چندین بیمارستان بمباران شده‌اند را چطور توضیح می‌دهید؟
🔹
- فرمانده سنتکام: هیچ راهی وجود ندارد که بتوانیم این را تأیید کنیم.
🔹
- سناتور آمریکایی: درباره این ادعاها تحقیقات انجام داده‌ایم؟
🔹
- فرمانده سنتکام: نه انجام نداده‌ایم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/akhbarefori/652412" target="_blank">📅 18:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652411">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d3f626cc5.mp4?token=jNK967fFETnXC0Iq8csREQM22r9FOTiH8nli0tyBfd8gf9kbQTGtVrU0AdS_KQWCJ6-3Ta9hvVHnyx3b1QvNmqd0gJ-TYeN6sRyIET4gwPWzCZ4SIVW_h3GsEJvG-3pNUrMQg8wKrwUqPDVJ-0ij3eFm0u0SXkwXHYbxgUw7NDwLag8r632TRVus8LI191Cgsh-corYo_kc5RQBMNJExDLWVUHFXydanUrE7RBjajC1K_M1VGEBq1bfU8yBt5JADnY45yCtSlp51_83bV_SPo3rk0F_Sd0qaJj3mHXcVwMnlbjTS_p_mATNPIheSjsWRVxFJcu0kdQ3-YOuY27sRfr7qhGcqmGn53vYyE6-21gCJvGeoMhBACQMllsBAYGFaQT1PJlSNP9vxWEufziSUiPvL0rlN196edPOYrMuauhdVpDLewQPaUDfp6L7bLs85xHkHyJmgPiFKFLoeavKlZf3LJQSTWZqZr1SOkMoarmBMSGo5mwfze0fZbidcrqhV-vTha4ovXRkBXqqGdvOJV_hTcfKnPuEP4tkIIDthPQ3kIbKcD6v0umav-193uG32y04IwnevfNUfQDFLFCJ7ZblKclCfGwD0IYht3cLugUGZXw6LFRmWj13GbXLcmnury7oSkh_JLaA31CMhpAHmpiQOfGMr-UaOQJpuFTrPI1M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d3f626cc5.mp4?token=jNK967fFETnXC0Iq8csREQM22r9FOTiH8nli0tyBfd8gf9kbQTGtVrU0AdS_KQWCJ6-3Ta9hvVHnyx3b1QvNmqd0gJ-TYeN6sRyIET4gwPWzCZ4SIVW_h3GsEJvG-3pNUrMQg8wKrwUqPDVJ-0ij3eFm0u0SXkwXHYbxgUw7NDwLag8r632TRVus8LI191Cgsh-corYo_kc5RQBMNJExDLWVUHFXydanUrE7RBjajC1K_M1VGEBq1bfU8yBt5JADnY45yCtSlp51_83bV_SPo3rk0F_Sd0qaJj3mHXcVwMnlbjTS_p_mATNPIheSjsWRVxFJcu0kdQ3-YOuY27sRfr7qhGcqmGn53vYyE6-21gCJvGeoMhBACQMllsBAYGFaQT1PJlSNP9vxWEufziSUiPvL0rlN196edPOYrMuauhdVpDLewQPaUDfp6L7bLs85xHkHyJmgPiFKFLoeavKlZf3LJQSTWZqZr1SOkMoarmBMSGo5mwfze0fZbidcrqhV-vTha4ovXRkBXqqGdvOJV_hTcfKnPuEP4tkIIDthPQ3kIbKcD6v0umav-193uG32y04IwnevfNUfQDFLFCJ7ZblKclCfGwD0IYht3cLugUGZXw6LFRmWj13GbXLcmnury7oSkh_JLaA31CMhpAHmpiQOfGMr-UaOQJpuFTrPI1M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ به منتقدان جنگ ایران: خجالت بکشید؛ شما خائنید
🔹
دونالد ترامپ خطاب به «دیوید سنگر»، خبرنگار روزنامه نیویورک‌تایمز گفت: «من [در ایران] به یک پیروزی کامل دست پیدا کردم. ولی فیک‌نیوز، یعنی آدم‌هایی مثل تو مطالب نادرست می‌نویسید.»
🔹
رئیس‌جمهور آمریکا گفت: «تو یک آدم جعلی هستی. ما به یک پیروزی تمام‌عیار نظامی دست پیدا کردیم. من فکر می‌کنم چیزهایی که تو می‌نویسی نوعی خیانت است.»
🔹
رئیس‌جمهور آمریکا اضافه کرد: «باید از خودتان خجالت بکشید. فکر می‌کنم واقعاً خیانت است.»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/652411" target="_blank">📅 17:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652410">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
امام جمعه زاهدان با انتقاد شدید از عملکرد مافیای اقتصادی در شرایط جنگی، خواستار برخورد سریع و قاطع دستگاه قضا با زالوصفتانی شد که خون مردم را می‌مکند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/652410" target="_blank">📅 16:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652409">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d04831a3b.mp4?token=s2cCXrIJWH51aKuyhUripp9_5SfWNKtKIUBw9C__fpmXgAAKmYkd95qA9HU4sf3VSc0BRGTqtrLOdKmhXjIwxPPLfO4wQLmY5CJYGZhcRyf-BfV53881fMO9h23vZKgypB4jIxV9yKDRFcNnS2v2HOwpt4xgsiMwT_u_nixTs2kZZLtae0GMwQOT-hMg7sncOgXA1ANjcHiH6aCWOIvdBK5DCu4nJrRTdNiecwRSFf20qY-f2Doex7HfBKfUwVuFwtHsjd0FRQMLn5rrG9wElQfyue3ilLF04yp77vfyMWX8NRSCwe_rqJE-rdSAeOI7lYxtimHGgoGG8CxMp5iRzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d04831a3b.mp4?token=s2cCXrIJWH51aKuyhUripp9_5SfWNKtKIUBw9C__fpmXgAAKmYkd95qA9HU4sf3VSc0BRGTqtrLOdKmhXjIwxPPLfO4wQLmY5CJYGZhcRyf-BfV53881fMO9h23vZKgypB4jIxV9yKDRFcNnS2v2HOwpt4xgsiMwT_u_nixTs2kZZLtae0GMwQOT-hMg7sncOgXA1ANjcHiH6aCWOIvdBK5DCu4nJrRTdNiecwRSFf20qY-f2Doex7HfBKfUwVuFwtHsjd0FRQMLn5rrG9wElQfyue3ilLF04yp77vfyMWX8NRSCwe_rqJE-rdSAeOI7lYxtimHGgoGG8CxMp5iRzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کنایه محمد منان رئیسی، نماینده مجلس به عباس عبدی: یک ادم وقیح است که خودش از همه رانتی‌تر است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/652409" target="_blank">📅 16:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652408">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owk-5cmBVPi3Y9YtDHVsUzwjH75s-baXemdgoB6Y-fi9idyRSZqsjWQFyvQE8bgtcyKdnFLuHm-UhinQ1gdm4VKFJFKj0BWSShk9rbw4XmHv4dQV5a89DmI6GynY3FIIXuQgYqOWzMivCk-4fJH5jUOkr6mtIRaooF-FVoK7EM1vljHIrYyPq5TAIYKBGdO5JZVmuAGn9NSuNKZ1eruLeCaiN-W9xGR66iR0Hi1K03qCR6pQrwdKLg-XZctadXG2e-ns4458upKcMHTFKncYxBpZs4W94o3BaqvBv_PZVyAezB1JQAGyeFj4oCcVRNEP5oISrIZ-_DYjjMEt6Du-HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خرید هوشمند، زمین سالم‌تر
🔹
هر بار که پلاستیک رو رد می‌کنی، یک قدم به زمین پاک‌تر نزدیک‌تر میشی  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/652408" target="_blank">📅 16:34 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652407">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Igdl8VHeBQMjN1kfMXTku3izTf6eUDIVUsRF_paSumWYw309KEczQ6i2mekloPt1gF4VmwqryrsBSOw0McG53juSg3rGEvQVq13LH7zo-ZLwFMHDPk0h9L5J58Lpc1WyAs8mFZCOlLF6b11cNDeuJnXOilYcW53HLR5LKATvvl-KTDo3lULCVE84JzKP_g_jRnFyqoSKRYJ39KMqlEykFviNAUTAglfqYucIokIPc37hl2ArWyD9gdS7NPBHJ_QJ9vma0m_DaOSlPSS1GV8QwpZXOlwN11zZCRnMill2Y8iNo0fw3SYiSMyQf5C3YbT-1A7Q5-BDn27GThcI6_yQOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گفتگوی سران آلمان و آمریکا درباره ایران
🔹
«فردریش مرتس» صدراعظم آلمان امروز به‌صورت تلفنی با «دونالد ترامپ» رئیس جمهور آمریکا گفتگو کرد.
🔹
مرتس درباره این تماس تلفنی گفت: «من گفتگوی خوبی با ترامپ داشتم و ما توافق کردیم که ایران باید همین حالا پای میز مذاکره بیاید».
🔹
«ایران باید تنگه هرمز را باز کند و باید از دستیابی آن به سلاح‌های هسته‌ای جلوگیری شود».
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/652407" target="_blank">📅 15:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652406">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zixaooe92l74C8HK8qE-MPV2CZAPVqOHVmmlWe7TjrPhJA_oaZwUE2xG1IQIbdqhRE8661OQGXztBlUw-zynoKlXGLwDbAVyQYfsnt7Bd4t22lVk6uWCwRLQBP8Ua-Slrg3xfp3uIQwyY6FNFHCqDg8Ebspg2tD95RrZn-1PzCGQQWZfCfluCHYyQcHcTSoTVFfwjjvR61YHP46WMTyLp41xedShbQy0BWnY9t9bQgf4Nde7Qo4Jxfq-A_hEWLjBrl6JncN89gtjOQkTAwCwrhzim9R4aTvQTkPBMP8hnPSPXnWntf4kOPSDpaSeDLCurJe8I9crVrzCamL4ecYi9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رزمایش غافلگیرکننده اسرائیل در امتداد مرزهای مصر
🔹
روزنامه عبری معاریو اعلام کرد که ارتش این رژیم سحرگاه امروز با مشارکت چندین لشکر، مانور غافلگیرکننده بزرگی با نام «گوگرد و آتش» را آغاز کرد که هدف آن آزمودن آمادگی نیروها برای سناریوهای عملیاتی اضطراری در جبهه شرقی به ویژه در حوزه استحفاظی لشکرهای ۸۰ و ۹۶ است.
🔹
معاریو افزود که هدف استراتژیک این رزمایش ارزیابی سطح آمادگی و رزمی ارتش برای مقابله با سناریوهای اضطراری متنوع از طریق آموزش فرماندهان و نظامیان در تمام سطوح از ستاد کل گرفته تا واحدهای میدانی با تمرکز ویژه بر منطقه مرزی شرقی که لشکرهای ۸۰ و ۹۶ در آن فعالیت دارند، است.
🔹
این روزنامه عبری تصریح کرد که این مانور شامل اجرایی‌سازی سناریوهای متعددی است که رویدادهای اضطراری را شبیه‌سازی می‌کنند تا نحوه عملکرد نیروها را آزمایش کنند به طوری که این رزمایش برای سنجش توانایی ارتش برای حرکت در «زمان صفر» از حالت عادی به یک جنگ با شدت بالا مشابه آنچه در ۷ اکتبر ۲۰۲۳ میلادی اتفاق افتاد، طراحی شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/akhbarefori/652406" target="_blank">📅 15:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652404">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b764854cc4.mp4?token=qheIUBRanFAAnT7D6QzKxK7rzKqnDYGJ6OVPxK-1us0X-vTnzuF3MYnOQX4D6-Mp6CtECG_qS27DyhZB_JECf4gST2R3PEYP50bVd-8u-S2uLy2Jst9lAmJJI7WD48XVC-Rtxa4mweCJcPf2AQWFl_Bx6JVpQmFg3a6X3IJWkWg9abG-UYunTqqBxTo7YFs1qGj13LTrrbl0kKGbBu1IozVgurXyo8MZhzvH3ARodA8lDOiw54elP8rM9J_4Q2qmX9a1fA9O4fQGlxGA2rLjgV7TWtZZKa0T_T9fufRNIssnC-IiAmJTvO5gW3V77KRdCtakGs9U8dSLiQ6WiUjVQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b764854cc4.mp4?token=qheIUBRanFAAnT7D6QzKxK7rzKqnDYGJ6OVPxK-1us0X-vTnzuF3MYnOQX4D6-Mp6CtECG_qS27DyhZB_JECf4gST2R3PEYP50bVd-8u-S2uLy2Jst9lAmJJI7WD48XVC-Rtxa4mweCJcPf2AQWFl_Bx6JVpQmFg3a6X3IJWkWg9abG-UYunTqqBxTo7YFs1qGj13LTrrbl0kKGbBu1IozVgurXyo8MZhzvH3ARodA8lDOiw54elP8rM9J_4Q2qmX9a1fA9O4fQGlxGA2rLjgV7TWtZZKa0T_T9fufRNIssnC-IiAmJTvO5gW3V77KRdCtakGs9U8dSLiQ6WiUjVQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ درباره ایران:
🔹
ممکن است مجبور شویم یک کار پاکسازی کوچک انجام دهیم، چون یک آتش بس یک ماهه داشتیم.
🔹
ما واقعاً آن آتش بس را به درخواست کشورهای دیگر برقرار کردیم.
🔹
من خودم خیلی موافق آن نبودم، اما این کار را به عنوان لطفی نسبت به پاکستان انجام دادیم؛ مردم فوق العاده، فیلد مارشال و نخست وزیر.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/akhbarefori/652404" target="_blank">📅 15:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652403">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btb9GGT0SjNcInudfuX9jv52Edwb8InavdvWu_khp5gzNWJyC1Akwi_mRgFik3ZOYgCYvZHEmVRmptKuXKL-6U5F8uKcpewPbDLrIuGB5lQtODYIol_32SfriaHeGv9OrBnC7sr7D-ZPopE5xMLfcuEdzYLbtxgZla4YPifblK1HhE5p_4C59eNcerHIwpfNTsdf2UG5feGbaQbYZ0qcSuDXjlr87vTR4_jBFcsPBpYIYaHDG0aJyMnksr28KkzsAcEjr_tmP5xcH2qL18jfaNJmA1U6V5CDr6SbXILWeeuEuslVqdFUd8XlSsdexqtKjS-hT4uVX5eWr5PBJGJAWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معجزهٔ ذخیره‌سازی ایران مقابل دسیسهٔ آمریکا
🔹
وزیر خزانه‌داری آمریکا می‌گوید بارگیری نفت در خارگ متوقف شد اما شرکت همراه آمریکا در فشار به ایران می‌گوید، تهران تاکتیک عوض کرده است.
🔹
شرکت کمک‌کننده به آمریکا برای رهیابی محموله‌های نفتی ایران، تنکرترکرز می‌گوید، اگر ظرفیت ذخیره‌سازی جزیرهٔ خارگ پر شده بود، نزدیک‌ترین نفتکش‌های در دسترس را می‌آوردند و آن‌ها را پر می‌کردند.
🔹
یک ماه پیش ترامپ گفته بود خط لوله‌های ایران منفجر می‌شوند، تنکر ترکرز اعلام کرد، بدون درنظر گرفتن مخازن خشکی، ایران یک ماه و نیم زمان دارد حالا ۲۴ ساعت از ابراز خرسندی وزیر خزانه‌داری آمریکا برای توقف بارگیری نفت در جزیرهٔ خارگ نگذشته است.
🔹
این‌بار هم این شرکت که پیوسته در حال پایش نفتکش‌های خالی ایران است، توضیح می‌دهد، هنوز هم نفتکش‌های زیادی هستند که ایران در آنها بارگیری کند اما تولید را کاهش داده تا با افت بارگیری نفتکش‌ها هماهنگ شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/akhbarefori/652403" target="_blank">📅 15:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652402">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msz7cGRz5TAprdZs3jQ0IMEqLGGf0l-FcEKvWzdQ7aVwHLxN8dfQYFOTGpUKLACA_bB3i897ZDuFwF0RcivztVZ8k55rAdXLFPrXPkg11j7Y02HAM-u2kkkFMMba6rVAtVq1WQBa5PS2TvzGSDw7ofVnP6afF0Lu_dAMU_5uU5eie0K_9qpjwvl45xY42UFol9w_t2VAWvNsiN5N-QxTIjMAIi5W_lPF7Pfwj6JwC18ifCcR2Nh4Nm-CDZ-LVC0uJ0kXdZmfXT7Lp8iIXaEVHqQBFmyZGFqHdRqUSHlOwfZU7NhOGydOPG6QHKY6pehKYV9twmd93ar1lT6tc5Zz4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک‌ها باز هم مصوبه دولت را پشت گوش انداختند
🔹
کسب اطلاع نشان می‌دهد از بستهٔ ۷۰۰ همتی مصوب وزارت اقتصاد برای تامین سرمایه در گردش صنایع بعد از حذف ارز ۲۸ هزار و ۵۰۰ تومانی تنها ۱۰ درصد تسهیلات پرداخت شده و ۹۰ درصد پرداخت نشده که به توقف تولید، کمبود کالا و گرانی اخیر ختم شده است.
🔹
اواسط دی‌ماه سال گذشته بود که دولت اعلام کرد برای حمایت از تولید و جلوگیری از شوک به تولیدکنندگان درنتیجه تغییر سیاست ارزی، ۷۰۰ همت تسهیلات سرمایه در گردش مصوب کرده و به ۴ گروه از تولیدکنندگان پرداخت می‌شود.
🔹
ابلاغ این بسته به شبکهٔ بانکی اواسط بهمن ماه انجام شده و قرار بود همان زمان به تولیدکنندگان پرداخت شود اما بعد از گذشت ۳ ماه تنها یک دهم تولیدکنندگان موفق به دریافت این تسهیلات شده‌اند.
🔹
مدت اعتبار این مصوبه ۶ ماهه است و بعد از اتمام آن بانک‌ها دیگر الزامی به پرداخت آن ندارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/akhbarefori/652402" target="_blank">📅 15:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652400">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EiwB4kuqbji51TfeqmDx6DuhstqAQKEBTal_D25LCfSuTbXOSgBjCm7CKDRoNCmvJWfyYTnm6XqgkB2UFjBL78603VGxZ1AZxEg5mpSNUf7k4RYdaqJz4x5JGoTNEHIgZZQ79zp5O0HoU3I8qQd12_e_09B_9VpR8FMU4N6ITuE-IHDMRurgMVJwy1weSx7UXTd2aMgK8sbJUfixO2aZsxccUOMvEugvd3u5idms00KrziStk50_ijJEJ-O4cL9O_Y7QYhfzBZT9ZSJMYvcddBl1xFc8JXEr3p-yn1Vg1-08V1ULAZD-dH7I-FL6XJgfK8lRcFSs2mFtdNE6iiUmEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KJq6CDIvIeytTU4JxuCoN4oUZPquBY9xX5puVNVDRgTepNsPEhcYQh2-HkWvYUgHSUkExXEeV2exeughVVSV7I-N6jBhKTtKCrFCyB9rwvveh_Y-jPDy9dOB64y_RsOxO48-OnmD43oIHfxMTv9i4mheLYNAMour43FZKD2wVCzu_IhpSXCamcJPQefZQx5NxeOB-JfFfLE-K6syXupcNnANIw9F5Femo_3KIGY4I-hM7aSNW6Ypxqa2kqlfWQsRLStdvclwhHvvsoh3I4Ph5kVGvqoUpLAPYv5zrBJimdzu8-WD0hxp3QrChCDWOTkZdW4o_GKIU0pI1LP5nmS96Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اعلام سقف ارزی جدید برای واردات برنج و نهاده‌های روغنی
🔹
وزارت جهاد کشاورزی: قیمت‌های جدید اعلامی در سامانه مربوطه ثبت شده است.
🔹
مهلت اصلاح قیمت ثبت‌سفارش این کالاها نیز از یک ماه به دو ماه افزایش یافت.
🔹
ملاک بررسی ارزش ثبت‌سفارش واردات برای مباشرین و شرکت‌های دولتی، تاریخ صدور کد مجوز موردی خواهد بود.
🔹
هدف از این تصمیم، تسهیل تأمین کالاهای اساسی و هماهنگی با نوسانات قیمت جهانی عنوان شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/akhbarefori/652400" target="_blank">📅 15:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652399">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
امام جمعه بجنورد: هر قدم عقب‌نشینی در برابر خواسته‌های دشمن مستکبر، قدم‌های بعدی را در پی دارد و باید تنگه احد زمان خود را حفظ کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/akhbarefori/652399" target="_blank">📅 14:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652398">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ترامپ: تحقیق درباره حمله به مدرسه {میناب) ایران ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/akhbarefori/652398" target="_blank">📅 14:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652397">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
ترامپ: به‌زودی درباره لغو تحریم‌ها علیه شرکت‌های چینی خریدار نفت ایران تصمیم‌گیری می‌کنم
🔹
ترامپ گفت ظرف چند روز آینده در مورد لغو تحریم‌ها علیه شرکت‌های نفتی چینی که نفت ایران را خریداری می‌کنند، تصمیم خواهم گرفت.
🔹
من از رئیس جمهور چین نخواستم که به ایران برای باز کردن تنگه هرمز فشار بیاورد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/652397" target="_blank">📅 14:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652396">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af5ce4b8cb.mp4?token=ie8cdS4GzbmbM53WrjzSscU7txse2eeVkpdlISfA3SekijW03G79gGczvrtggVyPjliWgc2oWimMDyvrXAfRa-d923GflhV2K9NNL-yr27esoiiFZJyET7OgoxccJF5vKgnx6skvzKK4-XmikOsZW46c3raECjA1JU1fMivafqOumiff-AxmBKSPeA3m_4F6t41TWNInu3knxptfDJmmMzwycDEPXcpBBT6Gen5rllmAwtFdee5iB4J2riu_vUve-tZpVg5Lu3aa2OcuKXzVYHggi5z8TOJib8q4MrDQiQ9Wn_iVEUYDiLZeN-fTeOzkCDFFdcxDWa360wzMZ-_DXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af5ce4b8cb.mp4?token=ie8cdS4GzbmbM53WrjzSscU7txse2eeVkpdlISfA3SekijW03G79gGczvrtggVyPjliWgc2oWimMDyvrXAfRa-d923GflhV2K9NNL-yr27esoiiFZJyET7OgoxccJF5vKgnx6skvzKK4-XmikOsZW46c3raECjA1JU1fMivafqOumiff-AxmBKSPeA3m_4F6t41TWNInu3knxptfDJmmMzwycDEPXcpBBT6Gen5rllmAwtFdee5iB4J2riu_vUve-tZpVg5Lu3aa2OcuKXzVYHggi5z8TOJib8q4MrDQiQ9Wn_iVEUYDiLZeN-fTeOzkCDFFdcxDWa360wzMZ-_DXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: همزمان با دیپلماسی، امکان جنگ هم وجود دارد. امیدوارم به دیپلماسی، فرصت داده شود هر چند برای جنگ تمام عیار هم آمادگی داریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/akhbarefori/652396" target="_blank">📅 14:34 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652395">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aynws7Bbz7Be73M0qATsB0rMnw0j8MtoWxxIk0X5hAIj1XcQRee4tYBELPjF-bqMxnfr_T-ENgzh6ul8VOq6_97v168zIwIXx79Fsm0V4uoJNuu_0_XS6VeKHRYYT4qcl2Fty3WRzO36MrpWZMajP-DtopNbw3qpfGk9_s-Qi_rmAecNuF1TlvkQG_h-cJXSW6UJCpDioDa8R8wCSDVADqmOGhhHxTkDBbhK47ewqr-dLc330RvKTBbBSfr9apPPBcBCm2k450_1qwsUUIZSo7pi_6hPMpNmXh9HGdL7VBAW5E7zQr2Zq58SQ8qzY1rRLyGnqyFUet9JHn-MAlnutg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: من هیچ مخالفتی با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال ندارم، اما این باید یک تعهد واقعی باشد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/akhbarefori/652395" target="_blank">📅 14:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652394">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad8617c6d.mp4?token=T-XZ-191VFupIWcARIIRO1lmW9Mc9UrPbqSwmjE4rbcLIxSJwat7KpLOiyEbQLUoKplNj4qNNNbZdVN2gUUjTB4ZWV05a5_Mbiido993XyD3AeSqtzu50SePl2-Otyb4173oWKaCtP3ymgnf9puE0mqvBIlgMw-Oo6Ll_yT6HFweQmN9MgCt05DWXH88yJdbgoZJKVJetSUNu8Gc25fLp8L62RkoVoZ07BNxnqf6vLwt3U8r7BVFgP3k2aHm5KvsQ8y65Iug-qbBLoWhzyHO7DzYduBUQLm7SiIiLMUsEdTqcJe_74Q1blgGIBkQo_XRIFONxMX3rsreXZGi23CNGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad8617c6d.mp4?token=T-XZ-191VFupIWcARIIRO1lmW9Mc9UrPbqSwmjE4rbcLIxSJwat7KpLOiyEbQLUoKplNj4qNNNbZdVN2gUUjTB4ZWV05a5_Mbiido993XyD3AeSqtzu50SePl2-Otyb4173oWKaCtP3ymgnf9puE0mqvBIlgMw-Oo6Ll_yT6HFweQmN9MgCt05DWXH88yJdbgoZJKVJetSUNu8Gc25fLp8L62RkoVoZ07BNxnqf6vLwt3U8r7BVFgP3k2aHm5KvsQ8y65Iug-qbBLoWhzyHO7DzYduBUQLm7SiIiLMUsEdTqcJe_74Q1blgGIBkQo_XRIFONxMX3rsreXZGi23CNGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: احتمال بازگشت به یک جنگ تمام‌عیار وجود دارد ولی ما هم برای جنگ و هم مذاکره آماده‌ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/akhbarefori/652394" target="_blank">📅 14:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652393">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d206e144.mp4?token=mUL1PhMsaxUqRTyr3GAaGAEoZENVYpqcssDDPcB4Dq4SfzV1DDhQqzZsnwo6EBPHak3SrdOwZVQV15i7aK1nzmnU12FoH6QKzfpotRdNJA0ePBFtNhbzsyq09ifiqVtASQxMe0comteptmxQAAKM9rzWNy6rdPeDXrXT48nfgke6E1AIBBqBr8oV2HoHVQFIVpVtxi1DEsfS4SD6_LN_lvXuQ2Lc_xOuZALj0a_2bB9couaScy38AuRDlK1DCfjXW6amaW8-Zs8UmCF6FdaAPXfbjyXQXlEmpQWnM2bqWHmHyl7c_wSb5pYs6_xbXgiZl3sKhvE-Ae5MmiGKyTyvIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d206e144.mp4?token=mUL1PhMsaxUqRTyr3GAaGAEoZENVYpqcssDDPcB4Dq4SfzV1DDhQqzZsnwo6EBPHak3SrdOwZVQV15i7aK1nzmnU12FoH6QKzfpotRdNJA0ePBFtNhbzsyq09ifiqVtASQxMe0comteptmxQAAKM9rzWNy6rdPeDXrXT48nfgke6E1AIBBqBr8oV2HoHVQFIVpVtxi1DEsfS4SD6_LN_lvXuQ2Lc_xOuZALj0a_2bB9couaScy38AuRDlK1DCfjXW6amaW8-Zs8UmCF6FdaAPXfbjyXQXlEmpQWnM2bqWHmHyl7c_wSb5pYs6_xbXgiZl3sKhvE-Ae5MmiGKyTyvIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: کشور هایی که به اسرائیل و آمریکا با اراضی خودشون با حریم هوایی خودشون کمک کردند باید پاسخگو و مسئول باشند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/akhbarefori/652393" target="_blank">📅 14:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652392">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
عراقچی: تنگهٔ هرمز در آب‌های سرزمینی ماست و مدیریت آن نیز با ما خواهد بود
🔹
تنگه در آب‌های سرزمینی ایران و عمان قرار دارد و میان آن آب‌های بین‌المللی وجود ندارد؛ بنابراین مدیریت این مسیر باید توسط ایران و عمان انجام شود.
🔹
اکنون نیز ۲ کشور درحال رایزنی هستند تا سازوکاری مناسب برای ادارهٔ آیندهٔ تنگهٔ هرمز و تضمین عبور امن همهٔ کشتی‌ها ایجاد شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/akhbarefori/652392" target="_blank">📅 14:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652391">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c515097104.mp4?token=IzIz5a_dqUtI0zZI4lR9EaOynZEZPSiwvKUy-yGKV9FuH-V8rkxJVtEba__jdwGpNe_xzJMleCiM8kJDVtGny1mJqyzJ0UYyEAxwdAWXn2Rww-ABMvT5BkFvyKeOBwmsvk6NRbmyJNsHKsjNeKM8Nt7Wm_NOOv6fY66nERw79ZyxT78Fp1dX-ti4cibX93WJcaxh7MXp3POUh1zR5Kpk0mSHUxbwm3y6o9VGii0-oHgnvhQf88oD0-KQzHyAtYw1_j6ZpDtnUOsi3k3W2IhYH0T4-btbuBn5qfwsHg6J9ZLmYpweqGEKnhBaWKja3XVA8hAQXksxaWDYU8nSEKRsIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c515097104.mp4?token=IzIz5a_dqUtI0zZI4lR9EaOynZEZPSiwvKUy-yGKV9FuH-V8rkxJVtEba__jdwGpNe_xzJMleCiM8kJDVtGny1mJqyzJ0UYyEAxwdAWXn2Rww-ABMvT5BkFvyKeOBwmsvk6NRbmyJNsHKsjNeKM8Nt7Wm_NOOv6fY66nERw79ZyxT78Fp1dX-ti4cibX93WJcaxh7MXp3POUh1zR5Kpk0mSHUxbwm3y6o9VGii0-oHgnvhQf88oD0-KQzHyAtYw1_j6ZpDtnUOsi3k3W2IhYH0T4-btbuBn5qfwsHg6J9ZLmYpweqGEKnhBaWKja3XVA8hAQXksxaWDYU8nSEKRsIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی:  خبر رد پیشنهاد ایران توسط آمریکا برای چند روز پیش هست/ پیام‌های از آمریکا گرفتیم که مایل به ادامه گفتگو و تعامل هستند
🔹
وزیر امورخارجه کشورمان در نشست خبری:
🔹
اینکه مطرح شده آمریکا پیشنهاد یا پاسخ ایران را رد کرده مربوط به چند روز پیش هست که آقای ترامپ توییت زد و گفت که غیر قابل قبول هست و ولی بعد از ما مجدد پیام‌هایی را از طرف آمریکایی‌ها گرفتیم که مایل به ادامه گفتگوها و ادامه تعامل هستند.
🔹
اینکه امروز چطوری دوباره این موضوع در رسانه‌ها برجسته شده، من اطلاع ندارم ولی قضیه مربوط به چند روز پیش هست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/akhbarefori/652391" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652390">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffeede06a6.mp4?token=aMYs94Ptl7VMpp7ym7y35cWzx8aUx4SiEpi82baBJzUuawN41JOVx2fRfj8U4U5QGYbjbDSuoRJgyOkrl64bFihJq459_79sx6IU0W0arwstUA3SAeiVCtg7OH4Dgg_hnKUtAXh3DUA-Wmd1w_EZmB5WTNFvdFMTcVbu_fSHKjLhMl6oegpn0KtNJqC4H92iuDElGI-uYSdCR6_xQRuALkyFZVeg0OwbCyc47u5LgxMMS_neRLnUTrMlI3MSvrGNK93MI_InUEEce2e2GIWeCNDjVrvvj9hw2RCKeMl0Z_vUY9uHId4ByIEmk-_C20oaf5jqENvAEdbTZuHuRoLFHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffeede06a6.mp4?token=aMYs94Ptl7VMpp7ym7y35cWzx8aUx4SiEpi82baBJzUuawN41JOVx2fRfj8U4U5QGYbjbDSuoRJgyOkrl64bFihJq459_79sx6IU0W0arwstUA3SAeiVCtg7OH4Dgg_hnKUtAXh3DUA-Wmd1w_EZmB5WTNFvdFMTcVbu_fSHKjLhMl6oegpn0KtNJqC4H92iuDElGI-uYSdCR6_xQRuALkyFZVeg0OwbCyc47u5LgxMMS_neRLnUTrMlI3MSvrGNK93MI_InUEEce2e2GIWeCNDjVrvvj9hw2RCKeMl0Z_vUY9uHId4ByIEmk-_C20oaf5jqENvAEdbTZuHuRoLFHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: به محض مطمئن شویم آمریکایی‌ها جدی بوده و آماده یک توافق عادلانه هستند، ما به مذاکرات برمی‌گردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/akhbarefori/652390" target="_blank">📅 14:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652389">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25be2c076c.mp4?token=rpUg6pO-hby6vvWvK9_drCOHVhtc6tczhnUEhPHo4MkOZ3_c3mCDmt4l74yf1BMWf0RrjE8hNEsewNfoKUHLONwSmyZgUx3P8Za90KGaI4jlB8y6ntnUdq0Mj2L0E3I8UGXD2P77Y9aJ8VK5hFy-Vgn35x6rgDC2qjm_TIXmc-t3yGfxVKBGbqTqkW8iOVFpXrAX0RY6j354GEA1ZbD8S3tpnSdeBboiS9GLVFu_b3qfl51axrWP_nyUvsffRtc6D0nawN_pETqq0TB8Xh2-I39bACHEYEd_RYvkDHygKm041ThL1M8I77mSdvwc0pU4O5j7caFw9HPAoPvbBXTf5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25be2c076c.mp4?token=rpUg6pO-hby6vvWvK9_drCOHVhtc6tczhnUEhPHo4MkOZ3_c3mCDmt4l74yf1BMWf0RrjE8hNEsewNfoKUHLONwSmyZgUx3P8Za90KGaI4jlB8y6ntnUdq0Mj2L0E3I8UGXD2P77Y9aJ8VK5hFy-Vgn35x6rgDC2qjm_TIXmc-t3yGfxVKBGbqTqkW8iOVFpXrAX0RY6j354GEA1ZbD8S3tpnSdeBboiS9GLVFu_b3qfl51axrWP_nyUvsffRtc6D0nawN_pETqq0TB8Xh2-I39bACHEYEd_RYvkDHygKm041ThL1M8I77mSdvwc0pU4O5j7caFw9HPAoPvbBXTf5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: تنگه هرمز باز است/ به جز کشتی‌های متعلق به متجاوزین، همه کشتی‌ها می‌توانند از تنگه عبور کنند
🔹
وزیر امورخارجه کشورمان در نشست خبری:
🔹
ما یک برنامه صلح آمیز هسته‌ای داریم و همیشه آماده بودیم تا اطمینان حاصل کنیم که این برنامه صلح آمیز هست و صلح آمیز باقی خواهد ماند.
🔹
ما آماده‌ایم به کسانی که شرایط ایران را قبول می کنند کمک کنیم تا عبور ایمنی از تنگه هرمز داشته باشند.
🔹
به محض اینکه تجاوزات پایان پیدا کند مطمئنم همه چیز به حالت عادی برمی‌گردد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/akhbarefori/652389" target="_blank">📅 13:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652388">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f74d2591b6.mp4?token=LjDkMs2bmcvW5FDs3bGyYtgjL0pqnzZiR7_6UmeLRBmK7_4coV6-pyviMCs1Jq3OrLY2P9vaBJkNDujvCF5N_SBe900M2Kx-Zi287IGgQ8M_TtaYKf87tQA4plK6PYQ4OsDcE-aG4P3KgDow8qh4m0Aih8NQt_5qmMWQl0hrJDAbqPebRtb-yPf0KHOzcJ31tXKYpzfL_qNzlM8kouYQTK4MP-H_zuJZAjG6JEgkS3hn4o6dQaXJBxc4R7_jyp48e7DRRj7dnpPeVZXDaOLII9lc8j7wcg1G-LWKGBCokBqKsanj92Vb4uUOl_FV-vEWZcIUyVx2heaMm30vV6BaIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f74d2591b6.mp4?token=LjDkMs2bmcvW5FDs3bGyYtgjL0pqnzZiR7_6UmeLRBmK7_4coV6-pyviMCs1Jq3OrLY2P9vaBJkNDujvCF5N_SBe900M2Kx-Zi287IGgQ8M_TtaYKf87tQA4plK6PYQ4OsDcE-aG4P3KgDow8qh4m0Aih8NQt_5qmMWQl0hrJDAbqPebRtb-yPf0KHOzcJ31tXKYpzfL_qNzlM8kouYQTK4MP-H_zuJZAjG6JEgkS3hn4o6dQaXJBxc4R7_jyp48e7DRRj7dnpPeVZXDaOLII9lc8j7wcg1G-LWKGBCokBqKsanj92Vb4uUOl_FV-vEWZcIUyVx2heaMm30vV6BaIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: هرگز به دنبال سلاح هسته‌ای نبودیم
🔹
وزیر امور خارجه: تنگه هرمز باز است جز برای دشمنان ما، هر کس می‌خواهد عبور کند باید با ما هماهنگ شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/akhbarefori/652388" target="_blank">📅 13:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652387">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLdU-rSwS9eRMh5BlYObJ_4apAEvSV5Z3L80Kb8miDwaPi2igo841oT1iWlBxR84LSjLrHsSY6AgBSeXE4R6n89HoBiTLxDNDUVrpzObk-foUi--X36kYiWO2CRtcTVpsffWp0t9U9ISO9BpUQd4Jy8drLB8CfBgKjtmBkHt1lVUhG3Y-HFOde7t-beAAoppGWQwVx6tc28aBgux0eTOAg12ZNzZtmPWnGNa_vQ7BD1ziY12vbU-9Ru6huVD_59Jf7uJ09_UHetYbaRNMcF2FZRJ0VS9nXh0_RizDs4KxERmM1UkGw4vSZXGchAj1VOXCCK_w4ruVqlMuFoWQliWXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکمیلی /
🔹
عراقچی درباره خروج اورانیوم از ایران به روسیه گفت: مذاکره خوبی با لاوروف داشتم. مشارکت راهبردی با روسیه داریم. با پوتین در روسیه دیدار کردم و در خصوص اورانیوم هم صحبت کردیم از پیشنهاد طرف روسی متشکریم این موضوعی بود که باید در حین مذاکرات به نتیجه می‌رسیم. موضوع غنی سازی ما پیچیده است و برای رسیدن به نتیجه با طرف آمریکایی پیشنهاد دادیم این بحث به تعویق بیفتد.
🔹
در حال حاضر این موضوع مورد بحث نیست.
🔹
نسبت به جدیت آمریکایی‌ها شک داریم. آماده توافق منصفانه و عادلانه هستیم.
🔹
رئیس دستگاه دیپلماسی در پاسخ به سؤالی مبنی بر اینکه آیا در زمان اجلاس سران بریکس امیدوارید به اختلافات با امارات پایان دهید؟ گفت: ما مشکلی با این کشورها نداریم. آنها هدف ما نبودند. پایگاه‌های آمریکا در این کشورها قرار دارد.
🔹
امیدوارم در اجلاس سران به فهم مشترک برسند. ما قرن‌ها با هم زندگی کردیم.
🔹
اماراتی ها باید متوجه این موضوع باشند. اگر به مسیر عقلانیت برگردند می‌توانند ایران را به عنوان دوست در نظر بگیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/akhbarefori/652387" target="_blank">📅 13:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652386">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5517ce1975.mp4?token=XFFaQGRTH_ikN1FgS9A5UGSK4zxlss-LdxrxroHqa-4SdzaIN6AzgDjmDPFrjeN-gCjBd6qqolssKsAtO0eJi2FlU75W7e6B5vh-3RgzpEho7hVDKmagm2gPqHITRkjruYDjCu6Yspe7W5AhPjjvrEEFY9tNX9cBa207NJuvwYWH2ooU2LDqPX6BcQNEgzJa9g-Yb1HpC7XhZXlsbRPCHVKvmw1Wmo75etxM4xDZ2HzNZ6xV8r8R3zgBYdhI_JcyU3K6TDIMvmwDBRCjW8iBrm3wwYGIwYUm8Q5s-9JKrk4scxuJDcqnpGY-PsCJ9P1zoyOMLE3qDMKNd72s6tbJUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5517ce1975.mp4?token=XFFaQGRTH_ikN1FgS9A5UGSK4zxlss-LdxrxroHqa-4SdzaIN6AzgDjmDPFrjeN-gCjBd6qqolssKsAtO0eJi2FlU75W7e6B5vh-3RgzpEho7hVDKmagm2gPqHITRkjruYDjCu6Yspe7W5AhPjjvrEEFY9tNX9cBa207NJuvwYWH2ooU2LDqPX6BcQNEgzJa9g-Yb1HpC7XhZXlsbRPCHVKvmw1Wmo75etxM4xDZ2HzNZ6xV8r8R3zgBYdhI_JcyU3K6TDIMvmwDBRCjW8iBrm3wwYGIwYUm8Q5s-9JKrk4scxuJDcqnpGY-PsCJ9P1zoyOMLE3qDMKNd72s6tbJUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر امور خارجه: پیام‌های متناقض آمریکا مشکل‌ساز است/ توییت امروز مقامات آمریکایی با توییت دیروزشان فرق دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/akhbarefori/652386" target="_blank">📅 13:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652385">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
تا دقایقی دیگر پیام حضرت آیت‌الله سیّدمجتبی خامنه‌ای رهبر انقلاب اسلامی به مناسبت ۲۵ اردیبهشت ماه، روز  پاسداشت زبان فارسی و بزرگداشت حکیم ابوالقاسم فردوسی منتشر خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/652385" target="_blank">📅 13:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652384">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/036c33f3d1.mp4?token=XYJtc2miu_toLs_VjcI-70gaYZMOSWUiw-zIRrjDT3Ltdw2lwYlm1lH_mDWKkdGsL2JUfWx51uBQKUogslUHHvXRE0pi0tdZeR5CM5XVs4OtkFtnBjapSh_08JO5LjsxYibnmItNacTYNmGrTnRM4MP8peP_-PoggTJ_aHpfuWC5Angycc1Ht-AZ3DkAwY7vh8RGTJW8_VtfQdZXzwtut9Hj9tJeqZ-SD8aNJJCF9n0ygRYRNZ0WW7d6YW4erBQvinttp5LWM605NKorjxtkRhNlI2hlAEMD3yb5A0Jy6lqZY8d2l1Oia8aOwxD-J_xyWxJdCkOwz0BWbe77TsY-IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/036c33f3d1.mp4?token=XYJtc2miu_toLs_VjcI-70gaYZMOSWUiw-zIRrjDT3Ltdw2lwYlm1lH_mDWKkdGsL2JUfWx51uBQKUogslUHHvXRE0pi0tdZeR5CM5XVs4OtkFtnBjapSh_08JO5LjsxYibnmItNacTYNmGrTnRM4MP8peP_-PoggTJ_aHpfuWC5Angycc1Ht-AZ3DkAwY7vh8RGTJW8_VtfQdZXzwtut9Hj9tJeqZ-SD8aNJJCF9n0ygRYRNZ0WW7d6YW4erBQvinttp5LWM605NKorjxtkRhNlI2hlAEMD3yb5A0Jy6lqZY8d2l1Oia8aOwxD-J_xyWxJdCkOwz0BWbe77TsY-IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: ما به هیچ وجه نمی‌تونیم به آمریکایی‌ها اعتماد کنیم برای همین قبل از توافق باید همه چیز مشخص و روشن شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/akhbarefori/652384" target="_blank">📅 13:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652383">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3abba85efb.mp4?token=epRJvUArw6OKBFFfjHtyaI0FN6nmGq6GvXchTo2kfkTSgjfHTXgJtWHGMsXOhYrESNa5G6_sDxDvkfFh5jWePoZ_SzHEf0Hh6vg8b__SaI2VJpry2qkRVztuYXySIR-r6DDhztWubgoo7xtEwn6GJXdBPMrVdVi1MNLnSq81ieUpWJ6v8uDRjpSQOxna-CtxJ5agmH7WM01XQOEv9FmDs6Qo_HeIMWZwD-zxTDsPS20SxLcnwanaW9LEWBbacFWgxuEuTk55eR4jdOyuvl9D13I2L-HBiWMTkveDiTPRivpaIs1gQEthMn6eb5V309DdNNVKRLao_L7Ph4CIL_PCEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3abba85efb.mp4?token=epRJvUArw6OKBFFfjHtyaI0FN6nmGq6GvXchTo2kfkTSgjfHTXgJtWHGMsXOhYrESNa5G6_sDxDvkfFh5jWePoZ_SzHEf0Hh6vg8b__SaI2VJpry2qkRVztuYXySIR-r6DDhztWubgoo7xtEwn6GJXdBPMrVdVi1MNLnSq81ieUpWJ6v8uDRjpSQOxna-CtxJ5agmH7WM01XQOEv9FmDs6Qo_HeIMWZwD-zxTDsPS20SxLcnwanaW9LEWBbacFWgxuEuTk55eR4jdOyuvl9D13I2L-HBiWMTkveDiTPRivpaIs1gQEthMn6eb5V309DdNNVKRLao_L7Ph4CIL_PCEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: ما در آتش‌بس هستیم اگرچه بسیار ناپایدار است؛ اما در تلاشیم تا آن را حفظ کنیم تا به دیپلماسی فرصتی مجدد بدهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/akhbarefori/652383" target="_blank">📅 13:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652382">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_IIAtcBVB2d6WRQ3qlzRYd7oE9WJ98QJ8UGchRiY4jQbLHre6ZIR3Lldg9Nj0Z1V9SlnfZTuLezVSbfgTNhsuOdxwW_Yoc0BD3zWMSOg2Eyr5e25HCIjcYNNrqIjv3u28ckHS4rm9UNire38y3DesJCd43GBP_V-VY_0eVco9Iatb1-fAdK0Qn5L2qBYqQlnhZqXD9_ExVKP_j-CbxmW2Mdxuub0lSl_rTdQvQAEq2Y-cJDHXE-h868yhVwrgVqVTdUizOBOkmDGMJ0QJmm8gY-0zE6Pzf19EjhbyX8BtAD6mQgzdV4WbYE-eKV4ea--MoLpqi_NOKD2TiThXqPMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اژه‌ای: امروز آزمونی دیگر در راه است، مبرم‌ترین نیاز در شرایط فعلی، اصلاح الگوی مصرف است
🔹
رئیس قوه‌قضاییه در فضای مجازی نوشت:
🔹
مردم گرانقدر ما بیش از ۲ ماه است که میدان را تسخیر کرده‌اند و حمیّت و غیرت خود را در ولایتمداری و میهن‌دوستی به رخ جهانیان کشیده‌اند؛ هزاران آفرین و مرحبا به این ملت سلحشور و وفادار.
🔹
صرفه‌جویی ملت در منابع حیاتی، مصداق مشارکت ملی و حضور مؤثرتر مردم در میدان است. قطعاً ملت ایران نیز از این آزمون سربلند بیرون خواهد شد.
🔹
در این نهضت ملی صرفه‌جویی و اصلاح الگوی مصرف که روی دیگر جهاد مقدس ملت ایران است، مسئولین و نخبگان باید پیش‌قدم باشند؛ مسئولین با اتخاذ تدابیر و تمهیداتی که مصرف بهینه‌ انرژی را مقدور سازد و نخبگان با ارائه طرح‌های مبتکرانه و خلاقانه در راستای تحقق مصرف بهینه‌.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/akhbarefori/652382" target="_blank">📅 13:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652381">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZGwWq49As_WLfCAYQkXjfQiMXb-hpPQwOEOMDfiQr4i3BfPkUTQCcvS-sm--PszCBBQOWitN-RcsOjgI1aOi_FgXI3Ncyqkb0fY5sb8r8kqVq7i3r8Kcc6bHiuYgMidYSaRhNAgvxZPkL_7GDAV5J_-MYwk21aX7dHALSFBU23bNz1oBr6aK2Iz6v55fwZXxyjzEPrasVSuZtZPXMLlY5FiA7kEP_9TBYjNpCzNhc_feV4DLoun5LQ-gcPu2KPSvjSlLq_p-x7WWl9WB7rZO2dngdckrIwbmZHwxnZxoZOSpkSGWb4Pz6SucLznyvafGd07twZwjMONNsLC27xvFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهم‌ترین نیاز امروز و فردای کشور تحکیم پیوند ملت، دولت و حاکمیت است
حجت‌الاسلام و المسلمین ابوترابی در خطبه‌‌های نمازجمعه تهران:
🔹
جنگ فقط میدان احساس نیست میدان تشخیص هم هست، در دوران جنگ جامعه‌ای عقلانی است که به استحکام دورنی قدرت و تحکیم پیوندهای ملی، دینی و افزایش سرمایه اجتماعی می‌اندیشد
🔹
آنچه در این نبرد مورد تجاوز قرار گرفت بخشی از حافظه تاریخی و تداوم تمدنی ایران بود، آمریکا خواست امروز ایران را محو کند ناخواسته دیروز بلند ایران را به یاد جهان آورد، این روزها ایران فقط در میدان نبرد و دیپلماسی اقتدار خود را به نمایش نگذارد، در میدان زندگی هم ایستاد و حکمرانی جوشیده از درون ملت را عینیت بخشید
🔹
مهم‌ترین نیاز امروز و فردای کشور تحکیم پیوند ملت، دولت و حاکمیت است ، تحلیل‌های سیاسی باید بر پایه عقلانیت، دانش، گزاره‌ها و داده‌های صحیح ارائه گردد، ارائه تحلیل‌های نادرست مبتنی بر داده‌های غلط و تحریف شده زمینه‌ساز تخریب سرمایه اجتماعی و فرسایش اعتماد عمومی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/akhbarefori/652381" target="_blank">📅 13:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652380">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آمریکا بازهم دبه کرد و پیشنهاد ۱۴ ماده‌ای ایران را نپذیرفت
طبق اطلاعات رسیده به تهران تایمز، دولت آمریکا پاسخ پیشنهاد مکتوب ایران درباره شروط پایان جنگ را داده است.
آمریکا با رد پیشنهادات تهران، بار دیگر مواضع باج‌خواهانه خود در موضوعات مختلف بخصوص در بحث هسته‌ای را تکرار کرده است.
گفتنی است ایران پیشنهاد خود را مبتنی بر مذاکرات دو مرحله ای ارائه کرده بود که در مرحله اول منجر به پایان جنگ و انجام پنج اقدام اعتمادساز از طرف آمریکا می شد این شروط شامل برداشتن تمام تحریم‌ها، پرداخت پولهای بلوکه شده، پرداخت خسارت‌های جنگ و غرامت، به رسمیت شناختن حاکمیت ایران بر تنگه هرمز  و پایان جنگ در همه جبهه‌ها از طرف امریکا می شد و در صورت تحقق شروط ایران، مرحله دوم مذاکرات با موضوعات دیگر طراحی می شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/akhbarefori/652380" target="_blank">📅 13:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652379">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3FRjqpeccCUdR4sA1_OZjUOapOwVQ2cj-cAl9viW2YEFWe_xvfbBV71OxbNtFstpXRTXZNKGwTci018BBUGEInULTW0ZjcK4YPPCPKTwnc1BchzZ73qZFfB24RR7PuYCYzhLmByG-fcjfzoIcIG9FrHDkzgjOQ4wzrgaiygrD5FFR4N7qnHS0WK225El90I4ruxHwaeYQTIri7Fkqi-vvJn5CP92i3N1DM9mjvvo4jyz2lBuH8s5m8uF6YGGf--mKX386m5_WVAZGb_tNIG8bF4Ldokpi2q8-z47luW4jKage9HlJ_b1BGt-KIQmTHeUUJLvsvmJ3vbsiVGB-iwjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حماس: هرگونه صحبت از خلع سلاح مقاومت همسویی با اهداف دشمن است
🔹
جنبش مقاومت اسلامی فلسطین (حماس) اعلام کرد: هرگونه صحبت از خلع سلاح مقاومت در حالی که اشغالگری و جنایات آن ادامه دارد، همسویی با اهداف دشمن در تحکیم تجاوزگری تلقی می‌شود.
🔹
جنبش حماس تأکید کرد که «مقاومت با تمامی مظاهر آن، حقی طبیعی و مشروع است که پیمان‌ها، قوانین بین‌المللی و آموزه‌های الهی برای ملت‌های تحت اشغال تضمین کرده‌اند.»
🔹
این جنبش عنوان داشت که «اشغالگری، هر چقدر هم که طولانی شود و فداکاری‌ها هرچه باشد، هیچ مشروعیت یا حاکمیتی بر سرزمین فلسطین ایجاد نمی‌کند.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/akhbarefori/652379" target="_blank">📅 13:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652378">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcr_lgrp0M3nZyVaqFbr65-Ikvy3rBT5zu-FakRgkhTEFCb3yu6Hm0c5sSyT9TJWQ2leRdW6a9Cerx7K50_JZsmcpn7KNMakTozfH1hqt1IITKVU5zRURojaxjX2b6D5Sc-b6pTY9tyPkKKI8HJJGYq9C2BbPz9Las30r3dgh7LLVC2NcnOD7ZeaK7O1Htbfq5AkaamckuB6EyXrl17e2KjfMs6r4-JjgTHs2-zVvAgjlL90m6mKeGMjns_aV8-kUG76fWMXHL6Wwx41EDd0jFcJ2_yLX1feEWGYMjOJ_MG7PzWcWnrh6tLIn2lXkVgTCITJGiy4otQUDwRMxIYRQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش تند قطر به یورش وزیر صهیونیست به مسجد الاقصی
🔹
قطر با اشاره به یورش وزیر صهیونیست به مسجدالاقصی اعلام کرد: این اقدام، نقض آشکار قوانین بین‌المللی، تحریک احساسات مسلمانان و تلاشی خطرناک برای تحمیل واقعیتی جدید در قدس اشغالی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/akhbarefori/652378" target="_blank">📅 13:16 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
