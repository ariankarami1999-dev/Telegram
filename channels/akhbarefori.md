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
<img src="https://cdn4.telesco.pe/file/GF-xu6iFIVpSV9z7HIaSBtJY3D--QlQqFiEHza23tlxtv_Tpy5G8oEHBfyyYCJjUl_o9zS3IeFkpcUukoqxQs8SQoZ4G64ApaTyj5B2pn869DMyhC7TQn4IJigR3dSW1KURFIRfTRP0c_yL8p2o2uB0BcA4aSA_gAIUP03zpWQTCKbh0WS6c5mufhtn0vtGB9l8SAI-FXi_KzKEY2_nIRZYLakqNt-XU3tROjkshUmDk4Jm7x1-E6K1JtnEt-AkSVChHQ91qxDQpTxKbfvQbYuRzR9FcZY8KByvn-9ZZ2VJxErCIhzzfh4UcQV3j3pLC8HTbrgrXOk4G8pDhycXnag.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.29M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 19:28:13</div>
<hr>

<div class="tg-post" id="msg-663226">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔹
نتانیاهو: نیروهای اسرائیلی در جنوب لبنان آزادی عمل کامل برای مقابله با هرگونه تهدید دارند و حضور نظامی در کمربند امنیتی ادامه خواهد یافت #Demon
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/663226" target="_blank">📅 19:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663225">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dx9WRA4Ge33pIOUfz2_TMHB5BFQ0PP3U4Do5L04qAbroCDHwcO3oP6X5EAYGvNnwKtwdnXyvhKfD4Z82PaRYfrLLlmrcMrLUdVwXPG94-H_59RFavPhuoD4k256JNAN3HyY9ulR24_BVZ1TGYwljwYxAVeguiA1Zo40wfSsjjdYYJxLL7j_ccDlXTXlt-9jciMi_ZJ1SlIiTGSR61u-vyqah_V1xGaUkbGGwlpKus8B3Cm9NqV6An48PQd5BlLomjuyjmMMefl63AmCntG_YEMn5VRo5Oun4ft5qaWYZCPuf_tp5AS2uitiL0Nk0myPajD9BOto4Zjls1JnFMqqcHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
جادوگر مشهور آفریقایی کیست؟ / ماجرای جادوگر غنایی که بازیکنان را طلسم می‌کند/ جادوی سیاه چیست و چگونه کار می کند؟
🔹
انگلیسی های خرافاتی به شدت مجذوب نانا کواکو بونسام شدند. طبق گزارش رسانه های انگلیسی، هزاران انگلیسی به دنبال پیدا کردن شماره یا آدرس جادوگر غنایی هستند تا با کمک طلسم های او بتوانند مشکلاتشان را حل کنند.
در خبرفوری،بخوانید
👇
khabarfoori.com/fa/tiny/news-3225623</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/akhbarefori/663225" target="_blank">📅 19:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663224">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔹
نتانیاهو: نیروهای اسرائیلی در جنوب لبنان آزادی عمل کامل برای مقابله با هرگونه تهدید دارند و حضور نظامی در کمربند امنیتی ادامه خواهد یافت
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/663224" target="_blank">📅 19:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663223">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXVRSl7cyEtY0k1-DL5cUV03lcOjLL0MLmzacVJtneKbR_zisXiMSPfCrai1noMxFiR4bVcbVsPsRl8OTVxACJASy_46hqjSkYYaqjPaPsyvonhw_By6Y0d4KpHFPX3L8xcR4ziZ2EWyzZT_X30aKcftk6LgtXk9OU1gk4Dl3TRQluOzM4iAcCWD3oLmBiam3zLqNDvvM8i2Xe6XJKZLj7pAEDDBmVP6OXb9jQUN7ARlRDogUDM7cA-UfNI4hhcF7NHpUUcBJmzHJpDaq2Z3BT0oX1X_yF2wf1zdVOiB4HX_RIJPhUIgH2Dxif-FqRcYvMIuo89Atz69xkiwJGrO-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/663223" target="_blank">📅 19:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663222">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔹
ملی‌پوشان والیبال با مچ‌بند مشکی و شعار «ای ایران» به مصاف آمریکا رفتند #ورزشی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/663222" target="_blank">📅 19:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663221">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔹
گزارش‌ها از وقوع حادثه دریایی در سواحل عمان
🔹
منابع خبری گزارش دادند یک کشتی باری در فاصله ۷.۵ مایل دریایی جنوب شرقی منطقه «داهیت» عمان هدف اصابت پرتابه قرار گرفت و دچار خسارت شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/663221" target="_blank">📅 18:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663220">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/329af23c18.mp4?token=fFq45O0CBpk9RJx8vdkbY6xjAYY0CPBOk03vE7b4rzAXGK8llj8qL9Pw4oFVwCNvP7frBr-DnlI91t9g-Qc0Fpy9p73bDtbvCJ-duggvB7SKycGwD641-YRYDvpHELCoaKlV6ayEc5hnZz_-ccQlViCr9DcpYiocEsL0PT2Ht6WnhjQZGGuYa9tzdpm4VCL2XL1fiHmLCnc6sU6-Lujmghy5Qij9HAL-wb8u7vSAhxph3T-a_ahlD35yyU-DnGCUION2bJrUanI7wIfdnH07DRYZ2fPaT8xvKbuNMD9KB5Ku0RHodA5PJ_Psr-0xcRkbrZjSvO0KjixSp0NLlBjjpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/329af23c18.mp4?token=fFq45O0CBpk9RJx8vdkbY6xjAYY0CPBOk03vE7b4rzAXGK8llj8qL9Pw4oFVwCNvP7frBr-DnlI91t9g-Qc0Fpy9p73bDtbvCJ-duggvB7SKycGwD641-YRYDvpHELCoaKlV6ayEc5hnZz_-ccQlViCr9DcpYiocEsL0PT2Ht6WnhjQZGGuYa9tzdpm4VCL2XL1fiHmLCnc6sU6-Lujmghy5Qij9HAL-wb8u7vSAhxph3T-a_ahlD35yyU-DnGCUION2bJrUanI7wIfdnH07DRYZ2fPaT8xvKbuNMD9KB5Ku0RHodA5PJ_Psr-0xcRkbrZjSvO0KjixSp0NLlBjjpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ملی‌پوشان والیبال با مچ‌بند مشکی و شعار «ای ایران» به مصاف آمریکا رفتند
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/663220" target="_blank">📅 18:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663219">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f38b22475.mp4?token=joO0QsAtQpfKPEha3Nd74A0czlwrNFkgGxGaBLsx06KH_DmwovE1CetWd6l-C6G2dggCrJqK-VCb_Wu2DFVLb6uEt5lgJVzVE08wGeZaEJV3AMm3EOpvAbE6PXg_DFURzLd4DvKT1h07ERDpTNQbC19F7Gs5Vdo8UfQqfi7oKrIbt6_x5PgYR0NNAlYbtiHgqSzCRs3iqTD9vhrhT0LQXiGWfEXwb5B7vcYLQKP9ePBg4zSaMNVra8GhEAqou5Upt660W9ujFHhRHgFe0b2waetGKrCFWnRXpQNBhZ6rGrhSxod4IFMKa44IaZsLyc26-RXsIXo_qfFgV0dmBQ-Dbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f38b22475.mp4?token=joO0QsAtQpfKPEha3Nd74A0czlwrNFkgGxGaBLsx06KH_DmwovE1CetWd6l-C6G2dggCrJqK-VCb_Wu2DFVLb6uEt5lgJVzVE08wGeZaEJV3AMm3EOpvAbE6PXg_DFURzLd4DvKT1h07ERDpTNQbC19F7Gs5Vdo8UfQqfi7oKrIbt6_x5PgYR0NNAlYbtiHgqSzCRs3iqTD9vhrhT0LQXiGWfEXwb5B7vcYLQKP9ePBg4zSaMNVra8GhEAqou5Upt660W9ujFHhRHgFe0b2waetGKrCFWnRXpQNBhZ6rGrhSxod4IFMKa44IaZsLyc26-RXsIXo_qfFgV0dmBQ-Dbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ویدیویی از زلزله ۷ ریشتری ژاپن که صبح امروز اتفاق افتاد
🔹
هنوز جزئیاتی از خسارات احتمالی این حادثه منتشر نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/663219" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663218">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFigtNwqyAZQsJEXm9KI-JpDjNiEJTUGx1K09Hd5qyBUkV6-NNpUYlgw0a8lkPnxCrLYtoZNdfEppTf7EqhnGyTx2uV47I60E8WDEn8ww1T1XGdCHdONm9Y3f3GtdEAByopRwABIDmag75QMml8H93AGrunQK64fBKSlAWecshsL9gEw2ECf2kVgvifm9jNzw_SRnkjVUhyo2ZPDlN_V6k8XzP0268mMJq_fXvobPe7Fas6-R_e4enbQkbMTv1uUxQvrH2RD0NN3GrdL8Grn-a6OpVB-EIGtAzvO2nXbrOWZr-UDIxmhILQ-uWIH9XUtqpyYam7wjnngFQdqdhuGxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
توافق ایران و عمان برای تعیین چارچوب اداره تنگه هرمز
🔹
در تماس تلفنی میان وزرای امور خارجه ایران و عمان، دو کشور توافق کردند که گفت‌وگوهایی را با هدف «تعیین چارچوب اداره آینده و خدمات دریایی در تنگه هرمز» آغاز کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/663218" target="_blank">📅 18:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663217">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1PANeAU6g0k6lQUcKr1XYdmo-Qxu9do1g85AYzDm4jwCXx46S1OkOcN9Zoskah_DtNYHP-8sh4E224issCAW7dQLexwb0UuhqpXCmYwnIjOwSDeKovLjDNwichx2h_DiQpZaetsqD6LogQXQuYMpBx2ZByvF58rMx5nKa1Tpg00w69mMpEzOim6YrNO04f3lKuC-94ookstPgsq334tlh8Zn3TbmR3MAQykhjtk4q1SWOLD8MRPTToNIPnYI3t6mhEIUrwv5H6rfD5loCYmp769wjFysuVMwJPpnlR86kng7jBwAtHvB13wQGZZY0l5_Rp6f-8qSyaOXYGepm0LLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
گزارش‌ها از وقوع حادثه دریایی در سواحل عمان
🔹
منابع خبری گزارش دادند یک کشتی باری در فاصله ۷.۵ مایل دریایی جنوب شرقی منطقه «داهیت» عمان هدف اصابت پرتابه قرار گرفت و دچار خسارت شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/663217" target="_blank">📅 18:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663211">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MgSYexz_vwAz5yjiCynA9DH83dw-sB8rP8vOvE2kWRF57FQ1eU-o7s0Z2qWs8poAUI-EHz6Lt6K0uuHU6rdAgr1Z6SbQWHajmu6UM7Eq-l5oTRjo4awhRtQ62UGAczZ0hIZ1CI7ZHQOYVB_1fnuaQZeEBrtaAoVqDvCnyk1jDUwLs64gZB3qK-ABsKMEwb-zcLKe5rE4Ui6HDY-ZFSRNdGu7IMPgnVU-TkJIu2hZ_3iKOf7SjrAuL_EdprU2bUeztzmAOlOeMd6kyJPlOEnzRtyL1zEEwxsX2sDSu3Rn9YMbVzEh7-lZwd3BJ52ru1GMleLAkDKWx9GVOjLpXbRBlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UeUAmXpceufRqzA0-d2BForVIirYADndyC2RRc4X-6Ll-uZ8psZM_gavQNgN5JZaJMaOt1aFf38M__oH_zpSmT7eaffLz-NQlUfwjSD_KV6a8gGy7_aXDhO3jOmuGT9xPJfcMdPXmL0s9lO6U65udeb_Y1Pf75599kMyQzfIuH_oFzrAffw8dXdxYsM8ENb7S5wZbvD6-2Fsi2MeCV8kOQyxhxPEjtlc5_oGDsoWROrJY42g31lflSb4dsv3O5Jw_kPpHFxBrGBeG8l292nfe2PPIX_lPaQNUycio6gEmAqpFTPwN08fy_B_nHUpUrghLY9SAXMbsVWFHD4BIxZfSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xrmqas7PM5DP8DfTn0H-4Eu3_kvpPGwS7VA3TMTzqhbxFR0TxKbGwwFZsPOXJ415kZ3MBLli0D2a-wgLXcgtfUNYwHDuDTmUnXKdWGJ5aS9RzXws4VHUe9BYJjMezJSw4Ddc0RwiEdnAEHZ-e0IdA0-282Fw6RIvUDWm-TF0VkCtxs1JI00UOjvBBe910m_269Ty4i4NzttOMsz65QFMdCEomqFb0E2EqMI2DsqGVjCTQBu2wlCElz6Bpj5iJ3tN3ZA4-GMNwBhHS0VS2JNl7QCY3NqpRfs-HMg2AtxdlC9vv9ULbZbW-PwWZGzqI4LHss2u34mGLB2TeI7T1klSBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vfRdYB3_gMK62MpR8N8g2PCY-SVp00qeJOhRdS6c7QXSE06dQeWFOIV-F526vtyZ6NfZ482SSGc-LmT3KUCzFmmMqsya_uxj5tgJOH2sP_ROJw_akvK8plAP2qkROsFjMD5xohWYouYDVG0_fwbxjAmg2biLmvZR1TU243vFD50ZlE-H0v5COj_0XpwThvz42OYTtjtATgwgS3rf3-_YYMByZwzVjP2IkrXllsYiJ1Q0mNrh9EBgjqhG73NLHJm7LzVqQdcqsm1-WmARLgaFcoO4_hKn4EnDXR97-tvdQ6Ocn6pdVqK42Pjj_6M19nZwcHnmRjUSIbV4vH8Ged7SXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sf-cdkIEN-mOIsCpePIPPCj5Lj1RiaPke9V2ZQuG4Xf9TKuMJIDgr-mNAdAX8E5S8pJ4Mld3Z4zHRWogvLJEar-FP-Mu_OAXLkUHKDhwWuDgFKq0SPMW1XuO7k3aPkPwNnUwtFyCvJPWsQRmwEVv7nSa1KsyJun018X_zR4YdoOSV6RdUPz_b7r0Qgy0NXwhwCOrHOa_DsoeG6_ue7NgtiulKOIpIzdc5hKE63CoBrejSfrmO2l7J604Ej_sAOMeC_FZHMtuJPaqRPZNIGN6TlUFtvX2wtvT286sfYm2z1l8BW1A1kQAijKjzLA8y5Dmx2qVzoy_AGdKQsjYBUpEuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
مفقود شدن بیش از ۲۱ هزار نفر در زلزله‌های ونزوئلا
🔹
در پی وقوع زمین‌لرزه‌های ویرانگر در ونزوئلا، گزارش‌های اولیه از ناپدید شدن بیش از ۲۱ هزار نفر حکایت دارد. عملیات جست‌وجو برای یافتن مفقودشدگان این حادثه همچنان ادامه دارد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/663211" target="_blank">📅 18:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663210">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ادعای وال‌استریت ژورنال درباره طرح ایران برای دریافت عوارض در تنگه هرمز
وال‌استریت ژورنال:
🔹
ایران قصد دارد با دریافت هزینه بابت خدمات امنیتی و زیست‌محیطی از کشتی‌ها در تنگه هرمز، سالانه ۴۰ میلیارد دلار درآمد کسب کند.
🔹
این طرح با مخالفت آمریکا، عمان و برخی کشورهای منطقه که بر رایگان بودن آب‌راه‌های بین‌المللی تأکید دارند، روبرو شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/663210" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663209">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔹
ادعای یدیعوت آحارانوت به نقل از یک مقام صهیونیست: نتانیاهو موفق شد ترامپ را متقاعد کند که اسرائیل را از جنوب لبنان خارج نکند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/663209" target="_blank">📅 18:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663208">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeAQDeZXaDbnMAg7KZvaxtM53ezWYUtDAUOpHYiIVnE25oHrotHr9alqgOm7sO4sehU4PRJk5roZUdWeyuJfwUBEv2f1Vcrp2nuKJv38eO8BVpHexp699K2Jz_Rdo1oAa37T8lx129CA0-xm52nSAXrlCsvGPmL5hK_gHVXevr1sNOwWXy52A4U-JMMIJZJARYmsJ5JlhFyUBzJkhhsag5a7aQUCFVRoI_UYaoXez4BH5aMEianrWWv4uSll86ajbtS5Xk93byjqIsMhzLekv0xaSYi_su1tWqhmGS9VJOQ-97giGbNHsh1G0Ybg52IU0KytTlFM73q2mnhRTfHDfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
لیگ ملت‌های والیبال؛ ترکیب شروع کننده ایران مقابل آمریکا
🔹
بازی ایران - آمریکا امروز ساعت ١۸:٣٠ برگزار می‌شود.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/663208" target="_blank">📅 18:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663206">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b88b3e8d1.mp4?token=scG3L1VJ0a-85K4zXTgFdASjXReOKRRsjbUN0KXFFgPnUVxleFFRYfVEM_NJ0xCqaQRsZln7TDIwbhZcBlkIPJdubXF3TTCdaZ2syqygdlUYj-ykXUNVUAwuD9S-YoA0Gm5EaYFYVDV5-vir3NREEofZGwVWM9Z9KpG4SWI4o1q0F5fjmKMTdzQ5X_jrPM-Q3-v44iUUdAmHKfFYmpqAc61dMPbPqvJXOtHUp_H19AClfb5PZzYflpngA8mFRVEw259xRYfAv0-uimrZYoWsxd2ox1WYVHjUr16_YQjoL5hIqfFNRuj4vkZJda2iedIna24jCuebtStj1P_sBOMxbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b88b3e8d1.mp4?token=scG3L1VJ0a-85K4zXTgFdASjXReOKRRsjbUN0KXFFgPnUVxleFFRYfVEM_NJ0xCqaQRsZln7TDIwbhZcBlkIPJdubXF3TTCdaZ2syqygdlUYj-ykXUNVUAwuD9S-YoA0Gm5EaYFYVDV5-vir3NREEofZGwVWM9Z9KpG4SWI4o1q0F5fjmKMTdzQ5X_jrPM-Q3-v44iUUdAmHKfFYmpqAc61dMPbPqvJXOtHUp_H19AClfb5PZzYflpngA8mFRVEw259xRYfAv0-uimrZYoWsxd2ox1WYVHjUr16_YQjoL5hIqfFNRuj4vkZJda2iedIna24jCuebtStj1P_sBOMxbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
فیلم رنگی از عزاداری ظهر عاشورا در سبزه میدان تهران سال ۱۳۱۰
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/663206" target="_blank">📅 18:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663205">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbLIKuKl6cW0bkAO7NNt0AkUKTvagJbxv207StYAuQkS2pCmddq6l9VQ3A8QLSjtch6bJZIosFXlRkOqX5zDMh6VyupoRTOh5q9BfzYJo-MUQwB7SDWMc2btO8VS1iyDYQTxHNTfi5eYOOPFEHJLmXH6o-zVQM3ejIsmc7rjfxBjuoXSG7zUAz7P7CFI6oy5zikaOV9aaW8xstzU9hFq9QGYPFw0puS7dHXEdAQCav4qC5UcC3riH_yc5wkKMK8kozCt5PkFUG5Rdjtrila1WNM7RC-Jr5ocSMW17MbrY4Xz24HkXAhK566Rf5rVz8eG_DwRhI9MHJVzzTOy7oOpTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
مردی که راز بزرگ پوتین را فاش کرد، به شکل مشکوکی جان باخت
🔹
خبرنگاری که برای نخستین بار شایعات مربوط به رابطه پنهانی میان ولادیمیر پوتین و آلینا کابایوا را رسانه‌ای کرده بود، در شرایطی مرموز درگذشت.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3225606</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/663205" target="_blank">📅 18:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663204">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-SUnRkpWaYWK7TGsbDo7wKqAyYcTWwNvGTWP31bgCRpVIvP8BAzbAhCWtW6mfaVgjZVCdCbXVgdANfbi2JgCvSFFBiAim3Xcwpy0K-A_ijTm4uZo_bF6WCDJM7uym0Bpx_YpvrKsIHveGLF6qIFB_m6RRMkcXRRF-90llE3Vi9bkPOCCAHvvp01W2kBhl5W4LOrGF8lZ1ad23C0s7BKl_0fpi1AW2tnxWLowAxClBpVJbhX4fxYobGNdZWd4hqgLdzzMy3n0rUxpRMQqzqxizlL4NriYaGflKE_BDLugTCcigsaBanC0rv80V_gx4c2hb8Nhj2QhtdFUt3Mi8gG5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سقوط ۵ درصدی بیت‌کوین در ۳۰ دقیقه؛ پایین‌ترین سطح در ۲۱ ماه اخیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/663204" target="_blank">📅 18:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663203">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/391d9fa18f.mp4?token=NtPLjqqGx6mnGx7ODto_rHeeVhBH7n98YtWFgrQBamE0YwM6Fw7hoKfixRH-lMaXnI4Yaav0dcFq8BN_ntn1KKU54YG_0khTU5YbFz5kAkSTk-QoLTLhoJPLcusl2gKiYDkSoxGROKJPVLC5cAUWSRTnE_TYuLZ0c00VgPYgdNL2vVbw-7JnqdvMSYBUQuOMT9esmSyGE6qb6Bxg9pXBbhQfqI_pMCHrFQyEynODVFtaD-ouBXKEVz2pVsHBsIJkcyITaLMJZML38JOOVXTlPa8Jbo6NikQEVbpDXC4uyZ1BzjLWbNb9V2_oSDog2UPGUmFb2pPkdFVHYXI5ZfPWgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/391d9fa18f.mp4?token=NtPLjqqGx6mnGx7ODto_rHeeVhBH7n98YtWFgrQBamE0YwM6Fw7hoKfixRH-lMaXnI4Yaav0dcFq8BN_ntn1KKU54YG_0khTU5YbFz5kAkSTk-QoLTLhoJPLcusl2gKiYDkSoxGROKJPVLC5cAUWSRTnE_TYuLZ0c00VgPYgdNL2vVbw-7JnqdvMSYBUQuOMT9esmSyGE6qb6Bxg9pXBbhQfqI_pMCHrFQyEynODVFtaD-ouBXKEVz2pVsHBsIJkcyITaLMJZML38JOOVXTlPa8Jbo6NikQEVbpDXC4uyZ1BzjLWbNb9V2_oSDog2UPGUmFb2pPkdFVHYXI5ZfPWgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
خاطره‌ مداح معروف از رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/663203" target="_blank">📅 17:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663202">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf02b627be.mp4?token=e4vUV8lZ_bmO-OxoU228csUbXBdpfDfeLlp5ts7DzN_KjWpjVdUt3o_Gb2CuKKtfE26KCRJUYRbkj29n2Cj2E0263RLRyDvsh70TFjLwiwkkmroIg6ileUMMKUeW45AvZJQf9nL-zhSbuHaKT-3lpgc2JHu7H_TJ_0_7e4ZbnlFKBwcb871LZ8kKDQ6e9IX6CZfljjOQK4fUpwAf_PvXUKXsW-VMwkwCbbBLBi4pel39q1RkIuLp0tMgH7Vt3BZ1h7ExLxovlDgM8po48-Wo4Js2F8pf6sjlnjHURHJ6zn-H0mUiRqk83YvG2zlRKH94VO2qbtqJTXVXmaNm-Ky-pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf02b627be.mp4?token=e4vUV8lZ_bmO-OxoU228csUbXBdpfDfeLlp5ts7DzN_KjWpjVdUt3o_Gb2CuKKtfE26KCRJUYRbkj29n2Cj2E0263RLRyDvsh70TFjLwiwkkmroIg6ileUMMKUeW45AvZJQf9nL-zhSbuHaKT-3lpgc2JHu7H_TJ_0_7e4ZbnlFKBwcb871LZ8kKDQ6e9IX6CZfljjOQK4fUpwAf_PvXUKXsW-VMwkwCbbBLBi4pel39q1RkIuLp0tMgH7Vt3BZ1h7ExLxovlDgM8po48-Wo4Js2F8pf6sjlnjHURHJ6zn-H0mUiRqk83YvG2zlRKH94VO2qbtqJTXVXmaNm-Ky-pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
دلسی رودریگز، رئیس‌جمهور موقت ونزوئلا، از افزایش شمار کشته‌شدگان به ۱۶۴ نفر خبر داد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/663202" target="_blank">📅 17:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663201">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b20ce1d3e.mp4?token=P9HTXVM9bztDC89oQJfGql140vAsXQeCyx_2LPXgwqSLMrsJojVGRcPlV08s5Bqu8pIYmhgjqWqs2EdzJ6WnbfXR2p6gFIB-qEn4lWBS63P42JwWo4LxYcY9gRSpOiS4GRbQeCHaJEM6ABp2dMtRVYA0tkH6KkhXJ8zrkMHARXg1dzHeIo9rcxU0yYx_HrzoDV-sB8pTlXRa7S8kl6UjIMifaPHiV3k98GoittvqIxJeX6Fck770SYqALlSk9_nMDJ7X2w6t1OxncGxmUT2UEoFqz2_iqcYUpnUTB1iieaTQB3rMLZjYWvS9xQB6duZejaaq_YOZgmyxi3lcXfArPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b20ce1d3e.mp4?token=P9HTXVM9bztDC89oQJfGql140vAsXQeCyx_2LPXgwqSLMrsJojVGRcPlV08s5Bqu8pIYmhgjqWqs2EdzJ6WnbfXR2p6gFIB-qEn4lWBS63P42JwWo4LxYcY9gRSpOiS4GRbQeCHaJEM6ABp2dMtRVYA0tkH6KkhXJ8zrkMHARXg1dzHeIo9rcxU0yYx_HrzoDV-sB8pTlXRa7S8kl6UjIMifaPHiV3k98GoittvqIxJeX6Fck770SYqALlSk9_nMDJ7X2w6t1OxncGxmUT2UEoFqz2_iqcYUpnUTB1iieaTQB3rMLZjYWvS9xQB6duZejaaq_YOZgmyxi3lcXfArPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
وزیر علوم در اجتماع شیعیان ترکیه در ظهر عاشورا: من از کشوری می‌آیم که یکی‌ از اولاد حسین بن علی به دست یزید زمان کشته شد و هنوز پیکر او روی زمین است. شهید حضرت آیت‌الله خامنه‌ای
🔹
و فریاد لبیک یاحسین توسط شیعیان استانبول
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/663201" target="_blank">📅 17:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663199">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1e9c4c4b7.mp4?token=FxOl2ibW0c-TxqzRmLjqsIcauhT6OUNv2Quj2SRbNc8ZhziYEthwnMb4iu27JQOLmBCMN8-TJxSlYa7NZFeq_BFpg7xRmMxcy5tjD5iQemdywOq0At6cF0iT153BxvnfJmt4r2exN2RCwI2f96nGA5pFNzWzjfUZQo8Tqvn1J5UGJKgVq5-jyPsMId1u2orSVYVMKlccsH4Niwgfl36dxjr4hHNnYvNoy2Q17DKX5rYOIdlnOT9xjyYSpGvenneg9XPAneuiqxyzQCH_0zVy2tOCY36n2NJKs8C3yG9dgb_Ur99I7TZasP0rMuhcL-wlDWH4ypCH4bCB0dYP9f-bvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1e9c4c4b7.mp4?token=FxOl2ibW0c-TxqzRmLjqsIcauhT6OUNv2Quj2SRbNc8ZhziYEthwnMb4iu27JQOLmBCMN8-TJxSlYa7NZFeq_BFpg7xRmMxcy5tjD5iQemdywOq0At6cF0iT153BxvnfJmt4r2exN2RCwI2f96nGA5pFNzWzjfUZQo8Tqvn1J5UGJKgVq5-jyPsMId1u2orSVYVMKlccsH4Niwgfl36dxjr4hHNnYvNoy2Q17DKX5rYOIdlnOT9xjyYSpGvenneg9XPAneuiqxyzQCH_0zVy2tOCY36n2NJKs8C3yG9dgb_Ur99I7TZasP0rMuhcL-wlDWH4ypCH4bCB0dYP9f-bvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تصاویر تماشایی از فوران آتشفشان در گواتمالا و برخورد گدازه‌های آتش به گردشگران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/663199" target="_blank">📅 17:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663191">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kUxrQoG_GNkqQ_4VyhBrR1QUyW2PsbhqajTCHSfVy1JL5OvXvgpBkkx0t5ZBJaKDwSubCdH5kudvlwDHVc-YrWiA7dtdN-x7g4HcQNPNJw-JcplGlMY7j1WFrxgUeWOS3xhW31d_U5xR-GcEQsCKWdTRSSwk5WL0EYw0ah8FIjRi4_5PFeQaJbtSSIAjnW9EPkJF_cpuKEah0eoGRSN0JB0411pQDShR7BhPD5TDU_d9WaKCz03xQC54-HFfWJBKhw2Hms50G4leMSB724prG0WcJ2oxOp-HrQ5cBuq2_x4SA52GKBfPFROTKbAz90FXSCbAaWR4FjRHfuKdo19_PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A4qPgIAwTagL0OAj0Hu9rNHvIrPKyy7j1UmYr4d5a1kWzBu0G4R__cZh5B3KpJnOGAlozufg9xwj3vDjj-MQnV34djG6vff-xSvQE6lb-A-jbwj_TPUfZBRKfAT3AwHe7tI6On3g9Ts2vLUg9adFXRLV5DhzH6cRLYVrJwO_exJKqumpSM2bEmYnBZMiUtv8ARsu2eC2eOaCN-iPo8rdBwZyATVybzUzXokUW-CI2trUr_RaCMQPtq_C8f_0AIcHI18-U5s81pQsEcnyR6ED6jMenwwSR7VUL0ZRMGlVpkFcE-xdZahBKJZIGQ5Rlx_mGjYvP7t3g09xZYib0Rlb7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X22HXmYcGT3t7pmWNul5AJS5fmPXq9aU9IeiUUyYt76L_ttiRIRvloJwI72qTBCZAAF5wuwVLx10DZF1WnWpNN3cTq-NFLhHUqosrXh5ZSaW4SabPjmZKkSOKJmdvn9leiFxM7z99Byl0ODuazNytyVTweMmE_Jn1AmemUkJw9sGsJoFf7POozt7tXx9huU5Bx5OJ-V5lzW4pxwX_6ghV_FkxiR7_jF4oVL4xV8txqpWWHgr3QEcCI5k4RrhGwDWUenuX-Vu0iVczpu5S8VC9qr0C6wYs7qNAs8zFwwlUYAs3TvFeY1Ofx6kItVHoIPG7hgZSVbpP08gneVkjDtDDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ozdoOen3FwX3f9vHB_mdJG2mvgVwItfay4_5Ihv2_RAUDwONlXwMdLOqVBhTrsJ6xy01bHIuEjNCc1rP8kBiRhQgLwFGZ8AuoX2Hj4XvheeLOQmlH30-7xOXiTSb5DcItBCsZ9hQLM6GLxQGqKCS-HkrvR6yY7dpRAGs8lvJBOXWEpA4q_SXGN3-ZFSZ_0kCBVfiZrAKIjIbmbTqOAYzDsh_DVyxvy2nvYUoJdmBm2RwgfxC-eU0sL1VLNql0DG2dI6dcaprGvCkYHEEiKfTloDk4tGODL_BFGCUI3aNBrJdTcxAAw6h2n5suNKSuZsBZDxc7Zrr5Bw8LZYU0XaJCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPmYkD4RDh2rfb1fEL3ER1mVmVJxxfcB7YdoTMszrUOxi_iw4x6dXqxwvTQNTGb8K2hNCMIkBtIgzvEUeYpPm11luedtFx1RG_A__RtV4gF1H8Dw45exR2AwGhhRfUHvbierhr8ZS8F3NmH0uHfuKmRAQ_zvsDMhUOEQP60Skq2gSMUP0drHnly7unwXcUJmqx9CEY6eZkAgxAdxgzF6CTdeHhcg5bVYtidBtPw94K_gPolf7nj_qWBbwoYu1V6svxZ3vpj4bNNBHYJ5PxaOFQxmyIyHHlK3OM_jHcaVPb3j6Db5vdWGkCe-Ezq4NIuevPElfSq3G587ESqflulhoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hNWnGNctYBnB19oJUNnlLgRFNlgn-QVwXpif8UmsX_ZqyWqSHG5SjcRx8HeDwGFgc-qRJC230WgPyhKZKmCBAbAtysOH8ITcvV7FxbPmpu4OsGlaQ0K9WXCU7-NieMkoF1GeVFKPH3sVjwOFLwqQ62qyUhEO7UwHH4Lt7Wx7I6DZJN9Md__h4FGNpbkUyOCb24oGuEa3vBT9k1YEnj5JKr6K9pAb744gUzWjoLmAyn6bK04qT5O3QM8ErXw42BB-Pi7YXUUc7WvhoZFBhyF51iwUlJaNizlXiYunk_ry_3WvRLowCp54l-eY7N5SwGRwoQV8J2akqjzZkkA62IGvOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DAdDNWuf5nlylX1jZhAihU-_bQqEaU6WFdFDGl4QSOgmu1w9eVZm1o-gTsUrPqDKnwf5r7W4-NOCE2J6hE3wjwLoVdojHzzyFqO4YA6MG757eA5ZsevTVB5nuIn7iLM0lK-iogT5JppZcfdkQt1uTxNZ58ylFdGUDdMK0Cxd0ceQJhnTQlOJLjS9DtcPyUePAItaVpgzAvn0EplS5ZvUbdZ9hB8vMGFdhXiPLP2xyRCYGW_oqakjfn455GdlLasbRp4KtIgBXkxWQLKRmjyKURwtQeO1_axJIpLoVEur0ryQ7xqxzB-qaXK_CoZPa-CdiTWaxn7APC8ORVOxiZH8XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JpyaKZiU2p4RRGARmvVJs-AnrMDpI8xvGOH2JeZ1qahPNQbaGPuLIDyB9hRVpWVZw-ssmQ_9XvxFH0xPaLDp6aqBMOWK0_fivhdX243KgPG1_M8-bS8RAFr_kTy8cDo1gxONeiuN3Bh9dTBX97tRJ_2xZtLqw8tzehKrwWKJWsyK7tLSMcOcLnCbrHnZfpYZX57ZhiaqclEJy-wmgZk2nn6TeCzMAY9foKaG7P6GceDDhVZkPyykowMnItQ4Xrn9e7qKeZwGGcYhrRKddwcWB7l4-nNOljQVyRWhCsd_s_NiaBOwrBkcd-plFkLydB_OY5YfPpVMHKrof66H5V19PQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نشان حسینی
🔹
عکس‌های ارسالی شما از گوشه‌وکنار شهر؛ خانه‌ها و محله‌هایی که با برافراشتن پرچم‌های عزا در سوگ امام حسین (ع)، شور و شعور حسینی را به تصویر کشیده‌اند.
🔸
تصاویر خود را با ما به اشتراک بگذارید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/663191" target="_blank">📅 17:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663190">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔹
ادعای جی‌دی ونس: توافق اولیه ایران و آمریکا برای ایجاد کانال ارتباطی نظامی مستقیم
معاون رئیس‌جمهور آمریکا:
🔹
در پی مذاکرات سوئیس، توافق اولیه‌ای با ایران برای ایجاد یک کانال ارتباطی مستقیم نظامی جهت جلوگیری از تنش‌های احتمالی حاصل شده است.
🔹
ما به دنبال راهی برای کاهش درگیری‌ها بودیم و طرف ایرانی با استقرار یکی از اعضای سپاه پاسداران در کنار نماینده‌ای از سنتکام در دوحه، برای حل‌وفصل اختلافات و مناقشات موافقت کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/663190" target="_blank">📅 17:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663189">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔹
#چند_خبر_کوتاه
🔹
معاون وزیر خارجه: میزبانی ایتالیا و رومانی از حملات آمریکا علیه ایران، اقدام تجاوزکارانه است
🔹
وزارت بهداشت لبنان: شمار شهدای لبنان به ۴۲۳۰ نفر افزایش یافت
🔹
کانال عبری: آمریکا ۲۸ هواپیمای سوخت‌رسان خود را از فرودگاه بن‌گوریون خارج می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/663189" target="_blank">📅 17:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663188">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlKLboKgTEhDlzx3zy9V86UqKZSQcXPgREKZPU3PlJZ3Qy8nvjDg-Wzfmxiw3DHANggKvM3AxQThPAwnzjtfAkB9ivFZfrF83jLLjY-_1vPMOjEj7AsqUa1t_pH3emXHIh8lxBT0CJhRwjwFsO8WWEpomiek0xLg0TyPMHxNe693sAujZE8hghQ8DpxT1rTGDRG9MSe39m259lOkNK32Nplvnr9RF4_T9ynFirxo92npDLTZ4fldaSMs28m2Xsh-GSCrdrmjaE6V9NWF1oGJHihE9Yrsv1D7gpNDugS2yrb1ss_bs7hcEthyySwmrUkB1g_0kZ9FDtRB1IyeEQEzkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
الحوثی: پیروزی ایران، موفقیت راهبردی کل محور مقاومت است
🔹
رهبر انصارالله یمن تأکید کرد که امت اسلامی در مقابله با آمریکا و اسرائیل، درس ثبات را از مکتب امام حسین (ع) می‌آموزد.
🔹
وی با «شر مطلق» خواندن اهداف صهیونیسم علیه ملت‌های منطقه، پیروزی جمهوری اسلامی ایران در برابر دشمنان را یک موفقیت راهبردی برای کل محور جهاد و مقاومت در این مرحله حساس دانست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/663188" target="_blank">📅 17:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663186">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه نیکوکاری مهرآفرین پناه عصر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cfae89a7e.mp4?token=l1MHSjwX4CwOdnmbypjFR4qevopD1XCPOnfpppviQEFuV2LeUUcgyiM1QtxffF8OM2aXZaTr-vFj77xmDvoVWZ6CtIKvL9-jLoYLvGQz5tF2ydpy8CtwkigtCJfFURjHcXQlVES8jk8p3cfDXpg1ivk-xOrm0Qv1M1XUpw_ip-9mqejFInhbqlILxRApY4TtcS8ON27G0jZOC43PBohQtJbu-lv7YC7OP_D1Th38i81kwovFOv-mh9aQPVD5OJ39rtnbALsAsaGdKWoQ6ASZ_4yJp2HR-YwbbQ_1fQUSw5zYRuAgizNqtzLUmXTLRPO9mZmzb4TCNTpR37GYenPQAwAuc4L3Msiny3phYJ7KpFWkdXAdrWVSM6gUXUvVR-W_-tSLmT46lK5vro_mtmE-mXyw_K__zmlIXM9iwf4f7n_PLPBgzcOxPWbVme8N6RpE31s9H_nofgZ7N_Jg9dpdwdQdv2uNbbrBLZ-OXBumb7ttS4Vbgo4l7-aIjpcX3czkU3mJhdHj_zcNmCUWSR4dZ7EAwOghNLjgs37lE1rSc_Qh3njNa_PHtDFWXS2TY3GhScrySLwmg6LQn7uhPqfua86HB5GL8FGXJwP9PqVLpbpOq4sGZ9uwWqxDv2BoCtXEFFOwxa0xKuP6Zs5EZ2YfsmhqGz7so8ep0igKU1l7mgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cfae89a7e.mp4?token=l1MHSjwX4CwOdnmbypjFR4qevopD1XCPOnfpppviQEFuV2LeUUcgyiM1QtxffF8OM2aXZaTr-vFj77xmDvoVWZ6CtIKvL9-jLoYLvGQz5tF2ydpy8CtwkigtCJfFURjHcXQlVES8jk8p3cfDXpg1ivk-xOrm0Qv1M1XUpw_ip-9mqejFInhbqlILxRApY4TtcS8ON27G0jZOC43PBohQtJbu-lv7YC7OP_D1Th38i81kwovFOv-mh9aQPVD5OJ39rtnbALsAsaGdKWoQ6ASZ_4yJp2HR-YwbbQ_1fQUSw5zYRuAgizNqtzLUmXTLRPO9mZmzb4TCNTpR37GYenPQAwAuc4L3Msiny3phYJ7KpFWkdXAdrWVSM6gUXUvVR-W_-tSLmT46lK5vro_mtmE-mXyw_K__zmlIXM9iwf4f7n_PLPBgzcOxPWbVme8N6RpE31s9H_nofgZ7N_Jg9dpdwdQdv2uNbbrBLZ-OXBumb7ttS4Vbgo4l7-aIjpcX3czkU3mJhdHj_zcNmCUWSR4dZ7EAwOghNLjgs37lE1rSc_Qh3njNa_PHtDFWXS2TY3GhScrySLwmg6LQn7uhPqfua86HB5GL8FGXJwP9PqVLpbpOq4sGZ9uwWqxDv2BoCtXEFFOwxa0xKuP6Zs5EZ2YfsmhqGz7so8ep0igKU1l7mgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
آنها
انتخابی نداشتند…
و نباید بهای فقرِ بزرگ‌ترها را بپردازند.
👶
نوزادانی هستند
که از شیر مادر محروم‌اند
و تنها راهِ تغذیه‌شان، شیرخشک است.
در این روزها نذر شما می تواند
🍼
سیر شدن کودکی باشد که چشم انتظار یک قوطی شیرخشک  است .
❤️
نگذاریم
هیچ نوزادی گرسنه بماند.
💳
5894637000012820
💳
6037991199529904
💳
6037991199506100
🔖
IR
710170000000216780692009
📞
*780*35260#
🔻
پرداخت مستقیم
Mehrafarincharity.com
⭐️
مهرآفرین باشیم
|اینستاگرام|
وب سایت
|
پرداخت آنلاین|
❤️
@mehrafarincharity</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/663186" target="_blank">📅 17:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663185">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔹
نقل‌مکان نتانیاهو به اقامتگاه مخفی
روزنامه هآرتص:
🔹
بنیامین نتانیاهو در ماه‌های اخیر به یک اقامتگاه مخفی در قدس اشغالی نقل‌مکان کرده است.
🔹
نخست‌وزیر رژیم صهیونیستی هم‌اکنون هفت اقامتگاه مختلف در اختیار دارد که هزینه‌های نگهداری آن‌ها، ده‌ها میلیون شِیکِل(واحد پول فلسطین اشغالی) برای مالیات‌دهندگان هزینه در بر داشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/663185" target="_blank">📅 17:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663184">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4882bbc4f8.mp4?token=BVZxd-_EpmqAnMVTmpjvvkM8xNXb6SqcudfpSyhS19GqZdpZ-bW8WrnxER7hR4MBjAYoFWsTnjMiVCtQuLE_KADo476IAHNZE0YrpVjpSH6-gh41s4Oab0MuEUr7x3ciT0g1pxT6zkAzEFVQ4cVDVBL7E2lRYWAAuurAxmMvgSa1liPy6JKIn6DUMay3P7cFNYAY2oBr6dukGnd-PN3Ntd0-BohJ09GTtCetxDmfTXTCHj6wudI3Cm3GQ7EFnT9ISrZZQOEqsZNqsE1NFgx-HVGbU7nIwNKda46hzPwCLe3ShvF2s4yWOkxBCYVzhZJSTs8wE63vCvzl91K8NZW7gkwTxGbGleSnMfTxPDvgcX3WNQ-2H4oCBc4cD6Q_syVDXfhuYt7MUEmdsjlmEKca4eYpYSLLX7SBuR7_p5AJVkv0hzXkq7b0mp9zoGkiyamU1aeCyvawIkshD1sN-6vSZ_dMmkLTUbzgjNh4swn1OF-U8ipl9dEC6jPkjnUKNdCeVo5V70jRZNp9z0cYRlZIdSinNuYNoIvm-a-fzBRrrdCJIq5k9EGVbOipz2eBdvop6eHSUchsXk2zqNn1a-F47XyMAbCNawXcrIQHOX55hSnx-OgE_uryAX4TVFVa7C3nFZz0Ap1snzUQChmLVXtB-4kodV2zcnopisX3zHKiqjE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4882bbc4f8.mp4?token=BVZxd-_EpmqAnMVTmpjvvkM8xNXb6SqcudfpSyhS19GqZdpZ-bW8WrnxER7hR4MBjAYoFWsTnjMiVCtQuLE_KADo476IAHNZE0YrpVjpSH6-gh41s4Oab0MuEUr7x3ciT0g1pxT6zkAzEFVQ4cVDVBL7E2lRYWAAuurAxmMvgSa1liPy6JKIn6DUMay3P7cFNYAY2oBr6dukGnd-PN3Ntd0-BohJ09GTtCetxDmfTXTCHj6wudI3Cm3GQ7EFnT9ISrZZQOEqsZNqsE1NFgx-HVGbU7nIwNKda46hzPwCLe3ShvF2s4yWOkxBCYVzhZJSTs8wE63vCvzl91K8NZW7gkwTxGbGleSnMfTxPDvgcX3WNQ-2H4oCBc4cD6Q_syVDXfhuYt7MUEmdsjlmEKca4eYpYSLLX7SBuR7_p5AJVkv0hzXkq7b0mp9zoGkiyamU1aeCyvawIkshD1sN-6vSZ_dMmkLTUbzgjNh4swn1OF-U8ipl9dEC6jPkjnUKNdCeVo5V70jRZNp9z0cYRlZIdSinNuYNoIvm-a-fzBRrrdCJIq5k9EGVbOipz2eBdvop6eHSUchsXk2zqNn1a-F47XyMAbCNawXcrIQHOX55hSnx-OgE_uryAX4TVFVa7C3nFZz0Ap1snzUQChmLVXtB-4kodV2zcnopisX3zHKiqjE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
در این ساعت‌ها، روضه‌ی عصر عاشورا را از زبان رهبر شهید انقلاب بشنوید
🔹
به سوی پیغمبر صدا زد: «یا رسول‌الله صلی علیک ملیک السماء هذا حسینک مرمل بالدماء مقطع الاعضاء»...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/663184" target="_blank">📅 17:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663183">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2je81J0VLKXkzT-Xo2c_cej9sMdkdDHhYVcCVd4dFXgIZhWw15fMcuiaMsPjwxao8z_5ERb0LJqayZGgEhc03R3ogO4Oii1vPQdzkvqME7xuZwaXoW18EWuaQwlQuTeyII5eBlEVjpHvIFHvFRNLTG1_v-0oKg_uc6muGCgRHcNHGsdkBu0lDVbEsC95RbHDdqaYOPvAFzIPA_UtozOoGWYQuWBUe3azGHBjoXP5CEVWaO4DLR35A4gsgKlkRniWb7xc4w46JMX3QpiSWSE2COcztp1TspWYUrcu0HWJBTIuslPPGEgHpaR2HuWNZBscrP80tPtj-lRQaYY_snMZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کشته‌ی شیوخِ مقدّس نما؛ حسین(ع)
آیت الله‌ مجتهدی:
🔹
در کربلا همه داش مشتی ها رفتند به کمک امام حسین علیه السلام و شهید شدند، مقدس‌ها استخاره کردند، استخاره هاشون بد آمد و نرفتند
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/663183" target="_blank">📅 16:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663182">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e5de2e37e.mp4?token=RNlyfbSH5a2THxUNpf3pIAMSO2xnJQ9P0KSyNGDCx3_NHWF14znLK8Rx-5xA7pM5GkKYjYWL7a63-N5LhIB85HPAY-En2VkMhzEXMl4t3Gbwi4XcSRPmo0wOnHji52SPHBJsJgpJ9V85PzeVhextV5TvZXNCCZXUwqKH2CptMVflmhtvj7EVGfv7BJvFUqxxYSrlUasuYrfWkz5mvP415MOKeiih6DUQzdXPBlD1bMH8xlmIf9SBwj7n5doX0RTLD71aqlBtTdTXM2mqjd5cNCB4_6UNQDEO6OzgzT1gS9-yA7Qj5vOFsKNtAVZhTwOm0WJ4PT2u-I_ynbHfDym8cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e5de2e37e.mp4?token=RNlyfbSH5a2THxUNpf3pIAMSO2xnJQ9P0KSyNGDCx3_NHWF14znLK8Rx-5xA7pM5GkKYjYWL7a63-N5LhIB85HPAY-En2VkMhzEXMl4t3Gbwi4XcSRPmo0wOnHji52SPHBJsJgpJ9V85PzeVhextV5TvZXNCCZXUwqKH2CptMVflmhtvj7EVGfv7BJvFUqxxYSrlUasuYrfWkz5mvP415MOKeiih6DUQzdXPBlD1bMH8xlmIf9SBwj7n5doX0RTLD71aqlBtTdTXM2mqjd5cNCB4_6UNQDEO6OzgzT1gS9-yA7Qj5vOFsKNtAVZhTwOm0WJ4PT2u-I_ynbHfDym8cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
حال‌و‌هوای ماه محرم در میشیگان آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/663182" target="_blank">📅 16:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663181">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMrR3cU1CT6NB8P7sp0lfTxXLQ-nkI4oP81jS-MeBlfCWVpQfIiG8e6W-9yIxDUSU2FNG8Ziqh6SEcxw4MP86PbFrcABvg-c7aFmO5jskJNUG3FAmS24ts5kSFZ9R6HEe8IHi_kqne87alo0z1fMqcNC3_F7bLfS7jzlHEC6DPStdvZLvoP1rD-XcxXUg3M-8r9inx8j6whXQ-uJeirNH68fsVBfHquBXdH_FoIh7W5ul9iM_a3hAi66rNZGtFhNz8yeRuEZAZHpnCT6CDbiu2jNiFjnbcOJ29A3U8Qbcb9sAWv81ytZ9BKP64K5359zNY5J7Uph2Bto0LsGqxhsEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
۱۲۷ کشوری که هیچ‌وقت در تاریخ به جام جهانی فوتبال صعود نکردند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/663181" target="_blank">📅 16:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663177">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k6MMsD9WQgRHFkjxsUcEYJjgXZX4iPorE4YBCFB3Ye3UGm8H7q9ZUQSuJkt-uxX3icwR16XT9Za9PNfRg5-G8T2W_hsQnpT2UVVTJQrTRcW9JsTE4jYGbWM4Koh8JgJ9VCTVY1-c2VPbi1eIgk2AxkC69MTIrdR57usUI73YVijlTF__pSxF1RCY65cfLxVLj5-HaBWFjaqru_fked4P0T6C-0fZP0V2TrA8Z7OzDDJNf_a70WdBQjXXb3S6e0KLXd1oDXVi5n_jvd22d86HH4h4YbE1YL87RlQ0Te9yav4yRKiPmZ7z168AQ2KNjeG5t8IkKHDpa5vVIHk_Iwky2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z679zFNjxiTxkjC5gNjbIJkT_5CE69NCPvfQr0Dghx0AmeLpBaTDv6XPvcrcA1EO8cCJlTinpObS-_zkIXSq-WKfJ-bNY1FSvDHYAGC-qQqDzbsATzYiHtjGT9CJ9Hhz2Gs4fSpjNIVM2pHZiTD0dc5eMWFbSRGkIgNdA2sTaFvH4UZ7RWlLcRVA6NAnvyKKRix5iRRxIx3w9-h1XZoRKeKnp0HpqekNfmh77Z29xUJ1uvC6xaKsxhEzmlrd5sDEsGBN6uzzltcCusgbRcDwazjyKSrBR2k_AK-XWroWd20nvcXJ7yq8KPbVh4lbbzSYmCrUW7db5vVx2lx_Gx8cvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VLFP2YUHMhAKG-Kd0xiyhwOsvtMQKEXICvSf2rafN8X9LLIV05fN0XBj_OaL7YiWsCIJpT4t2OH0erV7g46XqdYeWtD1jK_lQo9na5T-5p1NT3JB0vtbF-9G2olblMMpMnTgkC4ShlfFQBZgLRdbEa4JsxzdNAFH52Kuuv-7jKbLpVpG0qUKPMYCFd1l5nI-PRoheEp2_JdOSz1rIeQ2l3U2MeR3hv481j4IdvgTYguFHmma9_bD8LJMowL267PoBn8TghoX5codqpimAGXR6etQAsDyRD2o8ZrNloS0HLgZDDIcHrRCUWrTI6TzIl0gjOWQkzHOBJ8xoMqzRFCgzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vUmVNGLl-hbQeonal9yTBNK3Ubep9vNIppz6bBY5_rgUNxuUpdtpsRXKmRNiP4sfvtCk9BwTYVv4L2bWXTMth9ZXx9G911qOiaEu8IeTX4cQFvHcGuRJR7vIvO-cpO9sDbN8NsdM6KBW_AdMX3G-kONJWSo-EAMsOninlQVHvAjAkx-_2Taw-d_4V7Zqzi79Ztnlz_2UxZMhVe2URBMQxLfAQx1rHUMYy8a02SRFPs-3tLh7jV-A1CbE-VjLJQ-WOnNYJVvTMIALh1uzSRN92l2m8CLzRWOkZOO_xgiQM24NKfQyy6IpsTC9bXSRijW9ZP1S4NH7S-mQ0H9unRNrug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
مراسم عزاداری و بزرگداشت سالروز شهادت امام حسین (علیه‌السلام) در صنعاء پایتخت یمن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/663177" target="_blank">📅 16:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663176">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">از تبیین واژه علی الاصول تا نقد توهین کنندگان به تیم مذاکره کننده
حدادعادل درباره پیام رهبرانقلاب:
🔹
کسانی که مذاکره کنندگان را به برخی عناوین متهم می‌کنند، اقدامشان منطبق با نظر رهبرانقلاب نیست/ پیام رهبرانقلاب نشان از اشراف ایشان است و دست طرف ایرانی را درمذاکره قوی کرده است
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/663176" target="_blank">📅 16:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663175">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKyzJSbdJcREiHtuZ3JsMzLMxF1BHv9pGNhGnjUMqOO306cRsy488wlP3sGDzlWwFvJGpHBAYCOROxZSunvN_OdnjSouHm04MqeBHBeWhuLV2EVx_GfxZsQG__GRgalhUWW7LjAQ5nWBa0-IRwET1saEKKE_A7of3aBN25ooqLvrLHSsfypzRoNLtw3NjKj_TUhwcrba22GTGM2ygiwuyqHIExjKoXlOXLo9OlxpBlkIoC1zdnwBjDBVI9D7U3azRaxjIZWWVkESm7IZsuF965KE1S649_WGsY4mrccpqFP2qM5olqjs7m7Zr-t02MesSyyv5uXw4dkicwoYpzyW3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ترامپ از اروپایی‌ها در قبال موضوع ایران انتقاد می‌کند: من از ایتالیا ناامید بودم
🔹
من از بریتانیا ناامید بودم. ما از آلمان و فرانسه ناامید هستیم. ما از بیشتر آنها ناامید هستیم. اسپانیا یک نمایش وحشتناک است. اسپانیا حتی از دیدگاه شما هم وحشتناک است #Devil…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/663175" target="_blank">📅 16:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663174">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c36f8657cb.mp4?token=bh_tjfadTWwgbZL1_XWSPtWd2evIRMm8USekyUQpapnBPGbFZCdd4alr71di1reYACpcfd6sRviHpc1wdteFDFBwXhOjBC3QNvBEOqzDZ6xmlDggNnDwiWzBb3pbJyHx8hYWRJelcHjJchCTxHw6_AgBYtOnu60VaAzFcgxT9DiIcC684R2VA3hmK9ysngMh6iwRBXRl6zloMLWhyRh_97K1H4xERsqPbcd1W5E7d_ohk3QbCaVKHiOId3TmMQGOB4owkoZLOCBP8Pnc3iYz0X5-IASGi403gddW_UldK4vA4E0Ly18XU7JEe5wV1uuQdeji-vWa5mcnAdK4DOm9MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c36f8657cb.mp4?token=bh_tjfadTWwgbZL1_XWSPtWd2evIRMm8USekyUQpapnBPGbFZCdd4alr71di1reYACpcfd6sRviHpc1wdteFDFBwXhOjBC3QNvBEOqzDZ6xmlDggNnDwiWzBb3pbJyHx8hYWRJelcHjJchCTxHw6_AgBYtOnu60VaAzFcgxT9DiIcC684R2VA3hmK9ysngMh6iwRBXRl6zloMLWhyRh_97K1H4xERsqPbcd1W5E7d_ohk3QbCaVKHiOId3TmMQGOB4owkoZLOCBP8Pnc3iYz0X5-IASGi403gddW_UldK4vA4E0Ly18XU7JEe5wV1uuQdeji-vWa5mcnAdK4DOm9MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥀
نمیشه باورم که وقت رفتنه...
مداحی مرحوم حاج حسن جمالی
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/663174" target="_blank">📅 16:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663173">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">🥀
زخمی خط‌های مقتل| خط دهم: وداع ۲ غریب
🏴
امروز روز عاشوراست. هنگامى كه امام حسين(ع) تنها شد به خيمه‌هاى برادرانش، فرزندان عقيل و خيمه‌هاى يارانش نگريست و كسى را نديد.
◾️
سپس به خيمهٔ فرزندش امام زين‌العابدين(ع) رفت. او را ديد كه بر روى پوست خشنى خوابيده و عمّه‌اش زينب(س) از او پرستارى می‌كند. چون حضرت على بن الحسين(ع) نگاهش به پدر افتاد خواست از جا برخيزد، ولى از شدّت بيمارى نتوانست. پس به عمّه‌اش گفت: «كمكم كن تا بنشينم چرا كه پسر پيامبر(ص) آمده است.»
◾️
زينب(س) وى را به سينه‌اش تكيه داد. سیدالساجدین(ع) از پدر پرسید: پدر جان با این منافقان چه کردی؟
◾️
امام(ع) در پاسخ فرمود: فرزندم! شيطان بر آنان چيره شده و خدا را از يادشان برده است و جنگ بين ما و آنان چنان شعله‌ور شد كه زمين از خون ما و آنان رنگين شده است.
◾️
حضرت سجّاد(ع) عرض كرد: «پدر جان! عمويم عبّاس(ع) كجاست؟» در اين هنگام اشک بر چشمان زينب(س) حلقه زد و به برادرش نگريست كه چگونه پاسخ مى‌دهد چرا كه امام(ع) خبر شهادت عبّاس را به وى نداده بود زيرا كه مى‌ترسيد بيمارى وى شدّت پيدا كند.
◾️
امام(ع) پاسخ داد: پسرم! عمويت كشته شد و دستانش كنار فرات از پيكر جدا شد.
◾️
على بن الحسين(ع) آن چنان گريست كه بى‌هوش شد. چون به هوش آمد از ديگر عموهايش پرسيد و امام پاسخ داد: «همه شهيد شدند».
◾️
آنگاه پرسيد: برادرم على‌اكبر، حبيب بن مظاهر، مسلم بن عوسجه و زهير بن قين كجايند؟
◾️
امام(ع) پاسخ داد: فرزندم! همين قدر بدان كه در اين خيمه‌ها مردى جز من و تو نمانده است. همهٔ آنان به خاک افتاده و شهيد شدند.
◾️
پس على بن الحسين(ع) سخت گريست. آنگاه به عمّه‌اش زينب(س) گفت: عمّه‌جان! شمشير و عصايم را حاضر كن. می‌خواهم بر عصا تكيه كنم و با شمشيرم از فرزند رسول خدا(ص) دفاع نمايم، چرا كه زندگانى پس از او ارزش ندارد.
◾️
امام حسين(ع) او را بازداشت و به سينه چسباند و فرمود: فرزندم! تو پاک‌ترين ذريّه و برترين عترت منى و تو جانشين من بر اين بانوان و كودكانى. آنان غريب و بى‌كس‌اند كه تنهايى و يتيمى و سرزنش دشمنان و سختى‌هاى دوران آنان را فرا گرفته است. هرگاه كه ناله سر دادند آنان را آرام كن و چون هراسان شدند مونسشان باش. چرا كه كسى از مردانشان جز تو نمانده تا مونسشان باشد و غم‌هايشان را به وى باز گويند. بگذار آنان بر تو گريه كنند و تو بر آنان.
◾️
فرزندم سلامم را به شيعيانم برسان و به آنان بگو: پدرم غريبانه به شهادت رسيد پس بر او اشک بريزيد.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/663173" target="_blank">📅 16:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663171">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DAQsUFQ8mAyla7DO5zqqskGe7JQ8c5YlsL1Wno158FhrbJx6eKSTZ_Q-qY05O0rOCq25ZaFAsdod0Ntt2MFsSRqETOWxMsbxvk8T7_3TmZlQ4zqbCpRoZ5mAhC8-jbFr6nkKf-mPD8vJrVaIYocf2T-uLJa1hiqAJJE10U_1XzWkNgnEMUx14QVtbWbQeqfm0tNNE8yso9dbPwWXq2NqxNCn7zHJStpLvklZw4MySX4Sn0gqhzpkiy2yagUpeIH1VkOsVkV7JjoMjI5ZvF0rOJjjQaXxZljaweWyz_NMtDybuVpWIWE6ZoJKutLlbTWzAvTlLaPXf4wZR4B8LuTA2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lmZP-9m3qCCO3502vflEhX0sGhGKBAzlxL2V7K9DSREq_OlcXo7MyzzNRHxixd0LeTEBE3WD-0JrfXpQpQjoIUmrYZFw5cy4cnRUID_DTsrk6KPZuTWYqjNq_xYU8sBHhrSHGQFzvlO1R9b4_Iy6xZKTBChR9inGZEK0IKk_L7v4WO2C04d-Er9A6qfhq4XN6AkMlYRO950_rL7KwC2RuzTgWfuJPMoteGoyKC7ucI4qH7kQBY1r2J3hp3c0hBG1Uilhflc5WBBuy_gG2CdESIpu5k4i26_alR3wDwz-KbQfreGfaFF9ePeEvoC7_2eb1bDMnZHw9ZXOjw9fXZ-jXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
ادعای کپلر: عبور از تنگه هرمز با مسیر عمانی ۲ برابر شد!
موسسه کپلر:
🔹
تعداد عبور و مرور از تنگه هرمز در تاریخ ۲۴ ژوئن یعنی روز گذشته به ۷۰ مورد رسید که نسبت به روز قبل ۱۰۵ درصد افزایش داشته است.
🔹
این افزایش به دلیل پیشرفت تلاش‌های مین‌روبی و استفاده بیشتر اپراتورها از مسیر عمانی رخ داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/663171" target="_blank">📅 16:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663170">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔹
تکذیب ممنوعیت شعار علیه آمریکا و آتش‌زدن پرچم این کشور
🔹
قوه قضائیه با صدور اطلاعیه‌ای، اخبار منتشر شده در فضای مجازی مبنی بر ممنوعیت سردادن شعار علیه رژیم آمریکا و آتش‌زدن پرچم این کشور را «جعلی و کذب محض» خواند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/663170" target="_blank">📅 16:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663169">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8PuXg0n_q2kbyHmHnSiycNse9OM7C3TOUI2cT_maJuGKlFvghEIH4UFxjv9mhL-PMRr3J671EdLqZJvfFb-9oTIXmbnQEmNlLzayG6rxsA0CAfPe8TNskqjT_Y_5vLJKK7j4kxTPonIzlPn_tEk5Z9_dcQOwmqACmKC3UwmuzLkD4pLlW0jNNpt-QupC1h-QazAInGV888jgnomxQBfs_NnV9NeYVVmVyConBqqa6LZmbQWVvP3L8-BGa7gITGpMFF4J1AV6cB5jz35Ywi5-hFcCFuALic7po8lPPnfjkfbADIWSDXssrocrdHTn3nSCnFypG3W_BQFkVJe2w5T1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
واکنش قالیباف به دروغ الزام واردات محصولات آمریکایی
رئیس مجلس:
🔹
آمریکا به دروغ ادعا می‌کند که دارایی‌های آزاد شده ما صرف خرید محصولات کشاورزی آن‌ها خواهد شد. جالب است؛ تنها محصولی که ما در حال برداشت آن هستیم، همان چیزی است که شما کاشته‌اید: دهه‌ها بی‌اعتمادی.
🔹
این محصول، ارگانیک، فراوان و بومی است. اما ظاهراً آمریکا تنها سویاهای تراریخته، وعده‌های شکسته شده و یاوه‌گویی صادر می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/663169" target="_blank">📅 15:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663166">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زیارت ناحیۀ مقدسه</div>
  <div class="tg-doc-extra">حجت‌الاسلام میرزامحمدی هیئت قرار / @heyate_gharar🏴</div>
