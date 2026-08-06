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
<img src="https://cdn4.telesco.pe/file/gHBXz3IG75PWrvNIIQpBf-ZiFYxcLPUfMI8Vp0Ijj2YBAdIpouUGXeofzKR_YlSC33i3VaRujkbDxfMHMuEmhQd90cx0iZ_DaALOJiTJjiVaRrIJBdT6y_B7MbU7Svc0lcQr3ZYhgZubkd_FVgfuRYhV4siUjveoMi9Q1c0zSGzp_NmUOudMDdTRWn2Vl_FqktivbbcvqRo7-gcmC71j4tlYpgU9KMrURDj4cr798dLY5HD9xiozGjCDbk1ok8c47YDJ-33kMhIGv1zr0jtKsuyjWDSQYtEWoQC-NkzjEwKNllEanIt7wC1pFfIGV7rBAWxLrzKap7a1EzmbJc8amQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 18:14:03</div>
<hr>

<div class="tg-post" id="msg-137461">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
❌
محمد امین کاظمیان: آقای تارتار به من لطف و تمایل داشت بمانم و باشگاه پرسپولیس هم موافق جدایی من نبود، اما در نهایت تصمیم گرفتم جدا شوم، چون دوست داشتم در تیمی بازی کنم که شانس بیشتری برای حضور در ترکیب ثابت داشته باشم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/137461" target="_blank">📅 17:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137460">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
❌
فرزین معامله گری سرباز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/137460" target="_blank">📅 16:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137459">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
اعتراف تکان‌دهنده رامین رضاییان بزرگ‌ترین اشتباه زندگی‌ام را کردم!
🔴
طبق شنیده‌های کاملاً موثق، رامین در محافل خصوصی صراحتاً اعلام کرده که پیوستنش به استقلال، بزرگ‌ترین اشتباه زندگی فوتبالی‌اش بوده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/137459" target="_blank">📅 16:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137458">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
اعتراف تکان‌دهنده رامین رضاییان بزرگ‌ترین اشتباه زندگی‌ام را کردم!
🔴
طبق شنیده‌های کاملاً موثق، رامین در محافل خصوصی صراحتاً اعلام کرده که پیوستنش به استقلال، بزرگ‌ترین اشتباه زندگی فوتبالی‌اش بوده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/137458" target="_blank">📅 16:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137457">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇷
💙
رامین رضاییان میشه گفت تنها بازیکن جهانه که از نظر فنی فوق‌العادس اما از نظر اخلاقی و رفتاری میشه گفت بدترین بازیکن ممکن و با تمام مربی های کریرش لج افتاده ؛ بنظر شما حق با مربیان بوده یا رامین رضاییان؟
⚪️
رامین رضاییان
👍
⚪️
مربیان
👎
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/137457" target="_blank">📅 16:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137456">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔔
🔔
گفته میشود مبلغ قرارداد تیوی بیفوما در فصل آینده 850 هزار دلار معادل 140 میلیارد تومن است و احتمالا در پرسپولیس خواهد ماند. باشگاه فولاد خوزستان حاضر به پرداخت چنین مبالغی به او نشده و پیشنهاد معاوضه با رزاق پور را رد کرده است
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/137456" target="_blank">📅 16:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137455">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
امید عالیشاه بعد از 13 سال حضور در پرسپولیس به گل گهر سیرجان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/137455" target="_blank">📅 16:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137454">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
از اونجایی که پنجره کیسه بسته میمونه راه پرسپولیس برا جذب بازیکنانی مثل ایری و حسین نژاد هموار تر شده و فقط باید بانک شهر سر کیسه رو شل کنه و یه تیم جوون و درست حسابی ببنده برا امسال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/137454" target="_blank">📅 16:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137453">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Upi1Lp5l2bzbVRJjRsAnL1RrLoMR8Rn4vKzm2hszC3Xfq3cTu3zj4xz7nN7t5opbn3Z9ZlClbxyjYMxyVg9jc16FbhakM8N0FezvrzGQQ-UINVY4yVovLiAA586G1dnC5k-LwW9CUT-MDRzZ7AIOXASGtLThZFVOu3nQhOD7DQKWlRkVJtN4sZIn6ke7r0qI-M8-lb9To527ZU4Tmfyzp8IF1U3rTgqZUY36WBBjUK1hvRu0SFmSgF7sF-B1UmqUgDiFKnBDcWiuMY3SSchcmf3KmQsEbJ4kTQGNgDCf5D006OkGdHNqk3JIS-KgXkzdaPOiF7uXA-cqLRXViST3IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حسین‌نژاد و قربانی
کدومشون پرسپولیسی میشن
تکلیف ایری مشخص شد
همین الان در سرخ توییت بخوانید
❤️</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/137453" target="_blank">📅 16:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137452">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
🔴
👀
ورزش سه: پرسپولیس در آستانه جذب یک هافبک قرار داره که گفته می‌شه یک سوپرایز بزرگ برای هواداراست!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/137452" target="_blank">📅 15:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137451">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
❌
خبر ورزشی : پوریا لطیفی فر خرید جدید پرسپولیس سهمیه لیگ برتری حساب نمی شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/137451" target="_blank">📅 15:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137450">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyHcVpNbKVx2fX7tUCy-Y2sXridF-KDlMLQvbJv2mjzKUF8InxFcsjTDfYrAEhkoE1dHwLkf3oTu-pa8Aj8vDvlamom9KkQEdbgg-o1oZqv-S2r_aslA7T-_UTuqfHx41GCo_-iVtWAm_sVi3JnWEiSg2ygMQZR5Cp65QEzsWBBA_fGmihwd9GKtUKuKHykJZUq_9G6fgzkoLCUmawgpdjhqAZu8pbO2s9GG50wZgMveHYqodFTsaFn_QHWv7goqndjnB-2q4bIuflAdren1jvqAwYo0A0g3orsQy3EnLHXSUYxMs7Vx7JXAeIQaMD0gREeeC8xOz4Rjqwf-3ZFHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️
پیمان حدادی سفیر افتخاری چوگان شد
😀
✔️
دیدار مدیرعامل پرسپولیس و رئیس فدراسیون چوگان؛ تأکید بر همکاری‌های مشترک در توسعه و ترویج ورزش ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/137450" target="_blank">📅 15:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137449">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
آسوشیتدپرس: پیش‌نویس توافق درمورد تنگه هرمز نهایی شده و در انتظار تایید مجتبی خامنه‌ایه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/137449" target="_blank">📅 15:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137448">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owPDtxU_oxZW-RFjEiz-ozKZ_Rif5wp7k12ZZ7qnBgo-RT5mDMz6HJagAXPOmzlod_Zfnq4-gptWLWbiSC-FIntsrMrGp41FNkaBhq8_8SVBHlZDbc0pHlF3XJSfbjTHS7ytWCZgjzSBi3RO8NpCrteoo1e6wtfqkaH9gHCj1LekdDKwPLqqWMgaBB0yw8tg2Jl5_RDbbpaogM4ZEfr-NQ4KDt7Ldd6erVkoobiEz4mct4CNyOCvDgpLGTFhO8UN5Od1JPzi0AAwVvwRTk-YMs5DT3-bbTE1qb2fNib2JvYEXNnnuaF-KyhrjLwkUrs6bcFeiFN2XkyaFuaFtIk5oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
🔴
ایمن حسین مهاجم ۳۰ ساله تیم ملی عراق، در انتقالی آزاد با قراردادی یکساله به پاختاکور ازبکستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/137448" target="_blank">📅 15:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137447">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
باشگاه پرسپولیس هنوز در حال مذاکره برای جذب دانیال ایری است. اگر مبلغ انتقال شفاف و مطابق قوانین باشد، احتمال نهایی شدن این انتقال وجود دارد / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/137447" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137446">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
🚨
آخرین مرحله مذاکرات پرسپولیس با نساجی برای جذب دانیال ایری با در نظر گرفتن تمام جوانب حقوقی در حال انجامه / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/137446" target="_blank">📅 15:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137445">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_xjTddqSnXFgqOj1KLSYbsbEgHdOj6ljm9uBq7f1VEy-2JA_tY69e2Ik0t_pn_gy9YASTtG8q4d16hc7QzoZfLGFKBSlTc1mapeq0kawP_T2Sxa-lq9_UujVikV-laMo84Zl_zAUUbr36exMEUakvJUGJIKcGuAFja8M4j6dmz2ox-vgo1v06RpBZQ7IA3Kv5yzQ79p6RYLi8u9KQaWUMwkeopFoYfef7_vkaoYffBXUntPIEbVgEpTrQlBabumzD_gGZ3vREachpNiaaUFVdOSSzqco5ELvsYQjPWuXUV2xYQrghTPRf9FgVMeZOMcZ5Y37JUf-P1y8usNwDFPbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
نبردهای حساس لیگ اروپا؛ آغاز مسیر صعود در شبی پرهیجان
⚽️
دیدارهای امشب دور سوم مقدماتی لیگ اروپا، تقابل تیم‌های باتجربه با مدعیان جاه‌طلب را رقم می‌زند و نتیجه بازی‌های رفت می‌تواند نقش مهمی در تعیین سرنوشت صعود داشته باشد. رنجرز برابر یاگیلونیا، بنفیکا مقابل هارتس و سالزبورگ برابر پافوس از مهم‌ترین مسابقات شب هستند؛ دیدارهایی که انتظار می‌رود با فوتبال هجومی، فشار بالا و رقابتی نزدیک همراه باشند.
⚽️
بازی‌های امشب رو در
ربات وینکوبت
با ضرایبی شگفت‌انگیز همراه با ۵٪ شارژ بیشتر از طریق کریپتو پیش‌بینی کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/137445" target="_blank">📅 14:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137444">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">📎
📎
📎
یه سوال پیش میاد اگه واقعا حس میکنید هنوز تو دفاع راست مشکل دارین پس عیدی چرا جذب شد؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/137444" target="_blank">📅 13:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137443">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🚨
آخرین مرحله مذاکرات پرسپولیس با نساجی برای جذب دانیال ایری با در نظر گرفتن تمام جوانب حقوقی در حال انجامه / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/137443" target="_blank">📅 13:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137442">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⚡️
⚡️
خوش‌آمدگویی پرسپولیسی‌ها به محبی
🟪
🟪
کنعانی‌: بازیکنان جدید باید بدانند به چه تیمی آمده‌اند. خوشحالم محبی به این تیم بزرگ آمده و امیدوارم لژیونر شود.
🟪
🟪
علیپور: در جریان بودم که محبی چقدر دوست داشت به پرسپولیس بیاید؛ به او تبریک می‌گویم
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/137442" target="_blank">📅 13:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137441">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
✔️
باشگاه نساجی برای امضای تفاهم نامه قرارداد ایری امروز و فردا می‌کنه/ قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/137441" target="_blank">📅 13:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137440">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lx_hFI0XqN9KHQc9nwXyBuE_DGmJxJDP1n75DjnRHGQLo2FDRTXxPhOuSVHgJP7LMQvOZ5K3OTLGrsSsKWCgkvzpHvp4OE9RH08Ud26uXGQj3V4Ls5miHEegIg2jxUuxiWZKHnwSF9tWxDYMQGy02obs0TDRdHpxJ02LEf62NO7iQsJ9s-YOJ24ueo8r0oL4sDNns0AP9cN8PiRiOoCfgEssd5fUXpnUv0vGXW0tDXDYjah0fn5cCAJ5zb9Ya2Zai27uIY6JDZObTfXmCHnNRhOV-5a7rkDYJ4b7sDLUkEb_j233ft6Oo02oltv5PupYchgX1mXD_s4rCwBCOwejmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پرسپولیس در مذاکره با دنیل گرا به این بازیکن پیشنهاد داده که با نصف قرارداد فصل آینده اش بیاید فسخ کند که این بازیکن این پیشنهاد را رد کرده است و خواهان تمام قرارداد فصل آینده اش شده است..
✍️
خبرگزاری مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/137440" target="_blank">📅 12:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137439">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
❌
تارتار گفته جذب دفاع چپ خیلی مهمه و درصورت مصدومیت جلالی تیم دچار مشکل میشه/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/137439" target="_blank">📅 12:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137438">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">💠
💠
💠
پرسپولیس با وجود ۸ خرید، هنوز در خط دفاع، به‌خصوص دفاع وسط و دفاع چپ، کمبود بازیکن دارد. اگر این ضعف‌ها برطرف نشود، ممکن است از همان هفته اول لیگ برای تیم دردسرساز شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/137438" target="_blank">📅 11:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137437">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🫥
🫥
🫥
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/137437" target="_blank">📅 11:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137436">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWpuBtuBb4Y_UagAtDpqz2p3enF5Omi_1UndnVXggJtblyCa1sM_zJ49KTfLE23PUK5JnMtJjyt32Xr-mUsjxbQPmShxKnCyuubihjtYlIq3ZS_LfislePIS9tzEQae4zfiYidn2E-1aUMIVw6IYieTPgY6D78FLEQM-_4We43W2TxZAmh5FCurjJfLOL4zsaHYl4VDPl-m0IL1GE-j6hk1Je5Heh0atcYMof1zH8yPjaG-tj5i2zkIMu5VQzXmQdibWaxMPe3w6fyeYeYDjn-o5uXv-PxYyCZWsHoSgaKCu6gkdUdG-nCzwrF5ZpZNvWd2a2NMbX7bRjeirTaEmfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
💙
رامین رضاییان میشه گفت تنها بازیکن جهانه که از نظر فنی فوق‌العادس اما از نظر اخلاقی و رفتاری میشه گفت بدترین بازیکن ممکن و با تمام مربی های کریرش لج افتاده ؛ بنظر شما حق با مربیان بوده یا رامین رضاییان؟
⚪️
رامین رضاییان
👍
⚪️
مربیان
👎
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/137436" target="_blank">📅 11:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137435">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔹
🔹
کشوری‌فرد: مسابقات لیگ برتر با حضور تماشاگران برگزار می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/137435" target="_blank">📅 11:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137434">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
ایری فقط یکقدم تا پرسپولیسی شدن
🤝
🤝
🤝
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/137434" target="_blank">📅 11:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137433">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
❌
؛ به درخواست مهدی‌تارتار؛ مدیریت باشگاه پرسپولیس با 3 مربی‌ایتالیایی،اسپانیایی و ترکیه ای در حال انجام مذاکرات نهایی است تا یکی رو به عنوان دستیار اول تارتار در فصل جدید رقابت‌ها حضور داشته باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/137433" target="_blank">📅 11:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137432">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⚡️
⚡️
⚡️
استقلال طی یک بیانیه اعلام کرد که با وجود تلاش‌های گسترده و مستمر مدیران در هفته‌ها و ماه‌های گذشته، متأسفانه سومین تلاش رسمی باشگاه برای گرفتن دستور موقت جهت باز شدن پنجره نقل‌وانتقالات نیز به نتیجه نرسید و در مقطع کنونی امکان ثبت قرارداد بازیکنان جدید…</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/137432" target="_blank">📅 09:49 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137431">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⏳
⏳
مهلت ۴۸ ساعته ادعایی ترامپ که برای تعویق حمله به ایران گذاشته شده بود ساعت ۳ بامداد امشب به وقت تهران به پایان می‌رسه و فعلا نه خبری از توافق قطعی منتشر شده و نه خبری از تمدید مهلت تعیین شده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/137431" target="_blank">📅 09:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137430">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⏺
منهای ورزش
⚡️
⚡️
طبق گزارش‌های منتشرشده، اپراتورهای تلفن همراه برای اینترنت بین‌الملل ضریب 2.7 در نظر گرفتن؛ یعنی اگه کاربر 1 گیگ اینترنت بین‌الملل مصرف کنه، 2.7 گیگ از حجم بسته‌ش کم میکنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/137430" target="_blank">📅 09:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137429">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
ایری فقط یکقدم تا پرسپولیسی شدن
🤝
🤝
🤝
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/137429" target="_blank">📅 09:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137428">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
❌
الوحده تا 600هزار تا حاضره پایین بیاد و رضایتنامه رو بده.الان باشگاه باید سر دستمزد قربانی با خودش چک و چونه ها رو بزنه/قرمز آنلاین  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/137428" target="_blank">📅 09:39 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137426">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/137426" target="_blank">📅 09:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137425">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⚡️
هلدینگ در این مدت 500 هزار دلار به چیواله وکیل ایتالیایی پرداخت کرده بود که هفته‌ای یه بار به تاجرنیا اعلام میکرد خیالتون راحت پنجره باشگاه باز خواهد شد.
😁
😁
😁
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/137425" target="_blank">📅 09:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137424">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
📝
سیدجلال حسینی:
🎙
آقای کارتال خیلی ادعا داشت و نمی‌شد با او کار کرد. کارتال باشگاه پرسپولیس را خیلی کوچک می‌دید و نمی‌دانست به یک باشگاه بزرگ آمده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/137424" target="_blank">📅 09:35 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137423">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4988f1ce4f.mp4?token=Hp9c8F-7krLWwwh7RFLwK6U815cYwjmk4H-3gVvIYWSwtTv-lzJ4jlOsHHDiI_TGxhqnYKyzESXlzWCSJrliMwL1yqL-sm8otxvQF8SSgyTem_9j0QQQdiU3Qie_i1RudE35yjY76HsPi9zn5EVznOHIr2k_3ThfLwswCNPV4g2GgAisxvfCNqm0QRNvTIX3K2rfbL39q966N2FX1-TF_i8dnWT-6RoyCWXyP5Bg1-KPuU3qSSR37AQYnkYXjA_z9eSRsbJk5R9XojaOhRU1fovejh2nEd3zdgRCfXBUuKPJjBmFb7kLH_xIw2kG3Sppk9a8fn36tmMadhx4vvYN9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4988f1ce4f.mp4?token=Hp9c8F-7krLWwwh7RFLwK6U815cYwjmk4H-3gVvIYWSwtTv-lzJ4jlOsHHDiI_TGxhqnYKyzESXlzWCSJrliMwL1yqL-sm8otxvQF8SSgyTem_9j0QQQdiU3Qie_i1RudE35yjY76HsPi9zn5EVznOHIr2k_3ThfLwswCNPV4g2GgAisxvfCNqm0QRNvTIX3K2rfbL39q966N2FX1-TF_i8dnWT-6RoyCWXyP5Bg1-KPuU3qSSR37AQYnkYXjA_z9eSRsbJk5R9XojaOhRU1fovejh2nEd3zdgRCfXBUuKPJjBmFb7kLH_xIw2kG3Sppk9a8fn36tmMadhx4vvYN9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎁
بونوس ویژه ۱۵ چرخش رایگان بازی Egypt Power x1000 با شانس جوایز میلیونی فعال شد!
💰
فقط تا پایان ۱۷ مرداد، با حداقل ۱ میلیون تومان شارژ، ۱۵ چرخش فری اسپین رایگان ۱۰۰ هزار تومانی دریافت کنید.
📌
نکات مهم این بونوس:
👇
▪
︎ ۱۵ اسپین رایگان ۱۰۰ هزار تومانی
▪
︎ ارزش اسمی بونوس: ۱,۵۰۰,۰۰۰ تومان
▪
︎ مبلغ فوق تضمین‌شده نیست و میزان برد به نتیجه چرخش اسپین‌ها بستگی دارد.
▪
︎ پس از پایان اسپین‌ها، برد نهایی بی‌قید و شرط به موجودی حساب شما اضافه می‌شود.
🔗
آدرس ورود به سایت
اسپورت‌نود:
👇
🔵
sportn5b2.com
🔵
sportn5b2.com
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/137423" target="_blank">📅 01:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137422">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⚡️
⚡️
⚡️
استقلال طی یک بیانیه اعلام کرد که با وجود تلاش‌های گسترده و مستمر مدیران در هفته‌ها و ماه‌های گذشته، متأسفانه سومین تلاش رسمی باشگاه برای گرفتن دستور موقت جهت باز شدن پنجره نقل‌وانتقالات نیز به نتیجه نرسید و در مقطع کنونی امکان ثبت قرارداد بازیکنان جدید…</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/137422" target="_blank">📅 00:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137421">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKPkt4mYCaGoHGWqtBawLxWjhBqhPr_RnLwbAUm77xTgo2h5EwcOGF9x28A9xizzgqHZuZBrdJuISFtz8jBV2CpIpFYvg7v8HDBLkWbKFP1_D2yPPBapzaZIwBVfO0t-aSxzWnIxAxzsSw65DBgIvSNrbnXKwH6PWXUKQRQTHIyo4whLdvvl7WY7qH4UQAWaC79WChbFZT5_VExHYUCYjcJ4dWBPu9-W2s2aVu2joEWVp4xxgjigSuSlE6lWUXu97js6IxtbsIQult3wq-vkFFAWKFCXiT8kJZs0p_rhs2VAKnKdX2bKlOysleKbX0enTux9ArDigfZrK5YdtNSWww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تیتر سوپر حق فرهیختگان چاپ فردا
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/137421" target="_blank">📅 00:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137420">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⚡️
هلدینگ در این مدت 500 هزار دلار به چیواله وکیل ایتالیایی پرداخت کرده بود که هفته‌ای یه بار به تاجرنیا اعلام میکرد خیالتون راحت پنجره باشگاه باز خواهد شد.
😁
😁
😁
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/137420" target="_blank">📅 00:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137419">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5Tx3xujQpL1V4RJPNqc7ZbsydSYiH_g_O2HYYn44oryF44dzDFplnDooLT6_P0ppqbk69NnDT2IEP1SSTYfqGQNpuz76hi0_KzxOGzy-WZQyPlSWu54YWBtFwMYCCDVZA9ds0PIITZQ2Iv44sItxZ6PgWz8v1P5tnPryCQDP3Gbr8YjqSlENBYEjD4_e-JVhDNMf1GYuN-Gy1baXttEQWBqqfeKqHse9uUbNoFaku9O4heReWPtaogvPVg5bHVbqq3TNiAAhCzOQiKkqpBk31bjzAutPR9OcaND1jThZ9oOt92lxfmT8C7Ee6f2Iu_xvftbdaC_7sayPXghOPpHtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
وینیسیوس در اقدامی ایرانی طور تمامی پست‌های صفحه اینستاگرام خودش رو حذف کرد و عکس پروفایلش رو هم برداشت.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137419" target="_blank">📅 00:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137418">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
❌
پرسپولیسی‌ها ریختن زیر کانال تلگرامی باشگاه ماخاچ قلعه روسیه و ۱۳ هزارتا کامنت گذاشتن که آقا این محمدجواد حسین نژاد رو بدید ما ببریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/137418" target="_blank">📅 00:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137417">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/137417" target="_blank">📅 23:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137416">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/137416" target="_blank">📅 23:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137415">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⚡️
⚡️
⚡️
استقلال طی یک بیانیه اعلام کرد که با وجود تلاش‌های گسترده و مستمر مدیران در هفته‌ها و ماه‌های گذشته، متأسفانه سومین تلاش رسمی باشگاه برای گرفتن دستور موقت جهت باز شدن پنجره نقل‌وانتقالات نیز به نتیجه نرسید و در مقطع کنونی امکان ثبت قرارداد بازیکنان جدید…</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/137415" target="_blank">📅 23:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137414">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
رقابت پرسپولیس و تراکتور بر سر جذب هافبک الوحده ادامه دارد.
❌
❌
به گزارش قرمزآنلاین، در خبرها آمده، باشگاه الوحده رضایت‌نامه محمد قربانی را ۸۰۰ دلار تعیین کرده اما تراکتورسازی حاضر است  ۶۰۰ هزار دلار بپردازد و اگر پرسپولیس با این رقم موافقت کند الوحده مجوز…</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/137414" target="_blank">📅 23:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137413">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔹
🔹
🔹
با اعلام رسمی باشگاه استقلال، پنجره این تیم بسته باقی ماند
😀
‼️
پ.ن این همه هزینه کردن وکیل گرفتن
🙃
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137413" target="_blank">📅 23:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137412">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🗣
🗣
🗣
‏  پنجره استقلال همچنان بسته است/ خریدهای جدید در خطر از دست دادن فصل  ‏
✅
در حالی که طی روزهای اخیر در فضای مجازی عنوان شده بود پنجره نقل‌وانتقالاتی باشگاه استقلال روز سه‌شنبه ۱۳ مرداد باز خواهد شد، این اتفاق رخ نداد و آبی‌پوشان پایتخت همچنان با مشکل بسته…</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/137412" target="_blank">📅 23:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137411">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
فوری؛ معاونت ورزشی منحل شد!
🔴
باشگاه پرسپولیس در بیانیه‌ای رسمی اعلام کرد معاونت ورزشی منحل شد و ۳ مدیریت جدید جایگزین آن شد:
مدیریت آکادمی
مدیریت تیم بزرگسالان
مدیریت تیم‌های بانوان
🔴
پ. ن؛ البته در بیانیه باشگاه قید شده این تصمیم هیئت مدیره با قید «تا اطلاع ثانوی» هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137411" target="_blank">📅 23:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137410">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bK4EmgkBE8VbvrbQxhZy6DA2wpA_8RSGxc_T3cf4fCXHSjq0EFDTnR-9Dcy49hwN1T5UuUUhjich9dTY-Jc3UzY8JzB3kSBosjGILJhkk_08cibfu7nqovM7v_aWhWwHbSwlb_2NciubYQqSnHAur4otSjvX3i2J3mwTNAeDbF6pCwDK-A_P81sYOoFqZ2L1gz8GzGAxwTDzcWFbpvgNJJ6uS0KWgWVnUU5cI5d-HUkjXv6eAbzJ0jB-AV-ZV1Crcnbuk4RRbZgHqrAH1A6dtfVgiEaBmWBBw6zeb3Qzce5py_m-1CxzqZLjGCmpSthMnhnOtwvnOW2ps1GgbUVaWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
خط حمله فصل بعد گلگهر
.
👀
👀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/137410" target="_blank">📅 23:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137409">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjbrO8AQXJECVFZG6oybTDDLwYjr-EP7pEih16Fel0ytKhRZSzHz-E_AmUN9skMDPc9soMuMp8dq2_v49W0TGXIraCfPjVE3rciX2K0X5p97jA34FeoqQyW7Ls45SnowYYDSRaOsxvBgNmvLa7wGIiU6GdrZRRO94Pi1QqfNIPUUaS_6z5ux6G4cjxz5V8UN2LWOVbxyJQQ3e4dLNNq5gAFboYKvsmPxpGw-ZyREkRZUl70meJrXwc3yt7rdgTnLEgS0LAuNnyHRPNKSC7wa7XtCk7TZ-DFBq9dviUIgY6U79WsxPEl08NSzI8tN3vbWSZTICrB_kQ2RDzwROj8aQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
عضو هیئت‌رئیسه فدراسیون در پرسپولیس پست گرفت
🗣
با اعلام باشگاه پرسپولیس، محمدرحمان سالاری، عضو هیئت‌رئیسه فدراسیون به‌عنوان مشاور حدادی، مدیرعامل سرخپوشان منصوب شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/137409" target="_blank">📅 23:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137408">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
قدوسی: رامین تمایل داره به پرسپولیس برگرده و از قطر هم پیشنهاد داره و تکلیفش تا روز های آینده مشخص میشه.
❌
❌
اول نیاز به تأیید تارتار هستش ؛ بعد از اون بحث مبلغ قرارداد و پرسپولیس بیشتر از سقف خودش به هیچ کسی پول نمیده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/137408" target="_blank">📅 22:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137407">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
❌
فووووووووووووری از ورزش سه
🚨
جدایی دنیل گرا از پرسپولیس قطعی شد و مدافع مجارستانی از پرسپولیس جدا خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/137407" target="_blank">📅 22:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137406">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
تعداد کامنت های پست آخر پیج پرسپولیس به بیش از 130 هزار رسیده است
✈️
✈️
هشتگ های هواداران به جذب بازیکنانی مانند قربانی، ایری و حسین نژاد اختصاص یافته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/137406" target="_blank">📅 21:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137405">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❗️
❗️
❗️
سه پیراهن ماندگار همچنان بدون صاحب
🔴
🔴
در فهرست جدید پرسپولیس، سه پیراهن مهم هنوز به هیچ بازیکنی اختصاص پیدا نکرده است
🔴
🔴
شماره ۲ که سال‌ها بر تن امید عالیشاه بود، فعلاً خالی مانده و باشگاه هنوز جانشینی برای آن معرفی نکرده است. شماره ۱۰ نیز همچنان بدون…</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/SorkhTimes/137405" target="_blank">📅 21:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137404">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قدوسی، قرمزآنلاین:
🚨
پرسپولیس و تراکتورسازی حاضر به پرداخت ۶۰۰ هزار دلار به الوحده امارات برای محمد قربانی هستند
❌
و این به تصمیم خود بازیکن مربوط که به کدوم تیم جواب مثبت بده ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/137404" target="_blank">📅 21:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137403">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">💢
💢
💢
💢
💢
#غیرـرسمی
🔴
🔴
توافقات انجام شد؛ ایری یک قدم تا پرسپولیسی شدن.
❗
❗
❗
توافقات با باشگاه نساجی انجام شد. باشگاه تا نیم فصل تمامی رفت امد هاش با شرکت هواپیمایی وارش انجام می ده. و نیم فصل قرار شده بند خرید دائمی ایری فعال بشه.
💢
💢
تنها یک گام مونده نهایی بشه،…</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/137403" target="_blank">📅 21:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137402">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
قدوسی
🚨
از داخل باشگاه خبر رسیده که به جذب محمد قربانی بسیار امیدوار هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/137402" target="_blank">📅 20:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137401">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0995cd13e9.mp4?token=IgDimF36rVw8fkqC3FrpNnqB_KHTfXInX8Nnscj8YAqKygCIxQLvCo2jW7USAv3q74s72hCxs_qsLmtHaemBqTOGGx2VpAuShMemuPGvngEo3aKbIlAxOSkOpa6oOhjJ28M9eCRIdz9xNzoXmhiI8hS_3r-RRMTZIaUyG1u7hEihAAzMDxR1z-poCQGENjVTNLdIIdQeP1KjpTSE6MVSuuzDfFf6mN22RyK8hXuAlZudlRvn7vMC99GN6Uk_D6aFXygJygvSENqAqjrqCX1zcngqpcEDKHxXPs0JLv33txpCILAAavgYlOHuHrNxuEJpk5OtM51_jXxh4t_XKQ3CKjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0995cd13e9.mp4?token=IgDimF36rVw8fkqC3FrpNnqB_KHTfXInX8Nnscj8YAqKygCIxQLvCo2jW7USAv3q74s72hCxs_qsLmtHaemBqTOGGx2VpAuShMemuPGvngEo3aKbIlAxOSkOpa6oOhjJ28M9eCRIdz9xNzoXmhiI8hS_3r-RRMTZIaUyG1u7hEihAAzMDxR1z-poCQGENjVTNLdIIdQeP1KjpTSE6MVSuuzDfFf6mN22RyK8hXuAlZudlRvn7vMC99GN6Uk_D6aFXygJygvSENqAqjrqCX1zcngqpcEDKHxXPs0JLv33txpCILAAavgYlOHuHrNxuEJpk5OtM51_jXxh4t_XKQ3CKjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">7️⃣
بونوس اختصاصی ۱۵ چرخش رایگان بازی Egypt Power x1000 فعال شد!
💰
فقط تا پایان ۱۷ مرداد، با حداقل ۱ میلیون تومان شارژ، ۱۵ چرخش فری اسپین رایگان
Egypt Power
دریافت کن و بدون پرداخت اضافه، شانس خودت را برای شکار جوایز بزرگ نقدی امتحان کن.
🔹
پس از واریز، بونوس از طریق نوتیفیکیشن داخل حساب کاربری نمایش داده می‌شود و از همان بخش می‌توانید وارد بازی شوید؛ نیازی به جستجوی نام بازی نیست.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
🔵
sportn5b2.com
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/137401" target="_blank">📅 20:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137400">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
در صورتی که فولاد برای جدایی ابوالفضل رزاق پور کوتاه نیاد ممکنه باشگاه تا نیم فصل قید جذب مدافع چپ رو بزنه و با همایی فر و جلالی ادامه بده و بره جلو
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/137400" target="_blank">📅 19:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137399">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
بر اساس گزارش آکسیوس، آمریکا، ایران و عمان به توافقی موقت ۶۰ روزه برای بازگشایی تنگه هرمز نزدیک شده‌اند و احتمال دارد این توافق روز چهارشنبه از سوی آمریکا اعلام شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/137399" target="_blank">📅 19:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137398">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✔️
✔️
✔️
العربی کویت قید بازی دوستانه با پرسپولیس را زد و از این دیدار انصراف داد. این تیم گفته به خاطر شرایط منطقه و دردسرهایی که ممکن است در کشورشان برایشان پیش بیاید، نمی‌تواند مقابل پرسپولیس بازی کند و بابت لغو مسابقه هم از باشگاه پرسپولیس عذرخواهی کرده…</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/137398" target="_blank">📅 18:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137397">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⏳
⏳
⏳
⏳
روزنامه‌ همشهری هم نوشته پرسپولیس شانس خوبی برای جذب محمد قربانی داره و مذاکرات برای مبلغ رضایت‌ نامه ادامه داره...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137397" target="_blank">📅 18:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137396">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
قدوسی: رامین تمایل داره به پرسپولیس برگرده و از قطر هم پیشنهاد داره و تکلیفش تا روز های آینده مشخص میشه.
❌
❌
اول نیاز به تأیید تارتار هستش ؛ بعد از اون بحث مبلغ قرارداد و پرسپولیس بیشتر از سقف خودش به هیچ کسی پول نمیده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/137396" target="_blank">📅 18:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137395">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1xIpEpdZU7uDlKhgyzWDVjQgHV1MFDiIaifVKovkRhufiYXeZyLYo4rtKGfpCUhtWdmre4WDgqY_ao_XW3b7q0Q8lkArIH079Pez0rBrafz1f6ea0uI6KTbo3Nn3Tx5urO5V8t6vyH-pD61BWdJcu5CvhVCbiABAQSjBWxGRPvgvpfXgL8A_0ryLwPf79oqW-PJ7oqmoc4l4SU3TN7H6cBXHont0VBN5r1C3hN2J37tLBSKmwPPmLFO4EzpOX4hMRAJHgotCzhe-C_mcFwe3pKgl3fp-Jcqukwt_HfUw5sw2NBFNz_NSn_5ZuEcbyaVGvlZVmpzZReNeJtJlUUgjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حاشیه جدید برای سرمربی زنان پرسپولیس
❌
باشگاه ایستا البرز مدعی شده نیلوفر اردلان با این تیم قرارداد سه‌ساله داشته و فسخ یک‌طرفه قراردادش قانونی نبوده است.
این موضوع در حالی مطرح شده که اردلان چند روز پیش به‌عنوان سرمربی تیم فوتبال بانوان پرسپولیس معرفی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/137395" target="_blank">📅 18:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137393">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
ورزش 3: تارتار گفته پول رامین 36 ساله و بدید ایری و قربانی جوان و جذب کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/137393" target="_blank">📅 18:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137392">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5b5yAnABXGp3JPg4NvR_9xhhdtrzGCBoV2_csHYWb5uWVHZsatVlh7hHVllya1uiBrhnUOYgv7eAicTrrlO6ymp5xiH_YWoL2L8sjGXSLgpeOnNdYxboWu-plZS0kqapUUzX2qEfuTSv4v88bZkQxHbkoO-vWoByMGzBnRfvhx-jZXPhOKnf7GZvl7xm-sotxlG9xZkWJaZcoOwPP6C6xoEUoODKdYtxc-FK-WwhlZUinfZnGQEel5XcYAZ86yZAYnwuQA-3MEsS3o18JLls-YNBoVmASUAYQjVJ6oe_QVysdL1XW6ZT4NdT_CRDUAOzaGc1_euh3p3jxb8ZstzJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
امید عالیشاه بعد از 13 سال حضور در پرسپولیس به گل گهر سیرجان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/137392" target="_blank">📅 18:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137391">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
قرمزآنلاین: دانیال ایری، رزاق‌پور و محمد قربانی سه خرید پایانی پرسپولیس
🚨
🚨
باشگاه همچنان برای جذب ایری و رزاق‌پور تلاش می‌کند، هرچند فولاد فعلاً با جدایی رزاق‌پور مخالفت کرده است. همچنین با درخواست دوباره تارتار، مذاکرات برای جذب محمد قربانی پس از کاهش…</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/SorkhTimes/137391" target="_blank">📅 16:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137390">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
❌
فوووری؛ باشگاه فجر سپاسی شیراز بازی مقابل پرسپولیس در ۱۶ مرداد انصراف داد.
❌
❌
احتمالا نساجی جایگزین این تیم برای بازی دوستانه ‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/137390" target="_blank">📅 16:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137389">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
❌
امید عالیشاه بعد از یه‌ دور مذاکره با سپاهان، فولاد و ذوب آهن حالا با مدیران صنعت‌نفت آبادان نیز درحال مذاکره هست و هر تیمی‌ رقم بالاتری پیشنهاد بدهد قرارداد میبنده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/137389" target="_blank">📅 16:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137388">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdUez8Jhcf1dCTI1-0cCUE-CiG13n5nxEQXx-kjylW9BxFR3eKCnGCeEF3ueb_TS6IVlLWHEfTGOB3Id5FVqlgYjnhl67xxu6KYKm8090gBlSP2pF3U-KcsKQvZhEuj268oaXY5lPsThHZAtOeNF1jAASLWw8cpR2rcPfmkTMKaHS2Dj31qTCkwOtSvwjo7he4KZ0MaZcI6pDE_7Edq0_W7bs2hnYZkm8lj3WRfcFh4UQJpFVKDzpeY2x9heOIabTGqO_iwQ0NQi8TWGBJtK-huw82CuhFrTdDPwkiHN6P76x6A7DNHos8uan8fH-rOZZeCuyJlm0dD3pTHcaRvL-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">7️⃣
بونوس اختصاصی ۱۵ چرخش رایگان بازی Egypt Power x1000 فعال شد!
💰
فقط تا پایان ۱۷ مرداد، با حداقل ۱ میلیون تومان شارژ، ۱۵ چرخش فری اسپین رایگان
Egypt Power
دریافت کن و بدون پرداخت اضافه، شانس خودت را برای شکار جوایز بزرگ نقدی امتحان کن.
⚡️
پس از شارژ حساب کاربری و فعال شدن فری‌اسپین‌ خود، وارد بخش بونوس‌ها شوید و ازین فرصت چرخش رایگان نهایت استفاده رو ببر!
🔗
آدرس ورود به سایت
اسپورت‌نود:
👇
🔵
sportn5b2.com
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/137388" target="_blank">📅 15:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137387">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
❗️
🔴
رامین رضاییان و پرسپولیس!!مدیران باشگاه پرسپولیس صریحا تکذیب کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/137387" target="_blank">📅 14:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137386">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⏳
⏳
با پایان اردوی ۱۲ روزه تیم فوتبال پرسپولیس در ترکیه، بازیکنان این تیم امروز طبق برنامه در مرکز پزشکی ایفمارک حاضر می‌شوند تا تست‌های پزشکی پیش از آغاز رقابت‌های فصل جدید لیگ برتر را پشت سر بگذارند.
⏳
⏳
بازیکنان خارجی پرسپولیس هم که مرخصی 2 روزه داشتن امروز…</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/137386" target="_blank">📅 14:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137385">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⚡️
⚡️
مهدی تاج، رئیس فدراسیون فوتبال: تلاش‌ می‌کنیم تا فصل آینده بازی‌ها با تماشاگر برگزار شود/ تمام بازی‌های لیگ با VAR برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/137385" target="_blank">📅 14:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137384">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
❗️
🔴
رامین رضاییان و پرسپولیس!!مدیران باشگاه پرسپولیس صریحا تکذیب کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/SorkhTimes/137384" target="_blank">📅 14:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137383">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⬇
⬇
⬇
با‌ارزش ترین تیم‌های ایرانی:  • پرسپولیس: ۱۶.۵۰ میلیون یورو • تراکتور: ۱۴.۳۰ میلیون یورو • استقلال: ۱۴ میلیون یورو • سپاهان: ۱۲.۸۵ میلیون یورو  • نساجی: ۷.۶۳ میلیون یورو •  خیبر: ۶.۳۰ میلیون یورو • گل‌گهر: ۵.۹۳ میلیون یورو • فولاد: ۵.۸۸ میلیون یورو • …</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/137383" target="_blank">📅 14:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137382">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
❗️
🔴
رامین رضاییان و پرسپولیس!!مدیران باشگاه پرسپولیس صریحا تکذیب کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/137382" target="_blank">📅 14:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137381">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔻
شاهرخ بیانی: رضاییان با پنجره بسته کلاس گذاشت.
🔹
قرارداد رضاییان با استقلال 100 میلیارد تومان بسته شده بود و بعد درخواست 200 میلیارد کرد. مگر فوتبال ایران چقدر می‌ارزد که به بازیکن 200 میلیارد تومان بدهند؟ اگر به بازیکنی چنین پولی بدهند، تیم بهم می‌ریزد.…</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137381" target="_blank">📅 14:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137380">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b74c6288d.mp4?token=ez7IV-k1IsTZqMEDNP9yYNTZ3vUFfS4jvF-1zm9UEJPJMwVskqjvW6xWWgSTwc4qj8AsjFpGPVObXKuFRIVaSGf7qkO5e2wCMcse_9HI02snCxDzvAXeTZDksbGXzQzAXado40O4NK-oGnAVsyNJsULB7nT7vZOZbMkpeTaNCJE8JuzE2WWbYe0r7iP4iP4rFlCD6otjdyHH5kmiiXpKjjwSPD0pv83PVMNip7Ef-lFfY3PDO7lzZ9Zlc_NqHv0hzhu6tfzty_Ulb2TZ1o7xKHm3dZ8x1saVfSJ6zw4C0a4VDUyQr6XYdEFVvzIsTk5lZcWRlV6SR_Dh3yAcuhJsjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b74c6288d.mp4?token=ez7IV-k1IsTZqMEDNP9yYNTZ3vUFfS4jvF-1zm9UEJPJMwVskqjvW6xWWgSTwc4qj8AsjFpGPVObXKuFRIVaSGf7qkO5e2wCMcse_9HI02snCxDzvAXeTZDksbGXzQzAXado40O4NK-oGnAVsyNJsULB7nT7vZOZbMkpeTaNCJE8JuzE2WWbYe0r7iP4iP4rFlCD6otjdyHH5kmiiXpKjjwSPD0pv83PVMNip7Ef-lFfY3PDO7lzZ9Zlc_NqHv0hzhu6tfzty_Ulb2TZ1o7xKHm3dZ8x1saVfSJ6zw4C0a4VDUyQr6XYdEFVvzIsTk5lZcWRlV6SR_Dh3yAcuhJsjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗞
🇮🇷
🤍
فوتبالی: قرارداد امیر قلعه‌نویی با تیم ملی به زودی و بعد جلسه هفته آینده تمدید میشه تنها شرطی که داره اینه باید ژنرال تو جلسه قول بده که در جام ملتهای آسیا ایران رو فینالیست کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/137380" target="_blank">📅 13:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137379">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emtDFIGzy9KUaXPgSMQbgi1yPfFdhd17wdzzjR0cH9pBInD99ZA9QPsdX7d6HdmribT8DSpd_vifHGROSRzmVxNIoGhFt7bixcZ4zbrqXP_Zpo6ZbfycxNQk4fl0U4HuCgkU-KjwwyNnGpw8dejlK8FbXXcsYTXW1GMf7TED4AQncmJ5MrDN05DzMi36zbjMQ9evDqYJRVDwZymB9sh4gKzPU1ut96s_-4xWZGJRxP_xV6iOyspnoyOp3j8yqRu2uz1sNwDW6LESiOsxwdpAGFCxsZjIGCiHAiv3Ga3MlMzXKZrew0bOtHjmz1p4_dvaMJPzS3IGK3y1UDbR67X1TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
🏅
🏅
مقایسه ارزش مهاجمان تیمهای پرسپولیس، استقلال و تراکتور؛
💵
پرسپولیس: علیپور 1.7 - سرگیف 1.2
💵
استقلال: سحرخیزان 900 - آزادی 300
💵
تراکتور: حسین‌زاده 2.2 - مغانلو 800
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/137379" target="_blank">📅 13:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137378">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❗️
یحیی گلمحمدی با حضور در تمرینات دهوک عراق به شایعات حضورش در پرسپولیس پایان داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/137378" target="_blank">📅 13:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137377">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhcpRv8A5knrxXc_9E6qb7BQjoj1yrLyEOcAdeogH8GTCEBNLXxfXzB0YJKbMZyerpq16vx3NauSayHSnON4y8Yjwii14ZAkyLLkVAv1MkY0LvbU9PqH4CY9ZhoGnd8-UVXCV7PyuvDn88DL4M_CLgNs_A-3drVfrRdGDFgE91kWc5BW1E_yfCv6UnFeFLR1v9fd_P0OhMVuuNJ88G-2y3TXrSfqwPcAB2ZxGtheB9sjRYat5MkGQb-4SCNdYy6k08YthfIP3pEDqnX4CI3MCwJtjA-AkSUHt4gMQ5AE-01DPj5beeiLl_5TJR1KSRY7qxPbaF9HV5wxZQQZKMi3jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
اعضای تیم پرسپولیس با حضور در ایفمارک تست های پزشکی را انجام دادند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/137377" target="_blank">📅 13:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137376">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔻
شاهرخ بیانی: رضاییان با پنجره بسته کلاس گذاشت.
🔹
قرارداد رضاییان با استقلال 100 میلیارد تومان بسته شده بود و بعد درخواست 200 میلیارد کرد. مگر فوتبال ایران چقدر می‌ارزد که به بازیکن 200 میلیارد تومان بدهند؟ اگر به بازیکنی چنین پولی بدهند، تیم بهم می‌ریزد. بازیکنی در سطح رضاییان 20 میلیارد بگیرد، کل تیم بهم می‌ریزد. قرارداد رضاییان به اندازه کافی بالاست، حالا برای استقلال ناز می‌کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/137376" target="_blank">📅 13:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137375">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
منهای ورزش
❌
بعد از هشت ماه نرفتن بچه ها به مدرسه
❌
فوری : مدارس امسال از مهر باز نمیشن!
❌
+ عمران عباسی، عضو کمیسیون آموزش مجلس:
❌
قطعا تو مهرماه باز شدن مدارس رو نخواهیم داشت.
❌
حالا همه تلاش‌مون رو می‌کنیم که اول آبان یا تو خودِ آبان ماه مدارس رو باز…</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/137375" target="_blank">📅 13:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137374">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6wLg1bhT0CfgvPYg3h3z3WyMA15bBtbhdj1E0hrvgN74RwBvTJ-9YCDXn7gjpaUNhrMGCpuZPwzsfFUYknxOsAktuduqDRWTPm11_lt3QfdcHxY5c5OfbRH9RonUQn_9C7gSMMtG1dbsnRr1cCZqh6BERecNUzh20HDnKyaBTcLHwluJyLOntvECmGpgQNsXOBOT0Diu8BX65qpll5VVO7AbVoavwLGO9rkFWlOhiJuqCi_ernD6zzeAv3S4DVuyf47GIz8k_oS1IkjeyO2zv8QHBojzQFApSuLLoBydlIk2-TBbtLaoV4N_MGd5I0DczCPpctnJrWJG6bFHfuJ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
با اعلام باشگاه استقلال؛ رامین رضاییان رسما جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/137374" target="_blank">📅 12:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137372">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
❌
رامین رضاییان به باشگاه پیغام داده دوس دارم برگردم./سپهرخرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/137372" target="_blank">📅 12:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137371">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✔️
✔️
✔️
باشگاه خانه‌ای که در اختیار بیفوما و گرا قرار داده بود را از آن‌ها پس گرفت و این دو بازیکن را به هتل فرستاد؛
🔻
اقدامی که گفته می‌شود با این هدف انجام شده تا شاید آن‌ها ناراضی شوند، قراردادشان را فسخ کنند و از تیم جدا شوند.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/137371" target="_blank">📅 11:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137370">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
❌
❌
ورزش سه: مهدی تارتار از روند نقل و انتقالات پرسپولیس راضی نیست و مدیران باشگاه پرسپولیس دارن لیست خرید شو روز به روز کوچیک تر میکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/137370" target="_blank">📅 11:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137369">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
امین کاظمیان در حالی اولین بازی خود با پیراهن گل‌گهر را تجربه می‌کند که شماره ۱۰ گل‌گهر را بر تن کرده که نام تیکدری بر پشت پیراهن اوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/137369" target="_blank">📅 11:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137368">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
✔️
باشگاه خانه‌ای که در اختیار بیفوما و گرا قرار داده بود را از آن‌ها پس گرفت و این دو بازیکن را به هتل فرستاد؛
🔻
اقدامی که گفته می‌شود با این هدف انجام شده تا شاید آن‌ها ناراضی شوند، قراردادشان را فسخ کنند و از تیم جدا شوند.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/137368" target="_blank">📅 10:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137367">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
❌
رامین رضاییان با انتشار یک استوری تلویحا جدایی شو از استقلال اعلام کرد
🔹
نکته جالب اینه که خیلی کلی و راجب همه تیمایی که توش بوده حرف زده و اشاره به هوادارای یه تیم نکرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/137367" target="_blank">📅 10:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137366">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✔️
✔️
✔️
کیسه که محمد خلیفه رو خریده بود بدلیل بسته بودن پنجره اش ، این بازیکن دوباره به آلومینیوم برگشت
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/137366" target="_blank">📅 10:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137365">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✨
✨
✨
پیمان حدادی:
🔴
🔴
همه امید داریم که امسال بتونیم جبران مافات کنیم. در حال حاضر تنها تیمی هستیم خارج از ایران اردو برگزار کردیم. سعی داشتیم بهترین امکانات و بهترین بازیکنان را به تیم اضافه کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/137365" target="_blank">📅 10:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137364">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⏳
⏳
مهلت ۴۸ ساعته ادعایی ترامپ که برای تعویق حمله به ایران گذاشته شده بود ساعت ۳ بامداد امشب به وقت تهران به پایان می‌رسه و فعلا نه خبری از توافق قطعی منتشر شده و نه خبری از تمدید مهلت تعیین شده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/137364" target="_blank">📅 09:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137363">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‼️
رامین با آسانی هم به مشکل خورد
⚡️
رامین رضاییان و یاسر آسانی یکدیگر را در اینستاگرام آنفالو کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/137363" target="_blank">📅 09:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137362">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcMY1my44wlqRzC8Hulca65RxSTL_UgY9Qh2NKgtNFLf8UYVoeApKkC9PXoKfE7uod6WI0XdyRnXQKPQlzMvb-sAQDnaHPz1X-UgCPS1SsRVCMVTUOqZZXvJa_8G9bTLDsNtiKoFr_aqYQ9s8gql9Fm6Rdf_qu_XeO1CKSC90G1oe1WMQz6WWSoUDEiFJzXgLF4YVprtrjCNPafiWBDcTzbb-oaGhVZiqGfl9_ZaBb0CI-aqJN_KeXUKY0apSew3G0UuS_-ZPxss8bhexcB4770HBTBeHGqd1ITNUIGXuEYUwrtaxVoy8Z7Hps6IOBrrXKbnl2zYw-KhnyNapz1qCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین با آسانی هم به مشکل خورد
⚡️
رامین رضاییان و یاسر آسانی یکدیگر را در اینستاگرام آنفالو کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/137362" target="_blank">📅 09:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137361">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
قدوسی : پرسپولیس بین قربانی و حسین‌نژاد قطعاً یکی را جذب میکند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/137361" target="_blank">📅 09:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137360">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKgZZ2QZgtS-Sbal2Qm2Y1NTnreIsyVEEFvOubz3g1uYpJ3aR6hairMufqSyxvIK9YxUKgS5RvMlAMe2IlKUNMWsnLvBiprHhkIWHQbggDOw7Bn7Gen5xlIUCOkTTVDm7J0Qk2onGbQmsWA2d4r0-iKq4UKJopBnrzXj6yQ1rDUJdNc6OdjvJjVWBtLXAJfsbwinl26j0tuB3Cgp_ZGpV7O8go-9lzN-f_HEDqrNFDd0HR6-mciu5YMMw-THoeTmQlPdFil2shzz1Spf-dtMMQu1Q0lAAOvGc29tFjmqlGo2Mit3YnT5YqkJu6G_8efEQLgEM1SrqGELtrH6R4SOeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/137360" target="_blank">📅 09:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137359">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4988f1ce4f.mp4?token=KXRtQB30MO_JoN-QFXiQxuG4LA92dQ8crpl2NLqISQeeTVH2XrdNG57ISHHzIA9RONYAJNL6hlwiwZS7Y6Gf9QjeAbDYAFka7aL-9jlJrl2Cjbfna_5GwojUqZmmViqs3sQqs3p8stRDVUSFgysy_QaZQ1ZWn-fjN0Wlxt2shzxvvLwDPEg7iWgrKzbP6lrlu-dUpUI0i4E7dXdb9bT14WSia-h09YyTxAKJkXL6EH6KuapNHvabuUqTgurWOMNakhZ1BlsNNjCyheyQTUrfJf9TfuIOIi3LlkhfnQWFC6LejvZrQeYyLw4vapHDNkJZLrPghozD4VNIeVcfUbI5Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4988f1ce4f.mp4?token=KXRtQB30MO_JoN-QFXiQxuG4LA92dQ8crpl2NLqISQeeTVH2XrdNG57ISHHzIA9RONYAJNL6hlwiwZS7Y6Gf9QjeAbDYAFka7aL-9jlJrl2Cjbfna_5GwojUqZmmViqs3sQqs3p8stRDVUSFgysy_QaZQ1ZWn-fjN0Wlxt2shzxvvLwDPEg7iWgrKzbP6lrlu-dUpUI0i4E7dXdb9bT14WSia-h09YyTxAKJkXL6EH6KuapNHvabuUqTgurWOMNakhZ1BlsNNjCyheyQTUrfJf9TfuIOIi3LlkhfnQWFC6LejvZrQeYyLw4vapHDNkJZLrPghozD4VNIeVcfUbI5Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">7️⃣
بونوس اختصاصی ۱۵ چرخش رایگان بازی Egypt Power x1000 فعال شد!
💰
فقط تا پایان ۱۷ مرداد، با حداقل ۱ میلیون تومان شارژ، ۱۵ چرخش فری اسپین رایگان
Egypt Power
دریافت کن و بدون پرداخت اضافه، شانس خودت را برای شکار جوایز بزرگ نقدی امتحان کن.
🔹
پس از واریز، بونوس از طریق نوتیفیکیشن داخل حساب کاربری نمایش داده می‌شود و از همان بخش می‌توانید وارد بازی شوید؛ نیازی به جستجوی نام بازی نیست.
🔗
آدرس ورود به سایت
اسپورت‌نود:
👇
🔵
sportn5b2.com
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/137359" target="_blank">📅 01:27 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
