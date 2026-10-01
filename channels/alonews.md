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
<img src="https://cdn4.telesco.pe/file/LKUcJOMXwon0mKhbhlO5EuKDeiQnQUbLK71hd4w0xXNyZkC42PpXKYogpOmJRmq-Y4oA9SNmbty7xOX4JxsbAoJdaeJQ4tOzj7pMoPl4fKqckU19PYWCPuDgE-PxSNZk-D-FAlyXKhTbyhIoYORKLRPKNq1UxjrkJIEHE6Ym3bYVQgl8OTXcFTBoVw1R5iwV8NhMvuy9xHZavcgdxgmeIa6qjpL5h9F-RCWkdp9pUiRlexj-q9ts2XdcOGAOnhiLkNiiErULk6uhnutyXQVXc6ksF_thUIItdfbnx4AibW7enpBFPZYzf1B4ngbZzijzpxJh54C41bPe-YVhrcz9og.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 22:39:44</div>
<hr>

<div class="tg-post" id="msg-150476">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
تسنیم: پلیس خشن و نامرد فرانسه امروز به معترضا گاز اشک آور زده
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/alonews/150476" target="_blank">📅 22:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150475">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5b019bf6e.mp4?token=EMiQ3LLWQ08Jp8GWyM1uwE6snWed5rmt1XfcWOzv0Vvn6p9KH-1PK4yQCUMLepc17iCAlSrZOixeYCcekBtqvoE3JGxLVoQWNuOBTg5wXss4JvmYFDZXG3PWT0sCcj3nL_V9CnFcFMwsMQYvmDGbrOzItj9K4BGpKFIbKU3zDaMFp-CEQ33-4xyWPV13hVmVyrJsikCHLTnHf1bFb3tMXK6TcG6Megt_5jI6IHX9sgTQ5JtIsKGDue1EGm05EBN3v3gyBYX0Dgn8Qm9Ns0PhxzwR3uOGy1rZrHeX7jTYOQbKXBgm_44Rue0bRJ-qjDSGlfw_Co7vd4xj51Asjp_cMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5b019bf6e.mp4?token=EMiQ3LLWQ08Jp8GWyM1uwE6snWed5rmt1XfcWOzv0Vvn6p9KH-1PK4yQCUMLepc17iCAlSrZOixeYCcekBtqvoE3JGxLVoQWNuOBTg5wXss4JvmYFDZXG3PWT0sCcj3nL_V9CnFcFMwsMQYvmDGbrOzItj9K4BGpKFIbKU3zDaMFp-CEQ33-4xyWPV13hVmVyrJsikCHLTnHf1bFb3tMXK6TcG6Megt_5jI6IHX9sgTQ5JtIsKGDue1EGm05EBN3v3gyBYX0Dgn8Qm9Ns0PhxzwR3uOGy1rZrHeX7jTYOQbKXBgm_44Rue0bRJ-qjDSGlfw_Co7vd4xj51Asjp_cMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین، رئیس‌جمهور روسیه، درباره سوئیس: «ما از بی‌طرفی استقبال می‌کنیم، اما اگر قرار است سوئیس بی‌طرف باشد، باید کاملاً از تمامی تحریم‌ها علیه روسیه کنار بماند.
🔴
بی‌طرفی نباید فقط در حرف باشد. سوئیس چه چیزی به دست آورد؟ هیچ چیز.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/alonews/150475" target="_blank">📅 22:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150474">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
کارشناس صداوسیما: ژاپن توسعه داره ولی هویت نداره و با کشوری همکاری میکنه که اون فاجعه هسته ای رو براشون رقم زده، مردم ما نمیخوان مثل ژاپن باشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/150474" target="_blank">📅 22:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150473">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onTVWEw6WDUqyJQuQV1tSj8zKM9LRT5Lyp2Ht6-3FYZsSrydRbF-ti9d24jN-43VyXeOCnqe748ISkPvnG3X_p3xIMTsetZmHCOAkjUtDOMxpiQcC_UjjL7TnpNYVkXYcVSRAKMeeFLi3i2vNlgMlMbHlK_JnsASZJUhgPQ3rF6v1H684SrPlRnq56I26FJaacxg_zfcp_-wfEwaUXulsKe67wWjeFLUsJ8TpUE647KmxeU8gujxp2SHPW-VsHpKS0EuZa6ZZkAWaJTKDAIwW8aKGwecaC3Lf3bKMoq1CsBYnhvhqogtECt6P0o54BaXKSD5ohwXQZNLRsEWWnv_uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : قیمت‌ها به طور چشمگیری نسبت به زمانی که بایدن و دموکرات‌ها قدرت را به ما تحویل دادند، کاهش یافته است. به همین دلیل بود که من انتخابات را بردم، و اکنون قیمت‌ها به سرعت در حال کاهش هستند.
🔴
این تقصیر دموکرات‌ها است، نه جمهوری‌خواهان - اما ما در حال رفع این مشکل هستیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/150473" target="_blank">📅 22:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150472">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
بلومبرگ: ایران به‌طور غیرعلنی پیشنهاد کرده است که در ازای کاهش تحریم‌ها، دسترسی بازرسان هسته‌ای به تأسیساتی که در جریان جنگ آسیب دیده‌اند را دوباره برقرار کند
🔴
امتیازی احتمالی که هدف آن شکستن بن‌بست موجود در روابط با ایالات متحده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/150472" target="_blank">📅 22:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150471">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
منابع عربی: ایران پیشنهاد داده در صورت کاهش تحریم‌ها، اجازه ورود بازرسان هسته‌ای را صادر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/150471" target="_blank">📅 22:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150470">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
گزارش‌های اولیه از شلیک‌هایی به سمت تنگه هرمز منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/150470" target="_blank">📅 22:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150468">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QL1Upf3fsRMoPDfh0jzIfCyN_4tJ7VjqP8CJEQ9p04l_7WKFrLCBSyhO3Jmvbyt3lKcSRQhKXSb-LtAjgXQ1wYY267I2KVgiqzGFsUY81-UhBaFUl9Ish-UzP6-I5BDCC0UnAPi4WWOmJ2Cw6oKIw2omlXKYNzbR1U56Rx2hwHB_9O5EdoRBEQe-_OEX9KLL9eNemVCZMtsjvYD1dp6LQfglO4RuvbeueMCHXhfHQEtx2bf-Twf6s-cLcRfoInbznfBNIde069K2_VoHSvKv1ARrBoqYtVRslr-nRG8kBuNxMakI5TtmjxjCUq0FoGhGQNNIHGkct5A2H4fuDDTxNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983fb64c5e.mp4?token=s_n9h0QSNBajuo2aHe1Sj_O4AfIQYDMaApdy_K1BLgW5I7Z-4DxIrbqCyozgnvQfN8_gwIEXMgPNCvMrwsCNdSXDQKafTXscQmvF3xbZAwF0yOFCDOZPhMA2mOXBsaa1vEuzcJVw9SYp6PnGU6tBdo5jBwJ03ZVPPRk8hw-VcSkZwlt5DJDMSxdIs4rs8-YKN8kbCuVB-fVypv1YitBTHWFN-SCXu5uz09pV7As2lkaNMJXKvyEzr43B69_3aByoeJ1FtaEEDffyqZzSdGoT7JyBn7IkYoaOTyUiJrC_eBquCBIdFWxCp7yPGeCAcvkqvsHClzw8nHSYjlWXgcTmUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983fb64c5e.mp4?token=s_n9h0QSNBajuo2aHe1Sj_O4AfIQYDMaApdy_K1BLgW5I7Z-4DxIrbqCyozgnvQfN8_gwIEXMgPNCvMrwsCNdSXDQKafTXscQmvF3xbZAwF0yOFCDOZPhMA2mOXBsaa1vEuzcJVw9SYp6PnGU6tBdo5jBwJ03ZVPPRk8hw-VcSkZwlt5DJDMSxdIs4rs8-YKN8kbCuVB-fVypv1YitBTHWFN-SCXu5uz09pV7As2lkaNMJXKvyEzr43B69_3aByoeJ1FtaEEDffyqZzSdGoT7JyBn7IkYoaOTyUiJrC_eBquCBIdFWxCp7yPGeCAcvkqvsHClzw8nHSYjlWXgcTmUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در‌تروث پستی از اعتراضات ایران منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/150468" target="_blank">📅 21:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150467">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
وزارت کشور عربستان: تحقیقات اولیه درباره حادثه هواپیمای شرکت هواپیمایی دبی نشان می‌دهد که خلبان توسط کمک‌خلبان مورد حمله قرار گرفته است
🔴
خلبان هواپیما و کمک‌خلبان آن، پس از بهبودی کامل، صبح امروز همراه با یک تیم امنیتی اماراتی به ابوظبی عزیمت کردند.
🔴
تحقیقات درباره حادثه پرواز دبی توسط مراجع ذی‌صلاح پادشاهی و با مشارکت یک تیم فنی از کشور امارات انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/150467" target="_blank">📅 21:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150466">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سخنگوی نیروهای مسلح یمن: در ۲۴ ساعت گذشته، جنگنده‌های سعودی ۴۷ بار به یمن حمله کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/150466" target="_blank">📅 21:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150465">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بچه هاااا
من هیچ وقت تو زندگیم شانس نداشتم که چیزی و برنده بشم. امروز گردونه صراف و دیدم، چرخوندمش بهم 3 صوت طلا دااااااد
😂
فکر کردم الکیه تا اینکه ثبت نام کردم نشست به کیف پولم
😐
😂
شما بزنید ببینید چی در میاد
👇
https://r.saraf.app/s/agrd346</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/150465" target="_blank">📅 21:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150464">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
صداوسیما : فرانسه با معترضین دانشجو و دانش آموز به خشونت رفتار کرده و گاز اشک آور به سمت آنها شلیک میکند و حقوق معترضین را نقض میکند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/150464" target="_blank">📅 21:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150462">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8620d94f.mp4?token=egsjGnNwsghaocd_iwvBT9_VuC2NRkblJpOdbePmlAjXoIHSAxG3F5lfEDRcKv6-8j2ooklsEW0vIra6ZzwS9yY79CbLMsMVzRejDyztS3wYv71mxFWMilqukixu7bf0Wm7M6S_Gt7IK1D7t8CuDtlITCK_SzZQTfwwbWovQx-tZqWVui_hwLNLMWjP5SPDVGHdn9Uh-KWKRdu-fYqs3Bw6mU69MLAIKA8HWpzAigGxC-hnu6V8QQI-7Of5wYx18ugUmOJ45gRKZ78DkNW_4XVqEPkvNo32745ySXQw1tTZ3QJ9hwlyZ2dmiZErQE6PJnmucqfD5mLxyLZNS7VrkxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8620d94f.mp4?token=egsjGnNwsghaocd_iwvBT9_VuC2NRkblJpOdbePmlAjXoIHSAxG3F5lfEDRcKv6-8j2ooklsEW0vIra6ZzwS9yY79CbLMsMVzRejDyztS3wYv71mxFWMilqukixu7bf0Wm7M6S_Gt7IK1D7t8CuDtlITCK_SzZQTfwwbWovQx-tZqWVui_hwLNLMWjP5SPDVGHdn9Uh-KWKRdu-fYqs3Bw6mU69MLAIKA8HWpzAigGxC-hnu6V8QQI-7Of5wYx18ugUmOJ45gRKZ78DkNW_4XVqEPkvNo32745ySXQw1tTZ3QJ9hwlyZ2dmiZErQE6PJnmucqfD5mLxyLZNS7VrkxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما خواستار محاکمه محسن نامجو و بیژن مرتضوی شد که به کشور برگشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/150462" target="_blank">📅 21:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150461">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
کانال ۱۶ اسرائیل: اسرائیل در حال حاضر هیچ نشانه روشنی مبنی بر ارتباط خلبان عمانی با ایران ندارد؛ این در حالی است که رئیس‌جمهور آمریکا، دونالد ترامپ، پیش‌تر چنین اظهاراتی مطرح کرده بود.
🔴
در حال حاضر هیچ اطلاعاتی که دخالت ایران را رد کند وجود ندارد، اما هیچ مدرکی نیز برای تأیید آن در دست نیست
🔴
تحقیقات در عربستان سعودی همچنان ادامه دارد، اما تصویر کامل ماجرا هنوز مشخص نیست؛ بخشی از این ابهام به دلیل آن است که مقام‌های سعودی تنها اطلاعات محدودی از روند تحقیقات منتشر می‌کنند.
🔴
موساد و شاباک نیز از طرف اسرائیل در این تحقیقات مشارکت دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/150461" target="_blank">📅 21:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150460">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/150460" target="_blank">📅 21:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150459">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/150459" target="_blank">📅 21:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150458">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSSW0VWOrjpREbIpJ3axRM7nCO6Age0YYMWoPYjZe5ibq5Dlltep__GWlsHyseHLyhL96KnJkOhc940TDu_geNProS8-4PZev7P0qKKRWy7yMrbTUnekA4WvIf5hofBtrgMIFuq1sHfXoxPY4XAkuTMGprEVaa9z4nCeQ5oWzrmCOe97uiefFUhQWdsyIpu0ijllG9Oiu6kzTwbub4Y80HwbeqBPtFFObeGAIAK0DKqz3ZQpy-dpQlOuaYKMJnnoU_YjBePcKFU3KKzx7WcTYh78EVWdut7WGIOhGdqpW-EYftbrdFxQL0BnsJvWrW90QAOohArvzaArvRG96eVqiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
من بارها اعلام کردم که برای از بین بردن تهدید هسته‌ای ایران، به ۴ تا ۶ هفته زمان نیاز است، و من این کار را در یک شب انجام دادم! بقیه زمان صرف این کار می‌شود که مطمئن شویم این وضعیت همچنان ادامه داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/150458" target="_blank">📅 21:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150457">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
پوتین: جهان از شجاعت و مقاومت ملت ایران شگفت‌زده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/150457" target="_blank">📅 21:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150456">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: تحریم های جدید ایران(راه آهن و خودروسازی) حامیان آن را هدف قرار داده و راه را برای خشک شدن منابع مالی این رژیم هموار می کند.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/150456" target="_blank">📅 21:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150455">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b62a7d15bd.mp4?token=B82S42P1-zwyO5mscLJzZcmZ1e-AqyrSpp5SEv_mufDQWBbaseYvWbjeiIl8WHrCKxx668C84r6KVl0CMkP3nktWnOfSI8z9sZiDuG5o7uzZCp9P4Qk5g-dk6cdCRe-tjB2UxebOaa7XRRH6-fZenu9VICy4C-dZaZsDLBgYt4BWB9OPzPuovSjTZrSkcBOOnPy9qUbtWnJoZif5wYsI4E2TfdoRSh-CW54jXnq144Mnh98JcGjOuKkyNjWahqb3HYi54HA-l-Eee4nGcvDkTdx-u3L6-GBOoIpEZ8ebHN-a6IQur_mt0_1rDXtyKfdYFcdgdxicIww59hfEJa0pTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b62a7d15bd.mp4?token=B82S42P1-zwyO5mscLJzZcmZ1e-AqyrSpp5SEv_mufDQWBbaseYvWbjeiIl8WHrCKxx668C84r6KVl0CMkP3nktWnOfSI8z9sZiDuG5o7uzZCp9P4Qk5g-dk6cdCRe-tjB2UxebOaa7XRRH6-fZenu9VICy4C-dZaZsDLBgYt4BWB9OPzPuovSjTZrSkcBOOnPy9qUbtWnJoZif5wYsI4E2TfdoRSh-CW54jXnq144Mnh98JcGjOuKkyNjWahqb3HYi54HA-l-Eee4nGcvDkTdx-u3L6-GBOoIpEZ8ebHN-a6IQur_mt0_1rDXtyKfdYFcdgdxicIww59hfEJa0pTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
میلی گلد این فیلمو از طلاهاش منتشر کرد و گفت دزد نیستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/150455" target="_blank">📅 21:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150454">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
پوتین: جهان از شجاعت و مقاومت ملت ایران شگفت‌زده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/150454" target="_blank">📅 21:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150453">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ترامپ: اگر ایران پشت آن حمله به هواپیما بوده باشد ضربه بسیار محکمی خواهد خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/150453" target="_blank">📅 20:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150452">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b0dca1ef0.mp4?token=iQ5SluAghWBLz8PLVlYPzh0QP_9YqMXIZhLRgClJ7-d8VBZVQxwr_sq4xEoD3R63L2s8a3Ry3YB1R4thtgQ4HO18Dh1jphIPoOuA3DZxk8Axwueblh2-LCyEE3n3Us_4-fkgD1JUlTb5Tb5zOa0XHMcI-pKK8tL-vxAnGAVl4pbf3YEB6OBhc2qviPzeKbkGJD0GnA1rpV1eMGWf5Ctyn0hH0sYFaNjJ_a1_tPFMLNWlHGG59q_Ec7OWjeAkkWXwBjeWkGzjCZIBYqGQTJwhi3kkWkilY3fS3C8oXorSEU85HUly8nyZVz8DG5jRNW0_Q0xvtjXGVYk-6vUABkXXaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b0dca1ef0.mp4?token=iQ5SluAghWBLz8PLVlYPzh0QP_9YqMXIZhLRgClJ7-d8VBZVQxwr_sq4xEoD3R63L2s8a3Ry3YB1R4thtgQ4HO18Dh1jphIPoOuA3DZxk8Axwueblh2-LCyEE3n3Us_4-fkgD1JUlTb5Tb5zOa0XHMcI-pKK8tL-vxAnGAVl4pbf3YEB6OBhc2qviPzeKbkGJD0GnA1rpV1eMGWf5Ctyn0hH0sYFaNjJ_a1_tPFMLNWlHGG59q_Ec7OWjeAkkWXwBjeWkGzjCZIBYqGQTJwhi3kkWkilY3fS3C8oXorSEU85HUly8nyZVz8DG5jRNW0_Q0xvtjXGVYk-6vUABkXXaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: وضعیت نیابت‌های ایران، مانند حزب‌الله، چگونه است؟
🔴
ترامپ: آن‌ها با ایران می‌روند، بنابراین نیابت‌ها نیز با آن می‌روند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/150452" target="_blank">📅 20:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150451">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ترامپ: من به دولت، اقتصاد و همه چیز نمره A+ می‌دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/150451" target="_blank">📅 20:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150450">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوری/ترامپ:  اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/150450" target="_blank">📅 20:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150449">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ترامپ: ما ذخایر راهبردی ملی خود را با نفت ونزوئلا پر خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/150449" target="_blank">📅 20:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150447">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e448c031e.mp4?token=q6QJvnVcepgYEC1KUUtkUorPMDmkZUcE9y3fEqyNbRZryTJ9_pnVJH7redohmopm8M-hzRBkE8DQil3ZFCJwM4D0Kcrr-DeLmpaWF4vD4eIX7HMTLo3x80hb9dumKY6sw235UMxvUqbsShHcNe-nBgFwOPuy198wEV-T0cxuiBcUslMONJ4O399XdjBROcEECEc7__aYQVtAIIfyceM2RDC78TCsNBJwayoFUaIe9zP_qrNQNQ_oWmhCrXLynJ3odpq-F1oqgB0E6APg8HJ86ar-yMNmW_4mYt5Eewt0ZHQkqbd0Pyriu4F10hlWLF58cxlgvAzFG-rK2oL7DKCyYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e448c031e.mp4?token=q6QJvnVcepgYEC1KUUtkUorPMDmkZUcE9y3fEqyNbRZryTJ9_pnVJH7redohmopm8M-hzRBkE8DQil3ZFCJwM4D0Kcrr-DeLmpaWF4vD4eIX7HMTLo3x80hb9dumKY6sw235UMxvUqbsShHcNe-nBgFwOPuy198wEV-T0cxuiBcUslMONJ4O399XdjBROcEECEc7__aYQVtAIIfyceM2RDC78TCsNBJwayoFUaIe9zP_qrNQNQ_oWmhCrXLynJ3odpq-F1oqgB0E6APg8HJ86ar-yMNmW_4mYt5Eewt0ZHQkqbd0Pyriu4F10hlWLF58cxlgvAzFG-rK2oL7DKCyYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/ترامپ:
اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/150447" target="_blank">📅 20:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150446">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
ام بی سی: مذاکرات به یک باره مثبت شده است
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/150446" target="_blank">📅 20:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150445">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ترامپ: مقدار نفت عبوری از تنگه هرمز در حال حاضر بیشتر از قبل از جنگ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/150445" target="_blank">📅 20:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150444">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
فووووری/ترامپ: ایران پذیرفته است که سلاح هسته ای نداشته باشد‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/150444" target="_blank">📅 20:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150443">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/150443" target="_blank">📅 20:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150442">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/150442" target="_blank">📅 20:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150441">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea51d61a8.mp4?token=EaNvfyO8Y7zC_Hg63YyX3UjWjUbxfearEiOh74GgHCr1zNh39eB88_q1U0wsXKItXioBK96s8IdAzhXiW92UaGx03jeABwF-nXCRddWeycI9GzBa0qCImZWBqs9Qniu29ep_3XlaMHPPP9fM_32onbcYKHNGw2ISw85kytzkPFOi4bltKViF_Y3LOOX5y8aGl3foX7LYbiUSogIlDCjzj5PdnQJGi081WrNOnSdRyFrKYEfvZmCV5oYbkhb_3utsQeflk86xZnS7qxFgSCMG0ocUL7czre5MvewxJPVdQocdALhLxmEvWSbgvEmvbJDPxcI6ewKp1-NWTE6XjYkQsWYSyf0qAMidB9xb8DRWOoTEkg7E0UvRRsIrxc7G-wYPj4GM68BF3XIp-MOek5J_31M8j7Zf_AOG8teLo9KFt1YoloWYL2v8UpettKHbJBmpxMZ0_JSUzGcsz7GATv9TFq1ZmsdGpzM6wOxop2ec7abclT7LUnHxIAjU91tO51fXaXFHy0g39fmvukqMkGpDROzeYUTdWpGU4XGRDq2CaZs6rroz06afyxYuKRY25-AaWrbWBIDbC01qSwRrc-MEGlXHbRFjwyOwmh6dvHSqxN3JxtIvBPkgt5qfB2c4QQOl6v8sFoInlO5k95lE6PO9CiWWTWOzzxeor566rwe9wUc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea51d61a8.mp4?token=EaNvfyO8Y7zC_Hg63YyX3UjWjUbxfearEiOh74GgHCr1zNh39eB88_q1U0wsXKItXioBK96s8IdAzhXiW92UaGx03jeABwF-nXCRddWeycI9GzBa0qCImZWBqs9Qniu29ep_3XlaMHPPP9fM_32onbcYKHNGw2ISw85kytzkPFOi4bltKViF_Y3LOOX5y8aGl3foX7LYbiUSogIlDCjzj5PdnQJGi081WrNOnSdRyFrKYEfvZmCV5oYbkhb_3utsQeflk86xZnS7qxFgSCMG0ocUL7czre5MvewxJPVdQocdALhLxmEvWSbgvEmvbJDPxcI6ewKp1-NWTE6XjYkQsWYSyf0qAMidB9xb8DRWOoTEkg7E0UvRRsIrxc7G-wYPj4GM68BF3XIp-MOek5J_31M8j7Zf_AOG8teLo9KFt1YoloWYL2v8UpettKHbJBmpxMZ0_JSUzGcsz7GATv9TFq1ZmsdGpzM6wOxop2ec7abclT7LUnHxIAjU91tO51fXaXFHy0g39fmvukqMkGpDROzeYUTdWpGU4XGRDq2CaZs6rroz06afyxYuKRY25-AaWrbWBIDbC01qSwRrc-MEGlXHbRFjwyOwmh6dvHSqxN3JxtIvBPkgt5qfB2c4QQOl6v8sFoInlO5k95lE6PO9CiWWTWOzzxeor566rwe9wUc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین
رهبری شوروی سابق را به ساده‌لوحی، خودرأیی و اعتماد کورکورانه به غرب متهم می‌کند و می‌گوید که این عوامل به فروپاشی اتحاد جماهیر شوروی منجر شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/150441" target="_blank">📅 20:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150440">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87899a96b.mp4?token=U99QAs7-hMapaHycWIT5eJnpRCwbX2q2xYN1M-qN0nA4x9h3POhZeNyAml_oiswwRf3IKjDHRw3wOZpWy0M9E_dHBdC3VYBrnQD69ZemMkilQl52dbAGmER1mkIaxH_r2LeNpCYm-kyAr_RvD1OOzIaSiEOw3D_kyXQ5A6JXcX4f6r4ncV8H35QZ0FnVO7yJk_YK5QOrbm9XKoj2tDCh7LHgfFsrkAw3JeXEXfmU5XWxw5tI0bpaILCaC7-6MO0BoAIe6i40PD93ymE9z4NxDaaietjYHpT3nbpK6jcQCIVaW03KjJ-xbcv0F33sqNbNsX5iXptPa_q_fHuD4Fq0Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87899a96b.mp4?token=U99QAs7-hMapaHycWIT5eJnpRCwbX2q2xYN1M-qN0nA4x9h3POhZeNyAml_oiswwRf3IKjDHRw3wOZpWy0M9E_dHBdC3VYBrnQD69ZemMkilQl52dbAGmER1mkIaxH_r2LeNpCYm-kyAr_RvD1OOzIaSiEOw3D_kyXQ5A6JXcX4f6r4ncV8H35QZ0FnVO7yJk_YK5QOrbm9XKoj2tDCh7LHgfFsrkAw3JeXEXfmU5XWxw5tI0bpaILCaC7-6MO0BoAIe6i40PD93ymE9z4NxDaaietjYHpT3nbpK6jcQCIVaW03KjJ-xbcv0F33sqNbNsX5iXptPa_q_fHuD4Fq0Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بیژن مرتضوی
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/150440" target="_blank">📅 20:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150439">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ul51jlZwxvpr98lJvRH2j7XriQd2kEct-HCEHubPCBFvxwG9pg69jckz1tMatoTzUGVml8yzpFPp9W17_gYLdyk0mGBGg8ut5wg95elAL6sfsFk_9DiXFGhJvHzGjQ7AJGKvQpfaQWwSIWcsHptdSUyDDt5WyLwRzq1Bmp_hv2Gct_cobnmhTE9hsXXpp8TV_Ev1yXjVE0sB5SEQg4zqnXmKXXJDkTgM-9XSdKAV3CJR0TpyGQfRtQ81a1EniLGUKPWuxXfBlbmke6uEBR98fU9iwvzIAQZ05L5iD0JfCCzFAVqMJDz1al9ipUfy69fY4S9Rprokv5f2zMDFODttPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست وزیر اسرائیل بنیامین
نتانیاهو می‌گوید کودکان غزه از شیر مادران خود کینه می‌مکند
نتانیاهو گفت که کینه‌ی یهودیان از دوران نوزادی در غزه درونی می‌شود، در حالی که او اسرائیل را در جنگی علیه گولیات «بنیادگرایی اسلامی جهانی» به عنوان دیوید ترسیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/150439" target="_blank">📅 19:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150438">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
پوتین:
در صورت حمله مستقیم به روسیه یا کالینینگراد، استفاده فوری از تمام سلاح‌ها مطرح می‌شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/150438" target="_blank">📅 19:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150437">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAnmXKj2i3PIXYQigQaeinOYvEvlWVdGKXJR5aAdYU1RhfSS_QeW8TReUo8bxD1MCI4LDsLD3_535d8fAuTo_C1nUYT9QwiwueujgIPaI2wlmfSEIyt29HBhx_uhKyhuAIiWtfthqh6V02MzAy_w0k8x_wKkdUDN4IQ5el0-wYfL_2ttc7P2Qra3TNjrwohcWszI9H1LpPNpzjAOI8ePX_t3n09fGbTGAgKDz4Uvwwohj1Y9DFaEB_NsaUjaC8XN55FlYbNDn9EibD9URIJQd9CvVy2j_Fr-AqoVmhEUOZacKK1vuMNDgInCZzqpCVQ7aksraLq2DJ3Qz04REt65Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز سوخت‌رسان آمریکایی در آسمان امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/150437" target="_blank">📅 19:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150436">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34eeb2e93.mp4?token=Jt8X0VvdYMaAg6Ise_mzwQkBSZoS4aGJLAXOEAWOu9RSAlgC_jWDqCF45xcg2VjOeG60Sf8JRS9Ir1C7wSO8zYGbFzuDumeNF6LlQGlGWCYkluHZIiEB5-jO2N-nuSUFd8GbCqBklzY7e07BqHukkJvqyAU6obdfHMAQ59etLn_X5c3A781OZve2eRm7Uc4p-l7ltHzPMYTHShwB8y1t5SNueVxvU5CgJVNmJK9MExQWRDU-Md1BFliZl7ZiOGFzJQG-AHW1FU6jH1WzTEYjMyBGV3dcGaN-SH9fUwiPO_kfZZa2kGHV_BMxYnkAcQNE55vJhagk-wdrDY4Wi7yscw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34eeb2e93.mp4?token=Jt8X0VvdYMaAg6Ise_mzwQkBSZoS4aGJLAXOEAWOu9RSAlgC_jWDqCF45xcg2VjOeG60Sf8JRS9Ir1C7wSO8zYGbFzuDumeNF6LlQGlGWCYkluHZIiEB5-jO2N-nuSUFd8GbCqBklzY7e07BqHukkJvqyAU6obdfHMAQ59etLn_X5c3A781OZve2eRm7Uc4p-l7ltHzPMYTHShwB8y1t5SNueVxvU5CgJVNmJK9MExQWRDU-Md1BFliZl7ZiOGFzJQG-AHW1FU6jH1WzTEYjMyBGV3dcGaN-SH9fUwiPO_kfZZa2kGHV_BMxYnkAcQNE55vJhagk-wdrDY4Wi7yscw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش یک بلاگر به صحبت سخنگوی دولت درباره کالابرگ و پفک
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150436" target="_blank">📅 19:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150435">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtT5nkTS63WTi0HvbPeVN_puH0WExJjpHiIJsxyPo2VZIU5dXYsQzwvCZlA4BWnTrya9bFH-MUNQ67SRRadBdmOgO_KS6ffy7KzXreMiA8o2tP65RQ0A0ACrH4vqnrCvfZVOaJF3Siz8U7Ja0wdiUPenVqE6qhuz90JfuVeP6AShd_0Q3iGLyi-ZEdC5k9XzK3BoAyfv39VbSEfEWgn9OdEAWxHs27hhBLJJLr0iTDcwY_H1c3YTUZa7h43HLVneGY3yPQZuhky1ldq4aMdIzKIybizDPLnoQrwvJrNVy6GkfPLFJy8mf2LA3wohC4rayD-qIPhFzgOXiG5V6tBEdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت با ۳.۷ درصد افزایش از ۱۰۱ دلار عبور کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/150435" target="_blank">📅 19:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150434">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
۱۲ فروند اف-۳۵ از انگلیس به آمریکا برمی‌گردن
🔴
حداکثر ۱۲ فروند اف-۳۵ از پایگاه لیکین‌هیت انگلیس به آمریکا برمی‌گردن. برای این انتقال چند هواپیمای سوخت‌رسان هم ثبت شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/150434" target="_blank">📅 19:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150432">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
بلومبرگ:
ایران سپتامبر هیچ محموله نفتی بارگیری نکرد
🔴
بلومبرگ نوشته که ایران تو ماه سپتامبر حتی یه محموله نفت خام رو روی نفتکش‌ها بار نکرده. این یعنی محاصره دریایی آمریکا دسترسی ایران به بازارهای انرژی رو خیلی محدود کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/150432" target="_blank">📅 19:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150431">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noiOdxsTKzmtTUoBW8U0T1kkNUpzfUco5VbAtr5KFYQQ81uuevcv04_tWyEFkqF4RMmwzeo148KJ0dAkzV_nFYzF07hvr0whsVQ7yiLNqoCuSDQBU45MrtnyHU5TXbULRNm2m0sGizWUh6WDBcl-zsbfTHaiilKyxTIoNW00JXsWB-O5ACoW6OdeD54aLF59SEpB4UZ4IjmCekjrHMvyVlnBIAvQlccmdGzkEcgFMw1FLj2qznl527wgMPaKMCajr7klAepBnEd_W6gOjD9ivBSN4gWHbqS3p-ritWEA8U6BQ8vB4HBcj0ShTXhfyhwB8b3MrE-oppXBWzA3a0e6pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طالبان: تحریم هوایی ایران رو قبول نداریم
🔴
طالبان اعلام کرده تحریم هوایی ایران رو قبول نمی‌کنه. این گروه گفته چنین محدودیتی رو به رسمیت نمی‌شناسه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150431" target="_blank">📅 18:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150430">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c00080542.mp4?token=UnddqB5n6LFNzkuWPVVaHlvNzQ17PjQFl23J6euP21vVfQmSIgAG-JhgW_jfM-cMkgCNBYxRzpH_bduOFQ0TZQI_WnuSZU5SEHYLWcBLSFO59E3UzJscOkTvUKtTuIB8nP5k-rs0ftBHurSlQnjzu6kt_lLKOIbyxASqiVJBgem38NUW0LCsZb2npG7gmJPQK712pKOCDuagY1IJZs0DNthYFQsR79D8xeXLC0x0tGxnDNcOGjV7kM8swiZ7zqgBGzTrVDy6ba1dnCj5_Q7ENK2YAtSvbIytFhg5xt2nzBOJcmf4afy_uAqN6FgflM5DFper1Yby9HiXUFAxExg4MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c00080542.mp4?token=UnddqB5n6LFNzkuWPVVaHlvNzQ17PjQFl23J6euP21vVfQmSIgAG-JhgW_jfM-cMkgCNBYxRzpH_bduOFQ0TZQI_WnuSZU5SEHYLWcBLSFO59E3UzJscOkTvUKtTuIB8nP5k-rs0ftBHurSlQnjzu6kt_lLKOIbyxASqiVJBgem38NUW0LCsZb2npG7gmJPQK712pKOCDuagY1IJZs0DNthYFQsR79D8xeXLC0x0tGxnDNcOGjV7kM8swiZ7zqgBGzTrVDy6ba1dnCj5_Q7ENK2YAtSvbIytFhg5xt2nzBOJcmf4afy_uAqN6FgflM5DFper1Yby9HiXUFAxExg4MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پور علی: دو شب پیش رهبری نیم ساعت در تجمع شبانه حضور داشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/150430" target="_blank">📅 18:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150429">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/354527fcb7.mp4?token=JxrxNf-o6_L6YBrjy0Wnf2w4UZH-EO-72FX62NAKPYIjLIJ_EDrlkJV60SnDFSQB5pFg5Hlz1k2B25FEawzoqE9jzGi7IN_p51iTok14LlTlTHOY0cXfHwFHZ7ZcW6FIihpl79ybw7Yt7hQq8d_4YdVJaagtLEkOeK7-5sFEFG_S8a7WFYMi_9ps18SgnYFkrQYMuDUf4ly_xaI7tEUOdeCCeCEkXO312YBM9t7qfrsJevpefWl9S2ZfNR4Q3EUroxmo2f4I19SreYnIgTdv80ncuxqEQm35ZZO_Gvpn3jDtn3PFrpBZIVyDkr7q0Oi9LOLTyTNA7epuG4ubTrpEZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/354527fcb7.mp4?token=JxrxNf-o6_L6YBrjy0Wnf2w4UZH-EO-72FX62NAKPYIjLIJ_EDrlkJV60SnDFSQB5pFg5Hlz1k2B25FEawzoqE9jzGi7IN_p51iTok14LlTlTHOY0cXfHwFHZ7ZcW6FIihpl79ybw7Yt7hQq8d_4YdVJaagtLEkOeK7-5sFEFG_S8a7WFYMi_9ps18SgnYFkrQYMuDUf4ly_xaI7tEUOdeCCeCEkXO312YBM9t7qfrsJevpefWl9S2ZfNR4Q3EUroxmo2f4I19SreYnIgTdv80ncuxqEQm35ZZO_Gvpn3jDtn3PFrpBZIVyDkr7q0Oi9LOLTyTNA7epuG4ubTrpEZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دلار 260 هزار تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/150429" target="_blank">📅 18:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150428">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFofbmr6S3sF4r8fgSsOHFbKfmaNSshQRn56bRV5S1frWsShsMdWctLDmJR3jvP7e2BOKGytXMFiPLI37CWMqX0THHmrnJicmvDPoqHr7gQCKqjPt_FRrUa-z-b2Bo_md_n9Mjq-xDKH6CcmEZv3ezdfm_dclwEh9E4b8cO-SW5N2LxzKeSTaNAC6UUEyGtxplN-RzNwIEORKDqUaJ7E9TpJthnUh6zTKjxicbRbwCQ9mu9VMwlopVCwH5E4WNdVFJ6s3kjinIbP7lywKwqJBgfsG-RTMgs3R_ADYml5xGFznMZVds2t0PjmHqkTplO6CpJe9ylcfdzvTspPHh1g4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل (IDF):
ارتش اسرائیل دو تروریست را که در جریان کشتار ۷ اکتبر وارد خاک اسرائیل شده بودند، به هلاکت رساند: یکی از این تروریست‌ها در جریان کشتار ۷ اکتبر وارد کیبوتص بئری شد و در ربودن شارون هرتسمن-آویگدوری، نوعام آویگدوری، عدی شوهم، نِوِه شوهم، یَهَل شوهم و شوشان هاران مشارکت داشت
ارتش اسرائیل اوایل این هفته (سه‌شنبه) در منطقه شهر غزه حمله کرد و محمد جمال محمود ابوالشاعر، فرمانده یک تیم در شاخه نظامی سازمان تروریستی حماس، را به هلاکت رساند.
این تروریست در جریان کشتار ۷ اکتبر وارد کیبوتص بئری شد و در ربودن شارون هرتسمن-آویگدوری، نوعام آویگدوری، عدی شوهم، نِوِه شوهم، یَهَل شوهم و شوشان هاران و انتقال آن‌ها به نوار غزه مشارکت داشت.
در حمله‌ای دیگر در این هفته (سه‌شنبه) در منطقه جبالیا، ارتش اسرائیل مصعب عبدالغلیل ثاقب بلابیسی، فرمانده در شاخه نظامی سازمان تروریستی جهاد اسلامی فلسطین، را به هلاکت رساند.
این تروریست در جریان کشتار ۷ اکتبر وارد خاک اسرائیل شد.
اخیرا، این تروریست‌ها در حالی که به‌طور سیستماتیک آتش‌بس را نقض می‌کردند، طرح‌های تروریستی علیه نیروهای ارتش اسرائیل و شهروندان اسرائیل پیش می بردند. این تروریست‌ها از هوا و با هدف رفع تهدیدی که ایجاد می‌کردند، به هلاکت رسیدند.
پیش از انجام حملات، اقداماتی برای کاهش آسیب به غیرنظامیان، از جمله استفاده از مهمات دقیق و رصد هوایی انجام شد.
نیروهای ارتش اسرائیل تحت فرماندهی جنوب، مطابق با توافق در منطقه مستقر هستند و به فعالیت برای رفع هرگونه تهدید فوری ادامه خواهند داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150428" target="_blank">📅 18:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150427">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmASi5t4JyWJKuEUD4dyLIWRWDHhiGwCvdLFosc9AV2-coTHzoftd63U7dUrpPJjYQPZYMtE3AHS4xiORU78bCaH7L5ZS1NcF11aJxirLwtX3YMROcpLDCe-8_dykCp7sjnYcMHh8iNKyYkSVwSMVSQQpZvwVG64RXvacHtYhyT1DMjYj7dUINVykez2G1Wu4DVVTrQeq9unYVtO7Oz4pjtPZhEEFl7uKK7x5AOSq3lLGBM0SQzqVwFYuADegrutOwFZ6Kapv6CV5fQFP3BSyCMrYNKSOpQCh0-JeZXYreunLvHfgzJQ4KlXkLVCrCY-QDIRo9GfPbYHG9mqFoNbPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیژن عبدالکریمی: وضع مردم خوبه و کباب بازی میکنن و هر روز هم کلی خرید میکنن، هرکی میگه اینجور نیست دروغ میگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150427" target="_blank">📅 18:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150426">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe2519fac2.mp4?token=rPicb6O8psf8EZ9Fayq48l21-kG7cjgIUqnp2C1103hQj_HWKGG616xE8gAxAcME5n55-SoX0X6MdjTFutB9AMD8eONo7qGJzBTZwB0Pqi7zkfhUHJ_SgAVxdY4k3WJPG9n8zt7VLd7UjuFbCDMRYfXSHym-e5zW035QCH-9o09VUhHPkcE5vH1STNy_fExrzm1BDNgo5QXgUBcjw7gqABI9_1K2R_6hFWCpPcTRGZAreLLiUWlavo-do3618VKFskBdqQALrbboyMeaeeycV4wJtZxVq9iNFYGjgbIF2Um2ko1Bf8IBI_6r1LHtakTKQ584znt79WkAfKGsFveRFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe2519fac2.mp4?token=rPicb6O8psf8EZ9Fayq48l21-kG7cjgIUqnp2C1103hQj_HWKGG616xE8gAxAcME5n55-SoX0X6MdjTFutB9AMD8eONo7qGJzBTZwB0Pqi7zkfhUHJ_SgAVxdY4k3WJPG9n8zt7VLd7UjuFbCDMRYfXSHym-e5zW035QCH-9o09VUhHPkcE5vH1STNy_fExrzm1BDNgo5QXgUBcjw7gqABI9_1K2R_6hFWCpPcTRGZAreLLiUWlavo-do3618VKFskBdqQALrbboyMeaeeycV4wJtZxVq9iNFYGjgbIF2Um2ko1Bf8IBI_6r1LHtakTKQ584znt79WkAfKGsFveRFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امیرحسین شریعتمداری، فرزند محمد شریعتمداری، وزیر اسبق بازرگانی و مدیر فعلی ابرهلدینگ خلیج فارس، خواننده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150426" target="_blank">📅 17:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150425">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
پزشکیان :
هیچ‌گاه از گفتگو فرار نکرده‌ایم و نخواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/150425" target="_blank">📅 17:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150424">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7chVT2AmdEp-dmAPNe1W04eZlpl8o3Oy8VkS2S41UQD2SK-rfRP6TaRRM4kqCdjuV4olxcJrJLP4dsg3OGPAijGbWKXdU31y6ZgYf5QqzjWg-aZl-1u0SvXutvjgz8-zoP7-kxp5J5N75i-C5CHN0hwCs6SaHhjU3lacSpbCqtLB_waoea91qSNk91vP6V6Eza24eIzB3eqtw8d1nA2qT5qVTZzUFBXgiiqWiFpbcDb7H-xoqTjksyffM1WsiL06BsIo_A1dwRoSOh4mRHsgVvFLjUpJk41igFsXr-TilLGPd0qFFPhrDKP1xGtmd2YNETqYu8R5p86pzp4cy9tpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا قراره بیژن مرتضوی تو یکی از تجمعات شبانه ویالون بزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/150424" target="_blank">📅 17:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150423">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1wJrje4ON95LryVkNYsz6tN_LzIoMM5NA6LQamC1BoJjwBZHqdFIM5RF3uuYuv976Smd3JnjozQ7tsA3QHu3HfUis-LPOroauC3NQiSC-4ivWW4d9VeM-Ie4WwyfVZxtpYWb7vQhSuskrbrJmXjtYZb-DG4p9_2dMF5YV8xbTWE2yGg76zH94iBomAVN7HxCMGeAZ_KkfPRn0YvRobPY-9Vzp58W4lm6E9JBV9AWHCFgkflCAjm5eOEi6S0CHdD6jI-xPDDGUJ_cEZEfDK3eCAhan4EUD1Pw5p6rbkjFWdhjf_C2BY5zUT7KI4QOFdBu9TZPd3b1kYXq6Fhbf5Lhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر خروج آخرین نظامی و جنگنده ارتش آمریکا از عراق
🔴
شبکه فاکس نیوز همزمان با تکمیل عقب‌نشینی نظامیان و تسلیحات و جنگ افزارهای ارتش آمریکا از عراق و پایان ماموریت موسوم به عزم راسخ، تصویر خروج آخرین نظامی و جنگنده آمریکایی را منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/150423" target="_blank">📅 17:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150422">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
رسانه های عبری: امارات تحقیقات درباره حادثه پرواز «فلای‌ دبی» را آغاز کرده
🔴
کمک‌ خلبان عمانی که مظنون به تلاش برای سرنگون کردن این هواپیما است، برای بازجویی به امارات منتقل خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150422" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150421">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43b4c69e6e.mp4?token=A3UQR4dAeyY03rD5JB0HAurKFlzPwePswWjz1DcZjnjWVExxMRn4KE1K4ICKK1dk-R0QhsYMMaVdBDlWenKiJdHuTUG4FVnbQ-o2tORIc-xEREEhHObbXpd_BXSKrkrAZFxleIgLhj5roBy99SSni9v21eGrc5K58aThxufNy2B9NZRQGrlXZgAjr79okHWt2XW8y-cwPN0OrVRcH7UZ5kE7oNvhyj82hO03K0kQaJUh8t0fJcNtVTCG2_eE6X7fhtfO4nRciWKt7dAPmLReg9QcPhLJzPMASG3HfGqgL3oGH_3nrGfYiMg4CyMymY-o8kjbhJw_PhOifXXY6aThZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43b4c69e6e.mp4?token=A3UQR4dAeyY03rD5JB0HAurKFlzPwePswWjz1DcZjnjWVExxMRn4KE1K4ICKK1dk-R0QhsYMMaVdBDlWenKiJdHuTUG4FVnbQ-o2tORIc-xEREEhHObbXpd_BXSKrkrAZFxleIgLhj5roBy99SSni9v21eGrc5K58aThxufNy2B9NZRQGrlXZgAjr79okHWt2XW8y-cwPN0OrVRcH7UZ5kE7oNvhyj82hO03K0kQaJUh8t0fJcNtVTCG2_eE6X7fhtfO4nRciWKt7dAPmLReg9QcPhLJzPMASG3HfGqgL3oGH_3nrGfYiMg4CyMymY-o8kjbhJw_PhOifXXY6aThZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، نخست‌وزیر اسرائیل درباره عمان: سلطان قابوس فقید، رهبر عمان، چند سال پیش از من دعوت کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150421" target="_blank">📅 16:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150420">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
پزشکیان: عده‌ای کنار گود نشسته‌اند و می‌گویند لنگش کن
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/150420" target="_blank">📅 16:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150419">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
دونالد ترامپ در مصاحبه‌ای با مجله تایم:
هزینه‌های مربوط به جنگ ایران برای ما کمتر از درآمدی است که از نفت ونزوئلا در یک ماه به دست می‌آوریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/150419" target="_blank">📅 16:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150418">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: تحریم‌های اعمال‌شده علیه ایران یکجانبه هستند و از سوی شورای امنیت صادر نشده‌اند؛ بنابراین به تجارت خود با تهران ادامه خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/150418" target="_blank">📅 16:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150417">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
پرزیدنت ترامپ به مجله تایم: اگر به سوئیس می‌گفتم: «متأسفم، نمی‌خواهم سالانه ۴۰ میلیارد دلار ضرر کنم تا ساعت‌های شما را داشته باشم»، ما همین حالا ۴۰ میلیارد دلار کسب کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150417" target="_blank">📅 16:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150416">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
نتانیاهو: ما می‌دانیم که خلبان مهاجم، تحت "فرآیند آموزش و تلقین افراطی اسلامی" قرار گرفته بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150416" target="_blank">📅 16:24 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150415">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
نتانیاهو: اگر سلطان قابوس زنده بود، عمان به توافق ابراهیم می‌پیوست
🔴
بنیامین نتانیاهو درباره عمان گفت: «سلطان قابوس فقید چند سال پیش من را دعوت کرد.»
🔴
او افزود: «مطمئنم اگر سلطان قابوس زنده بود، یک شریک دیگر در توافق‌های ابراهیم داشتیم.»
🔴
نتانیاهو درباره حکومت کنونی عمان نیز گفت: «حکومت جدید موضعی سرد و فاصله‌دار دارد، بنابراین هنوز نمی‌توانم چیزی درباره آن‌ها بگویم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150415" target="_blank">📅 16:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150414">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
پزشکیان :  هیچ‌گاه از گفتگو فرار نکرده‌ایم و نخواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/150414" target="_blank">📅 16:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150413">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ترامپ به مجله تایم گفت: من آی‌کیو بسیار بالایی دارم. بالاترین هوش را دارم. من خوبم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150413" target="_blank">📅 16:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150412">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6rL1w948HftpWabC9SZBKOJ9IqXQa6c4WPubV7LS-uY7tMn2vNmCsVK-O6m6CBJeBZHYFmoW-IzGWmBok2CmchJGXDpVtzCIqQfUtNemEhiTsTopBdnmQ4XKCp9YiVqCzqVM3qVgUIXDlVxEFYMiFHCzm1wsUE3rK55PbD3jmHgWSiGrI0tyoTy2jv8o4ksvgfyks7FqxUhY_S5ucljG89xgGXpBIaC30xml-_7CzrZ7R5JBo96lspGJePdLkDyXInJw7CJGqyTtBW1MTlcJ63BDoNET2qT8YagbvZzzOassB-y3mRMM9jVzMUD0nqP0unjufb1DjJGIKz69E5X9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اختلال‌ها بار دیگر به فرودگاه ریاض بازگشته است؛ 10 هواپیما در انتظار مجوز فرود هستند و در نزدیکی فرودگاه به‌صورت دایره‌ای پرواز می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/150412" target="_blank">📅 15:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150411">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
دونالد ترامپ با روزنامه تایم: خبرنگار: آیا در نظر دارید که قبل از پایان دوره ریاست‌جمهوری خود، اعضای دولت خود را مورد عفو قرار دهید
🔴
دونالد ترامپ: بله، قطعا این کار را خواهم کرد؛ جو بایدن که به خواب علاقه زیادی دارد، برای همه عفو صادر کرد؛ من بالاترین ضریب هوشی را دارم. من بالاترین را بین همگی دارم و بسیار خوب هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/150411" target="_blank">📅 15:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150410">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ: تهدید بسته شدن هرمز را می‌دانستیم؛ ایران اکنون توان سابق را ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/150410" target="_blank">📅 15:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150409">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ترامپ: پیشنهاد ایران برای باز کردن هرمز «تقریباً کافی» بود، اما نه کاملاً
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150409" target="_blank">📅 15:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150408">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ترامپ: نظرسنجی‌ها جعلی‌اند؛ هر رقیبی را با اختلاف ۲۰ درصد شکست می‌دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150408" target="_blank">📅 15:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150407">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ترامپ: بایدن حجم عظیمی از مهمات آمریکا را در اختیار اوکراین قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150407" target="_blank">📅 15:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150406">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ترامپ: فکر نمی‌کنم نتانیاهو پیش از حمله ۷ اکتبر هشدار دریافت کرده باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150406" target="_blank">📅 15:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150405">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ترامپ درباره زهران ممدانی: او را دوست دارم، اما سیاست‌هایش دیوانه‌وار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150405" target="_blank">📅 15:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150404">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ: اگر من رئیس‌جمهور نبودم، امروز عربستان و اسرائیلی وجود نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150404" target="_blank">📅 15:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150403">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ درباره طولانی شدن جنگ با ایران: خودم خواستم جنگ را ادامه دهم
🔴
خبرنگار تایم از ترامپ پرسید: «ابتدا گفته بودید جنگ ایران حدود شش تا هشت هفته طول می‌کشد؛ اکنون وارد ماه هفتم شده‌ایم. چرا جنگ این‌قدر طولانی شده است؟»
🔴
ترامپ پاسخ داد: «فقط به این دلیل که می‌خواستم جلوتر بروم. آن‌ها را از میدان خارج کردم و همان زمان می‌توانستم جنگ را متوقف کنم، اما می‌خواستم ادامه دهم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/150403" target="_blank">📅 15:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150402">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ: دیشب بیشترین مقدار نفت را از طریق تنگه هرمز منتقل کردیم، بیش از هر زمان دیگری.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/150402" target="_blank">📅 15:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150401">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ: دیشب بیشترین مقدار نفت را از طریق تنگه هرمز منتقل کردیم، بیش از هر زمان دیگری.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/150401" target="_blank">📅 15:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150400">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ: ما سلاح های زیادی داریم و وضعیت ما عالی است. ما اکنون مقادیر زیادی را ذخیره و نگهداری می کنیم و آنها را بین متحدان خود توزیع خواهیم کرد‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/150400" target="_blank">📅 15:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150399">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ عملا گفت که تا انتخابات میان دوره‌ای فرصت توافق هست
🔴
حدود ۳۰روز
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/150399" target="_blank">📅 15:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150398">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ: با نابودی ایران، صلح را در جهان برقرار می‌کنیم
🔴
خبرنگار تایم از ترامپ پرسید: «هفته گذشته گفتید ممکن است ایران را نابود کنید. آیا همچنان چنین احتمالی وجود دارد؟» ترامپ پاسخ داد: «بله، این کار را می‌کنم؛ ممکن است.»
🔴
خبرنگار پرسید: «چطور رئیس‌جمهوری که خود را رئیس‌جمهور صلح می‌داند، از نابودی یک ملت سخن می‌گوید؟»
🔴
ترامپ پاسخ داد: «چون با نابود کردن ایران، صلح را در جهان ایجاد کرده‌ایم. فکر نمی‌کنم با وجود ایران هرگز بتوان صلح داشت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150398" target="_blank">📅 15:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150396">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ: ایرانی‌ها پیشنهادی برای باز کردن تنگه هرمز ارائه کردند. من برخی از جنبه های آن را بررسی کردم، اما نه همه آن، اما به سادگی کافی نیست.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/150396" target="_blank">📅 15:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150395">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ترامپ درباره رد آخرین پیشنهاد آتش بس ایران: آنچه را که یک سال پیش رد کردم، امروز با آن موافقت نخواهم کرد.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150395" target="_blank">📅 15:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150394">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol4PKXD9BWQiy0NjZAyDQdHnqjD_0NqwP4TeSvpn5btZjDWmjU5KgTY7ccWndinx7v9PzfqCpBEXJB_D9_AZNsIz570HS-XObhFewTQ62ylH8CSfu6tva0J3dQshmnKLOoSQ-yE-YGLR63J0O7H1SkezNmnjunqMKe4QDmX5SsMzRQIblutCsvstTOWKIOZCemo5QoC6tPso6LnbgT8JnRL6glmu0ua9_TsB78pCs0Du3ucUdoo7HYv6CsZ3fJULI5BhcBYuda37AqJUnoXkJqzp-EvhepiuHvKkxSMs0gsz9Jk5wFQuDLbU4KZG2JYp6SilEjYPaGZFrsiX6k5cCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت فلای‌دبی اعلام کرد که به طور موقت پروازها به تل‌آویو را متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150394" target="_blank">📅 15:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150393">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
تایم: ترامپ احتمال افزایش حملات هوایی به ایران پس از انتخابات میان‌دوره‌ای را مطرح کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150393" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150392">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
لحظاتی پیش سکه طلا از رقم بهت آور 260 میلیون تومان عبور کرد
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150392" target="_blank">📅 14:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150391">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ایلان ماسک به پنتاگون در طراحی و بررسی جنگ‌های آینده کمک می‌کند
🔴
«پیت هگست»، وزیر دفاع آمریکا، خبر از آغاز پروژه‌ای داد که چگونگی جنگ‌ها در آینده و تأثیر پیشرفت سریع فناوری‌های نظامی را در آن‌ها بررسی می‌کند. «ایلان ماسک» به‌همراه بنیان‌گذار کمپانی آندوریل و رئیس پیشین مجلس نمایندگان آمریکا این پروژه پنتاگون را رهبری می‌کنند.
🔴
این طرح «پروژه مریدین» نام دارد و پیت هگست مأموریت آن را بررسی «میدان‌های نبرد آینده» و سلاح‌ها و فناوری‌هایی توصیف کرد که نیروهای نظامی ممکن است در آن میدان‌ها استفاده کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150391" target="_blank">📅 14:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150390">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
بن‌گویر ،وزیر امنیت ملی اسرائیل: در جلسه کابینه امنیتی خواستار تحویل گرفتن خلبانی خواهم شد که قصد هدف قرار دادن صدها اسرائیلی را داشت؛ او در زندان‌های ما با تمام وجود معنای سیاست‌های مرا خواهد چشید، چرا که در اینجا جهنمی واقعی در انتظار اوست
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150390" target="_blank">📅 14:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150389">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
بدرالسادات عراقچی، خواهر عباس عراقچی در گذشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150389" target="_blank">📅 14:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150388">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmFi3eY_CH1tXJS_WCcdUBvyHkNrH-9avTt8D3PDz2AbJ8NP1ZBvLlub12v4bWjmaPwdZVCtVVLfwsS05KBlshxZrFnZm_bnU_OEqm-6dri-tLwxQhb35bCuE_JQcAj3dWJHkJzfRWOaEB77KTCblHYW47W4k-0Eys5QLJv7AI1Rg0nbFcD0eHYrbXO64LC9SzjEdIU2LXyx8BmQ3neD2PEBk4cYzd7x1Afr_TZJwZqKaU55qQQdo11ij5pRSPES4WAq_4DYJY1Y1GldDedmYQhjRhT3pMShph5SSJIA0m3dloiTjx-m7UQ7ids5nZFJh_1zr2Li_SNeDeqSgFlXHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیشب در بازی دوستانه بین کونیا اسپور و تیم ملی فلسطین در اقدامی عجیب بازی رو دقیقه 89:59 متوقف کردن و گفتن بقیه بازی رو وقتی انجام میدیم که فلسطین آزاد بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/150388" target="_blank">📅 14:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150387">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
لحظاتی پیش سکه طلا از رقم بهت آور 260 میلیون تومان عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150387" target="_blank">📅 14:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150386">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
اکسیوس: روبیو پس از بن‌بست در مذاکرات، روز دوشنبه از هیئت ایرانی حاضر در سازمان ملل خواست آمریکا را ترک کنند
🔴
منبع آگاه: عراقچی از قبل قرار بود دوشنبه به تهران برگردد
🔴
قطر همچنان در حال گفت‌وگو با هر دو طرف درباره پیشنهاد مصالحه‌ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/150386" target="_blank">📅 13:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150385">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
نایب رئیس مجلس نیکزاد: آمریکا هرگز نمی‌تواند صادرات نفت ما را به صفر برساند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/150385" target="_blank">📅 13:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150384">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlj-khDZWCUJTk3PuOMxfcoC2TiZPflxzdU6Xl4SSCi0NvHzuMzPiQGfZ2KH93NgDkQZpHYHezDhQ2i25vPMXcwYhzw2PBrpFt8mnseF1Iaa6TGr97FN5_xCiBpn4ZHAtxj386Y1GNQc015rpT7n670V3Oxb5_kFyKhNBVFne7Ood6BKwAlmE8zb0d_DVNHQITaGGjoRSp0WMoGR32Gt4XOWiD7F9GHW0OUcj7H4sQqIVg_3oGcvfjNmb_Odm06bsKCrB-26ehPiCDYaMHDNL9s5YjTO6JzYkQd5oYkcNY75bFZ1OLEUgyacF5kh3FCjhAnQOcRur5OWI0WbQy-Omw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
7 هواپیمای سوخت‌رسان اکنون بر فراز تنگه هرمز پرواز می‌کنند. به نظر می‌رسد ایالات متحده تلاش می‌کند کشتی‌ها را از سمت عمان عبور دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/150384" target="_blank">📅 13:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150383">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2d20e32f.mp4?token=u4c4HRmlhBXlt7WcYHtXMBBLlkSSsL_muMVR988JwwLXCbVyvYsAayHl0c1ZOBIvawSr1mnV2YCItbi1_uV_oTnJ23dByEigXmEZ_4nhjTrkLEiDFGqjtwJbttikMNZzNinYGeujUXWVor2RgKhcoIeypRo08jf85lRmCrG8wWTVfle0UTUZfoBk-ALth7EH9kkUxz_YX37xvzhZHWyniBjDa7arwLEs42ZVtnF2pFf7yliETWhkcVAZIGSIHaUo0SDRrZ463ek1m3BkXtWSh5qfQW796UaQ5ak9ct1kAv2z9FB3CbRuaqDlCkzxjFbd-QYrz3OUsjZzY1Q-i_fuSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2d20e32f.mp4?token=u4c4HRmlhBXlt7WcYHtXMBBLlkSSsL_muMVR988JwwLXCbVyvYsAayHl0c1ZOBIvawSr1mnV2YCItbi1_uV_oTnJ23dByEigXmEZ_4nhjTrkLEiDFGqjtwJbttikMNZzNinYGeujUXWVor2RgKhcoIeypRo08jf85lRmCrG8wWTVfle0UTUZfoBk-ALth7EH9kkUxz_YX37xvzhZHWyniBjDa7arwLEs42ZVtnF2pFf7yliETWhkcVAZIGSIHaUo0SDRrZ463ek1m3BkXtWSh5qfQW796UaQ5ak9ct1kAv2z9FB3CbRuaqDlCkzxjFbd-QYrz3OUsjZzY1Q-i_fuSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ولودیمیر زلنسکی، رئیس‌جمهور اوکراین:
یک هدف در دریای سیاه مورد اصابت قرار گرفت، همچنین یک محل پرتاب و ذخیره‌سازی برای پهپادهای تهاجمی در منطقه اوریول
🔴
همچنین، تحریم‌هایی علیه یک مجتمع نفتی در منطقه سامارا و یک انبار تدارکاتی برای نیروهای متجاوز در منطقه برانسک اعمال شد.
🔴
ما به تلاشمان برای سلب توانایی از روسیه برای ادامه این جنگ ادامه خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/150383" target="_blank">📅 13:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150382">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcwIWjr6Y7LxTQXBp9ZAELM_31B4ScTMr1ZSiCtQYkDDRWwEFrcpK-wDzLZylp0wIqAjPan0qkEGAQuuNcwu3f6nnILH0RmzM8gxIeS2GKIkrLx8hFIfLkuPSXAHeuayf0ITFHt2MvF49dTK7G4LSHcfGhPHQnXh27h80TLjC-wfWXW70f02BDJn1RcpcdG4mLXqCC85QDeShzGrOtdWk347SBb2v65ifm2aepf2r-EohLCLjLXiEBtCEoWzJ4yTFWdt0zPfXf0Tb-yp_VsbNv1lYw_uzdb5E_eChaaDza5-Mz6VPWx_xdGnx70YDHhEHKIzufNMK0lPe_Gv2BEJJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ گزارش نیویورک‌پست درباره هشدار اسکات بسنت درباره اقتصاد ایران رو بازنشر کرد.
🔴
بسنت: احتمالا ظرف دو هفته چیزی از اقتصاد ایران باقی نمی ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/150382" target="_blank">📅 13:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150381">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
رویترز: مقام‌های سوریه و حزب‌الله در ترکیه محرمانه دیدار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150381" target="_blank">📅 13:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150380">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
عوستاد خوش چشم: برای بار سوم تاکید میکنم که صددرصد جنگ خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/150380" target="_blank">📅 13:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150379">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsqoIejviYhl2YSq0gd9Alt7TnMHPCgV9ok9l0bzfHHNEqxObV8EFUGqEUM8_uPKtiF2t91uiohkp60FldwRl4aVFcAhwx0XklMkU5QP6TcNVGzDp9fw7Hg7WpRlArK8xjnEjhNVEen0HKmvyG46Y7ie0w7hWUWay1z40c--3sINebKZHILhCxkp-gfwaiM4W9E1MPMOKlzkAID2UiImUkc92rtKVwqzkaXkP7gFBVAdKZjhbGVdj7V_LjJcCeGXmwdzGNXOaEl7eutwGq-1iFz-NoVtdH8Bna_2WaOETRR9QiC2t4DsoOxQEP6K-Aumu61Vs0sa13Q4X0top_PGsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیروز تو قم عده ای برای تصویب قانون حجاب اجباری به صورت نشسته قیام کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/150379" target="_blank">📅 12:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150378">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e053e973a0.mp4?token=KRYVOZ8EBDS3quds9gKMtFNd_xS9ixaAHziH6ra1plp-CZp7USRW5INiKTpsikm_qZGWH2nu1Onogky0sFZYF2A_6PBho-0ZFRRCK9coyLdwsMdkylmK9atiV3Y48BQKMVeFYx_VszgqK_HhiS_YQZdhxELDcZyZq-kP4vedlKjWkysVyVk52VUTjWlthZD79TjHHc70TONVsbAsG60pN4vo2fUhzCN_-fT2NVWZjCpQShsdthP8wH1SvAKCuhzlacq3bhpiXj-qLjXF_zOxQqOzgzTxFIo5l4AMnoSrbvz4tcSvPKvUIYnJsiCg0W22IeM0Jep_E63dSJm4Fuu9sA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e053e973a0.mp4?token=KRYVOZ8EBDS3quds9gKMtFNd_xS9ixaAHziH6ra1plp-CZp7USRW5INiKTpsikm_qZGWH2nu1Onogky0sFZYF2A_6PBho-0ZFRRCK9coyLdwsMdkylmK9atiV3Y48BQKMVeFYx_VszgqK_HhiS_YQZdhxELDcZyZq-kP4vedlKjWkysVyVk52VUTjWlthZD79TjHHc70TONVsbAsG60pN4vo2fUhzCN_-fT2NVWZjCpQShsdthP8wH1SvAKCuhzlacq3bhpiXj-qLjXF_zOxQqOzgzTxFIo5l4AMnoSrbvz4tcSvPKvUIYnJsiCg0W22IeM0Jep_E63dSJm4Fuu9sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آمریکا با انتشار این کلیپ و نحوه شناسایی و منفجر کردن آدما با پهپاد، ایران رو به جنگ زمینی تهدید کرد!
🔴
تو این کلیپ سربازای آمریکایی وارد خاک ایران میشن، و دو نفرو با پهپاد میکشن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/150378" target="_blank">📅 12:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150377">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
حکمی، معاون فناوری وزیر ارتباطات : اگر استارلینک فعال شود وزارت ارتباطات و شورای عالی فضای مجازی را باید شهربازی کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/150377" target="_blank">📅 12:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150376">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
بازی تیم ملی فوتبال و گینه‌بیسائو به دلیل تحریم‌ها لغو شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150376" target="_blank">📅 12:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150375">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba87359042.mp4?token=NY1bM2Hq-fKt0wxlSMCHDIAWnE_G0y7cvHLSpKKvk-zrrq5S3R0eyNNYX3d0xf1VlwBujqGeLi_OKP873YuwVkAk0crDXyUM6XjwOfOUYLgGO0KXwlbxTFW7KLJXdrVVCl2tqxQTEqKZ6eTyrUHb9T0lh7lVZq3DmEEPgFNqhlFPvv8qKsnn6JnewjCDp3aFfpBAxUIy8QdruYyxhgPSAaTRhBn1yQAF7JT8rxp91E_Zz_cAJu4dTC65eK1zR4toBJxrpLnM67sN4r4MNY5g5ROLeWse5sMR1_-3mV-rPVNs-CpTosyJUjH10vsztkNkWWHSOSuDEFHnxH9S-rQVRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba87359042.mp4?token=NY1bM2Hq-fKt0wxlSMCHDIAWnE_G0y7cvHLSpKKvk-zrrq5S3R0eyNNYX3d0xf1VlwBujqGeLi_OKP873YuwVkAk0crDXyUM6XjwOfOUYLgGO0KXwlbxTFW7KLJXdrVVCl2tqxQTEqKZ6eTyrUHb9T0lh7lVZq3DmEEPgFNqhlFPvv8qKsnn6JnewjCDp3aFfpBAxUIy8QdruYyxhgPSAaTRhBn1yQAF7JT8rxp91E_Zz_cAJu4dTC65eK1zR4toBJxrpLnM67sN4r4MNY5g5ROLeWse5sMR1_-3mV-rPVNs-CpTosyJUjH10vsztkNkWWHSOSuDEFHnxH9S-rQVRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کشته و زخمی در میان نیروهای وابسته به عربستان در جبهه سامع در جنوب تعز
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150375" target="_blank">📅 12:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150373">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GbfIi72_vgvNBzShL_IEL_1f8l7lUm2V7Vw9_nhH-9XI8svXN08KtXrvJGcp_58DNnWVDgFIf-Mh60Tpz1qXlD3yXKI681hzEbk1Q-1306gdDmG7_Ly_Ip8zANOUt-mtaZasMMnV95OuDPYxTEPqbudGtr2EVRcWBEwfoa2fxfsnZ6yX20IAN0tRoXs4jQqjJZelOK-cQ3tNoN2Y77Obu7OjJBVD7zHtfA1uLftDqVd3dEVfOe7nl7ueAqEwKGL1rt7GjQ5Li5N3ZNvnjOsg8VYqRzi3c100VftDdKG4gwNKL34_m8prwmvODgaBoFZ4x-dSxIR8kI8IdX1D41c_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j8r72bBuUC_Tq2LPJ37izXZgOMGQvuugdZJBrDtMeuST4u6-Nm0zRo0ieq0QHUae91aKUWOPwjBJQlOYw5aOubIRPZCHPu5TeAxa6oaT6UgKM3PgMhlXXfeq7ZQ15UchF2jn9jMA7dFIslJikDnFdEyGKGt1i7HEIQzyqqQvhzuONg_LhsjatfxRWGNORkWF65CQgFZOqmGadnc3ZLqFswR67OpQUEMP3OgzVoRfG8QWuzX4nTmBauQpRJqeEXlLWWkZbE4bGBImi5pC4BIuCxGvXPNN-JIdg-VAkPJd-7p_8PYlo-4sfw1Hs7wS7ZoRDIkxOptuEeYf8-BfM6tgnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هواپیماهای سعودی، مناطق جنوبی شهر تعز را هدف قرار می‌دهند، در حالی که تلاش‌های مداوم خود را برای جلوگیری از پیشروی حوثی ها می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150373" target="_blank">📅 12:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150372">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgOgcqm6bBoHUuctqxoGFqeUgyIpSkBh29Kj5o0DiucF6_F-yVmcCn62-uklsSq_YUm7D0DIROAH8J14IgoP_vhV11s14wgbH3qAH3YprzUl-H-OpHAmNCX_lH0mQpjTlzfzhh31XHgn-eYhjBDxr9Yhe4er_iTR-n6qZHXXw2zsdz9Y_-lQEy9pv7HL_4AptTfSckx_Nq55w3JU7slLWLSRon9lRtC5m9CRPsXleq2i04cJi72dvYg8Fr6rR-rz8cl9tWokkpyTAvCyx0IbnoLinvPJfa8vjoCanaZcQjwEl2QLTQq1LH4qEX278HRj6LfCPlk4LWQlNcxkiOPAlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شده در فروشگاه‌های کشور.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150372" target="_blank">📅 12:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150371">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
خروج ترکیه از یک پایگاه نظامی در عراق
🔴
وزارت دفاع ترکیه: ما تصمیم گرفته‌ایم که پایگاه بعشیقه-زیلکان را به تدریج و بر اساس سازوکار توافق شده به مقامات عراقی تحویل دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150371" target="_blank">📅 12:17 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