</div>
<a href="https://t.me/akhbarefori/663166" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🏴
پک
#هیئت_قرار
ویژه
#روز_عاشورا
🥀
به احترام ذکر مصائب ذوات مقدسه، لطفاً بامعرفت و در شرایط مناسب گوش کنید.
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/663166" target="_blank">📅 15:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663165">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a01f9083c.mp4?token=PjMXvUMz5w1uyDWkcyA0a93cXDyrFnBejyiNKhPE3qTFs5hYUyNGaMOHMpFejVOuSvEbTN0MpLfFpB7NyonyGK2PlCy02-EFRpr8Gw0FfmmxnIHcFRi4oOmcnTTZJOe1PwHcPwAnpVKHLmqCmdXctqsXp9tZc1w9sDr6TJL2xUFZ7wNI6x1Gxu_Twsp8zQXjjYXRGb8J9uaB0-SnndHduBhu3cD2RvCZ2_Oj3rYffoAJZn2qQ9BhG-PN1QzRsvjOj381K4ItesRNgOXfcSkS7iCYBtq2T0uvuiE-c12nVJzODtpqJM8qIXnNHIPbMxQ2Ma3jLpW3_eN_CYYroGtz1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a01f9083c.mp4?token=PjMXvUMz5w1uyDWkcyA0a93cXDyrFnBejyiNKhPE3qTFs5hYUyNGaMOHMpFejVOuSvEbTN0MpLfFpB7NyonyGK2PlCy02-EFRpr8Gw0FfmmxnIHcFRi4oOmcnTTZJOe1PwHcPwAnpVKHLmqCmdXctqsXp9tZc1w9sDr6TJL2xUFZ7wNI6x1Gxu_Twsp8zQXjjYXRGb8J9uaB0-SnndHduBhu3cD2RvCZ2_Oj3rYffoAJZn2qQ9BhG-PN1QzRsvjOj381K4ItesRNgOXfcSkS7iCYBtq2T0uvuiE-c12nVJzODtpqJM8qIXnNHIPbMxQ2Ma3jLpW3_eN_CYYroGtz1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
۳۸ سال قبل در چنین روزی، مارکو فان باستن یکی از زیباترین و استثنایی‌ترین گل‌های تاریخ فوتبال را در فینال یورو ۸۸ مقابل شوروی به ثمر رساند
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/663165" target="_blank">📅 15:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663164">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔹
ادعای وزیرخارجه آمریکا: اگر ایران به حمایت مالی از نیروهای نیابتی خود ادامه دهد، هیچ توافقی کارساز نخواهد بود
🔹
اما اگر ایران واقعاً به دنبال یک توافق خوب است، ایالات متحده آماده انجام آن است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/663164" target="_blank">📅 15:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663163">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4087fb9ca1.mp4?token=R2H_ieyT82lA6sbbJVmGqekt6ZCIlgCoWnCk2EvmtLLwd0eL8P8EgILMHQqmtXpi0UI59HPDKWoX1TprmayV42-CZyQPXd0oNxdyv-4rs409Fheeu_lFv8LPVLiWlRL92VhDMtgXjOKsIH5-iOOdpOeLd4erDqDysPiCJda0Rb77fZnKSY7QgaMrsDx483MINQIopRn6aQjkNcoPxVeGCHf06SNTtAek4HlMy0omonFkouK5I__dMn9jLzHDHDZdIyj6lzTFZ-sYKSQ35K-JvMeVhvcxGY_zND1APXgKMTz7N2KaqmWSgAVqOjCH2-5LkDs_F0kHtFhGnYWG9aHxaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4087fb9ca1.mp4?token=R2H_ieyT82lA6sbbJVmGqekt6ZCIlgCoWnCk2EvmtLLwd0eL8P8EgILMHQqmtXpi0UI59HPDKWoX1TprmayV42-CZyQPXd0oNxdyv-4rs409Fheeu_lFv8LPVLiWlRL92VhDMtgXjOKsIH5-iOOdpOeLd4erDqDysPiCJda0Rb77fZnKSY7QgaMrsDx483MINQIopRn6aQjkNcoPxVeGCHf06SNTtAek4HlMy0omonFkouK5I__dMn9jLzHDHDZdIyj6lzTFZ-sYKSQ35K-JvMeVhvcxGY_zND1APXgKMTz7N2KaqmWSgAVqOjCH2-5LkDs_F0kHtFhGnYWG9aHxaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ادعای وزیرخارجه آمریکا: اگر ایران به حمایت مالی از نیروهای نیابتی خود ادامه دهد، هیچ توافقی کارساز نخواهد بود
🔹
اما اگر ایران واقعاً به دنبال یک توافق خوب است، ایالات متحده آماده انجام آن است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/663163" target="_blank">📅 15:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663162">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43bcf8b0c2.mp4?token=iSdxtZDI9Yfk-FkMrsnuVI782WSJ7UGMCdMEORMKq92E48XNgpzSmTsF_tAQVGqANa3fUP_ID6znEFbDiIKk-88_v0H16gVoEs2v5cuSp4lo-0f_QMGNWvZCDnkbPSj6kwNWQR3Xr-Js2PKuQwblZ82UNQyOP2GsoSbaQAwpzFmHBskmtBuyvI6yLznhZrbbKrfMyGNTMWWPyjKDSbYJyJ2OofPkP2T5W6unPOw1OAFOXIjOn7WtGk_mJCZ02xbjasWQcuzOb3ppEB9N-f47PZh_Rb6FWaEuzXVd9Srcj5kxSsZ5VuS_GHt5EfB5V3I_igKCMq8WGbXy3RYHFNBxRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43bcf8b0c2.mp4?token=iSdxtZDI9Yfk-FkMrsnuVI782WSJ7UGMCdMEORMKq92E48XNgpzSmTsF_tAQVGqANa3fUP_ID6znEFbDiIKk-88_v0H16gVoEs2v5cuSp4lo-0f_QMGNWvZCDnkbPSj6kwNWQR3Xr-Js2PKuQwblZ82UNQyOP2GsoSbaQAwpzFmHBskmtBuyvI6yLznhZrbbKrfMyGNTMWWPyjKDSbYJyJ2OofPkP2T5W6unPOw1OAFOXIjOn7WtGk_mJCZ02xbjasWQcuzOb3ppEB9N-f47PZh_Rb6FWaEuzXVd9Srcj5kxSsZ5VuS_GHt5EfB5V3I_igKCMq8WGbXy3RYHFNBxRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
روبیو درباره ایران: مگر دیوانه‌ایم که با دریافت عوارض در تنگه هرمز موافقت کنیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/663162" target="_blank">📅 15:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663161">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔹
حمله پهپادی رژیم صهیونیستی به جنوب لبنان
🔹
منابع خبری از حمله جدید هوایی ارتش رژیم صهیونیستی و نقض مجدد آتش‌بس در جنوب لبنان خبر دادند.
🔹
یک فروند پهپاد متخاصم، منطقه‌ای واقع در میان دو شهرک ميفدون و زوطر را هدف قرار داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/663161" target="_blank">📅 15:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663160">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d0068dbbda.mp4?token=ciITang41pZJp9jdFPC_75Zqn0RMo9Ukmb_PL-Z-oE030osZWT_qPnEKKC4CZjnL4mMswkIzzLHscTcqq3NQr3vYYXsooQBgCMQim2D_JxfY6AeIZtDScs5IsmYv5slNp3-IjFDhciGSAL9jihpg8nsRdXh7p4aS0PWchUDbHmeVjyn8BXOCM14FHoGRkJbil8J0KArmqLbj7PSPqos33qtow9GDPtxYF1bjKIZBnq84PFMpBWVSYL6g0sKx_5zgUFX7dV_cfKTvHJ5dAAA3uuQMvrLUa4YIhUTBdkFlGJcbdUfdBy3T_BGuK-q7yReWqPLu2x-rkdpU_eLxlXNmfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d0068dbbda.mp4?token=ciITang41pZJp9jdFPC_75Zqn0RMo9Ukmb_PL-Z-oE030osZWT_qPnEKKC4CZjnL4mMswkIzzLHscTcqq3NQr3vYYXsooQBgCMQim2D_JxfY6AeIZtDScs5IsmYv5slNp3-IjFDhciGSAL9jihpg8nsRdXh7p4aS0PWchUDbHmeVjyn8BXOCM14FHoGRkJbil8J0KArmqLbj7PSPqos33qtow9GDPtxYF1bjKIZBnq84PFMpBWVSYL6g0sKx_5zgUFX7dV_cfKTvHJ5dAAA3uuQMvrLUa4YIhUTBdkFlGJcbdUfdBy3T_BGuK-q7yReWqPLu2x-rkdpU_eLxlXNmfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ادعای مارکو روبیو در مورد ایران:
اگر کشتی‌ها حرکت کنند، آن چیزی است که ما به آن واکنش نشان خواهیم داد
🔹
اگر کشتی‌ها حرکت نکنند، آن نقض توافق است و ما با آن مشکل خواهیم داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/663160" target="_blank">📅 15:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663159">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔹
دلسی رودریگز، رئیس‌جمهور موقت ونزوئلا، از افزایش شمار کشته‌شدگان به ۱۶۴ نفر خبر داد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/663159" target="_blank">📅 15:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663158">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e213993fb.mp4?token=t9mMLbflJa3JdrW9SPpvir6UAMLlRmzquOOU5_XBT4GfqtFG177hj7_cOt-PL8B3k79lLjdhKtSU7yy0bJqOD20sLeuXTyErpJZJIvXBA-952GxRqraPgHWCfbDKFmaJESBKTFRADjeMNSR-OnDtezoL9n41kqBmXOEpfyGLc-wXhwwzly4ZzuNDp33q35rL6NeyrkUoDmKEwGNx9g6HmEbio6XHWh_hf9ZTpT7hlfeP9DWTW8WJvrkIdwJ868SHxh_LCzNMG_Ycmg7b5tOtM3obkJ6DoMFn_8qbet8DtdklpKIHckNYrRV77RGw4byu736j4prO1elpIvV6_i_zQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e213993fb.mp4?token=t9mMLbflJa3JdrW9SPpvir6UAMLlRmzquOOU5_XBT4GfqtFG177hj7_cOt-PL8B3k79lLjdhKtSU7yy0bJqOD20sLeuXTyErpJZJIvXBA-952GxRqraPgHWCfbDKFmaJESBKTFRADjeMNSR-OnDtezoL9n41kqBmXOEpfyGLc-wXhwwzly4ZzuNDp33q35rL6NeyrkUoDmKEwGNx9g6HmEbio6XHWh_hf9ZTpT7hlfeP9DWTW8WJvrkIdwJ868SHxh_LCzNMG_Ycmg7b5tOtM3obkJ6DoMFn_8qbet8DtdklpKIHckNYrRV77RGw4byu736j4prO1elpIvV6_i_zQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اتفاقی عجیب در آمریکا؛ درگیری هواداران اکوادور در میدان تایمز نیویورک
🔹
ویدئوها و تصاویر منتشرشده از میدان تایمز نشان می‌دهد گروهی از هواداران اکوادور در یکی از شلوغ‌ترین نقاط شهر نیویورک با یکدیگر درگیر شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/663158" target="_blank">📅 14:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663157">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔹
اختلال بانک‌ها بعد از ۳ روز همچنان ادامه دارد
🔹
رصد گزارش‌های مردمی در شبکه‌های اجتماعی، کانال‌های اطلاع‌رسانی و بازخورد کاربران نشان می‌دهد شبکه بانکی ایران از فاز اختلال شدید عبور کرده و بخش عمده خدمات به وضعیت عملیاتی بازگشته است.
🔹
در میان بانک‌های بزرگ، بانک ملی همچنان بیشترین حجم شکایت کاربران را به خود اختصاص داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/663157" target="_blank">📅 14:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663156">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔹
اقدام فیفا و اعتراض ایران و مصر: ورود پرچم رنگین‌کمانی به ورزشگاه سیاتل آزاد است!
🔹
فدراسیون بین‌المللی فوتبال (فیفا) اعلام کرد که هواداران در دیدار تیم‌های ملی ایران و مصر در جام جهانی ۲۰۲۶ اجازه خواهند داشت پرچم‌های رنگین‌کمانی را به ورزشگاه بیاورند و این موضوع ممنوع نخواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/663156" target="_blank">📅 14:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663148">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sxZM3J8W_TfVZTa1FKtKE792B-X6jq7j-YaMOJgeBLHL7LAmCtL_JtVMQmJ_YVpzPxd7cOhimFqtUo0sHEj1wKbMu-z4PZm8xokq3asVSD-kx1m6TdZLTa9QuuRaiwGgsaxrHEn1nm3FyNzxIZpSroBchz579lfpvaLUnZjYM3iWOjiNBLj4FZ21htTWmie3f9Airs4Rl89JE-Yw5floYKrT_HNSa-9OcF4lIz704ZXtdNZD1qdh22vFUxMlF6e50nC2q_jRUXTTTqOqM6gziqISiH-rFMlwRF15M2248OwZoqMot8G9LjINePfu-FBJy9FiLJWhSCNhd_3olZOZrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LWYkBUHq2_uDXzPt_Y2-xk6gQ3-sERSJ8ftY0Zx1vfgcgE8AEAeIQOYe9KpGtAVi5NDQsme5wFi-FkiMveqdeS0XZwn34oB7icvZREdcro7XQvZ_6rijR7xEjW4wlax6o42SojXljVJefOKLLslbWeNRUBjyzZT74rhKfsBKtHzBZlFUhNZrMVuq8giRkzlH_FWDHKIOe-SCo5SEhdEOhtFINwbXzd2XQnq5QkrssBF1PWugv1bAlFrbIYjRuRE-1Oiop5E8gnE0EfWP6vEEgc0yt2Rrvw-1iXEDkdM3Oa6nlejtBTRFm4WyGt5yHyF_v9YJLomAFn3qx4lVl6dvGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXWu3cg8-3xxOArOWdP20SPwQ0LPyA-I1TtvwE0kWWb1E3otxn_N6PWSNTMnzOqLeZeL5tTE59gtcsxLUsaa3GY-uG6qVC6F6kdfDKNgn4LjK17HAb2XkKO_0OOAeyKJY0EnsBpUKpeOPmdrtu0QmIj2fqtBtVTFzaVPALf9AeX_1rLnW08izu7wQTJVNyRPB2YG9b33AuwbNuo2p3_2nE_vz2GJPaxXgHrl7dH5zkyKi5gVhB8Ecq7F3dpmoi1K4IEyYYXSEHXdL_nGPSKttFe6mNARJ26AFuLIl36ocrlMHmH9RE6gjQHoii39gm1Ff-S4WecVz_6BDKAcGxVlQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IqT2lpl6ak1ZVGYnrrtmrqvsX7qfSJlRy2pOtqBYxPUXUbq7mNap6AG8tCohNVw2xKOWlN8gOJ-DNEUTwSlofBu_7teKBGiXD2VXJf4zHQo26KWh_Tt0FdBRfpFH47AzwsO74KlX48vutICpu0xy2qCysHWLS7ikqeoxYCLmePY2pJIdaF4YG1svqnG6hN3o06hy95EDZBxRgvW5nTy4hymMI99B427bkKHRQbEW6JxvCFgoWW1U3MUbLyqsrmeKtvpPcqLJv8YZB4NKFm4q2GKJdhKXLo0kA8MAWjtPszXJ3YU_UO_R6VAQ_gPHn2Ha5TvVgo2RdFfAhktRVyQDcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b8X0i2BrE8ZKXDb7bkDUS3ez9BIt4GMXHvVMJKyNx7NRw7L6kE0OSAVurOO62Qzpbw3IQC5P6TKwInDZeYPrM706dwjm_4Tc-aBuE7Q0ZWNdf-iJqKdd0VoCyrYVXTru2-0DTfS9XJMWyE-OIJwTtbNFgbGf1ElzSkNEqyij9dgMbr8cMjAv8yUve2tD6AuutBbfNqca_-4E-NIhtwC-cqoZEhZZvU-guSqByX4tpksOhC6flIUvqNqtwg6jTV0VJ4-i2n4eVeXCbeqjMkkwoYum7VFB2Au4DxhH0AXuEMtTSpG56avqhRxj4YWlHogjOgWTuTBcybJ3u1-EWC11Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JhOI1qSOeQBv7fJ2I5ledwZRrk3A6_ElPt23uOycigJ6Y-v8ZV8ozJZtH2dZXMuquj-qw5pxyURBIr15mmfdjH8n1jDso2ufb4vVZkjiXBQTaiuhS4F00IT7gO1H7jkygjux9IKFFr61zg3OgJV0iaaCdQ85vFS73eSu-_hjKOaE1CotysLJNcRo_kuU05f2JVVf0jvHqIcN4s_w0YvjMkeLL9vFrJ1sMw4iiIKW0j9jYSPIKoy_fJJB_-1EX1rp8zAeEk59fq1pIwsaFhwFyTStOriWGuNlZPABpieoit_cqQVVUX5g6qq2e5fnVlLQxxpql_7gB2bEND0uLYCRNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AKwfM_X3FE_AeImdM8NQe1YRMV-g7m6XmnCzrFWLRr0hTm1LeCM2_WoGmgO0N8h5CGXBCKHkMMm6Qf4G4CnD5hqpi7NvYk5ZK7QjSl0HedRC8DztagWMJWw_30QfY9Zx6LuCxnKmsIWqJHqgJNXSOCqwHVfNLLP7gumNgbUboDKAEIc-3ubVCpnE3iPRz_kXtT7HcmbXSq5TkKRkbhglb3BRZtFHhIVcekRLc_vb9erQNYS2BvtXHmNFhnbsOGnEygfE681MgC2zdwslC14m3pbmxiPCq39F0OidatbEAovCfQnB6t6v2a7_UWaAjKaHXbmBswoRs7Eki83LeueBXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EyjhiKOckwPB1n0pftWfjG3vZmQ3Gm1Bbpaa6XM0VOx_3lf44KIGDmaDSSU6bszdVEERl-2sMggomgvIf0b8J1uFHRS24lDyOAbkZ9vE8zVRJQxyT3R7QgcQ0_zYkjFu2kAAPHhGwxyYXGehje3cxue5n_jkIHncu175S513fW2Ext7he3kAjkyUfFZQ2TNa0pWx5y5_aln6q0tvRQ8u4Pqx4e87tSvW-LNAAfbEV4yM6SyLtVrM8JG6m7vwmYcbwEFpiuXyoFkbWjN6dvF0ovp6QtM59NO0brFoXHhgImy20_6fq304O9JupfpWZZnxLv6J7gw9BDR8xvB0gulAWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
رنگ‌هایی که اصفهان را به نصف جهان تبدیل کرد
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/663148" target="_blank">📅 14:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663147">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d2d818d7e.mp4?token=RUHOqOwFlv-Mr6eJe8w6mhOvC_xjh9WMT3ZLotzFCuJGKh2VaoWkEQFmmYWgV5Flw8h6BrIWrXlet0fNLPDPjriuwn6WKlcueiEXwA_YEAN6-OelnA_DfcoqGZSS4oYLNr5OXziJ7_3kYuP3AVR9U_ER2hMOcBA_uI22L1086WhHH3NHKj7m7ZTdbH8KMS0UGqTxb6rYmiEdARTLw5oK7YEhkbQ0n_sZig0UL2UEiBC0emnNP3WLwnP7srvh5c8aXgBdwJ03HwqR_z9GdDh90EtSvAhMHAezVxaASm62U_UmSTK4SLBNTsBvleOcTCCsxk3LJ4EErJTu1_ZNX1Axhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d2d818d7e.mp4?token=RUHOqOwFlv-Mr6eJe8w6mhOvC_xjh9WMT3ZLotzFCuJGKh2VaoWkEQFmmYWgV5Flw8h6BrIWrXlet0fNLPDPjriuwn6WKlcueiEXwA_YEAN6-OelnA_DfcoqGZSS4oYLNr5OXziJ7_3kYuP3AVR9U_ER2hMOcBA_uI22L1086WhHH3NHKj7m7ZTdbH8KMS0UGqTxb6rYmiEdARTLw5oK7YEhkbQ0n_sZig0UL2UEiBC0emnNP3WLwnP7srvh5c8aXgBdwJ03HwqR_z9GdDh90EtSvAhMHAezVxaASm62U_UmSTK4SLBNTsBvleOcTCCsxk3LJ4EErJTu1_ZNX1Axhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
انواع اسپرسو رو بشناسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/663147" target="_blank">📅 14:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663146">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKqUCh9B_rRB17AbQTNpBHfrRYiQwyERXCjI2cbMKHsXrLvFHpnUWybuf_n7WirWThzKI6itgcoqhiH6fuKM2kAQ3-a06kjN73RKr-jbFc7gwFvn8aNITSRe6FzIHp4VZXRSI-ABa1KaIcEOuCsUr4YIpRhOGDqARQZVlztKiBInmGUyXFiEGQKLvn6X1_Z-DQX0eGUKSnyHXliynDXQkypJQoryBhR5VHfzEP7iHeSodIqWCpGGP-2HHz6d2B6Yqo_GwQLk-XJn9DfBlzVE0EPSjktVJ5josi4rMrGTtcdfrfEwS7H9llZzbJfrLUG2wuUxHU2BxYK7SVetyZMddg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرمانده نیروی قدس خطاب به صهیونیست‌ها:
اگر امروز با اختیار خود عقب‌نشینی نکنید، فردا با خواری و شکست ناگزیر به فرار خواهید
شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/663146" target="_blank">📅 14:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663145">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38b91e6f21.mp4?token=NLt09eHjY_UKE2oOEkOVdL4JLbdy-eFJj2FJ43NuzF8hUwhXJDxeGgUg3AbbGj516KqDxR6aTWAfH7jvUJ7l_pjBW4NBDPp-3WV0emWXWpbRXM8W7YFwNR9LYLraznME9caCDaPHzfw4ql3OSpMq37jN9lqVPWD1xEqPe2Fsx-x7bc8t2ScULJma-vHTorefygXsCQnI-dJdcVFsybGXitt9rCvsE5ydKq1X4Wu3bJ9OkomqM9DPwfu-MYEy_FbGLRY5Cysk-Vl4OFHjiofMkB8xT3mNsGnKGmsSOqp_H6GTd1zedSPMyyCpsDhEStSIWncQ-BZHN4DBDgZrGUDSgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38b91e6f21.mp4?token=NLt09eHjY_UKE2oOEkOVdL4JLbdy-eFJj2FJ43NuzF8hUwhXJDxeGgUg3AbbGj516KqDxR6aTWAfH7jvUJ7l_pjBW4NBDPp-3WV0emWXWpbRXM8W7YFwNR9LYLraznME9caCDaPHzfw4ql3OSpMq37jN9lqVPWD1xEqPe2Fsx-x7bc8t2ScULJma-vHTorefygXsCQnI-dJdcVFsybGXitt9rCvsE5ydKq1X4Wu3bJ9OkomqM9DPwfu-MYEy_FbGLRY5Cysk-Vl4OFHjiofMkB8xT3mNsGnKGmsSOqp_H6GTd1zedSPMyyCpsDhEStSIWncQ-BZHN4DBDgZrGUDSgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ماکرون: یک نفتکش دیگر را توقیف کردیم
🔹
امانوئل ماکرون امروز خبر داد که نیروی دریایی فرانسه یک نفتکش متعلق به «ناوگان سایه» روسیه را در آب‌های ایتالیا توقیف کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/663145" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663144">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24b9cf430a.mp4?token=MUzYruUc6FFBF2LAWHf-35mu_tqHEDWK9P19NbQ9bo9p5qciYRkUhPoBlGC4RNuznSil6SvVTCuE5eq7uUYgRO4MsUDSMM3h0ecu9F1u4CvIXOFz5-ipAPlGpZ2MMjNIdIflM5Of3z-LChX3DTto0lr-Npfzulx349r5PIwRjr_TNLo7PBr1C4zj6or5oWYpnIx1OBOE8Jpt8rK0ZjDdhNPcrra5s5PbBRX8AjwAWwc45h6LtbMOCtqS4valRX-SDCmRH0YuXYc5Yan5tBEXMCBCtVvC_xL9hGgrpidwGD_7AupU_WYgi3tdsvyTSP6jN1n3AkFYnMofykDN2bdXEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24b9cf430a.mp4?token=MUzYruUc6FFBF2LAWHf-35mu_tqHEDWK9P19NbQ9bo9p5qciYRkUhPoBlGC4RNuznSil6SvVTCuE5eq7uUYgRO4MsUDSMM3h0ecu9F1u4CvIXOFz5-ipAPlGpZ2MMjNIdIflM5Of3z-LChX3DTto0lr-Npfzulx349r5PIwRjr_TNLo7PBr1C4zj6or5oWYpnIx1OBOE8Jpt8rK0ZjDdhNPcrra5s5PbBRX8AjwAWwc45h6LtbMOCtqS4valRX-SDCmRH0YuXYc5Yan5tBEXMCBCtVvC_xL9hGgrpidwGD_7AupU_WYgi3tdsvyTSP6jN1n3AkFYnMofykDN2bdXEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
حداقل ۳۲ کشته و صدها زخمی در زلزله‌های ونزوئلا
🔹
طبق اعلام رئیس‌جمهور موقت ونزوئلا، ۲ زلزلهٔ پیاپی ۷.۱ و ۷.۵ ریشتری در این کشور، دست‌کم ۳۲ کشته و ۷۰۰ زخمی به‌جا گذاشت.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/663144" target="_blank">📅 14:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663143">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e10e228e.mp4?token=eTOXf15wux4KEjbLgfNCHSZf0iizfyxtRxoVmSuWjjoibdDNUndTqPORYH9zjWzfY4eGjp95l-GQcHycK2tZXAivHrD8ILon8wfIB9p_st5Dk1KVo7P0PARN56pmrsKqxoyd8iLTuMr1SLacqtA7EUjZJs4XLwNrokatH1LOhY2tr8KgYN8pUDpQLmEWgdWrCv0w8ldNboi9tjdfJPHKFtsJj3kcQsPV2BZhptBVbokOokcQ0cWXqr1c63uWKHU0exteppM48njmi6VuBP3XyY1Tx_5vPjPOaHUMSQJvVNnap0nKPTLzuupKk_LM3BouuvHHHJlKZnvZDH-D_h08Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e10e228e.mp4?token=eTOXf15wux4KEjbLgfNCHSZf0iizfyxtRxoVmSuWjjoibdDNUndTqPORYH9zjWzfY4eGjp95l-GQcHycK2tZXAivHrD8ILon8wfIB9p_st5Dk1KVo7P0PARN56pmrsKqxoyd8iLTuMr1SLacqtA7EUjZJs4XLwNrokatH1LOhY2tr8KgYN8pUDpQLmEWgdWrCv0w8ldNboi9tjdfJPHKFtsJj3kcQsPV2BZhptBVbokOokcQ0cWXqr1c63uWKHU0exteppM48njmi6VuBP3XyY1Tx_5vPjPOaHUMSQJvVNnap0nKPTLzuupKk_LM3BouuvHHHJlKZnvZDH-D_h08Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
عزاداری حسینی در شهر نیویورک آمریکا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/663143" target="_blank">📅 13:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663142">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCKw9GUL94BFBL9k3ZYwwdEPHWzvBGO2Is4nN2m2ti4LDZ7xLqc1N11X4OQ7_GcxpZYNswnuD7nRAYR2VZx6bc9UdbxIoJz3xHIAnGeJXpY96VSnaJSDGRQ8sd85_s3jyIJcqzE_7z-VSVTZd48LOR3gg2CPX5dVLfuIDuGLMxs01EOkQQ-U2wQ7mMUvL56Pyg0l8I2RdmPxhCaDpxJ2lSrizo6TwAHcWWdoHHRCDMFBNiHMcEUfJZDychVvhjT_3m8owJFJwaCgExU3j5_KqkmlWcQEnE0xfTwtNvaMdBX7HjZ7BpnzsDPMmYOmwQfdyeCy8zIJsdVT3haMQ9_pWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پلاکاردی عجیب در یکی از تجمعات
🔹
تصویر پلاکاردی در یکی از تجمعات شبانه اخیر، با مقایسه مردم ایران و کوفه و اشاره طعنه‌آمیز به«خرید ذرت و سویا از آمریکا» در فضای مجازی پربازدید شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/663142" target="_blank">📅 13:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663141">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔹
رویترز به نقل از مقام آمریکایی: اسرائیل به نشانه حسن نیت از بخشی از منطقه امنیتی جنوب لبنان عقب‌نشینی کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/663141" target="_blank">📅 13:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663140">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آن نیم دیگر من که تصویرسازی می‌کند/به ازدحام فکر کن!
"زینبیه" بیت رهبری را نمی‌دانم چه‌طور و چه‌کسی نام‌گذاری کرده است، اما کدام‌مان تصور می‌کردیم که تبدیل به یک بلندی کنار گودالی شود که قتلگاه است؟ فکر کن!
به آن‌چه که اگر دیوارها نباشد پیداست فکر کن، به این فکر کن که نمای آن گودالی که انفجار درست کرده از زینبیه چه شکلی است؟ که یک نفر آن وسط تنها باشد، که ازدحام است، که موشک و دیوار و سقف و هرچه که تصور می‌کنی به یک نقطه هجوم برده است.
آن نیمی از من که تصویرسازی می‌کند سهم بیشتری از این چهل و دو سال گذشته را زندگی کرده است و همین حالا که نباید، از خواب بیدار شده و دارد این‌ها را مثل روز می‌بیند، دیوارها را برداشته است و از زینبیه به قتگاه نگاه می‌کند!
ایستاده‌ام و سرم بی اختیار به سمت جاذبه‌ای بزرگ چرخیده و جاذبه آنقدر زیاد است که دوسوم بدنم را دارد از چشم‌هام بیرون می‌کشد.
شب علی اکبر است و یکی با صداش توی گوش‌ام می‌زند:" یه لطفی در حق من می‌کنی؟! امشب منو دعا کن!" چه می‌گویی آقای محترم؟! من اینجا نیستم که! من کربلام!
علی اکبر ما بود پیرمرد
دنیا علی‌های زیادی از ما گرفته است، علی‌هایی که بخشی از زندگی ما بودند، علی‌هایی که نبودن‌شان حفره‌های بزرگی توی زندگی ما ایجاد کرد، علی‌های بزرگ و کوچکی که رفتن‌شان را به چشم دیدیم و آوردن اسم‌شان هنوز هم بغض را به گلوهای پیر شده ما دعوت می‌کند.
توی این همه علی اما بزرگ‌ترین داغ، مربوط به علی اکبر بود، بزرگ‌ترین علی که خلاف تمام آن‌چه که شنیده بودیم جوان نبود، که پیرمردی بود و حوالی خیابان کشوردوست زندگی می‌کرد، با محاسنی سفید و بلند و لبخندی که همیشه‌ به سمت ما نشانه‌گیری شده بود و اخمی که به سمت دشمن شلیک می‌کرد، همین بود که اشبه‌الناس زمانه ما(خلقا و خلقا) به رسول خدا شد.
از آن پیرمردها که فکر می‌کردی همیشه چای‌شان دم است، از آن‌ها که تصور می‌کردی هميشه منتظر مهمان است، پیرمردی با حیاطی کوچک پر از گل‌های عطری که بوی خوب‌شان را به همه تعارف می‌کنند.
گفتم گل عطری، یادم افتاد که یکی توضیح می‌داد گل‌ها که تشنه می‌شوند عطر خودشان را آزاد می‌کنند تا این‌شکلی آدم‌ها را صدا بزنند، بوی عطر توی تمام خیابان فلسطین، تمام خیابان کشوردوست، توی تمام خیابان‌های شهر و توی تمام شامه‌ها پیچیده بود، یکی داشت ما را صدا می‌زد و تشنه بود. هنوز تشنه بود.
ما اینجا مردیم
فصل مشترک تمام روضه‌خوان‌های شب هشتم یک شعر است که همه حفظ شده‌اند، که همه مثل اسم خودشان بلدند، که دو بیت است، که دو بیت است و قدر یک کتاب روضه دارد، که روضه‌خوان‌ها فقط اول‌اش را فقط می‌خوانند و مستمع باقی ماجرا را خودش بلد است، از آن روضه‌ها که به دهان و قلم من بزرگ است، کافی است یکی بگوید:" جوانان بنی‌هاشم..." و ما خودمان تا ته ماجرا را می‌خوانیم.
می‌خوانیم که علی اکبر ما را، همان پیرمرد سپیدموی را حرمت نگه نداشتند و چند روز دیگر باید برویم و "علی را بر در خیمه رسانیم..."
من نباید آن شب به زینبیه می‌رفتم، درست نبود که بروم توی قتلگاهی که خاک‌اش هنوز خیس خون است، حالا آمده‌ام کربلا تا سینه‌ام را بچسبانم به ضریح، شاید قلب‌ام آرام شود.
آن‌چه که ما توی روضه علی اکبرمان علیه‌السلام دیدیم و شنیدیم بزرگ‌تر از ظرف ما بود، اگر یک روزی خواستید روضه مرگ ما را بخوانید اینطور بخوانید که ما ته خیابان فلسطین مردیم، یک جایی نزدیک یک گودال!
به قلم مرتضی درخشان
@TV_Fori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/663140" target="_blank">📅 13:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663139">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔹
پایتخت ونزوئلا بعد از ۲ زلزله ۷ ریشتری
🔹
تلاش‌ها برای امداد و نجات در ساختمان‌های ریزش کرده ادامه دارد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/663139" target="_blank">📅 13:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663136">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YJMi-idwNWgEitv9IelnMvn6741rrsivKNk_TlgczBd4vJgCE1iYBLhl_wn2gKh-jOoOkzaRMDRDJoxUHt7lXfhVPKvqRI4SCJUqlQP52OaKWZXXyegvrfCBv8UI1uOWuznYz1lZxvFFgx1B9ew_tAz-hN0kMOJqB2vOHzT8CUa6TjLqGUpuknEfQ_DQPtsryOsy7XEtyZxQb5q2Q0os3FemarBRP2OaQ3inFJ5Uir9gNelfBiwp2atldIfiNf68JFljBgNBVMI1bbH5As6nCTCFw5_teegV3_fBuUaS6D-UuKlKwVTEOTplrhI4MWTq6XYFUPRikldAGYxCpFVB9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YvsOJ2tjQvozHSoeLMg9nD1VJSfcsqB95PNCx-URBR1DsJPXr3vtnp0-UTiYGSQ25DkKjRd_R2JjGwtrVc6Ymw9562OlKnNcsZ7PR_GlU2cO1-Yj3EU6nOhW7dRSFXxBH8U3X232jFiJRu1rHwsMXXrVw6H8WnPBm7hBeBmvm7OdEUeZpQSFEoLbGKCySEFltxCjsPIhycY7p12AShLkZowinB3rOefHsMAbP7pr3zSNAkKGgEFnBr_CtKP4ncNYzI_cg-ym1XP2K2MeZOfAXb9t6mYDyHmR1F78vGB2tq4F8RPL4wBV8_wbP4gTax5cVz3DlP6sWifrOfb9TKLEdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MmV8s4QXClr4f_ltbcKy2Eijx_8BSMGCXhFbOjns5YkR_HqzbYwmnQuPuv8zqynMH8J4XPgcpjs2wlDgMr4L7iLFZl4izRcQUJ9JC3phA8MdbjRr3ObLfZWKBZx5JQFJ5MTXQg0ojk_BKi0GU3Cx8od2mWqVZwdW_t3ZAlX9hYhDm8kDlsfl_JIpt5TOeku7sFAPBaYRTWrMx_gS98lOcyR1w4yTCJ5vCUMT70-p7MqYquAqZNRhEfO-_PJY_u6r8b4Wx6nVk401OqhhPMkWvZ8gatSwt_VNe7o5iI89fpJkD1Vv6YhvB1anYZ5wkSxKeuX6NZouTl0rvl7745KkJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
پس از هشدار سپاه، سه نفتکش که از طریق کریدور جنوبی از تنگه هرمز عبور می‌کردند، در حال دور زدن و بازگشت به خلیج فارس هستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/663136" target="_blank">📅 13:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663135">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIKFG0Lj6KtHcoBhO-dqMBt81I3YsZeoQZXGOq02VuzuztsMScPpmoeQmhC9nskvJcOO5EeyOe0Wml03GCMqrEsp3Hm8WRy9dEJPTGWWREyvhXlng6XIAoJw3pMB25cTwa_WOALpxcYStEVimx0aXZpu6t1c3DxrtlYEXBRGAd7EG5EBwkPS-9sJjdUJgu4_ES0r93odI9cP5HFgqH12jSC779s90ccTxX7s5cC67n-tob1wcFvg4AET5HOP-wn_ls_ldrqAYWur2yCTGFo8O-zIEgquswUCk9oM5TG_EPVQ73Nu0K3TS4ntqKZXxpZESz8_IFWmHGjgDT-NM03b9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
علیرضا بیرانوند در جمع ۱۰ دروازه‌بان جام جهانی با بیشترین تعداد دنبال‌کننده اینستاگرام
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/663135" target="_blank">📅 13:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663134">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔹
#چند_خبر_کوتاه
🔹
قطر: کار فنی روی جزئیات توافق ایران و آمریکا آغاز شده است.
🔹
دبیر کمیسیون امنیت ملی: تنگه هرمز به شرایط قبل بازنمی‌گردد.
🔹
وزیر نفت: حمله به زیرساخت‌های ایران، جنگ علیه امنیت انرژی جهان بود.
🔹
سازمان ملل: ۵۷ کشتی طی سه روز(۲ تا ۴ تیر) از تنگه هرمز عبور کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/663134" target="_blank">📅 13:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663133">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3efc1df48b.mp4?token=R45Jp-kzU2L6GVAzD1z_uxkBq7C9VWrmbwjcLigYccY48U7JwSHfBLo5rfcbv_1o5upXT8Ag0N0Er3ADNkETMnA7Yku_lMQ31leiYHFEZC1A7koMv9mKqySrCK1MDOAt9_sqaihX-Ca10QW5wU87qJJU4efB-JPlQXMK7l7PNFpjMU_ymlpiTEgn9Sk-PlIPB5WC_mYN4OomvZ6KV4HtW9E-oEgrG55cAfNCTQP-WU5gmE4g71H9aSyzIG4POodWDz3LCpf4-r2jhL3X7ZCI0mBFw4FX4wrNbKEzBVwng80OJjjIMjCGruEPsoIo7ptLIJiKTaJ0yYt70yzolHCGdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3efc1df48b.mp4?token=R45Jp-kzU2L6GVAzD1z_uxkBq7C9VWrmbwjcLigYccY48U7JwSHfBLo5rfcbv_1o5upXT8Ag0N0Er3ADNkETMnA7Yku_lMQ31leiYHFEZC1A7koMv9mKqySrCK1MDOAt9_sqaihX-Ca10QW5wU87qJJU4efB-JPlQXMK7l7PNFpjMU_ymlpiTEgn9Sk-PlIPB5WC_mYN4OomvZ6KV4HtW9E-oEgrG55cAfNCTQP-WU5gmE4g71H9aSyzIG4POodWDz3LCpf4-r2jhL3X7ZCI0mBFw4FX4wrNbKEzBVwng80OJjjIMjCGruEPsoIo7ptLIJiKTaJ0yYt70yzolHCGdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
بهترین نوشیدنی در حین تمرین چیه؟ حتما با دقت ببین و امتحان کن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/663133" target="_blank">📅 13:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663132">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-LA7cPKk4mbNf0XYU5Vn-CoN0Yi0ATf24fwcQAiqciQFve_6KHzxSkBuBxevIRls3KHV1bEHnMdGteC3UVwviVMSJZz5MQDvePLFbvwOwyiHZNbcXa_pIZb8BcqNMuveP4tMr2ZUFlhvsEryhbS6hhYnAaw_598ZN2HnH6xzqvM5b-0R8G6PYutYqtFN-MqGMtoL_qDGjJzkWHPTPtZ-e7qmCRe_64qXw-e7tE5i-LFM4kA08vyi1GoaOpq-gyEzS1H4oqjJkBR7Ku-dZHSiMAW_6GH4v69q4OpenJ0eyjxe8AqG_kEfisekho4uSRYAhnopb61TfkjBqvDt4d3CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
هر یک از اعضای تیم ملی آرژانتین در جام جهانی، به مناسبت تولد مسی، پیراهنی پوشیده‌اند که روی آن عکس خودشان در کنار مسی چاپ شده است
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/663132" target="_blank">📅 13:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663131">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3cba0fe4a0.mp4?token=mCb2t165KXGSZC6YOeV4Z-2a3jM1mWU_Rqk05DGW-nuY-XB3yEunncURkNB49jjmEjE57JIPvWsr8PDdGdmZHc2jxi0vMxr-l8vZDHzomCDeZ7agomEFasWIjygEJHkFxirYuObhWbrqkcCPY5XkJT2acY0uuqRHLBn7hdOobjGe2PxzpFKw0TK1X7JBlrmCneC1tNPX-s-S3I2vr1ime-DX1ULeCiazhriZkDtqsqt_lHAXFJXB_FG0AVj0Od6xoDCnf0DIfwIV5wPExWBOzKzjThff6yOcqf9adTw9E_-JUHlLwZaBQDvcNmQyQDl79OIBoh9vzNZjz3_kSv9awg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3cba0fe4a0.mp4?token=mCb2t165KXGSZC6YOeV4Z-2a3jM1mWU_Rqk05DGW-nuY-XB3yEunncURkNB49jjmEjE57JIPvWsr8PDdGdmZHc2jxi0vMxr-l8vZDHzomCDeZ7agomEFasWIjygEJHkFxirYuObhWbrqkcCPY5XkJT2acY0uuqRHLBn7hdOobjGe2PxzpFKw0TK1X7JBlrmCneC1tNPX-s-S3I2vr1ime-DX1ULeCiazhriZkDtqsqt_lHAXFJXB_FG0AVj0Od6xoDCnf0DIfwIV5wPExWBOzKzjThff6yOcqf9adTw9E_-JUHlLwZaBQDvcNmQyQDl79OIBoh9vzNZjz3_kSv9awg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ادعای جنجالی درباره حضور نظامی آمریکا در عراق و استفاده از پایگاه‌ها در تنش‌های منطقه‌ای
نجاح محمدعلی کارشناس مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
آمریکا بر خلاف آنچه رسماً اعلام می‌شود، تنها پایگاه‌هایی نظیر حریر در اربیل، پایگاه بلد در نزدیکی سامرا یا عین‌الاسد را در عراق ندارد، بلکه مجموعاً حدود ۲۰۰ پایگاه نظامی در عراق در اختیار دارد.
🔹
همچنین رژیم نامشروع اسرائیل نیز خود اعتراف کرده است که حداقل دو پایگاه نظامی در عراق دارد و در جنگ علیه ایران، از این پایگاه‌ها و حریم هوایی استفاده شده است.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/663131" target="_blank">📅 13:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663122">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M0MFAWPkxo4ceJtHOUg7KQ7b7WJZaCZN8A-9b2vDuw7Sewt1M_e1njIZ0q-00NjDWT05jR-evU2UubOE3TV1RuoY6bA7D4La5V08BAf6enqwWpGp3BV-JnHYShC8sEkXl7F_6BMIhcMeVTaaC_WVRseI9lZPnvXtLSYDvO7-ViyPI5gXNFrxxw65uvPEpydwVx0x3-4zbeVolelG1ICte0RYooDu8lKybP4TVFA5QQHlx3piowf6sg5gf8WR-9SWAirvqT5Atma80GZDwRKVgzNEl4ozRnf-Kb0gp35r4gaKxoKWVyirhN4QlSyVzJeUNoOWCK0Wg0v-_7A0FIkklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g6Uzx3HBTqhLCGG3DPN2v6FTq-cmjPHgxsZYALrWHRZQdtlvOBq41wWqVhTsAt5nKLCowZSZCNuKCbMeohj_1zBT21ULXPB5hliv0-T_zOXCRLZlFOQmxMIcClFJw9qw9CzhNA6FBjTuXAdakbtkdW--7XvNbcpi3wHjrqrg7IqhJayyDeRJ9kgxPRW0dte32Hie6zA3gptwXzJxgjnQWph1EQL9mlFeGv0WwvPndYLlvVRRv-JRTjorWxNAyanei41ciBwHJKYoiyd_L6lxNnl3iUURXKGfLsMu8wqWcuu-t0Stn2dK_n9AYN31MTNeRaKOY8vXW76YT5NMn9Uqmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g2WjBOyjus462iVraEhu0xd1R0Q1b6Qv92Znf19Oymx5ySiY-l0qJ7NBypGlWktJ4ffwWovjaP3uYO0x4W3ozaWSUTGqKV4EDOVqzK5hrh5ADShP9NhWAnL0l2N3oNAYN5BfM-nMJ8l-Lr_5AoYLxYkjrPzt9AdJEC4bb40gNBzZV4uLOk6RlQWedUqGgcYvoEXv3nwRXZnHzF70ws7Fp3KuoeLA0UN8xelv1Ch7jaQGhxJb0UMFfZ-CrH8kwh1ieK4UxYjCfsA_-oW-Y1mv27A9_I660V5s5AvXXZ0AUabl3BsoJr176ELyY0EaSO7ergrrVWPYRdu4MzO1RK4VvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GwwVthoIRRtj5aVfgtgTGdaQjd72UVSaMDPu7i4Xc_afT1lGuAPfPtqyQLK1J1NIGlxwZN3aWFLB0LQ12HWOwwAkzwupwyCRvSUVzAlmSzQvY01vqRkLVw8Jkv8Jsrf6oJx7TvBucVA-sXJwQ4AhRK4X7v-tSavoNRxC0Nni2dz9GdSREMWth67yVhk-X3BJy-NKwC7h0bAFKW8cu0PuQeLn0TzcwefnWj-r7VeMqtd1GuFggky3nCaN72zKCB3SVvGdxGdWhNLpkyxr6c0GvmBKdsJRshkMBhpUdhVa1ud9bq4yFJEzF4OejsJQojj8mNUFB1_FWe2Tu4KRThiZkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KCC_8T7PZWZqn320EmlNVI0DBtkCVkaXeLS4skZIigTyS7Pj9ZtewpO0CmQcqsZfzJc9BHy6tmXmIKw3DnY8Y5Mr7Dag4ckAFg9spjNYl-E_d047FoeqR5KUX9HYB94kZCLmUtpGSuK2qBBYYeGU_bRlkZlyCoAaZiVu3nkKYO4bK711SzuS10ZHkS89jinvWe8wlqeoUWvSxwW5tUhaH0gNdW543NAuWskPeWhnOab7BlFWEz0gTFgG8RIPlZiGJtM7n8OkCxK0mcC8jsYlekyNlP7HpcnFvwdhJkAdA0M1AOgi_wRQUoGmpHoNb6UXHuW4kLkvISdDIUI5lbEnvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZU2w_pmjNhdl_nj_o4K1QH3TA52sxttLP7Hp_lKCmjQamuVIv3HHpknBuIFlmewFxyHaJjeoHyCowvWNl2zd89ARDrRjz3-QwMZl5ssmwRUVp3qU0LZhLRFn8y1Unlz8zxDLnd2wTDQQIsltutRm6B8s-TFP6zjU9cAg88nD9Z3nB2VHULC3p1cDF2KnCg5kMj1MkxA_UiDJ3WimD37J7bIFeyQjFfHqUzI7l5P1dHaH4hC08gpy-W7oeWVF2LO28QkrsxZgwV6CTQvzBEx-KF4dgxHO9tvmLlF_J9zfzmBSlngy0CU9qxf6IsjCVxHvfoDAz5_CG5gAq-sBd20vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XsnhF_WXlXAwc613RAfWoZvAXVjpmZLj7gilrkipJIcG6Ma6Gdwm1suV0rf5Ec39HYe6_Dhdj1rjJX6GiQ8DXFeqCwr0iHTr0A2ynaYvnNHFYdYu9o_vsz-YRcY6BDUahXsIXWSm8b777medcZi3r2Rmtltiv_RYbUQLJOmmy9Hs7r2fC5h8pykdc0tl8ysmcR0HGxbi1cE5lEzD0jQXSEq-5nccLtxUK1N2fv8rlUFueX9b-C3__cg9piHwTHShz-4mRHHLE6TScFlNsYK2CXovLCCSaniu3xTo6ATSLuN3NsVwe6FNb653ODExQHElXKfV_-Bfwre9KdGFdq8dxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/klA9lPPrXP2XHjGobVnP30LWljGm09-iNoXgbs8zfOt3GVZPG9x62-n56sTFsbuky2Jnlnmjbb-CuZvCgxxJ-x5SvhDrs5uwj3f6pTIeJmb8mA6U7_ROV8nroZd0WwlYIjtQDK7BYQRORlhisSbTjW0bBPd8IGOsjW_FhOfRFGmUo_giO2T1Hyw9nG5xQiW35Sz3Eo3lv1yzktPhrpiJFW4rX-qq_tGe9emgF2QZ7FS_lEr43au14kBO2Ywu9yfKA1pjMbFrqPXiN7M7PmzdPkWMHLQYwaN_9-KKXwlYe3vZ06JKmneAOB1ucDmJ7Ouk8eL5dk5je7lwJQIvK55qcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ue_SR4QDmqo6yFOJF4FwEI5OX5c2wdWBUsP2L8TTNAQdDPebjJZT5Z_qMk-KWCD3iPq4IP8WLd0DHXKGy7maDWqn-osAZvo_Testud-FgV2wYQuaa1cXFt1C6QqJ0Jq2dKLE-re-TsStrKnMIpTRE_uKlwmu6X7aYVxXiEe220BFpjNxugq04WppNv4xGpUwMTxFq5UOKVlsWf8tS3OgsKJFJnHhDhtpDonXzGPXGBTG_8qWr0VqnXSZsbmJWvLqxKIuzVYkt8TY3zdt6CiqMMx6R6hX5RsyoDIwku8yp9p5qf14LgGEZPVqS7FHgrzHPh5UFXnjiSYRy8zvmZBHJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خادم حسینی
🔹
مخاطبان عزیز خبرفوری؛ اینجا محله شماست؛ تصاویری از شور حسینی و خدمت‌رسانی به عزاداران در ایستگاه‌های صلواتی که توسط شما برپا شده است.
🔸
عکس های خود را با ما به اشتراک بگذارید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/663122" target="_blank">📅 12:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663121">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82c049db14.mp4?token=RYGO7reSJlDVKLTE5X7C9Mf46oW0tkyofbIOjC1Ha-O1QJb4l3huXqb48qcDiQCEJ9RUWPwd1W6AYVJ9mlaWpW89wWV4_cj4EwTmu9eamsFnK3OclGIvnqRTBOZ7gb0mPPn-KAQRnTDhqasCPwspQD2sl3U05SM391veyJu-faa2PGuQDJ3y0QGZmUI0NlolTKNrdvVY435D4q56B8o3P1H2b5BXGmPKzZK8h6dUiT0mMxLUnEItASIxU0MX51c6XkbO3j_wUjkFDwRxDP-TsHvhjisvYv76GEZ9r0RU6fBL8TnoFn4ibwekyNvv0RynnMAQ-HC8meYrktUAO9CPGCQL5suWTI6v9J7jGv98flkiEf9yjt6YxNNgmvwWP0U73E5mgtzmOVNYU_Si5XWbqdqHRzNdbDuHzrn-NKICg_YTsQcblVBRvDj-T_JN_mdoVZWNJvIrJs5A2QdihQJKx4bvFWI0We4KIsjcllDW6no6wjVgimP2LVIhfTUBIiztQu9dM6TKsBZFPOYxQdiVcIbt9A65Z5gVAsLKU4pb6tfe78ut5GM-GcLM9NNAkdASvpUgmr1LNM6hWN36r1GN4KTIbu8UBDn0-LWcJYshS06smZrZi7EG8dbguT7MTGs3HcZQ5sGVoDEcmD-aus3rU2KEo31HFahwNcR9dWiBAxM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82c049db14.mp4?token=RYGO7reSJlDVKLTE5X7C9Mf46oW0tkyofbIOjC1Ha-O1QJb4l3huXqb48qcDiQCEJ9RUWPwd1W6AYVJ9mlaWpW89wWV4_cj4EwTmu9eamsFnK3OclGIvnqRTBOZ7gb0mPPn-KAQRnTDhqasCPwspQD2sl3U05SM391veyJu-faa2PGuQDJ3y0QGZmUI0NlolTKNrdvVY435D4q56B8o3P1H2b5BXGmPKzZK8h6dUiT0mMxLUnEItASIxU0MX51c6XkbO3j_wUjkFDwRxDP-TsHvhjisvYv76GEZ9r0RU6fBL8TnoFn4ibwekyNvv0RynnMAQ-HC8meYrktUAO9CPGCQL5suWTI6v9J7jGv98flkiEf9yjt6YxNNgmvwWP0U73E5mgtzmOVNYU_Si5XWbqdqHRzNdbDuHzrn-NKICg_YTsQcblVBRvDj-T_JN_mdoVZWNJvIrJs5A2QdihQJKx4bvFWI0We4KIsjcllDW6no6wjVgimP2LVIhfTUBIiztQu9dM6TKsBZFPOYxQdiVcIbt9A65Z5gVAsLKU4pb6tfe78ut5GM-GcLM9NNAkdASvpUgmr1LNM6hWN36r1GN4KTIbu8UBDn0-LWcJYshS06smZrZi7EG8dbguT7MTGs3HcZQ5sGVoDEcmD-aus3rU2KEo31HFahwNcR9dWiBAxM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
صعود مقتدرانه برزیل در شبی که نیمار اشک ریخت
⬛️
🇧🇷
3️⃣
🏆
0️⃣
🏴󠁧󠁢󠁳󠁣󠁴󠁿
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/663121" target="_blank">📅 12:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663120">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhOW46K1xnGINKEmnwS4axCRmzB_6SJkv8e7yxpkVfVzX1M8pSPRAN_tISxDGAH7jNv24gEgjmUopTl7mS9njI4BKBvH30Xs-80BWjhD3IDMUxd6DR7NPi-jTHuu2WBKuqrSAWy4qwoummvnca1j3iMyddIhmDwSS9OF1pxXKE9K7BZ7jm6IzPIZMjGfAud-62L67CMZUHilUm5eyIdQkAePWvMjRSxiQoihe6xCPhBYAhRuVo1hn2UINksZYegI7fLd_wzKLEg1b6Ox4Ap4DfU24X7iWHLGo4tOlIv8ku1vAtdpVDeby17CvqRKWUM2rMpb1Ryn21CFd18kRVYr4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دسته سینه‌زنی بزازها، سبزه‌میدان، یک‌سال پیش از ترور ناصرالدین‌شاه
🔹
عکس از: عبدالله میرزا قاجار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/663120" target="_blank">📅 12:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663119">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔹
رویترز به نقل از مقام آمریکایی: اسرائیل به نشانه حسن نیت از بخشی از منطقه امنیتی جنوب لبنان عقب‌نشینی کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/663119" target="_blank">📅 12:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663118">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRRTNtdteVd666VSxkyLHWhusrLDE39a75GreUISzWf2pNSasxQzoiTp5zxYg3vFXhmeaC0HConGhu6DIEfbzY8o97eYi1Sq6athv1axicCgtvpqxoJYqTcL2kkylZkIox9CRNJYOhJytDYeGr5VT7AHSLqJ56rNDpcp4HspRxIlJvLF0MRfMIAbSw-mJN1cPdE5d5gBK2Bl84ODDULdkaGZaWLIC3CYShSD1_BTxPaJgNuIxuM6wwpFKqdoUfiF4Tng_Hktyc9oExc1DdFlAGm6oHWMnBCF5V6buf-I98v196_IGE61EsA6Jk10LfHp2VhHGwqtNzb0ujiXXbS5Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
با این لیست ساده، مثل یک حرفه‌ای لکه‌های لباس را از بین ببرید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/663118" target="_blank">📅 12:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663116">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔹
#چند_خبر_کوتاه
🔹
اولین موج گرمای سال در اسپانیا جان ۲۱۲ نفر را گرفت.
🔹
سازمان پخش اسرائیل: آمریکا به درخواست اسرائیل، ۲۸ هواپیمای سوخت‌رسان را از فرودگاه بن‌گوریون خارج می‌کند.
🔹
پاکستان ادعای طرح موساد برای ترور عاصم منیر را رد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/663116" target="_blank">📅 12:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663115">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyAKGRcHAs3KWqkfzQ3QurIBniR403zjZ1R0Vi_zwBzT4xSxVAVTf4Rt5rJkixDvARcNtJpA_39O5oijD_Bt7qylS_YsPyiDGK3yVupBdbGYMnN5JKRJghasDkHRNUMJNbYdIZiGd4XKfBIMYvkb5-WUfO7C4SrgJM__HyVUt5euf2_a4oMeWqSRpQhTu2XbjzSVJ_Q0-5TBxoIhXl7WDHsBYiVPj6d48DhZ996f0E4sc9CyEqgv8KMBqxOEktBg2g6QWvyOSfADn_8w-2zhYduSDiUhxLHhLHnos5UvYb3NvkeF7MglrlybGxEFtzy3MqiZq0fuUu3BA_vQ2aafsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تصویر منتسب به حرم امام حسین علیه‌السلام در ۱۱۴ سال پیش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/663115" target="_blank">📅 12:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663114">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a0f7344ff.mp4?token=OgBZzurU_nVJ8MnfgFBVoqKFXgYCCFhC22SYotgTcPgxGt9OfzutbbbY23oCzBU9Fz2sbvL799_KWwykXWZeBJCxaeqAsK4Iepj-idw14CURCeISNPQ37dWOaQBssF7jqFhqdH5UCDwfjDlS8Saesxa_8U-IT_9Fal4yPpB6uPg5xfDtNL8cNqeUbTrz8HAkPHYlzgCbsVUwz2wdtyoQMoaKrtSoqF9sWlHQO1p9SIXzW68h8-zpa9UgrV9BTNz0_CZjpEAhXE7Lc7Ia_JBcL25e1z0j3-_rixgp74Vw-WgmlhWiP4x1hftz54AVF8dXb4i2nemCTyRWu8tAENJhQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a0f7344ff.mp4?token=OgBZzurU_nVJ8MnfgFBVoqKFXgYCCFhC22SYotgTcPgxGt9OfzutbbbY23oCzBU9Fz2sbvL799_KWwykXWZeBJCxaeqAsK4Iepj-idw14CURCeISNPQ37dWOaQBssF7jqFhqdH5UCDwfjDlS8Saesxa_8U-IT_9Fal4yPpB6uPg5xfDtNL8cNqeUbTrz8HAkPHYlzgCbsVUwz2wdtyoQMoaKrtSoqF9sWlHQO1p9SIXzW68h8-zpa9UgrV9BTNz0_CZjpEAhXE7Lc7Ia_JBcL25e1z0j3-_rixgp74Vw-WgmlhWiP4x1hftz54AVF8dXb4i2nemCTyRWu8tAENJhQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
وزیر خارجه آمریکا: هیچ کشوری حق اعمال عوارض عبور بر تنگه هرمز را ندارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/663114" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663113">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25c08365c2.mp4?token=WEsMWL1WnUgruT_gbuI4e0mLHeaAHx_clGPdSMK_CqTU7UH-zNzKvVy1reAeOU6mn33eeRn4uVg7GC_PRVkWqERg-pe3VOQIn776cG95dJNdqFwm5l83JtjjMl-K5ffQjmIfw2WZzpUffliZUDAWvnBC7w72VEpXmDIE86_fzfSyZeIk1j4bYQ9Xrtz3rLF-0SwRKULO6zl1yHen-4_mGptoTquGdsyswY-4-xYgs14UplIFc0OUbPYkpI2oD0UVy6HPKtYxzkDV4kxCj8MazXqDjjqSIjuYc3ZVCAElz4DPQkVnkFJDVMHwCv7fRcOJUbaVVAUQM2dZIi-d__ibM36eIhAiZVzckgGWTBtKoAuTb87nWtaId7BFkf_RdHtw64kGYhFNnEmR3ebCrDa9vKJa69WLJuwVchL01Qj3yenZTNbdUfEtHnPpGu2oV2evYcvvDBYCwOxhDtN7jj7TYotbREtxuEMsFOW-Ab87iWGaDW8IfXP5ard2QDrnVugLGlhE-dBPEiyCKzBg9VwYv3m2dTLba9x6g3YJV9AVIP88qcWe1Sn8DApcFok01vJW5qSnsVsomZgEmtXUezm_ts5-eUCyiFwDR-XehaPU7BmcC1zaHZZbYQmxSb5r2S5XS-_RqpBgVBxO9fBPKJtw_YWeTvwenLTsOSjmMYcc6bE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25c08365c2.mp4?token=WEsMWL1WnUgruT_gbuI4e0mLHeaAHx_clGPdSMK_CqTU7UH-zNzKvVy1reAeOU6mn33eeRn4uVg7GC_PRVkWqERg-pe3VOQIn776cG95dJNdqFwm5l83JtjjMl-K5ffQjmIfw2WZzpUffliZUDAWvnBC7w72VEpXmDIE86_fzfSyZeIk1j4bYQ9Xrtz3rLF-0SwRKULO6zl1yHen-4_mGptoTquGdsyswY-4-xYgs14UplIFc0OUbPYkpI2oD0UVy6HPKtYxzkDV4kxCj8MazXqDjjqSIjuYc3ZVCAElz4DPQkVnkFJDVMHwCv7fRcOJUbaVVAUQM2dZIi-d__ibM36eIhAiZVzckgGWTBtKoAuTb87nWtaId7BFkf_RdHtw64kGYhFNnEmR3ebCrDa9vKJa69WLJuwVchL01Qj3yenZTNbdUfEtHnPpGu2oV2evYcvvDBYCwOxhDtN7jj7TYotbREtxuEMsFOW-Ab87iWGaDW8IfXP5ard2QDrnVugLGlhE-dBPEiyCKzBg9VwYv3m2dTLba9x6g3YJV9AVIP88qcWe1Sn8DApcFok01vJW5qSnsVsomZgEmtXUezm_ts5-eUCyiFwDR-XehaPU7BmcC1zaHZZbYQmxSb5r2S5XS-_RqpBgVBxO9fBPKJtw_YWeTvwenLTsOSjmMYcc6bE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه به لحظه در عاشورا چه گذشت؟!
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/663113" target="_blank">📅 12:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663112">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeGaLYbuHDuytrUzFMxuJDtKfoFlS5pDRJ3hHFqLbkMV8JZILtiv1WUuDkyDco3izq85n8g8-koiTXjP4v4wLTGK9GTqAMbXl2ZDKHH9K_6O63-kwbqs_YYlFiDK_cDScG0WcbjFFosEwnbiI5YBrw1ZE9tKAuYki8rjhnRAdSbGycPmfu7x38bDD5EIMunujSi6rSuHxqlMqM26AhheIa9urJqOeMJnsKw4cuPDHVLfY6Zkkbp-opp9QdtA5w0frnGrxHSlsivzovOJRDf0gR31D0fG0CD2ZRoZpU4ION2f6_hLF8OXnsWh1ps8Chh15Mi-CdrLy_03wWQN7ZEKtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فارین پالیسی: ایران شکستی بزرگ‌تر از ویتنام است
🔹
جنگی که به اختیار انتخاب شد به یک فاجعه راهبردی برای واشنگتن تبدیل شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/663112" target="_blank">📅 12:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663111">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igyJ3YCBSfNwF8OQhlJfFT9RTLmVwDUsuZ7ASNO3Xm8cNT9PvsTNMPKrMwIArVJ8BRWt8YJLaSkn4qQpiBRQ5JRaHsjDoMdBGIgoAdGx2BWwQwfi3zAR1e3uK1JGrcEMZGCPzjGr3iEVrRPuIClH7eQv_tvtZEH6L8BWI264OmyeS7PNMUMoz8WOGcxz8PY2i9PQ6_2T1aMWd7lyZk5HVuJH0Q0w1K_QjPhn-eYctBkagHfLAsAyObL4jB6RrzBq1pTmZPNR0_RUyuf5MfXLmjWENjqJLygRaGFrn5fwLSN98JUsvdJobYXo18Ynr-2XxfX5LQuj0yclCVhRKqOr-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
توصیه‌های بهداشتی برای توزیع غذای نذری در عاشورای حسینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/663111" target="_blank">📅 12:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663110">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4908ef9ba.mp4?token=SOkNSyrjn2pzQfXDqyddNj4_2ho2eIemgm1vAio5RuzjxtYcWSe34bVTE5o0HKYlzUbsPtMKN9IpQMd45jps4lp58PGwg2OPkcxn9fMk1IHGCP8P2tzgIMUQaD6HHnr1AV6PiG-8wSx_yq-O30ZWJm7pSIWnh-RcwgupzZeOuKBh6TYngwWvZI9RLEMV_QwoIzKHptLImmKPM2qSfiEFLG2sGeDnNkSK4Y7HOjc9J8iAsyLLJNOnl7AJKLTftnuzvjpG3EteUPMKPDjCB9EQ1r9ix9l1w4V_mhqFLx44l2uoU5h0T2xWTzxAZOpm6e3PfuaBjY74THfL5Prlm5Is84i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4908ef9ba.mp4?token=SOkNSyrjn2pzQfXDqyddNj4_2ho2eIemgm1vAio5RuzjxtYcWSe34bVTE5o0HKYlzUbsPtMKN9IpQMd45jps4lp58PGwg2OPkcxn9fMk1IHGCP8P2tzgIMUQaD6HHnr1AV6PiG-8wSx_yq-O30ZWJm7pSIWnh-RcwgupzZeOuKBh6TYngwWvZI9RLEMV_QwoIzKHptLImmKPM2qSfiEFLG2sGeDnNkSK4Y7HOjc9J8iAsyLLJNOnl7AJKLTftnuzvjpG3EteUPMKPDjCB9EQ1r9ix9l1w4V_mhqFLx44l2uoU5h0T2xWTzxAZOpm6e3PfuaBjY74THfL5Prlm5Is84i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
موکبی کوچک، بی‌سایبان؛ اما به وسعت دل‌های عاشقان اباعبدالله الحسین(ع). آبادان، زیر آفتاب سوزانِ حدود ۵۰ درجه؛ کودکی ایستاده تا عشق را معنا کند..
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/663110" target="_blank">📅 12:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663108">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b805d990c5.mp4?token=W8NYNpKJXjVbXt52BJD32zLmrCLiXwVRtnul70CrBbsaiDpqo_U0Yc2wKTSyW-PvyZ2h2K0_bU6A3L9POB_Gl_7SOH93dcDtXVVwWG286QT_jF_ALssiMSJjzRyDpl_Ej5e_OgEFwkfxqvFrx1LJsPCc10K9DYn7hgkiRASTCmNORMf6YENEMdoILlw0V9gV-7tsIpJDkbj5rYMBse8MIC4pZGh9cWEZ9NFX6SKZ-d9m-NK0Gq9ltCKdgGJvFiBOBhpguFJL2_8-IVmw-ekqhMlRR9nsxgix0wqA9yzPAQ1_ISLNuEwC0rD16T41M5lpgvR23DS6FcR4cqt7txFuaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b805d990c5.mp4?token=W8NYNpKJXjVbXt52BJD32zLmrCLiXwVRtnul70CrBbsaiDpqo_U0Yc2wKTSyW-PvyZ2h2K0_bU6A3L9POB_Gl_7SOH93dcDtXVVwWG286QT_jF_ALssiMSJjzRyDpl_Ej5e_OgEFwkfxqvFrx1LJsPCc10K9DYn7hgkiRASTCmNORMf6YENEMdoILlw0V9gV-7tsIpJDkbj5rYMBse8MIC4pZGh9cWEZ9NFX6SKZ-d9m-NK0Gq9ltCKdgGJvFiBOBhpguFJL2_8-IVmw-ekqhMlRR9nsxgix0wqA9yzPAQ1_ISLNuEwC0rD16T41M5lpgvR23DS6FcR4cqt7txFuaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ایران در جنگ پنهان است؛ هدف آمریکا فشار، بی‌ثباتی و سناریوی ترور است
نجاح محمدعلی کارشناس مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
ایران هنوز در شرایط جنگی است و توافق‌های جدید صلح واقعی نیستند؛ این روند تنها یک وقفه برای افزایش فشار است و حتی سناریوهای بسیار حساس در سطح رهبری نیز در این چارچوب قابل تصور است، در حالی که بی‌اعتمادی میان ایران و آمریکا همچنان ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/663108" target="_blank">📅 12:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663107">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔹
وزیر خارجه آمریکا: برای دستیابی به توافق با ایران، در پی برقراری گفت‌وگویی سازنده خواهیم بود
🔹
وارد مرحله‌ای جدید شده‌ایم که امیدواریم به صلح منجر شود
🔹
هر تصمیمی که اتخاذ شود، با منافع شرکای واشنگتن در منطقه در تعارض نخواهد بود./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/663107" target="_blank">📅 11:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663105">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8115e8a083.mp4?token=nCFAqPIpap922gQZ0vPXnX924J7t1n3wVt5E_fDEygBIkARV7mNrsW0YexONVM7Qer4Lt_KgWcbvS0Ae_bo2na6xZAzV5PI1oT0lyeCfM1cS-nwatfmliHo1TjmSqtQIn8o3Ufajj7yQ7F7jI51Oe4OZt-Br_oj3yFeF-mUaErQeAVdj8ZXbzZJn8xgFuk9IE_-gM6LgdTmArunip0eEnrIx6hBCCarbnTCtBWTKZJs-nqQqEQxLhNgozbvwb7rhYpSRUKkucr-Freg1Gi4tuiRTVmhBMCPUM1eIYqYu7fRm5L5-2NzwldSU5yF5KoCUTcKmZCLeXaNeyDuwDAQdew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8115e8a083.mp4?token=nCFAqPIpap922gQZ0vPXnX924J7t1n3wVt5E_fDEygBIkARV7mNrsW0YexONVM7Qer4Lt_KgWcbvS0Ae_bo2na6xZAzV5PI1oT0lyeCfM1cS-nwatfmliHo1TjmSqtQIn8o3Ufajj7yQ7F7jI51Oe4OZt-Br_oj3yFeF-mUaErQeAVdj8ZXbzZJn8xgFuk9IE_-gM6LgdTmArunip0eEnrIx6hBCCarbnTCtBWTKZJs-nqQqEQxLhNgozbvwb7rhYpSRUKkucr-Freg1Gi4tuiRTVmhBMCPUM1eIYqYu7fRm5L5-2NzwldSU5yF5KoCUTcKmZCLeXaNeyDuwDAQdew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ترامپ: ما در حال ارائه بزرگترین کاهش قیمت دارو در تاریخ با اختلاف قیمت ۴۰۰، ۵۰۰ و حتی ۶۰۰ درصدی هستیم
🔹
اگر نیم درصد کاهش قیمت را انجام می‌دادید، کسی می‌گفت شما نابغه هستید - ۴۰۰، ۵۰۰، ۶۰۰، ۷۰۰، ۸۰۰ درصد. هیچ‌کس چیزی شبیه به این ندیده است.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/663105" target="_blank">📅 11:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663104">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACcui0G3ii9ZbnY7kfAWXxFJWJ5SySMVxNXcAvwcxRAGAQy1sqo-Cpdr331zvFhaYK4PT-Gvq3X8hHQ8Sh0c112zIWsM1mGiuou1AexLS6ASko9lIYUoBDEvfxHrhRRHMCQL1I7D9jN_AD5n0BCInjlQBTVV_a30vsLPvJJDdSTBaun6VD1yPKAz9UbDEb7weS5Im2vd_40tKs60DIdB5nA0Ibumf3esr4R2pzNC8xB86nM4zJEHMMPmsCwW1sVVwlHXuYUQgFqx5iodj8wAtihKNxDiSJPP_Qxsi5QOb-136ZSsTpHdAn9DNjji1TJN0c_x8FHLhd4k6fkLKtdm7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ردپای حیات باستانی در مریخ؛ کاوشگر ناسا مولکول‌های کربن پیچیده کشف کرد
🔹
مریخ‌نورد استقامت ناسا مولکول‌های پیچیده کربنی را در دهانه جیزرو کشف کرد؛ یافته‌ای که احتمال وجود محیطی قابل‌سکونت در مریخ باستان را تقویت می‌کند، اما هنوز نشانه قطعی حیات نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/663104" target="_blank">📅 11:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663103">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf8f90b53.mp4?token=nLwpu672jDlMBmLni2xhp_7sW8cRDXsCGxeLl-IsAvviXX8xj3kqcA-4EEvxTc6vmyP2w1GyqKVLstE2_GRL4LPvp4-WNarX3WLgyUkFyDV6xyZIA84FN1mK2mnqnkh4j_sVx9EJgM8trOqjX4aoOtAwSVQ-zeTbgICMlWr6E9Wl-DsZ8p1zVqxD2hQdCdB-EK8TLbfub1ShAc5uBD75-KK_HlpyjW1vzKdpHW9PrGcpzNniEto9GVkaWal_IMEtrzPRPCIiW3h1njNckik1YYLeK8ZXSqvTayFih2dJVzDV5adnl2cmen8-X6Cew3kNVlQpDs8AZnSMMGqXzWKqsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf8f90b53.mp4?token=nLwpu672jDlMBmLni2xhp_7sW8cRDXsCGxeLl-IsAvviXX8xj3kqcA-4EEvxTc6vmyP2w1GyqKVLstE2_GRL4LPvp4-WNarX3WLgyUkFyDV6xyZIA84FN1mK2mnqnkh4j_sVx9EJgM8trOqjX4aoOtAwSVQ-zeTbgICMlWr6E9Wl-DsZ8p1zVqxD2hQdCdB-EK8TLbfub1ShAc5uBD75-KK_HlpyjW1vzKdpHW9PrGcpzNniEto9GVkaWal_IMEtrzPRPCIiW3h1njNckik1YYLeK8ZXSqvTayFih2dJVzDV5adnl2cmen8-X6Cew3kNVlQpDs8AZnSMMGqXzWKqsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اين خوراک باميه بدون گوشت و مرغ انقدر خوش طعم و جا افتاده شده كه حتى گوشت دوست‌ها هم ازش نمی‌گذرند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/663103" target="_blank">📅 11:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663101">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cac175f85.mp4?token=Cx7k-Fl4_uEvacc3H7L9WSOhDoG7YzxLyAQsmp2D3fSj-7FbvqqhdBH3PgmHiOdverUltNrr58db_GeMeypAuEPLNvPc5MYRYphMhy08YNGXVYRcwvuOa3LZI089vwZ4m4nYfFDHkCH5vCRW-InRJR6qH8yVnH7vDjfD-j5k5drhaxyBM_7bS-Colv7osOym9V_jiVr8zTCyZlc5D8L55edn37fUVzVtWheVNP6u7H3iXZqggHHBim4Sq5HdZf9WeDXGIiXz8fSn3Zx61rTky-LTOCW7FIexUHkptKvlGR_SnaSOuxtvYjIU1JnVsSYcHLkGgrZmm1Wiy7ajs8TA8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cac175f85.mp4?token=Cx7k-Fl4_uEvacc3H7L9WSOhDoG7YzxLyAQsmp2D3fSj-7FbvqqhdBH3PgmHiOdverUltNrr58db_GeMeypAuEPLNvPc5MYRYphMhy08YNGXVYRcwvuOa3LZI089vwZ4m4nYfFDHkCH5vCRW-InRJR6qH8yVnH7vDjfD-j5k5drhaxyBM_7bS-Colv7osOym9V_jiVr8zTCyZlc5D8L55edn37fUVzVtWheVNP6u7H3iXZqggHHBim4Sq5HdZf9WeDXGIiXz8fSn3Zx61rTky-LTOCW7FIexUHkptKvlGR_SnaSOuxtvYjIU1JnVsSYcHLkGgrZmm1Wiy7ajs8TA8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
عزاداری محرم امسال در کشمیر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/663101" target="_blank">📅 11:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663100">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-B4ZKK-FQkQAWCDppuirZa-iyscJYK7kmVNpuJ-mQlgsQGK6i1TH9wdM_8zBSWn_YhBOfJPk34E0wt0RztPj0k8lKe48ft4MPjrjIQyQ6uVZrz-mOPyeIUkkz1Pu8esGjIPEpDST_c6LlJ4y79wPBYn3MTwz37bY51pBZVpoQ0IUw20fxODmqtrJ0apUxMzboLQl-fUP1Yr_WFoUNKLbPdAL0JdaM7f0r-f3uC2d-aVn1sutacMYqQkIkwciTYfS0g73-mQNhm-9tsEfUQ1nqfmlvp6_tZ9hEmLSpeo1kcSt8SspiTx6L3thWAT1QQp9gMQpzP-yBzeinzdVUbTMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
راهنمای ترکیب درست رنگ‌ها برای استایل آقایان شیک‌پوش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/663100" target="_blank">📅 11:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663098">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/10071cd098.mp4?token=Z4TtuhQ-iPbHxjy0ABZy6VWRfmiWxMinAPhlVOAaM39BmqfYzxXXepJ-UReYeB5-3v1OT14k-0hxDCLe7vP8l2uj_zoOK19xzPK3HQdz6mhXlhxQZWbWk85cpR2eXVfzURcc5H90Myz0TwM90FMKuKrY8yFKs9GFDMI6-CnPjIIUlsXQ_VIFHd5aMmMO4PqS6JStjDv6ZtuNWpuAQeeVyxs3yDcyekPWIkPlgztS3hn9fpr_sFLQRQXq-CpEljNlWna_6RL4WE_fX6aUY-BqkwrqnbeyNDXMpQUli9Qop1Y-N35zDanJCG5RjEW1KS8rMJa_8LvoczSDZ1GAugoHcw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/10071cd098.mp4?token=Z4TtuhQ-iPbHxjy0ABZy6VWRfmiWxMinAPhlVOAaM39BmqfYzxXXepJ-UReYeB5-3v1OT14k-0hxDCLe7vP8l2uj_zoOK19xzPK3HQdz6mhXlhxQZWbWk85cpR2eXVfzURcc5H90Myz0TwM90FMKuKrY8yFKs9GFDMI6-CnPjIIUlsXQ_VIFHd5aMmMO4PqS6JStjDv6ZtuNWpuAQeeVyxs3yDcyekPWIkPlgztS3hn9fpr_sFLQRQXq-CpEljNlWna_6RL4WE_fX6aUY-BqkwrqnbeyNDXMpQUli9Qop1Y-N35zDanJCG5RjEW1KS8rMJa_8LvoczSDZ1GAugoHcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
توافق جدید با ایران صلح نیست، یک آتش‌بس موقت برای فشار بیشتر است
نجاح محمدعلی کارشناس مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
یک تحلیلگر سوئیسی می‌گوید توافق جدید با ایران بیشتر یک وقفه موقت برای مدیریت تنش‌هاست تا صلح پایدار؛ به‌گفته او، نبود اعتماد و تضمین امنیتی می‌تواند دوباره مسیر را به سمت فشار، تحریم و تشدید درگیری‌ها برگرداند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/663098" target="_blank">📅 11:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663097">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOFlBXufCjKuLVmJU38Jw2f1VID-Yh9Qt5vuecUqOXhMZX9jAXTBpLHOWbY8X9iELQYIuG_1CAUM76LyF0Jov5vReXxplkoPoUeWkOgBLhoJ4fosUxRWExl6Ehlt1GfNXEftdtUnm8E40wv2hmIEsaLgXXIu-kk4b1dtNBbJYAwfyfTP0bkpmJY4KpDkYF9KM9Rxc_088B6eeF8PjjKh2haa99kGXZD8rlgO43kxqRjuFM7iuHUL4DpyQhDQML9m75xxD0KW9I7GJgaCcd5Ba-Jv7ZomVQJ4Pn1GBsHbq8Y3h1FZvJFqncX5Upuz8OV_0y6YNOFLgmcPIWSX05r4TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
لیست ثروتمندترین افراد جهان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/663097" target="_blank">📅 10:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663095">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904754cbbf.mp4?token=TzwFlBPH0vPQIKkTKpxq8zkfcbWSL3mmzQLV0LwOQs3hUrU0hxWyOYyj6_cBingPFT9IolQZmUSJCHJtYWqhhqTYfa7e3GmJTAjALQIw7aeNB90PtC0S3F9JsFaJ_XfjDDzH-2Mfi2cco4Q_TUdLTJf0EXR0dQ29y1djFqhvrzG5iKOPpKm3ZsNiedYuL_njGS8mLsnbHcdHHJP56aV2QDrmgvZ9G7SyfgnxtNSliNObn7nqnXnPgmqommclG75PYq8sIyUP5TjmMJH2waZyQU79E2F4BfR1etOO-YeexK7dRd3q7KSRI5NZ4SzYAd9FEp-5rmN7mLs5pjdvAPq3ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904754cbbf.mp4?token=TzwFlBPH0vPQIKkTKpxq8zkfcbWSL3mmzQLV0LwOQs3hUrU0hxWyOYyj6_cBingPFT9IolQZmUSJCHJtYWqhhqTYfa7e3GmJTAjALQIw7aeNB90PtC0S3F9JsFaJ_XfjDDzH-2Mfi2cco4Q_TUdLTJf0EXR0dQ29y1djFqhvrzG5iKOPpKm3ZsNiedYuL_njGS8mLsnbHcdHHJP56aV2QDrmgvZ9G7SyfgnxtNSliNObn7nqnXnPgmqommclG75PYq8sIyUP5TjmMJH2waZyQU79E2F4BfR1etOO-YeexK7dRd3q7KSRI5NZ4SzYAd9FEp-5rmN7mLs5pjdvAPq3ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
یک ونزوئلایی هم‌زمان با وقوع زلزله از لحظه دویدن در راه‌پله ساختمان فیلم گرفته و شدت آسیب وارد شده به سازه در این ویدیو بسیار جدی و ترسناک دیده میشه
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/663095" target="_blank">📅 10:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663093">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
| فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/663093" target="_blank">📅 10:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663092">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/004eddcfe4.mp4?token=O50P92HwlKv_s4NpC83NjIfT70wZiVnXOv1tMSVjrDp_DX7oji6ICTWP4A36AK6nHPICgvhDsO7K2xy3vYrFK2A_YPxwp7AUqB1hKaqcH1ztAes6kurrrypDKUjUgkHm6k9VxJITq_fcmhmABqpb-74NsFPnDlk-i5o6YiLibDqPpcJe-I8ECtSIijawc5NAb8bstNP8llE-HlO0na2EQeXPexz4GjW5HEKlOmsXq3wsZSbuKTf7ObsQIjC5kcXdJPJVeoENftYp5f0IWa1cRV5EdEgmw8Qvvx6ByebISpvG5fgnIDYIaKQrkyg-6-FpNpBYYnMErNU3RE7Zucc7bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004eddcfe4.mp4?token=O50P92HwlKv_s4NpC83NjIfT70wZiVnXOv1tMSVjrDp_DX7oji6ICTWP4A36AK6nHPICgvhDsO7K2xy3vYrFK2A_YPxwp7AUqB1hKaqcH1ztAes6kurrrypDKUjUgkHm6k9VxJITq_fcmhmABqpb-74NsFPnDlk-i5o6YiLibDqPpcJe-I8ECtSIijawc5NAb8bstNP8llE-HlO0na2EQeXPexz4GjW5HEKlOmsXq3wsZSbuKTf7ObsQIjC5kcXdJPJVeoENftYp5f0IWa1cRV5EdEgmw8Qvvx6ByebISpvG5fgnIDYIaKQrkyg-6-FpNpBYYnMErNU3RE7Zucc7bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
مکتب عاشورا؛ فراتر از دین و مرزها
حتی اگه مسیحی هم باشی، بازم به امام حسین(ع) ارادت داری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/663092" target="_blank">📅 10:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663091">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f444c745c7.mp4?token=Pmz6MLlviHLAIhycDPZg2AUyyc19MwLkLZC-SXF2f7VUMwhty3ni45kV_Wy08ErSrlULxoPjKIlj4g2A3yFfzFC_Apb7o9QfR1eWYsJ6g2sYqSvGshWKdvUrVx-5G698Uo-Gg3__9mB0sU8lsnYQMyoKUzZ548Sx6WFGdFgf8Bzpu-fvOD6s7IvakWSuGGhC3S3vDl70S0ppI2VXhMN6gDU6L_QuKfGd8KMzj-XHXft9sFAfaEa1B2g5d4I0OgsPjgjB25stQ6KjLAv2TgyENRmKXCiQMQwM2ZV8N8qkp_Gf_NssrMOlFydQjwFbFZoLEI-T7qTxJtzHXlIbahhHOGKMnwGkyab6mHGRfRt4FiQuAuY-cu6iCCBDesi-S4MoT2ulc6gl1JqHvimOaTfOmFiJAX6F8xEr26xETJH9V_ym0FZpZK_m4BiL4HMfXgw1FjmfcgFxjB7yT9nZRWCgf-Lw6z7GQkLWfmictTeiDof9Dkws4R-HoGNqYzybPEEVTSiRFVPDYBRQR3Hpy6Ye0OcVBnxmGsan7vCAnGa6bLGKpeNDhYRcjkstwV5wwCSY-5alurpzMi1bGpwhQ0Pd7idrB4QWvlZUF5xPMQ4bvtotLibwpf2t4bR4YZSB_VAKlrvgNEOuQIUIyP7MeeTMM3z3BXAAkdmdl4i2-5Lco2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f444c745c7.mp4?token=Pmz6MLlviHLAIhycDPZg2AUyyc19MwLkLZC-SXF2f7VUMwhty3ni45kV_Wy08ErSrlULxoPjKIlj4g2A3yFfzFC_Apb7o9QfR1eWYsJ6g2sYqSvGshWKdvUrVx-5G698Uo-Gg3__9mB0sU8lsnYQMyoKUzZ548Sx6WFGdFgf8Bzpu-fvOD6s7IvakWSuGGhC3S3vDl70S0ppI2VXhMN6gDU6L_QuKfGd8KMzj-XHXft9sFAfaEa1B2g5d4I0OgsPjgjB25stQ6KjLAv2TgyENRmKXCiQMQwM2ZV8N8qkp_Gf_NssrMOlFydQjwFbFZoLEI-T7qTxJtzHXlIbahhHOGKMnwGkyab6mHGRfRt4FiQuAuY-cu6iCCBDesi-S4MoT2ulc6gl1JqHvimOaTfOmFiJAX6F8xEr26xETJH9V_ym0FZpZK_m4BiL4HMfXgw1FjmfcgFxjB7yT9nZRWCgf-Lw6z7GQkLWfmictTeiDof9Dkws4R-HoGNqYzybPEEVTSiRFVPDYBRQR3Hpy6Ye0OcVBnxmGsan7vCAnGa6bLGKpeNDhYRcjkstwV5wwCSY-5alurpzMi1bGpwhQ0Pd7idrB4QWvlZUF5xPMQ4bvtotLibwpf2t4bR4YZSB_VAKlrvgNEOuQIUIyP7MeeTMM3z3BXAAkdmdl4i2-5Lco2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
یک ونزوئلایی هم‌زمان با وقوع زلزله از لحظه دویدن در راه‌پله ساختمان فیلم گرفته و شدت آسیب وارد شده به سازه در این ویدیو بسیار جدی و ترسناک دیده میشه
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/663091" target="_blank">📅 10:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663090">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e27b871710.mp4?token=N_wn9DqHpCgRRnPnOCPCvOiUoHmF1EBBWrBI9PCfaM5UDFn8H5sodQ5z01ZqbZPjkEMnyVhExBKXhciRH41pFwDECC2_K2ZuWAkOIKV7hUM8ZGIizQHsOtFKAVxd4SSxjqjsbkAf2JXK4OddWjWQLC_1ngshSsrznYTjI6TzMKWdmLfI8PUBUiPI3djxHquJWOIUZY4ebhyw4rZKxwu1jDCi_Hl3swLlnxnGchjEz2yxZvnLxDEhkOYwbejcxejt19gcORRxVe6QKz46BUbsba9aYbu0x2WNXFHRfdFB9qCWoRyCxQKytwCN6DV-Mm_cOxier2KTRwFYsl8zONXalw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e27b871710.mp4?token=N_wn9DqHpCgRRnPnOCPCvOiUoHmF1EBBWrBI9PCfaM5UDFn8H5sodQ5z01ZqbZPjkEMnyVhExBKXhciRH41pFwDECC2_K2ZuWAkOIKV7hUM8ZGIizQHsOtFKAVxd4SSxjqjsbkAf2JXK4OddWjWQLC_1ngshSsrznYTjI6TzMKWdmLfI8PUBUiPI3djxHquJWOIUZY4ebhyw4rZKxwu1jDCi_Hl3swLlnxnGchjEz2yxZvnLxDEhkOYwbejcxejt19gcORRxVe6QKz46BUbsba9aYbu0x2WNXFHRfdFB9qCWoRyCxQKytwCN6DV-Mm_cOxier2KTRwFYsl8zONXalw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تحلیلگر عراقی: ایران نیازمند «خانه‌تکانی» در روابط منطقه‌ای و بازشناسی متحدان است
نجاح محمدعلی کارشناس مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
ایران باید با انجام یک «خانه‌تکانی واقعی»، دوستان واقعی خود را از نیروهایی که می‌توانند به تهدیدی علیه ایران تبدیل شوند، بازشناسی کند.
🔹
ادامه نگاه سنتی به برخی جریان‌ها دیگر کافی نیست و ایران باید با رویکردی انتقادی و همه‌جانبه، به‌ویژه در قبال جریان‌های شیعی و معادلات نوین، در روابط خود بازنگری کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/663090" target="_blank">📅 10:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663089">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b651e0520.mp4?token=WhlHBuQjWxjSXkzq03cDH-tFzINCTmetD_EqUGN-EY5wmGQwbe8lwwhmWdLYzhvf1COo_QM27XzF5CfxO-F5BjgqxXPv-8Q2aMTvPDWNqyYT-U31XoBYsW6MUP3s86fSsluV1kizt1ITFpksqXxjmteiOz4EQpT2L0LRuR5DVv9VIvn1s0CRD6dj8c9c5cecxgnru1jzNm4FNRaCrVQkB-2B6RQHEXm4CpnhNbok48Hzm0Y97ixrYZEiIiX6CFXBZIIoTA8TJ5t1dtwbrVhBy9Gd71gfHRx_SBgpVkWRQGG82DaGb4lC8uHWmP8xuwaHmdq5xUj5WR4BjhXJZAeRSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b651e0520.mp4?token=WhlHBuQjWxjSXkzq03cDH-tFzINCTmetD_EqUGN-EY5wmGQwbe8lwwhmWdLYzhvf1COo_QM27XzF5CfxO-F5BjgqxXPv-8Q2aMTvPDWNqyYT-U31XoBYsW6MUP3s86fSsluV1kizt1ITFpksqXxjmteiOz4EQpT2L0LRuR5DVv9VIvn1s0CRD6dj8c9c5cecxgnru1jzNm4FNRaCrVQkB-2B6RQHEXm4CpnhNbok48Hzm0Y97ixrYZEiIiX6CFXBZIIoTA8TJ5t1dtwbrVhBy9Gd71gfHRx_SBgpVkWRQGG82DaGb4lC8uHWmP8xuwaHmdq5xUj5WR4BjhXJZAeRSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
موکبی ساده که دل‌ها را برد
🥹
🔹
دو کودک با برپایی یک موکب ساده نشان دادند گاهی سادگی و اخلاص، از مراسم‌های پرزرق‌وبرق تأثیرگذارتر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/663089" target="_blank">📅 10:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663088">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8oUQlYVrt77cSfN9RugZGDFBXca1USio0n9BPTmAIBHLLzT8uYVIalY2tFF0GQhEGvZyWCdJgmwbtrv-todF3_NJCe6LXmP54fjaZ4_u2YaPy85NUFuG2ensi9diqq6SF1RoSA1JjV-IbjZWHKeNfyQy2g6dvi-aGEzQOSn-a1lSdw4iWNLP6prvCGbDZme1vKIWBtO55aXDoT1g4IVzLrTR8gfvv_QZZ4vcs9906VG3s9idO83M7T7WFisARfHIHTVALYPH9qZvnWELaZ_rSl81guZXMLapkVwAH1c64ok-1kC1z8_xNVGFHrmbSQVC7xxkR9p4tiT_ZhAfp4n2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تاسوعا؛ روز انتخابِ ایستادگی
🔹
روز نهم محرم، تاسوعا، روزی است که فشارها به نقطه نهایی رسید؛ فرمان جنگ صادر شد، امان‌نامه پیشنهاد شد، و یاران امام حسین(ع) میان تسلیم و وفاداری، راه ایستادگی را برگزیدند. #به_وقت_حسین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/663088" target="_blank">📅 10:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663087">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWJ7XfFgKHQcBDTkLQZENuxZkbxvPsW2hqRSzgBp55idKBmDnO0xPdCnebdG5KnDPR6vQC0A_R3ipggIf0Q3KGrpjMu8Ow3bwNsmPwh7fKZ6fe8HyQi6lrxjGiEntTtCRB3fDo6sSDFcGBmRJ2RakdT8RCrhSsBRLyVmYGOkfPbvne0Dr6xIqNrcqAZpmCcVOP6q6uqx4J4ivVbfKevcMy6cowGROi2b0RR-Qt7LykIdRu0IXcJqvvo8QD1YnbkA3UZd2OrmVr1K4Xgh5pxSUQqVMBM25TRomu4kgFlAI3vxw5y478xRaReeubd2h4p2v9VQ-TAXanxTyFJCSb71yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
باز هم برزیل-اسکاتلند و باز هم زلزله‌ای تلخ
🔹
بار دیگر هم‌زمان با دیدار برزیل و اسکاتلند در جام جهانی، وقوع یک زلزله شدید در نقطه‌ای از جهان توجه‌ها را جلب کرد؛ موضوعی که برخی آن را تکرار یک «هم‌زمانی عجیب» با زلزله رودبار در سال ۱۹۹۰ می‌دانند
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/663087" target="_blank">📅 09:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663085">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HlAbm1WMRiCaMe_Cs0lxTFoPGuAe4JpTtnanInVdLpfgVvH6PQvIsiSX5ws08evJllIkuGanZZH5w0OirbRK0YQ3zm3cKYmJ31dkaMx3zOaiZYZNVQhSuOLDbT_qs-irjduI_2kTj9nlf7M7DmS8MKEbsjVRQFJuAJ-15se-6pV48noRWLiDZPT7tKpe_Unh0L8_eJ1rZze0vqbB7_dJKAbNPTq5qBQ9VdnpnaKW1908_qx-SODvlKFvwFMKjHCOFjZ-R9rvL5UmzX3ZkfrV2qEuYFFlKMpKqA8rJ6D8W66XyACt-3Id7uZsrGbAj3DcvbDkgq802ShM4es8rnCVyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ruSV4pdTKgxWbisnsK26BvmWvxdIm7IaMdxxW6L_BQfXqXBCStiI1VyyHD5wFmL7Uhcf-Ek45pzQYZIO1tKewzgc0hZJH22z4QUgnaSMTuNm30_r5b1oGTJftAu-MEK7qdOk1DaInrjh9qI5abU8IoPCPMEV816e4c-8W-aHfjSwBxjJW9A3QUSlaI1JzVmgPfIwDAt1sIbqfUfavn3L3f4s_-oHCQYh5J4Ho3qi0t0KLtq0itR63sXXtX6yxwks-A54NcqpLqOWP4c3MbYZkGSuqAN58ZAmR0nxOVXEO4G2pGjHeKEhPniPeV6Y5CD-dltEBcHQSj6OMGhy7zBaag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
تیم های راه یافته به دور بعد و نمودار حذفی جام جهانی تا پایان روز سیزدهم مسابقات
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/663085" target="_blank">📅 09:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663084">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔹
کاسبی جدید برخی جایگاه‌های متخلف سوخت به بهانه محدودیت کارت
شیرینی بده، بنزین بزن!
🔹
محدود شدن کارت‌های سوخت آزاد در برخی جایگاه‌ها باعث صف و نارضایتی رانندگان شده و طبق گزارش‌ها، در بعضی موارد متصدیان با دریافت مبلغی تحت عنوان «شیرینی» کارت جایگاه را در اختیار افراد قرار می‌دهند که تخلف محسوب می‌شود و موجب سوءاستفاده از شرایط و افزایش مشکلات سوخت‌گیری شده است./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/663084" target="_blank">📅 09:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663080">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsn6QkrX_lB_FvjGx-yj8D4yX9T3XLqvAdIwdKLmsccuK45WpJqkIhj1m7dyVW5bqQY93jCFDdzL6Q5pxG-tN21cHavZ4iE0WaMkjXD5WUTY5isvtoTqNR_2JHLJsobUKJ1Y6nMXEMfO4m00sM2GC9copS31kUYQW6li7bYpZRqV64_oS__mZAVtRktcOiIVFiZ9V4iRGIZT7HS04OpV3QwAXNpjxXcCjsm8_FWTHLnLMVAwUDJ0I9B8TaaO8ZVMsIoF8cPXCS6Bqw0z89ffGIrCBXOzwUhsgYNs8P2qRwy1fwJS9FpSXhzJnHyi2eUIRwy-1ca8RIbNMGEeyvbRFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RP6eT5fEn48qGfdUm6dBKulQr5pTGI85CvkaskEAlZXdtTF5IFOe5e14x3wn-jqSW5LmoSHGQ9HwMkjFPf-1AXNo8s01cY8jwMNtG9tA3BjppWvFO6NshWJxcElYQ_EEpkE8OBpnjg9x5m3RW5ATPOTcN21LWU2ICs4qf07nhZ3nquuYXTBwUElCcEY8SrquDOFlBJs0sldSGwBu2U7GoSyqqKwPAdEPOjpZCvbcGx2-5E5-0y5e1FgWlAkLRKdQgzZs5gyuvIO5YcDQlyM7TX_sv4fYLf-VSvQWgWOZ3CqvCPCOirOZ7uncf1rVPbJ8ujDbxpL7mwb6XEnjLgZSjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njzGSOKDvKKbEOdEwjZuOOEhLNadBkzyanDTplL7ebijLjTBS30hMEhigkru3A_eX-bnyqs2IVTCPA1LdHFmKJo81pX2m4HX7ARAOS4rNCOo43GKl31kVLkENPeqNl4rhoE1gnYsWVNvkLz-pVX6Qdbnr6D85erKYobmcbN_U1lkuSycENVsaO89II8q0F5Jp_xC3uwZT1dY9NniuqijUB_fAemqEF9fKI9Bn4XA2TIjwgj_QMcUQ4A3v1nYTa21nq2SLWIEcifebfKTTbGpoF1R-8uZ8NC_cTJetUPaiBiysZWa43Gp8Obhwt5zuDt2K-JeAMxBJ5sN04x71FypEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDHuQUFIsF1XavXL6n9y88GMp0N1wB3L271U3iA1gQEH562lkvoE1FjUosXuXgzq4Kx8s5CSH4RbpfFCZ53R9QJVz0UgGqQnEQnVjYDuDBAiL3o32UjCcyw08FAabwnJqzPcskTCgUkKIS78wkyZ4ahraWRDKhbtKscomMH3ygGNmJLbdw6fbiN715vhc7UR-_ZHE4EjYySd3eKRA433Zb6vexQIHShQfWKSPMhBkcAHOcq96ExXoLt-bEG_9jCC21m1f_8e_yCEdM5-RaQf7ntvYgaIZMyPN0oALynmcgJz72S-a16wIagLvfUjOFWkbAPPYOoPWnXTn-Rxv2fGhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
ادعای فعالیت یک گروه ناشناس برای «آزادسازی حیوانات» از مراکز آزمایشگاهی
🔹
گزارش‌هایی از شکل‌گیری یک گروه ناشناس با نام «جبهه آزادی حیوانات» منتشر شده که ادعا می‌شود حیوانات را از آزمایشگاه‌ها و مزارع صنعتی نجات می‌دهد. با این حال، هویت اعضا و صحت کامل این ادعاها مشخص نیست و جزئیات فعالیت آن همچنان مبهم و بحث‌برانگیز است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/663080" target="_blank">📅 09:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663079">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOBhc9l-esOgEPL8iPIR0vOT_6-26s8LMRoYX-0dVB9b6DDonO5jLhrqggQfsS88KhHT-n-EJTYkXczXUbkptABLDvr9SI4p1rRnHN4LRPp2_nQM2P5NSnHMsq8v0sVkdea2s9P-2ta54c7sJBV84ahW908jC0KcuYyvYOwVxEJl9Prg3p2kCYy51lSboYngYcx7OTskr-LBNWCUr0eY0QzawIyNpT04DgNIn0i_A7Asfn8lfAjdMvS4h5zQsQdIv48uxVdWawIMzPzAEsxk4ziowzS_IMlB6S711iwvvXq_DaD8j7wmuVzzlOINqP9fjyjJsZ9_wN5CcYp4R3BB_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ویرانی آخرالزمانی ونزوئلا پس از دو زمین‌لرزه
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/663079" target="_blank">📅 09:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663078">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_u-gy0mvBfTs5S72pK1DTCrd0P7Qc1N68Smuf9N29M1vkcp72O0JU-XctvkFKwS4Afz3LFgh48OduzlTua59XFe1jaN_s695kC5CVGgQ60fuGkg1uOJyeyF2boaOvLjISoc8vhlRpQ_THv3hNjfMU78c_xoD_i9LtmuQHvlxupYfTKUktLknkhGu1z65ZwWiT0sqKyY3do-GzPjYKheRIiCziP8OB15ZJsddo_j6pez9Byo-Q8BblARlfgdX_DumHXaCHp73zJ3XEjDhmiXd__q2B0jSLalE1X979AUteffaDMI2RzY1zVFeQD8iyxDyrMuAenMxZr4fDshqj-cXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت جام جهانی فوتبال ۲۰۲۶
🔹
همراهان گرامی خبرفوری؛ برای شرکت  در این پویش کافی‌ست یک پیام صوتی حداکثر ۱۵ ثانیه‌ای ارسال کرده و با لهجه شهر خودتان، پیام انگیزشی و انرژی‌بخش خود را به تیم ملی فوتبال ایران برسانید.
🔹
در ابتدای ویس، نام و شهر خود را بگویید و با صدای واضح و رسا، حمایت خود را از ملی‌پوشان کشورمان نشان دهید.
🔸
صدای شما می‌تواند انگیزه‌بخش تیم ملی در مسیر جام جهانی باشد
👇
#برای_ایران
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/663078" target="_blank">📅 09:47 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
