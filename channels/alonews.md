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
<img src="https://cdn4.telesco.pe/file/O2aWxPgh7A7l5-Le1oZrswqIGfq0EJpX4L_19Un-TS8jEGgbrnB4db_N1hAkJKdc12JlO8ziGQNnhLvBF3tQwDD6fRFEENQgy9I5m3TLC-iNZ_5PbL8neuZ3FRoiIQ4VyHjMaEW1uWPF3OPYgiyonr-5AOFSYeuZNLEyHKKc4025N_fiZsu5wq_HWvexJ76vX7GCST9YzmnMpgvZ0ylkbaFU7f_B_pZrzSD5f4XiNwDM4nOsL6HnyxJzWPDJu1DF81sLLWmpjovfbJraWiQCCZNUHUAKtgwYSwOrQsDnNFZiDX8jaZwd5e-aC8V1zx-srMfs8AQdkR48GfT57TubXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 952K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 16:29:40</div>
<hr>

<div class="tg-post" id="msg-120593">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی اتمی: وضعیت نیروگاه اتمی براکه عادی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/alonews/120593" target="_blank">📅 16:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120592">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
وزیر کشور پاکستان یک دیدار خصوصی با پزشکیان داشته که بیش از ۹۰ دقیقه طول کشیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/alonews/120592" target="_blank">📅 16:16 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120591">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ادعای اکسیوس: آمریکا تهدید پهپادهای تهاجمی از کوبا را شناسایی کرد
🔴
کوبا بیش از ۳۰۰ پهپاد خریداری کرده و برنامه‌هایی را برای حمله به پایگاه آمریکایی در خلیج گوانتانامو و کشتی‌های جنگی آغاز کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/alonews/120591" target="_blank">📅 16:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120590">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fff2934367.mp4?token=oJ0U0ASDprvuXjLS8CbKXS4Z9No0IxIX86BoUAQN1HDZFoPKTWDluxcbVK-Ayn_gHOYNRQudhof1MmOlmy8CE97gRaJtkVJrP3eacu8X7Mm0vkImzB9nvvpcLv49ppaDoFrk0vICq1ju5IuOWMd0wsH97Er4SuzW7UuwU47Q_zsIJDZtGyrEvkBQLgkTA5FH8GqXGBlc_Dm_kBaR7MPbubblD4OF6je-EPqezJMD6ZFB_JAUMACrYs7zpv4OoNIau5g-pg2p_uCEAkNFLvn8dKpuvkV8-qtoRzGp3Oe-Jiqs0xgaezFUIbp_qpVgZjT6BwybLb7k_abN8SSlA3Z-Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fff2934367.mp4?token=oJ0U0ASDprvuXjLS8CbKXS4Z9No0IxIX86BoUAQN1HDZFoPKTWDluxcbVK-Ayn_gHOYNRQudhof1MmOlmy8CE97gRaJtkVJrP3eacu8X7Mm0vkImzB9nvvpcLv49ppaDoFrk0vICq1ju5IuOWMd0wsH97Er4SuzW7UuwU47Q_zsIJDZtGyrEvkBQLgkTA5FH8GqXGBlc_Dm_kBaR7MPbubblD4OF6je-EPqezJMD6ZFB_JAUMACrYs7zpv4OoNIau5g-pg2p_uCEAkNFLvn8dKpuvkV8-qtoRzGp3Oe-Jiqs0xgaezFUIbp_qpVgZjT6BwybLb7k_abN8SSlA3Z-Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نارندرا مودی، نخست‌وزیر هند، به گوتنبرگ سوئد رسیده است، جایی که قرار است با اولف کریسترسون، نخست‌وزیر سوئد، و اورسولا فون در لاین در رویداد World of Volvo دیدار کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/alonews/120590" target="_blank">📅 16:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120589">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
نیروهای دفاعی اسرائیل هشدارهای تخلیه برای ساکنان ارزی (صیدا)، مروانیه، بابلیه و بیساریه در جنوب لبنان صادر کرده‌اند، پیش از حملات احتمالی اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/alonews/120589" target="_blank">📅 15:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120588">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
بلومبرگ: امروز یکشنبه هیچ گونه ترددی در تنگه هرمز ثبت نشده است
🔴
تعداد کشتی‌های عبوری از تنگه هرمز روز شنبه به ۱۰ فروند افزایش یافته بود، در حالی که در روز قبل از آن ۵ فروند بود
🔴
تردد بارگیری تجاری از طریق تنگه هرمز تا حد زیادی متوقف شده و حرکت محدودی تنها برای کشتی‌هایی انجام می‌شود که بیشتر آنها با محموله‌ها یا شرکت‌های مرتبط با ایران در ارتباط هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/alonews/120588" target="_blank">📅 15:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120587">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نتانیاهو: شش سال پیش در یک جلسه کابینه امنیتی در مورد خطر پهپادها هشدار دادم.
🔴
دستور دادم تا راهکاری برای مشکل پهپادها و هر تهدید آتی پیدا شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/alonews/120587" target="_blank">📅 15:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120586">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
یک سرباز ارتش دفاعی اسرائیل به شدت زخمی شد و یک افسر به طور متوسط پس از انفجار یک دستگاه انفجاری در جنوب لبنان در طول شب، به علاوه یک افسر و یک سرباز دیگر در همان حادثه به طور خفیف زخمی شدند. طبق بیانیه رسمی ارتش دفاعی اسرائیل، همه آنها برای درمان پزشکی تخلیه شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/alonews/120586" target="_blank">📅 15:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120585">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ادعای نیویورک‌تایمز: اسرائیل حداقل دو پایگاه مخفی در صحرای عراق را به‌طور متناوب و برای بیش از یک سال اداره می‌کرده است
🔴
آمریکا به عراق دستور داده بود که توی دو تا عملیات توی ایران، سیستم‌های راداری خودش رو خاموش کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/120585" target="_blank">📅 15:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120584">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
کانادا اولین مورد ابتلا به ویروس هانتا را تأیید کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/alonews/120584" target="_blank">📅 15:21 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120583">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
رسانه‌های عبری: نتانیاهو امروز با توجه به تحولات و تنش‌های منطقه با ترامپ صحبت خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/alonews/120583" target="_blank">📅 15:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120582">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
اسرائیل بیشتر از یه سال دوتا پایگاه نظامی مخفی تو بیابون‌های عراق داشته برای عملیات‌هاش علیه ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/alonews/120582" target="_blank">📅 15:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120581">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-jEsoORQVuf4nE4UoEf1cNjJ1fTh1ggQVfSU6PAC9sR1PNM7390T5ZwYplTogW4_I5FoHd32xhM-41WTdescJ9fEgrSDUBVDJluZrSwmnSiPeOrExLuspI-6L5_iVJGYVR2Wa9LnToIwch-fLVceUyX7dNdenIHt8EvLhe7kTxY-ZNRVQ4m5o7N2iv0yXhroFLSi8D7gPgqJLBHI1LEZcYOgOIIuxJW_gGggA4Vnav2-PlfeA8Kj4solTdMjQv04gNVbiBLlwxQSEMHycOBsABRYiWpW50h3A7bJbrpdptOFCQePOxT7LKw2pLj9xbhz88Ux0pZ1B1w-rSocCTOlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی گیگی
9️⃣
8️⃣
1️⃣
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
💤
این تخفیف فقط تا ۱۲ شب فعاله
💤
⭐️
@Napsternetiran_bot
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🔶
@Napsternetvirani</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/120581" target="_blank">📅 15:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120580">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ادعای نیویورک‌تایمز: اسرائیل حداقل دو پایگاه مخفی در صحرای عراق را به‌طور متناوب و برای بیش از یک سال اداره می‌کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/120580" target="_blank">📅 15:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120579">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
نتانیاهو: ۶۰ درصد غزه در کنترل ماست، برای هر سناریویی با ایران آماده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/120579" target="_blank">📅 14:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120578">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
دبیر ستاد ملی جمعیت: اگر با همین شرایط پیش برویم، در ۷۵ سال آینده جمعیت ما به ۳۱ میلیون نفر میرسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/120578" target="_blank">📅 14:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120577">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
هاآرتص: دادگاه کیفری بین‌المللی حکم‌های بازداشت مخفیانه‌ای برای پنج مقام اسرائیلی، از جمله سه سیاستمدار و دو افسر نظامی صادر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/120577" target="_blank">📅 14:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120576">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
عارف معاون پزشکیان: ما تا حد امکان قیمت کالاها را مهار می‌کنیم و بقیه آن به مسائل بین‌المللی بازمی‌گردد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/120576" target="_blank">📅 14:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120575">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
روزنامه Dawn پاکستان به نقل از منابع دیپلماتیک در اسلام‌آباد: سفر اعلام‌نشده وزیر کشور پاکستان به تهران در چارچوب دیپلماسی مستمر اسلام‌آباد برای احیای روند متوقف‌شده صلح میان آمریکا و ایران انجام می‌شود.
🔴
این سفر برنامه‌ریزی‌نشده با هدف جلوگیری از فروپاشی کامل مذاکرات صورت گرفته؛ به‌ویژه پس از آنکه شتاب حاصل از دورهای پیشین گفت‌وگوها در پایتخت پاکستان به‌شدت کاهش یافته است.
🔴
انتظار می‌رود وزیر کشور پاکستان، در جریان این سفر با مقام‌های ارشد ایرانی دیدار و گفت‌وگو کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/120575" target="_blank">📅 14:16 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120574">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rL8M1IC5szziD8T9MuzwcjbSVZsG2bsoNLqIYvSQ3GNypRK-LrgDINmLbUyU4T9oQ052PJJzRKm4owXSyFvIMUus0nTdRh4mmGceqqRMpHNiyVwaeH8UrBEf-gpB96uoN-XWJSUM1iUI3KDtmHtFmAJ4DMikGCbnMSTE6MHW90tgIDvqeUWoyKKvO9s_E-y2ditv5OroFl2O2bKoWRD52kU8OiH5Aqr67vKz-VvS_GQJeLp9GNF9N2OM8R9HkLDccLRP6EWHbaTMOYBYtoxLGUMivwXx3rjzPKW6iLU6qUW6qoxQ1lZRoZ-5D-hM3djQb6NInyOJmIih3nf3LNsUeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور در شبکه اجتماعی ایکس نوشت: ‏در روزهای جنگ، فرزندان ما در ارتباطات و فناوری اطلاعات، شبانه‌روز ایستادند تا ارتباطات و خدمات حیاتی کشور پایدار بماند. دسترسی باکیفیت و پایدار مردم به خدمات دیجیتال، بخشی از آرامش، پیشرفت و حق زندگی شایسته مردم عزیز ایران است.
🔴
روز جهانی ارتباطات را تبریک می‌گویم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/120574" target="_blank">📅 14:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120573">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
اقتصاد اسرائیل در سه ماهه اول سال ۲۰۲۶ به دلیل جنگ با ایران ۳.۳٪ کوچک شد، طبق گزارش کانال ۱۲ اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/120573" target="_blank">📅 13:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120572">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
گزارش سی ان ان از کابل هایی که زیر تنگه هرمز خوابیده!
🔴
مدیر تحقیقات شرکت تحقیقاتی TeleGeography، گفت که دو مورد از این کابل‌ها، فالکون و گلف بریج اینترنشنال (GBI)، از آب‌های سرزمینی ایران عبور می‌کنند. این شرکت اعلام کرده:کابل‌هایی که از تنگه هرمز عبور می‌کنند، تا سال 2025 کمتر از 1 درصد از پهنای باند بین‌المللی جهانی را تشکیل می‌دهند."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/120572" target="_blank">📅 13:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120571">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
دفتر رسانه ای ابوظبی : یه پهپاد نیروگاه هسته ای برکه تو منطقه الظفره رو هدف قرار داد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/120571" target="_blank">📅 13:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120570">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
امارات اعلام کرد: آتش‌سوزی ناشی از حمله پهپادی به یک ژنراتور برق در نزدیکی تاسیسات هسته‌ای براکه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/120570" target="_blank">📅 13:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120569">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax7Cm-EIQet44QweJASmnEmXnqhB2707FLBZnwov1dPBuDflaFuOZkkd2P1JmSnXqIAcd4FCjxX4wxrItbEl_4K5SChLTNcScLBz_fhAhWriQ9lh-cqVfTnXh8QbJa730OMHDc_i-2CFJjRRLyJVW0PnsYtBcneN-NU7hJjAT_QFBDm1-D5JKPWSBEk1EnA7VvU4twtcuvXg4hdIf2Ci4jC-dosQaUWbqANM1j6SN337lcA1hE3r_lHL6--P18DO1DlyXZG35-bDt9H5C6Oa-tC53Ydl8qQQlF02-bIsgVdfvqOJD8FzqeHEXE42dcDYQkmjMqEaiv_B0AsQ5LtEbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جلیلی سوم!
🔴
پس از سعید جلیلی در سیاست خارجی و تحریم و قطعنامه؛ پس از وحید جلیلی در صداوسیما و سقوط مخاطب و مرجعیت؛ یک جلیلی دیگر هم چند سالی است بر زندگی شهروندان سایه انداخته.
🔴
رسول جلیلی، عضو شورای عالی فضای مجازی و مدافع فیلترینگ؛ کسی که اینستاگرام و تلگرام را اف-۳۵ و اف-۱۵ می‌بیند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/120569" target="_blank">📅 13:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120568">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
دفتر رسانه ای ابوظبی : یه پهپاد نیروگاه هسته ای برکه تو منطقه الظفره رو هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/120568" target="_blank">📅 13:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120567">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
پزشکیان: نباید با آمار غیرواقعی جامعه را ناامید یا شرایط را عادی جلوه داد؛ اگر اینگونه القا شود که دولت عامدانه در مسیر افزایش قیمت‌ها حرکت می‌کند، ناجوانمردانه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/120567" target="_blank">📅 13:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120566">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
برخی منابع خبری از انفجارهای مهیب در پایتخت امارات خبر دادند ولی علت انفجارها مشخص نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/120566" target="_blank">📅 13:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120565">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQIsISRzSxoR1ABUSByeb1D0gzJl_YxeJ8qb0vvQv_SZi8-DN7yiPFCthh5bfQS8CLStpjUJAPUxlZxoCPVs118xxw3TRbl6QkkrG8rOLTtB_FMRKqGMoF5f6TWVYtnx7_SZxYRbqakxqmxPegzzS5NZrU-7JDDPUmBbiSc6rYDOfwYXFsRilnvYvC8lLzhDlmNHR3evi16J3FVEhGwzO8zOjGjBBxGTuze7bc8o9p0kcNllEnjbkzp4ila3d9qfexFfJqAXtk3uMLryYsSuzu02lzcAxyNaOKeOKijwTIzaK6MkaozCxrV7Kq1stUODU-tx0ibQvtu-Kx0ktR-tSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نروژ مرفه ترین کشور جهان تو سال ۲۰۲۶ شد نروژ این جایگاه رو بخاطر درآمد عالی،وضعیت خوب مردم،آموزش،ثبات اقتصادی و اعتماد عمومی بدست آورد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/120565" target="_blank">📅 13:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120564">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
حدود ۳۰ هزار نفر در فورتزهایم آلمان پس از کشف یک بمب ۱.۸ تنی منفجر نشده مربوط به جنگ جهانی دوم توسط کارگران در حین کار ساختمانی، تخلیه شده‌اند.
🔴
مقامات یک منطقه ممنوعه ۱.۵ کیلومتری ایجاد کردند زیرا تیم‌های خنثی‌سازی بمب آماده خنثی‌سازی بمبی بودند که طبق گزارش‌ها حاوی حدود ۱.۳۵ تن مواد منفجره است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/120564" target="_blank">📅 13:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120563">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
نتانیاهو قراره ساعت ۶ عصر به وقت محلی یه جلسه امنیتی محدود برگزار کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/120563" target="_blank">📅 13:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120562">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNDsFWNQwEN4Ix8E5-AEiDswBtzEJ67rXFPHrNyCiipP1rrAttb5eJUdx_s8tw1sZlZbVbidr_3Rv-PQCvRC34wXNAdAuuwgTb6kYhGv1zYvq39gQJcmtDXz8YqtCNCR8RzWXS3u1nd5Mj2uIBCdu6NuHAt4ILoCVX2OlvI6zdv9Am8S7cNwjmN2U_cNZJyY8QsXHqMqxoOjUs9VDmCylpGn8AIPCW9gqyjM94xDPro6WGg-5nWWsIlkmen_MVjMONokvBRms_h0ygXTbtDfDdb6YvsabKEvYwf1bIuBB6mvmWFkWabKad2vjzlq4lE__Q6sCgHuWFGWpP8bUeFsfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این حاج خانوم که تو خرابه های غزه داره قدم میزنه اينترنت پر سرعت داره ولی من ایرانی نه
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/120562" target="_blank">📅 13:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120561">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وزارت کره جنوبی : کره جنوبی و ایران به گفت‌وگوها برای تضمین امنیت تنگه هرمز ادامه میدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/120561" target="_blank">📅 13:16 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120560">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c08a1dc7e.mp4?token=SDZTRntUKfBGg6ipXSkN_LVnSgpU8oiLbHcNuSdjPBCHd-gysSkuIX1spFgonvkJ1U0gfQDDGeYbkL_CFhRgMKccRKEPLOekKEGnu1OWsSxUBGC55oqTPk0CRc9RfkED1PuA4HaaKP2EcS7_kIk4T5B1YKalXxALenyfnQUAPVt8GIsOO7ikL_wEqfTdP-DNq9BQUUXXdcz4hYQTVUWfBFSYpOGnTUzqgWYexcHzinaqkCQzMomYBUnnU1cZzeKtXJd3IpLgtARpqaNGJGJHe-gqgQ0xGlLyh3AIx09ui3vE_m1QaE1nQzl9T7KwIr7R8w4r_bzix4dtPwDT9k86bTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c08a1dc7e.mp4?token=SDZTRntUKfBGg6ipXSkN_LVnSgpU8oiLbHcNuSdjPBCHd-gysSkuIX1spFgonvkJ1U0gfQDDGeYbkL_CFhRgMKccRKEPLOekKEGnu1OWsSxUBGC55oqTPk0CRc9RfkED1PuA4HaaKP2EcS7_kIk4T5B1YKalXxALenyfnQUAPVt8GIsOO7ikL_wEqfTdP-DNq9BQUUXXdcz4hYQTVUWfBFSYpOGnTUzqgWYexcHzinaqkCQzMomYBUnnU1cZzeKtXJd3IpLgtARpqaNGJGJHe-gqgQ0xGlLyh3AIx09ui3vE_m1QaE1nQzl9T7KwIr7R8w4r_bzix4dtPwDT9k86bTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حاجی بابایی، نائب رئیس مجلس: اگر قرار باشد به نفت ما آسیبی برسد، کاری می‌کنیم که آمریکا و دنیا تا مدت قابل توجهی، از این منطقه نفتی گیرشان نیاید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/120560" target="_blank">📅 13:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120559">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9627342f.mp4?token=XlavYMrpNzk-h1skdbOFaaftLcls3E2SzYdfdNhZHvA53Otxya6a0lF1RNLNFwqOlX7eadOrj_jQA1Ar2bdBLWNr7JTfhRIHzjAhKX5aWZKki2FhfpNmMDqNztZy_WZBoKzst5Mmo9O7vTutx2VS_gplwiusQy1JN3-b_q2GiqFJlHhN5VYhPTFdGb7VOdhvNlYtPznyhRE-X2em9BNTlfM6TEcQIQMj_Xl2-oLaq3fXtoJ3bwdEJd2OY91OHYcSIkqTgxeGbVC097Ac-W1pVYB5P8lAHl_J50El20OZ00OODic_bNrJbubjpAW3ied5Qi-o8apF40SwtTgBnjmmIoPqEspAmFwQS5ysUAz1LJXpN5oWwC0gQRuQxxBbEALbI4v6Asw1-WkfNJzD1u-P3lv5TNlO1PKSmQTZo0r26iSUhEjik7wC24tcAJvMyEGr7WWIhD3yFbXxCVBq31o-I89Q-sIMqLkt4NjuOTpMqC252jAH4sjeVe20IloIlhx1QV8w6B-3Jyv_BiueddSGc9IcLXNr-Yo5VufT45R7PbYq8IqaKWoAsdns-3_iRWfzMBccNvhOdtvV-hWszeP25yeCtlMZu7cHwUp76g8xS3vpgtP_mlqxEBLGkhBPsg2dMAFvQ1JufBQvuvRQEHQvEUg1PStPdYyyveY3y_tQr6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9627342f.mp4?token=XlavYMrpNzk-h1skdbOFaaftLcls3E2SzYdfdNhZHvA53Otxya6a0lF1RNLNFwqOlX7eadOrj_jQA1Ar2bdBLWNr7JTfhRIHzjAhKX5aWZKki2FhfpNmMDqNztZy_WZBoKzst5Mmo9O7vTutx2VS_gplwiusQy1JN3-b_q2GiqFJlHhN5VYhPTFdGb7VOdhvNlYtPznyhRE-X2em9BNTlfM6TEcQIQMj_Xl2-oLaq3fXtoJ3bwdEJd2OY91OHYcSIkqTgxeGbVC097Ac-W1pVYB5P8lAHl_J50El20OZ00OODic_bNrJbubjpAW3ied5Qi-o8apF40SwtTgBnjmmIoPqEspAmFwQS5ysUAz1LJXpN5oWwC0gQRuQxxBbEALbI4v6Asw1-WkfNJzD1u-P3lv5TNlO1PKSmQTZo0r26iSUhEjik7wC24tcAJvMyEGr7WWIhD3yFbXxCVBq31o-I89Q-sIMqLkt4NjuOTpMqC252jAH4sjeVe20IloIlhx1QV8w6B-3Jyv_BiueddSGc9IcLXNr-Yo5VufT45R7PbYq8IqaKWoAsdns-3_iRWfzMBccNvhOdtvV-hWszeP25yeCtlMZu7cHwUp76g8xS3vpgtP_mlqxEBLGkhBPsg2dMAFvQ1JufBQvuvRQEHQvEUg1PStPdYyyveY3y_tQr6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پارسا تاجیک، مهندس شرکت «ایکس ای‌آی»،  درباره روند تغییر پرچم جمهوری اسلامی به شیروخورشید در شبکه اجتماعی ایکس، توییتر سابق، توضیح داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/120559" target="_blank">📅 13:07 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120558">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وزارت نیرو: تغییر ساعت رسمی بیش از هزار مگاوات صرفه‌جویی در مصرف برق به همراه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/120558" target="_blank">📅 12:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120557">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83970d0297.mp4?token=uQ_PmfpGp1cRWURkMeKh1MD8w1A8JUTetzbo9nXcnLasTPvhBr4EjzjFTodDewNhhLDIenjMjgl5OiU41jGiFQk6d7dUS9_2nKiF4UNRwwniW8VXOZE6XBYAfbXfeTVVcx2QyNHX1UXY2uAyF6BVTRUVQRpMLHN-96Y-Ko0u5htaZ0o61HL2XQIuEMUTYp_4sjoDchdirbkXYv_QKpetm_ozFC-9rVD4MjXbtCq64x4H3z2csBJytEsunLMeoQwEf_tE_mywC7nlqr-xK4QG2J5xGhcarb9IfmP1f4k4fpQmU-QTMzGBokqN97jRcPTMamwsYco8FoUtWw_OGVlxdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83970d0297.mp4?token=uQ_PmfpGp1cRWURkMeKh1MD8w1A8JUTetzbo9nXcnLasTPvhBr4EjzjFTodDewNhhLDIenjMjgl5OiU41jGiFQk6d7dUS9_2nKiF4UNRwwniW8VXOZE6XBYAfbXfeTVVcx2QyNHX1UXY2uAyF6BVTRUVQRpMLHN-96Y-Ko0u5htaZ0o61HL2XQIuEMUTYp_4sjoDchdirbkXYv_QKpetm_ozFC-9rVD4MjXbtCq64x4H3z2csBJytEsunLMeoQwEf_tE_mywC7nlqr-xK4QG2J5xGhcarb9IfmP1f4k4fpQmU-QTMzGBokqN97jRcPTMamwsYco8FoUtWw_OGVlxdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله‌های شدید ارتش اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/120557" target="_blank">📅 12:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120556">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
سوپر اپلیکیشن بله مجدداً از دقایقی پیش با اختلال روبرو شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/120556" target="_blank">📅 12:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120555">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVcA0G1eaW4FpGUDo6H-9g3j242fX6l9FTqhFW4HdefAMjNLSHFJ2MuovKXFSLPzRoLTGHAi5esIhLBqKhP4YomznlNmv86B_irXXQVY5JVLEaZrlz0JeNLgZfYdCOsxUZXorAdVSsCiAJ9H-H4ceSz8iYj0sHYI7zEpwb9i3C6OyyHRSrMca4Z7nyv0GHqYyH410K6NDSXTjMmScgv2QH8PrtUBHE_LGfeShV9qGWDH5dOWAvg_hDFK9wzzRToNs_MnEviWXO6XhAGkEgHf00syEWE5wvUyLhzPBrgzGhbJdEI9P9fBX_qlKV9GUJEDD0Qc_L3JUXAqtj1mbIA1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلهکی: یکی از کشورهای منطقه هشدار شروع جنگ را برای دورماندن از تیررسِ ایران، به تهران منتقل کرده است
!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/120555" target="_blank">📅 12:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120554">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
جزئیاتی از درخواست‌های آمریکا از ایران در مذاکرات
🔴
براساس شنیده‌های فارس از پاسخ آمریکا به پیشنهادهای ایران، ۵ شرط اصلی واشنگتن به این شرح اعلام شده است:
🔴
عدم پرداخت هرگونه غرامت و خسارت از سوی آمریکا
🔴
خروج و تحویل ۴۰۰ کیلوگرم اورانیوم از ایران به آمریکا
🔴
فعال ماندن تنها یک مجموعه از تأسیسات هسته‌ای ایران
🔴
عدم پرداخت حتی ۲۵ درصد از دارایی‌های بلوکه‌شدهٔ ایران
🔴
منوط‌شدن توقف جنگ در همه ساحتها به انجام مذاکره
🔴
این گزارش تأکید می‌کند که حتی در صورت تحقق این شرایط از سوی ایران، تهدید حمله آمریکا و اسرائیل همچنان پابرجا خواهد بود.
🔴
کارشناسان معتقدند طرح پیشنهادی آمریکا به جای حل مشکل، در پی دستیابی به اهدافی است که این کشور نتوانسته در طول جنگ آن را محقق کند.
🔴
در مقابل، ایران انجام هرگونه مذاکره را منوط به تحقق ۵ پیش‌شرط اعتمادساز دانسته است که عبارتند از:
🔴
پایان جنگ در همهٔ جبهه‌ها به‌ویژه لبنان
🔴
رفع تحریم‌ها
🔴
آزادسازی پول‌های بلوکه‌شده ایران
🔴
جبران خسارات ناشی از جنگ
🔴
پذیرش حق حاکمیت ایران بر تنگه هرمز
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/120554" target="_blank">📅 12:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120553">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Os8iicC7q6quuQltaHglvJgEP3k2hdbxoYalbp2U9l85CNnTYCuQ_CE2KKXTJA6PmSgIeiPwBA7GYwB_yBde0_UPPT8uGCsiwk-ZSdQ1o124nenCsNxUO8s_cDXvF2mjWDtHbaRsrqL9YrZUpvCjaJ1VGEjGallAS3-JYwKek2iv-CixeGvHhXAJ2Nunc-ZP0G_X-GfMaMlSguhjC2FocPQ-GjUaX9KidY6M0vrxOAgAuDmNpZL5xWJjtoE9mbYqM3f0vzmpbKnOrSKwig6V9f7_WC3oyGGeigFv3YWHyxd98iIuKpC5-aWqN0hGvcddZOZwlX-O2e4HwHqhiMn5gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست ترامپ تو ثروث سوشال : یه شب بزرگ تو سیاست؛ از همه متشکرم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/120553" target="_blank">📅 12:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120552">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBuSTV5cncXaycxC6mwncTkD1JkARasnZHLTEjaKKfix5G6NB8gVYUGVYHCzB30X1BNx9ytLDDTkUYJ8B6DOBaxufnT3VZMxevnpC61ys-RWTSaf92yfDZo0CFwfwC4xBPyiKLl8zJz2hqJnZVYfhjm3fICo3Ozt6G51keIbWUItn-_iXZaY-fUBuADXNe_6Sc2wTkmcCYigk1Lo6tBVSesHl0SENbGWyZk7xeweAC9DqmzVyvOa9fSUJzchkNQ8ZnYLBIYi92OZG3YLTmTkexnchhHIo8JEGdrUxhEcrY3SE__Pu-Wl1fmZy6FcCQ3kZqwNMUVldnNdoVKgvtkaeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا تو اصفهان برای خانم‌های بی حجاب ابلاغیه دادگاه ارسال میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/120552" target="_blank">📅 12:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120551">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزارت کشور عربستان: برافراشتن پرچم‌های سیاسی یا مذهبی و سر دادن هرگونه شعار در مکه، مدینه و اماکن مقدسه از جمله مسجدالحرام، مسجدالنبی، صحن‌های آنها و مسیرهای منتهی به آن ممنوع است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/120551" target="_blank">📅 12:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120550">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pJCoV_hplISPIgFQj9NzNmXy6p3uY2uU-zlAvQxmJY8SlFVdamFL2JsFyP69-dctzohc_0u0aD7r1QT5nU6oeq4TqzdfWTXvyxrQCJ-4-abYTqjmyuNnnluo0YjUYsR5EYNGk9wqHTJYrifq6rBqyBJGRuYMFhp-BSoDegXJs_fasWP1cZIOcd297YKcng5gmnTqoMT-tflaLAfLgbkcjhRJp2ZdywDR8CzL-2VlycC-t__A6y6avUoCop5x06V09WWbfyn2KLzrcUG6eUJCY4Zk3aO2c-SCD5JDUhyi7dRFquEQd2m7sAib3PieCqBFKps2cfhU6eHlEUIdIPbVMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
💥
اینترنت آزاد و رایگان
🌐
🚫
تنها جایی که کانفیگ
رایگان
میزاره
⬇️
⬇️
@NetAazaadBot
@NetAazaadBot
⚠️
هر ساعت 100گیگ شارژ میشه، رباتو داشته باشید تا مطلع بشید</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/120550" target="_blank">📅 12:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120549">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YldQrQWrZ8JIf9A2EzkJ5XfA1WlSLYU-TQYSYoDYVveK9cyBLsybTCefeaQrpFHpoaqWkUo_UUA_F5ZeHdAC8Iqk86p2Y_MGd-ugPJsfiH0U7Dwfe1KqhYzrjRK3yV9Hy92gsxl9AD1FBWMGHqZ287vxEhF1lMEJzmsEtE41XoD3CTR7ROIKy5e9Yeh2P9mtwrvPdG87Py4HEbQbW2iNERLoiaVLuggtdgbzKaFLvbVK__h2EpL2xNJS8g32lCJ5vWTanRTZMWNRXSRcDEqlNF3wYr8X06KHmbJfsJM_z6yuIUQTJGIsGSDXG5hwcoDte1Rh1fFrLlVmILp6BztSFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میزان: دادگاه «صادق ساعدنیا» برگزار شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/120549" target="_blank">📅 12:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120546">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MGzgjkcY0M3m2IAGLC9ZdiD1A-bkRXqFgwQG3LxFfvk-2yIuf1ko9rZzinxy1jjxU-UZpS1muJTncI3n79618Jd02KIAJ-idEw8NjK9qjnS9AIK67GAVaVFiXPUPI7s4Tgju_adwoL4vNK35RSGbPqtTsyASmt_EUl7Mj7GfBFlZSpUJdxWUKsHtkvZ9e1NCg3OsyEL3sJrvEGZ2TYAB1k3rOSjsmKTNa7YmPVd25xJFiQ76RHNlAD8yzYT7ImQSP0jcpeMiUTMp-BjC1XLuvq2SiYtDvufsXL_C9JFsOJSYqFVq-f1VSwkj_F7hcAPCfNRHbBiqQgOJMf1U_IYIuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5UWQqL9LdoTY06bDMP0LcWJqTNy1BUIbKjV3mIHCeWFr6iEDSYl30C9o5xNVwnENsqHqNnWBFDf6q8kpKXY2BjkAewh_kqRRc-rSzsEo5cdITIvdAiItRNbY_JKxL2S7wV4weXxgcUyzvEXasDAIUZp2NoXb_Q3IV2uO5EtPxAc6hM3acS2B6c3CwOBg8QdzZnmU8t7yVJSg6jRGUp7sITm2Lp_Ymp-21CspOSTAesDlpeSf3gnavTZCrlA8cRxVy8w_VZGw3XD9oGmTrCMIEiRtzrKvcUKmahTnL8572ttQQFgsQaKBJaRGucDrDto6EFdo3RZOf4N7BhKDfBu3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B3gPsxpeTX_ZGEHclvIq0Rb_kFT5pkLrgqQ60ErfGGoeQFjZy5GkzH6eM72YnnlJuvsMlLRSV_618SZ8LQlPEo4fZjTesRLdQyeC0YhdP-IPV7x5prWgPtUntGh0XfWNgz5sikVnyfdOM4YcNKwU7PcKXQdqHU60EVCWf8hudPZ2ELOGci6PxSyd2bFEXE6f4Bu0W9UtXQPQmkdpMPuKSxDx4HbamAsxzFV_knznhbYTrOyjk6-sUriw16jaodhqF5F3owM3Dbj_CJBYIqKVMFSKXjLYbLR-0EbbZPaLTGI9YOLLA7yIErGuMlQQNc9QMffIXUB5SXQPszwRcXE15g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصویری از نصب مسلسل ۱۲.۷ میلیمتری گاتلینگ چهار اول نصب شده در دماغه برخی نسخه های بالگرد میل۲۴ با یک سامانه دید حرارتی در روسیه برای مقابله با پهپادها ..این سیستم بیش از ۲۰۰۰ گلوله بر دقیقه آتش می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/120546" target="_blank">📅 11:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120545">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCQL5hcvtI20egbxYuNiALfrM4MV08fAiadQ2ptMGM8oJg-FwN8v5umSNzJ12tmL_YSM61krS9j9WZT9kGUfKtCWgk2G-FXYV3vWzxedU9AUjBQ0ieRkuLnyXK-vDRpUjkK1uWSkA1aymU2u2whjBCmanPx9m_ERLViLhm-rAc4MTuCZ0vS-HewWnUrJhw7Df3ax9K_vHl1BPEam5idfJzhM8ONuE8fjWsUS7X1GLU-hA4y3gqmM5kCl9JlTDd4d8L6flggBkCxVDZK8XEdNNiFA02Uu-_66vA9cpNWmhYuL7C6StWaWpVxSv6muA5XN-jDHvzqinroG6RPiBfv4DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از چند ساعت گذشته بیش از دوازده فروند هواپیمای ترابری راهبردی C-17A گلوبمستر III نیروی هوایی آمریکا در حال ترک خاورمیانه و حرکت به سمت اروپا هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/120545" target="_blank">📅 11:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120544">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
فارس: محمدباقر قالیباف، نمایندۀ ویژۀ ایران در امور چین شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/120544" target="_blank">📅 11:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120543">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
معاون شرکت مخابرات ایران: دسترسی به اینترنت باید برای همه مردم فراهم باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/120543" target="_blank">📅 11:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120542">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAfJWAFnfPhDHpPMd9eFU76oXElfaOBxV6jTJBQ8GzibK8nIlRZyUsvgAkTxdiHi7VcsQPPR-IAKMlJIsKKFtM7Bb6AmDSc4wGZh3y30L2c8hjDS8ybrliZhxJGumKCUXecbcwC62yuWJOmQnF6lmmCVPSQ4Om9p9FnKWi2GIlgAhJQX3yi9HD_7skJdtCwbHXm6-sC2yXBYokQl5RF0CV8ACKf9WFynLwheUGjiRqFDc2tI7qxqYi6yy4qCqqdtRUnVN0I9T1NwHsWv8FnhjvKcRjYOsHI5owMYViHlrmTOSU06fTrZKstRj0xWPg827oJqAiFZH5P2RpcWMw3ksA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری لو رفته از گلشیفته و مکرون
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/120542" target="_blank">📅 11:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120541">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fy0UlrjiWbsY5tJzWiQ8UdnxsIPi3JQWFD9Pj3CCMdtdG2Y0WdSHt7GAlegYPl8_PUYSg_pQm68GlCzje86Anr2Hoq-WIRtw1LcWLIXcu5U52W-NFcor-3dnsI2pQSlx2Vo72Bl4P5Jzet6h-1BjbeNMQqWvA_jVwJqvEVdkGHzfIaKNwUwlLTxw7cCYRXp0X2xE12cNd1ShnO4Hgi5YcloI6ulA8IZxG9qwq3pAVz-ev-mF0DBgk0cVWouLvDJfnKaAQxxS0t8qpouTq0epW9n8LhP89KRcKY3sd4GefadCIirNmHD2hWyuJVa0HU2w_72frWY6uoPvZYDAXwyuZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفر ترامپ به پکن نمادی از کاهش قدرت آمریکا بود، به طوری که چین تنها رئیس‌جمهور را سرگرم کرد بدون اینکه هیچ امتیاز واقعی ارائه دهد، طبق گزارش آتلانتیک.
🔴
فرانکلین فور می‌نویسد که با وجود پروتکل‌ها و مراسم پرزرق و برق، دیدار شی و ترامپ هیچ دستاورد سیاسی یا اقتصادی قابل توجهی برای واشنگتن نداشت.
🔴
مقاله بیان می‌کند: «وقتی آمریکا دستش را دراز می‌کند، دیگر هیچ‌کس برای گرفتن آن عجله نمی‌کند، و وقتی تهدید می‌کند، دیگر هیچ‌کس ترسی احساس نمی‌کند.»
🔴
شی نه تنها از ارائه طرح مشخصی برای پایان جنگ ایران خودداری کرد، بلکه از امضای توافقنامه بزرگ تجاری یا ارائه تضمین‌هایی درباره دسترسی آمریکا به مواد معدنی کمیاب نیز امتناع ورزید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/120541" target="_blank">📅 11:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120540">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
قطر و عربستان وضعیت منطقه و آتش‌بس را بررسی کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/120540" target="_blank">📅 11:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120539">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfU8JGszgvOgGADbtYdDJru0_pWttQRZnZN8yDdzSY3sAihlNWECH4f6eFiSWwccJbq6XtFzN2b5yF7HOs3j2rsjNu3STA-euosn1sCsm_WdqcvMKs5EwwTan-uS8WtbTYLFRGJmz5htHJI15hAprruEb8s9xm9BXcM3V3vr8GZvlWHZoX6iZtjDhJu1MgUqMtIyOuO9vGJZKWMveCEsgnUAslcvYR1xRdnnohYBDC-2Vyccft8ArKiXv9I9LS3HsP7d7PtdOgmHMFeif2elHyaOHRlRF_i1Az29N6B0gllwpIOuwFmJhjWszrn6NSulhIWlyelzl2g2T06RP2fBJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌ان‌ان: ایران به کابل‌های اینترنتی تنگه هرمز چشم دوخته است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/120539" target="_blank">📅 10:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120538">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
خارگ همچنان ظرفیت ذخیره سازی دارد
🔴
تانکر ترکرز: در جزیره خارگ، ظرفیت مخازن ذخیره‌سازی نفت هنوز تکمیل نشده است. چرا که در این صورت نفتکش‌های مستقر در منطقه را تا آخرین ظرفیت پر می‌کردند که تا کنون چنین اتفاقی رخ نداده است.
🔴
علاوه بر این؛ ایران همچنان نفتکش‌های متعددی در اختیار دارد که می‌تواند نفت خود را با آن‌ها بارگیری کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/120538" target="_blank">📅 10:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120537">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
بر اثر واژگونی اتوبوس در محور عسلویه به کنگان ۸ نفر از شهروندان جان باختند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/120537" target="_blank">📅 10:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120536">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجارهای کنترل‌شده در محدوده جنوب اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/120536" target="_blank">📅 10:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120535">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BR1LVa2WJt_YbxzO97AzomXFh8_-oJBU1IMlTpquI1h5wsGqNiqEevUJRso0wbNmNXzbYslODgRoc-HNCbgDPPHZLIONMl6eghIfqew8IcA_BHPw45nzoA4jq-FGemrD5Fg90JFPX_IjzxzA5B08gZcWy2DgLEqt3cURYunRj5Bg8bbWXTMEigyGfqQxoNu1NOSQH16mA96AjfZMWqO0yYuIPTUQqwK7M_n5op0aR3PSh7VtKVjw0gDlNDxOD0_Ak9G8raS6ieorU7ej3T2SPRODEnNOc2ERzC83PdIduIvdwVd95ZhVLLScxXmKL6hLrQ0TMBR9dTj4NhKtECVaTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت 6 ساعت پیش اتاق جنگ اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/alonews/120535" target="_blank">📅 10:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120534">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
تایمز: انگلیس برای جنگ آماده می‌شود
🔴
یک رسانه انگلیسی از افزایش بودجه دفاعی انگلیس خبر داد و هدف از آن را آماده شدن برای جنگ های آینده اعلام کرد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/alonews/120534" target="_blank">📅 10:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120533">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
تایمز: انگلیس برای جنگ آماده می‌شود
🔴
یک رسانه انگلیسی از افزایش بودجه دفاعی انگلیس خبر داد و هدف از آن را آماده شدن برای جنگ های آینده اعلام کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/120533" target="_blank">📅 10:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120532">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab2461585c.mp4?token=HJfnoISB6FcRLQmF-GMnDJp72ZBFRhrrU8A5q-annNv8pIpH98wQASjMz0iVQGoraL7ql59yh5EUCDNS8ipX-cUzE3ugdq9SSGxDqp-T1ZBNa6WmpBU69Cdcu70bgsuXHoMn7GN05PIeL042-Aqbak472V6mVOHnagF1bd2wYqZYnryAVqYOSJdjYBIkIeRckjx9gNyOJyztPTeEmKFIisZkGMTy2BDA0x8DeBHlCA-CYMuhHTQyJF8zJFpuAKdzByn63xdwahtirCRR-gyzJm-zp_KyZc97DAOGk2nujxBlvcmcrMJ8Jkkltl15ClYhmW4qvaJU4wh5uUTlNc_m5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab2461585c.mp4?token=HJfnoISB6FcRLQmF-GMnDJp72ZBFRhrrU8A5q-annNv8pIpH98wQASjMz0iVQGoraL7ql59yh5EUCDNS8ipX-cUzE3ugdq9SSGxDqp-T1ZBNa6WmpBU69Cdcu70bgsuXHoMn7GN05PIeL042-Aqbak472V6mVOHnagF1bd2wYqZYnryAVqYOSJdjYBIkIeRckjx9gNyOJyztPTeEmKFIisZkGMTy2BDA0x8DeBHlCA-CYMuhHTQyJF8zJFpuAKdzByn63xdwahtirCRR-gyzJm-zp_KyZc97DAOGk2nujxBlvcmcrMJ8Jkkltl15ClYhmW4qvaJU4wh5uUTlNc_m5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت غیرمعمول امروز هواپیماهای باری برای سوخت رسانی به جنگنده‌ها در منطقه خاورمیانه
!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/alonews/120532" target="_blank">📅 10:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120531">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ادغام کنکور سراسری و آزمون پذیرش دانشجو معلمان منتفی شد/ آزمون‌ها با شرایط سال قبل برگزار می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/120531" target="_blank">📅 10:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120530">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
الجزیره: پاکسازی ۲۴ ژنرال آمریکایی در میانه جنگ با ایران
🔴
پیت هگست، وزیر جنگ ایالات متحده، در سه ماه گذشته بیش از ۲۴ ژنرال و دریاسالار را بدون ارائه دلایل روشن برکنار کرده است. این اقدام شامل روسای ستاد ارتش و نیروی دریایی و دیگر مقامات ارشد است و شائبه‌های سیاسی را تقویت می‌کند.
🔴
با ادامه بن‌بست مذاکرات با ایران، تصمیم‌گیری درباره عملیات نظامی یا محاصره دریایی پیچیده‌تر شده و پیام‌های واشنگتن به متحدان منطقه‌ای گیج‌کننده است. همزمان، وزارت جنگ درخواست افزایش بودجه‌ای نزدیک به ۵۰۰ میلیارد دلار کرده اما توضیح قانع‌کننده‌ای ارائه نکرده است.
🔴
کارشناسان هشدار می‌دهند ادامه این وضعیت احتمال دستیابی به توافق سیاسی و موفقیت نظامی آمریکا را در منطقه کاهش می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/120530" target="_blank">📅 09:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120529">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
قتل هولناک نوزاد ۴۰ روزه در مشهد!
🔴
مادر نوزاد می گوید: از خوزستان به مشهد آمدیم و سوئیتی را در خیابان نوغان اجاره کردیم.
🔴
دو روز قبل همسرم که مواد مخدر صنعتی مصرف می‌کند دچار توهم و بدبینی شد.
🔴
او ناگهان تصور کرد نوزاد متعلق به فرد دیگری است.
🔴
ماهی‌تابه حاوی تخم‌مرغ را برداشت و با آن ضربات هولناکی به سر نوزاد زد.
🔴
سپس با کف دستش چند ضربه دیگر به سر او کوبید.
🔴
بعد هم نوزاد را به شدت به زمین کوبید و باعث مرگش شد.
🔴
پس از این ماجرا جسد کودک را داخل یخچال مسافرخانه گذاشت.
🔴
او مرا تهدید کرد چیزی به کسی نگویم تا اینکه دو روز بعد موضوع را به صاحب سوئیت اطلاع دادم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/120529" target="_blank">📅 09:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120528">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
دولت ترامپ اجازه دارد معافیت تحریم‌ها بر نفت دریایی روسیه که در روز شنبه منقضی شود و مجوز موقت برای کشورهایی مانند هند برای ادامه خرید نفت خام روسیه را به پایان برساند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/120528" target="_blank">📅 09:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120527">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
آب و فاضلاب عسلویه : با توجه به تعمیرات ضروری در خط انتقال آب کوثر، آب شهرستان عسلویه از ساعت ۶ صبح روز دوشنبه، ۲۸ اردیبهشت‌ماه به مدت ۴۸ ساعت قطع خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/120527" target="_blank">📅 09:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120526">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سی‌ان‌ان: کوبایی‌ها خود را برای «تهاجم آمریکا» آماده می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/120526" target="_blank">📅 09:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120525">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
کوثری، نماینده مجلس: ترامپ در جنگ با ایران درمانده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/120525" target="_blank">📅 09:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120523">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77a1405883.mp4?token=kNZbBn7DNdEL4DmTag2qnyUEVuYrBlFMlguz0kULGqE5DqefPTQg4d75KB6aiCEUGDyk7T4Y9aXQdFUwYd4ezqsrF8IN4mAsYSihtOfvfNLSR-qNb_-Km2eoQo17bF3YaNod4BZUHiq31d0-b-KtpvwNjajkzDavPQJhy6lShRZFl5oyinTU4kijnhyw6K9I-7_k4YSfxD6p_GIO9yzrBb-xTul1UlaBeMyDwbnigEluQwYemOD7Q5UKqDZvcDfyYXFRTFWrONyY7fUy1aoVxefGI2L0BBk4LmIlW-t0aXQ7rOIzotMp3rkFazxSLk0gdaMLC9GPc5ghbJgrH-sKQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77a1405883.mp4?token=kNZbBn7DNdEL4DmTag2qnyUEVuYrBlFMlguz0kULGqE5DqefPTQg4d75KB6aiCEUGDyk7T4Y9aXQdFUwYd4ezqsrF8IN4mAsYSihtOfvfNLSR-qNb_-Km2eoQo17bF3YaNod4BZUHiq31d0-b-KtpvwNjajkzDavPQJhy6lShRZFl5oyinTU4kijnhyw6K9I-7_k4YSfxD6p_GIO9yzrBb-xTul1UlaBeMyDwbnigEluQwYemOD7Q5UKqDZvcDfyYXFRTFWrONyY7fUy1aoVxefGI2L0BBk4LmIlW-t0aXQ7rOIzotMp3rkFazxSLk0gdaMLC9GPc5ghbJgrH-sKQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پهپاد اوکراینی به ساختمانی در زلنگراد، منطقه مسکو روسیه برخورد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/120523" target="_blank">📅 09:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120522">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZqDL3AcXFS9yFnLuvjzoKLHZpCcjIDefcBONoHbYKQ97XP-hYKCPUNbej-_1HFedyRIsCJwDjfddVspOlRhdejKMuBFGnlE1iDODORZ4xqPIQW3_xUMA8qy39mjDtcAp80rp0R2x7G5Xvr01_2WWEJnLDw3bm_W6ZFXemXRo6eP30dB5z5cC47hvG-A8odqx9el2XFVB5OqZC7m2nPAKoYUHN2uB8DrjX13GTeKYZA6Ru6u7F0eblw4ng93j8V05hFu9xpcaLzpUpBrKxS6DwzKKj3XTV1JnBTX0GZeSpoTllbkQSB02EnLzrlwLYv-w_Efdzvg25-Vyo4oMysTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات پهپادی اوکراینی فرودگاه بین‌المللی شرمتیه‌وو در منطقه مسکو روسیه را هدف قرار دادند.
🔴
شرمتیه‌وو شلوغ‌ترین فرودگاه روسیه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/120522" target="_blank">📅 09:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120521">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
بلومبرگ:یک نفتکش غول‌پیکر پس از توقف چند روزه در خلیج عمان به دلیل توقیف توسط نیروهای آمریکایی، سفر خود را از سر گرفت.
🔴
این نفتکش غول‌پیکر به ویتنام در حال حرکت است و دو میلیون بشکه نفت خام عراق را حمل می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/120521" target="_blank">📅 09:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120520">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b9e336326.mp4?token=CmbpEE3axXMXOgkRxzaL2kl_2HrtFq_wbr_83G-2V5KUTpiQNEoaNqCT9HasRuustACkmfD9JBk6ssURc6B_vKCKX-4dK8J26U20c9Njv8K5sySIP2oBTWQ-xr0qUbZtkKz9fhrBGxstTu2r2B8cepjCiv1uJvsAG9ST7dALdGGIy8jCIsziU34BXgk0QEuKroFUg9jh__7Gl8g5A5GNwyXnckcQe-cfi8eAYbkfSS-SCg8WnsxiInUmsXxla2BAjABPZ4hprk6vJXqQDf36OhpG4Ap61Cx_hEqERsbOwAtbMxW8aGFe7LtOZbNmFDiw928DoEgQQgtgu9EbU2eGVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b9e336326.mp4?token=CmbpEE3axXMXOgkRxzaL2kl_2HrtFq_wbr_83G-2V5KUTpiQNEoaNqCT9HasRuustACkmfD9JBk6ssURc6B_vKCKX-4dK8J26U20c9Njv8K5sySIP2oBTWQ-xr0qUbZtkKz9fhrBGxstTu2r2B8cepjCiv1uJvsAG9ST7dALdGGIy8jCIsziU34BXgk0QEuKroFUg9jh__7Gl8g5A5GNwyXnckcQe-cfi8eAYbkfSS-SCg8WnsxiInUmsXxla2BAjABPZ4hprk6vJXqQDf36OhpG4Ap61Cx_hEqERsbOwAtbMxW8aGFe7LtOZbNmFDiw928DoEgQQgtgu9EbU2eGVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم‌اکنون : کشتی‌هایی که پشت دروازه‌ «تنگه هرمز» ایستاده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/120520" target="_blank">📅 09:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120518">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsVScsPg8gvNXXl9PAIeuB-llQaSAWsLkxf32bFs_1zOlC54zbvufuj18FeyDjZ1n3vT8FmGTfgsa2kQlWvXCEsqdA_5DFiuCNwrQWgRvvbqh3OBg-iw6DvB5EdAD6mJDlecjkd7mg3bpPV1nWgo5LcquMB0jAga_fr2hWmVprSzwvuaHZ6OOqOZC_u4Bw-6WaQGqtk9_oRHkXQD1oVNxFCPOwnIojM5Z9jtBGpCn24KYU-5BVgzilvo-Vx2uXSP55EG5sifgK2GXO8y3ZYGry8E4YeiQGpADYxTNfQ8ge0nk7t4YDAeSAKX3GF8-Fsk4nF7NDMVFY1zUI_pOHmJzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62322570a3.mp4?token=R6g650cu_WLNeTDliRPjPEdN8XgkUicE4BaMu7uAd3RVQC6TAZ9hj7cqkczwAepNd-glL2zPhFrkzwsHDBOwzMGTqawEY3xBdaHVezPjcPUJgUwCBsBqzel9f2oNqxryy6sDqSj6HPkCckOD0zIaFUNvtaTKrK6TQ5gyJ-fMrEkGc5_PGsA-Nud860rPsFISpBUlYQc6zKbo15TqXk2cu8DI97RNgtXMk5nJHq2PjAhHDau5vsfrqn7GzDw0epV1tp8QDkP-WhhFT3gi_eQJjXXBjfG-dUPrfMg8aBAIwaMkjruMohAe6pc1Za1JzDrUUUME3y3_LB5Ou2_oaBxNiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62322570a3.mp4?token=R6g650cu_WLNeTDliRPjPEdN8XgkUicE4BaMu7uAd3RVQC6TAZ9hj7cqkczwAepNd-glL2zPhFrkzwsHDBOwzMGTqawEY3xBdaHVezPjcPUJgUwCBsBqzel9f2oNqxryy6sDqSj6HPkCckOD0zIaFUNvtaTKrK6TQ5gyJ-fMrEkGc5_PGsA-Nud860rPsFISpBUlYQc6zKbo15TqXk2cu8DI97RNgtXMk5nJHq2PjAhHDau5vsfrqn7GzDw0epV1tp8QDkP-WhhFT3gi_eQJjXXBjfG-dUPrfMg8aBAIwaMkjruMohAe6pc1Za1JzDrUUUME3y3_LB5Ou2_oaBxNiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای اوکراینی ایستگاه پمپاژ محصولات نفتی «سونیچنوگورسک» در منطقه مسکو روسیه را هدف قرار داده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/120518" target="_blank">📅 09:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120517">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
فایننشال تایمز: تنها چند کشتی روزانه از تنگه هرمز عبور می‌کنند.
🔴
پیش از جنگ، روزانه حدود ۱۳۵ عبور انجام می‌شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/120517" target="_blank">📅 09:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120516">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
مقامات ونزوئلایی اعلام کردند که «الکس ساب» متحد نزدیک نیکلاس مادورو رئیس جمهور سابق این کشور را به آمریکا منتقل کرده اند.
🔴
ساب، وزیر سابق صنایع ونزوئلا و از متحدان نزدیک نیکولاس مادورو برای دومین بار به آمریکا منتقل شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/120516" target="_blank">📅 08:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120515">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
کیهان: احتمال بروز جنگ اسرائیل و امریکا علیه ایران در زمانی نه چندان دور وجود دارد؛ آن هم جنگ فرسایشی / دشمن شانسی در آن ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/120515" target="_blank">📅 08:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120513">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CLX2Lv8Y4Wl-BZvUplbkmtSfIDJveIxtRro_W47_hFSPhSo8q27bhuU2WWuo1TwuMptKC2e3-gGY353aZDC9nBNrVAmzP33O8QFoEi4egLeAqPOBO-VpCP_yZkkzQoXUFQHl1QRrg3IKBREOWpP4BMJFj-8vr9YD7g_OY-2IF_OKnoI2bydiA7Sx_Ob4O-TQACbvNEcw-d8Q7le5ZNTwNRUQ7BftRBIFbyHue-lHA_go8JlUn02ZPUTBLfq1yjQKMoWo5rKPwtbSOzhS_hYGWYZ81HIynLKndbQNrbpL29iJuQ9BAo-AK57gEchKul4OyOqQpvS6gAduWKuZdpm4SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QWo5j4vdepRsNvbm6jbQskU7WXMzVeF6hZHseS6NAMqBLJ0uTmA9izY7OfDDmJUhc_kqByZnr_uWpjcpnixpBE88Lc2SUTREBYc3xpEs4nanLwcjsRTd-g7tZzzUCBTPnWoTdRQ-l79W6SRzKbRnKxBaMFbss-XTjnCdaE_Hmp8-ZQRvw6dZEDPEJPkyuzcbEQoPFWaE0zoHiyrvrd7j223_ezfbqzgrUty_VZsRf9lFvnraN0xzHPbSy7YdTLwYKP1CWsJGA1sIa8y4s1Zp0GE8PstmnGgHIBTdiq1kku76RHksUxVVF64232q4DeYfnunQv75aafd_UNJrhnGyFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ به انتشار پست‌هایی درباره سفرش به چین ادامه می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/120513" target="_blank">📅 08:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120510">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QxGWJVKUcc3QgfC6FRF93xwa_3j0iTt4NY87f6JQz8VpyCijPgRcNl8nFfh49y0k3x8UZzJcbP2qyY8jVhxLMRRi9G_e3guYztM4v0r6nb-wZQQ55eKhi1dyesCvyIog7wfcAelF1eHg-J8aB25sa000kQ364nke4btmyVyGfIYErqLbFcd4O1K3Qkv65Gkzsv4urbSsZrajMT9ZecYpLE0uoA46DrHba14lpgJlR0dfhn6YqcjGyofg8oL0Qrcr-Lpqtw2IEqMu6y89gu8lvRfhrSkoIFVGxKKS-Ke8VazABpay8WEtcbxUtstKTv0Dt7rShntJ6fMOquJ9EiTpgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T0P9gVe9t_7nuY8Vr3q-SlVrEXX6FRqFSICGTndv_ZLWERCWhZDX_8OKU3IZ9jz1cas9zSgVbBhNY4ZMrbNX5kcXyQcG_IeSWuq70PlxCWI_vDAFbBrp5dQITu9-jVWXBDNYoCIevGSBT-N12nnqUFZapmrw6WOIM2kzVVTD0sTA7OI8vtPVaLlYXlDPEF4wUJ2Kqx1-ZBMqrXNeMx4T4shhD4vuyBAKnlYen8tWk5rbjb59cWYsylTeeFyn82MnHAHG80XqH0-FhNxSfTIWCao6mXvWyFic8RPx9hf65ZuEbhwz9o28oJY8kV0uzOTK36byW_DILuz8ipAVIEIO7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v9cRnG4dfu6fwuw3Kpv5a0kdAWjXdOq0j-IosPoh5HSw0B5UGgHBAgLiD6s1mVN_z9KN30LBpONLLGs2A8sttXvCjhgwoQF0R7trTAjQG5jX5OhxU5ld8hc3f5p_UscSlvJj3GbYljHNllCOiBxMD5tprMzmlTaf6ClfC0VLIZhBU7WfocuQMrzoth2CgPox6rX0f1AlnDyaH0_XNcq8jgkcspPDhA8z7fLhfbHKXovS8_nDezgF8EJ-PI0XGTxNqvaPvsntB8mVkg1dhlfVCIryd9QxyJHdzJ08_SEunTTZkrH3nC8V_0ZW-MfaQS3UFKZ5L8Z4h6KCPRJ2YM0DnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دونالد ترامپ در Truth Social:
🔴
«همان آدم قبلی؛ فقط حالا پرانرژی‌تر!»
🔴
«رئیس‌جمهور ترامپ جوان‌تر می‌شود»
🔴
«رئیس‌جمهور ترامپ برعکسِ سنش پیر می‌شود!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/120510" target="_blank">📅 08:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120509">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E7Z_XHhN6L3uUTo40PlhIPKmniSR8XTA54lP-ygDUNWpzoh0e-D15pSkrM8v9zCq_sWdwRAdbVrvng2SNPtZPg-S-0YwaoPCyeSf4aCEatwsrNhmNqFuGJAoWVKygCgHkvDQH_zmPMcXiANregJaRtEh0bhN_92vjT0KRqnvPXYh8Qqn1Ze51aRUG6ajKft5Lv5Q9CRAT76M5SS05kJWjMSWpYIuBT7JHwrak2h6KsT87K5JDso1cfBBVfPFXRW8Y198LALKwyIkaICDsy5mGAmGgodMSf8MRamAwoE42EALbbrt0cwaylHOvluFgKydcIIVSYjjmGVI1uCt_KTtig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید یک پوستر به سبک جیمز باند از ترامپ منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/120509" target="_blank">📅 08:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120508">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egQr4GivL8rhAcAyJ8Xs2TboE0ADK2fqQ_X46nBbVBjZBDZ-v9I9FlvqZqys4Jm95s8Lpytm6mkJTuRlmFq12UZ_BbhNL4F3F6HXozzuXQSuKZH09YiR2M9pbh5t0tG6titTRv_cZvOUHynPcaz5ChCRYYp-NJIK431CZYxirocYpV20AAQvGeuFxQJmCpKAFAFu9E6IjQjpx73LayahmK-gf2Hw9u69JfyzJrpZCknGS-wC9UzPF_MFMdgj3n8ZyRauKJtsVoGTmug20RXXtOVgjR6C-9FdYoHbTGgjopJyiWAis_kcALbI_Up2gsFbcvc0V20PpyWZqPvnG0ZK3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/120508" target="_blank">📅 08:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120507">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z03Ce7EDenF4YsjLKBbTNSizqo6ErDSUQfspYyYfC3qmrPl1oOMkOkawrRwWwxnZ18FqYOMuel67R7hdvAi4l96da9FGhBrGkKIsSuFlZ_tef97yweA5YFMyYNPzLPvXRhe2v01EPWijWrGqu4k_BYs7spudK6kZPAjsiE7LZjg-gyjZucMM_Go5OukqpAxLWt-4rDZU7fLF90oZjK_CCfLvBpdeBJyjd__nkGxRJG8mXe8h6xi_tw9uIzzUUITyR7_CdmLVLhfzh_0RpdY8u2PXSdwwINjgGWrxa5muMIbyTRm79Fczi2uhJYUF2bJoJyvKt0yD-ZKtj3I0Dmfxfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیلی‌میل: نخست‌وزیر بریتانیا به نزدیکان خود گفته که قصد دارد استعفا دهد و یک «برنامه زمانی منظم» برای ترک خیابان داونینگ ارائه کند
🔴
برخی از نزدیکان از او خواسته‌اند که هرگونه اعلامیه‌ای را تا پس از دریافت داده‌های نظرسنجی از انتخابات میان‌دوره‌ای به تعویق بیندازد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/120507" target="_blank">📅 08:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120506">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
رویترز: کانادا در حال تقویت روابط دفاعی قطب شمال با کشورهای نوردیک است، زیرا اعتماد به ایالات متحده در پی تهدیدات ترامپ برای تصرف گرینلند و الحاق کانادا کاهش یافته است.
🔴
اتاوا همکاری نظامی خود را با دانمارک، فنلاند، نروژ، سوئد و ایسلند گسترش می‌دهد و در عین حال به گرینلند در توسعه نیروی نگهبان محلی که بر اساس نگهبانان قطب شمال کانادا مدل‌سازی شده است، کمک می‌کند.
🔴
نخست‌وزیر مارک کارنی می‌گوید کانادا هنوز به شراکت NORAD با ایالات متحده ارزش می‌دهد اما خواهان اتحادهای قوی‌تر در میان «قدرت‌های میانه» است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/120506" target="_blank">📅 08:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120505">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5Ue2pki3hMwDEiWwq0xuK00HWvmmbuh-piLbBgQE_pbdxD0YnnPOR1RWfdPgnNO3pgx2TARD8khhv8vmPHCuByMMN-4GLZ5-zJ__tc7hLFasm65DMrD5xbp_Po06IJSTp1qfqpKDxslNAtDzRFQFAEe7PumDYNZ80atUgJH1GEB_w2xqfKfjtYq43ZxXkfl8oENpefbK43eSgrwKGYG0gCglCMqFjehWh2jGCOvDuAXcbq38BDek7eu-d_O-Vq3S6PGe54UHf9aXzHnFqvLWy3McK3UfZINx8MJ9Ysbx7QwQRWgUfcGrr5xYJazTNZZwEMzEzCvqkxB3qL3DRripQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: باید آماده نبرد آخر بشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/120505" target="_blank">📅 08:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120504">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
طی ۲۴ساعت گذشته تعداد زیادی ترابری آمریکا وارد منطقه شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/alonews/120504" target="_blank">📅 07:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120503">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbKHbPdN-qdFGyW7AvbvcQIM14G5txnpSkwvInUhL6PjgOVD9KS8J475ruK5nVG7X9-88khqkCXYAFN_qcu0rNZRCZX1v1W80QR3qsAJgxpQYPFSS9BCU3uTw9yiBsaIydtXGs2s_AYwpnQxzT2pPuZKgWcV43NyujmSMexpR0j8bTy2BBJx0_qAcnmCPMR3bqKYoNo9Dnfhho7Qxl4W0xz5wcdjMbutbgi7kQIedTRSC4UlmP3hYHywxYfaLhGyDjzgeT-XyHjQpxkt_YbyOAiV77t3ZwTHdwoh9lP9BeBkBzB3BlIM0dhNttuk0t1nqBaz-eUjOmzVMkj9_BYEag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بابک تقوایی میلیتاریست معروف:
انفجار در کارخانه «تومر» در بیت شمش، اسرائیل، کنترل نشده بود. این حادثه ناشی از یک حادثه بود. انباری که پرکلرات سدیم مورد نیاز برای تولید موتورهای موشک‌های زمین به هوا در آن قرار داشت، به دلایل نامعلومی منفجر شد.
🔴
به گفته منابع نظامی اسرائیلی من، این انفجار به دلیل حمله پهپاد یا موشک کروز نیروهای دشمن رخ نداده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/alonews/120503" target="_blank">📅 07:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120502">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GHb4jP5MQQ_U-WTJVX3qrf2AtB9NaHLDjKeEejIrkzVKa8_FXSrDGP7iOtRN7udpeC1CDYf2OotiZ425yKkLcFtW2cpqGb5RLciTndTdOK1nXNhWRakyNiy6I4iwiCd7JFQ31IwpPXfMvOltcVo8Ljh499TBVxt7-rRbZQDli3tgPcz95Ac8MoJHIvRUPwNa5v7HP-V9XEpWiY4nWBagHIMaCYCPhRPumiwWNQq-JXi0ovPgSaJwOFi8TbZd_W7p94oiAkkRact_5dAIsOdbrLlYMmXyOqFlk5YWVOM6PqqcWfA_d4odFn_ZLGEKj1mGPcQq2BMpdabDe-71jX6-GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
💥
اینترنت آزاد و رایگان
🌐
🚫
تنها جایی که کانفیگ
رایگان
میزاره
⬇️
⬇️
@NetAazaadBot
@NetAazaadBot
⚠️
هر ساعت 100گیگ شارژ میشه، رباتو داشته باشید تا مطلع بشید</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/120502" target="_blank">📅 01:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120500">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlGweNkOJmVkxVNYZaNO_RsMWGiYG8asEb-5yPXlxbAvBFIIBaIborbaZ2N0iEMW9MDbcq0r1lFRgzaoMT76wr6fnG3HAXshijao7oXTGYXWrhGgLdK-BV5CSxWQxFYXeZWqTP4vfuJn747s5GGDwpICTh-tk5uLAxFXBEWE0fuJoNJx3dhHQReIYW19sY1A499PGyrBTu9iYTSurNTd7TkoYGO9cZEDPYDr3vYz1vjiicdcndauWAlXGayyHTOxfmcJSRwllkPEaoIoN2Y21kugnSjcKyT7H6rbBgJf-NXh_-KPhvcI-v8J8vKz5_K8cxovduqoJn8561xti030_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میخائیل اولیانوف، نماینده روسیه :
کارشناسا میگن آمریکا و اسرائیل ممکنه به‌زودی دوباره به ایران حمله کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/alonews/120500" target="_blank">📅 01:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120499">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e011596213.mp4?token=mZ2QHSvm1HZxkBwlTjIb5fPvg-MRtDbDL4SzKpl2YJHuz-S2hmM1x8Wu7VvcXkZL9qqlith4Xe0erxEsylaivL7k8KRPI-vSIeNEG755q5FGu9eeD_Zpn4IGhzfmkUn0TC5YySwk59rYWjoP7EuAsoUWeR8xGoYmVpxgAKnp6w6ZuhzVXb58br-1MKWjt_AIP68mXoDptz9an2w76zthaQa5P4n2WXrSwk8srOAOQLyM3Ga0Ewr4sioEjlF4cJKvgHaeggl1xxksvZacEeBdFtJX5VIECUw5bJOp_H5wSuWx9atSoKSOpvzEElUF-6C3OFq9f3fC3Lu27oKWsI1NPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e011596213.mp4?token=mZ2QHSvm1HZxkBwlTjIb5fPvg-MRtDbDL4SzKpl2YJHuz-S2hmM1x8Wu7VvcXkZL9qqlith4Xe0erxEsylaivL7k8KRPI-vSIeNEG755q5FGu9eeD_Zpn4IGhzfmkUn0TC5YySwk59rYWjoP7EuAsoUWeR8xGoYmVpxgAKnp6w6ZuhzVXb58br-1MKWjt_AIP68mXoDptz9an2w76zthaQa5P4n2WXrSwk8srOAOQLyM3Ga0Ewr4sioEjlF4cJKvgHaeggl1xxksvZacEeBdFtJX5VIECUw5bJOp_H5wSuWx9atSoKSOpvzEElUF-6C3OFq9f3fC3Lu27oKWsI1NPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یادی کنیم از حضور غرور انگیز بیرانوند در دایرکت یک مدل معروف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/alonews/120499" target="_blank">📅 01:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120498">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmBb-DIA_YiE-_xIuvdga8SeBlzYqtcz4qTE6w3rJiuabo8vRp6e2NsawdRhHrAau4pCnbreYmxstG8Jbd4-PCwdI4SHO90gYXRjLtjoO8roSCr5yxTETod52Ecg2Hsj-pqO44ZCTzxiuQgIbbM8LqVF6Mt2QAwwUjPHkwIa3ZIXWF7DQXpQ3pN793KMNlpNq8mg-cKIID8rXOvBnoEaUbQ5l6qMHwq-i-ev69vw1WOsnHE5wMYoIVcX5XqeubSVDUlsIx6rBNeo3nMmLmoLCTn55YlA41t2Gi7zT1oMWlgO4DDbRES5jtJkr8WLbOVJGsHInxRzPfmQIZIP4mCx4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیرانوند : با صدای بلند و رسا کف آمریکا سرود جمهوری اسلامی ایران رو می‌خونم. مخالفا هم نمی‌تونن کاری بکنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/alonews/120498" target="_blank">📅 01:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120497">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sj0vDORE6vCYn7d8RLQ4ZkJcMS7qVfSSH372FY75Wvxgmoyj9jRg5lIRQESAyRMAgXunXRWUGQrnPO0YPjaFmEy0NEMjiCde1oYGSuU4TMyoaOerk3uyduNwFIaNsQEON5vg0cEagKkmQ2ofq9FZVk51BvT1sdD94h8LEN521eEUEGgg74FjBpcmduSA-RovkxDIKhPhKqWieiBPk6-OYioTcPqNsiwqNvk5O57fOBY9TeSq7MUG_UCsptX0ZROSOgtFonbAaLwLrHl5QJ4KyepxJdORJ3ASuaS1AdZ5wAr6CU8SJz3EGFLMHwlu7uLDHzXRkC61tC15bfUAj4vBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: تو آمریکا 9میلیون آمریکایی پرچم ایران رو دستشون گرفتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/alonews/120497" target="_blank">📅 01:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120496">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
شبکه GB News ادعا می‌کند که نخست‌وزیر کیر در حال آماده‌سازی جدول زمانی استعفا است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/120496" target="_blank">📅 01:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120495">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
کاربران فضای‌مجازی گفته‌اند که این انفجار بدون هیچ هشدار قبلی به ساکنان مناطق اطراف صورت گرفته است.
🔴
کاربران فضای‌مجازی گفته‌اند که سوال‌های بی‌پاسخ زیادی دربارۀ این حادثه وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/alonews/120495" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120494">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muPamYvHylvpxwzcsDCYF7ne_-VAfQ94A5Pak4RbHrtCP-dgf7_7WvHQathiKKmEiAWIjD1GPc86SDQoseqEPsb8K8lA63til7hXGM0SuQX2bh--0UK6xgl8PPJP-qUWhIMqij1vDysCgRmKDWw-fKLTV4dDR-m6DACRlyz3zKe9k7mhDdaakZrEJwTUEP7ZH3aUcwyM1DxySpEh42HzzhWTimNxuSjWfuWgr86yn7qg6n45Qj8MEjPO3CKpwW9rsA_6Q7Bo-pRcF_Opt9LviIXKY9vjORLs9t_dAfVgAydWHIIm-uZInebUL5SGfxkdyUi5Qw1CP4mBpGurvtEtgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
🔴
حدادعادل: والا منم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/alonews/120494" target="_blank">📅 00:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120492">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fHbdUxkOTZCbge2O7n4Te3n7HeNvuSX-EW7ZizvIAJ5txDN_1hJoOaGU4ZFOKoLoWsgf3Gt6k2TnnxfqsLnHIdoc6bFBwQ7LNTGsX6k8BeuOKdnYbnHWzY0CrE6PhMj3r95QHxuzOOKU_EsesE1txKFrwpj7M0iF64fsZa2_6m5V_vG2QYw0YQPxtWrD5uetXmrjLvPgyLVe7k7UsFF0cr7az4DmbJOue5BRwhAET_Kvr3Dd3-QFY3ryid_jptHhfwGmrj8DDDunvh-03CSAp8G8IM2WFOdwU9UrtCoBxOykz3fAUuKpSQ9hEoHcqQh-FZ7_In6PAf6MVNRl2g3New.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KE6XUqcspKVQfkffdCV2INot2dzZgwnOUXdb2VdAbV_e4RMaor8LegDub2DI_Fc7Rordx26uDs-S3YyuIXAcjTFpR4AtMLoQAd9wwFKmC8Wwg2aKNtq8d1Gy6sQPwImK__Lq4XnvLk8fetIiRGFiY9zyDiT_QWaH01XPp_DvTptUWLdr_Q4XqO3UyGCbl2e6PpZVDHkCif8sT1nNkssGu_Jb6_qhrb2z02j-8aJH9xe1-5MPxveTYnEM61wCTlz0F0BzqcIIKU6bFkRL8Ta5FdDId-U7fx-vkpYg1oNl9rp6CPTWl6uzNNHwbvIAbgRLYnuQzda4UhhD_bMd2cTXRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی از جمله Channel 12 گزارش داده‌اند انفجار بزرگی که در منطقه بیت شِمش دیده و شنیده شد، مربوط به فعالیت شرکت دولتی دفاعی Tomer بوده است.
🔴
این شرکت سامانه‌های پیشران موشکی تولید می‌کند؛ از جمله موتور و سیستم‌های مربوط به موشک‌های رهگیر Arrow 2 و Arrow 3 که برای مقابله با موشک‌های بالستیک استفاده می‌شوند.
اما هنوز مشخص نیست چرا این انفجار ساعت ۱۱ شب شنبه انجام شده؛ مخصوصاً بعد از گزارش‌هایی که آخر هفته درباره آماده‌سازی برای حمله احتمالی به ایران منتشر شده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/alonews/120492" target="_blank">📅 00:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120490">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6fa999c5a.mp4?token=oDcbJAt71o8shpHhzlmt55g6Zrgdc6m13Gr8dLc9xEweCv59uQNK3sZQ-AzPYL9HWsdYfy7ZiF6umeuPaYR7OURUiC_pk6ZSGE8ZH0sxOkCWQ-IhJZb2ZZbrn0wrk_zQoXuoug6wRL_rxfcztOLSi5dzPggULF2SrCRJ0Xw3jg7I_PaGQe0pRr_Z4_Vn3juP10TIDDiquMMhwyOv0CDbhv2Y0Uu8mIlM-Ybf8cmuecXTiZNozY2RUNtpJ51riMRFiqRDtJYl9BEXC4pJ3RNjaOiMGuQnPXaGpedGmzXXZ1sdAVqExgIk_qKWVIQPAmn_fuX-WCjkdNaxPcgetAd7bw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6fa999c5a.mp4?token=oDcbJAt71o8shpHhzlmt55g6Zrgdc6m13Gr8dLc9xEweCv59uQNK3sZQ-AzPYL9HWsdYfy7ZiF6umeuPaYR7OURUiC_pk6ZSGE8ZH0sxOkCWQ-IhJZb2ZZbrn0wrk_zQoXuoug6wRL_rxfcztOLSi5dzPggULF2SrCRJ0Xw3jg7I_PaGQe0pRr_Z4_Vn3juP10TIDDiquMMhwyOv0CDbhv2Y0Uu8mIlM-Ybf8cmuecXTiZNozY2RUNtpJ51riMRFiqRDtJYl9BEXC4pJ3RNjaOiMGuQnPXaGpedGmzXXZ1sdAVqExgIk_qKWVIQPAmn_fuX-WCjkdNaxPcgetAd7bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کان نیوز: حادثه بیت شمس اسرائیل یک انفجار کنترل‌شده داخل یک کارخانه غیرنظامی بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/alonews/120490" target="_blank">📅 00:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120489">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
رسانه بریتانیایی امواج: این ۱۴ بند شامل خروج نظامی آمریکا از مجاورت ایران، پایان محاصره دریایی، لغو محدودیتهای فروش نفت ظرف ۳۰ روز پس از هر توافق اولیه و یک ترتیبات حاکمیتی جدید برای تنگه هرمز است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/120489" target="_blank">📅 00:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120488">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
رسانه بریتانیایی امواج: در هفته منتهی به سفر ترامپ به چین، ایران یک چارچوب ۱۴ ماده‌ای برای پایان جنگ، به واشنگتن ارائه کرد.
🔴
یک منبع ارشد سیاسی در تهران که به شرط فاش نشدن نامش صحبت میکرد، به رسانه «امواج مدیا» توضیح داد که این سند شامل ۱۱ ماده‌ای است که…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/120488" target="_blank">📅 00:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120487">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
رسانه بریتانیایی امواج:
در هفته منتهی به سفر ترامپ به چین، ایران یک چارچوب ۱۴ ماده‌ای برای پایان جنگ، به واشنگتن ارائه کرد.
🔴
یک منبع ارشد سیاسی در تهران که به شرط فاش نشدن نامش صحبت میکرد، به رسانه «امواج مدیا» توضیح داد که این سند شامل ۱۱ ماده‌ای است که در ابتدا توسط دولت آمریکا ارائه شده بود، به اضافه سه ماده‌ای که ایران به آن افزوده است.
🔴
این پیشنهاد که تا حدودی به دلیل تشدید محاصره دریایی آمریکا علیه ایران – و ظاهراً با ناراحتی ترامپ – به تأخیر افتاد، حاصل دستورات صریح به مذاکره کنندگان بود.
🔴
به گفته یک منبع مطلع، پاسخ واشنگتن که از طریق میانجیگران ارسال شده، کل این چارچوب را رد کرده است. گفته می‌شود که آمریکا بار دیگر بر مواضع از پیش تعیین شده خود در مورد پرونده هسته‌ای تأکید کرده و از پذیرش این پیش‌شرط‌ها به عنوان پیش‌نیاز هرگونه مذاکره خودداری نموده است.
🔴
با این حال، یک منبع سیاسی دیگر که از جزییات امور مطلع است، چنین توصیفی از وقایع را رد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/alonews/120487" target="_blank">📅 00:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120485">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
گزارش‌ها از انفجار و نور بسیار شدید در بیت شِمِش در اسرائیل
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/alonews/120485" target="_blank">📅 00:07 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120484">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdtwhL7C28eWBMKyeIA8HvGsAa51UeFzGMzeQvFEMzDQp2cRhBzz0Cj1I2THNUZTZmPKDYJPqyHp7hjnw3S2xAYghKcVl-9mH4UsZ4pDsdTWQAOgkU0fL4T9uNC11ToDeDo9RUlHLfJXAWEXZW6WZ_vQKSit9a9hEMpyGFJ02EoWziBBX7qqPGlJissh0dL0Ga0VmmR-OVsgi8IVC_sMtYNsChZU3gPheIr3KCbQmlLAKuim5z5Lfw4iK7GCCM4ORHKGSbgGorkpw6jQX0_blds8WDuaK-H3Rig87llpYOyIzp-S6Hv7veX5aK6QTbx1n_tZRaFtv3TCmwI4xbCVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ عکسی از خودش و شی جین‌پینگ را در Truth Social منتشر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/120484" target="_blank">📅 00:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120483">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/87e8503cc8.mp4?token=uRi4EvM3WD5THqq6P4R_ka8vp4wYO7AZa5UbDWCeWKuhSnr6fbBFMs9qsXGfAwlVt3gha14tLCdGBUYhiwv20ukyOlkSc5iFJHhk_2y8vVAoO0mBM8AsHOlGZ70bGiM3Ku2g3QwwlhsEUUtUGnnq76EXjOnZTsq3ltvR9S28x0nYl11kkaLt5xvI6KA0Lznvua0HoP31fe8zjjT3U2N5nFXp0_jibZVZYvMV3aMR-7VNXP3HjU-Xyu7WGO7q3ujk88wpNTWDSUG4cl7DOKItoh2fw0-u628Fjdv_JNSThboFgLwTn3FBChUPS6RBMEaaf00P5XxB0JwL16m22UDRBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/87e8503cc8.mp4?token=uRi4EvM3WD5THqq6P4R_ka8vp4wYO7AZa5UbDWCeWKuhSnr6fbBFMs9qsXGfAwlVt3gha14tLCdGBUYhiwv20ukyOlkSc5iFJHhk_2y8vVAoO0mBM8AsHOlGZ70bGiM3Ku2g3QwwlhsEUUtUGnnq76EXjOnZTsq3ltvR9S28x0nYl11kkaLt5xvI6KA0Lznvua0HoP31fe8zjjT3U2N5nFXp0_jibZVZYvMV3aMR-7VNXP3HjU-Xyu7WGO7q3ujk88wpNTWDSUG4cl7DOKItoh2fw0-u628Fjdv_JNSThboFgLwTn3FBChUPS6RBMEaaf00P5XxB0JwL16m22UDRBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش‌ها از انفجار و نور بسیار شدید در بیت شِمِش در اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/alonews/120483" target="_blank">📅 23:53 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
