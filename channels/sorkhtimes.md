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
<img src="https://cdn4.telesco.pe/file/evxyKxp_Rdk8RQ7MVdv85MZb9QEASaCZxHR7ZcisCvwiTlfRXr068rKazIzXPxCtu4rVH5RI_rOz9uFCiPuFNXBjee-2pyljm6EQnJ_FB-pVWD8vDBLbP7TouIRRAjz1JaRECXyvwl2lsVybPLkCM80QnLGLIur3h6e-ki7fSP0jAbD2kS-F66iajV5tTdylyX7-wqjLmdhYfP2AnXc3ABi7fm2mnNK4QY2eNXZnqnnZ4g5Jbl9kIptPYPjxm0pJuKhRVhIyVmTYEPu7-86F0g8-Bx52V2YzHxO3UatHZgG3zGH5OIAEf7qNWh1iNQHevKI7HcFTQ0aOGUu4hWU6cQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 12:35:10</div>
<hr>

<div class="tg-post" id="msg-135834">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_zEi2Iw7sH5I9AaoLqa9JAes6MB9HhPniJYO2MC90uzY6SRUc0n7roSgBX7jmttbAMAKspFd2kqp0_G6wVHgF7T-w0vpfp6DX5Yn0lkO55kNgAVBeHOHo6aRNslM__QTxffdB34GXDUap7qbSMLaMUptuUnQaWjIqN93PU32slmDeEFSw7AndaGjYXVOC5-x_nzckNPZKYNv96QEn90OYuMMEqg51vjX9BKZGh3Vs91cUsE9oQa0jVRYbWyPAp34KTQL5vVd8EG_nDAIZkSm82eIbH1VcgCCZ_cs1DWgUVD1jxBWs5w8FI58kC8qQuswUE4ND9soSHhBN0ePy4VfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی
؛
بامخالفت‌تارتارسرمربی پرسپولیس جدایی محمد عمری وینگر سرخ ها از این‌ تیم منتفی شد. ضمن‌اینکه محمد عمری برای تمدید قراردادش با باشگاه به مدت سه فصل دیگر به توافق کامل رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 397 · <a href="https://t.me/SorkhTimes/135834" target="_blank">📅 12:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135833">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
شنیده ها؛ گفته میشه علیرضا جهانبخش گفته تا یکشنبه به پیشنهاد پرسپولیس پاسخ میده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 944 · <a href="https://t.me/SorkhTimes/135833" target="_blank">📅 12:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135832">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">◀️
جدول خاموشی مناطق مختلف تهران منتشر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SorkhTimes/135832" target="_blank">📅 12:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135831">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMge7QhFwlDPHFXU4teTFBCBqB-w_Jh49oG2hT7YS7MP9D5iTcWLmI3kVsTHHa6fihTPPuu1gigBWBWzeaJbe71540VbTXeFrQ88lXyfpEZRhh3Y0SHdj4xSpneZWg4ZLXzZbWQeMY1Zzb-ddtnM0fDswGYMVe5JEFnX_YRpkgvAqFoW2zfi_kmP9u_2sat2s6YFEAh6NiaOpxWB3tnObVglQrZCKckVbLOx4GkINW-pCbg0BSJCARJaqPzFLDPDwJs0uanbqOpjb5s6AC0sbSwU3rvZuL3_5DgazY--9IsyA20CscfkqzkfDq5R4B3Wu0ujUSXUAR6eZt-2aL2-uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شنیده ها؛ گفته میشه علیرضا جهانبخش گفته تا یکشنبه به پیشنهاد پرسپولیس پاسخ میده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SorkhTimes/135831" target="_blank">📅 12:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135830">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
✅
پرسپولیس برای برگزاری اردو پیش فصل جمعه هفته آینده به مدت یک هفته تا ده روز راهی ترکیه خواهد شد/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SorkhTimes/135830" target="_blank">📅 11:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135829">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
فوری؛ با اعلام ترانسفرمارکت، علیرضا کوشکی از استقلال جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/135829" target="_blank">📅 10:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135828">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/135828" target="_blank">📅 10:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135827">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
مدیران باشگاه پرسپولیس روز گذشته جلسه ای برای چذب پوریا لطیفی فر با مدیران گل گهر سیرجان برگزار کردند و با این باشگاه به توافق رسیدند / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/135827" target="_blank">📅 10:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135826">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJAcPhprEWF0WaUqtRJbVGUTnQjSGEdiInVcToCDpJhhNiV_sieH2Y2UG85xltTtjXJEZ2K3qt7k36K3qnrru9MrNkySb5cEL930dLoDOScXj4nMPN_oFjtQRsrrHGELOOAF1A2NZjc5WbsCBUZrwOiyYEx5oOnG-2UqaIIyrIcns-QxjDahlSym2nHdYPV9Ny2zm23x0yxRaSHb5Jo1VcoovhyxeGBo05P6XsZePDv712q-cB54qCwxIRgjhMirwU32NdEyhgsREOITHZeTQ5rfODREymFrWPW32UO7g7bX0h9izQ050Ck0DLiXp3RdOqX5wRQQlEe68CeacARIxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
جدول خاموشی مناطق مختلف تهران منتشر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/135826" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135825">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❗️
🏟️
ورزشگاه آزادی تا دی ماه در دسترس نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/135825" target="_blank">📅 10:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135824">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
چمن ورزشگاه آزادی جمع آوری شد. پس از پاکسازی زمین و ضد عفونی ‌کردن آن، تازه کار اصلی آغاز خواهد شد. یه چند ماهی نمیشه ازش استفاده کرد 1 سال گذشته و اینا فقط دارن بازسازی میکنن ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/135824" target="_blank">📅 10:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135823">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/135823" target="_blank">📅 10:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135822">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❗️
❗️
فرهیختگان: مهدی تارتار با جدایی محمد عمری مخالفت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/135822" target="_blank">📅 09:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135821">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
بیژن مرتضوی، خواننده و آهنگساز ایرانی مقیم آمریکا، با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/135821" target="_blank">📅 09:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135820">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvat9KAHiZIDmZfKKw4_f_y_6g68jjZK3mR2PhRMOm86aIIg_Qusg7MamitvKufkBfnGVkEjZE_nXkr_JAMWrCe-cxd4qtTwCbCa1fCz0u7PA5fnU9r3mBerblSdDYCELAFNzRqriSxeiS-C6p2xGMXs8_NqodF2zr9_d4u1s09Au-O5DcdnYGigbRozKDll--7TDLZh8KFWDMY4GCLTMrSycx7NatMACiLmxqkT3LuHRSyCdY4rnwKxTNjysPTwtA-TGm0mElvlKISEcPVaeLQo5OjwsQaRpEB95fThX-4PwsiCdWb42GNEd5_JqVa7RW2UZbvmQS1puVe1A3m6pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری؛ با اعلام ترانسفرمارکت، علیرضا کوشکی از استقلال جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/135820" target="_blank">📅 09:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135819">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
متاسفانه طبق گزارشات، آسایشگاه سربازان در ایرانشهر با موشک زده شده است تعداد زیادی از سربازان وظیفه جونشونو از دست دادن و امار مجروحین هم بالاست
🔴
🔴
همچنین درخواست فوری از مرکز انتقال خون ایرانشهر برای اهدای خون در شهر بمپور برای مجروحین ثبت شده
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/135819" target="_blank">📅 09:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135818">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
ترامپ : امشب و فردا، ایران را با قدرت مورد حمله قرار خواهیم داد، توافق‌نامه همکاری با ایران یک آزمون بود، و ایران در انجام تعهدات خود در این توافق‌نامه شکست خورد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/135818" target="_blank">📅 09:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135817">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mw3y2ADgZ7suXnnvZWOPkHOpyuVMUna1lYEfCQSLvVuakKcoyMap9nxh-aUkPotJHGQjYcZQH9rBPTjsO-cwJkFjyrk2H_ueKBa5UQjPeSptZ5VPlNzDdWUupPDENqt-meO0Trq9_6bERPf7Tr6_zyYRCfypxSL5dWzHy1aciKVSmd4nUN18-snh06SvSBUd9SBRgZux9CEkznmFNTtFi8VWwdwWhqRNq6cvSYIyF_DFeGi7jjLh2_BJm8tvJ5VhZ9m2mr33ClfdYvLvbHYBblT3swrzaj4mvG_iQDNngk_mnl5TDQjidwyetPvgoW54YsMeeA2NHmaio_M1ZwkCmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صبح بخیر ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/135817" target="_blank">📅 09:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135816">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/135816" target="_blank">📅 03:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135815">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIZsj8TPtzK2ilItlfufxjXbanzWD6aUWpfNHsjrU06j3apnuSvMcjqQKd47rRwGaqFBUh0aV_7Kpf1eF5Hq_P62e0FMv4OdgmHYd4EmevPvjjJUCd3Z2IBhS0hDCjl1BiNvb7N0T8nMzcxbTP00qCmP1eb6CKwbUQrQ1iy6Ma7TeiYKeV4DYNFSNo20IDQfQLxujm0c5F2fr4xWBCoqS6QvLRdS_sBxjxsc6EqknVl-Vz8kyBwgn1KEzehBrD5DY35yxIE719YQFxkYh1ETrMI3JZk7jo-cj8YxLY4ZeYZ4EpVztMkQZshYOF4Njydd82NKj0XJy_NckxneiRpDLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/135815" target="_blank">📅 03:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135814">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
❗️
فرانسوی ها ساکت هستند و حرفی برای گفتن ندارن تو گروه  پ.ن رفتن اسپانیا به فینال فقط با یک گل خورده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/135814" target="_blank">📅 00:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135813">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
✅
خداحافظی فرانسه با قهرمانی و رفتن به بازی رده بندی ...خداحافظ آقای امباپه ..سلام اسپانیا به فینال جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/135813" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135812">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
✅
جونم اسپانیا گل دوم هم زد و در آستانه رفتن به فیناله ..فرانسه در آستانه باخت و رفتن به بازی رده بندی ...کیا میگفتن فرانسه اسپانیا رو میخوره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/135812" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135811">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfHnG1Upi-CAdxLsCaLuHD1rbDX8DJlZ4cd6y1uFyMN77YciaQfnXZXDGwK7Ke3N2yF2RXy5uY_F9je6X2FhfbwUbgh-1g3Dr2pA9gwTcNsJMGwqVGRemmENqalFe4RSGLJdkgBUjRJzEznqQrOr1yyQKp_7FJ5Fhw3kb7NsPj_7JHMjL4IEiOhedlYVv38Yx5DacL-d8fRkhTeOohD9sZSO8G3yYRxKK1CTN01XyBCRKtnGiwae230WqsI9qDzNwi4JN92Xq7I_7ziIvlXCLEnsUSwUlFEUc7d_FPpglKkSfUSC9a_WvZ2g6QN9K6s7VWmQhk4CCySdSHEmeX2-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پست خداحافظی رضا شکاری با چاشنی ناراحتی: خداحافظی همیشه تلخ است، خداحافظی از گوهر کمیابی مثل پرسپولیس تلخ‌تر...
📍
موفق باشی
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/135811" target="_blank">📅 00:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135810">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/135810" target="_blank">📅 00:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135809">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/135809" target="_blank">📅 00:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135808">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
افشاگری جنجالی رسانه عادل فردوسی‌پور از امیرقلعه‌نویی: سرمربی تیم‌ملی قبل از بازی با نیوزیلند تهدید به استعفا کرده و فدراسیون با پرداخت ۱۴۰ میلیارد تومان پاداش به این سرمربی در یک بانک‌خصوصی، قلعه‌نویی رو راضی به ادامه حضور در جام‌جهانی کرده! حالا هیئت رئیسه…</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/135808" target="_blank">📅 00:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135807">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
❗️
#فوری | محاصره دریایی آمریکا علیه ایران از دقایقی قبل مجددا آغاز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/135807" target="_blank">📅 00:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135806">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
گل‌های پرسپولیس در دیدار تدارکاتی مقابل شهدای رزکان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/135806" target="_blank">📅 00:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135805">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
✅
جونم اسپانیا گل دوم هم زد و در آستانه رفتن به فیناله ..فرانسه در آستانه باخت و رفتن به بازی رده بندی ...کیا میگفتن فرانسه اسپانیا رو میخوره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/135805" target="_blank">📅 23:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135804">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
گل اول اسپانیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/135804" target="_blank">📅 23:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135803">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❗️
❗️
مرکز مشترک اطلاعات دریایی به رهبری نیروی دریایی آمریکا :  محاصره آمریکا شامل همه کشتی‌ها، بدون توجه به پرچم اون‌ها می‌شه
🔴
🔴
محاصره، کل سواحل ایران رو شامل می‌شه، از جمله بنادر و پایانه‌های نفتی ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/135803" target="_blank">📅 23:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135801">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
پیروز قربانی: من نیوزلند رو با فجر سپاسی شیراز می‌بردم مطمئن باشید نیوزلند اگه تو لیگ 16 تیمی ما بود، جزو چهار تیم آخر میشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/135801" target="_blank">📅 23:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135800">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
ساعت 22/30 بازی حساس و دیدنی اسپانیا و فرانسه ...پیش بینی شما چیه ..کی می‌ره فینال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/135800" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135799">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
امشب ساعت 21
🔴
شنیده‌میشود؛ باشگاه‌پرسپولیس امشب از پوریا شهر آبادی و ابوالفضل جلالی دوخرید جدید خود در ویژه برنامه‌تلویزیون این‌باشگاه رونمایی خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/135799" target="_blank">📅 22:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135798">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
ساعت 22/30 بازی حساس و دیدنی اسپانیا و فرانسه ...پیش بینی شما چیه ..کی می‌ره فینال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135798" target="_blank">📅 21:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135797">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135797" target="_blank">📅 21:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135796">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6e06b7b2.mp4?token=W9L6z3q8aAWLBjpKBzak_zn2uDoI1X0lMtbD1rHWhZTjvPv0SqvwMk5Jx_QlvwNQG4snMtUqOjQXFeotvyZ7dolXpQtskQQfInL2ldGGedy3UwDdTJimCR5ntokc1efP_5-CDDIArIN6EaX36V8N5QrZ5htzoRswUj7g4xTiVSuj0a1LoRHV4QGv6bL8SNT3kM4ywVNgLMOLj3eeUdn07NrB4e1ULPfge4X_xQVqHIMbkr1xkfe3VPo5e7d7hAGKBNneTdKDYIluCkra0IpGofTLaQLHWduC5IFka_RsKe0dfH5mWEJ8CL9wUamUC71JQoDwRNPSRLTIlkjd-BbP2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6e06b7b2.mp4?token=W9L6z3q8aAWLBjpKBzak_zn2uDoI1X0lMtbD1rHWhZTjvPv0SqvwMk5Jx_QlvwNQG4snMtUqOjQXFeotvyZ7dolXpQtskQQfInL2ldGGedy3UwDdTJimCR5ntokc1efP_5-CDDIArIN6EaX36V8N5QrZ5htzoRswUj7g4xTiVSuj0a1LoRHV4QGv6bL8SNT3kM4ywVNgLMOLj3eeUdn07NrB4e1ULPfge4X_xQVqHIMbkr1xkfe3VPo5e7d7hAGKBNneTdKDYIluCkra0IpGofTLaQLHWduC5IFka_RsKe0dfH5mWEJ8CL9wUamUC71JQoDwRNPSRLTIlkjd-BbP2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/135796" target="_blank">📅 21:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135795">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
جااااااااااان کیسه سوزی باشه؟
😂
✅
جلالی : دربی حذفی خیلی اذیت شدیم و گل عالیشاه خیلی قشنگ بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/135795" target="_blank">📅 21:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135794">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✅
ابوالفضل جلالی بازیکن پرسپولیس: با قلبم به باشگاه بزرگ پرسپولیس آمدم و این تیم را انتخاب کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/135794" target="_blank">📅 21:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135793">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
❗️
خلیلی :
🔴
دیگر مهاجم جذب نمی‌کنیم و با سرگیف، شهرآبادی و علیپور ادامه خواهیم داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/135793" target="_blank">📅 21:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135792">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
محسن خلیلی سرپرست پرسپولیس: برای جذب کسری طاهری باید 200 میلیارد خرج می کردیم که به این نتیجه رسیدیم که قید این بازیکن را بزنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/135792" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135791">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4138202b6c.mp4?token=HYPv3eYLLOY3_ANQOXXuK7DeNSnSz_CUB43LbGA4PTokKYVpEgfzjzUJ8HRML9_Bph3Sq6XuxNHdVuyu3IUYrdQ2Evc9S7hFiynjfWjhPCwG6zowiTapI7Y1kgi_V5LaI-4Fgd5QlORzQ87owTm4IsTqrgevv1VM5RRlelfiQA10SXY35A9kbx4yzSeCtlYtdzI5RhmFVLggTIUGGJqjCK4rfdVa3eUnwzC7N3MNUU1EamQCgIDOBJCWOEu8yyNMjOyl41UQzS1JcwVfhRxKIg83Xlj18pzhJEVDu3pOlKwRnXtJSrQGvkyE6cr9iP3CJ_1iZdvU1uevbKINM-Q2Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4138202b6c.mp4?token=HYPv3eYLLOY3_ANQOXXuK7DeNSnSz_CUB43LbGA4PTokKYVpEgfzjzUJ8HRML9_Bph3Sq6XuxNHdVuyu3IUYrdQ2Evc9S7hFiynjfWjhPCwG6zowiTapI7Y1kgi_V5LaI-4Fgd5QlORzQ87owTm4IsTqrgevv1VM5RRlelfiQA10SXY35A9kbx4yzSeCtlYtdzI5RhmFVLggTIUGGJqjCK4rfdVa3eUnwzC7N3MNUU1EamQCgIDOBJCWOEu8yyNMjOyl41UQzS1JcwVfhRxKIg83Xlj18pzhJEVDu3pOlKwRnXtJSrQGvkyE6cr9iP3CJ_1iZdvU1uevbKINM-Q2Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوالفضل جلالی بازیکن پرسپولیس: با قلبم به باشگاه بزرگ پرسپولیس آمدم و این تیم را انتخاب کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/135791" target="_blank">📅 21:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135790">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e350a78f3.mp4?token=OzD-a9PJ9dHyteuzSHoo2ndyJFn2RLopZc6UTMoWFTLPsY97lEeHhJKZNQxqi6fxmVimQUS0Ah25L98O9hDoiksGtz4gun-37l0yMolcgf3mEnh3H96qniTVBFiA6RcBsXRTppot0swrrjnaEXRDIaiOnWyxkey8LbLT2nVTi8Oj_3CDR-SHfI63zJEtmglVz-A9eaejhDfIOGCuWPNjrm7i3w3HaRk4WjnToZkXx7_4-IxBIjk_NgrCjve9-gfT1RHhQLDJrj3reP-67sQYWo6DdKigMpf0zop0-yxAUkcmGigGB5q5lQOTMhRYgt7ffCPg4S3VccwjLaRv9563iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e350a78f3.mp4?token=OzD-a9PJ9dHyteuzSHoo2ndyJFn2RLopZc6UTMoWFTLPsY97lEeHhJKZNQxqi6fxmVimQUS0Ah25L98O9hDoiksGtz4gun-37l0yMolcgf3mEnh3H96qniTVBFiA6RcBsXRTppot0swrrjnaEXRDIaiOnWyxkey8LbLT2nVTi8Oj_3CDR-SHfI63zJEtmglVz-A9eaejhDfIOGCuWPNjrm7i3w3HaRk4WjnToZkXx7_4-IxBIjk_NgrCjve9-gfT1RHhQLDJrj3reP-67sQYWo6DdKigMpf0zop0-yxAUkcmGigGB5q5lQOTMhRYgt7ffCPg4S3VccwjLaRv9563iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوالفضل جلالی بازیکن پرسپولیس: امیدوارم امسال بتوانم دل هواداران پرسپولیس را شاد کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/135790" target="_blank">📅 21:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135789">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46267f8866.mp4?token=GkmJeIgR8CDFTmfijJvHfuqwbViHdR3nBRO0MqxAHf3uxXq6J9MIwERCDfFrCbbhei-DOoholwJm-UH1I8hVT-_8Lv31vdKPzi0YOOsTRJYdSUfAKeJSjGadDeR3havqfedqapOFAak36vnrinjEU5uHnJIliZgmfnYcvPnD59iFLtR-_L9aH6_cGR7DS4oZpj8PlkLxcdC2R-53l_YsTqeA9opti_NRcoAyeFY57R4TN-kTu_GE2fd8IZYZqOu_cfoOCTXe0RPTPw74KZxoTtzagiteoQyplK_Isbm9lSnLyBrrFMvYdedBnc6kxpmSv5grqo_l12k-fRuZNxA7YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46267f8866.mp4?token=GkmJeIgR8CDFTmfijJvHfuqwbViHdR3nBRO0MqxAHf3uxXq6J9MIwERCDfFrCbbhei-DOoholwJm-UH1I8hVT-_8Lv31vdKPzi0YOOsTRJYdSUfAKeJSjGadDeR3havqfedqapOFAak36vnrinjEU5uHnJIliZgmfnYcvPnD59iFLtR-_L9aH6_cGR7DS4oZpj8PlkLxcdC2R-53l_YsTqeA9opti_NRcoAyeFY57R4TN-kTu_GE2fd8IZYZqOu_cfoOCTXe0RPTPw74KZxoTtzagiteoQyplK_Isbm9lSnLyBrrFMvYdedBnc6kxpmSv5grqo_l12k-fRuZNxA7YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محسن خلیلی سرپرست پرسپولیس: برای جذب کسری طاهری باید 200 میلیارد خرج می کردیم که به این نتیجه رسیدیم که قید این بازیکن را بزنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/135789" target="_blank">📅 21:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135788">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
شوک به استقلال: آسانی فسخ کرد!
🔴
یاسر آسانی با ارسال نامه‌ای رسمی به باشگاه استقلال، به دلیل پرداخت نشدن مطالبات فصل گذشته و پیش‌پرداخت قرارداد فصل جدید، فسخ یک‌طرفه قرارداد خود را اعلام کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/135788" target="_blank">📅 21:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135787">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
یاسر آسانی قرارداد شو با استقلال فسخ و ایران رو ترک کرد / فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/135787" target="_blank">📅 21:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135786">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
✅
خلیلی: ما اصلا کسری طاهری رو نمیخواستیم و از لیست خریدمون خیلی وقته خارج شده
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/135786" target="_blank">📅 21:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135785">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
محسن خلیلی با کسری طاهری تماس گرفته تا در تمرین امروز پرسپولیس شرکت کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/135785" target="_blank">📅 21:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135784">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
بیفوما به‌خاطر کشیدگی کشاله هنوز تمرین نمی‌کنه. بعد از اینکه برگرده، تارتار کیفیتش رو بررسی می‌کنه و اگه راضی نباشه، توی لیست فروش قرار می‌گیره.
✍
خبرگزاری آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/135784" target="_blank">📅 21:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135783">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
#تسنیم؛ پرسپولیس سفت و سخت افتاده دنبال علی نعمتی و میخواد با یه جلسه حضوری کارو تموم کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/135783" target="_blank">📅 21:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135782">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/135782" target="_blank">📅 21:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135781">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/135781" target="_blank">📅 21:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135780">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❗️
فارس؛ پویا لطیفی‌فر هافبک گل‌گهر در لیست خرید تارتار قرار گرفت
😐
❌
پ.ن از گل گهر بکشید بیرون ناموسا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/135780" target="_blank">📅 20:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135779">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❗️
فارس؛ پویا لطیفی‌فر هافبک گل‌گهر در لیست خرید تارتار قرار گرفت
😐
❌
پ.ن از گل گهر بکشید بیرون ناموسا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/135779" target="_blank">📅 20:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135778">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❗️
فارس؛ پویا لطیفی‌فر هافبک گل‌گهر در لیست خرید تارتار قرار گرفت
😐
❌
پ.ن از گل گهر بکشید بیرون ناموسا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135778" target="_blank">📅 19:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135777">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9K0fWSXyvz4KAVSRpe9Zlba8rw08dorPfB1NAV702g4__TeDGUHzXSReGNynF5djKji9mRekno3dcXXKLWUV2BKiTqih8JdwTieSgKcMj6YHiNSCnciBKASNushTjtANFUaCwTxfhnaMM-VJUu4ibSemZy5YvOaRetptCvg74tS_6vDFhmgiYKOdNWDLpfIafUiQXWCvvwuxapRAYW_rNUXvPnSoCUkUM7HHKGo-f6t07pdd0WFb5n1ysyMaZzqtlzKF7bolcxGNCgdOrKOu74hBnjrRJl5Pm6TYgPvLbiRJ8xEcPUpJpPrlY_20qdBKpjSPwY0LWA_ttlq2CjqnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
فارس؛ پویا لطیفی‌فر هافبک گل‌گهر در لیست خرید تارتار قرار گرفت
😐
❌
پ.ن از گل گهر بکشید بیرون ناموسا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/135777" target="_blank">📅 19:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135776">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join
Join Join Join</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/135776" target="_blank">📅 19:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135775">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxdowrHDRSlyAl0FaMMkLkxL4vmcbI4MAaGPfNiASuIdGYWr07O_SMKM2y8SqbtbqDuLE5Hgxr0EoaQ9LiLQBU89LVCrWvtlcOstN0okECeis3Nk94ztHoJFjWodD5K4RYlV-jlM0TKW_83L2fWjPL5jl8vVOW1_jKlq8-13u0JmYEfQWtDcaMPBYdriYy_1nRq_izbcHf2S0TaZ6tTiM_75VWbTgiqzNejuOCZYIk4AJTi8VHLoG-JIaEi3NDi27tAPCf3ZNEozOGt690v1qRAc1ek5zHdbr18efPwA0OARFpuhMtNNfef1NFbtxHy_IXC_62er5bhXEquIcCX_RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکسمون عالی برد شد
✅
💵
✈️
@Bet_Giantss</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/135775" target="_blank">📅 19:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135773">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb37226cd2.mp4?token=EnlfD9qzpICKV8BgJU8Tst1WzrK3bJ8pESixvapDtcwAIjT1pKsp_qwLIPCOqL4nsnwzg-SkFBlTAed0n5J1azIHpuHdjUuhdtFj6xyk-9i0HLeUX3CdKN1raDANnA_YIQWhNfvGI6HENvOI-84O3IrwmWCv-Xrlr03QpFsofbnzFuMJm3p-1ElbEK0xyYHTYSjOo0XWxsilzhBY6VMZnPj36DW4k0iuXHAoC6h5X-6taY37I1-JL8tZ4DV2dzXkQKniexfiPRuASFIso5oJGJN0VuqBdr-dKN2e6qpmBfV3SrwYFVsT9ElA2MBBCOgZ4okKFduWULrVg-t-o-mcm6LidtQGsc_MiXQVIT9YTyn6hpZ9AfYCaeBDWnHNHWnso1VieUgj2q2eEpq2sRiNPBiK4n_od3fDEArmyQ95fh2hUgLzHjKPA4rYMKbnu8Zd43ytwJApmDgacK_w_uuvL9isvljkiteOAEFRF_IeZ51igy19nExMntqRwMtDH6cJsIVj2TMEhJJ9O_X4HG0j2MAADq29l6pBWIR4L2AUzZD3kMVXnyb7JPmebMxFkxJP3wCQINB2O0pToYFjYZ6VNoi9W2GTZ9gdxqAFZKUBa_SSsLec9yQ8JiRkktkQ_jTIUvukx6KSpZaY4MG5pSDyWBG-iMaCNa68XIWGHvdDCpY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb37226cd2.mp4?token=EnlfD9qzpICKV8BgJU8Tst1WzrK3bJ8pESixvapDtcwAIjT1pKsp_qwLIPCOqL4nsnwzg-SkFBlTAed0n5J1azIHpuHdjUuhdtFj6xyk-9i0HLeUX3CdKN1raDANnA_YIQWhNfvGI6HENvOI-84O3IrwmWCv-Xrlr03QpFsofbnzFuMJm3p-1ElbEK0xyYHTYSjOo0XWxsilzhBY6VMZnPj36DW4k0iuXHAoC6h5X-6taY37I1-JL8tZ4DV2dzXkQKniexfiPRuASFIso5oJGJN0VuqBdr-dKN2e6qpmBfV3SrwYFVsT9ElA2MBBCOgZ4okKFduWULrVg-t-o-mcm6LidtQGsc_MiXQVIT9YTyn6hpZ9AfYCaeBDWnHNHWnso1VieUgj2q2eEpq2sRiNPBiK4n_od3fDEArmyQ95fh2hUgLzHjKPA4rYMKbnu8Zd43ytwJApmDgacK_w_uuvL9isvljkiteOAEFRF_IeZ51igy19nExMntqRwMtDH6cJsIVj2TMEhJJ9O_X4HG0j2MAADq29l6pBWIR4L2AUzZD3kMVXnyb7JPmebMxFkxJP3wCQINB2O0pToYFjYZ6VNoi9W2GTZ9gdxqAFZKUBa_SSsLec9yQ8JiRkktkQ_jTIUvukx6KSpZaY4MG5pSDyWBG-iMaCNa68XIWGHvdDCpY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
شهاب زندی: برای فروش ایری قرار است هیات مدیره تصمیم بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/135773" target="_blank">📅 18:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135772">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
میلاد محمدی همچنان تمدید نکرده و اخبار قطعی شدنش کذبه اما توافق داشته/ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/135772" target="_blank">📅 18:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135771">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
پاسخ چمران به سوالی درباره قطعی برق بدون اطلاع قبلی: اگر می‌دانستید دو روز پیش چه تعداد تاسیسات برقی را زدند دیگر این سوال را نمی‌کردید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135771" target="_blank">📅 18:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135770">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FK1A8q9i9p1aBBhF_EOmsANWxYiGw9YOvkQzR0Fn0QuruyGcYbQFdhB1S5LaTDh7wtjoDhPXFYJa37Zw37BxbEHz15eRyArkDb0ZNqHIZPAVfz_Yj9vtEu5ilO2QrBiSmAyzAt_1QdEwfzd5jdeVt9C8Br1Om4HxootwATPT0aFewLQ-MG_8KfoEdENt9Dr8nDB8XBLc7S0u4aVLQJPYS4kYHIDFP1hgDwITwInnCGEyfzsp0FAUgsxSWuCOokfmYiiocf0zGANY9ieuwAe3g5TiGEZnZJv2W7_ZoS1dPp6axCBaH2AhP_BbhNlotvXbQHTSZqGEEXPwPSDM4-f1Ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135770" target="_blank">📅 18:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135769">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de17a51b64.mp4?token=PiBgEzg-UOmdv6S3O_9NHZfvI3N41Pd2nNBeiUs-XGLXWCWb3oKzzzxs5yjZaj98TcNbemePTkBcDJv12MyH5wEMXEzPTXFgLR-Jj58r7lwlRRwQXc2bTEIEQy5Fwylq_H6FKNUEdS69SHcJhsa6xaeCMB0fg9QlJVS-FTtxNktV5FnKuQLTxVdM0ZxhXpMhTe8yKdm7FfssSeCpK7Y-tydm4TcNz_gGS3pdICIEnND7vOx5Hf3wWialOKnhhGMlVPECHbL9xKBnKLnATV8E6RR1MNe7sh65cr1RRlmeHRZmAjILM5bm2P-VdOMLMOxVzt-EVJgH9M6EI5x43-JkLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de17a51b64.mp4?token=PiBgEzg-UOmdv6S3O_9NHZfvI3N41Pd2nNBeiUs-XGLXWCWb3oKzzzxs5yjZaj98TcNbemePTkBcDJv12MyH5wEMXEzPTXFgLR-Jj58r7lwlRRwQXc2bTEIEQy5Fwylq_H6FKNUEdS69SHcJhsa6xaeCMB0fg9QlJVS-FTtxNktV5FnKuQLTxVdM0ZxhXpMhTe8yKdm7FfssSeCpK7Y-tydm4TcNz_gGS3pdICIEnND7vOx5Hf3wWialOKnhhGMlVPECHbL9xKBnKLnATV8E6RR1MNe7sh65cr1RRlmeHRZmAjILM5bm2P-VdOMLMOxVzt-EVJgH9M6EI5x43-JkLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بیژن طاهری، سرپرست کیسه، بعد اینکه یاسر آسانی به فرودگاه رفته و ایران رو ترک کرده، رفته راننده رو مثل سگ کتک زده و گفته چرا بدون هماهنگی باشگاه بازیکن رو بردی فرودگاه!
😳
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135769" target="_blank">📅 18:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135768">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
شایعات؛ جهانبخش عصر امروز با مدیرای پرسپولیس جلسه داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/135768" target="_blank">📅 17:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135767">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
ادعای فرهیختگان: محمد عمری از لیگ قطر و امارات پیشنهاد داره و ممکنه باشگاه با دریافت ۶۰۰ هزار دلار از این تیم‌ها رضایت‌نامه عمری رو صادر کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/135767" target="_blank">📅 16:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135766">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❗️
فووووووووووووری
✅
قرارداد برای میلاد محمدی ارسال شده و تا ساعات آینده ممکنه اعلام بشه/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/135766" target="_blank">📅 16:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135765">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b882d31c48.mp4?token=AK7QviMgntoH5f5he4ZdF6txEWAkH6IrvSGlPiVOLnZJqUL9qc4z2tgYdym_n4A8Fyp0EJSCLTMHp2CDenPSGlZhbR1F0MTz9EKQYxAhDTw_-_FxaZOtq5l1OytvyEFrRLG2HKa7-7l3p7aRR3nqLIK5j3Qp73_E88gyOqMycRhahbhApV8nvt_lhHw1ijP3RwEui05z7LV6UDCfPfl_uPotOcrODn3qib6XarVZmLPUFvdN8trpyXS8XlL-pISdLzxKFlRou27fw9Izyd4FvveBePWHrhKodR8T_oh4nrr00yPxwnJdG_lP6N6kmbGNIt055HO2mKRSrfXbP4v_Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b882d31c48.mp4?token=AK7QviMgntoH5f5he4ZdF6txEWAkH6IrvSGlPiVOLnZJqUL9qc4z2tgYdym_n4A8Fyp0EJSCLTMHp2CDenPSGlZhbR1F0MTz9EKQYxAhDTw_-_FxaZOtq5l1OytvyEFrRLG2HKa7-7l3p7aRR3nqLIK5j3Qp73_E88gyOqMycRhahbhApV8nvt_lhHw1ijP3RwEui05z7LV6UDCfPfl_uPotOcrODn3qib6XarVZmLPUFvdN8trpyXS8XlL-pISdLzxKFlRou27fw9Izyd4FvveBePWHrhKodR8T_oh4nrr00yPxwnJdG_lP6N6kmbGNIt055HO2mKRSrfXbP4v_Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
این چیه برا نیمه نهایی ساختین آخه ناموسا
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/135765" target="_blank">📅 16:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135764">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
❗️
#منهای‌پرسپولیس
🔹
سینا اسدبیگی و محمدرضا سلیمانی با عقد قراردادی یکساله به دهوک عراق پیوستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/135764" target="_blank">📅 16:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135763">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYxDZaTyu54_IGeGNRdtBvALACD7A6c5PpjeaPY5sWdwCgNEUMjOwHTrVfnaYF3ZclKdz5sYu-ZdRb7gr1TmOLjN0kKd6VTYzOP_o6-6eAZ2CM5frDaZjZuO1Xa12CJTb6q1D6_kynkx8Gpu9cJTrg_sCLAWkN9ne9AbZy_BZp0hQQtZ7B8LAsgg_35pP_Kfli3cjaLJ24Gfagaaz83GWw43fBvRoDSbwc_DhYhJQMet_HtVg6gCRAPSaI2l3wDEiXf_hP7QpIddRY3P-oIS66K4id9jRFKlgOpsLH_YW-_YSENSI7CQlsSQtpdZ1gnZqO7fiGS1VCUrC8rhbQI71g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیروز تو بازی دوستانه امیررضا رفیعی بازی نکرده و گندمی جوون نیمه دوم به میدون رفته
🔴
به نظر جدایی رفیعی قطعی شده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135763" target="_blank">📅 16:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135762">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔹
عضو هیات مدیره باشگاه پرسپولیس استعفا داد
🔴
علیرضا اردوبادی عضو هیات مدیره باشگاه پرسپولیس، از سمت خود کناره گیری کرد.
🔴
علیرضا اردوبادی در ۱۸ آبان ۱۴۰۴ به عنوان جانشین سیامک جلوه به عنوان عضو جدید هیات مدیره باشگاه پرسپولیس انتخاب شد و بعد از اینکه پیمان…</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/135762" target="_blank">📅 16:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135761">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/135761" target="_blank">📅 16:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135759">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
تسنیم : رضا جباری با مسئولان باشگاه پرسپولیس جلسه داشته که ؛دو طرف در این جلسه به توافق نهایی دست یافته‌اند و گفته می‌شود جباری به زودی در تمرینات پرسپولیس حضور پیدا می‌کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135759" target="_blank">📅 15:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135758">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
🎙
علیرضا جهانبخش: می‌دونم که بین پرسپولیس و استقلال لباس کدوم تیم رو می‌پوشم اما الان نمیگم. پدر و مادرم طرفدار یه تیم هستن و هرجا اونا بگن، میرم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/135758" target="_blank">📅 15:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135757">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
فوری :پرسپولیس برای جذب رضا غندی پور اقدام کرد /خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/135757" target="_blank">📅 15:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135756">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbSaZ3VQsHAn8pIC8V2RYhfQ1N2FvJrd5tag8fzjA_VSEe7ZCGabBT5o6PJvBTT4TZdX7FITpcA1i9PAeH20zYgsi8qMDY5OZi0XP7ixQO-QKZEXM-lj0eTDetUBaBQCCKfiASgZiCRxZ73DDK7vl0zroZ5ZJjGFIEbpMbNLm-PA-9kVKN8g7sgz8RlzYgmrAH2rh2Wk0itFYIt1BV5BZJu4GNrVEaeXtC0WuoiJMIcTfLKfXsK7n0hjfIy9CA4pcg4H_im7UpzG56Lm-Rqy2wLF_635c1G5Y8DqcOvPuEVhT6L0W9JsyQoulUPfVx_CWcKL3ljlP0Wgwh8KnooX3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
افشاگری جنجالی رسانه عادل فردوسی‌پور از امیرقلعه‌نویی: سرمربی تیم‌ملی قبل از بازی با نیوزیلند تهدید به استعفا کرده و فدراسیون با پرداخت ۱۴۰ میلیارد تومان پاداش به این سرمربی در یک بانک‌خصوصی، قلعه‌نویی رو راضی به ادامه حضور در جام‌جهانی کرده! حالا هیئت رئیسه فدراسیون از رفتار قلعه‌نویی حسابی شاکی شده و قصد داره این مربی رو برکنار کنه مگر اینکه تاج مانع بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/SorkhTimes/135756" target="_blank">📅 14:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135755">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/135755" target="_blank">📅 14:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135754">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
ورزش سه :
🔴
بالاخره پرسپولیس و میلاد محمدی  روی برخی نقاط به اشتراک رسیده‌اند و به این ترتیب احتمال دارد در روزها و حتی شاید ساعات آینده قرارداد مدافع چپ ملی‌پوش پرسپولیس تمدید شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/135754" target="_blank">📅 14:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135753">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
تاخیر ۷ تا ۱۰ روزه لیگ ۲۶؛ فصل جدید فوتبال اواخر مرداد شروع می‌شود
🔴
🔴
براساس اعلام سازمان لیگ، در شرایطی که قرار بود فصل جدید لیگ برتر فوتبال از ۱۶ مرداد شروع شود، این مسابقات با تأخیر  یک هفته‌ تا ۱۰ روزه از ۲۶ یا ۲۷ مرداد شروع می‌شود. گفته می‌شود علت…</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/135753" target="_blank">📅 14:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135752">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUMUQDxDXgifJ3spWUnsBQgita2-tnfRD4WXXWa8eZ8y1VL2bBTs9QwAIEH5nu-hMhFZxImiFhldd4bPRfnY11bA62-9b1Oyv1cgfZkS-tmVMMlRGXattwExw6cGiOMS5YeJexm2nvgBW6tmDAT2uCRqRXamLCmEpK_GK5KzINjqNVwxj6Wf_kz0j59laQSnMcr3rwrIJtCtJNBaisc4Y9gXcpqALM5AY7VtN6zovJsCr41QECJE89dNF4prYYVhsO-MHasnUwWBEKQu_kr5aN7TQwKGUvBVzIdiLtdidwRRraQ1Tfl-mJ0rF9ut35GFaE7gsBa8ul7APXaWIfICmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تمرین امروز سرخپوشان در سالن وزنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/135752" target="_blank">📅 14:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135751">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
میلاد محمدی نتونست تیمی از اروپا پیدا کنه و احتمال زیاد تمدید میکنه / طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135751" target="_blank">📅 13:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135750">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🟡
علی کریمی با عقد قراردادی رسمی به سپاهان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/135750" target="_blank">📅 13:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135749">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
✅
فوری؛ با اعلام سازمان لیگ، برگزاری لیگ برتر در اواسط مردادماه لغو شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/135749" target="_blank">📅 13:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135748">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❗️
کسری طاهری مهاجم جدید نساجی: من اونشب تو شوک دعوای آقاخداداد باجواد خیابانی بودم که به یک‌باره‌رسانه‌ها خبر دادند که پیوستنم به پرسپولیس منتفی شده. بله از الان به بعد بازیکن نساجی هستم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135748" target="_blank">📅 13:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135747">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/135747" target="_blank">📅 12:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135746">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✅
💢
احتمالا علیرضا جهانبخش جانشین امید عالیشاه در پرسپولیس می شود!
🚨
جهانبخش جدا از عنوان یک بازیکن برای پرسپولیس قرار است سفیر تبلیغاتی بانک شهر هم باشه و پول خیلی خوبی قراره بگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/135746" target="_blank">📅 12:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135745">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
امشب ساعت 21
🔴
شنیده‌میشود؛ باشگاه‌پرسپولیس امشب از پوریا شهر آبادی و ابوالفضل جلالی دوخرید جدید خود در ویژه برنامه‌تلویزیون این‌باشگاه رونمایی خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/135745" target="_blank">📅 12:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135744">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrYhv_bo53wng5_Y1hCo9mDNLD3xkk3LmrbOeVViQ6rR7sU0Y2DPCAL2Ah8610pO08e3O_ml8H_BZY5qdvRheKfgJrSA1duNzStyyLWv4IywsGK8uR9KbC8jt-_zX6MlZ9dUe8aKKLzeJ_D-ZY8RzqHjzxhVB5b2O3t_4RHvdgso1EeOy3rk1PRDM9FIkG_GZvSsqmUQam-3NlyVmjw71NA11ZLKsYc0MxFovzKrAW8QhtqyfDVigquN1NQr7yLGZh19RqUie3pihBj9MIqPv0cYxMF6T1jqIqqd8nmE7GA7bfHb5HISwVKsv4bCwE8szOV5AedqNidDt5unBNbc-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/135744" target="_blank">📅 12:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135743">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✅
✅
جذب ایری برای پرسپولیس در یک صورت ممکنه که نساجی بدون دریافت یک ریال این بازیکن و به پرسپولیس قرض بده که احتمالش صفره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/135743" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135742">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936ce7543f.mp4?token=IqtrrOyLJKVxyoqZZAGGLE_8pG6sFotxPu6khnM9yy4quFMiMfdnj5HwXPuwNE-RbVFfRr3IcjK65McuWb2tyjeUUaVRGmZL0QRtctaaV6UTtE349O-RuOgWnl1Ho_h7oF_iGouEauE2B_24M8uUIw3tktJZZKaU1L870qxJG-e7Zmx6t-1B3ADqRlvqggAP2uy7rcxOOiQ1tXsgkTDqzZ7cioXk77RZ4amWhVQhUU7Qu8M-tCklQo0TWTqfAT0S52XEXGOvD_6nFSdQJOmRzjUjFDnVg1wGokxz1t6pNWHcmBX4rO2Fur4zLw-78CTSuvAbZtIEUR6M2PtifGXLyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936ce7543f.mp4?token=IqtrrOyLJKVxyoqZZAGGLE_8pG6sFotxPu6khnM9yy4quFMiMfdnj5HwXPuwNE-RbVFfRr3IcjK65McuWb2tyjeUUaVRGmZL0QRtctaaV6UTtE349O-RuOgWnl1Ho_h7oF_iGouEauE2B_24M8uUIw3tktJZZKaU1L870qxJG-e7Zmx6t-1B3ADqRlvqggAP2uy7rcxOOiQ1tXsgkTDqzZ7cioXk77RZ4amWhVQhUU7Qu8M-tCklQo0TWTqfAT0S52XEXGOvD_6nFSdQJOmRzjUjFDnVg1wGokxz1t6pNWHcmBX4rO2Fur4zLw-78CTSuvAbZtIEUR6M2PtifGXLyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برای طارمی چیکار کردی ؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/135742" target="_blank">📅 12:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135741">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
مراسم رونمایی از مهدی تارتار امشب ساعت ۲۱.۰۰ برگزار خواهد شد و از شبکه اینترنتی باشگاه پخش میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135741" target="_blank">📅 12:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135740">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
👀
شایعات: حدادی امروز با علیرضا جهانبخش جلسه داره!
❗️
❗️
پ.ن: طبق گفته خود جهانبخش مقصد آیندش تا ۲ هفته آینده مشخص میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/135740" target="_blank">📅 11:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135739">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVaeaOJ4gvzxYyhbCz4WF9i_6h3YgdJKGH7hbeNYno7rKESeof6Y7XmdRRKTPnMLZXcwq-QpkgUE9uSrKHqKodmjDmZkZ4Y6KsKNQvJ3am7-HxKPutQtQ3nWv1frgVYyd4CDK-YWUdJ7-IxmCsOtMUljSbAefRnxczgl2M0OSZLYOFuU5rm9XlGd0egXIHuUhkmkBWh0uZqaU_zEg_z3LXQnRJJ0zf52ME9OM4jvk5Y4xD3hd1tkhvKfZNVnZ3Nldh5Ok7JTLy-bIMBpjgx0Ad4hqaMtTubpcID6rPVoxSWiUtYfNLRNucW3Ew_glUMl188bOwn1QnH8gYdWyv2RCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
شایعات: حدادی امروز با علیرضا جهانبخش جلسه داره!
❗️
❗️
پ.ن: طبق گفته خود جهانبخش مقصد آیندش تا ۲ هفته آینده مشخص میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/135739" target="_blank">📅 11:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135738">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
✅
فوری از فرهیختگان: قرارداد پورعلی امشب نهایی می‌شه و از فردا به تمرینات تیم اضافه می‌شه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/135738" target="_blank">📅 11:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135737">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/57cf9a082f.mp4?token=pexUzFDKJtP47Xvh-XbVfcdI0hHYAvF1ly55BZYmpcH-nrMAMVvsyiXY_6e7Z6AcEMzddyUtFSGyVnzrrCcb2CXMmINZFqEk1KwC9qGyOWuMK_lIvd4FmFR3l3cFnMDjWsVC1wB001zDmF9yEzsK94s6xuHUoOEaAzm6vJK-KQD60gl1Zpu21GRPc7i_XAfaB_o4YppMAratHnMuJRXDWrOzlaG7sDSt1hsoPlTHq0AvNkPJrZl5AprWvFoLYhTgbWejnVVYFU8AKQeA1rh2VI4trFZVnS3petJ4T3H5IM7h2UYE8p_ZJKblKzBa47SGZ-XKC5JSIAfLzy1IYUgz9g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/57cf9a082f.mp4?token=pexUzFDKJtP47Xvh-XbVfcdI0hHYAvF1ly55BZYmpcH-nrMAMVvsyiXY_6e7Z6AcEMzddyUtFSGyVnzrrCcb2CXMmINZFqEk1KwC9qGyOWuMK_lIvd4FmFR3l3cFnMDjWsVC1wB001zDmF9yEzsK94s6xuHUoOEaAzm6vJK-KQD60gl1Zpu21GRPc7i_XAfaB_o4YppMAratHnMuJRXDWrOzlaG7sDSt1hsoPlTHq0AvNkPJrZl5AprWvFoLYhTgbWejnVVYFU8AKQeA1rh2VI4trFZVnS3petJ4T3H5IM7h2UYE8p_ZJKblKzBa47SGZ-XKC5JSIAfLzy1IYUgz9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاسخ چمران به سوالی درباره قطعی برق بدون اطلاع قبلی: اگر می‌دانستید دو روز پیش چه تعداد تاسیسات برقی را زدند دیگر این سوال را نمی‌کردید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/135737" target="_blank">📅 10:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135736">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
فرشید حقیری :
🔴
احمدنور امشب با احمدی مدیرعامل بانک شهر داخل‌ تهران جلسه داشته .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/135736" target="_blank">📅 10:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135735">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
استوری جدید فرشید حقیری در مورد احمد نور: قراره شده احمد خودش بره رضایت نامه بگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/135735" target="_blank">📅 10:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135734">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b1608df5b.mp4?token=sg_fkSpuAtt4cNsM9JiRwMrXUmchmHB1CkGyocpJrjH4KGL3TH9DRgebBdTneFfBLG7AtejrkAD70UopbCUipfek2Enzj3IyFE90OYbNHklJWrtq1We2RFKCvuMSyNQNfZigv9zo_KsM8NhnyH-h-yniXFezkENss6BDELN6lqa1sVUEtsc8dtvaTzhqGgFv4GZqNLiM4DNW5lI0aOCN3YnwMk-LG3qcvcIQ8XYIXCbKR9b752-APObrzrGg3Ga1pwwjH427yEYuEusd5kb5kFrShQuoEmEXgq3kdKUIWkvEMH4_NIxEVHnEucgoOg4sGjZBEoQKehqD_ECJvL1PnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b1608df5b.mp4?token=sg_fkSpuAtt4cNsM9JiRwMrXUmchmHB1CkGyocpJrjH4KGL3TH9DRgebBdTneFfBLG7AtejrkAD70UopbCUipfek2Enzj3IyFE90OYbNHklJWrtq1We2RFKCvuMSyNQNfZigv9zo_KsM8NhnyH-h-yniXFezkENss6BDELN6lqa1sVUEtsc8dtvaTzhqGgFv4GZqNLiM4DNW5lI0aOCN3YnwMk-LG3qcvcIQ8XYIXCbKR9b752-APObrzrGg3Ga1pwwjH427yEYuEusd5kb5kFrShQuoEmEXgq3kdKUIWkvEMH4_NIxEVHnEucgoOg4sGjZBEoQKehqD_ECJvL1PnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چمن ورزشگاه آزادی جمع آوری شد. پس از پاکسازی زمین و ضد عفونی ‌کردن آن، تازه کار اصلی آغاز خواهد شد. یه چند ماهی نمیشه ازش استفاده کرد 1 سال گذشته و اینا فقط دارن بازسازی میکنن ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/135734" target="_blank">📅 10:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135733">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">📸
تارتار در بازی دوستانه امروز به همه بازیکنان فرصت بازی داده حتی وحید امیری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/135733" target="_blank">📅 10:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135732">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
فرشید حقیری :
🔴
احمدنور امشب با احمدی مدیرعامل بانک شهر داخل‌ تهران جلسه داشته .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135732" target="_blank">📅 09:53 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
