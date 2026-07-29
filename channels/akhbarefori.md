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
<img src="https://cdn4.telesco.pe/file/hkrjOUuyViZ1jjCuqIc5TQOzPN2GPYLfNrJcxx3WrsjQ6BUhD-liLfk7oKMaTa7UT4PFsaTSDkP1VwKdpuJeZUXITLCuOy6OUskod1Aj8PxSJZbXhQDxi8AzkM4b6CCvop4PhEmAoMaX6RG-usuhJFJHzTr2VO8eU3SYr794TUtkLLr75ub0se212NSQkwsBmU5UBljNcRDXs3OcAp3khcL_gII6deVcw1vaK69EmXV9kBucpevIIm2nJQbZxJndjdo1kIKc8uN8obIQV1vf4dfMnlo4q39LeXGZ2I44xv7DEtIxHj_GbG92M6b23t19xyouISdl7NlZQFLDKElZJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.16M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 03:23:57</div>
<hr>

<div class="tg-post" id="msg-676519">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
حملات تجاوزکارانه آمریکا به نقاطی در ایران
🔹
خبرنگار صهیونیست وبگاه «آکسیوس» بامداد پنجشنبه به نقل از یک مقام آمریکایی خبر داد: «ارتش آمریکا در حال انجام حملاتی به ایران است».
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/676519" target="_blank">📅 02:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676518">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
پیشنهاد سنتکام به ترامپ برای حملات دو هفته‌ای به ایران
نشریۀ وال‌استریت ژورنال:
🔹
فرماندۀ سازمان تروریستی سنتکام طرحی را به رئیس‌جمهور آمریکا پیشنهاد داده که ذیل آن، تا دو هفته به زیرساخت‌های موشکی ایران حمله شود.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/akhbarefori/676518" target="_blank">📅 02:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676517">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
چند انفجار شدید اربیل عراق را لرزاند
🔹
به گزارش، شبکه اخبار عراق اعلام کرد که پس از شنیده شدن صدای این انفجارها، ستون‌های آتش و دود از منطقه قسری در اربیل به آسمان برخاسته است.
🔹
براساس اعلام رسانه‌های عراقی، هم اکنون سامانه‌های پدافندی کنسولگری آمریکا در اربیل نیز فعال شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/676517" target="_blank">📅 01:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676516">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjCXb3aBdhceoPe6i5T6J3xziAt5H5mCgR6NPiKgVVn16GH_Ziz5DTrqR9K1ifbtXdc3bQ0YNKcexeYldy6Zc1gVzfXr81o9gRMoCXQ6lZDdwKGtSdVHoEjO4WrO1dbjnemhBEwe-LwM-SYZGwKdYNunIfNNGuhTKLcSjL0aLUD4CegXl-AGDRG_t148GrlDhyYTuEVDhZ3XU7FzgTUpwHbxA8UG5YD8mbDX__vK7ksqIquraCViFmlWyD3gHkiM-2bsav0mMuW03x8XtuamRUhWR0pFrNlAZt0Pl4eRLx_1ZKgJyayBQj36oy1-6UKgZM1I1F8c2pUZ_yfJIZ8jGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر فروشگاه آنلاین داری، این پست می‌تواند هزینه تولید محتوایت را نصف کند.
قبلاً برای هر محصول باید:
❌
عکاس می‌گرفتی
❌
لوکیشن پیدا می‌کردی
❌
ساعت‌ها زمان صرف می‌کردی
حالا کافی است یک عکس ساده با موبایل بگیری…
رقبایت دیر یا زود از این ابزارها استفاده می‌کنند؛ سؤال این است که تو زودتر شروع می‌کنی یا دیرتر؟
@digitall_cast
ارتباط با پشتیبان :
@Digital_cast_support</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/676516" target="_blank">📅 01:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676515">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a98Y-UX7SNllfACX9ACm2f0_zK-K93mwjkjX--N3f3Y2ypAKyX_-xl8be4qyDlY0RtEBQswBrdCvBT2HbyeoByPCTkeUhabZsmHA2fMzWu4QrYwTup_9f2SNLbXoAolhsBtvE_31aqtW3nQSqDLApwpb9AhPSv-kS_JsO5Jxd_ADvEfIHoNAYWLqUu5nxtOyoWyIU00Zb_g1NMVYUKHaFMefSw-fOH2_M7kWZxIsF2rOgfDlA0rI5MV0vStYIdaQRu489jJy8tGJFB7vSHIWmsOrEGw6OkGNdqIUr9dn4tV3RfbBA3rVTSkvsPxWO_ztzYS8iEOXC50PufV6lNlKnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بسیاری از هواپیماها در خارج از فرودگاه ریاض در عربستان سعودی متوقف شده و فرود نمی‌آیند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/676515" target="_blank">📅 01:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676514">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKXPOaRheJO9ckjHz5e_G_JBI02DGQ8OD94wU6FpMJFmlpXzMW_N1Y3hvcegzszomiHvdWa8Ynuu2sg16ESrSGeK-FRT2jtVmp2o79Mxgxx_audp0OTwIOBnI3awc0eymfI9PyX4YxllXmUdKfgZySpLMPHQffn0L4myFan1P9irPlVpEtldCibtfZ4QjWR3Lo052mt3nm-em0zNAcDAHqUfv8UZtItmIRD8k7F7FLTNIQv2IU00XogIKlHFezDlFYStaR5FMbhvWIMZkde8bkRPkZg93Z9SgM8_IIGRZ6s6V_BJQM0k8s4ej_YE59qhkAMHdVDSL6GAHfkpJrtAVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعلیق فعالیت فرودگاه «ملک خالد» در ریاض
🔹
منابع عربی می‌گویند که فرودگاه بین‌المللی ملک خالد در پایتخت عربستان سعودی، بعد از شنیده‌شدن صدای انفجارها در ریاض، موقتاً بسته شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/676514" target="_blank">📅 01:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676513">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
گزارش‌ها از وقوع انفجار در ریاض
رسانه عراقی «نایا»:
🔹
صدای دو انفجار نامشخص، به وضوح در ریاض، پایتخت عربستان سعودی، شنیده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/676513" target="_blank">📅 01:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676511">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
روزنامه وال‌ استریت ژورنال به نقل از یک مقام دولت آمریکا ادعا کرد که
دونالد ترامپ همچنان در حال بررسی گزینه‌های خود است و هنوز تعیین نکرده که حمله به ایران در کجا و با چه شدتی انجام شود
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/676511" target="_blank">📅 00:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676510">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ترور ناجوانمردانه در شهرستان ایرانشهر
مرکز اطلاع رسانی پلیس سیستان و بلوچستان:
🔹
ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی که متأسفانه استواریکم "مهران سالارزاده" به درجه رفیع شهادت نائل شد.
🔹
تلاش برای دستگیری عاملان این سوء قصد ادامه دارد و اخبار تکمیلی متعاقبا اطلاع رسانی خواهد شد./مهر
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/676510" target="_blank">📅 00:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676509">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3c2975d3.mp4?token=E_0CTGRypleKqo-HQQhYYVd8jI0nBioL1ZsdNpwZIDNfYvUPOMO9r0anOHCktcV0Bj8OcrTkRlPrEylgdxvmIs6xeT2NXbdD2WKKllck5iu0jz7byx8trNmzph-ZLp-xoRuQreXGsZcEiJDuu3dym0TF4qTsw_5ESNMnmvYXSoFMZv5haTibtSJ7-Ser16KDS_bvDppUhNWovToMW3qCzwYC5dOYrQ-I8XY9sbqGuR5L9bKv9nDGZ7U1-ZkORZBMSowSX0yGyHDN31iLgU8bcX7HhNHCbHxlBnVq7PY0MK_663n6KlX1taJkKr0WK-ggvZ-98xv42sBU-4ZOS-Fnyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3c2975d3.mp4?token=E_0CTGRypleKqo-HQQhYYVd8jI0nBioL1ZsdNpwZIDNfYvUPOMO9r0anOHCktcV0Bj8OcrTkRlPrEylgdxvmIs6xeT2NXbdD2WKKllck5iu0jz7byx8trNmzph-ZLp-xoRuQreXGsZcEiJDuu3dym0TF4qTsw_5ESNMnmvYXSoFMZv5haTibtSJ7-Ser16KDS_bvDppUhNWovToMW3qCzwYC5dOYrQ-I8XY9sbqGuR5L9bKv9nDGZ7U1-ZkORZBMSowSX0yGyHDN31iLgU8bcX7HhNHCbHxlBnVq7PY0MK_663n6KlX1taJkKr0WK-ggvZ-98xv42sBU-4ZOS-Fnyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بین‌الحرمین میزبان زائرین پرشور و عاشق اربعینی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/676509" target="_blank">📅 00:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676508">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b1a77561e.mp4?token=cEqltR7L2jKL37zBPJKVAUjYdtzs7oWSEbuYGFFqX6HBuKIAupl5GoVD3ZuKFBjBdUrtAnmBMhxRQw9o-SXDXNeUMSq6hyMNjN6N_-N4X_V_TtHVewPxUBkWCf4DoKCK2RjOcgeg2y43wJwm2bGqElnp68b6KCmZM4MerZKuDXWK_83zAFCXwBrvDQdyw5M3iI4ym0-v8vE01rRY9Cqn2r98IE_4F6s0Mp7RwNw2DAyE95qPXWEzbCVTt3MtxXV0zi3rc1dx9a5WhAr0VqnyKCdFuPDRuftjhgvreg4AuDLwe7EfVwMF1tkeR_mjweZlcsyiLr7ivADvcpX448fRcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b1a77561e.mp4?token=cEqltR7L2jKL37zBPJKVAUjYdtzs7oWSEbuYGFFqX6HBuKIAupl5GoVD3ZuKFBjBdUrtAnmBMhxRQw9o-SXDXNeUMSq6hyMNjN6N_-N4X_V_TtHVewPxUBkWCf4DoKCK2RjOcgeg2y43wJwm2bGqElnp68b6KCmZM4MerZKuDXWK_83zAFCXwBrvDQdyw5M3iI4ym0-v8vE01rRY9Cqn2r98IE_4F6s0Mp7RwNw2DAyE95qPXWEzbCVTt3MtxXV0zi3rc1dx9a5WhAr0VqnyKCdFuPDRuftjhgvreg4AuDLwe7EfVwMF1tkeR_mjweZlcsyiLr7ivADvcpX448fRcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک شهاب سنگ آتشین عظیم در آسمان نیوزیلند مشاهده شد
🔹
مردم محلی می‌گویند: «شب هوا کاملاً صاف بود... و ثانیه‌ای بعد، یک چیز بزرگ، شعله‌ور و آتشین در آسمان ظاهر شد.»
🔹
کارشناسان معتقدند که ممکن است بخش‌هایی از این شهاب سنگ به زمین سقوط کرده باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/676508" target="_blank">📅 00:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676507">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiDJwnQQe0jqGj5n6ToTF7-TS4_Zn_B9cvcyFcT_KMmNgkfyA6tMznRiqPs5XhqvezbnEq2MqtDfXyAzmsX7TQ9xVLyTqpr_vUQ3DqnqBjTGVhpSHi7d1wJDJeebukVJqknxJorl9NQNBU_p3pwlD7lAEBmDGTNwNo0ohYy4Esd5w7lIhdbaCIIvvXQ8VMBB2LNzX_rzOg73AaANjc8WnoGbTFmbdLYmrXKiGLNYgPuxsgktd8v4E7XdLMoDOW6S9yZR8x0RMyGp6WSA-Z_SCdNs5z43gsg85pQCT-T8gVLybvE_nYNeWKmTtuRx9JpUMVXPIPZalHGon-WCVENWYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/676507" target="_blank">📅 00:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676506">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoZ-jaDt1CwyGp6hTxjdqycheM1Xrj0LzH_plazGLAwaO14XYiz8ij6wCgEpaZwh6UQLC94uYtL1h8RNTVM9AMgA3aJbOCV_uApb_TOIV-aQuNAPTgjTDmEDU_t1oQbtwD9YTZbDC6ghdhWSKIFOymAwR30Tw6gxKcDMKSJHyArHf4E2Nzffq8RxN5mXEhXBVFSvBQWhOtgyB0IKcIvo5hjFTW7Q1xBTrBNH95ax0azd7IpzFRueN06bwDZHVO9QcuYwhM55CPu1N1uHkFyWv-iZeBoGQulsqQHTddrJKe5MpCg2SGqLfoEx8dO6NLhRQkQXVSIYJPUDPa_x3C908Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت پرده حمله به عراق/ پروژه مرموز «اختاپوس» توسط موساد فعال شد؟
🔹
درگیری شب گذشته در یک زمان بسیار حساس رخ داد. آنطور که کاظمی قمی، سفیر پیشین ‌ایران ‌در عراق گفته است: حمله به عراق، آن‌هم در آستانه سفر نخست ‌وزیر این کشور به عربستان، نشان می ‌‌دهد، دستی در کار است تا جنگ منطقه‌ ای را تشدید کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3234193</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/676506" target="_blank">📅 23:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676505">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9oW2gikRqE4R2Ti5hXJhZY4wIJTyfgc1TFKJAwEWoUxQRGBzEhMeAMLLAKa3Fn7jAh_O6BTQhWF46JYzIsASnWsNriEDNnvmoJGWZT4dyVsIxP_c1Qdyy15lKd3PNgxv6VQzxCIlzYGRv8MlrL-YgtY7y0SlW_uEDB4Kq1YhiZEK6d-La3tMvdRWiJ_3DWQxDTH-NZr4zk3rMwZ37WN6JH7Pnp05ziZDcuHMmGiBpiwFSrUzZbV8QJhdylxGxBLwfPTBFI_rwYZrXWid212GX2bMaekLDlVNnuNkJB8P2RSA-43pQSM4HUbs2z4Y1ZjRbLKGzEjh_vzScSrs7KwPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترکیب جمعیت عربستان و همسایگان؛ چالش‌های پیش روی ریاض
🔹
عربستان با ۳۵ میلیون جمعیت، میزبان ۱۸ میلیون مهاجر پاکستانی، بنگلادشی، هندی و مصری است و از ۱۷ میلیون شهروند سعودی، بخش بزرگی شیعیان هستند که از سیاستهای آل سعود ناراضی‌اند.
🔹
این در حالی است که عراق ۵۰ میلیون و یمن ۴۳ میلیون جمعیت دارند؛ رقمی که موازنه منطقه‌ای را تحت تأثیر قرار داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/676505" target="_blank">📅 23:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676504">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
‏
معاون سابق وزیر جنگ آمریکا: نتانیاهو با کارت اپستین، با ترامپ بازی می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/676504" target="_blank">📅 23:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676503">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔹
داغ‌ترین خبرها را هر لحظه در وبسایت خبرفوری دنبال کنید
🔹
🔹
پشت پرده حمله به عراق/ پروژه مرموز «اختاپوس» توسط موساد فعال شد؟
👇
khabarfoori.com/fa/tiny/news-3234193
🔹
ترامپ در مواجهه با رضا پهلوی در مراسم خاکسپاری لیندسی گراهام چه کرد؟ / ویدئو
👇
khabarfoori.com/fa/tiny/news-3233989
🔹
موشک‌ های ایرانی، همسر دوم مرد اردنی را لو داد
👇
khabarfoori.com/fa/tiny/news-3233917
🔹
خواننده پاپ برای همیشه از ایران رفت
👇
khabarfoori.com/fa/tiny/news-3233955
🔹
خروج پردردسر علی دایی از مراسم بزرگداشت اکبر عبدی
👇
khabarfoori.com/fa/tiny/news-3234155
🔹
برای اطلاع از تازه‌ترین خبرها، اپلیکیشن خبرفوری را نصب کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/676503" target="_blank">📅 23:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676502">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UL5ejQ_wW5R4QSbKZUQ27s4RVbPU8XS5ZE8HqLzA3rtCLDJmuNV3ZKpl4QjRGLaPvImn0c3CYhXK-bpyzeXG4bxNB-fCVxo0GGLDsiYZazj2N3wXfEyvS-Qhn-CG__W1Tym5AFPFHRpcraKgAzkmWK9l8aSD6ZqAAvKlIujm2q731Gc5B9uyPtL_gsVLjJkEEy0aK5zCEYiFCSlgObmLfcDAIBifDw4gRpAVyZ-Mn8xhzApK0zXzvALopc2yp0uIbEXNtuez_1Kg_R7nrnYG5LJYTOZzOEbRPf1F0qDfiFaCwM8zt6uWsDIjmeMzqBXz9Qu1EAzunwLpXORpenJO6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سندرز، سناتور آمریکایی: ترامپ گفت که هزینه دارو را ۱۵۰۰ درصد کاهش خواهد داد، دروغ گفت
🔹
دولت او در حال پایان دادن به برنامه یارانه مدیکر است که هزینه‌های تجویز دارو را برای حدود ۲۵ میلیون سالمند افزایش می‌دهد.
🔹
شرم‌آور است. ما باید هزینه‌های داروهای تجویزی را کاهش دهیم، نه اینکه آنها را افزایش دهیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/676502" target="_blank">📅 23:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676501">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/haOQYjdDf18YzzjBh4tiOZL3eLsqS1z3edfbUXpe7gpeucCkqRG2TiVfou7FfBMpNAyvWtZE4xUsNWPX6Mu5qlyfnGvVr7nEpHv6DIVPqLDFKcKX9i4snJT1-VN8wJ8_SlHSiuxAcFtLlhdXFrZQv-YCLxTAhsDc-QXek3SfrdC4avRFnZweqymyYDc3j1D6u6WlNZG5lnQJwKufYquEAD6RJ7u-GjlTi-s0IIKg0DNULM3N5oWAsNjJypy4qnbKRIskX8BDD3Jim3S2JVWr4ocCVyWZRM-9ZZLpdg2FG8aORLcrZBvGAxIyY0nz-pGU3ni5lOOUDNGlbc8Q8hU4Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیمی از انگلستان اسیر خشکسالی شده است
🔹
دولت انگلیس اعلام کرد به دلیل«بارش کم سابقه باران و دمای بسیار بالا»، بیش از نیمی از انگلستان دچار خشکسالی شده است.
🔹
این کشور چهارمین موج گرمای گسترده خود در سال ۲۰۲۶ را تجربه می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/676501" target="_blank">📅 23:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676499">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/etCPak3J73XC0u1gjcB1IunHN06UgloG-_a26doGLHnHoYsN7agBP_y1witMrGZDrtN0-cT6LEz7Y8jZbrzzR21dY8qvQnkpnChQi1KfTp_BSC2UtWiMPd1ESTJOz737MHk0GPUgZG7cB4G674Y8aP2bHDC5SFrJZOF1-o0htKQ0W0jWMEjAWIc6BSY--uULRWA3hbGooN83i2w2cocpyUqxMQ0JYgxcqxs41GNekm2BEF6ODfV3LNF5CRG7OhS1nJ5rA4FEj459pg0AJOWoe3Fv2g_66JGif9qkr7YlDgOyob7KjRmJZRv2oA2idCATk0dwvFYuEBesepvzrO2R9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_5hd69tYU3adUPXbT8qcos4Y80Jo2P33jM140eA4cAe6duyk0M_Zvyy8dQutFDfpCTKLS39OGKqs_H43KgGbOhXc018wH-8ThGcDX4GisCQhNWrS4vYbQQia-2_v3Lf8gDK1OyNzrW_Va-z-dwD2p7cGjVrYWHIzwIuHFif1pM1_w1OVpZB_dJNrn4xOiJPQt8L7a0qYkWAdmaOq0yHRyJRphkQS1GKmMN07nXalCkVUPWTYAfsjVpRnfyQtqcHk4O7AOGjGzUZKpVlNI5XnBDH7qzq0fuZ0cWDslgZJB76Q6GCRiKPUm1cLLYwYg7bLBy7CDpC2xkjMVkfX87Yvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر برای تربیت دینی نوجوان خود چالش دارید، این کتاب را به فرزندانتان هدیه دهید
🔹
«نامه‌های بلوغ» میراث فکری و تربیتی اندیشمند بزرگ، علی صفایی حائری برای همه جوانانی است که در آستانه انتخاب‌های سرنوشت‌ساز زندگی ایستاده‌اند. او با زبانی صمیمی و عمیق، از بحران‌های…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/676499" target="_blank">📅 23:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676498">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9tqzqniFBkhfTeoZUcDnLf-PmcAQ9gFAGcjEDDHiJIN_l2mzxWoRxpFfOijyUOMqc_J5frVGmu1VWTXMYCNnM5oQa2ku5r5y__6MZQ3wZMEHttt_0V_2G_FsJoSErQ1PTRZYVgyoYT4cpNQTwO0EUhCt4qBOd4T5POu5-D7U1YCf4-9BdpIe7KWgdkocQqqwWadMFUh7Ijm1QVW835GaJ957t2xlsOS8bdCBjaTaz0rsUde7xHvAAFrdKpCmfcTr7nx_3WVIxJolNrxr3tx_t4Uj_xHgdRlst6blyoPGnSgO0kW2wDoOOfzo5Q-OXILnBG7b4a2Yw8DBFgLwlT87A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واگذاری هفت تپه متوقف شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/676498" target="_blank">📅 23:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676497">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
خوک هار درباره ایران: من دوست دارم تعرفه‌هایی علیه ایران اعمال شود
🔹
این واقعاً همان چیزی بود که لیندسی (گراهام) می‌خواست./ انتخاب  #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/676497" target="_blank">📅 23:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676496">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
روابط‌عمومی سپاه: بستن حساب کاربری روابط عمومی سپاه، نشانه‌ وحشت از داده‌های دقیق ملت‌های آزادی‌خواه منطقه از مواضع آمریکایی است
🔹
به‌زودی درگاهی جدید، امن و مطمئن برای ارتباط مستقیم با ملت‌های آزادی‌خواه جهان معرفی خواهد شد تا مسیر تبادل اطلاعات و آگاهی‌بخشی، مستحکم‌تر از گذشته ادامه یابد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/676496" target="_blank">📅 23:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676495">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15f83dac0a.mp4?token=Dzi1cJ9voS75JGrm-Cm4F3j-RErpYlHR0m_UoN7FufXs74rEhUYZxGqBa4Ohp6F5iTPidy0GNNDP4X6FWQ1snUcYaQttr8lhuBHJsoTBxsXnOWOlydKl8gyQkmlhPACQIDogNRCu9S6opRGLRgpQWzFQ7RGj46X8jvS02Nw9_k5Rr_HmcSdcv_JXXH-9qc-7axiK8tzfa82wZte7StkwGqU5Vjzz2hUUsiaeVCqiP8g7xmph3R5098oKX_q-5bwjOTU2BIpk31hlrNanLf3Tl0VFkiDJ-nfy9Bitkj4PKK4oQVnKQu_vpZE2lkqVeYvkWvMFhYNjB4-ABAEh2-Oucg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15f83dac0a.mp4?token=Dzi1cJ9voS75JGrm-Cm4F3j-RErpYlHR0m_UoN7FufXs74rEhUYZxGqBa4Ohp6F5iTPidy0GNNDP4X6FWQ1snUcYaQttr8lhuBHJsoTBxsXnOWOlydKl8gyQkmlhPACQIDogNRCu9S6opRGLRgpQWzFQ7RGj46X8jvS02Nw9_k5Rr_HmcSdcv_JXXH-9qc-7axiK8tzfa82wZte7StkwGqU5Vjzz2hUUsiaeVCqiP8g7xmph3R5098oKX_q-5bwjOTU2BIpk31hlrNanLf3Tl0VFkiDJ-nfy9Bitkj4PKK4oQVnKQu_vpZE2lkqVeYvkWvMFhYNjB4-ABAEh2-Oucg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سگ زرد: باز کردن چاه‌های نفت دریای شمال بریتانیا را ثروتمند می‌کند
‏
🔹
ترامپ جنایتکار در پاسخ به گزارشگری که درباره توانایی آندی برنهام، نخست‌وزیر جدید برای رهبری بریتانیا پرسیده بود، از تصمیم او برای گشایش نفت دریای شمال تمجید کرد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/676495" target="_blank">📅 23:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676494">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a062f9cc.mp4?token=KRV-QNuQRdukYSHUWIpsvdriBUckijCkr9AfwIUZ-cVLFt6knKdHXj7mtQP9crhlVKNXunxpi_mAAeiRRCXGQbPahiZm3KLAqZ6gGfjXspF-mtxo0-lFAaz-Kjn9C93iWJ4kwuviqxO5DL93S5q-2VywwB7Ua4SCUfJGUu5-9JVwto41jLW_4x-ah5Ncl5kFGlDiGgJ-N2oCUI0mucZ-kxQvCUKyvG-T-yXmdNlGMHlK8YXwvZ-S-F-IRD77FC5mQ2HqDE4VQDMvzgNjs8j2D_laQVE6h8q9YWOQWaZbyesfy4FGz363GpyMLy2gOtat63_9z3DzCTlg7F1tTepzVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a062f9cc.mp4?token=KRV-QNuQRdukYSHUWIpsvdriBUckijCkr9AfwIUZ-cVLFt6knKdHXj7mtQP9crhlVKNXunxpi_mAAeiRRCXGQbPahiZm3KLAqZ6gGfjXspF-mtxo0-lFAaz-Kjn9C93iWJ4kwuviqxO5DL93S5q-2VywwB7Ua4SCUfJGUu5-9JVwto41jLW_4x-ah5Ncl5kFGlDiGgJ-N2oCUI0mucZ-kxQvCUKyvG-T-yXmdNlGMHlK8YXwvZ-S-F-IRD77FC5mQ2HqDE4VQDMvzgNjs8j2D_laQVE6h8q9YWOQWaZbyesfy4FGz363GpyMLy2gOtat63_9z3DzCTlg7F1tTepzVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
قبل از حرکت، مسیرت را هوشمندانه انتخاب کن
🔹
در سفر اربعین، انتخاب مسیر مناسب می‌تواند زمان سفر را کاهش دهد، از ترافیک و ازدحام جلوگیری کند و سفری ایمن‌تر و آرام‌تر برای شما رقم بزند.
🔹
با مراجعه به سامانه ۱۴۱، مسیرهای مختلف را بر اساس آخرین وضعیت تردد، ترافیک و شرایط جاده‌ها مقایسه کنید و با آگاهی بیشتر، بهترین مسیر را برای رسیدن به مرز انتخاب کنید.
🔹
برای اینکه بهترین مسیر را انتخاب کنی، بیا ۱۴۱
#چشم_به_راهیم
#اربعین
#سامانه141
#انتخاب_بهترین_مسیر
#سفر_ایمن
#مدیریت_سفر
#سازمان_راهداری_و_حمل_ونقل_جاده_ای
#حمل_ونقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/676494" target="_blank">📅 23:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676493">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
سگ زرد درباره حادثه در مصر: از این حادثه مطلع شدم. این مثل سایر موارد است. در این شرایط، ما ایران را به شدت تحریم خواهیم کرد. آنها می‌دانند که این عواقب اعمالشان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/676493" target="_blank">📅 23:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676492">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
احراز سن کاربران شبکه‌های اجتماعی از سال ۲۰۲۷ در نیویورک اجباری می‌شود
🔹
از ژانویه ۲۰۲۷، احراز سن برای دسترسی به فیدهای الگوریتمی (مثل اینستاگرام و تیک‌تاک) و نوتیفیکیشن‌های شبانه در نیویورک اجباری می‌شود.
🔹
متخلفان تا ۵۰۰۰ دلار جریمه خواهند شد و کاربران زیر ۱۸ سال نیاز به رضایت والدین دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/676492" target="_blank">📅 23:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676491">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
استخدام در آموزش و پرورش برای امسال منتفی شد
محمدرضا احمدی، عضو کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
امسال جذب نیرو از طریق ماده ۲۸ انجام نخواهد شد. توجه به کمبود معلم، پیشنهادی مطرح شده تا نیروهای نهضتی، پیش‌دبستانی و خدماتی به‌عنوان نیروی شرکتی جذب آموزش و پرورش شوند تا دانش‌آموزان در سال تحصیلی جدید بدون معلم نمانند.
🔹
همچنین پیشنهاد شده دانشجو معلمان سال آخر تحصیل بتوانند با طی فرآیند ارزیابی و آزمون عملی یا تئوری، در مدارس تدریس کنند تا هم تجربه عملی کسب کنند و هم بخشی از کمبود معلم جبران شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/676491" target="_blank">📅 23:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676490">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
تشکر راحله امینیان، مجری صداوسیما از مردم عراق برای بدرقه باشکوه رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/676490" target="_blank">📅 23:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676489">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
فرمانده مرزبانی استان بوشهر از توقیف چهار فروند شناور با محموله کالاهای قاچاق خبر داد و گفت:ارزش ریالی این محموله برابر اعلام کارشناسان، ۲۰۳ میلیارد ریال برآورد شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/676489" target="_blank">📅 23:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676487">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
سگ زرد درباره حادثه در مصر: از این حادثه مطلع شدم. این مثل سایر موارد است. در این شرایط، ما ایران را به شدت تحریم خواهیم کرد. آنها می‌دانند که این عواقب اعمالشان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/676487" target="_blank">📅 22:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676486">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d107593ce.mp4?token=ZSHh94jN_zTk7-LFZ9SxvLG5KKBNOsU4wCRWP5zJWRZ0WNFkuk17DiYSqxPbt9kp0U-gJuwEZJw16xJqXWRlQIjm0hX7vGETI120Vj0qb4EPvObaVrdLPjBxtKb-ApXOCwgVlPt3bsPq3I_EmFgekcKiS2OHN-s0tFDZLnf_LSzGup3DLuChSubtLjpV3xBtUv5AjVHtUC3WOBj4rsYokR_bVxjOHd2Dgd_us6arkmFGVCgceQ2cYRy0kd-CR7zLp1K-LXp1nKoI7zYorUKV631vcVWmvzCtKpVlxcsWpy7rFX9W7PX3BCmIdRyXw9ZuVlK9ees9tnvshcu3RuGYzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d107593ce.mp4?token=ZSHh94jN_zTk7-LFZ9SxvLG5KKBNOsU4wCRWP5zJWRZ0WNFkuk17DiYSqxPbt9kp0U-gJuwEZJw16xJqXWRlQIjm0hX7vGETI120Vj0qb4EPvObaVrdLPjBxtKb-ApXOCwgVlPt3bsPq3I_EmFgekcKiS2OHN-s0tFDZLnf_LSzGup3DLuChSubtLjpV3xBtUv5AjVHtUC3WOBj4rsYokR_bVxjOHd2Dgd_us6arkmFGVCgceQ2cYRy0kd-CR7zLp1K-LXp1nKoI7zYorUKV631vcVWmvzCtKpVlxcsWpy7rFX9W7PX3BCmIdRyXw9ZuVlK9ees9tnvshcu3RuGYzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مراسم بدرقه زوار حسینی در میدان آزادی تهران برگزار می‌شود
🔹
آیین بدرقه زائران اربعین، روز پنجشنبه با حضور خانواده‌های تهرانی به ویژه نوجوانان زائر از میدان آزادی تهران در قالب برنامه «محرم شهر» برگزار می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/676486" target="_blank">📅 22:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676485">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دادستان مشهد: قاتلان ۲ بسیجی مشهدی دستگیر شدند.
🔹
فدرال رزرو آمریکا نرخ بهره را بین ۳.۵ تا ۳.۷۵ درصد ثابت نگه داشت.
🔹
شبکه CNN: وزیر دفاع عربستان سعودی امروز در واشنگتن با ترامپ و ونس، دیدار کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/676485" target="_blank">📅 22:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676484">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7db80720e.mp4?token=nkGz5_WdbrmoZwpMY7ePXZklVMUKfE8tCNNMmVTDbok58aI5oFiNt6xLKQbZ1LydG_h1tXkoh5e-4pbQWb-upr6c3mbNymIoFPAFlx98PD3bookDB7crpNs00ZutGWC37i8OmmB9_9MgNutI6r1TPoBOH-OxqxhZybYgg4-lewajYyIBDwXi-fyTXnpc4-bGbkEXZDEGKq397BE1EqGZQyCR20mmKKfvdI5anGjUnz9sAngvn29OlUVMvBvnqbsidbPaKwfWlKoU4A2tL_vv0eKWxBxpaAZ-fknCobP-Ku4KeYgiHAu-BGTcMbF3vI1pTSUwZdjNXBWNS0FfKdLPvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7db80720e.mp4?token=nkGz5_WdbrmoZwpMY7ePXZklVMUKfE8tCNNMmVTDbok58aI5oFiNt6xLKQbZ1LydG_h1tXkoh5e-4pbQWb-upr6c3mbNymIoFPAFlx98PD3bookDB7crpNs00ZutGWC37i8OmmB9_9MgNutI6r1TPoBOH-OxqxhZybYgg4-lewajYyIBDwXi-fyTXnpc4-bGbkEXZDEGKq397BE1EqGZQyCR20mmKKfvdI5anGjUnz9sAngvn29OlUVMvBvnqbsidbPaKwfWlKoU4A2tL_vv0eKWxBxpaAZ-fknCobP-Ku4KeYgiHAu-BGTcMbF3vI1pTSUwZdjNXBWNS0FfKdLPvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سه انفجار متوالی در سلیمانیه عراق
🔹
انفجارهای شدیدی دوباره در منطقه رانیه، واقع در استان سلیمانیه در شمال عراق، رخ داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/676484" target="_blank">📅 22:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676483">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XU5MQprNCQ7eysYQwFUD359S9ESZuEQ7zrNpehurnxZm7oIt-eEd50eLeVovWPwTwQ92Uh2RHDqVu1yC9EUTNLgPrSGBmJq5pV-1fDxyHbIm-UQ7KQILigitBmOD2PTPHczGqmIikajWDsE6_HS2vbmQF4Eq8NZaJXlpT4t3icDFcov8U2M-SzqcyA5PcmefhsZP1zU8MXpuCodti7SdDaynGLLENhmccqI1ZRYtoN62SHv9pmfFRvY09UWn2VRP8Udp5lV__FT_q7ucBj_fSGb5UgWgPidl0amyigwVayzX3wf1EsYitUbWf-nbyg7XXH1-S-MnmrfXFa4WXMJYng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ شبه جهانی
🔹
تنش‌های میان ایران و آمریکا وارد مرحله‌ای شده که ابعاد آن از یک تقابل دوجانبه فراتر رفته و به یک بحران منطقه ای تبدیل شده است. در تازه‌ترین تحولات نیروهای آمریکایی و عربستانی عملیاتی خباثت گونه را در عراق انجام دادند درگیری های یمن و عربستان همچنان ادامه دارد و همزمان تنش ها در جبهه های دیگر نیز رو به افزایش است. از حمله اوکراین به یک کشتی ایرانی با ادعای حمل تجهیزات نظامی گرفته تا حملات متقابل ایران به خاک اردن و مقر نیروهای آمریکایی همگی نشان می دهد دامنه این رویارویی در حال گسترش است. در این میان اسرائیل نیز همچنان به عنوان یکی از بازیگران اصلی این بحران دسیسه چینی میکند.
🔹
هشتصدوبیست‌وسومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/676483" target="_blank">📅 22:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676482">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
الجزیره: نقشه‌ای که نتانیاهو برای ایران کشیده بود افشا شد
ادعای الجزیره:
🔹
جزئیات جدیدی در حال آشکار شدن است که نشان می‌دهد مقامات آمریکا و اسرائیل چگونه معتقد بودند جنگ علیه ایران سرراست و کوتاه‌مدت خواهد بود.
🔹
مگی هابرمن، خبرنگار آمریکایی می‌گوید بنیامین نتانیاهو سناریوهای تغییر حکومت را به دونالد ترامپ ارائه کرده بود. لیندسی گراهام یک جدول زمانی چند هفته‌ای را برنامه‌ریزی کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/676482" target="_blank">📅 22:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676479">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رزاقی: بنادر عمان دست اروپاست، اروپا هم ایران را تحریم کرده
جمال رزاقی، رئیس اتاق بازرگانی ایران و عمان در
#گفتگو
با خبرفوری:
🔹
عمان بنادر بسیار خوبی دارد ولی این بنادر در دست اروپایی‌هاست و به علت تحریم نمی‌توانیم در این بنادر کار کنیم.
🔹
در طول جنگ عمان چهار بندرش را به تجارت با ایران اختصاص داد. منتهی تمام این چهار بندر روی هم نمی‌توانند مانند بندر جبل علی امارات عمل کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/676479" target="_blank">📅 22:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676478">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/390179d40a.mp4?token=oNIKzwWmDOMjDFlZDWOU2FpAv4HfmMQUbkJNuctQEQhZn2XTMjLmTAjKsZUHRZrv581YnDYJcS21Ps8ANpJNRsPVYgQIdsIAbmLt7J9xEGa3eap7yEigL1-luNKyJQDldn4yYHpXpa9TMHiqlQfE94ILsgGjBwfGGvAiTI6xMaihCUb5S_exYZZR2t1iAyEJuaOsb-acJzlz71ebQGjRqlLc6huqKG82pVTEOXg1ZfUjRz-pb0CEW1xXNUu0s0OZ3tTehIwHkWHvK4ABCL71arDXsR3N4OnUmHEeqm-MOuQNzFGVQ_BRZjQq3sdMAqKmd969JKr2sWBukRqJpeSHhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/390179d40a.mp4?token=oNIKzwWmDOMjDFlZDWOU2FpAv4HfmMQUbkJNuctQEQhZn2XTMjLmTAjKsZUHRZrv581YnDYJcS21Ps8ANpJNRsPVYgQIdsIAbmLt7J9xEGa3eap7yEigL1-luNKyJQDldn4yYHpXpa9TMHiqlQfE94ILsgGjBwfGGvAiTI6xMaihCUb5S_exYZZR2t1iAyEJuaOsb-acJzlz71ebQGjRqlLc6huqKG82pVTEOXg1ZfUjRz-pb0CEW1xXNUu0s0OZ3tTehIwHkWHvK4ABCL71arDXsR3N4OnUmHEeqm-MOuQNzFGVQ_BRZjQq3sdMAqKmd969JKr2sWBukRqJpeSHhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی جنگلی به ترکیه رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/676478" target="_blank">📅 22:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676477">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d69eea63.mp4?token=WFIaAlcyWJeoZp-UJOQDA4GiR_SaegF-t2jLHOhb5Od7X6hpRXThkFXqh-D370Y6Vlqcu17g5r0iEXGz5VC_IH95HHX7Iurtgmo_sTrhH85OoCp8Olg_hhVmJ6KYaftTmNft-yIWqieEnFa4ZIi_mskVX7LWb3oSLfGclJE31Dgu9sCQNDvHaq-gPXzRRLglvOVK9SKfRHR2h5wNJ9FvzYyrKQTwLLxMnN7ZUSCq3c5aHbAqQj-XLSgaknn1dd8kjpeNUj7xIGqw2pmCCQFPl03GrN_AVfcqTrg-_2O3Wtl3Dj442xjopp5GLI6vtPCi76HvpTBPB46YvVU7R3ogVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d69eea63.mp4?token=WFIaAlcyWJeoZp-UJOQDA4GiR_SaegF-t2jLHOhb5Od7X6hpRXThkFXqh-D370Y6Vlqcu17g5r0iEXGz5VC_IH95HHX7Iurtgmo_sTrhH85OoCp8Olg_hhVmJ6KYaftTmNft-yIWqieEnFa4ZIi_mskVX7LWb3oSLfGclJE31Dgu9sCQNDvHaq-gPXzRRLglvOVK9SKfRHR2h5wNJ9FvzYyrKQTwLLxMnN7ZUSCq3c5aHbAqQj-XLSgaknn1dd8kjpeNUj7xIGqw2pmCCQFPl03GrN_AVfcqTrg-_2O3Wtl3Dj442xjopp5GLI6vtPCi76HvpTBPB46YvVU7R3ogVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار مهم پلیس فتا که حتما باید آن را جدی گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/676477" target="_blank">📅 22:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676476">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
سه انفجار متوالی در سلیمانیه عراق
🔹
انفجارهای شدیدی دوباره در منطقه رانیه، واقع در استان سلیمانیه در شمال عراق، رخ داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/676476" target="_blank">📅 22:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676474">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEECa18z9zSeLmYi484mMffhL9eGL9bGJAhV1CzmW9gXyG-BqO_gzkd8xhUBbQXUWmEXwpuw2KOhNz1vcW56LChSfCubfOqTBthuhybAcSTuK1falM1Nr-aQsNzI0gRZorptFx4R4GjDfSYxxG62vXlWehC69eoYSF5_ehN0Iicu6JCXg58rTzAPBe0zJXvI7hp4xIwEPQvQk4il3uorwDgFOy9QZnlTEYS0Y5jyhFK8WqtBj1zyGZ-BI-OQgFAVfVKkljKSzWTCHdaBCF_FrAw0P_UShWCROmgJzxQLWZ7aAeGrR0Xvl8FIaReQg-xTyKGiEpifu-66gXbOuw2Uxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
آخرین اخبار اربعین را از «چشم به راهیم» دنبال کنید
🔹
در ایام اربعین، اطلاع از آخرین وضعیت جاده‌ها، مرزها و تردد می‌تونه مسیر سفرت رو سریع‌تر، ایمن‌تر و بدون دردسر کنه. آگاهی، بهترین همسفر شماست.
◽️
به‌روزترین اطلاعات از:
🟡
وضعیت لحظه‌ای محورهای منتهی به مرزها
🟡
خدمات و امکانات مجتمع‌های رفاهی بین‌راهی
🟡
هشدارها و توصیه‌های ایمنی سازمان راهداری و حمل‌ونقل جاده‌ای
🔔
همین حالا به «چشم به راهیم» بپیوندید و با اطلاعات دقیق، سفری ایمن و آرام را تجربه کنید.
✅️
@Cheshm_Be_Rahim
✅️
@Cheshm_Be_Rahim
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/676474" target="_blank">📅 22:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676473">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoFF0Di7J9JHo8jRDwcCnTRLp79pAv_vuf4wx68r46szlG99YY5gbT5HvH1f_EoqLcgUZiqpzMcIWXPM9x7VRJb6GOSzDR9BrGnYAEIiEIzfulnuS3fCbt49Vo3ubPktW-6M_2clYOwDvETkd4jTYwKN-KCHfhkyVFM9c7y7daEHvMaBwIqWHXgYNHRpXhuGr5TU_dHDKs372s0kkOqyMftMi23zAKBzk3gIDMuWXLsOtUvQcvO8b6uTQKR3fiNTdofdhIKvdofjT3mF5ZUJalmuv4bJsEk2PX1QTyj1JdbhdVxrStQbS0QOn8KD8DiovwbvSj7nMi0hVvaMffo3xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر چهار شهید ایرانی در پی حمله مشترک عربستان سعودی و آمریکا به استان کربلای معلی در عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/676473" target="_blank">📅 22:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676472">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
شوک قیمتی؛ بازار قهوه انفجاری شد
🔹
بازار جهانی قهوه این روزها رفتاری کم‌سابقه از خود نشان داده و به شدت صعودی شده است. پس از اعلام وقوع پدیده ال‌نینو، قیمت قراردادهای آتی قهوه عربیکا حدود ۲۷ درصد جهش کرد.
🔹
افزایشی که با نگرانی از کاهش تولید در برزیل، بزرگ‌ترین تولیدکننده قهوه جهان، آغاز شد. شاخص نوسان بازار قهوه حالا به بالاترین سطح خود در ۲۶ سال اخیر رسیده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/676472" target="_blank">📅 22:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676471">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d599cd43c2.mp4?token=veKpl6XqR9haMtKoZz1upD4sLJnkaed-nEvqRsZxtXwp8Wv9BE-eSbk6PK9qT2WJsi_VnknoBQnBQ-ThcZIi92NAcvChn5mxRYRSzOnxE3RnckERsAuSqIuzLPG4ElX2V4KYja28XqVrCpdz5IE-q288YM-0PTTZCUYaQJw0wc2KYXMyrxBp2A0pY0wYR70EHO2_g8ESl9ehED-fXt8EsqhgVVOQX_BE274Prhnz_EAZ4BQ4FwY7STe1wPOPkwCf1K21RmWCIfXgS5rBI93K63G3b6jfdnspQFtoNtMfwcYFP-LubXpyrKuUVxXIIZ89--zLKtVLmFZPI--jz9TJHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d599cd43c2.mp4?token=veKpl6XqR9haMtKoZz1upD4sLJnkaed-nEvqRsZxtXwp8Wv9BE-eSbk6PK9qT2WJsi_VnknoBQnBQ-ThcZIi92NAcvChn5mxRYRSzOnxE3RnckERsAuSqIuzLPG4ElX2V4KYja28XqVrCpdz5IE-q288YM-0PTTZCUYaQJw0wc2KYXMyrxBp2A0pY0wYR70EHO2_g8ESl9ehED-fXt8EsqhgVVOQX_BE274Prhnz_EAZ4BQ4FwY7STe1wPOPkwCf1K21RmWCIfXgS5rBI93K63G3b6jfdnspQFtoNtMfwcYFP-LubXpyrKuUVxXIIZ89--zLKtVLmFZPI--jz9TJHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران، سرزمین قهرمانانی که شجاعت را نه در حرف، بلکه در نجات جان انسان‌ها معنا می‌کنند #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/676471" target="_blank">📅 22:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676470">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نمایندگان مجلس در پی زنده کردن R&D در ایران
رمضان رحیمی، عضو کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
طرح جدیدی برای ساماندهی کارآموزی دانشجویان داریم که با باز شدن مجلس آن را پیگیری خواهیم کرد. ما می خواهیم R&D را در ایران زنده کنیم و رابطه صنعت و دانشگاه را بهبود بخشیم.
🔹
منابع مالی برای حمایت از دانشجویان شرکت کننده در طرح در نظر گرفته شده و صنایعی که در این طرح شرکت کنند از معافیت‌های مالیاتی برخوردار خواهند شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/676470" target="_blank">📅 22:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676468">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
کمک فوری برای درمان کودک 4 ساله ای که سرطان دارد
🔹
کودکی ست 4 ساله ، چند ماه است به سرطان خون مبتلا شده است ، چند جلسه شیمی درمانی انجام داده ، ماهانه حدود ده روز باید در بیمارستان بستری شود که حدود 15 الی 30 میلیون دارو احتیاج دارد.با کمک اقوام تا الان توانسته اند دارو ها را تهیه کنند. اما به دلیل گران بودن داروها و برای ادامه درمان و اینکه این بیماری طول دوره دارد نیاز فوری به کمک مالی دارند.
هموطنان عزیز این کودک بیمار برای بهبود در انتظار کمک های شماست.
🔹
مورد دوم: مادری ست بی سرپرست دو دختر مجرد دارد و وضعیت مالی خوبی ندارند.دو سال است به سرطان روده مبتلا شده ، پدر در حال درمان است.مدتی پیش عمل فتق و صفرا انجام داده و هزینه عمل بیش از100میلیون تومان بوده که با قرض از اقوام توانسته آن را پرداخت کند ایشان برای درمان سرطان باید دارو مصرف کند.
✔
پرداخت انلاین خیریه نسیم وصال:
http://www.nasimevesal.ir/payment-new
شماره کارت بانک ملت : ۶۱۰۴۳۳۷۸۱۱۴۱۶۲۳۷
شماره حساب بانک ملت: ۵۸۹۸۷۷۱۴۶۵
شماره کارت بانک ملی: 6037997599156198
شماره حساب بانک ملی: 0219934010000
شماره شبا: IR310120020000005898771465</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/676468" target="_blank">📅 22:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676466">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
سرپرست وزارت دفاع: راه شهدای اقتدار با اراده راسخ رزمندگان و خادمان صنعت دفاعی ادامه خواهد یافت
سردار ابن‌الرضا:
🔹
بازگشت پیکر مطهر شهید والامقام امیر سرتیپ‌دوم خلبان مجید کاظمی پس از ماه‌ها چشم انتظاری، روایتی نام آشنا و کهن فرزندان ایرانی است که عهد خود با ایران، اسلام و مردم را تا واپسین لحظه حیات حفظ کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/676466" target="_blank">📅 21:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676464">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0vQoBfUsb214t5OuHawe2z0H2WMWbPTjn_alYyLFBQw_hGXu16Yb_WIGhOwKSWzvYtU_jIs2H5zMrhm0bls_qLWFme62Kjjfcl0JmMWLyhA-rP86CMWf0w8DK1vAJ_uyEUDfKjz4e50BYSvJGaFhmwT09YISkq1ddtlNC9dMGUU3n4wIadJBwEkkgrjfy8nPzEhK-pDILBVqs_v9lxQ_CY6HVKK3A8h2Gxu2DqJverV4bRKaGFS1hJfeXFc4p6nokcRzU4upzgjQi0AW0ODnCHUklABeqUFBGnYIpdc4j2jh6tLmuVf-I8Bn0C2jEruDz2TqtiMCX2FCdro5wpnmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸۵.۳ درصد ایرانیان کاربر اینترنت هستند
🔹
روند ۳۰ ساله استفاده از اینترنت در ایران نشان می‌دهد ضریب نفوذ اینترنت از ۴.۶ درصد در ابتدای دهه ۸۰ به ۸۵.۳ درصد در سال ۱۴۰۳ رسیده است.
🔹
این روند افزایشی تا حد زیادی قابل انتظار است؛ چراکه هم‌زمان با گسترش زیرساخت‌های ارتباطی و اینترنت همراه، دسترسی به اینترنت در سراسر جهان فراگیرتر شده است.
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/676464" target="_blank">📅 21:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676463">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcFwnmDIu55-_h_CI9y4PA9w4pyjT77pHkQ2Y0FrEVjldEjN35MC10fKrMz9e35ptFhhGQJoelZleij0jfE9s9X3iub2tzMjMSU_-JElySsYA5VdmvJRtgzzXWujkHHDOn472iuWtcvJ3oGHQSufK7JESKpRNSTyW-S0qkcW5MQBu98w9WsBiiHln0AvkNstL-WGMWneTem4SEa14x__msE6yzoGgUG1Pgvj35kcOtryqct0AimxnqFMC1E9LO7oduF_Pea05LTSAqKgikAtz2BVqd9pm9VMSzfEmS8njxlcmvp1zsi6Pv8z_U253Dm_La5PRjoe1ttNvId5HdcSmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکورد بی‌سابقه جستجوی سَم برای کشتن ملانیا
🔹
پس از وایرال شدن ویدیوی جنجالی «ملانیا ترامپ را کجا و چگونه بکشیم» و پیشنهاد استفاده از عامل اعصاب VX در آن، آمار جستجوی این ماده سمی در سطح جهان به بالاترین حد خود رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/676463" target="_blank">📅 21:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676462">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
آثار تورمی ارز ترجیحی چگونه تخلیه شد؟/ کاهش تورم ماهانه برای دومین ماه پیاپی
🔹
زمستان سال گذشته بود که با پیشنهاد دولت، هر سه قوه به توافق رسیده‌اند که نظام چند نرخی ارز را حذف کرده و به یک نرخ واحد تبدیل کنند.
🔹
همچنین رهبر شهید انقلاب در ایام حذف ارز ترجیحی فرمودند و هشدار دادند: «درخصوص مسئله حذف ارز ترجیحی که اقدام لازمی هم بود، می‌بایست دلایل این تصمیم به روشنی برای مردم بیان شود»
🔹
اعتماد در گزارشی نوشت: اخیرا انتقاداتی به تیم اقتصادی دولت درباره سیاست‌های ارز ترجیحی مطرح شده و هم زمان با آن، وزارت اقتصاد در پاسخ رسمی به انتقادها تأکید کرد: «فلسفه حذف ارز ترجیحی دقیقاً مقابله با سیاستی بوده که طی سال‌های گذشته نه تنها به هدف کنترل قیمت‌ها دست پیدا نکرد، بلکه خود به یکی از مهم‌ترین بسترهای ایجاد رانت، فساد، قاچاق کالا و توزیع ناعادلانه منابع تبدیل شده بود.»
🔹
این وزارتخانه همچنین به آمارهای رسمی مرکز آمار ایران استناد کرده و روند تورم ماهانه ابتدا از ۷.۹ درصد در دی ماه به ۹.۴ درصد در بهمن‌ماه رسیده اما در اسفندماه با وجود هم‌زمانی با شرایط جنگی، به ۵.۶ درصد کاهش یافت و نتیجه گرفته که اثر مستقیم اصلاح ارز ترجیحی پس از دو ماه تخلیه شده است. البته در اردیبهشت‌ماه به دلیل تشدید آثار جنگ و محدودیت‌های ناشی از محاصره دریایی، دوباره افزایش یافت و به ۸.۸ درصد رسید.
🔹
همچنین آن طور که «عبدالناصر همتی، رئیس‌کل بانک مرکزی» در تازه‌ترین گزارش خود به کمیسیون صنایع و معادن مجلس اعلام کرده است که تورم ماهانه در تیرماه نسبت به ماه قبل تقریباً نصف شده و این موضوع نشان‌دهنده اثربخشی سیاست‌های پولی و مدیریت نقدینگی است. یاداور میشود در خرداد تورم ماهانه بار دیگر کاهش پیدا کرد و به ۵.۹ درصد رسید.
🔹
در روزهای گذشته «حمید رسایی، نماینده مجلس شورای اسلامی» مدعی شده بود که «نرخ تورم ناشی از حذف ارز ترجیحی بسیار و درحال افزایش است» و این البته در تناقض با گزارش های رسمی کشور است. گزارش‌های منتشر شده نشان از کاهش تورم در تیرماه دارد و ادامه روند کاهشی در مردادماه نیز قابل انتظار است./ اعتمادآنلاین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/676462" target="_blank">📅 21:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676458">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
خروج ۲.۲ همتی پول حقیقی از بورس؛ مقصد پول‌ها کجاست؟
🔹
بازار سهام امروز شاهد خروج ۲.۲ همت سرمایه حقیقی بود؛ در حالی که ارزش معاملات خرد به ۲۷ همت رسید. همزمان ۱۹۲ میلیارد تومان سرمایه از صندوق‌های طلا خارج شد و صندوق‌های درآمد ثابت با ورود ۱.۱ همت پول، مقصد اصلی نقدینگی بودند. در پایان معاملات نیز ۵۳ درصد نمادها سبزپوش و ۴۷ درصد منفی بسته شدند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/676458" target="_blank">📅 21:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676453">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6baeacb7c.mp4?token=X_5f0qQVvxWcVklMPpBmxSlP167K3BMtJJDuXo17J8F-HhfURNDtOjktEZNv-G2eDKWimcX30nsSxRJ22Gc6qjI2Hx4NJnFF-_0yL4dq2jnG1dX9Z1uAYkt5OJKV2j8OQhkPLUyCfe5IX3zKEzJQL04SDK55_zFUKY2TMkwgYgTBJR2cXg2rYYPDkRA02phDbR0g4fZLGvRTapTRLqyF30dzGLGZtJ7ySf5iFCPMBGkKzGOemmC9IweSflPLmqBlA-or-J34TnDGt9to_32BKmPNofbg85l8zGhMaW-3r0OalvLuK6Bwa4yv1Zf-ifQfyr-lYDgONqaw49cChuZZSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6baeacb7c.mp4?token=X_5f0qQVvxWcVklMPpBmxSlP167K3BMtJJDuXo17J8F-HhfURNDtOjktEZNv-G2eDKWimcX30nsSxRJ22Gc6qjI2Hx4NJnFF-_0yL4dq2jnG1dX9Z1uAYkt5OJKV2j8OQhkPLUyCfe5IX3zKEzJQL04SDK55_zFUKY2TMkwgYgTBJR2cXg2rYYPDkRA02phDbR0g4fZLGvRTapTRLqyF30dzGLGZtJ7ySf5iFCPMBGkKzGOemmC9IweSflPLmqBlA-or-J34TnDGt9to_32BKmPNofbg85l8zGhMaW-3r0OalvLuK6Bwa4yv1Zf-ifQfyr-lYDgONqaw49cChuZZSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
پیام‌های صوتی شما در پویش «همه باهم برای ایران» جلوه‌ای از همدلی، مسئولیت‌پذیری و عشق به میهن است؛ روایت‌هایی کوتاه اما پرمعنا از شهرها و لهجه‌های گوناگون ایران که یک پیام مشترک را فریاد می‌زنند: ایران، خانه مشترک همه ماست.
🔹
این صداهای صمیمی نشان می‌دهد که مردم ایران، فارغ از تفاوت‌های قومی و زبانی، در روزهای سخت کنار یکدیگر می‌ایستند
🔸
پیام های صوتی خود را به آیدی زیر ارسال کنید
👇
#همه_باهم_برای_ایران
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/676453" target="_blank">📅 21:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676452">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ud-0QSac3H5BFTBG2ddG8jkVSaZsmQzQghJ3-l4ZziMVnPr6agvIHn2uDfbJtlWwXCZK-phxj7pr9Vi08D1mpjRH-q5iDb926sOm4DlfXvCOIMjlymBSO54rQipmRTM05a74g5S78FM4rtpolXtneYEDAlnt3gn33R5gJWZsYOlsVNq8lDr8MqQw85dzi9iS_Bf_SWxSM23AJQt4I7URYdtAd0xY9Nfxo-ogC3C61YkiJkSSqA4UI1sVK59TGpViWlFe_HhQdiXeFRWyPwiqYppq2kwAd5f2Nuc2OwMpVPMUGUTQiFMMRpRQkIVRSNSIaG86_ItTNuDVLdvgK0VENw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تشییع پیکرهای مطهر پنج شهید ایرانی که در حمله شب گذشته آمریکا و عربستان به شهادت رسیدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/676452" target="_blank">📅 21:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676450">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/112ce0f51e.mp4?token=FBUp-nsdyWosGpa5uI035l8k2o7d-GCpl2t3s3C_HPDxHT2f1aNyLdvBXd0_-VCIOSGrqWHP2fzRJrF67pHUE4oAZsvv7TR1xa8TEr6m61IUKtogqpnd07SUYGl1wkW9ZUeRPHOTso76QHJAWYPJ-bWbJJkzMWkmpjdr7F9T4uXRDtB3l6bmF8ikSRQPGsin8JY4MYRJtl6939pVbKEhxqWfdIvKC8URTqLbSDEQ8fOrekoq_wy9uvzEyMECoIHdQIlGq-nZsx9UiHzaXQx6b7_Kue4fwNObTGIIyK9yqNPdvrfPLZUq4VuTqNVqS3kc3htLJJkdwMeSrZwpdT784CG-xgo1z_bUMy4K4Zdxt1j6tM8-1YyIyIvPXrU2iPb-ukGSeQrgWysMlsYryVppL6KwXkA6R4suctJf8aimttlVTiKD89M0QTvjgaApxsV6x8p4ToGXVn8LWgn53enjNXSLVxtOOSZrBYAslwPWjav-92nS28Kt3KZarVwoofI1u7wbdhEOYZm_4iqaYh_sITMMY-Fz-9ObEDb5DWEaBXtn4euF1PEhNAiuZXDDjbhEQwsA04GY6YawRYfPsdwYuENElzwF_ogwYmwZ-RS68senuNslV-e7hkvO5NRqJ4_DOmZm7B2NMRanlRM9tsdq56NyNG9q-Qj-3kjqtmI-Fok" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/112ce0f51e.mp4?token=FBUp-nsdyWosGpa5uI035l8k2o7d-GCpl2t3s3C_HPDxHT2f1aNyLdvBXd0_-VCIOSGrqWHP2fzRJrF67pHUE4oAZsvv7TR1xa8TEr6m61IUKtogqpnd07SUYGl1wkW9ZUeRPHOTso76QHJAWYPJ-bWbJJkzMWkmpjdr7F9T4uXRDtB3l6bmF8ikSRQPGsin8JY4MYRJtl6939pVbKEhxqWfdIvKC8URTqLbSDEQ8fOrekoq_wy9uvzEyMECoIHdQIlGq-nZsx9UiHzaXQx6b7_Kue4fwNObTGIIyK9yqNPdvrfPLZUq4VuTqNVqS3kc3htLJJkdwMeSrZwpdT784CG-xgo1z_bUMy4K4Zdxt1j6tM8-1YyIyIvPXrU2iPb-ukGSeQrgWysMlsYryVppL6KwXkA6R4suctJf8aimttlVTiKD89M0QTvjgaApxsV6x8p4ToGXVn8LWgn53enjNXSLVxtOOSZrBYAslwPWjav-92nS28Kt3KZarVwoofI1u7wbdhEOYZm_4iqaYh_sITMMY-Fz-9ObEDb5DWEaBXtn4euF1PEhNAiuZXDDjbhEQwsA04GY6YawRYfPsdwYuENElzwF_ogwYmwZ-RS68senuNslV-e7hkvO5NRqJ4_DOmZm7B2NMRanlRM9tsdq56NyNG9q-Qj-3kjqtmI-Fok" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات ضرباتِ ویرانگر ایران بر پایگاه دشمن آمریکایی در اردن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/676450" target="_blank">📅 21:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676448">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e12a6efbc.mp4?token=dVHc0paLSfeW2Vti_M-BJFZt_jGAq8A2vyMKVAzveH5DWSkWVZHTpf16cKbKcvxgMYPM7l8zqDpj84_OSKozfvtM9Hag8oK3UawvXO2wKqyEdrmps6asB0EFIAcKz1Pz8lDs3rWPLhbWJQm6qmLarW3ZLC4FQxr70S_I4yVNa3ZxlLkOhLrG9evgbTBDJJsl7aJ34wJdQ8-hP_3N-xF_acXM18xfHLIvILJjMEvhJln7yxQ5Mdb-ltg1zitazOg24RezvLdM_bazaeRLukNEl41Cy341hUNM5ole65qpykiim1pqu4p8OV8BlvhTiNNweUOz4GDlBOLpbRXoAWCr5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e12a6efbc.mp4?token=dVHc0paLSfeW2Vti_M-BJFZt_jGAq8A2vyMKVAzveH5DWSkWVZHTpf16cKbKcvxgMYPM7l8zqDpj84_OSKozfvtM9Hag8oK3UawvXO2wKqyEdrmps6asB0EFIAcKz1Pz8lDs3rWPLhbWJQm6qmLarW3ZLC4FQxr70S_I4yVNa3ZxlLkOhLrG9evgbTBDJJsl7aJ34wJdQ8-hP_3N-xF_acXM18xfHLIvILJjMEvhJln7yxQ5Mdb-ltg1zitazOg24RezvLdM_bazaeRLukNEl41Cy341hUNM5ole65qpykiim1pqu4p8OV8BlvhTiNNweUOz4GDlBOLpbRXoAWCr5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک
سنجاب مسابقه بیسبال را به هم ریخت
🔹
این سنجاب از اواخر اینینگ ششم وارد زمین شد و با فرارهای پیاپی، بیش از ۱۰ نفر از عوامل اجرایی ورزشگاه را برای دقایقی سرگردان کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/676448" target="_blank">📅 21:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676447">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02937f3d0b.mp4?token=N1Ps4DAAnFwoipMUc2SQ6M8-EUUjy3eCpCGw8DPmKthScKEg-hHaSBIdTW3UC1TPdmymB1NipHdveQvy_agW58UXOkSKqiHzvHVjzdVBLlE0JPUUABYgnCwmZweK_dpzO71iOms2_8i--raeUwwMduK_MDRMS9RCsNGVmsRgGMK_POSsL1L7MLrLf7Qz6tOjo993mj9yJACgl_4RLlyerYn5r4Q90mk8DFxzNjYApA9aqQs6KSe9XgeFR6wSPXeG7tOOMP7fkI9YNVmKXgQ9ZbPuomdRCSacMaJkiBiKsDl6VKooYjMup1oF1cT5oxOA32y3GjDLTBdMJgb8_6zD5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02937f3d0b.mp4?token=N1Ps4DAAnFwoipMUc2SQ6M8-EUUjy3eCpCGw8DPmKthScKEg-hHaSBIdTW3UC1TPdmymB1NipHdveQvy_agW58UXOkSKqiHzvHVjzdVBLlE0JPUUABYgnCwmZweK_dpzO71iOms2_8i--raeUwwMduK_MDRMS9RCsNGVmsRgGMK_POSsL1L7MLrLf7Qz6tOjo993mj9yJACgl_4RLlyerYn5r4Q90mk8DFxzNjYApA9aqQs6KSe9XgeFR6wSPXeG7tOOMP7fkI9YNVmKXgQ9ZbPuomdRCSacMaJkiBiKsDl6VKooYjMup1oF1cT5oxOA32y3GjDLTBdMJgb8_6zD5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مازیار لرستانی در مراسم بزرگداشت اکبر عبدی: اکبر عبدی نه‌فقط نابغه کمدی، اسطوره‌ای بود سرشار از صفا و مردمی‌بودن، تکرارشدنی نیست/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/676447" target="_blank">📅 21:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676446">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ترامپ اعتراف کرد که جنگ با ایران محبوب نیست
ادعای هاف‌پست:
🔹
کیلمید مجری مشهور فاکس‌نیوز در یک پادکست اعتراف کرد که دونالد ترامپ، کاملاً از عدم محبوبیت جنگ  علیه ایران آگاه است.
♦️
رئیس جمهور گفته است که سایر کشورهای خلیج فارس «در حال حاضر از یک حمله بزرگ هیجان‌زده نیستند.»/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/676446" target="_blank">📅 21:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676445">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
جنگ خودروسازان با توسعه مناطق آزاد یک اشتباه استراتژیک است/ اصلاح تعرفه و رفع موانع تولید باید همزمان انجام شود
مهدی دادفر، دبیر انجمن واردکنندگان خودرو در
#گفتگو
با خبرفوری:
🔹
تعرفه‌گذاری فعلی، غیرمنطقی و غیرعلمی است و باید به نفع مردم اصلاح شود؛ چه جایی بهتر از منطقه آزاد؟
🔹
سیاست‌های گذشته شاید زمانی با هدف حمایت از صنعت خودروسازی توجیه‌پذیر بود، اما امروز دیگر پاسخگوی رضایت مردم نیست.
@Tv_Fori</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/676445" target="_blank">📅 20:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676442">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c6fbe63ae.mp4?token=fOmAWtIy4ZAqBjFcFXpStLXYhbM7Ob8vTdHdhlFpF4dvyFLR03xqRy2kPA5851WB2R2umtTdhA9bnfPsQPLcQMZs2DeIBr1OcyuKSZORSkVG00oOjeXO85iV_QIr6JSMY_FgdEBju1do_4IQpMo8qtcs5Mrl-llaTt2CrtB757OSmXYAg8NZVidAGikcxFFShetxoH5EVW2mj2EPUTMHXJFDQGI0Q_XPjSy2LDSF2XcGdi-BmIBaShbtzQvGvSRLHcVwr0bbGa0_25Gid4G3mjqiafN7DEt80k8YtEmPQ64NaUHcDh6q6A73x8zl5O4cEQHhNXePiF_dLkQptMou8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c6fbe63ae.mp4?token=fOmAWtIy4ZAqBjFcFXpStLXYhbM7Ob8vTdHdhlFpF4dvyFLR03xqRy2kPA5851WB2R2umtTdhA9bnfPsQPLcQMZs2DeIBr1OcyuKSZORSkVG00oOjeXO85iV_QIr6JSMY_FgdEBju1do_4IQpMo8qtcs5Mrl-llaTt2CrtB757OSmXYAg8NZVidAGikcxFFShetxoH5EVW2mj2EPUTMHXJFDQGI0Q_XPjSy2LDSF2XcGdi-BmIBaShbtzQvGvSRLHcVwr0bbGa0_25Gid4G3mjqiafN7DEt80k8YtEmPQ64NaUHcDh6q6A73x8zl5O4cEQHhNXePiF_dLkQptMou8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم منتشر شده از دفتر لیندسی گراهام در روز حمله به ایران #Trash
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/676442" target="_blank">📅 20:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676441">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9TFNrJkhkOBWM-kuy_Yn9IlhBWpowItiAHOJwUJIhZShgImVTVVcM3I7W0wtQ8SaxOwr3e0cSECd8gR9xkyyAFeH8e6SB5wSqOC0lE8hm1os9AkAMf8-HkmxcrEz_H_BYXd8Eb3s9iLa_wablcYb5Yh0dM-joz-f9imXpQFr8bLs9inQrq6XmLrN96pJgCij1G64ZihBsWFK5eHuK-tIKqnZq7PsNBm_NTmtAaFV18KGdvhQQnxn3iEOdhWh61mdkMT6nuRP-J5lkNuokSMuGPPx0eKypFVcxryIbMAjPHOHNpugztn8L3BWQqEniQeTYvDuervQBEzZJadJ7F5Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترفند خطرناک زلنسکی برای ادغام جنگ‌های ایران و اوکراین
پایگاه خبری Responsible Statecraft:
🔹
شواهد زیادی نشان می‌دهد که زلنسکی به‌ دنبال پیوند دادن جنگ اوکراین با درگیری آمریکا و ایران در یک صحنه استراتژیک واحد است.
🔹
در صورت تحقق این سناریو، اوکراین از دریافت‌کننده کمک نظامی آمریکا به مشارکت‌کننده مستقیم در تقابل واشینگتن با تهران تبدیل می‌شود و آمریکا نیز از تأمین‌کننده تسلیحات اوکراین، به طرفی فعال در جنگ با روسیه بدل خواهد شد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/676441" target="_blank">📅 20:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676438">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
روایتی تکان‌دهنده از برزخ؛ از راز رزق تا شفاعت حضرت زهرا(س)
🔹
00:02:00 اهمیت و جایگاه والای "محبت" به هر جاندار و بی‌جانی
🔹
00:06:10 حمایت بانوی دوعالم از هرکسی که محبت ایشان در دلش باشد
🔹
00:10:00 بازیگری در فیلم نامه‌ای که خودمان نوشته‌ایم
🔹
00:18:10 سبک شمردن نماز ، روزی دنیایی و مسیرهای برزخی را محدود می‌کند
🔹
00:22:30 وظیفه اصلی هر انسان چیست؟
🔹
00:30:10 سیاهی قلب‌های ناامید، حتی در هنگام خواندن نماز و دعا
🔹
00:39:30 به حرمت کار خیر مادر همسرم؛ مرا شفا دادن
🔹
00:58:50 معجزه‌ای که برای من اتفاق افتاد
🔹
قسمت پانزدهم (مهر و امید)، فصل پنجم
🔹
#تجربه‌گر
: حسین صاحبی بزاز
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/676438" target="_blank">📅 20:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676436">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c101f5d684.mp4?token=onzlnTFGcfHVXRvwRhiva7FAiu41XhfoYarwQPNWdt_KyuPwFWLTqxb76U_TiSw4WWDPwu9x3UxvudoiLSA9L-nOp_zeVXlgZirrN0VYIlLcAaMWqzWBLd7NX0VHgNWfCM-QLz6jMEZD18WuTa52614rIsGQN81YMiMcveN1zrkTytC_NHhir7FnIB2NTZQqmOm3WkIE9hvfaKy3hlZ46CIt_nXdsuOh5nMqdXtMldqtC1M6UZhlGmnR4oK3d5dZV88XpCC_tgrWycF8sUvE-G4tlYpj_UfKH8gVkkjOGa8rEGukAUQwAJZW7XDtccAOsQ3R554FgjfijPTJAo5m0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c101f5d684.mp4?token=onzlnTFGcfHVXRvwRhiva7FAiu41XhfoYarwQPNWdt_KyuPwFWLTqxb76U_TiSw4WWDPwu9x3UxvudoiLSA9L-nOp_zeVXlgZirrN0VYIlLcAaMWqzWBLd7NX0VHgNWfCM-QLz6jMEZD18WuTa52614rIsGQN81YMiMcveN1zrkTytC_NHhir7FnIB2NTZQqmOm3WkIE9hvfaKy3hlZ46CIt_nXdsuOh5nMqdXtMldqtC1M6UZhlGmnR4oK3d5dZV88XpCC_tgrWycF8sUvE-G4tlYpj_UfKH8gVkkjOGa8rEGukAUQwAJZW7XDtccAOsQ3R554FgjfijPTJAo5m0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر دیگر از تشییع با‌شکوه زائران و رزمندگان شهید حشد شعبی در عراق
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/676436" target="_blank">📅 20:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676434">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3CY3f1VwH6km3UsO1vnrL91G9wsJNDBNB2koARCpVZc0Ooh6ioGeCKtqtp2mmYa6GZmqAvBjipsuDBvjcqqkcT9BeitFdcyVa6V-p3B-CQFIpn8ByWNJo15a1jRn9SpgK7azQsn0CBVoYWZfNFCdCMOgeZ2hWbGjNhER70VUehLJF7Ex1gCcEhtF21Xw4682V6_nBUiNwb7xCfSJaJtljNHeJerdZONIplj5E1MhsRZF5MPHau_lCuAy807rK-06_NXaq3EM0GV_tDjQxlHmJN3W6ijJpafaD5aVBHgsExePpwd4BGUh94HeGXI43kojmDRfYOgDTd-iRJsoDXZ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیدگاه افکار عمومی، آینده جهان با چه مخاطراتی روبه‌رو است؟
🔸
در این نظرسنجی بیش از ۲۷ هزار نفر شرکت کردند که سهم روبیکا حدود ۵۵ درصد، بله ۲۷ درصد و تلگرام ۱۸ درصد بوده است.
🔸
بیش از نیمی از شرکت‌کنندگان، بزرگ‌ترین خطر آینده جهان را جنگ‌های فراگیر و گسترده و حدود ۲۰ درصد نیز نابرابری‌های اجتماعی دانسته‌اند.
🔸
روندهای جهانی نشان می‌دهد ریسک‌های ژئوپلیتیکی و اجتماعی به مهم‌ترین چالش‌های پیش‌روی جهان تبدیل شده‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/676434" target="_blank">📅 20:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676431">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3a1eecbda.mp4?token=Wg5NzptfZzTOU6r-RHt94HV5jQNJSU-BEde5WAkNf8f0AZg94JXA3OVCy_pB953cw66KaFJEJ14sQWplq8yolwV5S8cv7fZpvZtU3SDrq3vrRcWpAwx6Q_SrrU_VFzfwCNmwP4j-tz9gMTrQs_gKO9LZtw5T5UaGJJPv_O7VY2JSD-Egjux4MNCGszVX9I_Kqwl7m-xt6_56rdQlnMyyPp4_bYzkSihUMXh3HGMv7JyZ9YcAlQOW1-fMEaRnuVaVANPgb3EralOGfHALuBhozZrdxYlfRxHC8YTlZXRPfmAp55aDbDxJrYq-LoA65zj-qzTJ2GL96IaX9qRilYyvrKd1bqSQhRZeAR1WbI03V2es7GoICV-RsroctfwKn6hm7_K_JSUWjjNoF_fEGnT0NLmoQy2vrHZ8bf4PRBzMman7hRxWLYiDQPicteMD8ts_hQ-ZiyIxkO1kbkeSCdQRM4MxW2vmw90TvOjlkJvO-zxzKFsiu5Z7l82-WBEKE6lWvfp67qsGzTXC48TJNnZBiydEoeraJ3nul9Q7mYgLroeTrAvnoBtm3AtjS-wpT-qKqb2iyDEmfFOuFeElMg_wIICuvKmk0JFGCgNGb35Hs7guhybHgy0SneViJ2dMktwWlv9uFhe6kemHFu6B0siv5seIUmcXSQPowkMrOtW6SOc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3a1eecbda.mp4?token=Wg5NzptfZzTOU6r-RHt94HV5jQNJSU-BEde5WAkNf8f0AZg94JXA3OVCy_pB953cw66KaFJEJ14sQWplq8yolwV5S8cv7fZpvZtU3SDrq3vrRcWpAwx6Q_SrrU_VFzfwCNmwP4j-tz9gMTrQs_gKO9LZtw5T5UaGJJPv_O7VY2JSD-Egjux4MNCGszVX9I_Kqwl7m-xt6_56rdQlnMyyPp4_bYzkSihUMXh3HGMv7JyZ9YcAlQOW1-fMEaRnuVaVANPgb3EralOGfHALuBhozZrdxYlfRxHC8YTlZXRPfmAp55aDbDxJrYq-LoA65zj-qzTJ2GL96IaX9qRilYyvrKd1bqSQhRZeAR1WbI03V2es7GoICV-RsroctfwKn6hm7_K_JSUWjjNoF_fEGnT0NLmoQy2vrHZ8bf4PRBzMman7hRxWLYiDQPicteMD8ts_hQ-ZiyIxkO1kbkeSCdQRM4MxW2vmw90TvOjlkJvO-zxzKFsiu5Z7l82-WBEKE6lWvfp67qsGzTXC48TJNnZBiydEoeraJ3nul9Q7mYgLroeTrAvnoBtm3AtjS-wpT-qKqb2iyDEmfFOuFeElMg_wIICuvKmk0JFGCgNGb35Hs7guhybHgy0SneViJ2dMktwWlv9uFhe6kemHFu6B0siv5seIUmcXSQPowkMrOtW6SOc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اندر احوالات اختلالات بانکی؛ کی بود؟ چی بود؟ چی شد؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/676431" target="_blank">📅 20:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676430">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🎥
تجربه واقعی تزریق زیکورپا؛ از زبان یکی از مصرف‌کنندگان
شنیدن تجربه واقعی درمان چاقی با
آمپول لاغری زیکورپا(داروسازی دکتر عبیدی)
، دید بهتری نسبت به روند درمان به شما می‌دهد.
یکی از مراجعه‌کنندگان
کلینیک آئورا
در این ویدیو از تجربه خود، میزان کاهش وزن و رضایتش از روند درمان می‌گوید.
🎬
ویدیو را ببینید و تجربه او را از زبان خودش بشنوید.
☝️
برای شروع درمان چاقی با زیکورپا، از مشاوره رایگان پزشکان کلینیک آئورا استفاده کنید.
👨‍⚕️
رزرو مشاوره رایگان
کلینیک آئورا (جردن|سعادت‌آباد)</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/676430" target="_blank">📅 20:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676429">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6730bf1abc.mp4?token=DTGVR8AtA15TyNy5rvSG3VVx3DDAqkyxd2WYfm8lkksMjbwTMJfGtkL3vuRH2oPk3RCBuoh1PC2aKoGBkV_t4A6biCLSmtHqZ4hrsPGj7vjjJguAZTiG9h3dFx3rEmx1c5-xhMYkeOcBAVl3eIh1zwS1Cpvt9rfd-RLETRBMhmTzoRlHSuMXsaCfyEBk0bC_g1vaErQzHQCshxuyvu9sMdjKat-71eSo5kxSjpvWpcxMI8KtVpeCb2dYoSIHA3ydlroZi3_WwZqZezRgoTQCoyFOc14La9ir1KLIMVfhzjaIfK0D7On7UztdYQMsRAdxbgFU3MWikT3FqciJaF0c2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6730bf1abc.mp4?token=DTGVR8AtA15TyNy5rvSG3VVx3DDAqkyxd2WYfm8lkksMjbwTMJfGtkL3vuRH2oPk3RCBuoh1PC2aKoGBkV_t4A6biCLSmtHqZ4hrsPGj7vjjJguAZTiG9h3dFx3rEmx1c5-xhMYkeOcBAVl3eIh1zwS1Cpvt9rfd-RLETRBMhmTzoRlHSuMXsaCfyEBk0bC_g1vaErQzHQCshxuyvu9sMdjKat-71eSo5kxSjpvWpcxMI8KtVpeCb2dYoSIHA3ydlroZi3_WwZqZezRgoTQCoyFOc14La9ir1KLIMVfhzjaIfK0D7On7UztdYQMsRAdxbgFU3MWikT3FqciJaF0c2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احتمال اصابت پهپاد به تأسیسات ذخیره‌سازی گاز در بندر دمیاط  سی‌جی‌تی‌ان:
🔹
یک تأسیسات شناور ذخیره‌سازی گاز مایع با مالکیت و بهره‌برداری آمریکا و با پرچم جزایر مارشال، دست‌کم هدف یک پهپاد قرار گرفته است.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال…</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/676429" target="_blank">📅 19:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676428">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b57d7228a9.mp4?token=HFiiPNZUhf81MFAethJRgC7A9tdPUpDzxNpMhrimmcaz2FO0XShPlAPj_VFAql2nPmzyHgVxtBzzGfVQ5WLqP1FLj5w0LKCeTG3UNQCBwN6D-jN4QwN8w0jU7dL2AlnMTo0V8Ke1AMc7wOMWdYH9VcDMTmTqMGjtLGCWYQc__7zUHOUysmU9h_x7cgTxqt1V6CDoUq8gSv6aXuSQZw9eYlM9asEMbMnjzHgQe6UT5ndnW9zIeSzwbLNP893g7VIwrV_2QdbREvvlBhCIDYdjbNtOsU-gpdgmXDIFvieZ7h4Ut3h2yzC9O4fDgwQQD9DAHwIhs2c1oBV55bNju3FE8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b57d7228a9.mp4?token=HFiiPNZUhf81MFAethJRgC7A9tdPUpDzxNpMhrimmcaz2FO0XShPlAPj_VFAql2nPmzyHgVxtBzzGfVQ5WLqP1FLj5w0LKCeTG3UNQCBwN6D-jN4QwN8w0jU7dL2AlnMTo0V8Ke1AMc7wOMWdYH9VcDMTmTqMGjtLGCWYQc__7zUHOUysmU9h_x7cgTxqt1V6CDoUq8gSv6aXuSQZw9eYlM9asEMbMnjzHgQe6UT5ndnW9zIeSzwbLNP893g7VIwrV_2QdbREvvlBhCIDYdjbNtOsU-gpdgmXDIFvieZ7h4Ut3h2yzC9O4fDgwQQD9DAHwIhs2c1oBV55bNju3FE8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد مشترک آزادگان ایرانی و عراقی در طریق نجف-کربلا: ترامپ را بکشید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/676428" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676427">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-B8voRgvqBD8wEZK8P7xR-tYCPmydocW4ov1RAmf5uD04M2Vjn9llX9uTBVal4HNF7I9_Nk6J3_3YpuHn4DfOMGKyu-kuBDl-y9-YLdfUKFmBmZDAJ5fPDGdUfOP2hMq4eO5zuxeey2JuxLeWwrlSFmUzeNlLvMZWL-uWNhRj607qMU3FAAXnN2rIT6dNewzWEyKHM8M06wvh5EBI_Xp2-MStbRZCHQ358N1_shEAw1yl_pk68dmQDnXl5knE4IOau_mLTwxhd7xkxmUKZvm6U0kGm4-eYwMlNnhBbNpqmqTckoVMvrRAigMNG0T4xzQQw7X7bYyXJAkETKhNtrSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
مسیر عاشقی پر از فرصت‌های ناب است.
▫️
فرصتی برای اینکه برای چند دقیقه هم که شده، بار خستگی را از روی دوش یک خانواده برداریم. با همین توان کم، میزبانی کنیم.
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/676427" target="_blank">📅 19:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676425">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37de8e66d6.mp4?token=EapXWZE3ymSwjvO1QqsQ76-PoP33CnqwXcN4d-LupKMyTjljUYelhFtUd22D0aFE3IzGrjpLuJUnrBivvuds5l9j4lisAoVWvVOCFTexCj31BXhc11V3CyIcpySxr_ZXgMjBogdFQizN3Dv4SQaadceO_64dudvidctlAawdI0GU2WuyrvtOF5MVlehToRFLD_NFX_kO9fm4CY8crKbMmyQqxuYUUJ6Gxs8UncKRjuSaRMd050bDtoOLk1z1Dd19Hy-6mTFKtlqzSsMVNvFWZwL1AMs4_BZ_Gs1ypVnL-ZINIAPAWKe767ZrAKSZs1ZkQEZOF-5yHQqLWAyatHqeFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37de8e66d6.mp4?token=EapXWZE3ymSwjvO1QqsQ76-PoP33CnqwXcN4d-LupKMyTjljUYelhFtUd22D0aFE3IzGrjpLuJUnrBivvuds5l9j4lisAoVWvVOCFTexCj31BXhc11V3CyIcpySxr_ZXgMjBogdFQizN3Dv4SQaadceO_64dudvidctlAawdI0GU2WuyrvtOF5MVlehToRFLD_NFX_kO9fm4CY8crKbMmyQqxuYUUJ6Gxs8UncKRjuSaRMd050bDtoOLk1z1Dd19Hy-6mTFKtlqzSsMVNvFWZwL1AMs4_BZ_Gs1ypVnL-ZINIAPAWKe767ZrAKSZs1ZkQEZOF-5yHQqLWAyatHqeFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مازیار لرستانی در مراسم بزرگداشت اکبر عبدی: اکبر عبدی نه‌فقط نابغه کمدی، اسطوره‌ای بود سرشار از صفا و مردمی‌بودن، تکرارشدنی نیست
/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/676425" target="_blank">📅 19:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676424">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7033b797.mp4?token=ewfTyHTsLDPCABDD313K08xleG-OWkb0My7-DHvVVZvtPiSNLh8acLDs7K3cF6Ryv-J2G4ImI5yCzYWe70-G2IyxrK7hHltfYhEtOi5EQmYsflzqAhkOdmia8s8nnGula_DyA0IDTAB1lL7ZlQU5ttx8UG1b4pY7cnX30LlLgh8yGgEOjnHQ-1fKq-reA1srNSFUwHTM1wLNsvzyY-8YZcsV6RIMukK7Ns_lZeLzR5rtnliwIAMmE8w7gqkj7Vf3YblK8AW1wrDVnG6ZvZZQsg9NK2cQagDyWJKgKFkmh42SzMRZdjJOXvmz6MevpGj7qGKsgejrj2e4VbOUSNEdp5GpgAFNlhayFj29W8WSXcG0pXE9xNw2Y9lbVT-R5UMMWMyHC-tandEIrwTX0HF17HDKa81GKAeBbc7a656YbaRjj19_sKZP9BHJERxCO_hMUaS0UjFRBWMZMh_5xuinAa8hK_9ncBDjKW8cMvuQdJKv2YTjI1ETENb9bzVdtZionsl0dsDMFQGZPQHjN_UtfLVUEYRFuzHkLnsNfXOk2Eg0YuJj7fgny_z5kI-9r7HjmRutetJX2BRnqxd-rQWWC6NIiavIZBQtkVZoiQfd5Bp4or8_krV5VYtxl1vKnUP6WvA16AdMniS0pnCZWJdF0DLXguEPFKR4Ab3XQkgJ3t4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7033b797.mp4?token=ewfTyHTsLDPCABDD313K08xleG-OWkb0My7-DHvVVZvtPiSNLh8acLDs7K3cF6Ryv-J2G4ImI5yCzYWe70-G2IyxrK7hHltfYhEtOi5EQmYsflzqAhkOdmia8s8nnGula_DyA0IDTAB1lL7ZlQU5ttx8UG1b4pY7cnX30LlLgh8yGgEOjnHQ-1fKq-reA1srNSFUwHTM1wLNsvzyY-8YZcsV6RIMukK7Ns_lZeLzR5rtnliwIAMmE8w7gqkj7Vf3YblK8AW1wrDVnG6ZvZZQsg9NK2cQagDyWJKgKFkmh42SzMRZdjJOXvmz6MevpGj7qGKsgejrj2e4VbOUSNEdp5GpgAFNlhayFj29W8WSXcG0pXE9xNw2Y9lbVT-R5UMMWMyHC-tandEIrwTX0HF17HDKa81GKAeBbc7a656YbaRjj19_sKZP9BHJERxCO_hMUaS0UjFRBWMZMh_5xuinAa8hK_9ncBDjKW8cMvuQdJKv2YTjI1ETENb9bzVdtZionsl0dsDMFQGZPQHjN_UtfLVUEYRFuzHkLnsNfXOk2Eg0YuJj7fgny_z5kI-9r7HjmRutetJX2BRnqxd-rQWWC6NIiavIZBQtkVZoiQfd5Bp4or8_krV5VYtxl1vKnUP6WvA16AdMniS0pnCZWJdF0DLXguEPFKR4Ab3XQkgJ3t4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروج پر دردسر علی دایی در بزرگداشت اکبر عبدی با هجوم مردم
/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/676424" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676423">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnLM5UNjIr77rbweJtd8fb8vYQgFiVo0Yt6bw89v0ga3E2zYVs_OCB2jyMLqQRT3CfTse-DlIbPPqKQE2s_SheixnS1rzJPMb083ypL8QOBiV92eNMiTN9MWdxPe4S2aIdifWKLDakfdPSV7vL8jUEc9Z4LR7iZtYLFja1lYyHz1O6MnD648WQ3fo1qBCXbbCPNksHxClEKc2zwpj8o2F-j_YoQVo8XeERYM3mkpjvxX-2YmlneTmDho8CBuLwTm5Ah9KXIZO4aEBT23hWwtr_Bvb3MCDYPCz2jNDhfRciBlydW-HkPaLWftbHyBFbZaFuTiPMBn21TTatYK7G4rtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هلاکت عامل تروریستی در بوکان
نیروی زمینی سپاه:
🔹
عامل تروریستی وابسته به گروهک‌های تجزیه‌طلب که به منظور اقدامات ضدامنیتی در شهرستان بوکان حضور یافته بود پس از درگیری مسلّحانه با رزمندگان قرارگاه حمزه سیدالشهدا(ع) به هلاکت رسید.
🔹
از این عامل تروریستی ۲ اسلحه کلاشینکف، ۶ خشاب و یک  موتورسیکلت کشف شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/676423" target="_blank">📅 19:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676422">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
احتمال اصابت پهپاد به تأسیسات ذخیره‌سازی گاز در بندر دمیاط  سی‌جی‌تی‌ان:
🔹
یک تأسیسات شناور ذخیره‌سازی گاز مایع با مالکیت و بهره‌برداری آمریکا و با پرچم جزایر مارشال، دست‌کم هدف یک پهپاد قرار گرفته است.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/676422" target="_blank">📅 19:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676420">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25c29d6742.mp4?token=sqX07ZHky0bfhJbBzUjvw7jHGW6tUxpd_-qkV7Rv8OX32mrqIYuSQ-vmZbamjPFvm3zlN4Jo9JbXD88pyHhtldwSD38yfjfMm_j8oF6BMqjmJoLWfVGgSp92q-JJAyv6kKmBKBk1gBane_tDrHO9-1bhB8uCdY7M0L6nDpID5HeWQKZ7gYWyvhimV3Jfgi02Kql9xDoaqCd0MVL70e5ICq0zNCmjiwPZmYJir4UnFuSf3IdZxrliTqzTwFmaQsWC0BQfdBjeNBeTWXq2foxjFx_NQ7wj8Uffuj1BZrDuTXmDiwxuS-2aU2pjR_5JspzAyn9RLPcKnHAKef2cmwhB1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25c29d6742.mp4?token=sqX07ZHky0bfhJbBzUjvw7jHGW6tUxpd_-qkV7Rv8OX32mrqIYuSQ-vmZbamjPFvm3zlN4Jo9JbXD88pyHhtldwSD38yfjfMm_j8oF6BMqjmJoLWfVGgSp92q-JJAyv6kKmBKBk1gBane_tDrHO9-1bhB8uCdY7M0L6nDpID5HeWQKZ7gYWyvhimV3Jfgi02Kql9xDoaqCd0MVL70e5ICq0zNCmjiwPZmYJir4UnFuSf3IdZxrliTqzTwFmaQsWC0BQfdBjeNBeTWXq2foxjFx_NQ7wj8Uffuj1BZrDuTXmDiwxuS-2aU2pjR_5JspzAyn9RLPcKnHAKef2cmwhB1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احتمال اصابت پهپاد به تأسیسات ذخیره‌سازی گاز در بندر دمیاط
سی‌جی‌تی‌ان:
🔹
یک تأسیسات شناور ذخیره‌سازی گاز مایع با مالکیت و بهره‌برداری آمریکا و با پرچم جزایر مارشال، دست‌کم هدف یک پهپاد قرار گرفته است.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال کنید
👇
@AkhbareFori_Ar</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/676420" target="_blank">📅 19:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676419">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعایی عجیب؛ پزشکان ایرانی در حال مهاجرت به عراق هستند
رامین پولادرگ، رئیس اتاق بازرگانی ایران و عراق در
#گفتگو
با خبرفوری:
🔹
تجارت ما با عراق متوقف نشده است اما شرکت‌های عربی از ترس تحریم‌های آمریکا و اروپا نسبت به تجارت با ایران بی‌میل شده‌اند و هزینه تجارت ما با عراق به همین سبب پر هزینه‌تر شده است.
🔹
عراق در زمینه‌های ساختمانی و برق به ایران وابستگی دارد و ما نباید این بازار را به چین و ترکیه ببازیم. در زمینه توریسم سلامت هم ما هیچ اقدامی نکردیم و این بازار سلامت در دست دلال‌ها اداره می‌شد. اکنون پزشکان ایرانی در حال مهاجرت به عراق به خصوص اربیل هستند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/676419" target="_blank">📅 19:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676417">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0f525e84e.mp4?token=JS2W6suz73glw7uKxyzvTHlFNDMzZ88jto5Rv6GfzJfbKGZDkx3ahXByow_YyWYYzsKmkJVlLOw7305mFgDR9CieuLr_OuX-tFTCXK0WNDuJQgKDff4Rv9BDVzEJS6a3r55Jin4DLW_1chhwfKZzXvIr0AxDVfemcjRE6Oj6V7arFuiOtFggBunmVo6JTiJyw8iiKn9WXtYTGeXfCbWUb6acIXZsxh2871N99pCQ4XmJY-SKZi9Ie5a05tsgByQBxW-ZQv9xaWEXXCI2Mj91ZsM8_EARFrv18HbGHc30_k1HfWMB-BLsSeiyzCF5oQZvHUzOZ6jeQx2upt0oHzi9NYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0f525e84e.mp4?token=JS2W6suz73glw7uKxyzvTHlFNDMzZ88jto5Rv6GfzJfbKGZDkx3ahXByow_YyWYYzsKmkJVlLOw7305mFgDR9CieuLr_OuX-tFTCXK0WNDuJQgKDff4Rv9BDVzEJS6a3r55Jin4DLW_1chhwfKZzXvIr0AxDVfemcjRE6Oj6V7arFuiOtFggBunmVo6JTiJyw8iiKn9WXtYTGeXfCbWUb6acIXZsxh2871N99pCQ4XmJY-SKZi9Ie5a05tsgByQBxW-ZQv9xaWEXXCI2Mj91ZsM8_EARFrv18HbGHc30_k1HfWMB-BLsSeiyzCF5oQZvHUzOZ6jeQx2upt0oHzi9NYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطره پرویز پرستویی از فیلم آدم برفی در مراسم بزرگداشت اکبر عبدی
/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/676417" target="_blank">📅 19:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676416">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ادعای انتقال سانتریفیوژ توسط ایران به کوه کلنگ
یک مقام صهیونیست:
🔹
ایران سانتریفیوژ به کوه کلنگ منتقل کرده اما ما از اینکه آنجا غنی‌سازی انجام می‌دهند یا نه آگاه نیستیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/676416" target="_blank">📅 19:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676415">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7c8063071.mp4?token=dqzNgkAZN9o2ICy3SsRxyzpQHiBLvbDo9dOayWv43rjBFjTafrR_ubWW6BBUbxNKbWploxuuZy9eOiiDfk0ZIKOV7n0xyW6Gvypl6WgL66WVzL4XPL5384iOF7-efY7NBsZI94tYIp-Jq67fqKN82wA0O2KCmHCONrQY7EEYOQ8-LoOxZhFZqPl2bxR0D4zEdp4bjDw0FNiMaq4vXd45m5Swg4JTyXxdanr_rM3ZoWs9dlKjixaLMaNnHB19LI5Cs1kl4i_7StzJ2BxLFixDx-YLyz7HDC5kCrqRkeGlHUG8gH0y8FQuQbkEjjw71Mcwy2pDrOh92VXqW-DUyrcfEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7c8063071.mp4?token=dqzNgkAZN9o2ICy3SsRxyzpQHiBLvbDo9dOayWv43rjBFjTafrR_ubWW6BBUbxNKbWploxuuZy9eOiiDfk0ZIKOV7n0xyW6Gvypl6WgL66WVzL4XPL5384iOF7-efY7NBsZI94tYIp-Jq67fqKN82wA0O2KCmHCONrQY7EEYOQ8-LoOxZhFZqPl2bxR0D4zEdp4bjDw0FNiMaq4vXd45m5Swg4JTyXxdanr_rM3ZoWs9dlKjixaLMaNnHB19LI5Cs1kl4i_7StzJ2BxLFixDx-YLyz7HDC5kCrqRkeGlHUG8gH0y8FQuQbkEjjw71Mcwy2pDrOh92VXqW-DUyrcfEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود معترضان به هتل نتانیاهو در واشنگتن
🔹
گروهی از معترضان به نسل‌کشی اسرائیل در غزه وارد هتل محل اقامت نتانیاهو شدند و علیه او شعار دادند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/676415" target="_blank">📅 19:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676414">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33ccefbfe.mp4?token=mMf3odjeHUY_YuMrFJMkmj7uhxGXlBK_82QuhBmdlY-q724zhwx_WQ-s38MkpByvI4q_fAA6GlQWUBC7QXzonWfPtrW2qClMxkhmI97c-HDNrPYQj9uD3i92vzw70yueq2nMz4ErG-9EixmHJhQUmdhmKxrB3oLaMG66VKHSwsqMDJG6Y1bn6NCY95PV96x2KD48Mg3T2yd67eXnQbXBBNDwgEWeDMp4-vxwFd95iFCrvNFQf-uZ6GB3FZVO39B5BJtIQz4T9u6HezzL6MSprJmEqavH_9rOeICvtjiwF0mugKsH8IKWkKMZvx2FAFCd3KDM-u1YBwgKRNrG8deVeAzvWbPmMZPqiMJvtLAB_VuHKlL7iZIOXshoi5LibdR0eJJC1p9KQTO-7IJGb24em6rlS57PwOmTFUFJEkVI33bE8Jv6P6FEu5duRcHdIlWVEtsZ3WS1uZeseLDVm1W9jt8JntlrVb0PPl-wJMIVH4jmIE2f7es0QPMLdUFjDwx7u9Df5pP8UudCx45VHbJC0OJwOGrL712r7GJoQJh07Gc5Yr_0BRYoOZVLvPItTNgpecZWHiIFvvOc2lDCgc4vvcN4ujrgQsPOpiFdROKmaXcT58XkFllkmQRwJwG_dUUNaqyi2UjSWzXWjmtI4795RjtoI3hL9EoCo-rt4TacAt8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33ccefbfe.mp4?token=mMf3odjeHUY_YuMrFJMkmj7uhxGXlBK_82QuhBmdlY-q724zhwx_WQ-s38MkpByvI4q_fAA6GlQWUBC7QXzonWfPtrW2qClMxkhmI97c-HDNrPYQj9uD3i92vzw70yueq2nMz4ErG-9EixmHJhQUmdhmKxrB3oLaMG66VKHSwsqMDJG6Y1bn6NCY95PV96x2KD48Mg3T2yd67eXnQbXBBNDwgEWeDMp4-vxwFd95iFCrvNFQf-uZ6GB3FZVO39B5BJtIQz4T9u6HezzL6MSprJmEqavH_9rOeICvtjiwF0mugKsH8IKWkKMZvx2FAFCd3KDM-u1YBwgKRNrG8deVeAzvWbPmMZPqiMJvtLAB_VuHKlL7iZIOXshoi5LibdR0eJJC1p9KQTO-7IJGb24em6rlS57PwOmTFUFJEkVI33bE8Jv6P6FEu5duRcHdIlWVEtsZ3WS1uZeseLDVm1W9jt8JntlrVb0PPl-wJMIVH4jmIE2f7es0QPMLdUFjDwx7u9Df5pP8UudCx45VHbJC0OJwOGrL712r7GJoQJh07Gc5Yr_0BRYoOZVLvPItTNgpecZWHiIFvvOc2lDCgc4vvcN4ujrgQsPOpiFdROKmaXcT58XkFllkmQRwJwG_dUUNaqyi2UjSWzXWjmtI4795RjtoI3hL9EoCo-rt4TacAt8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخستین تصویر از پیکرهای مطهر شهدای ایرانی جنایت سعودی_آمریکایی در حملات به شهرهای عراق/ جماران
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال کنید
👇
@AkhbareFori_Ar</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/676414" target="_blank">📅 19:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676413">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbSePobNdh6aoaJrRE8tlft45o3AzAhKyS-ena7pXD8iaOPQ2lCH7QUU_4SXc5hDuPeV_jiCU-6xaaeCUmVLHi1IHJVHIlfpZQFjHETBr-kisLB6XsaSsc7n3RguIbEFs-tJJH22oXduGdFrO5DrKb50LiNElIs8sx36pLseCvt9keqsVXNu_3rq94rglNQUI32JZ68DT1fc6PsIgCB1uvttGHdMU7WXus-oOIat7jTh4jlI2sJNjnUix9y3Y9iRNv4BYuK-7T3GgyY6pCxPogLU2um_iqBd4Zc4c0IORS1n6BhAZGAoojcEDNVVfDtlVUAzFYoU6cIKlp0LgnzddA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بختک؛ موجودی از جنس تاریکی که روی سینه‌ها سنگینی می‌کند
🔹
در فرهنگ عامه و باورهای کهن ایرانی، «بختک» موجودی نامرئی یا به شکل یک عجوزه‌ی زشت‌رو و کوتاه قد است که شب‌هنگام، زمانی که فرد در خواب عمیق است، ناگهان بر روی سینه او می‌نشیند. کسانی که بختک را تجربه…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/676413" target="_blank">📅 18:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676408">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVEwrE2QzCS6TmgArB8eLGySZCUjXUBPMfKrOyktlbltmGDU8NCuql0PzF9qs4nifRJR2YW4re_mwZRdgrUZeGBK1LKEh0UbCFJ7Xa66MgLZls9OxYosWldqEa7J2P0bHjtgNVn9XI6n5mG9uqlRr_V4iTsGSexcJPp4S2ZYl-TvMfsducU4oHQaOBZyaE6FvuDO-J-8t6FczbrKqAjiJe8BO46m-yw9vgATAd8G4kwmwg6_bwBQHdqDoW0yQ3qbYSE2w9jkLbrNj2R2tW90JKdpUkjFm3_m549uRYbnXOFz-sHix9lQtV5y_Ezi98-05KGLwXPpWJS5vrJaWK7AeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aaIWXPzxyYTk26sangQT3yYSyqmxU0uhUHeUqkg-WGQMhrGaOfQbCww0NVnbJOu-E5CBAkxs5IRkdrgaGEwXeaRBFfEAjMuE4M_bivp8JZnjjHXi0od7WaM5anl4TeeEcGxtYdemG-sZ7VYB0au5VYGqttTXMbxrGHiwUIaEwwKdzFWL1ibIOG87zg3omQBcNlu5UTtbFzfoF4Gf7MYLX9MYGIO2WURGqKaZHnqvq6nx2l5NLVqgrrEYNfkYNDpDhIoNP5LkLhvPl3T-1ieCjDDUO9gUeegCGSnCmVFhWqSQWJZt29WlSkfxTvIvcks0I-n3nvR6LG9Z1-ssTD-8Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sSmeX_AGiO4vxxVg-oyu0OtilSL6T9U6Z3lnrCXbCaDsJDhcbmMgLCOG1vpnJnl46Jc6J1VRuAjr7eDjXmiCc4S5yeGvef8pj-ULezN7vjBiP9KpUpFzJdRXwEVE3_vi_fpz5G5Z81XajggpyIwENKadcWP8LNX6WG73kqqIOgu6LIrmkryBANtNZQws0Qw24v0TPIq9-tnEFhdFDIKA_QAbNTguW8q7HhhFzgj3fZIuAtF5PVSH6_15AdRqsk76x0TdVo77uZwSW1dFApbjkNQ-3f2R-pUz-_2CB9RlMdEy5WPmRq7RsUerAeRPmLi4KiCa5J3riTIvJPey6OwqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WsoxOPZvvDXJBbK5emnLhH-nXf1N7qcHo_89DQSYin9pHbCj4oZXH7AkxmEhV-K0u90GBHeiI5auSCZRbu1LN9-D1wSZe3vvAZvcUW916UUIHa13JiOb7IDul7yWcGK4kjUpBcsOPm60iy05II_i-3j4K4n4WRY7xyHJKyR7VGGA2G0tEyOOVxSJ1btxJgr62t5vI-wZlab6rjAz2-H-k9UHoiI3fwJV5miPj6-gObjigidaWtsHz4WObVKGW0YDdDUF7PvSgzV1J0aYppezxErtIRKbGVpsgJtOXGmIEqrf2egyRtgEXTerHJ3_-RarY2bhCsCl1u64paOP151cyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jC62Ff72lthQQ696ZnAXK9AmGDL2UpWCEpclbfzRn5QwFiIobpsEb-mdN9iUcqHoF9gqtaClGhu7e6GujyvEtRyzOSeExKIt-JokOSnzxEI3VhwRh5z-QktzqgzKbZjhRyepJ4E_KPrFyZK5g7vz4OU4Y-k6a-hSeCwjayjynJUKvu-xJqDfGYz-XUzZPDZI2LGz-MnO1WIXmKxBtG3Y478ATe8aV5rIioiIgJwEc9zb2ofZwzEpQ6pQPjXdVKRJ0so_G619-68v5zp0-QuA2iPHBimGZkdIIBwgFRqlm-cWHwkl9MI61zk5A-NYpR39FPRE-qGbg2Oe896qfzWD6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اوکراین در تیررس موشک‌های ایران
🔹
اگر ایران بخواهد از خاک خود اوکراین را هدف بگیرد، کدام موشک‌ها به مقصد می‌رسند؟
🔹
در این اسلایدها با موشک‌های بالستیک ایران آشنا شوید که از نظر برد، توان رسیدن به اوکراین را دارند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/676408" target="_blank">📅 18:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676407">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
کاهش شتاب تورم در تیرماه
🔹
دکتر مهدی زاده مدیرکل سیاست های اقتصادی بانک مرکزی:تورم ۳.۶ درصدی در تیرماه در مقایسه با رقم ۷.۴ درصدی خرداد و ۸.۵ درصدی اردیبهشت حاکی از کاهش شتاب تورم است و به معنای کاهش سطح قیمت نیست.در واقع روند رشد شتابان قیمت ها نصف شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/676407" target="_blank">📅 18:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676406">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
پول بازار دارو به جیب چه کسانی می‌رود؟
🔹
بر اساس داده‌های رسمی، برای ایجاد بازار ۴۰۰ هزار میلیارد تومانی (۴۰۰ همتی) دارو در سال ۱۴۰۴، حدود ۲۲۲ همت نهاده مصرف شده است.
🔹
بررسی‌ها نشان می‌دهد پس از کسر حاشیه سود ناخالص ۷۰ همتی داروخانه‌ها و ۳۰ همتی شرکت‌های پخش، تأمین‌کنندگان دارو در مجموع به ۷۶ همت سود عملیاتی دست یافته‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/676406" target="_blank">📅 18:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676405">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQhrVfvZfqP_RZ9XCGU4MJRIbbYk5jJyShGkpNl4bFejei2i8yhoYHjiVTFROR--AVQ6B4iIh7-j4iWJ8_kqCpgzSbuLA6mw4hh1HWy3m4zX9sTHDZifdVCzCMNgk2hto3TaNglAdnXQvzMAHJniKqTxtzQo473FRlNDGKK_o0S5v1m0SKaaSoRsbjqaQ1qQOBJqehGilxOUKYNFcPpj_cndJ6QfRW0_RV0VzbNijFKiM4tgIedXC_BefE__KOV3c3Ln8O4VYCAoFIEM7bdLV1B5QmTow07xFeZTYK-P9-cscL-qYbzbHOl2YYg0kJaM10tar6YIQ4IhDfrvOW1TRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
متقی‌نیا تشریح کرد:
تأمین مالی ۱۳۳ همتی در چهار ماهه نخست سال؛ رویکرد هدفمند بانک کشاورزی برای تضمین امنیت غذایی
🔻
مدیرعامل بانک کشاورزی با تشریح عملکرد این بانک در چهار ماهه نخست سال جاری، از اختصاص بیش از ۱۳۳ هزار میلیارد تومان حمایت مالی به زنجیره‌های تولید و صنایع غذایی خبر داد و این اقدام را گامی راهبردی برای پایداری امنیت غذایی و تقویت تولید ملی دانست.
🔻
وهب متقی‌نیا تأکید کرد: این حجم از منابع با رویکردی هدفمند و از طریق تلفیق تسهیلات نقدی با ابزارهای نوین تعهدی، جهت تأمین سرمایه در گردش و تکمیل طرح‌های فعال به تولیدکنندگان و بهره‌برداران اختصاص یافته است.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/676405" target="_blank">📅 18:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676402">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jv8KdtEaDXIRwVnhKb8m9pW84ZqM6HVMtvT-p6JrwChxY3WjcckOx-jGen3rAwKI5DvKETRQo7HSyWzbnQ5C7a11oKB8iR1UBaio-w0JyBORtY5jZbdmHMitEFRVSFBng2UOV4aC0Sg7H5sdATOQ6FyZ0vA4rdoXwlU0PLNFzo41kj4zpvvZ0rYNB-nufSkCXRNuH1oi51wlI6sCEMUOOw7_WaZGC__JU7N4ZAVzRw6R-wbIFIX6TRRfk5BM9N9UCLmemSCJzUfRLmHyZqc-UFXMBINI8-MJn7vJa2PKNSkV6ugknDA5LkPjpjQoRdw2LSrdzHSchFQz3YRuSs1d3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ضرب‌الاجل مقاومت عراق به دولت و تهدید به پاسخ نظامی علیه آمریکا و عربستان
🔹
مقاومت اسلامی عراق با محکوم‌کردن حمله آمریکا به حشدالشعبی در کربلا، به دولت عراق تا ۲۳ صفر مهلت داد تا توانایی خود را در دفاع از کشور نشان دهد.
🔹
برای حفظ امنیت زائران اربعین، پاسخ به آمریکا را به پس از مراسم موکول کرده اما تأکید می‌کند که این پاسخ قطعی خواهد بود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/676402" target="_blank">📅 18:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676400">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3_xL6PGqP-GfildBOpBNnuZowYEnbWJKL4vBEITaTJqxTIURApZksz9OB93eM39039P_d907IL_t-45Jck4d69Sq1DZ4mKjVNeyliVEailcgoMwS-iCaRglEIK8u53CTLY38caE3KvpnMwk_mkJhfot7_lgaDZQnfOqv2CP_Vg6xO3ReW9PajYu7PURQUSNhy14FSm77WrzWYCFndbgUTsrMgCshoB95mVBwxR3yvqEFLRFc9z78CXgh-hhbcx2QM-yZCYtUZqLQzQG28BJQ90PNKR7TflLSGPKrpUFe-Oi1CXXFD-PG8_JzjyHQdRtTPq3x9AY54TV31hWzIkeRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
مهمان حسینیم؛ میزبان مسیر...
▫️
خاطره آن ۱۵ دقیقه‌ای که برای زائران قدم برداشتید، برای ما بنویسید.
▫️
منتظر شنیدن روایت‌های شما از دل مسیر هستیم
👇🏻
@Ertebat_gharar</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/676400" target="_blank">📅 18:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676398">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQkbBHx7Ay_EkIiBlwxrnuZnZSLUJtCgI8eJfZzgtlBhKSVxw5KbysCzno2q9E_pvPF1kjsu1pve2Io603E8igPlajcUWd2sD_w879vf6yDXowZjRSqj0sbF_AM5yvN-xK62hK1pWBh5s1WVE3VyQmXWns_EC2UA41qbNkD6gg7Mj2vFURlJJclJ98GSIY8DOcqAVSzs_4jWzkCuYXJiSz4es-CqmydDfFa6peJEGosKhUp4C9n02SLAFxm9UfaDwJNk7uV3-25pSAa7Bn--WPxno72JsDoWiMmvVtLkuI-okjNBWKNOwEYO46_mblPhLVXLVuaAINj-sEEey31zlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت ۴ ایرانی در حمله مشترک عربستان سعودی و آمریکا به کربلای معلی
🔹
پاسدار شهید علی اصغر آستانه
🔹
پاسدار شهید ابوالفضل متقی
🔹
پاسدار شهید مرتضی اکبری
🔹
پاسدار شهید امیر عباس درهم فروش
🔹
هر چهار شهید اهل کاشان بودند. / صابرین نیوز
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/676398" target="_blank">📅 18:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676396">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
پشت پرده تخریب پلیس امنیت اقتصادی توسط فیک‌نیوزها
🔹
در روزهای اخیر برخی رسانه‌ها و صفحات فیک که به دروغ پردازی معروف هستند، اقدام به انتشار مطالب کذب علیه برخی چهره‌های خدمت‌رسان در پلیس امنیت اقتصادی کرده‌اند.
🔹
اما اصل ماجرا این است که از چندماه قبل پلیس امنیت اقتصادی اقدام به برخورد و مواجهه با رسانه‌های فیک و باجگیر کرده‌اند و پرونده این افراد نیز در قوه قضائیه به صورت جدی در حال بررسی است.
🔹
همین مبارزه با فساد توسط عوامل پلیس امنیت اقتصادی موجب شده عوامل این رسانه‌ها که خطر بازداشت خود را لمس کرده‌اند، دست به تخریب برداشته و با دروغ اینگونه القا کنند که پلیس امنیت اقتصادی از آنها باجگیری کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/676396" target="_blank">📅 18:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676395">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Paz-yZqVXVSJpukYH7pOUgcEWXQcsAnPlLjDGMxwNFkNEhfnLXcAORrsQ0FMq_BmXTr7CjKNaPAJB_bMcOOEClgUgcYKLIvrkOfOccMkNuzQrHbvzT4nbMEwZEwo6axQXt3PyqITiR_G1_7UZvq4veZxDt2bNmQEMZ8KD4VW8wcZADxN-caUrgdqiEmeJqPrJ6qJ_DUNGHDwTYeCOKN1x9p4rmdpZ8H5Bqb45QDGs__SsjwUqYgB6cLmNyBg59gjM3QvkVlAjTrXZ5C7P60xlgdOo-eydG5_e8NGRWKjjvo-dliSfxFTj60APWiIt4VzVyzTotjLdeY40YpEAS5pQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شیخ صفی‌الدین اردبیلی؛ نقطه اتصال عرفان و سیاست
🔹
شیخ صفی‌الدین اردبیلی عارفی بود که بی‌آنکه شمشیری به دست بگیرد، بنیان یکی از قدرتمندترین سلسله‌های ایران را گذاشت. کمتر کسی می‌داند دولت صفوی که ایران را دوباره یکپارچه کرد، ریشه در خانقاه آرام و مکتب معنوی…</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/676395" target="_blank">📅 18:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676394">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b7e19da75.mp4?token=nawyS4qno0iJaIRE8CAe8hnY4XXq_WRwnMNls0knWJkDllORolM6ULVeRaybzDhIGnF6ZcZPwLTpL43ZvLXY4h2vLhU7NllErOzv8hDhRNdXLtr-2MZOHUsK1cwlHjHMUr6Di79FrMHbKv64-UGj6KPpMupE6cZdhJ_Bkm0MsFD2pskS6CiqIHPfEq2VYTzQm6Dw9HPYDO8EsceoRMQQJ-1LvbJjIFE2jUyIukmKwk-Z1CuaGsjiTfcatAtuxc7mWVD54-Xcqk9BOWqph4Ap2JWlIoJ6UlGNDzMJ0ZvYqoBG5KQFCMLevOPQdRcIGwWqk8msGdNpm1luaW4P0LR-7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b7e19da75.mp4?token=nawyS4qno0iJaIRE8CAe8hnY4XXq_WRwnMNls0knWJkDllORolM6ULVeRaybzDhIGnF6ZcZPwLTpL43ZvLXY4h2vLhU7NllErOzv8hDhRNdXLtr-2MZOHUsK1cwlHjHMUr6Di79FrMHbKv64-UGj6KPpMupE6cZdhJ_Bkm0MsFD2pskS6CiqIHPfEq2VYTzQm6Dw9HPYDO8EsceoRMQQJ-1LvbJjIFE2jUyIukmKwk-Z1CuaGsjiTfcatAtuxc7mWVD54-Xcqk9BOWqph4Ap2JWlIoJ6UlGNDzMJ0ZvYqoBG5KQFCMLevOPQdRcIGwWqk8msGdNpm1luaW4P0LR-7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهمانان شفاف ساحل قشم
🔹
ساحل دوطرفه قشم این روزها پر از عروس‌های دریایی شده؛ موجودات زیبایی که با جریان آب و باد به ساحل می‌رسند. تماشایشان لذت‌بخش است، اما لمسشان می‌تواند هم به شما آسیب بزند و هم به خودشان.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/676394" target="_blank">📅 18:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676391">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc1bd6606.mp4?token=U_Pv832wrvU5xd_I6eQAzv94xA7naJwD3N_1DGU22fzrjqbmsIY-e6p_IwyTLbSnFxngXsAvtH6CINVVk4BVmOQDe5IfFSM3rIYoZbCbGjedE1f5G-0RYCzp3wT68sxatw84HGO4oS76hTLbI8Q2yk1ib0lx7PuiqfXzcMTT5ASTOiZpxiFj6d_EzzUKf7qgYc2SGRVIpXkN_ca_3BxSNcuFm7tq23LddNBLoaS615NaOCKTJh-gxN85tUz3FTyXTqslkGGe4qJtYLkO7JJBUc5S0x1878CeCQ7vj-nyCm2InTq1Cw8HzpdsCaifhgL0U5O7zIcYxC8N8wUd4yd_sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc1bd6606.mp4?token=U_Pv832wrvU5xd_I6eQAzv94xA7naJwD3N_1DGU22fzrjqbmsIY-e6p_IwyTLbSnFxngXsAvtH6CINVVk4BVmOQDe5IfFSM3rIYoZbCbGjedE1f5G-0RYCzp3wT68sxatw84HGO4oS76hTLbI8Q2yk1ib0lx7PuiqfXzcMTT5ASTOiZpxiFj6d_EzzUKf7qgYc2SGRVIpXkN_ca_3BxSNcuFm7tq23LddNBLoaS615NaOCKTJh-gxN85tUz3FTyXTqslkGGe4qJtYLkO7JJBUc5S0x1878CeCQ7vj-nyCm2InTq1Cw8HzpdsCaifhgL0U5O7zIcYxC8N8wUd4yd_sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی چین از موشک بالستیک هایپرسونیک YJ-20
🔹
ارتش چین برای نخستین‌بار تصاویر شلیک موشک بالستیک هایپرسونیک ضدکشتی YJ-20 را از روی ناوشکن مجهز به موشک‌های هدایت‌شونده تیپ 052D منتشر کرد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان چینی دنبال کنید
👇
@AkhbareFori_CN</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/676391" target="_blank">📅 17:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676389">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45e147683f.mp4?token=SPC25EncP-CkAs_eaElN9XFyugQOzT8qFLb6Sc3fYAtE9Zo05FgLeVp8gCNZnKTd1r4fJtp5ktWmnY2f2b5o95HeXVUBWPJHMCkss-soBiIXmtZoJZqBfJgYEfnCzQaCl2KvzQK8QTfyReiZIK7fGfvu4-gulWZl-Xoin9Cqpl90WChPRtrt8aFK7REuIcO0d-17iuePmctrqRlYrn7-F__ikrHmCTGTnMz_9Pfxbb8RZh4uapINOB0gBgtwWSMbPc4q4xMBJwRvUCdKHtv1H6iCWkw0Lz9JwQqrsqYtZmqR8SOGI3KI8kcaPeLksqKUuDDevFmBUnefc5hmD0MUMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45e147683f.mp4?token=SPC25EncP-CkAs_eaElN9XFyugQOzT8qFLb6Sc3fYAtE9Zo05FgLeVp8gCNZnKTd1r4fJtp5ktWmnY2f2b5o95HeXVUBWPJHMCkss-soBiIXmtZoJZqBfJgYEfnCzQaCl2KvzQK8QTfyReiZIK7fGfvu4-gulWZl-Xoin9Cqpl90WChPRtrt8aFK7REuIcO0d-17iuePmctrqRlYrn7-F__ikrHmCTGTnMz_9Pfxbb8RZh4uapINOB0gBgtwWSMbPc4q4xMBJwRvUCdKHtv1H6iCWkw0Lz9JwQqrsqYtZmqR8SOGI3KI8kcaPeLksqKUuDDevFmBUnefc5hmD0MUMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آرزوی شهید تنگسیری برای حضور نوه‌اش در برنامه محفل ستاره‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/676389" target="_blank">📅 17:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676388">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69947047f1.mp4?token=d4790vh8AL5wgDhbOBIM6LGO62WKljUUUR_1LCyVITW40neD3rJKGhY_hfh7ZFCkUTp_8w4QuB6BQT5qNeRcdB-b4b3pQriPxIzBgsWDIWiBE7pZYh7kjsDCIuRJ24MTrdcZY27cnc9qB7Qo9NFtTZbr4-yGuHke0lM-ybCgg66uyOQb1ay6zGV0cuNyQDn9C3G644uZXKupJL-mZc8VEbEgVkSaE7WcZorNXvYLMMkqkayA49cH3hrCD7Grja9lIe-JbucPycaCQHfPWXFZ6KjUWN-56Ry-grRKVBXeTa2U-0Uy09NtiwOHUwzRMo2csc3YKjWyrrZvPfvaA7WlIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69947047f1.mp4?token=d4790vh8AL5wgDhbOBIM6LGO62WKljUUUR_1LCyVITW40neD3rJKGhY_hfh7ZFCkUTp_8w4QuB6BQT5qNeRcdB-b4b3pQriPxIzBgsWDIWiBE7pZYh7kjsDCIuRJ24MTrdcZY27cnc9qB7Qo9NFtTZbr4-yGuHke0lM-ybCgg66uyOQb1ay6zGV0cuNyQDn9C3G644uZXKupJL-mZc8VEbEgVkSaE7WcZorNXvYLMMkqkayA49cH3hrCD7Grja9lIe-JbucPycaCQHfPWXFZ6KjUWN-56Ry-grRKVBXeTa2U-0Uy09NtiwOHUwzRMo2csc3YKjWyrrZvPfvaA7WlIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مراسم بزرگداشت اکبر عبدی با حضور خیل عظیم هوادارن و هنرمندان و سایر اقشار در حال برگزاری است
/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/676388" target="_blank">📅 17:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676387">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31ca1a5ce.mp4?token=dSsPagXcAJmZuU8sM6wt3ohH9TleLkbTB4M6busnM2x2clwt9hHQbY5uIBNYTHmT9JDkVkbv-xi42IKxAZV_xBd3mCchqnXUKHbg0j2csRUGKSeX_dGbLnhV4uTEw9eOk7tCqX_wY0vMtvpHyKQw-ZLI99eK1B_IjWzR6yyFMZjzLszomUuhcaa-98NnzZYghqZONOjt03ebMZaYbu-MAHFJqXfZ9aV6WLSRLSS9db7eJZIa9_OB-NJyRz32mjLchLoEme_sTJyYX9gf0kIiiBv_O4unco3SbHRcU6BBIsHnlg0gbqTsI7qJyXHHd0zklYcj6ZOkwGnZOR_EJv2-MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31ca1a5ce.mp4?token=dSsPagXcAJmZuU8sM6wt3ohH9TleLkbTB4M6busnM2x2clwt9hHQbY5uIBNYTHmT9JDkVkbv-xi42IKxAZV_xBd3mCchqnXUKHbg0j2csRUGKSeX_dGbLnhV4uTEw9eOk7tCqX_wY0vMtvpHyKQw-ZLI99eK1B_IjWzR6yyFMZjzLszomUuhcaa-98NnzZYghqZONOjt03ebMZaYbu-MAHFJqXfZ9aV6WLSRLSS9db7eJZIa9_OB-NJyRz32mjLchLoEme_sTJyYX9gf0kIiiBv_O4unco3SbHRcU6BBIsHnlg0gbqTsI7qJyXHHd0zklYcj6ZOkwGnZOR_EJv2-MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عبور برق‌آسای تسلا از میان آب، همه را شگفت‌‌زده کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/676387" target="_blank">📅 17:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676385">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYsz76kV1pFWpENqgIZfNTw8NHXBt2X18SmpzTQxVjd5vXq-1IAOinonsGxCL4hiyEIBPkxfHR9QeEmOrphUYhULVE0-6ygJecNXtIx7doeM5sh55NAwW4IETlm5LYfNOuV4gS86xeqlH0MSXk6OnHsaNdy3bk1KWWTZ7ofjNAkfA19hdDgDLILc59RnzJjxdNzTuvbDBep5G3YfbDJZVUMYgIlYzwUd46fEuE2nBrKtoDyR0gPYPF1y3V8wd5lLXpF6cRCG-131XgSCQ7cYJWys-7JFJSWzBjSiyfdZhQzah7In_LUWMNPK25qtS47VXhrpeChLR31UILIRGSbrnQ.jpg" alt="photo" loading="lazy"/></div>
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
👾
داستان‌هایی از سرتاسر جهان
|
#روایت_جهان
| ساعت ۱۹
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
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/676385" target="_blank">📅 17:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676384">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVpxyssYoTzCc4OsU-aeUvTyKZJsAxSueyNf-fcmTMkl47Cvpjg9h78nXYrDaBwsrUw-yPJnxKa9rkcngr_FwOiY4LUcdSQr2a229GM3X2sHX5_oXQQwVj6jfkrsR4YOwG2Bm3BMUV-ZExjZnPfojxTRLFMn4e45bzo_zr0D8eQyZGEScELY8xKNFivTkW-kotmjxHRuDxfF_pPXRGEn4j_Ob-by2_1rltXniK6QxyrBAxyEgYECRjKKwIJhNyx1355U1OLeKYReGIwyRBPW6O17t_G2rLZ2hvII-OQ3MISZ7UVY8-UeIm77FhLfAp3elocgBmUeRAykP0lyxwrX4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن بیگلربیگی، کارشناس حوزه اقتصاد انرژی : بنزین مدیریت لازم دارد نه گرانی؛ کاهش مصرف و بهبود رفاه معیار سیاست بنزینی دولت باشد
🔹
موفقیت سیاست بنزینی با میزان افزایش درآمد دولت سنجیده می‌شود در حالی که معیار واقعی باید کاهش مصرف و بهبود رفاه عمومی باشد، اگر قیمت بنزین افزایش یابد اما مصرف کاهش معناداری نداشته باشد، حمل‌ونقل عمومی توسعه پیدا نکند، خودروهای پرمصرف همچنان تولید شوند و فشار بیشتری بر مردم وارد شود، نمی‌توان از اصلاح موفق سخن گفت.
ادامه متن:
https://eghtesademoaser.ir/fa/news/56135/
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/676384" target="_blank">📅 17:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676383">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zg3TZwbf9C465Wm1yOhpWFu1eJ2kWuwn1wwy-FHPKz8PF0q0ldZF_s4J52PuyY-CSbJ2AZete0mhFArQbG9gXls10mRSthMCJTmLJV4F-aGcpuicz0y3d1P5wx6g315a3LsNK6Tgiwgd1s_Zn3JNxXIMKTyBfjApZV9MjktjGxf0wDy88bRbwbCzHe1dE2dqyA1eVTlTEyNutAqVtyb0Kn-2OQ_Ni9QGYabvrcTMyLG_Wv6N78HORGHLVrsWPjArGqeS28dRIcaJjsEKH4aj4-UkE0gFj2cVWsFIgp8QTC8O8KvgvxZACmyT3H6EbsATTMUnnstQ5F4GUdiV0Tazwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پل ورسک؛ شاهکار مهندسی در قلب کوه‌های مازندران
#ایران_زیبا
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/676383" target="_blank">📅 17:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676382">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
از سوی رئیس صندوق نوآوری و شکوفایی ریاست جمهوری عنوان شد: موسسه ملل با گام‌های جدید فناورانه، وارد فصل تازه‌ای شده است؛ بانکداری آینده بدون فناوری معنا ندارد
رئیس صندوق نوآوری و شکوفایی ریاست جمهوری با تقدیر از رویکرد نوآورانه مؤسسه اعتباری ملل در توسعه فناوری‌های مالی گفت:
🔹
راه‌اندازی مرکز نوآوری و سرمایه‌گذاری فناوری‌های مالی ملل، اقدامی ارزشمند در مسیر توسعه زیست‌بوم فناوری‌های مالی کشور است.
🔹
به گزارش روابط عمومی مؤسسه اعتباری ملل، همزمان با افتتاح مرکز نوآوری و سرمایه‌گذاری فناوری‌های مالی ملل و رونمایی از چهار محصول راهبردی شرکت تجارت الکترونیک فناوری اطلاعات ملل (فام)، دکتر اصغر نورالله‌زاده، رئیس صندوق نوآوری و شکوفایی ریاست جمهوری، از اقدامات نوآورانه این مؤسسه در مسیر توسعه بانکداری هوشمند و فناوری‌های مالی تقدیر کرد.
🔹
دکتر نورالله‌زاده در این مراسم اظهار داشت: بسیار خوشحالیم که مؤسسه اعتباری ملل به عنوان نخستین مجموعه مالی کشور، مرکز نوآوری و سرمایه‌گذاری فناوری‌های مالی را ایجاد کرده است تا برنامه‌های هدفمند خود را در حوزه فناوری و کسب‌وکارهای نوین دنبال کند.
🔹
وی افزود: راه‌اندازی چنین مرکزی، اقدامی ارزشمند در مسیر توسعه زیست‌بوم فناوری‌های مالی کشور است و صندوق نوآوری و شکوفایی آمادگی دارد در کنار مؤسسه اعتباری ملل، حمایت‌های مالی و تخصصی لازم را از کسب‌وکارهای نوآور و دانش‌بنیان به عمل آورد.
🔹
رئیس صندوق نوآوری و شکوفایی ریاست جمهوری با اشاره به ظرفیت‌های ایجادشده در این مرکز تصریح کرد: بدون شک مجموعه‌های دیگری نیز به این زنجیره اضافه خواهند شد و مؤسسه اعتباری ملل می‌تواند همانند یک قطار قدرتمند، واگن‌های متعددی از شرکت‌های فناور، استارتاپ‌ها و کسب‌وکارهای نوآور را همراه خود کرده و مسیر توسعه و پیشرفت را با قدرت ادامه دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/676382" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676381">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4rbMyIojA9yMcwK1l7wS5ZTZAAxrfidIW74Xt258QzP4ADoUQpRemqCw7H8ts2A6tXwyiAZAMGh1oq3l2I9NmLT2hhdGDv_nhdWv-EPryMedXQoYnGizGg-X7oNK_2k31VEPCtN_mZl4QIP8px3osgsy8fMuYUM1pvnp9ix4ri_tybOvTMxnJpWU3eC_OeI5mHebx9HTzCOYOWsPoDd6lqxo01MIO-Wq0lW6dbz-ZGE9styWFBlTu-jY9P5MnrnsGUkjhz8wln-r2A4YiNmypWFdPi6M6VVtOGNj7okflJXbYcnuiO6GKYcM-6QxauZz_D-qrwUDYBtHHSZCGn0Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با این ۱۰ نوع گیاه و ادویه، سیستم ایمنی خود را تقویت کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/676381" target="_blank">📅 16:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676380">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
شهادت ۴ ایرانی در حمله مشترک عربستان سعودی و آمریکا به کربلای معلی
🔹
پاسدار شهید علی اصغر آستانه
🔹
پاسدار شهید ابوالفضل متقی
🔹
پاسدار شهید مرتضی اکبری
🔹
پاسدار شهید امیر عباس درهم فروش
🔹
هر چهار شهید اهل کاشان بودند. / صابرین نیوز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/676380" target="_blank">📅 16:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676379">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38ba69f36.mp4?token=fZbRvbyoNYMEiCowAzulXaYerhxsK3_39n3_4TlXOie5XdS6hWlP5XmV7niP35YK7PtHcXL3gJO0x0N9-Eb4nZeUFIK3xXot5YjwjW-2cbWCTbM36KLSzJhNLpA9L3-JhPp8vfzJl1DPSdl6dCqAcVuBNrCRmPLah_O09xoQ-3-0FxvLJNwIeTdHav5BrZYUirV9yDK5rqV192Tt34W1lWNXt8i94zPAXGzW7DMjtvlx1I6moJdMlKMGfAdbDCNL1JZlJMWVgU6K3gu5fnGqm1fhm_NO0aqP8y-zE06aHtku9yWbl6-et8PC4kypCyY6D27aEoVNRLceYDn_KZ4B34eW4P1Nbr0Qw5nCevi55fnr-1eWcsfwLADc_vZD2ABDSamobA5zRfMROLEUjU_W0sY4b1cdZrPUgrMBAtBopP8TGujuGpZb7tRplRvddlyf-nSBJeGa6UDz2UcbRTYUsaO6EwpqNuGXAHW0wm4OQo8j4G0Cwu6fOiOFCR_SBgGgN0LWQ7do_NB9HGzyikRtopgZVvTnnsJ4BL_PPj0J17YYd9jG8MEgyOEaN0Jr6jiiU_0-wXjToEtWAX6I4buKEoLRLDY9RdhAwMAbKLb0PSCddrV5Rgwl1BEd9d7C2yhxEVT77Ga29NHSTmvRWA6eUMIIo4-GPlk7fPZr2At6VRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38ba69f36.mp4?token=fZbRvbyoNYMEiCowAzulXaYerhxsK3_39n3_4TlXOie5XdS6hWlP5XmV7niP35YK7PtHcXL3gJO0x0N9-Eb4nZeUFIK3xXot5YjwjW-2cbWCTbM36KLSzJhNLpA9L3-JhPp8vfzJl1DPSdl6dCqAcVuBNrCRmPLah_O09xoQ-3-0FxvLJNwIeTdHav5BrZYUirV9yDK5rqV192Tt34W1lWNXt8i94zPAXGzW7DMjtvlx1I6moJdMlKMGfAdbDCNL1JZlJMWVgU6K3gu5fnGqm1fhm_NO0aqP8y-zE06aHtku9yWbl6-et8PC4kypCyY6D27aEoVNRLceYDn_KZ4B34eW4P1Nbr0Qw5nCevi55fnr-1eWcsfwLADc_vZD2ABDSamobA5zRfMROLEUjU_W0sY4b1cdZrPUgrMBAtBopP8TGujuGpZb7tRplRvddlyf-nSBJeGa6UDz2UcbRTYUsaO6EwpqNuGXAHW0wm4OQo8j4G0Cwu6fOiOFCR_SBgGgN0LWQ7do_NB9HGzyikRtopgZVvTnnsJ4BL_PPj0J17YYd9jG8MEgyOEaN0Jr6jiiU_0-wXjToEtWAX6I4buKEoLRLDY9RdhAwMAbKLb0PSCddrV5Rgwl1BEd9d7C2yhxEVT77Ga29NHSTmvRWA6eUMIIo4-GPlk7fPZr2At6VRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محیا اسناوندی، مجری صداوسیما در کربلای معلی: با وجود همه مشکلاتی که وجود داشت، مردم خیلی بهتر از سال‌های قبل در اربعین حضور یافته‌اند و این مراسم باشکوه‌تر از همه سال‌های گذشته در حال برگزاری هست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/676379" target="_blank">📅 16:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676377">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGBTydyEiqz_o83FtW52hq7xxChcqEjheCRgiAnrUd5j_LUNBEpkI6kCyf3JW1COOXkl7q3psxsMZ8zGhIHvNHhiKvggd7aFiIqi9bu1oaBJjbsL1UU6EpCpz5babSTko-m_et1V-anOW_5mBQQg-qXdyNNEOadTpJl0XCy51K3DvCq4x0DuubkdwFK5qSe6L5oFeAMQ5Ymp7nAb_LbusKv9yjK7Lj6XprqP366MhXP8BfIJRQVE9gLQXWYOvjFaiQA5NFkojOzllXvRGXmxPQhNDpZ2H7wdzbUZKosV2iraihbXmYaoU9FhEBWrMsmf-4zR51qt24N-NhBO57g8Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
امسال هم زائریم و هم خادم تا هیچ جرعه‌ای از جام عشق را از دست ندهیم
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/676377" target="_blank">📅 16:38 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
