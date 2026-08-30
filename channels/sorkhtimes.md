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
<img src="https://cdn4.telesco.pe/file/ZA-Qf694SOL71xhk_OcjYJZDxwvrfzFkf0VGj-Xzxccw8ebj6h4XnmmAtUrq5WMgvDk7gWiJB6GJXWpzfAbxjokvz9NsJoxqKC1e3gy90Sy8kSgO_jrcWbQbC-opz9T9sB1uaWDjqPnhFssURsSjIpbK2Vg3OdNAlKRWC4Z6C--RyiBNH2_EnPfBqXHJlqm158q79YVez8NjHb5eznV6susQqgEP6kANq51mUUMQd2LqPXhasNcXjN4RSvhAEGtrsB6nztcnaG1h6KhuvfpPmwQM0CmB0CA0lF7Nnc47iJPbWLccVkimbQneAFFBarl_0l3uirqx7_t4wcIQ7q9i3w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 21:36:25</div>
<hr>

<div class="tg-post" id="msg-139262">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3uwyJmPCvdarurk-jx7vb3XTynU9Bc9mflIYwl6_oWIS5NIngQRE67qqP-MArKbe4aabIIFZsgPDoiXTzjTsstZLVZP87rxOptk1HN97nBpxeEYvykX2xW94h7UWLTQA9D15cm3tIb6KsZrHarhtg7GY6WMtweK1pAXLRNLaPamvoZFf9ma38jcv6IP18fPP0q9Il-bFN_jTdlOeRX5EgqOG7SyDi2twh-QsfWCbGBBPgESKy_JypOeMLEySRks-vsE7aVJJgWXDhePTvwclW_CBJ0aALTkndnJGXvgbfmQNlmj6hMCHjIweS9a77CFhDbPcEeqitQmDD93QmEVoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
منچستر دوباره در مسیر برد!
شیاطین سرخ مقابل ایپسویچ؛ یک نبرد برای سه امتیاز، اولدترافورد آماده یک شب پرهیجان
[
منچستریونایتد
⚽️
🆚
⚽️
ایپسویچ
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/SorkhTimes/139262" target="_blank">📅 19:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139261">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👾
تیزهوشی و تلاش علیپور برای ثبت این گل کافی بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/139261" target="_blank">📅 18:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139260">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
نگاهی متفاوت به گل‌های اول‌ و دوم در برد دیشب
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/139260" target="_blank">📅 18:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139259">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
🔴
دو گزینه اصلی قضاوت در دربی 107
💢
کوپال ناظمی و موعود بنیادی‌فر، دو گزینه نهایی کمیته داوران برای قضاوت در دربی تهران هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/139259" target="_blank">📅 18:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139258">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGBHNRwCsIS6Iobd9br8mveqVQTPu-slVHlFOHeProfSEj3P1eEYfTNdjohGuD-Gxe0QC2n2PBzP236-d3tTiMMy_K23YABOUZN-ZUOm0xhqKAu6fsDpIn8dYL8qPDke9rDkhMa-pWfWFpjasWuZqD1JcyIO7nDiCIguOmilUtPS1Vi5ZxSjaxwUDZoe1vwplBRvg99A3XnKY5_KBZka8_mThBVanlv4XG5ZbUlkXXOuILYdmF_m4wmiR9LHpnIj0MQEJUvdUuBdjzioDco4fMCUixaZ16LCB-w1zSWcaSn5fFfKXGo8MLboEAzlASn-SYmIenR1_wHb5Bnek3wMBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رئال مادرید آماده یک شب متفاوت!
⚽️
مالاگا میاد تا جلوی کهکشانی‌ها وایسه، نبردی برای شروع قدرتمند و یک برد شیرین!
[
رئال‌مادرید
⚽️
🆚
⚽️
مالاگا
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/139258" target="_blank">📅 17:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139257">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
یک‌سایت خبری روزگذشته مدعی شده که مهدی‌ترابی در بازی با چادرملو دچار پارگی رباط صلیبی شده و فصل رو از دست داده! باید منتظر تایید یا تکذیب این خبر باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/139257" target="_blank">📅 17:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139256">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
عبدی : من زارع هم میخواستم، پرسپولیس گفت نمیدم. هاشم‌نژاد هم میخواستم که شکمش رو عمل کرد. کوشکی هم جواب تلفنم رو نداد. حسین‌نژاد هم بعید میدونم که تیم خارجی به ما بازیکن بده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/139256" target="_blank">📅 16:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139255">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
✔️
با 5 بازیکن چگونه برویم تمرین کنیم/ می توانیم برویم گرگم به هوا بازی کنیم اما فوتبال نمی شود بازی کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/139255" target="_blank">📅 16:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139254">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
✔️
حسین عبدی: 23 بازیکن دعوت کردم فقط سهیل صحرایی، مسعود محبی، پوریا شهرآبادی، پوریا لطیفی فر و دانیال ایری آمده اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/139254" target="_blank">📅 16:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139253">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✔️
✔️
سه پرسپولیسی به اردوی تیم امید اضافه شدند
❌
❌
پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن تیم فوتبال پرسپولیس، به اردوی تیم ملی امید ایران اضافه شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/139253" target="_blank">📅 16:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139252">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
فوری/ با اعلام مهدی تارتار باشگاه تا 22 شهریور بازیکنی به تیم ملی امید نخواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/139252" target="_blank">📅 16:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139251">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
✔️
پرسپولیس با 9 گل زده تا هفته چهارم بهترین خط حمله لیگ داشته و امشب با ثبت امید گل 4 بالاترین امید گل رو 4 هفته ابتدایی ثبت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/139251" target="_blank">📅 15:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139250">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🤩
✅
هفته‌پنجم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
طویله کیسه
🤩
🗓
تاریخ چهارشنبه ۱۱ شهریور
⏰
ساعت ۱۹:۳۰
🏟
میزبان نقش‌جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/139250" target="_blank">📅 15:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139249">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🤩
✅
هفته‌پنجم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
طویله کیسه
🤩
🗓
تاریخ چهارشنبه ۱۱ شهریور
⏰
ساعت ۱۹:۳۰
🏟
میزبان نقش‌جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/139249" target="_blank">📅 15:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139248">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
تیکدری دفاع چپ پرسپولیس در دربی/خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/139248" target="_blank">📅 13:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139247">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
❌
تیکدری: روز اولی که به پرسپولیس اومدم گفتم با تمام توان در هر پستی بازی میکنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/139247" target="_blank">📅 13:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139246">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">☑️
پرسپولیس برای دربی اردو زد!
🔻
با تصمیم کادرفنی پرسپولیس، اعضای این تیم بلافاصله پس از پیروزی برابر ملوان، راهی اردو در هتل المپیک شدند تا برای دربی ۱۰۷ آماده شوند؛ تارتار بعد از کسب این سه امتیاز به تیمش استراحت نداد و باتوجه به فشردگی رقابت‌های این فصل،…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139246" target="_blank">📅 13:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139245">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⚽
👤
🎙
ابوالفضل جلالی:‌
🔻
حضورم در دربی؟!هنوز هیچ چیز مشخص نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/139245" target="_blank">📅 13:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139244">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrunHVUHnhkNF2NMzNVqVqEXA-FpW0nOCwfTk4NGzGd9uG8mouXdrqzTBCFDxICvTVvPBGCk1n1pud57o73Ikc52XLLdruvPLtaSu5wTw7j_aeFxCMWCfDuQ5H68f8Ly5Aj6r4OqSH_KfNFHbOmfjMFUsH9_31JTQfe4TGil2x0Dh2hrKpSlzRh1RyJBZYPzBQigc6zxjhSycpyq9HxX10af0__9aH2kIrXUi4o1Pjl0kgPsmnp60V7AQwLhdV5RLeetZ43Cxo4R1lXKIC0JRwr63uuRPZNjaPREzISLQEXhTDvdz2sCn9rDvhaz22bCi4u4yXfouf8sfz_pZF1GQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی علیپور با نمره 8.45 بهترین بازیکن بازی پرسپولیس و ملوان شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139244" target="_blank">📅 11:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139243">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🗣
🗣
با تلاش کادر پزشکی تراکتور؛ مهدی ترابی به دیدار با پرسپولیس رسید و از روی نیمکت بازی را آغاز خواهد کرد. هاشم‌نژاد غایب است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139243" target="_blank">📅 11:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139242">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mywPe144r2sG5f8IPj1CVmphPt2RGApa8AToPbYb-ASeisApuN4Q016gq3adGAHz6g3tkIDg_XAe03nC3MIlCgSqovBIiu4KNET0a5mi4eescDUfxDAAx2nAvMzCdfONECHCZLhyFnvjEpq3Wmzw3_bKY7GKUQxdBCqqNbq89U00vQtgfjZjbUVqpgfcTnU_HyDGcENQep1H33QcfAkPmlfb_iCkzFU7yS6qw6gHDLafA6_IV75-xo4LShHprLqTfeHYc0ZyXMAIXJlpPvuXLYpiNuATJmzxT1mQKWbGDPPbpSFUya9idNcMaDKPHkO6m6XyVV8v9D9Q2DSnxAS-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در آستانه ۱۰۰ تایی شدن ؛ علی علیپور به رکورد علی پروین در پرسـپولیس رسید و به دومین گلزن تاریخ پرسپولیس تبدیل شد
✔️
✔️
علی علیپور با گل‌زنی در مقابل ملوان، در کنار علی پروین با ۹۵ گل زده به دومین گلزن برتر تاریخ این باشگاه پس از فرشاد پیوس ۱۵۳ گله تبدیل شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139242" target="_blank">📅 10:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139241">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
‌ تیکی‌تاکای تارتار؛ ۱۸ پاس و گُلی که نشد
❌
پرسپولیس با ۱۸ پاس متوالی روی زمین یکی از زیباترین حملاتش را ساخت و تا آستانه یک گل تماشایی پیش رفت، اما ضربه سر ایگور سرگیف از بالای دروازه بیرون رفت؛ با ورود اورونوف، سمت چپ سرخ‌ها هم فعال‌تر شد و ترکیب‌های…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/139241" target="_blank">📅 10:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139240">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1Vk-3CAFNv9tqIquyuN03L2zLT9m8UQDVITwnHQ9g9rh8dbWos15f8HSobDgWp2EyNN78eEYgHE0x2L3V9W5VNwKT84LTplm_Fr_n1Yx5YXWmPBdDTGdMTWLROCP2bVsGu2RAQ-vokrNnpmfUOqHuYEJZRrcBvWpKm3YTC0Os8ZgYuna_SsgBovgu1ky-nb3rzKN1VptPB1dBDSB6wr9jtMVvl9JUDU9eHkS6KBSC-Nktd8sHI77rcVVVr6lX55hJg8VuNF9FHycOEeSUN58kP592ohF1VlE5S0ownJcTM0dIDXbbwr50uvZOI18MQzx5dTMdw2k5kbW7sRw_N3Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
صادقیان دیشب تو ورزشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139240" target="_blank">📅 10:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139239">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
اردوی پرسپولیس برای دربی بعد از بازی با ملوان آغاز شد و بازیکنا به هتل المپیک رفتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/139239" target="_blank">📅 10:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139238">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🤩
✅
هفته‌پنجم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
طویله کیسه
🤩
🗓
تاریخ چهارشنبه ۱۱ شهریور
⏰
ساعت ۱۹:۳۰
🏟
میزبان نقش‌جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139238" target="_blank">📅 09:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139237">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
‌ تیکی‌تاکای تارتار؛ ۱۸ پاس و گُلی که نشد
❌
پرسپولیس با ۱۸ پاس متوالی روی زمین یکی از زیباترین حملاتش را ساخت و تا آستانه یک گل تماشایی پیش رفت، اما ضربه سر ایگور سرگیف از بالای دروازه بیرون رفت؛ با ورود اورونوف، سمت چپ سرخ‌ها هم فعال‌تر شد و ترکیب‌های…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139237" target="_blank">📅 09:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139236">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✔️
✔️
پرسپولیس با 9 گل زده تا هفته چهارم بهترین خط حمله لیگ داشته و امشب با ثبت امید گل 4 بالاترین امید گل رو 4 هفته ابتدایی ثبت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139236" target="_blank">📅 09:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139235">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
صبحی که تیم محبوبمون توی ی بازی جذاب و دیدنی بازی و برده بخیر.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139235" target="_blank">📅 08:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139234">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clB09SFqqre6oQ2O7ifCYQxaCnzhU4pkbPpPHg9HVlWIp_-Ng4FGXYVlzt9cHOnI4fUBJjwnzGeWEE5Zy6UEz-UX1WPEaRz6fYny-kQLB8NC733Ut2cmh6zzXOGNqM_JcPZdIU_rbCWKZShCYqeMs1IGdl33aMgkLP8b5cr5WOgW_iA5-QS2cOMRYdquH-qj07kLLL7D7BkQrblODWtAt05UmmUc3aMT0lcKv5om556jyvlM5O3RoRIkwMGT15rt-4ZnAW2sf90dYO9-pcGPQ0QiUZT6IZFjNYuUne_32ZfSVUvCsxqMJupyg8Wu2B-GAAVLZ8a2K2Ro9ogQ6bWoYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139234" target="_blank">📅 01:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139233">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
🔴
جدول رده‌بندی لیگ برتر پس از پایان هفته چهارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/139233" target="_blank">📅 00:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139232">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✔️
✔️
مهدی تیکدری: بعد بازی قبل همقسم شدیم که این بازی رو ببریم/بزرگترای تیم خیلی بهمون کمک کردن/روی یه اتفاق به تراکتور باختیم/هجمه‌ها بعد از باخت طبیعیه/ترافیک در خط حمله زیاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/139232" target="_blank">📅 00:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139231">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
✔️
دانیال ایری امشب به عنوان بازیکن ذخیره وارد زمین خواهد شد تا اتفاقات دیدار با تراکتور را فراموش کند.
✍️
ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/139231" target="_blank">📅 00:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139230">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
حسین کنعانی ، دانیال ایری ، مجید عیدی ، پویا پورعلی و محمد عمری پنج بازیکن تیم پرسپولیس که سابقه پوشیدن پیراهن تیم ملوان دارن
✔️
فرزین معامله‌گری هم که برای سربازی منتقل شده به ملوان تنها بازیکنی که سابقه پوشیدن لباس پرسپولیس داره
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/139230" target="_blank">📅 00:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139229">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🤩
✅
هفته‌پنجم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
طویله کیسه
🤩
🗓
تاریخ چهارشنبه ۱۱ شهریور
⏰
ساعت ۱۹:۳۰
🏟
میزبان نقش‌جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/139229" target="_blank">📅 00:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139228">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4r-dWA75ZYSWV9TyjAmfVv3_jFNJViKTKMstlaxXzTW6N0mYy_quT4PFpikYo3wJn9ZG_W0Jk-iecwR0NrAR8PZgFNPIVcWPEk_Ekl0zXNb3LViS-UGy1apiOZQsN_T1Cc_D14dS7DHWxus7SdCvCGQESIzB3coTTd56XcXURnk6n2laLC55vMii1igCcmGYpfFOp037KSLNmfeW6Nu-zQCdOTv6RW3OJzKZeG2HgqO_sSdOjVRXwS6k49B-575XHaU51leqZAQhYBbUBWFON23nJIHiW03WxdJvQDhtqe-7mJO98X_IniY1tKV-4M0xOd2DLJUz0FFNZQF1PLQ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
✅
هفته‌پنجم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
طویله کیسه
🤩
🗓
تاریخ چهارشنبه ۱۱ شهریور
⏰
ساعت ۱۹:۳۰
🏟
میزبان نقش‌جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/139228" target="_blank">📅 00:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139227">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✔️
✔️
مهدی تیکدری: بعد بازی قبل همقسم شدیم که این بازی رو ببریم/بزرگترای تیم خیلی بهمون کمک کردن/روی یه اتفاق به تراکتور باختیم/هجمه‌ها بعد از باخت طبیعیه/ترافیک در خط حمله زیاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139227" target="_blank">📅 00:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139226">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
کریم باقری: پرسپولیس از هر بازیکنی بزرگتره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/139226" target="_blank">📅 00:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139225">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
کریم باقری: نگران نباشید. پرسپولیس بهتر میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139225" target="_blank">📅 00:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139224">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
باقری: کادرفنی زمان می‌خواهد که میان بازیکنان هماهنگی ایجاد کند
❌
تیم پرسپولیس به نفرات توجه نمی‌کند، همه بازیکنان جمع شدند زیر سقف پرسپولیس
❌
تماشاگران پرسپولیس را تشویق کنند، نفر را تشویق نکنند!
❌
اورونوف دیر به تمرینات اضافه شده و کادرفنی تلاش می‌کند…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139224" target="_blank">📅 00:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139223">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
آمار برگ ریزان بازی
🔴
۱۶ شوت
🔴
۶ شوت در چارچوب
🔴
امید گل ۴
🔴
گل ۳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139223" target="_blank">📅 23:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139222">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‼️
🔴
علیپور با ۲۵۷ بازی، از سید جلال حسینی با ۲۵۶ بازی عبور کرد و به رتبه دوم بیشترین تعداد دیدار رسمی با پیراهن پرسپولیس رسید.
🔴
علیپور در ۲۵۷ بازی خود با پیراهن پرسپولیس، ۹۰ گل زده و ۳۸ پاس گل ارسال کرده است. او با ۹۰ گل و پس از پیوس و پروین، سومین گلزن برتر…</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/139222" target="_blank">📅 23:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139221">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✔️
خلیلی: امروز فقط بهای جوانگرایی را دادیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139221" target="_blank">📅 23:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139220">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZX7SJ8p2OgrJgv3vTBfgJ--jubsR7haVt-ADW2f7DsKh_5qtKDVAUm_55uty8tXN59LxAMzYxHUATc0VEsJ443rEFsjOp8N1jyoirJhgfK99NGi-unO-KjCQHLg1Mp5kvh9Z7jsABiEvWjpte47oY7gapNify10NK6mK86xlqvjGWIYTaBD7MVHyvckVDX3Pv5nLUN_UDM2VWIZz-WA-VccXQ1UHzGutFSx2aJuSVtvcrst9Jc2NUEmCU8bjCx7k_y0Q-mWsza6y53RJFlcrEHTnSPLmNWWCMfcrWbp6Wr6ZmGoFVLlOys5E1RqI-3OxmbzIHmdTe8u6kEP41MJTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
ستاره این روز های پرسپولیس تارتار
📊
عملکرد بیفوما تو این فصل
🔄
4 بازی 1 گل 1 پاس گل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/139220" target="_blank">📅 22:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139219">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
✔️
براساس‌صحبت‌های‌مهدی‌تارتار؛ سرگیف از بازی فردا مقابل ملوان به ترکیب سرخ‌ها برمیگرده و تارتار میخواد زوج علیپور - سرگیف استفاده کنه اما اوستون اورونوف همچنان نیمکت نشین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139219" target="_blank">📅 22:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139218">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
باقری: کادرفنی زمان می‌خواهد که میان بازیکنان هماهنگی ایجاد کند
❌
تیم پرسپولیس به نفرات توجه نمی‌کند، همه بازیکنان جمع شدند زیر سقف پرسپولیس
❌
تماشاگران پرسپولیس را تشویق کنند، نفر را تشویق نکنند!
❌
اورونوف دیر به تمرینات اضافه شده و کادرفنی تلاش می‌کند…</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/139218" target="_blank">📅 22:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139217">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
باقری: کادرفنی زمان می‌خواهد که میان بازیکنان هماهنگی ایجاد کند
❌
تیم پرسپولیس به نفرات توجه نمی‌کند، همه بازیکنان جمع شدند زیر سقف پرسپولیس
❌
تماشاگران پرسپولیس را تشویق کنند، نفر را تشویق نکنند!
❌
اورونوف دیر به تمرینات اضافه شده و کادرفنی تلاش می‌کند…</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/139217" target="_blank">📅 22:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139216">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✔️
✔️
کریم باقری:
🔹
به زارع دوست عزیزم تبریک می‌گویم؛تیم خوبی دارد و ضد فوتبال بازی نکردند.
🔻
خداراشکر برنده شدیم و توانستیم با روحیه خوب به پیشواز دربی برویم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/139216" target="_blank">📅 22:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139215">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
✔️
کریم باقری:
🔹
به زارع دوست عزیزم تبریک می‌گویم؛تیم خوبی دارد و ضد فوتبال بازی نکردند.
🔻
خداراشکر برنده شدیم و توانستیم با روحیه خوب به پیشواز دربی برویم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139215" target="_blank">📅 22:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139214">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_B6nz3SUuf6D6P_gXwuoouvQnGqcY4adKGAf9mHBxWofmwXqmAP-luY5fdipkvDkonObFTi1Cazu-Rqh6tSN7Qs5mh5DGXjN63RlOcUA9GfASUX8FSbqj847KHwtNXH1Se9tnsNjoEkoHYbnKZCcfeMqTUUC9A6hEFJ8cEGbDpwjHf4klhy1C2gcCKVy3OzUS4c4v1xvw_ILRpjIYuHHYgZlhQWgCGeJlNz8yr-ZQNiCH7Ig_ZnBeXN5nDa_kpgke_DzY2sK78jRukbGpdzt1UGOXi0Gm3q9ud-3Au6fCAD5WEZkqUJ_B_bvSR49olWRXU_L7pDcZtFtwuV30BS1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
🤩
پیمان حدادی بار دیگر این استوری رو گذاشت/ حسبی الله : خدا برایم کافیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139214" target="_blank">📅 22:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139213">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✔️
✔️
مهدی تارتار به دلیل افت فشار در نشست خبری بعد از بازی شرکت نکرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139213" target="_blank">📅 22:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139212">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✔️
✔️
گفته می‌شود فردا نیز مهدی تارتار برای دفاع چپ پرسپولیس از علیرضا همائی‌فر استفاده نخواهد کرد و مهدی تیکدری در پست غیر تخصصی بازی خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139212" target="_blank">📅 22:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139211">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
❌
🇮🇷
کنایه مازیار زارع به برنامه فوتبال برتر: دوست ندارم تصویر من را در برنامه تان پخش کنید. شما اینجا باشید من مصاحبه نمی کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139211" target="_blank">📅 22:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139210">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=DQbGCoTED0b9XkuqDXmGug8-mgwxAq3lTk7eY4aXN0uBEDVg-eZRBvt0A7y9q7CqNlwkg9OmQVSj9zxNsMxTZHNfQOv2fD2QzvTLWdHqoxXawVcvf9OzAlsqjCyv7a2ICzxacMmSIzl1vb_MbavgIShSNCPoXDmQzqoiREmI8-a_1Iol2Y5VN2osptD1Puj2YsUK_6WtTBk8TnTQYB1P2J5wNhMvpI28-5D3pgeDhu0vlOIXzo5DVfpAy2BqRlNFOH8mV0ev57681vwacb1jSYliSL9QJGj_ohYH9Bq3YnGsiK7Vd-RG1fz04FwuglFEu3bBdRFsj67BqTJZ4Bbbnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=DQbGCoTED0b9XkuqDXmGug8-mgwxAq3lTk7eY4aXN0uBEDVg-eZRBvt0A7y9q7CqNlwkg9OmQVSj9zxNsMxTZHNfQOv2fD2QzvTLWdHqoxXawVcvf9OzAlsqjCyv7a2ICzxacMmSIzl1vb_MbavgIShSNCPoXDmQzqoiREmI8-a_1Iol2Y5VN2osptD1Puj2YsUK_6WtTBk8TnTQYB1P2J5wNhMvpI28-5D3pgeDhu0vlOIXzo5DVfpAy2BqRlNFOH8mV0ev57681vwacb1jSYliSL9QJGj_ohYH9Bq3YnGsiK7Vd-RG1fz04FwuglFEu3bBdRFsj67BqTJZ4Bbbnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
کنایه مازیار زارع به برنامه فوتبال برتر: دوست ندارم تصویر من را در برنامه تان پخش کنید. شما اینجا باشید من مصاحبه نمی کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139210" target="_blank">📅 22:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139209">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e73d84229.mp4?token=o3PPyuNRPm9-Sg0R6d2XWib6D-nNl3E4OtoqzYczJeWg1RGVVV-dpYIQfZzo4VWLKi-bEMSPqbj0PEsLszri5WcIQQRwrAmZOcnbVIoQ1WMKrvHQMCoaUowZPNU9LOfPMu1BQWUcfuAxD7_8Omo2JB74vnEd4h21-9QNvhOfgtY5gDCa7SZmNKec47YdXwmMp_ZiE1vpIjgsKLpjPiLPreZDv_LJHW-D8WJ_KUJ_-XgB0TG-s36P9BvD_yWHcJZsc-FqUWlyXOviM8gVlCPkZc3Zq0TivaOS5__ZCLq05elcAh07vwImgjZPdNL4sTTG_wuNwCj52Mkwz8IQnXltcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e73d84229.mp4?token=o3PPyuNRPm9-Sg0R6d2XWib6D-nNl3E4OtoqzYczJeWg1RGVVV-dpYIQfZzo4VWLKi-bEMSPqbj0PEsLszri5WcIQQRwrAmZOcnbVIoQ1WMKrvHQMCoaUowZPNU9LOfPMu1BQWUcfuAxD7_8Omo2JB74vnEd4h21-9QNvhOfgtY5gDCa7SZmNKec47YdXwmMp_ZiE1vpIjgsKLpjPiLPreZDv_LJHW-D8WJ_KUJ_-XgB0TG-s36P9BvD_yWHcJZsc-FqUWlyXOviM8gVlCPkZc3Zq0TivaOS5__ZCLq05elcAh07vwImgjZPdNL4sTTG_wuNwCj52Mkwz8IQnXltcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
👤
🎙
ابوالفضل جلالی:‌
🔻
حضورم در دربی؟!هنوز هیچ چیز مشخص نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139209" target="_blank">📅 21:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139208">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIxd10KrJOYDvTjgWRSgEeyXQhMR-W5cGKyCXOnZ5uaEn49EB6pbg98TWo_eyKlN3bpGeR30M6J3yu3E6f9Ov4Qi_bAgFOn0ocZIXAilf0kOm7kqgNzuCRvFYDPCvoN47q46KAJ8mupkrg0Mo2maaAUe-Jv6UnoNneV687rVaKS4Emf3Owm8UFpWhU9ldncjQKb_Y-f6lb1lTuAAyH631UpxwdVjvNOGe9un2gk1wsypr3AnjONMMdiJUvmKPdWY_mcnUHAN84eJ7L3mODgjbEAVSqKQ-55xgeRh9ETMVK_UNYEal2xUSKt_YNWPN-HbmU7zFMcObelsIiP8lK9fKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
هوادار همین سبکو میخواد آقا تارتار تیمی بدون ترس و سراسر هجومی تیمی که می‌تونست امشب خیلی راحت بالا 5 تا هم گل بزنه
⏺
خداشکر با روحیه بالا سراغ دربی رفتیم و امیدوارم تو دربی هم همینطور و همین سبک رو ارائه بدیم
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139208" target="_blank">📅 21:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139207">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a052a7430c.mp4?token=MTX7P1x-z0QxMQNjyCenJJDgAder_epD8xXaMO9iJUHqdu668g-qWqbeBh8aypqGVMytABayqgvO8LbeTmsg4V-qMI1HzrJFzYV4XgakyHdBzuTWP2mtG4n9u4N7cobKpABBewA1XI0jZc4pfnzEZu-8G69hh8nQY7OT2UYuc7EoE4cjVquehjMW8QcWH0me4fv0i4VeZLFbmdzbbz3w5KuYOfD_mRr-W9iEYsHTWg4t4AFn2DUp6xhO9y6hE4gV9nGN3f1lehxXSrYbeXFtYtnUDcqIoLmb9dynErNeLI4u-FnGVf8IDKqo0ex6Zup0v8ReUK0oA35CIHVhnN83Y1iorc8nYgasZdmAdlN8zNNbljXzjIUelkCZvAp3qaWl8Jp7oQ8CsVXqEC3Ir7MceMoYG1_28avTuEqd6AhoLmd3PnYJWejxP2EhPOBHj---GdZPdvhE6RWIadUDLZ3l_5k4UIee-gyZNa-X58IfZWojAlnipCoWlj8JEcMqm6IHJ-gZyLTm8Q1S2m9_bjLxQSZsNyKNraRt9iNIiolGTweahTpclCGjUtQLmUQ8mZRueV9GTv-O5ARXDUqHsmAEdjZ1laoeUfuHA-P57csXlUa5zu-Cn3ZA1yVocsE9Aiu4ABSZBA8Ki_AOivk6rywxnvSLNzq8hyK6LFD_bRjpBxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a052a7430c.mp4?token=MTX7P1x-z0QxMQNjyCenJJDgAder_epD8xXaMO9iJUHqdu668g-qWqbeBh8aypqGVMytABayqgvO8LbeTmsg4V-qMI1HzrJFzYV4XgakyHdBzuTWP2mtG4n9u4N7cobKpABBewA1XI0jZc4pfnzEZu-8G69hh8nQY7OT2UYuc7EoE4cjVquehjMW8QcWH0me4fv0i4VeZLFbmdzbbz3w5KuYOfD_mRr-W9iEYsHTWg4t4AFn2DUp6xhO9y6hE4gV9nGN3f1lehxXSrYbeXFtYtnUDcqIoLmb9dynErNeLI4u-FnGVf8IDKqo0ex6Zup0v8ReUK0oA35CIHVhnN83Y1iorc8nYgasZdmAdlN8zNNbljXzjIUelkCZvAp3qaWl8Jp7oQ8CsVXqEC3Ir7MceMoYG1_28avTuEqd6AhoLmd3PnYJWejxP2EhPOBHj---GdZPdvhE6RWIadUDLZ3l_5k4UIee-gyZNa-X58IfZWojAlnipCoWlj8JEcMqm6IHJ-gZyLTm8Q1S2m9_bjLxQSZsNyKNraRt9iNIiolGTweahTpclCGjUtQLmUQ8mZRueV9GTv-O5ARXDUqHsmAEdjZ1laoeUfuHA-P57csXlUa5zu-Cn3ZA1yVocsE9Aiu4ABSZBA8Ki_AOivk6rywxnvSLNzq8hyK6LFD_bRjpBxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
⚽
دانیال ایری، بازیکن جوان پرسپولیس به سمت هواداران ملوان رفت و به هواداران تیم سابقش ادای احترام کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139207" target="_blank">📅 21:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139206">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWur9UM8q2ZXfONdQAhR72wlVLZl_NkMXJ7QX1dKN8VQb_-fKEWz3qH2NGRQ7lUhTI2k8RmjI-IKtJJQuApcsU0AOhNqsWaV2Ck3fAnjxh1JVb8TTyGaWjfPBXHZy0-X6KGCl0lZ3jGJcvSV-0zm0AMVTq2JFC7Q42KibAhCvpMIO_TiZPyrIMFrjh9w8OZtWesVeqvS1h6-_01uXwzSoNQTxk00JyNDO9JQihQqRi4QOkX7ecHqED5tRNZP4NcZHK6C6CbWueQmCmWd6eP-TJkWiNdJ6L0rHPj8gFqqUNM7cBoADcfb8zmTyj6OyVNMzz2b7lUF4qk5aSxWlV3hhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
جدول رده‌بندی لیگ برتر پس از پایان هفته چهارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139206" target="_blank">📅 21:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139205">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37d6965b1.mp4?token=To6Ep0jvHnqg8KYz57TSKK8a1QMMfvJ6Ywo6JxfriBkFp5bhjbXbyZu43K-LNQhKXqdWyMnw-vO4zFxtgfxlEbJNhR1YIGiYK0dxxpFvrR0yfqYLHu9eJ2H4l-duCf0ZYfOWsWNCmpvc8777uHziUODh4I1xpbs2-8oU0PXm-H8xhA2ushpkPl5mVa6cmY46plABEUl61mBiNLZUOTmIU0DjIqD9ZC5tW4x9HKMNhyoZMh28P_t47kM0Hy6jx2ulsrXF2pJQeWkYwkw0Srhf3SYZi6teIxrCRMmw65eNh-echeIbYqM-UOCezEFrpNd3dSUIJzXYW7NT6IlIu8Wyng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37d6965b1.mp4?token=To6Ep0jvHnqg8KYz57TSKK8a1QMMfvJ6Ywo6JxfriBkFp5bhjbXbyZu43K-LNQhKXqdWyMnw-vO4zFxtgfxlEbJNhR1YIGiYK0dxxpFvrR0yfqYLHu9eJ2H4l-duCf0ZYfOWsWNCmpvc8777uHziUODh4I1xpbs2-8oU0PXm-H8xhA2ushpkPl5mVa6cmY46plABEUl61mBiNLZUOTmIU0DjIqD9ZC5tW4x9HKMNhyoZMh28P_t47kM0Hy6jx2ulsrXF2pJQeWkYwkw0Srhf3SYZi6teIxrCRMmw65eNh-echeIbYqM-UOCezEFrpNd3dSUIJzXYW7NT6IlIu8Wyng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
تشکر اعضای پرسپولیس از هواداران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139205" target="_blank">📅 21:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139204">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
🔴
💢
خلاصه بازی پرسپولیس ۳ - ملوان ۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/139204" target="_blank">📅 21:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139203">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
به به چه فوتبالی .چه پرسپولیسی ...سه گل زدیم و شش گل نزدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/139203" target="_blank">📅 21:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139202">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
تیم  دقیقه 98 هنوز تو حمله اس و تک به تک نمیزنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/139202" target="_blank">📅 21:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139201">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
تیم سه گل زده هنوز سرتاسر حمله و تشنه گلزنیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139201" target="_blank">📅 21:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139200">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
اورونوف هم تا اومد تو زمین ی پاس سکسی داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139200" target="_blank">📅 20:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139199">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
✅
بازیکن ملوان اومد تو زمین سلام کرد و بلافاصله اخراج شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139199" target="_blank">📅 20:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139198">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⚽
🤩
سیو تماشایی پیام نیازمند…
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139198" target="_blank">📅 20:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139196">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6343db8016.mp4?token=g6r2IqkP57OzZClA292RirUib41wIWAuj4Pss0YsTE9JBdTH0SgZMLEwn4HH4iLY0QFZijHjL3b8dMb_cZO0VKQLX8Ihk9x_xZXDITBafNIk8Xs-G7zF-pfeqMgz_N9tMq77DsqZ_xpx9dMyq6rr7-7QSezcA7CZ6xoBrm_qBlsbukuqV3qB_g0PFaXs8hefMrSM64KYN2Sv0I3uLiwlZr3hwAJJIDI4kiV5tUcrFnOawWe3K16IF7YoFI9Ajt3eVnUNSk28ue-rvnwygjwZY9_VgAxb9hslIjX_ogHqgCyw6A9X8501OKi6Yp4T_Ags0wInJqNOh_50cNNx8aBZ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6343db8016.mp4?token=g6r2IqkP57OzZClA292RirUib41wIWAuj4Pss0YsTE9JBdTH0SgZMLEwn4HH4iLY0QFZijHjL3b8dMb_cZO0VKQLX8Ihk9x_xZXDITBafNIk8Xs-G7zF-pfeqMgz_N9tMq77DsqZ_xpx9dMyq6rr7-7QSezcA7CZ6xoBrm_qBlsbukuqV3qB_g0PFaXs8hefMrSM64KYN2Sv0I3uLiwlZr3hwAJJIDI4kiV5tUcrFnOawWe3K16IF7YoFI9Ajt3eVnUNSk28ue-rvnwygjwZY9_VgAxb9hslIjX_ogHqgCyw6A9X8501OKi6Yp4T_Ags0wInJqNOh_50cNNx8aBZ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🤩
سیو تماشایی
پیام
نیازمند
…
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139196" target="_blank">📅 20:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139194">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df197fe84.mp4?token=gqWh_ncQz_FQfrtflIDYhCeGxbF-0Ke_JRRlM23ftAp8QAvFv-uGniuzutpeDwH1Ls1HkogYFVHRr5Tfwj7EBg8qAUQ3cLpiz5Q2sNXdv2uE2qGYrjssHXHvdoipkXeLEQvKoKH67wCLvJrhr03bFzU5Luw5xEAlv7Ts5XySRK4pY2wxWr-mFPiBs4IgTc7o7vA9DQSUhWewTjr280_K5BeSvWgKaxSKNIWY14L_ppEKaygzbl8BQHA47TRD2XAzffiQcUnSIwmx8VsCVNXggcHPxREatmioSvj5_k7lo2xPZuSd4JOj3hdK__CsRVNzsai9fSRn4J11WaszSWyvgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df197fe84.mp4?token=gqWh_ncQz_FQfrtflIDYhCeGxbF-0Ke_JRRlM23ftAp8QAvFv-uGniuzutpeDwH1Ls1HkogYFVHRr5Tfwj7EBg8qAUQ3cLpiz5Q2sNXdv2uE2qGYrjssHXHvdoipkXeLEQvKoKH67wCLvJrhr03bFzU5Luw5xEAlv7Ts5XySRK4pY2wxWr-mFPiBs4IgTc7o7vA9DQSUhWewTjr280_K5BeSvWgKaxSKNIWY14L_ppEKaygzbl8BQHA47TRD2XAzffiQcUnSIwmx8VsCVNXggcHPxREatmioSvj5_k7lo2xPZuSd4JOj3hdK__CsRVNzsai9fSRn4J11WaszSWyvgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🤩
گل سوم پرسپولیس توسط علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139194" target="_blank">📅 20:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139193">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
❌
نیمه دوم نکشیم عقب پیروزی پرگلی قبل دربی خواهیم داشت‌.......
✔️
✔️
اقای تارتار یاد بگیر اینجور شجاعانه بازی کردن رو تو بازیا بزرگ نشون بدی
✔️
✔️
همینجوری جلو استقلال بازی کنیم بدون ترس پر گل میبریمشون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/139193" target="_blank">📅 20:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139192">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
بریم برای نیمه دوم ...بریم برای زدن گل های بیشتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/139192" target="_blank">📅 20:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139191">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a9742c8c7.mp4?token=t7zW-j4T3z2PA263NzsWH39C9y8o8rT5WwjhfEUYf3wU2UUwFFFqWLijFLM-9etonWalyCLZTj2KpShwxyhKYrVA6nDeUYRA9_VvJMp-SMwyi5fQylAvDFj5jrqAZM6NUoblVzrifv-wKV5ArSp-FhttPWYt53ZkDBIFnoTSDay6fTs3nZ5jtESJ-iTOJ9k7s6cXuOHbX-cvg5r1xN6w-qCxptri2Xo02W3hYCghOvSdoSebX3Ib82fmRvM_zV9xwr1LIPyuvhEzs8qCwdSeHRNZ6STmZI18r6fZX96QWAoRy_rJKm3hjZmtuQF1NiTDCowa1xtefN_il26YhIwzdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a9742c8c7.mp4?token=t7zW-j4T3z2PA263NzsWH39C9y8o8rT5WwjhfEUYf3wU2UUwFFFqWLijFLM-9etonWalyCLZTj2KpShwxyhKYrVA6nDeUYRA9_VvJMp-SMwyi5fQylAvDFj5jrqAZM6NUoblVzrifv-wKV5ArSp-FhttPWYt53ZkDBIFnoTSDay6fTs3nZ5jtESJ-iTOJ9k7s6cXuOHbX-cvg5r1xN6w-qCxptri2Xo02W3hYCghOvSdoSebX3Ib82fmRvM_zV9xwr1LIPyuvhEzs8qCwdSeHRNZ6STmZI18r6fZX96QWAoRy_rJKm3hjZmtuQF1NiTDCowa1xtefN_il26YhIwzdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
علی علیپور موقعیت خوب پرسپولیس رو به بیرون زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/139191" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139190">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
دیدی خوب بازی کنی نتیجشو میبینی؟
✔️
کاش جلو ترتر اینجوری بازی میکردی آقای تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/139190" target="_blank">📅 20:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139189">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5adad84121.mp4?token=uixnVKll937FHSa48W4fAvWY-klxffgGiTgMo5GUp2FR12NXM3k2jQRHwvZLoFopzWsp12JJBYBDIxAhf9OJhh4YUTnk-dvPqU3IzI831OlOhAedkx4BdTsEDVjoMykLLx2-jOxBAZf1FmSx4E3SHUpeYVdbUB_49V2PvyMKbmsxhkte_nJB5HihQ5JocWCdabFZH-Bqlt10AcGQKK7hcDS5HhD3k8Oa8J4sdJitGVX6-seTb4tTb1b-PzpXZOdG4goHSgnDKKlMAr1PYjpA5CwyeIl6IderN5V0xVz3wD_AATFbbLnKSbsG3pigjd14p_KPf8yE91zZs4YI5p911w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5adad84121.mp4?token=uixnVKll937FHSa48W4fAvWY-klxffgGiTgMo5GUp2FR12NXM3k2jQRHwvZLoFopzWsp12JJBYBDIxAhf9OJhh4YUTnk-dvPqU3IzI831OlOhAedkx4BdTsEDVjoMykLLx2-jOxBAZf1FmSx4E3SHUpeYVdbUB_49V2PvyMKbmsxhkte_nJB5HihQ5JocWCdabFZH-Bqlt10AcGQKK7hcDS5HhD3k8Oa8J4sdJitGVX6-seTb4tTb1b-PzpXZOdG4goHSgnDKKlMAr1PYjpA5CwyeIl6IderN5V0xVz3wD_AATFbbLnKSbsG3pigjd14p_KPf8yE91zZs4YI5p911w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
در بین دو نیمه اورونوف از سوی طرفداران پرسپولیس به شدت تشویق شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/139189" target="_blank">📅 20:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139187">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">چرا باکیچ رو بازی نمیده حرومزاده کعیر تو گلگهر با بازیکناش</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/139187" target="_blank">📅 20:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139186">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پورعلی کلا وله بخدا باکیچ توانایی جمع کردن وسط زمینو دارت</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/139186" target="_blank">📅 20:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139185">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نظری ندارین که چرا از باکیچ بازی نمیگیره؟</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/139185" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139184">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b85faf30c.mp4?token=a4Xx5SJBLvpi7lsLMbF2eRLKGvKyd70ie1gBs2lblU1NhI7D_RKZDobZmxS9We8m1-WmlciF7XJuhijFKyJ00C-6pZ9bCzQByMrSIOvq5SyWQkBCoJXL2Sq3CRZ64OImBJCSv4scmLJRerLHaNkjxiNcW2r0O5q6dlW3yJ7tatjmJqwjuIWNNYZZL1uIo3n6-GD8auqvC9qpe5E4J5n82jBFefMYfNYhbgiv3pLkUvAysx3Q9ucbiW38leeMZE2RUoK8cZIHUNMIXdAG_Q9sQuXroGCKK3QJhaE7RpkiSotc-JMZRrNH5bsZVNKrBEsblhqar7n9lfDJQTANADAqUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b85faf30c.mp4?token=a4Xx5SJBLvpi7lsLMbF2eRLKGvKyd70ie1gBs2lblU1NhI7D_RKZDobZmxS9We8m1-WmlciF7XJuhijFKyJ00C-6pZ9bCzQByMrSIOvq5SyWQkBCoJXL2Sq3CRZ64OImBJCSv4scmLJRerLHaNkjxiNcW2r0O5q6dlW3yJ7tatjmJqwjuIWNNYZZL1uIo3n6-GD8auqvC9qpe5E4J5n82jBFefMYfNYhbgiv3pLkUvAysx3Q9ucbiW38leeMZE2RUoK8cZIHUNMIXdAG_Q9sQuXroGCKK3QJhaE7RpkiSotc-JMZRrNH5bsZVNKrBEsblhqar7n9lfDJQTANADAqUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
مهدی تارتار و کریم باقری از گل انفرادی بیفوما به وجد آمدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/139184" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139183">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝙖𝙢𝙞𝙧</strong></div>
<div class="tg-text">چرا باکیچ رو بازی نمیده حرومزاده کعیر تو گلگهر با بازیکناش</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/139183" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139182">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSana</strong></div>
<div class="tg-text">پورعلی کلا وله بخدا باکیچ توانایی جمع کردن وسط زمینو دارت</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/139182" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139181">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSahand</strong></div>
<div class="tg-text">نظری ندارین که چرا از باکیچ بازی نمیگیره؟</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/139181" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139180">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">📌
وسط وله…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/139180" target="_blank">📅 20:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139179">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">📌
وسط وله…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/139179" target="_blank">📅 20:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139178">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
دیدی خوب بازی کنی نتیجشو میبینی؟
✔️
کاش جلو ترتر اینجوری بازی میکردی آقای تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/139178" target="_blank">📅 20:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139177">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HphTlPMzazaQoB-ezJVU7BWtCa9DJ8p6So9aGAmWPkYk0qFtP_Qh0hDk5IIqu56jxbUknyjApnEw7PhhridPS5WAdtxXB0F4EgehtqEAAu_O9pMFvu-QjlCDBWvbLjHFbX5R9mGwHObEz20vZBgizVVXVXKpvYzz0QG9kfba2HF5Sqs_QitkAOOmcNP0r93OJSO2cl5QzqmXLs1tS0EeTncn--SL9zEX_kVqH1d-yZ-N1z9IIbizLL06U7_7n6kDLSVJxC6KaS9xBKPcsd_S68sMqJAD4DnZ5AFvZEo3hyhJ6y8RC6onKQ7nnUA6m9H_qkVuRoAhSFjC148u2WlWog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
دیدی خوب بازی کنی نتیجشو میبینی؟
✔️
کاش جلو ترتر اینجوری بازی میکردی آقای تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/139177" target="_blank">📅 20:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139176">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ls9rTy3rP-Ke6TIf31X3x-wQlOxzxr9uGFpxd3yczWXJ_p_WEbJeBgAUuOEEsV23bzBmAKr3k5kG26QeGx1wC7zjsT7JXosWPgJdUmXA4w2W5kyS6c2Be_JiU8cyYl8fA3lOop6UlV7e7RtTJpkpFAsMm6M18i8LSNLI_X1jA-04gvcpiY2Z1fWMYg2It9GRfnBPMbtCqAgJ4XFoDWdlvBCsDcc_ykhLlsDjv8t3f1W4m-Ei7IeRUA__RuObRWRBUhNKLrW8_gjaYELvJw-bkZHGi4dDK0xOXmRcS6soHpi_fdIgZsIUxqCi7SFPZoMPh048NK3vBuJVF-7SXu0B9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یووه در تورین دنبال دومین برد فصل؛ پارما هم برای جبران شکست هفته اول آمده!
برتری کیفیت و امتیاز میزبانی با یوونتوس است، اما غیبت ییلدیز می‌تواند کار را کمی سخت کند.
نبردی که بوی برد یووه می‌دهد؛ اما پارما می‌تواند برای مدعی دردسرساز شود
[
یوونتوس
⚽️
🆚
⚽️
پارما
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/139176" target="_blank">📅 20:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139175">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
پایان بازی در نیمه نخست
⚪️
پرسپولیس دو - ملوان صفر
⚽️
گل‌ها: محمد پاپی(گل‌به‌خودی)، بیفوما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/139175" target="_blank">📅 20:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139174">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
❌
خداییش دو تا زدیم سه تا نزدیم .عجب تیمی ..چه استارت هایی چه ضد حمله هایی ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/139174" target="_blank">📅 20:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139173">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
✔️
همچنان معتقدم برای این تیم باید کلاه از روی سر برداشت و با این پرسپولیس باید با احترام حرف زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/139173" target="_blank">📅 20:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139172">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63de6c0cf7.mp4?token=WrtJddkFIpE8iKsEzlY4PlsxWxKmR3TW7FQ6IKFu33n_l4D2qu1Rv9fKFGOzewaYUgILppLaPepd5Yue6XgXByK87_vhRv5kwJAE9phbNpTt4fKF_ETubqlK7-RFD8Ygp4wOgx_df6DMqvfk7Yaz1b8d_Meu_RSPUcRQyqHuseQ-eEpNxPN5cx0WGcl4lU8bCq2AgO-qwiqKiUbaCm0pieo0QVRRo4jfvdv73sb1PU66z1DqJTdMyuNW2ouVx6oCE7tH1wZDSBlHb3e82c9ekhe_BAtxHwX0mvMWRd3PibZS7ERe67NB4ICcLhgFUEt-z7MIwAHGdgE6Bz9-I9mifUQMVhsmm76N9-AN1DTCOkIm7QfXLLNHxHKpTwT8gPV0B_dN1DQwWEyONNbrJv30WqX8-tyRoAIykooIZBVFPSY7nApLirNukCzqfiuX4N08udeISM2sy9bHUgc6s3atnejEaCan33QBQNryoUWwfpU010m2Bf6tmU_r7vft_9KTC_R9nUpN2MZ7gPC0uAWVDngTeLt7QBV_pCLK-2G5D9wpnH-idCPy5UpDjJK5g5jGTAS3gW8obbhjDEKSWqKykhHMn4w2QUQyjftqjs5iCRFNAycOp1hYI0QjyjkSc-WgS_Em7IHSWb8b2EvaaiaObSwdutwXPHjEoia3IS5WmCY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63de6c0cf7.mp4?token=WrtJddkFIpE8iKsEzlY4PlsxWxKmR3TW7FQ6IKFu33n_l4D2qu1Rv9fKFGOzewaYUgILppLaPepd5Yue6XgXByK87_vhRv5kwJAE9phbNpTt4fKF_ETubqlK7-RFD8Ygp4wOgx_df6DMqvfk7Yaz1b8d_Meu_RSPUcRQyqHuseQ-eEpNxPN5cx0WGcl4lU8bCq2AgO-qwiqKiUbaCm0pieo0QVRRo4jfvdv73sb1PU66z1DqJTdMyuNW2ouVx6oCE7tH1wZDSBlHb3e82c9ekhe_BAtxHwX0mvMWRd3PibZS7ERe67NB4ICcLhgFUEt-z7MIwAHGdgE6Bz9-I9mifUQMVhsmm76N9-AN1DTCOkIm7QfXLLNHxHKpTwT8gPV0B_dN1DQwWEyONNbrJv30WqX8-tyRoAIykooIZBVFPSY7nApLirNukCzqfiuX4N08udeISM2sy9bHUgc6s3atnejEaCan33QBQNryoUWwfpU010m2Bf6tmU_r7vft_9KTC_R9nUpN2MZ7gPC0uAWVDngTeLt7QBV_pCLK-2G5D9wpnH-idCPy5UpDjJK5g5jGTAS3gW8obbhjDEKSWqKykhHMn4w2QUQyjftqjs5iCRFNAycOp1hYI0QjyjkSc-WgS_Em7IHSWb8b2EvaaiaObSwdutwXPHjEoia3IS5WmCY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🎥
گل دوم پرسپولیس به ملوان ..استارت انفجاری و برق آسا از بیفوما
✔️
توسط بیفوما 33
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/139172" target="_blank">📅 19:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139171">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
همچنان معتقدم برای این تیم باید کلاه از روی سر برداشت و با این پرسپولیس باید با احترام حرف زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/139171" target="_blank">📅 19:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139170">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
همگی باید کلاه از روی سر برداریم و ایستاده این تیم و تشویق کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/139170" target="_blank">📅 19:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139169">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJSbBb-cn0cTUn_FPJ2mkAdLzlCV00-T_aaLrbP60hIzLxHCtN2Z9t1eE17t25sBOBPAGtJgPUTE_T2TYKs7iIyzOvh4JkPPvqT-eRsILOxZHHFS4JfzdWpnbrt9Hs9CrF_VjyAISlLUbPDhDlPfA6A8eqkCP0kBdgzVFcpCrE_YdYpnE6UuZuV7-eBOh9bxxk3_XV0vTL3xfeXlPAxyQUiEaSDRaLthxf2_Y82wsp36XZMF1TSUn6mbqbpkIa_NH7vub_4egkFRB0EksDj9tXlqEgnyakRrVX71ZquffZXbrCvgC2CHZgOkCwcHJTYGJz-9w4nl1FXeRbAPqzyc8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
ورود کاروان پرسپولیس به ورزشگاه شهدای شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139169" target="_blank">📅 18:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139168">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78df0f8e05.mp4?token=XRmiRO2sbB7bqPKLlc4fjUJst0iaC-Xhvry7HO3681-NLigmGGBpGNLiB18KaRHjqTy8-1BlsEq2lJ5DeJ_WS3ziWnn8BVZnuJNz-dd16F2JgMH-mJoYT7G-jxPO2KdrZ8FC-BLCsa9m4hpyOfp7onN0lun49IsU-ehijWJ2U4uC-Yg0JXmKgfh36CX23W7PCYUEo5L3ubZGZMYtOMKMHl4xZLbc4EtXdoGxFAsFF_3yjnQWp3phpHOqNSmMp1ogOhVJJxjn4E07cGvwzfpZijbJpiwFJtMZLwrwSc1H75tjWC_zWHQUJARJuw3rsbNTFsdUpcwW2zY3mNNxG6PJrxj6Ks72_3dNs73g7sgV9H-MfvCrfSOsVQ5ZyV44pcvztb-mDI_Q7YAg_m0NOmow5j4oFk3ikeck1zX7patjxe3IATE-bTpcVsNXL72K3lwIV_wl3-YkrWvxHhPwegTudqWXxoY94tA3dMqKCFWry3MeHpZVK_ldEtwSx7nefARYAyyD8QmrwrPh3p3EozqGL7qOc8Ucko1ufMN8tktRYIQylp2HryVMomiyoFhfJkH1SQfsdyBd_Z0a5cSEkT39NYluwHJkfJ7t9uaSXGlUeSHo7CkJtQXBkF9YbkjZxrWYVwGf4F0ykWaVL0DURz93iXsts62KYAuh4liRvJVpHH4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78df0f8e05.mp4?token=XRmiRO2sbB7bqPKLlc4fjUJst0iaC-Xhvry7HO3681-NLigmGGBpGNLiB18KaRHjqTy8-1BlsEq2lJ5DeJ_WS3ziWnn8BVZnuJNz-dd16F2JgMH-mJoYT7G-jxPO2KdrZ8FC-BLCsa9m4hpyOfp7onN0lun49IsU-ehijWJ2U4uC-Yg0JXmKgfh36CX23W7PCYUEo5L3ubZGZMYtOMKMHl4xZLbc4EtXdoGxFAsFF_3yjnQWp3phpHOqNSmMp1ogOhVJJxjn4E07cGvwzfpZijbJpiwFJtMZLwrwSc1H75tjWC_zWHQUJARJuw3rsbNTFsdUpcwW2zY3mNNxG6PJrxj6Ks72_3dNs73g7sgV9H-MfvCrfSOsVQ5ZyV44pcvztb-mDI_Q7YAg_m0NOmow5j4oFk3ikeck1zX7patjxe3IATE-bTpcVsNXL72K3lwIV_wl3-YkrWvxHhPwegTudqWXxoY94tA3dMqKCFWry3MeHpZVK_ldEtwSx7nefARYAyyD8QmrwrPh3p3EozqGL7qOc8Ucko1ufMN8tktRYIQylp2HryVMomiyoFhfJkH1SQfsdyBd_Z0a5cSEkT39NYluwHJkfJ7t9uaSXGlUeSHo7CkJtQXBkF9YbkjZxrWYVwGf4F0ykWaVL0DURz93iXsts62KYAuh4liRvJVpHH4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
ورود کاروان پرسپولیس به ورزشگاه شهدای شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/139168" target="_blank">📅 18:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139167">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/153ca3a7ea.mp4?token=sy3J8aUvpRe4_Unj2oC7_LymdPAoWUDeviuXYzYZdWm-AcoLE__6porC8iE6S6p58Gvkzu_ZIDK0VFGLrhpzaLfWUmEu2P9PlD7Y4_MKjqQdMe6uVsTFKBIPXmIWSjy3Zlsr-ZJrIW7pfQjMDtHrtwQfTnbQ-8O9m2Ud2SvWLEUumFobyx_CdFM5uCUNC5dN36uRlsN6y1fXAOm48S6gl4JyCrzR_aPwjJSOz-OiRDjZR1GSfK4IsaHVslcLJF6FudYK8W2e4ffc5VLEr5GrrS6a2fNMyDCI-8wB3ChGctoUdvMSPsa-RjjVKiZ5-nlx378WVE50q-woIEgOwr2q-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/153ca3a7ea.mp4?token=sy3J8aUvpRe4_Unj2oC7_LymdPAoWUDeviuXYzYZdWm-AcoLE__6porC8iE6S6p58Gvkzu_ZIDK0VFGLrhpzaLfWUmEu2P9PlD7Y4_MKjqQdMe6uVsTFKBIPXmIWSjy3Zlsr-ZJrIW7pfQjMDtHrtwQfTnbQ-8O9m2Ud2SvWLEUumFobyx_CdFM5uCUNC5dN36uRlsN6y1fXAOm48S6gl4JyCrzR_aPwjJSOz-OiRDjZR1GSfK4IsaHVslcLJF6FudYK8W2e4ffc5VLEr5GrrS6a2fNMyDCI-8wB3ChGctoUdvMSPsa-RjjVKiZ5-nlx378WVE50q-woIEgOwr2q-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کری سنگین هوادار پرسپولیس: آخرین باری که استقلال دربی رو برد دلار ٣۵٠٠ بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/139167" target="_blank">📅 18:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139166">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c76c3af39e.mp4?token=R9VE3DAjPcvXmWA3i000pv50IgeZRj2UaqGc8Vv1aYHtquXEjireEO1oGPA1xlXbUm20xiULptclLr7cEceVwxi2RjnVkgiv3O1oDdXYnHZv7ozcoCLc0z4NOf4pFznxEGdN0qinNyGQ3e2ZMk9mIJBLAaqOg6SCmWLksz1igr2dM7NVdO_DcfUWUYSVLWaveV4DGTgadML5iroP8yhK5wuc_K6fSMs8uK66HjOSnPWl3LdLef7WY4bDDiuPnownSxZz0lDtGi4cvlYbj3xvKuhnkGqYINIZp1vx8SIcaEn3FbmlIAQfPFuwp-toD9HL95p59anDwLqfAWpZUfFZtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c76c3af39e.mp4?token=R9VE3DAjPcvXmWA3i000pv50IgeZRj2UaqGc8Vv1aYHtquXEjireEO1oGPA1xlXbUm20xiULptclLr7cEceVwxi2RjnVkgiv3O1oDdXYnHZv7ozcoCLc0z4NOf4pFznxEGdN0qinNyGQ3e2ZMk9mIJBLAaqOg6SCmWLksz1igr2dM7NVdO_DcfUWUYSVLWaveV4DGTgadML5iroP8yhK5wuc_K6fSMs8uK66HjOSnPWl3LdLef7WY4bDDiuPnownSxZz0lDtGi4cvlYbj3xvKuhnkGqYINIZp1vx8SIcaEn3FbmlIAQfPFuwp-toD9HL95p59anDwLqfAWpZUfFZtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
⚽
ورود طرفداران پرسپولیس به استادیوم شهدای شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/139166" target="_blank">📅 18:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139165">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76152fe425.mp4?token=fpy7XaOR1G-50qPA7Xp43NpObxQikwxy-MSmWts7ZDJI9SVYkc0jExdm46fUlNfUCdzqHz6J5tCbgEeNuDso80AaeH3us82DCGhqC23JJDoGJsPFjg4xR2BX-Os3QF2afYhTEK5ULcg6m5GjhWij4oh4rzs_7OefjP7c6IwO20B5KdVeeTB_bB1WA-D56-lbn_oDA3S8D08iMeIkXCdWWA7d5cFj_UbM-6hyUVWZHk-TUvjjl7Y2ZOx1wF1d1A7DTaS-kU-Qtu7JDuC5RAFcPpaGO6Ysvqcf_K231mB8qyi9zIOhbjBt5DVJAGKgeXUy9nwHJyxhinoBHhhEotUXGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76152fe425.mp4?token=fpy7XaOR1G-50qPA7Xp43NpObxQikwxy-MSmWts7ZDJI9SVYkc0jExdm46fUlNfUCdzqHz6J5tCbgEeNuDso80AaeH3us82DCGhqC23JJDoGJsPFjg4xR2BX-Os3QF2afYhTEK5ULcg6m5GjhWij4oh4rzs_7OefjP7c6IwO20B5KdVeeTB_bB1WA-D56-lbn_oDA3S8D08iMeIkXCdWWA7d5cFj_UbM-6hyUVWZHk-TUvjjl7Y2ZOx1wF1d1A7DTaS-kU-Qtu7JDuC5RAFcPpaGO6Ysvqcf_K231mB8qyi9zIOhbjBt5DVJAGKgeXUy9nwHJyxhinoBHhhEotUXGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
روش جدید ورود هواداران به ورزشگاه شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/139165" target="_blank">📅 18:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139164">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95e62021f.mp4?token=FjxueTgpbxRmmsVXrKh2ru7yK2sz6GCvQsXrK8q-Gz1VebMsybeXiQBUGSpcJI5cz-cXpIQPojVZozkx2JYHAaJkAOy0yfWCKrcFyXu8LCpTaDm0CcmplmVwldcVTDz26AfecgIeVhhaA49vi55_5ZZ2_5oonAwLQFeM6zNUm3b__KK9CBikkxKK5hTS7AsVMrUsCTyK_S-hpmuTJO4FYFXS04m-AGXlnBOriMP-Mn2A9HwIb_nsrDGhAdSdVXFgLX9eyviMlNng2KWEPt-deUzP4bd62jc8UAa5A8UjipcsIoYoLnElifCsU2e_BeczJ1A3uLWkbOBJx1UeyIm8eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95e62021f.mp4?token=FjxueTgpbxRmmsVXrKh2ru7yK2sz6GCvQsXrK8q-Gz1VebMsybeXiQBUGSpcJI5cz-cXpIQPojVZozkx2JYHAaJkAOy0yfWCKrcFyXu8LCpTaDm0CcmplmVwldcVTDz26AfecgIeVhhaA49vi55_5ZZ2_5oonAwLQFeM6zNUm3b__KK9CBikkxKK5hTS7AsVMrUsCTyK_S-hpmuTJO4FYFXS04m-AGXlnBOriMP-Mn2A9HwIb_nsrDGhAdSdVXFgLX9eyviMlNng2KWEPt-deUzP4bd62jc8UAa5A8UjipcsIoYoLnElifCsU2e_BeczJ1A3uLWkbOBJx1UeyIm8eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
چمن ورزشگاه قلعه‌حسن‌خان کوتاه و آماده میزبانی از دیدار پرسپولیس و ملوان است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/139164" target="_blank">📅 17:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139163">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
کلیپ باشگاه برای بازی امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/139163" target="_blank">📅 17:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139162">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
🎙
روشنک مسئول مسابقات لیگ برتر:
✔️
✔️
شاید جام حذفی را امسال نتوانیم برگزار کنیم، هدفمان این نیست ولی شما ببنید چقدر امسال برنامه‌ها فشرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/139162" target="_blank">📅 16:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139161">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5fbb7cadc.mp4?token=sUerFUbpbX5xc5-F-XnEMd37VXYXVo2mZFDCrzE8GJyd5P6CYKQ7UKnfvcGrOa-K0vK3gNDzrFuPcyG5nh6Y4CSeLe0Oxu3uq4ZYvVx7Ei6Ol1yiILrlN0gj-uwBX-ul3yGAG7kYLHtn02L8K-UCuF7yrcmuDlrdalp6oS9WJitslXAmTxiT8TptIanUkTxVhQBsLtlUz_6cFrQLJTQ6jKyns0lHwwd4M0gp8Ijn9GCCC9CClSD37Mf4INEiopP0PmfNP4_HNULSSeP_hUoaakUr5RT_noaRJZU_Xj9WYR42yuBHtyv0pB6aaRpMQjBR8LXZjYqL1HdRiNFEAERYbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5fbb7cadc.mp4?token=sUerFUbpbX5xc5-F-XnEMd37VXYXVo2mZFDCrzE8GJyd5P6CYKQ7UKnfvcGrOa-K0vK3gNDzrFuPcyG5nh6Y4CSeLe0Oxu3uq4ZYvVx7Ei6Ol1yiILrlN0gj-uwBX-ul3yGAG7kYLHtn02L8K-UCuF7yrcmuDlrdalp6oS9WJitslXAmTxiT8TptIanUkTxVhQBsLtlUz_6cFrQLJTQ6jKyns0lHwwd4M0gp8Ijn9GCCC9CClSD37Mf4INEiopP0PmfNP4_HNULSSeP_hUoaakUr5RT_noaRJZU_Xj9WYR42yuBHtyv0pB6aaRpMQjBR8LXZjYqL1HdRiNFEAERYbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
▶️
این وسط یهو یاد برد ۳بر۰ پرسپولیس جلوی نسف قارشی ازبکستان افتادم، جهنم آزادی، پرسپولیس مخوف و گادوین منشا ‌بی‌رحم
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139161" target="_blank">📅 15:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139160">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
باشگاه فولاد امروز بار دیگر تمام پیشنهادات پرسپولیس برای جذب رزاق پور را رد کرد و این بازیکن در فولاد ماندنی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139160" target="_blank">📅 15:51 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
