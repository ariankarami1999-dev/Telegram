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
<img src="https://cdn5.telesco.pe/file/BIyWJRse90IGVeilFk4VGoazZQRUVio0U94t8byJJb6UYCTWWnzNMYo7flh7T2bz_gAAvVWWqH3sxLt65pjATZfNSWObkOjmhstV8sCCj5oZTY0Vf4CpPCo99kRyW3xrXXPS6PuazTZlaEcE_xhk40_ogXOvMVEbM-EnUSYsP9b6f1uIimkQvgHTzyB-Wcex_ZNHgojao7hSQquyGNzEint8KnOJaFCnLJy0HOy78C7HTA0soLqqC5mzOEOnVYcRTLLXH-ztEn_ro66fPURw2Facupr-PjEuEdsDezars8FNHcGRzjlBe6abcyJzh11mM5DWZKxyur86C8DOEDsnwg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 583K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 21:56:29</div>
<hr>

<div class="tg-post" id="msg-99981">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38664c7a49.mp4?token=t5W3VOOaF8oCV4c84dy4ABu7Sq8wgpSGDretqK-hMVGIkZZlBWJ4bp7o7dvQnf8kxpjkz9bjqCNawfy0LdrsRHoJS1L5l5U-3kqhKaoM8gNLAyWtnd62lyy64m5aGHs8TZZhsBFglIbqCO5POqe4i6FPiqR1h468Eb60VDT9BCanipaFnIKbaJlHxLLw2wyYjsK7LzZ2ctu3NSYTlVk1hPdeFn4f99Up4-4a_zNJxYLm-2bp-t8ANF27z4uRGEXotPB51-EXSGnJgWz9Yax9r8jv0LRusZglmJ8oi_6RrC3hzFHTd6mDiqD7UhSF7pK-tHRg03m6yxayPrxNpiCckg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38664c7a49.mp4?token=t5W3VOOaF8oCV4c84dy4ABu7Sq8wgpSGDretqK-hMVGIkZZlBWJ4bp7o7dvQnf8kxpjkz9bjqCNawfy0LdrsRHoJS1L5l5U-3kqhKaoM8gNLAyWtnd62lyy64m5aGHs8TZZhsBFglIbqCO5POqe4i6FPiqR1h468Eb60VDT9BCanipaFnIKbaJlHxLLw2wyYjsK7LzZ2ctu3NSYTlVk1hPdeFn4f99Up4-4a_zNJxYLm-2bp-t8ANF27z4uRGEXotPB51-EXSGnJgWz9Yax9r8jv0LRusZglmJ8oi_6RrC3hzFHTd6mDiqD7UhSF7pK-tHRg03m6yxayPrxNpiCckg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
مقایسه آرژانتین با دوره قبلی از نگاه گابریل کالدرون سرمربی سابق پرسپولیس که اعتقاد دارد در مرحله حذفی، هیچ حریفی آسان نیست
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 618 · <a href="https://t.me/Futball180TV/99981" target="_blank">📅 21:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99980">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsFfVvnooWGPCcEq5v4PlmcnjDoDyKBbYwJod1_h98FaFLldAYZR4zm7DMWtCURIhSwNDDYAeIubmLUoxbplsepnkgZNrfOOpBENtpHOhkcujAYEp1U05lUJt_Alf1GcVQfdrVk8x-kRtVWW8YkPlXX6DLLZ505A3qiE8-sM_Pq3quiW-n0Sp8tPH1M0EZWLXEU70nER3Y3Y52t2WLjKRU_RHAjvcqdbbKexobRwmFQZDvExMKNgs0WwB2PXZlheWr-3GtdeBsLXyDxwnKBhgkvZYv1VipN2G-YUch9jCiN7Oxb9H_7_ccaavhra1OW_SjoObRIQlrc-U4ey0vB-hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تب پیش‌بینی جام جهانی بالا گرفت
مشارکت ۵.۵ میلیون کاربر در جام «همراه من»
🔹
تب جام جهانی بالا گرفته و لیگ پیش‌بینی جام جهانی «همراه من» به میدان اصلی رقابت‌ها تبدیل شده است. تا پایان مرحله یک‌چهارم نهایی، بیش از ۵.۵ میلیون کاربر وارد این لیگ شدند تا شانس خود را برای حدس زدن نتایج امتحان کنند.
🔹
اعداد مشارکت خیره‌کننده است؛ کاربران تا اینجا نتایج ۹۸ مسابقه را پیش‌بینی کرده‌اند. فقط در ۳۰ روز نخست کمپین، بیش از ۹۰ میلیون پیش‌بینی ثبت شده که نشان‌دهنده فعالیت بی‌وقفه شرکت کننده‌هاست.
🔹
حالا با رسیدن به مراحل نیمه‌نهایی و فینال، این آمار باز هم قرار هست جابه‌جا شود.
پویش «همراه من
» دیگر فقط یک بخش جانبی نیست؛ کانون اصلی هیجان برای هواداران است که پا‌به‌پای بازی‌ها، در فضای دیجیتال به رقابت با یکدیگر می‌پردازند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 317 · <a href="https://t.me/Futball180TV/99980" target="_blank">📅 21:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99979">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/183d4ae8ef.mp4?token=i3nXf0U6bDyxvmBwySsRmRIrIyM741esFYyvMJ9XSjbFlmOpno6HylxbTXTrAadzsM4xCeGNWrOCFRydLdDNLnjiT4BQhnis4cyWqr3eBe6nJWAuoI8YhUkq8hi-IT0HTLLVPtGtkJkJSVQTaTWl20F6Tzo4TKdG4YvIuW8le80iLxuu2k4wpvC1l-oP67StforkiS14z2vUA27tetcub_RREEukqKSzXx2B60IFpzfqEr6ZwayUJlYf_yZeVVS-_TMXoOqVP0RipqLPzPBDd9-ia92FM_gKKImgSSWaxMUHzuWclnDt18o6g3kI7-lyvZH3e_5LeTp4RNNWJhmdNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/183d4ae8ef.mp4?token=i3nXf0U6bDyxvmBwySsRmRIrIyM741esFYyvMJ9XSjbFlmOpno6HylxbTXTrAadzsM4xCeGNWrOCFRydLdDNLnjiT4BQhnis4cyWqr3eBe6nJWAuoI8YhUkq8hi-IT0HTLLVPtGtkJkJSVQTaTWl20F6Tzo4TKdG4YvIuW8le80iLxuu2k4wpvC1l-oP67StforkiS14z2vUA27tetcub_RREEukqKSzXx2B60IFpzfqEr6ZwayUJlYf_yZeVVS-_TMXoOqVP0RipqLPzPBDd9-ia92FM_gKKImgSSWaxMUHzuWclnDt18o6g3kI7-lyvZH3e_5LeTp4RNNWJhmdNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو آدیداس برای 19 سالگی یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/99979" target="_blank">📅 21:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99978">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/Futball180TV/99978" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🚀
🛡
ثبت نام آسان و سریع
✔️
📱
اپ
ل
یکیشن را روی موبایل اندروید خود
نصب کنید و بدون نیاز به
🔤
🔤
🔤
وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/Futball180TV/99978" target="_blank">📅 21:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99977">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Ms0RVpwfJ1Z944lkIu67Uf6yVnLarK4FUR7GjZvO7Ocwhi10PgudTbiU3-YcZEcFj8jVPIWihgFXmC7BwMUF_khGpptzshJbDC_x1vvhyFn9evsBoE29o2MabgFHIIo5rYJFXc4uODx6GRaFBIpUKYgAHlTwBQp2eEV0No1NneQUrnh1vLkOu0jIhPgSrxEQuys_GaZCeoagsx0vZSSfxP5-xvF3IzSO9QnyjCR48PRPEr9Wb58CFVotfDDVfB4_yLRkxsAq5VOcWVfp5Zq84Wwl2TtrjuPuRsEa2RMzweKJ8OW-rEPFYKQneqn3lOX7L5xmk0x6IKmLuYRCyfCAjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎆
تورنومنت بزرگ
POpOK
Gamin
💥
فرصت ویژه برای علاقه‌مندان به بازی‌های کازینویی
🆒
📈
رقابت کن، امتیاز جمع کن و سهمت را از جوایز میلیادری بگیر
💰
😮
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
برای هر واریز
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
🏦
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از واریز
🔣
0️⃣
3️⃣
کش بک هفتگی
📇
امتیاز وفاداری همراه با انواع هدایای نقدی روزانه مخصوص کاربران فعال لنزبت
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
📱
https://www.lenzbet1.space</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/99977" target="_blank">📅 21:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99976">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnPlFCB1PVyOaNjMAetuWX8o1o23VmLiponmUyax3MZVDsIMgDiG5a8sseAITE6VK_V-i9JH2lO0nwVoZ0U1LdIidCoSHgjhHVVGFLhQY5-NFIrkh19pCH5t4o5Ask33Q2nY0UzDg4HXGiQpHf0StbbwP-QHblQMeNBh_jEakvB-ARS50peDF4WEU1QhgUk7xgOw4IRpNkx1LhYjfLfEQY1gvcqmZlu1NWcDb2FpXxrZUDnS86LZJoNj5Ux80Dru8gcSclA6eNdLSDSSSSeuIs8U4VzwnOfsIZaQcniXWVKio2TjXPzgA9FdYFHhAfBiihsYbbwcZkwLnrKvjliQzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ رسما کنگره رو از آغاز مجدد جنگ علیه ایران مطلع کرد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/99976" target="_blank">📅 21:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99975">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtY1DRHcVmAcfEg7s6Umb1VqOoQSciVS1OVFOmsHMqUDc4bxQa6W53EuaG_Q10ctcv6x0PxXmgIedsJSSb0EkkLUGf1el2AWk0kVo6nPVdVEmlBu0CV3UqKkoFLOKojCYzGDT4Tdup0U0lZtcWqDUFvny6F0ldPHksYfhImSrGyEsiw57Fk2NW6jm8yIyJW60-3bL7bJi5yEHcNTiyijVEFp32yUpbnTCa2TV7Bz_cBm-uhbVbqvyZPiPIVzpuzeJdaqRE7cJTdhSiA5eRoT677yJlTpJ1t3rcQ-xKfbjzrfoIrWwt9wV6ST-0vMMcfI5tU8jgbQbtKcluo1O-BzAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست مشترک زلاتان و هالند : قدرت در مو است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/99975" target="_blank">📅 21:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99974">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YM2sQZldPJNUPoQcjiqeXoDz6215xMkvf-Sivbar8bC1qNllwkRVerZECoWOLdJrcMyOjThvfgQ09j36D8kL3Aeezct9Il-N5d8217K47Q79RtQZWk57ExzscQEy6URuwQiPbqRWwkG3QYX9FsRCUzmVzHf9WpjocqbCYmUvGOBYsyhllCJWvmKUo6XtTDoFV5R-GOTRr4uYXWIqydKG3rOTat2PKf_IPgIcfQQMc9Q0rCQjgpl-bQ3-qbtJmHde5WkUG4mlBu9F07_UsVrcIA__ZJ1mro70Bl3zSzEN-N0x-pMTNnDO8B-iwcmUm7SFZbycuHT9oJYHyrfKgy4OjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
همه مربیان پریمیرلیگ در فصل آینده در یک قاب.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/99974" target="_blank">📅 21:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99973">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Abn4ViG6QXnfyC0s4rfYuD75BFi3OVFI8yGIsHOz0NC5ucjEyH-nhU7hVkr2pszfxTHDNjartGWF3ZpTA-9OWvDoyDVpfmdjx6JtNxnV6eRkILpTBvSXAg8b2hcEF4EP9CYqkgBztx3qf7kjHOVmkPGwTITRjguJ3boRTZVvp-Na-djaLa_jNB1wlmscPDPFDhQ1U_SHJKkj19QK7hwgQSAySEwXFI3yLWFVy2Qs2A0RHN1XV8WTrt8XCrxdWA6vg0o4JvPt0SR0tnsbft78SPHU5PBDXNyx44IhSs5yUFbdSPKqnhPvUWR5wXJiu4HNO_iNivnQOUAMslt7VPNRVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇪🇸
کوکوریا:
وقتی لیگ شروع می‌شود، جنگ با بازیکنان بارسلونا آغاز می‌شود. بعد از آن، بارها در دوره‌های فیفادی با هم دیدار خواهیم کرد و در آن زمان، آتش‌بس خواهیم کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/99973" target="_blank">📅 21:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99972">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-5iIyMmUXKzHeAlMMjM8JsXsNVdcyB0xf7cVKNs1h5_CjopuCUqElyboDijboZsIvp0aEOwypG10bsc4DigsLA2SaDDX9fY89vtK6tzMhff18aNf6ijvrEtnAYY4ED7gB9kbXtkDYcD7zFLBkBxV-h7dht00SUOcOuTaRC1Ahb7lDLBKY1y1Qbk5OPaIhzLxZNdynjEyZ77iSS20jJfiM8LkH1hF9bFiljFZGIBwDLTT6WRYBn57fKE1Ki5rcl5G3VS2-LCv_ntn_Ch7nq3a-pitMhA-I1crlYLQd_2LBsDk3TAPdZ54T2xFojiyuL5mU2tWpLI1F0irHRBriuiyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/99972" target="_blank">📅 21:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99971">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DB_jV3-CbeVANPIjHarmKUtZC60mj74HOvjN9sbWl0URY3EOLt_W6KKZB25wJq4TiobF9X0iBk_xxqo4e0McgAs3Btt4lJ_Cnxh-kulMD0Mw_b2xBZOvPaGGdyScbX9Ly1NUnJJ2hUEmfVAiFK3XWDTg2RyoMjuePsaiPwCztrPW0jYXDzegjjzbulGJytHAoI4f5JZsab1ns9kWnng2xw9hkm__C52r6jb9-Y9O2Y76vVs-FQfUOUHcFbTlbsYjLn3xSlF0XPuzAf75J5GG0QpfJ7dDO0VSPvHNHMu277pRMN16FAXN03Nb5TVvTNSBXUcDzWd_pRg0Ir53nmOn0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
طبق اعلام رسانه‌های ایتالیایی، پپ گواردیولا اصلی ترین گزینه سرمربی‌گری تیم ملی ایتالیاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/Futball180TV/99971" target="_blank">📅 21:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99970">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3mUtjqklhcriQjEHK0HX4S1r_PAE18ypxzWg-7Ntnw8fgy6DpSetGzb-_-nmNllXHuNundOhIVciMSxaYRUpSMikRi6wIVM3xTu_FV8NYpetXO2BUpEIzmJrRaXbxA9S6zxs3OZ1IRmqHEcZFceV712yMEXFyjLK3eL6njp_TTehtIlxXgODJfvBGFgK4UCsXM3tiydaxF8H4oaRej6tl2AGtq1fHnCo0TCb41bbTcNevrXSrJ7Oez3B-hnupfqhDNjD8-SBEfyFBXmfnJUtmnzEv4BtQxv0UPeklBsDvKVRraOllQYPE0IOnjKqN1d28PNdXSbSnVci7832ltHkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری - مارکا:
تیبو کورتوا دچار آسیب‌دیدگی نشده است. این بازیکن امروز معاینات پزشکی را انجام داد و همه چیز به خوبی پیش رفت.
🇪🇸
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/99970" target="_blank">📅 21:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99969">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4cbd524bc.mp4?token=gcHYitJlssx4osffQvzsolVNPInH2ZdIl4orJmdD9RtfmPRPhKgCWyndVj2x3Q_SWlAfS3A629wC2cSziRjtF2wwNce6z7p98sup01vaRgh2m8p-bYmUfg3fZhUC2KXfHEwezjvcr1Gj8_8etKQ7TFrPvV2DctSKHbcLZwtqUS-7_vufws9nttz0AMaVZ7jT_-TJ7Qag_GZ-z_EnbNkBjZSN-MG_EEm0fj-HiNO6-JviiCqPdh7ezKYlCVJJfRctbAtXSW_X0ml5HJ47BTdx3L5EtVJIZiEtzqsKcZf626jQM8I7_QUaLWOrvpVctTjDgjn2tdGeI7H1XdWHXzB_vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4cbd524bc.mp4?token=gcHYitJlssx4osffQvzsolVNPInH2ZdIl4orJmdD9RtfmPRPhKgCWyndVj2x3Q_SWlAfS3A629wC2cSziRjtF2wwNce6z7p98sup01vaRgh2m8p-bYmUfg3fZhUC2KXfHEwezjvcr1Gj8_8etKQ7TFrPvV2DctSKHbcLZwtqUS-7_vufws9nttz0AMaVZ7jT_-TJ7Qag_GZ-z_EnbNkBjZSN-MG_EEm0fj-HiNO6-JviiCqPdh7ezKYlCVJJfRctbAtXSW_X0ml5HJ47BTdx3L5EtVJIZiEtzqsKcZf626jQM8I7_QUaLWOrvpVctTjDgjn2tdGeI7H1XdWHXzB_vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرق ارزونترین تا گرونترین صندلی های جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/99969" target="_blank">📅 20:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99968">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e7fbe2f2.mp4?token=fkPwtHB8dH34-KRLFOM6-r0RsP1huj1HDTKaeanvM5c8ATV5hYAhjVV9DPfN-Q4y4nt78pOdsvGQBmWSTBVWmsdRvO8lBc2Y0yVS0U91wRLW7Y4mCMcV7ycGjuc7AQA_D3MydZZJupwKJ-FT_OCsOsHBKoTm8w3CP5u9EvQqXRqLit5pfBs_uVTa4RhFMz7skgbvsF5OZJjSku0_cw0b0kkpyfhWpu2UN9CM1gJRCiDseRUi-5-s-xZ_lrKgi5aLmMyEB4F8KIKvXDUh_mATAtbzqJN-N6o5_rs0rDC0-ggARXLYO993_cZkvjKhTZi7YaEjdKQz7GLnrRVSYqSk2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e7fbe2f2.mp4?token=fkPwtHB8dH34-KRLFOM6-r0RsP1huj1HDTKaeanvM5c8ATV5hYAhjVV9DPfN-Q4y4nt78pOdsvGQBmWSTBVWmsdRvO8lBc2Y0yVS0U91wRLW7Y4mCMcV7ycGjuc7AQA_D3MydZZJupwKJ-FT_OCsOsHBKoTm8w3CP5u9EvQqXRqLit5pfBs_uVTa4RhFMz7skgbvsF5OZJjSku0_cw0b0kkpyfhWpu2UN9CM1gJRCiDseRUi-5-s-xZ_lrKgi5aLmMyEB4F8KIKvXDUh_mATAtbzqJN-N6o5_rs0rDC0-ggARXLYO993_cZkvjKhTZi7YaEjdKQz7GLnrRVSYqSk2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا جان تبریک میگم که بالاخره استعدادت رو کشف کردی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/99968" target="_blank">📅 20:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99967">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tD9xtipWUjWlEE2zGw23W9gUGZti_N5YDlwpExCknFy8UKDFtlqBtOb5oJ_sZslpVpVYlRZBe8mwYKwgZRZPhlXrt-HdxgUMYss3KrMc6wpi_l9g2hkZsieg_XOiKy4jvLB0ckf0K-KXKiecGmvpvUA5Nw3NZuRKg0sQPBCOIwBqmNgoGa8L3zjdxK1eDbtBBewxFJNdoPuXii0R6CBmtkhajQARhzqwo56kQN25f0en100Zt2OgAlZ20BCTb_Yjo6p6DaKrHCDexg7JyIXjRkvgTEI6LbjtHhKyrO8PQW2e9Qzc-GXIR9BlI71oG3_MxT7oj42rWh2LGTvLnelgVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
۵۰۰ دلار جایزه نقدی + ۱ گیگ اینترنت رایگان!
🎁
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
🔥
نیمه‌نهایی جام جهانی ۲۰۲۶
فقط کافیه نتیجه بازی رو
قبل از شروع مسابقه
درست پیش‌بینی کنی.
🏆
۵۰۰ دلار بین تمام پیش‌بینی‌های صحیح بصورت FreeBet تقسیم میشه.
🎁
علاوه بر اون، همه برنده‌ها
۱ گیگ اینترنت یک‌ماهه رایگان
دریافت می‌کنن.
⏳
فرصت ثبت پیش‌بینی محدوده؛ بعد از شروع بازی دیگه امکان شرکت وجود نداره.
👇
همین حالا وارد شو:
https://t.me/betegram_bot?start=p7_r4EF37DCE</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/99967" target="_blank">📅 20:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99966">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SspYkHkfzDSvjZ-c2dw42tozxBAxoDBHwkSspS1nO-Bc2z3V-2TxfyDmgY1YnHDp5s9_WbGCOR8Nq7x4Il5cizAtG3tw7hDNdQUj7uhV_SHqFkbWOVzrXvQj2aDSxrjSqbYfSimeDCqvqSSNuvE9XCItBKyzl7uaSWficcK9pBQdXhGHTwGnHawuQwQ6QJcW_rwn_ETypnyl_TSlnkp0P6XPEVoUXMCa6MSc1yOGEzHUzYgKX-s1ntgtgq_hSYMblkxVb-QoADLV1PpWO8bPiNHI9RUkjE_ET5MOw8sPpRloLOXGgtspxRDCYh3Cfbj_RAN1W_7F62YYnb9CrVUrcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
❌
🇳🇱
روب دبی‌رینک داور ۳۸ ساله هلندی به قتل رسید. این داور گزینه حضور در جام‌جهانی بوده که در نهایت توسط فیفا از فهرست نهایی خط خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/99966" target="_blank">📅 20:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99965">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa4c44829d.mp4?token=beN8YY9xdG_jUpyocgHg5ubnAjG2dO_xX5XNN6p3jKdFGHqijgpj1W0UNCs88ix3hQqtnxwHd8TH5HC86lFiHysxZUTre7-YcQ_lR-K0ao-iM1q6DY9mMHMVGH2G0YzD0vYAL6BtTrcWB7Cnp8-4tHpwBzZDeEqP-K7_selH0b4uco6b_-aQGs337FLSN5VM34rOyHr9n8kCXks5rJQ4YFhc9DlfwVuAZK5-pWRQ7pfyQ3F5C0VRUTcplYCKsNJG1YOTxWE02q9l5yNWaFbkz8Yg3-DSbOEhxuk8Fh7M6vPthiseiJVX95263PrmbTk4V_1bDNwsBDiS7lZYFi09Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa4c44829d.mp4?token=beN8YY9xdG_jUpyocgHg5ubnAjG2dO_xX5XNN6p3jKdFGHqijgpj1W0UNCs88ix3hQqtnxwHd8TH5HC86lFiHysxZUTre7-YcQ_lR-K0ao-iM1q6DY9mMHMVGH2G0YzD0vYAL6BtTrcWB7Cnp8-4tHpwBzZDeEqP-K7_selH0b4uco6b_-aQGs337FLSN5VM34rOyHr9n8kCXks5rJQ4YFhc9DlfwVuAZK5-pWRQ7pfyQ3F5C0VRUTcplYCKsNJG1YOTxWE02q9l5yNWaFbkz8Yg3-DSbOEhxuk8Fh7M6vPthiseiJVX95263PrmbTk4V_1bDNwsBDiS7lZYFi09Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
🎙
بیرانوند: اینقدر تو آمریکا وقت کم داشتیم و باید سریع میرفتیم که شورتمون رو یادمون میرفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/99965" target="_blank">📅 20:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99964">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
هفته بعدی تاجرنیا مصاحبه میکنه که زن یاسر آسانی مخالف برگشتش به ایران بوده و ما تمام تلاش خودمون رو کردیم
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/99964" target="_blank">📅 19:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99963">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e8095565.mp4?token=X38eOES6gx-M1yEuiwrinweMHK8wFVDjtD2mAgI5EaitlRZoMnGKRx55RMefxthLnVdekK6uKXZv4_oiK3_kxFGeW2Q1LUfSuJ7hn33XDq9d1U6RrBu6amnWCuwDSnDQvNTCYJ3CDB33iuqVEWmByL2TJL9Chy73qTyyAroMMdnW7OxqnFgmLCqLDvj701mgiMKmLOXB5fZEVEjZchhytBXkNt7Xldk7zHgEXkcVdF08SxeCF2gaaQtvzXYkFh3475JdHaY3pqJofk47052jLepxiRskbSgEbvNI9b3bw4BhlsGYaIQgUy3YZZaLIrqu1U9nP_0FZ668Ww1x8Y5EEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e8095565.mp4?token=X38eOES6gx-M1yEuiwrinweMHK8wFVDjtD2mAgI5EaitlRZoMnGKRx55RMefxthLnVdekK6uKXZv4_oiK3_kxFGeW2Q1LUfSuJ7hn33XDq9d1U6RrBu6amnWCuwDSnDQvNTCYJ3CDB33iuqVEWmByL2TJL9Chy73qTyyAroMMdnW7OxqnFgmLCqLDvj701mgiMKmLOXB5fZEVEjZchhytBXkNt7Xldk7zHgEXkcVdF08SxeCF2gaaQtvzXYkFh3475JdHaY3pqJofk47052jLepxiRskbSgEbvNI9b3bw4BhlsGYaIQgUy3YZZaLIrqu1U9nP_0FZ668Ww1x8Y5EEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
پیش‌بینی سه‌هفته پیش نوسترآداموس زمان یعنی مجید جلالی از تیم‌های برتر جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/99963" target="_blank">📅 19:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99962">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4532025b1.mp4?token=PCfeFhIUbbVeLp3CFtlrJAMpr45y1uy1S9fCfqwfTpGJaDLshNWWDOk0tVqrPvoFbSU1t2lzUK4-UXCL88QTt19R-HT3p1CNuHL2PjgToVrEw8m32hBLkjZep4inZxa1ASCio5oG7WCfhcKqxD0MDiei_6Hbsjsjrp517MufAqIm4Y_Bg9i8ra_fyWQm1m4AuEMeO__l_7TRLz8gjyi3QPnh7RVgx-ZtXArqwF04cO_E2AvH9gmb4zSmqRiiEcvw3tI6BvYvCmallMBouJ0SvFhnpUY-ZsODjSgMVvnssRZhjpuP-EJy25L8IiluBriEdnlNBFNWIlTZ_doZ1lyrOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4532025b1.mp4?token=PCfeFhIUbbVeLp3CFtlrJAMpr45y1uy1S9fCfqwfTpGJaDLshNWWDOk0tVqrPvoFbSU1t2lzUK4-UXCL88QTt19R-HT3p1CNuHL2PjgToVrEw8m32hBLkjZep4inZxa1ASCio5oG7WCfhcKqxD0MDiei_6Hbsjsjrp517MufAqIm4Y_Bg9i8ra_fyWQm1m4AuEMeO__l_7TRLz8gjyi3QPnh7RVgx-ZtXArqwF04cO_E2AvH9gmb4zSmqRiiEcvw3tI6BvYvCmallMBouJ0SvFhnpUY-ZsODjSgMVvnssRZhjpuP-EJy25L8IiluBriEdnlNBFNWIlTZ_doZ1lyrOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل خودت رو بزن!!!
🔹
با افتتاح حساب غیرحضوري در باران بانک کشاورزی، از برندگان
۹۳میلیون‌تومن
اعتبار خرید باش!
🔹
۹۳
سال قدمت
۹۳
برنده در هر روز.
🔹
برای شرکت در ‌قرعه‌کشی
اینجا
رو کلیک کن.
شرکت در ‌قرعه‌کشی
🎁
اسامی برندگان تا این لحظه
https://www.bki.ir/fifa2026lottery
⚽️
فقط تا پایان بازی‌های جام جهانی فرصت دارید
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/99962" target="_blank">📅 19:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99961">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🔵
#فوووووری بیانیه مشکوک باشگاه استقلال: یاسر‌آسانی که توافقات مثبتی برای تمدید قرارداد داشت، بدلیل دیدار با خانواده‌خود در میانه مذاکرات ایران را ترک کرد و بزودی برای تکمیل مذاکرات به تهران برمی‌گردد
‼️
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/99961" target="_blank">📅 19:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99960">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
‼️
یاسر‌آسانی امروز در تست‌های پزشکی باشگاه استقلال در ایفمارک حاضر بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/99960" target="_blank">📅 19:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99959">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dciATydfgpkhCJDBBviMpZ63IqvVsXZwin-GtsnEWLHmkiyF0l4xT5DElrsCWM4gW3-Cxz5j1zA2r8j9yoZ_TeBlI3vF_CWUaaK5kBHaG3phnk3jmJODuVFwDzBeEElu0-79baiCVX9Gz49kuuF4czOmsl9Sj5FHijw91ypNxzw1AoDRAJ-7XXd7IYE1KRwbL5XAhYzWNxmOXs9I7-10F9arB8baODgcM8diEA2ZclxVYA-wNnd-qpyaKZqeUWCZtaUuxj1Ddti090NMq0jQZ0vLi1zVSQ2cU5DSbiRcDUC828kYex67pCxpQ4uIXd-WipuzkgMSTgaROIraQxOk8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری ادعای رسانه‌های داخلی: تاجرنیا موفق به جلب رضایت یاسر آسانی نشد و این بازیکن ساعاتی‌پیش ایران رو ترک کرده!
❌
باید تا تایید یا تکذیب خبر منتظر واکنش باشگاه استقلال باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/99959" target="_blank">📅 19:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99958">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🔵
#فوری
ادعای رسانه‌های داخلی: تاجرنیا موفق به جلب رضایت یاسر آسانی نشد و این بازیکن ساعاتی‌پیش ایران رو ترک کرده!
❌
باید تا تایید یا تکذیب خبر منتظر واکنش باشگاه استقلال باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/99958" target="_blank">📅 19:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99957">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8b173980.mp4?token=Xt-FL21rl9ZlXBTMbJbIo6USwwNnzdxhrQTYgICRVObtkuAMi7_O1BFQhxGLURY0b5KdoLLkoWT-ZyruwhR8wXo0gHGhdakw2MgLCg-mBQsOfYzgfdcOwKgxxDsakcC5Dk1PU5SPGYT_-bwC3A3s4imFdW6aD7ApfiOTMxlvxzLjOAfCKJrhDt5Xd9s9IDrGUtKV9yOjEDlBKlSQ351TSY3oFNNh8LaqfC0CHq6pIMGVmKINZUgLUmR488lzmrE1LZASo_EARh8um12jZf6wjAdzXsSUQnNkAp1SXpxv0LIYM5mI7kiFptPXFoKC-44ThT2tfDyMkZNIN6lOtuSkYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8b173980.mp4?token=Xt-FL21rl9ZlXBTMbJbIo6USwwNnzdxhrQTYgICRVObtkuAMi7_O1BFQhxGLURY0b5KdoLLkoWT-ZyruwhR8wXo0gHGhdakw2MgLCg-mBQsOfYzgfdcOwKgxxDsakcC5Dk1PU5SPGYT_-bwC3A3s4imFdW6aD7ApfiOTMxlvxzLjOAfCKJrhDt5Xd9s9IDrGUtKV9yOjEDlBKlSQ351TSY3oFNNh8LaqfC0CHq6pIMGVmKINZUgLUmR488lzmrE1LZASo_EARh8um12jZf6wjAdzXsSUQnNkAp1SXpxv0LIYM5mI7kiFptPXFoKC-44ThT2tfDyMkZNIN6lOtuSkYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی گل منشوری عمو رشید
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/99957" target="_blank">📅 19:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99956">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfgqdLDLqcfRjrlc932ij4fFC85whOM-ybqt5ljFds2FumVYRxaMAsQAGz5kljuXR7sYjvZQx6cjJwSpO-I1Go-rmdlSEvLRJQieGEyN4u-iOAImF_rAEKKsGon0fy9lxVVicHD4Oi7QsE1WG1-cKgm9aAPN_EIm-NYzXB_REXH4g5zhgQBdhQWa1BTQQS62qeO6_ZrX4J5FGHaamx7HFvA6qDjlBCryCdnvyaPMwPKy5GaoyU3uD74Rx_fCZBmv6mz3_5aB51iIJX8aXp2U25AAu_0uxYYnxbRm9icu8oGINE2WajUuJNV8aqx0ceOF1G4n0L-Z0ZPGDouKiQUTNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
لیونل مسی و کیلیان امباپه تنها بازیکنانی هستند که تا کنون در جام جهانی 2026، 30 شوت یا بیشتر داشته‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/99956" target="_blank">📅 19:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99955">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_GO1fYNctcPfvVAEc5Frrg-eC04GacOyxi9Zenz0a46WMwXxgqckoQaNcYQJFeMOAHEZGLgL_WvQO15Fh1lWjhTt6ar2qp8595U8XZYDGTcnQJ0U2P3Gm1fi2dIRnImVlxFhUd0Ofb0cfHC6a5Znq68VZLxNgX8RQqTNh8R7HsrPH4tX2VWr6tH2N4s4gQ3dhTEiKYk31bowXlxspYff5uzblLCHmdzKOaXSryvfJWVGlurn8pInjPwjvM527cTUU1bkCbLSkhaXtuM8nhZ5yn22H2_KfR7vN0YWB5Hhi6vraBTaZvAeDIP59EyCgP7nK55EKA7d7bNmz2VSJp_OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
چلسی طبق معمول اسپرم خرید؛ هریسون پی‌تونی، هافبک 18 ساله انگلیسی، از باشگاه ویگان به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/99955" target="_blank">📅 19:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99954">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdjM9Q2QEx5go1Mog5DG5jaz-7r6ff0pvdjGn5J_-npJPs5yzpBHmcea-wnm0_XJOXYUQ3M-MIc3jKT2G4CTRYKxSvehSXKWRBPUq9W5LZ0k4KyOcOUQbkkmIZkurXaNlkBkRIonhFGZwEm2LLoa7_LiOpYqWBBw_2Xw_jZz2x75QWuqIgEhnGzajUTXgiGi7sWYgGWcvU08WeR4QEdsPuHTi_KvvtMTzRHW9elpnmEwf6AstfTaqZHIJNESewTBecmkSPcLEevSIcnAUIjy10S1GW8A22cJWVYBGALGuAuqlVFIhkC_jIiX3455EAi8C4QlvGCOllP_zXdJMjKY5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
ترکیب تیم‌ملی بارسلونا در نیمه‌نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/99954" target="_blank">📅 19:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99953">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a785f38a0c.mp4?token=NBQdJtg2B4Nen1hT71prX_Xa8KX8aam3kNo1LOQYjMAsBKmbtvS6nzdw3KQHf6Lqaj_pzWsBRtDXPxcj0MXVxCuiE-6ShdLBg3H319US8YiK9iwBPQNZC1LtliZ11xFfIiE4doRc48yw_M264y3_wAZK3FdCcIux33vJVGmTnqQukmOOeAZT86JPuZ7c_GNUIFzYmDZ2bKMY9rzYIWAqUGShD-BbfW0mL3SlI3CGtKgFZCdgZDJVoynHwvMjERbnDkWqiCHS8oeRQcmMMF-GyZiTmJqVu29et0EFma9BTS7KplNCT-T4f5pzt5HYXrs8niolKmCnJu3W9fIgQGdXcBL2ddTe7xYsZKRB-ZwGjN6v7yCilld7LS2nUHx1hfuBvJKZnS9PKyls97Uo2rxWKRiiHCNDm4id7kAgRxxiKq6ZV_0cHWk66BbK60pDgOEsZ5qkoDsfJoyjTmM132mVD-tQ8DWkpKYTPNksP3Ezl4g6K4Pw5dT6w0GYM23iPyLKJJ0N3bhO3FyZy_gG8ZNL3cbbn48f1zZ9urr_3l0XjNc3OByN6O_ZFEm4GHjIPQoUYc1mOODV533egaL_QZJ8pABi-AKHwf6Kqf4ISfboCGOM6e-XMLyr-bB06jNuopTdiWdfJglukoXMtWbNjXJCRIC7H8i8bkgDJC333So6N-U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a785f38a0c.mp4?token=NBQdJtg2B4Nen1hT71prX_Xa8KX8aam3kNo1LOQYjMAsBKmbtvS6nzdw3KQHf6Lqaj_pzWsBRtDXPxcj0MXVxCuiE-6ShdLBg3H319US8YiK9iwBPQNZC1LtliZ11xFfIiE4doRc48yw_M264y3_wAZK3FdCcIux33vJVGmTnqQukmOOeAZT86JPuZ7c_GNUIFzYmDZ2bKMY9rzYIWAqUGShD-BbfW0mL3SlI3CGtKgFZCdgZDJVoynHwvMjERbnDkWqiCHS8oeRQcmMMF-GyZiTmJqVu29et0EFma9BTS7KplNCT-T4f5pzt5HYXrs8niolKmCnJu3W9fIgQGdXcBL2ddTe7xYsZKRB-ZwGjN6v7yCilld7LS2nUHx1hfuBvJKZnS9PKyls97Uo2rxWKRiiHCNDm4id7kAgRxxiKq6ZV_0cHWk66BbK60pDgOEsZ5qkoDsfJoyjTmM132mVD-tQ8DWkpKYTPNksP3Ezl4g6K4Pw5dT6w0GYM23iPyLKJJ0N3bhO3FyZy_gG8ZNL3cbbn48f1zZ9urr_3l0XjNc3OByN6O_ZFEm4GHjIPQoUYc1mOODV533egaL_QZJ8pABi-AKHwf6Kqf4ISfboCGOM6e-XMLyr-bB06jNuopTdiWdfJglukoXMtWbNjXJCRIC7H8i8bkgDJC333So6N-U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚠️
ابراز نگرانی عادل فردوسی‌پور: با توجه به جو سازی انگلیسی‌‌ها فکر می‌کنم علیرضا فغانی داور فینال نباشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/99953" target="_blank">📅 18:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99952">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01042c6d55.mp4?token=pRYE4IHW-foVyNPD61JF8n0m4A1WVjN9EzhNn9vNcefXc6icMX_IjeSNY4dEN2afIyUfLFEO62GuS6z_PzyuYgaVU_dPWQ3bA8LYgkLQ-8hajA0vWDQRr9FW5SQVYySj28Uux1CFSidRbernsS17mGFJ2XgR7ySUQX3mZXJW8u1rSMkP2BeS8tf4tElfDsnZld5MoyqACZjKQgW8g-5nscJDj3X__EMh213vmrkJrcCHW43CVOJYB4KdVRR-hV9XABUi7EskKRKFZRSkg8Od782EVUR2QsHmwvuUyxM00IzxqMkowR9aYrkUetEhK96D3ZRLUgn0Pj6BqQdOPAPuMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01042c6d55.mp4?token=pRYE4IHW-foVyNPD61JF8n0m4A1WVjN9EzhNn9vNcefXc6icMX_IjeSNY4dEN2afIyUfLFEO62GuS6z_PzyuYgaVU_dPWQ3bA8LYgkLQ-8hajA0vWDQRr9FW5SQVYySj28Uux1CFSidRbernsS17mGFJ2XgR7ySUQX3mZXJW8u1rSMkP2BeS8tf4tElfDsnZld5MoyqACZjKQgW8g-5nscJDj3X__EMh213vmrkJrcCHW43CVOJYB4KdVRR-hV9XABUi7EskKRKFZRSkg8Od782EVUR2QsHmwvuUyxM00IzxqMkowR9aYrkUetEhK96D3ZRLUgn0Pj6BqQdOPAPuMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوتا کپی‌بی ارزش از رحمت و دختر بیرانوند
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/99952" target="_blank">📅 18:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99951">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
⭕️
دونالد ترامپ: محاصره دریایی ایران از این لحظه آغاز خواهد شد. از این پس، آمریکا به‌عنوان «نگهبان تنگۀ هرمز» شناخته خواهد شد و از کشتی‌ها عوارض ۲۰ درصدی می‌گیریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99951" target="_blank">📅 18:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99949">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad476d739.mp4?token=hztgqBez6C_etfhcVNA70UAC11ReCG5PtGyo7YlCgX_otcvlWguTuTtPd0-O67PHOqRn9Yku5JyjWyf_Z3nT0Uag0AQzerOqe5kg72HTdUJwCwVeJ4GEOwjyNb3Pzkvm3fVLe9BDI5EQWXD7XJliBxfH-YMbH2cBJr6rPze4o9vRQdhbqLuh47ndkiyXaUC037zjNDEbX9ZOYJr16TnnBJgkrWpLmTipwEcIGTaQPv8H78ecxer1X7xOyHBnf1vyqOz3dgBJk9YKAe6zJH4b3J6ZrBJEmKSS8OEuy7w8Mk0DeT7byI_ohKh91tYecGD1289_O99iK1NXRNg5MpgKcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad476d739.mp4?token=hztgqBez6C_etfhcVNA70UAC11ReCG5PtGyo7YlCgX_otcvlWguTuTtPd0-O67PHOqRn9Yku5JyjWyf_Z3nT0Uag0AQzerOqe5kg72HTdUJwCwVeJ4GEOwjyNb3Pzkvm3fVLe9BDI5EQWXD7XJliBxfH-YMbH2cBJr6rPze4o9vRQdhbqLuh47ndkiyXaUC037zjNDEbX9ZOYJr16TnnBJgkrWpLmTipwEcIGTaQPv8H78ecxer1X7xOyHBnf1vyqOz3dgBJk9YKAe6zJH4b3J6ZrBJEmKSS8OEuy7w8Mk0DeT7byI_ohKh91tYecGD1289_O99iK1NXRNg5MpgKcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
حمایت فوق‌العاده مردم روزاریو از لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99949" target="_blank">📅 18:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99948">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba993e62ea.mp4?token=t_eA3t2fcbl4oiTLatU4mm_HJDQmzxb3Ij5So1Y_EOux9aLOYTHTQ0EWlRuAmRBcVMWD0w_zpbl58-V3bQMyrQZuegFjjLRXPLdsv3nCXaAzS_Lues97gJkHyPebJpmgeSlGE5h10h6MPJ30xJ9OtxSCSgFLmy2zn_QhhdZCoVt6vp21to3rnMtEmX0G2ppKn7Fqw_1MAVTo7N6fPD2n1gymFSnBIlDmULScU3aPBSY2TkpSfD1nIqkxlO9LSEi5XnnybS8JfvxesBOJgFV1jmQx2NO-FVS0hVfie6PecsRpzfG7Sk5Z_ymAvMTNLELQlAYbChRf8juCiMV5JUvL7wh6sF8E5EACHXvDBa5aJQxyaPtWVlzqX7NDld3Obt1YeJL-yEbVD2XD_PinTSgjEUDNq2rGRL5LDwGGrVB3xN53m9xUjLxo0pmiE5TuJBYSluWCJwC6KkqhVgbpR-ih8tqex8pI4BZ7eDrdbVl1rl7N9Lb_M3fMer1rRlIotBtobJQrc0aoUXbGKO3h-EAoVGQqrLf-tMk-RbVq-zfCAXSxERAZnmGv8UtwMQjfvNaPgWSWWwJgRyxuIdn9Z7M5e-4rIXPpiLli9G_8cuFYSBlFTqBrQrENbAKhxws7AWuh07qnJwDyGxOiEMINpYa-U4nQZXBX3HjolB-xU-sDXW4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba993e62ea.mp4?token=t_eA3t2fcbl4oiTLatU4mm_HJDQmzxb3Ij5So1Y_EOux9aLOYTHTQ0EWlRuAmRBcVMWD0w_zpbl58-V3bQMyrQZuegFjjLRXPLdsv3nCXaAzS_Lues97gJkHyPebJpmgeSlGE5h10h6MPJ30xJ9OtxSCSgFLmy2zn_QhhdZCoVt6vp21to3rnMtEmX0G2ppKn7Fqw_1MAVTo7N6fPD2n1gymFSnBIlDmULScU3aPBSY2TkpSfD1nIqkxlO9LSEi5XnnybS8JfvxesBOJgFV1jmQx2NO-FVS0hVfie6PecsRpzfG7Sk5Z_ymAvMTNLELQlAYbChRf8juCiMV5JUvL7wh6sF8E5EACHXvDBa5aJQxyaPtWVlzqX7NDld3Obt1YeJL-yEbVD2XD_PinTSgjEUDNq2rGRL5LDwGGrVB3xN53m9xUjLxo0pmiE5TuJBYSluWCJwC6KkqhVgbpR-ih8tqex8pI4BZ7eDrdbVl1rl7N9Lb_M3fMer1rRlIotBtobJQrc0aoUXbGKO3h-EAoVGQqrLf-tMk-RbVq-zfCAXSxERAZnmGv8UtwMQjfvNaPgWSWWwJgRyxuIdn9Z7M5e-4rIXPpiLli9G_8cuFYSBlFTqBrQrENbAKhxws7AWuh07qnJwDyGxOiEMINpYa-U4nQZXBX3HjolB-xU-sDXW4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🏆
در قوانین جام‌جهانی سیستم وار در صحنه‌ای که بازیکن به اشتباه کارت زرد میگیره میتونه دخالت کنه و کارت زرد از بین بره. نمونش بازی آرژانتین و سوئیس که پاردس اشتباهی زرد گرفت داور رفت صحنه رو بررسی کرد و بازیکن سوئیس بخاطر حرکت تمارض کارت زرد گرفت و چون زرد دومش بود اخراج شد...
❌
در نتیجه هیچگونه تصمیم عجیب داوری به سود آرژانتین نبوده و مطابق قوانین رفتار شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99948" target="_blank">📅 17:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99947">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
ژابی آلونسو:
انزو فرناندز میخواهد در چلسی بماند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99947" target="_blank">📅 17:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99945">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLAi3uEGgNh2_LuGUfF7WyQt8df4PsFsLN5Mhfam4LUWi9At-s8BHt9C_TZN-tIAuRi0LKSpgRj6XM7L7wXt3ynsvpY6bFevLjBtal9n1ONSdyxLjrVKCE_ZFpIjvkNqi-KuYvchIeYCHO1pdNp5596FNpP7fy-HZGzwUJHpRW43YfyLSmK6AchrxyVnqzY6P70angz44fAw3mecwF-xustks1Zh43mqJX8ACbh7Kp1JE5zH7fe2vsNe88ZzeON7xaZwhLbSYlekMo27acp9Iai0WfyBQ_lsavXJ-GAK9tFhCL3WUpWRUlJzHSa0QgEaWHdvl_2OHnNVsCcV77P7kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو: لوکاس دینیه به پاریس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99945" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99944">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PncgdPLScyhH81lfXf-zbnqdIUDKlpL5p6BwMBLnyDDxRj8-IzSA63d0t8SK846CsUWJ0iC0NUngX1dllEkapoF-ZjZF5d4qIteUzHMi_QGCuXpYPf0l-6CqghQWKPOBRr_pE3zc_jW__FCnRmcTlkqc0PlUdYZRZ2bt_AVjEH3cPCBA2zjAhoJFien2BzVkMxVRpWGrI-cbhkwG-RqFdYROzeSaX44gr1bUUrItHE__kdBKJSuqC9q7grghbAVz4P29jreWDZctWAecwhodq88ism8Jtw4K5WmeVvv_PpGwSKU_oSbQ-NLMUhy7cesgLcINKIaBGd6x4i7kxQwdaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب احتمالی منچستریونایتد در فصل‌بعدی با توجه به بازیکنان فعلی‌اش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99944" target="_blank">📅 17:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99943">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/as9Er5NVujF2avYEIwJnYZxLkuHlqeyVQTpQfKNr8C2inqDyMP7kQL3pVkpSj0n1CR27GKIBPf9zdJjNjLfhPHurUdDTXXI0UvRrxDvOcW2XGm1rSm0TflJX-rzQQQDjbZO_-m4EwZeMLokSBoU4OZjZ2deJWuQ4oHQTAPkmjdTYQLn8PAlCnsW_K9VX3aFYAxC78DgEsvcvf_7Fi8lPg9UeGt8wz4S6RKeqohWGRWTaRxPKouOSdkzO26E21ydHF26RXQTG2AICI1d2A44qDeDVjZrldqz42C-Ea4ePiz3cXgK6Y1IOt_Ab47FWr8-UHjMDfUAGjf1pHXjG1DGF0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو:
لوکاس دینیه به پاریس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/99943" target="_blank">📅 17:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99942">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d594556eb.mp4?token=n7LzaGqi2Z_17xye51obpOp4BcbywFClEwOw4LzJOWVyi-0jtfI9VLLAYMEjhnuJL1EW2cep0OoA7IY_v5Cv444fqDUeDLslKaZovkkm84FDh6ELcs-4zKf_xsNhM0WqrxUjjKEa_u_2SJ1sBSCjYDtH5SGBXwqyQ4vfw42Kr60WDOH4BjegNmM9M7LFp1kLYMDmFR0axXf864Vz0RlErfnnJFwR1rdpYxU1sdRTVuCd5TgPwyRITjwbYmGvWZ3R9Ls__WBETX3Zc4ZnnkSoOMwp74QqacBNM-J5BVJS4o3f6Tj8wt40cWWJn0hh5RU7qSo0P2MmLA5LNwnXX_TSNTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d594556eb.mp4?token=n7LzaGqi2Z_17xye51obpOp4BcbywFClEwOw4LzJOWVyi-0jtfI9VLLAYMEjhnuJL1EW2cep0OoA7IY_v5Cv444fqDUeDLslKaZovkkm84FDh6ELcs-4zKf_xsNhM0WqrxUjjKEa_u_2SJ1sBSCjYDtH5SGBXwqyQ4vfw42Kr60WDOH4BjegNmM9M7LFp1kLYMDmFR0axXf864Vz0RlErfnnJFwR1rdpYxU1sdRTVuCd5TgPwyRITjwbYmGvWZ3R9Ls__WBETX3Zc4ZnnkSoOMwp74QqacBNM-J5BVJS4o3f6Tj8wt40cWWJn0hh5RU7qSo0P2MmLA5LNwnXX_TSNTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🏆
هماهنگی‌جالب مسئولان برگزاری مسابقات جام‌جهانی قبل از آغاز هر بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/99942" target="_blank">📅 17:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99941">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfVhuL4J4tv8xly37QISpmq0MaPN8XjAVDOXjEl64QVF1bL2SIQUlyXR8KWrl18t0vGI1FnSwuAHPoZ4MvFM_DVMNvdrBZDqnaiisgqzrZhyVetIagpRZ68ImKs2fkn01mCvfubFzFbJKX8ZatKdta6HzDCq4UO0xH7N1lKrUo1MfEssZf78kNcdCNa0Wu4GDyo2jFgZxjEixA6VWR6qhAeqndLp5h-9FPgNnlO-tXZcw2i3sBeBm_GH4MA0OA3EOnzGjGosMkUcP1xXFrbuzNYNWQs1hyP4kRmUuAzB82e_7e31d3-YF0EP8l12Jfkaqm4QMFULhJbCQpJFvIKH0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملکرد امباپه تو 2 جام جهانی اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/99941" target="_blank">📅 16:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99940">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPSLxFIE3l2C0zy-Vbg7VTnOKZXhOBKwYEOqVHqRrKAK_9kYKpALCrAZxzQr1MSk87Yht6sT3lRkNC3P9gMj_fWQDJfnasHKi6oE06oFKeUIGXzQ43v5Q5m9PYNvakiPIjH4I5xIUI_ilHsnxUtsEQ7LOCad7rBsBuyYJAk8iQLxpqN02__TbOBoneA-aT8MdsOO9VYCEH3mzg4CE4mhbGEgEg2-qGSwJ0X9jmruQruIUZ8rrwc5vnY2hDNnenKgOZU9nVk2Og49dWWjHf7ce0adqc9cx2DAs7pyGOKqFJ_kVlcR9mVaID-gpvfVcTCXDT6eaqev-oKzxy2zwEeZQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بیشترین دقایق بازی بازیکنان هر باشگاه تا این لحظه در جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/99940" target="_blank">📅 16:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99939">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/99939" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">❌
با هر 1 میلیون شارژ ،
🅰️
🅰️
🅰️
هزارتومان شارژ اضافی بگیر
🅰️
بدون‌قیدو‌شرط
⚽️
تنها سایت مورد
#
تایید
ما
✅
اپ اختصاصی بدون فیلتر</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/99939" target="_blank">📅 16:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99938">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1pzLui_xaZQY5_Nx4fry0TzUPhHfYKWg-hdVTQTW216---vP9zITokIgP-6_FRMxbp2zcmmktIeNRXmAe9zOXt1cGcI55MxvycjIAW8CkWNsrq5CkOwaM86vjE23qoI_tCAqUc83R9v0bjBbjr88U6UBCryLRujOnz5aMrGpAaKxoH-jBqnqQgz1_Oxe3geu2syv-IRxvv6xmeM8BJjf8Vqx6N8q74bk0y3QWY7XarkSVSSVr7splCTrgQu2PjzpB-iaLM1UbkXPRhu6rCRmguuaAkaC5EVZPZnzV-DIb8LBJByM8I1gNS8g-NsANqBN5JVUPegm9D3998QrszWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تنها سایتی که ریسک شرطبندی
🅰️
🅰️
🅰️
آورده پایین#بت_اینجا هست،بخاطر اینکه :
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی میده
+
🤩
🤩
🅰️
کش بک بابت هر باخت
🏅
بهترین فرصت سرمایه گذاری و چند برابر کردن سرمایه :
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r21
@betinjabet</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/99938" target="_blank">📅 16:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99937">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef0fc183e.mp4?token=OwbUu9-zNHR1gTOO5yEKDE3C7zvXVkwM9RCb8PXiliE5xPPhER_4zbe4wkdhKeRqBHlTNoaaPzPs0Vj_bm_M126N_a723DAMJOK73D4LJtf9ny-OfGzZZk3kDT5MGHMs5Up8EL_BvwzHJ9JlDrPNrcXt__hmf2bmT5g5Bh5ci3WdY6G5jUjKbnXMYwnBkiafOujTxsKc6DBkGZJyxeCCJFNqEtMQkBanhUPIFyIoAxic-xZCKGnUVD5y5lR7Vnbe5-R5Dr4Sya7KIOsbtqrTIG2QgsvkKj2Qo7MowyQ-0aF4QOaKujYT78JW-tZqE5TfyVK1Z7cWJuAZLW0xR92L5Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef0fc183e.mp4?token=OwbUu9-zNHR1gTOO5yEKDE3C7zvXVkwM9RCb8PXiliE5xPPhER_4zbe4wkdhKeRqBHlTNoaaPzPs0Vj_bm_M126N_a723DAMJOK73D4LJtf9ny-OfGzZZk3kDT5MGHMs5Up8EL_BvwzHJ9JlDrPNrcXt__hmf2bmT5g5Bh5ci3WdY6G5jUjKbnXMYwnBkiafOujTxsKc6DBkGZJyxeCCJFNqEtMQkBanhUPIFyIoAxic-xZCKGnUVD5y5lR7Vnbe5-R5Dr4Sya7KIOsbtqrTIG2QgsvkKj2Qo7MowyQ-0aF4QOaKujYT78JW-tZqE5TfyVK1Z7cWJuAZLW0xR92L5Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
حمله بیرانوند به عادل فردوسی پور به خاطر اصلاح شایعه مجری صداوسبما. شایعه‌ای که درباره تعریف و تمجید ژوزه مورینیو از تیم ملی ایران دست‌به‌دست می‌شد، با توضیح و اصلاحیه عادل همراه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/99937" target="_blank">📅 16:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99936">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
مصاحبه جدید املاکی: یک توافق داشتیم و آنها آن را نقض کردند. آنها توافقاتی که داشتیم را زیرپا گذاشتند بنابراین ما فقط قرار است به آنها به شدت حمله کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99936" target="_blank">📅 16:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99934">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92cdfd4ea7.mp4?token=n4GC2kt3liL7VsZ0EsztDkLNWbJKv2U8LBEdm45LRslW6wE2e4nZ_bER1XIvxaFrNk-eZUvpUl0TgnPimf5UryFHbg4HwtXRmvNN0cONPOlifxQ_PGY4cvQwXHuTtNT57b3sDvqQfkJYHjHGYhghEkD29a8BPmu0d7Igy6SdnkgOW81IMl4dT0giBw6MvqnpLbuw1v5nI8fS7W_yTIB--j7vHAmaxflSMr3TiZdUcbrEdiP0ZYhcQPmD2oa0eORyf5Jr41WojSKNvrE0nJbEQI__xRzeWo4R-vIM9xqBgGVWrMFRq0NQUIfk0qZLGCPrwv9_ygWuv0Dc7TPsZXxc-h9UZ0mpBd_4ojKu4USioa0mO64oUGSVr6sZCA5cxbC4D9WAkLRGfIWXUmtFbqWpsKzTU7UvRrcOE-nzPeqwM2L0ibjeF6y2E5OyJAgLdlpH7tiXHiTgQ2RaN3gEs2BBLNNh7MmLOB0VQ6JL92lTSSDrfEykJ72r0e3TGH3-R3fqsZBzTVHVFRq4DunvCATk8YD3ZGgl0HO7igZOgCp66Fy-MJWsvLD-sxPTauHjQ1YNnMRHU0uGBivX1rNRT08tH4MI_6wX2d4U5UVKAf2y_JkNXP2HmzpZKlBQMXmsmlGQlCkkKoWCex7eGUFWVzlD1dXxkGcmntcOzsZX3FWCm5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92cdfd4ea7.mp4?token=n4GC2kt3liL7VsZ0EsztDkLNWbJKv2U8LBEdm45LRslW6wE2e4nZ_bER1XIvxaFrNk-eZUvpUl0TgnPimf5UryFHbg4HwtXRmvNN0cONPOlifxQ_PGY4cvQwXHuTtNT57b3sDvqQfkJYHjHGYhghEkD29a8BPmu0d7Igy6SdnkgOW81IMl4dT0giBw6MvqnpLbuw1v5nI8fS7W_yTIB--j7vHAmaxflSMr3TiZdUcbrEdiP0ZYhcQPmD2oa0eORyf5Jr41WojSKNvrE0nJbEQI__xRzeWo4R-vIM9xqBgGVWrMFRq0NQUIfk0qZLGCPrwv9_ygWuv0Dc7TPsZXxc-h9UZ0mpBd_4ojKu4USioa0mO64oUGSVr6sZCA5cxbC4D9WAkLRGfIWXUmtFbqWpsKzTU7UvRrcOE-nzPeqwM2L0ibjeF6y2E5OyJAgLdlpH7tiXHiTgQ2RaN3gEs2BBLNNh7MmLOB0VQ6JL92lTSSDrfEykJ72r0e3TGH3-R3fqsZBzTVHVFRq4DunvCATk8YD3ZGgl0HO7igZOgCp66Fy-MJWsvLD-sxPTauHjQ1YNnMRHU0uGBivX1rNRT08tH4MI_6wX2d4U5UVKAf2y_JkNXP2HmzpZKlBQMXmsmlGQlCkkKoWCex7eGUFWVzlD1dXxkGcmntcOzsZX3FWCm5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تقابل تاریخی انگلیس و آرژانتین چهل سال پس از بازی دو تیم در جام‌جهانی ۱۹۸۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/99934" target="_blank">📅 16:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99933">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MT3p8IiX3zMzJohaocdfM8POq0EJs-QYYNdE7NMkxmW1zEVyFnwBj0kBMd1iF_0PqeOhFA1EanDnbOYE6JJwWtUyoqYxH6KHOfKmpn3erXfMEYphDfWG6TAZMa7QeR7Sil8bKXEV7BUmX1BjTcuid1DBemIwXbNqX8lD1YfWQkVSYJQIa11lcS75QRIUlWSBDfsNWsQnUQOkwdtpnIi8dh2wZoq0KXF1j_RnfcpBr1lD4VDqgBDtMOslbkXOO8dqMXH1O_LgTP67wTe_VDeVaTKkctXKlBke3uKyqvx9TuDO1glegngoG6yGCRENPpzc12dRf_ooozn2mPjhxv4x4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: بزودی یوری تیلمانس به منچستریونایتد HERE WE GO SOON
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/99933" target="_blank">📅 15:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99932">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wn_yrDLVVLfRVvET2XqlqXhOopnVjrdMFjlRB2pvGosIUeEX9zLX-79Kjg-5hFD1HdP85ARwsA3FY9pBWSnmkgxZ387IPfu7qXfoRpxZvy75B7z6MSmfgNIfTVCX1LJq0sE0Z8Vmidz6bjBQTpUfaMWLWMuWAmBwhE0QIeZ4KqH5ZojCopkfKF_-5sLqZXzovCPJ_M-dMxje3Q5GYKuGCaObgm359hbWwH02y8I0_2YcxVnXXLy3yPwpsbgSaxeVs_-S3hAG1IR_-_ZzFUpnPgPCW2df3Pn5Y4uaIeHgRGw6nTV79wOmtr8TeJ9Rwbd7xyxfEuWCPifQjwFGkHkQ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عشق بارسایی ها تو تستهای پیش فصل این تیم شرکت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99932" target="_blank">📅 15:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99931">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇫🇷
🇪🇸
تیزر جذاب از بازی اسپانیا
🆚
فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/99931" target="_blank">📅 15:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99930">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/155791f176.mp4?token=X3kIjuKnvGD1EDLluy872Vb5nL99gpZmVsnUjpmyRQURMe1D9haL7CiduEBB9EbXElfo3QHEuYpIYrpa30xDdF7rHBBTIxuVDOnKOCSame504bvXRUZm30d0gOSIHZDa35zjNaqHUx6DO0DYCiqQCXG6g2xUMGbynWiW-JNnakcKqycck9Zxqtv_K7v9A0pQXo2nzbdJ-j4xRRZ1-KVzLsggE0wFKIndz9uOqPo8EsaBeJLXSLrxwUYwnew1PSUmY5QUrkXSvAf3BmC5RzTnt4O12P8C5H66n7BEgCrVCNQ0zFaWDlamScB7sYceUlsc6pV4XE29KoVcv-cmgkchEL4txWyL0-rouu57Rnyhg760MLYXVkJ2Bz_YDA_pZIvGpnR3PkIQyFZTE2uMLwplq_1LyGwt7hZCc3ds4P1WFnIz6JKd9w1rclIWUBuJDheSwCJ8VxtdywtngitZ8vUM1b_3Po-ewFnWBJ9mqZh96fHxHwUjx_7Qmv38Y6w_juBTfiTSzqC2Eo074yJGkhQEzWqTj0mej88OjFCAlZG9y6LuvYRom3PJ2qUsUgJG320qKt8F8Tn8mv8IqEdz_lUbnA48qMsOWb3fYiFRixTmIt_z-1XGO-uFl7SSERR9H6zsSlM5K3H1KxApIMkG50km56Qs5nynEKvDTkZGUGxu1Xc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/155791f176.mp4?token=X3kIjuKnvGD1EDLluy872Vb5nL99gpZmVsnUjpmyRQURMe1D9haL7CiduEBB9EbXElfo3QHEuYpIYrpa30xDdF7rHBBTIxuVDOnKOCSame504bvXRUZm30d0gOSIHZDa35zjNaqHUx6DO0DYCiqQCXG6g2xUMGbynWiW-JNnakcKqycck9Zxqtv_K7v9A0pQXo2nzbdJ-j4xRRZ1-KVzLsggE0wFKIndz9uOqPo8EsaBeJLXSLrxwUYwnew1PSUmY5QUrkXSvAf3BmC5RzTnt4O12P8C5H66n7BEgCrVCNQ0zFaWDlamScB7sYceUlsc6pV4XE29KoVcv-cmgkchEL4txWyL0-rouu57Rnyhg760MLYXVkJ2Bz_YDA_pZIvGpnR3PkIQyFZTE2uMLwplq_1LyGwt7hZCc3ds4P1WFnIz6JKd9w1rclIWUBuJDheSwCJ8VxtdywtngitZ8vUM1b_3Po-ewFnWBJ9mqZh96fHxHwUjx_7Qmv38Y6w_juBTfiTSzqC2Eo074yJGkhQEzWqTj0mej88OjFCAlZG9y6LuvYRom3PJ2qUsUgJG320qKt8F8Tn8mv8IqEdz_lUbnA48qMsOWb3fYiFRixTmIt_z-1XGO-uFl7SSERR9H6zsSlM5K3H1KxApIMkG50km56Qs5nynEKvDTkZGUGxu1Xc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😆
امیرحسین رستمی
: در برنامه شوتبال من خیلی از مهمون‌ها رو نمی‌شناختم، به علی علیپور گفتم تو جوونی بپر سریع برام یه لیوان آب بیار خیلی از بازیکنان تیم ملی میومدن توپ رو نمیتونستن گل کنن ولی من گل میکردم اونجا رو کات میکردیم از اول میگرفتیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/99930" target="_blank">📅 15:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99929">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrLYaRZPo9T94UOBy3JmGxFtM-Hfh5T3Fmtw3g2YR1vRytq52w1-TVtHuWtTYVaNQB4RbNfRprjoQSfSg19v4RjsNiAfQiT1jdO8jWdBgl1UVgKe4wdJi_8NzUXnDUntNqAT30Rjx48Qf_gD9Br6p0lf2lpT8BXWmxstBRe4JXI3R4HNulahcs0D3W34ERbXcSDe9INNXXD4aExbEENFOvyufxhVh6ESaD4l23Qb426IH5WsHCz3dM1UzEjHwzAAg2EKU0ZDKxy1uYCOChEIhfsmYOaT8Ut6jI4E51ScPkBoql37EVDj92FzNT3Wh2YOKwK-__SnHc9vH5OtJWaD6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه رم قرارداد پائولو دیبالا را به مدت یک فصل دیگر تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/99929" target="_blank">📅 15:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99928">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb6395bcd6.mp4?token=QZm3rr77Q6BAav0mvgDaEoyhe3RgFdSAjt7SljVAHuHRw_jD32GY6JdfLAdN4kmSpIfM2Kcu8RK5xqMWz7TCABa1X2DFDAQE3zHm75evUN4jC1BL9pc3qT_MMLHrzPl4iXTAW5VSFauvmvfaG1sLypu8FOLVEu71PiunPpgtMKRiGgrdx5TOTOmVxirgWE79DDo-XmiOn789uO8xu6zX-cFDF5PaoJPE0fK9MrFcDKSvSqPSOwyLxvP-RBCtLo2jh4sIM8ehkZvozxKGv0WCvUa7ijY1V8PK6cGdfFCRCvba0ZeEhsWNxWq4nf3iF76WGEIzxGxEIm9DnTv5rezFVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb6395bcd6.mp4?token=QZm3rr77Q6BAav0mvgDaEoyhe3RgFdSAjt7SljVAHuHRw_jD32GY6JdfLAdN4kmSpIfM2Kcu8RK5xqMWz7TCABa1X2DFDAQE3zHm75evUN4jC1BL9pc3qT_MMLHrzPl4iXTAW5VSFauvmvfaG1sLypu8FOLVEu71PiunPpgtMKRiGgrdx5TOTOmVxirgWE79DDo-XmiOn789uO8xu6zX-cFDF5PaoJPE0fK9MrFcDKSvSqPSOwyLxvP-RBCtLo2jh4sIM8ehkZvozxKGv0WCvUa7ijY1V8PK6cGdfFCRCvba0ZeEhsWNxWq4nf3iF76WGEIzxGxEIm9DnTv5rezFVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
انتقاد بامزه فیروز کریمی از مهدی طارمی: «میگفتید دونده می‌آوردیم جای شما!»
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/99928" target="_blank">📅 15:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99927">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cee2da53d.mp4?token=j6ZWCSqXe3sXM_HPN08xqMa-GQUjHFzkbBv1I_RuyK8PFVg5vGQ2VnAm3GwFJbxvzWYt3lQbxjf0qbRCTAu2bnoZyDoDfM05n6yi8iRkJEXoTfOOnK1uhmdtBU79vLtwJMxe7R7vGEge-LBp89pGIwf-GgGRxh1tsbGUu0sk7Fo0AQl9HdiBwO8svnNYsQ60qJC3mQ_pg9Xy7js3hdqdWYJQ_J_eOToapji9NRVhcFF2DdYMK7tsrXK8EfJWlxXrHEp3Fs7zG2H428VNl2M8-7lZh4SPnQfOgw8i_LVnMCMARxnxqe99N2UCTHR4GqaNMsxm08Lw3-hzoCinFVlIlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cee2da53d.mp4?token=j6ZWCSqXe3sXM_HPN08xqMa-GQUjHFzkbBv1I_RuyK8PFVg5vGQ2VnAm3GwFJbxvzWYt3lQbxjf0qbRCTAu2bnoZyDoDfM05n6yi8iRkJEXoTfOOnK1uhmdtBU79vLtwJMxe7R7vGEge-LBp89pGIwf-GgGRxh1tsbGUu0sk7Fo0AQl9HdiBwO8svnNYsQ60qJC3mQ_pg9Xy7js3hdqdWYJQ_J_eOToapji9NRVhcFF2DdYMK7tsrXK8EfJWlxXrHEp3Fs7zG2H428VNl2M8-7lZh4SPnQfOgw8i_LVnMCMARxnxqe99N2UCTHR4GqaNMsxm08Lw3-hzoCinFVlIlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😞
😁
عذرخواهی علیرضا بیرانوند از همسرش اکرم بخاطر تشابه اسمی که با اکرم‌عفیف داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99927" target="_blank">📅 14:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99926">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3c7adc098.mp4?token=lnM058BSfCjjQzilTvQnjGS0yTE6q3ZTs0vOvtZro7tu_e0M_rE-vsbEujBMlI-M0ABQaRKA8PzaMIe3vbiv18gJYzjCrEiVHyq7uB3GRyfCUF91dKIlIEmNeLFNcrEhlxqwG5n3yoTXWidHH9cTqt5dUDq3VVXf9VeFP-T7daAh0ILISZIY-4KmuU2xgLQiBJYWIPCPUUeOflsmouT50YS1nT7bNPDdW0y5pUjnATpEWyiOWLmZBQDrPa59ByrI2nLIFpQ_Rk84qaY351g0pPSe5Aj3OICnFXrFqdw2FJH6l5uhYOEFGWgQKpq2GoeIaXLdiO9YYcySjzf-R9WhcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3c7adc098.mp4?token=lnM058BSfCjjQzilTvQnjGS0yTE6q3ZTs0vOvtZro7tu_e0M_rE-vsbEujBMlI-M0ABQaRKA8PzaMIe3vbiv18gJYzjCrEiVHyq7uB3GRyfCUF91dKIlIEmNeLFNcrEhlxqwG5n3yoTXWidHH9cTqt5dUDq3VVXf9VeFP-T7daAh0ILISZIY-4KmuU2xgLQiBJYWIPCPUUeOflsmouT50YS1nT7bNPDdW0y5pUjnATpEWyiOWLmZBQDrPa59ByrI2nLIFpQ_Rk84qaY351g0pPSe5Aj3OICnFXrFqdw2FJH6l5uhYOEFGWgQKpq2GoeIaXLdiO9YYcySjzf-R9WhcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چهل سال بعد از دو گلِ تاریخی دیگو آرماندو مارادونا، این بار مسی مقابل انگلیس قرار خواهد گرفت.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99926" target="_blank">📅 14:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99925">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1294ecf8b.mp4?token=h8onuXgR8VW7IyBQYpRZTmeXo5OhK2cZH1V_VdqpziRu4dhBvblVOVhXNYAVRJ4xskAhg5HoNQhcVj18PGud5RgEQn6I1vYIuEMfxFK_l1nGr_PuiCHN_fqE5ZcwVEgN-oW_FJJ5UrCD5OB1SdnzQRkMJcEdPRKpC6G_P19nmUPgQJJLhG1Pjf36WHwf3cS7q5yXxfGYptts8QJmuODtEPBZv2nlubbYhOGLeIHd-ETO_3-_LuYaK85J5Iw6ag_PlNF_xqfbYt7mtNM9p5ctRRtZmjI6CWN6SkqovfuT3FT0oETPZqf_B5eMBOGuTL1CGh9F11cEQZoBfVhzKmSjag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1294ecf8b.mp4?token=h8onuXgR8VW7IyBQYpRZTmeXo5OhK2cZH1V_VdqpziRu4dhBvblVOVhXNYAVRJ4xskAhg5HoNQhcVj18PGud5RgEQn6I1vYIuEMfxFK_l1nGr_PuiCHN_fqE5ZcwVEgN-oW_FJJ5UrCD5OB1SdnzQRkMJcEdPRKpC6G_P19nmUPgQJJLhG1Pjf36WHwf3cS7q5yXxfGYptts8QJmuODtEPBZv2nlubbYhOGLeIHd-ETO_3-_LuYaK85J5Iw6ag_PlNF_xqfbYt7mtNM9p5ctRRtZmjI6CWN6SkqovfuT3FT0oETPZqf_B5eMBOGuTL1CGh9F11cEQZoBfVhzKmSjag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
🔵
علیرضا بیرانوند:
مهدی رحمتی بهم گفت مدیران استقلال نمیخوان‌باهات قرارداد ببندن پاشو برو پرسپولیس من قراردادم رو باتیم استقلال تمدیدمیکنم‌. من‌ رفته بودم که دیگه قرارداد ببندم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99925" target="_blank">📅 14:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99923">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpFLp8xjrv-wiG8Oov_xDKoZNabLotV_Btpb8kKFThri54wibq2lkJ1xFDg_pF-vwyo3I5ynKTLu1DIH9_LeMtzBKfj20m3W6x0Ru7bnlkiJveEpolmlZf58gFzwfyuhRcVCamSprVrw1w5aa0oajARmw9GhyYEOngVImKlXa4xZECYdVwoqRA8DW8CeO9M1ccePw_GamSNkDIwHYgRQla5Zdzxxf411jPKsdI0UOh426gIdVzUuj6O1Kz8YnZlk4-ENML6B4Gong-R5ODmDEeJyIVtG1QWgw_FMUbycSTGY_ho-UQk5mKjVNiiizpiuwhH8FSrb98GZ0yOGf4DgwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xv-avCcAULzfX1BqKsEBfaSC-bM4WobGIQ2e6OiEo7NZ38ZC-A2rWQKHcIK6DLFGG6z98qmLrELmJPojDnIlCcDepoQUJEzJm3fbU8HfknhfTlwtSi10dbqGOGvnjlMeU_5IvkSrXGYsmVonB6p2FY74TlBscMmbg6D4EVJvPyiDwOU0aNhcO23sU-t-HhnObDHEWTlRUjHr4ysBpDoaItRSTuBm-ymuN_y_yg_mD8-1fk-7bB_A0H98lC5qkmmrZn3fYiL_pk5vvGguULqcG3IqDfu3olbRyeC7mBFwtCLO5K2_8AqGONY6vEkwZuvTsEvvzLq94DoEG21eTdNYyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏆
دو داور فرانسوی، تورپن و لتیکسیه، از ادامه قضاوت در جام‌جهانی کنار گذاشته شدند. دلیل این تصمیم حضور کشور فرانسه در نیمه‌نهایی است. این دو داور از شانس‌های اصلی قضاوت فینال جام‌جهانی بودند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99923" target="_blank">📅 13:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99922">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYiaMS_JbtGC04PQSRWbUtovqs34Bfubq8bWIJhmAJ2x9J307MtTEfsGEB20d7ZAA9uWNy27y9s7XlEjQQd_sy3VT9sGI5fFfFJUI6Z4KvrYUJLf7HMJswxXRrJ6VjtBUyH-VN1S28vBEJlwNigL1yqQcxi5wK4xENDgiWGTLHLnnIuW16jmQs2j36f1IMkyS6JpVyrK79OXOmuJXrL6JDkzGrzl2AZ54i_mgNU7S-ybw89VNPa6Bo7SbztFiBvx-hsK7TEYN_4Ip1oTcGnA8tdco2a7ey92gYIVrc617cv78DMOOXFiTbxxEySN5X2wjQAi3GYtvm24LMzY4g4ABA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: بزودی یوری تیلمانس به منچستریونایتد HERE WE GO SOON
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99922" target="_blank">📅 13:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99921">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bae154b9d.mp4?token=M-L-qwLHbQ3JEjy3K5KZpLq794JeabgbSYnR1Vkas3Ou_KMjA1ZrVKLU6yajsu6_I9pcfzQdE34Ro--w4KP_SR5lmOPWDCWHnF6JCdmgzNURxt4n-W0G9woDfGqLlxq4KPiVJeegtTV1KOng-HA-ZtakN90Ezyp0IFoLP0Bbj9tNIc_7zolASUSVA23ZMlpOE9OyeQUn6xekO9qpxs3tAriOSlqamWOyn_EgFIitwMvbqroifLR9l9niP0CK8Ym2FUMsibt6721ZN-YfHrVkE60M57gP7gAfbjPO9aj3SF0Q3FxfOd7Ba5FJ57HdQxuhu0-NMKqlJC3zGNC5TvFQ4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bae154b9d.mp4?token=M-L-qwLHbQ3JEjy3K5KZpLq794JeabgbSYnR1Vkas3Ou_KMjA1ZrVKLU6yajsu6_I9pcfzQdE34Ro--w4KP_SR5lmOPWDCWHnF6JCdmgzNURxt4n-W0G9woDfGqLlxq4KPiVJeegtTV1KOng-HA-ZtakN90Ezyp0IFoLP0Bbj9tNIc_7zolASUSVA23ZMlpOE9OyeQUn6xekO9qpxs3tAriOSlqamWOyn_EgFIitwMvbqroifLR9l9niP0CK8Ym2FUMsibt6721ZN-YfHrVkE60M57gP7gAfbjPO9aj3SF0Q3FxfOd7Ba5FJ57HdQxuhu0-NMKqlJC3zGNC5TvFQ4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرحسین رستمی: وریا غفوری رو یه ایران میپرستن...
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99921" target="_blank">📅 13:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99920">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggkK9hYkO5sUesKkGlg-ImGA1IEsVNUS0bwTGk3FkO0r3hLPCXqb1TCs1lyGbh9IWjRWYdkLMJJpwSdYAMXPrdWnFC4Vi8BrRDShi1aBm70BLqLJ3ly8HsTgsJp2Pf1pbJs4B34mdMVPCTq7kV6lU6IMIyzBZsUNUgQGsew6gfQ-P5YDMgl2swsARj5or-9Jx7IGLCT0aYwL99Nlx19IipSIkjfq3IoiqWTSaxUdknCJB2nHwfUum8WGMKZs4yb2ySXyeTP4h0x20Wzi--piL9EkZ1FIb309JECPgPoUXW1kH9OrAADPLz9HJCz3IPxNMwg5_5F308vsz2l9fzu8WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری دیوید اورنشتین: باشگاه منچستریونایتد درحال مذاکره جدی با استون‌ویلا برای جذب یوری تیلمانس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99920" target="_blank">📅 13:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99919">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
دیوید اورنشتین: باشگاه منچستریونایتد درحال مذاکره جدی با استون‌ویلا برای جذب یوری تیلمانس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99919" target="_blank">📅 13:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99918">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70585e20b2.mp4?token=imeiliULs04YjLGOWPhoci6SiU1RZASZImHoWJqbmrXA2yIyT4oDGExn8QGId_xMfgRF-5QU7mduxF1YRSKyFtPcfx6f0fMySahTq8yKI7lEWAfVad1oWdR_q_HdileB6VPlzvKG38VhR7_pk0ATo3PLW1nN10v3T55rqh0dxQLQqpCLTCFBpfOsWmuj3iO-tMSuUwBWQjph_og3HkXIKBjbLjzYHDjzAEmxD_G_F4z5glf20oTEmVVz5f1VXqp-ucupG0_PaOtaoEvJYitQMjvqqbdYnp5VFGhwyune9pSt9xwNAH-VCmftBC1_5zAjOP625_2rnzAKwRi4vbGIAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70585e20b2.mp4?token=imeiliULs04YjLGOWPhoci6SiU1RZASZImHoWJqbmrXA2yIyT4oDGExn8QGId_xMfgRF-5QU7mduxF1YRSKyFtPcfx6f0fMySahTq8yKI7lEWAfVad1oWdR_q_HdileB6VPlzvKG38VhR7_pk0ATo3PLW1nN10v3T55rqh0dxQLQqpCLTCFBpfOsWmuj3iO-tMSuUwBWQjph_og3HkXIKBjbLjzYHDjzAEmxD_G_F4z5glf20oTEmVVz5f1VXqp-ucupG0_PaOtaoEvJYitQMjvqqbdYnp5VFGhwyune9pSt9xwNAH-VCmftBC1_5zAjOP625_2rnzAKwRi4vbGIAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تیکه ابوطالب به صحبت‌های اخیر بهاره افشاری: لطفا چمن مارو بذارید‌تو کیسه مشکی اگه خانم بهاره افشاری ناراحت نمیشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/99918" target="_blank">📅 13:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99917">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7de78bd0d8.mp4?token=odOwj-EiyZDW9SpOjUGwymEHZbBabhhh1Tk-kEJdVSVToXsvt7XHPZ8r-iLlU7J64Gy3TJK8YZu9s4uTa2UBb28ZZUwhB4KUpH3KoIn-8FRLLNKnQ2VYXzN_ZgU5rrvxBuHaevIEdSLQIYLSlvSdk4iWEItV5WzuaNwbF-nAOQJ1KFYS5ByQtHPYMPxvd7_lYPfIVccP-BeRcWKhRS-r0eu-rlzRboF8pqX-_D7twBdRUd2-Jzk0aobnrc4C7g_GqcwuhTlihDBSAUjmQr6DsHy2ZZ3jM8muLXUPE-LaqI1A6rJIxFOCyZ8HvkivnHRJEd_2CyFXRbfye3qtw7l0ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7de78bd0d8.mp4?token=odOwj-EiyZDW9SpOjUGwymEHZbBabhhh1Tk-kEJdVSVToXsvt7XHPZ8r-iLlU7J64Gy3TJK8YZu9s4uTa2UBb28ZZUwhB4KUpH3KoIn-8FRLLNKnQ2VYXzN_ZgU5rrvxBuHaevIEdSLQIYLSlvSdk4iWEItV5WzuaNwbF-nAOQJ1KFYS5ByQtHPYMPxvd7_lYPfIVccP-BeRcWKhRS-r0eu-rlzRboF8pqX-_D7twBdRUd2-Jzk0aobnrc4C7g_GqcwuhTlihDBSAUjmQr6DsHy2ZZ3jM8muLXUPE-LaqI1A6rJIxFOCyZ8HvkivnHRJEd_2CyFXRbfye3qtw7l0ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روحیه ستودنی حمید علیدوستی عزیز در مبارزه با بیماری سرطان
👍
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99917" target="_blank">📅 13:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99916">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgoxsAlQ2NZEzqcQ-6PZJ6g52A7ZQzPHHiXBXLOw3HXzKE5cRY1EigbYPcYPNRjn2Kk46NIOtI0Hgx0YoejZbi8OZMUc1uYnS8YdtzZ1IbfjDxufKUyyrjIG2qR3iOwarXLLDKEoNLINVkqRebIsklNUOKvUPHzPIpoDmVJ6d9aWdNeqtlEp6LLsrr7hZqOIQpNnwBckRsjtt9LKv8pEGkEQkfjPKIFWnBEZjQAfw4H4jCCBR-v2niEmctgpCGzpcO-Xb9aDyIRS577iu79aRJdU68yl6fLIS5eNOv9eO9aReKYYOLpoeC8rNUH5oOsl4sxJHBg-SHnvSMieijd3rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوری از رومانو: رئال‌مادرید درحال مذاکره برای تمدید قرارداد یک بازیکن بسیار مهم و حیاتی است که این بازیکن وینیسیوس و شوامنی نیستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99916" target="_blank">📅 12:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99914">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b696c11339.mp4?token=aHmIkF9ZS5pJhy9ptXxke3bPEl0gmG-2qfoDyvkc-7S1p2KpC0YouP3lbPFG7kAqM5HFC2q48eigBYlHMJ01XAB4uI63zA6OfgZvyeMeYaq5SwrqrQgYS2vYIElHabeo0POXZX-klom7JAVjhAsbuTvx9VHUJ2FQYisIbkUH85w4c27vQVpQNIyf7eRP3A-1_JeMtJ7A2PdLxhZPKN8_WCjGdWO95pg_Qj-zUxIVAvyWmG9eB-NzifCRlhjw3kT4nlYKgItPFe0EWQVc2IqRsCgFIRqfEPVEXE7NDm5iLovW5Qbb42YjXRNE72rKSFjkVtkF-f8xT099S18-YfoDnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b696c11339.mp4?token=aHmIkF9ZS5pJhy9ptXxke3bPEl0gmG-2qfoDyvkc-7S1p2KpC0YouP3lbPFG7kAqM5HFC2q48eigBYlHMJ01XAB4uI63zA6OfgZvyeMeYaq5SwrqrQgYS2vYIElHabeo0POXZX-klom7JAVjhAsbuTvx9VHUJ2FQYisIbkUH85w4c27vQVpQNIyf7eRP3A-1_JeMtJ7A2PdLxhZPKN8_WCjGdWO95pg_Qj-zUxIVAvyWmG9eB-NzifCRlhjw3kT4nlYKgItPFe0EWQVc2IqRsCgFIRqfEPVEXE7NDm5iLovW5Qbb42YjXRNE72rKSFjkVtkF-f8xT099S18-YfoDnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
آتش‌زدن پیراهن لیونل‌مسی در مصر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99914" target="_blank">📅 12:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99913">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb9971900e.mp4?token=RcOMLEnFhbaP8KGZc8Vz0IU8-1zS_bm-0KwqCXyJrnTZS-JgRGLzxw5rbDjNeI84GautbOxA_qK3H4V1-SBZYl49Ei1AsP8eiaD0sG-07Gpu8984B8PRenxBADSyxK2LoeMfOKNpKoRoJZ63viNBcnU9ctpb4JMcj8ctUulA87PeOwIN-lkzPPB81qw8LG81Sl_2Q-e34RaYBkv9VE72sTLLP5AYurbRhiPDi7MvtJkCV8JiWtFVYS6-W95xyJvrjxJwsqA-P7htJGtxMDDw3OxlqyFszQPlgNHh39mbJipS7fS6826nIzuT_tWiPYxJ-BA9CuNdtqWfcZUe5_l_ynt1PktKmUIMUwxh3nFFcJ-rRTgVwTRyXNM0dKQU_ZrcFwQPiUOr4TL3zIs0ROu8y3flJN2drtoiO1avFP8c2Lr5Zw3u10pngp-5ciNbyiwCa592BnrVO7CLiejK37qwdCQQlVzsrTa-bJEBNmohgOVKtVWXOpVL5PdE3qNRnesJCfzPn2Wv3erfq2fIHS3JPnmJnjokP0tY-FZO9Kd8PbfP4HC1xlnjpWOgH9YOptI9qoeLCzEyhq0U3_uZfKMlFYuFYw3N5-lwcv6SvOQSlzip1jG87ITxk_scnrArRtfZW40kdXTyHKM_gaEP1gK3FnTnUZz29v-srdEELBdvPYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb9971900e.mp4?token=RcOMLEnFhbaP8KGZc8Vz0IU8-1zS_bm-0KwqCXyJrnTZS-JgRGLzxw5rbDjNeI84GautbOxA_qK3H4V1-SBZYl49Ei1AsP8eiaD0sG-07Gpu8984B8PRenxBADSyxK2LoeMfOKNpKoRoJZ63viNBcnU9ctpb4JMcj8ctUulA87PeOwIN-lkzPPB81qw8LG81Sl_2Q-e34RaYBkv9VE72sTLLP5AYurbRhiPDi7MvtJkCV8JiWtFVYS6-W95xyJvrjxJwsqA-P7htJGtxMDDw3OxlqyFszQPlgNHh39mbJipS7fS6826nIzuT_tWiPYxJ-BA9CuNdtqWfcZUe5_l_ynt1PktKmUIMUwxh3nFFcJ-rRTgVwTRyXNM0dKQU_ZrcFwQPiUOr4TL3zIs0ROu8y3flJN2drtoiO1avFP8c2Lr5Zw3u10pngp-5ciNbyiwCa592BnrVO7CLiejK37qwdCQQlVzsrTa-bJEBNmohgOVKtVWXOpVL5PdE3qNRnesJCfzPn2Wv3erfq2fIHS3JPnmJnjokP0tY-FZO9Kd8PbfP4HC1xlnjpWOgH9YOptI9qoeLCzEyhq0U3_uZfKMlFYuFYw3N5-lwcv6SvOQSlzip1jG87ITxk_scnrArRtfZW40kdXTyHKM_gaEP1gK3FnTnUZz29v-srdEELBdvPYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینید و بشنوید از سرود زیبای بازیکنان تیم ملی آرژانتین در رختکن پس از صعود به نیمه نهایی جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99913" target="_blank">📅 12:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99912">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
❌
🔴
مدیریت بانک‌شهر بدنبال ایجاد تغییراتی در بدنه مدیریتی باشگاه پرسپولیس است و اگر اتفاق خاصی رخ ندهد احتمالا پیمان حدادی بزودی از مدیرعاملی سرخپوشان جدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/99912" target="_blank">📅 12:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99911">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QB6zMF-k2orqCo5rUX2wdbsObhi_C1oYUq8asU5yhF5e7DecWYMxHojMnNPxLIGUQth9l1S_N1TTrAGOPW3HxmLkOKtGxIOgAsJ6zDt3InIQXQ3QWaKftNBbc_dFyvBcuQPtrz0V65Y9qn1ONUiL-sf50hrFoLL0FiKQWx2vdt7yLCP8HWFVErhLyMNGSwfpB6bj_fZO-cU1eJULy5mwHBqFLa0dePy9m0a4FydITvfTP7i4udKYNI54YkjERZWKVFJceSeUIuppn-RYSX6KIn010KgQmKTJExEaMZioPC5p618EtoQCGHmH_C1ImxGhQN4o7mOhF-hoWQVCpvPbJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
👀
مسیر جدید فن‌های کریستیانو رونالدو :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/99911" target="_blank">📅 12:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99910">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_zlmBAUs8SzEqQL75amJYtlORWYciWdLkAEwu3V2L0C5fJufSayFDbPoN0QA_q-O1IZovJc5RD-y7GhpHdpUY52ANqD8xaQPEtaVo6CqKtTXjEP-q5X9PG2VmsJz-P4EAwd4uirw_8J5RTW591OctEt_q_hs3wS1e1jTKvnCYITogNCgKt-vkgbwbFeN70XbbeVVsontWFBh179bTxoahLt9ugcJBVeZxsf8Q9xbMOife1pXz4OfMAIOkyREGj4P8RAVnZW3n-mt3FnO6qZju7ehLTyZh66lQvwYgMRj0Vkv_jnyetlNCOPGu9xAJ8wX83zWbdLJU49ytRCN1iz1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🎙
ژوزه‌مورینیو:
«من سال 2003 شروع به کسب جام‌ها کردم و آخرین جامم را در سال 2022 به دست آوردم. این یعنی 20 سال افتخار و قهرمانی. به همین دلیل است که می‌خواهید داستان من را بشنوید. همانطور که می‌دانید، فیلم‌های مستند درباره افرادی ساخته نمی‌شوند که هیچ دستاوردی نداشته باشند.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99910" target="_blank">📅 11:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99908">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5142dd144e.mp4?token=Sf73sZFoUFx6CfqbdYu1w1kLAC19MrKFKUK-qRDf1ZUZn_Oskj5B9B0dBsdFQr7u9O11JAKYm5H_4-ZXJGGhmLsx9WZ-ZzFfSwOIj7UtH4l0yha8eYUjNhx36TrIcftaseh3a-o6rLaJAlqp5ohZjirnehklEkv2IH8wXc7ADjTT8wnQKgk4lth3dHF8gVXgQYnvE3MT9ou7_RUhy3W5EawIX9A4bMHD-RWGuMxbxr6EK7TVyiepuigntGw8UsegGSWwNUAkvRFtzxupIo_XofChYD0NY7ohkdDiuiTiOw8oE8zMBtnwDOK0DRYdoxXuv_ThzyW8Cwa_x64NgeYatQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5142dd144e.mp4?token=Sf73sZFoUFx6CfqbdYu1w1kLAC19MrKFKUK-qRDf1ZUZn_Oskj5B9B0dBsdFQr7u9O11JAKYm5H_4-ZXJGGhmLsx9WZ-ZzFfSwOIj7UtH4l0yha8eYUjNhx36TrIcftaseh3a-o6rLaJAlqp5ohZjirnehklEkv2IH8wXc7ADjTT8wnQKgk4lth3dHF8gVXgQYnvE3MT9ou7_RUhy3W5EawIX9A4bMHD-RWGuMxbxr6EK7TVyiepuigntGw8UsegGSWwNUAkvRFtzxupIo_XofChYD0NY7ohkdDiuiTiOw8oE8zMBtnwDOK0DRYdoxXuv_ThzyW8Cwa_x64NgeYatQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🏆
🇩🇪
سال 2014 درچنین‌روزی؛ آلمان با گل «ماریو گوتزه» در وقت‌های اضافه مقابل آرژانتین به پیروزی رسید و برای چهارمین‌بار فاتح جام جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99908" target="_blank">📅 11:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99907">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0uHZxR1vxjlrgzLpyfs88T6693fuElWVzLS_6kGp6B60EUuZdguOZ6FK7mUNY0O-zpeGDGveWDSmZHg7t2skJnaYKrITcC7rD9UVHItFFdxE9Ldy41o2eKZNgWY2oATwORMNlvdNuRL-OL347VRj54pCWY5HAX_1cRJB6RC-NarqHWJuxxssdotySN4pGnyAk6O8-9rV3uYH7o6C6SHjhQSdRXEt033HZUAH83r6HdurVgXggBNOx9QA3T92Or-BE_GgtmDmVJmWM_rIwN5DJY9Glg5vg8tZxFg9yeG3SEunDAY9JxNb6wSpT9iRZHMbkN5TCjKhEbjqcEnG7LMZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لامین یامال بعد از اینکه سال‌ها 18 سالش بود بالاخره امروز 19 سالش شد.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99907" target="_blank">📅 11:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99906">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/724b974651.mp4?token=W_K2KOpkqiMUvDteb0lO91M6j0HnJCYNkCZH33iP1MnNURO7e0pwYmbV4ypjeonu5iG3RWYkLgnH-Ib0QRlLHLIJdmgoZC26Ba0TxAGTDXQRRwRTxkMeOAjkh8TPVB8IaUC1CXcBvITLYdmYmQc7ko9vTiKLsHmF3OwJS7Pt2XMWR5GgAp1O1EfjORrdcZfXlZNkRhtYNFFZYjGmkfNaF-zWBDlLPx4DtpA4nWDnrMTn2PmB_l1-9N2F47TSS1X209OGsomD_88t5mS_0KoN0VzmrgY3ZtxBtafJXUkV21ivVyDlwppU4h81nM-FzyYjdeaZKrs0nIA0yB4U6zBNyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/724b974651.mp4?token=W_K2KOpkqiMUvDteb0lO91M6j0HnJCYNkCZH33iP1MnNURO7e0pwYmbV4ypjeonu5iG3RWYkLgnH-Ib0QRlLHLIJdmgoZC26Ba0TxAGTDXQRRwRTxkMeOAjkh8TPVB8IaUC1CXcBvITLYdmYmQc7ko9vTiKLsHmF3OwJS7Pt2XMWR5GgAp1O1EfjORrdcZfXlZNkRhtYNFFZYjGmkfNaF-zWBDlLPx4DtpA4nWDnrMTn2PmB_l1-9N2F47TSS1X209OGsomD_88t5mS_0KoN0VzmrgY3ZtxBtafJXUkV21ivVyDlwppU4h81nM-FzyYjdeaZKrs0nIA0yB4U6zBNyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمو رشید وقتی میخواد از مصدومیت بگه
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99906" target="_blank">📅 11:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99905">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmCwvfDzhkhQGDHTVlyG42ljPlBeaIDsSOzL8pDlEViL90cLjulxdZpdW-ru5BsdIwYj3i-F2NLW1WoLTis83kzZo0eP_GnTLj5JbUrP6sSgLtVq_-97bl4x3lzKAB25cSCF-sLffN0cW6a6VvcC_BocFsGSAWycSaBBMngY-9rpS3XXTc7TMTI9vOJALLefcfM3PyHaaDHrzjb3Pzcd3mA5OdJnR9FOkYV95jPhY749GYHgP6YS4jOMypBjUKtSPZ2ef1bzlHHhHpFGFucvIUJQ0LP3tP1stLgYKqS6Tlqk1W8sQ7zE5oPnt97jba0gyOZ0VoIgJJauhAHBMPrMwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇫🇷
🇪🇸
استوری گاوی قبل بازی با فرانسه:
اونا نمیتونن شکست مون بدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99905" target="_blank">📅 11:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99904">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2vOYj2cYnH0hr4UG7jK8plvhtLYiY06PVI0_Uqqn3nNSbN8fwaJUmSYvWBMI_QZ8YQe8JiNd6AGwkdy4s_lgIibczPAakDTuFA4zj2EMcAaTvKAbmT21wzddPHRLt4X13NZaRy37AfT9nneIkG84FpYVQcwYHOtAajA536ygkgiXQzpIEyV5OIGG1sSFtzxHOw1NmqSurtMCIjnE_gnGiyq1nw3U1x2fUvosDpdgOByjcrrv-RLKuaPvnXn4QXH-HKBMIPwxXVazaU6xk4UdYR_OVvNylgDFQ5MkE-XZ9og1KDaF-ihTbE1UfeV0DQJdYqwkVmdZm6G89qMUA3Atg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇳
نیکولو شیرا:
پاتریک ویرا کاندیدای سرمربیگری تیم ملی سنگال است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99904" target="_blank">📅 10:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99903">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e42b519e.mp4?token=cdj96WC4im_Q3eXx_mPsSvFvQvcxwZOr8keC9BRQew5rvoCh_OjvOpjqW_IxZ5hsArMz6ff6UtQx2I8_8VJyHTsd5kca4rFFCFBFlzRajFU_ORK2Gr5X7AkAGFsuOk_RmvwUglFaKhGon2UL5tdi-kvkk-RRazuzrWyCNjPUAYyOnf_V2y3mBTUid-VlXoRNOpDxSb7zSawRe_-bDshmXIAuAXSKVFHROL68_c6LFGXbuCkpY5Y5JsJQ8UwyjNOIHQVYGG8zgxRtOmoeVEde3joaVRpxi1tbfyUnk3D4EoY0zQgwW3mAsZpzNO3RsooTghrBMQHKmdqGJTAquSIj9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e42b519e.mp4?token=cdj96WC4im_Q3eXx_mPsSvFvQvcxwZOr8keC9BRQew5rvoCh_OjvOpjqW_IxZ5hsArMz6ff6UtQx2I8_8VJyHTsd5kca4rFFCFBFlzRajFU_ORK2Gr5X7AkAGFsuOk_RmvwUglFaKhGon2UL5tdi-kvkk-RRazuzrWyCNjPUAYyOnf_V2y3mBTUid-VlXoRNOpDxSb7zSawRe_-bDshmXIAuAXSKVFHROL68_c6LFGXbuCkpY5Y5JsJQ8UwyjNOIHQVYGG8zgxRtOmoeVEde3joaVRpxi1tbfyUnk3D4EoY0zQgwW3mAsZpzNO3RsooTghrBMQHKmdqGJTAquSIj9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصدومیت لیونل‌مسی در بازی سوئیس از ناحیه چشم که خطر به سرعت رفع شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/99903" target="_blank">📅 10:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99900">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7EYpyVYBbb4AwI1Whif_gpjau2lHztS-xb4cuB30jc5erJXRBspjuJuhQ8EbKrorIQ42nnZRkqWDSAgo6I3VuSE-P7tyVbMfNeKG_KDRU8RUXhkgyQgByP3qDN5KRdoMFtQdYtSLBxPEvQixPGBCYk0hHsvZaORK7jNyjho5-m46p4Nue9K-zeGCkfqGze7amtq8-uB9cUkDc7CwxPOK-zXhAHLIjt5t_yAajn_m94zshDn0Rz_QEEx_D-W7gpDT1UZr4PtjulOhPe5_GVmPizuhfoS9Z59eUE6RcAHEvt56AafrlPSYDw5_RMHRPEysbsxFhYhuvIOMBfPSJkMRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CbPB8L3Q3vY_21WyqqPndH4-pyzFWdJqlGdmLhITIvE8ijy00du8jAKPCyl7lgZQnBVccY-jVdYlQ20nKubOH1dpXfqZjD7iwCO1_WfQw45DCvbnAvc5TI5Dl2muB8ZmshBZGRdzNLWpsncREQj9JwPMLhuW-wv42VrvDnxsbptkn01srmQlOhM4xmH6z_cx8q6QyXZ3QIVb7Vnr32CYxjaOuma0zscwxNTFGanNhiSdkUktp9HlN_7-lCl5A4uwcL5w8CDZvThEG5ur6I2NgGBG4WiK2ttV8puInH-gKGbppKk3oLM1dsFuEWIpGb19jP93aCKhtHJn-umCA_X8ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sCdClMVV1imM_oquLG2BVo2NFfZ_IQ2YYDB5EHcOTPrvsN9Ka_yn7Vnyaf_xuqFPrwqt1ZPm55dMkQExphiqxIrBWn0e-pWT_oU0Fe125VweQiKM2nrA02G6fv99Xwi0X9Hc5lWa2hhRXGArVp-8M4k8Fa_5rVml8F_QjU8Zm5GuYX-nO3Szg1sS4kY8q1o4QkVggSIpVNm1EbKhXvBMUjG0SGuL-RhEb0YELpdC7blR2SG6eMBxHXVlDnuoS0FoQEpBaQaVAlGRyIGqm8Oz9tLuOXb5sgXeTf3qqqZCcvnrMpP2T2hgWzMSKQF6_-h2G6MJQDht30Q5pETkYNv8qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
یک سال پیش در چنین روزی چلسی با برد 3-0 مقابل پاری سن ژرمن برای دومین بار در تاریخ خود قهرمان جام باشگاه های جهان شد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99900" target="_blank">📅 10:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99899">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7079ceb818.mp4?token=byEJosRPQzCbE8Q945ssgMkQWI5dkUlHneh4-ynn8e4WGWr7AQj3-2RTRzumvms_NH9jB9DETI96h8kH6k28t1jl86EZ-bFOeVuNB2K-maTXncqPOc0u5fsmHKykVdu4r4yxLSyXa2POZcD80V_OZSKgO0gFycUyvTiF79bHiTuG1IJYB7QbYG-P-1_jN-83kvRXcB30cAxPy9ClW2YuW2wIFHOjFtRIbQPHYkCV_m7fyxkuz_uxMZ0nXnLQ-cMVuP8SI26-Mi6fk7aVqyyHIY7UobGjVV9lffJZhPCI5BmSIekdDjpoVNlLQe25cUEUbQ_7DusQri2d_6ApOeI-Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7079ceb818.mp4?token=byEJosRPQzCbE8Q945ssgMkQWI5dkUlHneh4-ynn8e4WGWr7AQj3-2RTRzumvms_NH9jB9DETI96h8kH6k28t1jl86EZ-bFOeVuNB2K-maTXncqPOc0u5fsmHKykVdu4r4yxLSyXa2POZcD80V_OZSKgO0gFycUyvTiF79bHiTuG1IJYB7QbYG-P-1_jN-83kvRXcB30cAxPy9ClW2YuW2wIFHOjFtRIbQPHYkCV_m7fyxkuz_uxMZ0nXnLQ-cMVuP8SI26-Mi6fk7aVqyyHIY7UobGjVV9lffJZhPCI5BmSIekdDjpoVNlLQe25cUEUbQ_7DusQri2d_6ApOeI-Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
جیدن آدامز؛ روایتی تلخ از درخشش و خودکشی در طول یک جام‌جهانی!
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99899" target="_blank">📅 10:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99898">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNoj7_vsVq6hQs8sc_qVXIN4uegDD3qcoFbgLnoqGN-ogHWVcDG8f19xmFTBSwRROF7WvU81qXnmZ_QCNuQBi-Ft4RBHdJcbKi0boatiQoJE6-HDxBZYKIIpwUTg93BvF8RNvPDVMdy_KxYOlauAFdfxfP8754D0uBa9vIjkgh4Ug9hj6g4kQOBgvFp_xhYgnoCn-FsZi3g2y5-u0XXpfzxFNX0b4CeIU9IoMfDCNQwXlcIYo8nkUp1HRZyQGpi4iL3CgC3tVbUlxC-p4Ugqy8DHNiB64hPETSi617wuvlsPKuKJt1Pkpnzxgj8ZXBKoQQ52Ommjq2AD6svUdzxv0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙️
نيكو ويليامز [
🇪🇸
]: امباپه یک بازیکن فوق‌العاده است، اما ما بهترین بازیکن دنیا را داریم: لامین یامال."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99898" target="_blank">📅 10:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99897">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2501cb2ee1.mp4?token=Sco9mMG5zlLCvyTPGfyXFVsRTS3ZcOZWqHithlrYjjWSYdgth52gCwsqmPJocZ7iLYowpp5HbL41dEb1WhTwGPqC7A62yf7iLFFPqOiBFlbqBKPnJlLDypi-ppZjCJpP775_8X6BHjEZZvUP-sNpMxPtTpoAAC8g2EyjGqje9uEPRjBPHiXFuY2yDYADuIicgtvbw7MpaoY-Px3gLBqnAUW4QMDW0kBTgGYog3iA-7sduEOUSZ8pLsWHena8qOGuMweXsxQM5ZWpN93vouym9zxFuQM-bbIfmZ4sDhOC-bYl-wLjqWc_qRoKn_7djEF0qhmkqLBuUBDns2urDZqIrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2501cb2ee1.mp4?token=Sco9mMG5zlLCvyTPGfyXFVsRTS3ZcOZWqHithlrYjjWSYdgth52gCwsqmPJocZ7iLYowpp5HbL41dEb1WhTwGPqC7A62yf7iLFFPqOiBFlbqBKPnJlLDypi-ppZjCJpP775_8X6BHjEZZvUP-sNpMxPtTpoAAC8g2EyjGqje9uEPRjBPHiXFuY2yDYADuIicgtvbw7MpaoY-Px3gLBqnAUW4QMDW0kBTgGYog3iA-7sduEOUSZ8pLsWHena8qOGuMweXsxQM5ZWpN93vouym9zxFuQM-bbIfmZ4sDhOC-bYl-wLjqWc_qRoKn_7djEF0qhmkqLBuUBDns2urDZqIrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
خیابانی و خداداد عزیزی دیشب نزدیک‌بود وسط برنامه زنده به همدیگه تجاوز کنن که برنامه رو وسطش قطع کردن
😂
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/99897" target="_blank">📅 09:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99896">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f0aac58e8.mp4?token=oxc_xAjz-9x2bS-izrp4af9Ldop84fXhf5UahpCucuAmL2CkMPj-eJwy5Tz4M6RLQmdz248-GEWhw4Q4DF2ISmpXySx1LwmEuMDxBjK7z-diHWTtBTaCfcBv_mDUM_nuPNc3_NedaM3rZ3lHZjtcTHgIXlE-KEp9zz8veJDPPELv5EbbuvQY_1MrBxpHPOlJiXqIGqoNUB9KVdZfhITp4eGRiHA_204gLJ5Sx8yIAd9SscfNIzIhrgjvKkYvJvG0qlgsp5skO3UMCRYSGkNj8pnOwkQezd88MB8QCipg2Zr5I_6isNkuJP_RfSzwgZvSZ0CVN47Kj_Dfb9tenzdOag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f0aac58e8.mp4?token=oxc_xAjz-9x2bS-izrp4af9Ldop84fXhf5UahpCucuAmL2CkMPj-eJwy5Tz4M6RLQmdz248-GEWhw4Q4DF2ISmpXySx1LwmEuMDxBjK7z-diHWTtBTaCfcBv_mDUM_nuPNc3_NedaM3rZ3lHZjtcTHgIXlE-KEp9zz8veJDPPELv5EbbuvQY_1MrBxpHPOlJiXqIGqoNUB9KVdZfhITp4eGRiHA_204gLJ5Sx8yIAd9SscfNIzIhrgjvKkYvJvG0qlgsp5skO3UMCRYSGkNj8pnOwkQezd88MB8QCipg2Zr5I_6isNkuJP_RfSzwgZvSZ0CVN47Kj_Dfb9tenzdOag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
خاطره هاشم بیک‌زاده از احمدی‌نژاد و روحانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/99896" target="_blank">📅 09:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99895">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a56d32af8.mp4?token=VmjM0CKCAfT0WDH-U2N3xNsA4r3vj41SoquBqasDQrg8H59ZEB1FYIG2ZD7dFVW-XKVNDpBFNKuU6Z_q4bQYS2znjAXJnMLT5FfCcFgqfHgZG28BUGX8vO0chZTyt271klfLqqLkLJLlIwVr03zH5zsECKOsesoKHFMmH9-ovA3MvnST2uhoGsHCqawZcpjF86TcaqhbuYX1zENXY3YNPT7HxstpGKChw4xReLQE5O-DEOdJvfj26KlcQmNOBT4LE6_ZEg_xQjtGigtFRVHZmriBPUMGULpt7-QECk9q4JoAS7_6dNDXYsQaCxuMAt72CB_t-nlRjrhEmAvJmECMiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a56d32af8.mp4?token=VmjM0CKCAfT0WDH-U2N3xNsA4r3vj41SoquBqasDQrg8H59ZEB1FYIG2ZD7dFVW-XKVNDpBFNKuU6Z_q4bQYS2znjAXJnMLT5FfCcFgqfHgZG28BUGX8vO0chZTyt271klfLqqLkLJLlIwVr03zH5zsECKOsesoKHFMmH9-ovA3MvnST2uhoGsHCqawZcpjF86TcaqhbuYX1zENXY3YNPT7HxstpGKChw4xReLQE5O-DEOdJvfj26KlcQmNOBT4LE6_ZEg_xQjtGigtFRVHZmriBPUMGULpt7-QECk9q4JoAS7_6dNDXYsQaCxuMAt72CB_t-nlRjrhEmAvJmECMiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
🎙
خاطره شنیدنی رضا جاودانی درباره شکیرا
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/99895" target="_blank">📅 09:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99894">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e6mbgUHB3gpTtpesTyy8QTbHGTIGwBCiRJAm5wiULw982qlPspymcm8Va_U1xXKFKi82KPHn8ivgP981-y8n9Fb19XRiy6gKg8JQQwFrECKuSw3L2wpZodjRsShdKk6YbVufqTLTPUPSobxJEtI8WVQ5sa9HKRcRWwNK0Bs_eJAqAsrCS8GFDnQrP_3Md5yv6S015eUshUNH7KC1nsWrLMx04ZYfHLWCb8hV5tCtY8GXl0TmIANTWVazhFiYAKK1DhsvV99zxqKAw1QiNUrcrpjDmuy4Y3nILeM6IvPuotJJ2QnasKGA_e8iUtnT5f_PdRGAKQSAg6Be9TVXcYQYbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
🇪🇸
ایوان‌بارتون داور اهل السالوادور بازی اسپانیا و فرانسه را قضاوت خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/99894" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99892">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sUJaMikxihlxCx25E7n-fN7IIvnJgmEkw9DYsRvrWZvkgM7NuX6hhuGH655H8G1kz_hNAx-ab_idCcoY6A3r9v-Qdms8w6mkFuzxDcqj_-L-B3byKruJtKthZqFD46kVs5MGR1cth74Ud55y8M5Hv_z_vTY1XGwBcuNqckxStegt-TXaPnLbJaFRPikX68dgB-9MDS8aMMbVepZKOGBomI-_A7ThpxIILvemU47OyfZGJTV8cbCZOyp9Sa8thoH3nRvQYhQXI-sYCdvFkLY53L_7CN0uWII2MvlmsvMbOTNrLtZ6Yhi8BxGsYC2oyfxqB5Jw3nnTGccDQonBfldHxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T_BGgmZ7MMoQLuUMqgD2Uu7RwlhIn15FH4FMkrXhSwadxBS94GgJpd1IU4caHEMEzrPn3xXq0HlMMRphXgBaIUasQZoDGfS0SpW4eXBT2eTefw9ni8n-syuEVLXSvnY3Pn6Vy7ylewebP2w3f2g-ETe405ttIa6DLwUepg5MEUexRKBjAVsC049wDPj_oi4BJNftSX9bJTyzOZ2DU2KrLij-mVRAT3zXozaedz2q9vx1ObTZvOQGs_YrmIe6oU5neO2QwLZzPPrcNyTS85sejNoP8fqwIaiq1o9-0WVS7G7DUcIJqStsr2soHIBgDUUGOPaIcRX4K-zdyOYkb7YQFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جورجینا در کنار رونالدو با کپشن “Daddy
💘
” که میگه کریس حسابی حالش خوبه، نگرانش نباشید و برید به بگاییای خودتون برسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/Futball180TV/99892" target="_blank">📅 05:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99891">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/os5qvIvu65_AmVvhPvRvt-niheqox6aY-c3hWwaWzlJy5TQWj8EhJ6W7cmLx3DMpQEMTrsZENaPwDFDKEawxMJa9RjRac3novg69T5j843W4AhVxun8289loaEcJ6EebqpHrfiYJvMkb0dvcbg8h4oH81Zk2-AL9_QKoz6_h1-7EoH7-QM9UJMDkPEmw9dwRknblJLDBlcyXZzQm8dExyZ1MCM90kmI6hfqN9ZFKro4ArFq1pArcHtH26l72TtKe4T29fFb6WIx3MsV8spXD0VLIZqISAq4J9jWBinrFmervVXwbwBjL45h3rgDu0gbZy83TtZ846b139vvm505SLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
#فوری
از بن‌جیکوبز: الاهلی عربستان در ساعات اخیر با ارائه پیشنهادی نجومی به مارسی و دستمزد فوق‌العاده به گرینوود خواستار عقد قرارداد با این بازیکن شده. مذاکرات گرینوود با فنرباغچه پیشرفت خیلی‌خوبی داشته و فقط دلارهای سعودی میتونه این انتقال رو منتفی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/99891" target="_blank">📅 02:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99890">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f230afe8.mp4?token=t5msF_I4J5M2FGf8QnD2PUw3HPtWssnD-H7JPn-6osoKhlCVHgatOW-sednwjx7VzAn9OsH87-npw6flG8T0D7dOPep5rBL5GB6-IWaN8KlPsPW4gcE4r7wN-VLOtCH5w78P04bH53f4hKSrHZhVAe0qmfdFcKtEBKXNFuS2Uqg1uZA4GhZwE9fMPTw39t65EWAU_jmqxaAsdNNbErw_iU6fEDTQkO8R6ABAO9cGx20rx7y2-EmBKv24N87J0c4rZB8iomb4A_a1ubZVeyMxNFFVK5djNrkirB8bXhbZG3wGIqB8IxmheZLg3AvIu8HTaDdZbh7QECovzfSTi2HBwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f230afe8.mp4?token=t5msF_I4J5M2FGf8QnD2PUw3HPtWssnD-H7JPn-6osoKhlCVHgatOW-sednwjx7VzAn9OsH87-npw6flG8T0D7dOPep5rBL5GB6-IWaN8KlPsPW4gcE4r7wN-VLOtCH5w78P04bH53f4hKSrHZhVAe0qmfdFcKtEBKXNFuS2Uqg1uZA4GhZwE9fMPTw39t65EWAU_jmqxaAsdNNbErw_iU6fEDTQkO8R6ABAO9cGx20rx7y2-EmBKv24N87J0c4rZB8iomb4A_a1ubZVeyMxNFFVK5djNrkirB8bXhbZG3wGIqB8IxmheZLg3AvIu8HTaDdZbh7QECovzfSTi2HBwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
🔵
دختر علیرضا بیرانوند: بابام استقلالیه و دوس داره بره استقلال
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/Futball180TV/99890" target="_blank">📅 01:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99889">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🇪🇸
🎙
خوان لاپورتا: ما تو بارسلونا برای هرکسی دولاپهنا نمیشیم. یه پیشنهادی برای اتلتیکو ارسال شده و هیچگونه تغییری قرار نیست اتفاق بیفته. بزودی می‌بینید که‌پرونده آلوارز به کجا میرسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/Futball180TV/99889" target="_blank">📅 01:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99888">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_-G0BfxvRAci5Kl2uwIQExz3yIYNuQ7EahPl02IGE4TdweSUfimYV6d8viay3aQbs9jKxiv06u7B4CzlDGGGNmo8ffTqTIk_mhNq5AxsXZtx7jfhiPhnxoySBq_wiGzRJFJc3trgb2oNNyvWhWhTvAlBLBFyIaOQ15TpsNEpTrWARLTEad6j4z1wlFGFTZhlGLsdd6PQrpsMHQizkGKKjg4XEQ-1e-hpxP9PVsP6shORzgSoNhR8lZsJS9Y6S7rcMNbfGyMf0K4IHOD1rs9tVs_x8LkrJ18DceW-LcyTDoBOqiRLRaY7LXW_msIxU-51bwRupa-lpSofhaS2UAARQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوووووری؛ اسپورت: باشگاه بارسلونا حداکثر مبلغ ۱۳۰ میلیون یورو برای جذب آلوارز به باشگاه اتلتیکومادرید پیشنهاد خواهد داد و رقم بیشتری پیشنهاد نمی‌دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/Futball180TV/99888" target="_blank">📅 01:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99887">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtcTSmohok9kr1X74apa2HxM1ap2NSVnqQ6ZvR5jDz1HTtusiGIUyO7zNIycdzX6IEppS7ZAebQXbCyqeUKQCJye3DGs0QhvvR57XCysie63oejmCD8Q6pvvMZ7gZvUyM0OKoyEqpqVDhENyuCVZbuom_7cevpSAr-5cBCL-wXoE7uhljs2rGcrHjcEA5Tue0ZJ8IX4mjyDuurMrkzl3nV4TpohK5EpnWZksIAwS6Sd1JfPuqDynkrA_R2BR96h3b0oP7YQtxZe40wodm3YjFSkRSxDMgHTDYY3fvtr9YFWR6gT7t6_sPTNNq1tOL1EBjcjLnIqKHjBCCcwgthXalw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
💪
‏ سوخت‌رسان‌های متعدد در خلیج‌فارس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/99887" target="_blank">📅 01:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99886">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvARmh-IuTKeYBMdJMgmzK-5st0YAkwCWVr-Uk58YtmeF8NlyTLGDdmoSC3w_T6W6P8s9rIB7bXcVYGiFq354pgPYgMj13zQSaK39CcxXTylwKjfljTh3MCqEosU5uoGRdgJyH2Xs4fTd-M36djGqKxTJlgV9-1YG-6sDYObzMJ80iA1m9qHVzZcMuj4CWTAWvNL750wCnj-k4KdpMbJFHNgGnU1OGEZ9bDipoie-ETKVbusWQWF7lt5PyOXRVtOxkCbQMkPjQiFcyujs8oZKRYZqqUslMIDuk9_ukUfdPaiQb3a0Vz3N1RdPKU5tPNUFbbvvP8cfp1dQ-L-8YeVlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوری
از رومانو: رئال‌مادرید درحال مذاکره برای تمدید قرارداد یک بازیکن بسیار مهم و حیاتی است که این بازیکن وینیسیوس و شوامنی نیستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/99886" target="_blank">📅 01:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99885">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i269wuzj4lYboKmm2-XvpA5dGT_aEBeBrtDspgMqVAQD3Nt4C2k3VnrMtyCcpFsrQFyoVfzXjTbSHmF95A3qk4xGK8nusyAxP2yt4WJ09n1TJERqbX2ZK08R3VvcF1nJPSW2mrGzHOlM781NWPfcQLBU64LCW07gjwnY1--C8m2jHzVtqprPXbEtA8-bECg3_mx7asaHjS_q1m8l-xTNcVAvRNlFRsFiZd5HpXOvZpSqnFu558rALEYSvATn6drdVIySQrlUufGrQWAeBvshYbJvtub52AVpadiGf33-KnRvISGY2CjmTK8SdFUD0fySHFw0tE6pnSQpudp50__ldw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لامین‌یامال با توپ ویژه فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/99885" target="_blank">📅 01:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99884">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXJR2DrpdyCKz8oc4aT2LhPRfVuyrd8hGMOH5QN--YErjJAxpyP5GSvvE2YtiPQmfDE8r7URVwB2fOEih_54Kc0-CBNdCgfnS-Z4_4py5STiUPetURZxoR3_9t-IL6_wHoHWr8tPKbfYjW4FGs-dD24UHb0eOKWniCcpuK9CdXWB91ptQ82Ek14MhY8W6-35HE-xcek6GWYZhY07W-Ty7q0Ro8J2YghoWSkxxUAhBnx4zlEliB6ycbAWg8kf4yVsxcod_dm_TdyINIp4y7wpTcmhsp4Jcb_hRG_OUw07zRNZF58JAR1ISW1ozr5yANpTKL930YESkhpCQ2U8MsjHGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
سنتکام-حمله به جنوب ایران آغاز شد
ساعت ۵ بعد از ظهر امروز به وقت شرق آمریکا، نیروهای فرماندهی مرکزی ایالات متحده حملات بیشتری را علیه ایران آغاز کردند تا به تضعیف توانایی آنها در حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه هرمز عبور می‌کنند، ادامه دهند. فرمانده کل قوا دستور این حملات را برای پاسخگو کردن نیروهای ایرانی صادر کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/99884" target="_blank">📅 00:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99883">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
انفجارهای متعدد در سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/99883" target="_blank">📅 00:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99882">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
چندیدن انفجار‌های شدید و پیاپی در مناطقی از بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/Futball180TV/99882" target="_blank">📅 00:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99881">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
#فوووووری؛ شنیده شدن صدای انفجار در مناطقی از استان هرمزگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/99881" target="_blank">📅 00:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99880">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XPTVLirm25S2DhHKDUU_jO01koYkA8dUY9b-fCBMqi0mRpzeCDTA_pnEzOwL0U5Op2bIhCyk8KxzA4WQlYrXpRXWkltyEn6rzyQbn46A1CB2VU4A7cx_tMeGLmptVg3vIq7p0qDHgvLas9qZ0FP-dsKCAZ1AaIoN195EyVJpwcvKt7ctjNTwgi_9FPuaeEmEdKfUcqdbPUi7ocJBazrxpPR-_tjwt2sxPeP50z4tPKyGq5Tyu7NER4sXmm4R1-h_LC2IRyLiF2p1z-0i6eyhn4fbzcnwpCJu9qhdquGVHKXqHb73-FAY-P2zjtqWxKBiOXvNgC0nMh5t0Q6Vw717SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
پرواز سه سوخت‌رسان از فرودگاه بن‌گوریون اسرائیل به سمت(احتمالا) خلیج‌فارسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/99880" target="_blank">📅 00:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99879">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
#فوووووری
؛ شنیده شدن صدای انفجار در مناطقی از استان هرمزگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/99879" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99878">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab9b193566.mp4?token=OwE_mE5RhDRyREzDKtMRJlSDq6kgvE_chI-Bb7SMx6EaYPGd-pPCBWjMpYeDp2FJQpnHYQqLm7l6gHznamEB06E07O-zYvLupCpjSbXfFojZKTp6FwVsF-hLBsItPgm1Hb3VpxcYVVCmL3g92xhSIFXEhoTRGFgOQZ_zC3Uky-AthLc0mKld5jA3Vv0ylcSmgvqWlKSyzg1nM9E_0IoRQX-p4aRGKFtL8TiuQWUYHfbz04cvUT9vKKrbEZwGVLegkxZoy5rGbwafjAaUMCfqc2cvhjJUGLca3uajlzomIe4vWb18HpLT0KmS9vJ2ZEAlVIV8G2XMHt0ZUucRDaDRwJVAGhUlvSOTvOxxu1vIBUWN1Ab7anxlfeEtzChtDnxL7sNKnYHszMay0_GcU8QWHdguNmatBaSS_CZCs4ybup44N3fRP4vxWAs3P8oZE0UBh2VDavhNQqUo4ir2OvnSfJVxyK-qnXNia95KcVSrOqvEkKr3nzfL5Qem4cHjmjCF8WTdq_V7Gxs2mkglSiRKFar3MEP4o9sRkOd-EZ3M5ZoenuDIV65vQtL-e5xiFVy4uINwJMfbsNU_goI1FfMBveQdXoVQ32B-zafzM5REdtryyIhL1_ZFfqbRErBc98jo1GDusRaU77e_vHFx78UYk7DVEOPwcFXithkN1yUxxh4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab9b193566.mp4?token=OwE_mE5RhDRyREzDKtMRJlSDq6kgvE_chI-Bb7SMx6EaYPGd-pPCBWjMpYeDp2FJQpnHYQqLm7l6gHznamEB06E07O-zYvLupCpjSbXfFojZKTp6FwVsF-hLBsItPgm1Hb3VpxcYVVCmL3g92xhSIFXEhoTRGFgOQZ_zC3Uky-AthLc0mKld5jA3Vv0ylcSmgvqWlKSyzg1nM9E_0IoRQX-p4aRGKFtL8TiuQWUYHfbz04cvUT9vKKrbEZwGVLegkxZoy5rGbwafjAaUMCfqc2cvhjJUGLca3uajlzomIe4vWb18HpLT0KmS9vJ2ZEAlVIV8G2XMHt0ZUucRDaDRwJVAGhUlvSOTvOxxu1vIBUWN1Ab7anxlfeEtzChtDnxL7sNKnYHszMay0_GcU8QWHdguNmatBaSS_CZCs4ybup44N3fRP4vxWAs3P8oZE0UBh2VDavhNQqUo4ir2OvnSfJVxyK-qnXNia95KcVSrOqvEkKr3nzfL5Qem4cHjmjCF8WTdq_V7Gxs2mkglSiRKFar3MEP4o9sRkOd-EZ3M5ZoenuDIV65vQtL-e5xiFVy4uINwJMfbsNU_goI1FfMBveQdXoVQ32B-zafzM5REdtryyIhL1_ZFfqbRErBc98jo1GDusRaU77e_vHFx78UYk7DVEOPwcFXithkN1yUxxh4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
بیرانوند: این نیوزیلند بود که ما را دست کم گرفت و می‌گفت کشور جنگ‌زده هستیم تا بتواند ما را راحت ببرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/99878" target="_blank">📅 00:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99877">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6782dde8a.mp4?token=NpIZMp2ueYWjvK1dLSeoPhHPGyOjXpN-BSk7m0osXzq3fCQ42Sf8Iy3Y8qD5QUyyxR093rUDb9BPLoYJ7Ci0RXRVLxAFhoPdCmhVsT38RuFy-SBA5g_d4AUwNK3tk7yMwCgMNg3Jn7MxpEACfAYeQbw1vL1I1Qt9LpqzuyMRNY47zzbs4p03LMzIPOY2B-C0Q8hIlXPkxCLh94N3blW99MtRFLZG6vM_IZJeOIxADverITGvzUUitzid9j-y7Jy-x80oUYFO3DQfEfu1dpM9LeoNTGGdSP3L4sCGx1AkOp-BO_lHx55Pi_1MdrSYZmWcq6r3WuL-r4HVtF6pVk0SvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6782dde8a.mp4?token=NpIZMp2ueYWjvK1dLSeoPhHPGyOjXpN-BSk7m0osXzq3fCQ42Sf8Iy3Y8qD5QUyyxR093rUDb9BPLoYJ7Ci0RXRVLxAFhoPdCmhVsT38RuFy-SBA5g_d4AUwNK3tk7yMwCgMNg3Jn7MxpEACfAYeQbw1vL1I1Qt9LpqzuyMRNY47zzbs4p03LMzIPOY2B-C0Q8hIlXPkxCLh94N3blW99MtRFLZG6vM_IZJeOIxADverITGvzUUitzid9j-y7Jy-x80oUYFO3DQfEfu1dpM9LeoNTGGdSP3L4sCGx1AkOp-BO_lHx55Pi_1MdrSYZmWcq6r3WuL-r4HVtF6pVk0SvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
😆
بیرانوند: آخرین بازی دوستانه ما پیش از دیدار با نیوزیلند، با کارمندان کمپ تیخوانا بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/99877" target="_blank">📅 00:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99876">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b76e61623.mp4?token=nx4Bc_GjxRaHSu6QWdwQW2PKVayo7Lvb_CZxVChWoV9r6Sx6HxJt5d-1inBNnYXBV5J3Pwocp7p7m3Amt1_dO_uPhWgLhCdTCc4YR2qZXjril_A96wppDgnKbe7_ynJzr7fkjNmQuqH-PZy8Ao2KWmV-Ddep_KrSRZJNetwnijlnq-hPlOnOCNyFhFI92AlqH3fgQE3Fz7gY84u06ojL9kEB3zlnVQfkE97LJsIMO0h73UJkeOve-be8CJw6fi2IAX5U7cg9pdy5IiczumAvUJzGrNA2XoUtv6XHTKxRTNRLP4rB0CcYR6lYmtzbNPit3olh6dNEVxWMNbxRs2ZNYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b76e61623.mp4?token=nx4Bc_GjxRaHSu6QWdwQW2PKVayo7Lvb_CZxVChWoV9r6Sx6HxJt5d-1inBNnYXBV5J3Pwocp7p7m3Amt1_dO_uPhWgLhCdTCc4YR2qZXjril_A96wppDgnKbe7_ynJzr7fkjNmQuqH-PZy8Ao2KWmV-Ddep_KrSRZJNetwnijlnq-hPlOnOCNyFhFI92AlqH3fgQE3Fz7gY84u06ojL9kEB3zlnVQfkE97LJsIMO0h73UJkeOve-be8CJw6fi2IAX5U7cg9pdy5IiczumAvUJzGrNA2XoUtv6XHTKxRTNRLP4rB0CcYR6lYmtzbNPit3olh6dNEVxWMNbxRs2ZNYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجری شبکه سه خطاب به بیرانوند و اعضای تیم‌منتخب فوتبال‌ایران:
از ته قلبم بهتون خسته نباشید میگم
در ادامه رو به دوربین:
به زحمت این بچه ها باید احترام بگذاریم
😐
😐
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/99876" target="_blank">📅 00:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99875">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7990a07676.mp4?token=M454iQvjSKPDclt_68MnuqAQxXWrE6i4yjZpBlJ-qDl_xDwZoyswQXSTvtlXKonY2CSEfAAtuDjRx3wIV01udMKOeJMMb9iK-yIS3UdCFKSRqP2ICvnBiODpfGB4Sa9rmnXPc3uEYcE1bra1K4SG5q5lmnk0x5D00oX6V_kvxTo7JLAbnjkfsLQEtUgNSoNhymRztdb53R1ogcPbQ5cD69K3XU3RGFBf57Es62UDu8dQxVRRtrUgJbch7DWeZ52ruV_8KM2QVz8Zupwnhp_zfSPBa6IG6P8dFem8fYScRCtSkmeaZ5CmDBhBm6tY7KOXMzGs0yBWOBOBGlB3z0jgtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7990a07676.mp4?token=M454iQvjSKPDclt_68MnuqAQxXWrE6i4yjZpBlJ-qDl_xDwZoyswQXSTvtlXKonY2CSEfAAtuDjRx3wIV01udMKOeJMMb9iK-yIS3UdCFKSRqP2ICvnBiODpfGB4Sa9rmnXPc3uEYcE1bra1K4SG5q5lmnk0x5D00oX6V_kvxTo7JLAbnjkfsLQEtUgNSoNhymRztdb53R1ogcPbQ5cD69K3XU3RGFBf57Es62UDu8dQxVRRtrUgJbch7DWeZ52ruV_8KM2QVz8Zupwnhp_zfSPBa6IG6P8dFem8fYScRCtSkmeaZ5CmDBhBm6tY7KOXMzGs0yBWOBOBGlB3z0jgtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
علیرضا بیرانوند: هرکسی جای قلعه نویی بود و با این نتایج برمی‌گشت، مجسه او را می ساختیم. خیلی از کارشناسان خارجی گفتند که باید مجسه بازیکنان ایرانی را بسازید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/99875" target="_blank">📅 00:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99874">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMYOjlEaJAcob5FCCz0m4DRL3hs0DRLbjsqFncVOkmQjwsnaZGlDol7Z6UIu7EwsMc47-wZFv7DFB53AzoW63i6qJcsgtsHHZNXNLiDNfiC2HTd4uTwdoMb-dqlHfcnx5AcLfFYHNUS-vwZZSTrYa2ASVA-RX3ALoKsqa93jpwg4tx2iOWkjTWo_LTudAMBeiqKDPlWubDGo9NlaHlgIFvhF91n-uKQgy8utv112xjJUa384aTNAAvOwRQjTSUQzeV_Y81lyKr2IPdyVZdBASkcvIJGsnXHlApW8RqzysY2_vZAiSEm2zTcyx3T4BQ-yGtNdAsWITKH3JHmtaUFSgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوووووری
از موندو: بارسلونا در صورت جدایی فران‌تورس و عدم موفقیت در جذب خولیان آلوارز به سراغ پدرو نتو ستاره چلسی میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/99874" target="_blank">📅 00:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99873">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-AFS8TGAySyoSRxjrCniG8eDWRR1EdB318kP0YxDezK98f0i7634XPE882LNY0Yw4r5YmPg-MFWzp98ysR56ZiPdTDNmEwhURgCdj64nJseMmK6vbWUV69DgS9zWCDBHCHG3vaUaziTskedRg1sJnGR18prOKtWdkHDwKR_OVnoOewmnaQtbGOo03UJ4vPMfr9vXYGHEP49Kl1E2GPlhYZTyatD9qMp3t8JT1-BO2aiyS5DiGEKCf5R4R1_MaTNhLqmOLNtKvX42WSTuiCobhaZiw8_ARvxS05YAwZmyRx7HPPPOhGHx11Nwgx5170PDbAc7jioBTk7tgUBrEKQAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جود بلینگهام با توپ ویژه فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/99873" target="_blank">📅 00:18 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
