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
<img src="https://cdn1.telesco.pe/file/YBO2SYkfAjnEnKNuR3WnJHvaFr9GraTp9k1835hALMt44EA0h9HOrSr7Az_DJGUfuz_qzWw2LHFHmZv9bGhfsR7EBLpw4Wji3PNK1xH1-r3QsTflsb08bieYaO_UVzsihWcbVVv68YmEF4OBt2_28qJ-ShUOc_J3AXlNr0DKfAihEx-gH6kS6nmnqi_w1DGmspMjBKiaoNv4_Xy6BleCKfZFDIXGMBSdIItVoPiI31fC6pXDs32Jsb_QdzIiI7z5KuJHxEqgRhvaCh3iiXvH5TEOQI9iy1Enc_FdNSB-LGqPkFsDDeGX-jTyCQx5CJQNXLfeWxlxafQzGVgRoW9SnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.36M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 11:09:31</div>
<hr>

<div class="tg-post" id="msg-76951">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ea07cb43fd.mp4?token=sxwa9WusqHnpmkLfnTQz2fCbGG5YnX80dqmZie5dBZG4lVj6ZaXxJefI9_MTz27ooqlh3Vhs-PculWLAdC9orDknl9ZBhWsn9HkpUQCzamm_zncuohLFCH00IpC_FpI-0HlZ0xLqahNr6TwrO8Y8FkTXAFtbsJPIaMjDTQv7j7EI2CduGrlCQdheeNemBiQS5o-K2PLmvWRIv2AIOP7j-yZ9WwiuOsVZPuPWlm04OHFCx5ImVPf2hYRielh4WLQBoploQLT2onCRIXYT1esFPUV9u22hqMfz-U03UOYYCC6sd-NC9kjI6kTULCEiQxQ0B8UVXaYQTRV0heUpiHGM3w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ea07cb43fd.mp4?token=sxwa9WusqHnpmkLfnTQz2fCbGG5YnX80dqmZie5dBZG4lVj6ZaXxJefI9_MTz27ooqlh3Vhs-PculWLAdC9orDknl9ZBhWsn9HkpUQCzamm_zncuohLFCH00IpC_FpI-0HlZ0xLqahNr6TwrO8Y8FkTXAFtbsJPIaMjDTQv7j7EI2CduGrlCQdheeNemBiQS5o-K2PLmvWRIv2AIOP7j-yZ9WwiuOsVZPuPWlm04OHFCx5ImVPf2hYRielh4WLQBoploQLT2onCRIXYT1esFPUV9u22hqMfz-U03UOYYCC6sd-NC9kjI6kTULCEiQxQ0B8UVXaYQTRV0heUpiHGM3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام:‌ حدود ۱۴۰ هدف نظامی ایران را مورد اصابت قرار دادیم
ترجمه ماشین:
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) روز ۱۱ ژوئیه سومین دور حملات این هفته علیه ایران را به پایان رساند تا نیروهای ایرانی را بابت حمله به یک کشتی تجاری دیگر در تنگه هرمز پاسخ‌گو کند.
نیروهای آمریکایی با استفاده از مهمات نقطه‌زن شلیک‌شده از جنگنده‌های مستقر در خشکی و دریا، پهپادها و شناورهای نیروی دریایی، حدود ۱۴۰ هدف نظامی ایران را مورد اصابت قرار دادند. این اهداف شامل سایت‌های موشکی و پهپادی ایران، توانمندی‌های دریایی، تأسیسات ذخیره مهمات، شبکه‌های ارتباطی و مراکز پایش ساحلی بود.
سنتکام طی سه شب حملات این هفته، به دستور فرمانده کل قوا بیش از ۳۰۰ هدف را مورد اصابت قرار داده است تا توانایی ایران برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه عبور می‌کنند، تضعیف شود. عبور کشتی‌های تجاری از این کریدور حیاتی دریایی بین‌المللی همچنان ادامه دارد.
از اوایل ماه مه تاکنون، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۴۰۰ میلیون بشکه نفت خام از تنگه هرمز کمک کرده‌اند.
CENTCOM
منابع حکومتی:
دومین شناور متخلف در تنگه هرمز مورد اصابت قرارگرفت/ مرکز تعمیرات و نگهداری جنگنده‌ها و مرکز فرماندهی و کنترل  ین پایگاه در هم کوبیده شد
روابط عمومی سپاه پاسداران انقلاب اسلامی اعلام کرد:
بسم الله قاصم الجبارین
فَمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُواْ عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ
🔹
در پاسخ به ادامه تجاوزات ارتش کودک‌کش آمریکا به پایگاه‌های ساحلی نیروهای مسلح جمهوری اسلامی ایران، علاوه بر اصابت و متوقف‌سازی دومین شناور متخلف در تنگه هرمز، پایگاه هوایی راهبردی آمریکا در العدید قطر در مرحله دوم عملیات مقابله به مثل هدف موشک‌های بالستیک قرار گرفت و مرکز تعمیرات و نگهداری جنگنده‌های و مرکز فرماندهی این پایگاه در هم کوبیده شد.
🔹
دشمن امریکایی - صهیونی بداند، استمرار تجاوزات او پاسخ‌های کوبنده‌تر را در بر خواهد داشت.
بجنگ تا بجنگیم.
روابط عمومی سپاه پاسداران انقلاب اسلامی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/76951" target="_blank">📅 07:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76949">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dkuvIlHfOqgld0B-fBtdf4aL_rp-NXgYGr5XhigJkMNO4xGY0xP2X3Q-94VGiwJl5EBsMxV1Cz_h1Fct-FxInjgD_uNt-2ZUnjp-cmdcPJAM9RbBpOFN_TSDyApd-v_keZJv-Phm9TsOqmTuGgKEGLpAK-F14fhbRcmErCWO0BPStW5bUIZVhRbOnvGfXGqXjCGAiYlj7Q122zx0UdVusYoKHVbFrTl9xyu7fszgC8tX0RN0UfbuPls0ElTvyt-u-8K2CMO2m0kTld1CjDLPnuOlppYpCApfyBK51M2oMTeydrWEEnpD_AhCSx251SvQKysuNXGlvJFZO4ap2PIyfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از شاهدان عینی، خبر از شنیده شدن صدای انفجار در دوحه، پایتخت قطر خبر داد.
پیش از این، وزارت کشور امارات متحده عربی با انتشار هشداری فوری، صبح شنبه، اعلام کرد که سیستم‌های پدافند هوایی این کشور در حال حاضر در حال مقابله با یک «تهدید موشکی» هستند.
همزمان وزارت کشور بحرین نیز اعلام کرد که آژیرهای خطر در این کشور، صبح یکشنبه، به صدا درآمده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76949" target="_blank">📅 06:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76947">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cb22334a3e.mov?token=eBtiUYtkynX3stlGMWCMon1YLB-QHOmzf04LJdJMXi8rB7jGhAEHnPt75uFmDtSedB9qAVk_bRtu5W6cMDhquvOiI_rW7EimqM70x35nutUt2ETY403cyC5ZY4RotL2zcXTBMY2uaVSDUQKV0ErqgOzXeNJ62JsP_FURik1N8FZVAKbTCHjAcZH9EtGK9dI6-i7PncNonajK17aakT61w9trlXCmyxJsm-6HdGneDo4w5oWIjx4c2fvv8FaHLz6CWRFSKD0BW9IsBi8vloH_M6SH0QGDRkT6ebT8jWJoPqPtHv7QPzT9IPU5UxhGy4q8YBeNqvXlfcvLFeurhyINxw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cb22334a3e.mov?token=eBtiUYtkynX3stlGMWCMon1YLB-QHOmzf04LJdJMXi8rB7jGhAEHnPt75uFmDtSedB9qAVk_bRtu5W6cMDhquvOiI_rW7EimqM70x35nutUt2ETY403cyC5ZY4RotL2zcXTBMY2uaVSDUQKV0ErqgOzXeNJ62JsP_FURik1N8FZVAKbTCHjAcZH9EtGK9dI6-i7PncNonajK17aakT61w9trlXCmyxJsm-6HdGneDo4w5oWIjx4c2fvv8FaHLz6CWRFSKD0BW9IsBi8vloH_M6SH0QGDRkT6ebT8jWJoPqPtHv7QPzT9IPU5UxhGy4q8YBeNqvXlfcvLFeurhyINxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی (به همراه تصاویر مختلفی از رد دو موشک):
همین الان از خمین دوتا موشک شلیک شد
درود وحید جان همین الان از خمین دو تا موشک شلیک شد
سلام،،ساعت ۵ نی دوتا موشک از الیگودرز شلیک شد
زنجان
۲۱ تیر ۱۴۰۵ ساعت ۵:۳۲
صدای بلند و ممتدی هم اومد برای چند ثانیه
وحید این دفعه هم از سمت خمین و الیگودرز شلیک کردن صداش زیاد بود ولی ۲ تا رد موشک بیشتر نمیبینم.
شلیک موشک از خمین
درود وحید جان از حدود زنجان موشک بلند شد دوتا
🔄
شهرستان داراب استان فارس ساعت ۶ شلیک ۲ موشک
یه موشک از داراب فارس بلند شد رفت ساعت 6:05 دقیقه
همزمان:
آژیر در بحرین
sirens in bahrain
5 دقیقه پیش قطر صدای پدافند اومد و آلارم روی گوشیا
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76947" target="_blank">📅 05:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76946">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PI5s6oOyA8l0ILG2iltMK5ZwMx3PxxAzqJxLW4yY6OYFRsGVb6O77JJ1ztlZ_Gs-CbGSMyVgVk3njkSTRh6xtFKwxRy-gI5BDJWihdD-lWOY7bKKPz3Y_rjJPFUq-W8knNTAOE3aFPTcjWQKhQOthfk4ooG-3LYU1gOx_sOPAEHQsrF7dF0YjL7Go8sRN-GfyGayURq8JoHIFliIwC9-GKKIdn8Og2FfavcRV_ipm8p-D6VdlMUvft08237glPeFoOXduR257N7T_2XCmHumhYwa3NKMgOcQ7q7m9FG4Fd3o04vBXCgB6WCWA1KR7S9YpXc_-vCznj3qelU3pR-grQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون امنیتی استانداری خوزستان گفته است که شهرستان‌های هندیجان، ماهشهر و آبادان هدف پرتابه‌هایی قرار گرفته‌اند.
هنوز جزئیاتی درباره محل دقیق اصابت، خسارات و تلفات احتمالی منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/76946" target="_blank">📅 05:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76945">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BcgpQp86re-oYKkHy8FFE_HK09PJjrWYx0wUQb43H2R_bo4gb_4EJR3klA8DaqdHjXy5yjh7Iy7L0f7TUQ5zRk1oliPluWs9OF-3O4gKnEI8U9Fa0MuA3p4h9iFITAQ5KI-7G3xnY3k5FGMC1V4FVs9MM-b4E2O3RpI7tc2XlE837J2bYkiPjUb2OTbyG7KQ3774g6_THHi5cIKwND-xDG4j0u0rsmjDqLv5bOZM6E6ZGksho637USPMTdImLydKuhzID25ogwVtALBcmfltosFXslmXOLRuwNY1IveG0MNNxtvWLe64SPwckhaKXhm7TWtvqcohQQKJmbLhWOxlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر و پیام‌های دریافتی تایید نشده:
سلام باز بوشهرو زدن ۳:۴۶
سلام وحید جان بوشهر سمت سرتل رادار زدن
بوشهر همین الان 3:48 دقیقه دو بار لرزید
سلام وحید جان ۳:۴۷ دقیقه بوشهر سه تا انفجار شدید شنیدیم
اقای وحید ساعت ۳ وربع صدای انفجار شدید اومد عسلویه از خواب پریدم
صدای دوتا انفجار  الان اومد  پایگاه هوایی بوشهر
۵ تا زد سایت موشکی چغادک-بوشهر،۰۳:۴۵
سلام وحید جان
ساعت 03:47
بوشهر سه چاربار صدای انفجار اومد
سلام وحید جان الان 3:45 دقیقه بهمنی بوشهر صدا اومد دو سه تا که خونه لرزید
🔄
جاسک
وحید ۳:۵۰ جاسک رو زد ۳ بار
سلام وحید جان همین الان دو انفجار وحشتناک در جاسک
منطقه نیرو دریایی جاسک
3:50 صدای جنگنده و چندین انفجار از بندر جاسک
سلام وحید صدای چند انفجار شدید در بندر جاسک
🔄
جاسک
خدایا بازم داره میزنه
دوتا دقیقا همون نقطه قبلی زد
ساعت ۵ جاسک
۲ انفجار دیگه جاسک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76945" target="_blank">📅 03:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76944">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VUS1DVErAuWWFJWPWkNbr1FLQqzDFIfJzJ5V6zy19yc1WZMq_6Rbbox4WuUIv5gCq9r_ryvd4PsFzpF7wTRF4WyTc6RoO5k_nDStB9i9Qh67k-_HMCjsXBAweIIu8ismx_sQNSzt0hqfZhnqrPvINAYUMr1JP95VxyTXbNoArUPgBkHgBcmtN9ilvn37Z9Q36Xr-iSycsWqCfCaOyEChnXaTz1nOKeRvBFcXyYTbr4xIuxIzljQtQM7yiGYWLClI5IPkXVeFEWoxiCSjFmxHiRJ1iFAVhTcxoE0vnfJtTgfqFAE2Lug2TtlhnKr4uWl-vOxzlmYBEg1623A167LgNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا:
"ایران انتخاب بدی کرد. حالا تاوانش را می‌دهد."
PeteHegseth
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76944" target="_blank">📅 03:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76943">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پیام‌‌های دریافتی:
دوتا سنگین زد کنارک همین الان  ۳:۱۸
چابهار الان دو دفعه صدای انفجار اومد
سلام وحید جان چابهار همین الان دو تا انفجار مهیب
ساعت ۳:۱۸ دقیقه دو انفجار با صدای بلند در کنارک
همین الان ساعت 3:30 دو انفجار شدید در جابهار و یکی هم صداش خیلی دور بود شاید اطراف فرودگاه کنارک. ولی دو انفجار چابهار واقعا شدید بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/76943" target="_blank">📅 03:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76942">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سنتکام: سومین دور حملات این هفته علیه ایران را آغاز کردیم
ترجمه ماشین:
امروز ساعت ۷:۱۵ عصر به وقت شرق آمریکا، [۲:۱۵ بامداد شنبه تهران] نیروهای فرماندهی مرکزی ایالات متحده پس از آنکه نیروهای سپاه پاسداران انقلاب اسلامی به‌طور آشکار به کشتی کانتینری «M/V GFS Galaxy» با پرچم قبرس در حال عبور از تنگه هرمز حمله کردند، سومین دور حملات این هفته علیه ایران را آغاز کردند.
یکی از اعضای غیرنظامی خدمه مفقود شده و کشتی به‌دلیل آتش‌سوزی در داخل و وارد آمدن خسارت قابل‌توجه به موتورخانه، قادر به ادامه سفر نیست.
پس از آنکه ایران به‌دلیل حملات پیشین به کشتی‌های تجاری پاسخگو شناخته شد، بار دیگر فرصتی به این کشور داده شد تا پایبندی خود به تفاهم‌نامه را نشان دهد، اما بار دیگر ناکام ماند.
در پاسخ، ایالات متحده با ادامه تضعیف توانایی ایران برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه عبور می‌کنند، هزینه سنگینی به این کشور تحمیل می‌کند. این حملات به دستور فرمانده کل قوا انجام می‌شوند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76942" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76941">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aUclG4Y-f5rh6pAXcLxeY-XnG3BdRy0QhOF_cx5-ZChQd6Js9RFy8-5Ob273r0yCQpweuTkCOmDcDoWcbApbQxhd1j2eR2ctQd0u1X31Z3c3MdqqEkV1zc091mymKRHYs1GeygcYSY4cK_cqSQV7AcQ4CnkM2zjvb5W9v6VLQdSgLd5xfESFeY0Ctb9nzcuiC3feugv6roPYpi6BEJDJY4mTWWitR3EWp0XdyCOKKelPRsFMSAuNSQah9MIxyl82IrYUo24d00lIFOjD6-3IJjW_Nupac0kNHDP91CN_2SAqHB1204vNGJHmDMwnZo-lQTQQXouMoG7Mc_ZmH20m2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
‌
بوشهر صدای چند انفجار لرزش زمین احساس شد زیرپام
صدای دو تا انفجار بندر دیر ساعت ۲:۴۶
۲۱ تیر
سلام
ساعت ۲:۴۰ شنيده شدن چهار تا پنج انفجار در کنگان و حوالی آن
وحیدجان
الان حدود دو و چهل و پنج دقیقه صدای چهار پنج انفجار بزرگ توی بوشهر
شبشه های خونه لرزید
وحیدجان سمت نیروگاهه
من تنگک هستم الان دود و نور قرمز از اون سمت می بینم
سلام اقا وحید ساعت ۲:۴۵ بندر کنگان چهارتا صدای انفجار اومد
سلام ساعت ۲ و ۵۰ دقیقه بوشهر صدای چندین انفجار
۲:۵۰ بوشهر صدا انفجار
صدای چند انفجار اومد در بندرکنگان
سلام.ساعت ۲/۴۵ دقیقه شهرستان دیر استان بوشهر.صدای دو انفجار مهیب با فاصله یک دقیقه از هم شنیده شد.موجش شدید بود
سلام وحید
بندر دیر رو زدن ساعت ۲:۴۶
تو جنک هم ۱۰ ۱۲ باری زد یا بیشتر یادم نیست الان
اسکله نیرو دریایی زدن
🔄
همین الان ستا انفجار دیگهههههه.
بندر دیر.
وحید جان الان ساعت ۲:۵۶ باز دوتا بمب دیگه بندر دیر رو زدن
۲:۵۵ بازم زدن بندر دیر رو
دو بار دیگه ۲:۵۶ زدن
کنگان همین الان دوتا صدای بزرگ انفجار اومد۲:۵۶
کنگان رو دوباره زدن
🔄
تایید نشده:
صدای انفجار شدید بندرعباس
همین الان قشم صدای یه انفجار مهیب اومد
دقیقا ساعت ۳
ساعت ۳:۱ بندرعباس صدای دو انفجار پشت هم اومد
صدای انفجار، سیریک.
🔄
استان بوشهر
سلام وحید جان بندر بوالخیر  رو زدن
سلام اقا وحید بندر بوالخیرو زدن
🔄
عسلویه بوشهر
یکی که در واکنش به خبر  قبلی درباره عسلویه پیام داده بود: "ببین ۱۰ دیقه پیش صدا اومد ولی نزدیک نبود" الان پیام داده که:
وحید اینجارو دارن میزنن
همین الان صدا و لرزش خونه ۱۰ تا انفجار
عسلویه
پیامی دیگر:
عسلویه
حدود یک ساعته نه یا ده صدای انفجار اومد که دوتای اخری خیلی شدیدتر بود
ولی منطقه پتروشیمی و پالایشگاه خداروشکر خبری نیست
همه‌ی صداها از  سمت ساحل حاله و ساحل بنود یا بندر تین هستن
تقریباً بین۱۰تا ۲۰ کیلومتر با عسلویه فاصله دارن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76941" target="_blank">📅 02:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76940">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vQxulJH0yw4TqsALqk0C8A0D0IGib48nWqAX2p_x9XnWfOvaMM3EU9A5PvA3iB-_WoU7usa3a4k3xj-OdV2fX1IGrnRDPu-I0Yj-IKR-vnWfQ2XCF1eLPagt7s8w3TeboUWEWqgw8W6hkrul68XGZMAnNJIrbrhwpBheDIs4VO-nic8IQrQzG9rqxjrASSyBT_ILFcc-TNcDvDE41gp4W81WUbEQ_jNogFjgHlLHx5UF4V_plrQrjaTinrQXsjMHDAtbHq85RRHxFZm9vbc4t85XW08CgjAKHNZaZqB249xDbT0BqzEbzxm7D2M14vy1xYkdAj4NdOcG-v6MZUTTaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با بیانیه سپاه پاسداران مبنی بر «بسته بودن تنگه هرمز تا اطلاع ثانوی و پایان مداخلات آمریکا»، یک مقام آمریکایی در گفتگو با خبرنگار آکسیوس اعلام کرد که سپاه یک موشک به سمت یک کشتی باری تجاری که قصد عبور از تنگه هرمز را داشت، شلیک کرده است.
به گفته این مقام، کشتی مذکور مورد اصابت قرار گرفته و دچار خسارت شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/76940" target="_blank">📅 02:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76939">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ve5tMQB7jntfPx4yyzfzfkhqz_UJuOzcQO-NgNxHOyYQMRa_-7mQotAhQPXPYlq3tlL2uQXmyAPYHE8s18C7vuY5Qrh_oq6A4IpoMTZ-7pqaCCVZ6edmjzOgWQvAZ_QFGTMDzDBG9kWmze4cFQLgj2uSY-04TbXD1cFO6ym8RwaH5ytNCEQ9EteJKB3nLO6HlZotitdRXevJJhwR23pVvezeB2hUehtXQGsoq57UNEyDZEvx_1h1is1_aUw2-3xLS-EJYGju8s8_pQLkT0HCacOcBN9cPvLyfZ0BspOSEEgptbKIaCUk9DADjof-xPt8jJJQ3QG-_qbgjdVbsI-AAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: یک کشتی را هدف قرار دادیم / تنگه هرمز تا اطلاع ثانوی بسته شد
ایرنا:
نیروی دریایی سپاه پاسداران انقلاب اسلامی:
🔹
بسم الله قاصم الجبارین
در اطلاعیه قبلی گفته بودیم مداخلات بیگانگان و تعیین مسیر غیرقانونی حرکت کشتی ها در تنگه هرمز، برخورد قاطع ما را به دنبال خواهد داشت و روند افزایش ترددها در تنگه را با اخلال مواجه خواهد کرد.
🔹
ساعاتی قبل، این تذکرات نادیده گرفته شد و با تحریک بیگانگان چند کشتی تلاش کردند از مسیر غیرمصوب حرکت کنند و به اخطارها و تذکرات ما در اصلاح مسیر و حرکت در مسیر مصوب بی اعتنایی کردند.
🔹
به ناچار یک فروند کشتی‌ که با خاموش کردن سامانه‌های خود امنیت دریایی را به مخاطره افکنده بود؛ مورد اصابت شلیک‌اخطار واقع و متوقف شد.
🔹
به دنبال این حادثه، اولا با توجه به بروز این ناامنی به سبب مداخله غیرقانونی بیگانگان، تنگه هرمز تا اطلاع ثانوی و تا پایان مداخلات آمریکا در این منطقه بسته و هیچ شناوری اجازه تردد نخواهد داشت، ثانیا اگر دشمن متجاوز به بهانه این حادثه که خود، مسبب آن بوده است، خطایی کند و تجاوز جدیدی علیه ما داشته باشد با شدت پاسخ داده خواهد شد و پایگاه های جدیدی از دشمن در منطقه مورد هدف قرار خواهد گرفت.
🔹
عواقب چنین مداخله‌ای بر عهده دشمن آمریکایی - صهیونی و کشورهایی است که خاک خود را برای این تهدیدات در اختیار پایگاه دشمن گذاشته‌اند.
و ما النصر الا من عند الله العزیز الحکیم
نیروی دریایی سپاه پاسداران انقلاب اسلامی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76939" target="_blank">📅 01:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76938">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خبرنگار اکسیوس:
‏
🇴🇲
🇮🇷
یک دیپلمات که در جریان مذاکرات قرار گرفته است گفت عمان در گفت‌وگوهای امروز مسقط پیشنهاد کرد که مسیر جنوبی در آب‌های عمان و مسیر شمالی در آب‌های ایران، هر دو به‌طور کامل فعال باشند.
‏
🇴🇲
🇮🇷
این دیپلمات گفت طبق پیشنهاد عمان، مسیر جنوبی بدون هیچ‌گونه الزام برای دریافت مجوز باز خواهد بود؛ همان‌طور که پیش از جنگ بود.
‏
🇮🇷
🇴🇲
این دیپلمات گفت ایرانی‌ها نتوانستند این پیشنهاد را در جلسه به تصویب برسانند و ناچار شدند آن را برای گفت‌وگوهای داخلی به تهران ببرند.
BarakRavid
سی‌ان‌ان:
یک منبع آگاه از مذاکرات به سی‌ان‌ان گفت عمان پیشنهادی را برای مدیریت تردد در تنگه هرمز از طریق دو مسیر با کنترل جداگانه تدوین کرده است.
بر اساس این توافق که هنوز نهایی نشده است، هر دو کریدور باز خواهند ماند. کریدور جنوبی که از آب‌های سرزمینی عمان عبور می‌کند، امکان کشتیرانی آزاد را مطابق شرایط پیش از جنگ فراهم خواهد کرد.
کشتی‌هایی که از کریدور شمالی، در آب‌های سرزمینی ایران، عبور می‌کنند، باید از ایران مجوز قبلی دریافت کنند؛ با این حال، طبق این توافق هیچ عوارضی از آن‌ها دریافت نخواهد شد.
CNN
علی قلهکی
:
قرار بود سفرِ عراقچی به عمان منجر به صدور بیانیه مشترک درباره مسیرِ شمال و جنوبِ تنگه هرمز گردد و در ادامه نیز «قالیباف» و «ونس» به مذاکره اضافه شوند که با بازگشت عراقچی، گمانه‌زنی‌ها درباره به بُن‌بست رسیدن دیپلماسی در مورد «بند ۵ تفاهم‌نامه»، بیش از همیشه تقویت شده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/76938" target="_blank">📅 22:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76937">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ScYm5r_GqrANkZkctaZc9F5dxGK3g_VD2Jh0_E29G_UBW-DloL_E5x3iXoVywnJnui4kePwETkuUUg9_4ZocNzfGTlkrzz7QTebbO9ZN5MGHo8WCisrsGdgaxBCxfuhlHEcKu24yhX8mYiP9hdFRE0DkLFqS0PV3hBWQomWzlLfdxlP-GxVjJ-COg3U6sjQsFbxVhdstZwxBGR37GCATewRMC7Lxeht8LKjRB0uhfQnMtKH_vxoqQ6uA2flEWq97ooLxsum4J49AYh2e8I4PzuXrH5k9g6UpQQYEaJUjviy2S6HZRmGBhU-p8akg2NFd9Jra0s2bpAjUuIRp3EWAqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش ایسنا، طی روزهای گذشته پیش بینی شده بود گرمای هوا تا هفته منتهی به دوم مردادماه با میانگین دمای بالاتر از ۳۹.۷ درجه تداوم خواهد داشت، از این رو تمامی سناریوهای بهره‌برداری شبکه بر مبنای نیاز مصرف ۷۵ هزار و ۵۰۰ مگاوات طراحی شده و مرکز ملی راهبری شبکه برق کشور و واحدهای عملیاتی صنعت برق در آماده‌باش کامل قرار دارند با این وجود بنا به گفته مسوولان شرکت توانیر  هیچ محدودیتی در تامین برق بخش خانگی اعمال نخواهد شد.
اما امروز  ۲۰ تیرماه برخی کاربران ایسنا [و بسیاری از دنبال‌کنندگان اینجا] طی تماسی عنوان کردند که در برخی مناطق  همچون محدوده ولیعصر، مطهری و قائم‌مقام فراهانی [و مناطقی دیگر و شهرهایی دیگر] با قطعی برق چهار ساعته مواجه شدند و با وجود پیگیری‌های ایسنا از شرکت توزیع نیروی برق تهران بزرگ تاکنون علت این خاموشی‌ها اعلام نشده است.
به گفته مشترکان همزمان، حجم بالای تماس‌های شهروندان با سامانه فوریت‌های برق ۱۲۱ موجب شده زمان انتظار برای ارتباط با اپراتور در برخی موارد به حدود نیم ساعت برسد.
isna.ir
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/76937" target="_blank">📅 17:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76936">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N2Rdcf-rKPWAhBVZEzAHOh2kTe5WugPDlUp7tylJN6nPRezKqbd_7IuEdtrCHN88MFcXHVNr-rOfjSlUeDcZSeZVV93ZdCLg8FvdD_aRIdycnr_kKUojgKTz8HrhGhQFE49n3Nft0lhECZd_OQR3BnA_Xqi8os5-kylxA0Hx1jAXqvkeUUv-v5fAD7REkwX2Ap3hmQ5Tv8Q7fXgKoeXYcgaYC_NfVQACzRgkgAHhEpQpnNbKcx6dWpUYcv5Uen-X1G2sBrufRIqJf9Gdntig44FGAyQjygdGEmvnNZg0eD9WpHHDazIr2tulDUjmHdO585ehID6os96oaBCjsIsrCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه امام رضا اعلام کرد دو نیروی بسیجی به نام‌های «سید سجاد علوی» و «مهدی هنرمند» در حوالی میدان سرافرازان مشهد هدف تیراندازی قرار گرفتند و کشته شدند.
بر اساس اطلاعیه سپاه، این دو بسیجی در زمان وقوع حادثه در حال گشت‌زنی در محدوده بلوار سرافرازان، در فاصله حدود ۱۵ کیلومتری حرم امام رضا، بودند. این حادثه همزمان با برگزاری مراسم تشییع و تدفین علی خامنه‌ای در مشهد رخ داد.
سپاه امام رضا اعلام کرده است که این نیروها در چارچوب مأموریت‌های تأمین امنیت مراسم تشییع و خاکسپاری علی خامنه‌ای در منطقه حضور داشتند.
در این حادثه همچنین یک عابر پیاده مجروح شد و به بیمارستان انتقال یافت.
اعلام کشته شدن این دو بسیجی در حالی صورت می‌گیرد که امیرالله شمقدری، معاون امنیتی [دروغگوی] استانداری خراسان رضوی، جمعه ۱۹ تیرماه
گفته بود
تیراندازی در بلوار سرافرازان مشهد «اقدامی تروریستی» نبوده و ریشه در یک «درگیری شخصی» داشته است.
خبر این درگیری مسلحانه همزمان با تدفین علی خامنه‌ای در شامگاه ۱۹ تیر منتشر شده بود. آن‌زمان اما جزئيات آن منتشر نشده بود. اگرچه ساعتی پس از این درگیری سازمان هواپیمایی کشوری از اجرای «مجموعه‌ای از تمهیدات ویژه» در مشهد خبر داده بود. همچنین گزارش‌ها حاکی از آن است که برای ساعاتی، مسیرهای خروجی شهر مشهد بسته شد و تدابیر امنیتی در این شهر به‌طور چشمگیری افزایش یافت.
این حادثه در شرایطی رخ داد که مشهد میزبان آخرین مرحله از مراسم تشییع و خاکسپاری علی خامنه‌ای بود و هزاران نفر برای شرکت در این مراسم به این شهر سفر کرده و امنیت شهر در بالاترین سطح خود بود.
@
VahidHeadline
شخص همون معاونی که اون طور صریح دروغ گفته بود امروز آمار هم اعلام کرده درباره تشییع‌کنندکان مشهد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/76936" target="_blank">📅 17:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76935">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VH0QraIrCx0vtibOkmrkRQ-G8tcdwhR_UhgzHJIDSM5d-wnLB9dN0VdQZtMoYUnhNNXcTU7YvHgf-Jx1jnB3xfl3DfYPyXBAqX4QoFK1vv_WshMeP9DfWI6b_ytQZ2guPT-OWSeRLaxlYtvvyBwxdYiGtq1BgbwbYXU_PBNRmPKXRbc1fLG2i3lOfX2VTKfzqQFWDyUyZkFV3g3Uo7JXSJfIwSlHVZNmzJBgGCUFQSgufezMSuWjN14WcAHL7blNv_entzyk6h1oAoQTWkg69Bf__U2obDblaB7U8sBEYHkwEhC8iLaWrWNEi3d-DBfj3tJITprDyozkvOk8byHQag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای، رهبر جمهوری اسلامی، در پیام مکتوبی منسوب به او که روز شنبه ۲۰ تیرماه منتشر شد اما تاریخ آن مربوط به دو روز پیش است، اعلام کرد انتقام خون پدرش علی خامنه‌ای «به‌طور حتمی باید صورت بگیرد».
خامنه‌ای در این پیام همچنین به «قاتلین» پدرش هشدار داد که «این جنایتکاران که فهرستی از صدر تا ذیل‌شان موجود است، آرزوی مرگ آرام و در بستر را با خود به گور خواهند برد».
او در عین حال تأکید کرد که انتقام «متوقف بر وجود شخص من یا سایر مسئولان نیست. ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادِ آزادگان در سراسر دنیا هر یک بخشی از این مأموریت الهی را انجام خواهند داد».
مجتبی خامنه‌ای در این پیام نامی از کسی نبرد، بخش‌های دیگر پیام خود را نیز به تشکر از تشییع‌کنندگان رهبر کشته‌شدهٔ جمهوری اسلامی اختصاص داد و به درگیری‌های اخیر ایران و آمریکا بر سر آتش‌بس، تفاهم‌نامه و تنگه هرمز نیز هیچ اشاره‌ای نکرد.
دونالد ترامپ، رئیس‌جمهور آمریکا، بامداد شنبه نوشت در صورت هرگونه اقدام یا تلاش برای ترور او، «هزار موشک آمادهٔ شلیک» به سوی ایران هدف‌گیری شده و ارتش آمریکا برای یک دورهٔ یک‌ساله، با امکان تمدید، آماده است «تمام مناطق ایران را به‌طور کامل نابود کند».
پیام عمومی مکتوب قبلی منسوب به مجتبی خامنه‌ای ۱۱ روز پیش به‌مناسبت هفتهٔ قوه قضاییه منتشر شده بود.
مجتبی خامنه‌ای در عین حال غایب بزرگ مراسم تشییع علی خامنه‌ای بود که بیش از چهار ماه پس از کشته‌ شدنش در اولین موج از حملات آمریکا و اسرائیل طی چندین روز با سازماندهی حکومت برگزار شد و نهایتاً ۱۸ تیرماه در مشهد به پایان رسید.
در جریان تشییع جنازهٔ یک‌هفته‌ای علی خامنه‌ای، بسیاری از شرکت‌کنندگان در این مراسم خواستار «خون‌خواهی» و «عدم سازش» شدند و گروهی نیز پارچه‌نوشتهٔ بسیار بزرگی با مضمون درخواست برای «قتل دونالد ترامپ» همراه داشتند.
مجتبی خامنه‌ای بود که کمتر از ۱۰ روز پس از کشته شدن پدرش در نهم اسفند ۱۴۰۴ به‌عنوان رهبر تازه جمهوری اسلامی معرفی شد، در هیچ بخشی از این مراسم حضور نداشت. در این مدت طولانی هیچ فایلی صوتی یا ویدئویی نیز از او که نشان دهد در چه وضعیتی است، منتشر نشده است.
این در حالی است که در مراسم تشییع جنازه علی خامنه‌ای تقریباً تمامی مقام‌های ارشد جمهوری اسلامی حضور داشتند، از سران سه قوه تا فرماندهان سپاه پاسداران و حتی سه پسر دیگر علی خامنه‌ای، مصطفی و مسعود و میثم، که از ۹ اسفندماه پارسال یعنی آغاز جنگ تاکنون خبری از آن‌ها نبود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76935" target="_blank">📅 17:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76934">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIeKTmwcwzApqQdPH4lWVuhgK6GGhmBr3S4pMIaGrG8gmCoIPeQwK-7gUnIg6KT4gIAGMWfk3-JUYVvm41j71N5uA5umjCqK8ae5sRdJhGjUe1kBC1xtxJof9q9DSZj-y-Dw3V8rnH61N74qStfUsF_2D1vqZ_QCC78a8rXECaQVr0ZhK3jLChCZK9TseirkqLQb42xqn4kFMC5yjOOVHL_96DOltaR2gOc4ji-Skp2JaZpvdVHcIWsNrs7xGoVsp3gxsV8CAN8v0JTaqcadptZwwTIwmaDjMWbl4OiJF6KpzH9EplyDScBbA0gKmcrktWBiR4YrLsznDtc7ZqUi0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای هماهنگی تشکل‌های صنفی فرهنگیان ایران، از صدور حکم حبس برای یک فعال صنفی معلمان خبر داد.
این شورا روز شنبه ۲۰ تیر اعلام کرد شعبه ۱۰۳ دادگاه کیفری ممسنی شکرالله احمدی، بازرس این شورا و عضو هیئت‌مدیره انجمن صنفی معلمان فارس، را در مجموع به سه سال و هفت ماه و ۱۵ روز حبس محکوم کرده است.
آقای احمدی به «اجتماع و تبانی برای ارتکاب جرم علیه امنیت داخلی و خارجی» و «فعالیت تبلیغی علیه نظام جمهوری اسلامی» محکوم شده است. او ۲۰ دی ۱۴۰۴ در خانه‌اش بازداشت و چند روز بعد آزاد شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76934" target="_blank">📅 17:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76933">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCJnvabSSNZTUqqz7Skfy0NoP8A7nioasi4lI-cacjAmmp_61Wzk2lqHDz0JMIMLXUzW0m1YNsX1IE8r9SgB6eG1-STQ6QkKm0SuwnuUVizOmpQT3iGjuCNPFvKVVMpjylxjcsLBdouhcWGUew44Ak-SVN6s_CeVPlRrrjbBXlVhgRqHFu-TVLNSjgNVqhw9mtYdriYxqhOqgX6lFXDB-sswIX-zHAKJwe3nRRKIJwU6XJdObIylCatUbL8052VgekTKkG8sSB0_5MTjs6D2G90OZhtvF46L2E1yxJa0xwKR6CHYavaQxh030v7XadfxNCa6M8wwQiE3kvTaBg1jUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کودک ۱۳ ساله در پی تیراندازی نیروهای مرزبانی به سوی یک خودروی خانوادگی در منطقه هو‌رامان استان کردستان جان خود را از دست داد. مقام‌های محلی اعلام کرده‌اند که این حادثه از سوی مراجع قضایی و نظامی در دست بررسی است.
تابناک خبر داد که این حادثه در منطقه مرزی «ته‌ته» هو‌رامان رخ داده است. اعضای یک خانواده پس از پایان کار روزانه در باغ خانوادگی، با یک دستگاه خودروی تویوتا در مسیر بازگشت به منزل خود در روستای «دره‌کی» از توابع شهرستان سروآباد بودند که نیروهای مرزبانی، به ظن آن‌که خودرو متعلق به قاچاقچیان است، به سوی آن تیراندازی کردند.
در جریان این تیراندازی، گلوله به کودک ۱۳ ساله‌ای که در قسمت بار خودرو حضور داشت اصابت کرد. او بر اثر شدت جراحات جان خود را از دست داد.
استاندار کردستان با تایید این حادثه اعلام کرده است که موضوع از طریق وزارت کشور، دادسرای نظامی و مراجع قضایی نیروهای مسلح در حال پیگیری است. او همچنین بر لزوم روشن شدن ابعاد حادثه، نحوه وقوع آن و اطلاع‌رسانی نتایج تحقیقات به افکار عمومی تأکید کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76933" target="_blank">📅 17:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76929">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/psNXqiUTWRGhpi-0ShMqOzwxw9nqsMJbVGG0BxlLWDbKvBMbWeV1WsQsNjQH6tfS86SVHAlD-ygNIxQyrQgSCxTqsmkYqeV9CB8zh4a0eoqu5FsFgfU8kaGHtzDZBng93dVV0Odu0Yu-5QK6kM4Ql2qfDNH0laGlp6Rhhz_Z_0OieZI2M3iCdxO6xUY5hiNeK-I9AHes0d1ujFg1klXaCap9FGlJUxCcgKlb5tK-Ka9AGJ3UGMks7HJ6bAUg2EpUbQpb3pKpnyN6_n_uDQj1hROP2y8EN7udSHTtF4nM7OregekAO8ITAn0cer0C8pKC68AUeYVnYBcghT_KuvhohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HXoSlrdqlfqAxZTL-Jmls3Hr_IvoIQCgNoY8MQojZusscfeLmUJV1ohMPlFKWj9JIU5HfETaFBlzv9NFOYjckl58W3YgtLQnVb9Yi8B2ufpN9j_SRhmZgSoOQ5wfqI-enMo0ocVTC3RTrkd-awwjDikLu1TZWjo1mddXz-ZBVM2LiN1ZBmif_o7naKfz_h9_7jNcHn4denhbRlOTlt5mZy3Ah6povRx7ZwMzAN0wYejXyhVS0l_Z04o2llG-tfQSjOGBAwKWiZ6x5mV9QO11Kw17815iVtcVI5vGHhxLviuoR1ysAxOXT4UUlfdMJhZ5JI--abdUpAA-vLQCoYUJ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hzVoJfJevMwm6m1aMbzeNm1yLtHxKzIdevvfCIK6Ca0dw230OwVOYnKOXUY9gCKZeLuSe5PSaHS1k44-W98mQRp89TIqqEnIZNw5kS_cpkHOpV2LLiPzBRk_QK2JqFFFF1AYZsODzrpQ6-i5VmvzTIuMKzEUaCw9xD-YUTRwH9y1PunX1L28OfhZ8ARYroRW9Xf4Xq8_D8qj8mnZkTiiciBwHEpTqhtFoWJvGwa_Wm-DxYSO1m63wrtU8QbpaoSU_XTxHT7VG4WJUo11tqYE3hcX20LGErJGYUL2sdezD-UUnRGWr0AXr_RBwFDqFcWaBowEjdEJfGIqx5zXvo3VFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2993ded2a7.mp4?token=Rx1a_NKQPwmhKVAkxtW4vOPBryElZLk3qRkEHeudmfqlJLxyvpj78BcwWMPeZV5cxO-toMw3KtTwW3F_HYHNJG8BUsjDTAeX3-YzEfYR_wU_0v6BYuJMfA7O8l1_mHKfuvSmEmy8h0HLdXtS-AVObtK5F2wEH41h0DeW0MTMhcUDW4Ecq5Ww-7OJi7UPNAKJjwjAGGrqivgyZrO3_2Gmr19a8Ugydgxo7QanMJVEWNougH-3T9Z9khyg5dltYk866Kl5qZfXxt45Kb4px2NyGW8lV7uRj21uA4AbwiPQnOgjnSGQdCTiIBzwbU-a7m2lmo89e3RfVjHcpStKoWs_lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2993ded2a7.mp4?token=Rx1a_NKQPwmhKVAkxtW4vOPBryElZLk3qRkEHeudmfqlJLxyvpj78BcwWMPeZV5cxO-toMw3KtTwW3F_HYHNJG8BUsjDTAeX3-YzEfYR_wU_0v6BYuJMfA7O8l1_mHKfuvSmEmy8h0HLdXtS-AVObtK5F2wEH41h0DeW0MTMhcUDW4Ecq5Ww-7OJi7UPNAKJjwjAGGrqivgyZrO3_2Gmr19a8Ugydgxo7QanMJVEWNougH-3T9Z9khyg5dltYk866Kl5qZfXxt45Kb4px2NyGW8lV7uRj21uA4AbwiPQnOgjnSGQdCTiIBzwbU-a7m2lmo89e3RfVjHcpStKoWs_lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شنیده شدن صدای انفجار حوالی پارچین، پاکدشت و قیامدشت در جنوب شرق تهران و دیده شدن دود
شنبه ۲۰ تیر
Vahid
خبرگزاری فارس:
فرماندار پاکدشت: صدای انفجار ناشی از امحای مهمات بود
صدای شنیده‌شده مربوط به عملیات کنترل‌شده امحای مهمات باقی‌مانده از جنگ بوده و هیچ‌گونه حادثه یا تهدیدی متوجه شهروندان نیست.
این عملیات با رعایت کامل ضوابط ایمنی و توسط نیروهای مسئول و متخصص انجام شده و از پیش برنامه‌ریزی شده بود.
پس چرا اعلام نشده بود؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/76929" target="_blank">📅 09:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76928">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H2lWzuyL3-PJtwUk2M28sXKXqbJcqArx5kRinaXIA44CMxkHdKegrs-GWcSZxebjm483XbmWYQk0zzT4wuVX5CctJ5X7Qqb2XKqUmlb081qgO2k1BK7Cjty0-54rbhk-fEcEuXUfiZk7_q90hpsHrL5HNHqcK9OT905vMxRuW3_TNJYFDs2Oojcwj8Ylzlz_FlDbbrOYyZgs57v_wVz4TjiCIeo145gEPHEAu5-foVp7gSPM4zB5zKEsN6lBoesSmCyD0GNhLeMGpjF0l_4P6TbODlz-6eb2fvoTNi_tR9vRJpVG-3bZZemhbSGMEuErbr7U1nnujRMtpTBrqTeFhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
صدای انفجار در پاکدشت پارچین
سلام وحید جان
پارچین همین الان صدای یه انفجار شدید ۹:۳۱
صدای وحشتناک قرچک. مغازه لرزید
کل قرچک صدا رو شنیدن
معلوم نیست هیچی
ساعت ۹:۳۰ صدای انفجار شدید سمت پارچین
دودش مشخصه
قیامدشت کلا لرزید
شهرک صنعتی خاوران
شیشه های مغازه لرزید ۹:۳۰
سلام ما خاور شهریم صدای انفجار شدید اومد شیشه ها لرزید
صدای انفجاری محیب از قیامدشت به گوش رسید
به حدی مهیب بود خونه لرزید
سمت شهرری هم لرزید حتی
درود ، عزیز پاکدشت صدای انفجار اومده دقیق ساعت 9:28
سلام ماهم صدای انفجار پاکدشتو حس کردیم از خواب پریدیم و ترسیدیم ولی یک انفجار بود
سلام اقا وحید ما تو قیامدشت چنان حس کردیم که انگار کارخونه خودمون منفجر شد
کل قیامدشت و چهلقز شیشه ها و خونه ها لرزید
سلام وحید جان ،پارچین انفجار شدید بود،ما قیامدشتیم،موجش تا اینجا اومد
سلام قرچک صدای انفجار اومد شیشها لرزید ولی دود دیده نمیشه
سلام ما محله ی ارکیده های پاکدشت زندگی می‌کنیم
و انقد انفجار شدید بود ساختمان ها لرزیدن
سلام پردیس  شنبه ۲۰ تیر حدود ساعت ۹،۳۰ یه صدای بلند اومد
ما پارچین هستیم همین الان صدای انفجار اومد تقریبا ده دقیقه قبل ،الان دودش هم میاد
وحید جان پارچین یه انفجار شد ستون دودش معلوم بود. پشت تپه های پارچین
تموم خونه ها شدید لرزیدن
سلام. نارمک ما صدارو شنیدیم تا قبل پیامها فکر کردیم توهم بوده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/76928" target="_blank">📅 09:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76927">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vB26bJ260Wd5AmFyZYGLKe_Fzqpe1QCUlP0PQyjL9xa18lRgeMGeHsU1c9QCX-E1mosU-NIV5UPD86RMELxYhOiTQ9uf_78K-Pz7awOWSe1G9EIKdf-7vM72UEP92C_WhVahGuv_pi046LOY8nQ_Zf8C4aWPpUdM6V3hLC6hhJBBKUZG1R9E4BA5vuAMR2U8jum_AF2FkATk3v68ps1eLL8peBTW3S1EQsQxUkfkuD2QplJQWLUUe-l1RuCm8Fe2RrXF2ICbudNd6fH65m5INcRLXb79XHu5EpBBOWFz9FtLN_hhocZnQBkLVO1LXRja_tuw-kFnTgJ2x_lOhQd6mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر تهران برای ترور من تلاش کند، هزاران موشک دیگر شلیک خواهند شد
ترجمه ماشین:
هزار موشک در حالت آماده شلیک قرار گرفته و جمهوری اسلامی ایران را هدف گرفته‌اند و در صورتی که دولت ایران تهدید خود را ــ که در بسیاری از نقاط جهان اعلام کرده ــ برای ترور یا تلاش برای ترور رئیس‌جمهور مستقر ایالات متحده آمریکا، که در این مورد شخص من هستم، عملی کند، بلافاصله هزاران موشک دیگر نیز به دنبال آن‌ها شلیک خواهند شد!
دستورها از پیش صادر شده‌اند و ارتش آمریکا آماده، مایل و قادر است برای مدت یک سال ــ که قابل تمدید است ــ تمام مناطق ایران را به‌طور کامل درهم بکوبد و نابود کند — ستایش از آنِ الله باد!
رئیس‌جمهور دونالد جی. ترامپ
1000 Missiles are Locked and Loaded and aimed at the Islamic Republic of Iran, with thousands of more to immediately follow, should the Iranian Government act on its threat, pronounced in many corners of the Globe, to assassinate, or attempt to assassinate, the sitting President of the United States of America, in this case, ME! Orders have already been given, and the U.S. Military is ready, willing, and able, for a one year period of time, subject to extension, to completely decimate and destroy all areas of Iran - PRAISE BE TO ALLAH! President DONALD J. TRUMP
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76927" target="_blank">📅 09:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76926">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XB-TUw9A-Cl6eH5NeO_nuHkC6DYg5aau7XJ8fGUs_3L_0EHX-mSmL0MlToHqfg4zOIP48Zi4RGe48SeCFPpWP3oYDKTkr-459OhVv7mpehcvbwBX29lp4Sy_oD_Rv0RlE58sKxer6zGx0uczMPVBk-RBP-iDQi1UyFkeiK3hTVZbDGhhfqPHeNIguzpXoLrorE_J_MKnA8s3j_W49W98xwKZ76FbW6I_OctSFqEFO49G11HIaWBSTTCHWJstvRnHmWIj3SmPElQvfhfdJcczEBu8WOcpiBikOJpSzumQ3qgsQLGBY9J5dVez1p5WZTVaRNZKEVpfGvt36IeD6-sxbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «سی‌بی‌اس نیوز»، مقامات ارشد آمریکایی روز جمعه فاش کردند که مقامات ایران در پیامی محرمانه به مشاوران دونالد ترامپ اعتراف کرده‌اند که شلیک به کشتی‌های تجاری در تنگه هرمز یک «اشتباه» بوده و این حملات توسط یک جریان «خودسر» از تندروها با هدف تخریب مذاکرات انجام شده است.
با این حال، کاخ سفید این اقدام را نقض صریح آتش‌بس دانسته و خواستار اعتراف علنی تهران به این اشتباه شده است.
براساس این گزارش، تیمی ارشد از سوی ترامپ، شامل جی‌دی ونس، معاون رئیس‌جمهوری، جارد کوشنر، داماد ترامپ، استیو ویتکاف، فرستاده ویژه کاخ سفید و مارکو روبیو، وزیر خارجه، مامور شده‌اند تا گفتگوها را روز شنبه در عمان ادامه دهند. در حالی که واشنگتن انتظار دارد ایران پس از این نشست تعهد خود را به باز بودن کامل تنگه اعلام کند، مقامات آمریکایی هشدار داده‌اند که اگر ایران نتواند به این ساده‌ترین بخش توافق پایبند بماند، امیدی به حل مسائل پیچیده‌تر نظیر تسلیم ذخایر اورانیوم غنی‌شده نخواهد بود و در صورت ادامه اقدامات خصمانه، با پاسخ سخت نظامی و اقتصادی مواجه خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/76926" target="_blank">📅 09:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76925">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OGdhxaYVIRMCxHzwY15G6M83JoZmT37_TasfqayVBF_MzCL-zdv2bk6d_wkYwZysK_NN6a7MuweUy_RhoJjDDycYbL8j8OOd6xGymz41rcnrwfTNtgQhquHu2zkiQIxMtnKCzQkF9X1BiwZGlnMgjQ14196OjBGTYMiNmKkTMifOmUlfwFRFqOYzjwGyeNwH3vOzM5VxEKfw9AuAYF5LzDUWm7NsQ-Tl5M5GSwhzt3mMRceBW-2XSg2Fzy4h_yTDtoTbgK3xOAFrl1ro-6LOqEJ2HtJuFhdUDQ4MbO8LT7ELD5-h7ara45QGAxjTnaDEUO3PivG1CewkZpOYDe26_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا از ایران خواسته است ظرف ۲۴ ساعت علناً متعهد شود که شلیک به سوی شناورها در تنگه هرمز را متوقف خواهد کرد
اکسیوس (ترجمه ماشین):
سه مقام ارشد آمریکایی روز جمعه در جلسه‌ای توجیهی با خبرنگاران گفتند ایالات متحده، هم به‌طور مستقیم و هم از طریق میانجی‌های منطقه‌ای، از ایران خواسته است امروز، شنبه، بیانیه‌ای علنی منتشر کند که در آن روشن شود تنگه هرمز باز است و ایران متعهد شود به سوی کشتی‌های تجاری عبوری از این منطقه شلیک نکند.
چرا اهمیت دارد:
ایران با چندین بار شلیک به سوی کشتی‌های تجاری در تنگه هرمز، یادداشت تفاهمی را که سه هفته پیش با ایالات متحده امضا کرده بود، نقض کرد.
این اقدام به چند دور تبادل آتش انجامید و توافق را در معرض فروپاشی قرار داد.
مقامات آمریکایی می‌گویند اگر ایران به چنین تعهد روشن و صریحی پایبند نباشد، این موضوع تردیدهای جدی درباره اجرای یک توافق هسته‌ای ایجاد می‌کند؛ توافقی که بسیار پیچیده‌تر و حساس‌تر است.
محور خبر:
قرار است عباس عراقچی، وزیر امور خارجه ایران، و بدر البوسعیدی، وزیر امور خارجه عمان، روز شنبه در مسقط دیدار کنند تا درباره وضعیت تنگه هرمز گفت‌وگو کنند.
عمان در هفته‌های اخیر، حتی پیش از امضای یادداشت تفاهم، با ایالات متحده و متحدانش در خلیج فارس همسو شد و یک مسیر کشتیرانی جنوبی در نزدیکی سواحل خود گشود که کشتی‌ها می‌توانند از طریق آن از تنگه عبور کنند.
ایرانی‌ها که معتقد بودند این اقدام اهرم فشارشان در مذاکرات با ایالات متحده را تضعیف کرده است، خشمگین شدند.
مقامات آمریکایی می‌گویند اعضای تیم مذاکره‌کننده ایران به آن‌ها گفته‌اند عناصر تندرو در داخل حکومت تصمیم گرفتند برای بازگرداندن این اهرم فشار، شلیک به سوی کشتی‌ها را آغاز کنند.
در مواضع علنی، تیم مذاکره‌کننده ایران، فرماندهان سپاه پاسداران انقلاب اسلامی و دیگر مقامات ارشد، همگی موضع واحدی دارند و خواستار کنترل ایران بر تنگه در آینده هستند.
پشت پرده:
یک مقام ارشد آمریکایی مدعی شد که پس از دو روز درگیری در اطراف تنگه در اوایل این هفته، ایرانی‌ها «دوباره به سراغ ما آمدند و خواستار گفت‌وگوهای بیشتری شدند تا برای حل برخی مسائل تلاش کنند.»
این مقام آمریکایی گفت: «آن‌ها به ما گفتند: “گند زدیم. اشتباه کردیم. بیایید به گفت‌وگو ادامه دهیم.”»
به گفته او، در داخل حکومت ایران بر سر اجرای یادداشت تفاهم و مرحله بعدی مذاکرات با دولت ترامپ، جنگ قدرتی در جریان است.
یکی از مقامات ارشد آمریکایی گفت: «افرادی در داخل نظام آن‌ها هستند که می‌خواهند به توافق برسند، اما ما نمی‌توانیم به‌جای آن‌ها تصمیم بگیریم. خودشان باید اوضاع را تحت کنترل بگیرند.»
چه می‌گویند:
مقامات آمریکایی گفتند انتظار دارند ایرانی‌ها پس از نشست روز شنبه در عمان بیانیه‌ای منتشر کنند.
یکی از مقامات ارشد آمریکایی گفت: «ما می‌خواهیم آن‌ها علناً بگویند که شلیک به سوی کشتی‌ها را متوقف خواهند کرد و به‌صراحت یا دست‌کم به‌طور ضمنی بپذیرند که گند زده‌اند.
در حال حاضر روی همین موضوع کار می‌کنیم. انتظار داریم ایرانی‌ها بگویند همه مسیرهای کشتیرانی در تنگه باز خواهند بود و هیچ عوارض عبوری دریافت نخواهد شد.»
یک مقام ارشد آمریکایی دیگر گفت اگر ایرانی‌ها از انجام این کار خودداری کنند، پیامدهای سنگینی در انتظارشان خواهد بود. او گفت: «اگر فردا موضع آن‌ها این نباشد، روز خوبی برایشان نخواهد بود.»
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/76925" target="_blank">📅 00:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76924">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IwlKnTZn7WGd0CeRNeCZcv0Fuve5UfUUwTZkZzmbWhs1NuffKZkFioOONtNP-eeY2wHplBO7H95tI8b5ZpZ8mM0Rr_kfA0cOqclU5AoRJ-B8fvHTOD26yQ80ohmDX4iAa0ftUtk7vBP50RGCFAlYusiwK7djQAwbiQgQyP6Dx-Irpp9v8LqaLDWluNQgCc7_PNCcCxtEKgu4a2r5zoAu1bAL0_X-SsrlCLIDM9S4RKj9AvTZX907v5wM-GEm8PoTw6O5pYMWlCc1XHTtsitvKa-xjhtiQWujDMOAA4czK8InAdn3X_aATfjdaVeG59S15ruTXaBwSDq9J-cWubiXXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا در اقدامی که از بی‌اثر شدن تفاهم اخیر میان تهران و واشینگتن حکایت دارد، تحریم‌های تازه‌ای علیه جمهوری اسلامی و شبکه مالی آن وضع کرد. در فهرست تحریم‌های جدید نام علی انصاری، از چهره‌های نزدیک به مجتبی خامنه‌ای و متهم به فساد اقتصادی، دیده می‌شود.
وزارت خزانه‌داری آمریکا جمعه ۱۹ تیر اعلام کرد این تحریم‌ها در واکنش به حملات جمهوری اسلامی به کشتی‌های تجاری در تنگه هرمز اعمال شده است.
این وزارتخانه علی انصاری را «تسهیل‌گر مالی» جمهوری اسلامی معرفی کرد و نوشت او بر شبکه‌ای گسترده از دارایی‌های جهانی به سود مجتبی خامنه‌ای و دیگر مقام‌های حکومت نظارت دارد.
بر اساس بیانیه وزارت خزانه‌داری، انصاری با نهادینه کردن اختلاس در ساختار جمهوری اسلامی و انتقال ثروت‌های عمومی به مجموعه‌ای از املاک و دارایی‌های تجاری در خارج از کشور، خود، مقام‌های حکومت و مسئولان ارشد دفتر رهبر جمهوری اسلامی و سپاه پاسداران را ثروتمند کرده است.
وزارت خزانه‌داری آمریکا همچنین شماری از صرافی‌های کلیدی وابسته به حکومت ایران را تحریم کرد؛ نهادهایی که سالانه میلیاردها دلار را به نمایندگی از بانک‌های تحریم‌شده ایران جابه‌جا می‌کنند و با استفاده از شبکه‌ای از شرکت‌های پوششی، فعالیت‌های مالی حکومت را پنهان می‌سازند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، پس از وضع تحریم‌های جدید گفت مجتبی خامنه‌ای «در حالی در انزوا پنهان شده که حکومتش در حال فروپاشی است».
او ادامه داد: «وزارت خزانه‌داری همچنان از همه ابزارهای خود برای جدا کردن او و دیگر مقام‌های ارشد حکومت از نظام مالی جهانی بهره خواهد گرفت. ما این دارایی‌ها را برای مردم ایران حفظ خواهیم کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/76924" target="_blank">📅 22:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76923">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb410e1088.mp4?token=TYW6t2RuU0jXz_V031lTczWqpfu0l9G3rZDxhNSsaUwWbGh2oghIomOE30bAssyxzKOuA4wmVHA6gCGqxV4240pBNMQc3VzTgCYOdzmgA1YMFXe5tzKUArqmrBAmuIykY6TiDPVuvInb68RnKybZhO44CIN1wSMztCTDINo56_6W27dt-6IvBRopjztReoPEGdq6hphvV2vLf8udbr5s3bAMObwD085FToybTn2bzKrplRKalsfqoK8RpmCKpdU1CihdtgQHUF2dfdbKec8qg4NucovSVmVDcJ5vy_BEVyC-dIE0peWC0OYKho8YK409luRcRO2qJG7Q4VQ25QGE9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb410e1088.mp4?token=TYW6t2RuU0jXz_V031lTczWqpfu0l9G3rZDxhNSsaUwWbGh2oghIomOE30bAssyxzKOuA4wmVHA6gCGqxV4240pBNMQc3VzTgCYOdzmgA1YMFXe5tzKUArqmrBAmuIykY6TiDPVuvInb68RnKybZhO44CIN1wSMztCTDINo56_6W27dt-6IvBRopjztReoPEGdq6hphvV2vLf8udbr5s3bAMObwD085FToybTn2bzKrplRKalsfqoK8RpmCKpdU1CihdtgQHUF2dfdbKec8qg4NucovSVmVDcJ5vy_BEVyC-dIE0peWC0OYKho8YK409luRcRO2qJG7Q4VQ25QGE9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به گزارش رسانه‌های دولتی چین، ‌این کشور برای نخستین بار با موفقیت یک موشک با قابلیت استفاده مجدد را فرود آورد که این امر پیشرفت بزرگی برای برنامه فضایی این کشور محسوب می‌شود.
پیش از این، قابلیت استفاده مجدد موشک‌ها در انحصار شرکت‌های اسپیس‌ایکس ایلان ماسک و بلو اوریجین، متعلق به جف بزوس، بنیانگذار آمازون بود. حالا چین با انجام این آزمایش موفقیت‌آمیز می‌تواند برتری آمریکا در زمینه موشک‌های قابل استفاده مجدد را به چالش بکشد.
شرکت فضایی اسپیس ایکس در دسامبر ۲۰۱۵، برای نخستین بار یک موشک فالکون ۹ قابل استفاده مجدد را فرود آورد و پس از آن در نوامبر ۲۰۲۵، موشک نیو گلن شرکت بلو اوریجین به زمین نشست.
فالکون ۹ حالا حدود ۱۵۰ بار در سال با پیشرانه‌هایی پرتاب می‌شود که قابلیت ده‌ها بار استفاده مجدد را دارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/76923" target="_blank">📅 21:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76921">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aMBVM4YlIEPLruJjcTRc2nPH54TBjAz0ZEkDGhU4G3KiJCtN6JBHXlt8pQHljxq4uxNxk5qCISyGFLsYB1NM_9kRdvG_KzJe3tBR3cxPx9rw-o6yLwsvUelw9KGdH92CNxirVv1843D087BYdh0dn8hjioMy1PkBNI97TKBRlI6BRnF5tfEP13ycsAAeWtPgRe3IjY8aZF-gVv05mZF0BB8IL6tuBksDbTia9yAq63I5qe3sqNrMq0tNchC4WCcYKstaPHpP4Hz3lp33mykaFX2HqCAID_X5J92Tj5nLwlPAeC_EaxgIIFCrKbNdOt7Yj6qPe0wAuby5W3y3k-w0Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf31c0a00e.mp4?token=qMEGhGm_Vq3R-Rh24YJIgIQ1_7YPVeOPd_LmPLmG-FdEoC5vNCs4vWgzvsJ5gO-fbSiT-ygDTCLIgkMcbtKXin9W-nHCi2tZJj782DnOP2gxZpdaWftL5OXRjgRXafnt-h_51JL4zBy7WGi7sXAi0_XqvzIG_Sv2LIurnKD67nsiBITsxSrQQP9Mal1OkJIHepmamIp6PEtsEU5enFlh1yAXj5UHWOu6riOHqRwoOfn0iU8uGpBgKRNM-1ZC-0hzxnG0AVPhIBVTI0foscwLXSDLYDhkqHuAQEMpqcudMy9QK44WI3ghmcG3sI_ALrsEalgFH9JjPugcDHWXlX3Bag" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf31c0a00e.mp4?token=qMEGhGm_Vq3R-Rh24YJIgIQ1_7YPVeOPd_LmPLmG-FdEoC5vNCs4vWgzvsJ5gO-fbSiT-ygDTCLIgkMcbtKXin9W-nHCi2tZJj782DnOP2gxZpdaWftL5OXRjgRXafnt-h_51JL4zBy7WGi7sXAi0_XqvzIG_Sv2LIurnKD67nsiBITsxSrQQP9Mal1OkJIHepmamIp6PEtsEU5enFlh1yAXj5UHWOu6riOHqRwoOfn0iU8uGpBgKRNM-1ZC-0hzxnG0AVPhIBVTI0foscwLXSDLYDhkqHuAQEMpqcudMy9QK44WI3ghmcG3sI_ALrsEalgFH9JjPugcDHWXlX3Bag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درخواست افتخاری برای حذف صدای خود از آلبوم "بدرقه" [بدرقه خامنه‌ای]
علیرضا افتخاری با انتشار ویدئویی علت این درخواست را ضعف فنی اثر عنوان کرد.
این آلبوم با صدای هفت خواننده از جمله محمد معتمدی، پرواز همای و ... به مناسبت تشییع پیکر رهبر جمهوری اسلامی ایران، توسط شهرداری تهران منتشر شده است.
Koronmusic
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76921" target="_blank">📅 20:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76920">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1e9af1050e.mp4?token=gXMvGEgba9QSO9fatJMd0TQZVr2ONRm09U5nSFRp3Ee7eniOrLuARcCdLlwtMxR67hvNilhAfBVoDOBMf30jdGkxGDJ-OFvFdwWate8oxpvPOY2ijlJ5Rjx0zeLPvq6kDCdJGfX91SJVhCdrArmIWj_E9ttki-RlImDRqEIbrz38KBEh_9dyHBM3wgqfLYZ_oIggO-vGqUazAR3bCPHGqsLbmhSHkl4tAG-qY0EMOAknvw1iz6AsXol-xZgy8J0A6mxlJyKGSLYqYckD-LWWCihSF2Mz8vqP75BfTYf6X_ZORedEzEwzZIe1ZFYYQQ6pQNzqqYyfHaaLB0bvtgxEUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1e9af1050e.mp4?token=gXMvGEgba9QSO9fatJMd0TQZVr2ONRm09U5nSFRp3Ee7eniOrLuARcCdLlwtMxR67hvNilhAfBVoDOBMf30jdGkxGDJ-OFvFdwWate8oxpvPOY2ijlJ5Rjx0zeLPvq6kDCdJGfX91SJVhCdrArmIWj_E9ttki-RlImDRqEIbrz38KBEh_9dyHBM3wgqfLYZ_oIggO-vGqUazAR3bCPHGqsLbmhSHkl4tAG-qY0EMOAknvw1iz6AsXol-xZgy8J0A6mxlJyKGSLYqYckD-LWWCihSF2Mz8vqP75BfTYf6X_ZORedEzEwzZIe1ZFYYQQ6pQNzqqYyfHaaLB0bvtgxEUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">PapiTrumpo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/76920" target="_blank">📅 19:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76919">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NW28BPwnfFnFdigPamtNg9UjkaODP5jA8kkfQtoWdt8aJ2WhcKnFG8sOd-2vzCoH82eMKGX39ZGpDmOLTMh8eeWRjWBVEvWN8w58bGSDjtLkYYItLW6CrURBbQ47wI4sWWYa97NpUfPxVrawj74TGLSK5oE2OTZ0SYSpJzveS-odviYj7Ebquw9ov5hyJZvDnwtJkfwwyh8rm-agWL6SvYxWiiyXkMPWFuAXtldkfRGlabR8oOQpyQDL2PL_E9TpzNLFaeaVF-gPL9zq9jecSE8rrcAnJNobNsUdxNyIBpbP5XAY5FW_flNFW-bfyw8hytDegWPyck9eWKSNpVKXmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از یک منبع آگاه نوشت که دور جدیدی از مذاکرات میان واشینگتن و تهران، احتمالا هفته آینده و شاید در سوئیس برگزار شود.
مقام‌های جمهوری اسلامی تاکنون در این خصوص اظهار نظری نکرده‌اند.
همزمان دونالد ترامپ، رییس‌جمهوری ایالات متحده، در تروث سوشال نوشت که با درخواست تهران برای ادامه مذاکره موافقت کرده اما به آن‌ها گفته آتش‌بس پایان یافته است.
@
VahidOOnLine
خبرگزاری فارس:
درپی انتشار اخباری از سوی العربیه و فاکس‌نیوز درباره برگزاری دور جدید مذاکرات ایران و آمریکا در هفته آینده، پیگیری‌های خبرنگار فارس از یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایرانی بیانگر این است که این ادعاها صحت ندارد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/76919" target="_blank">📅 19:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76918">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPV_dw16-jNQiHxxUHp5CJUb0GjuXhIvk5GBYUMSdnPtAenGCJJGS6cls0qXRzMxPZMA_WND4Co1bCMyRoBD5QdrDitIjmpzq636GrMkyv4oFsRw8UMZsgwzW3fs7ql62s8-gpz3y0MQxVL1-IusOOfbNTBul6N124qAE099JIeAugk1weSH-rMEROI-jHyMVoO9v-Tl9GoDqxVB4I1WugXom0LiUataYe0KOYVWPHjsD94gIRZK2erRew9xgJy6I_DzkwP7bKU-SpC8efQYgAXC23vEMsKLIDXU_1NVqd7tusKS401-9PKitnVRcFdXTt8v2ph8ydSWun_LcypxTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در گفت‌وگویی با «نیویورک‌پست» اعلام کرد که دستورات لازم را برای واکنش به هرگونه تلاش احتمالی ایران برای ترور خود صادر کرده و در صورت وقوع چنین حادثه‌ای، ایران با پاسخی ویرانگر و بی‌سابقه مواجه خواهد شد.
ترامپ اظهار داشت که مدت‌هاست در فهرست ترور تهران قرار دارد و به همین دلیل دستور داده است که اگر اتفاقی برای او بیفتد، ایالات متحده باید ایران را «به سطحی بمباران کند که هرگز پیش از آن ندیده‌اند».
او در پاسخ به گزارش‌های اخیر مبنی بر هشدار اسرائیل درباره طرح ترور جدید، با رد وجود طرحی تازه تاکید کرد که ایران سال‌هاست به دنبال حذف او بوده است. ترامپ گفت: «من از مدت‌ها قبل در صدر فهرست ترور آن‌ها بوده‌ام؛ زندگی همین است. امیدوارم دلتان برایم تنگ شود!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76918" target="_blank">📅 19:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76917">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifpcXdfSpn5qilb31HQEBaY82qWZdpB-T_LvDaIrik8BVcKoiFYXqvE5BWsozP4RrRmTwpCVx54pTJkm7nsTHpa4EJrAAasu5CwujeWSiTNrPliTtrMnJFrk6nBOBVkeJTFxNkDDS2JJF7Eu7PvjBeDD437--KwUBdk4ThTw2YfICxgnWF3x0j6KfaJgotO1YIfBAK7o6CHd5yrHMqlcnDGFndurhzg6wS-BgKf1wRz-vGVe5VBvQ7mAfdimIVWnxFPkZ5f0ByEOprIiXBfubFYhifjPvhEuIy2O4O_68QlaOKTIbp7h2pwWmMMVekWydXXBeERxu8eYbIsZoNiXfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امام جمعه اهواز گفت: فریاد ملت ایران انتقام است و از هرکسی که موشک و پهپاد دارد می‌خواهیم که زمین را از لوث وجود ترامپ پاک کند.
احمدرضا حاجتی  در خطبه‌های نماز جمعه گفت: سایه حکمرانی رهبر شهید همواره هست و آن مشت گره کرده او بر سر آمریکا فرود خواهد آمد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/76917" target="_blank">📅 18:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76916">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromﻣﺎﻧﺎ ﻧﻴﺴﺘﺎﻧﻲ Mana Neyestani</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V41U0Q1Ad_qv51Jtt4ApraDCwsqG4Q60yFhsThJLqCZSGjhEjQJdY-rHSZwVegDIbBo68H5BDvE1fqIylnNNTblI_Tb5x2FI5XtRZbC6md-UV7wRv3RYBknEGu9fd_wGJwQ44Ots7L2iztD1LkNRaVJfpbLva8gQEdXfMvYP6yWCD78s2n_ybT8CVIbyhfxHkn2i1KntkG81p1CNa9qVfSQTVWv0RwqygdtbZxLtlhQQmnRONtDIzSP6sRsI7lmCvm0r17woPxUyO_tYwWCg1miXdyatFwgK3Zte_OBlYhCbXxUMUINLZTcC0lJwC3bRddUQ0mvS5DAG6etXn6D8Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره زیر خاک رفت</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76916" target="_blank">📅 18:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76915">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DledGTAnMz9m3n2xUvtZVi_I_OyyNzst6K1iOrVNsFaYDxSRRFNIINnJlGAY-liL4cKv-3GoeSSPV_oQucMQ6t7NFJoVoqSOLEvAEE1V0XOFcp8MzkURtfma07h37qcZD0arA0obmqBNeuqL_8QLErs5r_kNSyiluSmUmHSgFYSJMDF5-2xizKvo6oUhZBveoVeMZOyL9i3UPClLg9I2j6mCSFRRZusHQI2qkaypPuKwNcrbSCUHPGIIC6VDLWuWz68k7FCA5G9dlho3En3SlrgYLXX8EQdyRVyP8i2TLbV80U-eEIsvTj5cqlwARL9JffH15kc-LNguqjZw1E-Q8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
جمهوری اسلامی ایران از ما خواسته است که «مذاکرات» را ادامه دهیم.
ما با این درخواست موافقت کرده‌ایم، اما ایالات متحده به‌صراحت و بدون هیچ ابهامی به آنها اعلام کرده است که آتش‌بس تمام شده است!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/76915" target="_blank">📅 18:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76914">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vmr6QCtouPj_TyJ2_MQfrRGyMfAjtqSTykm7hCDxhHhctI6jhUK-03MvaH_-ncAhA2poiK7JgOeY7D6MsdMusOaiy87AZWBcPgqUF6KvXNC8E13GvHyi3K6qM4nj93lpCU9VhfiQIpY-yFcFozttJS5I4nSj_6kkEGQCmfyjb2kdgYs51K-x9jZNShqh5XE5A2BBQhDrK2ZPpQRXYTy995jQ54bHFUPFmhiXbUUU10bum2r0HjFdG76LBbY-SJGi8v7vKOUNcu9nY_hxNG2uHkKq1yUhR_WZxcGdkGzA4mhSlcsTtkPRrxFz5QW81O5ZL3YYA6Cyq1ya8F0jOu4NdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت اکسیوس می‌گوید قطر، پاکستان و چند میانجی منطقه‌ای دیگر از جمله ترکیه، مصر و عربستان سعودی در تلاشند تنش میان آمریکا و ایران را کاهش دهند و مذاکرات هسته‌ای را از فروپاشی نجات دهند.
بر اساس این گزارش، با وجود آن‌که دونالد ترامپ روز ۱۷ تیرماه تفاهم‌نامه و آتش‌بس با ایران را «پایان‌یافته» اعلام کرد و دستور حملات هوایی داد، دولت او همچنان خواهان بازگشایی تنگهٔ هرمز و پرهیز از بازگشت به جنگ تمام‌عیار است.
یک منبع منطقه‌ای گفته میانجی‌ها معتقدند حملات اخیر ایران در تنگهٔ هرمز احتمالاً از سوی عناصری در داخل حکومت ایران انجام شده که با تفاهم‌نامه مخالفند و قصد تضعیف آن را دارند.
اکسیوس می‌نویسد مقام‌های میانجی روز چهارشنبه تماس‌های متعددی با مقام‌های آمریکایی و ایرانی داشته‌اند تا ابتدا بر سر کاهش تنش توافق شود و سپس تاریخی برای دور تازه مذاکرات فنی تعیین شود.
یک مقام آمریکایی نیز پس از نشست ترامپ با تیم امنیت ملی خود گفت دولت آمریکا همچنان به یافتن راه‌حل متعهد است و گفت‌وگوهای فنی برای رسیدن به توافق هسته‌ای ادامه دارد، هرچند واشینگتن حملات ایران به کشتی‌ها را «اقدامات تروریستی» و نقض عملکرد مورد انتظار در تفاهم‌نامه می‌داند.
@
VahidHeadline
خبرگزاری رویترز روز جمعه ۱۹ تیر به نقل از یک منبع آگاه اعلام کرد مذاکره‌کنندگان قطری برای دیدار با مقام‌های جمهوری اسلامی و با هدف کاهش تنش‌ها و فراهم کردن شرایط برای ادامه مذاکرات گسترده‌تر، در ایران به سر می‌برند.
بر اساس این گزارش، گفت‌وگو بین دوحه و تهران «با هماهنگی ایالات متحده» در حال انجام است.
این منبع گفت که هدف این مذاکرات، رسیدگی به اجرای تفاهم‌نامه میان آمریکا و ایران و همچنین موضوعاتی است که موجب تشدید اخیر تنش‌ها میان واشینگتن و تهران شده‌اند؛ از جمله اختلاف‌ها بر سر کشتیرانی در تنگه هرمز.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/76914" target="_blank">📅 17:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76912">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/unJTygOm4FS3fS4GbtMkjgTJjopjQkPtC3m_aFQmfjBRuL1GOF-TWzLu5a_Ujuu0Ml2vIMFmihdO-HscclRYI4TV58hUV4gg0jTOxx1zvTK9twyiEhtYjFUvrgYlCHebZfIGjd9x5bwegSb8YkhwTTrlUXA2tmRx75kwmfICFWitEXXw8K6QfHQz3yxDW8Gbi1EIzVZILwoHbF_xZ_kaT7HAx2mOGzRXv8SAbbPIlxO7QgR6mLo3eVpNcRLXqCFGBCgPBOGC4YZhWw6T--n9m_MHnwJizQrsrOofoxkKDcrNu0CuwmEAMnKfe5gTW9vZfHt6vpzoi1NCpomR0neT1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ik1JScTibBP17DAYgPd7NsaHCFIcIhuzc6mRbNppi3e8uviehvNk48SjzmTbRqDCX6DbiLtilI-V_SvOf1G8gn9pHx9pOLuD63BBK1WxTfqS2pkCTS4-IXSBH6gi7aPGAanDaEOgUJGjqES-R46th00gH46YwZ_1aim9xAg7XB-WxECb1F38ZXiHFbpM-YYNYoEVYgj6h1e5euD3igP0llv7aF7IVtZmc2e33fSs_ajDzyhGEeDGyFh4IkJ5FISEbDPAPydsRLlgFofCEixevG-31154eYUv2clcq7Uw4skUsdxqvW94sLmeQi0pABT5X8V5BkBjfqhurLE6qY1pOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به گزارش منابع حقوق بشری، نیروهای مرزبانی جمهوری اسلامی ایران با شلیک مستقیم به خودروی یک خانواده در روستای درکی از توابع شهرستان سروآباد، یک کودک ۱۵ ساله را کشتند و پدر او را به شدت مجروح کردند.
به گزارش هه‌نگاو، غروب پنج‌شنبه ۱۸ تیر ۱۴۰۵ (۹ ژوئیه ۲۰۲۶)، نیروهای هنگ مرزی مستقر در روستای درکی، بدون هیچ‌گونه اخطار قبلی، خودروی شخصی یک خانواده اهل این روستا را که پس از پایان کار روزانه در باغ گیلاس خود در حال بازگشت به محل سکونتشان بودند، هدف شلیک مستقیم قرار دادند.
هه‌نگاو گزارش داد که در نتیجه این تیراندازی، سام حسنی، کودک ۱۵ ساله، بر اثر اصابت گلوله به سر در دم جان باخت و پدرش، احسن حسنی، از ناحیه ران به شدت مجروح شد. به گفته این نهاد، پیکر سام حسنی به سردخانه بیمارستان بوعلی مریوان منتقل شده و احسن حسنی نیز در همین بیمارستان تحت درمان است.
شبکه حقوق بشر کردستان نیز با تأیید این رویداد از تشدید فضای امنیتی در مناطق مرزی مریوان، پاوه، بانه و سردشت خبر داده و به نقل از منابع محلی نوشته است که نیروهای مرزبانی و سپاه پاسداران در برخی از این مناطق، ضمن افزایش حضور نظامی، محدودیت‌های بیشتری بر رفت‌وآمد روستاییان اعمال کرده و در مواردی از دسترسی ساکنان به باغ‌ها و مراتع شخصی‌شان جلوگیری کرده‌اند.
تیراندازی نیروهای نظامی جمهوری اسلامی به سوی غیرنظامیان، در سال‌های اخیر بارها به کشته و زخمی شدن شهروندان، از جمله کودکان، منجر شده است. کیان پیرفلک، کودک ۹ ساله اهل ایذه، در حالی که شامگاه ۲۵ آبان ۱۴۰۱ همراه با خانواده‌اش در ماشین در حال گذر از خیابانی در این شهر استان خوزستان بود، هدف شلیک نیروهای جمهوری اسلامی قرار گرفت و کشته شد. در این واقعه پدر او میثم پیرفلک نیز به‌شدت زخمی شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/76912" target="_blank">📅 17:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76911">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FxWT_7bEv70et9_Osa1T3tLB-OmnGDteYL-NZYoKlfsBb56Pzdy8tn0TX4AW8ushtL3ffd0J1waRr0toLo_GQSg_IU3ZIMCzq37j8LMVdNjC-wJHAnjSvw8U1DbvYp9sL0bzRGhH30i6ymou2H3fPVrPd_bGk59kpMzzxjXWvPyYZ1pZ7PLp1i5Hzssbx1mzaehxteZCLcZ44RbGDPEOQv3DTq9X3LXfaG4JqISFD6lFztiEfXpilPkY9ygP_UorYFMKO7P3k82ow1FoK7J5CUXjqKXMg1ZNqoCgFG4pRXtk7jiRaKt49nSTTYMX7OrPxfb5jWmhwK_HyAzxyCvVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از دو منبع آگاه گزارش داد اسرائیل این هفته اطلاعاتی را در اختیار آمریکا قرار داده که نشان می‌دهد جمهوری اسلامی به‌تازگی طرح مشخصی برای ترور دونالد ترامپ تهیه کرده است؛ گزارشی که هم‌زمان با تشدید تنش‌ها میان تهران و واشینگتن منتشر شده است.
به گزارش سی‌ان‌ان، یکی از منابع آگاه گفته است هشدار اسرائیل در هفته جاری به مقام‌های آمریکایی منتقل شده است. منبع دیگری نیز گفته نهادهای اطلاعاتی آمریکا در هفته‌های اخیر به‌طور مداوم اطلاعاتی درباره احتمال تلاش برای ترور ترامپ دریافت کرده بودند، اما اطلاعات ارائه‌شده از سوی اسرائیل جدید بوده و به یک طرح مشخص مربوط می‌شده است.
سی‌ان‌ان نوشت جزئیات این طرح هنوز روشن نیست و همچنین مشخص نشده که آیا دستگاه‌های اطلاعاتی آمریکا نیز به‌طور مستقل این طرح را شناسایی کرده بودند یا تنها از طریق هشدار اسرائیل از آن مطلع شده‌اند.
کاخ سفید در پاسخ به درخواست این شبکه برای اظهار نظر درباره این گزارش، که نخستین بار روزنامه وال‌استریت ژورنال منتشر کرده بود، به اظهارات اخیر دونالد ترامپ اشاره کرد.
ترامپ روز چهارشنبه ۱۷ تیر به خبرنگاران گفت: «آنها می‌خواهند رهبر آمریکا، یعنی من، را از میان بردارند. من در همه فهرست‌های آنها هستم. امروز صبح دیدم که در تک‌تک فهرست‌هایشان قرار دارم. تا اینجا کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی خیلی دوام نیاورد. اینها آدم‌های شرور و بیماری هستند و باید این سرطان را ریشه‌کن کنیم. سرطان را باید از همان ابتدا از بدن خارج کرد.»
سی‌ان‌ان همچنین گزارش داد تنش‌ها میان آمریکا و جمهوری اسلامی در روزهای اخیر، هم‌زمان با فروپاشی آتش‌بس ۶۰ روزه، افزایش یافته و دو طرف تهدیدها و حملات متقابلی را علیه یکدیگر انجام داده‌اند. با این حال، به گفته یک مقام آمریکایی، تلاش‌های دیپلماتیک همچنان پشت پرده ادامه دارد.
به گفته چند مقام آمریکایی، برای انجام حملات احتمالی در شامگاه پنج‌شنبه آماده‌سازی‌هایی انجام شده بود، اما مقام‌های آمریکایی در نهایت ترجیح دادند فعلاً به جای اقدام نظامی، مسیر دیپلماسی را دنبال کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 490K · <a href="https://t.me/VahidOnline/76911" target="_blank">📅 02:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76910">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCgJqubr0rxHsB6iGPAQDF_xn6Ilxk2hFjki0SLoFbPS_KdaOQ8j1gzUAFfuljFWL2_mHVXAxiBn0PEgkY4NwBO2HctUE3CK8gJrN0RohCeDXWGR0_c8PWwGvryCD8u32TSpaATWRnPtbRqVHTXGZ38DtavIw5fftqyssD7T18APystTT7VBVryCEckLKXd9i740E28eF7PONf7IwS4t-fN9oVVDLEh63-tTQZEt5Ckog0fy1m9q3XJEibBm_KbbOx2GNTiC7zmBoXsqghY-771HheXbahXbFBoxjcGFwz-yp03Dwrw1GZ1x9VtmlBypxUNMaIO2zjSVB-rjuoqwbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی،  پس از ۱۳۱ روز بالاخره در بامداد جمعه ۱۹ تیر در حرم امام هشتم شیعیان دفن شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 485K · <a href="https://t.me/VahidOnline/76910" target="_blank">📅 01:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76907">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bdeuJFPsFDEJcOCJY47gusH0kQfJWPDbQPlBd5VLpPd5OYznH3lwUAWD_ndgGfYSvFwBGeq_CSPnVbk57e44XHzQp3gCfG2vzCkLzCl_JVrPreF4W_e_dRPBzz-a3tw30gtQ-2q0HwvjfaCKiS835PjG_u1RpNq9MaVWUO4_vCuIqNNbcZ6Cl1GYtCdUJFbjs8mCX_lJXGYWRi9gtS_3FP6Oez4eH6MXG1wd-MX-B38ZBZseE6GF2QeQXDe6zREFr9l9ZwY12HYaGERtx09Ga7EOXNjp1cdU5mDir6-P-BUsC71HCWDtDCW-S3DqegVik6P0aYisn6R6ezLDeWxoHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KsdU5RLdc2qdIISP4GkLJ_8k_vKXWDyN8oVGoVLkgi9R9d17frpfRLI4GfvCy3FLUDbwXMjqwsW0vNuMLNX-vpgZKvU7z1pwK_aZCf4Ux-oJTHnWcFK0NWv-tjPSxLsx65WiG_ZcySJoR-y014yiqtbf9_vwbevPtLXoxaksGQAc8LESbwa8pQxtTNkO5qiiZO6zA6GZyzlyya4G9t7G_Ql9fSCXoOCRHc0z60Zf9TXDhGAosAAkSxJVMNNsfsTo7E0E3LgCKvLzCt5si0sa9lbux-1vCvszYQH0HWENULBdb_Oyk3rA_h0xlaPVGpcMaXWMSOUbLU3WPGbTqjDcIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aUSBX32zSv_IEuQ1RnacEgEr407nTVswKAIsRecCSKEy3s4Bp32PyPK0zfwZ9fEw05IHTPc1uLaEvr6gmfcP2P1bIImwQ0NqtlHt6NAdwf1VB8cIrqP_SprjIF_i3iR4fBJlrQjT6fmNHaAE7SUW6E5lff8Y8gmKc6m4E_Pw5ib1KoRAqW3l2Gq3GVU8DgWsK6M415kuVp-0hhGdm2H-Nsl7rzNIc0R7VVHr5ZUWAfbJd9-SmsL23tfUEvVJkMvJNcMgipj4wK9GHTF_v2hvQ_rMdTRGP7UytPlKTsMradCJ0iiEvq2veAxUNul9_p3MPfg6RbZKx-6cHZaTMY1ldw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به گزارش خبرگزاری جمهوری اسلامی، ایرنا، معاون امنیتی استاندار خراسان رضوی وقوع تیراندازی در منطقه بلوار سرافرازان در غرب مشهد و کشته شدن دو نفر را تایید کرده است.
ایرنا گزارش کرده که امیرالله شمقدری گفته است این رویداد تروریستی نبوده و انگیزه اصلی وقوع این درگیری در دست بررسی است.
معاون امنیتی استاندار خراسان رضوی به ایرنا گفته است: «براساس بررسی‌های اولیه ابتدا ۲ نفر با انگیزه شخصی با هم درگیر شده‌اند که یک نفر از آنها کشته می‌شود و با دخالت نفر سوم، نفر دوم نیز جان می‌بازد، هر دو نفر با سلاح گرم کشته شده‌اند.»
آقای شمقدری تاکید کرده است که حادثه در منطقه سرافرازان مشهد روی داده است.
او وقوع هر گونه حادثه تیراندازی و یا رخداد امنیتی در محدوده بافت مرکزی مشهد و اطراف حرم امام رضا در روز پنجشنبه را تکذیب کرده است.
ایرنا اضافه کرده که بلوار سرافرازان که تیراندازی در آن رخ داده، در غرب مشهد واقع شده است و حدود ۱۷ کیلومتر تا حرم فاصله دارد.
@
VahidHeadline
تصاویر هم در همون منابع غیررسمی که پیش‌تر این خبر رو اعلام کرده بودند منتشر شده بود. از درستی‌شون اطلاع ندارم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 515K · <a href="https://t.me/VahidOnline/76907" target="_blank">📅 00:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76906">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFKOos9X67HLSMd83AuLbwE_pnGoSUvkq50nveYQ-M-HfzygbJI3hzCOj3ValYt3-vsQCq9_Gg79YLCyOh9_UU7liCzKyqs-jHpcxcV9aKaFJItYP4nN_t6E760_jSSRZlHHh0yludXvauY0oQ95IgRcKlWUuJCO4n7dROhGN3R6xoekz3WWoD4JDyTb1qnJvDWbZcjOR-Y838hBrEjr78v8YfQwPqJsMCBQ3UH7G1dwvrcm4NhVDPVY48B3viHxO2QmcGJs7SHFomzUo3RcwG62d4-poWjHnY7RhGJhOdF-S3ua9WNJtBcxmKe3aJV-F_U2XiA2jW4__v8S5v-pTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
فرماندار کنارک اعلام کرد یک منطقه نظامی متعلق به نیروی دریایی در این شهرستان شامگاه پنجشنبه در دو مرحله هدف حمله قرار گرفته است.
🔸
محمدیونس حقانی به خبرگزاری ایرنا گفت این حمله توسط «جنگنده‌های دشمن» انجام شده و نیروهای امدادی، امنیتی و دستگاه‌های مسئول در حال بررسی ابعاد حادثه هستند.
🔸
ساعاتی پیش از این نیز معاون سیاسی و امنیتی استاندار بوشهر از حمله به یک مقر نظامی در حاشیه شهر بوشهر خبر داده و گفته بود صدای انفجار شنیده‌شده در این شهر ناشی از فعالیت پدافند هوایی بوده است.
🔸
این در حالی است که صداوسیمای جمهوری اسلامی پیش‌تر گزارش‌های مربوط به وقوع انفجار در شهرهای جنوب ایران را رد کرده و اعلام کرده بود «تاکنون هیچ انفجاری در جنوب کشور رخ نداده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 475K · <a href="https://t.me/VahidOnline/76906" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76905">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zqq5bM-sdlIoTjsn-Y_rsOdKcwDBIWc3nX1RqIxxumZiKYUQR1UFC63-mcDq_yT9TOFdcqKldH0n2dKN88GPrPZCgjq3zm0-ZOToAYOoYSsXQi36OSsRkoE1hzmiDZTmiEUUdzpohLFfMdYE6MGP1sKB9iDkqvKus8fvl3YAa_E_OIu5dY_z-G9vFmTovTItBY-CU4lJ_KX1qUDHYcxsf2xxAWrrOo2Q4u_lCofQRYizAshx5DqeJC4_-dNxvlgiGqfbfjpkJQpqSa5usiN43ITKNjg7GyYJeA03kB5v5EbT892_DHg1N5QpVzsUSvT1MLYW7bIy6P2FsWEcnAVB4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ایرنا به زبان فارسی سخت تیتری درباره صدای فعالیت پدافند نوشتند، می‌ری توی متن خبر می‌بینی نوشته:
"لحظاتی قبل یک مقر نظامی در حاشیه شهر بوشهر مورد تجاوز و اصابت پرتابه دشمن آمریکایی- صهیونی قرار گرفت."
irna
به نظر می‌رسه از روی صدای انفجار برخورد پرتابه، مدعی تشخیص کشور پرتاب‌کننده هم شدند.
احسان جهانیان، معاون سیاسی و امنیتی استاندار بوشهر، شامگاه پنج‌شنبه اعلام کرد یک مقر نظامی در حاشیه شهر بوشهر مورد اصابت پرتابه قرار گرفته است.
همزمان صداوسیمای جمهوری اسلامی خبر داد تا این لحظه هیچ انفجاری در بندرعباس، قشم، سیریک و جاسک گزارش نشده است.
پیش‌تر رسانه‌های ایران از شنیده‌شدن صدای انفجار در شهرهایی از جمله بندرعباس، بوشهر، اهواز، کنارک و چغادک خبر داده بودند.
یک مقام آمریکایی شامگاه پنج‌شنبه به سی‌ان‌ان گفت: «ارتش آمریکا در حال حاضر حمله‌ای انجام نمی‌دهد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 463K · <a href="https://t.me/VahidOnline/76905" target="_blank">📅 23:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76904">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UVkhn3xF9K4hXgsGPpVACZjGP8lLH8A9I_qVCSfMv6iqIc2E6Egg-HS4ZcTonF3bRH_8YsCOxEur7Y69sPlyNIq0BBzUfhl_slt7B5kcQ7aV1CXMYFExEteLQzPtNleTVLC3Tb24LX2_KzVAffdVal_g9mQ48FC45bOzldK17ON1S0I_GvgPAAhJxerMPDc5g6ZAJKSb2o8iZCFnDuy-lx9QQRi89KBJXNa05O0XGBUVCHCGXAwS31MfsTuWdj3d3RUKZXI-fdtvx2u1rfHsfblC5yUZOBPsF6bycrQOeSQZq5AmFIM5Xk1hKQtI_kSHpCZ3eKjlSlBqEAPaxG6DjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی شامگاه پنج‌شنبه به سی‌ان‌ان گفت: «ارتش آمریکا در حال حاضر حمله‌ای انجام نمی‌دهد.»
پیش‌تر رسانه‌های ایران از شنیده‌شدن صدای انفجار در شهرهایی از جمله بندرعباس، بوشهر، اهواز، کنارک و چغادک خبر داده بودند.
همزمان آتش‌نشانی اهواز اعلام کرد انفجار شامگاه پنج‌شنبه ناشی از «نشت گاز» در یک ساختمان مسکونی در منطقه حصیرآباد بوده است.
@
VahidOOnLine
صدا و سیما بعد از تکذیب آمریکا:
برخلاف برخی خبرهای منتشر شده در  فضای مجازی، تا این لحظه هیچ انفجاری در بندرعباس، قشم، سیریک و جاسک گزارش نشده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 449K · <a href="https://t.me/VahidOnline/76904" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76903">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EuMP7ANWPhGU7BuStWsZOj517CI1AoS2lDkFB7fl8VUwlT0eKjCmpDIVJe4-N03XXuCs1ij8wOv_RMuAfuR57kfsC-PMyzW7-XT4TYQ9YLm_YJ73gC9ZMHCgdD69j0GbcA1Ur3UdfdrCBjAeSm5n0gSXhT1OQ3ZN08cqbzASGgxi1YhyjhvX5mj0QfohNZu11y1eb4BQ9FXh7aZSSBS1Lzup8zyhxM6e6fqgAG_AJMKHFOj_P-vLK44AJ8WUXb0rQinU1A7kThWbvX4NPr54PrgjzKfsPEQxmfQlpPOAAbrbJl_zFJNz9j3dLOndx44JDQcHM7vm03imgIF2ZWXPjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر صدا و سیمای جمهوری اسلامی ایران نشان می‌دهد که اقامه نماز میت علی خامنه‌ای، رهبر سابق جمهوری اسلامی، توسط مصطفی خامنه‌ای، پسر ارشد او، برگزار شده است.
پیشتر تلویزیون دولتی ایران اعلام کرده بود که مراسم تشییع علی خامنه‌ای، در مشهد با نماز میت به امامت آیت‌الله حسین نوری همدانی، به پایان خواهد رسید. دلیلی برای عدم حضور آقای نوری همدانی اعلام نشد.
خواندن نماز میت از سوی پس بزرگ علی خامنه‌ای، بار دیگر نبود مجتبی خامنه‌ای را در مراسم تشییع پدرش مطرح می‌کند.
مجتبی خامنه‌ای از زمان انتخاب به جانشینی پدرش، نه تنها در انظار عمومی ظاهر نشده بلکه پیام صوتی هم از او منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 455K · <a href="https://t.me/VahidOnline/76903" target="_blank">📅 22:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76902">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IvE7QJ81v67GdgCa-K2NJNZa1tWoWA99N9Z3lJWmr4ZUgMjnWfUqi9CrGyxwn-pv2juRAL_m76YAlMFp_oqGKKC34m1O-36X9emhOyjbmJM__NpXX03pUCRu0znTxYpUW5hQBrcNfYl4-gyTsVYBpeiFIW4EpiMvPvLVAxjMbKa5VbffBG_BRfKv6qySCIG5mpyJXOLGByRdKqJZfEM5q9JlHY1a77R2zSKD-sh6k_j0zZ8oPWH0l5zeey1e4VXSpEmWn3MrzenCqbJ1YNlTFiJLsIRe4hU16RHo27LUFh41ax0tErzQG2kxZTJ5mDVHgV72P9f8RXPo-RrbLMLsKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر شامگاه پنج‌شنبه از شنیده‌شدن سه انفجار در کنارک استان سیستان و بلوچستان، خبر داد و نوشت: «از جزئیات و میزان خسارات احتمالی هنوز اطلاعاتی در دست نیست.»
خبرگزاری مهر افزود صدای دو انفجار در اطراف بوشهر و در نزدیکی شهر چغادک شنیده شده است.
@
VahidOOnLine
من از چابهار گزارش از فعالیت پدافند داشتم ولی از کنارک نه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 436K · <a href="https://t.me/VahidOnline/76902" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76901">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axphtInK5Nx_xuknjBbehGk6zvbICRaXEEJCoB-o8nE3vRk1L_9cP-oGmZDDRk3iDnJ0aSp28XtW_UEayhUwCIl8UWVHzBdGTuJ8IkP3QNoksfxP8SRg_OHEePAjS6Ybn7Efe0pctY5LHvXEvKTf6CDRTS3RDfBje21yB9H6lcUco_pOkTVGX8XCxLYubq7m3tB_0i_RbuqYoWML_TVMYWh8nb-7KjdYSq_zuGer8Op-BNp8IYSxOSqgJN2brAXwO4twpApnmibkJZbVx-WKLOftelR-p9TuRQX07chzoo5fkVWVthoO_hgrRkhQNln8I_aaiIVfscRvR6rYUX4c3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری بلومبرگ روز پنج‌شنبه خبر داد که عمان رسما مخالفت خود با دریافت عوارض بابت عبور و مرور از تنگه هرمز را به سازمان ملل اعلام کرده است.
از آغاز جنگ تاکنون حکومت ایران بارها تأکید کرده است که مدیریت تنگه هرمز درنهایت با دو کشور ایران و عمان در شمال و جنوب این آبراه خواهد بود و آنها درباره نحوه مدیریت و دریافت هزینه عبور و مرور تصمیم خواهند گرفت.
حال عمان به سازمان زیرمجموعه سازمان ملل یعنی سازمان جهانی دریانوردی اعلام کرده است که با دریافت هزینه در تنگه هرمز مخالف است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/76901" target="_blank">📅 20:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76899">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FwQeQBb7bE7uTczphQXOHQrZ0LKyQvW_S35p6dzfZldUHYYuuYZj3NceXzP-8Pl4I-px7a1nTuGWBrwTmKHRs52THV8XMqDHNcuOJTJZuIPKfErgESe24OdxS4EWxrZIvReqx8mcNNr0PNXQnYlE4vapLAZr5RK8hxUIouCCKoH79Eizui_3BxECwtg67zeTjxXWSraI7BiiIJOuEijrv5HuX1h9qvjKkeSYwe4ftGIRjHdQNwQRBApWfT-7rPn20Op4MR9i0RXgoMI6Dg-LCKvgMBn9U_fMWM_8qgurvzirJVHrMBNzt1LIoJ4gr5aJtKCjhEoKTfniE8O3SWic8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZA9wesTwkeIXV-dtbWtelUnBJ3nb4XkuIoUB3_1rpt20zBCuD-jD7irYG9Bu5pC178b94wJaooaFJrv9Y3tDY-kLg5K3o6e_TxbnZgOQRLdQPSKUq997Hd01oROE4X6rJtWr_E0RFNuyeSvXBWmsgxG0FDtL7wSa0onsSgX3g3t0yRpIEKVKBMmuLCwOupLgAbxXuSehsFvKMt3xp8QxeDhdZpkFN8t9C_sIgTHM-_9R8sGIwn7NuWyaA3FZEi-elmyv4zWYAXijmjJFccqHJGR9UJUOb-YJuQP4DZwXS7dnfoaMPbXobyHUx4RYU1ZxXJuA4-44hsyZ9kkKQdNRiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیویورک‌تایمز به نقل از فرماندهی مرکزی ایالات متحده (سنتکام)، نیروهای آمریکایی در طول دو روز گذشته بیش از ۱۷۰ هدف نظامی را در امتداد سواحل ایران در نزدیکی تنگه هرمز هدف قرار داده‌اند. این اهداف شامل سامانه‌های پدافند هوایی، انبارهای پهپاد و موشک، قایق‌های تندروی نظامی و زیرساخت‌های لجستیکی بوده است.
سنتکام اعلام کرد که هدف از این عملیات، کاهش توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز بوده است. این روزنامه آمریکایی افزود که تعداد این حملات، حدود ۱۴ برابر تعداد اهدافی است که واشنگتن در آخرین دور تشدید تنش‌ها در ماه ژوئن مورد اصابت قرار داده بود.
@
VahidOOnLine
سپاه پاسداران انقلاب اسلامی روز پنجشنبه ۱۸ تیر اعلام کرد که حملات نظامی ایالات متحده نه‌تنها «پاسخ کوبنده» ایران را در پی خواهد داشت، بلکه ترافیک دریایی حیاتی در تنگه هرمز را نیز با اختلال مواجه می‌کند.
سپاه در بیانیه‌ای اعلام کرد که تردد دریایی به ۵۰ درصد سطح پیش از جنگ بازگشته بود، اما «ماجراجویی و دخالت‌های» واشنگتن در تعیین مسیرهای تردد، عامل اختلالات فعلی است. با این‌وجود سپاه مدعی است که جمهوری اسلامی در تلاش است ظرفیت عبور شناورهایی که مطابق با «ضوابط امنیتی» از سپاه «کسب مجوز» کنند را افزایش دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 437K · <a href="https://t.me/VahidOnline/76899" target="_blank">📅 17:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76894">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QiyiP9ElwVBjNgLnqyAve-2QPVMKx3ga_OLAQug5iXbSOg6KsUT9VjjVVqtQon0f_ixRfsSZNJS-saz_6DgqiSnCwP-Btc4XGmO7aJifd855c4h36i7YJEIQ8rhEaT0G1Y1QNmucuBrq4CKrUpy7ng6EGVILlzG07tzzEwjraBH_kXxlaU3jMKXQ3J5uoBLnejbh0Yjs549QGPatAnxnjUMXCNhgI9qSowEwS9t46uLr-hFuhK2ibPpFgs1pqdN9shhrClmGq2H-R2Zw9M28LLMKrfPe_aofTri7vCu1uwXT5uPrTEaoWKm19vdEcEFqawZGTIE6qbFgr1L4yD9YXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MYn7Tad2LM4z0BMJMXo6CFfSEpAnpu1A0O2-J1ds9aJb8iS8z3bDUsMe6Ps99XzykV_P0L_qEIXdFWEn8s3akGMvxf8KM2BC4ErlNFECYb3dPo5UNkyx71-a83HPBILyGGXJkxvBCtazHigy0dtoh877zJ2VThIkFtMa8N8xcjNHrpNZ2fSy_3JYhHgaD73VU1PcMDicea8FUQpzc0Ty5eOlKBfAJSOS1qqXOOvCi8dQ9qW8oHn3cWLHTKS6NDuhQnsUkA-gDr01vWr4OAqtXLlfbcSabuCqvsNg4fpN0eAg9eaxGn5lmp1fKEn4VuFnZE_hG6kq_p0oyk7WVwKNcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pEssGy3xc9aYC3DVjBkEn9Rudk88xlyWQ7QwWn6x5U3swMnUGj5BUOQPA5FTzHeaw6rTOStq45F6lNYqrvDhuXxVqOxUEoz-2lq2w3KleSDwHfrvriCRDbSWZ_Q9HimXDsQ7nzP8XoWCbp0euai868h1vmaShiLfzcc0S28p_N8HWYHzzQzQTk5rDVXSBtGtv3yfFG3JKg78d1qkawLHb16O50Lng5v3FTP-QyHjBqVJhQFPmJGD6lRFT7ebmRb3Lr37zmktFLH1l23wXqEIgi3doIdd26YrpGKnSBNIkqQ70UzM-LDMjYTtYs6BX_q6az88hPJIdCTG7A_nor0xsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/687c7e5359.mp4?token=pKyHyVOXUPTP_FV8cFPoQPC3I0bXyKPzIyUnKrb0lBAJ1PFi9i4IsEzPlK6VYbqevT3AT5St-Rzt-MkFXwDIPTrRWdIXJDVwumdlPb7_kyfL33fkGmg4snTWCsT-2VcSaB7gwELBzPTpqqAo_Wv3KwsJxk9Lv4yhUmV5uowvqzCZeIHq9C3J0DaguQoehjHbPYLW9hRbVViwbyv5JUF2NiqVzl62XshZflPy57-g8Ip5Vw2dvZp-tfXYmZYY9QFvQ_GRwQdxlSZZ9V-AYqSwICL3NMEaQBfXmOThBYstEw6tLVEqHISSBlpKgfDS6KwpQeF92SLi11r1opO0RXdfLw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/687c7e5359.mp4?token=pKyHyVOXUPTP_FV8cFPoQPC3I0bXyKPzIyUnKrb0lBAJ1PFi9i4IsEzPlK6VYbqevT3AT5St-Rzt-MkFXwDIPTrRWdIXJDVwumdlPb7_kyfL33fkGmg4snTWCsT-2VcSaB7gwELBzPTpqqAo_Wv3KwsJxk9Lv4yhUmV5uowvqzCZeIHq9C3J0DaguQoehjHbPYLW9hRbVViwbyv5JUF2NiqVzl62XshZflPy57-g8Ip5Vw2dvZp-tfXYmZYY9QFvQ_GRwQdxlSZZ9V-AYqSwICL3NMEaQBfXmOThBYstEw6tLVEqHISSBlpKgfDS6KwpQeF92SLi11r1opO0RXdfLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌زمان با ادامه درگیری‌های نظامی میان جمهوری اسلامی و ایالات متحده، روز پنج‌شنبه ۱۸ تیر نیز حملات متقابل دو طرف ادامه یافت؛ حملاتی که از جنوب ایران تا عراق، کویت و آسمان اردن را دربر گرفت.
رسانه‌های داخلی ایران از شنیده شدن چندین انفجار در استان بوشهر خبر دادند.
خبرگزاری فارس گزارش داد که صبح پنج‌شنبه مناطقی در استان بوشهر هدف حملات آمریکا قرار گرفته‌اند.
معاون سیاسی استانداری بوشهر نیز به خبرگزاری ایرنا گفت چند نقطه در این استان، از جمله حریم پیرامونی نیروگاه اتمی بوشهر، هدف پرتابه‌های آمریکا قرار گرفته است.
ساعاتی بعد، صداوسیمای جمهوری اسلامی به نقل از منابع محلی از شنیده شدن صدای چند انفجار در شهر چغادک، در نزدیکی بوشهر، خبر داد.
در همین حال، فرماندار عسلویه اعلام کرد بر اثر اصابت دو پرتابه به اسکله صیادی بنود، ۱۰ قایق صیادی دچار آتش‌سوزی شده‌اند. گزارشی درباره تلفات احتمالی این حمله منتشر نشده است.
هم‌زمان، رسانه‌های عراقی از به صدا درآمدن آژیر خطر در پایگاه نظامی «حریر» محل استقرار نیروهای آمریکایی در استان اربیل خبر دادند. همچنین گزارش‌هایی از فعال شدن آژیر‌های هشدار در پایگاه «ویکتوری» آمریکا در بغداد منتشر شده است.
در کویت نیز رسانه‌های محلی از وقوع انفجار در نزدیکی پایگاه هوایی «علی السالم» و منطقه بندری این کشور خبر دادند. وزارت دفاع کویت اعلام کرد در حملات تازه جمهوری اسلامی، دست‌کم یک نفر زخمی شده و وضعیت او پایدار است.
هم‌زمان، سامانه‌های هشدار در اردن از مشاهده چند موشک، پهپاد یا راکت در حریم هوایی این کشور خبر دادند و از شهروندان خواسته شد برای حفظ ایمنی، در پناهگاه‌ها یا داخل ساختمان‌ها بمانند و دستورالعمل‌های مقام‌های محلی را دنبال کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/76894" target="_blank">📅 17:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76893">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LHRs-ky0kiPH7VzLjIQAi2o1R6H34__Bq9iA_jvWjjs4n5WfsaK0UixDN1fessmj6AkyxMcKQ8wegTfHB_J3egjD3F4rxfT_YW0EzB9BNGdvjDU0kZkUok9--osp9b9S9Sby0zIlA98ASCVn9kFNPT5c9PTjHnBrDlmQ21nZ_QjkX6VnnlSOfexEQEJSncwBtA3m_bNdT8iC28BO6HT6uGsxPL-FjWgX8LCKvcwyrBjed1gTd9718Zr_pQANSG38Kvk4iPVcWUUuEmJPsYZS6vdTNKt7_edaMe6OEj6Yn1wxyh4LrwJmFGcTE4DczExZgKeUMXOdhcn7RPb6SCOl3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهران رئوف، زندانی سیاسی، فعال کارگری و شهروند دوتابعیتی ایرانی-بریتانیایی که در آستانه ۷۰ سالگی قرار دارد، عصر چهارشنبه پس از حدود شش سال حبس، با پابند الکترونیکی از زندان اوین آزاد شد.
این فعال کارگری در شرایطی آزاد شد که همچنان مشمول محدودیت‌های ناشی از اجرای پابند الکترونیکی است و وکیل و خانواده‌اش ابراز امیدواری کرده‌اند با توجه به شرایط سنی و جسمانی او، زمینه آزادی کامل از طریق استفاده از ظرفیت‌های قانونی، از جمله آزادی مشروط، فراهم شود.
مهران رئوف در مهرماه ۱۳۹۹ همراه با ناهید تقوی و شماری دیگر از فعالان مدنی و سیاسی بازداشت شد. با آزادی یا پایان محکومیت سایر متهمان این پرونده، او آخرین زندانی باقی‌مانده از این پرونده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/76893" target="_blank">📅 17:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76891">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gwtLNjiyoZ3bVpHKrJZeFk6x2zE70_EJrYr57fwveBsvmSUQME4q9Vd1Wvt_DCudgu2CDBSB4WxWiFtLoyt51gtcP6IqIph-uJnvyR7d4KDAeowUelL_G3ztr6wJZr6lURtBQ2hOOxrYVZk2yaeiv10Y_N-0R8J2OHF4No1dciB1C9t5guYd0ePT9Q5ENL8pzYprxiGZeNoOId_mG2jBvqFzEuwq5REVrjJL-W7m2V4x8--u8TX2NZEHAhFALYp0LIZ9QooYEwY46xZjWek9Fj-GWw8k1e_RdcYvLDo1wUMt3G5TsXjuFMX6diUHlWUFaRrQzcJHFNfp9yQyvAkNag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dQv-i8-wkGfE2SBpgom7TCyObBXzlAVW4VG8wmSsZIeITtvq6PaHZrNlz3H1ayuza3XsvGXxcl8rCp3SYA3xljZXojdNhanRpLR-nzY_MF_nPSa9zyEY77LivdVXaNt_NsCPVlnmzHQVLSRR7s21QyrcJY7nA-gYsAIH3frBGH4XxhjIX_PWhrsSewqvW6f22Ttuj_Bq_HXLtxtQjE2DM95FoID9pwcxfd4YkJ1DZDvSIJtgFxbCa7XpmLSEMjvHg6JU8nSYi9u_VO3JPv70T920ttOlP6HUXrwpGhxw_nWcUrv7T33IV-br0fMx-1s1e-ERkR7kYyLSJGKOq4OOCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری بلومبرگ روز پنجشنبه خبر داد که رفت‌وآمد کشتی‌ها در تنگهٔ هرمز پس از دور تازهٔ حملات آمریکا و ایران به مواضع یکدیگر، تقریباً متوقف شده است.
بر اساس این گزارش، داده‌های ردیابی کشتی‌ها نشان می‌دهد حرکت‌های قابل مشاهده در این گذرگاه حیاتی انرژی جهان عمدتاً در مسیری انجام شده که مورد تأیید ایران و نزدیک‌تر به بخش شمالی آبراه است، در حالی که کریدور مورد حمایت آمریکا و عمان عملاً بدون تردد بوده است.
@
VahidHeadline
راه‌آهن جمهوری اسلامی می‌گوید بر اثر حملات آمریکا به «یکی از ‌نقاط مسیر ریلی تهران–مشهد»، حرکت قطارهای مسافری در این مسیر متوقف شده است.
در بیانیه راه‌آهن به محل دقیق هدف قرار گرفته، اشاره نشده اما آمده که تیم‌های فنی و عملیاتی به محل اعزام شده و «عملیات بازسازی محل آسیب‌دیده در دست اقدام است».
توقف قطارها در مسیر تهران–مشهد ساعاتی پیش از برگزاری مراسم تشییع جنازه علی خامنه‌ای در مشهد رخ می‌دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 486K · <a href="https://t.me/VahidOnline/76891" target="_blank">📅 10:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76890">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86782c7f01.mp4?token=ZBHJHcqdxjssuGySRsDB1By7QPI_g3sGu2e7ScM0YTclHmrkpd50NTHsIz7O9kdQuSnpqUdM3rgYCs5xV7uJeus2HPJCcjrTCSvCTXNodpVOkHktuijMPWYyIGq8AIV0K-1TsPq38Po-MXRvuVRRvVDJG3Q6UrbVGHLfQ68gX9htymIyHxmOOT8o-K1-JutZATxT623PLPoCVLyIY_m1Qdwyee5uq7fr1gfBjOelcq43hGZEhfWid3l3pncoUbqRsE6DZQkNR5f9jp38GwqgH2sAgCpAkIkXJwVE5SlbFtWntIezrIiz090Rpr9yabKfiikpB05XGgxBxOuVTN0DfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86782c7f01.mp4?token=ZBHJHcqdxjssuGySRsDB1By7QPI_g3sGu2e7ScM0YTclHmrkpd50NTHsIz7O9kdQuSnpqUdM3rgYCs5xV7uJeus2HPJCcjrTCSvCTXNodpVOkHktuijMPWYyIGq8AIV0K-1TsPq38Po-MXRvuVRRvVDJG3Q6UrbVGHLfQ68gX9htymIyHxmOOT8o-K1-JutZATxT623PLPoCVLyIY_m1Qdwyee5uq7fr1gfBjOelcq43hGZEhfWid3l3pncoUbqRsE6DZQkNR5f9jp38GwqgH2sAgCpAkIkXJwVE5SlbFtWntIezrIiz090Rpr9yabKfiikpB05XGgxBxOuVTN0DfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در توییتر میگن 'ترامپ به محمدباقر قالیباف گفته محمد سامتینگ':
twitter
ترامپ: می‌گویند یک محمدفلانی دارد آنجا با بیل‌ یک کارهایی می‌کند. بیل‌ها شما را به جایی نمی‌رسانند. بزرگترین ماشین‌آلات دنیا هم احتمالا شما را نمی‌توانند به آنجا [محل دفن اورانیوم] برسانند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 509K · <a href="https://t.me/VahidOnline/76890" target="_blank">📅 07:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76889">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/faff74c4ac.mp4?token=dr3nnKLZnBTQJFRpeKoKwdXJp4HcmwCJm3DTzXqWhABgPwA7oTsDwUi5K9CBmm3-lxdROmIxdv1rdJBNdfe7gZBKfHiG_V8eTSN_IHvT_lj0Xjg1Wl7BBn4au0QTS_9vQi_8EoO_Bjkijbp-K2e_gzkSFq_eiUPvz-5xO53ov6S1jMeN_bXVt_2Qehdf8kB2hT2RAAavhSk_pzF4fuxICZThrWO_Qal81iPWanz6VPTvFNFr1Mw5QSsnIUhSKJhzfgRFf3pgCo2V4wKtlrpcHrtv8VDD3mYJtSw3ZuoOrHHwlpDZLBFkfzcGqNAegVtMiqTygwXTpR8F04c--bwYXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/faff74c4ac.mp4?token=dr3nnKLZnBTQJFRpeKoKwdXJp4HcmwCJm3DTzXqWhABgPwA7oTsDwUi5K9CBmm3-lxdROmIxdv1rdJBNdfe7gZBKfHiG_V8eTSN_IHvT_lj0Xjg1Wl7BBn4au0QTS_9vQi_8EoO_Bjkijbp-K2e_gzkSFq_eiUPvz-5xO53ov6S1jMeN_bXVt_2Qehdf8kB2hT2RAAavhSk_pzF4fuxICZThrWO_Qal81iPWanz6VPTvFNFr1Mw5QSsnIUhSKJhzfgRFf3pgCo2V4wKtlrpcHrtv8VDD3mYJtSw3ZuoOrHHwlpDZLBFkfzcGqNAegVtMiqTygwXTpR8F04c--bwYXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت سنتکام با انتشار ویدیوی بالا از حملات به چندین هدف مختلف نوشت: نیروهای آمریکا دور دیگری از حملات علیه ایران را تکمیل کردند
ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در ۸ ژوئیه دور دیگری از حملات علیه ایران را تکمیل کردند تا توانایی ایران برای حمله به کشتیرانی تجاری و دریانوردان غیرنظامی بی‌گناه در تنگه هرمز را بیش از پیش تضعیف کنند.
نیروهای آمریکا حدود ۹۰ هدف نظامی ایران، از جمله سامانه‌های پدافند هوایی، تجهیزات نظارت ساحلی، محل‌های نگهداری موشک و پهپاد، توانمندی‌های دریایی و زیرساخت‌های لجستیک نظامی در امتداد خط ساحلی ایران را هدف قرار دادند.
این حملات تازه در پی اجرای موفق حملات تهاجمی در ایران در شب قبل انجام شد.
نیروهای سنتکام در ۷ ژوئیه حدود ۸۰ هدف نظامی ایران، از جمله بیش از ۶۰ قایق کوچک سپاه پاسداران انقلاب اسلامی را هدف قرار دادند تا به‌دلیل نقض آتش‌بس از سوی ایران با حمله به سه شناور تجاری در حال عبور از تنگه هرمز، هزینه‌های سنگینی بر آن تحمیل کنند.
نیروهای آمریکا همچنان هوشیار، مرگبار و آماده اجرای عملیات‌هایی هستند که از سوی فرمانده کل قوا دستور داده شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 486K · <a href="https://t.me/VahidOnline/76889" target="_blank">📅 06:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76888">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اکسیوس: با «پایان» آتش‌بس ایران، ترامپ به نبرد بر سر هرمز روی می‌آورد
ترجمه ماشین:
کاخ سفید خود را برای چیزی آماده می‌کند که می‌تواند به تبادل آتش چندروزه یا حتی چند‌هفته‌ای با ایران بر سر تنگه هرمز تبدیل شود.
مقام‌های آمریکایی به Axios می‌گویند طول و شدت کارزار جدید کاملاً به اقدامات بعدی تهران بستگی دارد.
چرا مهم است: جنگی که با هدف تضعیف توان موشکی ایران و نابود کردن آنچه از برنامه هسته‌ای‌اش باقی مانده بود آغاز شد، به نبردی بی‌پایان بر سر مهم‌ترین گلوگاه انرژی جهان تبدیل شده است.
یک مقام آمریکایی گفت تشدید تنش فعلی می‌تواند یک یا دو روز، یک هفته یا یک ماه طول بکشد؛ بسته به اینکه آیا ایران به حملاتش به کشتی‌های تجاری در تنگه هرمز ادامه می‌دهد یا نه.
این مقام آمریکایی گفت: «می‌خواهیم کمی بهشان سیلی بزنیم تا بفهمند ما شوخی لعنتی نداریم.»
محور خبر: دیپلماسی فعلاً متوقف شده و فشار نظامی دوباره در مرکز راهبرد رئیس‌جمهور ترامپ قرار گرفته است.
ترامپ روز چهارشنبه گفت آتش‌بس ۶۰روزه‌ای که در یادداشت تفاهم (MOU) ترسیم شده بود، پس از تبادل آتش ناشی از حملات ایران به کشتی‌های تجاری «تمام شده» است.
سپس آمریکا دور دوم حملات را در نزدیکی تنگه هرمز آغاز کرد، از جمله حمله به اهداف زیرساختی در داخل ایران برای نخستین بار در چند ماه گذشته.
ایران با حمله به پایگاه‌های آمریکا در کویت و بحرین تلافی کرد، در حالی که تأکید داشت از ادعای خود برای کنترل تنگه عقب‌نشینی نخواهد کرد.
کمی بعد، ترامپ علامت داد که آمریکا آماده کاهش تنش است و به خبرنگاران در هواپیمای Air Force One گفت مقام‌های ایرانی «کمی پیش تماس گرفتند» و «می‌خواهند توافق کنند.»
مشخص نبود ترامپ به کدام تماس اشاره می‌کرد و مقام‌های ایرانی نیز فوراً هیچ ارتباط مستقیمی را تأیید نکردند.
ترامپ اضافه کرد: «فقط نمی‌دانم شایسته توافق کردن هستند یا نه. نمی‌دانم قرار است به توافق احترام بگذارند یا نه. راستش را بخواهید، یک جورهایی دیوانه‌اند.»
طرف مقابل: مذاکره‌کننده ارشد ایران، محمدباقر قالیباف، آمریکا را به «قلدری و خلف وعده» متهم کرد و هشدار داد که تنگه فقط با شروط تهران بازگشایی خواهد شد.
قالیباف در X نوشت: «اگر بزنید، می‌خورید. تنگه هرمز فقط با «ترتیبات ایرانی» باز خواهد شد، نه تهدیدهای آمریکایی.»
تصویر کلی: بازگشایی تنگه هرمز و بازگرداندن آزادی کشتیرانی برای کشتی‌های تجاری، عمدتاً برای تثبیت بازارهای جهانی انرژی، به یکی از اهداف اصلی دولت ترامپ تبدیل شده است.
برای ایران، حفظ کنترل بر تنگه به یکی از اهداف کلیدی در هر توافقی برای پایان دادن به جنگ تبدیل شده است.
این مسئله یکی از بندهای محوری یادداشت تفاهم آمریکا و ایران بود و برداشت‌های متضاد از بندهای مربوط به تنگه اکنون باعث فروپاشی این توافق شده است.
این یادداشت تفاهم ایران را ملزم می‌کند اجازه عبور امن کشتی‌ها از تنگه هرمز را بدهد. اما اندکی پس از امضای آن، مقام‌های ایرانی آمریکا را متهم کردند که با عبور دادن کشتی‌ها از یک مسیر جنوبی در نزدیکی ساحل عمان بدون تأیید تهران، توافق را نقض کرده است.
پشت پرده: مقام‌های آمریکایی می‌گویند کاخ سفید معتقد است فضای بیشتری برای تشدید تنش دارد، چون صدها نفتکش در هفته‌های اخیر توانسته‌اند از طریق تنگه از خلیج فارس خارج شوند.
به گفته این مقام‌ها، همین مسئله نگرانی‌ها در داخل دولت را کاهش داده که درگیری تازه فوراً باعث جهش بزرگ قیمت نفت شود.
پشت صحنه: یک مقام آمریکایی ادعا کرد تشدید تنش فعلی ناشی از سرخوردگی عناصر رادیکال‌تر درون رهبری ازهم‌گسیخته ایران است؛ کسانی که معتقدند یادداشت تفاهم منافع واقعی برای تهران به همراه نداشته است.
این مقام گفت ایران می‌دید که اهرم فشارش در هرمز در حال لغزش است، در حالی که صدها کشتی از مسیر جنوبی نزدیک به ساحل عمان عبور می‌کردند.
با وجود معافیت‌های تحریمی آمریکا، ایران برای فروش نفت با مشکل روبه‌رو شد، چون مؤسسات مالی تراکنش‌ها را تأیید نمی‌کردند و کشورها تمایلی نداشتند به معافیت‌های موقت تکیه کنند.
هیچ‌یک از دارایی‌های مسدودشده ایران آزاد نشده است، چون ایران هنوز گام‌های هسته‌ای مورد نیاز طبق توافق را برنداشته است.
به گفته این مقام، توافق چارچوبی که آمریکا میان اسرائیل و لبنان میانجی‌گری کرد، بخش مربوط به لبنان در یادداشت تفاهم را غیرضروری کرد.
آنچه باید دید: این مقام آمریکایی گفت: «بخشی از رهبری ایران از همه این چیزها راضی نبود.»
«آنها شروع به تیراندازی کردند و ما تصمیم گرفتیم وقتش رسیده محکم بهشان سیلی بزنیم. این یک روند است. ما صبر داریم. اگر احساس نکنیم به توافقی که می‌خواهیم می‌رسیم، آن را انجام نخواهیم داد.»
جمع‌بندی: معاون رئیس‌جمهور ونس روز چهارشنبه گفت موضع آمریکا ساده است: تنگه هرمز باید باز بماند.
ونس گفت: «اگر تلاش کنند آن را ببندند، پاسخ ارتش آمریکا را در پی خواهد داشت.»
«یا می‌توانند از آن تبعیت کنند، یا دقیقاً همان چیزی را داشته باشند که دیشب برایشان اتفاق افتاد. این فقط ادامه خواهد داشت تا وقتی که آن مسیر را باز کنند و تیراندازی به کشتی‌ها را متوقف کنند.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 449K · <a href="https://t.me/VahidOnline/76888" target="_blank">📅 06:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76887">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kOFlZF3eX7wLtATrK6W44Iw5qJeQsuaoiweEWJtykVRA_uL8WSDKwKqXVZkrzLWAWDrijGGy13RjHGDeQCOHJGyUKg3UXhFVrOaSLygFDrVSCC9EKB7-A0WgV7fYV_XZgVBBZ-wVSUZB_BudZeAQ9sqCod2Ik_Lxnd7asNto74w0bBf6cNtM6xdKN68fRw5IFK6yF4x6XhdIGjjmGQCPu4Hs2EEF-OVA-t3y6XvuzrdNm1LLmtNLxcswpf_dlYneQJbcke3knQz24WS_INhWggR1JcBAq9LC8LexVtrgo0cm8sPZDFNlfeQ4jce2zfLnnN9Ggj5RrqUMawqFaWsptQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران در بیانیه‌ای که از صداوسیما پخش شد، اعلام کرد نیروی دریایی و نیروی هوافضای سپاه در «یک عملیات مشترک پهپادی و موشکی، زیرساخت‌ها و تاسیسات آمریکا، از جمله اردوگاه عریفجان و پایگاه هوایی علی السالم در کویت، و همچنین پایگاه هوایی شیخ عیسی و منطقه جفیر در بحرین را هدف قرار داده‌اند.»
@
VahidOOnLine
متن بیانیه به نقل از ایرنا:
بسم الله قاصم الجبارین
قَاتِلُوهُمْ یُعَذِّبْهُمُ اللَّهُ بِأَیْدِیکُمْ وَیُخْزِهِمْ وَیَنْصُرْکُمْ عَلَیْهِمْ وَیَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِینَ
ملت شریف ایران، ملت کریم و مجاهد عراق؛
🔹
آفرین بر شما مردمان مومن و بصیر و وفادار که با موقع شناسی و تشییع بی‌نظیر در تاریخ جهان قدر و منزلت ولایت الهی و عشق عمیق متقابل مردم و والی اسلامی با مرام امیرالمومنین (ع) را به رخ جهان کشاندید و با شعارهایتان یادآور شدید که هزینه تعدی به مرجعیت و ولایت فقیه مسلمانان بسیار سنگین خواهد بود.
🔹
هرچند این تشییع باشکوه به ویژه ۲۳ ساعت تشییع عاشقانه در گرمای شدید، سرزمین عراق حبیب، مستکبران کاخ نشین را وحشت زده و آنها را به واکنش عجولانه به این قدرت نمایی مردم واداشت و آمریکای عهد شکن با زیر پا گذاشتن همه تعهدات بار دیگر نقاط متعددی از استان‌های ساحلی جنوب ایران و در اقدامی ضد مردمی دو پل در استان‌های شرقی به سوی مشهد مقدس را مورد تجاوز قرار داد تا اخبار این حماسه بی‌نظیر را تحت شعاع قرار دهد و این رویداد الهام بخش را از نظر مردم جهان پنهان دارد، غافل از اینکه این جنایات مردم جهان را بیدارتر و آنها را برای نقش آفرینی در مبارزه‌ با شیطان بزرگ مصمم‌تر خواهد کرد.
🔹
رزمندگان اسلام تجاوزهای ارتش کودک‌کش آمریکا را بی پاسخ نخواهند گذاشت.
🔹
در اولین مرحله از پاسخ تنبیهی علیه پیمان شکنان آمریکایی، رزمندگان نیروهای دریایی و هوافضای سپاه طی عملیات مشترک موشکی و پهپادی، ساعتی پس از حملات دشمن و نقاط مختلف کشور، زیرساخت‌ها و تاسیسات مهم دو پایگاه‌های استعماری اشغالگران آمریکایی در عریفجان و علی السالم کویت و جفیر و شیخ عیسی در بحرین را در هم کوبیدند.
🔹
سپاه پاسداران انقلاب اسلامی به ارتش کودک‌کش آمریکا اخطار می‌کند که در صورت تکرار تجاوز پاسخ‌های کوبنده ما به سایر پایگاه‌های آمریکایی در منطقه توسعه خواهد یافت.
و ماالنصر الا من عندالله العزیز الحکیم
سپاه پاسداران انقلاب اسلامی
۱۸/تیرماه/ ۱۴۰۵
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/76887" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76886">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QPqPx43V4X0n0UFFbP8WFtkITZ5CZ7oElkk4UQEVRfh7Loe58SbOWM09JxDMmlw7RIjoK5A-Yw6mzp5uOCHbxPs5WRHTOFOSKx_Oj-CaGljV-hyNbP5KsG6l5Pd4YnDetXUfx3PP0r-j985Pi_4aKPNAXVCw4JTYY6TZ0BBTJshz5pAThIdgI0LXGDymo1-WuO3fvIwFjNZgtJ7feoXMrnbzEfFfn7JfDTnThuAeMHk8xih51MOA-ibS984BPj53b0roQQyGWS0fZ-7a-ftuoAwJwcq9rsIAx1Z8RmsHZ-UBJafnXvNWSI9RufS8TRg1xzCnWkNFi9-4Nhhi4vL0rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی:‌ 'برج مراقبت ترافیک دریایی بندر
#چابهار
که چهارشنبه ۱۷ تیر  مورد حمله قرار گرفت.'
Vahid
چند دقیقه پیش هم دوباره از سیستان و بلوچستان:
سلام سمت کنارک الان صدای انفجار اومد
کنارک رو یه جوری سنگین زد از خواب پریدیم
۴ تا پشت هم
از بوشهر هم پیام‌های تازه‌ای می‌فرستند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/76886" target="_blank">📅 05:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76885">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1ee7dc63aa.mp4?token=WnUfaK3Oj4VPBFxxj9kyDqyzjAgZzFWeAWoJMk1ent5WHWhW6AUL-gADsnJqus8Z22tFnDpP8_pamiUQE0G6eS35jFkboIhEa0nbIO2x_SBovt_r41Kb4SA7-QrvCoa-c-wJBTzbQKMr1FrW8X2bnLX-P-yGYiFI8Tsy0V8t6jdzbz6hk6bdFsKgoKqQZ4Z9IrH291ZuRjj-ibB4KI_hWLdg9Hc9nu5Yhuh0oDihYxg-BHn8Rmwo9to4lRodZFJ_eSQq99Mlfi1mJdNNrZGKOzU63BNZ5BdiE2RU_0fM7z1OK_C2LhyKncwF1xjiFz3UsWGREs9yo36jokF7T0icAg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1ee7dc63aa.mp4?token=WnUfaK3Oj4VPBFxxj9kyDqyzjAgZzFWeAWoJMk1ent5WHWhW6AUL-gADsnJqus8Z22tFnDpP8_pamiUQE0G6eS35jFkboIhEa0nbIO2x_SBovt_r41Kb4SA7-QrvCoa-c-wJBTzbQKMr1FrW8X2bnLX-P-yGYiFI8Tsy0V8t6jdzbz6hk6bdFsKgoKqQZ4Z9IrH291ZuRjj-ibB4KI_hWLdg9Hc9nu5Yhuh0oDihYxg-BHn8Rmwo9to4lRodZFJ_eSQq99Mlfi1mJdNNrZGKOzU63BNZ5BdiE2RU_0fM7z1OK_C2LhyKncwF1xjiFz3UsWGREs9yo36jokF7T0icAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، بامداد پنجشنبه ۱۸ تیرماه، در مسیر بازگشت از نشست سران ناتو در آنکارا و در هواپیمای ریاست‌جمهوری «ایر فورس وان» گفت آمریکا در برابر حملات ایران رویکرد «۲۰ به یک» را دنبال خواهد کرد.
ترامپ گفت: «همین حالا ضربه بسیار سختی به آن‌ها زدیم. هر بار که آن‌ها به ما حمله کنند، ما ۲۰ برابر پاسخ خواهیم داد.»
او افزود تهران سه کشتی را هدف قرار داد و تاکید کرد هر زمان حکومت ایران حمله کند، آمریکا «بسیار شدیدتر» پاسخ خواهد داد.
@
VahidOOnLine
پست قالیباف:
آمریکا هنوز یاد نگرفته است که زورگویی و بدعهدی دیگر بی‌هزینه نیست. شفاف بگویم: بزنید، می‌خورید.
دست و پای بیهوده نزنید که بیشتر فرو خواهید رفت: تنگه هرمز، فقط با «ترتیبات ایرانی» باز می‌شود نه با تهدیدات آمریکایی.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/76885" target="_blank">📅 05:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76884">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اکسیوس:
یک مقام آمریکایی گفت ارتش آمریکا در چارچوب حملات روز چهارشنبه، دو پل راه‌آهن را در شمال‌شرق ایران با موشک‌های کروز هدف قرار داد.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/76884" target="_blank">📅 05:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76883">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5a9c09d7a1.mp4?token=jvAVcmpbrE6LUkLce1nROTaqUwQlr1uKSbcLzml8nLuXCs9noF4pFeiZkqi5j_ll0f2inpGPz4EFWkqwBDmeiYzJ1ED1jDDzs-ICzzOV0xlLliwdgz2tA2gEhxGGviaIZ4DPjQN5pIAAPAgEMnz2CgKVtaM3cFJyDXAwVsk8rB6p-2ltTskiTQNRLoPfGElDpuMNhVKs_KkpSOL94SYBN6xBEQkY6xoNQAiPJqFcM_YkZ6ZkWgJRXpk3tLiPROUS2sdQJcGbG7X3vn1b5lceuDUkVXhLDlLvUZX5BuWnp9ECx9BOqnkMkYOEIdVm1o3rwvz7guILMvydPonUQUfrug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5a9c09d7a1.mp4?token=jvAVcmpbrE6LUkLce1nROTaqUwQlr1uKSbcLzml8nLuXCs9noF4pFeiZkqi5j_ll0f2inpGPz4EFWkqwBDmeiYzJ1ED1jDDzs-ICzzOV0xlLliwdgz2tA2gEhxGGviaIZ4DPjQN5pIAAPAgEMnz2CgKVtaM3cFJyDXAwVsk8rB6p-2ltTskiTQNRLoPfGElDpuMNhVKs_KkpSOL94SYBN6xBEQkY6xoNQAiPJqFcM_YkZ6ZkWgJRXpk3tLiPROUS2sdQJcGbG7X3vn1b5lceuDUkVXhLDlLvUZX5BuWnp9ECx9BOqnkMkYOEIdVm1o3rwvz7guILMvydPonUQUfrug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی پخش شده با شرح: 'بوشهر آخرین دقایق چهارشنبه ۱۷ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/76883" target="_blank">📅 04:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76882">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EBetTlNgRVGl3jQIucKKptd3zwEAKIKyq0n5mZG7_PCla1KUU5H6VoYrSFDdF5pn-w-x6siI93_hkyACJaPPpyOW3uM4RJJS1tkaIGi8fb060jsUOBH3ZzdZGsd8oygejrZhucSSBRyb8AVi5W3_dwhu9o8lOQib9QEl5pkx6aM4ayQlpy2WgRCg0bpLqw1zdNvK2AuznEeuaDECitjH2JyWgs53SJeJ-oAJTyRz-KDVLhvV0EORXMZaUz6rcMFrHhx4mqszf6cbMbOGivEcUtbPh64k1LSUBIuAtwxToLzMKemTQBYp9m8bq1KSslXAZbPx2tjxZYD6rztnC7oyjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلی پیام درباره شلیک موشک از اهواز و امیدیه در خوزستان
و هم‌زمان درباره اعلام هشدار در کویت و بحرین
در خبری دیگر:
برای  نخستین بار در نزدیک به سه ماه گذشته چنین پیام‌هایی برای ساکنان قطر نیز ارسال شد.
قطر همزمان از میانجی‌های مذاکرات تهران و واشینگتن است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/76882" target="_blank">📅 04:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76879">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d485a6535f.mp4?token=L8LazVZ1_x90YWqP8Dh5MUm7bLS8P1hL7OBFpsJ3uhhIzu8ODVeyumkpNXSATEz7RS_bKDMRlQvFaHS8ZTLLKcmDSBG_mDooFpTR7fJBSXGXygGULTF31JLmxTgX0NiesKOrqljT5UKKMbIf_Yp_ZR-0CJKFxQj4-GPbdpvh4nnoJEMPHYYHA5hYDrGdO2bXA-DflHljBCZZH5Dgy5PQ9u4g1s7WQu5pQMXVEMVpnGskT3hK804AfmE0iHHdOc9a0zRP0YM0TBzDEvVqLVTx9ORyh3AnGA6zqcipr3hSlK83nv3mhmN2GdN5Qmx-DgH6Hhk05F2UBYkLS1sBD1BQvw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d485a6535f.mp4?token=L8LazVZ1_x90YWqP8Dh5MUm7bLS8P1hL7OBFpsJ3uhhIzu8ODVeyumkpNXSATEz7RS_bKDMRlQvFaHS8ZTLLKcmDSBG_mDooFpTR7fJBSXGXygGULTF31JLmxTgX0NiesKOrqljT5UKKMbIf_Yp_ZR-0CJKFxQj4-GPbdpvh4nnoJEMPHYYHA5hYDrGdO2bXA-DflHljBCZZH5Dgy5PQ9u4g1s7WQu5pQMXVEMVpnGskT3hK804AfmE0iHHdOc9a0zRP0YM0TBzDEvVqLVTx9ORyh3AnGA6zqcipr3hSlK83nv3mhmN2GdN5Qmx-DgH6Hhk05F2UBYkLS1sBD1BQvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای دریافتی و تصاویر منتشر شده با شرح 'انفجارهای حمله به آق‌قلا در استان گلستان'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/76879" target="_blank">📅 04:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76877">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iv1_98ALTjrCRBCLyqkQk1TSnRXmNc5HM-h0EkdPX5HZUnoqk1I6x80LvnOuOQeXHAbryZjta0h8vtY8FF02b1EAGiZ9x82kk6fb8Ul6W3IZ4M9XXhAkAUbSCVPPT1Yxbi4VNKf5roEHERwWICekG2Ag38eOnhvr1D3b1UOQxb2ph8vs2aeJnFTiC-mDkmh1GCHmRXZt5bKwA0Cni1a9q-IJqh7VB8qFV0ijm-h5DRx3cUnoc4bnH6zRJ_rW9Ehrm-NwZzUPakCPwfKBkV1yBi-VF43tj_PzQeJzxdYKVBS_tDfRmNnu6JbzbftAkLApkf6mndUs8oZNkUhPNwhGDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4761d5d8a3.mp4?token=WRMtRazSH3L-6m9fxtPw2NXvpkRLEdZyTKTZlxWaGqn4Ba3JylOPZmqMYxosb96avabOLyAxrIE26pCtOk2wZeZN65QoabdbhR10fhWl1xim4_Ng5AHzExW9ohZVMBAPQGZ7sfl_pH667HHHRJn6CHfj1o9CnT-yyHMrhz-6gORtFrCqcy9OJsNCExlh-AJAx3T672jMMneBcWC-kQjQSKAc2n_O4gBTu30XLofcIaYOkZlc4KLHBSvfsd_mbEjUxcg7AQm565b-yhT9VHxECA3FXs8MJrbBlKJD9krMZYfBOJBVlUBmFnpZ_2kpFX-jGQhU4OLumcU5cqqcTWm4dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4761d5d8a3.mp4?token=WRMtRazSH3L-6m9fxtPw2NXvpkRLEdZyTKTZlxWaGqn4Ba3JylOPZmqMYxosb96avabOLyAxrIE26pCtOk2wZeZN65QoabdbhR10fhWl1xim4_Ng5AHzExW9ohZVMBAPQGZ7sfl_pH667HHHRJn6CHfj1o9CnT-yyHMrhz-6gORtFrCqcy9OJsNCExlh-AJAx3T672jMMneBcWC-kQjQSKAc2n_O4gBTu30XLofcIaYOkZlc4KLHBSvfsd_mbEjUxcg7AQm565b-yhT9VHxECA3FXs8MJrbBlKJD9krMZYfBOJBVlUBmFnpZ_2kpFX-jGQhU4OLumcU5cqqcTWm4dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی با شرح: 'شلیک چند موشک از جم در
#بوشهر
پنج‌شنبه ۱۸ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/76877" target="_blank">📅 04:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76876">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6e40fe096.mp4?token=FsbDVvv3UI_LYCM3rxAZIY-4RaIX6tsEpLnjvSRARCdAXl_ohxs1fWqHrwVmqix5PKKoEidBIMr9ph62_msrguK6KkocsvJ3Ql3A-U48KIHcetW-_2dw06lHh7jaK3QqzjSu6Uz1EtIx5RIl__zsD_F7JBeVDhz4SZoOHhEWBgf2i7n9V5DJIGFZVD8QcWyfwVbSmdSajvQrdXdgCL90vD97G1MH6bgnueMePxu0zN5XQwSmPgqzTtTfaODNHUnIs5UQMvsJyZiwfZiDBxbhkoMosPRV0oTqxnU6ISXExr37oQBOpv1WgYQGz_V4RWOfEaVughf5-0nXVlBoBzoElQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6e40fe096.mp4?token=FsbDVvv3UI_LYCM3rxAZIY-4RaIX6tsEpLnjvSRARCdAXl_ohxs1fWqHrwVmqix5PKKoEidBIMr9ph62_msrguK6KkocsvJ3Ql3A-U48KIHcetW-_2dw06lHh7jaK3QqzjSu6Uz1EtIx5RIl__zsD_F7JBeVDhz4SZoOHhEWBgf2i7n9V5DJIGFZVD8QcWyfwVbSmdSajvQrdXdgCL90vD97G1MH6bgnueMePxu0zN5XQwSmPgqzTtTfaODNHUnIs5UQMvsJyZiwfZiDBxbhkoMosPRV0oTqxnU6ISXExr37oQBOpv1WgYQGz_V4RWOfEaVughf5-0nXVlBoBzoElQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدای ویدیو: هوافضا ی چغادک بوشهر رو زدند
ویدیوی دریافتی، نخستین ساعت 'پنج‌شنبه ۱۸ تیر'
Vahid
📍
گویا اینجاست:
GoogleMaps
via
Mitch_Ulrich
🔄
آپدیت:
پیام‌های دریافتی الان دوباره ساعت ۳:۳۵
بوشهر دوباره زدن…
همین الان پنج تا انفجار بوشهر
سلام وحید جان ۳:۳۸ صدای چندین انفجار، بوشهر.
سلام آقا وحید بوشهر سه دیقه پیش صدا انفجار اومد
🔄
آپدیت:
بوشهر رو خیلی بد زدن.
ناحیه‌ی بهمنی، چهارراه ریشهر.
ساعت ۳:۵۵
سلام
بوشهر همین الان بازم زدن سه چهارتا پشت سر هم صداش خیلی بلند تر از قبلی ها بود
۳:۵۶
وحیدجان الان ساعت 3:55 صدای 5یا 6 انفجار پشت سر هم اومد، احتمالا از پایگاه هوایی بوده
سلام وحید جان بوشهر الان ساعت ۳:۵۵ خیلی شدید زدن پایگاه هوایی رو
دوباره صدای انفجار اومد بوشهر ساعت 3:55
ساعت ۳:۵۶ دقیقه صدای حداقل سه انفجار در بوشهر شنیده شد.
بوشهر از ساعت ۳:۲۰ تا الان ۳:۵۵ کلی صدای انفجار میاد، ۳-۴تاش خیلی صدای وحشتناکی داشت!
الان بوشهر ضداى انفجار ٤ ٥ تا
ساعت ۳:۵۶ دقیقه صدای حداقل سه انفجار در بوشهر شنیده شد.
چند انفجار هم بعدش شنیده شد که بنظر دور تر میومد
🔄
آپدیت:
بوشهر ساعت ۵:۲۲
صدای دوتا انفجار پشت سر هم اومد
۵:۲۲ بوشهر رو همچنان دارن میزنن، احتمالاً پایگاه هوایی
سلام بوشهرو زدن
الانم صدای فعالیت پدافند و توپ سنگین میاد
وحید نیم ساعت پیش صدا انفجار داخل بوشهر اومد نمیدونم دقیقا کجا بود ولی خیلی بد بود صداش
🔄
آپدیت:
دوباره الان صدا اومد ساعت ۵:۵۶
اطراف محله بهمنی بوشهر ساعت 6:01 صدای دو انفجار مهیب شنیده شد
ساعت ۰۶:۰۰ صدای انفجار مهیب در شهر بوشهر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/76876" target="_blank">📅 03:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76872">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jhpF_Z3CTqTMSXGHFvDNUCkcaTlYyt5TBkm1iYOLqqThnAmz-LfSWkebx9nT22jLkHDj3mVrPlIvg2W-CCYU72IGqkB7dX34WbvuwVMfG7Ocf5QIUB3UX-MuRp4PRaVyj2jlG6XqXQfsZPikZD95iUbHHuUcn4vJaEnhyY00tTaMYVlTTB8xePyVwlpaFSvm7KzHQs95tlqrw3KsD1x28kVH8SsIRCQxZ7puwOsaB_l31sjbRt1NMYfYWKKkzssjZ6PSaiIs1LmoQPmk_6VOQPnGMerKK_ECGzSQM438bFeyFNFXhfCAaq29gVkjFGatb_6u9pG7XP8EqlLkhnsnBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aydrCl7R3WPTrlCqpiUWMi1awds0xuyky8tLJXOt68Qt1hoA7sa2jPk4x3vKkoF5rUpVjTgQc6kRPJ9yGy4ObglfcOsqwE1TxuNwm0YgR7g_VM2A30t4SSDH8JW99PDpB6Z-x5tGXRwuBmLEmyUEb5ere3cGZ7ein8qJMBxPnNT4vWTGOWpHtV6FrIggcemqyz6yzi2xdluEJSoGYDzNsR3jScXp4tNK5QljhFt3RAKwX5rIk_imv7tYLOlBfOOCijOeM9-jhaXeTVXqZaXdTd3j1wiWc_bvozuYZ5m47ZlSwLfI5GdYhbcQdFKH6oE_P1MqCmBHXPaTN4A-XnVAhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MhNb9k7e-ttGd8UGbbr9T6fyvC0k2W9hjRL3b5WTndqUfRf8yPY41SNdrpUE2l1jfH3gZKOENBCtpjKpvvS7NF89tgxDyc14z6yHI109kiqTCCx2ZM5BELI0GQR6NmOuj9IrWGNlZmuTjijn4CcLMURlra_A7QHZT40drauqLqlqY_gCe2iuWYSYTh09FEbmY_uLeQj5qCweT2c4I-Sk4gEd8t1eqVAixmnYozGgpo8zSVXru0i8aNI-_Sf7VFrXYbFo6LJEe1jNf3DAFuO_MsZGMScMs9DezDjB8OewLrtMpO2lUWDuCyZrOzFHbhF90cj2tHZaFSgS92pfaLcsDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c0e73ce6a.mp4?token=dc1zYRLR2tNOzlxafhE_-9sX4iWqBXrQvkepDy0cgbXHKtITR5Fx5HwR9gXK--xaj2y2QpA4_PQ2ZNvaB3Ngoi_plUnZvQEIr57vI9j0yPLT0qHI4JAukXSD4Dp1Uvs0ZMHEH065i3BO7YvboawfXcIZB3Zg2Iv2vH3tuSMULPeIoe7QJkJENbP35yEp6M_Krz4_lovG4bN6AummsbmD0SXvurvr3HXrP_LHWUC-N8zss_0d02RRCtvSEVhnHH_LrmCX8wVCCyTDxd4LLiCXsZQ8PvMd1TpPW8Eq7L2Xxhs9VUE-BpxSKEd70jy54BwE_RQRD1mP6QjjAb7Cl2q4tg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c0e73ce6a.mp4?token=dc1zYRLR2tNOzlxafhE_-9sX4iWqBXrQvkepDy0cgbXHKtITR5Fx5HwR9gXK--xaj2y2QpA4_PQ2ZNvaB3Ngoi_plUnZvQEIr57vI9j0yPLT0qHI4JAukXSD4Dp1Uvs0ZMHEH065i3BO7YvboawfXcIZB3Zg2Iv2vH3tuSMULPeIoe7QJkJENbP35yEp6M_Krz4_lovG4bN6AummsbmD0SXvurvr3HXrP_LHWUC-N8zss_0d02RRCtvSEVhnHH_LrmCX8wVCCyTDxd4LLiCXsZQ8PvMd1TpPW8Eq7L2Xxhs9VUE-BpxSKEd70jy54BwE_RQRD1mP6QjjAb7Cl2q4tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این تصاویر با شرح پل راه‌آهن در نزدیکی آق‌قلا در استان گلستان دارند دست به دست میشن.
آپدیت:
منابع حکومتی:
براساس گزارشات منابع محلی اصابت چندین پرتابۀ دشمن به پل آق‌تکه‌خان در مسیر ریل قطار در محدودۀ غربی شهر آق‌قلا در استان گلستان گزارش شده است.
براین اساس حدود ساعت ۱:۳۰ بامداد هفت پرتابه شلیک شده که دو مورد منجر به انفجار بر روی ریل راه آهن  شده است
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76872" target="_blank">📅 02:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76871">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WC2aen7D8JlpGEAqGdBtK2vAeFW4Omn1_CsfzZfQvYhTqKTyoAgenoHb54talDMTIkTfoyRWVOlJhfHJWxfm7RMZlGURNCoCpITgy2NCGd1q1b8QoVZTcAXWMpJU7DOyo6MHlJqxMc9FAFem9Qs3owvaLxWTGgnm2oH3wPFPS26oHrfU16MMxbqc_d_IqvaFy6q7YEBk572_uVodszl3wrj_FzJoKTo4U4AEcWMT6GNuG621PB-2b-0Am-8SMZVlodt7Fio8SFvhfttVp4rM-OfKtg4HOEXiMhl3fMwieQm2lUokWpkPzByJSpqlfz0acP8P4ctKELgbV334wtui9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در نخستین ساعات بامداد پنجشنبه گفت که حکومت ایران پس از حملات مکرر آمریکا در منطقه با او تماس گرفته و خواستار دستیابی به توافق شده است، اما او نمی‌داند آیا تهران «شایسته» توافق هست یا نه.
ترامپ در گفت‌وگو با خبرنگاران در هواپیمای ریاست‌جمهوری آمریکا، هنگام بازگشت از نشست ناتو در آنکارا، ترکیه، گفت: «آنها کمی پیش تماس گرفتند، آنها خیلی زیاد می‌خواهند توافق کنند. فقط نمی‌دانم آیا آنها شایسته توافق هستند یا نه.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/76871" target="_blank">📅 02:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76870">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پیام‌های دریافتی تاییدنشده:
استان گلستان آق قلا پنج شیش بار صدای انغجار و نور شنیده و دیده شد
سلام وقت بخیر ، استان گلستان هم زدن ، بالای پنج بار صدای وحشتناکی اومد
سپاه شهرستان آق قلا واقع در استان گلستان و حومه شهر گرگان رو هم زدن
سلام وحید جان
۵دقیقه میش گلستان رو زدن
شهرستان اققلا بدجور لزرید
۵بار لرزید ناجور
سلام وحید جان
شهرستان آق قلا بدجور زدن و مکانشو نمیدونم
کل شهر ریختن بیرون
سلام آق قلا صدای چند انفجار و نور رو ما هم شنیدیم ساعت تقریبا دو بامداد
۲بامداد چهارتا انفجار پشت سرهم آق قلا استان گلستان اخری صداش و شدتش بلندتر بود نور یه  لحظه دیدم ولی کجاخورد رو نمیدونم احساس میکنم دور بود سمت گمیشان رادار داشت قبلا
شاید باز اونجارو زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/76870" target="_blank">📅 02:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76868">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ozZKe11uJVZ3ZMRjHnkqx7LIuFcbJLswFTfFEDrbrn-ZvNrmull5r35O0uSF9Qb10VlLdef67cMXexwXV94iXRNrW7WCDByM2hlEAi973qtR649uPV2H9mwwCfPjPRphI97OyJ9Dl0GVMl6tvwfqwSO7kcBwEdX9ZcVibVKauQti9MVk9_h1hTDq6Cpv5KT0yOz7CIlbNq9HZbYE8y4Ta3Ckzou2DeHK9-pOfuxUilihkLPqBNuwd7URueNshiZFHK2-QuzoR2uNznp1rermxDjB38Wxd0J7eRHQBFbaLNDXRq2slvwoGzQg7ZruaPGTrk-6-kntEn1FT_jt5qbBUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f66b394713.mp4?token=QD5SIQTu-PDlR_R_E-tL0BNYs0Bp7NSiw39D23plIIIg5YUFJ06y0c6-6Pt3Y2XY6OVmS-8SSWDfgq4hx7kzw5tcKqdJrmaJ356vrGXu2VUjcOOJmUjzMA1MxiwvABC7L20rbHlUfJ6-OKNaeriHRQ3vOrqo7XEZYB-GMzDfIbemCXgbTlJL039H1heNhDvBNoahf7N_2Yn4qEaKSsWuN_tNtdQkuuHILQtBwW7m9IfIYoXFZS9hQr4bJbmP2zc44irn6pFVWCsvGkZPYYP-X2E_ThiiiqT2kB_LB-nHACkeLhaqPgNWzzagrKVhWguvnBFq0q5xK0VL7XgcpsHqXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f66b394713.mp4?token=QD5SIQTu-PDlR_R_E-tL0BNYs0Bp7NSiw39D23plIIIg5YUFJ06y0c6-6Pt3Y2XY6OVmS-8SSWDfgq4hx7kzw5tcKqdJrmaJ356vrGXu2VUjcOOJmUjzMA1MxiwvABC7L20rbHlUfJ6-OKNaeriHRQ3vOrqo7XEZYB-GMzDfIbemCXgbTlJL039H1heNhDvBNoahf7N_2Yn4qEaKSsWuN_tNtdQkuuHILQtBwW7m9IfIYoXFZS9hQr4bJbmP2zc44irn6pFVWCsvGkZPYYP-X2E_ThiiiqT2kB_LB-nHACkeLhaqPgNWzzagrKVhWguvnBFq0q5xK0VL7XgcpsHqXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر گزارش داد صدای چند انفجار در منطقه شمال شرقی «ایرانشهر» واقع در استان سیستان و بلوچستان شنیده شده است.
این خبر هم‌زمان با ادامه حملات آمریکا به اهدافی در جنوب و جنوب‌شرق ایران منتشر شده و جزئیات بیشتری درباره محل انفجارها یا خسارت‌های احتمالی اعلام نشده است.
@
VahidOOnLine
پیام‌هایی که من دریافت کرده بودم:
سلام شهرستان ایرانشهر روزدن
سلام ایرانشهر هم سمت فرودگاه زدن
سمت ارتش ایرانشهر انفجار شده
سلام ایرانشهر سیستان بلوچستان ساعت۱۲:۵۹صدای انفجار میاد
فرودگاه ایرانشهر میگن بوده خودم ندیدم ولی صداش خیلی شدید بود
سلام ایرانشهر سيستان بلوچستان همین الان ساعت ۱۲:۵۰ صدای شدید انفجار و پنجره ها لرزید.
فرودگاه ایرانشهر
پنج دقیقه پیش سه چهارتا صدای وحشتناک تو ایرانشهر(بلوچستان) اومد در حدی که شیشه ها تا مرز شکستن رفت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/76868" target="_blank">📅 02:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76867">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kYnthkbZtLcdiDOtYCDsedYhmdCleUMmHkDEmA4NRmuEGZMhuz3499eabFY5A94EEb1Anxh0-2n_JPFI6NflBgFb2cw5Ld8PWvVkt4G5yamcW2hvVoh43EeA3ILoPgcm-rKMLrsZYajJDO2dKOPEllIq418D02n4pX0PHcd-SwkHPt-WtjyHT_QZrX_mPlGkXTo_heAEMlVnmYQUPCh32R3zdIJzxRbC657ccwj2Qluu4cW1pQlxy9xfKGm06kcbfFmLhlP4KLjDC5SNaT-A24h1HxWz6pHWk2VBpHy8LsOE-AJix86YkBtLKHATBLng6KNz078w9wnocsZgQMdsbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ نوشته "این در تلافی بمباران دیروز کشتی‌ها توسط ایران است. اگر دوباره اتفاق بیفتد، خیلی بدتر خواهد شد!"
بیشتر از ده تا عکس و فیلم با شرح حمله امشب پست کرده. حتی عکسی که اشتباهی بعضی از منابع پخش کرده بودند:
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/76867" target="_blank">📅 01:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76866">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b103f9cf8a.mp4?token=WaZnJx4lGTUrFh3BAPJo2H72BXbnKAAK1oq215iljhjM1X_oO5ws420iQOeyEYnVI7u-voP9D4c_Y_xWeNdVPmAUk_JiwA6N9ml3nKEEAVQwNGUrEm-Vu9QPTz7s5wsKe0QvUUfjGoyERO__drIqyz9FAn_a0lZEzvQNZcYHI6d1pWHxMJ-YgmR3CBsm9WuOlQ5gL4-yFf5JcABfqV_USElvXylBXjwrX5ffklqab6oPvfnCyo152XiWo3pXPgn188TdzW6wxZAuDX0ZD3_pD7UKux_COIjPvOsQ0r_NOBOWOjVoG_AnbeLz2X8dmaORYev0tFiwcfQ2N9gnJDIoFw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b103f9cf8a.mp4?token=WaZnJx4lGTUrFh3BAPJo2H72BXbnKAAK1oq215iljhjM1X_oO5ws420iQOeyEYnVI7u-voP9D4c_Y_xWeNdVPmAUk_JiwA6N9ml3nKEEAVQwNGUrEm-Vu9QPTz7s5wsKe0QvUUfjGoyERO__drIqyz9FAn_a0lZEzvQNZcYHI6d1pWHxMJ-YgmR3CBsm9WuOlQ5gL4-yFf5JcABfqV_USElvXylBXjwrX5ffklqab6oPvfnCyo152XiWo3pXPgn188TdzW6wxZAuDX0ZD3_pD7UKux_COIjPvOsQ0r_NOBOWOjVoG_AnbeLz2X8dmaORYev0tFiwcfQ2N9gnJDIoFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: 'همین الان پایگاه نظامی بین چغادک و
#بوشهر
'
پنج‌شنبه ۱۸ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/76866" target="_blank">📅 01:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76862">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ocZlRbYQEn7ear51JUAlRs8mN2lU2SZ4prD-_vCgBC_Urgk5ao8MTZGut7gIIIXO_U-GkHACbR6NAornv8BqT6MmImL0x8oB9F47KaEy3qro3IgZT10KF9thnbbjipbPCmuPAtzEN_P9WI8a0DhhBDZUpusWlscT1P64kKY3OcRODqVlzoto1oypivKJEZm3IN4T88jFWIbRQbwsw04rQYdaYcirBnJH58b0bq220F8U5Oau1RuwihLmsixCiNRKeajvMQ7YvJmiRWUOmpjvJNfq2JK9FFl0r_JYwMr95UFs4nms3Miy9uIJ2ABiZ7cIbM9V37FqsIsOGyVZbRJ6Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kP9Vdqcd1hnfcDIniV7WduC4IgyBLho1Bx4XLUEytiiO58AMBO5yafQtxoBVkTwj6ZNLSehnbKv9C1CGazBKV6MOlnltfFMC_O-If0Dn7WfiyuLAJK6dmzo5RSo2nmXUi9BPCmYsQmFba6szLEULmZiUN3VEfXBeAxFIVxtjYOCwD-L-yU1-U3e3AHqlNMHPWWpmTnheGqrSoGmWUV0W864MSpv_hBGyez76cWvnmd-g2fP-eVHtmx0So0gdqJUChBDO4ZxtYHqRuZ15cZEe383FRvQc80v2C5QFJrrdpip-CujcGPIX_R7U8aKi_wVAKGSbY3iGXJP9pWXCzAjxnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/349d8753dd.mp4?token=BArUnVoVNVyiZ155tb8PqMi9HtSCLu1Lv0AJyqSQA3Rpwm7rhyWZ7qD4CqxDnOBlzmVMIBiDKKJfpSRjSmhJ7waM2tDtOa4b6KYykeLWfWOJ-71WjbyOfZzXnpXT0RJqMqftz3hlosgOnAqE37MnNqmFFaiXUm5lfDEc7FpBqzQdV4CNlG_s90yi09v-apfzr70sW_NQV6wAN0EsqFpdedYqW-E-XW0WMp5_AQaFu58zCrxc8jZRLh5vaZkZKO9s4R5hED6DZIYWJhEBfCUYJAVwUKSXdlc7Zyoq0mAX5-T6HV18zAFzqTF12cV1McN2Msg3m9ovWvRQrv7nBdBbtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/349d8753dd.mp4?token=BArUnVoVNVyiZ155tb8PqMi9HtSCLu1Lv0AJyqSQA3Rpwm7rhyWZ7qD4CqxDnOBlzmVMIBiDKKJfpSRjSmhJ7waM2tDtOa4b6KYykeLWfWOJ-71WjbyOfZzXnpXT0RJqMqftz3hlosgOnAqE37MnNqmFFaiXUm5lfDEc7FpBqzQdV4CNlG_s90yi09v-apfzr70sW_NQV6wAN0EsqFpdedYqW-E-XW0WMp5_AQaFu58zCrxc8jZRLh5vaZkZKO9s4R5hED6DZIYWJhEBfCUYJAVwUKSXdlc7Zyoq0mAX5-T6HV18zAFzqTF12cV1McN2Msg3m9ovWvRQrv7nBdBbtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر بالا با شرح
#چابهار
پخش شده‌اند.
در خبری دیگر:
خبرگزاری تسنیم گزارش داده است که جنگنده‌های آمریکایی پایگاه امام علی ندسا در چابهار را بمباران کردند.
تسنیم اضافه کرده که تاکنون صدای حدود ده انفجار در چابهار و کنارک شنیده شده است.
برق قسمتی از شهر چابهار نیز قطع شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/76862" target="_blank">📅 00:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76860">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c60aeedc6c.mp4?token=kJxaGv_X1ISDMdi1b8t7djyD4lcVu0Exzf1pjdjkPii3hxPkVHi3QrzSdU-Xk7GR8c1WWZVoSUEue6zUpuKB1R93n0wTdurzkUdrQshFCAh40Plw9SmxDJVNc31Fu7H3jyBOUhFcj9RXTmZWoxHhKruOjTWx1zyZvcdSMbm_kpzG0lI82qOMGWx0brhGzQhCAssA37tPpN6LsW5QXlaPA2COat8eDbkjGw42EHVXmPasQsnlsA2bSFmIfZw_gVR1PvWtkikHKw4zjNu5fsbQstKj8To-PC1WcXy_WfrzGGJ0KOi_onsakQTkM5YYdTtdcdKXNrZaKNneXtw55yoNfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c60aeedc6c.mp4?token=kJxaGv_X1ISDMdi1b8t7djyD4lcVu0Exzf1pjdjkPii3hxPkVHi3QrzSdU-Xk7GR8c1WWZVoSUEue6zUpuKB1R93n0wTdurzkUdrQshFCAh40Plw9SmxDJVNc31Fu7H3jyBOUhFcj9RXTmZWoxHhKruOjTWx1zyZvcdSMbm_kpzG0lI82qOMGWx0brhGzQhCAssA37tPpN6LsW5QXlaPA2COat8eDbkjGw42EHVXmPasQsnlsA2bSFmIfZw_gVR1PvWtkikHKw4zjNu5fsbQstKj8To-PC1WcXy_WfrzGGJ0KOi_onsakQTkM5YYdTtdcdKXNrZaKNneXtw55yoNfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'
#چابهار
، انفجارهای حمله ۲۳:۳۰ چهارشنبه ۱۷ تیر'
تصاویر دریافتی از شهروندان
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/76860" target="_blank">📅 00:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76859">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پیام‌های دریافتی:
چغادک بوشهر رو همین الان زدن چند تا انفجار خیلی شدید
سلام ساعت 00:28 دقیقه چندین صدای انفجار در بوشهر شنیده شد
00:30 هوا فضای چغادک 15 تا صدای انفجار
همین حالا بوشهر زدن
حدود پنج تا شش بار خونه لرزید
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/76859" target="_blank">📅 00:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76857">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ur0F1rscttNu2TswTwnM8yoQ4wjB4x75_OiHQC1Vcu2xzLE56FDsisDrhdi6VnDo7laUs6vEeq3qxAcKWZj4xTcJ9x1KzBhEIRyO3hq9GuLVLYfLUg1aVzX9NAvNBwAGAKOA9ytp24TYcCgr0Q6E4XRPzEy_AURJ4oYn_2SjsKCX_gC9_X5ro9rYGaiiuto7VqthXcaqUbkCytgmy32pV0AKMJ7o8SxCUf0-WJxTsSJPP7tryrIyCJhJkX1crQki7vpKH7j8Qjp8R_5QC8fKKEoRa9lPwg39m6q1MeUaQGwGPM2OYcH2JJiztM1sjt_tZt8aVH_pAPuq_sp5oEHLmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2188a0f9f8.mp4?token=LGXdhwjLncchwJOP3-XTpZntqmQ1EUEjZBw8XyHV-VV_YFhaa6X8RpbCU_xNvOhPit1R95XA1ItJP3hny575f4MAfZIYL5t_5B7uP8o-hRG957q6AgMgXejofAHK3X0qGuO95KMC9Veis7YzqJxKXofxfxo1UX6A_4ZQVj7ZONGzWjgCfZW5KIw_jsLhoNQ1h8vKZA9sPFvMBnbCzZARmSRsH6-j0B6BH2llWhg0pqVgeiYvcCXVnbewXCYMQeWidhenNVTrsLXvcURYDAkfmmTwvoS1g0rnApSpGPZjtSEj4BQHtJSvoE7h1a-Ld9zWWQo85uNU1DNzpRRj-YOT1g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2188a0f9f8.mp4?token=LGXdhwjLncchwJOP3-XTpZntqmQ1EUEjZBw8XyHV-VV_YFhaa6X8RpbCU_xNvOhPit1R95XA1ItJP3hny575f4MAfZIYL5t_5B7uP8o-hRG957q6AgMgXejofAHK3X0qGuO95KMC9Veis7YzqJxKXofxfxo1UX6A_4ZQVj7ZONGzWjgCfZW5KIw_jsLhoNQ1h8vKZA9sPFvMBnbCzZARmSRsH6-j0B6BH2llWhg0pqVgeiYvcCXVnbewXCYMQeWidhenNVTrsLXvcURYDAkfmmTwvoS1g0rnApSpGPZjtSEj4BQHtJSvoE7h1a-Ld9zWWQo85uNU1DNzpRRj-YOT1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون ریاست جمهوری آمریکا درباره درگیری‌های تازه میان ایران و ایالات متحده، با تشبیه تفاهم آتش‌بس میان دو کشور به یک «معامله» گفت:‌ «توافق اولیه‌ای که ما امضا کردیم این بود که اگر آنها از شلیک به کشتی‌ها دست بردارند، محاصره [تنگه هرمز] را لغو خواهیم کرد، اما ۲۴ ساعت پیش چه اتفاقی افتاد؟ آنها شروع به شلیک دوباره به کشتی‌ها کردند.»
آقای ونس با تاکید بر اینکه در صورت ادامه شلیک به کشتی‌ها در تنگه هرمز آمریکا ایران را نابود خواهد کرد گفت: «حالا، رئیس‌جمهور ما گزینه‌های زیادی را در نظر دارد. بدیهی است که من نمی‌توانم بگویم امشب چه اتفاقی خواهد افتاد، اما رئیس‌جمهور خیلی ساده به آنها گفته است، تنگه هرمز باز خواهد شد. این بدان معناست که نفت و گاز به سمت مردم آمریکا جریان خواهد یافت. به همین دلیل است که می‌بینیم قیمت نفت و بنزین شروع به کاهش کرده است.»
او گفت که تاکید ریاست جمهوری آمریکا بر باز ماندن شریان حیاتی مهمی در حمل انرژی جهان است و «این چیزی است که ایرانی‌ها باید بدانند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/76857" target="_blank">📅 00:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76856">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان شش انفجار در بندر جاسک
ساعت ۰۰:۲۴
سلام وحید جان جاسک رو زد دوبار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/76856" target="_blank">📅 00:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76853">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HwHi0_CZU6latmPCLkZSleHR_9z47TZ73OPng8aI7GvRMFds4apViHXOshAHxZFwGpgC3pZMxJLmP4jq1KDPpTvQvMghd27k1N0_Jn7xxs_CNnddHEXSKynWH5cLvCiD8yPxMtf--NOscQ4MD9zBDjnNP-596sucV9f0nOpHsPJQtPuUhEjmvd2CSUWdvmUJXB4bE3Vv661BbZPLL6HtDqHRzWaBy5scR6H-KYnagfZALn35h4qKl-xh61HgHZ45QY6_Uy5uTIjSEJJPlXpEHLoBdUJ0ioNjd_NWbVJqRxwveswGbF2iKmtvx21bP8bs_QzM3tS2SFshpKcQolr9Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8512e0af1c.mp4?token=n7RRC_iGSET3UWJwl9XdbSrHJbPGfn9il50YcqH6SdWwYA45-twJ7iqSCRUuh8QkYDCcd0YZSfAuqxtG7AnhxjEo0-EYyQhbACPN0QM2XcfxmcWYqb156F4W1-HE0FSIn0Ldeu4vFliARsHMSZMPumP13czcNqpAXWbgIAfdauSEpshN4cw4fEN-vZOsgXv_C5m_NEZ3AZssSfuEhHzUcLl7BIMBbAWQIfZOm22b1Z5eEJMtzexLWyYW-vU8S_Kh1ccisUmKLO-st8mmxkWu8qF6VG_1v5LCiJVwpjrLW7dr7iy_oxyxNIXoXX5FVOK4ZsyaPjRMwTKBj5KPwrWfGw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8512e0af1c.mp4?token=n7RRC_iGSET3UWJwl9XdbSrHJbPGfn9il50YcqH6SdWwYA45-twJ7iqSCRUuh8QkYDCcd0YZSfAuqxtG7AnhxjEo0-EYyQhbACPN0QM2XcfxmcWYqb156F4W1-HE0FSIn0Ldeu4vFliARsHMSZMPumP13czcNqpAXWbgIAfdauSEpshN4cw4fEN-vZOsgXv_C5m_NEZ3AZssSfuEhHzUcLl7BIMBbAWQIfZOm22b1Z5eEJMtzexLWyYW-vU8S_Kh1ccisUmKLO-st8mmxkWu8qF6VG_1v5LCiJVwpjrLW7dr7iy_oxyxNIXoXX5FVOK4ZsyaPjRMwTKBj5KPwrWfGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'بوشهر، چهارشنبه ۱۷ تیر حدود ساعت ۲۳:۴۵'
تصاویر دریافتی از شهروندان
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/76853" target="_blank">📅 00:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76852">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f98b02764.mp4?token=u2UWxZG1GaqEDzbEoQjBIN0Jiq12UCCG4Wh39CtWMS4abOPRluJJrfs0T6SfgNl02-CPqvs-UQB3DZfY8v0fiuBoPIYBipP9Y4HfAfdApQloei6nDEsyT1-yxRiYGpuJ0J908iNA9tLHxXhkf--hAGiO8scipKZtBlxi5GVvNWmTBOrhtqfDu69bNTFf8V1gqC8LgxY_Gus9XeIOweB0yuxFU2_eJHIEGsrR44vftUqglyCUOBfzTzpTiS34X6ys0FUnbwgt6IgJNUocJ8zdhQ4Llk7mkal627JQaZOi3Ggdzowc-YOpSNUB763tFndXDuOYcPN1G6LNkLruFA326g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f98b02764.mp4?token=u2UWxZG1GaqEDzbEoQjBIN0Jiq12UCCG4Wh39CtWMS4abOPRluJJrfs0T6SfgNl02-CPqvs-UQB3DZfY8v0fiuBoPIYBipP9Y4HfAfdApQloei6nDEsyT1-yxRiYGpuJ0J908iNA9tLHxXhkf--hAGiO8scipKZtBlxi5GVvNWmTBOrhtqfDu69bNTFf8V1gqC8LgxY_Gus9XeIOweB0yuxFU2_eJHIEGsrR44vftUqglyCUOBfzTzpTiS34X6ys0FUnbwgt6IgJNUocJ8zdhQ4Llk7mkal627JQaZOi3Ggdzowc-YOpSNUB763tFndXDuOYcPN1G6LNkLruFA326g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: 'چابهار، چهارشنبه ۱۷ تیر حدود ساعت ۲۳:۳۰'
لحظاتی پس از حمله آمریکا
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/76852" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76851">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان بوشهر ساعت ۱۱:۴۸ دقیقه بد زدن
بوشهر ۲۳.۴۸ یک بار انفجار
سلام وحید جان
بوشهر ساعت ۲۳:۴۸ صدای دو انفجار اومد که از صداهای صبح شدتش بیشتر بود
سلام بوشهر الان صدای انفجار اومد
اقا وحید بوشهر همین الان زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/76851" target="_blank">📅 23:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76850">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پیام‌های دریافتی:
صدای انفجار بندرعباس
باهنر
بد داره میزنه
بندر دوتا صدای انفجار امد
بندرعباس منطقه ۴ انفجار های شدید و پشت سر هم
بندرعباس ۳ تا انفجار پشت هم 23:45
سلام الان ١١:٤٦ دو انقجار با موج بلند در بندرعباس
بمبارون بندرعباس شروع شد وحید جان
ساعت ۲۳:۴۷
اقا وحيد الان بندر عباس صدّا چند انفجار شديد كه پنجره ها لرزيدن
ساعت 11:45
چند صدای انفجار بندرعباس ساعت 23:46
سلام صدای سه چهار تا انفجار شدید بندرعباس اومد
بندرعباس الان چندین صدای انفجار پشت سر هم اومد
سلام
23:47
صدای 6.7 انفجار از دور
قشم
سلام بندرعباس صدای انفجار مهیبی اومد
بندرعباس سه تا انفجار پیاپی و مهیب
صدای بیشتر از ۸ تا انفجار این سمت باهنر و اسکله اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/76850" target="_blank">📅 23:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76849">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p7hjoskKMAIU4GZRg4RQQ--C7lUjGh5PlB8UI92QwjezsGTP9yYwnHH5EkAfB_gWicEbGIuG7qJRv-7XpVB1lEG3yuEcmYCS-_AJ0tPkdUp26rE-amvkjk5mUeng1rZp5vYsJeSxYTu2TYd9MKjUWPn96Ym97Ubh7S4o2lLQEdiFIGbGH27wTV5Rh12tQVH8O799SFl3hBX1KW0GXc4MqEqbetA4N7BFFFfxo2MCM_k2h1oKvtJSy1vTXHhvJDT0PnhXKdd6zHM8BeyE6_zdWxUQm8IzgiDnt5YitUTnYv0m2hhNyMvzFgugPv7yBC-91Pd-NSuPj223Rexfa5SW-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام ترجمه ماشین:
به دستور فرمانده کل قوا، نیروهای فرماندهی مرکزی آمریکا اجرای حملات تکمیلی علیه ایران را آغاز کرده‌اند تا توانایی این کشور برای تهدید آزادی کشتیرانی در تنگه هرمز را بیش از پیش تضعیف کنند. ایالات متحده ایران را بابت تعرض بی‌دلیل اخیر علیه کشتیرانی تجاری و خدمه‌های غیرنظامی که آزادانه در یک آبراه حیاتی بین‌المللی تردد می‌کنند، پاسخگو می‌کند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/76849" target="_blank">📅 23:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76848">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
صدای انفجار چابهار
فکر کنم کنارک بود
چندین صدای وحشتناک  10تا بمب زدن
۵ تا صدای انفجار شدید اومد
چابهار
داداش الان چابهار رو هم زدن
7 و 8 تا صدا اومد
ما تو روستای رمین هستیم برقا رفت و صداش اومد خونه لرزید
سلام کنارک وحشتناک صدای انفجار اومد
چابهار زدن چند تا انفجار شدید
ما کمب هستیم واقعا درهای خونه ما بشدت لرزید
صدای انفجار از زمان جنگ هم بلندتر اومد
دود غلیظی بلند شده که تو شب هم کامل معلومه
از سمتی میاد که پایگاه سپاه اونجاست
البته ممکنه نقطه زنی باشه
الان 3 4 بار دیگه صدا اومد
جدا از اون اولیه
مجدد زدن با جنگنده
فک کنم اسکله سپاه بود چابهار بود صدا نزدیک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/76848" target="_blank">📅 23:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76847">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PpFSycqieWX7KC2ZT2YQz0fpE-4YaGyuE5SkE0um_jzTwO5H5Pd3wyYeUdLsoeBcbl-piO5sVHNs5iCqt1FVsHt4_SwyOtcTeX57DAbmjKzNBQfjUlSPQwTBbYgYtIcPpshzWlFeghbHSL392axdEN6t6ijWqeTf7e5ZmTxUgZy8liVqUfJj_qCmufJXZDxrGgUZDDgEQVMx_tBSbyzxMoGeBXI_mrgQqn2btnvCv3j5KftI0_TEsgKH79YSfnQ-umzqVukDQLD4c592Jp4I6vzmC5oVkeYJXqG_9jSsbhdDoiAx7RxESuDpFJQC28cYrra9SlvTR3sM_5BPMLRI_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری‌های فارس و مهر شامگاه چهارشنبه ۱۷ تیر گزارش دادند که حوالی ساعت ۱۱:۱۵ شب صدای چند انفجار در بندرعباس و شهرستان سیریک شنیده شده است.
بر اساس این گزارش‌ها، شماری از این انفجارها از سمت دریا و در محدوده ساحل غربی سیریک به گوش رسیده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76847" target="_blank">📅 23:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76846">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">(
⚠️
۴۰ دقیقه، ۸۰ مگابایت)
کل سخنرانی ترامپ در نشست خبری اجلاس ناتو با زیرنویس فارسی ماشین
دونالد ترامپ، رییس‌جمهور آمریکا، با اشاره به رهبران جدید جمهوری اسلامی گفت «ممکن است آن‌ها هم از بین بروند». او هم‌زمان تاکید کرد که درگیری با ایران طولانی نخواهد شد، اما واشینگتن در صورت لزوم به حملات خود ادامه می‌دهد.
ترامپ روز چهارشنبه پس از پایان نشست سران ناتو در آنکارا، در کنفرانس خبری خود از نحوه مدیریت جنگ با ایران دفاع کرد و درباره رهبران جمهوری اسلامی گفت: «آن‌ها رهبرانی داشتند؛ دیگر نیستند. حالا مجموعه دیگری از رهبران را دارند. ممکن است آن‌ها هم از بین بروند.»
او افزود: «ممکن است من هم کشته شوم، چون من هدف شماره یک آن‌ها هستم.»
رییس‌جمهور آمریکا در بخش دیگری از سخنانش با اشاره به تشدید تنش‌ها میان تهران و واشنگتن گفت: «فکر نمی‌کنم جنگ دوباره آغاز شود. آن‌ها چند کشتی را هدف قرار دادند و ما خیلی شدیدتر پاسخ دادیم.»
ترامپ تاکید کرد هرگونه درگیری احتمالی «خیلی سریع» پایان خواهد یافت و افزود: «هر اتفاقی که رخ دهد، خیلی سریع تمام می‌شود و فقط اوضاع را امن‌تر خواهد کرد، از جمله برای نفت. ما به دنبال یک درگیری طولانی‌مدت نیستیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/76846" target="_blank">📅 22:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76845">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGKDBV4OvZnSE9FO4X5HDn-NYOaWw83A4pdn6LmLIL_suuOWzhKVPJEreYv388ytNan2kpHRTBzb2A12ddpjKX0LGAQ-lD8odL5iAfc7LJnSL1nRhoS-OL-qTyFMZOKQZvPcfMiLlS5yY1ldwFPFJLBnRkxZcSxVZYbpkMxus-H0kIXAxgDEdU8mW3ZLtWtIIHJN329Yk5O_Cx04zwmjSpFDTKiOUTq-QQNcPRz1N0HWh5lzf_N4znI_KjNEsRXZl4uZJ_HiCrRKrYKvTaCEmnYqH__9ajxBvqnu_lpJzxOG9hhG_zbeLf30DBsTl6Fys4m18fud3Col1Puh-5ioMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی ارتش جمهوری اسلامی با انتشار بیانیه‌ای اعلام کرد که در پی حملات آمریکا به مناطقی در جنوب ایران، هشت تن از نیروهای هوایی و دریایی ارتش در بندرعباس و بوشهر کشته شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76845" target="_blank">📅 20:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76843">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VrJ4LaDjuNyMhzdT2cD7J8EpjXKM1tpTQhPh0oiXv0GLjQzvvjr0TGRrTUy1sOVIz_V0XXKNbNeo2O5InZFJAOj1lQqsHWB4gbf4_KglLh0JKU8-Scm7QGw0q5F43Ryxw0-lnpO7ijGTtxA4RRVh2fDwfMPKGIZo3BfI-DZ2eehS0fgah5PsGvICQxyMh9-UyALkE0EU9kGKuHEWj-c8KgFNFJlka-iqms2vvehxaP2jdasUCKSIBIKudtO-KMcB8Ql1qgXfSWCrsAHhQ5XF6wLCKc9yP7dBNhvNrn2zDaWf-nnaGak6iDxlug23n8boSCIigXU2xAq4nYe5E0GsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ffbf0a91d4.mp4?token=F52MeM9pTye-ffXehoa0Qk4FQlAcaikhAj9tS4E0mTvoaa4chjUfA0NmYxcrWKb_Yrx0fZ5Ss8z-Sl9juzYYl1MqP5vNX5bO-3-wTIqG-xNP4yoGX1ONTc2-mIYZ4ZuqM_3drmfV3WU9dVpUAb_jCQ-6gzlcpqJMQVjV4XKUDoxnFAAPI_2pAE7tzA6HD0kS-Oyf2w-cPtyhR2p2FNzjKzqvbJVAFjsXXPsOMCohJRVHUtcsMY0hr1bCfdUkovpElVBkCp6F6TO2r9apDyI3c4BUwwyWI4RAdB2T7SRLkaVR-2FMM9OUQ9SZQBkWQArwMmihv64fztuYn73riX7_xA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ffbf0a91d4.mp4?token=F52MeM9pTye-ffXehoa0Qk4FQlAcaikhAj9tS4E0mTvoaa4chjUfA0NmYxcrWKb_Yrx0fZ5Ss8z-Sl9juzYYl1MqP5vNX5bO-3-wTIqG-xNP4yoGX1ONTc2-mIYZ4ZuqM_3drmfV3WU9dVpUAb_jCQ-6gzlcpqJMQVjV4XKUDoxnFAAPI_2pAE7tzA6HD0kS-Oyf2w-cPtyhR2p2FNzjKzqvbJVAFjsXXPsOMCohJRVHUtcsMY0hr1bCfdUkovpElVBkCp6F6TO2r9apDyI3c4BUwwyWI4RAdB2T7SRLkaVR-2FMM9OUQ9SZQBkWQArwMmihv64fztuYn73riX7_xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رییس‌جمهوری فرانسه، چهارشنبه در حاشیه نشست ناتو در پاسخ به خبرنگاران گفت حملات جمهوری اسلامی به پایگاه‌های آمریکا در خلیج فارس، توافق موقت را نقض کرده و تهران در انجام این حملات اشتباه کرده است.
امانوئل مکرون در عین حال گفت انتظار دارد نشست‌ها در چارچوب آتش‌بس ۶۰ روزه میان آمریکا و جمهوری اسلامی ادامه یابد.
@
VahidOOnLine
فریدریش مرتس، صدراعظم آلمان، نیز در حاشیه این نشست گفت: «ما به دونالد ترامپ گفته‌ایم که باید یک توافق پایدار با ایران حاصل شود، اما این ایران است که مسئول آخرین نقض توافق موقت آتش‌بس است.»
@
VahidOOnLine
دبیرکل ناتو، حملات تازه آمریکا به مواضع جمهوری اسلامی را «کاملاً ضروری» خواند.
مارک روته، پیش از نشست سران ناتو در آنکارا به خبرنگاران گفت وقتی آتش‌بس برقرار است و جمهوری اسلامی «عملاً آن را نقض می‌کند»، واکنش قاطع آمریکا اهمیت حیاتی دارد.
روته روز سه‌شنبه نیز گفته بود هرچند جمهوری اسلامی در حوزه موشکی و هسته‌ای تضعیف شده، ناتو همچنان باید نسبت به تهدیدهای آن هوشیار بماند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/76843" target="_blank">📅 20:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76833">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aCqPZ13oxGzXYQTqOnj4oJ-LzmJuoAuGyuhru4oDYMd5BsZ0bRvXnqDcMatP5tVJHgI7CDLL051VCQVc92lcNDno4Hm8A6Wok5rEPsFgCehU_LcG7Pm8h7-q5WdZpnWCcy7_UhrwfmI01--qDMrp-jVeaI0lQsvsBCvxrc1bbsgYZb8BIBuehenFVKHKofg2asOys5sUcUhdvzgkMcN_g4iVCep1qTipqhE0i976_PUcveHuppBDA6C71-7eyVxBe_qC2yYk6SzVC7uf4tWHDaOWLAktAmihdQsE44lTsoRnZOQYs-lRZaKvIyHbSn1i9ctB-fvN8frCitqie6MLLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ls1MW3D0gD_CxXE7pR1ntzCz1lQHtNimO8x_PSu6EO6_0c3L7yXBrLyC6h21E17bcvouT1NDslvXpShqikTOHbeOaQp0H8FwcKlXOSe7gtYShWaJr8JDX4ZHTxdhaVmaWv4F9mrX9OmxLohpxUV2jFJyllCgQPE2vWVERlIjPuVLWF9u2rJiinA9H1jHKy5x19L8PAtRetpk7yOjL82S5XnnsRbRfVTYkX3CyzrRJH72BFOyymnwX37cvVLV-MiwLOIPOoQ_D9Jjp_2mMiwAhimUY4NLdisj1CC8rpJT1F_6o_gHiOlawD5MZtTRlSD3vWWCw2D7hZxhvagLmglagA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JOQO2jHlwk0zQCY-eeZCtsi7Wfn-EiEwqxLaudMkychHiYa8eOEYSv1O_MBh9-AsIq-OiMGRxO76aw6Tch5ow56F_6PR3j80m4UEOpPm7KajgoNLW94fgXVy8mSoMT5NP7Bpf2hz9J_NKGiXtOeywZ5r6G_WPTdEJTnXMwnyI1lFxgu3SzI_gSNxJfDwK0KiU3iEITOMNbBiBN6KmX6QM0z0MPErFE6Z2jQ-kDMLBpbqZ0ZzJhqf-2nB9AL0cEfQD85s_U3yrt-DWk7fOLaR64ifRRHIs-lJ0CDG9lw7P2X4owtgptfaola-s0qNjFcxdEG9DtfGUkovQgU6Mqm0zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J2yiEuSqf-bqxPfwnZJSHZNm6XzmPzv3ULOMvd7Pz1_BaP6AFvc_8-dKbOTQ0nPBGFeq4W1GPYxPruytNcKD3jsFvqEQ1W0S6crca0t4XBPnCAd7EiDuYW2hFLkGqKvknk3gN_uZ3vTGkcj6C462RdKmvnqI9ymc-YlFjgMs25j30fLuz1x-3j3ji7Vpeip0WipQR6HtodC0Xlh2nGER7q2qLV_B6U0hvIKy-i144rV5ilrNzjxnwDXkqhIA6YOml3tcxTybh8zdrrX4U3e1VlPOVBK0m8IDd5vqKWJacUr9Rqo1VG0B-anvEfcfvXIWj3gITq07JZyHSXATskKn5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VOuy_DKIJFS6wsxuDQzxKv1OH1UVD5p0XjoJUidEdmdeZHBeneK0GQW-n6vmX2H24GkGSJzdUKu4g3q01t4fVhHO3Pb2QLqndjERL_7JnaAN6iAEy-GTjc0HKu4dgsyakj_AdtwqGU7yIjouqAyNakKQAYc_vl3wG-ge-8gdDfXtx301i9hOhbb8RxUaTci8vqMCSByNzFU3nleITR1tcAVkDM13pqpYKMJ-u0tdFRy-_f8s-AQIopB-LCKxcXQDOqE246CyzFUHQormVEkLoSzXX7rObYu8G63vu9VO2DnW1_KhaPd5i_keGNUB78HfGNvax_C8tORGnjVypBsmPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e6cd91b041.mp4?token=dDdqG30hpUIuKYSV9iRKzkAB7-lzCP5-LoLhbzgydpxMyB6zFHBibzTzH2yFG7IKS4b0_QiD5RNZNNpZ_siPAdFWUblnWsZUaNWp3XUgjAmiLTCgnbEjWGpmw-gTAM08YRc3jxiemTvy75FE6hWsx1cRkwUHv5b0DUGVmn5m2QxoN4v6Nx_fIuW-8PwSMhVweDttaVzM2Op-2URXgwqm0N69wMHAfzLAaJvfvdBAajB32-5Q72qrx9jBrhIC9BzVKkLzOQFu3IzA0kfNDCHJNygUYnXSghIhs37Up_XuzlX8irFTfseqEiYn_7TClCgYHoZmIeFwHUg6vpuw791H3w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e6cd91b041.mp4?token=dDdqG30hpUIuKYSV9iRKzkAB7-lzCP5-LoLhbzgydpxMyB6zFHBibzTzH2yFG7IKS4b0_QiD5RNZNNpZ_siPAdFWUblnWsZUaNWp3XUgjAmiLTCgnbEjWGpmw-gTAM08YRc3jxiemTvy75FE6hWsx1cRkwUHv5b0DUGVmn5m2QxoN4v6Nx_fIuW-8PwSMhVweDttaVzM2Op-2URXgwqm0N69wMHAfzLAaJvfvdBAajB32-5Q72qrx9jBrhIC9BzVKkLzOQFu3IzA0kfNDCHJNygUYnXSghIhs37Up_XuzlX8irFTfseqEiYn_7TClCgYHoZmIeFwHUg6vpuw791H3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، گفت ارتش این کشور احتمالا امشب دور تازه‌ای از حملات علیه اهدافی در ایران انجام خواهد داد.
ترامپ پیش از دیدار با ولودیمیر زلنسکی، رییس‌جمهوری اوکراین، با اشاره به حملات جمهوری اسلامی به شناورها در تنگه هرمز گفت: «آن‌ها چند پهپاد و یک موشک به سمت شناورها شلیک کردند، در حالی که این شناورها حق داشتند در تنگه هرمز حضور داشته باشند. به همین دلیل دیشب بسیار سخت به آن‌ها حمله کردیم.»
او افزود: «احتمالا امشب هم بار دیگر حمله بسیار شدیدی انجام خواهیم داد. فقط کمی از قبل به آن‌ها هشدار می‌دهم.اما باید ببینیم در نهایت اوضاع چگونه پیش می‌رود.
@
VahidOOnLine
دونالد ترامپ، رییس‌جمهوری آمریکا، با تاکید بر نقض مداوم آتش‌بس از سوی جمهوری اسلامی، گفت: «آن‌ها هرگز تحت توافق ما به سلاح هسته‌ای دست نخواهند یافت. اما نمی‌دانم اصلا توافقی در کار خواهد بود یا نه؛ شاید این مسئله را بدون توافق حل کنیم.»
ترامپ گفت جمهوری اسلامی «هر روز» آتش‌بس با آمریکا را نقض می‌کند.
او افزود: «آن‌ها دروغ می‌گویند، تقلب می‌کنند و آدم می‌کشند.»
ترامپ بار دیگر از توافق هسته‌ای دوران ریاست‌جمهوری باراک اوباما انتقاد کرد و آن را «یکی از بدترین فاجعه‌ها» خواند.
او گفت: «توافق ما دیواری در برابر دستیابی به سلاح هسته‌ای است، اما توافق او [باراک اوباما] جاده‌ای به سوی سلاح هسته‌ای بود.»
@
VahidOOnLine
رئیس‌جمهور آمریکا با انتقاد شدید از مقام‌های جمهوری اسلامی آنها را «بیمار» خواند و گفت ما به آنها گفتیم بروید و مراسم تشییع جنازه خود را انجام دهید. آنها به جای آن، دیروز شروع به شلیک موشک به کشتی‌ها کردند.»
دونالد ترامپ که در کنار مارک روته، دبیرکل پیمان آتلانتیک شمالی، ناتو، در آنکارا با خبرنگاران صحبت می‌کرد با اشاره به حملات هوایی شب گذشته اضافه کرد: «ما هم دیشب ضربه سختی به آنها ضربه زدیم، خیلی سخت.»
@
VahidHeadline
ترامپ گفت: «آن‌ها درخواست یک وقفه کردند. می‌خواستند برای مراسم تشییع جنازه خامنه‌ای بروند. من گفتم این فرصت را به آن‌ها بدهید. و آن‌ها دو موشک شلیک کردند. منظورم این است که این دیوانه‌وارترین کار بود.»
رییس‌جمهوری آمریکا افزود: «ما می‌توانستیم آن‌ها را بکشیم؛ بنابراین فکر می‌کنم باید از این زاویه هم به موضوع نگاه کرد.»
او همچنین گفت جمهوری اسلامی درخواست کرده بود که آمریکا آن‌ها را نکشد و افزود: «ما گفتیم قرار نیست شما را بکشیم. هیچ کاری نکردیم. در واقع، ما امنیت آن‌ها را هم تامین کردیم.»
@
VahidOOnLine
ترامپ در جریان نشست خبری در آنکارا، جمهوری اسلامی ایران را به اشتباه جمهوری اسلامی «ژاپن» خواند. او بار دیگر اشاره کرد که در جریان جنگ، جمهوری اسلامی ۱۱۱ موشک به سمت ناوهای هواپیمابر آمریکایی مستقر در منطقه شلیک کرده است. فرماندهی مرکزی ارتش آمریکا، سنتکام، پیش از این اعلام کرده بود که این موشک‌ها رهیابی شده یا به هدف نرسیده‌اند.
@
VahidOOnLine
ترامپ گفت که حملات اخیر ایالات متحده به ایران «تاثیر فوق‌العاده‌ای» داشته است. او گفت که در این حملات، سامانه‌های راداری که تهران در حال بازسازی آن‌ها بود، منهدم شده است.
ترامپ هشدار داد که آمریکا می‌تواند تنش‌ها را بیش از پیش افزایش دهد. او گفت: «تاسیسات تولید برق، نیروگاه‌های برق... اگر مجبور شویم، آن‌ها را از کار می‌اندازیم» و افزود: «تاسیسات آب‌شیرین‌کن... اگر لازم باشد آن‌ها را هم هدف قرار می‌دهیم. دلم نمی‌خواهد این کار را انجام دهم.»
او همچنین اظهار داشت که ایالات متحده می‌تواند جزیره خارگ، جزیره‌ای با اهمیت استراتژیک در سواحل ایران را «تصرف» کند و گفت که در آن صورت، ایران «هیچ کاری» نمی‌تواند در برابر آن انجام دهد.
@
VahidOOnLine
ترامپ گفت جمهوری اسلامی «هر روز توافق را نقض می‌کند» و به همین دلیل آمریکا «چاره‌ای جز ادامه حملات» علیه ایران ندارد.
ترامپ با اشاره به توافق آتش‌بس، گفت: «آن‌ها هر روز توافق را نقض می‌کنند. دروغ می‌گویند. تقلب می‌کنند. مردم را می‌کشند.»
رئیس‌جمهوری آمریکا همچنین با انتقاد از دولت‌های پیشین ایالات متحده افزود: «در ۴۷ سال گذشته هیچ رئیس‌جمهوری کاری در برابر آن‌ها انجام نداد.»
@
VahidOOnLine
ترامپ بار دیگر تاکید کرد که ذخیره اورانیوم با غنای بالای ایران، تنها به‌وسیله تجهیزات آمریکایی قابل استخراج است. ترامپ با اشاره به حملات تابستان سال گذشته، یادآوری کرد که این مواد زیر آوار تاسیسات و زیر کوه باقی مانده است.
رئیس‌جمهوری آمریکا، با تاکید بر این‌که نیازی به اعزام نیروی زمینی به ایران نمی‌بیند، گفت: «وقتی که آن‌ها کاملا از بین رفته باشند یا توافقی حاصل شده باشد، برای خارج کردن مواد هسته‌ای می‌رویم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76833" target="_blank">📅 20:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76832">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sHFO1ECHhEAMIyDnbWi7By5rsKEnNiWyTwDlBPqae8tPJ2crm4YBDs0iz7Xfh4kJTKCg_Pn_nZTXnIR8-JXODN5ZU53IW-4i6d2SFGbPqFTH_Ao852TvndQKtP26_lCRz7zE9CrTl8rLIzxinNGhGqUBowSJAF285WFBIFNSeQnMtZ8u7g6QmChXm2Y1FMicSpA9X-HLSbdcOqqWy21VpFCUPlI3o9IlAahsZP6Us6Zk5oxY6O2dSzvgOlclNmd06lDM5q18dWs4VfenkYtm7xhwU808-HBTvQrWuxHe4O4H2MUXV7jY0wU_1s6pejqK_8Cl_Y_UOcvYAwop5KLDkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عفو بین‌الملل هم‌زمان با گذشت شش ماه از سرکوب خونین اعتراضات سراسری دی‌ماه ۱۴۰۴ در ایران اعلام کرد با توجه به این‌که در ایران «هیچ چشم‌اندازی برای تحقق عدالت وجود ندارد»، دادخواهی قربانیان این سرکوب باید از مسیرهای عدالت کیفری بین‌المللی «به‌عنوان اولویتی فوری و غیرقابل مذاکره» دنبال شود.
دیانا الطحاوی، معاون مدیر منطقه‌ای خاورمیانه و شمال آفریقای عفو بین‌الملل، در بیانیه‌ای که این سازمان روز چهارشنبه ۱۷ تیرمنتشر کرد، گفت: «با گذشت شش ماه از زمانی که نیروهای امنیتی ایران طی دو روز، هزاران زن، مرد و کودک را به‌طور غیرقانونی در سراسر کشور کشتند، ناتوانی جامعه جهانی در برداشتن گام‌های مؤثر برای پیگیری عدالت بین‌المللی غیرقابل توجیه است.»
الطحاوی افزود: «این بی‌عملی به تداوم چرخهٔ سرکوب مرگبار کمک می‌کند؛ چرخه‌ای که در آن بازماندگان و خانواده‌های قربانیان از عدالت محروم می‌شوند و زمینه برای وقوع جنایت‌های بیشتر فراهم می‌شود.»
این مقام عفو بین‌الملل همچنین بار دیگر هشدار داد که تلاش‌های دیپلماتیک برای دستیابی به توافقی میان آمریکا و ایران نباید باعث نادیده گرفتن نقض گستردهٔ حقوق بشر در ایران شود.
به‌گفتۀ الطحاوی، مقام‌های جمهوری اسلامی تاکنون هیچ هزینه‌ای بابت استفادهٔ گسترده و غیرقانونی از نیروی مرگبار علیه معترضان نپرداخته‌اند و همین مصونیت از مجازات، آن‌ها را در تهدید به سرکوب‌های خونین بیشتر جسورتر کرده است.
به‌گفتهٔ سازمان عفو بین‌الملل، «با توجه به این‌که در ایران، به‌دلیل بحران ساختاری مصونیت از مجازات، هیچ چشم‌اندازی برای تحقق عدالت وجود ندارد، باید مسیرهای عدالت کیفری بین‌المللی به‌عنوان اولویتی فوری و غیرقابل مذاکره دنبال شود».
سازمان عفو بین‌الملل در بیانیه‌اش بار دیگر از جامعه جهانی و کشورهای عضو سازمان ملل خواسته است بحران حقوق بشر و مصونیت از مجازات در ایران را در صدر دستور کار خود قرار دهند، از ایجاد یک سازوکار مستقل بین‌المللی برای تحقق عدالت در مورد ایران حمایت کنند و از شورای امنیت سازمان ملل بخواهند وضعیت ایران را به دیوان کیفری بین‌المللی ارجاع دهد.
ماه گذشته، رئیس سازمان عفو بین‌الملل نیز نسبت به تداوم سرکوب داخلی در ایران ابراز نگرانی کرده و هشدار داده بود توافقی که صرفاً به‌طور موقت جنگ را متوقف کند اما حقوق بشر را نادیده بگیرد، خطر آن را دارد که به پوششی برای تداوم مصونیت از مجازات، اشغالگری و سرکوب تبدیل شود.
عفو بین‌الملل می‌گوید توافق ایران و آمریکا، موسوم به «تفاهم‌نامهٔ اسلام‌آباد»، تنها در صورتی می‌تواند به صلحی پایدار منجر شود که حفاظت از حقوق بشر، پاسخگویی عاملان نقض حقوق بین‌الملل، جبران خسارت قربانیان و تضمین عدم تکرار این نقض‌ها نیز در کانون توجه قرار گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76832" target="_blank">📅 20:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76830">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uutRbam-Ws1pzfh2r949CarvXgxN0GYB8Zu2_KtI3z1wbznNLMWkloNMsn1JNr9plyn9rp-HecyMuhqLoMDi4IX-AuuQRiSDKSOvVB0oZbziBA4XujpIvwL4tJUUzWIL4nyMQVZUHdf5bbxnrct4_Vks_zYd-nqx8MGbWEofO0WFbUa13Fb4a39Y2TZAbOlylKB8uEUVbBx7YLXSRQBDlQ-gyGw5j2tyhDeH_QqkXCJnwjdZq2EK84CMlw73Re4tLHLSKLx63sQP5wRlcSflvSLgjF2_BSCaj4MHQD15-CKQXE9k1OQ4zpiKkGEgzQDkYE94KVc2SLUULBsMA10ILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ja2vOOv_cUzyPP5XWviKnXTFCtgZnrSZI7Ckt4iw2p6gf8Zs0IICjly1Mu3urm99k6j9P8pOvlAPlb1VoY1oYZPdWgS_d3HcCUYauNLDJ9pk43TxCz9Mle8QfIx1ddOqKkX09GSxN80Zr1l-6Y-o2N-hoFJ0JlCYoKQKr0qfLM4nzUufTRxZQVwd2nW7SXA_ev_qWiCMx4-yCtQkZHFYYN7fs1rTd8jDkA8X1RZdjkcJBntgkBZWYecWrVqJ5y6Emto2OAKa89YyE9_YapGm0eUcapXArNoIsjbYoK84fUTr69FVs12kP3f-2YqfO1tG88Ukr1yZUuZX-m0HxVi9jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، با اشاره به مراسم دفن علی خامنه‌ای، گفت جمهوری اسلامی به جای حرکت به سمت کاهش تنش، حملات موشکی به شناورها را آغاز کرد و آمریکا نیز در پاسخ، حمله‌ای گسترده علیه جمهوری اسلامی انجام داد.
ترامپ که در دیدار با مارک روته، دبیرکل ناتو، در آنکارا سخن می‌گفت، اظهار داشت: «ما گفتیم بروید مراسم تشییع خود را برگزار کنید، اما آن‌ها به جای آن، دیروز شروع به شلیک موشک به سمت شناورها کردند. به همین دلیل، دیشب بسیار سخت به آن‌ها حمله کردیم.»
رییس‌جمهوری آمریکا همچنین جمهوری اسلامی را «بیمار» توصیف کرد و گفت: «آن‌ها بیمارند. یک مشکلی دارند.»
ترامپ افزود حملات آمریکا «۲۰ برابر شدیدتر» از حملات تلافی‌جویانه ایران بوده است و گفت: «باید سرطان را از بین برد.»
@
VahidOOnLine
مارک روته، دبیرکل ناتو، در نشست خبری مشترک با دونالد ترامپ، رییس‌جمهوری آمریکا، در آنکارا، از حملات شبانه آمریکا به جمهوری اسلامی حمایت کرد و گفت این حملات «کاملا ضروری» بوده است.
روته با اشاره به حملات آمریکا افزود: «این یک پاسخ بسیار قوی بود و من در این موضوع با شما هم‌نظر هستم.»
دبیرکل ناتو همچنین از مواضع کشورهای اروپایی از عملیات نظامی آمریکا علیه جمهوری اسلامی دفاع کرد. او این اظهارات را در واکنش به انتقادهای ترامپ از برخی اعضای ناتو، از جمله بریتانیا و اسپانیا، به دلیل محدود کردن همکاری نظامی با آمریکا مطرح کرد.
روته گفت: «می‌دانم که شما درباره ایران ناامید شده‌اید، اما به نظر من این‌ها مواردی استثنایی هستند.» او افزود: «پنج هزار هواپیما از فرودگاه‌های اروپا در حمایت از عملیات «اپیک فیوری» به پرواز درآمدند و اروپا به سکویی بزرگ برای نمایش و اعمال قدرت آمریکا تبدیل شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/76830" target="_blank">📅 12:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76829">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fc9ddafbb4.mp4?token=q_Ay7xp3cJhQFgjMF4IExvmEr6_qNiWPRJDacjyc3z51k-NsqnVYaNzP5vEjIqhqprP2DUEh6keHwNltWV5QaxSxqtNB9T28BfGPORYt0toPP4QsnRcA600kZtpDzdSxNc5Cl27T1kqm-HbWinAvEvIYo0EP5vc6ul7OV_a1BCMiXHiiRnj75LVHpnniJYPtVvWWriDupcZ99YfX2yvVwnroLQz1JTndILNOrQ0RdOsxCMp_uzJ49F6gMz7D9eR8Hgc-8cAp7hZWTPJMzpwuf4CXLhKRdX8lkJoerVO8haWDKRZLYXkRq-JIkIFqkJOmQ42_7Uo6JqTAfZr50e_I1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fc9ddafbb4.mp4?token=q_Ay7xp3cJhQFgjMF4IExvmEr6_qNiWPRJDacjyc3z51k-NsqnVYaNzP5vEjIqhqprP2DUEh6keHwNltWV5QaxSxqtNB9T28BfGPORYt0toPP4QsnRcA600kZtpDzdSxNc5Cl27T1kqm-HbWinAvEvIYo0EP5vc6ul7OV_a1BCMiXHiiRnj75LVHpnniJYPtVvWWriDupcZ99YfX2yvVwnroLQz1JTndILNOrQ0RdOsxCMp_uzJ49F6gMz7D9eR8Hgc-8cAp7hZWTPJMzpwuf4CXLhKRdX8lkJoerVO8haWDKRZLYXkRq-JIkIFqkJOmQ42_7Uo6JqTAfZr50e_I1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره مقامات ج.ا: یک مشت آشغال هستند!
نقل زیرنویس، ترجمه ماشین:
سؤالی دارید؟
ـ آقای رئیس‌جمهور، آیا آتش‌بس تمام شده؟ آیا آتش‌بس پایان یافته؟ آیا تفاهم‌نامه مرده است؟
سؤال بسیار جالبی است.
از نظر من، فکر می‌کنم [تفاهم‌نامه و آتش‌بس] تمام شده. دیگر نمی‌خواهم با آنها سر و کار داشته باشم. آنها تفاله‌اند. می‌دانید تفاله یعنی چه؟ آنها تفاله‌اند. آنها آدم‌های مریضی هستند. رهبرانشان آدم‌های مریضی هستند و آدم‌هایی شرور و خشن‌اند.
دروغگو هستند؛ ما توافق می‌کنیم. و اگر من با او توافق کنم، یعنی توافق داریم. و او بیرون می‌رود، حرف می‌زند. ما توافق می‌کنیم. همه موافقت کرده‌اند: هیچ سلاح هسته‌ای. ما توافق می‌کنیم. آنها بیرون می‌روند و با رسانه‌ها حرف می‌زنند. می‌گویند ما حتی هرگز درباره‌اش حرف نزدیم. یک جای کارشان ایراد دارد. آنها دیوانه‌اند.
آنها دروغگو و متقلب‌اند؛ مریض‌اند. آنها به مردم خودشان آسیب زده‌اند. تا همین حالا ۵۴ هزار نفر از معترضان را کشته‌اند.
می‌دانید وقتی مردم می‌گویند چرا آنها حکومت را سرنگون نکرده‌اند، نمی‌توانند سرنگون کنند، چون مرده‌اند؛ آنها را کشته‌اند. کسی سرنگونشان نمی‌کند.
آنها اسلحه ندارند و طرف مقابل مسلسل دارد و آنها را می‌کشد. رسانه‌ها این را گزارش نکرده‌اند.
اما آنها آدم‌های بدی هستند؛ آدم‌های بدی هستند. و صادقانه بگویم، نمی‌خواهم وقتم را با آنها تلف کنم.
حالا می‌گذارم مذاکره‌کنندگان فوق‌العاده‌مان اگر بخواهند به گفت‌وگو ادامه دهند، اما من چنین چیزی نمی‌بینم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 458K · <a href="https://t.me/VahidOnline/76829" target="_blank">📅 12:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76828">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vrR42HneTxHDrptstuD7qb_5_m4qSws_m4BNmT0IU8Ojb5edFMDNZShvQYgQSVTYUMhMDcBIhsIvE3Mi_k3Lz4xxsr3V1JgihmI31tNMfknbjgRoyjBGNnsmBFbgMiSVGLsCOQi6_3QizxyUbvChRhdzieWkOFIymI3EPnWyNsMnbBmZLDl22XoBN9obHsWx7fZ4nN291ZrXE1zkTOkoWacKVIZ9pIq4NtmYrcHLp9WjqJg70AHPz2BMrAeTQfe6_jKlHmqp2t8RsNxJJC5v3tJZCnZ04auKCyUYjtegPaOgv6U57b2pqky9xZ9ekMEv0O8gIFD62d6USFr78XP_LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست پزشکیان، ترجمه ماشین:
رفتار دولت آمریکا به‌عنوان میزبان جام جهانی همان سیاست خارجی آشنای آن را دنبال می‌کند: دستکاری قواعد، زورگویی به رقبا، مانع‌تراشی و تقلب. این همان دستور کار MAGA آنهاست. ایران چنین بازی‌هایی را رد می‌کند. ما قاطعانه پای حقوق خود ایستاده‌ایم.
drpezeshkian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/76828" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76827">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
‌
الان زد بوشهر رو ۱۰:۴۱
سلام وحید جان ساعت ۱۰۴۰ صدای انفجار شدید در بوشهر
سلام وحید همین الان ساعت ۱۰:۴۰ دقیقه صدای دوتا انفجار شدیدی توی بوشهر شنیدیم
سلام وحید الان بوشهر رو زدن فکر کنم پایگاه هوایی بود دوبار صدا اومد
بوشهر پنج تا شش تا صدای انفجار سمت پایگاه هوایی و دریایی ارتش
بوشهرو الان دوباره زدن
بوشهر یه بار حدود ۱۰:۳۰ دوبار زدن یه بار هم حدود ۱۰:۴۰، بار دوم نزدیک‌تر بود
ما پایگاه هوایی بوشهر هستیم
حدود ساعت ۱۰.۴۰   دو تا صدای انفجار اومد
دو سه دقیقه پیش هم دوبار
به نسبت انفجارهای روزهای جنگ معمولی تر بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 425K · <a href="https://t.me/VahidOnline/76827" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76826">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KPXL-K98aMkj2NsIYTr-3nBzvojGMS9MAZPotOs7PspWbKEvsGIGFcFJGAn82j66qkgXY8-HbVRHmfkfXNV5zVa5h2QNtkB4hZFNq9rbjKPY6K9vhSZ3HvMQzFYFmAmz9XR8S-EglrudqiEwAyMJuEptF2DhOcykeTcddFzaPgvW1v4Q7qrz_PSM3BysN6D2UxhdRfTbFB1HKjFh4K8nYRiMjWDAj_g3T5RElpxBhH-9OmZBrBH5hII5yzGrjPVnkeMW-HbhvY4XyMhcMn4w7NfrzJor1FkcmRqW8ALHrjtgzUmzgdKjkJulaPx-_kSRKxug7zIE77Ci-rY6oRwxiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: پاسخ دادیم
منابع حکومتی:
پاسخ اولیه به تجاوز آمریکا با هدف قرار دادن ۸۵ نقطه از تاسیسات مهم نظامی آمریکا
اطلاعیه روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
🔹
به دنبال حماسه سازی ملت بزرگ ایران در تشییع دشمن شکن و پرشکوه بی سابقه یگانه دوران و قائد شهید امت اسلام، رژیم متجاوز آمریکا که روز به روز ابعاد شکستش بیشتر آشکار می شود و بازتاب جهانی خیزش عظیم و میلیونی ملت سرافراز عراق در بدرقه تاریخ ساز رهبر مجاهد شهید را شکست بزرگتری برای خود میداند، بار دیگر عادت پیمان شکنی خود را تکرار کرد و وحشت‌زده برای تحت شعاع قرار دادن این رویداد تاریخی، ارتش کودک کش و تروریست آمریکا در ساعات اولیه بامداد امروز با تهاجم هوایی به تعدادی از پایگاه‌های ساحلی و ایستگاه‌های غیر نظامی در سواحل استان هرمزگان و ماهشهر به طور آشکار آتش بس را نقض کرد و تفاهم اسلام آباد را زیر پا گذاشت.
🔹
در پاسخ اولیه به این تجاوز نیروهای دریایی و هوافضای سپاه پاسداران انقلاب اسلامی طی عملیات مشترک موشکی و پهپادی، ۸۵ نقطه از تاسیسات مهم نظامی آمریکا در بندر سلمان، منطقه پنجم دریایی بحرین و پایگاه هوایی علی السالم کویت را در هم کوبیدند و یک پهپاد MQ9 دشمن که قصد دخالت در عملیات را داشت، سرنگون کردند.
و ما النصر الا من عندالله العزیز الحکیم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/76826" target="_blank">📅 07:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76825">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpfKq04BtIubNBuLNG9vXNpfSROlkq9d_pHQXO6f0kqUitiNaieTpF2Fl80h06axv9AxhhZ4VKthW98U0Lim3AQeYK1D-amCvx1It3OzAUYrHLWexrv5dClP5gvNEgt6qwQVkbJ23Xwu6R8pptfNCBUc8uKclmE2HvQPk9IpKLwxNFloAZaFRjQxjyfFIsbsptXDrDE66_pp2FiIdVFUtOpNmh179qbZaNCy0lLTKSDYfegePjDQZH_r4i5sPu-2dRvNM5CP087GWRriKwI8FIdqdzlTEw5V0xV8pSqOAaUYKJ0nb_mpc3h976_ksvAvPPYDhHw2OjvKlmLKcwP-5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شوری اسلامی پس از حمله‌های بامداد چهارشنبه آمریکا به اهدافی در جنوب ایران در واکنش به حمله‌های دو روز گذشته سپاه به سه کشتی در نزدیکی تنگه هرمز در پیامی به زبان انگلیسی در اکس نوشت: کلیدی‌ترین موارد نقض تفاهم‌نامه ۱۴ بندی توسط آمریکا:
۱ - نقض ترتیبات ایرانی در تنگه هرمز
۲- تهدیدهای مداوم به حملات نظامی بیشتر
۳- حمله به مناطق جنوبی ایران
۴- بازگرداندن تحریم‌های نفتی
۵- استمرار حمله‌های اسرائیل به لبنان
او در ادامه این پیام نوشت: «دوره قلدری و باج‌گیری تمام شده است، راه به جایی نمی‌برید، ما اهل کوتاه آمدن و عقب کشیدن نیستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/76825" target="_blank">📅 06:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76824">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y6JspjlFc6qO1yjE4KinhBsYVM6Feal2vJZ62yNycdsVijetaABamAXBo_nHU9rbfCgAT_9Lfz_QQ9F_nDE9UcMiU_6kKqpC09RpWE2Le6Ctfxy4si5-TbAwFBvc8jr-kgDna7addttNvltdV5tI4tQUsqxd3OqVbspe6I43NoLcFD-jXvm3EWDCSIYOnZSec4obT2rgBXB2IGFpiBs11NealEkkzyKXUa0KxFuHzVyofdEyJ0v-2YFHDxdxcaR98el6J9wUWdc6YzBLwD9SA6FDXe-wJSX-sXCoi5cP8raJ_dH3K9WZF8U9VuhAyPu2PeaH6B3Op1wIJPqsMCZOWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
همین الان ساعت ۶:۲۷ چهار تا موشک داراب شلیک شد وحید
موشک پرانی همین الان داراب فارس
+ کلی چندی پیام مشابه دیگر از داراب و هم‌زمان پیام دریافتی درباره آژیر در بحرین:
Sirens again in Bahrain for the 2nd time just now
آپدیت:
ارتش کویت: پدافند هوایی در حال مقابله با حملات موشکی و پهپادی است
ستاد کل نیروهای مسلح کویت بامداد چهارشنبه اعلام کرد سامانه‌های پدافند هوایی این کشور در حال مقابله با حملات موشکی و پهپادی دشمن هستند.
در بیانیه ستاد کل ارتش کویت آمده است: «اگر صدای انفجار شنیده شود، ناشی از رهگیری حملات دشمن توسط سامانه‌های پدافند هوایی است.»
ارتش کویت از شهروندان و ساکنان این کشور خواسته است دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی نهادهای مسئول را رعایت کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/76824" target="_blank">📅 06:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76823">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e118ef7ca5.mp4?token=dA9NBlI8roTH_-Mg1AQ1eODV2i2aXBAbEW0ScZ1Vsi7mP2eUw61g6rW6A0tD3ThFAShrkQY1yBPCbXwQMjIG-stKDTr4vgvIxRvv0JdaNKCYyXuxR25vN3Nj8kxS5NPUc88SBW_YVrwYU1kXeg9hFQqsibuI9_ullv_hgxVKskmNevEZr_WAhRStgNQPOOkYAv_yyDpd5zl7-kGWYvFioPXQ7CiB8kvQAKFtY9eu_i8smBqLycJXS2i_3QeAhpnDN6aspm-F4mwU7KAZajv0DmwwkvXzqjgimeWeFa28WZmuOB12FMUQvNwfBbbVecdFr9b749NGLJn2uvS9mvQcSg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e118ef7ca5.mp4?token=dA9NBlI8roTH_-Mg1AQ1eODV2i2aXBAbEW0ScZ1Vsi7mP2eUw61g6rW6A0tD3ThFAShrkQY1yBPCbXwQMjIG-stKDTr4vgvIxRvv0JdaNKCYyXuxR25vN3Nj8kxS5NPUc88SBW_YVrwYU1kXeg9hFQqsibuI9_ullv_hgxVKskmNevEZr_WAhRStgNQPOOkYAv_yyDpd5zl7-kGWYvFioPXQ7CiB8kvQAKFtY9eu_i8smBqLycJXS2i_3QeAhpnDN6aspm-F4mwU7KAZajv0DmwwkvXzqjgimeWeFa28WZmuOB12FMUQvNwfBbbVecdFr9b749NGLJn2uvS9mvQcSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: بیش از ۸۰ هدف نظامی را با مهمات هدایت‌شونده هدف قرار دادیم
ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده آمریکا (CENTCOM) روز ۷ ژوئیه دور تازه‌ای از حملات تهاجمی علیه ایران را تکمیل کردند و در واکنشی فوری به تازه‌ترین حملات ایران به کشتی‌های تجاری در حال عبور از تنگه هرمز، بیش از ۸۰ هدف را با مهمات هدایت‌شونده دقیق هدف قرار دادند.
نیروهای آمریکا سامانه‌های پدافند هوایی ایران، شبکه‌های فرماندهی و کنترل، سایت‌های رادار ساحلی، توانمندی‌های موشکی ضدکشتی، و بیش از ۶۰ قایق کوچک سپاه پاسداران انقلاب اسلامی را در تنگه و اطراف آن هدف قرار دادند تا توانایی ایران برای ادامه حمله به تجارت بین‌المللی در این گذرگاه تجاری بین‌المللی را تضعیف کنند.
ایران اخیراً به سه کشتی تجاری در حال عبور از تنگه حمله کرده است؛ از جمله M/T Al Rekayyat با پرچم جزایر مارشال، M/T Wedyan با پرچم عربستان سعودی، و M/T Cyprus Prosperity با پرچم لیبریا. این تجاوز بی‌دلیل از سوی نیروهای ایرانی نقضی آشکار و خطرناک از آتش‌بس است و آزادی کشتیرانی را تضعیف می‌کند.
نیروهای سنتکام در موضع آمادگی باقی مانده‌اند و آماده‌اند هر زمان که توافق رعایت یا اجرا نشود، ایران را پاسخگو کنند.
CENTCOM
قرارگاه خاتم‌الانبیا: پاسخ کوبنده می‌دیم
خبرگزاری رسمی جمهوری اسلامی، ایرنا:
قرارگاه خاتم‌الانبیا: نیروهای مسلح جمهوری اسلامی ایران به تجاوز و اقدام تروریستی آمریکا پاسخ کوبنده‌ای می‌دهند
🔹
تحت هیچ شرایطی اجازه دخالت در امور تنگه هرمز و مدیریت آن را نخواهیم داد.
🔹
بی‌سابقه‌ترین رویداد و حضور مردمی در تشییع و بدرقه قائد شهید امت اسلامی، شکست خفت باری را بر استکبار جهانی و آمریکای جنایتکار وارد نمود.
🔹
ارتش تروریست آمریکا بدون هیچ گونه پایبندی بر تعهدات خود و در شرایطی که پیکر مطهر رهبر شهید مسلمانان و آزادگان جهان میهمان مسئولان و مردم سلحشور عراق می باشد در تجاوزی آشکار برخی از نقاط جنوب کشور عزیزمان ایران را مورد هدف قرار داد.
🔹
نیروهای مسلح جمهوری اسلامی ایران به تجاوز و اقدام تروریستی آمریکا پاسخ کوبنده‌ای می‌دهند و تحت هیچ شرایطی اجازه دخالت در امور تنگه هرمز و مدیریت آن را به آنها نخواهند داد.
🔹
مجددا اعلام می‌گردد تنها معبر ایمن برای عبور و مرور کشتی‌های تجاری و نفتکش در تنگه هرمز، مسیری است که جمهوری اسلامی ایران آن را تعیین کرده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/76823" target="_blank">📅 05:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76813">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tQlfASlYAcWvbt6BcLF7mUtWyj4HDjqiBiZPZtyZvjy1iz0PC-Ob8hiZp8zYlgsMgtySQSsV3toGN9wk6VcYXojAIkfiZ_hajaIfkc3Si0m818NRODfbJbn4yIi_5PrvWc3k9D0j17vYrIX_z4_87opwtl6GxVM4dDLaIWi0GJ0icQVQ0KOn3MgEipFASsuAQTPtYB5Un3EYJtdgWfdl9sMicpj3LSEepWgunl82jGiXdhGhvtPLIPnvCWR-OZMwq1RZe5nd7STQGYJeAnl-cKBEwuG-Ur-zs-0N0HDSaPtDqEDOik2yBk6jfHOr4ETPOLQxnwafa926TefSQ5njZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aoNJfsvT5NzlbkTuPEhO7YS_c0r7OTQ2evVRbI2_qfvty3UR2_ip1LUoc3W0pFAC1cYpc4-9crQm78ZMu40xmdzhXIuL37xoUzCy29gT1xuWg0w8XFsQojg3Ys5u-CZf-MTLXCHn-BVITi2lQXcDC1sGPv68aBlvr-lJju69J76K3172e02aN1nuDzv5jmNN1RS-CzAgaVoZ2MRDMSTjrlZOmn11OHl0NIs_XrH_2CMRK0YSCNgZf8ZdmrI7K-yR7NgrNR1XDEQoVURYCmbxw4edo4GNqELj5jh9JBmC-pWwMC_Ci8CmMLXty0eLvsq6k654waVC7h5M09-TTaIRWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Imy5AqdjDzRcyZ91cpuljK-caCSKX0Rq8RWrLeHZ98nlZkhL1wqkKr38oAPrf8h31BxZ7f-kXP9G_eMxHAjPjNIQCbrMI6cN2v_yWDKgNfi9_bpNV-i_T3If5xN6MxycPwjAVVpkfb5q5nmiqYDjamw8eA5ieIorda7od3-lieSnH1mIdKS-u_7jAbQNouRdHepjabezORVQnVbdtL1RHh3Yjx6wrEmbQH9J64zoi9D4sh74EXsyMMVj1gBmM_JuT_1zBWNh80GILC66F_wQ21fEyYek9IXJsEuUyKznH4Psg8jc2PTyRsypPyAVM_giQ2Pu8EbwksqYZJiJTHSHdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cqFy329vSmWnFow-rguOen8pwmYchd_gvhEf_rfBZhhTd_7rsrOcWiAbiuH3hbLtM8Oo1cTcnccSAZy_QQxF0xN7tVFbSBe2roxcBfb_kuyNxtsdfRPaqncEQHfqIwjcLk0WEI348VcrxSIkHDaf3_yDPGqpm8fNVApGPamLdvKhf91o5wxsf3OO24Iay8heDN_R-qAZ0hesgW3M-j-qM1d72zmJUGzWUqpHhRpMqgCaVm6NgHPFRCtoFHyv3SXNT5lEORSSwmdL9vGII7pCYWFpqDYPv7L0V9s9nPUa15KzXQz80yGIOG8l8S-YLSH28yy--1DN95QPH_rf33-Ozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XFNl_Ub9Xvi7p5j64gujxfseMMidivxGqDZrwDvuygELhk2EvCdjoDSXORs_a95315I449rvv5gsGpALOtCi1xC2FVSrAThLv8bZ5V2-VIJVK_QQIfRR7KRih6cPAv6YQbRBuygmGNDprtBkHLBIrT1KlYfyb3KEUYIru0xX9L88Xmon45U0rTQXwvZCYomQyxalLUqkRjWP8gECb9kCkpwF6OfyvS9sW75onao7Nzagz_oTIpnEhq3NRb1cYCR9Opyhk1UJ7B8aJRPDQnjlNc0H2Pc6-Jo4CitOuAnJgmxuIWsmzimdfpWjW7YsvWFKHAzYb2YihHgmhgg5VnRQqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/964f541742.mp4?token=IXVO3IpmSgfvjddtS_0oBzi6y9GPmSpEN4c3RgvhSP1cTbQFJCVaeLIERbRrSvhmgX5LeUe1a3hmX5SbDPfgIEAMW23tWBAo57R8G7Q7eMUOmF8a7CDoHeGBbb1OZXPpa0q2i2MeN_FHuldA2LNSXnr5sQ3nvZGgs_IzcDbzHmeSWuz_3tGX2xRQixojpOVLwWLAzOJGxS1K_qeLOThozHjM3GpkBKoH5eYHJCbO3_mCflvT-CqduIociK7IRkkExbH_FETFPTRSv8hz1LiLJkiiR9Uux2PY2qfKQTlguc1gA_RKuixhsB7V84yMuTq-tOl0IN_NhOx68JYir4sRWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/964f541742.mp4?token=IXVO3IpmSgfvjddtS_0oBzi6y9GPmSpEN4c3RgvhSP1cTbQFJCVaeLIERbRrSvhmgX5LeUe1a3hmX5SbDPfgIEAMW23tWBAo57R8G7Q7eMUOmF8a7CDoHeGBbb1OZXPpa0q2i2MeN_FHuldA2LNSXnr5sQ3nvZGgs_IzcDbzHmeSWuz_3tGX2xRQixojpOVLwWLAzOJGxS1K_qeLOThozHjM3GpkBKoH5eYHJCbO3_mCflvT-CqduIociK7IRkkExbH_FETFPTRSv8hz1LiLJkiiR9Uux2PY2qfKQTlguc1gA_RKuixhsB7V84yMuTq-tOl0IN_NhOx68JYir4sRWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکان نیوز تصویری از یک انفجار بزرگ در بندرعباس و ویدیویی از انفجار در سیریک، در پی حمله هوایی آمریکا را منتشر کرد.
@
VahidOOnLine
+ تصاویر دیگری که با شرح امشب پخش شده‌اند و من از درستی همه‌شون مطمئن نیستم.
اسکان نیوز گزارش داد که ستون دود از سمت پایگاه هوایی بندرعباس مشاهده شده است.
منابع حکومتی:
مدیر بنادر و دریانوردی شهید باهنر و شرق هرمزگان: دود سیاه در پشت بازار ماهی‌فروشان بندرعباس ناشی از اصابت پرتابه‌های دشمن به اسکله صیادی بندرعباس و آتش گرفتن تعدادی از قایق‌های صیادی مردمی است.
🔄
آپدیت:
پرس تی‌وی، شبکه خبری انگلیسی جمهوری اسلامی، از شنیده شدن انفجارهای دوباره در جزیره قشم و نیز چندین انفجار در جزیره خارک خبر داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/76813" target="_blank">📅 01:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76812">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rGbBjZHxthtyEC2J3lqNA9DOCiu3XeyUbnhGGnAVfde2NLIm2upOz24oJ9IN4M8GwRe4reGDHPxr_-LEyguHHJESVTPJ0YBW-TlL6IV8lwy_tWxM4V_wFuFViZN_2YYFyYCYzL8Aw_fV-YdWm6oFWoKYCeX7TRsA704Euuiz5zq02DcbGh87MYyADbWOjgXsDva5YxnR2mEJfIEvX4RHGjAQ56Xk9rqHllDX2sqZnnYuPV1iA_OeD9bE4DO6-L65_ZqIcsLcxs6tFsMJUiUbGJ9vQLEDQBBr9UJHuN0HEQM6GliG50yMZneTGOJv21bnFgK-GZhmVJlGIlUzyBlvFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی به اکسیوس گفت اهداف حملات شامل سامانه‌های پدافند هوایی، سامانه‌های پایش ساحلی، موشک‌های زمین‌به‌هوا، پایگاه‌های موشک‌های کروز ضدکشتی، محل‌های پرتاب پهپاد و تأسیسات بندری ایران بوده است.
به گفته این مقام، حملات امشب از نظر گستره و قدرت، چهار تا پنج برابر بزرگ‌تر از حملات مشابه آمریکا در هرمز، ۱۰ روز پیش، بوده است.
رسانه‌های دولتی ایران نیز گزارش دادند که صدای چند انفجار در شهرهای بندری بندرعباس و سیریک و همچنین در جزیره قشم شنیده شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/76812" target="_blank">📅 01:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76811">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mtSngceDU9sVQRVB1mIUTsNi0JY2yZKW3Ca6VBiONAP6cJmiOC6d2nT99YsQjg56nk7Cl7cXMYhqEdy1imXXeBhE7biJmP021kQti-asSgpeIkJ6uIxGWHbk54R-pJinjKMwJIJHroT4jb-NcYSXX9-JCOpV2apIBVIW4EC-1LZaDjGg2iDMx5nTBnTGrSCmaIVdsm0Nd8zVs5eWB9w8Dyi9Ciw9-kLBhvc1ooD4K8lXZVVQRTi7H8FuGBTrzJFjiJHm8T3h7_q71Xi2HUmOhtLGEv1RinJNkgzdvRUrIit8Cs9u1vk8rszLuNRrJZ3XeP_zGglSSahhAmpF7o-dTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه جمهوری اسلامی، در بیانیه‌ای، این که آمریکا اجازه نمی‌ده نفت بفروشند رو نقض تفاهم‌نامه خونده.
پیش‌تر امریکا هم
گفته بود
چون به کشتی‌ها حمله کردند، شایسته مجوز موقتی که صادر کرده بودیم نیستند تا رفتار مناسبی مطابق تفاهم‌نامه نشون بدن.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76811" target="_blank">📅 01:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76810">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rwxnKT-GrRLwY51tncNyA8DkVXWN07zuQc2rV-uN_sTqwd68Cz01O8zEM2ZL7tR1udU6rcgSdym1jxK3cDLz6ipRhj_QGCMUrJhO1n1ctdLjdTcFF6YdJGG1WkRpc4jiZBlzQqDROg3s0P-xwcmLmR1WNU7mxe2KYlxD09i1rXeo8i4vhMlX8MZp0samQJ-dzY1tNPFLrm8LO82RiH3w5Gv38gxQYye0pSn91MX0s6RGBH8OjSM24Kn-KuTXADAHJqWQv0bJYQBfP_OBPy6u3LbaMD6rcq6v_C7BNtyGIEIR5L70kKOOyhDUw6KS2JLETh1VbhUN1gXpe3EFNbYRLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای فرماندهی مرکزی ایالات متحده آغاز به اجرای سلسله‌ای از حملات قدرتمند علیه ایران کرده‌اند تا به‌خاطر هدف قرار دادن و حمله به کشتی‌های تجاری با خدمه‌ای از غیرنظامیان بی‌گناه در یک آبراه بین‌المللی، هزینه‌های سنگینی تحمیل کنند. حملات آمریکا در پاسخ به حملات ایران به سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند. تجاوز آشکار ایران بی‌دلیل، خطرناک و نقض روشن آتش‌بس بود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/76810" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76809">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پیام‌های دریافتی تاییدنشده:
سیریک، صدای چندین انفجار پیاپی.
جزیره هنگام الان صدای چندتا انفجار بزرگ اومد تعدادش ۱۰ تا بیشتر بود
صدای انفجار درگهان (جزیره قشم) میاد ولی صداش کمه انگار دوره به اینجا
سلام وحید جان بندرعباس صدای انفجار
قشم صدای چندین انفجار اومد
نفهمیدیم از کجاست
قبلش صدایی شبیه صدای هواپیما میومد
صدای دو انفجار ۱۲:۳۵ بندرعباس
سلام وحید جان
ساعت ۰۰:۳۲
ما روستای سوزا تو قشم هستیم
اول صدای جنگنده اومد
و بعدم صدای ۵-۶ تا انفجار اومد.
سلام ساعت 12:35 بندرعباس صدای انفجار اومد 4 تا.
سلام کشتی سازی بندرعباس خیلی صدا وحشتناک اومد
سلام بندرعباس ۴ تا صدای انفجار تا الان
آپدیت:
صدا و سیما:
شنیده شدن ۶ انفجار در روستایی حوالی شهرستان قشم
دقایقی پیش صدای ۷ انفجار در محدوده روستای طاهرویی شهرستان سیریک شنیده شد.
فارس:
دقایقی پیش مردم در حوالی سیریک و قشم صدای چند انفجار شنیدند.
هنوز محل دقیق و منشأ این انفجارها مشخص نیست.
🔄
آپدیت:
بندرعباس ۴ تا انفجار دیگه
دوباره ۴تا تا الان
شد ۸ تا ۹ تا ۱۰ تا
من مرکز شهرم خیلی بده
سلام وحید جان
ساعت 12.30 صدای 5 انفجار شدید ذوالفقار قشم شیب‌دراز  نزدیک جزیره هنگام
سمت پایگاه هوایی بندرعباس انفجار شدید همین الان
وحید جان سلام همین الان ساعت ۱۲:۴۷ بندرعباس چندین صدای انفجار پشت سر هم اومد لرزید
الان بندر عباس سه چهارتا انفجار بزرگ
درود بندرعباس ۱۲:۴۵ چندین انفجار پشت سر هم
همین الان کلی صدای انفجار اومد بندرعباس 00:48
سلام خوبی، همین الان بندرعباس صدای ۳ تا انفجار قوی اومد ساعت ۰:۴۵
بندرعباس چندین‌تا صدای انفجار پشت سر هم اومد
00/48 قشم پنج شش تا انفجار قوی
00.48 بندرعباس چند صدای انفجار پیاپی
🔄
صدای انفجار پشت سرهم بندرعباس 12:50
هنوز ادامه داره
یک سر دارن میزنن ۰۰:۵۰
مجموعا بالای ۱۵ انفجار
۰۰:۵۰ صدای ۹ انفجار دیگه هم با صدای شدید از سمت پایگاه هوایی داره میاد
بندرعباس ساعت.همین الان چند تا صدای انفجار پشت سرهم اومد۴۸دقیقه بامداد چهارشنبه۱۷تیر
سلام همین الان صدای انفجار پیاپی و نور نارنجی بندرعباس
بندرعباس رو همچنان دارن میزنن
👀
صدای انفجار و پدافند پی در پی بندرعباس همچنان ادامه داره
همین الان بندرعباس
صدای انفجارهای شدید، پنج تا شش انفجار
کشتی سازی بندرعباس، اطراف بستانو رو زدن
سلام صدای انفجار بندرعباس بیشتر سمت اسکله ساعت۱۲:۵۰چهار صدا سمت شرق اینجا صدا نمیاد سمت غرب بندر اینجا صدا میادسمت اسکله
🔄
ساعت 12:57 انفجار دوباره بندرعباس
بندرعباس ۱۲:۵۸ همین الان صدای خیلیییییی شدیدی اومد
خیلی تو شهر بود انگار
اقا وحید بندرعباس یجوری زد شهر لرزید
پیا پی اسکله باهنر داره میزنه پشت سر هم صدا میاد
ساعت 57 : 0 صدای شدید انفجار در بندرعباس
00:58 دو تا سنگین تر زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/76809" target="_blank">📅 00:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76808">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/umbpWVvGWZ8Q2gAh8bSUTdcUuHcvlYofjRpC77kUnStaeFf0gaVMqCHGw71fOvnRAYMJUGmEkyRLjv3_G_FDXbuWKJwh0AS1yThg95CH2InbeW71MvdQLdVOvXoGZ6IFqb_ufkqJeThpzmY1bxjtvcbHiTZXnWfG_A8bvbYrdO52MnStgq-pJgY4PIA0RnhO2yCwhc3AwNBBe8DuQmp0v2dcVE64NYii9MbvwkRzkWhzhP7ccglkkgRLpEO_RmnUvL0wvVL5GwltOm5G3oCUv-1ZDEU1NQkiml5IxjZu6hP2SSm0WJmNo7PKAT0VTWlPa86iFukBwnneN6k8EiblMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا معافیتی را که به‌طور موقت تحریم‌های نفتی علیه ایران را تعلیق کرده بود، لغو کرد و اقدامات جمهوری اسلامی ایران در تنگه هرمز را «کاملاً غیرقابل قبول» خواند.
یک مقام آمریکایی به خبرگزاری فرانسه گفت: «اقدامات ایران در تنگه هرمز برای ایالات متحده کاملا غیرقابل قبول بود و با عواقبی روبه‌رو خواهد شد.»
این مقام آمریکایی گفت تفاهم‌نامه واشنگتن و تهران «کاملا مبتنی بر عملکرد طرف‌ها است» و هشدار داد که ایران تنها در صورتی از مزایا برخوردار خواهد شد که «رفتار مناسبی» نشان دهد.
مجوز معافیت از تحریم‌ها که حدود سه هفته پیش اعلام شده بود، در ابتدا به جمهوری اسلامی ایران اجازه می‌داد به مدت دو ماه نفت خام و محصولات نفتی و پتروشیمی را صادر کند، تحویل مشتریان دهد و درآمد حاصل از آن را به صورت ارزی از راه بانک مرکزی وارد ایران کند.
اقدام آمریکا پس از آن صورت گرفت که بنا بر اعلام ناظران دریایی و دولت قطر و عربستان، در فاصله چند ساعت سه نفتکش، از جمله یک کشتی حمل گاز طبیعی مایع (ال‌ان‌جی) متعلق به قطر، در تنگه هرمز هدف حمله قرار گرفتند.
@
VahidHeadline
وزارت خزانه‌داری آمریکا مجوزی را که ۳۱ خرداد برای تولید، تحویل و فروش نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران صادر کرده بود، لغو و از روز سه‌شنبه مجوز عمومی جدیدی را جایگزین آن کرد.
وزارت خزانه‌داری آمریکا اعلام کرد مجوز عمومی X به طور کامل لغو شده و مجوز عمومی X1 جایگزین آن شده است.
بر اساس مجوز جدید، شرکت‌ها تا ۲۶ تیرماه فرصت دارند معاملات مجاز بر اساس معافیت ۳۱ خرداد را خاتمه دهند، اما
از ۱۶ تیر خرید جدید یا بارگیری نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران ممنوع است.
اوفک همچنین اعلام کرد هرگونه پرداخت به اشخاص یا نهادهای تحریم‌شده باید به حسابی مسدود و دارای سود در ایالات متحده واریز شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/76808" target="_blank">📅 22:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76807">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BB4DmIdpzDUD_HqpEq2OVKRJfTZtUS3b-agXHM9kg-6IjdvMfoLt3qWwQDnzt_-2eC-PwbBWQCQQoV_5Kp1LvbRQau1rvsvSE3xMd9rh6J60FTEw_MrnWIPbuSFrMnXfeiRB8G9R9QTomBKqhz_O4vrBu1aPZVbnW1y1GY8ELvT3cAq2RSrsnll89wYO7ScJjrLwDFigd-Ym4GnfemNU3GXAlZn6y2t25ahp-aj2XVKEPZupu1V7i5vWvA-UUzKA4-dMPEv0uVZCO3xj4dtPBlFQXKXKJlL4b74AIFdlBhvBEqA7pQdFvK868k0Be1pDLWlvLiNObpK8yOKgtVqqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت قطر اعلام کرده است که در پی هدف قرار گرفتن نفتکش قطری در هنگام عبور از نزدیکی تنگه هرمز، کاردار ایران را به وزارت خارجه احضار کرده است.
در بیانیه وزارت خارجه قطر آمده است که این کشور حمله به کشتی خود را به‌شدت محکوم و آن را «نقض جدی ایمنی کشتیرانی بین‌المللی، تهدیدی مستقیم علیه امنیت عرضه جهانی انرژی و تخلف آشکار و صریح از قواعد حقوق بین‌الملل» می‌داند.
اعتراض قطر به ایران در قالب یادداشت اعتراض رسمی به محسن محمد قانع، کاردار سفارت ایران در دوحه و در محل وزارت خارجه قطر به او تحویل داده شده است.
وزارت خارجه قطر اعلام کرده که در این یادداشت از ایران خواسته است درباره این هدف‌گیری توضیحات فوری ارائه کند، اقدامات لازم برای جلوگیری از تکرار چنین حوادثی را بلافاصله انجام دهد و به‌طور کامل به قواعد مرتبط حقوق بین‌الملل پایبند باشد.
قطر همچنین اعلام کرد که این کشور تمامی حقوق خود را برای اتخاذ هرگونه تدبیر مناسب، مطابق با حقوق بین‌الملل، به‌منظور حفاظت از منافع و توانمندی‌های خود محفوظ می‌داند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76807" target="_blank">📅 22:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76806">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXxvmqZibDpKv5Fr53LQJ5zE6V5UKS6jHSA7z8P_n2PUTBt45hkJzW4PESnKpY78IjGy3s-lcwgG7X_bMwn6xhiBJUD_n6BUkhYwyZxTKVx8rHbCaQFLv1mXKFqcEJLNCJToxv8wEdkh1GquLz0hSF6DhR4rEVHotrDha97Ea4nBynHlZa-keeYmSlJRnKcT2RNwvNpU7yQ5qBaZR4aUdHs_0sMVFTlCs5fWTHCmmkbmvnpMabBCBxfJ5GHFaTWT-R8utXPcbCywoDxuCb65qPw2K8pAHeEo0ndR9PQoQcSHTPqtalcp4a3RXD3Jfedvhu3wKey3mcUOeFwKeLmAJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی، نماینده مجلس جمهوری اسلامی، در شبکه اجتماعی «ویراستی» نوشت: حالا که دونالد ترامپ در تیررس ماست و برای اجلاس ناتو به ترکیه آمده است، رسما و بدون تعارف، محل استقرار او را در ترکیه با موشک هدف بگیریم.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/76806" target="_blank">📅 22:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76805">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ez80WwdT1E6R33_W-NQTpZWErxMUfuyx-hbIUoG0qEQGw4wPbi-9xk5jecDrGFjxWwSe8ZH8klhaFjIsAHR9cIndsIpQjxh5VckTWLqdqiW2CxP0hXrDQjdE1ro6TQ_FNXyLyYZdHDIJOCD-KJVya47OZGy5IOGkpXr_E5LNhROyr5oUCi5ayF3rkuZ6I_UEvDQkNwEkZLPkbfbPLr956pkgjrOCBvgtByOpEw-2UC4MnIod-EQKUwFfup-eBJSLhSd5mQW3rCLLC6K-4Rh-VTBtS9BZsKFk-JDV9sBED4qkXlAL9_iISSkEo5X7Gr_mgo6i68Piv5MSYfgNb_szJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر اسرائیل روز سه‌شنبه ۱۶ تیرماه در گفت‌وگو با شبکه سی‌ان‌ان گفت که با وجود اختلاف‌نظرهای گاه‌به‌گاه با دونالد ترامپ، رئیس‌جمهور آمریکا، درباره ایران، آن‌ها در مسائل کلان مربوط به نحوهٔ برخورد با تهران «هم‌نظر» هستند.
بنیامین نتانیاهو افزود که هنوز زود است درباره آنچه پس از امضای یک توافق صلح موقت میان واشینگتن و تهران رخ خواهد داد، اظهار نظر کرد.
او اظهار داشت: «رئیس‌جمهور معتقد است که می‌تواند برنامه هسته‌ای ایران را متوقف کند»، اما افزود که در این باره تردیدهایی دارد.
نخست‌وزیر اسرائیل می‌گوید: «در مسائل بزرگ هم‌نظر هستیم و گاهی هم اختلاف داریم، اما متحدان واقعی هستیم».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/76805" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76804">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i2uc8lUAcA9jdp5oFUzidteRrxM6ZDgOVapaf2iMUwvkUF1gJQeN3PZUCWAvD8q0aN-Tekx8nN9pjDw5dDPLQopEDEn4ZOp_W3IHTG0hIi9Iz8mkdUbP74gDXQ20xdC2NDvaGonienwmQAmt1gMAWghN1P7Tcl2s2eKAlvZtuV4QdVlE6jlkX8KmN55RDFeiAeZmED-LwtnM1uWs3WHMcrQ0n_keyffKlbXoIdjvUEBImNi1B_ihM6SyolHfC7-MH4FRJMiXLmdCS6fCzn-swY6L3k7K2Ak8CxAuHGU77GG1JHjqanzIVL2BxOYU7irIRo1b43m3RRgpTKWCX_FRkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی، روز سه‌شنبه ۱۶ تیرماه، به ان‌بی‌سی نیوز گفت حملات جمهوری اسلامی ایران در ۱۲ ساعت گذشته «تهاجمی» بوده و «نقض مستقیم یادداشت تفاهم» به شمار می‌رود.
به گفته این مقام، ارتش آمریکا امروز چندین پهپاد شلیک‌شده از سوی ایران را سرنگون کرده است. او همچنین با اشاره به حملات شب گذشته به دو نفتکش در محدوده تنگه هرمز، گفت که جمهوری اسلامی در این حملات از دو موشک کوتاه‌برد استفاده کرده است.
این مقام آمریکایی جزئیات بیشتری درباره محل وقوع این حملات یا میزان خسارت احتمالی بیان نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/76804" target="_blank">📅 20:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76802">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HobfGWAhvV0mDDCvw_qD5YdcRbXiZQ7aYMeY77GgpP7ylzCj5oFQAdx1OqkVYoiLLSVikYkjPyeRKWAPRD4nVPdw6hX1dAcipP0taqXLAa_3OaNkh3b1tI7cY2u_REBRpI9w1ZcbVkMxoh3Jxd1FweUp3VMoMfHxi2t5CwYU8QIrAuePjwv5eODmGxSnYQt9ruGDRVNawV1qMXQ3sb1tSUxReMt4lGu37ODqXiHPLtqNSjP5btG_ZsKtfKXvt2wtGk0H4J_c-MCt6x4cp9JC9vGDriaP0fmqaGeZk5MgKigED8NqAtUH9SzU_PkEyZJsVwKRBwZP-YJm9Y-vXIgVXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d3c7d37bab.mp4?token=Zc5hf54uc597A9Cb7rF6kIHT4FJCindif0F87kwMzge7d0oWDwk3rOVQ2nE_gN1j54CUNQ8CXTzlze7gUONVrVj0BNH-WA29lT5NsBBNmfEHjBrMfJMmqorrocstBWwWpSUUWzLFmMwnv2S9lWo-MzS5FX3gLkv6JkBYcIQUyOZ46mDnnngBVOUTh065N_Zr2p-UnlNq1N-1nsuY_UKVIlUjzmuh-ShJAilcTczh8eahgdgSuy5Sy2ADrkWlw1Sj5OnGDbM8Y32__JrK5QxP2VBMCynaJGxxjujlJIoJhFAZrDczkchIHSYWXZO3ug_OYsIUFOIYAM5biPWV6gfyGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d3c7d37bab.mp4?token=Zc5hf54uc597A9Cb7rF6kIHT4FJCindif0F87kwMzge7d0oWDwk3rOVQ2nE_gN1j54CUNQ8CXTzlze7gUONVrVj0BNH-WA29lT5NsBBNmfEHjBrMfJMmqorrocstBWwWpSUUWzLFmMwnv2S9lWo-MzS5FX3gLkv6JkBYcIQUyOZ46mDnnngBVOUTh065N_Zr2p-UnlNq1N-1nsuY_UKVIlUjzmuh-ShJAilcTczh8eahgdgSuy5Sy2ADrkWlw1Sj5OnGDbM8Y32__JrK5QxP2VBMCynaJGxxjujlJIoJhFAZrDczkchIHSYWXZO3ug_OYsIUFOIYAM5biPWV6gfyGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه ۱۶ تیرماه در جریان سفر به آنکارا برای شرکت در نشست سالانه ناتو، در کنار رجب طیب اردوغان، رییس‌جمهوری ترکیه، بار دیگر از عملیات نظامی آمریکا و اسراییل علیه جمهوری اسلامی دفاع کرد و گفت این اقدام را نباید «جنگ» نامید، بلکه هدف آن «خلع سلاح هسته‌ای ایران» بود.
ترامپ با اشاره به نقش ترکیه در تحولات خاورمیانه گفت این کشور جمهوری اسلامی را «به‌خوبی می‌شناسد» و همراه با چند کشور دیگر، در تلاش‌ها برای پایان دادن به درگیری‌ها نقش مهمی ایفا کرده است.
او گفت اطمینان دارد رجب طیب اردوغان نیز خواهان دستیابی جمهوری اسلامی به سلاح هسته‌ای نیست.
رییس‌جمهوری آمریکا در ادامه با اشاره به روابط واشینگتن و آنکارا گفت: «این حتی جنگ هم نیست، یک عملیات نظامی است؛ خلع سلاح هسته‌ای ایران است.»
او همچنین با تمجید از توان نظامی ترکیه گفت این کشور می‌توانست وارد درگیری شود، اما چنین تصمیمی نگرفت.
ترامپ در بخش دیگری از سخنانش از عملکرد متحدان اروپایی آمریکا در ناتو انتقاد کرد و گفت از نبود حمایت آنها در جریان درگیری با جمهوری اسلامی «بسیار ناامید» شده است.
او اظهار داشت اگر نشست امسال ناتو در ترکیه برگزار نمی‌شد، شاید اصلا در آن شرکت نمی‌کرد و با اشاره به اردوغان، او را «دوست» و «رهبر بسیار قدرتمند» توصیف کرد.
رییس‌جمهوری آمریکا همچنین گفت ایالات متحده برای دفاع از اروپا در برابر روسیه هزینه‌های هنگفتی پرداخت کرده، اما در مقابل حمایت متقابلی دریافت نکرده است. به گفته او، در جریان تحولات اخیر عمدا واکنش متحدان را زیر نظر داشته تا مشخص شود آیا آنها نیز در مواقع لازم در کنار آمریکا خواهند ایستاد یا خیر.
ترامپ در این زمینه از بریتانیا، فرانسه، آلمان و ایتالیا نام برد و گفت مدت‌هاست این پرسش را مطرح می‌کند که آیا این کشورها نیز در صورت نیاز از آمریکا حمایت خواهند کرد یا نه.
@
VahidHeadline
رئیس‌جمهور آمریکا در عین حال تأکید کرد «ما به هیچ‌کس دیگری نیاز نداریم»، اما این پرسش را مطرح کرد که چرا آمریکا «تریلیون‌ها دلار در ناتو سرمایه‌گذاری کرده» تا از اروپا در برابر روسیه محافظت کند، بدون آن‌که چیزی در مقابل دریافت کند.
ترامپ گفت: «به نوعی داشتم دیگران را آزمایش می‌کردم تا ببینم آیا کنار ما خواهند بود یا نه، چون مدت‌هاست می‌گویم ما به آن‌ها کمک می‌کنیم، اما مطمئن نیستم آن‌ها برای ما چنین کنند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/76802" target="_blank">📅 18:09 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
