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
<img src="https://cdn4.telesco.pe/file/QhBahW78tnnvtXEaJRcigCOOhEBKcrOEhYm9EEG46Z4UXBNu97Z_pHVHUn16PYNlFugGGFxHcam57mRylXjoBIWiwchCJF-A9upKRJpMYwlVP-Imte7tIIx6aPZSqPVknOAfvd7Q_mA-v2V-CoyNMPsmDvGw6PuPMbRKQTPz_GJqeCtmJJtgS7RsfjQTeb587KqDHWlJrhw2D6QC1S5iEpAqJZeUkLpeJ-IFexrZYU65I0tz2txoS370Pq97Z94vBeT7544763tOfHEmbT8bv4XLEL3tGc_P8PognjisSOqRph3Ac9ZnAXrHVrWyXQk-pSdrPJDz9IY0ne7wHw-qnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 04:12:46</div>
<hr>

<div class="tg-post" id="msg-138549">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQ_SGiuezat29CWI-oL1xowMmAUyuMWw71GEZIn1AGaFh-X6HtEvR5YiXHsQF1vU-4w9_WxWkIMy5mtf4CE54jmw97g9kX-5LeoE_v2m1Lfmv3L1vnSXb-hfkjc4DcnuG7t3viMuqF9bZ_DTyuDXrPQJNp8FN1wLk-CmB1VHbdmq7g8hw5zrRqYU7GpwtYT1dOX4C7toUeyfousos0FAcS4n_oFJMsDeWoEtude4dBzXA97NdoMQX3fpE2_0Te6G5mvlSR-j4aIFSTgf30RfIXhY8bJW61eqKHvuKB2ypFd_XYX9bu4mGligwh4rr_oiOfsG3NIqoPJAwvqKM36K-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
️ بونوس اختصاصی چرخش رایگان بازی Scarap Temple
💰
کاربران اسپورت نود می‌توانند از همین حالا، با هر بار شارژ حداقل ۱ میلیون تومان، متناسب با مبلغ شارژ خود ‌اسپین رایگان کازینو دریافت کنند.
💸
هرچه مبلغ شارژ بیشتر باشد، چرخش رایگان بیشتری دریافت خواهید کرد! با هر چرخش، شانس برنده شدن جوایز نقدی را دارید؛ جوایزی که بدون هیچ قید و شرطی مستقیماً به موجودی اصلی شما اضافه می‌شوند.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
🔵
نسخه جدید سایت:
Sportn5b2.com
🔵
نسخه قدیمی سایت:
Sport90.bet
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/SorkhTimes/138549" target="_blank">📅 01:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138548">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
حسین زاده :بهمون گفتن بازی با پرسپولیس بدون تماشاگره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/SorkhTimes/138548" target="_blank">📅 01:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138547">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✔️
✔️
✔️
تارتار تو تمرین امروز چند تا ترکیب چیده و هر کدوم در یک رسانه قرار گرفته
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SorkhTimes/138547" target="_blank">📅 01:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138546">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQarnTpWxH84On-2eYDbOLwwj_0IW_OdtzN2hP4SMZMgn_zZ9TlU30RfV7XhcjAYwZcgTUhDpC2f6rkVBQjaoWGX200-cVK3PlSJUV5YQ0YDi35N_ymHAxC00Q3QJO4jG5GEUWK7y9aWE0cfgGLSrDCjVRNwEDuHqKHLRa0c72wRxIRZK36ZFXi3be3qzYRP9Ft2vtw3WiHLTZuDSG27qYi3l4p-9u9lSlm4HwZH11WE1uWJvxM0F5zw9ix2LJwWSEb5vxuwc6vtV7r9dYx9aOH_eNHhkCJIBINFsiElFCRtfS3ZrKIwyr6ZY836Y4O34zNb2LnbOb0wBhZMVGhgxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
استقلال و سپاهان هفته سوم باهم بازی دارن
بعد اگه جفتشون از آسانی و طاهری استفاده کنن و بعدش بفهمن جفتشون غیر قانونی قراردادشون ثبت شده و تخلف بوده نتیجه بازی چی میشه
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SorkhTimes/138546" target="_blank">📅 00:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138545">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❤️
گل اول تراکتور به سپاهان توسط امیرحسین حسین زاده 83
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SorkhTimes/138545" target="_blank">📅 00:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138543">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
❌
مهدی تارتار تصمیم داره دیگه حتی تو آخرین تمرین قبل از بازی هم ترکیب تیم رو اعلام نکنه تا ترکیب لو نره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/138543" target="_blank">📅 00:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138542">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🏟️
آخرین وضعیت سکوهای ورزشگاه آزادی و وضعیت زهکشی و زیرسازی چمن این ورزشگاه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/138542" target="_blank">📅 00:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138541">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
⚽
باز هم حرکت عجیب و منشوری شجاع خلیل‌زاده، بعد از خوشحالیِ گل!!!
❌
پ.ن و بازم کشاله ران بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SorkhTimes/138541" target="_blank">📅 00:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138540">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
✔️
البته طبق حکم دایمی بازی لیگ دو تیم پرسپولیس و تراکتور بدون تماشاگره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/138540" target="_blank">📅 23:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138539">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
مس شهربابک از استقلال به خاطر استفاده از آسانی شکایت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/138539" target="_blank">📅 23:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138538">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
عینک‌زاده: فوتبال دعوا نباشد که لذت ندارد باید دعوا کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/138538" target="_blank">📅 23:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138537">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
⚽
باز هم حرکت عجیب و منشوری شجاع خلیل‌زاده، بعد از خوشحالیِ گل!!!
❌
پ.ن و بازم کشاله ران بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/138537" target="_blank">📅 23:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138536">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a31203bb22.mp4?token=bv5iR_88PkYpof0_UD-AmFzett0o2q_AP4cx3ku5YutwD4UZsoQt7UR7sOGzsfZJW00p7UF95xMUXDB81M4XsG4r02-E1ChZCiKkebeYaLyMzCMb3JbP0Ht2Ir20ncQaemunBjZFJ2eFwRAi8osKVueCm8Jpz-wqhmQS5B3Dt0_m878CSODkkFKLAgREuuGnjS8jNtxlU3tjZf9ekzdxoaH0f62h-O1a4QZGcoZPGZOqf5o8VO4q3r-WNsfrCs3U98ZbrPByYwHwCiTon0fIOeOKgKoKQA-6sLgCaAlxu8nXFqOYa5Rm995bfLCIY03TFJeYzVW8WYj0QemeZc9w5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a31203bb22.mp4?token=bv5iR_88PkYpof0_UD-AmFzett0o2q_AP4cx3ku5YutwD4UZsoQt7UR7sOGzsfZJW00p7UF95xMUXDB81M4XsG4r02-E1ChZCiKkebeYaLyMzCMb3JbP0Ht2Ir20ncQaemunBjZFJ2eFwRAi8osKVueCm8Jpz-wqhmQS5B3Dt0_m878CSODkkFKLAgREuuGnjS8jNtxlU3tjZf9ekzdxoaH0f62h-O1a4QZGcoZPGZOqf5o8VO4q3r-WNsfrCs3U98ZbrPByYwHwCiTon0fIOeOKgKoKQA-6sLgCaAlxu8nXFqOYa5Rm995bfLCIY03TFJeYzVW8WYj0QemeZc9w5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚽
باز هم حرکت عجیب و منشوری شجاع خلیل‌زاده، بعد از خوشحالیِ گل!!!
❌
پ.ن و بازم کشاله ران بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/138536" target="_blank">📅 23:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138535">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
|
#فوری
🤫
⚽
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس اخبار جذب مبین دهقان صحت ندارد و این بازیکن مدنظر باشگاه و کادرفنی نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/138535" target="_blank">📅 23:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138533">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
🆕
🏅
به گزارش رسانه «سرخ تایمز» و طبق گفته های عضو هیئت مدیره باشگاه پرسپولیس، باشگاه مصر هست تا محمد قربانی رو به خدمت بگیره و خود محمد قربانی هم علاقه منده تا به پرسپولیس بیاد اما مشکل اینجاست باشگاه الوحده داره بازی در میاره و تا الان…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/138533" target="_blank">📅 23:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138532">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0VgKM0HTQo1jNhyQ6UgNNYRdzyLjbICusGvpaNfEyfxUYhXE1Fo23cr_GOi3oQjgktcxCtWMtuGOPRnQJCD4OknNasDgIPUFOyUzJ9u5d9BkM5Cwr6XAPhnxQqiVjkLgorofs7TWo-yRgEtZhAqYFiPIaFHq3oEIJBB9XthpVhYahgms7skwT1cYppeX2CaM0xav62EP6NPkOxY2Zpozxnmw-mohdaUpHrWrfByAz4E8wnFTxek-LHx7SwXOCONDZh-geGhoUenouWDHOhnRu4S_DEwpCPNn-z1E8n6EZu6TI0iP38hM0zoWSRf8tgHj5BHoBQpaajGIoSDZmrwZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استقلالِ سهراب اگه بخواد انتقام کاملی بگیره؛ باید 8 تا به الوصل و 7 تا به العین بزنه:))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/138532" target="_blank">📅 22:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138531">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b8d2e556.mp4?token=guGz5XZmwq4Zl8tjTHXc-7v-oEc78BE_ouwIb1q7DPdGa1lczwKSySVFjLE4fWZHK06nR-w9TsC_gL9--jSJv_MpkJ1wsPSco85Oc2PSgnCh8BeTHa0pZ9aUOGAuXvTH7jGqJrqYVIYGKz0QK7YvI8QMXiysFhSJi9EDih3dBC82Br1cV8Dka1KKO7N57NhKSTXv5w6meYv70Kx9PvPA2qKT29iWebrz6zQNYYEq2E7G2hbNYJNOANt3n01VfucHMNGKyt9dWVKe18QV6yWmhJB8xGQc2mPWrJKctKR0-_IpAedEUPo6bCO67jRXzWgAH6w_34aLY9faBFMZX6TOTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b8d2e556.mp4?token=guGz5XZmwq4Zl8tjTHXc-7v-oEc78BE_ouwIb1q7DPdGa1lczwKSySVFjLE4fWZHK06nR-w9TsC_gL9--jSJv_MpkJ1wsPSco85Oc2PSgnCh8BeTHa0pZ9aUOGAuXvTH7jGqJrqYVIYGKz0QK7YvI8QMXiysFhSJi9EDih3dBC82Br1cV8Dka1KKO7N57NhKSTXv5w6meYv70Kx9PvPA2qKT29iWebrz6zQNYYEq2E7G2hbNYJNOANt3n01VfucHMNGKyt9dWVKe18QV6yWmhJB8xGQc2mPWrJKctKR0-_IpAedEUPo6bCO67jRXzWgAH6w_34aLY9faBFMZX6TOTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شادی خاص نکونام با بیرانوند پس از گل دوم تراکتور مقابل سپاهان
😂
❌
پ.ن هفته سوم قیافتون دیدن داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/138531" target="_blank">📅 22:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138530">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V57_VgBPVUgAB1AADm3ONYhErLxcvakp5z_GYF4TarAskaYAgUosY2cfjc21A-plKC1i8WJj0VkTdlmibYLvajmufhE3j1m8M0ScMCaJyZtCI16fuAfLlrzKpBWyDKwdc68FEyOCr_IgItxa2aZ9s-T-h5j-A4RWoQwfi9ayIWLoJvQiYYgizAFjSgsYD8h-sDCTZnZqZ5_g4MYZ50eVTpacTuq1ieLnwink1vicCXxWKEhb8coCg29y2lyFQjNHVoEIw5e6FCikRD7RXdrVmMXAlEKHFWIWlZQKkkBqACn84Ss5SS0-xUoIHcLnNbQ9Os0EL6PKblGY6TcN5FxxKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/138530" target="_blank">📅 22:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138529">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkAH3nqEMAYx6MkiUAv9oafrzTOITMh03wvHLWRXE2xNECgDdtlQFm3580rza8_5SnyakGJBLxShgeQReQ4PtMyfwLJTYRqaTL18yhjl7gkUsHPLHUH6e6BTIF_kLwP-AP-EDmvFtwueJ-7sQLviAzHOTxD2v12FvqdT7-pwkR6SHl7m4kXsNPquFlb2mQ7lVjyDPBHsl66ZryFiyaY_5Grn7gIiykTXt-JsR7jPEHjTvLrfLQykpaeHRApJ3YerTSji33aOqLiUB0D4ho-7qfAczdVXgefkwADO-O1rSQcz9qjkK_jBY_5HLNp_98OzfqTTg9Fori8o7773Pdjcbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
جدول لیگ برتر بعد از پایان روز اول از هفته دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/138529" target="_blank">📅 22:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138528">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
✔️
هفته سوم هفته مرگ و زندگی
✅
استقلال و سپاهان یکشنبه ساعت 19/30
✔️
پرسپولیس و تراکتور دوشنبه ساعت 18/30
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/138528" target="_blank">📅 22:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138527">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
کیسه و ترتر شش امتیازی شدن و کلین شیت و حفظ کردن امیدوارم فردا بازی و ببریم و پیام هم کلین شیت شو حفظ کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/138527" target="_blank">📅 22:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138526">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
دومی هم زد ...و جواد چکش دومین بردشم آورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/138526" target="_blank">📅 22:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138525">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b05abe66c.mp4?token=KZ-opqzItTuowR_TTEF7x5_x-ZgozjCREO4tQSR1nwx81O_xOZXvChyu4tomIzA9Txi0O73GdmykYNcI3hwuIrxI74xNbSFMXNxGLwFMEXbQ8haLdIP408SfyQRcImJsWiIs62ZzZP239Ud4zgY0pMUb7Zf0tALxUfXB_koyk_UNjl6tzPosXka5FAtFeZ95mnBaAQ32ikLzEE59L1R1uc2hR-tg9D1sW0SDdSXGSSo87IF2D0Dbv3BmULu-RubycbBcUoEostEgSFyN9wmr4atPYtwt67ndwdH_VqMBbEg3oRZX2E0jbyu1WD5pWTahFkM5TdI5Ok6izE2715vPzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b05abe66c.mp4?token=KZ-opqzItTuowR_TTEF7x5_x-ZgozjCREO4tQSR1nwx81O_xOZXvChyu4tomIzA9Txi0O73GdmykYNcI3hwuIrxI74xNbSFMXNxGLwFMEXbQ8haLdIP408SfyQRcImJsWiIs62ZzZP239Ud4zgY0pMUb7Zf0tALxUfXB_koyk_UNjl6tzPosXka5FAtFeZ95mnBaAQ32ikLzEE59L1R1uc2hR-tg9D1sW0SDdSXGSSo87IF2D0Dbv3BmULu-RubycbBcUoEostEgSFyN9wmr4atPYtwt67ndwdH_VqMBbEg3oRZX2E0jbyu1WD5pWTahFkM5TdI5Ok6izE2715vPzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔄
🔄
فوووووووووری :
❌
حق میزبانی استقلال با گوه کاری تاجرنیا گرفته شد و ای اف سی هر خراب شده که ای به عنوان میزبان انتخاب کنه استقلال حق اعتراض نداره
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/138525" target="_blank">📅 22:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138524">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❤️
گل اول تراکتور به سپاهان توسط امیرحسین حسین زاده 83
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/138524" target="_blank">📅 21:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138523">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
✔️
برنامه هفته دوم لیگ برتر  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/138523" target="_blank">📅 21:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138522">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❤️
گل اول تراکتور به سپاهان توسط امیرحسین حسین زاده 83
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/138522" target="_blank">📅 21:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138519">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d2cc7d25d.mp4?token=Y0WmMMwd4EbUYfGkMrRcQVc1D1r5vsCo8YCNledV3UAnaouvt1C16UfCHkdlBrJrjLdAC8op2WrJxgJgIHBvd08UqU3zjBSI9JeryvUcwUzc4sNG86InsAglNAnPVIC5DM285FMBgDsdN5Y016wXwHQx50G7ypfP0Quvuc-pC6vOBGYrgr-aSIrrLh2q7Qh7Xwcl88CYAAoAcLnwk4FNgEcAo_cy640qAx4_2xYq6ELUV30FO_EeEUvgBKUezNIdDkK4vW4rqebGfOwmnrjg7g8Nd7gGugWRnA7sEB4CGKiLxWjZkI7-404aND9rG_6WkY_LROAIXH_SSquerNNjKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d2cc7d25d.mp4?token=Y0WmMMwd4EbUYfGkMrRcQVc1D1r5vsCo8YCNledV3UAnaouvt1C16UfCHkdlBrJrjLdAC8op2WrJxgJgIHBvd08UqU3zjBSI9JeryvUcwUzc4sNG86InsAglNAnPVIC5DM285FMBgDsdN5Y016wXwHQx50G7ypfP0Quvuc-pC6vOBGYrgr-aSIrrLh2q7Qh7Xwcl88CYAAoAcLnwk4FNgEcAo_cy640qAx4_2xYq6ELUV30FO_EeEUvgBKUezNIdDkK4vW4rqebGfOwmnrjg7g8Nd7gGugWRnA7sEB4CGKiLxWjZkI7-404aND9rG_6WkY_LROAIXH_SSquerNNjKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
گل اول تراکتور به سپاهان توسط امیرحسین حسین زاده 83
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/138519" target="_blank">📅 21:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138517">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
✔️
✔️
شهاب زندی مدیرعامل نساجی: به مدیران ارشد استقلال هم تاکید‌ کردم مستنداتی دارم که آسانی‌ بازیکن غیرمجاز است و اگر مقابل ما امروز حتی یک دقیقه هم به میدان برود از آنها شکایت خواهیم کرد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/138517" target="_blank">📅 21:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138515">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✔️
#ارسالی | #تکمیلی
🆕
⚽
هوادار مقیم امارات به نقل از محمد قربانی: میگه به باشگاه گفتم اگه قراره رضایتنامم رو صادر کنین برای باشگاه پرسپولیس صادر کنین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/138515" target="_blank">📅 21:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138514">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9LS1vY1NTcrFF49F8kmf1YAk1hgd-NeAMVJn-p6mguvFvSsFNv0WwasyuFPgx4uMuYin1E4wyVftRLS9-cuhDaYDcIZPSaoy4Me8f-5p-X_nQOeg12Rp1x02N2nfnHB7QReaFzCLaUZS5XPLCYWv1Doub7dmGZ2njjO7yCCyiRJ35wAfjkCmhS0JE0LhcaqE5pvNK2lXQr5m6AgeUwR8P-zTSGmjUvejtA-H9R7bwVqgHYHcALUuDWTf6yig66StEEEzvT9BmGvm_XyTmBQ9SBakQuOOJ38iP3CrgWs2KlbBMBDGjqv-JO370ZA_tmEi5a4wlkmgfxlS9RSEvHtBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ارسالی
👀
⚽
هوادار مقیم امارات: امشب محمد قربانی به همراه همسرش دیدم.
✔️
خیلی مشتاق بود بیاد پرسپولیس،میگفت ولی چیزی دست من نیست باید باشگاهم همکاری کنه باهام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/138514" target="_blank">📅 21:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138513">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
گل شانسی کیسه
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/138513" target="_blank">📅 21:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138512">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔄
🔄
فووووووووووووری
🚨
امیر جعفری مدافع چپ گل گهر سیرجان از لیست این تیم برای بازی امشب این تیم خط خورد تا شایعات جدایی و پیوستنش به پرسپولیس قوت بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/138512" target="_blank">📅 21:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138511">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
فوری؛ مهدی تارتار : فردا چند تا از بازیکنان مون به علت خستگی نداریم و ترکیب شروع مون تغییر می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/138511" target="_blank">📅 21:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138510">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66e078a045.mp4?token=DSsUroZkvir-4dr4iPFjcNWSRY7VS4bqs-v_jx9vaZp2spfTUsKrGhIzLgYM1Sr-gU2Du9k0yz25TuHAWCNR5fE1VbkSTXG1PJhi2QvrV_RaFcqn4SwR5YIB0akkpAwl6dE5NwO3hN6v7CSgimzWpi4MJFATjGl83EYu7i3dvyHWIVw4xzXD4OS9TXGIL4ckoHIreru0RlxsZ8_ZYfy7LHI4pwnu-PyRKiZT0n3eZdeZZES_eALVQcu7ytBiKmDcVmSuNKOkANL-S84f0C7_YuFN_qYB9JNn3mO6HW14Lq4GwoyghuSbrlpMukkgzfl_xjP0RMmBbQtIzGT136STqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66e078a045.mp4?token=DSsUroZkvir-4dr4iPFjcNWSRY7VS4bqs-v_jx9vaZp2spfTUsKrGhIzLgYM1Sr-gU2Du9k0yz25TuHAWCNR5fE1VbkSTXG1PJhi2QvrV_RaFcqn4SwR5YIB0akkpAwl6dE5NwO3hN6v7CSgimzWpi4MJFATjGl83EYu7i3dvyHWIVw4xzXD4OS9TXGIL4ckoHIreru0RlxsZ8_ZYfy7LHI4pwnu-PyRKiZT0n3eZdeZZES_eALVQcu7ytBiKmDcVmSuNKOkANL-S84f0C7_YuFN_qYB9JNn3mO6HW14Lq4GwoyghuSbrlpMukkgzfl_xjP0RMmBbQtIzGT136STqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گل شانسی کیسه
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/138510" target="_blank">📅 21:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138508">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45979f2dc9.mp4?token=l0Dda85gpDlU8h3RNfMx4kquW8AOeS65yqhY1uisrig1b05u8kJmP2BIrlyTFxdJMZCe482NX5J4nG2tMY_SU3TQ2Efoj8UbccHSsxFVBhEVdsENVQ_F8wMw3IgZBbTorxmodo5GnRBy45ZGYrM7HocJ7fJfqILmJc2po827x11Kzgsvdv74xdj7vuyH75PJIWre5lGqzhhQU1Rmfy-ht3EXASgbOz7uO8hMqHGklpmU73jKSQpyMDjtzNnX0784ALbDqMJxRLoGYMCFNoFzUwSBqKszfsSluVs87aB445--jAmgSZ_v2B_rN_NtSKloOdRMm28I7S_OVrPG_B9YfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45979f2dc9.mp4?token=l0Dda85gpDlU8h3RNfMx4kquW8AOeS65yqhY1uisrig1b05u8kJmP2BIrlyTFxdJMZCe482NX5J4nG2tMY_SU3TQ2Efoj8UbccHSsxFVBhEVdsENVQ_F8wMw3IgZBbTorxmodo5GnRBy45ZGYrM7HocJ7fJfqILmJc2po827x11Kzgsvdv74xdj7vuyH75PJIWre5lGqzhhQU1Rmfy-ht3EXASgbOz7uO8hMqHGklpmU73jKSQpyMDjtzNnX0784ALbDqMJxRLoGYMCFNoFzUwSBqKszfsSluVs87aB445--jAmgSZ_v2B_rN_NtSKloOdRMm28I7S_OVrPG_B9YfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فوری: علیرضا کوشکی وینگر ۱۸۰ میلیاردی استقلال بعد از عملکرد ضعیفش تو بازی با نساجی به شدت از تعویضش عصبانی شد و بدون دست دادن با کادرفنی استقلال مستقیم به رختکن رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/138508" target="_blank">📅 21:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138506">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s4R3sRAIJEOKeh33I_FJLvU5kUlH1gqRm7TUYDir1XhS2SqSGGGuU8Ijed-Yqn2msFd6o36r8AbIBGqJrrHNUgpzK-S2QM2YAGRFK0iq9ipP76tImroo3iPOhhPtE9x_85dUOTaMBxaH3JLz3J_uGmhqeOUUtrHiossQwUewq5pD2Sn4vj4zBmjo5d6j_wQeXiblQpQPQHT-4hXCrXhFm_bzjsYhRRx-oLAg2WGEkAY19s5o0GUo8I2OLa37KRSbfJkFP4sc6XoSi2x6kUzUi33f4Fc1LWtxwfp4jfsbd23erRk4OuOSOguK6FUBuw3j2bjOA7a5EPBqlyfcuwhBqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/clPh_oXPAnvQqDIjyhyO2HIc7l5uzYSaaLb8EDflGX7emBLI5d8hJsKEkSvJWjzjE4-NQWZh8HprjjoeU_2gacCkUpVKFq5FhlTrl9LSDkEFlNm_f6HeO0hESA7K9TgD7Mvqb6Ye_C2KKXFphHXpvZOEbgNU2193zDrBgKFQPMfshaBYoATD2R2QJIx3GimJvxUeZ3hbUz4TJlSvvUExXN5ZfdrdgCHoyiW3vUZesKJlRqCvLliVpQDwDrsdBcyzv3mCFLuNLFJZvpErdnIYEmCwxbzL0Ex4HffbL0EvlITDd9vIky8T_9hEuXsjdIy2sdJV1eRADVj3fOMiMwIp9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#ارسالی
👀
⚽
هوادار مقیم امارات: امشب محمد قربانی به همراه همسرش دیدم.
✔️
خیلی مشتاق بود بیاد پرسپولیس،میگفت ولی چیزی دست من نیست باید باشگاهم همکاری کنه باهام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/138506" target="_blank">📅 20:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138505">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
تارتار: تمام بازی‌ها را باید به چشم فینال ببینیم استقلال خوزستان جوانان خوبی دارد اما محکوم به برد هستیم؛ بازیکنان فوق‌العاده خوب تمرین کرده‌اند و کار ما برای انتخاب ترکیب اصلی را سخت کرده‌اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/138505" target="_blank">📅 20:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138504">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
مهدی تارتار: عشق میکنم میبینم هوادارا تو نقل و انتقالات مطالبه گری میکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/138504" target="_blank">📅 20:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138503">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
فوری؛ مهدی تارتار : فردا چند تا از بازیکنان مون به علت خستگی نداریم و ترکیب شروع مون تغییر می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/138503" target="_blank">📅 20:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138502">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
تارتار: لقب تارتتا؟ من مهدی تارتار هستم!
❌
❌
اینکه هوادارن برای تقویت تیم، مطالبه می‌کنند جای تقدیر دارد و من از این موضوع خوشم می‌آید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/138502" target="_blank">📅 20:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138501">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
مهدی تارتار؛سرمربی پرسپولیس:
❌
مسئولیت نتایج و تعویض و ترکیب‌ها با سرمربی است و در تیم ما این موضوع جاافتاده است.
❌
لو رفتن ترکیب پرسپولیس؟!خیلی فضای مجازی را رصد نمی‌کنم و برخورد با کسی صحت ندارد.
❌
اعضای تیم ما از خانواده خود مراقبت می‌کنند.
❌
تا جلسه…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/138501" target="_blank">📅 20:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138500">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
تارتار: از هوادارا میخوام فردا ورزشگاه رو پر کنن ؛ من هنوز دو بازیکن دیگه میخوام.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/138500" target="_blank">📅 20:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138498">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
❌
مهدی تارتار؛سرمربی پرسپولیس:
❌
تنها هدف ما این است که می‌خواهیم بازی‌ها را ببریم و اگر با کلین‌شیت همراه باشد بهتر است اما بردن مهم‌تر است.
❌
قهر اوستون ارونوف؟!هنوز یکی دو بازیکن دیگر نیاز داریم و تیم کاملی نیستیم.
❌
در برخی پست‌ها کمبود بازیکن داریم و…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/138498" target="_blank">📅 20:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138497">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
زمان و مکان نشست خبری پیش از دیدار تیم‌های پرسپولیس و استقلال خوزستان مشخص شد.
❌
❌
نشست خبری سرمربیان دو تیم در هتل المپیک و طبق برنامه زمانی زیر برگزار خواهد شد:
❌
ساعت ۱۹، امیر خلیفه اصل | استقلال خوزستان
❌
ساعت ۱۹:۱۵ مهدی تارتار | پرسپولیس
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/138497" target="_blank">📅 20:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138496">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🤩
پیمان حدادی، مدیرعامل پرسپولیس:
❌
در موضوع اخذ مجوز حرفه ای باشگاه‌ها عده ای شایعه کردند سندسازی صورت گرفته، ممکن است برخی باشگاه‌ها چنین کرده باشند اما ما هیچ سند سازی نداشتیم و مجوزمان کاملا قانونی است. در ارتباط با قرارداد بازیکنان هم حاضر به شفاف سازی هستیم و از اینکه سازمان لیگ اعلام کرده لیست قراردادها را منتشر خواهد کرد هیچ دغدغه ای نداریم.
❌
قطعاً اطلاع دارید که دو باشگاه بزرگ پرسپولیس و استقلال زیان ده بودند. از طرفی در بدو ورود من به پرسپولیس پرونده هایی متعدد حقوقی وجود داشت که این پرونده ها فعالیت های مجموعه را تحت تاثیر قرار داده بود. امروز پس از گذشت حدود سه سال تقریبا هیچ پرونده داخلی و خارجی گریبانگیر باشگاه نیست. دغدغه دیگر ما،  اتخاذ روش‌هایی بوده و هست تا ضمن مرتفع کردن زیان انباشته گذشته با کسب درآمد پایدار، پشتگرمی به اسپانسرهای قوی و منابع در آمدی دیگر به خودکفایی برسیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/138496" target="_blank">📅 20:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138495">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNeTWsyKRn4EXxLgcnfhlOyQT3_v_xPaEF05CGnBq9ETQqc53m0BGRIfb3OkiGrlPFF9A4FoVxKdkoc3i26KF6rRudwhCUD9KIDRvlFHNyJpvNKgt1WiEbITQNyGipmJYbEXr2aPU5ywo9r6lwEjK6QZQh_7qm3AwF5UTMsUAOeNxBDW9kskPPEwum9Xyar7RkYKq7_Ii87Moajv_WU34fOBSKunKs_DN0X8yBHO1CWJ-q0RXNeioslY0KMvChEB8omR-XyUgZ_5DuusPOajA0x4HLF-YwvK86hkovSPrurhLjiGwmN6KK0WWdQvtlhLvvdvQj9BAg9kYo72rYgmng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽
اولین دوئل بزرگ فصل در نقش‌جهان!
سپاهان و تراکتور؛ جدال دو مدعی که برای صدرنشینی، از همین حالا شمشیرها را از رو بسته‌اند!
⚽️
لیگ خلیج‌فارس ایران
[
سپاهان
⚽️
🆚
⚽️
تراکتور
]
⏰
سه‌شنبه ساعت ۲۰:۰۰
🏟
استادیوم نقش‌جهان
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🌐
نسخه جدید سایت:
Sportn5b2.com
🌐
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/138495" target="_blank">📅 20:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138494">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
آسانی بازم فیکسه!
❌
مدیران نساجی ام گفته بودن مستندات جدیدی دارن، چه شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/138494" target="_blank">📅 18:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138493">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
✔️
✔️
شهاب زندی مدیرعامل نساجی: به مدیران ارشد استقلال هم تاکید‌ کردم مستنداتی دارم که آسانی‌ بازیکن غیرمجاز است و اگر مقابل ما امروز حتی یک دقیقه هم به میدان برود از آنها شکایت خواهیم کرد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/138493" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138492">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🎙
🎙
🎙
🎙
🎙</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/138492" target="_blank">📅 18:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138491">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🎙
🎙
🎙
🎙
🎙</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/138491" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138490">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🗣
🗣
🗣
فوووووری؛ مبین دهقان درخواست خروج از الوحده‌ امارات را داده است/ مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/138490" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138489">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
❌
❌
مهدی تارتار تصمیم داره دیگه حتی تو آخرین تمرین قبل از بازی هم ترکیب تیم رو اعلام نکنه تا ترکیب لو نره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/138489" target="_blank">📅 17:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138488">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
✅
در صورت خرید دهقان سهمیه لیگ برتری پرسپولیس نمیسوزه و ما همچنان یه خرید دیگه میتونیم بکنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/138488" target="_blank">📅 17:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138487">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✔️
✔️
✔️
یک خرید تا تکمیل یکی از بهترین نقل‌وانتقالات پرسپولیس
🗣
🗣
پیمان حدادی در تابستان امسال موفق شده حدود ۱۱، ۱۲ بازیکن جدید برای پرسپولیس جذب کند؛ بازیکنانی که بخش قابل توجهی از آنها جوان هستند و می‌توانند سال‌ها برای این تیم بازی کنند.
🗣
🗣
حالا فقط یک مهره…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/138487" target="_blank">📅 17:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138486">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✔️
✔️
✔️
یک خرید تا تکمیل یکی از بهترین نقل‌وانتقالات پرسپولیس
🗣
🗣
پیمان حدادی در تابستان امسال موفق شده حدود ۱۱، ۱۲ بازیکن جدید برای پرسپولیس جذب کند؛ بازیکنانی که بخش قابل توجهی از آنها جوان هستند و می‌توانند سال‌ها برای این تیم بازی کنند.
🗣
🗣
حالا فقط یک مهره…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/138486" target="_blank">📅 17:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138485">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
عشقم (دکتر جون )فقط یه قربانی
🥲
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/138485" target="_blank">📅 17:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138484">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
تارتار تمایلی به جذب مبین دهقان  نداره و گفته فقط قربانی/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/138484" target="_blank">📅 17:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138483">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
حدادی: دوران بازیکن سالاری و دخالت هوادار متمول در پرسپولیس تمام شده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/138483" target="_blank">📅 16:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138482">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
حاشیه جدید برای سرمربی زنان پرسپولیس
❌
باشگاه ایستا البرز مدعی شده نیلوفر اردلان با این تیم قرارداد سه‌ساله داشته و فسخ یک‌طرفه قراردادش قانونی نبوده است.  این موضوع در حالی مطرح شده که اردلان چند روز پیش به‌عنوان سرمربی تیم فوتبال بانوان پرسپولیس معرفی شد.…</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/138482" target="_blank">📅 15:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138481">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
❌
جدیدترین گزینه پیشنهادی پرسپولیس
✔️
✔️
امیرحسین ریوندی دفاع چپ ۲۲ ساله زسکا مسکو روسیه به تازگی به مهدی تارتار معرفی شده تا نظر نهایی خودش بابت انتقال اعلام کند
✔️
✔️
این بازیکن در بازی اکادمی کیا با زسکا مسکو مورد پسند روس ها قرار گرفت و در فینال جام حذفی…</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/138481" target="_blank">📅 15:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138480">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⭕️
⭕️
قرعه کشی لیگ نخبگان آسیا شروع شد؛
🎁
حریفان استقلال ایران: العین، السد، شباب‌الاهلی، نفتچی
🗣
🗣
کیسه خورد به پدرش العین و السد با عفیف و تیم سردار و سعید عزت الهی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/138480" target="_blank">📅 15:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138479">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
با رای کمیته انضباطی دیدار استقلال تهران و مس شهربابک 3 بر 0 به نفع مس شهربابک اعلام خواهد شد. این رای قطعی و ظرف چند روز آینده توسط فدراسیون فوتبال اعلام خواهد شد/ همشهری  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/138479" target="_blank">📅 15:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138478">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EalFJza7NNKKSPkb4rlyyz-UegQatbFA-71m0o9SMg-W-KOzwFMKGWBTT8cSaHQXfKJFCdS5Iw3EAcZQhVAzwKnJzWB7TVL68VfoHpz5U22RGw9QeaNwoW8VWKHtqTABQSOgypK1dByrI_7D4QwnBjpfKB7P6bv0OB94dZfzy-hGPFoZ_orErblSutYLtFJ_B2JTaPpRvR6fvuCXjH4ZFL1lX0mq5C__d35B7YMbeSxR5UySGpUzzlI_qoFdtK5KrbHvqhq3jK95Mg3U6Xj8lqT0PQnw0NjqhPWWBzXYmebNRPov2Kpv_5YQ2Q-c3xcz6lyTwh-cz_vrHIX3WFc_cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
⚽️
⚽️
خوشامدگویی باشگاه پرسپولیس به استقلال خوزستان
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/138478" target="_blank">📅 15:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138477">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
✔️
✔️
شهاب زندی مدیرعامل نساجی: به مدیران ارشد استقلال هم تاکید‌ کردم مستنداتی دارم که آسانی‌ بازیکن غیرمجاز است و اگر مقابل ما امروز حتی یک دقیقه هم به میدان برود از آنها شکایت خواهیم کرد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/138477" target="_blank">📅 14:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138476">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/138476" target="_blank">📅 14:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138475">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/138475" target="_blank">📅 14:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138474">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🚨
رسول باختر کارشناس حقوقی: یاسر آسانی بازیکن غیر مجاز است و دیدار استقلال و مس شهر بابک سه بر صفر خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/138474" target="_blank">📅 14:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138473">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
✔️
حریفان تراکتور: شباب‌الاهلی، الغرافه، الوصل، پاختاکور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/138473" target="_blank">📅 14:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138472">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6XWQtIXEgCZCyK1dcOLA0t7a5TSlLEL-GrIKvWZYDTiF_W9Oe-9Rd8zht-iquyZkIvLvOPGik-w6WNcs-khn0et5gek1uhBt_BeZbBbKtgpTiYV3VrWHBf4hJ1Vx2ZaaUoY8DSE6f4mVrRM-VCOze50i2L21KimvMTkdNd2i0_nCwayVPIARSd1Pf6yAiUqRwtf6PQZMRrq8C8nLRfzbACwUDWBmPJKH9m-K_GVCBWocZAiK6vHNE7dJDJ6ZmxtlRTmFVc2lGcmqo18RkMUtp8yDejEslI_fkhBUbNiLUxBrTcpI3OGAvpTyh-tHT8WFnwWBf949g9B9HWfRCTPAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽
جنگِ آبی‌ها در جهنم وطنی!
نساجی به‌دنبال شگفتی، استقلال به‌دنبال شکار ۳ امتیاز؛ قائمشهر امشب شاهد یک نبرد تمام‌عیار است!
⚽️
لیگ خلیج‌فارس ایران
[
نساجی
⚽️
🆚
⚽️
استقلال
]
⏰
سه‌شنبه ساعت ۱۹:۱۵
🏟
استادیوم وطنی قائمشهر
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🌐
نسخه جدید سایت:
Sportn5b2.com
🌐
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/138472" target="_blank">📅 13:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138471">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
✔️
✔️
حریفان استقلال و تراکتور
✔️
السد
✔️
العین
✔️
نفتچی
✅
شباب‌الاهلی
✔️
الوصل
✔️
الغرافه
✔️
پاختاکور
✔️
الشمال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/138471" target="_blank">📅 12:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138470">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
مبین دهقان در مصاحبه با همشهری انلاین اعلام کرد دوست دارد به پرسپولیس بازگردد
🔄
الوحده هنوز پاسخ نامه پرسپولیس را نداده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/138470" target="_blank">📅 12:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138469">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✅
✅
باشگاه تصمیم گرفت از رفتار اورونوف چشم‌پوشی کنه و حاشیه رو ادامه نده/ایران‌ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/138469" target="_blank">📅 12:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138468">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⭕️
⭕️
⭕️
😰
😰
شانس
🚨
🇮🇷
🇸🇦
رسمی؛ استقلال و تراکتور با خوش شانسی تمام به تیم‌های عربستانی نخوردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/138468" target="_blank">📅 12:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138467">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⭕️
⭕️
⭕️
😰
😰
شانس
🚨
🇮🇷
🇸🇦
رسمی؛ استقلال و تراکتور با خوش شانسی تمام به تیم‌های عربستانی نخوردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/138467" target="_blank">📅 11:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138466">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⭕️
⭕️
قرعه کشی لیگ نخبگان آسیا شروع شد؛
🎁
حریفان استقلال ایران: العین، السد، شباب‌الاهلی، نفتچی
🗣
🗣
کیسه خورد به پدرش العین و السد با عفیف و تیم سردار و سعید عزت الهی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/138466" target="_blank">📅 11:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138465">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
تا دقایق دیگه ببینیم کیسه و ترتر به کدوم تیما میخورن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/138465" target="_blank">📅 11:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138464">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
🤥
🤥
گفته میشه مبین دهقان آخرین خرید پرسپولیس هست و رضایت‌نامه اش هم زیاد سنگین نیست!  ۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/138464" target="_blank">📅 11:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138463">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
الوحده تمایل بیشتری داره که قربانی رو به اروپا بفروشه؛ تکلیف نهایی همه چیز تا ۴۸ ساعت آینده مشخص میشه/ورزش‌سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/138463" target="_blank">📅 11:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138462">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
سه بازیکن برتر زمین در دیدار پرسپولیس _ شمس‌آذر از نگاه متریکا :
✔️
✔️
محمد عمری: 7.84
✅
✅
ابوالفضل جلالی: 7.81
✔️
✔️
محمدمهدی محبی : 7.61  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/138462" target="_blank">📅 11:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138461">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
✅
سپهر خرمی: پرسپولیس امروز آخرین رایزنی رو برای جذب محمد قربانی از الوحده خواهد داشت
⏺
آخرین تلاش برای جذب بمب نقل و انتقالات که میتونه تیم رو تکمیل کنه.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/138461" target="_blank">📅 11:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138460">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
✔️
کنفدراسیون فوتبال آسیا حق انتخاب کشور میزبانی رو از استقلال گرفت، مدت زمان معرفی استادیوم دارای شرایط AFC توسط استقلال به پایان رسید و دیگر استقلالی نقشی در میزبانی خود ندارد!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/138460" target="_blank">📅 11:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138459">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
✔️
کنفدراسیون فوتبال آسیا حق انتخاب کشور میزبانی رو از استقلال گرفت، مدت زمان معرفی استادیوم دارای شرایط AFC توسط استقلال به پایان رسید و دیگر استقلالی نقشی در میزبانی خود ندارد!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/138459" target="_blank">📅 11:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138458">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf88a6445e.mp4?token=kCAAfxPmbuoNHarfvaerLZw-tuRtIT2VqSdMKVReZ-nSHsem8yCrw7ifY8l_AUw0AqVDq7ObH79NBGh0QDzXGLfqApf336-DrlLdcYuIWz3rqONPlQwK-a9wkDClwkfIWeY9a7PFt14Bda70MCxgyqgbIT-VNk3OnfdisvEcrul_bIixLSS0h4IKXug-WAMkeUxZNbavegD7Xq5yecuGzgUSiq1JOUXQvzY1AtSOKdVaW4fDti5hJ5eVBXVhHadQrBt55nqTsoty57TPaW-zFwoQe_da5fomhAG15dLQl6vmLjNVNZKyNpXFH3lWriMtndpFSeS0rl5wyRKcWsg6ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf88a6445e.mp4?token=kCAAfxPmbuoNHarfvaerLZw-tuRtIT2VqSdMKVReZ-nSHsem8yCrw7ifY8l_AUw0AqVDq7ObH79NBGh0QDzXGLfqApf336-DrlLdcYuIWz3rqONPlQwK-a9wkDClwkfIWeY9a7PFt14Bda70MCxgyqgbIT-VNk3OnfdisvEcrul_bIixLSS0h4IKXug-WAMkeUxZNbavegD7Xq5yecuGzgUSiq1JOUXQvzY1AtSOKdVaW4fDti5hJ5eVBXVhHadQrBt55nqTsoty57TPaW-zFwoQe_da5fomhAG15dLQl6vmLjNVNZKyNpXFH3lWriMtndpFSeS0rl5wyRKcWsg6ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پاس گل های برتر هفته اول در لیگ برتر در فصل ‎1405-1406 با حضور پاس‌گل ابوالفضل جلال به شمس آذر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/138458" target="_blank">📅 10:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138457">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
قرعه‌کشی فصل‌آینده لیگ‌نخبگان آسیا فردا ساعت ۱۱ صبح برگزار خواهد شد
✅
پ.ن استقلال و تراکتور بخورن به الهلال و النصر بخندیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/138457" target="_blank">📅 10:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138456">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⚡️
⚡️
شنیده میشه تیوی بیفوما در یک ماه اخیر برای ماندن در پرسپولیس زیر نظر پزشک تغذیه باشگاه 8 کیلو کاهش وزن داشته و علاوه بر اون زندگی حرفه ای شو سالم تر از قبل کرده و تمرکز اصلی شو روی فوتبال خودش گذاشته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/138456" target="_blank">📅 10:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138455">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
قیمت بلیط ورزشگاه قلعه حسن خان: 300 هزار تومانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/138455" target="_blank">📅 10:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138454">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5ezt_tJJMzAS9d7BRnmrIIW641RqV2j8LjkqPnEJSh48Q4RY2glyFo9IVaf4iJ8rjUiSiSlv9BAE1Cp92Tt_mvBhncN4JeFfY67jxcUs14z0mM0LJXbs1ineVat-oP-LMxqcfDwfmX8Ga66uhnBlfE8j5hkqkMt5IrjjZoklCsgcgWrUegwkVlqN5TU0sHlvmCcxMsTfSRUoGCyeS95Vc4AHFLlh1qn6PzHkFy98VW_Gp0fW0szvZAuYKsVfCKu0NOGzcICVdz1Wx8ZkSw7_QKifSHEfI67LfXh07896UYLLvlsnnIeuN2lwOVqVNqIBTkF4LB19YD1UdU5boowjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
🆕
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس دانیال ایری با شماره پیراهن ۸۹ برای پرسپولیس به میدان خواهد رفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/138454" target="_blank">📅 10:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138453">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">موجودی حساب : ۵هزار تومن  ادعا : ۱۰۰میلیارد دلار  ۱میلیون دلار بدینننن قربانی، ۳میلیون بدین حسین نژاد ۴ میلیون بدین قلی زاده ، وای تورو خدا اینار جذب کنید، دلالی کنید پول بیت المال رو ببرینید توش، من تو جیبم عنکبوت داره روپایی میزنه اشکال نداره بدید فوتبالیستای…</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/138453" target="_blank">📅 10:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138452">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">موجودی حساب : ۵هزار تومن  ادعا : ۱۰۰میلیارد دلار  ۱میلیون دلار بدینننن قربانی، ۳میلیون بدین حسین نژاد ۴ میلیون بدین قلی زاده ، وای تورو خدا اینار جذب کنید، دلالی کنید پول بیت المال رو ببرینید توش، من تو جیبم عنکبوت داره روپایی میزنه اشکال نداره بدید فوتبالیستای…</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/138452" target="_blank">📅 10:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138451">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_g1vJPyTx5vo4QlD3pVGT5oU505I3wQqBmrsxmlXkT3ZnNXy6S8osNV4I9C39uySefDt_oVI-cAQza0rZHik1fhKicuy3MeOLsbFb_JLsQaq-UTe-I_2dNvtEttCwaXDnMNR1ldLVrEvQYzjTdSMkkO57puZrrjqeRrqGz0cmH_8MxRio9eifiHKxZyljbbIyl3oep7iQf4SEzjUhjeeGvfNYekXUzdvV4y6kAvWf7UVhbvOuKeaacCg_prOK6N1rgxWNeFN23zB0NBqvRZ_lRCb4F4Du8PSth97TI0RKihLyyVy3bTdLHjpS79QgUwkr8afrJ3vDxBvwtsvWsucw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
پرسپولیس در یک پرونده حقوقی برنده شد
❌
❌
باشگاه پرسپولیس اعلام کرد دعوای حقوقی مطرح شده از سوی یک شرکت علیه باشگاه پرسپولیس، در دادگاه تجدید نظر استان تهران رد و رأی به سود سرخپوشان صادر شده است.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/138451" target="_blank">📅 10:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138450">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMhmdrza</strong></div>
<div class="tg-text">موجودی حساب : ۵هزار تومن
ادعا : ۱۰۰میلیارد دلار
۱میلیون دلار بدینننن قربانی، ۳میلیون بدین حسین نژاد ۴ میلیون بدین قلی زاده ، وای تورو خدا اینار جذب کنید، دلالی کنید پول بیت المال رو ببرینید توش، من تو جیبم عنکبوت داره روپایی میزنه اشکال نداره بدید فوتبالیستای ممادر خوب بخورن
🤣
🤣</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/138450" target="_blank">📅 10:07 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138449">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5L1oZDSwIC7T0-2itoqoCNqsMy3nzGQs3hlJWpAVGRC9y6q7WXK1-ryd7jSFEl9HGG9DDcH7Bci2y2U49T1-nZg1PT8dxeXhcTT-rXHW2uPO5Y9TR5uYoUcON1mJS43jlx-5rn_ahKiMBAUrTiU7RKIiTX7OuIy3Tgl0lCn7N2MCw9L6J5S8hMF70XQ7MwvKOr6IW9HbMb3obDDUhELG-EyeDkyVjU5iI-kGriaHj1fK2o-ti0zoK-Cw-a7el2khshsx1YYrzxohfeMwi7TSJ0J-JZKcMBpkpsxmfeS2A8j_hI6x4TAUij28Uc6MMApicAxGKGh6VUIDJCRAljDYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بیانیه باشگاه گل‌گهر علیه میثاقی در ماجرای تورنمنت 3جانبه و پرونده چادرملو
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/138449" target="_blank">📅 10:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138448">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddw9ImfEqgci73GymsDgoJOmXw7PWC9RoqJWCrG-A004ili0e0H5XQHfC4M1918qnJWnnAHJw_x_mR5zEK87YlGLelhvH1zFTqvtAu8u7fUYIk-vLwtYEGlupsqVgeQwdf_N4B68YQ2KWRjv1NjMfij8KrINK2YSafANTQaTHVVNRkkBb0PEIN-oVciU-fk-qmewmMjdKeHFds08Jl7I4firKMOu4anB-tzeXQgI_eoeA93dMceAwQrQCGDebz1jtzsQ7jG27aEnDLwUnmTmb9753dVlBvp2cp3s5F3Mabdsdqo8f3L165CoUFey589QHFlqfntF7Ki1hZHfbFizjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بازی های امروز لیگ برتر:
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/138448" target="_blank">📅 10:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138447">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✔️
✔️
💸
سود 355 هزار یورویی باشگاه نساجی از فروش 2 بازیکنی که حتی 1 دقیقه برای این تیم بازی نکردن!
🔴
دانیال ایری:
🔄
خرید با 405 هزار یورو
🔄
فروش با 600 هزار یورو
🟡
کسری طاهری:
🔄
خرید با 703 هزار یورو
🔄
فروش با 863 هزار یورو
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/138447" target="_blank">📅 10:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138446">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
قرعه‌کشی فصل‌آینده لیگ‌نخبگان آسیا فردا ساعت ۱۱ صبح برگزار خواهد شد
✅
پ.ن استقلال و تراکتور بخورن به الهلال و النصر بخندیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/138446" target="_blank">📅 09:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138445">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اصلا چه جوی راجب باشگاه؟ باشگاه مگه بد عمل کرده تو نقل و انتقالات. یه تیم تو زمین داریم یه تیم کامل رو‌ نیمکت. پنج ، شش تاهم بیرون از لیست که هرکدوم یه زمانی فیکس بودن. همین هفته اول ۱۶ نفر بازی کردن که همه خوب بودن ، اورونوف ، سرگیف ، باکیچ و چندتای دیگه…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/138445" target="_blank">📅 09:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138444">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromhamed</strong></div>
<div class="tg-text">اصلا چه جوی راجب باشگاه؟
باشگاه مگه بد عمل کرده تو نقل و انتقالات.
یه تیم تو زمین داریم یه تیم کامل رو‌ نیمکت.
پنج ، شش تاهم بیرون از لیست که هرکدوم یه زمانی فیکس بودن.
همین هفته اول ۱۶ نفر بازی کردن که همه خوب بودن ، اورونوف ، سرگیف ، باکیچ و چندتای دیگه بازی نکردن.</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/138444" target="_blank">📅 09:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138443">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
🆕
🏅
به گزارش رسانه «سرخ تایمز» و طبق گفته های عضو هیئت مدیره باشگاه پرسپولیس، باشگاه مصر هست تا محمد قربانی رو به خدمت بگیره و خود محمد قربانی هم علاقه منده تا به پرسپولیس بیاد اما مشکل اینجاست باشگاه الوحده داره بازی در میاره و تا الان…</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/138443" target="_blank">📅 09:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138442">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
✅
سپهر خرمی: پرسپولیس امروز آخرین رایزنی رو برای جذب محمد قربانی از الوحده خواهد داشت
⏺
آخرین تلاش برای جذب بمب نقل و انتقالات که میتونه تیم رو تکمیل کنه.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/138442" target="_blank">📅 08:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138441">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mD1PbUHk73sCW6R3RwvXpLM4cwktVz3zZl4qjzv8MQz-PjDs5mIuKm3Xaoxs3FTjY6Szp_cR8t0wmup_np7_itRCpJ7e4j7YOQbTPUS-nqxz_NXk_t7YBE95h8SmRo6ZtTr4FoUAv34b30-TKftWyONvUm-lTyr2P7b56585sxOuhfxhShiDYpBEIZbYqvSAg81fxcsXSKSw-kFi17n1-GOeHHcOXC4k8emoEhrh-SzlfuQJh6ReZosJYgxMekvCO-860bP1XZSZnwlUgEWlEOmbNS4c7AVLee6LeG6uOiAo_sI6lGsv2TyCnk3c0hwvxdyFH_W091JzT8MrP_QSkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/138441" target="_blank">📅 08:42 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
