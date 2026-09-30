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
<img src="https://cdn4.telesco.pe/file/IKvTy8_gV2jvj-MFsmrDB6mECCFRgRIE9HzaI0pRgMjrbH2CV2OnCXQ__nLY9_ta02gKzK45DaTXIUCJMdV69eNORqkAeVG79idMQNN0wka40G81JJ6sGRSnhaDlSkp_zCkDP8OkYRsHs6osXiQ_DHqFQ6mN4HQ_ZlPwA2gN9_ujzcw1z0-MShmXnVjUs6cRbTW6mRxUVJNnilHzLU51XLmu17YCjtiX0b_hR9EE_KxkD0c-CTENUtGaVuz4WQ_FouXMTtzUe6EE5fdsHT2R0yimXC9fI3W5JIyh2V52ONwk9v3YNNKaEca50k9SplocstD2CP5vgYSezPJmv87Fmg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.02M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 19:40:29</div>
<hr>

<div class="tg-post" id="msg-150256">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vXoQRFRuzsqh2G72vF00bC16h_eYa25p_YU-RXKSIbi_za39Q62YrSXCpMS0G0erI3S8lCjLy9Ds2ZpmGTcNQWn0zwUpf1DxmhsCsIPsKj1_o9Xf4C-9RUCSnL7vnVLxwAm_sDXMP9PjU_UTygRyd7nd0Rps1HelGiIsB4GQUiHdn8Xce9ZihPIMU30g56mbu9gzmjP3KYI7BLNxeWbh6tNKn442QXSb-EIJ8fr5T5JAaHT_dve8W1yu_O6x622Z3Cbg7_wldcV7zpFF1ysF5fO-bpqjrA-V6wKivTus9493SATs3a5TwZ51kFgdHVKkzNGv_Ii7eK2EDsXeJLUREA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nyXL2OI_YUePC6z83D4JlFAkjYsExD7mL4CZ_uNg0kE0aFy7vioTfHPZDr70UsHQGtsBeBdq46QV-BK77z8gJlPJohbtf2ReCmOrZMqiTzqt8KKkwUQkoGbrR7jPNSYTmiEqCRYvNrkNofUVIYUFVTeXCf_5KFmO4vOD_zsV821GjO9P6KF_zZYNjCkkcEMHhkK-A_OFmDrqgyKVqwvcfXsMNJ7Wg2rf_x17tiostvCQ2w42qKdoqSTQhiWH41UuRcNirAQFC_SaJfTriXM53brUj81-EBI37LgRI1ubDWbRS7zo-AOYtxDnVCjuCTwzDDj3BYhd_jdEv46PmaYWjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e068cf4205.mp4?token=Uo5s81K4tynhkU67xyeUfl74PF4vSiOR9RsslhNenOVg7a9EFW6hry90ZzWKjM5xpiHwmXeJH0NHsM8pD_EAuiaOhzNiT7fymtqxmCy20lbbPM4OtsecFQ8TYkqA9VAlMG4pfIcN7wYg8vPGFVduLtfDkO78DJAbfiSW6u1Vx9YgtQaAbH1pY1J8kdVtcvgyYtitWpZ9e3FxfNGYVk0FAErLC8tIjIJgjErjdzwZW8cKLAZpNqoYYdfoebSdbWeYbimE9uPvF0I8-3O8IX6shEMenFfXua7Ql8g8vwVRAYip0RBBV_TmdhsLYMT5XstWSbilZ7oskxltnKq4BJHqIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e068cf4205.mp4?token=Uo5s81K4tynhkU67xyeUfl74PF4vSiOR9RsslhNenOVg7a9EFW6hry90ZzWKjM5xpiHwmXeJH0NHsM8pD_EAuiaOhzNiT7fymtqxmCy20lbbPM4OtsecFQ8TYkqA9VAlMG4pfIcN7wYg8vPGFVduLtfDkO78DJAbfiSW6u1Vx9YgtQaAbH1pY1J8kdVtcvgyYtitWpZ9e3FxfNGYVk0FAErLC8tIjIJgjErjdzwZW8cKLAZpNqoYYdfoebSdbWeYbimE9uPvF0I8-3O8IX6shEMenFfXua7Ql8g8vwVRAYip0RBBV_TmdhsLYMT5XstWSbilZ7oskxltnKq4BJHqIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مسافران پرواز FZ1073 شرکت هواپیمایی فلاي‌دبي، پس از انتقال از فرودگاه طبوق در عربستان سعودی توسط یک فروند دیگر از هواپیماهای این شرکت، به فرودگاه بن گوریون رسیدند
🔴
جت‌های جنگنده F-15 نیروی هوایی اسرائیل، این هواپیما را پس از ورود به حریم هوایی اسرائیل اسکورت کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/alonews/150256" target="_blank">📅 19:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150255">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
فووووری
🔴
طبق اعلام بانک مرکزی اعطای وام برای خرید طلا، ارز و رمزارز ممنوع است و این ممنوعیت شامل تسهیلات مستقیم و غیرمستقیم بانک‌ها و واحدهای دیجیتال نیز می‌شود.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/alonews/150255" target="_blank">📅 19:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150254">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
منابع عربی: ایالات متحده دوباره شروع به انتقال هواپیماهای نظامی از قطر کرده است. تعداد هواپیماها نسبت به ۱۰ روز پیش، ۱۰ فروند کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/150254" target="_blank">📅 19:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150251">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddd1e8f01a.mp4?token=WNtiWGqJX9bqczfX9JCxPU8qvNaPE30Da-L1KQQ-RYRYnjVq6NTwbQvN_gxg_TiUMHhOGziuDPxax0IoMjCHLrUcRppm0bBV0e13H1UAnelqy344I_P6e3TIISJgxWsTG8VSl7ulWqOHfrx7P1W2WjbvwVJIcnShDLAj_Pl2gzK0rF1EgEjRqnF_Kj_DnLkcsPWqTQAhf8tUjmFC1_giR8c9VZMcnEpT8W3jxmg3INjCqU50O7JNs6SxrY2i-RWWZLMBDZQYH7UZUoEe2KESYGeyurPyKwnty74RdK_V15j7eLBZJy6KrDL3LAfFC8GWKzvaknqyq8gqkNb-GJmU7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddd1e8f01a.mp4?token=WNtiWGqJX9bqczfX9JCxPU8qvNaPE30Da-L1KQQ-RYRYnjVq6NTwbQvN_gxg_TiUMHhOGziuDPxax0IoMjCHLrUcRppm0bBV0e13H1UAnelqy344I_P6e3TIISJgxWsTG8VSl7ulWqOHfrx7P1W2WjbvwVJIcnShDLAj_Pl2gzK0rF1EgEjRqnF_Kj_DnLkcsPWqTQAhf8tUjmFC1_giR8c9VZMcnEpT8W3jxmg3INjCqU50O7JNs6SxrY2i-RWWZLMBDZQYH7UZUoEe2KESYGeyurPyKwnty74RdK_V15j7eLBZJy6KrDL3LAfFC8GWKzvaknqyq8gqkNb-GJmU7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی‌های مداوم در تأسیسات نفتی بقیق در عربستان سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/150251" target="_blank">📅 19:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150250">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
وام برای خرید طلا و دلار ممنوع شد!  بانک مرکزی:  اعطای وام برای خرید طلا، ارز و رمزارز ممنوع است و این ممنوعیت شامل تسهیلات مستقیم و غیرمستقیم بانک‌ها و واحدهای دیجیتال نیز می‌شود.  بانک‌ها باید متقاضیان وام را اعتبارسنجی کنند و منابع بانکی را بیشتر به بنگاه‌های…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/150250" target="_blank">📅 19:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150249">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
وام برای خرید طلا و دلار ممنوع شد
!
بانک مرکزی:
اعطای وام برای خرید طلا، ارز و رمزارز ممنوع است و این ممنوعیت شامل تسهیلات مستقیم و غیرمستقیم بانک‌ها و واحدهای دیجیتال نیز می‌شود.
بانک‌ها باید متقاضیان وام را اعتبارسنجی کنند و منابع بانکی را بیشتر به بنگاه‌های اقتصادی مولد اختصاص دهند و بر نحوه مصرف وام نظارت داشته باشند.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/150249" target="_blank">📅 19:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150248">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نامه بانک مرکزی به تمام صرافی های دیجیتال : هر کاربر فقط روزانه اجازه خرید ۲۰۰۰ تتر را دارد
🔴
تسنیم: صرافی های رمز ارز معاملات تتر را از ساعت ۲۱ هر شب تا ۹ صبح روز بعد متوقف کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/150248" target="_blank">📅 19:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150247">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
خبرنگار الجزیره: در مذاکرات، هیچ‌کس به‌طور صریح «نه» نمی‌گوید، بلکه بیشتر با ارائه اصلاحات و پیشنهادهای جدید پاسخ می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/150247" target="_blank">📅 19:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150246">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIcbXC05g22HOmz7jDBkQpvqsMpHagdehgeoIDpvBbgHDh6PHRykmAN1pZhula4FXmc8cjpZZMshw99qWBLDyzS-hDzenxO-CS2b2OTG-m0McISkiaVnrcfAHNM0210gtOAfWWZnjrJ8QvYAWvx9VHTzO2NVmuH6BiI_swqDeJ2iNsiNZHzWpqlBpcFIpwCrftmd7YXTKgRWBX8CpriyQ7k4OqHlyJ6uD9RrgnkgCmfamPPho8zazNI97oPvRZfmHofM3ZOoUbImjYh-rZhM8ATKiMA1tEloBUF-z8mAJcB4eeui8YD6pNn8-T3qkuku3CpqMSOe2aLJiuINhkGt1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: ایران اکنون در موقعیت ممتازی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/150246" target="_blank">📅 19:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150245">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
معاملات شبانه تتر متوقف شد
🔸
صرافی های رمز ارز معاملات تتر را از ساعت ۲۱ هر شب تا ۹ صبح روز بعد متوقف کردند
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/150245" target="_blank">📅 19:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150244">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
استاد خوش چشم: جنگ قطعی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/150244" target="_blank">📅 18:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150243">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPDVnxYHpeBYactP_hdd3SqkroFxI6TbjkWt3H1iVLRcTa4Hy_midvCxB_PgOTlwg6C78XWJbkPGm85JisrPPIM0IRYe4DNlcsFuM35wf74eKTka0XUvOyn1XtrhKc_74HREfgAXMn6XLw49UgsjKga0An_H1gzQlU2z_lmQWFm_F6tlALYEzVAX47MImgGFsxH1cf5TekHAsElHL-bxiPczzn_rx_Q6gcZu6jcV1gcvN3R4OPFizg9N_YGwGN62Du5JLdBee7JzZ5JEMUIMtbBYCSl05UbJ1QENHZvlfYejKK0I37K8w0BATD8DTXPqRNX94_6yPw7UdDdiLwhjzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ماچ و بوسه پزشکیان و کروبی در‌ مراسم ختم احمد ناطق نوری
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/150243" target="_blank">📅 18:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150242">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10869c87f.mp4?token=DK06qydIGnPnH0xGPT_gCe_RleuIbpdIZAjFdNwhq6Ym3xJqAkNFscUw5YkfzlICo7HAxwGt33u5Wk1ibeIdAL222Sf1373ydoiLv_DiBpim4zgGlae20Bn9bF-TbbsAa2UTtp8R0fTXgdUFaRpqE71RNfXPdoHFyC4zjTfBMsYpBP9Y7Zs6Imn6ZuVTOln_Q56vmBV_Tkf_DiWOenN-iDUi7WYwWLB3hdN2nkeD_4KLmYQeu94Iqv5oe5Xf5xBsbY1x94MJXQj9_Gxz12h5_bVJ5i_e7Wr6jzBhetrOzFPZoEvUA5DOIm2I7RTI8Ur975XI3j7p2iRfcAl0SceTZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10869c87f.mp4?token=DK06qydIGnPnH0xGPT_gCe_RleuIbpdIZAjFdNwhq6Ym3xJqAkNFscUw5YkfzlICo7HAxwGt33u5Wk1ibeIdAL222Sf1373ydoiLv_DiBpim4zgGlae20Bn9bF-TbbsAa2UTtp8R0fTXgdUFaRpqE71RNfXPdoHFyC4zjTfBMsYpBP9Y7Zs6Imn6ZuVTOln_Q56vmBV_Tkf_DiWOenN-iDUi7WYwWLB3hdN2nkeD_4KLmYQeu94Iqv5oe5Xf5xBsbY1x94MJXQj9_Gxz12h5_bVJ5i_e7Wr6jzBhetrOzFPZoEvUA5DOIm2I7RTI8Ur975XI3j7p2iRfcAl0SceTZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارسالی مخاطبان از شلیک موشک در فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/150242" target="_blank">📅 18:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150241">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری/شلیک موشک از فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/150241" target="_blank">📅 18:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150240">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فوری/شلیک موشک از فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/150240" target="_blank">📅 18:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150239">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
الجزیره: آمریکا احتمالا پیشنهاد ترتیب‌بندی جدید برای توافق با ایران ارائه کرده است.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/150239" target="_blank">📅 18:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150238">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60bd09c687.mp4?token=CnKg3Ay7X2Mg7DpsokLE6uz1oAHbGDMIjEA2ZE5aQRavB38MfTNGjo2V2f7DhxBSuIOeGzuKgk6Fai5DVQI0hlunshS0s5j_G-YKTC_wXOCnial9bgaUBHQzUIpp1JnWUXn3sPCSIXjHQWkXHTK2HrXi-h2OmdPYYK3B2PYaA3Gj7KgSZxLSOWRGM1xTxmZxl5mwyuUI9CrAkq-9U-dLL1Zf3_nONAKzpW1uyPyyx5A0MArHH1wsKJivLluVtyG69FHfmMjbcnr1q9V6epbw5IjjkBVBC4B-BPwwi5JLaLzvZr-1oDAvAxGqDxny4b0kWb2q9BJNn91uC7HUp61Pww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60bd09c687.mp4?token=CnKg3Ay7X2Mg7DpsokLE6uz1oAHbGDMIjEA2ZE5aQRavB38MfTNGjo2V2f7DhxBSuIOeGzuKgk6Fai5DVQI0hlunshS0s5j_G-YKTC_wXOCnial9bgaUBHQzUIpp1JnWUXn3sPCSIXjHQWkXHTK2HrXi-h2OmdPYYK3B2PYaA3Gj7KgSZxLSOWRGM1xTxmZxl5mwyuUI9CrAkq-9U-dLL1Zf3_nONAKzpW1uyPyyx5A0MArHH1wsKJivLluVtyG69FHfmMjbcnr1q9V6epbw5IjjkBVBC4B-BPwwi5JLaLzvZr-1oDAvAxGqDxny4b0kWb2q9BJNn91uC7HUp61Pww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عبدالحمید: به تخت جمشید رفتم آنجا محل سکونت ظالمان بود به همراهانم گفتم زود برگردیم
🔴
جوابتون چیه بهش؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/150238" target="_blank">📅 18:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150237">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا از هدف قرار گرفتن چند کشتی در هرمز خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/150237" target="_blank">📅 18:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150235">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9kt5HTylAhggY3MBFxUXOc0syg1Gaybx2Q4yTRj6jdbvRgeQcMEx08E_vaGnBfAvjqrhz5w1kUEANCadeiG4_n-_mlK9AELKVNja7EiazhLFWuMxwnH6ohLX3t1ivKIRRP4gfY7d7BPVr_uTrSHoRyUdmMVkqSZJ83U5Pw-HduOVaFDvCvV0lt7fhsdKCrihcpls6pRi4pUa-o_wkEhyRJeFidMILWDAjqPPwmg7G9OekvYz2xzfvW5VuaDv1Qe6qA5CCuTbHN39bkS8VKT_xlVhs-ZFDE5cgjGvrKv388TASWg6KClzdmQ9wuw4daVWRULsadG_vx-YDv38KiZvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واشنگتن‌پست:
نیروهای نظامی آمریکا از پایگاه‌های خود در عراق خارج شدند. این خروج پس از دو دهه حضور آمریکا در این کشور صورت گرفت که به مرگ صدها هزار غیرنظامی عراقی و هزاران سرباز آمریکایی منجر شده بود و اکنون ایران آسیب‌دیده اما با نفوذ رو به افزایش را در مرکز آینده منطقه قرار داده است.
🔴
نیروهای آمریکایی عملیات ضدداعش را از مقرهای خود در اردن ادامه خواهند داد. این خروج که روز چهارشنبه ۳۰ سپتامبر ۲۰۲۶ تکمیل شد، پایان ماموریت ۱۲ساله ائتلاف به رهبری آمریکا علیه داعش را رقم زد. آخرین نیروها از پایگاه هوایی اربیل در منطقه کردنشین شمال عراق خارج شدند.
🔴
این توافق در سال ۲۰۲۴ در دوران بایدن امضا و در دولت ترامپ اجرا شد. نخست‌وزیر عراق، علی الزیدی، آن را آغاز فاز جدید حاکمیت ملی توصیف کرد. ایران و گروه‌های وابسته آن این خروج را پیروزی دانستند، در حالی که برخی کارشناسان نسبت به افزایش نفوذ ایران و احتمال احیای داعش هشدار داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/150235" target="_blank">📅 18:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150233">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0d82bb00.mp4?token=M_jVW3cCCnchuk47pL4MMYlj87v8AzQCay-Bp3IDD8jpv7jWrpZwCJRzCjhotPfYHWqH5jrfwExmTeHeSu2xiO41_alxUrNaPTFsvXwNFtLy7g5AyoHzLZdsUlEe48ffyTcjMeSwrA2Pzr23D1BVZxgFQGbOdrKzS2srP6fHzSsCD2Xgke9ilR73jGYH5NheloCehHqqpt7oobOGWWIpR-vNDLTz7ZCZ8fuuMNtEHagv5yvHXTA-yJ8AWxBWsPNEIS9r5EDKJKtdM7ff11MrxwlkLW-G0zdr7C3aqzN6rUofFof8YE06vC3PleKK7NmzId-l8GhpBlShiXHlVTmjmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0d82bb00.mp4?token=M_jVW3cCCnchuk47pL4MMYlj87v8AzQCay-Bp3IDD8jpv7jWrpZwCJRzCjhotPfYHWqH5jrfwExmTeHeSu2xiO41_alxUrNaPTFsvXwNFtLy7g5AyoHzLZdsUlEe48ffyTcjMeSwrA2Pzr23D1BVZxgFQGbOdrKzS2srP6fHzSsCD2Xgke9ilR73jGYH5NheloCehHqqpt7oobOGWWIpR-vNDLTz7ZCZ8fuuMNtEHagv5yvHXTA-yJ8AWxBWsPNEIS9r5EDKJKtdM7ff11MrxwlkLW-G0zdr7C3aqzN6rUofFof8YE06vC3PleKK7NmzId-l8GhpBlShiXHlVTmjmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فواد ایزدی تحلیلگر صداوسیما:
دفعه قبل ترامپ اجازه داد تیم جمهوری اسلامی از پاکستان برگرده بعدش محاصره دریایی رو شروع کرد
اما ایندفعه قبل از اینکه تیم جمهوری اسلامی از نیویورک برگرده محاصره هوایی رو شروع کرده و اصلا ترامپ دنبال توافق نیست بلکه میخواد حکومت رو سرنگون کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/150233" target="_blank">📅 17:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150232">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AuV8-7l5GOMHlH6wfXmeJNjY8h-fU6gS2-Vvg1tVqzxVemiHBRzcj6rnWDGYGBYyI1O9mjyElclIRZTP96ji89w7bSZDTtKJeuitjVcKCC6mFCMdEAqMjxRivunbGP3JWnX71DMnaO9h6f2ICOvlwj_3yDL3WG5LCUyY2bt2BUCaydktBUDu0LY1PJtfmt62uZPkC2jGjw0dAj9aiIh_2Jki9zT8ViY2PxVzWJziCWZmrUBuTA-RNtRNCGksf0k7tQV2yO7ccIk1GPOeUS92I7wCpqX7d1KgxGzPR07n5faX3pZr69xDWCo_U5dbXxqF5yCmTcrlyoDfNrHy0wzMWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قتلی که گلستان رو توی شوک فرو برده!
🔴
تیر ماه امسال یه پسر ۱۷ ساله یه نفرو به قتل می‌رسونه و بازداشت میشه.
🔴
پدر، مادر و داداش کوچیکش برای گرفتن رضایت میرن خونه خونواده مقتول.
🔴
اما اونجا یکی از فامیلای مقتول، با اسلحه هر سه نفرشون رو به قتل می‌رسونه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/150232" target="_blank">📅 17:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150231">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYaVrFmaAHHHriNMxDtmtBJqUKP-9n5KN43fTEgmCZzsrxmTX5yjy_0a1FqjSid_Z6ydvtYUEZ0gyL0SpqEBABxkuiMVi6GTAViSVV4zWaVQfIc6wFh0dO99j3j1vPgia91QVvrmezFFkTrE_KYfuGyRQa_W2rVu8Es5xigwPUgN4UR8AFWBr00brdvqq0NtTPHVuZDohz9fda5FFXKBQhSLHngwGamTZ0V4O9HzS7_dUqrLtAK0L7hVEhdTGLGOkCw_BhDE6GtHa0nCenFi49GJh4AnmFbulM-KcdhPHREd3A0yQqdTjiw2yfk0kky1furbI1iP1R2Qc62GTkhpXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امجد طاها، خبرنگار معروف عرب:
به زودی برای مردم ایران اینترنت رایگان و بدون فیلتر وصل میشه و حکومت ایران هم نمیتونه دیگه قطع یا کنترلش کنه و بعد از اون طوفان میشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150231" target="_blank">📅 17:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150230">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو، در مورد "حادثه امنیتی بسیار جدی" که امروز صبح در پرواز شرکت هواپیمایی فلای‌دبی از دبی به تل‌آویو رخ داد، اظهار داشت:
در این حادثه، یکی از خلبان‌ها، خلبان دیگر را مورد حمله قرار داد و
"به نظر می‌رسد که قصد داشت هواپیما را با تمام مسافرانی که در آن حضور داشتند، سرنگون کند."
بی‌بی گفت که هواپیما دچار "چرخش" شد و شروع به "افت آزاد" کرد، قبل از اینکه یک مسافر و یکی از خدمه اسرائیلی وارد کابین خلبان شوند و با مهار کردن مهاجم، از خرابکاری او در سیستم‌های هواپیما جلوگیری کنند.
سپس، سایر اعضای خدمه وارد شدند و به "تثبیت" هواپیما کمک کردند.
نتانیاهو از افرادی که در این حادثه نقش داشتند، به عنوان "قهرمان" یاد کرد که "قدرت و شجاعت فوق‌العاده‌ای" از خود نشان دادند و گفتند که آنها "جان‌های بسیاری را نجات دادند و از یک فاجعه بزرگ جلوگیری کردند."
مهاجم، که مسئول این اقدام بود، پس از فرود هواپیما در فرودگاه طبوق دستگیر شد و توسط مقامات سعودی بازجویی می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/150230" target="_blank">📅 17:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150229">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDkDpjcJKy2b5QQK-zsvhdjAdRw0NbecJIlWcd1YoinYw1qJWwDy2-qqd-ZByNBVTCxJZhHPxm23xEWHq2MtyZWeJy9bkJ5ra3IesHo5mpm7NG5awEjFMoj8NkOHL5CvBv0t0dT8tiX5NKqp4kR8mjIpMkO4GiI8eVtgT5XuwnfceJ0ocpwd_7pRd-Izne__tsQNjRsVr28BSDnWYG8vv18xbkuOuxUCNoRV14KGkX9OuN7T8Ui0w07wlugYw0xViYJQ5OcO_tdW3aViu-jODiciFxtplk1dIGe4lS5rwnyAvrVAIVyXaaaz-PyVaiegIaxRu7X-smViIisbrzNl_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیژن مرتضوی: اومدم از خاک کشور دفاع کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/150229" target="_blank">📅 17:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150228">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
تصویری از حضور بیژن مرتضوی در ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/150228" target="_blank">📅 17:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150227">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pMiVN6ATjPWO9Ni2E0GYWtwtcpwjdDpj7V9MqoMIuuk8ZbDLVWgLUD7_NnomE4sjiQS1e7RPZ189ulD5mU3BMpZnPuzJ_PMkWa6WigPPz6-lGFO7LM77jQ7NDEElhxiSJAG1ivlcUJj5leuQ941j0JBfM_fZNFMjz6NgTZp_OR2bi1tDCmgZWAppEVNndVs8IBzyeUECSkuZvAGqN7CVZz9MoY8tLDXIRtKvNs_nqN8iz9vxD-kdkW7PjHRY1kWm09nFrmMe-IQnFm9vtw6KnP_yJEf53Psl0WlNK7-LLzBQMQ4Yia983KOtX4spVBod5zBRzxIW1YfKPaR26E6y1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
اسمارت واچ خارجی در دست فرمانده کل پدافند غیرعامل کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/150227" target="_blank">📅 17:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150226">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
دختری که پاشو میداد پسرها بخورن و فیلمش رو منتشر میکرد، بازداشت شد  مشاهده فیلم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/150226" target="_blank">📅 17:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150225">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLJNwAKqoIGrb88sKralfSBtgOLWLaZUeN8oGr485S4g00x5qMXd_mLvFiRlW_ZM07w9mbkmanFmgVGQMsfJBqetdxVp3OhgSotpQbcRxidQ8fWTdeqyy35fKyaaN49dhyov400o70XjFj6F-0nAP5Bdn5nAGHdSSM2rVljbPthzV9jdEozV7OTQPDWRpq342PN221DweH1R4dzWVuYzPhuLV0Sz4pPMa1F5IW5HwlapL9heJGDzL-WPYzWTFTlBaDCQtz3qeJC06t0_SlQXmweUeleTTMG6tCSsf7OvN8Ap-7-xRNfF3Oa1X6ShQaTX_WNPOEl7bX_XhszPJmtfPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از حضور بیژن مرتضوی در ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/150225" target="_blank">📅 16:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150224">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
لغو سفر نتانیاهو و کاتس به غزه در پی فرود اضطراری پرواز «فلای‌دبی»
🔴
بنا بر گزارش‌ها، سفر برنامه‌ ریزی‌ شده نخست‌وزیر، وزیر جنگ و رئیس ستاد ارتش اسرائیل به نوار غزه، در پی فرود اضطراری هواپیمای «فلای‌دبی» و احتمال امنیتی بودن آن لغو شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/150224" target="_blank">📅 16:51 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150223">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
نیویورک‌پست : ارتش آمریکا در حال استقرار لیزرهایی در تنگه هرمز برای از کار انداختن تجهیزات جنگی ایران است و به گفته وزارت جنگ آمریکا که اخیراً تأیید کرده، «پهپادها و موشک‌های کروز ورودی را با هزینه‌ای بسیار کمتر از استفاده از سلاح‌های جنبشی گران‌تر مانند موشک» از بین می‌برد.
🔴
پروژه آمریکا برای مهار قدرت لیزر ۵۰ سال در حال ساخت بوده! ارتش آمریکا ۵۰۰ میلیون دلار برای سلاح‌های لیزری «آماده جنگ» هزینه کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/150223" target="_blank">📅 16:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150222">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdziZ17PzDAzB57ijUPKVZWU9ZfxxyvWiaPZDRXPSY4_oDk2OB2p_4p16bQUI4buDkdcMYZTOJ9TDJeaJ-b78IP0VWtrAM8_CT4INeqVltuzjIlX125WazQcHWjGiaxjaJnBe_-WIz8evo9tma4nyBou8W2dJDUdqBShhltJ8bvT1JO8OowUOOmTSN4YL6_J0QyJwgQYIEHVUNWcf6I70YdTrZOzB0uiyfNKIPV9a6UDKQhumIQO4D2VdvgSloYD2zo0mwENwMHT0g_XzNH1rcf3aIshU7fnSFgx6YwSraLXBuQxWqVmTT0pnD-odgTbReJxf2t0oolUPHqgYLHUNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارزش هر همستر به 420 ریال ایران رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150222" target="_blank">📅 16:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150221">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
دقایقی پیش اخباری درباره حمله به شهر نفتی بقیق در عربستان سعودی منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/150221" target="_blank">📅 16:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150220">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rZLi68tzP4Gxie8rkM3mYKX_tHqRlrb_yJJo5vRH4jYsfNyZloV0ZVfG40KytarW-bHhpROZ3_8Jnynm3OBsROROnbdCTG87dfWFJtrrXTWdY83E7_MuTXb_9pB3CdXYxGbPEoizXGWcodBl_zRcj_khT4vNf8YFNPVT6UEWii_X5ROXoJbZGFqNuQmzZU2msB7rAJXig24Pb1-X8fbJZfZ_KeD-YS3UdZ-tCTqNJXnv-uCCJz-JcXeUHdGkcf_Ditejl9wpdF8W7uV_nMBq0w1cyD-RX19m5O88-ibxUrn9x0a2Ht52ar8D5TBY5LNdi-JxbdK1TeGioVhU1ZT70A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استفاده از رمز ۱۱۱۱ برای کارت‌های آزاد جایگاه‌های سوخت دیگر امکان‌پذیر نیست و متقاضیان برای استفاده از این کارت باید ابتدا از طریق کارت بانکی احراز هویت شوند و پس‌از دریافت رمز یک‌بارمصرف، می‌توانند از آن استفاده کنند
🔴
خانوارهای که هیچ‌یک از اعضای آن‌ها مالک‌خودرو نیستند، امکان استفاده از این کارت را ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/150220" target="_blank">📅 16:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150219">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
در صرافی های بین المللی 1 ریال ایران = 0.00 دلار  شت کوین ریال !
✅
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150219" target="_blank">📅 16:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150218">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKqVB8HUgHcfuLIJOkTn3aDLLpBoI3-uqbbhYpUBlzQEGGAhJAbqfDD68athzFb33jf0jPl3TYzM0AG8RUPAEVJsfsDjW6KtnemDKs0wU8_yJqrntUTRPBt_xS2pOQoRttXRl5mWOksmIBMDOs1amtrmlTaLaSC7_6ZdASHfpJAD1kCauKTJQGt0h9JrOgmB8VBl8-DtuFiFpdPivhivLyPaBfyG8BoTZoMaS7o8to4KQpfa4UNGAZumE2RVnfTczflJ32ADK_YjONCoGfM6qQtMCYtjgoxX7dq6R_Kk_XpHyfQDq4phwVWqtkt8F4Q-kId2fPzUEILr_nU6ZvxC9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیژن مرتضوی بعد اینکه چندروز پیش گفت نمیام ایران و شایعه نسازید، دقایقی پیش تو لایو اینستاگرام در فرودگاه امام خبر بازگشتش به ایران رو داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/150218" target="_blank">📅 16:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150217">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
عوستاد رائفی پور: نسل جوان شاهد افول سلطه آمریکا و فروپاشی اون خواهد بود.
👈
فروپاشی اسرائیل رو من هم با این سن‌وسال خواهم دید
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150217" target="_blank">📅 16:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150216">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bd4kHHEiAzL2asm4aCeDs_49oZdU2WYGEho9DVBhiZNORK6PLQ9uffLaZlRE6c01vke110FfO_NpWPEWPn6zHj-IWd9RiBHKhYrQJPmR9Ygbr-sBrKy_ZP1WuDtpz3vI0wfcGRZTXy6qywwTrsWBLW85xP-mlkfat7bGi-uGAe31PzlmJZfJ_Aay3e_eOw4K3ONwfkbBhB03KKPwBjSlsbPOLiky07iX-ld4N2KvgY89FQWr4jvZYbEyGUn9Du5PSk3Yp2M73sEz_hn8CF1-JbxKCa_f8WDsuy5YfM0e_mGZDdtJQq2dlhHAfZoUkqFpX_XFuCGY1KjBvQ00y2dNgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازار عجیب فروش کارت سوخت با قیمت ۱۳ میلیون
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150216" target="_blank">📅 15:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150215">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
عربستان سعودی از پذیرش یک پرواز تخلیه نظامی اسرائیلی (هواپیمای C-130 هرکولس متعلق به نیروهای دفاعی اسرائیل) و همچنین یک گزینه ارائه شده توسط شرکت هواپیمایی ال عال، برای انتقال مسافرانی که پس از حادثه شرکت هواپیمایی فلی‌دبی در فرودگاه طبوق به دام افتاده بودند، خودداری کرد.
🔴
به جای آن، انتظار می‌رود یک هواپیمای غیرنظامی دیگر متعلق به شرکت فلی‌دبی در طبوق فرود آید و مسافران را به تل‌آویو بازگرداند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150215" target="_blank">📅 15:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150214">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ائتلاف بین‌المللی در عراق: با توجه به خروج ما، دیگر هیچ توجیهی برای حضور گروه‌های مسلح در عراق وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150214" target="_blank">📅 15:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150213">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
دقایقی پیش صدای ۳ انفجار در حوالی کلانتری ۱۹ زاهدان گزارش می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150213" target="_blank">📅 15:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150212">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
همتی در توییتی خطاب به وزیر خزانه داری آمریکا: جوجه رو آخر پاییز میشمارند بچه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150212" target="_blank">📅 15:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150211">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
تایمز آف اسرائیل: مری ریگف، وزیر حمل‌ونقل اسرائیل، پس از حادثه صبح امروز در پرواز دبی به تل‌آویو، خواستار تعلیق تمام پروازهای فلی‌دبی به اسرائیل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150211" target="_blank">📅 15:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150210">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
رئیس پارلمان عراق: ایران کشتی‌های عراقی را از ممنوعیت کشتیرانی در تنگه هرمز مستثنی نکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150210" target="_blank">📅 15:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150209">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3REqAXxcg4t1C5GwQlw1VCg-qlNWUiHfLczeKdmc0O__ogbEv755ILDNn2t4inTijt_F1LOfLxQqiZcZiEcT0yyzhFNmvq9V_RBbOTtn9caOwb7NRRWwUPjtMdjM08jGsyjPG1C-PK2vmLc4GB-ZfIVqEfrNgyc297mPT4-YQN_o0HBpmW-GB7i9nKTvSd0vjdm9ig_hO7y7TVo6xJoaN-VMV7wU4tElaO2S9DjXcWwK8adCL5CJcxrikiL7xEIyzBsIW9wd8kdkFrGvFRbVrAUe5SYHGg6SDecCx7WeqYo9MFSji9qXML_7zNoXK0XgT9yO0VIirFO-xoUAkOrLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گارد ساحلی هند: ساعتی پیش یه کشتی باری ایرانی رو گرفتیم که توش 526 کیلوگرم ماده مخدر هروئین و مت آمفتامین(شیشه) توش بود و ارزشش بیش از 330 میلیون دلار بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/150209" target="_blank">📅 15:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150208">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjCMvSL_UxVgvBjdT6Ql0wTi4McLtUCVcSsKndv18syoLI_jo_PGUoXxkvEwV0_hJRVBl7zw0FFjA55eWuwKJlS44cYrgLzHej-iZWZ4MvxtA0VsSFP2mSQO5komYjNUdVLbncI3Pst3e1JpP_7KH4BtT_0RYEw4t7CWr-Bri2sgR2O48nN5GEeArEIaDGVPCk5xQhq-6KEEtlAdqj4ApYJFqEloECYKnBdcBLhwojqhDangVGOODAs6dNYYZ9t-MkNmv2wO6cPD3vjrAcSPPsdY9C25T7SkeuPTYxo8GvqdwoeKRMd9lg0Pn1yhctDzArCfTB0tqY1BCXfuAA19Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در صرافی های بین المللی 1 ریال ایران = 0.00 دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/150208" target="_blank">📅 15:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150207">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
رویترز به نقل از مقام ارشد سعودی:
برگزاری دیدار میان نتانیاهو و مقامات عربستانی در امارات، کذب است
🔴
یک مقام ارشد سعودی گزارش‌ها درباره برگزاری دیداری میان مقام‌های سعودی و اسرائیلی را تکذیب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150207" target="_blank">📅 15:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150206">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
خبرگزاری فارس: مدیریت بازار دلار تهران عملاً به وزیر خزانه‌داری آمریکا سپرده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150206" target="_blank">📅 14:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150205">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
خبرگزاری فارس گزارش می‌دهد که مقامات امنیتی ایران معتقدند اسرائیل در حال برنامه‌ریزی برای یک حمله تروریستی منطقه‌ای است که ممکن است هواپیماها یا فرودگاه‌ها را هدف قرار دهد و در این راستا، ایران را مقصر جلوه دهد تا با این کار، موج جدیدی از فشار بین‌المللی و "اتفاق نظر" علیه تهران ایجاد کند.
🔴
سازمان‌های اطلاعاتی ایران در حال حاضر بر جلوگیری از وقوع چنین سناریویی تمرکز دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/150205" target="_blank">📅 14:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150204">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا، به خبرگزاری Axios گفت که جی کلیتون، مدیر سازمان اطلاعات ملی، می‌تواند یکی از نامزدهای تصدی سمت "رهبر هوش مصنوعی" باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/150204" target="_blank">📅 14:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150203">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
بابک زنجانی: نفوذی ها با لباس انقلابی اومدن و دارن حسابی خرابکاری میکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/150203" target="_blank">📅 14:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150202">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سازمان دامپزشکی کشور: تاکنون هیچ مجوز یا موافقتی برای کشتار و عرضهٔ گوشت اسب، الاغ و استر صادر نشده و هیچ تصمیم اجرایی در این زمینه گرفته نشده است
🔴
کشتار و عرضهٔ گوشت این حیوانات تخلف محسوب می‌شود و با موارد شناسایی‌شده برخورد قانونی خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/150202" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150201">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">منابع بانک مرکزی برای عرضه ۱۰ هزار دلار به کارت‌های ملی تو مرحله اول یه میلیارد دلاره
❗️
یعنی نهایتا این ارز به ۱۰۰ هزار نفر می‌رسه   @shahab_gold_trading</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/150201" target="_blank">📅 14:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150200">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcyNZVWrqqoq1oWj2gghJlAAwYpoFfunw8tZHKjNyPebB4PNcjHyYJ5sW-9YgIhtGQm5EKzU6Gakp1ni7sQ5HDD3rblnZ5Va8MXbec0nNsehdmfttG9NHTEpzpUKlPXiBgnPkOgTDLSxhRUrPnO7OirPJDzaGKCoZtiqQOeKWQFJ0VH9ihCQq8klf4MIGZUnAVDSGZ11svi0FfCinL5BaEQQEKlWuizukEvhmkZ57lcReRHF5hmGVfj3Vee-oWEQYbrTsm8bcSM0MqKKThPrN1R4dcf_JtWkw3pI-f5ixRnBpnH4V2qR4y_p9hZ6Eyrbc9amjgiFwQj5KfQHJptpeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فلایت‌رادار از تغییر مسیر یک پرواز دیگر شرکت «فلای‌دبی» به مقصد اسرائیل خبر می‌دهد
🔴
بر اساس این گزارش، هواپیما در حال بازگشت به دبی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/150200" target="_blank">📅 14:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150199">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d16bea321.mp4?token=LVZMTIoFD5ijg4GbK51vG8dTEhwQ7YM8JU7mTXFn5krLaaN98Nz8bZHbcV4_qlJJgmXaYYmNoNIy1AJlsur5-oZzQVixK-8oDXz8V0s6PMKwphIRoakjgQUS73KORYGkHvUtIFUGRhZznXrk4ZbdJ5vanfH2SNeaHxue0d08_YXz3KHL2qI1ta4SiPHKMEhoKGftrbyapSRNq7dRJQ87fAZiry1DTvM4yUAhmNs3TKynx-1assAvmJubAeEWX9GU8RRozmA_DTGKZX0QUr37bE-7sBbL2W4stDID0uh4YPfJNLwenHK94MzKMdD55yi50EyFUkPJnacTMr5npqfzig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d16bea321.mp4?token=LVZMTIoFD5ijg4GbK51vG8dTEhwQ7YM8JU7mTXFn5krLaaN98Nz8bZHbcV4_qlJJgmXaYYmNoNIy1AJlsur5-oZzQVixK-8oDXz8V0s6PMKwphIRoakjgQUS73KORYGkHvUtIFUGRhZznXrk4ZbdJ5vanfH2SNeaHxue0d08_YXz3KHL2qI1ta4SiPHKMEhoKGftrbyapSRNq7dRJQ87fAZiry1DTvM4yUAhmNs3TKynx-1assAvmJubAeEWX9GU8RRozmA_DTGKZX0QUr37bE-7sBbL2W4stDID0uh4YPfJNLwenHK94MzKMdD55yi50EyFUkPJnacTMr5npqfzig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئوی یکی از مسافرهای اسرائیلی پرواز فلای‌دوبای: 'الان تروریست رو مهار کردیم. داریم آماده فرود می‌شیم. هر کسی صدای منو می‌شنوه، ما کمک لازم داریم. داریم به سمت تبوک پایین میایم، ظاهراً یه جایی توی عربستان سعودی؛ منطقه‌ای ناآشنا و ناشناخته. همه آدم‌های داخل هواپیما سالم و در امانن، به جز خلبان.
🔴
ما کمک لازم داریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/150199" target="_blank">📅 14:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150198">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWsFkiUOMIY_mXFENN-ubob5n4Q0STv0ZBNeDhi6-4slbcEuNXOiGroHDMVAf6mOSoD9NNoPaZyiXhykhZMSfS38TUwN-sEElAmRRndoNNtqfGH7Rjip5ACO2FwCGcZKA0Hm6Z0Ufp64psazHfX0njymBovf1hofCzBLNdoMllMV0NLZwI80oGHFSG9hdgWCjozfXBFenj0ycrAERlp2KHvJPDoLtZiJGBxY6qoEfJmzi96EkhLKwV-bJqlRk968vnBIBKUxUWcTvfUncE6-jw4opKm7i-HvXqug5w4Ur9nsTeXqBiqTgmrgZN3Yj71CuEsDOTy8eeNcgga12wz0sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسموتریچ، وزیر دارایی اسرائیل : دولت اسرائیل باید به نیت توجه کند، نه به نتایج.
🔴
هر کسی که تلاش کرد هواپیما را سرنگون کند و ۱۸۰ اسرائیلی را به قتل برساند، باید به عنوان قاتل مجازات شود. او و هر دولت یا سازمان تروریستی که او را فرستاده است.
🔴
سپاسگزاری به خالق جهان برای معجزه بزرگ نجات
🔴
اما وظیفه ما - من دشمنان خود را دنبال خواهم کرد و نابودشان خواهم کرد و باز نخواهم گشت تا زمانی که کاملاً از بین بروند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150198" target="_blank">📅 13:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150197">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9f5e17072.mp4?token=CjacKh-W5HXHA73WXI4Y0hpaGsS1V5YCaDQi88JdmV9BzzAoihkpHRITFWYeQRaZDs9f75iMihN63C6OtY4H-wOSjusf1MT_x3FGPN_C1rh0VageU6p-ImwuYy_AWUpW84Io0s9RRTyXTHFeLQEWq2RXUBSK5N1Ct6RLdQ3jkFcKiYxU2zXiklwns42haZrZJE10BCkohArDFeZfZyLhjIjc_FE6PNIAZdx0hwSMyjT4LjMH5F4HuVXCf3v5x31aV0aiB1GrTXO9o7TLj6OEMDZEXeFQqB_emq2q6Xae9JB1v4gBZt1qn3gxnprCbaC51BOYW1hAeT4zvYbaYDrDRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9f5e17072.mp4?token=CjacKh-W5HXHA73WXI4Y0hpaGsS1V5YCaDQi88JdmV9BzzAoihkpHRITFWYeQRaZDs9f75iMihN63C6OtY4H-wOSjusf1MT_x3FGPN_C1rh0VageU6p-ImwuYy_AWUpW84Io0s9RRTyXTHFeLQEWq2RXUBSK5N1Ct6RLdQ3jkFcKiYxU2zXiklwns42haZrZJE10BCkohArDFeZfZyLhjIjc_FE6PNIAZdx0hwSMyjT4LjMH5F4HuVXCf3v5x31aV0aiB1GrTXO9o7TLj6OEMDZEXeFQqB_emq2q6Xae9JB1v4gBZt1qn3gxnprCbaC51BOYW1hAeT4zvYbaYDrDRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری از خلبان چاقو خورده پرواز فلای دوبی
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150197" target="_blank">📅 13:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150196">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DABHVWDoKQAP0Ozz4_tgEWTxvkDOk2G412CIaHUWnQ4BMZqKYgzUOpIen59ANn6j3BE-hvYvcWuz1kVyMq7vAufQHpDXh3i-soQUinLsv5B7qqU1opgedcsWwDtsd8uTzc040X4-Dte6Xz1zbJU1NttX_UZGuGOn5ORQs2GvwGDAr3xB2P21uFJBeGa-qBX8bwjfhttviGrshvgVSC0SLnnkmhrOpg9uXEajLZuCS6sG5QZ8VKbA8DlMDGJZoWmCgF5WnmM2exexPnQgj3I-viHEP6i1gMhu899LxiH75tN9rCCKHhxK_nGC4fp44vZmBzqlH7-Ra4TWxcEypgnO8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از بال آسیب دیده هواپیمای فلای دبی
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150196" target="_blank">📅 13:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150195">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
پزشکیان: تنگه هرمز به عنوان یکی از مهم‌ترین گذرگاه‌های دریایی، جایگاهی ویژه در امنیت و اقتصاد جهان دارد
🔴
نگاه ما به این آبراه راهبردی، مبتنی بر حفظ منافع کشور‌های منطقه است
🔴
امنیت پایدار خلیج فارس و آبراه‌های آن، در گرو نقش‌آفرینی کشور‌های منطقه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/150195" target="_blank">📅 13:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150194">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
دیمیتری پسکوف، سخنگوی کرملین:
موضوع انتقال سامانه‌های S-400 روسیه از ترکیه، در حال حاضر در دستور کار قرار دارد.
🔴
کار مربوطه در حال انجام است و تماس‌های لازم نیز برقرار می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150194" target="_blank">📅 13:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150193">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ddc1df6f.mp4?token=F0TclWW-aVyEVE3SJViy_1Lt4KvhgxuD6qUpkJ2TQY7fvWGDu3tr4eI_yK5SyiT3DcY-3pyohAw5PVR-TC16E9kmcHKc7tj6H9wdbsMHaiRpHqMHv3YrO70t0uOsVoI-1Z8DcTf3fdL6fkI_VjHu9XQ1NCjldlf6Nsh5cHYuSJBylCBg4-rzkX3LCm9ODVjat7EcfydiLWhceeOdLICiHWhWB-QW0UZTzKZFMcr4Th5hyBXWfo4kJVzWbbEamdZXCoxuqh6S3qMhR3RAbsXC6CufQnf2x3TR7RziwP186feZOLGEjsxCezQyw01NMu0fs9ZRMq9gC7mL6fI-vjsiWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ddc1df6f.mp4?token=F0TclWW-aVyEVE3SJViy_1Lt4KvhgxuD6qUpkJ2TQY7fvWGDu3tr4eI_yK5SyiT3DcY-3pyohAw5PVR-TC16E9kmcHKc7tj6H9wdbsMHaiRpHqMHv3YrO70t0uOsVoI-1Z8DcTf3fdL6fkI_VjHu9XQ1NCjldlf6Nsh5cHYuSJBylCBg4-rzkX3LCm9ODVjat7EcfydiLWhceeOdLICiHWhWB-QW0UZTzKZFMcr4Th5hyBXWfo4kJVzWbbEamdZXCoxuqh6S3qMhR3RAbsXC6CufQnf2x3TR7RziwP186feZOLGEjsxCezQyw01NMu0fs9ZRMq9gC7mL6fI-vjsiWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده امارات در سازمان ملل: جزایر سه‌گانه متعلق به امارات هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/150193" target="_blank">📅 13:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150192">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
یک نفتکش در تنگه هرمز مورد اصابت پرتابه قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/150192" target="_blank">📅 13:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150191">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سخنگوی وزارت دفاع: اگر [آمریکا] شرایط و حقوق مشروع ایران را بپذیرد، راه برای پایان درگیری فراهم است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/150191" target="_blank">📅 13:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150190">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
سنتکام: نیروهای آمریکایی روند خروج نیروها و تجهیزات از پایگاه هوایی اربیل را به پایان رساندند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/150190" target="_blank">📅 13:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150189">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
جمع‌بندی حادثه عجیب پرواز فلای‌دبی به مقصد تل‌آویو
✈️
یک فروند بوئینگ ۷۳۷ فلای‌دبی که از دبی به مقصد تل‌آویو در حرکت بود، ابتدا کد اضطراری 7700 و سپس کد 7500، مرتبط با وضعیت احتمالی مداخله غیرقانونی/هواپیماربایی، را مخابره کرد.
🔴
هم‌زمان گزارش شد برخی…</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/150189" target="_blank">📅 13:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150188">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6cb9V5ghqvrxiCGLiqj_5kUgy6xWagEQmMkaV_7Np4TH7spblLAPElc3ZcCfCyQoA8QUR09JbeG06viX1NNV5rZmO23SUbOB-wcIdpMvaMjvfueCtmeAYgvkytYgIl7iABchK1vVB2VFi2d8pL2mCwuH6SzGU1pkYBn-UpWjQXo60_ha_EWKWbOSxztl6mdE-5OybC52SAfVFJfk2LUM7qetBgo58ZB2o9OXguhAR9lSghHLnqX8G9Rw7KJw6TLMsOw8rvTTlveufDHzpbkqmjvOQGDKpfu5yHysTMibrJk0WdCLftar-KN_63PVl2P3ugaF3fJWU4p9wRILk5Eww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک نفتکش در تنگه هرمز مورد اصابت پرتابه قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/150188" target="_blank">📅 13:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150187">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
چین: آمریکا و ایران به تفاهم‌نامه اسلام‌آباد برگردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/150187" target="_blank">📅 12:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150186">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سخنگوی سپاه : توی هر ۲۴ ساعت در تنگه هرمز درگیری نظامی وجود داره اما مدتیه که آمریکا پاسخ نمیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/150186" target="_blank">📅 12:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150185">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
یدیعوت آحارانوت: تخمین‌ها حاکی از آن است که حادثه رخ داده در هواپیمای فلای دبی یک اقدام تروریستی بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/150185" target="_blank">📅 12:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150184">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
یدیعوت آحارانوت: تخمین‌ها حاکی از آن است که حادثه رخ داده در هواپیمای فلای دبی یک اقدام تروریستی بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/150184" target="_blank">📅 12:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150183">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c905f1bc3f.mp4?token=Q5dd0snE3qTnt81vEcXDb8LuBPh9n6lcuzOeIVKhqlLlaktbV14mt81ecXDDhbF2QlUJDRsAmHEFfYbanRH4nY-bVAdU0aqU8UB3EMhKwtDzDy7cqW-5fDpNNsA65TiTK_JeeGujnpnRGDAQQskhOwBarOGaQ075igss5rNVl_041QxehDnSIoLnkaw2l1xlOwSg0zQDpyP_chW_L5RpijtDav9g1XJ8A568qqELzrHjNrNv1NrYQQd77QE0J-Yec2T3cdjkr56fR4qcRSlH7L3KZn8lgBeD_q0I3gT-U9AzvxCquk5vc2wMaay8VT_2efxn3TBPlXJP9DCVXVXmHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c905f1bc3f.mp4?token=Q5dd0snE3qTnt81vEcXDb8LuBPh9n6lcuzOeIVKhqlLlaktbV14mt81ecXDDhbF2QlUJDRsAmHEFfYbanRH4nY-bVAdU0aqU8UB3EMhKwtDzDy7cqW-5fDpNNsA65TiTK_JeeGujnpnRGDAQQskhOwBarOGaQ075igss5rNVl_041QxehDnSIoLnkaw2l1xlOwSg0zQDpyP_chW_L5RpijtDav9g1XJ8A568qqELzrHjNrNv1NrYQQd77QE0J-Yec2T3cdjkr56fR4qcRSlH7L3KZn8lgBeD_q0I3gT-U9AzvxCquk5vc2wMaay8VT_2efxn3TBPlXJP9DCVXVXmHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار تجمعات شبانه: قالیباف رسایی رو رها کن؛ در مجلس رو وا کن
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/150183" target="_blank">📅 12:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150182">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/737da06d5f.mp4?token=m-GLnOG0KYKDDKKggIGwhTGoBooh7kfkr_TgslRtWxeEHjpVX3gD399zxybuL3IQrm3tO7I8-Pcgao0FL_e9E1IYXDDz33LbzD7x20qfkh26a5eCjxd19kXivnx8kbOCRZU1weoZsmfRkT15hYzxFW-vh3R0i2T-00Y1f89Ki4wCVc5PRJMMEDE5-2fulhFvo5mWEkkZnCCzDgnBaBLUIHi59nA0ZLIqX5CH8rQiFVa4QJSsL1MsGkt1o_62MHjkeOoJGNozIoyK2UNnAuSoxEaNJWsaL5aflv52TUen9tZARW7iPhwHOHImAg-UH70iSO_vccOSgSSJE2IKwiE36A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/737da06d5f.mp4?token=m-GLnOG0KYKDDKKggIGwhTGoBooh7kfkr_TgslRtWxeEHjpVX3gD399zxybuL3IQrm3tO7I8-Pcgao0FL_e9E1IYXDDz33LbzD7x20qfkh26a5eCjxd19kXivnx8kbOCRZU1weoZsmfRkT15hYzxFW-vh3R0i2T-00Y1f89Ki4wCVc5PRJMMEDE5-2fulhFvo5mWEkkZnCCzDgnBaBLUIHi59nA0ZLIqX5CH8rQiFVa4QJSsL1MsGkt1o_62MHjkeOoJGNozIoyK2UNnAuSoxEaNJWsaL5aflv52TUen9tZARW7iPhwHOHImAg-UH70iSO_vccOSgSSJE2IKwiE36A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویر ویدئویی از لحظه فرود اضطراری هواپیمای فلای دبی پس از درگیری در کابین
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/150182" target="_blank">📅 12:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150181">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
مهاجرانی سخنگوی دولت: در جلسه امروز پیشنهاد طرف آمریکایی توسط عراقچی وزیر امور خارجه کشورمان به رئیس‌جمهور ارائه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150181" target="_blank">📅 12:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150180">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
پزشکیان: به آقای قالیباف گفتم اگر ما مشکلی داریم کمک بکنید؛ با حذف کردن مشکل حل نمی‌شود  ‏
🔴
واقعیت این است که ما همه عیب داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/150180" target="_blank">📅 12:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150179">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6b8d09462.mp4?token=gEB_nuv_dTtgaeucR9l2HYjdB3Fcpt86DaY4LMJk9m9yliL_0sEDiDP5pGDrQ1pZ2WmWe4K9SKS7UNTpuP6zWTQHIEQzo8URHx3icc41bL4tKMAj1HPqINsWKBSbh1gqSr3zEBfmeN_Jn3Mj53Wc9THBPZY6ihnLp7C7u_FunovSxq5Tyx3xXIY0BeemWYbYsknkVlC2H3L-AYeg9ib3IwOECP6MU34KD3QqQf1zpTAs-W2u0MCZAtfRTPhCe7P3XM4PeZhHIjKj91Qj6S5_PbC3sAqzvj687DXCsWTEW-gJhLI7KEUSDyjQtmq9oWzT8AaWKZMGI35KH4yM5aRqEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6b8d09462.mp4?token=gEB_nuv_dTtgaeucR9l2HYjdB3Fcpt86DaY4LMJk9m9yliL_0sEDiDP5pGDrQ1pZ2WmWe4K9SKS7UNTpuP6zWTQHIEQzo8URHx3icc41bL4tKMAj1HPqINsWKBSbh1gqSr3zEBfmeN_Jn3Mj53Wc9THBPZY6ihnLp7C7u_FunovSxq5Tyx3xXIY0BeemWYbYsknkVlC2H3L-AYeg9ib3IwOECP6MU34KD3QqQf1zpTAs-W2u0MCZAtfRTPhCe7P3XM4PeZhHIjKj91Qj6S5_PbC3sAqzvj687DXCsWTEW-gJhLI7KEUSDyjQtmq9oWzT8AaWKZMGI35KH4yM5aRqEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: به آقای قالیباف گفتم اگر ما مشکلی داریم کمک بکنید؛ با حذف کردن مشکل حل نمی‌شود
‏
🔴
واقعیت این است که ما همه عیب داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/150179" target="_blank">📅 12:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150178">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
رسانهٔ اسرائیلی:مقامات اسرائیلی در حال بررسی این احتمال هستند که یکی از خلبان‌ها تلاش کرده باشد هواپیما را به دلایل سیاسی ربوده و خلبان دوم تلاش کرده است تا او را کنترل کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150178" target="_blank">📅 12:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150177">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
فواد ایزدی تحلیلگر صداوسیما:
دفعه قبل ترامپ اجازه داد تیم ایرانی از پاکستان برگرده بعدش محاصره دریایی رو شروع کرد، اما ایندفعه قبل از اینکه تیم ایرانی از نیویورک برگرده محاصره هوایی رو شروع کرده و اصلا ترامپ دنبال توافق نیست بلکه میخواد حکومت رو سرنگون کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150177" target="_blank">📅 11:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150176">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c78f9d54.mp4?token=SVO_tuejzH7Uw_RcAnBXRQTq3S5c7ec8h3qVolj8BkUui-dXcLVausvq8pmyFyTTOx7WZ77aa3mP_9YlE8xmNJo7kGy_tlxZFxl6IW04mPL563q9LyzAGICb5Isuyw5sX2ncT1v1HdUkZaHM5zj-8s7iusao0dDFpVobbAgnv9qeU3UPR-7P9TqPxImedzizep0DS7ag4oAb_p47HoVREB_I8ZUs0MZaFEM0yOuAvl7jFvWzuaRSJgh_940j-dFAUcdjc9fEF0-6y9XvwfhfMtYEjyG3Ja-Nl0ygnw_u236s4Rjb_taSUOxoHcQR-_cVCVxtengogDP7v1w6PIBHhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c78f9d54.mp4?token=SVO_tuejzH7Uw_RcAnBXRQTq3S5c7ec8h3qVolj8BkUui-dXcLVausvq8pmyFyTTOx7WZ77aa3mP_9YlE8xmNJo7kGy_tlxZFxl6IW04mPL563q9LyzAGICb5Isuyw5sX2ncT1v1HdUkZaHM5zj-8s7iusao0dDFpVobbAgnv9qeU3UPR-7P9TqPxImedzizep0DS7ag4oAb_p47HoVREB_I8ZUs0MZaFEM0yOuAvl7jFvWzuaRSJgh_940j-dFAUcdjc9fEF0-6y9XvwfhfMtYEjyG3Ja-Nl0ygnw_u236s4Rjb_taSUOxoHcQR-_cVCVxtengogDP7v1w6PIBHhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ربات‌های چینی با لباس‌های سنتی عربستان، برای شهردار ریاض و سفیر چین رقص محلی اجرا می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150176" target="_blank">📅 11:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150175">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1bE1ziDmhDBMTfvZnS9kyT_gRRkTeQZa-8TVIlMUvCQhQ1UrD88zzUjAOfW7ZiCXrEnmGWhB7I9ue1jaCkDWwA3jOMJ5nZqjLE6JY9RHrdSXroHtjO2-dzCUsi9jtMOsEKTXpFgM1wdp_RS3SD5nV3cUdnflNJbY1N7fJLZWmSRCy0aDb2Obm5WBUEGOwdMKGMx0DeTYdvAOYlPu4Aw1CqHwzsuFPlHYGohEGZfDI5IO2ZvUCojAV0PnZY_SkHGTezYqXqyMy14JQi5zah8HvWOasdI56Mr33G85h33olC0eBoKKlkWZQzp9oJ_8H4myWx3zQJcBmKMpaw-vcWZUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گاردین:کاخ سفید به طور مخفیانه از امارات متحده عربی و عربستان سعودی خواسته است تا اختلافات خود را کنار بگذارند و اجازه دهند یک فرماندهی نظامی واحد برای مقابله با حوثی‌ها تشکیل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150175" target="_blank">📅 11:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150173">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VriWxapobUmyKbjGeQTCsyeWrXbcvRj0vaeGR_2o1RD5vO4wmW_xps-uwO0gOR3GWd_-wyXQEHJKt2SgyfQcUst80AZ5k3pRIm9IcDCnx74cSBaJih5GK1bcIY1zIv0mcO2lNN-NCJWKPu8-5wLR2hqeiplbf_i4kFypI9hBEv1ghBGAIX4BiUczCWSjVcFwTydTvXftSZaTTrWDeKrf5r9QihrWW_3ENltasVYjnFTBE8Md3F8chPk3L5vj-bjC57Nmf0BJmHqfE_5MfHBatl1HUQSR3QUULyi5lN9ceFh9WJi4GwVGj9YGNnHJ3rLV8OeQrtRG0lEZJnTqHFjJLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uKPb0QJywdhXnC3slHhJC47ze6_pAsAiSa3SrKW_YgeNSk8f8wsx2bsvqU5aQBoHb6UScV0F1AIk6DMK3FbxokxnLfAnqnR1G145bv7fWh4Dh6ksHuU4Vz1cj-kubXb9Y5Zw4jP3yBgCILwDfgGINNSu4ihgRt3P29znwSi4-pivJTq-8t7q1YiGVITl4tUeJn9Zf_uykTroJxsBO8cSfumPwL9PVdnEprdvaE_xILcizpuEodA6q0Z1emU4evjX2RlrkH6KEfZL6mRrByEJG-6epaSmaiu_GX5qKzEfBXiVIehfEk4M2vL3ZkuZMswRTot23rRdb2nXzkEtWNAqxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
مسافران هواپیمای اماراتی در خاک عربستان سعودی منتظر هواپیمای جایگزینی هستند تا آن‌ها را به مقصدشان ببرد؛ برخی از آن‌ها پیراهن‌هایی با لکه‌های خون به تن دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150173" target="_blank">📅 11:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150172">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
نتانیاهو به رئیس دولت امارات:
اسرائیل اطلاعات جدیدی از احیای برنامه هسته‌ای ایران دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150172" target="_blank">📅 11:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150171">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pUCwZeQj2OW9t3b7eB5wQ6pzRvgsmHYm2OwS-TGbJLk0HkkhYW_5OBUQv62BoFE3dlV0ckhRSps-RUyOs6lSr_7KK-ujXIF-GuUipl1dgd55Z3X2HCifatUNp913RJTcsuPUgPDWG9C8PIRxn9aqM5wc5jigZjQKTazocg7ro1sNBg-OpJPHlvytcZfY6HqG-D2pxeM5XxwWO01dljnRcUx5Vt_LCzcu0lfrJ8eA7Vv34ur8F3XjLVv6fp7TFAorbfDIjoS0def9l_dCpo1rqM-ZgYb0_--RXpd-VskeMUKZwzG3q74Y4DFlAebAh1DCDL07S4ggxpL9QypjwYMW_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دود ناشی از اصابت موشک‌های بالستیک تاکتیکی ایسکندر-ام در شهر دنیپرو، اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150171" target="_blank">📅 11:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150170">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
رسانه‌های آمریکایی: نیرو‌های نظامی آمریکا امروز، پس از دو دهه حضور و مداخله نظامی در عراق، پایگاه‌های خود در این کشور را ترک می‌کنند
🔴
نیرو‌های باقی مانده ایالات متحده، به اردن منتقل خواهند شد
🔴
شماری از تفنگداران دریایی آمریکا برای حفاظت از نمایندگی‌های دیپلماتیک این کشور در عراق باقی خواهند ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150170" target="_blank">📅 11:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150169">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل گزارش داد که خدمه پرواز شامل یک خلبان روسی و یک کمک خلبان اوکراینی بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150169" target="_blank">📅 11:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150167">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94d66c2f72.mp4?token=fQs5ZmwTSepkWrN5KgzsaU4W12K_TiZb-JovehBuqpoEBMA94FNXDZpaLPlPKLSj0LxZLLFx3CnfOOieAn-nxKnuZBahDoIsKuFqHg9H6ZZF6ZwsF8E6LGBLypGCmAOA1_tmgR8iHsOO82iKzDkIX9k_l3WSbp9OCzFZC6lhJgdQ1YNwP2Z2427MtlDefcgkgA6tbIBZqPkI-vKwryTsnyBuNa3rJ_cEtTIPqLny_ga5CKBu8A8vLMthAM3K23gD-7Ee_8bTlpPXSDJA3A7tF3QaJqlqKo0p2zSPGklTAfBxCTVJTi35FXKyG_Q9IZQ-EY7qGvcKFnzDsydRABfuGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94d66c2f72.mp4?token=fQs5ZmwTSepkWrN5KgzsaU4W12K_TiZb-JovehBuqpoEBMA94FNXDZpaLPlPKLSj0LxZLLFx3CnfOOieAn-nxKnuZBahDoIsKuFqHg9H6ZZF6ZwsF8E6LGBLypGCmAOA1_tmgR8iHsOO82iKzDkIX9k_l3WSbp9OCzFZC6lhJgdQ1YNwP2Z2427MtlDefcgkgA6tbIBZqPkI-vKwryTsnyBuNa3rJ_cEtTIPqLny_ga5CKBu8A8vLMthAM3K23gD-7Ee_8bTlpPXSDJA3A7tF3QaJqlqKo0p2zSPGklTAfBxCTVJTi35FXKyG_Q9IZQ-EY7qGvcKFnzDsydRABfuGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پروازهای جنگی متعددی در آسمان شهر طائف در عربستان سعودی در حال انجام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150167" target="_blank">📅 11:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150166">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJH36MvhQFoWp7q0GR-jWHE08CnciAOy3xeyi2eq49bLltBgMjfW9pPrj_XUcHtHMJ5ElWKT8YGDMyl_YA4zQuQfbT30_lDbN_phbRAe26hslmjw6YfniQ2mWvjeBzD-iAryMLCP0DdDCWIvSjU4WEtivFEdLepiVk1VayMiBG5etmHQ_M3J4v5k3ZONr9I9-_lehD9jZBdIqYB_9pGOx8IxGntyiJz_bO9HCQ_JbjmB99NZE_8yKlYiGqGE59QfgMe0rggcYbSdW9e7X2czif6Bx0-MfZIJo08gV0L6hothw5920998Hv0r3xeFxcVhjrfsZbkSJF5VH7gl2BvPZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کتب کمک درسی ۷۰۰ درصد گران شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150166" target="_blank">📅 11:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150165">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی :  دلیل درخواست کمک از سوی هواپیما، وقوع درگیری و نزاع میان مسافران در داخل آن بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/150165" target="_blank">📅 10:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150164">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF): «در پی گزارش‌های اخیر، رئیس ستاد کل ارتش اسرائیل در دقایق گذشته یک ارزیابی وضعیت با حضور فرمانده نیروی هوایی اسرائیل، رئیس اداره عملیات، رئیس اطلاعات نظامی و شماری دیگر از فرماندهان انجام داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/150164" target="_blank">📅 10:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150163">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
مورگان اورتگاس، سخنگوی پیشین وزارت خارجه آمریکا : اگه مقامات جمهوری اسلامی منتظر انتخابات میان دوره‌ای آمریکا هستن تا قدرت تصمیم گیری ترامپ درباره ایران محدود بشه، دچار محاسبه‌ای کاملا اشتباه شدن
🔴
کارزار فشار حداکثری علیه جمهوری‌اسلامی و کشته شدن قاسم سلیمانی هردو زمانی رخ داد که دموکرات‌ها کنترل کنگره رو در دست داشتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150163" target="_blank">📅 10:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150162">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سخنگوی نخست‌وزیر اسرائیل: حادثه‌ای که برای هواپیمای فلای‌دبی رخ داد، اقدام به هواپیماربایی نبوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150162" target="_blank">📅 10:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150161">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
فلایت رادار: یک فروند هواپیمای مسافربری بوئینگ ۷۳۷ شرکت فلای‌دبی که از دبی به مقصد تل‌آویو در پرواز بود، پس از آنکه برای مدت کوتاهی کد اضطراری ۷۷۰۰ و سپس کد ۷۵۰۰ مربوط به احتمال هواپیماربایی را مخابره کرد، اکنون در حال بازگشت و تغییر مسیر به سمت دبی است …</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/150161" target="_blank">📅 10:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150160">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
فلایت رادار: یک فروند هواپیمای مسافربری بوئینگ ۷۳۷ شرکت فلای‌دبی که از دبی به مقصد تل‌آویو در پرواز بود، پس از آنکه برای مدت کوتاهی کد اضطراری ۷۷۰۰ و سپس کد ۷۵۰۰ مربوط به احتمال هواپیماربایی را مخابره کرد، اکنون در حال بازگشت و تغییر مسیر به سمت دبی است …</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/150160" target="_blank">📅 10:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150159">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
پروازهای فرودگاه بن گورین به حالت تعلیق درآمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/150159" target="_blank">📅 10:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150158">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تتر به ۲۵۹ هزار تومن رسید  برای اولین  بار در طول تاریخ فقط در عرض یک روز ۱۰ هزارتومان دلار بالا رفت.   @shahab_gold_trading</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150158" target="_blank">📅 10:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150157">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
فلایت رادار: یک فروند هواپیمای مسافربری بوئینگ ۷۳۷ شرکت فلای‌دبی که از دبی به مقصد تل‌آویو در پرواز بود، پس از آنکه برای مدت کوتاهی کد اضطراری ۷۷۰۰ و سپس کد ۷۵۰۰ مربوط به احتمال هواپیماربایی را مخابره کرد، اکنون در حال بازگشت و تغییر مسیر به سمت دبی است …</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/150157" target="_blank">📅 10:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150156">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
منابع عبری: انتظار می رود این هواپیما 10 دقیقه دیگر در عربستان سعودی فرود بیاید
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150156" target="_blank">📅 10:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150155">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
فلایت رادار: یک فروند هواپیمای مسافربری بوئینگ ۷۳۷ شرکت فلای‌دبی که از دبی به مقصد تل‌آویو در پرواز بود، پس از آنکه برای مدت کوتاهی کد اضطراری ۷۷۰۰ و سپس کد ۷۵۰۰ مربوط به احتمال هواپیماربایی را مخابره کرد، اکنون در حال بازگشت و تغییر مسیر به سمت دبی است …</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150155" target="_blank">📅 10:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150153">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165b51a72c.mp4?token=ue69fZBl9w_6CW58KPdmqPESJl5cPMNC5UdkktdFn62cgQmKkAY3zOghOhgNadZb-oV0FI1B4U7VHvSHaa7ONsKNYFtVlufnmPjuUGEawD_BsMf93UwaHM-jsOSZH2V9n2M3j29EemhNnLd1H2ZRsbfVlGfnliXuocrtbVDYXm55pyFJp-Z90bWSVk2LdzKz1wqeN-MzoEMeHzrraN4x3mDGvTCOTWn27xBTYGYULcfuU7v8JmgOxmJEruDDwN9U1SCxNDXSOaxl5lon7hcepDT7PdRTU9KSHWZbDhnW5lHa0m2nVilg5tBwyGht_fSRZGCMX82YwdB4n27lfuRW1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165b51a72c.mp4?token=ue69fZBl9w_6CW58KPdmqPESJl5cPMNC5UdkktdFn62cgQmKkAY3zOghOhgNadZb-oV0FI1B4U7VHvSHaa7ONsKNYFtVlufnmPjuUGEawD_BsMf93UwaHM-jsOSZH2V9n2M3j29EemhNnLd1H2ZRsbfVlGfnliXuocrtbVDYXm55pyFJp-Z90bWSVk2LdzKz1wqeN-MzoEMeHzrraN4x3mDGvTCOTWn27xBTYGYULcfuU7v8JmgOxmJEruDDwN9U1SCxNDXSOaxl5lon7hcepDT7PdRTU9KSHWZbDhnW5lHa0m2nVilg5tBwyGht_fSRZGCMX82YwdB4n27lfuRW1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منابع ایتایی: کار ماست، الله اکبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150153" target="_blank">📅 10:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150152">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل در مورد هواپیمای بوئینگ ۷۳۷ فلای دبی: خلبان کد مربوط به ربوده شدن هواپیما را ارسال کرده است، شماری از اسرائیلی‌ها در این پرواز حضور دارند.
🔴
این هواپیما دیگر در اپلیکیشن رهگیری پرواز Flightradar نیز نمایش داده نمی‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150152" target="_blank">📅 10:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150151">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: مقام‌های اسرائیلی ارتباط خود را با یک فروند بوئینگ ۷۳۷ فلای‌دبی از دست داده‌اند و اسرائیل در حال بررسی احتمال هواپیماربایی این هواپیماست.
🔴
جنگنده‌های نیروی هوایی اسرائیل برای رهگیری این هواپیما به پرواز درآمده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150151" target="_blank">📅 10:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150150">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
فلایت رادار: یک فروند هواپیمای مسافربری بوئینگ ۷۳۷ شرکت فلای‌دبی که از دبی به مقصد تل‌آویو در پرواز بود، پس از آنکه برای مدت کوتاهی کد اضطراری ۷۷۰۰ و سپس کد ۷۵۰۰ مربوط به احتمال هواپیماربایی را مخابره کرد، اکنون در حال بازگشت و تغییر مسیر به سمت دبی است …</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150150" target="_blank">📅 10:04 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
