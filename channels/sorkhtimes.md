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
<img src="https://cdn4.telesco.pe/file/pF06wY8Xanbe_1IQVyqW59hXFcK5SXkZKfqQWopjYpZV0M7awkWMykDoLDEZqIDTE8gyfQd4tDedFkNG0Sw7k5UXTBaUW4z8HIc7v93nJwN_lPlz3qrOmBgKLgIy8QIIrL0_cpUPI-IGJb52SHsUpu2cYaZhO7XSnNSwJOYVRrHbkbbdblAVb8XhVSPKQfOZ62nz3nvqv5kAKM7nKLb6b4tz6pu18FcP2mXhLD_d7c7rcZqtVI6KOzN7QDjqOILv67e23uexEdwxILLCC35EXKJoVyJXOlv3frNpYoDKa2Tdf3e8L3ljSyDOc5B9I5neluePyzzgXTovhSsC_V3R4A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 14:57:31</div>
<hr>

<div class="tg-post" id="msg-136110">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/136110" target="_blank">📅 14:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136109">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/136109" target="_blank">📅 14:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136108">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
ورزش سه: بازوبند کاپیتانی پرسپولیس مدعی سومی هم داره و اون کسی نیست جز احمد نوراللهی که در آستانه بازگشت به پرسپولیس قرار داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/SorkhTimes/136108" target="_blank">📅 14:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136107">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔹
ممکن است دنیل گرا و تیوی بیفوما در پرسپولیس ماندنی شوند!
🗣
گرا در پست دفاع چپ و هافبک دفاعی تست شده
🔹
بیفوما هم حاضر به فسخ نیست و شاید تا آخر فصل بمونه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/SorkhTimes/136107" target="_blank">📅 14:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136106">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
شهریار مغانلو مهاجم سابق‌تیم اتحادکلبا با عقد قرار دادی به مدت 2+2 سال به تراکتور پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/SorkhTimes/136106" target="_blank">📅 14:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136105">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
شهریار مغانلو به تراکتور پیوست
🚩
خط حمله تراکتور برای فصل بعد ؛
🔖
هاشم نژاد
🔖
ترابی
🔖
حسین زاده
🔖
اشترکالی
🔖
مغانلو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SorkhTimes/136105" target="_blank">📅 14:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136104">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❗️
❗️
شهریار مغانلو با باشگاه تراکتور به توافق رسید./ ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/136104" target="_blank">📅 13:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136103">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
طبق گفته شهاب زندی مدیرعامل نساجی هم دانیال ایری هم کسری طاهری مشکلی برای پیوستن به پرسپولیس ندارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/136103" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136102">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
✅
پیام گلر یک پرسپولیس و ۹۹درصد گلر یک ایران در جام ملت‌ها است. برای چی باید اخباری جذب بشه که خودش رو در سطح گلر یک می‌دونه؟ که چی بشه؟
❌
❌
ضمن اینکه امیر رفیعی هم گلر مطمئنیه. چرا باید الکی چالش درست کنیم توی پستی که اصلا مشکل نداریم!!! به فرض جدایی رفیعی…</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/136102" target="_blank">📅 13:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136101">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
✅
پیام گلر یک پرسپولیس و ۹۹درصد گلر یک ایران در جام ملت‌ها است. برای چی باید اخباری جذب بشه که خودش رو در سطح گلر یک می‌دونه؟ که چی بشه؟
❌
❌
ضمن اینکه امیر رفیعی هم گلر مطمئنیه. چرا باید الکی چالش درست کنیم توی پستی که اصلا مشکل نداریم!!! به فرض جدایی رفیعی…</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/136101" target="_blank">📅 13:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136100">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
بمب پرسپولیس در آستانه انفجار؛احمد نوراللهی به تهران بازمی‌گردد/طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/136100" target="_blank">📅 12:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136099">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">💢
کاظمیان + رفیعی میرن گل‌گهر پوریا لطیفی فر میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/136099" target="_blank">📅 12:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136098">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
تمام راه‌های ارتباطی به جنوب، فرودگاه، پل‌ها، راه آهن و... دارن دونه دونه نابود میشن! آمریکا بدون هدف کاریو نمی کنه. یه سناریو بزرگ و احتمالا حمله زمینی پشتشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/136098" target="_blank">📅 11:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136097">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qT4xLBzMkU50wlOJohLh-0VUPAO8LpFplRGl1za4g6LyuP2ot9FsKtE1Abwd2DDmoRcvVQ_sev-SFUyeUh_ELQWtrMkxNCdC-YvkmeyFTIBe2pTpiGh-NwekWzVreJvrBv7RMv8tpgRlfsusyNGQuTlE9fk58AUq_E0niU1_3pPwTxyKGdzQdMhupLq0WrB_1rcozfEHW9HR-AIuUfEcJmJ6wN2ycb03BFvnoj21OfGHlyaUEnfco1j-nwhMbXYSVFkXMNil-kjUVf530beq-XWfi5l59dM1j1TXgD2kxDx59uB1Wkb9EEXB1ltU4nZFgIZma5ZqTHI4f_Ti8KRyYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☹️
تصاویر آب‌شیرین‌كن تخریب شده بونجی جاسك پس از حملات دشمن جنایتکار آمریکایی / ۲۰ روستا با جمعیت ۱۰ هزار نفری بی‌آب شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/136097" target="_blank">📅 11:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136096">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
✅
باشگاه سه گزینه برای دروزاه بان داره  ○ اخباری ○ گوهری ○ دیناروند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/136096" target="_blank">📅 11:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136095">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
ترکیب پرسپولیس تو بازی دوستانه امروز
▪️
پیام نیازمند
▪️
حسین ابرقویی
▪️
حسین کنعانی
▪️
ابوالفضل جلالی
▪️
مجید عیدی
▪️
محمد خدابنده‌لو
▪️
مارکو باکیچ
▪️
مهدی تیکدری
▪️
محمد عمری
▪️
امیرحسین محمودی
▪️
محمد امین کاظمیان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/136095" target="_blank">📅 11:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136094">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
برگام
🚨
فرهیختگان: کسری طاهری به نساجی مازندران پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/136094" target="_blank">📅 10:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136093">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
شنیده ها: میلاد محمدی برای تمدید قرارداد با مبلغ ۷۹ میلیارد تومن (سقف ملی پوش ها) به توافق رسید
❌
محمدی اما اعلام کرده پیش از امضا مطالبات فصل گذشته اش را میخواهد و باشگاه اعلام کرده پس از تمدید قرارداد واریز خواهد کرد! و این موضوع باعث چالش بین طرفین شده…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/136093" target="_blank">📅 10:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136092">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
🔴
مشکلات قلبی محمد عباس‌زاده و خداحافظی او از فوتبال  محمد عباس زاده روزهای عجیبی را در زندگی خود سپری می‌کند و حالا رسما فوتبال او تمام شده است. مهاجمی که سال‌ها با تعصب و جنگندگی‌اش در خط حمله، لرزه بر تن مدافعان لیگ برتر می‌انداخت، با تشخیص قطعی پزشکان…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/136092" target="_blank">📅 09:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136091">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
پهلوان علی آقا دایی خط قرمز مردم ایران است
❤️
🔴
با قلب قرمز به این پست تایید کنید
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/136091" target="_blank">📅 09:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136090">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbL2JFSkuPnKCxNSEiB7m-vN9XQuNYH0ky9E41vtCeaxrMOGv4lMDihUyd_Q_oC0ExhHPpySwJw5ONXSfUeuZEi7GwHPbThEd1mn_Bux6cI7PaRaqp4_wWniSRkENCpvKXQFjpxmgw2wg0QKUjCbBljJxeyLm7kD7dj1lwt2K6uxI45GVWGH_vA48mx8xLRLhVKbFjEjXhckOxat0W-itLSPpHP_FB6JfMZ8L48bFg-HYSAQaqXnLyPtXcla0_QF-Os_Kkeus8XyF3f-BL9sGsVKZvsyWI9LLKr2_ZCx057HOVlmymbaI1myEuv-p3gHEj0CqX_Joy288oRIKNtnKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پهلوان علی آقا دایی خط قرمز مردم ایران است
❤️
🔴
با قلب قرمز به این پست تایید کنید
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/136090" target="_blank">📅 09:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136089">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
✅
یک مازاد دیگر در راه است
🔴
تارتار که از وضعیت فنی چند نفر راضی نیست احتمالا بزودی یکی دو نفر دیگر را در لیست خروج می گذارد.یکی از آنها فعلا به سمت پشت دروازه رهنمون شده و احتمال دارد، کادرفنی اعلام کند به این بازیکن که نتوانسته خودش را در تیم اثبات کند،…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/136089" target="_blank">📅 09:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136088">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❗️
کریاکو یاگو، مربی یونانی و جدید بدنساز تیم فوتبال پرسپولیس که با انتخاب مهدی تارتار به باشگاه معرفی شده بود، امروز پنج شنبه وارد ایران شد و مورد استقبال نماینده باشگاه قرار گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/136088" target="_blank">📅 09:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136087">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
چند مسیر اصلی در استان هرمزگان بدلیل حملات و بمباران‌های دقایقی‌پیش مسدود شد
❌
پل محور رفت در مسیر سه‌راهی میناب به سمت رودان، پس از دوراهی سرز
❌
پل «شور»
❌
تونل شهید میرزایی در محور بندرعباس ـ حاجی‌آباد در هر دو مسیر رفت و برگشت
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/136087" target="_blank">📅 08:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136086">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
✅
یک مازاد دیگر در راه است
🔴
تارتار که از وضعیت فنی چند نفر راضی نیست احتمالا بزودی یکی دو نفر دیگر را در لیست خروج می گذارد.یکی از آنها فعلا به سمت پشت دروازه رهنمون شده و احتمال دارد، کادرفنی اعلام کند به این بازیکن که نتوانسته خودش را در تیم اثبات کند،…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/136086" target="_blank">📅 08:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136085">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
🔹
تارتار کاظمیان رو گذاشت لیست مازاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/136085" target="_blank">📅 08:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136084">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
فوووووووری
🔴
🔴
شهاب زندی: من به سرتیپ طاهری پدر کسری عزیز و خود کسری برادر کوچک تر من قول دادم بره پرسپولیس اما مدیران پرسپولیس به دروغ میگن گرونه. برای زارع تو ۵۰ تا تیم ملی نیست ۱۸۰ تا دادن اما برای کسی که ۲۳ تا تیم ملی مبلغ خیلی کمتر از این نمیدن
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/136084" target="_blank">📅 08:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136082">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8WueIHIUZl7nhrb6kaAfbpkbLULMfX2wVXDkHWQPOuiorqAd8zOqEUyaD1Qiv_x5scAfsRJgFUHPvox48Ie1MleDOWgMiEyWTNgz0dopMp0i-53XFOsS7grdoObdLrdT0CTG40CE2lKfHxoZvUxE0nkqabSKV5nI2CHvqt07hT8JOX4Bua4oNG934JKC3r2-vwlQpsg2Z3UzFquNqqVejszMnvsR48xgq1x6gG5cG1zJfE9SL__aErJMJtH5KbneMXSHvnGPMwh9ddvzNRIQ-W1mYAoW1QErhQ7uAZKbB5-1BZ5AnOTqocucY4rON9aa_Px-kCLpkwH7yNxQP5uJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a229bafa39.mp4?token=jOXDFe2hrZx3Osi-bbPb5FnR9BVFyR_LK1rDESeauQxNtY-RdZIJJemZkPrO-29oxMCuoRUlE77ZvjR169IaLziQcBgVO5ICcmTjpoFVZRXq8LKJ-io4db3H-BQ1j9CqxOrnwU3YldBirpmZjIxAsoGtxWaewmndTA31uMv9ytRvHlvEitfRkN3eGQvgG1VpPZwXDFPsnlzgtop6A5J8dn2b6MGPQWkPwAu-w7_6-Ijhak9XV62ZCXKPQgJAMcNECY0bE75mVQHzyKP_tR25CF4mWcIGPGcDK7gvrcxpOsfndxAnr3y4g2zjgjyBCW_q2vlvJvBFtKOkG7rt6AGgNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a229bafa39.mp4?token=jOXDFe2hrZx3Osi-bbPb5FnR9BVFyR_LK1rDESeauQxNtY-RdZIJJemZkPrO-29oxMCuoRUlE77ZvjR169IaLziQcBgVO5ICcmTjpoFVZRXq8LKJ-io4db3H-BQ1j9CqxOrnwU3YldBirpmZjIxAsoGtxWaewmndTA31uMv9ytRvHlvEitfRkN3eGQvgG1VpPZwXDFPsnlzgtop6A5J8dn2b6MGPQWkPwAu-w7_6-Ijhak9XV62ZCXKPQgJAMcNECY0bE75mVQHzyKP_tR25CF4mWcIGPGcDK7gvrcxpOsfndxAnr3y4g2zjgjyBCW_q2vlvJvBFtKOkG7rt6AGgNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📌
حمله شب گذشته آمریکایی ها به پل سه‌راه‌ میناب به‌سمت رودان
🫦
پ.ن: کمک های ترامپ به مردم ایران…همونطور که میبینید کمک از راه رسید،یه عده واقعا گاون توهین به گاوه بی رگ های وطن فروش،وایسید عمو ترامپ براتون برینه وقتی نمیتونید مسائل رو از هم تفکیک کنید میشه این
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/136082" target="_blank">📅 08:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136081">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
❌
فوووووووووووری
😀
کانال 14 اسراییل: پل و راه اهن و فرودگاه و پادگان ها در جنوب ایران بمباران میشوند تا جنوب تسخیر شود. بزودی نیروهای امریکا وارد ایران میشوند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/136081" target="_blank">📅 08:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136080">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E74Bs1sG4rzZ_9vJkKR-7Qt-S8QmncFSfKY_HGx7BLdaKqC8GsWcAhPpMQQQq-nXHBFfxJ3BHdCx7r-4NFYpyo-SPGhkKrDi3jDpSrpkwRi0O9dM1AhQXjMWJ9Z-MWrCLAqA9x-ogmnK_Wp4xVfAxszH5cAmeiNMUlcg12EaAXATrUzAJTY0m5OTc2Ri-AxfxLZJNscY7p-xomMD7VbRtA8XY5YRXoP2dSemhTYLf3TV6dIkMoZ6pflWyKWAzbhSV2VMCjbw-k7NbKVuqrXvmeO8O9TlJDWzxE5mnYw0OCaP1e3O1_PefDAMZckfOG6mtILf2o84pwLYgzP347cmHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرسپولیس ممکنه زندگی نده، ولی
شادی میده
عشق میده
اینه داستان سرخ...
❤️
‌
سلام صبح بخیر پرسپولیسیها؛
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/136080" target="_blank">📅 08:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136079">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136079" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://telegram.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/136079" target="_blank">📅 02:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136078">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3dHrBK-epXlS7xTVtXRfsZ9B9NS_yKREqeUNUgSisSyAxrXHvNYtBoC0Fg3uBr1DmzQPnQO2Y_zGRYWFWowbQqB9UzopbFOo3XNoSG_ueWBr3ibzsxdHCYeMlribq3o_qDN47GyZSrRfYqKJOYmnQENRgoypx3Yw8SSCExHYJX_ta2hNj1jdmo2BaplurL8vstw3M8TjQqYTFm3E6Xt5BXWwB_e--kfFOIftIzxONX1M0m35nhuS5UU9TRqN5XB7Hs8nz8mFF3F39JDOpn0Qz4hpwQ9MwBFlX_ZnB2txcEU4nQq8qJQWPAIqJUNw7z7FCe6ePPJ0vcxxMxaUT4eYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به دنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
🌍
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://telegram.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
Ⓜ️
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/136078" target="_blank">📅 02:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136077">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمهدی</strong></div>
<div class="tg-text">متاسفانه تابستونا دبستان تعطیل میشه هرکی میرسه از ادمین انتقاد میکنه .
اطلا متوجه میشین چی شده؟
🤣</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/136077" target="_blank">📅 02:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136076">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">این اسمش توش کنیه
ما کیسه نیستیم</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/136076" target="_blank">📅 01:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136075">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMehdihormozi</strong></div>
<div class="tg-text">اینا خرید که گرونتر بده به پرسپولیس دم مدیران پرسپولیس گرم دستش را خواندند به بازیکنان قول هم داده شما را می‌فرستم پرسپولیس حالا مونده چکار کنه</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/136075" target="_blank">📅 01:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136074">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❗️
شهاب زندی: آقای تارتار رفیقمه آدم سالمیه. آقای حدادی آدم سالمیه اما برخی در باشگاه پرسپولیس مانع انتقال دو ستاره ما به پرسپولیس شده اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/136074" target="_blank">📅 01:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136073">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
فوووووووری
🔴
🔴
شهاب زندی: من به سرتیپ طاهری پدر کسری عزیز و خود کسری برادر کوچک تر من قول دادم بره پرسپولیس اما مدیران پرسپولیس به دروغ میگن گرونه. برای زارع تو ۵۰ تا تیم ملی نیست ۱۸۰ تا دادن اما برای کسی که ۲۳ تا تیم ملی مبلغ خیلی کمتر از این نمیدن
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/136073" target="_blank">📅 01:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136072">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✅
✅
نیمه شب امشب صدای پنج انفجار در برخی مناطق حاشیه‌ای شهر یزد شنیده شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/136072" target="_blank">📅 01:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136071">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✅
✅
نیمه شب امشب صدای پنج انفجار در برخی مناطق حاشیه‌ای شهر یزد شنیده شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/136071" target="_blank">📅 01:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136070">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✅
فوری/ سنت‌کام:
❌
دور جدید حملات از الان شروع شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/136070" target="_blank">📅 01:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136069">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✅
✅
شهاب زندی: هواداران عزیز پرسپولیس، با همون مبلغی که کسری رو خریدیم میخوایم به پرسپولیس بفروشیم اما مدیران تون میگن نه
😐
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/136069" target="_blank">📅 00:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136068">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❗️
❗️
شهاب زندی مدیرعامل نساجی :
❌
❌
آقای خلیلی میگه کسری طاهری رو نمیخواستیم و گرون بود، اصلا قرار نبود برای کسری پول بدن، اصلا ما نمیتونستیم کسری طاهری رو بفروشیم، ما خودمون کسری طاهری رو خریده بودیم و ثبت کرده بودیم
✅
✅
هوادارای عزیز، مردم، مسئولین و همه سازمان…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/136068" target="_blank">📅 00:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136067">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
✅
شهاب زندی: هواداران عزیز پرسپولیس، با همون مبلغی که کسری رو خریدیم میخوایم به پرسپولیس بفروشیم اما مدیران تون میگن نه
😐
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/136067" target="_blank">📅 00:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136066">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZx3BCz1hbWO1Rhq4yKntrk2hX5QFWxXFwacJKL5A9kiBUrRR9pcaqEX53t83Y4CjD5refx-UcXSAjtH5dxwYfqM74ZIpSMNSeqruLxpFT4AZYNjCkIql_HkhyVSbgLzRwVJFwiHEzS1fIIxhHuBYpoOlzGD3rDl8VzThzSzDOg-RmYt_QB7iaDVAmL7cCHT5pZ4NPcl5gHkkBMnmzeslMoVVp7gqK9vqKRskwleankuHAg6oiVh77qeD13OE4zPiydDUZnzgyCylelufwi9WYHn5Gb9za8GIPJzgZlKsnvn3XGFkWVZALETflyhFBvEKuyIT_vAjULPdeO5dh7BKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
محمدحسین صادقی در تمرین امروز پرسپولیس حضور داشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/136066" target="_blank">📅 00:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136065">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
✅
شهاب زندی: هواداران عزیز پرسپولیس، با همون مبلغی که کسری رو خریدیم میخوایم به پرسپولیس بفروشیم اما مدیران تون میگن نه
😐
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/136065" target="_blank">📅 00:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136064">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❗️
شهاب زندی: پرسپولیس برای زارع که تو ۵۰ تا تیم ملی نبوده یک میلیون دلار پول داده اما برای دو ملی پوش ما میگه گرونه مقصر من نیستم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/136064" target="_blank">📅 00:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136063">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✅
✅
شهاب زندی: هواداران عزیز پرسپولیس، با همون مبلغی که کسری رو خریدیم میخوایم به پرسپولیس بفروشیم اما مدیران تون میگن نه
😐
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/136063" target="_blank">📅 00:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136062">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❗️
❗️
شهاب زندی مدیرعامل نساجی :
❌
❌
آقای خلیلی میگه کسری طاهری رو نمیخواستیم و گرون بود، اصلا قرار نبود برای کسری پول بدن، اصلا ما نمیتونستیم کسری طاهری رو بفروشیم، ما خودمون کسری طاهری رو خریده بودیم و ثبت کرده بودیم
✅
✅
هوادارای عزیز، مردم، مسئولین و همه سازمان…</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/136062" target="_blank">📅 00:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136061">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95f0e3225.mp4?token=koRNEPMp3uEKlv-CmKE3R3QdYGOT7OINzFyPEgL1FZrchdslhCTyPV9plK0kR7jwJBvNPORp7cin8dyJSP-pDya9ypFmNJ52bfdMdMk3WdfperyUdn2Tap75OBpixQFKNIQoB5I6TaTB7qTVjXdzbvMur-ZPA4sBHggcOVNhLosWCzrKYy0NUywOAk7Kvu5AhY2D55zZ6Jbu-2GySbLZ54-0KVydkKmUsdcpXhfidCYfs66CPxi6gmqKq73zw1H05ZvVUBF9fNrnpbfh92ddbgQkhKNfWYJO6Sk3MDZVyE2h0ryV2ppgxTIjIr2kVxVJImx8cIomQxhW-mLVwjX8-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95f0e3225.mp4?token=koRNEPMp3uEKlv-CmKE3R3QdYGOT7OINzFyPEgL1FZrchdslhCTyPV9plK0kR7jwJBvNPORp7cin8dyJSP-pDya9ypFmNJ52bfdMdMk3WdfperyUdn2Tap75OBpixQFKNIQoB5I6TaTB7qTVjXdzbvMur-ZPA4sBHggcOVNhLosWCzrKYy0NUywOAk7Kvu5AhY2D55zZ6Jbu-2GySbLZ54-0KVydkKmUsdcpXhfidCYfs66CPxi6gmqKq73zw1H05ZvVUBF9fNrnpbfh92ddbgQkhKNfWYJO6Sk3MDZVyE2h0ryV2ppgxTIjIr2kVxVJImx8cIomQxhW-mLVwjX8-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
عجب
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/136061" target="_blank">📅 00:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136060">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
✅
شهاب زندی: تراکتورسازی برای جذب کسرا طاهری نامه زده اما ما بهش قول دادیم بره پرسپولیس.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/136060" target="_blank">📅 00:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136059">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❗️
❗️
شهاب زندی مدیرعامل نساجی:
🔴
🔴
بی تعارف آقای اوسمار که مربی بود گزینش آقای طاهری بود و پرسپولیسیا سفت و سخت اومدن جلو، آقای اسکوچیچ هم کسری رو میخواسته
🔴
🔴
آقا قبول کنین دیگه آقای مهدی تارتار گزینش کسری طاهری نبوده، شما چطوری برای بازیکنی که ببخشید تو 30…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/136059" target="_blank">📅 00:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136058">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❗️
❗️
شهاب زندی مدیرعامل نساجی :
❌
❌
آقای خلیلی میگه کسری طاهری رو نمیخواستیم و گرون بود، اصلا قرار نبود برای کسری پول بدن، اصلا ما نمیتونستیم کسری طاهری رو بفروشیم، ما خودمون کسری طاهری رو خریده بودیم و ثبت کرده بودیم
✅
✅
هوادارای عزیز، مردم، مسئولین و همه سازمان…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/136058" target="_blank">📅 00:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136057">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
شهاب زندی: قرارداد موجود است همه چیز برای انتقال طاهری به پرسپولیس یه قرضی و رایگان با بند خرید دائمی موجود است آقای خلیلی دروغ نگوید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/136057" target="_blank">📅 00:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136056">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✅
✅
🔴
🔴
شهاب زندی: اسکوچیچ و اوسمار او‌ را خواستند اما تارتار نه! قرارداد موجود است او همین الان هم بخواهد قرضی و به صورت رایگان با بند خرید دائمی میتواند به پرسپولیس برود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/136056" target="_blank">📅 00:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136055">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❗️
❗️
شهاب زندی: قرار بود کسری طاهری قرضی بره پرسپولیس اما تارتار او را نخواست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/136055" target="_blank">📅 00:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136054">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
شهاب زندی: برای فروش ایری قرار است هیات مدیره تصمیم بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/136054" target="_blank">📅 00:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136053">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvMsku_St3afQgWk37DbxfgTrQHvmuNCf_vmdPfBruJSF_OVY_HQGLzvmoZyXhUrFwqJPX5Zyt-wo2mFbytwQulQ4LpNU6tH9K7ZYyBHGzJFNT0lpc1FNIZkoy88E4-ceb-D46BRHLdPYiaCDDtOWlgox_POamKZNUtpSOFW4QTjMJrgGnIyxdiZgpX5d7iAmvOv7u9qYRgv9ytP4V-u0XjHEvMo2_TXbT6-juFG9DXJfArl7tZhhtmMdZgdIn0Y9JnteuOJnJw7IAx4LftU1BGgBf6GpfkBqSOxxpB9oi5KwkYfWPR2uwUR2bT-ybcxvT7BDRWI9B5wAjpqPZoIrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فوری/ سنت‌کام:
❌
دور جدید حملات از الان شروع شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/136053" target="_blank">📅 23:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136052">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
علی دایی فقط یک نام نیست خود تاریخ و افتخار هستش  نه فقط تو عرصه باشگاهی و ملی و فوتبال بلکه تو زندگی هم شریف و عزیز هست  کمک های زیاد به خیریه و نیازمندا کمک به زندانی های مالی
🔴
بر بدخواهات لعنت جنتلمن
🍸
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/136052" target="_blank">📅 23:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136050">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
پهلوان علی آقا دایی خط قرمز مردم ایران است
❤️
🔴
با قلب قرمز به این پست تایید کنید
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/136050" target="_blank">📅 23:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136049">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
هرگز برا کسی که در حق شما بزرگی کرده و شمارو به مقامی رسونده شاخ و شونه نکشید
❗️
یا رب مبادا گدا معتبر شود!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/136049" target="_blank">📅 22:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136048">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❗️
❗️
واکنش تند گداوند به صحبت‌های اسطوره علی دایی: تنها مربی که در آزادی به عربستان باخته، روی فراموشکاری ما حساب باز کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/136048" target="_blank">📅 22:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136047">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❗️
❗️
واکنش تند گداوند به صحبت‌های اسطوره علی دایی: تنها مربی که در آزادی به عربستان باخته، روی فراموشکاری ما حساب باز کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/136047" target="_blank">📅 22:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136046">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJYZkNXqRID34DTqZeWZTHCmrOkB9Sad-DuMGkcGLs07klJ9NkhA9mLEF-2huvKAgWwpXg7LpbWem1B5D0WlIL6XoyN15vxQeDNnLah_lGFr5SZSxvniOUQXmG5P4uo7eio9xvnpeXV5x7tdnOTNCZYdrBWoM3nLlyX1oQun31TL1ZzJYyej2Uzv2u9ogovNgxt_X0T4D-s09ESMMeS7dBQrc8LdiW-axbcmiB8870U9o31eCRFKJa73WPxyElktN5AkoEbmZFjRjSNsTDc3ney1PlHgDlxDc1mi6PggB6ERDtV6jar4nFV5LFfeOUm_WEifsHoEguCZKTxRsGtX2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
❗️
واکنش تند گداوند به صحبت‌های اسطوره علی دایی: تنها مربی که در آزادی به عربستان باخته، روی فراموشکاری ما حساب باز کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/136046" target="_blank">📅 22:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136045">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
✅
جدول لیگ آزادگان در پایان فصل
🔴
نساجی قهرمان لیگ دسته یک شد  مس شهر بابک به لیگ برتر خلیج فارس صعود کرد
🔴
نفت آبادان راهی پلی‌آف صعود شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/136045" target="_blank">📅 22:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136044">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1HewT9Rm5WtrWryAibSuFOM_Jv5G0IfsTNLQLgi-rEN69LNCeCoPDUfGmtuR2MTKkgqbWM3IqtFcdYxdbLNZxrj_0MVrvwUsuLi8p_XA7-k9YnqUX3PhkDqao0MdzgtzvHh0gPkHkZWZS2QDwkZG1vmN_2IQ62uQlaoCrO1GhurFcKDDV_P50O0LgM09LerHtmpEAx36jl4JoQou17NG5cEpeLzGF8_f0bKx9zGnV-ZBZxDhj3ZPRApEKoNROyUrc45TZHcnaIBhylYjvL2WA9DJgRnzRsnbU-mRHDc_13X0FAOcqxcty8RUk4t3Tjk6WOh7-Pq4Sq9VoaMJW4e_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
مس شهربابک دومین تیم صعود کننده به لیگ برتر بعد از نساجی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/136044" target="_blank">📅 22:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136043">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فرهیختگان: محسن خلیلی دیروز در جلسه با تارتار برای برگشتن پورعلی گنجی به پرسپولیس وساطت کرده که تارتار قبول نکرده حتی بهش گفتن بزار ابرقویی بفروشیم مرتضی برگرده بازم زیر بار نرفته تا پرونده این بازیکن واسه همیشه توی پرسپولیس بسته بشه
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/136043" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136042">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJltSZWiwu0GaCt5fozrQ9aYlQGephhbJuLWGATYJ-e7BYLZCTPDH5fkvXDvqTrChh50lThUpL4Z0o0DwrPmMm3yPA2JDHxJbH_kLDkmYfbROTSHVRE-c7HdLSB8XRKBcfJDFSVwXFSwwpwwZ4_gGQLs6NVeARogseVNAqwwlzuIApZBjCVXQVNcrZJ5IrhURp7N2n8iowhiNHZcvpYLp60xBzAtBozaBnudPgt7eAPY1Jq0pa9F5iTaE-Gz_zAanUvTxzNkdXyBH1AzJQLYxSAJKGAWb0v_1iU26SdrOzojj4F6_s11G8N4ZuVGljY3QeywbiWfROsN8wuabrHVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
📸
تصاویری از تمرین امروز سرخپوشان با حضور اورونوف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/136042" target="_blank">📅 22:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136041">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVcqCLQryTS6QQNir2Bwmv3ouNqKr-0SaBhXI_83eUIYX_mmSVaH6iIS-vGZtlBbH2C8z2fpEGFnkApo8B2DkiOzxOwmCWQwQWhBNyKElCy55ctnztTON_L3gKpKuj54bZUbvHaFK7BwbXT2kk-b1yYXRRPuPJioA3OC3qQ0bSG_mwzQUClESidu_FwtkI-FHz2UCaSLOZ5uP8m0VymXutdXxNkWnddv-vzCf7uobl8lQ_s0V-wCAE4n8IlDi2CTmURlUWC_Y-zFmmCVF-Sz_vTLMhTLesIz7PTk04YnDMXE5TQcoKqhUn_DWDungkAYU60TUHWXmya_6lfHIzCc1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بمب پرسپولیس در آستانه انفجار؛احمد نوراللهی به تهران بازمی‌گردد/
طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/136041" target="_blank">📅 22:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136040">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
✅
اورونوف صبح امروز به تهران اومده و بزودی به تمرینات تیم اضافه میشه
🔴
مهدی طاهرخانی
🥇
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/136040" target="_blank">📅 22:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136039">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbGUUKNbMVnTUEwdaxMtwHmVSSWa2yG8wktAQsDzN7RKnCjBEHkpq-_Oh-upxxnRbLX04SmEw19zWEsB0u7IKqcIrwk1TEtsb57EM0SoC9isHcKrNTrXgP0HiqPAxCHGD600jyy7Oyx0tvKcN6Jn_IDfQ8vNC3FbGx91PPuPgZ2GC1L7Uu7n6inY_OJBmksG5yiEsG49tay9nJpSASOmAD2ZmerRJbthklwWgHX16GUogdmvX5twUCWxezFw2-WnvVBfRxLURaApE4PMiWRRqegvadO6ITUSGs3HLdatK3SGzotQJ0aiG1JO8xdEO1DGj68ms0BqGalepYKkglSX3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
عجیب‌ ترین بازی سال در لیگ یک رقم خورد، نود ارومیه با 7 بازیکن مقابل مس کرمان به میدان رفت و بعد از مصدومیت یک بازیکن، مسابقه به دلیل کمبود نفرات نیمه‌تمام موند و با نتیجه ۳ بر صفر به سود مس کرمان اعلام شد. این تیم پیش‌تر هم یک بار در مسابقه‌ای مقابل بعثت کرمانشاه یا تعداد کم بازیکنان حاضر شده بود
😂
😂
😂
❗️
❗️
نود ارومیه به دسته پایین تر سقوط کرده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/136039" target="_blank">📅 21:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136038">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5faf86265.mp4?token=Hz1cNmFkTb292Y7_LfSPplViiU9KX7ySph4lcaZRXmPNfFZhg-sbNwBHfAtwpINzfv1cfoLWvrd46XpdrUHqKZFPk5oXZNxP4PlggfOpPi4-L8Me6hNA-67hiS8CpmronsBgUIaA4xfDxYFUVKe6DHE0t48NP1BvHR1Y_5z9qyVX6hVrwfqgokNEGNEGakRvRcuDi-A4_z63LplPSpwiJ4cZyXz4UtqotFOF5pDVDyTbfVzpgYZVdSWw4MXt53b5Vb696GZkVbAuJDDvbFHm2iDlvpGDg85tyGPuX-xSJdCYouV3jhwBmV-uNgA3rM2Vb2TZ09Cn8S8vHBwmwOhCoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5faf86265.mp4?token=Hz1cNmFkTb292Y7_LfSPplViiU9KX7ySph4lcaZRXmPNfFZhg-sbNwBHfAtwpINzfv1cfoLWvrd46XpdrUHqKZFPk5oXZNxP4PlggfOpPi4-L8Me6hNA-67hiS8CpmronsBgUIaA4xfDxYFUVKe6DHE0t48NP1BvHR1Y_5z9qyVX6hVrwfqgokNEGNEGakRvRcuDi-A4_z63LplPSpwiJ4cZyXz4UtqotFOF5pDVDyTbfVzpgYZVdSWw4MXt53b5Vb696GZkVbAuJDDvbFHm2iDlvpGDg85tyGPuX-xSJdCYouV3jhwBmV-uNgA3rM2Vb2TZ09Cn8S8vHBwmwOhCoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
میلاد سرلک تو اولین بازی دوستانه فولاد مصدوم شد و به نظر میرسه چند هفته نمیتونه تمرین کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/136038" target="_blank">📅 21:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136037">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❗️
باشگاه پرسپولیس با وجود داشتن پیام نیازمند، معتقد است با توجه به در پیش بودن جام ملت‌های آسیا و اردوهای تیم ملی، به یک دروازه‌بان با تجربه دیگر نیز نیاز دارد. در صورت جذب اخباری، امیررضا رفیعی به صورت قرضی راهی یک تیم دیگر خواهد شد. / تسنیم
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/136037" target="_blank">📅 21:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136036">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
قدوسی در خبری فوری
❌
احمد نور میخواد برگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136036" target="_blank">📅 20:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136035">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
فوووووووووووری
😀
کانال 14 اسراییل: پل و راه اهن و فرودگاه و پادگان ها در جنوب ایران بمباران میشوند تا جنوب تسخیر شود. بزودی نیروهای امریکا وارد ایران میشوند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/136035" target="_blank">📅 20:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136034">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه، حتما عضو شین و‌ چک کنید چقد راحت سود میشه کرد
😉
✅
JOIN JOIN JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136034" target="_blank">📅 20:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136033">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMEZ3AB658ZQ0EnaTHJVr3vkJasG-q3Y7IW_T4wCgOcB6_Kq05NubSYuPb70bNGLRmmZ0GxtyVgy3gamD7jNXIWSPIeWRgXPizMSiGXlMy6WCjfyL6a8ErDXqrwDbSUO0cyg6oVRPKLHG0GDiTRMDwWjyzFbyWqIVuyFgAx-7gOw8E25l292_b-jj1g1oaC1r7rZymgCpKHR6mHJzXwyoE7-GWOOl1ynCOnMzurBVvZ_qLigfIgNp4rCsRR9fttFaCSZ49PJCLKKeYB4-4skSpsTlHj_vbPSLReFaXZxj2jKShoKPHUP8o923s7jsa1rT9JGinBf3Bf7n2CrSLvR_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب حتی با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🤷‍♂️
@PeakyBetBlinders
@PeakyBetBlinders
@PeakyBetBlinders</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/136033" target="_blank">📅 20:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136032">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
باشگاه پرسپولیس درتلاشه‌که‌از بین مسعود محبی و دانیال ایری یکی روبه‌خدمت بگیرد و مذاکراتی با هر دوباشگاه آن‌ها انجام داده. امادرصورتیکه بر سر رقم رضایت نامه به توافق نهایی و کامل نرسد به احتمال بسیار زیاد قرارداد مرتضی پورعلی گنجی مدافع 34 ساله سرخپوشان‌پایتخت‌یک‌ساله…</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/136032" target="_blank">📅 20:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136031">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
✅
پیام گلر یک پرسپولیس و ۹۹درصد گلر یک ایران در جام ملت‌ها است. برای چی باید اخباری جذب بشه که خودش رو در سطح گلر یک می‌دونه؟ که چی بشه؟
❌
❌
ضمن اینکه امیر رفیعی هم گلر مطمئنیه. چرا باید الکی چالش درست کنیم توی پستی که اصلا مشکل نداریم!!! به فرض جدایی رفیعی…</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/136031" target="_blank">📅 19:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136030">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❗️
اولویت در دفاع چپ با میلاد محمدی است.او گفته اول طلبم را بدهید بعد تمدید.باشگاه هم گفته کارها همزمان انجام خواهد شد.محمدی هنوز توافق و امضا نکرده است.
🔴
الترناتیو میلاد محمدی رزاق پور از  فولاد است/قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/136030" target="_blank">📅 19:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136029">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
فرهیختگان:
🔴
باشگاه تراکتور همزمان با علیپور و مغانلو درحال مذاکره است
🔴
شهریار به مراحل نهایی رسیده اما با علیپور بر سر مبلغ قرارداد تفاهم ندارد،
🔴
علیپور درخواست قرارداد بیش از 100 میلیارد تومان از باشگاه کرده که فعلا مورد پذیرش مدیران پرسپولیس قرار…</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/136029" target="_blank">📅 18:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136028">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووری از تسنیم
⏺
محمدرضا اخباری در آستانه عقد قرارداد با پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/136028" target="_blank">📅 18:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136027">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
#شایعات
‼️
با وجود توافق میلاد محمدی با پرسپولیس، مخالفت همسرش با زندگی در ایران مانع امضای قرارداد شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/136027" target="_blank">📅 18:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136026">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
مهدی تارتار پس از تمرین روز گذشته نام کاظمیان را در لیست مازاد قرار داد و قرار است کاظمیان فردا قراردادش را با پرسپولیس فسخ کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/136026" target="_blank">📅 18:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136025">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
🔹
تارتار کاظمیان رو گذاشت لیست مازاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/136025" target="_blank">📅 18:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136024">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">💢
💢
💢
پرسپولیس در حال مذاکره با محمدرضا اخباری برای گلر دوم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/136024" target="_blank">📅 17:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136023">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOinh6bHOGTt6OJd5HNJCN2A2urPDRN8WS3KigYHIGaR4-mRyG2mGsrUISYXbO2Yb-x5xELVyXIcc9eQpDRusSybNOzKU2xOBDE6QDYx6tNLRCGAQa8cEolpWbgPDqpH_9DhT01vsXrrZCXxwcimib_Pw9EhNRh6utCrVdBsuP9vKhk5urd5aEcbqH3hVl8x_vnpEhgYC0shbKnt26ias1Fqn8N86InexBjAMhvQxudjpu7fB9lSF4uV7dJuG4AAAQXYSwWOJTL-Fwxi1TcPMSZXp5dShWhko4qO41fdKvxZweLEWfr1IH3NP7-S4kfWG6IATCmHK8Pa3AbGZOJ4cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
رسمی؛ با توجه به پیروزی ژاپن برابر بلژیک بقا ایران در لیگ ملتها والیبال قطعی شد و حتی اگر دو بازی آخر خودشو ببازه سقوط نخواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/136023" target="_blank">📅 17:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136022">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">💢
کاظمیان + رفیعی میرن گل‌گهر پوریا لطیفی فر میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/136022" target="_blank">📅 17:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136021">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">💢
کاظمیان + رفیعی میرن گل‌گهر پوریا لطیفی فر میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/136021" target="_blank">📅 16:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136020">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❗️
❗️
جذب لطیفی فر کنسل شده است / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/136020" target="_blank">📅 16:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136019">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
تسنیم : سامان قدوس در لیست خرید پرسپولیس نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/136019" target="_blank">📅 16:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136018">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlOilxRF3rgiSJx4q2ZaqRV-wGSgGk9K1K5zXfS3QLFoxLe0mFbX8zz5uKvbo8RYSoTR6dmzxOIXukGKeBlZDyQh3dSFKQ_0VmYII9UbKpunjwRm0SyCSzRHOMN65YelVdD1bJE1D4O5S-DlZs_1piFCQqHCZLmjf_tD4PG7uDy9Sj6hQENSi-H8kQRFpNpJGCNXc0HvUIfQEfNeV4rkJs3Qx-AF_LBAIjbTGj3CaqWoLRCf5fAB6xifTkI9hey2qjSzBszsbjL0cTAfV-u6Hc9-oYdvBlgC6zn8h_opAYGTBGt2gV0EhFiSUGAHoMjY-n8MkZlbDA9JvrimA8nPVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تو 24 ساعت اخیر سرچ «لغو عضویت جانفدا» بیش از 5 هزار درصد افزایش داشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/136018" target="_blank">📅 16:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136017">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
تسنیم : سامان قدوس در لیست خرید پرسپولیس نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/136017" target="_blank">📅 15:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136016">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
❗️
اتحاد کلبا رقم‌ رضایت‌‌نامه سامان قدوس رو 500 هزار دلار تعیین کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/136016" target="_blank">📅 15:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136015">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
با جدایی سرلک، محمودی خواهان شماره ۱۰ برای فصل بعد شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/136015" target="_blank">📅 13:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136014">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
✅
سامان قدوس در فهرست نقل‌وانتقالات باشگاه پرسپولیس قرار دارد و سرخپوشان به دنبال جذب او برای پست شماره ۱۰ و جایگزینی با رضا شکاری هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/136014" target="_blank">📅 13:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136013">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
چهارشنبه هم گذشت و اورونوف برنگشت !
❗️
روزهای پایانی هفته گذشته اعلام شد اوستون اورونوف ۲۴ تیر ماه به تهران برمی‌گردد اما هنوز خبری از این بازیکن ازبک نشده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/136013" target="_blank">📅 13:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136012">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
فوووووووووووری
😀
کانال 14 اسراییل: پل و راه اهن و فرودگاه و پادگان ها در جنوب ایران بمباران میشوند تا جنوب تسخیر شود. بزودی نیروهای امریکا وارد ایران میشوند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/136012" target="_blank">📅 13:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136011">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❗️
یا تمدید یا خداحافظی!!!  فرهیختگان: میلاد محمدی باید سریعاً تصمیم بگیره قراردادش رو تمدید کنه یا بره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/136011" target="_blank">📅 13:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136010">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
تیم پرسپولیس که قصد داشت فردا برای اردوی اماده‌سازی راهی شهر ارزروم ترکیه شود، با یک هفته تاخیر اردوی خارجی خود را برگزار خواهد کرد.
🔴
🔴
پرسپولیس روز ۳۱ تیر ماه برای این اردو تهران را به مقصد ارزروم ترک خواهد کرد و احتمالا دو هفته‌ای در این اردوی خارجی حضور…</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/136010" target="_blank">📅 13:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136009">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136009" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">💛
آپدیت جدید اپلیکیشن اندروید MelBet
❗️
🎁
کد هدیه 100 دلاری:
giftcodeir
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
آموزش ثبت نام و واریز
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را فارسی کنید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/136009" target="_blank">📅 13:10 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
