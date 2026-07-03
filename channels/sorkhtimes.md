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
<img src="https://cdn4.telesco.pe/file/gO1DGM0xjkVNCgfyuXaA5oR_iy_nyCfP0q1AiuoR530jo7GTejCLCUWafjB0yjheb19ZogcFrJma6Mw4xTdxIRSZrnlZ5ZiOIodnKYgRotj1xzExZYvOaYPK0QAGz-zAz9Xr-LmcXKafrQ0v64k0CVcMZA-fA-Nu6ptRr6eUJ0rZa_5IRHkBa2xFhPqc5x5U8VQQ_naPlZXiC0AXRhkRcOEttZ_ixKlMTnwemUAjBsKUqsNaHfEvcuPSBaLFGYYVUYD66j28vQxiL1xJuyMqgx-uOOEIaqBkRtWNsVfMOOvb3AyV63LkZ8VTIw7WJYDzn3IvVdCoJ-0Eexb0WdMIEg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 21:24:38</div>
<hr>

<div class="tg-post" id="msg-134867">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دوستان بهترین کانال آنالیز ایران رو از دست ندید
هر روز فقط یک گزینه مطمئن می‌ذاریم، بدون ریسک‌های الکی.
بازی امروز: کانادا – مراکش</div>
<div class="tg-footer">👁️ 880 · <a href="https://t.me/SorkhTimes/134867" target="_blank">📅 21:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134866">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⚽️
جام جهانی ۲۰۲۶؛ وقتی تحلیل درست، سود می‌سازد!
این‌بار نوبت جدال
کانادا
🇨🇦
– مراکش
🇲🇦
است؛ مسابقه‌ای که آمارش یک نکته مهم را نشان می‌دهد:
«مجموع گل بیشتر از ۱.۵» یک انتخاب کاملاً منطقی و ارزشمند است.
دلایل:
✅
کانادا مقابل تیم‌های سرعتی بازی بازتری ارائه می‌دهد.
✅
مراکش استاد ضدحملات سازمان‌یافته و استفاده از فضاهای پشت دفاع است.
✅
اگر یک گل زودهنگام ثبت شود، ریتم مسابقه کامل عوض می‌شود و راه برای گل دوم باز می‌شود.
ما فقط احساسات را تحلیل نمی‌کنیم؛
داده و روندها
حرف اول را می‌زنند.
❤️
برای دسترسی به دقیق‌ترین پیش‌بینی‌های جام جهانی، همین حالا عضو شوید:
👇
👇
👇
https://t.me/+iIi9FxzzcYBjNDg8
https://t.me/+iIi9FxzzcYBjNDg8</div>
<div class="tg-footer">👁️ 880 · <a href="https://t.me/SorkhTimes/134866" target="_blank">📅 21:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134865">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
بازی های امشب
🇦🇺
استرالیا_مصر
🇪🇬
🔸
ساعت 21:30
🇦🇷
آرژانتین_کیپ ورد
🇨🇻
🔸
ساعت 01:30
🇨🇴
کلمبیا_غنا
🇬🇭
🔸
ساعت 05:00
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/SorkhTimes/134865" target="_blank">📅 20:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134864">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
🏆
برنامه کامل بازی‌های ۱/۱۶ نهایی جام جهانی
🇿🇦
آفریقا جنوبی - کانادا
🇨🇦
🇧🇷
برزیل - ژاپن
🇯🇵
🇳🇱
هلند - مراکش
🇲🇦
🇺🇸
آمریکا - بوسنی
🇧🇦
🇳🇴
نروژ - ساحل عاج
🇮🇪
🇫🇷
فرانسه - سوئد
🇸🇪
🇩🇪
آلمان - پاراگوئه
🇵🇾
🇲🇽
مکزیک - اکوادور
🇪🇨
🇧🇪
بلژیک - سنگال
🇸🇳
🇪🇸
اسپانیا - اتریش…</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/SorkhTimes/134864" target="_blank">📅 20:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134863">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
خبرگزاری تسنیم:
🔹
تنها مانع عقد قرارداد اسکوچیچ با پرسپولیس اختلاف مالیه که همچنان پابرجاست
🔹
مدیریت پرسپولیس خواستار تخفیف چند صدهزار دلاری شده
🔹
اگه توافق با او صورت نگیره احتمالا گزینه ایرانی مدنظر باشگاه خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SorkhTimes/134863" target="_blank">📅 20:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134858">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
پیروز قربانی: من نیوزلند رو با فجر سپاسی شیراز می‌بردم مطمئن باشید نیوزلند اگه تو لیگ 16 تیمی ما بود، جزو چهار تیم آخر میشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/134858" target="_blank">📅 19:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134857">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
زنوزی، مالک باشگاه تراکتور به صورت شخصی با مرتضی پورعلی گنجی، مدافع پرسپولیس وارد مذاکره شده تا این بازیکن راهی تبریز شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/134857" target="_blank">📅 18:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134856">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇹🇳
یک اتفاق عجیب برای تونسی‌ها در جام جهانی؛
❌
دوپینگ ۸ بازیکن مثبت شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/134856" target="_blank">📅 18:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134855">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🏆
جدول نهایی گروه F جام جهانی ۲۰۲۶
🇳🇱
صعود هلند به عنوان تیم اول
🇯🇵
صعود ژاپن به عنوان تیم دوم
🇸🇪
صعود سوئد به عنوان تیم سوم
🇹🇳
حذف تونس به عنوان تیم چهارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/134855" target="_blank">📅 18:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134854">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
🎙
رسول خطیبی: محمدرضا زنوزی، پس از باخت ۴-۲ تراکتور مقابل استقلال در تبریز، جشن گرفته بود!
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/134854" target="_blank">📅 18:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134853">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
ابوالفضل جلالی که قراردادش با استقلال تموم شده، دوست داره به پرسپولیس بره. چون بازیکن آزاده، پرسپولیس شرایط جذبش رو بررسی می‌کنه، اما تصمیم نهایی رو سرمربی جدید تیم می‌گیره.
🔴
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/134853" target="_blank">📅 18:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134852">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❗️
❗️
فوری؛ شنیده ها: ابواالفضل جلالی خودش رو به پرسپولیس لینک کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/134852" target="_blank">📅 18:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134851">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
نساجی مازندران به لیگ برتر بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/134851" target="_blank">📅 18:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134850">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
✅
🔴
باشگاه پرسپولیس: هیچکس از مدیران باشگاه به هیچ عنوان با خداداد عزیزی حتی یک تماس هم نگرفته و خداداد حتی گزینه هم نبوده و فقط از طریق لابی و رسانه ها خودش رو گزینه پرسپولیس کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/134850" target="_blank">📅 18:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134849">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from"mehran"</strong></div>
<div class="tg-text">اگه برگردیم به دوران یحیی بدبخت میشیم
بزور امثال پاکدل و دهقان و ابراهیمی و نعمتی و صادقی و فرجی و عیسی و خیلیای دیگه رو بیرون کردیم
تازه هنوز ی سریاش تو تیم هستن مث سرلک کنه</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/134849" target="_blank">📅 17:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134848">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">یحیی بیاد که دوباره باندبازها توی تیم بموننن و دلالی باهمدیگه</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/134848" target="_blank">📅 17:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134847">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #افشاگری
⚠️
🔴
به گزارش رسانه «سرخ تایمز» محسن خلیلی معاونت ورزشی باشگاه پرسپولیس در ۲۴ ساعت گذشته سخت به تکاپو افتاده و دنبال آوردن یحیی گل محمدی به پرسپولیسه؛تنها شخصی که تو باشگاه خیلی سفت سخت داره تمام زورشو میزنه تا مربی ایرانی بیاد…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/134847" target="_blank">📅 17:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134846">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
خبرگزاری تسنیم:
🔹
تنها مانع عقد قرارداد اسکوچیچ با پرسپولیس اختلاف مالیه که همچنان پابرجاست
🔹
مدیریت پرسپولیس خواستار تخفیف چند صدهزار دلاری شده
🔹
اگه توافق با او صورت نگیره احتمالا گزینه ایرانی مدنظر باشگاه خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/134846" target="_blank">📅 17:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134845">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
|
#افشاگری
⚠️
🔴
به گزارش رسانه «سرخ تایمز» محسن خلیلی معاونت ورزشی باشگاه پرسپولیس در ۲۴ ساعت گذشته سخت به تکاپو افتاده و دنبال آوردن یحیی گل محمدی به پرسپولیسه؛تنها شخصی که تو باشگاه خیلی سفت سخت داره تمام زورشو میزنه تا مربی ایرانی بیاد علی الخصوص که اون شخص یحیی گل محمدی باشه همین آقای خلیلی هست!
#نه_به_مربی_ایرانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/134845" target="_blank">📅 17:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134844">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسکوچیچ امضا کرده و الان رسما سرمربی پرسپولیسه/طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/134844" target="_blank">📅 16:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134843">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
❗️
میثاقی: قرارداد پرسپولیس برای اسکوچیچ ارسال شده، روی مبلغ قرارداد یه چند صدهزار دلاری اختلاف دارن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/134843" target="_blank">📅 16:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134842">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
خبرگزاری تسنیم:
🔹
تنها مانع عقد قرارداد اسکوچیچ با پرسپولیس اختلاف مالیه که همچنان پابرجاست
🔹
مدیریت پرسپولیس خواستار تخفیف چند صدهزار دلاری شده
🔹
اگه توافق با او صورت نگیره احتمالا گزینه ایرانی مدنظر باشگاه خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/134842" target="_blank">📅 16:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134841">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❗️
فووووووووری؛ تکلیف نیمکت پرسپولیس تا هفته آینده مشخص میشه. باشگاه از اوسمار تخفیف خواسته اونم موافقت کرده ولی میزان تخفیف رو اعلام نکرده/ فارس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/134841" target="_blank">📅 16:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134840">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
❌
خداداد عزیزی: ایرادات و مشکلاتی در پرسپولیس هست که این تیم را دچار بحران و حاشیه کرده است و تا حالا این مدل کار کردن رو ندیده بودم. در صورتی که در تراکتور همه چیز با یک زنگ به زنوزی حل میشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/134840" target="_blank">📅 15:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134839">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
✅
واکنش زنوزی به انتقال اسکوچیچ به پرسپولیس: اسکوچیچ مربی بزرگیه و تونست تراکتور رو قهرمان کنه اما او بدون ابزار قهرمانی نمیتونه در یک تیم معمولی دوباره قهرمان بشه!!!!!!
🔴
🔴
پ.ن آقای حدادی آقایون بانک شهر بهتون بربخورههههه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/134839" target="_blank">📅 15:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134838">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
✅
بازگشا سخنگوی پرسپولیس در مورد روند مذاکرات با اسکوچیچ :
❌
❌
تصمیم‌گیری، مذاکره، تفاهم، عقد قرارداد و امضای توافق با یک سرمربی در شأن باشگاه، نیازمند جلسات متعدد، بررسی‌های دقیق و رفت‌وبرگشت‌های فراوان است. اطلاع‌رسانی لحظه‌به‌لحظه درباره روند مذاکرات و چالش‌های…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/134838" target="_blank">📅 15:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134837">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
بازگشا: به یه ضد پرسپولیسی داخل باشگاه اجازه موندن ندادیم. هوادار مالک باشگاهه، از هوادار سواستفاده نکنید که بمونید و کنار تیم دلالی کنید. آخرین اخطاره باج نمیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/134837" target="_blank">📅 14:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134836">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/134836" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/134836" target="_blank">📅 14:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134835">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/134835" target="_blank">📅 14:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134834">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❗️
❗️
درحالیکه استقلال ، سپاهان و تراکتور تمرینات شون برای فصل جدید شروع کردن اما خبری از شروع تمرینات پرسپولیس نه تنها نیست بلکه حتی تکلیف نیمکت هم مشخص نیست!
🔴
🔴
حدادی داره کاری میکنه تا دلمون برای درویش تنگ بشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/134834" target="_blank">📅 12:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134833">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
🔴
فووووری؛ رضا شکاری از پرسپولیس جدا شد و به زودی‌ لژیونر میشه. تیم جدید شکاری در قاره آسیا خواهد بود/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/134833" target="_blank">📅 12:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134832">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
✔️
✔️
مدیران پرسپولیس پروژه فسخ بازیکنان را کلید زدند
❌
از عملکرد امید عالیشاه اصلا راضی نبودند ؛ ومرتضی پورعلی‌ گنجی، میلاد سرلک ، رضا شکاری ، تیوی بیفوما و  دنیل گرا  بازیکنانی هستند که نامشان در لیست سیاه باشگاه دیده می‌شود. مدیران پرسپولیس چند گزینه جوان…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/134832" target="_blank">📅 12:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134831">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
خداداد عزیزی: ایرادات و مشکلاتی در پرسپولیس هست که این تیم را دچار بحران و حاشیه کرده است و تا حالا این مدل کار کردن رو ندیده بودم. در صورتی که در تراکتور همه چیز با یک زنگ به زنوزی حل میشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/134831" target="_blank">📅 12:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134830">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
🔴
خداداد عزیزی:علیرضا دبیر اصرار می‌کرد برم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/134830" target="_blank">📅 12:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134829">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
🔴
دلیل ناراحتی اسکوچیچ از پرسپولیس اینه که قرار بوده باشگاه بهش پیش‌پرداخت بده که تا الان این اتفاق نیوفتاده/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/134829" target="_blank">📅 12:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134828">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❗️
❗️
عصبانیت اسکوچیچ از باشگاه
🔴
🔴
پس از مذاکره اولیه و سپس حضوری در استانبول، اسکوچیچ در انتظار ارسال قرارداد بود که این موضوع از سوی باشگاه چند بار به تاخیر افتاد و باعث دلخوری اسکوچیچ شد. هنوز هم به شکلی عجیب و سوال برانگیز در ۲۴ ساعت گذشته این اتفاق رخ نداده…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/134828" target="_blank">📅 12:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134827">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووووووووری
🔻
احمد نوراللهی در آستانه بازگشت به پرسپولیس/خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/134827" target="_blank">📅 12:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134826">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
#فوری
🗣
حضور کسری طاهری در پرسپولیس منتفی شد / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/134826" target="_blank">📅 11:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134825">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✅
با اعلام ترانسفر مارکت محمد قربانی بازیکن آزاد اعلام‌ شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/134825" target="_blank">📅 11:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134824">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
خداداد عزیزی :
🔴
🔴
اسکوچیچ سه هفته منتظر قرارداد با پرسپولیس بود خیلی هم راغب بود بیاد اما هر سری از طرف باشگاه بهش جواب درست نمیدادن
🔴
🔴
ما حتی برنامه ریزی نقل و انتقالات خوب کرده بودیم با چند بازیکن شاخص هم در حال توافق بودیم که همه چی بهم ریخت، داشتیم…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/134824" target="_blank">📅 11:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134823">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✅
🏆
برنامه کامل بازی‌های ۱/۱۶ نهایی جام جهانی
🇿🇦
آفریقا جنوبی - کانادا
🇨🇦
🇧🇷
برزیل - ژاپن
🇯🇵
🇳🇱
هلند - مراکش
🇲🇦
🇺🇸
آمریکا - بوسنی
🇧🇦
🇳🇴
نروژ - ساحل عاج
🇮🇪
🇫🇷
فرانسه - سوئد
🇸🇪
🇩🇪
آلمان - پاراگوئه
🇵🇾
🇲🇽
مکزیک - اکوادور
🇪🇨
🇧🇪
بلژیک - سنگال
🇸🇳
🇪🇸
اسپانیا - اتریش…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/134823" target="_blank">📅 11:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134822">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsNhXBbCzsqaPtBUO_oVyfgs_JsbrY0o2uyJllD0guDWeuj6suW04DoOJRSuL5s1DkFiM3aNty7RyVaCUCH_Tim33-fnmMQ_MaocFSRSQHlBKVaUiXslflkvIW9BvN8W4lLFTJQCwY76nZYMKBhPrBBsjwAE2b5VKrqTm-zyQ3plDGS_zYxmGvlqyxHppk5-W13kvM6LV0JppNQk9yK0d-gnvymKH1gZWGNcnkLTlp8k4MPS5bIVVYWNg5YeiH6YjUUNN-ve3k7dGdGs1UpXbdYQlbMR4ON5wKKN-xJmMhJio2Gvga2ffygzVXieSzkTNKIuSrCwljdaOFeFLhF_fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
پرتغال موفق شد کرواسی رو شکست بده و در مرحله یک هشتم به مصاف اسپانیا میره.اونم فقط 72 ساعت دیگه ..تیما دیشب بازی کردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/134822" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134821">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❗️
❗️
خداداد عزیزی:
🔴
تا جایی که من میدانم اسکوچیچ به پرسپولیس نخواهد رفت و حضورش در این تیم منتفی است!
✅
وقتی سخنگوی باشگاه، ناکاربلد باشه و دانش کافی برای جلوگیری از حواشی رو نداشته باشه، باید هم خداداد عزیزی در نقش سخنگو بیاد درمورد مسایل تیم ما صحبت کنه.…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/134821" target="_blank">📅 10:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134820">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
رونالدو فقط انقدر تنها 25 گل با 1000 گله شدن خودش فاصله داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/134820" target="_blank">📅 10:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134819">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">لحظه‌به‌لحظه با نبض واقعی مسابقه</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/134819" target="_blank">📅 01:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134818">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مزیت عضویت در کانال ما
با عضویت در این کانال:
فوتبال را حرفه‌ای‌تر دنبال می‌کنید
از تحلیل‌های سطحی فاصله می‌گیرید
درک بهتری از تاکتیک و جریان مسابقه پیدا می‌کنید
همیشه یک قدم جلوتر از بقیه خواهید بود
اینجا فقط خبر نمی‌دهیم؛
اینجا فوتبال را کالبدشکافی می‌کنیم.
https://t.me/+hhwRu0jTAzswN2Nk
https://t.me/+hhwRu0jTAzswN2Nk</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/134818" target="_blank">📅 01:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134817">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2ngbMOdIvVWpT2Q3znEiaHYsseQDFFQjYFoguQX17I3OKGIeWERflhuWwp1WpZSFYPDJSXCMN00ITuvysFisL5yAK5EicDuJptj_z8X_lmkVk0zguB9oiEtUqw_iEQcNHXaHrvxRQsCio2nlInP1eGz_WvGHbOiDHYakZjhM7ASbe9-xxHKijQV2YWgBjMo2f5Tw0kB7NAXzR6Kl2dYY1q1zJ5TFW4EbRAwCyNYdveiEmYmbWG-TAcZYD23T_b8o4ZdOK55LPS4Elx8z0iiUWToq1a9N3bZfLK-qTx4l30taYxEADm-gBVCC860v6q0hUca6oawaDE6EoG6IJGoqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
استوری خیلی سنگین رسول خطیبی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/134817" target="_blank">📅 00:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134816">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ul2pmuBSYFrnezAgN-LB3vo4qrM5Q-Jd54jpBn-Z3B5hAIqYzH1vZFqpRKhtzN6T63PbqwEy1AUpPwvbxv30E2WgViIBwd_cBgMOik4AUKwS7o97ZeZnxvvb3yw1yO6koWn6sn4H2B98E1M7f5LyTa-qPJ6HqYHII-izaB9sIARNijYFt3Yu_FKZVQbt_tKJ3ZPI2wVJd_x-8fwBGYTtef1cZv6WiQIcNf4g0SKuOVdGwHOMWWkswcCQ2RqwK5j0qsd-sZvg3oPIV9PdpEKG4u6zRaPVXWKYGy3Y8ftBYIY7M2L68qp6V9NKDKLFCcbY-W3A3847AFBL0YZ3zJ4vLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ادعای رسانه مصری؛ ژاوی گزینه هدایت تیم ملی ایران!
🔴
رسانه‌‌ Smashi Sports مصر، در گزارشی مدعی شد که "ژاوی هرناندز" سرمـربی سابق بارسلونا، در فهرست گزینه‌ های فدراسیون‌فوتبال ایران برای سرمربیگری تیم‌ملی قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/134816" target="_blank">📅 23:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134815">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
#جام_جهانی
🏆
کنداکتور آنلاین جام جهانی امشب و بامداد فردا مرحله یک شانزدهم نهایی:
🇪🇸
اسپانیا
🆚
اتریش
🇦🇹
⏱
ساعت ۲۲:۳۰
🇵🇹
پرتغال
🆚
کرواسی
🇭🇷
⏱
ساعت ۲:۳۰
🇨🇭
سوئیس
🆚
الجزایر
🇩🇿
⏱
ساعت ۶:۳۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/134815" target="_blank">📅 23:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134814">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
زنوزی: هدف خداداد از صحبت با پرسپولیس فقط خوشحال کردنشون بوده وگرنه میدونستم نمیره پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/134814" target="_blank">📅 22:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134813">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
✅
واکنش زنوزی به انتقال اسکوچیچ به پرسپولیس: اسکوچیچ مربی بزرگیه و تونست تراکتور رو قهرمان کنه اما او بدون ابزار قهرمانی نمیتونه در یک تیم معمولی دوباره قهرمان بشه!!!!!!
🔴
🔴
پ.ن آقای حدادی آقایون بانک شهر بهتون بربخورههههه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/134813" target="_blank">📅 22:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134812">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
زنوزی: طرفداران تراکتور از گالاتاسرای و فنرباغچه بیشتر هستند
😆
😆
😆
در ترکیه ابتدا طرفدار تراکتور هستند سپس تیم شهرشان. خیابان‌های تبریز شلوغ‌تر از خیابان‌های استانبول بود. امکان نداره طرفدار گالاتاسرای، فنرباغچه و بشیکتاش بیشتر از تراکتور باشه
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/134812" target="_blank">📅 22:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134811">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/134811" target="_blank">📅 22:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134810">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
زنوزی: طرفداران تراکتور از گالاتاسرای و فنرباغچه بیشتر هستند
😆
😆
😆
در ترکیه ابتدا طرفدار تراکتور هستند سپس تیم شهرشان. خیابان‌های تبریز شلوغ‌تر از خیابان‌های استانبول بود. امکان نداره طرفدار گالاتاسرای، فنرباغچه و بشیکتاش بیشتر از تراکتور باشه
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/134810" target="_blank">📅 22:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134809">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
زنوزی: طرفداران تراکتور از گالاتاسرای و فنرباغچه بیشتر هستند
😆
😆
😆
در ترکیه ابتدا طرفدار تراکتور هستند سپس تیم شهرشان. خیابان‌های تبریز شلوغ‌تر از خیابان‌های استانبول بود. امکان نداره طرفدار گالاتاسرای، فنرباغچه و بشیکتاش بیشتر از تراکتور باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/134809" target="_blank">📅 22:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134808">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❗️
صفحه رسمی باشگاه دهوک عراق عکس ها و ویدیویی هایی از معارفه یحیی گل محمدی و دستیارش محمد عسگری را در پست و استوری به اشتراک گذاشته که نشان می دهد مراسم معارفه ویژه ای جذب پرافتخارترین مربی ایران در جام های سراسری برگزار شده است.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/134808" target="_blank">📅 21:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134806">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">💥
❌
با مالیاتش میشه ۲.۵ میلیون دلار معادل ۵۰۰ میلیارد تومن/نیم همت
🫦
بدون احتساب اپشن ها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/134806" target="_blank">📅 21:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134805">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">⭕️
🔴
افشاگری تازه؛ ایجنت اسکوچیچ و درخواست جنجالی ۱.۸ میلیون دلاری
🔴
شنیده‌ها حاکی از آن است که ایجنت دراگان اسکوچیچ به دنبال عقد قراردادی ۱.۸ میلیون دلاری برای این سرمربی است؛ رقمی که فاصله قابل‌توجهی با قراردادهای قبلی او در تراکتور دارد.
❗️
اسکوچیچ در فصل…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/134805" target="_blank">📅 21:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134804">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
🚨
بانک شهر حضور اسکوچیچ در پرسپولیس رو مصوب کرده و امشب یا فردا باید قرارداد برای امضا به این مربی ارسال بشه/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/134804" target="_blank">📅 21:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134803">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet.apk</div>
  <div class="tg-doc-extra">54.1 MB</div>
