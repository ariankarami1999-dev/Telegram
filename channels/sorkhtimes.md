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
<img src="https://cdn4.telesco.pe/file/hthAthw_kPeEEk0EXkbbBPu8b6osLTkGOYeA5HuBaHf_hDrayCeVvCagfClVPrV701y7_LUYgjwcc8UMn13TMRYINaT8FcEsvenOR2rsCIAht54T-CCsiNAm7x0kIqwZdYNLo2TlNZ0VUIY4e0noHWh5Fq7Dd_CFI1x-W4S2JECmprFuemG5GNF24YiGO5Joi7UVO1KslZ9xx2ajYmt1Gs1ZT29sLlyf8NqE7J2Nz4xJGMNG7HL3rP1EDa5yw28D0tg8rXcb94Jt6lZ_KXYDL9Q4F_FtoniYFG4OxnlRxMOWJSXBZsCPwe6p1SooZjtFqfwnlLMPFR0fOtAuEHB6mg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 23:26:33</div>
<hr>

<div class="tg-post" id="msg-135712">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» حدادی شخصا میخاد با امید عالیشا،میلاد سراک،رضا شکاری،مرتضی پورعلی گنجی،دنیل گرا و تیوی بیفوما فسخ کنه.
❌
حالا باید ببینیم بانک شهر برای فسخ و آوردن بازیکن جایگزین بودجه میده یا نه
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SorkhTimes/135712" target="_blank">📅 22:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135711">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzWwYx6HT3UqFHOn6rt--F-Oxs__rQ6KMR7zFa-poPi606mM-RDD4jgq_y2qpDNgellEsodQjf3Y-nVTICETyrDEQvY1Bhda3YcC738Ae4a1NCK-erWUhfLqJk_6yHbxjd-gqC-Mxn1jo-NL0JMqzcHGXu_z3iNNDUpOGluDR90YONK7QxAvGSKAHkcDjJyeipab7njSW-SoEnvfzrvsDtv2Sihdn34SAaW7w34LU9ezBU0aEPaYgbS-YSWZtrHMV5YTYfKTmcmTTqBMbKlZXiMNF5MuAHKENjElFiMszKzsYRIlnqeg0wE8tQcp0NQ44gmUlHdUAzPTRFV0-RI4Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
تارتار در بازی دوستانه امروز به همه بازیکنان فرصت بازی داده حتی وحید امیری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SorkhTimes/135711" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135710">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔹
احتمالأ پوریا پورعلی امشب رونمایی میشه ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/135710" target="_blank">📅 22:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135709">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
#فوری | نیروی دریایی آمریکا اعلام کرد که محاصره تمامی بنادر ایران از فردا، در ساعت ۲۰:۰۰ به وقت گرینویچ آغاز خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/135709" target="_blank">📅 21:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135708">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
#فوری | نیروی دریایی آمریکا اعلام کرد که محاصره تمامی بنادر ایران از فردا، در ساعت ۲۰:۰۰ به وقت گرینویچ آغاز خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/135708" target="_blank">📅 21:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135707">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
#فوری | نیروی دریایی آمریکا اعلام کرد که محاصره تمامی بنادر ایران از فردا، در ساعت ۲۰:۰۰ به وقت گرینویچ آغاز خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/135707" target="_blank">📅 21:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135706">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
فوری ترامپ:
❌
امشب ما مهمانی بسیار ویژه خواهیم داشت که در حملات ما به ایران شرکت خواهد داشت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/135706" target="_blank">📅 21:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135705">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
✅
علی علیپور و میلاد محمدی امروز هم برای تمدید قرارداد خبری به باشگاه پرسپولیس ندادن. پیمان حدادی دیشب گفت که این دو بازیکن فقط تا امروز وقت دارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/135705" target="_blank">📅 21:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135704">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
🔴
دنیل گرا با نظر تارتار در لیست مازاد تیم قرار گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/135704" target="_blank">📅 21:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135703">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
ترانسفر مارکت: رضا شکاری از پرسپولیس جدا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/135703" target="_blank">📅 21:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135702">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/135702" target="_blank">📅 20:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135701">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔽
پورعلی داره می‌ره باشگاه برای معارفه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/135701" target="_blank">📅 20:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135700">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
🔴
🔴
🔴
🔴
🔴</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/135700" target="_blank">📅 20:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135699">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
🔴
🔴
🔴
🔴
🔴</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/135699" target="_blank">📅 20:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135698">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
رفقا این فرمو میتونید سنگین بزنید
🔥
🔥
تخصصی ترین چنل شرطبندی تلگرام
‼️
#VIP
#رایگان</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/135698" target="_blank">📅 20:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135697">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dc-4_tS4bN-eImaLRrGurhngb7pAK9STMIOgveDWJCU2JvEQ7UtL8wyNSeVOKY08UWE3esVjdmf1IYX3Yrp15dzYfC6RsgOb2TvQL2TePrewp3Q4Z2bW1Qi5zIcT8TO8cSG9t-ByfY_vFbqsUrjNefl3yjKdYoP5Op10vXTDMOkoT-bRpaZQAuBkzdb0dscoZyp26AH5p2j9Tv_UvmH_gRPgJQKFJVZoNWQLZaW7D5cHUN_vdZ7OgS1Dih39ZO2JJbkbK0ohuPDUPQHbt2EsuvSvbvsAqvKJQOzvxoMRuDy31VLSCLWqWYsywVqC4FYvFJIL9__zuh_2HY9gGIow6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
فرم VIP از بازی اول نیمه نهایی
🏆
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
باضریب
⬅️
4.38
📊
گذاشتم
اینجا
حتما استفاده کنید
💎
شروع فرم ساعت
🔢
🔢
⬇️
👇
⬇️
⚽️
برای دریافت کلیک کنید
🤩
🤩
رفقااینجا عضو بشین تا شما هم سود کردنو یاد بگیرین
👇
https://t.me/+wuaT6FTz8iViNmU0
◀️
https://t.me/+wuaT6FTz8iViNmU0
◀️
💎
💯
100درصد وینه
💯
💎</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/135697" target="_blank">📅 20:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135696">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⚽️
👤
سوپرگل سامان قدوس به عجمان در جریان بازی اتحاد کلبا و عجمان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/135696" target="_blank">📅 20:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135695">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❗️
فوری؛ قرارداد رضا غندی پور با شباب الاهلی با توافق دو طرفه فسخ شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/135695" target="_blank">📅 20:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135694">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❗️
پایان نیمه اول با برتری ۲ بر صفر
❌
گلزنان: محمد عمری، مهدی تیکدری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/135694" target="_blank">📅 20:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135693">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
🚨
#فوری | ترامپ: امشب به طرز ویران کننده ای به ایران ضربه می‌زنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/135693" target="_blank">📅 19:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135692">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
❗️
قرمز آنلاین: با تاکید و پافشاری تارتار آقا کریم موندنی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/135692" target="_blank">📅 19:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135691">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
یاسر آسانی قرارداد شو با استقلال فسخ و ایران رو ترک کرد / فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/135691" target="_blank">📅 19:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135690">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گل اول پرسپولیس توسط محمد عمری
⬇️
⬇️
⬇️
https://t.me/+sCs-XrTYp8ZlN2Zk
https://t.me/+sCs-XrTYp8ZlN2Zk</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/135690" target="_blank">📅 19:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135689">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
ترکیب پرسپولیس تو بازی دوستانه امروز
▪️
پیام نیازمند
▪️
حسین ابرقویی
▪️
حسین کنعانی
▪️
ابوالفضل جلالی
▪️
مجید عیدی
▪️
محمد خدابنده‌لو
▪️
مارکو باکیچ
▪️
مهدی تیکدری
▪️
محمد عمری
▪️
امیرحسین محمودی
▪️
محمد امین کاظمیان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/135689" target="_blank">📅 19:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135688">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
نخستین بازی سرخپوشان برای فصل جدید
🔴
تیم فوتبال پرسپولیس در نخستین بازی دوستانه خود برای فصل جدید فوتبال در دیداری دوستانه به میدان خواهد رفت.
🔴
به گزارش سایت رسمی باشگاه پرسپولیس، سرخپوشان ایران، فردا(دوشنبه) برای نخستین بار و در دیداری تدارکاتی با هدایت…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/135688" target="_blank">📅 18:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135687">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❗️
مهدی تارتار از مدیران پرسپولیس درخواست کرده با توجه به شانس کم پرسپولیس برای جذب ایری و زارع،اقدام به بازگرداندن مرتضی پورعلی‌گنجی به تمرینات تیم کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/135687" target="_blank">📅 17:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135686">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❗️
به پورعلی گنجی اطلاع دادن تا تعیین تکلیف خط دفاع پرسپولیس منتظر بمونه احتمال داره اگه نتونستن دفاعی جذب کنه برگرده
🔴
تنها شانس باقی مانده پرسپولیس مهدی زارع است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/135686" target="_blank">📅 17:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135685">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
قدوسی: مذاکرات با احمد نوراللهی در حال انجام است و مدیران باشگاه در تلاش هستند این بازیکن رو به پرسپولیس برگردونن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/135685" target="_blank">📅 17:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135684">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❗️
به پورعلی گنجی اطلاع دادن تا تعیین تکلیف خط دفاع پرسپولیس منتظر بمونه احتمال داره اگه نتونستن دفاعی جذب کنه برگرده
🔴
تنها شانس باقی مانده پرسپولیس مهدی زارع است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/135684" target="_blank">📅 17:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135683">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❗️
به پورعلی گنجی اطلاع دادن تا تعیین تکلیف خط دفاع پرسپولیس منتظر بمونه احتمال داره اگه نتونستن دفاعی جذب کنه برگرده
🔴
تنها شانس باقی مانده پرسپولیس مهدی زارع است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/135683" target="_blank">📅 17:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135682">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❗️
پیمان حدادی : ما به میلاد محمدی پیشنهادمونو دادیم فردا آخرین فرصته که قرارداد رو امضا کنه اگه نکنه از لیست تیم خارج میشه این پرسپولیسه که واس بازیکن تعیین تکلیف میکنه نه بالعکس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/135682" target="_blank">📅 16:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135681">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
عجب بابا عجب
😐
🚨
🚨
🚨
تسنیم: باشگاه نساجی مازندران رضایت نامه دانیال ایری رو گرون کرده و به ۱۹۰ میلیارد تومن افزایش داده!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/135681" target="_blank">📅 16:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135680">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
رضا جباری به کادر مهدی تارتار اضافه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/135680" target="_blank">📅 16:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135679">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
پیمان حدادی : صحبت از مهدی ترابی، دانیال اسماعیلی فر، آریا یوسفی، رامین رضاییانه آیا تیم رقیبمون به ما بازیکن میده وقتی قرارداد دارن؟
✅
مثل اینه من اورونوف رو به اون تیما بدم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/135679" target="_blank">📅 15:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135678">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
زندی:تیمی در حد قهرمانی بستیم.
🎙
برای خرید محمدجواد حسین‌نژاد با باشگاهش‌ به‌ توافق رسیدیم که روی مبلغ ۱.۸ میلیون‌ دلار این‌ بازیکن را جذب کنیم اما خودِ بازیکن حاضر به امضای قرارداد با ما نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/135678" target="_blank">📅 15:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135677">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2T3ao3YIQw_d2SjLdyiiNN7F2L1xqCGncHDETPCTh9bVb8nKjET1SOQn4llWD7msCZWAiS3spSFJe9cENjqHD_fB5TQp2EdWkOP8V5Yk4qn7s1R2jGl24TkaNNKO6KweevyCMpAvCl26cbmyCtevSUwnPoqi4JsKrk6LyZ3d7qiHIb06l4CShhjSbz-_tB81qwXl88SU4R5sNj6hzxOpF98-vIm_BuroxydMqM1uBSiWNAPFZfWPXbR2FnOI1tvNOWmMKr5aPglYmZ-3pdmA94p0AqQMOl7Ad-zj-93h8owcso-pRdrpndLOqY2wyjVsbMxovvs1iWvDzr_hS_Qvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیژن مرتضوی، خواننده و آهنگساز ایرانی مقیم آمریکا، با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/135677" target="_blank">📅 15:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135676">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135676" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/135676" target="_blank">📅 15:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135675">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
🆕
معرفی سایت و اپلیکیشن مل‌بت
🆓
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/135675" target="_blank">📅 15:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135673">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
عجب بابا عجب
😐
🚨
🚨
🚨
تسنیم: باشگاه نساجی مازندران رضایت نامه دانیال ایری رو گرون کرده و به ۱۹۰ میلیارد تومن افزایش داده!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/135673" target="_blank">📅 15:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135672">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mwGVrqir6hrPczyLMEe24nDvM2JAMCbzR8dRqgFpvTWpSxDa1X_VXvDXboFODOKWBLCFAp-uxVzE4zfGF1Fpt-j6AeHrLUSJVR4Tv2IK82fUCdBE35YkWczUjltvyHpyun0yUiAf-l2V4LolzmcNfPFdn_XkNqIAayrJJHKMMA5VO4boLLFugyprPhN0ih4GRDUbxrzSAXICisMj5nILKiWMRAK23uTd6HY73I0ShyWcKKJeub2KXh-nWpW3CqVd3Ir0Xb456bUI3X7HulSrdGkBJmvOpjCYePrJqFRZAoLqgfu80KEPz5Ght2Ho223P9QdH6dOCNuvZy7gdP-FPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
به پورعلی گنجی اطلاع دادن تا تعیین تکلیف خط دفاع پرسپولیس منتظر بمونه احتمال داره اگه نتونستن دفاعی جذب کنه برگرده
🔴
تنها شانس باقی مانده پرسپولیس مهدی زارع است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/135672" target="_blank">📅 15:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135671">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
شهاب زندی: دانیال ایری بازیکن ماست و دیگر قابل فروش نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/135671" target="_blank">📅 15:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135670">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❗️
قرارداد علی علیپور تمدید شد
❌
قرارداد علی علیپور، مهاجم باسابقه و ملی‌پوش پرسپولیس، پس از توافق با دکتر پیمان حدادی، مدیرعامل باشگاه، به مدت یک فصل دیگر تمدید شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/135670" target="_blank">📅 15:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135669">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
🚨
فووووووووووووری
⏺
حسین قهار خبرنگار فرهیختگان: پرسپولیس می‌تونه کسری طاهری رو بخره به یک شرط که نساجی با همون مبلغ به پرسپولیس بفروشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/135669" target="_blank">📅 15:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135668">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ia1SdwXllrMKqXbpEQTuSHWTdiuSD8EusgWGqSKdvQEv0a5ION1OCMbW1SI2hXZ34zmylKQ4Flx2q9nKjbXwYl5ALX157ZUJZXuic4HRzLO88nh4fL_9nnVaJLs68LpFMy3R3tr3zGCP5EebC2SNuvAuNBzAbv0QeVaumkD3I7t3on3WcWmO4HpAcNPAofqJZo_UFiwKV2pdcfWApPcat8l2VKpQSH7vbaL_tnV4iHi4ZjqHQr-owpTLmtkK3tHmOYGYMrR3CzixGRinBpbEr8czn8CC6ohg_5j0r3ogw6UHwBJ2sNW7IOTzK33VgDOd9p-AC8XtXOnzXrz3Ml-gOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
قرارداد علی علیپور تمدید شد
❌
قرارداد علی علیپور، مهاجم باسابقه و ملی‌پوش پرسپولیس، پس از توافق با دکتر پیمان حدادی، مدیرعامل باشگاه، به مدت یک فصل دیگر تمدید شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/135668" target="_blank">📅 15:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135667">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
🚨
فووووووووووووری
⏺
حسین قهار خبرنگار فرهیختگان: پرسپولیس می‌تونه کسری طاهری رو بخره به یک شرط که نساجی با همون مبلغ به پرسپولیس بفروشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/135667" target="_blank">📅 14:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135666">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❗️
❗️
حسین قهار خبرنگار فرهیختگان: خداداد عزیزی از انتقال طاهری به نساجی خبر داشت و سوالی که دیشب از کسری طاهری کرد برای به حاشیه بردن پرسپولیس بود. حاشیه ای که با جواب کسری طاهری میتونه سه پنجره نقل و انتقالاتی پرسپولیس رو ببنده
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/135666" target="_blank">📅 14:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135665">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✅
✅
فووووری؛ پیمان حدادی پس از عذرخواهی بابت مصاحبه ای که انجام داد ، موفق شد رضایت علیپور رو بگیره و قرارداد کاپیتان جدید پرسپولیس تمدید شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/135665" target="_blank">📅 14:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135664">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❗️
شنیده ها
🗣
پس از صحبت های تهدید آمیز پیمان حدادی؛ علی علیپور در جلسه امروز با پیمان حدادی شرکت نکرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/135664" target="_blank">📅 14:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135663">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaO_UvSmWtPsetwYjAMbVAGdCglj-YhgfyZZr2J4Y6-lOWbl2tRRyHOJ2Oj3YP2Jy8Tdhkxz1AEsf_EuTDG1TdqQgMqirTSq42pswx3-pT9luntIwlYPQ2Z3fI4a4LNrhZuOcybzJCww8CM3ScUMcDyhOSpiKGS5HOJ012VmM5TrFY_Ta45ufdOcpkADaVUUqvPrB-CWHeDBZhgkg3ZPR2i51hM1SOLxNCMA4Qa0_y-2mJx-acx1H6m_6X0sv2FQ02B4shyBHjDi4PH1DlPpShye3SFSsy3vNf0b_dLzgGPWQ5StNvuZ6azzTb40VFmIfXVs9Gy3l1W5499KUooH-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
علی علیپور مهاجم ۳۰ ساله و ملی‌پوش پرسپولیس بعد از توافق با مدیران این باشگاه، قرارداد خود را با سرخ‌پوشان پایتخت تمدید کرد تا در جمع قرمزها ماندگار شود
.
✍
📝
خبرگزاری ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/135663" target="_blank">📅 13:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135662">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❗️
باشگاه اعلام کرد با کسرا طاهری قراردادی امضا نکرده و هیچ قصدی برای خریدش از نساجی نداره/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/135662" target="_blank">📅 13:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135661">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlcYc_YWYZw6k7m4ZM5iX-ObPMgdBFrN9pAWA9BzbaJg8GDpPT4OF2bn5ajkpDDJpdrJFVvLJD17Icgs-JZn5h2fn8WY9pKj88sHMlaSXCB__mdcf-3NSH57Qq9izsPzlhpEXo6rF4_MLtaeOocxxI98_ENO3t0yvTO9vIyfiOt3hJkTxB3Hot8EbGHIylJiD-m-ILnzwEK8xzu9vGW_8sAVSc5PGkY42j6Oqr7D7fbkzwJqrwrYg7jkoJuKwuZpRAKna7W35IgkEc282F-Ec2u5qjRvmCa1O3R3YPCckg-Q5AeXDfMylBoSSYNJwo_tSOP0FyUjwrCOgBKzNislFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
باشگاه پرسپولیس با تصمیم مهدی تارتار به دنبال خرید مهدی ترابی است. اگرچه ترانسفر مارکت این بازیکن را آزاد و بدون قرارداد اعلام کرده اما باشگاه تراکتور با اطمینان اعلام می‌کند که او قرارداد طولانی مدتی با این باشگاه دارد.
✍
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/135661" target="_blank">📅 13:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135660">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
✅
دوخریدارزشمندنساجی دراین پنجره؛ وقتی مدیر عامل حرفه‌ای و کاربلدداشته‌باشی: برای جذب دانیال ایری و کسری طاهری 200 میلیارد تومان هزینه کرد الان رو هم 450 میلیارد مشتری دست به نقد دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/135660" target="_blank">📅 12:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135659">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❗️
شنیده ها
🗣
پس از صحبت های تهدید آمیز پیمان حدادی؛ علی علیپور در جلسه امروز با پیمان حدادی شرکت نکرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/135659" target="_blank">📅 12:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135658">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✅
✅
باشگاه پرسپولیس اعلام کرد : طاهری کصشعر گفت که فردا پرسپولیسی میشم ما فقط یه توافق شفاهی داشتیم بعد که دیدیم هزینه جذبش کلی ۲۰۰ میلیارد میشه بیخیالش شدیم رفت نساجی
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/135658" target="_blank">📅 11:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135657">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
فووووووووری
🔴
شهاب زندی مدیرعامل نساجی: کسری طاهری به نساجی پیوست. قرارداد ما و او به زودی امضا میشود. او فروشی نخواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/135657" target="_blank">📅 11:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135656">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/135656" target="_blank">📅 11:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135654">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/135654" target="_blank">📅 10:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135653">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
❌
فووووری از تسنیم: باشگاه پرسپولیس به طور کلی قید جذب کسرا طاهری رو زد و این بازیکن رسماً به نساجی مازندران پیوست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/135653" target="_blank">📅 10:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135652">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
بازیکنی رو که می‌شد با ۷۰۰ هزار دلار خرید، الان فقط باید ۱ میلیون و ۲۰۰ هزار دلار به نساجی بدن تا شاید بعد از ۱۶ مسابقه بتونن ازش استفاده کنن! پول بیت‌المال هم کشک ! یک نفر نیست سوال کنه که چطوری و تحت چه مجوزی بابت جذب کسری طاهری باید ۵۰۰ هزار دلار [معادل…</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/135652" target="_blank">📅 09:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135651">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
تصور کنید، پرسپولیس با سابقه چند ده قهرمانی،  از نساجی‌ای هایجک میخوره که هنوز وارد لیگ برتر نشده !
✅
پرسپولیس درواقع از تیمی که هنوز مسابقاتش در لیگ یک[آزادگان] ایران تموم نشده هایجک خورد!!
❌
❌
یک درصد هم این انتقال انجام بشه، از اون انتقال‌هایی است که هر…</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/135651" target="_blank">📅 09:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135650">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❗️
توضیح تکمیلی ِ حقوقی:
❌
اگر از سوی فیفا انتقال کسری طاهری از روبین‌کازان به نساجی، صوری تلقی بشه، دردسر حقوقی بسیار خطرناکی برای کسری‌ طاهری، نساجی و باشگاه پرسپولیس باز خواهد شد و ممکنه ۳ پنجره نقل و انتقالاتی پرسپولیس و نساجی بسته بشه.//خرمی
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/135650" target="_blank">📅 09:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135649">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✅
این قرارداد درصورتی که منعقد بشه، ریسک بالایی داره و یه پرونده حقوقی سختی باز میشه.
🔴
درصورتی که پرسپولیس بخواد کسری طاهری رو برای ابتدای فصل بخره، فیفا قطعا ورود میکنه و پرسپولیس و خود بازیکن باید برن جواب بدن که قصد دور زدن قانون رو داشتن یا نه...
❗️
کلا…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/135649" target="_blank">📅 09:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135648">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗️
ورزش سه: کسری طاهری با عقد قراردادی قرضی از نساجی مازندران به پرسپولیس پیوست
🔴
تفاهم نامه سه جانبه پرسپولیس، طاهری و نساجی امروز امضا شده و طاهری یک فصل قرضی در پرسپولیس بازی می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/135648" target="_blank">📅 09:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135647">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🎬
حمله و توهین زشت بیرانوند به مهدوی‌کیا: بازیکن نسل گذشته تیم ملی تا مکزیک آمد با اینفانتینو عکس گرفت، ولی حاضر نشد به کمپ تیم ملی کشورش بیاید!!
🔴
بیرانوند:  آقای مهدوی‌کیا از چه چیز ترسیدی که به ما سر نزدی؟
🗣️
بعد از بازی با بلژیک کدام یک از اسطوره‌های…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/135647" target="_blank">📅 09:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135646">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/185e8a93ff.mp4?token=cgzdxIhlwG3501wqpxu9-VluiWKDc1aIlbe-DzzA1usFPjM0mHqbH2TixrJxtoF3cczY0Wdnz5iJ4pwaSt_v7Ky3jyu_gDXEeUUiNGmRKIHvE4YoVKQFTkFs7E8B5abFpsn3ZPaphd198GvEMBQheCt1UkY8_v2lbiWGxpGmfN12xG6AKzkeaZxkuxQbQBak56jqFE2X7Dh_RqV-2-8SjHrLCOayeEaK6Sv8aMqXuBME45vFovBw0JQaGLQjvpPGIjbKXSQ3X2AtQ5cY17cduwBaZXP9t3FhwDqNrTAlG6nupD4Lr3klQbrm4z3tEPqFsgqiWQYxH3hvWNbUSfDY9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/185e8a93ff.mp4?token=cgzdxIhlwG3501wqpxu9-VluiWKDc1aIlbe-DzzA1usFPjM0mHqbH2TixrJxtoF3cczY0Wdnz5iJ4pwaSt_v7Ky3jyu_gDXEeUUiNGmRKIHvE4YoVKQFTkFs7E8B5abFpsn3ZPaphd198GvEMBQheCt1UkY8_v2lbiWGxpGmfN12xG6AKzkeaZxkuxQbQBak56jqFE2X7Dh_RqV-2-8SjHrLCOayeEaK6Sv8aMqXuBME45vFovBw0JQaGLQjvpPGIjbKXSQ3X2AtQ5cY17cduwBaZXP9t3FhwDqNrTAlG6nupD4Lr3klQbrm4z3tEPqFsgqiWQYxH3hvWNbUSfDY9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
مهدی تیکدری: دوست دارم هواداران به من لقب تیکی لامبورگینی بدهند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/135646" target="_blank">📅 09:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135645">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFINQuzmnzug0pnSAU9DAYlnE1oFIppScuEBxX-BgXSXHdJ0Fj2u_d14R_JjvqRiM9vHCWBb0OGADLH7QLDjvAM2L22YlBUB6hVC6XkRvYABMP1y_ZTk_hFHmoYLFgUx-sLXKI3pFE-M7-BJ_rTKg1RzrEsySAAsEvLrKKWkJPomwvRjrizzmN2wXwp35v6BRZLL8usgAlxmQuO6oz4HJoenKpeAgKvzn4afS-61gDactRMoOQvHCzRlA7RIu7TbCfopXxLXsOiwdQ33fr71F9JxbXQ52JlsXPmkhQCxItGrynXhtMf9-Y_sz6Xjm48OjWjnnpefoGzz0-0Ey4UaeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اوستون اورونوف چهارشنبه‌ وارد ایران خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/135645" target="_blank">📅 09:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135644">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
دختر بیرانوند : بابام استقلالیه و دوست داره برای استقلال بازی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/135644" target="_blank">📅 09:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135643">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0a6a5812d.mp4?token=nB7dM9IVQdF01QRqRuaHRMEYAVywu4VAbkZnIqeQtMDaa2PGLUywyR0lwRueC7eArZNcnisrJUN9wMeZ49NRuUChkwBu6T7lEauIxpg0tBHHVukNphC0_5mwDb_xquGcXcVWVXy7iflQH2u-LqR0VTRs3FszmYz3IZPSrmapFqUWk3yieEMyNYTroJo2r0v-k3NXwXd_EILLfaK1hvQBvB1UmzvZlkAbi-l1tC0iaiYK_-grBfkTc1NXaOVTJXAjvJgCr28rR2pXRpwWDf9BqRxnEUAPYAcGCbF1Dh5l-gfydhRlnHs3dDb_peSQJ-emHy-OzCiiaaqX4mdyCWBMng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0a6a5812d.mp4?token=nB7dM9IVQdF01QRqRuaHRMEYAVywu4VAbkZnIqeQtMDaa2PGLUywyR0lwRueC7eArZNcnisrJUN9wMeZ49NRuUChkwBu6T7lEauIxpg0tBHHVukNphC0_5mwDb_xquGcXcVWVXy7iflQH2u-LqR0VTRs3FszmYz3IZPSrmapFqUWk3yieEMyNYTroJo2r0v-k3NXwXd_EILLfaK1hvQBvB1UmzvZlkAbi-l1tC0iaiYK_-grBfkTc1NXaOVTJXAjvJgCr28rR2pXRpwWDf9BqRxnEUAPYAcGCbF1Dh5l-gfydhRlnHs3dDb_peSQJ-emHy-OzCiiaaqX4mdyCWBMng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دختر بیرانوند : بابام استقلالیه و دوست داره برای استقلال بازی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/135643" target="_blank">📅 09:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135642">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/889c05b23a.mp4?token=pKu3Hgcm4hlU8gibS8CsTMLu-Yd7ysdrXpbl190BfmfcyZ-D-yvMKucNpFWLvSCiBiPx2E1EpBUwm5dJtILY6ope7idFgnh9K8oADBbCXgEtiizPieg35KwQsbZxtgtllwwEmoxUwcIzmqAghi9hMaxf_5AXbpsDX7lujXScxEximxRTpLWLuzhri_5uEBByhphdS8CCExIKgH3_RVCmCfaq2ky23R8jkefQHnmMd47KXLoCnfEJhyqyz3kBRYxj-MIbL2kXReb5iWkOmX7RulHX5jvHt2dWeMWfOMRCt-VhMXSdr4Oe2PpBPBfaq55bhfxqPfV3DP5cvlO0pCawT4eK7l2yS7PsDK4p9ryjdjjVubrUN6D40M27sX8yBi0-XA6v9vUwxgxkg4Sm6DvJd1rijCPgKgZnrQTSCdDDGnhy_6bSOqdaZL_8PZy_z-xzl_FqPcEWdkSLf7pNM1kF4z-GMnc-U-HYmbeGjwI_gXeVJ1dg9nn6rc2X9IKDHiDbTVuGeBOclPbxSWYmshZkflAehHPGqJ7Gt6ZIRkH3K8Xr_y5F-H9bx-HbqdOMnOnxSwlcMpko7sYRmWvLZQh5le4uOwdBYhsc9E-3LZ8REtjWG2uLp6JoSAUhtwpdqPQRGCfmoBSRgTldLEcNQcY5tCGcjCti760TaHd8naUCvh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/889c05b23a.mp4?token=pKu3Hgcm4hlU8gibS8CsTMLu-Yd7ysdrXpbl190BfmfcyZ-D-yvMKucNpFWLvSCiBiPx2E1EpBUwm5dJtILY6ope7idFgnh9K8oADBbCXgEtiizPieg35KwQsbZxtgtllwwEmoxUwcIzmqAghi9hMaxf_5AXbpsDX7lujXScxEximxRTpLWLuzhri_5uEBByhphdS8CCExIKgH3_RVCmCfaq2ky23R8jkefQHnmMd47KXLoCnfEJhyqyz3kBRYxj-MIbL2kXReb5iWkOmX7RulHX5jvHt2dWeMWfOMRCt-VhMXSdr4Oe2PpBPBfaq55bhfxqPfV3DP5cvlO0pCawT4eK7l2yS7PsDK4p9ryjdjjVubrUN6D40M27sX8yBi0-XA6v9vUwxgxkg4Sm6DvJd1rijCPgKgZnrQTSCdDDGnhy_6bSOqdaZL_8PZy_z-xzl_FqPcEWdkSLf7pNM1kF4z-GMnc-U-HYmbeGjwI_gXeVJ1dg9nn6rc2X9IKDHiDbTVuGeBOclPbxSWYmshZkflAehHPGqJ7Gt6ZIRkH3K8Xr_y5F-H9bx-HbqdOMnOnxSwlcMpko7sYRmWvLZQh5le4uOwdBYhsc9E-3LZ8REtjWG2uLp6JoSAUhtwpdqPQRGCfmoBSRgTldLEcNQcY5tCGcjCti760TaHd8naUCvh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
حمله و توهین زشت بیرانوند به مهدوی‌کیا: بازیکن نسل گذشته تیم ملی تا مکزیک آمد با اینفانتینو عکس گرفت، ولی حاضر نشد به کمپ تیم ملی کشورش بیاید!!
🔴
بیرانوند:
آقای مهدوی‌کیا از چه چیز ترسیدی که به ما سر نزدی؟
🗣️
بعد از بازی با بلژیک کدام یک از اسطوره‌های تیم ملی یک استوری دمتان گرم برای ما گذاشت؟
❌
👀
پی‌نوشت: دمتان گرم بابت چی؟ بابت حذف و نرسیدن به جمع ۳۲ تیم؟؟؟ چی میگی تو؟ دهنت رو آب بکش اسم آقا مهدی مهدوی‌کیا رو میاری. خوبه خودت هم می‌دونی اگر کسی با شما عکس بگیره فحش میخوره. چون محبوب نیستین.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/135642" target="_blank">📅 09:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135641">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
بیرانوند: اگر به استقلال بروم می‌شوم یاغی پرومکس؛ هنوز برای برگشتن به پرسپولیس فکر می‌کنم
😐
❗️
❗️
سال قبل از استقلال پیشنهاد داشتم و قرار بود اتفاقاتی بیفتد که نشد؛‌ امسال هم این پیشنهاد هست.‌من اگر استقلالی شوم یاغی پرومکسم. خیلی‌ها دوست دارند من به پرسپولیس برگردم ولی خودم استرس دارم. هنوز برای برگشتن به پرسپولیس فکر می‌کنم.من تا زمانی که تا صد مطمئن نشوم که پرسپولیسی‌ها دوستم دارند برنمی‌گردم. اگر عملکردت خوب باشد برندت حفظ می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/135641" target="_blank">📅 08:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135640">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet.apk</div>
  <div class="tg-doc-extra">54.1 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135640" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
جدیدترین آپدیت اپلیکیشن 1XBET
🤖
✅
ورود / ثبت نام از اپلیکیشن
🎖
بزرگترین اسپانسر رسمی لالیگا
🔵
حتما
بدون فیلترشکن
از اپلیکیشن استفاده کنید
🎁
هنگام ثبت نام کد هدیه 130 دلاری vipfarsi را وارد کنید.</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/135640" target="_blank">📅 02:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135639">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyXMiU2F7fe_21KY-cQ6GcMmBXGIYsHGHQzzWq0fd71xvYisg43K-IABX71HsJghb9jU1C7jhV3RCP0tYCyxnVPw0h8qS0KMASod73VegQpq4WqRqcwCUs0abEhx44LEOQrSWwaBaiybfNiPjebvD7aChg2tnDXQUat7gzU2gH5WGU9kNh-fhtyRUFf5p0Tvv98I_iGYTp0BPHNE7X9xxaSOq2EwBQW5cdNCJaDMPw9_GeLATAODQ6VC7vzPPd1s6obyE8KneujLXZdsGCcpavOVQRmVtVYz157nzbYax5t3PHh1iXso3GhU31k-Z2WL1V3xGwjMc8Dm5aLreJ1B2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1️⃣
همین حالا در وان‌ایکس‌بت پیشبینی کنید | Bet now on 1XBET
1️⃣
🏆
نیمه نهایی بزرگان؛
فقط چهار تیم باقی مانده‌اند…
🇦🇷
آرژانتین
🆚
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
⚡️
وقت آن رسیده که قهرمان واقعی خودش را نشان دهد.
بازی ها را با بالاترین ضرایب پیش بینی کنید
🔥
🟦
آدرس وان‌ایکس‌بت:
🌐
Link :
1XBET.COM
🌐
Link :
1XBET.COM
🔑
برای ورود به سایت از وی پی ان (فیلترشکن) کشور های آسیایی یا کانادا یا ترکیه استفاده کنید.
➖
➖
➖
➖
➖
➖
➖
➖
🌐
Channel :
@iran1xbet_official</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135639" target="_blank">📅 02:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135638">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">#تایمز_توئیت
🫦
یه مشت زنا زا… شدن کانال دار و خبرنگار جاکشا نون زندگی شونو از خبر پولی و بولد کردن بازیکن های ایجنت ها در میارن هرجا کیر خر دستشون رو نمیگیره همگی میریزن رو یه باشگاه خاص…. جمع کنید پوفیوزا ۵۰۰ تومن بهتون بدن تخم های طرفو از دهنتون درنمیارید…</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/135638" target="_blank">📅 01:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135637">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">#تایمز_توئیت
🫦
یه مشت زنا زا… شدن کانال دار و خبرنگار جاکشا نون زندگی شونو از خبر پولی و بولد کردن بازیکن های ایجنت ها در میارن هرجا کیر خر دستشون رو نمیگیره همگی میریزن رو یه باشگاه خاص…. جمع کنید پوفیوزا ۵۰۰ تومن بهتون بدن تخم های طرفو از دهنتون درنمیارید
🫦
سر شب آدمو مجبور میکنید شیلنگ عنو بگیره روتون…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/135637" target="_blank">📅 01:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135636">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromali habibi</strong></div>
<div class="tg-text">قهار مدعی پرسپولیسی بودنه ولی از وقتی تو رفته فرهیختگان بساط این روزنامه همینه</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/135636" target="_blank">📅 01:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135635">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⛔️
من نه کاری به صحت سقم اخبار دارم درخصوص کسری طاهری و نه قصد حمایت دارم، اما یک سوالی فکر منو درگیر کرده چرا خبرگزاری فرهیختگان از بدو حکم گرفتن مدیرعامل فعلی باشگاه هر روز در حال زدن مدیران و باشگاه پرسپولیسه
‼️
دوران اقای رضا درویش چرا صحبتی نمیکردید ؟!…</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/135635" target="_blank">📅 01:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135634">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⛔️
من نه کاری به صحت سقم اخبار دارم درخصوص کسری طاهری و نه قصد حمایت دارم، اما یک سوالی فکر منو درگیر کرده چرا خبرگزاری فرهیختگان از بدو حکم گرفتن مدیرعامل فعلی باشگاه هر روز در حال زدن مدیران و باشگاه پرسپولیسه
‼️
دوران اقای رضا درویش چرا صحبتی نمیکردید ؟! همه چیز گل بلبل بود ؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/135634" target="_blank">📅 01:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135633">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
ماجرا از این قراره که کسری طاهری اول با نساجی قرارداد بسته و سه هفته پیش برای انتقال قرضی به پرسپولیس توافق کرد.
🔴
درواقع نساجی اینجا به لحاظ مالی داره سود میکنه و با زرنگی تونسته کسری رو بگیره و بعد به پرسپولیس بفروشه.//خرمی
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/135633" target="_blank">📅 00:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135632">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❗️
❗️
جزئیات عجیب از هایجک کسری طاهری توسط نساجی!
🔴
فرهیختگان مدعی شده پیمان حدادی دو روز پیش به باشگاه روبین کازان نامه زده و خواستار جذب کسری طاهری به‌صورت قرضی و بدون پرداخت مبلغ، یا انتقال قطعی با ۷۵۰ هزار دلار شده بود.
🔴
اما در ادامه، زندی مدیرعامل نساجی…</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/135632" target="_blank">📅 00:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135631">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
طاهرخانی فرد نزدیک به باشگاه :
❌
یکی از مدیران باشگاه پرسپولیس این موضوع رو تایید کرد و کسری هایجک شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/135631" target="_blank">📅 00:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135630">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/135630" target="_blank">📅 00:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135629">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
✅
فرهیختگان:
❌
باشگاه پرسپولیس امروز تازه نامه نهایی رو واسه خرید کسری طاهری زده، در حالی که شهاب زندی مدیرعامل نساجی ۴۸ ساعت قبل نقد پول رضایت‌نامه قطعی رو پرداخت کرد و انتقال رو نهایی کرد و امروز هم کارت بازیش رو گرفت... حالا هم به پرسپولیس گفته نیم‌فصل…</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/135629" target="_blank">📅 00:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135628">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
فدراسیون  فوتبال روسیه آی‌تی‌سی کسری طاهری رو تو سیستم tms برای باشگاه نساجی مازندران صادر کرد و نساجی زودتر برای جذب کسری با روبین کازان بسته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135628" target="_blank">📅 00:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135627">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
فرهیختگان:
❗️
مدیران باشگاه نساجی با روس ها ارتباط خوبی داشتن و کسری طاهری رو ۸۰۰ هزار تا خریدن و می‌خوان با 1.2 میلیون دلار به پرسپولیس بفروشن.
❌
امروزم کارت بازیش واسه نساجی به فدراسیون رسیده و تا نیم‌فصل حق جدایی از نساجی نداره
😐
😐
😐
😐
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/135627" target="_blank">📅 00:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135626">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
طاهرخانی فرد نزدیک به باشگاه :
❌
یکی از مدیران باشگاه پرسپولیس این موضوع رو تایید کرد و کسری هایجک شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/135626" target="_blank">📅 23:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135625">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
طاهرخانی فرد نزدیک به باشگاه :
❌
یکی از مدیران باشگاه پرسپولیس این موضوع رو تایید کرد و کسری هایجک شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/135625" target="_blank">📅 23:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135624">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
فدراسیون  فوتبال روسیه آی‌تی‌سی کسری طاهری رو تو سیستم tms برای باشگاه نساجی مازندران صادر کرد و نساجی زودتر برای جذب کسری با روبین کازان بسته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135624" target="_blank">📅 23:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135623">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❗️
برگام
🚨
فرهیختگان: کسری طاهری به نساجی مازندران پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/135623" target="_blank">📅 23:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135622">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
🔴
فرهیختگان: یه باشگاه لیگ برتری دیگه کسری رو خریده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/135622" target="_blank">📅 23:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135621">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❗️
پس چرا خودش میگه فردا با پرسپولیس میبندم
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135621" target="_blank">📅 23:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135620">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
🔴
فرهیختگان: یه باشگاه لیگ برتری دیگه کسری رو خریده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/135620" target="_blank">📅 23:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135619">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
انتقال کسری طاهری به پرسپولیس منتفی شد!
🔖
فرهیختگان: این مهاجم جوان در ۲۴ ساعت  گذشته به عضویت یک باشگاه دیگر ایرانی درآمده و عملا طبق قوانین رسمی فیفا اجازه پیوستن به پرسپولیس ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/135619" target="_blank">📅 23:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135618">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">😳
😳
😳
😳
😳
😳
😳
😳</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/135618" target="_blank">📅 23:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135617">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/135617" target="_blank">📅 23:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135616">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
فوتبالی: وحید امیری از باشگاه خواسته یه فصل دیگه بمونه تا با پیراهن پرسپولیس خداحافظی کنه. خودش هم گفته حتی اگه بیشتر نیمکت‌نشین باشه، مشکلی نداره. حالا همه‌چیز به تصمیم تارتار بستگی داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/135616" target="_blank">📅 23:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135615">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_zi8FPepSd60WmTw4QZ4BRQQYUC1iVdldyeYnmPLBC3ZGdTULHZzjMZ_TsKbTOrKBX7wWzvgdwwVfNQt3AFdI0qjjkox4IINCTt_dK7uhB1pQoKAhCsBYzz2i871p7mZ2R-y7wCvDI5PZyoQ0Wf6ffX9eW4Ae4rxzvHAn26rpI8NQ43y-7qeCI0CeVaCLXGg5kp6vkptZlb_dwwa0wpbAzqcKe5TI8luwarxG0A3XYHPP3xPzw7xoWU2ZBF6prj5vvGdzUxIoUnB6CqvvNbjgVokw7Ak4znXRj--RZyuML7RkkrUjKwKYNvCBFJF0QYHsZPQHU2TWp8NOqhKI6QtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کسری طاهری اولین برنده جایزه توپا (پدیده سال فوتبال ایران) شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/135615" target="_blank">📅 22:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135614">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32499e90a2.mp4?token=ahSCsm9tNAH9cW6xt82uHNcBH5_w3O_tm0m-e-X_86fb8reysQdRrt7u10bEcTiHVzz-REx3bpvZI7_i0ZA13SHy9FIQUpWmHS-YmcSN-CRQTrsysdW20gzCgjcG4-ju6iJsOf-kyouLnLVTkg9uRsSZ04ZipNfVPH1v_6H746fmoXmEbApr8XEHkosXjixCx9G8oyUUOSbrcdYOCUZjK8P82xMv950qIuIRn5bdxVyvrkkACt68y5i_6Sc2hds5KxtF28VJAEma-EYefA38iFhTTdlAvxjwtKzbMxVTGGKqqmMdtcjcydIOB93qArsEw9DanVMGGiSz7AJCfbnhAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32499e90a2.mp4?token=ahSCsm9tNAH9cW6xt82uHNcBH5_w3O_tm0m-e-X_86fb8reysQdRrt7u10bEcTiHVzz-REx3bpvZI7_i0ZA13SHy9FIQUpWmHS-YmcSN-CRQTrsysdW20gzCgjcG4-ju6iJsOf-kyouLnLVTkg9uRsSZ04ZipNfVPH1v_6H746fmoXmEbApr8XEHkosXjixCx9G8oyUUOSbrcdYOCUZjK8P82xMv950qIuIRn5bdxVyvrkkACt68y5i_6Sc2hds5KxtF28VJAEma-EYefA38iFhTTdlAvxjwtKzbMxVTGGKqqmMdtcjcydIOB93qArsEw9DanVMGGiSz7AJCfbnhAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اشک های مجید عیدی در مراسم معارفه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/135614" target="_blank">📅 22:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135613">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72ecbd7633.mp4?token=h4PEdmG8MvhkIn2SvfRFLKpYZKybpLs0yEAbphDi_eO8RydzN1aQ4e5gU-c9mpAm28JD0m3bHetiptIAJs-R7WTQMFNDd_GkKAUrA6mZVVljWw1EWE5uSG5PQRiExBFIOnlmnz_hi_H6aT3y3i60JhvXNkW-xxO7Qgnkyt_qz7mu_mhOvIe7DOzHqQboU9GFxQJRQPHYPBr64h3ISbj3Q2x8j5Ig3EHxMhQpSgSsBfs2kYnTCCfj7BxA3Tsyz-Z-CACUveSaY0lW9ryPAkO6AoRPIfCJrvPrjbYIFo31WMBfbUmpU-idVl0gjx4vWUF1wl-oyKATqq7UVMQ5nAU_gIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72ecbd7633.mp4?token=h4PEdmG8MvhkIn2SvfRFLKpYZKybpLs0yEAbphDi_eO8RydzN1aQ4e5gU-c9mpAm28JD0m3bHetiptIAJs-R7WTQMFNDd_GkKAUrA6mZVVljWw1EWE5uSG5PQRiExBFIOnlmnz_hi_H6aT3y3i60JhvXNkW-xxO7Qgnkyt_qz7mu_mhOvIe7DOzHqQboU9GFxQJRQPHYPBr64h3ISbj3Q2x8j5Ig3EHxMhQpSgSsBfs2kYnTCCfj7BxA3Tsyz-Z-CACUveSaY0lW9ryPAkO6AoRPIfCJrvPrjbYIFo31WMBfbUmpU-idVl0gjx4vWUF1wl-oyKATqq7UVMQ5nAU_gIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شنیده ها :
⌛️
باشگاه پرسپولیس ساعتی‌ قبل با پرداخت 700 هزار دلار به باشگاه‌روبین‌کازان؛ کسری طاهری رو باعقد قراردادی یک‌ ساله قرضی همراه با بند خرید قطعی به ارزش 500هزار دلار دیگر به خدمت گرفت. بخش رسانه ای باشگاه بزودی پوستر طاهری رو منتشر خواهند کرد. …</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/135613" target="_blank">📅 22:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135612">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
پرسپولیس با سه بازیکن جدید به توافق رسید.
🔴
به گزارش قرمزآنلاین، کسری طاهری در پی توافق با روبین کازان در آستانه معارفه شدن از سوی باشگاه پرسپولیس قرار دارد. روبین کازان رضایت نامه قرضی او را صادر کرده است.
🔴
رقم پیشنهادی ۴۰۰ هزار دلار بود که با چانه زنی…</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/135612" target="_blank">📅 21:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135611">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcckcrXrpZN3AYV9tisLCzqRpcpYJbhh4VFJBO5t6yQ_jlPu89qcgkp8zIxe59Bj3_QEoTncays8JRxtiy0O0uiHUb-jsy11CEmnYJuuLgGEZhNf2KhM6xY_LNUAEFKqMUC3ppozExY0u65ziMFZo-A2mFpUvUvHUhtS23sMKvuhY_nrmIX3TW0oNBNAJEjWadC15-49nO1YRlBICdhJsnq4fKS60fTElmw0fPpe3vyaPrlFCkD5zMWB8uzKTeXVUnTPkc3VrOFajumxHd52IMLQawleqDLZNAIrJLtrYvgN9BwPmqgxqFX1tX27EogEp1G6AzDgB8sT7M-i_puGmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرسپولیسی‌ها عصر امروز تمرینات خود را در حالی پیگیری کردند که پیام نیازمند و محمدحسین کنعانی‌زادگان پس از حضور در جام جهانی ۲۰۲۶ به تمرینات تیم اضافه شدند و کریم باقری نیز در جمع اعضای کادر فنی حضور یافت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/135611" target="_blank">📅 21:42 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
