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
<img src="https://cdn4.telesco.pe/file/D1YSc4QyUKLklhC20sbDWv_i2pa16qmPt4GYYyagysRe0IoQ8KtpKeTMelgNiGB-9kZi1Z5ZH1a5f6wy0D6oVLaOi8kUrcZxBeKPeN8ow4YKzi5ZQAQR5rqzJyLuhwH0zPqyIPI3bVqKKNjanr8G8so55RIUCQjZWfCEFQ247M644ixQn3692bSmlemN4J5a4c6XwDJSRW_luFHLPG4grZKUZUNWYMpG6oM7SPBaapAdLGfJ6pSSgiEviXYErblEoJnT99rSwTsPY7GEe64IBNJzyZokj1vR3W3g7ew9ri5eU3Fg5ppDDfNNwsjaQ3bANHPl7zcyS5orM5qQ1eJW2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 446K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 16:46:03</div>
<hr>

<div class="tg-post" id="msg-30484">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQH3QUxY5RsWlc5HNS-Gvn1s_XggF5U_WUkR0MCL0K7BbqG-zqcT9DmEfoYsaNPhrfk9nPVj9fqvfFoB5BTsnoh5VbgcSbhf1Het1Zhis0YpaIQ9sru0Sh6SjkYKnc9RDtJd8FGHfeLS9HN32mpK9RSppIrrpgDUkLY4AxBEgaZOa4DE0KCnh_6Ub60aWUaHEAL8HxyVosD9xg6eWPrG1QpT8-6iw7x1Ku9779itKmajOzjXgQhRCic7tQGTE5Lx-xCJQRHwXlwNktb5bbVvKIRCNSGRPnC3RdJnCZWyY_w-UqLAd-ngWdNO8YeDD_VnOgeg2TnJfbNziV0Ak2jAXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام حجت کریمی مدیرعامل باشگاه تراکتور؛ معافیت تحصیلی علیرضا بیرانوند یک ماه تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/persiana_Soccer/30484" target="_blank">📅 16:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30483">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHuIG5Ink5lj_m7LGvj2Ms4zYkFiLsTBLBuTbVtvn_ZLbD8ilyXzPsKpb06TUYEX-fuXG4_6h_vGHUCvoQxiTNLmC7z90xmgHA15ckZl3gk13aIA3YeSSP3JL01tNyp2_hWF2e8Ej_7BBYYu1GEjFTuDVVpBnBtDt6ht4Zqh8WdWbmkacQp25Gi4bpDZcoP5BGfdKyopP2Ro3Gu7FhNYN7TVrP5369Ua9s0AEpLENgararLb2Xod6fc2_885yQN-L1maFRALps_jwkV7khyTOwMpyuPJfalRLnghID-Rnj_nqBwsSTO55jn2XzK0keyLPWXvH0aKQcpwzc4emf6UKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
👤
مصاحبه دو سال پیش علیرضا جهانبخش کاپیتان تیم‌ملی: بانهایت‌احترام بازیکنان ازبکستانی هیچوقت نمیتوانند خودشان را با مامقایسه کنند آن ها نه در لیگ معتبر اروپایی بازی می‌کنند نه عملکرد خاصی داشتند، آن ها توانایی شکست ما را ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/persiana_Soccer/30483" target="_blank">📅 16:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30482">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jh2ieWo2NgAdsyTzn2d5GRpv_uSUuAnbEJCf6msrTzg8RWi5dC1DVzHfOgJO6cNBJZ_IKiHUfthXXRaI6_Wl7BdOiPRAEpv1CseDejwm18qoiOssF92kFrd0oz_VjBiKZonSAYx7hlLdBP_Jhk_TYk25ByADTPT0eT7jF11QyJkqQxaI_Cmvth2suJ6WleqRVcY7OTfp64fa3Xk0LE9TXF8bnEiuhafZqYryZkWdNw9oI1tDzgAsRm9fKkJDyLXJ3Q0RW_hygSue-BL5mpW1nIcjjX5E12DgcW-Khod_D4pAUXNDQSYB8dqSm2mYDd5ZFe6e6KpJ6NRZptJbPzPTwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناسان AFC؛ سعید سحر خیزان رو بهترین بازیکن دیدار امشب استقلال
🆚
السد انتخاب کردند. سایت فوتموب‌هم بانمره 8.9 لقب بهترین بازیکن این مسابقه رو به یاسر آسانی ستاره البانیایی آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/30482" target="_blank">📅 15:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30481">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpn6ZpjOdzXzD7-YpTTE1mNk3t1QOd0BKxSjdUMFPJLSctM8CjxKKKbitjAk5v1OrXAGx2I6kZGDrI4rXHLVxH1uZX1BXXPgLou9VBapD8vVc9f_VEND6tgwuMHeJuwL-yBwcclIQiQV_XN4BdWXOym5KCYcNStVp5_f2fYCZQgYBhpjL4gJd6hSGTX9J-3FMK5j0pB-0ZgIKDbQSQxQdJx_wrUKnHyPSYxtcTiZBBcsSsqsGdiypnQnNlp7j0nErsC2jRTAy8f2yyYoIqhPrD3XGUx2uGstIbce6qS56XfiR6bhlIl-ocVcmhZOpuDj8p1xau9KNiiOYTOu0Yfo2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه تمام هشت قهرمانی لیگ برتر منچسترسیتی از فصل ۲۰۱۱/۱۲ به بعد پس گرفته بشه و به تیم‌های نایب‌قهرمان‌داده‌بشه این شکلی میشه. تو سایت‌های شرط‌بندی احتمال‌محکوم‌شدن منچسترسیتی بسیار بالاست و ممکن این تیم به چمپیونشیب سقوط کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/persiana_Soccer/30481" target="_blank">📅 15:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30480">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
تابانی‌به‌فینال‌مسابقه‌مسترالمپیا 2026 نرسید؛
بهروز تابانی درجمع ۱۰ نفربرتر مرحله مقدماتی دسته اوپن قرار نگرفت و از صعود به فینال رقابتا بازماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/30480" target="_blank">📅 15:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30479">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6y8HI07bKyh6812-ShlO5TJlFSDi4ffDf8yHYvHRIGgnLcTqmMGk8zyAdffYCkG8UbCn78KGM4BsDDP-ZI4W-JpvxBe8_Ch3ZoqknWLITFcXuRsfR9wTYEvnSQ9YKODwamHMc90wom-FwkkWDIuk53ukzGOAQdlhwOoXH2oz4ciBdA_fgfL_Au6R00CFv4rXWRSDf0ZrW2pW4Q11lFdLOgOOs3HjTSil3is4xjuud6fltzFnnKlMAvaq7oNFaPXxiVFd7U81q_3hKHOo90N3lNW1QXZujcEIhip5lOvPhY6SDXQMnkEwM-MkRi0mfwbSUw-UVLapafD9qhFdQ_gwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
مقایسه‌تعداد جام‌های تیم‌ملی پرتغال قبل کریس رونالدو و بعد از اومدن کریس رونالدو به تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/30479" target="_blank">📅 14:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30478">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcFV7W5GGSHfJCNjmE6K_5AXcoJM1d5ZxbgnyEAx-AqlYtSZKEhckJDxggrO-mkMHSvMIbHcL8EEXZB80lnCSakQstXh3l2SGZFEQlC9csj0V3F7dX90ISyJpxKAl_KTrO_bqp9UsF36fH-vEiKB_13sldIdOKmopqNT01dmHj5hxmQ6TjVL2HWqV9DCxR5H3_ejpQiCC5M0RjTHXNFr_UUlB5tbN0CveAgAzoC8lT_4UwlX_OIovlmrnKfihsJXN1GFkplneSSzFU6d4G4mlceA-DAecwSC7oqZqd0fJoonMVPzcFAwEbU82SBM-vyQLO0hfAI6I-wAfo1pefk1Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مدیریت پرسپولیس طی روز های آینده و تا پیش از نیم‌فصل‌قرارداد اوستون اورونوف ستاره 26 ساله‌ازبکستانی خود راتاسال 2030 تمدید خواهد کرد. توافقات بین طرفین انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/30478" target="_blank">📅 14:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30477">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXVPrd_jzvmTt3RTKhFIPfEWPE2zNM3zyMGqwhjOTQvt8-yAh7Ai4Ebt7ZJSf0F_j4yGL7awf-nbgTM8jk-7JrYeFYsnsouKIfJjS2Vs8yaOyMQSEKxjC_YEg0Fs0DOfS-X5mM0YphP3LdZj_WqrR71_X4pDu_7zblaqmbdqrDcTSELOreuoXbQtL1bYEx_K_8H9aXXXe7Tp6kPhhSQg1dIqZ9Uf-SsNE9dxvcpzQxjGkv0EqtBNW17mhC2BEJYE9VsmsTf04dMqZ6h9PZbOxcwKwfIbl7tLvIZODvr6QX_y7nSJN7X1XVssr8vnibtSTemYOu61SJ109MmwzZVmGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلیمانی وکیل علیرضا بیرانوند امروز صبح بعد از کلی رایزنی باعث شد که سربازی‌ این گلر تا اوایل آذرماه به تعویق‌بیفته. او به بیرو قول داده که تا آذر ماهی راهی برای معافیت کامل او پیدا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/30477" target="_blank">📅 14:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30476">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USHWxtuDroylHAab6NSFB4VhXb1OsJCRfS9t6a6IbqulKh-Fg1FgsSyMnFw21S2ck9FF6DFVEskSURZHYq8A70xGHPr_NMBUYyCFZj34KSF3YV6cdVWLrEvM9sHJ17yKlZmevWzT1rWiCwyril7mRZQdWY8vrHtp-qBFnXz3gmpx8C-6txdhHusTFb5s_xNhb_z7EopZduN1RvBXVafFnl7Ow6nRqtWzRDs9TMeWBIhkklkvb_EwJsMO9mpDIx7aERDiRy2N_UZzVv1zBkNJF2HLLmc0lig5DUB3oZUHmU9aFy075HNBdNM1LEP6LTlsheUKGlkoR9tgxTGHHJX7uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کول‌پالمرستاره24ساله‌چلسی:
خیلی دوست دارم که یه روزی درآینده نزدیک شاگرد ژوزه مورینیو شوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/30476" target="_blank">📅 14:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30475">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">📌
قیمت روز خودرو/جهش قیمت خودروهای مونتاژی در بازار امروز
💢
آخرین بروزرسانی قیمت خودروهای پرفروش پلاک ملی طبق استعلام از نمایشگاهداران و دفاتر فروش خودرو تهران،/ ۴ مهر ۱۴۰۵
⭕️
این رسانه هیچ نقشی در تعیین قیمتها ندارد، بلکه صرفا اعلام کننده قیمتهای کف بازار…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/30475" target="_blank">📅 14:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30474">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/am0fX_DxTTim3BLMVjZbIDs49BPC8NuKtVUTO1zcJdQeZwRG-RLR2wSorSGhbs6LvDnq6vWWopZeb6qf0rriaRvS7RAYyoflgD3-o_5P9y0H-910-DBu-hFHFqYBlg6dZct8JfF476J4yDZIvxZEWOf7gNT_jCqlfvZyyR6xdBmzLeJeOKmyBnP1wCx2LzDXsBLQLSL9UdTLglRDRZ_Dpx45NphQAnmvisgEjryipBlpyzRV58E4fxpb6YKz9_IZ70MHKxlKeJhd1YJFZx29USrwMPD6GGwzZgysVRSL2pA-ATNyd2Pk6a82tj71DTZArMOrFmEnrmjyvZiEXxW8Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برسی کامل‌ودقیق سیزده سال ناکامی امیر قلعه‌نویی سرمربی تیم ملی در رقابت های ملی وباشگاهی؛ وقت بازنشستگی فرا رسیده ژنرال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/30474" target="_blank">📅 13:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30473">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIa9rh6lgi_pWyaG6Uyj4_QnDD_eI77fV7uX8ZOBAkeH59HBY1TaG26rvOj0BUEVzAbrs0sTdsXFSCPKEjLK3kF1_r0NTD6NYcLjffLBhxbi7_kOY2t0peD_iONnjmpdlahKPA6idDcu_T_j--E0XFKax76eWO9ao6mgFVztSCR3LnGmxDfW2rT6aIJz8TDqFiafMkjNa-QTFqHP7qF_RPfOIRp1IQtIPNCGSqCtYdwkRprrpHD3r0HRo0Ttzcay9DeuzN37VMJLFC8K57zZeX43RSAvHq9hOPdwVJMh1Dfu9BXc95sQ1cO6I3hBxbkwQWhhBsdV6qLmvH0zYaKvLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🟡
#نقل‌انتقالات|فلورین‌‌ پلاتنبرگ: جیدون سانچو ستاره‌انگلیسی منچستریونایتد درآستانه عقد قرارداد و بازگشت‌دوباره به تیم دورتموند قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/30473" target="_blank">📅 13:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30472">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63e94cf509.mp4?token=EC-ukQASjMSnl-YEtKsh9kSvyH0rsgNXpt3bVj8jQw3wf9oDX95HcXeLm42GjxMUDmBGWZtVWULNZCGYZ-sPbhXSzwXuBqRtLom_VP1ihDryw0oJ9wsm02z7qf_GOt4mcmY7k3CM_piKT5QVQfmwaudY857BNznz7Cq95zAY-WNh1XQv1YPXOad0VtemlqzoIPGeJRitVbjx7TaMsQFZdFepZFKtkh_W3Bg5xfRar7nkNo57IKAun7mGjE6s0RUl5ZyagAQWKCJLXjCfczBWHuCafigSLiz_oY6ArkgejbdbfUiznqLcx6nMSX_MMrETGdIp0wODXC6Qo6Yo7YZboRIvSxsZxpaIPjBamyzn-A-91KLqFxLWRpcUKN05_KURDU_4nSfsd7ldZJIVJ6_9wlHzap_ctiuyL23UN2wxTv2Ed67jBZJef-HDioJo0ePU4DJDPTZqsh2OcQVqTzUHakAjgQoClkAFMliNMd-F6GNJi38IEqnpaWQzGTU0K1oblOrTcb7uk6u9Xp61Kz-2mFbXQafylj_0icoaoEVL8iOYTMaxc_G1SpSZNIzjZDkU4fMJ9RoOTY-jBdeu72iISAgj96hWXk0el7q8GDxT-y9fKsqL8P85WfTV7CuArOGSd6T9jKsB4_hmP0YgNdx5rE0BGDI6voUGMJ7VvcTBt9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63e94cf509.mp4?token=EC-ukQASjMSnl-YEtKsh9kSvyH0rsgNXpt3bVj8jQw3wf9oDX95HcXeLm42GjxMUDmBGWZtVWULNZCGYZ-sPbhXSzwXuBqRtLom_VP1ihDryw0oJ9wsm02z7qf_GOt4mcmY7k3CM_piKT5QVQfmwaudY857BNznz7Cq95zAY-WNh1XQv1YPXOad0VtemlqzoIPGeJRitVbjx7TaMsQFZdFepZFKtkh_W3Bg5xfRar7nkNo57IKAun7mGjE6s0RUl5ZyagAQWKCJLXjCfczBWHuCafigSLiz_oY6ArkgejbdbfUiznqLcx6nMSX_MMrETGdIp0wODXC6Qo6Yo7YZboRIvSxsZxpaIPjBamyzn-A-91KLqFxLWRpcUKN05_KURDU_4nSfsd7ldZJIVJ6_9wlHzap_ctiuyL23UN2wxTv2Ed67jBZJef-HDioJo0ePU4DJDPTZqsh2OcQVqTzUHakAjgQoClkAFMliNMd-F6GNJi38IEqnpaWQzGTU0K1oblOrTcb7uk6u9Xp61Kz-2mFbXQafylj_0icoaoEVL8iOYTMaxc_G1SpSZNIzjZDkU4fMJ9RoOTY-jBdeu72iISAgj96hWXk0el7q8GDxT-y9fKsqL8P85WfTV7CuArOGSd6T9jKsB4_hmP0YgNdx5rE0BGDI6voUGMJ7VvcTBt9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناراحتی آردا گولر ستاره ترکیه‌ای رئال مادرید از مصدومیت کیلیان امباپه در جریان بازی شب گذشته دو تیم ملی ترکیه - فرانسه در لیگ ملت‌های اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/30472" target="_blank">📅 13:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30471">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3tDiZ7DZfL-anynF8tZhoQdDnVfoJTZ1nM5SSf5HrDlb4fproAf_eGH3qv918u2KP4jvb-89TJEkq9Xha7odFqNMtXkkUinLVBKlUa8ZWIO4aXP5E0EbmmnvWlZ9MO76QerQ6ud6jjs_veF36GVHuWr6Crh-FMGSi_PqZzDFRe9hz4Yc3n-wIzj__ZzCe9hEyXO9i1Kfx2pT-UA-wLj1k7qKM1F_RPXror26GA3EIoc97wMOm6I8ir2_LkO1hp4MiWP-JcNlXtGNJ9lxfwQ3H1mMJQ2uRwDAbxhqliMDY_Q3aI2ZIKTSHnpczrW_fTSJrg5vVMd18ZcnX2tiIlkUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درصورتی که اتهاماتی که به من سیتی زده شده ثابت بشه جام‌هایی که در لیگ گرفته به این صورت بین این باشگاه‌ها تقسیم میشه: منچستریونایتد سه قهرمانی، لیورپول 3 قهرمانی، آرسنال 2 قهرمانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/30471" target="_blank">📅 12:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30470">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWI77XTPzH9cMwdPZR5wNUyIK1lWal3oK3QYs5c7zMRlEWYA41XvwyKsyPCqXEdU4fOYgD4HNG3GwAUJs-WeeY_atx2OmqGzz2tkgr2cWeX-z-YxI5LhDqeOebOrSlY8_LQY8I82Oltyf2nSPdu6jhZb0I-_hhKF-TuT08ruPWmke3TNUtReE54wwYUyF0rd_hRaCfaSE6zp1qbG9ewgnrlNbn1stUGLhgqf5770ePM12PMb0NkHMMt-2nb8Xdo1Dc60wzyhWgoPWg_eGccmYYoK5CIp9IgJIcahdxmOClWHO_GlECa8PV-gh8v6tFY9aNzKRCXBCH5mODAEAba26A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇹🇷
باشگاه رئال مادرید برای تمدید قرارداد آردا گولر ستاره ترکیه‌ای‌خود تاسال2032 به توافق کامل رسیدند و فوق ستاره به زودی قرار دادش رو تمدید میکنه. پرز دستمزد آردا رو حسابی بالا برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/30470" target="_blank">📅 12:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30469">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWbo9fcojbNGxB0XZ_ub-OAhJoRRO_FfzhGVu8ott5-ByX0vOUUPMvCr94iXH4KlieWNp-izmRG0mEuXOW6VVJMNLumwBbzYGZf7Vs9ZAWhbwCSX8JwoWz-Omsadg1bRqMlCHhymiVo85teK9GCUk24_Gvo2TKLFqJI0vrTe0Lai3FHE7eZyqQ99KeDpC87sKBG3NKYG_-zvMsLqchdfS42JAEAYaQc4Aknbf46tKirrDXEex42uPwBXhS9vuYuTNAkMVGREqTmECVr_lxbrJC9Tn0qdTvF1anypn8L4-Pxw00fuX1JaCdzxVWx3NTyrimUlZ8fJbP3KDNzNgvBuow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
شوک‌جدیدفیفادی به مورینیو و رئالی‌ها؛ در فاصله یک ماه تا دیدار حساس با بارسا؛ کیلیان امباپه فوق‌ستاره رئال مادرید در دیدار امشب خروس ها از ناحیه‌کشاله‌ران مصدوم‌شد و زمین بازی رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/30469" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30468">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4b13e0d2.mp4?token=HOnyAVdNRktEj0azqwZT0qqOXFIAarlKq1UKTcllNTg0M1XC-9M_6L_bODCBE4jEXuUAgGGBg5jvVH7bvL232pKrFDV-kZ2vdMAHNRx1mAZNa59Fucmg51rvssr8cAcprA_tT6yZB1z0yk9WtjBrTscsO2jLSvvnusEhu7KNt_s23Ze5-fGx4GAZ85evZeGdQ8tOwW109qYcFhO4FCjj18NVBFHtfeixteDLb-hRiPw9-6HzkCtFat-uKIdEMV3mE0fCQwISRjPEeTQ0GzJOQG5I04WNaQvpY4sF2LS6lPZ-UtRavhiqyZHqJlJ6BU3mEZEGYTjjOO2fsi7RvcXDzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4b13e0d2.mp4?token=HOnyAVdNRktEj0azqwZT0qqOXFIAarlKq1UKTcllNTg0M1XC-9M_6L_bODCBE4jEXuUAgGGBg5jvVH7bvL232pKrFDV-kZ2vdMAHNRx1mAZNa59Fucmg51rvssr8cAcprA_tT6yZB1z0yk9WtjBrTscsO2jLSvvnusEhu7KNt_s23Ze5-fGx4GAZ85evZeGdQ8tOwW109qYcFhO4FCjj18NVBFHtfeixteDLb-hRiPw9-6HzkCtFat-uKIdEMV3mE0fCQwISRjPEeTQ0GzJOQG5I04WNaQvpY4sF2LS6lPZ-UtRavhiqyZHqJlJ6BU3mEZEGYTjjOO2fsi7RvcXDzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
تعداد از کاشته‌ های استثنایی کریس رونالدو فوق‌ستاره‌پرتغالی در دوران‌حضور درمنچستر و رئال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/30468" target="_blank">📅 11:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30467">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c87985ff1a.mp4?token=slWFqzdcI6z2_0EShEfBdgWJYY6Lid7LGkHRc70pV6InPcf0KYsxzYj0dJzgLGz_sW1CUTytbfKBqUCA9rqWHJWzPymtunb8fxaDiW9sOIn6wKlev4b0ZW7uPbGp8cmEtkCyyps4sArTBrHzzRG9y3QNUjNu55oRnAKwpsga5F_tlEY0rVGpWKyOJE7SIi023CvUvGZPT_RAAzS3lghXeS1jZm1h3ERDf_ZhHy1GjDpP5zN-6zgVzjm20q4jJgBiY0AXBPq63I6rFtaiCSo2twECH068rw-TbCn9xkrQUy8RvVnDVomL4pWpGdW3OWQj3J-5JnmfOySZTGxAjXIbYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c87985ff1a.mp4?token=slWFqzdcI6z2_0EShEfBdgWJYY6Lid7LGkHRc70pV6InPcf0KYsxzYj0dJzgLGz_sW1CUTytbfKBqUCA9rqWHJWzPymtunb8fxaDiW9sOIn6wKlev4b0ZW7uPbGp8cmEtkCyyps4sArTBrHzzRG9y3QNUjNu55oRnAKwpsga5F_tlEY0rVGpWKyOJE7SIi023CvUvGZPT_RAAzS3lghXeS1jZm1h3ERDf_ZhHy1GjDpP5zN-6zgVzjm20q4jJgBiY0AXBPq63I6rFtaiCSo2twECH068rw-TbCn9xkrQUy8RvVnDVomL4pWpGdW3OWQj3J-5JnmfOySZTGxAjXIbYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
چهارده‌مهرماه شاید یکی از آخرین شب‌هایی باشدکه مسی را باپیراهن‌آرژانتین می‌بینیم. شماره ۱۰ بعدِسال‌هاافتخار، جام و خاطره، حالا به‌آخرین فصل‌ های دوران فوتبالی‌اش‌نزدیک‌شده؛ جایی‌که شاید هر بازی، آخرین قاب از حضور او در زمین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/30467" target="_blank">📅 11:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30464">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60d4945a7.mp4?token=VYVnIE0GdBzAQJszV-NEmd3T8drTENTasLg89ZT-5zEUBSbrDjcKrZoj3w5rxYNIczsQK6H6NmxqhDCQHeGDewcmR8SY1U8wHu4v5TOmvbrCwizD8ygo-zKDPWqsS3cp04DM2Kc1S9c8LNyVuaayrAMODKzfW8dkQzRe8ypLv23vixsqXXlq-SWam_VHqFFPBZDZvykSAa_TnkDHG_WwIb33N3EvJFc4X3ae70bOPfKRyIXpbPukiKgQOu4zlmF_QaliD2jYO-vUcVyETKR9vkrvaGoY_HZZ1shnWc2GPTb25gOqLE3y4I-Zr89P28EOGzw60ziKxcwXK09Ms9ICfSx1qPcakrLqllo4HAqv1nBWrcjQTWitaF9Cj5AgqSqpCYX0tcvN9ArdEBoTthba_YKaVK5E1EV1ytGam5wWv-tlnFBGCUeIVxXD1k-I6kbepteUGueys6Tbna-KJ2vHOnp1yejFmh73A1ko6hbJSPg8LOpYG1gKvPcUyhITZaBKszqt_dAXevo4pY_mly0upnSKnYEE7_K9Cnm8vnt9ih7gQR8ZdhLio_n_uFX9xQJpOaOS5jOtDj_rhc2xj2GDXU1GRi63JAosCpeY5NoPJ8vDJ_NyUsWrKcJ41MOAbVmlq1eSfnU-0Ntu2lr0-aPEHRaNpQEDfgB35Y2RvFDM30c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60d4945a7.mp4?token=VYVnIE0GdBzAQJszV-NEmd3T8drTENTasLg89ZT-5zEUBSbrDjcKrZoj3w5rxYNIczsQK6H6NmxqhDCQHeGDewcmR8SY1U8wHu4v5TOmvbrCwizD8ygo-zKDPWqsS3cp04DM2Kc1S9c8LNyVuaayrAMODKzfW8dkQzRe8ypLv23vixsqXXlq-SWam_VHqFFPBZDZvykSAa_TnkDHG_WwIb33N3EvJFc4X3ae70bOPfKRyIXpbPukiKgQOu4zlmF_QaliD2jYO-vUcVyETKR9vkrvaGoY_HZZ1shnWc2GPTb25gOqLE3y4I-Zr89P28EOGzw60ziKxcwXK09Ms9ICfSx1qPcakrLqllo4HAqv1nBWrcjQTWitaF9Cj5AgqSqpCYX0tcvN9ArdEBoTthba_YKaVK5E1EV1ytGam5wWv-tlnFBGCUeIVxXD1k-I6kbepteUGueys6Tbna-KJ2vHOnp1yejFmh73A1ko6hbJSPg8LOpYG1gKvPcUyhITZaBKszqt_dAXevo4pY_mly0upnSKnYEE7_K9Cnm8vnt9ih7gQR8ZdhLio_n_uFX9xQJpOaOS5jOtDj_rhc2xj2GDXU1GRi63JAosCpeY5NoPJ8vDJ_NyUsWrKcJ41MOAbVmlq1eSfnU-0Ntu2lr0-aPEHRaNpQEDfgB35Y2RvFDM30c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعدادی از گل‌های کیلیان امباپه برای رئال مادرید در دو فصل گذشته بعد از پیوستن به به این باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/30464" target="_blank">📅 11:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30462">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KoQIDkzcTAB5A3Ezn4z_od1C92uvyQhvk2gqFUgH_NACKu8-A89KXj0ImZT1xv0dDtkuzurl8Y5NaFB-sRse1yxUR2Z0-ELdz7xyiiz7cMl38cFFuzNv6mzwm9Y7LHCkovpOtY-hinrCgxF-Sm7anjfLOSyapbGkuNVnTEJuIsARHJlO7-j8C2empbpRBQeKC4KM3c87n5Lrj9IjKePTH34hzwE9zDCjLZ57kcZmcqYzuRyjQ7iNtEEwvyu-3AFL_m61-2ucv4mvUieGzJ5yreLQdRIxCktE63hyVeZaQR0K6EaC2XEeYxhEj3Fhl8p9T2w3FX1ejCezMM2csDcM7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0TplsJ27ZIn23ScXfZ9FirUCYIUBRJgzftVAViqKRGYG6Frt5bUJDRSh2Z0YPWfBpMzq9KdFpLkZvh3AR54JHMJXJu3xVv7bII3ilefxGu2zYItGi8K-2x4uehZ_NCVJmVaunhjUywEmUh-OE4iBDIfxS01ZHSEYdtKKyrmNOpA6LP4y0pqRmxEqFDx-agKQ7L8BXQs4CGbTjcX-vx5NvF8Utkl5Na3wvE7AHeVBuwjc7vjJh1I6--V2efPCsSxDrU08C4Hkhh-qJAmEWUbzPUcgQIc3FoMo1G-fs6FH1dZiaJBEAshyozgsSGYrE_4mcnUWsICLZ9eb1-ImnN1NA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
برسی کامل‌ودقیق سیزده سال ناکامی امیر قلعه‌نویی سرمربی تیم ملی در رقابت های ملی وباشگاهی؛ وقت بازنشستگی فرا رسیده ژنرال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/30462" target="_blank">📅 11:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30461">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌استقلال تاپایان‌هفته جاری 400 هزاردلار به فابیو کاریله پرداخت‌خواهد کرد و پرونده این سرمربی درفیفا بسته خواهد شد. نظری جویباری پیش از عقدقرارداد با ساپینتو با این سرمربی برزیلی قرارداد امضا کرده بود و حالا بدون اینکه پاش رو تو خاک‌ ایران…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/30461" target="_blank">📅 10:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30459">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6160de2528.mp4?token=mlCJTdAUnTy7YnsTuQQS5aEe7RImq9cnKvhmcsQFmuMR3SWuOdwfhXmEkIa1r86XKA3OEsINQkQPCImIwxegwuKjXoFbqFJZdxgLq6M2RCsGx3N0mONTMfA1MP7hBQsC9lVvmcLg6pVxjadpKn8atXT3NfWC78SDeUbkAQRR1c5N5l1Sfc2kfLcEEVV8IMItQ5YNR4LlVSfbUbqrWJdr6_3rJ-yZIbqyJUf_wVWGQ1OtVaiYwwN_UoqQjg9CCYeCSVauTJRZFi9CABdXdWd9KS9V_-VEFiDKwm3yVf1jjZw_GZV0Ocr9VoJqGjYfKJuuffq7wpMv-FT8w5EOxIxsBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6160de2528.mp4?token=mlCJTdAUnTy7YnsTuQQS5aEe7RImq9cnKvhmcsQFmuMR3SWuOdwfhXmEkIa1r86XKA3OEsINQkQPCImIwxegwuKjXoFbqFJZdxgLq6M2RCsGx3N0mONTMfA1MP7hBQsC9lVvmcLg6pVxjadpKn8atXT3NfWC78SDeUbkAQRR1c5N5l1Sfc2kfLcEEVV8IMItQ5YNR4LlVSfbUbqrWJdr6_3rJ-yZIbqyJUf_wVWGQ1OtVaiYwwN_UoqQjg9CCYeCSVauTJRZFi9CABdXdWd9KS9V_-VEFiDKwm3yVf1jjZw_GZV0Ocr9VoJqGjYfKJuuffq7wpMv-FT8w5EOxIxsBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آلیشالمن بازیکن‌تیم‌بانوان‌کوموایتالیا با انجام این فری‌ استایل در اینستاگرام کریسمس رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/30459" target="_blank">📅 10:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30458">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT2vXESX6hIBByGJNd95TeErOTTcmiNKU3E0AuzuL4zjj6tQuV28jIpsroM8FY3OA4cSAKTIl3QX-jnLzKEt3IiFbIYY_6jH9hrakpfzPXIisee7YMufIiZ2AYO1Qo5DkGZBaNvJqj8KGQjzO6mvGmlGDdL5RawOoR5hJN_a_ou-e8uJTmSiqg3m5xIu3QOvxqM2eNYqxjdd7hlvNFT-_SDOC7JXl_3lfPr4fj5TamHeto02KT5tfG0YVlrp2gfkuQVS1OHFMfI7XB7Z9cAEw63T4k-vIX23eg2hvAPsol4sg3SFV0O6zswvH96c0aaUpiUWm17mNPlYkuSLy6Gxzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال مذاکرات مثبتی با فابیو کاریله برای تسویه حساب و بسته‌شدن‌پرونده او پیش از شکایت به فیفا داشته و بزودی با پرداختی مبلغی این پرونده بسته میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/30458" target="_blank">📅 10:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30457">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLxhnGwp036NgmvRXDacvaZGdgIt73PCaRmFA_VNge7yXRrmR6TmYzHo1jk5Qcrl0g0iVF8jDu0inv9UwiCdScd8YVO_-0MQFwhwcYtJ0eGvSBw-phK4Cye3Zczm-tSsR-GarWDdOoaJWzFOuvJWvXIO8pQ6-kXY-aAHsongQecHXZLbLfmy1BngKoJH8iYBfFGgV4lzmHsoCXQPb8dg7JCI7eUl8PTOrKKt9Me16hXsn78LdFj9WG2Dh43fLDDYEYXEhRRhOA5rE5kxmDpqSw_q9S2C3JkXBMQdb_JbBp1oL4N4n5B9TGu79vAHWhi0qAmQVUz7N6p1PjD1XoHOnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درصورتی که اتهاماتی که به من سیتی زده شده ثابت بشه جام‌هایی که در لیگ گرفته به این صورت بین این باشگاه‌ها تقسیم میشه: منچستریونایتد سه قهرمانی، لیورپول 3 قهرمانی، آرسنال 2 قهرمانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/30457" target="_blank">📅 10:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30456">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/30456" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
جدید ترین نسخه
اپلیکیشن بدون فیلتر wepari
ثبت نام آسان
✅
📝
🖥
رابط کاربری راحت و سریع
📲
کاملترین برنامه موبایل
🇪🇸
اسپانسر رسمی لالیگا و یوونتوس
🇮🇹
🎁
بانس 100درصدی  اولین واریز
💵
Promo Code
:
sport100</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/30456" target="_blank">📅 10:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30455">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPepFWcOaVkU6spaqFmB159X3LtsYyVmUgHPFGpzWVQ9hguiFlMvGqJRvHIuU8lRF667bmTWuD3jIdXdTfs8dusW4AdhahkwZ7rWAKs1PSGUXy9QdHf0c54gIFcdUJbLzqYAz9IlMJv29HK6W2oIDgLtQEYdaiYbL1Q2IWS5pwLQRV48_Zf9QL2BeSHTJ2RYWCmHdsi37b5siEwX_hBZ3naC6gvgTmXLKHaMVgeQbCadXwmyQOdGHtrnyXMUS5etNCSNvB_dbTHMzNiK2oGw_hcbiKDInfqi-JTWdiroFQxUkgardcoyccOdn6YhRZDhiM1v-rSPdPOchUhgL_FGzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
بازی های مهم امروز را با آپشن های تخصصی
در
wepari
پیشبینی کنید
👍
💵
امکان شارژ یو ووچر پرمیوم ووچر_ترون تتر درگاه مستقیم بانکی و...
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🎁
بونوس ۱۰۰ درصدی اولین واریز
🎁
هر یکشنبه تا سقف ۱۰۰ دلار بونوس هدیه دریافت کنید
📱
کاملترین برنامه موبایل
🇮🇷
پشتیبانی از زبان فارسی
‼️
لیمیت نکردن اعضا در هر شرایطی
برای ورود به سایت
فیلترشکن
خود را
خاموش
کنید!
🔑
❤️
🖥
Wepari.com
🖥
Wepari.com</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/30455" target="_blank">📅 10:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30454">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f59d54b38.mp4?token=lymRA_YQKC8WaRZR9j5fTNxtnWaM6qAV3S2ddM7yLuwokUOvh-e3fQpyrioW2h5Drt9ZmiDtgRR01jNMoXWSlQy9Qp-VXak-6Nw7Qhj0skPdvR_CNl30z6WEVRRliXo_vpd0lqDwa6nM6Ecs7qNR8XhDcZYH9WSIUz8r5M2NgMcWhPV2FAAN5tiJ2qR-KkViJS6HnTugSZIPOrKkaVXo2yOQIkTYHcmjNz5zHCIeUVvkheUow45Lb3CAzlPCEI36aDScgUK1UxZ_bJSsO-RqNTd4_lfiPURrjgVytnaMJ5_2OWwJtZmS6xZ5u836sPNgfYf0cODlEY9fSS6tCW3AqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f59d54b38.mp4?token=lymRA_YQKC8WaRZR9j5fTNxtnWaM6qAV3S2ddM7yLuwokUOvh-e3fQpyrioW2h5Drt9ZmiDtgRR01jNMoXWSlQy9Qp-VXak-6Nw7Qhj0skPdvR_CNl30z6WEVRRliXo_vpd0lqDwa6nM6Ecs7qNR8XhDcZYH9WSIUz8r5M2NgMcWhPV2FAAN5tiJ2qR-KkViJS6HnTugSZIPOrKkaVXo2yOQIkTYHcmjNz5zHCIeUVvkheUow45Lb3CAzlPCEI36aDScgUK1UxZ_bJSsO-RqNTd4_lfiPURrjgVytnaMJ5_2OWwJtZmS6xZ5u836sPNgfYf0cODlEY9fSS6tCW3AqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مورگان راجرز ستاره انگلیسی تیم چلسی:
کریستیانو رونالدو بازیکن مورد علاقه منه اما من در نیمه‌ نهایی جام‌ جهانی در برابر لیونل مسی ۳۹ ساله بازی کردم و باور نکردنی بود، تصور کن در دوران اوجش چی بوده، نمیشد در برابرش کاری کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/30454" target="_blank">📅 10:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30453">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b295745c6b.mp4?token=MN6TORNuE4dlB_jK2iVS0Jk1qKZbVhSfulmCgL94ge0Brp1pwSb8JZQrPKfOG2IpeJAarIB5X-mtC77CiJY5cVFzflLip7AqFTPEMsZtk9A0TclVtvPHiK3U8sc7ErfXDwh3Lxj0Lmsh1xd5Gw-BGsyw7Z3Vo8OFdUoEPhRBrW2DtkmxH01iAv47vpDsrNQRjQRdfsu3cztw6QprS07rKSBh5QvGnd-3kvw9i_uhxgrzj2fwzxBxtzJ29mwPU3KfdOM4AtmwSoA-9ZAaDQXie3FrecGP2wCccfMY5jSg1mFNL2A5j_jTLJxyHl1GtektcAwk97iT9qkl2ZHkRJ-FZbccz2WS_RgUEN1PHbWG6aLxRYVYxSosdl0CD9Dvom8RuQU_RaLtBXZwKXLN15fhAqU2_Grti4G-s4zdhOnYhGhGliB7b18iRVpdE8LjjtvPo43arpRIRvCjN_NCPV4f0hgAmFI1mj5Zv9tVWPVO2lWhm1gWlPUF4j9jz6znsBHV2dYN5No_b0zuNP7Ph-NcZ73RCEw7c9Jh89VEVqpUO-xXTGMUzy7IdqX-LDTTx4K1v9DN6c5dwESd2w0E3sSBMJ5NfWQi5nRh1I_8EgbEUebgFNlesQQrihTlaXhfk-Sn_O3YT35aPzQj3RDDxwePV3YIRvW0KnHUnn2mgPzsxbE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b295745c6b.mp4?token=MN6TORNuE4dlB_jK2iVS0Jk1qKZbVhSfulmCgL94ge0Brp1pwSb8JZQrPKfOG2IpeJAarIB5X-mtC77CiJY5cVFzflLip7AqFTPEMsZtk9A0TclVtvPHiK3U8sc7ErfXDwh3Lxj0Lmsh1xd5Gw-BGsyw7Z3Vo8OFdUoEPhRBrW2DtkmxH01iAv47vpDsrNQRjQRdfsu3cztw6QprS07rKSBh5QvGnd-3kvw9i_uhxgrzj2fwzxBxtzJ29mwPU3KfdOM4AtmwSoA-9ZAaDQXie3FrecGP2wCccfMY5jSg1mFNL2A5j_jTLJxyHl1GtektcAwk97iT9qkl2ZHkRJ-FZbccz2WS_RgUEN1PHbWG6aLxRYVYxSosdl0CD9Dvom8RuQU_RaLtBXZwKXLN15fhAqU2_Grti4G-s4zdhOnYhGhGliB7b18iRVpdE8LjjtvPo43arpRIRvCjN_NCPV4f0hgAmFI1mj5Zv9tVWPVO2lWhm1gWlPUF4j9jz6znsBHV2dYN5No_b0zuNP7Ph-NcZ73RCEw7c9Jh89VEVqpUO-xXTGMUzy7IdqX-LDTTx4K1v9DN6c5dwESd2w0E3sSBMJ5NfWQi5nRh1I_8EgbEUebgFNlesQQrihTlaXhfk-Sn_O3YT35aPzQj3RDDxwePV3YIRvW0KnHUnn2mgPzsxbE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از این چالش عبور توپ از اشیا؛
هیچ کدومشون نتونستن کامل توپ رو رد کنند تا بالاخره نوبت به اسطوره تاریخ باشگاه رئال مادرید رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/30453" target="_blank">📅 09:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30452">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2a1eTBc3aiIraHuFolu6AbsxjPBQWxx6Y2cE_FBEPDpp5YiZbeNzj0q6O6tUpYrFIcXMvxh3OtjWXqxhke6aoOA9gvB5y6E-6E3ZgbLUPLWGKVPWI3mtWSBzt17gXfnQw74tcZ6BF3WDk8PFqxe1khPm4SAiwihrXkPGfZMoxgjjW6pcDSw-VZWr2vp-0GbZrYycYzEc44344_1Q1G9Z8qr7wldBJV1Q6r-2qNpj9As72Zu6-qDTvK-T6gZstgcfUVz2KGACCcDQmAr7S9M4MHV70Gvk6BVT6Fg6zZlYT4MJKFWFAA97ZClOD9T2HlXH0XVdrZKTD-xZNbg0aHAPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
#تکمیلی؛ بااعلام‌فدراسیون فوتبال فرانسه؛ مصدومیت کیلیان امباپه از ناحیه زانو هست و بدلیل جدی بودن مصدومیت امباپه، او بزودی به مادرید باز خواهد گشت تا روند درمانش آغاز شود. گفته میشود امباپه حدود 3 ماه دور از میادین فوتبال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/30452" target="_blank">📅 09:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30451">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUnKDDO-_jn13tsiJ3e5WWwkNEFLeACusF58K9QgpjP5tI_zgxRoNE7xcIxVubdLJyQ2nnmrLGO7z93vcmclrURKQwsTbEf3VcQNjtmbBS6fkjgdhwt-8pLIjtpY4aB2VGiys6Od2H8SbZp7_uPxHyPBbqmUeruhOOSimf9iNlgILt0QMd15e-N3NpQMcU0Jw17Pj3Gk3Jh0cXNQ-xIuMwda5a96pXbAaUs5FmPlFHZylWtmAInedzljCL0dwWspznRD-vI46FJpnoxWhA5uEOVj2cOH943lyYchhZ3rFnMZUqbVASiV_f_P0o0QvzSaleNfNvTZAComcuWMKBCb9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
رسانه‌ های بارسایی در حال مانور دادن خبر انتقال ارلینگ‌هالند به‌بارسا درتابستون سال بعد هستن و قصد دارند بافشار به‌مدیریت این انتقال در تابستون 2027 نهایی شود. از نگاه اونا پرونده انتقال آلوارز به بارسا تموم شده و این انتقال هرگز رخ نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/30451" target="_blank">📅 09:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30450">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CS9-Pz7bqzOvju75GxKYXhJeXg_fg_PAcpvcwDEXz2-GrpmsfX4hXz8j9dGzlRYsi8lfxBuVSUKQGoNlJ5gEcqqFfIoWnHTT53Snv6-GwVCSPZwjiHPiXEq0gJonmYPFB8uQl-etZfDVBnvry6v1pH3FD3GGWRqM4Hvc6qivHv3-pIk4oF3KzpBAV0Z7NJmTT8MAd2qCM-3nruJRuRkGLFZNYthPgeJHD6N5BfU5I4iPDAt5HZLWfs6NJa52UeUqWce2CWY2giyuRU7ME553nct8DcijvzL2E4gf50VAoDXvipRu4WGORwQPP-VslnewmOswkwDSACrqz0essRwvHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
شوک‌جدیدفیفادی به مورینیو و رئالی‌ها؛ در فاصله یک ماه تا دیدار حساس با بارسا؛ کیلیان امباپه فوق‌ستاره رئال مادرید در دیدار امشب خروس ها از ناحیه‌کشاله‌ران مصدوم‌شد و زمین بازی رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30450" target="_blank">📅 01:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30449">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34b91abd7e.mp4?token=XYCzFuGxjjkYcSL7rxD2MVCvyaICf11BfCgwcuV4PCgar_ew9LP8jMT7L91L4y3Jqn7_2vlHf-1WuF287HTEhF18OG6wNn11EfaCk_ZmAaJOb-XVGWdXgO35W2c1ZKRQT-4geA2QnbtSFJRG1hFORwlrvJ2-yRAVAV32rxc4-zl5triWY4sxQlRD90ifxCdqs5aAWFWzUbh-vaAOJQTH-3LwmlXYWF1FXXK0zV6_RnxHz15bVuvLJk5sh0TEG5lpWwADOeZEc5IieQgoo7X3mtsYa_7egLxzrWvvmT-JEzaoLt0IFuOnUbbUrqpFSiTiJUNOw9WweQgysxFdv67zWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34b91abd7e.mp4?token=XYCzFuGxjjkYcSL7rxD2MVCvyaICf11BfCgwcuV4PCgar_ew9LP8jMT7L91L4y3Jqn7_2vlHf-1WuF287HTEhF18OG6wNn11EfaCk_ZmAaJOb-XVGWdXgO35W2c1ZKRQT-4geA2QnbtSFJRG1hFORwlrvJ2-yRAVAV32rxc4-zl5triWY4sxQlRD90ifxCdqs5aAWFWzUbh-vaAOJQTH-3LwmlXYWF1FXXK0zV6_RnxHz15bVuvLJk5sh0TEG5lpWwADOeZEc5IieQgoo7X3mtsYa_7egLxzrWvvmT-JEzaoLt0IFuOnUbbUrqpFSiTiJUNOw9WweQgysxFdv67zWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش بازیکن شماره سه تیم ملی کبدی بانوان ایران بعد این اتفاق خیلی خوبه. اول برگاش ریخت بعدش رفت ازش عذر خواهی کرد بلندش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30449" target="_blank">📅 01:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30448">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDWNJ1TInT5TNsAIh8nVQV1344v43w9kWurgBLbRmx8DQ7KseZKjdO9g5O1UiAOB3KNH2jsllrQWTB9oniqFPP10D6RkJYK3rws-GteApKbe8QW3GDMAVF-T4jRnAJIwY-FgHYbGIE0onXUpchuw_gbaZ7givBbKzi2hR21UqbK-C177lzUJcuTJbJpnRwuMduwILMwRYRmLnjTmWPmmUuM36vDQbnrTUOHu4cAXw4Qwem_G3aArBT7snZfoU4DvF-QDK97LlUG0USQkrSBZvsAJX9rWXjANxRVnhASHhwFZtmcEJYD6ON1bRhdjEuc4KPKkSWma2pGXSRJtLo80Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛تاکیدچندین‌باره سهراب بختیاری‌زاده به مدیریت باشگاه استقلال: بین مامه تیام و فابیو آبرئو یکی رو در نقل و انتقالات نیم فصل جذب کنید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30448" target="_blank">📅 01:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30447">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWc4vcKNxiJqjoRVlU4JroPPdjBqYDvGV-wM3ZureU3Tia66qrhpjMrE2wS2FfiPsM0T7q6-z8VfGeffWpPkXRaR58IPNBnIYkOmrwwxBGSl-Kaa2pJvMRzL7OEBIFbD8p5phQdQHwwFZo0wHfD44nbsKIPfjTgWowzS5hfUMdT_BZqJIrtRbcCuDAdqCdTKGBLAHHBqdpGSQ65keRheEiWLKEBKrUb1MMnJHxSIBSXPuAhzhjFYoS2xZEz2GNETWGxz6ZhYiFqYWRsm6XDTo9534NuI8j5AsKlqKyZ1rcaTDB4x_xstfeaLMeza1TPiUYH021NWAo597MTtChs71g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ تکرار فینال یورو 2024 با تقابل تماشایی یاران هری‌کین و یامال در ومبلی لندن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30447" target="_blank">📅 01:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30446">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jj4Uz6NLyT9QBIghdlOdLHZoCKa9CSy8of5jKMFeQt0V5mMRe_jVDIK2IwA1siKJ4SYAylwuL8V2oUbVQsbIFosl80nv8t-oldWMYu5z_dpyB3DeKEjbnL8XdpzPLr9SUKO_48cxQtfqBo1gXOP79A02qJRaifVoQskLLvjKEDMlmRZESN_XoUndrASd62B3xQDkonEgm_1nO0c_fJ-ujefFgf45jBfQt8gnN9VCGcD7M8V9JLW4xd92aknjoBAeWqhRn6FT_lchidLwru26HNtJUBBmElzT6H8ELaiMozRGjORPfbjwdXXYRJhxjeMv5BxQuL2eJtbqWkzSJ5X08A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌ دیروز؛
برد فرانسوی‌ها و شکست ایتالیایی‌ها دراولین تجربه زیدان و بازگشت مانچینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/30446" target="_blank">📅 01:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30444">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Srf51yGUHDLeP92dwCOEtLEl9EYQUyaytlajP3g3CgVxl7PDDozvg2fvl9DKHEGzmB38JkNlG9SaF08wJXGV-EASydKyE1ShTV45EBNIuwNEgXQVF3S9J1jpco1pY6gdhiTQ4By9WGSdrtXSuL3sGqvsNiN-VFF68MmZSmA1lMfW-idSKZf-EYYNsJ-UZ6K9Em97gb26ZGlUGusxRcNTjlG5B1Md8Y1x3HWiEUrFILdGvUk26vBfHoXwXg745qO2GWnDMp4zUXHyWu_Swj344F4D-LbUm6OLCEAYfd2PAZKH-ZvDGWfQY2i_O9WKqIacFQ6hJNZP8KuvDqiuXEcyOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازیای امشب هفته اول لیگ ملت‌های اروپا؛ مانچینی با شکست استارت زد؛ زیدان با برد. سوئد با درخشش گیوکرش و ایساک سه امتیاز رو گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/30444" target="_blank">📅 00:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30443">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHnmNET_35uI9ccMehLJZR-uZV7N2xdBgO50E__ouC1NAZqPRHksex1pMdGSZlZLrK6dPxsfbIAHL_A6BAZU0w0yInF3BuhEG1QEF26rV4_EIiHA1f8xVPfcP6TqI0DAZUJeMALYl_Ki4B1Ct7DVlR_PL7cDiNzfOLirknWm2g4x3WvMBPjXIt6hsgvEs05LQolIn6PyxVkbhbthxiRi6chXwM-2hAcNjnNojnKgqtgscIf6LfwSA9AEudJlF4L_WxQQ2mXYMoBvtK2eH3y4JAdGGYwhUy-Z55dzcERx_KFR4O8HD4BZOfG5Z9_THodeH1_e4n4LBSQnWJB7qWhzPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ ازبازگشت زیدان به عرصه مربیگری تا نبردخانگی لاجوردی‌پوشان با یاران کوین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/30443" target="_blank">📅 00:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30442">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H95lNf2fCk4lxft6rsXiW_Ef690wPr_AmuYTF-HePvx2mQbI2C7szHFE65SFIiP_cYjyyQBiuN-fkrZcy4eaojxrtCnuKaY4LymK5ZaqlHknydTuIJJzr5I2Wd6ux73b2aCYveY_n7QS9_6yz-fOcozfAYEe-X8z-iLyTHDk4tKGJlv0XkKIUibEotIIcyS8b0CCv4VH8cqIDRmf_hJy7as0VA5mVkXOgULUVT-LxybRHsiF6TzWhaBzj5dDSbwuWWzHaLQio7zg1pIluMRkNudyFy6QpkZ3lLGgQ5aCA81CA04EV3b3drDAWWlMGEHN3js9nxZ3z9yWhTCAtM5jGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ قرارداد مامه تیام با تیم چوروم اسپور ترکیه تا پایان فصل جاریه اما هر باشگاهی که او رو میخواهد با پرداخت 300 هزار دلار میتواند رضایت نامه این بازیکن رو از باشگاه ترکیه‌ای دریافت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/30442" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30441">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nptYs_YOGGuBwK_rlCSL3E0XVMd-uLuCVetKT2M86bZYTY0cC-1jJ_hhzyJElgTILdulF2tKHo3KgAhBzmJPPg3zgk-GPBj6DRnqj1ToHAKcnApkZl9NoIDuCBQE1v9Bu4oFwJTpvzwPImVe-84kLhbzru2wdNbGmGkjbXwfyy8_GwhBnboM5Ckym0CPCbVLN7Z_USPpP7RptPAcV39-_PBap2PM6i2qsYLaXX6rblF10dc2MXoJkSwwQiId11NpYoGGNzl2CAbXlBsNNrQjKlnDuPm9LnlGs4u82XWw_je0o-MiVSZHVEm0JxhEyhxUG1M55XZkPrW7RC2_Vhxhdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج نهایی و جدول رده بندی رقابت های لیگ برتر بانوان در پایان مسابقات هفته دوم رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30441" target="_blank">📅 23:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30440">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jli9nvZGfJe-WkqX6PQhO8njeVLHZrr273jvGfGmVI6X1EzIb0mw0b8YmZtMEf2kLvsvy5chcPPNX5vJr6OS2vkewhl8I32BpOYrZoMb4fVFkFr-PbdV9Qp8J6LIBQ32J4p2z7ot-KEOjj9iasGDbIzSRiZlT5opRwJloiPJPBkdL3VHmQfoysf6kAn4qtWJTxSE1njE9q-JDlzOh3U6rXcApD366IE0F33MP-NGE68IBq2ddFrD9uPTjz3tCZrEVf7spvlfrgOM6syt0GwBnMmjAltw1V0PXIKdkCd62kswlULXM9VyPC3iSRCa2SZJysLW_0OcRRGddg3uQW2cMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت مصدومان پر تعداد باشگاه رئال مادرید درفصل‌جدید؛ فده والورده و ابراهیم کوناته به جمع مصدومان پرشمار کهکشانی‌ها اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30440" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30439">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔵
👤
مهدی توتونچی مجری شبکه ورزش خطاب به حسین گودرزی مدافع‌چپ تیم استقلال: مطمئنی استقلالی هستی؟ فردا روزی مثل جلالی نری داخل یه‌برنامه دیگه بگی نه من نگفتم استقلالی هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30439" target="_blank">📅 23:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30438">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8p9UQq_JxCy-5UxlLJbDwxR9KPmyzQPMUK-uauS-w6-aYkpophTlvXO6R6NuWyWNm_KCm3F3zSHsRjBlU522AEjeYGN9JrE3yoiTeNZ_I5DYQ-X54ps-oX-GJt2Orq-c6iSqGcEnq8QNLuW1Yl_6eVBSUBKBaV_hpp4vi0MNZpvwvopm1SxgQk2S9wwQs7fBwWsJ8A1cNL-19TwXdCCOERWzeIYh9glUQUJSiK5TCt1Ab9jWsKgzr329O01nfXlgMVD_a2bjI-COOMC03F4QnhftSBBYX6eFvXp042X4-M1Dh7-XXChPt5Zz-ZyXc7VwhFSAgPhxni0Onak2wGVlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شاگردان مهدی‌تارتار درپرسپولیس امروز عصر در دیداری دوستانه یک‌برصفربازی رو به چادرملو واگذار کرد. علیپور بدلیل مصدومیت دراین‌بازی غایب بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30438" target="_blank">📅 22:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30437">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGh251_hxMXef9AHLuRC3ERaAb9sfttn2JsRILaOU7YB3gV4rfHVLbNq-YWxKjkhfFZsL2cn0x5BztbhfezVibkjDTIAnHqrvXMclKT2565uewWurgDz-35TJCZ5Xj_8PDR9bGjUTfk5bo4lWDwyOKezf3CPf6tqaB2B-8GCpAE26fMYLrjXRcCxUODil_XwOnKyWMOXKsoK2QjKJvs1DF_0j1My3-iUn3AZkmgHz1Z1CWkCpT2G-TQ5MpdhCJYW74btew642XWu7aXUf-oMeeG1c2N2s1PfIYpnicfjkmSoH03bbdi_8rMBewc-dYJkWBh2otad2gDIshMRG20vtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇳🇴
#تکمیلی؛ باشگاه منچسترسیتی انگلیس برای‌فروش ارلینگ‌هالند ستاره‌نروژی 26 ساله خود در تابستان سال‌آینده 200 میلیون یورو میخواهد. از بین دوباشگاه بارسلونا و رئال مادرید هرکدوم این مبلغ رو پرداخت کنند بند فسخ هالند فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30437" target="_blank">📅 22:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30435">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uz8rVP11gpI8MvDxl-WZ1eJal-80sr60vNoVsxyX8Kv4xhruiMsOtEhs6pcUK4C7Soew-Nj92F350f6tsdccPupIiHb4rYgNZPnlBXpJ_5D0ZzVOP046UNBHEkmc8-UvF5i_tRTOsCrk1e00SbhCBOiq5PHFoZh55SC_FTL9LdPONIZNWZVHL_WA0zvYiXQoMoaZgEtnphjS5jUUhJFJ9cI4c2hYZ7Vnm1FNx5etD-AGCEgdPvIJnDAaqX0FiCN4M5a0s-Uq1YJVLvf95cBKuekI8ovRW6Ech-FmNxLmCtTzYcLgARZ5PSf3X-to6bAZnOG37V12zwmeO0BPeDpm2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YtoV7NdJFSZGbivjOwH3g9WYZoP2Y055XIkXkeEBX8ku--pzfT8LZ3t39Ii7BVRrx9qcxwiMBgI6BbxEbUF417bgOMMQHm7nXDfBBWV0FRo2JaUVdcLgEmU_m0yAgfmvD9F0qWAi2smV52xSc-7Hk8jhdkJAmPQ6ft3MXjdg1tpEgFbWAWbJXL1AIjr_zfKgodNzYyEw8nBRgYxfaKHNmbWgBlvNhe--WCk8SPvexCWK6rF-fXozwyD3Lb3rOhncaLX-eJJlEl7kl_UG6DZwnfjQ4VxvvvYqN3rYCaBC6G7XWEYufFADcoL-ku5z4qtquZs1NL_O6mVVBQDDQqL03A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول برترین گلزنان تاریخ؛
ارلینگ هالند ستاره 26 ساله منچسترسیتی‌که تا کنون موفق به زدن 370 گل شده گفته که هدفم اینه تا سن 33 سالگی به رکورد هزار گل زده در کل دوران حرفه‌ایم برسم. در حال حاضر کریس رونالدو نزدیک ترین به رکورد هزار گل زده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30435" target="_blank">📅 21:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30434">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21cf909039.mp4?token=ungUb1xKBKeYf37A1t1ZTkARD2LloXTT5Y4opOH78vJp7qnTJZrN_NAQ84jISmXLeftmWgajpSQjagKRXTB5n0oKBVfttaStFyZnfTeP5ynyzc38qWRBdKZ8H8fcqBD-6oybvjELsA-hj-gjuJj1aQaGAvkgjDcGkRs_R8ha8IZZqANWacXjL6j7Rhkuh6RpCO6h1J1XQ_ETJFT2svDU7bCZSvp_RljKGAArtR9v6Yv19Ofca5tskqbhOExqq4wNoy7e9GjgWEsTq5Zg0C0hEoSNydRqz9PMFTYEVU4chxNtRw7dR_CXQ6mXSnL2F4U9XbBbH9IXLtfv-bRCbH0A8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21cf909039.mp4?token=ungUb1xKBKeYf37A1t1ZTkARD2LloXTT5Y4opOH78vJp7qnTJZrN_NAQ84jISmXLeftmWgajpSQjagKRXTB5n0oKBVfttaStFyZnfTeP5ynyzc38qWRBdKZ8H8fcqBD-6oybvjELsA-hj-gjuJj1aQaGAvkgjDcGkRs_R8ha8IZZqANWacXjL6j7Rhkuh6RpCO6h1J1XQ_ETJFT2svDU7bCZSvp_RljKGAArtR9v6Yv19Ofca5tskqbhOExqq4wNoy7e9GjgWEsTq5Zg0C0hEoSNydRqz9PMFTYEVU4chxNtRw7dR_CXQ6mXSnL2F4U9XbBbH9IXLtfv-bRCbH0A8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد تند جواد خیابانی در برنامه زنده برجام از فدراسیون‌فوتبال و کادرفنی تیم امید بعداز شکست تحقیر آمیز مقابل کره شمالی در بازی‌های آسیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30434" target="_blank">📅 21:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30433">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJOMRgcj0FSEbv-KqLUQCdyXLbmqabbsGTc9-oTUaTpS1WhfF6otYqgOR-WHVKTczvM_aW0RKX0X2y7i-Chju8yPBLUGpH1njMtKz4-g6Z7a3LbzTmsYoyvhokSwameM19HkX0Yjq0R4y3W0ypiCN4LeOllq28VcfKe0AmrzbqNIS6xzwd2TD_5rMKRC6jnO2nVv4nWqz-TS5oNhb491-owKFSCXCMdGqweLf92ck5SCqKPtQCU1ygfsHYzlvCfHMrf-nOVpuIlnMqmfDKeFZoktP4zBQzNLVDg5Sg_eYnY5ntNNgVw4MTWDU22VEwNBA4QaUW92WjAEaEj2LfjLrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت فصل جدید لیگ‌ملت‌های‌اروپا؛ نگاهی بیندازیم به پر افتخارترین تیم‌های این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30433" target="_blank">📅 21:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30432">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYciwdHvdzwN49WYHmM8vjfJYDBkEkt7F5t8AcdYF1a3CuWF3MJPzIgveKp1ZsRcaAUKXETxqt3X2iOuvgtunZcD9VY2n9MIFGX7xRbWfIEXmqerZwlEc1-rWiepUqUZp5WTsDgQj0vslqbgrCRFXvjy2clzMtgp6SC-N_p4wGEbpVqxBB-_tMsyF9b6g0grC3zFiwYKVjq_9UbqOBhtkPgKmZWucZDj6hcyQ9FAm0ey0ZXESykVZgMbXP442puIZ8ThP76_WcoKlmrQ-X5MVyJljOay-GTd5pTa6roRy_R1D2q2rjlxviNTSPuBdN-QYXPhKuZRWcL9UpRDTU30KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
دو لیست‌متفاوت از تیم‌ملی؛ لیست محبوب امیر قلعه نویی
🆚
لیست‌سیاه‌امیر قلعه‌نویی رو میبینید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30432" target="_blank">📅 21:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30430">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/537ed2cb9e.mp4?token=NZUdPRvIZLEsV527et081giQz8lbMZVg5uFfm1mFVlWJrExbZ5SWpjlBpSMDfD4d2Sfv1x7qGl2Mz1TloXlrbLM_gFQQo780GsTQFq_ljuscjDxz2030mR-o1wVaCrF6mJA2AMM4y7q5Ua-j0agzvlFwahQONowATHs4HVQ3Cx_fQR7Wcpkv3pyc-PGJpZFu9BBFNCIIaQDrVOAtWf6MSpp5i3c3XHFKrBn88lX6egFUPge5rzbpUe4CEw_6ezex2GiOZa5embZ_i61RwG3dIqXnDfOAS0M2QWltkdAkBb0fEx8LeigJhuCP19bwq5Q_ktU0hcVu1GhQSyZ9Z26fpSgK9q32TcYWy8K8qBmWEkH8M5f3oI-AgRYxIDHgaNKroCGHXqNLlZ933BJaG1BjrdUwSu3cgy_ZFFizveaKJpys4RTwIHiqJcQhx83sEhoA0zgSjXxKDMTPGwVgpIApz_S-q3CuF1UHW38IvfzCQvYbschlfSuiPJFSUPg0U5zkdsajimtC2ercbQKx2ZUd73l-0L62rDbm2peeWHUnHu6x0tOvUOnDVdGE7Y1IsLfDMcugQahIgnweS9ZWme80QFhSdnuoXQr3yopZcGWbdTDzeqkTlln_UlTvCNVeGjQdEdumjJgFnxPrdDjWhOoWl1I6ura6tCxE4p6YWADvVq8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/537ed2cb9e.mp4?token=NZUdPRvIZLEsV527et081giQz8lbMZVg5uFfm1mFVlWJrExbZ5SWpjlBpSMDfD4d2Sfv1x7qGl2Mz1TloXlrbLM_gFQQo780GsTQFq_ljuscjDxz2030mR-o1wVaCrF6mJA2AMM4y7q5Ua-j0agzvlFwahQONowATHs4HVQ3Cx_fQR7Wcpkv3pyc-PGJpZFu9BBFNCIIaQDrVOAtWf6MSpp5i3c3XHFKrBn88lX6egFUPge5rzbpUe4CEw_6ezex2GiOZa5embZ_i61RwG3dIqXnDfOAS0M2QWltkdAkBb0fEx8LeigJhuCP19bwq5Q_ktU0hcVu1GhQSyZ9Z26fpSgK9q32TcYWy8K8qBmWEkH8M5f3oI-AgRYxIDHgaNKroCGHXqNLlZ933BJaG1BjrdUwSu3cgy_ZFFizveaKJpys4RTwIHiqJcQhx83sEhoA0zgSjXxKDMTPGwVgpIApz_S-q3CuF1UHW38IvfzCQvYbschlfSuiPJFSUPg0U5zkdsajimtC2ercbQKx2ZUd73l-0L62rDbm2peeWHUnHu6x0tOvUOnDVdGE7Y1IsLfDMcugQahIgnweS9ZWme80QFhSdnuoXQr3yopZcGWbdTDzeqkTlln_UlTvCNVeGjQdEdumjJgFnxPrdDjWhOoWl1I6ura6tCxE4p6YWADvVq8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پارادوکس‌شبانه‌ابوالفضل‌جلالی‌روی آنتن زنده: من هیییچ جایی نگفتم که از بچگی استقلالی بودم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30430" target="_blank">📅 20:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30429">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VC4tnY4gG4n82OysQELsgB2XymZ9Ps45Qy0i7sHmnstvmcRjiNrvCsg7B5sNFcxeOG663h9g-SXoDTR0-mqLQaxB6MdcqaFYH6FlNnkYQzoyRLXWi23CnX0VaqVLd-rH0ztQpLPx_PIz3vzIgvqvzkgEASOMKSCCdN1kAlil2yUsE5gpkRx56C84gqt5iLbl2hC3XGTvzixfp3nLsi3fFOnOoFFkpg02imhKFo5dcJQQzbkAw-ZHDAM_P0nxUK6qFTbNSihuFCrHkk4yCew3HrNkzlz9-caupYIyGGhwxap1SIhayrtnVIC4cRS3q7xoyw_VOjtDThw0p6gqFxSTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌برتر بانوان؛ آتش بازی پرسپولیس مقابل قوی‌های سپید انزالی و شکست آبی پوشان پایتخت مقابل خاتونی‌ها در ایستگاه دوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30429" target="_blank">📅 20:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30428">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEJHaFtFd7S8gDkJgECdzn63PaL8ope9Hc8mJPLrFnxbzu9kmlTekIUQIpXmzAk3RHb1VRy17rW0jFYBBr6dVdUDZwrjqE3hOdfXRy_PSDGP-axP3ZmI0PAxwKSIgjs0sbGkrHkVzRPaEYvlCb2QxGd9tWYFmmLeuX7p77jJS__TyKk3w9bzDb32MjqnFMUbzr-ompiUajrWp2forLB3-qR3caPXvNg3O4cAUchlNjsn3ktqPxHE0iqZp5JiP6uzHZeGtevdOJablC7U3SOYE2PGMwz5rj0DSTWWpgnZrj25m_fLe9oeOJvGAnDXH3tCaj1iCoXmIk0HqhPqzjsTbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بااعلام کادرپزشکی باشگاه استقلال؛ حبیب فرعباسی دروازه بان مصدوم آبی‌ ها به دیدار شانزده مهر با تراکتور در هفته هشتم لیگ برتر خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30428" target="_blank">📅 19:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30427">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-ROpXu-lf4aDNJD8Jojca7ZJJx-6ahO2Z-i0DLrDVbyswK8QHnarLw8wXdbNV92K7V9aP5Q8RJw8_zYs7-xuEArYv1Sk_OupfQnVuXbQZoFiUaJPDnosOLzB945fzvsWf8FL8UsGMAO0vVALp30hGUS-SSouFIGPWQR9I5k6xhkCEMjIcLP206vE9MzdfI-x9wHMhiSaOOXvvWwKEPfS5osovtxQQPfSWm3o55MgMosxLiiVI1ehxBoW-yq_dYsBPAkWeBHDtGACWkkV14KhefPG_dmN1wj9P5qEa4cdDW2xJhC7u4jo-8kqlWw04RN5UL_-wlwzCCurktBvV60qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
عشق و حال مهدی قایدی ستاره ملی پوش النصر امارات با پسر کوچولوش میلانِ عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30427" target="_blank">📅 19:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30426">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCyEX63i5Ff8k2u7unIG6mA4_JDSW8ZYM-Gbd-NaExrKfIaspVZuBlDxzNi97dbQuUfORRlCVllz5gBk78qqpEVxxqk32NHiGMcTn1Pn6zixNEQFhr_BicDETY47FEnfttV_N9PXvRGv42uVzSNkSGCP1iD4-hxC_Rq-vwzgM3cHEOVyGcWTgl1Mg65v6kG5nhrVfOQjsfg3DGVtpXgBLPgkWBqpUNztbwSsKZ52X23Geh4Do_atnuWTvR_Udf_9TkMTQ-92BQxWXpEvVxEwbVDd0c2Oeyhe1ecm6Ujdu_ktlqD5NfM9Vtsk3lN0Y-y8Cajcxk7HTM7mZYGnC257CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ظاهر جدید وین رونی اسطوره باشگاه منچستر یونایتد با کم‌کردن 40 کیلو از وزنش در تنها دو سال. درکنار کاهش وزن رونی اخیرا یک عمل رینوپلاستی "عمل بینی" انجام داده که باعث شده همچون قبل خروپف نکنه و راحت کنار خانومش بخوابه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30426" target="_blank">📅 18:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30425">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iik75cqNXB2y5BbGAh1dZBOEpbUc2ADJnJFEKrqIo7-bSzkLvIP4IKb0v1syggk0azitdJRYRkXA3zG_aqr52ZIESIb0AgdJBmjArHNTt8uFVzKz2YuTGnmXoDnQ55PXo7NQZdmJ6ehVaSqEiVAbAZmD7H4kZJosr2bpNyqSlsPvbzaMKJlOzSi5AuMWHNARuBaGoWpFJ4q63U8_mVsgDdgMsPBKtOWeggnwyYvJxiWD7nHdPtcGc5YCNo3XNXMeNq--PVZH5be4S1GQjWZ2U7sIvJLnUtXdBQIPwj3DfJ4y9OdCXd5lmIT4w3Q0wCR-IQ62yFI0n9fCG1CqBPWVbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
بعداز تمدید قرارداد اوستون اورونوف؛ باشگاه‌پرسپولیس قرارداد پیام نیازمند رو هم 3 ساله تمدیدخواهدکرد. تمام توافقات لازم انجام شده است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30425" target="_blank">📅 18:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30424">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMpO1U9XrpReDqLAsD1jGkfuksm_MgeIr9CfGmiyNs9W8hwmaHNZG34F5DRVBhpwsEwU4QiNjCvnoSZHkeyuZ0WLeUbF3xC6yKgkduwA-8XOmEDZz6ABeHShAg2OrAIHgdbHv6gyVNTHmyc71retb1_vb3JDN_FnEIIzazMgRWso0PRGTELp7RlZNNl0up-1jLIXuxEAQlEQzBV15_fh93JpDCaZw1pxT58817Ur4y8F-4pHHOoEOX45KLLcce022TM55DvIBsd8mr-6wf4KvuOZ1VigQcf-slaNe82K67aSoGFxQD45MFBRk3lb72NbO1BI1jP9QkOF_7TcVNMDKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌برتر بانوان؛
آتش بازی پرسپولیس مقابل قوی‌های سپید انزالی و شکست آبی پوشان پایتخت مقابل خاتونی‌ها در ایستگاه دوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30424" target="_blank">📅 18:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30423">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rfoaii2j198F-IF5ZOkhAw_a73kvzWqBFQaLcIOA3Vqo-f-IbtfLRBSAHdkl-FBfo3o5sbOhsVgDDkg-7zKHwfw3ECh52D7KDktqGxuYWak48vfRv2XCOJnONBjj6rp7d0OTlcG68DrQ2VOagP0_Zsu4o2xls6IdxwKKRBnxw_nxefL_FjgGGVOc_hqZuSf5CmN9Y7Ntg-iQwAV0xqT4Hb3Q38408fBg11f_2K9RQCYAU_v11Za7e9y-qdZsn-lR2jCCivs3LL5lV1KinQuci9s-XGZ0IJu44JYxFmkfsJdzTRpMbBCR4Ehq-co7iaBDnn2xR5Pp8Q6WTFd2yDDxpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
پرسپولیس دربازی‌دوستانه امروز برابر تیم چادرملو با این ترکیب بازی میکنه: امیررضا رفیعی، پویا پورعلی، امیرحسین طاهری، علیرضا همایی‌ فر، میرشفیعیان، مجید عیدی، محمد خدابنده‌لو، یاسین سلمانی، محمدحسین‌صادقی،تیوی‌بیفوما و سرگیف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30423" target="_blank">📅 18:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30422">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdgujlST_Zu3UhTaWKZ4t9zpAEFipCfRIStlXU5FHDzewV3rk3ZoN1jR_IN6A49m3NrijS_7ocVxtYTFaegyZzu9SOl4MRFe18w3-Zj1r2TFCPfbPu5AdZLors__PSXKqSSOyN8XB-3E4A25tUhkCLD6s9Mx5hI22GljXwL2VfT78zsoSoYaa0BT_rRJNfCw3wGK5izaJZItm2xDnKBIxG-iDFrL1mX3oY24xaCoTBpw3u1MzVNVk4Vaz0iF67eyB10UT8ZJyVkD20F3QsBcKlDrB7v80e65pXOiKbP8j33prPH_ZH4rwmJfVvW60MJCJeUaFBVoJlEATsn69Pa3Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوید اورنشتاین: من سیتی درتمامی ۱۱۵ مورد از اتهامات لیگ مربوط به‌تخلفات مالی، به جز فقط یکی، مجرم شناخته شد...! هنوز درمورد مجازات‌ها تصمیمی گرفته نشده و تمامی تنبیهات همچنان روی میزه. این مجازات‌ها میتونه شامل جریمه‌ های نقدی، کسر امتیاز یا حتی اخراج از…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30422" target="_blank">📅 17:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30421">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDZaufFLH2sY8CR3eSMA2v9DfUOYGqpgI8vrXxmuG9g6L5x4-3X389Git-xs-oMb3Uguk3kpUCtIHaucBq1iNIZBtAcoV_QUvnbTEsXLJihB0Bh0SQPvhf7MAZ_pIdElqMAtcMQ1W5YLE3wuN1teDAx4OITS7zhnpcXXFQX6kJFQG4e-IYbCRd6NyJ07uKTEBbfVsD8pYHufqU6ODRQ9O43joWvcXUaGNHYYokbo7KDIs2y6rARBlpkaSusVGr0B5dahmDi1G1K5LuH2I9Yw9Zw_oHLTu1diIhuWdowxIXKq4TldfmIQLAXCxaTPStaz5tTi25G5Gf8wk3Dmr7AcuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوید اورنشتاین:
من سیتی درتمامی ۱۱۵ مورد از اتهامات لیگ مربوط به‌تخلفات مالی، به جز فقط یکی، مجرم شناخته شد...!
هنوز درمورد مجازات‌ها تصمیمی گرفته نشده و تمامی تنبیهات همچنان روی میزه. این مجازات‌ها میتونه شامل جریمه‌ های نقدی، کسر امتیاز یا حتی اخراج از رقابت‌های لیگ باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30421" target="_blank">📅 17:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30420">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLYFzATDabHF2DWse0aAGWc3id543DW2Eg683Eb7LErevXLVIz2eyBP_7FD22WVGraEtdT0MdrJn9XbLJl8kN2nhb-eQ1k4a2b7_YIB0j3k_eYpRo4MLEbMkFQ0kSRXKRYLfi5kaIlhtYxjwQUwvt6IHSowwwM_ldFNkwNNQui7MpFFBipR2FH4V4aMvJ4D7zn9fRDYKb7F0SUyBg1YSDtHm0y-_mxED1Uv8QskVWvoJCAWv3aZkrXhvIPiHv4AhZKWMS13dcKPwEaGz0_rY-0wivdfa7mhjXsuNZfuY3zbdgiKA0j14IZJhhfi5PwbRq2P5vJ52DAtzEckpJNYemA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
پرسپولیس دربازی‌دوستانه امروز برابر تیم چادرملو با این ترکیب بازی میکنه:
امیررضا رفیعی، پویا پورعلی، امیرحسین طاهری، علیرضا همایی‌ فر، میرشفیعیان، مجید عیدی، محمد خدابنده‌لو، یاسین سلمانی، محمدحسین‌صادقی،تیوی‌بیفوما و سرگیف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/30420" target="_blank">📅 17:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30419">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlT_kEJ5nr4h8r-4GsUncZ9vqEj4z7kQzHAtxulz6W1oimPN9_IIhflhyIQAt1H5G4c2yXSllPlSYODhqZeJsYpJGR1JQcXgzdfNhDUtyK5imcrfdXh_i52g3k6ss84ehKFEuHwW3YywSjgsa2p9eYo8ofYYgG8H6euNW01kEwJ6oiqvyDTX5APK1J8_vc320cLqySnqikC_-kpBIq13bPICm3vVWbRR_Bz_MQP1cFewD-yEj4zRizX2azWJXYP_x9Bws49U-WUsNO1uQFtEx1tTDycutS_e0--gyfL6QSGqNgGJvngWBahZ6UP4B8XWzdWD-awHFvG09TmIXLaiPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تاثیر نادر محمدی بر فوتبال روسیه؛ گل عجیب با پرتاب اوتِ آکروباتیک! الکساندر کوزمین، مهاجم بالتیکا، بایک‌پرتاب اوت همراه با پشتک حرکتی شبیه نادر محمدی انجام داد و توپ وارد دروازه روتور شد. دروازه‌بان روتور نیز بالمس‌توپ در ثبت این گل نقش داشت؛ اگر توپ بدون…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30419" target="_blank">📅 17:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30418">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e998b3c1.mp4?token=d8u9vdgbvQk5gC_9QSWMkcayzFJudTcPe-GVQiO1EVaCBFGDuxsP2kqjpx9Zewe4B6QOnWdb6LNIiBxnjHA-grdEZx7Ux2etdnqpVDRBol-k7JeidiWeaq_6JYs740DksrCSoc5fqv-hW77Iapd39odrsVBJ48dZEsK0n3QrYf8q76b-ltvfkFDChLJbgyAhsfqu-MTDQIfk19Q9x0jcLWdCTrNj-vprQJTJwFm-9m8rsg6_I4WY9AM-YsSyC-xje5-k61u__XopytlwHcIFkcSQoE4sJ9p7AgY6N0N5wlO4qqVtvSg5c_RWkHEoG39ICk4Wha3Ut-zBMX4af5M1ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e998b3c1.mp4?token=d8u9vdgbvQk5gC_9QSWMkcayzFJudTcPe-GVQiO1EVaCBFGDuxsP2kqjpx9Zewe4B6QOnWdb6LNIiBxnjHA-grdEZx7Ux2etdnqpVDRBol-k7JeidiWeaq_6JYs740DksrCSoc5fqv-hW77Iapd39odrsVBJ48dZEsK0n3QrYf8q76b-ltvfkFDChLJbgyAhsfqu-MTDQIfk19Q9x0jcLWdCTrNj-vprQJTJwFm-9m8rsg6_I4WY9AM-YsSyC-xje5-k61u__XopytlwHcIFkcSQoE4sJ9p7AgY6N0N5wlO4qqVtvSg5c_RWkHEoG39ICk4Wha3Ut-zBMX4af5M1ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بعد درخشش نادر محمدی درلیگ روسیه با پرتاب اوت‌هاش؛ حالا تو تمرین‌ماخاچ‌قلعه کادر فنی یه توپ دست محمد جواد حسین نژاد دادن و میگن هرچقدر میتونی پرتابش کن به سبک نادر محمدی. انگار فکر میکنن همه ایرانی پرتاب دستشون زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30418" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30417">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e769a610.mp4?token=a9Incy81n5idvpvzuzrMmJUtuJFHUQK-pp_FgtuY7MG8JLAvOdfCuDdwgWrKfpgk9gQWU1MVw70Cm2hJmVAv09yP2VqRFvYQxoTltiYZGX7najXvijtWNVFYN7ga19QLBjdVdGP1BZ9GPySbOlo3QOcBvR5DcZG62zVdF7iGnqlDqIzqYsIYc7UImWoUdlLBtxsaq-l4Be8l_IERH7ormqZpbPQW2pfoic1VP1TGd7HpiubcR02EczXbgHZ9akCQSWDfQylIpUZPmuF7chNjfT95BBu5UWUhtEpLOzCbF1PQeW_qjswLbdkvoDEOjuKJpLOO2E78-ItTdO6baMo0Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e769a610.mp4?token=a9Incy81n5idvpvzuzrMmJUtuJFHUQK-pp_FgtuY7MG8JLAvOdfCuDdwgWrKfpgk9gQWU1MVw70Cm2hJmVAv09yP2VqRFvYQxoTltiYZGX7najXvijtWNVFYN7ga19QLBjdVdGP1BZ9GPySbOlo3QOcBvR5DcZG62zVdF7iGnqlDqIzqYsIYc7UImWoUdlLBtxsaq-l4Be8l_IERH7ormqZpbPQW2pfoic1VP1TGd7HpiubcR02EczXbgHZ9akCQSWDfQylIpUZPmuF7chNjfT95BBu5UWUhtEpLOzCbF1PQeW_qjswLbdkvoDEOjuKJpLOO2E78-ItTdO6baMo0Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ساعت13:30 تیم‌ملی‌برزیلِ کارلو آنچلوتی با این ترکیب در دیداری دوستانه به مصاف استرالیا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30417" target="_blank">📅 15:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30415">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QN21XuPr27mNncJVwbE4lLZZyVUJE7RHkwY-9bmZeRFoPrzO5BaR5LRCbPeZTQbucAtaOcKH2ScmG6i2nG_A_Gfh-rEDAiL7TrenDJ_E4yBYDnRSJmlQZu0ULOgrOR3K_efZ5fj5QepsxjzRbeR64wVTWQOg58QGZ8R-5ObAWzZAgDXrvu-llW7c2_l8L3CzWcUlWmmQqjoeyjCs7WT92jUSCu2qZYfgazeOOL_e4pZ9hvtma8ZJDOkn9kc7cs4RQ2vUxWdA7IlITm-cY-l-xQXX18g7m5ARQ4HJKiYE88ybTHf6_qSj6mHm26YdFiAT5rh4PNYwvfoHSwDokvyXLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C5W-gvbseTnXEiaQrKp1VlNQbZHrlVzrsVhX6WarESenlfkBfI44fLse3kiOk566n6QhQ6ghHJiw5KUswGPcU3a7Yc1er-gPyyCbadDdCjutAbl9YmwUPvMKiGQyqzItQmiitQpvGVM-0EZJIaysKH_-fCyXuPoHU6wloAAl3Wo-nV_qbz3XLHum4T4VGBMV_hrpR-yU9MU_1gWzGvcG8QEEPsI1aiMFpxawDHQ4YCYMpQ_DfsIYVnMPaGxn2p6Z1wCAW1Cka7JmLMb9QuP318yHHUxWKicGX11Kha2zJE4e1GUKEwej0kVisZU4YcvxNONPhZ3RFJkc9W7F5UJ9_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
انتقال سهمیه بنزین به کارت بانکی از فردا؛ نحو اتصال کارت سوخت به کارت بانکی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/30415" target="_blank">📅 15:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30414">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9587608d.mp4?token=tYh52Y8SmMREcOhsUQ0zReJQM1-LXsfvGId412jFKbtUbbEla0QLRp4uurKUdmSNVZLM_Map6DERyfd3VyAvUhNLCOpMRzl0o-0UtZxw-6UQIksdpub-i_KPQLAEhx3hvChO6yUPkDtNhjFJ45Vf9pIC7iqWvYEfVJkcTWexl8VCNd_jOvwM-S5diujklkYfU-kkC29FWxZJ4tuw6xSEc-zbCSmssGMBxYchMsSiH81P9wnzUtFMYWoFim128RV7oJGE057ufJh7t4livgPhDIMCIh25IXprGELkJnHSUPgFZUNKvN-WJ0WTbnUuMnW02vdLVRtqmVwuxA8rLvkAAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9587608d.mp4?token=tYh52Y8SmMREcOhsUQ0zReJQM1-LXsfvGId412jFKbtUbbEla0QLRp4uurKUdmSNVZLM_Map6DERyfd3VyAvUhNLCOpMRzl0o-0UtZxw-6UQIksdpub-i_KPQLAEhx3hvChO6yUPkDtNhjFJ45Vf9pIC7iqWvYEfVJkcTWexl8VCNd_jOvwM-S5diujklkYfU-kkC29FWxZJ4tuw6xSEc-zbCSmssGMBxYchMsSiH81P9wnzUtFMYWoFim128RV7oJGE057ufJh7t4livgPhDIMCIh25IXprGELkJnHSUPgFZUNKvN-WJ0WTbnUuMnW02vdLVRtqmVwuxA8rLvkAAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد تند جواد خیابانی در برنامه زنده برجام از فدراسیون‌فوتبال و کادرفنی تیم امید بعداز شکست تحقیر آمیز مقابل کره شمالی در بازی‌های آسیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30414" target="_blank">📅 15:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30413">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6521c21a5e.mp4?token=SHrYLrN9_t7F8ZAcipmeeZ2z2cgY0UlabQ3MJrr12-TP_QjmAOm9F8uoBEseMxZilngmCvAZRm2Syih5UhoiUkp7odA9fABtWqtmg_ED-TxcU8VtejFNC0mSX9hd9c9fdJFj2opOlAopUBNnUroBL3I4ZotmfmDcihYtIzB0937cjqAO80IIbxRux0K6LErkjr8yMr-9PEix01XJmo0gPCC9R_f2-fjssX805FpBG82cdx-ful-ghf62zzac9FTSvA7Qa48upanPTaZgUTUIx9pRYGgcxA3nC9n3Ftsn4rrt6_ywHGG35HWKygJ_x2NJXcKEIvP-BlcyiuIf6D4kPTUbWELFBV0mVgKKLKXYy3B7Lp7dIIprXPlrvr13vljdh4JIKx4rjMRMeUQG3GKAj4yzD030UwawxX0XfAHsOUzGEul2P-Vs2bQN2uEK9OaWAbbp_xxCr4Mvu4z2kBIopj_J7pV03gFzJJs9HRAErvLxxDFZrmtArs5v0OjddZ-4WWjOroUmsg-vxQaxhgUP8ZQK5jKjPJqF87wTAMHR5Vg_p2plOcBdMlfnQRdT2pOM2Yh2lcRmMqN5A_J4YEDcQQeA8DHo42ZHgThhvjOQBA8mnEa17fEd0wdJWwOM5l_1VVfYffYMSg3lrGMYa-2znZprUlhHe-xIGyz3yUOTO38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6521c21a5e.mp4?token=SHrYLrN9_t7F8ZAcipmeeZ2z2cgY0UlabQ3MJrr12-TP_QjmAOm9F8uoBEseMxZilngmCvAZRm2Syih5UhoiUkp7odA9fABtWqtmg_ED-TxcU8VtejFNC0mSX9hd9c9fdJFj2opOlAopUBNnUroBL3I4ZotmfmDcihYtIzB0937cjqAO80IIbxRux0K6LErkjr8yMr-9PEix01XJmo0gPCC9R_f2-fjssX805FpBG82cdx-ful-ghf62zzac9FTSvA7Qa48upanPTaZgUTUIx9pRYGgcxA3nC9n3Ftsn4rrt6_ywHGG35HWKygJ_x2NJXcKEIvP-BlcyiuIf6D4kPTUbWELFBV0mVgKKLKXYy3B7Lp7dIIprXPlrvr13vljdh4JIKx4rjMRMeUQG3GKAj4yzD030UwawxX0XfAHsOUzGEul2P-Vs2bQN2uEK9OaWAbbp_xxCr4Mvu4z2kBIopj_J7pV03gFzJJs9HRAErvLxxDFZrmtArs5v0OjddZ-4WWjOroUmsg-vxQaxhgUP8ZQK5jKjPJqF87wTAMHR5Vg_p2plOcBdMlfnQRdT2pOM2Yh2lcRmMqN5A_J4YEDcQQeA8DHo42ZHgThhvjOQBA8mnEa17fEd0wdJWwOM5l_1VVfYffYMSg3lrGMYa-2znZprUlhHe-xIGyz3yUOTO38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های پیمان یوسفی روی آنتن زنده درباره حواشی امیرقلعه‌نویی و دعوت نکردن مهدی قایدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30413" target="_blank">📅 14:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30412">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esw1M9FCYq6JnE9CzMC-SYcD101nNXbpQToesTwALI8OHrbGW0UzYACY7-YAClISUFw-6LdgLz2HOHeYRxql7pVXe4msX4I4tpsSZesOp6VnRfeROxHw8ywvaUwd3YyZOpfDOJn3zIITPfy4wm4A7VC4MZIGDsjfS-9Z40owW1gXflPMpFjYfSRelPgdQRjVCkC6DSOuIvlAnhMg9KoWYuHB2oCjWqXJX2notYfu8IBKza4FIpBBTFGcfMdua3hNxRi98gUrxoWAlvHiI9KH65HIHD39srtEMvpwiF2qhvYC15bLaFXQEcefUZzn1Ml8XxZPqkumpvGIbBcgHG0YgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رافینیا دیاز کاپیتان بارسا؛ صاحب جدید شماره 10 تیم‌ملی‌برزیل؛ این شماره سال‌ها بر تن نیمار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30412" target="_blank">📅 14:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30411">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-j0WNPP8kw3pBz2sKJh5j2rM0SoF-aWGoOEyVqMbM78V4aX5RocP64mrwkcgM6xC_nM9i2GEPaNR4fgJXpniW987IpkRv2Q_UnSRmz7lie2NLmhbzespmsTnK3Nmo9T9crBjQpCzndMDJ44wXQhVQAthN1gB-7m335D-jdYRGY-YiefBzKj7ypQxL6c5d3aMIbjFFoDnY7-n3XAyWWbNUeKj04RK4wSvsMrV3nw05grBNBPZVnPAmrU4OlSQTXHDonXoy2TxBs8hB87nma45--PzxVFeiZ8-OZUF0GQRBUw2HqBWZz5U2FPxRRvkM4sZIiX8EWr3T82XOqQbVPw5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه سپاهان قصد داره درصورت جدایی مارکو باکیچ از تیم پرسپولیس درنیم‌فصل او رو با قراردادی 1.5 ساله جذب‌کنه‌. مهدی تارتار علاقه‌ای به‌سبک بازی باکیچ نداره و بلافاصله بعداز فسخ‌قراردادش با سرخ ها با باشگاه سپاهان قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30411" target="_blank">📅 13:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30410">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goiJOKNM-bQ5gfqiHJc_XpPGJi1kkCE7toGAmaN10kMjBxBC-CBUvdIW4wnYZY2aTTtVO-gGjdLwVVXEDbKfKI-1yhoIArz65cVADkBlCcdqdW--XYSFwgJCxaudtEsv21RQJO1mAL4a8mP0u38PpV4el93q-3lo3PJjswk1FC04XjHapy8nDmo7_usLSXK79fpcrJPm-eUQ1lenf9cLuKxrAXw428vpO2HuWK585go2BrXzUfiZ_IyJH2PAU3FmNTuVQ67zSum3SPC7fEEsyk30VGHGbc17-Chn5v928-E-zU4UZClWPVUU2GA24RzXtb_BzviQYw8Bn6uNQ2NanQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج 4 دیدارمهم‌امشب هفته اول لیگ ملت‌های اروپا؛ از پیروزی خفیف پرتغال با گلزنی ژائو فلیکس تا توقف شاگردان ژاوی مقابل آلمانِ یورگن کلوپ و پیروزی شیرین نروژ با درخشش ارلینگ هالند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30410" target="_blank">📅 13:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30409">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzj4We8w7F1OHMTQ2eibQcZSGCJZiD5IAisA-vyuB80uoQbPxZgUZQXD79JLtO0cG__gBVK8N9nI43V-Bkb97Gmzf0F26sTWgoUNU_9bzHkRg65VaaIzeH53wY6Q5xxY63X8FUr3VakuTMtEkaoicOxALA6Xu_JT0JfImqAHLM2bVVEl1ikx4T4QikZ47JCdUy_hu7CFO5o5sMDOu7Z7GoYhquWxqF8gvvSNkO96cKhEw_t9tNGneGcSUx9CTX9jY9sbccYkU7wLsTE30WkDBb0APthR5-CA3IAGV1qQomKtpbY5FEwVCWWWOt2ignQyhuObGj26y5kYBWiyKVds3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30409" target="_blank">📅 13:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30407">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4-APQn0zx8yEji3bIcdVFlbwb4WZJhSYvO2lfzu1gmUEmile3_odEdLqrLPZe6NlycfeR2_Vrl57NfZVyOtf-KRsL6cHguaM7j6jhxPG3rQePqu8xoXoCfzKdXop3COIDNE-DJ0j0YUb6iMCsuEjKLm1L3iCExdA0zxYE4QoyLFvRgaRSOtj73DZ3_ctvlcARPBNQn1mvpabYBTE4IilK_BsC61-Scnx1A9UQV7D4tN6jLtlICHhRzNL73zHte4SX3IPtNN16eXaoEFBLKQw3cdxFE7Ew-za6NbDdlHV4WDRr-s7eUjFHdZAOfkhF3q2UDeiFbVXw5pINiXweFJ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌برزیل‌فردا دراسترالیا به مصاف تیم ملی این کشور میشه‌. حالا اعضای این تیم به محض ورود به کشور استرالیا بااین‌استقبال میزبان رو به رو شدند. همشون زدن زیر خنده‌. قیافه آنجلوتی رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30407" target="_blank">📅 12:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30406">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3hgQI9BhoIMpjCkkYf3S8kDS6ngrRZMLju17GhTGo2wc9XrdVkrG5Qb53RLRWRs9GT7fbfXFRa_16SB_GIsbLwmriPHK5WkysO6nZA_lHoudYjYZ26L3tJR7DH_8PmkJ7GmAxTTgRfExtbCV6wgVy__Kk1-WtaNuYu7231Nisp8hcGEQ8yr1rZjwDrwyLdI6kT9p21IRAFfzG3296oP1d1GnK3KdY6mcZpMd1muRSEm6C_5_F3NzyEtycD1yAferRmfZ4tT-3ICK5KXxoRF-reqAhB5HalGh23nc7Tbn9BodyR4CqxKDYUF-wm7t8saV5rlURGJfG7_66DYc3fyog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛جدایی‌دنیل‌گرا و مارکو باکیچ در نیم فصل از پرسپولیس قطعی‌شده‌است و مهدی تارتار به مدیریت اعلام کرده نیازی به این دو بازیکن خارجی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30406" target="_blank">📅 12:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30405">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaaGJMYE58bUQWmHLGuh3uEq68M7eeQx0IpCTixwMT1rkJbk5uYlW3l1wPoDHWK30aWRqXp4fpHcQ98zTpVtnwRm39uc08XJF0NJKXohJo_8ZoMhvHDxt70W2FBWH9bWxMyq7hcntCm_CCfx55a96bgDEF71qeiuOusgF0atF4WCwPTu-JJAhray8t1DGbYqpPeEkBGLTDDaeCjotw9dGWUqQtiwcTdy_Lcn79h8uj8QYZkTmfw10sg-xgV67J6e67F5CoSLn9MmjnySrMBMsNmXq8XA4W3m7NJsoj-NrMtPugMVxAW6KCxmsjrwmgN9TKqo-maoojWObOW5pXSGgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ دستمزدسالانه مامه تیام درسوپرلیگ ترکیه 750 هزار دلارامضاشده و دستمزد فابیو آبرئو آقای‌گل سوپرلیگ چین 950 هزار لار درسال ثبت‌شده. جفتشون‌هم 33 سالشونه. آبرئو در نیم فصل بازیکن آزاد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30405" target="_blank">📅 12:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30404">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZjJ-dCJyu1AMAJnN3BMvLyTwkSJWTbNysxcCwoHrtXNgMV-gZtjJ4l3b5IKLkTaNhwmWcwvEjIvTlV3UGbeRVN_24ifIJrclvvpGiRwBFdX0IYcGcJc8XKwPSxi9hEaF9A7oH7cM19wO5H58QZQ3H-sFcGvb3cLnmT3MXjR2fa939yDNRY-VNzN0CDKimCAqjjtDz67T7_mgjHPe1XkuC_hfxp5Lvu3dkJAHZECNr7jgF6gpfa1n-yXzuKsgH9MK1oQnrGzDNOKZvy9TmqOu8fYM2qqRpdCPvu33uK8SdOjIAy7a_bR4hBtOXeLk5kmrVAuzYpG4tLalC4YkV7GLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آلیشا لمن ستاره‌تیم‌بانوان‌لسترسیتی: بارها گفتم بازم میگم نباید تفاوت زیادی بین دستمزد بازیکنان در لیگ مردان و زنان باشه. الان همونطور که لیونل مسی و کریس رونالدو در فوتبال آقایون میدرخشن من هم درفوتبال بانوان فوق العاده بازی میکنم بنابراین نباید حقوق ما…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30404" target="_blank">📅 12:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30402">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxY9XrV6rsJ7Jwenx2m5uFNDV7jkZ1keG5RIhSYrFtrLuOfQzC6Xe9JIlDxOj2DtZoQtEopIxhoTe5NsQFjy8wCthoYm5VQiGgwL_bLHGXHP2nTP8JbJfAM_fyh5xB_n2NbT1SEjaesodY8rAPhdjlYjpaaQ-kaKo7UarVMldB409G_A8H6-kf__LZomFrB_rTjdRaU6BbF36KonskiA4jNDD7A4IbQmK-06LKu6huNbOlUPkFLnbnhdONXUmLCSwSI5qo6UNqpLKge4FU4_TTgRahwzIYIoXtMgMqWpDEAvh8uaCAyKFwP4cSEZOd0OnFMCEcZmxlZdw7cpgmc_rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ال‌ناسیونال: اولیسه خواهان بند آزاد‌سازی ۱۷۵ میلیون‌یورویی درقرارداد جدید با بایرن‌مونیخه و گفته درصورتی تمدیدمیکنم که این بند رو بگنجانید و هر باشگاهی "رئال" این پول رو داد بند رو فعال کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30402" target="_blank">📅 11:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30401">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/638f1de447.mp4?token=Rq2A39Ll2heMgsH1KMBtbbmHDv8cD9cODVtPC-RBvvC4JDZLn7bPkXhRkG9HZIO747UefsiV5rZQBHNCh4vuh6dF-vwI1xbnKBnsaCs4ZBWLs0ybyzCp2sVViwZnsYV9U3VOOv1YRztbvTVRdQsfdmqZze21v5MaTC0UMq9h4tcPzP6jt-6KV-UFrcRFkV4JSHOlA07zGTNRPjcECFJzY_7jfnFe72yT33FN5Gryrtuqat_mXdTVB-7UQPc148iAuN0d6zIWKJjJpDZ34o694LBI0qfXNTFNkmXj1DJOTsTsv0r8rSIfJj5fIbRx4W1G8ycIgKzkmZRpGoBaUg79xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/638f1de447.mp4?token=Rq2A39Ll2heMgsH1KMBtbbmHDv8cD9cODVtPC-RBvvC4JDZLn7bPkXhRkG9HZIO747UefsiV5rZQBHNCh4vuh6dF-vwI1xbnKBnsaCs4ZBWLs0ybyzCp2sVViwZnsYV9U3VOOv1YRztbvTVRdQsfdmqZze21v5MaTC0UMq9h4tcPzP6jt-6KV-UFrcRFkV4JSHOlA07zGTNRPjcECFJzY_7jfnFe72yT33FN5Gryrtuqat_mXdTVB-7UQPc148iAuN0d6zIWKJjJpDZ34o694LBI0qfXNTFNkmXj1DJOTsTsv0r8rSIfJj5fIbRx4W1G8ycIgKzkmZRpGoBaUg79xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رافینیا دیاز کاپیتان بارسا
؛ صاحب جدید شماره 10 تیم‌ملی‌برزیل؛ این شماره سال‌ها بر تن نیمار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30401" target="_blank">📅 11:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30400">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIfLsuG_oJVsv3XjA81LnJfWYAO5SuzyEbuMi7O8ghLW--pPJFsaLGx2GX59psqItZfkNbIP9g_k4F5jWrTZoe6se_86ZP5LjmeBOxh6Z4Y7n7hsOdyqx06IpMO_nEPFqS0qVmJSW9-f11ErpHPocn_M56mUxWpNeqX3EuCdRbb_oIUxnYOk5tpe4NG_PlhAc84r3WdbuX2Ns-C_vnzwSbPm9oii3Gyny3BwXwFmJi4EXNrNo-JBW6d9tVqbYbLKa4iqIbW5LFeLDhC0eblwAd7q0qtsBClcviezyK4IcPIMZfj9HTyhujuj60qPW0SHFNR9Y3kLwI2Os1_19Ccz_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیویی‌کوتاه از تکنیک و مهارت‌های خیره کننده جیجی‌ گابریل 15 ساله‌که‌ بزدی یه راهی بارسا میشه یا رئال مادرید؛ هایلایت کامل عملکردش رو تو کانال دوم گذاشتیم. پسن ریپلای شده رو نگاه کنید.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30400" target="_blank">📅 11:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30399">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/649db87b28.mp4?token=rJMXHb7WQrKUDG1K3kNsyGmzwn0iSk88jiBdlqTRYVxZMJf2Ake9DpudqBIH4sVy5ZvRA9jesGeESIdL3Ep6SP5XdJigddbe3WaabijB_Zeb1vTtK04Up1TCfNrjiqoWe9VmnOfY-7U4PQ_tCxSuH9M7VeckDm8VROV1hfd8hW66aJyywqztSUic24JMssquhscv-fp54UUOvEQyaa_dh9_PhOSmpHuZbQ0k7dAcg_S8zqM_HD4f7mV4ymagzJxO7Q_5SSkwhb9JBeUHOZcIniwmQ07cu1THOs-84w7VL4lXSIVqfQbGjEjCGUYJKPVx1SfdqZweYrmaOc8UXDKcPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/649db87b28.mp4?token=rJMXHb7WQrKUDG1K3kNsyGmzwn0iSk88jiBdlqTRYVxZMJf2Ake9DpudqBIH4sVy5ZvRA9jesGeESIdL3Ep6SP5XdJigddbe3WaabijB_Zeb1vTtK04Up1TCfNrjiqoWe9VmnOfY-7U4PQ_tCxSuH9M7VeckDm8VROV1hfd8hW66aJyywqztSUic24JMssquhscv-fp54UUOvEQyaa_dh9_PhOSmpHuZbQ0k7dAcg_S8zqM_HD4f7mV4ymagzJxO7Q_5SSkwhb9JBeUHOZcIniwmQ07cu1THOs-84w7VL4lXSIVqfQbGjEjCGUYJKPVx1SfdqZweYrmaOc8UXDKcPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30399" target="_blank">📅 10:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30398">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKomqnT3VsiC0rydf2vkP1tYYZ2AdlfmvNApHIRaxKE-Qqt3vy7NzKjE_oXbClcDmfjVf0Daq0T4_hS6TOVvbsVaK_NAcUnGryuGWvm1lwET8I5n63H_x5oxJwRT97eTUFUgJeKJ_GvS_3k72WJkpjCR7e1c264d1RC9o_eSOD0ML7cbxcsrvC9Di4RUNNqgB_eKdj6lSHNRH4_1Oi5Zmk7SXL6CFk8-tdTWGb-bdpJ8mhJ9mewnLdIun09etWKRd5fYvgW4WYXDAub3-5IdjaU5l6BCzjgOVrH_hRqWOCnbQHscK87dHYHJnd0Gnkrx2cCrAYgX5dQtZFOIOubL6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30398" target="_blank">📅 10:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30397">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698f9deb89.mp4?token=nvfbgmxrL4NjXuIuUelTfY6JWj8m2yxDFZIXYINzPwW77gd5D2rLVgEXAJAADTFbEPJLoanTCTtX5NorMa9GEUdOLy9DaIidtCiyZbkArcuyKYSfsMFzltnnRxl8V1Oam2EWjXooJbTdPZ2TsS6WW_DQ2uLkTtK95bV1eTX3xXAj6gOpdRKkbAuaIXu4PAZGueEnDXt9x_Dc2k8TtG1GlpAs3cAIUjSLSrNzWngJCeTsrhWePc09Rx_-jAo2Uzvo-x-13_i-xv7QiDnRcjbp5pVujQ6HIHrXiXf0H--EsMfz9ch6ZlJJEIJ-PLXFfCxC-swpEMtjQ2_BSHmRD2xaMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698f9deb89.mp4?token=nvfbgmxrL4NjXuIuUelTfY6JWj8m2yxDFZIXYINzPwW77gd5D2rLVgEXAJAADTFbEPJLoanTCTtX5NorMa9GEUdOLy9DaIidtCiyZbkArcuyKYSfsMFzltnnRxl8V1Oam2EWjXooJbTdPZ2TsS6WW_DQ2uLkTtK95bV1eTX3xXAj6gOpdRKkbAuaIXu4PAZGueEnDXt9x_Dc2k8TtG1GlpAs3cAIUjSLSrNzWngJCeTsrhWePc09Rx_-jAo2Uzvo-x-13_i-xv7QiDnRcjbp5pVujQ6HIHrXiXf0H--EsMfz9ch6ZlJJEIJ-PLXFfCxC-swpEMtjQ2_BSHmRD2xaMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین‌گزارش نیما تاجیک خوش‌ صدا بعدِ جدایی از صداوسیما در بازی شب گذشته آلمان
🆚
هلند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30397" target="_blank">📅 09:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30396">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XD11WodSUD8QGR34n4DEHaqaGnLYCR94Nous6ciOHN2O0N-IsVRy2FIwnjX5LgII9NyEUgAKsB4xtK7xj7smkrYzRVHBQy8XDAbL6rJHBHSjtzXROUxYp_A7Z5x3X3cu2bBoLQ0ZujloEROxywNRUY2VjAkhBW02mzUOnIcEMySmpNBwt0-lq2_LFiSH4yAZZyFStsZvIysW0SXL0U4SZRk7RAAu1dryKDy5UmDcNogza7xZxGkyc5qts2WeqDpviK31pZ8WRaSIT-33jf2TvkRLRejM7GDjgd-KGZGig1mW7ytOu_bFwEThgOeSlOYc_dPvldHw28Qux98FAyLh3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
گلزنی‌تماشایی‌کریستیانو رونالدو 41 ساله در بازی امشب پرتغال مقابل ولز در لیگ ملت‌های اروپا؛ این980 امین گل کل دوران حرفه‌ای رونالدو بود. البته دقایقی بعد این گل توسط VAR رد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30396" target="_blank">📅 09:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30395">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da1f2ad337.mp4?token=hoQbFphHE7kniR6rp9heuY9FC-iBDYLRaGGqEbJtmadxciF2d8AlQiprwy6oM8q0fNz9g2cZObTU-Otw_inDFQiJFHNghPO-jUS4XqVg-IA6c44CtrsYsEO-t-8nFvqBeRCnXI0kM0gn8YEElza3jPeL1iSMRdoDpMRAsDiEf9xNFKqg1rnLpjD2m2voMSvJ1udD55u9kytgW8oJld5xuPwIxWuzmOdCSGxi1YvyL1NDUiWFnrPiMkbj5wLSxhqGs1imGYLi5l_eTO40OqABUF3nQ6bWKWrxY75Da4AiceFMU2nUKAKMbG1mEGlV4-DVsMnOgyf9jwDWuGEtLEWkpADqR_wW8bM5T5Cmw8A0GXrAS9dVhTnA4GYhjW9AccQ_g5PhVKeSTlhKmW5ksTSBAaY9uXgGlXKrlfLo1hSLK_B6Xuh72SdXUaHFCDmqr5lkVbOgMz5MzvvRgGsH1eK1T66E1wUctkIxX8PbJiUR7WNeMmZqlUhq6NU013SREA7d_vLMyhBm9JJSJD1SEtm8w9tf0AJ6RegLeeCkUJ8lYuPgua8PRlD4Ov3tC0P2A2qA_ylPoDHBrjQliRyUq9iIR0QEa83ii2j8ocEL-2HGzmdmW_Hj_fgcFUoMwfUxg6yISLnOLthFv7B8d3pi0xEaI5CVb6ycVX3oLmVZW4HuHPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da1f2ad337.mp4?token=hoQbFphHE7kniR6rp9heuY9FC-iBDYLRaGGqEbJtmadxciF2d8AlQiprwy6oM8q0fNz9g2cZObTU-Otw_inDFQiJFHNghPO-jUS4XqVg-IA6c44CtrsYsEO-t-8nFvqBeRCnXI0kM0gn8YEElza3jPeL1iSMRdoDpMRAsDiEf9xNFKqg1rnLpjD2m2voMSvJ1udD55u9kytgW8oJld5xuPwIxWuzmOdCSGxi1YvyL1NDUiWFnrPiMkbj5wLSxhqGs1imGYLi5l_eTO40OqABUF3nQ6bWKWrxY75Da4AiceFMU2nUKAKMbG1mEGlV4-DVsMnOgyf9jwDWuGEtLEWkpADqR_wW8bM5T5Cmw8A0GXrAS9dVhTnA4GYhjW9AccQ_g5PhVKeSTlhKmW5ksTSBAaY9uXgGlXKrlfLo1hSLK_B6Xuh72SdXUaHFCDmqr5lkVbOgMz5MzvvRgGsH1eK1T66E1wUctkIxX8PbJiUR7WNeMmZqlUhq6NU013SREA7d_vLMyhBm9JJSJD1SEtm8w9tf0AJ6RegLeeCkUJ8lYuPgua8PRlD4Ov3tC0P2A2qA_ylPoDHBrjQliRyUq9iIR0QEa83ii2j8ocEL-2HGzmdmW_Hj_fgcFUoMwfUxg6yISLnOLthFv7B8d3pi0xEaI5CVb6ycVX3oLmVZW4HuHPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین‌گزارش نیما تاجیک خوش‌ صدا بعدِ جدایی از صداوسیما در بازی شب گذشته آلمان
🆚
هلند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/30395" target="_blank">📅 09:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30394">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMtFLKDBO2jKBsGCoX7Mf_TPdNgcKb3Iq1LLQ2pr3ixUqxQ8l35xwPDe0ISc-K3PAZs54v5ZHvcC2xBrmTbSlhNXhUeoMsa83X37zN9y-PXc9VPctUchwus_NJYkT3WHrmLVjbVWKE9QSDSAykyIfmP7Q8M9s76lBivptrOaUUSnBQJiS0TRMBGWU-c7E12FdzjoLg7amoCZ0-J6_It9EnXFqquPDM5D3kbuUAIgOlmx5YEzrrXGexRVx6KRl3K2hFUMlgqWHjObg8prD2J_VgBIFLdZyLwuw7PqCfeJFVGsCYyiMELJWuTdhge49i4q9o7UUhEV2EpQS3XV-hh4BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ حسین خان عبدی بعد از افتضاحی که دربازی‌های آسیایی به بار آورد بزودی بعد از بازگشت به ایران هدایت تیم ملی امید برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/30394" target="_blank">📅 08:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30393">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-H9PK64ILpCa_LrTf8f8j3JHBmWRawr48Y_8Syz1RQ_4tE7EQAnbp-icRy6H43zJbIw4jFb2zzw1i_rjCdNR9YSXF7QSxdd1gl1DMZo2TR7CssnU_QsRuaf6AWJcP8xA6lchVaubJYJQsV9weec-nGly25EQib0UcuEgDmuplDlXKzqPDcdI-XuzRoGfvbpU-COnnnRgIHD0NdcS1hrgAGNF-1dNfGFCvSeAeKojaHamOg5UiLBIvyKFtcqlk5l_LFt72-1nbXWFXuTsVnRUNpONLgUFwKo7AEKV4HlCug9MfHvOR4no8dDG0NuO9hOwRoR5xesyoMZz1gxtN-VbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ جالبه بدونید ازبکستان بعد از 6 بازی و 5 ماه بالاخره طعم پیروزی در یک مسابقه رو چشید. این‌بازی‌های‌دوستانه تاثیر زیادی رورنکینگ بندی فیفا داره. باتوجه به برد قاطع‌کره و ژاپن‌به‌احتمال فراوان در رنکینگ جدید چند پله سقوط خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/30393" target="_blank">📅 01:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30392">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57e45f06f2.mp4?token=fxuzgcK3NkgI_T3rrQIWOno7uM44VdaXBo9dtmwuttinBb4C2pSuDEtBplNk-tcoxpZJlJFv-lHwnc57s_81kqxau7l-4OXezdszOGW27isMinnHRbPYPW0QpK7SYKY-YDDUQT--mdFcGcfOA4dyein3TzwgGYj6n02Fv2h6zymWT1PM1NqqklebHDK94rvECtbWfMC-x_mWt3-TwV7lGeDZhlSqeVYsBAS0Bcae-C6SEGc9M9La2AOd7IxL_cXNUHBaO_DOFWMAVfr72fFMYQuJnYrdOToXPzpw8T1S-PZ0hclsZ5ZCZX4J7vvh3qVgYNGBRgJ0Fz3QsYYOKtfSXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57e45f06f2.mp4?token=fxuzgcK3NkgI_T3rrQIWOno7uM44VdaXBo9dtmwuttinBb4C2pSuDEtBplNk-tcoxpZJlJFv-lHwnc57s_81kqxau7l-4OXezdszOGW27isMinnHRbPYPW0QpK7SYKY-YDDUQT--mdFcGcfOA4dyein3TzwgGYj6n02Fv2h6zymWT1PM1NqqklebHDK94rvECtbWfMC-x_mWt3-TwV7lGeDZhlSqeVYsBAS0Bcae-C6SEGc9M9La2AOd7IxL_cXNUHBaO_DOFWMAVfr72fFMYQuJnYrdOToXPzpw8T1S-PZ0hclsZ5ZCZX4J7vvh3qVgYNGBRgJ0Fz3QsYYOKtfSXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/30392" target="_blank">📅 01:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30390">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYaBwtTYZxTqwYXmJVO4qF2PMYBX83VtcICOgS0tOgxB845An6k5EVowVM3b6-xyIXd6UXodQCADGFdXt2o4oDiFa_tv2lhUb9LHggP5rabeXPfO2aXYawni2MXwV-ZR3dKgtVibPjrQBGuVbIjZViKY-1L7NcqmNhogV4-n5O1uCQFJavpAR2sq4vXG-tqcY29p7fiuhPbCjrV6bf31wiI2cb-5aysUt1O2_qYYqLWuLkMkn20un6pwI44jLv0jkkJ5jwE-6f1tC598vlJ2ZbdOqhjJX-HCTGzYiWmZgMZmwYQVbVymiLABrBt-RBvuIrZ0oOu7zZ8kOA6ZplSLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ ازبازگشت زیدان به عرصه مربیگری تا نبردخانگی لاجوردی‌پوشان با یاران کوین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/30390" target="_blank">📅 01:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30389">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mP5OiuakhywOGIHhoChw4R6GL1syh9A36ipjdXn947UeYLlcQbeDRoklD9gctWmKt-Z1sA-AsO2atjao816DzGvZ7gjEQahWAPXRZNbwi_LqrhavkvOKL_YxWOo7phgiA2jt_oosGUI7v8bugfkbf9NHrnCSH-7W7iql9XxSYHi2Tv51uXVzZXHWg8X9BjF-UTebIrMIvEE5YL_XVuv4_egPgDRxOIsGbE_dHb0BdTFS6Id1DdizmYTEsYqLO2ABG-7DjtTC25U_XwWujIQdLLXK1bq3s6c1kpwdnFFCO8k8IUlJPEaxltkaFbwads0xOJFqRuzRo6s8QKvEN668Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
ازتقسیم‌امتیازات در تقابل هلند و آلمان تا برد سه‌گله ژاپن و کره جنوبی در شب شکست سه‌گله شاگردان امیر قلعه‌نویی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/30389" target="_blank">📅 01:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30387">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xzmo-0zOLZPH_2fj1SO_gCCMOLnvVtSsK3tZy9NF4f-Z6utrRrdrgWbjzrqpOdxPBhnnSK0OTg05NHCLuedVBtcEk71zfVAtBLuMdGxB51TajtkuqyGPG2NE4Jt8nDkqYQ1syXCq_SeiLa3O_Dhff_wdvlpxS9JAA_rOue_17o819i5BgeetQT1nqi6g66BG6g9aeZUoiIRR53cpLs_bMtpPIg5AOnqU1sKEjIug43TtZmW7GMTZWCh7pI-zxydEBoBL3lbvexGH-MaGtJTa6EK43bOqnxEN9kXBvTyj_itpbyKLlb2LpOBQFiSzMuSMjd3SiuyJ0ZL1fR1I_sC-wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق‌شنیده‌های رسانه پرشیانا؛ دو ایجنت نزدیک به علی تاجرنیا رئیس هیات مدیره تیم استقلال از صبح امروز تماس‌های خود را با مامه تیام ستاره 33 ساله سابق آبی‌ها آغازکرده‌‌اند تا در صورت عدم موافقت فابیو آبرئو برای‌اومدن‌به‌ایران بلافاصله مامه تیام رو…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/30387" target="_blank">📅 00:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30386">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AypLGCRBsUbwxrdM68SIh3VCcA9JP5p9UEWWzj3fVIWcOQ9yVm8KRapwXBrna3GMFVYwO753_dPazm7Frh1FuYH0B5Xdng1JWZGIq3-skIXqdAgAuSRqVqZJNfHiAdEn3b341eD9PF0WMbH1o2z1Se8S6oee9piAoDKRwa4hHGEy4k5lMrJBld9wA_LJ2KN5hUJw2-2mApWdgmggXWh7Y1Ji5sATFU4huCjWuMSJ_Z5UNFomDY32nnA75G5HrHD6hsk7YgqeZMtFnCMh1FeUGg19eiS2pVn6YUgyI7AZt6j3pToi9rtu88o-siHsPkTBW02juduYOu_KlWNKo2Qf2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
گلزنی‌تماشایی‌کریستیانو رونالدو 41 ساله در بازی امشب پرتغال مقابل ولز در لیگ ملت‌های اروپا؛ این980 امین گل کل دوران حرفه‌ای رونالدو بود. البته دقایقی بعد این گل توسط VAR رد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/30386" target="_blank">📅 00:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30385">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8FvtKPR0DPkT5ykMLzP9BKXya67p5chAkdX5d84LdctDYiMvqyued15KoooSGUJ0SfB-Dl_V_J3H5hBMEwb91Gx4w1VadoD5IYt0-wOQMcyqjKp6DWZuGw7W0MT2JNR-y2mQxqli2oaOOwpAnUfGd5Tmn2lYBzbTH1qeVV9LMXcqg_eW-I3XS6b21kaavpYYMPdn27mMcYLABlYJqqFVzrVQYP7rSGk7kgJvxxSnw1-K00ILVyOGZ9IEjjVm2WS5qYOoxp6xnNQVUaYOObY91IZvHJSjJ0mtZC3w-2l8Rur7EfK6FtmOs3R6Lb7El_1KQzXFKjDFugjQiJw4Dy1Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
گلزنی‌تماشایی‌کریستیانو رونالدو 41 ساله در بازی امشب پرتغال مقابل ولز در لیگ ملت‌های اروپا؛ این980 امین گل کل دوران حرفه‌ای رونالدو بود. البته دقایقی بعد این گل توسط VAR رد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/30385" target="_blank">📅 00:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30384">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fahhyJ1pe1atYpJ7ysmZ83SyPV7a7opQM8PqcBWAxvW-pwRccpH_Xa77C93a4Sn7Xguohz1tadsCJCvyejxVrkSG3IJU8nqrxP3WUG0a2QEf1nzn6V6ah1AEmYbm1faRW2sCv5ICKtT_72250oKV9jqtJQRXw3fxbIDFnxn2ap0MMWfqZ7Zwo83H4YkQKfpQx6CXkxNEcdVIwORsezF5rnvWB1J4XcdzqnzIFnmmHjtBBTBYAm62_52Wvfi81XnqNDf40tbpXPj9VLEsDH-wPmMY-IO3zod3k7JQ0-1jInRoPfkcu17Td8eLDOxmCTN1gxwgAkofREuiQJ_v5v0HDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
دو لیست‌متفاوت از تیم‌ملی؛ لیست محبوب امیر قلعه نویی
🆚
لیست‌سیاه‌امیر قلعه‌نویی رو میبینید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/30384" target="_blank">📅 00:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30383">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeeiVlNQMnoKNxchzUiXVANu13czJ-hXfNQG2jg1_2hj6LvzZg5gmRkF81D0LPAFVmyvtPTtMQI1xliZH4XVCKj6tf6FQir5_VH_dn1P3LLb3IoYUmNb_1Km4rBhMLgxrsSml8J7zuZ3yEU42TnOERzfornFApHchwacBiG7zPrQE6zPybJumkPRC17s70Wss3jRhN1uASuz6O6HQ-dVwS_ZtQcUaxrq2tNks7UlYcw-AY71br5XZqUzDs3sNjo3bZLQ8cg2weNW1czp_-4lfDhUIGNckSMTUmCeNIat4DWNSIhG20PJ7AaSCrPqAa-N_ujca4oo4-chZ9T3KR_uyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحبت‌های تند جواد خیابانی علیه کادر فنی تیم ملی بعد از شکست عجیب مقابل تیم ملی ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30383" target="_blank">📅 23:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30381">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56e908efe.mp4?token=Hc53mfPmZMRHhWaStWG80AsqFeoNCgFge17fWo6cXyovgI2XnRkctrLAhtgUYxkM6mFWCG0vWt2YC_FR3lErpxtICQt0KDSHoNg2ZGTq1-KhnZ-wNbzVB9nPO2iMz8ZE91AZty775j0komZ_4zH1QisJxUmg8yF_830S36asWh8NmsUe83J348hyPv3daNFgi5xA4mXOtXOY0265zlxbhItAFt-y1yH4wM-gzDU9A6wXjGZJTZStMetk58lLnH8LxldMhNNRQHobuCrmxq4gxL-_rzE3yEyDV__wiRvErgz2Nswn4C_LzhdlU2p9TJjlNb0vRRlNsmgh0CgU0L1_Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56e908efe.mp4?token=Hc53mfPmZMRHhWaStWG80AsqFeoNCgFge17fWo6cXyovgI2XnRkctrLAhtgUYxkM6mFWCG0vWt2YC_FR3lErpxtICQt0KDSHoNg2ZGTq1-KhnZ-wNbzVB9nPO2iMz8ZE91AZty775j0komZ_4zH1QisJxUmg8yF_830S36asWh8NmsUe83J348hyPv3daNFgi5xA4mXOtXOY0265zlxbhItAFt-y1yH4wM-gzDU9A6wXjGZJTZStMetk58lLnH8LxldMhNNRQHobuCrmxq4gxL-_rzE3yEyDV__wiRvErgz2Nswn4C_LzhdlU2p9TJjlNb0vRRlNsmgh0CgU0L1_Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول لیگ ملت‌های اروپا؛ ترکیب تیم ملی پرتغال برای دیدار با ولز با حضور رونالدو؛ 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30381" target="_blank">📅 23:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30380">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmpMBHu8Rd4xGv-aqoypicbZhCb2lJUfL4HM6RaMuG59G8ReKo_VXhjdRx-Nw4HZvOMhcifo9dhp_vKJbrWc3qsfW4whZBbQu1wuRXibOQ6Tu6EC_6ixizQi9qWwBIrkgQodZJSjobzbKx5LweC5m7ozBGG2YtqSqpREwok0Fw7O6l7gVA3iftnYA1INztndYOrDZon00l0ktCvLPRLSmKn9tc0qEcV3pRs0EBz2irVX8QfeomjxhFFi4J4VOxXoKbuD2kW1yByO5glJqDZ3o-FYenRfflmgMboisnh6IedDIzVYpOq1a-6TnHW2HOtGiidcmq9U3yo8XkyppKbRWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ابراهیم کوناته مدافع میانی رئال مادرید از ناحیه رباط زانوی دچار مصدومیت شده و ممکنه چند هفته روبه دلیل مصدومیت از دست بده. مدافعان تیم رئال مادرید در حال حاضر: هویسن، آسنسیو و رودیگر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/30380" target="_blank">📅 23:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30379">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEdpEDsCWwnGBuzRphZUZuLu2s6C7VL8YZxPHj4sY06TlpEx47ugod8Y8hsrfYw3xfETfOF67YzITNTcf7DhfwutXIaXJIrKsgrAOn3vNUwZ3QJUesLjvJxlg3g-H0JF3K-wXxgJDwAs8SoAXgEGA4rJDBrrNSxWqHRhzrDK3i3lNGWS--6xDo4RiTcQj35xA1RjLOEbXQIGn2mG1K0kxAW85TLvLYgmmv2SH70LIE9libbQS56XK2dZXClRjjXyc5bDQzv1awbuH-g3syDmCbkmYlZqcvoEhi5fqZV6SJfLHc68NZfirwRRJb5pTBhwsHLc8WGoafkHsH7LBHyeYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اختلاف برگ ریزون دستمزد مردان و زنان در مستطیل سبز؛ دستمزد کریس رونالدو در النصر 142 برابر بیشتر از گرانقیمت ترین بازیکن دز لیگ بانوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/30379" target="_blank">📅 23:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30378">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRstPOcY1Z--aabZdyXJdkuGei_xT6yYBZt1bhqC_Zp1YxwD0nVbXp7_u0vNOE6eMHNwHsgj0JbtYbG59MlfRoc_bwzfOtQLg6e97X9_3N50zdoQDxFnHbn1T9slwBUzty6hCVSllcQE2WGCwac1f3LxHLIIcrp3rPW-ECiqAQetZiktZGYdPsvid-MjrAGWqNQtJXQ-C1vq2cnp_HgInf-gIKIbix5BpNHQkCg7sChtVN_Kqe1QcTQ4I1k0gn3ym2HVrs4k56WY9eUxAC9TSWSv97GGzQOPxCmQaKwSqGE35L5NrYnaJQDDX0NtcZvcaPzymSGD-Xx9B0BUVXPtyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌برزیل‌فردا دراسترالیا به مصاف تیم ملی این کشور میشه‌. حالا اعضای این تیم به محض ورود به کشور استرالیا بااین‌استقبال میزبان رو به رو شدند. همشون زدن زیر خنده‌. قیافه آنجلوتی رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30378" target="_blank">📅 22:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30377">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af2ff5c23.mp4?token=FB3pFNKYRx86oU2haMu-wIGzvJnI9oWiex0GYBxFpMsu5rQAkkKqKFpTQuYK7Q1pHh09z6auiSDkk6Ebe30YSMslNiXQL7KfskcpBJe5oWpneEH45sG-sfjDppdW7G7KKW2bIYW-LNOnmKArVhRA0OTJSqcJMZkANdzgPhZashKT3O6lC2A-dGlhYW3Scih1q9cv95DZPLgP27c0YnpbZf_gwMMbmpXNLyh_jUl6p3v2v_PmDAeAdZi0iIX5GYlA8JHZfQDjr7DMwbsz080bxtvRGJiNanfVMmX9L4N3xlf4QHJeq1tHEK3FjYdJftiSM0A6MTboD8lAv2-I2Z65LbQYeNwuXSllOazYeLfRZziD9mZLB2XWeccfDD-iAw08YiHosOTREk6uuhSO6f_l-5MNAi6qFzlK5Q2LPKXCnjVQkTlBvSmgA9XQKBgl5pJjNVZ3E2sy6w2mWDOT4RYyYJH6dCRgVlE6EZRdt6FM3LeH6f8okFulHTR2t1P_w4vuxHc5uzN2Okgbfm0dDZNm24wx3B2eWebzwsfklHdRGs9bu_N-xYBBModBPMIbT2Iuyu9b2dZmhw_eKgF5aB0O38S97THZO-2-b8ETqLhuXaftCDmP4n1j_Niwkwa-IGpacP3LMEEBx31uh-f40xFx_-LiPaosxj54MFOnfzydAWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af2ff5c23.mp4?token=FB3pFNKYRx86oU2haMu-wIGzvJnI9oWiex0GYBxFpMsu5rQAkkKqKFpTQuYK7Q1pHh09z6auiSDkk6Ebe30YSMslNiXQL7KfskcpBJe5oWpneEH45sG-sfjDppdW7G7KKW2bIYW-LNOnmKArVhRA0OTJSqcJMZkANdzgPhZashKT3O6lC2A-dGlhYW3Scih1q9cv95DZPLgP27c0YnpbZf_gwMMbmpXNLyh_jUl6p3v2v_PmDAeAdZi0iIX5GYlA8JHZfQDjr7DMwbsz080bxtvRGJiNanfVMmX9L4N3xlf4QHJeq1tHEK3FjYdJftiSM0A6MTboD8lAv2-I2Z65LbQYeNwuXSllOazYeLfRZziD9mZLB2XWeccfDD-iAw08YiHosOTREk6uuhSO6f_l-5MNAi6qFzlK5Q2LPKXCnjVQkTlBvSmgA9XQKBgl5pJjNVZ3E2sy6w2mWDOT4RYyYJH6dCRgVlE6EZRdt6FM3LeH6f8okFulHTR2t1P_w4vuxHc5uzN2Okgbfm0dDZNm24wx3B2eWebzwsfklHdRGs9bu_N-xYBBModBPMIbT2Iuyu9b2dZmhw_eKgF5aB0O38S97THZO-2-b8ETqLhuXaftCDmP4n1j_Niwkwa-IGpacP3LMEEBx31uh-f40xFx_-LiPaosxj54MFOnfzydAWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌برزیل‌فردا دراسترالیا به مصاف تیم ملی این کشور میشه‌. حالا اعضای این تیم به محض ورود به کشور استرالیا بااین‌استقبال میزبان رو به رو شدند. همشون زدن زیر خنده‌. قیافه آنجلوتی رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/30377" target="_blank">📅 22:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30375">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gmzqwyHHVg7QKo1azpBW-FhFQlBVk6JKLgYraGM21s7Ne6jaiUDX2mGnzeqFnni6LsqOqqhGPuI2hHiiCV3XM6I1ODir09PguNtK_KYnuxtzRMNbmvbIQ8gT60k4BY8fb1iMb70BvmUkZfl-kAYbvCEu333E6D10JJU8YD0zlNVu6oFTclmq6w-GwEbn-SnhnG7M6OXPuxija1vJCpP628XggnaJFq3BjpZZ7VKh2HGjG9qj5MzbevFrQSWmay1tMYAV33nugfHiAdJf1yqiJogbkc7aEVrF14LaLl_FBwmiZJrjAR2KS3VyxQOHMjfQnuh8YRQLHYd3WVb_N3xuHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WpO-DUyFtCVSLNSCiyYacatFGQDlJUF9N5H-fljGVXqmzm979mQGMuqx-Y8-iaoguDrdMX9n9LOXVCX5cF0LLhhYcLZiKflt7MHsqM5eZfIZbLe3xttbHSbQRlofY50rDd9erw7pZr2iKI90tK6JRvqLTahwzYNsd0PUcNlq02LP5ICSXh8b5maBf6oMdINSV38OTmIQIBlOPc7qIVZWIGybeYBd30y0yJ_hoSV1d3yS0cb6XewKlRMqi3TELcjEEm2jkaKRRop76mP75CQsxjT4ZmlUwjSv7f_qnHOtH6L5B4wGy6NbzrS1_4w7pHL2gf8OIwNf9C1VuwArlOOMew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول لیگ ملت‌های اروپا؛ ترکیب تیم ملی پرتغال برای دیدار با ولز با حضور رونالدو؛ 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30375" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30374">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBTiHEzkHQNPl_N0Zr6N_MEgekYEYSyXKXEPwMR49nC97Tr6gb97fQeMXSnH5NGltOUdVHgOu8qxpSaAtMnS60fDbsmcrxJQbUXWYRDJNdPEQY2YsmeoVDEdSQrW1klDkXU0udsjDYGFV2XevbkTU89iLUEePZoXx1drEdV5OwPNSgrwiYyidqulckHrcdLASSXsQ7hbZuMCIwWrA7NN9KLhTiTqi-VBzmc_O3a43Xjg28BvkryGTqgDgWV7uIaItLibLM4DAx_6hg2ltihCv_UJX3PKiZOuef-_ia8U3jDBGX0wCYTn3zx3Ux1zitkry4BiLQKeflqUGrvO9YLtuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ گزینه اول باشگاه استقلال برای تقویت خط‌حمله‌آبی‌ها فابیو آبرئو33ساله است اما درصورت عدم‌موافقت فابیوبرای‌اومدن به ایران در این شرایط خاص؛ گزینه‌مدیریت‌مامه تیام است که‌رابطه نزدیکی با حمید مریخ ایجنت یاسر آسانی نیز داره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/30374" target="_blank">📅 21:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30373">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uT_FwqEsCumg2OzL83MKlsXUSnltyVOohzqC29LNXwcc5olgNKxXtlVKKm0uUpgIPzEz6F3eyp_8O3Fv8Hs8RS8pUP-4WU0ubdopoN-k6d9WB3m4k-SOfVZJ1KWaPBKxu_kHq8XJxVBCfcy3RjIiiWKJQwVyfFJqXgM_CBZcp0euYeWThHl3ytGaSlTtf8MX-g4Sd2KwKdKt6BvADPTfqXJBCu6Ux_qa-Sh3VQB0EyGaN3YnQNPUDWjDEfCngn-Z-i8s7rmg0bU95iqhZHowEakGIOG6Sei2xLVOIFDXTItOV2lUpROzXyte99wkhjDW_algDI0DXB--l1aM9ZcfcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جذاب‌ترین‌مسابقات‌ملی دراین فیفادی؛ به هیچ عنوان این هشت مسابقه دیدنی رو از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/30373" target="_blank">📅 21:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30372">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🏀
پرتاب‌های دیدنی مژده نظری ستاره تیم بستکبال بانوان ایران؛ با دوستاش شرط بست 200 دلار برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/30372" target="_blank">📅 21:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30371">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‼️
صحبت‌های تند جواد خیابانی علیه کادر فنی تیم ملی بعد از شکست عجیب مقابل تیم ملی ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30371" target="_blank">📅 21:06 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
