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
<img src="https://cdn4.telesco.pe/file/h3kEKV1g-DBCh1LL5Pn8OoBGPJlLpPtovy2nA-0yvA2oDK4dJgJ2t2prDP3TpJFy8S3I2H8ePkxHQr45HAOJnWsfJMMMpWaeFcPsr0JNL4__twBkQnsfoEh02x7o84jGpB4RVuuyNmKUrPkGbJiOdA9gkbs5so5V2EQ5iLvdfkLQ_c48T_WnvyAsEk0_3QDjGIRkU68YjtWDlgn_BXsnfftkHvz7ZvlSDyJ7Xeu-w_FZVuht5CtmAqXAreA_LI4o0_nPCCGFxTT1OTFA7c3bgoDS3n3wTEH-6u12iMc599nHO9xgWlHaZ3ghwY8TiSXyEAYueJP5pCR62YabZg3wDg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 958K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 22:58:53</div>
<hr>

<div class="tg-post" id="msg-120023">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-RpGzAogTN9Vfrg2Aab6lc0eOK2EUFfoJnqQCupUOYlR450n5X36cdkpNM3NGEEbpoynxg_8d52Ji5ivCW0Uxl5NI5UsZptGlswbMJeZL_pGARi9rQIuTofKtuAI_akIxSCC8ga4JKWBSpTAdY9Ap4vRT8uNjCXEjMBZdqIniWyOA84q2cxReoOhVBrK7mPYVVPhiCSR120hJEhHUl4iEA6nAERvfraCglRGvl339OOYTB7vosLJOk6rxzwoOTo3pMiuuev22HutvLMJEFS3Bek6uqjQolZm_2FkFBkb4PFhW94f4_XkBp-cYsQqBaW1qhlDyXp6VRO0pjpwc89sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارفعان نبیان ، جوان ۲۶ ساله اهل اصفهان، در جریان اعتراضات ضدحکومتی بازداشت شد.
🔴
خانواده‌اش بیش از دو ماه است که هیچ خبری از او ندارند، اجازه ملاقات به آنها داده نشده و او از حق دسترسی به وکیل محروم بوده است.
🔴
رژیم او را به اتهاماتی مانند محاربه (دشمنی با خدا) محکوم کرده که مجازات آن اعدام است.
🔴
گزارش‌ها حاکی از آن است که حکم اعدام او صادر شده و خطر اجرای آن با طناب دار بسیار جدی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/alonews/120023" target="_blank">📅 22:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120022">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
به گزارش Ynet، آیزاک هرتزوگ، رئیس‌جمهور اسرائیل سفر هفته آینده خود به نیویورک را به دلیل «شرایط مانع از این سفر در این زمان» لغو کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/alonews/120022" target="_blank">📅 22:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120021">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
خضریان، عضو کمیسیون امنیت ملی مجلس: ترامپ در جنگ گیر کرده است و با بلوف زدن به دنبال این است که عقب‌های سیاسی را در ایران فعال کند تا مردم را به سوی تسلیم سوق دهند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/alonews/120021" target="_blank">📅 22:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120020">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
خضریان، عضو کمیسیون امنیت ملی مجلس: ترامپ در جنگ گیر کرده است و با بلوف زدن به دنبال این است که عقب‌های سیاسی را در ایران فعال کند تا مردم را به سوی تسلیم سوق دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/alonews/120020" target="_blank">📅 22:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120019">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
خروج مرغ زنده از خوزستان ممنوع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/alonews/120019" target="_blank">📅 22:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120018">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
عزیزی، رئیس کمیسیون امنیت ملی:
پیش بینی کردیم که هرکس که ترامپ رو به هلاکت برسونه، 50 میلیون یورو پاداش دریافت کنه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/alonews/120018" target="_blank">📅 22:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120017">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">⭕️
درک گفته های زنده یاد
فريدون فرخزاد
هنوز برای سه فاسد قابل فهم نيست!!!
🔴
حتما این ویدیو رو ببینید.
🤔
«مردی که ۵۰سال از زمان خودش جلوتر بود»
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/alonews/120017" target="_blank">📅 22:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120016">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
شبکه فاکس نیوز از استعفای فرمانده کل گشت مرزی آمریکا خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/alonews/120016" target="_blank">📅 22:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120015">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل اشاره دارد که تکذیب سفر نتانیاهو از سوی مسئولان اماراتی‌ ناشی از ترس است؛ زیرا ابوظبی می‌ترسد به عنوان یک طرف در محور ضد ایران، ظاهر شود.
🔴
امارات در تلاش است است که سطح حضور خود را در مورد روابط با اسرائیل نسبتا پایین نگه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/alonews/120015" target="_blank">📅 22:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120014">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ظهوریان، نماینده مجلس: بخش انرژی کشور ۱۴ میلیارد دلار خسارت دیده است
🔴
۸ میلیارد دلار بخش گاز آسیب دیده است
🔴
ظرفیت تولید گاز کاهش پیدا کرده
🔴
پخش پتروشیمی ۶ میلیارد دلار آسیب دیده است
🔴
بخش فولاد ۲.۷ میلیارد دلار آسیب دیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/alonews/120014" target="_blank">📅 22:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120013">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
نتانیاهو: اورشلیم را تحت حاکمیت اسرائیل برای همیشه حفظ خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/alonews/120013" target="_blank">📅 22:27 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120012">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ea891eb47.mp4?token=Ddh80i6UqmbzVeJj2O6t3g5fmm4oIyhEcprnbikp-j3D_OXsO_Qx6npr42txYsVEGT_1ABNEMU6fpOJVJq5clYU5lCY9zit_IrtRiKq9r2bk8oMsSZLJ5LrJXgMaf14JLCuY3H9VzhYa1NMpLqFUB5BsYYYhJzDCeJ2BboujcP6CtfDHdVWRNj6y3sCsDZWXV92sguTayvcjXFYO-igbjGO8k-ljQhdoutmNwvYbIz6INyI8n4IZLk15IGWa43bvn6O2WPBxnAiAGg89P3ML16U8LTm-u0pZipsjQM0V2BQFfhUuTwQ6sUP9I4-yoDjmJxxe34o0HmKjPtqgqUVXCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ea891eb47.mp4?token=Ddh80i6UqmbzVeJj2O6t3g5fmm4oIyhEcprnbikp-j3D_OXsO_Qx6npr42txYsVEGT_1ABNEMU6fpOJVJq5clYU5lCY9zit_IrtRiKq9r2bk8oMsSZLJ5LrJXgMaf14JLCuY3H9VzhYa1NMpLqFUB5BsYYYhJzDCeJ2BboujcP6CtfDHdVWRNj6y3sCsDZWXV92sguTayvcjXFYO-igbjGO8k-ljQhdoutmNwvYbIz6INyI8n4IZLk15IGWa43bvn6O2WPBxnAiAGg89P3ML16U8LTm-u0pZipsjQM0V2BQFfhUuTwQ6sUP9I4-yoDjmJxxe34o0HmKjPtqgqUVXCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: دشمنان ما به دنبال نابودی همه ما هستند. همه ما.
🔴
آنها بین راست و چپ، سکولار و مذهبی، یهودی و عرب تفاوتی قائل نمی‌شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/alonews/120012" target="_blank">📅 22:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120011">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تعرفه سرویس های Vip
⭕️
✅
1 گیگابایت
⬅️
235/000 تومان
✅
3 گیگابایت
⬅️
735/000 تومان
استارلینک Vip
💫
🌟
⭐️
5 گیگابایت
⬅️
1/150/000 تومان
⭐️
10 گیگابایت
⬅️
2/350/000 تومان
ویژگی های سرویس های Vip :
❤️‍🔥
✅
متصل در تمامی دستگاه و اپراتور ها
✅
مناسب استفاده روزمره در تمامی برنامه ها
✅
دارای ساب برای اطلاع لحظه ای باقیمانده
✅
تک لینک بدون نیاز به بروزرسانی های متعدد
✉️
پشتیبانی و خرید:
🔤
@safevpn_secureSupport
🤖
خرید فوری از ربات:
🔤
@SafeVPNXBot
📢
کانال اطلاع رسانی:
🔤
@safevpn_suportt
😍
کانال رضایت :
🔤
@safevpn_feedback
╚═════════════════════════╝</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/alonews/120011" target="_blank">📅 22:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120010">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
خبرگزاری ایسنا : با قیمت قطعی خودرو باید خداحافظی کنید،چون تو جدیدترین طرح فروش ایران‌خودرو و سایپا،خریداران باید نیمی از مبلغ خودرو رو امروز بپردازن بدون اینکه بدونن در زمان تحویل چه قیمتی در انتظارشونه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/alonews/120010" target="_blank">📅 22:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120009">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
اسرائیل معتقد است که رئیس‌جمهور ترامپ پس از بازگشت از سفر به چین تصمیم خواهد گرفت که آیا عملیات نظامی علیه ایران را از سر بگیرد یا خیر، طبق گزارش کان نیوز.
🔴
مقامات ارشد ارتش اسرائیل و فرماندهی مرکزی آمریکا (CENTCOM) در هفته گذشته درباره احتمال از سرگیری عملیات علیه ایران گفتگو کرده‌اند. بحث‌ها شامل امکان حملات هدفمند آمریکا به زیرساخت‌های سوخت و انرژی ایران بود که هدف آن فشار آوردن به تهران برای بازگشت به مذاکرات و مجبور کردن به امتیازدهی در برنامه هسته‌ای‌اش است.
🔴
اسرائیل به واشنگتن اعلام کرده است که از از سرگیری عملیات نظامی علیه ایران حمایت می‌کند و معتقد است عملیات «شیر غران» خیلی زود پایان یافته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/alonews/120009" target="_blank">📅 22:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120008">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7be8ab919.mp4?token=H7s1q3LM9H0BUw2PWERF8Uhe91ZSFUBb6ZrwTT5xncNg5a0Uax4l8lpgBw2itpBjGvazivSHXI5thZGSVi_ya0xeFeR-2npg27lpqAZUJRWc8tvYJHf6YDF6upSFWlHFGoshn0z-S2_if9Qv8FXfqOkS02dlPvVsXuSCXLSX-pvCyby4stMbyVC8gQQpMj5AwgSOeAFiHNB6aHCXDBVXamhxGbz2lqhLIjstcjIuNylyGB_wkCUYvj46fUar49UrBK04k9Op-z_vGS44m8n0rOLU01c-dfOubG7KXFlN-OKlC2OZ26HdDiBTjh2gaHSiMQu886KrcTHRGbKR1KM42Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7be8ab919.mp4?token=H7s1q3LM9H0BUw2PWERF8Uhe91ZSFUBb6ZrwTT5xncNg5a0Uax4l8lpgBw2itpBjGvazivSHXI5thZGSVi_ya0xeFeR-2npg27lpqAZUJRWc8tvYJHf6YDF6upSFWlHFGoshn0z-S2_if9Qv8FXfqOkS02dlPvVsXuSCXLSX-pvCyby4stMbyVC8gQQpMj5AwgSOeAFiHNB6aHCXDBVXamhxGbz2lqhLIjstcjIuNylyGB_wkCUYvj46fUar49UrBK04k9Op-z_vGS44m8n0rOLU01c-dfOubG7KXFlN-OKlC2OZ26HdDiBTjh2gaHSiMQu886KrcTHRGbKR1KM42Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست جدید کاخ سفید تو ایکس : بازگشت قدرت آمریکا به صحنه جهانی
🇺🇸
🇨🇳
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/alonews/120008" target="_blank">📅 22:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120007">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
عراقچی: دنیا فهمید دیگر نباید سر به سر مردم ایران بگذارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/alonews/120007" target="_blank">📅 21:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120006">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
رویترز: آرامش فریبنده بازار نفت دوام نخواهد داشت
🔴
تحلیل‌های بازار نشان می‌دهد که ثبات نسبی فعلی در قیمت‌های جهانی نفت تنها سکوتی پیش از طوفان است و ریسک‌های ژئوپلیتیک به‌زودی نوسانات شدیدی را رقم خواهند زد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/120006" target="_blank">📅 21:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120005">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران: ایران پنج شرط خود را برای مذاکره با واشنگتن اعلام کرد و میانجی پاکستانی آنها را [به آمریکا] رسانده است تا منتظر پاسخ آمریکا به این شروط باشد.
🔴
ممکن است برداشت اولیهٔ آمریکایی این باشد که اینها حداکثر سقف خواسته‌ها است.
🔴
تهران منتظر است که میانجی پاکستانی پاسخ کاخ سفید را بیاورد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/alonews/120005" target="_blank">📅 21:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120004">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
تصویری از روسای جمهوری امریکا و چین در ضیافت شام
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/alonews/120004" target="_blank">📅 21:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120003">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
بلومبرگ: ناامیدی و خشم مقامات سعودی و قطری از سرمایه گذاری در شرکت داماد ترامپ در پی وقوع جنگ و انتخاب گزینه اسرائیل توسط کوشنر
🔴
مشتریان عرب کوشنر همچنان احتمال همکاری‌های بیشتر با او را باز گذاشته‌اند، مشروط بر اینکه جنگ با توافق صلحی پایان یابد که برایشان قابل قبول باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/alonews/120003" target="_blank">📅 21:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120002">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajrqxuT0VV2VUGbAY6XQw6HvDrt47ONuIj-Fig3yi7QLuNse28T0QpxaB_87c0ZFTVrOGGxxDy1NuD38p_JPIeD4cbuiWQxNf7QPnbWRMgJ5RJ8DfhZ-a4tRRHdCkZ8W1JiR2uBI5ITJQp5VDTCN6VD62GEnVZOkY8aPqS45nhUxA1nx8cCnudqeRZFwvfxsI-g9ddTbiks2z_cEI5CKqYHC0oyQ2omig5TgWKIV7n2jE7zE_-7lFk5VqzvJaqKk3v7bKsKUftYlD3dupzCIeGr_ozJEuu88vYjSC5QKIf4xfJiq0_ESN3mE3Mv2GOibe2UUup1X4LIbHeOEre3CPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از روسای جمهوری امریکا و چین در ضیافت شام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/120002" target="_blank">📅 21:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120001">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سازمان بهداشت جهانی: نرخ مرگ و میر مرتبط با شیوع ویروس هانتا حدود ۲۷ درصد است و هیچ واکسن یا درمان خاصی برای ویروسی که می‌تواند باعث سندرم حاد تنفسی شدید شود، وجود ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/120001" target="_blank">📅 21:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120000">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
الی کوهن، تو کانال ۱۲ اسرائیل : ایرانی‌ها داشتن سعی می‌کردن مکالمه‌هامون رو شنود کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/alonews/120000" target="_blank">📅 21:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119999">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned «
»</div>
<div class="tg-footer"><a href="https://t.me/alonews/119999" target="_blank">📅 21:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119998">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/alonews/119998" target="_blank">📅 21:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119997">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVarzesh+plus | ورزش پلاس(K_B9)</strong></div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/alonews/119997" target="_blank">📅 21:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119996">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b70acc0f.mp4?token=TUA_ry5zpY3eli0ZJzmzI8F7bwoppJ3Dcwy0CYX55hNPtOJatJlidDVBALleLj707chgBSgo6qCgZUcppNR8hABIKdJHQ2r4nK9c1Jnc68qLDcbjjLPJa0z_eHglPbsf__6Ev0rJJei6PCvB2BlKpA6OZmImJMo-tZmoDweZwQSkgOumaWlUYoqOpc_n_l2BAnphxGBhbVMLd_0bM2RMaraDA4YUN4l5-dn8o42hsW3IfL5tXVRNd0gvMU2CUG1SyVBYP-gr0ApUKdvN8Kuc0P7Jx7umXCLKBSNk8UFlBKcElPYmaiE-rrZe7sqbPchL7_cAIOgoyxdYyygJ7q_fyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b70acc0f.mp4?token=TUA_ry5zpY3eli0ZJzmzI8F7bwoppJ3Dcwy0CYX55hNPtOJatJlidDVBALleLj707chgBSgo6qCgZUcppNR8hABIKdJHQ2r4nK9c1Jnc68qLDcbjjLPJa0z_eHglPbsf__6Ev0rJJei6PCvB2BlKpA6OZmImJMo-tZmoDweZwQSkgOumaWlUYoqOpc_n_l2BAnphxGBhbVMLd_0bM2RMaraDA4YUN4l5-dn8o42hsW3IfL5tXVRNd0gvMU2CUG1SyVBYP-gr0ApUKdvN8Kuc0P7Jx7umXCLKBSNk8UFlBKcElPYmaiE-rrZe7sqbPchL7_cAIOgoyxdYyygJ7q_fyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس کانال ۱۴ اسرائیل: رژیم ایران به شدت به پول نیاز داره و در حال انجام تماس‌های مخفی و مستقیم با دولت ترامپه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/alonews/119996" target="_blank">📅 21:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119995">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3TtHg7R614t8H3iK0Y57TzYCi4nn3tWeRWnuNfpt_AAuAdQ1Rb9Wb6hhvbdwlgieehrhm-iQCflrnPApgWBejDNnt-usmoXHLJ5k3WoL-QYwSm-JUzMAnPPk924yZ3_xk1dMm9qhmNmtNq_D-nnDwdIzU8Xcj1svqXszBikkoa7iU9d6w13TzhPAScynVS96RrG_6ecvTanRuY-uwxnqhfFprPuUJnqbUo-1pe8tXhrTaBqDh9iBwnE11qIF9bsudvzV1JH34ptAlOtfIPUUdkQR7pB1DGgdvAWgl-igoLYuKUWiXsfmEhQlU28J-jYoI9tKsixfndepMGZYNYHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: تشکیل دولت جدید به ریاست جناب آقای نخست وزیر علی الزیدی، و ابقای برادرم فواد حسین در جایگاه وزارت خارجه را تبریک می‌گویم
🔴
گسترش روابط برادرانه و دوستانه تهران-بغداد همواره در صدر اولویت‌های سیاست خارجی ما باقی خواهد ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/119995" target="_blank">📅 21:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119994">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8affe9b8.mp4?token=Q1LUsslc0kYWZsCLovtlOH92fJm20JDnfyvVsRLdQmr4Z3xogP1FW9wl1zztOGIgDQK5WWuvEgRt4ipR6OH6Wk3WpnX-UOBHVRtmBw3gwoVQtMq8vA8LsvCwz8JhFBk3MMH9DnnMSoJNyPemeXI-A_FsO9zzTtYf0TK55akUKYtcTcZD98zZNgMMNxSQMvMXqDmZf6pfAnX_OHnVAfW3SJ3hbom5Fgs4WfsVKXJzq-T3u7QWBuoQPqkqhqzD4V_IcrA3LTZkJQjfaWvDayCBOfeWtOPy4jR8ohYre23sJrLMLOiMxN7NVK_cGieQaSbNKhvJsUkFyGNWg0Yu9jTObg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8affe9b8.mp4?token=Q1LUsslc0kYWZsCLovtlOH92fJm20JDnfyvVsRLdQmr4Z3xogP1FW9wl1zztOGIgDQK5WWuvEgRt4ipR6OH6Wk3WpnX-UOBHVRtmBw3gwoVQtMq8vA8LsvCwz8JhFBk3MMH9DnnMSoJNyPemeXI-A_FsO9zzTtYf0TK55akUKYtcTcZD98zZNgMMNxSQMvMXqDmZf6pfAnX_OHnVAfW3SJ3hbom5Fgs4WfsVKXJzq-T3u7QWBuoQPqkqhqzD4V_IcrA3LTZkJQjfaWvDayCBOfeWtOPy4jR8ohYre23sJrLMLOiMxN7NVK_cGieQaSbNKhvJsUkFyGNWg0Yu9jTObg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش عراقچی به دست دراز کردن خانم وزیر خارجه ویتنام در اجلاس وزرای خارجه بریکس در هند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/119994" target="_blank">📅 21:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119993">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
اوکراین پهپادهایی را به مناطق کورسک و بریانسک روسیه به سمت مسکو پرتاب کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/119993" target="_blank">📅 21:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119992">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GR8pRUUfqyan9PlJAQU2ktICQ1EyzHfkE5lwmxaffo-3lZ3K4tbMofDhEBF9UjL0SYD8jQEbAIVLTfxQBIedxfbPUZKH0eo8osOvUa0PKfdQc5woO-H9U7Y-xe24zBtstngbSmWszD9KzJ5jkN5mmR1fJVWkXFpKpfP6rI13tw3tMkBq_bt7y83o6nw9ZZjX4sdf2XNs81co9DicEw1XFb3laWKT9IwIXaz4uah4_tEe9DuNQTKx1euNNXKHF-yMGFOsMhttptmoAg-OWzID0lWSfjN5Dz_plVE-Br6DBV981ShPT3fsSopKvyxTcR2oNWB0HrJvnCbymWpVz3o8SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار عراقچی و وزیر خارجه مصر در حاشیه  نشست وزرای امور خارجه بریکس در دهلی‌نو
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/alonews/119992" target="_blank">📅 20:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119988">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BGdP7gvau53Vd7BR2MsY_dxRLFh1TvrHNGanf7i9LIIXF9H5entH_sUvPRMSE19vnpixMD-T0w5_3CaUYk6EU8uriIbRR4YtRiNQ4ANPEcWfCBguj-rYIMhsF2ckcBxZXDmw0sJpJUx04TW6dSa2fhm9c9KQR5QtKnQbBvABsorzx78UxCdxqjcM2bOFUnusFU1aaXt9eNcwOF-nzEFTy8vvpdExr6wInUfhnAaGmvH9qB30_s7jZhtIXT5bIJfctaJRj_WChRq4tmWbVxMtClj2N6wFHGxHwlRxdxHbtf-cONIw7toPl6U4mimj0fUCyrAxyr5DovQbL0D0GkFZow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ux8gOdCK2RYzSr5PVEI5HnTrgZtgu7qn7JCK0UzK2-stEcF9MxW0H9uYRtoppF89lJzer_PKgilJWvaE2k3_4Ba1gBYH6LFCyPLKDm2HKShyw1apxtGrGkEqryobnVQwPU9spfHb4XoRptcY7kawsPoebaPi2aJi4aC3AbDWw4CmPXpGOXY_8GMp6S7lC0-4qEdi76xrER9WayxqqTqGnTlTBsPuWwQ5C56QfSTUfeg7aYjsisJBW3g7XPE2PqRXIcMLktYFx8rAzooSfzKJn6APQvxLdJGZ9ZId03UcWqSnORGEOCWTLMYG1hF_iPxWMTW7brD-HOW_XXg023CmHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ljnmr1Dg5AK7gEYYmretoGRzNu4LAKIeA0F43cdYg7yGSfLAS0b_f2RpFwWH9-Tj65fsl1FI6zdrt7MKTpxIBqjEGa-BEllBVF7CzMMZ-45An9fAcUQYRC8_CRrJzkZn1PFqZoAUKmXgeI89gxzOb3SMQWOT6NFIY_KAy5akpJwmAcauLJxG2W1YDctoMoQtKK3-QnbJ-vCL0rf0NwXrSXUeCwuVdcKyIOOfs4y5D624VBIP5GDhl5Z-mQk5Whpqdsk2WMnHmhjwZaYlVUF233JjYmpRY1rysQsycy-1KuqLZiXaBKQyycrckzrZBsQ1nLrzoFYBIenWj8A4fBBjPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L6WFEgknuStxE_4HmYwvJ6vkM2Xxqt8GYGQCF4v3VIuLaYuVSaf_e8zlzrNNTFUEfhRFeXpNE1_ubreYef_LdtMEy4ODQbKmoOWgGAiuHb7ToljO8jDbXUMggr5FVkjGmVrktAxQTkpRrPzwNqWxwZvo742OEgN3gCA9y_sM2CbBKXPVsJ-lnpwchMHd3vTIuUZCAe0Ct5vCw2-Jhsg95RU3pOi1NOYOLdEnvtswl0bXaP6OPWK4dTqrRG1ChvhsBd_J9H9jNe0fRLZSCFhOpyVSN2C5H2c3knmcPKh9FOnqhiD4B3tjbzBn_LpOQ-hyLmAXBiKvVL1wsKyR5Ah1Cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ارتش اسرائیل شروع به توزیع توری‌های ضد پهپاد به نیروها در لبنان کرده است، به طوری که تقریباً ۱۵۸٬۰۰۰ متر مربع تاکنون توزیع شده و ۱۸۸٬۰۰۰ متر مربع دیگر در حال خرید است، طبق گزارش کانال ۱۵
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/119988" target="_blank">📅 20:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119987">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
کانال 12 عبری: اسرائیل سطح هشدار خود را به بالاترین حد ممکن افزایش می‌دهد تا برای احتمال جنگی تازه با ایران پس از بازگشت ترامپ از چین آماده شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/119987" target="_blank">📅 20:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119986">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
واشنگتن پست: چین از جنگ آمریکا علیه ایران برای تقویت روابط با کشورهایی مانند تایلند، استرالیا و فیلیپین، با ارائه سوخت و فناوری سبز، استفاده می‌کند، آن هم در زمانی که به نظر می‌رسد دولت ترامپ علاقه کمتری به رهبری تلاش‌های بین‌المللی برای مقابله با بحران جهانی انرژی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/119986" target="_blank">📅 20:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119985">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
روبیو، وزیر امور خارجه آمریکا : ترامپ از رئیس جمهور چین کمکی نخواست، آمریکا به کمک چین نیازی نداره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/119985" target="_blank">📅 20:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119984">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb1a1c79f8.mp4?token=SMm-VTCSNA1bSqmlDc6_ILBHW0GOxrSevnuCnjot5G7N1WET9wYJecV-Z8tcirI8rj-LWWXWco3rZSRgEEWcWVNxzWRrN11F3NnI3x2u78SSvohuJQjdN4y8Ute2ZnE0orTcrj5fkQRQsJGpDLhkCeyLPUiOOqoMhOBSIRv_fQ2eEp9uSet5BZ_AY_6VL-Ea64AsyqnxX29S7xd-VUZ7GCuv6Lkk_l0AaqFOxFvpLyClpy15kg8BrRxkD_oUWKgw-wc-5bbiRMhOXW6l9KYeOIiayv36xXaIgK5_ZJFdrwsXp-BjmSxQf3akfOqpjm_MFvB5VBtAkjSTgWDMRCNhsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb1a1c79f8.mp4?token=SMm-VTCSNA1bSqmlDc6_ILBHW0GOxrSevnuCnjot5G7N1WET9wYJecV-Z8tcirI8rj-LWWXWco3rZSRgEEWcWVNxzWRrN11F3NnI3x2u78SSvohuJQjdN4y8Ute2ZnE0orTcrj5fkQRQsJGpDLhkCeyLPUiOOqoMhOBSIRv_fQ2eEp9uSet5BZ_AY_6VL-Ea64AsyqnxX29S7xd-VUZ7GCuv6Lkk_l0AaqFOxFvpLyClpy15kg8BrRxkD_oUWKgw-wc-5bbiRMhOXW6l9KYeOIiayv36xXaIgK5_ZJFdrwsXp-BjmSxQf3akfOqpjm_MFvB5VBtAkjSTgWDMRCNhsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله دو سرباز اسرائیلی رو که داشتن فرار میکردن هدف گرفت و با پهپاد کُشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/119984" target="_blank">📅 20:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119983">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
گزارش واشنگتن پست از یک ارزیابی اطلاعاتی محرمانه ایالات متحده: چین در نتیجه جنگ جاری آمریکا با ایران، در زمینه های نظامی، اقتصادی، دیپلماتیک و رسانه ای، دستاوردهای استراتژیک گسترده‌ای را به هزینه ایالات متحده به دست می آورد ، در حالی که نگرانی فزاینده‌ای در وزارت دفاع ایالات متحده در مورد پیامدهای ژئوپلیتیکی این درگیری وجود دارد
🔴
پکن از جنگ با ایران برای تقویت جایگاه بین‌المللی خود استفاده کرد، در حالی که واشنگتن بخش قابل توجهی از قابلیت‌های نظامی و اقتصادی خود را از بین برد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/119983" target="_blank">📅 20:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119982">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
رسایی؛ نماینده‌ی مجلس:
دولت قصد داره میزان سهمیه ماهانه بنزین ۱۵۰۰ تومنی و ۳۰۰۰ تومنی رو کاهش بده و قیمت بنزین ۵۰۰۰ تومنی رو هم به ۲۰۰۰۰ تومن برسونه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/119982" target="_blank">📅 20:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119981">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o33P6VihoKkKs2O8gXOiqNgw_mh3soIDoMYQ7GlrFkpJ3P-ZA0Zbzz6G-yaj4O2OgQ30GqaFOC00tKpu1FIafdwsep6ScOcXUz6Lm6vM2CWNfu1JqXl2NYVsHC5Cl8xZEwEjdh6qt_tNNpVWypcnWnvEhYEWRgYt4QrvQRW11lTDwbp7Pe58QKy2ybwUvIiwAKcMSQtVSRAZVU6mND7J5O1bPbYnxwiTNoAASv--EjsdKb91iMxtHfHxxGNnm6xPMS-UpwOfpx3ycU22g8LFNTCWpP6XxqoHgd45wqKQKc0YzfH4vtjPzoLGbO6Tnu4VkPpBp4mjfcn24gZvQ2WbKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
اشتراک v2ray استارلینک
🗯
گیگی
150,000
تومان
🔗
لینک ساب برا چک کردن مصرف و حجمتون
🔥
سرعت و کیفیت بالا
✅
پشتیبانی دائم
📱
جهت خرید پیام بدین :
@v2safeBot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/119981" target="_blank">📅 20:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119980">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه پاکستان: اسلام‌آباد از نقش چین در میانجی‌گری برای حل‌وفصل تنش‌ها میان ایران و آمریکا حمایت می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/alonews/119980" target="_blank">📅 20:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119979">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
واردات نفت خام آمریکا از ونزوئلا در هفته گذشته به بالاترین حد خود در هفت سال گذشته رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/119979" target="_blank">📅 20:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119978">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزیر دفاع بریتانیا : بعد از این‌که روسیه حملات سنگینی به اوکراین کرده
🔴
قراره ارسال سامانه‌های پدافند هوایی به کی‌یف رو سریع‌تر انجام بدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/119978" target="_blank">📅 20:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119977">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ایالات متحده موفق شد اورانیوم بسیار غنی شده را از رآکتور هسته ای برای اهداف تحقیقاتی در ونزوئلا خارج کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/119977" target="_blank">📅 20:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119976">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
شبکه MS NOW: شرکت‌های خصوصی چینی در حال بررسی فروش موشک‌های ضدهوایی به ایران هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/119976" target="_blank">📅 19:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119975">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
رونگ هوان»، فعال رسانه‌ای و تحلیلگر سیاسی چینی، تأکید کرد که پکن مناسب‌ترین و توانمندترین طرف برای ایفای نقش میانجیگری فعال بین واشنگتن و تهران است
🔴
او اشاره کرد که بهبود روابط چین و آمریکا در ماه‌های اخیر، افق‌های جدیدی را برای ترغیب دو طرف به بازگشت به میز مذاکرات مستقیم گشوده است.
🔴
این تحلیلگر سیاسی توضیح داد که منطقه در وضعیت تنش‌آفرینی متقابلی به سر می‌برد که نیازمند ابتکاری از سوی چین است تا نردبان کاهش تنش را فراهم آورد که آبروی هر دو طرف حفظ شود و به وضعیت بی‌ثباتی که به ضرر منافع همگان است، پایان دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/119975" target="_blank">📅 19:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119974">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
برد کوپر: ما درگیر اقدامات خصمانه علیه ایران نیستیم، بلکه آتش بس داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/119974" target="_blank">📅 19:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119973">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
وزیر جنگ پیت هگستث: با وجود آنچه ممکن است در رسانه‌ها بشنوید، آمریکا در حال افول نیست. ما همچنان قوی‌ترین قدرت نظامی روی زمین هستیم، اما این قدرت نیاز به تجدید دارد.
🔴
با تهدیدات جهانی که به طور مداوم در حال تحول هستند، زمان آن رسیده است که سرمایه‌گذاری ۱.۵ تریلیون دلاری، یک پیش‌پرداخت نسلی، انجام شود.
🔴
این سرمایه‌گذاری تضمین می‌کند که ایالات متحده برای نسل‌های آینده قدرت غالب و بازدارندگی بی‌نظیر در برابر هر دشمنی را حفظ کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/119973" target="_blank">📅 19:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119972">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ایلان ماسک درباره مذاکرات آمریکا و چین : من حس خوبی نسبت به این مذاکرات دارم. فکر می‌کنم نتیجه خوبی حاصل شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/119972" target="_blank">📅 19:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119971">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ترامپ : چین موافقت کرده ۲۰۰ هواپیمای بوئینگ خریداری کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/119971" target="_blank">📅 19:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119970">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCmDdBgL7eVn4GlcV3cnxW5kwM44n0tpSjNSautCfPJ64M9dbVMaXCx_D5O2JSrkXUNTW44WvijqfIeidkO6AHpE5tqoj1RNlVZNrVVmkQCixZN3TL1XpxtkrXDEMwT_v1XWeEHNKPBKWK1xxp-61mglAQhDGoZjqxHuRncEtNzIFEUql1ZB_s5_B-H9uVtqWAYA84Rs8Pq6LSk8rkEBovBazA3Kt-pnMmjfLNjzhoZgxLOPrUR3EfocquMuW5qScfGU5EWezW3sR-_64k4E2VbLMdW1R_aFmw0SVYBp_TuDdws66of6oahuyDojB5PEKXWKn6gsvWSnBhUvBx8Fxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برونو رودریگز وزیر امور خارجه کوبا در شبکه ایکس اعلام کرد که آماده است پیشنهاد کمک ۱۰۰ میلیون دلاری ایالات متحده را بررسی کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/119970" target="_blank">📅 19:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119969">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
دولت کوبا اعلام کرده است که جزیره رسماً بدون سوخت است و انتظار دارد سیستم انرژی در روزهای آینده فروپاشی کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/119969" target="_blank">📅 19:27 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119968">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
مجلس نمایندگان عراق با اکثریت مطلق آرا، فؤاد حسین را به عنوان وزیر خارجه در دولت جدید تأیید کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/119968" target="_blank">📅 19:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119967">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d6ffb480d.mp4?token=tvIyRJ2sRRvI1luhEQRpeMlhRoEt01wEdmsBa1gH4PNQgsxt6hE0OTVxFPT8c4oR5qP1X0e5V2hSNHoprIFi_9Ulpmc7uGBpYQb8bQyuHbn49LYoPUqvSjjcqTYXIetgK0G3uHypL-zpo8BWRjdUHelG-MX57DDpavCw9ADRdHOpnZ9eltz-FH1b40OT63hh2D8V-m_DPmFkUKsW0TUzFd_fUVN1EtLrFXxWXINfIGzDRlLUyeSo-Gs-BPL7zPT8QPONMfF7l8jclUip-ZZcvKt836iWTN4Nvs0kLJWFiWtLonXmd-Aj0GkIKnh8t6_MqSGV2O2uSixVmLalIlAM9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d6ffb480d.mp4?token=tvIyRJ2sRRvI1luhEQRpeMlhRoEt01wEdmsBa1gH4PNQgsxt6hE0OTVxFPT8c4oR5qP1X0e5V2hSNHoprIFi_9Ulpmc7uGBpYQb8bQyuHbn49LYoPUqvSjjcqTYXIetgK0G3uHypL-zpo8BWRjdUHelG-MX57DDpavCw9ADRdHOpnZ9eltz-FH1b40OT63hh2D8V-m_DPmFkUKsW0TUzFd_fUVN1EtLrFXxWXINfIGzDRlLUyeSo-Gs-BPL7zPT8QPONMfF7l8jclUip-ZZcvKt836iWTN4Nvs0kLJWFiWtLonXmd-Aj0GkIKnh8t6_MqSGV2O2uSixVmLalIlAM9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ان‌بی‌سی: آیا رئیس‌جمهور شی از رئیس‌جمهور ترامپ خواسته است که به تایوان سلاح نفروشد؟
🔴
مارکو روبیو: خب، این موضوع قبلاً مورد بحث قرار گرفته است. این موضوع در بحث امروز به طور عمده مطرح نشد. ما قبلاً موضع آن‌ها را در این باره می‌دانیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/119967" target="_blank">📅 19:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119966">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
عراقچی: امارات در حملات به ایران شریک فعال بوده است
🔴
ایران در برابر تهدیدها محکم ایستاده و سر خم نمی‌کند. آن‌ها این مسئله را دیده و تجربه کرده‌اند
🔴
در عین حال، کسانی که با زبان احترام با ایران سخن بگویند، با همان زبان پاسخ خواهند گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/119966" target="_blank">📅 19:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119965">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سنتکام: امارات، بحرین، عربستان، کویت، اردن و اسرائیل در عملیات آمریکا شرکت کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/119965" target="_blank">📅 19:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119964">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ترامپ : هر کشوری که این مقدار نفت بخرد، بدیهی است که نوعی رابطه دارد، اما او دوست دارد تنگه هرمز باز بماند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/119964" target="_blank">📅 19:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119963">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سناتور کنگره خطاب به برد کوپر:
شما میدونستید ایران تنگه هرمز رو میبنده؟
🔴
برد کوپر: همه احتمالات در نظر گرفته شده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/119963" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119962">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
میدل ایست نیوز : پارلمان عراق به برنامه دولت علی الزیدی رای داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/119962" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119961">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ترامپ : رئیس‌جمهور شی علاقه‌منده که درباره ایران به توافق برسه، اون گفت : اگه بتونم کمکی بکنم، حاضرم کمک کنم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/119961" target="_blank">📅 18:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119960">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
هانیتی از فاکس: آیا درباره حمایت چین از ایران با شی صحبت کردید؟
🔴
ترامپ: او گفت که تجهیزات نظامی نخواهد داد. این یک بیانیه بزرگ است.
🔴
اما در عین حال، گفت که آنها مقدار زیادی نفت از آنجا می‌خرند و دوست دارند این کار را ادامه دهند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/119960" target="_blank">📅 18:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119959">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
مارکو روبیو: نیروهای مسلح اوکراین در حال حاضر قوی ترین و قدرتمندترین نیروهای مسلح در تمام اروپا هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/119959" target="_blank">📅 18:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119958">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a2ffaa67.mp4?token=RalWm9-86kP83Q8qUdzulyDbvvYHeDnoIeVdHEWFttYlLR76NBrAYn-Cq_pkw1X9ITINxRehtrG3FdbqBmdF-xporS6JCUx2ooz6AAZ8yinufLT_qXSMLemhFM_l3cmmo7BV-BmyZQhlAL64uPJHKWI23vz1AgntIPDBkNCOn_J5tCz2X3HhlDpjUHYSFcLlJ9x1qJI-qsdtuE03NjsE2UeNDwR-BK5rpujymWFLHNMcYT8UA1I545zMuHCU-0PsuxXFxyTttok1RECJr_kcn6cGcVmY7zNA9-_JgIYFHWwBLRLLfDk-PHZC1H7IE0UsCvYqSlM01WJpIkE6fCl1_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a2ffaa67.mp4?token=RalWm9-86kP83Q8qUdzulyDbvvYHeDnoIeVdHEWFttYlLR76NBrAYn-Cq_pkw1X9ITINxRehtrG3FdbqBmdF-xporS6JCUx2ooz6AAZ8yinufLT_qXSMLemhFM_l3cmmo7BV-BmyZQhlAL64uPJHKWI23vz1AgntIPDBkNCOn_J5tCz2X3HhlDpjUHYSFcLlJ9x1qJI-qsdtuE03NjsE2UeNDwR-BK5rpujymWFLHNMcYT8UA1I545zMuHCU-0PsuxXFxyTttok1RECJr_kcn6cGcVmY7zNA9-_JgIYFHWwBLRLLfDk-PHZC1H7IE0UsCvYqSlM01WJpIkE6fCl1_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هانیتی از فاکس: آیا درباره حمایت چین از ایران با شی صحبت کردید؟
🔴
ترامپ: او گفت که تجهیزات نظامی نخواهد داد. این یک بیانیه بزرگ است.
🔴
اما در عین حال، گفت که آنها مقدار زیادی نفت از آنجا می‌خرند و دوست دارند این کار را ادامه دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/119958" target="_blank">📅 18:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119957">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
برد کوپر: فرماندهی مرکزی ایالات متحده در پاسخ مستقیم به تهدیدات جمهوری اسلامی ایران ایجاد شد.
🔴
طی ۴۷ سال، رژیم ایران منطقه را به وحشت انداخته و خصومت با آمریکا را به یکی از اصول اصلی حکومت خود تبدیل کرده است.
🔴
سوابق خصمانه و مرگبار آنها علیه آمریکا به خوبی مستند شده است.
🔴
در کمتر از ۴۰ روز، نیروهای سنتکام به اهداف نظامی خود دست یافتند. با نابودی ۹۰٪ از پایه صنعتی دفاعی ایران، این کشور برای سال‌ها قادر به بازسازی آن سلاح‌ها نخواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/119957" target="_blank">📅 18:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119956">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
برد کوپر: توانایی ایران به‌طور قابل توجهی ضعیف‌تر شده؛ اگه بخوام از تجربه خودم بگم، تو حدود صدبار عبور از تنگه هرمز معمولاً باید ۲۰ تا ۴۰ قایق تندرو می‌دیدی ولی این روزها فقط ۲ یا ۳ تا می‌بینیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/119956" target="_blank">📅 18:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119955">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
برد کوپر فرمانده سنتکام: توانمندی‌های موشکی، دریایی، پهپادی و صنعتی ایران ۹۰ درصد تضعیف شده است. او افزود که نیروی دریایی ایران تا یک نسل دیگر نیز به سطحی که پیش از جنگ در اختیار داشت باز نخواهد گشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/119955" target="_blank">📅 18:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119954">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0lqNCryX_rNnEaBgAg4cjOWDXKmcKTi-hKmhSldgUDH23I_wfD36TrpZNiRqhJQVXe3xfm0EEPhbLimjrX3-SIF0R4Gn7465arESpP5Cc8x8pH_YpxDanErpMm-LMzX87EolzowhZiwaKj7Zmvo39js_T8YiFAQDrqJrZjNh1Wsj96b8nMXCxAr1u-wnPJ50y6HC2LOxhc7gSHZeLPz8DEYVc1sl3pSHl52p1oUtcY1Nr088xfT08Vj3p-EzHshTAN1HhBp8RwRe5keMVvxW1ILPD9WJlQMPel-kEjBy7gxodjm8fQ5LV1wNAmTlk2NKHYDrYR11DkOKwrzXBQiKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: از فداکاری و ایثار مردم سپاسگزارم، با همدیگه ایران رو میسازیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/119954" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119953">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
فرمانده سنتکام، دریاسالار برد کوپر: امروز، حماس، حزب‌الله و حوثی‌ها همه از تأمین سلاح و حمایت‌های ایران قطع شده‌اند.
🔴
این نتیجه از پیش تعیین‌شده نبود و نه به شانس به دست آمده است. این حاصل ماه‌ها برنامه‌ریزی دقیق و بر پایه دهه‌ها تجربه است. این نتایج همچنین…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/119953" target="_blank">📅 18:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119952">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
منابع خبری می‌گویند کشتی باری هندی که روز گذشته به مقصد شارجه در حرکت بوده در تنگه هرمز هدف قرار گرفته و غرق شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/119952" target="_blank">📅 18:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119951">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
فرمانده سنتکام، دریاسالار برد کوپر: امروز، حماس، حزب‌الله و حوثی‌ها همه از تأمین سلاح و حمایت‌های ایران قطع شده‌اند.
🔴
این نتیجه از پیش تعیین‌شده نبود و نه به شانس به دست آمده است. این حاصل ماه‌ها برنامه‌ریزی دقیق و بر پایه دهه‌ها تجربه است. این نتایج همچنین بدون هزینه به دست نیامده‌اند.
🔴
برد کوپر درباره ایران: مذاکرات حساس ادامه دارد.
🔴
کار ما آماده بودن است و ما آماده‌ایم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/119951" target="_blank">📅 17:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119950">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
فایننشال تایمز خبر داد: عربستان سعودی پیشنهاد یک پیمان عدم تعرض میان کشورهای خاورمیانه و ایران را مطرح کرده است.
🔴
به گفته دیپلمات‌ها، این ایده بخشی از گفت‌وگوهای ریاض با متحدانش درباره نحوه مدیریت تنش‌های منطقه‌ای پس از پایان جنگ آمریکا و اسرائیل با ایران است.
🔴
دو دیپلمات غربی گفتند که ریاض برای این طرح، «فرآیند هلسینکی» در دهه ۱۹۷۰ را به‌عنوان الگویی بالقوه در نظر دارد؛ فرآیندی که در دوران جنگ سرد به کاهش تنش‌ها در اروپا کمک کرد.
🔴
آنها افزودند که پیمان عدم تعرض یکی از چندین ایده‌ای است که در حال بررسی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/119950" target="_blank">📅 17:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119949">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: طی سه روز گذشته هیچ بارگیری در تاسیسات نفتی ایران انجام نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/119949" target="_blank">📅 17:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119948">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
سی‌ان‌ان: ایران از چین خواسته تا برای پایان بن‌بست میانجیگری کند، در حالی که آمریکا از پکن می‌خواهد ایران را برای پذیرش شرایط خود تحت فشار قرار دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/119948" target="_blank">📅 17:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119947">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
رادیوی ارتش اسرائیل: دور جدید مذاکرات میان لبنان و اسرائیل در واشنگتن آغاز شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/119947" target="_blank">📅 17:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119946">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca2a56d1d6.mp4?token=QwxBSTe4XOYexQbt47oHjNXttUlI5U560BzVtnTyTVNaI8_7ZQtR3mhahMQAHaG7fDMvS7u1_shNVwB6gZ4rhdTPs3A2PH_itXTPjfU5911UDkleoDN9M_7UasmHsTGCxBdDQU9gOY3VXDM8PWeL_V7WirwBHwA5gqcFPzvN8dG_4l1I9gvqebqjYLD4K1MTDDauyKmWyWBaHxU9OdYdrz9-slXxiJaLBR0xQeZ8GOEOVptYf7MVAXEe3-aJcaISCitR5uGPAw58DQCX1EFOprSRWaa2hNR4EAUHS0su2o-VbPDcy4l0z0c5MX_g4OUzx92VFZ8_x7p3rIo0b0gqVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca2a56d1d6.mp4?token=QwxBSTe4XOYexQbt47oHjNXttUlI5U560BzVtnTyTVNaI8_7ZQtR3mhahMQAHaG7fDMvS7u1_shNVwB6gZ4rhdTPs3A2PH_itXTPjfU5911UDkleoDN9M_7UasmHsTGCxBdDQU9gOY3VXDM8PWeL_V7WirwBHwA5gqcFPzvN8dG_4l1I9gvqebqjYLD4K1MTDDauyKmWyWBaHxU9OdYdrz9-slXxiJaLBR0xQeZ8GOEOVptYf7MVAXEe3-aJcaISCitR5uGPAw58DQCX1EFOprSRWaa2hNR4EAUHS0su2o-VbPDcy4l0z0c5MX_g4OUzx92VFZ8_x7p3rIo0b0gqVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عارف: به هیچ قیمتی تنگۀ هرمز را از دست نخواهیم داد
🔴
اصلا تنگۀ هرمز مال ماست؛ ملک ما بوده حالا مدتی از ملکمان خوب استفاده نمی‌کردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/119946" target="_blank">📅 17:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119945">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78047a712d.mp4?token=kL_nGvQ4B4A5YgzOEnvZ01Q7IRUzA2csgT_dMhln1T2hmj8-8SSTse_5f9hkIlKHFrCT1VQqn0b0zUqcZ5ueRzZyyhA3Pj4cC882SF72zCsaw_Cir_r3uvOjaGkAUQoCTisgs--2-4kykUc2YlzrTN9UHUrNu2naOQX-1-Xn94dndyq4J13XcLn9viepaG3Sb4MsCCfkGfA7BHYH-_xfHio2X7k0m1YbyXI34iwgLvVhiJAeP6nk5z-4UvdnQldRXKJZ7tMMSxTrdVeJVjnbq7tNFzjoEeneWG_gKtAVDKJ24rEbHt0um1lMyBIAhuzec5QiENUtC4FIRiSwTMGFOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78047a712d.mp4?token=kL_nGvQ4B4A5YgzOEnvZ01Q7IRUzA2csgT_dMhln1T2hmj8-8SSTse_5f9hkIlKHFrCT1VQqn0b0zUqcZ5ueRzZyyhA3Pj4cC882SF72zCsaw_Cir_r3uvOjaGkAUQoCTisgs--2-4kykUc2YlzrTN9UHUrNu2naOQX-1-Xn94dndyq4J13XcLn9viepaG3Sb4MsCCfkGfA7BHYH-_xfHio2X7k0m1YbyXI34iwgLvVhiJAeP6nk5z-4UvdnQldRXKJZ7tMMSxTrdVeJVjnbq7tNFzjoEeneWG_gKtAVDKJ24rEbHt0um1lMyBIAhuzec5QiENUtC4FIRiSwTMGFOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترور هدفمند در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/119945" target="_blank">📅 17:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119944">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773d4b4c68.mp4?token=k5kv_JUTW8ypwCz_lxWd0SqP6lyVBv8K_42G8RIPCqsOD1DhVLykqeWyLqBWccveq_9a14F69CNd_ObEZYDEwQKEyBofswRI_1vvGzEpziuMLtEJiwVXYu5cEoVkr90-UC6g4dhz2JM71c3cs63pNHngzk5pLl24bwlhTBOEzcdLa3LnjZ2wWOyBS2cHIFWBRuBmgBp9hxS4D8eTJ7VdJ4bgg8WltVzX7FZ56XDeYnGLPUVC7LPXoVXx9dKBOV8oz4AeUL9JW2Kuep_kz3FEa_KHXUoQBwWV1DH6kad_nQubsghiIdDdf5bQdMS16h9x6fpWoREpkUJpoywapZeSIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773d4b4c68.mp4?token=k5kv_JUTW8ypwCz_lxWd0SqP6lyVBv8K_42G8RIPCqsOD1DhVLykqeWyLqBWccveq_9a14F69CNd_ObEZYDEwQKEyBofswRI_1vvGzEpziuMLtEJiwVXYu5cEoVkr90-UC6g4dhz2JM71c3cs63pNHngzk5pLl24bwlhTBOEzcdLa3LnjZ2wWOyBS2cHIFWBRuBmgBp9hxS4D8eTJ7VdJ4bgg8WltVzX7FZ56XDeYnGLPUVC7LPXoVXx9dKBOV8oz4AeUL9JW2Kuep_kz3FEa_KHXUoQBwWV1DH6kad_nQubsghiIdDdf5bQdMS16h9x6fpWoREpkUJpoywapZeSIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو: همان‌طور که یک متفکر زمانی گفت، به‌ویژه در روسیه، او گفت: «دولت اسرائیل یک ابرقدرت کوچک است، اما ابرقدرت است.»
🔴
ما قرار است به یک ابرقدرت بزرگ جهانی تبدیل شویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/119944" target="_blank">📅 17:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119943">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Srjfrh-CmfDmSBWbLMa69rXsn6R6J9WNDI3_AqOXFQD9_4BD_vneHo7IGauX0W5lOdJXP4vjYW62h__rhVLvRqENNJML6TpuEEhrS6PpniUxf-QkP94plptKIqzN7plLEGWgQI3A8kUqPrhyVwhO7VtFX6B9_IewfJTSNHkaXr1rPowBdN8onqx6w6ODISswnDpRnXSFGeWhyKSr0JWbc87oTk_jOtZLuOEnvO_Sd9tcCmWW3N-GcBbL2hjoEulTy94WhharV4zwLvm2kdTRZ5tsn8WGDKLT84rJQoeNn_6ANp1ER5AH54sDBWwzLIpnDjw6Ms-fxk6AcEgXYfFCeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزرای خارجه روسیه و ایران در دهلی‌نو دیدار کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/119943" target="_blank">📅 17:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119942">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
روزنامه اعتماد: پیگیری ها نشان میدهد زمان احتمالی وصل شدن اینترنت «شاید نیمه خرداد» باشد!
🔴
نخستین نشست ستاد ویژه ساماندهی و راهبری فضای مجازی قرار است طی هفته آینده به ریاست عارف برگزار شود. ضمن اینکه طبق شنیده ها این ستاد قرار است زمینه‌های لازم برای رفع انسداد اینترنتی را فراهم کرده تا احتمالا تا میانه‌های خردادماه زمینه اتصال شهروندان به اینترنت بین‌المللی فراهم شود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/119942" target="_blank">📅 17:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119941">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ادعای خبرگزاری یونهاپ: یک مقام ارشد کره جنوبی گفته است که بعید به نظر می‌رسد عامل حمله به یک کشتی باری کره‌ای در نزدیکی تنگه هرمز، کشوری غیر از ایران باشد.
🔴
خبرگزاری یونهاپ: یک مقام دیپلماتیک کره ای گفت که دولت در حال تمرکز بر جمع‌آوری شواهدی است تا ارزیابی خود را در مورد حملات به کشتی باری با پرچم پاناما که توسط شرکت کشتیرانی کره‌ای اچامام در تاریخ ۴ مه اداره می‌شود، پشتیبانی کند.
🔴
این مقام وزارت خارجه افزود: «ممکن است همچنان احتمال حضور بازیگری غیر از ایران وجود داشته باشد، اما عقل سلیم میگوید که این احتمال بالا نیست. هیچ دزد دریایی در آن حوالی نبود.»
🔴
این مقام اضافه کرد که سئول انتظار دارد در صورت اثبات این ارزیابی در تحقیقات بیشتر، «پاسخ مناسبی» از طرف ایران دریافت کند.
🔴
وی همچنین گفت: «به محض اینکه (عامل حمله) به‌طور کامل شناسایی شود، یک کارزار دیپلماتیک متناسب با آن را آغاز خواهیم کرد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/119941" target="_blank">📅 17:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119940">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
مارکو روبیو، وزیر خارجه آمریکا:
سرعت رشد نظامی چین در ۱۰ سال گذشته بی‌سابقه است، هیچ نمونه‌ای ندارد.
🔴
آنها میلیاردها و میلیاردها دلار در سیستم خود سرمایه‌گذاری کرده‌اند. فکر نمی‌کنم این فقط محدود به تایوان باشد.
🔴
فکر می‌کنم آنها آرزو دارند که در نهایت بتوانند قدرت خود را به صورت جهانی مانند ایالات متحده فعلی اعمال کنند.
🔴
آنها هنوز در این زمینه عقب‌تر از ما هستند، اما با این حال، پول زیادی سرمایه‌گذاری می‌کنند. آنها اکنون بدون شک دومین نیروی نظامی قدرتمند جهان هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/119940" target="_blank">📅 17:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119939">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سخنگوی کرملین ، دیمیتری پسکوف:
اروپایی‌ها نمی‌توانند میانجی در مذاکرات بین روسیه و اوکراین باشند.
🔴
آنها به طور مستقیم در جنگ در کنار کی‌یف شرکت دارند و طرفداران ایده وارد کردن ضربه‌ای کوبنده به روسیه هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/119939" target="_blank">📅 16:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119938">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nq3U-RZTksHn8YGOn9SkdghqWhvhurZodXUNYLeNf_MuKgzRrrcb6PcdBgbAf8ynFjVbo93b6-VepSyRRHGRTbQ7S_1fyW2NvwpAZ-gtDRfZgvSHYHNK5KMN073WsqA4T0yjiAiBAnRW9wtv3H1ie6VRZ2zpCljeUppNcX8p_niBrPA2456MtZrW4OCkQQe8kJtnF0N6BmvaxaoGYazNl3oYQT_gMxQfRWi-m5S4jK-e0vi5q--WwGeGWrPezGxxgiZjQbbUNMFfbKI_CE-ozQ5a_FpCQGYd5zvoZaGkcmzlvkDOV7_pWtkec3iewaB0p8_DUKrt6PKn3CkAlvQCCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حساب کاخ سفید در X:
تاریخ در حرکت است
🇨🇳
🇺🇸
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/119938" target="_blank">📅 16:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119937">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
رویترز: وزارت بازرگانی ایالات متحده گزارش داده است که حدود ۱۰ شرکت چینی، از جمله گروه علی‌بابا، تنسنت و بایت‌دنس، مجوز خرید تراشه‌های هوش مصنوعی H200 انویدیا را تحت توافق‌نامه‌های مجوزی که اجازه خرید تا ۷۵٬۰۰۰ تراشه برای هر مشتری را می‌دهد، دریافت کرده‌اند.
🔴
با این حال، تاکنون هیچ تحویلی انجام نشده است زیرا شرکت‌های چینی پس از راهنمایی‌های پکن محتاط‌تر شده‌اند، در حالی که تغییرات سیاست‌های ایالات متحده و فشارهای فزاینده در داخل چین برای مسدود کردن یا بررسی دقیق سفارش‌ها، معاملات را بیشتر به تعویق انداخته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/119937" target="_blank">📅 16:51 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119935">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d1ff0730.mp4?token=tgqfFRdbvwQmLJjG580yINrxj8u6InEAwXEU537N8ABTXZV5xvwAPMkkrU_DVgAMoLCGGN0Xnu4Pzytgy41kPukisrbBewt5pzezsWKlZC8kmZM272WHDANmHFbNRL4w7GwkjmjD9CZxoX4dw5g6Opb9TsEP4-KJxAPofpFrrIZ98dolmAVDddA9xjsFNacXEEV6OUQPsArnJctP8hsqCccu3E16zaSACzNYEOTsSas4aD6Cu-1R39RI4BFq9PYGNvmlKMF_UUcZix548Qa108yEc9WL0HDrGqP1q7CvrLsbFIIhreRXhlL8EDXJ5drOeI05Kd4Kkedoq6cCSqF-qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d1ff0730.mp4?token=tgqfFRdbvwQmLJjG580yINrxj8u6InEAwXEU537N8ABTXZV5xvwAPMkkrU_DVgAMoLCGGN0Xnu4Pzytgy41kPukisrbBewt5pzezsWKlZC8kmZM272WHDANmHFbNRL4w7GwkjmjD9CZxoX4dw5g6Opb9TsEP4-KJxAPofpFrrIZ98dolmAVDddA9xjsFNacXEEV6OUQPsArnJctP8hsqCccu3E16zaSACzNYEOTsSas4aD6Cu-1R39RI4BFq9PYGNvmlKMF_UUcZix548Qa108yEc9WL0HDrGqP1q7CvrLsbFIIhreRXhlL8EDXJ5drOeI05Kd4Kkedoq6cCSqF-qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایلان ماسک با پسرش X_AI_12 ، در سالن بزرگ مردم در پکن در جریان اجلاس رئیس جمهور ترامپ با شی جین پینگ همراه است.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/119935" target="_blank">📅 16:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119934">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سی‌ان‌ان: مقامات ایرانی از چین خواسته‌اند برای پایان دادن به این بن‌بست میانجیگری کند. از سوی دیگر، واشنگتن از پکن می‌خواهد تهران را برای پذیرش شرایط خود تحت فشار قرار دهد.
🔴
روابط دوستانه ایران و چین در عمل نیز مشهود است؛ به طوری که کشتی‌های چینی اغلب اجازه عبور از تنگه هرمز را دارند. روز چهارشنبه، همزمان با ورود ترامپ به پکن، ایران به یک ابرنفتکش چینی حامل دو میلیون بشکه نفت که از اوایل مارس در خلیج فارس سرگردان بود، اجازه عبور داد. این اقدام می‌تواند به عنوان یادآوری منافع ملموس روابط نزدیک با چین برای تهران تلقی شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/119934" target="_blank">📅 16:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119933">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJcYEVBpzf_9XPp7SWqtvUDJ37mR-pTI9n-bvSP5kubanYIz5a_H7bGSj_sonWDwwUslYnjOVyUkw7KBuZ3P2M2MYNQn9wqvh1v-hlM2bqbqyNpcqJYtoTTxXGYeoW-BFjbyBckxY1VstLbP_7DvcNt2DzPh3gV2c0zKx0HRXjOQMB_MM-sSnM_F9DOgD66te_svHV9fL9fy5XD4lXRsLc8uOMo9tPvU0VlCfy8aRAwTMFvXlGKDWC0i5UIRayERm3EKPkahFrPgpMMLRdpbq9qrSz5sspLN3r3rMT4mO5sxBMLh1ks66y8vdlRUoniu0ctm2Y8hcLkSJ6bUFVFVDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: نیروهای ما از زمان محاصره تا امروز ۷۰کشتی را برگرداندن و ۴کشتی را توقیف کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/119933" target="_blank">📅 16:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119932">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b272b4c4.mp4?token=KsAQJ8Fhdi4YvqmACw0pAE3FrHTZ7EBqqhEQDpXS9NBoYrh9ZMVBGyqdhypy6hUzUM_SQGRDmXai14dd_CTmaL0IlUmFFgKhQ99Pz3RuphNQyrBO_9nkIRz9wDE7d-LzMHuc6sOL_g5rTJYwF8XOIbynSyuvCbtxNUciBAfGx6GSa2J5_KVjuYelTWHQ2QAxAhDito02M54_gBgralUNdbrKr9A5a3MX-TG-5P-22zgUfXX_DRhHN3qwIRvvRF-l4POPyCOQOUQR0Po3Y5BRNNoV77w2DeCDQr7aJ41P9SadHXXET2aCHwkC7eiSskyZCL1-8wIP-yXq4W1hl8o2T4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b272b4c4.mp4?token=KsAQJ8Fhdi4YvqmACw0pAE3FrHTZ7EBqqhEQDpXS9NBoYrh9ZMVBGyqdhypy6hUzUM_SQGRDmXai14dd_CTmaL0IlUmFFgKhQ99Pz3RuphNQyrBO_9nkIRz9wDE7d-LzMHuc6sOL_g5rTJYwF8XOIbynSyuvCbtxNUciBAfGx6GSa2J5_KVjuYelTWHQ2QAxAhDito02M54_gBgralUNdbrKr9A5a3MX-TG-5P-22zgUfXX_DRhHN3qwIRvvRF-l4POPyCOQOUQR0Po3Y5BRNNoV77w2DeCDQr7aJ41P9SadHXXET2aCHwkC7eiSskyZCL1-8wIP-yXq4W1hl8o2T4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گوشیT1 "ترامپ موبایل" بعد از نزدیک یه سال تأخیر بالاخره داره عرضه میشه
- یه گوشی طلایی ۴۹۹ دلاری با برند ترامپه که چیپ اسنپدراگون سری ۷، رم ۱۲ گیگ، حافظه ۵۱۲ گیگ و دوربین سه‌گانه ۵۰ مگاپیکسلی داره
- به نظر میاد در اصل یه گوشی ساخت چین باشه که فقط مونتاژ نهاییشو تو آمریکا انجام دادن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/119932" target="_blank">📅 16:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119931">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NN20EEOIom_EoKTsBxH-0J2uuJbrQjsw_ubha1H1ue-OQhoD74F8JG2ultmbCs2Gl2gyHtuM-mKBH6jtjKq6nIO7Al8BjZ-MSc8CEtlQ1EBhPfWkNLX5U4JgF4-UDBlQdVKxB6g57JvKMDIPyHyerfCkPzcp9_GdrEUSnHo7zI7pwTj31ElKxLO02MNziJJAeZcpjA8JIM5-_5iCp00q9IAzsTsov-4NBKnCnELpz-gWCXihLFNlmqfh9CtXg5R0P4iTJcDjFPR1C2_mCteFaFmm6o7MzFCxcanMr-No2idOBTG0zGbXBxBrp47gWy_NBmCuSmKpS56jzFbGlcQq8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری پربازدید از رزمایش ۵روزه سپاه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/119931" target="_blank">📅 16:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119930">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a78d859539.mp4?token=nqFUo4KiFROrnBMiHXnRyTWEYapi06RWJ3Vwyxz1gzmjOnqWXoleaIoOxu9PjKoq7uzdehvRQAhaa4qOjvvZ_u3LaW-lwLv0wVP6o_7E8BetSWfsCJApmif8HFFhFIXvnHefzoq_O5L9LqYiT1kA8M39fhbh4HMxLYqFaavYdntyGvRedSuq7sJp2FJp13gvJoAMK01K0zVsjojECkeMQZJaTtKktTh2pJV_uqZcgtDQizjjmJhcxvWltTJSSQ7YIAldXy4t6Au508JT48yylnkVV1iLDzN6NOWNjGzq-BvSfekNC81jiLKepOhafoDO_vo9oImqodFSMw2NuQtQ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a78d859539.mp4?token=nqFUo4KiFROrnBMiHXnRyTWEYapi06RWJ3Vwyxz1gzmjOnqWXoleaIoOxu9PjKoq7uzdehvRQAhaa4qOjvvZ_u3LaW-lwLv0wVP6o_7E8BetSWfsCJApmif8HFFhFIXvnHefzoq_O5L9LqYiT1kA8M39fhbh4HMxLYqFaavYdntyGvRedSuq7sJp2FJp13gvJoAMK01K0zVsjojECkeMQZJaTtKktTh2pJV_uqZcgtDQizjjmJhcxvWltTJSSQ7YIAldXy4t6Au508JT48yylnkVV1iLDzN6NOWNjGzq-BvSfekNC81jiLKepOhafoDO_vo9oImqodFSMw2NuQtQ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دقایقی قبل اسرائیل بازهم به لبنان حمله کرد
✅
@AloNews
خبر جنگ.‌‌</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/119930" target="_blank">📅 16:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119929">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c14226825.mp4?token=p4-OEvb9TXsGJN91aIqUfw-E_pIVRkNEcAIFGk97vVOK5tU1MKLh3Fsuki0DjhLfm-Dv1wXJI81ud4DbafUlFd_epSBaG6ZC_ebMwFlFYXvISn2nDX8vu9WfEm6ZEuJM6chmFSLuNXFLl04uK7cpq6CdmzJQG3m7lCKSv66PvGIXqUQuiOMxuUDqyA4o1Z-dwYbf937P8EAXJNBaXGRPhGfAvXv-9MKUdMj4LmnKMzVeungFNNoxKoQBllO0fSm7Q308VXbDMJzZ6Q1ygPzgnb_6ppdl5lcOr5Cay4Z6KKrCLh3D5v5wqWNKztD3T9Cnzsw7CtIIt4E6_xjxPcOqxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c14226825.mp4?token=p4-OEvb9TXsGJN91aIqUfw-E_pIVRkNEcAIFGk97vVOK5tU1MKLh3Fsuki0DjhLfm-Dv1wXJI81ud4DbafUlFd_epSBaG6ZC_ebMwFlFYXvISn2nDX8vu9WfEm6ZEuJM6chmFSLuNXFLl04uK7cpq6CdmzJQG3m7lCKSv66PvGIXqUQuiOMxuUDqyA4o1Z-dwYbf937P8EAXJNBaXGRPhGfAvXv-9MKUdMj4LmnKMzVeungFNNoxKoQBllO0fSm7Q308VXbDMJzZ6Q1ygPzgnb_6ppdl5lcOr5Cay4Z6KKrCLh3D5v5wqWNKztD3T9Cnzsw7CtIIt4E6_xjxPcOqxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا : ما رژیم رو عوض نکردیم، ولی خودِ رژیم عوض شد
🔴
ترامپ هم بارها ادعا کرده، ما کارمون رو کردیم و عملاً رژیم عوض شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/119929" target="_blank">📅 16:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119928">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16e9579c2c.mp4?token=M7neKZuzXhJY3Q79oZSzaSZHriyObCuBX00hznZmNcpoolQ_9yOscSV5iaOBclk_cMK3mv77aG9PRDxnlFEdAxOa9uy_udc8gK1oWnWNugu9VG2WGOnYeq3PsP2K5u80Mcl-jIDGUStgNqDobhzyw9NCUVgLcwrcb-CoAy3jnh9o_dM2YwfQD3HtfQP1_Qo1a9TG8uruiIW1iRaRsyRc_JEQsU6zF5R_yUeswvMichfyfbvGzHo3qEUm9CMw08d2wuUHpHE2jRFRE8lQ3R_EP5K-nBYQh1V96OvLgyCzx9HWevONjvxmtkg9wlK4JU6XJb4e4DCMGicpqh9ONdW9Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16e9579c2c.mp4?token=M7neKZuzXhJY3Q79oZSzaSZHriyObCuBX00hznZmNcpoolQ_9yOscSV5iaOBclk_cMK3mv77aG9PRDxnlFEdAxOa9uy_udc8gK1oWnWNugu9VG2WGOnYeq3PsP2K5u80Mcl-jIDGUStgNqDobhzyw9NCUVgLcwrcb-CoAy3jnh9o_dM2YwfQD3HtfQP1_Qo1a9TG8uruiIW1iRaRsyRc_JEQsU6zF5R_yUeswvMichfyfbvGzHo3qEUm9CMw08d2wuUHpHE2jRFRE8lQ3R_EP5K-nBYQh1V96OvLgyCzx9HWevONjvxmtkg9wlK4JU6XJb4e4DCMGicpqh9ONdW9Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه مارکو روبیو:
سیاست ایالات متحده در مورد تایوان از امروز و از جلسه ای که امروز اینجا داشتیم بدون تغییر است.
🔴
مطرح شد. آنها همیشه آن را در کنار خود بالا می برند. ما همیشه موضع خود را روشن می کنیم و به موضوعات دیگر می پردازیم.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/119928" target="_blank">📅 16:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119927">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da369ff9fd.mp4?token=ma4Cnenj66k-AA8AAFAQ18F3Ubcg7dTmy4AFrI7MQ6sB187GmPXgX_nMDcLXdqEpd70RXaRQMWPeNXjGJHoAPcLHWsUN6QHyZc1ep9UoK5oNsAGq1B8s2WWLmdYMGGms8NETU-oHdpP5KdtJukLBtxbyNFbRG365Zcy3LtDsyoOYt8NK2g2svB13oxjm_z6gZoikrTB1XbJAW_Kds2XBgrWxyRHkZHn0xQWRj6YIGPuGIx4_u828EeybriYPuBxV9bU0G5fivffhEoEcCi4jGHhls_1FvMdmZOToUwakbyvkHjB7QHmxcMU2dG0kIq6qDKTTj_3AqD2mQENNg5-S-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da369ff9fd.mp4?token=ma4Cnenj66k-AA8AAFAQ18F3Ubcg7dTmy4AFrI7MQ6sB187GmPXgX_nMDcLXdqEpd70RXaRQMWPeNXjGJHoAPcLHWsUN6QHyZc1ep9UoK5oNsAGq1B8s2WWLmdYMGGms8NETU-oHdpP5KdtJukLBtxbyNFbRG365Zcy3LtDsyoOYt8NK2g2svB13oxjm_z6gZoikrTB1XbJAW_Kds2XBgrWxyRHkZHn0xQWRj6YIGPuGIx4_u828EeybriYPuBxV9bU0G5fivffhEoEcCi4jGHhls_1FvMdmZOToUwakbyvkHjB7QHmxcMU2dG0kIq6qDKTTj_3AqD2mQENNg5-S-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور ترامپ در پکن:
من می خواهم یک لیوان را بالا ببرم و یک نوشابه به روابط غنی و پایدار بین مردم آمریکا و چین پیشنهاد کنم.
🔴
این یه رابطه خیلی خاصه‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/119927" target="_blank">📅 16:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119926">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb14e02d3d.mp4?token=BHHHLbVsOqt8Ut99qlB9G4p89GXHycy5xUXQFFvNbeeCAw9OSOh3sCF9P4aeASx1vjXBCM5ghS3LT8JrNA6GlLW5f_M98kWSj6_XlJxfQfLKueoI7ryRmfH64Zal7Ng1RVM032GowC5aUI-CW9-OGaURNEudq38TqIsrV232EDsPLD5n6e_QrsTLyWDsZK45NzygqUyqrcFJUEsLAqkykC-T9LlSRbcQse0cyrzyTxjPt245_FB6k6Nqgr7ODCXrzed1IbOmuzPU1TxUCGjXDeW5qMt0IyfaSC3YvKLKvqSaihaiWhKSYmF7nr5wT7hKcXn3gQzGUB_UZabUglWq5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb14e02d3d.mp4?token=BHHHLbVsOqt8Ut99qlB9G4p89GXHycy5xUXQFFvNbeeCAw9OSOh3sCF9P4aeASx1vjXBCM5ghS3LT8JrNA6GlLW5f_M98kWSj6_XlJxfQfLKueoI7ryRmfH64Zal7Ng1RVM032GowC5aUI-CW9-OGaURNEudq38TqIsrV232EDsPLD5n6e_QrsTLyWDsZK45NzygqUyqrcFJUEsLAqkykC-T9LlSRbcQse0cyrzyTxjPt245_FB6k6Nqgr7ODCXrzed1IbOmuzPU1TxUCGjXDeW5qMt0IyfaSC3YvKLKvqSaihaiWhKSYmF7nr5wT7hKcXn3gQzGUB_UZabUglWq5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور چین شی جین پینگ:
هم چین و هم ایالات متحده از همکاری سود می برند و از رویارویی شکست می خورند.
🔴
دو کشور ما باید شریک باشند نه رقیب.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/119926" target="_blank">📅 16:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119925">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وزارت امور خارجه هند اعلام کرد که یه کشتی با پرچم هند در سواحل عمان مورد حمله قرار گرفته.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/119925" target="_blank">📅 16:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119924">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
یسرائیل کاتز، وزیر دفاع اسرائیل درباره ایران: ماموریت ما کامل نشده؛ ما برای احتمال اینکه ممکنه مجبور شیم دوباره اقدام کنیم، شاید حتی «بزودی» آماده‌ایم. گر اهدافمون تأمین نشن، دوباره اقدام خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/119924" target="_blank">📅 15:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119923">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T61QHmzeT8nmm6bslCSDLoFJfDOVmRiUaV4fjpS8HXkGaZoFtzdetnnPbVaqvDRIXAOKtxPOMn53jzfpVthgbAwX69Zxy0TkvqDGjC79gGzboyt3Nvtw6h1HqbZnuuMV2Kv3WRotryu6kFnt5IikojyICLLrlVspTbTAl9TrQQSC6ZfTYDV2eqxpa9FONPUk0sBfqVfGLj77GJNvZJRiV8drJ9o6F3XF7PsqEkCzAeXSng3-9mGdtkNihB0SXDZ1WJ4wltZ4qogCO1S86gfti6lOZ5NhQyqStmUdCEy7bOmJQ8Lt21l63Y7BUIH4tGnLKBhlSmYdl-7MY4J_VYJf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ توی چین یه جوری رفتار میکنه انگار اون میزبانه و رئیس جمهور چین اومده آمریکا.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/119923" target="_blank">📅 15:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119922">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
اکسیوس:
یک مشاور ترامپ اذعان کرد مشکل این است که «ایران زمان بیشتری دارد و آنها روی تقویم سیاسی ما حساب باز کرده‌اند تا به سودشان تمام شود.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/119922" target="_blank">📅 15:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119921">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: باز شدن تنگه هرمز به نفع چین خواهد بود و انتظار داریم قیمت نفت در شش ماه آینده کاهش یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/119921" target="_blank">📅 15:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119920">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
آکسیوس: ترامپ احتمالا بعد از برگشت از چین‌ گام بعدی خودش رو در مقابل ایران برمیداره. یا پروژه آزادی و باز کردن تنگه هرمز رو از سر میگیره یا حملات نظامی رو شروع میکنه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/119920" target="_blank">📅 15:10 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
