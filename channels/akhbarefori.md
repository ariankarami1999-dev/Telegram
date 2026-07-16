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
<p>@akhbarefori • 👥 4.35M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 12:08:39</div>
<hr>

<div class="tg-post" id="msg-671720">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aA4_jk89iBO5rvhauMB990irWCuOYG8EIjdniQAapA5_ULegRlq_nxAcbC02YDQrE13XNTyFvCnI2b6zC46ndaBLm-nSudiVrd3wFl8K7cl_eDgjOcfskMaaoZhD7JHFOv_AkAnC1icAy29o82j2bayzmuy8CNA_0LcBUWeTohxtNtdkK-oMT_dYayrWiLMsHqxlM9ymzl1XWwsXzj-rhNZG56YQCUm-tIudEIdcOpeLgrG7k7Da20Xv6n2TsAwAhj5BHqL_eTOh3TiJH9lNinNQ_GeyquZFrg1Wm8a-Lmbv38-HVAmXINZewirGMKa_bCO7pEmaSSz6QTGBhqfjUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علیرضا فغانی داور فینال جام‌جهانی بین اسپانیا و آرژانتین شد
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/akhbarefori/671720" target="_blank">📅 12:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671719">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/687172f5a5.mp4?token=hYO-PKf2nv5eWONilqkqBAru519LMbO8sVyyTzGs1tj3PPkY1a5AIdegeaug-8G_o1yBaUlTqqernohGpg0m5Xq_z37Dgb1Hgi6VPs4SN-g1OoWW6A_0KVOFf6WJZfXUWMI1AwlMjHZYyIfNBg5VIEbzMA0hytrRyQcvCkr0jv65wztWvEF5BtJpkv7CUT0tbbOOArB2UhpfL3Nn8kLkpimbu9xpLzPQCCMtyeGYhkUBDKbETpIaRvu-FcZeEWxRWQw9Vhjy34j1Jk1DVEYwIws4iMqZHPtsSgcd6E0zrEkNhiuJfHmcr0EH_zqPi0yNWtFaWQplbEETQGhpbLlXWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/687172f5a5.mp4?token=hYO-PKf2nv5eWONilqkqBAru519LMbO8sVyyTzGs1tj3PPkY1a5AIdegeaug-8G_o1yBaUlTqqernohGpg0m5Xq_z37Dgb1Hgi6VPs4SN-g1OoWW6A_0KVOFf6WJZfXUWMI1AwlMjHZYyIfNBg5VIEbzMA0hytrRyQcvCkr0jv65wztWvEF5BtJpkv7CUT0tbbOOArB2UhpfL3Nn8kLkpimbu9xpLzPQCCMtyeGYhkUBDKbETpIaRvu-FcZeEWxRWQw9Vhjy34j1Jk1DVEYwIws4iMqZHPtsSgcd6E0zrEkNhiuJfHmcr0EH_zqPi0yNWtFaWQplbEETQGhpbLlXWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گاهی کسایی که بدون پتو خوابشون نمی‌بره، دنبال یک حس امن می‌گردن! #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/akhbarefori/671719" target="_blank">📅 12:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671718">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
لغو سفر نتانیاهو به آمریکا
دفتر نتانیاهو:
🔹
به نظر می‌رسد مراسم سناتور گراهام تا پایان ماه به تعویق افتاده است، و به همین دلیل نخست‌وزیر نتانیاهو هفتهٔ آینده به ایالات متحده سفر نخواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/akhbarefori/671718" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671717">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
رویترز: شرکت‌های کشتیرانی به‌ طور فزاینده‌ای از عبور از مسیر تحت هدایت نظامی آمریکا در تنگه هرمز اجتناب می‌کنند
🔹
شرکت‌های امنیت دریایی هشدار می‌دهند که هیچ تضمین قابل اعتمادی برای عبور ایمن وجود ندارد/ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/akhbarefori/671717" target="_blank">📅 11:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671716">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کانون بازنشستگان: ۵۰ تا ۶۰ هزار میلیارد تومان از معوقات افزایش دستمزد بازنشستگان پرداخت نشده است
علی دهقان‌کیا، رئیس کانون بازنشستگان تأمین اجتماعی در
#گفتگو
با خبرفوری:
🔹
۲۰ تا ۲۵ درصد بازنشستگان مستأجرند و با رشد شدید اجاره‌بها، بسیاری برای تأمین هزینه مسکن ناچار به دریافت وام شده‌اند؛ موضوعی که توان آن‌ها برای گرفتن وام درمان را نیز از بین برده است.
🔹
با وجود افزایش نیافتن برخی مزایا، حدود دو ماه از معوقات افزایش حقوق بازنشستگان نیز پرداخت نشده که ارزش آن به ۵۰ تا ۶۰ هزار میلیارد تومان می‌رسد. با توجه به کمبود منابع مالی، سازمان تأمین اجتماعی در شرایط فعلی امکان کمک به تأمین اجاره‌بهای بازنشستگان را ندارد.
@TV_Fori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/671716" target="_blank">📅 11:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671715">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
توانیر: برق تمامی مراکز آزمون کارشناسی ارشد تأمین است.
🔹
آب و فاضلاب تهران: امسال آب در تهران نوبت بندی نمی‌شود.
🔹
مدیر اورژانس غزه: رژیم صهیونیستی بطور نظام‌مند کادر درمان را هدف قرار می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/671715" target="_blank">📅 11:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671714">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0UZRMXI-2AHhF1wHnOiNXvFNmERaUdOhS_szC5-GjjuFcJm2ohvkmQLDq-NPx8bcH5-9hAYnoVAN3iHT3Fe-Y8asKJkVwRp42-oxFmpUo9afxrzt8fhxCyZURTp8XwKWXg71WnObODJKTp2EK7tyFAnwCNptgXFw538J5l-_oCNYzm4GolTZsW5U85TasmvuscnYqiwBOFaoLKgunZ7Xr8_Fx--_Ve3oDP_ndHev1wERQ8gtNAv4SdJdm45or4D8Rr0GKw6ibOxO_NPgosrotn70MscnSFh5DpjKWiZ2_azBK1v6FxJhputxU-xQmdXBBTZpSxwyu9dqN423TcJnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف یک محمولهٔ سلاح در سیستان‌و‌بلوچستان
فرمانده مرزبانی سیستان‌وبلوچستان:
🔹
درپی توقیف محمولهٔ سلاح از قاچاقچیان که قصد انتقال آن به کشور را داشتند، ۱۵ کلت کمری، یک کلاش و ۱۸۶ فشنگ جنگی کشف شد.
🔹
تلاش برای دستگیری عوامل مرتبط با این پرونده ادامه دارد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/671714" target="_blank">📅 11:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671712">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
سپاه هرمزگان: به‌دلیل انهدام کنترل‌شدهٔ مهمات باقی‌مانده از حملات دشمن در شرق بندرعباس از ساعت ۱۱:۳۰ تا ۱۴، احتمال شنیدن صدای انفجار ناشی از این عملیات وجود دارد
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/671712" target="_blank">📅 11:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671711">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🏆
کامبک جنون‌آمیز آرژانتین مقابل انگلیس؛ انگلیس طبق معمول ۶۰ سال قبل بی‌جام به خانه می‌رود
🏴󠁧󠁢󠁥󠁮󠁧󠁿
1️⃣
🏆
2️⃣
🇦🇷
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/671711" target="_blank">📅 11:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671710">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
شادی کارمندان خبرگزاری آرژانتینی در طول بازی با انگلیس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/671710" target="_blank">📅 11:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671709">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afca301f1.mp4?token=JPn3MVnFyi3eqAWlrjSTCCJDjm2LB8w99JG6KT19-h7sqsQByBWpKs--RVIMKpJK3Y0lEjRMy_l9lBl4iet5vpwEM2SFflJpNwJnz_XaT_D_aFu2dPILP6GsxG49nsGJa9vmJzPU6s-HMyNnP1ZqbOgtp3FVp0IiHTuY8TDXuRV7EBloV8bMsdkuvWEv6VLcwZX11EWQ9tonmBbuailnmfRphc-_awK2ztgp-1PYppMZODXiTbOLg1Fcd1sr3zfDdmhtX_MTyf5jo2Iko3HBY6RgPIJeR5mRJWrr7XPFs8HuZOVQreVkNhgeeSrP0lpPK3UJRYGxqa4Txs1wmOuBgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afca301f1.mp4?token=JPn3MVnFyi3eqAWlrjSTCCJDjm2LB8w99JG6KT19-h7sqsQByBWpKs--RVIMKpJK3Y0lEjRMy_l9lBl4iet5vpwEM2SFflJpNwJnz_XaT_D_aFu2dPILP6GsxG49nsGJa9vmJzPU6s-HMyNnP1ZqbOgtp3FVp0IiHTuY8TDXuRV7EBloV8bMsdkuvWEv6VLcwZX11EWQ9tonmBbuailnmfRphc-_awK2ztgp-1PYppMZODXiTbOLg1Fcd1sr3zfDdmhtX_MTyf5jo2Iko3HBY6RgPIJeR5mRJWrr7XPFs8HuZOVQreVkNhgeeSrP0lpPK3UJRYGxqa4Txs1wmOuBgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات هوایی رژیم صهیونی به خیمهٔ آوارگان غزه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/671709" target="_blank">📅 11:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671708">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXuYrHLXrpT9V-YMn0HO1LM7hyXHvah_CXHh-nodHt0AbMqcIvqhROV2nH_vF1qQivuEeu5WISRHON_Knw8ddXj2T9FIu74PXGtn15Q7tWJmgn8R4MTDrBpwT13w1KEu5bC2NuLoFmOLcMBbdAPY-HEAAx_X49CnQOyKk9ncjw8s1_1LFkesjNrnelVv73YDaUqUmoKLtEwyUJsYAYW0q9RmMxKedXnwmXnlIDzjbTuUXkppx_k66xb-0sa9z2iBkHC5cm3luexayB1QeZIr2HszyOfhXkBUH1CfiqfUFUf9BEgrDXKsKbiygRoMiIWbWdvKEud5UL556Lo4Cy3NXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا آمریکا با نیروی زمینی می تواند تنگه هرمز را تصرف کند؟
🔹
طول تنگه ۲۰۰ کیلومتر است که به همین میزان مقابل سواحل ایران قرار دارد. عمق این سواحل به دلیل اتصال به سرزمین اصلی صدها کیلومتر است. برای بازگشایی تنگه و تسلط بر آن باید قوایی در نظر گرفت که بتوانند بر این جغرافیای بزرگ مسلط گردند.
دراین‌باره بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3230762</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/671708" target="_blank">📅 11:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671707">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در بحرین درپی حمله موشکی و پهپادی به این کشور
🔹
ارتش بحرین: مقابله با حملات هوایی ایران؛ امروز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/671707" target="_blank">📅 11:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671706">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0a706486b.mp4?token=PA9xSlYj0Fmhb_A6fvSdXuYHna5kRF5l1GI8kFwWup6Whso8hyFggrP8fDg5FQgLdnuEKSFMKPQQYWH5Km9sO6xu9TXl7KN7O-fnmnIsnB0SokW6ytndjvTsSeivB2DsQd97A1DlKGw_USne1No2_YjYYpFKQqSW4h2kvoOmlIdQuv3FsiTs74BsCGVNRScqnahUPUVmb4eQWI7463jzv0BfEz8Mrn6koWh3cwqpQmlmFUPwQEXij9kovDbHJ2VV4-puFGRz-9qjo3L2qUMoTsJfVj4y9k5sTDT5KxxCVG7q9tVp7UkEBNsBOmdiPvofEna_RbKiIxZzLQqc-97iUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0a706486b.mp4?token=PA9xSlYj0Fmhb_A6fvSdXuYHna5kRF5l1GI8kFwWup6Whso8hyFggrP8fDg5FQgLdnuEKSFMKPQQYWH5Km9sO6xu9TXl7KN7O-fnmnIsnB0SokW6ytndjvTsSeivB2DsQd97A1DlKGw_USne1No2_YjYYpFKQqSW4h2kvoOmlIdQuv3FsiTs74BsCGVNRScqnahUPUVmb4eQWI7463jzv0BfEz8Mrn6koWh3cwqpQmlmFUPwQEXij9kovDbHJ2VV4-puFGRz-9qjo3L2qUMoTsJfVj4y9k5sTDT5KxxCVG7q9tVp7UkEBNsBOmdiPvofEna_RbKiIxZzLQqc-97iUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ست مولتون، نماینده کنگره آمریکا: «هیچ‌کس به دونالد ترامپ اعتماد ندارد... بیشتر مردم جهان معتقدند که گفتگو با دونالد ترامپ، اتلاف وقت است.»/جماران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/671706" target="_blank">📅 11:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671705">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bb2WkH6N4bJWJa0znpDc8Z7aos5Zp1SVTFSqWcm5Ud6l1Se4ndvJWBGqMjwE9YQMTu5qHF-HQNl07898gEmKIhWaIIID_QqJ_cOUOfB-7z1OWpO98rMxWCCHX40mBT47dwEgBHOMvl_QoXzabIyCpSf1Amj9pNaYfhpWy2lVbqiPnqN2ccAV6v-kZXWEAebzJwWDzvkTU0Zj3nwqk8-QUZcCgNdKt01s1-xnkQuX8Bn1VlpJDhUeYB7s6i0dJ9Wg0EvPTB6Q73pS_9RDNjjm2G98TkoVl81kJLx9PQAGNvDhlVqLwHT29QXHVAf7j3F7N0KTA8C7iI9rc6u_oeGYBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قابی به یاد ماندنی از حسین محب اهری، امین تارخ، آتیلا پسیانی، داوود رشیدی؛ هنرمندانی که حالا هیچ‌کدام در قید حیات نیستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/671705" target="_blank">📅 10:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671704">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سفارت ایران در انگلیس: حمایت از محاصره دریایی ایران به عنوان همدستی با آمریکا تلقی می‌شود.
🔹
صادرات سوسیس آزاد شد.
🔹
محور هراز  ۲۹ و ۳۰ تیر  مسدود می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/671704" target="_blank">📅 10:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671703">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCXEXqouiMEUZegho8XzRqZLN0pDBh28Vh-VE1Sj4MDX2e3BNg1XbmQoj57e8XIGxeFSabrKh_qpN3_gd9iMjg1aQvuDOWiXyCdijmrQbHfu1hH7vlcEzRVO7Ii1ZiQYXnYG1E1wxjxlnpF4IQVecvgHVvR_oKImFpjETeNdtenVKIuDcYpla1YnV7XdpJ0qNzrXkwUZcZeqqTPDHR5ejHNbZBu2fNlVkhrpY6pV27httUGIjXjPBHU6ZfZAFHRwnNADNhVE0r9UshxCQ5yZECiRcU2yDFDB3I-cnIyl2Hx9RYdGJNClRWcnR1A60MKFT7bCm4PEPLbNPoc2oRXKMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران قهرمان جام جهانی تکواندو در بخش میکس شد
🔹
در دیدار فینال جام جهانی تکواندو ۲۰۲۶ بخش میکس در شهر چونچئون کره جنوبی، تیم ملی ایران موفق شد در دو راند روسیه را شکست دهد و قهرمان جام جهانی در بخش میکس شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/671703" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671701">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9bfa53b18.mp4?token=YZ42gLEdQyANTRVQN9s-8jSmTCGWiwnx1q5m91aJ_tYsdL5guebgnYtbIAkGnGkzmf-RsBEGsaaQYZUKOK5oHJ6e7ym83yADp5cIRByl8bKApFoX9lE0Vx5X866G4bsHN2LbRsk_2or5iJCA8iiC7vaUQrMWyMTv_vXfYkTTVBoCfurW4rpdHkRUhkbXi1FRQ0JqvhUzdJR99tzjFAXdpYnrkWWVTUrP4fL0DW_xwM_7n54XPtmTg9OVR3UkpON0bYpKm8AEAwZgko2Tog7zj43W7mb4UAic4aJ9A7cQjj0BbLoQBN92l1coOtohU3xAiXBQ4eFrevJjnF_urCF-D4t3HwgNeXRhG1fxn73ma0FLYun2Vin7I34-mViwBVP-7kVp02F6B1usQmwRgCUm-PemZlkhmOJ9klzyP2RmlT3plyC1Da7tNuk0cQzSZbMuIkSgr6fFufxBJi0oFREDu1Hzh2ZB_csCYu4QMNDXqamRuUg6TR5IqWTbeiPsV_cGuorQPNBB9ypZECdmrDT_L-IzqdNomYjGeziabl6mTG6i4GXjYaMBNf6S7YBEwtlr_dKAArwYc9MI4gvynQ5slmzbFJNNFKOgLTAtGOy-L7iUVoZqVQOnLTIiu7mCCEFlrBpnVZtww0hjeGHt8t8LIRUbwlrrjCnOzkpZtqxDnTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9bfa53b18.mp4?token=YZ42gLEdQyANTRVQN9s-8jSmTCGWiwnx1q5m91aJ_tYsdL5guebgnYtbIAkGnGkzmf-RsBEGsaaQYZUKOK5oHJ6e7ym83yADp5cIRByl8bKApFoX9lE0Vx5X866G4bsHN2LbRsk_2or5iJCA8iiC7vaUQrMWyMTv_vXfYkTTVBoCfurW4rpdHkRUhkbXi1FRQ0JqvhUzdJR99tzjFAXdpYnrkWWVTUrP4fL0DW_xwM_7n54XPtmTg9OVR3UkpON0bYpKm8AEAwZgko2Tog7zj43W7mb4UAic4aJ9A7cQjj0BbLoQBN92l1coOtohU3xAiXBQ4eFrevJjnF_urCF-D4t3HwgNeXRhG1fxn73ma0FLYun2Vin7I34-mViwBVP-7kVp02F6B1usQmwRgCUm-PemZlkhmOJ9klzyP2RmlT3plyC1Da7tNuk0cQzSZbMuIkSgr6fFufxBJi0oFREDu1Hzh2ZB_csCYu4QMNDXqamRuUg6TR5IqWTbeiPsV_cGuorQPNBB9ypZECdmrDT_L-IzqdNomYjGeziabl6mTG6i4GXjYaMBNf6S7YBEwtlr_dKAArwYc9MI4gvynQ5slmzbFJNNFKOgLTAtGOy-L7iUVoZqVQOnLTIiu7mCCEFlrBpnVZtww0hjeGHt8t8LIRUbwlrrjCnOzkpZtqxDnTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر از یک کشتی مسافربری که ارتش آمریکا آن را منهدم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/671701" target="_blank">📅 10:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671700">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVx1JRFzyY_cCHk84xb7PsYP-ksMxMPwJ-CWg82r9cG_icuNYdvL1y06qHqAJRD1_MiTRAHx-_0Vza50fSyIGoXC98KcjY6SdioUDQ6hGFqIDPZfu3mfeq3BHY0sngRrY1byzYXG4VeOWRM_8fK5JazbQGoQX2tSbuYX-imuzjNQ0zEwYjCOjz42siNmByLHtR6P1wr-CgN7LbL5D1v0p31zrhlH0-K1KaHkVDYMG4UXip7fbJLdvmSNYNOQ6iJ6AXVwguU7vl31654NUf81ddcC87dqxUbw0iEhJJXgwgXA8Ca3CO_R-wR1vsSHk2gCp8jCOK5GYgOPD-V41ZLJ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
کشف جالب مسی و یارانش از گلر انگلیس
🔹
بازیکنان آرژانتین پس از پایان بازی با انگلیس به‌طور اتفاقی بطری آب جردن پیکفورد را پیدا کردند. او تمام عادات پنالتی زدن بازیکنان آرژانتین را روی این قمقمه یادداشت کرده بود.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/671700" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671690">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m_o7oIX5XpavsLupQk0zGnN6ixnv5LE865VVD-W7Ado2dbPMxNm7A1pWMQgQd74Tn9GoRB3Dnutn38x_qSOR9j3hv0_pjDXfyO33zASWcTLKZ1SSfZnMoK2TRCHOnJBLcELKLvcvyufMErZaKSc5E4SjgGlsX3oor4WBpM5-gkcp2DAmvKUF11x-vbBrYglVFux7-2iuFHHakI9MRvHoukzFHuuT9VsmGQmNdHYvYa1Dq8gIvLpEF7_PnmPTzuPOaib1h5MJcS1jHbepIU3bsQueo7hF7tHW-vER2_TBRi2Ng7fKOinQGWDwwOUU6_pBk1VhZrSITeZlOly8ylTXxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mDsSxYaHhnaw9UQb9A0mi6sbTKNfQNFyLV1EklmM_HFWHnCmQvR4JGDDa2QWqQydyUqgGYbM93aAEbSK2i0C-f1s6GPCy0phDoRtJfLk-fllu1zDt-eUcw2scCXAYNgbgidnCdttLg1c02Pw8HGIN98vjxp1KKwMiPG2PfqxfL6dSVmH-YePMQDkzkPX_trx7ZP8gnCPby3d3m6Fw9DgKc9OTMnD33HHK1gAPMSozcoR1-gPXsQIdz5m5rYVYbhWJVpLv2OJlNHLzxjMyvQc54KUAkgh-alMzOc38l2BPhAfTniFYkd_rNA3IA5l7-UnptbHsdVSk7O3WOYiQTjWvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uyO7-3j_ibFcfNklyOONqcp4kbDBPB5S7drhtoCyb_djGC-BmCJV5MRJOhzw_Rzi0fv1WBIVODtyTUF_ZmlbQyQEyVWJ1FMV-QK3Yq8u6WYzLwIYJ_U2KjtWqSp_LczPrtDeXRJk1cgOQKbJCNnx3qu9-HADEBBenGFfpSrS6KSy9Hu9vSy5dxM6Oo22Oxi2NEtnnZFVHruoafNdU9e8d3yy0Tcwh1-Me9ZKJw9LYW-ksBwV4IJnQnnsIHnxhZ2TfaPovucjxwkT3MXgNFve6FQ1tzPRzt3ngFNSXzgU6B6ZuXPmG0zkplCBPD6OWiXe2j1kg6bFcAEVk2OdIpvTog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hE-7prwvPA69XbP73pd6EZSkKNBLOjpl7anyo8fd4jc2hu6dpn4t1GmCtx-VbfLCBMA5Ru3XvtS_4CzwxOn67KHkMRUluv0bxiCxyEbEw58VR0C7GaQZi2fFuyHkoZbeHDNiauUh7-FYoKboNDI5QubCiSCXcr9jYVbyNf2SRroURTd4DzsQeGtUksWO_bkN0iysAvfC7s3RHZR0rQHvniii3iOzwmBO165QYnMMoVWEA4kxvLNf-qPh1MjccRLDNR0ibrDBWh1cy36I0mDMVXcls1gR8RFDIDaRoGeysr0cuMXMkt4frma8k1gowOvVp4GHK1p04ocZbqThr196NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hMI2bKMOVoh6HUR8BG2WG-mMrn4kEMtCL8JIOBl_rQmkB7csHB-biu-2g7CNyC2orkNhdUEh-NrD_UqKtVrn6xor_JiTctixzmoszP0rtYP1ndJSM4BemvRSkcPwGSwLm6O5Bzd8C3VpkeqAVt2TX8MmVYZ-5jbDz2B7bIJZOrd1AsODKv-fy63vhzF8M_1h4Q5AUuwvcEb4dnDNmW7EgPhETeSdY3KA8DZizoxIs7xhx1556ukaYQkY4H0GUmAhQX50YWtapdP_7_u9UllYhTiuCaejtkhWud33borXwCy4-f5u1TLgZWwRQmheSJixYlxbpysUtIbW-jAw4XG4hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/idhip0qeiGqgx25pO_1Y92ieSjvbWEmyfnMsIB4DR3qRP9Kcuh08qsebITyEeOjHuPyVxAM4p_4iCHLg9VvgZoGd68c9yBYJuEpOeSgOW2UEPuUlHBZz7WGau2Y4q9f0XSa0ug0cHOJ06uHg-e2VQH53-eExL1_b_kXDHp99xT4CH2YGTESyThsXHdS3BY8DDS5Asy5frjmaN67MGELrXTYWLgNuTLR01YAdS9_JGx_JsxjU43mRF50n7JLkN1vtP3sHaw_4vyuW2MULOvL_emNPgf3JQDTB8rfvRY8n73uAPZ71qmApYFypFUF6ILNuYGt7xB7E8O03ex8fGAHhSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HVYx9G_6cOYGf9l-lvBjZRLEg7qeY2laYmCZm8oCelubXMEIAsXPYP-2b_o3GK2uIuDUY4OZHqDxUQwhq9KA3Kr_4WOvg9VSq217OL3_KLcdOEoZ5Mv5_y6QQ9PA5EqlrvXZMZtmpNVAH4G7p6yINCih7xByVhDYQfcWH-iXsRmS2AQja8mNn6qS2eBN5J42RCE7nsCBqtp47oTgtk5rYdg_AayTkoO4ufrKoDN0omh_x1FQnIVgMtIvzHsuuaeJQmUD5GIq_gUki85EKcf2kcEYLfmUTJ4CUnu90zOuHg1b52w6N_gZZ1S2r22NrbSGN2q3WCH6rdaSiuWyU_pDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N3ybDoRCU2zOWuqQhMGghbmcvIEU2J49FYqxcIfwmNJUfiv57H2JOMYUB_ZOCTbmxcEhEE81Bgiq9KW6RX7HgBHUYi-bMhAZWZabQ3DBshwcli35IRjEkOvSJfAUT5PhY83nAw7glXKFKAvh-0IZ36kBZOMPb6f3JifaETvnwbkI58dmRioUK6xZh_B6SjiyiHidEzMS1rPmPYl7ziH8e5GSUAzW9giOup-hdKf94TTK7BLAs7oAWzm14wbsNfUJv2Tq1YF96EoYiflYHq37_aCeamEHKoOc5JyDr4YXfTyoEmTuuUzlBDzhqVKmUnMqohmd5HOZMLC-qnnv_Dsnjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTdZbv4s046q47SgeIxkvCc7hhJRWnKOVnwwTowAbThTMFPhilD_hmetDoPSGogq9WASkFc5SRAhWQJsIV6y2pDmWKN85qndWUfh-rQn1-GlzZPiYG3-V-lgABkU2OGgHbLHJgqOiVPaAh0T-itPIhhjihFOlOPc_yROpwogu-Ki0KcO4KSG7RsYMBzDBNsu4kRPY0dig1gXRa_1pk2GOIugBLJ7pyXeNPpBxb689XsS42DbZMgHsx2l4b9Gl9NZVKfTbpY2ZRR7LQqMLozlJlngaTVjKvHZSVSrOqQziDRpizQdPfjihwjGI1qfFuBC9omuNpb_nb7kTVzB_hmrkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rnhJtXs8sXkOXbRRF0nEzXtnzE0QNmPGhyZpnjKha66Az64RVentjqw760QYkanr0pSKTkA87GcJhdMK-Ddne3OWJWJNhQ58L9DeWxcJN973NII2YojMA-5YLjoTqaJQ5yzVVQ31dSF4m1n0zi5vsHYXlSSJbyJItDbSvtRgtaYrBhskvzh_hDiPqNj952fr_8O4m41UNRzM3pHYphe0lS_byBirlF9trWBgelmuR9iR4io4JW-meJtuTG2-LBjdJbXnqLKHri4D7PxbnU4igjY3an9Pho_LPmIDXzsV4l2iG7zAFBFAXNf5W5QPOBdi-0OYVbJuaXD70sGDoco11Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بخشی از پیام‌های ارسالی مخاطبان خبرفوری در خصوص قطعی برق خارج از زمان مقرر
🔸
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/671690" target="_blank">📅 10:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671689">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
پاکستان خواستار خویشتنداری ایران و آمریکا در تنگه هرمز شد
🔹
سخنگوی وزارت خارجه پاکستان با تأکید بر لزوم بازگشت به وضعیت عادی در دریانوردی، از طرفین خواست با خویشتنداری، مسیر دیپلماسی و گفتگو را برای تأمین صلح و ثبات در پیش بگیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/671689" target="_blank">📅 10:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671688">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
سی‌بی‌اس: ترامپ از رد پیشنهاد توافق هسته‌ای ایران ابراز پشیمانی کرده است
شبکه سی‌بی‌اس:
🔹
دونالد ترامپ در محافل خصوصی، واشنگتن را به‌دلیل رد پیشنهاد تهران برای محدودسازی برنامه هسته‌ای مقصر می‌داند.
🔹
او معتقد است این تصمیم، فرصت کلیدی برای جلوگیری از گسترش درگیری‌ها را از بین برده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/671688" target="_blank">📅 10:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671687">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
بهترین دستور مرغ سوخاری رستورانی همینه، امتحانش کن
😁
مواد لازم:
🔹
سینه مرغ یا فیله مرغ
🔹
ارد ۱لیوان
🔹
نمک، فلفل‌سیاه و قرمز، پاپریکا، پودر سیر و پیاز
🔹
یک عدد تخم‌مرغ
🔹
نصف لیوان‌آب #آشپزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/671687" target="_blank">📅 09:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671686">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
سپاه: مرکز ارتباطات ماهواره ای و رادار هشدار اولیه پایگاه هوایی آمریکا در علی السالم و اسکله نظامیان آمریکایی در شعیبیه کویت منهدم گردید
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/671686" target="_blank">📅 09:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671685">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c61d032f9.mp4?token=SDvKgoRGJHZ3g40DrWIluP1lYl1DLfZBsHrXZxbuZ1QaFlJAEiUWfNXnCwFpP38S0S5_6qk7aI1CjEEsOEj2PMN5KqZzJ70wgYFUXbEij9Cex4gfXYJWGjQyYgJyB_GDBn50_7bNbHCfnIh6c23R3KCNS6zim1vbHS5hmM3x-24ELrCEIpkVtuN2IGJkQ3GOn2n8H-pQ5UrKKNfxAWYHJgT7qjmyJ_1u8L5ewpCKGZcgH4fG31N4fA2gAm_bdCjrgB8I-Xnqa3xiH58Nm6OM6NEAW_e_I7IhM2V1e0iFvfGKE33pRnKU3hjGl766a3W_I_nxJVJuXXz0Y4T5garJ8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c61d032f9.mp4?token=SDvKgoRGJHZ3g40DrWIluP1lYl1DLfZBsHrXZxbuZ1QaFlJAEiUWfNXnCwFpP38S0S5_6qk7aI1CjEEsOEj2PMN5KqZzJ70wgYFUXbEij9Cex4gfXYJWGjQyYgJyB_GDBn50_7bNbHCfnIh6c23R3KCNS6zim1vbHS5hmM3x-24ELrCEIpkVtuN2IGJkQ3GOn2n8H-pQ5UrKKNfxAWYHJgT7qjmyJ_1u8L5ewpCKGZcgH4fG31N4fA2gAm_bdCjrgB8I-Xnqa3xiH58Nm6OM6NEAW_e_I7IhM2V1e0iFvfGKE33pRnKU3hjGl766a3W_I_nxJVJuXXz0Y4T5garJ8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار قاطع سخنگوی قرارگاه مرکزی خاتم‌الانبیا: زیرساخت بزنید، هرچه زیرساخت در منطقه باقی‌مانده را می‌زنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/671685" target="_blank">📅 09:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671682">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33412fc12.mp4?token=KO42oax181Rgsrw7u6N8xPIh1IgkeGyCUOFAASxFQ7wi_05KR74zYvzspMwpOCgPPBa7Wr0flZBsPLFkM44KYTD4TGtmnXe8ubffaQ1HoXsAFoiHJqXVh-nP2fwn0iMYHa7h0oxvkGvdc7lI7UGcS5CoM01YZXJIa42qHXOPXFsCp48x4Omq3ltlVAdSXIg1hyLgRQtsNrIrNWAUx6ggW7DeXgKjQk-ZqeTGPacYxKJEKf7RaJvisC71t6bMgErBR81UZDSjJjnnl69aoNBKML6K_jSgnhrorFElEcxA_h8yKEBFxMCg2l1vDqIs8dNBlyoxE7UsZwTmmaMFpZnJhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33412fc12.mp4?token=KO42oax181Rgsrw7u6N8xPIh1IgkeGyCUOFAASxFQ7wi_05KR74zYvzspMwpOCgPPBa7Wr0flZBsPLFkM44KYTD4TGtmnXe8ubffaQ1HoXsAFoiHJqXVh-nP2fwn0iMYHa7h0oxvkGvdc7lI7UGcS5CoM01YZXJIa42qHXOPXFsCp48x4Omq3ltlVAdSXIg1hyLgRQtsNrIrNWAUx6ggW7DeXgKjQk-ZqeTGPacYxKJEKf7RaJvisC71t6bMgErBR81UZDSjJjnnl69aoNBKML6K_jSgnhrorFElEcxA_h8yKEBFxMCg2l1vDqIs8dNBlyoxE7UsZwTmmaMFpZnJhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیمه نهایی جام جهانی| کامبک رویایی آرژانتین با درخشش مسی؛ تعویض‌های تدافعی توخل کار دست انگلیس داد؛ آرژانتین رقیب اسپانیا در فینال شد
🔹
آرژانتین ۲ انگلیس ۱
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/671682" target="_blank">📅 09:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671681">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
سپاه: در «موج هشتم عملیات نصر ۲»، با استفاده از موشک‌های بالستیک «خیبرشکن»، رمپ جنگنده‌ها و مرکز فرماندهی ارتش آمریکا در پایگاه «الازرق» اردن مورد هدف قرار گرفتند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/671681" target="_blank">📅 09:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671680">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
سپاه: در «موج هشتم عملیات نصر ۲»، با استفاده از موشک‌های بالستیک «خیبرشکن»، رمپ جنگنده‌ها و مرکز فرماندهی ارتش آمریکا در پایگاه «الازرق» اردن مورد هدف قرار گرفتند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/671680" target="_blank">📅 09:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671679">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be48491e1.mp4?token=paVM5Uu3ELt-t4cLDhuwCFFzn0X56SYNwj9w1ZJvEul7mwGTn0rT_rm3WfFM4cdmh5wwpVAFLXp0j2l1LkgyBwrhAWklgot3szEGx2pni_e8mRR1nCZjtAiV5gBFDlDyWJq6Vuu8ypkFsfI6Abdc3AU9GNUip1rZdIZJAaRLqraaphTIiryBFkW4kfE40B5JajduOuGmQ2qN2yoXGKapcqSyx47wctjtx7WYzxWopL3RsxC5gK0bShEX4N7EwbTQB6R0J47_4eFF3MK5Uwn8kbqvdBLQIM3dJeKLA1LUG9vvv-IXddLw21GMThAZ91Xyb5BnDm623kbTd3wxk_b5cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be48491e1.mp4?token=paVM5Uu3ELt-t4cLDhuwCFFzn0X56SYNwj9w1ZJvEul7mwGTn0rT_rm3WfFM4cdmh5wwpVAFLXp0j2l1LkgyBwrhAWklgot3szEGx2pni_e8mRR1nCZjtAiV5gBFDlDyWJq6Vuu8ypkFsfI6Abdc3AU9GNUip1rZdIZJAaRLqraaphTIiryBFkW4kfE40B5JajduOuGmQ2qN2yoXGKapcqSyx47wctjtx7WYzxWopL3RsxC5gK0bShEX4N7EwbTQB6R0J47_4eFF3MK5Uwn8kbqvdBLQIM3dJeKLA1LUG9vvv-IXddLw21GMThAZ91Xyb5BnDm623kbTd3wxk_b5cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویرانی گسترده ناشی از حملات وحشیانه اشغالگران صهیونیست در شهر دیر البلح در مرکز نوار غزه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/671679" target="_blank">📅 09:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671678">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
آزمون کارشناسی ارشد ۱۴۰۵ با رقابت بیش از ۶۵۰ هزار داوطلب
آغاز شد.
🔹
پنتاگون: ماموریت ائتلاف در عراق در اواخر سپتامبر به پایان می‌رسد.
🔹
ونس: اسرائیل در نبرد افکار عمومی آمریکا شکست می‌خورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/671678" target="_blank">📅 09:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671677">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
سخنگوی ارتش: تنگه هرمز تا به رسمیت شناخته شدن نظام ایران بسته می‌ماند
🔹
امیر اکرمی‌نیا ضمن تأکید بر حق حاکمیت ملی بر تنگه هرمز، به همسایگان درباره عواقب میزبانی از پایگاه‌های آمریکایی برای حمله به ایران هشدار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/671677" target="_blank">📅 08:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671676">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
تکذیب شایعه حمله به ۵ نقطه استان کرمان
🔹
معاون امنیتی استاندار کرمان با رد گزارش‌های فضای مجازی، تأکید کرد در پی تحرکات اخیر در جنوب کشور، هیچ نقطه‌ای از این استان هدف تجاوز قرار نگرفته و اخبار منتشرشده کذب است.
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/671676" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671675">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
حملهٔ بامدادی دشمن به کبودرآهنگ همدان
استانداری همدان:
🔹
بامداد امروز نقاطی در کبودرآهنگ مورد حمله قرار گرفت که این حمله آسیب انسانی درپی نداشته است.
#اخبار_همدان
در فضای مجازی
👇
@akhbarehamedan</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/671675" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671673">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adefafbaf.mp4?token=MvPj54VqEv0tjgHELf6AO2iu0gbVwUEtaVkLwAKXiWVz3lqlSRJT1OoUSYiX6gi-oRqvdMda19kOh6xniojyZqqvUhPV-1mEcMzVMGhbyVJeDnAp4BWe-xBNhZSZFwzksxyOKvhAI_REsQxwL5Pzv-8Ee8v3PlzVNxGvmup1KeiohFbQjeftMODvuaC9S7DZM2o4fnvBm7lQF_R__DqLtegTH3Hao-8FaA0rlyzj4LJrYO1pFKaLDavMLyYroqitLtphaoePeTFbM_g-TjoleaD4u1Fb5YqzBxqdmJQwLrTBWUCfhKeECcdFKdVkrHnynhG4wIlMym9Uf58JbUOIpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adefafbaf.mp4?token=MvPj54VqEv0tjgHELf6AO2iu0gbVwUEtaVkLwAKXiWVz3lqlSRJT1OoUSYiX6gi-oRqvdMda19kOh6xniojyZqqvUhPV-1mEcMzVMGhbyVJeDnAp4BWe-xBNhZSZFwzksxyOKvhAI_REsQxwL5Pzv-8Ee8v3PlzVNxGvmup1KeiohFbQjeftMODvuaC9S7DZM2o4fnvBm7lQF_R__DqLtegTH3Hao-8FaA0rlyzj4LJrYO1pFKaLDavMLyYroqitLtphaoePeTFbM_g-TjoleaD4u1Fb5YqzBxqdmJQwLrTBWUCfhKeECcdFKdVkrHnynhG4wIlMym9Uf58JbUOIpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش‌های سیل‌آسا در شهر العین امارات
🔹
بارش‌هایی که در سال‌های اخیر به دلیل تغییرات اقلیمی، وقوع آن در این منطقه افزایش یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/671673" target="_blank">📅 08:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671672">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
علی اکبر ولایتی: تنگه هرمز متعلق به ایران است و هیچ قدرتی در دنیا نمی‌تواند تنگه هرمز را از مالکیت ایران خارج کند
مشاور رهبر معظم انقلاب:
🔹
این تنگه با فرمان شجاعانه و خردمندانه مقام معظم رهبری، حضرت آیت‌الله سیدمجتبی خامنه‌ای (مدظله‌العالی)، به‌عنوان یک دستاورد ارزشمند از جنگ ۴۰ روزه، تحت حاکمیت ایران قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/671672" target="_blank">📅 08:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671671">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
اعتبار کالابرگ سرپرستان خانوار دارای رقم پایانی کد ملی ۷، ۸ و ۹ شارژ شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/671671" target="_blank">📅 08:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671670">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
‌جزئیات حمله بامدادی آمریکا به سمنان  سخنگوی ستاد بحران:
🔹
بامداد پنجشنبه، بخش‌هایی از فرودگاه سمنان هدف حملات هوایی دشمن قرار گرفته است
🔹
خوشبختانه بخش‌های مسکونی در شهرها و روستاهای استان سمنان امشب شاهد حمله‌ای نبودند.  #اخبار_سمنان در فضای مجازی
👇
@Akhbar_Semnan</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/671670" target="_blank">📅 08:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671669">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
مرحله دهم عملیات صاعقه ارتش؛ پایگاه ها و مراکز آمریکا در کویت و بحرین هدف حملات پهپادی ارتش قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/671669" target="_blank">📅 07:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671668">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
وزیر علوم: کنکور سراسری در زمان مقرر برگزار می‌شود
🔹
برای برگزاری آزمون، هماهنگی‌های لازم از تأمین برق حوزه‌های امتحانی تا هماهنگی‌های امنیتی، با دستگاه‌های مختلف انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/671668" target="_blank">📅 07:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671667">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc6d27d3b9.mp4?token=DOyzYNe6N-xn2HuQpviccguUkAdxhxAZx7Ea-2QeFxN-S_wss_hazmy_mWQ6_hemz5lhUAjRQHY9Fu4Q5d4InQYFFDo85C2QVqa26zGTn4avReqPF_Rri99gh-k0m8O1rtB4lmgGcay_ObacCRmXKJX_g8alU8FZHvC9ZtPGKsyfb9a0UFG8umzpClz3ssdqEpMD3hov7OnyEFeK80QptVN0LpZScU-ChYsmkTxtLrloCvXfOQGKV9REo-QnvAJ2rGKWDjvA7ZsGQa_Y92-JfyBK-yAQCFLtDuz1EO-gWeliCftoFB7aPMa50VUhOtFCoBDKJWo-zWdmLutmypuyInKuFXKTOXtHAybqa_oG3C8QViTZ3ZWudagIf1jno31p4LlAioOVjQzCKiCjuFx9R-qC-mqwR2yjQfp7wyTqCH9OY3uqunmKrcPnt9OwnG8NwjB2t0e0b55dEqpA3oSwFfXD-wn8Y9DrTZVyRjsO44V5CPlOmMhVxyePyi1qKgo0i_VH1wyhiSuBlHEJrzemViDlrANgeUCEjdNxUngOtShYhcOEaGRLhnBgxX0Wf1JnidB8wNQLCp5BhEMH9NH0LvdNhGN8KTl4EF1MkdJRYnwP9Re0vFAnLFLLUeZQNm3zWK0WqC8u2B6abSJbKXAiU5M9De0sQH0elmD5YElyCg4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc6d27d3b9.mp4?token=DOyzYNe6N-xn2HuQpviccguUkAdxhxAZx7Ea-2QeFxN-S_wss_hazmy_mWQ6_hemz5lhUAjRQHY9Fu4Q5d4InQYFFDo85C2QVqa26zGTn4avReqPF_Rri99gh-k0m8O1rtB4lmgGcay_ObacCRmXKJX_g8alU8FZHvC9ZtPGKsyfb9a0UFG8umzpClz3ssdqEpMD3hov7OnyEFeK80QptVN0LpZScU-ChYsmkTxtLrloCvXfOQGKV9REo-QnvAJ2rGKWDjvA7ZsGQa_Y92-JfyBK-yAQCFLtDuz1EO-gWeliCftoFB7aPMa50VUhOtFCoBDKJWo-zWdmLutmypuyInKuFXKTOXtHAybqa_oG3C8QViTZ3ZWudagIf1jno31p4LlAioOVjQzCKiCjuFx9R-qC-mqwR2yjQfp7wyTqCH9OY3uqunmKrcPnt9OwnG8NwjB2t0e0b55dEqpA3oSwFfXD-wn8Y9DrTZVyRjsO44V5CPlOmMhVxyePyi1qKgo0i_VH1wyhiSuBlHEJrzemViDlrANgeUCEjdNxUngOtShYhcOEaGRLhnBgxX0Wf1JnidB8wNQLCp5BhEMH9NH0LvdNhGN8KTl4EF1MkdJRYnwP9Re0vFAnLFLLUeZQNm3zWK0WqC8u2B6abSJbKXAiU5M9De0sQH0elmD5YElyCg4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحله دهم عملیات صاعقه ارتش؛
پایگاه ها و مراکز آمریکا در کویت و بحرین هدف حملات پهپادی ارتش قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/671667" target="_blank">📅 07:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671666">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
گزارش سی‌بی‌اس از تدارک پنتاگون برای حمله به کوبا
شبکه سی‌بی‌اس به نقل از مقامات آمریکایی:
🔹
پنتاگون در حال بررسی طرح‌های حمله هوایی و تهاجم زمینی به کوبا با مشارکت لشکر ۱۰۱ هوابرد است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/671666" target="_blank">📅 07:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671665">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0I1oSSzID1YXjsC3ISpzDdyFLtzeUZIIVmpb6SCUoGIqtylJDRKprjF8omEfAaBBIyHEeo7ZKE-8U6eGKYSgRFDZ7FdMW-QvwXT6Iw-Ks9pHu2FEmZ15mQ4t3mtytZB7eWIaELbXCGHepcxa0CaHTTlL4vUP8mQOkiL5PRt-HzQ0k4s1yeMx167KN5jBK670awwqcSN0R-1ODrilDcKUIouvKWOl9_qvFG9liBdsWUakfcLsY6tps2dC6SqkkhIvlL96q9f1ZT1G02JDuee3v3UMo0Yrw4nIbXQ5oFAP1UuxdlwGYHS5-dQwTXGOb4kRTzUG7MGr9kRcF8W8xnWZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۲۵ تیر ماه
۱ صفر ۱۴۴۸
۱۶ جولای ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/671665" target="_blank">📅 07:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671664">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
صدای شنیده‌شده در خرم‌آباد مربوط به پاسخ موشکی نیروهای مسلح کشورمان علیه اهداف و منافع دشمن آمریکایی بوده، و جای نگرانی ندارد
#اخبار_لرستان
در فضای مجازی دعوت
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/671664" target="_blank">📅 07:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671663">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
خوک هار در پست جدیدی مدعی آزاد شدن یک جاسوس آمریکایی توسط ایران شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/671663" target="_blank">📅 06:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671661">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdf67f9770.mp4?token=lPwcM5iJUAGGz0qrocqBxMU-Z5w-IDlo2KkoPucTm4GW4ZgHxoiNvqi3Y-pcF7h3nOkxIj8AzQCDvLutK0iveYhryWPIb2SrzvGRboE0XdKlwvRDNrVkjpyRTr8dltB_6JDDmeWfT-NTQBCAav35t_FaSYiT5ynQb-A09W38z0z1O6eo02pL8NIHomMpjmEhrT1ykIMOvrmAWj5456I_g5FQhAxIVYEU2Q6-o0PULAwgd9xpp5iRbbvZFrd-qPiMvRJK-l7Dkln4sOMT1VvTofRUfJQqN6kgbouw_OrcAVPaSPHj1KHVJ34rsT4cXffyF5GNq2imfQNPYzEB-7PX5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdf67f9770.mp4?token=lPwcM5iJUAGGz0qrocqBxMU-Z5w-IDlo2KkoPucTm4GW4ZgHxoiNvqi3Y-pcF7h3nOkxIj8AzQCDvLutK0iveYhryWPIb2SrzvGRboE0XdKlwvRDNrVkjpyRTr8dltB_6JDDmeWfT-NTQBCAav35t_FaSYiT5ynQb-A09W38z0z1O6eo02pL8NIHomMpjmEhrT1ykIMOvrmAWj5456I_g5FQhAxIVYEU2Q6-o0PULAwgd9xpp5iRbbvZFrd-qPiMvRJK-l7Dkln4sOMT1VvTofRUfJQqN6kgbouw_OrcAVPaSPHj1KHVJ34rsT4cXffyF5GNq2imfQNPYzEB-7PX5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش جمهوری اسلامی ایران، ساعتی پیش در مرحله نهم عملیات صاعقه و در پاسخ به تجاوزات دشمن، سامانه‌های ارتباطی و مخازن سوخت ارتش تروریستی آمریکا در اردن را با پهپادهای انهدامی، هدف قرار داد
🔹
پهپادهای انهدامی ارتش جمهوری اسلامی ایران در مرحله نهم عملیات صاعقه و در پاسخ به تجاوزات دشمن کودک‌کش به  مناطقی از کشورمان و پادگان بمپور ایرانشهر که منجربه شهادت ۷ تن از درجه‌داران و سربازان نیروی زمینی ارتش شد، سایت راداری ثابت، سامانه ارتباط و مخازن سوخت ارتش تروریستی و کودک‌کش آمریکایی در پایگاه الازرق اردن را هدف قرار دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/akhbarefori/671661" target="_blank">📅 05:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671660">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۵/
رادار پیش‌هشدار سامانهء C-RAM در پایگاه علی السالم کویت و نیز محل تجمع سربازان جنایت پیشه ارتش تروریستی آمریکا آماج حملات ترکیبی قرار گرفت‌
.
روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
مردم غیور و بپاخاسته ایران!
در پی تجاوزات شب گذشته دشمن به نقاطی از سواحل و شهرهای جنوبی کشور، فرزندان دلاور و قهرمان شما در نیروی دریایی و هوافضای سپاه، در موج هشتم عملیات نصر ۲ بارمز مبارک یا زینب کبری (س)، در یک عملیات ترکیبی با استفاده از توان موشکی و پهپادی خود، رادار پیش‌هشدار سامانهء C-RAM را در پایگاه علی السالم و نیز محل تجمع سربازان جنایت پیشه ارتش تروریستی آمریکا را آماج حملات خود قرار داده و درهم کوبیدند.
🔹
بار دیگر به مردم شریف کویت یادآوری می‌کنیم که این جنایات توسط آمریکا با استفاده از خاک شما علیه ایران مسلمان انجام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/671660" target="_blank">📅 05:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671659">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار در سمنان
🔹
دقایقی پیش مردم در بخش‌هایی از سمنان صدای انفجار شنیدند.
🔹
هنوز محل دقیق و منشأ این انفجارها مشخص نیست.  #اخبار_سمنان در فضای مجازی
👇
@Akhbar_Semnan</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/671659" target="_blank">📅 05:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671658">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
روابط عمومی سپاه حضرت سیدالشهدا  علیه‌السلام استان تهران:  دقایقی پیش صدای انفجاری در محدوده شهرستان پاکدشت شنیده شد این صدا ناشی از عملکرد سامانه‌های پدافند هوایی در منطقه پارچین بوده
و
هیچ اصابتی رخ نداده است
#اخبار_تهران
در فضای مجازی
👇
@akhbarTehran</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/671658" target="_blank">📅 05:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671657">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
آمریکا مدعی پایان حملات به ایران شد
🔹
ادعای سازمان تروریستی سنتکام:
«در ساعت ۹ شب به وقت شرق آمریکا در ۱۵ جولای، موجی از حملات علیه ایران در شامگاه به پایان رسید».
🔹
این بیانیه ادعا می‌کند: «نیروهای آمریکایی به مراکز فرماندهی، سایت‌های پدافند هوایی، قابلیت‌های موشکی و پهپادی و تأسیسات نظارت ساحلی ایران حمله کردند».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/671657" target="_blank">📅 04:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671656">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
آسمان ایران بسته شد و تا اطلاع ثانوی پروازها لغو گردید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/671656" target="_blank">📅 04:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671655">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار در سمنان
🔹
دقایقی پیش مردم در بخش‌هایی از سمنان صدای انفجار شنیدند.
🔹
هنوز محل دقیق و منشأ این انفجارها مشخص نیست.
#اخبار_سمنان
در فضای مجازی
👇
@Akhbar_Semnan</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/akhbarefori/671655" target="_blank">📅 04:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671654">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
شنیده شدن صدای ۲ انفجار در خرم‌آباد
🔹
دقایقی پیش مردم در خرم‌آباد ۲ صدای انفجار را در این شهرستان شنیدند.
🔹
هنوز محل دقیق و منشا این انفجارها مشخص نیست و تاکنون مسئولین استان در این خصوص اظهار نظری نداشته‌اند.
#اخبار_لرستان
در فضای مجازی
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/671654" target="_blank">📅 04:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671652">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79545378d8.mp4?token=j08VSyMXJQ4gUonBaJFhyJoacG8xN3XT7OImzeccvctyZKdZBsgHQVjfbqD8UMw4yK1w1q1bp6RvQ3NhzGwa19-I2-uCqfRp9X3qPGIsbSAjRCXMznqUktDuKhWzkDE0xY3AxhRzrbCcTXfnRBqtvHCCoklUTfgJKYKl0VF1xpPYRPZs9myN96z-LQPifcG4kmy04J5WE4yeYcddf5nWLiwcgINumgwH2t9K-WPGFyAEk36pvyCTKNvTPgcqRemB1bSUdS0MTIRshkWXDR6Fe0bSg2N82qdpNYQXTc3Wh5PD-RFe7bMvL-k0P9yRxBtYDrIj-S5e5XMpZUfRXojKgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79545378d8.mp4?token=j08VSyMXJQ4gUonBaJFhyJoacG8xN3XT7OImzeccvctyZKdZBsgHQVjfbqD8UMw4yK1w1q1bp6RvQ3NhzGwa19-I2-uCqfRp9X3qPGIsbSAjRCXMznqUktDuKhWzkDE0xY3AxhRzrbCcTXfnRBqtvHCCoklUTfgJKYKl0VF1xpPYRPZs9myN96z-LQPifcG4kmy04J5WE4yeYcddf5nWLiwcgINumgwH2t9K-WPGFyAEk36pvyCTKNvTPgcqRemB1bSUdS0MTIRshkWXDR6Fe0bSg2N82qdpNYQXTc3Wh5PD-RFe7bMvL-k0P9yRxBtYDrIj-S5e5XMpZUfRXojKgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع انفجار در پایگاه‌های آمریکا در اردن
🔹
منابع محلی می‌گویند که انفجارهایی در پایگاه هوایی «موفق السلطی» در منطقه «الازرق» رخ داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/671652" target="_blank">📅 04:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671651">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
برخی منابع می‌گویند دقایقی پیش صدای انفجار در حوالی پارچین و پاکدشت شنیده شده است؛ این موضوع هنوز در دست بررسی است و تایید نهایی نشده است
🔹
گزارش تکمیل پس از ارزیابی‌ها متعاقباً اعلام خواهد شد. / تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/671651" target="_blank">📅 04:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671650">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
حملۀ دشمن آمریکایی به خنداب
معاون استانداری مرکزی:
🔹
در ساعت ۳:۳۰ دقیقۀ بامداد نقطه‌ای در خارج از شهر خنداب هدف ۲ حملۀ هوایی دشمن قرار گرفته است.
🔹
اخبار تکمیلی متعاقبا اعلام خواهد شد.
#اخبار_مرکزی
در فضای مجازی
👇
@akhbar_markazi</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/671650" target="_blank">📅 04:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671649">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
فعالیت پدافند در آسمان تهران برای مقابله با اهداف متخاصم / مهر  #اخبار_تهران در فضای مجازی
👇
@AkhbarTehran</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/671649" target="_blank">📅 04:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671648">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
یک فروند پهپاد MQ9 رهگیری و منهدم شد
روابط عمومی سپاه:
🔹
دقایقی قبل یک فروند پهپاد MQ9 دشمن در آسمان اندیمشک توسط سامانه نوین پدافند هوایی هوافضای سپاه رهگیری و منهدم شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/671648" target="_blank">📅 03:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671647">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
فعالیت پدافند در آسمان تهران برای مقابله با اهداف متخاصم / مهر
#اخبار_تهران
در فضای مجازی
👇
@AkhbarTehran</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/671647" target="_blank">📅 03:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671646">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
منابع اردنی از شنیده شدن صدای انفجار و آژیر هشدار در پی حملاتی از جانب ایران خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/671646" target="_blank">📅 03:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671645">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
رسانه عراقی: شلیک مجدد موشک از کویت به ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/akhbarefori/671645" target="_blank">📅 03:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671644">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
آسمان جنوب عربستان بسته شد
🔹
عربستان سعودی به‌دنبال حملات دوشنبه‌شب نیروهای مسلح یمن به فرودگاه بین‌المللی ابها، ناچار به تمدید تعطیلی سه‌روزه فرودگاه کلیدی جنوب خود شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/671644" target="_blank">📅 03:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671643">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c99c70405.mp4?token=HBRIxWR1hLLUjdN8tcbXKmCuvoI-MyPUq93NWiZ_TIGuFxsgg8YUnyTtLRQKAb45UsMl9ODbretR9etKKT7q-QK5lHowKSpXUdqf0NbtJZQ7S7gqri3mmZhYgx2YxqQYqd2E1kpbiFaVmFL17vbtt4ICHiJLIzHJUtvM4rNzRwDdobTskB61BoAXEcEXaN7mjMyOzo4VW8uSKd0G2OcffgUl6HQpF2QWFLL_lfOnXNm9eL3a4qTR-8qn1n6RcOr6GrwH3vbFWlMqSj-Uz2Ox4i7_jQvN5Jof3I57kHhSiz6vHf1qihyO2-1UNULCquMsLW1bIA_uA-y4l8i1ZidzEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c99c70405.mp4?token=HBRIxWR1hLLUjdN8tcbXKmCuvoI-MyPUq93NWiZ_TIGuFxsgg8YUnyTtLRQKAb45UsMl9ODbretR9etKKT7q-QK5lHowKSpXUdqf0NbtJZQ7S7gqri3mmZhYgx2YxqQYqd2E1kpbiFaVmFL17vbtt4ICHiJLIzHJUtvM4rNzRwDdobTskB61BoAXEcEXaN7mjMyOzo4VW8uSKd0G2OcffgUl6HQpF2QWFLL_lfOnXNm9eL3a4qTR-8qn1n6RcOr6GrwH3vbFWlMqSj-Uz2Ox4i7_jQvN5Jof3I57kHhSiz6vHf1qihyO2-1UNULCquMsLW1bIA_uA-y4l8i1ZidzEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصابت به مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/671643" target="_blank">📅 03:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671642">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ابراز نگرانی اسرائیل از فاصله گرفتن آمریکا از موضوع برنامه هسته‌ای ایران
المانیتور به نقل از یک منبع اسرائیلی:
🔹
همه چیز حول هرمز می‌چرخد. هیچ‌کس درباره مسئله هسته‌ای صحبت نمی‌کند. این بدترین نتیجه ممکن برای ماست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/671642" target="_blank">📅 03:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671641">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
اصابت به مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/671641" target="_blank">📅 03:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671640">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
گزارش‌ها از حمله به پایگاه آمریکا در بحرین
🔹
همزمان با فعال‌شدن آژیرهای هشدار در بحرین، محل استقرار نظامیان آمریکایی هدف حمله هوایی قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/671640" target="_blank">📅 03:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671639">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
‌ منابع خبری از انفجارهای شدید در بحرین گزارش می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/671639" target="_blank">📅 02:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671638">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f1d94e129.mp4?token=biTR6fcVDsY0SnqAD_UiBANsf0yGfuep0xSQMBKlfD50NqTUn6EvykuqDvIUT5Tb-u2KRb6BKsAplaD-3IFviA18VvTceqJr3oJR-r3wH3czOhozlV3hgrf0XmcuevqvJKhF5B5sil4mJRrahnrlbCS7MUNjbP8_bUrV6jgjtLotFD2rZFiZnmLKXAgIW3qRGOmW5MxaOr01ANcvVy8MAfVeEcTKqg0g80PKdJRptxfeRXacpQGLHmjparByYNyY0ApGkCyIUaNR35i0jLtAxnYn4_z0gHNTWwx09FE8NAPaRIJVMf4sqAdvHDb8UhAZk6T02zsQrjVJYhg-BtcoOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f1d94e129.mp4?token=biTR6fcVDsY0SnqAD_UiBANsf0yGfuep0xSQMBKlfD50NqTUn6EvykuqDvIUT5Tb-u2KRb6BKsAplaD-3IFviA18VvTceqJr3oJR-r3wH3czOhozlV3hgrf0XmcuevqvJKhF5B5sil4mJRrahnrlbCS7MUNjbP8_bUrV6jgjtLotFD2rZFiZnmLKXAgIW3qRGOmW5MxaOr01ANcvVy8MAfVeEcTKqg0g80PKdJRptxfeRXacpQGLHmjparByYNyY0ApGkCyIUaNR35i0jLtAxnYn4_z0gHNTWwx09FE8NAPaRIJVMf4sqAdvHDb8UhAZk6T02zsQrjVJYhg-BtcoOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش‌ها از حمله به پایگاه آمریکا در بحرین
🔹
همزمان با فعال‌شدن آژیرهای هشدار در بحرین، محل استقرار نظامیان آمریکایی هدف حمله هوایی قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/671638" target="_blank">📅 02:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671637">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
معاون رئیس‌جمهور آمریکا: تامین امنیت مسیرهای دریایی فقط با استفاده از ابزارهای نظامی بسیار دشوار است، زیرا هدف قرار دادن کشتی‌ها با استفاده از پهپادهای ارزان‌قیمت بسیار آسان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/671637" target="_blank">📅 02:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671636">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
گزارش‌ها از حمله به پایگاه آمریکا در بحرین
🔹
همزمان با فعال‌شدن آژیرهای هشدار در بحرین، محل استقرار نظامیان آمریکایی هدف حمله هوایی قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/671636" target="_blank">📅 02:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671635">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
گزارش‌ها از حمله به پایگاه آمریکا در بحرین
🔹
همزمان با فعال‌شدن آژیرهای هشدار در بحرین، محل استقرار نظامیان آمریکایی هدف حمله هوایی قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/671635" target="_blank">📅 02:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671634">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
استانداری هرمزگان: در ساعت ۲:۲۰ نقطه‌ای در حوالی بندرعباس مورد اصابت حملات دشمن آمریکایی قرار گرفت. / فارس
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/671634" target="_blank">📅 02:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671633">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qn_c3o5OQYKxdEnPyR1nclc_lTVW392u7SCAMUtfXhLjU90KSG6r0L3llROgbcGpcdRDns2XXZi9m3DBQcTOQamJAiLzkvl96cvUb6Jjt_pBuWGSHwr1e4HXLJN5zUIInmC0XovY5535wvVK7HeGS_l0rXuuOPKwfZm0O7IPDSS2LmEP_HdfbMbyTd7SnsIKD1SCNsJh51Dzf71y9kVobKjE2JayUjxuLSEf4cvkIFlFt5CWzDjC1w70FL2J-X3PTKh_XFAmzlKUyCOtUTpesDmbjAtck4rx6ngALWkPcisL5dnWDbxLIKRzkjcArB-RbIX0UdfUlLlq7M3R-fLqOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به یاد سربازانی که دیگر بازنگشتند...
#بمپور
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/671633" target="_blank">📅 02:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671632">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ادعای خوک نجس در مورد آزادی شهروند آمریکایی توسط ایران
🔹
ایران به یک شهروند آمریکایی که در دسامبر ۲۰۲۴ در زمان ریاست جمهوری جو بایدن به ناحق بازداشت شده بود، اجازه خروج از کشور را داد. او اکنون در خارج از ایران و در وضعیت خوبی به سر می‌برد.
🔹
ایالات متحده آمریکا از این حسن‌نیت ایران قدردانی می‌کند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/671632" target="_blank">📅 02:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671631">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
اصابت مستقیم حملات هوایی انتقامی ایران به منافع آمریکا در کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/671631" target="_blank">📅 02:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671630">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
تکذیب اصابت مجدد در قشم توسط استانداری هرمزگان
استانداری هرمزگان:
🔹
در جزیره قشم بعد از اصابت پرتابه به کارخانه پودر ماهی سوزا برخورد جدیدی گزارش نشده است. شنیده شدن صداها احتمالا دارای منشاء دیگری بوده باشد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/671630" target="_blank">📅 02:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671629">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
مدیر بیمارستان شهید بقایی اهواز : پس از حمله تجاوزکارانه آمریکای جنایتکار به اطراف بیمارستان، موظف شدیم ۲۱۱ بیمار بستری را جابه‌جا کنیم
🔹
تمام تخت ها و بیماران بیمارستان شهید بقایی ۲ به علت وقوع شرایط اضطراری تخلیه شدند.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/671629" target="_blank">📅 02:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671628">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1c09abf4.mp4?token=BnqE-rOS2ggUpvAy-QHwEeo6oRn9edijje9g80qOk6KK7zKHBeqfOyaBrIJEtIsv3BERw5NpH5oe4NlkjD2sgTzs3Vme82Z_WxKzlFicGtJm9KeaCiTP7ZIx60SFOrEX4nSjTk0ubLWQrw37W_qyO_6Xm2FLQh4LKU0qfYvJ6C7oyHxMGaLy-LwWBc1v8imFsse6kHZxJj2mRxfir0xee2Cn9cMn_a59HgbKYQ6bgzkblEA_qDaiywzRNDGh726NeK9R01h4QYmpUVLHpZTI1Fcq7Xk1eKc6p1FRonDm0C9nBBCskjj84Av68PgdIeHaj6lMbBv9G4ZmrWvN9_kJRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1c09abf4.mp4?token=BnqE-rOS2ggUpvAy-QHwEeo6oRn9edijje9g80qOk6KK7zKHBeqfOyaBrIJEtIsv3BERw5NpH5oe4NlkjD2sgTzs3Vme82Z_WxKzlFicGtJm9KeaCiTP7ZIx60SFOrEX4nSjTk0ubLWQrw37W_qyO_6Xm2FLQh4LKU0qfYvJ6C7oyHxMGaLy-LwWBc1v8imFsse6kHZxJj2mRxfir0xee2Cn9cMn_a59HgbKYQ6bgzkblEA_qDaiywzRNDGh726NeK9R01h4QYmpUVLHpZTI1Fcq7Xk1eKc6p1FRonDm0C9nBBCskjj84Av68PgdIeHaj6lMbBv9G4ZmrWvN9_kJRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصابت مستقیم حملات هوایی انتقامی ایران به منافع آمریکا در کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/671628" target="_blank">📅 02:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671627">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc0678b866.mp4?token=pg7Eyf1cZ29OJajhQBKPL04NFEHZCvagfiXjsUFVOyR95SArdvjmZs3DhjGsaE4AVYI__D12I_QjWMSSXGTjOHzEscEOknxoOv20HI0qabaqnfrU2lUJk9YCi58SuGD9TzY8Aq1B0fb4fsr70EDpvgNyItYIhpF3lxx5diSOEbIp_SxzYQ7oO9g_S7qehhPAr7sT4dMc9Kd1rDYy5szwMV7QzgfI9fnISQvGemNMVkOkuON6HWxDElawbb-2sMgjAN1jiDRzmdiLFtSlK7MsicVON4Jfax02PjYHL0NLqGgpCAe4zL2bY3zYFMoQH-QWWAaC-Q9C9zZCnFd6zT4Zwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc0678b866.mp4?token=pg7Eyf1cZ29OJajhQBKPL04NFEHZCvagfiXjsUFVOyR95SArdvjmZs3DhjGsaE4AVYI__D12I_QjWMSSXGTjOHzEscEOknxoOv20HI0qabaqnfrU2lUJk9YCi58SuGD9TzY8Aq1B0fb4fsr70EDpvgNyItYIhpF3lxx5diSOEbIp_SxzYQ7oO9g_S7qehhPAr7sT4dMc9Kd1rDYy5szwMV7QzgfI9fnISQvGemNMVkOkuON6HWxDElawbb-2sMgjAN1jiDRzmdiLFtSlK7MsicVON4Jfax02PjYHL0NLqGgpCAe4zL2bY3zYFMoQH-QWWAaC-Q9C9zZCnFd6zT4Zwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کجایی مرد؟!
کجایی…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/671627" target="_blank">📅 02:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671626">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9iZA-aNExcKq3rz4eGX8UJX0ar8o4irVB4K7OCvxfao9w1Z56rJXCSK9Tk6e5_TI37wR0I6wEBbeDiPgTpjHvx3P07vG-Us8SRFor7u2wgu9JK9Vq_wZiKm8FU1yW45WbCy77u1D970UO59-0CjZBf_j3KQABywVJUDOb9m7Y90-8_2Ohji41qWq94TMBR4gv3oDadsdWV17YXZulXhWnDS5bK_0DbOWHZBIH2STUDBsI4ZmAWDKDwX0Olf_9OWB1bRw-aUxrmo8aYt64sXaRAc8hkZUbDaHzdqeDovA_-pA5Xm9tvlXfWxMylpSG0hjv2Ajh5PXvs1uNqt5JzUyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه انگلیسی زبان DD_Geopolitics: اطلاعات جدید تأیید می‌کند که ایالات متحده یک بیمارستان سرطان کودکان در اهواز را هدف قرار داد!!
🔹
آیا ۱۶۸ کودک در میناب و صدها کودک دیگر کافی نبود؟! چرا اسرائیل و ایالات متحده مداوماً به کودکان آسیب می‌زنند؟!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/671626" target="_blank">📅 02:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671625">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
وزارت خارجه آمریکا فروش تسلیحاتی به عربستان و کویت را تأیید کرد
🔹
آمریکا با فروش راکت‌های ۷۰ میلی‌متری به عربستان و فروش خدمات پشتیبانی نگهداری، تداوم عملیاتی و حفظ آمادگی ناوگان هواپیماهای ترابری C-17 به کویت  موافقت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/671625" target="_blank">📅 02:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671623">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f178abbd0.mp4?token=R4eaHyw26cCwx_j1jC7gDnCrbHSt82qVQpzxLcmy91XWvTY3eVkQfieQI18vYav9_c2uUwNhZuARUszz18_xgsD3dwlO9rUMHFlbsekYEy7sPr3CbteyDrhMWslTWFtLJ3KBqHMd8vt1BYo_yt1r_GKuoQWiE_NfWAU9NlmJqdMTMWh3iQra7uSlcc9h5CNcN9KnAjDnoyej19oa-rO3HkZmW7AXBzL2xZr2pqihZ1P3-3MinKmcHsUykNqEZBnCMPEQ4ccpFQF5olLTyTx17J_pW4BpHpIOjklzT9RrplWRWr6hNZo0ydwMhI7sZcIN6KArDH16qvdqtpy37Bt7vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f178abbd0.mp4?token=R4eaHyw26cCwx_j1jC7gDnCrbHSt82qVQpzxLcmy91XWvTY3eVkQfieQI18vYav9_c2uUwNhZuARUszz18_xgsD3dwlO9rUMHFlbsekYEy7sPr3CbteyDrhMWslTWFtLJ3KBqHMd8vt1BYo_yt1r_GKuoQWiE_NfWAU9NlmJqdMTMWh3iQra7uSlcc9h5CNcN9KnAjDnoyej19oa-rO3HkZmW7AXBzL2xZr2pqihZ1P3-3MinKmcHsUykNqEZBnCMPEQ4ccpFQF5olLTyTx17J_pW4BpHpIOjklzT9RrplWRWr6hNZo0ydwMhI7sZcIN6KArDH16qvdqtpy37Bt7vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شلیک ۶ موشک از خاک کویت به ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/671623" target="_blank">📅 02:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671622">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sh8mXsOFzPjdxHhDoRYVWOre9jWkQqOofHqhV264E_OFtJjiwSES38IGDlXHKZjsmWjieNGWdgrckCcXJr07-VG80YMw-PobnOHJfQrn9mAjwKMMflUfoCSPnAV9BkAZrN_W2HymsEb2koHDq3iMnO2fDnROrE00-ECqBCCKPKtGxiPJn4ywdBHd_xqc6xyjsG8-12JXZbWfnzlNO8Y2QNAIRJ5QrfoJDDeMqr1cWDyw6C-W0_xHhjq1vacMY27H_jT1TQ_EwJfzEGKP-sPZcr8hcQxd8sci4YM9Ex5IfJu7KkuN5Xa6NnW_dsMfgCj3E-MP-CnjVGYigyt0dltlUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ریچارد مدهرست روزنامه‌نگار بریتانیایی : هنوز نمی‌تونم بفهمم چطور یه کشور دیگه رئیس کشورت رو ترور می‌کنه و تو هنوز باهاشون حرف می‌زنی
🔹
این یه مسئله حاکمیته. چطور این به عنوان یه خط قرمز مطلق در نظر گرفته نمی‌شه؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/671622" target="_blank">📅 01:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671621">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
استاندارد هرمزگان: خسارات محدود در برخورد پرتابه دشمن به بخشی از یک کارخانه تولید پودر ماهی در قشم / مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/671621" target="_blank">📅 01:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671620">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
وقوع چندین انفجار در کویت
🔹
منابع محلی بامداد پنجشنبه از حمله به منافع اقتصادی و تأسیسات آمریکایی در کویت خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/671620" target="_blank">📅 01:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671619">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doz1VAQpp97thcH9UFPQxy9oq41zzoidCIbvMFt5YAg4siKE3KVFYaDfjTNDHhwimP0wFMHnpK-pXUrYaTYxPTg-qAvqXSlI6xBFxmUJBLc6URMW3ARpFaS2Ij6LtQiM-1EdLiLLTM1uXg2yHJJeASr6SELxZJUgm10tAFvJ94Cv2NHeGyPH3WbgT0njhL_zev_oxMJpfOeWylos9CJnBuwVKagakzaKrKN2MloUhW4AVwbvr0GCeQKHNQRVegPk6nf1anitynUimVyKeQOmGZkJy90j7kVny3d34PIXWllZBnW3Kx_pv1wup2H-D0fkns205P93-xZsdMI_IJ132w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: ایران تاکنون به تعهدات خود پایبند بوده است؛ برخلاف آنچه وزیر خزانه‌داری آمریکا انجام می‌دهد که با نقض بند ۹ تفاهم‌نامه، تعهدات خود را زیر پا گذاشته است
🔹
واقعیت این است که اجرای تعهدات تنها زمانی امکان‌پذیر است که هر دو طرف به‌طور متقابل به تعهدات خود پایبند باشند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/671619" target="_blank">📅 01:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671618">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDbnOuOcmrmPVzc2pd_HS3cOmkrv9d1w0ZEjplXLZ_o72s5OncfbVy4TiSh2uoU_VwHJA9zPKFaEp8XDbamQa3GDRGm0dfeJpYFer2UN5YUv3iP1W3foob-aaHeVa1t_aez7GNHuG1VokyDw2AKVlPNZFKjwYS0S6LBEnpmWBJHCCKQUB9hZMT4b0bqfNN7bCGgvX7MvfPWfwUjnLaalzD1q5SuyLZ9irtmp8bofOsv8ywuXO1bh8VOOck2l4L_L5ombFYJLDlGTyzYaswLYqrC5_E-5kuXXSJAc27o6s-2Uck7EtArivHefEXR-jqaj6H6Bpy65IEQYEmf2PeiBvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی سپاه: دشمن تصور نکند که می‌تواند جنگ را فرسایشی کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/671618" target="_blank">📅 01:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671617">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
اصابت مجدد پرتابه‌های دشمن به نقاطی در سیریک و بندرعباس
🔹
دقایقی پیش پرتابه‌هایی به بندرعباس در مرکز و سیریک در شرق هرمزگان اصابت کرد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/671617" target="_blank">📅 01:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671616">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qhk1IKmLPQG2LcgdPeEdb0lpDjaSBVTPy0HdqH_3y80RykvuS3cMleRV4xewqn1EGYoaMF2_pHwzL5sPzOQGMYykxOrcEEQl9iPUFyKjas1orlTOjVhheGvQAYjtTYf-63oOtoKUoXWgjAwlRq0lZ3ExPiqdFI2AeJotgI0ifZvjEcYnfwoHcuT1kMqObR6z6jEaAjj_l9vOAOLingmHna0BvzQXJLV9Y_5MiHKTucLIEUxszcztrZMEi-LXfEl7Yj3BUXnU8BAuYaLeUNV0-Gpy-KHCB27G9H8jeC2D10IXOf7MjkERsHvW0DpVN1rC1-CxY_jKZ0YhHYTE13kc3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر آمریکایی : دوباره می‌خوان تقصیرش رو بندازن گردن هوش مصنوعی؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/671616" target="_blank">📅 01:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671615">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
اصابت پرتابه دشمن آمریکایی برای دومین بار در حوالی سیریک
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/671615" target="_blank">📅 01:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671614">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGA0GIQrVBPfCOFj5psfRjMloaAHVBHPueU1rbaaUuIVl-pCbxe3_gr_tH8S6uixZQMHu02VBvXsDcySGmeSvvIh9lzmxKi_1zQabBV2nibZugUmn3Su_IPkkgItsaHEZyhQqxaimnHBrHhoD0cYWMILbbxY-uivYgMUq68mr7rRl6Wpf42KFueNkj1QD2UntmXKbgUSOwoC6zaYNuHW5Mbd9FkNBqr7f3uK4-gs0XiYJjGJ5q41T2rI8U3C4EzCK6RMRJCX6aFElldloAQxCyyLzE0yApLkEc_t3kVSbZhLnerOi-CEZ8H0RQkz7fewdaSTAb234SsXuG7bLva48A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تشدید فعالیت هواپیماهای آمریکایی در منطقه
🔹
فعالیت هوایی آمریکا هم اکنون بر فراز منطقه تشدید شده است؛ به‌طوری که ۱۰ فروند هواپیمای سوخت‌رسان از نوع KC-135R و KC-46A، به همراه یک فروند هواپیمای هشدار زودهنگام E-3G (آواکس)، در آسمان منطقه در حال پرواز هستند. / تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/671614" target="_blank">📅 01:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671613">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
در پی حملات دشمن بیمارستان بقایی ۲ دانشگاه علوم پزشکی اهواز موقتا از چرخه خدمت خارج شد
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/671613" target="_blank">📅 01:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671612">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهایی در بندرعباس
🔹
ساکنان محلی از شنیده شدن صدای انفجارهایی در شهر بندرعباس خبر دادند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/671612" target="_blank">📅 01:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671611">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
فرمانداری راسک: مردم از ترددهای غیرضروری پرهیز کنند
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/671611" target="_blank">📅 01:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671610">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
صدای انفجار در قشم شنیده شد
🔹
دقایقی قبل صدای انفجار در جزیره قشم شنیده شد و موضوع در درست بررسی بیشتر است./ ایرنا
اخبار لحظه‌ای حملات امشب
👇
khabarfoori.com/fa/tiny/news-3230721</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/akhbarefori/671610" target="_blank">📅 01:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671609">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
اصابت پرتابه دشمن آمریکایی در حوالی سیریک
🔹
۵۵ دقیقه بامداد پنجشنبه نقطه ای در حوالی سیریک مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه متعاقبا اعلام خواهد شد./مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/akhbarefori/671609" target="_blank">📅 01:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671608">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ارتش: تنگه هرمز تا پذیرش نظام قانون‌مند ایران از سوی آمریکا بسته می‌ماند
سخنگوی ارتش:
🔹
تا زمانی که آمریکا نظام قانون‌مند ایرانی را نپذیرد، و سازوکار مبتنی بر اراده ایرانی بر تنگه هرمز حاکم نشود این تنگه بسته‌ خواهد ماند.
🔹
تمکین آمریکا به مفاد تفاهم‌نامه، دست برداشتن از شرارت‌ها و دشمن‌ستیزی، و حاکم‌شدن قوانین ایرانی راهکار بازگشایی تنگه هرمز است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/akhbarefori/671608" target="_blank">📅 01:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671607">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cced705f5.mp4?token=Zm3DxvCVZTXaZjpGV9QBvKkvE9nMvRuUXWXvPIXUufHKWOFLG9_XGrEYEYmG10dbK5IRgPUTcZ7ZBO5t2wjku6z5hSbZsjSPEVpGmavRseQSukAD7K3lp72XOuL2sxy53su3Zi-UPrDDhRW-3A09Cwxbb_Rx8b8t4630SNMDr0CDPBO9ia7u9RSujgqZBMokvsnYawlFB-QuZkw1EE7SGU7ZinJhEaMMi5g_p8IVLMzivPXZ07uiN9WmcWWSIlhAgBMcI3hEhwuImJ5S1XseOqJB5-aEmcinugvEJpPKj3cOrCMECBgVApYukmBKwPZQXHvICtUufpU7670UGsTawQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cced705f5.mp4?token=Zm3DxvCVZTXaZjpGV9QBvKkvE9nMvRuUXWXvPIXUufHKWOFLG9_XGrEYEYmG10dbK5IRgPUTcZ7ZBO5t2wjku6z5hSbZsjSPEVpGmavRseQSukAD7K3lp72XOuL2sxy53su3Zi-UPrDDhRW-3A09Cwxbb_Rx8b8t4630SNMDr0CDPBO9ia7u9RSujgqZBMokvsnYawlFB-QuZkw1EE7SGU7ZinJhEaMMi5g_p8IVLMzivPXZ07uiN9WmcWWSIlhAgBMcI3hEhwuImJ5S1XseOqJB5-aEmcinugvEJpPKj3cOrCMECBgVApYukmBKwPZQXHvICtUufpU7670UGsTawQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آمریکا مدعی حمله به یک نفتکش در مسیر بنادر ایران شد  نهاد تروریستی ستاد فرماندهی مرکزی آمریکا (سنتکام):
🔹
ما امروز یک نفتکش خالی را که قصد داشت به سمت یک بندر ایرانی در خلیج فارس حرکت کند، از کار انداختیم.
🔹
این کشتی هشدارهای متعدد را نادیده گرفت در حالی…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/akhbarefori/671607" target="_blank">📅 00:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671606">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/494055b9e4.mp4?token=jj2s6ehbyLS4w1yZhdjqhvNB5MnzOYJValvJUrLjCKfvGQlM79gAOydzxz6Ik_YL53jQ0MkuLCBCXIQDiHLkbWyNyWl66R-MiZUJM2zJiFo2jAaR0ff0aRTRrPs-znuqhlWdFq9LIjlzzzHesJP-gxmqZZHi_Hvn76SRj58GoqBdeWr_ndq5yticlYx8WviTwRao-K0PgGtiryeO866qiNzzbFs7XiFRsGAztDU0csXXhba6tHvoub5s5PaFXldOKSZ6sFNzrYZt-HKBmDqrdmtxZQ90p0xkg1U4pORhi3mQ9cH8LS_i24XnWxpQZKyf2DwxK7xn5miwckYJqRTTJIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/494055b9e4.mp4?token=jj2s6ehbyLS4w1yZhdjqhvNB5MnzOYJValvJUrLjCKfvGQlM79gAOydzxz6Ik_YL53jQ0MkuLCBCXIQDiHLkbWyNyWl66R-MiZUJM2zJiFo2jAaR0ff0aRTRrPs-znuqhlWdFq9LIjlzzzHesJP-gxmqZZHi_Hvn76SRj58GoqBdeWr_ndq5yticlYx8WviTwRao-K0PgGtiryeO866qiNzzbFs7XiFRsGAztDU0csXXhba6tHvoub5s5PaFXldOKSZ6sFNzrYZt-HKBmDqrdmtxZQ90p0xkg1U4pORhi3mQ9cH8LS_i24XnWxpQZKyf2DwxK7xn5miwckYJqRTTJIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت بیمارستان شهید بقایی اهواز پس از حملۀ آمریکا
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/akhbarefori/671606" target="_blank">📅 00:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671605">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b35b61078.mp4?token=gGxNRp_b80agWkv2oloM9uL-bWU7U8i6gexRs5l3yMCqJd_su1CjcacFYnQEMy3OwPxPqhR2njjnUneH5CKERkYEmpNCuMf_uyJBMbLeXoeElc4E7a1qie59PS3ueptuvhteT97ahC8fVtcD_v2E3AxJR3-4JTWSOdhuzlLHGDyK-Vbq7Q6yCYwbPSysIqQF8sA119mB846h-2OIdVc7QUi1QKLJ6o05oWTZll_doZIn0eWws5SbU6eMDuYrX2wFVCGxXIr5eS88_OvtnO2TtO2xgxYl9r_yFBNCSjLF5Mtf4IffCNmpIWDSys25OpdKdtDqmBSf_aiI-bjuPX1NjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b35b61078.mp4?token=gGxNRp_b80agWkv2oloM9uL-bWU7U8i6gexRs5l3yMCqJd_su1CjcacFYnQEMy3OwPxPqhR2njjnUneH5CKERkYEmpNCuMf_uyJBMbLeXoeElc4E7a1qie59PS3ueptuvhteT97ahC8fVtcD_v2E3AxJR3-4JTWSOdhuzlLHGDyK-Vbq7Q6yCYwbPSysIqQF8sA119mB846h-2OIdVc7QUi1QKLJ6o05oWTZll_doZIn0eWws5SbU6eMDuYrX2wFVCGxXIr5eS88_OvtnO2TtO2xgxYl9r_yFBNCSjLF5Mtf4IffCNmpIWDSys25OpdKdtDqmBSf_aiI-bjuPX1NjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشارکت کویت در جنگ تحمیلی آمریکا علیه ایران
🔹
رسانه‌های عراقی با انتشار تصاویری،‌ گزارش دادند که کویت با پرتاب موشک از خاک خود به سمت خاک ایران، در جنگ آمریکا علیه جمهوری اسلامی مشارکت دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/akhbarefori/671605" target="_blank">📅 00:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671604">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
امتحانات دانش‌آموزان بوشهری لغو شد  مدیرکل آموزش و پرورش استان بوشهر:
🔹
با تصمیم ستاد عالی آزمون‌های وزارت آموزش و پرورش امتحانات نهایی روزهای ۲۵ و ۲۷ تیرماه، در این استان لغو شد.  #اخبار_بوشهر در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/akhbarefori/671604" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