</div>
<a href="https://t.me/SorkhTimes/134803" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
جدیدترین آپدیت اندروید 1XBET
✅
ورود / ثبت نام از اپلیکیشن
🎖
بزرگترین اسپانسر رسمی لالیگا
🔵
حتما
بدون فیلترشکن
از اپلیکیشن استفاده کنید
🎁
هنگام ثبت نام کد هدیه 130 دلاری vipfarsi را وارد کنید.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/134803" target="_blank">📅 21:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134802">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxnzr4YYEBDv5ducyXym0OzaRbNJaScjP94hFzSZzQo3WmaJqDR9P0yTgoC7VZ9D7V4Mnc8F5DOgWM_nT_5zYwTRsfpxyn3R3t8rFNS5YSU4VMGEQPYLAr9LDecHtzUwLFSCeadkicuPD9LI4Ig73ejshzX6d0j8rK_d0AUCn72Biv3T2dPIXcS2BibKJtxfEeh5tG8a7BUyActVYadp9WKrztNiAv2SUOROGbilcvQPXPr5yBQcRztxJGZsXSzlkumuyIpuDdyFcmvRSCHB6XzLaMQPlov3JinULpQZpsjLBZEhWBT8mRwNKodhfplDP5pMDiDbIN1oK5rjE5nhbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1️⃣
وان‌ ایکس بت برترین و خفن ترین سایت پیش بینی بین المللی که به کاربران ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
vipfarsi
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر بازپرداخت هدیه میدهد
🔔
آموزش ثبت نام، واریز و برداشت
🟦
آدرس وان‌ایکس‌بت:
🌐
Link :
1XBET.COM
🌐
Link :
1XBET.COM
🔑
برای ورود به سایت از وی پی ان (فیلترشکن) کشور های آسیایی یا کانادا یا ترکیه استفاده کنید.
➖
➖
➖
➖
➖
➖
➖
➖
🌐
Channel :
@iran1xbet_official</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/134802" target="_blank">📅 21:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134801">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/134801" target="_blank">📅 21:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134800">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
🚨
بانک شهر حضور اسکوچیچ در پرسپولیس رو مصوب کرده و امشب یا فردا باید قرارداد برای امضا به این مربی ارسال بشه/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/134800" target="_blank">📅 21:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134799">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
فوتبالی : پاسخ مبهم دروژدک به دوراهی تراکتور - پرسپولیس
✅
مذاکره پرسپولیس با دراگان اسکوچیچ شایعات حضور احتمالی دروژدک در جمع قرمزهای تهران را ایجاد کرده و گفته می‌شود اسکوچیچ در صورت حضور در پرسپولیس، هموطن خود را هم به این تیم خواهد برد.
❗️
و در همین راستا…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/134799" target="_blank">📅 21:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134798">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
❗️
عصبانیت اسکوچیچ از باشگاه
🔴
🔴
پس از مذاکره اولیه و سپس حضوری در استانبول، اسکوچیچ در انتظار ارسال قرارداد بود که این موضوع از سوی باشگاه چند بار به تاخیر افتاد و باعث دلخوری اسکوچیچ شد. هنوز هم به شکلی عجیب و سوال برانگیز در ۲۴ ساعت گذشته این اتفاق رخ نداده…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/134798" target="_blank">📅 21:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134797">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔽
در جلسه هیات مدیره صحبت از پنج گزینه ایرانی و یک گزینه خارجی به عنوان الترناتیو اسکوچیج شده تا اگر جذب او به هر دلیل میسر نشد چه کنند
🖥
ممکن است درباره گزینه های خارجی دیگری هم در جلسات صحبت شده باشد.ما از اینکه نام،عملکرد،رزومه،زشت و زیبا و شرایط ۵ سر مربی…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/134797" target="_blank">📅 21:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134796">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W25nY1GpxJlgtCcgyZltsL4MQIzmDbJ-Pf7T8z33lE_xiaE_1EeUnMnG7OUfSqXwa3G4CmPhn7DFDtreUv6BIuSuiRH8sHK691biMfo7VGL2E2vlWLu4EDj-hh01LkqrCLasP0SAg_BWzl5ymBg9ejZlNuN7HpmC-fPsugrQm_ZCXCVPXd6GvB1b1iARyoREikvNVxkVrwkcWtpoN3_bDI2c0JXlXx3ygzzs7t2KptH5GyULIOer6lUAWR_NStYUnh53uPu5ho1FNlbwIk0bnye9BhQm4lUurRFfZ_HJv19bHSb7nsw8GbGMkf08P2EJCU09yRuo99aIbIoT5oNWpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عارف آیمن بازیکنی که در دو فصل اخیر بسیار به پرسپولیس لینک شده بود؛ بالاخره بازیکن آزاد شد
❗️
موافق جذب این بازیکن مالزیایی هستید یا خیر؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/134796" target="_blank">📅 21:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134795">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLYtaOu4gIrX2EISWWb4yVlKA6MwiS53mJOnYmwBZlBYXnXUJIFD9W4slBbqH5KkTB3h7ah2gXCQrlF9KNMkWwyVydAcWJ8R3TACHjQmPiw0sDG-oTXi1FlxNvtLp-gBGxC4KLNp9l8NrdvwfP_dmfdms9pKU4zCLgRtG-5SlNIVv1gq5VLdB0dhnSVn-VZ1X0WySGg0DlW3ILPL70ybZ-ByVgwW_ujYwKBtAjdPDBWCa7hyINg6Th_9pZ7NK0FQxWzOBfv7qd6d4sff7vEyiWwMEalur_PgtPAb1qvyit2kC9COnBBasXbysx6C--wujVlLEvODEslEC3Icicwd0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عارف آیمن بازیکنی که در دو فصل اخیر بسیار به پرسپولیس لینک شده بود؛ بالاخره بازیکن آزاد شد
❗️
موافق جذب این بازیکن مالزیایی هستید یا خیر؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/134795" target="_blank">📅 21:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134794">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
❗️
خداداد عزیزی:
🔴
تا جایی که من میدانم اسکوچیچ به پرسپولیس نخواهد رفت و حضورش در این تیم منتفی است!
✅
وقتی سخنگوی باشگاه، ناکاربلد باشه و دانش کافی برای جلوگیری از حواشی رو نداشته باشه، باید هم خداداد عزیزی در نقش سخنگو بیاد درمورد مسایل تیم ما صحبت کنه.…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/134794" target="_blank">📅 20:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134793">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❗️
❗️
خداداد عزیزی:
🔴
تا جایی که من میدانم اسکوچیچ به پرسپولیس نخواهد رفت و حضورش در این تیم منتفی است!
✅
وقتی سخنگوی باشگاه، ناکاربلد باشه و دانش کافی برای جلوگیری از حواشی رو نداشته باشه، باید هم خداداد عزیزی در نقش سخنگو بیاد درمورد مسایل تیم ما صحبت کنه.…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/134793" target="_blank">📅 19:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134792">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✅
منتفی پشت منتفی..کنسل پشت کنسل  ..نمی‌دونم باشگاه داره چی کار می‌کنه .نه بازیکن گرفتیم .نه سرمربی داریم ....بیاین جواب ملیون ها هوادار و بدین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/134792" target="_blank">📅 19:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134791">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✅
منتفی پشت منتفی..کنسل پشت کنسل  ..نمی‌دونم باشگاه داره چی کار می‌کنه .نه بازیکن گرفتیم .نه سرمربی داریم ....بیاین جواب ملیون ها هوادار و بدین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/134791" target="_blank">📅 19:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134790">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❗️
❗️
خداداد عزیزی:
🔴
تا جایی که من میدانم اسکوچیچ به پرسپولیس نخواهد رفت و حضورش در این تیم منتفی است!
✅
وقتی سخنگوی باشگاه، ناکاربلد باشه و دانش کافی برای جلوگیری از حواشی رو نداشته باشه، باید هم خداداد عزیزی در نقش سخنگو بیاد درمورد مسایل تیم ما صحبت کنه.…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/134790" target="_blank">📅 19:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134789">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❗️
❗️
خداداد عزیزی:
🔴
تا جایی که من میدانم اسکوچیچ به پرسپولیس نخواهد رفت و حضورش در این تیم منتفی است!
✅
وقتی سخنگوی باشگاه، ناکاربلد باشه و دانش کافی برای جلوگیری از حواشی رو نداشته باشه، باید هم خداداد عزیزی در نقش سخنگو بیاد درمورد مسایل تیم ما صحبت کنه.…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/134789" target="_blank">📅 19:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134788">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
خداداد عزیزی: حضورم در پرسپولیس منتفی شد و در تراکتور می‌مانم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/134788" target="_blank">📅 19:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134787">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
✅
سعید اخباری کاری رو کرد که طی ۵ ۶ فصل اخیر لیگ برتر هیچ مربی انجام نداده بود
🔴
آسیایی کردن یک تیم غیر از تیم های پرسپولیس،  استقلال ، تراکتور ، سپاهان و فولاد
🔴
آخرین بار یحیی گل محمدی پدیده رو آسیایی کرده بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/134787" target="_blank">📅 17:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134786">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/134786" target="_blank">📅 17:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134785">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قدوسی: برخی منابع ما تاکید دارند قرارداد با اسکوچیچ امضا هم شده و حالا دنبال تخفیف و برخی مسائل هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/134785" target="_blank">📅 17:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134784">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
🔴
عادل‌فردوسی‌پور: تمام توافقات لازم انجام شده؛ دراگان اسکوچیچ سرمربی  پرسپولیس خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/134784" target="_blank">📅 17:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134783">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
✅
فوووووووووووووووووری
🔴
🔴
فرهیختگان: در صورت پیوستن اسکوچیچ به پرسپولیس هلیلویچ و دروژدک دو بازیکن خارجی پرسپولیسی خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/134783" target="_blank">📅 17:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134782">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoHvZrg5-9fTtBUEXiEq4N7ov0S3q1irTg_aX4cBT4foV5bUA9QztHWTb7V4FOzkfv1gvDgVLbo3vkkrtCvFawzuPpSg6l5EDop732LUPm5-FGTRxp3_CDhnCIKcCP1kWNs9UZ3ivQ8rsH_x-jLdLxIQR2oJdfKsA9Ux9V2vRd5EiNazo19n140agrBgRfMj1RwLGKBHEJ_Dc36yEZ1ngyNGv1O840ncyFMzhdoP2EfS4c6pFCgqT6shTTPVlX0TtrWoQDNlqm9oFK1leQveAqZhtWKDdVloi0O7m-P93Ygg2hwTFkso4GlURz8zOXDp_2FV6OlDd6-mU2APCit0EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صحبت های جنجالی سوشا مکانی:
🔖
🔖
علیرضا بیرانوند اسمش علیرضا نیست و این آدم اسمش محمد صفر بیرانوند بود و تا 12 سالگی شناسنامه نداشت چون در محله‌ای که زندگی می‌کرد که شناسنامه نداده بودن، بعدش کلی پول به پسر عموش داد تا براش شناسنامه جعلی جور کنه و سنش رو هم اشتباه زده و الان با یک اسم و هویت جعلی زندگی میکنه و با همین ترفند سربازیش رو عقب انداخته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/134782" target="_blank">📅 16:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134780">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❗️
یاسین سلمانی پس از ۱ سال و ۴ ماه در ترکیب اصلی پرسپولیس قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/134780" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134779">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/SorkhTimes/134779" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/134779" target="_blank">📅 15:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134778">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bX7XIYVXYyXzM5BhSAVqUeyMlCtmvcI7WWW8F8Yqnks6oZvRpFsFVkG2xJQMTXXY1Y--oOmcIykknySRLNDECRH-iSsErPe6zjeDRc8cubOrH-944vxEmn0pSGvlRc3XtEP0vaR9ENgdPdIheu1AH6lIfwKQGbo4VhgLfGCKfVnf7p4De6Mc5WQnlmIvzS3M7mVGbPkOrHVNL_iKQyhJvhxssMg5lBfIRKE9RAHyF2BZlZLMVJXzFTsXRKtppBRqGDa5fOYFj8RGj12nNfaI95egOPtI5tb0gE1proab5pJXZ-GH4_zGFCGVbv6kecA-HaqYIpr7K8zZ-h4bBFqCIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🆕
Link
🔜
MelBet1.net
✅
🆕
Link
🔜
MelBet1.net
✅</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/134778" target="_blank">📅 15:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134777">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">#نظر_شخصی | #شفاف_سازی
📌
این وسط ممکنه یکسری ها بخان از آب گلالود ماهی بگیرن و به نفع گزینه های خودشون شمشیر بزنن ولی موضع من مشخصه
🚩
من حالم از یحیی و هرچی مربی ایرانی بهم میخوره اسم مربی ایرانی میاد بدنم کهیر میزنه،و هیچوقت هم از اینکه پشت درویش درآومدم…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/134777" target="_blank">📅 15:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134776">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
🔴
مهدی رحمتی :از امیر قلعه‌نویی تعجب میکنم، اولین چیزی که او به من گفت، این بود که به هیچ‌کس هیچ قولی نده، اما خود او قول صعود داد.
🔴
🔴
اولین هدف آن ها صعود از گروه بود اما اتفاق نیوفتاد، پس بیایید عذرخواهی کنید، تاج و قلعه نویی باید حداقل از مردم عذرخواهی…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/134776" target="_blank">📅 14:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134775">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
🏆
برنامه کامل بازی‌های ۱/۱۶ نهایی جام جهانی
🇿🇦
آفریقا جنوبی - کانادا
🇨🇦
🇧🇷
برزیل - ژاپن
🇯🇵
🇳🇱
هلند - مراکش
🇲🇦
🇺🇸
آمریکا - بوسنی
🇧🇦
🇳🇴
نروژ - ساحل عاج
🇮🇪
🇫🇷
فرانسه - سوئد
🇸🇪
🇩🇪
آلمان - پاراگوئه
🇵🇾
🇲🇽
مکزیک - اکوادور
🇪🇨
🇧🇪
بلژیک - سنگال
🇸🇳
🇪🇸
اسپانیا - اتریش…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/134775" target="_blank">📅 14:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134774">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✅
محمد نصرتی درباره حضور دنیس اکرت در جام جهانی: آقای قلعه‌نویی، با دعوت از اکرت در حق یکسری بازیکن جوان اجحاف کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/134774" target="_blank">📅 13:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134772">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puZuNoagL32_YGadztkK6vipjvw5e8vwjErjjQwxlWDXZHmqxsklzdAwTRkfrYXpefEHN4YsyYRCrCE6dQrCCN0vdFvDipRTEmpB3mDPLTkq9S3_ViP9eyf24md2Ce5TueJnnyu6ylP3eSLfnPpr2rUyz9T0F8XO9yNEhIy0hFegAgxfsum2CmdsQZABj-BnT0a_UjpLNY35Xm9YMHxeO_FZP2xQTdLFmkmRmOoREP4qQetShomXLDOJb3e1qX2MfLIDIWHnYhNf5IsNwECem-7L5ycrfiFcAQr4e2h1oW_p2FbfNot1Iv2O9l5Z60tqxHToIIXLnvdD3f9o_tNGmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ماجرا وقتی عجیب میشه که بدونیم سانل کونیویچ دستیار اول اسکوچیچ در تراکتور دیروز با یک تیم اسلوونیایی قرارداد بست !
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/134772" target="_blank">📅 12:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134771">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⛔️
⚠️
گوساله! گوساله هایی که نیم فصل با هرچی اوسمار بگه، اوسمار نیارید تجمع میکنیم کیر زدید به تیم مادر تیم رو گاییدید
◀️
اینقدر گاب نباشید آدم پرستا،هدف باید موفقیت پرسپولیس باشه فرد مهم نیست
◀️
یه مشت رسانه تخمی دارن تیمو به گوه میکشن باشگاه باید همه شونو تخته کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/134771" target="_blank">📅 12:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134770">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
◀️
باشگاه پرسپولیس درآمد و سود امسال از برند و لوگوی خود (منهای پول اسپانسر و‌ مالک) را 771 میلیارد تومان اعلام کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/134770" target="_blank">📅 12:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134769">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">#نظر_شخصی
📌
دوستان من نظر شخصیم میگم ممکنه خیلی ها موافق یا مخالف صحبت های من باشن که عقیده همه برام محترمه
📌
از دید من اقای اسکوچیچ مربی بسیار خوبیه و بنظرم باهاش میتونیم نتیجه بگیریم، اما چنتا نکته هست که منو نگران میکنه
📌
مورد اول:اسکوچیچ نشون داده قدرت…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/134769" target="_blank">📅 12:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134768">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⭕️
🔴
افشاگری تازه؛ ایجنت اسکوچیچ و درخواست جنجالی ۱.۸ میلیون دلاری
🔴
شنیده‌ها حاکی از آن است که ایجنت دراگان اسکوچیچ به دنبال عقد قراردادی ۱.۸ میلیون دلاری برای این سرمربی است؛ رقمی که فاصله قابل‌توجهی با قراردادهای قبلی او در تراکتور دارد.
❗️
اسکوچیچ در فصل…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/134768" target="_blank">📅 12:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134766">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» حدادی شخصا میخاد با امید عالیشا،میلاد سراک،رضا شکاری،مرتضی پورعلی گنجی،دنیل گرا و تیوی بیفوما فسخ کنه.
❌
حالا باید ببینیم بانک شهر برای فسخ و آوردن بازیکن جایگزین بودجه میده یا نه
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/134766" target="_blank">📅 11:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134765">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78b91b0d6.mp4?token=bu-rPRrvBW9PQB6dFJjkfKIQP1WEywK01YHyAjl_D708GPCIKpHLjH2Uinu6X7aLqMOtInz4El3IhjNUktnkltWUobJ8BYLhlJf8hQpa7H5lDPPR2wlY5AQF_tCVnzEy1XD3qeUMZEfphJLqaoCVrSO88uILA4wlPnIeEk0t_W5UDFhbabCJjrg4agXAeMvHLvDkYTVHPViVzsD9I9OmRCAPahkvm7BHDRojeH1nPrlOKMNL53tZxAZsYxmHFqwYnJfrLRF_fDsfYY8mLgbC9heeck6Pq_7Ny3KC4nWuxpkurgNrH65c0aiaF28pZbuS7MHUGa6PLnJLdrAsLKOXUTdH1A_OapVkSKMpg8kneoj5ifTbjIlh_zmRa4rD033YtX3MgPD57zXASDLxxcAU11Eb_1QSTyw9bt5QNYesFCw2TF0J96mXFiiRd5YNK8IW0o3hWL1Z8M_L_lVkgv8p3Q4HQwphT3ETgB2Xnyz8e1qwsDL54YzHbDsjhAssJTugokCgjNuHNrIyrEgCu1f6NnWgyOA5hmh9d7UezmjdUXgpm7XrNKK-xRUTH01CAwqCcIsejNfleyQQb90LBRnutvN4ccsnisUkITPfhwVsSXPv2Yw0lPtlqyojaezjf9Mk1_WCcRWSoRFZFxlijuSoX7slXaE8stkTQINS6_ANiPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78b91b0d6.mp4?token=bu-rPRrvBW9PQB6dFJjkfKIQP1WEywK01YHyAjl_D708GPCIKpHLjH2Uinu6X7aLqMOtInz4El3IhjNUktnkltWUobJ8BYLhlJf8hQpa7H5lDPPR2wlY5AQF_tCVnzEy1XD3qeUMZEfphJLqaoCVrSO88uILA4wlPnIeEk0t_W5UDFhbabCJjrg4agXAeMvHLvDkYTVHPViVzsD9I9OmRCAPahkvm7BHDRojeH1nPrlOKMNL53tZxAZsYxmHFqwYnJfrLRF_fDsfYY8mLgbC9heeck6Pq_7Ny3KC4nWuxpkurgNrH65c0aiaF28pZbuS7MHUGa6PLnJLdrAsLKOXUTdH1A_OapVkSKMpg8kneoj5ifTbjIlh_zmRa4rD033YtX3MgPD57zXASDLxxcAU11Eb_1QSTyw9bt5QNYesFCw2TF0J96mXFiiRd5YNK8IW0o3hWL1Z8M_L_lVkgv8p3Q4HQwphT3ETgB2Xnyz8e1qwsDL54YzHbDsjhAssJTugokCgjNuHNrIyrEgCu1f6NnWgyOA5hmh9d7UezmjdUXgpm7XrNKK-xRUTH01CAwqCcIsejNfleyQQb90LBRnutvN4ccsnisUkITPfhwVsSXPv2Yw0lPtlqyojaezjf9Mk1_WCcRWSoRFZFxlijuSoX7slXaE8stkTQINS6_ANiPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
درخواست عجیییییییب هواداران پرسپولیس از علیرضا بیرانوند
🔴
«برگرد پرسپولیس»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/134765" target="_blank">📅 11:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134764">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✅
🏆
برنامه کامل بازی‌های ۱/۱۶ نهایی جام جهانی
🇿🇦
آفریقا جنوبی - کانادا
🇨🇦
🇧🇷
برزیل - ژاپن
🇯🇵
🇳🇱
هلند - مراکش
🇲🇦
🇺🇸
آمریکا - بوسنی
🇧🇦
🇳🇴
نروژ - ساحل عاج
🇮🇪
🇫🇷
فرانسه - سوئد
🇸🇪
🇩🇪
آلمان - پاراگوئه
🇵🇾
🇲🇽
مکزیک - اکوادور
🇪🇨
🇧🇪
بلژیک - سنگال
🇸🇳
🇪🇸
اسپانیا - اتریش…</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/134764" target="_blank">📅 11:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134763">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
🚨
محمدحسین میثاقی: دراگان اسکوچیچ با عقد قراردادی دوساله سرمربی پرسپولیس شد. اسکوچیچ هم اکنون ترکیه است و به زودی میاد ایران!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/134763" target="_blank">📅 11:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134762">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⭕️
🔴
افشاگری تازه؛ ایجنت اسکوچیچ و درخواست جنجالی ۱.۸ میلیون دلاری
🔴
شنیده‌ها حاکی از آن است که ایجنت دراگان اسکوچیچ به دنبال عقد قراردادی
۱.۸ میلیون دلاری
برای این سرمربی است؛ رقمی که فاصله قابل‌توجهی با قراردادهای قبلی او در تراکتور دارد.
❗️
اسکوچیچ در فصل قهرمانی با تراکتور قراردادی
۷۰۰ هزار دلار
داشت،همچین قرارداد فصل  قبل او حدود
۱.۳ میلیون دلار
عنوان شده است.
❗️
از سوی دیگر، در حالی که هنوز توافق نهایی حاصل نشده، گفته می‌شود اتاق فکر آقای سردبیر از همین حالا مشغول برنامه‌ریزی و بستن تیم برای فصل آینده است.
❗️
همچنین مراجع ذی ربط به دلیل مسائل امنیتی به باشگاه توصیه کردن از جذب اسکوچیچ صرف نظر کنند
❗️
اگر این ادعاها صحت داشته باشد، روزهای پرحاشیه‌ای در انتظار باشگاه خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/134762" target="_blank">📅 10:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134761">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/134761" target="_blank">📅 10:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134760">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✅
✅
فوووووووووووووووووری
🔴
🔴
فرهیختگان: در صورت پیوستن اسکوچیچ به پرسپولیس هلیلویچ و دروژدک دو بازیکن خارجی پرسپولیسی خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/134760" target="_blank">📅 10:18 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
