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
<img src="https://cdn4.telesco.pe/file/NCpguSLUrZnZg9KR1pqg7bTN9QTlBwtXtrr7ymrnvDI7NyxcPiyqorqxCxH1CGoLDTBZI_5pTV9_28DZOLD6IhSNVJiWpgqc9xdSqRmSBaI-UrwXyO60d0scnLXeS7uIAAFnk9aho3TJeYXdgFxB2zFORXP4NS-eRFuUi6KXs0JMtFiwEz5fD9QuO6nn3dynE-qWiZjP3V7NT2h0nIm5PEozOIJxEVUdkaTU8qc44PJbkpUrgIgQo9vE040FmD-4FYPBTajAvCoZKA3XWif_tuuAbNylQJZEpID6bwEPCLoHKFnfjKi8mVmWwBCeUSF4jof9_6-jL55Lq_APclE3cA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 262K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 02:39:50</div>
<hr>

<div class="tg-post" id="msg-84527">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9mj-EaGoXN6P7BuInaeCBaTvtjYVn3K6cn7Uwx1ndEIPY9XG6sSMZ5zfIlWFrrgWCNbiOLBIo-GciwmTebTSgJboq2pkyH_ysLcMXk3jpy3TJ8o5oqfNCavyVgPIQ65wvF7pwdDaC3pfdlc2emcLZpi0qBuN6RvUm9ZVacrcYWSefwCndwHO5Ra8EMj-eAjrQ2SQZ-ahod1Qwss3b8QPYnXoO2C15nWE3cPjkl00rbyj2iB25IU0akJDEJfsotJ3bpiOk9YOed3yD1Ts_w28aGlNk7G_3r3bFTqqAtouVmgikzsEcBanGH-UH-lzIOfQk8C8wsMGOFym52uvrmgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحنه رو پسر</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/funhiphop/84527" target="_blank">📅 02:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84526">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اگه خداحافظی مسی هم مثل آخرین کنسرت ابی بشه چی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/funhiphop/84526" target="_blank">📅 02:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84525">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">شوخی بسه دیگه حاجی، وقتشه بیایید بگید مسی تازه ۲۵ سالش شده و نیم فصل برمیگرده بارسا</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/funhiphop/84525" target="_blank">📅 01:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84524">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vn7fkpUzzmXbBx-W-8JDArEuJoLr2QUMNHqpZHCYpc7fMXMAFsEIRtwax9O7I-CkYbt1CutE_Xm0eEsqudWNBtoFQPeV-6N0GufmiVPpvx6CXN2VRTfbNAe6TMW7eUtwtg3kaUjiCBMMbUjyZtRGOZAqNM55gS1In2mqTMi7Xqt3nkg7XmukaAKS26jUwo6C1YIVqlWUfkV4cxcMEXQAeN9It_6hxBcZCVNy2HV5VCH0E6QMmrwGg_lTumG7BA2R4MlpBtz96TKiFgCgLsLFKF_3AYcyYwm7xmXTo0DqsIX34S3VR_OlVZvLHFj5Fhm6bT6kzh9-JbXZjMlpYaUspQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاهی که امشب آرژانتین توش بازی میکنه یک ساعد قبل بازی:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/funhiphop/84524" target="_blank">📅 01:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84522">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شما براتون مهمه که تتلو عفو خورده و برای ازادیش باید تتو هاشو پاک کنه؟  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/funhiphop/84522" target="_blank">📅 00:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84521">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHedWoL9-WjW4YbJO1CMFpAM_Fgk2cYxZ3_ojsHKCDkORlS_rU8_-xZ_pzfemVljmWu--5pNwQT9mgEsxY5TX_pIRBBL8SyJs_2AHoGNEH6UL5tYl2xze3ikjXJLH7_jljdtJOOApgeoLfYwnQUDyg98Sv5OLFCVNLSoUYyD8aICDHu7BCyGfmfQBfYTzKi314TzJXxvCVvqcD2wR-oeWF3_egW3PGSw-csGG2blsHa4Nrl-L1gXYlKb6EptNKkRH3vTcImhGOSgUamdGhhn7nP2ky4dbgxQ4xUWACjWab2nkWztzI4yWDSdqai6nh8jcEILv249M45hV8as_RJZNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر این یارو خداست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/funhiphop/84521" target="_blank">📅 00:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84520">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شما براتون مهمه که تتلو عفو خورده و برای ازادیش باید تتو هاشو پاک کنه؟
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/84520" target="_blank">📅 23:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84519">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ قاتل :
باید کار را تمام کنیم و تنها مسئله این است که تصمیم بگیریم با روش خوب این کار را انجام دهیم یا روش نه‌چندان خوب. به‌زودی متوجه خواهید شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/84519" target="_blank">📅 23:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84518">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وال استریت‌‌ ژورنال: ⁦CIA⁩ یک لیست از ۵ الی ۱٠ نفری مسئولان ایرانی رو به اسرائیل داده گفته اینارو نباید ترور کرد چون بعدا قراره حکومت رو به دست بگیرن تا ایران کشوری نرمال بشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/84518" target="_blank">📅 23:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84517">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">همتی: بسنت گفت تا دو هفته دیگه ایران فروپاشی اقتصادی می شود‌. ده روز گذشت و چیزی نشد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84517" target="_blank">📅 22:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84516">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHd63QHJ6FFpFmMy5XxnutNKCNgAA1R80-xiuu4QqLtsEzMQxeJ7dXtqNvmiha8Aso4AptP3RhwYhHE9-8R2cJ6KaDw90NjzZVpx1VWPKaONMwicRkstw7J_dtQcTusWdoPBA8b6RhkfFhisqdAa1e_fAdHp7mhPPtek2bbE2e0vE7Avs-C8kw-WoQRziWcYkBu9mcLZyDko4iw09b0SuFS7jnDIxTmxacp8H5jd8pN9wQsg1QGV9m1DQY9AeZLFB8nlZZFxRXUaf8_bVaPUMmgtyoDiICdbO3zjVNv2CBG2Ox_FxMlpPPuRR5aeQXqEZYdFY8mngQnupY8UOSXxqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلثوم اکبری که 11 شوهرش رو به قتل رسونده بود، به 10 بار اعدام محکوم شد و این حکم به زودی اجرا میشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84516" target="_blank">📅 21:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84515">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpExLJ3PiCVhZOR_2q4zmwbcOKP0CvyZHVHeOetfVenv0v3uwNICAtFkMWMClx9wDAK5SNy4DEmnAq1zOo93Fs_3fci_vs5am8yaXKqkWtWREZHU3UMvC0H4THD9wy72G04BJlNLuqwimX-0kgER7iP4qReCm5nETRwRMjDMhKE2MEaOipcVdfdUotZ4XFHwFwf8U_1Jm160-Q-7AJPpoABH06QY3hWjdi8G8pRlc1qbGdNNrcoKpSXOFG7wW5179Py-KG4gcKrKlEEX0dqxYEBlHgl894jLwB0AATtM3t40rKCV87aRuXOo4CFptFt1wHUz0_yxY8siSgTboeiv3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته نشدی انقد پول فیلترشکن کند دادی؟
🤨
سرویس مولتی سرور با بیش از ۵ کشور مختلف و آیپی ثابت
👌
💎
سرویس های پر طرفدار :
💫
1 کاربره 1 ماهه با حجم نامحدود : 148T
💫
10  گیگابایت 1 ماهه : 45T
◽️
-همراه با تست رایگان
🫰
جهت دریافت تست رایگان و سفارش :
👨‍💻
@storkvpnsupport
🌐
Channel:
@StorkVpn</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84515" target="_blank">📅 21:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84514">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پوتین و پزشکیان جمعه با هم دیدار میکنن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/84514" target="_blank">📅 21:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84513">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Waiting</div>
  <div class="tg-doc-extra">The Creator</div>
