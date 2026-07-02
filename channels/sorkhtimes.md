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
<img src="https://cdn4.telesco.pe/file/GI7TGwWfZbo2pOKp_iVLOFpUaNXsNWKSU-B6fNE8IIP7PKdKzxcRhvndyYVZw5k6JJoBN9XIbk8-CDN2pyiMuvQ7Dinu7Nbk1m2WYF1JUwOY6DeyJVe4yMORlY6w7zbnrziWW1HwvfBKn05zOXqv8IB7zMsXbuKAF2MxIyUPTqOJlEmD8wG0iWognD_Jg1MsQNlMX4qoRet8RGKA5mBPPCqVao9jb31I3E7eo6TDYnHuR2cxNZmjEQrdwqOMwTWv_kv6ZgFCDyYYSa7Cklwpo9iVm4R3MuZ_PNEP3_73vOXuFuUKI75N_o8AEOHCf51F28Q6dVM8VfF-qC34m7BjPg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 18:05:51</div>
<hr>

<div class="tg-post" id="msg-134787">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
✅
سعید اخباری کاری رو کرد که طی ۵ ۶ فصل اخیر لیگ برتر هیچ مربی انجام نداده بود
🔴
آسیایی کردن یک تیم غیر از تیم های پرسپولیس،  استقلال ، تراکتور ، سپاهان و فولاد
🔴
آخرین بار یحیی گل محمدی پدیده رو آسیایی کرده بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 671 · <a href="https://t.me/SorkhTimes/134787" target="_blank">📅 17:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134786">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/134786" target="_blank">📅 17:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134785">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قدوسی: برخی منابع ما تاکید دارند قرارداد با اسکوچیچ امضا هم شده و حالا دنبال تخفیف و برخی مسائل هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SorkhTimes/134785" target="_blank">📅 17:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134784">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
🔴
عادل‌فردوسی‌پور: تمام توافقات لازم انجام شده؛ دراگان اسکوچیچ سرمربی  پرسپولیس خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/SorkhTimes/134784" target="_blank">📅 17:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134783">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/SorkhTimes/134783" target="_blank">📅 17:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134782">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bx9UzpYT-p4iSuVy3jqcjuj8GvitjhMounH6BZP9jgL50rlLRHV-AIXAAFGqKWdRjyf02X8pt_7plQybhwtV1o3aN2bdLElySULFzPW7WprHLkVpaMUA82kjzf_AYjnvKzz0eSQ0LFKp7D_GvKAuY4iA54-TW2ul-nkoWBDDN4o-bLceaZkEpLuPrtxlr4GErFLq0TdudEnKhfoE5vTC90tCaR6tKk6OUFlcdHuTFLXw63NlAStFmiIuw32AlvAR64TZH8NxajrViwLW2GjhvcYT19PF3juWtqqgGmjl6A2N3_UHb4fOAzPvOTkb-wAPm4bZ77yDYRiPT3izMuOrKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SorkhTimes/134782" target="_blank">📅 16:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134780">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❗️
یاسین سلمانی پس از ۱ سال و ۴ ماه در ترکیب اصلی پرسپولیس قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/134780" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134779">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/134779" target="_blank">📅 15:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134778">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u17BJjfrg-yH4h4q1WuiRHBB-_EDSHSleWQ-mJl8GkAoFqVnNihZhugi-4TZTliWPT9ku3-9H7cZ-atM6vEHDb961XHc-CVxs9nmXF49V_WewaseQuT33NmfaRmwd4EjOgnCOOJNL1VvXrczqb5_c7Y49WJJrmOQN2aDmwM64dJlFdEOuRCUaSLcZdp0QYL__KsvOVlDZwfLNbXc7z49y6QKB0KcDzXcP0DLfiI1LRweJITnwHyc1e3Qt1VKZW16uFbaCqoB9NaMd7sMax09H6yuKdt2Ku6dXeZhQKdL4BMecUJWfhTVmPxFVJsmn503uoZSs7W8jF5PziuSe-UQJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/134778" target="_blank">📅 15:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134777">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">#نظر_شخصی | #شفاف_سازی
📌
این وسط ممکنه یکسری ها بخان از آب گلالود ماهی بگیرن و به نفع گزینه های خودشون شمشیر بزنن ولی موضع من مشخصه
🚩
من حالم از یحیی و هرچی مربی ایرانی بهم میخوره اسم مربی ایرانی میاد بدنم کهیر میزنه،و هیچوقت هم از اینکه پشت درویش درآومدم…</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/134777" target="_blank">📅 15:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134776">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
🔴
مهدی رحمتی :از امیر قلعه‌نویی تعجب میکنم، اولین چیزی که او به من گفت، این بود که به هیچ‌کس هیچ قولی نده، اما خود او قول صعود داد.
🔴
🔴
اولین هدف آن ها صعود از گروه بود اما اتفاق نیوفتاد، پس بیایید عذرخواهی کنید، تاج و قلعه نویی باید حداقل از مردم عذرخواهی…</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/134776" target="_blank">📅 14:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134775">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/134775" target="_blank">📅 14:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134774">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
محمد نصرتی درباره حضور دنیس اکرت در جام جهانی: آقای قلعه‌نویی، با دعوت از اکرت در حق یکسری بازیکن جوان اجحاف کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/134774" target="_blank">📅 13:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134772">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/us_Ry5Xh7MLgZZaNYXMf7SuYGGYWbdOZbKNM7M1PKyDTH6IUoV6WvXPnP4JwYzDFCVPMOFJorI0Mqa02uFgwjDvgANizE8klNjjYBsr7BUyxGlNIh8uRI2b0hLCiVld0c1X_XQMlOFDCa4I0PtZSdZX3GCSCVD-lML9Aiy4pNfGJlN1kswggfpnWP68uwkmtp9qQ7Y619E7WARld3sd_4r5a6XI1pRwkUPzgXfN1MrNfUJJ13IK5y5owujHscohzUOkjQ9eo7HBgYoFVaY5vWU9TxYxd7OF-aJbQfd1uoIIgaUGD6lrMM-d-JWuw-fS6tgHbrKVXP4ZvdHtEU8730g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ماجرا وقتی عجیب میشه که بدونیم سانل کونیویچ دستیار اول اسکوچیچ در تراکتور دیروز با یک تیم اسلوونیایی قرارداد بست !
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/134772" target="_blank">📅 12:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134771">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/134771" target="_blank">📅 12:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134770">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
◀️
باشگاه پرسپولیس درآمد و سود امسال از برند و لوگوی خود (منهای پول اسپانسر و‌ مالک) را 771 میلیارد تومان اعلام کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/134770" target="_blank">📅 12:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134769">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">#نظر_شخصی
📌
دوستان من نظر شخصیم میگم ممکنه خیلی ها موافق یا مخالف صحبت های من باشن که عقیده همه برام محترمه
📌
از دید من اقای اسکوچیچ مربی بسیار خوبیه و بنظرم باهاش میتونیم نتیجه بگیریم، اما چنتا نکته هست که منو نگران میکنه
📌
مورد اول:اسکوچیچ نشون داده قدرت…</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/134769" target="_blank">📅 12:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134768">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⭕️
🔴
افشاگری تازه؛ ایجنت اسکوچیچ و درخواست جنجالی ۱.۸ میلیون دلاری
🔴
شنیده‌ها حاکی از آن است که ایجنت دراگان اسکوچیچ به دنبال عقد قراردادی ۱.۸ میلیون دلاری برای این سرمربی است؛ رقمی که فاصله قابل‌توجهی با قراردادهای قبلی او در تراکتور دارد.
❗️
اسکوچیچ در فصل…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/134768" target="_blank">📅 12:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134766">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» حدادی شخصا میخاد با امید عالیشا،میلاد سراک،رضا شکاری،مرتضی پورعلی گنجی،دنیل گرا و تیوی بیفوما فسخ کنه.
❌
حالا باید ببینیم بانک شهر برای فسخ و آوردن بازیکن جایگزین بودجه میده یا نه
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/134766" target="_blank">📅 11:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134765">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78b91b0d6.mp4?token=OmYfvNqo8eIreixM8jzvjYrL5zapUhKrrp82xNyAkzK9LmFzB1czQdg9MvcM5JzVve3tsSOJ83JHeIic80Nxkhnr8o1vKJO79kCTpOcz8cqWJiGw2e4R7EJzp7Xo9Tb5tr8GN1XHeTc2DJgJXodvPaj-IBcYKtRgOO143NFKKlx0STbWSFdO3vouSQPIKwCRqZCMBsvgfPYvqGyrRU1Ha1uXNe1wh54gOX8mlpDOpapfpWZ-V2_uv398yQb7TqMz4dojdBv24Tlays7SJWxmAWa8A_6tguGhlfNgdfpPsPznxHR_W_cTZOEDR3pxEk7uNqFpnI3D163A6Fs1zsKOt3yrDzF0ne51s40T13hxs6EIyTc7lWeCYtJZjF93zLsJMzBiEalEAJXM0dNMWcthEJjvv1OjBXGem5HBtCIE8xy1GbeOdM7x_2MmGWrZ8by0BHv8yjnfUE2QRZJd251ZevColTG8Dr9eeeYcgk5GNJkkgIDV8PjlMubJATc3zGqzPoDfwKHhKdiltvkwwmiVZn73oGRkMewTn9s9NFUX9shmrvcByMKAaLpswWTmipQLPk8ZVzDIh3jXPpj5HWVn109lJE8z2aYyEogP3RjCIBtOhOW2D0GM6zUpUbpC51wanWasJf1vZsZbNJX2Vy8ufcJRtjO6Kv_p5sgRNWdvSMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78b91b0d6.mp4?token=OmYfvNqo8eIreixM8jzvjYrL5zapUhKrrp82xNyAkzK9LmFzB1czQdg9MvcM5JzVve3tsSOJ83JHeIic80Nxkhnr8o1vKJO79kCTpOcz8cqWJiGw2e4R7EJzp7Xo9Tb5tr8GN1XHeTc2DJgJXodvPaj-IBcYKtRgOO143NFKKlx0STbWSFdO3vouSQPIKwCRqZCMBsvgfPYvqGyrRU1Ha1uXNe1wh54gOX8mlpDOpapfpWZ-V2_uv398yQb7TqMz4dojdBv24Tlays7SJWxmAWa8A_6tguGhlfNgdfpPsPznxHR_W_cTZOEDR3pxEk7uNqFpnI3D163A6Fs1zsKOt3yrDzF0ne51s40T13hxs6EIyTc7lWeCYtJZjF93zLsJMzBiEalEAJXM0dNMWcthEJjvv1OjBXGem5HBtCIE8xy1GbeOdM7x_2MmGWrZ8by0BHv8yjnfUE2QRZJd251ZevColTG8Dr9eeeYcgk5GNJkkgIDV8PjlMubJATc3zGqzPoDfwKHhKdiltvkwwmiVZn73oGRkMewTn9s9NFUX9shmrvcByMKAaLpswWTmipQLPk8ZVzDIh3jXPpj5HWVn109lJE8z2aYyEogP3RjCIBtOhOW2D0GM6zUpUbpC51wanWasJf1vZsZbNJX2Vy8ufcJRtjO6Kv_p5sgRNWdvSMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
درخواست عجیییییییب هواداران پرسپولیس از علیرضا بیرانوند
🔴
«برگرد پرسپولیس»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/134765" target="_blank">📅 11:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134764">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/134764" target="_blank">📅 11:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134763">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
🚨
محمدحسین میثاقی: دراگان اسکوچیچ با عقد قراردادی دوساله سرمربی پرسپولیس شد. اسکوچیچ هم اکنون ترکیه است و به زودی میاد ایران!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/134763" target="_blank">📅 11:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134762">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/134762" target="_blank">📅 10:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134761">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/134761" target="_blank">📅 10:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134760">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/134760" target="_blank">📅 10:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134759">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
🔴
واکنش یوسفی هوادار پرسپولیس به شایعات پخش شده در خصوص کمک برای خرید بازیکن یا سرمربی:
❌
با هیچ ارتباطی با مدیرای تیم ندارم
❌
نه بازیکن میخرم نه دخالت میکنم
⛔️
به دروغ نویسان هم باج نمی‌دهم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/134759" target="_blank">📅 09:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134758">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❗️
رسمی؛ باشگاه های اماراتی از جذب بازیکن و سرمربی ایرانی در فصل آینده لیگ ادنوک منع شدند و تمامی بازیکنان ایرانی این لیگ ها باید به ایران بازگردند/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/134758" target="_blank">📅 09:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134757">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-Rn0H2IMRbC1OOkS0Kzs5SSFNiOrvqM9NsZkQknHNhn_ew3UrbdVj-zAy5aGDB0SyxkJ4nFxcwpvxnoigO7xP4eggBgf0iDAAYwpy2JPlWfIkydyuWda0nb4hrGEAYH-BOGqOXOw1-1iPF5AKXoiarPV6yhBZ1YAuCukgOInrMhQ0IdS5FKOanXG84AJHhi7jEfFtyEXIVjvYNByKnGd7hmnY5KZJaJONlxK_ddQPH4_Tf-J4VPKo5YqKgYsipVKnI9Vr1CnR1hQr9ZWRrw2TvRY6BlOzPdA_YVVoK2LnKBcoP0N0Hf4Cnt4YxX6n79zkba239DcpVESGOkzG40jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/134757" target="_blank">📅 09:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134756">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فوتبال فقط دویدن ۲۲ نفر دنبال توپ نیست؛ جنگ افکار مربی‌هاست! اگر می‌خوای بدونی پشت پرده تصمیمات پپ گواردیولا یا کارلو آنچلوتی تو دقایق حساس چیه، جای درستی اومدی.
در [لایو تیپ]، ما بازی‌ها رو در لحظه آنالیز می‌کنیم:
📊
بررسی فرمیشن‌ها و تغییرات سیستم در جریان بازی
🎯
آنالیز تعویض‌های طلایی و تاثیر اون‌ها
🔥
بررسی نقاط کور دفاعی و فضاسازی مهاجمان
⚡️
آمار زنده و تاثیرگذار که هیچ گزارشگری به شما نمی‌گه!
اگر فوتبال رو با مغزت تماشا می‌کنی نه فقط با چشمت، جای شما اینجاست:
👇
ورود به جمع تحلیل‌گران و فوتبال‌فهم‌ها:
🔗
https://t.me/+hhwRu0jTAzswN2Nk
🔗
https://t.me/+hhwRu0jTAzswN2Nk</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/134756" target="_blank">📅 00:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134755">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
سنگال گل اول و به بلژیک زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/134755" target="_blank">📅 00:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134754">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/134754" target="_blank">📅 00:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134752">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
🚨
محمدحسین میثاقی: دراگان اسکوچیچ با عقد قراردادی دوساله سرمربی پرسپولیس شد. اسکوچیچ هم اکنون ترکیه است و به زودی میاد ایران!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/134752" target="_blank">📅 00:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134751">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسکوچیچ امضا کرده و الان رسما سرمربی پرسپولیسه/طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/134751" target="_blank">📅 00:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134750">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
هوادار متمول پرسپولیس به مدیریت گفته 3 تا بازیکن شاخص براتون میگیرم و پیگیر اینم هست افشین پیروانی به تیم برگرده / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/134750" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134749">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❗️
انگلیس از کنگو گل خورد
😐
🔴
چه جام جهانی سمی ایه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/134749" target="_blank">📅 00:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134747">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
بدرود کاپیتان دوست داشتنی ..کاپیشاه هر جا هستی موافق باشی
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/134747" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134746">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9366cf9e2.mp4?token=RNdOIvMZ9ugBOlqy_FtzeBviUdazNy_fyjCzO0EdW9hb1qvKok3_U1cNKRixI8xoVVeO0aBy0Pho8HagYVCRXHCFiL7JPTeI56LrTzVO2aSPMtNl7kmV8JE_3avo9Sk753TMXrKyemvmkjPhyhYIwnLVbZHGjRNtkpAntl1QTTlSLE8wM2YypAVxHfL713-7LZhK-UTEYIxbjh4I72hLvxjHQCX1NdmEhdbwTJH0pekd4OshsSVAL2cGK3OIDicJ5EBK23ox3C0nzPTGkmeHXfqTpeA3R2oegtP6cVlv1_cWruZvb-Y7s-WMbXUy8yp4DzWsGsPHypSTjXrAeV2o6U0gDl95iem0umYLdMCUof9hszMEd8tjm1LzwdODCe_eABkiP3iPQTsEArhIyb4Nfs_PLhd_YSy_OS1dLDlPmf4PQgMict_6wepCLp7JZ6HKFQHAPUuF3piUhnDRiqjZMXnJ_GJwEpJaHByjaENcxpJBQOCJJAyWS36mcRyYkAuprdb3jr7vwJmQ8WqBtkVE-YGdqFzED0dATyqKXXv3DGTtK-U1d6Bd42J3mLMj0J1ALnC1ulV4det1oQE-2yLIcvhhuH9L3q6D9x4immPiuqv58zH1SAaUAjOuqbdh5JnERBOGULfouu5Wvy2_jamAd9SuXNZFkWhzYPI5kOw7XD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9366cf9e2.mp4?token=RNdOIvMZ9ugBOlqy_FtzeBviUdazNy_fyjCzO0EdW9hb1qvKok3_U1cNKRixI8xoVVeO0aBy0Pho8HagYVCRXHCFiL7JPTeI56LrTzVO2aSPMtNl7kmV8JE_3avo9Sk753TMXrKyemvmkjPhyhYIwnLVbZHGjRNtkpAntl1QTTlSLE8wM2YypAVxHfL713-7LZhK-UTEYIxbjh4I72hLvxjHQCX1NdmEhdbwTJH0pekd4OshsSVAL2cGK3OIDicJ5EBK23ox3C0nzPTGkmeHXfqTpeA3R2oegtP6cVlv1_cWruZvb-Y7s-WMbXUy8yp4DzWsGsPHypSTjXrAeV2o6U0gDl95iem0umYLdMCUof9hszMEd8tjm1LzwdODCe_eABkiP3iPQTsEArhIyb4Nfs_PLhd_YSy_OS1dLDlPmf4PQgMict_6wepCLp7JZ6HKFQHAPUuF3piUhnDRiqjZMXnJ_GJwEpJaHByjaENcxpJBQOCJJAyWS36mcRyYkAuprdb3jr7vwJmQ8WqBtkVE-YGdqFzED0dATyqKXXv3DGTtK-U1d6Bd42J3mLMj0J1ALnC1ulV4det1oQE-2yLIcvhhuH9L3q6D9x4immPiuqv58zH1SAaUAjOuqbdh5JnERBOGULfouu5Wvy2_jamAd9SuXNZFkWhzYPI5kOw7XD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بدرود کاپیتان دوست داشتنی ..کاپیشاه هر جا هستی موافق باشی
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/134746" target="_blank">📅 23:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134745">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✅
✅
🚨
🚨
ایلنا: قرارداد شکاری و عالیشاه فسخ شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/134745" target="_blank">📅 23:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134744">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» حدادی شخصا میخاد با امید عالیشا،میلاد سراک،رضا شکاری،مرتضی پورعلی گنجی،دنیل گرا و تیوی بیفوما فسخ کنه.
❌
حالا باید ببینیم بانک شهر برای فسخ و آوردن بازیکن جایگزین بودجه میده یا نه
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/134744" target="_blank">📅 23:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134743">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔖
عادل فردوسی‌پور : نکنه پس‌فردا صبح با سوییس بازی داریم ما خبر نداریم اینا خبر دارن که مراسم استقبال گذاشتن
🖥
این همه تعریف از استقبال و دستاوردسازی برای چیست؟داستان تغییری نمی‌کند، ما از مرحله گروهی جام جهانی ۴۸ تیمی حذف شدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/134743" target="_blank">📅 23:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134742">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
❗️
🔴
شنیده ها:اسکو تا اخر شب رونمایی میشه بعدشم تیکدری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/134742" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134741">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emObAQUX00mLpeXd-MkjWdHKCa7MEC6Kn6vn7GGYQpyXEB7mh2YPLXhMTZXHj1P5huF_NmFuL71JnOUNR0KRjX07UWoj9KS58aAR_OrtzaTYh9GNTeOu_h9VfQj4BoTXsXRFKs_dd4fwIw4axE8J9HtBuNiBfiDBSCBKISS9gyHVee17VP-Ckl1ugIuPvKAn10wom9ETegVKMpu6969bcogz7GI10UVsUgruoF_FY2ivmOgsX-pd8RGSf2oKq_EQObyoCfvIMGnczKDrjfusjcVA232U2Rm7hZMVsgffnbPp-Y-DAc4UnDbzHAT9X9yhWJN2NCmDTjyMSCEdvA2oWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
تمرینات پرسپولیس احتمالا از روز ۱۵ تیر در ورزشگاه شهید کاظمی برگزار می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/134741" target="_blank">📅 22:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134740">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">💬
ادعای عجیب دبیرکل فدراسیون فوتبال؛ ممبینی:
🎙
چادرملو برنده شد اما ممکن است گل‌گهر به آسیا برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/134740" target="_blank">📅 22:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134739">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
فرهیختگان: در اردوی نیم فصل پرسپولیس  اوسمار ویرا جلسات شبانه ای در قطر  در یکی از هتل های دوحه  با هوادار متمول با هماهنگی سروش رفیعی انجام داده که این  اتفاق باعث بی اعتمادی مسئولان باشگاه شده ؛ که خبر این جلسات به گوش بازیکنان هم رسیده و حواشی در رختکن…</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/134739" target="_blank">📅 22:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134738">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gn-SZ2BrKv2jlSUf27LrYeFmtmCDHehfEKZLUihlCv7jYJz2fkMlcKLR09nUG7miKRuBjd8fGHzKmR-nRzGdfnKl0av0Po9FB8TUkXZXIKwiHvJ4zmnAq2yoLLLitntsxqKd6EcYcLAQGls5ID157NjlQSwjFaQ9QWN43tTIsbmSVNlXxKmaoa3m3lGADX1xAseEtNiM2IgJ1xXHKNS6z209LPp70VYXji8qg7rrtzaS9yXbadYME6wg1oA0om8WFAWhFFK7CeUwXgfZLNkB9G8t0SoLOXgSfZlYQC3sAgN9scGW5sRdR1fKenCyhgixpUZYJRnwjqkIlDRK2cNIkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام ترانسفر مارکت؛
مجتبی فخریان به پر‌سپولیس بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/134738" target="_blank">📅 21:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134737">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
🚨
🚨
🚨
فووووووووووووری
🚨
محمد مهدی نبی مدیر تیم ملی، هدایت ممبینی دبیرکل فدراسیون ، مهدی خراطی مدیر اجرایی تیم ملی، سیامک قلیچ خانی مدیر رسانه ای ، محسن معتمدی‌کیا مدیر روابط عمومی و یکی از آنالیزور های کادرفنی به همراه افسران أمنیتی تیم ملی موفق به دریافت ویزای…</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/134737" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134736">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❗️
اوه اوه ...بیست دقیقه تا حذف انگلیس توسط کنگو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/134736" target="_blank">📅 21:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134735">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❗️
انگلیس از کنگو گل خورد
😐
🔴
چه جام جهانی سمی ایه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/134735" target="_blank">📅 21:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134734">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‼️
دانیال مرادی، رئیس دپارتمان داوری: ۱۳ کمک داور و ۱۲ داور موفق نشدند آزمون هارا پاس کنند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/134734" target="_blank">📅 20:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134733">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9ed04d87.mp4?token=I3YufHOxjvRJAzb2Z7lPWgEJ2Frdj01VuVXWDWv1F8xNqNaqVS2-4vhWnoJ4V-BFZrVDRLYx2l0Q-2Hx9WDQpjaC-pHjqb4sQVv0PNDA-CRZHIjo61MBZa08IGHAt1EwiNzAOUsn_X-FuwAXzJDjCMgVj8b4krqMbU-SZsUKr5hiS0e5J6Vjfc5HjZV_VF8VlFEMhXI7sJfQTbwuNXB2pm3hyJeBedOFXOrQopySPKi6IJ2ILfg40eshrSa1KFeuUTUKymULqnpp8CvXyXf4a9VXUHYlcN4U0x9rNYkqozv43ZRC4bbD4tv6wucuITQtXGzjiwDUpHrL6bTPr8Xpooi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9ed04d87.mp4?token=I3YufHOxjvRJAzb2Z7lPWgEJ2Frdj01VuVXWDWv1F8xNqNaqVS2-4vhWnoJ4V-BFZrVDRLYx2l0Q-2Hx9WDQpjaC-pHjqb4sQVv0PNDA-CRZHIjo61MBZa08IGHAt1EwiNzAOUsn_X-FuwAXzJDjCMgVj8b4krqMbU-SZsUKr5hiS0e5J6Vjfc5HjZV_VF8VlFEMhXI7sJfQTbwuNXB2pm3hyJeBedOFXOrQopySPKi6IJ2ILfg40eshrSa1KFeuUTUKymULqnpp8CvXyXf4a9VXUHYlcN4U0x9rNYkqozv43ZRC4bbD4tv6wucuITQtXGzjiwDUpHrL6bTPr8Xpooi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
ادعای عجیب دبیرکل فدراسیون فوتبال؛ ممبینی:
🎙
چادرملو برنده شد اما ممکن است گل‌گهر به آسیا برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/134733" target="_blank">📅 20:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134732">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/80f7520ba9.mp4?token=WS0O7lTgflcmEr3Zp6SYFZmsUvcg8cUhqbdzE8nkOBHloRxz3nm0mUIKSLT4TQMn62mny5X_-N0VrWNpVfvqamzb_jjHu9PitnNS3PPOdp89mkrMF7kZvOI7aBlxlAJOycjPWU9b_5yxQap5_0_L084Ussl2KlGfFJoc5AVwevgVQcybWcOxRn3OuQLBZPfHCQQsRXkkqzB8Zf3v_8TGdf4muzSA64hx7G3Z1iHk7TdxMPDRJcz15DIZlrF3mG0zWFeUuSFAWoHKE5Bnyucgz6wqpJXv2ijLnWnhN5MOaDokWBVrLWDcyHqtLWcYvgWEo0ZDuApr4imrSjKT-hcs7w" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/80f7520ba9.mp4?token=WS0O7lTgflcmEr3Zp6SYFZmsUvcg8cUhqbdzE8nkOBHloRxz3nm0mUIKSLT4TQMn62mny5X_-N0VrWNpVfvqamzb_jjHu9PitnNS3PPOdp89mkrMF7kZvOI7aBlxlAJOycjPWU9b_5yxQap5_0_L084Ussl2KlGfFJoc5AVwevgVQcybWcOxRn3OuQLBZPfHCQQsRXkkqzB8Zf3v_8TGdf4muzSA64hx7G3Z1iHk7TdxMPDRJcz15DIZlrF3mG0zWFeUuSFAWoHKE5Bnyucgz6wqpJXv2ijLnWnhN5MOaDokWBVrLWDcyHqtLWcYvgWEo0ZDuApr4imrSjKT-hcs7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شاهکاری دیگر از فیروز کریمی: قلعه نویی 5 سانت رو تحمل کرد 10 سانت رو تحمل کرد ولی دیگه 30 سانت رو کجاش بذاره؟؟
😐
😆
😆
😆
😆
😆
😆
😆
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/134732" target="_blank">📅 20:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134731">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» حدادی شخصا میخاد با امید عالیشا،میلاد سراک،رضا شکاری،مرتضی پورعلی گنجی،دنیل گرا و تیوی بیفوما فسخ کنه.
❌
حالا باید ببینیم بانک شهر برای فسخ و آوردن بازیکن جایگزین بودجه میده یا نه
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/134731" target="_blank">📅 20:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134730">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🔥
💵
اگه دوست دارین از بازی های
جام جهانی
یه سود تپل و درست حسابی به جیب بزنید حتما داخل چنل بت زیر عضوشید خفنه واقعا
☑️
🖥
JOIN
JOIN
JOIN
JOIN
JOIN
JOIN</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/134730" target="_blank">📅 20:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134729">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aN0ouVP89JrvkHumBDpZwJeMI73gwud422BO03ofxViSkfXtbXj-JN-JAGjYtmJjb0Zq8SA7BzVU_MoCFy8ACo0Q6kZUnYvq3dwlltQUINvZeO_mImOfR3_jr7182xMEoAKhwNi-ZhMR7wSLyh3lEPc3hwgH7mk7vr0dLyei0CoGauMzFl53gHgsvcvjdspqqudopF9YpuInU2fso7Tre-qHJK_xlK7N51CzJcCuwzwnKLrpX65E2szVgiuKsonF2mFz3veh6Nprii3ymhfetPOftG6zxDteG4UKbqBDnesXHnOInWzNfyHOIClPo_0kiPos3cdnVKnxO_2QyLSczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هردو تیم گل میزنند_بله
Odd: 1.80
🛫
200میلیون
بستیم روی همین بازی اگه توم میخوای کلی از این آپشن های خفن ببندی (بدون ریسک) حتما عضو کانال VIPزیر شو
🛡
https://t.me/+6L9plEThEMk5YTJk
آمار روزانه 90 درصد برد
🔥
✅
با آنالیز حرفه‌ای و تخصصی که روی ، فرم ها انجام میدیم میتونید به سود میلیونی برسید
💵
💯
🆔
@ARON_TIP
@ARON_TIP
🆔
@ARON_TIP
@ARON_TIP</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/134729" target="_blank">📅 20:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134728">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❗️
میساکی:
✅
جام جهانی رو میدادن به خودمون، بخدا بهتر از آمریکا برگزارش میکردیم.آمریکا نتونست میزبان خوبی باشه.
😆
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/134728" target="_blank">📅 19:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134727">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
✅
🎙
امیر قلعه‌نویی:
🔴
از جام جهانی حذف شدیم ولی خدا بهمون عزت داد!
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/134727" target="_blank">📅 19:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134726">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
دلتون براش تنگ میشه؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/134726" target="_blank">📅 19:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134725">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
تشویق وایکینگی هوادارای تیم ملی تو فرودگاه
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/134725" target="_blank">📅 19:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134724">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
خطر بروز جنگ از جمله مسائلی بود که تردیدهایی را در جذب اسکوچیچ ایجاد کرده بود‌.برخی مدیران این نگرانی را داشته اند که همچون اتفاقات دی ماه که دراگان ایران را ترک کرد او در صورت بروز جنگ قرارداد را فسخ کند اما ظاهرا دغدغه ها و موانع برطرف شده بویژه ابنکه…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/134724" target="_blank">📅 19:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134723">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
پرسپولیس قرارداد را برای اسکوچیچ ارسال کرد
🔴
با رسمی شدن جدایی اوسمار ویرا، باشگاه پرسپولیس امروز قرارداد خود را برای دراگان اسکوچیچ ارسال کرد تا این مربی کروات در صورت امضا به طور رسمی به عنوان سرمربی جدید سرخپوشان معرفی شود.
🔴
قرارداد باشگاه پرسپولیس با…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/134723" target="_blank">📅 18:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134722">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
🏟
پرسپولیس از ۱۵ تیر، بعد از آماده شدن چمن شهید کاظمی، دوباره تمریناتش رو همون‌جا برگزار می‌کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/134722" target="_blank">📅 18:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134721">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
قرارداد دوساله برای اسکوچیچ ارسال شد تا امضا کنه! #ورزش3
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/134721" target="_blank">📅 18:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134720">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗️
قلعه نویی: استعفا نمیدم و آماده میشیم برای جام‌ملت‌ها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/134720" target="_blank">📅 18:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134719">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4FK-gCQkt-nvfZDCkAObumuYl7Yygqm5RBPQWDeDFROYcQM388AwI3sj0mGrOJbINrCVg7Td-PS0Z-od1WDJwTPzommbCtdZ0w9zFTZdKYniakcyS-QNodqUwUTEJwEEj-8S_l4imwd5_Rka9bcsE-uVAxrm6PfCmVQAKal5ka3DEP-f5KxUxBaRcyUYeg9IQhtNHDnPPFjXDt5S_hJyH0yQ5c4bBLdzhnPcnBbYIej79pzoUUpPQFG9qwCb66SD8cecZnI2DZSL475zG64HE96Fu0PRqTipU6SU3ePvYbRFmQgeZqtHAxLctO3F_7Z1i4fUWcU8xas2bMf2Lh4qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
شهاب زاهدی، مهاجم سابق آویسپا فوکوکا به تیم جوهور دارلتعظیم مالزی پیوست
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/134719" target="_blank">📅 17:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134718">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
تشویق وایکینگی هوادارای تیم ملی تو فرودگاه
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/134718" target="_blank">📅 17:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134717">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd1a0c4bd.mp4?token=nJVnrUba75X09O9JTjjZ2c2cc_G72mJViF2uh8l780aDWXetSo2lQZfEjQ2m3SHT80vDCFT9sUuAM5ny5n7mQEIM5Iqsru4XOCdZe-YQ0tywVkHFhydFjqVDMEpEIEAjeitVcoJgRg2miZphhBqLg_pPZx-oQaT2y1o2iQ5VDq0M8w041RC946mDC4mNKcLOxCUJNwGurelwSq4T0VViprvXivISUa_qeGWEtX0OMCNatcVeGoPbrT1xr2L4KcsAbhSSg9Hnx5bFpncwKvS6501XkZ4EYhmErm64A-BYIFPPj4eGRGBI1y8oVDa0OHcsxvR9byLmiFXDWGB9X3bkmr3giQl6bZdAwDiaN5aJd0f6yJT0H7Cgi-8URhM2B0JdNActtzAJqzHNd32vOkFDN04w77WRTolT4bqL0bfut2WgG7mUeZRxb_SBcUjTtDoq9LOx29rCMndOJ99alygRJTbC5bkb8GNgGJ-RiBt1yPFX_ar6m1iJy5GqKd8U1k9vAUTQrJ1q72YRAX4OFRu4N_FDoQtlWT72WtknZXnG3S_QRwSVEL4oGKbnUorakG6lx-V7S8X95bh-jHFN3bOODJ48-fZc1oBIQ6iZ2YtIO9k4FsV8pisbfZ1xlsE9CwO5LeixtYxQUtb7Bl9uQK1QQQ8hgwONh_cllOgV4FPv3vE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd1a0c4bd.mp4?token=nJVnrUba75X09O9JTjjZ2c2cc_G72mJViF2uh8l780aDWXetSo2lQZfEjQ2m3SHT80vDCFT9sUuAM5ny5n7mQEIM5Iqsru4XOCdZe-YQ0tywVkHFhydFjqVDMEpEIEAjeitVcoJgRg2miZphhBqLg_pPZx-oQaT2y1o2iQ5VDq0M8w041RC946mDC4mNKcLOxCUJNwGurelwSq4T0VViprvXivISUa_qeGWEtX0OMCNatcVeGoPbrT1xr2L4KcsAbhSSg9Hnx5bFpncwKvS6501XkZ4EYhmErm64A-BYIFPPj4eGRGBI1y8oVDa0OHcsxvR9byLmiFXDWGB9X3bkmr3giQl6bZdAwDiaN5aJd0f6yJT0H7Cgi-8URhM2B0JdNActtzAJqzHNd32vOkFDN04w77WRTolT4bqL0bfut2WgG7mUeZRxb_SBcUjTtDoq9LOx29rCMndOJ99alygRJTbC5bkb8GNgGJ-RiBt1yPFX_ar6m1iJy5GqKd8U1k9vAUTQrJ1q72YRAX4OFRu4N_FDoQtlWT72WtknZXnG3S_QRwSVEL4oGKbnUorakG6lx-V7S8X95bh-jHFN3bOODJ48-fZc1oBIQ6iZ2YtIO9k4FsV8pisbfZ1xlsE9CwO5LeixtYxQUtb7Bl9uQK1QQQ8hgwONh_cllOgV4FPv3vE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تشویق وایکینگی هوادارای تیم ملی تو فرودگاه
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/134717" target="_blank">📅 17:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134716">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✔️
#تایید_خبراختصاصی
⚽️
🤩
رسمی؛اوسمار ویرا از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/134716" target="_blank">📅 17:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134714">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5xe984EWyU5Psg9lF2ZtmRVjVu7fXcjraZSbu-6K6UOm90K-VkzIF1toYXyqTa6oohyaaYViEeDFAPkhtETTXz5SZtkm6K2Q2fqS7j-YW9EZN8IBl059xop4Kw87Ox9cM4YA8srKrKjz7p_0wDSKEmupVTiWAKOlBbKNULMB2s6htuLq4IHVt1-Wc_QYgSh4plGzCVni8at17Tl9H5a_IIj_WuXjEAP2xb5NnqKnf-DVIQdgu0HcPVXezrjLB6a_TRk5zJAGUaRh4jDVEiS82UtBb-oVmIUI4V_CmhGPxnGDrdUpIxVc7JqDg1P9auMgO8R4L6j9tQc7H--CAUksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» حدادی شخصا میخاد با امید عالیشا،میلاد سراک،رضا شکاری،مرتضی پورعلی گنجی،دنیل گرا و تیوی بیفوما فسخ کنه.
❌
حالا باید ببینیم بانک شهر برای فسخ و آوردن بازیکن جایگزین بودجه میده یا نه
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/134714" target="_blank">📅 17:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134711">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
✅
شنیده ها :پرسپولیس تا ساعتی دیگه آفر رسمی رو برای اسکوچیچ ارسال میکنه تا با توافق کامل روی جزئیات امضا بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/134711" target="_blank">📅 16:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134709">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
🔴
مهدی طاهرخانی
🔴
یکی از مسئولان باشگاه بهم اطمینان داده که صد درصد و بدون شک اسکوچیچ سرمربی فصل بعد پرسپولیس خواهد بود
✅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/134709" target="_blank">📅 16:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134707">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pbp9ZASbhf6rIChoviXyZas9pmlsc_FSNzQV7LYqHAexdsyZzlvTZ6IwZUZ6E4jhK_l6pyrGhiwNjuPXUStFrKst8qjtIrXo4YSpLqLt6dP5Z_q8DtadjVJMgVLVGOBwhYisI13bSXB43TM_St1VUvoKNqKF4c_-8Dag54rHJLBXkh5Qan5-IC_cQaEOpAWVTUfDwgHOFky7ULOX0rK6GhFrNSnVJDS-sWPSNFXh4Dlm2-qqEnfX5YAn_mkaQItZYgahOCTvXCZGSwOPD4JquzxnvHFW76FmxNImol-jfsvDCqCRbFmUWaYWgLRKE4sCxMPmmWnqPvv742McQkQCgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دلتون براش تنگ میشه؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/134707" target="_blank">📅 15:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134706">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوررری
🚨
اوسمار ویرا ظهر امروز ایران را ترک خواهد کرد و جدایی این مربی از پرسپولیس رسمی شد…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/134706" target="_blank">📅 15:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134705">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7158fe0fc1.mp4?token=dVU4FoBolwdaRrzDsYcmr85QSLvWU_myVsQFV1Cg8oK92nP34UXn-r3IhOwjaR1v8lwu6B2jG-coiqdWiAHCRmDFYmHc_-4ZmIzLS8sK8JBmIDlDs5Aj_-1CwOOAlSsIPjXECoZZkreDpDCj-bgsrYrzdIDXeS7ELaVs50d8ONUIin0YuvvsT7ayzBLuLWAJGqbCvmPQOQx5vAGiReAsvhMg2o_Z3oeggZ0uhaZnCqDLOOWEcjKzje6YJSrnmGTeIOsXXwZ6WjnBfMcfhG_cCeVl0ekq49iy9nwTmrop1_CmLao7PPceTfYKyJ-zIPi7eGJapDUqCYKL9D51J4uslA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7158fe0fc1.mp4?token=dVU4FoBolwdaRrzDsYcmr85QSLvWU_myVsQFV1Cg8oK92nP34UXn-r3IhOwjaR1v8lwu6B2jG-coiqdWiAHCRmDFYmHc_-4ZmIzLS8sK8JBmIDlDs5Aj_-1CwOOAlSsIPjXECoZZkreDpDCj-bgsrYrzdIDXeS7ELaVs50d8ONUIin0YuvvsT7ayzBLuLWAJGqbCvmPQOQx5vAGiReAsvhMg2o_Z3oeggZ0uhaZnCqDLOOWEcjKzje6YJSrnmGTeIOsXXwZ6WjnBfMcfhG_cCeVl0ekq49iy9nwTmrop1_CmLao7PPceTfYKyJ-zIPi7eGJapDUqCYKL9D51J4uslA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
افشاگری جنجالی کاپیتان نساجی علیه استقلال
🚨
کاپیتان نساجی مدعی شده آرش رضاوند بین دو نیمه بازی استقلال و نساجی گفته «شل بازی کنید چون پرسپولیس عقب است» و استقلال عمداً جدی بازی نکرده و همزمان پرسپولیس کامبک زده قهرمان لیگ شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/134705" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134704">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
✅
✅
تسنیم: علیرضا بیرانوند شهریور ماه سرباز میشه و باید بره فجرسپاسی
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/134704" target="_blank">📅 13:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134703">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🤩
🤩
🤩
باکیچ : کریم باقری هنوز هم می تواند در پرسپولیس بازی کند
💬
من گذشته کریم را ندیده ام اما می توانم قول و تضمین بدهم همین حالا هم او شوت های قوی و قدرتمندی دارد و اگر خودش بخواهد می تواند الان هم برای پرسپولیس بازی کند. او هر روز در تمرین شوت می زند و قدرتش…</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/134703" target="_blank">📅 13:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134702">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
✅
علیرضا بیرانوند ملقب به تنگه در آستانه عقد قرارداد با بشیکتاش ترکیه قرار دارد/ فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/134702" target="_blank">📅 13:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134700">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‼️
محسن مسلمان: سال 96 زن گرفتم و همون سال هم طلاق دادم. دو تا خونه و 114 تا سکه دادم واسه مهریه. الآنم دیگه پول مهریه ندارم که زن بگیرم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/134700" target="_blank">📅 13:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134699">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/134699" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/134699" target="_blank">📅 13:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134698">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tZ-mJBCMqgnap5F8Z-XgxVXd42MY9JLm0gmFjM6EMZBWBn5x9UTjkhlsyGkjy7jSI5ibf61cs2O8kqcA0kpjK341ynmTrTmSUe1GMaG04wcJXzoFP1iRpm9al5WEJuvHNJc8CeOMouWluUrDkpQrtLCJwkF-noTQIUUOvb0XefeASYcDiB_N3Qd5OrH5AVJFmKFV4o2AwUGhMsLxaLVHbpDm30pXzKYKjd1zET0RdE5zp_VwwuLITpYGj6JuxNRxx2qPgcZJbLHHA4RUjMsjjNf4To741D_n8nbWR5fInk_VqRKlSH2x-vAh1LfUhoVvxzU94fzFspqJgA6pEK0CqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی فوووق جذااااب
انگلیس
و
کنگو
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
⚽️
🔥
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/134698" target="_blank">📅 13:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134697">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
🔴
پرسپولیس با طاهری تموم کرده و فقط بخاطر اینکه مشخص نیست قطعی باشه یا قرضی هنوز رونمایی نشده
/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/134697" target="_blank">📅 12:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134696">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
🔴
مهدی رحمتی :از امیر قلعه‌نویی تعجب میکنم، اولین چیزی که او به من گفت، این بود که به هیچ‌کس هیچ قولی نده، اما خود او قول صعود داد.
🔴
🔴
اولین هدف آن ها صعود از گروه بود اما اتفاق نیوفتاد، پس بیایید عذرخواهی کنید، تاج و قلعه نویی باید حداقل از مردم عذرخواهی…</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/134696" target="_blank">📅 12:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134694">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
اوستون اورونوف و ایگور سرگیف اولین خارجی‌های تاریخ پرسپولیس هستند که در حین عضویت در این تیم در جام‌جهانی بازی کردند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/134694" target="_blank">📅 12:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134693">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
🔴
#تکمیلی؛ شماره 10 پرسپولیس در فصل جدید رقابت‌ها به مهدی تیکدری ستاره‌جدید سرخ‌ها رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/134693" target="_blank">📅 12:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134692">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
✅
مهدی رحمتی: این حرف ها چیه که ما نباختیم. خودمون رو که گول نمیتونیم بزنیم. آره نباختیم ولی حذف شدیم اونم تو یکی از ساده ترین گروه های این دوره جام‌جهانی. تاج و قلعه‌نویی باید جوابگو باشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/134692" target="_blank">📅 10:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134691">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
کمالوند سرمربی خیبر شد!  پ.ن و. احتمالا پنگوین (مهدی رحمتی )سرمربی کیسه میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/134691" target="_blank">📅 10:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134690">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❗️
❗️
❗️
فوتبالی : شنیده می‌شود کریم باقری نقش بسیار مهمی در لیست مازاد پرسپولیس دارد و نفرات این لیست با نظر او و البته اسکوچیچ (که به احتمال زیاد سرمربی بعدی پرسپولیس است) مشخص خواهند شد.
❌
❌
قرار است اسکوچیچ بعد از سفر به تهران، جلسه‌ای را با کریم باقری برگزار…</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/134690" target="_blank">📅 10:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134689">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوررری
🚨
اوسمار ویرا ظهر امروز ایران را ترک خواهد کرد و جدایی این مربی از پرسپولیس رسمی شد…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/134689" target="_blank">📅 10:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134688">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
سردار حسن‌زاده، رئیس ستاد وداع و تشییع رهبر شهید:
🔻
روزهای ۱۳، ۱۴ و ۱۵ تیرماه تهران تعطیل است.
🔻
روز ۱۵ تیر کل کشور تعطیل است و در قم ۱۵ تیر و روز ۱۶ تیرماه تعطیل است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/134688" target="_blank">📅 09:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134687">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
🔴
مهدی طاهرخانی
🔴
یکی از مسئولان باشگاه بهم اطمینان داده که صد درصد و بدون شک اسکوچیچ سرمربی فصل بعد پرسپولیس خواهد بود
✅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/134687" target="_blank">📅 09:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134686">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❗️
عملکرد اوسمار ویرا در دوره دوم مربیگری در پرسپولیس:
🔴
۷ برد - ۲ تساوی - ۶ باخت
🔴
۱۷ گل زده - ۱۶ گل خورده
🔴
میانگین ۲.۴ امتیاز در هر بازی
🔴
عدم کسب سهمیه آسیا
🔴
حذف از جام حذفی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/134686" target="_blank">📅 09:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134685">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
✅
عملکرد اوسمار ویرا در دوره اول مربیگری در پرسپولیس:
🔴
۱۳ برد - ۴ تساوی - ۱ باخت
🔴
۳۳ گل زده - ۱۷ گل خورده
🔴
میانگین ۲.۴ امتیاز در هر بازی
🔴
کسب قهرمانی لیگ ۲۳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/134685" target="_blank">📅 08:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134684">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
🤝
🤝
اوسمار ویرا دقایقی قبل رسما قراردادش رو با باشگاه پرسپولیس فسخ کرد و از جمع سرخپوشان پایتخت جدا شد‌. بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/134684" target="_blank">📅 08:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134683">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
ترکیب پرسپولیس در دیدار امروز برابر چادرملو
🛜
سیستم پایه:۴۴۲
❤️
امیر رضا دفیعی
❤️
حسین ابرقویی
❤️
مرتضی پورعلی‌گنجی
❤️
فرزین معامله‌گری
❤️
دنیل گرا
❤️
میلاد سرلک
❤️
مارکو باکیچ
❤️
تیوی بیفوما
❤️
محمد عمری
❤️
یاسین سلمانی
❤️
محمد امین کاظمیان
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/134683" target="_blank">📅 08:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134682">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اخرین فرصت برای عضو شدن بعدش میخوان  کانال رو خصوصی کنن</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/134682" target="_blank">📅 01:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134681">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_cj5I6wgb1RfVu-I_dbGiIPrO6mHHuvl3V0BQAl-OK82zbPRmSel7Oh0sNLQ4RegEmUSX-Be9iUTEbrLLiVe7bWKDlex5PJ2kKB5f4gM5xnBKRQdv7moNE9BQcdRzf1jPyb0nqsVDnqCctJbQdru-hG3EHwUWOeJW_crjetK83sVm8Rzo7Ap8ZvbBsM4hdqbbq74lTkQGj7mql3ed6pvyE8xQIYoBRER5yPatZPgIpRtqeUyF_kIaI4-_cjzHxFHYwHfOVH1GqhPp43tGz2VWc88J0xN0in_WKdjzyKTNnHcmF-ftYnqLRyJric1uqnS-p7_IfU2i7cwJ7WtNL0Ew.jpg" alt="photo" loading="lazy"/></div>
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
?
💡
کافیه یه کانال معتبر پیدا کنی که کارش تحلیل فوتبال باشه و دارای چند سال سابقه کاری باشه کانال پیشبینی تیپستر پرشین همونیه که دنبالشی چکش کن
👇
https://t.me/+iIi9FxzzcYBjNDg8
https://t.me/+iIi9FxzzcYBjNDg8</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/134681" target="_blank">📅 01:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134680">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
🔴
مهدی طاهرخانی
🔴
یکی از مسئولان باشگاه بهم اطمینان داده که صد درصد و بدون شک اسکوچیچ سرمربی فصل بعد پرسپولیس خواهد بود
✅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/134680" target="_blank">📅 00:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134679">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
ایجنت دراگان اسکوچیچ: اگه اتفاق خاصی رخ ندهد اسکوچیچ سرمربی پرسپولیس خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/134679" target="_blank">📅 00:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134678">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
✅
تایید شد
🔴
تیکدری به پرسپولیس پیوست.//خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/134678" target="_blank">📅 00:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134677">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🚨
آخرین جزئیات از توافق پرسپولیس با اسکوچیچ
🚨
🚨
پس از مذاکرات فشرده مدیران باشگاه پرسپولیس با دراگان اسکوچیچ، سرمربی اسبق تیم ملی فوتبال ایران و تراکتور، توافقات نهایی میان طرفین حاصل شده و این مربی کروات در آستانه حضور روی نیمکت سرخ‌پوشان قرار دارد.
🚨
🚨
بر…</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/134677" target="_blank">📅 23:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134676">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❗️
❗️
با توجه به برخورد و واکنش هوادارن پرسپولیس، عملا بانک شهر بی خیال جذب عزیزی شد!
✅
البته با توجه به حضور پیروانی در آمریکا، بعید است، محبوب ترین سرپرست تاریخ باشگاه پرسپولیس به شغل سابقش بازگردد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/134676" target="_blank">📅 23:45 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
