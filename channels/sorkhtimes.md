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
<img src="https://cdn4.telesco.pe/file/Znc5Ez7D2EcnZAIT-wOU_XmllE09aud7leeRyX1G2ADfrJ74XK5LmAK5uDiFFcyjFKsKFl6P7fKfdi9-2nm6D7zQ6qr9BwnL-GuForAMJnacC_Wz9HkS9iYfUD7rWJVlZI1lcyYEyy42HCtIf3nsPkzsDuHe68pMmhHRyGbleruSzFl7IeHz64fJcwUtq4pVTtrBet8wiOSiUoD77YGZ00w3IaeaD2wzBp1qc2MZxSxAo0FgZpQFONwoH30IPmmI-SW0OWGkBXa4waZ6Tv6G32deIMN8V4950g9pPF6cxT3QGZbg6xNTSnyhnSEQgfGchih1NVfBZEqxMfxjBcuD8Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 16:18:20</div>
<hr>

<div class="tg-post" id="msg-135846">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❗️
پنج کاپیتان پرسپولیس در فصل پیش رو مشخص شدند
⏺
1_علی علیپور
⏺
2 _حسین کنعانی زادگان
⏺
3_محمد عمری
⏺
4– محمد خدابنده لو
⏺
5_اوستن اورنوف
🔴
پ.ن: در صورتی که وحید امیری به پرسپولیس اضافه شه، احتمالا کاپیتان اول تیم میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SorkhTimes/135846" target="_blank">📅 15:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135845">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
محسن خلیلی سرپرست پرسپولیس: برای جذب کسری طاهری باید 200 میلیارد خرج می کردیم که به این نتیجه رسیدیم که قید این بازیکن را بزنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SorkhTimes/135845" target="_blank">📅 14:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135844">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
افشاگری جنجالی رسانه عادل فردوسی‌پور از امیرقلعه‌نویی: سرمربی تیم‌ملی قبل از بازی با نیوزیلند تهدید به استعفا کرده و فدراسیون با پرداخت ۱۴۰ میلیارد تومان پاداش به این سرمربی در یک بانک‌خصوصی، قلعه‌نویی رو راضی به ادامه حضور در جام‌جهانی کرده! حالا هیئت رئیسه…</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SorkhTimes/135844" target="_blank">📅 14:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135843">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135843" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SorkhTimes/135843" target="_blank">📅 14:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135842">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XMOvsN5W-vMlOvOqbi9NRdVQndFZMv1ogg-lHT-aIDKXk3Qb9Q59BgUuWhLktxtRXnppw1ltbUV-OCxRkX9vdXy3lobrLUugrxZtw5pBkjn9PmerZs52WgeJOdZTITybMjlt1lFPKDCyS7ouu5g8QpGSGju_hlcamaiddNEheYyIlnb7SRj91G8YhmvpcAHwrLez_-fhtBM2K6bM0TM2lzvVe5U8HsOqAmU-yHf3byWzlcQy8xqfA_I73ueug2X0PYNQ783xl_ZTHskM4Zg7opQutUlBREM-gcOArxyvCNfSDoPLBUjtJCLX5blJ3UoYXWKxSuPDr7DDM2jwEKHxLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی فوووق جذاااااب
انگلیس
و
آرژانتین
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
▶️
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🌐
دانلود مستقیم اپلیکیشن اندروید
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
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SorkhTimes/135842" target="_blank">📅 14:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135841">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
#فوری
| ادعای اکسیوس:
🔴
🔴
ترامپ جلسه‌ای در «اتاق وضعیت» کاخ سفید برگزار کرد تا درباره یک تهاجم گسترده در ایران بحث کند
🔴
🔴
منابع می‌گوید که این حملات، دامنه‌ای فراتر از تهاجم‌های کنونی در اطراف تنگه هرمز خواهند داشت
❗️
❗️
جلسه مذکور بر طرح‌های جدید برای حملات به اهداف استراتژیک در ایران، متمرکز بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/135841" target="_blank">📅 14:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135840">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
🔴
با اعلام فدراسیون فوتبال، کمیته استیناف درخواست تجدیدنظر باشگاه پرسپولیس در پرونده علیرضا بیرانوند را رد کرد.
🔴
باشگاه پرسپولیس نسبت به رای کمیته وضعیت بازیکنان فدراسیون فوتبال که به موجب آن حکم به محکومیت به پرداخت مبلغ یک میلیارد و ۲۰۰ میلیون تومان داده شد، اعتراض کرده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/135840" target="_blank">📅 14:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135839">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
شوک به استقلال: آسانی فسخ کرد!
🔴
یاسر آسانی با ارسال نامه‌ای رسمی به باشگاه استقلال، به دلیل پرداخت نشدن مطالبات فصل گذشته و پیش‌پرداخت قرارداد فصل جدید، فسخ یک‌طرفه قرارداد خود را اعلام کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/135839" target="_blank">📅 14:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135838">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
شنیده ها: یاسین جرجانی، مهدی زارع و مسعود محبی سه گزینه جدید خط دفاعی پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/135838" target="_blank">📅 14:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135837">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tsb4Dg4CbhiaNdLJXyv1Xdy317AHHm4A4zXuOje2psjEkxVoX0vOPVDVCfrg-p9EtBZ3LtFLNEV6tCoTBZdvCS1Jyp9ga6fIwjJFLv6AW_r5YYmmQEiK_L9cy5C4LOkl133E1t8CzMm0LfZ15FYTI8DSNvnW_kTUVoc5PKRPwrUJm1wX24JMyLHIV1iVs91DLINw9aHDN1li5MjTWTH4HOZN2lucl8_NeKqtOY83LcRVbaP8G2duA5nbPmLlo_QC5FYSFodR-mtz1CojAKLDeZGiRIidaAeUa7hDhJ3VmyvKRwdUE9DROg_VmoEoqpZI-xZ7Iu9oA0trAC2uu9Ot7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شنیده ها: یاسین جرجانی، مهدی زارع و مسعود محبی سه گزینه جدید خط دفاعی پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/135837" target="_blank">📅 13:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135836">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
نظر و حرف دلتون و بگید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/135836" target="_blank">📅 12:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135834">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_zEi2Iw7sH5I9AaoLqa9JAes6MB9HhPniJYO2MC90uzY6SRUc0n7roSgBX7jmttbAMAKspFd2kqp0_G6wVHgF7T-w0vpfp6DX5Yn0lkO55kNgAVBeHOHo6aRNslM__QTxffdB34GXDUap7qbSMLaMUptuUnQaWjIqN93PU32slmDeEFSw7AndaGjYXVOC5-x_nzckNPZKYNv96QEn90OYuMMEqg51vjX9BKZGh3Vs91cUsE9oQa0jVRYbWyPAp34KTQL5vVd8EG_nDAIZkSm82eIbH1VcgCCZ_cs1DWgUVD1jxBWs5w8FI58kC8qQuswUE4ND9soSHhBN0ePy4VfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی
؛
بامخالفت‌تارتارسرمربی پرسپولیس جدایی محمد عمری وینگر سرخ ها از این‌ تیم منتفی شد. ضمن‌اینکه محمد عمری برای تمدید قراردادش با باشگاه به مدت سه فصل دیگر به توافق کامل رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/135834" target="_blank">📅 12:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135833">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
شنیده ها؛ گفته میشه علیرضا جهانبخش گفته تا یکشنبه به پیشنهاد پرسپولیس پاسخ میده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/135833" target="_blank">📅 12:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135832">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">◀️
جدول خاموشی مناطق مختلف تهران منتشر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/135832" target="_blank">📅 12:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135831">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMge7QhFwlDPHFXU4teTFBCBqB-w_Jh49oG2hT7YS7MP9D5iTcWLmI3kVsTHHa6fihTPPuu1gigBWBWzeaJbe71540VbTXeFrQ88lXyfpEZRhh3Y0SHdj4xSpneZWg4ZLXzZbWQeMY1Zzb-ddtnM0fDswGYMVe5JEFnX_YRpkgvAqFoW2zfi_kmP9u_2sat2s6YFEAh6NiaOpxWB3tnObVglQrZCKckVbLOx4GkINW-pCbg0BSJCARJaqPzFLDPDwJs0uanbqOpjb5s6AC0sbSwU3rvZuL3_5DgazY--9IsyA20CscfkqzkfDq5R4B3Wu0ujUSXUAR6eZt-2aL2-uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شنیده ها؛ گفته میشه علیرضا جهانبخش گفته تا یکشنبه به پیشنهاد پرسپولیس پاسخ میده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/135831" target="_blank">📅 12:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135830">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
✅
پرسپولیس برای برگزاری اردو پیش فصل جمعه هفته آینده به مدت یک هفته تا ده روز راهی ترکیه خواهد شد/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/135830" target="_blank">📅 11:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135829">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
فوری؛ با اعلام ترانسفرمارکت، علیرضا کوشکی از استقلال جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/135829" target="_blank">📅 10:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135828">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری از خبرورزشی
📊
📊
📊
علیرضا جهانبخش کاپیتان تیم ملی فوتبال، بمب نقل و انتقالات مدیران پرسپولیس و بانک شهر برای هواداران این تیم است!
⚽
⚽
⚽
⚽
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/135828" target="_blank">📅 10:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135827">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
مدیران باشگاه پرسپولیس روز گذشته جلسه ای برای چذب پوریا لطیفی فر با مدیران گل گهر سیرجان برگزار کردند و با این باشگاه به توافق رسیدند / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/135827" target="_blank">📅 10:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135826">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJAcPhprEWF0WaUqtRJbVGUTnQjSGEdiInVcToCDpJhhNiV_sieH2Y2UG85xltTtjXJEZ2K3qt7k36K3qnrru9MrNkySb5cEL930dLoDOScXj4nMPN_oFjtQRsrrHGELOOAF1A2NZjc5WbsCBUZrwOiyYEx5oOnG-2UqaIIyrIcns-QxjDahlSym2nHdYPV9Ny2zm23x0yxRaSHb5Jo1VcoovhyxeGBo05P6XsZePDv712q-cB54qCwxIRgjhMirwU32NdEyhgsREOITHZeTQ5rfODREymFrWPW32UO7g7bX0h9izQ050Ck0DLiXp3RdOqX5wRQQlEe68CeacARIxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
جدول خاموشی مناطق مختلف تهران منتشر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/135826" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135825">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
🏟️
ورزشگاه آزادی تا دی ماه در دسترس نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/135825" target="_blank">📅 10:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135824">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
چمن ورزشگاه آزادی جمع آوری شد. پس از پاکسازی زمین و ضد عفونی ‌کردن آن، تازه کار اصلی آغاز خواهد شد. یه چند ماهی نمیشه ازش استفاده کرد 1 سال گذشته و اینا فقط دارن بازسازی میکنن ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/135824" target="_blank">📅 10:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135823">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❗️
پایان بازی، برتری در دیدار دوستانه
🔴
پرسپولیس 3 _ 0 شهدای رزکان البرز
✅
عمری، تیکدری، میرشفیعیان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/135823" target="_blank">📅 10:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135822">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
❗️
فرهیختگان: مهدی تارتار با جدایی محمد عمری مخالفت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/135822" target="_blank">📅 09:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135821">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
بیژن مرتضوی، خواننده و آهنگساز ایرانی مقیم آمریکا، با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/135821" target="_blank">📅 09:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135820">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvat9KAHiZIDmZfKKw4_f_y_6g68jjZK3mR2PhRMOm86aIIg_Qusg7MamitvKufkBfnGVkEjZE_nXkr_JAMWrCe-cxd4qtTwCbCa1fCz0u7PA5fnU9r3mBerblSdDYCELAFNzRqriSxeiS-C6p2xGMXs8_NqodF2zr9_d4u1s09Au-O5DcdnYGigbRozKDll--7TDLZh8KFWDMY4GCLTMrSycx7NatMACiLmxqkT3LuHRSyCdY4rnwKxTNjysPTwtA-TGm0mElvlKISEcPVaeLQo5OjwsQaRpEB95fThX-4PwsiCdWb42GNEd5_JqVa7RW2UZbvmQS1puVe1A3m6pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری؛ با اعلام ترانسفرمارکت، علیرضا کوشکی از استقلال جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/135820" target="_blank">📅 09:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135819">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
متاسفانه طبق گزارشات، آسایشگاه سربازان در ایرانشهر با موشک زده شده است تعداد زیادی از سربازان وظیفه جونشونو از دست دادن و امار مجروحین هم بالاست
🔴
🔴
همچنین درخواست فوری از مرکز انتقال خون ایرانشهر برای اهدای خون در شهر بمپور برای مجروحین ثبت شده
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/135819" target="_blank">📅 09:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135818">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
ترامپ : امشب و فردا، ایران را با قدرت مورد حمله قرار خواهیم داد، توافق‌نامه همکاری با ایران یک آزمون بود، و ایران در انجام تعهدات خود در این توافق‌نامه شکست خورد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/135818" target="_blank">📅 09:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135817">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWEEe21caJHlh1c4_cG3i0z-1WiBvSx2Sp3KqTMkjqXsVYjeA6OcKGy7in0DRq9m2giCyVUiPenCNpoW066i9Q8WMCVVxq9c_S3SZtkI7h6NUiNpq8NCIzz60FL87d00XOa_Z4KBzvdgQwjBTZC2qeI0rUeDzT1G7FdZUkXQwFB-vCFh7iCVN-qRv_Gh14npQSXmidNE61kfrIuE2tJsY66aQG66Q-8RKP4PfVXSwv2rw_9-OjBYUFNLdgUWZZJpqNqvACkI3thSKov8dAnvizW0BiP8BHIoXjO7hnG-876tDqNW6ArWWZ6VL9KaCv4c_0PTUKOB1Z2tu_quuHnIag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صبح بخیر ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/135817" target="_blank">📅 09:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135816">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135816" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/135816" target="_blank">📅 03:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135815">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmUE52savUmbcvHSNKPH7_IHkmXHyhdzbZQfGroOWzaAoaJRlc3XM5ULQE0Ojx8jJ5upNa0TQXxQAtnB0IVMyZEpci97A9WujHUaqXjQrGZX6RZVX1f3wZxZlJ5OTlcCMTXD7AQIX2KpP-MA9LRyHeN0tLOWnn0iZ0SQDCXpxWvZch1efOeJn0Ai0lcC6Cn3g0QONZj7g_Srj6gqb2ORHUqcXdZUaIBbDD6uqS3iFbnw157DPLoZC9gin_3iPx7mpFg-LjMlLVqPv-B2ICBoQZ6J6IcYNaWgqzt9DS74RJZGfvDcvxmKTnus7KG4u3hNeEp47SJgIxLG8ds7W9iIhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/135815" target="_blank">📅 03:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135814">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❗️
❗️
فرانسوی ها ساکت هستند و حرفی برای گفتن ندارن تو گروه  پ.ن رفتن اسپانیا به فینال فقط با یک گل خورده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/135814" target="_blank">📅 00:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135813">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
✅
خداحافظی فرانسه با قهرمانی و رفتن به بازی رده بندی ...خداحافظ آقای امباپه ..سلام اسپانیا به فینال جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/135813" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135812">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
✅
جونم اسپانیا گل دوم هم زد و در آستانه رفتن به فیناله ..فرانسه در آستانه باخت و رفتن به بازی رده بندی ...کیا میگفتن فرانسه اسپانیا رو میخوره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/135812" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135811">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ak3RcH4capydcD88bMcSgwZ8Fn_hXC5Y-Y5h1_flVWolT5W6xiXY9ysehXbKmzIlaqM9u5VPSbgV9lLliNwy2DwhiCJuRN1zwAHdLQGVL2uZWx9S0X5FAG1FFtFCnftH7NjURkgdKRKLLZfJzqMkQU5x7qImImEiXblqIMeWxY7ZVhvsj0L3EvL_LGGa-XQ7XfkVRvp-TTfRVErtROR3GceTdJFt_R30zJn71J4g_jK351-zT16c6b_SOjdn-Yos1sWB67H_WgX1K2U5yUfQ_S_Lr0bwW__ThrOgwmjdv8NbG7OrVRXy72FU9SUAaR5ACkM24NAH6H4jdr74vcYaGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پست خداحافظی رضا شکاری با چاشنی ناراحتی: خداحافظی همیشه تلخ است، خداحافظی از گوهر کمیابی مثل پرسپولیس تلخ‌تر...
📍
موفق باشی
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/135811" target="_blank">📅 00:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135810">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری از خبرورزشی
📊
📊
📊
علیرضا جهانبخش کاپیتان تیم ملی فوتبال، بمب نقل و انتقالات مدیران پرسپولیس و بانک شهر برای هواداران این تیم است!
⚽
⚽
⚽
⚽
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135810" target="_blank">📅 00:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135809">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری از خبرورزشی
📊
📊
📊
علیرضا جهانبخش کاپیتان تیم ملی فوتبال، بمب نقل و انتقالات مدیران پرسپولیس و بانک شهر برای هواداران این تیم است!
⚽
⚽
⚽
⚽
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/135809" target="_blank">📅 00:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135808">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
افشاگری جنجالی رسانه عادل فردوسی‌پور از امیرقلعه‌نویی: سرمربی تیم‌ملی قبل از بازی با نیوزیلند تهدید به استعفا کرده و فدراسیون با پرداخت ۱۴۰ میلیارد تومان پاداش به این سرمربی در یک بانک‌خصوصی، قلعه‌نویی رو راضی به ادامه حضور در جام‌جهانی کرده! حالا هیئت رئیسه…</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/135808" target="_blank">📅 00:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135807">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❗️
❗️
#فوری | محاصره دریایی آمریکا علیه ایران از دقایقی قبل مجددا آغاز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/135807" target="_blank">📅 00:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135806">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
گل‌های پرسپولیس در دیدار تدارکاتی مقابل شهدای رزکان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/135806" target="_blank">📅 00:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135805">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✅
✅
جونم اسپانیا گل دوم هم زد و در آستانه رفتن به فیناله ..فرانسه در آستانه باخت و رفتن به بازی رده بندی ...کیا میگفتن فرانسه اسپانیا رو میخوره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/135805" target="_blank">📅 23:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135804">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
گل اول اسپانیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/135804" target="_blank">📅 23:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135803">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❗️
❗️
مرکز مشترک اطلاعات دریایی به رهبری نیروی دریایی آمریکا :  محاصره آمریکا شامل همه کشتی‌ها، بدون توجه به پرچم اون‌ها می‌شه
🔴
🔴
محاصره، کل سواحل ایران رو شامل می‌شه، از جمله بنادر و پایانه‌های نفتی ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/135803" target="_blank">📅 23:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135801">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
پیروز قربانی: من نیوزلند رو با فجر سپاسی شیراز می‌بردم مطمئن باشید نیوزلند اگه تو لیگ 16 تیمی ما بود، جزو چهار تیم آخر میشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135801" target="_blank">📅 23:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135800">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
ساعت 22/30 بازی حساس و دیدنی اسپانیا و فرانسه ...پیش بینی شما چیه ..کی می‌ره فینال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/135800" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135799">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
امشب ساعت 21
🔴
شنیده‌میشود؛ باشگاه‌پرسپولیس امشب از پوریا شهر آبادی و ابوالفضل جلالی دوخرید جدید خود در ویژه برنامه‌تلویزیون این‌باشگاه رونمایی خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/135799" target="_blank">📅 22:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135798">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✅
ساعت 22/30 بازی حساس و دیدنی اسپانیا و فرانسه ...پیش بینی شما چیه ..کی می‌ره فینال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135798" target="_blank">📅 21:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135797">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎥
ابوالفضل جلالی: وحید امیری خیلی به ما می‌تواند کمک کند
🔻
فعلا در تیم، هم‌پستی‌ام وحید امیری است!
🔻
آقا وحید یک بازیکن حرفه‌ای است و از لحاظ ادب حرف ندارد.
🔻
با وحید امیری، حسین کنعانی‌زادگان و محمد خدابنده‌لو در تیم صمیمی هستم.
🔻
بدن وحید امیری آماده است…</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/135797" target="_blank">📅 21:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135796">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6e06b7b2.mp4?token=lsZCTvcQ2BKf73UzloVwEP0HXsnn54QafBbb4AmXJBCl8HJ4EHF5oSRgA651BZMJjMtFGQGDgoT0kNwBZKi1tkH-Kn4dBssTEUUSg7zW8jsiC5k86PEE1r5g24P3tEaBsNURSeUckWwYSWGpqJCZB3fm0g1E1xsbPjqmar5r1cC9zQs_6aHp3uQ8TkZY6AlXEgAV0kbBFknSKd-hPIqkQWP4i12S41aUVX9DvNG6H-CMFpJZ_7NsiRP3OdLuNYAyTObUOrHanhpKCEUQ8RZYkLi1GM8THe27ItzATw7XUZJ7YO6WsVb5-qn1LXsxKLrDl_upUBGmQ1ugoMnXyY-i-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6e06b7b2.mp4?token=lsZCTvcQ2BKf73UzloVwEP0HXsnn54QafBbb4AmXJBCl8HJ4EHF5oSRgA651BZMJjMtFGQGDgoT0kNwBZKi1tkH-Kn4dBssTEUUSg7zW8jsiC5k86PEE1r5g24P3tEaBsNURSeUckWwYSWGpqJCZB3fm0g1E1xsbPjqmar5r1cC9zQs_6aHp3uQ8TkZY6AlXEgAV0kbBFknSKd-hPIqkQWP4i12S41aUVX9DvNG6H-CMFpJZ_7NsiRP3OdLuNYAyTObUOrHanhpKCEUQ8RZYkLi1GM8THe27ItzATw7XUZJ7YO6WsVb5-qn1LXsxKLrDl_upUBGmQ1ugoMnXyY-i-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ابوالفضل جلالی: وحید امیری خیلی به ما می‌تواند کمک کند
🔻
فعلا در تیم، هم‌پستی‌ام وحید امیری است!
🔻
آقا وحید یک بازیکن حرفه‌ای است و از لحاظ ادب حرف ندارد.
🔻
با وحید امیری، حسین کنعانی‌زادگان و محمد خدابنده‌لو در تیم صمیمی هستم.
🔻
بدن وحید امیری آماده است و او زودتر از ما سر تمرینات می‌آید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/135796" target="_blank">📅 21:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135795">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
جااااااااااان کیسه سوزی باشه؟
😂
✅
جلالی : دربی حذفی خیلی اذیت شدیم و گل عالیشاه خیلی قشنگ بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/135795" target="_blank">📅 21:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135794">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
ابوالفضل جلالی بازیکن پرسپولیس: با قلبم به باشگاه بزرگ پرسپولیس آمدم و این تیم را انتخاب کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/135794" target="_blank">📅 21:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135793">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❗️
❗️
خلیلی :
🔴
دیگر مهاجم جذب نمی‌کنیم و با سرگیف، شهرآبادی و علیپور ادامه خواهیم داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/135793" target="_blank">📅 21:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135792">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
محسن خلیلی سرپرست پرسپولیس: برای جذب کسری طاهری باید 200 میلیارد خرج می کردیم که به این نتیجه رسیدیم که قید این بازیکن را بزنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/135792" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135791">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4138202b6c.mp4?token=kJMFPW2JfuXHoQqul9g3vKhI2GYJJuCpTR1iIG70GienqE_foh4255yTzJiw0DiXN2kfZP2Xz1wrxP12fTA-p6_0pAZeo43P3QfObuo_V4MYVng4fzSUtpjVIHgAgveiUvlAB5hNz6P8TFj2WBkxwQgtHOTTVyEGUXrCWguodugh2MrJFWySWyZnwcOqABlzJzBzFn4IhPO2Ia8zDHnSlKgcKMTH04sLSeZXjTrYiPn_Gji1HoZpUt4msa4OfoMrHdmaTwvdQNG3k40LLBz5gatrJMDzBcKz6EGPG6ZLL4aplJQqq0XV9JUosjQM9j4bXvdWvl_OImrGL9T7orR-2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4138202b6c.mp4?token=kJMFPW2JfuXHoQqul9g3vKhI2GYJJuCpTR1iIG70GienqE_foh4255yTzJiw0DiXN2kfZP2Xz1wrxP12fTA-p6_0pAZeo43P3QfObuo_V4MYVng4fzSUtpjVIHgAgveiUvlAB5hNz6P8TFj2WBkxwQgtHOTTVyEGUXrCWguodugh2MrJFWySWyZnwcOqABlzJzBzFn4IhPO2Ia8zDHnSlKgcKMTH04sLSeZXjTrYiPn_Gji1HoZpUt4msa4OfoMrHdmaTwvdQNG3k40LLBz5gatrJMDzBcKz6EGPG6ZLL4aplJQqq0XV9JUosjQM9j4bXvdWvl_OImrGL9T7orR-2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوالفضل جلالی بازیکن پرسپولیس: با قلبم به باشگاه بزرگ پرسپولیس آمدم و این تیم را انتخاب کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/135791" target="_blank">📅 21:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135790">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e350a78f3.mp4?token=W1n3A0oQ4uUN2MBEDvdAArUdyrwglFEahUsVeKIjkcL5_j13ry9NbD6rMF2Aa1zDO2Oxb85Go_YemO76BYw0tUpoH3nAKuAUqgBKQK3Nt-qsj7iCPNigxvUl07b_gZ_eKSo7GndR1BYV34Rqdanv7RO4dDMUF38hcwFuH4vjYwns7c-RjC2g0PB413hpAWyFbkl9ntPLwj6V1bcXCP60YTXc4dF9HlYYFu3A2iLGN7b1JLzqhg4rAk4WGL7OzLgtWRfNf68CAkMGHiXtnL3TsumSF7bJrxoaRFtxUeUnb1wOFZ5u9YudaiPN2awiBQiMPHgj8ZBdHUZ6E0X6IALpwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e350a78f3.mp4?token=W1n3A0oQ4uUN2MBEDvdAArUdyrwglFEahUsVeKIjkcL5_j13ry9NbD6rMF2Aa1zDO2Oxb85Go_YemO76BYw0tUpoH3nAKuAUqgBKQK3Nt-qsj7iCPNigxvUl07b_gZ_eKSo7GndR1BYV34Rqdanv7RO4dDMUF38hcwFuH4vjYwns7c-RjC2g0PB413hpAWyFbkl9ntPLwj6V1bcXCP60YTXc4dF9HlYYFu3A2iLGN7b1JLzqhg4rAk4WGL7OzLgtWRfNf68CAkMGHiXtnL3TsumSF7bJrxoaRFtxUeUnb1wOFZ5u9YudaiPN2awiBQiMPHgj8ZBdHUZ6E0X6IALpwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوالفضل جلالی بازیکن پرسپولیس: امیدوارم امسال بتوانم دل هواداران پرسپولیس را شاد کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/135790" target="_blank">📅 21:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135789">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46267f8866.mp4?token=AkdGY8sDvDGOGnQq_7G3dR66tvC_3cgkcovEYKmlng2wy4b_4YN_U4RzryfFg02RWbilVJ5T-bNMiJTfopfQwha3bL23rzRguR-V67D7Cd2u2RMmuNYOhIe5FX-lt39b37r0uCidoBl-8_A13qDYeIJn4FeehAUzNPyN0kKbXsqBJU65YWC6-1IDWKZMVD0gwlc6I5TDfGUUD_rq9bhoTV0XFR3tdmJXCe0URCRiAmpYqEM5W6qbAOGwcDw4KKDaTaXfzYm9VjAxvyUpU8RrXLSm3hijpjBnTlg5Tr5Q0ZW_v-u3YQsKd53EMygAQ2skIYhw3ocjfkVHmpIaGALIgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46267f8866.mp4?token=AkdGY8sDvDGOGnQq_7G3dR66tvC_3cgkcovEYKmlng2wy4b_4YN_U4RzryfFg02RWbilVJ5T-bNMiJTfopfQwha3bL23rzRguR-V67D7Cd2u2RMmuNYOhIe5FX-lt39b37r0uCidoBl-8_A13qDYeIJn4FeehAUzNPyN0kKbXsqBJU65YWC6-1IDWKZMVD0gwlc6I5TDfGUUD_rq9bhoTV0XFR3tdmJXCe0URCRiAmpYqEM5W6qbAOGwcDw4KKDaTaXfzYm9VjAxvyUpU8RrXLSm3hijpjBnTlg5Tr5Q0ZW_v-u3YQsKd53EMygAQ2skIYhw3ocjfkVHmpIaGALIgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محسن خلیلی سرپرست پرسپولیس: برای جذب کسری طاهری باید 200 میلیارد خرج می کردیم که به این نتیجه رسیدیم که قید این بازیکن را بزنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/135789" target="_blank">📅 21:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135788">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
شوک به استقلال: آسانی فسخ کرد!
🔴
یاسر آسانی با ارسال نامه‌ای رسمی به باشگاه استقلال، به دلیل پرداخت نشدن مطالبات فصل گذشته و پیش‌پرداخت قرارداد فصل جدید، فسخ یک‌طرفه قرارداد خود را اعلام کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/135788" target="_blank">📅 21:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135787">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
یاسر آسانی قرارداد شو با استقلال فسخ و ایران رو ترک کرد / فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/135787" target="_blank">📅 21:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135786">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
✅
خلیلی: ما اصلا کسری طاهری رو نمیخواستیم و از لیست خریدمون خیلی وقته خارج شده
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/135786" target="_blank">📅 21:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135785">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
محسن خلیلی با کسری طاهری تماس گرفته تا در تمرین امروز پرسپولیس شرکت کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/135785" target="_blank">📅 21:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135784">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
بیفوما به‌خاطر کشیدگی کشاله هنوز تمرین نمی‌کنه. بعد از اینکه برگرده، تارتار کیفیتش رو بررسی می‌کنه و اگه راضی نباشه، توی لیست فروش قرار می‌گیره.
✍
خبرگزاری آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/135784" target="_blank">📅 21:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135783">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✅
#تسنیم؛ پرسپولیس سفت و سخت افتاده دنبال علی نعمتی و میخواد با یه جلسه حضوری کارو تموم کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/135783" target="_blank">📅 21:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135782">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗️
❗️
برگام
😐
🚨
علی نعمتی هنوز با لوسیل امضا نکرده و پرسپولیس زنگ زده بهش تا بره مذاکره حضوری کنن/تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/135782" target="_blank">📅 21:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135781">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
به خیر گذشت
🔴
فوری:علی نعمتی راهی قطر شد!
🇶🇦
✅
علی نعمتی، مدافع فولاد، با امضای قراردادی به لوسیل قطر، تیم تازه‌صعودکرده به لیگ ستارگان، پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/135781" target="_blank">📅 21:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135780">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
فارس؛ پویا لطیفی‌فر هافبک گل‌گهر در لیست خرید تارتار قرار گرفت
😐
❌
پ.ن از گل گهر بکشید بیرون ناموسا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/135780" target="_blank">📅 20:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135779">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❗️
فارس؛ پویا لطیفی‌فر هافبک گل‌گهر در لیست خرید تارتار قرار گرفت
😐
❌
پ.ن از گل گهر بکشید بیرون ناموسا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/135779" target="_blank">📅 20:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135778">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❗️
فارس؛ پویا لطیفی‌فر هافبک گل‌گهر در لیست خرید تارتار قرار گرفت
😐
❌
پ.ن از گل گهر بکشید بیرون ناموسا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/135778" target="_blank">📅 19:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135777">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_JLfwdw_azPKeoHH-cIMQ2mPZGhfCvdI5z-cX_I31akpoNNkym0SGCroz5Kis9xSMrSeggYMBukQHhZ2jTa8mRv0Y_3L5PyK0t6uUvE48VxDcetSfPIO66iLjO3LWBSmiQctAhY0g4oznGtaWcT8m4hJLATusnYxZYQx0oHwlxpFqYx_j1Bq7UH3u6t3CVk21GIT7-eeDnXF7sF22VXpzm51-EItM6kyP3YWYZd7zzL_fEsYu8L0upI9qZ4XRhnLco3yQ6wXDuzErv_UBWXancO5ooHArPcO3LQiJfmlC2eBz-VXx6ZV1b1Krf5YKQ1ctWzCaGDFQ0HJhKam4EK4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
فارس؛ پویا لطیفی‌فر هافبک گل‌گهر در لیست خرید تارتار قرار گرفت
😐
❌
پ.ن از گل گهر بکشید بیرون ناموسا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/135777" target="_blank">📅 19:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135776">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join
Join Join Join</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/135776" target="_blank">📅 19:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135775">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNELrtinQ3aJCnMFaYZCFElo_IPrx2AZVa0D0IPaPvIpzUfwpwF1JNtywCJaPTsy-8TlqeX7icDYomjoMOCiRos6Rc5wjWSHhOTK6J-tl5EwWtp-SgH_jNpxEcsej15XYLU2Pd8o8uEln0OHA3qV8Q5nLDI3vfmaMzXC0oBb4A0TJ4LTpk5vY_wtUq11K3Q7AtNbsdAKyflNJt7kRwLzFRWOkS8QEDwlb3VH5QOAY8Ec8JWqtzoPvR6JLyFlgIn5AyexqRKHmAjKfiS9lovFzTakcwAiLQ3zx1IoaeQ-fAoyk6Mgvk3ianDCGgkRh1gjbYkMnGVcsQlTYJeXNMceYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکسمون عالی برد شد
✅
💵
✈️
@Bet_Giantss</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/135775" target="_blank">📅 19:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135773">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb37226cd2.mp4?token=lQktv79w_bd8DnXOg2quMh1CUWlTp8JpgxcAA8bPkH83jowthftDLhAd1zDQcrGFq57VjHkKVcsDuoW8z9WpBKbiKzz-uyXEw-DhLH1OL5s3YF5BlkFcQqwd94Jtfc9Tda-yhLf1dn8ae1HObsMZ0JY6FK2mqVUf1gOPZDCOcmEUlFwCNfvida475KBmSD7bztsXxfFFgrD0gOVfFtA304R-5dfJPVldq0m1xOcCCBsRmxkwGIA7mp3ygEPva0bRcWEDSMAqAvQfqm6gawbt6MT8gi4JkZ_U_i0qj2e-MbKXkRzV5BOr3CsyWk0z4qvLg6AFGlr1mUjQmIyhhXi2B1IWIGuk6H6qOzFMkecRBZt6r-16HgcKZfCo7ofQZfs4JNpmkgSBYdBp_ebt5Lh6nnFel13IXgKNVxDDDQ9I8GfzNFcKL4CF9x8x6GVtOepXVu4YkyAQgd6EHgt3o-Ju6YO2CW5W1Aen_HihZMCVQqTvyTWpHaoLDu21xuNkkBKStR2FmF7onbb77xqfiCAnaOENUjYyxnyBKxTtbEjeholYuqqeIKK_yiSUqjIgZtnqHEZSc4RAs9EXpgM-_asIo9sXxbYUZ8QOLQ2656ohQTnW7fgG9Fe45SyCVDLx3bYCSq82y9OONEforliN6bWFdtWqGD7ku9KUv64yoRvQnUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb37226cd2.mp4?token=lQktv79w_bd8DnXOg2quMh1CUWlTp8JpgxcAA8bPkH83jowthftDLhAd1zDQcrGFq57VjHkKVcsDuoW8z9WpBKbiKzz-uyXEw-DhLH1OL5s3YF5BlkFcQqwd94Jtfc9Tda-yhLf1dn8ae1HObsMZ0JY6FK2mqVUf1gOPZDCOcmEUlFwCNfvida475KBmSD7bztsXxfFFgrD0gOVfFtA304R-5dfJPVldq0m1xOcCCBsRmxkwGIA7mp3ygEPva0bRcWEDSMAqAvQfqm6gawbt6MT8gi4JkZ_U_i0qj2e-MbKXkRzV5BOr3CsyWk0z4qvLg6AFGlr1mUjQmIyhhXi2B1IWIGuk6H6qOzFMkecRBZt6r-16HgcKZfCo7ofQZfs4JNpmkgSBYdBp_ebt5Lh6nnFel13IXgKNVxDDDQ9I8GfzNFcKL4CF9x8x6GVtOepXVu4YkyAQgd6EHgt3o-Ju6YO2CW5W1Aen_HihZMCVQqTvyTWpHaoLDu21xuNkkBKStR2FmF7onbb77xqfiCAnaOENUjYyxnyBKxTtbEjeholYuqqeIKK_yiSUqjIgZtnqHEZSc4RAs9EXpgM-_asIo9sXxbYUZ8QOLQ2656ohQTnW7fgG9Fe45SyCVDLx3bYCSq82y9OONEforliN6bWFdtWqGD7ku9KUv64yoRvQnUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
شهاب زندی: برای فروش ایری قرار است هیات مدیره تصمیم بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/135773" target="_blank">📅 18:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135772">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
میلاد محمدی همچنان تمدید نکرده و اخبار قطعی شدنش کذبه اما توافق داشته/ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/135772" target="_blank">📅 18:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135771">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
پاسخ چمران به سوالی درباره قطعی برق بدون اطلاع قبلی: اگر می‌دانستید دو روز پیش چه تعداد تاسیسات برقی را زدند دیگر این سوال را نمی‌کردید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/135771" target="_blank">📅 18:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135770">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccta__a9b7MB3rpTQx8YdVQ5t_oL7HtpwWZMawyAbp9rxTElNQLRlvNfGq27tAqcvp4SVl7s_fisq519jqXY9bz8IONoI-SvZqlYsj_9pAD_vA2-hEHv9BDA4izqdaT9mEMcsedKfQKp721OV1qftbdNT9uZmQ6OEiXL5K-TwS_--ja62xEeheDJQACAjQdghcRiJSuDQFmUvVe77LETQK_WKWU7PMcNMVV0QxLu1Hyzf7v14wydPhlHk5W63Z1XXnIw9UmDsXKLRLy1rIrNkRw8ksJZicXAl4xhbiuscg5vGDWZ9CtDSpaA6tmdv09qrsaRG8BHOnQ3p68x0-KTgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری
از خبرورزشی
📊
📊
📊
علیرضا جهانبخش کاپیتان تیم ملی فوتبال، بمب نقل و انتقالات مدیران پرسپولیس و بانک شهر برای هواداران این تیم است!
⚽
⚽
⚽
⚽
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/135770" target="_blank">📅 18:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135769">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de17a51b64.mp4?token=hGZmMWaZigD0uswl8Y8xomy8Ff04sMcypiWiAXrLWTl7tLDTYZXu3MWMeHYoS14uYCqF4rCNF-rQWyprxnBEaJMQNok36p43qG138wViHb4zMdxvj5lfv-LAuvnnVC9xHtsf-FCUL1gyHEE_IUvzeMf_SbBI_BCbqdi3OEFqP9GUxfnbOlr2zxVOlMTto6p8e60hMOIFJZ9KrRVZcrgCipvZu5BuL6FDOJeEk3PjW7Y7xoYKoCmTPiguzEPx8mNg7c3ZCbL8W4-iEFgmGMWJO7KCQOBOYwLBzlQl4rJqWbscAPmgDE6aeJpUMwqvoR0uXxEqpQEBMMyw9sBrKePmtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de17a51b64.mp4?token=hGZmMWaZigD0uswl8Y8xomy8Ff04sMcypiWiAXrLWTl7tLDTYZXu3MWMeHYoS14uYCqF4rCNF-rQWyprxnBEaJMQNok36p43qG138wViHb4zMdxvj5lfv-LAuvnnVC9xHtsf-FCUL1gyHEE_IUvzeMf_SbBI_BCbqdi3OEFqP9GUxfnbOlr2zxVOlMTto6p8e60hMOIFJZ9KrRVZcrgCipvZu5BuL6FDOJeEk3PjW7Y7xoYKoCmTPiguzEPx8mNg7c3ZCbL8W4-iEFgmGMWJO7KCQOBOYwLBzlQl4rJqWbscAPmgDE6aeJpUMwqvoR0uXxEqpQEBMMyw9sBrKePmtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بیژن طاهری، سرپرست کیسه، بعد اینکه یاسر آسانی به فرودگاه رفته و ایران رو ترک کرده، رفته راننده رو مثل سگ کتک زده و گفته چرا بدون هماهنگی باشگاه بازیکن رو بردی فرودگاه!
😳
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/135769" target="_blank">📅 18:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135768">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❗️
شایعات؛ جهانبخش عصر امروز با مدیرای پرسپولیس جلسه داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135768" target="_blank">📅 17:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135767">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
ادعای فرهیختگان: محمد عمری از لیگ قطر و امارات پیشنهاد داره و ممکنه باشگاه با دریافت ۶۰۰ هزار دلار از این تیم‌ها رضایت‌نامه عمری رو صادر کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/135767" target="_blank">📅 16:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135766">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❗️
فووووووووووووری
✅
قرارداد برای میلاد محمدی ارسال شده و تا ساعات آینده ممکنه اعلام بشه/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/135766" target="_blank">📅 16:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135765">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b882d31c48.mp4?token=JmpmykJKTzu_eR_cYr3MJEEJI2IkEL0TFkjusUk90trGJZMKuQitDLSYQdpomnVuPPuFC862Rk5xWVNCz-GC0ewiikah-yfMSUqrv1FO2XNMzbEROjG7XP1RtiQRZXTAA_yVZhxuOqE4Xl0OaYdkm4Bj-N1HG_WcK2LLhcRg-WAHF5Nq8BU9o_Z4QMJsGK2T1m31jlvF55cRr0pRstYfdgr45Drn62Azhn3FZKqzxoFwBPOm_EsLV9Y_AmDSBpnIoJkw4Fi7zAZ3Ye0jFs8_4ucNtEadXGPjtxl4akued_AV7YHCm-fJqwxPy7WpbfSrVQW5W8-m9zft_ff2MRdWYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b882d31c48.mp4?token=JmpmykJKTzu_eR_cYr3MJEEJI2IkEL0TFkjusUk90trGJZMKuQitDLSYQdpomnVuPPuFC862Rk5xWVNCz-GC0ewiikah-yfMSUqrv1FO2XNMzbEROjG7XP1RtiQRZXTAA_yVZhxuOqE4Xl0OaYdkm4Bj-N1HG_WcK2LLhcRg-WAHF5Nq8BU9o_Z4QMJsGK2T1m31jlvF55cRr0pRstYfdgr45Drn62Azhn3FZKqzxoFwBPOm_EsLV9Y_AmDSBpnIoJkw4Fi7zAZ3Ye0jFs8_4ucNtEadXGPjtxl4akued_AV7YHCm-fJqwxPy7WpbfSrVQW5W8-m9zft_ff2MRdWYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
این چیه برا نیمه نهایی ساختین آخه ناموسا
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/135765" target="_blank">📅 16:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135764">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❗️
❗️
#منهای‌پرسپولیس
🔹
سینا اسدبیگی و محمدرضا سلیمانی با عقد قراردادی یکساله به دهوک عراق پیوستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/135764" target="_blank">📅 16:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135763">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9eXXATciAUP6zIH7sYeEUqTHQQsw1qbuTTJQgDdbq9wNRJFTh_POlsmmQzmXtAeOJ-5ukapymogZLgxv-KfQQ5cCs27c3pYu8pMg0WpTcpzOq6XinlI_zse-fNem0BR0WixKq85ZjiaHckSee8n-y97JavPiQiXBGVj0gUkM0PPjdFLQFqiXNgM8GhxfUwey3iq9mpZt1cQ4ddphdP7zAQDtVDPzgXSPqbiDJwjaW0RnyE9FJICJR_1oDDVW5mcwSrQnSkMtZAkh6D6b1PbDcK5LgxtG-sKGLypm1WLhh8y82vRmpn8QpLas25VlwXGMwQ2xZwWc524vTCFbrGX6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیروز تو بازی دوستانه امیررضا رفیعی بازی نکرده و گندمی جوون نیمه دوم به میدون رفته
🔴
به نظر جدایی رفیعی قطعی شده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/135763" target="_blank">📅 16:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135762">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔹
عضو هیات مدیره باشگاه پرسپولیس استعفا داد
🔴
علیرضا اردوبادی عضو هیات مدیره باشگاه پرسپولیس، از سمت خود کناره گیری کرد.
🔴
علیرضا اردوبادی در ۱۸ آبان ۱۴۰۴ به عنوان جانشین سیامک جلوه به عنوان عضو جدید هیات مدیره باشگاه پرسپولیس انتخاب شد و بعد از اینکه پیمان…</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/135762" target="_blank">📅 16:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135761">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔹
عضو هیات مدیره باشگاه پرسپولیس استعفا داد
🔴
علیرضا اردوبادی عضو هیات مدیره باشگاه پرسپولیس، از سمت خود کناره گیری کرد.
🔴
علیرضا اردوبادی در ۱۸ آبان ۱۴۰۴ به عنوان جانشین سیامک جلوه به عنوان عضو جدید هیات مدیره باشگاه پرسپولیس انتخاب شد و بعد از اینکه پیمان حدادی به عنوان مدیرعامل باشگاه پرسپولیس معرفی گردید؛ از سوی باشگاه به عنوان رئیس هیات مدیره سرخ‌پوشان معرفی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/135761" target="_blank">📅 16:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135759">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
تسنیم : رضا جباری با مسئولان باشگاه پرسپولیس جلسه داشته که ؛دو طرف در این جلسه به توافق نهایی دست یافته‌اند و گفته می‌شود جباری به زودی در تمرینات پرسپولیس حضور پیدا می‌کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135759" target="_blank">📅 15:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135758">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
🎙
علیرضا جهانبخش: می‌دونم که بین پرسپولیس و استقلال لباس کدوم تیم رو می‌پوشم اما الان نمیگم. پدر و مادرم طرفدار یه تیم هستن و هرجا اونا بگن، میرم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/135758" target="_blank">📅 15:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135757">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
فوری :پرسپولیس برای جذب رضا غندی پور اقدام کرد /خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/135757" target="_blank">📅 15:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135756">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rA5tTQs1Y4Uudc0I-JTJoxW1P4hrVgfI2vfrxpwioMBJhoIIxfTM2-DocZ8WXxIEmNDiyVopVsWZ0dM4l6V0DflAc32W06pUGvsQibKHwG3kwpD1sUi6rZbgON2lSBfLTV2ovE6wQpaGfR7J8MFkZg8m0IncMsJ0WHWM6L_ruKpRa-gtBCcPyU7HhcO7cu_wJoUMBpNafYvJCFewn9GU6UjfI5tudS4Ki1dSPbqjxPIk84mLK9CBpNCLSqr1PDPdSLRasaxUnctk7qaYB6WsiJJ5vcs1DMy2Jqn-lI_2gecmLi6-7z6cnOGMquN7lcQdVvNnihwYxLYrDdJjdMGnWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
افشاگری جنجالی رسانه عادل فردوسی‌پور از امیرقلعه‌نویی: سرمربی تیم‌ملی قبل از بازی با نیوزیلند تهدید به استعفا کرده و فدراسیون با پرداخت ۱۴۰ میلیارد تومان پاداش به این سرمربی در یک بانک‌خصوصی، قلعه‌نویی رو راضی به ادامه حضور در جام‌جهانی کرده! حالا هیئت رئیسه فدراسیون از رفتار قلعه‌نویی حسابی شاکی شده و قصد داره این مربی رو برکنار کنه مگر اینکه تاج مانع بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/SorkhTimes/135756" target="_blank">📅 14:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135755">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🚨
📊
فووووووووووووری
🚨
قرارداد میلاد محمدی با پرسپولیس تمدید شد/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/135755" target="_blank">📅 14:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135754">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
ورزش سه :
🔴
بالاخره پرسپولیس و میلاد محمدی  روی برخی نقاط به اشتراک رسیده‌اند و به این ترتیب احتمال دارد در روزها و حتی شاید ساعات آینده قرارداد مدافع چپ ملی‌پوش پرسپولیس تمدید شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/135754" target="_blank">📅 14:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135753">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
تاخیر ۷ تا ۱۰ روزه لیگ ۲۶؛ فصل جدید فوتبال اواخر مرداد شروع می‌شود
🔴
🔴
براساس اعلام سازمان لیگ، در شرایطی که قرار بود فصل جدید لیگ برتر فوتبال از ۱۶ مرداد شروع شود، این مسابقات با تأخیر  یک هفته‌ تا ۱۰ روزه از ۲۶ یا ۲۷ مرداد شروع می‌شود. گفته می‌شود علت…</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/135753" target="_blank">📅 14:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135752">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IB9Z--U6D44CJdhqEc8MVhol56Vs1Tw7y6R6tjEFhiIUJFQtTIG8E85hD6HKxKe5kFLYs1cP0O273XLscOI-wl95QSVLUyJO2HR_flYmuffe9gknI7TBzGXKWJJnFQkytH0WoGY5IzXEyZLaNkylzngu57HKh3GMIOAZpgj1pBHRg6pRhrK5sDUHVG4lAT-Kk6HCsq1YFvTom3q2l-Js8pfoez16L5OQSgyuF4yjrOtS51LmGnYW5tgFCSvhUQ4mCuO7WXbnUZ-rlJHiADV5l0sX96mwp--kHQJyL9osbtNhNhVKgyW7Z0RbkTG3-2GciUzN5yKPS-RHGOdFCowo1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تمرین امروز سرخپوشان در سالن وزنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/135752" target="_blank">📅 14:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135751">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
میلاد محمدی نتونست تیمی از اروپا پیدا کنه و احتمال زیاد تمدید میکنه / طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/135751" target="_blank">📅 13:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135750">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🟡
علی کریمی با عقد قراردادی رسمی به سپاهان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/135750" target="_blank">📅 13:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135749">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
✅
فوری؛ با اعلام سازمان لیگ، برگزاری لیگ برتر در اواسط مردادماه لغو شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/135749" target="_blank">📅 13:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135748">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❗️
کسری طاهری مهاجم جدید نساجی: من اونشب تو شوک دعوای آقاخداداد باجواد خیابانی بودم که به یک‌باره‌رسانه‌ها خبر دادند که پیوستنم به پرسپولیس منتفی شده. بله از الان به بعد بازیکن نساجی هستم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/135748" target="_blank">📅 13:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135747">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✅
تایید شد بازم
🚨
🚨
🚨
فوووووووووووری :
🔴
کسرا طاهری: قراردادم با پرسپولیس فردا رسمی می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/135747" target="_blank">📅 12:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135746">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
💢
احتمالا علیرضا جهانبخش جانشین امید عالیشاه در پرسپولیس می شود!
🚨
جهانبخش جدا از عنوان یک بازیکن برای پرسپولیس قرار است سفیر تبلیغاتی بانک شهر هم باشه و پول خیلی خوبی قراره بگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/135746" target="_blank">📅 12:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135745">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
امشب ساعت 21
🔴
شنیده‌میشود؛ باشگاه‌پرسپولیس امشب از پوریا شهر آبادی و ابوالفضل جلالی دوخرید جدید خود در ویژه برنامه‌تلویزیون این‌باشگاه رونمایی خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/135745" target="_blank">📅 12:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135744">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kh9VOWYRtW6yqRodooUAro9Dmk8kbuO6vj7IaGUPfgiyBw1lQYdA40JUxTSpswuMWPHrmTiJg1EXl4jqKby2ZRK1oZnY_QjYAP-1ebR_lmH-eB8TN3StvNDnGZu0jHrMeD-8pvVjwn3Bg3OKcQMcGL4jn1bOMiRxrzVVFWf8HhvHXHdBwTpyzV2neWmaVEfs655zdyjaafr2lzZkDUi9dLxUphnYpWUJa1elmqRIYKWzyRJEqoo9UjaJL-2YnTAMiLRQOaFnKW62adGDMZxPFCt1DQfwrBKaUesQYfbKEmQduv_8yBWBnaUQ8mZZdCVKHUJ6CbeKiM4FnGUQkUAs-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/135744" target="_blank">📅 12:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135743">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✅
✅
جذب ایری برای پرسپولیس در یک صورت ممکنه که نساجی بدون دریافت یک ریال این بازیکن و به پرسپولیس قرض بده که احتمالش صفره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/135743" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
