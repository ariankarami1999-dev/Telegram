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
<img src="https://cdn4.telesco.pe/file/dv-1XR8JlYFVkT2OgS5mIyi95tsANhKtya1QbAm7_KdArqbMF03M9DfoXxFkuJyMSLPDp3L40_hrNEnQKt4caC598MzadwmZnx96QoADnHFrCsNDLrwK859BjlncACKVbGJuDjlz2SOiNJVJF_rXb_TaYwfvkvxwhPbB8O9zxxobLY_vTJwqZij49-JtriG1WYxeYRTB_moC_3jpYAJmWQs_hzKeiJXSI-mp5cbTqofPD4fsZmgP2qwqPENtIj7KsZGneSEWQga5fhVXtPNsrCDE0TxSej_fwNJfI8YF9AJ8-p7mbINsv483FldF78SKDNL8gkS2P4MtG8LInqwFgQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 12:21:09</div>
<hr>

<div class="tg-post" id="msg-135331">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❗️
❗️
لیست تیم ملی امید اعلام شد.
❌
در این لیست 4 بازیکن از پرسپولیس به تیم ملی امید دعوت شدند.
🔴
امیرحسین محمودی
🔴
علیرضا همایی فرد
🔴
سهیل صحرایی
🔴
فرزین معامله گری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/SorkhTimes/135331" target="_blank">📅 11:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135330">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
برای تمرین امروز چهارشنبه به بازیکنان  پرسپولیس اطلاع‌رسانی شده و در این بین به ۳ بازیکن دارای قرارداد، گفته شده که تا مشخص شدن وضعیت‌شان، در تمرین شرکت نکنند.
✅
امید عالیشاه، مرتضی پورعلی گنجی و میلاد سرلک این سه بازیکن هستند.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/135330" target="_blank">📅 10:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135329">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
محمد قربانی: با باشگاه الوحده امارات قرارداد دارم. رضایت نامه من برای باشگاه های ایرانی 2 میلیون دلار و برای باشگاه های خارجی 3 میلیون دلار است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/135329" target="_blank">📅 10:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135328">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
✅
بازم تایید شد
✅
محمد قربانی: بله باشگاه پرسپولیس به صورت جدی دنبال جذب من است. اما مبلغ رضایت نامه من بالا بوده و این کار را کمی سخت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/135328" target="_blank">📅 10:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135326">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❗️
❗️
شنیده ها : فوری؛ پیغام‌جدید محمد قربانی به پیمان‌حدادی مدیرعامل باشگاه پرسپولیس: پیشنهاد مالی شما رو پذیرفته‌ام، رضایت نامه ام رو بگیرید روز شنبه قراردادم رو امضا خواهد کرد.
❌
❌
پیشنهادمالی‌پرسپولیس: سه ساله بوده. سال اول 80، سال دوم 110 و سال سوم 150 میلیارد…</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/135326" target="_blank">📅 10:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135325">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
فورییییی به نقل از CBS :
🔴
علیرضا فغانی قضاوت فینال جام جهانی 2026 برعهده خواهد داشت !
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/135325" target="_blank">📅 10:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135324">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❗️
تارتار قراره در تمرینات نظرشو راجب باکیچ و بیفوما اعلام کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/135324" target="_blank">📅 09:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135323">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMAYVayrQVZOyVmnVjCj2j_8_fP69et_Ork8nrjSR4ii_RS8hoR0n_noRuMb9jtzFisUosFzxfBJE4-3MdtsC4LPTWykOI4vvmmVjwvhGzhKQxjE_UB-qrqDtOVSl62-H7iE94YoNj2FP2S773PFjP-3MrnCALlGFZ8F9FiwOG6TNqUbts6uEF4sdeAIAMKXljy0H3UULo4CyAqGl4I84YcUohNbUeOoR8WvSw4bJHUg-O-IbCGkZzemRfPNpsxH4fI0skZvq0CKyp17OFiOBt2JUtjq-ldtaUbXUsyMVe1BpzQRN9t90MNL8G2NRYepT8WBi2MPgVqt9zks33SehA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تیتر روزنامه گل: «گل‌گهر به پرسپولیس پیوست!»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/135323" target="_blank">📅 09:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135322">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
ترامپ: این اقدام، تلافی بمباران کشتی‌ها توسط ایران در دیروز است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار وخیم‌تر خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/135322" target="_blank">📅 09:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135321">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
مهدی زارع، گزینه جدید پرسپولیس!
🔴
🔴
طبق شنیده ها، مدیران پرسپولیس مذاکرات برای جذب مهدی زارع، مدافع ایرانی تیم اخمت گروژنی روسیه را آغاز کرده‌اند و این بازیکن یکی از گزینه‌های اصلی سرخ‌ها برای تقویت خط دفاعی محسوب می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/135321" target="_blank">📅 09:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135320">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp0CPZWS8K4zH1PeWWVdaanfyYbN8gyxA2Vqg4eFeWkdVJiX6RPnusNpWW6PFqzxn-PUpRr5kpCYPqBwLGAizmUl4hZaw0u2ttQcwv-oix945mmy81efRodkdUso-3CynqJ4D-Me1bv5UxMonE36jrPzIPSsOMyipq-8nAj-AuVrjuM_bAtjT6pxuncNkmKrGE6E2bnhQ1cgEWjZqp5lVDiGFbpUdpxxZsb0FVnf5Ibh9q8XHWBKXLQO4nEqpjXhSM_vAPZbL59pMQz6jhAQTvg7J4BTi9DOOttt24MIxDfpHK8a7ST75JDyAbdUbAnWqoFo0fegW8DYHV3CDX50lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مهدی تارتار کادر پزشکی گل‌گهر رو به باشگاه پرسپولیس معرفی کرده و احتمال بسیار زیاد تمامی کار پزشکی گل‌گهر به پرسپولیس خواهند آمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/135320" target="_blank">📅 09:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135319">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135319" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر پنجشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
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
https://t.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/135319" target="_blank">📅 01:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135318">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oy4AiyCW9YhXDVNj1gV9QU7PDtgy_miXm0NhZfgD-li9EmJNz-nZwuXCgt0D5lFUTrhtiKVLcNWVLUum2qwcjyk-WA95P0SWHweI2beDrojss16rR-t_2cu5de__o36dZIA_7OQCGh5G-5-vv6aVr3qX9BKWz4_6XNxrz9bO3mBIhIAJ4XPPhdECBOT5OreL3AdWyz-AGqPuncuVqjWcYy8XFEv9UHaVgvkRrlBZY0cL5nzJkeXtYDSi50oq2O-8rg-3lAsgpyqvAEXUsqZD7RsWAPGvMxmFZsE3VCSu4KTKhfKIQvKgR21lIrTM1SA_A9qY1cPQyuWMsMoh8zZ6pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین سایت جهانی برای کاربران ایران با واریز برداشت مستقیم
⬇️
🪙
سایت بین المللی و معتبر لاین
بت
❤️‍🔥
اسپانسر لیگ  فرانسه
💳
واریز و برداشت ریالی
👀
بازگشت باخت ب صورت هفتگی
📣
دارای پشتیبانی فارسی فعال
🎁
بونوس
💯
روز های دوشنبه
🎡
کدهدیه ثبت نام
➡️
L5670
🔗
《 لینک سایت برای کاربران ایرانی》
👍
《 دانلود اپلیکیشن اندروید》
❤️
https://t.me/+dukgrB6-zGsyNGM8
🔻
جهت استفاده از وبسایت از آی پی کشورهای آسیایی
🇷🇺
یا کانادا
🇨🇦
، استفاده کنید
Ⓜ️
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/135318" target="_blank">📅 01:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135317">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
🔴
مقام ارشد اسرائیلی به الحدث: ترامپ در تماس تلفنی به نتانیاهو اعلام کرد که حملات امشب به ایران تمام عیار خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/135317" target="_blank">📅 01:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135316">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❗️
❗️
طاهرخانی: کوشکی رقم خیلی بالایی درخواست کرده و باشگاه داره باهاش مذاکره میکنه تا قیمتشو کم کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/135316" target="_blank">📅 01:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135315">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
🔴
علیرضا کوشکی هم‌اکنون بازیکن آزاد است اما باشگاه استقلال در تلاش برای تمدید قرارداد با او است. پرسپولیس کار راحتی برای جذبش ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/135315" target="_blank">📅 01:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135314">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
انفجار های چابهار خیلی شدید و بی سابقست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/135314" target="_blank">📅 23:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135313">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
✅
ورزش سه
❌
علی علیپور در حال حاضر باتجربه‌ترین بازیکن پرسپولیس محسوب می‌شود و این موضوع باعث تسهیل در تمدید قرارداد این بازیکن شود.
🔴
هرچند که او احتمالا انتظار دارد تا پرسپولیس عدد مناسبی را پیش روی این بازیکن بگذارد تا او از نظر مالی هم شرایط بهتری را…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/135313" target="_blank">📅 23:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135312">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
🔴
موج جدید حملات سنگین آمریکا به جنوب کشور آغاز شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/135312" target="_blank">📅 23:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135311">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❗️
آکسیوس: شدت حملات امشب طی ساعات آتی بیشتر از دفعات قبل خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/135311" target="_blank">📅 23:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135310">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
فوری/ CNN:
🔴
حملات آمریکا به ایران ممکن است در ساعات آینده آغاز شود، تیم امنیت ملی ترامپ در حال تصمیم گیری در مورد دامنه و گستردگی حملات آتی می‌باشند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/135310" target="_blank">📅 23:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135309">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❗️
❗️
نساجی برای خرید ایری ۷۰ میلیارد پرداخت کرده و دو تیم استقلال و پرسپولیس هر دو بدنبال جذب این بازیکن هستن، احتمالأ رکورد مبلغ رضایت‌نامه تاریخ لیگ برتر شکسته بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/135309" target="_blank">📅 23:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135308">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cO8kSNw4TwnUL3CMULrXwp-Qk-QcI43o20n66sczAIfi3exxriNyK5KBKSgbWxEjADNHdWX_EIfIcq13SLGo8QyXK4jlMW8ddjpfceWb6OfebP1WLvwV6kkIovrm8lpRLPdnhUqR9ZLOJNI3TplOd5KWdYhhsBxumJ_r1S1vaT1PrhbZgx5J7LdCg-1hDzegPEtznFgPex42XjwfYPEks7xL_NsjmRADfJNlw_oGPqTCNIfPhW0rfi3wBTYTGC5Ckzred4WSHr5UYyrILW6aWOis681Wj-3evKcIa0n_9WyctveNECb6AOntPQ51jHyjvXcm4ukz89mDMAEnZzSJbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
خبرگزاری آنا: به دلیل یه سری مسائل حقوقی هنوز از جلالی و شهرآبادی رونمایی نکرده. بعد از حل شدن مسائل حقوقی از جفت شون رونمایی میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135308" target="_blank">📅 22:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135307">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
ترامپ: حملات امشب به ایران ممکنه خیلی بزرگ باشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/135307" target="_blank">📅 22:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135306">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
گویا باشگاه استعلام‌ گرفته که مهدی ترابی هم اکنون بازیکن آزاد است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135306" target="_blank">📅 22:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135305">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
قدوسی: مذاکرات با احمد نوراللهی در حال انجام است و مدیران باشگاه در تلاش هستند این بازیکن رو به پرسپولیس برگردونن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135305" target="_blank">📅 22:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135304">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❗️
غایبین تمرین امروز پرسپولیس:
❌
پیام نیازمند ( تیم ملی )
❌
محمدحسین کنعانی زادگان ( تیم ملی )
❌
مرتضی پورعلی گنجی ( مازاد )
❌
میلاد محمدی ( تیم ملی )
❌
دنیل گرا ( مازاد )
❌
میلاد سرلک ( مازاد )
❌
مارکو باکیچ ( نامشخص )
❌
امید عالیشاه ( مازاد )
❌
علی علیپور (…</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135304" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135303">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
غایبین تمرین امروز پرسپولیس:
❌
پیام نیازمند ( تیم ملی )
❌
محمدحسین کنعانی زادگان ( تیم ملی )
❌
مرتضی پورعلی گنجی ( مازاد )
❌
میلاد محمدی ( تیم ملی )
❌
دنیل گرا ( مازاد )
❌
میلاد سرلک ( مازاد )
❌
مارکو باکیچ ( نامشخص )
❌
امید عالیشاه ( مازاد )
❌
علی علیپور (…</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/135303" target="_blank">📅 21:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135302">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❗️
غایبین تمرین امروز پرسپولیس:
❌
پیام نیازمند ( تیم ملی )
❌
محمدحسین کنعانی زادگان ( تیم ملی )
❌
مرتضی پورعلی گنجی ( مازاد )
❌
میلاد محمدی ( تیم ملی )
❌
دنیل گرا ( مازاد )
❌
میلاد سرلک ( مازاد )
❌
مارکو باکیچ ( نامشخص )
❌
امید عالیشاه ( مازاد )
❌
علی علیپور (…</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/135302" target="_blank">📅 21:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135301">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
نخستین تمرین پرسپولیس زیر نظر مهدی تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135301" target="_blank">📅 21:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135300">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6CR-aqPTUQ3LfOW8E2Z7MDxGTAhYWfdMfEbSDtg94u0eT9Yig_B78ZEtDcfR2TRvhicFYUHwYTNSIKPcqDHVg1wAh4it5NdhBnCnKHoPEcW57xrP970AyAutpzwwpjkamAQ2zpnro-xSoaPRB2wHhsAuByDMbxGC2UKps_7aR-VIYEyY85Ue2fjPqVYX-hE7d_wY-i95uyYiac5QagXql8kNwSG71YOFU-ePwhfveOPoyDuEV8YtMEMa783HCbcQi988_xSroSRTCH2WfwOm3X-vc7mmHTAjbsxb4pYlGTky-GBN24Agvv2dhiB8nhDEOPeQQgWlG4GYTl6BHnORA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نخستین تمرین پرسپولیس زیر نظر مهدی تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/135300" target="_blank">📅 21:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135299">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzTlFxat2k2ZlyUOf_LqOBvWpJkefMaqhJZdix-QZDlCVkUH77NxDAWZBVgfr1wgTpmYxmFD8g2NZDOJUadApR5Q5wRpNJ3BXH23me2XxF4uWveqZcpw1PwjQUkdgkVo0_p-FHtf4Eg3ih9K3hYr5rasilAKH7C_Yr8ChHBHVna4VvUfmEHC6jFgf3RtFstlPr2c34dRBkXomd7o5Bp8FrkRxFnof05tWjrOR5Zd05s7Ftb3F3S4kzwCF5zWZdto7sfZ2vrkDbj9CqURxcQ9ckrk0ImTBn7CrugIhL9--BO0IpL6u_XpRn4fwmGPR6-Gv9pZeAEIP3_gn8C9FaEt_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه سپاهان که تمایل به جذب نعمتی داشت، طی روزهای اخیر مذاکراتی با این ملی‌پوش ایران انجام داد و به توافق نهایی دست یافت تا خط دفاعی‌اش را با جذب او تقویت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/135299" target="_blank">📅 21:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135298">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه ، وقتش نرسیده که از فوتبال دیدن پول در بیارید؟
😉
✅
@FuckBet</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/135298" target="_blank">📅 20:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135297">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jDFi6fddJmy-CcoecI7fdcg2dyocyWf98wP2f6X95D9ht0SRnVOBTkUvyYvYTi5DzlxG65tqR57lUNXtXyxYjSKGeRmJdZLXv-VwkXA6lVwHb8rFmZ8dp9fnGUeDPYrvr_NHmAGn396cEaKzBMNLP8IFFX2yU1i0ueD8L-UOwd7qmjV0mfxeuCa7BUaD_mFgxxozYB24Oa_e0p4v_wUIkgzZc7gTRAf4tyPbonhD74y8AXFDu16x4OQNT5By2EvpSUPtDl30LZPhpdHTfXmdg7jVQ5W-5QCEZClx91Fe74h-lPHHwQ7BFd84bQ5Wr0zl5uu8V3C1Rt1tlfJcNtPiBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی نه ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/135297" target="_blank">📅 20:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135296">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFW9ce85-y0-EaNYUh_WKLH9T1kWkJ8viP0dIZLTZL5LyzohCrjmByuaFlXEeoTktcq8fDyK_cjU0gnN0X9Ssc14U0upvjfIQ84B0UsiXmTayTZCbeRwfHx3Nmr00Nr0ANkXbhea8Kg2qKsLs35KQDSMFk_30qrz8Qnsu2tyTd4lv5OJxfIZFRtoe2TZxm3ZLzhPm7ubNT0dLXNgLpmqPSsSgiHMvh341CYfyc7OK4RDgW0GWD1aBz2YkcydxjGTrr9ZRjz_LP50OKKg25I3UhM3rcIGm9JOaIK-bz-4AioQSnfOLv9paeduRvZ9lQsbHJQkEU3oUHODBnhx5GWpzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مراسم معارفه ی تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135296" target="_blank">📅 20:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135295">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
یه هوادار تو دایرکت نوشته: امروز دم باشگاه بودم آقای خلیلی گفتن نه نوراللهی میاد نه محمد قربانی رضایت نامه هرکدوم دو میلیون و پانصد هزاره//قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/135295" target="_blank">📅 19:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135294">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
باشگاه به خاطر فشار هوادارا فعلا پورعلی رو تو آب نمک خوابونده تا نتیجه مذاکرات با قربانی و نوراللهی رو پیگیری کنه و اگه اونا جذب نشن پورعلی رو نهایی می‌کنه/ فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/135294" target="_blank">📅 18:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135293">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❗️
❗️
شنیده ها : فوری؛ پیغام‌جدید محمد قربانی به پیمان‌حدادی مدیرعامل باشگاه پرسپولیس: پیشنهاد مالی شما رو پذیرفته‌ام، رضایت نامه ام رو بگیرید روز شنبه قراردادم رو امضا خواهد کرد.
❌
❌
پیشنهادمالی‌پرسپولیس: سه ساله بوده. سال اول 80، سال دوم 110 و سال سوم 150 میلیارد…</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/135293" target="_blank">📅 18:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135292">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
#شایعات
🔴
علیرضا کوشکی در حال مذاکره با پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/135292" target="_blank">📅 18:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135291">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
تصاویری از حضور بازیکنان تیم پرسپولیس برای انجام نخستین تمرین برای شروع فصل جدید که چهره ها نشون از روحیه و شادابی بچه ها داره با کادر جدید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/135291" target="_blank">📅 18:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135290">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
شهرابادی، طاهری، پورعلی و جلالی پوستر رونماییشون آمادست و فقط منتظر تأیید حدادی هستن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/135290" target="_blank">📅 18:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135289">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-Go1yjFn1x2COiajtPgzxQ_uSuava9eRqfYJfQda4kxypgrq1wyqCuQERotElDJzjui0lCOAI2-Ke1E1r0-2_qv-RRBsy8byiU-kNew7_LSsdayzb9hztYbf8trSZmxUcknL-s5VZMxMlkaNEfDGpSuz7QzjO7NEBcGon7Fu0dHBDzCpjKCMT3bQdUVXq8IZi0Bs6sByT_Q5Zb3DWxvCVZPMPepUPHAo-sGQo3CcWABV-beDx-KfIKjSvHiZ1iljytPaBHm8f5qVzw7eXoGFAtF602YdVhWGbQSxQYYsihpJySIvilfDjpIZ7ir9n2s6auh1smiZHMGaw7KFHyyyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصاویری از حضور بازیکنان تیم پرسپولیس برای انجام نخستین تمرین برای شروع فصل جدید
که چهره ها نشون از روحیه و شادابی بچه ها داره با کادر جدید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/135289" target="_blank">📅 18:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135288">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
احتمالا باشگاه برای رونمایی لایو داره  وگرنه چه‌ اصراریه که تاخیر داشته باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135288" target="_blank">📅 17:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135287">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✅
✅
باشگاه ماهم عالیه
❗️
طاهری، شهرآبادی، جلالی بستن و عکس هم انداختن پوسترشونم امادست
❌
اما باشگاه میخاد یجوری رونمایی کنه که تبلیغات داشته باشه
😐
مثلاً لایو بزاره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/135287" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135286">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
🇺🇸
ترامپ:
❗️
دیشب جزیره خارک رو زدیم ولی به نیروهامون گفتم نفت‌ش رو نزنید ممکنه بخوایم جزیره رو تصرف کنیم چون از دستشون کاری برنمیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/135286" target="_blank">📅 17:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135285">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
باشگاه به خاطر فشار هوادارا فعلا پورعلی رو تو آب نمک خوابونده تا نتیجه مذاکرات با قربانی و نوراللهی رو پیگیری کنه و اگه اونا جذب نشن پورعلی رو نهایی می‌کنه/ فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135285" target="_blank">📅 17:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135284">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
تایید خبر دیشب مون
🚨
🚨
🚨
🚨
تسنیم: ابوالفضل جلالی دو ساله به پرسپولیس پیوست.همچین پوریا شهرآبادی چهار ساله با پرسپولیس امضا کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/135284" target="_blank">📅 17:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135283">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
احتمال افزایش نفرات لیست مازاد پرسپولیس؛
🔴
وضعیت نامشخص چند سرخ‌پوش
❗️
❗️
فرهیختگان: دور جدید تمرینات پرسپولیس در حالی از فردا چهارشنبه در زمین شماره سه ورزشگاه آزادی برگزار خواهد شد که هنوز تکلیف نهایی برخی از بازیکنان این تیم مشخص نیست.
✅
✅
اگرچه مهدی تارتار…</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/135283" target="_blank">📅 17:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135282">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❗️
ترامپ: حملات امشب به ایران ممکنه خیلی بزرگ باشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/135282" target="_blank">📅 17:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135281">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❗️
❗️
#فوووووری از ترامپ: آتش‌بس با ایران به پایان رسید و از این لحظه هر دستوری بخواهم برای زدن ضربه نهایی خواهم داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/135281" target="_blank">📅 17:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135280">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
مطابق اعلام سایت ترانسفر مارکت؛ تا به این لحظه مهدی ترابی و مهدی هاشم نژاد قراردادی برای فصل آینده با باشگاه تراکتور ندارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/135280" target="_blank">📅 16:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135279">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
🚨
🚨
⭕️
بازگشت خانبان به پرسپولیس: به‌زودی....!
⭕️
بر اساس شنیده ها، مدیران ارشد باشگاه پرسپولیس با توصیه خداداد عزیزی به دنبال بازگرداندن مهرداد خانبان آنالیزور سابق پرسپولیس به کادرفنی پرسپولیس است
🔸
آنطور که از باشگاه پرسپولیس خبر می‌رسد احتمالا باید برای…</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/135279" target="_blank">📅 16:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135278">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
💙
ابولفضل جلالی با قراردادی دو ساله رسما به پرسپولیس پیوست.
❓
نظرتون درباره جلالی چیه ؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/135278" target="_blank">📅 15:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135277">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
💙
ابولفضل جلالی با قراردادی دو ساله رسما به پرسپولیس پیوست.
❓
نظرتون درباره جلالی چیه ؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/SorkhTimes/135277" target="_blank">📅 15:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135276">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
البته این خبر هنوز رسمی اعلام نشده و یکی از ادمین های ما در نشر آن عجله کرده. جلالی گفته امروز، فردا با رسانه باشگاه مصاحبه می کند که پالسی است به نشانه امضای قرارداد‌. این مدافع چپ جوان به تازگی تمام پست هایش با پیراهن استقلال را در اینستاگرامش پاک کرد.…</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/135276" target="_blank">📅 15:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135275">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
💙
ابولفضل جلالی با قراردادی دو ساله رسما به پرسپولیس پیوست.
❓
نظرتون درباره جلالی چیه ؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/135275" target="_blank">📅 14:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135274">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❗️
با تایید سهیل صحرایی این بازیکن به عنوان بخشی از مبلغ رضایت نامه گلگهر برای شهرآبادی، از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/135274" target="_blank">📅 14:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135273">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❗️
شنیده ها :گل‌گهر برای شهرآبادی 120 تا میخواسته
❌
ولی گویا صحرایی + 80 میلیارد توافق کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/135273" target="_blank">📅 14:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135272">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/295a60cd54.mp4?token=OzktttyDueHEbCP8ec2tqZ8Ojw4d0UprlONG6I5nkrDauZTTy0cwwvGNLmrUVtnAUBCeSZQIBbyMQbTtd9YS4gEKj2YmM45M4rVHXZ-p1R-zGbIGmhhdyQBp6rrnz44PSTLGMKSbgAM5nzV8FIjxCfmTVk4mPftaMqhSUTC-VAQIabdnvNK12UZiG7gTudWu1mnUqUtqeGh-Aze1E2ZKrW_Mjgk8E38pBf8NbCYOeuvqdh4Q7QfZo0LO_yEHPWG7UI-AY4-xgkCf4VFR-kQsuDwXsotcgrES_bh4JFV_QFDDM4gb5VVzRWlnHYLQIGfaM0QE82YTM3L318X_9LbPpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/295a60cd54.mp4?token=OzktttyDueHEbCP8ec2tqZ8Ojw4d0UprlONG6I5nkrDauZTTy0cwwvGNLmrUVtnAUBCeSZQIBbyMQbTtd9YS4gEKj2YmM45M4rVHXZ-p1R-zGbIGmhhdyQBp6rrnz44PSTLGMKSbgAM5nzV8FIjxCfmTVk4mPftaMqhSUTC-VAQIabdnvNK12UZiG7gTudWu1mnUqUtqeGh-Aze1E2ZKrW_Mjgk8E38pBf8NbCYOeuvqdh4Q7QfZo0LO_yEHPWG7UI-AY4-xgkCf4VFR-kQsuDwXsotcgrES_bh4JFV_QFDDM4gb5VVzRWlnHYLQIGfaM0QE82YTM3L318X_9LbPpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سهیل صحرایی هم وارد دفتر باشگاه شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/135272" target="_blank">📅 14:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135271">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135271" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/135271" target="_blank">📅 14:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135270">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/135270" target="_blank">📅 14:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135269">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsNaBiQJymnYjlNP9lIIKb6D1YTibg5SkwRp1qlA9mSkEVOdmVL1uI7bRgNgY2d9UjzxburHJC4TQ3joxqbs40YSNR_n5Q3rkYoLzapDTiJEtdbss5le3zUM8uY9D6FZh6I4gj2h68kNm-IuIi04twq7MjwlFtPswWEhrWuqVDY3-4_ubsNImxkVOx2Xx0CQltQtq6V0HGnCEA4uCDlChaO_aTnmoq7uedAz3MJ5LI1cMGF8LWWeuUgRMsHjG5MTSCrak3i1-MZ_0t-aJv8sz5sdwee9zXEaeDP24h_cZvEGRYjf_oinv3841W2hry0ehkQVqB7gZS0Ej0y7VhxuXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💙
ابولفضل جلالی با قراردادی دو ساله رسما به پرسپولیس پیوست
.
❓
نظرتون درباره جلالی چیه ؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/135269" target="_blank">📅 14:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135268">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c56bb19ad7.mp4?token=Kjm2cR9A5VnnFReRWxaaxqbV7ptFhCpfVL6i7f-rqK_-fQS-IrQiTUS54UG5Qg2x7-9Z_EJfGMP9IIoF8JOqLPZYZZJmJSZ5SIcJMTFuNWxNVyMyefaUx0WFKFsfGoGcuyluGw8j0mB83iWCQjsk7Bhq13DKmTxr4xUYBhrh8p0Fuju_chUzh6cHK2yWnis3SmcieqBZc8QaKl-vB6Fqo9UEyDuQ_zYoHixA48S8G0xVZH26CfJqbxyzIVih-qDsDoy-OEz_WVxsGMfrXKj5MCafaClln8Ot7uTQC67FyMR84LhmkGj7Wm5ZRt1G5IPna-MicwaJFSmuN1EY50ed0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c56bb19ad7.mp4?token=Kjm2cR9A5VnnFReRWxaaxqbV7ptFhCpfVL6i7f-rqK_-fQS-IrQiTUS54UG5Qg2x7-9Z_EJfGMP9IIoF8JOqLPZYZZJmJSZ5SIcJMTFuNWxNVyMyefaUx0WFKFsfGoGcuyluGw8j0mB83iWCQjsk7Bhq13DKmTxr4xUYBhrh8p0Fuju_chUzh6cHK2yWnis3SmcieqBZc8QaKl-vB6Fqo9UEyDuQ_zYoHixA48S8G0xVZH26CfJqbxyzIVih-qDsDoy-OEz_WVxsGMfrXKj5MCafaClln8Ot7uTQC67FyMR84LhmkGj7Wm5ZRt1G5IPna-MicwaJFSmuN1EY50ed0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پوریا شهرآبادی هم بعد از جلسه با مدیران پرسپولیس، مثل جلالی بدون اینکه با خبرنگارا حرف بزنه، محل جلسه رو ترک کرد و رفت اردوی تیم امید.
✅
✅
خودش گفت باشگاه اجازه مصاحبه با رسانه‌ها رو بهش نداده...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/135268" target="_blank">📅 14:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135267">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e4a201f71.mp4?token=d1d4JPvztZmTNsElCfVBQ8fb1Px-w6GTTB8SAw6h8SDifS_gRc0kogZadd31juq2uO8FMWyziRpzTH14lHmVdQTobL74s33sMW9En9NgIae-4lwhJYcbMGvZjmxF7TmMiFm5EtVux6ZKUpALLZg4EFGTi0dLAjFRrrgph9bXIe6kUahjPmanQ3aSmfLLr-Z3FpRsFULIXntK1VC_iSBQ01Wa3ggmqi-JQxQZhYyNOTZ9SLh0FggecjRmkaSbp_BblR83IgYQMITkcKhufBKaKxtNNm3C6cA93q0HEJ9kgCbHqtPYEfn5ttO0RrT8s1cMI6PjQpW24xKq6ezumDnGlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e4a201f71.mp4?token=d1d4JPvztZmTNsElCfVBQ8fb1Px-w6GTTB8SAw6h8SDifS_gRc0kogZadd31juq2uO8FMWyziRpzTH14lHmVdQTobL74s33sMW9En9NgIae-4lwhJYcbMGvZjmxF7TmMiFm5EtVux6ZKUpALLZg4EFGTi0dLAjFRrrgph9bXIe6kUahjPmanQ3aSmfLLr-Z3FpRsFULIXntK1VC_iSBQ01Wa3ggmqi-JQxQZhYyNOTZ9SLh0FggecjRmkaSbp_BblR83IgYQMITkcKhufBKaKxtNNm3C6cA93q0HEJ9kgCbHqtPYEfn5ttO0RrT8s1cMI6PjQpW24xKq6ezumDnGlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🏅
جلالی هم اومد بیرون… به خبرنگار ها گفته با رسانه باشگاه مصاحبه کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/135267" target="_blank">📅 14:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135266">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24a7269d75.mp4?token=ZTuYP5gu19NKXXM9vb9miUyX24E6X67xPs2D8As2lrcCz0cxhXfOIhJOEfu33oTq62Q4uEFthvjhj53ICromSZhVNeJIA0Sqo7Hq75xhM4Qr5jfH3tZSS03iQFiWCFSnziunsVMTrGtNxjIvYXIyFIP6DddqeBUxk11RqmBcKtCeG2ebZKLy56VIX-EBTQ9mJlhO-LhnEf9Tp9hwFB9cW3IUN_rS8DUrxhd5ISPo_Fpwx3gOnGqx6XRNoEjo17f2mPYdaZMlhjI1PzR09i0GltBj06UNrtn18jGwe7hOOaY55ZoepHrS-EftO_7HP1bRPrbny41fhKy0z49TebXZdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24a7269d75.mp4?token=ZTuYP5gu19NKXXM9vb9miUyX24E6X67xPs2D8As2lrcCz0cxhXfOIhJOEfu33oTq62Q4uEFthvjhj53ICromSZhVNeJIA0Sqo7Hq75xhM4Qr5jfH3tZSS03iQFiWCFSnziunsVMTrGtNxjIvYXIyFIP6DddqeBUxk11RqmBcKtCeG2ebZKLy56VIX-EBTQ9mJlhO-LhnEf9Tp9hwFB9cW3IUN_rS8DUrxhd5ISPo_Fpwx3gOnGqx6XRNoEjo17f2mPYdaZMlhjI1PzR09i0GltBj06UNrtn18jGwe7hOOaY55ZoepHrS-EftO_7HP1bRPrbny41fhKy0z49TebXZdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
محسن خلیلی برای عکس یادگاری با خرید های جدید وارد باشگاه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/135266" target="_blank">📅 13:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135265">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkXwXS9u6Xmpg-0NCSVv9ih6OzfldHYnZ0ZSqXRGoUdbwCXjMDvLhZ7fzG44-hfyaZ2RGkloxK0y6zcWzG-CZ9fLa9e2cEqOolqTHpW9n7VLkjM4zeVBYAjLBgZc0Wm7ucPpWWKvt1l5G4d-AWKygc4rRFJ7vUGSpoWk2kOd9dIhFEZgdSlKylFUCg3u2RLiACkyEfNLYRlFT9ZAfD16_rMHtcRXhJYWDEPAgPhUXdY4gLx7DUI6sV-XrOeSHeeaF13J_3kglNQfmU208xsKKTpJRk5kYSeR3MQ2hEe58DrZReEQ9UJldo8fD73cnzfHlkEARyCLMFPDj3qVOTZpEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
نظرتون در مورد ابوالفضل جلالی؟؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135265" target="_blank">📅 13:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135264">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86ba7ad723.mp4?token=CVsSgBRshaYigwdA8bljVxL5_6D3gjCNrX6uSoLJF5xfSXsZ0NO_kTbjHmCeqGHbCvazWZBy8GGR371-x_hROTwMiCINQ70eN142JPde-rdJEI8J3GTCe6hzAc38oFGaDtkgzy_kKef4T5L8enRlI9zFmqmuhsr59R7fHBrKclqyVpUll-XuKPwJhrDVxRe24YTGFMxIBake5cfRMdS7rsKMMVcPdcZFXJ9UVXyecqtFbNkXP9tkp2-aNdgbSBnXxBqGK4XlurHzC5X-_aEGrcHX0Z7sHbbTRg0omOwVBEgQapWiUYJF2X44U7AFKsLNGr02ieXvOmWu3a9HKwZI6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86ba7ad723.mp4?token=CVsSgBRshaYigwdA8bljVxL5_6D3gjCNrX6uSoLJF5xfSXsZ0NO_kTbjHmCeqGHbCvazWZBy8GGR371-x_hROTwMiCINQ70eN142JPde-rdJEI8J3GTCe6hzAc38oFGaDtkgzy_kKef4T5L8enRlI9zFmqmuhsr59R7fHBrKclqyVpUll-XuKPwJhrDVxRe24YTGFMxIBake5cfRMdS7rsKMMVcPdcZFXJ9UVXyecqtFbNkXP9tkp2-aNdgbSBnXxBqGK4XlurHzC5X-_aEGrcHX0Z7sHbbTRg0omOwVBEgQapWiUYJF2X44U7AFKsLNGr02ieXvOmWu3a9HKwZI6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گل پوریا شهرآبادی به استقلال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/135264" target="_blank">📅 13:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135263">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
پوریا شهرآبادی برای عقد قرارداد وارد ساختمان باشگاه پرسپولیس شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/135263" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135262">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/838edcfe33.mp4?token=kZoIcxQpzH19__PPVo_KRQI5zG6t3vYNzOwAkbruEnFt0-KKJAXnAXlGwk430U2IEDm27kLsg9gzJYzz2elcw-B8SlMNGTZENwKIMibGHac7H6G-gosWYdScWaT5atg3kUy6yXTRIYAxF39X4YfO6m2h-1wfJSiaBlQ-k8pzFcI1EKgW3hJcpnNOd6QQEWj-5HFTf6BZXAMQ4ZoB1Rs4n2oddV_fb1BcVl47j61cnDRrGufMZf5tmyYNDqCxF6mhpPiQVyoglrmlXl3EpeDu5GuUVMYIUbob8VcOTOn1qTLOuwwco6Wm5uz-3teF-tHHDszNHyuQV8CVhKXGZUAbtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/838edcfe33.mp4?token=kZoIcxQpzH19__PPVo_KRQI5zG6t3vYNzOwAkbruEnFt0-KKJAXnAXlGwk430U2IEDm27kLsg9gzJYzz2elcw-B8SlMNGTZENwKIMibGHac7H6G-gosWYdScWaT5atg3kUy6yXTRIYAxF39X4YfO6m2h-1wfJSiaBlQ-k8pzFcI1EKgW3hJcpnNOd6QQEWj-5HFTf6BZXAMQ4ZoB1Rs4n2oddV_fb1BcVl47j61cnDRrGufMZf5tmyYNDqCxF6mhpPiQVyoglrmlXl3EpeDu5GuUVMYIUbob8VcOTOn1qTLOuwwco6Wm5uz-3teF-tHHDszNHyuQV8CVhKXGZUAbtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پوریا شهرآبادی برای عقد قرارداد وارد ساختمان باشگاه پرسپولیس شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/135262" target="_blank">📅 13:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135261">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔹
فوری؛ابوالفضل‌جلالی مدافع‌سابق استقلال برای عقد قرارداد با باشگاه پرسپولیس وارد ساختمان این باشگاه شد. قرارداد 2+1 ساله توافق شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/135261" target="_blank">📅 13:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135260">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فرزین معامله گری خرید چهل میلیاردی خلیلی به خاطر تمدید محمدی و خرید جلالی در لیست مازاد تارتار قرار گرفت/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/135260" target="_blank">📅 13:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135258">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
ترامپ: ایران دروغگوعه و من از امروز به بعد دیگه نمی‌خوام هیچ ارتباطی باهاشون داشته باشم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/135258" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135257">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
فوری/ ترامپ: به نظر من، توافق‌نامه با ایران به پایان رسیده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/135257" target="_blank">📅 12:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135256">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❗️
فیفا به درخواست ترامپ، کارت قرمزی که مهاجم آمریکا، داخل بازی قبل گرفته بود رو بخشید تا محرومیت بازیکن تو بازی بعد جام جهانی رفع بشه!!
❗️
پ.ن سیاست آوردن تو فوتبال و ترس از آمریکا و ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135256" target="_blank">📅 12:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135255">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
اگر پرسپولیس همزمان مهدی زارع و مسعود محبی را جذب کند، پرونده انتقال علی نعمتی به‌طور کامل بسته خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/135255" target="_blank">📅 11:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135254">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
هوشنگ‌ سعادتی به مدیر پرسپولیس قول داده امروز جلالی رو ببره ساختمان باشگاه پرسپولیس برای عقد قرارداد؛ اگه باشگاه استقلال تا ساعات آینده با جلالی برای تمدید تماس نگیره امروز ازیاغی جدید فوتبال ایران رونمایی خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135254" target="_blank">📅 11:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135253">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
مصاحبه‌جدید دراگان‌اسکوچیچ: هرگز برای یک فصل حضور در پرسپولیس 3 میلیون دلار تقاضا نکرده بودم.
🔴
بایک‌ باشگاه‌ بزرگ در حال مذاکره هستم و ممکنه برای‌فصل‌جدید مجدد به لیگ برتر برگردم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135253" target="_blank">📅 10:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135252">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
یاگو به عنوان مربی بدنساز فصل آینده پرسپولیس انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/135252" target="_blank">📅 10:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135251">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
شوک بزرگ به استقلال؛ سایت آفریقایی Africafoot مراکش نوشت که مونیر الحدادی ستاره استقلال با باشگاه الاتحاد مراکش توافق کرده...
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/135251" target="_blank">📅 10:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135250">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⚡️
⚡️
آسانی و منیر حدادی در آستانه ترک ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/135250" target="_blank">📅 10:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135249">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
برای تمرین امروز چهارشنبه به بازیکنان  پرسپولیس اطلاع‌رسانی شده و در این بین به ۳ بازیکن دارای قرارداد، گفته شده که تا مشخص شدن وضعیت‌شان، در تمرین شرکت نکنند.
✅
امید عالیشاه، مرتضی پورعلی گنجی و میلاد سرلک این سه بازیکن هستند.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135249" target="_blank">📅 10:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135248">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❗️
امروز پرسپولیس روز شلوغی خواهد داشت...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/135248" target="_blank">📅 10:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135247">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❗️
اسکوچیچ: با پرسپولیس توافق کردم انواع و افسام انعطاف پذیری ها رو داشتم اما در آخر قراردادی که برای من فرستادن مبلغش خیلی کمتر از اون چیزی بود که توافق کرده بودیم و من از این موضوع بسیار ناراحت شدم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/135247" target="_blank">📅 09:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135246">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
❗️
باشگاه پرسپولیس خطاب به ابوالفضل جلالی: اگه قصدت بازار گرمی نیست بیا قرارداد باهات ببندیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/135246" target="_blank">📅 09:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135245">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❗️
فووووووووووووری
🚨
قدوسی: حضور علی نعمتی در پرسپولیس احتمالا منتفی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/135245" target="_blank">📅 09:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135244">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
برای تمرین امروز چهارشنبه به بازیکنان  پرسپولیس اطلاع‌رسانی شده و در این بین به ۳ بازیکن دارای قرارداد، گفته شده که تا مشخص شدن وضعیت‌شان، در تمرین شرکت نکنند.
✅
امید عالیشاه، مرتضی پورعلی گنجی و میلاد سرلک این سه بازیکن هستند.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/135244" target="_blank">📅 09:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135243">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGUh73hzqUXNiO6zIPoUspe-MqyBK5TeaASIj3VTi6POZxfK5CLpCdKUnIOentMZ-hcA12EELJmvS1GRX0upinEee1I-5Gl5D6QViSTcKZxq2UCcMSxqNuZXHu7upoxAUKrfvU_-5XufwjxAwa9yrQLvQcuNRiz-EvShI31f6Hfiw9ZCnP0CWeVYjCy9jbA-5DLDrGWdiFUmf7O74wrM_Ku0AYR_OFxouuxeCvyJY2b-XDRBU0TeG5DvlNN1sZPSXct0D_3ToXTKGP53HunyawfrpekZGJesTdwCKzZ6Q9JrOaRKZh4KDjAbZj9XNC9p-cI4riiFriiV4YI-CQ2MvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برای تمرین امروز چهارشنبه به بازیکنان  پرسپولیس اطلاع‌رسانی شده و در این بین به ۳ بازیکن دارای قرارداد، گفته شده که تا مشخص شدن وضعیت‌شان، در تمرین شرکت نکنند
.
✅
امید عالیشاه، مرتضی پورعلی گنجی و میلاد سرلک این سه بازیکن هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/135243" target="_blank">📅 09:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135242">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✅
نمودار درختی دور یک چهارم؛
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/135242" target="_blank">📅 09:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135241">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135241" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر پنجشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
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
https://t.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/135241" target="_blank">📅 01:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135240">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVywQJpfY5F74Z65vcC51-_58ak8JXm-EDsq71QbkvclXRntMnbgupmvD6gUAN0iaybcIyyeR27ZogGYFqd7UKd8H_4rZ732YXSyccGNHXFN2VXm7SwwDUR5Ek9RVNictiZ5jfInQxESiAVFR8pmOEhRGlMww0McXaLBzLXbRkKk-0ZEkzdmzMXuvs_HUFMBVGbfCkOYXb8sd_zu9Ib-HcHquFjdyxjikRp5D7av49uioHWCsjhx1RHmJQ58jJXmrmUZaT6YPke5n0sSA_RvyhnYFRG8tW2AbtHVyePKww0ss7aBChYnzSkBXOTO5OA0-UnC0ozjhxxUBlv_F67Kfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین سایت جهانی برای کاربران ایران با واریز برداشت مستقیم
⬇️
🪙
سایت بین المللی و معتبر لاین
بت
❤️‍🔥
اسپانسر لیگ  فرانسه
💳
واریز و برداشت ریالی
👀
بازگشت باخت ب صورت هفتگی
📣
دارای پشتیبانی فارسی فعال
🎁
بونوس
💯
روز های دوشنبه
🎡
کدهدیه ثبت نام
➡️
L5670
🔗
《 لینک سایت برای کاربران ایرانی》
👍
《 دانلود اپلیکیشن اندروید》
❤️
https://t.me/+dukgrB6-zGsyNGM8
🔻
جهت استفاده از وبسایت از آی پی کشورهای آسیایی
🇷🇺
یا کانادا
🇨🇦
، استفاده کنید
Ⓜ️
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/135240" target="_blank">📅 01:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135239">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❗️
فوووووووری/سنتکام: در پاسخ هم حملات ایران به کشتی‌های تجاری و نقض آتش بس، مناطقی در جنوب ایران را بمباران کردیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/135239" target="_blank">📅 01:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135238">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
✅
فوووووری؛ آغاز عملیات شبانه ارتش آمریکا در جزایر جنوبی ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135238" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135237">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
❗️
فوووووووری/ارتش آمریکا در پاسخ به نقض آتش بس از سوی ایران، اهدافی را در جنوب ایران هدف قرار داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/135237" target="_blank">📅 00:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135236">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
حسام حسن، سرمربی تیم ملی مصر پس از حذف در بازی با آرژانتین با ادبیاتی تند گفت:
🎙
هر عواقبی را می‌پذیرم اما می‌گویم که این مسابقه کاملاً مهندسی و تبانی‌شده بود و همه دنیا این را دیدند. اگر تا این حد اصرار دارند که آرژانتین قهرمان شود، چرا از بقیه تیم‌ها…</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/135236" target="_blank">📅 00:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135235">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
🔴
به امید عالیشاه، میلاد سرلک و مرتضی پورعلی‌گنجی اعلام شده در تمرینات حاضر نشوند و در لیست مازاد قرار گرفتند.
🔴
🔴
باشگاه همچنین به سروش رفیعی اطلاع داده قصد تمدید قراردادش را ندارد.
🔴
🔴
تارتار هم گفته هفته آینده درباره ادامه همکاری با بیفوما تصمیم نهایی…</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/135235" target="_blank">📅 00:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135233">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
❗️
وای چیه این فوتبال ..از دقیقه 80 تا 90 آرژانتین سه گل زد و بازی سه بر دو جلو افتاد ..برگام ...جونم به این فوتبال جذاب ..مسی موند تو جام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/135233" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135232">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❗️
با جدایی اوسمار ویه را و حضور تارتار فرزین معامله گری در پرسپولیس ماندنی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/135232" target="_blank">📅 22:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135231">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
دراگان اسکوچیچ:
❌
چون اجازه دخالت در نقل‌ و انتقالات را به مدیریت ندادم حضورم در پرسپولیس منتفی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/135231" target="_blank">📅 22:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135230">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
❗️
فرهیختگان: علی علیپور برای تمدید قرارداد با پرسپولیس کمی فرصت خواسته تا پیشنهادات حوزه خلیج فارس‌ اش را بررسی کند سپس پاسخ نهایی را به باشگاه بدهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/135230" target="_blank">📅 22:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135229">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✅
✅
محمد گندمی ؛ سهیل صحرایی، فرزین معامله گری ، علیرضا همایی فرد و کسری طاهری از پرسپولیس به تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/135229" target="_blank">📅 22:32 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
