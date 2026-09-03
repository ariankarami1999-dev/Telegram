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
<img src="https://cdn4.telesco.pe/file/HVHNnZVEfZwhBXFC_ykW-C95tQbmsa7EBoa4bG9tuNn_APwdDG2dmZLZ2wjt9la-4AKAUg_6jvi9VfyrNGLzb_4gja7JFUIo2sAdYQp5-_9o1jDq3Dp3lkgyRr_HMk8dAlzJFR2ee-ShVm1Y8eVY1oJXr94mJ457tMV_a4El1A8bbmXGGzjEYkmoihil4orZUjrYwifrMTUr49LpDK5ErMFzMdvrXRndeZqtEmzu1Rp3gKAY-KVZJ9o_GYwJqzaNbBdKaSZUwACAHgDCyUnc0OxM5fWW1zaLt_G2_q6cQvVIsyil0g92tCwra3bB2BOs6DrDUV7Hyl0O1_q6D9_fcw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 12:48:51</div>
<hr>

<div class="tg-post" id="msg-139476">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🤩
| فارس:
🔴
❤️
🔄
تارتار امید چندانی به دنیل گرا ندارد و حتی درصورت بهبود مصدومیت هم نیمکت نشین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SorkhTimes/139476" target="_blank">📅 10:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139475">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
باشگاه استقلال نسبت به عملکرد و سرعت بالای تیوی بیفوما مشکوک شده و احتمال می‌رود درخواست تست دوپینگ از این بازیکن پرسپولیس را مطرح کند.//هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/139475" target="_blank">📅 09:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139474">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
♨️
🗞
| #فوووری از تسنیم:
🔴
🔵
👤
پرسپولیس بخاطر استفاده از آسانی مستقیم به فیفا شکایت می‌خواد بکنه نه کمیته انضباطی
⚠️
❌
کمیته انضباطی فدراسیون شکایت های گذشته در مورد آسانی رو رد کرده بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/139474" target="_blank">📅 09:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139473">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✔️
✔️
عادل فردوسی‌پور: ترابی قطعاً ادامه فصل رو از دست میده، با خودش صحبت کردم و گفت دو پزشک بهش گفتن رباطش پاره شده و باید عمل کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/139473" target="_blank">📅 09:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139472">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✖️
✖️
هافبک و کلا استقلال برداشته و خیلی خالی هست هافبک ما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/139472" target="_blank">📅 09:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139471">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❤️
❤️
❤️
❤️
🔴
صبحی که دربی و مساوی کردیم و هنوز داریم حسرت تک به تک نزدن علیپور میکشیم بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/139471" target="_blank">📅 08:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139470">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsvU1A7tYkHdl9IMvFz-wS__-7ZtVjFXvFfcM0S3oQ_mZ3zFs1Ur9hv22rh_2wCc9FUr3QxEh9wFIGLsyo3XKYQV3KXUjAjsyzeIj0tQIpTsqdnFoo_t8QYgGCFDq3VPE_fidq5QhCLxrz6FKfnwZpF5nrsFhlnPJuTqS5Dzt0votnsa8TEcE5k8u2ySemEZewKDKEY0JCu1qRmLp39jWun8VDTPo5Ie3xGlnZKlbVbGSfgdsdpr8H6GLPEWuhX6pkM4XMWxjwds5m6MNJBisrDSmOKizyWguoheiFBedUCdqgdt8Vkr5ZzxLoBs9N4k9m-tz8b-vXs_1NqxS4Bj9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
دوئل‌های جذاب در یو‌اس اوپن!
🎾
جیمی فاریا
🆚
کارلوس آلکاراز
🎾
رِی ساکاموتو
🆚
فرانسیس تیافو
🟡
کدوم ستاره‌ها از این نبردهای حساس سربلند بیرون میان؟
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی دیدارهای یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
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
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/139470" target="_blank">📅 01:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139469">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/139469" target="_blank">📅 01:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139468">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⚽️
⚽️
استقلال و پرسپولیس امشب در مجموع 33 شوت بهم زدن که 9 تاش در چارچوب بود، برای درک بزرگی این عدد باید بهتون بگم که در مجموع دو دربی قبلی 33 شوت زده بودن که 10 تاش تو چارچوب بوده که یعنی امشب به تنهایی اندازه دوتا دربی قبلی روهم موقعیت دیدیم
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/139468" target="_blank">📅 00:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139467">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0X8LxkR-zoI7ukPi6zKc-wwRAHyC0nlCUMCrM8JFhuH88h-l7JEssXzmoNR8JMUj15W8i8JctUIDuNJ3tAkhiLK8ugpfd7tD0GXqiZZhficXWOYdFI09B4BHiLVxPfb7GwP9WEoyAB268vmKsw1GTo9tyUVACdxsfrEgPspkHA47pVKO_mwhcb1MtTl-dp9NWqfNVH1E68DvdS1Bng0puZy5zInDufcBFEDv67SsgE5mvXKORRP3cwXv2QfIsVwH3KWAspTeo2_jsG-UYzHAHLMuFzLM9ORLHmfnwBdcBYv3PkGhkVU04ocWH_5fyr9rzAJluH5NQaKH1-T6W25mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽️
استقلال و پرسپولیس امشب در مجموع 33 شوت بهم زدن که 9 تاش در چارچوب بود، برای درک بزرگی این عدد باید بهتون بگم که در مجموع دو دربی قبلی 33 شوت زده بودن که 10 تاش تو چارچوب بوده که یعنی امشب به تنهایی اندازه دوتا دربی قبلی روهم موقعیت دیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139467" target="_blank">📅 00:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139466">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
20 بازی بدون شکست
🔥
✔️
حسرت کیسه در آستانه ده سالگی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/139466" target="_blank">📅 00:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139464">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
فارس : نظر می‌رسد نظر کادرفنی پرسپولیس نسبت به ۲  بازیکن دانیل گرا و تیوی بیفوما  تغییر کرده و احتمال ماندن آنها در جمع سرخپوشان بسیار زیاد است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139464" target="_blank">📅 23:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139463">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnxzwnxYcDi_Mv46NEhUhI7YYY5jVi7WS4dYj9w8wKI_Jqi5chwkgScFxtL9RDK-maG46b1UIwAhLvFUJMzjhLC-AXBtVmKb4o2RzuefziYT5OTOP_z2gvx6dHS5ps88kNpCUJJBz-Qs4nK6jyw0P3DsQpMklOxdyn_E8DoLL9_H0zRmLkcEuZecUZUNrGn7pR8XyICQpA3UaBibBgFStgqiNodFDbvfUcmUBEOuVFoKLtg07oSFrdY0EzmudxpQyaW1X83e34D2utkFj2N6iAWnUVT4iZcYGPvDBJi03ZJbXzgXuRb0d-oR68fKtD5vBGsoVkEwImjp8G1JnEDdcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
پایان بازی | شکست ناپذیری پرسپولیس به ۹ سال رسید/دربی جذاب برنده‌نداشت  استقلال
1️⃣
-
1️⃣
پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139463" target="_blank">📅 23:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139462">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fc62967a0.mp4?token=r5p7xDrwRI3fTbBJxVQO7ohqatT_beZWnBLrtf9GQjJ93x9zfinjntWgmQUZAt8VJP5UmKwKwK_Ebt08lThs5sbt7P2vF_k3ECoosQdBJCy1u-67E68gTrM9yuZq_pTL8dr61dVAdtareQRSSXdUnVT3BAsWuAhKZOoSuGzsK8puTCnilGhMJfa0E_2oVPQAcvDYMFm0cM6dmvvfIUnrSdBj5dgb_TBdGDlQLK9qas2COCurHvYh_K4A8YVy0TQs24q-afxwRQaJMZWU7b79m1x1dQUy0hf26k6Bi6K4XfD1_C-OS_l9weMzdG-IULOaUPoQIxkLB-xNpKygVbKMaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fc62967a0.mp4?token=r5p7xDrwRI3fTbBJxVQO7ohqatT_beZWnBLrtf9GQjJ93x9zfinjntWgmQUZAt8VJP5UmKwKwK_Ebt08lThs5sbt7P2vF_k3ECoosQdBJCy1u-67E68gTrM9yuZq_pTL8dr61dVAdtareQRSSXdUnVT3BAsWuAhKZOoSuGzsK8puTCnilGhMJfa0E_2oVPQAcvDYMFm0cM6dmvvfIUnrSdBj5dgb_TBdGDlQLK9qas2COCurHvYh_K4A8YVy0TQs24q-afxwRQaJMZWU7b79m1x1dQUy0hf26k6Bi6K4XfD1_C-OS_l9weMzdG-IULOaUPoQIxkLB-xNpKygVbKMaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
بیفوما امشب دوباره یه استارت ۴٠ متری زد فرعباسی وحشت کرد دستپاچه توپو زد بیرون‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139462" target="_blank">📅 23:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139461">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
جدول لیگ بعد از هفته پنجم .اختلاف با صدر سه امتیاز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/139461" target="_blank">📅 23:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139460">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❤️
خدا بنده لو، بازیکن پرسپولیس:
⚪️
بیش از اندازه در مورد ارونوف حرف زده می شود. چیز خاصی اصلا وجود ندارد و هنوز خیلی از بازی ها باقی مانده است. او اصلا افت نکرده است و اصلا زیاد بازی نکرده که بخواهد افت کند. همه از کیفیت اورنوف خبر دارند و هر تصمیمی سرمربی…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139460" target="_blank">📅 23:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139459">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
کنعانی زادگان: تارتار تیم خیلی خوبی بسته است و امیدوارم آخر فصل قهرمان شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/139459" target="_blank">📅 23:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139458">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
کنعانی زادگان: تارتار تیم خیلی خوبی بسته است و امیدوارم آخر فصل قهرمان شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139458" target="_blank">📅 23:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139457">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❤️
❤️
❤️
ترکیب پرسپولیس برابر استقلال
🇮🇷
پیام نیازمند، مهدی زارع، حسین کنعانی، مهدی تیکدری، مجید عیدی، پویا پورعلی، محمد خدابنده‌لو، محمدمهدی محبی، تیوی بیفوما، ایگور سرگیف و علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139457" target="_blank">📅 22:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139456">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
✔️
هر دو گلر بد خوردن گلارو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139456" target="_blank">📅 22:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139455">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
مهدی تارتار: ما و استقلال خانه نداریم!
✔️
پرسپولیس و استقلال متضرر می‌شوند و ما خانه نداریم در شهرقدس از پتانسیل هواداری نمی‌توانیم استفاده کنیم.امیدوارم هر چه سریع‌تر استادیوم آزادی آماده شود.
✔️
اورونوف هم یکی از آن‌هاست هر کسی از هم‌پستی‌اش جلو بزند،…</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139455" target="_blank">📅 22:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139454">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
تارتار در نشست خبری: گروه داوری امروز خیلی خوب عمل کرد، خسته نباشید به آنها می گویم/ امروز هم پرسپولیس خوب بازی کرد و هم استقلال
✔️
✔️
به خاطر گل مساوی که خوردیم واقعا حسرت خوردیم
✔️
✔️
هم ما می توانستیم برنده بازی باشیم هم استقلال اما در مجموع ما یک مقدار…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/139454" target="_blank">📅 22:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139453">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👤
خدابنده لو، بازیکن پرسپولیس:
✔️
بازی بیرون خانه برای ما حساب شد‌. امیدوارم ورزشگاه آزادی زودتر درست شود. در مورد خودم نمی توانم اظهار نظر کنم. الان فضا بازتر است و امیدوارم ادامه دار باشد. دو تیم موقعیت های خوبی داشتند و آمده بودیم برای بردن اما حیف شد.‌شرایط…</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/139453" target="_blank">📅 22:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139452">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bebc6bdd.mp4?token=K0QbmmprOLReMEabQ9cniBP-p_xy38BQg7B9rfaunZ2yVva8Wi92WUS_ePlhfeAMVUPAcNrbZXHvXaXco4cuY-vsIz0r2FcDHlt4lGiSMRq6npl00Ne_X9VWVYhj5eGqOOjICvQgEHMdogURtaATnnuEsh-E0aRLzapIR7bWUKscF3GgVlZXSV8_PzhvQoieTLyyVX09x0WPUuqPHZmdnU6r0Uke7MNl1UjHM3-OrHMEaeiibMKCAH2pqnWN81w7Gx5qFy2dWyixHcVVV7zns_HTBJdSDLE3jK6MWkuzrADS2Wywu59nxogqmobZBJgixWPwvWrG5pq2B9uenmMHkzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bebc6bdd.mp4?token=K0QbmmprOLReMEabQ9cniBP-p_xy38BQg7B9rfaunZ2yVva8Wi92WUS_ePlhfeAMVUPAcNrbZXHvXaXco4cuY-vsIz0r2FcDHlt4lGiSMRq6npl00Ne_X9VWVYhj5eGqOOjICvQgEHMdogURtaATnnuEsh-E0aRLzapIR7bWUKscF3GgVlZXSV8_PzhvQoieTLyyVX09x0WPUuqPHZmdnU6r0Uke7MNl1UjHM3-OrHMEaeiibMKCAH2pqnWN81w7Gx5qFy2dWyixHcVVV7zns_HTBJdSDLE3jK6MWkuzrADS2Wywu59nxogqmobZBJgixWPwvWrG5pq2B9uenmMHkzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
خدابنده لو، بازیکن پرسپولیس:
✔️
بازی بیرون خانه برای ما حساب شد‌. امیدوارم ورزشگاه آزادی زودتر درست شود. در مورد خودم نمی توانم اظهار نظر کنم. الان فضا بازتر است و امیدوارم ادامه دار باشد. دو تیم موقعیت های خوبی داشتند و آمده بودیم برای بردن اما حیف شد.‌شرایط تیم خوب است و همه متحد هستیم. هواداران صبورتر باشند ما تغییرات زیاد داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/139452" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139451">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
✔️
✔️
مهدی تارتار : بازی زیبایی دیدیم/هم ما و هم استقلال میتونستیم برنده باشیم/از مسئولین اصفهانی و از داور تشکر میکنم/حسرت میخورم که نبردیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/139451" target="_blank">📅 22:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139450">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVH0btZVD_ifeEQv9lADHK4M_ZPnwo6DRp0akEXzvhQIluZZiBDQ7ch9gtlAdVharA67Eas90BSoTL5OQqDknInOzfta78Q60YC88ygK17GGP8m7gU7QTEa-jHQxj0C0Ihv4W1rm3xYfu2fb629IwtUIF7J_8YnQSDXE9fRgYwQPd6ZSJPeCPnmdyKiQQ76wSiB0LT5jZitdgtZLCrxK37OxLKAMpWVZXTHIVpad4I4RucRqWGH8r7XjG4xiVYSGC5bFwVpxk3QmDx79FKrrnH9C-fcrgJAFffr8srUwF-1yBSr8mhtDhFvQACVA2IFjzGfOcjeoODDfXgPX5jyYgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
جدول لیگ بعد از هفته پنجم .اختلاف با صدر سه امتیاز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139450" target="_blank">📅 22:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139449">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✔️
✔️
ترامپ: من استفاده از سلاح هسته‌ای علیه ایران را رد کرده‌ام/ ما دوست داریم با همه کنار بیاییم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139449" target="_blank">📅 22:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139448">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
🤩
🤩
خداییش یکی از بهترین داربی‌های چند وقت اخیر بود
✔️
داربی چهارشنبه‌شب نقش جهان، برخلاف پیش‌بینی‌های اولیه/ اطمینان وریا در مقایسه با سیدجلال، موقعیت‌های استقلال بیشتر بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139448" target="_blank">📅 22:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139447">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4d2d12ad.mp4?token=nFJiX2Ij31dcv4AsEg4XA5dAw8CbbTK-3x-kPidSHKQa2JC6O_DHY98AiW2D7Ly8Ma1ZxyQgvlXcxbgLbeJTXFOcdghR2P6ztPAuFwolrw6rLy-AT0by2BrQOBK5ETDmk7p4bpKGjmMs6t84KCFnC2oVLgswZmmElOGcuRTF1xQGbSHE5ruAvLCGpB-PZ6QGYdVjj6dYuUP4xuGt1p0SKesHv0onEH6r940MIIP5WcaXDclI7m0KHsYx9zx0QQWuAUmm-f5eM4ZLccD4qjzxUBF_oTinz8DRv1Fj6ky91je1mA3vQ1IXagNYStyijgv8BCRgOAPmQtqJztuEJDvkIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4d2d12ad.mp4?token=nFJiX2Ij31dcv4AsEg4XA5dAw8CbbTK-3x-kPidSHKQa2JC6O_DHY98AiW2D7Ly8Ma1ZxyQgvlXcxbgLbeJTXFOcdghR2P6ztPAuFwolrw6rLy-AT0by2BrQOBK5ETDmk7p4bpKGjmMs6t84KCFnC2oVLgswZmmElOGcuRTF1xQGbSHE5ruAvLCGpB-PZ6QGYdVjj6dYuUP4xuGt1p0SKesHv0onEH6r940MIIP5WcaXDclI7m0KHsYx9zx0QQWuAUmm-f5eM4ZLccD4qjzxUBF_oTinz8DRv1Fj6ky91je1mA3vQ1IXagNYStyijgv8BCRgOAPmQtqJztuEJDvkIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🤩
🤩
خداییش یکی از بهترین داربی‌های چند وقت اخیر بود
✔️
داربی چهارشنبه‌شب نقش جهان، برخلاف پیش‌بینی‌های اولیه/ اطمینان وریا در مقایسه با سیدجلال، موقعیت‌های استقلال بیشتر بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139447" target="_blank">📅 21:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139446">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6faf16beef.mp4?token=id7DoH54Nn_dPQ502EECykGbAdpND-COMNGfBuZfaF7qBLaezflrGvj5e9hfnYcC8SvjQzryNbGGK3YHrX3CirSLUE0wT7tDn5-3pSkGI_EJH2ZzXeX7v849wuiSUHUqh9JkU0rWJ3CI6umHJsLcIqwj-bBITP_zYTqpdTfeVph8zUySk_tFnUimSwPsfCeNpvq4nzbpUbw6anwwSVffwKciwtU7oV_FHqH2_tC5r_mol2L-QmhNe_9QoDgIQUqsNIn8i-RMPzlHLGcjiNyOEQYbSRVmi-WoD9pfLjl1eLLGDkE6eHY_PSkFTsE1oFv66vC7n2yu6HNiKSnzd_fO_jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6faf16beef.mp4?token=id7DoH54Nn_dPQ502EECykGbAdpND-COMNGfBuZfaF7qBLaezflrGvj5e9hfnYcC8SvjQzryNbGGK3YHrX3CirSLUE0wT7tDn5-3pSkGI_EJH2ZzXeX7v849wuiSUHUqh9JkU0rWJ3CI6umHJsLcIqwj-bBITP_zYTqpdTfeVph8zUySk_tFnUimSwPsfCeNpvq4nzbpUbw6anwwSVffwKciwtU7oV_FHqH2_tC5r_mol2L-QmhNe_9QoDgIQUqsNIn8i-RMPzlHLGcjiNyOEQYbSRVmi-WoD9pfLjl1eLLGDkE6eHY_PSkFTsE1oFv66vC7n2yu6HNiKSnzd_fO_jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
تشکر بازیکنان پرسپولیس و استقلال از هواداران‌شان پس‌از پایان داربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139446" target="_blank">📅 21:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139445">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🔱 Hero 🔱</strong></div>
<div class="tg-text">سر لجبازی ایشون سهمیه های فصل بعد ما هم به باد میره،نه با گرا فسخ کردن ،نه به ارونوف بازی میده نه باکیچ،هر کارشناسی هم حرف میزنه میگه ارونوف فاصله داره با ورژن خوب خودش،سوال من اینجاس ارونوف دقیقه ی ۸۰ به بعد اومده تو بازی چیکار بکنه تو کمتر از ده دقیقه؟؟؟ اونم دربی</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139445" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139444">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⬇
👤
آقای تارتار بازنگری بکن وسط زمین وله، چرا از باکیچ و لطیفی فر استفاده نمیکنی ؟! لطیفی فر هم بازیکن مستعدی هست هم قامت بلندی داره،مسئلت با خارجی هارو کی میخای تموم بکنی ؟ به چه قیمتی میخای اورنوف و باکیچ بازی ندی؟دقیقه ۷۵-۸۰ برای بازی دادن بازیکن جوان و تلنته…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139444" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139443">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPcuuYeuICSV1VxaR17GcxJWXaEoosg2LAdeTiqMH_JZDD8j54kf8v-O65c_ibMMpV6mMr8HgCytg4oPC2KdTaiiG0B0-x6OG_FmKGLk_BC5odNBaH21rkkQk113sTim5V5M_TxjMWw2G9dTtuxIsTF1GqXYU1sM0BY6ZZ2xhOkD-3TNbhiOsoI2EtbjUhh79JQAlDPU5VJT55Vu9J_DeGhj8h0NQZ0gjmoiYs69qy2UPlpvqKsRxVcd-z68tAmMtU8I9_C4WJM7gjwRxvkMKX-kBH0WoMXMuggn1ge24uys1meU8wkQou1dfu6S533cIMXDxOtvry6UhXkM6UdxMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
♨️
🗞
|
#فوووری
از تسنیم:
🔴
🔵
👤
پرسپولیس بخاطر استفاده از آسانی مستقیم به فیفا شکایت می‌خواد بکنه نه کمیته انضباطی
⚠️
❌
کمیته انضباطی فدراسیون شکایت های گذشته در مورد آسانی رو رد کرده بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139443" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139442">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
هر دو تیم و هر دو سرمربی به مساوی راضی بودن و خوشحال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/139442" target="_blank">📅 21:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139441">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🗣
🟥
بازی خیلی خوبی بود از هر دو تیم ولی بنظرم بعدا حسرت این امتیاز های از دست رفته رو میخوریم، تراکتور تیمی نیست که مثل بازی جلوی شمس آذر به راحتی مساوی بده و باید قدر این موقعیت هارو بدونیم، بنظرم راحت میتونستیم ببریم اگر تعویض ها زودتر انجام میشد و باز هم…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139441" target="_blank">📅 21:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139440">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🗣
🟥
بازی خیلی خوبی بود از هر دو تیم ولی بنظرم بعدا حسرت این امتیاز های از دست رفته رو میخوریم، تراکتور تیمی نیست که مثل بازی جلوی شمس آذر به راحتی مساوی بده و باید قدر این موقعیت هارو بدونیم، بنظرم راحت میتونستیم ببریم اگر تعویض ها زودتر انجام میشد و باز هم اگر وسط زمین رو داشتیم متاسفانه هم جلوی تراکتور هم استقلال وسط رو دادیم و همین باعث میشه دقایق حساس فشار سنگین بیاد روی تیم و بعدش با کوچک ترین اشتباهی باعث میشه گل بخوریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139440" target="_blank">📅 21:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139439">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-text">📌
وسط وله…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139439" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139438">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-text">📌
وسط وله…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139438" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139437">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-text">🔵
دربی تهران در نقش‌جهان اصفهان!
پرسپولیس
🔴
و
🔵
استقلال؛ در دیداری حساس و هیجانی از دقایقی دیگر در لیگ خلیج‌فارس ایران به مصاف یکدیگر می‌روند.
🔗
برای پیش‌بینی این دیدار حساس همین حالا وارد سایت معتبر اسپورت‌نود بشید و با بالاترین ضرایب پیش‌بینی کنید:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
مینی‌اپ رسمی اسپورت نود:
👇
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/SorkhTimes/139437" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139436">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✔️
✔️
✔️
بی انصافیه اگه از عملکرد خوب مهدی تیکدری نگیم!
✔️
برای اولین بار تو عمرش اومد پست غیر تخصصی دفاع چپ بازی کرد و هم در دفاع و هم در حمله موثر و خوب بود
✔️
✔️
پر تلاش و انگیزه از دقیقه اول تا آخرین دقیقه ظاهر شد و امیدوار مون کرد
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/139436" target="_blank">📅 21:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139435">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
ما به اینا نمیبازیم ...نه ساله نباختیم به اینا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/139435" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139434">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✔️
✔️
✔️
پایان بازی | شکست ناپذیری پرسپولیس به ۹ سال رسید/دربی جذاب برنده‌نداشت  استقلال
1️⃣
-
1️⃣
پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139434" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139433">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
✔️
پایان بازی | شکست ناپذیری پرسپولیس به ۹ سال رسید/دربی جذاب برنده‌نداشت  استقلال
1️⃣
-
1️⃣
پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139433" target="_blank">📅 21:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139432">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
✔️
امروز هر کاری خواستن با مجید عیدی کردن از بس که اون سمت اتوبان بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139432" target="_blank">📅 21:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139431">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✖️
✖️
هافبک و کلا استقلال برداشته و خیلی خالی هست هافبک ما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/139431" target="_blank">📅 21:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139430">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
✔️
✔️
هر دو گلر بد خوردن گلارو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139430" target="_blank">📅 21:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139429">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
گل مساوی و خوردیم متاسفانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/139429" target="_blank">📅 20:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139428">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❤️
❤️
❤️
ما به اینا نمیبازیم ...گل اول و محبی زد روی پاس بیفوما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/139428" target="_blank">📅 20:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139427">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
🔴
بریم برای نیمه دوم ..الهی به امید توووووو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/139427" target="_blank">📅 20:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139426">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
امیدوارم نیمه دوم شانس با ما یار باشه و کارو تمام کنیم ..شاید ارونوف تعویض طلایی ما باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/139426" target="_blank">📅 20:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139425">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
نیمه اول دو تیم خوب بازی کردن و بازی زیبایی و دیدیم از سمت هر دو تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/139425" target="_blank">📅 20:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139424">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
نیمه اول دربی بدون گل تموم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/139424" target="_blank">📅 20:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139423">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
بدون شک بهترین بازیکن نیمه اول .تیکدری و زارع بودن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/139423" target="_blank">📅 20:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139422">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✔️
✔️
✔️
پرسپولیس خوشگل کیسه رو کرده تو قوطی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/139422" target="_blank">📅 20:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139421">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‌
❌
❌
پرسپولیس بهتر و سرتر و سرحال تر داره بازی می‌کنه و سوار بازی هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/139421" target="_blank">📅 20:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139420">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❤️
❤️
بریم برای بازی ..الهی به امید ...خدایا امشب و پرسپولیسی باش ..حس خوب و انرژی مثبت و بفرستید برای بچه ها ..انشالله برنده بازی ماییم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/139420" target="_blank">📅 19:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139419">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
همه چیز آماده دربی پایتخت؛
✔️
✔️
هم اکنون ورزشگاه نقش جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/139419" target="_blank">📅 19:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139418">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/105ef18474.mp4?token=KpEMeN8HQ0LLByOhZbC3RMMknbR6PLMnwj5aGMMK-OuNj9pC2tQ2PM5RGzLt-vU4iC7M__Xo-S7-fcUXllBly_yRZ6zYCJUJzSfE4OwGNp8O7dn-t60KIu0ul42kSgShgqrlSJ6o9PrQ3vp_JkKnpQr3l60-RFrC6qfNDST3U4ITwGklvJ40Jthm_l2S8OcwI4EE7V5PX_11VKMBoXE_Gl0KFM_T1yRDX1pHdSjvGh1XOy1R9Ogc1ddmIvh90sUw0WChPkOjGFs_L9IfmE_2OUSMrDxMup7nZmOEpsmPRwGKeBXDIOsw-Ig0_QCaqcY5bYRgmvW4GbYW4ySpDDSEA3Iu1rl5PJCSmVf7tb3LWRzqqeo3nNlO0eANr1G4sWCzRsgZWlmB-9zSWxq7wrPPjRWJsG_mbRwqSDmglbirJMi2RHPq5XZll6za1oEmgyppbLYbHAj_X-UvQT5oqoSr14kjPARASnAL1laOW9zOpvNZFOU9W-t7gCu096dVFgnXgpveyMrCIcQqcDAnkbKg-oepOAZfgfATRdzJTg8VOJ5t_svPkaqVzr3VHLOMYjbwgh9J0O0_ICVZmbvzITwe-W0tvCPX3JRZ5TSoBDzSIkks4ttc0dt9ynxAznpzLdo_oTT65q9-632MK9e2NCijZVL9dKnT3w8rEi8oTbeXWEU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/105ef18474.mp4?token=KpEMeN8HQ0LLByOhZbC3RMMknbR6PLMnwj5aGMMK-OuNj9pC2tQ2PM5RGzLt-vU4iC7M__Xo-S7-fcUXllBly_yRZ6zYCJUJzSfE4OwGNp8O7dn-t60KIu0ul42kSgShgqrlSJ6o9PrQ3vp_JkKnpQr3l60-RFrC6qfNDST3U4ITwGklvJ40Jthm_l2S8OcwI4EE7V5PX_11VKMBoXE_Gl0KFM_T1yRDX1pHdSjvGh1XOy1R9Ogc1ddmIvh90sUw0WChPkOjGFs_L9IfmE_2OUSMrDxMup7nZmOEpsmPRwGKeBXDIOsw-Ig0_QCaqcY5bYRgmvW4GbYW4ySpDDSEA3Iu1rl5PJCSmVf7tb3LWRzqqeo3nNlO0eANr1G4sWCzRsgZWlmB-9zSWxq7wrPPjRWJsG_mbRwqSDmglbirJMi2RHPq5XZll6za1oEmgyppbLYbHAj_X-UvQT5oqoSr14kjPARASnAL1laOW9zOpvNZFOU9W-t7gCu096dVFgnXgpveyMrCIcQqcDAnkbKg-oepOAZfgfATRdzJTg8VOJ5t_svPkaqVzr3VHLOMYjbwgh9J0O0_ICVZmbvzITwe-W0tvCPX3JRZ5TSoBDzSIkks4ttc0dt9ynxAznpzLdo_oTT65q9-632MK9e2NCijZVL9dKnT3w8rEi8oTbeXWEU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
همه چیز آماده دربی پایتخت؛
✔️
✔️
هم اکنون ورزشگاه نقش جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/139418" target="_blank">📅 19:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139417">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
بازدید بازیکنان پرسپولیس از ورزشگاه در میان تشویق هواداران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/139417" target="_blank">📅 19:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139416">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1244018c05.mp4?token=k_FvjQNw--5kgOsWg9DR-7vqe_ygIIDGv6f_jwgQnCe5Iz3S61jIqDg9a-appf5TFdgRDpN7c8WgxIkOzdqOFqWQLtyoxnWqJcT38SQFG74EIpv9qEHqRsKNgmjNgupyeSeStxESxbO2ywTLrYadIKhyjSa5a6iaoBluL8zsGZoUSpHOLKVnL4d2JxPx97Rwp4R97bvzjQNWBRROW5gTi_4iGlDJXzEZM0a_GxxQe7OqaD8eqCIpTFXBBeo2stBxiGfwhGtx0jNLVfGthBx3f3lNZHBQRlBga1mAy5ems0iPkQu_UyBKxmBizyXBegvQo-dQE4aJ4hrSWFHada3hHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1244018c05.mp4?token=k_FvjQNw--5kgOsWg9DR-7vqe_ygIIDGv6f_jwgQnCe5Iz3S61jIqDg9a-appf5TFdgRDpN7c8WgxIkOzdqOFqWQLtyoxnWqJcT38SQFG74EIpv9qEHqRsKNgmjNgupyeSeStxESxbO2ywTLrYadIKhyjSa5a6iaoBluL8zsGZoUSpHOLKVnL4d2JxPx97Rwp4R97bvzjQNWBRROW5gTi_4iGlDJXzEZM0a_GxxQe7OqaD8eqCIpTFXBBeo2stBxiGfwhGtx0jNLVfGthBx3f3lNZHBQRlBga1mAy5ems0iPkQu_UyBKxmBizyXBegvQo-dQE4aJ4hrSWFHada3hHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بازدید بازیکنان پرسپولیس از ورزشگاه در میان تشویق هواداران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/139416" target="_blank">📅 18:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139415">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❤️
❤️
❤️
ترکیب پرسپولیس برابر استقلال
🇮🇷
پیام نیازمند، مهدی زارع، حسین کنعانی، مهدی تیکدری، مجید عیدی، پویا پورعلی، محمد خدابنده‌لو، محمدمهدی محبی، تیوی بیفوما، ایگور سرگیف و علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/139415" target="_blank">📅 18:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139414">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❤️
❤️
❤️
ترکیب پرسپولیس برابر استقلال
🇮🇷
پیام نیازمند، مهدی زارع، حسین کنعانی، مهدی تیکدری، مجید عیدی، پویا پورعلی، محمد خدابنده‌لو، محمدمهدی محبی، تیوی بیفوما، ایگور سرگیف و علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/139414" target="_blank">📅 18:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139413">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❤️
❤️
❤️
ترکیب پرسپولیس برابر استقلال
🇮🇷
پیام نیازمند، مهدی زارع، حسین کنعانی، مهدی تیکدری، مجید عیدی، پویا پورعلی، محمد خدابنده‌لو، محمدمهدی محبی، تیوی بیفوما، ایگور سرگیف و علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/139413" target="_blank">📅 18:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139412">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔵
دربی تهران در نقش‌جهان اصفهان!
پرسپولیس
🔴
و
🔵
استقلال؛ در دیداری حساس و هیجانی از دقایقی دیگر در لیگ خلیج‌فارس ایران به مصاف یکدیگر می‌روند.
🔗
برای پیش‌بینی این دیدار حساس همین حالا وارد سایت معتبر اسپورت‌نود بشید و با بالاترین ضرایب پیش‌بینی کنید:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
مینی‌اپ رسمی اسپورت نود:
👇
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/139412" target="_blank">📅 18:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139411">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⚽
⚽
اندازه گیری چمن ورزشگاه نقش جهان توسط نوشه ور  مدیر برگزاری مسابقه دربی 107
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139411" target="_blank">📅 17:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139410">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44157a322f.mp4?token=v21BbWSEPVyjhh2aadUebAmrXknVhFptigMtmBAWDNuKoGPlzwVAM8KHlsCYR24usIbtoBk-C-u3L4UchWohqxbCf52T5Q7MAsu9n6Vt2_WOZOIGnivn_Ef2WFJmgyKlJ-Sj0g-K96MyIubthRjVw9C6DWdcQSBU2RYM0hasJw-S0RqHYCcEoxDJVfs0PA8UvktXKzWJ5Eg_RIICkZAMGw0-wAD60YphhpnxSt4QwoGl8pcU96Qfa87rMJVg_R9ki038rSB4a54BODYUscuFeC2eQdGCqgpgEg5M7r8TWWVgRJZelwvfucSBi_68VOVK-fKZikmtVJ9e-kxNMrpfHbq1BqsCOkA7tPkoXhE28skZqMs2ZJs26OADOM4UWscdvoWsMOmo-7m3R1fSKwmQkLcWJEL_llWKheCWWtwWCiAs_CAFM6Vp4XuyULcaJb0q8fPkIqqTxaGhci6sF6-YDK3iWUP9husttep8GJOBS9eijQlyzv5vClHAuAl9fsIk96Ql8yT1hkhIMQbOF9zf_HUngUJxYggdp-JDduxc-XStvnEvoqiao_WnnqSoYqwi4hz2ACl3oFt5FzfAhfMIDmx-s033_4MlXXQ0YXQcECcW2MuzbUdNxt9SOAaSnxGt8mTe_8ghpMzIDTyDPjI41SCVdtBDhAKRXiRYpvMsRAU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44157a322f.mp4?token=v21BbWSEPVyjhh2aadUebAmrXknVhFptigMtmBAWDNuKoGPlzwVAM8KHlsCYR24usIbtoBk-C-u3L4UchWohqxbCf52T5Q7MAsu9n6Vt2_WOZOIGnivn_Ef2WFJmgyKlJ-Sj0g-K96MyIubthRjVw9C6DWdcQSBU2RYM0hasJw-S0RqHYCcEoxDJVfs0PA8UvktXKzWJ5Eg_RIICkZAMGw0-wAD60YphhpnxSt4QwoGl8pcU96Qfa87rMJVg_R9ki038rSB4a54BODYUscuFeC2eQdGCqgpgEg5M7r8TWWVgRJZelwvfucSBi_68VOVK-fKZikmtVJ9e-kxNMrpfHbq1BqsCOkA7tPkoXhE28skZqMs2ZJs26OADOM4UWscdvoWsMOmo-7m3R1fSKwmQkLcWJEL_llWKheCWWtwWCiAs_CAFM6Vp4XuyULcaJb0q8fPkIqqTxaGhci6sF6-YDK3iWUP9husttep8GJOBS9eijQlyzv5vClHAuAl9fsIk96Ql8yT1hkhIMQbOF9zf_HUngUJxYggdp-JDduxc-XStvnEvoqiao_WnnqSoYqwi4hz2ACl3oFt5FzfAhfMIDmx-s033_4MlXXQ0YXQcECcW2MuzbUdNxt9SOAaSnxGt8mTe_8ghpMzIDTyDPjI41SCVdtBDhAKRXiRYpvMsRAU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
مصاحبه با مادر و دختر پرسپولیسی
✅
پرسپولیس امرور برنده دربی خواهد بود؛ شک نکنید.۲-٠ استقلال را می‌بریم؛ علیپور و بیفوما گلزنی خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/139410" target="_blank">📅 17:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139409">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5be238bd7.mp4?token=JKOg4Axj74cbXOusemmqu6nZVcSFzkln3I3yAn99NKx3q1HirOoCzosLRWvPPMinzCwsHVjXehwhNnlevQDIgyKeum05VGxyz9GjijooqfxZIIhxR8jpzOlTvbCfICtxDk6IezwQoqRPS4Vy17x567PxTyPzpRgiexqEqXUWCpgoerjKlq-njhGBBmSEGT8KSmIQ8uzPbLyBwkyaia4oVZsCMsq2befIb4kRYV9_4Zf57zxZQ-XsJV4qjI2r0pwnTycmrnlrAk1v4QxprEsgFq8VpLWeV7hrBlrwM5JFLtEMo9MAgXuHLWV7hQqH7qSLcExSkGn9KIpb_SfoVTKdAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5be238bd7.mp4?token=JKOg4Axj74cbXOusemmqu6nZVcSFzkln3I3yAn99NKx3q1HirOoCzosLRWvPPMinzCwsHVjXehwhNnlevQDIgyKeum05VGxyz9GjijooqfxZIIhxR8jpzOlTvbCfICtxDk6IezwQoqRPS4Vy17x567PxTyPzpRgiexqEqXUWCpgoerjKlq-njhGBBmSEGT8KSmIQ8uzPbLyBwkyaia4oVZsCMsq2befIb4kRYV9_4Zf57zxZQ-XsJV4qjI2r0pwnTycmrnlrAk1v4QxprEsgFq8VpLWeV7hrBlrwM5JFLtEMo9MAgXuHLWV7hQqH7qSLcExSkGn9KIpb_SfoVTKdAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
ترافیک سنگین در مسیر ورودی به سمت ورزشگاه نقش جهان اصفهان در آستانه  شروع دربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139409" target="_blank">📅 16:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139408">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a4db0aec.mp4?token=R-igav9ZDI1a2M_G3lVrxxw7YmKWq7Y55yMzpr4YFUKjVSYu_WLe5sm8tTWH_0EE2paBjqt3nb4W3gouV4yjW9x22O01Lmo9nNxknDgnvAEDKFPKmW8-YF8pPjjaU8BsFGHAUrSqIXTE-5-np5bnv-RcQSefsbrFfFlKNbBTvT-1vxT9VyMmMxjonN3AU4q8xQ4_rYwZfzofc9-vkwuLKA8q66uG68m7x189m-AX0Zkl0jkhEAhsNe1ML-PnZiGxWreN4LKl3cHGLek7dpzBaOcpZAl6jJzteN3ETc4zKdlvyLr4EgHGvVpdFrDnQ6XTXVAoQmnZiRggpWuTsKI34YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a4db0aec.mp4?token=R-igav9ZDI1a2M_G3lVrxxw7YmKWq7Y55yMzpr4YFUKjVSYu_WLe5sm8tTWH_0EE2paBjqt3nb4W3gouV4yjW9x22O01Lmo9nNxknDgnvAEDKFPKmW8-YF8pPjjaU8BsFGHAUrSqIXTE-5-np5bnv-RcQSefsbrFfFlKNbBTvT-1vxT9VyMmMxjonN3AU4q8xQ4_rYwZfzofc9-vkwuLKA8q66uG68m7x189m-AX0Zkl0jkhEAhsNe1ML-PnZiGxWreN4LKl3cHGLek7dpzBaOcpZAl6jJzteN3ETc4zKdlvyLr4EgHGvVpdFrDnQ6XTXVAoQmnZiRggpWuTsKI34YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
هواداران استقلال و پرسپولیس در مسیر ورود به ورزشگاه نقش‌جهان اصفهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139408" target="_blank">📅 16:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139407">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/282676305a.mp4?token=Q-f7ERqfMFQFRmL1CA71t1VfT8fVrdjIA_jrevn8ZLQXhSZ015aju7ar9yXMHSrEtcIIE7aBe2Q3l9difOzQgbyuR6K079L-V3yANrj9N8iKANH11shtQPTQljO3ZcbDyrxfvc5-gr57G2CT-e3keQNGa74crs82UkR1ztjoYz1jdLZ2ITC1vkCrj0u_3tswti5efkTUbUghObfivc6m6QJ1hDJDaKQfzE7PQVZ6OtQoqJ6eIriXXoGn3iPtQr5BoWQzXvhu30hyekn-Hp3UKuwKS8qBpzifB_Fsgz2CTW0aXF0qqnS2Tvhi5sEEBOZri_d0ysC-EraVdlcX196Ztg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/282676305a.mp4?token=Q-f7ERqfMFQFRmL1CA71t1VfT8fVrdjIA_jrevn8ZLQXhSZ015aju7ar9yXMHSrEtcIIE7aBe2Q3l9difOzQgbyuR6K079L-V3yANrj9N8iKANH11shtQPTQljO3ZcbDyrxfvc5-gr57G2CT-e3keQNGa74crs82UkR1ztjoYz1jdLZ2ITC1vkCrj0u_3tswti5efkTUbUghObfivc6m6QJ1hDJDaKQfzE7PQVZ6OtQoqJ6eIriXXoGn3iPtQr5BoWQzXvhu30hyekn-Hp3UKuwKS8qBpzifB_Fsgz2CTW0aXF0qqnS2Tvhi5sEEBOZri_d0ysC-EraVdlcX196Ztg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حضور دو جیمی جامپ پرسپولیسی و انجام خوشحالی رونالدویی
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139407" target="_blank">📅 16:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139406">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7410fd3106.mp4?token=SbuMTYeGOK2qCDp_Hhfw1iyvsxTuwZfu4NexBgIErGecBs6mOLUtNG7MMgqT1f9-I_3-mKOfjT1u_rbJijJ5oFAE8QNwYZKQUFGjCS55uwSmJQjtMdyow-p4IZzLce55i545XzPwYWxOObiGLQXLTKsL1erUzMotulsoyiPdhqV67JBVENKrcNqENJUxGnAyVm7cOFdfNS6IrbprbfIWIkXe-DR0EyFW1h2dszgIMtsMf-B4hqwlEUc64yYue2sFbh98DC9lFLYzbKUVE2OTMatzmbd7KWhc6xNnaNsAJ-16sN-exSUBpUm3kSZR1VdANEuRBzXaQnxmMtLqQa5UTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7410fd3106.mp4?token=SbuMTYeGOK2qCDp_Hhfw1iyvsxTuwZfu4NexBgIErGecBs6mOLUtNG7MMgqT1f9-I_3-mKOfjT1u_rbJijJ5oFAE8QNwYZKQUFGjCS55uwSmJQjtMdyow-p4IZzLce55i545XzPwYWxOObiGLQXLTKsL1erUzMotulsoyiPdhqV67JBVENKrcNqENJUxGnAyVm7cOFdfNS6IrbprbfIWIkXe-DR0EyFW1h2dszgIMtsMf-B4hqwlEUc64yYue2sFbh98DC9lFLYzbKUVE2OTMatzmbd7KWhc6xNnaNsAJ-16sN-exSUBpUm3kSZR1VdANEuRBzXaQnxmMtLqQa5UTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
⚽
اندازه گیری چمن ورزشگاه نقش جهان توسط نوشه ور  مدیر برگزاری مسابقه دربی 107
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139406" target="_blank">📅 16:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139405">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
✔️
✔️
محسن خلیلی: ابوالفضل جلالی به دربی رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139405" target="_blank">📅 15:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139404">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
❌
رسمی؛ ممبینی که صبح از سمت دبیرکلی برکنار شده بود، مشاور مهدی تاج شد.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139404" target="_blank">📅 15:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139403">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⚽
⚽
پوستر جذاب باشگاه پرسپولیس برای دربی
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139403" target="_blank">📅 15:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139402">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55bf0f119c.mp4?token=dv-33zqr_vehS08r7OZf_Q0_9_ceP69V3flvwfkeYFL1F8PHnO9CM2HGZvYvXiVi2xTHm7oGL-05F0vsLCNfPGkIEugjlLvcg-_aUbpaqIitjOvtIuGWxxIllKR7wQT21YwNiGPFq9SGooRufBLGmiMtXTKFlD0Nv6PB-_SqQXSK-jPoMPplhI11vuYaf72i1ZpODSP4PcqD_8vjCx8RNaaXqS-cmWRY-vNhuOPSZ1W47cLbYU9YhRLWt4BIpTNEdtFCSQPphLKBcwOUHA0unid7L-GJJGmOw3VtU_qEXpSowkInBo5Q7-4Xl2e7nXaTbg7uM3tuw-vs2OuQ3SuyMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55bf0f119c.mp4?token=dv-33zqr_vehS08r7OZf_Q0_9_ceP69V3flvwfkeYFL1F8PHnO9CM2HGZvYvXiVi2xTHm7oGL-05F0vsLCNfPGkIEugjlLvcg-_aUbpaqIitjOvtIuGWxxIllKR7wQT21YwNiGPFq9SGooRufBLGmiMtXTKFlD0Nv6PB-_SqQXSK-jPoMPplhI11vuYaf72i1ZpODSP4PcqD_8vjCx8RNaaXqS-cmWRY-vNhuOPSZ1W47cLbYU9YhRLWt4BIpTNEdtFCSQPphLKBcwOUHA0unid7L-GJJGmOw3VtU_qEXpSowkInBo5Q7-4Xl2e7nXaTbg7uM3tuw-vs2OuQ3SuyMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ورزشگاه نقش‌جهان ساعاتی مانده به شروع دربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/139402" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139401">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✔️
✔️
✔️
محسن خلیلی: ابوالفضل جلالی به دربی رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139401" target="_blank">📅 14:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139400">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✔️
✔️
با اعلام استاندار اصفهان دربی تهران در ساعت 19:30 در استادیوم نقش جهان اصفهان با حضور تماشاگران برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139400" target="_blank">📅 13:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139399">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
🔴
🔴
مروری بر بهترین گلهای پرسپولیس در دربی‌های لیگ برتری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139399" target="_blank">📅 13:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139398">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccTraOCRQCfiRripKO3yRIJq8dOag5LYCPOsrnznbJEBPgOdh95Lo44Re3tRabG1R5OX42I1K1XbaiC8OE54vST78LaGSQF-U18cfJO0qa6wtkNwBH3El__dCXCWrordVLw6o-lvlrelkpqNE6TYCQJtl3_MwGxK1l8l1FVZhqjUwf0LybWtDJ6kGJ3G2wul1ML6JYIlk2t5YhGsfu0I062cbPrWwtxphUtQGtlMDOdwBOgRT-aIHG_nwRBTc_g1pSh_CR-5XY208xp2ECk9bW_UVaEz54QYcrcNI0lCXHiNcZO6oThQkBlj7LZb7VsUl9b_72EuR-MlIGlBxkuvlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
اصفهان در آستانه یک نبرد بزرگ!
⚽️
پرسپولیس و استقلال؛ دربی پایتخت در حساس‌ترین جدال فصل برای شبِ فراموش نشدنی.
[
استقلال
🔵
🆚
🔴
پرسپولیس
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
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139398" target="_blank">📅 12:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139397">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
نتایج 19 دربی اخیر پرسپولیس و کیسه:
📊
در 19 دربی اخیر دو تیم 8 برد سهم پرسپولیس و 11 مساوی سهم دو تیم بوده، و نکته اینکه کیسه بردی نداشته
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139397" target="_blank">📅 11:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139396">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⚽
⚽
پوستر جذاب باشگاه پرسپولیس برای دربی
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139396" target="_blank">📅 11:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139395">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcd6b3f28.mp4?token=kifhkdGSMKQyslBrXhIp4D6I4Djt8nFIZzHnFKb1VD9cM18cEs6DeSQcsLFty5GwrUqJ732r4ljZKxPAI95kPboQCQ_v75Q4PSb8xyyf8Pc6YESjJxA2uBnAoXR7yg9kojUoVyX4vUNyaCoex-4ff6hH70F5q9AbQ1DuMpkLqD6y3XiKqtCeamTdaUEiL4hklI_NnTMYcLcCn5ffSyRqzVN36Aqs1-t-4sLSabzaUZZP3J-1f-i13nWaPRbgP3cmwQqKorzb_-rBxrDyVcMwExUEaOIocEq9ApbRNszCkFMRZulprKXNtkzT67rvsU7_RqShs6eWhhYf-OxbgO1Viw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcd6b3f28.mp4?token=kifhkdGSMKQyslBrXhIp4D6I4Djt8nFIZzHnFKb1VD9cM18cEs6DeSQcsLFty5GwrUqJ732r4ljZKxPAI95kPboQCQ_v75Q4PSb8xyyf8Pc6YESjJxA2uBnAoXR7yg9kojUoVyX4vUNyaCoex-4ff6hH70F5q9AbQ1DuMpkLqD6y3XiKqtCeamTdaUEiL4hklI_NnTMYcLcCn5ffSyRqzVN36Aqs1-t-4sLSabzaUZZP3J-1f-i13nWaPRbgP3cmwQqKorzb_-rBxrDyVcMwExUEaOIocEq9ApbRNszCkFMRZulprKXNtkzT67rvsU7_RqShs6eWhhYf-OxbgO1Viw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
بهمنی، سخنگوی سازمان لیگ: 6 هزار بانوی هوادار تماشاگر دربی 107 خواهند بود/ درهای استادیوم نقش جهان ساعت 12 باز می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139395" target="_blank">📅 10:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139394">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/566218d82d.mp4?token=sa0f1Qwdge_kGpBhTklahaL09jP52luulK3wfAu6qjL312F5CTyImOwc-3L_9U8Sua75Pk2bfQtMt0s_BszYCYCd8p5j4KA_LVyQ5GFN9QU_R1ulxBjIOsP3N7SOvRgGZikBPpUA2bKY_AqN9Q9fiiVL6BMXd5Vw5H_llvDSpcRcmykRflKpSXS_ShKwQrHIdx_5C6uIKS_dJE10Z_LLWKujTxRNI0eP6k5K8BvzzSUNDOJP8wJ3FotokrBtvnp6AQI-Sb_KcIsXVIAlXe37szbot3TXkOah2Kc2qgV-J-wrbYs5HPR3I_OyrO2qt94bnt_ETPiwbiTQwWeMjt9DCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/566218d82d.mp4?token=sa0f1Qwdge_kGpBhTklahaL09jP52luulK3wfAu6qjL312F5CTyImOwc-3L_9U8Sua75Pk2bfQtMt0s_BszYCYCd8p5j4KA_LVyQ5GFN9QU_R1ulxBjIOsP3N7SOvRgGZikBPpUA2bKY_AqN9Q9fiiVL6BMXd5Vw5H_llvDSpcRcmykRflKpSXS_ShKwQrHIdx_5C6uIKS_dJE10Z_LLWKujTxRNI0eP6k5K8BvzzSUNDOJP8wJ3FotokrBtvnp6AQI-Sb_KcIsXVIAlXe37szbot3TXkOah2Kc2qgV-J-wrbYs5HPR3I_OyrO2qt94bnt_ETPiwbiTQwWeMjt9DCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
فیلمی وحشتناک از حمله دیشب به سیریک
🗣
بیچاره مردمان این منطقه
🖤
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139394" target="_blank">📅 10:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139393">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0cZ7BATv_s-g9yu9QjeAUaK5zWzQ7SnM1A9Z_6vKvd1mEc19q3lcVAaJRyTShD1CSosjy3X85jgvXWyeq3WtL4hpn2EMipPC-4Bcd7N3o1vBizWehIUD20ShZjBnfYZuf1ZnyUCXWxswklKJTeUqToETzJEVcxkudyGzm2NUHpMcczPxBO2_OKKy1P5nORxaFn7dhi7UX-kznpBqVXu9P9vKy_opUiu5e9Xx8OUQZ87LOTS_t_PuIq6gEN-hw-AGY9jWziKe7eADh9ud4RgyWBgKzeznKFx6C9tK2Geym1tEz2cYHlJO2nb0VHJCrlmmBQ9AD1YkOXh1j1orxBLeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
⚽
پوستر جذاب باشگاه پرسپولیس برای دربی
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139393" target="_blank">📅 10:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139392">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
✔️
برای کمک به تیم ملی امید  هفته هفتم لیگ برتر فوتبال لغو شد!
✔️
ایسنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139392" target="_blank">📅 10:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139391">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkXAX8iYqDhRUDBxJ9Id_-N5I1f9N2QtrD2ny7gZEXLxQfu69Od66EVh-MWX1RmFV4xnFbzgYUhgkfKkiuNoMPqGrmxCYJSOLWzm21yKryh5w41Ug9khEJiwbo5NhuSKWJ3KJQvE0bITKiqasR3oRV6tIOFTwUbirDZjqWjETZfNdrkKGClYZ9VYQk7-KbitIt_cLvnYDtORub1TMIhvpX_OiGFBiJpIEuAqrz__JKGZU_hjBj9sFw-Xx1pkXK_XqF5yBowH5Qb178mIk4V1eW3LShbNQefFEEnLI1I4V_Xc8K7EnsOnqAiMoFmtVHZ8RAJniF6Hepd4yA5oxaSWtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⚽️
تسنیم: شایعات الکی و بی مورد نسازید، دربی با حضور تماشاگران و بدون هیچ تغییری در استادیوم نقش‌جهان امروز برگزار خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139391" target="_blank">📅 09:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139389">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3Uv4ajO4pRcqlJgLih2IuVNL6mFfskuU3mV4a7Nkt2MyMehosDmyotmQoLK3Jm2PHYRQM-ITVf6MSkn73LW4G-mSK-EJH3NI-6rx0KdM0gXQPNkHhXEXu1yuVpPHSg4eDwB9blb_3ZKB0TZhsk4_hXROpi4gBMevHk6RJBNRNUW9xRiNfc_AgdgsZgjafDQTB8OOllXFlWq3Us4S6FkKiqjVTHJxH4yo_Jk6B8Y9UPFfqMlUlvTfZTnk04DXrdRMREXJtOFLuZlNyW2BtX3GgjdxliGU8cn_UKp5CweWmXwm0qQ-heyIOUNtuJb-aWgcee20SMTnoNu_qzwujizqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
با اعلام استاندار اصفهان دربی تهران در ساعت 19:30 در استادیوم نقش جهان اصفهان با حضور تماشاگران برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139389" target="_blank">📅 09:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139388">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❤️
تکذیب شایعه برگزاری بدون تماشاگر دربی استقلال و پرسپولیس در نقش جهان
⚪️
⚪️
استاندار اصفهان شایعات مطرح‌ شده درباره برگزاری بدون تماشاگر این دیدار را تکذیب کرد و گفت: این مسابقه با حضور تماشاگران و طبق روال پیش‌بینی‌ شده برگزار می‌شود./ مهر
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139388" target="_blank">📅 09:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139387">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✔️
خبرهای رسیده از فدراسیون فوتبال حاکی از اینه که احتمال لغو یا برگزاری بدون تماشاگر دیدارهای فردا لیگ برتر، از جمله دربی وجود دارد
❌
❌
تصمیم نهایی به‌زودی اعلام خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/139387" target="_blank">📅 09:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139386">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇷
🇮🇷
صبح روز دربی و پر از استرس بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139386" target="_blank">📅 09:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139385">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDCx5-k2slix0X2W4EAgK387fkptlwScwpNzLJBesArrvqRL7lQR2WbRMPyokXNgRp9weK-1JwzKqssj8Uh3nlzRwBBKYGU3f6wyUqjLspJ64QWpHahMsz16Q1j_7I0VplESmLNFmtNDBgKUtZ2iPwJt2PTrIJls6RvrSGjDcmo4qdsJdvHOgA5MFeME8rMSHgd04WEAMX-Ssx-BSBLAg4beutnMIqmFhYlMfSfkhESm0S4JHaPXB0rkM5sKf_3R_3wcDEOcCBpbvLmWFWvEDgqMzYRemR-owPfv7djUck8difg3nyCOIbkaPxhMnldNFlcqJzmYZ_HBTYIOlgPOjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
دوئل‌های جذاب در یو‌اس اوپن!
🎾
الکساندر زورف
🆚
لورنزو سونگو
🎾
آندره‌آ گِریِری
🆚
الکس د مینور
🟡
کدوم ستاره‌ها از این نبردهای حساس سربلند بیرون میان؟
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی دیدارهای یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
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
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/139385" target="_blank">📅 01:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139384">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
فووووووووووووری
🚨
شورای تامین استان اصفهان فردا 8 صبح جلسه اضطراری داره
🗣
سه سناریو پیش رو دربی پایتخت قرار داره
⏺
1_ برگزاری دربی پایتخت بدون مشکل
⏺
2_ برگزاری دربی بدون حضور تماشاگران و عودت پول بلیط به هواداران
⏺
3_ لغو دربی پایتخت و برگزاری آن…</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/139384" target="_blank">📅 00:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139383">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
✔️
#مهم
❌
❌
دربی لغو نمیشه و اینکه یکم دیگه هم ایران هم آمریکا حملاتشون رو تموم میکنن و دوباره جو اروم میشه !
🔄
🔄
البته درسته خیلیا اینترنت شون اختلال خورده ولی تا فردا صبح درست میشه
✔️
به امید برد پرسپولیس
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/139383" target="_blank">📅 00:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139382">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❤️
ترکیب احتمالی پرسپولیس:           ‌‌‌‌‌   نیازمند تیکدری زارع کنعانی عیدی  ‌‌‌    پورعلی خدابنده‌لو ‌‌‌    عمری بیفوما محبی      ‌‌‌‌‌‌‌‌       علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/139382" target="_blank">📅 00:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139381">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
✔️
#مهم
❌
❌
دربی لغو نمیشه و اینکه یکم دیگه هم ایران هم آمریکا حملاتشون رو تموم میکنن و دوباره جو اروم میشه !
🔄
🔄
البته درسته خیلیا اینترنت شون اختلال خورده ولی تا فردا صبح درست میشه
✔️
به امید برد پرسپولیس
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/139381" target="_blank">📅 00:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139380">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
در صورت بالا رفتن درگیری ها، احتمال لغو پروازهای داخلی وجود دارد و از این رو تیم ها برای سفر به اصفهان باید برنامه خود را تغیبر داده و با اتوبوس راهی این شهر برای انجام دربی شوند
✔️
✔️
البته تا این لحظه خبری مبنی بر لغو پروازها مخابره نشده است///طاهرخانی…</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/139380" target="_blank">📅 00:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139379">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
❌
تموم شد
✔️
اولین توقف تراکتور تو قزوین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/139379" target="_blank">📅 23:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139378">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344f252bb4.mp4?token=frZ5gOD8rFSi2J5YMgrh7zoxPDjwyHvtWqICIVH0lAHoEqnSbtvJHll9S_4wIA-8dcfkoEq6oaArSpnTXq-TNgGD61H_FUo4A-u2hPKn7yLgkKwdRlrah5z5AdKjrfIFpsKJ9QHAsZOnh-rMby1bLbsRyzXjTm5k84u5ATSV6x0Wcc3gIH0Cj2a9VmqTd-vFESKEmU72XJyuCJSWUmVNju7eToCQNTi42YCgGYeDk8nteRFYrOOz-AhJWZTkfDTKgxEcMNKEaCEs57Nb-b9D34B7D4kYygLFKLL6pnjZ0xbRy-ycpzNcncB1-_pwy21K9oAiFlHVh1jFc2M-HFtU6hy7boRac5mUS-kjH5Rn4Y0XdrgPpBipDFs_HW_6KGI4Sgr1tXlQnhUiqpl8nJ5h3xBOR0pbIO2rM2IyO_vx5t2-sg4HTCLhF5ky2Ibme2LW9lxTG7wQJ9VIphvbrvXyHohmqPByCEUdYaeoBBCrqEzMb2s7U1i0J_3kZL5DInFj4vD4hZQy-kjtsyzh64wodi94iHFZcF6WSgf9Hlr6SjpGZliuLy88q3xlwsnqf2vES4jOpDJ904TpNh6FrpiVFtsGXMFvwyqIykC3QmhSCV6UPBYHiMjUNHocuQXAO469l4GnwIiG_KGYh_wKZLS8sWl8rMjLAlBkn3hH76CXn4M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344f252bb4.mp4?token=frZ5gOD8rFSi2J5YMgrh7zoxPDjwyHvtWqICIVH0lAHoEqnSbtvJHll9S_4wIA-8dcfkoEq6oaArSpnTXq-TNgGD61H_FUo4A-u2hPKn7yLgkKwdRlrah5z5AdKjrfIFpsKJ9QHAsZOnh-rMby1bLbsRyzXjTm5k84u5ATSV6x0Wcc3gIH0Cj2a9VmqTd-vFESKEmU72XJyuCJSWUmVNju7eToCQNTi42YCgGYeDk8nteRFYrOOz-AhJWZTkfDTKgxEcMNKEaCEs57Nb-b9D34B7D4kYygLFKLL6pnjZ0xbRy-ycpzNcncB1-_pwy21K9oAiFlHVh1jFc2M-HFtU6hy7boRac5mUS-kjH5Rn4Y0XdrgPpBipDFs_HW_6KGI4Sgr1tXlQnhUiqpl8nJ5h3xBOR0pbIO2rM2IyO_vx5t2-sg4HTCLhF5ky2Ibme2LW9lxTG7wQJ9VIphvbrvXyHohmqPByCEUdYaeoBBCrqEzMb2s7U1i0J_3kZL5DInFj4vD4hZQy-kjtsyzh64wodi94iHFZcF6WSgf9Hlr6SjpGZliuLy88q3xlwsnqf2vES4jOpDJ904TpNh6FrpiVFtsGXMFvwyqIykC3QmhSCV6UPBYHiMjUNHocuQXAO469l4GnwIiG_KGYh_wKZLS8sWl8rMjLAlBkn3hH76CXn4M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💣
⚽️
❤️
حمله شجاع خلیل زاده به عادل فردوسی پور: من دو سال است که فحش می‌خورم اما خم به ابرو نیوردم، فشارهای زیادی روی منه و خدا رو شاهد میگیرم که یزمانی می‌خواستم از فوتبال خداحافظی کنم اما این کار رو نجام ندادم، دو سال فحاشی به من شد و تمامی این فحش‌ها تقدیم به عادل فردوسی‌پور
🔻
همه مردم تبریز می‌دونن عادل فردوسی‌پور با تراکتور مشکل داره از زمان برنامه 90 همین بود، الان هم همین است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/139378" target="_blank">📅 22:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139377">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
شنیده میشود که چندین بازیکن تراکتور به دلیل بدنسازی بد مصدوم شده اند و باشگاه تراکتور با تعطیلی لیگ به دلیل اردوی تیم ملی امید موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/139377" target="_blank">📅 22:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139376">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
✔️
شایعه شده که تارتار دوباره میخواد همون قمار از پیش باخته بازی تراکتور رو تکرار کنه و با یه مهاجم وارد بازی شه و عمری رو به جای سرگیف بازی بده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/139376" target="_blank">📅 22:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139375">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
✔️
سهراب بختیاری‌زاده: می‌خواهیم ریتم خوب شروع لیگ را ادامه دهیم و پرسپولیس حریف خوبی است که به امید خدا بتوانیم آن‌ها را شکست دهیم و با روحیه بالاتر راهی لیگ نخبگان شویم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/139375" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
