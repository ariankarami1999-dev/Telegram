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
<img src="https://cdn4.telesco.pe/file/N7lJ9EI_jdFitQWXEPdibUyRAVMAeNim7BDa4HlVnaduZVN9JEjNSMsuppOH79jtD5VOFJYjCH6GzY7aSjxP6j9077XOkW9pmc2j118ruF85M3NUpeevv1t-GDBcdAqbei-VWcncXoy3RlfsGmbAZi2gzWxX_qxpUvZbfLV-zkVGp2hM9v9UDlfEWt5nGRhNRY-BJptvrBkbhK2mAVBvTs7ca7JxIcCVbud0N8jGNv7rat7jC-Yf_3IK6qZ3fTWupxQAhevn6bP4PE2_OW5uGHCkig4TdTCL2Vs2lNnIQHOS31vZDGKUVlb_qgLR7mPBoXD904mAXAcQZ2muil1ryQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 12:21:40</div>
<hr>

<div class="tg-post" id="msg-136792">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">➡️
➡️
➡️
➡️
⬅
تارتار به دنبال پاکسازی پرسپولیس!
⏳
💬
مهدی تارتار پس از بازگشت از ترکیه قصد دارد چند نفر از اطرافیان باشگاه را به دلیل لو رفتن ترکیب تیم کنار بگذارد.
⬇️
سرمربی پرسپولیس به چند نفر مشکوک شده و پیگیر این موضوع است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SorkhTimes/136792" target="_blank">📅 10:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136791">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
🔴
ورزش سه: هیچ کدوم از هافبک های پرسپولیس بازیساز نیستن و دو خرید جدید پرسپولیس در این پست (لطیفی فر و پورعلی) بیشتر وظایف دفاعی دارن. پرسپولیس اگه پست 8 بازیکن نخره تو شروع فصل به مشکل میخوره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SorkhTimes/136791" target="_blank">📅 10:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136790">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
❌
امیر عابدزاده که به تازگی بازیکن آزاد شده و احمد گوهری از گزینه‌های باشگاه برای گلر دوم می باشند ناگفته نماند وضعیت اخباری همچنان مبهم است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SorkhTimes/136790" target="_blank">📅 10:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136789">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🌀
🌀
🌀
پرسپولیس خواستار جذب مدافع تراکتور شد
🌀
باشگاه پرسپولیس با ارسال نامه به باشگاه تراکتور خواستار جذب صادق محرمی مدافع تیم فوتبال تراکتور شده است.
🌀
محرمی پیش از این سابقه بازی در پرسپولیس را داشت و از همین تیم راهی دیناموزاگرب کرواسی شد.
🌀
باشگاه تراکتور…</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SorkhTimes/136789" target="_blank">📅 10:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136788">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
صادق محرمی درخواست خروج از باشگاه تراکتور را داده و قصد ندارد فصل آینده در این تیم باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SorkhTimes/136788" target="_blank">📅 10:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136787">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
گل پرسپولیس به تیم مصری توسط بیفوما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SorkhTimes/136787" target="_blank">📅 09:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136786">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
فرشید حقیری: یاسین سلمانی دیروز پشت دروازه تمرین کرده و احتمال زیاد می‌ره مازاد تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/136786" target="_blank">📅 09:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136785">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/136785" target="_blank">📅 09:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136784">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
خبرنگار پرسپولیس:
🔴
امروز محمدمهدی زارع و پویا پورعلی در تمرینات عالی ظاهر شدن .تیکدری هم مثل همیشه خوب بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/136784" target="_blank">📅 09:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136783">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
🔴
گزینه بعدی پرسپولیس برا گلر دوم گوهریه آماده س ولی برخلاف اخباری سهمیه لیگ برتری  حساب میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/136783" target="_blank">📅 09:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136782">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbSCzSVj9Iyq-QUFPkt5e6O-hGBnXmZcjJipNGdf91RkvcmnyeV1wNfzlpbfHpPgbrvYD81DxWgHIcbKN4fwziOHWTSRqxM36_WNaW4zJKxG36CLKbxXKp9K5-hmbGggQUeUPjDC6CgAZia_FW5kmrtT8ThCT9CzBITLAhWCfQbRtrEzitWLSSgCUJnA-AdOn9S9i7ln5sbyurbnArF-WgPMhZ4n1YJQs-vZpp_nfIhxrl8Dry-sVQKWZDNZbR0jsVsT_g--4OxJ7PyU23ag5WTBchIckj1QZvb31Xpyxga0-NAK5zWE2CV4jCm9UumMMHac88I2dwkvMgTHBu1XCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کریم باقری : پرسپولیس فصل گذشته مشکلات زیادی داشت و من خودم شخصاً جزو کسانی بودم که از عملکرد و نتایج تیم راضی نبودم اما نسبت به فصل آینده امیدوارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/136782" target="_blank">📅 09:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136781">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZyeTtheH-vqNCogWMSAEZ7vfMDnGf6mPdKii4jBsefeT54f-fEoq3E-V6ppMLZVQITx1W39XNBiSm3ugNNsclQpCk8bCyD_lvCVSuOH6jqPCmQ_6qgUC-MSx112meL8Ct2o9weXJDNyhvtkSofsXUns9VS_q2dXLsGRlOgE6S18QpoR8Mecp2kAL4sFNh2KbjcQOapzXTDU0MaDSZiSwx_qumHJ0xTB60M5wfJXv-C7eOWs1K-uQLtkiiz4fgTxR49Bvvs-3AmGCXeesGYECjPsoOkwXtFKckh4jY57YTYlTPZurHlaBUE-yrP5ZcqlHQsDy7Uls7C2R8jBqa6Raw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبح 5/5/5 تون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/136781" target="_blank">📅 08:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136780">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jonhy-DzYjHbeMGTtX2ySYfnTek9Mf27CkR_g7Ws0m34vLLcF9i4g5AuFXVX-pOwm32yT_Zld07TJpdxjmsz_i0lY1vfeajKghh-vg4XbIdmCqKUc37OX_80YPYK50ham7KRKyAljk8nzvDRN9bXF16xy6XUXX61uG8kanm4elAVGYc76OymuaLQdan67GpW9i_kYqY23-Et_rrqS7SEJYifkrmklKtyYm0ZKNCa-TjJLQrkuYRPQU-YaUAX616hMZz_Xyc9t53r8Aifd9Sml2WMUoufN8jcJAxbHr-iGA39UxgARY1v0SzgOuRlYUqNAQC8da1lZMuoAP7IXdXnsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
ربات وینکوبت در دسترس تمامی کاربران
🟢
بدون اینکه از تلگرام خارج بشید میتونید مستقیم وارد سایت و بخش بازی‌ها و کازینو بشید، پیش‌بینی ثبت کنید و براحتی واریز و برداشت انجام بدید.
📌
حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر براتون باز میشه:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/136780" target="_blank">📅 01:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136779">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
✅
✅
نظر شخصی :یا به گندمی اعتماد کنید که  الان تو اردوی تیم هست .یا رفیعی و برگردانید ...یا به امثال آرشا شکوری و آرمین عباسی اعتماد کنید و جذبشون کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/136779" target="_blank">📅 00:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136778">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">➡️
➡️
➡️
➡️
⬅
تارتار به دنبال پاکسازی پرسپولیس!
⏳
💬
مهدی تارتار پس از بازگشت از ترکیه قصد دارد چند نفر از اطرافیان باشگاه را به دلیل لو رفتن ترکیب تیم کنار بگذارد.
⬇️
سرمربی پرسپولیس به چند نفر مشکوک شده و پیگیر این موضوع است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/136778" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136777">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
تارتار اسم یه مهاجم خارجی رو به باشگاه داده و درصورت جدایی بیفوما و گرا مدیریت برای جذبش اقدام میکنه/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/136777" target="_blank">📅 00:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136776">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/136776" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136775">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136775" target="_blank">📅 00:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136774">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
مهدی طارمی: این جام‌جهانی فاجعه بار است، فاجعه‌ بارترین. فیفا باید هر مشکلی را که وجود دارد، حل کند. اما متاسفانه از همان ابتدا نتوانستند چیزی را حل کنند. اکنون دوباره برای رفتن به تیخوانا سفر خواهیم کرد، بدون ریکاوری. این منصفانه نیست. اگر این از نظر فیفا…</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/136774" target="_blank">📅 00:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136773">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
وکلای باشگاه پرسپولیس گفتن جذب کسری طاهری خیلی پر ریسکه! باشگاه پرسپولیس مجدد از یه وکیل خارجی داره مشورت میگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/136773" target="_blank">📅 00:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136772">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
در حرکت رونالدینهویی هایجک خوردیم و اخباری رفت به گل گهر و شاگرد رحمتی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/136772" target="_blank">📅 23:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136771">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔘
🔘
امیر عابدزاده هم تنها گلر بزرگسالی هست که سهمیه لیگ برتری محسوب نمیشه چون لژیونر بوده   جذب گلر بزرگسال اشتباه بزرگیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/136771" target="_blank">📅 23:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136770">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔘
🔘
امیر عابدزاده هم تنها گلر بزرگسالی هست که سهمیه لیگ برتری محسوب نمیشه چون لژیونر بوده   جذب گلر بزرگسال اشتباه بزرگیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/136770" target="_blank">📅 23:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136769">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
شنیده‌ها: با توجه به عدم جذب اخباری احتمالا یا رفیعی برگرده یا گوهری که بازیکن آزاد جذب بشه
🚨
پ.ن: برای گلر دوم رفیعی یا گوهری هم جوابه بعید برن سراغ گلری که قرارداد داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/136769" target="_blank">📅 23:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136768">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
در حرکت رونالدینهویی هایجک خوردیم و اخباری رفت به گل گهر و شاگرد رحمتی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/136768" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136767">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⚠️
⚠️
اخباری قرار بود امشب رسمی بشه ولی انگاری تماس مهدی رحمتی باعث شده به فکر رفتن به گل‌گهر بیفته ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/136767" target="_blank">📅 23:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136766">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🫥
🫥
حالا باید بگردیم دنبال دروازبان مطمین برای ذخیره پیام ...حالا چرا این وسط چرا رفیعی رفت دلیلش معلوم نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/136766" target="_blank">📅 23:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136765">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
در حرکت رونالدینهویی هایجک خوردیم و اخباری رفت به گل گهر و شاگرد رحمتی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/136765" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136764">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFJLU_0gFzqo8shvfZiMVq6noMMJVc6RWrFLfMnsR_cqiNxXURwlR7RIKv_D8BareNDin82BM6cdCzJzO_yYxWG8hOCUMpXAgWrbhTamsB53O58HsJfyDJi8gzTTmKfsapyqr5G_T6Nh7MMI7Y8jmt-Rj8NI0Jtsdiyu8i5mUXxE_ruKhGEEOszCXmL-gQnUNdUCWPtF2AmWfRjg9CP_X3cSiGsBZaT73zh3u3OY6-kTsKovKACGcv8rUNvRw9RLBaFSNIYs-UK0FIum4LfpRZk4tC84WVKadF4lEtimhYs8gUJmO6U1AKVnJptVJ60FBVsByMAixETHARWpJXAfQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
📸
از بازی دوستانه امروز با نماینده فوتبال مصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136764" target="_blank">📅 23:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136763">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
در حرکت رونالدینهویی هایجک خوردیم و اخباری رفت به گل گهر و شاگرد رحمتی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/136763" target="_blank">📅 23:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136762">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
در حرکت رونالدینهویی هایجک خوردیم و اخباری رفت به گل گهر و شاگرد رحمتی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/136762" target="_blank">📅 23:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136761">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🚨
محمدرضا اخباری تا دو ساعت دیگه قرارداد شو امضا می‌کنه / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/136761" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136760">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔻
⚽
ویدویی از حال و هوای پرسپولیسی‌ها در اردوی ترکیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/136760" target="_blank">📅 23:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136759">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🕹
هیجان واقعی کازینو؛ جایی که شانس و مهارت به هم می‌رسند
!
🎰
اگر به دنبال تجربه‌ای متفاوت و پر از هیجان هستید، بخش کازینوی وینکوبت بهترین انتخاب برای شماست. از بازی‌های کلاسیک مانند بلک‌جک، رولت و باکارات گرفته تا صدها اسلات جذاب با جوایز بزرگ، همه چیز برای یک سرگرمی حرفه‌ای فراهم شده است.
🎰
چرا کازینوی وینکوبت؟
• تنوع بالای بازی‌های کازینویی
• میزهای زنده با دیلرهای حرفه‌ای
• گرافیک و کیفیت فوق‌العاده
• بونوس‌ها و پیشنهادهای ویژه
• محیطی امن، سریع و کاربرپسند
🕹
همین حالا وارد دنیای کازینوی وینکوبت شوید و هیجان واقعی را تجربه کنید. شاید برنده بزرگ بعدی شما باشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/136759" target="_blank">📅 22:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136758">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🟠
🟠
🟠
مهدی عبدی در لیست مازاد مازیار زارع قرار گرفت.
✅
✅
چه بلایی سر خودت آوردی پسر..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/136758" target="_blank">📅 22:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136757">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
فووووووووووری و رسمی؛ رای نهایی دادگاه پژمان جمشیدی صادر شد و نتیجه آزمایش تجاوز منفی اعلام شد و پرونده بازیکن سابق پرسپولیس و فوق ستاره فعلی سینما مختومه اعلام شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/136757" target="_blank">📅 22:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136756">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
ویسی:
❌
اومدیم که امتیاز بگیریم و میگیریم
🎗
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐️
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/136756" target="_blank">📅 22:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136755">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❗️
رامین رضاییان نام استقلال رو از بیو پیجش پاک کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/136755" target="_blank">📅 22:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136752">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8mkkmdBJbmcnsGNKuU1Bb1Bhs-_d7Gxrw05FolT1TmJ1sjnzHAMw_d65lGSv5chCQCijvk9ZJ9B4tqhORxQUTzjK36i5hguvRywKKwOhRzMQ4WvYbtvX2_o_gxBFCdjrnxtk0Yx4H8tbzz-J_4f5AWddaW0MoIm6YbmT1YlQky1rnGR1k_I52HDzcsKd3Kub1aAqzOC9VrlD6E9TS7sffh4GYYkP5UAeprOqNk_lTciuGaYzc6M94by63-ydbUOfvRBue0SHXYoqFrbYOmQ0IwvCEMeIX7tU3ls88fkCvVbj6nx61jw_P07F4YSCKq9Zuc0qxuuVlXhu0sTbTQF2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فووووووووووری و رسمی؛ رای نهایی دادگاه پژمان جمشیدی صادر شد و نتیجه آزمایش تجاوز منفی اعلام شد و پرونده بازیکن سابق پرسپولیس و فوق ستاره فعلی سینما مختومه اعلام شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/136752" target="_blank">📅 20:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136751">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726dada166.mp4?token=dzcMo3gmfQMzASivMSH1dJL0CLRP0MyYnP0zN-LPB6HEiIkI7pdRj7NKnnEDg7tfSCANuiRusOf1OHyZpuP6tkXIPG-XFGO4n6_7LFxAwBtVVZ1AUHrmce2oYUK5XoApkZdZZHCO6Wg8qJvE7Ch7NMhZX0e88s8PsoIH-iw2o8gCQsgPPKe9bnwPdy5CF1oJHtyv3-dWW6kwDa_5iOGeV4KGgshL4SU67JG5rHCxX9Dbt9ztigkUViOxg6EdtqB2p1JqVgHjH08svOwx96XYm8ELA0gvKY2Vrqg33o8RX3qEEef2Wz-3QxSHXk2s9NK6ahiL46-NRKsndkgMwiCjgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726dada166.mp4?token=dzcMo3gmfQMzASivMSH1dJL0CLRP0MyYnP0zN-LPB6HEiIkI7pdRj7NKnnEDg7tfSCANuiRusOf1OHyZpuP6tkXIPG-XFGO4n6_7LFxAwBtVVZ1AUHrmce2oYUK5XoApkZdZZHCO6Wg8qJvE7Ch7NMhZX0e88s8PsoIH-iw2o8gCQsgPPKe9bnwPdy5CF1oJHtyv3-dWW6kwDa_5iOGeV4KGgshL4SU67JG5rHCxX9Dbt9ztigkUViOxg6EdtqB2p1JqVgHjH08svOwx96XYm8ELA0gvKY2Vrqg33o8RX3qEEef2Wz-3QxSHXk2s9NK6ahiL46-NRKsndkgMwiCjgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گل پرسپولیس به تیم مصری توسط بیفوما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/136751" target="_blank">📅 20:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136750">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⚡️
⚡️
🚨
🚨
🚨
🚨
فووووووووووووری
✅
محمدمهدی محبی نهایتا امشب یا فردا قرارداد شو امضا می‌کنه
🔽
تمام توافقات با کلبا نهایی شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/136750" target="_blank">📅 20:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136749">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⚠️
⚠️
نیمه نخست دیدار تدارکاتی پرسپولیس و پیرامیدز مصر با نتیجه صفر - صفر به پایان رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/136749" target="_blank">📅 20:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136748">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🏅
ترکیب پرسپولیس برابر پیرامیدز مصر
💢
پیام نیازمند، حسین ابرقویی، سین کنعانی‌، علی رضا همایی فرد، مجید عیدی، پویا پورعلی، مارکو باکیچ، مهدی تیکدری، محمد عمری، علی علیپور، ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/136748" target="_blank">📅 19:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136747">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">💠
💠
💠
آخرین خرید ها از زبان قدوسی:
😀
با محبی به توافق کامل رسیدن
🔹
اخباری تا چند ساعت آینده امضا می کنه
😀
ایری و طاهری هم باشگاه داره محکم کاری می‌کنه تمام شدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136747" target="_blank">📅 19:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136746">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
اعضای کادرفنی تیم پرسپولیس :
🔴
سرمربی : مهدی تارتار
🔴
دستیار مربی: وحید فاضلی
🔴
دستیار مربی: علیرضا محمد
🔴
دستیار مربی  : رضا جباری
🔴
دستیار مربی  : کریم باقری
🔴
مربی دروازه بان : حسین اینانلو
🔴
مربی بدنساز: یاگو
🔴
آنالیزور: میعاد قاسم زاده و محمد کهن  …</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/136746" target="_blank">📅 18:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136745">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">💠
💠
💠
آخرین خرید ها از زبان قدوسی:
😀
با محبی به توافق کامل رسیدن
🔹
اخباری تا چند ساعت آینده امضا می کنه
😀
ایری و طاهری هم باشگاه داره محکم کاری می‌کنه تمام شدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/136745" target="_blank">📅 18:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136744">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">https://www.facebook.com/100050246329900/videos/1060805676383532
لینک پخش زنده بازی پرسپولیس _ پیرامیدز مصر داخل فیسبوک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/136744" target="_blank">📅 18:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136743">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🏅
ترکیب پرسپولیس برابر پیرامیدز مصر
💢
پیام نیازمند، حسین ابرقویی، سین کنعانی‌، علی رضا همایی فرد، مجید عیدی، پویا پورعلی، مارکو باکیچ، مهدی تیکدری، محمد عمری، علی علیپور، ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/136743" target="_blank">📅 18:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136741">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
خبرنگار پرسپولیس:
🔴
امروز محمدمهدی زارع و پویا پورعلی در تمرینات عالی ظاهر شدن .تیکدری هم مثل همیشه خوب بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/136741" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136740">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⚠️
☹️
کانال ۱۴ اسرائیل مدعی شد: ایران دستور توقف کل حملات به کشور های عربی را صادر کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/136740" target="_blank">📅 17:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136739">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
تایم و رقبای سه دیدار دوستانه پرسپولیس در اردوی ترکیه مشخص شد.
❌
سرخپوشان در تایم های 8،4 و11 مرداد ماه با  تیم‌های «پیرامید»، «آنالیا اسپورت» و یک تیم دیگر به رقابت می‌پردازد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/136739" target="_blank">📅 17:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136738">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">💛
حسن روشن علیه قلعه‌نویی و فدراسیون
💢
حسن روشن:
«۱۴۰ میلیارد برای قلعه‌نویی ناچیزه؟! خدا رحم کرد تیم حذف شد! لابد اگر صعود می‌کردند به قلعه‌نویی و بازیکنان هرکدام یک استان می‌دادند!»
• روشن همچنین پیشنهاد فدراسیون برای تمدید قرارداد قلعه‌نویی به شرط قول قهرمانی در جام ملت‌ها را «خنده‌دار» دانست و گفت چنین پیشنهادی اصلاً منطقی نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/136738" target="_blank">📅 17:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136735">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⚡️
⚡️
🚨
🚨
🚨
🚨
فووووووووووووری
✅
محمدمهدی محبی نهایتا امشب یا فردا قرارداد شو امضا می‌کنه
🔽
تمام توافقات با کلبا نهایی شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/136735" target="_blank">📅 17:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136734">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔹
🔹
🔹
فوری/کانال ۱۴ اسرائیل:
🔹
ترامپ دستور توقف تمام حملات به ایران را تا اطلاع ثانوی صادر کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/136734" target="_blank">📅 17:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136733">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
شنیده می‌شود در صورتی که امیر قلعه‌نویی قول قهرمانی ملی پوشان در جام ملت‌ها را بدهد، در تیم ملی ماندنی خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/136733" target="_blank">📅 17:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136732">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❗️
❗️
محمد مهدی محبی با عقد قراردادی سه ساله رسما و شرعا به پرسپولیس پیوست / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/136732" target="_blank">📅 17:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136731">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
خبرنگار ورزش سه حاضر در ترکیه: محمدرضا اخباری هم اکنون در تمرینات پرسپولیس حضور داره و تیم رسانه ای پرسپولیس در چند روز گذشته هیچ عکس یا فیلمی از تمرینات گلر های پرسپولیس نمیزارن / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
…</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/136731" target="_blank">📅 17:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136729">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
#تسنیم؛ پرسپولیس سفت و سخت افتاده دنبال علی نعمتی و میخواد با یه جلسه حضوری کارو تموم کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/136729" target="_blank">📅 15:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136728">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/136728" target="_blank">📅 15:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136727">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
مشکل رضایت نامه حل شده و قرارداد هم بین طرفین نوشته شده و مشکلی وجود نداره و ظرف چند روز آینده امضا میشه/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/136727" target="_blank">📅 15:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136726">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
✅
اخباری تو تمریناته و به همین دلیل چند روزه از تمرین پرسپولیس عکس منتشر نمیشه
🫪
/ورزش‌سه
😕
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/136726" target="_blank">📅 15:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136725">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
محمدرضا اخباری در حال حاضر دبی حضور داره و امروز با دریافت برگه مجوز خروج راهی ترکیه میشه. طبق شنیده ها قراره اخباری امروز به صورت رسمی معرفی بشه ///قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/136725" target="_blank">📅 15:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136724">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
مشکل رضایت نامه حل شده و قرارداد هم بین طرفین نوشته شده و مشکلی وجود نداره و ظرف چند روز آینده امضا میشه/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136724" target="_blank">📅 15:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136723">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
آنا : محمدمهدی محبی به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/136723" target="_blank">📅 13:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136722">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
🔴
قدوسی: اخباری زمان خواسته تا بیشتر فکر کنه چون یه پیشنهاد دیگه هم داره و میخواد جایی باشه که بازی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/136722" target="_blank">📅 13:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136721">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⚡️
فوووووووری
💥
💣
اتفاق خاصی رخ ندهد محمد مهدی محبی خرید بعدی ما خواهد بود//طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136721" target="_blank">📅 13:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136720">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
شنیده می‌شود در صورتی که امیر قلعه‌نویی قول قهرمانی ملی پوشان در جام ملت‌ها را بدهد، در تیم ملی ماندنی خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/136720" target="_blank">📅 13:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136719">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❗️
🚨
فووووووووری از خبرگزاری ایرنا
🚨
پرسپولیس نمیتونه کسری طاهری به خدمت بگیره و تا نیم فصل باید در نساجی بمونه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/136719" target="_blank">📅 12:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136718">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
✅
پنج بازیکن جدید پرسپولیس از نگاه ورزش سه:
⏺
محمدرضا اخباری
⏺
دانیال ایری
🔴
ابوالفضل رزاق پور
⏺
فرهان جعفری
⏺
کسری طاهری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/SorkhTimes/136718" target="_blank">📅 12:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136717">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
❌
پرسپولیس در انتظار امضای قرارداد ارسال شده برای اخباری
🔴
با توجه به اینکه محمدرضا اخباری در کمتر از 10 درصد مسابقات فصل گذشته برای سپاهان به میدان رفته، سهمیه لیگ برتری محسوب نمی‌شود. / تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/136717" target="_blank">📅 11:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136716">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✅
✅
طاهرخانی: احتمال داره فردا از محبی رونمایی بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/136716" target="_blank">📅 11:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136715">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
✅
پنج بازیکن جدید پرسپولیس از نگاه ورزش سه:
⏺
محمدرضا اخباری
⏺
دانیال ایری
🔴
ابوالفضل رزاق پور
⏺
فرهان جعفری
⏺
کسری طاهری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/136715" target="_blank">📅 11:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136714">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">💥
💥
با جذب محبی و لطیفی‌فر سهمیه‌ی لیگ برتری پرسپولیس تموم میشه ولی قراره یه سهمیه بزرگسال و دو سهمیه زیر ۲۳ سال اضافه کنن تا ایری و طاهری و رزاق‌پور رو هم بتونیم جذب کنیم/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/136714" target="_blank">📅 11:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136713">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
✅
اخباری زمان خواسته تا بیشتر فکر کنه چون یه پیشنهاد دیگه هم داره و میخواد جایی باشه که بازی کنه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/136713" target="_blank">📅 10:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136712">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
🚨
باشگاه پرسپولیس قصد داره‌ تا ۲۴ ساعت آینده از چهار خرید جدید خودش رونمایی کنه ///فرهیختگان
🤝
محمدرضا اخباری
🤝
دانیال ایری
🤝
کسری طاهری
🤝
پوریا لطیفی فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/136712" target="_blank">📅 08:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136711">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❗️
❗️
دیشب و بامداد امروز هم حملاتی به کشور عزیزمون نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136711" target="_blank">📅 08:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136710">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
✅
خبرگزاری تسنیم در واکنش به صحبتهای قلعه نوعی که گفته از خودگذشتگی کردم اومدم تیم ملی تیتر زده که آقای قلعه نوعی میتونه دیگه ایثار نکنه و از تیم ملی بره و برگرده لیگ برتر همونجایی که تو ۱۰ سال گذشته هیچ افتخاری کسب نکرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/136710" target="_blank">📅 08:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136709">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
بعد از 13 شب .دیشب و بامداد امروز هیچ حمله ای به ایران و نقاط ایران از جمله جنوب نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/136709" target="_blank">📅 08:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136708">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uO7SSacuk2VqAFrkWKHFunwc66lb029wMglisYAR8QGRkVKpe4_UvvIodtLbsEZf8EOIS_Z_o8Oiygv9k2ukS0ycwq7loO31KJybdv2uTMn8yhrQWA2YkKbh8e_pboGUKgjGLsaGD0fcJJlBo8-_X4IzLAJE90smitBr7joCeRtu3qCfPFr5E6lUAgmzcHsA9FPJ3HFNus1L-mA31l__Xd0WgiekPGogcXpldCyOfmjWyMz4z-Qmlu1_jJTaZ1mW6ba4chXegwERgJwYbGq2RNQ_XkXn9eDG1NAhOIZDcnSa8BvP5_pV_ChhxQ6RoKXdx16bF-dS1zUOTnlxLXW-9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/136708" target="_blank">📅 08:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136707">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">درآمد ثابت واقعی میخوای بسم الله
👍
سایت های شرطبندی دنبال ادمین این کانالن ، داره ورشکستشون میکنه
.
😂
👇
JOIN JOIN JOIN
JOIN JOIN JOIN
فقط یک هفته جوین باش میفهمی پول درآوردن چقدر راحته
😍
🤝</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/136707" target="_blank">📅 01:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136706">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UVHoYItptXG3bbOWWKxRbuUA-h2wHCbTrJNuLY1DAVaeBXBA4waCNoX48TOdB_70yonoeNvHc4FXmDKQdBH0UGDlrRPO3w-5SRqQfHxYF3Zt-pU40so6_GdhDAq3vn84fQo_yj4ib4zUiqrYqeNbBd3IdBxAwHMM-h56OLAnh99tXL1KHEAIxTvrfCMBWLsU-qeIJNnWQzfm2K_VgEOGOwu0T-Rv6oDr1jcrL7YB5qLtv-v-T410_LERpgc-Dx2miXToIjQd_CdE5l16e0ax2jllzd7TDGMuckObQaPtZdyHi4YeZR4fiSXDtNo1ILXS-bLcOcJNB1FXEUD6AmAXdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
رفقای بت باز و اونایی که اهل پیش بینی فوتبال هستن از همگی دعوت میکنم این متن رو بخونید
...
🤖
با ربات
هوش مصنوعی
پیش بینی فوتبال ماهانه 30 الی 40 میلیون تومان به جیب بزنید،
کاملا واقعی
🔥
📣
رفقا این ربات طبق آمار و ارقام تیم ها و الگوریتم افت ضریب خیلی راحت بازی های مشکوک به تبانی و فیکس رو پیدا می‌کنه فوق‌العاده پشم ریزونه.
😄
👑
t.me/+bReDKwrhVk5lMmM0
👑
t.me/+bReDKwrhVk5lMmM0</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/136706" target="_blank">📅 01:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136705">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
محمدرضا اخباری در حال حاضر دبی حضور داره و امروز با دریافت برگه مجوز خروج راهی ترکیه میشه. طبق شنیده ها قراره اخباری امروز به صورت رسمی معرفی بشه ///قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/136705" target="_blank">📅 01:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136704">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🎥
⚽️
ویدیو باشگاه از تمرین تیم با کپشن:
😀
از ضربه‌های تمام‌کننده تا واکنش‌های تماشایی؛روزهای پرانرژی پرسپولیس در ارزروم
❌
پ.ن حال پرسپولیس خیلی خوبه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/136704" target="_blank">📅 01:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136703">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
✅
ورزش‌سه: اورونوف، تیکدری، عمری و محمودی اماده‌ترین بازیکنای تمرین دیروز پرسپولیس بودن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/136703" target="_blank">📅 01:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136702">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
فارس: حمید مطهری گفته هیچ جوره نزارید رزاق پور بره پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/136702" target="_blank">📅 01:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136701">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
|
#فوری
🏅
🏅
به گزارش رسانه «سرخ تایمز» باشگاه خیبر خرم آباد طی نامه ای خواهان جذب تیوی بیفوما شده است،اما دو باشگاه تاکنون به توافق نرسیدند.
⭕
🤩
خیبر اعلام کرده از قرارداد ۸۵۰ هزار دلاری بیفوما ۲۵۰ هزار دلارش رو پرداخت میکنه و ۶۰۰ هزار دلار حقوق باقی ماندش رو پرسپولیس پرداخت بکنه اما حدادی به عبدی گفته ما نهایتا ۴۰۰ هزار دلار از حقوق بیفوما رو پرداخت میکنیم، درنهایت اگر اختلاف ۲۰۰ هزار دلاری بین دو باشگاه حل بشه تیوی بیفوما به خیبر خواهد پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/SorkhTimes/136701" target="_blank">📅 00:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136699">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
تکمیلی :قدوسی : تارتار گفته بیفوما و گرا برن و سرگیف بمونه اما خلیلی میخواد سرگیف ملی پوش رو رد کنه تا گرا و بیفوما بمونن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/SorkhTimes/136699" target="_blank">📅 23:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136698">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">💥
💥
با جذب محبی و لطیفی‌فر سهمیه‌ی لیگ برتری پرسپولیس تموم میشه ولی قراره یه سهمیه بزرگسال و دو سهمیه زیر ۲۳ سال اضافه کنن تا ایری و طاهری و رزاق‌پور رو هم بتونیم جذب کنیم/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/SorkhTimes/136698" target="_blank">📅 23:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136697">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❗️
از تمرین امروز
👀
💪🏻
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/SorkhTimes/136697" target="_blank">📅 23:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136696">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QICGlIhEKETdQE8p14COmoekki7quxQBhM5Ct8aRigRbUxrCBYsWApMCp16Qinjq2srT1-gAzgUlUAgWSXl1wO82L7TMtAxpvA6me70CbYzsp11hMiL6GLNJd4wg3UWUWBwYlmFyX822nYgsJJ6gTtcafXvXlQDemJjbTvHRXLGpoGVUumiBd54ZSrAHrj9a6TbnRaDRe4Prt0k_j3K-HLV8gIlYJ-yfLhz96pRNpp_JznwulxxlFpLCrCmKN1p-fnB9ZqbF_lhO3OtVfNn_81uffmcAxsxlAAe_aQrjRcTDOrIdcnnUIZGHSugtcu4IBmOWq4HSNSuIZ9uJ6JKjtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
از تمرین امروز
👀
💪🏻
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/SorkhTimes/136696" target="_blank">📅 23:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136695">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⬅️
⬅️
⬅️
وای‌نت: اسرائیل خود را برای حمله گسترده آمریکا به ایران در فاصله شب جمعه تا بامداد شنبه آماده کرده بود، اما دونالد ترامپ برای دادن فرصت بیشتر به مذاکرات، این اقدام را به تعویق انداخت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/136695" target="_blank">📅 23:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136694">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
🔴
پوریا لطیفی فر ستاره 22 ساله تیم‌گل‌گهر با عقد قرار دادی چهار ساله رسما به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/136694" target="_blank">📅 22:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136693">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
فرزین معامله گری از پرسپولیس جدا شد و در اردوی ترکیه حضور ندارد و شماره بیست پیراهنش هم امسال تو تنه عیدی هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/136693" target="_blank">📅 22:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136692">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
معامله گری که سرباز شده و برای دفاع چپ فقط ی جلالی و داریم و خلاص که اونم مصدوم شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/136692" target="_blank">📅 22:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136691">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgrNChHN823BzNKH6jyX0_hQaoW5OiBVZEaZwoacd32Mj4X1Pis5bqjLkkY6YSS0wFiGXur81mY8jmCRH9SFdc2bAlCfBnyp9v29d0_CBQ6o18uDm0jQmuFs1uqsUtzg62POHqjGXrnlteaRofvVOzFeRcp16tJxzFkkc8tiCKpE2dekY_IvTvfbgMMbOrKBhOTFNEuMVnS74vf2fsaXGveAge8cXtCs6o_vTACekpzm1p0BPIDAl3MbjdIAeIA7UCxboYW0tj-VHlJeq0fyyJutAF8qb0r4Rv5siKTWv3qZyb-B5R6G6KSAzX81L13dZhwqy0JZGSAb9WDaPfTaPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
محمد خلیفه، گلر جوان و ملی‌پوش آلومینیوم به استقلال پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/136691" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136690">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
ایگور سرگیف توی تمرینات پیش‌فصل بی‌نظیر بوده و تا الان انتخاب تارتاره برای نوک خط حمله
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/136690" target="_blank">📅 21:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136689">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb0a656a22.mp4?token=GFC9a-tKnem8zAAAHgxaSrZhONHAcLP5zWSE-5HSJanP7NsUopBW7zJHIYTQOZpmbM1DqVSgYCxcGM40l8mtHRHQJZ-Xw2rmQd7ASi3ifXHI21zEVEQq7NM_ohtS4mITuQkriygN5xtPaq63SteXX-24QglcAXa5PCW7XrtW0DtUNc0kNfqLBapQPRwAsspc2K7e84FUD4CkzpgbFnpa1t9VWNa_qXjuy8VYNga3hQAM2jJzcBkdJ_SPvOExaqaXthoYJqKnI4PuhI4o_Z4JuMXAzzVuJ82Dogzb5ewpFe9hLWVzpm5jUzt55pUM9rH6VpywZFNbi3sk4Y3GU67sgSHvpcIm-Leq568zrLrFjN1TTQT9tFZHlHliOHJMHsmJFNtUg-rrVxc2UmzD2vmKuWjdSODJtcSzITrMsE7ejqnl_XhdhKeHr5bh8F99jld_2CfGhGed5lIAZXCR6KNOAq8nijCcwZq4aDaBKb5BR1qU0SYRhgrXHPax7LbhQIs8z7kp2F4c_zpSThMlQc45nvhbOyFH8-GtL2lHP6U8TJdKeIPL5CmIecz8hOvm1R5hpxuiWdyXG6G6gf07hNVwFRhG9CNCk7NcarMQndvhbBa2rdpFmmiqV6IUi_I54CNTGP05tv24EL62JKIFBZ23u4toUeZiZcNvNDPugbyw-ZY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb0a656a22.mp4?token=GFC9a-tKnem8zAAAHgxaSrZhONHAcLP5zWSE-5HSJanP7NsUopBW7zJHIYTQOZpmbM1DqVSgYCxcGM40l8mtHRHQJZ-Xw2rmQd7ASi3ifXHI21zEVEQq7NM_ohtS4mITuQkriygN5xtPaq63SteXX-24QglcAXa5PCW7XrtW0DtUNc0kNfqLBapQPRwAsspc2K7e84FUD4CkzpgbFnpa1t9VWNa_qXjuy8VYNga3hQAM2jJzcBkdJ_SPvOExaqaXthoYJqKnI4PuhI4o_Z4JuMXAzzVuJ82Dogzb5ewpFe9hLWVzpm5jUzt55pUM9rH6VpywZFNbi3sk4Y3GU67sgSHvpcIm-Leq568zrLrFjN1TTQT9tFZHlHliOHJMHsmJFNtUg-rrVxc2UmzD2vmKuWjdSODJtcSzITrMsE7ejqnl_XhdhKeHr5bh8F99jld_2CfGhGed5lIAZXCR6KNOAq8nijCcwZq4aDaBKb5BR1qU0SYRhgrXHPax7LbhQIs8z7kp2F4c_zpSThMlQc45nvhbOyFH8-GtL2lHP6U8TJdKeIPL5CmIecz8hOvm1R5hpxuiWdyXG6G6gf07hNVwFRhG9CNCk7NcarMQndvhbBa2rdpFmmiqV6IUi_I54CNTGP05tv24EL62JKIFBZ23u4toUeZiZcNvNDPugbyw-ZY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
⚽️
ویدیو باشگاه از تمرین تیم با کپشن:
😀
از ضربه‌های تمام‌کننده تا واکنش‌های تماشایی؛روزهای پرانرژی پرسپولیس در ارزروم
❌
پ.ن حال پرسپولیس خیلی خوبه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/136689" target="_blank">📅 21:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136688">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
✅
ترامپ قرار بود عملیات گسترده‌ای که راجع بهش صحبت میکرد رو امروز صبح علیه ایران انجام بده ولی لحظه‌ی آخر عملیات رو متوقف کرده تا به ایران یه فرصت مذاکره‌ی دیگه بده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/136688" target="_blank">📅 21:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136687">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
🔴
پوریا لطیفی فر ستاره 22 ساله تیم‌گل‌گهر با عقد قرار دادی چهار ساله رسما به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/136687" target="_blank">📅 21:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136686">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
با اعلام باشگاه پرسپولیس، قرارداد محمدامین کاظمیان با توافق دو طرف فسخ شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/136686" target="_blank">📅 21:29 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