</div>
<a href="https://t.me/funhiphop/84513" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید Creator بنام ویتینگ منتشر شد
🆔️
@Amircreatorrr</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/84513" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84512">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AROtzPrGC84Qd7rJPUyuZgm08XuS5CY5FM_W0HxzQfs9QeDRzITj2buvY3RIAbFOO9Qu4FpyxLv8vjb4JKjPUjLanp7o6YNl8f42Of2iCvKRWdrBCRVuyhiL49dcIIeaRGIAKTdajZRdPoGvrL4gLkv8z223VhcXUjFrMyusQQqohXoFZdTYKsU3XiW3cndQwiVEvySExXWXtQDcHvLhxUNTnTYkixidNwX53jGNi9-r1vOY82ZkeWrxpsOJWgYnoZ0UM1YTPtiRgrp5b8LuF0HfzlBiIdGXOceg0OspyLQ1aq2CA04PwpVAFvoOvOtURFaRbL19WD1iLU1NUbegLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید Creator بنام ویتینگ منتشر شد
🆔️
@Amircreatorrr
📥
Download</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/84512" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84511">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حمایت از آرتیست:  Download  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/84511" target="_blank">📅 20:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84510">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ملت ویو هاشون میریزه میرن با یه رپر هایپ فیت میدن، دکی هم رفته با کسی که مخاطبای رپفارس با اون فهمیدن معنی فید بودن چیه فیت میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/84510" target="_blank">📅 20:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84509">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترک جدید عرفان پایدار و هیپهاپولوژیست به نام "بچه مردم" منتشر شد.  SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/84509" target="_blank">📅 20:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84508">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jll_hhsSRSfz7YF9Jc9E7RXB9JOk6P0WR-5sdwtyJWl-MWgsWQq1YCnNj_DbfebrGEG2886KOZMtwDD3U_EcVfqf7ELagmV3UjcCawbezN4nNrBYek0BvV3JfTD4zL9_8h9GImhZKZAAaVEdoLWLsmZHsQ6VrjVT07Xs0Mxpk9SHLmSxeXRCGY8EyaQiRT1FgVZdB1Tv5vafMgNVni6_MBysNiLBuyauuomFVjntqFKNfn-AlGrrSsjUQ_b9RXAA3oleHIjXwlC0IDohBXaEZRbcLsFiq0Wlh9C4c8Sg2t7YZwpwU-z1lHsIDY86cnadrHQoVXlQNWBrHy1RZ0uUTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید عرفان پایدار و هیپهاپولوژیست به نام "بچه مردم" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/84508" target="_blank">📅 20:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84505">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab91fa8060.mp4?token=RgXsmrpHTQLIiNPL8r8IhF2mapts0PCZjw-d20cz4Ig8WKDCgrnanLjr67Gyx1f5gjGE4GuvcCUFXtezYU7OG1ibHuX0KOqccOqkN8Ga3lUSjYLA4wRZ-PBGpgsT0AQ1rTlpYpllk1YZOSfn5GGibc5P3cc4cWJKX-ABajB2ZNG-Nj5rzB6LWtL1yP85niLbo72Til7M1o4KuJAEdR7hDwycXPd6mvLfUEPQxvDa52Vsf6X6THmlQjolk19WsTJxu-fw1xbvIV2lY4xnGfAWEkI3vZ5w16XWzjYHst8eDzco6NopV-TNudcjeRqauZAIPa5m77-67RcynN4nlkHvpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab91fa8060.mp4?token=RgXsmrpHTQLIiNPL8r8IhF2mapts0PCZjw-d20cz4Ig8WKDCgrnanLjr67Gyx1f5gjGE4GuvcCUFXtezYU7OG1ibHuX0KOqccOqkN8Ga3lUSjYLA4wRZ-PBGpgsT0AQ1rTlpYpllk1YZOSfn5GGibc5P3cc4cWJKX-ABajB2ZNG-Nj5rzB6LWtL1yP85niLbo72Til7M1o4KuJAEdR7hDwycXPd6mvLfUEPQxvDa52Vsf6X6THmlQjolk19WsTJxu-fw1xbvIV2lY4xnGfAWEkI3vZ5w16XWzjYHst8eDzco6NopV-TNudcjeRqauZAIPa5m77-67RcynN4nlkHvpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشق امشب آخرین بازی ملیشو میکنه و همچیز بعد ۲۰ سال تموم میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/84505" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84503">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=aswwXgiv4v-I7teq5LlbsgBiiyfeHxN9Wi66Hh8dgqEg0pfi8LWD2UNM4dvtDFLQvUMEY3ttbaMaGZLQgkLEI_6O2MUod-zr5fq_GnE1nLqdvlfk9-deCyIVexUOESa1sN6qDmjR72oSkTvCg6u4t-tOoO28E6qhGDOQgf6uaZMK3Yr0dWg9GVtkrF2_ZK0TKF_7CNRNTTPWHBtJPa6qtpLhMsspUF9fOGlD-yZGOISC4DWkhKCTW3giTf2I2Y9MK64QJG7x1cRtqlC7HEvZ44JzuWRsEiWAcQ5_jbf2UE1Dfhb3jg1pEtAznpcfAChCXMM3zGXFz_gLtapLbodj9g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=aswwXgiv4v-I7teq5LlbsgBiiyfeHxN9Wi66Hh8dgqEg0pfi8LWD2UNM4dvtDFLQvUMEY3ttbaMaGZLQgkLEI_6O2MUod-zr5fq_GnE1nLqdvlfk9-deCyIVexUOESa1sN6qDmjR72oSkTvCg6u4t-tOoO28E6qhGDOQgf6uaZMK3Yr0dWg9GVtkrF2_ZK0TKF_7CNRNTTPWHBtJPa6qtpLhMsspUF9fOGlD-yZGOISC4DWkhKCTW3giTf2I2Y9MK64QJG7x1cRtqlC7HEvZ44JzuWRsEiWAcQ5_jbf2UE1Dfhb3jg1pEtAznpcfAChCXMM3zGXFz_gLtapLbodj9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکارترین پرونده فساد توی تاریخ ورزش کشور
یه خانم با تیمای بزرگ فوتبال مملکت قرارداد می‌بسته و می‌گفته بهم پول بدین، منم در ازاش با داور سکس میکنم تا نتیجه رو به نفع شما بگیره!
بعد از دستگیری، این خانم اعتراف کرده که با بیش از ۴۰ داور سکس داشته و باعث صعود خیلی از تیما شده!
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/84503" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84502">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رایتل ورشکست شد به مزایده گذاشته شد
شستا آگهی مزایده عمومی دو مرحله‌ای فروش نقدی 100 درصد سهام شرکت خدمات ارتباطی رایتل را روی سامانه کدال منتشر کرد. ارزش پایه‌ این واگذاری 130 همت تعیین شده است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/84502" target="_blank">📅 19:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84501">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf8c96111.mp4?token=Z2uCc2Es3sYVOV0jSwGmmRDROpWAOO4WEoq5XUknCI3fwrSQMYaQ5P2U5jO72yoV9NU9vgGHExBdwfYuGD8cPBCBCYaKVIEScM3sm9AJqF5KPHbA-DOlsHmdEeZODY33uGPTpYHzdBsNa-KlGJ2oMynVWbeP-U8fG2KfidRBKVRY0yQstcQQdX_OVP_mAL5JVsRAP6tIL5z7IJZjdIa0LsoqtmHKwfwqvlQzhqUjGS5kTbePnGv1GzCWgtl-u7zJXMGCFuVSHto5MHS7xEP15Jyt7bsbEK8NcjJnarU4oUEV2BKg7zE0Qwyr_j8HaqFyZzixVjCN0CFmZ9LlWTjEzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf8c96111.mp4?token=Z2uCc2Es3sYVOV0jSwGmmRDROpWAOO4WEoq5XUknCI3fwrSQMYaQ5P2U5jO72yoV9NU9vgGHExBdwfYuGD8cPBCBCYaKVIEScM3sm9AJqF5KPHbA-DOlsHmdEeZODY33uGPTpYHzdBsNa-KlGJ2oMynVWbeP-U8fG2KfidRBKVRY0yQstcQQdX_OVP_mAL5JVsRAP6tIL5z7IJZjdIa0LsoqtmHKwfwqvlQzhqUjGS5kTbePnGv1GzCWgtl-u7zJXMGCFuVSHto5MHS7xEP15Jyt7bsbEK8NcjJnarU4oUEV2BKg7zE0Qwyr_j8HaqFyZzixVjCN0CFmZ9LlWTjEzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسره جلو چندتا دختر جوگیر میشه می خواست از تو یه ماشین بپره تو ی ماشین دیگه که بگا میره
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/84501" target="_blank">📅 19:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84500">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ea14d958.mp4?token=hDwATBBLtflwTkND5sajDF-7uYEAF0bEHOcem3TiW7jm3P9beBUhGrO5D7tNjhmFRDPgKKQ8pI7RT3oBLsrkZ8YdqsIU6j2Dm2-WYQtrPhgMkClw5VD8x6creJ3oSaldnXZuL8MAVMQrfy8cJBQbRlRdny5PAPmNrE2xQrqQCvEFLpTt2MZgzJouJZM81QB_AXW1bD6HFU2EPvh3fejko3-UO_wU_2ty1-WIT6YE3KTz0P0QMfjgFjOloZNtYNiuLk1Qsk-5XcdjWmbD-WRkrYn2rhJDVWribuJM4Kqih6ACPSrhwi0IxtQtNRchd3sdxM8lGnvWaz1UZli8eiT3CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ea14d958.mp4?token=hDwATBBLtflwTkND5sajDF-7uYEAF0bEHOcem3TiW7jm3P9beBUhGrO5D7tNjhmFRDPgKKQ8pI7RT3oBLsrkZ8YdqsIU6j2Dm2-WYQtrPhgMkClw5VD8x6creJ3oSaldnXZuL8MAVMQrfy8cJBQbRlRdny5PAPmNrE2xQrqQCvEFLpTt2MZgzJouJZM81QB_AXW1bD6HFU2EPvh3fejko3-UO_wU_2ty1-WIT6YE3KTz0P0QMfjgFjOloZNtYNiuLk1Qsk-5XcdjWmbD-WRkrYn2rhJDVWribuJM4Kqih6ACPSrhwi0IxtQtNRchd3sdxM8lGnvWaz1UZli8eiT3CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اونایی که تو سال ۲۰۲۶ ایرانی ان:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/84500" target="_blank">📅 19:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84499">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNvX_Yleb92Qt5Sc6UbiiMuFcPQRmRcVj_8aE6UYHZLqIlw8L3ITPODTigqZYPaom-pYHUGffFX1FW81uuVhDft-kZB-iYBiJXpK8ktzxupuTUavyAl6dX_W_LnIJITHl86Fy8HUMTe6f1PTTtdCMeQ7gbhw3XSzdv6nup2-GRb7Q8z6bV4-00THi-bbmJ49ZxfbPSzOwVlZudu03y4b1yqE0GjN8sPI9aJmBIXoqt8B3SuUn2FT8waB8HdY64OxTmJIoGoi3uBbemtQwhc8r0-GkxuWgc6Kp6FjT_dt7k9t2Cq-_rX0loM1m29WVaKqzvkaqk6jLXklr6udHwPUqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعا نامزدش چطوری دلش اومد دل این بچه رو بشکنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/84499" target="_blank">📅 18:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84497">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb27cdfea1.mp4?token=VkOpJCodWkbzmZ-HDO4Olg4Tjkor-_7uF2ZtqJBHwG03FEp6lOyKax3oNwIDY8g9ntLmp-R-X2eswDjlYcv_hnBKV3SnlWxOjo_FEc3haubZNuL6b7e-c9ca5fJ-MC-VV9-WuJR-U2te7mGO1m7KEBYvWUiZxPkTu-bHjEWkDY7qmOvHZ-9WWlpKyhOj4LyNh5jg86qiIgm1bF6q0G6IK60KUtGH87wvDRsylvapGkajKph6HNDjLBbZfIqcdwrDBJpLtfD6YQwMvgsXfS6UWSYJpsSHYMaJ6aQYSZ8CblE2pd6bWgS5bMrAEZQh-sggCqRgMJWxR14JRt-fu-SyCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb27cdfea1.mp4?token=VkOpJCodWkbzmZ-HDO4Olg4Tjkor-_7uF2ZtqJBHwG03FEp6lOyKax3oNwIDY8g9ntLmp-R-X2eswDjlYcv_hnBKV3SnlWxOjo_FEc3haubZNuL6b7e-c9ca5fJ-MC-VV9-WuJR-U2te7mGO1m7KEBYvWUiZxPkTu-bHjEWkDY7qmOvHZ-9WWlpKyhOj4LyNh5jg86qiIgm1bF6q0G6IK60KUtGH87wvDRsylvapGkajKph6HNDjLBbZfIqcdwrDBJpLtfD6YQwMvgsXfS6UWSYJpsSHYMaJ6aQYSZ8CblE2pd6bWgS5bMrAEZQh-sggCqRgMJWxR14JRt-fu-SyCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بری‌بت
✔️
دو شرط رایگان در روز
⭐️
🇪🇺
برای پیشبینی بسکتبال، تنیس و والیبال
⭐️
🥳
بر روی بازی‌های ورزش مورد علاقه خود به صورت زنده شرط بندی کنید.
🤩
۳۰٪ از میانگین هر پنج شرط خود را در قالب شرط رایگان دریافت کنید.
💱
0️⃣
1️⃣
🔣
شارژ بیشتر برای شارژ با روش رمزارز
⭐
مجهز به سیستم پی اس ووچر
👑
😀
ورود به سایت:
😀
g14
🅰
📎
https://bhdyfhicoas.shop/fa/affiliates/?btag=914641_l303106
❤️
کانال تلگرام
😀
📎
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/84497" target="_blank">📅 18:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84496">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">جوک برتر قرن
احضار سفیر فرانسه به وزارت خارجه ایران
در پی برخورد خشونت‌آمیز دولت فرانسه با اعتراضات صنفی دانش‌آموزی و موارد نقض‌ فاحش و گسترده حقوق بشر، امروز سفیر فرانسه در تهران به وزارت امور خارجه احضار شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/84496" target="_blank">📅 18:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84495">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بزار باهات رو راست باشم عرفان، همون قبلی ام به ورس تو میرسه میزنم آهنگ بعدی  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84495" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84494">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دیدین گفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/84494" target="_blank">📅 17:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84493">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvnJ7o5WT5H9g4kuQkaWbQMGY9nWYMdE2mwQQcaG01Euo34wm_D2T9hwVkB_f-_4G-570S1oO5YbWAxFY9Yvr1JCR7CxAW2JqFHvXXSZj1KNbHmiTb6bwKCWmL5yc6GXe7alhugB1l8A0oMupdQhcLE-8mOM7LyYCyiqCepXN0nvVeMO9LYSCOp6Ddw_3XAMaVhEUtY6K_oRgnUySWc-8eGbC01U-5Fiia7Pr2GQNv_s5nq-ZsJztmUtfT_IOMaM0IMBzGj-W0xbpQMmZgmsI67wBQYlwIUrb4Jgc-kaxm3P8ItjrixQt21ogsXEiMF0CxDbsPZTmEAmcskDy5zzpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا شکرت
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84493" target="_blank">📅 15:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84492">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FP9mlR_xKVhfa691qxaoyEl3oPvAhVnUQMu0QofVq-2Nx4i6wJzc26U6G559n9ENIsjL6wmHgr7Zchv_Ryt-tb4ZKW9yzJ2kxMIf7KpreSRBDicQOIHytjD2chXmLCjBymqiS8Svxcj04bM5HfSm7ufeme65qT9IUco3ou2lAzBKcUMfakaVMpBwSFCudo33s1iqZm0mKZxjnIhhY6lmCXIytDwd19HGGIKah6QmIuCt5l2qdKQ8Y3PXz1CoKuS3UI5lkFcQdHYtyYjoZKAxEfpgGh6cVzSsWWmfGjtBv-Wzyuf0nLzTdae6Idgk1CjCS7DPn1_c4es0zbQ0zNhdHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی فلج های مغزیه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84492" target="_blank">📅 14:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84491">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دولت فرانسه اجازه ازدواج مرد با مرد رو صادر کرد
👨‍❤️‍👨
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84491" target="_blank">📅 12:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84490">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">من دقت کردم ویلسون هر وقت با ودکا مست میکنه ویس میگیره، انگلیسی صحبت میکنه خطاب به ایمانمون و عرفان و هیچکس، هروقت عرق سگی میخوره فارسی ویس میگیره خطاب به فدایی و پیشرو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84490" target="_blank">📅 12:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84489">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJ4ohiEYknZslU9HmdY6-AtBpLpu0jAOi46EKTCpzgAbfJCoIuj31sH81RB25hA4UUwk6-gv3-q1E97lW-U8aqwEUJdrrHcFFipoetvvMMjqM3BRmLY9k9lvl3T2e3cdP35WaUq1adsec6pKAuIpV4u-RIZTapSFdWGliy4EWs830cmw9H0IyZsNdbtsdeMNcYusS801bZzQGFv9et58elEktu_kU3Y54QBdSdloaGF9aXJlqlUnvOPNJfEcvWP4yngts2D2aBazlbwBppINPIsgrHwscOtTKTMt5Hr1fQi8KOIayljMKclZgK09gjOyGThPoj_oVpVwNdafWNFynA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزار باهات رو راست باشم عرفان، همون قبلی ام به ورس تو میرسه میزنم آهنگ بعدی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84489" target="_blank">📅 11:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84488">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">هرچقدرم از خطرناک بودن طاعون تو اینستا کصشر تفت بدید من یکی این سری ماسک نمیزنم، کیرم تو این دنیاتون</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84488" target="_blank">📅 11:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84487">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2951b20357.mp4?token=SFYJSsNAX8dPhK0jtageIDYIB-jZL-3uGQH59BfJ5SThaeHVY7hkthHuHqnAGJlCvcR_6cMjJ6PHCmeh7yHqyK6um-Pbfb6HqopHN4th79i71zZuqR9687tfLsQra5YlmdRKa7biW8e2MKH0pUbK4fCr2q6DLnmph1zb5ByFRVVUH70jTJBw-6Dk7DYg6_yx1HnUQCJkko7MAXIdCxqQnyDh3BNyIDCeX9_m8JbUvdyICFB2GhzoCuW3Pcjn6zPM6NAIl9f1z3zAMR3GyFq5rnw41VXgKnsjwp06A-9aLifMlEvJytL7y6b8OCSL-RRMAKQPG6zySbxneIkQlYQ64g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2951b20357.mp4?token=SFYJSsNAX8dPhK0jtageIDYIB-jZL-3uGQH59BfJ5SThaeHVY7hkthHuHqnAGJlCvcR_6cMjJ6PHCmeh7yHqyK6um-Pbfb6HqopHN4th79i71zZuqR9687tfLsQra5YlmdRKa7biW8e2MKH0pUbK4fCr2q6DLnmph1zb5ByFRVVUH70jTJBw-6Dk7DYg6_yx1HnUQCJkko7MAXIdCxqQnyDh3BNyIDCeX9_m8JbUvdyICFB2GhzoCuW3Pcjn6zPM6NAIl9f1z3zAMR3GyFq5rnw41VXgKnsjwp06A-9aLifMlEvJytL7y6b8OCSL-RRMAKQPG6zySbxneIkQlYQ64g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمو بخدا من نبودم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84487" target="_blank">📅 11:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84486">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/84486" target="_blank">📅 11:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84485">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbDmgLh97lWGlEdofTxF6ilXTI6mZvzuyjF9KE80fy5xHP53s0f536t7DI72SIibFH7opmMTPVOrtjkCWmrZjOmIzXuC-dxkzylmbGTOLagfINNVZ8cF4XDVD-vfU8p--8_Fj4X-8kIB-baJXtmuT0DP1JxwznWG2_KF1zoUp2o3AYjh4ScseFPmwItnsF3rAbXeWI91WOgToaRP86bk60JamfP5ekog73COzgyYBJ4sZfO6P8PwOEV5addYfQwf4cxH3WYI-x8GjVQasaA9HRjFfRNILUQMzR99zjfOtZHYPFfwkmL39XQa1N3RVorRgeAHne1Xrkvb8CoP1B5Zxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
کرواسی - اسپانیا
⏰
ساعت ۲۲:۱۵
🌎
📲
مقدونیه شمالی - سوئیس
😀
ساعت ۲۲:۱۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R14
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84485" target="_blank">📅 11:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84484">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رئیس پلیس تهران بزرگ: از این پس قلیان و موسیقی زنده در کافه‌های تهران ممنوع است و با ارائه دهندگان برخورد میشود
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84484" target="_blank">📅 09:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84483">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سلام، پاشید برید مدرسه+دانشگاه بدبختا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84483" target="_blank">📅 06:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84482">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سلام، پاشید برید مدرسه+دانشگاه بدبختا</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84482" target="_blank">📅 06:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84481">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4JH4IQwumvwE0vrbMXY-1sdGRdlH18F9CA2je7U6Al9RW7G2p63431JFf8ko5hrPyU9zgjkfyULmS7sqSToSvyDC8moc5GR4XOU3KOXWXM44B2DDDIgLBjy0ONNYAj7DxqujVuV_fqueYAbxY1AOB5_-bZqgBmHEAowuH6_3k_jbtmtR5sMBARk7hJLe9xfT_P79n9NHwqgiB1rdK3nlPW_WXjNpFSul1AQIhfr1qxt7GCDEM_NN8ui52LBqJomjWhRXp6oZK6J1NQ1gGUcyVeCV-3svrnrFCAjDt7rTyiIVJyV5rAmnDzXpmVpziDGKW9BIdQOwAxRU085jhAWBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حوثیا که نیروهوایی ندارن بالگرد آمریکایی چطور در نزدیکی های دریای سرخ بعد از کد اضطراری ۷۷۰۰ سقوط کرده؟
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/84481" target="_blank">📅 01:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84479">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MJJBsTWv1fj7Ua51YwRzUJ6aG1nHPii8X36W8m-nacxFBENqz4rKIx8wMsqrMNp6giLH_oZGuqaIl6P9Mwenn6b0h0UosWmqQ5YZjUJay0gqd2DcIrtE_1T-_sHIx5V-J3f8NlY1iiXOpaIT_60eGC4_WMqTNen_fyPiB1DoU5F6gpnXtVIOAf-BAduAUeRxukItPnlohrTODsh62rX0Gnq16HYRJ1NXOvSTSh5xwvk6H4ZgzsBid3V_jwwzRS-aTc-jHKkKV60FICdKQTF6toT1Y5lrcPiFNVxZRukeJAJKYuRX7U99SvgHmFj9Ri7Vl8fXCyrPBChdBhRCua014w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LR5MET5GqdUfwaEMnBrPxlIsGdIyeND8Z6BB9OQODY6PSvuoyiSM43tlRl7N6lr2TI5Z3xyULO0zkxkstKvMt4mjSHnhni1zaQ6n6wiGHVwmdogv86OgUEObOB6mDFQNRH_ZdDzekt8YXclwtvi_aKkKZXBG5U2UwsJHf_xb1MLAmiwGQWIgu4ddBOLttWF2A6wbUMeDTA-jjP6GroR3xFGxLtgc9-9QITkHayzM8YuereuQBwx-GS6mLh0BPKyPMZHbtIwyEt-gYPzmnR6AWsCPewqClh07bXTDVwECNxqjoKDoijCxJqnZYjT-NwL6gwbemVLTH2PqUJ81T454fA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بهترین وینگرای جهان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84479" target="_blank">📅 00:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84478">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اولیسه واقعا خداست، دلیل این که فنای بارسا ازش بدشون میادو نمیفهمم، بازیکن رئالم نیست بگی از رو تعصبه</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84478" target="_blank">📅 00:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84475">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اولیسه واقعا خداست، دلیل این که فنای بارسا ازش بدشون میادو نمیفهمم، بازیکن رئالم نیست بگی از رو تعصبه</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84475" target="_blank">📅 00:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84474">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XP4UAHU6_9xwSzwg8N-zlk_mFPD6hoVxcAHdGDqEVvN4mb69gJ6ijQTqC8HmmSLM4uUu5-wTGCbxJSCxSNo-2Xq08wNKqPdxyBudpdUjq6NbOHnCyzXJuPIaKoOJi2PA9mmbFLBPYd2ZKwpJPe-XiTuVgOK4m2fP_MIagZtUzSOIvYoexm4JSJYs3ivgRQ-YsTXecGI7hJ5VhGbvVfrthwbv0eUXcfseNYIdnjOM2r2z9z_erk5AaEAGlfYxb2Fgcr7CaPUPK5Yo2GWfdkeNeihdR0O6lSTj5ZBQr_Wk4gHTp-zuMqlOW5A_J_0y0Au87jeFEbo4aa4Yhglq_eW1kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر تنها کسی که شبیه آدمیزاده بنیامینه که اونم فعال رپفارسی نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/84474" target="_blank">📅 23:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84473">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ:
معتقدم ایران در تلاش برای ربودن هواپیمای «فلای‌دبی» که عازم دبی بود، نقش دارد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84473" target="_blank">📅 23:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84472">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ویدیوی وایرال شده از شهر شلخوفِ روسیه مبتلا به طاعون تو سیبری که نشون میده چندین نفر با لباس‌های محافظ و مخصوص، تو شهر درحال رفت‌و‌آمد هستن؛ اینطور که میگن در حال حاضر بیمارستان قرنطینه شده و داروخانه‌ها هم آنتی بیوتیک‌هاشون تمام شده. @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84472" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84471">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b249c59827.mp4?token=X8GSakSJHJnKRZAreYrzAnf2r-yesLAmWjlGyWZBMH-cxaVLlSpK0RcGDnMprp0TSztrzBIE-SQgm6Y88pwWpvanMO6Zs_rxhHTngHOc2ABHhcaE-qEc6bHp8K7HJqFK8nr74CRrCIqOHsRPiVBDmd5Odxu8XMqljQsSRg31NtVg7JjjQpa3ybWgTWjEVf8b3onA71_sjjBxJwWnqFq0mfg2Aqmv537CnP4V76AOYNTavNve4smxOregrBUMsfkYimW18vIKsQajoh4ZanLns6oYF0ZiU9CUmRv5HIi2eDgbd3G4fXFHfRQ4qgd502toRlLGxZgqGVGwq0Nh_O0jfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b249c59827.mp4?token=X8GSakSJHJnKRZAreYrzAnf2r-yesLAmWjlGyWZBMH-cxaVLlSpK0RcGDnMprp0TSztrzBIE-SQgm6Y88pwWpvanMO6Zs_rxhHTngHOc2ABHhcaE-qEc6bHp8K7HJqFK8nr74CRrCIqOHsRPiVBDmd5Odxu8XMqljQsSRg31NtVg7JjjQpa3ybWgTWjEVf8b3onA71_sjjBxJwWnqFq0mfg2Aqmv537CnP4V76AOYNTavNve4smxOregrBUMsfkYimW18vIKsQajoh4ZanLns6oYF0ZiU9CUmRv5HIi2eDgbd3G4fXFHfRQ4qgd502toRlLGxZgqGVGwq0Nh_O0jfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این‌سری دیگه ماسک نمیزنم یه ویروس ناشناخته از آزمایشگاه طاعونِ روسیه پخش شده، چند صد نفر قرنطینه شدن و چند بیمارستان هم بسته شده هاگوپیان: طاعونی که تو روسیه پخش شده، حدود ۱۰۰ برابر کشنده‌تر از کروناس  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84471" target="_blank">📅 22:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84470">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">این لوکاکو چرا نمیمیره</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84470" target="_blank">📅 22:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84469">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbed26b887.mp4?token=EatNpbfn3a6RiFvsw9ZYQ0EKUNgGgcpVX6-8Mn8ZWxjCmOwtDt_Z2crfHamiZFYHQ5NzKflhcMUUgdDxT5PfgVb5RvyyuKWBJOnETvQLXT-t7fmj5AqXP_CH_t_mMxUpBHSIiagQ9Sh1QBLcy9mnhb7BjaW44DsYtc0oBVRyGz256PCQrED3anlVgkwI48L0Ba9Rl1AFPQHD_IegpyMixfANDXJgu_XHq8RPlpHlv5HKPo9gkGvoB9lOG1guVcG62vTNJ7Eg-OGXo80yljEVqdvXUvsm0yXUXhwpmQv35QfNBdkpZGs0RgWakXEuUVIcWdWt0x_fWeXEWGCIs0G5Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbed26b887.mp4?token=EatNpbfn3a6RiFvsw9ZYQ0EKUNgGgcpVX6-8Mn8ZWxjCmOwtDt_Z2crfHamiZFYHQ5NzKflhcMUUgdDxT5PfgVb5RvyyuKWBJOnETvQLXT-t7fmj5AqXP_CH_t_mMxUpBHSIiagQ9Sh1QBLcy9mnhb7BjaW44DsYtc0oBVRyGz256PCQrED3anlVgkwI48L0Ba9Rl1AFPQHD_IegpyMixfANDXJgu_XHq8RPlpHlv5HKPo9gkGvoB9lOG1guVcG62vTNJ7Eg-OGXo80yljEVqdvXUvsm0yXUXhwpmQv35QfNBdkpZGs0RgWakXEuUVIcWdWt0x_fWeXEWGCIs0G5Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با یه پست رپی ناب روزمون رو شروع کنیم  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84469" target="_blank">📅 21:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84468">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خیلی دوس دارم بدونم اینایی که از رپ دنبال محتوا ان تو باشگاه چی گوش میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84468" target="_blank">📅 21:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84467">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">منو برگردونین به اونزمان که تنها دغدغمون این بود که حصین زد یا فدایی
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84467" target="_blank">📅 21:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84466">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">LCPV</div>
  <div class="tg-doc-extra">Creator (ft sahar)</div>
