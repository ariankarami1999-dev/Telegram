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
<img src="https://cdn4.telesco.pe/file/N7lJ9EI_jdFitQWXEPdibUyRAVMAeNim7BDa4HlVnaduZVN9JEjNSMsuppOH79jtD5VOFJYjCH6GzY7aSjxP6j9077XOkW9pmc2j118ruF85M3NUpeevv1t-GDBcdAqbei-VWcncXoy3RlfsGmbAZi2gzWxX_qxpUvZbfLV-zkVGp2hM9v9UDlfEWt5nGRhNRY-BJptvrBkbhK2mAVBvTs7ca7JxIcCVbud0N8jGNv7rat7jC-Yf_3IK6qZ3fTWupxQAhevn6bP4PE2_OW5uGHCkig4TdTCL2Vs2lNnIQHOS31vZDGKUVlb_qgLR7mPBoXD904mAXAcQZ2muil1ryQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 17:54:16</div>
<hr>

<div class="tg-post" id="msg-136741">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
خبرنگار پرسپولیس:
🔴
امروز محمدمهدی زارع و پویا پورعلی در تمرینات عالی ظاهر شدن .تیکدری هم مثل همیشه خوب بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 274 · <a href="https://t.me/SorkhTimes/136741" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136740">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⚠️
☹️
کانال ۱۴ اسرائیل مدعی شد: ایران دستور توقف کل حملات به کشور های عربی را صادر کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 791 · <a href="https://t.me/SorkhTimes/136740" target="_blank">📅 17:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136739">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
تایم و رقبای سه دیدار دوستانه پرسپولیس در اردوی ترکیه مشخص شد.
❌
سرخپوشان در تایم های 8،4 و11 مرداد ماه با  تیم‌های «پیرامید»، «آنالیا اسپورت» و یک تیم دیگر به رقابت می‌پردازد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/136739" target="_blank">📅 17:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136738">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">💛
حسن روشن علیه قلعه‌نویی و فدراسیون
💢
حسن روشن:
«۱۴۰ میلیارد برای قلعه‌نویی ناچیزه؟! خدا رحم کرد تیم حذف شد! لابد اگر صعود می‌کردند به قلعه‌نویی و بازیکنان هرکدام یک استان می‌دادند!»
• روشن همچنین پیشنهاد فدراسیون برای تمدید قرارداد قلعه‌نویی به شرط قول قهرمانی در جام ملت‌ها را «خنده‌دار» دانست و گفت چنین پیشنهادی اصلاً منطقی نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/SorkhTimes/136738" target="_blank">📅 17:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136735">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⚡️
⚡️
🚨
🚨
🚨
🚨
فووووووووووووری
✅
محمدمهدی محبی نهایتا امشب یا فردا قرارداد شو امضا می‌کنه
🔽
تمام توافقات با کلبا نهایی شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SorkhTimes/136735" target="_blank">📅 17:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136734">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔹
🔹
🔹
فوری/کانال ۱۴ اسرائیل:
🔹
ترامپ دستور توقف تمام حملات به ایران را تا اطلاع ثانوی صادر کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SorkhTimes/136734" target="_blank">📅 17:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136733">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
شنیده می‌شود در صورتی که امیر قلعه‌نویی قول قهرمانی ملی پوشان در جام ملت‌ها را بدهد، در تیم ملی ماندنی خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SorkhTimes/136733" target="_blank">📅 17:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136732">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❗️
❗️
محمد مهدی محبی با عقد قراردادی سه ساله رسما و شرعا به پرسپولیس پیوست / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SorkhTimes/136732" target="_blank">📅 17:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136731">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
خبرنگار ورزش سه حاضر در ترکیه: محمدرضا اخباری هم اکنون در تمرینات پرسپولیس حضور داره و تیم رسانه ای پرسپولیس در چند روز گذشته هیچ عکس یا فیلمی از تمرینات گلر های پرسپولیس نمیزارن / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
…</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SorkhTimes/136731" target="_blank">📅 17:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136729">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
#تسنیم؛ پرسپولیس سفت و سخت افتاده دنبال علی نعمتی و میخواد با یه جلسه حضوری کارو تموم کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/136729" target="_blank">📅 15:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136728">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/136728" target="_blank">📅 15:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136727">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
مشکل رضایت نامه حل شده و قرارداد هم بین طرفین نوشته شده و مشکلی وجود نداره و ظرف چند روز آینده امضا میشه/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/136727" target="_blank">📅 15:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136726">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
✅
اخباری تو تمریناته و به همین دلیل چند روزه از تمرین پرسپولیس عکس منتشر نمیشه
🫪
/ورزش‌سه
😕
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/136726" target="_blank">📅 15:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136725">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
محمدرضا اخباری در حال حاضر دبی حضور داره و امروز با دریافت برگه مجوز خروج راهی ترکیه میشه. طبق شنیده ها قراره اخباری امروز به صورت رسمی معرفی بشه ///قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/136725" target="_blank">📅 15:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136724">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
مشکل رضایت نامه حل شده و قرارداد هم بین طرفین نوشته شده و مشکلی وجود نداره و ظرف چند روز آینده امضا میشه/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/136724" target="_blank">📅 15:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136723">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
آنا : محمدمهدی محبی به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/136723" target="_blank">📅 13:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136722">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
🔴
قدوسی: اخباری زمان خواسته تا بیشتر فکر کنه چون یه پیشنهاد دیگه هم داره و میخواد جایی باشه که بازی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/136722" target="_blank">📅 13:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136721">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⚡️
فوووووووری
💥
💣
اتفاق خاصی رخ ندهد محمد مهدی محبی خرید بعدی ما خواهد بود//طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/136721" target="_blank">📅 13:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136720">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
شنیده می‌شود در صورتی که امیر قلعه‌نویی قول قهرمانی ملی پوشان در جام ملت‌ها را بدهد، در تیم ملی ماندنی خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/136720" target="_blank">📅 13:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136719">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❗️
🚨
فووووووووری از خبرگزاری ایرنا
🚨
پرسپولیس نمیتونه کسری طاهری به خدمت بگیره و تا نیم فصل باید در نساجی بمونه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/136719" target="_blank">📅 12:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136718">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
✅
پنج بازیکن جدید پرسپولیس از نگاه ورزش سه:
⏺
محمدرضا اخباری
⏺
دانیال ایری
🔴
ابوالفضل رزاق پور
⏺
فرهان جعفری
⏺
کسری طاهری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/136718" target="_blank">📅 12:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136717">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
پرسپولیس در انتظار امضای قرارداد ارسال شده برای اخباری
🔴
با توجه به اینکه محمدرضا اخباری در کمتر از 10 درصد مسابقات فصل گذشته برای سپاهان به میدان رفته، سهمیه لیگ برتری محسوب نمی‌شود. / تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/136717" target="_blank">📅 11:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136716">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
✅
طاهرخانی: احتمال داره فردا از محبی رونمایی بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136716" target="_blank">📅 11:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136715">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
✅
پنج بازیکن جدید پرسپولیس از نگاه ورزش سه:
⏺
محمدرضا اخباری
⏺
دانیال ایری
🔴
ابوالفضل رزاق پور
⏺
فرهان جعفری
⏺
کسری طاهری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/136715" target="_blank">📅 11:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136714">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">💥
💥
با جذب محبی و لطیفی‌فر سهمیه‌ی لیگ برتری پرسپولیس تموم میشه ولی قراره یه سهمیه بزرگسال و دو سهمیه زیر ۲۳ سال اضافه کنن تا ایری و طاهری و رزاق‌پور رو هم بتونیم جذب کنیم/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/136714" target="_blank">📅 11:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136713">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
✅
اخباری زمان خواسته تا بیشتر فکر کنه چون یه پیشنهاد دیگه هم داره و میخواد جایی باشه که بازی کنه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/136713" target="_blank">📅 10:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136712">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🚨
باشگاه پرسپولیس قصد داره‌ تا ۲۴ ساعت آینده از چهار خرید جدید خودش رونمایی کنه ///فرهیختگان
🤝
محمدرضا اخباری
🤝
دانیال ایری
🤝
کسری طاهری
🤝
پوریا لطیفی فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/136712" target="_blank">📅 08:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136711">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
❗️
دیشب و بامداد امروز هم حملاتی به کشور عزیزمون نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/136711" target="_blank">📅 08:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136710">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
✅
خبرگزاری تسنیم در واکنش به صحبتهای قلعه نوعی که گفته از خودگذشتگی کردم اومدم تیم ملی تیتر زده که آقای قلعه نوعی میتونه دیگه ایثار نکنه و از تیم ملی بره و برگرده لیگ برتر همونجایی که تو ۱۰ سال گذشته هیچ افتخاری کسب نکرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/136710" target="_blank">📅 08:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136709">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
بعد از 13 شب .دیشب و بامداد امروز هیچ حمله ای به ایران و نقاط ایران از جمله جنوب نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/136709" target="_blank">📅 08:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136708">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATOHHPUbDuJILcHTqe2E2hlwPMxGaWjL7THYp_G0V6sfXoDSFu-MKE4DwOLfJfcdqKMNUZ_Fj2rWs_D8YIkajJKWTCd5TVNM6GK7_zPtE6f5IGkYDEQW2n2OeIoIBJGEX5jeg7Zp57-tpYNUW5blx0bHKLxyiK_0I2B5AnYQZ6TO5E8tCh0qEupZdVvC86GnXfzDax41Zs0jMYF9CN_nC8_Tqfr4_EySyuYlApnRjlt2dq0LbBC63RzHW8HZtDbqdsb_0TmNMDT-bDuwIOiRB8gCc7_5n76lN33Tv-h5Wo1Bi5EvQfRPcgEig6NGJWY5crTqDc8tSLbWFniIYFMi6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/136708" target="_blank">📅 08:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136707">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">درآمد ثابت واقعی میخوای بسم الله
👍
سایت های شرطبندی دنبال ادمین این کانالن ، داره ورشکستشون میکنه
.
😂
👇
JOIN JOIN JOIN
JOIN JOIN JOIN
فقط یک هفته جوین باش میفهمی پول درآوردن چقدر راحته
😍
🤝</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/136707" target="_blank">📅 01:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136706">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i1eKjxm1LlwXBW1kbG2jkHhKuw8oerIVvLWZtL1J5WqsPQAUuVou5qOTGYH20H1B5T38EkVdq0iuU8XDwX4CMsX1gqGbY8PUInXE6KTsUrrUxW2MiBcihPvwiwhUf3qz-0x8x1glc05xeN7mxVUtU4PYnQQ16O9y9roIJrwwynKO0do6iB6JASrUVIrlsAdho3thmzEsuyrU4HTlI7mjf-rvqoejkmj5NR29eneN0mybsFIXHlMUszOYDXK73BVjCqHyv4rp37Ps_zq-de_YihVzSMaSVWV6G6mCHdmluLpZOk2BwNwLlIKcrJNs2Gouw1aPgXgxW8NVmFa6IvDbFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
رفقای بت باز و اونایی که اهل پیش بینی فوتبال هستن از همگی دعوت میکنم این متن رو بخونید
...
🤖
با ربات
هوش مصنوعی
پیش بینی فوتبال ماهانه 30 الی 40 میلیون تومان به جیب بزنید،
کاملا واقعی
🔥
📣
رفقا این ربات طبق آمار و ارقام تیم ها و الگوریتم افت ضریب خیلی راحت بازی های مشکوک به تبانی و فیکس رو پیدا می‌کنه فوق‌العاده پشم ریزونه.
😄
👑
t.me/+bReDKwrhVk5lMmM0
👑
t.me/+bReDKwrhVk5lMmM0</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/136706" target="_blank">📅 01:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136705">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
محمدرضا اخباری در حال حاضر دبی حضور داره و امروز با دریافت برگه مجوز خروج راهی ترکیه میشه. طبق شنیده ها قراره اخباری امروز به صورت رسمی معرفی بشه ///قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/136705" target="_blank">📅 01:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136704">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🎥
⚽️
ویدیو باشگاه از تمرین تیم با کپشن:
😀
از ضربه‌های تمام‌کننده تا واکنش‌های تماشایی؛روزهای پرانرژی پرسپولیس در ارزروم
❌
پ.ن حال پرسپولیس خیلی خوبه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/136704" target="_blank">📅 01:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136703">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
✅
ورزش‌سه: اورونوف، تیکدری، عمری و محمودی اماده‌ترین بازیکنای تمرین دیروز پرسپولیس بودن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/136703" target="_blank">📅 01:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136702">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
فارس: حمید مطهری گفته هیچ جوره نزارید رزاق پور بره پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/136702" target="_blank">📅 01:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136701">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
|
#فوری
🏅
🏅
به گزارش رسانه «سرخ تایمز» باشگاه خیبر خرم آباد طی نامه ای خواهان جذب تیوی بیفوما شده است،اما دو باشگاه تاکنون به توافق نرسیدند.
⭕
🤩
خیبر اعلام کرده از قرارداد ۸۵۰ هزار دلاری بیفوما ۲۵۰ هزار دلارش رو پرداخت میکنه و ۶۰۰ هزار دلار حقوق باقی ماندش رو پرسپولیس پرداخت بکنه اما حدادی به عبدی گفته ما نهایتا ۴۰۰ هزار دلار از حقوق بیفوما رو پرداخت میکنیم، درنهایت اگر اختلاف ۲۰۰ هزار دلاری بین دو باشگاه حل بشه تیوی بیفوما به خیبر خواهد پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/136701" target="_blank">📅 00:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136699">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
تکمیلی :قدوسی : تارتار گفته بیفوما و گرا برن و سرگیف بمونه اما خلیلی میخواد سرگیف ملی پوش رو رد کنه تا گرا و بیفوما بمونن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/136699" target="_blank">📅 23:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136698">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">💥
💥
با جذب محبی و لطیفی‌فر سهمیه‌ی لیگ برتری پرسپولیس تموم میشه ولی قراره یه سهمیه بزرگسال و دو سهمیه زیر ۲۳ سال اضافه کنن تا ایری و طاهری و رزاق‌پور رو هم بتونیم جذب کنیم/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/SorkhTimes/136698" target="_blank">📅 23:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136697">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
از تمرین امروز
👀
💪🏻
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/SorkhTimes/136697" target="_blank">📅 23:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136696">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQhO6mt8LWbGAjSIROf5k-5BAgX1nzE5b1yx_d3kZ83fvpTLnPfveyMVqHvy3uCubkJMMrHro3WyAlkVOzYpluU7jgA3N2JXDZmMV59bvpkpVTbki12MqqXbOSLSfdl5w1yC529UqjIOPP3e0j4WRb4YQ6pO-bl6vw0CdNBz2BNVnKKJtjL2jH2meqQshNWYERyLqdiGzGW9_LSHfDfYo41lSFnZSEIMqaL4l5la0gDqOq6Lm9zjBP7wb_--NW489k9AfNSUxIUxjPs0JmcrCknhewnw9KmITV9H4rZX8bghMw7pEt-HDeAIYyWlAumC1ZkvU4BYBmxyYufPZy-XQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
از تمرین امروز
👀
💪🏻
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/136696" target="_blank">📅 23:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136695">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⬅️
⬅️
⬅️
وای‌نت: اسرائیل خود را برای حمله گسترده آمریکا به ایران در فاصله شب جمعه تا بامداد شنبه آماده کرده بود، اما دونالد ترامپ برای دادن فرصت بیشتر به مذاکرات، این اقدام را به تعویق انداخت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/136695" target="_blank">📅 23:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136694">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✅
🔴
پوریا لطیفی فر ستاره 22 ساله تیم‌گل‌گهر با عقد قرار دادی چهار ساله رسما به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/136694" target="_blank">📅 22:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136693">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
فرزین معامله گری از پرسپولیس جدا شد و در اردوی ترکیه حضور ندارد و شماره بیست پیراهنش هم امسال تو تنه عیدی هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/136693" target="_blank">📅 22:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136692">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
معامله گری که سرباز شده و برای دفاع چپ فقط ی جلالی و داریم و خلاص که اونم مصدوم شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136692" target="_blank">📅 22:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136691">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvzEVfXD8BTG-F7-eEMAkJiCPSFfALIAbAKXHyJER20-1_vsQxHPtp_kKgYLDSNICwWFToXodEXa2nx6Ls3qJ46nEo8gTIBK5dtt6Rbote0D7spOAUXaSSPIwgk2kUIL_lPBWV2iQSBXEYgwcnzg0EfDRZu39Y468wEzigglt4Zb5i2FwjKffIt0rC6u9CwyVgxp6GQFIumZ7DO5xKRp3RP2b2pMu78Heq-FBpGMMA89xg6Ud90Mki1xdv6XjICd0gvNKl30bpyqvQiyjmJpWG4iOEEGlOjoAzS8SymrrAjFf6kaW8oxWC0727t0iV2iFXLx4Ku7wjt0CiX60IogBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
محمد خلیفه، گلر جوان و ملی‌پوش آلومینیوم به استقلال پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/136691" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136690">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
ایگور سرگیف توی تمرینات پیش‌فصل بی‌نظیر بوده و تا الان انتخاب تارتاره برای نوک خط حمله
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/136690" target="_blank">📅 21:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136689">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb0a656a22.mp4?token=JAOZUzTKkrg4yTOgVYEuSSSZR_nQ-gw1Jnb3nEk3CdAC8rwaKchlyF4s0bLRTEr-HusHr09KOlO9HEh2BOJ8XbtavMO_4oLykyaucq_s1H3MKHZEkfnJMBXu69c5JF0BPsqssSatu0fXiRCjmF0ArB4htgutNbMIVRinBk49-AgVnpa0SFP6XUcueNAuZDcA_gU2w1Z45LNl1VKH6l_34KYzwBNrzqckx_Mk1P06xzeigK3nzyCRQjqx8_gA9kdoUYB1eBbIvyKigxC64aAvPyCvm-r2-Nid5jI7YIowxsgf6DVUrZTO2nZ0P6yXLCkuXsIaejZ9izPCNBvnF6u5CgObVn2FsZl51dVKqIOZjGNhap9Xxmvion-tEwAmoInEO58M6ssWP0X8eWpllnpQiNuXDTa501lbLYKqChanCRgsAqaPbF3zWPFzW8N4Bz_S12ahbeZfYyQpJe0yXCkthuTAlxDymRPUE5KNXTS2vUeSQSpTtaFXljLT-DveQGX_Z-qIon9T8xVJ9cA0HdZ8Vg4zOw_tlrXpxV0wjG2fUwDZQ9NJXidyLFm9vA_fbEGzftnqCuGB6gu1lSfpcg8jlfoPWJ2_8CohuDaCG-mSssihBQ98ZzWnsoMo1t2YEHl7VdFuC3cI_Jc0-s7R1_-ddQ2yfuYpuHTZATHS_XMWrjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb0a656a22.mp4?token=JAOZUzTKkrg4yTOgVYEuSSSZR_nQ-gw1Jnb3nEk3CdAC8rwaKchlyF4s0bLRTEr-HusHr09KOlO9HEh2BOJ8XbtavMO_4oLykyaucq_s1H3MKHZEkfnJMBXu69c5JF0BPsqssSatu0fXiRCjmF0ArB4htgutNbMIVRinBk49-AgVnpa0SFP6XUcueNAuZDcA_gU2w1Z45LNl1VKH6l_34KYzwBNrzqckx_Mk1P06xzeigK3nzyCRQjqx8_gA9kdoUYB1eBbIvyKigxC64aAvPyCvm-r2-Nid5jI7YIowxsgf6DVUrZTO2nZ0P6yXLCkuXsIaejZ9izPCNBvnF6u5CgObVn2FsZl51dVKqIOZjGNhap9Xxmvion-tEwAmoInEO58M6ssWP0X8eWpllnpQiNuXDTa501lbLYKqChanCRgsAqaPbF3zWPFzW8N4Bz_S12ahbeZfYyQpJe0yXCkthuTAlxDymRPUE5KNXTS2vUeSQSpTtaFXljLT-DveQGX_Z-qIon9T8xVJ9cA0HdZ8Vg4zOw_tlrXpxV0wjG2fUwDZQ9NJXidyLFm9vA_fbEGzftnqCuGB6gu1lSfpcg8jlfoPWJ2_8CohuDaCG-mSssihBQ98ZzWnsoMo1t2YEHl7VdFuC3cI_Jc0-s7R1_-ddQ2yfuYpuHTZATHS_XMWrjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
⚽️
ویدیو باشگاه از تمرین تیم با کپشن:
😀
از ضربه‌های تمام‌کننده تا واکنش‌های تماشایی؛روزهای پرانرژی پرسپولیس در ارزروم
❌
پ.ن حال پرسپولیس خیلی خوبه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/136689" target="_blank">📅 21:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136688">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
✅
ترامپ قرار بود عملیات گسترده‌ای که راجع بهش صحبت میکرد رو امروز صبح علیه ایران انجام بده ولی لحظه‌ی آخر عملیات رو متوقف کرده تا به ایران یه فرصت مذاکره‌ی دیگه بده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/136688" target="_blank">📅 21:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136687">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
🔴
پوریا لطیفی فر ستاره 22 ساله تیم‌گل‌گهر با عقد قرار دادی چهار ساله رسما به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/136687" target="_blank">📅 21:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136686">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
با اعلام باشگاه پرسپولیس، قرارداد محمدامین کاظمیان با توافق دو طرف فسخ شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/136686" target="_blank">📅 21:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136685">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136685" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/136685" target="_blank">📅 21:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136684">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZvZdJfhxyNzBmRPVabf2vAr5vyaXXEp2AbKiAivr_QSq020uYQARh3VgR7vGi311YyNjxL1tDdoKFkSkdbAFr77zC6cnx0C4rjq4vbz2d62Li4IpW469oJI_-l9KjiIuYJ7aFepMI--713BKfYH89Pif90AsjvbGl25B1NbEZTxwpNGU_r34pClEqk3tgT5J7pfkZeCU_GuDHGMxmCm57EIo8_sNs-ZHwGPIkDQGFAdgXAn_dmClCyMKiuSnEORg1wWN5Ai5QCk8gusAtT5YBvIhpnTQ-iDblWrxu1DBWoNjlAShpsF6vSJRC0Nrt-bQpynr4dOAZQvtpcy4I5bwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هر
چهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
Ⓜ️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/136684" target="_blank">📅 21:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136683">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
🔴
پوریا لطیفی فر ستاره 22 ساله تیم‌گل‌گهر با عقد قرار دادی چهار ساله رسما به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/136683" target="_blank">📅 21:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136682">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWJr0AYtGi7yXwn9RW5dxUnW0nq0pKXYEHjENE4N3oNQotvTtPacwDZpFxbOcVhagz1wOJ5N49g_TA9WC2TPUG7EbqU40UZLTGsz83MwNPWV0Nd6BxqY8yFCMPdT3LTIzSwP8WeinGWTtioUoJOtpWT1y1IbeXBl6xDepvr6tGwwpDJCY6Re_Besdu5GsYWRJTMPeg0YlsBLJRivVIhxIy8fBrO55eEEivMw7cdXqZ7V7ziBgsZLGlTlBa8rHzq8ei1OkAePiFpt5756LZ8caj5gFqes27mP7A803Qg-6VVhuoN8XuDB11OGwXNkBWGxIGWzrmQiQ86yaw67gI-x2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام باشگاه پرسپولیس، قرارداد محمدامین کاظمیان با توافق دو طرف فسخ
شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/136682" target="_blank">📅 21:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136681">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShmOdWLQ1XxYOtZWp_TilILZGtrTQMazYwWJ5s615qris3NHB4Bn8jI5VhnREJBPfPuyGAykC5DqyjYqUlzlUqyT232XoZn4LAK4cBsLEMrf1bMjkZpeHbqOtbtqfAu_YlJb1Ctf7YYQVtpiZra8GDmhqDaeDj0lczsOfGZYVo0bv_KU5u-HSRjCGXv21QxB6uj2f8nNUhkeHL5fuIkHQeRLTuKpf4JReleBjlJCpeokQUKakCGIMxIA-e0iWpHZd53pZUkBXC03arn_9-xx1w13vpt-Vh-LX7uDJftEzl-_j43zBhBrZfz87HK_EEvyUucj9NyLqGUqDaZRooCpsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پوریا لطیفی‌فر با چه آماری به پرسپولیس پیوست؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/136681" target="_blank">📅 21:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136680">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChLrAcMgSjiBqadVxflbmnF9aq4sJJmAFRQsQqIodnkMQ2l0W2-CRVcVtAus1GnFe7a-TfFgZGdUz0t1gConnJnFfIyQ6u_fV7-cyMtrtQAyVKPvD050A5feYQMAab4K7IXvd5UHNjBwzwyA1tCfAtRdUHrcINk9lkkQocIB-vABMfAVbOhTJA_b0vM6VNYNk8E2xLS9canSf26opaechT58GxvElxrB9rSfzVMguovJl-sDKg1x_j2Juo2NC7wgNb0IR8SNqrDIK2NYA6g3_64I9OA2q0a7Dy1glcAzM5fOXGQUKkcQvl5kNF1q-T58OhlnIFDBWR6_gsiPTsZQEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوریا لطیفی فر ستاره 22 ساله تیم‌گل‌گهر با عقد قرار دادی چهار ساله رسما به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/136680" target="_blank">📅 21:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136679">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SulMrBibYFqRa4DWVRcbO0w8EeuCZSuRIoWNVnqFq6xRre-Cbq_0-lc9sCQhxCNufWL-F6tOcnnWtwHMmAJdBwIjHYXHjLKi8tSWKrpxZde0cQ1GrWQVqimClJmifALUYIiYRZsnrkcbRGOYjaUJxJBCSCjRG1rOVMXfg3JQW3MpyaLEuWpsP9WFaVz3Csyi0lPJnsGOEDqbGbgXlUEUq_92UxodqCklH49TV9tx9wEwdDLemUJJeAJd58C6u3biw3Gr1SxiZl3et2bRPq3HBpxGTOV-qQH7_gOMsMm6Uxy3xa6kus93wA4XVadqc-XlH_b5y3kVlSNUpV-uq9ZJQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽
لطیفی فر با عقد قراردادی چهار ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/136679" target="_blank">📅 21:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136678">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
🔴
فوری
🔴
محمدامین کاظمیان از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/136678" target="_blank">📅 20:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136677">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❗️
❗️
با جذب دو بازیکن؛  سهمیه لیگ برتری پرسپولیس پر می‌شود!
🔴
🔴
پرسپولیس  زارع، جلالی، عیدی،  پورعلی،شهرآبادی  و  تیکدری را به خدمت گرفته و در حال نهایی کردن انتقال محمدمهدی محبی و لطیفی‌فر است.
🔴
🔴
در بین خریدها شهرآبادی چون فصل گذشته سهمیه زیر ۲۱ سال گل گهر…</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/136677" target="_blank">📅 20:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136676">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
شایعه: قراره که امشب حدود ساعت 23:00 محمد محبی قراردادش رو با پرسپولیس امضا کنه و رسما پرسپولیسی بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/136676" target="_blank">📅 20:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136675">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
فوری/ ترامپ: مهمات برای یک حمله بزرگ به ایران آماده شده. سران ایران که خطرناک‌ترین آدم های جهان هستن باید تصمیم‌گیری کنن. شاید تسلیم بشن، شاید هم بزن تو غار قایم بشن. چون تو ایران غارهای بزرگی هست! ایران شروع کرد کل خاورمیانه رو زد. اگه بمب هسته‌ای داشت،…</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/136675" target="_blank">📅 19:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136674">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
۳ خرید ناب در راه پرسپولیس
💥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/136674" target="_blank">📅 19:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136673">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjNGkoM4IW1SOU4agk8EhR1mY0zGaw21xwloAPcHmpALN3AeK5c2sutk2im7PYeO2sny0IVDySHvkjjJJRpACu9tGGzE-mWhyhuKN4AjT_Yf9z_IJ3t6REx4PJqxNl88jfoir7U6C5JZdsYuFTzET44t4QP-7Wa9hdLiBFqcfupLZQ-LQc7TSmyjSVqxYkYCnkug6_LdKzN8EmmSHBw7Eexe6ID1Qp3qJilklyLiY2wnjMpb08yMeVEgKJ97XTv1r1w8PdvfECT-tpkmhlUVFcMVVFJrI3379EnWvznAbqEty7AzslhJSi2c4f6RTVdB62kq36G4GttOYTN1Ct6aDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ایگور سرگیف توی تمرینات پیش‌فصل بی‌نظیر بوده و تا الان انتخاب تارتاره برای نوک خط حمله
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/136673" target="_blank">📅 19:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136672">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">💥
💥
شماره جدید بازیکنان پرسپولیس در فصل آینده مشخص شد
🔴
محمد مهدی زارع ؛ شماره 4
🔴
محمد عمری ؛ شماره 7
🔴
مهدی تیکدری ؛ شماره 8
🔴
ایگور سرگیف ؛ شماره 11
🔴
یعغوب براجعه ؛ شماره 13
🔴
پوریا شهرآبادی ؛ شماره 17
🔴
امیرحسین محمودی ؛ شماره 19
🔴
مجید عیدی ؛ شماره‌ 20
🔴
ابوالفضل…</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/136672" target="_blank">📅 18:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136671">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❗️
❗️
سایت طرفداری: استقلال نزدیک به ۱۰ هزار میلیارد بدهی بالا آورده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/136671" target="_blank">📅 18:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136670">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
قدوسی: محسن خلیلی میخواد بعد از جذب کسری طاهری قرارداد ایگور سرگیف رو فسخ کنه . تارتار تاکید ویژه ای کرده که سرگیف رو میخواد اما خلیلی میخواد سرگیف بره تا گرا بمونه
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136670" target="_blank">📅 18:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136669">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
❗️
شهاب زندی مدیرعامل نساجی :
❌
❌
آقای خلیلی میگه کسری طاهری رو نمیخواستیم و گرون بود، اصلا قرار نبود برای کسری پول بدن، اصلا ما نمیتونستیم کسری طاهری رو بفروشیم، ما خودمون کسری طاهری رو خریده بودیم و ثبت کرده بودیم
✅
✅
هوادارای عزیز، مردم، مسئولین و همه سازمان…</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/136669" target="_blank">📅 18:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136668">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
۳ خرید ناب در راه پرسپولیس
💥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/136668" target="_blank">📅 18:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136667">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✅
✅
محمدامین کاظمیان بخشی از قرارداد توافق پرسپولیس با گلگهر برای جذب پوریا لطیفی فر می‌باشد
🔹
محمدامین کاظمیان + حدود ۸۰ میلیارد رضایت نامه = پوریا لطیفی فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/136667" target="_blank">📅 18:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136666">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
باشگاه استقلال پیشنهاد 5 میلیون دلاری آسانی رو قبول کرد و این بازیکن شنبه به ایران برمیگرده !!!
😕
😕
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/136666" target="_blank">📅 18:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136665">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
در شرایطی که قرار بود امروز بازی پلی اف لیگ برتر بین مس رفسنجان و صنعت نفت برگزار بشه.. تیم مس تو زمین حاضر نشده و آبادانیا جشن صعود به لیگ برتر گرفتن
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/136665" target="_blank">📅 16:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136664">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
تارتار اسم یه مهاجم خارجی رو به باشگاه داده و درصورت جدایی بیفوما و گرا مدیریت برای جذبش اقدام میکنه/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136664" target="_blank">📅 16:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136663">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❗️
❗️
خطر رفع شد؛ به ادعای ورزش سه زکی‌پور ۲ ساله با تراکتور بست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/136663" target="_blank">📅 16:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136662">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
دنیل گرا و تیوی بیفوما هم توی اردوی ترکیه کنار پرسپولیس هستن.
❗️
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/136662" target="_blank">📅 16:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136661">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
۳ خرید ناب در راه پرسپولیس
💥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/136661" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136660">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⚠️
⚠️
تیم فوتبال پرسپولیس در اردوی ترکیه با فنرباغچه که هدایت آن برعهده اسماعیل کارتال است، یک دوستانه بازی برگزار خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/136660" target="_blank">📅 16:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136659">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
پناه بگیرید
✅
میلاد زکی‌پور رسما از سپاهان جدا شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/136659" target="_blank">📅 14:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136658">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔹
نگاهی بندازیم به هایلایت‌ پوریا لطیفی‌فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/136658" target="_blank">📅 14:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136657">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❗️
میلاد زکی پور، مدافع چپ سپاهان پس از قرار گرفتن در لیست خروج محرم نویدکیا، به پرسپولیس معرفی شده تا جانشین میلاد محمدی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/136657" target="_blank">📅 14:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136656">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLpOjqRLCLCvLoJbTLLoztYS5s3fzeCnbwhlr2q3kkPuE3F8S5v2Q_RV7yJfBZxGYTMB5QsdBAg_iTp18J-CSgg6PnWd5tVNWLj-1flhVTLXYs0zVkgLku1ZPt7NBCW09XlwY8m_ls9VSMsfUyq5jRPmzX24r7SkhVKvX6NmHtWYBCn7T-yVTCNlOPV-dsMWKji0Q7sFsgQjYLV-vs9WijxMAiqpy5ZzZiAZWzvBQnLaFRHn_hskMObKP1vZJ5rLb8lEd7ghgGiMC1WKGun-znf3Q0Or0dyV5Z2xuhrBJ9Ryerh3ynE2IqzPHV1eTwyxOpTV11JM7BKPT-zoV0fOIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽
لطیفی فر با عقد قراردادی چهار ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/136656" target="_blank">📅 14:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136655">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4oSX9Ojy6YiGVMw77O6Fe5MpU-w50MaWH8l6K70nuL_9saJw9RUZjvcwAwZ1cTWaQlrCZamP6r0zA2VQ712eqHKPjDp139F-XT1dbPaXhta1BrUYTi7VMRZxNlaQGnWjLqGEr6m02VKgdjOhdK8_eohep0tEBGlA5y_pkqHhQM3zt9OmCHMEkhovgT6sji1aIYD_E3sg9wYTVIsPgo7g7mWLRYY5eLTEgFW58D-nXd5OFKzSncsbSiAPmcp7TXdWoKOcPYw53D7G8EWcijtVYUf1M2ItI21F214lK9W5c914n96hk0-8CzIn2nrmfy18bPypL7gA7pIC5lZeiLe3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
۳ خرید ناب در راه پرسپولیس
💥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/136655" target="_blank">📅 14:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136654">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuAoCL_E7Q3DXt2wq_N45kXh5ICqhENa3q4-xgRD0nzC2Ih6gj52oW-S0cuBZ39Q94TmGS3e-LlE-AR8s_a4C1cbs-L2Cq3bKJ50A6CoA6ipTYhIMjlXNBHHgHrccmj1WvDzdsdrt4RLSc0Wr9DYepkJAmQa0Ndp6-VCALqnRRlhQ4weGLiwlgyBTi1jnKLac8cuMMrhGaq25PmUpPTj2hh9EC7ISGWeLbJyVxQr1F5vd0_renc1ObV8E_XS0iYz4eiaqK_Y74omlEQrk4HWCY-l_Rrg3TE7IjRdaqa2xfhrdX3hzzgG_t3-JhiEYx9VL8d8Kn-ouxv9048DebsIxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مدیر رسانه‌ای جدید پرسپولیس انتخاب شد
❗️
❗️
فربد بقایی مدیر رسانه‌ای سابق چادرملو و ساپیا جانشین روزخوش شد.
🔴
🔴
بقایی حدود ۱۰ سال قبل در سایپا فعالیت داشته و فصل گذشته در باشگاه چادرملو مشغول به کار بود.
🔴
🔴
خبر انتصاب بقایی طی امروز یا فردا از رسانه باشگاه منتشر خواهد شد و بزودی او راهی اردوی ترکیه می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/136654" target="_blank">📅 14:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136653">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
پیروز قربانی: من نیوزلند رو با فجر سپاسی شیراز می‌بردم مطمئن باشید نیوزلند اگه تو لیگ 16 تیمی ما بود، جزو چهار تیم آخر میشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/136653" target="_blank">📅 13:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136652">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❗️
واکنش ابوالفضل رزاق‌پور به پیشنهاد پرسپولیس:
🔴
نامه رسمی به باشگاه فولاد آمده ولی من وظیفه دارم سر تمرین بیایم تا تکلیف مشخص شود. خودم با باشگاه هیچ حرفی نزدم و دو باشگاه باید باهم حرف بزنند.
🔴
🔴
حضورم در پرسپولیس برای دعوتم به تیم ملی تأثیر دارد ولی امیدوارم…</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/136652" target="_blank">📅 13:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136651">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❗️
مشکل سربازی فرهان جعفری حل بشه با قراردادی ۴ ساله پرسپولیسی میشه/طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/136651" target="_blank">📅 13:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136650">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">#تکمیلی
⚽
💥
حدادی منتظر پاسخ محمد مهدی محبی؛توافق با کلبا انجام شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/136650" target="_blank">📅 13:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136647">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
💣
One Signature. One Earthquake…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/136647" target="_blank">📅 13:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136646">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🤩
باشگاه پرسپولیس فردا در دیداری تدارکاتی به مصاف پیرامیدز مصر خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/136646" target="_blank">📅 13:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136645">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
⚽
لطیفی فر با عقد قراردادی چهار ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/136645" target="_blank">📅 13:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136644">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hk3AxxPBl03oVG6KlZZyoTwxxGwpo55OkLL_pJ3L26pvegt_hsw9SaUqTyJR5UvYM1q_dDWu0-bL-RkxlXJyyAn0cphp2mHWtLqe2DQ_UZDalDUQ3XOJBOMqC4Ayqs76NQ3jZ9NhxF29gogtBguTQwXgnYWGoFvg_74In6dqgLjf07Q9-egqKnfq2n_H8sjfm1ur86hxc94yk2K2fEGcsshpvkxHOByxiGvEoq3W529OkfH_67ZJkbqZB6oA2MwBKBPcijLgnbCfiol5ECmzYGTucUvHPfBehi1jj0-H14PMLqisZ8-iVWMGePF0CpMl0v6L7bcQMBCgwpEfa3sCnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽
لطیفی فر با عقد قراردادی چهار ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/136644" target="_blank">📅 13:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136642">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/136642" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136641">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/136641" target="_blank">📅 12:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136640">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
امروز تکلیف نهایی دانیال ایری و کسری طاهری برای پیوستن به پرسپولیس مشخص خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/SorkhTimes/136640" target="_blank">📅 11:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136639">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
بعد از 13 شب .دیشب و بامداد امروز هیچ حمله ای به ایران و نقاط ایران از جمله جنوب نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/136639" target="_blank">📅 11:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136638">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
🚨
باشگاه پرسپولیس قصد داره‌ تا ۲۴ ساعت آینده از چهار خرید جدید خودش رونمایی کنه ///فرهیختگان
🤝
محمدرضا اخباری
🤝
دانیال ایری
🤝
کسری طاهری
🤝
پوریا لطیفی فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/136638" target="_blank">📅 11:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136637">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
برخلاف شایعات ؛ حضور براجعه در تصاویر اولین تمرین پرسپولیس در ترکیه
❌
در حالی برخی منابع از عدم حضور براجعه در اردوی ترکیه پرسپولیس خبر داده اند که این باریکن در تصاویر اولین تمرین سرخپوشان در ترکیه حضور دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/136637" target="_blank">📅 11:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136636">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
🚨
🚨
باشگاه پرسپولیس با باشگاه اتحاد الکبا برای انتقال محمدمهدی محبی به توافق رسید  #قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/136636" target="_blank">📅 09:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136635">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ga82mPV77sN6UcOXX7jFt-Hztpsvd9cDu-32OwzUKNvmyggyr401rS-FZJ3rm4CFZTAANmKFCZzzT3coCbz3Akt2QMs7V3Ts25fTtcjxG5LP39q2Xy10hg4sevsKNtVkThF-iNub2mZG2KU01Gccj_Quy1M9ZjGilysoGwyF_XOL2RvLRkP1lwg4YR0P7hnCaVeUkSN818uu8ucH5I9scn0k1ryzkar5IJRipWFFBcWC9hpMvDMxrnY9uaukqtf8ZRFW1fltjCTDxU4N3LjB5UcNYI6yDZ_YmIx4Ot-UOR9qCZvVHmuVazvFZ9dS2LZFCe8VT5ZGS-D50mU3S1dHfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف شایعات ؛ حضور براجعه در تصاویر اولین تمرین پرسپولیس در ترکیه
❌
در حالی برخی منابع از عدم حضور براجعه در اردوی ترکیه پرسپولیس خبر داده اند که این باریکن در تصاویر اولین تمرین سرخپوشان در ترکیه حضور دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136635" target="_blank">📅 09:33 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
