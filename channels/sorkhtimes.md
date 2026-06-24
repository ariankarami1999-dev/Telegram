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
<img src="https://cdn4.telesco.pe/file/piGl73GdhNQhrUosfF7Rqb80v5mSORjtBLIVNVD10WBKMLxVziObjNt2Q3RMgeAt7x71v_qJlX1M_mzD-VqzNZGsLfFgMOLurM5JikfnNYPdUCtzC-w_a8DBZuYlGeFqppuVb8N8S5FvxBVps707dKeGSG4UXpCFUorzBHqLT5YqjfLMz74YBjwUHBIJhIm_AG5T296Q_CcpHGw5caA2mH4RveQVSSa5R5-Rcnuei8eWgSgPyIOwvBJgf-KWe_WoI_3ocY_9uxQK_RZpdebwwxFHTXjZcrGC2zeQtkqECFnUS7WCSrJRxoTES8lkmpuvLjl7EmO6Fy_viL80YIQeKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 15:47:36</div>
<hr>

<div class="tg-post" id="msg-134206">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❗️
طی ۲۴ ساعت آینده جدایی اوسمار ویرا از پرسپولیس به صورت رسمی اعلام خواهد شد.
🔴
بدین ترتیب و در صورت برگزاری مسابقات پلی‌آف احتمالا کریم باقری به صورت موقت هدایت پرسپولیس را بر عهده خواهد داشت. البته هنوز احتمال حضور اوسمار در پرسپولیس در این تورنمنت وجود…</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/SorkhTimes/134206" target="_blank">📅 15:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134205">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
باشگاه تمایل به فسخ قرارداد و قطع همکاری با اوسمار ویرا دارد.
🔴
🔴
به گزارش خبرنگار قرمزآنلاین، قرار بود اوسمار ویرا در باشگاه حضور پیدا کند، اما هنوز این اتفاق نیفتاده است.گویا مدیران باشگاه هم تصمیم داشتند جلسه ای را برگزار کنند که این نشست به ساعات دیگری…</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/SorkhTimes/134205" target="_blank">📅 15:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134204">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❗️
اسماعیلی‌فر، ترابی و هاشم‌نژاد با تراکتور قرارداد دارن و تراکتور هم قصد فروششون رو نداره///آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SorkhTimes/134204" target="_blank">📅 14:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134203">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🤩
تتوهای خانوادگی مارکو باکیچ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SorkhTimes/134203" target="_blank">📅 14:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134202">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
پرسپولیس و مسیر جوانی در تیم
♦️
شاید بعد از چندین سال بسیار واژه مسبر جوانی برای سرخپوشان مهم و حیاتی باشد چون تیم از لحاظ میانگین سنی در وضعیت بسیار بالا قرار دارند و شرایط ایجاب میکند که در فصل جدید به جوان گرایی رو بیاوریم تا از لحاظ سبک بازی هم شاداب…</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SorkhTimes/134202" target="_blank">📅 13:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134201">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❗️
باشگاه شاید قرارداد میلاد محمدی رو تمدید نکنه.چون قیمتش بالاست ...سر همین داستان دنبال جذب ابوالفضل رزاق پوره///قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SorkhTimes/134201" target="_blank">📅 13:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134200">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
اختلال در خدمات کارت محور بانک‌ها رفع شد و خدمات کارت‌ محور هم‌اکنون در دسترس مشتریان است و روند ارائه خدمات به روال عادی بازگشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SorkhTimes/134200" target="_blank">📅 13:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134199">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
درصورت جدایی اوسمار، کریم باقری با توجه به این که اسکوچیج بارها از او تمجید کرده است، ماندنی خواهد بود.
✍️
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/134199" target="_blank">📅 11:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134198">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
فرهیختگان : اوسمار تمایلی برای ادامه کار با میلاد محمدی ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/134198" target="_blank">📅 11:49 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134197">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
ترامپ: ایران اگه توافق نکنه ظرف یک هفته تمام خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/134197" target="_blank">📅 11:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134196">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDU28daw-Z0AZopIq7AROJZJlxCILCUygb3ctpYj4G7E2EygiDrsn7VZNL4lrALqx1ot7j9ynE8K6B4tWYp8zo0lcf2BJV0P9csfUuicxK_Tqnsv0HClBlmfUwk7NfpeHDr3Qfb4JueCWJAwrCSWqZkrrQ-MRPSXcVH3ZXmbktLIsIBHAtjYhB0nCHUR8XGkI4Qa2AuIiHLu2aXj-ep_xldK94UKxhMo3OCsYL2TaR8uaFlHobVSWzAKUYJyViSUJWgrl-9GQ-uCGNrSBNZUVTvLLA2UxqDB4V3WzWNUipanzChq8bXzc4-EnH0-XX1ii3kJ2kt3iNASyS2WScfrAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رونالدو فقط انقدر تنها 25 گل با 1000 گله شدن خودش فاصله داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/134196" target="_blank">📅 10:36 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134195">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
باشگاه فرهنگی ورزشی پرسپولیس با انتشار پیامی، صعود تیم نساجی مازندران به لیگ برتر فوتبال ایران را تبریک گفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/134195" target="_blank">📅 10:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134194">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❗️
❗️
تیم چادرملو اردکان برای دیدار مقابل پرسپولیس، ۶ ستاره خارجی خود و از جمله هادی حبیبی‌نژاد را در اختیار ندارد و به نوعی یزدی‌ها هم نیز مانند پرسپولیس با ترکیب نسبتا ذخیره وارد میدان خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/134194" target="_blank">📅 10:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134193">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⭕️
برانکو پس از بازنشستگی از سرمربیگری، به عنوان مفسر و کارشناس جام جهانی با دو شبکه تلویزیونی از کشورهای کرواسی و ترکیه همکاری می‌کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/134193" target="_blank">📅 10:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134192">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
امیررضا رفیعی:
❗️
من یک فصل دیگر با پرسپولیس قرارداد دارم. پرسپولیس خانواده من است و دل کندن از این تیم برایم سخت است. دوست دارم بمانم اما به شرط اینکه فرصت بازی به من برسد. من قبلا هم خودم را نشان دادم و ثابت کردم دروازه‌بان بی‌استعدادی نیستم
🔴
شما اگر از…</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/134192" target="_blank">📅 10:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134191">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEalcGpnMoDxBprVe7mgJ78Fvux2MZf7iYl-GsIx4L8BmC4pgVylM2WM1zr0wp-VSdtNkHqnTYSfLiFy6h4vvjZSZ8asu9FEY-uc_QpAGANsSmrcMkzVfrXDUpaZkiyBTPEmaODrBljEiJRStoyv_ijBqjr2rOxus5lHAsW5b-aQuolld04EP99CpF9BDvn_s5mEGbbejh5T35q6-oADWKzn3Z0ucUnh3VSwDBk7_x3aMEclqqeQQMHReyVjBvQtPzkieutCI4TKRm3UkAAndVj2bdFbEiIx6UQeq_ewCB7DDgtbWYLHfpiACm58NyVShkfprt1qJHZlW8nfZElHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزارت امنیت داخلی آمریکا اعلام کرد که به تیم ملی ایران اجازه می‌دهد 48 ساعت قبل از بازی حساس مقابل مصر وارد سیاتل شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/134191" target="_blank">📅 10:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134190">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
شرایط جالب برای صعود :
🔴
با توجه به اینکه 8 تیم برتر سوم صعود خواهند کرد، در صورتی که شاگردان قلعه نویی در بازی آخر مقابل مصر به مساوی برسند به احتمال قوی جواز صعود به مرحله بعد را کسب خواهند کرد
🔴
اگه ببرن که مشخصه قطعی صعود حداقل به عنوان تیم دوم، اگه ببازن…</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/134190" target="_blank">📅 10:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134189">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❗️
رفع اختلال تمامی بانک‌ها تا پایان امشب
🔴
بانک مرکزی:
🔴
اختلال خدمات کارت‌محور در اکثر بانک‌ها که اقدامی پیشگیرانه برای حفظ امنیت بود، برطرف شده است؛ خدمات بانک‌های ملی، صادرات و تجارت نیز در حال بازسازی است و پیش‌بینی می‌شود تمامی خدمات بانکی تا پایان امشب…</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/134189" target="_blank">📅 09:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134188">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8G3vkK6zMv3RMjCREXP3Ps9mtjpl72v1WWsyd2nZh7kvXLYT6hiSyJxcmVreCV3v0MFond9j1JaGk8fMaKz5fFNdBy-oQHTOIrhKn34QHtGo7Srph-tXeWXy5z7Z-ZFiP-hSGtuqH0cNFeIpNWNYgQYWGbdzTaQtGv0wI4eI8UEaq7umcQWbhyIVsYsC2mH1WM5_mEH-mAE1wnw_mULvsjR_TuSZIXjKNayvsGzWTZcFGSXqbzRCw1nb4zMcHUZKuFd4h7rLtrzxbnd_7Wvr7uvnpNwI3OpxiG3xFh3VkVblurQ5RDGh-IaMKvNH57_X7SRSAmf7pKyzCzl9cIUXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بازی‌ بامداد امشب رو با ۱۰ درصد بونوس اولین واریز پیش‌بینی کنید!
🟡
Colombia -
🔵
DR Congo
⚫️
جام‌جهانی گروه K
⏰
بامداد چهارشنبه ساعت ۰۵:۳۰
🏟
استادیوم آکرون
📌
جام جهانی ۲۰۲۶ رو با وینکوبت پیش‌بینی کن و ۱۰ درصد بونوس اولین واریز بگیر.
📌
چرخش رایگان گردونه، شانس روزانه تا سقف ۱ میلیون تومان.
🔗
برای پیش‌بینی بازی‌های جام‌جهانی با بیشترین آپشن ممکن همین حالا وارد ربات مینی‌اپ وینکوبت بشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🔗
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/134188" target="_blank">📅 02:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134187">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">#بماند_به_یادگار
🔗
💯
تا روزی که اردوبادی و اینانلو داخل هئیت مدیره هستن این تیم رنگ آرامش نخواهد دید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/134187" target="_blank">📅 02:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134186">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
❗️
اسکوچیچ خواهان جذب دروژدک مهاجم اسبق خود در تراکتورسازی، برای پرسپولیس شد.
🎙
خبرگزاری تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/134186" target="_blank">📅 01:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134185">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
ترامپ: ایران اگه توافق نکنه ظرف یک هفته تمام خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/134185" target="_blank">📅 01:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134184">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔻
فوتبال 360: مذاکرات پرسپولیس با هادی حبیبی نژاد مثبت بوده و این بازیکن در آستانه همکاری دوباره با اسکوچیچ قرار دارد. هادی در فولاد نیز شاگرد اسکوچیچ بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/134184" target="_blank">📅 00:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134183">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uov6N3c3cWXd3EzZtxTur-SWMBh5tzcEh0ILhUYfwA65DWrKreF_c6gk6F2gr5aG9hmTNvKcY9kMlfKvSdiNXdHKPCRAY1OYXPa6v9zpU3PB0aQ2mJXVHOzkzVqBuRNWeaak3r9yUQjvmPZJsccCMG-jtm5BJ-Y7JrS0SrVHupd65UNIrbXF1mdG078LySwB4y0XK64hTFBA7Oqf90ltVW61j_CFY5C-7TmPPIxyyoKpULUhKlMbJyUxSW0KrLNhAZQTDNCpJFQE6p4mEVuinYX4wVNQqfJEVoO8mR24WN1LTlUGX3W0UhzgPQv54KcsIO6NaCHwpXFT_EyUwPZW0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
برانکو پس از بازنشستگی از سرمربیگری، به عنوان مفسر و کارشناس جام جهانی با دو شبکه تلویزیونی از کشورهای کرواسی و ترکیه همکاری می‌کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/134183" target="_blank">📅 00:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134182">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❗️
🚨
#شنیده‌ها
💵
پیشنهاد مالی جدید علیپور به پرسپولیس برای تمدید قرارداد: ۲۵۰ میلیارد برای ۲ فصل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/134182" target="_blank">📅 00:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134181">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
کریم باقری: دروغ می‌گویند که سبیل من را زدند
❗️
کریم باقری، مربی فوتبال:  نمی‌دانم چرا به دروغ می‌گویند سبیل من را زده‌اند در حالی که خودم اولین بار در بازی مقابل قطر سبیل‌هایم را با قیچی زدم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/134181" target="_blank">📅 00:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134180">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8081bf998b.mp4?token=bLYvHvIwXtbvRGTsJpCOACQyUfc0pMRrrKKjIZVKxpBaUp2yGg39xhxH-xRmIl4GLBhNEijxVl77RcAKT6ePNhPp8LoY7w_IG66dTI8w3pmkIH5O-Um34feCvLiAMGrTu8TcrQ05gyyX7ypDhOTtF32hBUkNhIOhMkLKExCCV33LgqbyBUZfzaeIyXzRKIIpJb3Cv1XVqwCsa5Ewhemz39Vr57Pz2YeZJH-RUloykBvqjHZSmVU5Vwzi1W5cZMwQfqjxSa6Yc5WnpR_3d3uduGw-Kk9OIEV2EnD6H7zWWgMDCrYmqxkeD1X-oqJTFUkFgECQITpuERZ-0dxPLn6ufw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8081bf998b.mp4?token=bLYvHvIwXtbvRGTsJpCOACQyUfc0pMRrrKKjIZVKxpBaUp2yGg39xhxH-xRmIl4GLBhNEijxVl77RcAKT6ePNhPp8LoY7w_IG66dTI8w3pmkIH5O-Um34feCvLiAMGrTu8TcrQ05gyyX7ypDhOTtF32hBUkNhIOhMkLKExCCV33LgqbyBUZfzaeIyXzRKIIpJb3Cv1XVqwCsa5Ewhemz39Vr57Pz2YeZJH-RUloykBvqjHZSmVU5Vwzi1W5cZMwQfqjxSa6Yc5WnpR_3d3uduGw-Kk9OIEV2EnD6H7zWWgMDCrYmqxkeD1X-oqJTFUkFgECQITpuERZ-0dxPLn6ufw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کریم باقری: دروغ می‌گویند که سبیل من را زدند
❗️
کریم باقری، مربی فوتبال:  نمی‌دانم چرا به دروغ می‌گویند سبیل من را زده‌اند در حالی که خودم اولین بار در بازی مقابل قطر سبیل‌هایم را با قیچی زدم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/134180" target="_blank">📅 00:49 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134179">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23ca2071a6.mp4?token=UqtOl3Z14ddQJFRYKqcn9tiNKGzHqR115vmljdjtn8xo841fQBi3tpdhvQoby6Iip81hlYU07Xbw5Egm07jAamgBPjf7GYLpM90VfcEvOqtxUr8L22FYY0ITZuH5Z8cXPCVI01_hkk6jwOt9uL9iRK3xZcvp8iUfnhaKGeW3h2v8uHPVWkvslRz-37tUpV1wC4h52kQle9nMPsQUhtoq1UAEjMJMZpc2RxLFBm1EixCvYPC0klSwxu8A1v-cDwW-65VlQvrEWjtK6RsGjIBIyNbQ-2otg0qI02AUn1_9WqDV2F0A7vvCkYTpQQSfvr_aJANL_U6vLzyOmVI6G0LTdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23ca2071a6.mp4?token=UqtOl3Z14ddQJFRYKqcn9tiNKGzHqR115vmljdjtn8xo841fQBi3tpdhvQoby6Iip81hlYU07Xbw5Egm07jAamgBPjf7GYLpM90VfcEvOqtxUr8L22FYY0ITZuH5Z8cXPCVI01_hkk6jwOt9uL9iRK3xZcvp8iUfnhaKGeW3h2v8uHPVWkvslRz-37tUpV1wC4h52kQle9nMPsQUhtoq1UAEjMJMZpc2RxLFBm1EixCvYPC0klSwxu8A1v-cDwW-65VlQvrEWjtK6RsGjIBIyNbQ-2otg0qI02AUn1_9WqDV2F0A7vvCkYTpQQSfvr_aJANL_U6vLzyOmVI6G0LTdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📍
چه قابی….
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/134179" target="_blank">📅 00:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134178">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2rtsmr84UAS5FKE-NCo2R3NWUHg65ZsMtB2DX18eJL3DNQSPVWhC28IeRUnHvRelPCFN1f4NFnWJweSYTk-KXQVDYFFS08gMLibFZQapGzHFqzylVazT00cIj860hLMOWmMfdN_P7wQLn35Siiwr9q3IrNe1xmjbF8weq9jLnuZmMDm8w2OtzWT2sPPYYB-80TTN5hq7BWii6anoMT57ji01vnriEAROcewyYUKcAqgBZ4_EEdiA0ErQE-5PjdqClBZW1PHGuy37SDZyaZ7_iW3165owb4NnyYv1IwX0Yc4tF4XyPiboVcvzXRNxFYeXaNftdhgQVmvbUjiX-MT4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
بیفوما برای فسخ قرارداد با باشگاه پرسپولیس خواهان600 هزار دلار است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/134178" target="_blank">📅 23:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134177">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTboBXEm71PszfsXlXRmn456sdZaNp6ctniVJz2FKDRhRLX4HTyZr9hSFhhXdmBpVW0fAUVIOU6WY-eZJySERxTYnqz5JgTYK9CXQPfDKV-C0wW8fraiqmK5TSLqRO0Npw8AsvEI9GeRmM6WveLdR5CH40nVdvFCyRdRVRpkCJXZVtvmvHNmchWZuxvNKXcKsUQpzN-bq7cTvUeAxZoHkbcWRTtDRmW7ijbEG-YXUi_cIId0c28wXHchjKQXx51pU7pA4cuIvWYK9I_1vUkXqTjHee9aMWRBhLMY8U7rkgaGbHMQxhDcRJnGcncGJfn-uDsRdbAevSMkdUPz-aQZhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
فوتبال 360: مذاکرات پرسپولیس با هادی حبیبی نژاد مثبت بوده و این بازیکن در آستانه همکاری دوباره با اسکوچیچ قرار دارد. هادی در فولاد نیز شاگرد اسکوچیچ بود
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/134177" target="_blank">📅 23:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134176">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/36a825c4c0.mp4?token=ZE8A0WPFFB3gOYGRCO9XHLquT-aecx6XCC8j0A7AQ6Ks7KgaREUi8xbNboHRlB0EdRi7afuhycKNZ_oLp2Zgqg6Y4YlZiKYKz9m40aCF1lXnJuDsdpuw_UU9FrIJz2LGpW9uPiOtlNx0Qb_cPm_AWCQ9Y-OYrjX8lQezqDfgrQElIyL-IYmJk14dJNt0R3Msy8xvYzgMRZSqoxAIzQ5vbSD-RuQXYSjGMUkfX7ljzt5uVIBobonyk7RZy4c-h_0c9HHcKb43R3sGhZ9qBQFBKOaHh92S8jUWNF-U2zRM5jKdipK6QhtZEdxFfbJF0Av6bQcIwrTZm7q59XVxD65nqIkq1Qs2pp4cHRAs8Fm3-U4rB63-_8Mwj8waqDQibjo4_O54euxie8Dw7ANbejg8DlM3MJrwF3f7T_wQEJz2YkD_FKl91se9zWMm3Rfk8UkDyFZYmKQx6hhdXP5Cs73tvbp666UvwnM2TCkKM5MF5RA2Cl1EAO33QhY4QQibibAePbaiC5fOXWznSHntJBXOlmTeLLYmj_4Jg32oHbmqhcdWb2y4HaqfJ5eOvhFXdcVtnXZPu42OxCy0VkplL1HsIafsDwsM4WLD3fdyfFtHYhQdtvOjGWgh7pC_GcOozPllpMW3oxnN5b1zHgtnuTe-5mtwvsmK74P-GXGzV0cLeO0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/36a825c4c0.mp4?token=ZE8A0WPFFB3gOYGRCO9XHLquT-aecx6XCC8j0A7AQ6Ks7KgaREUi8xbNboHRlB0EdRi7afuhycKNZ_oLp2Zgqg6Y4YlZiKYKz9m40aCF1lXnJuDsdpuw_UU9FrIJz2LGpW9uPiOtlNx0Qb_cPm_AWCQ9Y-OYrjX8lQezqDfgrQElIyL-IYmJk14dJNt0R3Msy8xvYzgMRZSqoxAIzQ5vbSD-RuQXYSjGMUkfX7ljzt5uVIBobonyk7RZy4c-h_0c9HHcKb43R3sGhZ9qBQFBKOaHh92S8jUWNF-U2zRM5jKdipK6QhtZEdxFfbJF0Av6bQcIwrTZm7q59XVxD65nqIkq1Qs2pp4cHRAs8Fm3-U4rB63-_8Mwj8waqDQibjo4_O54euxie8Dw7ANbejg8DlM3MJrwF3f7T_wQEJz2YkD_FKl91se9zWMm3Rfk8UkDyFZYmKQx6hhdXP5Cs73tvbp666UvwnM2TCkKM5MF5RA2Cl1EAO33QhY4QQibibAePbaiC5fOXWznSHntJBXOlmTeLLYmj_4Jg32oHbmqhcdWb2y4HaqfJ5eOvhFXdcVtnXZPu42OxCy0VkplL1HsIafsDwsM4WLD3fdyfFtHYhQdtvOjGWgh7pC_GcOozPllpMW3oxnN5b1zHgtnuTe-5mtwvsmK74P-GXGzV0cLeO0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حمله تند سعید اخباری، سرمربی چادرملو به پرسپولیس: سهمیه آسیایی حق تیم ما بود، باید با تیمی بازی کنیم که از ما امتیاز کمتری داشت و سه هفته است در حال تمرین است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/134176" target="_blank">📅 23:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134175">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
گفته می شود در صورت صعود تیم ملی به مرحله بعدی جام جهانی ممکن است، بازیکنان مشمول به خدمت مثل علیرضا بیرانوند و مهدی ترابی از سربازی معاف شوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/134175" target="_blank">📅 23:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134174">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTipkhPiKAwZp2_KLU02Rn50Pb_W4fZuV9qM7oteQKlmfqPSDzqRxSDoTlzRd4TSqxZbLK4e1m3vLjb6qGBQu_tWWGDFVG8pgnC1rwgYVd4nF1ft7Gy-OSe95_78_5FmVT1CPhXsfqwKTlRMlmnHTf8UB1Js4gWFhBZdIeJjbJOuIl37u1xV68v9je49lUUjXUjREu6qolDpjPowgrUoYkY3hxlE3xhh0w73Pf_j9jSABNrNlTSY8qMJTBOH6bP_GRTbTYtQF9mw2uq5ME94CZAc_JsL7u6gPihle-z7F4r_UOzl6L9MTIV4AMUECeaJWWiGJtd7dCfouRBgEqhxaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مادر دیدیه دشام سرمربی فرانسه فوت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/134174" target="_blank">📅 23:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134173">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❗️
نشست خبری پیش از بازی پرسپولیس و چادرملو برگزار نمی‌شود
🔴
به گزارش رسانه رسمی باشگاه پرسپولیس، به مناسبت فرارسیدن تاسوعا و عاشورای حسینی و به احترام ایام سوگواری اباعبدالله الحسین (ع)، نشست خبری سرمربیان پرسپولیس و چادرملو پیش از بازی برگزار نمی‌شود.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/134173" target="_blank">📅 22:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134172">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuiWSswro_wB9k4jxRLF7xPuYDOGbMsEofoFFUbfafimQRDVZaujwX6mzThjyEDWFLR_2r6FmJCOo1Egqg-utm_it0nN2oLW-By_QR_bQt5GXxmWaqVje2Mr95BhIZ9Uu_K2f7IdPeUFVXxzpBuZO6-aT-UGrAMIldxQo7uIAogZb0mJUqFZ7xpgE6nt9vcdd9w1oLMMJEDUTGWGf7wKnTuUy3pMqNbEgDfEaxwFZnsmGmd-zaj3QTv7yIYb3D84mnmBCSBFQR-sU2pjaxjF-3bq6r4luGZS72ukL9-Je_VmYY6AVngLK7ga0IO8NbVvnRy9AZSmH8_mzDFYJ69a2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
امیرحسین محمودی: اگر فوتبالیست نمی‌شدم احتمالاً کشتی‌گیر می‌شدم. اول کشتی را شروع کرده بودم و دو سال کشتی گرفتم. در کشتی هم خوب بودم و استعداد داشتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/134172" target="_blank">📅 22:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134171">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🎥
خبر میثاقی برای تصمیم درباره نماینده سوم آسیا: تورنمنت سه جانبه بین گل گهر، چادرملو و پرسپولیس برگزار می شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/134171" target="_blank">📅 22:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134170">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
ازبک دومی هم خورد ..احتمالا سرگیف و ارونوف و بیاره تو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/134170" target="_blank">📅 22:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134169">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
ازبک دومی هم خورد ..احتمالا سرگیف و ارونوف و بیاره تو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/134169" target="_blank">📅 22:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134168">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjxGb5nnhcNQARPtIXgsOoYXAoD0SLfve5QF3nKmOOBd6hGMg4xDGSxtBjZtV6Kktoi70krgIczU0rh3nJwokRlT9fhdSob-oGQfVx7I49gVe-aUdmLRxffMx3eQ2VApHDb4w05DoEtPfBD1cKBCbpsXVhnfdRmUEB_wuoFWMyi4IxLKNgz42s6QHn2f98vpcSMg3Coi1ZKd-4DCiIPyFJZq4u_q_3C1xd37NpzUocMIY3FD_0sRSfmI3JXiYEFareJJWn_yHnbVt3vXEJQ5Vuhe9ME6dC1iBuWr98JOmSRPhqVgaOVjgBBZx5BInIcOgam_by6P_QRPI_VBSXQdYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گزارش تصویری از تمرین امروز پرسپولیس
🔴
پرسپولیسی‌ها در ادامه روند آماده‌سازی، با تمرکز و انگیزه تمرینات خود را برای حضور در تورنمنت انتخابی آسیا دنبال کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/134168" target="_blank">📅 22:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134167">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⚽️
✅
رسمی؛ اسطوره کریستیانو رونالدو باز رفت تو گینس؛ بیشترین گل زده در جام جهانی توسط یک بازیکن - 6 گل توسط کریستیانو رونالدو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/134167" target="_blank">📅 22:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134166">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siJDT1Fi0CLDcptmclyDtfnedzRTopwM-uzZaoI-slW23lri0YAY2pbbOywF-ri0SY9_oT2EKEQ_MXA-RQl7ino90gU5lUXfbcorf8Wbdhz2gldy1OcpRbBg6r99HRKJo6tN43sjaS_8mQsB0vQ7YlEPURvMMtpQp6skTFS-iovMdV1MxFLCPCiOlgsVuoNvcK67i40NHuyAn0n3Iks0QoTdtlILU1Aa8DniLsU3HJ9banaHP-ynZpm9OYtpv5SU3rnko6J09blFUmtkWfZvR-raKFvZNNgFJThGHuubxmXeX4iIWVlbjhhoB8VL1TAB2OClQs65wEwRMa3oaP0nyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بازی‌های امشب جام‌جهانی رو با ۱۰ درصد بونوس اولین واریز پیش‌بینی کنید!
⚪️
England -
⚪️
Ghana
⚫️
جام‌جهانی گروه L
⏰
سه‌شنبه ساعت ۲۳:۳۰
🏟
استادیوم ژیلت
📌
جام جهانی ۲۰۲۶ رو با وینکوبت پیش‌بینی کن و ۱۰ درصد بونوس اولین واریز بگیر.
📌
چرخش رایگان گردونه، شانس روزانه تا سقف ۱ میلیون تومان.
🔗
برای پیش‌بینی بازی‌های جام‌جهانی با بیشترین آپشن ممکن همین حالا وارد ربات مینی‌اپ وینکوبت بشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🔗
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/134166" target="_blank">📅 21:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134165">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfdyRlfJe3xkEIGKqTKXxg3kOUo_nGAFE56fGmv_LoVQm4igzFVQ6AcXidQTxu_21-7gmws6f2ZSx33Yenn7dcndZMSQL3e1LuVe8tjmyFNlqkvbZNUCgnHsSgu1_VcCLX67XY0SRp2Wu4rgXZ08CffeaOa8yp9h7R52dhe22JyoW4c4-7mobbv9B5fvbBwcbREuhwQNynN-dgSi4mvSyjT4Xk5LDisvNl4emXDCi6dIBxfAY3fwBdqQqx-0Hq6TNH3vgsL4rqIrUAL4jCgnytiSHCtr8ZO0ZvgOuk81JgXe0MZODbXl033b46pWc6Hx0c3zn8wh36bnpKSPrf3aaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
✅
رسمی؛ اسطوره کریستیانو رونالدو باز رفت تو گینس؛ بیشترین گل زده در جام جهانی توسط یک بازیکن - 6 گل توسط کریستیانو رونالدو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/134165" target="_blank">📅 21:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134164">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
فووووری: سعید اخباری سرمربی چادرملو در مقابل پرسپولیس حاضر خواهیم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/134164" target="_blank">📅 21:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134163">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
داور فینال جام جهانی قطر
❗️
سیمون مارسینیاک از لهستان داور دیدار ایران و مصر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/134163" target="_blank">📅 21:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134162">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
✅
رونالدو گل اول و خیلی زود زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/134162" target="_blank">📅 20:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134161">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
✅
رونالدو گل اول و خیلی زود زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/134161" target="_blank">📅 20:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134160">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
ساعت 20/30 عجب بازی بین پرتغال و ازبکستان انجام میشه ..هر کدوم ببازن حذف میشن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/134160" target="_blank">📅 20:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134159">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
فووووری: سعید اخباری سرمربی چادرملو در مقابل پرسپولیس حاضر خواهیم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/134159" target="_blank">📅 20:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134158">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❗️
❗️
تیم چادرملو اردکان برای دیدار مقابل پرسپولیس، ۶ ستاره خارجی خود و از جمله هادی حبیبی‌نژاد را در اختیار ندارد و به نوعی یزدی‌ها هم نیز مانند پرسپولیس با ترکیب نسبتا ذخیره وارد میدان خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/134158" target="_blank">📅 20:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134157">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
تسنیم : مخالفت سازمان لیگ با حضور تیم امید چادرملو مقابل پرسپولیس
🔴
با توجه به اینکه بازیکنان چادرملو هنوز در تمرینات حاضر نشده‌اند، مدیران این باشگاه از سازمان لیگ خواستند با تیم امید خود در تورنمنت فوق حاضر شوند. این درخواست با مخالفت سازمان لیگ همراه…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/134157" target="_blank">📅 20:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134156">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❗️
عجب جام جهانی شده ..اون از اسپانیا اینم از پرتغال
🔴
پایان بازی رونالدو و یارانش در بازی اول غافلگیر شدند.
🇵🇹
پرتغال 1-1 کنگو
🇨🇩
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/134156" target="_blank">📅 20:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134155">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
فوری: حملات سایبری شدیدی به بانک‌های کشور انجام شده و اکثرا از دسترس خارج شدن.
🔴
یه سریام میگن بعد از محاصره دریایی آمریکا، دولت خیلی ضربه دیده و در آستانه ورشکستگی قرار داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/134155" target="_blank">📅 19:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134154">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
🔴
مدیران باشگاه پرسپولیس در آستانه نهایی کردن قرارداد هادی حبیبی نژاد ستاره 30 ساله ملی پوش چادرملو اردکان به عنوان خرید سوم هستند. مدیران باشگاه پرسپولیس گوی رقابت برای جذب این بازیکن از استقلال و سپاهان ربوده اند و اگر اتفاق خاصی ندهد حبیبی نژاد فصل آینده…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/134154" target="_blank">📅 19:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134153">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
داور فینال جام جهانی قطر
❗️
سیمون مارسینیاک از لهستان داور دیدار ایران و مصر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/134153" target="_blank">📅 17:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134152">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❗️
باشگاه شاید قرارداد میلاد محمدی رو تمدید نکنه.چون قیمتش بالاست ...سر همین داستان دنبال جذب ابوالفضل رزاق پوره///قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/134152" target="_blank">📅 16:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134151">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
باشگاه تمایل به فسخ قرارداد و قطع همکاری با اوسمار ویرا دارد.
🔴
🔴
به گزارش خبرنگار قرمزآنلاین، قرار بود اوسمار ویرا در باشگاه حضور پیدا کند، اما هنوز این اتفاق نیفتاده است.گویا مدیران باشگاه هم تصمیم داشتند جلسه ای را برگزار کنند که این نشست به ساعات دیگری…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/134151" target="_blank">📅 16:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134150">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
ورزش‌سه:
🔴
اوسمار ویرا از پرسپولیس جدا شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/134150" target="_blank">📅 16:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134149">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhOGzOvS4cQV7WCi4kRLkV4K8S_8_8IJV64p7EhUdVzCkvMwJ8c5vtVasPdMQZxcEOWQropEGn7oLe6prGb410kPxvZVaMa6SBthvBSmRVv30M97vSj8rPSKjNKs00aUPK86O1Sl8hSYKqET9-fyeNO7Obya2njzlRXtTzZzJ_h0jGYV4WJvujDHMHemSwVVbUvnC_AshBabOEfw9v9vTP6Pl6W8pq9XZ0VdqZ5nVhc9a_uKcI7Q4sxW4U-Oyn3NhGnmn7EOOrIpNneWdSkKuSFzF3okgKNrzzsKhyhXpqk3swtJKWrOGI8diqKLVsp5kd7FjktpdUPYzId5pMdMTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
داور فینال جام جهانی قطر
❗️
سیمون مارسینیاک از لهستان داور دیدار ایران و مصر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/134149" target="_blank">📅 16:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134148">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2dW-s3O6ZfxVIA2Y9BNxdXUAQOGeNEQe3GNxoraWdMnJ8LV8_ImFmWlFK5gV4Dj4yf2oJyLnD8xP-44lad2FVFhnCX0J-GowV7YDmzuOGg8pff_e6P7WU4Vvubp1Q-kMApJLOeanOhbM3o2cwTEeCSkfx2hjW1UARsETZLD3Mww8DnTDz9LxkcWM_538YxbXXipfkZUfF5PwKFIL4UottI6333ZTeadvd_TQbsC8ApELb_HiinG2zq-O1dHK3tCaO7ORWrIadbyzz0acu8PMg2iAUrg8yvAV0IGFw0SItOVKcTXB72cud_SFR1EhQt02FUX4dyX-U5dt276_wdbPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
رده‌بندی تیم‌های لیگ ملت‌های والیبال 2026 در پایان هفته نخست
🔴
ایران در رتبه پانزدهم جدول
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/134148" target="_blank">📅 16:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134147">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRNiQB5bad-Jl7XN1f1PZCiuG6YBDk0Fklk2MMr3pz7QyTonbM3gr4m1HCtmv5kWZZ_52voC_vlPhwB4nfi0pBS2DScfSxV3dPgzdLUg0ZIkfajWlj42rEIsdBKXuQw_BnNIYEPiZsjoOp55z_NVZJ4Agpe_3pxrPDkspJId9WU107gzeT9F6KXuJfMHjbH7zgwoCpZS9qvDN6eRTeATD26DQFDJ00HMF-nWg_gFzu3P4BN3kuG7StL0Mls3pH7fhJM1Ms2L8sbpIYNRhgGabPyBWqBqlBrJ-IBJ38zSy0dhgnjvatJMn-MxSCAzPPk2SBynk9u2sx4ZM_mpLNg-JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
درصورت جدایی اوسمار، کریم باقری با توجه به این که اسکوچیج بارها از او تمجید کرده است، ماندنی خواهد بود.
✍️
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/134147" target="_blank">📅 16:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134146">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d841d0291.mp4?token=VQ5tjXT-lPKYMk2B4DAmAsvDTzt2MxxrXff4efAzBM4akOxDfmjHNQtD3jDaTW5-kj8NAyQ25HpGolX9kmuZvv8wUPS6DY-XcR29Ce7AqbgcggnletdrcTOfUp3DOyaoGFFmDfBBTU0TTbV8bZE_lXCqdADtEExAvDwnL9C-tlENBe7Fa4p1EYnIrehWv0hSRrQ27fGMoicnp01aKK6vpUjZTr14TpEqf8aEAK6FDTVQHBntF4mnXBZk9RrBIJgbpB6N7uGAhO12O6XFKVRyGsYwFVOMi6PlyuZDM-D9fPAe08xkf3zh1FmBC_ApT5AJEQqA87WAzaL0lmG2ngX8jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d841d0291.mp4?token=VQ5tjXT-lPKYMk2B4DAmAsvDTzt2MxxrXff4efAzBM4akOxDfmjHNQtD3jDaTW5-kj8NAyQ25HpGolX9kmuZvv8wUPS6DY-XcR29Ce7AqbgcggnletdrcTOfUp3DOyaoGFFmDfBBTU0TTbV8bZE_lXCqdADtEExAvDwnL9C-tlENBe7Fa4p1EYnIrehWv0hSRrQ27fGMoicnp01aKK6vpUjZTr14TpEqf8aEAK6FDTVQHBntF4mnXBZk9RrBIJgbpB6N7uGAhO12O6XFKVRyGsYwFVOMi6PlyuZDM-D9fPAe08xkf3zh1FmBC_ApT5AJEQqA87WAzaL0lmG2ngX8jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
محمدرضا اخباری
: کارهای انتقالم به پرسپولیس تمام شده بود اما در نهایت آقای تارتار با جدایی‌ام مخالفت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/134146" target="_blank">📅 16:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134145">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
#فوووووووووووووری
🔴
با اعلام رسمی پایان فصل؛ قرارداد امید عالیشاه با پرسپولیس یک فصل دیگر به طور خودکار تمدید شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/134145" target="_blank">📅 16:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134144">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗️
مسن ترین بازیکنان حال حاضر پرسپولیس:
🔴
عالیشاه(34)
🔴
پورعلی گنجی(34)
🔴
بیفوما(34)
🔴
سرگیف(33)
🔴
کنعانی(32)
🔴
محمدی(32)
🔴
باکیچ(32)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/134144" target="_blank">📅 16:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134143">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
مذاکرات پرسپولیس با اسکوچیچ مثبت شد
🔴
مذاکرات پرسپولیس با اسکوچیچ داره بهتر می‌شه. اسکوچیچ که سر بند فورس ماژور جنگ و مدت قرارداد بحث داشت، ظاهراً با باشگاه به تفاهم رسیده و فرداست که همه چیز نهایی بشه.
🔴
اوسمار هم که قبلاً می‌گفت می‌تونه برای بند تمدید…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/134143" target="_blank">📅 15:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134142">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
❗️
#منهای_ورزش
✅
اختلال گسترده در خدمات بانکی؛ بانک صادرات، ملی، ملت، تجارت و کشاورزی باز هم قطع شدند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/134142" target="_blank">📅 15:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134141">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❗️
خبرنگار الجزیره: ظهر امروز به وقت محلی قرار است مراسم نمادین امضا و مبادله متن توافق مرحله اول میان دو هیات ایران و آمریکا برگزار شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/134141" target="_blank">📅 15:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134140">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
واکنش باشگاه چادرملو به برگزاری پلی‌آف آسیایی؛ بازی را عقب بیاندازید.
✅
ما هفته گذشته فراخوان دادیم، اما بازیکنان مطمئن نبودند که این بازی واقعاً برگزار می‌شود یا نه و اصلاً فرصتی برای آماده‌سازی وجود نداشت. قرار بود بازیکنان پس از مراسم عزاداری امام حسین…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/134140" target="_blank">📅 15:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134139">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otML8a0oh-ItxKmkff4V7RbR_EmIQcXIsN6qJhZKAYJ2OdMGHfdIJrM3xjZ9gEbBwHXrCyk_Tzn9UFWH6Kc-St4q9aGpjLGGFhWTDJvb8ZSI81iOhXp28xPBRmsBSEIgf9SosudYNWoKXoDgVMEmj46bLmg8RORK0G6cxRLgkzIvUk2Fwmqwa_xIrRvVKQKBl8MpHf8F-DWi-sg3hxQQ8JPr56xni3nWoV7Wash0cHqr2d25ZwuTh-BjQ7Gw1X1ST4pnrxT-8-IG6JFYbvXKh5ujzlH79ir2lp8-ypKMy1L7eJCGYjYzGITYSdl4esB73oRyNBrEhVs_M5z8DmtO4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
توئیت کاربر بلژیکی با نزدیک دو میلیون بازدید:
🔴
ما نتونستیم ایرانو شکست بدیم اما حداقل (مثل دولت آمریکا) ۳۰۰ میلیارد دلار هزینه نکردیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/134139" target="_blank">📅 15:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134138">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⚠️
پوفیوزا
بزارید طرف بیاد بعد بگید لیست داده
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/134138" target="_blank">📅 14:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134137">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_sdw7Ypt7mC9Wujka-9lq9HAwzkoS88uCwlDioSATvMVVofFSf_0Ovln6boleNncs0xktZGiovwILAdcO6R03AQ1SSRzMAt0VKwiVMWwDZGaG5OoaTl2IobYt6TCnMyBQHLVmoit5dG-WcQxpJpQP33KsKgOol_HXPcF5sVNfFYOvPcy284Od32SFYnOQRLyFli7bDjLniIF5ruLgqAMxrPKbmQq446B9wxGZc4zjCbL7njdjKCCVW6pvu_pBM1FDl8Bsv-39wDn6Ndpcz1Gfo11_X9dnomflijE_F-EcLMdSc2O6ZKx1gnrTU4oTBmrZEoXpvUP1lXPWN6t0bW3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه K جام‌جهانی ۲۰۲۶
[
پرتغال
🇵🇹
🆚
🇺🇿
ازبکستان
]
⏰
سه‌شنبه ساعت ۲۰:۳۰
🏟
استادیوم
ان‌آرجی
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/134137" target="_blank">📅 14:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134136">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
اختلال هر ۴ بانک که مورد حمله سایبری قرار گرفته بودند، رفع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/134136" target="_blank">📅 14:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134135">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
علیرضا بابایی مدیرعامل چادرملو اردکان:
🔴
با وجود مخالفت سعید اخباری سرمربی تیم و اعضای کادرفنی به خاطر آنکه احتمال مصدومیت بازیکنان ما وجود دارد، در احترام به تصمیم هیات رئیسه فدراسیون فوتبال، کادرفنی درخواست مدیریت باشگاه را تمکین کرد و برابر پرسپولیس بازی…</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/134135" target="_blank">📅 14:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134134">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
چادرملو هنوز تمرینات خود را شروع نکرده و تمایلی به حضور در مسابقه مقابل پرسپولیس ندارد.   احتمال انصراف این تیم از بازی مقابل پرسپولیس دور از ذهن نیست. / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/134134" target="_blank">📅 13:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134133">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ir0ZJTuL0Crg6srXcVCcsxVQYZm9qmmmgytbyh5Ek2nXKgpfQO_D38fhFURgwA68kNEIcGdamQF2eNLer9vVSbevAgCyOsKVjnPExJ5pZteIV0u0i0rx4ZVzUeBcusBOxnxzYzf_2-SbAg0UpWd18akBhGVsvOBmA-vsUlqR2EnyqYOShNz3m1WGKGxbSDhBMtFJesaDkPd1xocLD0S2IKV2cNQqBnxgpMZDMQg3OSdsTIYzhpGckTbsLC9hGwrpcWPOr1VAzqyEBk4iJAdPAFBEdX76mbdnLAlu9v0dRi_UCZwUYfZP7R3ebCncMG-2zo2J_gnDkIbOzoZf-3GLFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ورزش‌سه:
🔴
اوسمار ویرا از پرسپولیس جدا شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/134133" target="_blank">📅 13:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134132">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
🚨
اوسمار گفته اگه قراره فصل آینده سرمربی نباشم تورنمنت سه جانبه رو هم نیستم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/134132" target="_blank">📅 11:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134131">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❗️
طی ۲۴ ساعت آینده جدایی اوسمار ویرا از پرسپولیس به صورت رسمی اعلام خواهد شد.
🔴
بدین ترتیب و در صورت برگزاری مسابقات پلی‌آف احتمالا کریم باقری به صورت موقت هدایت پرسپولیس را بر عهده خواهد داشت. البته هنوز احتمال حضور اوسمار در پرسپولیس در این تورنمنت وجود…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/134131" target="_blank">📅 11:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134130">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
سازمان لیگ : بازی پرسپولیس و چادرملو ۵ تیر ماه در ورزشگاه پاس قوامین یا شهر قدس برگزار خواهد شد
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/134130" target="_blank">📅 11:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134129">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
انتظار می‌رود تا ساعاتی دیگر، خبر رسمی جدایی اوسمار ویرا از پرسپولیس و انتخاب دراگان اسکوچیچ به عنوان جانشین او منتشر شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/134129" target="_blank">📅 11:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134128">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
انتظار می‌رود تا ساعاتی دیگر، خبر رسمی جدایی اوسمار ویرا از پرسپولیس و انتخاب دراگان اسکوچیچ به عنوان جانشین او منتشر شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/134128" target="_blank">📅 11:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134127">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
یه مشکل از دو تا اختلاف پرسپولیس با اسکوچیچ حل شد
🔴
مدت قرارداد که اسکوچیچ می‌خواست دوساله باشه ولی پرسپولیس می‌گفت یه ساله، حل شد و رسیدن به یه توافق وسط: یک+یک ساله
🔴
اما هنوز یه گره باز مونده: بند فورس ماژور. اسکوچیچ می‌گه اگه این بند فعال بشه، باید کل…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/134127" target="_blank">📅 11:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134126">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✅
فارس: چادرملو در بازی پلی آف شرکت نمیکنه و پرسپولیس مستقیم راهی فینال میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/134126" target="_blank">📅 11:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134125">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❗️
اعلام زمان و محل برگزاری دیدار چادرملو و پرسپولیس
✅
طبق مصوبه هیات رئیسه فدراسیون فوتبال مقرر شد برای تعیین نماینده سوم کشورمان در لیگ قهرمانان سطح دو آسیا دو مسابقه پلی آف برگزار شود.
❌
بر این اساس در دیدار اول روز جمعه ۵ تیر ۱۴۰۵ ساعت ۱۸:۴۵ در ورزشگاه…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/134125" target="_blank">📅 11:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134124">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
✅
تایید شد
🚨
میثاقی: پرسپولیس 5 تیر به مصاف چادرملو خواهد رفت و برنده این بازی 9 تیر با گل گهر مسابقه خواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/134124" target="_blank">📅 11:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134123">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
مذاکرات پرسپولیس با اسکوچیچ مثبت شد
🔴
مذاکرات پرسپولیس با اسکوچیچ داره بهتر می‌شه. اسکوچیچ که سر بند فورس ماژور جنگ و مدت قرارداد بحث داشت، ظاهراً با باشگاه به تفاهم رسیده و فرداست که همه چیز نهایی بشه.
🔴
اوسمار هم که قبلاً می‌گفت می‌تونه برای بند تمدید…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/134123" target="_blank">📅 09:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134122">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">#تکمیلی
🚨
🇮🇷
صبح روز دوشنبه اسکوچیچ به باشگاه از طریق ایجنتش پیغام داده که روی پیشنهاد آخر باشگاه فکر میکنه و ظرف ۲۴ الی ۴۸ ساعت آینده خبر میده!
🔴
مدیران باشگاه و بانک شهر درخصوص خاسته اسکوچیچ درباره نقل و انتقالات موافقت کردن و همچنین درباره مدت قرارداد امروز…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/134122" target="_blank">📅 09:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134121">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✅
استوری معنی‌دار اوسمار: خدا همیشه خوب است. متعهد بودن، حرفه‌ای بودن، با دیگران مهربان بودن و قابل اعتماد بودن یک انتخاب نیست، اصول شخصیت انسان است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/134121" target="_blank">📅 09:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134120">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzm4SPVC8uMN_gA8scCtzFGxWOrCAzXVUnv-sJGeSUqpq8dUQC8KNc_bibmde6EntduNkb5g301In4kG70E4sNZzrxURn2cCFEgCCGYP8sH9R3gfML9MHWbDf3P6sKOW85FFKkYq0mUgeUsDYodjbTLxZnAlO0MV54TGfYLlR9F5lAE6127KT_4HUHAtcodmI0mpO_pw8wyR0OBT2FLqJEZmxgpPPYnoYLOyXRoQuVGOotgiwPMgHwHtvV_2PC9r4LWHJr1Go6fGScc7FsCCPHL-KrmNY4Gv3PxW792jbTYY6fvx1WthaAbrZWwDHnUbwyypQVzXc1v6MaY6Gi9-aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه I جام‌جهانی ۲۰۲۶
[
سنگال
🇸🇳
🆚
🇳🇴
نروژ
]
⏰
بامداد سه‌شنبه ساعت ۰۳:۳۰
🏟
استادیوم
مت‌لایف
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/SorkhTimes/134120" target="_blank">📅 05:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134119">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #تکمیلی
🤫
🏅
حدادی و اسکوچیچ سر عدد ۱.۳ میلیون دلار برای ۱ فصل به توافق رسیده بودند؛اما اسکوچیچ خواهان قراردادی دو ساله بود و میخاست بندی داخل قراردادش قرار بگیره که در صورت جنگ کل مبلغ دو فصلش رو دریافت بکنه،از اون طرف مدیران باشگاه میگفتن…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/134119" target="_blank">📅 02:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134116">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
منزل بیفوما و دنیل گرا پس گرفته شد  مذاکره برای فسخ دو خارجی پرسپولیس
🔴
فرهیختگان: باشگاه پرسپولیس به دو بازیکن خارجی تیمش اعلام کرده که اجازه ورود به آپارتمان خود را ندارند چرا که دوران حضورشان در این تیم به پایان رسیده است.
🔴
تیوی بیفوما و دنیل گرا هر…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/134116" target="_blank">📅 02:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134115">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HX0IQ319lBmjh6WO4R4N1o2QtcUMMsgmbQQ6LX7lYPXQ3OYY-zifL35FnhQScoWcyXlhpDTkp72VHLIuNhs1pDHpCCQFu8VbB068x4KLpz2lxEG1SgKGALmE8nAE1GFmWXYHNq8NaweHkmzeSUXYU_k016pm-8EcDN3a57f7-k6b3efpn1eHkzToWrJtQuQRR5kN2lNdnuE7xXEoLy3_6F_BfOo_217fPcgjRs3zAsM404ipjCs57ARbVWRLPK1DidLavhBFTLvsgzs-gdQGKKNnm2KriPtLwGaOZ66QJdpvSeylCxWgOC2TUhrm2u544C3732neEt7AhWbWZEgWQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه I جام‌جهانی ۲۰۲۶
[
سنگال
🇸🇳
🆚
🇳🇴
نروژ
]
⏰
بامداد سه‌شنبه ساعت ۰۳:۳۰
🏟
استادیوم
مت‌لایف
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/134115" target="_blank">📅 01:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134114">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/SorkhTimes/134114" target="_blank">📅 00:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134113">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dee5f09984.mp4?token=hH8QjVkwyIDa6dVxY4gQt_ESXDmg924PBTCQQzoF1vCmFLpFQO2IVSYaBtVaWU1UJYmXJyxEcPhNtybbf1KI-a5YCANzg-LM77x-dmHucT_ci1J56yLBZ_JmGNvS4QG0bA6UuSPKu0yf_XlHw4MfNHboZ03dBTVnHVFXLrnVnExBT6Aho8OFU_NaKjLCA9udL5_Jnqc7BVMtvNZicI022GBsbu5NWHfqnvLxDHzIe6U6pOqQhSo_ABIM6xGK9BNBp43jwjwaqWd_S7iQDZ2yG2qcy4tfAuZy_AQ9eppEiH2G71hbK-FVrajgRmJKSgfY3GNrXkinTYRNKYlzBl9-9DMj60Bir_RoXYqxjUT9ExwTBto79PWKh9unXwpicPzpK6-w-8GjR32TiTkka_LF9q5u3J7ufbyBgAHjNNKZAlY3S5Ym3NI6tbhIauPkz6fCAKoUAxUV8Kel5FSOT3EHbIRKe1qnNa3W_JiHbsalEWXHToHxqLEOYVLtGuCcBtK2VYOY8VpHPh3izhFBbhQHIZ5nV-9Lc7KSGwsKqU2CMYXt3yEWxIIUiMBd-ERwxV3BEerx_3nVbJyS-79A62H5w1-YylHxrlKx5X0ZOorXMaRSaWPG_-TiPuIPqr6risN2stTCWj7OO55vTAvevsDs4oUy3dAKjkAuTB-hPsN_oDU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dee5f09984.mp4?token=hH8QjVkwyIDa6dVxY4gQt_ESXDmg924PBTCQQzoF1vCmFLpFQO2IVSYaBtVaWU1UJYmXJyxEcPhNtybbf1KI-a5YCANzg-LM77x-dmHucT_ci1J56yLBZ_JmGNvS4QG0bA6UuSPKu0yf_XlHw4MfNHboZ03dBTVnHVFXLrnVnExBT6Aho8OFU_NaKjLCA9udL5_Jnqc7BVMtvNZicI022GBsbu5NWHfqnvLxDHzIe6U6pOqQhSo_ABIM6xGK9BNBp43jwjwaqWd_S7iQDZ2yG2qcy4tfAuZy_AQ9eppEiH2G71hbK-FVrajgRmJKSgfY3GNrXkinTYRNKYlzBl9-9DMj60Bir_RoXYqxjUT9ExwTBto79PWKh9unXwpicPzpK6-w-8GjR32TiTkka_LF9q5u3J7ufbyBgAHjNNKZAlY3S5Ym3NI6tbhIauPkz6fCAKoUAxUV8Kel5FSOT3EHbIRKe1qnNa3W_JiHbsalEWXHToHxqLEOYVLtGuCcBtK2VYOY8VpHPh3izhFBbhQHIZ5nV-9Lc7KSGwsKqU2CMYXt3yEWxIIUiMBd-ERwxV3BEerx_3nVbJyS-79A62H5w1-YylHxrlKx5X0ZOorXMaRSaWPG_-TiPuIPqr6risN2stTCWj7OO55vTAvevsDs4oUy3dAKjkAuTB-hPsN_oDU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بیرانوند: مهدی طارمی قبل از بازی یک سخنرانی حماسی کرد و به بازیکنان گفت اگر سر خود را در مقابل بازیکنان بلژیک پایین بندازید، بلژیکی‌ها ما را له می‌کنند و آبروی ما را می‌برند و باید در تمام لحظات سر خود را بالا بگیرید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/134113" target="_blank">📅 00:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134112">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d02fae5a3c.mp4?token=J3qgqYCclrj_AE-4IvpfYp-6xaTKH6qnhpxNfZhtnGyyKMI6wGqHXg3dJgZc_Zv_9UeHSVQpAp7kTMBvA3X4MPLf3-aRvVLcjzEjnSsR-7djcF7se6k4kM0C8ret3DsDOhMOv-Yh9-eV9QSxvu5vRmVjnCseqa99fYme4QAfSy8uw9WRkeZjLdce6XzV6HZzt18pNzNlS3uovmO3iBzAt7T5-u5Z719pDSVGSY2cLYElj3f5AZ90k2rNQKkrO2cLCfbWgqVlVzQ8JtpjMup2PAYhrOCjRhCPBDsoavIw3h7NovIWAHVZwcDXaWe6rXtzsp6tSCQbbpH-ikDTIhPIAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d02fae5a3c.mp4?token=J3qgqYCclrj_AE-4IvpfYp-6xaTKH6qnhpxNfZhtnGyyKMI6wGqHXg3dJgZc_Zv_9UeHSVQpAp7kTMBvA3X4MPLf3-aRvVLcjzEjnSsR-7djcF7se6k4kM0C8ret3DsDOhMOv-Yh9-eV9QSxvu5vRmVjnCseqa99fYme4QAfSy8uw9WRkeZjLdce6XzV6HZzt18pNzNlS3uovmO3iBzAt7T5-u5Z719pDSVGSY2cLYElj3f5AZ90k2rNQKkrO2cLCfbWgqVlVzQ8JtpjMup2PAYhrOCjRhCPBDsoavIw3h7NovIWAHVZwcDXaWe6rXtzsp6tSCQbbpH-ikDTIhPIAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
علیرضا بیرانوند: مردم ما ۴ ماه سخت را سپری کردند و همه تلاش خود را کردیم تا دل آن‌ها را شاد کنیم و شرمنده آن‌ها نشویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/134112" target="_blank">📅 00:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134111">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
باشگاه گل گهر سیرجان به صورت رسمی از شرکت در تورنمنت آسیایی انصراف داد
❗️
بیانیه جدید باشگاه گل گهر سیرجان: ما در هیچ تورنمنتی که خارج از چارچوب مصوبات رسمی فوتبال کشور تعریف شده باشد شرکت نمی‌کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/134111" target="_blank">📅 00:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134110">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W02jom2R0cRAWAucnm6se7PSUmtBnmU3YhgLMLyTuVp6yT8qSTkQZME5PxVLpVL2cIGr85u6OLUP2-dS7Nb9vwT8Y3_KBrBwFypBg3qjdLmePkUimuva-TRXPPI7yieKJiEMwxAgWNcZ1PniEUPlOjci9XfBCAkcYqBEn2NUZjGoTZm76NphlzpNY0DGGzwlfvGvuVs6DbPDZ1Vuqe0xSsSN6r-EMkCtagxZRT51Zz5nWZNyuJOuR4sOlsemvmoBcXO1YFT9R7ibFk6LKAd_Sa1ci6XDbgKhbFx2Bubl19ovZwPK1szicuuRHM2XiZh8vpARla_Y3QADsEOXcRM9HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تیمهای صعود کننده به دور حذفی جام‌جهانی تا این لحظه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/134110" target="_blank">📅 22:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134109">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✅
امین حزباوی، مهدی تیکدری، آریا یوسفی، کسری طاهری و مهدی لیموچی بازیکنانی هستند که پرسولیس با چراغ سبز اسکوچیچ به سراغشون رفته////فوتبال 360
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/134109" target="_blank">📅 22:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134108">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPaGxAmcHKqYzKRgoIXVqg6PzKe6EpqJm27HcpaeLMrE7HpBrgfbOIfBqPSwyVaKMycybwnbZMrScHurigGHtm_Ca90kN4Jvhxrbr0nxjKzGJDxr1BBup3Zkh3TvU3QHPy-rx9zqjJqgaWFHS6SwsIuc6ULs1cBhZtWQx4RRF7IvzE6CoWEM2RaGHiCg7kU1CJJd5fwTN5KspaoiQocojV5eIRQb1-SHKfuC5pKps6BaevSR5_DQdivfZUy59P-878IcYKHCR1815kOeqaMAUuwKwAJCfiP2FFRkKfME6GX39uRrfzyh5dvLsDTliE0uXDb-1dEdNqhzg0Eoff7oVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مثل اینکه یکی از بندای توافق ایران و آمریکا نشون دادن لب گرفتن تماشاگرا وسط بازی بوده،
🔴
امشب برای دومین بار شبکه سه لب گرفتن تماشاچیارو نشون داد:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/134108" target="_blank">📅 22:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134107">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🇮🇷
بیانیه باشگاه پرسپولیس در خصوص تصمیم عادلانه فدراسیون فوتبال و سازمان لیگ
🔴
باشگاه پرسپولیس در بیانیه‌ای ضمن تقدیر از فدراسیون فوتبال و سازمان لیگ، تصمیم برای برگزاری دو مسابقه به منظور تعیین نماینده سوم ایران در رقابت‌های آسیایی را اقدامی عادلانه و در…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/134107" target="_blank">📅 22:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134106">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🇮🇷
بیانیه باشگاه پرسپولیس در خصوص تصمیم عادلانه فدراسیون فوتبال و سازمان لیگ
🔴
باشگاه پرسپولیس در بیانیه‌ای ضمن تقدیر از فدراسیون فوتبال و سازمان لیگ، تصمیم برای برگزاری دو مسابقه به منظور تعیین نماینده سوم ایران در رقابت‌های آسیایی را اقدامی عادلانه و در راستای تحقق عدالت فوتبالی دانست و تأکید کرد که «حق باشگاه‌ها باید در زمین مسابقه مشخص شود.»
🔴
در بخشی از این بیانیه آمده است: «بسیار خرسندیم که تصمیمی درست، ورزشی و منطبق با عدالت اتخاذ شد تا سرنوشت سهمیه آسیایی در مستطیل سبز رقم بخورد. امیدواریم تیم‌های حاضر در این دو دیدار با ارائه مسابقاتی جذاب و جوانمردانه، نمایندگان شایسته‌ای برای فوتبال ایران در آسیا باشند.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/134106" target="_blank">📅 22:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134105">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
مدیران باشگاه پرسپولیس برای توافق با بیفوما برای جدایی کار بسیار سختی دارند! / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/134105" target="_blank">📅 20:54 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