</div>
<a href="https://t.me/funhiphop/84466" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید Creator بنام "ال سی پیوی" منتشر شد
🆔️
@Amircreatorrr</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84466" target="_blank">📅 21:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84465">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFnmur3Tp8BKFMRHSAWPneUmCKXhRgnEP5763TvEUsezP_S7z8cnpJmJ71Sly2xu6k7oFm_j3ooQDv5q5msXcOEyXfSvEJ4xIE2nkMmYX7jucKnjsAtYc98Y9Wqt_9Lgcd86v-Tko5ZBlwMrvKh3WplGavumPdsWWDOGrYNs7wMqRpMhwaZntvPktQ_nivKx4SwwgCEAmXLVruGEm9lskB_Zwk_3pCHkvvjQMDlvAKwCGxxqmOQsiO2ZIMoALFRTpPS1t6drSqk-xx6xuVaBFJwa6AihjSWLrx1-mmk7RtdqvENdPHfdcA5CtBmTXgQVT8oXNbwzuyQtwhMsiL77Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید Creator بنام "ال سی پیوی" منتشر شد
🆔️
@Amircreatorrr
📥
Download</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84465" target="_blank">📅 21:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84461">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GY-vfxk035fD3lmIKEe_HRovWaEXzUCQQoNyhp0NQuLzIi28AgwEZIn3W92T6jbtnNgDqD7Y0QHyjCyUAKe87uZUH3BayxsmuuJ9FWcbbPHw_JLAbBbB4bYu1l09jMNaIlp7U_4PpfZ8UaJQD5d0Io8fBu7Zz9toOeYsM3eGGrKleylD0AbEm5SngCNrfyd9XNrW4oT3O7xyiVYdTykV5N3vsWDjNj-7a-XvHd9C8yg7j0KndNwpxpXYb30szbpjwbNzziwiv-MlC-Fp-T_v8FvYi1OBkVG0ToI290P3yNdLAKhUCIUw8vJ1ix_aF67OVYJFDw6HjnlJxJz5BM-_mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HH7o64JbMlDF_7VSwH-Uixv0DaVJTXYVJWvtlH331gwf2oLuJ5OMJOSr7X_z7xO5kszimuXC41x_mbTEnWxODXyki8aaH7eOUKkXRhw0tbR3qg3CMxyyhRQEezIADMhqK8khBREQPbIwybDGQqtpzGMS9vvouliBiVm59uYh05klrRYEVt9Y0t2_8AHJyBNz6wVwOeyzzIfLO2SgEoEgZIIFcby4dsk-6GNuldOzjnWYxKSA0IbaISTIWSgKikqOUe8dAHLdtTYGLmTr5byQ5MnaFmV_AUGyNI4tU7_B-hVAHYBK6U-lDVtHNZoWBgZNR2We1iMLfWlUTqcgLdZnow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQTFmypQJffFCgRaiWEJqfXVJTlsCLDUsIGfCV6Z0PwyDSG4meycpNJZ5LaolTuvZUyf5Zilnjwy_fXD81uQRKSZRGHR699imzjMRFaEFPTv9DEtXxazPbSAlQUJ5KD13ZzV3goO0ynObBs49D3w5RzXHzebji6UTk_SaIBcM5Ge6IUjJX2kglVNPvNvjudEyjo-oF6GB9lu5Gm8IX0-oywQTM_WLoQeVdvlM6fPC9BEQIhLvhGSgDFzLlg-_1hhHkoW1d5aO5p-Rh_k1j4-bEU69PQovdSEhZPNxMxlJHFHH-GquizWA-sciMRR1dJ_fvOrmtwag4ytnfBpjP4ICw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ef8uXIQBOuHOkTX4GAeLGuXFqJM2qUZtOe4tJbC7x0NUwqdDuESoe6eZlCx3ZqwR-SCNxxqF0lfNw_psopciIfwMopAuGrtL3bA-82oZOpTdYBOl-47F4J3eNjCRz8lZqdZ6SYP2pNgbIjfyheJ_26pkoh-v5kANjzi5CF8FVqs7hCA4dC_hBCgi0iVLapcS7KP18b_m63iqe-Bnqva0VV5eHT8G0soGmIgXuaVd_Qoxs_aCrIXRXb3-ojm9KeAipqUrr4dB0FKUu81RaMUT2lUxnPBic0AUKTLxwF-IYsHf0-4jsPOl7gCbxCR5YMc90Q0UVPxUQg7szZ6lSDumeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کلیشه برعکس و اینجور پستا تو اینستا زیاد شده و دخترا با این ترند حال میکنن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/84461" target="_blank">📅 20:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84460">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دکتر مسعود پزشکیان:
تاکنون، آمریکایی‌ها سه بار پس از مذاکرات به ما حمله کرده‌اند و این نشان می‌دهد که آنها به دنبال گفتگو نیستند؛ بلکه هدفشان سرنگونی نظام جمهوری اسلامی ایران است.
حمله آمریکا به ایران، که با هدف سرنگونی نظام صورت گرفته، فقط باعث اتحاد بیشتر در میان مردم شده است و ان‌شاءالله، این ماییم که از این دوره سر بلند بیرون خواهیم آمد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/84460" target="_blank">📅 20:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84457">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ارتش یمن داره حوثی هارو با ماشین زیر میکنه و میندازه تو دریا:  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84457" target="_blank">📅 20:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84453">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e122cdcfbe.mp4?token=GHM9m2Qiu8EFKxzAjPGDjAel9onbm5qPNKeNrWtdfoaqHHqcnmJtMX1Z7bL0UVXfpbrucM2P2hjBDF-QAiUvm9gv20BLtLrJxQ6WvWo56Oj1N0Ief3kyQmuAKEI7skXMcxmbdKIdBHHJbw-MTkwTcKYM_kPwsWtEVraqyX9agKOR6FOOJt9tHEWMvyQyBrFDSojkzSQnI560hICVA9Drvl7_rtIs93abEPvEf0_xQPGeaymq5NIfcKo0zpm-tPTyTtwOJsoONePJ7A1yGg8g40xXWPFwLktXdemkE6jok-T-xY9ts9qbB_rLRc1X-wfOt5FG9tXiSgH7kFfZINCSuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e122cdcfbe.mp4?token=GHM9m2Qiu8EFKxzAjPGDjAel9onbm5qPNKeNrWtdfoaqHHqcnmJtMX1Z7bL0UVXfpbrucM2P2hjBDF-QAiUvm9gv20BLtLrJxQ6WvWo56Oj1N0Ief3kyQmuAKEI7skXMcxmbdKIdBHHJbw-MTkwTcKYM_kPwsWtEVraqyX9agKOR6FOOJt9tHEWMvyQyBrFDSojkzSQnI560hICVA9Drvl7_rtIs93abEPvEf0_xQPGeaymq5NIfcKo0zpm-tPTyTtwOJsoONePJ7A1yGg8g40xXWPFwLktXdemkE6jok-T-xY9ts9qbB_rLRc1X-wfOt5FG9tXiSgH7kFfZINCSuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش یمن داره حوثی هارو با ماشین زیر میکنه و میندازه تو دریا:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84453" target="_blank">📅 19:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84452">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/84452" target="_blank">📅 19:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84451">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqvFLrN0kHK9XPDYW49ONWL6WAqvSASofjCHvahI97fF7K0LQc7Q_PR7A8hfUfthbTxC6qOUc-tMjjU7LfMSh5IZY9Kiy_9YgGmuu941lEz6rpeRtVix4W39vuzijonVsYr5Yn51F4jPabqp-kv40Ap1AaatNM7sDFW8v3VLHixrdMUCG7r3mZxbjZBgosXn27fH7FO2LeSozYY3q7IveBJ2lmPspsoHeHZBKREHGqDVrSTA3fpye7IP7NW3tkmxKTY6Bc_TJssCiWhGeeAJegCK0HQoV_-MLwGW0rFdGkqDCzopfdCu-Ep1kiZ0c_BBjLA6ftOnJmQor__vYv5Rrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G13
🅰
🛒
ورود به سایت
👇
✅
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84451" target="_blank">📅 19:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84450">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پسر خاورمیانه به روزی افتاده که تو نسخه بدون جنگش روزی ۸۰تا نقطه مورد اصابت موشک و پهپاد قرار میگیرن، وای به روزی که جنگ دوباره شروع شه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84450" target="_blank">📅 18:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84449">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LosgSFwWOBhtrWHuuOyiIaIplET_akuTLHbJxN-6pvDlqPlrbjeNgidQVUfM6whxE0lCh5SiUcnxFdyNNRMEzdQgoRvDco66cvxfGiRC4NjmTT-VJPnQNS-J2qWDO3olqejWcp_njiwqGLie8esYFx25DeEA60VFfurXxV6CuznJTW4yZKpoi4OmFfY1uhDwggpDv978hgH_vLZ_dIso0sA5CmP5ta1I27XOQ3fmExlG5-qwqS98xHCkFQd-vBw8GbolkZ-3lIzvOtZOg2PmBVTmgWE6BeXExNGS-cYpexZlYeJVOCG55Ntv6Cb24w0QB2WEJS4ZAyQoEmjLU6TxyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منوچهر عاقل ترین فردیه که تو توییتر دیدم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84449" target="_blank">📅 18:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84448">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UU_Zu45tclf9RJGU0IDOlq0o6T4PZPjXVWMpvECKGSG1C3-3sx7tGcvGN4KJ0IY-Yl9kTEcLXDAdcI2VxsWzp3BT1q9LzDh5uXIImYKIFox4MByqjWXkTn9fjdBZqxrGzTL2CleD4Fzxj6rLt1YHIfOgl2XnmXfZvhlIdU2FDRDZzFPpNuRYShv5NLeE4hk8-iqj597JOP8hoSgCJgyi6HkQUGP96GcwouT9yai-KhUKBWhxg0Y0BtCrWEiuOvCKOsaTMYIHIx-7GHPje8kwoAIS6EWCO6Ec7eCpc9KGIA3_vELEhz5jW8u1kcTYMMJ0K5rMaGCzINM-PLDqG5Kq_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این شاهکاره ولی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84448" target="_blank">📅 18:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84447">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آلبوم جدید امین تیجی به اسم «پله اضطراری» منتشر شد. Spotify  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84447" target="_blank">📅 17:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84446">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مغازه دارا واقعا بدبختن، با یه کیر دومتری تو کونشون دارن کار میکنن درحالی که ملت فک میکنن اون دومتر کیر برا خودشونه و میکنن تو مشتری
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84446" target="_blank">📅 17:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84445">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJymZxkXCz0cguwm2L-okShP8a7nCI8OP5wBkdLgeZP-s3WLkrWDQM37ba2hS2kOCyGL-pVpPOF59dY8oCzL_WhErZQRgxNWYyJMe73_7zYCVLGTeP8TLDnEptK9WUM2DOeNMDDQvm12Z0b-5x60cGXjDjeEMg6RJ720jWxoPHBghd_WUnIKAKOeLD6lqh0GLdYeKzp6TRabsCBFo0LCCl7d0-92Lx-WhTlkbCOIO90iwcWjpGRfZjaMYHbMiSRXcM6IQA111wBm6CScBLp_MRds29rYimSTt1nhW6OQkeyFg9d7M0ohaq27TgPr6cT4gDOOa4aaY37CrmH2ZVFNXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84445" target="_blank">📅 17:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84444">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmNaOc_sIlsB-tifodbvZL9UlMHgN6_0HDK_2EvgThmMHd-ohJPJ9jOuRCqrSqnVea0QcO4iEHKZG59n55diKtqQETIvUQsyh-juBks5BmQXPR403cS6t_kbb-GZVDFdFLCT9JdAv3WRMC0QgbSyQPbby9cULr16YCAJQ8CLsGj_KufSITO9A_z0a0htLq2jX4bpvC8O_dCQFbRhrOeGZ_o13u_AW8Ef1ZaD8BVgjQe8LeFBlnyucilPez6RuBhS6yHx2DfYL8p9xWvN7b80A-pxqYySCb9oG66T1diR7kBTEM6brGbvTqCFfgfcgOpbhzNLXR-3mhnBlHe0d48WHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چارت؟ کدوم چارت؟ چارت یوتیوب با آیپی زیمباوه یا تاپ۱۰ ساندکلاد با آیپی هلند؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84444" target="_blank">📅 17:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84443">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/269eed4b24.mp4?token=TJl1GUrkDTdBLQou1_FFkv_yIroCW-PVcudw1cWqyQtY8jZalmgW-0HGHn0YN1GfiiUYVN83zruHvN0nfffc9xeD8LK1VbuMyF6JDpiNnVg4H5I_B_0y8oHXEw0C5Rx08FtJIgp0w8L3waPlhYG9SXu8uE2lRtBCznZLKmklWdKN4GncROzuDKV6ATj3MxzVoT8-VGnvOeDtmp1mc0301U60h1VrKcC9YsOVqVOnhtR0j0F0mJeH7ecqUAJGLPBZSCE4Jym835p9jn1rSo7Se8fmde_hHjH2Q2DJ30A0WFBrz8BOslwxojq_IMcviKAppbBogDOoUPQuJofFA5JuZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/269eed4b24.mp4?token=TJl1GUrkDTdBLQou1_FFkv_yIroCW-PVcudw1cWqyQtY8jZalmgW-0HGHn0YN1GfiiUYVN83zruHvN0nfffc9xeD8LK1VbuMyF6JDpiNnVg4H5I_B_0y8oHXEw0C5Rx08FtJIgp0w8L3waPlhYG9SXu8uE2lRtBCznZLKmklWdKN4GncROzuDKV6ATj3MxzVoT8-VGnvOeDtmp1mc0301U60h1VrKcC9YsOVqVOnhtR0j0F0mJeH7ecqUAJGLPBZSCE4Jym835p9jn1rSo7Se8fmde_hHjH2Q2DJ30A0WFBrz8BOslwxojq_IMcviKAppbBogDOoUPQuJofFA5JuZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تورو خدا بسه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84443" target="_blank">📅 17:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84442">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کیفیت اصلی فیلم اسپایدرمن اومد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84442" target="_blank">📅 16:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84441">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9jF6hWvrxOrpGp_b9wrvm9fVDMf_9dqgoQrjbr4-6pa0hUyKNaV0ikSfkcXv3AP9GBcfgnZKJ2LwAWALCCl_uAzMozyTf2BCNxShpg9nEfAUILsRpxVK2Cl5pU6wsOYT_bYAJHF8UDjnJqx0lr32Wc6M_tRgsHo1UsEW-64i8peD_xkyRJPe4wgZnnoMHacQhRTvzsAqR6HgICJiEJEMe0CR5mcjAVVk9Gi8ooVaeBzxhJZBdvHb1zK4Hg2sgoAqsG0iVJvJX49alZ7DVdt8LNtt77Ab7gtOk_ENUbVeLwnVXC1Bo41tEcEvDrPLwaNDH2glSvKavNEnw8puPx24A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاگان همچنان درگیر مهدیار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84441" target="_blank">📅 16:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84440">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijBv2kroTTfgvceaXzgluHmkIG1jcvWVRaULmzNtP71uv0RWga1G_zBgwwU3-rbQ9w8L0DOTABPvkQ32DeX72zyLjo2leM1A9N63oxSEu5O3FIdDEzLNml31z5ulWc0ciddqDHUTr2_kKc3tRRyMt4HVpMJjy6KcwgWdNuYxhogJ3YaLeGvQvJ_qNZMCIV67dZlfvvtR-4MffMkeC0KOy-FCa2-RwL0zJuu5A_A2KepOrq6SQl6IEpmm9LkXauOuy5_2cf75Ll1_tmKz79GoWS01DLJ3opqjlKmOxryXCQYRXSvq2CBSt5qDU3Xuhud3Cs3nWMtcJjv3MBCN5JenOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زود قضاوت کردیم
میلی پول ملتو تسویه کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84440" target="_blank">📅 15:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84438">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تیجی داداش هرچی نسخه کنسل شده دادی بیرون از نسخه اصلیش بهتره که
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84438" target="_blank">📅 15:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84437">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وکیل تتلو گفته که تتلو شاید امروز آزاد بشه.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84437" target="_blank">📅 15:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84436">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEkUZslEdJZAqmjvzlR-laRYmgNpP_1YQVi9A9lIx6j7TrSnStKVAh8i7taADVQGjhtqWrOFEnSkfteFXn6_e6BdwLgNZU9Kk422pdYSG6UXz8jZZvNpVFC8HCvTM6tz6q-2ITWpCWd1pG7zjkBUk13CdKR-pbpPYZEJYXABuNYhWERXVjkG3cw2bHxJqM8S-XqiWyuTlGx19_hqaiT00mRtFxWa8hNOBkBOyFT-tp3iMZhBZfgb5vE4CHXCcpmDivSN3E7dhQ6sAf1ADMsEUC9reH9QNjRTbCivShUDewyJc4zJtPsx0oGIrlNyNdi9-T6xf3nNwcVRuWw-Wdl1_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ورشم؛ خبرنگار نزدیک به ترامپ :
آمریکا در حال آماده سازی حمله هسته ای به ایرانه.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84436" target="_blank">📅 14:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84435">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84435" target="_blank">📅 14:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84434">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMH_TmUS61gGDZq3XOqdMf18kY9Jxf-4o7mq8KjeiSZ07V7BmpGOYj2-R_bM0HC-E8rapLu1FB1uOoPj1QwCsECEzbVXBuBWMYeKlfcQYkHovTnczX4OztJqKmOxcArE9Bmfc_bOlPS33rhEQjpPC9zyYqAAuXxU6AzasZrBmWYWY9A-ygWMugxj7ILC0Abg8jmAzvBV_x2MqonauEkwmKykAmJ9VbOtlPhH5mTYoqiERG-nU7B0HsnWYH3BzrS9AQrWi_V9x-WTMtcH6GbYCWwwTI1dqfbgI3zo3dt5mEo71VdKRsZWxuVgZqox5g-zqUatR78QUFAXKDu82HhEGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
فرانسه - بلژیک
⏰
ساعت ۲۲:۱۵
🌎
📲
رومانی - سوئد
😀
ساعت ۲۲:۱۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R13
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84434" target="_blank">📅 14:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84433">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آلبوم جدید امین تیجی به اسم «پله اضطراری» منتشر شد. Spotify  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84433" target="_blank">📅 14:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84432">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3008a810e4.mp4?token=aYt9C273SJ_-4rgrIYbI2_rmE6oSr9UZ7K3voi8lIt2U5HWZgGFJj-SffuK2q-fHMNiIYrM22U_jvJ5Bxk5URamyNUOE-MltBh9B6FOHAYDu6rPWAdd3sDjuTwx0FQQvPQyqA6N4NRJdupNW_aIlkcBUl7SrGt_K_ifWe4vcYWs295p5bVY98CnOE0JMAdHBaqOTFbPZDPBqh95ztvu0nl0XeYInKfoSad7Hgh8LYvKM7GHQSQzhay0Yf8BD0XeIukVVaZ97M_rwSkJOAFsW7tfSns7xAEgeXxJQsdQbM5DVOBKVA8bM6RG4P-pPDlancmmuouWqTVdSZEX1UtZliw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3008a810e4.mp4?token=aYt9C273SJ_-4rgrIYbI2_rmE6oSr9UZ7K3voi8lIt2U5HWZgGFJj-SffuK2q-fHMNiIYrM22U_jvJ5Bxk5URamyNUOE-MltBh9B6FOHAYDu6rPWAdd3sDjuTwx0FQQvPQyqA6N4NRJdupNW_aIlkcBUl7SrGt_K_ifWe4vcYWs295p5bVY98CnOE0JMAdHBaqOTFbPZDPBqh95ztvu0nl0XeYInKfoSad7Hgh8LYvKM7GHQSQzhay0Yf8BD0XeIukVVaZ97M_rwSkJOAFsW7tfSns7xAEgeXxJQsdQbM5DVOBKVA8bM6RG4P-pPDlancmmuouWqTVdSZEX1UtZliw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این‌سری دیگه ماسک نمیزنم یه ویروس ناشناخته از آزمایشگاه طاعونِ روسیه پخش شده، چند صد نفر قرنطینه شدن و چند بیمارستان هم بسته شده هاگوپیان: طاعونی که تو روسیه پخش شده، حدود ۱۰۰ برابر کشنده‌تر از کروناس  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84432" target="_blank">📅 14:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84431">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">این‌سری دیگه ماسک نمیزنم
یه ویروس ناشناخته از آزمایشگاه طاعونِ روسیه پخش شده، چند صد نفر قرنطینه شدن و چند بیمارستان هم بسته شده
هاگوپیان: طاعونی که تو روسیه پخش شده، حدود ۱۰۰ برابر کشنده‌تر از کروناس
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84431" target="_blank">📅 14:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84430">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">آلبوم جدید امین تیجی به اسم «پله اضطراری» منتشر شد. Spotify  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84430" target="_blank">📅 14:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84429">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUbz7kXGtPgP1usNRA7f1JOYasRkcMa2v-RDlDpdSrUYrpftzEoXi3Hx3TwEBkvOrUD9aJSJ2J_R2zyXU09SWmmXjVTycNTqB8CiQbWroT4KOtSQbNPZeLiCmnmsakf3pJ8K410HAT-ZMrEp00p2o6bmyZNRDdB_fBmUETi-2uRE_MOy3zRHRZ9zP5SG7Exq3EoSWOmO9mGkEIylI0-cqBiUiKN8She0Wtl6Us4jVob-VmoOCzXBjV_H3w_QF-G-ORvnVgPHwmzyEtrD9jyRC0QbaQXXA9emRYXdviEKGCubMfDfP1GwGQaEN9r6AW4XVw1SUD32sRk1UXo2dZfSQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید امین تیجی به اسم «پله اضطراری» منتشر شد.
Spotify
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84429" target="_blank">📅 13:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84427">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l6Aaf4B_wln46uszurFTV0D25KhjNUdDaWphka9G5BSLzmjpybKHBYeJBG-bfX6BuDj0PvCY37chpHbKAD8InKsmcPvTaHyZJtAqfxEGrgeT-owDCPtOQrmPJdkTZaaD1gMfL2XcGh_CwcLUM_GS1F0EXUxB19Vn1Xv5RuNUTcCjaYDIcnTN0MF2rdRFSjOPTslk3Kc81ZooS6DFBFssnPMZc4haYF-24vZFOXENM0kAYrYeuiB4KhFJq3DKlk3bJR5zc7ETEN2UJTNhF2WolCLUEhqKVFn-HUjYiBOTyuAGWX3UH3IM3qUpdXvOqcmInKJAr4ivnwxWnaLaboxJAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X_ypeQuri5F1R3aycu2iAz-jgRmdP00hm9xVOGr9Ha-WFU4OJts18PQqAupEaRYs1XdIfdPJ2SiPFTsOWw3rvqVnv7a5_-8dOPhhMI6dq6S9ZtDDoCvgVn8WrI_Emliqban-5kzo4cBk8kKj7u9C2BgofMHhjeDIZuElqlOO_Y7D2tj-CkIO7MTiNRps8utyjWZZiPeMKOpURGIXKQ7tKtrCPsXEYOWVmDu-CLN2NlPfFQGD3cnbcrXA7M-bjD8BsW0iHlVNOHlmUZKuGBgj68V6CA9oNe6E5WLKYrrY4zDLSrCSLKts3cuhfE9UbOJ7GNaARdVBk98nInq2IEmP9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صرافی ایرانی omp finix که امتیاز رسمی و تایید شده ای داره، پول مردم رو بالا کشیده و ۳ ماهه درخواست تسویه حساب مردم رو پرداخت نکرده و مردم رفتن جلو قوه قضائیه دست به اعتراض زدن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84427" target="_blank">📅 12:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84426">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">علیرضا رئیسی ۲۱ ساله و علیرضا سپاهی، امروز همزمان با اذان صبح اعدام شدند.
قبلا علیرضا سپاهی بخاطر از حال رفتن موقع اجرای حکم اعدامش راهی بیمارستان شد که متاسفانه خوب میشه و حکمش مجدد اجرا میشه.
علیرضا سپاهی با دختری که دوسش داشته شب قبل اجرای حکم باهاش ازدواج میکنه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84426" target="_blank">📅 11:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84425">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1MwfIeYT1bS0ZDYGAQ_c1SLOSv5mpkH1hGg77vkSXfxSiUIl9blK2kRpXXmZlbE3cp6-vyEMnrSJVCiDAjBu942oOHBChk4uv0njcJkvktGxqp_M024psoMirJOAse9588v0h0zt9N2dLRDV878MFLxi0FZzYVJ_p_uN3r-N2hzrKnxwbTS47drJ9iKnQfsG4ERSozz1ILXJxoMOn9uiGr4kwfZDVzulL-yGNMoJWLHB0JNSMcdTREVT8A563pqZ6clpONMv4mQR8lns8tV3Z9vLITW4UqNujV6rJl1npZRu6pOHEnSsU8opoghEURW1piQjvhKUgxneah9LdsXSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/84425" target="_blank">📅 03:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84424">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فدوی: قیمت گازوئیل تو اروپا 2 یورو شده که یعنی 700هزار تومن
ما اینجا 10 هزار تومن پول بنزین میدیم که حتی یک دلار هم نمیشه و اصلا متوجه نمیشیم گازوئیل لیتری 2 یورویی یعنی چی
حتی با اینکه قیمت ما سه نرخی هست بازم کمتره به یه دلار هم نمیرسه
این شرایط قیمت ها بخاطر ابهت نیرو های نظامی جمهوری اسلامیه که بوجود اومده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84424" target="_blank">📅 00:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84423">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تو رسانه های اسرائیلی قراره بزنن
تو رسانه های آمریکایی قرار نیست بزنن
تو رسانه های ایرانی "زدن" که میگن چی هست؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84423" target="_blank">📅 00:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84422">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بمب افکن های B1 آمریکای که برای انجام عملیات تو بریتانیا مستقر شده بودن برگشتن آمریکا
ناو جورج بوش هم رفت تایلند استراحت
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/84422" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84421">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90aedaaa0c.mp4?token=rgyEbNlSSeiuJ4e-6aIgcyX1EB7uokqmTyBRcBf-tjW0jCrAawrSPQgg2RDvy7bEM4Exw-Hy1CGqYO2ozvnTfThyaxoGtVX5DIJj5k_eRlTYWAnBLFg1yq4vuc1_-a-PIi4Lj8zVkFUA5oFNQqzKTEcXSJwg0QvAaGELelTxujgCNUjOlIVviKLFp7rtBaXjPD57QsApesislD_yM6WkBkihtsVX3JSJgJUY2ssTYzco7rxtjqNEw4z_chFFOf20sYAroSDqgpdDIzSR3L2LgZCEQanpFllIJGnVqzmnHcV5K_wi4KClQr2Vok1cuHEgsCO8m5LYdQGQgMdsh5MrFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90aedaaa0c.mp4?token=rgyEbNlSSeiuJ4e-6aIgcyX1EB7uokqmTyBRcBf-tjW0jCrAawrSPQgg2RDvy7bEM4Exw-Hy1CGqYO2ozvnTfThyaxoGtVX5DIJj5k_eRlTYWAnBLFg1yq4vuc1_-a-PIi4Lj8zVkFUA5oFNQqzKTEcXSJwg0QvAaGELelTxujgCNUjOlIVviKLFp7rtBaXjPD57QsApesislD_yM6WkBkihtsVX3JSJgJUY2ssTYzco7rxtjqNEw4z_chFFOf20sYAroSDqgpdDIzSR3L2LgZCEQanpFllIJGnVqzmnHcV5K_wi4KClQr2Vok1cuHEgsCO8m5LYdQGQgMdsh5MrFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رژه همجنسگرایان
🏳️‍🌈
طرفدار فلسطین
🇵🇸
تو فرانسه
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/84421" target="_blank">📅 23:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84419">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa13ecbc2.mp4?token=YgvqwxTAf8GRBv8irEaVQmRKqxb_fjQtD5w-umCAfF23NUhN5Fp-f9-Y6A4Yq_3_CJeMIFdth7JLUD9F7by_UkD4myfdQRm4Yu88sJeaYNflrbbt9-sJ32KuyhOs24F7VQ1mf8QivFcX8n7DHQ6c_REI_CM8BVQLyReM9c_C9Tqw1n-gCNkpPhw0k3OVAK9hlh1mdT_zVs023vVslY0ROOvumitAv11d-pJxeoQyo59UGoqYLTTj7mWpP9O2uLJH-IFc3qAsX7GJqbZAH3mqBe_Ep9NwDvV4XzwahQLb-Xb8cymo9MHnikSgxYXe9UnpgMqDAMUPCcwTLPGUAROqYVao0YY7K8KIjypmMqrBZchknmZpfM0ONMZuDt2VBIoMiZwTWomfHDpN9NGfaH070hLuppdD9lN-Q6056MxIPxDh0R3sGtI5jp-e7oOpR-kNSqGIaH9RGsyJVjytdQbmEAU6H9Mjd3ugIkqgOftRPomDgJYTayCybDYLZk8oJ8ix0EgwYa_Q13l-9XAdTv-yxuH9ow_dZsOp1dISItEDTOoXkCXUeOtNHcZnj5fj84fE2_Iewd-PST-WSixIQ8MoA0vdx-qZeUbH6kRlzGZljNW9iElvh3d6sXlyruBzLAKiay5fzU8zFaKP0KV6JRBVJVmG80psdnAgYr0PdzYgeeI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa13ecbc2.mp4?token=YgvqwxTAf8GRBv8irEaVQmRKqxb_fjQtD5w-umCAfF23NUhN5Fp-f9-Y6A4Yq_3_CJeMIFdth7JLUD9F7by_UkD4myfdQRm4Yu88sJeaYNflrbbt9-sJ32KuyhOs24F7VQ1mf8QivFcX8n7DHQ6c_REI_CM8BVQLyReM9c_C9Tqw1n-gCNkpPhw0k3OVAK9hlh1mdT_zVs023vVslY0ROOvumitAv11d-pJxeoQyo59UGoqYLTTj7mWpP9O2uLJH-IFc3qAsX7GJqbZAH3mqBe_Ep9NwDvV4XzwahQLb-Xb8cymo9MHnikSgxYXe9UnpgMqDAMUPCcwTLPGUAROqYVao0YY7K8KIjypmMqrBZchknmZpfM0ONMZuDt2VBIoMiZwTWomfHDpN9NGfaH070hLuppdD9lN-Q6056MxIPxDh0R3sGtI5jp-e7oOpR-kNSqGIaH9RGsyJVjytdQbmEAU6H9Mjd3ugIkqgOftRPomDgJYTayCybDYLZk8oJ8ix0EgwYa_Q13l-9XAdTv-yxuH9ow_dZsOp1dISItEDTOoXkCXUeOtNHcZnj5fj84fE2_Iewd-PST-WSixIQ8MoA0vdx-qZeUbH6kRlzGZljNW9iElvh3d6sXlyruBzLAKiay5fzU8zFaKP0KV6JRBVJVmG80psdnAgYr0PdzYgeeI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدیدا این بابا بولد شده حرفاش شبیه شیما کاتوزیان نیست؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84419" target="_blank">📅 21:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84418">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Chera?</div>
  <div class="tg-doc-extra">The Creator</div>
