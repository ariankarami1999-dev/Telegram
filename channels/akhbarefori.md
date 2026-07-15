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
<p>@akhbarefori • 👥 4.37M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 23:34:48</div>
<hr>

<div class="tg-post" id="msg-671574">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZ-8S_1SIF7FymyzDBUhspp3vq6tjh2US48hwZ5eCk4Vn6JF9PDeJIsgUFSuPX4LLhEbJ_i-1xfbPTybZzhQVaUWcAGXd6KZAQYmpOCgfzbXVJPT10kvggVzeASrz7EfxtL5rsJmP_4PuJE9tOctsBmr854tS-D0fAPSF0Y5ULXfMMdj7O5AetHW-5pXqj28RWdDfAFlnN2nOIsPoBB89q9tRBQX2GrCckX1to7qg0VgUBbdBIg8VDaRU0nNeTR_WowYOx9Fi0UX_rT8qFJg4Hq3mpwvWvCZrdw4P2ZyY_9q3bAQy41jHRqwTmdmL5xMwBHxoWS0uK5R37JTKz-_bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران در میان ۴۰ شهر جهان با بیشترین آلودگی نوری شبانه
🔹
توکیو، نیویورک و سئول در صدر شهرهای دارای بیشترین آلودگی نوری جهان قرار دارند و تهران با امتیاز ۷۵.۲، رتبه ۳۸ را به خود اختصاص داده است.
🔹
آلودگی نوری تهران از شهرهایی مانند ریاض، دوحه، زوریخ، ونکوور بیشتر است.
🔹
آلودگی نوری علاوه بر پنهان کردن آسمان شب، چرخه خواب انسان و زیست بسیاری از گونه‌های جانوری را نیز تحت تأثیر قرار می‌دهد.
@amarfact</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/akhbarefori/671574" target="_blank">📅 23:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671573">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
شنیده شدن صدای دو انفجار در کنارک
🔹
از کنارک گزارش داد که دقایقی پیش صدای دو انفجار در مناطقی از این شهرستان شنیده شد.
🔹
براساس این گزارش، هنوز محل انفجارها مشخص نیست و صدای پرواز جنگنده‌های آمریکایی شنیده می‌شود.
🔹
طبق اعلام مسئولان منطقه صدای انفجارها از مناطق بیرونی شهر شنیده شده و اکنون شهر در امنیت و آرامش کامل قرار دارد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/akhbarefori/671573" target="_blank">📅 23:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671572">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
موسسه اچ اف آی ریسرچ: فعالیت بندر فجیره در امارات عملا متوقف شده است
🔹
با وجود دو ناو هواپیمابر آمریکایی و پوشش هوایی سنگین آمریکا ، بندر فجیره در امارات عملا عملیات خود را متوقف کرده است.
🔹
با توقف فعالیت این بندر، حدود ۶ میلیون بشکه در روز از بازار حذف شده است.
🔹
این بندر اکنون «تقریباً مرده» است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/671572" target="_blank">📅 23:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671571">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hda3pRGPjBlwb8zekvS73PVOTqYURAPjaW-hXNN4TCRO3Z2EP1BDV21TSvixaKUmhM5bzoQ6qfQy4Colh7Ujj423yjH0btyl6iF-kGNQiRagra6QaG8RlZ4Z584VC3d6Uy2NCwF1ZVeqhsX0tjoybnYE_5NPMTkg2NOhFgrilRO56EVoTvgtCzGkgesJ3tbGHvH11c_B7QT9ie0HcSy3ho9QvONdPs1yGR3eHT8ogxYC8tfkPMgShXxxfyKJhXNHjtAQxOFzlgHKHSm9D1Ke4qEKL31TGEharjfSfOcD1zHmJXOeVmDU-iN_5EqkcZpkzIB9nhSLxhUaAYWvudnKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهاجرانی: داغ بمپور، داغ همه ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/671571" target="_blank">📅 23:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671570">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4wVCMwvRNPrC-Lo9lMEgw4ciAsvwiIJ1IAqxT4OtW_hx5LYKaJQlyKLMhKSThHX2uvtVWYK2d1UBA2zCvE9-iY2_FUKnbW4fMl-Kphvc0hnYV8kLhsxI1I_Qi_gw7ak5kaSatZ21uwejTdVV3ypK6Y9DGVLqlJvImnv55u0-B16mskiLMvX3nVrI53kdnlU-8dyTUE0EqJOMdQPa-g8m4JYy48H1rpmlOjH95rELE3jNKgki-tAmAHxVoqZY6bNja-vJ4EhO9P0wYkH-zSNWvitvpxIRQ1tpROFG5n5fck7AtDvop66KH13l3waqVWFARycj03B_N_5IpwHOjInnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصول مومن بودن از منظر امام علی (ع)
🔹
امام علی (ع) در پاسخی حکیمانه، ایمان را نه فقط باوری قلبی، بلکه ساختاری شانزده‌گانه بر پایه‌ی چهار ستون اصلی (صبر، یقین، عدل و جهاد) و زیرشاخه‌های عملی آن‌ها تعریف می‌کند. این رویکردِ جامع، ایمان را از مرز اعتقاد فراتر…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/671570" target="_blank">📅 23:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671569">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
آژیرهای هشدار در بحرین به صدا درآمد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/671569" target="_blank">📅 23:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671568">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار دیگری در اهواز خبر داد
🔹
منشا صدای اخیر هنوز مشخص نیست.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/671568" target="_blank">📅 23:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671567">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYhUEtCLDMMcUK3DlScF1PPouqMAbLCIcpF0bKPheEt-H-ysLFvqwJQ4DYv5jfOqqC0WxwujNjMCrgi8WfNde1_pg-dxbRxoPGBr6loI0zGIdiciWbPCV3ls4YuySiQT1qohorkbr2MjEWoQpJ6RXwdAknDtlB3kZeLheWmLmd4s6GGgnEoliXpKGnVdxNA3TAQoEsObtVW9gXqGMXcosd6pVYuoGwSqdBJVMo6FvxIrqYPErl4vxdxrOEqkDYQefZ4um2_PUXi0XsRCcHZIZZ2DUSjpTkrHWFaI6lo0We5anv2dZVc2-ZEkcE4jpG43ewk10nrTGdGSv5o8piGhVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در ترکیه چه گذشت؟/ جلسه محرمانه‌ای که باعث شد ترامپ به فکر "جنگ بزرگ" با ایران بیفتد
🔹
به نظر می‌رسد یک جلسه محرمانه و مرموز باعث شد ایران و آمریکا وارد جنگ با هم شوند و درگیری ها دوباره اوج بگیرد و تفاهم نیز به سرعت از بین برود. این جلسه مرموز مربوط می شود به جلسه مخفی ترامپ با سران ناتو در ترکیه.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3230677</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/671567" target="_blank">📅 23:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671566">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
انفجارها به بحرین رسید
🔹
منایع عربی از شنیده‌شدن صدای انفجار از حوالی پایگاه آمریکایی شیخ  عیسی در بحرین خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/671566" target="_blank">📅 23:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671565">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
انفجارها به بحرین رسید
🔹
منایع عربی از شنیده‌شدن صدای انفجار از حوالی پایگاه آمریکایی شیخ  عیسی در بحرین خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/671565" target="_blank">📅 23:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671564">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
صدای انفجار در راسک شنیده شد
🔹
دقایقی قبل صدای انفجار در شهرستان راسک استان سیستان و بلوچستان شنیده شد./مهر
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/671564" target="_blank">📅 23:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671563">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af223d3da.mp4?token=BTYgWg8or-7NHyUI7PYV8ClIlBNbCX-yDyYt5w1qiU9ZxboQ2eADJafNA1e1D2sFQXcQ1LvmJIsWwBi3woUpNAfDd1xSao1vBD1yg-yGfaCf1Yis2Ss1spEk6zQQ-g23Dzo_SszJIslvwUsPniGED9upK-nI914RuE0DYeEcBw9S9ptISDtP8xbs_81kel3q64SvqwO-K_NxhxSFeRlqhE5PhG2iMLctM9fhFzRJq0iOGKt8K0spttSHoaGRhEPvbxs5n9FkvDkY9NcYY6HDnX-tpemkVgQJFHero2nflQ_SbdJx01earqj5LotMc_gBETSukbcJ_Y9nlLtTITMkYUQbod7j_DtOe7e-diuRe5TBMtO2LY1ibMGFmjifwVvvjFgfiOER3NCCUin2_V9nglba5Hq7vaKyUJMXz3ahSflScj_nl8pULHl8D_swCrpE29KYspe_8mR-HgKS8rovL_WUI3vdGacJE7Ax8ik96RvvYQO0P3oXQSPJmqmF2-TTMhLLaB4wtcsSyv9OZDvgIrKjJdXj4b-dMJjRE23bYsJ5puqWfph9g4ATSdo_fW2Dlcq-Hzev-09ePzicSWK4krbBNilP1n-kgjtJfykVJ1fbOiuauwAYFNHrpLA1GeG309rxN3QdaaBNChgd42WJw91Aar1n94fuFIbPH93xXVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af223d3da.mp4?token=BTYgWg8or-7NHyUI7PYV8ClIlBNbCX-yDyYt5w1qiU9ZxboQ2eADJafNA1e1D2sFQXcQ1LvmJIsWwBi3woUpNAfDd1xSao1vBD1yg-yGfaCf1Yis2Ss1spEk6zQQ-g23Dzo_SszJIslvwUsPniGED9upK-nI914RuE0DYeEcBw9S9ptISDtP8xbs_81kel3q64SvqwO-K_NxhxSFeRlqhE5PhG2iMLctM9fhFzRJq0iOGKt8K0spttSHoaGRhEPvbxs5n9FkvDkY9NcYY6HDnX-tpemkVgQJFHero2nflQ_SbdJx01earqj5LotMc_gBETSukbcJ_Y9nlLtTITMkYUQbod7j_DtOe7e-diuRe5TBMtO2LY1ibMGFmjifwVvvjFgfiOER3NCCUin2_V9nglba5Hq7vaKyUJMXz3ahSflScj_nl8pULHl8D_swCrpE29KYspe_8mR-HgKS8rovL_WUI3vdGacJE7Ax8ik96RvvYQO0P3oXQSPJmqmF2-TTMhLLaB4wtcsSyv9OZDvgIrKjJdXj4b-dMJjRE23bYsJ5puqWfph9g4ATSdo_fW2Dlcq-Hzev-09ePzicSWK4krbBNilP1n-kgjtJfykVJ1fbOiuauwAYFNHrpLA1GeG309rxN3QdaaBNChgd42WJw91Aar1n94fuFIbPH93xXVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکرار و تاکید انتقام در پیام‌های رهبر معظم انقلاب
حجه‌الاسلام قمی، رئیس سازمان تبلیغات اسلامی:
🔹
رهبر انقلاب در اولین پیام، پیام شهادت دکتر لاریجانی و پیام به مناسب چهلم شهادت امام شهید، به انتقام و خونخواهی تاکید کردند/ این یعنی انتقام حتمی و قطعی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/671563" target="_blank">📅 23:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671562">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
پرواز جنگنده‌های آمریکایی بر فراز سواحل جنوبی سیستان‌و‌بلوچستان
🔹
هم‌اکنون صدای پرواز جنگنده‌های آمریکایی بر فراز سواحل جنوبی سیستان‌و‌بلوچستان شنیده می‌شود.
🔹
مردم منطقه صدای اصابت ۳ موشک و انفجار را مناطقی از شهر چابهار شنیدند اما هنوز محل دقیق این انفجارها مشخص نیست.
🔹
مسئولان امنیتی و انتظامی گفتند که تیم های عملیاتی به محل های انفجار اعزام شده‌اند و به زودی اطلاعات دقیق به مردم اعلام خواهد شد./تسنیم
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/671562" target="_blank">📅 23:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671561">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
مهر: شنیده شدن صدای انفجارهایی در بندرعباس  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/671561" target="_blank">📅 23:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671560">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
۴ نقطه در اطراف شهر اهواز مورد تهاجم دشمن آمریکایی قرار گرفت
معاون استاندار خوزستان:
🔹
دقایقی پیش ۴ نقطه در اطراف  شهر اهواز توسط دشمن آمریکایی مورد تهاجم قرار گرفت.
🔹
تاکنون این حملات تلفات جانی در پی نداشته است. /مهر
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/671560" target="_blank">📅 23:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671559">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
پاداش میلیاردی برای سرمربی تیم ملی
🔹
مهدی تاج، رئیس فدراسیون فوتبال، مبلغ ۱۴۰ میلیارد تومان از پاداش ۳۵۰ میلیاردی اهدایی از سوی رئیس‌جمهور را به امیر قلعه‌نویی اختصاص داد. همچنین تیم ملی ایران برای حضور در جام جهانی، حدود ۱۰ میلیون دلار نیز از فیفا دریافت خواهد کرد. در همین زمینه، یکی از روزنامه‌ها با تیتر پاداش برای هیچ به این اقدام واکنش نشان داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/671559" target="_blank">📅 23:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671558">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40564f6cd.mp4?token=FW1FvLbbg6vAb66JK2HITP_ol9H4nHhVjg9ILk66ux4lMQj8rGx8yeLTPEbBMd_aFYTvO7sWL8EP-Tw8CSexH44iBfoqIZ7XCiBehqBpLBQPc5FNla32UF5OgZnhNwAl82eC44a3isVfzRPq6dvzR4bpUIc8wiftI_QiM6RAPECVDwcNFYQqAf9FEFzf_CwC7lOT-10lvvU7VtC9PhqkH3vFYt6K9cOJ3dChk-2PyTlF7rSJvf9R4MwxFWmXAQnKiGqJE8acM3d12urjYnQV8eW7Y7dFP3voHM3199Zhmfj4G2mLmhVgUNbfV54fMZdfddYk5kyoLmU2cgV2JzrEPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40564f6cd.mp4?token=FW1FvLbbg6vAb66JK2HITP_ol9H4nHhVjg9ILk66ux4lMQj8rGx8yeLTPEbBMd_aFYTvO7sWL8EP-Tw8CSexH44iBfoqIZ7XCiBehqBpLBQPc5FNla32UF5OgZnhNwAl82eC44a3isVfzRPq6dvzR4bpUIc8wiftI_QiM6RAPECVDwcNFYQqAf9FEFzf_CwC7lOT-10lvvU7VtC9PhqkH3vFYt6K9cOJ3dChk-2PyTlF7rSJvf9R4MwxFWmXAQnKiGqJE8acM3d12urjYnQV8eW7Y7dFP3voHM3199Zhmfj4G2mLmhVgUNbfV54fMZdfddYk5kyoLmU2cgV2JzrEPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به ترور شدن توسط ایران فکر نمی‌کنم
خبرنگار
:
🔹
تهدیدهایی علیه جان شما از سوی ایران وجود داشته است... آیا از ظاهر شدن در چنین موقعیت‌هایی احساس امنیت می‌کنید؟
🔹
ترامپ:
من حتی به آن فکر هم نمی‌کنم، چون اگر فکر کنم، خیلی مؤثر نخواهم بود.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/671558" target="_blank">📅 23:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671557">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
مهر: شنیده شدن صدای انفجارهایی در بندرعباس
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/671557" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671556">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91ae1b4fe0.mp4?token=dE1cI5Tzr43-bE9tzl1sxGDG_8RjDy0gK0YtBKKIItHB8PbpJCZF87-H9tmwQI7lxq4MmDNPDIRtfXhtYFtir8w2MxxautnmImoM5b93fycPVOCTQ561e_RlB2bniMxnSL0A-hIZgdvHyAWZGKrJPre4UmZOxr5FnHqo2DOW_0OjLgncNvSJf7kwGp5gVxgjhRCJ5kEDVCmqLLFDIAXz3bUlU8dQ3WJKPejkVktf9xve1rT-z8Bez3rih_6lZrSs2tUqZST_Hb4H8q8TIiyD6xN9GE9zFF67hXNkAohL0axTOpy8uXu1zXOjmaohzeIxYBd4BAG04BfYYFsH3M7hlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91ae1b4fe0.mp4?token=dE1cI5Tzr43-bE9tzl1sxGDG_8RjDy0gK0YtBKKIItHB8PbpJCZF87-H9tmwQI7lxq4MmDNPDIRtfXhtYFtir8w2MxxautnmImoM5b93fycPVOCTQ561e_RlB2bniMxnSL0A-hIZgdvHyAWZGKrJPre4UmZOxr5FnHqo2DOW_0OjLgncNvSJf7kwGp5gVxgjhRCJ5kEDVCmqLLFDIAXz3bUlU8dQ3WJKPejkVktf9xve1rT-z8Bez3rih_6lZrSs2tUqZST_Hb4H8q8TIiyD6xN9GE9zFF67hXNkAohL0axTOpy8uXu1zXOjmaohzeIxYBd4BAG04BfYYFsH3M7hlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایرانی‌ها می‌خواهند توافق کنند
شیطان زرد:
🔹
آنها آدم‌های بدی هستند اما می‌خواهند توافق کنند
🔹
می‌توانم به شما بگویم که آنها می‌خواهند توافق کنند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/671556" target="_blank">📅 23:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671555">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de1acb88a.mp4?token=dcLUYs4-0rVSE6j8_38x2NYq_7yE04aysTK_BKW0j0hBQjcf_Hgq9bfamxkHlwSIpumo2Ds9GW6tIZeSICqONvffQQAMXAFA7qhZv8JDReD73exCcysx2oeYwaK0v-7Cu2VMIm-dUPUaOxc6drAhXR60PXGLzxwvATH0EzuQyppkqHo460nQ47fXwLWVi9Y51s2czQhKnCLTZUfHFe8L6SKcFok65hCnJg59R4iiowWDTprwTJDJkFd15w37dS_5S8r_GrZDBH3ZXz4RBHjUoCOuNqz-iF4ucC30eUDZoPf50YaL_0Wk0u9FZJ_pGhHREqzjkuLiw4FxEl5kO-UPOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de1acb88a.mp4?token=dcLUYs4-0rVSE6j8_38x2NYq_7yE04aysTK_BKW0j0hBQjcf_Hgq9bfamxkHlwSIpumo2Ds9GW6tIZeSICqONvffQQAMXAFA7qhZv8JDReD73exCcysx2oeYwaK0v-7Cu2VMIm-dUPUaOxc6drAhXR60PXGLzxwvATH0EzuQyppkqHo460nQ47fXwLWVi9Y51s2czQhKnCLTZUfHFe8L6SKcFok65hCnJg59R4iiowWDTprwTJDJkFd15w37dS_5S8r_GrZDBH3ZXz4RBHjUoCOuNqz-iF4ucC30eUDZoPf50YaL_0Wk0u9FZJ_pGhHREqzjkuLiw4FxEl5kO-UPOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک ایرانی مقیم خارج از کشور: ایرانیان مقیم خارج جنگ‌طلب نیستند، ما نمی‌خواهیم کشورمان بمب بخورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/671555" target="_blank">📅 23:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671554">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psyIWUT8GHuZ9TD7QUJpfYX3QI0dSCH2G2XvSqIB6ACRM34s5pDm8japkslBKDtmFWdmDd-LTsKN4339VN8SlebELrjQCCvrKpLAyyDHzsO7nvTg_7FDuEn2WN3unxOQfwaDkQAI6t2ifmU6dhKJ14kQe-pQwFEucYMwuaelhzQfcRWvcNOJTpxi2TeTg_bxqVJe82XuTUwU8nLIUtBioZ098qF02YCqDFYjgCLgjmiffm0ueTQcIw7vKPXWotNsSQokLARKjtNLMZnf1dFJ436kqVbKmltymmDSvMsrbuLL1iKa_Avc9fYJRsw18wgvL8PMzLwTWyg69gEqc3wJ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای بوئینگ‌های مرموزی که در مسیرهای جنگی پرواز می‌کنند
🔹
تحقیقات رویترز نشان می‌دهد شرکت‌هایی تحت کنترل یک کهنه‌سرباز نیروهای ویژه ارتش آمریکا، چند فروند هواپیمای قدیمی بوئینگ را در مسیرهایی به کار گرفته‌اند که به شبکه‌های تأمین نیروهای واکنش سریع سودان مرتبط بوده است؛ گروه شبه‌نظامی‌ای که به ارتکاب جنایات گسترده، از جمله اتهام نسل‌کشی در دارفور، متهم شده است.
در خبرفوری بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3230659</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/671554" target="_blank">📅 22:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671553">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دبیر اتحادیه املاک تهران: برخلاف گفته دولت، اجاره‌بها ۳۰ تا ۵۰ درصد افزایش پیدا کرده است
سعید لطفی، دبیر و عضو هیئت رئیسه اتحادیه املاک تهران در
#گفتگو
با خبرفوری:
🔹
اجاره‌بها تابعی از قیمت تمام شده مسکن است، با توجه به اینکه افزایش قیمت مسکن  داشتیم، قطعا اجاره‌بها هم نسبت به سال گذشته افزایش پیدا می‌کند.
🔹
برخلاف گفته دولت مبنی بر اینکه نسبت به پارسال فقط ۲۵ درصد افزایش اجاره‌بها مجاز است، به‌طور میانگین بین ۳۰ تا ۵۰ درصد افزایش قیمت در اجاره‌بها اتفاق افتاده که این موضوع با توافق میان مالک و مستأجر انجام می‌شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/671553" target="_blank">📅 22:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671552">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
صدای چندین انفجار شدید در اهواز شنیده شد/ جماران  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/671552" target="_blank">📅 22:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671551">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZkvHG0tv1xTAs138gOCgFQDM-8kdYLO9F8hk3KUUp4wmGrOoEVGnAVTQ56mKx9mM8rRTqnB3jiKQl5t-XpaxrFn6h9kHsre1xkprlef6VuCgffjaJWKE4L05tUr4MJij_xptWAhDpUzF1A1H5B_NWEokHoTW6ltVXPIDK12M3SMojAjH6iOkkVzYOzTtvzM5kZr_kIXw1fpZ_ZGRuPQWm4R_hUIxaMgYhOCEi7V8cNkUPmLQUV_j3HR955xjYO0zVZcakfM03HnefAvjDM76KbJXxRZshrS1uUikdzsNqZ8xdQMESEOtlHm2u1I2o1eLFH7967kXsQn38kNbJgqXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سنتکام دقایقی قبل از آغاز مجدد تجاوز نظامی به خاک ایران خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/671551" target="_blank">📅 22:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671550">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
منابع عربی: از دقایقی پیش صدای چند انفجار در کویت شنیده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/671550" target="_blank">📅 22:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671549">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
صدای سه انفجار در چابهار شنیده شد/مهر
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/671549" target="_blank">📅 22:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671548">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
آمریکا از شهروندانش خواست به ایران و افغانستان سفر نکنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/671548" target="_blank">📅 22:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671547">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
صدای چندین انفجار شدید در اهواز شنیده شد/ جماران
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/671547" target="_blank">📅 22:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671546">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c8e99b02.mp4?token=JlIO2-nSfSjmLJp2fMBXpTkjFlUvuuNn4tzFWtJRh9IfmSMUtga6_PaAuNGyzsba9KAEHOEQ1mNdDmhu_9UX0lFl-qVNFSjWtBsFI-KGhViArXzQHUzYz_WuPGnxlxz9FUw92pakQ0MNo6CWlXPLhf5eohcASVlC8BRaJsjIVlHEKRLb7i3dPSFhXz0fDLBOVAvt_iemCUhrO5wprxT2eJfbH3-MdjOyZKdVbASfKs5CT-11CsO1eX_FGBPEebHcrJdjDnAXQKGilyIp629N9eS30-RwXe9MT3RVVhO0SmBlrxA3Mud6bTT-VByx71UEyDyTitSk04zQkaiJ0_nb2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c8e99b02.mp4?token=JlIO2-nSfSjmLJp2fMBXpTkjFlUvuuNn4tzFWtJRh9IfmSMUtga6_PaAuNGyzsba9KAEHOEQ1mNdDmhu_9UX0lFl-qVNFSjWtBsFI-KGhViArXzQHUzYz_WuPGnxlxz9FUw92pakQ0MNo6CWlXPLhf5eohcASVlC8BRaJsjIVlHEKRLb7i3dPSFhXz0fDLBOVAvt_iemCUhrO5wprxT2eJfbH3-MdjOyZKdVbASfKs5CT-11CsO1eX_FGBPEebHcrJdjDnAXQKGilyIp629N9eS30-RwXe9MT3RVVhO0SmBlrxA3Mud6bTT-VByx71UEyDyTitSk04zQkaiJ0_nb2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیامبر از انتقام مسلمانان نمی‌گذشت
محمدحسن رجبی‌دوانی، پژوهشگر تاریخ اسلام:
🔹
اگر عباس عموی پیامبر به ابوسفیان نمی‌گفت قبل از دستیابی پیغمبر توبه کند و اسلام بیاورد، پیامبر به محض دستیابی به او به انتقام مسلمانان او را می‌کشت.
🔹
همان‌طور که بقیه را دنبال کرد و گفت اگر به پرده خانه کعبه آویزان شده بودند آن‌ها را بکشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/671546" target="_blank">📅 22:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671545">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
عراقچی به قطر سفر کرد
🔹
وزیر امور خارجه جمهوری اسلامی ایران به منظور شرکت در مراسم ادای احترام به حمد بن خلیفه آل ثانی امیر سابق قطر به دوحه سفر کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/671545" target="_blank">📅 22:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671544">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
از کسانی که مذاکره با ایران را رد می‌کنند، راهکار جایگزین می‌خواهم  ونس، معاون رئیس‌جمهور آمریکا:
🔹
نیروی نظامی یک ابزار است، اما دیپلماسی ابزار دیگری است. من از آمریکایی‌هایی که می‌گویند نمی‌توان با ایرانی‌ها مذاکره کرد، ناامید شده‌ام. پس پیشنهاد شما برای…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/671544" target="_blank">📅 22:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671542">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1833a97fe.mp4?token=PGQ0paRx_rhQcBMv-9Y9D3_QuDzVz_-V47iOR1kwvfMk6KGUHJy7WHWfApblStjwvMrlAaXK77AFpKwLWtqnAbs1Ew69qsqMquDqTi_3v-6DuvJWkraVck817soozfs1VLkMCA2oT21yXxnzHc9--qJFenblnGI162UrI6GyFWtTzt4vZzC4X4dQAuE6XQlUkqLWxIhWvIivno6xyyNeEaEk1xweikLdZ9NSbcEwZewK56nKdQp7TfFNej9SdC6Cp_vb8W5_V_e9ImaJ3rODi8xGDBzjmhT7hqLE6ANg2qYj_ccsT4xqTVMrB4R6EMBH28fziOAw3Vzpo8GxTmp7ZFXBMsWdEz8bZdEJvsg_Mn7YAHqgxFJsOwJFKT0PxEyJvkazbmznBOdyAlzehvK6ZGz9LbI_87PIMlDvvGxIBioJVgjLTwTljAXQ-DS4seRMTcW4g5WgoPMYTrYK1VxtKkdKkq8EPLUMZ82XOl5Jbcep4d3aS848eUsQ1yR42yrl_DquZQOzqmlE-rSxxuxb7-VpSZgjtbHy8_gIEkMzs5QhKAxdyVG5Nt2T5-RI0UC6b9CDo2FGVgdbon7s_WkQ-S6D-RPhLVXjUTo59ofCuJkTJEXmFMdS2z6bY8QzbdneUC1w7ymqa3P_xHE7r4uUpjeUeKJHj5g8wYQkBw5M-0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1833a97fe.mp4?token=PGQ0paRx_rhQcBMv-9Y9D3_QuDzVz_-V47iOR1kwvfMk6KGUHJy7WHWfApblStjwvMrlAaXK77AFpKwLWtqnAbs1Ew69qsqMquDqTi_3v-6DuvJWkraVck817soozfs1VLkMCA2oT21yXxnzHc9--qJFenblnGI162UrI6GyFWtTzt4vZzC4X4dQAuE6XQlUkqLWxIhWvIivno6xyyNeEaEk1xweikLdZ9NSbcEwZewK56nKdQp7TfFNej9SdC6Cp_vb8W5_V_e9ImaJ3rODi8xGDBzjmhT7hqLE6ANg2qYj_ccsT4xqTVMrB4R6EMBH28fziOAw3Vzpo8GxTmp7ZFXBMsWdEz8bZdEJvsg_Mn7YAHqgxFJsOwJFKT0PxEyJvkazbmznBOdyAlzehvK6ZGz9LbI_87PIMlDvvGxIBioJVgjLTwTljAXQ-DS4seRMTcW4g5WgoPMYTrYK1VxtKkdKkq8EPLUMZ82XOl5Jbcep4d3aS848eUsQ1yR42yrl_DquZQOzqmlE-rSxxuxb7-VpSZgjtbHy8_gIEkMzs5QhKAxdyVG5Nt2T5-RI0UC6b9CDo2FGVgdbon7s_WkQ-S6D-RPhLVXjUTo59ofCuJkTJEXmFMdS2z6bY8QzbdneUC1w7ymqa3P_xHE7r4uUpjeUeKJHj5g8wYQkBw5M-0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امنیتی‌ترین فیلم سینمای ایران رفع توقیف شد
🔹
آغاز اکران فیلم سینمایی «لباس شخصی» در سینماها
🔹
فیلم سینمایی «لباس شخصی» به کارگردانی امیرعباس ربیعی و تهیه کنندگی حبیب والی‌نژاد
🔹
#لباس_شخصی
روایتی از پیچیده‌ترین پرونده امنیتی بعد از انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/671542" target="_blank">📅 22:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671541">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ادعای ترامپ: سوریه در تعامل با حزب الله دقیق‌تر از اسرائیل عمل خواهد کرد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/671541" target="_blank">📅 22:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671540">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
تیم مذاکره‌ کننده ایرانی به اسنادی دست یافته است که نشان می‌دهد افرادی نزدیک به دونالد ترامپ، از جمله استیو ویتکاف و جرد کوشنر، با بهره‌ گیری از اخبار محرمانه حول مذاکرات و جنگ، بازارهای مالی را تحت تأثیر قرار داده و سودی بالغ بر ۹ میلیارد دلار کسب کرده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/671540" target="_blank">📅 22:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671539">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
صدای انفجارها بار دیگر در سلیمانیه عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/671539" target="_blank">📅 22:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671538">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14afdc3e6d.mp4?token=p3ljGY466YhZHOjaxjUbBeYqdw23yQUXii_zrjjsf9RBVXdjt3Lwr9UpqbOroeHPlwHHF9bzFJk80FgD8EzCtU8fpmR6_hyS_3zMKsH2POeAwIPF6YavHHgXcBGTsPYmmW44oWbsSbtAjSbAqg_3EwCNESKA1oh_7od_oBKqBV2Pnd7f4zIxaoVF9ZfCNOsN2eave-Dkc6LS8t_KJb0N2DeAIoPvCfVGTZDUw-IgTifoCKAukepOBp2MT95TcFYpynHlqkkp7XvIo5GuEPUhhV396XloZbwn6wPIi3OaexiAWp0ZiR9mLpHieumPx99D-KMdc3Jwq4kkvKvGLmyFLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14afdc3e6d.mp4?token=p3ljGY466YhZHOjaxjUbBeYqdw23yQUXii_zrjjsf9RBVXdjt3Lwr9UpqbOroeHPlwHHF9bzFJk80FgD8EzCtU8fpmR6_hyS_3zMKsH2POeAwIPF6YavHHgXcBGTsPYmmW44oWbsSbtAjSbAqg_3EwCNESKA1oh_7od_oBKqBV2Pnd7f4zIxaoVF9ZfCNOsN2eave-Dkc6LS8t_KJb0N2DeAIoPvCfVGTZDUw-IgTifoCKAukepOBp2MT95TcFYpynHlqkkp7XvIo5GuEPUhhV396XloZbwn6wPIi3OaexiAWp0ZiR9mLpHieumPx99D-KMdc3Jwq4kkvKvGLmyFLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از کسانی که مذاکره با ایران را رد می‌کنند، راهکار جایگزین می‌خواهم
ونس، معاون رئیس‌جمهور آمریکا:
🔹
نیروی نظامی یک ابزار است، اما دیپلماسی ابزار دیگری است. من از آمریکایی‌هایی که می‌گویند نمی‌توان با ایرانی‌ها مذاکره کرد، ناامید شده‌ام. پس پیشنهاد شما برای اینکه مردم را از تیراندازی به کشتی‌ها در تنگهٔ هرمز بازداریم، چیست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/671538" target="_blank">📅 22:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671537">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
مخالفت AFC با درخواست فدراسیون فوتبال ایران
،
گل گهر نماینده ایران در آسیا شد
🔹
کنفدراسیون فوتبال آسیا با ارسال نامه‌ای به فدراسیون فوتبال ایران اعلام کرد گل گهر نماینده کشورمان در لیگ قهرمانان آسیا ٢ خواهد بود و در خواست فدراسیون برای حضور چادرملو را نپذیرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/671537" target="_blank">📅 22:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671536">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90873cbacb.mp4?token=SdL6-okPRE7o6F3n7RtUGMqrEWnTRpwZTOivq2bXxwmQh5O6Quykcjf-RQmjwIufIg4fuCi5tjFwyTs7MvOesXrcXNrGnwyv3hhV0_MEpTKO8Vhq73PSRgiaUbvwCBzBRxO0diUMhcopHb9s_RSU6an6NlMyxFvHV9-qL1ITJJvrum6SPjPATV19lQQxuPeJqHsG77u9NMlDOy3BpwBR-2Mnm4ne6MxqF4iR1aM-l1kTnhEpDxr2WkzLX4JokBq-nUbKrTgbYKgx1zGnBK5yUgPui59_TUFI9vtvy_MqxXoW5t9Rgk0Gli0eBzsHtEpdaErI8xsyxrEHAQUJPuSLZZfxAM3nYHTxMYlpeW5DzVum6rlTB1JOuA9PFw6eekO-ti7ABPDJW5hC60D2KIHELl6WyxC7EoTMhGjY_mhZEWkHsA1fEmCo1gK2dycxIkkp8kmPv9Ol8NXwnifm91yZr_r_u2J1vyo9fnnxywsjKl1DsW0D56QliR8HaP-5KzNiVaa14aaFEaWpEo-pSOWBDDRC8UXTDOUeu-oBPr4J-LNKoMpAHlqBHNn6F339t6Sjrk23TtTzokhC5_TtT2jPaEIOTDA67-Ir8G3oFHCSaoFEQ_wufxEYkXkbWNHWTANzm4581RK-yTgReJRjCo7rbyw2O_h7CjZjW7mw1LlDZSY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90873cbacb.mp4?token=SdL6-okPRE7o6F3n7RtUGMqrEWnTRpwZTOivq2bXxwmQh5O6Quykcjf-RQmjwIufIg4fuCi5tjFwyTs7MvOesXrcXNrGnwyv3hhV0_MEpTKO8Vhq73PSRgiaUbvwCBzBRxO0diUMhcopHb9s_RSU6an6NlMyxFvHV9-qL1ITJJvrum6SPjPATV19lQQxuPeJqHsG77u9NMlDOy3BpwBR-2Mnm4ne6MxqF4iR1aM-l1kTnhEpDxr2WkzLX4JokBq-nUbKrTgbYKgx1zGnBK5yUgPui59_TUFI9vtvy_MqxXoW5t9Rgk0Gli0eBzsHtEpdaErI8xsyxrEHAQUJPuSLZZfxAM3nYHTxMYlpeW5DzVum6rlTB1JOuA9PFw6eekO-ti7ABPDJW5hC60D2KIHELl6WyxC7EoTMhGjY_mhZEWkHsA1fEmCo1gK2dycxIkkp8kmPv9Ol8NXwnifm91yZr_r_u2J1vyo9fnnxywsjKl1DsW0D56QliR8HaP-5KzNiVaa14aaFEaWpEo-pSOWBDDRC8UXTDOUeu-oBPr4J-LNKoMpAHlqBHNn6F339t6Sjrk23TtTzokhC5_TtT2jPaEIOTDA67-Ir8G3oFHCSaoFEQ_wufxEYkXkbWNHWTANzm4581RK-yTgReJRjCo7rbyw2O_h7CjZjW7mw1LlDZSY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر روبرتو پیاتزا درباره کت‌وشلوار پوشاک زاگرس:
«کت‌وشلوار خیلی عالی و کاملا مشابه استایل ایتالیایی است»
«زاگرس؛ تلفیق شخصی‌دوزی صنعتی و دقت در اجرا برای ارائه‌ی محصولی با استاندارد بین‌المللی»
📌
مشاهده در اینستاگرام:
https://zgrs.ir/zi
🌐
وب‌سایت:
www.zagrospoosh.com
📞
02143064000 (داخلی 330)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/671536" target="_blank">📅 22:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671535">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
احضار سفیر انگلیس در تهران به وزارت امور خارجه
🔹
در پی اقدام ناموجه دولت انگلیس در قرار دادن نام سپاه پاسداران انقلاب اسلامی در ذیل قانون مقابله با تهدیدات دولتی، هوگو شورتر، سفیر انگلیس در تهران، امروز چهارشنبه توسط علیرضا یوسفی دستیار وزیر و مدیرکل اروپای غربی وزارت امور خارجه، به وزارت امور خارجه احضار و مراتب اعتراض شدید جمهوری اسلامی ایران نسبت به این اقدام خصمانه به وی ابلاغ شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/671535" target="_blank">📅 22:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671534">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b8c2d1a0.mp4?token=A5pQFETtnT3ZFTyC0kKB0YdPx5aqce2KXpyccnfceHyrsPzwXa2p4IObEsfRcvU780n7N5o4V8WsLsbrQq_xe4onnNPrvz-cqJqaPPH2mq1FcOQ3paFOsBka2jFi6AUXDXw7pIqQn_OMy-1SbDSgyPPRYYfP-mBhL9Hj3aHd1c9GuggasjsCFMGHlYZjOjtSWhWBKR_imp01ni2vJD2iY7LlFz-S_XXXDzOCeB6fB1TVvIe-bSddAYzCUWM9TyHlyjQjalOYg9fVM5L-UhrKU0QycBkCXnGsfgb2s3ox8o0WKqm7c_HEPfHxSUj4wq3UIqbgmTb1RUd4wP0plY94qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b8c2d1a0.mp4?token=A5pQFETtnT3ZFTyC0kKB0YdPx5aqce2KXpyccnfceHyrsPzwXa2p4IObEsfRcvU780n7N5o4V8WsLsbrQq_xe4onnNPrvz-cqJqaPPH2mq1FcOQ3paFOsBka2jFi6AUXDXw7pIqQn_OMy-1SbDSgyPPRYYfP-mBhL9Hj3aHd1c9GuggasjsCFMGHlYZjOjtSWhWBKR_imp01ni2vJD2iY7LlFz-S_XXXDzOCeB6fB1TVvIe-bSddAYzCUWM9TyHlyjQjalOYg9fVM5L-UhrKU0QycBkCXnGsfgb2s3ox8o0WKqm7c_HEPfHxSUj4wq3UIqbgmTb1RUd4wP0plY94qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قوه قضاییه با قاتلان شهید عجمیان و شهید آرمان چه کرد؟
🔹
دکتر محمدحسن رجبی‌دوانی، پژوهشگر تاریخ اسلام در محفل الهیات انتقام از نرمش قوه قضاییه در مقابل مفسدان داخلی گفت؛ افرادی که باید به قصاص و مجازات می‌رسیدند تا در نهایت بتوان خونخواهی و انتقام از امام امت و شهدا را در خارج از مرزها پیگیری کرد؛ اما خیلی از آن‌ها به سزای اعمال خود نرسیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/671534" target="_blank">📅 22:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671533">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e727526ccb.mp4?token=hb-uxtZOChNVsf2Ix9UfhgxyZDPxZovc4wTHcDgmEaNuh9WEDa6kUZVBK4Jp8vqYVBKXQi0u1x8kFpMXKwTT9NvaBK-NpyAhVeASdRtvVYNv0fm0ku1VLth-yW7Jgh6T43gM_T5v2KrLvxI4XereRrfhGiG0_DK-qxP_SP724jwuRAvxwFRAL3n-jhuLnqYNLmMs6OavPYxBg23A5HNtIoM__ir-VKNXsPo8bZn90Ro_rGEnAB3E8AqzS2rTBxfVCdHmOUrO7j0fX5z3VXpJNm5GFbu1cuxDTFf0H_kVfjxS0hg-AICtOxCBr3abITcz2bk7QDvzl9cRfEU0CswRXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e727526ccb.mp4?token=hb-uxtZOChNVsf2Ix9UfhgxyZDPxZovc4wTHcDgmEaNuh9WEDa6kUZVBK4Jp8vqYVBKXQi0u1x8kFpMXKwTT9NvaBK-NpyAhVeASdRtvVYNv0fm0ku1VLth-yW7Jgh6T43gM_T5v2KrLvxI4XereRrfhGiG0_DK-qxP_SP724jwuRAvxwFRAL3n-jhuLnqYNLmMs6OavPYxBg23A5HNtIoM__ir-VKNXsPo8bZn90Ro_rGEnAB3E8AqzS2rTBxfVCdHmOUrO7j0fX5z3VXpJNm5GFbu1cuxDTFf0H_kVfjxS0hg-AICtOxCBr3abITcz2bk7QDvzl9cRfEU0CswRXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای انفجارها بار دیگر در سلیمانیه عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/671533" target="_blank">📅 22:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671532">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
سی‌بی‌اس: مقامات دفاعی ایالات متحده در حال بررسی طرح‌های اضطراری برای اقدام نظامی احتمالی علیه کوبا، از جمله یک حملهٔ هوابرد، هستند، هرچند که هنوز هیچ تصمیمی گرفته نشده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/671532" target="_blank">📅 22:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671531">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
پروژه آشوب با تصاویر قدیمی؛ ادعای تجمع در پاساژ چارسو تهران تکذیب شد
🔹
عصر امروز، چهارشنبه ۲۴ تیرماه، تصاویری با ادعای اعتراض مردم در پاساژهای چهارسو و علاءالدین تهران از سوی برخی اکانت‌های ضد انقلاب در شبکه‌های اجتماعی منتشر شد. شماری از کاربران در شبکه اجتماعی ایکس نیز با انتشار مطالب مشابه، این ویدئوها را بازنشر و تأیید کردند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/671531" target="_blank">📅 22:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671530">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcfe604fc8.mp4?token=XDtWNztVGBmnZMYLVY8uqECSYf52OzNxsPuRPsnJN0jWsRRhw7vaqw31M3HUJzLiuAS-c-gTPh_HW_arPPf-P1pBd78GpeBUDc7tb_HUuYaWLMOCHyAUyeWJxhrIaRKXA3K_UrS9I2jun_0b2B0y21h7i1g-NEHcLr2_083rtqJUGaOM3KG62LbEJje6OuRqXyqL2V5jzuf2wU9YlZdhJ6ch5M_3tumV4xaAD1oGPvwYDJVOqFXMXQK6-1UgBqNULO7dm2myzVa2LKgnHTr_9lVzVMVQGRTGwMcp3MdNuBTZxMIHvrLlBgMNRI17NyaIJfjHEJ6JX0vbMgcDTum-WLq-P1EiiEzkzJar-JtHOe1CzgJAEYP1KIuYLxLLW984k9qioPRHJoNB62Imlu5_NWKeBvULxkL4tZv9UEJ0PoDo_bqN2V67AufWF2Hf7vl2LMj1MNuckvRxxlX9g6kGy8j21KumZlwna1Zc1y0PWJAbwu-gZDScDG5EsyXzgQQ_A6wFr_6OwLuFAoc2p_bLYVGOHq7RfwCX7gCZqOx-Qz2xYb5EP8DT0j6nVkdgUn_25f47z4mSQQt5GQVQU6D3aNJ92FvXGnLIYKFoa10JPeGQDGfTpghdE9-9A6TSB2Bmqlbp42VlSdj6-f63xHGz6_qkHyuCETlAN0FH642Ggxo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcfe604fc8.mp4?token=XDtWNztVGBmnZMYLVY8uqECSYf52OzNxsPuRPsnJN0jWsRRhw7vaqw31M3HUJzLiuAS-c-gTPh_HW_arPPf-P1pBd78GpeBUDc7tb_HUuYaWLMOCHyAUyeWJxhrIaRKXA3K_UrS9I2jun_0b2B0y21h7i1g-NEHcLr2_083rtqJUGaOM3KG62LbEJje6OuRqXyqL2V5jzuf2wU9YlZdhJ6ch5M_3tumV4xaAD1oGPvwYDJVOqFXMXQK6-1UgBqNULO7dm2myzVa2LKgnHTr_9lVzVMVQGRTGwMcp3MdNuBTZxMIHvrLlBgMNRI17NyaIJfjHEJ6JX0vbMgcDTum-WLq-P1EiiEzkzJar-JtHOe1CzgJAEYP1KIuYLxLLW984k9qioPRHJoNB62Imlu5_NWKeBvULxkL4tZv9UEJ0PoDo_bqN2V67AufWF2Hf7vl2LMj1MNuckvRxxlX9g6kGy8j21KumZlwna1Zc1y0PWJAbwu-gZDScDG5EsyXzgQQ_A6wFr_6OwLuFAoc2p_bLYVGOHq7RfwCX7gCZqOx-Qz2xYb5EP8DT0j6nVkdgUn_25f47z4mSQQt5GQVQU6D3aNJ92FvXGnLIYKFoa10JPeGQDGfTpghdE9-9A6TSB2Bmqlbp42VlSdj6-f63xHGz6_qkHyuCETlAN0FH642Ggxo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت یک تغییر: اولین بار که رهبر شهید را از نزدیک دیدم، فقط مات و مبهوت نگاهش مانده بودم/ آن‌قدر آرامش و نورانیت چهره‌اش برایم عجیب بود که دیگر هیچ‌چیز اطرافم را نمی‌دیدم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/671530" target="_blank">📅 22:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671529">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
فعال شدن پدافند هوایی کنسولگری آمریکا در اربیل
🔹
شبکه المیادین از فعال شدن سامانه پدافند هوایی در کنسولگری آمریکا در اربیل خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/671529" target="_blank">📅 22:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671528">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4312fee5c5.mp4?token=qHq0QzC9MJn4KWXA9voahx_AezpRhw1YEpKmecpav4cSCm9Bs3X6qhMlGkgdhgzS2qgygZ1HHXbYb1obKDoa-6qMsaBoBEGzFCploWh7mJdrbPPPkK2hax_3JS9PZfLLcuQxZDKpRrBvb9qgi6PSb8UKddFFcyR75klXDLOk9PkSXeWtV07NUL-Q_4_8DLYQ7ufuqhvwGRLeN90-NMQbxjTHuIniv0vboL2P6uaFPW6_wnvL5sw9Lo2OxbGwtArxEeJvB-Mz2OaUY-rTioEE_VAAP2WH9LR22KkfH1iRxGkQFIXv6GzO5lqRlzlPiqxo9AoZPM00jGH7Jao9OGQoGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4312fee5c5.mp4?token=qHq0QzC9MJn4KWXA9voahx_AezpRhw1YEpKmecpav4cSCm9Bs3X6qhMlGkgdhgzS2qgygZ1HHXbYb1obKDoa-6qMsaBoBEGzFCploWh7mJdrbPPPkK2hax_3JS9PZfLLcuQxZDKpRrBvb9qgi6PSb8UKddFFcyR75klXDLOk9PkSXeWtV07NUL-Q_4_8DLYQ7ufuqhvwGRLeN90-NMQbxjTHuIniv0vboL2P6uaFPW6_wnvL5sw9Lo2OxbGwtArxEeJvB-Mz2OaUY-rTioEE_VAAP2WH9LR22KkfH1iRxGkQFIXv6GzO5lqRlzlPiqxo9AoZPM00jGH7Jao9OGQoGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عامل اصلی آتش‌زنی فرمانداری و کلانتری شهرستان دهاقان به دار مجازات آویخته شد
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/671528" target="_blank">📅 22:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671518">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JTf8_8qxH-JvCUXreaAqhlZg_76JSwAmIVr4qFEXSeMSex7bvDqiwGzAaxl0feF48xiIIgLQA-jvxnWpbxy1v5d00QT2EtmncFmCnozoDML73MclSJgPFwQTbrBeGjoMsIVMnNLMFEBkOPQ17exK2EeUmNv8mXMft7umpNxSC1Sr1-DZbc8uzoGAccmHW3Sps9V56IQcOn_PxJ_45RX3MjJhnxdovBJ6klxxT6a6sBHnmz2FMlhtVJz1q8Hu4wmwvPtSDUjb_JDBrjqyp2QFxDncLML8aMdjEH7i8PZC_E8OnLLXZcn13_gsnDRvzdulwHEjvJyKka4n92bGjkSw0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O_xrWNfcOtxwznTC_BYlIWwWNoQnccaUntU9A_5JmQfalE47qf8W6HoNtq_ysTEHsmJhVz5GK2pL-4XKzQRQqEHM_0bg7OjT-y4xYKw2xi-dtlMo3jenNdNTYXycmAh_iygSk1aFlxyyiQm0GBD9Vm63fUrjDZuVdaKFgBXa_ypxD_sbZK9yTMxS88OtHBKuMjjb_qKxljvkThA_th9gH4hQ2-6CkCaUwzvt7ehqODMANcxbRT2wB-b24ta2nT8iH4qqnii4WFTlvv0D2jA8ECnNCspmoB1FuHQvhpV475H_m8HkQvxuqsKsi3HQ9lmjXsTTM3CR0d4NdkwCu9XNFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eH0XBfV_0VRLsS1J1ChcC5eelRp77EJMPokvNWVpZTa81r0cskulhzIQyqiB-9dfSsEQj80CbKiFe_r47oGRAj9B9DfkMmuS8SAF7QTu1HBA3xoi3mm8o8uRy7FcIYARR6nWF2JCq7s2kVDU3KSnWvdjxLVRq-9YmnQhl_zV_TqWKwlhOp2-9eulrsAAIWjHcunRAgBUCQls6LGIiIVXA3QBz2U_uBABvKik2E7MJTavwJO777DvW3ZLFw4iH3bXGr8QhLJhN48wyUSyUvbFVr2gVews8ZE8BirmTdnMA3-PASry5nI052VvYz9psLnc5wmKA6UvMbfMmeoK7gQxEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AqA_yfx4t9SKgS0KLQriB5bD8jTnpBkL5XNoRq78UUJj3d8AY2FAzc5z9dtiAtYmwwWAfcG05mu-mn9u_vkGp5Uh8JV6koUpBaiznmXcmuc6KHbLcQWE2QIoL_6vvKAfKeyxbCEjl0B50zjuXKIxuvhGX1HilLDAwzSh0LNJa7v-wobvY3_tHJIbFUS9KMYDGlBAA99kX41iRu4PyFLzxrmqYYMLTYb8-HYfnIs1ShhCeH730IBUg1Ppeskl8Wnq7HW2E95EF5Rt_GUe-A_D_bGMHV33-eVwouAByQUchRdshKhPaZaBfxlf4gXg9pSxKezu-CFGJGgU2BWowTGUzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vwe3F5HlLwtX8xPJlGESGZ6Ltou6Jth8IFCUpAq5aHxy_dKw8TKWGQmQTa57e63ugwoEiEjCg2WhkO6nbODi56YL6x98WJMWfqqBgeWHNRtz-aAqiO9jOWb-Ws7OwXyCuTYFHf4zPVFCZYWlxh8sZXikQxPJZqnt7agAoyAUGPaYdwcguXQlY3PFPl9L6p-b1Q_FpozxQ17aEm3KNw7VyYu3q2NtAqKa2if6ZMlYbF5Qyznu7xfEgstExCtwNEVz1M7I8wZUcI4VJhccrZbl2DNL65QEodFAuSY8XaOFnHgbwlF9hLAHLC5BbdgIpD6RKv54CT6MDcnesxeFGRQdFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vz6TRtA7f03aRqb1bAgVih42-APMTaRsjLCrJaDNxCXaHOT28OstNMv7u_iR3dHb0_lTRwm-_UF3PDaAIIt8ptGPxXlnmhtQ1OlnE6oY37nEzZfmb562zplU6x-0Hwh7DKpiwuNnj4nCycxFehVmYPyLPFbj-4uSfT0lObCKIAmyUCmxZNNFn0jT3bC4C0uzdmsqImoUgR32QPTGrMYUH5UnorbifiRJCeJlqdWhpynBYYpe-DfZQGUfxHPpLb2s9Q_N2pwjIJ1GlXYGiEa_UhNWKxsPB3osVSpMNT0RY-RXxd0g-D6WCSgG1PTbE1dat-MlNTsiqDnNMGhnvE3FnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jmbOcJXdhBeIQGAxSbgw1F4_p738MDvBrAIU7nmTecSSJ0UhUlxaIujOOZsuPUUZ-j5dHhyjfn_CAP-npRr7yUa2rr3qhMTK76JbuBAqpLBfxz99nRTup-G-XBx77k9CvlCpSmenuSe0ir-JNF4FlqRtRbSGnTBbIxHKpq89jecCe0iQgLRMCeMDJyv7CVsCemhwZoBnkmEI2l-YHyBOrcfYwImOm_YgaeA4ZthSWYzQ5XOV4sYm-TeGQoiPjVUM5Ufio3w4OpvPxA1OCaFjFbqKyRCnzvmgj9jq6s5Ya_Fz4kPMG1-BnVamhqcD-uDqzLihQg871cYXa6buyrnWbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J3TFxuu2O7VV0x7cyQN7MCz99D_vD4uLzAzkcqPLBSGIraDXn6Wy-bQPuZcHw94Ce9Ms7vFdtyc20c2t6QChU60z-sckZpUWGvjrjPkd1YI_LLgws5XLED2vjvrd73NQUxLtcNKhxcl2RvfN75a6kf7gdx_VbirFRko_9-OmI2DOqyOlNXhxZWwPpjrFHYTabZvvpIjKFDc_p8sYQwcwh2QbzN3309BTEf25u5D6j3sMC0WRYIkVwyhWbaVgykSFe4Q0P_v7Nrlk8xgrPwcjS507OHkHLQls6Gz9OpWs5STN3Mb_I0RHoCyijPOf3AeBWDo1MH2CQwyUGETUUGtbRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hqvp3vRaSflKCUokDsKgG3Uy-0R8u9ixqutmpUJkhCb8maPZ5BfkKhxhPq2660gmkXe66xVmviyZvfaKz4_vAKT31cnfeCKOin95BcgWRxxZADZEfAgPFj4py7P5OeUGM2lAkPSmez9MhpxAnorZnckhUPuiUwDtj4F8ZOgqs-zBQ3zybWAwF74vGDS_cQ4F9SXAgjOaWHIHmlMsxfarKmVQJyOvObtso3B1zRr_1pltgL45uFaWielSMCqkaBKZlbWlrK7zQ7fANNXn1MUJJBzq9n07ejYIzwIbFPNPKYwu9b6475o0irwzaGI7IDEANjSDT_efky89EPF7G1haGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gfqLt15qgXvwqit1zOg0gasl2EylADyPREbJJTDS0B0j-T0_cx4uzMIu5EHnFz7u4fUt1jkef0fUASt8LwytNEAPg4qPMRPiRTbP3ftmFoReU8Hs_ufR0_a3WpjQB8pFhlMoqDSkaQAGM3ScQhmHIwqF5N_sgkeXotGO2rTgjRAuL34RIhc8kEaArW8ZPnBNYJ4QE9Ybi4FHMZBJILLMLxNX6C0jKQp0KaOGbhiPsPrwulPJDRLmCkf_RR3vNhsBRlnsfOEJXLe_iarFALmzg6sBZh4nXOa5lpRHdsWMWx_aEUh4IeEl-C5N1h5aDX1Jk5NQLOnAmK2h0zw2J3QpRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
روایت مخاطبان خبرفوری از قطعی برق در ساعاتی غیر از زمان‌بندی اعلام‌شده
🔸
اگر شما هم چنین تجربه‌ای داشته‌اید، از طریق الوفوری با ما در میان بگذارید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/671518" target="_blank">📅 22:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671517">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
معرفی فیلم: کتاب قانون
🔹
ژانر: درام، کمدی، عاشقانه
🔹
امتیاز (IMDb): ۷.۰/۱۰
🔹
خلاصه: زنی لبنانی که پس از آشنایی با اسلام، با مردی ایرانی ازدواج می‌کند و به ایران می‌آید؛ اما آنچه در رفتار برخی مدعیان دینداری می‌بیند با آموزه‌های دینی که به آن ایمان آورده…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/671517" target="_blank">📅 22:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671516">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
شیطان زرد درباره ایران: من از تعیین ضرب‌الاجل خوشم نمی‌آید
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/671516" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671515">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e6e5618c.mp4?token=Yrn9NhTujHN1GxPmW55yJ6Knjh_YK6m5GQXptP-h8R3BM4ljO7Jg7IQlNuzx0L-mKPaONalr7SiYwoRhEhIi2O4VGfzO7ZGsICEnSDzu1QaaqQ3Kh_AW16lk1xnWzK-IFDC8bQlphJ0qWbLa6xxu47CXQ3U7MMxziyJzDmcRUgOZLSyLrrGjr8mFcAK1uL5tpvyQ29fmfiV56igQ2OkM97rDmHqJ6TX4rN0NCOJjKQhffCLPEWH9RFZ75oC-yAz9DLfuYPz84Mo12zRHaRp02n4OvGl5zIU9LXOjGLcYz-dIXjeUSnri_w-79ssP5M8p_8qx5FWn8a0SK9cTxDIWZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e6e5618c.mp4?token=Yrn9NhTujHN1GxPmW55yJ6Knjh_YK6m5GQXptP-h8R3BM4ljO7Jg7IQlNuzx0L-mKPaONalr7SiYwoRhEhIi2O4VGfzO7ZGsICEnSDzu1QaaqQ3Kh_AW16lk1xnWzK-IFDC8bQlphJ0qWbLa6xxu47CXQ3U7MMxziyJzDmcRUgOZLSyLrrGjr8mFcAK1uL5tpvyQ29fmfiV56igQ2OkM97rDmHqJ6TX4rN0NCOJjKQhffCLPEWH9RFZ75oC-yAz9DLfuYPz84Mo12zRHaRp02n4OvGl5zIU9LXOjGLcYz-dIXjeUSnri_w-79ssP5M8p_8qx5FWn8a0SK9cTxDIWZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروی نظامی یکی از ابزارهای حل مسئله است، نه راه‌حلی نامحدود
ادعای جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
🔹
کاری که رئیس‌جمهور بسیار بسیار ماهرانه انجام داده، این است که گفته ما در این شرایط زمانی از نیروی نظامی استفاده خواهیم کرد که به چیزی که سعی داریم به آن برسیم، مرتبط باشد...
🔹
اما ما قرار نیست کاری را بدون پایان و به طور نامحدود انجام دهیم... ما سعی خواهیم کرد از نیروی نظامی خود به عنوان یکی از ابزارهای متعددی که برای حل مسئله در اختیار داریم، استفاده کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/671515" target="_blank">📅 22:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671514">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7b3fa6a0e.mp4?token=h1BpGNNwDSHpyA623jkwQ3jS4TBE8styypKVHO0uQyD6_QNjvMrEfBVRYKX0lWmqitErBXG1FyYxtYPDYu-_nAECkDG5XjDJjvZ5pHaBuz6l4LF-Hlue7BKGk3nUFBfUbUZ6yEmrhSAdr2cpS65buJSr2J4hOeVTXLmOzz30NXlmSyfprfbkGNFfI3hGRkavnj89J5f9S1Ov7zMqIsYfg-i3xvMv_qpGbG5xydo_KI7nh6SNYaUhcHY67lPnkf0Dx3rGEdBjXrn4Nz02VOZS_PiJ6F_k1RtzTUHX_iFRhSOGMliQIcz1N9I25JUxuYCeQBXVMPTdR7zkYNHHovBRBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7b3fa6a0e.mp4?token=h1BpGNNwDSHpyA623jkwQ3jS4TBE8styypKVHO0uQyD6_QNjvMrEfBVRYKX0lWmqitErBXG1FyYxtYPDYu-_nAECkDG5XjDJjvZ5pHaBuz6l4LF-Hlue7BKGk3nUFBfUbUZ6yEmrhSAdr2cpS65buJSr2J4hOeVTXLmOzz30NXlmSyfprfbkGNFfI3hGRkavnj89J5f9S1Ov7zMqIsYfg-i3xvMv_qpGbG5xydo_KI7nh6SNYaUhcHY67lPnkf0Dx3rGEdBjXrn4Nz02VOZS_PiJ6F_k1RtzTUHX_iFRhSOGMliQIcz1N9I25JUxuYCeQBXVMPTdR7zkYNHHovBRBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مأموریت من تحقق اهداف رئیس‌جمهور در قبال ایران است
جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
🔹
این همه حرف‌های بی‌ربط و مزخرف وجود دارد، در حالی که کاری که من واقعاً سعی می‌کنم انجام دهم، تحقق آن چیزی است که رئیس‌جمهور به من گفت تا به آن برسم، که همان حل و فصل این مسئله به گونه‌ای است که به اهدافمان برسیم. ایران سلاح هسته‌ای نداشته باشد؛ جریان آزاد نفت و گاز را داشته باشیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/671514" target="_blank">📅 22:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671513">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09524fedc4.mp4?token=I64ZfFYpTzE2822bvhyNAFekVYqdtF-cnqke_J_Qt41cu89Fy3U7Br5M2q-hmt8-6uAHpkkaNEDo7DGHuloloBgg0RwoE5kEZi-5-rWDIzMl4iAl3YQhLZAzKk4PRldkhKyPPSlk7KjAq5--wLNuORNJwWS8kt7kJSWhAPPA4LBz2Utlr9kmuJvQES0VI1IccigNj4wB9x59DWSnTAeYEZp9cEVM-yPjGRoGY9Z54VVuyEPv6Lxb1h22QaLv_92cyo2ceOj0w6Teed2s-c4awFwgjZW-jyq5dEEWebRON4XDchC3ApgMZzRbTWZHXqGAAj9_cTygNfUbHYOEUmZ3Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09524fedc4.mp4?token=I64ZfFYpTzE2822bvhyNAFekVYqdtF-cnqke_J_Qt41cu89Fy3U7Br5M2q-hmt8-6uAHpkkaNEDo7DGHuloloBgg0RwoE5kEZi-5-rWDIzMl4iAl3YQhLZAzKk4PRldkhKyPPSlk7KjAq5--wLNuORNJwWS8kt7kJSWhAPPA4LBz2Utlr9kmuJvQES0VI1IccigNj4wB9x59DWSnTAeYEZp9cEVM-yPjGRoGY9Z54VVuyEPv6Lxb1h22QaLv_92cyo2ceOj0w6Teed2s-c4awFwgjZW-jyq5dEEWebRON4XDchC3ApgMZzRbTWZHXqGAAj9_cTygNfUbHYOEUmZ3Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در انتقام دیگر هیچ خط‌ قرمزی مطرح نیست
🔹
گفتار مهم استاد رحیم‌پور ازغدی، عضو شورای عالی انقلاب فرهنگی  درباره از بین رفتن خط‌ قرمز‌های انتقام درباره انتقام امام شهید امت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/671513" target="_blank">📅 21:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671512">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ونس درباره مذاکرات با ایران: نیروی نظامی یک ابزار است، اما دیپلماسی هم یک ابزار دیگر است
🔹
از آمریکایی‌هایی که می‌گویند نمی‌شود با ایرانی‌ها مذاکره کرد کلافه می‌شوم. پس راه‌حل شما چیست برای اینکه افراد دست از شلیک به کشتی‌ها در تنگه هرمز بردارند؟
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/671512" target="_blank">📅 21:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671511">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ونس: ما برای تغییر نظام ایران، نیروی زمینی اعزام نخواهیم کرد
🔹
معاون رئیس دولت تروریستی آمریکا که به توان نظامیان ایران اشراف دارد، گفت که این کشوور قصد ندارد نیروی زمینی برای تغییر نظام ایران اعزام کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/671511" target="_blank">📅 21:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671510">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
اعمال محدودیت مصرف آب در فرانسه در بحبوحه گرمای بی‌سابقه
🔹
وزیر گذار بوم‌شناختی فرانسه مونیک باربو روز چهارشنبه گفت که این کشور با وضعیت خشکسالی «استثنایی» و «بسیار نگران‌کننده‌ای» روبروست و تعداد بی‌سابقه‌ای از مناطق تحت تأثیر محدودیت‌های آبی قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/671510" target="_blank">📅 21:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671509">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
تصاویری که می‌بینید انفجار موشک نیست!
🔹
در شرایطی که برخی استان‌های جنوبی کشور درگیر جنگ با دشمن آمریکایی است در همان حوالی، معدن باریت آبترش رفسنجان با انجام عملیات آتشباری مشغول توسعه عملیات معدنی و افزایش تولید می‌باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/671509" target="_blank">📅 21:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671508">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
فعال شدن پدافند هوایی کنسولگری آمریکا در اربیل
🔹
شبکه المیادین از فعال شدن سامانه پدافند هوایی در کنسولگری آمریکا در اربیل خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/671508" target="_blank">📅 21:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671506">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0868a52354.mp4?token=DTu1e-IyXmvE3nL9PYNCbbM2d2FrEcGytOjJ2KabwB2YN3osohd1GG1wn9Hj-kbdQ33UUNFKIDm4riLg_n-0zotepzBmWzeE2z0NkhYGwZn_OKHHY6uh8aAvMeiLWjaslqvCZh7uZ-Ymh5DtjotItROD3to7VXw24nPI5X2NoszC873JsoCURw6rC-64CnxultpAOyNXZ-jXBAUwXPI7dIuEKqBRzxZrq7WGywSJscLk1e4wSSWWxfCLOHblFPKgsdFBg41sfvZU8u1huRHzJaIxDwehhu3DJYe8MP8p9-UdvGsU9nhUTtRkJy_3k3rhUMnvuZt_dxAHre3tbWR8zLrckKE-WaEBNKoMBHdyhhGh1VINdZSmioasCGCOOExxQAzvR8y9rQZ012uOtRH9ZbD9OvPmHzRo0LJUUqXbYd0prSUPuRJPreBGONEp6MR8C9ov_LrAWW9kjnn0N1CkFH7GESBWcO2farv_GXNdoYNb7auHPJp71YPOnMogLdyNm60nZw9OYgJEhIDo_ISdtFz9OhuRp7Zxpv9nyEPX4XofS4OafyA8Qnb6h6SKoEuCF9LCimILDfXcOKbBLtcHEK3Y9XNB_MFDNcvz8PrHohijNkyxQ28RrWavHza0AYw-pOXkW6MBMHmitBXjkhDK5cAJRKnWYnag2kIU1GzuXUI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0868a52354.mp4?token=DTu1e-IyXmvE3nL9PYNCbbM2d2FrEcGytOjJ2KabwB2YN3osohd1GG1wn9Hj-kbdQ33UUNFKIDm4riLg_n-0zotepzBmWzeE2z0NkhYGwZn_OKHHY6uh8aAvMeiLWjaslqvCZh7uZ-Ymh5DtjotItROD3to7VXw24nPI5X2NoszC873JsoCURw6rC-64CnxultpAOyNXZ-jXBAUwXPI7dIuEKqBRzxZrq7WGywSJscLk1e4wSSWWxfCLOHblFPKgsdFBg41sfvZU8u1huRHzJaIxDwehhu3DJYe8MP8p9-UdvGsU9nhUTtRkJy_3k3rhUMnvuZt_dxAHre3tbWR8zLrckKE-WaEBNKoMBHdyhhGh1VINdZSmioasCGCOOExxQAzvR8y9rQZ012uOtRH9ZbD9OvPmHzRo0LJUUqXbYd0prSUPuRJPreBGONEp6MR8C9ov_LrAWW9kjnn0N1CkFH7GESBWcO2farv_GXNdoYNb7auHPJp71YPOnMogLdyNm60nZw9OYgJEhIDo_ISdtFz9OhuRp7Zxpv9nyEPX4XofS4OafyA8Qnb6h6SKoEuCF9LCimILDfXcOKbBLtcHEK3Y9XNB_MFDNcvz8PrHohijNkyxQ28RrWavHza0AYw-pOXkW6MBMHmitBXjkhDK5cAJRKnWYnag2kIU1GzuXUI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروی هوایی روسیه ۳ کشتی باری اوکراین و ۴ قایق بدون سرنشین اوکراینی را به این شکل هدف قرار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/671506" target="_blank">📅 21:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671504">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/050eacefc3.mp4?token=ULclwugKovY2EY7Yv1GUAY3ftneGp5ZbxVC2XNn8hatBUmiZfJiXeHbUaSy1JpimNkJEOoCblpJIyT51AYiIP0veASoRF_sp2u2Qk2uDWqVfDyAqAZ2-oicDxh-dezPAfUpXzXeJCGAciBwG8P92tPLNo392owukUk6bAvT7MmtYrfazvIHWBrwSCw7B9VD9hOlJjwtE9efVFlGV-fSryhR9-pO7EHpsrNtcHvlP0cFz7MafWWJ08XVn7PeI6Cl7a6Z4xlkZODDv2uwA-bvhpZ7Qfz5KPhCKcyXv7nVJG8NZkom84ieffC1JVM94F8lraqEbWXXV5_hjaz7IHgo7Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/050eacefc3.mp4?token=ULclwugKovY2EY7Yv1GUAY3ftneGp5ZbxVC2XNn8hatBUmiZfJiXeHbUaSy1JpimNkJEOoCblpJIyT51AYiIP0veASoRF_sp2u2Qk2uDWqVfDyAqAZ2-oicDxh-dezPAfUpXzXeJCGAciBwG8P92tPLNo392owukUk6bAvT7MmtYrfazvIHWBrwSCw7B9VD9hOlJjwtE9efVFlGV-fSryhR9-pO7EHpsrNtcHvlP0cFz7MafWWJ08XVn7PeI6Cl7a6Z4xlkZODDv2uwA-bvhpZ7Qfz5KPhCKcyXv7nVJG8NZkom84ieffC1JVM94F8lraqEbWXXV5_hjaz7IHgo7Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله موشکی به مقر تروریست‌های ضد ایرانی در اربیل
🔹
رسانه‌های عراقی از حمله موشکی به مقر گروه‌های کُرد ضد ایرانی در اربیل خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/671504" target="_blank">📅 21:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671503">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
انهدام یک فروند پهپاد «لوکاس» در بندرعباس
روابط عمومی سپاه امام‌سجاد:
🔹
امروز یک فروند پهپاد «لوکاس» دشمن متجاوز، توسط سامانه‌ نوین پدافند هوایی سپاه امام سجاد تحت شبکه یکپارچه پدافندی کشور در بندرعباس، ساقط شد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/671503" target="_blank">📅 21:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671502">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
تداوم حملات توپخانه‌ای و هوایی رژیم صهیونیستی به جنوب لبنان
🔹
منابع خبری از تداوم حملات هوایی و توپخانه‌ای رژیم صهیونیستی به مناطقی از جنوب لبنان خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/671502" target="_blank">📅 21:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671501">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b4786a59.mp4?token=LW8kGWtWY7e9MQHEawQzAjQhTgWEuZUAp4kXSWxyUSHSaCNPz9rDWvYkTnU3_Bdnqe4KYVwNCM4YM8r_TibO9Oxx036VLILymeankX3Qh9AoxHT9uxU-UVyzHRL14VBfLIOjy8dWbVl1DjH-CiNkaqetgcRPc9Xbf4Y6s9JjNzG3NGcv7bU4gmuhT04puLxK3x3U4vNCKQfwxGb1SdY-ruV5zc050RSPLAaNaNb4Z8HMCBMNYMcq0dpiJ9ju0Of2JLh2QE2cRzn_WmC9kLW7TJn1_J2XwOXazTyojBbsVmj_jdebnhPWmxcogOVUSIzh6bpx-UsGjCSyNbhz3EiyRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b4786a59.mp4?token=LW8kGWtWY7e9MQHEawQzAjQhTgWEuZUAp4kXSWxyUSHSaCNPz9rDWvYkTnU3_Bdnqe4KYVwNCM4YM8r_TibO9Oxx036VLILymeankX3Qh9AoxHT9uxU-UVyzHRL14VBfLIOjy8dWbVl1DjH-CiNkaqetgcRPc9Xbf4Y6s9JjNzG3NGcv7bU4gmuhT04puLxK3x3U4vNCKQfwxGb1SdY-ruV5zc050RSPLAaNaNb4Z8HMCBMNYMcq0dpiJ9ju0Of2JLh2QE2cRzn_WmC9kLW7TJn1_J2XwOXazTyojBbsVmj_jdebnhPWmxcogOVUSIzh6bpx-UsGjCSyNbhz3EiyRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقام امام شهید، یک مأموریت الهی است
حجه الاسلام محمد قمی، رئیس سازمان تبلیغات اسلامی:
🔹
در پیام رهبر معظم انقلاب واژه‌ای بود که انتقام و خونخواهی را از یک سنت جاری الهی فراتر برد و آن را به «مأموریت الهی» تعبیر کرد
🔹
برای اجرای «مأموریت الهی» همه باید آماده باشند، تلاش کنند و برنامه ریزی داشته باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/671501" target="_blank">📅 21:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671500">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای مهیب در اربیل
🔹
منابع رسانه‌ای از شنیده شدن مجدد صدای انفجارهای مهیب در اربیل واقع در شمال عراق خبر دادند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/671500" target="_blank">📅 21:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671499">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ونس: ما برای تغییر نظام ایران، نیروی زمینی اعزام نخواهیم کرد
🔹
معاون رئیس دولت تروریستی آمریکا که به توان نظامیان ایران اشراف دارد، گفت که این کشوور قصد ندارد نیروی زمینی برای تغییر نظام ایران اعزام کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/671499" target="_blank">📅 21:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671498">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDF1PtQ-FJG1DDIpberz15WZchVQAdljVFBbm-p7nkPMiv1qO4_eKlbVaUdp1aakD6IoiXtD7WNzM-U6Rmvpl8F1Gva54ked1HauiUo3y1TFVAVPOvxp7q6PnPYqTgconryodZ5bimiGpO4jyTsCLnMEK3Tgs8ww972m_AzlHG_g8t1x6hX8mUicqYC3k5kM1_xOL91bdqY2w4s6V8GkCNGKOxLN4vwoqcQRVDXQmhHLVOyIBSa7g4nb91oHjNA3sgXdTneXRpfNxnCptF72gdjh4WMLMxUck8jsM0NBUumNiHgBGdpYBYUE3ofYlMuStSRwJ9qFznnmLJbRYfhbxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ایران یک جان به‌هم‌ پیوسته است
🔹
ایران را نه با خط‌کش جغرافیا می‌توان برید و نه با واژه‌ها می‌توان تکه‌تکه کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/671498" target="_blank">📅 21:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671497">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
قالیباف: مردم جنوب کشورم، شما عزیز جان ایران هستید، جان ما هزار بار فدای شما
🔹
به مردم جنوب کشورم که این روزها در خط مقدم جبهه قرار دارند، می‌گویم که از ابتدای جوانی دوشادوش شما خواهران و برادران عزیزم اسلحه به دوش گرفتم و جنگیدم، شما عزیز جان ایران هستید،…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/671497" target="_blank">📅 21:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671496">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
قالیباف: بنده هم در میدان دفاعی و هم در مقابل طراحی دشمن در جنگ رسانه‌ای بودم، بعد از آن هم با علم به تمامی مشکلات و تخریب‌ها در سنگر دیپلماسی حضور پیدا کردم و هیچ‌گاه از زیر بار مسئولیت شانه خالی نکرده‌ام
🔹
هدفم اعتلای ایران عزیزتر از جان، تحت هدایت‌های…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/671496" target="_blank">📅 21:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671495">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
قالیباف: حمایت و اعتماد شما به سربازان عرصه دفاعی، دیپلماسی و خدمت، دست آنان را مقابل دشمن برتر می‌کند
🔹
مطمئن باشید آن‌ها جان خود را ضمانت امنیت شما و منافع ملی ایران گذاشته‌اند و با تدابیر رهبر معظم انقلاب و مسیری که طراحی شده، نتیجه این اعتماد و حمایت…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/671495" target="_blank">📅 21:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671494">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
قالیباف: برای ما مسجل است که انتقام خون آقای شهیدمان را به ثمر خواهیم نشاند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/671494" target="_blank">📅 21:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671493">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
قالیباف: همه می‌دانیم که مسیر دشواری پیش رو داریم. آن‌ها قبلا هم ما را با ناو و حمله هوایی و زمینی و ... تهدید کرده‌اند، نتیجه‌اش را هم دیده‌اند پس نباید از تهدیدهای دشمن ترسید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/671493" target="_blank">📅 21:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671492">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‌
♦️
قالیباف: مرز بین جنگ یا مذاکره با دشمن، براساس امنیت و منافع ملی مشخص می‌شود و تشخیص استفاده از هرکدام از این ابزارها، متناسب با اقتضای زمان و شرایط، با ولی امر و فرمانده کل قواست
🔹
همه ما وظیفه داریم متناسب با تکلیفی که نایب ولی عصر (عج) معلوم می‌کنند،…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/671492" target="_blank">📅 21:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671491">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
قالیباف: باید بتوانیم بین دو روش نظامی و دیپلماسی، هماهنگی ایجاد کنیم و نباید از جنگ یا مذاکره هراسی داشته باشیم
🔹
جنگ و مذاکره دو روش حفظ منافع ملی است. مذاکره در این مقطع همان‌گونه که بارها اعلام کرده‌ام معادل سازش نیست، بلکه در کنار جنگ، بخشی از راهبرد…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/671491" target="_blank">📅 21:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671490">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‌
♦️
قالیباف: تفاهم‌نامه زمانی معنا دارد که بندهای آن معتبر و درحال اجرا باشد
🔹
اگر قرار باشد ایران از تفاهم‌نمامه انتفاع نبرد، دلیلی برای پایبندی به چنین تفاهمی نداریم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/671490" target="_blank">📅 21:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671489">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
قالیباف: نگاه ما هم در جنگ یا مذاکره باید براساس منافع و امنیت ملی، واقع‌بینانه و بلندمدت باشد. لذا راهی جز تکیه بر توان خود و قوی شدن نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/671489" target="_blank">📅 21:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671488">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
قالیباف: آمریکا در هر زمان که بتواند به‌دنبال ضربه زدن به ایران و پیش‌برد منافع خود است و این محدود به جنگ،  مذاکره یا فقط این رئیس جمهور فعلی آمریکا نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/671488" target="_blank">📅 21:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671487">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHOLv9iYoXVLcOzAcAm5wM1bfCw4MyjaSM9blB4uaCGmFcGS0VzyPWwWKBc_wDxX5AUtGscN2TkrlWNBMl_ewmf8NdAcMFZ-D80cHuDqFl-4d9Jpvv16z8_qPfilvRuvsoheVs2BeyhgKSDcxCCq9djTS3eVHckkjbmw4WmNFVhL_LKV5ZZcFtPgue7hFA1GFyHIq6cfMJjDOXJr-18zognCTn-g64P52JRHNAWotZeN5Oxyx4Ngu34NBArC4f-NNyf4P2sGMsPxTUpAG-XvsoB2IxE0Rxhqm_RUW2S5qlaq5GEAviOY0pwlhCH8WZCFhUZi_vqQrRzI3HxJDY9qYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
با بیمه‌بازار، سلامتی شما بیمه است
رسیدگی به سلامت دندان‌ها مهمه و داشتن
بیمه تکمیلی مناسب
خیالتون رو راحت می‌کنه.
✅
در بیمه‌بازار
می‌تونید پلن‌های مختلف را یکجا ببینید و پوشش‌ها و سقف تعهدات را با هم مقایسه کنید تا انتخاب مناسب‌تری داشته باشید.
🦷
پوشش دندان‌پزشکی تا سقف ۴۰ میلیون تومان
👈🏻
دریافت مشاوره رایگان و استعلام قیمت
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/671487" target="_blank">📅 21:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671486">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
قاليباف: ما در یک جنگ جوهری و وجودی با آمریکا قرار گرفته‌ایم که هدف آن علاوه بر ساقط کردن نظام مقدس جمهوری اسلامی ایران به‌عنوان نهاد اصلی جبهه حق و چندپاره کردن کشور عزیزمان ایران است. این راهبرد دشمن تغییر نکرده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/671486" target="_blank">📅 21:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671485">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
قالیباف: باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم/ ما هیچ‌گاه از جنگ استقبال نکرده و نمی‌کنیم اما باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم / باید از ابزار دیپلماسی و مذاکره…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/671485" target="_blank">📅 21:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671484">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
قالیباف: باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم/ ما هیچ‌گاه از جنگ استقبال نکرده و نمی‌کنیم اما باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم / باید از ابزار دیپلماسی و مذاکره هم استفاده کنیم تا منافع ملی را محقق و تثبیت کنیم
🔹
این روزها که دوباره آتش جنگ شعله ورتر شده سوالاتی در بین مردم و گروه‌های مختلف پرسیده می‌شود و هرکس به فراخور نگاه خود به آن پاسخ می‌دهد. آیا ما به دنبال جنگ هستیم؟ آیا جنگ و سایه جنگ پایان می‌یابد؟ آیا با مذاکره می‌توانیم به اهداف خود برسیم؟ وقتی با آمریکای بدعهد طرفیم اساسا مذاکره چه فایده‌ای دارد؟ و در نهایت موضوع مهم این است که چگونه حق خود را بگیریم و پیروز این جنگ باشیم؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/671484" target="_blank">📅 20:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671483">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2aac84bd.mp4?token=XFiKYnjRZ4h7W97i9AlrI48mKnRYeGtXD-EExpgWCFmI7p9ZiC70nlMGixg5GmcivoWD5Q-JRQtuZaFcBi0PJYFFJ1dM-UIFLE8RCBlB1H8x5T-K8FvWBRnDfQD_BcpWxcBoLsVMpusfKbunpJUKbFwnReHo_jWqwyuq5ppSXLIvrHKY0mN0GkgsNb3YJAeJuNdfuZ2-3m_-d5goTPTWIF42p1b77GB5j1ay3ZA3yCOA1WCwGBebbIHxTonoIZigB3nJU5DkbgFAu91FUanjsR5MnNMY66jauFdCTuH4O-MxAKFEiXevVyEnIbrU1E_5riJzdpreFr-a8g7Ce3oy3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2aac84bd.mp4?token=XFiKYnjRZ4h7W97i9AlrI48mKnRYeGtXD-EExpgWCFmI7p9ZiC70nlMGixg5GmcivoWD5Q-JRQtuZaFcBi0PJYFFJ1dM-UIFLE8RCBlB1H8x5T-K8FvWBRnDfQD_BcpWxcBoLsVMpusfKbunpJUKbFwnReHo_jWqwyuq5ppSXLIvrHKY0mN0GkgsNb3YJAeJuNdfuZ2-3m_-d5goTPTWIF42p1b77GB5j1ay3ZA3yCOA1WCwGBebbIHxTonoIZigB3nJU5DkbgFAu91FUanjsR5MnNMY66jauFdCTuH4O-MxAKFEiXevVyEnIbrU1E_5riJzdpreFr-a8g7Ce3oy3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ رعدآسای ایران
🔹
ساعاتی پیش در کویت، صدای انفجارهایی از نزدیکی پایگاه نظامی آمریکا شنیده شد. برآوردهای اولیه از آسیب شدید به تجهیزات و نظامیان آمریکایی حکایت دارد. با وجود سانسور گسترده رسانه‌ای، جزئیات کامل عملیات به زودی اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/671483" target="_blank">📅 20:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671482">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ae1e724d7.mp4?token=QpQ7KQI7smkoVUn_wNujNKbsJ7tn0RNBS5U4TnL3CYot1d09alJZTelPs5RuUq4ClC2L1y9okrXdBcTsMgUYMh3MDa1vJFi1369gTZ2uyTXh96e470bQXf1cmxvS7hJiE0K03P7jvQN6IAOMmX0cy0Df-gMxOW_s2-5hrBclod1jSRVqzgO4HVvI4QEBZWe3O0F-3ZLrq6k94gV91zjA0kjaQ6fSkUBqUVgkwlRsTTnzu6Ak0Ulrj263uzxjGOlNJ7auUASUAgviEuzbImbvzj1BkZ7nwBgotKObTmlDDmr8b9T0oZiH39g5KhCeireURgZ4U_snwmLJA_jeWwNLsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ae1e724d7.mp4?token=QpQ7KQI7smkoVUn_wNujNKbsJ7tn0RNBS5U4TnL3CYot1d09alJZTelPs5RuUq4ClC2L1y9okrXdBcTsMgUYMh3MDa1vJFi1369gTZ2uyTXh96e470bQXf1cmxvS7hJiE0K03P7jvQN6IAOMmX0cy0Df-gMxOW_s2-5hrBclod1jSRVqzgO4HVvI4QEBZWe3O0F-3ZLrq6k94gV91zjA0kjaQ6fSkUBqUVgkwlRsTTnzu6Ak0Ulrj263uzxjGOlNJ7auUASUAgviEuzbImbvzj1BkZ7nwBgotKObTmlDDmr8b9T0oZiH39g5KhCeireURgZ4U_snwmLJA_jeWwNLsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط تیرهای برق در نیویورک، چندین خودرو را به آتش کشید
🔹
سقوط دو تیر برق در منطقه «کانی آیلند» در بروکلین نیویورک، منجر به بروز حادثه‌ای گسترده و آسیب به اموال عمومی شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/671482" target="_blank">📅 20:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671481">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
اکسیوس: دیدار با نتانیاهو در دستور کار ترامپ در هفته آینده قرار ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/671481" target="_blank">📅 20:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671480">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
صدای انفجار مهیب در هرتزلیا در شمال تل‌آویو
🔹
رسانه های عبری گزارش دادند صدای انفجار در نزدیکی یک واحد تجاری در منطقه هرتزلیا شنیده شده و پلیس رژیم صهیونیستی تحقیق درباره احتمال پرتاب یک شیء انفجاری را آغاز کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/671480" target="_blank">📅 20:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671479">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
دبیر ستاد مرکزی اربعین حسینی کشور: همه مرزهای اربعینی کشور، از جمله چذابه، مهران، خسروی، تمرچین و باشماق، آمادگی لازم را دارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/671479" target="_blank">📅 20:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671478">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ix0GF255cVZjj69Qlsi1-MYlt_i6sTHpbeFk9Uh1NWq5TiAuQ_vI8nWnnla96ViMcwUKPmxszZvO19n9pmd2YEnjjdPKGRUdCmjxG57XYcpbQ6aF72gVBNsz7z4Jx1TgQgfq5rCo7W7iN07PmnRvb2mTLVlCdrCkSE453i6Wi6n7WBw8LN_bvpoRyvr_8tGFOyDnL542xR9xFfsTuTbnNuXwRr5VdJGCNroKB4aMR0aT5vjcJKzJnRa8lLAvCNBiynW618EQa4qdfVK8EEV_LRpH8rWsniNOhwXiOMOPg-aF66sq3hJZc_GjzslHeqjaTv8-Tgw88AT3LIRdeWxXVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه‌های عراقی: صدای انفجار در منطقه کویا در اربیل عراق به‌گوش می‌رسد/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/671478" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671474">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0c5efec0e.mp4?token=ksKrSGnKB4IL7BqG280j2FEdCBtlkkTiMHk391AG3_8PJk4kNdP_mPRl1K1Zitd_aJpxmw33r-1cpauNh6P5ivQwL6exX1LQAgYWlvA7qdAHIMBpJupj3dcGdh0IDSJyVw_xoq86NTnOQoTY8LKFQRUVGnvTOAEmYsFSdGAMGbMbvQ5wHoJO0v_10qpPRA4YxEeozUtnXqNwqCC-coKhidKDtH2_n6Se-N94byDTCJoF3qccZ29zEKlh6FORoCPPmdrMx7t73mfLWff4rfSlB2ryC03-6vXhhaVIntkIbxLFGjMMNp33dyw9Cwd-HIca8ZB8Xm_hhlpt0lgxCefF8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0c5efec0e.mp4?token=ksKrSGnKB4IL7BqG280j2FEdCBtlkkTiMHk391AG3_8PJk4kNdP_mPRl1K1Zitd_aJpxmw33r-1cpauNh6P5ivQwL6exX1LQAgYWlvA7qdAHIMBpJupj3dcGdh0IDSJyVw_xoq86NTnOQoTY8LKFQRUVGnvTOAEmYsFSdGAMGbMbvQ5wHoJO0v_10qpPRA4YxEeozUtnXqNwqCC-coKhidKDtH2_n6Se-N94byDTCJoF3qccZ29zEKlh6FORoCPPmdrMx7t73mfLWff4rfSlB2ryC03-6vXhhaVIntkIbxLFGjMMNp33dyw9Cwd-HIca8ZB8Xm_hhlpt0lgxCefF8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلاقانه‌ترین وسیله‌ای که امروز می‌بینید؛ «تلاک» به خانه‌ها آمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/671474" target="_blank">📅 20:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671473">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
خبرگزاری یمنی «سبأ»: فرودگاه‌های أبها، نجران و جیزان عربستان همچنان تعطیل و از چرخه پروازها خارج هستند؛ این فرودگاه‌ها در پی حملات موشکی یمن تعطیل شده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/671473" target="_blank">📅 20:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671472">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
تجربه‌ای شگفت از مرز مرگ؛ ۲ ماه کما، ازدواج در برزخ و بازگشت به زندگی
🔹
00:06:30 دو تکه شدن موتور در اثر شدت تصادف
🔹
00:09:20 نوید بازگشت به دنیا در اولین دقایق تصادف توسط خانمی با چادر خاکی
🔹
00:20:30 ندا و فرمان به انجام سجده شکر
🔹
00:35:40 نظاره کردن امام حسین(ع) هنگام تعویضِ سنگ مرقد مطهرشان
🔹
00:47:20 تناول انار با پوست از شدت خوشمزگی
🔹
00:56:50 ازدواج در برزخ و تشکیل خانواده
🔹
01:04:00 شفا یافتن و خارج شدن از کما توسط انگشتر امام رضا(ع)
🔹
قسمت دوم (رهگذر خواب‌ها)، فصل پنجم
🔹
#تجربه‌گر
: داوود سلیمانی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/671472" target="_blank">📅 20:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671471">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
پروازهای شیراز – دبی پس از پنج ماه از سر گرفته شد
🔹
این پروازها که پس از پنج ماه وقفه اجرایی می‌شوند، از امروز (چهارشنبه ۲۴ تیر) آغاز شده و هر هفته در ۲ نوبت، مسافران را جابه‌جا خواهند کرد./ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/671471" target="_blank">📅 20:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671470">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWpQLdWmRX5As3LSI9hR1DY7K3ylC27kdrraWsVX5WdhXEXgH1mYpBaBZ8Q9-VIuR7lUb9DyRShJzNctk0Yv0SNAeAVk1jY3q9vGV8GTMb9dKTh9ObyuBnckX4bKFrDONlmdDKq6ZGs4T_uNll6A9ah7hY-cEpJGPW33fLtgB0HMCTfgtFxLVgUBMUueco-V5aTAOERUqjmqeB3-JfHuuzEAjV1-CppEIsx0XC9vBG34InaGxib45B6_HTve52H-jJmG-yKssznzRmvEthGFyw-gUTN6PTTEen17c-rNvSM1SBfv8Nm8MzI1D2lT_NCEV1LQk9lDRc0Gi7rQYrOSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیگ ملت‌های والیبال | پایان ست سوم   ایران ۱  اوکراین ۲
🇮🇷
۲۲|۲۱|۳۰
🇺🇦
۲۵|۲۵|۲۸ #ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/671470" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671469">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
آمریکا جنایت خود در حمله به انبار گندم در هویزه ایران را انکار کرد
🔹
سنتکام گزارش‌ها درباره حمله نیروهای آمریکایی به یک انبار گندم در هویزه واقع در استان خوزستان ایران در ۲۳ تیرماه (۱۴جولای) را رد و انکار کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/671469" target="_blank">📅 20:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671468">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXNyvNkhoREMd1UJhNqd8taLeTDz4kqNDBsrFYqk0mU5RaRelhJ6VSb7s34IEv7_Rpl2hAPgoRbaVlIj4xWmI2d_8qKqCqCqqQfhiTaKlF4JoNHuZypKt8S8L-EosrK77AzOGr3ZlgsX2xeR9XwKKmlFUzhR1yYN1Uqovyc3oGrOtrgctp5cfHItvXkh2PyYXua6ZuPWnig63m96Kx5cE8XGe-SQ15_gAq2ur0YEiX3yyLf2ACNP48DOKQAgzqk0V-0ldrvjn6uSWZyKQGk_RKI-sxSuh6KYRRGYjZqOXp6tGu_5dQHcIQ6OqeWXCo3HErptvxjMFmN1VxnTwbcQNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت یوسف پزشکیان درباره موضوع انتقام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/671468" target="_blank">📅 20:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671465">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OpH-MI0tMitkw8EHVpB8JyiubFfeI6bjg3EsnhcgclRLh358G_1_vIDowbEmSxyKCcpgY0sXDoAwSkZwcvxqsB6t2qx6ntXcV4-8pSTFeZakSpSGk-1mBPEDVIL7VDahJz-GELbw_nooTaYgTZzagmiTU9TASCAafExU9tNGciUyDdi7F0agVaVcqBujB_v_hNMAfGOYfTKGSyzF9bgWn8n_YLNC8Vp5FLuhMHlOJO5TCmK1d3y93xaU1wORhpUJoOSNGgCN7SnwvqBIJa99KTkqYQsLIaQZe1leDOEV9jGwU1_tCEGFZDmlCFbkGOvQFe6AfMrbCEcrmIx7DYeLcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kl3O7JO_Wiv-TS_iVo8CuCOUC3mVzHU8mWDNq9-p-10SDmXyb-wEWq74H2Cy_9Mwl4AF895ILIHnawfW5O9ieTHe23Pwgzso_0uriIRNjhFhDqMxobEI36QqfvaZRExr5rlRxiz_zMI8vNQqeaXypyfT_o0M7Pk_Vxe98wFqSeIRObKrDBbZD-p_-SeTye6pxFuh2SD1c_WbaD-pBCIEM03g0I57ELmPPN6CXabOJukwpzkerUP_Ozcs_aOxJ7TWFGYCiNZh0XLQ-bAmEkGFdmHLP0uFs7Wh2X-imYsycf0vSSa0oD5l0WhbY2Jmjo5RNHtNn0wouEw6oGcYJTxCHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DkFlN_9x6HXGLS8Vm9qQE0PykMtN26G3o6bxBH-gno4bvuinhFrVfmvjZe_owXKXKrseiNIYlQ8QhZ-r_zrx5NQBd2l0pZcx6CcB9sQXbsyeQ3cMzjXzqSabqXGbTbl2jj6kY4udU8c9sN57lvicUxdDAcqt7DeT6dTX70HIyXJ0y-89ehoN29VEJ6o3ic8ekB__JIDsLiTYeFC1P3ioq7lv4n6gCqRMw9SVW86HBv-2PMVWW_Gn3sDDv3sCzIKGlkA4XgqUhatOvnPxY-ldoxi27r7N-Uqdz8zXsm4cWN17fynnQgxH7gqxQiDndTFlGmLo9iXjKjPc6PQVkoTohA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از انهدام پهپاد آمریکایی لوکاس در بندرعباس توسط رزمندگان سپاه
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/671465" target="_blank">📅 20:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671464">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
عون: تلاش برای توقف جنگ علیه لبنان و عقب‌نشینی نیروهای اسرائیلی ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/671464" target="_blank">📅 20:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671463">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
یکی از مسئولان باشگاه پرسپولیس: اخبار مربوط به مذاکره با یاسر آسانی صحت ندارد و این بازیکن در فهرست نقل‌وانتقالاتی سرخ‌پوشان نیست
/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/671463" target="_blank">📅 20:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671462">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YW282-1Xc-iLjlW8IU-fpaJrDZLt2XSJ8MaGGz4iYs2ES_b4fZYny_LnEWwT7_cbY1ezCe1Tk2IaoFx7LNoTqC70xLAvFYuY7fsiMeNXC60XaDD1p1Dod1i62LBDkJhmUZj9snOcnXhYvTo7WQPKdgGTlJjMPMfZUCuBrNpdZxXvLhEJQDTdIHvDr9P6Kbw6fV5_gT2WMrU04SDlGbJGETU72Iyy7NtUGtaVW3fHilc0vE5bsEeR-iX6EfYUpvmGBXHR5UFptUiK7Ajh3l8gDr0PagjJEiJ8CMHLSOCNrXWnFiDN4wapBpy8ZbYnwe_8jLSbdYywRZGrJoShTSAvpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه امروز قیمت‌ها رو دیدن...
تو شرایط خریدت رو هم ببین
💎
اجرت از ۳٪
🏦
خرید طلا با هر بودجه، از ۵ میلیون تومان
🔄
تعویض طلای سالم با عیار۷۵۰
👰
سرویس عروس از ۱۰ تا ۶۰ گرم
📲
داخل کانال
https://t.me/haghgo_gold
ادمین :
@haghgogold
_
__
آدرس شعبه ۱: ستارخان بین فلکه اول و دوم صادقیه پاساژ زرناب طبقه همکف پلاک ۳۲
شعبه ۲: فلکه اول صادقیه زیما مال طبقه B1 واحد۴
برای اطلاع از موجودی تماس بگیرید :
09924100036  ---  09924100039</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/671462" target="_blank">📅 20:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671461">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: فعلا برنامه‌ای برای مذاکره نداریم و روی دفاع متمرکز هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/671461" target="_blank">📅 20:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671460">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1_1693951181.pdf</div>
  <div class="tg-doc-extra">7.8 MB</div>
