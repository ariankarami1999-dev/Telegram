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
<img src="https://cdn4.telesco.pe/file/PDgrB4vGEfeYGq1eUfOS8P1nw22r5D6RAEDR2s8FAEq9ltpQtIvnFbdb4gZ3wDVVpmMn8WUjo503Z9TxtGJPd8YIJmZbN6X66I9LydBfwHSupY1KPXsx6ElPCyvndMtseNlgAga4hxgVjxMOfY3XDrR-X4mxM0PHbTvvb-0kjq_mKalwX9OTIcOo3TSmN55d4mqdtNyEbo0ZCEVbRb_e2nchR2ojI6_Kz1bn3SlXSdnENHL7j3k8F1r40Vqu6wYKbF8b0H9CTvw_pkdNwsBSRyKj0A9p0XCiv4pFq1hgb1P1lZ2QT8f0ZOV2qI1FhVE-8pHZaL0gRsq-25VBscbgbQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.38M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 19:43:38</div>
<hr>

<div class="tg-post" id="msg-671453">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
رسانه‌های عراقی: صدای انفجار در منطقه کویا در اربیل عراق به‌گوش می‌رسد/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/671453" target="_blank">📅 19:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671452">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
منابع عربی: دقایقی پیش ۲ انفجار، پایگاه آمریکا در کویت را به لرزه درآورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/akhbarefori/671452" target="_blank">📅 19:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671451">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxBP8byHvY7gumD2CgdnFqwbWNged4j0jRfvPG8qD82oh_Sjsp7MtC6V2nhAbH88HeHZhlx54qLrbVIAG_2mYNVMI-AcZX4zdRinNb2drYWycn91kX-jGNci5SUVfraEHRBwaOPAZfMcKfcSsGndCZG1FMSI2vC7lu3qV8IWj9rRw40sDsvPeqtPzn-z88qWk6Fe-jnl5D_c7VR8irreEDB89azmB0dLYkOtBm_LxSU_gFyS388vig371PXFjAn9tqw6asWw7baZaMVrOc4RFEO4lE7Ga6bjgzxb39s9iNsCIXlIozaRLZ2haB7ti7fsO_34STnwQm3Ba8fWiIkopQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر عضوی از ملت؛ یک پرونده انتقام!
🔹
این اطمینان را به همگان میدهم که ما از انتقام خون شهدای شما صرف‌نظر نخواهیم کرد.
🔹
انتقامی که در نظر داریم، فقط مربوط به شهادت رهبر عظیم‌الشّأن انقلاب نیست؛ بلکه هر عضوی از ملّت که توسّط دشمن شهید میشود، خود موضوع مستقلّی برای پرونده‌ی انتقام است... و بخصوص نسبت به خون اطفال و کودکانمان حسّاسیّت‌ بیشتری خواهیم داشت.
رهبر انقلاب
۲۱ اسفند ۱۴۰۴
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/akhbarefori/671451" target="_blank">📅 19:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671450">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای انفجار در کویت گزارش می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/akhbarefori/671450" target="_blank">📅 19:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671449">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVN5Lah88ZxRQ0Ujv0kzf09wjxF1S1XYbAt5dguZ_JjQRBVjaSqxsnRZKbvx9z5X3-6jrV8VdCSqPdiYvtRPCrgl7aD-ZuDMDDkW2RfY0Ox6_prtjDSdlD5RBqPLNnC7e9wYstGiDZhmZxPuYGAVH1edOIjZgqfTqbRTnBuMULjDUHyGFQmmrPh-OKgAxWdm_OiO9l2ccAOtc8Zccb66SgDdDD_wsBF_pEK2JvAikJ24PDAWt09Rh4vrYT1rCMQIjhWlm6rI84PJTMc-UatFnC_fnRcTvU69Lh_2G0Wslqotiq-5w7VfAV3xFc1WFR29bYDnZpdPIm9AUcXT00yU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسامی شهدای حمله شب گذشته آمریکا به پادگان ارتش در شهرستان بمپور
🔹
روابط عمومی ارتش اسامی شهدا در حمله شب گذشته آمریکا به پادگان ارتش در شهرستان بمپور را به شرح زیر اعلام کرد: ۱_رضا شفیعی ۲_فرهادعلوی ۳_ابوالفضل ملایی ۴_حسین جعفری ۵_علیرضا قاسمی ۶_حسام‌الدین…</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/akhbarefori/671449" target="_blank">📅 19:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671448">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای انفجار در کویت گزارش می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/671448" target="_blank">📅 19:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671447">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
آخرین اخبار و حواشی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/671447" target="_blank">📅 19:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671446">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxj3rNycE49l0K7zO-AwFuIpJw7bw3VD71lBNn2ziGXUBJ4_reiByICVff03UudT5YRtwYJfGsegvc4XYIjh-iirCMxzO6JDQJ9xgwolmQb3Zz9m3HfXKCCoU6U3lqULm5B0JvyFUkgYW0a_6fpfST4zE3Vn8OlSO9x1HU6Ec6bKFzmezlSzv8hPL75dfBWur3HER7PUbsf4_cCPUmhhv_oSKpKzof8_sbE6J33CZU9LMa4XaaPub4vruW9iRcE-nslg25rBZpVz7FtkE_3DM0-eNur312xfX6PTJeSLhZh_z4C6SfakZ7Gapn2WvjsGCDSQxfUiJbtC66RKsDV72A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت خارجه اقدامات رژیم صهیونسیتی را در فلسطین اشغالی محکوم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/671446" target="_blank">📅 19:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671445">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
لیگ ملت‌های والیبال | پایان ست اول  ایران ۰ - ۱ اوکراین
🇮🇷
۲۲|
🇺🇦
۲۵ |  #ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/671445" target="_blank">📅 19:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671444">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b474fc302.mp4?token=Gyk9ayJ6WrCxZutoTA6e_oN7Xsd9SKLaDV2qD-cwJsxCZPb8Ad-89IrpMfzcQCqt8h82h3hr38StTPGfhuyYJAR9LyH32NHVV7EMJ56H6V7cuDLyTT0o5plVsx-uRRc29GwY8SVsiCDHSu4qbRgagtkDaTr2T3_Mrz3ebwnyZah2PLeJpSmK5CtEXTd2ReeKFxqq1MQ0-rrYV3PwNliDCDm-NETArWhN1jfu5pyE2bQmSycipgdW225DFa__sQL4-r7rFFTTQarbxt_3T_BxFLxZTk-YdZiBXSmFckWvugkyRgStsU0zQbvpI6CCKIwO-y42IiWyFsAlL6btg3Su8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b474fc302.mp4?token=Gyk9ayJ6WrCxZutoTA6e_oN7Xsd9SKLaDV2qD-cwJsxCZPb8Ad-89IrpMfzcQCqt8h82h3hr38StTPGfhuyYJAR9LyH32NHVV7EMJ56H6V7cuDLyTT0o5plVsx-uRRc29GwY8SVsiCDHSu4qbRgagtkDaTr2T3_Mrz3ebwnyZah2PLeJpSmK5CtEXTd2ReeKFxqq1MQ0-rrYV3PwNliDCDm-NETArWhN1jfu5pyE2bQmSycipgdW225DFa__sQL4-r7rFFTTQarbxt_3T_BxFLxZTk-YdZiBXSmFckWvugkyRgStsU0zQbvpI6CCKIwO-y42IiWyFsAlL6btg3Su8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرویس عجیب والیبالیست جوان تیم ملی در دیدار با اوکراین
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/671444" target="_blank">📅 19:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671443">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IO7d-CX2PV341PU77rUw3lUpPu2bugXUb7cs0S7Ewg6wmeugC6MKumTbJ_gPJwbl1YkQTZ0j31tlXSepgiDSyQgbuf5RWNBHGgw6YuK8Ec4nA8KiB6yMZb3cFwYpffvY-cesz7kc3Sk304xjV4lGn2PZ5j2dDfx-JR8ga8RgQ2RyPzMhxDbGulF4poY94O72eAlBe-Mtscm0Y7DMqWPeP0nqGlWSlvo9EjBi1HkWc3JJfkd3L9uKBXMUZRtXpa2wUT7U5jVV5P_azWsS9OLByyPuWJtSzOxfx1QdI7rokeOxenuert7VyJyXnpbvMLx9GFK5FZiebQ3MK73hb95_0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/671443" target="_blank">📅 19:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671442">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
تصاویر دیگری از لحظه حمله وحشیانه مزدوران سعودی به فرودگاه بین‌المللی صنعا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/671442" target="_blank">📅 18:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671441">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
آمریکا با ادعای اشاعه هسته‌ای و تروریسم، تحریم‌های جدیدی علیه ایران و روسیه اعمال کرد
🔹
وزارت خزانه‌داری آمریکا در دور تازه‌ای از اقدامات محدودکننده، شماری از اشخاص و نهادها در ایران و روسیه را به بهانه مقابله با تروریسم و فعالیت‌های هسته‌ای هدف تحریم قرار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/671441" target="_blank">📅 18:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671440">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
اصابت پرتابه به جزیره هنگام؛ استانداری هرمزگان در حال ارزیابی است
🔹
دقایقی پیش نقطه‌ای در جزیره هنگام مورد اصابت پرتابه‌ای منتسب به نیروهای آمریکایی قرار گرفت؛ استانداری هرمزگان اعلام کرد گزارش تکمیلی پس از ارزیابی‌های اولیه منتشر خواهد شد./ مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/671440" target="_blank">📅 18:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671439">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_y5vU-XTSMntD_rUFULBz6u3HskJ1LY7fHPsHtphePB5a3Y_UL5P4fB4nwAQwF_KcjtDUZp_T3Im9bq9HxTL2WuLSfeSPvWHWvaXhJIgMR-b_dHKiF5HHfKGtioht2sRJPWRl2slDh7qW2fYcgEvIzInkf7YcOkrRQBuZ_nYJYSuAlJFNkgInDFRLWcHQS72qunW4s5pEfr-ppvMJGXWmOdAysa0Uz5g1t4yjcO1t7tjczPhsLYtpwQoXRCaCnIMEPHhP8xsr4Ec6dzhd_IOR1GYn1ykUU7UT48ybboCiaeSfRVVOnWhhsGyAIvAr1szh01LD6KjNCDI6n3c5XEyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد کشتی‌ها در تنگه هرمز ۹۰ درصد کاهش یافت
🔸
در ۲۴ ساعت گذشته، تنها ۱۱ شناور تجاری شامل ۸ نفتکش و ۳ کشتی باری از تنگه هرمز عبور کرده‌اند.
🔸
تعداد شناورهای عبوری نسبت به اوج بازگشت ترددها در ۴ تیر (۵۷ فروند) کاهش چشمگیری داشته است.
🔸
تردد کشتی‌ها اکنون به حدود ۱۰ درصد میانگین تردد در ماه‌های دی و بهمن سال گذشته رسیده است.
@amarfact</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/671439" target="_blank">📅 18:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671438">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5Wb7jjbKvZgk_TRuSTxUPrI6W4rFL-Re7h9sdW2eQEGx6kugRMEJYC24y-kc-OtSWbbQZqaLtLqEkmrboz3Ogyiz92cBK0OoW5Ly04Ld5N4YZOAc3LxeQNJ3vbgx55pYGmncectCrrbafehYL8Wxw0z9WP7bsqpfpBhM7N40y96xflFwV4b7lNXTfHA0RPMRCGUv6_pOVPBgtMyz9soaQi5TWFzf5fWgVTUZQslDJNC-dQyfUGH1Q2qb8SCOPd467JKXM-pql7VbV27tDCE4_4WNhNzWvvlAd5Z8nFqFaYpzg2ccX487_deRplex3YXa70NumhdITYkp9tGgAOXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت خارجه: نقض تعهدات و تعرض به خاک ایران بی‌پاسخ نمی‌ماند
🔹
سخنگوی وزارت خارجه با تأکید بر اصل «تعهد در برابر تعهد» و حق ایران برای توقف تعهدات در صورت نقض طرف مقابل، هشدار داد هرگونه تعرض به خاک کشور، فارغ از موقعیت جغرافیایی، با پاسخ قاطع نیروهای مسلح مواجه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/671438" target="_blank">📅 18:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671437">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
لیگ ملت‌های والیبال | پایان ست اول
ایران ۰ - ۱ اوکراین
🇮🇷
۲۲|
🇺🇦
۲۵ |
#ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/671437" target="_blank">📅 18:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671436">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
جلیلی: خون‌خواهی امروز ملت ایران یک مطالبه جهانی است
🔹
خون‌خواهی‌ که امروز ملت ایران آن را فریاد می‌زند، صرفاً یک مطالبه ملی نیست، بلکه مسئله‌ای جهانی است.
🔹
این مطالبه، دفاع از حق همه ملت‌ها در برابر کسانی است که به خود اجازه می‌دهند با نهایت گستاخی، حاکمیت ملت‌ها و عزیزان آن‌ها را هدف قرار دهند و به آن‌ها جسارت کنند.
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/671436" target="_blank">📅 18:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671435">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c1785fe7f.mp4?token=aRXya8LC6PhPJOSAvIC5WtJChbaOMfgECbXkzVQxIwc9p0cADp9r6ncUl_riEOL8nXLoO_gdbSh5ehyXWPzpX7Q7n099wr50w-gVE4g6kKO1MnhadxYAiX1BlQKBgnbzAp6gnoAEi8bXwAfS0m93jHThnZm6s-qWcNAoXc4iJarHSHGQnIsqiuZpZpbBIBRjBQdB4HwYIpw8uZhGQE6_IoySQLdMAcW9-Qk6TJ_B96RRl3FJWDL1e8ReAa6wnFfpc7xQdTJThDl4i_GIBGvEHqA-sZOKZq2Urw83892xgRZbWmOgxVWAjeZ1G15IOvwXhZKo9zY0HkZW0F_bXl9dQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c1785fe7f.mp4?token=aRXya8LC6PhPJOSAvIC5WtJChbaOMfgECbXkzVQxIwc9p0cADp9r6ncUl_riEOL8nXLoO_gdbSh5ehyXWPzpX7Q7n099wr50w-gVE4g6kKO1MnhadxYAiX1BlQKBgnbzAp6gnoAEi8bXwAfS0m93jHThnZm6s-qWcNAoXc4iJarHSHGQnIsqiuZpZpbBIBRjBQdB4HwYIpw8uZhGQE6_IoySQLdMAcW9-Qk6TJ_B96RRl3FJWDL1e8ReAa6wnFfpc7xQdTJThDl4i_GIBGvEHqA-sZOKZq2Urw83892xgRZbWmOgxVWAjeZ1G15IOvwXhZKo9zY0HkZW0F_bXl9dQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از طوفان آخرالزمانی در نزدیکی سان آنتونیو، تگزاس
🇺🇸
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/671435" target="_blank">📅 18:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671433">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Di05xbGqTG8Wfj4mioVaC-oslvaLG2crpmXeHkJf-yAZFu9Z5IA08dHJWJwp3erdek7BuhAoBPbhX0PyCbBdiQLZ05N3Osn4SjA1khQYGlYjwBhBEWFuXX7eWvtM4dYGffhVFFlmoAbTOldM4m3Kg-mcCl-XG9tHKCUodgPGZ01KhGD-YIvcsm4P5A4o7mrEsVL-Xdxb-GXTAe5ZlgkQp20VZ4yiyeGT2Omu7zI7pMGYAXNgUR_11X7NadOAQT75weqEndW9vLr7EwvDn24UXR6VtNJMIo77ExImHXJX0gTA7DXq_Ozj_UE0-HrjkdU6EYmlgCALpBdGBOE1wnz9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rlwSOBf5E781CX21LOwrgCC7pF68kGL1lKTqgPluX1JI1mrj5eQcnOl4J3Plf5AjkhxTVwQzIWCYwKZTvB0YGHY40lqLShrDvmDsgThNGc9WF1VFQLnu6-WQkstBuSRhjcddmhGNsQ5s2uJgk4d4tJeFiEluXndBdcadNldi1MJtoCZpGv1ZrmmL_YEM4Fdf96efNhpXk8pjwWJbJxTzDRqtywmDc0vT9MKtLl7_pEOCwzhRCCFLvq6i4kU7cjOQLnSJw7KErY8apEMy4PfsdeD54s19Sks9hZW_AG_A7jMZeo-mYzRTZQQUiRe2KJhstEQ6go-fXNVgow4whXPKCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
ایران، وطنم ، جنوب
🔹
استوری رامین رضاییان درباره اتفاقات روز های اخیر در جنوب.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/671433" target="_blank">📅 18:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671432">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkF3sx9Ewah4t7xyyQ2gjm9ezjAu2t6xaNjgih2W3lSKZgd3Pg5nPEn96JYuft2yqgv2LWv0P8rqaWmy0tppET9OtzFH_2Cvod8RDoxA1KPgwHG4o2sZUHnmOHWnVlHOUTrg-BzWwyahlzN1t8MKPRVHeqAZLtHE5J7r7RSs4jdyYUSVjdvKRKJCc0-MQQRpOIhL-n5Mlgq4iv-YjdEAq2Ll0LIyNirvZbhL2HPu11JcGFtiBb5tZJCI6XjrmwNuRuUpYLOnpS1TPPmHB4ek2bSXP9ewK6WpoT-VU8E6bNPfU9iZWkH-hl93X_OLAvpP4LsYuwuUbaJzjm7XL4XJgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چه‌طور یه انتخاب کوچیک می‌تونه به کاهش مصرف برق و کمتر شدن قطعی‌ها کمک کنه؟
🔹
انتخاب لامپ LED با کاهش ۸۸٪ مصرف برق می‌تواند سهم شما برای همکاری با هموطنانمان در کاهش مصرف برق باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/671432" target="_blank">📅 18:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671431">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUNWEwm_jO0DVWXxzhnMJlnpdljg3MDc8AtNnGE-WrvrWJ739RcVQsqjhQq015oOnRd5s52z5douA3qAFWuFG4x069Qhp5i3oBj4xLf7natbx_hxn7TykgEdlPJScoXIu7hZo-2nbbkgUtV00udcmw1d_ZP1bGp1Ljw6S3QnEVWBo9Qj-3c0e0ZxpNhdV0u9P7bVuia8pM9657i0Rf51RYqYvj-fN61mi17pXQ6ip7IRK3nxYXhBCHwAS2aCmIMNdOq0OsL0L9uEUjgLp6wFo-BUpdpWpmWOSBQq_0FRAZY8fQiROPiEA1k_TMA1PWEEM1SNbX49pF6yKj3HR0eoJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران درودی؛ بانوی نقاشی ایران
🔹
ایران درودی، بانوی نور و رنگ، نقاشی بود که از دل رنج، زیبایی می‌آفرید. بوم‌هایش میان رؤیا، کویر، آسمان و امید سفر می‌کنند. او با تلفیق شکوه ایرانی و نگاه مدرن، جهانی شخصی ساخت؛ جهانی درخشان، شاعرانه و رازآلود که هنوز مخاطب…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/671431" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671430">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7151964478.mp4?token=tU7JuYsrI8XpM_GD-lJlJZ10-ixJZ4xf-5TPUuPRhwrbDkyFAMQwDKD7tWv2MEU3UCdktI7HUnGz6KAiWA_KqByyiOgFHwTJxs9ZIqk-RSnAefml1dpEmeTit9JoZf6zNVcVmnxzAmiEEL54HyncKj1Lo3z7RZ1Xl014ECBuRTfr2FAHe4w5-LJEphgp1uASM1LFYLLHLVoMplqbU_VnlDTdsU4FG6CX5yjgCwL9H7-ykgL1mVbs5-088aw0iCLXOKzVdul3Zqp_-BE1O-wK2adsA6A9xLL_kd11EEj7s9okU5AQhF-zxBOENh1iOYwvqUtyQkGS_xFopRF9dwOdOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7151964478.mp4?token=tU7JuYsrI8XpM_GD-lJlJZ10-ixJZ4xf-5TPUuPRhwrbDkyFAMQwDKD7tWv2MEU3UCdktI7HUnGz6KAiWA_KqByyiOgFHwTJxs9ZIqk-RSnAefml1dpEmeTit9JoZf6zNVcVmnxzAmiEEL54HyncKj1Lo3z7RZ1Xl014ECBuRTfr2FAHe4w5-LJEphgp1uASM1LFYLLHLVoMplqbU_VnlDTdsU4FG6CX5yjgCwL9H7-ykgL1mVbs5-088aw0iCLXOKzVdul3Zqp_-BE1O-wK2adsA6A9xLL_kd11EEj7s9okU5AQhF-zxBOENh1iOYwvqUtyQkGS_xFopRF9dwOdOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کابوسی که هیچ سلاح آمریکایی قادر به حل آن نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/671430" target="_blank">📅 18:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671429">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فایننشال‌تایمز: ذخایر بازار نفت در حال اتمام است.
🔹
ادعای تازه ترامپ: روسیه آماده است به‌زودی توافقی با اوکراین انجام دهد.
🔹
یمن اقدام انگلیس علیه سپاه پاسداران را و گذاشتنش در لیست گروه‌های تروریستی محکوم کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/671429" target="_blank">📅 18:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671428">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
تجاوز جدید رژیم صهیونیستی به جنوب لبنان
🔹
منابع خبری از حمله توپخانه‌ای ارتش اسرائیل به شهرک عیتا الجبل در جنوب لبنان خبر می‌دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/671428" target="_blank">📅 17:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671426">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f72b47b139.mp4?token=V-MJAmgjQXZhz9fUoE44nKc8TcVAeio7Kbf3duVVb9a3B9bC3HIGwvE53_tpd2RsA3itXP1hKY3HUuITqTd4zMoskMUILIzzEFZfa_1ah8DzSOQLKKwr5oKhSApHLBN1CZFIayVVYtaVvcUhHGvqmV26qNkb5K-1-G-b7kBO3rLsT72MvbfO_ncG9461ET3lij69JGvUJqHi8Yn565X7T2Eh2BrtxTv9fTSilvZsf3NL9Lx8orCQzK2KQiRWV5xkdynhva3QD137LrXtXE4IWoKSeiQ4pd_2u-Mv-U3ik47bQ4tQ_Vka7tn4boSH2y1fyWiUdHGjSnPPRKucWSNk3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f72b47b139.mp4?token=V-MJAmgjQXZhz9fUoE44nKc8TcVAeio7Kbf3duVVb9a3B9bC3HIGwvE53_tpd2RsA3itXP1hKY3HUuITqTd4zMoskMUILIzzEFZfa_1ah8DzSOQLKKwr5oKhSApHLBN1CZFIayVVYtaVvcUhHGvqmV26qNkb5K-1-G-b7kBO3rLsT72MvbfO_ncG9461ET3lij69JGvUJqHi8Yn565X7T2Eh2BrtxTv9fTSilvZsf3NL9Lx8orCQzK2KQiRWV5xkdynhva3QD137LrXtXE4IWoKSeiQ4pd_2u-Mv-U3ik47bQ4tQ_Vka7tn4boSH2y1fyWiUdHGjSnPPRKucWSNk3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد: خوب خواهد بود اگر اسرائیل از بخش‌هایی از لبنان و جنوب سوریه خارج شود
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/671426" target="_blank">📅 17:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671425">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e88234b22.mp4?token=HouTw8_JetQN36GJxo1g4LFtzhdFPAXi3HM7QncJAogr1lhqHTnd9Z78VGDECv9nbPL_bISlIUzWZvgWnhh1OFm4Il2Zz4KqfbZ4jjUYVZdzF8MOq6_cN4wNtsK2WHNvU3oZEWJFR0qF5UejKVE1MIVfaiu4jF8gJs7bA9jiE8D7f85q10Jrr58KWfmT0q6p3Rs4TnREK2p0vnXB-F1GuhZYDQ3a4bFRkdI1YbbFco79C6ViEjjQjPmt-TkECFTQY_IDo-Gwcdi7QRtyqzFjqGCIIES0L9FHCnEC6MktI8LojyewMu-phr6OfdvVjHFc1eAuBXb_WmmnNGis8zaBlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e88234b22.mp4?token=HouTw8_JetQN36GJxo1g4LFtzhdFPAXi3HM7QncJAogr1lhqHTnd9Z78VGDECv9nbPL_bISlIUzWZvgWnhh1OFm4Il2Zz4KqfbZ4jjUYVZdzF8MOq6_cN4wNtsK2WHNvU3oZEWJFR0qF5UejKVE1MIVfaiu4jF8gJs7bA9jiE8D7f85q10Jrr58KWfmT0q6p3Rs4TnREK2p0vnXB-F1GuhZYDQ3a4bFRkdI1YbbFco79C6ViEjjQjPmt-TkECFTQY_IDo-Gwcdi7QRtyqzFjqGCIIES0L9FHCnEC6MktI8LojyewMu-phr6OfdvVjHFc1eAuBXb_WmmnNGis8zaBlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پدر همسر شهیده رهبرانقلاب: اینکه ملت و رهبری خواهان انتقام باشند منافاتی با مذاکره ندارد
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/671425" target="_blank">📅 17:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671423">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lOAZgS2DZTAEMVw4UNYaQLHs8NnHgQmrgSM0qfFWNUmyH7oPEm_zOmqAQjiX5XgvZnL4TYaZ-OXHA8Nq9o9eepzje-d3HH5O87BIFihx56tSeu8r2d0jxiCEkvspM2Y5ZnCXV3hV_0iaHtPaGF5JAEk_qqWalbm92vEl6Ch5lkvAp9UtrTO4Qa3ECpzABLYqIFTv9Q0cqwZG5D7BsAq0UAQa6Sq1DCADTio7AE54FbyTji3rqPhX1DdLo3vERi4cmZFzFqr0GyF9woDHnSR5xst6tBTCaEPuZFLTpBMIC4klUrc6CSzjDlOa22JoHxb9du4uI2xQBd-9ikP-8cYjDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UvuPRoscqm-XKgGvyywq3m0gd-DgsVmR0FVax7BjJqLYc7EsArthyqDQHSGpXUB1Fix0CwxkNjT82RG3eCoqDg2dpb2iizqdrcA6bf_Z5K4K9_l5XfrYcoA_J0VMA8fHr3jntUyNUVieL3j9mHhejXJUtOYf6-cTxsqVdmuwTlPEbNoisnCVgxnHDTN0yJWkL_5whOkkArsowPwNVz6yoTz4mVzJPtFYVTfKuoVFaK_H4Dpovb5khwkwZ8Oqi0oHMZIX8kVDM9Zbd5vO5qU8bFPTuX8ykFk-yYr2uTM2tUAPQ5s-VMQOfH-7bcHM4fnttHwR7P1Fpxs-8I9qiszchg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایران در رتبه ۸۶ جهان از نظر چاقی مفرط قرار دارد
🔹
مصر، آمریکا و عربستان از جمله کشورهایی هستند که بالاترین نرخ چاقی مفرط (BMI بالای ۳۰) را دارند و ایران با ۲۵.۱ درصد، در رتبه ۸۶ جهان قرار گرفته است.
🔹
در ایران، ۳۲ درصد زنان، ۱۶.۳ درصد مردان و ۱۲.۴ درصد کودکان به چاقی مفرط مبتلا هستند؛ موضوعی که نشان می‌دهد زنان بیش از دو برابر مردان درگیر این مشکل‌اند.
🔹
تغذیه متعادل، فعالیت بدنی منظم و اصلاح سبک زندگی، مؤثرترین راه برای پیشگیری از چاقی و کاهش خطر بیماری‌هایی مانند دیابت، فشار خون و بیماری‌های قلبی است.
@amarfact</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/671423" target="_blank">📅 17:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671419">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hC7zQzfxVL1trCq58hRwncO02v9g821th-v6g8iqIb4r4v2YSIA9xgERSiSyI5w43dw3XSEqSXySJb7fZIQP1H6xPPJ2w4YvTBTh_fwGAiNepnUzQz7IJChYKxCHoqjWUFdo9vzu3FBtHxynLAE4KPoMHmRnQkRhdJ0hBHd4KwxrdNSRtE7s0KzD-wmhBM9i6tDvviS9FdowsYnVLjx5CadE6smWFAKNxxWiSaHeB8JUYtkaLXQQBEzViD3OVlBLy_MvcMHd-01yGbCGIXt_8vmv2EWjfrsLoF9PU2JT0BQQpFgvPKyAXlrYQbtgagI_yC96W8fiFx-fvVzNQmd0aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u502A8Z88HgGFqJ-Wnb99jc0glJ305tVF6D0FJ3uEulmQdRuMu2JoBxorvY8k4LAEnQFu25xGfrFq1tyXKZD4JxzshxkIWxiBzaYe-k_osrKOTos9h2f--NdM8VknD3hgliQ58Q-OFcbTkv0awSaaJP7KiFo4UdGm7pirsbIfvhm3CWhtelONMcVqhWAt1jEYauIEFoiENwj4ipU1YXHNoloWCmhsRITUErgWlxwZcKpV3Mzjmo1Rd-3Go3lRSD4sIVh0UM4K5qQwwYhHCLCQrlSsMSaXg6AlDKTK76PZErs5mTBBw_n4ZyhUbH9pk_oBwNgAr1wyhi-mIoufLFaWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fKhynGwLEuBieDUW0dgBX2Tf5dyyK_5dMiF2P63kUiatxHcfi-iUlE3abQRLsuYl65s9p1RdsW3qUp0NxcQ0yso1r8q82NpwOiPvLWAWGpiB-MI7pgzqicy9Cog24lWfM2OvflBNWQdtwYQkkas727HAd57LI_QCB_7t2aPdqpp0eRvR7__1GB4NrzdAB1aCz10qkoI-Wda4RrXVwevK0XwRv5c1NHT75tzsZf_SSCQh7h6rhOXe5ACSkSQAQB4IS3npbyuG5-PjRATIqaDxZdAwn4_kFYMVenJzTmuwwl6dquw2Bn5Nbi6nV9xk1OXciUCUb3Om-kHc4TaT4riAcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5fb84a8b.mp4?token=JTj1wsDvWEvdaE8d1u60HIgXCj9t6GJQ4jRKL87plCdhJqbNIorsF0ZkanOfyxFcFGaDoT4L5QzQm_-VPeGSh3nc2DnfIMtEf2c1ujLFgFYN49dJNzs1e12G9TEGEqpq-2uwG3lhcZPSCbfhATcb7QxGd3jmzNUyQL9vc2pg3zdB1u1Y0pkYX6uhPVYTYr8Hwq61yBvVOLS5iIoLwO4nGos3ZIXtw9G1q1xRAssXTRTo4_Lisj3-jGhtiIpAviXul8s_cZMZR66xgZ2VlW4VWo798peskQw7aJtfa67cNy2aAcELanGzB_6O_b9njHCr8GWh5L8h7R_lvbJOoOLTNY8Pj4i22twswahsdp7kro6l_HXSParK-uNfTKmGtCxVOE_XRvIGL0xP6IPxKiJb7MCaeIilpZ37xuFFqEX0oj9SNHKSqUVWTEqoKkq6ynBiHdyak6KWY5RN9ucPUIu1xnF4FbE8xcsilywFAiRLsz0voc4W7wTOroFuws55ZfWyr6Q6cwOw8ykePETN4a3TTq8IKcGpRCEUQF8ojQ0p0l9leZZJqK4u077_jACShLPIBNmPI5csNL47d4LF9Epj8m1E2u_gtZcsgOnf9ireJgNNWU1H-uACf7Ldy88dmYD4AzmfN-cG3vjjsHtYW_pir0UUJyLy1vqcb38Y2mJrNh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5fb84a8b.mp4?token=JTj1wsDvWEvdaE8d1u60HIgXCj9t6GJQ4jRKL87plCdhJqbNIorsF0ZkanOfyxFcFGaDoT4L5QzQm_-VPeGSh3nc2DnfIMtEf2c1ujLFgFYN49dJNzs1e12G9TEGEqpq-2uwG3lhcZPSCbfhATcb7QxGd3jmzNUyQL9vc2pg3zdB1u1Y0pkYX6uhPVYTYr8Hwq61yBvVOLS5iIoLwO4nGos3ZIXtw9G1q1xRAssXTRTo4_Lisj3-jGhtiIpAviXul8s_cZMZR66xgZ2VlW4VWo798peskQw7aJtfa67cNy2aAcELanGzB_6O_b9njHCr8GWh5L8h7R_lvbJOoOLTNY8Pj4i22twswahsdp7kro6l_HXSParK-uNfTKmGtCxVOE_XRvIGL0xP6IPxKiJb7MCaeIilpZ37xuFFqEX0oj9SNHKSqUVWTEqoKkq6ynBiHdyak6KWY5RN9ucPUIu1xnF4FbE8xcsilywFAiRLsz0voc4W7wTOroFuws55ZfWyr6Q6cwOw8ykePETN4a3TTq8IKcGpRCEUQF8ojQ0p0l9leZZJqK4u077_jACShLPIBNmPI5csNL47d4LF9Epj8m1E2u_gtZcsgOnf9ireJgNNWU1H-uACf7Ldy88dmYD4AzmfN-cG3vjjsHtYW_pir0UUJyLy1vqcb38Y2mJrNh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار تصاویری از پذیرایی یک سرآشپز ایرانی از بازیکنان تیم ملی اسپانیا در جام‌جهانی موجی از واکنش‌ها را در پی داشته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/671419" target="_blank">📅 17:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671417">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
فوری|نشست علنی مجلس شامگاه دوشنبه ۲۲ تیر ماه با حضور ۲۵۹ نفر از نمایندگان در بهارستان برگزار شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/671417" target="_blank">📅 17:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671416">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlEf-ilwJWH35cGvObChzJDwyQ8I49ov2g7iARMedDehZA4R6P-hmyitkJmZkNTTC4aZhJGNeFly5RajeZOSRggcB_j2JCV0-Y8FPTcwlafmFlu_-1np6iIpHXnLH3-qbW5r8NnTiMv9JOcAfsM7KbtZjzDJW5KF0wWsaacz_gJxtuto1ezu8yyfhFtmcUd-dMmUsmbriEVuLjt0Th7rEEykrxBo3ryN_OAMFKVrR9q4Yo9mitAC5LPSVE0hPi9jRjwn5lZJYLEHllOro36OuJUOnNisxAzft4fTWw0FPbQrNWl58W0bgm1W9c4GxaGdblVSB1oO4bu-8bpL2n2mgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه پخش روزانه خبرفوری
مطالب مورد علاقه خود را از طریق هشتگ‌های زیر دنبال کنید
👇
🏸
ورزشی |
#ورزش_صبحگاهی
| ساعت ۸
🍱
آشپزی |
#آشپزی
| ساعت ۱۰
🧠
روانشناسی |
#سلامت_روان
| ساعت ۱۲
✂️
فوری استایل |
#فوری_استایل
| ساعت ۱۴
💰
آموزش دنیای اقتصادی و سواد مالی
|
#دارایی_هوشمند
| ساعت ۱۶
👑
معرفی شخصیت‌های تاریخی
|
#نامداران_تاریخ
| ساعت ۱۸
📚
معرفی انواع کتاب‌ها
|
#فوری_کتاب
| ساعت ۲۰
🎬
معرفی انواع فیلم
|
#فوری_فیلم
| ساعت ۲۱
🔸
نهج‌البلاغه
|
#نهج‌_البلاغه_بخوانیم
| ساعت ۲۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/671416" target="_blank">📅 17:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671415">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
تداوم حملات یمن به فرودگاه ابها عربستان تا خروج کامل از چرخه عملیاتی  منابع آگاه در صنعا به روزنامه الاخبار لبنان:
🔹
حملات به فرودگاه ابها با استفاده از سامانه‌های موشکی جدید و با شدت بیشتر، تا خروج کامل این فرودگاه از چرخه عملیاتی ادامه می‌یابد.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/671415" target="_blank">📅 17:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671414">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJJ1J2aRJ88SSszTyRjO7XKUgKrFtrMwYpnfvKscDk1mGuD2CiRoZmGrGlqCtxruoyOYDn1MC9uXyp8X_43foSGCbsxlb2urZpWs4jXI9dHvv2aXNcGxGibk2vPz3-BWVh_BeXuokvE9zzEcvX38XHGxNitEc6gHaPEXedy0bxRajAZu-p_u2FfgRJP8pLEhatkLqjnnJM7A3K50I7ZAnSHJrvcLj5_IfKLfBPjgtYRDF9CjFV4y2YmwPX8siAQ1tGkd31x32RLzI8q9Jg0haCDHmBUXlS2b1o0M68CvHoodCXVhsjspdpwOFa6GZrQ8GGamWeQmL5_I0c5xvxiVoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
۱۷ سرمربی از ۴۸ سرمربی آغازکننده مسیر جام جهانی ۲۰۲۶ کنار رفته‌اند؛ آماری عجیب که از موج بی‌سابقه تغییرات روی نیمکت‌ها خبر می‌دهد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/671414" target="_blank">📅 17:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671413">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Np_SystHEl7mqf19CmvOrWtif7yrkNxghqApi1zROhGWy8U8a3Khq6h8R6l4NjYrphFJMMLkCYkL7UXxwshHu2Rsko3pBj8nh7uZ3dkIlgcr_HRDnaK9xjgVC-tEdJ7d4yTvMu-DtceyWrI1x1JLoRgFxhqjsnKiaokCKA2lZ2KDFw2zPB4semWSjPGcSiyKXdy9O2vtA-uXFvW625bFHp2qP6Qtvq3OhHKsvpmM2dzABz3zzL21_zCysNaYNmlHoZf_dOlk3gHqxakEpA15MycYasUiRuE7CPsRJu_MgNRQa2JOH_N1laXURkw4mLjYEQuOOBY4I5HSVRksEEU6fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش اینستاگرامی محسن چاوشی به جنایت وحشیانه آمریکا در جنوب ایران  محسن چاوشی:
🔹
جنوب خون من است که می‌ریزد. به یاد جای خالی مردانی که دیگر  باز نمی‌گردند⁩.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/671413" target="_blank">📅 16:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671412">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
کامران یوسف خبرنگار پاکستانی: پاکستان به نظر می‌رسد یک گام به عقب برداشته و پس از آغاز دوباره درگیری‌ها میان ایران و آمریکا، رویکردی «صبر و نظاره» را در پیش گرفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/671412" target="_blank">📅 16:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671411">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
شاهکاری به نام Lindt؛ کارخانه شکلات‌سازی در سوییس :)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/671411" target="_blank">📅 16:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671410">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/699d8b25a3.mp4?token=grfo1Uh4lkBaUSCWQf1rDB5g7AldbfQBfOZhxBy7eq8cDapAGLSY9o-2HUrgVz1xIR7fvXlYgbk0XBbgzTkbUSb9S2R9NVxiyE6yJ81by_ZksxDc971lVbdzbcXFEsGYynOpqd8L9Qdk08-5fxG_nCDYyIsmtYizW2YgkFJNx-OgGOVLd4FwA5XOTR0JX8by0HXTPvZuanto2qpKAZiNnNLSvjLBQs6ZsCX1sULJwUMbP_7xtCWX7YkyGKGBqPFDyfnuxfRPLZLS8Dbb7r6dus7ly4lT2sRAjq2C_A-6IMmvarcM3KhEItZqHi307V-dmzWK4lIZJ5soVyH2U3r86wr5BrH1ySk7dsS2j5l8PzXTtPYiBtO8S7kJ6sLhmsYTUzNuSKzeoiymB4_gV_JN-Z83ZZaTHs3oD9_2KEeYwnMgnyptezKZFNGjG6ypJy_dvADFBflm_rdJzIBSPRO9y2f4kPtJ6e_x1jcMv3F8ZlkEzqa_suBhFzk6WMmB5tdDXNkMlBWetR1hqZRJjMx_krQimV6mqzJ1VYc6PKGwUy3c3pu37tKVVaj1p2P7UOrIMZWnWQffO9dvMtYCtYfYNNQE9axM208ObzR6tx-NVz3DCvhvBZPdO5vXrFErE1YqGnMfdXEubF9L_BuE2P-f_P0ffkTT5M7XBA8Q58HEQ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/699d8b25a3.mp4?token=grfo1Uh4lkBaUSCWQf1rDB5g7AldbfQBfOZhxBy7eq8cDapAGLSY9o-2HUrgVz1xIR7fvXlYgbk0XBbgzTkbUSb9S2R9NVxiyE6yJ81by_ZksxDc971lVbdzbcXFEsGYynOpqd8L9Qdk08-5fxG_nCDYyIsmtYizW2YgkFJNx-OgGOVLd4FwA5XOTR0JX8by0HXTPvZuanto2qpKAZiNnNLSvjLBQs6ZsCX1sULJwUMbP_7xtCWX7YkyGKGBqPFDyfnuxfRPLZLS8Dbb7r6dus7ly4lT2sRAjq2C_A-6IMmvarcM3KhEItZqHi307V-dmzWK4lIZJ5soVyH2U3r86wr5BrH1ySk7dsS2j5l8PzXTtPYiBtO8S7kJ6sLhmsYTUzNuSKzeoiymB4_gV_JN-Z83ZZaTHs3oD9_2KEeYwnMgnyptezKZFNGjG6ypJy_dvADFBflm_rdJzIBSPRO9y2f4kPtJ6e_x1jcMv3F8ZlkEzqa_suBhFzk6WMmB5tdDXNkMlBWetR1hqZRJjMx_krQimV6mqzJ1VYc6PKGwUy3c3pu37tKVVaj1p2P7UOrIMZWnWQffO9dvMtYCtYfYNNQE9axM208ObzR6tx-NVz3DCvhvBZPdO5vXrFErE1YqGnMfdXEubF9L_BuE2P-f_P0ffkTT5M7XBA8Q58HEQ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه قصاص انجام نشود حیات جامعه بشری در معرض خطر قرار می‌گیرد
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/671410" target="_blank">📅 16:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671405">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nz_7_yGXmXJzMF7ykt5Vo-EtOe9y3UeUOMlosEGrWmxBO6Td5Rw0ePmESl_MI4GM7Cxb_PvG_hiDImCQOxieO5YmMHqfmCKxbkT-ffFa16cS14Ou8MvkZdIYXH0EjSVRIGprhmMqORGcGh1ida7dHr_CZADqmPAtjIMAsQGZY3uWycHJCC8rp76kuC-U--3hvlnSD83hN2pm9zVqnmpVNCc8SZ93jlkVS7xRsW4oMEyB475v1Y4phVavihuU-e-OB8P0YHCo2zzKfVfmVOA-FzmTINrhrBHliHRvbIjOyim7kh3GflemugzU1-Q8kJ510-xzGM_kCP7phFv09rpZig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XyihS84tHjmfRl9lNpyr4TBCfgE7XAbXwiJ-lrGtRLbvFctTLSwEK9k3iJMOsfvRl3kNImClJ_MULfl0x6NfC630JIW9xgM8hEQpOf0mL4YhtwhTg5JNcMcDNMTtCvwoQ__58AMeyyBjuiMu1G8SCtnLrg8rlUZx7oUi28UfZq3QEn0SDQaZ6M4x7hbk9fYJofk0NQiWx3sHOrvlUcijazKibw7-mnJeeFsHnLhX7RVTUVz4idVtR57f-bS5QOZcwhkS24zjBe0FjBgUMPLiem9S_vpF5HTiM6o-jXWWo2NBPc3ZgjFuyW0vWUik3219sB2U8PB-djZ6N2Y-5yh-SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AwaK32-sb7ZL--sqOODVN82BQbld_GKop3ZvD2lk_pOqC5a5O-fH70p4r0m-zgVQDJfPCHHrJ8iSPj-DR9BDPj5P1lWz6UMxAjQZ1SVvstg5sfnEMFWEy17WJYm_voVQP_kTuerMqfvII5L8zlmIX1jBEXych9kLUIH3kpP2oC9wO61xIRW8JkUWEMF4-Agyzl7jKZ6YQbc6EP-fveJRImkFJ0lntwFqihBS0gzzuPziOw4ME2xgwQtK4Jj80cjEj8Zi-U4mJEWOxYNx-BHr2SJ4gSwwiuFRqLi5n5cu6dmaH57W675AfvMKan24y_2Mr1q5RVlU12m9xs-h8nNtag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oklv56r7UJ3GVSpO-6sjXc-HUgvMyIAWaF30a9ylXYDskiBhFGeBR9zHiv9Ak8ZeLGiRtkThnTimFjY4HWSrvjnMTtqKDuGlKMWuOgM-Z9w3PXoY4dxZorF4MdkafyOidUsjseXwW3KRgp03TbQ0-8Qp8zwoAHWwID4-tB9pHfh144-PE3tKUt-r8HISRnLPIpzOKmd7QMO9izZ-JG-whvlkc3-CH6ck_kEgysW9vf4ETBA92HCtbie3lYftmct5R3a4fp8GW-XoQe_iHJFnKVdeCbA-ceL4Wyo4MHwEWwVWNx-X40ItfLC_aRncMqlDoXESG82-IehgqvIqgZl0Qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از موکب تک نفره اربعین برای خدمت به زائران پیاده
🔹
یک بانوی سالخورده عراقی، موکبی کوچک را با هدف خدمت به زائران پیاده روی اربعین برپا کرده و در گرمای شدید هوای جنوب عراق خدمت می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/671405" target="_blank">📅 16:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671403">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9b25a297.mp4?token=GjsnL77MhFRR5Iz9HGg8VfsuCzDhprT1KTtPPCa2H1UTPBNgNNePhiwH4Raklc8-dJ7YqqEMn3eC-DHXBf_tyoCY6mtpdqmKSYXD2ZKWVuViD0QcjzmGVRSBPPPxrO9ZsxQmCjxRtufk687wI5sThSRm1_H8ISWWPkyWr4K8li1PcU78KDeUbTfU627XQXabXF6BRoJnbAieqw6js7QvM5i4zOc4NmPn0HwwGCB7Nnl8fRDvSf3Ux5mBtfZVF5_yQJHWdtLgD3cTGuN9MMzrmDWcqG7ZSH7guS7RR_1iPDjFHruceQERO0eVA09TmAS7zu7KRzcjbED1SMMH8NZ9cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9b25a297.mp4?token=GjsnL77MhFRR5Iz9HGg8VfsuCzDhprT1KTtPPCa2H1UTPBNgNNePhiwH4Raklc8-dJ7YqqEMn3eC-DHXBf_tyoCY6mtpdqmKSYXD2ZKWVuViD0QcjzmGVRSBPPPxrO9ZsxQmCjxRtufk687wI5sThSRm1_H8ISWWPkyWr4K8li1PcU78KDeUbTfU627XQXabXF6BRoJnbAieqw6js7QvM5i4zOc4NmPn0HwwGCB7Nnl8fRDvSf3Ux5mBtfZVF5_yQJHWdtLgD3cTGuN9MMzrmDWcqG7ZSH7guS7RR_1iPDjFHruceQERO0eVA09TmAS7zu7KRzcjbED1SMMH8NZ9cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از انهدام تاسیسات آمریکا در مینا عبدالله کویت
🔹
صبح امروز سپاه پاسداران طی اطلاعیه‌ای اعلام کرد سوله‌های شرکت KGL متعلق به ارتش آمریکا را منهدم کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/671403" target="_blank">📅 16:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671402">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
دیدار ترامپ و نتانیاهو، دوشنبه در واشنگتن
رسانه اسرائیلی i24:
🔹
انتظار میرود دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز دوشنبه در واشنگتن دیدار کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/671402" target="_blank">📅 16:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671401">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HegyA1Ea1aeV-BvMfRgAxPVgGLepJBOeoeXaTe1t8tlJWjbimRV-xiE8cDDFM3-MSlZ8xx1teqCDIOOyYRpU578wwxEY4WI5NK4A1JwevUasJbqSbKftXl9xbz4Up9LkH81eFwQrAXmDtkGPmC8HCKJvCyGl8EGYHEwrKHI33hbYjck4j0IK2Kwp-QeveFOEePP524oaZWwORDg0VTe_UG_8QTGlit3Vf0ImO8MiCSueeuwpGfJcXmcxrUPF6JaWOOCcdzKU5lIuvk-IZQpp0mstxg3eZy0uu4-_d0R8aa4DzoQ73A1IaXASBKytrP_A4U0Efb5bcMKZ9xpfbSMC4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنی که از سایه برادر به مرکز قدرت رسید | دارلین، خواهر لیندسی گراهام کیست؟
🔹
دارلین گراهام نوردون، خواهر کوچک‌تر لیندزی گراهام، در مراسمی رسمی در ساختمان کنگره آمریکا سوگند یاد کرد تا باقی‌مانده دوره سناتوری برادرش از ایالت کارولینای جنوبی را بر عهده بگیرد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3230598</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/671401" target="_blank">📅 16:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671400">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08b6047653.mp4?token=XrSNZXiSYM6zDNWx7Re_f5Kw72mYz0ZBOOek2wj9ALlymLGRQjIJBBtwrTvMBPPM_6zZGOok1X-ixmfEDD1tWts2aTonmbQhr0hHuXXTiNsq3gPuxnkrOkQ02MjARFddvtrEe7DoQS1-Uy298GLsd3cPqj_Ccnw00MXv_o6qSlqF8QRA34E4gdPt-wAsKDkR5KIijYgem_uvCrYue9NNKM5ojoA_vwKR0iFm2-4kqnQ5h7e5HWQiINmQ0EU76LqNs7NiKLbTxbPzDGlqrF0CVXvVD6gnvPKTNQ0aAinwc_lpeRd8x8kisAWMXf-85C3G3oS2m-gQhH1SbplLkK--bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08b6047653.mp4?token=XrSNZXiSYM6zDNWx7Re_f5Kw72mYz0ZBOOek2wj9ALlymLGRQjIJBBtwrTvMBPPM_6zZGOok1X-ixmfEDD1tWts2aTonmbQhr0hHuXXTiNsq3gPuxnkrOkQ02MjARFddvtrEe7DoQS1-Uy298GLsd3cPqj_Ccnw00MXv_o6qSlqF8QRA34E4gdPt-wAsKDkR5KIijYgem_uvCrYue9NNKM5ojoA_vwKR0iFm2-4kqnQ5h7e5HWQiINmQ0EU76LqNs7NiKLbTxbPzDGlqrF0CVXvVD6gnvPKTNQ0aAinwc_lpeRd8x8kisAWMXf-85C3G3oS2m-gQhH1SbplLkK--bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هلیودون؛ ابزار تخصصی معماران برای شبیه‌سازی دقیق مسیر حرکت خورشید و تحلیل نحوه نورگیری ساختمان در طول سال
🌞
🏠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/671400" target="_blank">📅 16:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671399">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP-hK1dR_AVswq5vzpC1i78um-zqsTuO4o-ToSpT4QL7P1IglSrOJvGK1E-7l6yKr9tObfnXR25zdno2iAo8lYOVNmdApngFlz1Nkg-Fo82mL3jGbdpkW6tRx8ebn124Nd3_awvopZQIaJpmlwQo9lKRm6oh8PipwDnqPfZ_YQsPTkCksNBTulXfzJuXHUIzPhkr5QVkurRe4UeGFL5F4tz_bh_pa8s2xQnkkDYdhK1NPnYshmlr72iQvKd3UdwyBaZ-paEPTaRCtt24S2Rm90LvzvHIQajfADavWte5Ks18jlOokjdqCwbLD7L6ldfXvjUNra0VsbrgWrXD-nHAFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور احمدی نژاد رئیس جمهوری سابق در سفارت قطر در تهران و امضای دفتر تسلیت درگذشت امیر سابق این کشور
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/671399" target="_blank">📅 16:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671398">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7485d4f748.mp4?token=sr1rA22-_uHgKqLb_2Il5hpO3OXzT0qRmAOALv-V0HawT6NvAfqxXIbkfjum07KiSoYXBU4OZj3vfcS0l3yluv2XNJ0OPibchZJs_ZPZq8ANRIcG6ugH7jgj4y3lSIkxYjb1CMinCtGOXmSjamh4AKO_umVmKS8LNwcvSIwFUVgL1vd-M3Y4RAbrobAnCJ9wbuHZ9EX2hoE6e2wYH01DlFNk6ZEVD3IyjBYFJdcdPAiJyFClPRcIzgsK8VcIKclNgpntKv_BEcMj6_tdOksu-dKWUnoXLK_6RW-vkJGmIZBdLCnmaEcHmE6eNWx5qfoMUNey26prz5dLNHByVlu6wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7485d4f748.mp4?token=sr1rA22-_uHgKqLb_2Il5hpO3OXzT0qRmAOALv-V0HawT6NvAfqxXIbkfjum07KiSoYXBU4OZj3vfcS0l3yluv2XNJ0OPibchZJs_ZPZq8ANRIcG6ugH7jgj4y3lSIkxYjb1CMinCtGOXmSjamh4AKO_umVmKS8LNwcvSIwFUVgL1vd-M3Y4RAbrobAnCJ9wbuHZ9EX2hoE6e2wYH01DlFNk6ZEVD3IyjBYFJdcdPAiJyFClPRcIzgsK8VcIKclNgpntKv_BEcMj6_tdOksu-dKWUnoXLK_6RW-vkJGmIZBdLCnmaEcHmE6eNWx5qfoMUNey26prz5dLNHByVlu6wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور با خرج‌های روزمره و کوچیک سرمایه طلایی بسازیم؟
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/671398" target="_blank">📅 16:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671397">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14c810eb0d.mp4?token=GM-rTnB9CxSwddMUYjn3eVbwWxCTNRRtVTVtlubso9u_VsRvdPgz-sOaWjRqzMnpNjJ6ArirYJl48V7IBZ7GGgnkAnWr7SKSd-GGH8e__WRSqt8l85InmR7nZLObxhUHamg0bYTRkmGe454hP25zexX2h2LHVVPX0XpX48MBQfi9cgo90w2qwDb9b9mOalRQwvFYxsHFMn7oqDZ6-3Q7vj2JWd_XDXWCFsoDPNxhwDhlTkIfOOhyKw0ujETphKtAefP4-A2RL0t4lnQ3qwzW3jNuAi68oBVRzg0E0gKsJXDnlP3VtzX3q0GVzP1mW4FgrtBHvBC_2RxoEwCRDYOl_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14c810eb0d.mp4?token=GM-rTnB9CxSwddMUYjn3eVbwWxCTNRRtVTVtlubso9u_VsRvdPgz-sOaWjRqzMnpNjJ6ArirYJl48V7IBZ7GGgnkAnWr7SKSd-GGH8e__WRSqt8l85InmR7nZLObxhUHamg0bYTRkmGe454hP25zexX2h2LHVVPX0XpX48MBQfi9cgo90w2qwDb9b9mOalRQwvFYxsHFMn7oqDZ6-3Q7vj2JWd_XDXWCFsoDPNxhwDhlTkIfOOhyKw0ujETphKtAefP4-A2RL0t4lnQ3qwzW3jNuAi68oBVRzg0E0gKsJXDnlP3VtzX3q0GVzP1mW4FgrtBHvBC_2RxoEwCRDYOl_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توقف استفاده از کریدور تحت حمایت آمریکا در تنگه هرمز
🔹
داده‌های پایش ماهواره‌ای «کپلر» نشان می‌دهد با وجود ادعای ترامپ مبنی بر «باز بودن تنگه هرمز»، روز گذشته هیچ کشتی تجاری از «کریدور عمانی» (مسیر مورد حمایت آمریکا) عبور نکرده است.
🔹
در همین حال، آمار حوادث دریایی در منطقه به ۵۶ مورد و شمار قربانیان دریانورد به ۱۷ نفر رسیده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/671397" target="_blank">📅 15:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671396">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
رسانه آمریکایی: پنتاگون، هزینه‌های واقعی جنگ با ایران را پنهان می‌کند
کلش ریپورت:
🔹
برآورد‌های داخلی دولت ایالات متحده نشان می‌دهند که درگیری جاری با ایران می‌تواند تا ۱۰۰ میلیارد دلار برای مالیات‌دهندگان هزینه داشته باشد، که این رقم بیش از سه برابر آمارهای رسمی اعلام‌شده توسط پنتاگون است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/671396" target="_blank">📅 15:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671395">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
سنتکام: دور حملات علیه ایران امروز به پایان رسید
🔹
فرماندهی مرکزی آمریکا در پیامی در شبکه اجتماعی ایکس اعلام کرد «در جریان این عملیات ۹۰ دقیقه‌ای، مهمات هدایت‌شونده دقیق علیه سامانه‌های دفاع ساحلی و همچنین محل‌های نگهداری و پرتاب موشک‌های کروز در جزیره تنب بزرگ به کار گرفته شد».
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/671395" target="_blank">📅 15:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671394">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
رسانه‌های عراقی: دولت عراق در راستای همسویی با خواسته‌های ایالات متحده، نام حزب‌الله لبنان و سازمان‌های مرتبط با آن را مجدداً در فهرست تحریم‌های خود قرار داده است
🔹
این اقدام پس‌از سفر نخست ‌وزیر عراق به آمریکا صورت گرفته‌است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/671394" target="_blank">📅 15:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671393">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b03649594.mp4?token=UcSaIxspC54T93Mb549i1vSl4CxrffWsObaK7Ej4VE2hkQ3nl2kH1l3CM7fjrgtgWSgBuRehpGeAwlqDnpoFisuSEmlytZkritQTTFvAd12h_5jRHj_V6dvIdkb3ebkSRkwDRVOg4owvqxbYB-onR-2xuARZEXTGB2g1MJ6SpMT4f5nVRI5iJSEO-LhMUbTF5X4yLpxmWSG1ABCx3aYfpt1YjcKtIzsi16vHonnpolq74a0SRcRlHJmwgZeaJPI3h9t4E-D2A2x2w3PHaOe6sNrvRWdzeU2b3rtvw0DnmZAX-LYA33ZhLp2haBOQ26Vfym8NgzsMJNeSeejXJaLeLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b03649594.mp4?token=UcSaIxspC54T93Mb549i1vSl4CxrffWsObaK7Ej4VE2hkQ3nl2kH1l3CM7fjrgtgWSgBuRehpGeAwlqDnpoFisuSEmlytZkritQTTFvAd12h_5jRHj_V6dvIdkb3ebkSRkwDRVOg4owvqxbYB-onR-2xuARZEXTGB2g1MJ6SpMT4f5nVRI5iJSEO-LhMUbTF5X4yLpxmWSG1ABCx3aYfpt1YjcKtIzsi16vHonnpolq74a0SRcRlHJmwgZeaJPI3h9t4E-D2A2x2w3PHaOe6sNrvRWdzeU2b3rtvw0DnmZAX-LYA33ZhLp2haBOQ26Vfym8NgzsMJNeSeejXJaLeLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار آمریکایی: جنگ ایران باعث سقوط ترامپ و حزبش خواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/671393" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671390">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cae589567.mp4?token=vzuqBRMOzrMMczHhajEd8TFVJvF9djrwtMmbyi4AH96twEkMIt0hemGKxpuSaM4mBtjRIX1VFGn6gb-CCLzEfT3oYiNSTNKa69wPGrnmL10m4zey_b2lMg1JgLYnUCtJI3pC96d7PknEuHn9obZloi8J9sbe_7Fw4k9wMCY_wnbJJ1kOjMfiml3gzE6QHlDUMTnc5RJY1leklFbOpdd1nKyYehhKsTa62A4-t1FO64W8TQ43PCy-nxbn4SpRM92fyfqY4VtsTDPbFNPxgV6tLAiXlIKrSEVo8R4DtrHNPRHrbOSbjK0YuZJG3QIX9Sn4xthbN-FY5m4rqBDjwaCXww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cae589567.mp4?token=vzuqBRMOzrMMczHhajEd8TFVJvF9djrwtMmbyi4AH96twEkMIt0hemGKxpuSaM4mBtjRIX1VFGn6gb-CCLzEfT3oYiNSTNKa69wPGrnmL10m4zey_b2lMg1JgLYnUCtJI3pC96d7PknEuHn9obZloi8J9sbe_7Fw4k9wMCY_wnbJJ1kOjMfiml3gzE6QHlDUMTnc5RJY1leklFbOpdd1nKyYehhKsTa62A4-t1FO64W8TQ43PCy-nxbn4SpRM92fyfqY4VtsTDPbFNPxgV6tLAiXlIKrSEVo8R4DtrHNPRHrbOSbjK0YuZJG3QIX9Sn4xthbN-FY5m4rqBDjwaCXww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی‌ ناشی از گرمای شدید ایتالیا را فرا گرفت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/671390" target="_blank">📅 15:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671389">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4872d05318.mp4?token=caGLdfmJrDlvBOh4pqVQs5_HdkJNuqhqN2rpt7TxDrqCTNrqyEu9vIHg7AZLeDIQ9Rd8ve67VqtdBhJkEHZLwV7rR-prHoO4zi-WvhGTsBZURZ0iuRh1smB9M_17fwsJzLbxZygJSRjc2pXt9TDFgtRGg4Z17G7gT7G1WNPFlXKhMUwIum7jiXFBmLw1p5W-RGpIPbGOQbKCKrJdnW7KaSiBNQNq9wZs2NRPLev2VNFtkphqXQMs20GOtavVtr3BYuzQlyOWlFu2DKZHYibjrtfPuZah-vzeHTHUbWQ0VXxFDRYAlFlosBuVo8DAuYZIs4F124Hm2DD3iTPm4audOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4872d05318.mp4?token=caGLdfmJrDlvBOh4pqVQs5_HdkJNuqhqN2rpt7TxDrqCTNrqyEu9vIHg7AZLeDIQ9Rd8ve67VqtdBhJkEHZLwV7rR-prHoO4zi-WvhGTsBZURZ0iuRh1smB9M_17fwsJzLbxZygJSRjc2pXt9TDFgtRGg4Z17G7gT7G1WNPFlXKhMUwIum7jiXFBmLw1p5W-RGpIPbGOQbKCKrJdnW7KaSiBNQNq9wZs2NRPLev2VNFtkphqXQMs20GOtavVtr3BYuzQlyOWlFu2DKZHYibjrtfPuZah-vzeHTHUbWQ0VXxFDRYAlFlosBuVo8DAuYZIs4F124Hm2DD3iTPm4audOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گلدان لاکچری با هزینه ناچیز؛ ایده‌ای خلاقانه که این روزها وایرال شده است
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/671389" target="_blank">📅 15:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671388">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRq640HP-2PpV_4m-f1UnhWybsRH1rz8YRYLFqIkLrUM40a2954VNQVVoErbHA7ts1Z8DGrPTsvodoo-nrxAhFoRIz0ZGudbDeNYhFIpecRfsI9S1qgYqGujq5uJkgXrDxLMskNb2QZcYHrx89RSybcYUU8beV6V4VJhpnzImyVxwszewWZzTwIWpxYneCWPNYyWyVsQfgkw0KItWbZ-KeFxTgFy5jz3Z8UqtYX53-Q1oPmT_Zf2yzBt3eFnzojXNk23yNZFJeNcYfNRWhMsyR3kCpZHzQQvAwD9PzTxZFsBIg15Co7khiMiaHYIhWImy0E2waCXTLKoFi4B7OxVUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
تنها ۱ روز تا پایان مهلت ارسال آثار به سوگواره رسانه‌ای «بدرقه یار» باقی مانده است.
▪️
سوگواره «بدرقه یار» فرصتی برای ثبت و ماندگار کردن روایت‌های مردمی و آثار رسانه‌ای مرتبط با تشییع رهبر شهید انقلاب است. از تمامی هنرمندان، عکاسان، خبرنگاران، فعالان رسانه و تولیدکنندگان محتوا دعوت می‌شود آثار خود را به دبیرخانه این سوگواره ارسال کنند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگوتایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر، مصاحبه
• آثار هوش مصنوعی (پوستر و انیمیشن)
📌
هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش به دبیرخانه سوگواره ارسال کند.
🏆
به برگزیدگان هر بخش، جوایز ارزنده و یادبود
#بدرقه_یار
اهدا خواهد شد.
📅
مهلت نهایی ارسال آثار: ۲۵ تیرماه ۱۴۰۵
📩
لینک ثبت آثار:
https://survey.porsline.ir/s/aU5VZuaW
📨
همچنین می‌توانید آثار خود را از طریق شناسه زیر در تمامی پیام‌رسان‌ها ارسال کنید:
@Badraghe_yar
برای اطلاع از آخرین اخبار و جزئیات سوگواره، کانال رسمی «بدرقه یار» را دنبال کنید
👇
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/671388" target="_blank">📅 15:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671387">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
عراقچی به قطر سفر کرد
🔹
وزیر امور خارجه جمهوری اسلامی ایران به منظور شرکت در مراسم ادای احترام به حمد بن خلیفه آل ثانی امیر سابق قطر به دوحه سفر کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/671387" target="_blank">📅 15:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671386">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
امتحانات نهایی رشته‌های تحصیلی پایه دوازدهم در ۴ استان لغو شد  وزارت آموزش و پرورش:
🔹
بر اساس تصمیم ستاد عالی آزمون‌های این وزارتخانه و با توجه به شرایط خاص کشور در استان‌های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته‌های تحصیلی…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/671386" target="_blank">📅 15:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671385">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_uzVww1ZThEHZ-K_39ifdH_JasFpM9u4McT2nEVBq1h0nCK621jpOkIJnGqJwg2LkGfkg2mioiQTbZg7xev7elghqWFV21tIm4QwlX-DiuzCR1SVPFUTZXCNXOqPV_XyQvnSg89u2QZwQXn3WZytErGvwcyimMpYpMi54RrbDrpDPGQQbIjVjdBw3SC5Kf0V5_5YMo6yGSF5OdwXAVf2owO7Fb0uhqfOMD-ZqM46rwPjoQQNTqh3l4FtwkDEFq0lRsmz10YRJRiZNIH2Lh8v8BuTSfK3IW1YnleAPP_S2xMhRp6DGCQIJB0UFtdI5tty_MyPweGeSM3pOFpXYH7bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا از ضرب سکه طلای جدید یک دلاری با تصویر ترامپ خبر داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/671385" target="_blank">📅 14:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671384">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f4fb22104.mp4?token=QrfxkDjj83waNsX-eDmHo1hckhR53qGxeFQsVYsCR0DnluNC2mPRKe572I7is7sdFwUmcxu6kmPNB9s8hL8G2DYQlatZLPsWML5xymuuprWcxoIX0DhZVMfV1Wsq4ecX48740MroFSZBdTT6AnxkijqBMEzZcVqscHcurNDcg9oW98f_H27OOVLgbjoVMqFlhXEMAMCWuTDvSbgdeYADLqD-SB5cdkqqjb_gFOJmpNiN36m7Ji-8NWBk3pBrnvUxHrrCLwqDhMOE6pv3HrQG8uVVgbWYwntBIxgNWN5IJ0-SlYONoBaeR8tGsH8CId9Uf6VmGKzRz8dxWKMiDkKvcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f4fb22104.mp4?token=QrfxkDjj83waNsX-eDmHo1hckhR53qGxeFQsVYsCR0DnluNC2mPRKe572I7is7sdFwUmcxu6kmPNB9s8hL8G2DYQlatZLPsWML5xymuuprWcxoIX0DhZVMfV1Wsq4ecX48740MroFSZBdTT6AnxkijqBMEzZcVqscHcurNDcg9oW98f_H27OOVLgbjoVMqFlhXEMAMCWuTDvSbgdeYADLqD-SB5cdkqqjb_gFOJmpNiN36m7Ji-8NWBk3pBrnvUxHrrCLwqDhMOE6pv3HrQG8uVVgbWYwntBIxgNWN5IJ0-SlYONoBaeR8tGsH8CId9Uf6VmGKzRz8dxWKMiDkKvcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنگه هرمز همچنان بسته است
🔹
تنگه هرمز همچنان بسته است و در ۲۴ ساعت گذشته دستکم ۲ کشتی با شلیک اخطار نیروی دریایی سپاه متوقف شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/671384" target="_blank">📅 14:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671383">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
سازمان امور مالیاتی:
مالیات خروج از کشور
در سال ۱۴۰۵ برای سفرهای خارجی عادی از
۹۰۰ هزار تومان
در نوبت اول آغاز می‌شود و پرداخت آن به‌صورت الکترونیکی از طریق سامانه‌های تعیین‌شده امکان‌پذیر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/671383" target="_blank">📅 14:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671382">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
زمان اعلام قیمت بلیت پروازهای اربعین مشخص شد
🔹
سازمان هواپیمایی اعلام کرد قیمت نهایی بلیت پروازهای اربعین اوایل هفته آینده اعلام خواهد شد.
🔹
درحالی‌که برخی گمانه‌زنی‌ها از تعیین نرخ ۲۳ تا ۲۵ میلیون تومانی برای بلیت رفت‌وبرگشت پروازهای اربعین امسال حکایت دارد، دبیر ستاد مرکزی اربعین تأکید کرد قیمت‌ها هنوز نهایی نشده و جلسات تعیین نرخ همچنان درحال برگزاری است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/671382" target="_blank">📅 14:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671381">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/614c0b0bbd.mp4?token=CU0fIXs8kjgpt30QHIj8ghnyxMnfwCBaSbEiQC0f2udZaM4r5Fs3bbNz6mS4aj3QzPWZwLytjD1ViIvx7rgx3s2__f5sBK8olmllvLEKeGDu8Ejjiq73QnRIxIigAJhnTNv7eUnC65BS28UZD2Aimnf1ZRzdqGo0f908uuizf9JWwtpBPZUAoU-hJXN9Dh4f7umVAiziiAkRYBNzy6ku3RuEeUxosWXhMygBGWN7A5JAXyThX_xOkY4UZ3OjnHaBR0ml5FLPfDaIgzTeHVpO3UoYO9oNZa-oV5Vjk-4wlWq24bzsgAcGpTsdRBlfUNPlTNflcfh9V6LidqviJ9g0Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/614c0b0bbd.mp4?token=CU0fIXs8kjgpt30QHIj8ghnyxMnfwCBaSbEiQC0f2udZaM4r5Fs3bbNz6mS4aj3QzPWZwLytjD1ViIvx7rgx3s2__f5sBK8olmllvLEKeGDu8Ejjiq73QnRIxIigAJhnTNv7eUnC65BS28UZD2Aimnf1ZRzdqGo0f908uuizf9JWwtpBPZUAoU-hJXN9Dh4f7umVAiziiAkRYBNzy6ku3RuEeUxosWXhMygBGWN7A5JAXyThX_xOkY4UZ3OjnHaBR0ml5FLPfDaIgzTeHVpO3UoYO9oNZa-oV5Vjk-4wlWq24bzsgAcGpTsdRBlfUNPlTNflcfh9V6LidqviJ9g0Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان شدید در آلمان؛ خسارات گسترده و اختلال در پروازها
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/671381" target="_blank">📅 14:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671380">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f37729ca78.mp4?token=rNWH9jaJNcwpRlVcvUNxyqx5V-E0SJMNvCXSWju3yLi__Wh0HbNpOZyTo8xx6Rh6tPniFfaEJOVnBLx_633lcVbnkplfimtZjLIj5Y5EoxNjxyuigvTS0uF7OGuylrvdtviLa1xF3MyzrVTuSpLw6DNYQnAO3cJa3Dnu6j9eeoejU4vn1X9HBhd9vPzMyAGN9sJLantlkh_UNBkzZ4oaym8RD2XmBqkMSTiWglOOnQRAeug6P-ixk7JGiY8cxXZfGn1JH90xtjVuPx1_h66jr6neYKh8soWUjU-0kU6sGBa9BKyMd9pTq6t0jcNMGxracxaiq4uclTq68k7OPedzznskaeLIudHQdAeqCPlrGYJIWBJEPmHqLxpsqrtO_gyQWsbWZQqjvrRh6XGf4_XjYiMMcLBAHMR1klVBhutpEIjiyIBtDQZMMCpThfufNdmA13WWydeFyH2qxIDVlqMxyjAfMgHsEbD_waLlOcUDw2JkMC59qJ8rM5T_KLtfFN6MNarPxf6hd2-oKHi1PwRXffNCVyCr9EugRWuidpjA0dhF-Ud5x_dl7heStPmZ3oVtD49Bf8yZBUgeq-FQbrdjxarM9oPWHtV4-ZEb3Uj73n9oK_QxjE5exf23YfOCKtJXJf6Aa0gtZlxAjagzhOV43sloHWAnlRwBqpSpONL4AhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f37729ca78.mp4?token=rNWH9jaJNcwpRlVcvUNxyqx5V-E0SJMNvCXSWju3yLi__Wh0HbNpOZyTo8xx6Rh6tPniFfaEJOVnBLx_633lcVbnkplfimtZjLIj5Y5EoxNjxyuigvTS0uF7OGuylrvdtviLa1xF3MyzrVTuSpLw6DNYQnAO3cJa3Dnu6j9eeoejU4vn1X9HBhd9vPzMyAGN9sJLantlkh_UNBkzZ4oaym8RD2XmBqkMSTiWglOOnQRAeug6P-ixk7JGiY8cxXZfGn1JH90xtjVuPx1_h66jr6neYKh8soWUjU-0kU6sGBa9BKyMd9pTq6t0jcNMGxracxaiq4uclTq68k7OPedzznskaeLIudHQdAeqCPlrGYJIWBJEPmHqLxpsqrtO_gyQWsbWZQqjvrRh6XGf4_XjYiMMcLBAHMR1klVBhutpEIjiyIBtDQZMMCpThfufNdmA13WWydeFyH2qxIDVlqMxyjAfMgHsEbD_waLlOcUDw2JkMC59qJ8rM5T_KLtfFN6MNarPxf6hd2-oKHi1PwRXffNCVyCr9EugRWuidpjA0dhF-Ud5x_dl7heStPmZ3oVtD49Bf8yZBUgeq-FQbrdjxarM9oPWHtV4-ZEb3Uj73n9oK_QxjE5exf23YfOCKtJXJf6Aa0gtZlxAjagzhOV43sloHWAnlRwBqpSpONL4AhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجاب استایل‌ها دین‌فروشی می‌کنند/ با هزار قلم آرایش و عشوه و ناز ضربه بزرگی به بدنهٔ مذهبی ما می‌زنند!/
تلویزیون اینترنتی مدار
این گفت‌وگو را در آپارات ببینید
👇
▫️
https://aparat.com/v/qypc186
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/671380" target="_blank">📅 14:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671379">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCinjjNgG1CTbsjah3Akvvo51P5kAe0cbllI-_SWySDPWWOToNguGyKeT7uJwGMz34Bv7bTJBCEw8ScekI7vUQD44y8W2SDKfY7fMgP3LWtO7OIf5QhPq-17sC4fXyOn16sRnQtjGCx4KPuM4H-QTBOewvTKGbqp9afgDmJQoUVCFqs3zlz-WL3GipIdybwlhM3i4G3UCNLfyfsOrqB6yjYASbvKn5ZaFMjUT53PAGLD6lDHBrVk3zalGJkj4bYITw_gqkNx37FBA6md8IVJDFANuHbwlgFHF_rWq5pjof1rz1-nOz5ijobMemPx-U8oQrN8u3ttJ9A3qNhj-yr3Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شال مناسب هر رنگ لباس؛ این ترکیب‌ها استایل‌تان را چند برابر جذاب می‌کند
😍
#فوری_استایل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/671379" target="_blank">📅 14:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671377">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ادعای اکسیوس: خوک هار جلسه‌ای در روز سه‌شنبه در «اتاق وضعیت» کاخ سفید برگزار کرد تا درباره یک تهاجم گسترده در ایران بحث کند
🔹
منابع می‌گوید که این حملات، دامنه‌ای فراتر از تهاجم‌های کنونی در اطراف تنگه هرمز خواهند داشت/ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/671377" target="_blank">📅 14:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671376">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
دامنه
t.me
تلگرام به وضعیت عادی بازگشت/ علت تعلیق و واکنش پاول دورف
🔹
دامنه کوتاه و پرکاربرد تلگرام با آدرس
t.me
که برای هدایت مستقیم کاربران به گروه‌ها و کانال‌های عمومی استفاده می‌شود، پس از یک روز تعلیق و قطع دسترسی در سراسر جهان، بار دیگر به وضعیت عادی بازگشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/671376" target="_blank">📅 14:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671373">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a0-_4Y7VDfGZaO3aHhHJ3xmA2fww3XxT5mUl9Mch0Umgi_SOV6o1B-pjgOnpIQDeqZV2cA6na5RYSg_c5XdwgGHCCJPGt3En-GkK0pysLV7X7H6Mc8zhD1KUwNxPe7ASYs5plUQHSTriT_ZU4i-tAzFR_rbpFg4Bwdi1lggwInUzi-5kjtkYfJuuXEMP3_TD7depmBn8nCZkFOB8-MLJoenmBhniRnftIgSiNNU_MoT02zzSll-j0_Yp3fELy1XklPXy1RJET1xr9BPU5l5dmZVAD64LfsagWLk5eM5KCB9x14evx0W4JrN7hSdENKa53uD9bzjchsYhGQWCsL0hRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3Jgp4NHT6jR7SPlADT90iwXvllwpZxcEdyasRPctbVsE_Rbx-sK2F0tN8yDLScOlHm6ymCyT3lcWRH4VeTA2EjblnCbJHZYmhOroyTMfSNfxMGlNmd80Geq0NmLoZg1mKoztwRNMEsbXmNrO_YwX2ZikH3cWyvTiBwMcy3JWOmpqkSx_XKGnHGTTkJEowOI25SymBnVyEEMjJcs86TrhsQTIFi78FjfrsmYCGmwLp7y9MLLXWejslwNcVTcLQbxLQC3XcU5j0Xb8RnxrasIJotBzSAEmkvP4wwPVQYBA1fMwoYXQlLVJph0NBVNAhR00qLxTJAB6G9_vFzEC1_x2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BcNMNx1a4pw3T09mCbAtm305DIHOkTkcT7kIm0m6qMYRo8s492vyCNda3be_bxsFBwOzuH2f7UIFbPuyhuLQjGt_7mhgnsqexiE2O6cRPiRZAz6MLvtc4sn6bnf1yc_J9kzjZSgU2xbbHoQmU0ZdRIlu0BPtEqnwpAJu3IJm6tF3-ptACIqJXXJr60zWzxojfSTd3PXuHJ_e_0bvqsLseeLYE7upY_rEGKLw4vdNS_0oBHgh0VNRNx7-qKWcby5N9klej4IVZD7gPBCH31pgr-IVpoRRkqyGGkJ98ncXmV2gbt5HTy5FNyzhMzdK8XZJygrch61KtuJlEtIwhVj-BQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر ماهواره‌ای جدید از حملات ایران به پایگاه آمریکا در اردن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/671373" target="_blank">📅 14:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671372">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea1443322f.mp4?token=pHORpOk4JVg8UgaVVot2Q0QAhCymKGDwGeFeMcv_8y84mb8IWUGyCpwm_9OBQddHP7KmDxcyppI4qm40kXtl2kx8L7qMO_-3zjJQCYAC2ltfwG2Bmcvhivwkw3mjyYpk6Y1uyPMnF5wwJf0cyKeOgvhRsrrTh5CEkqp0qdNiIF2-5XNByp6KR1BGUSc3Ges3peTc1Eyu677gEzN2kfa1GB76LQwV2NiQFC-M8a9Q4Ruk5eVaHtqJq4nUvafFH_TTG7OU7qHHa--pAPyok7O5MwDLkSJBHataJo2gH9cEMpPlJTdMBUcsBPW8PBHBn2KFE5h0j9JCAQZsY2jTESFLgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea1443322f.mp4?token=pHORpOk4JVg8UgaVVot2Q0QAhCymKGDwGeFeMcv_8y84mb8IWUGyCpwm_9OBQddHP7KmDxcyppI4qm40kXtl2kx8L7qMO_-3zjJQCYAC2ltfwG2Bmcvhivwkw3mjyYpk6Y1uyPMnF5wwJf0cyKeOgvhRsrrTh5CEkqp0qdNiIF2-5XNByp6KR1BGUSc3Ges3peTc1Eyu677gEzN2kfa1GB76LQwV2NiQFC-M8a9Q4Ruk5eVaHtqJq4nUvafFH_TTG7OU7qHHa--pAPyok7O5MwDLkSJBHataJo2gH9cEMpPlJTdMBUcsBPW8PBHBn2KFE5h0j9JCAQZsY2jTESFLgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین تصاویر دوربین بسته از جنایتکاری که امروز صبح به دار مجازات آویخته شد
🔹
از لیدری اغتشاگران و فیلمبرداری برای رسانه‌های صهیونی آمریکایی تا  آتش زدن کلانتری شهرستان دهاقان در کوتای ۱۸ و ۱۹ دیماه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/671372" target="_blank">📅 14:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671371">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
نیروی زمینی ارتش: در تجاوز‌ دیشب ارتش تروریستی آمریکا به پادگانی در بمپور ایرانشهر ۱۳ تن از کارکنان مجروح شدند و تحت درمان هستند  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/671371" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671370">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTpeLGTbs5juPPUE5rRF09Z52EQQypDsQoor52koq3SjsfblkiV9dIyZyKjuKnDv9kKsSFMp1X30WKB_MYytVmnwo0jS5SIZzXcrtX6Set-pLSIM5VPX-HacZBoo5Vk1dtZFw2dLPiQ-sRxw5cewh5IuI3DSOeRl0_v0rkHPBHsxFHrOEQF4XCJT7f7xXW3OVV-6NZ0dZiwmYmHPknVphfWv81M3pl8p9wo7CiygHwWOZLGfTkVZguYD02-_9AMOl2YYaZupmVoiDV2b9a0tP9U8XwiIUI2cho_7iRBdTTFA2V11OG8qQEhBOqPpjQs0x9KEpqAjGWWDvlHMqM8p1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسم جنس پارچه‌ها واقعا جالب و زیبا
هستند
🪡
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/671370" target="_blank">📅 14:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671369">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
تیزر قسمت دوم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای داوود سلیمانی که به دلیل تصادف  شدید، ۲ ماه در کما به سر برده و جامعه پزشکی بارها از بازگشت ایشان ناامید می‌شوند و روح ایشان در برزخ ازدواج کرده و تشکیل خانواده می‌دهد، ولی بالاخره در روز ولادت امام رضا(ع) از کما خارج و به زندگی دنیایی باز می‌گردد را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: داوود سلیمانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/671369" target="_blank">📅 14:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671368">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IojIUNruKxtjHCFwc1KDbM226aZGyc-5iOCR3uYeVv_uJsjaODhxvDZPAk3d_8uI55OeQxwly8Qp_4AnZH6ad6fNEuW5pAZXSScZ_uyz8Mmx_PZPx3h9YdvWgIi_nrvIwk77hZHzTQOPtEIb4PV8JqeGw1N11MSMcnJJOEkVXqVkR_M479N3QHfvqnxuD1g_o2Ejxk6E-PTPZ5mfQn3NCq_9aeG7vPL_TjAip-BjxVZCdGFXp7fiq_Z930hWHAyAmlf3pPeeCM9qzzpEm1EFFm-Yl6jtpzoZJ6FJ18wBQv7o43sA8_aL7Ncpd45tgDVkT7MOF4wEyREyRoTV5wG1Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکونومیست: ترامپ برای بازگشایی تنگه هرمز گزینه‌ای جز بازگشت به تفاهم‌نامه ندارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/671368" target="_blank">📅 14:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671366">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
امتحانات نهایی رشته‌های تحصیلی پایه دوازدهم در ۴ استان لغو شد
وزارت آموزش و پرورش:
🔹
بر اساس تصمیم ستاد عالی آزمون‌های این وزارتخانه و با توجه به شرایط خاص کشور در استان‌های
هرمزگان
،
بوشهر
،
خوزستان
و
سیستان و بلوچستان
، امتحانات نهایی تمامی رشته‌های تحصیلی پایه دوازدهم در روز پنجشنبه ۲۵ تیر و شنبه ۲۷ تیر لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/671366" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671365">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c58836f04.mp4?token=nLD0Pq505l2T8VUFC9BYN1f8Xrm51ANOdPrGNQw3mDIeTTjDmgfcnI4gYrWVsUDOZvPDiYePYzDxxNVIOZCCQWta6KixPE_OPdC7UPEXufETVHjHDUlLLFoPxvcemLtVShEfbJkU2i5BYFRls6Yeai17nBY0PbAQtm4IVK5W6jE02IetlEefbB8JABHSHTvWpz7gXovsrg3oGdw-HxZBgpo2_eymBnwtKX6-GnqmevaPURAFCb89NXt6llwWQnFzqvexbE-oBPE6_Iycwo73_av7XiewbQ-InmSxlUrVWIYA1NLHNQIp9a0v6ZyrV-25gBhcl7tSy_SoYc5rKXGinA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c58836f04.mp4?token=nLD0Pq505l2T8VUFC9BYN1f8Xrm51ANOdPrGNQw3mDIeTTjDmgfcnI4gYrWVsUDOZvPDiYePYzDxxNVIOZCCQWta6KixPE_OPdC7UPEXufETVHjHDUlLLFoPxvcemLtVShEfbJkU2i5BYFRls6Yeai17nBY0PbAQtm4IVK5W6jE02IetlEefbB8JABHSHTvWpz7gXovsrg3oGdw-HxZBgpo2_eymBnwtKX6-GnqmevaPURAFCb89NXt6llwWQnFzqvexbE-oBPE6_Iycwo73_av7XiewbQ-InmSxlUrVWIYA1NLHNQIp9a0v6ZyrV-25gBhcl7tSy_SoYc5rKXGinA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش خوک زرد به پرسش درباره کشتار دانش‌آموزان میناب
🔹
مجری: آیا متعهد به انتشار یافته‌ها خواهید شد؟
🔹
ترامپ: فکر نمی‌کنم کسی بتواند بگوید آنجا چه اتفاقی افتاده است. در حالی که چنین اتفاقاتی در جنگ رخ می‌دهد، موشک‌ها در همه جا پرواز می‌کردند. و نمی‌دانم چطور کسی می‌تواند بگوید که ما آن را شلیک کردیم.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/671365" target="_blank">📅 13:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671363">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/692f9b40d5.mp4?token=VHJd-bviYCTVaW8x_l1JO45RkoYY6dIfek6pPdDhU-Z7OFfqAM2MmXmh7y7387MVM1c6VUJ7_BfCn0tl_nn7tq9fZlX9VCGJdr9doLSou_5vsgBJ60zgRNFxUhf_0VOTj6EboD2Wa4PXrib8FekEk-Y0a_x4gF_FZfDQdnCLAGELDBeDX7OtQw6ZIjF2eFSa_lv_NqCCFaEMZKXw-xT1cfdpvvShiBlAmJlJOCT32vIvDQg-EiJQsQemunj3gQsOAwMUejpVK_nH_sNWz4-i4M2RW-Od-avyjHQKPwapwrWtCbkBv3mD_SJGZ2xKu8htVubsxhQUKjdf5QlRtDLk-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/692f9b40d5.mp4?token=VHJd-bviYCTVaW8x_l1JO45RkoYY6dIfek6pPdDhU-Z7OFfqAM2MmXmh7y7387MVM1c6VUJ7_BfCn0tl_nn7tq9fZlX9VCGJdr9doLSou_5vsgBJ60zgRNFxUhf_0VOTj6EboD2Wa4PXrib8FekEk-Y0a_x4gF_FZfDQdnCLAGELDBeDX7OtQw6ZIjF2eFSa_lv_NqCCFaEMZKXw-xT1cfdpvvShiBlAmJlJOCT32vIvDQg-EiJQsQemunj3gQsOAwMUejpVK_nH_sNWz4-i4M2RW-Od-avyjHQKPwapwrWtCbkBv3mD_SJGZ2xKu8htVubsxhQUKjdf5QlRtDLk-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش اینستاگرامی محسن چاوشی به جنایت وحشیانه آمریکا در جنوب ایران
محسن چاوشی:
🔹
جنوب خون من است که می‌ریزد. به یاد جای خالی مردانی که دیگر  باز نمی‌گردند⁩.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/671363" target="_blank">📅 13:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671362">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
منبع آگاه وزارت اقتصاد: اخبار منتشرشده درباره تغییرات در شبکه بانکی صحت ندارد و هیچ تصمیمی در این زمینه اتخاذ نشده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/671362" target="_blank">📅 13:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671359">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
آیت الله اعرافی: تفاهم‌نامه تمام شد؛ مذاکرات را ادامه ندهید
🔹
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
🔹
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/671359" target="_blank">📅 13:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671358">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
خونخواهی، طرح حاکمیت تنگه هرمز و اصلاح برنامه هفتم، اولویت مجلس است
عباس گودرزی، سخنگوی هیأت رئیسه مجلس:
🔹
اولویت مجلس بعد از رسیدگی به خونخواهی رهبری شهید، طرح حاکمیت ایران بر تنگه هرمز و اصلاح برنامه هفتم است.
🔹
برخی از اصلاحات در قانون بودجه ۱۴۰۵، برخی از طرح‌ها و لوایحی که نیمه‌تمام ماند یا توسط همکاران امضا جمع‌آوری شد، در نوبت اعلام وصول و یا بررسی در صحن مجلس هستند.
🔹
تعداد قابل توجهی طرح توسط همکاران در ارتباط با مسائل معیشتی، اقتصادی، کارگری، بیمه‌ای، رانندگان و مهریه، در دستور کار است که در اولین فرصت باید به آن‌ها رسیدگی شود./ خبرفردا
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/671358" target="_blank">📅 13:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671357">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/691ec6572b.mp4?token=Ge49x7haPQPtCI80CapBd-spLM0PWZAobNdVWrEmFKGRy5XY8p-ctXauLeAbv9ahOx4SgmDlqWyQkJePbj347RTgK0mSPH8PhVtuS2GeAH3j1i6oCBca0IUqc2-_RQ4_NhNxiHrBZgG8r4ohymFij3uv9rDxxH3c2-GNwn1dZsGCU9-arSDIYPaYzQf3OUZtKG67zzUkSA6bdjjrGoodrjdLWkFoiR0nN_QJ1QBkdFFq6XKaWnl_F_S-BQLEag8_zoCn3TLA_zkh7eyizuni-m45qMc6y3Byd7SpZ55IvkCCV4b_mh4HLUhYtIakwE9b-6rr7qOUMkJmVWMn9eDRww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/691ec6572b.mp4?token=Ge49x7haPQPtCI80CapBd-spLM0PWZAobNdVWrEmFKGRy5XY8p-ctXauLeAbv9ahOx4SgmDlqWyQkJePbj347RTgK0mSPH8PhVtuS2GeAH3j1i6oCBca0IUqc2-_RQ4_NhNxiHrBZgG8r4ohymFij3uv9rDxxH3c2-GNwn1dZsGCU9-arSDIYPaYzQf3OUZtKG67zzUkSA6bdjjrGoodrjdLWkFoiR0nN_QJ1QBkdFFq6XKaWnl_F_S-BQLEag8_zoCn3TLA_zkh7eyizuni-m45qMc6y3Byd7SpZ55IvkCCV4b_mh4HLUhYtIakwE9b-6rr7qOUMkJmVWMn9eDRww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر لحظه شلیک موشک های خیبرشکن، ذوالفقار و فاتح ۱۱۰ در موج‌های سوم تا هفتم عملیات نصر۲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/671357" target="_blank">📅 13:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671351">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5kWOVQRutFSfWY07DxKtET-crW0zr912mpCHin5Vrf1l2rVYVB_K3mpnyqZNM47H2Pz6iUnh13gGn3LRa7MnwZyVCZl8HKhI1U_Kl6_zHAB_5cQ6uj47rKu994S-va0hsz3EvksZgfvDadfFDMbbRuZOuUN2Qz41hcJYqxcn-YC0PSXTunXPUe6Noijr-jdSYe0nW8HffXUuLEqE4Lwdb0VVSkIL-wIjzxgNbxnNuSWOnlcn46ohP9RPmdlqZJYInrBmFvks5Q0jSG_0uYENWn1FK4WUrCQUuG-l1WiWoCVPS4MnoMayseV9U196XTH1mAFig9DjSXSkgZ9iRhNuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHcykeZZ4tUFItBuKxzCqFd8sLarNUz1VnJ2RZ1qKtUtChg1Zz1UDOHJtdfybKpQC8Je2LIffjPZxoPfhXCasAdi5wES3T1gONUtzDx0nqLFrqB6CvLBhQZJVpekF2oew_UaATYvOYG7a6fv20nbO3dOSm61KfXKXQEJG2_r8LeiAthit-cM4H7aADRu5eecmRll_qTwRF5CUmJhfGmCfimvQCgzA9v4l_YFUjDwSqZi-s7ZCu2MBuWYyCRtevsg6wcF89ETtLJeat88z36bBbwU-TVn1h3gTw25zmgWLhJuwx5B2l30B-2av-piliHq10OUr8EZv-Aap9R5vwmjvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D8p6FbUHwufQ_Ao5VolVSB2eI5_FpyZTJmM3hmYgCCvIX-f-ENUHgTSG3cfmMBGkwSZxUPbBhH7DGmv1duVdI6iaCwbC7eXbPrZ9bKZ7wnbV4cIcPBcTdiriCLQkNnzEs_Bv3eAhNUhdTJUBEX6qlvbumLA9CamzaKxye7lcQfEq4XrFw8I_wNiNXziH89aULrUhJOlf6UPG2cONexIsMFRYoAXZmclTYRD3bq9-d_dKwz-HtoUHgmx5N2a-0e14nAfawp5HvtOqLqgaemoY0CfduN5BOGcVjC2TVUNtx6-X4S703MlCGt5enKgVItmedHI4X_EuxX0t2eOz5TbAcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gJaORypUdaX-x_1ivETu880TFb0p5GAo-6O7f_m40zuERkDSX84ZLGgYpgCA_mmCltDzL-_HS3dMMhrOQpzo0w5iuv1Hdv549vXwZK6o_isO6WJlgexmoY9OM25cH8IXivk6ttWE7p_0tb02QjhmEteUMWiv2PTpgN2lw_gDqtqNq4ORhzdBuRLfBWormkxiZVsz7eSL1EZYym1Et1z8KxFiweIsxNR4yAE0RIiQcI76bavXppU-xZa_oMuF7t6_DomzP6KQlcY72fVQCbqUE-rpuhs0HS1KNmZcSIXplstUJMSAUEUFXMzCRZPhRSXi_boN_0LmBd14AgczoZ1edg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/le1_8Uig97nqZgzNH8Ew132Zh9OLqv--h9of_e-bSPnrp99nDu3HpNvgq7U9er6yLdS0t4nd4HbTJua7ET22SCbxIl2UcAuggEoHrT1fmTkr-wA9ryoHgDqHlZYTvpUlw_KAJCqMhH70wyj1S20rmgLqD1gfiCi37ZGp2wyL1x52WQMSYriIodpkbFn0tCNHUwBw4807vpROUL1wrn3azUFxcRZquFJWdx7QnUYYaXs8bJZJaikQtfX5Sc9IgioeRgl8It1lQTn2K5Pl7MwEwh-OdV9u9c3lMy5uycaV7zJotfc-rLYN6z3mj29oae38K5SOemq4t6KHky81HwchMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W_xa7q5TYzpufi22LIGurTtXQiP2EjPw6nmDSZbVer3VbMbyEpthDYpbYZO6Df3rGaV1ZwXt07gTblD8ojjx90sGrHJu7CDKfOzchonS-JQA9vT0aw998UdHr50AJ_ywicq4g5XXGrhf0FKGkEa826hzm4IqqC9v1rfIni4ucUmHo6unFNfx2oc-3GHnZ04VI2vpKinbPH_ysg6pxMuOzv6UCvQ2aSbW4cW8AZwwlxhg9ts8qaIA-whIb-UyBhT-ZtUMsi6naCWe1wcXlyzUeSVpBJ2uka4-YXkr-WjoJ6zKGg4DmlGMqSaDciCp7OjhoWSOjxgSI0aiCjfqDmxV7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شش دستور قهوه سرد محبوب که حتمأ باید امتحان کنید
😋
☕️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/671351" target="_blank">📅 13:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671350">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laagSd3piz7QCD3hlwFVnK5CBeKY2ainNxKT6VMSfNZlC8G0KgwXIN7VRkjaHW86vxAh_9vEIdJI6EfQcYrFnXw56Pno0553-h6wGPTPNW3NqsV1aebrZtiYQbsjCX9YhU6WUEyqnreslPtYIPM_U2_ASM6MTYf7TpGN8gx7wdFPa9ntQvFM5wKRtpCP_B7rqA0GNjTB-JxrXQZzFYfupe9Nv0RlzB9oHr2sc4Fy8J-Jlmv2CW9BRNTbMfWj-izB2jg_1JhYsf6maHu6FnDWGqQUEItnU7i5gar65CEFKmZk40h83RnTU-rBXmj4lUn4XyM39487e6d3YdNB4b19Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۴ تیر ۱۴۰۵؛ ساعت ۱۲:۳۵
🔹
امروز بازار ارز، طلا و سکه نوسان‌های متفاوتی را تجربه کرد؛ ارز کاهش یافت اما طلا و سکه تحت تأثیر تشدید تنش‌های سیاسی و نظامی ایران و آمریکا و افزایش تقاضا برای دارایی‌های امن، صعودی شدند./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/671350" target="_blank">📅 13:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671348">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f43adc06f.mp4?token=t7RzNq6SQ2o5qxqg9akzs0OhN4PYI4YNGdcVJYVXJIQV9pO47E6yXNt3d0xlrK8iKD1-FH3jCMS3TiY0aNkI4mwAFMp61E6QU-TWEp71xznIJ3muwAVnVJB1w3kzojX9UFolmbJZT8OzZ5vd5AIpsJ35B_B_aMCx1PmMZc2IrQXuC2EjTgRBvrw-E3vdKW3p_N0C2Fl65tLM376ibpo06bcUjgLRKP59t4H1dlQpgd80R2icGGmIWUpsnW-fBlaEo2rVXGnP9O8A1VVUAds3Dq3kf625i1h4vx4XPVVvzCLysHZHbfpX0hPF2UIwX-rUlRtjMxFWcd-6B3HiWSNBsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f43adc06f.mp4?token=t7RzNq6SQ2o5qxqg9akzs0OhN4PYI4YNGdcVJYVXJIQV9pO47E6yXNt3d0xlrK8iKD1-FH3jCMS3TiY0aNkI4mwAFMp61E6QU-TWEp71xznIJ3muwAVnVJB1w3kzojX9UFolmbJZT8OzZ5vd5AIpsJ35B_B_aMCx1PmMZc2IrQXuC2EjTgRBvrw-E3vdKW3p_N0C2Fl65tLM376ibpo06bcUjgLRKP59t4H1dlQpgd80R2icGGmIWUpsnW-fBlaEo2rVXGnP9O8A1VVUAds3Dq3kf625i1h4vx4XPVVvzCLysHZHbfpX0hPF2UIwX-rUlRtjMxFWcd-6B3HiWSNBsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی‌های گسترده، آسمان شرق کانادا را نارنجی‌ کرد
🔥
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/671348" target="_blank">📅 12:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671346">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یک کارشناس انرژی: بهانه جنگ برای قطعی برق به لحاظ علمی پذیرفتنی نیست و این مشکل حداقل از ۱۰ سال پیش قابل پیش‌بینی بود
هاشم اورعی، کارشناس انرژی در
#گفتگو
با خبرفوری:
🔹
با وجود وعده‌های سال گذشته وزارت نیرو مبنی بر عدم قطع برق صنایع، از دیروز بار دیگر خاموشی دو روز در هفته برای صنایع مولد اعمال شده است.
🔹
استیضاح وزیر نیرو به دلیل رایزنی با نمایندگان و پذیرش خواسته‌های آنان چه حق و چه ناحق برای پس گرفتن امضاها، به نتیجه نرسید و به جای تمرکز بر حل بحران برق، مسائل سیاسی در اولویت قرار گرفت.
🔹
همچنین نسبت دادن خاموشی‌ها به جنگ از نظر کارشناسی قابل قبول نیست، زیرا بحران برق سال‌هاست قابل پیش‌بینی بوده و ادعای کاهش ۴۲۰۰ مگاواتی تولید نیز با توجه به کاهش همزمان مصرف صنایع آسیب‌دیده، توجیه‌کننده تداوم کمبود برق نیست.
@TV_Fori</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/671346" target="_blank">📅 12:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671344">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bdab62a3e.mp4?token=OGI3zY0QM1C9ZZuSa6zyeXC88SDT4i5aCvNyj9cPiIeBRN84r30IsovTI96PlWHOBMA14fW0B-jZnZlCeSkrc_gtMitZmwzEuh8UgZR7jdDSaRYlBrWsoKAGcHk4kHFOD1-fi6E2IndfSHZZ9pUVqwJcMWFKegZNuVNxEYGTGdgbsrCrz11yB5eeZ__foCqvaOjzuYVb1lutkMepW8Z4VQ9V0mnfpOs80SiQanZrrv3DmGi0aNMUepbEiB5-yvD3QwxS0Qqa0-OXJaTuIJ-H_t8Cgi_utNGr-ePbBNrNu3_0srtLedKLTgkf9qxaEOp5JpxhRFH8EpPWkNqgmUnYvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bdab62a3e.mp4?token=OGI3zY0QM1C9ZZuSa6zyeXC88SDT4i5aCvNyj9cPiIeBRN84r30IsovTI96PlWHOBMA14fW0B-jZnZlCeSkrc_gtMitZmwzEuh8UgZR7jdDSaRYlBrWsoKAGcHk4kHFOD1-fi6E2IndfSHZZ9pUVqwJcMWFKegZNuVNxEYGTGdgbsrCrz11yB5eeZ__foCqvaOjzuYVb1lutkMepW8Z4VQ9V0mnfpOs80SiQanZrrv3DmGi0aNMUepbEiB5-yvD3QwxS0Qqa0-OXJaTuIJ-H_t8Cgi_utNGr-ePbBNrNu3_0srtLedKLTgkf9qxaEOp5JpxhRFH8EpPWkNqgmUnYvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از خسارات وارده بر اثر حملات ایران در روزهای اخیر به پایگاه‌های ارتش آمریکا در منطقه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/671344" target="_blank">📅 12:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671341">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bfd6c5c54.mp4?token=hrZdj-fX8ighKlOCYddZRWQ80dWJI5RAagg62hBU0NgjIvd0movtmpVOU7oC7dAigdOzFHHJ1FBlumrG98TKVlYKYVNKefulVXPW8a-iD3nGeWTam_UlhqpH3Lz6gBriN2eY6I2mytIw6KWhuxSAFnXgJNYrjLmFRYSbaGlj0AmzDMzNhVP7G3ZGN7z3vTGtuSB7xlYKIzQfWahN2w7oMCh6vQbcL0yVCO1UGRzzoXSVcYJ51AjitdDt6CT_zOgvCw7lWyYFBPCnKGDhHQYT8qH-uyO2gLsIBN88L-CI5nYW2QXUcpMqrQNfhu1StUnVJgYdwJerGjvco7N4k8UDww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bfd6c5c54.mp4?token=hrZdj-fX8ighKlOCYddZRWQ80dWJI5RAagg62hBU0NgjIvd0movtmpVOU7oC7dAigdOzFHHJ1FBlumrG98TKVlYKYVNKefulVXPW8a-iD3nGeWTam_UlhqpH3Lz6gBriN2eY6I2mytIw6KWhuxSAFnXgJNYrjLmFRYSbaGlj0AmzDMzNhVP7G3ZGN7z3vTGtuSB7xlYKIzQfWahN2w7oMCh6vQbcL0yVCO1UGRzzoXSVcYJ51AjitdDt6CT_zOgvCw7lWyYFBPCnKGDhHQYT8qH-uyO2gLsIBN88L-CI5nYW2QXUcpMqrQNfhu1StUnVJgYdwJerGjvco7N4k8UDww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در تاریخ بنویسید؛ جنوب فقط یک جغرافیا نیست، جنوب نام صبوری این سرزمین است که بی هیاهو سالهاست ایستاده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/671341" target="_blank">📅 12:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671340">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
شهادت ۷ نفر از کارکنان پایور و وظیفه نیروی زمینی ارتش در بمپور
🔹
ارتش: پاسخ تجاوز ارتش تروریستی آمریکا به ایرانشهر را خواهیم داد.   #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/671340" target="_blank">📅 12:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671338">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
مسدودسازی ۱۳۰ میلیون دلار دارایی رمزارزی ایران توسط آمریکا
🔹
وزارت خزانه‌داری آمریکا ۱۳۰ میلیون دلار تتر متعلق به بانک مرکزی ایران را مسدود کرد؛ مجموع دارایی‌های مسدودشده منتسب به ایران توسط شرکت تتر از مارس ۲۰۲۵ به یک میلیارد دلار رسیده است./ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/671338" target="_blank">📅 12:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671337">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1f21ab0c.mp4?token=qbwOfXsnEzoxc6x69J8hAlWAnqfZNxpImIiSILKbNwh5xeg4dHrYqIK1rUwWC9MCkRrttmJ4Hb-hvUvrn0sZ45_qlwwVhLLBeE43zKS8ZYIHBw1rNxqQP94Fw62JO1wcqakFlD7mK2uLqvv8z1Pk7BImw1YMmh9Qb0-V4jry5YsT6b9AXLeCLixfgOpMmuYDVAopu2x7mfUDPeW2oIB0HTuWP5ZuZAdcoVpw4GydynrDplAxfylPhYxUVOay31QTCCw-ZoGszGHdi1Uop9Impy-WAn7iBI7ldosJtUQy309sX-5OVFVFLd4Inzqgzxj9ON0IazRWPqjiZrFcUeAfoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1f21ab0c.mp4?token=qbwOfXsnEzoxc6x69J8hAlWAnqfZNxpImIiSILKbNwh5xeg4dHrYqIK1rUwWC9MCkRrttmJ4Hb-hvUvrn0sZ45_qlwwVhLLBeE43zKS8ZYIHBw1rNxqQP94Fw62JO1wcqakFlD7mK2uLqvv8z1Pk7BImw1YMmh9Qb0-V4jry5YsT6b9AXLeCLixfgOpMmuYDVAopu2x7mfUDPeW2oIB0HTuWP5ZuZAdcoVpw4GydynrDplAxfylPhYxUVOay31QTCCw-ZoGszGHdi1Uop9Impy-WAn7iBI7ldosJtUQy309sX-5OVFVFLd4Inzqgzxj9ON0IazRWPqjiZrFcUeAfoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عمو پورنگ وقتی اینارو گفت نمی‌دونست مادرش این برنامه رو هیچوقت نمیبینه...
❤️‍🩹
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/671337" target="_blank">📅 12:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671327">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DwwcxXn852-ah8fPGSFBgLwbq04f731lci9SD-YLI78R39QUm7qGmpScc4TpU0TC91iONb9qDa9ULcBW8SC7dLK8rnQHIOsv3K6coau78H2lsK6v5olNmGGJlLxtXeLGdgHgzporhcYi5UjowV6raaGxtaTLabw4Z8re9Q79x1P47v1mwFgEsglP9TTbUaIWEj87hfeRkCLKEYBOUu22C9oW3aEGU8RAcQ6ELM0hkn4R_0Jmfe597MZ0f-3Ybmusa5Yhl-b8mrVZVUXc9jCF52nA1DHi37s-LpyemtfBbUsQA1CkAqHnxO32C1lFOqMLj6PbIN4Zk-0F1yt6p2aPpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LsmuT0hVFMzCcd53plhuZkcDVEbWb8wGosgDXpADI7OViDg65lX6JHJOF4j29HhwmhCEnZzDAV1CRLY2sdUairJpluFZYGhncR68JPFQzQ65RCGfPDppba__Sy6tp87Lg_7eevRxS4nw4qfkLMrJTmUBrZzcH44eo3Vfar3NCVQKXtxf8Pz_cWKGzWJ7N9AuKTTYAZsqMlmvtH6T58PHhWcYSWxE5uRSfVAk_tfACGHBytdiPT5xw3WkH4tRCUriq2M06RVaLEmlX0646seXa5elX-xjX-D9nVyiTTYmPPdf4l3dYtVrj1kLHmAesWlqIdhXEfLO9Dc8ET6KI74wqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FcPhUonx0Fc0xBBtYI-7avZsAFD_UAw8Hl186RFMx0VZgIj5MLdb-OioATvqt0DONPmndA6ftMj2CDAdHAVB1sk6asT-fuVJqU1hSRTKkBRxORunfts9a25KIGtkei3Iahhqe1x6XdS_PG51EZTc35oczjEtO5rul8WNdH9O08UrSye9s8igwOwaYoFJKfkEX2u4x7CNu7hunsUV2F8yVWwff-km2X-Y7Io0M8SUSL2C0Qqo9FGYlPCdxJeUk_V7tFZOGujJOoRx1-JwqmCs-skkrSCaJ9Hds-4ZHhdIsOsr6W5iloJhquHh4SiozI9mUfZoqCkXght8NbBuUkEJig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lCYw3OTwTwdvnuUHN48zuNbmb5DAwJpvCEj3sjYmRmtWM0UzYzhQ3_a2LubJL3TeYq7cgF0ouueQlKJT3NqxsuWnPoHjbettBhONQzfAtP6nqdT2m5skj_tKUvka_z1-YRR9tCRXG4gG14-r9k8D1E3yspD01hsXHJj2zsnhUgp7h7_PXFuAMKhKBIY48vkSutruhGcQEtxbGvdFtKQMEiWvjbi-Cm_6i15PWxe6Ed20XjAowPAVBIBhuFVhZ9hfAbC9hzUU4-fwxB7zlR4Cnb3p2b-uwkHIcfp5LOm_oso_cLjTphJfB5LIJXr1aMzcOcUVSxdUKajcpVHqe2HH2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NRILQbGvPmzKilgnBub7chRLq7dh_CutptQb7dbsFR6RBmneX_gEynMf6pwXpJ1x8wd4K86z4-Mp_T7CSG9elZPnb4qbzYhyu9-E3rDz7OAsX3KzbbE9nquptA9jgiW0XWy3cnlNf17gADVIC4e1tRVNyWGIDlj6-230nelFRcAJEBuhNPxrWqZooGMbjiI43P5Yl2YIZDPsiCoooxHcTqqPxlrY1W364QiDW_Gvksz4-lvH97PRbeoO2XngtL4IjjgpWSEV8SxhL0RQKmNgLpHPBYmc0mawZME_TWENrZmZLc70gJpf2uiV7UcabSEmgh0UCVQTHzCx2y44lrUYKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZRU0bsGloPqpWw2MU_AgQyTCU9PY5cmM4Kl7NV4kgom0XahbLyQbbCKl5Hav0RgqPC8Flr51Iv2LwwrYLOsdFoKT2H1A2lvK908uB1Wnsb-qqKLFkYzjDQLb1BmYfPWm4EiLG2hLOu_BvMkA9Um6XZFeCxosPTcwcvsBl3Xs2vsyizB1aUmI5k1TuM8ihZY6US1Nac1frMGOr2PKyWLWGK3i2o0uJKjG2JLY7uoM3Bu_lFS-WIV5Np6-BZLSYQUuoVhPCgdvCGeP3e2TmbAJL8mqn7m3BshEQJESELXiCaSds2hzNYhEDXQO7o_jlXNGyfA5vrgLHB6glhsdzUqL2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F-X0dF2UigedfME9Bue5dYu4eJaAWSf6MTtzuskH-IhQL-DgccbgZyr9fMkhdKEc-qqrU5Yp3yMgsI2YUjuWQAH7fCJlTTjVH7GbOKwXQEsLxYYJdtR4HjMvlSZTDG4HJQw8Zs4EaggZJ0XRa1h09QkPdzhbiqaGPKZrz75BtNxcW4BM1jiU5hBrg4pt_Ixyg_gxGo-oyuJ2g-4LFVI4ozkss0w6azTJO1GMdxpwsF4Mjbu-JBvGIo524KLF9DX8IxgThHv11gEogTnA3CKDgO5NMaetFovJ78as8J9chZkMB4A92NwweOhUJS-Es6jVFHSvQevx2AYxaP5XRsIfAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4fRYdBuh15bLKtl1EpXK4k-H-Vxmy9JLjAl4ILB3riFlIYD74mM-4a_Idf_vc-y-bfw3yELiFl2yKchUYqyFvSP9LOBDZMU3gRcOFM6YO24kt66R8L8YaQ5hnpUEkxVA2kz1FtKv0WGNiE3Nos8cDeymQLaDp2E-aN_b5rnAXZewA8AFrkzN58508Tu0_nbzFB2aXJZO0QJisDphnZl-LYUBHjYUqLNwbYPpgmyu6s-Yy9cve8UXA1Vm2M7GhvEVqZqE38a2gsOowNmtcSsscVOqLH-fArceyZDsfilLT0bajqkN2E2bTSHgtW7s08-WFypN7sIJoGybmEkHe6Vrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SGIfU6VhkP-vAkIwcpvBLUb5FdSd8bFHCQi-YbDXxwDiwfK5O_vZUiRZxyb4i2zmOiF-mU-q_l8s8FKuNA4bhBuPW5lkNYsTTyXmj4o6B3wjIR6HQ1h_gwQVW1T18S39iO-3ymkqirI_3IXnkpWQxrZrM2xh3EFE_LOLxPyDGNh2r1BESwiN_mOxi5g8ZEpCfbjEr1V8Dm7jmjdbOp_rtSMNvHS24DH3pAZlLBbyOdJqBOcbwAn-mBsCrdUPiA8iRdjA0bQtxyiEY78scpIrPJCPn1k83RawNYsI7pkUm9W75MnHpGYRpnDFGa1ZAEi4BBuFmdJU-oIfwsK5suVL-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBN6HEkgGjMRDZe-xsHDqh5eJSpoPtGK4RufVrNg3RoR0qoRBrkZmQaCs6sW1WLnRK9f2u7W62zrJFLbWlh5d9DyCPN1DDxCnl0VSL9yimswe9bhUrBz_MDEcUThvpvhxCImEqLn3teUKPZWIPWntXHeVK4xxAuFkFKUmc8qGqH72_m0ld6vUHy8vETj2RUPKD5MWusK7UUR11MIh8h3jcIRIq50uVj8CVKXjAilIF22U42rk4rrqHtCXZ6dpeXTER6M27QizUBShxWAPRAlx2Uw5W6aWM4J1bETAfcaBLU2OMsIMo6raDhFZfQJj9SPVXxLrTsmkv15CFoZ3cNVbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
روایت مخاطبان خبرفوری از قطعی برق در ساعاتی غیر از زمان‌بندی اعلام‌شده
🔸
اگر شما هم چنین تجربه‌ای داشته‌اید، از طریق الوفوری با ما در میان بگذارید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/671327" target="_blank">📅 12:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671325">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22f635ba3.mp4?token=eAHUOgBwrkdO_TCL_INp6-OAi4VlA2fnHVUBBeJVayWMamNLKXq5_78-rOpDbFR0M9hTb-PSAPvc2aNp7yonIuAJJNgwIii3zMkYL_2xjgacsagUmUEckvGiMZPPswyFxQBTnLhDsISC_VSMWovGnN-prEqnU5aDAZ42PytUdEPrI6e8DxZoe7fdLRRlazIgdwduTkY_LKy2f39Co36MZvfmK-OTLxgQPorbFbw18LpPzji7FialQTugxZeagIrmBrth7OmA_XvngGL75mamwnOGoBss9dDrYRM2ZPbPp0ZC2Oi3fvrpsWZSQEnElcgAZfVRdWHhcBdjwkkIrr_-3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22f635ba3.mp4?token=eAHUOgBwrkdO_TCL_INp6-OAi4VlA2fnHVUBBeJVayWMamNLKXq5_78-rOpDbFR0M9hTb-PSAPvc2aNp7yonIuAJJNgwIii3zMkYL_2xjgacsagUmUEckvGiMZPPswyFxQBTnLhDsISC_VSMWovGnN-prEqnU5aDAZ42PytUdEPrI6e8DxZoe7fdLRRlazIgdwduTkY_LKy2f39Co36MZvfmK-OTLxgQPorbFbw18LpPzji7FialQTugxZeagIrmBrth7OmA_XvngGL75mamwnOGoBss9dDrYRM2ZPbPp0ZC2Oi3fvrpsWZSQEnElcgAZfVRdWHhcBdjwkkIrr_-3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمایش بی‌نقص اسپانیا، پایان رؤیای فرانسه؛ فینال منتظر آخرین مهمان است
▪️
قسمت چهاردهم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/671325" target="_blank">📅 12:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671322">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8da24524.mp4?token=htoJBxaqXZS3CjgstVhg9SCJ7Gk-icFWOe7iY-fwEdE93Qu7C8pCRxC7ylEMKT4CWTkwMrZD4ObJBoZOKvB8D_ZBsNPpvJzqebdTslAuBEr5jtXdpnY0IEPcMpQBimNukuPynIytDwnGUpjPt2nq6NOPgVJrA3IrRnBGqt7aS2bUDHVOxL4mswNj1UZahdwJ9Gz09GUQGzJrNguqmn2yPcXlL1aj2P0LxBs7xzFXFGoUB-pK5csx0INPC5nCkbvOM1vlrD4hMdqwCwOMIfOnid1qJ2pOPP0CKQyTNPWPNJwACIHQcmzA4SCKIBFKrMJpbJg-1DnwDcjoOFMt-ChtGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8da24524.mp4?token=htoJBxaqXZS3CjgstVhg9SCJ7Gk-icFWOe7iY-fwEdE93Qu7C8pCRxC7ylEMKT4CWTkwMrZD4ObJBoZOKvB8D_ZBsNPpvJzqebdTslAuBEr5jtXdpnY0IEPcMpQBimNukuPynIytDwnGUpjPt2nq6NOPgVJrA3IrRnBGqt7aS2bUDHVOxL4mswNj1UZahdwJ9Gz09GUQGzJrNguqmn2yPcXlL1aj2P0LxBs7xzFXFGoUB-pK5csx0INPC5nCkbvOM1vlrD4hMdqwCwOMIfOnid1qJ2pOPP0CKQyTNPWPNJwACIHQcmzA4SCKIBFKrMJpbJg-1DnwDcjoOFMt-ChtGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نشانه‌های تروما‌های حل نشده چیه؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/671322" target="_blank">📅 12:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671321">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muWuwceaRlHwAM_qrt_Oc9OoLvqhiWLmJKxuOHMmJ-vajLGLJ3RiNtbMFALhnDhBkUVBX9UD4ue7pBrLTBJGXh5BKXa5mdfzcNN1n-ahR49Sy8raFCO2Lts5NutPdp_evuMFYz3jcIgs2Jze4E1a7wWm7bi7Y5iChOXaO9jheMuLCs5WsDrMj7hXP_a1_41YG5w5e7St2wTa48AnJwqMUdmWw3qbdximOqNF7W-vQ1cKHtCaaZbDAswureMPm2uW3mqTEwFRzvas6Sq1wonJWUBNz_cwXo5U-vpdwVGcYEghB0LelPkmjbQL6-JhLGLRQxXjxWJjizOVGwRZ9J7guQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظی تدریجی با پول نقد
🔸
بیش از ۹۸ درصد از تعداد تراکنش‌های شبکه پرداخت در خرداد ۱۴۰۵ به خرید کالا و خدمات اختصاص داشته است.
🔸
حدود ۹۰.۳ درصد از ارزش این تراکنش‌ها نیز مربوط به خرید کالا و خدمات بوده است.
@amarfact</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/671321" target="_blank">📅 12:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671320">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10cb57b80e.mp4?token=FeCuDId5_k6JOT_tyjty0KdOXnJd1OT6ZbulFv14-7zDJWVgPV1gV2A1EbPiKc3D5OZI0X-ZtjBo84NaUpoi-75ccLOry4bpk5mBL6qWGUPvLj9gh_Tz36k1SOvup424z5uAQEOjHvBm6xl5CdFUgX19uNh38rJgPi_yxhcEY-It_wGY3eT_8JZe8MAFQ5MfG8iDMZ5zjOYSrU3uDMgiaGyGmne8Tw-zt3QtjW5DHbAb1W-yYWDv9DCjcHABGobAy3ivFujQvUPsuxZxh2gKHIPa56St1KYOr4dgBc0gZdctdU5_XStRjCQrC4Di_l3l_kfmGppkWAkb9eXGP92R6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10cb57b80e.mp4?token=FeCuDId5_k6JOT_tyjty0KdOXnJd1OT6ZbulFv14-7zDJWVgPV1gV2A1EbPiKc3D5OZI0X-ZtjBo84NaUpoi-75ccLOry4bpk5mBL6qWGUPvLj9gh_Tz36k1SOvup424z5uAQEOjHvBm6xl5CdFUgX19uNh38rJgPi_yxhcEY-It_wGY3eT_8JZe8MAFQ5MfG8iDMZ5zjOYSrU3uDMgiaGyGmne8Tw-zt3QtjW5DHbAb1W-yYWDv9DCjcHABGobAy3ivFujQvUPsuxZxh2gKHIPa56St1KYOr4dgBc0gZdctdU5_XStRjCQrC4Di_l3l_kfmGppkWAkb9eXGP92R6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله با انگیزه نفرت مذهبی در آمریکا: کارمند مسلمان در یوتا هدف ۱۵ ضربه چاقو قرار گرفت
پلیس ایالت یوتا:
🔹
فردی ۴۸ ساله در مرکز خریدی در سالت‌لیک‌سیتی، یک کارمند مسلمان را با انگیزه مذهبی و با ۱۵ ضربه چاقو به شدت مجروح کرد.
🔹
قربانی که تحت عمل جراحی قرار گرفته، در وضعیت پایدار است و ضارب توسط حاضران در محل دستگیر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/671320" target="_blank">📅 12:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671316">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aNLZc0NbOeYi9CvokCoDzgfoZsfQ-iauWqp4YEdXX1b-p2mXOmUUGbd0lsTXME3SQYOEp2MGOYcs6MRctC8Ksw7KliKLhDa6KSYEslq9YkjRzyyYXZsn-0OQ5KMeWgWPZ3hnbNnmHx8Awehr3so6bBGYP7b9YmxRoG74Mqs71uHplK-S6Kz-4Hy6U1_vB2n2wSQNiZQ5lk2WUdb7jf9GYRxQjjr41W5bHvM1C0TZfDJbY8glG1Rp2qPEALk_bkuDp3zOmhIQ_xkNkadmDi-TeAwR4e_0IJPv8l3O87vKZglp650eW9pkD8MLa8XvZYv0A4vjE4yCm4VpVspFMUK-XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WrV6bxAMqVOjn1IBYxMoCLFzbdv84ie8o7f8F1zt_s5kG-bj0vxE3S4YPY2esGZ3Z2gWetvyRZcsx7oEE-Tux46SGFBlU1Caxtg3qRBaEUNIihwnBYfzFqcvvNfVSfgEUrL7JgDXiXUpY-3JprMo4L0-SPmSAPHvzeuLlEhMnW8GxnAJvcqYuhhf5kCIITaMwnZWodYFBby5KljpfM19NuVD_AcRwWQB28MbQqGOrI0LWE5WoD6wDpeE3vnC_r-DQibFPoaijPwmCGczHAUWTEzFXnFk1rulV-ajh1rmynDn7VSvV6H3GQ5M2ANC0Slq7If6ZR8K7HePw7cif74snQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TrkTNdm70ZYmAdsqm9QQFhYQ3_5hED1QmPF0h4L2QaHqvaFHuweNdcF5bzm8zPapRr7uVMerGn5TU0hUbZxqo1OVx8oPNH_KOmiuOO_rd5l9EaG8FG7hmN9u9KwB7p2ieA9lTM13zJH4qH87KhmAuejbc2iIVd7u0dvLXwjE0c33DOfA28gfvohOkGKRQaBI8eL8yzUqyxsZAEsjXttfq5G5ylKd8Htsv9uu0nKS3TuDiLJeipMStyeZIW7pdx6q577ZZn-tW-hwHRTb3NDBV0abPiMlR_1IuDVAhDOJzyJ0FsVON_5fooYbARzA0wmAVr0nd0QF7YNNtPJpEkM34Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cP6sX_U_vJFm1_dxJDv965v2Ekd3FgoIr-hQqImaiME2Ga-Xjf95_FmNExdOyxJeUZkTpTP0lQbTfSjwYl7WatUNM_7H0vzHthHs3AhjrRINwagIXCJGCvXSlnIFMSUQaBI4JArEfp8R_0b9vaRCTTUu2Dct8Fn53MCaJg7-qktI5oJLcpP-6b2gI0g9b9SM5mJLJaXKlHx89D9s91ldVkn2E-vjcwuUNHk61wNAp4LHccWdP2nf0Np1cjmzp4H6FvfumrgWup2nOi-hW3W4uTV6IxrukSM-bkhonFljnD_QmtEKwkttLV05c3OB9H17_EBwqUuxKK3TnTYjIuhjyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شکوه خیره‌کننده جنگل‌های هیرکانی
🔹
مجتبی صابری
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/671316" target="_blank">📅 11:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671313">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a7487a4d.mp4?token=eU59q0zl1aIM-EEK0V-mc4LNL_z1mAGa7bzm6OahBaTLrhj_3rGXZIcXdgPldOZH1FvbuUw-p9hBYrH7qLSfrLpfJmPuO7sdZdF7eQdupcB2L8yEXw-cQxnUZodNyIQKcozaZbCVUL67mPB5awnDR1Bkg-U6A3Gjgvvno_eAMyxasooWhYfvfkQ5RogNdjEEbJCVTJnUNuUBFoiJb2G_6r_cNSGoGpxLNasrpQ2H0MEA8HiZfaAvfImOaDEaL7vMI_u4Ay3siP0Dei148KTr9-xS7WkefvREhlOthpEN41BU82sTP_Nlpvd2daQ_HzjSvkE3QgqXHKJsXVUpJu68sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a7487a4d.mp4?token=eU59q0zl1aIM-EEK0V-mc4LNL_z1mAGa7bzm6OahBaTLrhj_3rGXZIcXdgPldOZH1FvbuUw-p9hBYrH7qLSfrLpfJmPuO7sdZdF7eQdupcB2L8yEXw-cQxnUZodNyIQKcozaZbCVUL67mPB5awnDR1Bkg-U6A3Gjgvvno_eAMyxasooWhYfvfkQ5RogNdjEEbJCVTJnUNuUBFoiJb2G_6r_cNSGoGpxLNasrpQ2H0MEA8HiZfaAvfImOaDEaL7vMI_u4Ay3siP0Dei148KTr9-xS7WkefvREhlOthpEN41BU82sTP_Nlpvd2daQ_HzjSvkE3QgqXHKJsXVUpJu68sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله بوفالو در پارک یلوستون به پدربزرگ و نوه‌ای که قصد عکاسی داشتند، آن‌ها را با جراحات شدید راهی بیمارستان کرد
🦬
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/671313" target="_blank">📅 11:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671312">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWNtybIXePrl1byoiIRPbBkVQqSumlD_iV5cPzxUss7bKhZouiJ1dVCydiiZt8AvP97BU0tSBG84FxxpC5WT8gSH2fiP9j2RcFiCRtAVWU08SFuIApEtC_vzPElKLykHNzhg_pebCLc6hTjfPUT5nkBAwGOCXmK49ih_1dbQse_Uzwnpg3JwFRH5hIRi9iqmZwBrgel4KfS3Hnq06aY9Ly83PexqIIcNwojyImWKjjqLOtmdm4SHGCEYNTuRnt6JO75YBKYu1-BWq_phqKWLOiezsH9F_aj79Rc9V8cJleL5XtiR9uE0meXRXyzVl3YVCfrLwWMQwo0PHTcl9HykPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهندس نظامی شرکت صهیونیستی رافائل بر اثر حملات ایران به هلاکت رسید
🔹
رسانه‌های صهیونیستی اذعان کردند که مایکل کاتز، مهندس نظامی شرکت تسلیحاتی صهیونیستی رافائل، بر اثر «جراحت‌های واردشده در حملات موشکی ایران به حیفا» در عملیات وعدهٔ صادق ۴ به هلاکت رسیده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/671312" target="_blank">📅 11:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671310">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb36b6e79.mp4?token=XOV45Z3IyQkIdYyxw_4ClfxJjeMk54ieyzWGwF_qw9bhvaL1RQc1vkRIXeO5i62ghsZDjEq5X9d2agLPoFDO_g_fyAmtWepo6BLzAD5dVUvXn5D4Q8XhyanfmEPk3eE1bD5_ng0MAYIFnwmu5jzK-CF4ZA-heUIO7Xm9LfuiEIZic2SqVq1TK-Vyc3a1kCqA5ZGnEtXx0p070mC2uOt2cCyWgJvht-VNiKV7Ch5do-fJ5lr_vbAnMVj0DBVZSaJFPGi-Wl5Xmo25UNAM-vVb9LZplp2Dmj5MTx46OttJ9ObSDWf6Jf9RTAOyUM6pfb7huej4STN8NnQc2FW-XONnBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb36b6e79.mp4?token=XOV45Z3IyQkIdYyxw_4ClfxJjeMk54ieyzWGwF_qw9bhvaL1RQc1vkRIXeO5i62ghsZDjEq5X9d2agLPoFDO_g_fyAmtWepo6BLzAD5dVUvXn5D4Q8XhyanfmEPk3eE1bD5_ng0MAYIFnwmu5jzK-CF4ZA-heUIO7Xm9LfuiEIZic2SqVq1TK-Vyc3a1kCqA5ZGnEtXx0p070mC2uOt2cCyWgJvht-VNiKV7Ch5do-fJ5lr_vbAnMVj0DBVZSaJFPGi-Wl5Xmo25UNAM-vVb9LZplp2Dmj5MTx46OttJ9ObSDWf6Jf9RTAOyUM6pfb7huej4STN8NnQc2FW-XONnBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آهوهای زیبا جزیره خارک که از ترس صداهای انفجار به خیابان‌ها و کنار مردم آمده‌اند
🥺
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/671310" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671309">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
بندر فجیره خاموش شد/ ۶ میلیون بشکه نفت از بازار حذف می‌شود
موسسه HFI:
🔹
بندر فجیره امارات که مهم‌ترین مرکز جابه‌جایی نفتکش‌ها در منطقه بود، پس از حمله موشکی سپاه به دو نفتکش(VLCC) از چرخه فعالیت خارج شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/671309" target="_blank">📅 11:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671307">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFDWZsRmYdzGKe1CTEbkIkKVuKl5awJFK7BRl3oN9k75GJvp9WLBqA0LhT1iITDOxTnZxdUxHrp54HL1ZUncNJuwuvN4cZQH-9oZR_05N1-nKrezvKVIhKzQfpfFOuNgluJtiVYrCqWyhXYbeGk0biEpEk65gpCap2Ma_vM1Hx7uk7fARhIUxprP_-L6URiPIudOCyLmr8DYH4uUcOpGYYGifF2QPsR59h25xdOvYcjio8tQZgqo-GS8Q3LRvmTt4qqKITil9vRjfkMYWLmUFzV74Xpdgw_8ITw3xcreW2HMnG_6HnL4i8rhax2oFIlkLceyHCcZUHqk5tKe5ceoCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آکسیوس فاش کرد؛ ترامپ در اتاق وضعیت برای حمله گسترده‌تر به ایران چه تصمیمی گرفت؟
🔹
همزمان با ورود جنگ ایران و آمریکا به مرحله‌ای تازه، دونالد ترامپ با برگزاری نشستی محرمانه در اتاق وضعیت کاخ سفید، سناریوی گسترش عملیات نظامی علیه ایران را با عالی‌ترین مقام‌های امنیتی و نظامی دولت خود بررسی کرد.
گزارش آکسیوس درباره تصمیمات خطرناک این جلسه را در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3230476</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/671307" target="_blank">📅 11:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671304">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pX49HXaha9raM85hYX6kL_BxJtFYM01P1LNKH7ZACKfgK-2cUmG7WRHj3Yo9xzTddqfXqMz0KODxmvPPRHIBXxEtsj7xBSpnh1jqRujS0R0BETPd8A8vZS643OOD0GOgLORKAtoaXGrHnvPNRjXUknd68Z6-wjj0N501PQWbs8pmXmZkyTwsne05SFRvww89NT_-B3a45TBmbtaS62DZKtEkuJvDhkLedAstMBoAu-FfDfbaHKq5PHC-cElD_caCreMxxa4_XHY2vBsqVwZeek6tXQ0eQ4u2_N_QJ4oOHZYHUSlt7LCjoFe77RvN_9WrKAB-gRGorLM43UBsrPhQCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسئولان با پشتوانه ملت، باید اصلی‌ترین مطالبه مردم، یعنی خونخواهی را در اولویت تصمیمات خود قرار دهند
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/671304" target="_blank">📅 11:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671303">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ba0bed2bc.mp4?token=fv9jb9-s0IUjkjJHULp4Ov7Hc-N8g1Qjsxv-xbwQOdMF5CsFw-cFX6r54ULN8GA6e_RlEERzXqymHvsgz88lThWSQCskL0in5qEWYHIBKggqFmZkHtXDOQsdXa1vlCpGK1A_BmjWlJQLjvAe8lH7X56-LFjQ-KUex7D9tHpiwYGAIU4yk7Wl3wzsq9EuhrVcr4b7ar1HpVVvfD-v4HGmqwwfMGEFQCEkxlLx3eEG3oOoHyj0Y-e8RqoXyghgeS-MQGrTF7FielUKLpmUQdzoQ66ZdjuwQIUUv0b7TaYGVi_J6-NenGeEx7QtgvSktbUgaTPy-Z6YkN6Io4R4G8D0yjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ba0bed2bc.mp4?token=fv9jb9-s0IUjkjJHULp4Ov7Hc-N8g1Qjsxv-xbwQOdMF5CsFw-cFX6r54ULN8GA6e_RlEERzXqymHvsgz88lThWSQCskL0in5qEWYHIBKggqFmZkHtXDOQsdXa1vlCpGK1A_BmjWlJQLjvAe8lH7X56-LFjQ-KUex7D9tHpiwYGAIU4yk7Wl3wzsq9EuhrVcr4b7ar1HpVVvfD-v4HGmqwwfMGEFQCEkxlLx3eEG3oOoHyj0Y-e8RqoXyghgeS-MQGrTF7FielUKLpmUQdzoQ66ZdjuwQIUUv0b7TaYGVi_J6-NenGeEx7QtgvSktbUgaTPy-Z6YkN6Io4R4G8D0yjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف تحلیلگران بی‌بی‌سی:
آمریکا با تشدید محاصره دریایی ایران، به اهداف خود نخواهد رسید؛ بعید است جمهوری اسلامی ایران دست از تنگه هرمز بردارد چراکه این کنترل، مبنای مادی هژمونی منطقه‌ای ایران را تامین خواهد کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/671303" target="_blank">📅 10:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671301">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76fd68a7fa.mp4?token=ZQ9Ku4m4sJrrE4qYpA5nKoijpICMpywPPCH0qNKUJ1c6f7BviXijqZc8V7DlR8IVH7nYh1brxdrjYxGHtUIgczCjOjqYcq91Pbadqy9FIPoGskR-L_JLjGYpfbggQfY8SL4W5A2RgNquAu-StlMYxCQeW6i9y70O-0MwZuxJIVP4ZB7ShEQQSwzMqLDrCNN-H-suPO2aV5UmwZgVDmRVMOC28pgu3n-8RaiG2-XtbZpQFeODfQcPTMBbUyJmmzsBrN6prJZwrftCnhwJxygD_1--Tiy5IKQW6k-o_aL2san_kMZlsEQKSELrh3u0gri3-RQQ9oneRdq1VpI9ysHeGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76fd68a7fa.mp4?token=ZQ9Ku4m4sJrrE4qYpA5nKoijpICMpywPPCH0qNKUJ1c6f7BviXijqZc8V7DlR8IVH7nYh1brxdrjYxGHtUIgczCjOjqYcq91Pbadqy9FIPoGskR-L_JLjGYpfbggQfY8SL4W5A2RgNquAu-StlMYxCQeW6i9y70O-0MwZuxJIVP4ZB7ShEQQSwzMqLDrCNN-H-suPO2aV5UmwZgVDmRVMOC28pgu3n-8RaiG2-XtbZpQFeODfQcPTMBbUyJmmzsBrN6prJZwrftCnhwJxygD_1--Tiy5IKQW6k-o_aL2san_kMZlsEQKSELrh3u0gri3-RQQ9oneRdq1VpI9ysHeGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تابستان امسال گرمتر از حد نرمال خود خواهد بود
رئیس مرکز ملی تغییر اقلیم هواشناسی:
🔹
با گسترش پدیده النینو در اقیانوس آرام در پاییز و زمستان امسال بارش‌های خوبی خواهیم داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/671301" target="_blank">📅 10:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671299">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmGUuy91IKpbsxcxppxVPjk1s43oFdM0EjAfCKrHmXxvYUly4Y5rAOI0z6hSEESRKqeN313ROjSLq8rH7ljJhWYq41KQyQigax8GmNn872RdW8KUdISdn6RZWrt8wVsIuHODYCvNqu0En_1uLZ04MEZz3xhyNbnwQf6sLcvcXIUtcIy1LH5CKpj8DFSbA27tyVsmAE8BfbuP8Ja-MGxLXHG929Vs4xT7iUnlmo0Ei1ePQ_tFZ9Jo-yYBQXEk11pgs4kPszj6nXvHJrLUgYVKQkYlHadUU_QhvyUUFQUTi4i13DrnptKDiORkh4ek3dqEpN9vHwjjx8LEvNytclr-hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امارات سهم خود را گرفت
وال‌استریت ژورنال:
🔹
امارات پس از کمک به آمریکا در جنگ علیه ایران، از جمله مشارکت در اجرای ده‌ها حمله هوایی علیه ایران، در ازای آن به دسترسی گسترده‌تر به تراشه‌های هوش مصنوعی آمریکا و امتیازات ویژه دست یافته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/671299" target="_blank">📅 10:37 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
