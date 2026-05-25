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
<img src="https://cdn4.telesco.pe/file/SYz0mCiBSVEziyOpLUPVfjB28ylym2P-0RkBHRlDZEOmw72rHO6fZqI6AHNo649Q82Cj6mtWScdCE-YNmCZeJteo8k5bu8ih0UrBoj4yGYG5SFpTwtmMIzjxkji8fsRUSeFoX3AYbXBx-JnUYf5oaqsn6RFJeTJ5WPsZFec1B1z4-zoJ3oIDuk9N51frR8X1wqSSRCyz18iS86Pe38QIgPszjzp_cGZDS1RlxoyODiAv6cNe0-mM6Gl5A5MKC4hgEZO4tcYf6Or_iTUDJhzf9FxLPk2yLUa7-IlbacJaGp6Y_wl-hhClHa6NPxrBYACZ9ARnaIy9UDqlVnPK9iO-Aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 177K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 22:27:12</div>
<hr>

<div class="tg-post" id="msg-75869">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نتانیاهو: دستور دادم حزب‌الله نابود شود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/funhiphop/75869" target="_blank">📅 22:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75868">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فعلا تا وصل میشه بیایید برید از بات منجی کانفیگ رایگان ۵۰۰ مگی بگیرید پولشو بگایید:
https://t.me/TheMonjiBot?start=cFP8AVPe</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/funhiphop/75868" target="_blank">📅 22:08 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75867">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تو زندگیم همیشه مثل پزشکیان بودم
هیچوقت کسی جدیم نمیگرفت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/funhiphop/75867" target="_blank">📅 22:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75866">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نت برگرده روز اول ۲۰۰ گیگ دانلود میزنم ۲۰۰ هزار تومن میندازم جلو ساقی وی پی انم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/funhiphop/75866" target="_blank">📅 21:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75865">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پشمام معین میخواد واسه باز شدن اینترنت آهنگ بخونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/funhiphop/75865" target="_blank">📅 21:50 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75863">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فارس هم تو یه خبر گفته نت دست شعامه و باز نمیشه، تو یه خبر دیگه گفته رئیس جمهور دستور باز شدن نتو به وزیر ارتباطات داده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/funhiphop/75863" target="_blank">📅 21:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75862">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فارس هم تو یه خبر گفته نت دست شعامه و باز نمیشه، تو یه خبر دیگه گفته رئیس جمهور دستور باز شدن نتو به وزیر ارتباطات داده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/funhiphop/75862" target="_blank">📅 21:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75861">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhkzLzJhfunS2-RA1bzY4oVt_korGh1vH9bLAClc_oDe0kW9MFosgY68Co1VjNVJ7F8Q8Hq0T506EAP3plYnBHZIJFu_h7kTBZucviZiUVWPXcB0g0CT7YSRyVGP4KlyyJIdMPRn-K58GzbPP_9A12rrSlLv4Cla392PywZVHqxUbajOWteXiK5Ns2XjoQ6dn08Puyhp1VJhWZBicp8zsjIdBFc6LFJ5b4Jvvlqglger550N8sye-17-HykJrfIfXfVFVKPhPxDRI-2kj9wHmgHfGa2odewuW2kqyrcBOhYPFW3P6RV77dlLDtpP6H25xEql16cGePFU0kmNxSCOPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی: پزشکیان و کابینه اش گوهی نیستن که بتونن راجب وصلی اینترنت نظر بدن یا عملی انجام بدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/funhiphop/75861" target="_blank">📅 21:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75860">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚀
اینترنتی که قرار نیست وسط کار جا بزنه!  اگه از قطعی، کندی و وصل‌نشدن‌های اعصاب‌خردکن خسته شدی، وقتشه یه اتصال پایدار رو امتحان کنی
👇
🛰️
IRAN ORBIT
✔️
اجرای روان روی V2Ray / V2Box
✔️
پایداری بالا روی اپراتورهای مختلف
✔️
مناسب استفاده روزمره، AI، شبکه‌های…</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/funhiphop/75860" target="_blank">📅 21:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75859">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwHIHc8nYjFjbk6vwHNR8Nl-TznLd4_SwFpq8cpNP0r9E5fubaUMQ1pIwtukNgm0WRH01K03t0ROYw62IgAdyj3FqHJi5h26zLO3dmSCyTi9xgigWpQcQXtrHZm7h3V07N5egb_d8WE4h4eVmTgCVDJklhVys90-waLiVbFas5XaAR4aaNsIQgY-CEkVxI8XL-eiaSTlKE2D_LJF7NIrZlDY_cjjFNuIvoWFtXvX9kOHY-ggpXtwUiIBACJ9T23x22LPW9LCwvC3P1jFQSiE1ZuN_mXeJhr6mGgyh-gNniBvxdXRxH6XQO9DBpUfOZafJKLI439DMRVx2770Nyt6Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
اینترنتی که قرار نیست وسط کار جا بزنه!
اگه از قطعی، کندی و وصل‌نشدن‌های اعصاب‌خردکن خسته شدی، وقتشه یه اتصال پایدار رو امتحان کنی
👇
🛰️
IRAN ORBIT
✔️
اجرای روان روی V2Ray / V2Box
✔️
پایداری بالا روی اپراتورهای مختلف
✔️
مناسب استفاده روزمره، AI، شبکه‌های اجتماعی و سایت‌های محدود
✔️
بدون محدودیت تعداد کاربر
✔️
سرعت خوب + اتصال پایدار بدون افت شدید
⚪
1GB = 150
⚪
2GB = 290
⚪
5GB = 700
⚪
10GB = 1300
⚪
20GB = 2500
📎
سفارش:
🛒
@IranOrbitBot
📎
پشتیبانی:
🙎‍♂️
@iranorbitowner
🟠
@IranOrbit</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/funhiphop/75859" target="_blank">📅 21:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75857">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فارس:
یک منبع در وزارت ارتباطات: مصوبه بازگشت اینترنت به وضعیت قبل از دی‌ماه ۱۴۰۴، دقایقی پیش از سوی رئیس‌جمهور به وزارت ارتباطات ابلاغ شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/funhiphop/75857" target="_blank">📅 21:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75856">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ:
ما در عملیات خشم حماسی ۱۳ سرباز از دست دادیم تا اطمینان حاصل کنیم که پیشروترین حامی دولتی تروریسم در جهان به سلاح هسته‌ای دست نیابد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/funhiphop/75856" target="_blank">📅 20:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75855">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رئیس شورای هماهنگی تبلیغات اسلامی در تهران:
هنوز هیچ زمان مشخصی برای تشییع سید شهدای انقلاب اسلامی، حضرت آیت‌الله سید علی خامنه‌ای تعیین نشده است و مردم به هیچ وجه نباید به شایعات دشمنان توجه کنند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/funhiphop/75855" target="_blank">📅 20:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75854">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏الحدث به نقل از منابع آگاه :  ‏ جمهوری اسلامی شرط انتقال اورانیوم با غنای بالا ‏به چین را مطرح کرده است.   ‏همچنین احتمال دارد فرمانده ارتش پاکستان به ‏دوحه سفر کند.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/funhiphop/75854" target="_blank">📅 20:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75853">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏رئیس بانک مرکزی جمهوری اسلامی پس از سفر هیئت قطری به تهران برای رسیدگی ‏به پرونده پول‌های مسدود شده، به قطر سفر کرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/funhiphop/75853" target="_blank">📅 20:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75852">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaGULaLV32k2ihuLMN62C6JptIS9i6HXrIPLjQdY6TJzY0gC_rgExof3fNTFmKKigD4Ekk72eAprvYtFZWaLMjjektRA1b1C2ETs3YRyZa8bzwtXss4siHDY86uyZnUkoUPACu3waS7m1QA3DNF9bgHuBqeqCNUsYSHgcF6TuQeRg2Giq1ix3Rg9hxcNWeBEiZGfRo0bdt9OzvN65OQlB-f6PmDQsgbNRIhMzM49z0v5P9doxZUMbfttdJU3k7ef1mZe1LQArk0Jr8GZi0Xw9-xMnG2IA9DZsLxkQG2JkH8ofwA0HPuE_RKCngYUJr4NNENpqWaCO44lROPODcKHdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای عباس پرتوان برس به داد ما ملت ناتوان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/funhiphop/75852" target="_blank">📅 20:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75850">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سینه مرغ ۶۵۰ تومنیو کجای دلم بزارم</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/funhiphop/75850" target="_blank">📅 20:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75849">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">منابع به شدت معتبر فان هیپ هاپ:
مقامات
در اسرائیل پیامی از ترامپ دریافت کردند که مذاکرات به جایی نمی‌رسد.
او بین حمله در آینده نزدیک و حمله در حوالی ماه اوت (۶۰ روز دیگر) مردد است.
زمان ترجیحی او در این مرحله، زمان دیرتر (نزدیک به ماه اوت) است.
در اسرائیل مقامات از این موضوع به شدت ناراضی هستند و با توجه به وضعیت در لبنان تلاش می‌کنند او را تحت فشار بگذارند تا زودتر حمله کند، اما فعلاً موفق نشده‌اند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/funhiphop/75849" target="_blank">📅 20:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75848">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏الحدث به نقل از منابع آگاه :
‏ جمهوری اسلامی شرط انتقال اورانیوم با غنای بالا ‏به چین را مطرح کرده است.
‏همچنین احتمال دارد فرمانده ارتش پاکستان به ‏دوحه سفر کند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/funhiphop/75848" target="_blank">📅 20:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75847">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رویترز: قالیباف و عراقچی با پروازی فوری و ناگهانی اکنون در قطر حضور دارند. مذاکرات باقرشاه و پروفسور عراقچی در دوحه بر پرونده تنگه هرمز و اورانیوم غنی‌شده متمرکز خواهد بود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/funhiphop/75847" target="_blank">📅 19:50 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75845">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ouump2ozjG725j4K_zqY8IyijR_-cFiLT8xU49APd536kJUv4sK1n11JhSCBN1-7erhEnTWM3hdKBKSredfteJGUfSubrQbrcaHVPiubaWH5aEd9lF784CGFy1jv0TaGsyDT6NX2j9lY4g36Ef9y0bffah02iY5OHp1q6acwuFV7NOnEJuQ9_YAcJPubO_RyrPiVzDQ7RPswLod4bL8VBCP6KIBf_3_Kn2gN9-PkMMIbGhQ1nscwsjCC2o8-T9kOzNAV1onqhMX4pDhTOdrJrxagZ_kDos0cS2K3sDK5wjS1GPPdBgysYWOcjVwZQ2aVc_GR83hsEB-si_xNkarvfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qbhbqEo_qp7ueipQb1Z8nka7SokCXVLB35o7YEA28SIGfalBww1SXFYu3W_XsSwdH6ERnxMvhx-8uefPf6Z88YgMUHkZdLdKiQQrH_bhs2emp-Cv3Lxd8t-ixcJoJQeoGMEx3YqFrtxD5zpOKrj8M4KnDigwG9gmr-uQieyc9E3LL3ZX1Kt5eYbyUvqnkK2MpaDqhEDh8V2nru2vXGujhxaiRggso2zSBzPRhMrjbDPEDAGG-OQmUS1ZiY5DXzgj3HhTwnkECWKcPiHhZt6z56pyZHDEdTDYrks8a2kfrl_P048WA4nbjdThbULMHA4M92zNHNKJtgfOo-w3QThhuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الان مثلا خواستی بگی تو خیلی متفاوت عمل کردی آخه حرومز
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/funhiphop/75845" target="_blank">📅 19:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75844">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmG4kxDEi4sRlPy0xWFZdbXOtDrdkqE59aTG77ZYkIF1anrXj1xosqNcT-MffEBN-B4tACNqBxIsu0Phc-sqn8KkqZN1JJXLQJXey7v3TrUoSlBC0VuGjGEFyFPVVPAuPzrqcaj8fIt-PoQkc0aROQeQYYSV8m5o1N5EqO7s-aXfW7Rjik_qAUl64aSxmG8M34ngmq_UWcAofb7_KliQ5uYPsHErEuueQwcF89uRzhZmDjwCEdimcbck64VYWjbOKU_ElCLSAix99pNMWuZMy5S5qJFGaJTF8m7An6Mrnk4s3E0dde0av5oewrBPTrJL4B2ELHqKwx7mPrtYyXlGUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب سری ای شده سری اسپرز و تاندر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/funhiphop/75844" target="_blank">📅 18:31 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75843">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وال استریت ژورنال:
مذاکرات ایران رو بحث برنامه هسته‌ای و رفع تحریم‌ها به بن بست رسیده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/funhiphop/75843" target="_blank">📅 18:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75842">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">باستونی دید فلیک نمیخوادش حالا میخواد بره رئال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/funhiphop/75842" target="_blank">📅 17:57 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75841">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgD-D3UKoDzAvnSc2GBz6IJXwBY7nHCY3zIn5rwR2XB4VDBMpSJvxOQDlif_f-XxdsaMO3rz-K1NcQjk0NKTD_w3b0S23KCvt5Fc-S9GSoz_dzY1IMntda6bYpcIZ-O_lEVnZPe6saxpGTTdO7v6l7Sc-LOgZ8WbLjEnqtLHW-h57weYvop6J-8t9C8UtecDADItjdp3jZcGIvXGgnYLvd4_F8arp-63Dlqj81HoEAY59ZP4ouq70vaBlqrzgQrJzFTuMUe2blsLsWDqvDl541rCRHxGVWgRR5cSYSY5tYBuhG7F3pxbseFhkPpeTYpmXG8D64lXR0CQ7Dha6xVVgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس: سامانه جدید آرش کمانگیر یک پهپاد متخاصم را بر فراز آب‌های خلیج فارس با موفقیت سرنگون کرد.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/funhiphop/75841" target="_blank">📅 17:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75840">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odvy8hHw0f_ViHfZYyeCI2MC9DyxUZXqYHsYluxN7ZaC8Ji40upxWdctm1_1ilhHwxizQpOxx3mqwvX7moagRkpAcImY08caMsa1yWcfB_if7QbU3-1QhcJTuzxnKVQRw_G0KTxZkgY9ezL_eNB_VbNzWHhuUCs45PJTT_nJPtlaEB_N4DVvNTiiGbTO41AdbR_ix13FaAchNHv6JLojiGP8XHx9Bi6FPxy3-rCT718_w-CcLctwo7g7gIjZL4gRnFh5XjDas5U-cihnobSuJKnNYIDGeKuazjHLAS9lVghgxdkQy3j-yhkg1SMs34lMXE1MjU933CL4Dljsrf--_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
سایت بین المللی
bet120x
✖️
👍
دارای مجوز رسمی Gambling Judge سوئد
👍
💳
شارژ حساب از طریق ارز و
یووچر
و پرمیوم ووچر
💳
تسویه حساب دلاری سریع
💊
بیمه شرط میکس
⚠️
فروش شرط
🔔
ویرایش شرط
3️⃣
2️⃣
🎁
20%هدیه واریز از طریق ارز و ووچر
┅━━━━━━━━━━━
🎁
10%برگشت باخت به صورت روزانه
🎁
10%برگشت باخت به صورت هفتگی
🎁
10%برگشت باخت به صورت ماهانه
💻
ادرس ورود به سایت:
https://bet120x.com/fa/?btag=971470
➖
➖
➖
➖
➖
👈
آموزش واریز و برداشت دلاری
👉
🔪
کانال اطلاع رسانی:
👇
g4
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/funhiphop/75840" target="_blank">📅 17:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75839">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ پیوستن به پیمان ابراهیم (به رسمیت شناختن اسرائیل) رو در یکی از بند های مذاکره با جمهوری اسلامی قرار داده  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/funhiphop/75839" target="_blank">📅 16:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75838">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یعنی قراره قاتلین
حضرت سید علی خامنه‌ای
💔
، قاتل خانواده‌ی رهبر جدیدمون
💔
قاتل سردار سلیمانی
💔
، قاتل سید مقاومت حسن نصرالله
💔
، قاتل شهید فقید اسماعیل هنیه
💔
، قاتل دانشمندمون محسن فخری‌زاده
💔
، قاتل سردار حسین سلامی
💔
، قاتل سردار محمد باقری غلامعلی رشید
💔
، قاتل سردار موشکیمون امیرعلی حاجی‌زاده
💔
، قاتل شهید فریدون عباسی
💔
، قاتل شهیپ محمدمهدی طهرانچی
💔
، قاتل سرلشکر شهید احمدرضا ذوالفقاری
💔
، قاتل سید امیرحسین فقهی
💔
، قاتل شهید اکبر مطلبی‌زاده
💔
، قاتل سردار سرافراز عزیزمون علی شمخانی
💔
، قاتل فرمانده بی‌بدیلمون محمد پاکپور
💔
، قاتل سرلشکر عبدالرحیم موسوی
💔
، قاتل سرتیپ عزیز نصیری‌زاده
💔
، قاتل عزیز اطلاعاتیمون اسماعیل خطیب
💔
، قاتل شهیدان غلامرضا سلیمانی
💔
و مجید خادمی
💔
، قاتل سردار سرافرازی که بر بستن تنگه اصرار داشت یعنی شهید علیرضا تنگسیری
💔
، قاتل رئیس جمهور آینده شهید بزرگوار علی لاریجانی
💔
، و قاتل شهیدان دیگر مانند محمد کاظمی
💔
، حسن محقق
💔
، داوود شیخیان
💔
، محمدباقر طاهرپور
💔
، بهنام رضایی
💔
، اسماعیل احمدی
💔
، علی‌محمد نائینی
💔
، مهدی رستمی شمستان
💔
، سعید برجی
💔
و منصور صفارپور
رو به رسمیت بشناسن؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/funhiphop/75838" target="_blank">📅 16:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75837">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ پیوستن به پیمان ابراهیم (به رسمیت شناختن اسرائیل) رو در یکی از بند های مذاکره با جمهوری اسلامی قرار داده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/funhiphop/75837" target="_blank">📅 16:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75836">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دقیقا همونجا که با خودت می‌گی این دیگه ته زوال عقله، ترامپ میاد برات به صورت عملی اثبات می‌کنه که تازه کجاشو دیدی:
مذاکرات با جمهوری اسلامی ایران به خوبی پیش می‌رود!
این فقط یک معامله بزرگ برای همه خواهد بود یا هیچ معامله‌ای صورت نخواهد گرفت — بازگشت به جبهه نبرد و تیراندازی، اما بزرگ‌تر و قوی‌تر از همیشه — و هیچ‌کس این را نمی‌خواهد!
چون من این همه برا توافق با ایران زحمت کشیدم پس به صورت رسمی دارم می‌گم تمام کشورهای عرب هم باید فورا و به صورت اجباری به پیمان ابراهیم (عادی سازی روابط با اسرائیل) بپوندن وگرنه خیلی ناراحت می‌شم.
راستی جمهوری اسلامی ایران هم اگه دوست داشت و با ما حال کرد خوشحال می‌شم اونم بیاد تو پیمان ابراهیم.
ممنون.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/funhiphop/75836" target="_blank">📅 16:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75835">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رویترز:
قالیباف و عراقچی با پروازی فوری و ناگهانی اکنون در قطر حضور دارند.
مذاکرات باقرشاه و پروفسور عراقچی در دوحه بر پرونده تنگه هرمز و اورانیوم غنی‌شده متمرکز خواهد بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/funhiphop/75835" target="_blank">📅 15:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75834">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3wZ2qZa_hpnJEp4F8dhWn-tA4DhT1uYCAUjz4IMuR8q1ImjvlnGIZr9Q5hQ6Ueza5d6g6jaSu7TyGY2n5l5V5HFBCakaCWIiGeq3HF60i3EpXQy9yFBGFRQEdylxHV7R9Vt4vQIxvwDC0ZpCWej6wSH5HtHeR0ldHCWhJ37imUaCPK-_Qs0fG_Z4SuMYRwTxx28_5X6RuJSolSWBZIxmHE74N0C1ofwoafzGfR8FH4hYqH4vVjkWqow0-JQ7zK9RzXRdk_W8H8i8RbzvZFg2x0gJi-8Kgmdjlm2huJg2nRCIvLRpnAnYefx1UjW8tDIGkQR9UvtQCBQ66P7YjPIDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست تیم ملی بارسلونا برا جام جهانی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/funhiphop/75834" target="_blank">📅 15:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75832">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بنظرتون بعد از تیم فوتبال جمهوری اسلامی کدوم تیم شانس اول قهرمانی جام جهانیه؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/funhiphop/75832" target="_blank">📅 14:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75830">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhHC0weZinNpZONOO32W-QguleEiqka5uhZmvBknmFNQdvHN-cNueOWwWScTp0qFitPssYlM0m_ePs9ITzlZBhL8edn6nlWgMuEWDmZqBVxSoPV1hX9fguBGOOukFU4kD6m-SabsDDOR0W13yNTs1pcRULMdz-qK_1gI11urfPDeUFMfGNioEqEjQSC7d1Ka2p4806EH0RjegvfNlEj8zH7SJdSIP1sQgq77W64X9yAWcbiEioI603UOAVdUW6l9_tnos3y7bocyQaLoQqGmd10VGD1-UxGq0sxSskQNCM2ee21ARzwvYrYmAC21HImZw05-9PlRDQLMqe1cEgrtxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه داداش چیزایی که به من می‌گید اصلا هم درد نداره:
من به همه دموکرات‌ها، جمهوری‌خواهان جداشده و احمق‌هایی که هیچ چیزی درباره معامله احتمالی که من با ایران انجام می‌دهم نمی‌دانند،
می‌خندم.
یا معامله با ایران یا عالی و مفید خواهد بود، یا اصلاً معامله‌ای صورت نخواهد گرفت.
این معامله برعکس فاجعه برجامی است که دولت ناکام اوباما مذاکره کرد و راهی مستقیم و آشکار به سوی دستیابی ایران به سلاح هسته‌ای بود.
نه، من چنین معاملاتی انجام نمی‌دهم!
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/funhiphop/75830" target="_blank">📅 13:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75829">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حاجی این دید کافی نیست اینجا
اومده پیویم داره اسپم می‌کنه جمهوری اسلامی محکوم به پایان است
بمنچه اقا</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/funhiphop/75829" target="_blank">📅 13:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75828">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sm-mex0Hq0aqv6xSjd-iC0g4oxMrN3JQSbJYD87JN9EbpLnNnZ7n90LhGFrFuffSDNVXsGAe5DpY2oEmf9cGHpu3qYQDzZio4dDtcCmxmuVZqWTCNIPQ37s8ijvs9fqlDpekkg8fTvXgZ_8k36p4vFEGgQeIl01gTe3GJu9RNKmQs--8tbmPFCyTnoR2lPhMRFFwztTq0BGtB4CayRkLOT2U28IeDTNoyf7BgOl8ObajA-HOyUpeUjV8CB1ebMkeKyrbNuSdDbynUUgPdFlj-m6kAj__sBSxOKbSVNzBSOW9xHpZoGgKF7GAqgGDlEf1vy1kSnAIZS5gJeHnakXvJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو توییتر حقمونو پس میگیریم</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/funhiphop/75828" target="_blank">📅 13:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75827">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fw5kB8688lrDWHsmI-5Fvxt70_Qtp2H5lEn49lOY4B2e8T3aSQmExLT-9yc5Pg-kSk9S6-Sjtoq7n2rlL3Q4nh_auo4SiqouT2amuqrQZqO9AOh-It5hpv9rULSKojgd1L1sUK-rjKWBZnP1IJQy1lJY-JMlcr-u9ttmgYtYIHDldnoaxzXMbw8fa60A4fgcZoHjhIuhCSL2KpCyrx8fMdSPFIJT3Up-JzNYhrSlfk48aedQigx7tLR_7fbRdMVj-pKcIyth-RsZTVDpFMlBo2byYv6VkWDBhG9eTU1K8UA1QysXbF9QALnHGmRYenQChXRtJzzvbosD3Y4_awZs2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو توییتر حقمونو پس میگیریم</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/funhiphop/75827" target="_blank">📅 13:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75825">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">داداش من خودم اینترنت بین المللم ولی الان بحث، بحث امنیته
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/funhiphop/75825" target="_blank">📅 13:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75820">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بعداز قهرمانی ایتالیا تو جام جهانی ترامپ عملیات نظامی رو علیه جمهوری اسلامی آغاز می‌کنه.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/funhiphop/75820" target="_blank">📅 13:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75818">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مثل اینکه بازگشایی اینترنت بین الملل تصویب شده
مرسی از مسئولین محترم
😍
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/funhiphop/75818" target="_blank">📅 13:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75817">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فرمانده‌ی قرارگاه مرکزی خاتم‌الانبیا:
پدافند هوایی ایران در جنگ تحمیلی سوم به مراتب بهتر از گذشته عمل کرد؛ ان‌شاءالله سامانه‌های جدیدی را به‌کار خواهیم گرفت تا بیش از پیش با حملات هوایی دشمن مقابله کنیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/funhiphop/75817" target="_blank">📅 11:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75815">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBJI-1nQofdAbTAknj4MYuJebdrsRaxOqfgK-h-B20iL_R4fG7OeGSY0-PkRWWaKo3vMpsCo-amdLdwuzdZxB_jF97wL_nKp1DthwJasu0BdBEyrNrZpaszS5Zurd_YhGYUrrGAYMDhjzgXtDeSn2xTysl0nMXgqd6VR7ngimw8gt_0YEdA326h8gbdDjVAhXTcZxgXGq5LoxNfuW2CMj--plu7ld7qKDTVni37_ij_ZtVabbwkJo4y7KgUEYTGKr9qFsvim_cvK-xOayTSHw99SmB4IibdxalxapJ0M0_Ewyzq73MNM4UmRrnq1ACwGsfB8glb0VuBk4f7rS-7Mxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکدوممون از پشت پرده ی سیاست مدارا خبر نداریم
سیاست خیلی کثیفه پسر.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/funhiphop/75815" target="_blank">📅 11:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75814">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e9742a944.mp4?token=A7KERJoZtSnCTmvNv_JOZRT0wuh4awau9U85Pd5Axy_gr-8S2oxJ2R7JbdxnQ5rI40s4IIo7h-vZLFTY9CBvzHfk7-KdC6qnP9kSSbCO5DtLilWvoo32ifMKE0jmkH9Z0lvlDrpBOA3iF9OXzHZeiERWbM0Q7ijITveSjKV5OshOL-O6K0-R5Vv8-iqpj3aqcZroujREqnK9Dk6KEmmBvdJx_4dWaz4JRNZgk5KlghrcT8Ehu2u0bJQs7P3FggRqNo27OH14P5fXG1a1RFJNBVyiZOh4hSJmacqGE6q7B7pcbB69W0vpLvlYS02h24MLziHgmMX-f_p_XP7fFOZ0gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e9742a944.mp4?token=A7KERJoZtSnCTmvNv_JOZRT0wuh4awau9U85Pd5Axy_gr-8S2oxJ2R7JbdxnQ5rI40s4IIo7h-vZLFTY9CBvzHfk7-KdC6qnP9kSSbCO5DtLilWvoo32ifMKE0jmkH9Z0lvlDrpBOA3iF9OXzHZeiERWbM0Q7ijITveSjKV5OshOL-O6K0-R5Vv8-iqpj3aqcZroujREqnK9Dk6KEmmBvdJx_4dWaz4JRNZgk5KlghrcT8Ehu2u0bJQs7P3FggRqNo27OH14P5fXG1a1RFJNBVyiZOh4hSJmacqGE6q7B7pcbB69W0vpLvlYS02h24MLziHgmMX-f_p_XP7fFOZ0gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکتر اسماعیل بقائی، سخنگوی وزارت خارجه:
اینکه ما به نتیجه‌ای در بخش بزرگی از موضوعات مورد بحث رسیده‌ایم، درست است.
با این حال، اینکه بگوییم این به معنای قریب‌الوقوع بودن امضای توافق است، هیچ‌کس نمی‌تواند چنین ادعایی کند.
سیاست‌گذاری و تصمیم‌گیری در ایالات متحده دچار نوعی تردید نهادی شده است.
تغییرات مکرر در مواضعشان وجود دارد؛ در عرض چند ساعت با دیدگاه‌های مختلف، اغلب متناقض و متضاد مواجه می‌شویم.
این روند هر مذاکره‌ای را مختل می‌کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/funhiphop/75814" target="_blank">📅 11:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75813">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">قالیباف برای هفتمین سال متوالی، بر صندلی ریاست مجلس باقی خواهد ماند.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/funhiphop/75813" target="_blank">📅 10:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75812">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OW6DmSQ4OFeM5yF_1OGraCpQHHs1YHkLmz0N6gmocV6A5j4cSkMpgo5EZpHt11cv0qsmZM2FllmlLv53DhI0yn5OFJWF7iwEFB_h-fEiFnSvLxWUyveDQMHyYx210lz0NQLxQ3QIGn6MWYdwU3RYJx7vIV1aH_Fv4wm7G_cpwhd6_BQiN-eKtGZuiOy3OskbIBiGQxzLOTnQ_17NnK1-OiDYqz81DlJQn3rtKb71XsnsoDYP-2j7uVNcQ3dM_hKVZv1AoELsyo0TgCK44wXe79AZrCZH2eFTw8K4-iVfhXPRR9ZbhW_h8I9txVKngqKLMdrI-vuYMev6S9FNlbgoiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو این روزا و این شرایط این عکس رو گذاشتم که بدونید هرموقع که توبه کنید خدا هواتونو داره و پاداششو میگیرید.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/funhiphop/75812" target="_blank">📅 10:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75811">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsO29k5WGEQFE_A-kEp04r1R0kEZA1KQTMRCujYxV7w4zNI3skG0NagUVekqjOyKtSS1kQ_XAbMSBL8RcaUsxOfixpVvxDsjk-o6Y76l4_qf3atdJDUnOXGFuzO2dzGx0gwYCyC9ufdj6ZSP2y8yCpe1Ub3qR9TH1M00Uh0eCh62TQs0k6alWtgPjR5v7Fr6-JM8TMQUdkeoBx1QeiZfYBxgyTyV9ojyKLODJdTOA8fgkZJ0nvjl_7aZGX-_fhNdzQYEJ0AtI9vm3m2dv6Ak-pB8k9ZgBSwy6AaLHu9vcbYqSQMSpAarSI1HboLehsYEwQXjuJrgeEPaMJf2p_hUmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتیجه کارا ترامپ:
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/funhiphop/75811" target="_blank">📅 09:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75810">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/itD-BdvRbkZhFvBhd0yN0y8ZrU-eA_6rE1GaMXfoKoA-upmHC0HhF6hEkMj0Kyd312_v2oPgFoIS2-iOCd0yotyodpfCzaC8nzHwm15_Q3B4Tl683GJkduZr-NktEJJt1SB1q5hQKit9j17ik_My3RaXExL5Txct2KyuiZCBe_su_qHaWWa-I4xRvaPQQjMbEdqAksTUkVsgLOs1WhNF0tdAu3pY1wn5oIpCdKswY7nPYoT1qXQb3W4T1JE2C6BcEaIDzGo1y5ENL1kP45VTi5E3r8ZdCjXnlzkahiQzd0PEbq47MaMdoQdqlps8dKY1DhB7x_a5_JAzeT_wFLWV2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ رئیس کمیسیون امنیت ملی به تهدید ترامپ: قابلی نداشت
.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/funhiphop/75810" target="_blank">📅 09:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75809">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/75809" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن اندروید سایت جهانی دربی بت
💰
اولین سایت جهانی با امکان شارژ و برداشت ریالی(کارت به کارت)
🔗
برای ورود فیلترشکن روی کشور مناسب قرار دهید مانند فنلاند و المان و....
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/funhiphop/75809" target="_blank">📅 09:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75808">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AExM-H5FJFT5HIEQNG88bBjxOiImaTk3aR3wkWpfU_UJ9fAwTgSmV_VVDPyG4fysAlh68cU5Xa7o2F8wzkf0zEgti0dnPjxF5plJL9r12RqK0KZl898ag2HDTy4abArSZIE84Wevccqnj7v9Qomirdb_uW5uhRzpF0N5FqOIO1mqOCuPvAlwLAogGlefXaQBv-jYptbnQTqA122H8cVK17fXgij67b76u5JksESfpQTuUi3M6tIBwF9LvVPN1rA57L5T8ufoewytz2ysUVBTUY2wh6xgM9SAImHA44cjO6-fwtwjYCR1TZ1IN3S2qEGC0E6VGV0lR-nQdEFRut4LPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :r4
🅰
🪙
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/funhiphop/75808" target="_blank">📅 09:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75807">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رویترز: اسرائیل اعلام کرده حتی با توافق، می‌خواهد آزادی عمل نظامی علیه تهدیدات ایران و نیابتی‌ها را حفظ کند. نتانیاهو همین را به ترامپ گفته است.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/funhiphop/75807" target="_blank">📅 08:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75806">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mriMSDPF77gKrHR09Z7kK-31eC_el_vBPQIN4JvWRRWo3SBmjHokNhwHieGRLHdENosTgLZA24830jJ1uBhVA-zwA00yNpnuTCMDJFn2lRAxNgbvaVRiaPbeM3-92hC8d44dPLKjaIYdAjz-jIFh2mtpTej1O-TG8X4by4GqZF8JQGU_lFtqP5GhWcufWOlQ1eE8M78zRKfeZ1u8ULDuLkeIwefoJPaXgHCN8174dbrSSMmERUM1HpUZdCh0uIe-VW8VQOeHlMTCUmRsMoL5hoihNxa8qliFvP_g3aJLkSVS7wgxY46BSuy7-TpwrV9ymQSJANxMijIThTS5W4vQyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏بیو پیج اینستاگرام ترامپ بعد از توافق</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/funhiphop/75806" target="_blank">📅 08:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75804">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKiXuZnWPSfsimd1PWoO2dx3Lbp8B1z1mn1qzlSRV1M7yrp2gJ6juya1XriW3K_iDgtxxHD4TLGZI2yvYwptIId5TeFsZUm1jeYBmfzun_muoNnpdwx0vAdpFOueO8Me6S_ImfrGY9jMBDnxFc7prN_XkBwEWHPILQBUJQ857YphxyX2ImiEDgMgHN5gCggCO6yJOHmv5pVPOZPTq09c7y_8ODimFog3GbtqVwB2hDXTQ0EbTAnb0mX7EfyVDmXqOUMfax9CF0LC7pNZbiqi9CcLALUNPPL97x-zh8u8nBWFhgqVIFIQvLo1fzR0Ra3YxUnlSCn6M96IAcgQMFEq0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان ببین کاراتو
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/funhiphop/75804" target="_blank">📅 08:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75803">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تسنیم:
حکم اعدام عباس اکبری، از اغتشاش‌گران و پیاده نظامان مسلح دشمن در ۱۸ دی ماه در اصفهان، به جرم محاربه و تخریب اموال عمومی، امروز صبح همراه با اذان صبح اجرا شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/funhiphop/75803" target="_blank">📅 07:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75802">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">۱ ساعت پیش چندین انفجار تو قشم گزارش شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/funhiphop/75802" target="_blank">📅 06:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75801">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0009c0f177.mp4?token=flgfsiYi_LaDWE1jO9Csq0qdK2ROZcWZMAnpdxzglak_ZtW9RvOtHMC-mminZSN7rVnx4ikwd3ZYndWcX4tMobJ2bPb7rzoGvnUNe4inFq-9ufnbR765-ep8RAwY5eL05wnN9OJrQltlA1PHl7mETGbJj8KixlQ3YxBnjsRSQ64AQL7xjbhJrTByE7DEoMvQD_L62xnqhrM4PrxQPO-6u5i6Cs8PeHCS-6hQGMCk1JjUMVt4Pd5XvVR1KSJ5EgaHkEMYuKw3ck_C9vHBE3LKZPl_XGRy0XGZ60MRah1d6OANsneDcRLqe-eVHqa6nz0gZdb-hIibt4X7GHRTaHk8nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0009c0f177.mp4?token=flgfsiYi_LaDWE1jO9Csq0qdK2ROZcWZMAnpdxzglak_ZtW9RvOtHMC-mminZSN7rVnx4ikwd3ZYndWcX4tMobJ2bPb7rzoGvnUNe4inFq-9ufnbR765-ep8RAwY5eL05wnN9OJrQltlA1PHl7mETGbJj8KixlQ3YxBnjsRSQ64AQL7xjbhJrTByE7DEoMvQD_L62xnqhrM4PrxQPO-6u5i6Cs8PeHCS-6hQGMCk1JjUMVt4Pd5XvVR1KSJ5EgaHkEMYuKw3ck_C9vHBE3LKZPl_XGRy0XGZ60MRah1d6OANsneDcRLqe-eVHqa6nz0gZdb-hIibt4X7GHRTaHk8nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدان بولیوار: معترضان ونزوئلایی روز یکشنبه در میدان بولیوار در کاراکاس ترامپ مارکو روبیو را آتش زدند.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/funhiphop/75801" target="_blank">📅 02:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75800">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c85e6431c.mp4?token=TrxYnTiePue7qQ3S9w9HwTVZEVEe8OXBtCDNADOtZNnWLH1SNT_rJeodDLLzh9JgbCdzY5K0aoOyyE3crzm-Ysg_FvTb4VfNQv4RVBlqinfhpEAsHAuwpgkr2s-IGdfgdUusgcg6RRvVO-sZ6jaeRfknICbYWkqig2WpCYc6aJipFcTrkCA7Znlc5GqFh8mCs-iemOnVW38EhkaIlExJnL4rgdEXl9XMwJSnLQIh5-NAVqo8Cic23MTmkecNdIV9OFoM5vHvIeTnMTTyiDSni0RD3rwO4i8_a6CfRQ6qg7fmFJplLesyVo-W0gZvBpBsIu-Gn0nTWsBFR7wukBX5YaAD7jHZFRG3CHO5OTFfe0ksE5GvN8meiHoN5EQzcz2ms8uoHuJ5lUnmvX-9_C3hf1JZ4vabsppRsWRWs4NpO7N8dm8KMTs2WJP8mA9cvy4xltAMLWFmjvUqUZDtlrhwfx66_oa69v4h_VYaHy99gmYXwEEnZGxvaA7Fo4Z6I4_FBAzgPP9wPusQ2PgHBtwdsJbj9dMnSdyJBiFITjsRb3sxNQN34-TW8jbMAGGRuL4ZOqczS3eabhXDlOQ9a1c02_0GmjKobjSiBdQijSwG-cKzqZLlMaU1PP6N5a3m5aEw8NHGjNgihvfCSXEAv0JIysBTQAPjXesVgiSR_74ZcOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c85e6431c.mp4?token=TrxYnTiePue7qQ3S9w9HwTVZEVEe8OXBtCDNADOtZNnWLH1SNT_rJeodDLLzh9JgbCdzY5K0aoOyyE3crzm-Ysg_FvTb4VfNQv4RVBlqinfhpEAsHAuwpgkr2s-IGdfgdUusgcg6RRvVO-sZ6jaeRfknICbYWkqig2WpCYc6aJipFcTrkCA7Znlc5GqFh8mCs-iemOnVW38EhkaIlExJnL4rgdEXl9XMwJSnLQIh5-NAVqo8Cic23MTmkecNdIV9OFoM5vHvIeTnMTTyiDSni0RD3rwO4i8_a6CfRQ6qg7fmFJplLesyVo-W0gZvBpBsIu-Gn0nTWsBFR7wukBX5YaAD7jHZFRG3CHO5OTFfe0ksE5GvN8meiHoN5EQzcz2ms8uoHuJ5lUnmvX-9_C3hf1JZ4vabsppRsWRWs4NpO7N8dm8KMTs2WJP8mA9cvy4xltAMLWFmjvUqUZDtlrhwfx66_oa69v4h_VYaHy99gmYXwEEnZGxvaA7Fo4Z6I4_FBAzgPP9wPusQ2PgHBtwdsJbj9dMnSdyJBiFITjsRb3sxNQN34-TW8jbMAGGRuL4ZOqczS3eabhXDlOQ9a1c02_0GmjKobjSiBdQijSwG-cKzqZLlMaU1PP6N5a3m5aEw8NHGjNgihvfCSXEAv0JIysBTQAPjXesVgiSR_74ZcOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موزیک ویدئو شکیرا برای جام جهانی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/funhiphop/75800" target="_blank">📅 00:38 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75798">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">هیهات از تسنیم:
خبر رسانه اسرائیلی درباره متن تفاهم کاملا کذب است.
آی ۲۴ نوشته است که مقامات آمریکایی می‌‌گویند ایران تا زمانی که انتقال ذخایر اورانیوم غنی‌شده خود را آغاز نکند، هیچ‌گونه تسهیلاتی در زمینه آزادسازی وجوه مسدود شده دریافت نخواهد کرد.
همچنین گفته شده در این مرحله ایران تعهداتی درباره جزئیات موضوع هسته‌ای داده است.
ولی دروغ می‌گن ما هیچ تعهدی درمورد هسته‌ای ندادیم آمریکا هم تو قرارداد گفته قراره همین اول کلی پول بهمون بده چشتون درآد.
بر مبنای چارچوب اعلام شده ایران، در صورتی که آزادسازی اموال بلوکه شده اتفاق نیفتد یکی از خطوط قرمز کشورمان رعایت نشده و تفاهمی در کار نخواهد بود و به همین دلیل احتمال عدم تفاهم وجود دارد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/funhiphop/75798" target="_blank">📅 23:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75797">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خب کصکش وقتی جفتمون می‌دونیم کاری نمی‌کنی اینکارا برا چیه آخه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/funhiphop/75797" target="_blank">📅 23:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75796">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRF0-e4kG3dK2fkuptJnRRFJhfR13QifCdscOTeIgvByExu0gZaxuM_R2D70BtX98D5GpEcxOSs9TS1GUt26XICsmLdItATet0B939eP-wVfXquYgHYF-Hv0n1ZEoIXi-MFMNO7-ltx-Uh9Cp51y_zJUVsd9_TFHOQIuVs2CdGRfAm0BrTV3pMujpxTBovKfWmsbnvURQwBaqYQqmXJj4AHT5nVMguSFxfHXcWaRcuz-o0M_H95MJKXPohvdaALFKItlktdl92jCTde-R51fsix3zELDIYcCdCiGOopVj-pCqsqtl7MMoLRHGqKt5Zb6UR_bL_KxQw681S6U7F8wnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب کصکش وقتی جفتمون می‌دونیم کاری نمی‌کنی اینکارا برا چیه آخه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/funhiphop/75796" target="_blank">📅 23:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75795">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وحید جان بنظرم چنلو تخته کن بریم</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/funhiphop/75795" target="_blank">📅 23:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75794">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مقامات آمریکایی: امروز یافردا توافقی با ایران امضا نمی‌کنیم و رئیس‌جمهور مایل است به آنها چند روز فرصت دهد تا آن را تکمیل کنند.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/funhiphop/75794" target="_blank">📅 22:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75793">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🟠
فروش ویژه OPEN VPN اختصاصى
🛜
سرعت بالا + پایداری عالی
🔰
امنیت تضمینی و اتصال بدون قطعی
🚀
مناسب گیم، استریم، دانلود و استفاده روزمره
📆
پنل كاربرى حرفه اى براى مشاهده حجم،زمان،تعداد كاربر
🌐
تعرفه سرویس‌ها:
🗣
اوپن حجم بالاى 100 -گيگى 55 هزار تومان -نامحدود…</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/funhiphop/75793" target="_blank">📅 22:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75792">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ys9mLqQ5W2fUNZQFSu8qMkLsJKl-BYRjYOwGSeqY0TMcyzX8fJY8ZQNNgv5Ntismc_GAVG7PEyz1TwRaW9LhpWKQ04zyDPKNwnG8HIT9QF5Iq3HTMSOqWS3_ZhlgP6GNLGm94ObAUqF4euPPBWobuB3FS5P25BTs_s0T5XwbIyQ7aHjTfGnLzkBUEO-kGnMfddmaH6ZQN-Kjqrr57-G62inPWK267PKP1MxWAnmBTryo679IGOUIZxdfZDBy6DeGkuEHFYGrlMwAj_5FtBxQ5ZCSjamEKYQ5RNHCAskImufuCsK2dEzybwEBfFPciuT2cMZal6MOrlKd6G_ZAifjBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
فروش ویژه OPEN VPN اختصاصى
🛜
سرعت بالا + پایداری عالی
🔰
امنیت تضمینی و اتصال بدون قطعی
🚀
مناسب گیم، استریم، دانلود و استفاده روزمره
📆
پنل كاربرى حرفه اى براى مشاهده حجم،زمان،تعداد كاربر
🌐
تعرفه سرویس‌ها:
🗣
اوپن حجم بالاى 100 -گيگى 55 هزار تومان -نامحدود ٣ ميليون تک کاربر
🗣
اوپن + L2TP اختصاصی پهنای باند 50mbps گیگی 200 هزار
🗣
اوپن + L2TP اختصاصی پهنای باند 85mbps گیگی 350 هزار
⭕️
سرويس هاى اختصاصى قابليت تقسيم سازى به چند يوزر براى همكارى
📉
تخفيفات ويژه سرويس ها روزانه در كانال
📣
📣
@awsvpn9
👩‍💻
🕛
@awsvp9</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/funhiphop/75792" target="_blank">📅 22:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75791">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2e3_eE_G2Yv2O30UV6ysWuy2EbAdU5Aiu_kF9T81W68xqGX4BiOiYNa0tR9_B7nDyqhllJZ8RNHr4r579LxhU2bi1KGLgLXG5qdBJWz0ozcrvs-2CHaGQYpEiHuoVlsD7sxJ6ktr8F06NPreoj-B-cEVyy4ipOoUW-tXMT2w0U7JQS01EO4UaquT8-zEc-tERgtpcfNdpr_z2DbglTyKhZH9Ch2AUtHPhIr8ppXaSxBIrEY8ppzzyrtg29kMSRlp1hdfKGIfJwwg-nhjYOwn9HvMICYABzQAnko0V4_2EqHSvquiwe_wIR9zwqyF3tCJVNRH_LvWoCkUEMC6HTFTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدرت هوش مصنوعی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/funhiphop/75791" target="_blank">📅 22:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75790">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مارکوس روبیو به نیویورک تایمز:
ما آن را به تعویق نمی‌اندازیم.
اما مذاکرات هسته‌ای مسائل بسیار فنی هستند.
واضح است که نمی‌توان یک موضوع هسته‌ای بزرگ را پشت یک دستمال کاغذی در ۷۲ ساعت حل کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/funhiphop/75790" target="_blank">📅 22:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75789">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ: اگر با ایران معامله‌ای انجام دهم، معامله‌ای خوب و شایسته خواهد بود، نه مثل معامله‌ای که اوباما انجام داد، که به ایران مقادیر زیادی پول نقد داد و راهی واضح و باز برای سلاح هسته‌ای فراهم کرد. معامله ما دقیقاً برعکس است، اما هیچ‌کس آن را ندیده یا نمی‌داند…</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/funhiphop/75789" target="_blank">📅 21:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75788">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmxxOd4eR2YQBvJgmOu2ozs-gPp0_zIrcHWJjy7v3bKPymsHhOD-LmhlQiF8BasT8Xm4mfCaluomgcmmaa3JcC6zNYn7W0ZS3J-9FVNNI_J-UM7fJVLR8IxpwdTmP8wMu-HArWI6jwaAgbMHc-ZuRF5ma_Ssf18W7GvOudQtyMlOMwCc6g5LC4xJKzNLO8pTGQCvc71T6gvQ09i7QBpJo8L5A2d-uMvGo7x6I2Cq5YLnXB493OQr1TC0Cf-xq5wznJHEEuBhsuKnbTyo2czRvhXjednTR847t_hRpdemzc8HbioczgcO5nhNJLYSWBV2U7L7uuRXaLXrrbvA6hAPTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
اگر با ایران معامله‌ای انجام دهم، معامله‌ای خوب و شایسته خواهد بود، نه مثل معامله‌ای که اوباما انجام داد، که به ایران مقادیر زیادی پول نقد داد و راهی واضح و باز برای سلاح هسته‌ای فراهم کرد.
معامله ما دقیقاً برعکس است، اما هیچ‌کس آن را ندیده یا نمی‌داند چیست.
(یعنی چی آخهخارک
حتی هنوز مذاکرات کامل به پایان نرسیده است.
پس به بازندگان گوش ندهید که چیزی را نقد می‌کنند که هیچ چیزی درباره‌اش نمی‌دانند.
برخلاف کسانی که قبل از من بودند و باید سال‌ها پیش این مشکل را حل می‌کردند، من معامله‌های بد انجام نمی‌دهم!
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/funhiphop/75788" target="_blank">📅 21:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75787">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">عملا هیچ چیزی تغییر نکرده از دیشب
ترامپ کصکش فقط خواست مارو حرص بده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/funhiphop/75787" target="_blank">📅 20:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75786">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اگه کانفیگاتون ضعیفه دست به گیرنده ها نزنید و پول اضافی خرج نکنید، اختلال سراسریه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/funhiphop/75786" target="_blank">📅 20:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75785">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">الجزیره: مشکلات جدی‌ای در مذاکرات وجود دارد. از جمله: موضوع لبنان: آمریکایی‌ها خواستار این هستند که نوشته شود اسرائیل می‌تواند «اگر تهدیدی وجود داشته باشد» عمل کند، ایرانی‌ها مخالفت می‌کنند. موضوع آزادسازی دارایی‌ها: ایران قبلاً در چارچوب توافق کلی دارایی‌ها…</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/funhiphop/75785" target="_blank">📅 20:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75784">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">الجزیره: مشکلات جدی‌ای در مذاکرات وجود دارد.
از جمله:
موضوع لبنان: آمریکایی‌ها خواستار این هستند که نوشته شود اسرائیل می‌تواند «اگر تهدیدی وجود داشته باشد» عمل کند، ایرانی‌ها مخالفت می‌کنند.
موضوع آزادسازی دارایی‌ها: ایران قبلاً در چارچوب توافق کلی دارایی‌ها را آزاد کرده است، آمریکایی‌ها روشن کردند که این فقط در توافق نهایی اتفاق خواهد افتاد.
ایران به پاکستان گفته است که توافقی وجود نخواهد داشت اگر آمریکا بر این نکات اصرار کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/funhiphop/75784" target="_blank">📅 20:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75783">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کم کم دارم یه رابطه عمیق بین خودم و تسنیم احساس می‌کنم:
علیرغم برخی گفتگوهای امروز، کارشکنی‌های آمریکا در برخی بندهای تفاهم از جمله موضوع آزادسازی اموال بلوکه شده ایران همچنان ادامه دارد و تا این لحظه این موضوعات حل نشده است.
بر این اساس، در حال حاضر همچنان امکان
لغو
شدن تفاهم
وجود دارد و ایران تاکید کرده است که از خطوط قرمز خود برای احقاق حقوق مردم کوتاه نخواهد آمد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/funhiphop/75783" target="_blank">📅 19:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75782">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رئیس ستاد مشترک ارتش اسرائیل:
با دقت تحولات را درنظر داریم و آماده بازگشت فوری به جنگ شدید برای تضعیف نظام تروریستی ایران هستیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/funhiphop/75782" target="_blank">📅 19:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75781">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یعنی کسی هست که واقعا خشخاش میکاشته و با پیامک قوه قضاییه پشیمون شده باشه؟  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/funhiphop/75781" target="_blank">📅 19:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75780">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یعنی کسی هست که واقعا خشخاش میکاشته و با پیامک قوه قضاییه پشیمون شده باشه؟
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/funhiphop/75780" target="_blank">📅 19:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75779">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رویترز: مجتبی خامنه ای دستور داده که اورانیوم غنی شده در ایران بماند  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/funhiphop/75779" target="_blank">📅 19:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75778">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvBMJRnPDhwxzXNhiwHGfjhU80jZ-uNHklOlXFFNqBnlOMyYrYZGm836w5iKzZs3wr-QyEHTUD_M8VMeEjjDf29NsF3DrMkBlSGAaLph3I5qOJvDnLfHeBZgqy18cECNFePn7DZZzetpIQp2dmBY9bjAVL3d2VORxSqTc0Mi6K9QM--2hx9DrJDxcCIdnH3yAJxW276HP6wa40qyiQvInRVqgoj7LTTGjDKk6DSrETrZ4p5blHR7z-6Enf4lPp3qmjB_wlPP-fN3rXu7RZK6rGBE8tSvjd2D2xyg1BFH2UUKozyOJcUxm5pRpw6CcPUkwm8vcLOtPsESSDbW1VF0uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وا
@FunHipHop
| blue</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/funhiphop/75778" target="_blank">📅 18:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75777">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فاکس نیوز به نقل از یک مقام ارشد دولتی:
اگر ایرانی‌ها در مسئله غنی‌سازی امتیازات قابل توجهی بدهند، ما نیز در زمینه رفع تحریم‌ها امتیازات قابل توجهی خواهیم داد.
در موضوع هسته‌ای، برنامه فعلی این است که با کل ذخیره مواد غنی‌شده برخورد شود.
اگر توافق نهایی‌ای داشته باشید که ایرانی‌ها در آن خواهان ادامه‌ی غنی‌سازی باشند، پس توافق نهایی‌ای ندارید.
درمورد تنگه هرمز، این مقام گزارش‌های خبرگزاری فارس را که حاکی از کنترل تعداد کشتی‌ها توسط ایران بود رد کرد و گفت «ما فکر نمی‌کنیم دریافت عوارض نتیجه قابل قبولی باشد» برای این مسیر آبی که حدود ۲۰٪ تجارت جهانی نفت از آن عبور می‌کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/funhiphop/75777" target="_blank">📅 18:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75776">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آکسیوس:
برخلاف گفته‌ی روبیو، یک مقام ارشد در دولت ترامپ گفته است که انتظار نمی‌رود توافق با ایران امروز امضا شود.
چندین جزئیات باقی مانده که باید نهایی شود، با رفت و برگشت‌هایی بر سر بخش‌هایی از توافق (برخی کلمات که برای ما مهم است و برخی کلمات که برای آنها مهم است).
مقام آمریکایی گفت که مقامات ایرانی با سرعت کافی حرکت نمی‌کنند و چند روز طول می‌کشد تا پیش‌نویس از تمام مراحل تصویب عبور کند.
رهبر معظم ایران، مجتبی خامنه‌ای، قالب کلی را تأیید کرده است، اما اینکه آیا این به توافق نهایی تبدیل خواهد شد یا خیر، سوالی بی جواب است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/funhiphop/75776" target="_blank">📅 18:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75775">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کان نیوز: نتانیاهو در گفت‌وگوی دیشب با ترامپ، نخست‌وزیر تأکید کرد که اسرائیل آزادی عمل خود را در مقابله با تهدیدها در همه جبهه‌ها حفظ خواهد کرد و این جدا از توافق ترامپ با ایران خواهد بود و ترامپ هم این را مجدداً تأیید کرد. ترامپ تاکید کرد که در مذاکرات بر…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/funhiphop/75775" target="_blank">📅 18:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75774">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MitiG3PtbJDUhWxVRWrUGZ5BiI3IYmZLV6xvaV9Smn8yX143z5QSL4tSoAGVXrnB59aDVHsX-29Jrki-sXVvw1LZhIrHCWiC_JjWZ9rtKEcnetWur-7uEOV2vhO_5keBuOJDhP28OV5So8AzkQlqRpzKL6N4QrAqsCnoBX5kCvrOuSxuzmd1UAabnU0yeTEYkRzo-ZctRyopb5JRIKusDosW7majfDa7YTeeTC4YdPIhjaOOm3Bedp_qk92IBBi2FkItoLIO-ANPrZGg7BLOomzVA_JC2bS9y-WqQo_yTSKxnEVbaeB8-nX10pklwyBPCPe2dd3uCoBUsevEzT4-8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ که اوباما رو برای اعتماد کردن به حرف خامنه‌ای برای نداشتن سلاح هسته‌ای مسخره می‌کرد، حرف پزشکیان که می‌گه ما سلاح هسته‌ای نمی‌خوایم رو پست کرده.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/funhiphop/75774" target="_blank">📅 18:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75773">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ یه طومار فحش به برجام نوشته و گفته نه ببین مال من فرق داره:
یکی از بدترین قراردادهایی که کشور ما تاکنون بسته است، توافق هسته‌ای ایران بود که باراک حسین اوباما و آماتورهای دولت اوباما آن را مطرح و امضا کردند. این یک مسیر مستقیم برای توسعه سلاح هسته‌ای توسط ایران بود. این موضوع درباره قراردادی که دولت ترامپ در حال حاضر با ایران مذاکره می‌کند صدق نمی‌کند - بلکه کاملاً برعکس است!
مذاکرات به صورت منظم و سازنده پیش می‌رود و من به نمایندگانم گفته‌ام که در امضای قرارداد عجله نکنند چون زمان به نفع ماست.
تحریم‌ها و محاصره تا زمانی که توافق حاصل و تصویب و امضا شود، به طور کامل و موثر باقی خواهد ماند.
هر دو طرف باید صبر کنند و از صحت توافق اطمینان حاصل کنند.
جایی برای اشتباه وجود ندارد!
رابطه ما با ایران حرفه‌ای‌تر و سازنده‌تر شده است.
با این حال، آنها باید بفهمند که نمی‌توانند سلاح یا بمب هسته‌ای توسعه دهند یا به دست آورند.
من می‌خواهم از تمام کشورهای خاورمیانه برای حمایت و همکاری‌شان تشکر کنم که با پیوستن به کشورهای توافقات تاریخی ابراهیم، (عادی سازی روابط با اسرائیل) این همکاری تقویت و مستحکم خواهد شد و
شاید جمهوری اسلامی ایران نیز بخواهد به آن بپیوندد!
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/funhiphop/75773" target="_blank">📅 17:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75772">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سرلشکر محسن رضایی:
پشت صبر راهبردی ایران خشم انقلابی ملت است.
در صورت هرگونه اقدام نظامی علیه تنگۀ هرمز و تلاش برای ورود به خلیج فارس، جمهوری اسلامی پاسخی سخت، دردناک و بی‌نظیر خواهد داد.
اگر دشمن به تنگۀ هرمز وارد شود و سعی کند با زور آن را باز کند، ما هم محاصرۀ دریایی را می‌شکنیم و ممکن است از NPT خارج شویم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/funhiphop/75772" target="_blank">📅 17:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75771">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8SLwDJzP2krztWrT05Q3eO9AJZMa6HhqYor97Ln2YWJHkVqVkuDFgpNbkvD5550zc9hoRQMIozHzbfWfxBSh1aoKwv3z2SddS_jMQU4CgMOzkbQxBMxfxe4_xGoSzGQRvbBRcCxovqGWepj9Ds1bwz4r3_Qe30xiOz9PoWUTWkfjmWZwu5gSOzOVpuPiK0OqI4C5jH9qbE24hJR-KWbGifotYBXmJsBnSitltbOWB9xfJJ-YSH7kvWI65NDXaxCrW0pKmSOM0QKWNUo7SSVN-iOSf7XtvjX-IqF11x5WFJYVZzu6F0k6Y5fK-KLpMlI6XU_IgeLRzKOsEcO4rbAXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ نتانیاهو رو هم روانی کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/funhiphop/75771" target="_blank">📅 17:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75770">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ به آ‌ب‌ث خبرها:
نمی‌توانم درباره توافق صحبت کنم؛ این کاملاً به من بستگی دارد، و اگر خبری باشد، فقط خبرهای خوب خواهد بود.
من معامله‌های بد را انجام نمی‌دهم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/funhiphop/75770" target="_blank">📅 17:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75769">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a2494136.mp4?token=a3FSxmVZue6cISE5KGthylrZHfvUtNmhsF6bYk5pcrDZEnXPUOormtiWhLsVJdu3QW-kCbwa_PTrdOmecraM4cRH1VLfcxlJ68uVhNrMRDJpQ2Qam8yVBEDuNCTPC57sb5zsvadUq93zQAfoBGPkZWt4Tl0ME9RKCUPp6q8Rkjacx5U3H-R_pB68spCAjyvBmnnyOvh5GqUab6oPuBjjLP7kJEfCWj1wOsebTVQPWgrGXF1LUEFICCtRoAWb9b-Z6BwI6QRp2m3II1y2ZmwrsbFccGMqvwHJqqhlFC4CpaugHoNdG9r3sHlHdAj-rJKQhPVmdqUrcAaPD74N-HJrbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a2494136.mp4?token=a3FSxmVZue6cISE5KGthylrZHfvUtNmhsF6bYk5pcrDZEnXPUOormtiWhLsVJdu3QW-kCbwa_PTrdOmecraM4cRH1VLfcxlJ68uVhNrMRDJpQ2Qam8yVBEDuNCTPC57sb5zsvadUq93zQAfoBGPkZWt4Tl0ME9RKCUPp6q8Rkjacx5U3H-R_pB68spCAjyvBmnnyOvh5GqUab6oPuBjjLP7kJEfCWj1wOsebTVQPWgrGXF1LUEFICCtRoAWb9b-Z6BwI6QRp2m3II1y2ZmwrsbFccGMqvwHJqqhlFC4CpaugHoNdG9r3sHlHdAj-rJKQhPVmdqUrcAaPD74N-HJrbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من در حال تماشای ۲۳۹مین لایی جرمی دوکو به صالح حردانی و سوپر دابل هتریک روملو لوکاکو مقابل بیرانوند :
@funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/funhiphop/75769" target="_blank">📅 17:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75758">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qN52ZF5n-6vfdnBuyACMbak73pzMjVjLIFYNGIYZhLOqAuRsVsKU36MYTWY3qQ5vDEm-QpPVZ2-BHDytkuZwLq84auOKRQN7AprHcoFn6eBElS4QnG1LNfckwMMfs8IqadvB23AF1IY32JSHA4RKRktf86S7XUUqrH84E8WDRO-lfGsf06mygkujJO8RnOknDqo4XoIGiWAggGoWp7L86_Brfq2pzI_VGoApinhNwEr5m1dbJY65k77_Kwl8x1rKYNbcVZoHv0xsiC1HQZ_mHoK-x_yNYmUD4Q9iTNkumy2EXviSAT6s7aJ4d1bzeizpMUev5qIZog7LlVnw1PKqTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ezgHMCEaoSeqkrM-801SvL-JXiVgf5Y8zOjfvMwTyGeK56jZek5KrnVWQrhaPAHfkUHUFVGLbCJ1Wp7HXNBTYKGtWz1nPovpSpopO3xFlX9QRZlh3J0Dr8aliSaQ1foA7teeitnoezjabC41ltCrSavunKNwLYouO1mc38PqeoHnItfNZpNpliJ-M02tSBJyIFHT-FxBlogEWy23uXYSpPTgjVImUZjPggSLnowxI1fS-6w5OYitjzYZtf56pyVd3TTsx6jzf9MHAhAeyGtRbhBbqW_atZeHFO-O0JAZGzKbdyAMnLN6Xd4Ky24ZUYhOWlHBZTE6elUrVaKvHCL_Ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همون همیشگی  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/funhiphop/75758" target="_blank">📅 16:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75757">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1XMMzKWSRQbT17kROfx6wg2kmdClv_XrS4douPiASXKFC5eA9vmNEfUInmiN01Qo7BYauhT31opHSlqSbZ7rU7FBXCqBC3hVUiSYsiMfHEB42R7ree8YlBc9pUmvvv_7jfDA5p-EMiWa4ajxhMmmcJIhQhyK9m-xJbW5I_S8201tdmQaNaJ1xo1cGgtme23d0gpYE42LGPNmw2gYR-Zxlc5orVIUhVSfrLyMEF5nFOCbt-pKhZzRT4TK4HGCDT365jTUWrLM1CBYLEMZzyECBkmv3C0NrxCWOb6TdowoSQ1p8iDCN2_oYXoSv9vge0JGfBNW_70hf7Ftamms1MoNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی بیا یه بار شبیه آدم بزرگا رفتار کن ببینم به جز دلقک بازی چی بلدیخارک
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/funhiphop/75757" target="_blank">📅 15:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75756">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بیشرف خیلی خوب گفت</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/funhiphop/75756" target="_blank">📅 15:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75755">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خب کسخول توام رسانه رپی داری درباره همه چی نظر میری</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/funhiphop/75755" target="_blank">📅 15:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75754">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">در آخر هم کیرم تو کشوری که چارتا خواننده و فوتبالیست و بازیگر بخوان توش راجب همچی نظر بدن و لیدر چیزی باشن.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/funhiphop/75754" target="_blank">📅 15:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75753">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">علی کریمی اشتباه زیاد کرده تو زندگیش، ولی گاییدن مادر شاهین نجفی یکی از اون اشتباهات نیست.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/funhiphop/75753" target="_blank">📅 15:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75752">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تسنیم:
عبارت «تمدید آتش‌بس» اصلا در تفاهم نامه نیست.
برخلاف گزارش یک رسانه آمریکایی که می‌گوید طبق تفاهم نامه «آتش بس میان ایران و آمریکا به مدت 60 روز تمدید می‌شود»، این عبارت در متن وجود ندارد و
تعبیری که به کار گرفته شده است، اعلام پایان جنگ در همه جبهه‌ها از جمله لبنان است.
بر اساس متنی که هنوز نهایی نشده، در بازه 30 روزه موضوع تنگه هرمز و محاصره دریایی پیش برده می‌شود و زمان 60 روزه‌ای برای مذاکرات در مسئله هسته‌ای در نظر گرفته شده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/funhiphop/75752" target="_blank">📅 14:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75751">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=WM_yRKY3nmfOYUCuf7F8OyPp2GHGVsJgUx-ZooVvScv8zr-YGA1whiGdyM_PhOwSEsKzIifL_9AswBDfTZ8JNEii7mfZBPOfsbkaHiqonhJO3xdFAZvKuMD31pVU3Pbia0Kk8j_iKJoG2t5QgsGqiFeAGWcWPYi5PcT2N4ACjukzvscj418rmZhy3mGRs1vEOoJbpJwWOwywZ1w1M-bGyQ1oBqwzm4tX1_Xr2HlpMwpTLyw_jc2CTX-Naz2XucQ0ZhhiCEmZvuzxo-UvGpAE2v3z0IYtc1bR6oHvO7krTMfpzqq-LlgWVlRiRIb3IyD1WrfwS5Gacgn-lq5PCkpdKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=WM_yRKY3nmfOYUCuf7F8OyPp2GHGVsJgUx-ZooVvScv8zr-YGA1whiGdyM_PhOwSEsKzIifL_9AswBDfTZ8JNEii7mfZBPOfsbkaHiqonhJO3xdFAZvKuMD31pVU3Pbia0Kk8j_iKJoG2t5QgsGqiFeAGWcWPYi5PcT2N4ACjukzvscj418rmZhy3mGRs1vEOoJbpJwWOwywZ1w1M-bGyQ1oBqwzm4tX1_Xr2HlpMwpTLyw_jc2CTX-Naz2XucQ0ZhhiCEmZvuzxo-UvGpAE2v3z0IYtc1bR6oHvO7krTMfpzqq-LlgWVlRiRIb3IyD1WrfwS5Gacgn-lq5PCkpdKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر:
به پیش قراول امت اسلامی، نیروهای مسلح و مقتدر نظام جمهوری اسلامی ایران موفق شدند، یک فروند پهپاد شناسایی فوق پیشرفته مداری اسرائیلی را، توسط آتش پرفروز و پدافند قدرتمند هوایی ایران و یک سامانه دفاعی فوق پیشرفته و نامشخص شناسایی و در منطقه بندرعباس، سرنگون کنند.
جزئیات تکمیلی متعاقبا اعلام خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/funhiphop/75751" target="_blank">📅 14:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75750">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فاکس نیوز:
توافق احتمالی مقرر می‌کند که نیروهای نظامی آمریکایی به مدت ۳۰ روز در نزدیکی ایران باقی خواهند ماند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/funhiphop/75750" target="_blank">📅 14:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75749">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فرمانده قرارگاه مرکزی خاتم‌الانبیا:
به مشت گره خورده پیکر رهبر شهیدمان قسم، نیروهای مسلح مقتدر کشورمان اجازه نخواهند داد تجربه‌های دردناک تاریخی در حین مذاکرات تکرار شود و به اذن الله اقتدار و سرافرازی جمهوری اسلامی ایران را بر دشمن تحمیل خواهند کرد و آماده پاسخگویی سخت و جهنمی به هرگونه تجاوز هستیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/funhiphop/75749" target="_blank">📅 13:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75748">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2rayYar</strong></div>
<div class="tg-text">🔐
سرور اختصاصی ترکیه با پینگ فوق‌العاده پایین
مناسب گیم، ترید، استریم و استفاده حرفه‌ای
✅
سرعت و کیفیت عالی
✅
آی‌پی ترکیه واقعی
✅
پایداری بالا و بدون قطعی
✅
مناسب استفاده 24/7
✅
بدون محدودیت زمان و بدون ضریب
💰
قیمت تک: هر گیگ 150 هزار تومان
🤝
قیمت همکاری: هر گیگ فقط 120 هزار تومان
با ضمانت عودت وجه در صورت قطعی
🙏
برای تست و ثبت سفارش پیام بدید
✉️
:
@V2rayyar_sup</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/funhiphop/75748" target="_blank">📅 13:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75747">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ci2DF9jgF4ZFptEuH_ak-U8ReMTmU1ouQUjclEIu_Ed8HgI1aqySKPJWP5IeR_V19ft6-iZ0UG_3WqGI6fVax5Q570FhTXa713_i3d_S2bVSICz05F84zYDQOV1aU_9B0Rh2SXzGNtPeX45-koxJZDa7KYj2trJZqQa-Xh7hK6HCPr33GYYvGv2ND_-Pxmi5sE-zOz-RcaFu43IhSZSxBsEaU1dHrIWu7wyaG7QD1VG-ejQ2Gufivl97IyrB1ZtbnadECiF7DpSf_7jUfob1nreUHDhG5mz1GZrzIea13rWpl2JSCHE5iwcJnJegJNdz4pKIRt15qcYGbtE4cky_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقیقا
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/funhiphop/75747" target="_blank">📅 13:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75746">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کان نیوز:
نتانیاهو در گفت‌وگوی دیشب با ترامپ، نخست‌وزیر تأکید کرد که اسرائیل آزادی عمل خود را در مقابله با تهدیدها در همه جبهه‌ها حفظ خواهد کرد و این جدا از توافق ترامپ با ایران خواهد بود و ترامپ هم این را مجدداً تأیید کرد.
ترامپ تاکید کرد که در مذاکرات بر خواسته مستمر خود برای خلع سلاح برنامه هسته‌ای ایران و خارج کردن تمام اورانیوم غنی‌شده از خاک این کشور پایبند خواهد بود و بدون پذیرش این شرایط، توافق نهایی را امضا نخواهد کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/funhiphop/75746" target="_blank">📅 13:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75745">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یک منبع خیلی آگاه ایرانی در گفت‌وگو با خبرگزاری رویترز:
در صورت موافقت و تصویب توافق میان تهران و واشینگتن در شورای عالی امنیت ملی ایران، متن سند جهت تصمیم‌گیری نهایی برای آیت الله مجتبی خامنه‌ای، رهبر جمهوری اسلامی ارسال خواهد شد تا به تایید ایشان هم برسد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/funhiphop/75745" target="_blank">📅 13:25 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
