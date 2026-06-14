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
<img src="https://cdn5.telesco.pe/file/S2f7k9OsDcygU_UauoYw1PX4vlFWtnpEMQtq4FfE0Yu-3TW5Fb3-DVkN1IFkiDmzsztmSm6EKU0P9ry49aUoNw1tQDeNtTTL5FeKCcRMJFSBCyqvDLtdERLXjQA7IGjjWQge9bKWR2hqgeC_ht4DSrQsf6Y0omcJahcaEyej2lVtHfe-lgopqTipeMqb_G_kQj8saRuMv6rgLHJUc-8IrmoUQ3EumCxYBealmC7a7wR05mEqKC44vJ0rHpssifKf-HFnxBx89hFXtuIqOO8kgMNgle23fVzYP3vuSziNodsriWFRTh8N6kb4TI1hufTfuPwebWicsDDAxYy5HlUYIA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 551K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 03:12:55</div>
<hr>

<div class="tg-post" id="msg-93119">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16174ed8b3.mp4?token=nfZ3zvfYFXsv8FGyd_cdIH8LOahL_QgxCeTXPIVOVLFxgncem43qCQywJzPjxwsDrVIDKzTBElmKzVlHcgxY2SwtkOQPAMtdCYPMzvSG6GC0jEtNPKqmdxYDOnvjwXAFXWWs1AC4-vUqsH4JlD0EegTwTB3WEf9x-uIxHhVad0wmdvqrVpJlM7Kz_jncucuviK4O1qtH05tcc2Y7VxO8ntISUdlQqIAsovL9jShyF8OzkOord-hT9dnaOlJGIX4EVZPsWRRdjGoDT1iRz3RStz9cX2OH4ZBOrmgpQKYf-a1TKTSSxaEAwJ-ZqqfJ6RLVmZbW7NublRtMMXDwHnEXSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16174ed8b3.mp4?token=nfZ3zvfYFXsv8FGyd_cdIH8LOahL_QgxCeTXPIVOVLFxgncem43qCQywJzPjxwsDrVIDKzTBElmKzVlHcgxY2SwtkOQPAMtdCYPMzvSG6GC0jEtNPKqmdxYDOnvjwXAFXWWs1AC4-vUqsH4JlD0EegTwTB3WEf9x-uIxHhVad0wmdvqrVpJlM7Kz_jncucuviK4O1qtH05tcc2Y7VxO8ntISUdlQqIAsovL9jShyF8OzkOord-hT9dnaOlJGIX4EVZPsWRRdjGoDT1iRz3RStz9cX2OH4ZBOrmgpQKYf-a1TKTSSxaEAwJ-ZqqfJ6RLVmZbW7NublRtMMXDwHnEXSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت فعلی سه ضلع مثلث توافق:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/Futball180TV/93119" target="_blank">📅 03:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93118">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqGOhG6a9yKvxiyivzUdAKa3IWUuj7xjfbjhkL8ryH_q9knRDPHFIFVCxWdkBYxxd95YfdqtLNTjaAD-LaMkke5NynmhXpSWiaFwzjDIhva6GhWfgD2UKFPE22kxYpHP_z3ZGWyiyRw0HdHxpkQR92igjlr-k0rLETedZvWcNckB7kPf6mpB1b-MpfRrpIRTpiKJnzFiRQo6ptHNS4JEXh1UM8m_0-OXlwPZ-8_7u6rchkOJu1_kBJW_e-IUgpsVKniMx18JM92EIES_dUEUm0x_1KiUMeufHJPoNJvpo32Zdgj7RQnkW9VadK7aLkb02o5DtXscmloZm-9GfHwopQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐸
😊
کیم‌کارداشیان و لوئیز همیلتون درحال عشق بازی در سواحل آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/Futball180TV/93118" target="_blank">📅 02:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93117">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb26c4bcc.mp4?token=MkGU2qMs7av65p_NFmymndkhsFbvhArVZX5LoEJg7U1JGjmXdlnidXpMJljfYpHrnsPtW38jPjvJ93mWzyZPNRRRysb4p1bsA3m7D4wuyKlUwOn-A_5s8Qv9fJOdche0YAwIUdF7Ju_mX09PsejXM8Ff41g_hY2qB7C0nwGOkMLGmiSiKCx_ca3lTFcv0vo8HBzt6wCuH0Du5ueuYx4e6dolUSXrCFxihtVdEpGefC_S6w8mRtooleGhmt1LMosR0cXaYX5Hp26NaEiCy_C8b4ZzfMFO0_TOmYBsXDdHE7m3ffquVW9mQ9ozmig3bkjuQEu-5avEz12O7WwOxiUNpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb26c4bcc.mp4?token=MkGU2qMs7av65p_NFmymndkhsFbvhArVZX5LoEJg7U1JGjmXdlnidXpMJljfYpHrnsPtW38jPjvJ93mWzyZPNRRRysb4p1bsA3m7D4wuyKlUwOn-A_5s8Qv9fJOdche0YAwIUdF7Ju_mX09PsejXM8Ff41g_hY2qB7C0nwGOkMLGmiSiKCx_ca3lTFcv0vo8HBzt6wCuH0Du5ueuYx4e6dolUSXrCFxihtVdEpGefC_S6w8mRtooleGhmt1LMosR0cXaYX5Hp26NaEiCy_C8b4ZzfMFO0_TOmYBsXDdHE7m3ffquVW9mQ9ozmig3bkjuQEu-5avEz12O7WwOxiUNpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇯🇵
شادی ژاپنی‌ها بعد گل تساوی به هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/Futball180TV/93117" target="_blank">📅 02:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93116">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjMbGzrqjL6CAopYHT-S4D-GJSJOxyMHL8GF2w5CbSLfw9DxAWbJyMd0Cx8KXKzD4EDxEUAmUsuM41rF45z6VLJCt5maGK-xjOgVWSp8T_BC_DyQTWj4wE6hKY2-guukz2rOcBkmiM2cBToIerus5vEu8O2l9uaLVR5ji2mBTpxYcc-crUR60dAetn3XpThIOrYD_A3EvF7mq5V6WeJjdxAk6Yhkfm5Ksiu6F36dSC63YSOflx1gehP14Z_tCuUmrlhhCQ53NnH5bxqFFOus0KrkRQp1eJQ3Y0J8ZcJpdYg0OBvmNzZThd_L_aqMLkdmMiNlGuOGUsREuNSm1tEzAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
💥
باشگاه‌هایی که تاکنون بیشترین گل و پاس گل را در جام جهانی ثبت کرده‌اند:
◉ 4 - لیورپول
◉ 3 - بایرن مونیخ
◉ 3 - اشتوتگارت
◉ 2 - آرسنال
◉ 2 - موناکو
◉ 2 - رئال مادرید
◉ 2 - فرانکفورت
◉ 2 - فاینورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/Futball180TV/93116" target="_blank">📅 02:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93115">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🇺🇸
در آستانه ورود تیم‌فوتبال جمهوری‌اسلامی به آمریکا، ماموران امنیتی این کشور درحال کشیدن حصار و محفظه امنیتی مقابل هتل محل اقامت تیم قلعه‌نویی هستن تا اتفاق و حاشیه‌ای حداقل تا قبل ورود به ورزشگاه پیش نیاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/Futball180TV/93115" target="_blank">📅 02:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93114">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🇺🇸
در آستانه ورود تیم‌فوتبال جمهوری‌اسلامی به آمریکا، ماموران امنیتی این کشور درحال کشیدن حصار و محفظه امنیتی مقابل هتل محل اقامت تیم قلعه‌نویی هستن تا اتفاق و حاشیه‌ای حداقل تا قبل ورود به ورزشگاه پیش نیاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/93114" target="_blank">📅 02:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93113">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
دونالد ترامپ
:
«این توافقنامه بزرگ صلح و امنیت را برای کل منطقه به ارمغان خواهد آورد. بسیاری از رؤسا تلاش کردند با ایران صلح برقرار کنند، اما همه آنها قبل از من شکست خوردند. رهبران منطقه برای اولین بار رئیس‌جمهوری را یافتند که قادر است به آنها در تحقق صلح واقعی کمک کند. با باز شدن تنگه به امضای توافقنامه در روز جمعه، به منظور پاکسازی مین‌ها، نفت از هر دو طرف دوباره به منطقه و جهان جریان خواهد یافت! رئیس‌جمهور دونالد جی. ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/93113" target="_blank">📅 02:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93112">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XaSfROHgowLsJjvPb4Wm_zlJC2RP00L49iD83KS5qvjTlednIQsc0PAJA2VRgUHX11aDGumm8PnRL5d8oyfPoYVT9wjzNXiqdHRKVkXtBDLEiXxgB8pFkghAVLELwenjcIgKlNlsHceJHaGTAnMh8Ih5Rjeq5aHstibylHDZsLkqXSl_LsRGu2jbnbi6KHaNZCQyVo6SMDTcQxnITb5Ks2B8OQXLFDd_Vds-1dgzXu4LnV8pcbCaOLvvIZbKHmPfiQZyVOb2NPYE0DZb2UVsLeQFHRZVVrb87bEbT01jHt-S5YC3Yc1YTMb6Dsn9D4HtrGitTUmmlLVnEjxoYo3v6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری
؛ بن‌جیکوبز: انزو فرناندز امروز رسما و کتبا درخواست جدایی خودش رو تقدیم مدیران چلسی کرد. انزو فقط و فقط خواستار حضور در رئال‌مادرید شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/93112" target="_blank">📅 01:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93111">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQgbk1EYecZ1ls035hPhedHtDAA-1guBjwOK2seBNou3CbEv9x-hAS_VAYNOLu4BdIcZDfGFEeiOuPTMDy8wgvB1yEAyVy8Ayrqm96es2bgkBjhWwNa1ViuHzxi6YpwdZoL0G6DY8d9Z1-3EV4g6MHtYDbQLsrUicnH4QmAUwBP1hMZtlS06EOhpnv5_aOtHBbMuERB-WNF-3wNSdx4yhaBVo55k-GzFCfeOt8N8Rc7rrEJGEp9xBqpOQXW_PsAu2KH076BeU9JfMYiBgXSZoKlQIshzIDrd5OrtLWHjDFd59ciofYtWbtqiY9T-gi67HtaAXcpE_9dLTSz4jq-CqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
🏆
🇯🇵
ژاپنی‌های با فرهنگ اینجوری اشغال‌هارو بعد بازی از روی سکوها جمع‌آوری کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/93111" target="_blank">📅 01:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93110">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjHik3vPQopfk5r7UugdH-QHU1DAyoWsFTGV6rF-MSuKcxILleRXvYJ6wPepz9APN9QlP4i_I2MDmaBKoM5JUJbQBM7_T91qznkG4D-LHwBF_MQQKrbXfn4MCVkIGcxokKOjt6AY0YRmHIMLmawGzjOHNnhEXZ4TcMwey75ihA1cshPzkMnlyugIuG9Bb-5R7G-zmBuheKjrql_48lWf9_UKNk1iHpHa2OmIDWrLPzTl1LntHK39-mD5eJdfLo1EDL3ZfL92Rx_tSLHapgGB1b_jFewZ1mcCS7jVckE2lqSWHgFXJs1VO-UGxGK7p28HYo5lI2IZ9zgtcK5uF6qv8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فن‌دایک بهترین بازیکن دیدار هلند و ژاپن شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/93110" target="_blank">📅 01:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93109">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dki3TSkXBg5pG4zSpuJfZsEiY69bUAH8IK-2t9HihOz0A24l5sQpQgwrj9UtfUTsTIgurQIA05io2EjT1zfzM4oM9lzkirPRsqLcRDVOa67CskR_zWy5JOhSJJpgtGsis9qdykVBtYZYAuU7WqUqNcYgmHmvTt8bRgduRqSiw7b8Pz9mBFx0IUIiANEZh78GJFr1Imw5vxArzcLYTMWAxM0vysQtl-XWNjh4oukjUVKRNnzN0hTDrhE9VCfd-xLJ_4fiVkx-LGFH9LhNlzQV7WEn4WOfgNepGd4ehG6nUJ8RnlH3m3K9a0eByug7OvPt40ZQbTH9hbg9rfXlZcLbDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: رئال‌مادرید امروز دوشنبه از مارک کوکوریا رونمایی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/93109" target="_blank">📅 01:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93108">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
سقوط نفت به ۸۷ دلار پس از اعلام توافق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/93108" target="_blank">📅 01:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93107">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vywhXwS0WAvn_4UX4llChIfX4lPXdCsNxSyEpHZA_wZVuqB8VLobxEDWHXmAUe73Vr6kBSau-skMTK3R2oSPkkSLTl_0S6hrExw8uWZxgqxzeHJz_IWcfCY9saez-X_zPqmC-ujUpdT1d1ekx0XTHrpeOQjKY1Shaujx3FONHJMxexO3KnF-d2AAXkiVdlVvb9dbTJ_LS4XIsIKrNh74p_N36sZOAhV19zlNrmwTUZX-lQGP4l0csCzXd42gZW9PGpnWsCC0lScABXQd_RqSYr8ERjUbualiEDvMTcNnDPguHLvKkLkJMSCgWjDCf2EESwsxWXZcnVZM_zlkdqJAeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سقوط نفت به ۸۷ دلار
پس از اعلام توافق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93107" target="_blank">📅 01:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93106">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSn97WnOXr-zTSPSnoMBSCzLmNV5aAlmhn_Bs6ANosOEBvBYlxaMSKz8DhKXUWw5ICtSaGtmKV0_tz7EzFMzYABRLn-lk42jdRRJaH5sUDviRx3rZ87QPMw8JoydwYI8E6V7XRimJBKqREfZz3-pUW7XpE6zkxESikBZUKNYzFq6Ng6K1DQeRthl_mXNcuhPcWxLe6fX-W1xJLjecQdGX4TQjXk8FLK8ebaZ1vhsH1ox17gDoqkIJDWDUu7TDUCHxMAPvkcCPHjLuYp-9hfSqJ1H3jPm0TaTZkBe2wUjRBMPSc-NXZtU3kouw-b6RVHQ58L5EEZy2FVAKGFF4uIN0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
جی‌دی‌ونس: به نمایندگی از پرزیدنت ترامپ در مراسم امضای تفاهم‌نامه صلح در سوئیس حضور پیدا خواهم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/93106" target="_blank">📅 01:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93105">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/93105" target="_blank">📅 01:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93104">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Se23xvIRBWDjUiqDmhgL5Km-3q-bJujjOvbW8ochRZp7vC__DR-DyzrZpFfgofYq631tWyjKDhOgdkSGKLLvn4EgxhNGT4U32m9HoBPQ0AIpKc7xk-J90IzgXkmbnx69j5vQVSNXC7xwR9uYy8Qn1DeBcEFXGH2EDkbyH1ypMjp0CL8tvIp6b-Ddx6-RyFOGw5n-dVACNMqJDR7979JqCv-VsxVqSKCE-1FvAHyJQhIho8FaS2ziVyw-HxmhLVoK0nBfJlaQ5ZAqP57DBCp1RUWIzEC5ULIGGUoKbbtIxC1MRLAYggMjdfu2iesSST0VhXA43xOoyjpwMNh1r8_qQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/93104" target="_blank">📅 01:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93103">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCDiNxcYCDF8dSHWbFwwe4_6QaI7I7aMMaJNfD1Myhzn_-dxziIpCVsUGZuciA5AGnKKOCiez-Z3mTulwk_4A3uh6_ptQpOiqlVlCAeKURAQ6pUueFDzmjoCuPX88qAVFvhOwhsG9XwKy0HBIVScuKe_k2K4jpg1nbLDZq4SHGIhp7UIqsqotZdVtP0KuiHcGNvZP9bNhWyPg4MlYzbW3vhSDZqE7kdSjRMTcaO_mtNdhPGEc6A2b_3EDKuF_kzJEVT8fXSX0OqTcGDCTHOsgRMDbQjgGukaKdwtt3le16r6wLWvHHIYkce-gWtLVeGwqehBpP2ZfaSz-fyCazf5NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|جذاب و دیدنی اما بدون برنده؛ نمایندگان آسیا قصد تسلیم شدن مقابل اروپایی‌ها را ندارند!
🇯🇵
ژاپن
😀
-
😀
هلند
🇳🇱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/93103" target="_blank">📅 01:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93102">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcuPgG_TXrl0LX_ZysByPZdbMC1oE9qj11icSOgMFSh4o031NFrLrsPedktoDyyDe9A0ODoePLcgge2XhAa_AiwAq7RACoGrr96XKFRZuyNy0cYpufCosWXHnPrVyG4D_LRjmJa2QCzsXxgrRGaslKwn7HtvDrKGdNqjstB-mElI14Aij9qnjD1txTy4IBSwFQiBwBJ7cDXGZTyeIldnhyCWKBW8V9bK_dz7QheNXPvqqIxh5nESGun9Jg2cZ9G2E1p_gCKAweA53non7O1F84r4MfyZDKbZKEo-ImviKqORGH_Oh3woKuQZiKxGpCqipoF-naCQdcH2uwiBX2VLzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به بازیکنان بی‌غیرت هلند
😒
😒
😒
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93102" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93101">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🇯🇵
گل تماشایی ژاپن مقابل هلند دقیقه ۸۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/93101" target="_blank">📅 01:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93100">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/848488b7c2.mp4?token=hYcUbaxBHGhYQ1Tumq6BQbIDW4f9ceMtDatvPAC6CueA2xMyZtloSgjNAVIjsUETq44R-lip350-sI2aT6h2ZBgl1uTqkuXgP1o59I9y3Wx51eFzOmpSoOZwZLpdQgTtCi_DkIRRXU1ofRtH1qazzBTLhehPyhJFJkbhEnXJU4jhYo0mTcSUI16gxoU9Y_dkeHHmMCWKMvjOkg8LFhZQYSYvp0sGb4iC8pYo8rYl2kYSKgqCRY2zhkF-Im5CTDbXWEB1JGlTUL4qre4xoxPYICyq7iAcZcLk5sEvJjZOKGpBTdl5s8-d2FZRh7e7_SJPUd8p7juDtGVmHo2W3T3y3w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/848488b7c2.mp4?token=hYcUbaxBHGhYQ1Tumq6BQbIDW4f9ceMtDatvPAC6CueA2xMyZtloSgjNAVIjsUETq44R-lip350-sI2aT6h2ZBgl1uTqkuXgP1o59I9y3Wx51eFzOmpSoOZwZLpdQgTtCi_DkIRRXU1ofRtH1qazzBTLhehPyhJFJkbhEnXJU4jhYo0mTcSUI16gxoU9Y_dkeHHmMCWKMvjOkg8LFhZQYSYvp0sGb4iC8pYo8rYl2kYSKgqCRY2zhkF-Im5CTDbXWEB1JGlTUL4qre4xoxPYICyq7iAcZcLk5sEvJjZOKGpBTdl5s8-d2FZRh7e7_SJPUd8p7juDtGVmHo2W3T3y3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇯🇵
گل تماشایی ژاپن مقابل هلند دقیقه ۸۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93100" target="_blank">📅 01:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93099">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aW9q31hinZCsAhQTUnF4U98wqe_kjmWJ3JyEHrUHRzt4gUIuWu7OWUs9G6HRw-h55JM0CqXBXBvgfQwdgLHY4XfPaGWMZ7MnhGwGSsBL6t7MafKztSioiyuoFCBAMnWLnumqDtt-iY4ws7ar39MK6vA-kRjFeoKgREmeDe0y81ArE6oxtqxOpRUFnbGl-mUdhH15b1JYk6IM38nj62J3xV-jXIcTWZi8atpFWw0wvtRM4eJUcF0KfadIJSrSOhROukYWCyFWKn02BvIDTTDRERcBTaDtb1TobYIUWWLHAG9x7M9wNv6jFZ_vG8dU7W97ZANjFcGsv0Xe3vlMoN_XlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇮
اعلام ترکیب ساحل‌عاج مقابل اکوادور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/93099" target="_blank">📅 01:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93098">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ژاپن مساویو زددددد</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/93098" target="_blank">📅 01:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93097">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گلگلگلگلگلگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/93097" target="_blank">📅 01:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93096">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D8IZEKB6ONsbfcNKiCvtm4e0OqjUyoDHJs3yheOUNBL1_1lhdRQCK4zb_WzReKzt1zA20-u-xLJnFwYoNQ8rjxSj11XgMMIBgj6MItzXnuZD4zcKwE6QYOwsHhV139GOweK6ZNKRH8La34pKdFDwohgLeaqdUMWXHynD_GJikditAoBzraLxfsbC9dYicg6W5roVoEiLvcaI2m66Z4h3w1gvCA2wA2RdzV7FcbHww7l_sbzgfkuEEoeMKcxujyD7gNn4Lunrk2ytCoUyrIfAt7dIvP8FWQXpB1s8QEf3EU3RvpFrmHaB1MJTeWrcw8gTDKqh2BY4T8dnbOFU23yG1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😔
😔
صداوسیما با اقتدار اعلام کرد که جمهوری اسلامی برنده جنگ با ایالات متحده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/93096" target="_blank">📅 01:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93095">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NYWliR5-7Wvxkz9TIuj216FMTNYHQfqXmFwkq7SgvFFYn9rwTbELNCyfZak7-4ZGcLS1MkbNRDGYJ81hEztKOJbHpSmml9-i36YsvyUueGo9D4OytyNL4Rf1N4UiJXQDwMcpLeBlg5__xP64hKJoLyQb7y7UkQS76Rqs7scvjjQJAVyA9cfbjER-mjDuw2rTUuFeQSjaztIkYKcJaXUkDYnHnm4AFIa8KvFbz7Xk7kcJVcXnxT54FazUx8xYfgnxlgap6Uh5qJKJeFcSw8OPAmbcPWNfOYaEDbjVfyshASeZ2AkzYYanuTD06Bfq4uj1pYAhctUzXoX-VuXjoFxSWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇮
اعلام ترکیب ساحل‌عاج مقابل اکوادور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93095" target="_blank">📅 01:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93094">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edf1267e6b.mp4?token=bnArXaLFz0s6kD2IhmUCubEp8Oy8dJlfqaPRXw5xB8T6smYz0HV8lkSZJ29Uu60frdxwlot5dckoaRf7tzDqg2JWxodnA5ptvPd36-bYxoJ01fWjJy8N1beQYCUzyeo0OB8dK7pf4ae8-K8HD3fjR9AgtNvSB5JsY__tMGwA9pnud43BGCBAhHPD28hjm5BYjBeGdOTrtIN4LZaj-KReVra429WCgI9z76MvcX0B0Sogyl6D2i-Z-aIoTubMS50M_53HP-y3IVdrRkWOUBhLObNWjSEoSfxpK6huoHLSkAyJ_yscZ0S7teYXwfIVGLXP0g9BWHTDJLCL9LtzgdMQpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edf1267e6b.mp4?token=bnArXaLFz0s6kD2IhmUCubEp8Oy8dJlfqaPRXw5xB8T6smYz0HV8lkSZJ29Uu60frdxwlot5dckoaRf7tzDqg2JWxodnA5ptvPd36-bYxoJ01fWjJy8N1beQYCUzyeo0OB8dK7pf4ae8-K8HD3fjR9AgtNvSB5JsY__tMGwA9pnud43BGCBAhHPD28hjm5BYjBeGdOTrtIN4LZaj-KReVra429WCgI9z76MvcX0B0Sogyl6D2i-Z-aIoTubMS50M_53HP-y3IVdrRkWOUBhLObNWjSEoSfxpK6huoHLSkAyJ_yscZ0S7teYXwfIVGLXP0g9BWHTDJLCL9LtzgdMQpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
صداوسیما و اعلام خبر توافق با آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/93094" target="_blank">📅 01:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93093">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJfzNOgka02A5Rsr1hLHIauBcn2_BuaQwb1sf0oxDgd3oGLhh7_CBaJautPbztPI92OmklrJBTz7ppsHVd0Y7TyVWTzsOaspVV2y1wcIzJkdFFi_D6tp0RGMuVavGy9-vUKfurS2G6WlRQznf7gUyv9MP29jdPUOqw3BwZYvEb6v_NpjJOMZ9RLs4ie2LUJi6IHf2Hk_JHsfI_fLvppSU0E17YPFWMmkCul3-ptPclY3hxQJnwJT5cz8d9WggbWy_rDe_I6kUzcC9lc7y1VNzmqgUKeEYHj_lKEB7-SVBM6hKSyyLZNFByRc6PG1Cdoc40G2jeHUm0BWqQNdJDjVlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
🇺🇸
#فوووووووری
از ترامپ:
توافق با جمهوری اسلامی ایران نهایی شد. به همه تبریک می‌گویم! بدین‌وسیله من به طور کامل اجازه بازگشایی بدون عوارض تنگه هرمز را می‌دهم و همزمان اجازه رفع فوری محاصره دریایی ایالات متحده را صادر می‌کنم.
کشتی‌های صلح، موتورهای خود را روشن کنید. بگذارید نفت جریان یابد! رئیس‌جمهور دونالد ج. ترامپ
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/93093" target="_blank">📅 01:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93092">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjPLQm9613Wj0m6Y7cRkgs3w37cTmQ97RrMBunyCJpVnJggsxFGNtFYYSeyc5GBzXNC_12NGRpxncdxdP4F5mIddGgGQQT8H7FyNiPDR3nPhlsYl9uzlPyj5_10KmlODxDiSf4jiYzeTfiMuRtfoxON8cTGQi1ND1HmfG-UZWwp6Hbven2uXCOfTdmM8hPaHB-9EOsx6udDGHnPAY16bVktEcplnWK2MI-SZRMDWfm9A-LLkFJFj3y5oZEMZxaozq-emC8ZUedt2LfabXatjE7FE4vxMgt6iRZsNwU8dYHFBl-xP1dfaADpTktRWhKHT-u4qDti2-hvuBoII-OxoGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شبکه خبر هم خبر توافق رو تایید کرد: نخست وزیر پاکستان از دستیابی به توافق پایان جنگ آمریکا علیه ایران خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/93092" target="_blank">📅 01:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93091">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/58579d5699.mp4?token=BmDzYTU7OoQflmMKEgO3EiopKoMA6VqiX7CPGwQzMxKN0nSJxDHZrennj_V0TRlWKNVW5JNua2arbFiAeU6-bS1wnjFL3lcT-AoIy4Glmip3qHK10Dxqoa2iDebRdBJsVBuXxQrHJ2lI85GsneURubSgsm-fIcgOAgs-IdY9BsmrCG3TNmCdCFz03KVJm03czdPw8MKIPo_Ik4MiZsRXYQlsz03mS1kJebwWzRbERH1aTrC-0Qy02QMUi2TTNWg6ui4LxpWD6TS97iXWIUEoftjWfnkMnB6pzk8wx1XdjxpPjhqbSCMDVUDghcEnWRTp6hFPhcO434MIUvGcFg9XaA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/58579d5699.mp4?token=BmDzYTU7OoQflmMKEgO3EiopKoMA6VqiX7CPGwQzMxKN0nSJxDHZrennj_V0TRlWKNVW5JNua2arbFiAeU6-bS1wnjFL3lcT-AoIy4Glmip3qHK10Dxqoa2iDebRdBJsVBuXxQrHJ2lI85GsneURubSgsm-fIcgOAgs-IdY9BsmrCG3TNmCdCFz03KVJm03czdPw8MKIPo_Ik4MiZsRXYQlsz03mS1kJebwWzRbERH1aTrC-0Qy02QMUi2TTNWg6ui4LxpWD6TS97iXWIUEoftjWfnkMnB6pzk8wx1XdjxpPjhqbSCMDVUDghcEnWRTp6hFPhcO434MIUvGcFg9XaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
🇳🇱
گل‌دوم هلند به ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/93091" target="_blank">📅 00:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93090">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">با اختلااااف بهترین بازی جام‌ تا الان</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/93090" target="_blank">📅 00:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93088">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/93088" target="_blank">📅 00:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93087">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گلللللللللللل دوممممممم هللللللنددددد</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/93087" target="_blank">📅 00:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93086">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇵🇰
#فووووری
شریف، نخست‌وزیر پاکستان:
خوشحالم که اعلام کنم توافق صلحی بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شد. جنگ در تمام جبهه ها پایان یافت. مراسم رسمی امضا روز جمعه، ۱۹ ژوئن، در سوئیس برگزار خواهد شد.
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/93086" target="_blank">📅 00:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93085">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f8d5fb15d0.mp4?token=fjAFANxCLb0OG6p1-69IZCMmvoZOZqY7e-JH5B0ns08IXY4P35ZF494L3DdSr2Ewy3Z0TVJfbEBoBZD1pH3bkhsEKBlMuFBeNu9M0YoquSKbtrXCCpn5WsiDTg6DoVs8NxTtQGpVv56297u8atxmy2t0rVT8Lo6vGW89k2wIVZfvQ2GpZuGvfNqP1ORCHdrsri9oiTUYsDdeydk7iYAlLwKTK7w43YRqLSt9vjPOJmLNkAG2yt9nLIBGWIUqvl8b2NrlGfKvOjXMQzUlVT22mmPNmx3wpetuk7nTVgcAPl1Qu3M8x_H9uCJpcI_o-TpVu5g15QF6_cFfKLuCMfEQxg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f8d5fb15d0.mp4?token=fjAFANxCLb0OG6p1-69IZCMmvoZOZqY7e-JH5B0ns08IXY4P35ZF494L3DdSr2Ewy3Z0TVJfbEBoBZD1pH3bkhsEKBlMuFBeNu9M0YoquSKbtrXCCpn5WsiDTg6DoVs8NxTtQGpVv56297u8atxmy2t0rVT8Lo6vGW89k2wIVZfvQ2GpZuGvfNqP1ORCHdrsri9oiTUYsDdeydk7iYAlLwKTK7w43YRqLSt9vjPOJmLNkAG2yt9nLIBGWIUqvl8b2NrlGfKvOjXMQzUlVT22mmPNmx3wpetuk7nTVgcAPl1Qu3M8x_H9uCJpcI_o-TpVu5g15QF6_cFfKLuCMfEQxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
🇯🇵
گل‌تساوی ژاپن به هلند توسط ناکامورا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/93085" target="_blank">📅 00:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93084">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ناکاموراااااااا</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/93084" target="_blank">📅 00:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93083">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ژاپنننننننن زدددددددددد</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/93083" target="_blank">📅 00:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93082">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گلگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/93082" target="_blank">📅 00:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93081">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: من علاقه ای به تغییر رژیم در ایران نداشته و ندارم. تحریم های ایران طبق توافق برداشته می شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/93081" target="_blank">📅 00:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93080">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
#غیررررررسمی؛ توافق موقت ۶۰ روزه ایران و آمریکا رسما امضا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/93080" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93079">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9d2bccef1a.mp4?token=sk3T6a29UHIjC4LePk7cYhVcpMYF9y2DHPfX-Sr6uaEP4_5AeoQly5vMsa51DriseXEhDSmpc4uNDCMkYf41Sdd4kHGxd5BdLexksgL7ylno4VN0G3USbEIYGOSJ4En_N1HMEjj_mrIMAokIm0f4zDIuwrRDimjbrCsUwXAD7Ekru2rPX8GBkZAnov2OgAl69LSVGabZTnValxSa1rLMXcWYaflfQNNacz8yMbk0TIRaAg6nozoeZ3xmKu2dNCP-IFaHHfNxzq6DgnRIEnnhWqTDWEOJw8Uys3C7YqfnZOfmG0_6rbcVUZdU88aEMygE5kvZ6sjRv85Ek8-91ShyBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9d2bccef1a.mp4?token=sk3T6a29UHIjC4LePk7cYhVcpMYF9y2DHPfX-Sr6uaEP4_5AeoQly5vMsa51DriseXEhDSmpc4uNDCMkYf41Sdd4kHGxd5BdLexksgL7ylno4VN0G3USbEIYGOSJ4En_N1HMEjj_mrIMAokIm0f4zDIuwrRDimjbrCsUwXAD7Ekru2rPX8GBkZAnov2OgAl69LSVGabZTnValxSa1rLMXcWYaflfQNNacz8yMbk0TIRaAg6nozoeZ3xmKu2dNCP-IFaHHfNxzq6DgnRIEnnhWqTDWEOJw8Uys3C7YqfnZOfmG0_6rbcVUZdU88aEMygE5kvZ6sjRv85Ek8-91ShyBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
🇳🇱
گل‌اول هلند به ژاپن توسط فن‌دایک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/93079" target="_blank">📅 00:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93078">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فن دایکککک زددددد</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/93078" target="_blank">📅 00:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93076">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">هلندددددد زدددددذ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/93076" target="_blank">📅 00:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93075">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/93075" target="_blank">📅 00:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93074">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
#غیررررررسمی
؛ توافق موقت ۶۰ روزه ایران و آمریکا رسما امضا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/93074" target="_blank">📅 00:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93073">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آغاز نیمه‌دوم بازی</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/93073" target="_blank">📅 00:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93072">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پایان نیمه اول
🇯🇵
ژاپن 0 -
🇳🇱
هلند 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/93072" target="_blank">📅 00:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93071">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ژاپن دو تا موقعیت عالی رو از دست داده</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/93071" target="_blank">📅 00:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93068">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PvvgwFkzaGsP2BXNCJ4j-zaB_Tn3rvTE-Vi1ZyyFtKjUQ2oX1v8v7ZAOXConlRxpz4sIJ2b05J-fAaPDpoeki4IDplvaMysJiQcD78a8s2A5Ujagl850fTxLyqnitLl5ojqpU3TMKPVRmeu7vSWhgv3kcsn653jLe0KupK0tvNP99CXYWYseROZ0Ex8FyTO8BC8YR-xHzwOzHhBsABonTcPDfThjShcdxEVHssDn5VUx0p33Ys77FNHzZmcDj6DZni4ecbTxUsk6QKYu4FSlmiqGjQUJ8ezCPqQ48RKNWgaa2llegV-Q_CqUTG2Lmj9U-924yS6tVaky8Hjy8zyu4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ay2LZg7jwJYGLsa_EXNwKIzmc6J3l18PdgKBRmBaPJtKWn6Cm25-_v0ejOPMT_f6oGhLZCA8YEFoGOnWXsMeMqNMKtiRAFoOtZJBJvwfJeRFbobV1Oy4yIOe19jYK3iNbo3aBF9Gky_QdZVHVH3QybSbnHJ7dHT1xBQKxiCKsuDEKM3AXQ4R9ekkiZjX6BqVuvA_-YnyQQk_a0ehwnYTIACipgxeW-VOErQ7muj85-wKE3fsZAU02sQGYHa8lVNCqyX6T-zC9kdDphNn_lVmWp8REfIXH5MXwKQjIhVCNZTjwEVnn-LZb1DSMoiMnmBtCYRcickn3Mu49jC8iqgfjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GomSLF8zzk76vDkle8mzq3jXkL2BvmUBEJg2NSK8ArJqWHOe9MunNypv7qhrSdOQSgqUVYbiyLIRX3tmd1XKtHaQME6PG_mvlVsDfR3A5uuZ0-qstiUxfmpaxlUaRcmwblQkuyixB9iDqyqcyXDJ5Ki79kTtKaX6NM2-cNe7QKUl0h9V_kOWEzSWVWY2ukwH7-K-lujs6b6ciwcbr_vTdMhLSoSqR9mUx7vPCdMRGNjgjl3K53V45iaSzeC8D22vQGQ4MdBqX7BzWW_nuwkkLg7zKaCXkw2d9N3bRsuja7cTnYxzhLodFEt5eaRj8GtdDYJg2xMPaj2qPo6Y5l8_oQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شات های رسمی رونالدو برای جام‌جهانی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/93068" target="_blank">📅 00:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93067">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سوپر سیو گلر ژاپن</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/93067" target="_blank">📅 00:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93066">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">۲۵ دقیقه از بازی گذشت کلا یه شوت از دو تا تیم دیدیم</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/93066" target="_blank">📅 23:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93065">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Plgio1EnWOe5sv0EUqaLou5wMbtmt3hAnr0868wVroeTkQaBulVaDI4hxULtM2l7-6eJocXyo884dAugnOKB6_ljwICNl2MYxvAbqHZCu5TTzJIVqhXcVlQ70COP-o1KH3ROw4dUg-vfPLfO6vkVQZfSFvrWaIvq4D-me496mj5BLO5k9i_jj03WdKSleOfovUEjtwaQ-BSNE8PW8AjF_9s2EFLN8ZxN2KMd6L70PHIWPvZedsVEhqJVICJ2rnh_h2JmWgX3_-oyIu_C-Tm_VZYqFYnX3Dxjl_HFrPAFeTWhh34e1rWCWsKZnPRpxiHFXOl627yid-arLYGgOSf0DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لوئیس دلافوئنته سرمربی اسپانیا آمادگی یامال را برای دیدار با کیپ ورد تایید کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/93065" target="_blank">📅 23:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93064">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سوپر سیو گلر ژاپن</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/93064" target="_blank">📅 23:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93063">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">شروع بازی هلند و ژاپن</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/93063" target="_blank">📅 23:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93062">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCOtNg94PLIGwRMyhAtpykWtva_JZcYBILy1s5ztDDAcrr9yUKuZTMJpzNLbPzEhE-Itxuo8tLER6qytF_PeFkbe1hnYv1WmFS6rJ5mdZbw0oJGxI3sRelLsEM9LHhVsIMjpnjY9QC_yMd4ME5Gp7wIMf9Eb20-SKSRlOTxzz6RcA1yru-oBNySXaS4va9Fu9waZjwab8JGoeUA_8Yq1yS5-yADc9KawD80iBp5WVmHG9Yzin5f5yn2PjF4sq465jOOntwEAccb7cURsL9e_OofAzbZ6qDcayBI-1jdOjrXSVWYsmy8I5QN7QC2CBOViiybpUVqejGpiiHha1CbDCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو:
ناتانیل براون به بایرن مونیخ :
HERE WE GO SOON
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/93062" target="_blank">📅 23:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93061">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gffHd1oWXQPloG_-KFJFCKLgAWPVq05QRFgueCXYASrjxUVoLRN3Nc7UnkIi5uKEm9nEzYg_TbKlANHXDBM0Gzpaz5xEr6rXhHnYDldSbt3Ezz7tpbRm_I5wjG5hNF1_paw5wO3Uwz-TmCLnEVkQCXazvFoIP4XETovyR8tRVwXXGvMMkPRUJF9iA-8gr_pG9OM3FEVP6EvBd8PTcPxfn5CyJSHr92pNT9X5cS6Jcx9OXuIQXzmlHYR-dhE81MExff6SxlDykx58OGIpn6brZ4-KCJft-nvgQ50caxhbW92-SuBOeJnn6UabrdlOZBRdh-I_eZEl-2iGeuMAuqZuQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کای هاورتز به عنوان بهترین بازیکن دیدار آلمان و کوراسائو انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/93061" target="_blank">📅 23:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93060">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بشتابیدددد که فاک بت آنالیز از بازی ژاپن و هلند گذاشته سریععع بیایید و ازش استفاده کنید
💸
@FutballFuckBet
💸
@FutballFuckBet</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/93060" target="_blank">📅 23:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93059">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mni-1W0eUr4Q9bsly7ezma8dvk5lzNIbCYiWhEPYU2Zuuh-LADsUoMcUF9il5Fpe46r3722twhJytGgmqCoQWSJr0Z4suFiPA8qIZh40ehaS0JID8m_tsEe53aQsPJOHphZAuWMQHh_trXZYdrUzi8cYi1EboDBG1eOXsXAs0a1Nux7nnbYD2DxWjXyh0GU5mHaMXhPRRWzoNpn33prXSnAzwjsabTq6Oo4o43BF64GzeZgbh8iAIUmnHsu4AIfgBOmaeb5UMMoj7hWJSvgX_q3eqxgjtHYZNLOMbIvvERVPKIf7beE9neFxZ29ju_bqIEd19fS7foZVQ_9QzZ5awQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇾
مولینا خبرنگار اروگوئه: آمریکا بدلایل نامشخص اجازه فرود هواپیما و حضور اروگوئه رو در کشورش نداده. این درحالیه که کمتر از ۳۰ ساعت دیگه با کشور عربستان بازی دارن!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/93059" target="_blank">📅 23:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93058">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXSpYgV4_Iavv1cyvRxxndVJt8lXxwnfqDOkMfoFStxdV9NiKqmThEvMESHeIZ-AC1xT5fFhaE9ao114ZgEH3PMkuj1WyG85ZX8A-OtiWj77wCsWH66jiQxhbgnEK1Pay-OCigGTq9xFW7kB8Dws2eh5IAoC35kBPZCVEyBgYOLqsCVeO204Xc0M7JCcDqkLi1uRHg5ZK1dIBlPiCdqw0ivDkdMPBgeITuFrYiNhBuuMpJIfWwLGN7YOoRUMjcf45dgW2JkqMzuaxtZvqGjXfI-wHPfkMOfhxzoqguCJvmm0W2q_repmwr_cQMknd1jykTmNdHVcjUQaxRVi02r84w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوش و بش یورگن کلوپ و توماس مولر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/93058" target="_blank">📅 23:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93057">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0240278273.mp4?token=oEs1KKjoLUKWyg5OqlejSpdF4eBiNUIOQ9MYT-D_B6BA3D5OliH4EQWxOjlFg7UGmMxMlVDsfq9pF9BRVwFsFa2m8zFzU6zKcLU8BvQlFTlNB7DKsQNhMBvTcLbb4MnhgaNeXYIZVFudihz961rbeDd9de1JRAwPWxKmgvFfikRHgUnLkX0yvJjlMFVjpA58qSYEReuXZ0UcKI20kjV3n-uUPoeYy2bKvtGKSchuCNjHuqNybg8w3pr3gtyE7KjyzwowRKZPByi2JxqxxFHymCHeoYlm8Jcojpad2MJB6jasENJUFcDLyIPUBXGkFkAbZnmSzL-TY91u-YJQMDtvBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0240278273.mp4?token=oEs1KKjoLUKWyg5OqlejSpdF4eBiNUIOQ9MYT-D_B6BA3D5OliH4EQWxOjlFg7UGmMxMlVDsfq9pF9BRVwFsFa2m8zFzU6zKcLU8BvQlFTlNB7DKsQNhMBvTcLbb4MnhgaNeXYIZVFudihz961rbeDd9de1JRAwPWxKmgvFfikRHgUnLkX0yvJjlMFVjpA58qSYEReuXZ0UcKI20kjV3n-uUPoeYy2bKvtGKSchuCNjHuqNybg8w3pr3gtyE7KjyzwowRKZPByi2JxqxxFHymCHeoYlm8Jcojpad2MJB6jasENJUFcDLyIPUBXGkFkAbZnmSzL-TY91u-YJQMDtvBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کار جدید حمیدسحری با کپشن:
آلمان 7-1 کوراسائو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/93057" target="_blank">📅 22:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93056">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLvQAiR3HfgNN9BJvUUKS_WYilGEscoL7jwRs-vYxASUPbOd2QbCr8AVmNKOkViwbwct_02Z2lXgPoeFeNm6Dg3aOLON0Cso6MXiXfCM_qdydD7PNafcDdSYxrLVeXRA7-mJYZDAi2h7900AUZKkHpEkwxJZEQ-IfFP2iSlUvYKM9H-HTI2w68lQ3T6gsxR0mKoy-t1vLj3U5T_Ob_3Pq_LwUGc9wMKysUoQEq7a5M0nK_vRb1QnxflWEMbhRZAgB1bzqHg6volIO_cqyNcekAG0YdR6Jae8u4X3XLDDQwzPUFLPMsBQPoVAxFIO3k_H3jg5AkjgqTkTVASdsx_ZtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلمان عزیز امشب ثابت کرد با این حجم از قدرت شایسته قهرمانیه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/93056" target="_blank">📅 22:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93055">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">➡️
فصل قبل:
❗️
یک مدافع چپ جلوی یامال بازی خوبی ارائه داد: کارراس در بنفیکا، که پرز جذبش کرد.
⬅️
این فصل:
❗️
یک مدافع چپ جلوی یامال بازی خوبی ارائه داد: کوکوریا در چلسی، که پرز جذبش کرد.
⚠️
پرداخت بیش از 100 میلیون یورو برای جذب دو مدافع چپ، تنها در طول یک سال!!!!
﻿
وقتی فکر و ذهنت به جای تقویت تیم خودت، فقط روی متوقف کردن رقیبت باشه، شایسته موفقیت نیستی
😉
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/93055" target="_blank">📅 22:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93054">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0jQjAeWtYs5dItrru4dRuCfIpJCSjh7Nm4roOU2sOEAu0MPm8bx5EewS03pJ8QVnOxoxQjhHNWAfF883-7bVDhTadWby9RnGOm2sI-MCBX4t1WIWvNCQVUV4c2Snt0zGaT87Hc7RUuQGbGJdFPyjHFhl15MFT7Ea5LoPf5qRNYfEawdSu-j-QIE08rHZo4TvBK9tjULNsFI89iJS8KNVuo3ecULKkXiib7ZNeIz6xX_HMctinDC1-4CCQZdX_Oq95Muo6mIlXNotCj--GKq20qUmZl2Fgu80DRZGbJdGbzpp0j3kVNQoXlVwE9cYp7uHWtb1ILS0E1l61wnAAHQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از خامس رودریگز مقابل ژاپن در سال 2014، دنیز اونداو دومین بازیکنی شد که در یک بازی جام جهانی یک گل به ثمر رساند و دو پاس گل داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/93054" target="_blank">📅 22:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93053">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbQ4p9kd6yl9xHrABiszmni1bDh2DzrcryG1cE_DJ18FuNT9ThRNpPmdZYx8rJzeYTKkkGuQgW0AKRqt2FGoopUxLGgQDnAjduOo60eehW2l9vvgiYgssBjnAOeKFdmQolT1RPamEpvQVS7OwZ7TbWSlyBhE3e3nWqivqhlFmPmMfrzz4GrT0PaxU8T1tqVFuoADm6ho91HzEGYIajqa10Xm_KFi75TVD9sWt1IIbAPZZfLwMfydOw9KTfdu1ZeDxPFL5XeTjk0yJJl5jmUQTwb8npGs3g7_-wQg8mwBJHnT-ZXrBm856AJK6c_dmdJoqK1tQtXew5j71gKrdttrow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
تیم ملی آلمان در 10 بازی اخیر خود در تمامی رقابت ها پیروز شده است
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/93053" target="_blank">📅 22:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93052">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پایان بازی | شاگردان ناگلزمن اولین گام را با تحقیر حریف شروع کردند
🇩🇪
آلمان 7 -
🇨🇼
کوراسائو 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/93052" target="_blank">📅 22:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93051">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icSj4IH4GQPoqtx0KZoWHOUazunxpbdUlh2HMibHTaBPv0s_4BZ4NjPlcBzqRJzeopyLrQvc1kEvHRKKEK_biU1EAkjMYo4O0MidY5UiPGixpSsYyKqkikTVYpBFZHuWxckPpJGc6DDKjafw2m3jqcup1pW9OQ7Taz3g3kYOqW9FLtji2TpHNHoAj2u7bxOmZ9nKyDQ1QLO99zMleOJXyaTyT3ilbmrA2n3zfj5QOcw7hLzdFtC4AilM-aMUbeUwC3evGwqCnUBNqSd4l2mL2rpTTKkHaqi_9J-Xs2r3T2wg5-YjBBXnFUdFuIeU8z-9XyQwJJ1Pkg48btdbEVpJSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آلمان جلوی کوراسائو ۲۷ تا شوت زده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/93051" target="_blank">📅 22:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93050">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
#اختصاصی_آبی_تاج_اسپورت
🚨
Coming Soon
🔵
🔺
💣
💣
💣
✅
بعد از محمد خلیفه و بهرام گودرزی، سومین بازیکن جوان و ستاره هم در حال نهایی شدن قراردادش با شخص یکی از اعضای هیئت مدیره استقلال است.
🔵
مذاکرات فشرده با ایجنت این بازیکن از چندین روز قبل به درخواست شخص تاجرنیا آغاز…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93050" target="_blank">📅 22:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93040">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D29-yxYNJuCOqV3CVzWnyJDE4ycgmrQk2wtJb8xdIfosUSNin6UQfBmV34d72dxkWyv7Y2qdAWMNLMqGlcyTKzAtzvpY-67gQbJMM1EUUGQmD7TAIKCcpuvzS02V7oNczLLix-df9yQ5tGza_O83B0oEp79F4_3dxccqlgi0LsvYKZQ6KQC2dQP7Quwwhm6P1WvN6VuZGKwOFAyrKjWP25HZ2IIpi0jju0AxI3sWX-lv2bM5Kg-xZNJCKGEUuBH0E6gB_nhalInDTm_LRamMm8kdudftEGaMHy8v14rstzTLJhBXsoKouwopjJ3Sh-VWe61LXzsAoIDs_JyKfg_H7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAL2vkfTX_cXXXulVTvC0DnZ-PHyjkY9NrPHugyjSX8Sbtwt8U55P-oje7W8Y9Blu7oJedd04EHnQS93naAeT8tl3zevWHmo3Fo-dkg5ynREa3BwjEwWxcfcdsRfE87NgaAbIcM8arE8Ji44P1nvP3-DAIB9xC4B2v78V7T3ACRWm4hem9IvSjnhgFa37YjbfU9nyL3D_nqJ0Jhm1XRBH6bHeE3BuzDCj-h28P85DEkZRc5gWmh-p4Cp-SEaFettJF6NF5tFl8lA2d2hN6wLbiLYXvr7mybumBHssDU1xveL5jWcrRNI8Z-kvNPzDgn4-nf-62s6SsIa8a4ShYviow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dtmaB_1MUnEZjdvbGOBQK1hKe3vqy9RzUaPfe3X6-GIKhqsMpcZleaCAXL_gipELK4FDVDEp45bpFhoGxFQHZZZEsfOV_FDqBYL-dQ87tN8rUJP8jbTHuB2Eiz59psM_V6Zm59Gw_3VZHzEKT_0TMkDDgiQh8w-bA1aSSrgx6fZIXLmKj1CE7s7xwT3jJw7SJoJvMAIXMIawrSa55fK8lFrPgWvG5MOlhg68Yt0EPOQnhX6OAJDKwGZXH_AHCKeXnrggZ5yd1ICdSjfZ5qKIBRjORDZut6-hbuPuAqZ7lZnNmHZQ3WNm5Oqj6rcVT_sIFa9tBNL3KnuCCc_mhEIDMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G3MXbFCtzS0AWm-3ZQaaXmdFXf7_uND378E0KqCIhhqjS0hi5BmODiz5t7gHbn3eILD11ToZ7pHMYrYv1Z0aFWjkwjuLl9xQ4fosnncMH_sQq4yMHuq8RwZ_Sq4M78bKmchelHay-5JYACvqVxDR9GwspjU2W4tVDqE1S1flHcrpTW3eX-Prn6xt78vHznqtfaxioYcrczOTonPU17H3Huyf3JNQMuCR6aEbeD_I1fj7KyyNizDsUBHrdyPWiFcbskNWd8prMrn1zULsxB9bSdLm5jbz2kWe7jlQJz9VxqHv0RZ5Tlns2maFJ2Dg-a46pGzvBZtE578lSBLazAURew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kE8HsH7fEOGjpUoDsVozz_U3SiZCucqsJ8xwelqNFrncmtLPajyz-xazaBwKpHfMf9vJiRxEC4WgpQpuqb5dMMaU4lHHEG1jn6nXRod_WKmdxBP4ndr9GMwA06c7MrUkgOv6FPhE5Bfy4odvBaHxXz395vingLRIPzPKr60dvXc0Ou8kiNKREEva6z2nxYRz9TC0ZBU7t9vPdSvHZ29b7ObFl42uVD6yIxEeo5CIMIVRgaZSpz-5dWnA6_kjXu8uqTzGZ3kyJ3Pfu930nQOP3KLN9p5BEqrJBUZAnvR3mp6PKvioHIztF_x0ggIdg9lKXnoXsa28wL6__LlnjC1nIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ja1BDJkwcvRELHNkbGoK4z5yMfKX0vOjQwrPJ8MyvQd87QF5CiXypqJkxAIUPkJbumOp1ZeLYhh5K0ImQdj7SOOn2L0oMmqpwCDwiyZuJInTuOKG4fbYc9pl_WjG6YbIdnOMxvvZcn6PIoPktbrxgznaJbANcxhXIdBqVm6knltHlXtTjCPqXlid0rFHoNtHlZsNhlFrD3E9U75F_ugby2-Hxgd7QO3pu2PnU0zh-Tm14Z_mt1U-pSbDmzUvlCVCNyglyNUV2nuM6DuxM8GA3fHQHMcPxCGcGAMUhT_lSwS4z5goKElQxLC0dm61IkumJzSOZIOgGDKsyqOZ_kON-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qy3eSRsLYc0nTHok3gSGAAK-N6wh3VHkjqjKon46yEPz3EoeGWx3pTAZM6eb7Cu9Asjo2EHxrCQYEIDk0SM3BpBOXkjJNnhJm4iO_3_n0j5eoa7kRz_04VOKt7Q3ku6q3h2aiBraYj2Z897N3YHeLi4eoJbES7xBj7GGuYbKYNtTrnwMVS63mJc6GcOiVheWjcFmOcjATseflpmrYIavcu0KCWWuGl25BOjPwmA0gdjIritvM_3syJ4N3B756J2LJn9jM4DmFfX940u25GuVrLm8Kh6YqL2r53_b9D-KM8Cz2zZ7yQ4c3t3h7iaTl_DyZ3P1CJDhm_dV1WnUVd6DXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJmJElSvNHI_YG5eWDZy4SqZCpST3bEga8a2DAB96NDLqaZ7Q6YWtWJhSIiLXLx2QnoCTev7DzgFbA5FanIyswCtVbgE9DvTpXcnuqcpPA6cIQr7WSeCSsXJDEINrJVUMHQNtjyuVKOw59dQpf5KJp7PLTkJzbqrZLzNJzwxCnfDjQsczjez177iYm3Z9NrjMVzFKmyno9_32hm4ipe_ZsDhZbompS8SIQvosanqOLPMScEbEO9gMGDJFDRYVhy7OWMG924f634G5QflpC2OxaLf-90Aojaon5T0WFoand-wU3zkYK5zfvQGLhW4qSK43QoRko6iprTNH4CbFefZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vbmq7OXWv60-8WLbDutJ02J7OOqmljqZQgT1qboQc3cC3EtChjHV2UuR_SLrSaZeYkqOtu35GvBHIQPwVRPXToLGDzP4FGnkyMzhN276sQOxwViRDDsACt8eFpmQP6OeqxTdc7aoYEzcHhJoD6p2EzcsDT_cGe3v7MGlsqxq8pWGa-hmwe5a7XsblD4gEoPLXnmCsheBpjmOn1g7EnZhvCpar9ed5vyrVraOTVmOXlYoKzjz5VP81ZnQ-Gj1A37KuO_YKi9PTWU58a8nIPxUwE2LMaaiWwBwPoxq-MlamhLyMfdUZIiUAx9c6qZ45mRUopPy8AG5vOsPhBzUs6BQUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jk-Isi5aRSQaGPN0UXpj7hsM5eDzI-dQJJDyzWcbM7xBwM9sMFJUnIbkgU1O_2pU1daCBoPAHidedLWHXLi5a40L7H_q8J-iDHJJn05zuPW5OkuynBhxGAK5ebS1uC-uGHr3DOJFtyInTa6ZAQsPe8R3kpps9fQRewMeHi0oura4ix50YuZvYnH6yarfkzQMGo3_evaUbn7qaQ2K7LHCB_xG6CNBOAB4sO7pVChTI8_cWvNlIH2-z5yhKN3Cj1kzdvtoLv-9zMpu-bGKO14kegd_lkGL9LCAQ9_EjWVLoQFD7RjoJLq-9DITXdMn1EvmX_6bFM-b4Wu7opck65tIhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاتای جذاب برای نیمار فنا
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/93040" target="_blank">📅 22:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93039">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArEezXPnAUO4fo6kTlr0V4cEggscbQ5JEtWqYm2gPcRhvFg4z21YIiDmAx25f1_VUVteCiw6_rukcfriTgQAhSez8Lg579rlZdeTxYv6ihLeCoW_QfsOzVBKJsXkAw93VZzK912CVOg_tI6pIjHVbmi6Gjd8HNg33LWauRYhxldkSPDNbDZH2hH9MmOXoqSK6jcAvh5EKJ7nil6wxtqRNqOAnzmpJ4FfK3JS2TqY7PBLk0ok77oMwqU3A9XEmo8UsKFkXcy8fRqhyCgwAa5ii8chpfn_IsrBkLSX8wczxpAOlGyx1IUrQxDkbY-I6nL9_1prN2rxF5j6a6i1cWAdiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان بازی | شاگردان ناگلزمن اولین گام را با تحقیر حریف شروع کردند
🇩🇪
آلمان 7 -
🇨🇼
کوراسائو 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/93039" target="_blank">📅 22:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93038">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVCU_WlA4K6iX7rnAI5w76qNdmPjCij3robI4hAqestbQXmIb4G9q1BNJs21eFhZSbfCPEAyzqdwyvJ-48KUtJP6mew3Gu8uFTUq_PsK5EY2Ifh9NBAPHGsan5mgs4Q-gTBF8bA0hN3ZBuODN_fqMkvoNIwpwIbvBOGGHwQKkyNkP5-InBCgMKCvkIcrQ3_jAMX8xNXzifKh68fk32byfz9m_h6zcZcnP51eGKiPA_4Um2NAAc2vSNKrCBN3pdK-dZW35m0vfKWhYXmEU-mlqk8Ca_26jiH7mvJQ3Tp619BDQDXJs_yvNCnDbYIQawvBE982wVlAxaYUlBwJ31oYxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🔥
🔥
تیم ملی آلمان تبدیل به تیمی با بیشترین گل زده در جام جهانی شد:
۲۳۹ گل —
🇩🇪
آلمان
۲۳۸ گل —
😀
برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93038" target="_blank">📅 22:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93037">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">هوادارای کوراسائو دعا میکنن این پنج دقیقه هم بگذره</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/93037" target="_blank">📅 22:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93036">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f0490e11b.mp4?token=Y4lRxVEOfhKCBmug7NblYaHFv_QWkwelXkPbW2jz0Dj8XcoXkWQtHATItSDRHc_-aJMSafYjHJmKoQr891fT9fj_8syGAbVsqWv4ymv0VOjTgm91t30auaB1hN40N_zX_-fx3QBi0kqTfcsJ1qwMKpOE3jDGBNuz8nFBpWWwwv6ybiMKUZJTRFXU-3CJqIRDkG14hRDO_qFIqLVGS1YDv49SmraNk1PfjxIxnIZEWUVbFs8BJRWjSEizRy6C1D7QJn6SdsJaC7YUX53es-HFgEQKELPEAk903CDWt0yseeEBUFdtkR1y5EPRwX-MG2XO3E7cOc7Z1xHdTrgrwv1fAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f0490e11b.mp4?token=Y4lRxVEOfhKCBmug7NblYaHFv_QWkwelXkPbW2jz0Dj8XcoXkWQtHATItSDRHc_-aJMSafYjHJmKoQr891fT9fj_8syGAbVsqWv4ymv0VOjTgm91t30auaB1hN40N_zX_-fx3QBi0kqTfcsJ1qwMKpOE3jDGBNuz8nFBpWWwwv6ybiMKUZJTRFXU-3CJqIRDkG14hRDO_qFIqLVGS1YDv49SmraNk1PfjxIxnIZEWUVbFs8BJRWjSEizRy6C1D7QJn6SdsJaC7YUX53es-HFgEQKELPEAk903CDWt0yseeEBUFdtkR1y5EPRwX-MG2XO3E7cOc7Z1xHdTrgrwv1fAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل هفتم آلمان توسط هاورتز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/93036" target="_blank">📅 22:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93035">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">هاورتز دبل کرد</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/93035" target="_blank">📅 22:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93034">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آلمان هفتمی هم زد</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/93034" target="_blank">📅 22:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93033">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6OTy9zDZKxodWNoxqmImZusRfvev3YlGWhxpqS9Qa7HiUTghl8gqNpP_cZPET2zwl1zJEmcI3FaH6LUwzOdTf7HrP6v2Ejc1xeoieBVKSiMZdoB5pbf0ZWDY3eG3YX716w_faItKaDpRQG-2kj-uurlObEYFRTYav-f5idJOaIyvEVHpEv91wfUuNlGgimZ3uMNtsYPelV94ug0d9Hhh-85aIbxGwlZhhbj7AeOCHW-7NGv4C_8nnWkXvlVvVTXSBht8l3KEUiLXiIrdbCa5twcKlKLvehTzyFI02FPujsFOcZ2CGWlFig9Vq_NO9sOXwyq_go6sf-la9Ga_a8BHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
ترکیب رسمی هلند مقابل ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/93033" target="_blank">📅 22:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93032">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3dc1080cfb.mp4?token=CYqJQers1cu0AOlk7FgeCnVxBcxDUBAswD9dQvWsIkk8-e4BoTbVkH1OvmVYtcCD_qmP9tJtiln8dB7lK-hnDaGrde_LAWcxrc68sNuuH59cNMYdzXbzm9DDppvfKfO5IBCUaNwI2Ftr7nZFRUy1DwcFPkFT2G34rY_G_2Qa9wJisjTh0bO4v6-grlMrY-ZDjBYyKYJDpNmkj5QBgxUV9ybnzljOgp7ulFu-L3Gt6CO9HDZrPscD8JNEAEXzGCFRgtmaZEcWLpUawWfxZYpLCmIR69fI445CSAKWIQ4nNNy78z1KPZVxouh72Rvohuwd9eSA4-NVTk25W6RwfqXt4g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3dc1080cfb.mp4?token=CYqJQers1cu0AOlk7FgeCnVxBcxDUBAswD9dQvWsIkk8-e4BoTbVkH1OvmVYtcCD_qmP9tJtiln8dB7lK-hnDaGrde_LAWcxrc68sNuuH59cNMYdzXbzm9DDppvfKfO5IBCUaNwI2Ftr7nZFRUy1DwcFPkFT2G34rY_G_2Qa9wJisjTh0bO4v6-grlMrY-ZDjBYyKYJDpNmkj5QBgxUV9ybnzljOgp7ulFu-L3Gt6CO9HDZrPscD8JNEAEXzGCFRgtmaZEcWLpUawWfxZYpLCmIR69fI445CSAKWIQ4nNNy78z1KPZVxouh72Rvohuwd9eSA4-NVTk25W6RwfqXt4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل ششم آلمان توسط اونداو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/93032" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93031">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آلمان شیشمی هم زد</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/93031" target="_blank">📅 22:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93030">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQIUYvvCSejeE7UgEE8WsyLugg-Bpbn5U5YQIL2ze_T8JcNlDWr8IAXFTtsuSJfguud_CQNpkU9FwRgw2e51GKnpStHAZ29J1dtMNwpxB6a-a5Ou5ENcyd65YywtGyaZGYHoz9LBIaJZIreC_sPNrvvaT_9wauIPcLX37s3rQTyqMgcrzI20PFetr9hSxKxy7jHLP_2n1yTERvKUMjYZq_MkJdIb89wdsjBGwa4j6xjRFn1R1IAT1So04bRep26gfbe_kcu9UEuH0Jw4SnjZyhq2szgrET7YEFKMcrpi_96QEmansxQCWbar0tiBVey6fEVjxgbEq4ZApz_QJfv6Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
ترکیب رسمی هلند مقابل ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/93030" target="_blank">📅 22:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93029">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0rZEm68Jjzm92CnKBxDwA1vPg3u5h0E6XaH2AUmCttEjAjIWtw2e1tWZPX2sxA5eiY7RM3c6kdLiCknNndb8o2XmKQawKx7DxlYr-GHdeGKwtPo8DwnoGixk0dgrBWokXSAMDT5jgcd2Oeqc9SVG4R1q2vZkQnJK0YNEIAEt88JEWYOL97HuyuaZJiwDTSF70-eit_v4lV0iIZTzMOneHSogqhxZzfeXs9KGXz3Kj_vlV8XT7YEZ3HlMXT9cpQ9-b7WNuvPFJnYGH6_XkeYd42-v-94S_GcXyXQPuNWskkKCvGIM6kfUF2a7-W62QEp23Fjyt28rrJ8l10tFTZyQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استایل عجیب هوادار کوراسائو
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/93029" target="_blank">📅 22:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93028">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5399ab6b00.mp4?token=bNGrZVxMbxe1Pkkwk75TVXLiqGn3i7EXu8ZhzICiKYVeMgdl9zJKZo4-M-o9HqLm8fO5fx_IY8gAD0BMaXToYaZjE3loURRLSbOoJQ0vAj5PkFZT_cILJnezFaaPqFXF1PacfoGz_CaQYPpkWPBelS8WWXtFcrsr5uBj75H2FTBCAmeCSD3GiWiAVlV0pv9UY7HKx-1aacKgDfmdQfclv1jtRLc_GKq2ux7nPkM19txE9ijnEKVJsVdgJ3LTMfAhZpdL80Yfn-4Na3vRefzPnK4kJmkfkcFxO9GLzBffJucICX8brVdi-r_jd4i56sNMFLidfB4UhWMifbWyjzDY4J1zWxXiuDpjGGlXIOpsKA46tFVG-brGD54ntng1z-PiFUl-AnHTfBkKOQLoPn6S1L6O6hagtRU203EtJK0tAhghDlAZxICHqjy9gOTPtNrQANYYTKqwuSnEX-MPzE3TsYHsQ0jA1dVoBHsyP7xXzFvRqnSmcjFGOr5RLXOcXQihPyYgNYJqtm10PuzXQz5_7-wI2pK2jd-cBJ6BArjJQhjkIukPE-4ZCtD7uU5PygXmQX_x4sU4466qKCLWilj4BcIeyG3JzUEjyvxCbFeHu6IxL8hqTatWEu6Hj3iDzN3uIDnlxN4Zoboa9MyZvdXXe0zV57PuvO05maGqdrIQXrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5399ab6b00.mp4?token=bNGrZVxMbxe1Pkkwk75TVXLiqGn3i7EXu8ZhzICiKYVeMgdl9zJKZo4-M-o9HqLm8fO5fx_IY8gAD0BMaXToYaZjE3loURRLSbOoJQ0vAj5PkFZT_cILJnezFaaPqFXF1PacfoGz_CaQYPpkWPBelS8WWXtFcrsr5uBj75H2FTBCAmeCSD3GiWiAVlV0pv9UY7HKx-1aacKgDfmdQfclv1jtRLc_GKq2ux7nPkM19txE9ijnEKVJsVdgJ3LTMfAhZpdL80Yfn-4Na3vRefzPnK4kJmkfkcFxO9GLzBffJucICX8brVdi-r_jd4i56sNMFLidfB4UhWMifbWyjzDY4J1zWxXiuDpjGGlXIOpsKA46tFVG-brGD54ntng1z-PiFUl-AnHTfBkKOQLoPn6S1L6O6hagtRU203EtJK0tAhghDlAZxICHqjy9gOTPtNrQANYYTKqwuSnEX-MPzE3TsYHsQ0jA1dVoBHsyP7xXzFvRqnSmcjFGOr5RLXOcXQihPyYgNYJqtm10PuzXQz5_7-wI2pK2jd-cBJ6BArjJQhjkIukPE-4ZCtD7uU5PygXmQX_x4sU4466qKCLWilj4BcIeyG3JzUEjyvxCbFeHu6IxL8hqTatWEu6Hj3iDzN3uIDnlxN4Zoboa9MyZvdXXe0zV57PuvO05maGqdrIQXrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
پشماممم از جو فنای هلند
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/93028" target="_blank">📅 22:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93026">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ae46c9a9ea.mp4?token=sH4JV5HIt2d5z4x1VbCnyi4fCFr84tJOLiT1C-QuqV-GVDk3TVl3A5JPyza3DUhGVLxX-j7V3Qj2zKQzD-zThzy58oEskoAIjRULjH28AHfoNxp7gBgOtxBAa_M6obW_LHGcFdCoj5W-M2skz11WhpoFXLpiAUCcLB-a2n95GpLqAWl-HMaeu6UG6T-UurW-MH-mEdSjR6k9aS2ElQSR_hTDn2rHw1qQDqNdfeB0td3zDe12YRty3Nbqi33kj2uSiKbL9mpZ-OuHmRhqEyYEnwKZ6FyEdVBIiBH-Hg2bWWbYKARzh1iDDvUYqSSDqXFsA1ymIgMSBu0tlX3bCZZh1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ae46c9a9ea.mp4?token=sH4JV5HIt2d5z4x1VbCnyi4fCFr84tJOLiT1C-QuqV-GVDk3TVl3A5JPyza3DUhGVLxX-j7V3Qj2zKQzD-zThzy58oEskoAIjRULjH28AHfoNxp7gBgOtxBAa_M6obW_LHGcFdCoj5W-M2skz11WhpoFXLpiAUCcLB-a2n95GpLqAWl-HMaeu6UG6T-UurW-MH-mEdSjR6k9aS2ElQSR_hTDn2rHw1qQDqNdfeB0td3zDe12YRty3Nbqi33kj2uSiKbL9mpZ-OuHmRhqEyYEnwKZ6FyEdVBIiBH-Hg2bWWbYKARzh1iDDvUYqSSDqXFsA1ymIgMSBu0tlX3bCZZh1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل پنجم آلمان توسط براون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/93026" target="_blank">📅 22:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93025">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ناتانیل براون گل پنجمو زد</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/93025" target="_blank">📅 22:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93024">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گلگلگلگلگل پنجم آلمانننن</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93024" target="_blank">📅 22:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93023">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">📊
بایرن مونیخ باشگاهی است که بازیکنانش بیشترین گل را در تاریخ جام جهانی به ثمر رسانده اند.
80 گل - بایرن مونیخ
79 گل - رئال مادرید‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/93023" target="_blank">📅 22:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93022">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کوراسائو گل زد ولی آفساید شد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93022" target="_blank">📅 22:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93021">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xg60JmXiCx6RFjTwI5nYzfRWcKXPTG02u12Vzw_OArQYP6KyGWklXBIAt5JHiNMBzELmQvO5lTzPS-2qrlSeTZd3vditTwua7xLN5P_fZakqPW0lMNq9gV8_24K-CQPEb7ENBwTFr9ovSwuxyjlBL9DuVeQX-N6XkInJZAlGrr-I3KHcO3ToY5KJoKQNWxSFfSs2Ya-ay5pLCra07_pNGfAoJMnDRGtgRfJEDprGJMvImZC7pe9-BstH6YOoHRKtdNcrWEc_zh3_P1t6tgg3pkkTnWK63LBPkYajwqNUqwxE-RenXsnvyIYRSNBuQ1woXGnEaAIKCKsBy1vPVGpIVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار کای هاورتز در جام‌جهانی:
4 بازی
4 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/93021" target="_blank">📅 22:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93020">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kujou88A9MidY0OrtF1IftEoTcOqnoI6TO0dEeld7TC-fxqHW7CMbEMlIQ_0dopDycRRPcRBYotbBiYkeow8DWK6r19F2zgbMkxGn7VyoMRK3QSlxrkrS_u-DJLT9ViNyH6ANpEER-2DVKkrWMEdZZ9XqfttHjBgzHhHSpxOdty5J3sfWLay-efL8BanH_kayDX7AkCcqXTDm-hyGmuHSQc12HhSybBmYcoi-9-FaFBhHlj-EkN5zMmV3FJvQjvAoiJOBUG4XJg9H3f85JTYNt6THnIAAGX2_PzVm5dqBwawQBr7QIq-yL1O3Uocz1bIEinrMxgYxEl64KFbKj3bEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اوه اوه
😈
🇧🇷
دیشب موقع گل وینی یکی از هواداری برزیل کنترل خودشو از دست داد و یه لحظه ...
⚠️
👀
🔖
کلیپ کاملش رو داخل ربات زیر گذاشتم
💥
🫦
🖥
🔞
https://t.me/FoootyHub_Bot?start=HyU5AoEy
💦
⚠️</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/93020" target="_blank">📅 22:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93019">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سانه چجوری این توپو از دست داد
😐</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/93019" target="_blank">📅 21:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93018">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سانه چجوری این توپو از دست داد
😐</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93018" target="_blank">📅 21:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93017">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBkCPE0n_HkkH0bGgcsjbOrCRTgeaLGHhcd4fUOpx5tBYP55CgOrfeufZ6Sx4gNnVpGI3oUDaujHmn17GaxwR_TseAm2SoUQwJrdln15PwMUvtxeE1MdEBcbICLoBczUffZ2XNyCWt1e1Kq4BMp8pAyrFnYW9y3TOmonLmOpd000sEtvbQBqkvEyT2fbdk4qlYF3BaBuYKAZhh7CPN9GD9LrCXIL7XhjgnHhIzvb-flo6yPNMzSw0ThJl9sGuPnIUA37N9h_0gt49XvRzl2vcmFXl61pN5PABIMMiz8e2wvWdcvLNXVUVPHooz8Lg21Y5d0YaIhRk2e0OtHi-RiQqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور هیتلر در ورزشگاه برای تماشای بازی آلمان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/93017" target="_blank">📅 21:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93016">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/theusWaZ_TYax9nJ5XCfYaCsnNYlVznz5UmBObslk8unS-9KINphI9ibRGeezyNo6gtAQNMAN-Bo1gBriBLd1ub7oEH2sateb_a62ze8sRfOKDknDbZrbnHnLKl7uQiME23Y0QlXEb-SKCspwWNBoetzmNCo0vuOhzB6oTzuBPaHAZMZVY5NAQztjp9SzXfP40kHiPL6-DX0b2D3ffOoo5HPnAPUkVLe300f-cN9_Jrl-2SXIuJR6QnAuDv_AoiQBjKNJXu6CFsJwqMDoNtkUYoHzTInqgsunpENjZL9FJz5Y5Lrjawr141OpmOgzYxvGLqW9tkOMXHptvQELnZc1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
🇳🇱
نمایی از ورزشگاه دالاس قبل بازی ژاپن و هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/93016" target="_blank">📅 21:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93015">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b7e8323f65.mp4?token=TFtEQ5gSQ2CssaqMsg0uEzrucd9BJ-qk1zp4bM3qv2M8SThCXFvO2k0rdcUKuYx79qLLsg2Ggg5lkfZgjtNxP5wc-Yvv3_g2ipLsKX7WifLRVhNAzhCLpO_VI4lbwevd7NX7oWh7WA87KyOsIsoYUiyP1pQFQnxyLn6TluFlVaI3xUlViKZIkO91wZBTs8BrdAjmNtHc6PLyR0TZgHO7uis_5BlE7KqEQHaIAdLBuhtzYi9Re0gj_8T2k2inm-ATVTFltyFNVuQtJWlhlR3YWdajYx4nR-ANcHdOF1Ndr3mvkhVWDuBmb_-Fjc6ZCJTd2LQUpgfbuc89ncAkwg69Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b7e8323f65.mp4?token=TFtEQ5gSQ2CssaqMsg0uEzrucd9BJ-qk1zp4bM3qv2M8SThCXFvO2k0rdcUKuYx79qLLsg2Ggg5lkfZgjtNxP5wc-Yvv3_g2ipLsKX7WifLRVhNAzhCLpO_VI4lbwevd7NX7oWh7WA87KyOsIsoYUiyP1pQFQnxyLn6TluFlVaI3xUlViKZIkO91wZBTs8BrdAjmNtHc6PLyR0TZgHO7uis_5BlE7KqEQHaIAdLBuhtzYi9Re0gj_8T2k2inm-ATVTFltyFNVuQtJWlhlR3YWdajYx4nR-ANcHdOF1Ndr3mvkhVWDuBmb_-Fjc6ZCJTd2LQUpgfbuc89ncAkwg69Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل چهارم آلمان توسط موسیالا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93015" target="_blank">📅 21:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93014">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گلللل آلمان چهارمی رو زد</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/93014" target="_blank">📅 21:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93013">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گللللل چهارم</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93013" target="_blank">📅 21:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93012">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بریم واسه شروع نیمه دوم</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/93012" target="_blank">📅 21:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93011">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENa3Wtk6jwnSJPOGmSdDDlc7wqEaANghrLwUSyEFt3Y-VRnhwULun9HR8qIeamHfDEXh6rDZwcxbKjU6AAkBAOfTB02Al_5Sx2GVeG1WDfFWotKxj0yE74Yi8R-mJQqhDleVB4uOZzDBAiB4eCpL0iEl8fvCGEtj0xTunnQHYPOsINmvLt7wIPwxnV7M1QttjkLBlg73TqgpOfeN0SthZNyNA147S6cl_6pHgb_nP-O98jhog7Hdvf8MpZTP8JPy8xAFh1If7d6g_rAHVg5le0Rl0n2PfmxoDdlhgDyxhUWjgsdRFCbubL8075zGX1wcQ-04y2M0JIMrDepdrVuC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
آلمان برای اولین بار از 1 ژوئن 2002 مقابل عربستان [4 گل] در بازی افتتاحیه جام جهانی، 3 گل در نیمه اول به ثمر رساند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/93011" target="_blank">📅 21:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93010">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfF3x6-8yYvyqbpBsSEuwT31NtBthbXDBhBd7f3oV2RQWS-JtsJVwMJgQEaYWDLJlc44KNzxdaI4CSZpxonI_Fw9_SnzD038iCgsCh5yg9VySwvFHjxezPDHB5Wh_bGcZqON2zV4yMN_YcEZ91ktkauNMlPVtSMRtD_Kwqwx4LMeAwT0l32-8LrdsymlUCcQGAhX6su2IY4pacdvWZLH7CVcYkdEMGPcor53nO9nxkf8uelvE-TmI1SI4VcCUGf4ltVjGHbyfbbxE0XxgMk4Y8q09WMeBMkoUvKvA_lh6DtPhzWcI-Nbnyd31U3uTehoc3b5A3-cU-kbns4t0VCk1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیک ادووکات سرمربی کوراسائو با 78 سال و 260 روز مسن ترین مربی در جام جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/93010" target="_blank">📅 21:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93009">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پایان نیمه اول
آلمان 3 - کوراسائو 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/93009" target="_blank">📅 21:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93008">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f6788069f0.mp4?token=NaoRSvIoxqnDpDriLInitMdv496bCmU5rd0gFaGIhohd75t8GK3lSr-zq7BLv3pkAUu4lDnWt2jfy2U0O28bLmQ92z5CNzzQdWgHlxCH1oDqkn4v1O3Rct6VX2q-foB3rh3xDXWLt92CtZ5lt66Iw5G6Fk3qdKwXlp_ocm13hsAHV4V_PdrL4cHH1btyO0dmzpMGVg7Wb5tOFpnGHlMw0S3owuqoUzEZsy9y1UCJgJKAe5qdI2v4XKxOPnumxrrNQuKgqlzYIGzPRquCuY9SXMTGH9WUxPz4c0NPDlYCwIqjD4u0HiI-2rM4T-tLqk589-Laf08Zo7sFTVVv9LavIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f6788069f0.mp4?token=NaoRSvIoxqnDpDriLInitMdv496bCmU5rd0gFaGIhohd75t8GK3lSr-zq7BLv3pkAUu4lDnWt2jfy2U0O28bLmQ92z5CNzzQdWgHlxCH1oDqkn4v1O3Rct6VX2q-foB3rh3xDXWLt92CtZ5lt66Iw5G6Fk3qdKwXlp_ocm13hsAHV4V_PdrL4cHH1btyO0dmzpMGVg7Wb5tOFpnGHlMw0S3owuqoUzEZsy9y1UCJgJKAe5qdI2v4XKxOPnumxrrNQuKgqlzYIGzPRquCuY9SXMTGH9WUxPz4c0NPDlYCwIqjD4u0HiI-2rM4T-tLqk589-Laf08Zo7sFTVVv9LavIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم آلمان توسط هاورتز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/93008" target="_blank">📅 21:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93007">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گلللل سوم برای آلمان</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/93007" target="_blank">📅 21:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93006">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پنالتی برای آلمان</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/93006" target="_blank">📅 21:19 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
