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
<img src="https://cdn4.telesco.pe/file/UtH2I92lfk5ugLHHd0UGRuJHNly02HUwNOlICNEIazy0WmodVyW1N0ZVPKzL5IiRh6T-85wQzjZ3_GmE78mU8hLn-ZRn_lF9OIpM2l6p2gCjiiEzsWmyBtP5_nlYH4ZtbknYMkt82dhCIXDpYVUZKSdOogMJyJt8tctnkRbESVdqdRx4LxT3NcT2afzZk4nSnpABycr20ZQrE6ZXYFd6MZDK5YgwCsOaEIf1wPe-sajipBzk2EE9ZB29nf4LBeekBG_n77ZzZksHzmrOoDb5TAGaY16qV28Y3XXae3V9pNNdUDzmYqDc8fjPPB3m-NZLAtDbIzwBtaaA0Go6yfzMng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.4K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 22:39:44</div>
<hr>

<div class="tg-post" id="msg-140809">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⭕️
⭕️
ترامپ:
🟢
اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/SorkhTimes/140809" target="_blank">📅 21:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140808">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
❌
❌
ادعای جنجالی حسن روشن درباره ساپینتو
⬇
حسن روشن، پیشکسوت استقلال، مدعی شد در دوران حضور ساپینتو در استقلال، اتفاقاتی در اردوهای تیم(دختر بازی) و محل اقامت او رخ داده که حاشیه‌های زیادی ایجاد کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/SorkhTimes/140808" target="_blank">📅 21:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140807">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
❌
خبرنگار: شما ایرانی‌هایی که آمریکا باهاشون در ارتباطه رو «دیوانه» خطاب می‌کنید؛ چطور میشه با آدم‌های دیوانه به توافق رسید؟
❌
❌
🇺🇸
ترامپ: شاید منفجرشون کنیم. باید بین این دو تصمیم بگیریم؛ یا منفجرشون می‌کنیم یا به توافق می‌رسیم. زمانش که برسه، تصمیم می‌گیریم.…</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/SorkhTimes/140807" target="_blank">📅 21:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140806">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
🟡
🔴
حسن روشن:
🤔
🤔
ساپینتو اکنون بهانه دیگری پیدا نکرده و روی داوری تمرکز کرده است. ساپینتو یک مربی درجه سه است. صریح می‌گویم روی آدان در دربی نمی‌توان حساب کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SorkhTimes/140806" target="_blank">📅 21:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140805">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
یاسر آسانی: رامین رضاییان کسی بود یک دقیقه بعد تمرین تمام اتفاقات رو لو میداد و همه میفهمیدن و ساپینتو برای همین لج کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SorkhTimes/140805" target="_blank">📅 21:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140804">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/SorkhTimes/140804" target="_blank">📅 21:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140803">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
هاشم نژاد به تمرینات تراکتور برگشت و برای بازی مقابل استقلال اماده هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SorkhTimes/140803" target="_blank">📅 21:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140802">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXqelgtsIGPVR5qt1eF7xwJ8NIQ5RcsUxdyepnPykuafJ9ZLsMRIOJ3AM2sYZ72fHxNlhxlvEDJHAZRQys-PKkAPxA-rkJmgZTb-q4lnXvzXZCgivpM1ipCcFKrgn3TkhEtZX-FlXH_0x8rzahJP6XJ3fC1ORNs-SdAmu35MoMWFM7z6fJtJoBcVQVJcDwccabmrnHyjmW_1ZMiKy3iS3AvX0vIsb5x1cAB4jQWsRD91NiBvUBbP9MgixZdPN4xwAulXuhBwNg7m2FbEaTJHgWu0PedXu6eRVuI-0MG9nkKqK3-LBfLDGpscw_6ycxTI2I5zcmCDGkz8YGz6R9p4qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد شمال و جنوب اروپا در یک جدال سنگین امشب در پارکن!
🔥
⚡️
[
دانمارک
🇩🇰
🆚
🇵🇹
پرتغال
]
⚽️
دانمارک بعد از برد ۲-۰ مقابل ولز با اعتمادبه‌نفس بیشتری وارد بازی می‌شود و در پارکن هم معمولاً تیم سختی برای حریف است؛ پرتغال اما با ۶ امتیاز صدرنشین گروه است و دو برد متوالی داشته. نکته مهم امشب غیبت کریس رونالدو است؛ او اردوی پرتغال را ترک کرده و برونو فرناندز هم با مشکل جسمانی روبه‌روست. در مقابل، دانمارک روی هویلوند، دامسگارد حساب می‌کند.
سناریوی محتمل: بازی نزدیک و پرموقعیت، با شانس گلزنی دو طرف.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/SorkhTimes/140802" target="_blank">📅 21:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140801">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
نایب رئیس فدراسیون فوتبال پرتغال: رونالدو دیگه به تیم ملی برنمیگرده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/140801" target="_blank">📅 18:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140800">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2Y1j0OJbvgeqdNqhV0taUXPNjzo3Pg81srVHz1Tjp5g841mg1akQUqoxsXBX_tzo5-yhD--b8ePiehyE0jLQc_txZBjyXxhMUaVohIRYBwMhASDWOnzFIY71_w6yAcUWU35XadX872zruhrBh43p9PkVjWjtbKf_OGZeCtpq7aAuuAfUCtkl1BdBW-L-ggBz5MJ__WZuUaHAZHLv0m-I5wgtN7lTDWjWJAU0MEPVq1eHbHqppgy2o5CeXtL-8AdYdYkVhnd8LRPD-QANPtcvYiYbRnAJYdpJIP41obwJF0fjKesVrGrTG5DedEd-kiJllJraxqqClqquN72nbuLoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علی علیپور دویدن را آغاز کرده و احتمال حضورش مقابل صنعت نفت وجود داره/ورزش‌سه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/140800" target="_blank">📅 18:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140799">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lChtiS53vtJChmNQCON8durcNFYeSkxvmd2vrWO2xvraUPW-aucDzQRZEAVrnYZy9afqrc5h48JaYtiSUJFeK67L7Y-GcZ4HZkro5yNkRqE8SSY9hvF2B0A0XpGSRp3rTde3vyJiaKUdu-wIbyfYxa75JjtQEtmJZJrJroqgPjrvy2HJTPolamLsNPAlKTVyAuFa6usxhX503K62DTfBr7YYf_16pYqGA8-JpFxW-11etzT6BgARUCxEei7WJyvvkckRZdWeFuoOnfP4-z21B6__G_UYY9PkAGw5ePNmhyNsGVFDj3efFf-EzVVC4Xa4YrDnqO2BHj2v9C9rCKK4Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
گویا بازی دوستانه سلحشوران تیم ملی برابر گینه بیسائو به دلیل محدودیت‌های پروازی لغو شده است. به این ترتیب سوژه خنده سوم این فیفادی از دست رفت!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SorkhTimes/140799" target="_blank">📅 18:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140798">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔄
🔄
هوشنگ نصیرزاده: پرسپولیس با شکایت از آسانی به CAS وقت خود را تلف می‌کند هیچ سندی علیه آسانی وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SorkhTimes/140798" target="_blank">📅 18:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140797">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4PtnYaYnsaV9g71OpMmlHZAUdkjO6j5JMcKi1lWy-2qrzxhjTLvoKJ8ilT5bxuycCwCHNTSPWfxXCmQg-ZceMOiC2_y7mm6Z1HiBu1yWmejw4wf2dXWlX_TPPP3ol4PZ75ikxiVk8SOpHSEyJxi7ED-a6azX-0AkssVx9sPlCo40VfljB5lnBc5wWkP-B0fdhUmJ9cSlrihEch8gc91GowvjExb_IvSvxlkX-S-OFhpbQTKuhFQCbLCSAEQUMmwnWjr-SyjwdeIJczjPMT2xLQO2Wu2X6VdrNzQ6Q4_Jjp-_czoWeMdB1DiD1H5FLFBTCDHORz7MpS_XobFD1VvGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
ایجنت دنیس اکرت در تلاشه که این بازیکن رو فرو کنه به یکی از تیم‌های ایرانی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/140797" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140796">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfgWwQLICTcjQmmXO9fmcNh-6NSA9-p1Jm9Z8eP6F-rbvyq_NmXaO3R1VZJV2cqtzMd7gNitMOCiPurdY3-qh8QpBMS8KmB7mNlQY50m7GwProOa2tTfmScwHMlf9BcppuicStq0d3R77-7z1nD2RVjrIjL3vk9CyOiyrXDE7LrfwPjA0wQMJnR_77AIllCWxNi_nbXzxcl6GwyWcuAtXGkustNwm0BR0dopIgbRmcpOW0_Lyg57hIs2uPMQQIejr6ck6YQuTMdQGDLN-3vk9SNMAYOsjJfEsfs4wUvrqu-JrYkXShgXQyYiyajSI9hFniOtjDy2CIl5mUyAwlKXCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نایب رئیس فدراسیون فوتبال پرتغال: رونالدو دیگه به تیم ملی برنمیگرده
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/140796" target="_blank">📅 16:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140795">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jD2VbV6R-8Lak9X4tLiZfRa1gSm--GT1kk-9933uLJGCM1lIC5W2tIrNQsI_0l2QMIv0D_79vcAOfafjaB0uBmvgXgNLCxArZMGxmDS-ZSGbpA87HZR55qRU9XkBAzJOCmiIxYURi3pqMsPHxNJMI-DrgY4xobd9eBakANkviAIaHzVBF6mNhW9jXQRyC9oPiZCkpiAYzOT2pNDHlPByp8VyCf7d_wkQeT8rNhYNqMSktOIwYO011QRe3C7o4P3QZUHM6wFeCC6rUgl9pu0cK1JVn04tnmPdS78Q9qkizK1eNBTOTnlzBL95lMG4MzjFGBdfblbhi-0hlZm9Wl7i3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
دیشب در بازی دوستانه بین کونیا اسپور و تیم ملی فلسطین بازی رو دقیقه 89:59 متوقف کردند و گفتن بقیه بازی رو وقتی انجام میدیم که فلسطین آزاد بشه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/140795" target="_blank">📅 16:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140794">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/140794" target="_blank">📅 16:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140793">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KO4elTNkFyB6HE9Xoj4P3ezYMY3SU6XkaySk7YdQGQpklcau9kpr8Vcao2PqpOHEFvl27xD8tDgaylh8Vwq_bpkYK8J-d2PPJUTt2DeeNTvHhRBIBCpMgUAY09K-dgD3onMoeTVr1SYMDw6jPIER1KpkwfiAGF3zkN9c0ct3rTCVr2WXbbjr8SkJwEaooO8qRi8XZzHPQTYezC2dRv333wLO65w229v_0kaM_MQWHUjWjAX45-jDZnu9xe81c4PI9aL7Ns7xe01HcJMfNKbXiST1hKVEC1cJsQj3bfnUmQ_83N3z8Lg4nvRNbUaty28PJFcF1K_n-TIFXkUXfXB6kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🔴
در یازدهمین سالگرد درگذشت هادی نوروزی کاپیتان فقید پرسپولیس، یاد و خاطر این بازیکن در دیدار امید پرسپولیس و سیاه جامگان زنده نگه داشته شد.
🔺
پیراهن شماره ۲۴ هادی نوروزی در دستان هانی نوروزی فرزند هادی و بازیکن تیم امید پرسپولیس در عکس تیمی پیش از بازی.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/140793" target="_blank">📅 16:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140792">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g03-1NLnHx-OR2UQQ5BDMMNkvNJllatVUUgpsSQfgffsg6ysTAR5yDfNSHtYE8a8oFIGDv1jiZDEid3OXRSIxOP6-noxuIrnMk8D_Az0t9p4A0XjJ5M0YFkMmCF8yCQkYWjB62m-0igYGvqb4dqlu2wcn0SG_Pl1WCgELO6dWX_SjILCQ52eNGYTreCcK4J3r9z4Tgplsl01cz8gnwpbPDI7GUjGDbWt3whmBldA_Vlg5eGZ4JC5BJAslEWXQZMzfkZC3BibU6LoxbF2DjNOb3rmjtq60g4F20brtYpyRWgILdsVi2q8WpmXW-jKz5E1MA3HvNbA8f7d-sUGLZPrwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
Germany -
❤️
Serbia
⏰
Tonight 22:15
🏟
Allianz Arena
🇪🇺
آلمان بعد از ۱-۱ مقابل هلند و شکست ۰-۱ برابر یونان هنوز زیر نظر کلوپ به برد نرسیده و مهم‌ترین مشکلش تبدیل مالکیت و برتری میدانی به موقعیت‌های باکیفیت است. صربستان هم شرایط خوبی ندارد؛ در دو بازی ابتدایی لیگ ملت‌ها مقابل یونان و هلند شکست خورده و با صفر امتیاز قعرنشین گروه است. از نظر تاکتیکی، انتظار می‌رود صربستان عقب‌تر بازی کند و فضای کمی بین خطوط بدهد؛ خود کلوپ هم روی همین موضوع تأکید کرده و گفته شکستن دفاع فشرده برای آلمان چالش اصلی خواهد بود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/140792" target="_blank">📅 15:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140791">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⭕️
⭕️
⭕️
خبرورزشی: مرغ حدادی یه پا داره بردن شکایت آسانی به Cas همین و تمام
⭕️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/140791" target="_blank">📅 14:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140790">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
✅
✅
تیوی بیفوما که بدلیل مسائل سیاسی دعوت تیم ملی کنگو را رد کرده بود دقایقی پیش برای حضور در تمرینات پرسپولیس وارد ایران شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/140790" target="_blank">📅 14:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140789">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
🇬🇭
کارلوس کی روش بعد از باخت خانگی ۴-۲ غنا جلو گامبیا سیکش از تیم ملی غنا زده شد و باید دنبال تیم ملی جدید بگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/140789" target="_blank">📅 13:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140788">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
❌
❌
دراگان اسکوچیچ از طریق واسطه‌های نزدیک به فدراسیون فوتبال، برای بازگشت به نیمکت تیم ملی و هدایت مجدد ملی‌پوشان اعلام آمادگی کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/140788" target="_blank">📅 13:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140787">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🗣
سرگیف و بیفوما هردو در تمرینات تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/140787" target="_blank">📅 13:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140786">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
❌
قطبی یک قدم تا بازگشت به فوتبال ایران؛ مذاکره ادامه دارد  •
✔️
✔️
مدیر برنامه افشین قطبی اعلام کرد مذاکرات با فدراسیون فوتبال ادامه دارد و دو طرف در حال توافق بر سر شروط همکاری هستند. طبق مذاکرات انجام‌شده، قطبی قرار است مدیر فنی تیم‌های پایه و سرمربی تیم امید…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/140786" target="_blank">📅 13:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140785">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
محمد نصرتی درباره حضور دنیس اکرت در جام جهانی: آقای قلعه‌نویی، با دعوت از اکرت در حق یکسری بازیکن جوان اجحاف کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/140785" target="_blank">📅 13:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140784">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
❌
هفته هشتم لیگ برتر در آستانه تعویق!
✔️
✔️
در صورت قطعی شدن برگزاری سومین دیدار دوستانه تیم ملی در فیفادی پیش‌رو و انجام این بازی در ترکیه، احتمال تعویق برخی مسابقات هفته هشتم لیگ برتر وجود دارد.
✔️
✔️
در این صورت، دیدار حساس استقلال و تراکتور نیز ممکن است…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/140784" target="_blank">📅 12:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140783">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⭕️
فووووووووووووووری
❌
محمد مهدی محبی مصدوم نشده و اصلا مصدوم نیست. امیر قلعه نویی دیشب با هماهنگی قبلی برای توجیه شکست های پیاپی به محبی ستاره تیمش اعلام کرده باید تا دقیقه ۳۰ مصدوم بشه و تعویض بشه تا فشار رسانه ها کمتر بشه و این یک حربه از سوی قلعه نویی…</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/140783" target="_blank">📅 12:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140782">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
میلاد سورگی: از باشگاه بزرگ پرسپولیس ممنونم که باعث شد من به فوتبال معرفی شوم و به تیم ملی برسم. امیدوارم روزی به عنوان ستاره به پرسپولیس برگردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/140782" target="_blank">📅 11:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140781">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🗞
لیست بازیکنانی که قلعه‌نویی ازشون ناراضیه و شاید دیگه دعوت نکنه:
❌
محمدمهدی محبی
❌
صالح حردانی
❌
سامان فلاح
❌
احسان حاج‌صفی
❌
حسین حسینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140781" target="_blank">📅 09:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140780">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
خط خوردگان بزرگ لیست
😀
محمدحسین کنعانی‌زاگان
😀
روزبه چشمی
😀
شهریار مغانلو
😀
هادی حبیبی‌نژاد
😀
علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/140780" target="_blank">📅 09:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140779">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
پیگیری‌ها از مسئولان باشگاه پرسپولیس نشان می‌دهد که هیچ پیشنهاد رسمی از سوی باشگاه‌های خارجی، چه از قطر و چه از سایر کشورها، برای جذب محمد عمری به باشگاه پرسپولیس ارائه نشده است و بحث جدایی این بازیکن صحت ندارد. / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/140779" target="_blank">📅 09:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140778">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
یازده سال گذشت
❌
روحت شاد؛ هادی جان 24 ابدی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/140778" target="_blank">📅 09:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140777">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
❌
❌
دراگان اسکوچیچ از طریق واسطه‌های نزدیک به فدراسیون فوتبال، برای بازگشت به نیمکت تیم ملی و هدایت مجدد ملی‌پوشان اعلام آمادگی کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/140777" target="_blank">📅 09:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140776">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
یه سری شایعات از بازگشت اسکوچیچ به تیم ملی در حال انتشاره که نه تایید می‌کنیم و نه رد می‌کنیم./فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/140776" target="_blank">📅 09:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140775">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AT37vy77d6MaUrIwBEWpOHwf2Z1Xe1uZ2BI-rkfFA1RA3Q-BRoUbNy-7tFry03G31lLX-MSU9Ki1Z3z3LkAAfUtBV7YbN0vYXcMPidF0oJlAj5IFpD2kfsCeF-Eq_KqrBGAiWf8UydjZEeD4bFmbGtS8irFZKdghVGHnoxVBO_SgfYA6dm4ekWA63PVJ1Y9nGKpGV1Kg0qA4F6nxTN7-v7pJ3LkEULBlT--EXLSB0lFds7Nt6o5zMgZd18Uf8Hv_4Oj0O5bt5Trs-dP4FqwWNS90JiZ_3Z9TBil29TeFIpA6sXHIf1GVGUYzeKHFcrDuMqXmaCOeKknXq_6UNeRoUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/140775" target="_blank">📅 08:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140774">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FE-7JsGXAmQIgM3sFQAOMHZ38M-VmYttHJjgcHGzwgbtUR0-C5TpveqJ4q47WM1pJK-jHM8vSEAa4jO0sp9kjnuaiegW0q_3FZqA-PzQ01oNEFnL4IM52PpQcrV6c_xfrGFQV-yRPXW2x5HDYpQaIFb0ztruPmajgRozmgNbOru8X0qVfdJ4bM6xiDfYd0REXX0lZIBMVubTmlX4wNDxAWcaiVPeEdF52tpC5J5LE49eHFZkocfE6crG2KPQo3sEuKS6fQIeCVBYqk6OAWu2NntAVqgJ7ZUW_4OorPoWJEgb6_Cd_ehgN2msRIsz2AqM_lzuNknmrMr2VScuAhQwXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شبِ سنگین فوتبال؛ چند تقابل با پتانسیل غافلگیری
🔥
⚡️
⚽️
ژاپن و اکوادور شروع‌کننده بازی‌های فردا؛ کنداکتور فرداشب پر از تضادِ ضریب و احتماله؛ جایی که بعضی انتخاب‌ها از همان ابتدا جهت مشخصی دارند و بعضی‌ها تا دقیقه آخر قابل پیش‌بینی نیستند. آلمان و نروژ روی کاغذ دست بالاتر را دارند؛ پرتغال، هلند و اتریش اما وارد بازی‌هایی می‌شوند که یک اتفاق می‌تواند همه‌چیز را جابه‌جا کند. فرداشب، عددها حرف می‌زنند؛ زمین تصمیم می‌گیرد.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و با اولین شارژ خود و دریافت ۱۰٪ بونوس ویژه این دیدار‌هارو رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140774" target="_blank">📅 01:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140773">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
🚨
فوری/ ترامپ : به زودی اتفاقات مهمی درمورد ایران خواهد افتاد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/140773" target="_blank">📅 01:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140772">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
فرهیختگان : دقیقه ۲۷ قلعه‌نویی خواسته حاج صفی بیاد تو بازی تا رکورددار تیم ملی بشه و به محبی گفته یجوری بیوفت زمین که انگار مصدوم شدی وگرنه مصدوم نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140772" target="_blank">📅 00:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140771">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
تعویض زودهنگام محبی، به دلیل مصدومیت که احسان حاج صفی جای او را می‌گیرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140771" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140770">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIeEhF_g__myiahiSsrK3YFasijyTqz_R4iRnpCCf8dKpX6R3Mvnz3iOvehkm9hV4UYx3SdS4yhCTGoHfCKuZnMNye8ZeHOifEj-t2w86k0u4nzbja_ZXVQjjg0sB6vxOYoP0u-FBQ6ie3k8eoyJXWJ8kEeWGCqVEinzhkut6h0LuMWvJAv9daLMIwOPSABlCOCiaEm9-ZdCwiEmORD4xPhE-HtpGg0223EPkkjgCim9t0ReHZltC6VHDx7Jo6dRYRYI3v2qXhRHmdV9UA_AE8XA02NdZ5KklnyspjPDZFkxMB12nn8mGOTeCkspRPx9ou0bCz29z1a8v_Y7S1BeMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
عالیشاه در خانه
❌
دیدار تدارکاتی روز جمعه میان پرسپولیس و گل‌گهر در ورزشگاه شهید کاظمی فرصت خوبی برای قدردانی از کاپیتان سابق پرسپولیس است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140770" target="_blank">📅 23:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140769">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
لحظه گل ثانیه پایانی جوانان پرسپولیس مقابل پارسیان توسط محمدامین قرنجیک
👍
👍
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140769" target="_blank">📅 23:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140768">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c458bfa09b.mp4?token=Uburu5V5im67KYCvU34m9d5lMbD5yMrcukQ-W4nSZZLj3j-NObw7aXOBNN-Id4_EZqtdUtUsF09-D_mpCXMAf73zlENkecGSPICYYcOnp3PkYZWoG1XppwY5cjatRQJtANDu3RnIDbWj42_qkFDPhj916k6yVDqXNL6vvmF-IK-an8F5az0pjYwb6C8hODqC2QlQT6Thh0ITSI_7b0--42eJsK1COlD6Bxp8f20Ek1PXC4paB7P0edqIioY6hzv21heb3LICy6W89jpHpUZzK8FGc0Jzd4KWQEEdIWkc1K0hxC2PAXNwoTjifMyjCKwZ-Xqget32PgwlKpm8-j_MOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c458bfa09b.mp4?token=Uburu5V5im67KYCvU34m9d5lMbD5yMrcukQ-W4nSZZLj3j-NObw7aXOBNN-Id4_EZqtdUtUsF09-D_mpCXMAf73zlENkecGSPICYYcOnp3PkYZWoG1XppwY5cjatRQJtANDu3RnIDbWj42_qkFDPhj916k6yVDqXNL6vvmF-IK-an8F5az0pjYwb6C8hODqC2QlQT6Thh0ITSI_7b0--42eJsK1COlD6Bxp8f20Ek1PXC4paB7P0edqIioY6hzv21heb3LICy6W89jpHpUZzK8FGc0Jzd4KWQEEdIWkc1K0hxC2PAXNwoTjifMyjCKwZ-Xqget32PgwlKpm8-j_MOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بالاخره گداوند رو‌ بردن سربازی
😂
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140768" target="_blank">📅 23:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140767">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ca8ba9d21.mp4?token=u1PdSYqXgmhTYs8CYFA1gOXJTbVn5Ik3tduaNiSqc9yNDGBfbcQhu8pulcr6Fu7R81iV_0U5kEmIjwIvlzjapul_XxFYiDCqHrEri3YBi4obG-i4zwN8-vH0KXpeotye-zlRGWBuKFGBYJsze8p9XV0l1UIwjtorLe750Ivt7eKvcmBe9hioiY1xSbMum16epbggACHd_ATcoPyrMB5tSTYWSMi3A2mKMKQm0Epl27j153OBctaEpWOhjUDHMWWmlqbH0lXTPihK_5Dun6k4qOjBez2mmclwlBX9XkC7dy1Gt1tZ0f3-Ldni_lugo2xScCQqlfRJkSnBJ2SskAoS4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ca8ba9d21.mp4?token=u1PdSYqXgmhTYs8CYFA1gOXJTbVn5Ik3tduaNiSqc9yNDGBfbcQhu8pulcr6Fu7R81iV_0U5kEmIjwIvlzjapul_XxFYiDCqHrEri3YBi4obG-i4zwN8-vH0KXpeotye-zlRGWBuKFGBYJsze8p9XV0l1UIwjtorLe750Ivt7eKvcmBe9hioiY1xSbMum16epbggACHd_ATcoPyrMB5tSTYWSMi3A2mKMKQm0Epl27j153OBctaEpWOhjUDHMWWmlqbH0lXTPihK_5Dun6k4qOjBez2mmclwlBX9XkC7dy1Gt1tZ0f3-Ldni_lugo2xScCQqlfRJkSnBJ2SskAoS4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دلداری خیابانی به بیرانوند قبل خدمت رفتن
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140767" target="_blank">📅 23:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140766">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaciSfQFHqAs5k8jw7B51kISQp_vnPUosTf8cb6PAg6kV9S5vKOMwj8SkPkmHOnRY8ftI5gdtswCznwZIH6iLe5GSVc7eAS2ePCFzcyNdXUTOJXrR1YdiCGqFZxhveiIDZo6q8bFX0TBbYCb3S-RASfz3lWFt3Wt3RMzWomtbiYd-dO0BRI-UZ86VSJtyJsuZkqC25e8mQDrLeobw6gfi0POGhk-t6rBE__WZZ9P7_5vyl8IGeLN9lE-iB7AnJxk9Kz1oT5sDoa6-4NKrZNdXhr2t2_-HNbXU4JWEjbmmO4agGSW1sjcudKGPNZsHkFFAupBNvDD3D6W4UwMQW2xyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🤍
قلعه‌نویی: اشتباهات و نتایج اخیر رو می‌پذیرم و مسئولیت فنی تیم با من است. برنامه تیم رو دوباره بررسی می‌کنیم و در انتخاب بازیکنان، تاکتیک و آماده‌‌‌سازی تغییراتی میدیم.
⚪
می‌خواهم تیم ملی رو حتی بهتر از قبل بسازم و از مردم می‌خواهم فرصت بدن انتقادها رو می‌پذیرم اما تسلیم نمیشم!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140766" target="_blank">📅 23:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140765">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LezaFkQRdWWQkvI3Jmkamzqb5pIDAioGMWRjXlRtlNeIcqbiL42kJ_n2KYQEAoLE8QIBU9jQWWEh318jeMuCJoOgRU3XhBMFBZF-nFPiGJYpWF5euuvgB59RK2Prj0ri6WZMutwnCNf6OIwGJXfaz7HGX5Nt32xP0VcCJBEKpqe4c-oIGtXWcyxCVj_u2i-DPnadTgh2SsegaUzhiew4ceomUU---ttGhpJBwXdGQ1_Tlz-Vulbo_LGAHBIYRroREeQlOlxG6uAB32FqPz0kHdFTDLEUDIEdo6hH4W5LPW5DcWiBAXIRtE67MU1adMTAPNiOg9IPRKxGIu_mohhJRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
یازده سال گذشت
❌
روحت شاد؛ هادی جان 24 ابدی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140765" target="_blank">📅 23:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140764">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
✔️
کریستیانو رونالدو امروز برای سومین روز متوالی در تمرین تیم ملی پرتغال حاضر نشد و طبق گزارش رسانه‌های پرتغالی و اسپانیایی، اردوی تیم را ترک کرده است. این اتفاق پس از اظهارات ژسوس درباره غیبت رونالدو مقابل دانمارک رخ داده و برخی رسانه‌ها احتمال بازگشت او…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140764" target="_blank">📅 22:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140763">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
🚨
فوری/ ترامپ : به زودی اتفاقات مهمی درمورد ایران خواهد افتاد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140763" target="_blank">📅 21:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140762">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامپ: جمهوری اسلامی‌ هیچ پولی براش نمونده؛ برای همین فشار آورده که توافق کنه و رفع محاصره بشه. وگرنه چه نیازی به توافق دارن که پیشنهاد میفرستن؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140762" target="_blank">📅 21:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140761">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
🇵🇹
👤
رونالدو اردوی پرتغال را ترک کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140761" target="_blank">📅 21:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140760">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSpNb2FfDURsyQqelBvTiUjyDwLmT-m3HJauzFBaGdQAWmE-RRrH1avVQJrIvbXLztWCZRVQ49MthBaNtJKW66WF_XR3mEzbQ57rUt27BjQwqnRHAQcD7loTNEpJccDLlcShqglSTxpF8HS5eO5396zuEHkMGcRFGVsAI0LVaE40qxXugq0cfJ7uVaVtau-yQ2qx26qNq-ZrIBBhtfMrxrpmTGb_TgWvYbQXTNRkBCSElQCp9nzAjGjPtnL_86fybAUQfI5kMYhtrCIEu4k8LyNQWbaOqT5lfcR7zGPW8QG-CV45nymo9wmnZWtacO8enfyzpjoT3OlOPO06QQalmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇵🇹
👤
رونالدو اردوی پرتغال را ترک کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTime
s</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140760" target="_blank">📅 21:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140759">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vntubhx1h6NLrgKCZZFeh0C-qmFTgNI2k5odW9js4MlRmO6DpUGjJPGJdsnnOMgZWD2mXBY0ZKhA-IrnMJo4gKXsFaS_5QzDDb6S1aDnJzdDAsf1dzEXNLUyTUnbdQYryAiqVOQ9wY6Lgl_1L5YqCCGCgvAaQ8iPz4yyhyEU8Re2SgjeY-H2oydvEsg7D_wlTAUPdCl4aeIjWN3QsovJpeLn4quXHTwK3Z_TMZRKKcH-c1wVjOJHAvRrSfNQGTrUj4QsVys3zDYdDaW7Vf-zBRpirFxYQyg8SfvCepb1GxwxNnF2S2SApPBYjH34ibPARRZ-PAPEacjORrzEzBnfRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نزول فوتبال ایران به رده ۲۳ جهان
▫️
تیم ملی فوتبال ایران با شکست مقابل ازبکستان و روسیه، در جدیدترین رده‌بندی فیفا یک پله سقوط کرد و به رتبه بیست‌وسوم جهان رسید؛ جایگاهی که در سه سال اخیر بی‌سابقه بوده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140759" target="_blank">📅 21:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140758">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRum4kaqhURwfaXJL35BHczftPe2ehUyFUyIsgayXGZ-w1Mlp9vss0mP22AuCmdN7MkRATX9FpgAumYq_0optA-EIJfRDMPY9DkVUT6fHGkVCl3V0HzLmsdkwwVojHfA8Rdd66vKPhIO2_RI3xWKRXfV27K1_WR3TCdLCek-utlR8RB-1Zaa1Tyg_B51jOMCO2-Uc96qpw9qVBCq0pL6wku_95rIKUaWq3xyXa05-lwOJX-vZ5U3Lw1HBUxEQkYh5RO6G_IFPJm_EoaX14B-xsiWABH-cInPHTHRhmMXO6UAP25FXkciepOxjHtavk0vnmKpvKKbK6VhQSYk93nQ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🩸
لیست مصدومان باشگاه
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140758" target="_blank">📅 21:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140757">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
مذاکرات مدیران باشگاه پرسپولیس برای جذب فرهان جعفری ستاره ملوان ادامه دارد و اتفاق خاصی رخ ندهد این ستاره به زودی راهی پرسپولیس خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140757" target="_blank">📅 21:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140756">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKK0HvL4SFWvKKUSveDagqVfQ2FsbDbGsrWShD4jgobkBFQE1aoEZjfvjo2zIQXJrscTZj6CSCGqCvImnmxfZlZRu80bDwJSKyzLQLbf2Bm5KNAODqgSIVMNZ8BAvkKUgZ3M_GeWUPAqsvqDS9sKQNZR6N3fIw32HVR24at4P4TkMurV41hsOMIQBkibyHsUz3Nmvsu83wXZgeRWBZM5zXs67Vtf63CFoYP2wS4ianp7jWnH0GMy3ekRmKyuWsIG7D4bAcvueM9F6EdTpxjwRblGH101e12usxajLmsUK6nCMIAdc8ETeE5IkMCPXIQAOg8N35gkT7h5WBTCkVs-cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
وقتشه پوکرو حرفه‌ای بازی کنی!
🎰
اگر به دنبال تجربه‌ای متفاوت و پر از هیجان هستید، بخش کازینوی وینکوبت بهترین انتخاب برای شماست. از بازی‌های کلاسیک مانند بلک‌جک، رولت و باکارات گرفته تا صدها اسلات جذاب با جوایز بزرگ، همه چیز برای یک سرگرمی حرفه‌ای فراهم شده است.
🕹
همین حالا وارد دنیای کازینوی وینکوبت شوید و هیجان واقعی را تجربه کنید. شاید برنده بزرگ بعدی شما باشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140756" target="_blank">📅 20:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140755">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxxGlNGiBCbOoqJShMZVYd4fK2HIPBlC0k0NfkX9FAdJmEybq5kBIbND7UD3pbIFZ31Ar38yZrJw8Rho9cqwpHO-a2WEGn4DsBZXCDlEfSdy38xr8GgFVjB0Zv_RgoDhh0jS7MuvEjs_CqWwgBinvHH9A64nggCA5nGijfLaMj37ygXWgGTAqkPDsJw8yNA4IKjN8RPkE_hDdN7jrHSewyDVt916WfmlI3mmyuUE0cZE4HfwFvt9mAnfcv7pxjD_Iq8XdE6WHw9LMRuHQxbuNogsvAs-uCwyoRNVdYj5nGoi4RF9xsubK1y38SwM77yNDzocN77WOaHRCOz6LKGqyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
والیبال به میرزایی رسید!
🔴
با حکم احد میرزایی؛ رضا صفایی سرمربی تیم والیبال پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140755" target="_blank">📅 19:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140754">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
تیمداری مجدد پرسپولیس در والیبال پس از سال ها
❌
❌
تیم والیبال پرسپولیس تهران در گروه چهارم رقابت های دسته یک کشور با تیم‌های طلایی‌پوشان ورامین، نیروی زمینی تهران، بوعلی قم، مقاومت شهرداری تبریز، سروقامتان ارومیه، بنیس شبستر تبریز و روژمیوه زریبار مریوان…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140754" target="_blank">📅 19:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140753">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔄
🔄
هوشنگ نصیرزاده: پرسپولیس با شکایت از آسانی به CAS وقت خود را تلف می‌کند هیچ سندی علیه آسانی وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140753" target="_blank">📅 16:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140752">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">⭕️
⭕️
⭕️
خبرورزشی: مرغ حدادی یه پا داره بردن شکایت آسانی به Cas همین و تمام
⭕️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140752" target="_blank">📅 16:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140751">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
تعویض زودهنگام محبی، به دلیل مصدومیت که احسان حاج صفی جای او را می‌گیرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140751" target="_blank">📅 16:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140750">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
❌
هفته هشتم لیگ برتر در آستانه تعویق!
✔️
✔️
در صورت قطعی شدن برگزاری سومین دیدار دوستانه تیم ملی در فیفادی پیش‌رو و انجام این بازی در ترکیه، احتمال تعویق برخی مسابقات هفته هشتم لیگ برتر وجود دارد.
✔️
✔️
در این صورت، دیدار حساس استقلال و تراکتور نیز ممکن است…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/140750" target="_blank">📅 16:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140749">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⚽️
گل های بازی بانوان پرسپولیس چهار - صفر ملوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140749" target="_blank">📅 16:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140748">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d02c1a357e.mp4?token=tlbrpNI9nNykSNISqHv1CcqVzgcI9gSW78ogRjbJoar8kNU0H5Uo522WcxAhaPuElmvTnyxr6qeC9ij7Qw43vrJq3TnP6ZJIzzkhTd5h8LTrywT0ErD3x9gl7DoeclBkKlICbq8w4gixLNQIEmkD5POu2lRRaXP3OaljDaA7SqDD38KF25wXEDOERk7_MSKeMA1oxJNiKWyuKEi0Wr8KwTcuWU1terGdN1rP8yi0MMIcq_SL6nTCO05W9VLURjg7W9chQBDCIsxUN633b_xQobZICSkwBxzyHOPxrcJ7WTOdCqiF2rWwd_B69oJY7ev4NA1YnO_p_NSjH_mrvE6cUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d02c1a357e.mp4?token=tlbrpNI9nNykSNISqHv1CcqVzgcI9gSW78ogRjbJoar8kNU0H5Uo522WcxAhaPuElmvTnyxr6qeC9ij7Qw43vrJq3TnP6ZJIzzkhTd5h8LTrywT0ErD3x9gl7DoeclBkKlICbq8w4gixLNQIEmkD5POu2lRRaXP3OaljDaA7SqDD38KF25wXEDOERk7_MSKeMA1oxJNiKWyuKEi0Wr8KwTcuWU1terGdN1rP8yi0MMIcq_SL6nTCO05W9VLURjg7W9chQBDCIsxUN633b_xQobZICSkwBxzyHOPxrcJ7WTOdCqiF2rWwd_B69oJY7ev4NA1YnO_p_NSjH_mrvE6cUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ملی‌پوشان فوتبال ایران پس از برگزاری دیدار تدارکاتی برابر روسیه وارد ایران شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140748" target="_blank">📅 16:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140747">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/140747" target="_blank">📅 15:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140746">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ca-R0qJQE-X-MPGdhwNOBeKSKt1PW2kT66GHyEgbHtY8nm1MtPQQy8wZa9r9pbH7EpO4zz2MW3ypFs7-CCqsUX1LRVawwuLr5Q9Q6RyNLqIriJpJL-Y0zUlB5l8BAWptr5beV0AM3F57HBFssyXCHKck-JLhIXoA-JKCWCeUSxEtJ0IdtazXLgxnHQuZBIjUxgCnQM8fYTK5vyAgU5i6sUSE6U0tlng470iVtotVv1kVqUWXPxSxBX0_svG9MyL_nS2EVoBiHD7vZ-F-9Y_OFHZz2JcUoPMHBEn_pP72iAovfaH-TU9_a5f4LrLwZzbET6vtXuUzjZdxAFUyQ_3elQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
اگه درآینده جنگ رخ بده و بیش از 90 روز طول بکشه بازیکن میتونه یه اخطاره 30 روزه به مدیریت باشگاه‌بده و بعدش‌هم توافقی قراردادش رو فسخ کنه اما اگه جنگ کمتر از 90 روز باشه بازیکنان خارجی باشگاه‌ها حق هییییچگونه فسخی ندارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/140746" target="_blank">📅 14:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140745">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/140745" target="_blank">📅 14:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140744">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⭕️
⭕️
ابوالفضل رزاق پور مدافع چپ تیم فولاد: از پرسپولیس آفر دریافت‌کرده‌ام‌اگه دو باشگاه به توافق کامل برسن درنیم‌فصل راهی این باشگاه خواهم شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140744" target="_blank">📅 14:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140743">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔄
🔄
عملکرد یاسین سلمانی در دیدار های تدارکاتی  امسال پرسپولیس: ۸ بازی - ۴ گل - ۵ پاس‌گل :  پ.ن تارتار به شدت راضیه از یاسین   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/140743" target="_blank">📅 14:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140742">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
بازگشت دنیل گرا به تمرینات پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140742" target="_blank">📅 14:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140741">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mURZ6sFLO2ZgQroitFh0G49Xr14_GoDyQ-P_D5pJH7fqF_Ay20Y7289JWnjEOzr0yL2Pf_7Wp_J6xnYDSvQlP4A3-HkLmSOvJ0stT_pGmwErk-oCibGiKr-6v5ZFN4pvvEXHkLIFggG0jbmpx8JP07oytd4WdV5IGaSx-c0098VJhJqSRzeNILxQGv3yws8_os-KPngfAnAuCBb31ecVkn6GsPiu9ryZtfYv-E0XsJZOGCWAMsRFybwoxBzU1qNvj8suX6uy5U8OmMgxjN5StSU6tZC1fWa4l584KV7IaG-FhfI64ktg7xWxKFULTRngtEDZ2ihVYlD_KNrzVZky1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎲
هیجان واقعی همراه با کازینو
اسپورت نود
🔵
کازینو آنلاین
اسپورت‌نود
، هیجان واقعی با بردهای بزرگ همراه با انواع
بازی‌های کازینویی،
🎮
انفجار،
💣
رولت، بلک‌جک،
🃏
اسلات و بازی‌های زنده
همراه با پشتیبانی ۲۴ ساعته همین حالا شانس خودت رو امتحان کن!
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140741" target="_blank">📅 13:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140740">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‼️
آخرین وضعیت پرونده جادوگر فوتبال؛ تمام اموال نامشروع مصادره شد
🔄
🔄
رئیس کل دادگستری استان البرز:
❌
❌
در پی دستگیری و محاکمه شخصی که در محافل ورزشی به نام «جادوگر فوتبال» معروف بوده است؛ وی به اتهام «فعالیت تبلیغی انحرافی مغایر یا مخل به شرع از طریق ادعای واهی و کذب» به تحمل ۵ سال حبس و ضبط اموال نامشروع حاصل از جرم محکوم شد.
❌
❌
حدود ۶۶۰۰ دلار، بیش از ۲ هزار یورو، ۸۰ سکه تمام بهار آزادی، ۳ شمش طلا و مقادیری طلا و ۲ دستگاه خودرو تویوتا لندکروز و مرسدس بنز از متهم کشف شد.
✔️
✔️
متهم هم اکنون در حال تحمل پنج سال محکومیت حبس صادره است و کلیه آلات و ادوات مختلف مربوط به سحر و جادو که از متهم کشف شده بود هم معدوم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/140740" target="_blank">📅 13:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140739">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
🏟
بازسازی زیرساخت‌های پرسپولیس
✔️
✔️
رختکن‌ها، چمن، نیمکت‌ها و سکوهای ورزشگاه شهید کاظمی بازسازی و بهسازی شدن. بازسازی کامل استخر درفشی‌فر هم تقریباً تمومه و قراره نیمه دوم مهرماه به بهره‌برداری برسه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/140739" target="_blank">📅 13:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140738">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🤩
⚽
شاهکار پیمان حدادی در پرسپولیس؛ درآمدزایی ۱۳۶۵ میلیارد تومانی از پیراهن سرخ‌ها
❌
پیمان حدادی، مدیرعامل پرسپولیس، پس از پشت سر گذاشتن نقل‌وانتقالاتی موفق و پیروزی در پرونده‌های حقوقی باشگاه، حالا با یک دستاورد اقتصادی قابل‌توجه مورد توجه قرار گرفته است. بر…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140738" target="_blank">📅 11:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140737">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ya2exjCh1Ar6koNXm7MsxJXSavk4VG7laMIj4dVfoHeJUUv33xjsThlb_vPSmkiaoUXhko1XPIQDXTC-mvmNqpw2Yh8_DmGTNiL6Brwzu_RLbK9QYCIEMCR49QfFq8odBXcAq9t9dhdt3Dm_9fblTdgk6U1edqsKY73WjM3NiR1w0ORsW3-pb9L9B4dDydH90gOqlvJE5TEnofgD6c7Rle2ml3NkrX14NFfjpQSG5m8ZWMUodo_ZILATvbAR09GHfflAk_S4ctpTNrf3gUUv5YgI5sQr4CxmnMnhZIQEbB_0Fq90_rZTvTVvApIbklXvLKZ_RdKjQsdwejeOOZUN9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140737" target="_blank">📅 11:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140736">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3297ba87bf.mp4?token=BX1yMjNn5HHqMK6Nu-Qk5HD73i6ef6QMN1uogrQxWWfpL52HugI3tRejdRg4WMmSd3lnZxwAxBGdlecYXCBwUKoUx2LepO3XwKX1OBmwH0lsqpKUac7GSFvm7beZI5cYvuaIP4OeGCbyxfCi3qgrz34A9jMifOuBjnNYgeMx775MYATY02CPJIq4xjxLa8S3V4MLbng7mc0B3HN2m9IQueXoCLCckpoGFRbX4NXvku1eGtjPBte2MZx8WKiAu0-U5yH2hpEeFHELan2inFtp9x3NFsgOQGjxFvGSVSnuIRnxHbruYAD23PCTBbg-FDQegX9YMLBSM6tHKn04bpzHMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3297ba87bf.mp4?token=BX1yMjNn5HHqMK6Nu-Qk5HD73i6ef6QMN1uogrQxWWfpL52HugI3tRejdRg4WMmSd3lnZxwAxBGdlecYXCBwUKoUx2LepO3XwKX1OBmwH0lsqpKUac7GSFvm7beZI5cYvuaIP4OeGCbyxfCi3qgrz34A9jMifOuBjnNYgeMx775MYATY02CPJIq4xjxLa8S3V4MLbng7mc0B3HN2m9IQueXoCLCckpoGFRbX4NXvku1eGtjPBte2MZx8WKiAu0-U5yH2hpEeFHELan2inFtp9x3NFsgOQGjxFvGSVSnuIRnxHbruYAD23PCTBbg-FDQegX9YMLBSM6tHKn04bpzHMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
۶ سال گذشت...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140736" target="_blank">📅 10:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140735">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✔️
✔️
مصدومیت دانیال ایری از ناحیه کشاله ران پا بوده و مداوا روش شروع شده تا بزودی به تمرینات برگرده؛ اما بعیده به بازی صنعت نفت برسه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140735" target="_blank">📅 10:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140734">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
🏥
دانیال ایری در بازی آخر تیم امید مصدوم شد؛ MRI کشیدگی عضلات لگن و بالای کشاله ران رو نشون داد. کادر پزشکی پرسپولیس هم درمان و فیزیوتراپی رو شروع کرده تا هرچه زودتر برگرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140734" target="_blank">📅 10:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140733">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
❌
گروهبان قندلی: از بازیکنانی که به آنها فضا دادیم اما نتونستن چیزی که مدنظر ما هست رو انجام بدن در اردوهای بعدی استفاده نخواهیم کرد
😁
✔️
✔️
این بازی ما رو یاد جام جهانی انداخت و سطحش در حد این رقابت‌ها بود. برای ما بسیار مفید بود هرچند از نتیجه ناراحت هستیم…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/140733" target="_blank">📅 10:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140732">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
❌
گروهبان قندلی: از بازیکنانی که به آنها فضا دادیم اما نتونستن چیزی که مدنظر ما هست رو انجام بدن در اردوهای بعدی استفاده نخواهیم کرد
😁
✔️
✔️
این بازی ما رو یاد جام جهانی انداخت و سطحش در حد این رقابت‌ها بود. برای ما بسیار مفید بود هرچند از نتیجه ناراحت هستیم…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/140732" target="_blank">📅 10:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140731">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7PZYGzIXfdiEV0VExtW1jkQcYClpPlAZIVM_kPShaW6rBGRR1YJ7XnfBG50pTvgoCnnq3kuYAjlI9IDsrrmRTVJUxxQKeMrQkLbGJcFjA18JdDUiVxzQl0QwJkZaSOg9yeTp8RWIybGFefYbdPrNnWPChmV2yVCkqx-rGSw5BUSS8Rqe1ABshMKB5OdRkgb1AUtD-M3wjKwDch3LbcrgCSc742hORnHtplmAmz6wcK2Zro8S1t-qf7cUw0uUyFK62fS2NWbDJsYMlSt9yn7XIMH3dmlOueOHLCXMDXC1yEG2eJUFbXyDse5I9aRDy-N02xveDndnvUtUkhu_iAJgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
حمله تند روزنامه‌های ورزشی به قلعه‌‌نویی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140731" target="_blank">📅 09:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140730">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_766-04C9iSKOW6MJdyXA4_AwsDepwDKdpu-myk82_OdC5Q78N-Y76a7SnLVwoolRZkZk2QyFxwThZgLABvq50kMjbMZcx_7TPvug5-5jMJo03vO382JHlmSQyrDJujMoV7Gu5EdPMRLtcOJr_rg4Ycqx4G6pyj3hXhUpeEiPQ1J-1CXP3IdnD3uzdevGaDJC9SPvi36XFXR1RPpF9SOtYV_2gIu1dhT0ejKAo0WI_v-60_p44Fq_ZBQ-tU00kQXsjc1JueRsS65q-XQ6szW84MDioQaZC0rdetDxQwiXc-NRpJi6lbP2L8EAgtxYr0yRVvbDjEsTLjOOwpMH3e3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140730" target="_blank">📅 09:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140729">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5wo42YPwL3985CKkUcQztd2pyAo0lspUGfEKv9hIHD3T4aPtPXBG9kmqtXNWJTdtsY4TzzcLAlLi3ckl83jx6-khNADzazsQDo-G--jgLP4Og78Bp1GLmaIi7m-AR5xoLibKEWnTUv1g_Gwur6YkgOX1y1-oBmzTUoYtkjyjne2iqm4-SrzarsJsifogdFeXx6eRvNzwubqK-30DnvsxRYfETxC8kveqwHw04cKartKAewqQiqYpOkOjoaCozFarvrxZUNv01zLH6Ff0a0kOpU9pvkcFdtNx99ZZL6y0VZ_4FTkkhrEp6CWF0ieEEFr5TGeTQWQZZPUfkMOWw_p4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/140729" target="_blank">📅 01:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140728">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f33OFAG1IldG98t7zWmbwvVM5_YGvp7Aq4tVk9z--wjlXcC4N0jspnYcslG_m3MzEBSeaYR9XLf1OW0rFfGl9Ciwu87qE5n0uqQo-rD2vV-tI2soj9XWtBwZjjzjYYfPK81Gd_yBwZWolRNCNsxzpp2iujAYU4jhgKUn8mm2LPkM24GGooBoiTKA8pZzCW9WvxMe7zb9B5QuQLXoxSJv8S74GDzzs-fw-LHCll5b5SXdvW2Otqo0m_iaFMmIaQ3iXR1Z5x8j3fWFdhzPcGzdrPzgi9j-Ca6E3TCIQMb6j0RcYATPzPCePkAoTFkJUukrbpNH6I8R-YJW2cL5CHreXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
در تاریخ بنوسید تو فوتبال‌‌فاسد ایران قرار بوده استقلال جام رو بگیره بجاش ٧۵٠ هزاردلار طلبش از مهدی‌تاج رو بلاعوض کنن‌‌. پشت‌پرده درحال انجام بوده اما مخالفت شدید باشگاه‌ها این معامله کثیف پول با جام بهم میخوره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140728" target="_blank">📅 00:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140727">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
#فوووووری
🖍
دانیال ایری به دلیل مصدومیت در تمرین امروز  سرخپوشان غایب بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140727" target="_blank">📅 00:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140726">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🏆
🏆
نتایج بازی های امشب:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140726" target="_blank">📅 00:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140725">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5oL4kFt3gf3VhPSOtPNxdNDRiBKXMrkRSlTVCePSd2ap6QqtOsVCsSUs_xZ17McctBudZpMOa3PG6pQw3fDJ7abIW69YzrWB4pRF9F0_wTkaPXoJ7U8ADm29tKteMRtsjTxt2M1wvi0xPyZHCD9kWmrI7vYWhXT9MWMK7FYuhksl3pUYsaFZ1P638W0HeS3gUfm2XvOVbXBOg1K87m6m0Ac0Bb1BuV0qBx8bJk4shnEkp-beO25H1AJRbA2QzebDzPhw5vIJ-djBCwUo_QVcFyINpPwXuv73jsXJ5SMSLKAcwFoZXEso8sHhUZUw_1gFEzaRg-lrKLitVo83G8yRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏆
نتایج بازی های امشب:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140725" target="_blank">📅 00:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140724">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♨️
🤩
🤩
افشاگری باورنکردنی میثاقی از یک ایجنت، عارف آقاسی، پرسپولیس و پیش قرارداد برای یاسر آسانی!
🔄
🔄
محمدحسین‌میثاقی: پرسپولیس به یک ایجنت ۱۰۰ هزار دلار پول داده بود که عارف آقاسی را به پرسپولیس ببرد ولی این بازیکن را به استقلال برد و الان باشگاه از این ایجنت…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140724" target="_blank">📅 00:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140723">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNSbctMoWxrv9mr8-C6R-pMqWaLgCPdqzcdpRL3qrZzvqDAw2IlfKQWhXe5F2oiJ-P2kHJL3Os6UWqXcwcjSRL8N1lEKsvB9zprZJbEXcSfV6z7UyaPa-8jsD_EDryv4rZ-dsO88jqEUdmR8WmpAHBKewuXGJgOUTK4yfhvUtNCYEHuUDgnt7Rlhwtwn8m62LknW92g1dJCGeFrKW8k2vAStU-Q1fiuGuDsSdv8zXLyy4FCLTJ4bPEx9y6axt56ssfhx_EG6CRoqocE50MI1PoT4ipiV90wRolr3DZoYaF8irXcGaGGuSURn-YuwPHuErZJ4u-eYEdvZoezwTTRA5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🔻
مدت قرارداد احتمالی جدید نیازمند با پرسپولیس مشخص شد
⚪️
⚪️
پیام نیازمند گلر پرسپولیس که اخیرا مذاکراتش را با این باشگاه برای تمدید قرارداد آغاز کرده طبق شنیده ها به توافقات نسبی دست یافته. طبق شنیده‌ها قرارداد جدید نیازمند با پرسپولیس 2 ساله خواهد بود و گلر فعلی سرخپوشان قرار است دو فصل دیگر نیز در جمع پرسپولیسی‌ها باقی بماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140723" target="_blank">📅 23:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140722">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">📘
📘
در 14 بازی آخر تیم ملی با هدایت امیرخان فقط سه برد داشته که اونم مقابل گامبیا، تانزانیا و کره‌شمالی بوده
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140722" target="_blank">📅 23:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140721">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5fr_rvgLRoKbt8jfBPNba7tzVBvfMsqvDh3iPPwpR0eDXQr2y8K4jPAnJjqP2lG7Sg3z0wNGbdR00ZaFyMazEAsBoTnQSn1cmd8Zqd3FzQHe7hFL5rn5JTnYtw5ro16Oe6lZgx9IPxSLlVzGJJBDGODvbSp2KpFITn4WHd_0TUJ6fph8QHVNeZqyA_ona2vKiN-gSBCmwQrHDelVeO0uEFehwUwK3fAWnN20lelEkvbUAUoux9BssZ6PK-7wCzpRJg6bQVkWSqRnlOJ_t-C8EOWPB6c5vpCbm5kyDob6IkEHdrviAVb-Ak4ztxaabSWPWmJ1knb-OqlGPRaeTOqqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
قرارداد ۱۳۶۵ میلیاردی پرسپولیس برای تبلیغات البسه
✔️
✔️
باشگاه پرسپولیس قراردادی به مبلغ ۱۳۶۵ میلیارد تومان برای تبلیغات بر روی البسه تیم‌های خود شامل بزرگسالان، رده‌های پایه و بانوان منعقد کرد.
✔️
✔️
این قرارداد برای فصل جاری جهت اطلاع عموم بر روی سایت کدال…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140721" target="_blank">📅 22:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140720">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6Oc5RIBJkEEC2v14LE828JI5RXeeQx4FQy-ELxtAy3p82QEIMXOoG1rsqoGuEauOAa_TDrz9gx9REoICwr6Q2SPDP5J_za1U3HRqaGiQ5aDpKX26KA4SAd3H07oSds-YUlmlx0I_QleJ6D90hyA0UKdEp0RGEjxlUHl1htutVSu2o6h5Cb75YoDprAz-QRP9UGSNnyANiTOrGHof4RDHH0K6khAvw_dJlpmGeWMC4v0bhq0kkjRnoMGsxeqNX3sE2KAMEOJAVkqUf9wgAbTtFalPv3CBxee8p0rVQgvfcUaLOL8Hh7cYsBQS2mAWpYLe14M4B37oGoaQvKECCaRvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امشب اگه پیام نیازمند نبود، فاجعه بازی انگلیس تکرار میشد؛ تفاوت دروازبان درجه یک با دروازبان معمولی اینجور جاها معلوم میشه
❤️
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140720" target="_blank">📅 22:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140719">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
لباس پرسپولیس عوض می‌شود
⚡️
⚡️
باشگاه پرسپولیس برای فصل جدید رقابت‌های فوتبال، در آستانه تغییر برند تولیدکننده البسه خود قرار دارد.
⚡️
⚡️
⚡️
برند «یوسف جامه» در فرایند مربوط به انتخاب تولیدکننده البسه باشگاه پرسپولیس، توانسته نظر کمیسیون معاملات باشگاه را جلب…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140719" target="_blank">📅 22:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140718">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1880075a0d.mp4?token=DG4o3gV8p5VNTwj47c0jY1QGIGlsNkC3bNMX_O9dxRvOMnpNMGKh6ySJygcBnwZMbLPlVj3ay85Hy6pfKudG2e-0lRVc3aOXp4W77Azpj1wU48MXFnQmzMP2hyzilCcuKu96yZto6Ho1vnBqfLVNeKx4xcj-HPA98UmQzbM3Uqvt5rFZeHrNKgtsa-knsxNSrtTUal2pb7XkMcHkPpfRUJJk1EJH_PHx3cDEkQcbI6gNgetZHIBjKPhDHKWOtjQceREBr3gA8VOKEzT53yzFF4FheO-e_XvoEUQj5PIxvsP4-kq8ScRTk7bZGzdRFl_twxg9YZ6NS2uzbsXYZ-xTtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1880075a0d.mp4?token=DG4o3gV8p5VNTwj47c0jY1QGIGlsNkC3bNMX_O9dxRvOMnpNMGKh6ySJygcBnwZMbLPlVj3ay85Hy6pfKudG2e-0lRVc3aOXp4W77Azpj1wU48MXFnQmzMP2hyzilCcuKu96yZto6Ho1vnBqfLVNeKx4xcj-HPA98UmQzbM3Uqvt5rFZeHrNKgtsa-knsxNSrtTUal2pb7XkMcHkPpfRUJJk1EJH_PHx3cDEkQcbI6gNgetZHIBjKPhDHKWOtjQceREBr3gA8VOKEzT53yzFF4FheO-e_XvoEUQj5PIxvsP4-kq8ScRTk7bZGzdRFl_twxg9YZ6NS2uzbsXYZ-xTtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
درگیری شدید در بازی رده نوجوانان لیگ تهران میان تیم‌های کیسه و شاهین!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140718" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140717">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✔️
پرسپولیس هنوز هیچ توافق یا مذاکره‌ای با اندونگ انجام نداده/طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140717" target="_blank">📅 22:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140716">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✔️
✔️
پایان  بازی روسیه 2 _ 0 ایران
✔️
✔️
یک نمایش ناامید کننده دیگر از تیم ملی/ با «مدل بازی متفاوت» هم باختیم!
❌
❌
در حالی که امیر قلعه‌نویی وعده داده بود تیم ملی با مدلی متفاوت برابر روسیه به میدان می‌رود اما نمایش تیم ملی همان همیشگی بود؛ نگران کننده و ناامید…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140716" target="_blank">📅 21:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140715">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66e4f7259.mp4?token=NEzzy4_HetEOzxoYnQ3wWlZ3fEGlOxe0mzNZ3a7kh4uRC5N3NlNS-VwhcfZsLrFRDdv4CpGHneTjuJI-DMZFwOu2B6mmAQXXW3pJjwAjw9O7Y5jiA3YPM3J2QTVzP9gWn0rXjb03EgZu5Wstz-t-AJeJbSMBa-xXUvDvxoBfnfQKb-8qr3fSaxJZ6v3RjG1nzTL7lVTykuUcdnFjO7cOTfosr5xDwb8-o3VopYKEOymUXmVjLQ_OKslXSO_3YD3p-EH_tFjDZlnr_t6hHwldJobRzvKDQRQUATVWtmoaFOFztc2sflAjK_ECxw9asFvOUHiu4SLkBn3Issk1beWugg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66e4f7259.mp4?token=NEzzy4_HetEOzxoYnQ3wWlZ3fEGlOxe0mzNZ3a7kh4uRC5N3NlNS-VwhcfZsLrFRDdv4CpGHneTjuJI-DMZFwOu2B6mmAQXXW3pJjwAjw9O7Y5jiA3YPM3J2QTVzP9gWn0rXjb03EgZu5Wstz-t-AJeJbSMBa-xXUvDvxoBfnfQKb-8qr3fSaxJZ6v3RjG1nzTL7lVTykuUcdnFjO7cOTfosr5xDwb8-o3VopYKEOymUXmVjLQ_OKslXSO_3YD3p-EH_tFjDZlnr_t6hHwldJobRzvKDQRQUATVWtmoaFOFztc2sflAjK_ECxw9asFvOUHiu4SLkBn3Issk1beWugg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📘
📘
در 14 بازی آخر تیم ملی با هدایت امیرخان فقط سه برد داشته که اونم مقابل گامبیا، تانزانیا و کره‌شمالی بوده
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/140715" target="_blank">📅 21:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140714">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✅
✅
سومین سوپر سیو از پیام !!!
⬇
دمت گرم واقعا پیام جون
🔄
یه تنه جلوی آبروریزی رو گرفتی سلطان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140714" target="_blank">📅 21:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140713">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGeHuQyU2Gw54XtiPa95O2hbbhO_yFl4LwontNcnDXv8o30_FMShklmHOLnRKH9qLRGlTlLvRjoWbHLhGeiZImdvfxJsRASECrr72NLrYtfXJN2fFYiBve1dSvQJ23ja4ZDXFODrqkeTq7smFl_9EcU6byYnwPjrwW5qttmL1sV3kK1j10HyOgSIcXHvjp99rMh8CGRVy3BUCDGNZ2ZGSg5ptDVuWWH0-1K0Vaaj1RTF84BEl_6uGnGvckyogpf4G0IG7wx2a9yUUMaNlwF1ktoCXwTcI-rlKiX_jFBueWhV1qaZeOdLHHt6h_EGGoTf2tIWwn50guH-kuLuEGWuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
🔄
تصاویری از تمرین امروز تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140713" target="_blank">📅 21:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140712">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
✅
آقای قلعه نوعی با ی خداحافظی کل ایران و خوشحال کن .....سومین گل هم از ازبکستان خوردیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140712" target="_blank">📅 21:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140711">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
❌
با دعوت احسان حاج‌صفی به اردوی تیم ملی این بازیکن در صورتی که مقابل ازبکستان و روسیه حتی یک دقیقه بازی کنه رکورددار بازی با پیراهن ایران خواهد بود و از علی دایی و جواد نکونام عبور خواهد کرد
✔️
جواد نکونام ـ 149 بازی ملی
✔️
علی دایی - 148 بازی ملی
✔️
احسان…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140711" target="_blank">📅 20:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140710">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⭕️
⭕️
⭕️
خبرورزشی: مرغ حدادی یه پا داره بردن شکایت آسانی به Cas همین و تمام
⭕️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140710" target="_blank">📅 20:39 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
