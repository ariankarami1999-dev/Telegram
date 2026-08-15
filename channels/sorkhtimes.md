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
<img src="https://cdn4.telesco.pe/file/ZyQ-8UIjjarU2Dpxih-D7j1gGTPTuTe6Fuhg8MCLkiZ0GIikuuPjQsAmEM7YeOJqqRQ63sgLxqAIR7HbjJ3P79a17iStAv1RPfDiKsaA59qiB5Rfo4MUYNSGuwOH7IP90cm53dE58GZPXOCSgnNB1S9Uxqe4BS2EpyINrsIDr35knl3zNzGy_MOz-lYGihIdLMZCOmsoZDN5BCDYFdT52PeEkjsa7URGXgRfds5b4hNlCo7Ftvpv-glw16Jc2ancNiwuTMxPyJk-LuPP1AXk6WLQuzWb44jxU_DwdGFLAfmiySV7op_wy2RT8hN1Y5QSKQvwIx88wjR0M36h2EraKw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 21:45:18</div>
<hr>

<div class="tg-post" id="msg-138253">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
دکتر پیمان هنوز مونده تو استودیو فوتبال و تکون نخورده   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 700 · <a href="https://t.me/SorkhTimes/138253" target="_blank">📅 21:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138252">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✖️
✖️
واقعا بازیکن بد نداشته امروز پرسپولیس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/SorkhTimes/138252" target="_blank">📅 21:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138251">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✖️
✖️
واقعا بازیکن بد نداشته امروز پرسپولیس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SorkhTimes/138251" target="_blank">📅 21:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138250">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‼️
بریم برای نیمه دوم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SorkhTimes/138250" target="_blank">📅 21:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138249">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
نیمه دوم هر کی بیاریم داخل..‌ بازی و در میاره راحت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SorkhTimes/138249" target="_blank">📅 21:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138247">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fF4tgCNN6qAiW0oNr1NFWDkuZig4h0Kdr719K8NdqIRfL6wchIp82s1ENaI1uLTkwJMuO7jxi1yRx4lx0Rp08qanLWRJecY9srBmGs8jGHcrBepDUA_tqWiA2Yvi56YMUrCNqt3dvkilZLFKX1ErmmlCgpXPTF5zWC2UmQUneKsYe2ITnyedT0k5k_bERDdvGJPQbPnvclr0ruexY0uqlBYZQiAfvTPmYD83NWNFL4E2mfEkbBhr0YJlPq7Zr21lsmSVVouhd_fQPlDfVLMpNuTcddPluBb2qMha4xJoTHTQ5HcS5j0BaU7syxTzqgHQZ9JbFzha2lSeHm4K21g6Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرسپولیس؛ آماده برای شکار شمس‌آذر!
🔴
Persepolis -
🟢
ShamsAzar
🔵
لیگ خلیج فارس
⏰
شنبه ساعت ۱۹:۳۰
🏟
استادیوم سردار آزادگان
📌
فقط تماشاگر نباش؛ همین حالا وارد مینی‌اپ وینکوبت شو و با اولین شارژ خود و دریافت ۱۰٪ بونوس ویژه این دیدار رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SorkhTimes/138247" target="_blank">📅 20:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138246">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">هواداران اگه امسال قهرمانی می‌خوایم برین پست آخر پیج بانک شهر و پست آخر پیج پرسپولیس :
👈
جذب محمد قربانی
👈
اخراج اینانلو
👈
اخراج احد میرزایی  ( اینانلو و میرزایی ۲ مهره ضد پرسپولیسی هستند که مانع تقویت پرسپولیس می‌شوند و حضورشون سم مطلق است )</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SorkhTimes/138246" target="_blank">📅 20:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138245">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
دکتر پیمان هنوز مونده تو استودیو فوتبال و تکون نخورده   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SorkhTimes/138245" target="_blank">📅 20:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138244">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
پیمان حدادی: در حال مذاکره برای جذب محمد قربانی هستیم و برای جذبش دغدغه مالی نداریم ولی بعید می‌دونم الوحده فروشنده باشه چون هنوز قیمت ندادن و شاید قربانی تمدید کنه!   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SorkhTimes/138244" target="_blank">📅 20:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138243">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736ad661da.mp4?token=GVK1tHUlX_1ILO-0xXqlddJMMB0GfUDJA7r1_mAKP2TiB_wyV1sRNDK701KqphzDaVq_oYVIDn83qVq3vEwDDK5gXS9Ch-pTWvxsSGAxSR87RG094-Erzxaha9t-CkAvn4Z03Kri4ObswzDQix2IyOKWzSl3imVOTzdhdVgmKXDGxwl2kuHfUF_MSyQ35FRE0hCUS6XD_JtPo9CH2PWONzcDuTzTGKv-ukgmR8MTM30BNokfxChjlLQFEBnBwKkkYxIiBORbfUbhZsfmXgzOWMuD8KPsgh-ZIsfAroVrxNeymbbMNaSwem2LYu1dC8Shvaa8RxM5RrZiS12j8llJFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736ad661da.mp4?token=GVK1tHUlX_1ILO-0xXqlddJMMB0GfUDJA7r1_mAKP2TiB_wyV1sRNDK701KqphzDaVq_oYVIDn83qVq3vEwDDK5gXS9Ch-pTWvxsSGAxSR87RG094-Erzxaha9t-CkAvn4Z03Kri4ObswzDQix2IyOKWzSl3imVOTzdhdVgmKXDGxwl2kuHfUF_MSyQ35FRE0hCUS6XD_JtPo9CH2PWONzcDuTzTGKv-ukgmR8MTM30BNokfxChjlLQFEBnBwKkkYxIiBORbfUbhZsfmXgzOWMuD8KPsgh-ZIsfAroVrxNeymbbMNaSwem2LYu1dC8Shvaa8RxM5RrZiS12j8llJFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#
منهای_پرسپولیس
☑️
گل اول صنعت نفت آبادان به ملوان (اولین سوپر گل لیگ امسال
♦️
صنعت نفت آبادان  یک - صفر ملوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/138243" target="_blank">📅 20:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138242">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✖️
✖️
یازده تای اون زمین کی هستن که اینا نیمکتن
😂
:
✔️
رفیعی
✔️
ابرقویی
✔️
تیکدری
✔️
اورونوف
✔️
شهرآبادی
✔️
سرگیف
✔️
باکیچ
✔️
لطیفی فر
✔️
محمودی
✔️
همایی فرد
✔️
سلمانی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SorkhTimes/138242" target="_blank">📅 20:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138241">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
بهترین بازیکن نیمه اول از نظر شما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/138241" target="_blank">📅 20:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138240">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
خوشگل میشه به این تیم امید داشت و امیدوار بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/138240" target="_blank">📅 20:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138239">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
تیم سرحال نشون داده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/138239" target="_blank">📅 20:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138238">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">⚡️
⚡️
شنیده میشه تیوی بیفوما در یک ماه اخیر برای ماندن در پرسپولیس زیر نظر پزشک تغذیه باشگاه 8 کیلو کاهش وزن داشته و علاوه بر اون زندگی حرفه ای شو سالم تر از قبل کرده و تمرکز اصلی شو روی فوتبال خودش گذاشته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/138238" target="_blank">📅 20:07 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138237">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
❌
✖️
جونم به این تیم ..چه تیم شادابی درست کرده تارتار  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/138237" target="_blank">📅 19:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138236">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✖️
✖️
دو گل تو بیست دقیقه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/138236" target="_blank">📅 19:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138234">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
بریم برای اولین بازی فصل با تارتار .الهی به امید تو   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/138234" target="_blank">📅 19:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138233">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
بریم برای اولین بازی فصل با تارتار .الهی به امید تو   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/138233" target="_blank">📅 19:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138232">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
شماتیک ترکیب پرسپولیس برابر شمس‌آذر  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/138232" target="_blank">📅 19:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138231">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
در سیاست کاری ما نبود از یک سن بیشتر بازیکن جذب کنیم. عدد درخواستی او از پرسپولیس کمتر از سایر باشگاه‌ها بود ولی از سقف ما خیلی بالاتر بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/138231" target="_blank">📅 19:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138230">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
واکنش حدادی به شایعه حضور محمد قربانی در پرسپولیس؛ حضور او به احتمال زیاد منتفی است و با الوحده تمدید می‌کند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/138230" target="_blank">📅 19:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138229">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
در سیاست کاری ما نبود از یک سن بیشتر بازیکن جذب کنیم. عدد درخواستی او از پرسپولیس کمتر از سایر باشگاه‌ها بود ولی از سقف ما خیلی بالاتر بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/138229" target="_blank">📅 19:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138228">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
فووووری از پیمان حدادی: با رامین رضاییان مذاکره کردیم، تخفیف خوبی داده، انگیزه داره برگرده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/138228" target="_blank">📅 19:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138227">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
حدادی : رامین خیلی انگیزه داره بیاد پرسپولیس‌  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/138227" target="_blank">📅 19:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138226">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9f6013dab.mp4?token=di3dyv6Tl-2Ra_YrzMBrfYWk-M91eCCAYLG0NW9SfQ3JLJD2WHth8eL7g0RpaMcP_hwbw2y9YikhjL2D4-StKOvZtVEhHWmjMSoqLORb9-SgNK1uWV78dHu-k2mSqw-s-h5unJsSPrekkNoZdzUQxSDhnarD8tEtViPUu5ij7F_k1YuGmmSsu1lEbtn8d9nHIYNGlhSwIDa8n1caktWToSmOOCo99NKwzNd2v-P51TEpHwf2HiPU4SEj9P-JQ2VwBoRd3cDj6vlJZhjbgHWC_dyXkSztbZOJGyN_jA3HId6bDP4B2oqpBALD6WQJM36xrkvuUCp08bokYsk-sbNfxpDtCpVQec1JFsHSWlQg9gesBbRIEr8uuxJ0AqQh1UNMTewEWkKJb-DSH_uNydfMzDrBS5AMln3oVM71hZRJK5HS5KcBmmnOObPCR5vyZ4eDk3q26ykaoi63o3AMs8h-HfHp6ESKiztULhUSCIcWRiQHsdW5lO-LFgi1sBepCZyuPVz-M-NTwFikOlid1v27vSaLQpNEm3YrZSGzFemZ201hhrGYEcHjLbK3flTbkP6ROAbpVQ-RsqReHIadPj9WoxK3CtX4nMl3VlhZN3tUoCAI-nTbiypawRHWIA6ohNZqjOa0xSFU1QQa30VD0KUMGrGSPalhgfwpgiY1eMDTu2k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9f6013dab.mp4?token=di3dyv6Tl-2Ra_YrzMBrfYWk-M91eCCAYLG0NW9SfQ3JLJD2WHth8eL7g0RpaMcP_hwbw2y9YikhjL2D4-StKOvZtVEhHWmjMSoqLORb9-SgNK1uWV78dHu-k2mSqw-s-h5unJsSPrekkNoZdzUQxSDhnarD8tEtViPUu5ij7F_k1YuGmmSsu1lEbtn8d9nHIYNGlhSwIDa8n1caktWToSmOOCo99NKwzNd2v-P51TEpHwf2HiPU4SEj9P-JQ2VwBoRd3cDj6vlJZhjbgHWC_dyXkSztbZOJGyN_jA3HId6bDP4B2oqpBALD6WQJM36xrkvuUCp08bokYsk-sbNfxpDtCpVQec1JFsHSWlQg9gesBbRIEr8uuxJ0AqQh1UNMTewEWkKJb-DSH_uNydfMzDrBS5AMln3oVM71hZRJK5HS5KcBmmnOObPCR5vyZ4eDk3q26ykaoi63o3AMs8h-HfHp6ESKiztULhUSCIcWRiQHsdW5lO-LFgi1sBepCZyuPVz-M-NTwFikOlid1v27vSaLQpNEm3YrZSGzFemZ201hhrGYEcHjLbK3flTbkP6ROAbpVQ-RsqReHIadPj9WoxK3CtX4nMl3VlhZN3tUoCAI-nTbiypawRHWIA6ohNZqjOa0xSFU1QQa30VD0KUMGrGSPalhgfwpgiY1eMDTu2k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
واکنش حدادی به شایعه حضور محمد قربانی در پرسپولیس؛ حضور او به احتمال زیاد منتفی است و با الوحده تمدید می‌کند
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/138226" target="_blank">📅 19:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138225">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
حدادی: صادقانه با رامین خودم مذاکره کردیم ولی خب چون سنش بالاست و اینکه با تخفیف بالایی داده هنوز رقمش بالاست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/138225" target="_blank">📅 19:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138224">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
حدادی:تکلیف قربانی رو باشگاهش مشخص می‌کنه ولی بعیده باشگاهش بفروشتش   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/138224" target="_blank">📅 19:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138223">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
حدادی: درحال مذاکره هستیم با قربانی اما بعیده باشگاه الوحده قربانی رو قرضی یا قطعی بده
😑
😑
😑
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/138223" target="_blank">📅 19:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138222">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
پیمان حدادی: شفاف بگویم بازیکنان جوان را می‌خریم که رقبا نتوانند بگیرند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/138222" target="_blank">📅 19:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138221">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
پیمان حدادی : امیر جعفری دفاع چپ گل گهر در لیست خرید ما نیست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/138221" target="_blank">📅 18:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138220">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
درصورت تایید مهدی تارتار طی 24 ساعت آینده امیر جعفری مدافع چپ 25 ساله گلگهر سیرجان به پرسپولیس خواهد پیوست.
❌
❌
تمامی توافقات با این بازیکن و گل‌گهر سیرجان توسط مدیریت پرسپولیس انجام شده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/138220" target="_blank">📅 18:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138218">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
✅
✅
حدادی: ۵۰۰ میلیارد تومن برای شهرآبادی، محبی، زارع ، اژدهاکش، لطیفی فر و ایری رضایت نامه دادم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/138218" target="_blank">📅 18:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138217">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
حدادی: کسری طاهری رو نیم فصل میگیرم اگه نره سپاهان   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/138217" target="_blank">📅 18:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138216">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
فوووووری
✔️
✔️
حدادی:  به روبین کازان برای کسری نامه زدیم به ما گفتن ۱ میلیون دلار + ۲۰ درصد حق ترانسفر بازیکن و ما رفتیم شهرآبادی رو خریدیم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/138216" target="_blank">📅 18:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138215">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✖️
✖️
یازده تای اون زمین کی هستن که اینا نیمکتن
😂
:
✔️
رفیعی
✔️
ابرقویی
✔️
تیکدری
✔️
اورونوف
✔️
شهرآبادی
✔️
سرگیف
✔️
باکیچ
✔️
لطیفی فر
✔️
محمودی
✔️
همایی فرد
✔️
سلمانی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/138215" target="_blank">📅 18:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138214">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔄
🔄
🔄
یک تیم کامل و خفن فقط روی نیمکت هستند</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/138214" target="_blank">📅 18:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138213">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
شماتیک ترکیب پرسپولیس برابر شمس‌آذر  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/138213" target="_blank">📅 18:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138212">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
شماتیک ترکیب پرسپولیس برابر شمس‌آذر  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/138212" target="_blank">📅 18:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138211">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0GL-onWLxm2-gWSUkHjZ6AO5nqPh7GP48LQcSvU_azUWbsHhKa4ns2y3WV1Pwx4xlMBsDiE9VztZ9sKeu4Rd9E4EcKw0VgiSXiDEuhoaQIYX8lyDngNHVUUdWbi2es21ixVI2PdhMs0H1hHsodzqeiAwbruWvhTO2tuVzeeQKxwCX-Crl_NY2seRLuKfyGfEj9eo2ph77Bw9_9HTvJZfonsEFNc9GMLdsnTmRKg2oydrjsEWM9FqhCK9IV0DSf8eZSFz1a2pobt9tB_aWCQvksj73Dov2XRBck4U3tTzuSP9I9p97HrQLztZaq7Pbu_OEv_R38xAZnSvP-lt090ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
شماتیک ترکیب پرسپولیس برابر شمس‌آذر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/138211" target="_blank">📅 18:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138210">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
فوووووری
✔️
✔️
حدادی:  به روبین کازان برای کسری نامه زدیم به ما گفتن ۱ میلیون دلار + ۲۰ درصد حق ترانسفر بازیکن و ما رفتیم شهرآبادی رو خریدیم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/138210" target="_blank">📅 18:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138209">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
پیمان حدادی مدیرعامل پرسپولیس:
✅
تصمیم گرفتیم کادر ایرانی انتخاب کنیم و پای این کادر بمونیم و از کادر حمایت کنیم ابزار لازم براشون فراهم کنیم و بهشون زمان بدیم . ممکنه در هفته های ابتدایی نتایجی خوبی نگیریم ولی از هوادار میخوایم به کادر فنی فرصت بدهد . …</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/138209" target="_blank">📅 18:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138208">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
حدادی: ممکنه پنج شش هفته اول نتیجه نگیریم که ایراد نداره
😕
😕
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/138208" target="_blank">📅 18:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138207">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
پیمان حدادی مدیرعامل پرسپولیس:
🚨
از زمانی که مسئول اجرایی پرسپولیس شدم روزهای سختی را پشت سر گذاشتم. قسمت نبود به مسابقات آسیایی برویم. پرسپولیس با پوست اندازی به یک تیم نوین تبدیل شده است. نبود در آسیا و نگرفتن جام در 2 سال آسیا برای همه ما قابل قبول نیست.…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/138207" target="_blank">📅 18:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138206">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
پیمان حدادی مدیرعامل پرسپولیس:
🚨
از زمانی که مسئول اجرایی پرسپولیس شدم روزهای سختی را پشت سر گذاشتم. قسمت نبود به مسابقات آسیایی برویم. پرسپولیس با پوست اندازی به یک تیم نوین تبدیل شده است. نبود در آسیا و نگرفتن جام در 2 سال آسیا برای همه ما قابل قبول نیست. امید داریم از شرمندگی هواداران پرسپولیس در بیاییم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/138206" target="_blank">📅 18:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138205">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
❌
یک اتفاق جالب در بازی دیروز سرخپوشان
👍
در چند دیدار دوستانه اخیر شاهد لو رفتن ترکیب سرخ‌ها پیش از بازی بودیم، اما دیروز ورق برگشت و هیچ رسانه‌ای نتوانست ترکیب اختصاصی تیم را پیش از بازی منتشر کند. به نظر می‌رسد مهدی تارتار به وعده‌اش عمل کرده و پس از…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/138205" target="_blank">📅 18:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138204">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
علیرضا محمد، مربی پرسپولیس: چمن استادیوم سردار آزادگان بلند است .سبک ما روی زمینه و باید کوتاه شود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/138204" target="_blank">📅 18:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138203">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎥
🔴
بازدید بازیکنان پرسپولیس از چمن ورزشگاه سردار آزادگان در آستانه بازی با شمس آذر   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/138203" target="_blank">📅 18:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138202">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44bfb0b88b.mp4?token=PRjS6W9GqV0_Vbma59bhZNh31DFL7ruXv1LAbQjSBnkQHGTX1ne4YytPjWiahfEk_WgITPPsHfZMnLult1qAgFWrNj0AG7WV4BAzICIkb_akOaE4TgN8o8CU7Y6AfUkRM06KFe1tB_UnKCJoh7Gf_GzKs72S77WstGV7CHdF_HXdm-qgX0E8d4O4CRa5l_BG0oFSJVKORxihTPJPRFsiEsV3wKnHN4BZB7R1JvP0I3sGlUtcs5iMg5RSjLIsa0s52WxSYsMlzb-wLXQU92cZTFLK4s_7tCg6CjZ1QvScPW9OMctcYo8MVyQQTUXzUCbhzh8jWM5f2v3L_qvZuZOZxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44bfb0b88b.mp4?token=PRjS6W9GqV0_Vbma59bhZNh31DFL7ruXv1LAbQjSBnkQHGTX1ne4YytPjWiahfEk_WgITPPsHfZMnLult1qAgFWrNj0AG7WV4BAzICIkb_akOaE4TgN8o8CU7Y6AfUkRM06KFe1tB_UnKCJoh7Gf_GzKs72S77WstGV7CHdF_HXdm-qgX0E8d4O4CRa5l_BG0oFSJVKORxihTPJPRFsiEsV3wKnHN4BZB7R1JvP0I3sGlUtcs5iMg5RSjLIsa0s52WxSYsMlzb-wLXQU92cZTFLK4s_7tCg6CjZ1QvScPW9OMctcYo8MVyQQTUXzUCbhzh8jWM5f2v3L_qvZuZOZxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
حال و هوای ورزشگاه سردار آزادگان در فاصله 90 دقیقه تا شروع بازی شمس‌آذر - پرسپولیس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/138202" target="_blank">📅 18:07 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138201">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3e0a826af.mp4?token=i0VzmY_oMHZf0idhFTpD0ywMfXRko-O02VPaGTYzVtFf5SpzgkKndCtaM2jwk56pCf4X0GyEoj66XKjaZIIBoqjHtq2bGyXWa4ibbsFz5sB-XcJtbGB0TS4oYf2H9I7BE7PPV4UYmTkZAJ1rEkmMDqOZvVam-GAESsGVr986H0gOdJSHHVyiqIzoBuTHwvuDIBVp8h7FZzRZsrcUCdS3ovx4debCgx14BP_RWwp8Ml1DG5srg2BBDvCaB7EICUNtUzymf5ea1ULmlvvuQvFO09zBZNOezd6j5rvXcdAeNjBqscQtJ3ZkVY3DGDxqh2ZtXj1Bh--TfDcUHdC9HXkv7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3e0a826af.mp4?token=i0VzmY_oMHZf0idhFTpD0ywMfXRko-O02VPaGTYzVtFf5SpzgkKndCtaM2jwk56pCf4X0GyEoj66XKjaZIIBoqjHtq2bGyXWa4ibbsFz5sB-XcJtbGB0TS4oYf2H9I7BE7PPV4UYmTkZAJ1rEkmMDqOZvVam-GAESsGVr986H0gOdJSHHVyiqIzoBuTHwvuDIBVp8h7FZzRZsrcUCdS3ovx4debCgx14BP_RWwp8Ml1DG5srg2BBDvCaB7EICUNtUzymf5ea1ULmlvvuQvFO09zBZNOezd6j5rvXcdAeNjBqscQtJ3ZkVY3DGDxqh2ZtXj1Bh--TfDcUHdC9HXkv7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
🔴
بازدید بازیکنان پرسپولیس از چمن ورزشگاه سردار آزادگان در آستانه بازی با شمس آذر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/138201" target="_blank">📅 18:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138200">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🎥
🔴
ورود تیم پرسپولیس به ورزشگاه سردار آزادگان برای بازی با شمس آذر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/138200" target="_blank">📅 18:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138199">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e7899739a.mp4?token=T8yjpyFLdCbfzj_8ymoV9Fu6JU-0pA9_bNY6INktxANc2G771OK7v760L8ZLTIDTkDh18dT9gYpbfRQ12M12ojz05gZtxGyJTdLxu9LZ2MhkRVfi3nM0BbQYMfvmn3GRSqNKiPLry1mr88s6EsZd_w2vJYqlC1pOYtewaBCBo4yunAzHcUyRkWB_-QKTffqkkoMN1YatEGb6TH4G2XwqrBHEWEWEJZPL11-pVHf2CBMU1R3qc4oOCSB48RAgf0GrA24cZYdXikh-_9C3RDChn4GQq33Z2puAiNUCyEWmhoM0rqyOGCTuxqL8pLCcV6l4ux8ogg2YfLZjm3YKAg7Ctg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e7899739a.mp4?token=T8yjpyFLdCbfzj_8ymoV9Fu6JU-0pA9_bNY6INktxANc2G771OK7v760L8ZLTIDTkDh18dT9gYpbfRQ12M12ojz05gZtxGyJTdLxu9LZ2MhkRVfi3nM0BbQYMfvmn3GRSqNKiPLry1mr88s6EsZd_w2vJYqlC1pOYtewaBCBo4yunAzHcUyRkWB_-QKTffqkkoMN1YatEGb6TH4G2XwqrBHEWEWEJZPL11-pVHf2CBMU1R3qc4oOCSB48RAgf0GrA24cZYdXikh-_9C3RDChn4GQq33Z2puAiNUCyEWmhoM0rqyOGCTuxqL8pLCcV6l4ux8ogg2YfLZjm3YKAg7Ctg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ورود بانوان هوادار پرسپولیس و شمس آذر به ورزشگاه سردار آزادگان
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/138199" target="_blank">📅 18:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138198">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
یک روز مانده به بازی بازم ترکیب تیم لو نرفته و کاملا مشخصه جاسوس شناسی شده بعد از سالها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/138198" target="_blank">📅 16:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138197">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔄
🔄
مدیرعامل مس شهر بابک: آسانی فسخ کرده بود؛ از استقلال شکایت کردیم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/138197" target="_blank">📅 15:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138196">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⚡️
⚡️
شنیده میشه تیوی بیفوما در یک ماه اخیر برای ماندن در پرسپولیس زیر نظر پزشک تغذیه باشگاه 8 کیلو کاهش وزن داشته و علاوه بر اون زندگی حرفه ای شو سالم تر از قبل کرده و تمرکز اصلی شو روی فوتبال خودش گذاشته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/138196" target="_blank">📅 15:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138195">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
علت ماندن تیوی بیفوما در پرسپولیس، کاهش وزن، آمادگی جسمانی مطلوب و همچنین تغییر نگرش او و اصلاح سبک زندگی شخصی‌اش بود.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/138195" target="_blank">📅 15:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138194">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⬅
⬅
⬅
حمید مطهری سرمربی فولاد گفته الی و بلی رزاق پور باید بمونه و اگه بره پرسپولیس استعفا میدم!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/138194" target="_blank">📅 15:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138193">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
سینا اسد‌بیگی: بعد جدایی از پرسپولیس افسردگی گرفتم، دلیل جداییم از پرسپولیس فوتبالی نبود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/138193" target="_blank">📅 15:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138192">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9CliBIsW7MMcw4BDolcG_dDUPENyfzsxUFEmtMuerh829UBhYzgh7IVC8Zv4khfYcALEQgBkYXpht4nGSElT_IZG4R4KxtYbU4v9WYn6sTQhjxMrtGzqbvjYJQ2YCoTPrjqu7WQE9rbWVZ0XBvmECr7aXlAd5p3nOnMijR7ibTP7n9gGU8bC8LQBS4_bHfJx9Nril8iS967shaXiWLLWfWq8KDjWqzP7_w-L4u0W4f_7XXfn-pJZjgLUpUwjxLq-aJO9PWvBbPPfGIJBjY-9z5FJGI3qxOlbNYhcv71iaXgAH0c3psYEcJgfw0gETPFhBLftKkrw3uGXXi54vIXng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇
⬇
اگه ترامپ تصمیم بگیره قبل از شروع هفته دوم به ایران حمله کنه، لیگ دوباره نیمه تموم میمونه و استقلال برای اولین بار در تاریخ خودش دبل قهرمانی رو تجربه میکنه
😅
😅
⬅
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/138192" target="_blank">📅 13:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138191">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
باشگاه قراره امروز از دانیال ایری رونمایی کنه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/138191" target="_blank">📅 13:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138190">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">💢
💢
💢
💢
مدیرعامل بانک‌شهر فرداصبح بودجه لازم رو برای جذب محمد قربانی دراختیار باشگاه پرسپولیس قرار خواهد داد. مدیریت‌باشگاه پرسپولیس‌آماده‌اندتاسقف 800 هزار دلار برای محمدقربانی هزینه‌کنند. این احتمال هست که مدیریت الوحده یه مقداری مبلغ رو بالا ببرند.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/138190" target="_blank">📅 13:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138189">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🏆
رضایی سرمربی شمس‌آذر: امیدوارم فردا بیش از ۱۰ درصد به هوادارای پرسپولیس نرسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/138189" target="_blank">📅 13:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138188">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIB5FFcvfOhbn4Wo2ZZQaaVFxgfVv5Rq1XuYvpJTpox4BLDPPggfEaQj8eHl75BvlerS8KpXPTQJjj1zSTex6iztM0zvzdkNkL7GeyiYvQBJVoWBojOkFTOr8zIegzwIGTKyFZQpev5sRmKb6c6GhKymD9dt5Ws76ltxMGoU0LAh6ZhQQTcOG7u6TsDfPBbxYgMjUTfhuWxtlmF4TjOSYTyQAkxNuOM733FzimQPyRuJRQ22wrB950LUx05lkzVcVG2d1Yf5uvGqjZayE35DfaQbSnwTYIpm-HP4CsqAV9zwI9Fg_8xpdliShWJ6gl5Tz_Ens1wywxOMQuBWjiQWUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽
شروعی تازه، آزمونی سخت در قزوین!
پرسپولیسِ تارتار برای اولین قدم در فصل جدید، مقابل شمس‌آذر به دنبال یک شروع قدرتمند است.
⚽️
لیگ خلیج‌فارس ایران
[
شمس‌آذر
⚽️
🆚
⚽️
پرسپولیس
]
⏰
شنبه ساعت ۱۹:۳۰
🏟
استادیوم سردار آزادگان
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/138188" target="_blank">📅 13:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138187">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvHlpn9PX0euP6cdxyt4CBN4rfY2Bgih3qlQOEZu-lxaLbOfjNew-KEZv7Wn9MO819z3gkcNUJSggIiI-roDgsenjZ0uTVQbfGbkG86Awn0I3WKHKuWNEQbWIrDie1eqGKZgw4Su7tOE2665ObQ0oQTcMx461dzRn6aY_DHN9Mj_32un_MeSHK8VGEOPTAbdmyd0j4mZgEphJx-p-lAunWTkBunh9jd5xuFedxnvz5wL6asard6UV6yhUIegmqmknyZ5Znco3XlffNVJhcWA7kM296i7oY3HQ7NaOchRsH0oJDLrTMyN1iZaffvFTNBRTj090wvsU8buKQ59_Qk1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مهدی‌ترابی بازیکن تراکتور بدلیل مصدومیت در بازی دیروز مقابل پیکان، حداقل ده روز غایب است و بازی مقابل سپاهان و پرسپولیس د ر هفته دوم و سوم را از دست خواهد داد
✍️
خبرگزاری تسنیم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/138187" target="_blank">📅 13:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138186">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
❌
آنا:
🔴
سازمان لیگ سه گزینه اصلی برای برگزاری دربی مدنظر دارد،
❌
سازمان لیگ قصد دارد دربی را در یکی از سه شهرِ مشهد، اصفهان و تبریز برگزار کند.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/138186" target="_blank">📅 12:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138185">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
با اعلام امیرحسین روشنک مسئول برگزاری کننده لیگ برتر؛ دربی پایتخت ۱۲ شهریور ماه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/138185" target="_blank">📅 12:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138184">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c4ae02899.mp4?token=ICx-G-eupRh5QZBzr6y9UxIpc_w0FvP0oFA3gEqrhFk-QL1-jvlY59WIfVhkSsubxfAZWxY6QGxDCIxxgrvr_HFVtERwE5e3ZgdLp9qY658mt4Ef42k0xunIBjStf0ytI0XlTDgHAQEQpUkyI1GObIj-42OEpKubDfQWPYyxBBDa-AmrhdSjyvDLuaX_s_j20izTLtraAfKPRH2nS-nKUFG8hJAMi_UObsnotpSKu1HXczaD_Q_KTmH7t8Z5i-48q2hkkgBI2wYZCb-mHuDyKkxCpstgMQieKcrLEkhI3g8JpSewauPDBzNrxBkzFeOZ9DkzDarGbetVtOEXtDSmmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c4ae02899.mp4?token=ICx-G-eupRh5QZBzr6y9UxIpc_w0FvP0oFA3gEqrhFk-QL1-jvlY59WIfVhkSsubxfAZWxY6QGxDCIxxgrvr_HFVtERwE5e3ZgdLp9qY658mt4Ef42k0xunIBjStf0ytI0XlTDgHAQEQpUkyI1GObIj-42OEpKubDfQWPYyxBBDa-AmrhdSjyvDLuaX_s_j20izTLtraAfKPRH2nS-nKUFG8hJAMi_UObsnotpSKu1HXczaD_Q_KTmH7t8Z5i-48q2hkkgBI2wYZCb-mHuDyKkxCpstgMQieKcrLEkhI3g8JpSewauPDBzNrxBkzFeOZ9DkzDarGbetVtOEXtDSmmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔄
🔄
دیشب وسط مصاحبه یه هوادار استقلال رفیقش میاد انگشتش میکنه
🤣
🤣
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/138184" target="_blank">📅 12:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138183">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
500 تا دیگه رفت رو رضایتنامه؛ گلزنی محمد قربانی برای الوحده که داغ دل تراکتوری ها و پرسپولیسی هارو تازه کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/138183" target="_blank">📅 12:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138182">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mrv55QS2UpE5xd9NikQICwDbl-xLVZhHUp7hdv6oyyCrl_zSalfHjT06wNCmi31B6fYNKXpcPAn1ZyoEKpYFYEBMbHjptm6h4VafxmnUp2VpYB300HqVp7oDHbQDX3K7b8taZCvV8uUyrQefweAUFStMoC_B9bUMfW-F1ht5UJzmMHX_s6ZSML3AzRtW8p9EazSn3Ih1hx1MQOsAt3lsPnn2h6Cezq02c80z8Drexd99Z2VQrsdqodd_PnPkFoAY_Ordp9prpqcNPG4JkUiMZRSZq1KCX-fmTpMT3J2ksGMH2ru4mjThxIKJGCjq5T2HkJdtfAGRPrmKc1D21g82wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری / آنا
⚡️
جدایی قربانی از الوحده رسما منتفی شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/138182" target="_blank">📅 12:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138181">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
✅
تکمیلی :
🎙
مهدی‌تارتار سرمربی پرسپولیس: علاوه بر دانیال ایری بزودی دوبازیکن جوان و شایسته جذب میکنیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/138181" target="_blank">📅 12:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138180">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0l1IeboVwMt220KgxqxZe6S-eqK1xnsxXIa02KZDKcNX3V3GSZE4gYKq8PxoRkmlWotCLZlpaiTP_YFrPCvtvWQnVd5h3vklIdzHQCw9oNPVAcfK4JSYnw6CjCoblPVNzuKtNmTXTsm35byf3vgYgpgom4UjPpupyDb9fpB9FJYYTFMa0M8FQJ0K7Ug-84k5pJ_IKCq-xXyGLdP2K__V5-eRr0MSjFX1nL1dWN_jlsNbQpafs2sdKF7uP34sfQYuwGXZB6ELOsIBfvz85TxQhuukuUlch_4KHd0egB6MZgXHyXFBF_0PPeqPVPinNArcSpy-bPvRez_-ETaAMaSAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووووووری :
⚡️
تراکتور از جذب قربانی منصرف شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/138180" target="_blank">📅 11:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138179">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
مس شهربابک از استقلال به خاطر استفاده از آسانی شکایت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/138179" target="_blank">📅 11:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138178">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
پوستر روز بازی پرسپولیس مقابل شمس آذر با یادی از شهید طرفدار پرسپولیس از مدرسه شجره طیبه میناب  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/138178" target="_blank">📅 11:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138177">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
مس شهربابک از استقلال به خاطر استفاده از آسانی شکایت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/138177" target="_blank">📅 11:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138176">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">💢
💢
💢
شایعات؛ امیر جعفری مدافع چپ گلگهر به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/138176" target="_blank">📅 10:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138175">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFii8HG1YSRcWTAk90GxISYqVNOIkntf0HVTf0YBF2MqJYqSXwyLsbL7JZJp0FVTNFJlwm7Iqhc8GOAAzjZ7sGK3mJVLPvEOfVondPDZSXquz3D9m7CrVvidIaWPaHNpJIQsmBEBOtApPaz3NJMidjoBSVkZNTIbdc4GBABjR_-SHZ7eE_FBwRLqPXP-AGt_zXes5I0UN0kY09oX8KGZLZBpBVYslqJvRQVhAGhCJVHxIqNjswXkqzZd1pIKrjT5ZVKY9IL8m3PABXnwKvTVgnn1hFcTkSucpzeIQeTbww3_NOCbLZIxzMOmBh0H2Kn45b9vbPiA3Svw54csfehstg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پوستر روز بازی پرسپولیس مقابل شمس آذر با یادی از شهید طرفدار پرسپولیس از مدرسه شجره طیبه میناب
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/138175" target="_blank">📅 10:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138174">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">💢
💢
💢
شایعات؛ امیر جعفری مدافع چپ گلگهر به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/138174" target="_blank">📅 09:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138173">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
🔴
صبح روزی که عشق بازی داره بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/138173" target="_blank">📅 08:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138172">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLshJqSCzzUiwqP9H14D0kNTgjBZ22nlrw-BBnFm0k7jzPcD4HdJc2NCcmmR1U4QCQIfUS8w3iLyqR6J9k0zBmTg-6LBghnPdwgYJ8jn6PQ_jCSTCkXjl9xkkpDym85XHVpMLr6DjLGYh3e2lk0UAiuRZ5FPKeUNd-WFqVyqGz74STggIXQX2gxNBtXYssTfELyfCpc-WIWtu4Kwm5MOBCeQRNSqfWySVK-HX-881IP5PWKSIJAP-repvfJ0Mq1U4n-TAC8C0LBMVjP44oR5IkS5iQTnGg8IEOh6LWhpmwdZqh3HjmOOO2GhSPXt86M_drdamS7UaiJpRjw_t3h5kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">➕
دسترسی سریع و مستقیم به اسپورت‌نود
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
🔗
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/138172" target="_blank">📅 02:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138171">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">💢
💢
💢
💢
مدیرعامل بانک‌شهر فرداصبح بودجه لازم رو برای جذب محمد قربانی دراختیار باشگاه پرسپولیس قرار خواهد داد. مدیریت‌باشگاه پرسپولیس‌آماده‌اندتاسقف 800 هزار دلار برای محمدقربانی هزینه‌کنند. این احتمال هست که مدیریت الوحده یه مقداری مبلغ رو بالا ببرند.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/138171" target="_blank">📅 01:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138170">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔄
🔄
❌
شایعه شده که پرسپولیس قرارداد یکی از خرید ها رو ثبت نکرده تا به عنوان سهمیه آزاد بتونه قراردادش رو ثبت کنه.
❌
میگن این بازیکن تو گل‌گهر بوده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/138170" target="_blank">📅 00:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138169">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
با خرید امیر جعفری سهمیه خرید پر میشه ولی .....
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/SorkhTimes/138169" target="_blank">📅 00:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138168">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✔️
✔️
✔️
گفته میشه که کارت بازی همه بازیکنان پرسپولیس صادر شده و پرسپولیس تنها میتواند یک خرید دیگر داشته باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/138168" target="_blank">📅 00:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138167">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
یک روز مانده به بازی بازم ترکیب تیم لو نرفته و کاملا مشخصه جاسوس شناسی شده بعد از سالها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/138167" target="_blank">📅 00:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138166">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
❌
یک اتفاق جالب در بازی دیروز سرخپوشان
👍
در چند دیدار دوستانه اخیر شاهد لو رفتن ترکیب سرخ‌ها پیش از بازی بودیم، اما دیروز ورق برگشت و هیچ رسانه‌ای نتوانست ترکیب اختصاصی تیم را پیش از بازی منتشر کند. به نظر می‌رسد مهدی تارتار به وعده‌اش عمل کرده و پس از…</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/SorkhTimes/138166" target="_blank">📅 00:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138165">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
ترامپ: ایران خواستار غرامت خسارات درگیری نظامی ۵ ماهه است و من هم از آنها غرامت می‌خواهم چون سربازان امریکایی را کشته اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/SorkhTimes/138165" target="_blank">📅 00:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138164">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
امیر جعفری که گفته می‌شود بازیکن مدنظر پرسپولیس است بر روی بیو خود قلب قرمز گذاشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/138164" target="_blank">📅 00:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138163">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
عضو مستعفی هیئت مدیره استقلال به صراحت اعلام کرده نامه فسخ یاسر آسانی پخش شده و بازی کردن او غیرقانونی است.
❌
❌
تیم‌های لیگی با شکایت به AFC و FIFA می‌توانند این تخلف را گزارش دهند و نتایج خود را جلوی استقلال ۳-۰ کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/138163" target="_blank">📅 23:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138162">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
به امید اینکه با این کیت قشنگ ؛ خاطرات و لحظات خوبی رو تو ذهن و تاریخمون هک کنیم
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/138162" target="_blank">📅 23:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138161">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQS_05EZ6ZgWZav709Xq_DsEkHyJM00Qdt-kLWv54yltUwj73sF3mySr2brjimp7x2SLMSQIIW6l__4JBHoJCMEb4MXyW2ecsr7UpKD2knKISKaJSLdY1AhFd2nRUVHzO56oO5KJXAsWlx-YD94XbFMwYlxqEO3BxPyTZ8Atx_Dgjw6dSxwDMJ6Cx4FkvTcjCtked4vPiHzlLhJbkl4627xRwppEyDuHBkOxIXmiZQDsbxwWX4-0EKMNbmhbqINvVfjmJ_GQ5xCH9piUzJ-FhDv0DyZsK6EbZbk778I3mcOz_F1NT_y6MsT-PYrHMPRhWkk0wQC2-s6JIYvD8Xx-gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
امیر جعفری که گفته می‌شود بازیکن مدنظر پرسپولیس است بر روی بیو خود قلب قرمز گذاشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/138161" target="_blank">📅 23:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138160">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
بازی کردن آسانی تخلف است
🔴
هیأت‌مدیره استقلال اقرار کرد فسخ یک‌طرفه آسانی بطور قطع انجام گرفته و قادر به‌‌بازی نیست‌. مس شهربابک بعدبازی بدون فوت‌وقت شکایت برای ٣ بر صفر کنند‌. شرایط جنگی و اولویت نبودن فوتبال برای مردم نباید باعت چشم بستن تیم‌ها به این جرم…</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/138160" target="_blank">📅 23:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138159">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fea0075aa.mp4?token=Ix6KWrVuK0o1n_8tkD8IAExRkAraqryhujpPV0SFzPcJF4fhJ2UK9JqmQetj1tXNAn-f331kUP_SL3h1QpT4dzGeZ6VoOZpqT_WZx_7Ct0TceXMiY8WFx-s9--2riWAKXdY0bdwV9yyMmfAWHngYn0_eqOQNbqXWmP2ZBAox5TjEuvhUw75II00ZgjAWoalK0SBj53jvMm6MxvhhDmQjhLAlD8N2AezWrwYcYct3pADRG1pWG0jm_fqyVNAig0DZcs1Ww42NoovjIhhMXGPr5a7xtcfIRFtjXe_gHVi3if_iNMsQOJaXuGY1FdgdXWHR639QJH-olUaBAwznIpoUGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fea0075aa.mp4?token=Ix6KWrVuK0o1n_8tkD8IAExRkAraqryhujpPV0SFzPcJF4fhJ2UK9JqmQetj1tXNAn-f331kUP_SL3h1QpT4dzGeZ6VoOZpqT_WZx_7Ct0TceXMiY8WFx-s9--2riWAKXdY0bdwV9yyMmfAWHngYn0_eqOQNbqXWmP2ZBAox5TjEuvhUw75II00ZgjAWoalK0SBj53jvMm6MxvhhDmQjhLAlD8N2AezWrwYcYct3pADRG1pWG0jm_fqyVNAig0DZcs1Ww42NoovjIhhMXGPr5a7xtcfIRFtjXe_gHVi3if_iNMsQOJaXuGY1FdgdXWHR639QJH-olUaBAwznIpoUGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بازی کردن آسانی تخلف است
🔴
هیأت‌مدیره استقلال اقرار کرد فسخ یک‌طرفه آسانی بطور قطع انجام گرفته و قادر به‌‌بازی نیست‌. مس شهربابک بعدبازی بدون فوت‌وقت شکایت برای ٣ بر صفر کنند‌. شرایط جنگی و اولویت نبودن فوتبال برای مردم نباید باعت چشم بستن تیم‌ها به این جرم استقلال بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/SorkhTimes/138159" target="_blank">📅 23:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138158">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
قدوسی: 24 ساعت مهم برای قربانی در پیش داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/138158" target="_blank">📅 23:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138157">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇷
💢
پیراهن فصل‌جدید بعد از ادیت نهایی رونمایی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/138157" target="_blank">📅 22:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138156">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhYcY3DavZSVr9hYcXCv5MCJ3iy_Pa3eKfvqOupyWiWZo4iKuFRSEZizeYTD_VKT6uBOxa-HeTdCZ43ahERu-E6NZtBNiOzE2g3DOPxD4Cl-X9PFLChr656wAlXYr0FYWTo33cw-Ti2cIitOHL9mWscCy45mU-jjTEEaELuq53EytlFyodVrYIjtxGjS9d9SXiqPoQst0KfEKMx3_n9Wu_V-SN64Qvc0sEm6L4i_dPABkRtnC7vXu6iwbvSujK52CVLd9AX0GGE0X-JVZ-CHzWwEEcxwcuiLr_rgHUs64xx6tBKuQfUUwZmTYMHeB37ZsLDnx9lkz7JDgG07vt52XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
🔄
زیباترین کیت 5 فصل اخیر از نظر شما؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/138156" target="_blank">📅 22:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138155">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇷
💢
پیراهن فصل‌جدید بعد از ادیت نهایی رونمایی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/138155" target="_blank">📅 22:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138154">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
خطاب به مدیران باشگاه مس شهر بابک: یاسر آسانی طبق گفته ی خود عضو سابق هیات مدیره باشگاه استقلال، کارشناسان و قانون واضح فیفا، امکان عقد مجدد قرارداد با استقلال و نداشته و غیر قانونی بازی کرده است.
🔹
منتظر شکایت این باشگاه هستیم.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/SorkhTimes/138154" target="_blank">📅 22:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138153">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
500 تا دیگه رفت رو رضایتنامه؛ گلزنی محمد قربانی برای الوحده که داغ دل تراکتوری ها و پرسپولیسی هارو تازه کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/138153" target="_blank">📅 22:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138152">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bf45d8651.mp4?token=jcoGi8iQKUpdGoEKea1tNoLolXZsvC0KV5XvfnnVTKY5qPQmFIK_f0eu98631NdxT3m80F3_7LhZoxIVrD-82hCPAJT514BW9L7HjDkgrPrVK1duhTweJnH2dk0v6yaG9GkQglnARHYvoydl8Y-biu3XJaRnWMo4CTZd2Y77wIQbwHO0MOpfYlGKVChqN0yjn8jJolNXl8BD3hrg4U6yH9af7nTjjwMpuK7LcDc412izAngOMfKKg_myaIyoGxdujRv3hxgIy1o-MI7n3OuxvJ9cwWz7ib5LNCd5DjWkDptUBAXa2mxCLx1nNJSnU255kJzA9kICT-hhvqSx-jUg3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bf45d8651.mp4?token=jcoGi8iQKUpdGoEKea1tNoLolXZsvC0KV5XvfnnVTKY5qPQmFIK_f0eu98631NdxT3m80F3_7LhZoxIVrD-82hCPAJT514BW9L7HjDkgrPrVK1duhTweJnH2dk0v6yaG9GkQglnARHYvoydl8Y-biu3XJaRnWMo4CTZd2Y77wIQbwHO0MOpfYlGKVChqN0yjn8jJolNXl8BD3hrg4U6yH9af7nTjjwMpuK7LcDc412izAngOMfKKg_myaIyoGxdujRv3hxgIy1o-MI7n3OuxvJ9cwWz7ib5LNCd5DjWkDptUBAXa2mxCLx1nNJSnU255kJzA9kICT-hhvqSx-jUg3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
500 تا دیگه رفت رو رضایتنامه؛ گلزنی محمد قربانی برای الوحده که داغ دل تراکتوری ها و پرسپولیسی هارو تازه کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/SorkhTimes/138152" target="_blank">📅 22:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138151">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
چیه این پرسپولیس ..
❌
محمد قربانی بعد ورود به زمین گل زد برای تیمش
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/138151" target="_blank">📅 22:03 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
