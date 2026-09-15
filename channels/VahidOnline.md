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
<img src="https://cdn1.telesco.pe/file/U1XMXwco1CELN4UxIggJKhxukAtl5TnPYMfaxLiRzLq4vbihQKS49SHFhnL_cmng2AquwDepJCvb7WQrsYGlGK-3t_PQ8_0kJ1t6-5eLvgXAJtXeub6GLoDuwF7rwrrZjt8Gf5hCBn4mmHwzODUXpzE6aSEI4UDyggeO6zVkIlmXOzkgCRDMpr_X6jaO9f1bjzufSaODwK5GR2EA3VZs8m2AXtZCHyoE5sBJL9QU1Y1n0UkiGVxSSjfrB0jYNpq98A51c8KfkbL1xXcjB9mPi6M2ctlIcznCKimt1Zcwoy-Ae9OYgkOum0hfsDFJdoKqvNMgKqZwH027fp66m7Xocg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.4M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 15:26:15</div>
<hr>

<div class="tg-post" id="msg-78379">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bIP5yz1uI3vLeQ6xxhSUs_1lBTlBdvI3VaUd3mEnlu-nvvq83BH0DJO5Ekv6w0w9uazLEwbLU9IVd1EXtUttvvI6GMh4qaAC2U3EmZSWGWeYoSzFbk0mi1l3_gj4F6GfBp6F-FF-eseNod0K0NeJ7JPmrDKXoWd4USCOb2sy40yn2nbXtIWp-lBPcxWmaH0VRCPbL4_YPSSer-cJK88zGH1LoktMvTKsHQgLapgQ7s47BnOfHOtGoshCjm3pSN2GIHEd-cCJfDtz-q_JhWeD1tLoBX9r_bITmVmU-a54s0MRDo_l2zeVL_RHaMRsKkoLIkCo1ooNSYf_SY8m5M9lFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست‌کم ۱۰۰ معترض در ۱۳ استان ایران در خطر اعدام هستند
سازمان "حقوق بشر ایران" اعلام کرد دست‌کم ۱۰۰ نفر از بازداشت‌شدگان اعتراضات دی‌ماه در ۱۳ استان ایران با حکم اعدام روبه‌رو هستند؛ بیشترین شمار این افراد با ۴۶ نفر مربوط به استان اصفهان است.
بر اساس فهرست منتشرشده، پس از اصفهان، ۲۲ نفر در استان‌های تهران و البرز قرار دارند.
همچنین ۱۰ نفر در فارس، هفت نفر در خراسان رضوی، پنج نفر در مرکزی، سه نفر در یزد و دو نفر در سمنان در این فهرست ثبت شده‌اند. در استان‌های خراسان شمالی، گیلان، اردبیل، ایلام و قزوین نیز هر کدام یک نفر با حکم اعدام روبه‌رو است.
این سازمان می‌گوید فهرست منتشرشده تنها شامل معترضانی است که دست‌کم در مرحله بدوی حکم اعدام دریافت کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/VahidOnline/78379" target="_blank">📅 15:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78378">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GOA8H2ScBFNEv6OAi9vteXzy21iHB0gPkZjZxrWnT1NLX_O8h0HUrM3rKHk7X4wsd181KP-SGvCwu8WHFfQhU8DgThq831o5mZplUXj0aD99_9A3U7-2PJwrO3wOdWaq2R8_4SbgdEMn244ONLemXlyaDiewiXZs5JM2CN-IVHagLV8fXC0zxHaO8seIBG4TGQ8TP-GueVu9bnzvqy7ybicU9b32S68Q-MAWtmI2sBdlJeAcCy8KyRAujU5S11E3L4aJPTk8Ve5-9Bjsbrupl-HM24GDJ15hwhZvNCF7N6jICE-ovze0FyrqMbPSAvpfk4fb4kDL2Ft2u9irpkMR7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، شامگاه دوشنبه ۲۳ شهریور ۱۴۰۵، از حمله پهپادی به دو «قایق صیادی» در حوالی بندر کرگان در آب‌های خلیج فارس خبر داد.
بر اساس این گزارش، در پی این حمله که تسنیم آن را به «آمریکا» نسبت داده، تعدادی از صیادان حاضر در این دو قایق مفقود شده‌اند.
عملیات جست‌وجو و امداد رسانی برای یافتن مفقود شدگان آغاز شده و نیروهای امدادی و دستگاه‌های مسوول در محدوده حادثه در حال جست‌وجو و نجات هستند.
تسنیم نوشته است جزییات بیشتر درباره این حادثه و وضعیت صیادان پس از دریافت گزارش‌های رسمی اعلام خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/78378" target="_blank">📅 03:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78377">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QF67Qj3BVLxCop4xkSKGeV9-OYZht6xTnN3vr3gAGiGAK9T2ggW6yNXbYGcRIHmIiyfg-x2PTnU221OvRMmH_TJA-MLstSXrsFY1knBUbJCkqdsG07hRtGnBd7TlfFljrB3mVwPznLF0mKZXk9ElNjtWgjvHN1t03VhHEYApxW9iQUEm1SPBsPh80MNHoUAjbEssMNJxFHPr3bis7aoD-epia7a7Ag9eEAkO13hjQ1Q1DdtuufCL-NPQ7xkDytvoADY6hzAiX2VI6sbTvWiRknKWO3av2oEMxDuG6akYLOLC46lciqZwovkXcblWFrCityNiUkVzDO1K1kxA25g0DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی است یک نفتکش با پرچم پاناما اخیراً در تنگه هرمز با یک مین دریایی برخورد کرده است. این ادعا کذب است.
✅
واقعیت: نفتکش «El Gaia» با پرچم پاناما ماه گذشته هدف یک موشک ایرانی قرار گرفت و از کار افتاد. آخر هفته گذشته، ایران بار دیگر این نفتکش را در حالی که در آب‌های ساحلی عمان قرار داشت، با یک پهپاد هدف قرار داد. این نفتکش در حال حاضر توسط یکی از شرکای منطقه‌ای یدک‌کش می‌شود.
ادعای کذب سپاه پاسداران نمونه دیگری از دروغ‌ها و تلاش‌های آن برای ارعاب است؛ آن هم در حالی که می‌کوشد مانع تردد کشتی‌های تجاری در تنگه شود
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78377" target="_blank">📅 23:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78375">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FKECnpvySdOJvxiXOS9g8z0jdHh577q4URexBrP5aZHGjlIBZWvY97VN6ldbP0CURI3YDSMjC2EoquhnxqfInaEAN3vP21kYKKl2DLv_z_iPf5_389C4lrsjCyInX_UqKMb58JkY-QfkE5fH0S08f8w8yimFloK3BbIlgQwlHDe1oAKDOZF5bRT0T42dUor9ehp1nX9tORDEl70CSNhW9Ysoy5gSmVnJztVCG4X59PDjtp6OcK_AFs9HSzrULBrGx1oRz2fC7WwB2basLbsbTh4xtjqZZ_-TRJ9kvpK1qO2nbjhYKFlA02cBWUlY14CrxrDxfP0xHaISST7RddeMMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/khgxbWMUmnKTUxafjtbZxxG632Xx1jKFnxdNlJQzxEdfC4lfyOuNykrBBZEJWUxFkxLw18Q_rMyG8AJ-ZLm2-mS1IIUXovXbsQKhndg4IyrExHJAB7yeVrLTX63Y1eYAInwCOYOV3MP6t-sRpy6ireuYp0GdvrCJQ1SRtGZpyTM8fqAzjkrDTdH5TV6WrYhKCxP-AdCRLfDiU54bgH6iyCGRKo6Zj8ttpmPSdTm3pIvl9131aynvoK61Xs8b3kDNpTRn7NRi26HvsiW6zSFq0mlYFLBNyx6QQHj0BmBoshN8CiHyihqV0igRb_WHB4eIqoENlu94U9TGdqhq0afbMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ در پیامی در شبکه اجتماعی تروث سوشال تاکید کرد که افزایش قیمت‌ها در سراسر آمریکا ناشی از سیاست‌های جو بایدن و دولت او بوده است.
او نوشت که حتی بهای نفت نیز در دوران بایدن بالاتر از سطح کنونی بوده و دولت او مانع از دستیابی جمهوری اسلامی ایران به سلاح هسته‌ای نیز شده است.
ترامپ با اشاره به اینکه قیمت سایر کالاها به شدت در حال کاهش است، افزود که بهای نفت نیز به محض پایان یافتن درگیری نظامی با ایران—که به گفته وی زمان زیادی تا آن باقی نمانده است—مانند یک سنگ سقوط خواهد کرد.
در دوران ریاست‌جمهوری بایدن، به‌دنبال وقوع جنگ روسیه و اوکراین و بحران‌های بازار انرژی، قیمت نفت در بهار ۲۰۲۲ به بالاترین سطح خود رسید؛ به طوری که قیمت نفت برنت تا حدود ۱۲۷ دلار برای هر بشکه افزایش یافت.
@
VahidOOnLine
رئیس‌جمهور آمریکا در شبکه اجتماعی تروث سوشال از کشورهای جهان خواست پس از پایان درگیری‌ها، هزینه‌های ایالات متحده را برای حمایت از کشتی‌ها و کمک به عبور محموله‌های نفتی از تنگه هرمز بازگردانند.
ترامپ با اشاره به اینکه نفت در حال عبور از این آبراه است، تاکید کرد کشورهایی که هیچ کمکی به آمریکا نکرده‌اند، باید خسارات و هزینه‌های این اقدامات را جبران کنند؛ زیرا واشنگتن این ماموریت را بیشتر به نفع دیگران انجام می‌دهد تا خودش.
پیش‌تر کریس رایت، وزیر انرژی آمریکا، اعلام کرده بود میانگین تعداد محموله‌های نفتی که با حمایت نیروی دریایی این کشور از تنگه هرمز عبور می‌کنند، رو به افزایش است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/78375" target="_blank">📅 23:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78374">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rk_USEtZ_xj4diqse49ZsVDiavi8OehHjlVQtFyiCxJ2vcwjEvXQPgEDT3_IBY7f4dvl5-3mdGuyC_c8BD9k6CORrhhvJnpwqqusx4HMSzcNyp4481S9GYmZsyxtj0NXoUutfBzuAucd-4PGjjxswYlBAB-950GsGxtkgp4jkBVJ96jEA7NSkgHYyuzP520TGEQ9hGvPkXZS__YZGooiUwgs4ORzdQEqAk_o8P0zjnMvK6UztQaRsu5Z1nIM2rZcUjw6jNKT2ZT0f-LWsHw7kbh1RWKev-G16SDTFTfQwgH1_shG6hwlnJf_XLVokOqQzzx35y77XnSFb4pKWvwqhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایرانِ شکست‌خورده می‌خواهد خیلی سریع و به‌شدت به توافق برسد.
من تصمیم خواهم گرفت که آیا ایالات متحده آمریکا وارد مذاکره بشود یا نه — ایده‌ای که نسبت به آن آمادگی داریم. از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
ترامپ نوشت: کشور در حال ورشکسته‌شدن ایران می‌خواهد سریع و به‌شدت به توافق برسد. من تعیین خواهم کرد که آیا ایالات متحده آمریکا وارد این داستان خواهد شد یا نه؛ چیزی که ما نسبت به آن نگاه باز داریم.
پس از انتشار این پست قیمت نفت اندکی کاهش یافت.
اظهارنظر اخیر رئیس‌جمهور ایالات متحده در حالی است که ایران گفته برنامه‌ای برای مذاکره با آمریکا ندارد و شروط متعددی را برای توافق با واشینگتن اعلام کرده است.
در همین حال، اسکات بسنت، وزیر خزانه‌داری آمریکا در راستای برنامه فشار اقتصادی بر ایران موسوم به «عملیات طرد اقتصادی» از همه افشاگران خواست تا چنانچه اطلاعاتی درباره «تسهیل‌گران تروریسم ایران» دارند در اختیار وزارتخانه تحت امرش قرار دهند.
او با انتشار پیامی در شبکهٔ اجتماعی ایکس خطاب به کسانی که در سراسر دنیا اطلاعاتی درباره شریان‌های حیاتی اقتصاد ایران دارند، نوشت: «این شانس شماست. اگر اطلاعات قابل پیگیری برای وزارت خزانه‌داری دارید، ممکن است واجد شرایط دریافت جایزه باشید، صرف‌نظر از این‌که کجا زندگی می‌کنید یا چه کسی فیش حقوقی شما را امضا می‌کند. اگر چیزی دیدید، بگویید».
او همچنین بار دیگر تاکید کرد که وزارت خزانه‌داری آمریکا عملیات طرد اقتصادی را «برای قطع تمام شریان‌های مالی رژیم ایران و حامیانش» آغاز کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/78374" target="_blank">📅 19:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78372">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/078a1aea27.mp4?token=uqq_nh1DQTLFi6OMhkn_7rbhn6H7c8Xr2IB-0w7eayeZo_RTWjUqAJGUMMUFXP5hW-0ylC71juH9tQJ_TqHlXZrlRdvkeo7xT7x8S8JpUW_j9nXzq3QS8CmNOHZ1lqp1T04N126XMjsCkM1zqrGfkneATGO_O_q7N8ywyZknIgR3ydDT8j21uWYss_BYTor3tTpyh1mnz5_6nGOoNRgjtwOH1raE9-ztYvDtqpJbntTztWfynGLhDrAjdZdCgd-AAt9zAQEquiC3rDHV7ZMW5cfpIlnC5uC47J6DkGCIFDP4N5YlmVy9_sX2q47oSawuexCocnH3MYOGv12zU0MXKg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/078a1aea27.mp4?token=uqq_nh1DQTLFi6OMhkn_7rbhn6H7c8Xr2IB-0w7eayeZo_RTWjUqAJGUMMUFXP5hW-0ylC71juH9tQJ_TqHlXZrlRdvkeo7xT7x8S8JpUW_j9nXzq3QS8CmNOHZ1lqp1T04N126XMjsCkM1zqrGfkneATGO_O_q7N8ywyZknIgR3ydDT8j21uWYss_BYTor3tTpyh1mnz5_6nGOoNRgjtwOH1raE9-ztYvDtqpJbntTztWfynGLhDrAjdZdCgd-AAt9zAQEquiC3rDHV7ZMW5cfpIlnC5uC47J6DkGCIFDP4N5YlmVy9_sX2q47oSawuexCocnH3MYOGv12zU0MXKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رشت، حامیان حکومت شبانه به آشکده سحرخیزان حمله کردند.
در ویدیویی که آشکده سحرخیزان منتشر کرده بود، عبارت "آش برای افراد با حجاب رایگان است"، به دیوار نصب شده بود و در چرخش دوربین، چندین مرد محجبه در صف ایستادند.
همین بهانه‌ای شد برای یورش و تخریب مغازه.
این اتفاق یکشنبه، ۲۲ شهریور ۴۰۵ رخ داد.
دادستان بلافاصله علیه آن اعلام جرم کرد و مدیر رستوران بازداشت و خود رستوران پلمب شد. ولی انگار این واکنش از نظر لباس شخصی‌ها کافی نبود و دیشب ریختن رستوران رو تخریب کردند.
via
pkhwshhal
,
yaghma_fashkham
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/78372" target="_blank">📅 18:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78371">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشگاه تهران - دانشجو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqYhUM7EpsBYSW1690TWjQSWOIH1zMQe3Fi4jGxN6pQ-Q4hCBYNDkvvIi2H34y4xXPj5FTahVQTDT3hMXOIks3Gv-NlWhPAC3aWCgWLmKKVPPzQU6UYTmWZ67HJnw_zTFZm4ZGE88yN_oICf2_Ihm01_nQ24Q6sLrfZx54AfR90q5RghJa9juErHMqVAOABhFkLqVhH7EcmIW0nWWhtBzYjM1XlPw4KCiQlj4XtPz-jzVBPzG2lOX5oGTRV1B7Z55NCn_R_U_mvtDDhwIMZM3E5Z6k34gmBtdhxhuW99lb4zEdN3Zdy0h9exCBrrUSeWQWYuWigIi5NOokOgFYVmrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
اتهام «بغی» برای محمدپارسا گلچین، دانشجوی دانشگاه تهران و دارندهٔ مدال طلای المپیاد!
بنابر گزارش‌های رسیده به تهران-دانشجو،
#محمدپارسا_گلچین
، دانشجوی ورودی ۱۴۰۳ کارشناسی ادبیات دانشگاه تهران و دارندهٔ مدال طلای المپیاد ادبی، به «عضویت در گروه
باغی
» متهم شده است.
همچنین، «اجتماع و تبانی علیه امنیت داخلی» و «اقدام تبلیغی بر خلاف امنیت ملی» دیگر اتهاماتی‌ست که به این دانشجوی نخبه وارد گشته است. او در جهت دفاع برابر عناوین مذکور، به شعبهٔ ۲۶۸ بازپرسی دادسرای عمومی و انقلاب مشهد احضار شده است.
محمدپارسا گلچین، شنبه ۲۲ فروردین ۱۴۰۵ به همراه جمعی ۱۸ نفره از دانشجویان در جریان یک بازدید دوستانه، توسط مامورین مسلح و به‌طرز خشونت‌آمیزی بازداشت شده بود
. پرونده سایر بازداشت‌شدگان نیز در جریان است و در انتظار دریافت حکم و احضاریه هستند. درصورت دریافت اطلاعات تکمیلی، گزارش پرونده‌های سایر دانشجویان متعاقبا در تهران-دانشجو منتشر خواهد شد.
#سرکوب
#بازداشت
#دانشجوی_زندانی
دانشگاه تهران-دانشجو
اینستاگرام
🆔
@Daneshjo_UT</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/78371" target="_blank">📅 17:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78370">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d288c0bbe.mp4?token=DAQeec1RYmpVAUBEz7qajepbmE-FpuAvJmMOrOa2EX4WzVBGThM5VU8I2Bx8p62NKSFIuX2VjLzZvQYiaI0o_RcoKcUKYle__7gTiOJXQQnfnnFLQEXmM2IHmEIUo3B9RZb7FXMr4WP8rTOqGZgMtuIWOy3EWefsRvTTdgP6i6-_smJTyYNIfSUitpJ6iESIwsaIpjWdeYDpMzgjMwMIBKPY0mJmOcbTaAQNcFseqXSUWNi_x2O1lYeaevhEIhq5FMJFZoD9M74E-RbjXaO2t7ihhLCKHQeURznqzvLkM2-RUeB2vJK8oD-wf-XV82RwNYwjMM1ukLplmsBB-tY41Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d288c0bbe.mp4?token=DAQeec1RYmpVAUBEz7qajepbmE-FpuAvJmMOrOa2EX4WzVBGThM5VU8I2Bx8p62NKSFIuX2VjLzZvQYiaI0o_RcoKcUKYle__7gTiOJXQQnfnnFLQEXmM2IHmEIUo3B9RZb7FXMr4WP8rTOqGZgMtuIWOy3EWefsRvTTdgP6i6-_smJTyYNIfSUitpJ6iESIwsaIpjWdeYDpMzgjMwMIBKPY0mJmOcbTaAQNcFseqXSUWNi_x2O1lYeaevhEIhq5FMJFZoD9M74E-RbjXaO2t7ihhLCKHQeURznqzvLkM2-RUeB2vJK8oD-wf-XV82RwNYwjMM1ukLplmsBB-tY41Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صفحه اینستاگرام رستوران «دستپخت بی بی» در تهران، به دلیل انتشار یک استوری با نوشته «هیچی کتلت بی بی نمیشه» به همراه موسیقی متن «بی بی گل» از معین، به اتهام «انتشار محتوای مجرمانه»، با دستور قضایی مسدود شد.
پیش‌تر نیز در سال ۱۴۰۱ نواب ابراهیمی، آشپز، در پی انتشار دستور پخت کتلت در اینستاگرام خود همزمان با سالگرد کشته شدن قاسم سلیمانی، بازداشت شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/78370" target="_blank">📅 17:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78368">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B5OWPz1wlBmxonD6YTNfwYshvFto5UjCrZtFhcPgeywIvLH77NBG_KkPVxPt5ArOA8Y2bt6zapHRYmOosBbmomY43bVPs484-duBDSl-9xdyAxXgq33-TqUyaSdbKrq35u9eLdNhcGiPwKme8lzoKBprf0sHjsuyC-2YcrhkgccNJrRmdvZBui1X-cR4p6J-PhHVjGMfQB9RuL8Qa1y-lpYY2eOaizlQuB0ovkkKQS2i5nCXvSMCXNrSpk-MFoGf-JjqAT6nftOr5ME0FKLupXHxF64uEO44nCW76Uc5hlxzrbU0QwGhJZjcvNTLlNjPspHFqYWYnoLX4v8Ebo9YjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hfbwfEBNpiJxcuFETSUUV8yL4tD8zQhkuWcEm9Bp1LUsyTAWz2vmFxJWQnmdYv3IJH_Z70FMoYQOv6YOqOxG_sNsSgOfV4KTxTG9MUwHrosHu4g971-g8zhZGHN4oArnfE0gZbSTzUzOAyTtHiTmTFdTsVuZWrImXMU_5nQroroBtLGXWYhXUK_TD3Tywjq4XjNybuYJlDkQNGAK9pgLSwCtt-J2YYtaWajsTiWpltNp9uualc60bLk2f5GNnmzSrkxYVWij3T9NeH_STaZ3PA1naHlMEMg8i5LUSbYRpU8FK7CmixO0qrDXacv0SM4IjN1C4f3Lj3LDxlRo9i1bfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«یحیی سریع»، سخنگوی نظامی حوثی‌های مورد حمایت جمهوری اسلامی، از انجام عملیاتی گسترده با ده‌ها پهپاد و موشک بالستیک علیه اهداف نظامی در منطقه خمیس مشیط عربستان سعودی خبر داد.
سریع گفت پایگاه هوایی «ملک خالد» در این منطقه هدف حمله قرار گرفته و آشیانه‌های جنگنده‌ها، رادارها، باندهای پرواز و انبارهای مهمات از جمله اهداف حوثی‌ها بوده‌اند.
سخنگوی نظامی حوثی‌ها این عملیات را پاسخی به حملات هوایی عربستان سعودی به یمن دانست.
@
VahidHeadline
«محمد بن سلمان»، ولیعهد عربستان سعودی، امروز دوشنبه ۲۳شهریور۱۴۰۵ در جده با دریاسالار «برد کوپر»، فرمانده فرماندهی مرکزی آمریکا، سنتکام، دیدار و درباره تحولات اخیر منطقه گفت‌وگو کرد.
خبرگزاری «رویترز» به نقل از رسانه‌های دولتی عربستان سعودی گزارش داد این دیدار در شرایطی انجام شده که درگیری میان عربستان و حوثی‌های مورد حمایت جمهوری اسلامی در یمن شدت گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/78368" target="_blank">📅 16:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78367">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwI8zh5Rb1-iQ0OWEcUJCDwJdTpx_yKhdGV-TzASJ2XitjYnZYtvF58mySYa69LFXlFOO3qO7Xm2MUjn7dvDR5DT6SYaNQ7kYa9neYmCafOE8wT5S5J62jFlQV_mV2q7Gay-JhHf6bFyFy_T_1bd26xnyZEgOUoLrpe-PCWkP3Zn2-FMAatqypX2aoRQQkvPqWjnP-5If-v5ZiVlC35fGyLGi-b9Q8lxxrgAes7vsOfyT-D63qIbNbvmAnX6vOZboEedLDkVQCC-2vd4Vt4OZMWHwgBirMVjZXdI47c8qF3hXMfdsqIQ5-qxPCT2k2c2tcfENy3lqYSaML1uTrZN0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین امروز دوشنبه ۲۳شهریور۱۴۰۵ گزارش‌ها درباره کمک نهادهای چینی به جمهوری اسلامی برای هدف قرار دادن یک پایگاه نظامی آمریکا در اردن را تکذیب کرد.
خبرگزاری رویترز به نقل از وزارت امور خارجه چین گزارش داد پکن «قاطعانه با این اتهامات بی‌اساس مخالف است».
این واکنش پس از آن مطرح شد که روزنامه «وال‌استریت جورنال» به نقل از مقام‌های آمریکایی که نام‌شان فاش نشده است، گزارش داد جمهوری اسلامی پیش از حمله موشکی ۱۷شهریور به پایگاه «موفق‌السلطی» در اردن، تصاویر ماهواره‌ای این پایگاه را از نهادهایی در چین دریافت کرده بود.
در حمله موشکی جمهوری اسلامی به این پایگاه نظامی آمریکا، سه نظامی آمریکایی کشته شدند.
براساس گزارش «وال‌استریت ژورنال»، مقام‌های آمریکایی نام نهادهای چینی را که گفته می‌شود تصاویر ماهواره‌ای پایگاه را در اختیار جمهوری اسلامی قرار داده‌اند، اعلام نکرده‌اند. این مقام‌ها همچنین دولت چین را به مشارکت یا دخالت مستقیم در این اقدام متهم نکرده‌اند.
«دونالد ترامپ»، رییس‌جمهوری آمریکا، نیز روز یکشنبه ۲۲شهریور۱۴۰۵ به گزارش‌ها درباره دسترسی جمهوری اسلامی به تصاویر ماهواره‌ای یک پایگاه نظامی آمریکا در اردن از طریق نهادهای چینی واکنش نشان داد.
ترامپ گزارش مربوط به دستیابی جمهوری اسلامی به این تصاویر، پیش از حمله‌ای را که به کشته شدن سه نظامی آمریکایی منجر شد، «کم‌اهمیت» دانست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/78367" target="_blank">📅 16:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78365">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XGcFQiA7dLZ9o8uqcpJZI2bU7GW7EHMsmcwFO4gSZ3QQrLiUha19SH_QdjJmQVqFc9XOjQoa3suzZnfrIo2veGwXTnn1VFa1MvKLNHbLK4mEwla-_LV3Q5oIHPSFqIXFGVMVBH3xWRiKA2TEAmLMdolzeA8sUbBcf6L80irh7g7Cps90_lzR78EOeuPANL4o9ny-LfvRyUQ8hM_FzyTb0SLvfyAYsxpGbIjdlDo2pCpDi10gP_K_mxD2UsWQCO9K6CByEoWqax2bo27aOj_KO5IBXa-fyKXKtyORALi9KGYGx4XFnFUWgGH7FxJ4FmafDNYJUMgvjb0WrhSzfieNoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/avxn93VMWOUrb8t61DV9GxdbAuMpCCdOKzqe1KA9mHMMBcU1Aj-EfeV29uzq6pLRFk_Xk2JlsZqPxGUalRgYUtaTlx6DxrmvEwShPLkENwHG0zSyBffmpY2A13j5DhBvJiw8gwzR7ohurRRjzqn-_umJAPwyGkJazEu_JGwzZuqcAbx5lettw9jMPoSZ_9JB_JoQHZhZle9SQ4Axh7wMLhEOmm2hDh1LZno0Ckk--2Z3y5PpkQwLtzX56SJkyCWVnqdjB50DMwvppnYxECKe5kWF2AmPr1KhUlVK4jGxTnLDCQ72EY7LPdJ7v0Di1hnmnOaaW2YrI5Rqn-a1to74Dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی روز دوشنبه و پس از اعلام خبر صادر نشدن ویزا برای محمد اسلامی، رئیس سازمان انرژی اتمی ایران برای شرکت در نشست مجمع عمومی آژانس بین‌المللی انرژی هسته‌ای در وین، از احضار کاردار اتریش در تهران خبر داد.
بقایی با اعلام این خبر گفت می‌دانیم که این تصمیم تحت فشار آمریکا گرفته شده است اما این واقعیت، چیزی از مسئولیت اتریش کم نمی‌کند.
@
VahidOOnLine
پیش‌تر:
به گفته یک مقام آگاه که با اسوشیتدپرس گفتگو کرده، محمد اسلامی، رییس سازمان انرژی اتمی ایران، برای نخستین بار در چند سال گذشته احتمالا در نشست سالانه کشورهای عضو نهاد ناظر هسته‌ای سازمان ملل متحد در وین شرکت نخواهد کرد، زیرا از سفرهای بین‌المللی منع شده است.
این مقام گفت اتریش از کمیته تحریم‌های سازمان ملل خواسته بود برای اسلامی معافیت از ممنوعیت سفر صادر شود، اما این درخواست پذیرفته نشد.
این مقام که اجازه اظهارنظر درباره این موضوع حساس را نداشت، به شرط ناشناس ماندن صحبت کرد.
اتریش به عنوان میزبان سازمان ملل متحد در وین می‌تواند برای مقام‌های تحریم‌شده درخواست معافیت از ممنوعیت سفر کند تا آنها بتوانند در نشست‌های بین‌المللی سازمان ملل حضور یابند.
به نوشته این خبرگزاری آمریکایی، حضور نیافتن اسلامی در کنفرانس آژانس بین‌المللی انرژی اتمی نشانه دیگری از وخیم‌تر شدن سریع روابط ایران و کشورهای غربی است.
از زمانی که اسرائیل و آمریکا در جریان جنگ ۱۲روزه به تاسیسات هسته‌ای ایران حمله کردند، جمهوری اسلامی اجازه دسترسی بازرسان آژانس به تاسیسات هسته‌ای آسیب‌دیده در این حملات را نداده است؛ این در حالی است که تهران بر اساس تعهدات خود در چارچوب پیمان منع گسترش سلاح‌های هسته‌ای، از نظر حقوقی موظف به همکاری با آژانس است.
آژانس همچنین نتوانسته است وضعیت ذخایر اورانیوم ایران با غنای نزدیک به سطح مورد نیاز برای ساخت سلاح هسته‌ای را راستی‌آزمایی کند.
تحریم‌های سازمان ملل که دوباره برقرار شدند، شامل ممنوعیت سفر، تحریم تسلیحاتی متعارف، محدودیت‌های مربوط به توسعه موشک‌های بالستیک، مسدود کردن دارایی‌ها و ممنوعیت تولید فناوری‌های مرتبط با برنامه هسته‌ای است.
با وجود اظهارات این مقام درباره احتمال عدم حضور اسلامی در کنفرانس، خبرگزاری دولتی ایرنا روز شنبه گزارش داد که اسلامی تهران را به مقصد وین ترک کرده است تا در کنفرانس آژانس شرکت کند و با نمایندگان کشورهای مختلف دیدار داشته باشد.
مقام‌های ارشد کشورهای عضو آژانس بین‌المللی انرژی اتمی قرار است از دوشنبه تا جمعه در مقر این نهاد در وین گرد هم بیایند.
آنها درباره بودجه آژانس تصمیم‌گیری و آن را تصویب خواهند کرد و درباره دیگر مسائل سیاست‌گذاری، از جمله پادمان‌های هسته‌ای در خاورمیانه، گفت‌وگو خواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/78365" target="_blank">📅 16:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78364">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AQXbssNUn2jY0R2t4dg62hjchDrt4XhcrscYq0I7Bb8YsnMkFpsZ1wY_V6qrDDy_Ykzi3Ogv5GMsUptbTMwhxFHmbdsL2W5OCRxUi7URiTZGKU-rwj_PzNdOyzqFJqbjQXvcgVodQ_eRkF1Omf5U896h3w0aUTv2WWZHfbe5RIlx-z1Q0hnv2eA7G2kEz_RAcPYUpaqF3dQbRlBoMFOVSrJl3ykH8hrE2GydPT1llo9F-PHhfRp9TNFw9GTV2mW4L09ToqqQKNAnToL0_CZN54wjmnmXQqIXA85ic-pdlgTfLdgcl_70WNdh_B_wxuA47S_mbTfFEytlgnQXKTXrEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آستانه چهارمین سالگرد قتل حکومتی مهسا ژینا امینی از اصفهان، رشت، فومن، مشهد و نیشابور ‌خبر از تشدید فشار برای تحمیل حجاب اجباری و حضور دوباره گشت ارشاد، حجاب‌بان‌ها و نیروهای لباس‌شخصی در خیابان‌ها می‌دهند.
یک شهروند گفت در میدان علیخانی اصفهان ون گشت ارشاد مستقر شده‌ است و ماموران «بدون تذکر قبلی»، زنانی را که حجاب اجباری ندارند بازداشت می‌کنند و با خود می‌برند.
شهروند دیگری فضای اصفهان را «به شدت امنیتی» توصیف کرد و گفت نیروهای گشت ارشاد در مناطقی چون جلفا، مرداویج، چهارباغ و میدان نقش جهان مستقر شده‌اند و با زنان بدون شال و روسری، برخورد می‌کنند.
یکی دیگر نوشت: «در اصفهان دیگر ون گشت ارشاد نیست، اتوبوس است. با اتوبوس دختران را جمع می‌کنند و می‌برند.
...
در مشهد نیز شامگاه ۲۲ شهریور، نیروهای مسلح وارد پارک ملت شدند و به زنان تذکر حجاب دادند.
شماری از شهروندان از رشت گزارش دادند برخوردهای قهری درباره حجاب اجباری در این شهر شدت گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/78364" target="_blank">📅 16:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78362">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bc68687ab7.mp4?token=B7aJzrh_Y9tSdxdOifxKWkMBk8eTAHbP_oRRSM1z67M_JiK5Lff_rQQ_EIQWB4mZANG3zdEtXefJ8XAuc1_TM9HEx7aHt9R8xrhFFZ8cQPyQ0FyZWhTVT3uwPLczLdJnwM5BSgHt6rnZz2_Xx6lVqNf545f1w1ybU5hM3gNkBhKxTYodXEQQBXKaEmJhO9R2kMOOvNef4IfHWvYeLTMNaVQt96iXTGUm-0rEFi6QbOyO6fFsSXBBTQB4JNu7_4losm5p9irGOVhggy9CR7eECE9zx7J55l4486TKMSm9rXhTVeAP6uj3rCuVV6sjaecpsQbuB568lRMs0OIC-sMO0w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bc68687ab7.mp4?token=B7aJzrh_Y9tSdxdOifxKWkMBk8eTAHbP_oRRSM1z67M_JiK5Lff_rQQ_EIQWB4mZANG3zdEtXefJ8XAuc1_TM9HEx7aHt9R8xrhFFZ8cQPyQ0FyZWhTVT3uwPLczLdJnwM5BSgHt6rnZz2_Xx6lVqNf545f1w1ybU5hM3gNkBhKxTYodXEQQBXKaEmJhO9R2kMOOvNef4IfHWvYeLTMNaVQt96iXTGUm-0rEFi6QbOyO6fFsSXBBTQB4JNu7_4losm5p9irGOVhggy9CR7eECE9zx7J55l4486TKMSm9rXhTVeAP6uj3rCuVV6sjaecpsQbuB568lRMs0OIC-sMO0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ویدیوی نجات خلبان آمریکایی در ایران
۲- یک نفر از ۷ نفر سوت موشک که داره به سمتشون میاد رو می فهمه.
سعی می کنه به نفراتش خبر بده اما نمی دونه کدوم طرف بدوئه. در نهایت یک انفجار هر ۷ نفر رو می بلعه.
A_z_im
سی‌بی‌اس پس از پنج ماه با یکی از دو افسر ارتش آمریکا گفتگو کرده است که در نیمه فروردین‌ماه هواپیمایشان در اطراف اصفهان سرنگون شد.
این افسر که براوو معرفی شده، لحظه برخورد موشک دوش‌پرتاب با جنگنده اف-۱۵ آنها را مانند برخورد یک قطار باری توصیف کرد و گفت به همراه خلبان که در این گزارش «آلفا» معرفی شده، تلاش کردند هواپیما را نجات دهند اما خیلی زود دریافتند که امکان نجات هواپیما نیست و باید خروج اضطراری انجام دهند.
پس از خروج اضطراری (ایجکت)، آلفا و براوو در حالی روی زمین در بیابان ناهموار در ایران فرود آمدند که حدود هشت کیلومتر از یکدیگر فاصله داشتند و هرکدام تنها بودند.
آلفا سالم فرود آمد، اما براوو خوش‌شانس بود که زنده ماند.
براوو گفت: چتر نجاتم در حمله اولیه آسیب دیده بود. یک لحظه به بالا نگاه کردم و دیدم چتری وجود ندارد؛ ترسناک‌ترین چیزی بود که در تمام عمرم دیده بودم. همان‌جا مکث کردم و دعا کردم: «خداوندا، اراده تو انجام شود. اما اگر قرار است از این ماجرا جان سالم به در ببرم، به کمک نیاز دارم.»
او در پاسخ به این پرسش که «فکر می‌کنید هنگام برخورد با زمین با چه سرعتی حرکت می‌کردید؟» گفت: براساس توضیحاتی که دادم و جراحاتی که داشتم، متخصصان معتقدند با سرعتی بین ۱۱۳ تا ۱۶۱ کیلومتر در ساعت با زمین برخورد کردم.
او افزود: یک معجزه در روزگار مدرن بود. باور دارم این اتفاق گواهی بر لطف خداوند در زندگی من است که باعث شد از آن لحظه عبور کنم؛ به‌گونه‌ای که هرچند دچار جراحت شدم، اما آسیب‌های فاجعه‌باری که می‌توانست توانایی‌ام برای زنده‌ماندن را از بین ببرد، متحمل نشدم.
این سقوط باعث شکستگی کمر براوو شد. او همچنین دست و شانه‌اش شکست، مچ پایش پیچ خورد و سر و صورتش بر اثر بریدگی و خراش خون‌آلود شد.
براوو گفت، مجروح بودم، اما همه ما آموزش دیده‌ایم که با شرایطی که با آن مواجه می‌شویم سازگار شویم و بر آنها غلبه کنیم. با وجود جراحات، تا جایی که می‌توانستم سریع از محل فرودم دور شدم.
براوو به سی‌بی‌اس گفت امن‌ترین جایی که می‌توانست به آن برود، ارتفاعات بود.
بنابراین با وجود شکستگی استخوان‌هایش تصمیم گرفت از مسیر کوه بالا برود و خود را به خط‌الرسی در ارتفاع حدود ۲۱۰۰ متر، برساند.
@
VahidOOnLine
چیزی که می‌بینم رسانه‌ها و کاربران فارسی‌زبان دقت نمی‌کنن اینه که این مصاحبه نمی‌گه که افسر آمریکایی با دست و پای شکسته کوه ۷ هزار پایی رو بالا رفته؛ بلکه می‌گه خودش رو به ارتفاع ۷ هزارپایی رسونده. بین این دو تا خیلی فرق هست.
در نظر داشته باشید که خود اصفهان بین ۱۶۰۰ تا ۲۰۰۰ متر از سطح دریا فاصله داره. یعنی ممکنه ایشون فقط با صد متر صعود خودش رو به ارتفاع ۷ هزار پایی برسونه.
Ardeshir
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78362" target="_blank">📅 08:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78361">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g0ctMAJ5_GKi6MLmrlyjh2jc0spaX-kULKZacN1AHzWxdH9OepinbVqCdWQDhJm4PZJjCeWLoDTZNyALioc6yXt116A8Pep0Lqw3nf67dpV-bn07r43ojx0V_HAw-7WsY75xkGumymiE1Cds6cjP8I_m4et-_uYgPfQw1_29gnJabdGZPe7uyscr2EnbMB0E7z8esbUw_nA_LcmqShPAFVogW9brE6LOJzu8FKlwPEx1fCgUsW4l3Du97rySzw-ys_8aLsXv37MWcUbPNwdf1NYd_mQwptJPZYAwRmTDMykvH79YW7y_uuRi_bnNgd7D8YPd0iSWRSS9fm4ogYQxYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه عمان از تعویق‌ نشست ایران و کشورهای حوزه خلیج فارس و منطقه خبر داد؛ نشستی که قرار بود روز دوشنبه ۲۳ شهریور در شهر صلاله عمان با محوریت وضعیت تنگه هرمز برگزار شود.
بدر بوسعیدی، وزیر خارجه عمان، روز یکشنبه ۲۲ شهریور در شبکه ایکس نوشت که این نشست «به منظور دستیابی به اجماع» به تعویق افتاده است.
او تاکید کرد عمان همچنان به تقویت گفت‌وگوهایی که به «ثبات و همکاری پایدار در منطقه» کمک کند، متعهد است.
عباس عراقچی، وزیر خارجه جمهوری اسلامی، پیشتر گفته بود که روز دوشنبه در نشست هشت‌جانبه وزرای خارجه کشورهای ساحلی خلیج فارس و دریای عمان در صلاله شرکت خواهد کرد.
قرار بود در این نشست درباره طرح ایران و عمان برای ایجاد سازوکاری جهت تردد امن کشتی‌ها در تنگه هرمز گفت‌وگو شود.
تعویق این نشست در حالی اعلام شده است که آمریکا پیشتر تاکید کرده بود در مذاکرات مربوط به تنگه هرمز مشارکت نخواهد کرد و هرگونه مذاکره مستقیم با جمهوری اسلامی را بر پرونده هسته‌ای متمرکز می‌کند.
مقام‌های آمریکایی به کشورهای منطقه گفته‌اند واشنگتن درباره وضعیت تنگه هرمز مذاکره نخواهد کرد و موضوع اصلی مذاکرات احتمالی با تهران باید برنامه هسته‌ای جمهوری اسلامی باشد.
مارکو روبیو، وزیر خارجه آمریکا، نیز پیشتر گفته بود تنگه هرمز نباید تحت کنترل جمهوری اسلامی باشد و آمریکا برای تضمین امنیت کشتیرانی در این مسیر اقدام خواهد کرد.
در مقابل، جمهوری اسلامی و عمان تلاش کرده‌اند کشورهای منطقه را در گفت‌وگو درباره سازوکار تردد کشتی‌ها در تنگه هرمز وارد کنند.
قرار بود نتایج رایزنی‌های تهران و مسقط درباره مسیرهای امن کشتیرانی در این نشست به کشورهای منطقه ارایه شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78361" target="_blank">📅 22:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78360">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzinYbfLBZEiE33U5TTsJVq-ighwig1kIxjZLlPEz9uwIJIrgyHvrlHmLVSRQR3cJXTm3skdhpM11G3aNP3-zoYLImx8MJXxMVNQajqUsePLfC29Ec-nMskBg5q-wSMSps7AihGR4LnbxoDqgXReMrojUYHGY9hHN739FtXP3twEKYaJ95yQZat3jcSsgbkvp96NCcB_l7BT1VFbx2IMedJiFkdkMD2fkgGtruEKDnH30J8R383E9w-7kcvS3EVB7XnMubefwYgtusifvO1PM5KjgPlDBllvHrcrR1iSFJHUow5kgwL4ogl5lKBP7cv_ocq_StWR8jkGHw3dhss8Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه نیویورک تایمز روز یکشنبه ۲۲ شهریور ماه در گزارشی به نقل از چند مقام ایرانی نوشت، مسعود پزشکیان، پس از حمله نیروهای سپاه پاسداران به سه کشتی تجاری در تنگه هرمز در اوایل تیرماه گذشته، به‌شدت خشمگین شده و این اقدام را «بی‌پروایانه و غیرمسئولانه» خوانده است.
این حمله‌ها که منجر به آتش‌سوزی یک نفت‌کش حامل گاز مایع قطر و آسیب به شناورهای دیگر شد، درست زمانی رخ داد که ایران به توافقی با ایالات متحده برای پایان دادن به درگیری‌ها نزدیک شده بود.
بر اساس این گزارش که فرناز فصیحی به نقل از مقامات ایرانی نوشته است، پزشکیان پس از آگاهی از این ماجرا با احمد وحیدی، فرمانده کل سپاه پاسداران، تماس گرفته و با لحنی تند خواستار پاسخگویی شده است. با این حال، وحیدی ضمن سلب مسئولیت و ابراز بی‌اطلاعی، به رئیس‌جمهوری اعلام کرده که نه مجوزی برای این اقدام صادر کرده و نه شورای عالی امنیت ملی از این عملیات مطلع بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78360" target="_blank">📅 22:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78358">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/930e263d13.mp4?token=O1Q4dNcJzAmhIf-_WtBpeuWkfZCJuW0gB8-T_YX87rnTg_XcJUspgFPqi8zqPs1u03iofxv12HSPNHQPsPqsp4pbKdXhAFj-zmdht2IPAGthrVVvWY8KHzk7PE2RZ-zsenNknMdAONl8YDEFxM2P6IzXMXT8_Z6Mf5Nek0F7PTJ2xZsrSnpJUAGf36E6HNKGbZaJvBQ_tagmmOMgu_9sZE5X1wxaaHbyspU8twTTcLsc4s6ueJtWdDt7RcsoadZFYrHPlvkpTcmvslbFibENfdeiMvNSUaTzmGX8YPgQ33cnOwJapt4IuntZgMA8ClC6vkdGt1lnPshcxYJw9nQAjA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/930e263d13.mp4?token=O1Q4dNcJzAmhIf-_WtBpeuWkfZCJuW0gB8-T_YX87rnTg_XcJUspgFPqi8zqPs1u03iofxv12HSPNHQPsPqsp4pbKdXhAFj-zmdht2IPAGthrVVvWY8KHzk7PE2RZ-zsenNknMdAONl8YDEFxM2P6IzXMXT8_Z6Mf5Nek0F7PTJ2xZsrSnpJUAGf36E6HNKGbZaJvBQ_tagmmOMgu_9sZE5X1wxaaHbyspU8twTTcLsc4s6ueJtWdDt7RcsoadZFYrHPlvkpTcmvslbFibENfdeiMvNSUaTzmGX8YPgQ33cnOwJapt4IuntZgMA8ClC6vkdGt1lnPshcxYJw9nQAjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز پیش، پس از اعلام نرخ سوم بنزین در ایران، تصاویری واقعی در شبکه‌های اجتماعی منتشر شده بود درباره اینکه بعضی از تلمبه‌ها در جایگاه‌های سوخت (پمپ بنزین) امکان نمایش همه ارقام بنزین ۱۰ هزارتومنی رو ندارند و مجبور شدند در ادامه نمایشگر یک صفر بچسبونند روی بدنه تلمبه.
حالا محمدباقر قالیباف، رئیس "مجلس شورای اسلامی" در «ایران»، اون انیمیشن رو پست کرده.
ولی درباره قیمت سوخت در یک کشور دیگه:
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/78358" target="_blank">📅 21:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78357">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qiz5EvDT4XqZKwhM7N9Prqo5o8xNdK7hrlLU94bZKbHvNTnyAIMBoDTgIp6cQGN7YPbsnzE9REIcocg8ibuD-j18ogKvgtEHxKlUPltljmHdQX9QZ5D56AlDhru_yy8hEljTmlP3pqhCiKvbkUjzV40kdii-iWU91rgVQlbg4BodnoW28sqtM1fhc9qYUsVMktwasYvMgzYfoDW5gMIhaUp4kNPTAavaYX420VD3lqoPHlevJdt9e9QmQEHeYArkRVfJcZqbmSO9X5ZuKcIhajXNeqCNPWbH9FNeQmcctqBt--v1_wVNWMYHBEBcCFdP3F3brO6dmvkFTvBWDuqLTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین رسولی‌نسب، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در شاندیز، به اتهام «محاربه» از سوی دادگاه انقلاب مشهد به اعدام محکوم شده است. او در حال حاضر در زندان وکیل‌آباد مشهد نگهداری می‌شود.
خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، روز یکشنبه ۲۲ شهریور ۱۴۰۵، گزارش داد حسین رسولی‌نسب به «محاربه از طریق مشارکت در تخریب اموال عمومی» و «اجتماع و تبانی علیه امنیت کشور» متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78357" target="_blank">📅 18:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78355">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pIahZmXZG-hdy7OG6Zgl2DwtQUKABGRYDIxpFj6EMFERY0YtygyxeJVaezKBDhBNCs-u4EVvvGx7WKYTAhIEaqL8oK5lOfiDCHmrZEJUNyh6LU209T_wld64Qvx2ED3THQyeQrLYM9YsXpwLZDwJmPDHyPidRqNYFoOAfAzqZgi0o72eUXwnIqBq5drjg7v5UklUmhrUUQfvF3-qVaEz7UgBqcIlfJo491Ad6l6TDTI5ku0pLHrXOJzAJUal4urMcqStjV82ToVYJj42ayWLXbbIweFbbNXFFnF41z7ci9AJQLyvRpBLio4wb5TqoAKuwdvCxJV85-srvW3IVsU-Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HzE1vF0qlDdaWeA4dtQL3d4B6mCDmxnBDmnIpQYp8phhuKBUx7OdBKuyqeC2zcpyDd4AB16IeJqRlQpjgNsoEQ0-kzA39jtY6KRw_FDIqamrMBqbz05YvaPPIdkN1Z2yk037C7WSbT-n-T8aL4_7BBedAw0NAef8dM0Qdgmz-zXOCdwgrZmEFt7Wb25jQZf6EC0Nfc0bWAzoeSEe7dGMdLVfqfDj1HONUBvfGtfXZ2mbuxsIJ3ok3MoEGdbVImpg-xR7I2gj3V8v16kuRuOmMXVTn5W21CEE-0o1Je1l8TdcR-p09JYmz313S83Ml3tiSphYHgdSRkG5Vh_afHKb1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان ثبت احوال: در کارت ملی‌های جدید از هوش مصنوعی و بلاکچین استفاده کرده‌ایم
quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78355" target="_blank">📅 18:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78354">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l4bJkKO_Mf4C0cgVYKz2u2EX8lXkeEO4JF7Ys-8C40MQE_f3v1QqG_vdEmh9N5e5V6EWAZ9FWgZ0G4_MsxbJkVWopeH8HtIcZoOH-yNx46yUwuFiABAlxqIXuMZFXVPtGMfUGz66Z7AJjokeMMpr9el4WewejIVeMG4eC1lKKRIYvakR9jQu_sasu3hhu72gRNjJccQYt_8bny0nuj9-izeZb1q1ULKc3aXUws93q0JrzAi9KuEc2eWglm7l6RjgxDgas5wA9NySKvMeeUhhtztot3ktZLpSJckRKjig942OQjYkNbwpu8iU2uaERSuN3WylQ3Ue6obEb5ZOqmXroA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز یکشنبه ۲۲ شهریور۱۴۰۵، گفت «موضوع ایران» ممکن است پیش از انتخابات میان‌دوره‌ای آمریکا پایان یابد، اما در هر صورت جنگ با ایران بلافاصله پس از این انتخابات تمام خواهد شد.
ترامپ در جریان سفر به ایرلند و در حاشیه مسابقات گلف اوپن ایرلند، درباره احتمال توافق با جمهوری اسلامی گفت ایران به‌شدت خواهان توافق است و به‌طور مداوم با آمریکا تماس می‌گیرد، اما واشنگتن تنها توافقی را می‌پذیرد که به گفته او «درست» و مطلوب باشد.
او همچنین در پاسخ به پرسشی درباره دیدار وزرای خارجه کشورهای خلیج فارس و دریای عمان با ایران گفت این موضوع برای آمریکا اهمیتی ندارد و تصمیم درباره دیدار با جمهوری اسلامی به خود این کشورها مربوط است.
قرار است این نشست روز دوشنبه در عمان برگزار شود. ایران می‌گوید یکی از موضوعات مورد گفت‌وگو در این نشست، مسیر جدید تردد در تنگه هرمز خواهد بود.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، نیز بار دیگر گفته است شرط ایران برای بازگشایی تنگه هرمز، بازگشت آمریکا به تعهدات خود در تفاهم‌نامه اسلام‌آباد است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/78354" target="_blank">📅 17:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78352">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q3GxVvE_G025TTgkq_iAtcqgxMEgcnploWDpBk-PjE7dCPOPF7YIFiuh7tlaSPROMHU31EZzsz39cC3gdzl_IbFKMYW_GvECJJKyt-0T9eI7zYIyeU_3RnKM0_2P9eiC8HKbJY3-CYRLJ05qCo1k6knHAFKyExbU57FMr1ZSB5B8xTdl8dc5pD3BMTVgkYUP4UJH9ng3Bj944IZe0da7ppSz1Xz8n7J0W948iTviSwm4ZGVXq7aiZjJXdHYna-M9dSv9bweSgypZKYOeRtdBnKQqBnLkEkZzh-kyYjlD_f2oqbnna8kmFOUZTzy2XqIsa2kelojaYzZL9Hf9YkVxMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h5QJs8neQ0CrWDqaC_M0gpDxeqvdkPLxPZI-RijTNfist7vHFHdtJ2v6yPpZZrvux8T5DOrTLfKReO8H_CIdkjS0hoA1Z7eh0nNzwzdZ4gfYBlMeSGBobzGcsIxijuq0gIdWiAKaOvV9pQAaa5r0Q4OG1Q7wZipeux5CBkE5-sGDJ6wMTsR8lC5P_QSDRXdK2sFFNZ-Cs1IJwWeB4lOsm5G2shgZYi39NiDuYt7JbaM1TjBIkw0v1xP0ssXdzuElXtY41W9Jp_JdiDFuba1ZZLwvilzJRjvLJMY0_F_CLuM3R6mf2Sh2hu2yJbhK43jyNArHk6YIaVWQWe-m0drk3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) روز شنبه، با صدور یک هشدار امنیتی، از هدف قرار گرفتن یک کشتی در تنگه هرمز خبر داد.
این نهاد نظارتی دریایی اعلام کرد: «گزارشی مبنی بر وقوع یک حادثه در محدوده تنگه هرمز دریافت شده است. یک کشتی هنگام عبور از تنگه هرمز هدف اصابت یک پرتابه ناشناس قرار گرفته است.»
@
VahidOOnLine
امیر تیموری، فرماندار شهرستان قشم، اعلام کرد یک کشتی تجاری حدود ساعت ۵ صبح امروز در محدوده جزیره هنگام و ساحل شیب‌دراز جزیره قشم هدف قرار گرفته است.
به گفته فرماندار قشم، در این حادثه یک نفر کشته و سه نفر دیگر مجروح شده‌اند.
تیموری عامل این حمله را آمریکا اعلام کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/78352" target="_blank">📅 15:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78351">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddbff18bf8.mp4?token=n3EDgcFlEr2_ElIQ9T4vBQw7PFpyMbqs8Dyj06CxiKEvq0zkX9zPz07l1ZbdNPFrxdox20g6vkoLLdZn2FueO0M07Mcc6Bhm2enKAxWhdv5O38h_sVfpZUfUsbgu-P8tRNow92qvfF7q7tkyiT_S00i6tAMOnRkYXINlHkV3FKVrQ74zMB4zu8v-Qtck1kspJGrRswH3SHZt4Cc5eOtbkm4E-3tDvkKi8pbiuQa-8cNLvJOp5X3Oo0prN6BqqUb57FKzohesQNaGPrpUdiMcXLbner1zFt0AC3MVhIJxxz2_k_gI-ap7ClvbRIGmGCAoyBha-CLwd6M3abQm7TvMYDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddbff18bf8.mp4?token=n3EDgcFlEr2_ElIQ9T4vBQw7PFpyMbqs8Dyj06CxiKEvq0zkX9zPz07l1ZbdNPFrxdox20g6vkoLLdZn2FueO0M07Mcc6Bhm2enKAxWhdv5O38h_sVfpZUfUsbgu-P8tRNow92qvfF7q7tkyiT_S00i6tAMOnRkYXINlHkV3FKVrQ74zMB4zu8v-Qtck1kspJGrRswH3SHZt4Cc5eOtbkm4E-3tDvkKi8pbiuQa-8cNLvJOp5X3Oo0prN6BqqUb57FKzohesQNaGPrpUdiMcXLbner1zFt0AC3MVhIJxxz2_k_gI-ap7ClvbRIGmGCAoyBha-CLwd6M3abQm7TvMYDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تور اجبارى اتاق شلاق براى "عبرت" متهمان
یکی از شهروندان با ارسال ویدیویی که مخفیانه از اتاق اجرای احکام شلاق ثبت کرده، مشاهدات و تجربه مستقیم خود را با بنیاد عبدالرحمن برومند در میان گذاشته است؛ روایتی که به‌زودی در قالب یک شهادت‌نامه تفصیلی منتشر خواهد شد.
او درباره انگیزه خود از انتشار این ویدیو پس از چند سال می‌گوید:
«آنچه در جریان بازداشت و صدور این حکم بر من گذشت، در برابر حجم بی‌پایان ظلم و بی‌عدالتی شاید اهمیتی نداشته باشد؛ آنچه برای من اهمیت دارد، تاباندن نور بر گوشه‌ای از این سازوکار مخوف است تا همگان ببینند مردم ایران برای داشتن یک زندگی معمولی با چه مجازات‌های تحقیرآمیزی روبرو می‌شوند.»
@
IranRights
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78351" target="_blank">📅 15:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78350">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9047a957c6.mp4?token=phjnPaw-e_5O6wAYGvfnE6v64MgC7njGNqxEf9OQxaQDK9fxrRuyjIoSVssd_G0Q2IDJozgUzlSi7Q7FOvRALxWlbT0NBgQ09_qGnJaTD58GlO3Yia3TyZ5DwRXTJmiPpqDs93a5xHq-Zg5T7RoToX-KDQzg36ytesvfXGJlwsaI-B1Wnj_kVj_fjZRD1WYS_x92XAdNgJ0Vq3-nwh7VsUEbgox74jDvp8_ISK9WM47IPaw9y3Cx2jEosqHEuUT59Uw_tg1PkS6j0IISG-1gHyQHQuEuUpCG6O7S14i5GBQ3UAPBAQT395A7lHahOtTDH_VkhKQthcQCX8OnU7mRvw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9047a957c6.mp4?token=phjnPaw-e_5O6wAYGvfnE6v64MgC7njGNqxEf9OQxaQDK9fxrRuyjIoSVssd_G0Q2IDJozgUzlSi7Q7FOvRALxWlbT0NBgQ09_qGnJaTD58GlO3Yia3TyZ5DwRXTJmiPpqDs93a5xHq-Zg5T7RoToX-KDQzg36ytesvfXGJlwsaI-B1Wnj_kVj_fjZRD1WYS_x92XAdNgJ0Vq3-nwh7VsUEbgox74jDvp8_ISK9WM47IPaw9y3Cx2jEosqHEuUT59Uw_tg1PkS6j0IISG-1gHyQHQuEuUpCG6O7S14i5GBQ3UAPBAQT395A7lHahOtTDH_VkhKQthcQCX8OnU7mRvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهوری آمریکا در جریان دیدار با مایکل مارتین، نخست‌وزیر ایرلند، در دوبلین بر اعمال کنترل مقتدرانه و یک «محاصره دریایی باورنکردنی» بر تنگه هرمز تاکید کرد و گفت این اقدامات مانع از جهش شدید بهای جهانی نفت شده است.
دونالد ترامپ همچنین گفت نیروهای سنتکام به‌طور میانگین روزانه ۲۵ شناور و قایق را متوقف و توقیف می‌کنند؛ اقداماتی که به گفته او بیشتر آن‌ها در تاریکی شب و در جریان گشت‌های شبانه انجام می‌گیرد.
این در حالی است فرماندهی مرکزی آمریکا، سنتکام،
امروز
اعلام کرد طی ۶۰ روز گذشته و از زمان ازسرگیری «محاصره دیوار فولادی» ایران، مسیر ۱۰۰ کشتی تجاری را تغییر داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78350" target="_blank">📅 23:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78349">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2vAiT_i7NXh-XE_Fq_50V0CHQKd-pqGFhyT3xg0et9j6oC0sDNawhYvHzuftYbPxj3x0CyLPxui5cDCju8B_5lKVsnlMvexZ0l7g-g7f9nHDUvTrg_POD1cafxNdxGvQlDbDN3NzHiQdOwQxsVQ_wqImYx7gch7LmPpcqd771rk0GOdXrsiL48MMpOq1rpFUNMwHeYZKMZQDUXnPDL1E5pPEABdHeFneGXarLZiW-hOAZ84Zu7ujYJZxNyc8BYMivc-8NDYHWV6kFCf35B7rgWSuG4BEviRUmo7evU6YiUpz7LkriINXBGxOJlETGdjfEwrW2GACmuq4w-uCgLc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واژگونی یک دستگاه اتوبوس حامل کارگران مجتمع مس سرچشمه، در صبح شنبه ۲۱ شهریور، یک کشته و ۳۸ مصدوم برجا گذاشت.
سید محسن مرتضوی، رییس مرکز فوریت‌های پزشکی رفسنجان، با تایید این خبر گفت ۳۸ مصدوم این حادثه برای دریافت خدمات درمانی به بیمارستان منتقل شده‌اند. به گفته او، بررسی‌های اولیه نشان می‌دهد ورود یک دستگاه ون به مسیر حرکت اتوبوس باعث انحراف و سپس واژگونی آن شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78349" target="_blank">📅 21:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78348">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5jlQMHc48wwMLHcvPc8_IovhoRhCCZDg6NBt-GDMS7VcvMzxyR1ycHZ9sLOMZEFR_66wW5eYLaanMs4EVsnDbo8EwdiBjMY_P7ICt00Ap6mdt1zS76ckZtYKDw2YO4t-9wYSUkEAku6lZOHBkzaLDUDZn-gLwfwcXAB_5nhZsvJwkY7zDFsNNHVApjEDj9SNJyM0Gm4jIkHxm1yJFjJ_dS62IUZwDsaVUxf5QoLfebGVoLOFd-nt_8pDAztbsH8tfx_QEW-0dDTpOU7dyGN9GrwfEWeCkAjix1JZSHDXFNsBbg0xbXpnuJyWBFN4cZ34KRxeVlPi-n5W73hpZQ-3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع امنیتی عراق به خبرگزاری فرانسه گفتند نیروهای امنیتی این کشور سکوهای پرتاب پهپاد را منطقه دورافتاده الطیب در استان میسان در جنوب عراق و در نزدیکی مرز با ایران کشف کرده‌اند.
همزمان خبرگزاری رویترز به نقل از دو منبع نظامی در عراق اعلام کرد این منطقه مرزی پس از کشف سکوهای پرتاب پهپاد بسته شده است.
کشف این سکوها پس از حمله به خط لوله نفت عربستان سعودی انجام شده است؛ حمله‌ای که ریاض و بغداد گفته‌اند از خاک عراق انجام شده است. بغداد روز شنبه گذرگاه‌های مرزی شلمچه و چذابه را نیز بسته بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78348" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78347">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYvdaq4tTszrc0at8vSIwBe4GZAErfdf9qpI8gH5HAEBKaLW9THg4AB8feIWpT0DPQg7gQuXkqP8PKimdbLy471ka9ebILWVC5TVMyORmrXnsJF-5Uymq8x1Z2LT1hxyj8lPBc1CM4XRFPVjdqakDXV4CCn4RxSQW2_cT3WsvmY6BgJyyOUaZPKXGWU-rcQIXlgWjDsZWJsgOpN3FhRuxs_hbDdVayLrF51c9PxktjzwjEnzjeNeuso9iuNMdwh3eB1LEbNfdC86NYIeiEpKvyw9f8iGhIvv1VqyDNih8fQ1tYNqXQlM7d5X8UcziPlivWwea_ufl6b_UG6HyyxcHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، به نقل از یک منبع آگاه گزارش داد تفاهم نهایی جمهوری اسلامی و عمان درباره مسیرهای جدید کشتیرانی، به معنای بازگشایی تنگه هرمز نیست و باز شدن این تنگه به اجرای هفت شرط تهران از سوی آمریکا بستگی دارد.
این منبع گفت تهران و مسقط پس از گفت‌وگوهای فنی و دیپلماتیک، در اوایل شهریور درباره جزییات مسیرهای جدید ورود به خلیج فارس و خروج از آن به توافق نهایی رسیدند و قرار است این تفاهم به‌زودی با حضور وزیران خارجه کشورهای منطقه اعلام شود.
بر اساس این گزارش، تفاهم تنها میان جمهوری اسلامی و عمان است و کشورهای دیگر، از جمله عراق و کشورهای ساحلی خلیج فارس، برای اطلاع از جزییات مسیرها و ترتیبات تردد در نشست حضور خواهند داشت.
مهر نوشت مسیر ورود به خلیج فارس به‌طور کامل و بخشی از مسیر خروج از آن در آب‌های سرزمینی ایران قرار خواهد داشت و تردد در این مسیرها بر اساس ترتیبات تعیین‌شده از سوی جمهوری اسلامی انجام خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78347" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78346">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0c0eda53bf.mp4?token=l6KUlRR_nnK2xonHHiunWr9qNTduhif-SIE-_F8qS8134vRv5Ee6EEvGIig1TcOwGMNK617SgTuu34G8JY9wrcAYUz12HkESJ6RK9hhBWWGmT065x_hTH21mVG7mTtREfMWOm5GN7g4D9v6qzgEFUSGo7P7VGSaGY5m21rlly5xaW2YaIZRAX-05FlvLnV-M_u0rCM-ycRU1c7e2GOOudSiHFJKRUgLU1E-3h15EwDd614roKmouwzUu96q0ZBTP1UT4rkUGMd-fI9oXCW97ToTE_Ui2wDnpfp_X3y8iMlYSnWRSa7mj4OzfD9mgJSAYvbTD85tJXVc_vxp8PoENZw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0c0eda53bf.mp4?token=l6KUlRR_nnK2xonHHiunWr9qNTduhif-SIE-_F8qS8134vRv5Ee6EEvGIig1TcOwGMNK617SgTuu34G8JY9wrcAYUz12HkESJ6RK9hhBWWGmT065x_hTH21mVG7mTtREfMWOm5GN7g4D9v6qzgEFUSGo7P7VGSaGY5m21rlly5xaW2YaIZRAX-05FlvLnV-M_u0rCM-ycRU1c7e2GOOudSiHFJKRUgLU1E-3h15EwDd614roKmouwzUu96q0ZBTP1UT4rkUGMd-fI9oXCW97ToTE_Ui2wDnpfp_X3y8iMlYSnWRSa7mj4OzfD9mgJSAYvbTD85tJXVc_vxp8PoENZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت امور خارجه، روز شنبه ۲۱ شهریور ماه گفت اطلاعات تهران نشان می‌دهد حمله موشکی آمریکا به لامرد از خاک یکی از کشورهای حاشیه جنوبی خلیج فارس نیز انجام شده است.
اسماعیل بقایی در گفتگو با رسانه‌های دولتی ایران گفت این موضوع نشان می‌دهد آمریکا «برخلاف همه قواعد و اصول حقوق بین‌الملل» از خاک و حاکمیت ملی کشورهای دیگر برای حمله به ایران استفاده کرده است.
او تاکید کرد ایرانیان این موضوع را پیگیری خواهند کرد.
بقایی همچنین گفت برخی کشورهای همسایه، برخلاف «اصل حسن همجواری»، اجازه داده‌اند از قلمرو آنها برای حمله به ایران و «ارتکاب جنایت جنگی علیه مردم» استفاده شود.
در نهم اسفند ۱۴۰۴، یک سالن ورزشی در لامرد فارس، مورد حمله دو موشک قرار گرفت که منجر به کشته شدن حداقل ۲۱ نفر، از جمله ۴ کودک، و زخمی شدن ۱۰۰ نفر شد. این حمله اندکی پس از حمله هوایی به مدرسه شجره طیبه میناب رخ داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78346" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78345">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2qBK6HZRrpXVm58RDSfj87gTQZqunGYb2mWH6KGd7AFtMC1PXIdLaVtq9umVaVSSiGc5w9Dipjn7VsjGIIi5lMLgm6KeUyAvbawcb1oKcUohZcLsfSR3L8kG7oEyR8Kfh9QBdwTftYfA4XVjHF8Iwh0bTETObCqPLoHUpprLmDvldXs47JUbJla947ug_sbAfdwGR0Znr0XFXFTmhL-WKBay1gqHbgUJI1XqGKXZE6kyyDLI60cDR5QxhGBqFPdXGNrCaSZ_7kBQ3aIlAMElZp3w8G2EaceFYDk5owtruPSm4rryzdF3_dvVXllkdymrz75OV5weCU-cn_HJavObw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت احتمالاً جمهوری اسلامی مسئول حمله هوایی به عربستان سعودی بوده که به تعطیلی خط لوله شرق به غرب انجامید.
او روز شنبه در دوبلین و در پاسخ به پرسش خبرنگاران درباره مسئولیت ایران گفت: «فکر می‌کنم مسئول‌اند، احتمالاً خودشان‌اند.»
ترامپ افزود با محمد بن سلمان، ولیعهد عربستان، گفت‌وگو کرده و او را «دوست خوب» خواند.
رئیس‌جمهوری آمریکا همچنین گفت حوثی‌های همسو با جمهوری اسلامی با دولت او تماس گرفته‌اند و اعلام کرده‌اند نمی‌خواهند آمریکا مستقیماً وارد درگیری شود.
او گفت: «آنها به‌مراتب ترجیح می‌دهند ما درگیر نباشیم و بیشتر شناورها را عبور می‌دهند. فقط یک کشور هست که از آن راضی نیستند و ترتیبش را می‌دهیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78345" target="_blank">📅 15:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78344">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/243b69b1d1.mp4?token=Bt4_PIrOvZQXQ8j5Ad0-dCqm1GsEzBA_bYvgsZGc0NZMOh1qxngPs9M8O2OMyYUhcB2eUysGW8PSqZkb7vJrzOja2aj_neF427pMyjFAHzlu3m2VAAdmdfsQjsdv83qYXRlUOFFvSxXaRE2dnmEjMuYvqXs-YiPUjPHhEGb_El9IQ_EVik-XlOnJCNuhI7mfDfC-iDmw6-Y9S_QXNNDLIuBNOiLyVVk2dovSAyZleBMJ0AHTyPvTkd5ggoaIiIPE9FVS4hmakNBy7uCFOax7P8EvFViK0ewGm3HMdCwg-jMy4e-74fgwkVlOPw2vgAiT7fHJPapVuOIDBf5-iIHkiA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/243b69b1d1.mp4?token=Bt4_PIrOvZQXQ8j5Ad0-dCqm1GsEzBA_bYvgsZGc0NZMOh1qxngPs9M8O2OMyYUhcB2eUysGW8PSqZkb7vJrzOja2aj_neF427pMyjFAHzlu3m2VAAdmdfsQjsdv83qYXRlUOFFvSxXaRE2dnmEjMuYvqXs-YiPUjPHhEGb_El9IQ_EVik-XlOnJCNuhI7mfDfC-iDmw6-Y9S_QXNNDLIuBNOiLyVVk2dovSAyZleBMJ0AHTyPvTkd5ggoaIiIPE9FVS4hmakNBy7uCFOax7P8EvFViK0ewGm3HMdCwg-jMy4e-74fgwkVlOPw2vgAiT7fHJPapVuOIDBf5-iIHkiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای منتشرشده در رسانه‌های اجتماعی نشان‌دهنده ازدحام در خروجی مرز بازرگان است.
برخی گزارش‌ها دلیل اختلال در تردد از این گذرگاه مرزی را «محدودیت‌های ظرفیت پذیرش در سمت ترکیه» عنوان می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/78344" target="_blank">📅 15:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78343">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUtsi3BgcIbgS26np-XfaWUz3W2PsXHlIxqdThNvYNZOENVTxYjyjImpofi2OXm5Tu14sYjkjpPD-kzHyuS_6HRL5FAfrfx9nHwlx26YBD0n_wl0EVjz38IiXjoumGxxMUcs5JjyHi5SS5nJHTQPSGpOZ8xyTuBkAEkZV3w57pb546pluEC8tt3akn02blsltD2YYmoC70F9MSgm5td-PW92EXX559tensDxN2LMlfWU1DZtY3TNOg4IoHOgOwxVFvyHFnYKPq58qAKwsRPqcWf5GOEpcOoI-94M6VIjpep774y6EYUZC6GfsKN-uPktv4W1aXf4cKD5kPzoQLFdoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون استاندار خوزستان اعلام کرد مرز چذابه نیز همچون شلمچه از بامداد امروز با اعلام مقام‌های عراق تا اطلاع ثانوی بسته شد. بنابر اعلام ولی‌الله حیاتی، هیچ تردد کالا و مسافری از این مرزها انجام نمی‌شود.
ساعتی پیش رویترز بع نقل از دو منبع امنیتی نوشت عراق پس از تازه‌ترین حملات پهپادی صورت‌گرفته به عربستان سعودی، دستور بستن گذرگاه مرزی شلمچه بین عراق و ایران را به عنوان یک اقدام احتیاطی صادر کرد.
مرز چذابه در استان میسان عراق قرار دارد و دفتر نخست‌وزیری عراق بامداد شنبه فرمانده عملیاتش را برکنار کرد. این برکناری پس از آن انجام شد که تحقیقات تأیید کرد آخرین حملات پهپادی به عربستان سعودی از خاک عراق انجام شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/78343" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78341">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V4gdpPt8t2YIRTOpdvZm3zx566MXLRuKR_oCYEzo3fDiK9P7m_V8-oW7YsRh5ZxVD80ELsXx78EBzuHRkztqWOP6dpJfDfwS1Ll8E1I9CRXrZstYjKsDsmA4vH1QAkZUQypneGjzC685wTd-SqC1_i_ToHaV5TzS4MoGe1B9azYNgEXOjfv1nnvOIWa3GEohzDu_b5-bMSge2aix0KPJhy72exa0YdTKTcUBpwuup0qIGfgtbYCN05ia8yWXDu3RiO5Zpakz_fnqWEaBrfymNhzUwJwYaqa8btlVKl3wy_IZNikef1RuudY-SGLGA2b6mA9YUAhmcbirCUXgEEj6rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fm2ZRfyUXW37wwVKhlbSVQlq2JH0ykZMlsYeV2FzGBw7lqQjfdWHOX1CtHREKyIpNwIW9fT-c5n0bFA51XMYvoRy7KJQP_VlM6eOTZ8NBBzv_Hs35L8fsbkxdwN_ax3ewn8jQq6MsXtS-gEnGG5NFJUnahBIdS9Irxmd_L_Q1tVC5lwTMHSp3q7madN-1a04-1hb4BwdghP5_Z78uJKzgpAM197r7vjtNcS2FgsCRpvGWbDoCJF1jzki2qjH0sOOSM2t_vum4TYtS70By5pTtyINu6K4YZ45ijPAiU6MB9mhF0VDTP42KHO9w3Unn0NuDn38OWBvbawwm7NAZ2im5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درگیری میان نیروهای نظامی و امنیتی جمهوری اسلامی و افراد مسلح در منطقه «بخشان» سراوان، پس از بیش از هفت ساعت همچنان ادامه دارد. «شیوار نیوز» از حمله به نیروهای حکومتی از دو محور، شکسته‌شدن بخشی از حلقه محاصره و خروج شماری از افراد مسلح از محدوده درگیری خبر داده است.
این درگیری حدود ساعت چهار بامداد شنبه ۲۱ شهریور ۱۴۰۵ و پس از محاصره یک خانه مسکونی آغاز شد. شبکه اسناد حقوق بشر بلوچستان پیش‌تر از استقرار گسترده نیروهای نظامی و امنیتی و استفاده از سلاح‌های سبک و سنگین در این منطقه خبر داده بود.
براساس اطلاعات منتشر شده از سوی شیوار نیوز، نیروهای نظامی و امنیتی پس از آغاز درگیری، محدوده حضور افراد مسلح را محاصره و مسیرهای منتهی به محل را مسدود کردند. بااین‌حال، در ادامه افرادی از خارج محدوده محاصره، نیروهای حکومتی را از دو محور هدف قرار دادند.
@
VahidHeadline
قرارگاه قدس نیروی زمینی سپاه پاسداران اعلام کرد در جریان درگیری با افراد مسلح در شهرستان سراوان در استان سیستان و بلوچستان، سه نفر از نیروهای سپاه کشته شده‌اند.
بر اساس اطلاعیه این قرارگاه، این سه نفر با عنوان «پاسداران گمنام امام زمان» معرفی شده‌اند.
قرارگاه قدس همچنین اعلام کرد که تا پیش از ظهر روز شنبه، چهار نفر از افراد مسلح ناشناس نیز در جریان این درگیری کشته شده‌اند.
این اطلاعیه جزئیات بیشتری درباره هویت افراد مسلح، گروه یا سازمان وابسته به آنها، محل دقیق درگیری و چگونگی آغاز درگیری منتشر نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/78341" target="_blank">📅 15:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78340">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AqIJCohlpDOmz6r_wm0nBWc3cD-d-3Jb8lOB6IGX788h4_FqCioAnR_neWabdyBMPyqiA0n9Om7NQz1lJz4aj3JQfF9jPjCkz40O_oJnQo_-M0IEUw6EMrbLVY4GVlCCBR_JZlZEXRtnmf0tJOI1Ja2-kyiWzaJnRya2j_jVs-JFJNKtG-7AbmUqLEToyDNFM8vXls_HAbY8dMxNQTkszxFq4K1q1-u0TY4WrEclnfCns6fm30-7r0pvwb8SXIHY2VflyaEgP-ptEQU7Rn5R24idqvbGrSPGH7nDa7n9_ElN8PDIbZ2Z5ZuLfmN-Ug4Pzw6FW4JaWM3rkoqKjpHkyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سودا ابراهیمی شمس‌آبادی، بلاگر ۳۳ ساله اهل بندرعباس، که از ۹ فروردین در بازداشت به سر می‌برد، به اعدام محکوم شده است.
بر اساس این اطلاعات، شعبه سوم دادگاه انقلاب بندرعباس به ریاست قاضی خواجه‌حسنی، سودا ابراهیمی شمس‌آبادی را با اتهام‌هایی از جمله «توهین به رهبری»، «فعالیت رسانه‌ای و تبلیغی برخلاف امنیت ملی»، «اقدام اطلاعاتی و امنیتی به نفع دولت‌های متخاصم» و «عکسبرداری و ارسال تصاویر برای رسانه‌های فارسی‌زبان خارج از کشور» به اعدام محکوم کرده است.
دادگاه همچنین او را به دو تا پنج سال حبس، محرومیت از برخی خدمات دولتی و مصادره اموال محکوم کرده است.
حکم اعدام سودا ابراهیمی شمس‌آبادی روز اول شهریور به وکیل او ابلاغ شده است.
بر اساس اطلاعات رسیده، ابراهیمی شمس‌آبادی در جریان دوران بازداشت، به مدت ۲۰ روز در سلول انفرادی نگهداری شده و در دوران بازجویی تحت فشار شدید قرار داشته است. خانواده او در این مدت از محل نگهداری و وضعیتش اطلاعی نداشتند.
قاضی خواجه‌حسنی که این حکم را صادر کرده پیشتر در سال ۱۴۰۲ از سوی مقام‌های قوه قضاییه در زمینه‌هایی از جمله صدور بیشترین احکام و جدیت در انجام کار مورد تقدیر به عنوان قاضی نمونه قرار گرفته بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78340" target="_blank">📅 15:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78337">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/myDK-gBz7VFfuN4ysNC36zdPQer2cgRCq_Iv_7mEcTbuQ0fWwXctr3QM_YRe9MAF4A_AiS-QigxTZ6pkzyHVDq7Wq6W98CVVGXZihh8o1aP6dUvvXPwedZh073gBpfJ7sUrBPbVlckEm_LJEuRN85pzpAvIwdwyfRUfHQLNALEf9exk2alix3F2a0WNb8hehppM7oiEr2CoHSDhrlXTGxGmT_Xhw3E0BHOxil4wM1Ee5LvJeshcROFnQQ6ve0HrbNXIrryVVU0T_iLS8XMjN2M8ZyO8VICsM7Cqc_xhyrxVeK68bcVWYG88w13rJNh0ck9fbr3Cig0THVeHsY9gEgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q647DV7W0jONfWZCfQQ41C1ZoByPuwORNR3hZEkwr1UWJntoiCyE479B5cn3Q43qaEQVICJ92mtrnELIPX30u9u5Sm2YSjlEFTyET4UyQv9N6S0kVxZCvH0lg2t6oHCPEyQB1nVL6OohbqK2KUF-gqqNIaHfLU18wx50Z4HvakGD6HBTSezscN1vIskizyectts_UDSZj_1ahsxYaBL9gQ1JpPCYkr8ZTp_iEx_AZIsyrVX3rHgCO80iolZkmIBOhpyqqhM21vCLu0e1MYxbQ_iCf1iAjbopaCvBOEfWfwrflehaiCDO-udzj4oc-uR7HTHOe927HiKQU1PPGPx29g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X7FnYHNgDYfqtZiFHHs3JnJIS0hSmNCizo57Cw9y31L6QR61KTf3ZGmBw38t9vyIfO6BpepBUROEEiKP-qGvDAdXQlsHipQPPtL9M24cmhmtbevjCh6HFE_dKM00Z-WyCMTEHlD9mtsqX3fScMDVf9Hh3dzDJQyZqqRh95gqB1x_3f0mbEDNcuk-SOnQZWY6ZaKXBuELaa6b4Kr9QslfKvL55dx05Iim2J4iygGwgrmzo2aFQTOeYhmgGwIF_BGxy9ydcFUuxWrjaX7tlVPB-roFRyDYuOlg_DSu6EdSWxhWm3w7ArZi58YwHbOYSCs4RPY_BJMuEjw1k61ztbjsOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت انرژی عربستان سعودی روز جمعه ۲۰ شهریور با انتشار بیانیه‌ای اعلام کرد که خط لوله انتقال نفت «شرق-غرب» (واقع در مناطق ریاض و مدینه) صبح پنجشنبه هدف چندین حمله قرار گرفته است.
در این بیانیه آمده است که به دنبال این حملات، عملیات انتقال نفت در خط لوله مذکور به صورت احتیاطی متوقف شد.
این رویداد همچنین منجر به مصدومیت تعدادی از افراد شد که خدمات درمانی و مراقبت‌های پزشکی لازم به آن‌ها ارائه گردید.
@
VahidOOnLine
وزارت خارجه عربستان سعودی اعلام کرد خط لوله نفتی شرق به غرب این کشور با پهپادهایی که از عراق پرتاب شده بودند، هدف حمله قرار گرفت.
وزارت خارجه عربستان سعودی افزود بنا به درخواست نخست‌وزیر عراق، در این مرحله تصمیم گرفته است اقدام تلافی‌جویانه انجام ندهد.
@
VahidOOnLine
خبرگزاری رویترز گزارش کرده که بغداد دستور تعطیلی گذرگاه مرزی شلمچه میان عراق و ایران را صادر کرده است.
دو منبع امنیتی عراقی به این خبرگزاری اعلام کردند که عراق این گذرگاه را به عنوان اقدامی احتیاطی و در پی حمله پهپادی از مبدأ عراق به خط لوله نفت شرق-غرب عربستان سعودی، بسته است.
گذرگاه مرزی شلمچه یکی از مسیرهای زمینی اصلی میان ایران و عراق است.
براساس گزارش‌ها پهپاد شلیک شده به عربستان از استان میسان عراق شلیک شده است. این استان در قسمت جنوب شرقی عراق و هم مرز با ایران است که مرکز اداری آن شهر عماره است.
@
VahidHeadline
رویترز نوشت: به گفته این دو منبع، عملیاتی گسترده برای تعقیب و پیگرد عاملان این حمله به عربستان در جریان است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78337" target="_blank">📅 05:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78336">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/78336" target="_blank">📅 22:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78335">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOpK1tp0cpaaHvtHT_3ZJlgfg4gXu5RLh_YvyOzCpQ_wbDbc_ymINFYqCaaYIDsZkF7KR6L_hKFuR2WZzPCFBXGRA8pDvcEqUXNr7GvcLgYchvbwtajgJ6MTR2u1S4DH6W9QbWZ8My_v8Y4UYdxKTyyGQ03BRGDnd1zs_3eoUbyHbixmw9Ln_PzE2HQc7NX8afApDw5QyMLpXx_smvj3vA4aa6toLR6DLQy_iD7zr5YvETmev9aNrlaAh9WPGhEIIi8Lk1PdKDt--R1L9enuMpzkzh9XIxS0FrTlS1DDIHvrs6-PzpNm5ZaNUsCVFHhBv25XFcSIHpdrURnV8tX-6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس دولت چهاردهم جمهوری اسلامی که به هند سفر کرده است روز جمعه ۲۰شهریور۱۴۰۵ در پایتخت این کشور اذعان کرد که فشارهای آمریکا بر ایران به مرحله «دشوار و خطرناک» رسیده است.
او با اشاره به این که جهان امروز در یکی از «پیچیده‌ترین مقاطع خود» است، خواستار «همکاری عملیاتی» کشورهای عضو بریکس شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78335" target="_blank">📅 20:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78334">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=kzSPmz7jPN5JOvKgDmq0kotBODueSyHqzzuCjFrtS_YGJVPMNSM1lASzx9_3x_IQJdRlwSn3SS5F0yilD28GZn_yE6RTsfFeW6H0u-n7oMSGDECojEArpn6gacdoLMmr2Zd3HXiR8pvK6ELbiynJd5wGiRMCHJxmdizDB2ErllmWnnLsbJ7FWAfP3LhGzSVcWMdwl_K0Dq8ceETou4NLmQBJqLWXlLTBm7I14JID0c1qNv0acBSO-eIcjkqIGTNS6jI8GwV4ScF8I_6E-YmMQjk0lh8zvzaU6E0LobXh8C5HD-lvpH3tcZ_IC7XwihikD0cormgNUIXjAHRw00W1_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=kzSPmz7jPN5JOvKgDmq0kotBODueSyHqzzuCjFrtS_YGJVPMNSM1lASzx9_3x_IQJdRlwSn3SS5F0yilD28GZn_yE6RTsfFeW6H0u-n7oMSGDECojEArpn6gacdoLMmr2Zd3HXiR8pvK6ELbiynJd5wGiRMCHJxmdizDB2ErllmWnnLsbJ7FWAfP3LhGzSVcWMdwl_K0Dq8ceETou4NLmQBJqLWXlLTBm7I14JID0c1qNv0acBSO-eIcjkqIGTNS6jI8GwV4ScF8I_6E-YmMQjk0lh8zvzaU6E0LobXh8C5HD-lvpH3tcZ_IC7XwihikD0cormgNUIXjAHRw00W1_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواهر امیرمحمد شاه‌کرمی با انتشار ویدیویی در صفحه اینستاگرام خود، از حضورش در مکانی خبر داد که به گفته او، برادرش آخرین لحظات حضورش در آنجا را پیش از بازداشت سپری کرده بود.
او در توضیح این ویدیو نوشت: «۱۸ شهریور، برگشتم به همان خیابانی که آخرین نگاه‌های برادرم آنجا بود؛ تا صدایش را از همان‌جا دوباره بلند کنم. این‌بار ایستادم برای صدا زدن نام امیرمحمد شاه‌کرمی.»
در این ویدیو، خواهر امیرمحمد با در دست داشتن تصویری از برادرش، نام او را در همان خیابان فریاد می‌زند.
امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، در ۱۸ دی‌ماه در شهر قدس بازداشت شد و پیکر او حدود ۶۰ روز بعد به خانواده‌اش تحویل داده شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78334" target="_blank">📅 17:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78333">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/957af9390d.mp4?token=MXcQF3ntznIM-RWeg5XwEzazvumN1aKjWsMcI9bPK0S2KLqzf3ohEoZ8JaoZ51xJNjrJVPJGukvjqWKXL2H2rSGZfqZDx4RS_4ue0Esj6F9UJDveoETxZxihdGB3SWQNoavnnn6k1GByrh42h2DbZu8lRwreJyH9ZOHp0b9GmdJaclUrXkkHLAZiV1agzuWtlgLhh7isY16kUHpk5rHMA8E2UNmPEiFywqO1IokLI3kvUklxMrPIa2eNuKOGVFhrPPF6EK7iE6JQm8RFPOaYj8va8THU6gzymalbm4V_TzPVM9WVHPcDlquiJEN8pRa6VxBGGtp11dyGMm1UDzA9Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/957af9390d.mp4?token=MXcQF3ntznIM-RWeg5XwEzazvumN1aKjWsMcI9bPK0S2KLqzf3ohEoZ8JaoZ51xJNjrJVPJGukvjqWKXL2H2rSGZfqZDx4RS_4ue0Esj6F9UJDveoETxZxihdGB3SWQNoavnnn6k1GByrh42h2DbZu8lRwreJyH9ZOHp0b9GmdJaclUrXkkHLAZiV1agzuWtlgLhh7isY16kUHpk5rHMA8E2UNmPEiFywqO1IokLI3kvUklxMrPIa2eNuKOGVFhrPPF6EK7iE6JQm8RFPOaYj8va8THU6gzymalbm4V_TzPVM9WVHPcDlquiJEN8pRa6VxBGGtp11dyGMm1UDzA9Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: تسلیحات کشف‌شده در علی الطاهر را ایران برای حزب‌الله فرستاده بود
نخست‌وزیر اسرائیل روز جمعه ۲۰ شهریور اعلام کرد نیروهای اسرائیلی در جریان عملیات در ارتفاعات علی الطاهر در جنوب لبنان، مقادیر زیادی تسلیحات را از زیرساخت‌های حزب‌الله خارج کرده‌اند.
بنیامین نتانیاهو با اشاره به تسلیحات کشف‌شده گفت: «مقادیر بسیار زیادی سلاح از آنجا خارج کردیم که سال‌ها توسط ایران سازماندهی و تامین مالی شده بود.»
ارتش اسرائیل پیشتر با انتشار ویدیویی اعلام کرده بود، نیروهایش پس از به دست گرفتن کنترل عملیاتی ارتفاعات علی الطاهر، زیرساخت‌های زیرزمینی و روی زمین را منهدم کرده‌اند. به گفته ارتش اسرائیل، این شبکه بیش از دو کیلومتر امتداد داشت و شامل ده‌ها راکت، موشک و پهپاد و همچنین موشک‌های ضدتانک، مین و مواد منفجره بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78333" target="_blank">📅 17:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78332">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ae2ehLk0YXl47tOUwtAUl64u0YzYA6gwdBmWOuOEmGE-9NcPPa8FirZYDuBfOCMJ0nkGxANXcGF_BhCLUntL60XJMNTW-KCNIcMmHAS6adulujxeZJ6eFNg7LsAJa-IMlDnf6nDzGAHY3SssvaPWpdkqbWoLRLlb9D06hrZCqj0pnK8ua70DiSnxurt5580EQ_0vh1OK_0FGEH0BS9_x34rR8GBO_ufoV5fr0vYcdutTiqJH_gHNSoflzpHFIKe-Pbd6e4pl-F7UgnjUWKBBPP4UXVphNr0TFVD2iw6pMCsxR_dZtKaIkHlSwFSgncn21hFOoy-YH_UlREhDtqnhmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، گزارش‌های رسانه‌ای مبنی بر آسیب‌دیدن هواپیماهای آمریکایی در جریان حملات موشکی اخیر جمهوری اسلامی به اردن را رد کرد.
او پنج‌شنبه ۱۹ شهریور در مصاحبه با شبکه نیوزنیشن، در پاسخ به سؤالی درباره این گزارش‌ها، گفت: «نه. هیچ خسارتی وارد نشده است. هیچ اتفاقی نیفتاده است.»
کمی قبل از اظهارات ترامپ، شبکه خبری فاکس به نقل از یک مقام ارشد آمریکایی نوشته بود که موشک‌های بالستیک ایرانی در جریان حمله گسترده موشکی سه‌شنبه، ۱۷ شهریور، به هواپیماهای جنگی آمریکا مستقر در اردن، آسیب زده‌اند.
فاکس‌نیوز این خبر را به گزارش جنیفر گریفین، خبرنگار ارشد خود منتشر کرده است.
شبکۀ خبری سی‌بی‌اِس برای نخستین‌بار این موضوع را منتشر کرده بود که در جریان حملات موشکی ایران به پایگاه نیروهای آمریکایی در اردن، «چندین هواپیمای نظامی ایالات متحده، آسیب دیده‌اند».
ارتش اردن روز چهارشنبه ۱۸ شهریورماه با صدور بیانیه‌ای گفته بود که ایران در طول شب قبل، ۲۰ موشک بالستیک به سمت اردن شلیک کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78332" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78331">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sIUy6lxhEzAgROnNfGb6SFp8nX7-EeykZ4q0xm16_fyu8cMXhhQ-inx5OB6gncTOVZ6usxRW6qT4a8l1Di9QWaw52mF7wYU9C7o8O7CCZr4et8z3dBvrQrApn1ktQFodusw_OYZ0zAaf8X_0G_yGoYQHV9D5xai8iJRKc4VZRBjBk7oUFeASTXmDHa5IUaDE6eS4jHgUYwivQtMUlAl_ZptcQIE9itKLtH5ts8w1oUgvc4HFlpFaBtpuryhRiHCVqPlTx9AJqtO3vAIFIV9JnWwOH0DSs9Os8yqti3EHaJnOwo7UAbfhmHb0rTd8hsRwg8p_BCODi3PpfR3YCnm4Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت آمریکایی «آنتروپیک» اعلام کرده است که سه عملیات مرتبط با حکومت ایران را شناسایی و مختل کرده که در آن‌ها از مدل هوش مصنوعی «کلود» برای تولید و انتشار محتوای تبلیغاتی، طراحی سامانه‌های نظارتی و تهیه اطلاعات مرتبط با هدف‌گیری نیروهای دریایی آمریکا استفاده شده است.
این شرکت روز پنج‌شنبه ۱۹ شهریور در تازه‌ترین گزارش اطلاعات تهدید خود، مجموعه‌ای از موارد سوءاستفاده از مدل‌های هوش مصنوعی آنتروپیک را تشریح کرد. این گزارش فعالیت‌های شناسایی‌شده و مختل‌شده از دسامبر ۲۰۲۵ تا اوت ۲۰۲۶ را پوشش می‌دهد و علاوه بر ایران، مواردی مرتبط با چین، روسیه و کشورهای دیگر را نیز بررسی کرده است.
بر اساس این گزارش، آنتروپیک حساب‌هایی را شناسایی و مسدود کرده که از «کلود» برای اجرای عملیات نفوذ با هدف تاثیرگذاری بر افکار عمومی استفاده می‌کردند. سه مورد از این عملیات به عوامل همسو با حکومت جمهوری اسلامی مرتبط بوده است.
آنتروپیک می‌گوید هر یک از این عملیات از سوی فرد یا مجموعه‌ای انجام شده که یا مستقیما در یک نهاد تبلیغاتی حکومتی ایران فعالیت داشته یا به نمایندگی از چنین نهادی کار می‌کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/78331" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78330">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5B0RnKDfxgWhDqSoJqaoNMzDVVbA5aK31xZjtya7OfNFLHcFA5lhqo6AFB1tbknJcQfvR1drm4nN9FXz6LtZffqwpGUhckbfwfKILZDrMt_py9tdWkfCG55hXZX6qWZf6gyN8e_eLcjLccdH0V8dIUbCGo-djMISpSO5JShDd8zXSgWCE5sOg1VbFdD2wH5ohZTnb8iyd2TeQxbXsXYbU9ZJX19HQfhbY3w4jzt1trvJCduuC2IM0aMG0pDE8lNt4j99pjzFMIbSKmA2SrdRyvfzlATsIrBf4NzV6Q1qx9nMRrleJyyEAJHLFpNvnGCbMps0i3Afmq1-owSRNqDUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت مخابرات ایران با انتشار اطلاعیه‌ای در سامانه کدال (سامانه اطلاعات جامع شرکت‌های پذیرفته شده فهرست شده در بورس) اعلام کرد هزینه مکالمه تلفن ثابت با تلفن‌های همراه از روز جمعه ۲۰ شهریور ۴۵ درصد افزایش می‌یابد.
به گزارش انتخاب، بر اساس این اطلاعیه، سقف هزینه مکالمه تلفن ثابت با تلفن همراه از ۶۲۵ ریال به ۹۰۶ ریال افزایش یافته است. این تغییر در پی ابلاغ دستورالعمل افزایش هزینه تماس تلفن ثابت با تلفن همراه، تماس میان تلفن‌های همراه و پیامک اعمال می‌شود.
شرکت مخابرات ایران اعلام کرد میزان دقیق تاثیر این افزایش بر درآمد شرکت هنوز مشخص نیست و آثار مالی آن در گزارش‌های دوره‌ای منتشر خواهد شد.
این شرکت در خردادماه نیز هزینه ثابت ماهانه تلفن ثابت را ۴۵ درصد افزایش داده بود. هزینه ثابت ماهانه مشترکان خانگی در تهران و کلان‌شهرها به ۴۳ هزار و ۵۰۰ تومان، در مراکز استان‌ها به ۳۲ هزار و ۶۲۵ تومان و در سایر شهرها به ۲۴ هزار و ۶۵۰ تومان رسیده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/78330" target="_blank">📅 17:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78329">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb8399ab74.mp4?token=VZK9kbMNm2zPsYOAr6wTEa85aroLpyG7ToCZJ78JYsZI4c5yuSgNNMDUa5qtuduM8IjnN2d8mb5FCTVXvhd2ptszcIVBCt6rQDGqhFehFTMk_x57dJ5t180-whf5MnZy-7AB0brhC3QFb75a-wRv5Pd7cbRpquctuXQfFNw2YcY9IM2EdLpL5QEm4NladrGYv-ji2nt7MOi9mO4N_suYhzHB89iLIul_BpffrR4vU2lciRMr5X5UNqfeY_rnz2bxjC8A_dNaeOcEHyRuo2ik4MWeW5fNBo6BJzNFMIYOaNN_AqYRWxKwL4n_ydAqSiqVdxEZj2oU9RlvqU-0rqoU6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb8399ab74.mp4?token=VZK9kbMNm2zPsYOAr6wTEa85aroLpyG7ToCZJ78JYsZI4c5yuSgNNMDUa5qtuduM8IjnN2d8mb5FCTVXvhd2ptszcIVBCt6rQDGqhFehFTMk_x57dJ5t180-whf5MnZy-7AB0brhC3QFb75a-wRv5Pd7cbRpquctuXQfFNw2YcY9IM2EdLpL5QEm4NladrGYv-ji2nt7MOi9mO4N_suYhzHB89iLIul_BpffrR4vU2lciRMr5X5UNqfeY_rnz2bxjC8A_dNaeOcEHyRuo2ik4MWeW5fNBo6BJzNFMIYOaNN_AqYRWxKwL4n_ydAqSiqVdxEZj2oU9RlvqU-0rqoU6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی زارعی دوز دره سی، زندانی سیاسی و یکی از آسیب دیدگان اعتراضات سراسری ۱۴۰۱ که در زندان قزلحصار کرج محبوس است، توسط شعبه ۲۳ دادگاه انقلاب تهران از بابت اتهام «افساد فی‌الارض» به اعدام محکوم شده است.  بر اساس اطلاعات دریافتی هرانا، حکم اعدام آقای زارعی دوزدره‌سی…</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78329" target="_blank">📅 17:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78328">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/78328" target="_blank">📅 07:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78327">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okBWXGEPyTG0LlQwfyrrJNovSdIG5dQzzMBhx_W0HEkJHK2sOLvUtXGzpInmkKJKRVABddfGqlhQGt6DafVK1GV_z5ESQMKx01PbQmVAmCpX5PVRffVWZfuriNhOYP00LzqZ5JgwBvVOY4UgIfMzfQXS_yLrUhO17phKO6XIrpq6SuoEHJa1Z8Ex7hvLRxtpf_cUR-rdObxVBxd1B-ZKNZvs1QacygvY2MF0T3TUkLSR1_mlzst2G7T9luTH82XVZrn6HDPmCUfw3HQ85r6we8Ut0RDb-O-gHZCQDZmq6IlpdfNEHwTRI8CFDattgO_41vJlzYFmPRC1etzzzPPpLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا در دومین شب گردهمایی انتخاباتی میان‌دوره‌ای جمهوری‌خواهان که در دالاس در حال برگزاری است، بار دیگر، تنگه هرمز را «تنگه ترامپ» خواند و گفت «ما تنگه ترامپ را کنترل می‌کنیم». رئیس‌جمهوری آمریکا بار دیگر تاکید کرد که هرگز نمی‌توانیم به ایران اجازه دهیم سلاح هسته ای داشته باشد و نخواهد داشت. او گفت که ایران در حال عقب‌نشینی از همه جا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78327" target="_blank">📅 07:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78326">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8pZ5c4fpPj_ooI0xL2jDCmNdqQwH_KAbJfaV3OUqCRIgmv2Xkm9fdut1akYAv8QnpPVbp-shDh31GE6kYGr_7rEJnURiq1VX-kDHryUzH-LsdGwW5DAo_VxRvo28JDABTP7Sr7qOL0v_IXTNTmM_oOtTmEeysVm8Wa9r--ZhRIm2iIMFC8M-dAz7BeJySZ34cRrJISSeffbrnqjrnCJHu7u12fVAcLkA8HuroRcYUOD-TQtWPStOvtuTN4Flg7yqZiD6Xwa5v6McOD6jZFyN8AnjOJbyZfLrnWHJPLYXM4zec9V53O9_-WDbm30WPyuTl8EE60jqc9_c5fKgK5LFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هانگ کائو، سرپرست وزارت نیروی دریایی آمریکا، به اپک تایمز گفت نیروهای جمهوری اسلامی خسارت گسترده‌ای به پایگاه پشتیبانی نیروی دریایی آمریکا در بحرین، محل استقرار ناوگان پنجم این کشور، وارد کرده‌اند.
کائو در توضیح استقرار اخیر ناو هواپیمابر یواس‌اس آبراهام لینکلن و الزامات لجستیکی عملیات طولانی‌مدت گفت خسارت واردشده به پایگاه بحرین بر امکان پشتیبانی از این ناو تاثیر گذاشته است.
او گفت: «خدمه این ناو جایی برای پهلو گرفتن نداشتند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78326" target="_blank">📅 07:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78325">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neXoBEHvzQUhYinB1ozithcpI0Rk7p4nmaA6jrW8AUOvGhBrlv94NqbqSNQa7an0-prtFFSdyyzVUzEcYhS1Gfzeya_1kCCymifl2rQvPp3QZPaVTxf9Xoo84Oh6DF_hNGefyNmE-8T05XIvdhuErnCxIHGIgxBlsS6RidjlcGkPwTp2iJ4N6el6l036E7HGR0ycpXEs4zvJZq8rNpbAs_jU1Nkl0f9-uWtBr3KY0krq231UW2FlT7R9ED0DXRdbwVgrqy4SC0CCcqoyXIn5UA2YE54o7JE1GUp1Khj8LPjTvUoWfBBG8l1Kpc48eKz3cj2jrjSN-0JCvM0Ugp4ZiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت پنج‌شنبه ۱۹ شهریور هم‌زمان با تشدید درگیری‌ها در منطقه و افزایش نگرانی‌ها درباره اختلال در عرضه انرژی، بیش از شش درصد جهش کرد و نفت برنت به ۱۰۷ دلار و ۶۳ سنت در هر بشکه رسید. نفت خام وست تگزاس اینترمدیت نیز از مرز ۱۰۰ دلار عبور کرد.
بر اساس داده‌های اویل‌پرایس، قیمت نفت موربان با بیش از پنج درصد افزایش به ۱۲۲ دلار و ۴۸ سنت رسید و سبد نفتی اوپک نیز با بیش از چهار درصد افزایش، ۱۱۲ دلار و ۲۵ سنت قیمت‌گذاری شد.
افزایش قیمت‌ها پس از حملات به نفتکش‌ها در خلیج فارس و دریای عمان و پیشروی حوثی‌ها در سواحل دریای سرخ رخ داد. رویترز گزارش داد تصرف بندر مخا و پیشروی حوثی‌ها به سوی جزایر حنیش، نگرانی‌ها درباره امنیت تنگه باب‌المندب و مسیر صادرات نفت عربستان سعودی را افزایش داده است.
هم‌زمان، تردد کشتی‌ها از تنگه هرمز به‌شدت کاهش یافته و داده‌های اولیه نشان می‌دهد ۱۸ شهریور تنها هفت کشتی از این آبراه عبور کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78325" target="_blank">📅 03:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78324">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/09d9c8c443.mp4?token=JHYS6GdaDSMXZQ0mvnvSzVnj27T0eZDkL9Z96UnFwqN0aTI1xBxuO0JLNOaaU_IXjrv_fDkdc1r3HtgWZvxyAzPAMaUDQyAi2xtMz0g8JGuSSXAeu3AlHII29TU2RvGecXi6RVkfGQFdS5XTgxHvCr4P2Q7kFddAlG06gPIZk9XKzkjHGwLaUYMo5et1ht687NNOcyZf1K9GP_3cXt8GCTQm4C49_wlL8eU8lTUpHuse_Vb2XP1-NJwK2GFlz13DXQzJUjQWrKpfnb0nzH1oE4TL5j7z2fvZA6F2tCPjOob53_RsdpVFa-oJW2_aVlzuCEx-LpVU5XEiwC48tSYy5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/09d9c8c443.mp4?token=JHYS6GdaDSMXZQ0mvnvSzVnj27T0eZDkL9Z96UnFwqN0aTI1xBxuO0JLNOaaU_IXjrv_fDkdc1r3HtgWZvxyAzPAMaUDQyAi2xtMz0g8JGuSSXAeu3AlHII29TU2RvGecXi6RVkfGQFdS5XTgxHvCr4P2Q7kFddAlG06gPIZk9XKzkjHGwLaUYMo5et1ht687NNOcyZf1K9GP_3cXt8GCTQm4C49_wlL8eU8lTUpHuse_Vb2XP1-NJwK2GFlz13DXQzJUjQWrKpfnb0nzH1oE4TL5j7z2fvZA6F2tCPjOob53_RsdpVFa-oJW2_aVlzuCEx-LpVU5XEiwC48tSYy5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتشار ویدیویی در شبکه اجتماعی ایکس نوشت
:
امشب بزرگ‌ترین پایگاه ایران در خارج از ایران، یعنی تونل‌های علی‌الطاهر در لبنان را نابود کردیم. در حال تکمیل مأموریت هستیم. سال نو مبارک!
پیش‌تر ارتش اسرائیل اعلام کرد شبکه تونلی حزب‌الله در ارتفاعات علی‌الطاهر را با استفاده از بیش از هزار و ۱۰۰ تن مواد منفجره تخریب کرده است.
به گفته ارتش، در این تونل‌ها که طول آن‌ها بیش از دو کیلومتر اعلام شده، ده‌ها موشک، راکت، پهپاد، سلاح‌های سبک، موشک‌های ضدزره، صدها مین و مقادیر زیادی مواد منفجره کشف شده است.
بر اساس اعلام ارتش اسرائیل، با انهدام این سایت، عملیات تخریب شبکه‌ای متشکل از هشت تونل به طول مجموع ۵٫۴ کیلومتر در منطقه علی‌الطاهر و قلعه شقیف تکمیل شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78324" target="_blank">📅 01:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78323">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GzTmKcb75vxza_dSWbP6lYhM1m12M14B3WKZhkXGjcCUh0Fzw9pbbBmgh2dpGVi6zqxIagNtd-iqt5i-X_G8X7BjTj200lBSP__3_sOu3wP_dPWJZMN4SbXyvmVwjzDK6q9sz8Tt5iP6pu3V2BVN523Ph01aVb8ELRxi37pp8_JC17fzyPLxZUkB1XByUbZknlBERSis4yZzDSzNF58CyU9Wy9DnjsFR43Sme4N8mEBqJ4PJVy8LpiNql47bAGE2s_czSvstJexyP8LakPA-n3HBY9_tnXjr_kt4c_fdF8SF1tE0EdTg_UAZSsMeHQMrGsny3iaA-tlyGSwb_dLlLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا، یوکی‌ام‌تی‌او، عصر پنج‌شنبه به وقت واشنگتن از برخورد چند «پرتابه» به دو شناور در نزدیکی سواحل عمان خبر داد.
بر اساس این گزارش، این برخوردها در فاصله چهار مایل دریایی غرب شهر خصب، در استان مسندم عمان، روی داده است.
طبق این گزارش، کاپیتان یک شناور اعلام کرد که شاهد آن بود که چهار پرتابه نامشخص به دو شناور نامشخص اصابت کردند.
در پی این اصابت‌ها، یکی از شناورها دچار آتش‌سوزی شد و از وضعیت شناور دوم اطلاعی در دست نیست.
مقامات عمانی در حال بررسی این واقعه هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78323" target="_blank">📅 01:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78322">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c378ed4e1d.mp4?token=a96BkqcTZcbjoMWJd5z59Jub-7qOuI4pOQKk47UiB4q8WqM-mJLOkM2LpgishXDClnuK9GFKhI4xojXGlYI-TB7C5vhuCv25_LZ6FFnQ8M3jlw3qB1jApwBx3xZtvJfwpdEl1WssCJKXzaxGUrnPvLPQhW3Jbfq6dsZI76TwvSKQ1B8vwoa6ZOFYi2XvdzMq77h7yi86VZNVJBpv6iVJeLfX_iqc8uDaIsKR39ms_eAcj2ezwiw72HyIWAAiUo-SoNuBGx_FGISS7D06GqB_QPgDZ0QM78fQOZtIIJy-ixixMkYAQn8sacSC5sfdCF1nPcbd_ODmNcvNe_wLPIFoaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c378ed4e1d.mp4?token=a96BkqcTZcbjoMWJd5z59Jub-7qOuI4pOQKk47UiB4q8WqM-mJLOkM2LpgishXDClnuK9GFKhI4xojXGlYI-TB7C5vhuCv25_LZ6FFnQ8M3jlw3qB1jApwBx3xZtvJfwpdEl1WssCJKXzaxGUrnPvLPQhW3Jbfq6dsZI76TwvSKQ1B8vwoa6ZOFYi2XvdzMq77h7yi86VZNVJBpv6iVJeLfX_iqc8uDaIsKR39ms_eAcj2ezwiw72HyIWAAiUo-SoNuBGx_FGISS7D06GqB_QPgDZ0QM78fQOZtIIJy-ixixMkYAQn8sacSC5sfdCF1nPcbd_ODmNcvNe_wLPIFoaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران روز پنجشنبه ۱۹ شهریورماه تصاویری منتشر کرد که به گفته این نیرو، هدف قرار دادن یک شناور بدون‌سرنشین آمریکایی در ورودی تنگه هرمز را نشان می‌دهد. سپاه اعلام کرد این شناور با شماره بدنه ۵۸۳۸ و از نوع «سیل‌درون» بوده است.
علی عظمایی، فرمانده نیروی دریایی سپاه پاسداران، گفت این شناور بدون‌سرنشین «جاسوسی» متعلق به ارتش آمریکا در تنگه هرمز مورد اصابت قرار گرفته است. او همچنین گفت: «تنگه هرمز مسدود و تحت اشراف اطلاعاتی و کنترل هوشمند ماست و هرگونه تحرک خصمانه مورد هدف قرار می‌گیرد.»
نیروی دریایی سپاه در بیانیه‌ای اعلام کرد ارتش آمریکا طی روزهای گذشته شناورهای بدون‌سرنشین خود را به تنگه هرمز اعزام کرده است. مقام‌های آمریکایی تاکنون درباره این گزارش اظهارنظری نکرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78322" target="_blank">📅 22:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78321">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tf2HYyDCKsC3FsyazpRUDXmgUr1SejksFw7W20-uD4xDdJ8oKwHsiKS3d4oC7pxddk8kA50ahz6Qv3ePKb48iHu5V70z9vGrxEMlwKKnWki5ofjCrthpJqxaOU5vmEKtx2O73BnRIzM_X3pWy1TiWXhbmn7qdP2PAm6-kSephzYJ8uygcp5IJFG4nS86Bq7vZrdhDna0jN03P3pCsftk0g5B-Dk01MNq4vcuTmoVfA-ll8p39jkxaCrXmSllDb-6MeO4v5NiPMYaVYj9toWcfXDOkcPHeUTc414u_PeeK7lX4jlfCC_Vva4scPKQdUBjVuf9SMQCADaBSS7qzHVOzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، روز پنجشنبه ۱۹ شهریور در گفتگو با بلومبرگ اعلام کرد این سازمان بر اساس تصاویر ماهواره‌ای، شاهد تحرکات ساخت‌وساز در سایت بسیار مستحکم «کوه کلنگ‌گزلا» (Pickaxe Mountain) در جنوب مجتمع اصلی غنی‌سازی ایران بوده است.
گروسی با اشاره به اینکه بازرسان آژانس هنوز موفق به بازرسی از داخل این تونل‌های عمیق نشده‌اند، گفت: «نشانه زنده از تحرکات در اطراف این سایت ساخت‌وساز وجود دارد، اما اطلاعات دقیقی از فعالیت‌های درون آن در دست نیست.» او یادآور شد که ایران پیش‌تر قصد خود را برای انتقال تجهیزات به زیر کوه جهت «مصون‌سازی در برابر حملات» اعلام کرده بود.
این اظهارات در پی ارجاع پرونده هسته‌ای ایران به شورای امنیت سازمان ملل مطرح می‌شود. بر اساس گزارش‌ها، آژانس از ژوئن ۲۰۲۵ و پس از حملات نظامی آمریکا و اسرائیل به تاسیسات هسته‌ای ایران، امکان راستی‌آزمایی وضعیت ذخایر اورانیوم با غنای بالا را نداشته است.
دونالد ترامپ، رئیس‌جمهوری آمریکا، بار دیگر با اشاره به این سایت زیرزمینی، نسبت به هرگونه اقدام ایران هشدار داد و در یک تجمع انتخاباتی گفت: «ما متوجه فعالیت‌های مختصری در کوه کلنگ شده‌ایم. به ایران توصیه می‌کنم دست از پا خطا نکند، چرا که مجبور خواهیم شد ضربه بسیار سختی به آن‌ها وارد کنیم.»
از سوی دیگر، سی‌ان‌ان روز گذشته به نقل از منابع خود گزارش داد که ایالات متحده در حال توسعه سلاحی با نفوذ بیشتر با قابلیت تخریب اهدافی در زمین‌های سخت مانند کوه کلنگ‌گزلا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78321" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78320">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCYA3EofFg6rYNBV_v7X4k45vta0xS7T-TuJpwCncqBEx8f4CCHnGRf5kj55s4a86bxjkdeWXYXILCVq4SnUdcD-xSZtIz6C7rKPDyjxMXIdO--haiJPZVlYccTsn91TInd8TCVpyhf8m-WewWac8lCdnvGkR7EuBDgVoqhDoPTRH6j9jzIoLBz6QenLM8GjFwIslHLjBAaovxyUKrIe-kNgsHmS8hvp7nmAW2--UrK68nkNpn_VMsObbUOBFFRPw1YzPMVBhMqx_aeHyZlwDQZaqV4V_LF_YHg_m4T5g2PjjGUkzOX-hPBMS8iy0YTNpTU4L6s-kD-x4Vh6bv98SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه قبل ماموران امنیتی به منزل خانواده «کیاوش میرقاسمی» از کشته‌شدگان اعتراضات دی‌ماه۱۴۰۴ یورش برده و «سمانه عصاران» مادر او را بازداشت کردند.
به‌‌دنبال تشدید فشارها بر خانواده میرقاسمی حالا صفحه اینستاگرامی مادر او از دسترس خارج و کنترل آن به اجبار به دست نهادهای امنیتی افتاده است.
تمامی پست‌های پیشین این صفحه حذف شده و تنها یک پست به دستور مقامات قضایی در این صفحه قرار دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/78320" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78319">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LA5Qvjr1BV1Mzw_gkg9l2MRyBUF2kzyJ5eu-AOWn3PD2U_eMrFUT_1eBIfHtqXcF1tpL-_Z5-bLJi4MQvvyfYPeDvbsqaxI0yX09Eiwvpi2Mzm6PJjFeQgTEXR1Z1A7V6uXEZ9eTnQdaJg6kT2x1VWy8TdidKcNxHAIztesq0nUlHqfnKRRPA5F32KLeuCYQJ9j-R2hEkq4YMJBbjprJboO6it4nM-iRto1pqzTjHMfcuTimAKtjb6pd6TbkHAWZnBRfdBney-rCaNcHA0rDbEOgEnH49O0kvaH-vavQBth4uJR5A-GA1VJi4IC80DnGYwPLAwSjzG4aB6L-Ec-btg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس بریتانیا دو نفر را به ظن ارتکاب جرائم مرتبط با ایران و نقض قانون امنیت ملی بریتانیا بازداشت کرد.
این دو فرد در لندن پایتخت بریتانیا و در جریان تحقیقات مربوط به فعالیت‌های مرتبط با ایران بازداشت شده‌اند.
پلیس متروپولیتن لندن با صدور بیانیه‌ای تأکید کرد که این تحقیقات، با هیچ‌یک از حوادث ماه‌های اخیر که در اماکن و ساختمان‌های مربوط به یهودیان و جامعۀ ایرانیان مقیم بریتانیا رخ داده بود، ارتباطی ندارد.
هنوز جزئیات بیشتری از هویت افراد بازداشتی یا ماهیت اتهام‌های منسوب به آنها منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78319" target="_blank">📅 18:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78317">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P17gpFpfg5LpIbo1BIrpbz6dhZkhhV_yQxW1JkSjvO7jYI2Orod1AWXZ2ZlnKzeZK4UTD7vvpz14epTaKfOa7jubs4rc_GdlhtV_v6Ov6ppOqsRfKXB61CyqephPrIDptKqt3V8OLbDYKQvHGn4vPtaC0l6JuNEczzmcKg1QF5oAah2Rcy10vjwcmkLAnuNTemagS-cQT-Mxa7Wfi2A7Bm045p_6FAmVAydGqu617hD_pXvkvuSSCWpmEh9bNS5Ag2CUQ2TS56CZGuV2Gb7rGpuprFZnTUg-aRRRMdW4VJp1_YFBqHs78kYhz6iGac7FRuGXXNMuRhNU6SID4Y5zBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TAkpPi0hoqHAgTR6oWgqCbo_eJXnnnVMPbIR95pBEYz-hUHKl8Qp3wL_XJGBXlQ7mtkAU4U9aoXPJkaJOZ0uFOnc7f2hzVQDB_t37_VIiUA6Rw838yY0noaERu5Zj19Cj3VEyZD2Dw3urAEVlHUBT6W3pxy_Wk9aJjlxu0PtuRLET2U4fUDt4NO2zeczNutHSzb8R6ZxU-Z4uaXQ2W56buh2E87qbrGuRrh8Jtuy-um7u4FLoXR2iyFmDF2Oxico2TfJYdcJ-lmuvMXxzCjzNfYbk3sfl7OXTZ2AzmVtrQxG1pNj2NIyzsU3HJq9UHLJZ0uZeZWg1qdLfzF3ctI7yg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اکانتش در توییتر:
MaryamAzimih
مریم عظیمی، مهندس ایرانی اپل، که پیش‌تر از بازداشت و انتقال خود با چشم‌بند در خودروی نیروهای اطلاعاتی جمهوری اسلامی در مشهد و تصور مرگ قریب‌الوقوع نوشته بود، در مراسم جهانی رونمایی اپل، یکی از فناوری‌های جدید دوربین آیفون ۱۸ پرو و پرومکس را معرفی کرد.
عظیمی در ویدیوی از پیش ضبط‌شده اپل به‌عنوان مهندس کیفیت تصویر معرفی شد.
او در بخش مربوط به دوربین آیفون ۱۸ پرو، قابلیتی به نام «تصویر مرجع اپل» را ارائه کرد.
اپل دوربین این مدل را پیشرفته‌ترین دوربین خود تا امروز توصیف کرده است.
حضور عظیمی از دو جهت در میان ایرانیان مورد توجه قرار گرفت: نقش او در توسعه فناوری تصویربرداری در یکی از بزرگ‌ترین شرکت‌های جهان و مخالفت علنی‌اش با جمهوری اسلامی، از جمله روایت شخصی او از دوران بازداشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78317" target="_blank">📅 17:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78315">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FcW9QHsW8fCDdf3jACMz9p-FRpS3rDqUNXXf--o0nLiHMJLqLPbNAx9PgC7ENLSxzo3SsX5avKkZXaWkLUFZ5zW1s-q3cbhaXq2RcBljTKxQTypyfaBXxPkKCz9VlEG5ktYH1_nqyqVdMIR-_IQmusA0PviVtcO5h6wwreIjH8C3_5Dohqb7yU6lFu09pS7ZUI7k3VrKBFux_nPQlZglyxQd1T0esgYGjE-Wna8PvTyAaT2dCo-k0up07MTelP4jzjFZu9tZF1HQ9cw0YaA11xrmS0bHSKV15uVwxZiHGSnn0RooswpBgnpcRrFdA9lYBIeFUWK1hifiQ5eeDUuquw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cJbNQOxfTXVUla8mu7A0giOFNIvo5sCZnSH1dyC7zcZAVJDX6U7Q51Uk4-B29_FcZD7oTzskaB_IFCk7H9EqtdfuvfsLRtOKuJ79eGUSpJkzvgYT9gNsU-13ELlpFWOmOlExStj22KJ1Vl9LTstaKChWnLoAG8MoCZAKjpx-3f3a9RUJQu6-0AtckyecwTFuXGSVjNjm4X6mj-ci4Az4Cf2h2kinuAdhQptiNXNbRiS0hnwvE7i7lOkUWhHOkpfTOzQFN02c8ctSTbcT8b5psnUhLUIu97PnWUC5pWsJqarBoTQc_a01wNDJ-klhikz0JqG_byPf-KstaMkRzDn52A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78315" target="_blank">📅 16:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78314">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GkTRTt1dPIfcGMzMt_qIK4he6D5FdphPnoqN6oc8kR17g2sg9iBbYcUu9C6Cd8BWOpWpWvA3XJrG1vZ6CNMVPahmK8MieSIQs-mpcwW9f_eICVCULtv-uSPeMPwW_1FvNOAIfao5Bpl_rKQ-uxi9ouh6lW3sd5PHVaM2gamwu0eKARvGeCb-6bsh1Xv8kdPYUnjPljmuBzDJ5QivfRAnr6PFZ5bYekIj_lXEGNXoARcx2RJN_FSJ7QXjvaJCfOYjdTWGRGKhOtj_B9Mb564Z4gcavyjzxtpJxk6ik64CTapWn-UM4FaB_aX5n_buzAAjIRaRh3m3RUfHg6CmbZOJnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند افزایش روزانه قیمت ارز در بازار تهران روز پنجشنبه ۱۹ شهریور (۱۰ سپتامبر) ادامه یافت و بهای دلار به ۲۳۵ هزار و ۷۰۰ تومان رسید.
dw_persian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/78314" target="_blank">📅 16:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78313">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctG5Dc0GVhBz_tZAWbVsXrG1pzicZ5dywKoKQJ2dlE3e83Pdbu-KXiHcMEkHd1EHpGb2cw99NT0cnQozh2xdMPJoIigmla6ORK3ZhJ83Q-UvsZ8XKBTmoJCSxe14e8MfGo7tp5giIDGYrkeHx1zVozcAgOqh0qjZ9I84r473RmyB7evblztBgQhdu47Akr1pHzmJ82xXldPeTtbNn49jWeJDxwDrbDZCLo8oCM3HbZ8beAtS7DyNgpX756bJyyxYqIJSU2sHHnYpZsrQi5th0WtJkirvDBR4IAXbrPd-vO_bCZyzqxH59aNWUgnQxAcia5lIMi542CpTyvxcReYCUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی افزایش تنش‌ها در خاورمیانه، قیمت نفت شاخص برنت روز پنج‌شنبه از ۱۰۲ دلار عبور کرد که نسبت به روز گذشته حدود یک درصد و نسبت به ابتدای ماه حدود ۸ درصد رشد نشان می‌دهد.
طبق برآورد اداره اطلاعات انرژی آمریکا، ماه گذشته تولید روزانه نفت ایران به خاطر اعمال مجدد محاصره دریایی آمریکا ۸۰۰ هزار بشکه نسبت به ماه ژوئیه افت کرده، اما هم‌زمان تشدید حملات جمهوری اسلامی به کشتی‌ها در تنگه هرمز و آغاز حملات حوثی‌ها در دریای سرخ و باب‌المندب به نفتکش‌های عربستان نیز باعث شده متوسط تولید روزانه نفت کشورهای عرب منطقه در ماه گذشته ۹۴۰ هزار بشکه نسبت به ماه ژوئیه کاهش یابد.
مجموع تولید نفت ایران و کشورهای عرب منطقه در ماه گذشته ۶.۷ میلیون بشکه کمتر از دوران پیش از جنگ خاورمیانه بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/78313" target="_blank">📅 16:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78312">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZxeVhN_01GUef5IKhJxknlu7EIUA6mz-eqO8BEAbfbL9pSRXjLxiMHFYlJw4BFAAKOUE0r9V32ST0eNPD_lplHUEYWErt_3ksB_OxYfoOsxIvkrVc1CudHG3PU3qua5CMWEH0QqjBTpu_P4dOPTP8cdD8I-IptLsF-fFZf58N2jEBVvggYRSd-g22_18F0eyVjA-oHioMr4lZ2Jxq67BCq1Sf0JMKe-oBfEh1_5IrocBiO3cWoi-qf3gX2AhPm0qbpkgsrmJiH-sJjzZt9eU8EgWtf4tJOTcqFJENQ44US9w3hLoEL60V0FVDIh39YEuBecton42IomVsqglrV9Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع ارشد ایرانی و سه فرد مطلع می‌گوید حکومت ایران با استفاده از سازوکاری شبیه تهاتر و با دور زدن تحریم‌ها، در حال وارد کردن میلیاردها دلار کالا از جمله تجهیزات نظامی از چین است.
در این گزارش که روز پنجشنبه ۱۹ شهریور منتشر شد، منابعی که نام‌شان اعلام نشده گفته‌اند بر اساس این سازوکار تجاری مخفی، نفت ایران در ازای اعتبار برای واردات از چین در سال‌های اخیر، یک شریان حیاتی مالی برای تهران همزمان با افزایش فشارهای اقتصادی و نظامی ایالات متحده فراهم کرده است.
آن‌ها گفته‌اند که این سازوکار همچنین به چین، بزرگ‌ترین واردکنندهٔ نفت خام جهان، کمک کرده است تا به نفت تخفیف‌دار ایران دسترسی داشته باشد.
به نوشتهٔ رویترز و به نقل از منابع طرف گفت‌وگو با آن، ایران از این سازوکار برای خرید دارو، وسایل نقلیه و تجهیزات ارتباطی از چین نیز استفاده کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/78312" target="_blank">📅 16:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78311">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b2c630a3b3.mp4?token=hmaFJc_gtoLcekWqWIxeAIxUW2j0ie3XBM0Jij0aAvM1YgqPDJkXYuJ44N-YDbySlnEYhR5QPDufL6Fb3mTe2YZAYJLTBuI20HZw0uu2mDmxm0udg59bE3wzHRo3DHzUAuYEJwcuLPz_ML5S-_QlL4xVE3jTKsjhUTJSEbL1YuI8kndDJ9n091IAmZ-zg777YUjXBzCycRfPJW-5Y5NrwOjHovjdL2WNHBwPXuuISvRgpTOaCq8rPku5xO4n7dWuVrpXpIOo2U9yvuiD3fvMU2dOHQ1lc-_Tf03w4M5AmmD11yorCqX07ST0JtLJr_dkPlHuyRysxg6u6QVJqGq9nA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b2c630a3b3.mp4?token=hmaFJc_gtoLcekWqWIxeAIxUW2j0ie3XBM0Jij0aAvM1YgqPDJkXYuJ44N-YDbySlnEYhR5QPDufL6Fb3mTe2YZAYJLTBuI20HZw0uu2mDmxm0udg59bE3wzHRo3DHzUAuYEJwcuLPz_ML5S-_QlL4xVE3jTKsjhUTJSEbL1YuI8kndDJ9n091IAmZ-zg777YUjXBzCycRfPJW-5Y5NrwOjHovjdL2WNHBwPXuuISvRgpTOaCq8rPku5xO4n7dWuVrpXpIOo2U9yvuiD3fvMU2dOHQ1lc-_Tf03w4M5AmmD11yorCqX07ST0JtLJr_dkPlHuyRysxg6u6QVJqGq9nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تخریب «کاروانسرای روس‌ها» در سبزوار:
quotes
خانه واجد ارزش تاریخی «تومانیان» معروف به «پادگان روس‌ها» در سبزوار روز چهارشنبه در روز روشن با لودر تخریب شد و اعتراض گسترده فعالان میراث فرهنگی را به همراه داشت.
تصاویر منتشر شده در شبکه‌های اجتماعی نشان می‌دهد که یک دستگاه لودر روز چهارشنبه ۱۸ شهریور بخشی از یک بنای تاریخی معروف به «پادگان روس‌ها» در سبزوار را تخریب کرده است.
«پادگان روس‌ها» یا خانه «تومانیان» در سبزوار با وجود آنکه در فهرست آثار ملی ثبت نشده بود اما از سوی میراث فرهنگی به عنوان یک بنای واجد ارزش تاریخی اعلام شده بود.
معماری این بنا متعلق به دوره پهلوی اول بوده و در زمان اشغال ایران توسط روس‌ها، ارتش روسیه مدتی در این بنا مستقر شده و به همین دلیل به «پادگان روس‌ها» مشهور شده است.
مجتبی کاویان، مدیرکل میراث فرهنگی و مدیر پایگاه بافت تاریخی سبزوار در گفت‌وگو با صدای میراث گفت: این اثر بدون هماهنگی و بدون مجوز میراث فرهنگی تخریب شده و اعلام جرم علیه تخریب کنندگان این اثر واجد ارزش تاریخی قطعی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78311" target="_blank">📅 16:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78309">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OlRD3h_ZCbDGzySTbUkxg1TH5NTSmBBj0ALegq5GAW2QhBPaw2FY5KbwjcWm5o0gkGHfwOeQX5n4JeItx_NnEkksww3PExXFQnOpLsOA2zTcHBqftOMNtloMgAcScy8xOjhvCJeCc4DjK91b5fEqdN9YgUl4mYlh5yG9I7zglbzzTyQGye5MzdGyhQOJDtlSjxC0qaYlGRttk6yb47xaCT26tlgJiqixRPid-C8RqalhKlLdq3B8UEEvDASUfdG8aRrTtzrhv77cnKZn3k7DMIvYFTIhTo8r4O9YV69pUMRHhQ_aKFbePpx9DSjzciNPiqR8ogKxFVyFNhjPgG15eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/STNp2V-_GHmDmHHC3RXwdmgri-A-zaEDYdPl5u_Useo1NjQxr-mEJ0ejzXsbmkaGdTnYXcx5_Rg3vKSktFvI8nxz1nLU3uHH0O71Wd9qFds9waWKJSGvf3urY8THuTEQ0FsThuDjgrwGM51P6un_bSQMcvtrzoTxvZ5LEvNHILoZtVKs-FR-gss3G4R9E47Ey6OkfF_vqMQMLYQhj6_DWczgbZwKCErIoqTGiLcpOJGy0kib0tw0VsZTFmAzJ4V0K_5Riyo1-znC9MPvQKrsWVgBVbQcluelSLibEa1gkk7RKVYMjKFkWV-A8dGKQMphy23wLBTe0E5kc_ogoRbEnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ از مشاهده «تحرکاتی» در کوه کلنگ‌گزلا خبر داد و به جمهوری اسلامی ایران هشدار داد: «توصیه می‌کنم ایران زرنگ‌بازی درنیاورد، زیرا مجبور خواهیم شد بسیار سخت به آن حمله کنیم.»
ترامپ در ادامه از حاضران پرسید آیا ایران باید سلاح هسته‌ای داشته باشد و پس از پاسخ منفی جمعیت گفت دولت‌های پیشین دهه‌ها تلاش کرده‌اند جمهوری اسلامی را از دستیابی به سلاح هسته‌ای منصرف کنند، اما به گفته او، مقام‌های جمهوری اسلامی ایران «زبان گفتگو را نمی‌فهمند.آن‌ها فقط یک چیز را می‌فهمند و اکنون به مقدار زیادی از همان نصیبشان می‌شود».
@
VahidOOnLine
رییس‌جمهوری آمریکا، در گردهمایی جمهوری‌خواهان در دالاس گفت جنگ با جمهوری اسلامی مدت کوتاهی پس از انتخابات میان‌دوره‌ای سوم نوامبر پایان خواهد یافت و تهران خواهان توافق با دموکرات‌ها است.
ترامپ برجام را «یکی از بدترین توافق‌ها» خواند و گفت جمهوری اسلامی در مسیر دستیابی به سلاح هسته‌ای قرار داشت.
او افزود: «اگر من برجام را لغو نکرده بودم و اگر با بمب‌افکن‌های زیبای بی-۲ آنها را هدف قرار نداده بودیم، اکنون سلاح هسته‌ای داشتند.»
ترامپ گفت در آن صورت مجبور بود با رهبر جمهوری اسلامی تماس بگیرد و بگوید: «جناب رهبر، حالتان چطور است قربان؟ کاری هست که بتوانیم برایتان انجام دهیم؟»
ترامپ در ادامه تاکید کرد: «ما نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. موضوع بسیار ساده است. نمی‌توانیم اجازه دهیم آنها سلاح هسته‌ای داشته باشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78309" target="_blank">📅 06:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78308">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78308" target="_blank">📅 06:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78307">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78307" target="_blank">📅 06:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78306">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78306" target="_blank">📅 06:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78305">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پیام‌های دریافتی:
سلام الان ساعت ۰۰:۲۵ قشم صدای انفجار اومد
قشم صدای انفجار اومد
وحید قشم بد زدن تمام خونه لرزید
#قشم
00:24 نوزدهم شهریور
صدای انفجار و لرزش
قشم صدای شدید
شیشه ها لرزید
موج انفجار شدید همین الان قشم 00:25
وحید قشم یه صدایی اومد
شیشه ها لرزید
صدای یک انفجار بندرعباس
وحید جان انفجار شدید ساعت 12:25 قشم
سلام صدای وحشتناک باعث لرزش شیشه خونه شد
سلام قشمو بد زد کل ساختمون لرزید
همین الان نزدیک قشم صدا انفجار اومد.
خونه لرزید.
صدای انفجار به بندرعباس رسید لب ساحل نمیدونم کجا زدن
درود به آقا وحید شبت بخیر ساعت 0:25 انفجار سنگین از سمت دریا نمیدونم قشم بود یا جای دیگه ولی بندرعباس به شدت حس شد
قشم لرزید
موجش قوی بود
شدید بود خیلی
توی دریا بود انگار
سلام داداش وحید .صدای انفجار مهیب در قشم شنیدیم
خیلی مهیب بود ..
۰۰:۲۶ بندرعباس انفجار رخ داد
فقط صدا نبود
در و پنجرها هم تکون خوردن
صداش انقدر جدید بود ما داریم میگردیم میگیم لابد اسانسور ساختمونمون ول شده
🤦‍♀️
صدای انفجار در خونه لرزيد قشم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/78305" target="_blank">📅 00:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78304">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/692967643d.mp4?token=F8s0fu0yKRCI-6dfkBRUFZy0ms0iHG2_IeraKjlTaRPf0xquaGvos_aWkRV-fFaCUSBNR0FAx-qCBCLzfc7llXeUuv9E9Ekk06LE_tvU2yVvKwibmrSi-w4P_igYCCHzh9qGDYqDSq0Iz_EkoJzhSl7PufwlybUEVRZOGrdC-AJz_23B9MjdSg6zoixINXCjK5FXNupLplUHVIGEYPoVqicfuBRqFERMjlK010CI69W1l1_-Sjy9waKApOtmI7-o9Smllc-mx0AMRNoRyoK2jlJgDY9hcDSayr6CWVvev3QyQnWQT30RiKbMd1nkzuq6rU8_i55yfLWqFdwA0jMEcw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/692967643d.mp4?token=F8s0fu0yKRCI-6dfkBRUFZy0ms0iHG2_IeraKjlTaRPf0xquaGvos_aWkRV-fFaCUSBNR0FAx-qCBCLzfc7llXeUuv9E9Ekk06LE_tvU2yVvKwibmrSi-w4P_igYCCHzh9qGDYqDSq0Iz_EkoJzhSl7PufwlybUEVRZOGrdC-AJz_23B9MjdSg6zoixINXCjK5FXNupLplUHVIGEYPoVqicfuBRqFERMjlK010CI69W1l1_-Sjy9waKApOtmI7-o9Smllc-mx0AMRNoRyoK2jlJgDY9hcDSayr6CWVvev3QyQnWQT30RiKbMd1nkzuq6rU8_i55yfLWqFdwA0jMEcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز چهارشنبه ۱۸ شهریور گفت که از دید او جنگ با ایران «بلافاصله» بعد از انتخابات میان‌دوره‌ای آمریکا پایان خواهد یافت.
دونالد ترامپ پیش از عزیمت به سمت شهر دالاس برای شرکت در اجلاس حزب جمهوری‌خواه به خبرنگاران گفت: «فکر می‌کنم جنگ بلافاصله بعد از انتخابات تمام خواهد شد. چون آن‌ها (ایران) دیگر نمی‌توانند دوام بیاورند».
ترامپ درباره وضعیت ایران افزود: «آن‌ها مستأصل هستند و تلاش می‌کنند بر انتخابات تأثیر بگذارند».
ترامپ در پاسخ به پرسشی درباره حملات گسترده طرفین در اطراف تنگهٔ هرمز گفت: «حملات توسط ما انجام شد. ما ۹ نفتکش آن‌ها را زدیم. قرار است حملات بیشتری انجام شود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/78304" target="_blank">📅 23:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78303">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/739c863db9.mp4?token=Nhphxp6tD_etozLdLghDTgzpd_CDEKF8iBxaGGVgTfJ9ZWkUigDS0WdKrTj3ykkLdY-8NaYyXvALBv79eSaq_-JEe4JzDtKyVCTJMBknJHYdn7UHdRZ2Hg7lFsIHNkFtj2lLv06GKEueKUWlzaxS2_CH6_zV3Hz1au5wxW3h0-8632Ml0NKRNsEkc5bAjZag9bws__dYEROMwboaT3c374uMsykc0e7Y6JHZ9I20auxh1DHWjl3SidJdPNXuEF4C9I_-Bs3KcFAqtgy10VYMrr30Lnzy9zkEpDtb_TVDQQMuUzgIA-LD0smY-cJC8nWH_Nim1GPDG34ifsjbsIZFcg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/739c863db9.mp4?token=Nhphxp6tD_etozLdLghDTgzpd_CDEKF8iBxaGGVgTfJ9ZWkUigDS0WdKrTj3ykkLdY-8NaYyXvALBv79eSaq_-JEe4JzDtKyVCTJMBknJHYdn7UHdRZ2Hg7lFsIHNkFtj2lLv06GKEueKUWlzaxS2_CH6_zV3Hz1au5wxW3h0-8632Ml0NKRNsEkc5bAjZag9bws__dYEROMwboaT3c374uMsykc0e7Y6JHZ9I20auxh1DHWjl3SidJdPNXuEF4C9I_-Bs3KcFAqtgy10VYMrr30Lnzy9zkEpDtb_TVDQQMuUzgIA-LD0smY-cJC8nWH_Nim1GPDG34ifsjbsIZFcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامعلی حداد عادل می‌گوید حکومت فعلا نمی‌تواند «به علت شرایط جنگ آن‌طور که باید وارد جبهه حجاب» شود.
این عضو شورای عالی انقلاب فرهنگی و مجمع تشخیص مصلحت نظام در ادامه می‌گوید شرایط کنونی کشور از نظر حجاب «بسیار سخت‌تر از سال ۶۰ است که شروع به کار کرده بودیم».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78303" target="_blank">📅 21:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78302">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o0-2cD2eVCj5H9S0ywXMQlo_g3GHz58OM8OstawGlShk3bAcXLcwCLDcWLCqaIywLFDIXmzxITTTuonviUWqzxUOu9x_4pcRJBPNox5iZjBTjQ2od6RS_t1JtExc5OscU7k_rbxWNVuc03jeNduG3jgkl2oixfN5b218KSTx7z3bLI5JL995d3q0J4BdsbkUiK2mtTWUFG4TYoHoacSA5FhSj6k-4OzAGDUnVsruse-UkJdKnrMmQKX31UVHj7w9Xjh2aykDGM_Px-DU1WU6V017fXEtEsbF-iXgD1lCiS_5WGT3E1o14jPxJV0lJnQLOaVBZ6nvK-bNfBjYsY2HQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز روز چهارشنبه ۱۸ شهریور به نقل از منابع دیپلماتیک گزارش داد که شورای حکام آژانس بین‌المللی انرژی اتمی با صدور قطعنامه‌ای، پرونده ایران را به دلیل نقض تعهدات منع اشاعه هسته‌ای، پس از ۲۰ سال به شورای امنیت سازمان ملل متحد ارجاع داده است.
این قطعنامه جدید در پی قطعنامه پیشین شورای حکام در ۱۲ ژوئن سال گذشته صادر شد؛ فهرستی از موارد «پایبند نبودن» ایران به تعهداتش که درست یک روز پیش از آغاز حملات هوایی اسرائیل و متعاقبا ایالات متحده به تاسیسات هسته‌ای ایران تصویب شده بود.
بر اساس قوانین و الزامات حقوقی، گزارش رسمی این نقض تعهدات به شورای امنیت سازمان ملل، مستلزم تصویب دومین قطعنامه از سوی این شورای ۳۵ عضوی بود که اکنون به سرانجام رسیده است. این اقدام می‌تواند مسیر را برای بازگشت تحریم‌های بین‌المللی و افزایش فشارهای دیپلماتیک بر تهران هموارتر کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/78302" target="_blank">📅 20:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78301">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gjxgc6xxZEBzsJmfiLN24umjnaYmfmYwMZi8Uyk-6j5dJZYDe2LfHYa_96unkErf_c-7U7sDBisNc5dzw53nbVfZcOVc2Qtvfng2AYsbWuYXPk_NDH9NlWyEMWxm3PPy0m4ZtnQDJQAEdOw968IzJmuuVXDIanUB2lubIl2uCf38Ikq_WZsi2ccg2BmHhGEYhoLl7njLyGZLin9BlOHpQhjviCoO3YWpCEUwupfjP69SOAN18VyMmRzVVHtqBYCfX1yNCKwPhfcsIVMWV_nSocu97Pm30bKVDeQco0pYhxwjAD_8Fw-Qk7Bqpa3b1D-3ATJI2WK8JxXQDp6ARGG5hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: 'شناور آمریکایی در تنگه هرمز، سمت جزیره سلامه خصب عمان، چهارشنبه ۱۸ شهریور'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78301" target="_blank">📅 19:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78300">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5c510746f.mp4?token=nkh1mpfITCF3S_a9usJqLbxdOnRNefZH6ZG-U4iD2fWf4DOblphBuYxrJXAKsd-D3HEZ6RrNjlwwjVnqUohxYWPmjxFlgvXDBl65mnysmLcNbC5kpqgK8jd44t4Cq2_qi4ok5O7n5TyPqRw3arntiZPHgoHhJvFb3pRs5YmT2ejuNFiwvToJn-2kl9z65nP5h10WWZC2bxmG7IsC4hnJOS8btMENXgdVdG2SRPe1XuCcEv9gy8Qtyxo3GQ0R4akh2mY9xhZ1zTn7IDNjCiVgT5kRo3nprSvQBGOCCABkXTX06cyDW2rP3H0E6RRjW8Gaf_vmmJ-X-QcOIhesdKQCYw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5c510746f.mp4?token=nkh1mpfITCF3S_a9usJqLbxdOnRNefZH6ZG-U4iD2fWf4DOblphBuYxrJXAKsd-D3HEZ6RrNjlwwjVnqUohxYWPmjxFlgvXDBl65mnysmLcNbC5kpqgK8jd44t4Cq2_qi4ok5O7n5TyPqRw3arntiZPHgoHhJvFb3pRs5YmT2ejuNFiwvToJn-2kl9z65nP5h10WWZC2bxmG7IsC4hnJOS8btMENXgdVdG2SRPe1XuCcEv9gy8Qtyxo3GQ0R4akh2mY9xhZ1zTn7IDNjCiVgT5kRo3nprSvQBGOCCABkXTX06cyDW2rP3H0E6RRjW8Gaf_vmmJ-X-QcOIhesdKQCYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با حضور در قله جبل‌الشیخ (حرمون) و اشاره به تسلط بر مناطق مرزی سوریه و لبنان، هدف اصلی کارزارهای نظامی جاری این کشور در منطقه را شکست و سرنگونی رژیم ایران عنوان کرد.
نتانیاهو در پیامی ویدیویی، به حضور نیروهای نظامی اسرائیل در مناطق مرزی سوریه و لبنان اشاره کرد و گفت: ما اجازه نخواهیم داد هیچ گروه تروریستی در مرزهای ما مستقر شود. این یکی از دستاوردهای عظیم ماست، اما کار اصلی هنوز باقی مانده است.
نخست‌وزیر اسرائیل با ابراز اطمینان از دستیابی به این هدف افزود: کار اصلی ما شکست دادن و تضعیف کامل رژیم ایران است. ما بسیار به این هدف نزدیک هستیم و می‌دانیم که کل این محور سرانجام سقوط خواهد کرد و ما این کار را انجام خواهیم داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78300" target="_blank">📅 18:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78299">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ufqbASvR0cwxloZe2njensz6AY2f8CXzyKF8DmsTiI2lh402no0uN8Y_AQan9Ju9YFk09a1oogkXSncfQ5fwsrSX3jDoHczqRGxgMRUuld1vfE22f6Vos9llIvg0tpSKFTEOHerRlE9dUNEt2h9XmAE91BxmK8anwAYFmiV7Sl37ofpgY1AlWg7LKdAXwlYe1wJRXY_GqHR12PWu9zRnQz-ft3S9k8uWnRA0ns_T1jxctovnbDzY5UeriupsqWiCuVXQ3h4FIHfwGpJD5OAzlkZ_nZe_vSPKrLqBq0gpxJKxss2ef-21OAkFEEo9CPhTsG5IpZfxStqU_0Aijw2bIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه پاسداران برای پایان وضعیت کنونی و بازگشایی تنگه هرمز از آمریکا خواست جنگ و تهدیدها را متوقف کند، اسرائیل از لبنان عقب‌نشینی کند، محاصره یمن پایان یابد، ۲۴ میلیارد دلار از دارایی‌های مسدودشده ایران آزاد شود و مداخله در برنامه‌های هسته‌ای و موشکی جمهوری اسلامی متوقف شود.
حسین محبی، سخنگوی سپاه پاسداران، روز چهارشنبه ۱۸ شهریورماه گفت اگر آمریکا خواهان پایان وضعیت کنونی است، باید ضمن «توقف کامل جنگ» از تهدید دوباره دست بکشد.
محبی در بخش دیگری از سخنانش تهدید کرد که در صورت ادامه حملات، پاسخ سپاه گسترده‌تر خواهد بود و گفت: «اگر دشمن دو یا سه هدف ما را بزند، ما با ۲۰ هدف پاسخ محکم می‌دهیم.» او همچنین گفت جنگ کنونی برای نخستین‌بار «آسیب‌های راهبردی» را مستقیما به آمریکا منتقل کرده است.
این اظهارات در حالی مطرح شد که با تداوم محاصره دریایی ایران، صادرات نفت از طریق تنگه هرمز متوقف شده و فشار تحریم‌های مضاعف دولت ترامپ، باعث تورم کم‌سابقه در ایران و رسیدن قیمت دلار به ۲۳۳هزار تومان شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78299" target="_blank">📅 16:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78298">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TC87Kum3syLzgK6RMvr_3hifT4d7JjI-H5xtyGQeGUM2_3aEMcHg1yh076x9nL3ekPrjMqux4w5pF5j9xoJKM5QNlE_pkcuUdklchaWWoPiWnJfVx_qlHXPIr0xzyNrX9DqvqW32UMhtZ-dd-I7NHjv9nQmbd63DDH5uZgk3lrgR3Eu5SKZVSlqbja4RCYbHCp_0wXpOU6wWPDZviqfPoDzdp8NlU1LUUac_8-Kgvr0JnHjw-3QKPxh6-4MPxdatKkpDsMRbAxFS6GoipHeKj1qOafA4tWgeyzWsa6boa-9nQTiDpzQUNOsCUQ-k_x7hPyEoO_MlFFcb8nVG9ihlNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت ارزهای خارجی در بازار آزاد ایران روز چهارشنبه ۱۸ شهریور ۱۴۰۵ رکورد تازه‌ای ثبت کرد و نرخ دلار آمریکا از ۲۳۲ هزار تومان گذشت.
برخی وب‌سایت‌های اعلام قیمت ارز نرخ دلار را در معاملات ظهر چهارشنبه تا ۲۳۵ هزار و ۵۰۰ تومان نیز گزارش کردند.
هم‌زمان قیمت یورو از ۲۷۱ هزار تومان و پوند بریتانیا از ۳۱۵ هزار تومان فراتر رفت. این افزایش‌ها در حالی ادامه دارد که ریال طی دو هفته گذشته بیش از ۱۵ درصد ارزش خود را در برابر دلار از دست داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78298" target="_blank">📅 16:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78297">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0A0_o5B_OVbVR48-b22YDjSFbJcVE3EfMixg5FocHHhNHLfePi4mL5IKev-J49nslJ9sNpnOmTmrcB7gFSD2D24JaFfUQTAev6lxtBF0HbtkBVfv8MGIb8EKSIqRionaMCBDJfT8oADYmG6s7xnYlKrMsky42In9wRruKXfBvnQaI5x72IyXoOhNuLJibRj6ZVCxY-ZB9_qLU4bCWtehUiNknx7sERcWm0Jqe5wt85qQIZe9v7vgoHkJvh8SZlcUh1vUDd4Lhi2vglrRsYM9LH5a05x6fQoQnIjaAGFxd5kgdFE1LKsC6gmcKlN2vmsvfRel5XeE6nYxsbKplP4XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت خام برنت برای نخستین بار از دوم مرداد به ۱۰۰ دلار در هر بشکه رسید و بار دیگر وارد محدوده سه‌رقمی شد.
افزایش قیمت نفت و ارز در شرایطی رخ داده است که درگیری‌ها در خلیج فارس و منطقه ادامه دارد. شامگاه سه‌شنبه ۱۷ شهریور، آمریکا اعلام کرد پس از حملات موشکی ناموفق جمهوری اسلامی به دو ناو جنگی این کشور در خلیج فارس، پنج نفتکش مرتبط با سپاه پاسداران را منهدم کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/78297" target="_blank">📅 16:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78295">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O8MmommEumSLV_GCUnShtAcrc9uvKuMaSGBhcxFCLXl77kSx-6VkOuFFrv2EptvHICbbhtVBV0g-TneobfrsSfqOdKNCkQ28zDNQ7qouTR9sRIvIVWAKSDFUDqrE_G-5mTRWiS93sBhsvvuuGX3r8IqLAgYFFMAchmuJijf62WQVa7pwUfXp9VIHc6DXhLiMh6M-7JFssAV4syJdEnbFDol_4pXExmgVmLVsKkJWJ9r1WHR29hQ4asLxQLh4xlp3G7EiU6D2f6Vl8qGgWm65TA1n6-jfTZ5xyxpZNLetxjIqb_-ab0GTd5_GxzWIcweqa1Awp_W5kQoU2fBjrtWu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fNs3EmO4r_TpEzvkUWJYm7EB3yxMz8T4eXLx6ItBO0OL8HcaLxHh-AdIRnrL5h7JTw_hZBy7yFOF-zN8b8naMjmHSOdGZ-nRWmOEIvJuQ5U3oop2e105Virc5e1m9Sz0ovKOObq1LhxZ9nVwzjSBPyXK6E0k33if6Oti0mb_bs4uhDnHNSPQG1PYr2LzRPWYoqkXRkoq9xPik_kSdViTBKcaF3wxZtuBMkd7vm3PiQ0UKN0uD8-xHP1GKQY_uDXDZRqYkGcACD4MZFCsZcbu-Bul_DHEJoVn3dg2H6DOWfZY1ljayjQIlbVfX8pOvAOOyRqkRMlEpX3xNApNtHGVEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا (UKMTO) ظهر چهارشنبه ۱۸  شهریورماه از وقوع حادثه برای یک نفتکش در ۲۴ مایلی بندر راشد امارات متحده عربی خبر داد.
براساس این گزارش، «کاپیتان یک نفتکش گزارش داده است کشتی‌ای را مشاهده کرده که در حالت لنگراندازی کج شده است، که احتمالا نشان‌دهنده ورود آب به داخل آن پس از حمله با یک پرتابه نامشخص است.»
@
VahidOOnLine
مرکز عملیات تجارت دریایی بریتانیا اعلام کرد یک نفتکش در ۲۸ مایل دریایی جنوب شرقی بندر فاو عراق با یک پرتابه ناشناس هدف قرار گرفته است.
بر اساس این گزارش، ناخدای نفتکش برخورد پرتابه با شناور را گزارش کرده است.
خدمه نفتکش در سلامت هستند و تاکنون هیچ پیامد زیست‌محیطی ناشی از این حمله گزارش نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/78295" target="_blank">📅 16:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78294">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pNTVyajKTecFFu3FR1CrHwC3yk_nbQZaA5aFXx1JVEXyuEsE_-p-oQwGqwoilsz7lrMnBGaFi02lDYpwkj4EqU2EcP3_jgdHrLdI96y0dhQL_EbKFIno1q3Xov6-RT0vO8b0mFD3i6H5g5dR5W-fPv22JiUl-toBBjBSP9DvnBuYx75BR-17Ws_ICS0F-DNb8zmA0Vl7VdhmmyYsPAPbifJpnR6-fGpBgeHnx88k4Qu6TyFA9X1tNM9PRVii66CB0HKx1UKvmegs9-o8bIobYdVgu7jW7W9tBfyNzZDCOcsHb23xb9PmXyorMHiIDKooHIvhNczZJO2_RJUWu9tkEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین:
🚫
ادعا:
نیروهای سپاه پاسداران انقلاب اسلامی ایران (IRGC) مدعی شده‌اند که دو ناوشکن نیروی دریایی آمریکا را که در خاورمیانه در حال عملیات بودند، هدف قرار داده‌اند.
این ادعا کاملاً دروغ است.
✅
واقعیت:
هیچ ناو جنگی نیروی دریایی آمریکا هدف قرار نگرفته است؛ تمام حملات مورد تلاش سپاه پاسداران شکست خورده‌اند.
در همین حال، نیروهای آمریکایی تنها طی هفته گذشته موفق شده‌اند ۱۰ نفتکش ایرانی را منهدم کنند.
این شناورها بخشی از یک شبکه سایه چندمیلیارددلاری بودند که منابع مالی سپاه پاسداران را تأمین می‌کند و ایران قادر به دفاع از آن‌ها نیست.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/78294" target="_blank">📅 16:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78293">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QUkeQapkD3tsmVFEmo9Z8hBHkzqPxlV6-j3G6WOAJ_njhj9KACH0pgg_xMAJ4a986UDU_q4OVKN5A13BQWFKLdjIOFTmrjAt6iG-uYfHVLS3-wB9JIGc3zptEDN-Mp6JwGP55rDAx3E6ETY9mT1T7YdXkzf8f59-HCAcH5wF30GYk0-NUyghJtbcN7ZsENaHuKaZlPPSm1qeM4QuSORyRLAwWKCAaGfBpu1o6b2NNu6OKV4p6uht6B91BnW_tuWtv4hMuUgMxhQQh02TJQbUOm_zbEtQ851WDyfUlrauRP-2Jq8qdFgGpSuClfSGxgBv8cIlKe0Q9heSb4xTEtGkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«ماموستا محمد نزهتی»، روحانی اهل سنت و امام جماعت منطقه چیانه در شهرستان پیرانشهر، در یک حمله مسلحانه کشته شد.
سپاه پاسداران او را از روحانیون همکار با بسیج معرفی کرده و مسئولیت کشته‌شدن نزهتی را متوجه آنچه «گروهک‌های تجزیه‌طلب کردی» و «صهیونیستی-آمریکایی» خوانده، کرده است.
براساس این بیانیه، نزهتی سابقه «همکاری طولانی» با «بسیج اساتید، طلاب و روحانیون» داشته است.
سپاه همچنین فعالیت‌های او را در راستای حمایت از جمهوری اسلامی و آنچه «وحدت شیعه و سنی» خوانده، توصیف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78293" target="_blank">📅 16:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78292">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11f95a9d62.mp4?token=lvFDbwrrQkJBcA-3nd7wibZB6gKwZNohnR4CH_jsqK-1HgLQ_AwB9AaAkDtGCKKCsFuqMxoDX9tzDb_61mnXtYuIlH_4B_-GuV0mxi-RwtqjqR3tfNFlh2GvEacX2OXe7lEUjLTFvgx6gUBqmHIfhkDCywAvOX6JbN0plE9JbCli5wseGu3PuTlGLNimheAK-JgMXaN1l0f5k_k3SvH1N8IfxgLXnEVv5O-NqDjuVR1xvXoLY0SIjGsDFgZHeqFza-8YhWdD-Eb7ovHUPa7RS1q0y73PP9nnyCmuoP5gzgg3-OwI4-LPeeLfHRWuJX2Ef_xpmcvfXlOVDSyUGWlmsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11f95a9d62.mp4?token=lvFDbwrrQkJBcA-3nd7wibZB6gKwZNohnR4CH_jsqK-1HgLQ_AwB9AaAkDtGCKKCsFuqMxoDX9tzDb_61mnXtYuIlH_4B_-GuV0mxi-RwtqjqR3tfNFlh2GvEacX2OXe7lEUjLTFvgx6gUBqmHIfhkDCywAvOX6JbN0plE9JbCli5wseGu3PuTlGLNimheAK-JgMXaN1l0f5k_k3SvH1N8IfxgLXnEVv5O-NqDjuVR1xvXoLY0SIjGsDFgZHeqFza-8YhWdD-Eb7ovHUPa7RS1q0y73PP9nnyCmuoP5gzgg3-OwI4-LPeeLfHRWuJX2Ef_xpmcvfXlOVDSyUGWlmsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشک‌های مادر یسنا (فروغ) اسکندری در سوگ دخترش
یسنا اسکندری، وکیل دادگستری و نقاش، شامگاه ۱۸ دی‌ماه ۱۴۰۴ در منطقه آریاشهر تهران هدف شلیک نیروهای جمهوری اسلامی قرار گرفت و جان باخت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78292" target="_blank">📅 16:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78291">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OmFFSKoB9kkjyS2FS8u3sSHxp-NKvwTu20GMXAS4aKQMPwQBXMS0975VLJjLAjgebEh4NOT-RqnC-iWS_MIAXK6IDmEjDQzQMlWbOMXHpldHGha4JTFJKbPANcbJbl_bQ00cs2_5qPKSnHoWTWvlBBoI9bRNlZBg3oisjO32RP2x8Rij9fdnURbGYTLqQxsY9ZZPr6svk8T1HrwM2CtOCKGeCCwxuIMQ2VT0D4KXijwqxEm4pxAOJ2woF2UjaNxkbFej5ZfCts4ShcFy8enXHF2CRTkeQhngCt6OlTiCzoWKyz3L6y2xPd8at3M9O5CllvvH8tzXblxQBrlgUW5zvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران: دو شناور و هشت نفتکش را هدف قرار دادیم
سپاه پاسداران که در طول چند ساعت گذشته با انتشار چند اطلاعیه از حملات موشکی خود به مواضع آمریکا در اردن و بحرین خبر داده بود، در آخرین اطلاعیه مدعی شده است که در واکنش به حمله آمریکا به ۵ نفتکش ایران نیروی دریایی سپاه به «دو فروند شناور آمریکایی و هشت نفتکش» حمله کرده و «خسارت های زیادی» به آنها وارد کرده است.
در این اطلاعیه که بامداد چهارشنبه ۱۸ شهریور منتشر شده همچنین ادعا شده است که «۱۰ فروند کشتی متخلف که به گفته نیروی دریایی سپاه، قصد عبور از «منطقه ممنوعه و ناایمن تنگه هرمز» را داشتند حمله شده است.
این گزارش‌ها هنوز از سوی منابع مستقل تایید نشده است.
با این حال، سنتکام در اطلاعیه نیمه شب سه‌شنبه خود هدف قرار دادن ۵ نفتکش ایران را در واکنش به حمله به رزم‌ناوهای خود دانسته و گفته بود این ناوهای جنگی خسارت ندیده و در حال ادامه ماموریت‌های خود هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/78291" target="_blank">📅 08:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78290">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3e8057645e.mp4?token=PV9tEnyvP2HJz_I6Urd3CJvDae7omvwhTIQ5n7I3Q9SBwkxhVvgJoPYgt5YOrmWNIqDxlXK2yoz3YprRDUqImbdkLi-uyPVReW8zNfF1j5tG7FCZHTLIdLgrKT9aQW236HU9GwkEb0JfqB5tPtQ8B_U2IY8b9XqkKIsWJzDn2JMGsC1BoCFf8S1VCG3U-wiI06Iv0wuujL-HCHxSudVqfmBAl4GJ264SEH3y3gw7nB-D25uvYOx5AB-pb-3Ziv7HUiZy9Nw-qVSuxZ8euKQHE303iFc_BWisqrYRZljVhdvTppnvcpjA66tsawsY9g_cMvcMajfFWnVX4dz89T0M1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3e8057645e.mp4?token=PV9tEnyvP2HJz_I6Urd3CJvDae7omvwhTIQ5n7I3Q9SBwkxhVvgJoPYgt5YOrmWNIqDxlXK2yoz3YprRDUqImbdkLi-uyPVReW8zNfF1j5tG7FCZHTLIdLgrKT9aQW236HU9GwkEb0JfqB5tPtQ8B_U2IY8b9XqkKIsWJzDn2JMGsC1BoCFf8S1VCG3U-wiI06Iv0wuujL-HCHxSudVqfmBAl4GJ264SEH3y3gw7nB-D25uvYOx5AB-pb-3Ziv7HUiZy9Nw-qVSuxZ8euKQHE303iFc_BWisqrYRZljVhdvTppnvcpjA66tsawsY9g_cMvcMajfFWnVX4dz89T0M1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) با انتشار ویدیویی نوشت: نفتکش ریسکو روز سه‌شنبه، پس از آن‌که در واکنش به تلاش‌های سپاه پاسداران برای حمله به یک ناو جنگی نیروی دریایی آمریکا توسط نیروهای سنتکام منهدم شد، در خلیج عمان غرق شد.
@
VahidOOnLine
M/T Riesco sinks in the Gulf of Oman, Sept. 8, after being destroyed by CENTCOM forces in response to attempted IRGC attacks on a U.S. Navy warship.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/78290" target="_blank">📅 05:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78289">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت 4.19 دقیقه صبح بندرکنگان الان صدای انفجار اومد
در و پنجره ها شدید لرزید
سلام صدای انفجار نزدیکای بندر دیر
صدای انفجار شدید.بندر دیر.
ساعت ۴/۲۰ بامداد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/78289" target="_blank">📅 04:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78288">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CJw1hqajvrdmCmNmixQoQ3cteK7aeKomQdhx9qnnVif_5GNGbJi8pC3vw5Y8yM3zs8sa1IIa_peA8Wdkj0JaYp81XB4oIRxjHctj6P4hF6GLzU10YqWvoslijdI1QDdzM75yw5A2fqQwWNGqHmutx0xihZCv7XiHzlAW0PhcI6KXJP6I9kjgKnDeYNUmhPaSYcbmHg-OfT9YWba0kWAMoEMBZxcW9zt8bnOj89y8PSm7ziAi3sWuGcpZO_65zeK64d4cjU3PnVeIZLZeE1U1EN3Ovw9rtSEHM3y_mZ-MiGTE1aHd3rOil5gARZ1oqo41LJ1OBcsd3Tv6ScV5tMYO7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران در بیانیه‌ای خطاب به «مردم مبعوث شده ایران اسلامی» اعلام کرد که با رمز «حیدر کرار» به پایگاه الازرق اردن حمله کرده است.
در این بیانیه آمده که به محل استقرار جنگنده‌ها حمله شده است.
پیش‌تر اسکای‌نیوز از رهگیری موشک‌ها در آسمان اردن خبر داده بود.
تلویزیون دولتی سوریه نیز گزارش داد که پدافند هوایی سوریه برخی موشک‌ها را که از ایران شلیک شده بودند بر فراز شهر مرزی اربد در اردن رهگیری کرده است.
برخی رسانه‌ها در ایران از جمله همشهری نیز گفته‌اند که سپاه با «موشک‌های خوشه‌ای» به اردن حمله کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/78288" target="_blank">📅 02:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78287">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d875f49ad.mp4?token=MLwYC4k-vTGrssWppIS_wP1qBD3di8eDT49FcdopVSsa0oBKBuVZpXbbu0DLO6OX32zzy4Y8hFoqiTtqng1V_DxbAlP4g8ueJgQrEJeWxQ7oQGdyb0PtucMNcQC9EtyVImKn44bn92wPT3Q7BQ6FtWpGgulDO5OoSyWF8voyJjqHE3pQ5Df9BcOy75wMaLfQxHhTbrXD6Wh7OJaLFk-x4jYFRlqFHNtz70KAM9vjOqR4qfb7AfxktHD3dP1N6V5Q_RLTQUA_L54gQPkjqwgjZqa1DXO3NaOpeQaehtnXRB878YG5rC5ZB8yEx7A3fm0p59FSo_Bul7UEt8Me2bxjUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d875f49ad.mp4?token=MLwYC4k-vTGrssWppIS_wP1qBD3di8eDT49FcdopVSsa0oBKBuVZpXbbu0DLO6OX32zzy4Y8hFoqiTtqng1V_DxbAlP4g8ueJgQrEJeWxQ7oQGdyb0PtucMNcQC9EtyVImKn44bn92wPT3Q7BQ6FtWpGgulDO5OoSyWF8voyJjqHE3pQ5Df9BcOy75wMaLfQxHhTbrXD6Wh7OJaLFk-x4jYFRlqFHNtz70KAM9vjOqR4qfb7AfxktHD3dP1N6V5Q_RLTQUA_L54gQPkjqwgjZqa1DXO3NaOpeQaehtnXRB878YG5rC5ZB8yEx7A3fm0p59FSo_Bul7UEt8Me2bxjUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین
خبرنگار:
آقای وزیر، بخش زیادی از توجه افکار عمومی آمریکا معطوف به آخرین تحولات در ایران است. می‌توانید درباره حملات آمریکا به نفتکش‌های ایرانی صحبت کنید و توضیح دهید که این رفت‌وبرگشت اقدامات در ۲۴ ساعت گذشته چگونه بوده است؟
مارکو روبیو:
بله، این رفت‌وبرگشت کاملاً روشن است: ایران همچنان تلاش می‌کند کشتی‌های نیروی دریایی آمریکا را هدف قرار دهد و هر بار که این کار را انجام دهند یا تلاش کنند انجامش دهند، نفتکش از دست خواهند داد. فکر می‌کنم امروز هم دوباره شاهد این موضوع خواهید بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78287" target="_blank">📅 02:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78286">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b638672d55.mp4?token=gmm_ecnYs_CFyPaX6FeqMlf5t3_w5n0Q75W9qIUWLrdHC5KrqNoavcpWLu14krvM-JG-I9VPoY4arB6CnnbzD1n-gbzE906M47_HMg7evlglL_twoLGxon9nILVkUr-y6u9XN-4O66tH1izEmGXFuYM1la_VyBY3o58IvNK5V52CDRXHdOCqHX3MI5zO1rOKj_F6MPaBEUQkGPj9Z5A-UJiN0BEDOr_g6qxvIsGJwi5eYgnyg96T4PxaFt8-HcW-TTwqpQr3V9-rk_DyFEhX309kecwYFkQtKExhhiJgMXglzMj9AZ0bWB_Qv1BFFTBCGXN2QE644VwQm3mghi3LFg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b638672d55.mp4?token=gmm_ecnYs_CFyPaX6FeqMlf5t3_w5n0Q75W9qIUWLrdHC5KrqNoavcpWLu14krvM-JG-I9VPoY4arB6CnnbzD1n-gbzE906M47_HMg7evlglL_twoLGxon9nILVkUr-y6u9XN-4O66tH1izEmGXFuYM1la_VyBY3o58IvNK5V52CDRXHdOCqHX3MI5zO1rOKj_F6MPaBEUQkGPj9Z5A-UJiN0BEDOr_g6qxvIsGJwi5eYgnyg96T4PxaFt8-HcW-TTwqpQr3V9-rk_DyFEhX309kecwYFkQtKExhhiJgMXglzMj9AZ0bWB_Qv1BFFTBCGXN2QE644VwQm3mghi3LFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: "
آمریکا ۵ نفتکش سپاه پاسداران را پس از هدف قرار گرفتن یک ناو جنگی دیگر آمریکایی توسط ایران منهدم کرد"
"U.S. Destroys 5 IRGC Tankers After Iran Targets Another American Warship"
ترجمه ماشین:
تمپا، فلوریدا —
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) روز ۸ سپتامبر پنج نفتکش حامل نفت خام ایران را منهدم کردند؛
این اقدام پس از آن صورت گرفت که سپاه پاسداران انقلاب اسلامی (IRGC) طی دو روز گذشته، دو بار یک ناو جنگی نیروی دریایی آمریکا را با موشک‌های بالستیک هدف قرار داد.
ناو جنگی آمریکا با موفقیت از حملات ایران اجتناب کرد و به گشت‌زنی در آب‌های منطقه ادامه داد. هیچ‌یک از نیروهای آمریکایی آسیب ندیدند.
در پاسخ به تازه‌ترین حملات ناموفق ایران، سنتکام نفتکش‌های حامل نفت خام سپاه پاسداران
M/T Kaviz، M/T Charminar، M/T Horizon 1 و M/T Riesco
را در
دریای عمان
و همچنین نفتکش
M/T Derya
را در نزدیکی
جزیره خارک
منهدم کرد. نیروهای آمریکایی پیش از حمله به کشتی‌ها و از کار انداختن آن‌ها، به خدمه دستور دادند کشتی‌ها را ترک کنند.
ایران از این نفتکش‌ها به‌عنوان بخشی از یک شبکه چندمیلیارددلاری پنهانی استفاده کرده که منابع مالی سپاه پاسداران و نیروهای نیابتی منطقه‌ای آن را تأمین می‌کند. ایران هیچ وسیله‌ای برای دفاع از این شناورها ندارد.
در ۵ سپتامبر نیز نیروهای سنتکام سه نفتکش حامل نفت خام ایران را پس از آن منهدم کردند که سپاه پاسداران تلاش کرد به یک ناو هواپیمابر و یک ناوشکن موشک‌انداز هدایت‌شونده آمریکا حمله کند. تمامی تلاش‌های سپاه پاسداران برای حمله به ناوهای جنگی نیروی دریایی آمریکا ناکام مانده است.
centcom
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/78286" target="_blank">📅 01:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78285">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dc7356e9f5.mp4?token=Cke9sH4nqi5v4RnIZd_qL8rwo6IMzlbpPK_DwepulZe_HaT78zH1YHIyDKhGKZkn_JG068GCDl4SQ414ecsW1BUYWQJsrpWpAz4ryNgRFa9aKIRKELDCrHga51eAl9PAf-8UHzuoGwjwz85qy_eFER9t0Qh1X5_Nb6avp1c3sPqn-2SfuyRAPIITtpnzhnFgCrbNDbCdK6-ypJVRfiwPTS4iLRqG0E35slFsuTQG0H4SvDzwn4ZKlt_7wJeJoRMmRfmtZf6C5F2HjFOiaa0NDDnuCHZ5NNF97lrdb6-1545y15UN6UF64e2AHeXv5b42yicnUdeVkAjp_OwOMWi7Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dc7356e9f5.mp4?token=Cke9sH4nqi5v4RnIZd_qL8rwo6IMzlbpPK_DwepulZe_HaT78zH1YHIyDKhGKZkn_JG068GCDl4SQ414ecsW1BUYWQJsrpWpAz4ryNgRFa9aKIRKELDCrHga51eAl9PAf-8UHzuoGwjwz85qy_eFER9t0Qh1X5_Nb6avp1c3sPqn-2SfuyRAPIITtpnzhnFgCrbNDbCdK6-ypJVRfiwPTS4iLRqG0E35slFsuTQG0H4SvDzwn4ZKlt_7wJeJoRMmRfmtZf6C5F2HjFOiaa0NDDnuCHZ5NNF97lrdb6-1545y15UN6UF64e2AHeXv5b42yicnUdeVkAjp_OwOMWi7Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنا بر ده‌ها پیام‌های دریافتی از صفهان، یزد، خرم‌آباد، خمین و شهرهای دیگر چندین موشک پرتاب شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/78285" target="_blank">📅 00:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78284">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C1ejcj2DMPME9vCkdpjYZxt7LUfeMFjNs9ILC3rwRFOeBPAGQGmyQ_THvhzXEwZeGW_HZPhV2CVgqKMzClmdIgPuwQRrkDCSfCWWtCZ2ApzSWVwHxOBwAJ_XDe1fWnnb9-yOoCr4axFbY66oEFWmC3zNLug7XQDqf69sPp6Zy4mdM5xycghXGP5RsTlFpC-fTd8bbjzemd8C42AaQKEm5HkrL9F27vHNLl2_K-y9IUbhm3EOEti68chv4n5N9X2wPWNLw5pKA514cPtWnhrbfaSP4NWHYVyDFBLOgiDOUzhreXGXJFKNp3lrQ5b12XiFs07YbODnTP8XUcyolGmO3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی گزارش‌ها از حمله ارتش آمریکا به اهدافی در جاسک و اطراف جزیره خارک، رسانه‌های حکومتی در ایران تائید کردند که یک نفتکش دیگر نیز در اطراف جاسک هدف قرار گرفت و خدمه آن با قایق نجات در حال انتقال به مناطق ساحلی هستند.
پیشتر رسانه‌های حکومتی در ایران گفته بودند یک نفتکش در اطراف خارک هدف قرار گرفت.
رسانه‌های اسرائيلی و آمریکایی به نقل از مقامات آمریکایی گزارش داده بودند که علاوه بر اهداف دیگر، چند نفتکش ایرانی نیز هدف نیروهای آمریکایی قرار گرفته‌‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/78284" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78283">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ar_ZmyigWfYVXOjp83VDy4ZbSl84FEx86euZNI2rk0X3grVJBDaeG6kpKKqaZKVo2ZT06_TO6zBSCz4jyc2JoiHQssek-vxQT2xj7b1uMx3Ii5GVMzGt7Jj20SZpE_edk9nZk5V0ndg-cF-7I5xXdxMzlBs7m1IIT5ACKtvz7CchKrX0iqMPhH2IALOUO0QPxwh_Cx52xF1uuya3NALheDkYGXSsoLj1mEfSQqdXlRuNHJzM8SrDGZPg9y1tXnnfErzfTCbxnztkdB9LMQMVQ5sgp370mGW1wM1PCZ_sHEtngOD1zQSol14zvF4jD1INGpNxM_ETOPIZHbkOhpwBGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار سپاه به خدمه نفت‌کش‌ها در کویت و بحرین: شناورهای خود را ترک کنید
سپاه پاسداران انقلاب اسلامی هشدار داد که نفتکش‌های مستقر در لنگرگاه‌ها و اسکله‌های بحرین و کویت را هدف قرار خواهد داد.
در این بیانیه که در رسانه‌های جمهوری اسلامی بازتاب یافت، اشاره شده که آمریکا به «چند نفتکش ایرانی» حمله کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78283" target="_blank">📅 23:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78282">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L_6POc9FTW35m4Mb0zD6H-Lgdpne4J9KHJx6edLTV4xLzhiIr8DM1iQ-uZLQdj6fG_gATUtlBZov19c_vDbF3dXER9s1T2h_QvaIY9t6Vn9Lo5upYClVn35Sy7I6jZpOtoUQ8m9jwzH8-910vgyToDL-74EkQEqSQv6K8E25exTg3VtOq1I5LrAbgslMhmPG4edtVGpe59N7BJ3zOps6O2WRxO1EYyNJjkKuYwdP2yv0avh7qhGh0fAU7FHzQIFMfWMJ0ghKmEyaWG9Lnf0p0L-zBtsonnYSYu2wqYBIu39RiI3Yyk3WUr43N5tyF3Q3ClctKvlalVYTKy-TgLOYJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس‌نیوز: ارتش آمریکا نفتکش‌های ایرانی را در نزدیکی جزیره خارک و جاسک هدف قرار داده است
شبکه فاکس‌نیوز شامگاه سه‌شنبه ۱۷ شهریور به نقل از مقام‌های ارشد آمریکایی گزارش داد ارتش آمریکا اهدافی را در نزدیکی جزیره خارک و جاسک هدف قرار داده است که شامل نفتکش‌های ایرانی می‌شوند.
فاکس‌نیوز به نقل از این مقام‌ها گزارش داد، این حملات بخشی از تلاش گسترده‌تر آمریکا برای افزایش فشار اقتصادی بر ایران است.
مقام‌های ارشد آمریکایی افزودند این راهبرد شامل غرق کردن و از کار انداختن نفتکش‌های حامل نفت خام ایران می‌شود.
@
VahidOnLive
خبرگزاری تسنیم، رسانه وابسته به سپاه پاسداران، گزارش داد که یک نفتکش کوچک ایرانی در فاصله ۴ مایلی جزیره خارک، هدف حمله موشکی ارتش آمریکا قرار گرفت.
تسنیم نوشت که این نفتکش در محدوده لنگرگاه جزیره خارک مورد اصابت پرتابه نیروهای آمریکایی قرار گرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78282" target="_blank">📅 22:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78281">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNtkcBMiS6BhCzfYJmaSDDMp_5JAnme4-YQytY7bc4bQUk6FG_j-ZVPsobcw_6MNMnXGaEfwxHKw2iqdQy2QtXLiZ6AD-GRdkA7RquPIAxKeR3RI4_eNuyrITQgAvtBzU9ucMB160NX8KF-2gNjTw0XUOAt2euUb-TolR3qFT7BZZxrL85l5c_cDiS3kFIVDtxj6chjbSz-SE_a8ewf_qI-z96ZJRqzZvqUdf_heoelFOUlPYCsbrR4ylpYvsCZDm-0F45lpHRAArVWfQsleA-xSpRX-KZabhDswCbi4sAmSxM2-n8poIaVhbhsvnqLJW23RME2f-Mru8kxEBdfUTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، روز سه‌شنبه ۱۷ شهریور اعلام کرد ارتش آمریکا به سه نفتکش ایرانی اخطار تخلیه داده و آن‌ها را به هدف قرار دادن تهدید کرده است.
عبداللهی هشدار داد هرگونه حمله به نفتکش‌های ایران با واکنش نیروهای مسلح جمهوری اسلامی ایران همراه خواهد شد و پایگاه‌ها و منافع آمریکا در منطقه هدف قرار خواهند گرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78281" target="_blank">📅 22:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78280">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">"صدای انفجار از حوالی ساحل جاسک"
خبرگزاری فارس وابسته به سپاه پاسداران:
حوالی ساعت ۲۱:۴۵ امشب، صدای انفجار در شهرستان جاسک شنیده شد.
منابع محلی می‌گویند صدا از سمت دریا و نزدیکی منطقه سنگ سیاه به گوش رسیده و انفجار در دو مرحله و با فاصله کوتاه رخ داده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/78280" target="_blank">📅 22:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78279">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsiF6LnOmbLwvFOHsdqp2XxTjzTLtli7LpYDbJRPC1qEc_FCc1u9Nz3jnl_fdm_6QN6lEM-Y1Q7pAGihnnszGbzbbZgl8aeXuxYp0gwqxnPiWKSMmb_G0xtl7NC7W5NheAjWFJ2bLdAsQwcT5bLjlcSpU4oO2g0mSUgq64Kk69HSYeYMZ4GMTSdVwFxkCzYOl8gbmw-Tm1kTNoxNOcqcvS1BS8-I_NKnG08J0443gGsb3QypyNRHZqgnJYqUDl9q0WUQs02CkXeiZnUohALQPR4VWda12GdJBY96aWr83lBPmRmnha7IbOddZjPkrPNjQJqo5QbhgHTdw1J2t_F-_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی روز سه‌شنبه ۱۷ شهریور به رویترز گفت یک شناور بدون سرنشین زیرسطحی نظامی آمریکا در خاورمیانه، هنگام پایش آب‌های منطقه در حمایت از جنگ علیه ایران، دچار نقص فنی شده است.
این اظهارنظر ساعاتی بعد از آن منتشر شده که سپاه پاسداران انقلاب اسلامی از «شکار» و به «غنیمت گرفتن» یک شناور زیرسطحی آمریکایی در تنگه هرمز خبر داد.
مقام آمریکایی که به شرط ناشناس ماندن صحبت می‌کرد، گفت این شناور معیوب از «مدل قدیمی‌تر» بوده و هیچ‌گونه تجهیزات سونار یا رادار طبقه‌بندی‌شده حمل نمی‌کرد.
او افزود این شناور بیش از یک روز پیش دچار نقص فنی شده است اما به سرنوشت آن و یا کنترل نیروهای نظامی ایران بر آن اشاره نکرد.
در بیانیه نیروی دریایی سپاه پاسداران ادعا شده که «یکی از مدرن‌ترین زیر دریایی‌های هوشمند و بدون سرنشین» ارتش آمریکا در بامداد روز سه‌شنبه به دام افتاده است.
پیش از این گزارش‌هایی درباره مین‌روبی آب‌های تنگه هرمز توسط ارتش آمریکا با استفاده از تجهیزاتی مانند شناورهای زیر آبی بدون سرنشین منتشر شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78279" target="_blank">📅 22:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78278">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulCR025nTjCCnMPRhEigBPLPh8zSbteZQZPNL_OzfgpVrB_09JD510SgvHSvjYorzfVPlO9w9C22rm2v3_piUlbxEre-ZUV73s1j5RVyiyRRABWIVBHFFA4cMrS0lhV0ueUffVKXNE5bf8gjlD6Ew4qpA1vA-isfK8NpH5xksKVvCt5QYH4aBgfnd9iUsf-GDflCgC6ghzUuWJhGvxI-J07A2QkK-cT6fCX-XQgAlx1ViaX_Jx5osDWrebTjZ1n6rd2QCx5KeT9eyzKCIumzCFnce4UdEAlq632_WFL3cpCoQYSvnvnLX3WIzpl3fz_T6Ux6O4GtZS_kGOX2OJSwMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای دولتی یمن روز سه‌شنبه ۱۷ شهریور خبر دادند یکی از فرماندهان ارشد حوثی‌ها را در جریان یک درگیری در استان تعز به اسارت گرفته‌اند.
منابع نظامی، این فرماندۀ حوثی را ابوعلی الاجنی، رئیس سازمان اطلاعات و شناسایی انصارالله، معرفی کرده‌اند که در یک درگیری سنگین در تعز در جنوب غربی یمن به اسارت درآمده است.
این چهرۀ مهم حوثی‌ها، که با وجود جایگاه نظامی‌اش در کادر رهبری حوثی‌ها جا ندارد، به همراه ۹ تن دیگر بازداشت شده است.
درگیری‌های سنگین در تعز از پنجشنبۀ گذشته در جریان بوده و تلفات زیادی به جا گذاشته است.
در همین حال مارکو روبیو وزیر خارجۀ آمریکا هم با اشاره به نقش نیابتی حوثی‌ها در قبال جمهوری اسلامی، گفت معتقد است که «دست ایران پشت بسیاری از حملات حوثی‌ها به عربستان سعودی مخفی است».
وزیر خارجۀ آمریکا با تأکید بر روابط دفاعی کشورش با عربستان سعودی، گفت واشینگتن تحولات یمن را از نزدیک زیر نظر دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78278" target="_blank">📅 22:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78277">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbFDxSCZIuCLisYfg1naXfKT9z-2-PvG0fuJKuweCdfprj9-0EqlLBgVso8w0bQCFjG6O-Zt10RYULYbclKMwIte5gCdxyIFDTI8S51AsDHEZNErMpoH8AFhaVnmUQnljAqJLT14GbKbDmxTOYZnAQUY8R-nACN_xPAF1qNu5XOLWWQzZXmpsiSejBcvdX2GDnjTRmS_eN-V3Aep2QlInePvnOpMSVXwP5L9P9STfkLEVanE0mvz08v1RjbLvY3VDzYfr-jQr4zTGk7WEgGY2VxOKE90ApVw5nwvokAxa61WvYO5HsQpwNnGzUNkL8mN6cmZ3nRj9EY4ADA7Es3dgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا، روز سه‌شنبه ۱۷ شهریور ۱۴۰۵، اعلام کرد در چارچوب «عملیات طرد اقتصادی»، ۳۶ شرکت و فرد مرتبط با بخش هوانوردی ایران را در فهرست تحریم‌های خود قرار داده است. این اقدام شامل ۲۷ شرکت هواپیمایی فعال در ایران و همچنین شماری از شرکت‌های واسطه، نمایندگان فروش و ارایه‌دهندگان خدمات باربری در کشورهای ثالث است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78277" target="_blank">📅 20:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78275">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bTJIsjRkC4u5UG0w28FCdxIwnsAn8cUB4WJlXyTfs-QPjoXFXJPI1YGCexnQVGmAK9NexJnNKu74pdoYNlmZbeyqsII96BPyX7dW_yB3x0Jej39MsElgtqXg4atnj2UupqjxGGGQ4JUgs2XqSx8yGR0DrSLeKotel841UnGgZ5IF81IG6Orb9tBpzfzuo7GoNqV577LcCssbDp6HAdjWjW2gV4ul968J4-BjBsGMhYjGqanJ3OAdHkZGVYgF_6i4I3__PNWj5w9fiuwjBwFU3v9HOQaNfSzJ22Tt4S4G_aPQbdGaKKBUMuBHdc9RkUjY39HelEIGpPXnei_2F1ypoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cbsY2r2d6wxlzUYYhWkjnCHyQ_XqZVnG_4-1AVZVTqNJucFxzPv6STQU2vIs7ezohC2mT4HSyk8tIXs8j50qBzhFAf3qsYmqKu8WWs9qk5oj_XzS8eIAI5CHjIDb_hwZerCO4oRdRU_WD8qZ-dNqDM4wuz4p1_G-1cIRb-4LGJBUu-cOvDXAv5ARaLUsrOMcN4I45efO5IPUBz2NcNTdk3dNFOPr0rfjVVYLD7EAFD1v22EUZXAePoGBZdB0qgYnjNoM4alcO0Ly7Ol6nKJJxbEMHO2OFkL89bVpFsbvIEtHBmu6ndrFQh3G8Lij7pFYQu96KhPA17zkfzvRXELUiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی، روز سه‌شنبه ۱۷ شهریور اعلام کرد که یک زیردریایی بدون سرنشین متعلق به ارتش آمریکا را در محدوده آب‌های تنگه هرمز توقیف کرده است.
سپاه پاسداران توقیف این زیردریایی را «غنیمت گرفتن» توصیف کرده و اعلام کرد که تا ساعاتی دیگر تصاویری از آن را منتشر خواهد کرد.
این زیردریایی هوشمند حدود ۵۸۰ سانتی‌متر طول و نزدیک به سه تن وزن دارد و می‌تواند تا ۱۰ روز بدون نیاز به بازگشت به مرکز هدایت، عملیات خود را ادامه دهد.
@
VahidOOnLine
روابط عمومی ارتش جمهوری اسلامی ایران، روز سه‌شنبه ۱۷ شهریور اعلام کرد که یک پهپاد MQ-1 در آسمان بندرعباس شناسایی شده و با شلیک سامانه پدافند هوایی ارتش، سرنگون شده است. این پهپاد تهاجمی از سوی ارتش آمریکا مورد استفاده قرار می‌گیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/78275" target="_blank">📅 18:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78274">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuff6dRe1D8qHP0_vJhW7o0JCM_OwrHDKOryL97KLURbBfQJ5e2jX6383XreRgEjeTE4puaTSdvyYLD48E7zwrROgkL7cMm40v6bHiIcxfKvY1UblUXhUvPq2dfNYg8PlU5uXcaA6qqZBsi6u5OrWb-rcHlywZ_qPEqNzfvXLy2Ed8SIj5NMt1wYaMnZxdHKE5J9a2wwhprBfnwWdsjTfUGJsQIeFf9fuloA5BkJcwVWEkSZheriJXFywT97NThWzG0kkPSONvKGAGXBkP-OiwQumiRUa4an-tjRbvElCwAsqYhU0OciKEMBz28qc8SlbvSION2EVGKeV72QGLLzkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبدالرئوف اسحاقی، فرمانده حوزه مقاومت بسیج پارود در شهرستان راسک استان سیستان و بلوچستان، روز سه‌شنبه ۱۷ شهریور در جریان حمله افراد ناشناس کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78274" target="_blank">📅 18:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78268">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sPSIBqb_0CLtWiPGybsUF8DgrNOOTb6m0fOG6ECtjvuWsTM3toQOpxG8Dt2TdQHjILakjqKmBnV5XJSEiKuk8dNvxnmU4rnkHpjvxVsfoVom9PnRAMuxYpjXhRS5xY16RBcnuwu3jiRN1SKW_gO8ytf-3I1UbHDUyl41nQEjDI96wOx8uGcx3q9eqwywahzQ3hrYTOuQcmcyXeGkD5YBVleABfjUQHWPwWeJkD63e1817f1ti6kvv8rv7E_V_0xK8ZISYoAfMt5cmB0PPozXidC0VykQs9rc-2qkIoSBVEV7VEZDNan90X38juODrNwVi6lJUv946UJYby3YD8n9IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JUmKNrGUtjyR-g3kDsI-wni4S5AZSvZgReC94f0rYLnpKKUIQ6A2m8WWnNw-anGRgdrnNuLHZDaJVepfrFbB6lz8xyRP6dM5FHjwNzLseBzXEnFDtX7PHQBrsEKLG4s_aa5dgeUFA9qnwkrWh8jvrO27Ve_o9ARaxKZa1pFL2ocEltJfnTEdJbSGJ63BhtnXrmPf1LEmx5l_wNCMMhGVaR-mVw_1hFB9vWJvpkVu3cXOA3mGfe8ahKNzJZPZcLsYk1IGBtXvWsUEoZmVzvb1W_xPPLfTApOoeh9XoMvNs-hCSlJxoonc7WNaWSoSCarPDx1rD6Uk8tFXhB62C73rWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gALQluVkM0hFO-NV6HOYhDjKjAZatBnZoJwDxWAF9OTpIca7PuYYURKQuZXSRfsZdElBciBQKY2TW22z88d8YU8XJDxCQjBw_kQQDaxHlu6Fbaouiwq0On2BFUxOSqlhqZcF8E3cjhQAkGKbGdBtcSdPeyeGviU-xsAPMG5VhcFvmL0dpH_Cc-TJ8mMTDfnsVsCdC41oH6wIJtX3Wtx5njfDwv660DdZakKrgHXOpcCZkoTC-ckvm9uSGwndTR3AJMzkuloHIDLHBQ2iZkq6WbWYhL825RH4W-7wsgyFw1BjqA7elkfDDwLd883RZ33sRyRwX3Yy2q_PEzz1xVUJEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ip9yBiWX9Y-CdnXrGOWgQLJ0Gj1gfjqoejivW_V_526fXksDvScHmLuY-U4jeC13EWI7zsJqI3GTIDpWUWnTry3fee8A-304KDMgt2vCSwasQJRUm1hy5TWl_0rY7FvFJFXEgsJnWvgioIcIE5CsqNgvpKL9RTBGwEjuzbtLsBybt6xywlwyE0b785zpYnuvU9320DdoUl_z6rrU3F6VlqwG8tYKC8SmAkZpQKK_FLNRCujgMTgV2hP1Vxnz_SP7l4K32OzvcxSMxQXMlNHMB60hUUWdkOC36ART75PGOAEut-jZ4SczunZOH17dBlYHGVsCZvHFSGg0c_BD2km5hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QdleWGHoWZuRdYUUP1ljnT2ebdXp0f5MM9DrkLCP6JGNGDn2Hs6LrlcxCKlvvMtldQBUsJCa9WIR-of8RDXVeNVAb2ezgQeaK1PIPCCwsktz00-IAn8t2RjlbGcJOhZL18BJ5kXm0L1iYyviUwSQ4p8CuWc4JCGBQbQ7E942NwFGJX0m4Xfrm5NENTHS9O1ErDJWdn0qw0r7VFK-V2tWDFio47TyXKK5R7qdU1CGr9DWVRFittesH4NUCVjCYeAFtRG1zd_Dma6zjzExPArnr3IV0Qx6FLI5rYXYTxfmhjMYZGkDRCwAZU-qmUPvpBnwvX14c_IgZH1SW95MdRxBYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e0b5c1294.mp4?token=U1_-m351lTkQ5MtABIXQl-rnQr6oBzv1MMOpf0byOOUnsZNUVv3bZj6qcOvpXHj6laOqylb4s_8KEzD7Ojs7TBLjA4TrR-Z3rHz39U9I-bHl8vrRChyOqwOqxHLX0gic-afSbtHcHNHH_vEyfaI3Qu4Qwu3luOcJCRyy4YcDXf7D2_3_nQBIxn0RVCVIJtKotFCzlpI7ayMI3kveysQxy56ESKO3XzP7luhKRjSfQIGnM2PedL6pSzYVn2G6OIchr38deuX9oLv_9YFVigGklZb7N7BlOXHFwBejejBo49q6Wb2WBJibyz9GpjUUgpfpEwQ1YGVDsEhmtuWSOM_tyw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e0b5c1294.mp4?token=U1_-m351lTkQ5MtABIXQl-rnQr6oBzv1MMOpf0byOOUnsZNUVv3bZj6qcOvpXHj6laOqylb4s_8KEzD7Ojs7TBLjA4TrR-Z3rHz39U9I-bHl8vrRChyOqwOqxHLX0gic-afSbtHcHNHH_vEyfaI3Qu4Qwu3luOcJCRyy4YcDXf7D2_3_nQBIxn0RVCVIJtKotFCzlpI7ayMI3kveysQxy56ESKO3XzP7luhKRjSfQIGnM2PedL6pSzYVn2G6OIchr38deuX9oLv_9YFVigGklZb7N7BlOXHFwBejejBo49q6Wb2WBJibyz9GpjUUgpfpEwQ1YGVDsEhmtuWSOM_tyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عرفان میرزایی، خواننده رپ ۲۱ ساله و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در زندان دستگرد اصفهان جان باخته است.
درباره چگونگی مرگ او دو روایت متفاوت منتشر شده؛ ایران‌وایر از اجرای حکم اعدام و ایندیپندنت فارسی از مرگ بر اثر شکنجه خبر داده است.
بر اساس گزارش ایران‌وایر، میرزایی پس از شناسایی در ارتباط با اعتراضات بازداشت و با اتهام «محاربه» به اعدام محکوم شد.
این رسانه می‌گوید حکم او روز یکشنبه ۱۵ شهریور بدون اطلاع قبلی خانواده اجرا شد و تلاش نزدیکانش برای جلوگیری از اعدام نیز نتیجه‌ای نداشت.
ایران‌وایر همچنین به نقل از منابع خود گزارش داده است که خانواده میرزایی پیش‌تر برای خودداری از اطلاع‌رسانی درباره پرونده و حکم اعدام تهدید شده بودند.
به گفته این منابع، آثار متعدد جراحت و کبودی نیز پس از مرگ بر بدن و صورت او مشاهده شده و پیکرش با محدودیت‌های امنیتی در روستای غرغن فریدن به خاک سپرده شده است.
در مقابل، ایندیپندنت فارسی به نقل از نزدیکان میرزایی روایت متفاوتی از مرگ او ارایه کرده و نوشته است که این جوان در نتیجه شکنجه و ضرب‌وجرح شدید در دوران بازداشت جان باخته است.
خانواده او گفته‌اند هنگام تحویل پیکر، شکستگی‌هایی در دست‌ها، پا و لگن مشاهده کرده‌اند که آن را ناشی از بدرفتاری در زندان می‌دانند.
بر اساس این گزارش، میرزایی اواخر فروردین ۱۴۰۵ در یک ایست بازرسی در شاهین‌شهر بازداشت شد؛ ماموران پس از بازرسی تلفن همراه او و مشاهده ویدیوهایی مرتبط با حضورش در اعتراضات، وی را به زندان دستگرد منتقل کردند. نزدیکانش می‌گویند او در ماه‌های بازداشت برای گرفتن اعتراف اجباری تحت فشار و شکنجه قرار داشته است.
دادبان تاکید می‌کند، تفاوت جدی میان دو روایت درباره علت مرگ عرفان میرزایی، ضرورت انجام تحقیقی مستقل، بی‌طرفانه و شفاف درباره مرگ او در بازداشت را دوچندان می‌کند. اصل ۳۸ قانون اساسی شکنجه برای گرفتن اقرار یا اطلاعات را ممنوع و اعتراف حاصل از اجبار را فاقد اعتبار می‌داند؛ ضمن آنکه هر مرگ مشکوک در زندان، به‌ویژه همراه با ادعای شکنجه و آثار جراحت، مستلزم بررسی موثر و پاسخگویی مسئولان است.
dadban4
دو منبع به ایران‌اینترنشنال گفتند دلیل جان‌باختن او، شکنجه شدید در زندان دستگرد اصفهان بوده است.
اطلاعات رسیده حاکی است پیکر او هنگام خاکسپاری، آثار متعدد شکنجه داشته و دست و صورت و لگن‌اش به شدت متورم بوده است.
بنا به اطلاعات رسیده، ماموران امنیتی به دلیل ترس از تجمع مردم، اجازه خاکسپاری عرفان میرزایی در اصفهان را ندادند و پیکر او روز دوشنبه ۱۶ شهریور در روستای غرغن شهرستان فریدن به خاک سپرده شد.
زمان دقیق بازداشت عرفان میرزایی مشخص نیست اما منابع می‌گویند که او در ارتباط با اعتراض‌های دی‌ماه بازداشت شده بود.
بنابر این اطلاعات، ماموران پس از بازداشت، ویدیویی را در تلفن همراه میرزایی پیدا کردند که درگیری میان معترضان و نیروهای حکومتی را نشان می‌داد و از آن به‌عنوان مدرکی علیه او در پرونده استفاده شده است.
iranintl.com
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/78268" target="_blank">📅 16:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78267">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tW0V9mMWsoy7TT2SjoslNcBJpEJqrLrFistYH9cTHg4_zEqkZRSD6txta46ZMyoTD1kaAM-sRxIqRSNQARcTat_7B46PXxG1WCE8MKOrl3QgTrMQJ6qz1UcV1C1qpfX8TprSU3vC7ixiseQqyaZfVWp3OEYLr_RD5Iz_AFX9zDnkecdlu7zB_XKM-ofJ0sliw_rvntzoLEE7zP0XOmpr1qluSM985UZSYnmwfjrQ7wDpRxVSp55Vf7zhIq7a0UQUD2ODZai418G17cgN9wv5Bswa_ekyccEU4gmcSH3MMpzk5in2ocxiqvC0ZIazBViRj1W5YEVkxp8w6aiiggPf2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش آسوشیتدپرس مقام‌های سعودی اعلام کردند موجی از حملات حوثی‌های مورد حمایت حکومت ایران به عربستان سعودی در ساعات اولیه روز سه‌شنبه، ۷۳ نفر را مجروح کرده است.
سرلشکر ترکی المالکی، سخنگوی ائتلاف به رهبری عربستان سعودی که در یمن می‌جنگد، گفت حوثی‌ها «تأسیسات غیرنظامی و اقتصادی» را در شهرهای ابها، جازان، نجران و خمیس مشیط در عربستان سعودی هدف قرار داده‌اند.
او گفت ائتلاف به رهبری عربستان سعودی «با نهایت قاطعیت، تمام اقدامات عملیاتی لازم را برای بازدارندگی شبه‌نظامیان تروریست حوثی» انجام خواهد داد.
به نوشته این خبرگزاری آمریکایی، این حملات در حالی صورت گرفته است که درگیری‌ها میان حوثی‌ها و نیروهای دولت یمن که مورد حمایت عربستان سعودی هستند، طی چند هفته گذشته تشدید شده است؛ درگیری‌هایی که آتش‌بس چهار ساله در جنگ داخلی یمن را از بین برده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/78267" target="_blank">📅 08:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78266">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W4Z7Sh7sqHMblUR24gDh4SiEdAKKo6UlrYugnzxoxUutIzqvvq9GoyZ7Uzwlf68jy58YZnMRuImcHSO3-13xscY1DyZ-scNX0Qaz6lz4DArm-7J3ANbDuq5guG6inh8DSAnUMdnPYTNEqIPEU8NoClS8GxRSildnl4kvjS2oGaMpSe8ocjvcSLoC3irOUmhHhz7jhssUaruTYj72s6MNq9qDswW0wISz4hz-k4ANVKR0hE14KCNecPQrinslrCpTxLFgbd92-JoJv8DUnznFeosSJnBgg6gO7cHBR3sgLT-b-SzWSb9pBIwUyQ-dWYd9bdzWf5kcFHnemCk4IPko_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
وقتی ما در جنگ با ایران پیروز شویم، قیمت نفت به‌شدت سقوط خواهد کرد؛ درست مثل هر چیز دیگری که دارد سقوط می‌کند (اما بیشتر!).
بنزین گالنی سه دلار، اما در نهایت به زیر دو دلار در هر گالن خواهد رسید.
همه این‌ها به‌سرعت اتفاق خواهد افتاد و ایران هرگز سلاح هسته‌ای نخواهد داشت.
MAGA!
رئیس‌جمهور DJT
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/78266" target="_blank">📅 04:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78265">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/980dd40283.mp4?token=YVnWA2DGfo4SREOa_4-QIYtmayGyRSeAnZqDy_FnYNRLM07izcfnHmSarTSknzl551K3s9Y4_umWxjLvA-0WANob1ewS0UZM71tD6vPmOuCU4LbzSriPdyd9QjGWqIXH_eHh3TA0TqXzyAo0P947os0cpPweoLK7UJCnLuHZCN9ygDBHctSJe9cF8dHuGsKawtNNSV77yIjQbvPezs4I2gZ-Fatmkw1-nLaCmEGwW7lU8N4nLFDRD0yFKwRqQYWd6OgGlFSPGWsS-EVjNkDzCSfL5Ipa4g_jNcPyPZFNT4K4XBMyEqPR9_IdyBCESP7V4lJiCCgT9H-LHBPNesA3vg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/980dd40283.mp4?token=YVnWA2DGfo4SREOa_4-QIYtmayGyRSeAnZqDy_FnYNRLM07izcfnHmSarTSknzl551K3s9Y4_umWxjLvA-0WANob1ewS0UZM71tD6vPmOuCU4LbzSriPdyd9QjGWqIXH_eHh3TA0TqXzyAo0P947os0cpPweoLK7UJCnLuHZCN9ygDBHctSJe9cF8dHuGsKawtNNSV77yIjQbvPezs4I2gZ-Fatmkw1-nLaCmEGwW7lU8N4nLFDRD0yFKwRqQYWd6OgGlFSPGWsS-EVjNkDzCSfL5Ipa4g_jNcPyPZFNT4K4XBMyEqPR9_IdyBCESP7V4lJiCCgT9H-LHBPNesA3vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجید ابن‌الرضا، سرپرست وزارت دفاع، مدعی شده است که نیروهای نظامی این کشور توانایی هدف قرار دادن ناوهای رزمی آمریکا را دارند.
روز گذشته محسن رضایی نیز گفت: برای اولین بار موشک ضدناوشکن را بالای سر یک ناو آمریکایی آزمایش کردیم. این موشک خاص، جهنمی برای آمریکایی‌ها به وجود آورد و فرار کردند.
فرماندهی مرکزی ارتش آمریکا - سنتکام - روز گذشته در
پستی که در شبکه ایکس منتشر کرد
تلویحا به حمله به دو ناو خود اشاره کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/78265" target="_blank">📅 04:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78264">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G9gUurfSGj2ucAHdD8MJA2N695SKba2Rf6sy5Fwc4VKhu5h31gAIL7d_SnKXTKKHqA4WyllQGODTApaaPzGXbXdRfi4oE1qub6RqoWFTsDSfo2JJU4FGhUo2JPxvy1gEqj21zXXXvUua0RQbd9zSiPkQHzLTVHXqkU7oFNQtAwp4XRSjEbZQ1ylvAEalWOO1xtbRT_G-gHF2KTUqqVTKklenOvVh3c3PgPHQLJl_3ecSq7GfxFpfm9Cau5KBIlheU5ojHSRfu0bmHSwJuBji5BQAh_o7p9RUyQA2RFPGKDT0k5ebr_PMk7aZ_u1NsHpwwdLMmc9R_mkCxIsCl7xQlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانیال کریمی، پدر امیرمحمد کریمی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴ در مرودشت، روز ۱۵ شهریور به زندگی خود پایان داد.
امیرمحمد کریمی، فرزند ۱۹ ساله او، ورزشکار و عضو سابق تیم ملی نوجوانان تکواندو ایران بود که ۱۹ دی‌ماه ۱۴۰۴ در جریان اعتراضات مرودشت با اصابت گلوله کشته شد.
پیکر او در روستای جونجان از توابع مرودشت به خاک سپرده شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 449K · <a href="https://t.me/VahidOnline/78264" target="_blank">📅 19:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78263">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsDOz0mo6EN6kZtP4hFM8sYzfmZMqpk4pGP5YaTAo3cY9aEbahjWxWtSNjAyvdXBMmUIpCiJLpWiBe3TQbdTNF1kXlFOsu3rq4Ow1O8ulfpgwEFDQPA0pwuxJHSQEMxizQLjKM_CTqv87uwK43u_IW_V5XAe336EChQZKaMjyyCJsP_XAlE6cZjvGyTriARUIIZg_ClEIbM3-lujOtnZBrYU9A4worj7bZIfemdPMXpoL2aBdByuEhiGFTP4XtzXwtuPFNyO1Fq-gsR-ohF-XKznJ8vzTe9XHdZYJGb-E18lS1q9YR4BBDH6Wznj1R723MKlzzTuz36ZoRvpA-hhjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیدا حیدری، نامزد ابوالفضل سلیمانی الموتی، از جان‌باختگان اعتراضات دی‌ماه، روز پنج‌شنبه ۱۲ شهریور ۱۴۰۵ به زندگی خود پایان داد.
منابع حقوق بشری ایران، به نقل از خانواده آیدا حیدری نوشته‌اند که این جوان ۲۵ ساله، حدود هشت ماه پس‌از کشته‌شدن نامزدش جان خود را گرفته است.
خانواده آیدا حیدری گفته‌اند که آیدا و ابوالفضل قرار بود همین ماه مراسم ازدواج خود را برگزار کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 457K · <a href="https://t.me/VahidOnline/78263" target="_blank">📅 19:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78261">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LP5dZuVQtt-doacpckLJtvrnclqoAShA6sDP05FLq8Fw-9PS3Io6kqKYwGaDi3yKAqk7MsqNVPKecpwCx6TGR7ET_Vkmc7qL4IBbZfgnigGUNuhzR-_FAjCO2EXX4RGeS_qK6RI3WQqUfk2_UwjqUYO6eJVRnHP9R9-NZpkrVTTvrt51BV8PEJhKOEmosLvs4qrSKYyDbGp_fa8cQTRp3Tk6r8ojO4sSwbFcoscDH8jClxBUA4-2DCSQoho5c7QzKLXuzivKnIENhYcWKyW1pVBeMW0QqnkhVGqIqqgTwLqP7KHFaEDzXq5sNglyUQQHUknuhXf_hHn66BGAMAQRWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ تصویری ساخته‌شده با هوش مصنوعی از حمله جنگنده‌های آمریکایی به جزیره خارک در تروث‌سوشال منتشر کرد که روی آن عبارت «خداحافظ خارک» نوشته شده است.
realDonaldTrump
رییس‌جمهوری آمریکا چند تصویر دیگر نیز در این شبکه اجتماعی منتشر کرد؛ یک نمودار آماری که روی آن نوشته شده «ارزش پول ایران از بین رفته است»، دیگری نموداری که روی آن نوشته شده «ایران با یک ابرتورم مواجه است» و نمودار سوم که روی آن نوشته شده «صادرات نفت ایران سقوط کرده است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 453K · <a href="https://t.me/VahidOnline/78261" target="_blank">📅 22:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78260">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 437K · <a href="https://t.me/VahidOnline/78260" target="_blank">📅 22:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78259">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jrtu18D7MmwP8g406edRotqoVH8e8vMYNtG0I_6bXL3SXqn7qureI4FYv7IKDUw17DcmGL2nrqJGYpi0z-T7reWSeryA4kxF7_XrrfzzldiGP0VD0UZPNj4OlfPwtIreR9zSf8FC9kOAyzsnv_b7g5bsrotJ9d72sU8Ancrlic7Oi7qsnqSV5j1V74uKms-9i6qPxMByTwxe5_55685ceid4kPzzGcTEnh6kZAxdZaI7Tg54wfr2JB1Yx2LnA9eeESWHf3aS4fOpbayWE4mT02bOrohxYgrGz2cvLe3eztXByWCQY_d9xoMz32KVBlEU2mcbCTSmunstSbJQ_K0LhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 432K · <a href="https://t.me/VahidOnline/78259" target="_blank">📅 21:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78258">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4f1fd10186.mp4?token=rEEVM9yaEApmQNbN6vFm-j8GtMzw2E7GomgPHKWH7rY-Xj55iXPVjSqYskC9tPlJP5cX7pg9IWlyLtDaR3z5dnEwZSXsfQVyWW3Qal36fc7BXUokkQH06IiNdCvSpdbHTKye0LRvVfnGY4D8xYjh21AjMaIJFM9uJkZT-eTdLQ_Avd_YZ_P6jYanP-z5q2x69rMz1bVtHDOFdwlVdw0xzcKyA26Q5eH3F4LivegkN2fwa9SZn6qGQf8U-W0Mr7qpMNJuXYvydVySG8jyCmKLhRDJfx5XxA64na0LocHeBMfpTXodKB6CkKLc4mbhGoM1GjjZFK1YDlfcWaFpDE3BRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4f1fd10186.mp4?token=rEEVM9yaEApmQNbN6vFm-j8GtMzw2E7GomgPHKWH7rY-Xj55iXPVjSqYskC9tPlJP5cX7pg9IWlyLtDaR3z5dnEwZSXsfQVyWW3Qal36fc7BXUokkQH06IiNdCvSpdbHTKye0LRvVfnGY4D8xYjh21AjMaIJFM9uJkZT-eTdLQ_Avd_YZ_P6jYanP-z5q2x69rMz1bVtHDOFdwlVdw0xzcKyA26Q5eH3F4LivegkN2fwa9SZn6qGQf8U-W0Mr7qpMNJuXYvydVySG8jyCmKLhRDJfx5XxA64na0LocHeBMfpTXodKB6CkKLc4mbhGoM1GjjZFK1YDlfcWaFpDE3BRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نرخ سوم بنزین به ۱۰ هزارتومان افزایش یافت
فاطمه مهاجرانی، سخنگوی دولت گفت نرخ سوم بنزین از بامداد ۱۷ شهریور به لیتری ۱۰ هزار تومان افزایش می‌یابد.
سهمیه ماهانه ۶۰ لیتر بنزین با نرخ لیتری ۱۵۰۰ تومان و ۵۰ لیتر با نرخ لیتری ۳۰۰۰ تومان بدون تغییر باقی می‌ماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/78258" target="_blank">📅 21:41 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
