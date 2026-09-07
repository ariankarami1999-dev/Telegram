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
<img src="https://cdn4.telesco.pe/file/Wgb402k0b2AHDzmzPSzD6ni9LB8gB416e6a12LaC6GZaHFpW0C4mNuykAPzWNbjYNwqZCnajcdIRQt9qg3wOZMgnHXkr3SfXz_eqc43GM_ESiN0CWQc2i7sbmxvgzqZlL6HJ5mB0ReymBOK9_Ef_msOVMkgNOBHrC6jHwbTbPhe8DoAl-VXnSTKDqriU0_fnluf73KWpF0WhY89o0ZqmczVfiWqNttmtay-Bn5IqzG3M27FFTdZIFOD1HiaaRHeTvgKFrhICiN3CysW5Mi1fna9AWJSyyJxgFiJkM7stTbRsnlxwOYDeIEgV4FKhXCt6WOx_rnIIkHScEf_pgOCX_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 19:42:49</div>
<hr>

<div class="tg-post" id="msg-139704">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
واقعا چهار روز چهار روز بازی کردن تیم و بچه هارو خسته کرده و واقعا تو ساق بچه ها خستگی واضحه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/SorkhTimes/139704" target="_blank">📅 19:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139703">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
تازه میفهمیم که چرا ارونوف و روی نیمکت می‌ذاشت تارتار ‌..واقعا آماده نیست   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 124 · <a href="https://t.me/SorkhTimes/139703" target="_blank">📅 19:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139702">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
بریم برای بازی شش امتیازی ..امیدوارم مثل بازی های گذشته از دیدن فوتبال پرسپولیس لذت ببریم ...الهی به امید توووووو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 386 · <a href="https://t.me/SorkhTimes/139702" target="_blank">📅 19:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139701">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OP22Iw4BI_HoHCeE0iRuXFzXyD-joTCUUZ_S_fWe8ErTfW08S6A_YxwRRJQCtBiJs8P1DSo2-mwYnQW2kILj1qekheVXouNrJKHfGOTWOG4j0Z_qZMew8PXch-fOJ2-LfxMtLDG6xdE3xQY04SB0x5L57Pnr2oV5t2Yny2819ACvEi2J5rWezK_TIEkpPP6NAdlQPcnwYaSBs_T1AK3QhszYCQsAV9StoUhNaERSuIsJzfmQJrtOZhoUx3ngzboZhYkn4mecsa_wwDATn_VbzIn2NWJQ4g4DMpZx8LFk2TbzurTBSZmWIMXfXNfj5CQ2rC43wWYB5VKqDQRFb1RHMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
نبرد در نیویورک به اوج خود رسیده!
🟡
گرنداسلم یو‌اس اوپن؛ جایی برای جنگِ ستاره‌‌ها
🎾
بزرگان تنیس برای آخرین جام بزرگ سال می‌جنگند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی رقابت‌های یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتونو ثبت کنید:
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
<div class="tg-footer">👁️ 690 · <a href="https://t.me/SorkhTimes/139701" target="_blank">📅 19:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139700">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
شماتیک ترکیب پرسپولیس مقابل ذوب‌آهن
🗣
اورونوف دلها فیکس شد
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/139700" target="_blank">📅 18:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139699">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✔️
هوادار پرسپولیس درباره جنجال امید عالیشاه و خداداد عزیزی
❌
❌
آقای خداداد عزیزی به قول سیدجلال ما پرسپولیسی‌ها هیچ چیزی از یادمان نمی‌رود. خدا نکند که ما پرسپولیسی‌ها با تو رودررو شویم؛ می‌توانی از بیرانوند بپرسی. مثل خودت با تو رفتار می‌کنیم. کل افتخارات…</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/SorkhTimes/139699" target="_blank">📅 18:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139698">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
✔️
صحبت‌های هوادار پرسپولیس درباره اتفاقات بازی تراکتور- گل گهر و حواشی ایجاد شده میان عالیشاه و خداداد عزیزی!
❌
❌
از کمیته انضباطی سخت می‌خواهیم برای یک بار هم که شده رای درست بدهد.‌امروز نشان می‌دهیم که هیچ کسی حق توهین به عالیشاه را ندارد. امید عالیشاه…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/SorkhTimes/139698" target="_blank">📅 18:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139697">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
✔️
هواداران پرسپولیس در پاسخ به فحاشی خداداد عزیزی به امید عالیشاه، کاپیتان سابق خود را تشویق کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/SorkhTimes/139697" target="_blank">📅 18:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139696">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
✔️
ترکیب بازی امروز همینه و تایید شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SorkhTimes/139696" target="_blank">📅 18:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139695">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3392d48f0.mp4?token=VrbEfQSDYchJl_zvboFaqP_vkrxX2Z7empe0hYNVmgWW0UKm6oNkTTbYM9Q2-TPhqOYy6-zQ745jEn4BQU0TVFcDy9GUj2N-ksZnMXWDPGPVZleLnfJceZTlpv_vJC2Ve90GaEIXUcyiKRptpewS4zY0clOWVZQht26BebOZ7NlGxf-k8OosBpKI0u4_i5MhLnxTteeCueEPxzrL71o-6kmiAyCQhhFkKmi4PpSr_kxZzI5Wvqkd1gIXxlQwa8GsgC8LCNF37LTvzPa5OPHoKk0Dr7_Z7_NjR6PPjwwXafSpiMjsJwE1jcG7dPMbQ4wG8tP52AjuGT7kxBw7pwkbZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3392d48f0.mp4?token=VrbEfQSDYchJl_zvboFaqP_vkrxX2Z7empe0hYNVmgWW0UKm6oNkTTbYM9Q2-TPhqOYy6-zQ745jEn4BQU0TVFcDy9GUj2N-ksZnMXWDPGPVZleLnfJceZTlpv_vJC2Ve90GaEIXUcyiKRptpewS4zY0clOWVZQht26BebOZ7NlGxf-k8OosBpKI0u4_i5MhLnxTteeCueEPxzrL71o-6kmiAyCQhhFkKmi4PpSr_kxZzI5Wvqkd1gIXxlQwa8GsgC8LCNF37LTvzPa5OPHoKk0Dr7_Z7_NjR6PPjwwXafSpiMjsJwE1jcG7dPMbQ4wG8tP52AjuGT7kxBw7pwkbZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
هواداران پرسپولیس در پاسخ به فحاشی خداداد عزیزی به امید عالیشاه، کاپیتان سابق خود را تشویق کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SorkhTimes/139695" target="_blank">📅 18:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139694">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
✔️
✔️
نیمکت
✔️
امیر رضا رفیعی
✔️
ایری
✔️
ابرقویی
✔️
جلالی
✔️
باکیچ
✔️
لطیفی فر
✔️
یاسین
✔️
صادقی
✔️
محمودی
✔️
بیفوما
✔️
شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SorkhTimes/139694" target="_blank">📅 18:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139693">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
✔️
شماتیک ترکیب پرسپولیس مقابل ذوب‌آهن
🗣
اورونوف دلها فیکس شد
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SorkhTimes/139693" target="_blank">📅 18:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139692">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPlfmgKsjkXULu3UzAukGSqW3gRy8IJPO48iYapAIkyqHxd_-Wqq9emB4yZOWcm7mGMu6h64fPgEN7xKKBplNSj7fuqY3R-NKAj5Trddcn3yYNv0o0b23YN5kqmZKyDH3PzoheOaK1m3efhjjqD-VHbDhHgXSdoOJzM_0gNNzls4j5gfTeREB3-D6J1ZNGmGbu6Q211zbh5urt-sUyP7n4yKIVhoNxC9MnBpfPULW8hbYNuaQW4ECidNxLEb1w_javHohiufeAsKsep7XPtqx6MUMhWQqaankuaxllIQVU1yBbZtEqyatpW-1hn3jMSvc5O7ZzBFTZQGw49l2M-AxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
❤️
ترکیب پرسپولیس در بازی فردا برابر ذوب آهن
🔴
سیستم پایه:۴۴۲
🔴
پیام نیازمند
🔴
محمد‌مهدی زارع
🔴
حسین کنعانی‌
🔴
مجید عیدی
🔴
مهدی تیکدری‌نژاد
🔴
پویا پورعلی
🔴
محمد خدابنده‌لو
🔴
محمد‌ مهدی محبی
🔴
اوستون اورونوف
🔴
ایگور سرگیف
🔴
علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SorkhTimes/139692" target="_blank">📅 18:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139691">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❤️
❤️
ترکیب پرسپولیس در بازی فردا برابر ذوب آهن
🔴
سیستم پایه:۴۴۲
🔴
پیام نیازمند
🔴
محمد‌مهدی زارع
🔴
حسین کنعانی‌
🔴
مجید عیدی
🔴
مهدی تیکدری‌نژاد
🔴
پویا پورعلی
🔴
محمد خدابنده‌لو
🔴
محمد‌ مهدی محبی
🔴
اوستون اورونوف
🔴
ایگور سرگیف
🔴
علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/139691" target="_blank">📅 17:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139690">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7939cefa83.mp4?token=gW-Fm4APwVKcrbd73RK-12QVtd3vIsbiuykw6-y1j_Um-Qbm4slq3oCygZ0QkX8nLCQSKLCLNhHDofC9AyCyfVZ8wDdyl3GVZzckHp_VCxi07i2hmw-x4vYfUIutSL0rKKHKtkEyUN0cmbUZYuCSH6wxaOAc2HE-ex_NxA_9TOKZEN-ne7P_J_BV-Po0DCcSTAvXiKkLBaOwuorOrBJIKH87ZGc2QshL0GmfetRhbTrAY5RZ8mAjxZNfD4lX8CjNdNGwN_P092SsO5FQMFAK4Vu4ROZ5cYCYygnZXcEjKHjvDR8QYIyr-Ib0nhXNrgALm0NU_-gF0gFf4rVO6OU2vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7939cefa83.mp4?token=gW-Fm4APwVKcrbd73RK-12QVtd3vIsbiuykw6-y1j_Um-Qbm4slq3oCygZ0QkX8nLCQSKLCLNhHDofC9AyCyfVZ8wDdyl3GVZzckHp_VCxi07i2hmw-x4vYfUIutSL0rKKHKtkEyUN0cmbUZYuCSH6wxaOAc2HE-ex_NxA_9TOKZEN-ne7P_J_BV-Po0DCcSTAvXiKkLBaOwuorOrBJIKH87ZGc2QshL0GmfetRhbTrAY5RZ8mAjxZNfD4lX8CjNdNGwN_P092SsO5FQMFAK4Vu4ROZ5cYCYygnZXcEjKHjvDR8QYIyr-Ib0nhXNrgALm0NU_-gF0gFf4rVO6OU2vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📌
هوادار پرسپولیس:
✔️
ورزشگاه آزادی درست بود، بی‌افتخار ترین تیم لیگ (تراکتور) عمرا قهرمان نمی‌شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/139690" target="_blank">📅 17:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139689">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8432a81f4.mp4?token=OmU8RwALwrLOBXMle-I68YrfePIN9ijh77VzNiY9d-KvxzKdN5Pl3FLxt9vKIfxWrrdJIWc51IU_JQ9IlZBWXqoO1jekaMZoYUTQD2H3tujlEENmPBU3iHpupupxiNUAR0G3nakTGsCTIgAYru4gVI0cQrv7yw17phvhw8wzxU_5b5XlM0zooRi1N-vg5U16ruajzFma6-ETAUaf1fJjDNeQOA34yGuTc65mknfJsLqjYz4R0VBgZ-s7e228VOkK7V_CFaB5x30GW3bvKsKQleF39n-UIvhZsflwZkg-5DIGzohI2Y_X_hfGofRFC1fnSnuNzaItPMBun3tEB_SfAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8432a81f4.mp4?token=OmU8RwALwrLOBXMle-I68YrfePIN9ijh77VzNiY9d-KvxzKdN5Pl3FLxt9vKIfxWrrdJIWc51IU_JQ9IlZBWXqoO1jekaMZoYUTQD2H3tujlEENmPBU3iHpupupxiNUAR0G3nakTGsCTIgAYru4gVI0cQrv7yw17phvhw8wzxU_5b5XlM0zooRi1N-vg5U16ruajzFma6-ETAUaf1fJjDNeQOA34yGuTc65mknfJsLqjYz4R0VBgZ-s7e228VOkK7V_CFaB5x30GW3bvKsKQleF39n-UIvhZsflwZkg-5DIGzohI2Y_X_hfGofRFC1fnSnuNzaItPMBun3tEB_SfAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
بانوان پرسپولیسی و تشویق امید عالیشاه در شهرقدس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/139689" target="_blank">📅 17:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139688">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XECHEZIwEKBR6EsFa83DXfr-cFWKOhL-IzgkkZ8G52h637ty4YxlbMFuNANJFh_uew_xqxGDdp3GrtQgHh1gGVIuofPy3x4egxJ4P0D-wZUrkJcQurz_B6EtpDJ7McUzy9nmhm2CjszrhnJxchCXEZsoFO52KcN1MmqjEtivjIV6DKiNf0v__CyyLEf3DdOPnjQNnpgD27yf9JrrJsEnii12auGIMUERHoCdreB8sgLn2lNHyx93cK-4zpULbk83EIQk1t5SZcupAvYBFkWhXsiYUeaN1fgjKBn22CP2Jfw4bFrDvkB6tLDzEhdY5-kEHc0cjydpmMQnPoHlrCmx4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
عالیشاه وکیل گرفت
❌
❌
شکایت عالیشاه از خداداد عزیزی به زودی در مراجع قضایی ثبت خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/139688" target="_blank">📅 17:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139687">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lY8ImTqs5MatLT128UOzSOdhr0yh0oBMD9LJUWytBq3hdKBCYj7j5r9Dx2UqNOwQXVPQlKcS1DH6e5LpTqJSd10eQd_RRfUfvp6EE95Lym3jWuun93GuhP9h0iW1GXHhS6J1OOkuV7nI9u80KIj-X-xZUONbMKP5eD8-RqlzP0BR6K5dEK0XwPYj52Y6FQGbo3kPKOZ2qvAkqRwisVPfGjkakEpoG_nxqeYuwalXHm_R18xUKyS7ojiysAhB_EbgKEwuK1IrWltZUCzajzR5o3mjWmq_8YOHOZpkMO8U7_TckVvZVf4Ny1S1qyy19AfzqlVT-7wt9HG04QaOIdCEkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
هوادارا دم در ورزشگاه شهرقدس
😂
🗣
ورود بدون کارت ملی ممنوع!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/139687" target="_blank">📅 17:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139686">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
گفته میشه که ویسی از که از خداداد عزیزی پخش شده فقط بخشی از فحاشیش به امید عالیشاه بازیکن گل‌گهر بوده و بخش زیادی از فحش ها و صحبت ها پخش نشده و قرار است به دادگاه ارائه شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/139686" target="_blank">📅 17:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139685">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
لیست تیم ملی امید اعلام شد.
🔻
اردو برای اعزام به بازی های آسیایی 2026 ناگویا از صبح فردا دوشنبه 16 شهریورماه در هتل المپیک برگزار می شود.
✔️
✔️
اسامی دعوت شدگان به شرح زیر است:
✖️
✖️
محمد خلیفه؛ادیب زارعی؛آرمین عباسی؛محمد امین حزباوی؛مسعود محبی؛دانیال ایری؛یاسین…</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/139685" target="_blank">📅 16:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139684">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
پرسپولیس با مدارک جدید دوباره پرونده آسانی رو پیگیری کرده و معتقده حضور این بازیکن در استقلال غیرقانونیه. سرخ‌ها میگن مدارک جدیدشون کامل‌تر از شکایت‌های قبلیه و امیدوارن این بار نتیجه پرونده تغییر کنه.
🚨
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/139684" target="_blank">📅 16:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139683">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
🔴
پرسپولیس موفق شد امتیاز تیم دسته اولی فولاد نوین رو بخره و تبدیل به پرسپولیس ب خواهد کرد و سید جلال حسینی هدایت این تیمدرا برعهده خواهد گرفت/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/139683" target="_blank">📅 16:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139682">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJwt3uKMve-EjiLKuiogaQE9pe_PaNaAdwyEhGvM1L05gRoSmdpIE5yHmbCYrhhU4GBPDcjupNiduJm4QhSpPNG6141-OHucvDpYHpdfa5H-Y4L-aEi_FwQZUl-wfa4mpqdqf0q75mZt0SVqdy9SZBqoZVURp0m8J_Dgf0iBklIwX7V_Ed6vB2AmSlFXr8kZipVe2K6UpJ2Ghj4dBUcnA5V22XtyUOe08OiJGYIs3UmBuMpGoFvx77zbfRhTDistH9YWXCqu9Ber9JUP1X4vk9cZVVel3uLeXCnwCZMWUqXVRMxwOkmV7SZS9U5oRjIKXAcFj5ONFzMMBDfEb8nN_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پرسپولیس مقابل یک حریف سرسخت!
⚽️
ذوب‌آهن آماده برای غافلگیری
سه امتیاز، پاداش یک شب بزرگ
[
پرسپولیس
🔴
🆚
🟢
ذوب‌آهن
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/139682" target="_blank">📅 15:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139681">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❤️
🎉
تولدت مبارک پسر متعصب پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/139681" target="_blank">📅 15:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139680">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⭕️
⭕️
فوووووووری
🚨
امید عالیشاه با حضور در دادسرا از خداداد عزیزی شکایت کرد
🔔
80 ضربه شلاق در انتظار افغانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/139680" target="_blank">📅 13:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139679">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fln1z6JxDW1HkpiQKgtQTkVu-20s71er6wM4tt9RaJM5eMJolv-qr6gNBYP-gZXsm9PHKa_2qzbp49_U9UojgeNfOkLsmtbKuzFhwzSNxVioe78Y3SR3b_ezjV2KHvLlheNZSzbJ-hF9lVNhClAfjt5yMUXa3RT8TnwZYX9Z4TqtZMSVI8qEdi31mj8S9wV7rPamini5inFEwXfXrkDFt2aaU93gwJ9WPd-8m0YYz8BHg5QzNdf-QBNhzavBwiFQuaLaRd51slW9DwHCZmEfrch2wwRQakOmyTHPuROdaIiUMx5Rr6VGO-m7tYgE3maA5Zhs5Dt2h1zfJpS00eEcUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عضو پنجم هیئت مدیره پرسپولیس مشخص شد.
✔️
به نظر می‌رسد روند انتخاب عضو پنجم هیئت مدیره باشگاه پرسپولیس به مراحل پایانی رسیده و حسین صابری خورگو به عنوان عضو جدید این هیئت معرفی خواهد شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/139679" target="_blank">📅 13:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139678">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⭕️
⭕️
بهاروند: طبق مصوبه هیئت رئیسه فدراسیون فوتبال لیگ نیمه کاره قهرمان ندارد.
🚨
🚨
پرونده جام حذفی فصل قبل بسته شده و درباره برگزار شدن یا نشدن جام حذفی این فصل هم هنوز تصمیم گیری نشده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139678" target="_blank">📅 12:24 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139677">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
درپی‌اتفاقات‌دیشب؛ به احتمال زیاد خداداد عزیزی سرپرست تراکتور دو الی چهار ماه از همراهی تیم تراکتور محروم میشه و امید عالیشاه یک الی دو مسابقه گل‌گهر رو به دلیل محرومیت از دست میده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139677" target="_blank">📅 10:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139676">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
❌
#فوری؛ بعداز حرفای‌ دیشب تاج برای اهدای جام قهرمانی فصل گذشته به باشگاه استقلال؛ مدیران دو باشگاه‌ سپاهان و تراکتور به فدراسیون اعلام کرده اند یک‌ تورنمنت سه‌جانبه برای تعیین قهرمان برگزار کنند. به‌ اینصورت‌که تراکتور - سپاهان به مصاف هم برند و برنده اون‌…</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139676" target="_blank">📅 10:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139675">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
طاهرخانی ادعا می‌کنه پنجره نقل انتقالاتی کیسه تا آخر تابستون ۱۴۰۶ بسته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139675" target="_blank">📅 08:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139674">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❤️
صبح روزی که بازی داریم و شش امتیازیه بخیر
❤️
❤️
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139674" target="_blank">📅 08:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139673">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
می‌خوای پیش‌بینی کنی، ولی نمی‌دونی چطور حسابت رو شارژ کنی؟
وینکوبت کار رو برات ساده کرده!
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🎁
بونوس ویژه اولین شارژ:
فقط با یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و به موجودی اصلی حسابت اضافه کنی.
🟣
آدرس سایت وینکوبت:
wincobet.com
🔗
همین حالا وارد مینی‌اپ وینکوبت شو و اولین شارژت رو انجام بده:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/139673" target="_blank">📅 01:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139672">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/139672" target="_blank">📅 00:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139671">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❤️
❤️
ترکیب پرسپولیس در بازی فردا برابر ذوب آهن
🔴
سیستم پایه:۴۴۲
🔴
پیام نیازمند
🔴
محمد‌مهدی زارع
🔴
حسین کنعانی‌
🔴
مجید عیدی
🔴
مهدی تیکدری‌نژاد
🔴
پویا پورعلی
🔴
محمد خدابنده‌لو
🔴
محمد‌ مهدی محبی
🔴
اوستون اورونوف
🔴
ایگور سرگیف
🔴
علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/139671" target="_blank">📅 00:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139670">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❤️
❤️
ترکیب پرسپولیس در بازی فردا برابر ذوب آهن
🔴
سیستم پایه:۴۴۲
🔴
پیام نیازمند
🔴
محمد‌مهدی زارع
🔴
حسین کنعانی‌
🔴
مجید عیدی
🔴
مهدی تیکدری‌نژاد
🔴
پویا پورعلی
🔴
محمد خدابنده‌لو
🔴
محمد‌ مهدی محبی
🔴
اوستون اورونوف
🔴
ایگور سرگیف
🔴
علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/139670" target="_blank">📅 00:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139669">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❤️
❤️
ترکیب پرسپولیس در بازی فردا برابر ذوب آهن
🔴
سیستم پایه:۴۴۲
🔴
پیام نیازمند
🔴
محمد‌مهدی زارع
🔴
حسین کنعانی‌
🔴
مجید عیدی
🔴
مهدی تیکدری‌نژاد
🔴
پویا پورعلی
🔴
محمد خدابنده‌لو
🔴
محمد‌ مهدی محبی
🔴
اوستون اورونوف
🔴
ایگور سرگیف
🔴
علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/139669" target="_blank">📅 00:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139668">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd7cdc1c0.mp4?token=S_S643tcOTAIGskWbDM52Dz0Kwc4zCg-I-giRPR7zuguJzaPbhVNNd3AF1e2yAevnqwKCU0qoceqAMXR6pV3d2Wss3AQEgI4tpOR438hQd0xBWaOg_LX4BbQKpW-SZp64ZugfNtirJgTDprTrmZw0RMi60o-hClhJJxIcckQtlz2psXYdR1ULYrXPVqZDDumRJhgq1ZvxCSOe3Wsgc0ud4gYj1kmiMUz8cpqz8vRua2S6fE7kF_5KmJW-JYlBZKcYwdNYunG2N-JJAkc97IRRiDK9a1CN_Qn9kqtq7OUxjIBF8kC8KFn0nVLkieINHBCHi2T4VOViWxcO5MOnP2Oag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd7cdc1c0.mp4?token=S_S643tcOTAIGskWbDM52Dz0Kwc4zCg-I-giRPR7zuguJzaPbhVNNd3AF1e2yAevnqwKCU0qoceqAMXR6pV3d2Wss3AQEgI4tpOR438hQd0xBWaOg_LX4BbQKpW-SZp64ZugfNtirJgTDprTrmZw0RMi60o-hClhJJxIcckQtlz2psXYdR1ULYrXPVqZDDumRJhgq1ZvxCSOe3Wsgc0ud4gYj1kmiMUz8cpqz8vRua2S6fE7kF_5KmJW-JYlBZKcYwdNYunG2N-JJAkc97IRRiDK9a1CN_Qn9kqtq7OUxjIBF8kC8KFn0nVLkieINHBCHi2T4VOViWxcO5MOnP2Oag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
چشمی باید اخراج می‌شد
✔️
✔️
حسین عسگری:
خطایی از این واضح‌‌تر و محکم‌‌تر نداریم مصداق خطای شدید و اخراج است
✔️
✔️
تورج حق‌وردی:
با شدت به زانوی حریف ضربه زد مصداق خطای شدید می‌باشد و باید اخراج می‌شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139668" target="_blank">📅 23:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139667">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSlqK-r3ZQ9o-YLLL1lLKkK9FTrwJQgQxBMrxfJF9i8x0u_Ds9VXA3aQxJhuP8M7i5_6vdw8qzfhOJvk_60L0b0jALGsYzgUnX5QD1xSwTcUibcG9ByzDgJZKWkMjbWrc2y4a7s5-HSCbDeVybWGHWoXyEsknNISqTk7IRzXfta10jjqVS0xKzlqMAx_mkRTNlbEs4tTHjzVGBBGJCRTL88vHAYKP27qvIwFm5RHgkJ4jZldBVjfqdtfKOxTsxbLfkItztXl7hOdNXfwFn3C45UYQJ1ZeW0WWN4NPpeUUoIZEm5cmt2fKY5dldnq2Xh_PFZOpcMXNq_7W1UmTaKVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
اگه فردا ببریم با ۱۳ امتیاز میریم دوم جدول
❌
❌
فوق العاده مهمه ۳ امتیاز بازی فردا</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139667" target="_blank">📅 23:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139666">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🗣
🗣
فوتبالی: اورونوف فیکسه تو بازی فردا
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139666" target="_blank">📅 23:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139665">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✔️
✔️
تارتار: باید با خداداد عزیزی برخورد شدیدی بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/139665" target="_blank">📅 23:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139664">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
✔️
۶۰ لیتر بنزین ۱۵۰۰ تومان و ۵۰ لیتر بنزین ۳۰۰۰ تومانی بدون تغییر ماند؛ افزایش قیمت نرخ کارت جایگاه صرف معیشت مردم خواهد شد.
✅
✅
✅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139664" target="_blank">📅 23:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139663">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⭕️
⭕️
فوووووووری
🚨
امید عالیشاه با حضور در دادسرا از خداداد عزیزی شکایت کرد
🔔
80 ضربه شلاق در انتظار افغانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139663" target="_blank">📅 23:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139662">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
لیست تیم ملی امید اعلام شد.
🔻
اردو برای اعزام به بازی های آسیایی 2026 ناگویا از صبح فردا دوشنبه 16 شهریورماه در هتل المپیک برگزار می شود.
✔️
✔️
اسامی دعوت شدگان به شرح زیر است:
✖️
✖️
محمد خلیفه؛ادیب زارعی؛آرمین عباسی؛محمد امین حزباوی؛مسعود محبی؛دانیال ایری؛یاسین…</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/139662" target="_blank">📅 22:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139661">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
✔️
بازی با ذوب آهن آخرین بازی پوریا شهرآبادی و پوریا لطیفی فر و‌ دانیال ایری برای پرسپولیس خواهد بود و بعد از اون راهی اردوی تیم ملی امید خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/139661" target="_blank">📅 22:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139660">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/139660" target="_blank">📅 22:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139659">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/139659" target="_blank">📅 21:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139658">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🗣
محمد عمری و پیام نیازمند به ترتیب کاپیتان سوم و چهارم پرسپولیس شدن/فوتبالی
🤝
🤝
🤝
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/139658" target="_blank">📅 21:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139657">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
سخنگوی دولت: نرخ کارت جایگاه سوخت از بامداد ۱۷ شهریور به ۱۰ هزار تومان افزایش خواهد یافت، در جلسات کارشناسی اعداد متفاوتی گفته می‌شد اما چون رئیس‌جمهور به مردم قول داده بود همان ۱۰ هزار تومان تعیین شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/139657" target="_blank">📅 21:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139656">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✔️
✔️
✔️
منهای ورزش :همراه اول تو جدیدترین شاهکارش، سقف مصرف بسته اینترنت ۷ روزه «نامحدود» شبانه رو از ۱۰۰ گیگ رسونده به ۲۰ گیگ!
✔️
اینترنت نامحدود تو ایران = ۲۰ گیگابایت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/139656" target="_blank">📅 21:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139655">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✔️
✔️
نایب‌رئیس مجلس اعلام کرد: سهمیه ۶۰ لیتری بنزین با نرخ ۱۵۰۰ تومان حفظ می‌شود، سهمیه ۳۰۰۰ تومانی از ۷۰ به ۵۰ لیتر و سهمیه ۵۰۰۰ تومانی از ۳۰ به ۱۵ لیتر کاهش خواهد یافت؛ نرخ چهارم بنزین هنوز نهایی نشده است
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139655" target="_blank">📅 21:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139654">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RR039yjDiCjw4LIne_FaDrdIYWUEYZjqJZKg7m2Cje2dzqVG4ynUEQOGacoslsk85OwmcAY85YV_p2Zx75MU8D8Fw3SNO83-N8TwQm5IrZB46AcySYVY9Ae33HAu-k5gohpaRdR-jtmOVrVirTMh9yEwD-oYzynUZxBXNnFdpXoOT5eCfbh9oNEjf-OectyIn-gFvyPnjnJAbb-HaZ3h2v9aAY7pFjfAq0qz0cytb55ejMSdztWr9biGtO3vZ5im1KSpNmW9ss-slQu-2h1HbULXe8gW5tNt3txqK3BKZo9iXFvlIqtw5b6vlehE43gFpy2mTqIzbkHSovn04I9ydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
تصاویری از تمرین امروز تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139654" target="_blank">📅 21:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139653">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgbCOlbdrn9oQ4rwv2WQ45DGaTpYnNbBmitRuTGvvAcx9eQk-tH3rQQy7eCKw1NInc3fkfaBIKE5g28mV5Hxuzrg2EX46k7vXuTxfVbQDHO85PTKVxDxfZ83THb3s8wdMM28yg0ftasnqi979y4HkEFPEcvB-RWH5sKX5yv2uED40O5h_0amf-dSkvu9wZ_H_yR1vh-55f5KyKNFNx5uLNP9rRjzIxO6oh3IE2pFP0PRr8OTtcFvHMWY46BT-H6xxGGW1-uiywaXhgQqp_YUcWeR3DefGBJndHCFp7GqFkor9tQhlGcB4N8b5pbcNfiL_YmYQbmhhUdaHmbcLvEidw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
جدول لیگ پس از پایان بازی‌های امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139653" target="_blank">📅 21:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139652">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✔️
✔️
بازی کیسه هم مساوی تموم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139652" target="_blank">📅 21:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139651">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🗣
تا دقیقه 70 کیسه و آلمینیوم صفر صفر مساوی هستند ..و بهترین نتیجه برای پرسپولیس همین مساوی هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139651" target="_blank">📅 21:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139650">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🗣
🗣
فوتبالی: اورونوف فیکسه تو بازی فردا
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139650" target="_blank">📅 20:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139649">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
ابوالفضل جلالی در ترکیب فیکس پرسپولیس مقابل ذوب آهن قرار گرفت و تیکدری کار را از روی نیمکت اغاز خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139649" target="_blank">📅 20:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139648">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jvt7Lzs4Fk0o0PxoyBbm2asujBCm16Kc5DNtJY-IU11xXl6JacLl619wE-hGTh9FRC--LnsjPi-4L2CIqq5tamdivxPCPuIA7s4dw4JvQs67EQrVjRlzIXWhpjsXPwAbnXsFXM9cZ230jYZuO2w51AmXrMKxlQGMnZwpIJBU3GtIftJ9wO58hzI7HTGA1jJfPEwTGslRNEFlrLE40uw1ZDFi36WNasF4L3wU7OY30JU_j94Q_mdUc3wU64mXqP2kXqdLF7j-BSEKxjcGTrE8L9AXatpzALll8tiE_nkvi77YTfidXpws8c11FN56KqiW9JpnzFUafkvz8nGCs9mqqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
حلقه اتحاد بازیکنا تو تمرین امروز
🤝
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139648" target="_blank">📅 20:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139647">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
✅
سه بازی مهم هفته بعدی
✔️
شنبه :گل گهر و تراکتور
✔️
یکشنبه : آلمینیوم اراک و کیسه در اراک
✔️
دوشنبه : پرسپولیس و ذوب آهن شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139647" target="_blank">📅 20:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139646">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
✔️
حضور ابوالفضل جلالی در بازی امروز  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139646" target="_blank">📅 20:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139645">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9bgzVZ8obgtouK4d7mMJqHB-K6HMmZ-zwQRq2lq5Rm8u6eSWWzWtnQE245u6Ihkxyz3poNzxqBJD06fXjh8jLQ4qGzC71wryHr9HYbWEVMxKVsM2K4UqIBeLk1-uzHQRP-RqFch0CqSdVNyfCDP648y68728mEShurN5xDH6rnEje-QqDX7e4Xjwxns_xqEB2HXeA14swyL_N8x1uEBzsUrUOYvs0NTnOS-t5whLT9mdEmmC2suL450D0tT9quJy5DRTDLpcqEk2z11zev8L0wb9EOYGu8I4EgOKfji7oZYFnlkc7Y3PG3tCD7kUN4nHVEOM4zgUgJ9WEm9Cr9ufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
کلاسیک ایتالیایی در راه است!
یوونتوس و میلان؛ جایی که یک اشتباه، بهای سنگینی در تورین دارد.
⚪️
Juventus -
🔴
Milan
⏰
Tonight 22:15
🏟
Allianz Stadium
🎁
بونوس ویژه اولین شارژ:
فقط با یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و به موجودی اصلی حسابت اضافه کنی.
⚽️
یووه یا میلان؟ امشب فقط یک تیم می‌تواند سربلند از زمین بیرون بیاد.
🟣
[
برای ورود به سایت کلیک کنید:
]
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139645" target="_blank">📅 20:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139644">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
✔️
✔️
مهدی تارتار: کاش میتونستم ۲۲ بازیکن بزارم تو زمین اما این برام چالش شیرینیه/هم بیفوما و اوستون و هم عمری و محبی رقابت شدیدی با هم دارن/بازی با ذوب‌آهن برامون از دربی مهمتره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139644" target="_blank">📅 17:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139643">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✔️
✔️
مهدی تارتار: اگه همه‌ی باشگاها اجازه بدن ما هم میزاریم بازیکنامون برن تیم ملی امید/منم دوست دارم اونا پیشرفت کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139643" target="_blank">📅 17:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139642">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139642" target="_blank">📅 17:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139641">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
✔️
✔️
مهدی تارتار:
✔️
بازی بسیار مهمی با تیم با تجربه و با کیفیتی داریم. ذوب آهن کادرفنی و شجاعی دارد
🗣
تیم های ویسی فوتبال جسورانه بازی می‌کنند. با توجه به اینکه هفته قبل دو امتیاز از دست دادیم محکوم به بردن هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139641" target="_blank">📅 17:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139640">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✔️
✔️
واکنش عبدالله ویسی به اظهارات رکیک خداداد عزیزی: واقعا خجالت می‌کشم در این مورد صحبت کنم/ تویی که فحش می‌دهی! شما خودت ناموس داری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139640" target="_blank">📅 17:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139639">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
تارتار: ما با پرس سنگینی که انجام میدهیم طبیعی است که نیمه دوم تحلیل برویم تمام شاخص ها نشان میدهد که در این چند هفته پیشرفت کردیم
✅
✅
شده سه روز به سه روز بازی کنیم باید جام حذفی برگزار شود
✔️
✔️
بیفوما و دعوت به تیم ملی؟ او خودش هم خواست که تغییر کند…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139639" target="_blank">📅 16:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139638">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✔️
✔️
✔️
مهدی تارتار:
✔️
بازی بسیار مهمی با تیم با تجربه و با کیفیتی داریم. ذوب آهن کادرفنی و شجاعی دارد
🗣
تیم های ویسی فوتبال جسورانه بازی می‌کنند. با توجه به اینکه هفته قبل دو امتیاز از دست دادیم محکوم به بردن هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139638" target="_blank">📅 16:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139637">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
عبدالله ویسی سرمربی ذوب آهن: اولین نفری که زنگ زد به تارتار و برای بازی‌های خوب پرسپولیس تبریک گفت من بودم/ پرسپولیس واقعا چشم نواز بازی می کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/139637" target="_blank">📅 16:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139636">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✔️
عبدالله ویسی سرمربی ذوب آهن: اولین نفری که زنگ زد به تارتار و برای بازی‌های خوب پرسپولیس تبریک گفت من بودم/ پرسپولیس واقعا چشم نواز بازی می کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139636" target="_blank">📅 16:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139635">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🗣
🗣
🗣
عبدالله ویسی سرمربی ذوب آهن: با یک بازیکن ( امید عالیشاه ) وارد مذاکره شدیم برای یک فصل از ما 130 میلیارد خواست و من جلوی این انتقال رو گرفتم. ما تیم جوان هستیم و نمی‌توانیم چنین هزینه های بکنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139635" target="_blank">📅 16:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139634">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nc5rEpaiYPFLziRwjeFasoASbJd5Tw_haDuMYnX84cMtUpx3f0H0P2stOi8c0DpjxdrShN70qG9J1rIdvfNRzPPIFtAzAVKiKhjcjFsyrv1O4ekNLMWyWeXl3qfLY4C_fdjtvbgOIt-PJxXmNuG76POozsEi0yf6izQSUmakdRi66tROgus6vpOsY-0PBRy8SAzKaqebqDk9AZjLPPGiaEtONKvTTUeP4QwsoDpq2JC7ijWZ8gDlu-iyUcBtFPuzSTmWjjK5XKHnLXMAyqCuRAEYxW68R9W1-xe_5c9i47o-HmrgB44RjnRHXaxpnNQQLlv6LqiMK8gLsI2wcWCjAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
مرتضی کرمانی مقدم:
✔️
امیدوار بودم که کادرفنی از ابتدا از اورونوف استفاده کند ولی این بازیکن در ۱۰ دقیقه آخر وارد زمین شد. من نمی‌دانم چرا باید از دقیقه ۷۵ به بعد تعویض کرد؛ اگر قرار است بازیکن روند بازی را تغییر دهد باید حداقل بیشتر از ۲۰ دقیقه بازی کند تا بتواند کیفیت خود را به نمایش بگذارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139634" target="_blank">📅 15:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139633">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Epr7O4FuRjOzMWfsUlk-umj1zxQiXbQ8OEfDOro8HsY0U_zcvDONrPYSlXF2dZDO63vCbSNpknZDfYoj8Zd1CeNQXSOBekSdB7nSYiKwHLhes2CBVf6mKGu5AQbXmLCkAFtWkdeb7fCkKi7Sw_5JznixNRhuv6r4Xmpblxdi3jphpPOTNCJnsQOBvMpfFY7PXGd7pub_v5XdIki01LPIQhJ9CvAfBYcP7SlJnuDQ20uWL9tqPPsg5ZHqRjig90d4Ppi4Mz65-K3fCy-ZizT2W6JWC8vzOZBOx9f2fU8Rm_pu00jDUgqGs3eIemlj4u1u4GTnCbFyINglHIdFhWgMBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
با اعلام کمیته انضباطی، خداداد عزیزی، سرپرست تیم فوتبال تراکتور به دلیل تخلفات رخ داده و بدرفتاری در قبال مقام رسمی مسابقه، باید ظرف مدت 48 ساعت دفاعیات خود را به این کمیته ارسال کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139633" target="_blank">📅 15:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139632">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
✔️
فووووووووری
🚨
امید عالیشاه قصد داره فردا با حضور در دادسرا از خداداد عزیزی شکایت خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139632" target="_blank">📅 15:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139631">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAXwZWqBF04_bADXnoV_l-J6TIo-BwLMuH9rXxNNa5wybWeaTy6z-D1KrfepU2SgDY9kXk84zK01Er8uuaPJWtJdK5o3xtHV0xe_0aM1IG_VNsZ5LtUE3pYucuc87I6uY2cIFDvrYLY2zxhKDwXkZLpcsJ22UlI6llKdDUZHkBSvgNcTeELv7eY-fGNqqM6SMJ08GEAO68SGouQSIRHFnOHQKcinnI0OIubwl-xm2WZNpqWLT8u8buftcZAXacHOCr-KYVKDRQOZ8oNUReLrs7p8yvywDucyadonuh6zqybu0Q0-tK_NkLhkvnuVza3dS6PBZvhkIXGZJ68Ovpi_3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کاتالان‌ها در مستایا آماده شکار خفاش‌ها، نبردی برای صدرنشینی!
🟡
Valencia -
🔵
Barcelona
⏰
Today 17:45
🏟
Estadio de Mestalla
بارسلونا با تکیه بر مالکیت توپ و قدرت هجومی، به‌دنبال کنترل بازی از همان دقایق ابتدایی است.
والنسیا می‌تواند با دفاع فشرده و ضدحملات، برای خط دفاعی بارسا دردسرساز شود.
با توجه به برتری کیفی بارسا، کفه ترازو به سود آبی‌واناری‌ها سنگین‌تر است.
📌
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و پیش‌بینی خودتو ثبت کن:
👇
🟣
[
برای ورود به سایت کلیک کنید:
]
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139631" target="_blank">📅 14:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139630">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✔️
✔️
طبق اخبار دریافتی عالیشاه هرگز به خداداد فحاشی نکرده و فقط در واکنش به توهین و هتاکی های وی گفته خفه شو بابا و بعد هم به رختکن رفته و این بخش از  فحاشی ها که فایل صوتی ان پخش شده را هم نشنیده./قرمزانلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139630" target="_blank">📅 13:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139629">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✔️
✔️
✔️
تارتار قصد داره در بازی فردا مقابل ذوب آهن از شهرآبادی در ترکیب اصلی استفاده کنه
📝
خبرگزاری مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/139629" target="_blank">📅 13:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139628">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✔️
✔️
بازی با ذوب آهن آخرین بازی پوریا شهرآبادی و پوریا لطیفی فر و‌ دانیال ایری برای پرسپولیس خواهد بود و بعد از اون راهی اردوی تیم ملی امید خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139628" target="_blank">📅 13:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139627">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">◀️
🔴
از دیروز که باشگاه گفت پرونده ، آسانی رو به CAS می‌بریم به هـــول‌‌ُووَلا افتادن‌... دیروز تاجرنیا و امروز این هوشنگ اصرار میکنن که نکنید بی فایده‌ست‌!
⭕
اصلاً ما دلمون میخواد شکایتِ بی‌فایده کنیم چرا آنقدر میترسید فشار میارید مانعِ ما بشید‌؟
✅
اگر فایده…</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/139627" target="_blank">📅 10:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139626">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xcti45pkmpNhY6oOnDhj1ez7rkaYACy3AodoNXHE0Zop_XzMSd1m5dBkiUnRCEHojWib7V-kzMsmaOz1F0SHZoJj_P1YH4BF557-OCYisvCLTVW2gFyQ-vS6BiMVcRN_YXNiCllBGYHpE73mWUJySaoTdeTAEdxuACGGi7Ga1jv8QQFdtB3YlS9FQnXWYt3ZHtR1aMj-_qVlmyCmfPaVCVs6Zjai88CBQ4L4gVM0CjtWzcDBV1qpilb6Av-ywkAElx2vW_kJVymotAOqf2Z4AQ6P7V3claRKlxAdWfDwOHOxu3QzwidCtlwM7x58Gf1-yeysYX38keCrRNw5lT1Q4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🗣
ازاون اتفاقا که فقط تو ایران میفته
✔️
فرشته کریمی کاپیتان و اسطوره تاریخ
فوتسال
ایران با عقد قراردادی به تیم
فوتبال
پرسپولیس پیوست
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/139626" target="_blank">📅 10:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139625">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139625" target="_blank">📅 10:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139624">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd0e507217.mp4?token=quIRh2GBWPujXVB_H7DDxI5TDmqfx5R3b_zcJG06rGmVnf0dChcAz0n1HbXMMvPd4Ge-J64l_rv_ldkuc57LampVcIUHgTpiGgbXvWNBsXZJiki_RVhgOzYHEKbGaDKKtt4ey8KgyRF6Ha7bDtiyVbJUVTHMqo8ayERZJe14Eu8yTsPtfBSIdVW7sm7TYfdEcjmzvVgGHMLnZ3lbpcbGyex6Bb5hiiEh1KE66Er9EJL7K_ezBXyctno2iaOlwPBjEyHQw9XOl93GVFGRWeoopXC2S8nTVlJX5SjC8Iualdg0Mmws_jOTimAWCU77xQ4AQmZBlXhtgWt2ZeuUCuWs1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd0e507217.mp4?token=quIRh2GBWPujXVB_H7DDxI5TDmqfx5R3b_zcJG06rGmVnf0dChcAz0n1HbXMMvPd4Ge-J64l_rv_ldkuc57LampVcIUHgTpiGgbXvWNBsXZJiki_RVhgOzYHEKbGaDKKtt4ey8KgyRF6Ha7bDtiyVbJUVTHMqo8ayERZJe14Eu8yTsPtfBSIdVW7sm7TYfdEcjmzvVgGHMLnZ3lbpcbGyex6Bb5hiiEh1KE66Er9EJL7K_ezBXyctno2iaOlwPBjEyHQw9XOl93GVFGRWeoopXC2S8nTVlJX5SjC8Iualdg0Mmws_jOTimAWCU77xQ4AQmZBlXhtgWt2ZeuUCuWs1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کنایه باشگاه گل‌گهر به بیرانوند: وقت‌کشی، کسب‌وکار من است! چه برای به‌تعویق‌انداختن سربازی، چه برای کُشتن زمان مسابقه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/139624" target="_blank">📅 10:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139623">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139623" target="_blank">📅 10:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139622">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⭕️
⭕️
🚨
🚨
🚨
🚨
خداداد بعد از اشتباهات داوری به نفع تراکتور در زمین جنجال می کند بعد از بازی هم مصاحبه  جنجالی را چاشنی کارش می کند تا حواس ها از داوری پرت شود. یک سناریوی تکراری! اما آقای عزیزی! عالیشاه رکورددار نباختن در دربی در حد شما نیست؟تفاوت شما با تماشاگران…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139622" target="_blank">📅 09:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139621">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139621" target="_blank">📅 09:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139620">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
طبق اخبار دریافتی عالیشاه هرگز به خداداد فحاشی نکرده و فقط در واکنش به توهین و هتاکی های وی گفته خفه شو بابا و بعد هم به رختکن رفته و این بخش از  فحاشی ها که فایل صوتی ان پخش شده را هم نشنیده./قرمزانلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139620" target="_blank">📅 09:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139619">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✔️
✔️
طبق اخبار دریافتی عالیشاه هرگز به خداداد فحاشی نکرده و فقط در واکنش به توهین و هتاکی های وی گفته خفه شو بابا و بعد هم به رختکن رفته و این بخش از  فحاشی ها که فایل صوتی ان پخش شده را هم نشنیده./قرمزانلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139619" target="_blank">📅 09:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139618">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139618" target="_blank">📅 09:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139617">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e65ac9cd.mp4?token=vn3EAjfo373QVKCpfwcKhF9SkchNaYIiA6VXt6iu89QhAPrHfWwoRGKqWkugMX4gxteQnbzTEqLgVEvppD5Y1AyfAlgxpfxHqwtc6yavmFMKvc_5XbwGdE9zgVIAewfTjJDFX6D6xW527JjH4hq2h9ftDMmtaxe2YtdY3amaUMhOGBV2pG88eEdJh0z2rICKl4z9KjzrsI5iIoow6BxqQSYoynCyiNXXAWxomRrA_vimIPSljSd8GzMcCspCIwqKmxA0RwyPPkLxQZvsSLHUS2nagSAzlvIaZ5fSflfMOFWp2RfgxPIAp7uFsUmR5_pnv1Vw9y52mKepC_G51ccTZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e65ac9cd.mp4?token=vn3EAjfo373QVKCpfwcKhF9SkchNaYIiA6VXt6iu89QhAPrHfWwoRGKqWkugMX4gxteQnbzTEqLgVEvppD5Y1AyfAlgxpfxHqwtc6yavmFMKvc_5XbwGdE9zgVIAewfTjJDFX6D6xW527JjH4hq2h9ftDMmtaxe2YtdY3amaUMhOGBV2pG88eEdJh0z2rICKl4z9KjzrsI5iIoow6BxqQSYoynCyiNXXAWxomRrA_vimIPSljSd8GzMcCspCIwqKmxA0RwyPPkLxQZvsSLHUS2nagSAzlvIaZ5fSflfMOFWp2RfgxPIAp7uFsUmR5_pnv1Vw9y52mKepC_G51ccTZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139617" target="_blank">📅 09:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139616">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQL6f0P1OmZ1WoEkLjWs4J8z6hBzhau_8o1U3L9QdYoOuaLZjkc5gFTexK0F6VC4l0wKhjaQ5BwgZ3gCBQvxpNaQMlqjNBfc6g3ammx5X3UU5EfnNeLHJaAqg-kA0ntUBoN5uSz4yo-mzjfD1rDyAbSt_OsJZg_M2awl7ix46KPCCa95Amlqc_hvQiLp9W2H7sG1DUJwC3J6nBRktJMdMkMq8LMAKzqibB092oikCOifzmXk5slBarbO2heYI7isDdPMB0qwDj4UG44U2ZXNABhuJbQvHd-TV6hixIMsAcPecYU-jSkdQ36RRCoSyDtyJvqvDQVvz3Eoc9EYh4xV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139616" target="_blank">📅 09:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139615">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T65HB0hGbYtFkOncr_WZOlfgNI_axWcvsPeW7r3NBwv3N3BwismsBcTjik1IOWAFT5EhjYSqhyhtNfrShdHUBVSTcuxYpt2BSqEQV9YD_ObJw7L7V_100l0pInBGqtmW1lfrsFqz70es76ejVvX1DxCTZgt8CajeVIVrM1aiLFuOnH0N9v2BQahQxBV8_Gn8eEKylhFVYkhHlbERkphHNIgJRcmLZNvqdZYNJyq8KK1428t-UhyVpTsDEAk3TcJSJ7dg0OQ-tKspmigw_7tkugIQ5ynt_-dcBoC3tz7eYqLLqvbPFnE7nMMR7SBhINLYNXeoySHJHUevQfKaYcEXtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
زورف و تابیلو؛ زورف با تجربه و ثبات بیشتر شانس بالاتری دارد.
تین و منشیک هم جدالی نزدیک و جذاب خواهند داشت که سرویس‌ها می‌توانند تعیین‌کننده باشند.
🎾
Zverev -
🎾
Alejandro Tabilo
🎾
Jakub Mensik -
🎾
Learner Tien
🎁
بونوس ویژه اولین شارژ:
فقط با یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و به موجودی اصلی حسابت اضافه کنی.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و اولین شارژ خودتو انجام بده و این دیدار رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/139615" target="_blank">📅 00:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139614">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
بازی با ذوب آهن آخرین بازی پوریا شهرآبادی و پوریا لطیفی فر و‌ دانیال ایری برای پرسپولیس خواهد بود و بعد از اون راهی اردوی تیم ملی امید خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139614" target="_blank">📅 23:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139613">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✔️
✔️
ورزش‌سه:
🚨
احتمالاً رقابت‌های هفته‌ی هفتم بدون ملی پوشان امید برگزار خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139613" target="_blank">📅 23:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139612">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✔️
✔️
ورزش‌سه:
🚨
احتمالاً رقابت‌های هفته‌ی هفتم بدون ملی پوشان امید برگزار خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139612" target="_blank">📅 23:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139611">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e817b6a0.mp4?token=CG7Jz-0BjBEZWgZaogNnGBwSyjtgDoqMrNWJBxo-cha_Q5OWK0iXBPdzMundrYFuWgqC4s1_nW4GqI7RItGEVECPqLYOtNlbUP0XT9f1F7uveYSlkzU23xzXLb_VybTE1NQVXjQEcOqCSEzsDctdPofPdaoI65Wg_f45d_bMUo06R408D1c1_FBR-9VfY0dn8BMAWasRWjiggv9F_FKectndxy239dyGI_rZrrJmGV0MH-0wpQTKP6Xlr4G2wSNVTTAz55JiGKqU3q-vMYuyDRuQSNLLHt-qFS1fYC--nbS5ix-Jpi5txIsuPY1V49wP3j-UaLJHt_mk8wH-_0iXdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e817b6a0.mp4?token=CG7Jz-0BjBEZWgZaogNnGBwSyjtgDoqMrNWJBxo-cha_Q5OWK0iXBPdzMundrYFuWgqC4s1_nW4GqI7RItGEVECPqLYOtNlbUP0XT9f1F7uveYSlkzU23xzXLb_VybTE1NQVXjQEcOqCSEzsDctdPofPdaoI65Wg_f45d_bMUo06R408D1c1_FBR-9VfY0dn8BMAWasRWjiggv9F_FKectndxy239dyGI_rZrrJmGV0MH-0wpQTKP6Xlr4G2wSNVTTAz55JiGKqU3q-vMYuyDRuQSNLLHt-qFS1fYC--nbS5ix-Jpi5txIsuPY1V49wP3j-UaLJHt_mk8wH-_0iXdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
جواد نکونام : نمی‌دونم داوران با تراکتور چه مشکلی دارن و امروز هم یه پنالتی و یه اخراج نگرفتند هر هفته داریم ضرر میکنیم
😅
😅
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/139611" target="_blank">📅 23:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139610">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ha-wH4eGTil9Ki3ff4RsRz7yiETnNw03NFAmn3H64_SMygGjc_tEkMOUhlPFQDC0OeV21SssAx-Ob06XFr3G3RXfv9Y_MHQ6iVxKW00aIgbcXYwmTCc4R61UX2JrL4qpSDU1mOMrTpj3zKEjV6_hS3S_c9S1N_V2ANFCszLoOcYuB_KBfTOQC-DcHIfoXQAEsTRttku_a8htUvzac_zXAKdBVsK97ba96w-OM9k7-5X7Aa3NPBLx_FLzPmHLJ66abbAsYbXngBIWryTHTaRUWbw8Q7QOahUG8DjHLU2Xj2_2ZpL2T8hvgUtz78HZOeuna04zNVp6NxzzHkgUhH1gIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
تصاویری از تمرین امروز سرخ پوشان بعد از یه روز استراحت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/139610" target="_blank">📅 23:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139609">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
تارتار: ۶ تا ۷ بازیکن من تجربه بازی در دربی را نداشتند، خودم انتظار نداشتم اینقدر خوب بازی کنند
🔴
بگومگو با سرگیف؟ همه بچه های تیم مثل فرزندانم هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139609" target="_blank">📅 23:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139608">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
داوران دربست در خدمت تراکتور؛
🗣
بازی با پرسپولیس؛ اخراج نشدن مغانلو در دقایق ۳۸ و ۵۵ با کارت زرد دوم
🗣
بازی با چادرملو؛ اخراج نشدن حسین زاده
🗣
بازی با گل گهر: گلزنی با کمک، کمک داور که اعلام کرنر کرده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139608" target="_blank">📅 22:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139607">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQDuWe6CBAUR1VjWmS6wyXqQC14onosrNmBsyNCJfS1ayWmIhFI3ELLWMJfdKy88u4dc2xiANfcnee_LQM6-U2SO6qNLKeduZynGD_Cr98Ym8EQnMYbznL0V8wgxrieQYmGbBbRKzgcKAXbv4i649W0zmhaK5PyQRtEbHx_O4dBZCuqBOBLGXJNyuMIybgCd45G8eNpcb-wGio8j2qKN1ybFK_X6VpmCn2DdqazkJusp5hdsxmtib58W_1U1lU6w0INxtTARd0xA6hdeNtnMIWOg2qPC9er_sta2MiH8OasPtBhlghaqaRUHkal2svv6YcGXJvi696OCpcXIGJAwAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🟥
حمله جنجالی و تند خداداد عزیزی به امید عالیشاه:  اسمش رو نمیارم تا گنده نشه! در حد صحبت کردن نیست. به من میگه برو بابا. مال این حرف‌ها نیستی که به من اینو بگی. کجاها بازی زدی؟ سابقه دعوت به تیم ملی نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139607" target="_blank">📅 22:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139606">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🟥
حمله جنجالی و تند خداداد عزیزی به امید عالیشاه:  اسمش رو نمیارم تا گنده نشه! در حد صحبت کردن نیست. به من میگه برو بابا. مال این حرف‌ها نیستی که به من اینو بگی. کجاها بازی زدی؟ سابقه دعوت به تیم ملی نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139606" target="_blank">📅 22:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139605">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
✔️
🚨
🚨
🚨
🚨
فووووووووووووری
🚨
محمد عمری به علت مصدومیت از ناحیه زانو دیدار برار ذوب آهن و خیبر خرم‌آباد را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139605" target="_blank">📅 22:15 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
