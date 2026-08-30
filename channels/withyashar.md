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
<img src="https://cdn4.telesco.pe/file/dr-oemOtFIAJqvXa_OycHatoHKAKxeJF_F-fA8cpf_eUbeHvuHElIpacv66i27nsAc0kog-naMveZZcEPuw1nmEwuP-KR9Gppf_xOga5Ih1JPTx4xt5_dS0G3U2sgLIuZRv2NBlwx-bXUSamBUTXrkuvub12iL3jhTOpJZ5JtP3IqJtHA6i0XPS-91NhL_GBSF27XEzLGZNyY5u1oexxry5VW2k_2sY4VyMIX1VjpmAb-BTnJyecOXuPvNudOlFmCktUuzAFiu3_9Vf-4keHdX3VIQmMpTeykEqp0vLkv8YK5-W_UsfrVw1p5oUAJ1Gcfou1lVSmD28-dweaj97rew.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 439K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 12:13:41</div>
<hr>

<div class="tg-post" id="msg-21705">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آکسیوس به نقل از گزارش سنتکام میگه جمهوری اسلامی یه مشت آشغال ریخته بود (۲۰۰ شئ شکل مین) تو تنگه میگفتن مین‌گذاری کردیم ولی کلا ۱۱ تا مین انداختن تو آب، که ازون ۱۱ تا ۵ تاش درست انجام شده بوده
.
@WarRoom</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/withyashar/21705" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21704">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqQL4LIn9lW4qb_F84B6RFSbdqr1199qk7iMX8DLhz2vKTRVrkvH2GYi37_fpRCJsV1SiZF-u_dWAs4wYoSI9eTmI7dbdv-JfhMa_k5hHq-hM5BO1npbicUPzqk0UjG7Pel_kA-AzVmkz3BglHQR9ru8J8vFuOR40DFCn-zkgmh57igtaOuxbVrMFsgwgykdyzmSQQsDDQutnsio-lMz-q67Arn1TCC5XuGAbUqAbibTKSa1U8IO9ttiRfvFTZF5aQBs6fxtLc3wit0jtjLWkuH03to-pYGgzcGIbTzNJoSK5shr2k-0HPqIjt9g2NC6-28bW3jCxFysTTbxOfpcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۲ فروند جنگنده F-16C/D گارد ملی هوایی اوهایو
از بال ۱۸۰ شکاری و اسکادران ۱۱۲ شکاری در مسیر خاورمیانه هستند. این جنگنده‌ها با کال‌ساین‌های
TABOR11 تا TABOR16 و TABOR21 تا TABOR25 و TABOR17
ابتدا به پایگاه لاژس در آزور پرتغال می‌روند و سپس راهی خاورمیانه می‌شوند. در این عملیات، هواپیمای سوخت‌رسان
GOLD10 (AE066E / 62-3569)
پس از سوخت‌رسانی به جنگنده‌های TABOR11 تا TABOR16 و
GOLD12 (AE44FF / 23-46116)
در حال بازگشت به پایگاه گارد ملی هوایی بنگور است. همچنین
GOLD22 (AE0479 / 58-0061)
برای ادامه سوخت‌رسانی به جنگنده‌ها در حال حرکت است و
GOLD25 (AE5FAC / 19-46065)
نیز در این مأموریت حضور دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/withyashar/21704" target="_blank">📅 09:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21703">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بر اساس گزارش نشریه "اکسیوس" به نقل از منابع: مدیر سازمان اطلاعات مرکزی آمریکا (سیا) پیشنهادی را به مسکو ارائه کرده است مبنی بر برگزاری یک اجلاس که در آن ترامپ، پوتین و زلنسکی حضور داشته باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/21703" target="_blank">📅 03:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21702">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">@WarRoom
جعبه شیرنی ۲</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/21702" target="_blank">📅 02:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21701">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشایان</strong></div>
<div class="tg-text">سلام یاشار جان. این یه پیام دلیه که برات می‌نویسم زیاد ربطی به ماجراهای روزمره نداره. خوشحالم که پیدات کردم اینارو بهت بگم چون بنظرم خیلی بیشتر ازینا حقته بدونی. من ۳۰ سالمه. ۸ سالم بود که تو دبستان شهید باهنر تجریش با رفیقام قفل وبسایتت بودیم. تو زمانی که آخوند نمی‌ذاشت بچه های ایران نفس بکشن یاشار رپفا یه تنه آرتیستای جدید و سبک جدید حمایت می‌کرد و میاورد بالا و من چون اینترنت خونمون دایل آپ بود می‌رفتم پاساژ البرز تجریش، یه مغازه بود مسعود موزیک که سی دی پستای جدید وبسایتتو برامون میزد و اون زمان رپ برای ما انگار تمام آزادی و چیزی بود که نداشتیم. و امروز برام اصن عجیبه که حتی پزشو نمیدی و زیاد به روی خودت نمیاری که اگه تو نبودی اصن چیزی به نام رپ فارس با اون دوره تاریخیش که هیچوقت دیگه اونطوری نشد به وجود نمیومد. الان شاید نسل جدید باورشون نشه اما ما یادمون نمیره تو کی بودی و چیکار کردی. تو فری استایل همه رپرا یه پسر عینکی لاغر بود که کم کم همه فهمیدن این یاشار رپفاعه. خوشحالم که الان از طریق این کانال از حالت باخبرم. به امید یه روز که تو ایرانمون، توی یه ایونت که کتاب خاطراتت از رشد موسیقی زیرزمینی ایرانو نوشتی و برا علاقه مندا امضا می‌کنی بیام و کتابتو بخرم و امضاتم بگیرم. عشقی داداش.</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/21701" target="_blank">📅 02:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21700">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">@WarRoom
جعبه شیرنی</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/21700" target="_blank">📅 02:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21699">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromalireza</strong></div>
<div class="tg-text">سلام یاشار جان عشقی
امروز دو تا مشتری اومدن (من صندوق دار یه مغازه شیرین عسلم تو پایین شهر) دو تا مشتری اومدن زرتشتی بودن و اصالتا یزدی واقعا خیلی آدمای با شخصیت و خوش رو خوشتیپ خوش صحبت با فرهنگ بالا با اصالت و واقعا زیبا بودن اصا انرژی مثبت فراوان اصلا خیلی حالم خوب شد و انرژی گرفتم
ولی در روز چند رأس عرزشی میان مغازه واقعا آدمای کثیف بی شخصیت بی ذات پرو و طلبکار بد رو کثافت و کثیف بد تیپ بد چهره شبیه خوک میمونن و شپشو ان آدم حالش بهم میخوره و واقعا اعصاب خورد کنه وجود شون حروم زاده های بی مغز قاتل
واقعا بی صبرانه منتظر روزیم که از دست این شیعه ها و عرزشیا خلاص شیم و مردم با اصالت مونو ببینیم و کلی کیف کنیم</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/21699" target="_blank">📅 02:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21698">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اتاق جنگ با یاشار :
P-8 Poseidon
@WarRoom</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/21698" target="_blank">📅 01:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21697">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اتاق جنگ با یاشار : تنگه دعوا شده
@WarRoom</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/21697" target="_blank">📅 01:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21696">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
🚨
چندین کزارش از شنیده شدن صدای انفجار از تنگه هرمز
@WarRoom</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/21696" target="_blank">📅 01:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21695">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/21695" target="_blank">📅 01:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21694">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">@WarRoom
hamshahri javan</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/21694" target="_blank">📅 00:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21693">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/21693" target="_blank">📅 00:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21692">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏آزاده اخلاقی، همسر محسن نامجو می‌گوید نامجو ۶ روز پیش «به بهانه پرینت چند کاغذ در سر کوچه» با یک صندل از خانه خارج شد و ناگهان با چمدانی که از همسرش ربود، از ایران سر درآورد. اخلاقی همچنین افشا کرد که نامجو حتی پاسپورت جمهوری اسلامی را نداشته و با واسطه‌گری بهمن بابازاده، خبرنگار امنیتی که ۶ ماه با نامجو در تماس بود، مجوز حکومتی برای بازگشت به ایران را دریافت کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21692" target="_blank">📅 00:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21691">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtMY5cny8CCXcnLfgtuLESDy8FOL_Fw4ENDRDMWCBauzavYOD6WMpnyoaQSE0XSUPVga95mefnUSaLr7iRvlHZaRuJvbZbfQUdCqDAQaeEvgRpkeufmBNO0FyVVdHBWZHIqz2HU7im9zBwnMscetRdQb5OyrJ-No1PTR76TKDW2YrOngiPfEKgLHYllueChYeBB6El7DZ5_AS-lb1ZxsInjXS7wT77yHGY_Oe78fKW0dq39spJfgaSSZbxecqB548A-TlvZKQsLaS8u1mqolC8Snj37bL8obQtzQAUmL2KShb-DHtCH3YLsTm4Xm04NHS8zDN3Z08zCXTlkzMeEZsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کارگاهی محدوده بزرگراه آزادگان انفجار رخ داد ؛ یک کارگر جان باخت ,در این حادثه یک کارگر 21 ساله جان خود را از دست داد و یک مرد 30 ساله نیز مصدوم شد.
@WarRoom</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/21691" target="_blank">📅 00:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21690">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flJtZk0_wWeEuZh1IagvLtHqz-cveHMYkBtTTc15RTR3RJG_PLTvyc06GhXrANSZZJ3_tZXS7Y25LW7onxHdRo6LXTEHAr5vo_xIrQhftMXI7QAxTtAON7eDyKL5Xm6q4ScXSWtW0e3oKjoJJlF80-URyOEpPdLV0xGlsfkvF1KvydJe4Mn-SVywka9O86OQTx77U5K7Onglyq5a91JgIY7kVCZvT6Il5ZIH9uxX67DnlnzjnmK0DLNTzl0fDiwL9QEDIr67bT7PcuDtUef_lSoqhkmD7hbo0rW8Aa9jUoMbdjd-eKGo1XAOJ4zChTpQincnkbsUmMkCuwd4El9Sqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل
: فرمانده یگان نخبه و یک
تک‌تیرانداز حماس در غزه کشته شدند
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21690" target="_blank">📅 23:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21689">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پدافند جنوب غرب تهران فعال شد
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21689" target="_blank">📅 22:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21688">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">کاظم دست کج غریب‌آبادی:
تلاش قطر و پاکستان این بود که بررسی کنند آیا امکان بازگشت به اجرای تعهدات تفاهم اسلام‌آباد وجود دارد یا خیر.
ایران آمادگی خود را از طریق تفاهم با عمان درباره تنگه هرمز مشخص کرده، اما اجرای تعهدات بر عهده آمریکا است.اما آمریکا تعهدات خود را متوقف کرده
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21688" target="_blank">📅 22:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21687">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">باراک راوید خبرنگار آکسیوس: ابتکار بستن تنگه هرمز از سوی فرمانده نیروی دریایی سپاه مطرح شد
دو مقام اسرائیلی به باراک راوید گفتند با اینکه طرح بستن تنگه هرمز توسط سیاست مداران ایرانی درحال بررسی بود، تنگسیری بدون گرفتن اجازه کل تنگه هرمز را مین گذاری کرده بود
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21687" target="_blank">📅 21:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21686">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بانک مرکزی امارات متحده عربی با تأکید بر لزوم رعایت قوانین توسط تمامی شعب «بانک مصر»، از آغاز تفتيش و بازرسی فوری این بانک در رابطه با مبارزه با پول‌شویی خبر داد و اعلام کرد که اقدامات احتمالی بعدی را بررسی می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21686" target="_blank">📅 21:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21685">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مارک لوین : قطر یک رژیم سلطنتی و اسلام‌گرای شیطانی و نامشروع است
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21685" target="_blank">📅 20:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21684">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9a3d293ea.mp4?token=dnv-P0vdBF-9hDSZPuTJRt7y_Vv3cpXPUDzETclUmKSzrLdKSANMzA8o1QXW-tSJjsKo9KRs0eqmZrnPDNhWHvd1LKO7NB9axriX_fghB_YsvPFgVa7_xrHBuMRIsQvPWChLH08Sh-xL0MK2MiaJLxDjpIakvZiyCIHfFprVlqWAUUMiwvAiTq21VHSOKfTN0Q9l3469A5aB8sdJzXFDzMwPRCyfG4jYTbot-4Jv0DKhP3jeKNYZMQH14cwwmZW1N9r1nSqSAMs7WrZhAvGxgKbg4mWCIlINF5qIbHXjZhOKAfsE2Dp8v6rWOui_qfsylErkQxFMzkpH4XgUahPr5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9a3d293ea.mp4?token=dnv-P0vdBF-9hDSZPuTJRt7y_Vv3cpXPUDzETclUmKSzrLdKSANMzA8o1QXW-tSJjsKo9KRs0eqmZrnPDNhWHvd1LKO7NB9axriX_fghB_YsvPFgVa7_xrHBuMRIsQvPWChLH08Sh-xL0MK2MiaJLxDjpIakvZiyCIHfFprVlqWAUUMiwvAiTq21VHSOKfTN0Q9l3469A5aB8sdJzXFDzMwPRCyfG4jYTbot-4Jv0DKhP3jeKNYZMQH14cwwmZW1N9r1nSqSAMs7WrZhAvGxgKbg4mWCIlINF5qIbHXjZhOKAfsE2Dp8v6rWOui_qfsylErkQxFMzkpH4XgUahPr5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در تروث : دریاچه آمریکا توسط اردک‌های دونالد محافظت می‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21684" target="_blank">📅 18:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21683">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ‌ در تروث : «سی‌ان‌ان (CNN، شبکه خبری آمریکایی) در یک مارپیچ مرگ قرار دارد و MS NOW (شبکه خبری آمریکایی که به‌تازگی نامش از MSNBC تغییر کرده و ترامپ با کنایه آن را “MSDNC” می‌نامد) هم همین وضعیت را دارد؛ واقعاً تقریباً هیچ‌کس هیچ‌کدام از این دو شبکه را تماشا نمی‌کند! بهترین فرد در سی‌ان‌ان، هری انتن (Harry Enten، تحلیلگر و نظرسنج سیاسی CNN) است، چون حاضر شد نشان دهد که دونالد جی. ترامپ (رئیس‌جمهور آمریکا) شش برابر محبوب‌تر از آبراهام لینکلن (رئیس‌جمهور شانزدهم آمریکا)، جرج واشنگتن (نخستین رئیس‌جمهور آمریکا) یا هر رئیس‌جمهور دیگری است. او اعتبار دارد؛ اخراجش نکنید! سی‌ان‌ان را می‌توان با مدیریت و مجریان جدید دوباره احیا کرد، اما MS NOW را نمی‌توان! چون یک برند بزرگ را هرگز نمی‌توان واقعاً نابود کرد!»
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21683" target="_blank">📅 18:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21682">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مرکز اطلاع‌رسانی فراجا : الف.ل، از سرکردگان شبکه تراستی که طی سال‌های گذشته مبادرت به دریافت ارز حاصل از صادرات کرده بود، توسط کارآگاهان پلیس امنیت اقتصادی فراجا شناسایی و دستگیر شد. بدهی این فرد به شبکه بانکی کشور، ۳۰۰ میلیون یورو معادل بیش از ۷۰ هزار میلیارد تومان است. این فرد تاکنون از اجرای تعهدات خود امتناع کرده و متواری بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21682" target="_blank">📅 17:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21681">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTjW3DCG9Q6SP90Z7mZ9qWdnddcvkskYJc1yjr3lKyb1Yz5bGWFsRRi2kxmT0iA0cpIv-teZ2ukIOYGkb_1EChClmz_2my3brrg-25nEHPY5l7zGWodhz3so2BevvH4j8B-CVBs7NQm6eUW_2u3xwUoZWre79__otshk7wDtDesIt1QmygZBbhjZfswlBXd2p-Pep1PNbvQTI1culnXf1Ut0cOlQFw1pvOoTKkEQaOBO09HRQq6M8LReXaGqnvH7_fOib6lkRON808hi8k3pDscTij9CxTApmuAz8y5k1n9sZ1kKaGOoQhim3ljLu1byJ5S7_vJKD1tXuZkI5_A0WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت کارکنان ناو لاوان به کشور پس از 7 ماه
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21681" target="_blank">📅 16:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21680">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خبرنگار وال استریت ژورنال:
هیچ چیز به اندازه احتمال ادامه حمل و نقل دریایی هدایت‌شده توسط آمریکا از طریق تنگه هرمز، به اهرم فشار رژیم آسیب نمی‌رساند. اگر این امر ادامه یابد، اوضاع را تغییر خواهد داد. اگر چنین شود، اوضاع بسیار بد خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21680" target="_blank">📅 16:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21679">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCM3pO2HSVxGnSZdJf1Y52aDlFd4N0RhcH0Oicb8w_B3-3Y3bnGL4dKLLONqHRahKlcKlY-rPGmCtb1WAuvTk7gIrfUSlOiB_Gk47Rr77a4QWYBHM7m1PyQuYmmyAwshZpxCRNDgIjAPGscHnG1_5Mk9FvMPmDyIxOANGNkStkh_iCpCjIw0J64Yk1XmvyznYge8qWLx0IBjhip1pCVSNypAFpbwEs_Zt6FzXR3_WwPp3DAJ6ZZsvQEqdAy_KKfjLWP5zKMXu3PUy5hNEQdCMqEfwtXOw9olb_WBrQVF8t0iXNtgPFPjpqnPCTajkJx4v2vP2o8P0q4HIy1W7LEG8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر ماهواره‌ای از بقایای ناوچه‌های جماران، نقدی، بایندر و چند شناور دیگر
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21679" target="_blank">📅 15:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21678">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اتاق جنگ با یاشار : شکاف و درگیری در  بدنه حاکمیت
؛ تنها ساعاتی پس از آنکه مجتبی خامنه‌ای در پیام خود به مناسبت هفته دولت تأکید کرد بیان ضعف‌ها و کاستی‌های کشور در شرایط جنگ می‌تواند به دشمن روحیه بدهد و به انسجام جامعه آسیب بزند، مسعود پزشکیان در گفت‌وگوی تلویزیونی تصویری کاملاً متفاوت از وضعیت اقتصادی ارائه کرد و گفت: «پول و درآمد نداریم» و دولت با کمبود منابع مالی و ارزی روبه‌روست و مشکلات کشور بیشتر شده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21678" target="_blank">📅 15:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21677">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رویترز: جنگ و تشدید تحریم‌های آمریکا فشار سنگینی بر اقتصاد ایران وارد کرده است.
مقام‌های ایرانی برای نخستین‌بار در این گزارش به ابعاد قابل‌توجه فشار اقتصادی اذعان کرده‌اند؛ مسعود پزشکیان می‌گوید تجارت خارجی ایران به دلیل تحریم‌ها و محاصره دریایی آمریکا حدود
۳۵ درصد کاهش یافته
و تورم سالانه نیز به
۶۶ درصد
رسیده است. مجتبی خامنه‌ای هم از دولت خواسته برای مقابله با تورم، بیکاری، افزایش قیمت‌ها و مشکلات بازار اقدام جدی انجام دهد
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21677" target="_blank">📅 14:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21676">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3UNTm82g9CUiMTt-d7IMb-Wn89_gJkPXbyKBPZ-BVz7Fa5SM36Bxw-1McOQYlRrdJasUYPctMBPdpmhO7nKw1E79AibqTNsYjB1jpnBw6LREBXS1e6Ak26YDZifyjPNtYQ1ut8iJjVO2PkBK9QxaL6JcE2ZLY6thZDjgadtMhm8rRu5Fmt4Zo3fGwTq32nMi16YulXeMy5c-famBAZ70mvltgPJ7ste0jgUnAvxou4rr2EmQ_yAOskoAmJAg4o7Aaio3NKXhDZvmEfjwpwH_UqR7NUZefhQsKHc-BxYNifDM6f4CW8zDelWHGb3KTR3iEqKxjKL_VXYBMO7uvbfPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب، یک تانکر نفتی به نام "ELLIE" تلاش کرد تا از تنگه هرمز عبور کند و از مسیر جنوبی استفاده کرد که توسط ایالات متحده پشتیبانی می‌شد، اما این تلاش ناموفق بود و تانکر به عقب بازگردانده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21676" target="_blank">📅 13:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21675">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خبرگزاری هاآرتص در تحلیل‌ خود درباره وضعیت ایران، با اشاره به تضعیف موقعیت جمهوری اسلامی، افزایش فشارهای داخلی و خارجی و نگرانی‌های فزاینده در میان مقام‌های حکومت، ارزیابی کرده است که احتمال به خطر افتادن بقای جمهوری اسلامی نسبت به گذشته جدی‌تر شده است
@WarRo</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21675" target="_blank">📅 13:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21674">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مؤسسه نیروی دریایی آمریکا USNI : گزارش داده است که ناو هواپیمابر تئودور روزولت CVN71 و ناوگروه رزمی آن در هفته‌های آینده از سن‌دیگو حرکت کرده و برای استقراری بیش از هفت‌ماهه در خاورمیانه آماده می‌شوند. فرمانده ناو نیز خدمه را برای مأموریتی حدود هشت‌ماهه آماده…</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21674" target="_blank">📅 13:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21673">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نرخ دلار ۲۰۷،۰۰۰ تومان(سقف تاریخی)
دلار کف بازار ۲۱۰ هزار تومان(سقف تاریخی)
تتر ۲۰۴،۰۰۰ تومان
بیتکوین ۷۷،۶۳۷ $
انس جهانی طلا ۴،۴۵۳ $(آخرین قیمت)
نفت برنت  ۸۸،۱۰$(آخرین قیمت)
@WarRoom
۱ ظهر تهران</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21673" target="_blank">📅 13:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21672">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الجزیره : ترامپ ترامپ می‌خواهد سایه جنگ ایران را از انتخابات کنگره دور کند به افکار عمومی داخل آمریکا و بازارهای جهانی اطمینان دهد که منابع انرژی دوباره با قیمت‌های قابل‌قبول در دسترس خواهند بود و ایران دیگر این سلاح مهم، یعنی تنگه هرمز، را در اختیار ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21672" target="_blank">📅 12:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21671">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">استیون میلر، مشاور کاخ سفید:
تنگه هرمز برای ایالات متحده باز و برای ایران بسته است!
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21671" target="_blank">📅 12:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21670">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">فرمانده مرزبانی فراجا از کشف ۳۸ قبضه سلاح جنگی با اشراف اطلاعاتی مرزبانان در غرب کشور در مرزهای استان کردستان خبر داد.در این عملیات، ۳۸ قبضه سلاح جنگی شامل ۲۰ قبضه کلاش و ۱۸ قبضه کلت به همراه ۳۹ عدد خشاب و یک هزار و ۳۵۰ عدد فشنگ جنگی و یک دستگاه بیسیم کشف و ضبط شد.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21670" target="_blank">📅 11:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21669">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ در‌تروث مدعی شده آمریکا با ونزوئلا به یک توافق تاریخی نفتی دست یافته که بر اساس آن، بخش خصوصی با حمایت دولت آمریکا کنترل اکثریت بیش از ۶۵ میلیارد بشکه ذخایر اثبات‌شده نفت ونزوئلا را به دست می‌گیرد؛ به گفته او، این قرارداد بدون هزینه برای مالیات‌دهندگان…</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21669" target="_blank">📅 11:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21668">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ در‌تروث مدعی شده آمریکا با ونزوئلا به یک
توافق تاریخی نفتی
دست یافته که بر اساس آن، بخش خصوصی با حمایت دولت آمریکا
کنترل اکثریت بیش از ۶۵ میلیارد بشکه ذخایر اثبات‌شده نفت ونزوئلا
را به دست می‌گیرد؛ به گفته او، این قرارداد بدون هزینه برای مالیات‌دهندگان آمریکایی، ذخایر نفت آمریکا را بیش از دو برابر کرده و در آینده باعث افزایش عرضه نفت و کاهش قیمت بنزین در آمریکا خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21668" target="_blank">📅 11:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21667">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وال‌استریت ژورنال به نقل از منابع آگاه گزارش داد دولت
ترامپ
به میانجی‌های مذاکرات ایران اعلام کرده است که
هیچ علاقه‌ای به بازگشت به چارچوب تفاهم اولیه‌ای که در ژوئن با ایران شکل گرفته بود ندارد
.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21667" target="_blank">📅 10:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21666">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وال‌استریت ژورنال به نقل از مقام‌های آمریکایی گزارش داد واشنگتن با سرعت در حال انتقال مقادیر زیادی مهمات، موشک‌های رهگیر و تجهیزات نظامی به خاورمیانه است تا توان نیروهای آمریکایی و متحدانش برای مقابله با تهدیدهای احتمالی ایران تقویت شود. این انتقال شامل سامانه‌های دفاع هوایی و موشکی، از جمله رهگیرهای پاتریوت و تاد، از نقاط مختلف جهان به منطقه است. مقام‌های آمریکایی می‌گویند این اقدامات بخشی از تلاش واشنگتن برای تقویت حضور نظامی و حفظ آمادگی دفاعی در برابر هرگونه اقدام احتمالی ایران است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21666" target="_blank">📅 10:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21665">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نیروی دریایی سپاه انقلاب اسلامی: رویکرد ما در مورد تنگه هرمز تا زمانی که اقدامات آمریکا متوقف شود و این کشور به تعهدات خود عمل کند، ادامه خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21665" target="_blank">📅 02:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21664">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7E-IGhjEznok24_UjteJyN_-t_0u44G517PE0rweAbOuQZ9P_5X2RzI79g00VCThvjyFRxiyWXg20uZ28uaC4I3ITF2EQgTDOLBzqyxhSU90q6hIQ_nkumV-pYgTEltRMITvDlNeTPHNAy-7ejXwo0KNZsoDCeQXlXtIXM51hYLPR0OomqZTenzkU3Okdm6krh1GHuTWZc070uLiRV4X6tqDmON2YbopnacvJv0uwggmchMcgSsF7C1oTJgQadyIYR393LdQSUvOATvlGbmLrZnyRXl07m-VKkBcM9AerEnsjyBQRiseEysH_DMQPMgpmJU5eCV9T0tGByIqU447w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای جدید نشان می‌دهند که یک عملیات لایروبی مخفی برای ایجاد یک مسیر دریایی جدید در سمت عمان از تنگه هرمز در حال انجام است.
این مسیر دریایی حدوداً 1600 فوت عرض و عمق طبیعی آن تقریباً 93 فوت است، که نیازمند لایروبی محدود برای عبور تانکرهای نفتی بزرگ است.
آمریکایی‌ها می‌گویند که کشتی‌هایی که از این مسیر عبور می‌کنند، به دلیل جزیره مسندم و انحنای زمین، خارج از دید ایران باقی می‌مانند!
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21664" target="_blank">📅 00:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21663">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اتاق جنگ با یاشار :  امشب مارگاریتا زدم
😁
ببینیم چی‌میشه … بیداریم
⚔️</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21663" target="_blank">📅 23:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21662">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18d571649.mp4?token=BId2FEoLP6eA8yME3ViP5eYaX-h3ACPmT7RPt4C67hvmGmyaIWqPBIaoKHbVBCBSY8BJNrgLy_zBRrCpmUjdAXfHwOFWWIImnBI50aei9iExqsMzV0RvzyQWxGgbhTxbb7KqkBVLTyBzeQFXgCmM_b57yLo661yvs-QqpL_4_-PNBZ9sGiJujm2kW3CLM__Hcp7hCxqZ_6D_BbxWvkPcUcsZGkxJX5Sdpjn3H9eoxg_TVRXmOHKRanryCI6VNQglCQnL_FXb-JBpeBMSYLZPFqghvBk4C_xP2lKKHMd13AzPSyoddr-ZNVoFRArTTpgYZOhwSUvgZTwqsbG60HWbhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18d571649.mp4?token=BId2FEoLP6eA8yME3ViP5eYaX-h3ACPmT7RPt4C67hvmGmyaIWqPBIaoKHbVBCBSY8BJNrgLy_zBRrCpmUjdAXfHwOFWWIImnBI50aei9iExqsMzV0RvzyQWxGgbhTxbb7KqkBVLTyBzeQFXgCmM_b57yLo661yvs-QqpL_4_-PNBZ9sGiJujm2kW3CLM__Hcp7hCxqZ_6D_BbxWvkPcUcsZGkxJX5Sdpjn3H9eoxg_TVRXmOHKRanryCI6VNQglCQnL_FXb-JBpeBMSYLZPFqghvBk4C_xP2lKKHMd13AzPSyoddr-ZNVoFRArTTpgYZOhwSUvgZTwqsbG60HWbhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: اونایی که میگن تحریم تاثیر نداره عقلندارن
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21662" target="_blank">📅 23:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21661">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFAzfuNi3Tc-WA9t4nVJ1kbuikkiECMvJZ_HkRjPnJi6JTploOqnYBRabnFzGeuaQ0GcCFrD3qcgeCoTs06_Kn38GMgn4Tl6bW3Zhvd2l-0UhkWudJtJIX-V0dhpMr6CMrKTmog01eUR7pLPqu7cgEVJhLX2S9VkGyy5keEFm2S34qlax2ugPWYwnNiTCe3fl4OPttMQKXCaQjvbKlvEZ8BKSaKqeprmGRhYENIDmSN5EQp2NDXznEuJc-I88pii-WwpkJYrO38d-jeCeEmaiNJ9XBiYAHZtMXyjWkbZh0u5gM3H012y_Ld2OrJ9bx5bDoZLui_XWdiVBzS9TaKA_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : مخفیگاه دقیق: سه تا موشک/پهپاد ساعت نزدیکای ۲۲ از نزدیک مدرسه پرتاب شد یه تونل دارن فقط چند صد متر با خونه ها و مدرسه فاصله داره یه جاده اسفالت فرعی هست رد میشه  صد یا دویست متر بیشتر با محل پرتاب اینا فاصله نداره..سیریک-بمانی @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21661" target="_blank">📅 23:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21660">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دیدبان اتاق جنگ : مخفیگاه دقیق:
سه تا موشک/پهپاد ساعت نزدیکای ۲۲ از نزدیک مدرسه پرتاب شد یه تونل دارن فقط چند صد متر با خونه ها و مدرسه فاصله داره یه جاده اسفالت فرعی هست رد میشه  صد یا دویست متر بیشتر با محل پرتاب اینا فاصله نداره..سیریک-بمانی
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21660" target="_blank">📅 22:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21659">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مسعود پزشکیان هم اکنون اعلام کرد نرخ سوم بنزین، از ۵ هزار تومان به ۱۰ هزار تومان افزایش پیدا می‌کند.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21659" target="_blank">📅 22:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21658">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دیدبان اتاق جنگ : سه تا پهباد بودن یکی افتاد نزدیک ساحل
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21658" target="_blank">📅 22:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21657">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnF6gFXtGjr_lbQGgEknl5Hy4rstKBFDC1e1wOfaYUzL-rDus8PgAuhzhePBfvC2fPO-L01y9JRNbfSpmfie6ZJApXJGi72cPiypr2GC7FdMvwZfN8uWLJFuFQ4JH70F6vlrDkUnjJ_nyPkzTQbyMFzMkQcYZWg3wYsZQzda4I3hE1XEIrcTYLXX0MJkFf78NhelukeP99hpAvL3YklhZyOGMaVC_QRWt82gpyPGa1xuP8Kv8Tut75WyDZQ-6wIGIWNV0E1EZompz9WGLnj7jw05FLMNsqSyaqnAoO_vqESYLl1NNYt1mpSAQPZU1o03v_4xx3Esc4gdAigHH0T24w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی در تنگه هرمز در آتش میسوزد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21657" target="_blank">📅 22:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21656">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گزارش ۳ پرتاب از سیریک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21656" target="_blank">📅 22:10 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21655">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گزارش ۳ پرتاب از سیریک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21655" target="_blank">📅 22:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21654">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مستند و مصاحبه جنجالی کامل تلویزیون إسرائيل با یک نیروی ایرانی ویژه در موساد با نام مستعار آرش در داخل ایران ( در این مستند صحنه ها بازسازی شده اند ) که در طول جنگ۱۲ روزه نقش مهمی را در انهدام سایت های پدافندی جمهوری‌اسلامی ایفا کرده بود. با زیر نویس فارسی…</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21654" target="_blank">📅 21:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21653">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کرملین
: پوتین ۱۰ شهریور با پزشکیان دیدار می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21653" target="_blank">📅 21:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21652">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">موشتبی ای آی : گاهی اوقات، بیان صادقانه نقاط ضعف ما، کمک بزرگی به دشمن است.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21652" target="_blank">📅 21:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21651">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52453c0c98.mp4?token=SKreyovLR_1MGmDRbm-u79nXBSKzPKEjOgNY7fk_9vW7uOR4aL-anoQ-8K52-lq4ZMUT6pOA-tE61VbtzGgH6Qe3iICGSa4rPsbs0jEV0fzx0mrafWamJ5RYmaFmMcYOk3-j-_RX1d2qYd71KIaBn3ZypgNCr2v4AbCt6eOIbqR3PfX4MTaNBVeeQbgDooXCzUbNYyunE75OVxQU5C9cmHeSIwp8oJkTSj9CVTmYFRm76RyQ-1LAIDVqC8d-J_TRmgBM9NENOJ_rrfnBV97fWgnJmxLpLHU1JkGCx0f2NwojFhqURLGzMYi2b6S7OgIhSyifezXBv5fwzESV4kJjww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52453c0c98.mp4?token=SKreyovLR_1MGmDRbm-u79nXBSKzPKEjOgNY7fk_9vW7uOR4aL-anoQ-8K52-lq4ZMUT6pOA-tE61VbtzGgH6Qe3iICGSa4rPsbs0jEV0fzx0mrafWamJ5RYmaFmMcYOk3-j-_RX1d2qYd71KIaBn3ZypgNCr2v4AbCt6eOIbqR3PfX4MTaNBVeeQbgDooXCzUbNYyunE75OVxQU5C9cmHeSIwp8oJkTSj9CVTmYFRm76RyQ-1LAIDVqC8d-J_TRmgBM9NENOJ_rrfnBV97fWgnJmxLpLHU1JkGCx0f2NwojFhqURLGzMYi2b6S7OgIhSyifezXBv5fwzESV4kJjww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
:
می‌بینید که چقدر خوب می‌جنگیم. ما بسیار خوب می‌جنگیم. به ونزوئلا نگاه کنید. فقط ۴۸ دقیقه!
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21651" target="_blank">📅 20:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21650">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f934b07069.mp4?token=dHZv25V8VgiKo2RCMu25_nfjLh8u1u7US9EpAvypfL_MNMwtD5brfsIBTSjPCkCPtJmOOBKQLGJQAvZLSZV75KPu7mpxBY-_btYC99-qjBC89hzL9S2UbwyS0cB1Dq6Xqhnj2XPXqWwTtAiidBU6hLw2Ug1U30quOo8JOBF2ChZZxXbqxmZciAAYKd0pD0B5RSlmLMnE4jDjCOy5BFAqyn3KjxNuHwEpTAXsXGQ0TvquGC2D1tXoKUdaTbW5l2GclcMbpmRfF_Cl60II6CRXUkgPirF-JMWFWwNJWdC1m14HwVlFp_Y7EyHJ65LVTsbYhWC6DV6P5f0DL-IAmpqnfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f934b07069.mp4?token=dHZv25V8VgiKo2RCMu25_nfjLh8u1u7US9EpAvypfL_MNMwtD5brfsIBTSjPCkCPtJmOOBKQLGJQAvZLSZV75KPu7mpxBY-_btYC99-qjBC89hzL9S2UbwyS0cB1Dq6Xqhnj2XPXqWwTtAiidBU6hLw2Ug1U30quOo8JOBF2ChZZxXbqxmZciAAYKd0pD0B5RSlmLMnE4jDjCOy5BFAqyn3KjxNuHwEpTAXsXGQ0TvquGC2D1tXoKUdaTbW5l2GclcMbpmRfF_Cl60II6CRXUkgPirF-JMWFWwNJWdC1m14HwVlFp_Y7EyHJ65LVTsbYhWC6DV6P5f0DL-IAmpqnfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«رویای آمریکایی دوباره بازگشته است؛ فکر می‌کنم این بار قوی‌تر از هر زمان دیگری بازگشته است. در حال حاضر شرایط برای ما بسیار خوب پیش می‌رود.»
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21650" target="_blank">📅 20:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21649">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2130ad167.mp4?token=ir5fQjdm3bL-jkzySOKNyyqUGM9G89_HSk5vCDtqiUJucBfQ9JxiMFYPI2xigEzAqPk5w8m0vQhhC6A6_G8XKciIPwkIQGTkFXS5fqhtEbxFh5fl30JYyAVkYQJ0zaZwafrLTksc7hISxvsnI4fHgeob9H_MSp0fgCMZgQYAHpQvV5I8KHiGpYZdbaOG3_hgIh3O5sgUuYZEcHJZySEVW1Tn0XT_Bc8BO6QEEyLhm9JXEe3uMeUAZfHCOtDj6XitLB9e0iqgM4ptfTh2TvcU8hG4h7HW0PPWB_dtVBoZfTG2TUd-u9aUwtUoUN3CprI7-ZYxnKMdpl87pmuQ90buqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2130ad167.mp4?token=ir5fQjdm3bL-jkzySOKNyyqUGM9G89_HSk5vCDtqiUJucBfQ9JxiMFYPI2xigEzAqPk5w8m0vQhhC6A6_G8XKciIPwkIQGTkFXS5fqhtEbxFh5fl30JYyAVkYQJ0zaZwafrLTksc7hISxvsnI4fHgeob9H_MSp0fgCMZgQYAHpQvV5I8KHiGpYZdbaOG3_hgIh3O5sgUuYZEcHJZySEVW1Tn0XT_Bc8BO6QEEyLhm9JXEe3uMeUAZfHCOtDj6XitLB9e0iqgM4ptfTh2TvcU8hG4h7HW0PPWB_dtVBoZfTG2TUd-u9aUwtUoUN3CprI7-ZYxnKMdpl87pmuQ90buqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی های
ترامپ:
«راستش من دوست ندارم با آن افرادی که پشت سرم هستند(ناسا) صحبت کنم؛ چون بیش از حد خوب به نظر می‌رسند!»
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21649" target="_blank">📅 20:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21648">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا: وزارت خزانه‌داری وعده داده بود تمام شریان‌های اقتصادی باقی‌مانده برای تهران را قطع کند و به تهدید رژیم ایران پایان دهد. او تأکید کرد حامیان ایران نمی‌توانند همچنان به دلار آمریکا و نظام مالی جهانی دسترسی داشته باشند. بسنت…</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21648" target="_blank">📅 20:28 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21647">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">وال‌استریت ژورنال: پروژه عظیم «نئوم» عربستان متوقف شد
وال‌استریت ژورنال گزارش داده است که پروژه چندصد میلیارد دلاری «نئوم» عربستان، به‌دلیل هزینه‌های بسیار سنگین، مشکلات تأمین مالی و بازنگری ریاض در اولویت‌های سرمایه‌گذاری، عملاً به حالت توقف رسیده است.
بر اساس این گزارش، بخش‌های مختلف این طرح جاه‌طلبانه نیز در ماه‌های اخیر با کاهش مقیاس، تأخیر یا لغو روبه‌رو شده‌اند؛ اتفاقی که ضربه‌ای جدی به یکی از نمادهای اصلی «چشم‌انداز ۲۰۳۰» محمد بن سلمان محسوب می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21647" target="_blank">📅 18:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21646">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT-Dj9FLpRmqyqBSwUH7dBJtABkgo6YMfMIYobZUp-fmqXFUJ3U1FwsejNeMYzW6RGeNJnqMAPQIv3iiMzrpCgQ3JOZgz0fGmvnJ-WZmAC-aqOgVaEVoC2nwGoYwncDPpnFKobSk8wIVUIxz4eUaHyPPZFslsiysBt6wHmH-IWiIFC0OgPg1y0d8UgVB9jsHg5mufboT65mgJ3DTdeOoG0z9uPIhTbZbXapQoq2Rkn_d_h2eDXlSmJLlMh9JKVSDzPC9fV4sZMf0jMCO4nGQe5YIpaMGjwN_76g82Rm4oi2LkckA-GldywLaG_BHCNVGeIoV_d6yQqNP9A-zdn54-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
وزارت خزانه‌داری وعده داده بود تمام شریان‌های اقتصادی باقی‌مانده برای تهران را قطع کند و به تهدید رژیم ایران پایان دهد. او تأکید کرد حامیان ایران نمی‌توانند همچنان به دلار آمریکا و نظام مالی جهانی دسترسی داشته باشند. بسنت گفت
بانک مصر امارات
این هشدار را نادیده گرفته و آمریکا امروز نخستین گام را برای پاسخگو کردن این بانک به‌دلیل آنچه «حمایت مستمر و فاحش» از رژیم ایران خوانده، برداشته است.
وزارت خزانه‌داری آمریکا:
در چارچوب «عملیات طرد اقتصادی» (Operation Economic Outcast)، شبکه اجرای قوانین جرایم مالی آمریکا (FinCEN) پیشنهاد کرده است
دسترسی بانک مصر امارات به خدمات بانکداری کارگزاری مؤسسات مالی آمریکا لغو شود
؛ اقدامی که عملاً دسترسی این بانک به بخشی از نظام مالی آمریکا را هدف قرار می‌دهد. همچنین
دفتر کنترل دارایی‌های خارجی آمریکا (OFAC)، رضا محمد تأییدی، مدیر بانک ملی دبی، و یک شرکت پوششی مستقر در هنگ‌کنگ
را تحریم کرده و مدعی شده این شرکت در پول‌شویی وجوه برای یک صرافی تحریم‌شده ایرانی نقش داشته است. خزانه‌داری آمریکا این اقدامات را بخشی از تلاش برای
قطع آخرین شریان‌های مالی مورد استفاده حکومت ایران
عنوان کرده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21646" target="_blank">📅 18:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21645">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گزارش ویژه فاکس نیوز : ترامپ ‌به فاکس نیوز می‌گوید ایران با افزایش فشار اقتصادی، صف‌های طولانی بنزین و تورم فزاینده‌ای که کشور را تحت تأثیر قرار داده، «برای توافق التماس می‌کند».
وزیر امور خارجه ایران می‌گوید دیپلماسی هنوز امکان‌پذیر است، اما استدلال می‌کند که فشار ایالات متحده مؤثر نخواهد بود و از واشنگتن می‌خواهد که اعتماد را بازسازی کند و به حقوق ایران احترام بگذارد.
در همین حال، مقامات نظامی ایالات متحده می‌گویند که خطوط کشتیرانی بین‌المللی پس از عملیات مین‌روبی در تنگه هرمز باز هستند، زیرا رهبر عالی ایران همچنان از دید عموم پنهان است.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21645" target="_blank">📅 17:54 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21643">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bi36ZKtw_CKXHaxXI7y2ZuPJInm_sFHVnP9nsiMKRFFzRATDJq0N8DedqCBIScVOv-FiW1EoQ5DBbJT9q8TX49Y2oRI_UZFse-I-lRqJi2biZiAvXcTQ5wQg5mFu--ZPtXjDpFSgPWPYGpp6_Gpu8yOuum69KHqCDhM4R_Rx2JlwdMxOHzcuv_iuerse7xab9ihVP2JxlVcKjIKjHNs3ywzu2FMxehf6ZFbYumDCT-KcfZcr_qAr8L5ag6Su0F2BPuSQgqiguF5c4qw40jBVNtQM8J5gjUgmv3lL5tXb8e_T2PuOB1TdVF_Pu4qWq4fKgveQ2oNM374StrKJYx4A1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دید بان اتاق جنگ : هم اکنون ستون دود از سمت شرکت کاله آمل پیشتر کارخانه کاله آمل در ۱۵ دی ۱۴۰۴ (۵ ژانویه ۲۰۲۶) دچار آتش‌سوزی گسترده شده بود
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21643" target="_blank">📅 17:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21642">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دبیرکل سازمان بین‌المللی دریانوردی:
حدود ۶ هزار دریانورد در ۴۰۰ کشتی همچنان در تنگه هرمز گرفتار هستند
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21642" target="_blank">📅 16:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21641">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFKov2xtbsRyrDe1VhRyznT-wsa8gtnIOXg9qn9yPXNlzT9TjX5O3g8WnuO5Cqq__-tJ9R6Zuhn5qOG0zitHhvH4pC_ly0gfSH1nqKznbT8J6EA9hKKuudu8kF3TxJK8u7gq9Is1F0tT-1EOMUCs9WbYL4APx0Fbt_Vtq1RmhoaI2RdXtf48YDxP__livOgm3UJtDUgy7iu2Q2g0ZlyAYBMH_wRYWx6IITfSC8PVofQ5n4zTDxzcW4JsAVzDd6dG2CQ8Zdw0pXs7L4FCERjpdbfZn6W6yqS9lwo7duJNl4-ESVz4eK1Zerm0JQg94mqA6gxIxPGx7AoT48yEiWYwsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : دیگه از اون آدم مهربون خبری نیست.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21641" target="_blank">📅 16:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21640">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مستند و مصاحبه جنجالی کامل تلویزیون إسرائيل با یک نیروی ایرانی ویژه در موساد با نام مستعار آرش در داخل ایران ( در این مستند صحنه ها بازسازی شده اند ) که در طول جنگ۱۲ روزه نقش مهمی را در انهدام سایت های پدافندی جمهوری‌اسلامی ایفا کرده بود.
با زیر نویس فارسی
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21640" target="_blank">📅 15:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21639">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxEHTQEicXvqldcZshb2my8sb_6L28J7P24yHG6J2Rgle6cDzij5XvzYbln_IT43l7tITzWUssHw5iCqMnqCfhOy95FhrCbjzlt1cw07jL0MfSBrGX0RT3hO4ZH_xRpYsbWoCLl6dnhJ4PAPmvM5UoCCOe9PdAZgtPJqNztgCH9bCuMrXJpReOpXkoItodOpGkEy1YkGK0xIjzj3tBcE19iPhfpf-7GDIsnxpeXwD5jwNsgOvGSwiQZaYNNm4X0i7vDZELB3rM3gysA5DjV2Y2voRaaQxRxSBAdsPr_gy9drz2z22wxZvu7D2x6cYOcwV358qyusSs2BjI9_46opVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دید بان اتاق جنگ : من با یه صدای لرزیدن شیشه اتاقم بیدار شدم دوباره خوابیدم  ، بعد نیم ساعت رفتم دم پنجره یهو چشمم به این افتاد @WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21639" target="_blank">📅 15:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21638">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50b72f483d.mp4?token=m8cgBhmWuDJ0lw_eNumQsyold9ol13zwszG0LH9iP-zuivwb2j5s-ID2-SBndRWCUUdlqBAcULGsS6VvdAGVe9kEUsIvywP9blUr5GnDqoum803z1Gw5_YpiorLAXUeJW5tYOohol42fwL0JZEVVCNPeKZ1FZ4gbuVeFRpkZm1dAJ7DwrddNXgjkyoEit960mODugmLE3Bu4WI7HoRfcJobNdjxEBaCLGBF180DGJgyu_pO12zyGXY8Z666AI2BP0Yk1zjkc18aDU73ODMxo4VfVOIAOKEsiXIw2O7jvrtci3RY7rZ2Y8r5REglo4OfnxuRNI1dyLXqV2WsCHHf1Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50b72f483d.mp4?token=m8cgBhmWuDJ0lw_eNumQsyold9ol13zwszG0LH9iP-zuivwb2j5s-ID2-SBndRWCUUdlqBAcULGsS6VvdAGVe9kEUsIvywP9blUr5GnDqoum803z1Gw5_YpiorLAXUeJW5tYOohol42fwL0JZEVVCNPeKZ1FZ4gbuVeFRpkZm1dAJ7DwrddNXgjkyoEit960mODugmLE3Bu4WI7HoRfcJobNdjxEBaCLGBF180DGJgyu_pO12zyGXY8Z666AI2BP0Yk1zjkc18aDU73ODMxo4VfVOIAOKEsiXIw2O7jvrtci3RY7rZ2Y8r5REglo4OfnxuRNI1dyLXqV2WsCHHf1Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : اگر ایران سلاح‌های هسته‌ای در اختیار داشته باشد، این پایان اسرائیل و پایان مردم یهود خواهد بود. و مهم نیست که چراغ قرمز باشد، چراغ سبز باشد یا چراغ آبی؛ من به رنگ چراغ اهمیتی نمی‌دهم. این برای من مهم نیست. ما باید این کار را انجام دهیم، زیرا در غیر این صورت نابود خواهیم شد. ما دیگر اینجا نخواهیم بود
@WarRoom</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/21638" target="_blank">📅 15:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21637">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175422b47.mp4?token=XjtmojjzPeOdDAi4uAuxZosK_B-g-S122CyUfR1Yxe9sBcW-hUOjSuGZED4WUMzeNLR_drbyND5_ZRG9ENoc1uYIsaZ8KQ7TFFmZMD_MC7ImWiaRPj66fM8FXpLdvg9qrlszU3XnSIlgnCMyHRvWjSTK-2uudJi32LEXcsVz48Lr_puJvRHYRgiQNY6DdS17Bc4AJAFaXZVBT6E1wNPmJryRJkrMCFtIPJejdD06lZj8RoKd8rhzAzNqIOyS6skWRSRa86sBThj1mbVCrgCmQngDrcwyApO713IMoKJihodJqdakWklnY3cXVnnP7rUcDh7IxIxhHOg3q_Zm6wrBCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175422b47.mp4?token=XjtmojjzPeOdDAi4uAuxZosK_B-g-S122CyUfR1Yxe9sBcW-hUOjSuGZED4WUMzeNLR_drbyND5_ZRG9ENoc1uYIsaZ8KQ7TFFmZMD_MC7ImWiaRPj66fM8FXpLdvg9qrlszU3XnSIlgnCMyHRvWjSTK-2uudJi32LEXcsVz48Lr_puJvRHYRgiQNY6DdS17Bc4AJAFaXZVBT6E1wNPmJryRJkrMCFtIPJejdD06lZj8RoKd8rhzAzNqIOyS6skWRSRa86sBThj1mbVCrgCmQngDrcwyApO713IMoKJihodJqdakWklnY3cXVnnP7rUcDh7IxIxhHOg3q_Zm6wrBCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویری که ادعا می‌شود برای بندر کنگ و لنگه امروز صبح هست.
@WarRoom</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/21637" target="_blank">📅 15:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21636">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca2bad7297.mp4?token=onbaGYUnGtH3Djgi9rav0G6SlkV3zJYirA3HyL8AdTk5Yp5E5DilnLLar8V0f2PEPV4gEVZLZFfFjHF77L62Gt7MSjDbVqpNs1ZjYRn1F5tzsybPg8gVrbhhbffvy0A5URjYFs774lVHTN9Jz5j5YfEOz5LehEfYGDxbys-POpxRF3tqvxhSq6-Op8s5ljJSqeJL-vCLyiGFjv_eoHxsq6sOH8rqjC0cGsqQJED65wh0XQTf7xsepxcRkFvJvlSl9ntFaLh-IlAmbGN6tKhCbduaYuW6ovupb0UczbmzClMQrYQuoXFgkn2BA25ew-zKp9B89MjZg4xpaJ5ffbK9WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca2bad7297.mp4?token=onbaGYUnGtH3Djgi9rav0G6SlkV3zJYirA3HyL8AdTk5Yp5E5DilnLLar8V0f2PEPV4gEVZLZFfFjHF77L62Gt7MSjDbVqpNs1ZjYRn1F5tzsybPg8gVrbhhbffvy0A5URjYFs774lVHTN9Jz5j5YfEOz5LehEfYGDxbys-POpxRF3tqvxhSq6-Op8s5ljJSqeJL-vCLyiGFjv_eoHxsq6sOH8rqjC0cGsqQJED65wh0XQTf7xsepxcRkFvJvlSl9ntFaLh-IlAmbGN6tKhCbduaYuW6ovupb0UczbmzClMQrYQuoXFgkn2BA25ew-zKp9B89MjZg4xpaJ5ffbK9WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دید بان اتاق جنگ : من با یه صدای لرزیدن شیشه اتاقم بیدار شدم دوباره خوابیدم  ، بعد نیم ساعت رفتم دم پنجره یهو چشمم به این افتاد
@WarRoom</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/21636" target="_blank">📅 14:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21635">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آکسیوس گزارش داد روزانه حدود
۲۰ تا ۳۰ نفتکش
از مسیر تحت حفاظت آمریکا در تنگه هرمز عبور می‌کنند و حدود
۹ تا ۱۰ میلیون بشکه نفت
جابه‌جا می‌شود؛ نزدیک به نیمی از صادرات پیش از جنگ. امارات، بحرین و کویت به این مسیر پیوسته‌اند و عربستان و قطر نیز ممکن است به آن ملحق شوند. آمریکا قصد دارد با
افزایش عرض کانال اصلی کشتیرانی تا اواسط سپتامبر
، امکان عبور حداقل
۵۰ کشتی در هر شب
را فراهم کند و در نهایت
۶۰ تا ۷۰ درصد صادرات نفت پیش از جنگ
را احیا کند. آکسیوس همچنین گزارش داد حدود ۲ درصد کشتی‌های عبوری ماه گذشته مورد اصابت قرار گرفته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/21635" target="_blank">📅 14:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21634">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ed644e27.mp4?token=hkdNeKflQgML9Ag4i0OOIj1VD7oXUJgaXh1BJQ_mAe8nJrlF0cCd2OOXWzv1a1_uPsZl_ASb3HxxBrWL6xPwVloHB-rnzNtjFZMVUHNIu5fNHHONMF7rKdKbdqeaOHPbRIIy0H2MNmMon-WAr-NHDvL1mTWNvsHurBo3qwgtN-OuzcgloEGOjXEu8_tACGr9qEP951KDFvYcnrz53DfmuL1ehJqSFom6RE8dsF6gJTnC-EYYs7mHHSwUEuHsbzrddkNuKilft-dDxoTgf-WOzXSek8TFwwWJoK7_V0oCinzD-FOgOTSnfZ9o4q7yhGsAQ4b6bqeib7K4uqiLCDjwNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ed644e27.mp4?token=hkdNeKflQgML9Ag4i0OOIj1VD7oXUJgaXh1BJQ_mAe8nJrlF0cCd2OOXWzv1a1_uPsZl_ASb3HxxBrWL6xPwVloHB-rnzNtjFZMVUHNIu5fNHHONMF7rKdKbdqeaOHPbRIIy0H2MNmMon-WAr-NHDvL1mTWNvsHurBo3qwgtN-OuzcgloEGOjXEu8_tACGr9qEP951KDFvYcnrz53DfmuL1ehJqSFom6RE8dsF6gJTnC-EYYs7mHHSwUEuHsbzrddkNuKilft-dDxoTgf-WOzXSek8TFwwWJoK7_V0oCinzD-FOgOTSnfZ9o4q7yhGsAQ4b6bqeib7K4uqiLCDjwNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صف پمپ بنزین پشت زندان رجایی کرج , ساعت ۲ ظهر امروز جمعه
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21634" target="_blank">📅 14:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21633">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نیویورک پست: پسر ترامپ، زندگی منزوی را سپری می‌کند، در حالی که با تهدیدات از سوی ایران و تلاش‌های برای ترور پدرش روبرو است. او به شدت تحت تأثیر ترور چارلی کرک، فعال محافظه‌کار نزدیک به او، قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21633" target="_blank">📅 14:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21632">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پروفسور جان مرشایمر، استاد علوم سیاسی دانشگاه شیکاگو : وقتی فشار اقتصادی یک کشور را تا مرز فروپاشی می‌برد، معمولاً آن کشور تسلیم نمی‌شود، بلکه برای بقا واکنش نشان می‌دهد و دست به حمله می‌زند. مرشایمر با اشاره به حمله ژاپن به پرل هاربر در سال ۱۹۴۱ گفت فشار اقتصادی شدید آمریکا علیه ژاپن و قطع دسترسی این کشور به نفت، در نهایت به واکنش نظامی ژاپن منجر شد.
او درباره ایران نیز گفت اگر تهران احساس کند بقایش در خطر است، به آمریکا و متحدانش پاسخ می دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21632" target="_blank">📅 13:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21631">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آکسیوس گزارش داد آمریکا در نبرد بر سر تنگه هرمز به‌تدریج دست بالا را پیدا کرده است. بر اساس این گزارش، نیروهای آمریکایی با هدایت و حفاظت از کشتی‌های تجاری، عبور نفتکش‌ها از مسیر جنوبی تنگه را دوباره برقرار کرده‌اند و مقام‌های آمریکایی می‌گویند کنترل عملی این مسیر اکنون در اختیار آنهاست. اگرچه حجم تردد و صادرات نفت هنوز به سطح پیش از جنگ نرسیده، اما نفوذ ایران بر رفت‌وآمد دریایی در هرمز نسبت به ماه‌های گذشته کاهش یافته است.
@WarRoom</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/21631" target="_blank">📅 13:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21630">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وزارت امور خارجه رژیم :
تمام کشورها موظف هستند از اعمال تحریم‌های یک‌جانبه توسط ایالات متحده خودداری کنند، و تحریم‌های اقتصادی ایالات متحده علیه ایران غیرقانونی و فاقد هرگونه مبنا هستند.
@WarRoom
یاشار : بابا شما که قوی هستین چرا ترسیدین ، تحریم هم که برکته
🥴</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/21630" target="_blank">📅 13:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21629">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ در مصاحبه با شبکه 12 اسرائیل: این موضوع «تنگه» هنوز باز است.
واکنش ایران بسیار ملایم بوده است. آنها نمی‌خواهند ما دوباره به آنها حمله کنیم، این تمام ماجراست. بقیه چیزها مهم نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/21629" target="_blank">📅 13:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21628">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بلومبرگ : قطر در ادامه اختلالات ناشی از بحران تنگه هرمز، وضعیت «قوه قاهره»(حفاظت حقوقی و قراردادی در شرایط اضطراری) برای تحویل گاز طبیعی مایع (LNG) به مشتریان آسیایی و اروپایی را تمدید کرده است. این تصمیم به‌دلیل ادامه محدودیت‌ها و ناامنی در تردد کشتی‌ها از تنگه هرمز اتخاذ شده و بازگشت صادرات گاز قطر به سطح عادی را به تأخیر می‌اندازد. قطر پیش از جنگ یکی از بزرگ‌ترین صادرکنندگان LNG جهان بود و اختلال در صادرات آن، فشار بیشتری بر بازار جهانی گاز، به‌ویژه در آستانه فصل زمستان، وارد کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21628" target="_blank">📅 12:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21627">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گزارش‌ها از سوریه: نیروهای ارتش اسرائیل (IDF) با آتش سنگین به منطقه تپه بت‌ال‌ورده، نزدیک به شهر بیت‌جان در مناطق روستایی غربی دمشق، شلیک کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/21627" target="_blank">📅 12:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21626">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نرخ دلار ۲۰۱،۵۰۰ تومان
دلار کف بازار  ۲۰۰-۲۰۵ هزار تومان
تتر ۲۰۰،۰۰۰ تومان
بیتکوین ۷۹،۷۸۰ $
انس جهانی طلا ۴،۶۰۹ $
نفت برنت  ۸۸،۰۸$
@WarRoom
۱۲ ظهر تهران</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/21626" target="_blank">📅 12:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21625">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">فری استایل یاس به همراه من (یاشار رپفا)
۲۰ سال پیش و زمانه همچنان بی رحم است…
@WarRoom
@RapFA
✅</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/21625" target="_blank">📅 11:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21624">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgsezGJ-ifgQ8M7X5vPbDIRzOGc7r1nJ5VCYYvkkxqZxCe2Ibcvss9MtoijPyEdvEGb303kmAq1dfRgbzf-4vqPL5XPHrQxJja0V1hXIN9uCw_oxPwXxVPHgZ37AnXCYoSsAhpW9NgDOTmuOdSvfuCQm8frcwLYtXSlg-rgxK76Q1LgycV328dQFO3mJC7iKF8NqADvTNESm-1BlPu86WOfHg87_uexLJteIT2ndv4Flk-Qwausw9onsXI4Do7pJT0AfCHmxrkqi8d7tTovYGA3LbwO0Xx91e8LbE_lyquyXIoGJlQ_vrPHtnrlaqe-20NADnyMrbH-irfXPTT0wgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی از دیدبان اتاق جنگ : کاری با دست خط ندارم سطح سواد عرزشی جماعت که برای ۹۰ میلیون نسخه میپیچن (اسرائیل)
@WarRoom</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/21624" target="_blank">📅 11:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21623">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آغاز واریز سود سهام عدالت:
سبد ۴۵۲ هزار تومانی: ۴۴۳ هزار تومان(۲.۲۰$)
سبد ۵۳۲ هزار تومانی: ۵۲۱ هزار تومان(۲.۵۹$)
سبد یک میلیون تومانی: ۹۸۱ هزار تومان(۴.۸۷$)
@WarRoom</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/21623" target="_blank">📅 11:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21622">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wnj-P-D4MIcpRs_MkfeVy7g-eVUE5zer0ELDuPQkrUTJ4Lugou8Gnvtt1x-GHIlPcNsDtWPNyFjpZAhtvEqzgmE2w0WN8o0eRO6t_7-d6hh4n5HlkfHQkJ_7dC63amPqI5VyuNNx9DhKDQlO-nOXxnt1yAF91S5dEzgQJcbhfXiRRCp1SR6jobLF10jmeWB6jyp7jR-xow4yrN397CqwGxL7pg_aAA6JBsdpaDFM4R5AZ1NXSbnxtEc6KxnCrZV--robVcpWIefICTXpBmKrfOQ0YAZHAzZID5rtWPnQRGYLiZ7Y_pH5cMT2FrilIUlWlehWOneg4wd7W11fMQf6bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث دوباره:  تنگه هرمز در حال حاضر قلمرو جدید آمریکاست
@WarRoom</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/21622" target="_blank">📅 11:07 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21621">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_we-VR_aPw5WH1Ax8V9wPLUhxRf-lNvvwdCT_oxPscdYNH7lm8ZSr9Hp98LuLjbUn9jYuf-skej0PCU47qGtoJt1xuqfe_Ce4vSe7epuAN2QhjK6XMIYFCn6q1SxAVClNhIRO3a5IO-qh-wqwXER2vFcLFLwjW42LI5WDJAIp6xoBRK-nBBadK_NfDjOeaQtG_B9ZfGtGHlSaT19IMxJBjkvwxOQDY2gRLNN7CZPq8BL_dW86-fFNxRAGWxx8HGVmMcmgkrdKYK_AcLfu6MfRDHuM5LutWpD6OYKG96yIWZNquJcmAxSg1mheD0lVoUlIb1GExuNPDMe1Stz6BrYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هارالد پنجم، پادشاه نروژ و مسن‌ترین پادشاهِ در حال سلطنت اروپا، در ۸۹سالگی در بیمارستان دانشگاهی اسلو درگذشت. کاخ سلطنتی اعلام کرد او صبح امروز جمعه ۲۸ اوت، ساعت ۶:۳۵ به وقت محلی، درگذشت. هارالد از ۱۹۹۱ پادشاه نروژ بود و بیش از ۳۵ سال بر این کشور سلطنت کرد. او به‌دلیل کم‌خونی همولیتیک تحت درمان بود و پس از ابتلا به یک عفونت باکتریایی در خون، وضعیتش به‌شدت وخیم شد. پسرش، ولیعهد هاکون ۵۳ ساله، اکنون پادشاه جدید نروژ شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/21621" target="_blank">📅 10:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21620">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دریاسالار برد کوپر، فرمانده ستاد فرماندهی مرکزی آمریکا (سنتکام)، مدعی شد نیروهای آمریکایی از زمان آغاز محاصره بنادر ایران، عبور حدود
۱٬۵۰۰ کشتی تجاری
و انتقال
۷۵۰ میلیون بشکه نفت خام
از تنگه هرمز را تسهیل کرده‌اند، در حالی که به گفته او، ایران اجازه صادرات حتی یک بشکه نفت خام را نداشته است.
کوپر همچنین مدعی شد هیچ کشتی ایرانی بدون اجازه سنتکام وارد یا از بنادر ایران خارج نشده و تنها در موارد بشردوستانه اجازه تردد داده شده است. به گفته او، تاکنون حدود
۷۵ کشتی تغییر مسیر داده شده
و
۳ کشتی
از زمان آغاز محاصره بنادر ایران از کار انداخته شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/21620" target="_blank">📅 10:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21619">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
«محاصره و عملیات “
طرد اقتصادی
” اقتصاد ایران در حال فروپاشی l را درهم خواهد شکست. آمریکا طی ۱۴ روز گذشته با مدیریت خود
۱۳۰ میلیون بشکه نفت
را هدایت و منتقل کرده است.
ایران: صفر.
@WarRoom</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/21619" target="_blank">📅 10:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21618">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxZubeuqeXL5t7WM12lSAl8wlTQFg7u4HVBSGyiDmdZc-NC6Q3LCk7mi-qX8IUav94i6WlwVh3MHCJ9PnZaydhITRp2aqX9IATCzsabhn9bbmGwiPrNrl8QmsiCyNSp1RV7x4Q1cXFIzu_dXn3W7J2RsWg5vk_6gffrM6ElGzhh2iGlECeWlPZiZM7HNkm_jWdvdpUiPoU5HSMsz0IBY-tzlzp41HUdldQ10pZ2ytw6yQt5-Vto69eSvN1NqwhQP_kSmLjjDPkawFCtAFitFNnWWriPgIsZh4i97vfxVnG8xfCN6NoE0JGvueWErQSqb5mA2QlwbiuyE9xCxSU5Y5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ با انتقاد شدید از گزارش جاناتان هانت، خبرنگار فاکس‌نیوز، آن را «بسیار نادرست» خواند و گفت: «من نمی‌خواهم با ایران دیدار کنم؛ آنها هستند که می‌خواهند و برای توافق التماس می‌کنند.» به نظر می‌رسد این یک سوءتفاهم باشد چون هانت در گزارش خود گفته بود مذاکرات مستقیم میان آمریکا و ایران فعلاً در جریان نیست و دولت ترامپ به‌جای مذاکره، در حال تشدید فشار اقتصادی و تحریم‌هاست؛ هم‌زمان کشورهای عربی، از جمله قطر، برای گرفتن امتیاز از تهران تلاش می‌کنند. ترامپ در ادامه از برت بایر، مجری فاکس‌نیوز، خواست «زیردستان بی‌کفایت خود را سر و سامان دهد». بایر نیز در واکنش گفت هانت «خبرنگاری عالی» است و تأکید کرد فاکس‌نیوز اصلاً نگفته ترامپ خواهان دیدار با ایران است، بلکه برعکس، در گزارش به صراحت گفته شده بود ترامپ نمی‌خواهد دیداری انجام شود و مذاکراتی در جریان نیس
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21618" target="_blank">📅 10:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21617">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سازمان عملیات دریایی بریتانیا بامداد پنجشنبه گفت که یک نفتکش در آب‌های نزدیک منطقه «الخصاب» در شمال عمان، مورد اصابت یک پرتابه نامشخص قرار گرفته که باعث آتش‌سوزی در آن شد. @WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21617" target="_blank">📅 09:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21616">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqAunymUuAmqLUeBrGu9BFPToQwE_xe4gkNVnF1aorEiR3TtM4GjS71TWsI3gL1nsFzKvbrvE-SpJSop6E5Ua4VEheFU3_Adr6Mjo2HHAsgyFswq8ZtiBn82dw58TGUafLrH3d84VweuSKMQz-UVteqlF2E2FHz35PBX3ybjuQd_rq4bU661BNpPRfC4vnjBVvzuuuFJzk9x3hKRSQC5GAMQx3-cecw-tHt20pSDpweY2uUqhpJrA_Ld9o2HT-jDX2YC0q5z2GwIleaevDm_WKpokAAH2hEbs658q0Cq3W8GApqiCDyxw-YakSNO_PPt3J52SPpLhHpwdlpaQfaurg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایران کشوری رو به فروپاشی است
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21616" target="_blank">📅 09:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21615">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGgL5rUc1SZ_mP2JOLUQWsNO2RfVLwYZP7Et0gmzGmpLithUvMB3XdFcM3yRNVtGOFfbNe4-fautZoV8d0U4hqHE28ufMP8Y3bQu6V8eO9Pf6oZaboeelRimGqvhA7T3DVE40AUcfpT5fir8t9EgzgWWWW-049osOX4jVXZ9cxX5N70LxS4Hmr7tGz2A7JM3kHvFCCFkLdenW070wW9ctDAir2Lx-j3I21DrdnJNkHv1e62nFh-KDd1-yfUjoyMYZP9ItlU18ZPzsCW2I070Rp8ThKXsHvkeW3Oyn5TGm4pO6yoi224b3Yxwvgbi6WGCA7v-0GRLJpRPT3BfsKR8lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶ سوخترسان آمریکایی و ۲ پهپاد در خلیج فارس در حال مأموریت هستند ، بعد از مدتها این حجم مشاهده میشه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21615" target="_blank">📅 00:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21614">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d6860a3c4.mp4?token=bHOhEcerCQjB2R6e9PuA847XmoZ0yoveezFqP9PGZOjHlBAE6MUXVgEBo4BT83LuwmvwtXQUtqiJyrBvS-1utfQgMsszz9lNnUvEX1W7w5qO4notHBy3sE7KxRyWvGP8f-s-EY4mnhVawv2TQDrwhQgr9KJuVz42wSoEQ7WHbd-j9OzPXow-we2zpY_nONmiPI2fceIYjbecHqCEofqVvh3nq_iwGjhcJkI9XenWyH5xyW0XG7v1RuAwkrU3-KxgdUx-Vv0abhhamszDMTQYmiuHdSJZrT4SIEmTf_ktpgGP1W2LX-psHBt5-8yu2KmCC1ugx-0a3kbQ11a2LmyaRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d6860a3c4.mp4?token=bHOhEcerCQjB2R6e9PuA847XmoZ0yoveezFqP9PGZOjHlBAE6MUXVgEBo4BT83LuwmvwtXQUtqiJyrBvS-1utfQgMsszz9lNnUvEX1W7w5qO4notHBy3sE7KxRyWvGP8f-s-EY4mnhVawv2TQDrwhQgr9KJuVz42wSoEQ7WHbd-j9OzPXow-we2zpY_nONmiPI2fceIYjbecHqCEofqVvh3nq_iwGjhcJkI9XenWyH5xyW0XG7v1RuAwkrU3-KxgdUx-Vv0abhhamszDMTQYmiuHdSJZrT4SIEmTf_ktpgGP1W2LX-psHBt5-8yu2KmCC1ugx-0a3kbQ11a2LmyaRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : هر کسی میخواد برقش قطع نشه میتونه از بورس برق با قیمت آزاد خریداری کنه.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21614" target="_blank">📅 23:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21613">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">محسن کج بند رضایی، دبیر شورای امنیت ملی، ادعای وجود توطئه ایران برای ترور پسر دونالد ترامپ را «دروغی بزرگ» دانست و گفت این ادعا ساخته بنیامین نتانیاهو برای فریب و ترساندن رئیس‌جمهور آمریکا است. او مدعی شد نتانیاهو با انتشار گزارش‌های جعلی درباره «توطئه ترور ترامپ» او را ترسانده و بر تصمیم‌گیری‌هایش اثر گذاشته است. رضایی افزود: «اگر تصمیمی بگیریم، هیچ‌چیز مانع اجرای آن نخواهد شد؛ اما این گزارش‌ها صرفاً یاوه‌گویی‌های نتانیاهو هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21613" target="_blank">📅 23:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21612">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دیوید بارنیا، رئیس پیشین سازمان اطلاعات خارجی اسرائیل «موساد»، می‌گوید جمهوری اسلامی در نهایت در اثر ترکیبی از فشارهای اقتصادی، عملیات علیه حکومت، و اعتراضات مردم ایران سقوط خواهد کرد، و تحریم‌ها به تنهایی برای رسیدن به این هدف کافی نیستند.
@WarRoom
🚨
🚨
🚨
حتما چنل رو دنبال کرده
🤣
🙌🏾</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21612" target="_blank">📅 22:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21610">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گزارش پرتاب موشک زد کشتی از سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21610" target="_blank">📅 21:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21609">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وال‌استریت ژورنال گزارش داده است که دونالد ترامپ با بازگشت به چارچوب اولیه توافق ژوئن با ایران مخالفت کرده و ترجیح می‌دهد با تشدید فشار اقتصادی و تحریم‌ها، تهران را به دادن امتیاز وادار کند. در مقابل، ایران تأکید دارد که بازگشایی تنگه هرمز باید بر اساس همان چارچوب ژوئن انجام شود؛ چارچوبی که شامل کاهش تحریم‌ها و محدود شدن فشارهای آمریکا بود. پاکستان، عمان و قطر نیز برای میانجیگری و نزدیک کردن دو طرف تلاش کرده‌اند، اما مذاکرات تاکنون پیشرفت چندانی نداشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21609" target="_blank">📅 21:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21608">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ به شوخی می‌گوید:
ما یک خلیج(مکزیک که شد آمریکا) داریم. ما یک دریاچه(انتاریو که شد آمریکا) داریم. حالا چیزی که نیاز داریم یک اقیانوس است.
بنابراین شاید مجبور شویم نام اقیانوس اطلس یا اقیانوس آرام را تغییر دهیم.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21608" target="_blank">📅 21:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21607">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خبرنگار: با کدام رهبران در مورد قطع روابط با ایران صحبت کرده‌اید؟
ترامپ: چیز زیادی برای صحبت وجود ندارد. ما نمی‌خواهیم با آنها صحبت کنیم. تنگه هرمز باز است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21607" target="_blank">📅 21:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21606">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ: ایران در وضعیت بسیار دشواری قرار دارد و نمی‌تواند حقوق سربازان خود را پرداخت کند.
اقداماتی که ما در مورد ایران انجام می‌دهیم، به این معنا نیست که ما از گزینه نظامی چشم‌پوشی کرده‌ایم.
ما نمی‌خواهیم با ایران صحبت کنیم و قصد نداریم جلسه‌ای با آن برگزار کنیم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21606" target="_blank">📅 21:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21605">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">شرکت روکِتسان ترکیه موشک کروز «چاکیر» را با موفقیت از یک پرتابگر زمینی آزمایش کرد
. این آزمایش نشان داد چاکیر علاوه بر پهپاد و دیگر سکوها، قابلیت شلیک از خودروهای زمینی را نیز دارد و می‌تواند اهداف زمینی و دریایی را با جستجوگر تصویربرداری مادون‌قرمز هدف قرار دهد. برد این موشک بیش از ۱۵۰ کیلومتر اعلام شده است.
جنرال یاشار گولر، وزیر دفاع ملی ترکیه،
نیز درباره تسلیحات جدید روکِتسان گفته است: «ما این سلاح‌ها را عمدتاً برای بازدارندگی می‌خواهیم، اما اگر استفاده از آنها لازم باشد، ترکیه بدون تردید از آنها استفاده خواهد کرد.»
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21605" target="_blank">📅 21:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21604">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ: هیچ نگرانی‌ای از حمله روسیه به ناتو ندارم
دونالد ترامپ در گفت‌وگو با آکسیوس گفت که «اصلاً نگران» حمله احتمالی روسیه به کشورهای عضو ناتو نیست و تأکید کرد: «هیچ مشکلی وجود ندارد.» او همچنین گزارش‌ها درباره سفر محرمانه جان رتکلیف، رئیس سیا، به مسکو برای هشدار به روسیه درباره حمله به اعضای ناتو را رد کرد و گفت این سفر «یک کار معمول» بوده و «هیچ پیامی در کار نبوده و هیچ چیز غیرعادی‌ای» رخ نداده است. با این حال، گزارش‌هایی از جمله گزارش وال‌استریت ژورنال و CBS مدعی‌اند که رتکلیف در مسکو به روسیه درباره حمله به ناتو هشدار داده است؛ موضوعی که تاکنون از سوی مقام‌های آمریکایی یا روسی به‌طور رسمی تأیید نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21604" target="_blank">📅 20:55 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
