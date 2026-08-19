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
<img src="https://cdn4.telesco.pe/file/S5MCnZJDAdSMxyFbmzelaw5waxrF2xudSBw4Pp1sB0QWtjf56TqnhZIAeVnA0MVCsKNLOvSqbUy2rrPdn1jefQNXAETX8tv_82EbcGqqms2fcs7RyJJOkIn2ghhiSbfZDt9-tPhjJEgupO4UprXlsWcjaZnufXObGzklyJOQvQIVPPrzzmNlHgrK-ZrJf_cQYmte0sT_9jhKD7RX2wFKPwBtVYvVqSVmMR-3-KR1-ZQ6ELH_nJySxe4EWJm_IdZktWn4gUyNgD68mWzRtUN1jn3fDbsgqf3CgcN2mhSJ5ZxJrBAy7BswdDYIh220V_AU-21Li8wzMQmEqfH58dLeKQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 20:48:42</div>
<hr>

<div class="tg-post" id="msg-138592">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⚡️
گل سوم هم زدیم ...بلند شید و این تیم و ایستاده تشویق کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 154 · <a href="https://t.me/SorkhTimes/138592" target="_blank">📅 20:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138591">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
همگی باید کلاه از روی سر برداریم و ایستاده این تیم و تشویق کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 669 · <a href="https://t.me/SorkhTimes/138591" target="_blank">📅 20:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138590">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
✅
نیمه دوم میتونیم شاهد ورود اورونوف و شهرآبادی و تیکدری به زمین باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 849 · <a href="https://t.me/SorkhTimes/138590" target="_blank">📅 20:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138589">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_lgBu7cho_U6fihpQvU6zkJwH7AX0mWb27QEAmjZ0Vqknq1qX-cWjfBe1r7knCRHVskoediJXtW4xwV9gnrvujCStcgCpqDKU4tqJYX-JqEjkNu9MkUvVQVVuusJgkOunJsy63AFEsjQTZojWyQQ6MmuX25F4ecwdm2TpYxMJPJNpEqZNLqLFvxsjKZn9IGHFJElKPzpdrknYLJK8pmvPks2H4eEv6QUNhf8nBPKMDfH8IB8qiCjkt37V4rVRFXWMUOeQFNYHfr1qNu1XoFGxhHjRsKYbGDrBUWdK7DwBnlgETttTpY6JXDGdeizCkCrSFvilA7QQeU9dBElKP5Yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/SorkhTimes/138589" target="_blank">📅 20:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138588">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
مثل نیمه اول با اختلاف زارع بهترین بازیکن زمین بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/SorkhTimes/138588" target="_blank">📅 20:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138587">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
نیمه اول و با دو گل پیروز شدیم ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/138587" target="_blank">📅 20:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138586">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
گل دوم هم علیپور زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SorkhTimes/138586" target="_blank">📅 20:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138585">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
⚽️
بااعلام‌باشگاه پرسپولیس؛ مصدومیت ابوالفضل جلالی جدی نیست و این بازیکن مشکلی برای دیدار هفته آینده مقابل استقلال خوزستان ندارد. جلالی امروز بازی  درخشانی در ترکیب سرخ‌ها داشت.  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SorkhTimes/138585" target="_blank">📅 20:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138584">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
باید برای این پرسپولیس تارتار ..تیم جذاب و هجومی با احترام حرف بزنیم ..چه تیمی درست کرده تارتار.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/138584" target="_blank">📅 19:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138583">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
✅
گل اول و خیلی زود توسط خدابنده لو زدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/138583" target="_blank">📅 19:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138582">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
با اختلاف سه گل ببریم میریم صدر جدول..الهی به امید تو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/138582" target="_blank">📅 19:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138581">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⚡️
⚡️
جمعیت خوبی هم رفته دم هوادار گرم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/138581" target="_blank">📅 19:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138580">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
با اختلاف سه گل ببریم میریم صدر جدول..الهی به امید تو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SorkhTimes/138580" target="_blank">📅 19:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138579">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
🔴
📸
شماتیک ترکیب پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SorkhTimes/138579" target="_blank">📅 19:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138578">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
🔴
📸
شماتیک ترکیب پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/138578" target="_blank">📅 18:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138577">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
نسبت به بازی اول فقط جای سرگیف و بیفوما تغییر کرده و همچنان اورونوف روی نیمکت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/138577" target="_blank">📅 18:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138576">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
🔴
📸
شماتیک ترکیب پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/138576" target="_blank">📅 18:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138575">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5SkboM3RZN9xZSRAjKjx432V666TWfdLmoSPML7BCYHi0Qq_37PkyiPKe10-K6e7y6Vj2jKqpdDZtRqnk7lrxX35Y6aqNuABY2_9MjxiPkUVhtqSUhKizJ1Cb4eD6F7OVoq_1sudvbRlIbYfDW2A5P6M6Y72957wauMUgJRzzocbDtiBnJrBaacN238U87GjBeO9CpghYyfBpGNNv9s8R9oMMD3aJqjsg4MNCwBvioLB6t32puTdLmruhqAKWTJB1sFW31bxoAuht4qL3ceY9Jwfhj1NvPHzoBVKCE6YrhhjEPHq632w-_qBiIdR1QKyrmMLMw0LaBSpzbiinErCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
شماتیک ترکیب پرسپولیس برابر شمس‌آذر  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/138575" target="_blank">📅 18:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138574">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d137678386.mp4?token=RZqlqT4FPAmSdEcflafwbaVql0FKZOcjrBHgcfTUIi5-70YkLxTcnUiiYpM551KWb83WQry0ynpjNRV7fhTxHVN1axWSLSPqlNYbh8Vnz8lwCEq1hCXm0wUZzYMCDSfXJ-WI3Dd0SPVbajPDPJPj1SViD1IyjvxaGDlRhQELfZej2V9QoWS8GqIvhzP6QDBeTC8i3lvwzxfp5yxKHWbU5RpW41gMSbD9UtTRR3nWOEzo7zgqOIk9bq6_XtBpc7pNEUvu5aO4U-0_4-gKRnNBJdh6h16P9BF9vwEhYjs4EGfyYU8PCQeni1BEDiOsuUac-pfyqzARDtBD5-96REQHTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d137678386.mp4?token=RZqlqT4FPAmSdEcflafwbaVql0FKZOcjrBHgcfTUIi5-70YkLxTcnUiiYpM551KWb83WQry0ynpjNRV7fhTxHVN1axWSLSPqlNYbh8Vnz8lwCEq1hCXm0wUZzYMCDSfXJ-WI3Dd0SPVbajPDPJPj1SViD1IyjvxaGDlRhQELfZej2V9QoWS8GqIvhzP6QDBeTC8i3lvwzxfp5yxKHWbU5RpW41gMSbD9UtTRR3nWOEzo7zgqOIk9bq6_XtBpc7pNEUvu5aO4U-0_4-gKRnNBJdh6h16P9BF9vwEhYjs4EGfyYU8PCQeni1BEDiOsuUac-pfyqzARDtBD5-96REQHTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
‼️
هوادار پرسپولیس: تیمی که ۷ گل خورده و دسته سه رفته، به ما نمی‌خوره! فینال آسیا واقعی رو ما دیدیم. استقلال بره آسیا ۷ تا بخوره، خوشحال میشیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/138574" target="_blank">📅 18:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138573">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff8f1d1ef5.mp4?token=M0QMToN37a0nt1TxLTDV-YJgJZzolj8aWbuvf-sFmVTx3S45PFUDIw-Sncw0ol6oDkae0DtagJDswQNeVB_dOEEOnpEVq23cKmBNrTWoNz-oG-P8CprpZVbvJ4y4ZQfv9V2Q_nCIq3juRonKPnOz5XxlwBFMppxfR7f_l78kJTFfJJdVWfnPKFyZKcK__ciUHPz4NHrG6Rz3Au0hdakuN9XLjl_ssNTk-JVkd6e5h8p5w0aiCN3wValtXMQmesqN7crxCwkS56N1zfbTi4RUvkM8sBqpq5WhNecq3DGwucVVRByiKJro6239XtqAtajM67s7OC36L1aKOS6-PVH2Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff8f1d1ef5.mp4?token=M0QMToN37a0nt1TxLTDV-YJgJZzolj8aWbuvf-sFmVTx3S45PFUDIw-Sncw0ol6oDkae0DtagJDswQNeVB_dOEEOnpEVq23cKmBNrTWoNz-oG-P8CprpZVbvJ4y4ZQfv9V2Q_nCIq3juRonKPnOz5XxlwBFMppxfR7f_l78kJTFfJJdVWfnPKFyZKcK__ciUHPz4NHrG6Rz3Au0hdakuN9XLjl_ssNTk-JVkd6e5h8p5w0aiCN3wValtXMQmesqN7crxCwkS56N1zfbTi4RUvkM8sBqpq5WhNecq3DGwucVVRByiKJro6239XtqAtajM67s7OC36L1aKOS6-PVH2Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
🔴
هوادار پرسپولیس: از رنگ آبی و استقلال نفرت دارم! تارتار تیم خوبی ساخته و پرسپولیس همیشه قهرمانه. استقلال تیم نیست، عروس آسیا هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/138573" target="_blank">📅 18:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138572">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a524ae095.mp4?token=PO7r9zb__K03ULbQRWLmEozbOV5KxwQvAzJHQKaaVopZ7UOw5IdUYDxqy2ZDyJWzJrPtGw9T26eaYCz88P5DiXb1BQdUkLBddrh6yCEJ-O-ei0k9jkCX19EgDm45qu1JIwFhi2RxXhsyrgIUPFn_g1jOn3aJI0fIULJJuI2JOVQE23u4YOQEUBe4wslbrJ4c7KecyySv9cw7UUuXuvK01KfRJLkDDLC4hBykQ6JbkugRH-AUX6KTVCJ9H2Q4OeEisLNBJvSDVSiQFyYxu4SdhreHeincx3xJ2gLLXg45C34R40cZCkUgvIS9p_8OMy7oEbyePbybeYuwTRTSkVXcBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a524ae095.mp4?token=PO7r9zb__K03ULbQRWLmEozbOV5KxwQvAzJHQKaaVopZ7UOw5IdUYDxqy2ZDyJWzJrPtGw9T26eaYCz88P5DiXb1BQdUkLBddrh6yCEJ-O-ei0k9jkCX19EgDm45qu1JIwFhi2RxXhsyrgIUPFn_g1jOn3aJI0fIULJJuI2JOVQE23u4YOQEUBe4wslbrJ4c7KecyySv9cw7UUuXuvK01KfRJLkDDLC4hBykQ6JbkugRH-AUX6KTVCJ9H2Q4OeEisLNBJvSDVSiQFyYxu4SdhreHeincx3xJ2gLLXg45C34R40cZCkUgvIS9p_8OMy7oEbyePbybeYuwTRTSkVXcBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏅
وضعیت ورزشگاه شهرقدس در فاصله یک ساعت و نیم تا شروع بازی پرسپولیس.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/138572" target="_blank">📅 18:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138571">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3a1e95c93.mp4?token=tOTlMSDd_HE6BzREFE0LvJ0PlxtX5mN5PpvPr8isrO8Ydin8NArE0c8V_DRzbQxRJ8uRa4qC9OsACLNBfP1hvclCKNMU4_BB68JyDJaTmmUXoTlWoow2xxblrccgnfEZpxAQ542W_WgzbhgvEQh1OYS1M5LyEccv2tqF2F0KNJ0pc6x5o11xkiXBDe3KXb4cGq01MkpOvnmzGy1X-PXu-_M5haIejCNX2LdCjNt3aKzZnHKgId75jVd5q-ew_q6vWVQH8ZW1Z2kSGTXaNA4axnUVPXHiD-V5ZmyUcCweuJFmn-mCqTbNyKj7YgVjAVWnfDNmML-qSSmGtwOi0BTSNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3a1e95c93.mp4?token=tOTlMSDd_HE6BzREFE0LvJ0PlxtX5mN5PpvPr8isrO8Ydin8NArE0c8V_DRzbQxRJ8uRa4qC9OsACLNBfP1hvclCKNMU4_BB68JyDJaTmmUXoTlWoow2xxblrccgnfEZpxAQ542W_WgzbhgvEQh1OYS1M5LyEccv2tqF2F0KNJ0pc6x5o11xkiXBDe3KXb4cGq01MkpOvnmzGy1X-PXu-_M5haIejCNX2LdCjNt3aKzZnHKgId75jVd5q-ew_q6vWVQH8ZW1Z2kSGTXaNA4axnUVPXHiD-V5ZmyUcCweuJFmn-mCqTbNyKj7YgVjAVWnfDNmML-qSSmGtwOi0BTSNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ورود اتوبوس تیم به ورزشگاه برای مصاف با استقلال خوزستان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/138571" target="_blank">📅 18:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138570">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⚡️
مدیر برنامه آسانی: نامه فسخ دستکاری شده است
🔹
مدیر برنامه یاسر آسانی، هافبک استقلال، انتشار نامه فسخ قرارداد این بازیکن را تکذیب کرد و مدعی شد نامه منتشرشده با هوش مصنوعی دستکاری شده است.
🔹
رسانه‌های مختلف امروز نامه‌ای منتسب به فسخ قرارداد یاسر آسانی با…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/138570" target="_blank">📅 16:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138569">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
دانیال ایری در لیست پرسپولیس برای دیدار با استقلال خوزستان قرار گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/138569" target="_blank">📅 16:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138568">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
❌
شوک بزرگ به طویله کیسه/ نامه مشاور حقوقی یاسر آسانی که اعلام کرده قرارداد رسما فسخ شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/138568" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138567">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gh8fRqQqG4Zx-5HAWUNF2h8N70bQ773WQvXFJzC36ttvReDQqt5qZUOB2ALDFEPr7_eE9uLKPQopltnRp9M_GHtKpGM1z3GA1rPX-kK4T7FD92QF-vG-pG5KV9qAM11PrwewuPUG9jdiSzd1gwmmEHZtpX-iX6oxCFSmmb5B0Ln_QlqlYCqdlQMhoYxCA0ecePPryamF9v-eXVO7ZSQiO8Oa1YJV3am50-kCTUrxNMaoO6ZFAGNhbD7_DGO_O78wSZLI70pV-FG_WHKBsdKik7vUJM07SXP2x8vYtoXDHFVZEtyJno1w_nTCchW6N5zHI4ASv1Sr1LDdhShEdI6Lug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رسمی؛ با اعلام سازمان لیگ دربی پایتخت برای اولین‌بار قرار است در اصفهان و ورزشگاه نقش جهان برگزار شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/138567" target="_blank">📅 16:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138566">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1Xt_d1hIS0PqqZvQP1yZmYLs0zFL9cIIMoXM2Uh81DwsPSFZ-StMhVmX1x9zLFwKieE1EZp_FgQtA5TzaJzyW9ccc0NgLVZNH18DpamRoTORCOpZ7cU2HrBFa58_3bC-DiiRUuLw17Nyjn-K3nVkTNuxqD7K7Gl0Ieh79YJBcZDO9WeqKunftB9iMt2m0LUsIlTLZ3aGCqH4nQCGVNxZGFnA1QRJxWL--YNeCS6RsUe3qRJEbTAmbRUezAlQYMnYNSuUu0ANhMBkEVD-ICN2apTTwlLklSxDHkylHmZN1Dl8qOP6SX8TSR14yvZQK2EOkkUSffH2xythc14VWz5uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
استوری وحیدقلیچ: رییس فدراسیون فوتبال روسیه دنبال منه
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/138566" target="_blank">📅 16:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138565">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">📊
🇮🇷
🇮🇷
نتایج ۵ بازی رودررو اخیر پرسپولیس و استقلال خوزستان:
🇮🇷
پرسپولیس ۳-۰ استقلال.خ
🫱🏻‍🫲🏻
پرسپولیس ۰-۰ استقلال.خ
🇮🇷
استقلال.خ ۱-۰ پرسپولیس
🇮🇷
پرسپولیس ۴-۳ استقلال.خ
🫱🏻‍🫲🏻
استقلال.خ ۲-۲ پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/138565" target="_blank">📅 16:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138564">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e06320f5f.mp4?token=gl0UF5OerE0_YFxoYDebJuFr2sqXbWQ3BpgnuUr0wvLHoY45b76kPzMokWID1TfWPdGLRxZWAj84WPAnI5VWQEAXGGabsB0GEXf3rdfPQ-UkbCi8bA2cHLCvs3B0Dh8cW0CU66TUPAKm7oZlSUkKjhHVJkC-jRJSR1ea7NsW7Ejd9ioKw7KMH7JYymCyAWiHJ4p4ewOS2WFNTzwEGrtXransNVuOXHIrZkjRkjxVux4QQlulzZi_6ID2Y4B1Vzywd3phoG-yEk3HztbJxddp4H3eyDBDP83Ya5z4bTOiQxYqGQHvjJif5OEcOXirIl7poqAx1TUvEsZMi8Z048RtNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e06320f5f.mp4?token=gl0UF5OerE0_YFxoYDebJuFr2sqXbWQ3BpgnuUr0wvLHoY45b76kPzMokWID1TfWPdGLRxZWAj84WPAnI5VWQEAXGGabsB0GEXf3rdfPQ-UkbCi8bA2cHLCvs3B0Dh8cW0CU66TUPAKm7oZlSUkKjhHVJkC-jRJSR1ea7NsW7Ejd9ioKw7KMH7JYymCyAWiHJ4p4ewOS2WFNTzwEGrtXransNVuOXHIrZkjRkjxVux4QQlulzZi_6ID2Y4B1Vzywd3phoG-yEk3HztbJxddp4H3eyDBDP83Ya5z4bTOiQxYqGQHvjJif5OEcOXirIl7poqAx1TUvEsZMi8Z048RtNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏟
ثابت قدم مدیرعامل شرکت توسعه و تجهیز:
ورزشگاه آزادی اویل آذرماه آماده می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/138564" target="_blank">📅 16:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138563">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2698fac3f.mp4?token=bNUIiMQ7cIBrbemoZYJ8J2FOve7nOa5JE9VFj9PiIPIABq32BMftdsghaAzcl6mbSJWAgwZtclUr1KROjA3a38d9JXPl3VX6jSHJGB1LNoL1LxlRQ9n7jOqJ5sK1xhwSVaz2i0iTA24ag75xFyApP92IwA5UNS0a0QCHtGEJRXRhBVIeQ5KgFdITcmE_T-YKNRY9Ut3UB5Bnw69HU7dTCLXx_8-OwViu1oyWUCx6AqAUQpkRResJMLvcXlDB0BGGLAXnl2oSphZBpMbn5fKXAZN4d1tZ2QIlZxj-rLtvbgQ-R9LXpclhm5DXC8l0iOaX7Lx3mlRYkFulgrotcfnjYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2698fac3f.mp4?token=bNUIiMQ7cIBrbemoZYJ8J2FOve7nOa5JE9VFj9PiIPIABq32BMftdsghaAzcl6mbSJWAgwZtclUr1KROjA3a38d9JXPl3VX6jSHJGB1LNoL1LxlRQ9n7jOqJ5sK1xhwSVaz2i0iTA24ag75xFyApP92IwA5UNS0a0QCHtGEJRXRhBVIeQ5KgFdITcmE_T-YKNRY9Ut3UB5Bnw69HU7dTCLXx_8-OwViu1oyWUCx6AqAUQpkRResJMLvcXlDB0BGGLAXnl2oSphZBpMbn5fKXAZN4d1tZ2QIlZxj-rLtvbgQ-R9LXpclhm5DXC8l0iOaX7Lx3mlRYkFulgrotcfnjYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⛔️
آقای کمیته انضباطی اگر یکبار به صورت قاطع برخورد کرده بودید و درگیر رانت و فساد تلفن بازی نمیشدید،الان کشالش رو میکرد تو
کون
ناموسش به مردم توهین نمیکرد مسبب این بی قانونی و فساد اخلاقی رفتاری شما حضرات هستید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/138563" target="_blank">📅 16:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138562">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
✅
✅
کمیته انضباطی قصد دارد به صورت ویژه شادی گل جنجالی شب گذشته شجاع خلیل زاده را مورد بررسی قرار دهد و با توجه به سابقه او در انجام شادی های جنجالی، احتمال محرومیتش وجود دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/138562" target="_blank">📅 14:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138561">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
❌
کشوری فرد دبیر سازمان لیگ برای بازدید از ورزشگاه نقش‌جهان در این ورزشگاه حضور یافت. بر این اساس، احتمال دارد دربی استقلال و پرسپولیس در هفته پنجم، روز 11 شهریور در نقش‌جهان اصفهان برگزار شود.
✔️
✔️
گزارشگر دیدار روز گذشته سپاهان و تراکتور نیز در جریان مسابقه…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/138561" target="_blank">📅 14:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138560">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byAW3CJWweLTRhGawcWhaGQ2P9GB1wk4SPaDzJ2sPagsKCOlKn1nTFLaAaQY3sq71Ki8rQ_6h8r1veiJm2dpFlYGePjXqLPBm3ksY6xaDt-4KB_yl97LHU3lLTQh5JLXttSm1-VwkHGWGe9PkxyCTimojNcGBWmRfpbMe9mzlRvLHT1bf2vc-G09fe08skk9fbNboE_WQiHyFzLb7QbWx93LFwjs3I8TLX-uLdnikPBfnGeXVXF6cXvISNK38cQcJawiWABKBcfLigp0VAGfhaFYfH06X5HIE7BZc2ztM9dhovb6uT30i5cCumm0hgO7xs4nM0ctGAfEV08Jh7OOPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽
نبرد سرخ‌ها با آبی‌های خوزستان؛
پرسپولیس برای شروعی قدرتمند، استقلال خوزستان به‌دنبال غافلگیری!
⚽️
لیگ خلیج‌فارس ایران
[
پرسپولیس
⚽
🆚
🇮🇷
استقلال‌خوزستان
]
⏰
چهارشنبه ساعت ۱۹:۳۰
🏟
استادیوم شهرقدس
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
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/138560" target="_blank">📅 13:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138559">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
با درخواست کیسه به عنوان میزبان دربی ، دربی رفت به احتمال خیلی زیاد اصفهان و ورزشگاه نقش جهان باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/138559" target="_blank">📅 12:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138558">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
فوری؛ باشگاه نساجی مازندران از باشگاه استقلال تهران شکایت کرد
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/138558" target="_blank">📅 12:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138557">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
محمد گندمی، یعقوب براجعه، دنیل گرا، امیرحسین طاهری، علیرضا عنایت زاده و کوروش اژدهاکش از لیست پرسپولیس برای بازی فردا خط خوردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/138557" target="_blank">📅 12:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138556">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
⚽
باز هم حرکت عجیب و منشوری شجاع خلیل‌زاده، بعد از خوشحالیِ گل!!!
❌
پ.ن و بازم کشاله ران بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/138556" target="_blank">📅 12:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138555">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
آسانی بازم فیکسه!
❌
مدیران نساجی ام گفته بودن مستندات جدیدی دارن، چه شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/138555" target="_blank">📅 12:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138554">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
قدوسی: پرسپولیس و تراکتور میدونن که الوحده قربانی رو نمیده ولی از ترس اینکه اون یکی جذبش کنه پا پس نمیکشن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/138554" target="_blank">📅 10:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138553">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
فوری: بازی تراکتور و پرسپولیس در هفته سوم بدون تماشاگر برگزار خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/138553" target="_blank">📅 10:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138552">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
⚽️
🧡
رامین رضاییان میان تشویق شدید هواداران فولاد با شعار « رامین، رامین، رامین ما دوست داریم » وارد خوزستان شد؛ فقط کلاه رامین رو ببینید
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/138552" target="_blank">📅 10:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138551">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
مهدی تارتار قصد دارد از سیستم چرخشی در هفته های ابتدایی استفاده کند تا ضمن آمادگی تمامی بازیکنان فشار کمتری به تیم وارد شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/138551" target="_blank">📅 10:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138550">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
جنجالی‌ترین بازی هفته سوم بدون تماشاگر
‼️
✔️
✔️
تراکتور و پرسپولیس هفته آینده باید در دیداری حساس پشت درهای بسته به مصاف هم بروند. تراکتوری‌ها حالا به دنبال تعلیق محرومیت هواداران هستند تا سکوهای تیم‌شان را پس بگیرند؛ تصمیمی که می‌تواند روی بازی برگشت در…</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/138550" target="_blank">📅 10:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138549">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/138549" target="_blank">📅 01:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138548">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
حسین زاده :بهمون گفتن بازی با پرسپولیس بدون تماشاگره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/138548" target="_blank">📅 01:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138547">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
✔️
✔️
تارتار تو تمرین امروز چند تا ترکیب چیده و هر کدوم در یک رسانه قرار گرفته
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/138547" target="_blank">📅 01:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138546">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/138546" target="_blank">📅 00:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138545">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❤️
گل اول تراکتور به سپاهان توسط امیرحسین حسین زاده 83
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/138545" target="_blank">📅 00:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138543">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
❌
مهدی تارتار تصمیم داره دیگه حتی تو آخرین تمرین قبل از بازی هم ترکیب تیم رو اعلام نکنه تا ترکیب لو نره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/138543" target="_blank">📅 00:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138542">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🏟️
آخرین وضعیت سکوهای ورزشگاه آزادی و وضعیت زهکشی و زیرسازی چمن این ورزشگاه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/138542" target="_blank">📅 00:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138541">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
⚽
باز هم حرکت عجیب و منشوری شجاع خلیل‌زاده، بعد از خوشحالیِ گل!!!
❌
پ.ن و بازم کشاله ران بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/138541" target="_blank">📅 00:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138540">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✔️
✔️
البته طبق حکم دایمی بازی لیگ دو تیم پرسپولیس و تراکتور بدون تماشاگره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/138540" target="_blank">📅 23:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138539">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
مس شهربابک از استقلال به خاطر استفاده از آسانی شکایت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/138539" target="_blank">📅 23:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138538">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
عینک‌زاده: فوتبال دعوا نباشد که لذت ندارد باید دعوا کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/138538" target="_blank">📅 23:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138537">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
⚽
باز هم حرکت عجیب و منشوری شجاع خلیل‌زاده، بعد از خوشحالیِ گل!!!
❌
پ.ن و بازم کشاله ران بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/138537" target="_blank">📅 23:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138536">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/138536" target="_blank">📅 23:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138535">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/138535" target="_blank">📅 23:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138533">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
🆕
🏅
به گزارش رسانه «سرخ تایمز» و طبق گفته های عضو هیئت مدیره باشگاه پرسپولیس، باشگاه مصر هست تا محمد قربانی رو به خدمت بگیره و خود محمد قربانی هم علاقه منده تا به پرسپولیس بیاد اما مشکل اینجاست باشگاه الوحده داره بازی در میاره و تا الان…</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/138533" target="_blank">📅 23:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138532">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0VgKM0HTQo1jNhyQ6UgNNYRdzyLjbICusGvpaNfEyfxUYhXE1Fo23cr_GOi3oQjgktcxCtWMtuGOPRnQJCD4OknNasDgIPUFOyUzJ9u5d9BkM5Cwr6XAPhnxQqiVjkLgorofs7TWo-yRgEtZhAqYFiPIaFHq3oEIJBB9XthpVhYahgms7skwT1cYppeX2CaM0xav62EP6NPkOxY2Zpozxnmw-mohdaUpHrWrfByAz4E8wnFTxek-LHx7SwXOCONDZh-geGhoUenouWDHOhnRu4S_DEwpCPNn-z1E8n6EZu6TI0iP38hM0zoWSRf8tgHj5BHoBQpaajGIoSDZmrwZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استقلالِ سهراب اگه بخواد انتقام کاملی بگیره؛ باید 8 تا به الوصل و 7 تا به العین بزنه:))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/138532" target="_blank">📅 22:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138531">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/138531" target="_blank">📅 22:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138530">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V57_VgBPVUgAB1AADm3ONYhErLxcvakp5z_GYF4TarAskaYAgUosY2cfjc21A-plKC1i8WJj0VkTdlmibYLvajmufhE3j1m8M0ScMCaJyZtCI16fuAfLlrzKpBWyDKwdc68FEyOCr_IgItxa2aZ9s-T-h5j-A4RWoQwfi9ayIWLoJvQiYYgizAFjSgsYD8h-sDCTZnZqZ5_g4MYZ50eVTpacTuq1ieLnwink1vicCXxWKEhb8coCg29y2lyFQjNHVoEIw5e6FCikRD7RXdrVmMXAlEKHFWIWlZQKkkBqACn84Ss5SS0-xUoIHcLnNbQ9Os0EL6PKblGY6TcN5FxxKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/138530" target="_blank">📅 22:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138529">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkAH3nqEMAYx6MkiUAv9oafrzTOITMh03wvHLWRXE2xNECgDdtlQFm3580rza8_5SnyakGJBLxShgeQReQ4PtMyfwLJTYRqaTL18yhjl7gkUsHPLHUH6e6BTIF_kLwP-AP-EDmvFtwueJ-7sQLviAzHOTxD2v12FvqdT7-pwkR6SHl7m4kXsNPquFlb2mQ7lVjyDPBHsl66ZryFiyaY_5Grn7gIiykTXt-JsR7jPEHjTvLrfLQykpaeHRApJ3YerTSji33aOqLiUB0D4ho-7qfAczdVXgefkwADO-O1rSQcz9qjkK_jBY_5HLNp_98OzfqTTg9Fori8o7773Pdjcbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
جدول لیگ برتر بعد از پایان روز اول از هفته دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/138529" target="_blank">📅 22:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138528">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/138528" target="_blank">📅 22:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138527">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
کیسه و ترتر شش امتیازی شدن و کلین شیت و حفظ کردن امیدوارم فردا بازی و ببریم و پیام هم کلین شیت شو حفظ کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/138527" target="_blank">📅 22:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138526">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
دومی هم زد ...و جواد چکش دومین بردشم آورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/138526" target="_blank">📅 22:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138525">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/138525" target="_blank">📅 22:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138524">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❤️
گل اول تراکتور به سپاهان توسط امیرحسین حسین زاده 83
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/138524" target="_blank">📅 21:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138523">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
برنامه هفته دوم لیگ برتر  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/138523" target="_blank">📅 21:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138522">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❤️
گل اول تراکتور به سپاهان توسط امیرحسین حسین زاده 83
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/138522" target="_blank">📅 21:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138519">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/138519" target="_blank">📅 21:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138517">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
✔️
✔️
شهاب زندی مدیرعامل نساجی: به مدیران ارشد استقلال هم تاکید‌ کردم مستنداتی دارم که آسانی‌ بازیکن غیرمجاز است و اگر مقابل ما امروز حتی یک دقیقه هم به میدان برود از آنها شکایت خواهیم کرد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/138517" target="_blank">📅 21:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138515">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✔️
#ارسالی | #تکمیلی
🆕
⚽
هوادار مقیم امارات به نقل از محمد قربانی: میگه به باشگاه گفتم اگه قراره رضایتنامم رو صادر کنین برای باشگاه پرسپولیس صادر کنین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/138515" target="_blank">📅 21:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138514">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/138514" target="_blank">📅 21:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138513">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
گل شانسی کیسه
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/138513" target="_blank">📅 21:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138512">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔄
🔄
فووووووووووووری
🚨
امیر جعفری مدافع چپ گل گهر سیرجان از لیست این تیم برای بازی امشب این تیم خط خورد تا شایعات جدایی و پیوستنش به پرسپولیس قوت بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/138512" target="_blank">📅 21:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138511">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
فوری؛ مهدی تارتار : فردا چند تا از بازیکنان مون به علت خستگی نداریم و ترکیب شروع مون تغییر می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/138511" target="_blank">📅 21:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138510">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/138510" target="_blank">📅 21:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138508">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/138508" target="_blank">📅 21:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138506">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M7Ew48owWXOiYzRWhBXAiGWkTGW06RFrdC6Xxj7yre5yMBF3OO72Lt7vgL-sBRjfS62Nd_sxwsp2_uraZakAeOzfWaITCgm57xtClmv-XzCHGzdMAbOszhPESW4bC_wyjS2BO6_defr17FHhToLwCZ4doi4g3Axgu1BbGtFGOWR9ZO1DUSni6mAFQKUp0H71fQJIvdU6fpf320f2pX7oxIVAGrL5V_YmIjlr2tSvXAug7JAy_pLVsw-kj9XsRPKjLw14094nOijmCOx41bRfCpiaq1ZeQj81r_0cKqMsgsCu463pmzIBlTkwx-TyLkZoFnU5ZF476cyCo-TSopJeiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oSUPS2wSyWVYuW8khRNlrVpMaIgypUR8q1m8Bm7QIo-MYrQHix3NAEb9x6ZMCY7VkLr3WDyHPw0k5ksW615EOkjzWBxrY06qCpZNjjoLHC57Sh-kRZMBPmBApCTJKMYpV0gC2TT6xzBcA2TBYomvewVs_lvVg7fZM5ETIys9egxT6Mm6I_vKp4oMiYnWjrg0cKhNW4zwoOpXq2txguhjQwBT4iOlAx7VhTMW4xOY8dlk0YNeutEedNPrBYfV76SQsWru9KEJJl3DmPN4Rouzo6pP5qh0EuGQSzkhg_80P2MTJ0XtKeUzXOl42ANIEYVO5NLxSFgAX1hl9PwyRlULFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/138506" target="_blank">📅 20:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138505">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
تارتار: تمام بازی‌ها را باید به چشم فینال ببینیم استقلال خوزستان جوانان خوبی دارد اما محکوم به برد هستیم؛ بازیکنان فوق‌العاده خوب تمرین کرده‌اند و کار ما برای انتخاب ترکیب اصلی را سخت کرده‌اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/138505" target="_blank">📅 20:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138504">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
مهدی تارتار: عشق میکنم میبینم هوادارا تو نقل و انتقالات مطالبه گری میکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/138504" target="_blank">📅 20:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138503">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
فوری؛ مهدی تارتار : فردا چند تا از بازیکنان مون به علت خستگی نداریم و ترکیب شروع مون تغییر می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/138503" target="_blank">📅 20:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138502">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/138502" target="_blank">📅 20:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138501">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/138501" target="_blank">📅 20:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138500">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
تارتار: از هوادارا میخوام فردا ورزشگاه رو پر کنن ؛ من هنوز دو بازیکن دیگه میخوام.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/138500" target="_blank">📅 20:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138498">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/138498" target="_blank">📅 20:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138497">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/138497" target="_blank">📅 20:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138496">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/138496" target="_blank">📅 20:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138495">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqJ646YXcpTKSeopktVPI5kpjKs7vsac_ij64SpoCDdgVAgZ3bzq98yLm2FrtAToR2WcbeBzZRquoHmdIAUCXVcn1DoHaP_aCuPrwEupVXwUBfbedxl-YgM7lt-DFJiHY5hFgxVzAi5F0fHyMYg6FaFvBzOv7NlhuEIbT53Z69M42sCFUUnlUgxtFIGBPvJ4CqSfBhPXsFDfnv2NUN3Izvgo70W1XGfqwl1cv39p3tE3y7lcsBXY7cBMkU9P9dpgP4xRwNwrhgJcFIAaJyF9vg1u1NFQ5Bvcda-78F0HTBRz7kkO7A9LbMsmG8FMr2-4Df_uKUVMDwNUwjuFERT0HA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/138495" target="_blank">📅 20:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138494">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
آسانی بازم فیکسه!
❌
مدیران نساجی ام گفته بودن مستندات جدیدی دارن، چه شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/138494" target="_blank">📅 18:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138493">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
✔️
شهاب زندی مدیرعامل نساجی: به مدیران ارشد استقلال هم تاکید‌ کردم مستنداتی دارم که آسانی‌ بازیکن غیرمجاز است و اگر مقابل ما امروز حتی یک دقیقه هم به میدان برود از آنها شکایت خواهیم کرد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/138493" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138492">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎙
🎙
🎙
🎙
🎙</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/138492" target="_blank">📅 18:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138491">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎙
🎙
🎙
🎙
🎙</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/138491" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138490">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🗣
🗣
🗣
فوووووری؛ مبین دهقان درخواست خروج از الوحده‌ امارات را داده است/ مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/138490" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138489">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
❌
مهدی تارتار تصمیم داره دیگه حتی تو آخرین تمرین قبل از بازی هم ترکیب تیم رو اعلام نکنه تا ترکیب لو نره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/138489" target="_blank">📅 17:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138488">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✅
✅
در صورت خرید دهقان سهمیه لیگ برتری پرسپولیس نمیسوزه و ما همچنان یه خرید دیگه میتونیم بکنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/138488" target="_blank">📅 17:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138487">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/138487" target="_blank">📅 17:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138486">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/138486" target="_blank">📅 17:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138485">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
عشقم (دکتر جون )فقط یه قربانی
🥲
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/138485" target="_blank">📅 17:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138484">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
تارتار تمایلی به جذب مبین دهقان  نداره و گفته فقط قربانی/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/138484" target="_blank">📅 17:40 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
