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
<img src="https://cdn4.telesco.pe/file/ZEA21uWy6n3MfH1OqXrKVl65sgu9XL6_bqYWCqkGc7j4DhF4U9ZDAr-X6uIjs-NY2vZq4_SMoIFm78M_pbg1GZJezDSAsKJkvRCEsv8rFmbg6x1hz_nTH4ktD0mXMyTEuQDbnyEmS9_xNrRfeK2zTctc5Ar9pnTzaBWclzCMmpe7aa9AhC8rTv953JKTKz_fNTXydGcCZHv-llZKFYIYDITjxENe727i_0ytX1-zoy-H6MuysUH_4gdc-WZUAKAtUXoKEjkZ5svIwz0FWxQmOY3kXzYuLf5l_5NgQprl8I4plqkmeOsMJyvhgZaiLK0w0q2Z4Dh890DUF-OQA0GrcA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 975K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-05 09:25:37</div>
<hr>

<div class="tg-post" id="msg-144010">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-T-Z8gsT0fDzkNJcT66NtCAzVbyVRhHtehDuN_WXKMM-fYHqduYv5p6ZdQmnS8KzqBUwE2-hQsQSIx00yr82Ebtl_PpSifwWdwe7ndGzhtBkRoT2j5qp4j3TzA-ClV0nbit_ACz67rloyEOL18P6OmP0hDHiEuoehiiJXcXMz1A4cbctOpNIpC9gzpySVXK1r7BHPQWP8xvaAyelNy5QHMRwBlOF00CnmGT5ATwDQ_vEoUeCaU8KHsmrAkP1QTPsbKF6Lp0PiuQVHufP-5-Y_qQ2qm-3DvW2sliEXyg_E7_I6tfxOtl3iup-XHA7hrBvoMopMv9qRLkxNS38Xna6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناو هواپیمابر «تئودور روزولت» به همراه ناوگروهش، در مسیر استقرار طولانی در خاورمیانه!
🔴
مؤسسه نیروی دریایی آمریکا گزارش داده است که ناو هواپیمابر «تئودور روزولت» و گروه رزمی آن برای استقراری بیش از ۷ ماه در خاورمیانه آماده می‌شوند؛ فرمانده ناو نیز خدمه را برای مأموریتی حدود ۸ ماهه آماده می‌کند.
🔴
این استقرار در شرایطی انجام می‌شود که حضور و عملیات دریایی آمریکا در منطقه به‌دلیل ادامه درگیری با ایران افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/alonews/144010" target="_blank">📅 09:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144009">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
آمریکا مدعی نفوذ هکرهای چینی به نهادهای حساس این کشور شد
🔴
دولت آمریکا ادعا کرد یک گروه هکری چینی به وزارت دادگستری، ناسا، بانک مرکزی (فدرال رزرو)، سنا و سایر سازمان‌های حساس دولتی نفوذ کرده اما با ایجاد اختلال مانع گسترش این نفوذ شده است.
🔴
وزارت دادگستری آمریکا روز چهارشنبه در بیانیه‌ای اعلام کرد دامنه‌های مورد استفاده در این حمله سایبری را توقیف کرده است
🔴
بر اساس مدارک منتشر شده،‌ وزارت انرژی، وزارت بهداشت و خدمات انسانی، مؤسسات ملی بهداشت و چهار شرکت ناشناس در آمریکا و کره جنوبی در میان اهداف هکرها بوده اند.
🔴
سخنگوی سفارت چین در واشنگتن اعلام کرد که اگرچه آنها با جزئیات ذکر شده در بیانیه وزارت دادگستری آشنا نیستند، اما دولت چین قاطعانه با همه اشکال حملات سایبری مخالف است و مطابق با قانون با آنها مبارزه می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/alonews/144009" target="_blank">📅 09:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144008">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
اینستاگرام شب‌ها برای زیر ۱۸ ساله‌ها قفل می‌شود
🔴
شرکت متا برای پایان دادن به شکایت ده‌ها ایالت آمریکا درباره آسیب‌های شبکه‌های اجتماعی به کودکان و نوجوانان، با پرداخت تا ۱۸ میلیارد دلار موافقت کرده است.
🔴
این شرکت همچنین پذیرفته به‌طور پیش‌فرض برای کاربران زیر ۱۸ سال روزانه دو ساعت محدودیت استفاده تعیین کند و دسترسی آنها را از نیمه‌شب تا ۶ صبح مسدود کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/alonews/144008" target="_blank">📅 09:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144007">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
هشدار یمن به عربستان سعودی: رویکرد فعلی هزینه‌های سنگین و جبران‌ناپذیری برایتان به همراه خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/alonews/144007" target="_blank">📅 09:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144006">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ان‌بی‌سی: حملات ایران خسارت بی‌سابقه‌ای به شبکه اطلاعاتی آمریکا در خاورمیانه وارد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/144006" target="_blank">📅 08:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144005">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
بلومبرگ: ژاپن به دنبال حمایت از احداث خطوط لوله‌ای برای دور زدن تنگه هرمز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/144005" target="_blank">📅 08:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144004">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiouK-ZBxpKULBYGRVIj_ufQd8IdLJTLlrNLhcdrMB_HFwXzeLZadEvvu0nqLBD_NMrXMDzxo3mCHbJOQ5_yFYOPxX6e--Y0CJM3ifSyLPlwZzxWkUyYtNHyVsJOaAZ02tWKuLf7fF6Bgi-bnEi75DEnrT83K29ojQf2RjHt2JOob0lhfVNGOHmTb93ajzj2vX_MJn3aSJb8foafkNnwjy4C3rlgNTriwMMyZtpa_eSOaRB8YP0M4J20FbcnPqJvKmOj5uyPg3ZzKpby_ypyoDj1BNqLRJaLR0EL_KAkOfIai9tF6GtcvAavN4yCObrHKOyK4z7hf4JQZ5TTMTbthA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
خالد شیخ محمد، که دولت آمریکا او را از طراحان اصلی حملات ۱۱ سپتامبر می‌داند، قرار است در ژوئن ۲۰۲۸، بیش از یک ربع قرن پس از حملات، محاکمه شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/alonews/144004" target="_blank">📅 08:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144003">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzD4nNLbzo6KAUi0mR-z6ng0vTCJBrpHqh8I2QKtM5KYSm3w_iQnEUWWISM_tpYRf9UuAxQUSfx-_UTlVP1z0JeAOgxdIb-Adz3Iw7FxLXcOOF7ckMMIeCcIO4_cV4fizp7I_cDIM8826lX02IhucEqehKAvhU9VrwhwjRcistyb2MsvJ4Ybt7hjhqWBZ1j7wVaG9cWuUs9sM5XObwcyCGq6Jpa8PCpoZprhMdZRYBER6exMEhldf4JK3nnbedSjQu8hRc8kgUsxf3_Se1lwRSsSjMwg1LZNSs_O3tjaDzK5Jmfylbn2qRo7xoNj_IwSfUQFeh1Qo7ZT45hDzlRYZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
اصابت پرتابه به یک نفتکش در تنگه هرمز
‏
🔴
سازمان عملیات دریایی انگلیس بامداد پنجشنبه گفت که یک نفتکش در آب‌های نزدیک منطقه «الخصاب» در شمال عمان، مورد اصابت یک پرتابه نامشخص قرار گرفته که باعث آتش‌سوزی در آن شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/144003" target="_blank">📅 08:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144002">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سخنگوی کاخ سفید در واکنش به سفر وزیر خارجه قطر به ایران اعلام کرد که هیچ مذاکره‌ای با تهران در حال انجام یا برنامه‌ریزی‌شده نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/144002" target="_blank">📅 08:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144001">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
کاخ سفید در بیانیه‌ای اعلام کرد که «دونالد ترامپ» رئیس‌جمهور آمریکا فرمانی را امضا کرده که بر اساس آن برای حفاظت از سیستم برق این کشور در برابر تهدیدات خارجی از جمله تلاش برای خرابکاری و حملات سایبری، وضعیت اضطراری ملی اعلام می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/144001" target="_blank">📅 08:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144000">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
کریس رایت، وزیر انرژی آمریکا: خواهان پایان دادن به برنامه هسته‌ای ایران از طریق مذاکرات و بازرسی هستیم. وی افزود: ما نمی‌توانیم اجازه دهیم ایران برای همیشه عرضه انرژی در جهان را تهدید کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/alonews/144000" target="_blank">📅 07:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143999">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb306c37b2.mov?token=TAQIRvSUdfwInbAx4SWfZUIQuY67DChtlBBDsf0gM3KTtwStiWxsYNCZQf7DSOSabQuKihcndHxUAdLMrcAvpQrLADWWrdl7HRjUToMKrWcbRl1s6LwC9dUMC5zK6ePU8ku5FU4rdwyUmZ-CiPZ7OctOiZTWFPuw1dDSYgIaqm40Cy81k3UVTVtZtJAM5BC3NsGY-Rb9fHLt6tcrNseF6RQ20RiHN-v4tHNSIqRACU6W49h97FnT68A6Ls6EhfCuLERFF-pI0hhP1YhjDxuruNU4KRm3FINJFVIBn7cMYnvsjb5xuGU9dkP3RpYiGLJawGHCpo6ypHIitGJ7MWzQqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb306c37b2.mov?token=TAQIRvSUdfwInbAx4SWfZUIQuY67DChtlBBDsf0gM3KTtwStiWxsYNCZQf7DSOSabQuKihcndHxUAdLMrcAvpQrLADWWrdl7HRjUToMKrWcbRl1s6LwC9dUMC5zK6ePU8ku5FU4rdwyUmZ-CiPZ7OctOiZTWFPuw1dDSYgIaqm40Cy81k3UVTVtZtJAM5BC3NsGY-Rb9fHLt6tcrNseF6RQ20RiHN-v4tHNSIqRACU6W49h97FnT68A6Ls6EhfCuLERFF-pI0hhP1YhjDxuruNU4KRm3FINJFVIBn7cMYnvsjb5xuGU9dkP3RpYiGLJawGHCpo6ypHIitGJ7MWzQqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صف عجبب پمپ بنزین در کرج|دیشب
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/143999" target="_blank">📅 07:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143998">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpPZLg9CHqIv6rtVhseTrCpNXslrUrVRmVhQRLmG7CyLAPqfM2h5fnvvutRdscO-Qov--boTKFvqTe8_q7sCe_2ugPxPPXdfn64bZIvtf0FUUamOBt8Kt4JYI7NGgmsVV3a2lbwfVFz4xpfnwE-kVdO6CEENoMZmOLuTeiCQdb_JR2TB6p_Z_ewravMIV-IH7Dq8yx604HRD_fZqwL8E8_ZJm2epyI9CdN7tnnPQNJ1K2mYhhzyMeczBVIzD52FiZZu27yKMvIIsW6bOaFaly1SCLGXDjvqVBDpG29ZTk0i4GG3idLvJsdtZ-RtenVfFjm4z_NkpwSg1GC8Q--bQlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👮‍♂️
مد
ا
رک رسمی تحصیلی «مقاطع متوسطه و عالی»!
✔️
از دیپلم تا دکتری | کاملاً غیرحضوری
✔️
قابل استعلام قانونی
+
قابل ترجمه رسمی
✔️
مناسب برای
:
مهاجرت
|
استخدام
|
ادامه‌ی تحصیل
ارتباط با مشاور
:
https://t.me/mydiplom_support
ورود به کانال :
https://t.me/+lHweVa-y92IyZDA0</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/143998" target="_blank">📅 01:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143995">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff574e553.mp4?token=oGk-DE3IJQxc4GpirRcWnfOVumP_BGih4djc8rksN3ZGZxAT_x4VT8VD3htsigtg64jHrAUnMnYldPC2oMufMpiiF01wGGQc32ZQadGEAKAfMyhPiIHiDAsop-hszpdjqbJfAd6wF8B6n-SO8OpAMZ5lgSBoHj3HAhFqlcPAAaGgpY-RqnsLxEpYn-JQ2Ge6Zh0wLh-dMVk42P_6O5iTXeafE6iHE5XX8qHkCCI7X5i_dSzY7j6p486zYcvzNOHu5b1AknXXrCLFQuMj5RQKAwB77plQeE0lXIi3tyJOIqIm35Xjnm1fJp_TUctzBZGP4_PJt5F9HJW7HgZN6r7VXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff574e553.mp4?token=oGk-DE3IJQxc4GpirRcWnfOVumP_BGih4djc8rksN3ZGZxAT_x4VT8VD3htsigtg64jHrAUnMnYldPC2oMufMpiiF01wGGQc32ZQadGEAKAfMyhPiIHiDAsop-hszpdjqbJfAd6wF8B6n-SO8OpAMZ5lgSBoHj3HAhFqlcPAAaGgpY-RqnsLxEpYn-JQ2Ge6Zh0wLh-dMVk42P_6O5iTXeafE6iHE5XX8qHkCCI7X5i_dSzY7j6p486zYcvzNOHu5b1AknXXrCLFQuMj5RQKAwB77plQeE0lXIi3tyJOIqIm35Xjnm1fJp_TUctzBZGP4_PJt5F9HJW7HgZN6r7VXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهروندان اسپانیایی ساکن منطقه "سئوتا" به ساحل "ترامپولین" حمله کردند تا مهاجران را بیرون کنند و اقامتگاه‌های موقت آن‌ها را تخریب کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/143995" target="_blank">📅 01:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143994">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHo1MmwmsSP7ffOC3iwOTPT58sr_r2t59LBE4vELm5DQErv9KTbzFwEaRl_aLR-xMEUMew1F19Ue_KnLPAzLsWDkQ7DJhgkTm-At01EwZiIlLSJfhh0L7keEJIzgncRCv1dxAW0zfsftS4CWQY078rXpA1qvuylTngX-UoTO3gIjfj07p_lcfKcxxu2nOUxJuYZuLPVWb8pVXfl6kh8TXgUY35ZvIdiWbCprSz_rO8NYLZRPxEAd31J9AOqGD2to44itS3ezhiFGikycBC9H3VXezh3JIWiufO822HTzsl6FrHTRlNWsw4WWkkY1kSxYorUuq_f3foQbMteFaDEMmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از سه‌شنبه هفته بعد هوای خنک وارد کشور خواهد شد و گرمای تابستان را خواهد شکست و در بعضی مناطق تا 10 درجه کاهش دما خواهیم داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/143994" target="_blank">📅 01:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143992">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
یک مداح مفتخور، بیسواد،دوزاری و پلشت: من با ۱میلیون اندازه ۱۰میلیون میرم عشق و حال، گرونیا الکیه و قانع باشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/143992" target="_blank">📅 01:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143991">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ec2c1a908.mp4?token=rRE5FvDg_26DIaMf30nsZgIi2B6-d89T-g9G6uXHO6HhrkTYFtgSVFbPSTR1nlzS08hDxpdVYzdeejTpmj5Jd8UcoEUm68reo-zhm-OYrc-REd86zHjAGUfFnGVZ92xE1qrbCcl2s3scGEEqow208tJQ1hFYF_gOGEQ5mpFfikQw9fFcCTJeJYvkrxgjtHKchfuhBw2Y6EAx26ldv7hZYUGNiTjTnSjf-_hZAct6-OBOPwgiwnux_vVPNMbjkMHpLlCHzn7Mjo136qamlSZ79FFDXqiDTBRpiCdbdJsye1cRK1SOmTkv1snSM5d59_RHyn-nqjQGoCC5HPz_quiRXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ec2c1a908.mp4?token=rRE5FvDg_26DIaMf30nsZgIi2B6-d89T-g9G6uXHO6HhrkTYFtgSVFbPSTR1nlzS08hDxpdVYzdeejTpmj5Jd8UcoEUm68reo-zhm-OYrc-REd86zHjAGUfFnGVZ92xE1qrbCcl2s3scGEEqow208tJQ1hFYF_gOGEQ5mpFfikQw9fFcCTJeJYvkrxgjtHKchfuhBw2Y6EAx26ldv7hZYUGNiTjTnSjf-_hZAct6-OBOPwgiwnux_vVPNMbjkMHpLlCHzn7Mjo136qamlSZ79FFDXqiDTBRpiCdbdJsye1cRK1SOmTkv1snSM5d59_RHyn-nqjQGoCC5HPz_quiRXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک مداح مفتخور، بیسواد،دوزاری و پلشت: من با ۱میلیون اندازه ۱۰میلیون میرم عشق و حال، گرونیا الکیه و قانع باشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/143991" target="_blank">📅 01:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143990">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏
👈
بلومبرگ:
وزارت دادگستری آمریکا در حال احیای «دادگاه غنائم جنگی» است تا بتواند نفتکش‌های ایران را به‌عنوان غنیمت ارتش مصادره کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143990" target="_blank">📅 01:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143989">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fff4810f1a.mp4?token=sAjFJWNf6RQFvmjdGbYY7OYZoFKy2akGqk-AuUkLOCZKyVMuvOfWb2noLenXa4kFzHjBVKiO-_wEkMYNPJqprw1ES8ce6sQoUbzD7_k4XwmcCEQsOwEjTBViW2LT64mIYeEYyrZHJv6g6Kjx26wECc_3t3L4zLzPSOj0jTadJKQyH5PlfNHIeVdF5wcB16pPkp8E4fDda8JESX_NOAgT_1l0gFHPfyc8QykCl4PnvzGv25QDqyUx76vYgOk23hQrvChmQRcBQ34HC3KYznlgcHDtQxnb7jaA1bWMnnvtcuda7hfe6JPjxDbg-qqtDIbpMbnfJJsm49baTORJKOfMBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fff4810f1a.mp4?token=sAjFJWNf6RQFvmjdGbYY7OYZoFKy2akGqk-AuUkLOCZKyVMuvOfWb2noLenXa4kFzHjBVKiO-_wEkMYNPJqprw1ES8ce6sQoUbzD7_k4XwmcCEQsOwEjTBViW2LT64mIYeEYyrZHJv6g6Kjx26wECc_3t3L4zLzPSOj0jTadJKQyH5PlfNHIeVdF5wcB16pPkp8E4fDda8JESX_NOAgT_1l0gFHPfyc8QykCl4PnvzGv25QDqyUx76vYgOk23hQrvChmQRcBQ34HC3KYznlgcHDtQxnb7jaA1bWMnnvtcuda7hfe6JPjxDbg-qqtDIbpMbnfJJsm49baTORJKOfMBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قیمت یخچال تو 3 روز 70 میلیون بالا رفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/143989" target="_blank">📅 01:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143985">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aFuzSsWR6NQ8cCF0lW9y5d7yK3y0SjlAlB09uvwsPVqNoV6ws2n81ulLpfGSNCLtzSZoGWyGN-C-FFfkauQy6dL7yfepH2Ol4DvN4-ID4Av5hEloSpdohC-qhTt7S7VHq_fw8_htlHacnSEwDZmEgyN_gzNA1YsbtvS-IGk05mv33vHp8t1fChyzUEg_rJRHfWMp1wpMxuqqQ6xqFmUsY23JaZk6BTEZaL1tJYlsHXAS8On82sdT8qEE0l9extIo13u1W_OzrCCFZHI9hwlbNb4ctiZ3jZnLQXwfHTkwdBjnQ0VUFeEusJzkUaeRhiruITHPgihHoIsEBlLnZwrEsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PD4OZ2mw551dUxGSjervyfM08obvu8oKGawCrgXvroPjyBf6ESu3y8UaNiGrWZC2W1aRSol-Rfd-kGchcFL6WQHPM27uJIrDxw2ZKvPqROp61PGM_laltfJ0zrQNEHGbHSlRJQK1pU5TYRQoR-i271jGSpKKZXqeXYfY6izWbM46DfH8xDuHLLawjo9gGTdtIdUioJVgodaw9FZN3aE_AJrLwzqMnirT5o4P-_V6xxezIITV8NI--YHm6DtKZo--jpbFITSftXQkL4WwpqqzkwKh_S_Sae2kKggqh66_eppcKFU8_p1Uhp9AcV6AHssv5i06CcGomggHvf4woFj7Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u3kpAakCBjAfxIX69OqM-UREc3xWQHkks1A0GYLJcsKykOVtkCpPCy8-QS-QZyogassPKf4LBJvY7lwbmXvHTvguquZQ_ywmrCU-3BN56U1i7LmDjagMr9d9ReadAP00aNkiRA2RM_snTvbzkCrXkmXC0BqZEOEeCMwc7lo8stGj3VNDIDritkHMi2RZvP7t9k6wrfuFUPrAYuzynnRu7AeYwqssjIoPsoCrm8PSbvpuAc0vfQroHXneCc9VDkN1ss3YPaP1g5zqIELkD-u3dmnzfw1H1700qOPh225XJfmWzLiit33ICFwe8zWJhoggQHrWz2LQU2k2mjiER1yxVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RnQarny6JjnmCfDU4SmQMn6rSUdhkuSydcw6e2fdx5TlgHoK-Us30kNHQGAO4PaaYoXtk_N67aH0dz4DXYZfoIPel3cO1iKM_oDtbym798HYio8R9YVQC2aX8wLfMCHZ_yMR4Sbf63agMCqSIEk2i-mO_0WAqPWdktpldPAJwh8Qc_jlc_QiLzOb5cBeSbhy6SrctiCIEdzdLa3QfhqJ_eArxEkVAML1p9pYRla8GrXoqJi3tEIRCJO6Yvv048egURPiJkJJ6kqYPtBB8nDBWBWsN_t-YcwPnhJbuluKx2Z3wkZzRhU-MalPDtqL3e1xd3EESIPSMMzP5ml9MVyyVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تو هفته های اخیر تعداد زیادی از دختر های ۱۲ تا ۱۸ سال تو مناطق مختلف تهران و کرج در حال ناپدید شدن هستن، از هیچ کدوم هیچ سرنخی وجود نداره و طبق گفته منابع خبری احتمالا بهم دیگه مربوط هستن و ممکنه حتی یک نفر پشت همه این ها باشه و همشون جاهایی که گم شدن هیچ دوربینی نبوده تا الان طی چند روز گذشته ۶ دختر با نام های :
زهرا متقی ۱۲ ساله چهار باغ البرز
ندیمه اکبری ۱۵ ساله پرند تهران
هلیا عین الهی ۱۴ ساله پرند تهران
زینب سون قوریی۱۷ ساله پرند تهران
آنیتا شفیعی ۱۵ ساله اسلام شهر تهران
پرنیان ۱۸ ساله فردیس کرج
گم شدن اگر ازشون اطلاعی دارین لطفا به خانواده هاشون خبر بدین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/143985" target="_blank">📅 00:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143983">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2_qqSOXVe4M1P04tkb9HvlIYqHxaYRiEErLOpcxrqGYjAVhHVmVp6ozBj-CzDqzf4oKoEqw9Tz-dMGKGQv99vaOcolpbSmhhnHwvwfi99WlqClqSPoOe-tRXRzG6zqVKw42UcOZQ4E-Jzv-IvtA9UPgE1dOyOxcVqsiovNkhlRCUzB0oRplY6BN_U_sOpLb9oD2roc9u4lgXrRkvNPXtuZjtD_PYMdKv4IRlaRbhFcPNerbOK7lBz-vKq-uZQ3dEp1CvOgY-ITo5-k8csru53tpHSJepM62TUYAukWn9JvlD-a0cYEWQbSBadpvpP2PwOywBi9XOwSZUvuStQyj4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a421747c71.mp4?token=BfM-46uWCrGBFNe23VYMiT6HGT5DXdyPrkT74Rw6hwN1MFlL8ZFcc1AfvIyJEWNFyjvzUJaJ1PvLTjpiU8nDJT4azCETj7g8fJ4nUQNpfoIBbvKVtVG77T0q-vba2CDIlewy5RBBbS1MrmUR_u5lhNl2WN5nzQz3NKcSJc-_Wt4CGBwwDZxGFaOxNTN9RLvHPsXsNTicBCJPFRwWFFYRl_a24cw2dq7gEUTwX5jffnh-XNmHnwQNNMJGqmpKjNO2U5JSCo5zaYGc6Dfbr_cH953EuVGM8HKbRQsa7Y9HogSivNcPJ4SVDM4MJbeWN-O9BBj3VluQK01ClpRFDkQtlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a421747c71.mp4?token=BfM-46uWCrGBFNe23VYMiT6HGT5DXdyPrkT74Rw6hwN1MFlL8ZFcc1AfvIyJEWNFyjvzUJaJ1PvLTjpiU8nDJT4azCETj7g8fJ4nUQNpfoIBbvKVtVG77T0q-vba2CDIlewy5RBBbS1MrmUR_u5lhNl2WN5nzQz3NKcSJc-_Wt4CGBwwDZxGFaOxNTN9RLvHPsXsNTicBCJPFRwWFFYRl_a24cw2dq7gEUTwX5jffnh-XNmHnwQNNMJGqmpKjNO2U5JSCo5zaYGc6Dfbr_cH953EuVGM8HKbRQsa7Y9HogSivNcPJ4SVDM4MJbeWN-O9BBj3VluQK01ClpRFDkQtlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله سپاه به اقلیم کردستان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/143983" target="_blank">📅 00:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143982">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
آتلانتیک» به نقل از مشاوران ترامپ: ترامپ از سرسختی ایران و امتناع این کشور از کوتاه آمدن خشمگین است
‏
🔴
دستیارانش او را متقاعد کرده‌اند که به طرح جدید فرصت بدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/143982" target="_blank">📅 00:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143981">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6Azer-pumTve5TnP_wMqYTFjp-F-b1lNrG0Lly-M4g4uuIvo4nzS2_l1io7olyavl05ZRxPp-WwoLXknqVA0TbB8lAwH1wqkCm-48DlfwfILTpAWsbc_vj-7MH94hvLl_l6eTk8bjYQKxiToZxrWQhbEJHa5sEv_ZYNsZn5lbCTZp76rOuX9TVeuCRGPY_MmbhYySDWAukDt6U6VqRscVuNzrDcPDD615QcITy7fgmY3FtE9aeaO7pORkuPMHeQ0V1-mOMMUG9WFfkhfx0Fy01Y7968BPQO1h1V6wGA-xhFW320BVv8ddKdFMqAF4GFognDhP-1XiLWPx7vkXk13A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صادرات نفت عربستان به آمریکا در ماه جولای به صفر رسیده و هر چند سابقه داشته در یک هفته عربستان صادراتی به آمریکا نداشته باشد ولی اینکه صادرات یک ماه صفر باشد در ۴۰ سال اخیر بی‌سابقه است.
🔴
براساس داده‌های کپلر انتظار می‌رود در ماه جاری صادرات عربستان به ۳۰۰ هزار بشکه افزایش پیدا کرده باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/143981" target="_blank">📅 00:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143980">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f654d70c1f.mp4?token=ibocldB1rTN-6cY8trYUmXBeusCORZXIhMFCyjwYuGx3eQx4_bycq8a3Au5cwJKVBrz9DxeTs3j4ab3YLFDnlolpHNZuTv_vkWS9b3KaA8gu2SxUxZABl1PTqYGB1yyRfnvnH1cfxnSXqXnrVWDRjpdE4Z5jFz6Tk8ZakP0ZwI_87P136qhfSBtYe30zEJcwZqhWR2SZzaEh0MZa8NOJUG4L8VTzQiHGy19NjI5KTtzzVs_RcLETmHFqKmxXgdCW5BP3-dIaErAQB1OuoGfxYG-vByOcwo5pB28B_YodcONtUE5XVbgJXhQ6Mj0rkzfzTPinW3Arp4vhMHjrWF9g0oeZjwfYXEcBe9qCuhsLxlxFCyfKJrRrB9uBGa6EQkhX69GfUQFfhp17fKOYtXzWZihHxFiPRWEZcqblSzf2nBSykRcYheaBUrKeXzsSOP9H1JLZy-luPPC_imv4vJJTH9A3cywcFtJWvXJLhmmQlHi1d64OK66DsOSnam8RYC6pThA8AOf4B9ShQruWNkkVosSaL44JR5JT0KEITRPfn8nNBc3pVsv6XkBliYdmmwWWhc2-_91psY5u0wYFST9_np1dVj37pY-q4c_1pjPyxnixV9dOetQT_kcXR8FmoRAzfxptlIw8PTRh5AvMMCO0cwI3CF-b5g-SGXPrJJe5oTs" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f654d70c1f.mp4?token=ibocldB1rTN-6cY8trYUmXBeusCORZXIhMFCyjwYuGx3eQx4_bycq8a3Au5cwJKVBrz9DxeTs3j4ab3YLFDnlolpHNZuTv_vkWS9b3KaA8gu2SxUxZABl1PTqYGB1yyRfnvnH1cfxnSXqXnrVWDRjpdE4Z5jFz6Tk8ZakP0ZwI_87P136qhfSBtYe30zEJcwZqhWR2SZzaEh0MZa8NOJUG4L8VTzQiHGy19NjI5KTtzzVs_RcLETmHFqKmxXgdCW5BP3-dIaErAQB1OuoGfxYG-vByOcwo5pB28B_YodcONtUE5XVbgJXhQ6Mj0rkzfzTPinW3Arp4vhMHjrWF9g0oeZjwfYXEcBe9qCuhsLxlxFCyfKJrRrB9uBGa6EQkhX69GfUQFfhp17fKOYtXzWZihHxFiPRWEZcqblSzf2nBSykRcYheaBUrKeXzsSOP9H1JLZy-luPPC_imv4vJJTH9A3cywcFtJWvXJLhmmQlHi1d64OK66DsOSnam8RYC6pThA8AOf4B9ShQruWNkkVosSaL44JR5JT0KEITRPfn8nNBc3pVsv6XkBliYdmmwWWhc2-_91psY5u0wYFST9_np1dVj37pY-q4c_1pjPyxnixV9dOetQT_kcXR8FmoRAzfxptlIw8PTRh5AvMMCO0cwI3CF-b5g-SGXPrJJe5oTs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرماندهی مرکزی ارتش ایالات متحده (سنتکام) که مسئولیت هدایت عملیات نظامی آمریکا در خاورمیانه را بر عهده دارد، چهارشنبه ۴ شهریورماه در شبکه اجتماعی ایکس ویدیویی از فعالیت سگ‌های نظامی در کنار نیروهای آمریکایی منتشر کرد.
🔴
سنتکام اعلام کرد این سگ‌های نظامی در سراسر خاورمیانه ماموریت‌های حیاتی مختلفی انجام می‌دهند و به‌عنوان نیروهایی مورد اعتماد، در محافظت از نظامیان آمریکایی در برابر تهدیدها نقش دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/143980" target="_blank">📅 23:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143979">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
فایننشال تایمز: اگر فشار های اقتصادی تاثیری بر مواضع ایران نداشته باشد، آمریکا حمله نظامی گسترده خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/143979" target="_blank">📅 23:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143978">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">💢
این تحلیلگره از تو کارگزاری پشت پرده طلا رو دراورده
منم پی‌وی تلگرامشو پیدا کردم بهش پیام بدید
براش بنویسید«
طلا
»
دو تا نقطه ورود میده همینارو بگیرید …
سیگنال هاش رانتی هستند عموماً
👇
@mahanmazandarani_pv</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/143978" target="_blank">📅 23:48 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143977">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fW5JRc8-VMtffQl0mTWrgHVmbEqVSOTCr-wbqA-C4KxiU5sP9vK23YtjyWIAcsZk_bsJ3WWV6AQEgszo6gX1u7GMmsmbKJHFfnDzKnPv_VN8VfbgzR5DBA14CapI4B5a9jk_DGrZgIsMY2hWXbKWcHd_J_IHaL4zh2aiY7clCP0lNEHI_IjHgyvDpgsMn2wSEJeyfJfuSZ6xN5pMoo_wdnj8n62YpunLPx7l3BCS3M_dYrQORFnuXgl62SSd5VwbuWStqWDrxC2GsI08dT6V6bcoXhz81enlmUZhURZwMrlmWbfbamUAHhQjOpYNXfBJxxd0Fy5hamWYOt3iMvRAdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سیسی ، رئیس جمهور مصر : نیروهای مسلح مصر برای مقابله با هر تهدید خارجی آماده هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/143977" target="_blank">📅 23:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143976">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
صداوسیما: صف‌های طولانی بنزین بخاطر شایعات کمبود بنزین و افزایش قیمت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/143976" target="_blank">📅 23:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143975">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
رئیس سازمان انرژی اتمی: ایران در جمع کشورهای دارنده سامانه گداخت هسته‌ای است و اکنون از مرحله اثبات فناوری عبور کرده و وارد مرحله ساخت سامانه و قابلیت‌‌سازی شده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/143975" target="_blank">📅 23:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143974">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
بلومبرگ: متحدان آمریکا به‌طور خصوصی هشدار می‌دهند که احتمالاً هنوز مین‌های ایرانی در تنگه هرمز وجود دارد؛ موضوعی که ادعای دونالد ترامپ، رئیس‌جمهور آمریکا، مبنی بر اینکه نیروی دریایی آمریکا آبراه را به‌طور کامل پاکسازی کرده است، زیر سؤال می‌برد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/143974" target="_blank">📅 23:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143973">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
پمپ بنزین‌های تهران وحشتناک شلوغه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/143973" target="_blank">📅 23:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143972">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmrbQr9uvKUWhmQShFKYflkAMXADx9159OHTXzn9ckSp93RkLLFy0kiGaQikvGEfOqQE0mma4o-NBWgvjOt00uVG796BlVNX_zia_-KlsQXk0O3uP-RdaVr6okEbpu6yc25cpmUFWqU7jCLGxnsIcwa5SDti4CqOGW3xIhjacy_VvNV_FYJKY1z3Q49FLODL5HKJdWWz8r4vtK5-mmkIjWyesWJLdKKeoAcrDlY2nbeSVZjhkI3BFGrli6Cpt3Pdhk7mQSf6VXCKzR85au16Dbe-FBBYC_zZSpnkWmULNwZhD-7LX1s0EqJrctUqxuhWobCW2lU5X5fGQFb5D6Jtjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زهرا پزشکیان، دختر رئیس جمهور، در پیامی به همسر رئیس جمهور آذربایجان، تولد او را تبریک گفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/143972" target="_blank">📅 23:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143971">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFhsjBafuUGQYlahD62GmOw32UPnC6-VI9KnUBk8Vxriv4UqfhJ34RHXMl_XnfCazWsdHRBpS7aoAzk_6mn4A72YA0pxWZ-tKlbfDBWKuoOJPQvAN65qkXS1000J-hZe7EnUpZaKidpJctdevjojVVFeAejcG5hZld5wZZtDbxPUvA9l-1SMmyvShlj_79ug7uHl87QMKNWN2n7b7txhaHnLdBOby4IuUkyAVyjbeT8h9bBW3z2NApI4EIvpFPmO35CeeF0SxFRoxjyOqAs59alnXbX0LlRe7t0cASnx1cyqjj0-Z8ZwuXfKfQVg0RfFB7EVG8xGHwoxp9Gox9CEvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه ایران:
آمریکا، ناو هواپیمابر «یواس‌اس آبراهام لینکلن» را برای نمایش قدرت به منطقه اعزام کرد؛ اما پس از ماه‌ها جنگ و بیش از ۲۰۰ روز بدون توقف در هیچ بندر، اکنون این ناو برای استراحت و تفریح خدمه، راهی تایلند شده است.
🔴
ماموریت: نمایش قدرت.
🔴
ماموریت فعلی: نمایش تعطیلات.
🔴
«من خسته‌ام، رئیس.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/143971" target="_blank">📅 23:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143970">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m8gWztXX-uLNI8tTWX16vYIXioA6lGgRghK8VS5qolVAQv4IJlJ_U6nHd80rVozB4h3LYDryfqu3FJPpZtoGXUmEJOXUtw2aGDWbxWZmpaYkCleE0h7EiG5UxdG90RKpiXoLLv5RYwjN4vCETGQTZTTbt-ejCz2Z9Yr9TV43EN1njvC-THzC1yPJmeiU9YIBrbQMz7CgOx37weL8Lcdxl5HizgrVt1UYJbffmssI_WkvPFsgUwtFgq-HTxyGVdxGha-5hGG9PcZn9fh6ba_JzeDdAweG9FEiyA9zbPM6npbXmjNlOx5fgGIEyoqv-mwbcB3MsPGDQJTx0frYyng_2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید علی کریمی خطاب به شاهزاده رضا پهلوی و تشبیه وی به قورباغه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/143970" target="_blank">📅 23:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143969">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
قائم‌پناه: توزیع بنزین در کشور عادلانه نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/143969" target="_blank">📅 22:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143968">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/143968" target="_blank">📅 22:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143966">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WHKT5ULV6Wa_ejiGNnSqpnXqCaRyPwUK7LNG-WblaiVYx_wy0b7K9u1IKn4fcyNC9VZ-WNm-RTHMQjVAAgavyavhy-0IP_vVcPuDe-tkYNcp3q9ldfM4jaaqheJWnQ7YT_vuTz8QG4qPUNqJbZQG5p_VwtTqpykyNr2ZKjcWcbQjwAUdl3u5WdLrD68CRLUqZoSpJtx-dx94k-7Y2kmvcL4izfS-JNqrezft1IfQ4fXAQibfap54y32p_1c5zIqQN7Rvzw-4uHbHCak6W86zQQK7MXBrA6q72A--JNN2yhofIiHcSl551-jQfZ5sM3ZX4riJgHpRWW3bWlT1zg3PZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oe0BT7nhbt5YT_Vilvnc6C31xCj6LJZV9KXAOGpN7KnkUsK8SettznqY6_1p33OYsmYF7pkYfsU2gusQVc9F1Shs0ftcelemtCYqV-VS0nfKE7m1mDvtb9MhGbVQlGAYUdSz_AGWMX3Hck8feoeKu3dlp01nUjAXKDLnEZP4JfvAux-iA3IHWzjO32SWuIJQYaaTJ0F_g4Lbpa-MCGrReTDz-8uPb2WEFzb-zzvYLRNMzRyKVTySMzLFbVuttFPIf20P1YAmyIl8WUS5dd5N7kvRLpq9U3G3baJzBZQ1SrraDxmtyHvEFksLhjK9ACwjW4NSDxTRaM0ROPDR05JCLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ناو هواپیمابر USS Abraham Lincoln قراره در شرق تایلند پهلو بگیرد تا خدمه ناو استراحت کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/143966" target="_blank">📅 22:51 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143965">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
جان رتکلیف، مدیر سازمان CIA پس از بازگشت از روسیه به کاخ سفید رفت و با مقامات دیدار کرد
🔴
در این جلسه، پیتر هگست، وزیر جنگ، و دن کین، رئیس ستاد مشترک نیروهای مسلح، نیز حضور داشتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/143965" target="_blank">📅 22:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143964">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
به گزارش بلومبرگ، احتمال دارد پوتین اوکراین را با سلاح «هسته‌ای» مورد حمله قرار دهد: به گفته این خبرگزاری، تعداد فزاینده‌ای از مقامات روسی به این نتیجه رسیده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/143964" target="_blank">📅 22:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143963">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: نخست‌وزیر و وزیر خارجه قطر در دیدار با مقام‌های کشورمان در روز پنج‌شنبه، درباره ادامه تلاش‌ها و ابتکارات میانجی‌گرایانه قطر و دیگر تحولات منطقه بحث و تبادل نظر خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/143963" target="_blank">📅 22:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143962">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: خواهان پایان دادن به برنامه هسته‌ای ایران از طریق مذاکرات و بازرسی‌های آژانس بین‌المللی انرژی اتمی هستیم
🔴
هدف ما این است که ایران از طریق مذاکرات، بازرسی‌ها یا استفاده از زور، تسلیحات هسته‌ای نداشته باشد.
🔴
ما نمی‌توانیم به ایران اجازه دهیم تا ابد امنیت عرضه انرژی جهان را تهدید کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/143962" target="_blank">📅 22:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143961">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
گزارش‌هایی از حملات هوایی اسرائیل به منطقه سِروبین در جنوب لبنان منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/143961" target="_blank">📅 22:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143960">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزارت خارجه قطر: وزیر خارجه فردا در تهران با شماری از مسئولان ایرانی دیدار خواهد کرد.
🔴
وزیر خارجه در تهران درباره کاهش تنش و فراهم کردن شرایط برای گفت‌وگو رایزنی خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/143960" target="_blank">📅 21:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143959">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzjOIy8U5HBmoxS0JVF6We61w0eqSFvTWNuO4Zc_x8xf8wDLxCfPRaU_wZib8Df1tU8G91KnMdeSARRlGROSzxN-3DkHri7NqpEfCErJNZn2oVMKW-zCcTJJ4kXpHDerDS0qDtSbN7KqsELd51a4eIzFpF4xo07aNo2DpR73sJGq9T3xG-zfG7XyPXtqhzg5W1--Ju9R_6Ui9-jDRo2O52p0BYO4lPj2kW0KHHkoBt0Vte5TJCEfBubT_W4mGqYtB400XtUmR0g4tAGYV3FK04ve2RO1eNk64bTtP2V51OYmMU-J9hMSuCKtzdpR31g4PSP9TUrsE6e18EJp5F1BgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش تورم مرداد به ۸۴.۴ درصد
‏
🔴
بانک مرکزی: شاخص تورم نقطه به نقطه در مرداد ۱۴۰۵ به ۸۴.۴ درصد رسید.
‏
🔴
این شاخص در ماه گذشته ۸۳.۹ درصد، و در مرداد سال گذشته ۴۱ درصد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/143959" target="_blank">📅 21:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143958">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZTl_ogeXRMYYevyApIw-7zIOY6FRB4SEPQ4MeoKggGZHK3bP4qLrdCmVx5n4U-vKnuTzs-9_yKkE9yB6oKjppvSEUuXMo39AotErWQBMS-oS6qgceN6cBFcL6AZpmFPkiiV8Bg5A3Y3yatk4LGqi_ClmZJY42t6tZv1ZYvDU4qZlNJKjorP5mK0pPLJ6NotZTPzTe2wLZpEhy9hw05aUkIxb0b0M1aLqGNWSovbkrhJHNhzQd7PcjjaqBopNv64z3_uA0Bo2cxhV6H4KK23VaJwPIIxghd3TNV60MVO3Xz4E97NSeG4mnU0kn3EtX2ns-_T5k5zLY0fHMRaL8VrGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: رابطهٔ راهبردی ایران و چین به اجازه هیچکس نیازی ندارد
🔴
از موضع اصولی چین علیه تحریم‌ های غیرقانونی آمریکا استقبال می‌کنیم
🔴
نماینده ویژه ایران در امور چین: ما از موضع اصولی چین در ردّ تحریم‌های غیرقانونی علیه ایران استقبال می‌کنیم.
🔴
شراکت راهبردی جامع ایران و چین بر پایهٔ احترام متقابل، همکاری برد-برد، و چشم‌اندازی مشترک برای جهانی چندقطبی استوار است. رابطهٔ این دو کشور نیازی به اجازهٔ هیچ‌کس ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/143958" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143957">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
سیلاب در نپال حدود ۸۰۰ مفقود و بیش از ۱۰۰ کشته برجای گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/143957" target="_blank">📅 21:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143956">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlq3vI9DWHPNV6LCaYvQtAnxKCgWm-smU6GMWUb3FgIJZrANGDDk-U13kyn-SAdebCBKOdlkLIfhARfJRidHuDG9FcdsRHp1-GQbmAL8VITmumDPq2T8Z3ars0DabIYMpx4bkbROMpPAAJC2oblbUv_vE5BhHm3H-kxcMwNWgrJVNYV04-xMV3A8NdGe0XzZt0WjjI5KYwuUBmcW0_F2JR5Vfq4aITwAuR-6iTK_TB3XS1-GHRVGUaE9nN2FsBxRkIH-RoJBPo8NkjOVRbBLX3c8GxM23rW59kdGfIbF9ITVgBNadM5x6dHKjTXWng24jhgnLNNHhfYJbw7AxM85bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار سفیر پاکستان در تهران با ظریف
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/143956" target="_blank">📅 21:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143955">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
عراقچی: ما از شورای امنیت می‌خواهیم که از استفاده واشنگتن از اقدامات اجباری و تحریم‌ها برای مجبور کردن کشورها به تغییر منافع اقتصادی‌شان، خودداری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/143955" target="_blank">📅 21:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143954">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
بانک مرکزی: تورم مرداد ماه نسبت به تیرماه فقط یک دهم درصد افزایش داشته و به ۳‌.۷ درصد رسیده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/143954" target="_blank">📅 21:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143953">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
خبر بزرگ پزشکی؛ آمریکا درمان جدیدی برای یکی از مرگبارترین سرطان‌ها تأیید کرد!
🔴
سازمان غذا و داروی آمریکا (FDA) یک درمان جدید برای سرطان پیشرفته لوزالمعده را تایید کرد؛ بیماری‌ای که سال‌ها یکی از سخت‌ترین سرطان‌ها برای درمان بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/143953" target="_blank">📅 21:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143952">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDPL-VWMex7huVS2hPHddm5PxTJOwgBtRplpj8hBceHV65sVlzv3JOkBp-IQKi1kfTJ-B0kLMGqyzySUJ18BVx_K_LnnhtgK4vTNp1wwBs7AgGZXIuUMYKjbBe7hS3oqltRnuEpmMb1PQoSSqv55Elfmi3T-9WvmyCxiUBIjhMXQfCJ9Dv55ssMMJ_FGWp7XO7TaOG2QKbxFU8F93Rw9YfqQT245UpYBfnjch6jYxVeuKVjEDM7IMPaaHZ_bZvKFqLmGCBmm9IHNDgatv9f3Eanhu_NTPTqLBHdgl_gOcmtsYR-9OhLHddVlUObg2AgCP_gudAGQYlBEQENubUYFJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه 14 اسرائیل:
مجتبی خامنه‌ای یا مرده یا مرگ مغزی شده و از اول ماه دیگه هیچ خبری ازش نیست؛
چند ماهه که اصلاً دیده نشده، حتی تو مراسم یادبود پدرش هم نبوده و فقط چند نفر محدود ادعا می‌کنن دیدنش.
الان عملاً سپاه و بقیه دارن کشور رو می‌چرخونن و یه خلأ قدرت خطرناک ایجاد شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/143952" target="_blank">📅 21:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143951">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
کارشناس صدا و سیما: در حالی که ما به علت محاصره نمی‌توانیم نفت صادر کنیم، کشورهای منطقه روزانه ۷ میلیون بشکه نفت از خلیج فارس صادر می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/143951" target="_blank">📅 20:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143950">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4082c1b5.mp4?token=l0r64hTozxZIxRC-QDot3cn5hI56VP27-vAG5QitZtbs-mvkJ5yeqga_7r1n0JQ3Ly7U8ABRpHHZdaDQ57N2lGr6QMjL899RwK6Z-95OnsE1VVNCFop6mxJHucLdXzo3OppPt30miCK6xZLySqwA-DTWoD9Ou-DGhwclocAB9mJfwFIJOOWzrA3ea-pCdw-72jxHOCMTEx7EvhT135xVQeiIToKatXCQi8zODeBBVCjnI4dCfmev6_5aEg3l61fbooDXrByVTocX7Enz-UWrhV3no-1KAWurzI4qWrxlZPjsJuyzfOgCBcRuo3XSSWGzvmJnWBehhO-hBl3fH-qjdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4082c1b5.mp4?token=l0r64hTozxZIxRC-QDot3cn5hI56VP27-vAG5QitZtbs-mvkJ5yeqga_7r1n0JQ3Ly7U8ABRpHHZdaDQ57N2lGr6QMjL899RwK6Z-95OnsE1VVNCFop6mxJHucLdXzo3OppPt30miCK6xZLySqwA-DTWoD9Ou-DGhwclocAB9mJfwFIJOOWzrA3ea-pCdw-72jxHOCMTEx7EvhT135xVQeiIToKatXCQi8zODeBBVCjnI4dCfmev6_5aEg3l61fbooDXrByVTocX7Enz-UWrhV3no-1KAWurzI4qWrxlZPjsJuyzfOgCBcRuo3XSSWGzvmJnWBehhO-hBl3fH-qjdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عارف: آمریکا به امضای رئیس‌جمهورش احترام بگذارد؛ راهبرد ما جنگ نیست، اما خوب دفاع می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/143950" target="_blank">📅 20:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143949">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
گزارش فایننشال‌تایمز در مورد کارزار تازه واشنگتن برای تشدید فشار مالی و تجاری علیه ایران: پکن که تا ۹۰ درصد نفت صادراتی ایران را خریداری می‌کند، روز سه‌شنبه به آمریکا هشدار داد درصورتی‌که شرکت‌های چینی به دلیل تجارت با ایران هدف تحریم‌های ثانویه قرار گیرند، دست به اقدام متقابل خواهد زد.
🔴
این تهدید برای واشنگتن اهمیت زیادی دارد؛ زیرا هرگونه افزایش چشمگیر تحریم‌های آمریکا علیه شرکت‌های چینی می‌تواند مذاکرات حساس تجاری میان واشنگتن و پکن را تحت تأثیر قرار دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/143949" target="_blank">📅 20:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143948">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
سی‌ان‌ان: قیمت نفت برای سومین روز متوالی با افزایش امیدها به توافق ایران و عمان برای ایجاد مسیر جدید در تنگه هرمز کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/143948" target="_blank">📅 20:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143947">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfO1-ZEgJXC-22LODIpKhhbjZlWiuKdFLMNNk2tMQqmIfWU3X48gVZo7LRrBa4K-sL1FqauKasNYygPIA_ev5lQ_cD3eAOhfJG-PHNzgReM_EXmP_5tVRGvwR2EtzhbTcwFDRtfL__2sncAM13ei1Pvis_8GKe-s84W7_eEwSS7H8u9GTCTnwfb2jjDsq_VzygbK9Klhho1a8aCeLdkrQNa3ktaibvwJuApUcZkQSgDG4Q2d3iwrUboD2PhB1kjrBK2ZXLhp-vDGrfYKsoVU3DejVWQxo5bXDAh-1Ewo0SZvviqgSut8dayG6lFYit3__mur_tbuPyn9xuY4N9Sa7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش نبویان به بیانیه مشترک ایران و عمان درباره تنگه هرمر: عراقچی از دستور صریح رهبر مبنی بر انحصار ایران در مدیریت تنگه هرمز تخلف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/143947" target="_blank">📅 20:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143946">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/442a0c2db8.mp4?token=r-K17hu9xh_uKKLds2rvsWksUziR43km9DvudYWn_qT7kzR7_29jCV7kbtRy-GpNcoT-0hQoUD2OvqV0DNKg17wDnQZxeNlNpRLgKls_EWZB0fm75NQHBirw2R5ixtt780n-VDL_XV9VUbdcCKzy_KtbWczHKY1sTHHW07nPXO2U94YH7DA_-H3KmUcPMgBHsIxjXOThJGskQDdp8UIxArNw_WQZgJInxm9AcYrMbc-WSBD3gxZgb_go9jeTyimS-NfHqvGEWIQZ-EqHwsz_XoeOZgZMddqmAoX-oI581-Xj3FPmZ7DeWmG2j0hL39K-JTaKsPzE0A0sYvCD9HNDeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/442a0c2db8.mp4?token=r-K17hu9xh_uKKLds2rvsWksUziR43km9DvudYWn_qT7kzR7_29jCV7kbtRy-GpNcoT-0hQoUD2OvqV0DNKg17wDnQZxeNlNpRLgKls_EWZB0fm75NQHBirw2R5ixtt780n-VDL_XV9VUbdcCKzy_KtbWczHKY1sTHHW07nPXO2U94YH7DA_-H3KmUcPMgBHsIxjXOThJGskQDdp8UIxArNw_WQZgJInxm9AcYrMbc-WSBD3gxZgb_go9jeTyimS-NfHqvGEWIQZ-EqHwsz_XoeOZgZMddqmAoX-oI581-Xj3FPmZ7DeWmG2j0hL39K-JTaKsPzE0A0sYvCD9HNDeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
سیل در نپال یک پل را از جا کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/143946" target="_blank">📅 20:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143945">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
آمریکا: مذاکرات لبنان و اسرائیل از سر گرفته خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/143945" target="_blank">📅 20:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143944">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
بحران بنزین شروع شد
‼️
‼️
خودتونو آماده کنید برای طوفان!
تحلیل ترسناک این پسره رو حتما ببینید
👇
https://t.me/+6PPyWURHtW5jN2M0
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/143944" target="_blank">📅 20:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143943">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/va_wFzVnPIV5MHEWrO_Irdcaz_uCZs4hyckqxs6c0josXg6L5AMySxiPfXibgZ79sWePSfcGxWK37zLH5o-Y3FYYtuULgD2fJvcSk8aYp-Ai8ul2HgtqEKnef0dReN5Oma98z9J8UAj4BKs-EqQohUxXZj7socieK_4ktkT5Gbgy59A4t65H0Qd9USdwwJph4jYA_aOIVT7pWNRqUCqb7wHaTbytidbuRgd6QY5utndXdf7kWSS2AJrYxrdV6vHwYWCeLiNJUICY1sY-9UeClgsKON2xH_junEe14Zipo0sD7SDScqhjySPdRbTt9svhMbNeaBrbAJXPpjwSxPpeDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال:
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/143943" target="_blank">📅 19:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143942">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7c7f3f23.mp4?token=iTyCpJYSvnWScYwCkSHqOix3l36bCPirdP9PH3KwngaW6U3K13gPn-9v_UNF23jQAZEoCBAHV7kbb5ngAm7JqyUgk42Usfr43Cc2PjFyPUlpYqR7TkyqDwL1C-K1na_Sez6bagPJm7bn7m4jA1yKY1-st-t52O2BmbFXXTqtZPeS42J0pdXkFx5_SeQ6xJxgvaFVfuxzBPX-BBu1sSi692956P-tFTZ9wLW5q89_yAZo-S_S-2vKtwsIg8r7djqOuYUREarcKWzanilhmLxJjNID0Bd5j3YE0IiTBA8fXn2sr0hMsgqiD5MIHfAmVYnU_rUx4Sg9uf1IC-K0yiAn7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7c7f3f23.mp4?token=iTyCpJYSvnWScYwCkSHqOix3l36bCPirdP9PH3KwngaW6U3K13gPn-9v_UNF23jQAZEoCBAHV7kbb5ngAm7JqyUgk42Usfr43Cc2PjFyPUlpYqR7TkyqDwL1C-K1na_Sez6bagPJm7bn7m4jA1yKY1-st-t52O2BmbFXXTqtZPeS42J0pdXkFx5_SeQ6xJxgvaFVfuxzBPX-BBu1sSi692956P-tFTZ9wLW5q89_yAZo-S_S-2vKtwsIg8r7djqOuYUREarcKWzanilhmLxJjNID0Bd5j3YE0IiTBA8fXn2sr0hMsgqiD5MIHfAmVYnU_rUx4Sg9uf1IC-K0yiAn7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیروز کسایی که سال ۱۴۰۴ برای ثبت‌ نام یه ساله لاماری شرکت کرده بودن و هنوز ماشینشون رو تحویل نگرفتن جلوی شرکت مربوطه جمع شدن و خواستن در رو از جا بکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/143942" target="_blank">📅 19:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143941">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/592c74d9a4.mp4?token=TZLnYdu1sfGp3F7IR9OO39PYZtpMCtmM3PQAUC9QoK6dQhbe544ZF_O-PT157VZBRwstLG2RyEIUHyYm-cfU_grQAXa6sv3OZ_iw8YAIc3vl2S-eX6Z6OCIRQdno9yBciulG3MoTHMDyNuHhH55nsgcWCWuTHcEezyS5Nsp2DFlOQCgDZnWIHgV7j79nXbGjLMAZsQp1ToqNYANb6WLbJ0_ZEys8eZHZTV8ksnpOm72fEhMYVop8Gecx0ei5yWw-uVH9O2gjWVKfrLBOxL3YQ4r5FhqKKDDtv8AbuJNk9lESqLbzstXZ_Vrxq8MKCP7f44Wq9aIvWSzCn3pf5A3SPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/592c74d9a4.mp4?token=TZLnYdu1sfGp3F7IR9OO39PYZtpMCtmM3PQAUC9QoK6dQhbe544ZF_O-PT157VZBRwstLG2RyEIUHyYm-cfU_grQAXa6sv3OZ_iw8YAIc3vl2S-eX6Z6OCIRQdno9yBciulG3MoTHMDyNuHhH55nsgcWCWuTHcEezyS5Nsp2DFlOQCgDZnWIHgV7j79nXbGjLMAZsQp1ToqNYANb6WLbJ0_ZEys8eZHZTV8ksnpOm72fEhMYVop8Gecx0ei5yWw-uVH9O2gjWVKfrLBOxL3YQ4r5FhqKKDDtv8AbuJNk9lESqLbzstXZ_Vrxq8MKCP7f44Wq9aIvWSzCn3pf5A3SPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک ایست بازرسی عادی در یمن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/143941" target="_blank">📅 19:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143940">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
رئیس سازمان انرژی اتمی: تا تدوین پروتکل بازرسی از سایت‌هایی که مورد حمله قرار گرفته‌اند، آژانس نمی‌تواند از سایت‌های هسته‌ای بازرسی کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/143940" target="_blank">📅 19:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143939">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhVFz0yuKMehF3op5h9GwfVmMMCECLk-VXqLUSVv8yJA1pRMgluPvbOTkNUFW6Fs6b2hXO8spe3XAU_CFIO6HejCyp4iVBUHNfbQbD6U5JLSc0ki0WxPPv-nEhwhAzht_tI4SOAHwpkolMClw1riYc87cycQ1PtuYTmj2DUbtkKsyljD4EmX8mfw8pKsb3AkmG0Psaj6I1CsE1rKs6LDpB7EOGdOgpW16gnQV5oQmna4MAif9wPGj_lQ52gxt19uivuLbQS3WU11DjqLaDx5yjyYUoWJTJQvoTYy7jFSWqMVPA_T8GMpV8DaDts4xQTSdquQ57Lv44iC7OFLJge3rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بدلیل گرونی سنگ قبر یه عده دزد شبونه از قطعه ۲۱۷ بهشت زهرا کلی سنگ دزدیدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/143939" target="_blank">📅 19:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143938">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سی‌ان‌ان: پاکسازی مین‌های تنگه هرمز کار ساده‌ای نیست
🔴
همکاری ایران حیاتی است
🔴
صرفاً اعلام بازگشایی نمی‌تواند خطر مین‌های دریایی را از بین ببرد یا اعتماد بازار را در میان صنایع کشتیرانی و بیمه احیا کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/143938" target="_blank">📅 19:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143937">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
یک منبع دیپلماتیک به شبکه المیادین:
نخست‌وزیر و وزیر خارجه قطر به زودی به تهران سفر خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/143937" target="_blank">📅 19:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143936">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
یک نفتکش هندی به نام HAANA لحظاتی پیش قصد داشت از مسیر جنوبی تنگه هرمز، موسوم به کریدور عمان، عبور کند.
🔴
این نفتکش پس از دریافت هشدار، از ادامه مسیر منصرف شد
🔴
همچنین گفته شده در ۲۴ ساعت گذشته هیچ ترددی در مسیر جنوبی تنگه هرمز مشاهده نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/143936" target="_blank">📅 19:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143935">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ترامپ: سفر رئیس سازمان اطلاعات مرکزی آمریکا (CIA) به روسیه ربطی به تحریم‌های ایران یا احتمال حمله مسکو به انگلستان ندارد
🔴
دونالد ترامپ، رئیس‌جمهور آمریکا، گفت سفر جان رتکلیف، رئیس سازمان اطلاعات مرکزی آمریکا (CIA)، به روسیه «به‌نوعی یک سفر نیمه‌روتین» بوده و گمانه‌زنی‌ها درباره دلیل این سفر را رد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/143935" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143934">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d12996542f.mp4?token=Js8IvWZiWq27KK53nGt_IcoNxG0a_LeoKRyIFyyIKRRuSzjU_XZ2r8VL5Ldppwe5jP-tIKWRQudN9BchQQicgH543lmuivLYz9PaXbivjgis8hjpRAnmGfbtZ5DPWiSZ7RWg63cQcPSLMD7xyYQ4unvL_tPn8MYUlOtw0phTUZqH60EHAdZQfonvbb7c_USy0ekmU-tjwuZ00aCkgUCU4CFHEveiWI8echLAcwghLRdojjP5qq-I2lUKu8qecdZvrdPzakfh3MpHDQhLGPjR8g01KwuH_PI7ZQZ0hfmZXEnyFiA5mTFnq5kwFicR9A0VLNsK1n54_n0WnmKz3rr7Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d12996542f.mp4?token=Js8IvWZiWq27KK53nGt_IcoNxG0a_LeoKRyIFyyIKRRuSzjU_XZ2r8VL5Ldppwe5jP-tIKWRQudN9BchQQicgH543lmuivLYz9PaXbivjgis8hjpRAnmGfbtZ5DPWiSZ7RWg63cQcPSLMD7xyYQ4unvL_tPn8MYUlOtw0phTUZqH60EHAdZQfonvbb7c_USy0ekmU-tjwuZ00aCkgUCU4CFHEveiWI8echLAcwghLRdojjP5qq-I2lUKu8qecdZvrdPzakfh3MpHDQhLGPjR8g01KwuH_PI7ZQZ0hfmZXEnyFiA5mTFnq5kwFicR9A0VLNsK1n54_n0WnmKz3rr7Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگست: گزینه حمله نظامی در هیچ نقطه‌ای از تنگه هرمز منتفی نیست
🔴
ما به هیچ‌وجه استفاده از حملات نظامی در هیچ نقطه‌ای از تنگه هرمز را منتفی نمی‌دانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/143934" target="_blank">📅 19:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143933">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ:
شب گذشته 22 قایق نظامی تندروی ایران را در تنگه هرمز هدف قرار دادیم و نابود شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/143933" target="_blank">📅 18:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143932">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Egopf7fjGjdS8NVWhMlUHVrqf99rf1FvJvnmbnK0BY0vrVtufKyL5JRdTbFJWGeyNb4BlWCvOXHur34hcu73ZJsMPvBA8PjPg3zeB_HcmVww3Lw9FD7wztqg8gkT6jLSezJNoqvBKlEyfIPQKxQmKp1u92KNw9KLGDbUCpkl7EtWhrH8TrRDcVFIXhzreQx9QV4CXR-OXy-JUMFHy982N4kXD4YsaV3flC1FudAskm_rEmNEhRuP4zOkt1hrw7gSJekANyCkHbs-8pGGRpJOGdIdR9kXuloOZepp9iTdi76jaCYQinLDdoQD9QV67n1xMfZwB146vLluh93w9bdyBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی:
اینترنت رو قطع کنید، یه دیقش هم ضرره
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/143932" target="_blank">📅 18:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143931">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏
👈
خبرنگار کاخ سفید:
گزارش هایی وجود دارد مبنی بر اینکه روسیه در حال آماده شدن برای حمله محدود به انگلیس است، سفر ناگهانی و غیر عادی رئیس سازمان سیا به مسکو نیز به همین دلیل بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/143931" target="_blank">📅 18:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143930">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f48fa42be5.mp4?token=SvLRHIDhne_657VaWsaH_hNtKXPQLQsqrsFnHSOXoBEuy9WMgVSVg0Q0So9jbNcoNR-2GhhzQZX6xeqM94-WvYDRe5nQaVZwnpjfznI33fx2ZzxGlCno6OOvMC_FTywORqi9K4SWwOK42oZSni5QIrqWt8XoCiXOx7HyvysCBtuem5xhxn0Htr8D5uiNq1j3qbfos3BBeSphN7OdYzZmAAt1okuN4ZlqgJAIpI6mVIp86ngK6PX_u9xEhL1HBK-8il1aU1N-xfGcKgmRK14EtpGp27KTh6cPw-Sv2eV4S_7JoEn-K1yAEHFJv9_296jWdpRBtd4YAqNL1RspAJD7VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f48fa42be5.mp4?token=SvLRHIDhne_657VaWsaH_hNtKXPQLQsqrsFnHSOXoBEuy9WMgVSVg0Q0So9jbNcoNR-2GhhzQZX6xeqM94-WvYDRe5nQaVZwnpjfznI33fx2ZzxGlCno6OOvMC_FTywORqi9K4SWwOK42oZSni5QIrqWt8XoCiXOx7HyvysCBtuem5xhxn0Htr8D5uiNq1j3qbfos3BBeSphN7OdYzZmAAt1okuN4ZlqgJAIpI6mVIp86ngK6PX_u9xEhL1HBK-8il1aU1N-xfGcKgmRK14EtpGp27KTh6cPw-Sv2eV4S_7JoEn-K1yAEHFJv9_296jWdpRBtd4YAqNL1RspAJD7VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از مسئولان‌نظام هنگام مال مردم خوری
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/143930" target="_blank">📅 18:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143929">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMGruYeTxfjtw8CEnsa5Vxov2GcdQOK4wUC6triEzqLOkGHoKBq7TTk_rayrTmyp1ukEr7Xl0QwUstbvxHl9NGWbEij7ovinML6raQtvqe_OkDWd-6H793YedY1x3toX9Xnbi7aF--nJ8ZaN6G0xUJmTLj_TKPwcYl6KV1gWGOP4inJyNOew8f_Bq2TSAEbYlKlHRPzbIbJV9-TISKI1SzgXiEk03KeTerj71kTuiQzeN0Ib_ph9E0euAtJuADbcqOmKOBNciCg611Ywi-pIq18lqvcTtelCw9kQiPIxoacFIE_GhsOBnalBhio-KpRzKRFlaIQEBhnL1kQBtn-mAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چادی هوپان: یه عده خائن از ویزا نشدن من خوشحال شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/143929" target="_blank">📅 18:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143928">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cd6b5d203.mp4?token=Ao671VICvy7nsKaX3RxTVQFpX_fMeYW3VYFYjzh6x5jaSfA1QdOn3-hX0KR0KIsfOb6znRAKIPdg9y1KYSKMtexX24s1G_92DaQvjpWQjafHeestvokpjx5YOloP_eQBNw92MXj2XbfMNV0D5_uFNdKIhS-oDuFX_pB-oqeUuBw5SbYg7N-o7FM7k07BBXH9TwtbtqJQkeGU8aCjEdenLD35VVW8iHfEBIQTf31d1lQkAuaLAEB_dLIzW5NhljnuaUooD3B7WNSn9FnrisAQQe_sbXbWmmfmsjv1wYeWp9ZzkHftuGb-NwgGslw0IADeui5s4eWPGvOVwltqPljQyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cd6b5d203.mp4?token=Ao671VICvy7nsKaX3RxTVQFpX_fMeYW3VYFYjzh6x5jaSfA1QdOn3-hX0KR0KIsfOb6znRAKIPdg9y1KYSKMtexX24s1G_92DaQvjpWQjafHeestvokpjx5YOloP_eQBNw92MXj2XbfMNV0D5_uFNdKIhS-oDuFX_pB-oqeUuBw5SbYg7N-o7FM7k07BBXH9TwtbtqJQkeGU8aCjEdenLD35VVW8iHfEBIQTf31d1lQkAuaLAEB_dLIzW5NhljnuaUooD3B7WNSn9FnrisAQQe_sbXbWmmfmsjv1wYeWp9ZzkHftuGb-NwgGslw0IADeui5s4eWPGvOVwltqPljQyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیالوگ ماندگار مرحوم داود رشیدی که حال و روز الان ماست
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/143928" target="_blank">📅 18:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143927">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
وزیر ارتباطات: پرونده فیلترینگ باید در کشور بسته شود
🔴
استفاده از فیلترشکن‌ها خسارت بزرگی زده است
🔴
افرادی هستند که اصرار دارند در بر همان پاشنه بچرخد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/143927" target="_blank">📅 17:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143926">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qor9VOqNNt0-sbqqm-6u6TPVNX7zIoDKBCMacvAGZ1PW1KzBrpSer5k1Ib4-VtkzCYogMaQHyCUBh-Esv1XyYvT3LWB5VhyWMMcG_8K6YK2Xfuhg0KzLkU1yMMwUhQH06dgxLV_JIJcjIuu-utdfGJwrGyjdI4FzPI0e873VHLLeJlfc2WKh56m5ZypdYz04yvymYaaAVq3Dtv9D7ZRqLtBhPNIEJCqLzv3eaTljfh204Nwiy795zZMkTKnp3sI9yJXqC3iwSMxKKk3U9f0yVrl_IMhR-GfiSW8X2ENIcJlQGRJY-UPVtCO0YQUBMBxKpZRqJSNTPPQFd3tlyYADZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به الجزیره گفت که حکومت ایران "با مردم خود بسیار بد رفتار می کند، آنها بسیاری از معترضان را می کشند."‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/143926" target="_blank">📅 17:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143925">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrI9Np-4CHv7T4BCznkzhyPi3g0UhbkJ1IrBWn7jO9p1z8NiCwqnZOxuhF6PN-7saA7uYr2WeV7YkusZD7rCG0s4hVt8OhQhtepQwVi08EaXt1P-qrKt-DF3aho6xojUy4_kjk-Zv3XtuW0DAjmqkPx943VaqAMszoqnKL-ZABWVoTuNXgVMpFfPUFsRdVa--7l89YYcQ8pJz_o3SMgqlQ0Tvzx3RrnGpTspq9qgtGvuNhvmWlYYtxAoeSjmBxHmUTbGPsPv_MP-V8vdupghUz-zB8IgNL1nsuE-BWoodhKQOBiXu9KE2A6YvVQ-K1lfEi7_4Ycar7I-B86Wrnb8jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: رهبر ایران زنده است ولی دست و پا و بدن به شدت آسیب دیده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/143925" target="_blank">📅 17:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143924">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ: رویارویی آمریکا با ایران تابع هیچ جدول زمانی نیست و تا هر زمان که لازم باشد ادامه خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/143924" target="_blank">📅 17:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143923">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
دلار و طلا ریخت
‼️
بیا اینجا ببین کی باید بفروشی و بخری
👇
https://t.me/+6PPyWURHtW5jN2M0
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/143923" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143922">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de06f44cb7.mp4?token=up08NF56CoUsTdUdECgZCKqOhvyN0S_mK_E4CoIBRmQfb_imwh3tn-V4PkBNVh8LSxqlbjjhTxsW119ijso418OdE5yMLqohbzICBu3UlFp5PqIq96egMhd0HYvgzhcx1lD0NMkg58HN-yUWshq2gqWZKoNGP0MZoauDuzpaeNssHnXh6zTvdmDoSAUVTgYyu5apCOFtO4MXbfSewaGpk1RRBx6uiCLdxzAJa4ZAw0PfToKV4xqYVvEFDrKTbEp4eKWz0CZ4zdqRVoHO3L9DqatZJrLdRSQFDafPnoE9bZms2foFaC_qTucGl6NJidmUDwNTTUSEW1sYTqzNPGDgCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de06f44cb7.mp4?token=up08NF56CoUsTdUdECgZCKqOhvyN0S_mK_E4CoIBRmQfb_imwh3tn-V4PkBNVh8LSxqlbjjhTxsW119ijso418OdE5yMLqohbzICBu3UlFp5PqIq96egMhd0HYvgzhcx1lD0NMkg58HN-yUWshq2gqWZKoNGP0MZoauDuzpaeNssHnXh6zTvdmDoSAUVTgYyu5apCOFtO4MXbfSewaGpk1RRBx6uiCLdxzAJa4ZAw0PfToKV4xqYVvEFDrKTbEp4eKWz0CZ4zdqRVoHO3L9DqatZJrLdRSQFDafPnoE9bZms2foFaC_qTucGl6NJidmUDwNTTUSEW1sYTqzNPGDgCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اگر دونالد ترامپ رئیس‌جمهور نبود، اکنون اسرائیل وجود نداشت.
🔴
این یک تضمین است. اسرائیلی وجود نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/143922" target="_blank">📅 17:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143921">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b63c7b29f.mp4?token=WhrKBBwZDIDvf4C3zQxyVFVR9xZDysJHcBlznNXKm11eUCSmUrez_HfoluN_FvOEY5CeO1cYiWrwdYxgxfy9VDSoXze1YGRcq8u6EThaX8QQS35Cwyb6Srefx31NhenpVp_cIKoXU77HzXvRH1wc5Njx4F2Iso8lrqdw8hFVV_sNYn5SgW5WhIIw5OfYodxv9-p8XN33I5YQ3KIDdOrv4OkHbHIQFXVgtWfihDENWuOeSezynK1HA8E318vLYoTIZocQKUb8r9bm1vVfNqVdvHTEaaFP57rTdmRfmtARkrTRSTONprmlHwrCaxNP_73DDKDSecTvYm7Ip2DzHRvkIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b63c7b29f.mp4?token=WhrKBBwZDIDvf4C3zQxyVFVR9xZDysJHcBlznNXKm11eUCSmUrez_HfoluN_FvOEY5CeO1cYiWrwdYxgxfy9VDSoXze1YGRcq8u6EThaX8QQS35Cwyb6Srefx31NhenpVp_cIKoXU77HzXvRH1wc5Njx4F2Iso8lrqdw8hFVV_sNYn5SgW5WhIIw5OfYodxv9-p8XN33I5YQ3KIDdOrv4OkHbHIQFXVgtWfihDENWuOeSezynK1HA8E318vLYoTIZocQKUb8r9bm1vVfNqVdvHTEaaFP57rTdmRfmtARkrTRSTONprmlHwrCaxNP_73DDKDSecTvYm7Ip2DzHRvkIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
وقتی به لندن می‌روید، وقتی به پاریس می‌روید، تقریباً انگار قانون شریعه (احکام  اسلامی) یک سبک زندگی دوم است.
🔴
این مسخره است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/143921" target="_blank">📅 17:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143920">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61179d1b62.mp4?token=jSDvCjeGHKHA_eCF_ZahdIpmbOXxZ2nD02F_-vfR9fiEw_xNnE9N9ul5t0sxkI2xLPUVcrJwheqddpZfoPP61O1jpKVe1nxrEpevXd4fGHZEyWuNtrWDJtXRTmhiy2LkM4QpijDqg1JVKx4bdy_inH3tJutAWJywAZaUk4JUhFNybhJpeSJWdWJd05o40fAB2FOkWe8VWkfBl4BxCzGdgpKcqjFG7MYB4oyBThSF3q-Q2wq-xTyDTtZyorg1h_VHnK1X8uL2ggr29CMVtR-oTT0eGtUyZdkV-nnSvReHL5rETKHXSHnIm4qkULHY3lDL4TFJPnsLkETvFUZ7HszVDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61179d1b62.mp4?token=jSDvCjeGHKHA_eCF_ZahdIpmbOXxZ2nD02F_-vfR9fiEw_xNnE9N9ul5t0sxkI2xLPUVcrJwheqddpZfoPP61O1jpKVe1nxrEpevXd4fGHZEyWuNtrWDJtXRTmhiy2LkM4QpijDqg1JVKx4bdy_inH3tJutAWJywAZaUk4JUhFNybhJpeSJWdWJd05o40fAB2FOkWe8VWkfBl4BxCzGdgpKcqjFG7MYB4oyBThSF3q-Q2wq-xTyDTtZyorg1h_VHnK1X8uL2ggr29CMVtR-oTT0eGtUyZdkV-nnSvReHL5rETKHXSHnIm4qkULHY3lDL4TFJPnsLkETvFUZ7HszVDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره تورم در ایران
:
فکر می‌کنم تورم ۳۰۰ درصدی دارند. شنیدم ۹۰ درصد است. فکر می‌کنم تورم ۳۰۰ درصد است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/143920" target="_blank">📅 17:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143919">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07afc966eb.mp4?token=VWXTtouvHKRpPifmXcik3WCvJn3IHNc_X4XesuaSDPaWxClCxH1TZWvMpqRqnaTrtlRzZODT3ijxVFKfn3PNyQ_6FdUQliN9gM4JPvZjYjfjHSiXD44ewU1K8g2rJicy80fzKtDijtfsd72lTLKdjZPzIQRF8eoq_zN6K-NUgoGGABrbLawhPjVZdZi2UhMoNIG_3g5UJjyj3pZsb-SNg3z6yDL1_t-m3ij4g3pa-WpZrMg7cSC8getRqMrpesQsbJxvCpBccuwlwgRqSPyDH3SrKPOB3FLysbkg0tioPIqkQD4Rs43AxDlnOG3g-YGUGWl-1DEEjcN7Ow78MZeWgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07afc966eb.mp4?token=VWXTtouvHKRpPifmXcik3WCvJn3IHNc_X4XesuaSDPaWxClCxH1TZWvMpqRqnaTrtlRzZODT3ijxVFKfn3PNyQ_6FdUQliN9gM4JPvZjYjfjHSiXD44ewU1K8g2rJicy80fzKtDijtfsd72lTLKdjZPzIQRF8eoq_zN6K-NUgoGGABrbLawhPjVZdZi2UhMoNIG_3g5UJjyj3pZsb-SNg3z6yDL1_t-m3ij4g3pa-WpZrMg7cSC8getRqMrpesQsbJxvCpBccuwlwgRqSPyDH3SrKPOB3FLysbkg0tioPIqkQD4Rs43AxDlnOG3g-YGUGWl-1DEEjcN7Ow78MZeWgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: وقتی افرادی حاضرند شما را بکشند، اعتراض کردن در ایران بسیار دشوار است. به همین دلیل آن‌ها اعتراض نمی‌کنند.
🔴
و شانس وجود دارد زیرا آن‌ها بسیار تضعیف شده‌اند... بسیاری از سربازانشان حقوق دریافت نمی‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/143919" target="_blank">📅 17:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143918">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e724bf7fc2.mp4?token=KwWznANESmrxQJ1qnDOZ2rhMYJly4oWlSyO4F8StHfkTF4J-b8_-hkam1G_SdEPbWNSqh4iKA-VTQKTK0m3x3x9jle_Os6957NUw-orgJQVW7xZENtkMscig_5DtdDuml9-e4gvuI-LuI3aO2KmDIVuFxNNipUHsO-LS9kFKG8dIOkRCAa-l4z0CmWjIk1knvWweA9bQBO7F5MTh0j_cxelq9cwrRLwhnvu4LRYgoWqZ5o5sfO0qoio7N8d4sblzHkEm4cL47p2CG2KP_3eyDTnPBRZwdtl6zEinsoTiWyjahNtII78cssg8QaHdIcMWRUAleYOTCX9Dm1CfFR8tpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e724bf7fc2.mp4?token=KwWznANESmrxQJ1qnDOZ2rhMYJly4oWlSyO4F8StHfkTF4J-b8_-hkam1G_SdEPbWNSqh4iKA-VTQKTK0m3x3x9jle_Os6957NUw-orgJQVW7xZENtkMscig_5DtdDuml9-e4gvuI-LuI3aO2KmDIVuFxNNipUHsO-LS9kFKG8dIOkRCAa-l4z0CmWjIk1knvWweA9bQBO7F5MTh0j_cxelq9cwrRLwhnvu4LRYgoWqZ5o5sfO0qoio7N8d4sblzHkEm4cL47p2CG2KP_3eyDTnPBRZwdtl6zEinsoTiWyjahNtII78cssg8QaHdIcMWRUAleYOTCX9Dm1CfFR8tpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کانادا
:
آن‌ها هیچ چیزی ندارند که ما به آن نیاز داشته باشیم. ما می‌توانیم بدون آن‌ها ادامه دهیم.
🔴
چند مورد وجود دارد که می‌تواند کمی آزاردهنده باشد، اما می‌توانیم آن‌ها را از جای دیگر تهیه کنیم.
🔴
حرفه است که به کانادا درس دهیم که دیگر نمی‌توانند این کار را انجام دهند.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/143918" target="_blank">📅 17:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143917">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ: من باور ندارم که رهبر فعلی ایران فوت کرده باشد
🔴
اگر هم مرده باشد، دارند نمایش خیلی خوبی اجرا می‌کنند؛ چون مدام صحبت از این است که باید برای گرفتن تأیید نهایی‌اش با او گفتگو کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143917" target="_blank">📅 17:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143916">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ترامپ به الجزیره: ما در حال دستیابی به یک پیروزی بسیار بزرگ هستیم و ایرانی‌ها از تورم عظیم رنج می‌برند و اقتصادشان در حال فروپاشی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/143916" target="_blank">📅 17:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143915">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فوری/ترامپ درباره ایران: بگذارید این را به شما بگوییم، من متوجه شدم گروه سوم (سران کنونی ایران) هم خوب نیستند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/143915" target="_blank">📅 17:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143914">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
فوری/ترامپ درباره ایران: بگذارید این را به شما بگوییم، من متوجه شدم گروه سوم (سران کنونی ایران) هم خوب نیستند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/143914" target="_blank">📅 17:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143913">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ترامپ: ما مین‌ها را از آنجا خارج کردیم. اما تنگه هرمز، به کار خود ادامه می‌دهد، یک تنگه فعال است.
🔴
بله، گاهی اوقات ممکن است یک پهپاد یا موشک شلیک شود، اما این یک تنگه کاملاً فعال است.
🔴
مقدار زیادی نفت از آنجا صادر می‌شود.
🔴
دیشب ۲۰ قایق ایرانی را منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/143913" target="_blank">📅 16:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143912">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3f8d4b27a.mp4?token=ScMPIImqAc3dqiLkQiLAzkQ8XypAox821pF8ZmViPCSf6vBa4BEIbDgHsMA6STsUOsrnce2e25bOZnftKWF-nkkfVT0CuzuMtcaZGdffzDZWTDSET7UdsDK7NN5Dt4WrC2KbdWgw4YCk0UyI7iRSFtwWQEHeuimpz5Ucx3Rl5yTbi553hvFi2WyRdUvo5YPOMNPEVYsOnrCXWEBepR3lMTymHxL4H5CjNye1DWm9v4vsXxe7_iREXC_saURwy-4zr1NhUfzbnVAcV6sOZZ7ODktc9cQ9JSfShNiZglOu17PRVeDU9A5mhfhDlgdgJQgPkjDwJw9Nl80a2DZ_qgbw9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3f8d4b27a.mp4?token=ScMPIImqAc3dqiLkQiLAzkQ8XypAox821pF8ZmViPCSf6vBa4BEIbDgHsMA6STsUOsrnce2e25bOZnftKWF-nkkfVT0CuzuMtcaZGdffzDZWTDSET7UdsDK7NN5Dt4WrC2KbdWgw4YCk0UyI7iRSFtwWQEHeuimpz5Ucx3Rl5yTbi553hvFi2WyRdUvo5YPOMNPEVYsOnrCXWEBepR3lMTymHxL4H5CjNye1DWm9v4vsXxe7_iREXC_saURwy-4zr1NhUfzbnVAcV6sOZZ7ODktc9cQ9JSfShNiZglOu17PRVeDU9A5mhfhDlgdgJQgPkjDwJw9Nl80a2DZ_qgbw9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من قطعاً قانون شریعت (احکام اسلامی) را ممنوع خواهم کرد.
🔴
ما یک سیستم عالی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/143912" target="_blank">📅 16:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143911">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f2bb31062.mp4?token=B0JHHn03A_m3wMJJ-q0EdgKonqV7jofO48wiejLgu4304sxBW7nvgBhgwgiTxEZPGA59UbTPvnplIWFAZyr-tTnvWzYsu1xIIOHgxIksUZQmlhJaiupLxuBUj3sW8Sj5m39VE1AUzvPkyTUmWddzRo094trO5KHnsUvd7RSfTMEs6P0rRQ26dS2qm-vHIF-Sha-EWqJ4t8h0fjgk3slwbY6ceQYNZIX-ELDY9B2ZU2OzsnMSkzkYOxh6w_MyTBkkwOf3r0LXT02E4GRZ7Am8OjBP-UPnOwRbcJVi41valA_xwtfZIQPfG9pui5cdDNJ4t9hl5deCOAzkjrRGm6ITug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f2bb31062.mp4?token=B0JHHn03A_m3wMJJ-q0EdgKonqV7jofO48wiejLgu4304sxBW7nvgBhgwgiTxEZPGA59UbTPvnplIWFAZyr-tTnvWzYsu1xIIOHgxIksUZQmlhJaiupLxuBUj3sW8Sj5m39VE1AUzvPkyTUmWddzRo094trO5KHnsUvd7RSfTMEs6P0rRQ26dS2qm-vHIF-Sha-EWqJ4t8h0fjgk3slwbY6ceQYNZIX-ELDY9B2ZU2OzsnMSkzkYOxh6w_MyTBkkwOf3r0LXT02E4GRZ7Am8OjBP-UPnOwRbcJVi41valA_xwtfZIQPfG9pui5cdDNJ4t9hl5deCOAzkjrRGm6ITug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
ما به زودی پیروزی بزرگی در ایران خواهیم داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/alonews/143911" target="_blank">📅 16:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143910">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acb401a2e6.mp4?token=R0JG1tU3Q1a9o-Q-h_H8bfkxljgHYHn2dIW5iV5wSUmndMsSvTpYwcnHWRdlK-Jpa65DdU99m4LqONnviIvYJVVJ80mJM9PVhr0BhoJQkHY7bDwcI4WQRx03FXf6bWNQD3gLotYxCeWz7ltpxJzO0GlMgijzEXiRmTZMZ8vogh6doD1Eay9m4bXP_mBm8rSLPXc7hto79bBLXW3NqoSihHy4TSs_Iq6czkgXwYhYcDlKWfJhNToJMhUWM7p8pAirOs2l6vxOjNLul4VU_O_MtWOLaQ7JjIAmZaKcek0jvqGx2EcnIvFM4QKMC79vrilqDwwplBtt0m_umsP7QDJUSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acb401a2e6.mp4?token=R0JG1tU3Q1a9o-Q-h_H8bfkxljgHYHn2dIW5iV5wSUmndMsSvTpYwcnHWRdlK-Jpa65DdU99m4LqONnviIvYJVVJ80mJM9PVhr0BhoJQkHY7bDwcI4WQRx03FXf6bWNQD3gLotYxCeWz7ltpxJzO0GlMgijzEXiRmTZMZ8vogh6doD1Eay9m4bXP_mBm8rSLPXc7hto79bBLXW3NqoSihHy4TSs_Iq6czkgXwYhYcDlKWfJhNToJMhUWM7p8pAirOs2l6vxOjNLul4VU_O_MtWOLaQ7JjIAmZaKcek0jvqGx2EcnIvFM4QKMC79vrilqDwwplBtt0m_umsP7QDJUSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
ما از همان ابتدا واقعاً و به‌طور کامل بر ایران مسلط شده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/alonews/143910" target="_blank">📅 16:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143909">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
رایزنی وزرای خارجه عربستان، ترکیه و قطر درباره کاهش تنش در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/alonews/143909" target="_blank">📅 16:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143908">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bab00cbf2d.mp4?token=FBLeVKYhyHIIE-M0ZbTCScCmX_Isp9R6pRiCexxZd-gP6XSgDKLUK_dNgZJo3c1-EmYd3rOI1pQhXp3AZwjCAInGK4gwiEy_8EfXezz82kbcCn5K72j5dn_q1kqyuCmlPvD0dzxzowN3rWu3o-R1xIPvLP25Gv7Xjn-BGMvLcadQ7PDGA8nTjiPmiBYg5jaL9szHuNUqu1r4XVdY2X-fo3-PX_9LbwZRfA348k5JhMHd585K1qGulrkNcUbKajlRW77mRZaV1agI0VhYB4gSOH0lpxup6hFbd3rSjwmYmrwGwI2_er-IRQJiE3CSUWk5QZLueAHaokNEbiz81E7iAHEfr3xDgFhaUrQCqgPx8KSM2LgBf0ETwnvn7Aecrd7BcPcBjZflcqoasniA5xNeewGEYokE50rBjP4nzii10OwXp7FW48PyJw94UrQe7gMgkkXTkFRr6CWRP_0xK9wnRM8x_s2ThH518usUw1e2PWkQryc5sgHnRXHbMhgBY2ZlpQTR0ovov9xZ9lwwkXvsYyPLNqbi7VMaO1m5TSuMeYXpcN0_1uksgvwH5HQxkwq8zQFXobEsRt7hsGwnJNxR1kGHbChCIXF0wb77U_io_z0q3Yz2DqBV6klRnPHziewKsu0ESAVvV2HB2HRGn5nJnsJPhN_crT3J7xcancjBTjM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bab00cbf2d.mp4?token=FBLeVKYhyHIIE-M0ZbTCScCmX_Isp9R6pRiCexxZd-gP6XSgDKLUK_dNgZJo3c1-EmYd3rOI1pQhXp3AZwjCAInGK4gwiEy_8EfXezz82kbcCn5K72j5dn_q1kqyuCmlPvD0dzxzowN3rWu3o-R1xIPvLP25Gv7Xjn-BGMvLcadQ7PDGA8nTjiPmiBYg5jaL9szHuNUqu1r4XVdY2X-fo3-PX_9LbwZRfA348k5JhMHd585K1qGulrkNcUbKajlRW77mRZaV1agI0VhYB4gSOH0lpxup6hFbd3rSjwmYmrwGwI2_er-IRQJiE3CSUWk5QZLueAHaokNEbiz81E7iAHEfr3xDgFhaUrQCqgPx8KSM2LgBf0ETwnvn7Aecrd7BcPcBjZflcqoasniA5xNeewGEYokE50rBjP4nzii10OwXp7FW48PyJw94UrQe7gMgkkXTkFRr6CWRP_0xK9wnRM8x_s2ThH518usUw1e2PWkQryc5sgHnRXHbMhgBY2ZlpQTR0ovov9xZ9lwwkXvsYyPLNqbi7VMaO1m5TSuMeYXpcN0_1uksgvwH5HQxkwq8zQFXobEsRt7hsGwnJNxR1kGHbChCIXF0wb77U_io_z0q3Yz2DqBV6klRnPHziewKsu0ESAVvV2HB2HRGn5nJnsJPhN_crT3J7xcancjBTjM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مرتس صدراعظم آلمان: ما باید از این جوّ غم و ناامیدی خارج شویم.
🔴
ما باید از رنجش گسترده‌ای که برای مدت طولانی کشورمان را فلج کرده است، رها شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/143908" target="_blank">📅 16:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143907">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ به الجزیره: برای مذاکره با ایران «عجله‌ای ندارم»
🔴
ترامپ در گفتگو با الجزیره مدعی شد که هم اقدامات اقتصادی و هم نظامی در مواجه با ایران «موثر» هستند.
🔴
او در پاسخ به سوال خبرنگار الجزیره، افزود که «من هیچ برنامه زمانی ندارم، عجله‌ای ندارم»
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/143907" target="_blank">📅 16:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143906">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
یک منبع ارشد ایرانی: توافق با عمان در مورد تنگه هرمز هنوز نهایی نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/143906" target="_blank">📅 16:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143905">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2cbeca874.mp4?token=H69cSwawonRatsxWpKb0X_2RLx62frXfiKNDq8u91j09lU2cEb8iNPGjDAAB3ZsM3SrItokZXeforOfqIW9FvIJpPzJJGunXU-2ncspXNwR9vrkGUPIhZc8gJtjqtCiOpEv7J-ILPy1455L3gvQzSh1QanbNphbx-v9ieocE0O1lVG3HbSHQ2xCT2-aM2I23vX93jqvnYtsEUpkG3TFRFadvaRC7fG66XFfRu3AaSpCeVr-gmva7EnjTjUGAuHtiVHEVT8AtCXBkOwoGVzj485KtMjkJoqVfEpBM1x9GYIfRVeJvIxmNfZcDMoBZf57WloSRTLO_PsjemGCqIsMCJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2cbeca874.mp4?token=H69cSwawonRatsxWpKb0X_2RLx62frXfiKNDq8u91j09lU2cEb8iNPGjDAAB3ZsM3SrItokZXeforOfqIW9FvIJpPzJJGunXU-2ncspXNwR9vrkGUPIhZc8gJtjqtCiOpEv7J-ILPy1455L3gvQzSh1QanbNphbx-v9ieocE0O1lVG3HbSHQ2xCT2-aM2I23vX93jqvnYtsEUpkG3TFRFadvaRC7fG66XFfRu3AaSpCeVr-gmva7EnjTjUGAuHtiVHEVT8AtCXBkOwoGVzj485KtMjkJoqVfEpBM1x9GYIfRVeJvIxmNfZcDMoBZf57WloSRTLO_PsjemGCqIsMCJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به‌دنبال وقوع سیلاب‌های گسترده در نپال، نزدیک به 300 گردشگر خارجی مفقود شده‌اند.
🔴
این سیلاب‌ها تاکنون دست‌کم 17 کشته و حدود 400 زخمی برجا گذاشته‌اند.
🔴
گزارش‌ها حاکی است مناطق مرزی نپال و چین نیز تحت تأثیر این سیلاب‌ها قرار گرفته‌اند و عملیات امداد و جست‌وجو برای یافتن مفقودشدگان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/143905" target="_blank">📅 16:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143904">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae40c1a74.mp4?token=dMw8Q_rw4l2nbVAnr7OJvgNPnTCnbIEqHBmxbyde5Meu9c0ELv5bJoUF6RGae5dHBtNVJKB_BIVCdmFW5oaCfZ59gDQx-nyIeJ7pJuovaIx-sEN02jVipEXCm8aoetnlo_u-G9XtdHB-falKQ-pWJn-3MavBSokdw9gS-bLQjRXjZPt4ZRq428kwsk2YVo3FvCKuwBV73YMaUPwFmx_IH6vOH2d8EsRZaH66IjOI2fIe2N71Gp4gFHP8ysMxDkigH8wDX-wcsXQqtnBLx24lymhIFre_i7PdoS5DugqNtr3Gs1axcwHHX594RLWu1SCLmScOWXPu5XrVtaK4LENfwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae40c1a74.mp4?token=dMw8Q_rw4l2nbVAnr7OJvgNPnTCnbIEqHBmxbyde5Meu9c0ELv5bJoUF6RGae5dHBtNVJKB_BIVCdmFW5oaCfZ59gDQx-nyIeJ7pJuovaIx-sEN02jVipEXCm8aoetnlo_u-G9XtdHB-falKQ-pWJn-3MavBSokdw9gS-bLQjRXjZPt4ZRq428kwsk2YVo3FvCKuwBV73YMaUPwFmx_IH6vOH2d8EsRZaH66IjOI2fIe2N71Gp4gFHP8ysMxDkigH8wDX-wcsXQqtnBLx24lymhIFre_i7PdoS5DugqNtr3Gs1axcwHHX594RLWu1SCLmScOWXPu5XrVtaK4LENfwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار دیشب تجمعات شبانه: دلار شده ۲۰۰ تومن همتی یه کاری کن نگن که بی غیرتی
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/143904" target="_blank">📅 16:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143903">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXmvfpz553C-t-y2bk7LBfv-8GzhBt2vMJtpDE9OBqb_YJ-OZHQfuDU-luukhIUke4esGTxm0nrCbfQeSiRD0kY4Kv1rVU8jA6oqXpxQOUr954ZbNFDtQqDtjT3O4HNQ2i90Vh4RdgClN7B9kqXp9kCpCRnfZDWFXFx0fZ_PtJ2Gclp7A2Qja4vKiQhiO7wrfCRojgGzXA2Y0TmPStG_zR_3RNrqi5MUTIt16Ge6xoYT3B7yD_3b76dZKonWJJ1oMCk2_8ti3rBbnZU_b-TTIJqarsBQALGTFKPB2pWnpKChemHVSxAPS3Zure-MZ-989iyU6bfpUi8dZdVXFPUhrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایالات متحده، تعداد هواپیماهای تانکر سوخت‌رسان خود را در پایگاه هوایی العديد در قطر به بیش از ۹ فروند افزایش داده است
🔴
در حال حاضر، بیش از ۱۵ فروند هواپیمای تانکر سوخت‌رسان در امارات و قطر، و حدود ۲۰ فروند در عربستان سعودی مستقر هستند تا از عبور نفت‌کش‌ها از تنگه هرمز پشتیبانی کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/143903" target="_blank">📅 16:11 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
