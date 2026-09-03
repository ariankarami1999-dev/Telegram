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
<img src="https://cdn4.telesco.pe/file/HVHNnZVEfZwhBXFC_ykW-C95tQbmsa7EBoa4bG9tuNn_APwdDG2dmZLZ2wjt9la-4AKAUg_6jvi9VfyrNGLzb_4gja7JFUIo2sAdYQp5-_9o1jDq3Dp3lkgyRr_HMk8dAlzJFR2ee-ShVm1Y8eVY1oJXr94mJ457tMV_a4El1A8bbmXGGzjEYkmoihil4orZUjrYwifrMTUr49LpDK5ErMFzMdvrXRndeZqtEmzu1Rp3gKAY-KVZJ9o_GYwJqzaNbBdKaSZUwACAHgDCyUnc0OxM5fWW1zaLt_G2_q6cQvVIsyil0g92tCwra3bB2BOs6DrDUV7Hyl0O1_q6D9_fcw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 01:51:16</div>
<hr>

<div class="tg-post" id="msg-139520">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRBUg9tUdSyNa9aQUjYNaCWY8mGwnVw7x0c6Ool6LO-jVq40Hpfd6IeoZ3BdS3173hzo8A7DwDC929ARNiOsuRcwk-kumHAvSRjXAZnCBZilBW2ABX6_ZCiyEqAaSReFCBs3iB_393LFrw4RWL16OREDJ3rXzB-QoBZgBryk1MQOJGQYWk9GbSvPHh3QSlNn-CrqjDMMZ3xOkQJyBOicvY3Uhj1tFBZsnD89_Orl5HU4D7eO74Ym7y4y9DKydjTg2asqq56CEMEsJ4C_3_SIxfKrjHysYwteK7iFnU0Ob0FG4jUPC0qs64PJE6zX5hV7IC1AEBGuuQaSBFhI9Ya1VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🇮🇷
تصویری از ناخن‌ بلند کنعانی زادگان در صحنه درگیری با آقاسی که در برنامه فوتبال برتر نشان داده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/SorkhTimes/139520" target="_blank">📅 01:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139519">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
فوری ترامپ: آماده حمله دیگری به ایران هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/SorkhTimes/139519" target="_blank">📅 01:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139518">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7cfe803aa.mp4?token=s1iisiLwykARniPIxmovUhk0CF-VxL-p_7X-u6khI3EOczmMMxp9HJZijkukBX5u2NfBNhSJB5CyrpLUxe4Fwfvv7dw80hniQBFRx-81f2zPG4DfJGYje5_6O7OBhpF7NOpMrTQrzeMVds2bclDb0AFyjKrRKocRU_G-VmLSXmdGLF7Z3PNJmrjGvMO8p81gZx1ZDBXfoKmIbPAgvCjbYfI4D4r-qXQbYN52Q85qOFEbAr6xc-H-isTSeq8ZgaSccp3FtRaevpM93U8diGVnhFtuZmma3f6jGX_mfk5YML5VmDxUYCVYZOSU1h1G1awzwI6bu03aMvD-XUSDmbwLNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7cfe803aa.mp4?token=s1iisiLwykARniPIxmovUhk0CF-VxL-p_7X-u6khI3EOczmMMxp9HJZijkukBX5u2NfBNhSJB5CyrpLUxe4Fwfvv7dw80hniQBFRx-81f2zPG4DfJGYje5_6O7OBhpF7NOpMrTQrzeMVds2bclDb0AFyjKrRKocRU_G-VmLSXmdGLF7Z3PNJmrjGvMO8p81gZx1ZDBXfoKmIbPAgvCjbYfI4D4r-qXQbYN52Q85qOFEbAr6xc-H-isTSeq8ZgaSccp3FtRaevpM93U8diGVnhFtuZmma3f6jGX_mfk5YML5VmDxUYCVYZOSU1h1G1awzwI6bu03aMvD-XUSDmbwLNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇮🇷
تصویری از ناخن‌ بلند کنعانی زادگان در صحنه درگیری با آقاسی که در برنامه فوتبال برتر نشان داده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/SorkhTimes/139518" target="_blank">📅 01:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139517">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: شما تعویض های تارتار در دربی را ببنید که تماما هجومی و در خط حمله انجام شد
❤️
محسن خلیلی: اینجا پرسپولیس است شما نمی توانید ناگهانی 80 درصد تیم را جوان کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/SorkhTimes/139517" target="_blank">📅 00:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139516">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: شما تعویض های تارتار در دربی را ببنید که تماما هجومی و در خط حمله انجام شد
❤️
محسن خلیلی: اینجا پرسپولیس است شما نمی توانید ناگهانی 80 درصد تیم را جوان کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/SorkhTimes/139516" target="_blank">📅 00:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139515">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⚽
🎙
رضا جباری:پوریا شهرآبادی جزو 3 مهاجم برتر لیگ است؛بازی در پرسپولیس پرمهره از بازی در تیم ملی سخت‌تر است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/SorkhTimes/139515" target="_blank">📅 00:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139514">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
خلیلی: بهترین نقل و انتقالات چند سال اخیر را امسال داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SorkhTimes/139514" target="_blank">📅 00:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139513">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
✔️
دعوت بیفوما به تیم ملی کنگو بعد از درخشش در پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SorkhTimes/139513" target="_blank">📅 00:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139512">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
✔️
✔️
باشگاه استقلال:
✔️
سرعت بیفوما خیلی عجیب غریب بود و مشکوک به دوپینگه! ازش شکایت میکنیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SorkhTimes/139512" target="_blank">📅 00:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139511">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ks355RTOx4PFXYqOe_m6NT2Xb3tvUXg_MT6zXs5gIYCYfra3__lnb3o8Vv4PVfVAboX_1Pl_MORwIyoTmjv4C9q69l1EWYMx9gACd21vmx9BN1TbE8QZM_GL6pJbAVv_4m9pfh5KJrSf6KXQjFvfbVXaq0QdpqmtktA2y25a4X-ySziCRdrnp40SAv0ksxXpa2Rfxr6XFTyzDNw9txyKixm-4Fz6yWts0TxUEU3Mz74xt3vO6pXRop9lCer1iQuIsglUJCEOUhhaDCyhvuaOeT56C_E3lZssQCtK9FeKqwoSvU-cSmSCX0zwxQ0AhSXCyzdI1hoiWMSmH-nf_OmMJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🟠
جدول لیگ برتر در پایان هفته پنجم
👑
تراکتور با فاصله ۲ امتیازی همچنان صدرنشین است
👀
فاصله منطقه سقوط تا رده پنجم؛ تنها ۳ امتیاز!
❌
چادرملو و استقلال خوزستان؛ تنها تیم‌های بدون برد
🔼
تراکتور، استقلال، آلومینیوم و فجر؛ ۴ تیم بدون شکست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SorkhTimes/139511" target="_blank">📅 00:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139510">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: برای دربی 5 بازیکن جدید در پرسپولیس بازی کردند اما استقلال تیم پارسالش در دربی به میدان رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/SorkhTimes/139510" target="_blank">📅 00:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139509">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: من شاهد هستم که تارتار واقعا دارد در پرسپولیس زحمت می کشد اما یک سری هجمه ها روی این مربی وجود دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/SorkhTimes/139509" target="_blank">📅 00:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139508">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👤
محسن خلیلی:
✔️
با کفش‌های بیژن طاهری هتریک کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SorkhTimes/139508" target="_blank">📅 00:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139507">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
جباری: سبک بازی ارونوف و نوع بازی تیم با توجه به تغییرات در حال هماهنگی است و به مرور زمان بیشتری برای بازی پیدا می‌کند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/SorkhTimes/139507" target="_blank">📅 00:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139506">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00e2475d08.mp4?token=A-zpjpa8Uvkz5mfCdXH8j1xNxceNoRAXmUmV6kZRuk91SibSiD0Qji5-D5k5SKnPpfKjo_7xW28_i1mjg7HMpsC3Lt9k2-10k2r2ZjGNc-iWnS9CF0WSah1OyhTXyq9QRSireViIoHNzmcLaWhyxgUMXgi-TL13pAvwaSZn0qUUkXvezzVVqZIWd1aaHvt4ai20UsXfI2j8wAiXJTULcBrCxA14UPztoQjMYAiI5ivs7ZnK77fC-Ig_J0lUrRQLfNI_ur_A8ERblPB0_Q94xPyPQxpf8HHOjqLnX1ZylHBllPZuVxcYcdqBxKCpmbzqB4d6Ol-B8tRY-YEYn-R0ueA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00e2475d08.mp4?token=A-zpjpa8Uvkz5mfCdXH8j1xNxceNoRAXmUmV6kZRuk91SibSiD0Qji5-D5k5SKnPpfKjo_7xW28_i1mjg7HMpsC3Lt9k2-10k2r2ZjGNc-iWnS9CF0WSah1OyhTXyq9QRSireViIoHNzmcLaWhyxgUMXgi-TL13pAvwaSZn0qUUkXvezzVVqZIWd1aaHvt4ai20UsXfI2j8wAiXJTULcBrCxA14UPztoQjMYAiI5ivs7ZnK77fC-Ig_J0lUrRQLfNI_ur_A8ERblPB0_Q94xPyPQxpf8HHOjqLnX1ZylHBllPZuVxcYcdqBxKCpmbzqB4d6Ol-B8tRY-YEYn-R0ueA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
محسن خلیلی:
✔️
با کفش‌های بیژن طاهری هتریک کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SorkhTimes/139506" target="_blank">📅 00:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139505">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇷
🇮🇷
نظر محسن خلیلی و بیژن طاهری درباره برگزاری دربی در اصفهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/SorkhTimes/139505" target="_blank">📅 00:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139504">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a595378b0.mp4?token=Fintz02ddbLVGcMpkgUxS_EEwRKfR27dWG3-bpXmsA9u6xVHMv_Usyhj2d0fwEthhl7zRPDvnJ6SoPriy_S2DK1k1NzwlAPhn5NHNfaNfeciuvDwyZECcGsVq8ViWgVXyhTbdkZXvfzSJktY65Q5_V0zZOQEdPzI-lhtuwWwXT1evsWaZeQ9yMMkWpWLn2SbBWQ-LvIbx5xMoLQ3sL5sAGmZFcxJB0Dmb30pdJQHIUlxyfgN2FhNXuHXFmgcpLyspLfRN4YASG2tGqQF16-O9mud9v7sw1YpGdbYeYSPSHVT0Wd6MY67cUn8lml59ZdNjAAHWHBEVLzGihUspLhoAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a595378b0.mp4?token=Fintz02ddbLVGcMpkgUxS_EEwRKfR27dWG3-bpXmsA9u6xVHMv_Usyhj2d0fwEthhl7zRPDvnJ6SoPriy_S2DK1k1NzwlAPhn5NHNfaNfeciuvDwyZECcGsVq8ViWgVXyhTbdkZXvfzSJktY65Q5_V0zZOQEdPzI-lhtuwWwXT1evsWaZeQ9yMMkWpWLn2SbBWQ-LvIbx5xMoLQ3sL5sAGmZFcxJB0Dmb30pdJQHIUlxyfgN2FhNXuHXFmgcpLyspLfRN4YASG2tGqQF16-O9mud9v7sw1YpGdbYeYSPSHVT0Wd6MY67cUn8lml59ZdNjAAHWHBEVLzGihUspLhoAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
محسن خلیلی مدیر پرسپولیس: ۸۰۰ میلیارد بودجه لازم تا ورزشگاه آزادی تا چند ماه آینده آماه شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SorkhTimes/139504" target="_blank">📅 00:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139503">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⚽
🎙
رضا جباری:پوریا شهرآبادی جزو 3 مهاجم برتر لیگ است؛بازی در پرسپولیس پرمهره از بازی در تیم ملی سخت‌تر است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SorkhTimes/139503" target="_blank">📅 00:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139502">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⚽
🎙
رضا جباری: کنعانی و علیپور با رهبری‌ خود نقش کلیدی در ایجاد همدلی و ساختار کلیدی تیم دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SorkhTimes/139502" target="_blank">📅 23:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139501">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
جباری، مربی پرسپولیس:  یکی از جذاب‌ترین داربی‌هایی بود که در این سال‌ها دیدیم. تیم پرسپولیس همیشه بالاتر از همه‌ی نام‌ها است. دنبال ۳ امتیاز بازی بودیم که به آن نرسیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/139501" target="_blank">📅 22:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139500">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/di3M-rkwcCymljxKqDJ8_VEo49hhFcvMZT5MaHm8kWzwjxbsFSg5FQpCKMKeGDHqAqiihpu9wZ105O7vHa8rnkQdoFCAwxC1ATNgoPkVuk0Jwwi1RckI0LXnOrpP7F-yorl4W0n5YDU73nv91BLGx-cp8bor2FMmiBgW-UD83XvNcim0UvyfYec5zNqYv3Vwbu43SP3iJ9slrNxH7ioEdBywpwiFN0rVY8SJLSF57PRECLBJTLIWZTfSfbc0SiIz_P5ibSWTJyaUpc_EK9LfoXvxrOaibnlGB0Mnlza0ZJTblN-mfz-Gq2lugxjZ5UkbwUIlB4qBzDgTjU0naCPyHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
تست های پزشکی تیم بانوان
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/139500" target="_blank">📅 22:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139499">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arOS11sMzI5UXZDF4HFeeQTNipeCCqgL-v6kY_2pXC3agiYPkRrIRD5Dft1hTfUUBwrQnpU3Mn5ZM2s3iIp6IAZMcVNdlQX4BSFXaRBgpxM-qI-HVJktz9L9Ovn-cy6QyFdwpJMvI1tmpaZ3S2Tu_404SaTtP87VFsGRxk0CgSuY9vBFzlKOrBtj1RRAiUWpqF1nj2ecVZnJw7uNqYlbqJYAK6z2ki9xDKLfSSCqHe_tnIIufUvGoBcq9LnnfjvWBms20r7C4lSwX05mSUwQmfaBM05U0RFkQgY7KNSXTtzO8zSumukNzcW98c4o0N2oS8d4Oc68T3oQ-xlQDnXs_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کمپانی دیشب یازدهمین بازی بدون شکستش مقابل استقلال رو انجام داد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/139499" target="_blank">📅 22:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139498">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSMWlKrPiKfByCwRepfACy2GcaqJXx52KeVNHaRYWZzhWQR7lcU5WodPW_nSV6SL02eLYOEpKjZw6oTYk7caKhlRsgSqsLFgG3CP2YZirep5NAeZCrQ1LAKE5savFp6NbjWjVefqJSa_NCBeUBjZyvnfyDEDbsXQ9-o6c1yEG_wDRSxeeei3PtOLnI5K4U3cBjZsYLPTRnwv7cCj24QRD7qUXi1nQ-7bGrXW0oRkqilfKQ9sm0uyI0lm_WeFoj7m5SBWizIjG4RzMkYqkF2FmzTcqH29I-P3hjjUyab6P8Q6RjEZDHZg443cwVb5PmroRgioppFGtx11jEDAli5aAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دیدار برگشت شهرآورد لیگ برتر بین دو تیم پرسپولیس
🆚
استقلال به‌احتمال‌زیاد 20 اسفند ماه در ورزشگاه صدهزار نفری آزادی برگزار خواهد شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/139498" target="_blank">📅 22:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139497">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
تارتار ضعف پرسپولیس را پیدا کرد!
✔️
تارتار به این نتیجه رسیده که پرسپولیس نیاز به یک رهبر در خط هافبک داره و نیم فصل قطعا در این پست تقویت خواهیم شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/139497" target="_blank">📅 20:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139496">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hm3AvlVjZ9AOiGEaLk1sUeJZ7AEG9oUmbTMcSA6YC04RWmTDm9MtlfJ6MkkEg1HUNebLcjPcCBaZYcIvhwC7QjmdWf1kQ91A670pZOYb6oxk1hSyWmJfEn3_QwPj2j5R5DDlPVSJFOh2--jLsMy92Yxvy_VXNihXeS_I1S4-_ITZWrnnIpuH0ATpnSln2SauhWbnSk7utUWWlB4-6jvcUMM7-QzeM-TNpIZt9gkoLWGJ0t6A4FK1ijXoIqFh6jz_3WfV6OlFsTNlf7UlNkA6ndCLHbnwzLSNbR1KVNHWWXsGAxjQZpeWDtDtYPdVtb13S0c9itXzc9bhbWAMPSoN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🎙
خلیلی سرپرست پرسپولیس:
❌
مصدومیت گرا از ناحیه آشیل است. تارتار گفت اول باید او را ببینم و در مورد ماندن و رفتن وی نظر بدهم. هیچ اختلافی بین اورونوف و کادر فنی نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/139496" target="_blank">📅 20:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139494">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrEOnHtRVYiw52GrJ2EA4_3OfmoYSH6Kw0Oj8O2HBWWTgrEHE2tBaWblBpGEJVdbzJ8m41emcFz04IfsprMbtUs1j-Nk-fcxyCBxRncCiIXbqbwmi6WCBTZ3dz-97QgFNvroUs1NcEPMHpwMbGD8d6cmIu7ab-6ls7YqCLDRUj8W__O-SYtPiiXBIXHnoMNi9Zwz0mevKefD_ZKV0H_usluGr_ksOkQCmv3E6uCAag8uE1CINqMVbIYIDe31XCARaH5VnYLzSAwxcDWXkqYjIOCt9RN9iUMe8Ig7zqHCb121l58U7ksg-Y_tGwp0BMSQmm-keNlyFQ44aXZ7tEI1sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
نبرد سرویس و قدرت در نیویورک
فریتز به‌دنبال عبور از سد بلوچی
شانس بیشتر با ستاره آمریکایی!
[
تیلور فریتز
🎾
🆚
🇮🇹
متئو بلوچی
]
🟡
تنیس یواس اوپن
⏰
امشب ساعت ۲۰:۳۰
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/139494" target="_blank">📅 20:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139493">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0ItbsYza2L6JHmpWO64WuiMc-XAzRzGaQmTLjC3ZWgv026WYvOGIshAwUwaD6yvOMHJeOzWfl0dXifFF7MwQvNGY9jUY6Mfca8jLeYCUiqQYISzgQ9YkvdvocQWTU3QSi_ZPoY7DRIh8_bgTZ_V7DYHp5wRl3hMpnT8YAKVOpCsWKCl9qx2YM2di2_8ldPrnQn8WMsaX-velFgyXSUyQ9EpikOTXhtV9mnRaW6sqRlY8TRBGlCHjhCHMMPEBT5mdM2sH9hONY0tnzCU38y5s0Tgn7WarsMxCj5YgTJueGhdSebQSsTsS8TlZrFADFQ1TckmEF-LbZgjfmZEeGwVOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
حضور ابوالفضل جلالی در بازی امروز
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/139493" target="_blank">📅 19:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139492">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlELnFD67FxjnEdC2UrZ1oxipA6vT7WVKW0rvhtP-mgPDCDqdocT6VOSMSTb3dH8RtUmzbYGgfp50-4tAKzK-C1vY5E6ULmmln3RCbeYXHr6VH7WSRLbIbJ4tYj772d7avznRGp81jLUZfrVDEFPxHq2Dg_PgW2tgY3fjREt5LvhQXOHR0kpP1pOi5StMCqIiZK30PQHMnlaPiHa6OY5G8cbUUtvWHTZqHQkWoEeVKkcsLvMgLTGW7Gu53gaq6XgjLltZUJz-Le_HBvlojpKFUFW5I0b2kffklO7s-S3UVeMn9hMgrBA165nFhtLpDbm_h7ErMAA1zH7raUVdA7nmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
محمدمهدی محبی زننده ۲۰۰ مین گل تاریخ دربی بود
👌
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/139492" target="_blank">📅 19:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139491">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">#بماند_به_یادگار
🔗
💯
تا روزی که اردوبادی و اینانلو داخل هئیت مدیره هستن این تیم رنگ آرامش نخواهد دید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/139491" target="_blank">📅 19:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139490">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC2g893onQ39syxOhE7-t9b04_q-PLtccbZdMZeva0s_9QGhpcijNYRNPNXulZAfzWXcT3a5S4ipBHew0Y-vMKi0K4m01nHyMizPs6WtbLvQodUQI7FSO9-DmLiuGJx3bfViXFM7ioWiMH3HE7M526H2TFF9vQ2yOA4NGAqnlLXRRurzWjNiqlqLe213A_NYVT5SG1B8XF9xwTrDuQR-5g24UJ8wC8JvOc-UH81ZNrzX46Eq2uHWfZXAqQUCgu5ZS0-3Yv4XEAoHEnayO5v5ZnXbbAbCPQizkp-zTMM0nNZeeLAURdDbYia8E9sOZijEouK-PvhKf1fohCUr7ivz6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
پرسپولیس امروز در دیداری تدارکاتی به مصاف مس رفسنجان رفت و با تک گل پوریا لطیفی‌فر به پیروزی رسید.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/139490" target="_blank">📅 19:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139489">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLInYUXqLIDcMmVy5XHbfWXx0anAk54nQlck6dqxZ8hWb5YIXH-jl45fVK75a-PABnLjSQ7tY-biUn-jcq7suSMUpjRXWbQpvAlJS35iSE51cy1tRFdfmE7nnww7dHaSxzjZJSxB6BJRzC2CtxDrv8PJmlzbHzarsI3c0ZLflmEH-zV6gC8Y_oNgY8Ky9xzKQrnD68Hs8Hg2fa_9TMD87I-vdoAK9wwBSi2HdcO0OBgC_oWhZH1ZrylUNUBAVlO5AIuR1v0LlyWBePbreBL8jrmHJr93jNZ1WG77Ul-wEWJM8pMg_KUp_QWFhvY7DNq88b8gbiiqH1cpWJfHJjp0rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🗣
محمد عمری از فصل قبل تا الان توی ۱۷ تا بازی برای پرسپولیس فقط ۲ تا گل زده!
⬅
⬅
با اینکه آمار همه‌چیز نیست و کارایی بازیکن روی بازیِ تیم هم مهمه، اما هوادارها اصلاً ازش راضی نیستن و انتظارات رو برآورده نکرده. امیدوارم بازی دیشب براش درس عبرت شده باشه، تصمیم‌های درست‌تری بگیره و بیشتر به درد تیم بخوره
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139489" target="_blank">📅 18:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139488">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏅
باشگاه استقلال قصد دارد به دلیل حرکت حسین کنعانی‌زادگان در دربی ۱۰۷ مقابل عارف آقاسی علیه این بازیکن شکایتی را به کمیته انضباطی فدراسیون فوتبال ببرد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/139488" target="_blank">📅 18:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139487">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9PwJ3ZqR41PFX4kWw0upOFNM8LjgYOFSoFoBahCsbSvWicm0esHd3Go7M6OpKHYdBUAmMj-wch5Bk6DSWkG2Y92-uUl4ZGPkwF_TV3aiDhfXyZohhmrG8NtRcJBYW8SJQ08snd7apYXUkNd4E0USt4jz4z1m8uzAKJ8MZnQTopdbAroTSjsKmgIMCQZRMuDxpniKdkHDJQlTweKGRIFP0u1VcKcRHQijA4XGMiIPyTIvhSuHciMgDGRUCV3dY5TAwvt9m28aj_tunqdzdASnf7ILmlnzN1df9ogy-OaUJi2RoIW_yR_Q69uIwq0SaR_DwwFWPRWgpGCXzPAbEtlMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
باشگاه استقلال قصد دارد به دلیل حرکت حسین کنعانی‌زادگان در دربی ۱۰۷ مقابل عارف آقاسی علیه این بازیکن شکایتی را به کمیته انضباطی فدراسیون فوتبال ببرد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/139487" target="_blank">📅 17:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139486">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✔️
✔️
دانیال گرا مدافع مجارستانی تیم پرسپولیس برای هفته پنجم از لیست بازی خط خورد تا یک سهمیه خارجی سرخپوشان برای فصل آینده به خطر بیوفته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/139486" target="_blank">📅 16:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139485">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
✔️
خبرگزاری مهر:
🔴
پرسپولیس پیشاپیش شکایت خودشو برای حضور یاسر آسانی تو دربی آماده کرده. پرسپولیس اعتقاد داره کمیته انضباطی و سازمان لیگ صلاحیت لازم رو برای پرونده درباره یاسر آسانی رو ندارن و استعلام فیفا باید منتشر بشه
🔴
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139485" target="_blank">📅 16:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139484">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
❌
❌
طولانی‌ترین روند شکست‌ناپذیری در تاریخ دربی؛ پرسپولیس با 20 دربی بدون باخت
✔️
✔️
کیسه کش حسرت برد دربی رو به گور می‌بری
😂
🫵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139484" target="_blank">📅 15:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139483">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=HrdRYNy9p0jp8nHNEeZsd0AzntHmzw4RXvOj4MarbdShq5CIB-26Nn-8xN_7lOHYb9hHtTqCRnHug96-j8zYUo6XJwJQ7NSn7PVVz3pV4jSPoXGucjT97dVy1IPjyV2FHn0RxcG2QDAiht0YlJirRDi3TDgf8khdQLd-rAkaLC4bJwdFIh-jiDof6GmLWsB_-rnGq7lxqgrKQpfat4EwbC9kYSJX7Ev8F96IF_gavpRv4Jj6T9WuRJ4GTYvsoiAO_5b7DlhRiOCmxUwAEWKYhcHpJap1KlzAEoylBDvyjA8rkgQJdRyUUZo2yh_wIipqkhb9Fcsmj4L3ft3K_m9ZQhRgAqpvre9lRExkDg_JrK80XbrtoHruHFR6YhPx2L__7MLHXd27un5_W0USAp6XIilSuf5-41SDYnxmkXoyeV9x6PAw0m5S21Q1Q86NwYGvbxWOipIVVoBJi03wAKxbnziOY8s9SlwYVuHfw0vfyLPqsbCPniTF7HRmxiXXWQZZnh6m68YBPPHVqsEZNSijjBHLle-eJt_ZHYALPtaNAWh8b9FtA3mBntgh0Pneqbd6Nf5kINIHmuG1a-fkaw12P9DbsuMhWWYIuYTnwMi3UpurIu0dYg83SSNDONjFuYs97Z5gBHqQ7hn2mvvhQle8PJ9Zq93ppaIIf6KS3Yzq42k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=HrdRYNy9p0jp8nHNEeZsd0AzntHmzw4RXvOj4MarbdShq5CIB-26Nn-8xN_7lOHYb9hHtTqCRnHug96-j8zYUo6XJwJQ7NSn7PVVz3pV4jSPoXGucjT97dVy1IPjyV2FHn0RxcG2QDAiht0YlJirRDi3TDgf8khdQLd-rAkaLC4bJwdFIh-jiDof6GmLWsB_-rnGq7lxqgrKQpfat4EwbC9kYSJX7Ev8F96IF_gavpRv4Jj6T9WuRJ4GTYvsoiAO_5b7DlhRiOCmxUwAEWKYhcHpJap1KlzAEoylBDvyjA8rkgQJdRyUUZo2yh_wIipqkhb9Fcsmj4L3ft3K_m9ZQhRgAqpvre9lRExkDg_JrK80XbrtoHruHFR6YhPx2L__7MLHXd27un5_W0USAp6XIilSuf5-41SDYnxmkXoyeV9x6PAw0m5S21Q1Q86NwYGvbxWOipIVVoBJi03wAKxbnziOY8s9SlwYVuHfw0vfyLPqsbCPniTF7HRmxiXXWQZZnh6m68YBPPHVqsEZNSijjBHLle-eJt_ZHYALPtaNAWh8b9FtA3mBntgh0Pneqbd6Nf5kINIHmuG1a-fkaw12P9DbsuMhWWYIuYTnwMi3UpurIu0dYg83SSNDONjFuYs97Z5gBHqQ7hn2mvvhQle8PJ9Zq93ppaIIf6KS3Yzq42k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
❤️
👀
✔️
تو این صحنه کسی متوجه نشد ولی وقتی از دوربین نزدیک تر صحنه پخش شد مشخص شد نوک انگشتای نیازمند بود که باعث شده توپ به تیرک بخوره وگرنه گلو خورده بودیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139483" target="_blank">📅 15:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139482">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
20 بازی بدون شکست
🔥
✔️
حسرت کیسه در آستانه ده سالگی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139482" target="_blank">📅 15:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139481">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❤️
خدا بنده لو، بازیکن پرسپولیس:
⚪️
بیش از اندازه در مورد ارونوف حرف زده می شود. چیز خاصی اصلا وجود ندارد و هنوز خیلی از بازی ها باقی مانده است. او اصلا افت نکرده است و اصلا زیاد بازی نکرده که بخواهد افت کند. همه از کیفیت اورنوف خبر دارند و هر تصمیمی سرمربی…</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139481" target="_blank">📅 13:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139480">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⭕️
⭕️
⭕️
با اعلام یاسر همرنگ
🚨
کوپال ناظمی داور دربی شد
📺
موعود بنيادی فر داور var شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139480" target="_blank">📅 13:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139479">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
✔️
باشگاه استقلال نسبت به عملکرد و سرعت بالای تیوی بیفوما مشکوک شده و احتمال می‌رود درخواست تست دوپینگ از این بازیکن پرسپولیس را مطرح کند.//هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139479" target="_blank">📅 13:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139478">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjFUKg7BTWkSEswd3Ytx_Q1UhUcPfJJMRXUr3XVDk0-SOOZUPFLn6CBvQRQ9vh_-6q4Yoy_pvOS9VV1CVxam2dD8edMAgGqgEZOQ59QgJepinJHubNvkTqLoyGjsr6gyQswXy_NaVUf11pk6LwdcKAHUA5rvdjUWavXwZxIqLPWpraMQk0TRI6nNPjMzD4EdoH3M1Q4S7UR2zZOJZepWYnkoYPCbkR7Zunr0vZDCO-cweUVXaED-f-WnGHjj-L04Cc0T8hlnTv2dqoyhkpAeX2IyVGARIEDU1QyMDE1fqrXWOadx739oYVbf745LFLVL6F9sm3iwXtdPJRM64bU03Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سوسیداد و سلتا؛ جدالی برای سه امتیاز
دو تیم آماده برای یک نبرد نزدیک و تماشایی
کدام‌یک دست بالاتر را خواهد داشت؟
[
رئال‌سوسیداد
🔵
🆚
🔴
سلتاویگو
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139478" target="_blank">📅 13:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139477">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔄
🔄
🔄
با حضور یاسین سلمانی در بازی دیشب حالا مهدی تارتار به تمام بازیکنان پرسپولیس بجز محمدحسین صادقی که تا حالا در لیست قرار نگرفته بازی داده و تمامی بازیکنان با ذهنیت آماده به سراغ ادامه‌ی لیگ میرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139477" target="_blank">📅 13:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139476">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🤩
| فارس:
🔴
❤️
🔄
تارتار امید چندانی به دنیل گرا ندارد و حتی درصورت بهبود مصدومیت هم نیمکت نشین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139476" target="_blank">📅 10:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139475">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✔️
✔️
باشگاه استقلال نسبت به عملکرد و سرعت بالای تیوی بیفوما مشکوک شده و احتمال می‌رود درخواست تست دوپینگ از این بازیکن پرسپولیس را مطرح کند.//هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139475" target="_blank">📅 09:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139474">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
♨️
🗞
| #فوووری از تسنیم:
🔴
🔵
👤
پرسپولیس بخاطر استفاده از آسانی مستقیم به فیفا شکایت می‌خواد بکنه نه کمیته انضباطی
⚠️
❌
کمیته انضباطی فدراسیون شکایت های گذشته در مورد آسانی رو رد کرده بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139474" target="_blank">📅 09:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139473">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✔️
✔️
عادل فردوسی‌پور: ترابی قطعاً ادامه فصل رو از دست میده، با خودش صحبت کردم و گفت دو پزشک بهش گفتن رباطش پاره شده و باید عمل کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/139473" target="_blank">📅 09:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139472">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✖️
✖️
هافبک و کلا استقلال برداشته و خیلی خالی هست هافبک ما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139472" target="_blank">📅 09:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139471">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❤️
❤️
❤️
❤️
🔴
صبحی که دربی و مساوی کردیم و هنوز داریم حسرت تک به تک نزدن علیپور میکشیم بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139471" target="_blank">📅 08:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139470">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHG6JTnyoN8lOc10Ece_nm9yZdWd0IE4ObNb8w6V1UonQ6Zb7XiLliPriXN_oG3jDPcNXg6cgMM4UwxCmd1OldKQOrC7mCD6kpRoF_8i5f-4P2xwmaeOBYrk89v5Pfd63DtjOKlYraKwM6WPdn_szY7PgAb6bAhV2gO_XTDl_RbQMgmyfz-X9q1YhJVEuA53adL6LtzfDHujhbJm7AcIFK-REWCvc79NYzOGVxATGQwWc2HjlON8S7dtVCamCbFbhKdSFoCcvuDBanl147xuTvVMNeQy2vKNm4afYbFAZCm0DiniRUpIDRenb4CLy3ED_SG12j1MokE6Yf-WdMhwYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
دوئل‌های جذاب در یو‌اس اوپن!
🎾
جیمی فاریا
🆚
کارلوس آلکاراز
🎾
رِی ساکاموتو
🆚
فرانسیس تیافو
🟡
کدوم ستاره‌ها از این نبردهای حساس سربلند بیرون میان؟
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی دیدارهای یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/139470" target="_blank">📅 01:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139469">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
✅
سه بازی مهم هفته بعدی
✔️
شنبه :گل گهر و تراکتور
✔️
یکشنبه : آلمینیوم اراک و کیسه در اراک
✔️
دوشنبه : پرسپولیس و ذوب آهن شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139469" target="_blank">📅 01:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139468">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⚽️
⚽️
استقلال و پرسپولیس امشب در مجموع 33 شوت بهم زدن که 9 تاش در چارچوب بود، برای درک بزرگی این عدد باید بهتون بگم که در مجموع دو دربی قبلی 33 شوت زده بودن که 10 تاش تو چارچوب بوده که یعنی امشب به تنهایی اندازه دوتا دربی قبلی روهم موقعیت دیدیم
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/139468" target="_blank">📅 00:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139467">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZXB0tZG9VzT_rxuGqqXWP5-_ZKrob_3o8YfHFsw6_L12clVJ3e-0JvhwIuI1JskkPvcBLLBs1nm3zpzqafsyqvJ2rDF64xQjKAaIXIfeS73V8rec9Tb_ZifnY6Cjw7pZ41fAp2jil9uCwPK_jvf96ETd9qRidA2nvrtgHDKldx3wp3CKMne3BqKOU_Di932YqzJMOKOyM7jtXiqB2Pc7ET4Dt8aSLWPHj4sYItpjeyfTnQnTD96aNeTJE1sQmRAZXd4vmgLb3vhBL9H4oTfE3HrsF2aCPBFpd9E96mMptONCwVZpVmRux1-kU-WJsEaaSLm3VJlPci2JuiyOBAiMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽️
استقلال و پرسپولیس امشب در مجموع 33 شوت بهم زدن که 9 تاش در چارچوب بود، برای درک بزرگی این عدد باید بهتون بگم که در مجموع دو دربی قبلی 33 شوت زده بودن که 10 تاش تو چارچوب بوده که یعنی امشب به تنهایی اندازه دوتا دربی قبلی روهم موقعیت دیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/139467" target="_blank">📅 00:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139466">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
20 بازی بدون شکست
🔥
✔️
حسرت کیسه در آستانه ده سالگی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139466" target="_blank">📅 00:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139464">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
فارس : نظر می‌رسد نظر کادرفنی پرسپولیس نسبت به ۲  بازیکن دانیل گرا و تیوی بیفوما  تغییر کرده و احتمال ماندن آنها در جمع سرخپوشان بسیار زیاد است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/139464" target="_blank">📅 23:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139463">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-rV3k78TGBg5zs81fBAllAzdzU_F1Gy7ORhl-9HwFZ_BL7iP7pquzrIWusLz8EfLsT1NQ_T2DA8gTN7locIeH0Nzp6EIey-tZc9Hc8H_0UUsOEIRbuNzVakh-Amc5LjSdEIlrSJ5ZjjKOd5TqWYg0ovfaCYNctBVfpe15CGrt_S9InDz3lqGonRvUtn7OHt4zBcUcDU6AImeMQiXw0xPLpr6v1cH2E7GL6QLP_ujtdTC3snUQVRCgSauMDyHqwcZkcckiqpVRrSixjGOSyELV8tu9Rz4Nz-WSFQQK2WRx_i9XDuu64ZBhVe7R67x_bEuUxv_YwXEJ22jE7W8YCDtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
پایان بازی | شکست ناپذیری پرسپولیس به ۹ سال رسید/دربی جذاب برنده‌نداشت  استقلال
1️⃣
-
1️⃣
پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/139463" target="_blank">📅 23:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139462">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fc62967a0.mp4?token=X_SzSgDg4j-NSlQPg4IO-nW9QxfED9PACTIybn14vyQJh4IvrG9R9bcWLokHx5wzIfOSHyB8Irqyt5wO-ovw37y5JrsOZeICftVwApAAAc0A7jzhVeHDCRBmz5kfzNBCX9KFTV2MtrkLUgj1v5buxVLBtfh4OhgtKzQPW6qk3R31xEdE5-sXnKNUq3DLbaLxr-liJvcXHkN3T0LifN4zhtF4W6jcFK_b_5uyLaM-G9k6XLkYF6ySKLNqT_YDN75OE8GbZuXL_mqVSMTaqJ8z3ZJ_SHT-MC6t48mOCsycHeSZt_AxjAA4B3jGcL4MxkfWoCG3FVQDsY2Ltn6f8bRV8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fc62967a0.mp4?token=X_SzSgDg4j-NSlQPg4IO-nW9QxfED9PACTIybn14vyQJh4IvrG9R9bcWLokHx5wzIfOSHyB8Irqyt5wO-ovw37y5JrsOZeICftVwApAAAc0A7jzhVeHDCRBmz5kfzNBCX9KFTV2MtrkLUgj1v5buxVLBtfh4OhgtKzQPW6qk3R31xEdE5-sXnKNUq3DLbaLxr-liJvcXHkN3T0LifN4zhtF4W6jcFK_b_5uyLaM-G9k6XLkYF6ySKLNqT_YDN75OE8GbZuXL_mqVSMTaqJ8z3ZJ_SHT-MC6t48mOCsycHeSZt_AxjAA4B3jGcL4MxkfWoCG3FVQDsY2Ltn6f8bRV8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
بیفوما امشب دوباره یه استارت ۴٠ متری زد فرعباسی وحشت کرد دستپاچه توپو زد بیرون‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/139462" target="_blank">📅 23:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139461">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✔️
جدول لیگ بعد از هفته پنجم .اختلاف با صدر سه امتیاز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/139461" target="_blank">📅 23:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139460">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❤️
خدا بنده لو، بازیکن پرسپولیس:
⚪️
بیش از اندازه در مورد ارونوف حرف زده می شود. چیز خاصی اصلا وجود ندارد و هنوز خیلی از بازی ها باقی مانده است. او اصلا افت نکرده است و اصلا زیاد بازی نکرده که بخواهد افت کند. همه از کیفیت اورنوف خبر دارند و هر تصمیمی سرمربی…</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/139460" target="_blank">📅 23:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139459">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
کنعانی زادگان: تارتار تیم خیلی خوبی بسته است و امیدوارم آخر فصل قهرمان شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/139459" target="_blank">📅 23:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139458">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
کنعانی زادگان: تارتار تیم خیلی خوبی بسته است و امیدوارم آخر فصل قهرمان شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139458" target="_blank">📅 23:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139457">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❤️
❤️
❤️
ترکیب پرسپولیس برابر استقلال
🇮🇷
پیام نیازمند، مهدی زارع، حسین کنعانی، مهدی تیکدری، مجید عیدی، پویا پورعلی، محمد خدابنده‌لو، محمدمهدی محبی، تیوی بیفوما، ایگور سرگیف و علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139457" target="_blank">📅 22:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139456">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✔️
✔️
✔️
هر دو گلر بد خوردن گلارو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/139456" target="_blank">📅 22:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139455">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
✔️
مهدی تارتار: ما و استقلال خانه نداریم!
✔️
پرسپولیس و استقلال متضرر می‌شوند و ما خانه نداریم در شهرقدس از پتانسیل هواداری نمی‌توانیم استفاده کنیم.امیدوارم هر چه سریع‌تر استادیوم آزادی آماده شود.
✔️
اورونوف هم یکی از آن‌هاست هر کسی از هم‌پستی‌اش جلو بزند،…</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139455" target="_blank">📅 22:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139454">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✔️
✔️
تارتار در نشست خبری: گروه داوری امروز خیلی خوب عمل کرد، خسته نباشید به آنها می گویم/ امروز هم پرسپولیس خوب بازی کرد و هم استقلال
✔️
✔️
به خاطر گل مساوی که خوردیم واقعا حسرت خوردیم
✔️
✔️
هم ما می توانستیم برنده بازی باشیم هم استقلال اما در مجموع ما یک مقدار…</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139454" target="_blank">📅 22:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139453">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👤
خدابنده لو، بازیکن پرسپولیس:
✔️
بازی بیرون خانه برای ما حساب شد‌. امیدوارم ورزشگاه آزادی زودتر درست شود. در مورد خودم نمی توانم اظهار نظر کنم. الان فضا بازتر است و امیدوارم ادامه دار باشد. دو تیم موقعیت های خوبی داشتند و آمده بودیم برای بردن اما حیف شد.‌شرایط…</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139453" target="_blank">📅 22:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139452">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bebc6bdd.mp4?token=cGWYjWrMA9AuOvY3ISfIBivf2p2Qyl4FijHTciFKJZ8-j7modkXPYSDdzF1xdB53tKvL1BSKl_3FCKnRvbRoD986W7b-vFWuBVprZ0UYie915cYPPW7DqEL0kt_CnD3hGOJOJV23my_SS1iOgNhoMrE9fKHJB18JvDtuqftSlNDcw71rI6-0P-A_0mK2m9z6AXZnKsJSjwx7PF2aLDUoQbgVKHv_dDDHC0FTyHg8213w287PMv77mpqOO8d6BK3gzPes5BjC1VLQKE2R9vZEgbJ9i9Orbxj6ihS3IvcrjGIhYPrYtirbWGpLqSOyLYMEtDR4uSq1rOOtViiG2ULTYDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bebc6bdd.mp4?token=cGWYjWrMA9AuOvY3ISfIBivf2p2Qyl4FijHTciFKJZ8-j7modkXPYSDdzF1xdB53tKvL1BSKl_3FCKnRvbRoD986W7b-vFWuBVprZ0UYie915cYPPW7DqEL0kt_CnD3hGOJOJV23my_SS1iOgNhoMrE9fKHJB18JvDtuqftSlNDcw71rI6-0P-A_0mK2m9z6AXZnKsJSjwx7PF2aLDUoQbgVKHv_dDDHC0FTyHg8213w287PMv77mpqOO8d6BK3gzPes5BjC1VLQKE2R9vZEgbJ9i9Orbxj6ihS3IvcrjGIhYPrYtirbWGpLqSOyLYMEtDR4uSq1rOOtViiG2ULTYDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
خدابنده لو، بازیکن پرسپولیس:
✔️
بازی بیرون خانه برای ما حساب شد‌. امیدوارم ورزشگاه آزادی زودتر درست شود. در مورد خودم نمی توانم اظهار نظر کنم. الان فضا بازتر است و امیدوارم ادامه دار باشد. دو تیم موقعیت های خوبی داشتند و آمده بودیم برای بردن اما حیف شد.‌شرایط تیم خوب است و همه متحد هستیم. هواداران صبورتر باشند ما تغییرات زیاد داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139452" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139451">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
✔️
مهدی تارتار : بازی زیبایی دیدیم/هم ما و هم استقلال میتونستیم برنده باشیم/از مسئولین اصفهانی و از داور تشکر میکنم/حسرت میخورم که نبردیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139451" target="_blank">📅 22:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139450">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDu9rCtFXgQx7tbjVrCbjHdBVa5_GD5V0NQFgags2UnUuS6eoBo0_m18-zUJ_IdlSEyiYDUH8EQn32Y_DJLFOuI9K1Wil_vnKuAvx8S78vua9W-3sjXwmSCbYo59EkVxG_lUz7SNpaxm0jTpJqB-81998uHLhYQxKjF5RqpdLUJIcHSR0x0tQTT3UMdjnzUvLYQdlNABnF0h6feQ5PvpAiLoKfOLfNdUUWslZyGMQ4G4jWB7_ilZr53fTpuNl7SIpE1opnYiNALFP2-_sm5Ed-Zbeb2jmt0pVztu617g4Nss-O2B0My7zvLVaTCwgD76hx-cbkZL-NFjpZ6UmyYHyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
جدول لیگ بعد از هفته پنجم .اختلاف با صدر سه امتیاز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139450" target="_blank">📅 22:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139449">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
✔️
ترامپ: من استفاده از سلاح هسته‌ای علیه ایران را رد کرده‌ام/ ما دوست داریم با همه کنار بیاییم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139449" target="_blank">📅 22:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139448">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❗️
🤩
🤩
خداییش یکی از بهترین داربی‌های چند وقت اخیر بود
✔️
داربی چهارشنبه‌شب نقش جهان، برخلاف پیش‌بینی‌های اولیه/ اطمینان وریا در مقایسه با سیدجلال، موقعیت‌های استقلال بیشتر بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139448" target="_blank">📅 22:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139447">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4d2d12ad.mp4?token=KQVdvXR9AHcxdmP1EtvwPWfMGKf_2X3FMK6d_pQv7wesAlRR6mC8mo94uVH3rFJhXatYoyrwslWvNYSAeiYghHIRJuXottpXkHAr6Z4XKZmfZX7nMqyYnwqpN09QWNUsFpIEJJfAiar8yLDKV_w9-JP59z02Li0qyswqkpkZ3ySTuWDBeoIymBFrkN-5Rz1USspEDU995y-cvR7M6sEm7gItAM-VZheXoafofBPHeB7U784u6ZzSSa2H1U4owPXZLjYHGkYxUPw-TJ1_Nwk4nGbe_R_6hc6jX_H3tSW9R3K-eyjqjNhBCn-VdhMxwKrPl0n6w9e3CE88yAhW5cG4uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4d2d12ad.mp4?token=KQVdvXR9AHcxdmP1EtvwPWfMGKf_2X3FMK6d_pQv7wesAlRR6mC8mo94uVH3rFJhXatYoyrwslWvNYSAeiYghHIRJuXottpXkHAr6Z4XKZmfZX7nMqyYnwqpN09QWNUsFpIEJJfAiar8yLDKV_w9-JP59z02Li0qyswqkpkZ3ySTuWDBeoIymBFrkN-5Rz1USspEDU995y-cvR7M6sEm7gItAM-VZheXoafofBPHeB7U784u6ZzSSa2H1U4owPXZLjYHGkYxUPw-TJ1_Nwk4nGbe_R_6hc6jX_H3tSW9R3K-eyjqjNhBCn-VdhMxwKrPl0n6w9e3CE88yAhW5cG4uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🤩
🤩
خداییش یکی از بهترین داربی‌های چند وقت اخیر بود
✔️
داربی چهارشنبه‌شب نقش جهان، برخلاف پیش‌بینی‌های اولیه/ اطمینان وریا در مقایسه با سیدجلال، موقعیت‌های استقلال بیشتر بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139447" target="_blank">📅 21:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139446">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6faf16beef.mp4?token=FY6PuOsECRwQLgEYUJDIsQyKU3iGgzXQIDiXg5i-LV5YFzXLKukIdDPWjWHN0uQnQiUq78B5Q8kWB9uvvNv2Y22CBKawafsM9g6W0-Nt2t5ZeVyIm9ziMjMR2_mYwbIu7K6IlGdsrEBxKXHnqovPFYV30b2bSuagh8rNqloOtpvAONPRU8he2n2DD5LKP5rIN51Cse_1M2JlwUWCytRrtQHylTe9rR_nWxvP27bbpTGp7_AOHrqWMDhxro_xt9C7YiY5B0EoWHusfkWon_K4mNg7_gc66R2IL86m3r5GKCDX1E1HKo-oDIe-0bOjumrIFapFEc-vjGzLnffHt6EA7zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6faf16beef.mp4?token=FY6PuOsECRwQLgEYUJDIsQyKU3iGgzXQIDiXg5i-LV5YFzXLKukIdDPWjWHN0uQnQiUq78B5Q8kWB9uvvNv2Y22CBKawafsM9g6W0-Nt2t5ZeVyIm9ziMjMR2_mYwbIu7K6IlGdsrEBxKXHnqovPFYV30b2bSuagh8rNqloOtpvAONPRU8he2n2DD5LKP5rIN51Cse_1M2JlwUWCytRrtQHylTe9rR_nWxvP27bbpTGp7_AOHrqWMDhxro_xt9C7YiY5B0EoWHusfkWon_K4mNg7_gc66R2IL86m3r5GKCDX1E1HKo-oDIe-0bOjumrIFapFEc-vjGzLnffHt6EA7zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
تشکر بازیکنان پرسپولیس و استقلال از هواداران‌شان پس‌از پایان داربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139446" target="_blank">📅 21:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139445">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🔱 Hero 🔱</strong></div>
<div class="tg-text">سر لجبازی ایشون سهمیه های فصل بعد ما هم به باد میره،نه با گرا فسخ کردن ،نه به ارونوف بازی میده نه باکیچ،هر کارشناسی هم حرف میزنه میگه ارونوف فاصله داره با ورژن خوب خودش،سوال من اینجاس ارونوف دقیقه ی ۸۰ به بعد اومده تو بازی چیکار بکنه تو کمتر از ده دقیقه؟؟؟ اونم دربی</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139445" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139444">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⬇
👤
آقای تارتار بازنگری بکن وسط زمین وله، چرا از باکیچ و لطیفی فر استفاده نمیکنی ؟! لطیفی فر هم بازیکن مستعدی هست هم قامت بلندی داره،مسئلت با خارجی هارو کی میخای تموم بکنی ؟ به چه قیمتی میخای اورنوف و باکیچ بازی ندی؟دقیقه ۷۵-۸۰ برای بازی دادن بازیکن جوان و تلنته…</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139444" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139443">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsTfPXgVOk_yn3ihCM5lbdOnYuzWZVN-eXbzI1e_CNaB1yBb4tctSMgBYASiOOCGXXJlYiq7JuFOPY1rlwF3EJY8OmJ8Z0zwkQz61JaZyAKy2Y8gcQkjvnSHZABs6IrwTX_PLDlP03AWlFz0_XwgqjSdpUVyre6zUEH-sVmfVCuSy7-D2-ITXvIpTuU9P4AsmFAGXBvLiXm2G50i5ZwvIvaRKIVav_PqNBhaSnpdsWSJO5FSRfWb6Yn0DTHHgKNx-ozULsoL938Kq7VyYhSIeMX46ZJVXYGviv-l72uCKewqdKiEKJHG3g5EhzRR1XKVS7rw7oklZRb1b_rvLksQrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
♨️
🗞
|
#فوووری
از تسنیم:
🔴
🔵
👤
پرسپولیس بخاطر استفاده از آسانی مستقیم به فیفا شکایت می‌خواد بکنه نه کمیته انضباطی
⚠️
❌
کمیته انضباطی فدراسیون شکایت های گذشته در مورد آسانی رو رد کرده بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139443" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139442">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
هر دو تیم و هر دو سرمربی به مساوی راضی بودن و خوشحال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139442" target="_blank">📅 21:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139441">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🗣
🟥
بازی خیلی خوبی بود از هر دو تیم ولی بنظرم بعدا حسرت این امتیاز های از دست رفته رو میخوریم، تراکتور تیمی نیست که مثل بازی جلوی شمس آذر به راحتی مساوی بده و باید قدر این موقعیت هارو بدونیم، بنظرم راحت میتونستیم ببریم اگر تعویض ها زودتر انجام میشد و باز هم…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139441" target="_blank">📅 21:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139440">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🗣
🟥
بازی خیلی خوبی بود از هر دو تیم ولی بنظرم بعدا حسرت این امتیاز های از دست رفته رو میخوریم، تراکتور تیمی نیست که مثل بازی جلوی شمس آذر به راحتی مساوی بده و باید قدر این موقعیت هارو بدونیم، بنظرم راحت میتونستیم ببریم اگر تعویض ها زودتر انجام میشد و باز هم اگر وسط زمین رو داشتیم متاسفانه هم جلوی تراکتور هم استقلال وسط رو دادیم و همین باعث میشه دقایق حساس فشار سنگین بیاد روی تیم و بعدش با کوچک ترین اشتباهی باعث میشه گل بخوریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139440" target="_blank">📅 21:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139439">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-text">📌
وسط وله…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139439" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139438">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-text">📌
وسط وله…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139438" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139437">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-text">🔵
دربی تهران در نقش‌جهان اصفهان!
پرسپولیس
🔴
و
🔵
استقلال؛ در دیداری حساس و هیجانی از دقایقی دیگر در لیگ خلیج‌فارس ایران به مصاف یکدیگر می‌روند.
🔗
برای پیش‌بینی این دیدار حساس همین حالا وارد سایت معتبر اسپورت‌نود بشید و با بالاترین ضرایب پیش‌بینی کنید:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
مینی‌اپ رسمی اسپورت نود:
👇
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/SorkhTimes/139437" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139436">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✔️
✔️
✔️
بی انصافیه اگه از عملکرد خوب مهدی تیکدری نگیم!
✔️
برای اولین بار تو عمرش اومد پست غیر تخصصی دفاع چپ بازی کرد و هم در دفاع و هم در حمله موثر و خوب بود
✔️
✔️
پر تلاش و انگیزه از دقیقه اول تا آخرین دقیقه ظاهر شد و امیدوار مون کرد
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139436" target="_blank">📅 21:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139435">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
ما به اینا نمیبازیم ...نه ساله نباختیم به اینا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139435" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139434">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
✔️
پایان بازی | شکست ناپذیری پرسپولیس به ۹ سال رسید/دربی جذاب برنده‌نداشت  استقلال
1️⃣
-
1️⃣
پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139434" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139433">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✔️
✔️
✔️
پایان بازی | شکست ناپذیری پرسپولیس به ۹ سال رسید/دربی جذاب برنده‌نداشت  استقلال
1️⃣
-
1️⃣
پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139433" target="_blank">📅 21:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139432">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
✔️
امروز هر کاری خواستن با مجید عیدی کردن از بس که اون سمت اتوبان بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139432" target="_blank">📅 21:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139431">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✖️
✖️
هافبک و کلا استقلال برداشته و خیلی خالی هست هافبک ما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139431" target="_blank">📅 21:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139430">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
✔️
هر دو گلر بد خوردن گلارو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139430" target="_blank">📅 21:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139429">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
گل مساوی و خوردیم متاسفانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139429" target="_blank">📅 20:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139428">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❤️
❤️
❤️
ما به اینا نمیبازیم ...گل اول و محبی زد روی پاس بیفوما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139428" target="_blank">📅 20:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139427">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
🔴
بریم برای نیمه دوم ..الهی به امید توووووو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139427" target="_blank">📅 20:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139426">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
امیدوارم نیمه دوم شانس با ما یار باشه و کارو تمام کنیم ..شاید ارونوف تعویض طلایی ما باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139426" target="_blank">📅 20:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139425">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
نیمه اول دو تیم خوب بازی کردن و بازی زیبایی و دیدیم از سمت هر دو تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/139425" target="_blank">📅 20:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139424">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
نیمه اول دربی بدون گل تموم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/139424" target="_blank">📅 20:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139423">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
بدون شک بهترین بازیکن نیمه اول .تیکدری و زارع بودن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/139423" target="_blank">📅 20:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139422">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
✔️
✔️
پرسپولیس خوشگل کیسه رو کرده تو قوطی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/139422" target="_blank">📅 20:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139421">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‌
❌
❌
پرسپولیس بهتر و سرتر و سرحال تر داره بازی می‌کنه و سوار بازی هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/139421" target="_blank">📅 20:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139420">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❤️
❤️
بریم برای بازی ..الهی به امید ...خدایا امشب و پرسپولیسی باش ..حس خوب و انرژی مثبت و بفرستید برای بچه ها ..انشالله برنده بازی ماییم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/139420" target="_blank">📅 19:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139419">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
✔️
همه چیز آماده دربی پایتخت؛
✔️
✔️
هم اکنون ورزشگاه نقش جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/139419" target="_blank">📅 19:29 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