</div>
<a href="https://t.me/akhbarefori/671460" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
فایل کتاب به نوجوان گفتن از نوجوان شنیدن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/671460" target="_blank">📅 20:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671458">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/El-IIwbRX2GqEf5YnLWHnF5dXh0z4bqGPPK0rKNmvZWVQPTnjNkewWtATRdQNm_euGfXUTCpzO1hie3yLDfbWNvTte3nuPLjSEuN9g-k9BzQQz8loyjfrvntUePzhXCH2SJJ8NtcJi9cgPwAsfdqToBO5NZ28R8XmvDc4L0xoVVgI_ZncAcXiILN33QILTzyActB-ICA9Lf-gEgvy8oAi2iJFFqQyLR1kEhB-yJfzw2dmWUgMBn13tBj_W8sdpELZNx7QpDBA1wMPKUf1INv0_kZTXyqsOswo763zvhrVxNNCrr_ZAuqbihhWiMpcTiPHWsvSBUYrTwcEo9gxhIFfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P422JLmDhyqKFMxGOdZ91lITVEE-Y4c78bTz_AJcZEy__kOud1xUe11jLUT_nAoYt7kxQxnAIKb6caPBvUswGfOBmqDz1JeIsoEUZ_a3ReZ1Fp5vKNeytl_7Ls7nfxJkxEWrFOt_asqg2-PzT4Ws6mdDHHGCIJdudV6S3Hb68Eb1GOwrGIbyQPLT0boQLnWgwHbzgGgYseXdBcUZRbYbg-As78pitpbM2vguGFkoS11sMhhSrIpCUSW6WW0cLI2m-glmkVatztZ2UUX4QjWIFRKesKudNAJ_zN8h2FfXVRFPVnqSYOdgd9SFjlcEBrqBjLVolJCaeEbeAghC-trfvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر نوجوانت به جرفت گوش نمی‌ده، این کتاب رو بخون!
🔹
«به نوجوانان گفتن، از نوجوانان شنیدن » اثر آدل فابر، حاصل سال‌ها تجربه کارگاه‌های آموزشی است؛ کتابی کاربردی که با زبانی ساده به دغدغه‌های نوجوانی، احساسات، انضباط، گفت‌وگو، مواد مخدر و... می‌پردازد و راهکارهایی عملی برای حل چالش‌های والدین و مربیان ارائه می‌کند.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/671458" target="_blank">📅 20:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671457">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtvwuK2U5YJGaoXfNp1k0KrnJfATLBn-L2jTj0qFNe08VTUzyIR9H_k0fT_VyhJlms-a6Kek5hc8YNs5eV0oWvtsTauLJtSf5RTZvLVe_r0H9fL0rEBolyNbDlPuTJO_SeL7GlIK-3T2nFuAo4rAmuLPWqOFAFLLm9Cb5pqB-kRhFyQuNHClqkJFB-73q4HFoLGhoRyQdJVLwZz4OJp4JpuJKjTT7AnrlGp05yVgvwhylSciSSgSbIB8S_GKCMuhaTZc5ZguRmLhIpFgaZ_NEOckqazeJEbwifwTGpjPismiWz_AjbQRX0hLK9FWji2AQ1yFWq1tVg88twREhVYnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلاهای بورس کجاست؟
🔹
در ماه‌های اخیر طلافروشی‌های آنلاین با این نقد مواجه شده‌اند که به اندازه‌ای که طلا معامله می‌کنند، ذخیره طلای فیزیکی ندارند.
🔹
حالا یک فعال حوزه طلا این سوال را مطرح کرده است که مگر صندوق‌های طلا در بورس، به اندازه معاملات خود طلای فیزیکی دارند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/671457" target="_blank">📅 20:09 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