</div>
<a href="https://t.me/funhiphop/84418" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید The Creator بنام "چرا؟" منتشر شد
🆔️
@Amircreatorrr</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84418" target="_blank">📅 21:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84417">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DF5z6iZ2GoAq6jOMVaTugx4P0vL15-GsraE0PGMF1PmeCaKScRZmpSCH1ff5Bek6XJ8EQVphWtha1mXH8IKnL_4jdFWTt3Hyhvbnv_nREnjb3SrB0zSi2fhW_v2kyauq2-ypw8PsN8An8DA3xynAbgVSllsGP5wVD_WuNhcKDSUZML8vbWzgsOD9ElVG-BfZ5d0jJ0tGPANX22sBFP2tHLW4-zTtGmpHKLlDvoktj9ryX8_O2DviMAxeeBvNFNqIiyHozbAQEcgS4k3fUH2swV00-0RgfM2WPl9bj8_1DOH8gB8-DiP4khSbmuuB4s4miLRM45OR1VeUXpF3Tw9svA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید The Creator بنام "چرا؟" منتشر شد
🆔️
@Amircreatorrr
📥
Download
نظر شما درباره این ترک ؟
عالی
👍
خوب
🔥
متوسط
❤️
ضعیف
👎</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84417" target="_blank">📅 21:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84416">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وزیر نفت جمهوری اسلامی استعفا داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84416" target="_blank">📅 20:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84415">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KC0dhPNh7vRCUBTNM21c3eNTjeTcRIktJ_-mdCIScJHWdXzvdYYaC5TXop7KeutcqKU5jTbxLa2krPV7a2Au2cdOfHL6P_M4nqfPq4DvciFm4DAbJunduSyHVYYmSftiJ_u3H_wO0QKqqfr12m7OIwQJ2AverRxonM1yQPIQhviitrUe2_wX0V9iDbNDjf8Rm8RKEGhoBbJVBBkcKO2z3zVAyxvMOswqmhej04naJaUwOofb8ePlsga0d4WOIoOUhMFtgyCaZEeXVZnD6_QfyAC110udYa0JZwZZHAH3Yb7RTO4_F6vsYR4LMFbNaDt-KJN5y8HuqsK4iY1gQIn0QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید گوچی فلیم و کاگان به اسم «هالیوودی» منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84415" target="_blank">📅 20:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84414">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/us80I3Uw38orgrlRlUbH48icN_T4N3YwMttShVTE0Cb0-Tuwh1iAr_gPuw0Plf27uYA5NqSkx5hjEc6blIp9YTh6_Vn1Ofydmb-P3rpismJPPdFO_4X0msPpoCW1Ha4H6BV5y0L0_k-Pncoa34tI82a-A3jCeJJusRcNW2Ur5XoaaQ8LMxMcfzIuJ_08gLcdDFYG5WkEJzKI50Suef98tsexFrr0nSTANnaspZx-DeC3FcRcK-j54b0cVn7kumcFyxruTdi6PbhJpNDWXc7i-xvMnQiqcP9VtOZS2fDsvjvqptIYUp4njS-zCVbLepvyO8C6NOXEM1M0ghzRHvRgNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G12
🅰
🛒
ورود به سایت
👇
✅
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84414" target="_blank">📅 20:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84411">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCHzMtVK-acXPlaH-yuIBFxcj5NkA1DbfFpvwB8oZVp-7S_ztaEG6aQIgmQXtufBwP_FomWVm7umG6Kb4JfBExYsr3i9_ShBuESAUYRQvNU4qvaB30CBEzpEonHZepDLdMOLAnbao_F9IFDOtjhLtNDTREtZZfXE6v52glbyh8qMrxmz5Fl6BanytZ_zXy4Y5giYdw3043bHT3whTNC8HqxCdlw1K3HNV_q1PrfTB_V2FmX8joETHNTbaPiAw5mv1WwFQXXQw7oXd8mJ3jEPNUAVlPSj2vQfXqLPNLLPjAiwZDuj8sAm-_o201ZzcIaljHRHRL7riVNJExffYdeYQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاد کلیپ های دوران بچگی میوفتم توش میگفتن من از اینده اومدم و ماشین ها پرواز میکنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84411" target="_blank">📅 19:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84410">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تهشم داداشم جوکویچ پیر سگ مچ زورف رو‌ خوابوند</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84410" target="_blank">📅 17:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84409">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دلو از دیس به دکی پرایم رسیده به دیس ریری</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84409" target="_blank">📅 17:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84408">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دلو از دیس به دکی پرایم رسیده به دیس ریری</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84408" target="_blank">📅 17:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84407">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Je5M-OfmeBNLcu4ZDC_KtfUTuzUv5CahN5w0N0JA0at8fsCWYfSit4sar63VQArkpU0LumLroeAP1DnFyRPY6hv4I7d4x28C-85sk85U0uxfl3L6WA_3Rnqqf0tEawYnvvs4xuvuAYTutB_PZCANhL-uCYGc5vlweDyOCHO-w3JBtTMYuh762g5ZlRnHqLT67ES7P0pFHtvLM9N2TNY7bcZGex-enxZ3koG-_53zHkWWqsCA9S2MH4ZfKRohqDszLqZ4K0DkCzeMM8KJu0pb4eMpKW5uEcy1wiH3uNgpbjUstsodHLYoXkQwBGci5Pl5unN8iT7AHe9ctjtsiL6EDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دلو به نام "هاها" ریلیز شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84407" target="_blank">📅 17:20 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
