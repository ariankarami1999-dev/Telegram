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
<img src="https://cdn4.telesco.pe/file/RphuTCfrxuxxe6lK-0EJ-_tqfcS_xT4QZ6cnUajj8RB4WSj2cLqX2mlmeFTMYkzS2Qisd8bmt1_IeHlbcGrLxjigrfNEvuaYQpdGvP3TNpwK7Gpbit6vnQjQNmMqNOwmblgTt3e7RqnTtgBovIbDkjXjdnSVaZ3G1-ND6_d5_jz-bIwtEOwwgVKjFPsXQLRrM-D5M-S6kLOInxOhWSXRblQEHu8ipkd_xzLRv0p-Vg5wv3cbHD2Ar6yJ60yjKUqLKAmkoF-G8exAyIZdl1UqZr-VEJzq6K9zk3npqgsY-zuXhlFMZ03ud4ywOwXnvUzpbYvrUPe0nWmMgqXpXqCaLw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 00:05:52</div>
<hr>

<div class="tg-post" id="msg-446469">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuM2jXl1NB8e4emNYnbSdFHG00tmsFX3VKEShbWdpnPiAoRcxSdn7lVKIhf4quenhT3BwpAWXne-KkJpIhLR6LqEMcE9CudFXTEi4XIcfSdw3edfm9otYnZqPjcGzvX_lTsBLiJp0_ApT8Tq5-wVuQAjXTqRbIhFxYxW_DDEmkamnTv9bHdLPiTN5psbNJzdmkeYBTHB64CryAlczOS_ETgB6JV2pTo-2vaZIeC_nc1cdLUpTyxi79GjWWbvKBwX4UtRMWeR3VerrI2m_6k8Us7gBGpmLHTeNGXMdoZwSELhQftZx_3bEJLtrpqGDGikJIdOkdMge8FNlJdKPBruOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخت خرما
🔹
روزی امام علی(ع) درحالی‌که باری از هسته‌های خرما همراه داشتند و در مسیر با یکی از مسلمانان مواجه شدند.
🔹
آن شخص از امام پرسید: «ای ابالحسن، این چیست که با خود می‌بری؟»
🔹
امام علی(ع) فرمودند: «ان‌شاءالله، درخت خرما!»
🔹
آن مرد در آن لحظه از این پاسخ تعجب کرد.
🔹
مدتی گذشت و زمانه سپری شد. روزی آن شخص از همان مسیر عبور کرد و چشمانش به نخلستانی بزرگ و پربار افتاد. در همان لحظه یاد آن گفت‌وگو و کلام امام علی(ع) افتاد و تازه فهمید که منظور امام چه بوده است.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 611 · <a href="https://t.me/farsna/446469" target="_blank">📅 00:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446468">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ada85a1d3.mp4?token=bisy9gNpFAp7QHREpr4BigOwS4ikfcpSDQ1_csWftzWf1SC78Y1dm0_voN4yUCiGw0uBT4kQ9IWXmRXfVX3e7wJZ8ByHngAYIx_XerSEks5v_bbIs6_l8kuEenmwCIwbYZUif6Vv7M9vtw7Bf8xLEE-ouYCi1CXf3FUwMZ9Q9mSiWhllXAdGgwmTpYsynP_gwiP0nCaXj44h02S-R2tf9wVB_I3cS9x1GMKgBkMz37O_fGg8khbE-60uvNTSKByUbrwrl6NHMYeLuLSXEc0F59z8vyIOefTwv_N-SSmA0CvTCjU7ExYHkgKF16DVoYoZE4z4r0Kg1JtyZYuqB2vbtT1SRDW136WSfAO5VfYLV-bSfybPRhYXegafg5O3v17eFPngwbBhKtvMFcCu7qNGdJXoigALyKFIVC7GUwwuOkNKvpPg6yhBRW-MPFSyySQ_sUh3fXhgtTkQZaSjoTahyJ7J2rXkIS3rwSXZN_U07OAhBThsM1aaHb3ssEp53TqLvtslhJz116sGyV-DK3scTubu88EORGeWmgnYO4jg6K1nd4--RiJ5NK10pj03_6OVX6cUGFtehrCinWMMbdJHCLzLS90q2Qz5SXYXLOnoF0mCzOTGcwb1lP0RBnoGbsxqoWwN1wO-jS3VHetg3z0FT_jnBM2J_YlmVLVHviMr06o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ada85a1d3.mp4?token=bisy9gNpFAp7QHREpr4BigOwS4ikfcpSDQ1_csWftzWf1SC78Y1dm0_voN4yUCiGw0uBT4kQ9IWXmRXfVX3e7wJZ8ByHngAYIx_XerSEks5v_bbIs6_l8kuEenmwCIwbYZUif6Vv7M9vtw7Bf8xLEE-ouYCi1CXf3FUwMZ9Q9mSiWhllXAdGgwmTpYsynP_gwiP0nCaXj44h02S-R2tf9wVB_I3cS9x1GMKgBkMz37O_fGg8khbE-60uvNTSKByUbrwrl6NHMYeLuLSXEc0F59z8vyIOefTwv_N-SSmA0CvTCjU7ExYHkgKF16DVoYoZE4z4r0Kg1JtyZYuqB2vbtT1SRDW136WSfAO5VfYLV-bSfybPRhYXegafg5O3v17eFPngwbBhKtvMFcCu7qNGdJXoigALyKFIVC7GUwwuOkNKvpPg6yhBRW-MPFSyySQ_sUh3fXhgtTkQZaSjoTahyJ7J2rXkIS3rwSXZN_U07OAhBThsM1aaHb3ssEp53TqLvtslhJz116sGyV-DK3scTubu88EORGeWmgnYO4jg6K1nd4--RiJ5NK10pj03_6OVX6cUGFtehrCinWMMbdJHCLzLS90q2Qz5SXYXLOnoF0mCzOTGcwb1lP0RBnoGbsxqoWwN1wO-jS3VHetg3z0FT_jnBM2J_YlmVLVHviMr06o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل عاشقان آقای شهید ایران پشت درهای مصلای تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 985 · <a href="https://t.me/farsna/446468" target="_blank">📅 00:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446467">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjwOIURE7aLdG0JiAWNtYFxC67XBPS6kKZ3APif7xmHZpcnendQGPXjz3F5z4q0q28psT-2Wsx5sbpUXSvUbIyk7apC3wycSaB639NZOeHVMsObKsONXW2rDBUQDaxcnSIlH11v0vCfaZLVvzXlkuaKDkh7Rm3ayoDdmCrbIXIOD1h7R3NU4Ji8PJjiGRPoxbkT0AxFd_ywq2lDPjiphW81XZU4Vg54GsOk_AvXskV6GWjHhhzZsSvLj2ltN1VB270ZY0ijX751P4Yp1MUiaKXulIZuUONdt__cPzITMRRLzwLgyNlhERNmMV-iBz4Kq7WjSIg6Hr18DzDnR6W0Wxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
| شنبه ۱۳ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/farsna/446467" target="_blank">📅 00:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446466">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jC4-eEELaJkN45kKOYOHF5Vn3KLPGpVOVooDStsTBOHWiHoAS8ji9ur1SPc5ZCwl5-zeDRcwhOsDkCzHQWwR2Of1dL94nfnY1n9p6Ss7N5qsYtt4kCVwoTeoWjZmfyxoP1yFU4lZUjHNSKOikH1qYQsSur3CYLOlHP8cpu6nypZsIyagQNE05MgyXluVGlmGZFEX6sFgX4okrYWmydmFSq0s_YaYxUbZXgio4vQYORzkHA0Wsb-lR-NdxEiKfadFnQ7DT78mgltPcDlu9bYhr8dtpQQVekQwSExYDQ60l3O_Sd57gRnVTxJQ9gJ2XXwjEwqWj8ycL1ErsKdFEHveNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاه رسانه‌های جهان به حضور مردم در بدرقۀ آقای شهید ایران
🔹
تقریباً تمامی رسانه‌های معتبر و مکتوب بین‌المللی اخبار مراسم وداع با حضرت آیت‌الله خامنه‌ای رهبر شهید انقلاب اسلامی را پوشش داده‌اند.
شبکه سی‌ان‌ان
🔸
گزارشگر ما فردریک پلیتگن از مرکز تهران گزارش می‌دهد که انتظار می‌رود میلیون‌ها نفر در شهر پایتخت روانه خیابان‌ها شوند تا برای رهبر سابقشان سوگواری کنند.
شبکه الجزیره
🔹
مراسم تشییع آیت‌الله خامنه‌ای قرار است به نمایش وحدت ایرانی‌ها تبدیل شود. آنچه آمریکا و اسرائیل در جنگ علیه ایران انجام دادند نتیجه معکوس داد زیرا حکومت نه تنها سقوط نکرد بلکه قوی‌تر شد.
یورونیوز
🔸
در صورتی که برآوردها مبنی بر حضور بین ۱۵ تا ۲۰ میلیون نفر در مراسم تشییع رهبر عالی ایران محقق شود این بزرگترین مراسم تشییع در تاریخ ایران خواهد بود.
ایندیپندنت
🔹
مراسمی که قرار است برای تشییع و تدفین آیت‌الله خامنه‌ای برگزار شود از لحاظ میزان بزرگی و اهمیت آن در تاریخ نمونه‌های اندکی دارد.
آسوشیتدپرس
🔸
آیت‌الله خامنه‌ای به خاک سپرده می‌شود. او در بیش از سه دهه رهبری خود ایران را بازسازی کرد و این کشور را به یک قدرت منطقه‌ای تبدیل کرد.
الجزیره
🔹
پیکر آیت‌الله خامنه‌ای سرانجام در شهر مشهد که به دلیل میزبانی از حرم امام رضا مقدس‌ترین شهر ایران است به خاک سپرده خواهد شد.
🔹
خاکسپاری در نزدیکی یکی از مورد احترام‌ترین شخصیت‌های مذهب شیعه، افتخاری بزرگ محسوب شده و بازتاب‌دهنده نقش آیت‌الله خامنه‌ای به عنوان رهبر سیاسی عالی ایران و بالاترین مرجع مذهبی آن است.
خبرگزاری فرانسه
🔸
انتظار می‌رود این مراسم بین ۱۵ تا ۲۰ میلیون عزادار را به خود جذب کند که آن را به بزرگترین مراسم تشییع در تاریخ کشور تبدیل خواهد کرد؛ قالیباف این رویداد را «یکی از مهم‌ترین لحظات» در تاریخ ایران خواند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/farsna/446466" target="_blank">📅 23:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446465">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a79a851cf.mp4?token=HFkJmGvYyt-mIULvsolAu52RR9PfwUxJRMByfIYpa9uICLuQ-MD3ZTRgRl811ihqNvpI8upeWuuGZcbJcwhOLIxC2FAznTbWO3cB-YY-XWpRkOzEPv-Mh_vb4bN8dPvGEKG8Hkb7SCkTyHaCJWNNVYvp4ez4R516AFstV1JbJMy4x1sMQd3Yu_wB75Aq8Hb9vK-VP33MT9SAvjw7LZi22u74mcRHVZkxol0NdIeEmFh44zOozorJAz75w0vPJuS4KFr6KDxoEKrrsIVSRMcTBL7M8S9oSrbZbC_nYdk_x5rwcT3N5EZig_1OvNu1cJwBLkkN4MXxRBl8m66q7jvD71F2pBPiVOQPMqbZALC-yXgGgOnF5xzKSGGH_X5lC3hbJVtwT9e6RbWwAIYeCUDSuCizDvoRb6qqzncB-Oni37Ie8K7k1cCQNGpssGnOptDeEv3JybRICty3PWR_Y0TEzVV2oaycL_QcPAwPsQvBTYLXhaK_OOkMDupBq0zrGjohKx9OHD7ePVB-0-akdJe8TRFVBITtxFAGlhC5kaKhc9iX8RVwC3rC1cYJ64-cTJ4Y38F8O2y2EO9uNX3pKlnXL7CAHe2ocJ-4nwl7PRYAaIfE4KXu_uIYL6KqqqAlzao3_I83XdaED1gbTFWU5LMQSlqpwpA2dAM2_NZRvqXZxuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a79a851cf.mp4?token=HFkJmGvYyt-mIULvsolAu52RR9PfwUxJRMByfIYpa9uICLuQ-MD3ZTRgRl811ihqNvpI8upeWuuGZcbJcwhOLIxC2FAznTbWO3cB-YY-XWpRkOzEPv-Mh_vb4bN8dPvGEKG8Hkb7SCkTyHaCJWNNVYvp4ez4R516AFstV1JbJMy4x1sMQd3Yu_wB75Aq8Hb9vK-VP33MT9SAvjw7LZi22u74mcRHVZkxol0NdIeEmFh44zOozorJAz75w0vPJuS4KFr6KDxoEKrrsIVSRMcTBL7M8S9oSrbZbC_nYdk_x5rwcT3N5EZig_1OvNu1cJwBLkkN4MXxRBl8m66q7jvD71F2pBPiVOQPMqbZALC-yXgGgOnF5xzKSGGH_X5lC3hbJVtwT9e6RbWwAIYeCUDSuCizDvoRb6qqzncB-Oni37Ie8K7k1cCQNGpssGnOptDeEv3JybRICty3PWR_Y0TEzVV2oaycL_QcPAwPsQvBTYLXhaK_OOkMDupBq0zrGjohKx9OHD7ePVB-0-akdJe8TRFVBITtxFAGlhC5kaKhc9iX8RVwC3rC1cYJ64-cTJ4Y38F8O2y2EO9uNX3pKlnXL7CAHe2ocJ-4nwl7PRYAaIfE4KXu_uIYL6KqqqAlzao3_I83XdaED1gbTFWU5LMQSlqpwpA2dAM2_NZRvqXZxuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دعوتید برای «سلام آخر»
◾️
از ۶ صبح فردا تا اذان مغرب روز یک‌شنبه
◾️
مصلی امام خمینی(ره) تهران
@Farsna</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/farsna/446465" target="_blank">📅 23:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446464">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
آیت‌الله بوشهری: شخصیت علمی رهبر شهید، منتقدان را به مدافعان ایشان تبدیل کرد
@Farspolitics
ـ
link</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/farsna/446464" target="_blank">📅 23:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446463">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‌ بغداد هم برای تشییع رهبر انقلاب تعطیل می‌شود
🔹
با اعلام استاندار بغداد، پایتخت عراق روز چهارشنبه برای تشییع رهبر شهید انقلاب اسلامی ایران تعطیل خواهد بود. @Farsna</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/446463" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446462">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAZ9MTChmuUmI6cXEEYd857dmts23c9fj-YkJl7XPYq23Uc1qg3dSn5wh5S0O5y_kiHlQhpu2qTstql0MfYaFHjAS8PG0BMQ1_woLbMuk-z8ZtPQvuOZecV0RzpMkmhQcC_dB9F836ohbG6xHLitpWgd7qWyXmrMbW_nRUrkmx5d1Q_8C8HDaBZu2ocwSz1BFprttDQWFBjzY3c8v38Vchy4vvOAWVuyFHmdyM--35x2fKkmZoSBEQWZlipNHtrovV1GdPM-gInT3N6dj0yIIj2BqqfdwvV9u5K3TnCBDqEl3TK-SX8mzXrvBSiHOMg_WJSV_Mx2kAXgt1BZ-Q1muA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از شعار نوشته‌شده روی موشک عماد با سرجنگی شدیدالانفجار
🔹
رزمندگان هوافضای سپاه در آماده‌باش کامل عملیاتی حس حضور در مراسم بدرقه رهبر شهید را به شهرهای موشکی آوردند و شعار
#باید_برخاست
را بر روی موشک‌های آماده روی لانچر نوشتند.
@Farsna</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/446462" target="_blank">📅 23:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446461">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a350193e58.mp4?token=hJmTfo1I_WA_7PphnkaFtJ1daW8W3ijAgZ32KT8MnbFCUyvVPCN8JCA2vlPrSXVNcWtjgY4Lzx5CfvKxf0zG20BImkDkgf3YBYjPsF3ms-QSgYU5sKuQK3H7zDpeR8b2FHt8nTmHdgh95JB7Z_j3xNDRBIF_yKhi6YFeRCJDN9gpMWxjymSnkitg_6hOk-3q6lrhh5qjzaHBG4ckJBQGsbGL8rpDptx3VHzCtfjWIfq3Oo5nqt0mzoVIM4BPv8OnWymCg51gWiAn_EsThuD47HlSntEIvcN0P8G9JnZkzWNPyvmYKWtDgNmV6jLl_MyBkFkyfcu6QC3oYxWLY5GSLHUg59WSE2wi76NtG7tttZoEgPEhVhLZKXTcqmgP4hea3Fkt_0EdjJrWTqtvG9p-lKxqA1WbUCy9Cj1ljfs-LZC59GVVOzGGrMBdN4ixF07Pi8HYXBAHlt03ATEUW0cpF6F7fzj8GxwAb6gGe3H_FRTkB-ITCRYpMoOZl8hFjIOrcYCn1OWEmv2nfM06RvzWnZoVIMH6-Cl6oeIH0MhCJp0b0_v5YQr_rFkot9bO75h8HF1P1Jx34a2FRYqZF3B2D8FNx9pbIu_QYRUvXU0jas3DmZcNW7uvOCW_Fp-MxSDrQYA3LpcLkmCR5aQ_gcoFo-_YX4GLhM3YDbb9qwP1Rcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a350193e58.mp4?token=hJmTfo1I_WA_7PphnkaFtJ1daW8W3ijAgZ32KT8MnbFCUyvVPCN8JCA2vlPrSXVNcWtjgY4Lzx5CfvKxf0zG20BImkDkgf3YBYjPsF3ms-QSgYU5sKuQK3H7zDpeR8b2FHt8nTmHdgh95JB7Z_j3xNDRBIF_yKhi6YFeRCJDN9gpMWxjymSnkitg_6hOk-3q6lrhh5qjzaHBG4ckJBQGsbGL8rpDptx3VHzCtfjWIfq3Oo5nqt0mzoVIM4BPv8OnWymCg51gWiAn_EsThuD47HlSntEIvcN0P8G9JnZkzWNPyvmYKWtDgNmV6jLl_MyBkFkyfcu6QC3oYxWLY5GSLHUg59WSE2wi76NtG7tttZoEgPEhVhLZKXTcqmgP4hea3Fkt_0EdjJrWTqtvG9p-lKxqA1WbUCy9Cj1ljfs-LZC59GVVOzGGrMBdN4ixF07Pi8HYXBAHlt03ATEUW0cpF6F7fzj8GxwAb6gGe3H_FRTkB-ITCRYpMoOZl8hFjIOrcYCn1OWEmv2nfM06RvzWnZoVIMH6-Cl6oeIH0MhCJp0b0_v5YQr_rFkot9bO75h8HF1P1Jx34a2FRYqZF3B2D8FNx9pbIu_QYRUvXU0jas3DmZcNW7uvOCW_Fp-MxSDrQYA3LpcLkmCR5aQ_gcoFo-_YX4GLhM3YDbb9qwP1Rcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزا و ماتم مردم بروجرد برای آقای شهید ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/446461" target="_blank">📅 23:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446460">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e008d976a.mp4?token=UzyUrEfR3YK1AMPf5goJmYW8TLj4bZLyEspKnT6Fo7NywgbtTtB4q05A5V3ht6s3JkxVdfnDYYnpHiJaG4KKKDxGg6-YsSFqHUGGSnTP7v1FmGBS1IfyOgo6BoC3VV3v1R5K1LfwRINaohDpeG2WVvWkaGGNEdNhB_aP3MbNER4hNDmy1HNJZNM3WE2-ZTYQ2vxnYE3yvGp3dFEqPQeCIBzlV1zPh94JCCa3P3NOivjKwExOqr61yhcGD2fP_pF0HQ8zKuq3cGa5Kt-_VBMgxMl8BdZwszAPXdcmpOlUzdyUghLZje5vbla1qIwxo510ISWS9RSdBNJ0rnRx18J61g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e008d976a.mp4?token=UzyUrEfR3YK1AMPf5goJmYW8TLj4bZLyEspKnT6Fo7NywgbtTtB4q05A5V3ht6s3JkxVdfnDYYnpHiJaG4KKKDxGg6-YsSFqHUGGSnTP7v1FmGBS1IfyOgo6BoC3VV3v1R5K1LfwRINaohDpeG2WVvWkaGGNEdNhB_aP3MbNER4hNDmy1HNJZNM3WE2-ZTYQ2vxnYE3yvGp3dFEqPQeCIBzlV1zPh94JCCa3P3NOivjKwExOqr61yhcGD2fP_pF0HQ8zKuq3cGa5Kt-_VBMgxMl8BdZwszAPXdcmpOlUzdyUghLZje5vbla1qIwxo510ISWS9RSdBNJ0rnRx18J61g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ستاد بدرقه رهبر شهید انقلاب: اقشار مختلف عراق مدت‌ها پیگیری کردند تا بتوانند میزبان پیکر رهبر شهید ایران باشند
🔹
روز چهارشنبه بر پیکر مطهر رهبر شهید در حرم امیرالمومنین(ع) و احتمالا در حرم امام حسین(ع) نماز اقامه خواهد شد.
🔹
رهبر شهید پس‌از ۶۹ سال…</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/446460" target="_blank">📅 23:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446459">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🎥
گفت‌وگو با مردمی که از همه‌جای ایران زودتر از موعد برای وداع آمده‌اند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/446459" target="_blank">📅 23:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446458">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8776d64d2c.mp4?token=B5Qs2XwSauX_4K9_BXb3u5cbBpl7v5bpUGp5BnR8ytyjeQuMDiL2qcQsM7S0-DENGHMeB4-B6noe0zdF9JdmUbhveaQR2nj3JRuMqYIsScHHfmevvDawUa1TcUiAatqX389Qcodv_uBj1BfjIBk99S8It-n9IB8hSrB5ZVlpDKrohx037jL0uEp_WkfF32-K_qGozKSLGYNSPm19DM4JpMfbluWxtfnxjn8on74HLHYKqchuOq3XggwACGmWvAd1AeHFQFMlXCK9wq4eYVUwSCa8l8yY6ndQAr89gZw5FwrZ-fY2phq1ejfcM0hAjSFWVq-t5Be7czuPOv504ZmvcIG2Ve9e84ho-gz5cfCX8S13kJL9LZd9-ptEPRjMY_KojHflX2bU2gEK5TN8j1ljrGmQR47X8VIzasIjFafvhBCct8kxHjPzCSfoUr8LptAlml-JpqxiEUcmi9F745s2cap7jZYdpH9nCkE8KzbsS5SuU1Ug4PJn-VETSPVr6jHok_7pR_q7nHXcwiXCCZVVaF915arktYt2L1RdHapbWpl6JhZju0iPAbqfrx_yU77YgRt1434kKpZ9bOjX3-jtHUQjUuq_AU8vdkJ7nkEjJqzsLy6K384vDA0i-NxqG5ZsqkOXgIv2pbrda5-b56iXoieOIgbyOCfjg4stQ7Jb_7c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8776d64d2c.mp4?token=B5Qs2XwSauX_4K9_BXb3u5cbBpl7v5bpUGp5BnR8ytyjeQuMDiL2qcQsM7S0-DENGHMeB4-B6noe0zdF9JdmUbhveaQR2nj3JRuMqYIsScHHfmevvDawUa1TcUiAatqX389Qcodv_uBj1BfjIBk99S8It-n9IB8hSrB5ZVlpDKrohx037jL0uEp_WkfF32-K_qGozKSLGYNSPm19DM4JpMfbluWxtfnxjn8on74HLHYKqchuOq3XggwACGmWvAd1AeHFQFMlXCK9wq4eYVUwSCa8l8yY6ndQAr89gZw5FwrZ-fY2phq1ejfcM0hAjSFWVq-t5Be7czuPOv504ZmvcIG2Ve9e84ho-gz5cfCX8S13kJL9LZd9-ptEPRjMY_KojHflX2bU2gEK5TN8j1ljrGmQR47X8VIzasIjFafvhBCct8kxHjPzCSfoUr8LptAlml-JpqxiEUcmi9F745s2cap7jZYdpH9nCkE8KzbsS5SuU1Ug4PJn-VETSPVr6jHok_7pR_q7nHXcwiXCCZVVaF915arktYt2L1RdHapbWpl6JhZju0iPAbqfrx_yU77YgRt1434kKpZ9bOjX3-jtHUQjUuq_AU8vdkJ7nkEjJqzsLy6K384vDA0i-NxqG5ZsqkOXgIv2pbrda5-b56iXoieOIgbyOCfjg4stQ7Jb_7c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ستاد بدرقه رهبر شهید انقلاب: اقشار مختلف عراق مدت‌ها پیگیری کردند تا بتوانند میزبان پیکر رهبر شهید ایران باشند
🔹
روز چهارشنبه بر پیکر مطهر رهبر شهید در حرم امیرالمومنین(ع) و احتمالا در حرم امام حسین(ع) نماز اقامه خواهد شد.
🔹
رهبر شهید پس‌از ۶۹ سال حالا با شهادت به عتبات نجف و کربلا مشرف می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/446458" target="_blank">📅 23:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446451">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C3E03-lra2e6mSQKxh8ZES829fDzWR5hgByF7EGVowtYgeYuePfXPl9npSt4jBYoKvQteDBkmmIMnFNuZPNTkglujwtvss-braWgNxZBpePvNb-dvK_oAzH1_G_35Xsguj6xMfSa3rEmVT6W00RbtIUgCuZnhVxtrwe7WnKlKgKZZpEkrNDKfmJriD1Eg8Ura0i5rcs1GpW_AExOSR7Mz3l48TERxSczsRSXgCwos-izS9pTguWDoKVA1gXJERZDEwx64P0xHpgVja_d9uMdOqK6QU7D7odisdPtTimmyqpGE30lJ6KbI36pHce9PFtDg3MREK2Wom6OGhPPCEz6SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Db4Ye5pyYw-6NCAJ_TU5isHH3B-eap8LtzqQn4Ox-kgMKw4qe0rUOw0EdUk9pskiP9XjfqgPHRBeOE9E94Q0_MY06FW7d-26uBVlUHcBwDzmCEKFpMdsVNl7jQ6wuicPL3nks7_-8lhzW92yoHn4-Zw6N2-Ajahcv5xY25ZIcAWnEpSISfUvE9mWZaH-VBceIZlVILlmlfodpiPteU2dvcH37Cj90l6G0KqSXRudQSEiFTjGNFnMYgYpYopeLmI3CwdlDCfWP-VzxIFr-o5DlWdyT1qZ2q-lOrgWbxi9Y9AbGMBhXYYS7oJNx5rI8rVpOtYsekxyDvOkO0_X8cs8kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AMX1nxdvFb60vFhmCvwKHem1wzdZja5kfXvpi7AfuhCuJsMxvt__awsedyKaj8SomOAzZuVeG7dP7ZZuxKHrVrvQJpCBpv9lL0_soomYDLYsyISSiKDp0oFuZ6Cn6oaGRnrCKyeHw3D9ip2URcSWAxbBO-BKQ9v2k0oaegklNsmddUu0Rru2RafxNkeSGctZt3xxRa3ZuTegdN6x5BuRw6T43pI0NRdBBQ0MJeGy4uWeDlxvcHrGq7iHPy-2ZbUOPWvc0JqHwOanHK8A08e0hml97pmH98QGSk85vsvVERSGW7mLMlVX22BjJR_OjHEvTbAdv128QN3ktSqnFC9D3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CCHIvRkqUFlsPeqWVS8cWnjO7L0Jqo2ClK7RhT365LD22rZrE7u5uLZ-aljt01kimRKWznD_8_XIJICwIyAFOAL5jpC74-1pBalodqOidHwgfza9O9GhNyvZzwm-7HLaVu_piGlAe4tlhhxxbYLxbfaJJMpaeq6lNiCRCSAYQFD0sJgsKtL_j2M_UGgbDFqoF9zinXs-Ga_iok0H8_SHFkuZ3rRATpJ3Nk1f-lLhSSlOg4yLrZIo7Z9rjvEG9v1aLCLs6p8bFvDHppuIS3WDyBy_7OwO6MbToflQaVxPB2Ev3PhU_H5Hwhk0UnXDBksLp0idDkeo4v3gFeJOeFuBlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t9AHq5AhUFQQvLVhXvOvRa2X8Kz0w2F9i0I7BZFUfbnTPvUSzZuYgqospdQuDHZvRJpB4KUqToWlUBpTDp2ZpFVb13bwLfNT-UoChKSpgvF0DAlo24CBCWiS2JqrWrfPhFWmnE-ZjjLweDaQ5JuXLtm1ka_QWwytDSxqVAYh3pnBTKfopMMYE0b17xYJXoCndX9UnLEzNjXwGigtf1g3RK3QzeIZVorezAF0i1rvZVycbUTmYC3iwC23zsKet-b3GK6sBR4N9ihzrmXzG4X43glo9we38qykq1hteqSogpqsyR91id-K3272BgAyc11Bm7aj2TnF2dMZCAveUBuOFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tCfU3uKzaTfmH2YgrtWMx6oe70rD3EkbJwzylLtHfkA-Xt53S78kqNu1dDJ0UTu3BDxaLCeHh5uFI6pu2pmBSEOfXp3XhTvqmbwymTUP8biOEIxjbEdHW0-mXkRWh-2du_6ijPqgadxS5NiVmcO7hyACgHJNKscrByuUUhfAE2QlwpffPMDpxmB1qPQNVkVzvlNb3LhJTzbQvx3r451g3T25N4ZTxUyRfZDKzVlbX3TQuSYiPsSOEOJrwA-2tP42WLx3SJRGcQOEpAls9cfSOox8NavoeJzYg6hyt4ajW8W0bA5PUTn6IiPGg7vNNtemnDZ07r34iO581JK83mUQQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_i22rWAJkSw7Sly_9YXYItmx6UtzdIfvwMvZDNwo3RL1_2ZTVJYmVQ18_inxMQ6nhNq8_SU5HUdZOWt-y1X47UcLipqLWOJmMF59G38WAq3l2A0Ed6Ynv7OFeDDcmlDS1Ttx-K768vtHAp6uHYVMR5cB9N8CINnddyCelK5w4kFNJUiPjz6RROxVH8vJiTPTZVyBPItD4E4zy8eS5EidfTlnc1e76Qwai7YTMXM1TcAe5ggwdcsY2naB-bIYupSh4jR2AVCfgTe3K4hG_BJzd8Ku4Psdnqgjf6diCWTdaeuDcf7p-1KNrJK6eeLHvO1z6UlWGwPEEQ7xlfOqyT8cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
۱۲۲ روز تلاش برای یافتن تکه‌ای از پیکر شهدای مدرسۀ میناب
عکس:
مرتضی استادزاده
@Farsna</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/446451" target="_blank">📅 23:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446443">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/950e330a0b.mp4?token=XTipvKgzPrt8JDdaWVX5b4eAq18oyMxuxSDiERIZ0ZxYuxwdvxzENCF0_rjynB4OppD-9_Taar2TQyV7PNbfWC7PVNllRCYG8UGqVZlksUixh3tX_TCDe-RoOWcbc5eRwIDisr9rcZMQrXba0KrsJfkCN8sYWLdgiVAIWMwLF1wttlrb_l4vK1xFtI75RY4oRADy0JPe8hMRU0Z1J7Wp26ZZ4aKRfqHsjcbVOTQvYfaUbD6H6vvj9Oql1wB4JRQwE-l4cCNH9jQQxb99DhdCqhUUuWyXAA03hxcLT25r-rbQfVIl1onls3Spuybtq9dVrrTqfJe2g-05un_8PFl9LRYBsiSmMKMz6KyJDCYLPPHcvGYk5dLjISy8JDExWTnopSftbR0qkiCwCMkUfGz_MztnspngMrynwdqQzF054UH5wEpsA5mef08IvA863UpJ00m3RKB10Bq21wXMhXSBHnC3Up1uTgw6uPxIjf91VohQNbIbfqAcF4BT8QoD1jcmsz_cP9QlaMRrGUIGUwWk4FbuoOr3Nkmu71Ur3Wyoiujs-nZvbONRtfuNLfmUTpp3Rq2FGGf6GR8YZe-jngzXn1ytqxiLH_BpRLGr1NZem1sWkI5pb_k1M_SqAC3Pbb_UhRJM44rVsLdTFJ72xzbnnn2TGEeLitCNIuyTDAC_UwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/950e330a0b.mp4?token=XTipvKgzPrt8JDdaWVX5b4eAq18oyMxuxSDiERIZ0ZxYuxwdvxzENCF0_rjynB4OppD-9_Taar2TQyV7PNbfWC7PVNllRCYG8UGqVZlksUixh3tX_TCDe-RoOWcbc5eRwIDisr9rcZMQrXba0KrsJfkCN8sYWLdgiVAIWMwLF1wttlrb_l4vK1xFtI75RY4oRADy0JPe8hMRU0Z1J7Wp26ZZ4aKRfqHsjcbVOTQvYfaUbD6H6vvj9Oql1wB4JRQwE-l4cCNH9jQQxb99DhdCqhUUuWyXAA03hxcLT25r-rbQfVIl1onls3Spuybtq9dVrrTqfJe2g-05un_8PFl9LRYBsiSmMKMz6KyJDCYLPPHcvGYk5dLjISy8JDExWTnopSftbR0qkiCwCMkUfGz_MztnspngMrynwdqQzF054UH5wEpsA5mef08IvA863UpJ00m3RKB10Bq21wXMhXSBHnC3Up1uTgw6uPxIjf91VohQNbIbfqAcF4BT8QoD1jcmsz_cP9QlaMRrGUIGUwWk4FbuoOr3Nkmu71Ur3Wyoiujs-nZvbONRtfuNLfmUTpp3Rq2FGGf6GR8YZe-jngzXn1ytqxiLH_BpRLGr1NZem1sWkI5pb_k1M_SqAC3Pbb_UhRJM44rVsLdTFJ72xzbnnn2TGEeLitCNIuyTDAC_UwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرثیۀ تاریخی شاعر برجستۀ جهان عرب برای امام شهید امت
🔹
تمیم البرغوثی شاعر فلسطینی با بیان‌ ابعاد شخصیتی و الهی آیت‌الله العظمی خامنه‌ای قصیده‌ای در رثای رهبر شهید انقلاب سروده‌است.
@Farsna</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/446443" target="_blank">📅 22:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446442">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d1b34e56.mp4?token=oYkfEe21M1gqRFH1X6Ry2JoJcmQVoXsffMNOV9Yp44LBSb9-A4jS2YBAOmC3f7oMNo6-U-1i4RcQ6JoESYpgDKpnZ9PO1j2wGC72gCRsa2Wg2eHw1ALf2sjPqv9ozwfbuR5ODZYE9sYyiLp8-ELYye0VVTRCfdXZBeyMF7JnCeXvSuz9hts2d_ezvq_tcQhLsCVHvS_VjpjYHkwkDCpNprP2pIviC9faVinOxaW_PRnQzp3ztVOFkQZFP_gtqtmKf-Xro_cEqJgo3KI1HpA-Wpw41zdwE2CLJb_KZhcGNijddkTkAB7sQNnGFJHVjHPDwaIyEF__beRuwmruzVjBCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d1b34e56.mp4?token=oYkfEe21M1gqRFH1X6Ry2JoJcmQVoXsffMNOV9Yp44LBSb9-A4jS2YBAOmC3f7oMNo6-U-1i4RcQ6JoESYpgDKpnZ9PO1j2wGC72gCRsa2Wg2eHw1ALf2sjPqv9ozwfbuR5ODZYE9sYyiLp8-ELYye0VVTRCfdXZBeyMF7JnCeXvSuz9hts2d_ezvq_tcQhLsCVHvS_VjpjYHkwkDCpNprP2pIviC9faVinOxaW_PRnQzp3ztVOFkQZFP_gtqtmKf-Xro_cEqJgo3KI1HpA-Wpw41zdwE2CLJb_KZhcGNijddkTkAB7sQNnGFJHVjHPDwaIyEF__beRuwmruzVjBCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور رهبر شهید انقلاب در حرم امام رضا(ع) در سال ۱۳۶۴  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/446442" target="_blank">📅 22:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446441">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0d65fa4fa.mp4?token=B_3d9sWbRbH3sSVtcqzro78dcqtd0fPBmqjnKs5T5QdOa2j7q77SebkvUr5WOMCGhxrZPXIHaWz959D4ZcUrtGxxXSknkFGFI-6GCI8hwaUlQpA6W9Ysy12PntNQ3tHkART_jupYUFiUbXKcDfvh9SP0NPo2255ehWflJn-qjhutVVJEdhQEIKDrXMj6zMZ2ytWZLs50c4F-g0Y8vxVT8SZjqcCRJzplgrN33Z7brOnG3DP1Mp8iZaHMatUWRRpBKDVBub7gkjpSTtWni130sd3Ip28wCOPzIzl1XAzUXUZTEPQfx4KErpexJ80BVGHo0M2MUVS2kMlCbplG-ZU1kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0d65fa4fa.mp4?token=B_3d9sWbRbH3sSVtcqzro78dcqtd0fPBmqjnKs5T5QdOa2j7q77SebkvUr5WOMCGhxrZPXIHaWz959D4ZcUrtGxxXSknkFGFI-6GCI8hwaUlQpA6W9Ysy12PntNQ3tHkART_jupYUFiUbXKcDfvh9SP0NPo2255ehWflJn-qjhutVVJEdhQEIKDrXMj6zMZ2ytWZLs50c4F-g0Y8vxVT8SZjqcCRJzplgrN33Z7brOnG3DP1Mp8iZaHMatUWRRpBKDVBub7gkjpSTtWni130sd3Ip28wCOPzIzl1XAzUXUZTEPQfx4KErpexJ80BVGHo0M2MUVS2kMlCbplG-ZU1kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاندار تهران: راس ساعت ۶ صبح فردا درهای مصلای تهران باز می‌شود؛ قبل از ۶ [خبری از بازگشایی] نیست
🔹
مردم طوری برنامه‌ریزی کنند که از این ساعت به بعد به مصلی بیایند.  @Farsna</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/446441" target="_blank">📅 22:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446440">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6b0c4b111.mp4?token=ID8PE5RnzWnVRLa1AZYKjT0pDgnt3aHIwWbTj5FDbmXJHjFZ0oGTU9FLLZPpdwd1okbJPub13lGsU3RH3wV-CnSKVjOfA9914KlXGmULXm46uxqugGTMIQEQQToO3b29dhmOgLuUAKogJRoXzpsJ0hRS9OXIZcJOkdG8y11NVvY317Ea_Qbns58OAC3r1MYcW77-4nFFiRynrK3CyHSXXCB0aEpzQ3up63HWG5POJLyiIcVtyZBsY4hz3eBRUHUZQs7CpDz4kHyLBTYUi_QyXM7iVvJlrs82G30wF0gdEKVwkOWka1eovvL1g7cMaIPK9XOADUsRq_GF2Z0zlFk6Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6b0c4b111.mp4?token=ID8PE5RnzWnVRLa1AZYKjT0pDgnt3aHIwWbTj5FDbmXJHjFZ0oGTU9FLLZPpdwd1okbJPub13lGsU3RH3wV-CnSKVjOfA9914KlXGmULXm46uxqugGTMIQEQQToO3b29dhmOgLuUAKogJRoXzpsJ0hRS9OXIZcJOkdG8y11NVvY317Ea_Qbns58OAC3r1MYcW77-4nFFiRynrK3CyHSXXCB0aEpzQ3up63HWG5POJLyiIcVtyZBsY4hz3eBRUHUZQs7CpDz4kHyLBTYUi_QyXM7iVvJlrs82G30wF0gdEKVwkOWka1eovvL1g7cMaIPK9XOADUsRq_GF2Z0zlFk6Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین وضعیت مصلی تهران پیش از آغاز وداع با رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/446440" target="_blank">📅 22:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446439">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1b9646a94.mp4?token=eRQpHWMjCjNFmvbF9MPDX2-h1H8Dj3gIxrUEniC22AUEie30m41YxqUZQDs_FB-9BFA79zKrVy4nRRGgkkCaAqsdqv3xOzG9SQwSfOYJuUFuvdjqLzCMmcIiiBiQL8Ns6CoAyswcQfW0SngDgadkmBd9jmp6ArgQyOOkOtKsogE-j2An1WSahgT7NN2YdFpiqEQgRnvd0wHJUiZmzQvLXuFxuCE_-Sz2egKgaJb07-L5WpWP5yS8xi3T2f239vlH5e8tbxiNekNMZjH2Wik5hJquhj2QiyvIRmj2zvyQlfyvJbsEcpKDseOStZiNmQPWw5xe7AgYDIqgv5z4-BZfuEYW5uu7YgaelhvoN8m4XBgEEA0UqaoGAJzoga4Vc3-keVWRBjfhlM8LOd1gzVjieeH0tPl_Hpq2KPu-cjFZzKrsoFukIxZgDr-UXQe4TvvaTvYOzHqc1ZgJ_iLRXihxFtgvv2RXHx-wjnwN2FM1WW-LQY33iy2DMVJ00j4xFGsbTRZ6ddLf7OhIZSdnCYxyOt1uXTASpyk_3czrutOj1EXPKBSLtwl7zb-71U8Kxn6iS-uLriRnISpnl1xtMG4s2S0qNRCXXkET7Gx1_v0b8q79wBDgRO_0-2vzzlkrY3YpqNBxKFO08ST3N3DH4VDLovllkUNGXJNyelIg0z2Ki8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1b9646a94.mp4?token=eRQpHWMjCjNFmvbF9MPDX2-h1H8Dj3gIxrUEniC22AUEie30m41YxqUZQDs_FB-9BFA79zKrVy4nRRGgkkCaAqsdqv3xOzG9SQwSfOYJuUFuvdjqLzCMmcIiiBiQL8Ns6CoAyswcQfW0SngDgadkmBd9jmp6ArgQyOOkOtKsogE-j2An1WSahgT7NN2YdFpiqEQgRnvd0wHJUiZmzQvLXuFxuCE_-Sz2egKgaJb07-L5WpWP5yS8xi3T2f239vlH5e8tbxiNekNMZjH2Wik5hJquhj2QiyvIRmj2zvyQlfyvJbsEcpKDseOStZiNmQPWw5xe7AgYDIqgv5z4-BZfuEYW5uu7YgaelhvoN8m4XBgEEA0UqaoGAJzoga4Vc3-keVWRBjfhlM8LOd1gzVjieeH0tPl_Hpq2KPu-cjFZzKrsoFukIxZgDr-UXQe4TvvaTvYOzHqc1ZgJ_iLRXihxFtgvv2RXHx-wjnwN2FM1WW-LQY33iy2DMVJ00j4xFGsbTRZ6ddLf7OhIZSdnCYxyOt1uXTASpyk_3czrutOj1EXPKBSLtwl7zb-71U8Kxn6iS-uLriRnISpnl1xtMG4s2S0qNRCXXkET7Gx1_v0b8q79wBDgRO_0-2vzzlkrY3YpqNBxKFO08ST3N3DH4VDLovllkUNGXJNyelIg0z2Ki8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رجزخوانی رزمندگان نیروی زمینی سپاه برای دشمن در مرزهای غرب ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/446439" target="_blank">📅 22:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446438">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3acc934c23.mp4?token=VeReUjOp6E8usZdnbZRh5Ni8Tg7YZeNNfprHAtTiahdNMQtCvvUaFkyLCliIMyNC0RIeClrkkbKvgLM6l7rkR5X1vpKY-8EabVaZV4oAAZOebax6-ij6sxVRqu-vWwGahmOw9DuN6ms95CuF7bZqb6RK85JIdNZeUTf71MHMCZ0M4ydpuqiru8hB5vby6UtuD_E1NShmdUI1DWBRxnkeJxnV_vloBuFsDQLkBBjqy2vLkPPpshU3bN9Dmq_79ZhZmrCXhNKdvnttD5qwAALc6om1ogGq67NxEvd5LviP2BLmZBVcIS4HstrtSwq4TNF0tqNLGVoA9iGZ_S_pkUGphA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3acc934c23.mp4?token=VeReUjOp6E8usZdnbZRh5Ni8Tg7YZeNNfprHAtTiahdNMQtCvvUaFkyLCliIMyNC0RIeClrkkbKvgLM6l7rkR5X1vpKY-8EabVaZV4oAAZOebax6-ij6sxVRqu-vWwGahmOw9DuN6ms95CuF7bZqb6RK85JIdNZeUTf71MHMCZ0M4ydpuqiru8hB5vby6UtuD_E1NShmdUI1DWBRxnkeJxnV_vloBuFsDQLkBBjqy2vLkPPpshU3bN9Dmq_79ZhZmrCXhNKdvnttD5qwAALc6om1ogGq67NxEvd5LviP2BLmZBVcIS4HstrtSwq4TNF0tqNLGVoA9iGZ_S_pkUGphA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاندار تهران: راس ساعت ۶ صبح فردا درهای مصلای تهران باز می‌شود؛ قبل از ۶ [خبری از بازگشایی] نیست
🔹
مردم طوری برنامه‌ریزی کنند که از این ساعت به بعد به مصلی بیایند.
@Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/446438" target="_blank">📅 22:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446437">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‌ اعلام تعطیلی رسمی در استان ‌«ذی‌قار» عراق برای تشییع رهبر شهید انقلاب
🔹
شورای استانداری ذی‌قار عراق از تعطیلات رسمی در این استان در روز چهارشنبه آینده به مناسبت تشییع پیکر مطهر رهبر شهید انقلاب که در شهرهای نجف و کربلا برگزار می‌شود، خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/446437" target="_blank">📅 22:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446436">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc0642946c.mp4?token=PHkh3ZsnTX3-uGI6uU7F3yfoXK4QKlE0dm5lTCbi8Fk-6z-sFv49Is0jGDB7_sziu6F0OI8K9GiOgVPGvQ_DNfAGqFObOhQCbPCLsbFQ9DrGeVjHybNgIDASh6s00qxtzaOi6tq9soCu_rYIDNFnOXs-EelIYGBy7Cnp7OMq36WuttGpzzg3bWrA8Girdx6GO9fhieGrXKPx4m7yjIOVAyukon-uofHsaLJrPPrL-Fl-57a3OuzUfHNqVPvVXZELlCZrgpB7eWHCjo-s7rg9jus0P0an7PpXLBvT_dpDWK-ox02T-bO69tSAjTxSbgHwrneE7tFp5S3eyXATRCf6LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc0642946c.mp4?token=PHkh3ZsnTX3-uGI6uU7F3yfoXK4QKlE0dm5lTCbi8Fk-6z-sFv49Is0jGDB7_sziu6F0OI8K9GiOgVPGvQ_DNfAGqFObOhQCbPCLsbFQ9DrGeVjHybNgIDASh6s00qxtzaOi6tq9soCu_rYIDNFnOXs-EelIYGBy7Cnp7OMq36WuttGpzzg3bWrA8Girdx6GO9fhieGrXKPx4m7yjIOVAyukon-uofHsaLJrPPrL-Fl-57a3OuzUfHNqVPvVXZELlCZrgpB7eWHCjo-s7rg9jus0P0an7PpXLBvT_dpDWK-ox02T-bO69tSAjTxSbgHwrneE7tFp5S3eyXATRCf6LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سؤال خبرنگار صداوسیما از رئیس دفتر رهبر شهید انقلاب: نمی‌شد آقا در تهران دفن شوند؟
@
Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/446436" target="_blank">📅 22:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446435">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e176fcf876.mp4?token=WB9g8qJSaEkpCxAn_cYdrk4cLYCm5_u86ouNPnHJjQ9KoGnyjghWgId81_WHdk24OUpgV_b5spc8ie4cp1PtT0aBbLhzMfmCn3jr4fF1TXC2dh4qexZix9N5cPG6t4270_4BLvRSMNn2lZDqAOzFEMKMGDESztIU2cSsByWuUKLypgHIH0nLkQilQxAJnldjTE9PvBPGvD4WzObi5DJpzk4fES2YQVRIb-BFg4TC5-4W0yjYB8SgIJD7lk5_9yYz8HVS8i1AgYYJUE1ql-809fnZ37KjhRT8DgzMiVYu4t8lBmvVVszjbrrNxNml-kUQAznkDLHyW8J3__YPgkigKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e176fcf876.mp4?token=WB9g8qJSaEkpCxAn_cYdrk4cLYCm5_u86ouNPnHJjQ9KoGnyjghWgId81_WHdk24OUpgV_b5spc8ie4cp1PtT0aBbLhzMfmCn3jr4fF1TXC2dh4qexZix9N5cPG6t4270_4BLvRSMNn2lZDqAOzFEMKMGDESztIU2cSsByWuUKLypgHIH0nLkQilQxAJnldjTE9PvBPGvD4WzObi5DJpzk4fES2YQVRIb-BFg4TC5-4W0yjYB8SgIJD7lk5_9yYz8HVS8i1AgYYJUE1ql-809fnZ37KjhRT8DgzMiVYu4t8lBmvVVszjbrrNxNml-kUQAznkDLHyW8J3__YPgkigKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تصویری از وداع سردار سید مجید موسوی، فرمانده هوافضای سپاه با رهبر شهید   @rahbari_plus</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/446435" target="_blank">📅 22:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446434">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsnOrlZAyBwITkfqsIT4LLZBccbOrbrgHN6mwLHMkVnMwTpJMiQ_Mnt7RUF2cfTUk9stRxbwbPdpZy1GZKVY2oK30NC5AwEWeDqmw5PIeLo1Auz8Qr0e4AuNWhX4JmT_YKUWW-85HQ50inaa1WHfRWjbpFlNSjbFm7-SkJhHHe94V3_HxBHXfDm2Kc1ORRANi_c1JqGz8LDbI-5s-8-HomsQy6c70XPLKtNGRMthMHEUyl8NpUjdaq9b6cRCh31BBBWw0PXgpMU75UUaviPrvWZTcX140ZhZ-9Qp1FpyuBdZrAqic8xi17k3HOuR0cjAu7PAhmIGz-hI1z8mlUnZpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش قالیباف به گزافه‌گویی ترامپ علیه مردم ایران: به فکر سوءتغذیه ۴۰ میلیون نفر در آمریکا باش
🔹
تصور کنید بیش از چهل میلیون از شهروندان خودتان وابسته به کوپن غذا (برنامه کمک غذایی دولت) باشند، اما همزمان یک کشور دیگر را «گرسنه» خطاب کنید.
🔹
این حرف، یک اعلام یا ادعای ساده نیست؛ این یک فرافکنی است. یعنی مشکلات خودتان را به دیگران نسبت می‌دهید.
🔹
نصیحت‌ها و توصیه‌هایتان درباره برنامه SNAP (برنامه کمک غذایی آمریکا) را برای خودتان نگه دارید.
🔹
ما خودمان درباره دارایی‌هایمان تصمیم‌ میگیریم شما فکر نرخ سوء تغذیه در کشور خودتان باشید.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/446434" target="_blank">📅 22:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446433">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/123fcf84dc.mp4?token=T1mmYvfrOwGuotV1zklRQotOXORBIpktpIcKgih-5HDuOP_q3Hm7W8Bq1Xqnrd_3qbtbgIQyP1EB-0B1E2Oh-3Cf6gu-bxtCoerpv4j2stz2iFLhOb1TfLFSnXNkGDZhDCerOdI4N4B7_mR8rG8vK6iUGnIAV2r6u-6DulIzTR9cNOo08jnRnfa03tLoP89rir-ebt334c6I3tvVJlgRZWVbQmUxEJz6BTKsEwIo7erJCCngHqyeRg6iIUc5uC22RqjETLnvzcAK8rzgpVaJ9CYYd0oLXyKIIh27rdsSX10KG6n4r-mQJ0UP99V0SSkyfDxnW8Ob0rxPcqefn5ODMoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/123fcf84dc.mp4?token=T1mmYvfrOwGuotV1zklRQotOXORBIpktpIcKgih-5HDuOP_q3Hm7W8Bq1Xqnrd_3qbtbgIQyP1EB-0B1E2Oh-3Cf6gu-bxtCoerpv4j2stz2iFLhOb1TfLFSnXNkGDZhDCerOdI4N4B7_mR8rG8vK6iUGnIAV2r6u-6DulIzTR9cNOo08jnRnfa03tLoP89rir-ebt334c6I3tvVJlgRZWVbQmUxEJz6BTKsEwIo7erJCCngHqyeRg6iIUc5uC22RqjETLnvzcAK8rzgpVaJ9CYYd0oLXyKIIh27rdsSX10KG6n4r-mQJ0UP99V0SSkyfDxnW8Ob0rxPcqefn5ODMoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ای عشق دل‌افروز؛ دل من به تو گرم است...
@Farsna</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/446433" target="_blank">📅 22:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446432">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c5c84c5a.mp4?token=VU6cISYjoGpHShBiu0pGRYyQmvZL9t1t8Gperp0n35Y755HFpeD7qWw3pnmDtCbviSlil2JTpZcWyefBWHIMHLwf-VF-RbQdbxTJh7Zt5TK5zBsJXEfEDBQrwLnm0OuehSBXhS2GLQlwMIpcawFdXR9gOLudJq-FNacfDBB81jLZbMBX3tcYJHRmM15i8GspVql7O5w2aN1PlCbShDtIrTmgzLpWhUb1xZCllKHib9-5vXiXakRPV4NQOvL775D9oRRw3_WHz8wSMq09v1zWkg5W0Vi8qnY5yBPw7wPGnWGMKp8PlO4T2PKGCDSRFo00nr2GmnTTHoKdIKxpjunpQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c5c84c5a.mp4?token=VU6cISYjoGpHShBiu0pGRYyQmvZL9t1t8Gperp0n35Y755HFpeD7qWw3pnmDtCbviSlil2JTpZcWyefBWHIMHLwf-VF-RbQdbxTJh7Zt5TK5zBsJXEfEDBQrwLnm0OuehSBXhS2GLQlwMIpcawFdXR9gOLudJq-FNacfDBB81jLZbMBX3tcYJHRmM15i8GspVql7O5w2aN1PlCbShDtIrTmgzLpWhUb1xZCllKHib9-5vXiXakRPV4NQOvL775D9oRRw3_WHz8wSMq09v1zWkg5W0Vi8qnY5yBPw7wPGnWGMKp8PlO4T2PKGCDSRFo00nr2GmnTTHoKdIKxpjunpQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همونی که براش نمردیم آخرسر فدای ما شد...
@Farsna</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/446432" target="_blank">📅 21:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446425">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jtgm7jvkWThL8Djajc1kmg9qerrL409BrZ4bIAVKCloDzDjogmY1kiFRmRYCJI9O07qh69P9QeOftaUferj6Yl23C7lIN5EDwa3KqsEbP_ffxKvkZOCZGgCP0RdgnJrkoBVVZYYECRL_6iJxU15KnkGSk-ETGXn0A-VQIJtQqF_94ANBYgu_yMJc8-rJtKyFtxWlLwgqObsokmQK_hIGIY1AFgB_Cmthvga-8jqWUsEGtDuh433ZDt0mYGNKh1Kqeu4rhUtGNUB9Jqf2XP0WrFpvOKKEFQ-XMdVSYczvGVFXuoplL3kndZ-a7rtbyAg8x6W4U4Ae1s3KKmseHvpxSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oUF0Hz3wBbq6zjAEvTdsg1eBqFlj4RiXx7pJlzV_KqZq0_NClwNX88ZuaI5Gksu2bQpz3k2shA5S7GMpDNJbwbXHPhFkSa3DSSaSeT5FwaVF7UNqjefBiFZaCcmiABrmD6P9WN_rmFL-CEkrT0F3R-FAOED70b9RtKXZ4GoMXqS8eobpIcyvBnbl0XH-_5hMZNNdFE9H_ngR9uIYBed4hBLjvaKpkjs8TZPCdktFef_oiFjhlV4RCXi9-DuBEBz_4uzI4bg5D2a9jlOKskJFGrbA_AYdrG-2xzNkMnzaumGprIkBj9I1L6tcjL4n1NEIfvkRyTxXrgD_X61kl_SiIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DS62LAaN9LTNEuPkkcmXCmGkc5kNzl0Gw6MPvkkkkY3QkurIcXwjnMeYLLH8KfUm_GBcvaeVd-D7-GIvhj-ROcj8jmnfhbqaH7hRwte5mxVfQ-KLK9_psCxvXajyizgTyO6LMTuGK_Kcpvew6qZriKS2HbtIBFqwnoxgJZnETLdhFJYsumCvOjx97WTq7PeJG3fQFqET2wyvdmmdzzaw_Q7PbADeIiFGFK4bShk2Yx-vroTWY5CaIeufXG7RnJgZ0X1ZOjb9ad--DprrAuPuVY-XImjuhtCJMt7ecKgueKHIWLIxle1eb9VWh57MhLEII6ZBUFBFD6esvakNN1AvpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YF6Ib1Ai7tWVK107glJMHYHIbkSab04H9nUyHF8Q_S_VTrJ4TUesglfULVIj736n9Xv12KEWPkO_ALY4BL8CwFbbGGlPhH5M09U8cYkRN1kYI_kDX8EaMR8K3DWhtWjrYNEWuBfQNQNCegNSLYdrf-3vCrlgiL_eCM5jn3M5vpAiR1xtgJ1CA57IQpYEbx3BelMWlaGDOrvQar5yo6c6BYhA3Q8IkqBI5DXPkwMYOv7beYv6-X8rZkkyQkC6A3H_4U9lyp3TV0CdSARyqh-nb6WO2RPvsoflnyGz_BsRjQgMZY_tCFSwvTERG0Ay7oHyiCjNfJ31xmnwkXmuUIvWwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7kU-4C85wiUIePTptFMwUi6pRjNx0yorD2oqtIqy5jyqKjt-eecbCziMPEBYwyid3kYxIPkSeCIKWnHJxbYv8K7L6LERaoBJhS_fhsttqABZr8RS9a2n5JZevzgVakRi1JmI6H7EIYo8ao40c1JFK2QwZ5dgUEsRsdN91iCqjbiMScq4AULCYUNojFFu6TlSwU33VCGeYkY1Nz7g_xEZOuX3wknvj9dNy4RbhSrkOYlDPzJ4XB2B7dfz7hsQU0fd8emoCDNPmCrtKZ6mKlZbOilYd52beabPePYE_gYRMbhvhSl7a_914t2Kxt1kv6sl7hjv42hkq_1rTwg2JPrlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HfId_Fs_0mnKWW8ZcoZ5Z-e5stUngf2eJlBcynVYWXuTeV2Y4m3eLi_pzpAtcPH_Mm3WOypvLtGRdCQxB-M15pC09j4im_iOGzezd0EEdt5pEuDtiyJ_rw0TyBjhdQiKsvH6mBg58KmliaXosfjFOu4q1CA8bXF4h7kU0ATEWgDqd4GV5TNQ6sfqfVgG4_lfAnze9gLuYbz4Hxq7ywm4SvXNRVweoN59KEn0A4Bs1DNioo1_ryDVTAtsxYGMAX1duC-cGiawOi_eUdRcBhZ-48L1L0JAroRr0mDYWQVFafHaq8eXRt5DeTwTBKT-86BfYLBuCVcG2kPY5xIXGMmi8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IPbLI5-Ay37HMicJuzZPfSqgXOcngRjMgeWT-P5aFOVkrknR9dqn05zMxrUPzKpESKeMVJBMrUJnpTjSxED3puEGh7cYW9yoEBCLGH0vgwA8fZlI2es7yNIgtJjRkLNFcWRUOPuj7HxRylq7VNuHFXzXbpz5HKEOLzWsVyOo_NVAbMXdhTG_Aea6lqZ12lQFC3CRR07ujvWlH37-eSLd9oC_9MjVvrotQqI_LGXbU1w0DGOxKwUgkCsnA4LVAES14w4APDYlG-gIx4BTW2zBD2hdSu0ddgU6_sbWgPRz8opA7ulNh9v6FJXaPverQ5B6s3E_eRteBoN6S9d2yKr-fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تشییع پیکر شهید مصباح الهدی باقری
عکس:
محمدحسن اصلانی
@Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/446425" target="_blank">📅 21:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446424">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9efa1991e.mp4?token=XvLwdhOjasNuA1nedqFo7_lGfN3F9N50exUBB2cQLVez9bU-l6tm-Rwiu4TsXqGIAedZCFavyj0OxaREb2vwJUV7w53HhtdNowJmFrp1ETuiqfACen-fa-wH7kU-5jZqAUNcy7fpMQLPI7eQH8IMice63RmxNnQ4h-Aw-NUVjoCSAizDarPrpqs0CAWd_X768g572xRDdKnjUhnfvBHULO-AsMQgMiud8SBUQ54cmz1yKgUyp8DECcrX7XcU-gpZ2T7KNPtcneRgTH4GuNTlEcNvP-wGlYbGfuL2BvftyUv5mUqIz1cBpJncYe5jIMcO__eoHi_9cYtp-LgKttz5Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9efa1991e.mp4?token=XvLwdhOjasNuA1nedqFo7_lGfN3F9N50exUBB2cQLVez9bU-l6tm-Rwiu4TsXqGIAedZCFavyj0OxaREb2vwJUV7w53HhtdNowJmFrp1ETuiqfACen-fa-wH7kU-5jZqAUNcy7fpMQLPI7eQH8IMice63RmxNnQ4h-Aw-NUVjoCSAizDarPrpqs0CAWd_X768g572xRDdKnjUhnfvBHULO-AsMQgMiud8SBUQ54cmz1yKgUyp8DECcrX7XcU-gpZ2T7KNPtcneRgTH4GuNTlEcNvP-wGlYbGfuL2BvftyUv5mUqIz1cBpJncYe5jIMcO__eoHi_9cYtp-LgKttz5Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیرکل جهاد اسلامی فلسطین: خون رهبر شهید مسیر آزادی قدس را قوت می‌دهد
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/446424" target="_blank">📅 21:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446423">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PR244XM_s18T-p82iOILm_j7mYlxAuQ8N_1jrysDg4rPXrF4JXUUUrnVmJH7wS4CpLDqNypoYNnckyOrt7y_ZhnVMt_w_YQfYZVgYwT3T42iPvacLmFoJVafWbkLW0dm6IXu3TfFOYEDRMmUmwHICqN0H5Fgs1sIoivVvGxa7o6-_c4JY-VSNkQayEISmeyF9VMnChBCqZq6MBkDnjk5ZRTuSqynEjZib37O5rdJMG0-fOzsSh-b-D-NHbRRiTqMP2cCuiEtNO1afSKqnMPSYxGI-lOlzreo7BY96RWv6w4r45oXn1n95kPZ6MRnPsd84rtr0iTRRrOB09HI5gGrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار معاون رئیس شورای امنیت روسیه با پزشکیان
🔹
پزشکیان: از مواضع حمایتی و همدردی دولت و ملت روسیه قدردانی می‌کنیم. باید از ظرفیت‌های شانگهای، بریکس و اوراسیا برای توسعه همکاری‌ها بهره گرفت.
🔸
مدودف: حمایت شایستۀ تحسین مردم ایران از نظام ضامن حفظ ثبات و اقتدار کشور بود. مصمم به اجرای پیمان مشارکت راهبردی با ایران هستیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/446423" target="_blank">📅 21:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446422">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea23085be.mp4?token=BDEkDHmY_f_OfoCkflQ-cJjAqNeRcbsxc8TjqptQc5k-EmC876RMd2oivnW_AHMqg4MsnrDTo7ELdkpTyOX3Lc-ZW32ohrv8AL1Hzvt7AhtFp-ocywlIcpezVivvjMcwVg4iqfePU_EKqElNnsj-Cim4xq1KWey5EsuBNA9uAjVHOwfokn7XIk4CSTWYTEbXNbMeJ-uNqssNPddp65bCAz152V-jY0lGwXr2KFoe1UQ-npG-pgm7ohmdVl1EPhOoHlCIzThm47c-8fcd07MU_cDf_1lJQem2A2ye6FeLOy6DYdNodXg-w5vKnW6EE_nkdfKmWU9hdkYHQb0RcJv80Y7hAuWBQiGuMfh-tllEGzdEGM-AkzmVcfUIJ75ykjn5knKpHEIWrarpBNeuDbJD8GUP6jNemJUcqY790knk4oEu9zO7oM2g1AdU6_mD3rsQOF7S_WyEZqk1kl_XWPXXvtxAAipn_-LbEUcPxtWd_XBJDeYf7ERzSeZGp8QmyFOtmvYh1PT33YTZM9Vk4kBOR2lLA7nBVeVf6IPPbkATbUo2ukVA1P9yxpWx-wAqBHK6YY3_m862iRGQ7hRv5aNlXsfJPZgDEmz2t4m4CarGnYVaoPL8VGC91wxwIOdPGT8FVgbib7j5Od-iEqHlmwKJ1Ybgs_KTr8rai4RQoI1YN7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea23085be.mp4?token=BDEkDHmY_f_OfoCkflQ-cJjAqNeRcbsxc8TjqptQc5k-EmC876RMd2oivnW_AHMqg4MsnrDTo7ELdkpTyOX3Lc-ZW32ohrv8AL1Hzvt7AhtFp-ocywlIcpezVivvjMcwVg4iqfePU_EKqElNnsj-Cim4xq1KWey5EsuBNA9uAjVHOwfokn7XIk4CSTWYTEbXNbMeJ-uNqssNPddp65bCAz152V-jY0lGwXr2KFoe1UQ-npG-pgm7ohmdVl1EPhOoHlCIzThm47c-8fcd07MU_cDf_1lJQem2A2ye6FeLOy6DYdNodXg-w5vKnW6EE_nkdfKmWU9hdkYHQb0RcJv80Y7hAuWBQiGuMfh-tllEGzdEGM-AkzmVcfUIJ75ykjn5knKpHEIWrarpBNeuDbJD8GUP6jNemJUcqY790knk4oEu9zO7oM2g1AdU6_mD3rsQOF7S_WyEZqk1kl_XWPXXvtxAAipn_-LbEUcPxtWd_XBJDeYf7ERzSeZGp8QmyFOtmvYh1PT33YTZM9Vk4kBOR2lLA7nBVeVf6IPPbkATbUo2ukVA1P9yxpWx-wAqBHK6YY3_m862iRGQ7hRv5aNlXsfJPZgDEmz2t4m4CarGnYVaoPL8VGC91wxwIOdPGT8FVgbib7j5Od-iEqHlmwKJ1Ybgs_KTr8rai4RQoI1YN7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم از حالا پشت درهای مصلی برای وداع با رهبر شهید صف کشیده‌اند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/446422" target="_blank">📅 21:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446421">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6fb908b86.mp4?token=rTRmgC_EGCuC5zbaEv4ictLnK8YaQg8tBKO_mIYhGTgjc5Z5yyamHVtPEVHwAmRmM4cuvKzJDxsSz-Gq8fczD54Vf27-dJ3fRu3G-8ogpVghBsywFyVbU9Vvj7YxFd1E7_0VwRwQhLvh7_oSndVVRzfrAtxUsfhIUjbcUZj8M_mA7zj1Wbtf5ITNQ8qpKVq4BqQkAh9cOExZQe0PdnXCYHhKA1na7uxyv7IRojrvT6cVNV8CKaeQsrL3A7XbhkVir3ANn8xZJEjhInBUqFK6oi_IzuUe-9i-YN6AXmbnmKCZCRdd9Jawr71rYV5g3cGHyrOSyu6GLsNpIcC6fBGeCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6fb908b86.mp4?token=rTRmgC_EGCuC5zbaEv4ictLnK8YaQg8tBKO_mIYhGTgjc5Z5yyamHVtPEVHwAmRmM4cuvKzJDxsSz-Gq8fczD54Vf27-dJ3fRu3G-8ogpVghBsywFyVbU9Vvj7YxFd1E7_0VwRwQhLvh7_oSndVVRzfrAtxUsfhIUjbcUZj8M_mA7zj1Wbtf5ITNQ8qpKVq4BqQkAh9cOExZQe0PdnXCYHhKA1na7uxyv7IRojrvT6cVNV8CKaeQsrL3A7XbhkVir3ANn8xZJEjhInBUqFK6oi_IzuUe-9i-YN6AXmbnmKCZCRdd9Jawr71rYV5g3cGHyrOSyu6GLsNpIcC6fBGeCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس اقلیم کردستان عراق: جمهوری اسلامی با حمایتی که از مردم در این جنگ دریافت کرد وارد مرحلۀ متفاوتی شده است
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/446421" target="_blank">📅 21:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446419">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZWGIyO8uB4JwWGSMraFJzOz-ETKdrqznhf4b_atbFIRRHcKReGD_M2AxPqJXJskThu0VJKBQgo8Q6qAFvPxkBQnkm0Ogev11gLqSOofhKdIHbZWh1QWpD_17QIJofQi7VfMJAKLvjCaCvyPSebO6Vmx_ZEJKtaivN-Y3c58nHb6ML8Hg4jlApTT3tm8C7Fh7JMsEfZtSmx_PRB7WR3UN549jEC0rGdCKCcF7-C3ddld9d8cCdjNS5rjd4-nCrAJ4j96yxGy1MZczYV3buLcXjgof1k-fx462NOgwG1lusVThP37R7nWJCIF1Uc3BpYjx44o7rF56Ax0fugXqsidEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پورجمشیدیان: ۱۷ تیر پیکرهای مطهر به عراق منتقل خواهد شد
🔹
دبیر ستاد ملی مراسم وداع و تشییع رهبر شهید: در یکی از دو فرودگاه بغداد یا نجف مراسم استقبال رسمی با حضور سران این کشور از جمله جناب نخست‌وزیر برگزار خواهد شد. در ادامه، تشییع و طواف در کربلا و نجف…</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/446419" target="_blank">📅 21:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446418">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPMPjp8_4U5KtIvk48F06TNAKcGnGLBq8kCoZ9PzieLEfWuYubz9CaCKJhpfwObRZxLWm8eLjB_HhzVm1M2YZGvL_ZeNWZJ1yYMB7s--9ipNkfDdDjKfXr4Hv7CeVD4_fouT-sIUwc8QCgjuOebqtOH4AMF3McC0J_Gwj-PI_yRPtjbjkiaN5v7SbgpA30VuO6Rc5TpmSY0j6P6dOmq-LSmiffu4j1LpE5KuPnYGi0oFo7yE61hIFwxqBBqaaphQecmV9E_2RQV6g5FaumHPB25CMZ8Jw_IL2VQ5d1dEmrOIv0Mvo5jiCygIq0hzhy0ocRY8L-r-wPFLg99_2Qv4Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تصویری از وداع سردار سید مجید موسوی، فرمانده هوافضای سپاه با رهبر شهید
@rahbari_plus</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/446418" target="_blank">📅 21:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446417">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5075a6dd50.mp4?token=WH240uKr6R9po-Nb1iF4mjzbOGGRUlBea94tAoFmmsMo4YhucrQ_WoJ2WIfdBFN5Woa9E5CTPoKwSx8I0qxAqjWczmKKi0KHf25VV5XmnZUgZLGYNsibx2EjPr-5PIAq1x9ZRFVE-jqcgZE4fPG9zvZFF0MyxzzH6UNqvdNnVOmJsm44wGVgp1lrluzWrOGUTCjvhtqtojAlwP4vqqgfGAMGi47eqtnUWO6joy-B3pmR5W9yt06vE8faIc0uKB9SCAxsbUliWZsqaGVLU-fpPzu_sSu-OqYw7EeZ6H9Hs_o01ksrufw0m0_KMdDYGupYZ6XN0Uh0XdR_AjOPESZFIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5075a6dd50.mp4?token=WH240uKr6R9po-Nb1iF4mjzbOGGRUlBea94tAoFmmsMo4YhucrQ_WoJ2WIfdBFN5Woa9E5CTPoKwSx8I0qxAqjWczmKKi0KHf25VV5XmnZUgZLGYNsibx2EjPr-5PIAq1x9ZRFVE-jqcgZE4fPG9zvZFF0MyxzzH6UNqvdNnVOmJsm44wGVgp1lrluzWrOGUTCjvhtqtojAlwP4vqqgfGAMGi47eqtnUWO6joy-B3pmR5W9yt06vE8faIc0uKB9SCAxsbUliWZsqaGVLU-fpPzu_sSu-OqYw7EeZ6H9Hs_o01ksrufw0m0_KMdDYGupYZ6XN0Uh0XdR_AjOPESZFIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: رهبر عزیز ما در مقابل تمام قدرت‌ها با قدرت ایستاد و از استقلال و آزادی ایران و مسلمانان دفاع کرد
🔹
تقریبا در دنیا کشوری نیست که بتواند در برابر تحکیم آمریکا بایستد اما رهبر ما این کار را انجام داد.
@Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/446417" target="_blank">📅 21:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446416">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a20753a44.mp4?token=dGVL2c3ItlpOwoo_vYWaTVVQlY38k7ADERIwgeF_8D1v_8gZZ_cdBWy6odB_scI8nWVyN-tTYrk3BlDBeBhmck-Jx_uC5_yIWqz_X_UkMGGyRQUFrKkGI1DteKZj0Gdt3Xo7RF5tdldYNXCyr1RPfnWyywDc-eMYrR8P0Xwl7Q47uJjYbe0n5AerbcfEyv5ilhhe0lSxTf3fmYQ71pfLdbMnhTItucidi79w8A0ttlqT4NkyZwvrWH9L-iVGbOjIPhGRF4O9qEI415TKRJVs-xFMiSgNkyncyx8yQeVG-a61OjVVAI3yLCDUJjmGOpNF_KpSuz4ccv_SNmDoanLypA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a20753a44.mp4?token=dGVL2c3ItlpOwoo_vYWaTVVQlY38k7ADERIwgeF_8D1v_8gZZ_cdBWy6odB_scI8nWVyN-tTYrk3BlDBeBhmck-Jx_uC5_yIWqz_X_UkMGGyRQUFrKkGI1DteKZj0Gdt3Xo7RF5tdldYNXCyr1RPfnWyywDc-eMYrR8P0Xwl7Q47uJjYbe0n5AerbcfEyv5ilhhe0lSxTf3fmYQ71pfLdbMnhTItucidi79w8A0ttlqT4NkyZwvrWH9L-iVGbOjIPhGRF4O9qEI415TKRJVs-xFMiSgNkyncyx8yQeVG-a61OjVVAI3yLCDUJjmGOpNF_KpSuz4ccv_SNmDoanLypA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسعود ده‌نمکی: در تمام سلسله‌های گذشته، خاک ایران از دست رفت و کوچک شد ولی این مردم اجازه ندادند در جمهوری اسلامی یک وجب خاک ایران از دست برود.
@Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/446416" target="_blank">📅 21:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446415">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fe1d1a188.mp4?token=BdRzCtswJdT4KUKSS8TXMpWWsCIAl-4D_wJp9oE-SZzIzWxrzZod60CGAouSZTSD1ilfOe3g4mPvkG3wk_LucSspKDnGLpFYUMqEBLTqn9WVbdRsFyd0O_V3-YeyrFPe3SjEBSzxO2JTmtsy2zrOEHbN5aBN9utRlXglDqUaDqd4HWUB75qZrcMLFLKQu_4h42BNzx4FYmaxb-QvtPPtQjrDIRg8pinl4KIo0PMY4blpEcDcQ0oBuFBd4y77UkwQe5_-PFU6gVfalJG6ZFAld38W2n0biOWLhg4PabSTqKCtJmyO01oinXzOZoAdKikVCo9YslZb7PB7J7U9KsdBVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fe1d1a188.mp4?token=BdRzCtswJdT4KUKSS8TXMpWWsCIAl-4D_wJp9oE-SZzIzWxrzZod60CGAouSZTSD1ilfOe3g4mPvkG3wk_LucSspKDnGLpFYUMqEBLTqn9WVbdRsFyd0O_V3-YeyrFPe3SjEBSzxO2JTmtsy2zrOEHbN5aBN9utRlXglDqUaDqd4HWUB75qZrcMLFLKQu_4h42BNzx4FYmaxb-QvtPPtQjrDIRg8pinl4KIo0PMY4blpEcDcQ0oBuFBd4y77UkwQe5_-PFU6gVfalJG6ZFAld38W2n0biOWLhg4PabSTqKCtJmyO01oinXzOZoAdKikVCo9YslZb7PB7J7U9KsdBVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: رهبر شهید انقلاب همواره ایران و ایرانی را عزیز و سربلند می‌خواستند
🔹
۳ اصل عزت، حکمت و مصلحت با تدبیر ایشان در وزارت خارجه شکل گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/446415" target="_blank">📅 21:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446404">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c187e9edbb.mp4?token=A6-FXA8L6D_v0Xhf9N1-PSCwEVALzauHg0LttqB5jBshkH9ULC04KFIsSLi9S3u_rhUo_aiYQi0CsH0HYQF5WhWR_FwoSdnyiCky0u-S1Se6INWlQt8QteytVw6_B0Ksuk3K6JdJu8PLUNW2a2wO92wx5zkP-eZ62zbwxOyuGR73w2i29J3nPYQOtwLqkzcRnj49NwuQuMg-Yicxs-9qFXf02MXQSKhD2Vbt1wFWSc4lR6dmY-jowBR55iRH6SyKuODdpOm3pMUyb56Mka3HxnIAxU61gIJ3q7L6kAJTirgCnekdBv591mUMnolvEdcKYiGgeAbHphxwYybbkWZE0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c187e9edbb.mp4?token=A6-FXA8L6D_v0Xhf9N1-PSCwEVALzauHg0LttqB5jBshkH9ULC04KFIsSLi9S3u_rhUo_aiYQi0CsH0HYQF5WhWR_FwoSdnyiCky0u-S1Se6INWlQt8QteytVw6_B0Ksuk3K6JdJu8PLUNW2a2wO92wx5zkP-eZ62zbwxOyuGR73w2i29J3nPYQOtwLqkzcRnj49NwuQuMg-Yicxs-9qFXf02MXQSKhD2Vbt1wFWSc4lR6dmY-jowBR55iRH6SyKuODdpOm3pMUyb56Mka3HxnIAxU61gIJ3q7L6kAJTirgCnekdBv591mUMnolvEdcKYiGgeAbHphxwYybbkWZE0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عباس موزون برای اولین‌بار راز گلیم‌های آبی بیت‌رهبری را فاش کرد
@Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/446404" target="_blank">📅 21:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446394">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HunfiGdDVSIV9Yg5aFU0Awd3iSgx3JNwJqXY3EvL7XhfNt-O2QJPENnDxF4ueqcRi73WE-yY_oUZuRj2Fm18js6nTDmYQf0qM6KkqF3NVyI5fU9HEoT0EfmXTdNYapc_BHliYYlg2p4Fz7p0Rt5ec9pIu6p2dgXIA2IjD8YRPje8RKIqAvCNI8sJUiJZ4TGXRa1dMTaY_7p2tQTtVKn_uolL6LXNBkFgDLFU-O55_pX-fmR2p_QAxRWqB4boUZFN6C_DzDtJH9ZZAYLETh4Zm_FmkJRzwAVJUyuCV4K4uxJmjfW6r-AzNlefwswXdKPMukHP4tkSRWLlWlBNIahRGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NtJLLxdFLmum1wfzwbikOZkDA695_YXh8Ske2460sQsjlQabZANNxigRm6R99U9InpXf1AWw5ao6Snimgyk87VYdgJVjcAs5BGenhJsELbberVBZjYFRr5ftZqToH9-YpHWdlosHY5_lNQ5KbCRqR6mE73rnsvtlbYXc8s_Pw0m6E4khg-qPiXvDrK8aqwy48AMjHFo0mn2CBvHzAqbmiLOP7tDxzHzm4zPIcoPnhY3XvGChPUaoG0IA1mgrlP97GH0VKFR_8qkTKaSWN7N12RBSFdNhEsVNOKShIZKlFXNZh4-v9AkvFSlLV04_Hv1BgKrYBpAtHy9x_N_gwVMU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JxJg8roUpM1SaesmNI8ALK6qtJnGzB3G_0NfvgicVwR-7kWuf34X08JYzGg6gTjetcI_w6DRLUBiOrPWfDXRuXgJ4L0Xc-sXnilvQgZHqSDmeTByY7kuGDYS2hI5nsRuKq79UdbwsmOMbBtp9aHAzUJhWPv2fp1wS309OQkcm1zPkj1RXzMLNNp9FanNciS5hTj3DHkgiHcoGeQyXv0dF61puDncwzfTCyCVkgrc0T9sgdiKizBgCMeSXVpfl-5QAihZQ8gQEbshbB1Gkq8ZHZ5IlieHBLYP0zOEW9pHseSQ-2aLKPdolqtzRhXiybvPJtJcpMMrr00uSkWD8jIs7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/juXNcE5odA71O8-2XvZrxsxSy1FqvBFK6YVDZYD7msfQs07IyobD6-nVre0MUon73pBUbkBBG8pMKK-NDLdZyKJd47UjhCe2-xpnOoY1PQsPUnzwNJQNKBAIcek7ZHYmKDYUkI8mlZE6JRugmLCByUVnK_81cPC3rKbgpyLKfOU_M3GtUCAYkipVH2prHJM7DpK3HvERlska3PKQHwDJSo__mYlJeEyorwtXl1L03DsmCVX8fjBaNEEb9jZPJjHi4nvRuKcPPJTr2W0lM3tXZ9F90vMVz10Rv1o9vX9zIo-pWpnybFi17_fmg1vfXPQcXST-1yYI2xXJYR2yds6Bww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vdwSswt9ISwlepzppCwLldCJwPK5mf9QG1eJeSClvIMjJ3OJSFaTzPmlTL4zgCemMLJPO-0gE0U0SStJ4B2nxKWFXfGzB50F181lDqxOIuM0qMK6aVGkA4lSmULoglKbxlDbdRP1BrtpMJB-lg-ib4MfA9xQR9zjsvZ4N-h2KXW97DFL2TjFvAJ6-nOEtIIOtpmsF4fZqyVN3C8_rAh_puPn8z4UYrHaQ2uYpbZigYIN2IXJq3jlALtq27AwPXBFMrRIWcGpXDH1n2vEnyHNZZdcnELNwpFc76XicVEsZN5oROK0_vB66B-GQ-IqPXxxu83JpdAMrMOIBesw8CEcwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dwj90iZu-sPv_0Bz0GEp2UuueSpEIpPtUeNkdLvHdYDEAmNZ0aYQ7F9Zv36fK7jzxrUtgwM8_jOSXIYfWCeuUI6hYXiPk-NcVZaUxUggRK2f3VdCQKfKp8Q-HxuIqFA1HpIpM0ESYAn2uZGkp_DUxWAuytlsla7sbU8RKNb8sxk_nK1uKzs30Kt_c8MS0EqHee1vEaxTky5HZRVUce8kfIZB2iP1AdsMssi1--T-a0bKQGGDHisRPdDd2Z69fAHJWznhP-0LNpxk0JHS2ZoO0aqlFxqCOrlsv7P0ovahf9Ord3dY_VtdcC96QYIDJwxCSJ1ojpkjafO6Hj_wi1HiRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rL500rdf_aL_mmeStcgkROIFYN2HXCoo4u9v32rpcnJZdKWFk0tmuwM9mb86znf4KNrKL14ezNfhUzqln9iNVVU_jlNuQ40GpNJzDM5psncKAoAyMsLBQ_MYEry1VFza5oP1qe8lIxqcBC5qc_aTkQtVS6YKkfECs78IX3-KUazZJTdoJDym45Y_eUSKAGm2SwsNLUwha_KIqCF601Ld8X_TpnMh_fDQvLkIpkOFD53q_cSPTMbSIw7Qc5bqSSef1ebBbClwkUvWOk1XPcmN9wsUqwdda5BuwH_t9eNnzf5R4WjCyqfPI8U7QIkn23G3JLt7XiANBgC2T5bTmBY8xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/av0qHstAzph8vf7Tjs6gaPQDkGJO6lAFEEzVSUnbC5ePIsMzpg3ZJ2q1lXUGd9SKcTpsq_si_-Xx3J0ycnHcr0ZMk973ueUYfyEv-y3VQ_u97gmlM5JkBRgpVijUWIxhzxNoBtCl8zDQIhkThZgb9jZVlLCTuPkQ4RRLs5XilVF0EA9_2JIJaJRqZhF3YXKgA1U6-RDG50yBFQfnzwJ2PtZuNSAocrLetdM1bvEukLNFR10Yx9dnDs6LYhugtXTqJESEsjkpNYdzR6IU4RAeaiIlhsdlZpkznVA-Q5dbSN-6nKMMnvFXoWl7i_9Hb7vgIFC_bafncOvN6ZrAkBANgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XYydXeXMnqhM6kI_j4fw6S7vi5AAdXV3t3Y4ru9kKP2Dq-N8Gplggh8NriAc1Ok4yY21Z51QF0mB3sne-SCz0QOJ9n7xNK7W7lhsgiD8ePmnCJhvzSFVk05CoGtRv7SEdJuyKgqHiFkNkhJ-V_Yu-YDvUGMK9JSrZeu_XEe55zSkbMAm1j530llp9NARYXJ_ov5STb72UErydau1uFVklKqIdxkIY9BfHTpgc8A_YPQhZFAW8m5Dw43Z-5dk_l_DRCCBdckDYPsiNzxIU7NbfPp9BjnrJlG3NHnCJ6qR9ePWyBZFQ4gaWbG651H1SU0oM_QmhSILEGEH3CdU8aYzNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dTVbMsSbxDu2JvW143j1_NZ986hC_UhlfegYx63rEobTAImiWPdq8rdT2hCiRr7vKtOav-jEMisW6DYwnu7qx-2bDorfeAGUHgr9Pmy3z8SOPcD8b5uyIga_0boV7OdXtp5IoMpYuK7RJ3YY1XLFGdQCyinwK9xE4PtvcVJx9Y4ibMB7QVKGBVTHWfoyXEV012_dH_mD73rMMhAN6C3a4F0vj-fpPP2eKKAEuuZ7s6rAfpECCISv1eFrWl0dGrLRbq1z7N5AFhwVml_z-zXWKRuzj7EuQe71wkaDZmkvFj-u5CxgfPwRATCEXeQQIclv15gYiFbb7omct2Raj_GtNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
سرودۀ شاعران در رثای رهبر شهید انقلاب رضوان‌الله‌علیه
@Farsna</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/446394" target="_blank">📅 21:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446393">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca41dc09d7.mp4?token=lIOrnveIf1sfOnpo_EXTAsANvfTti33tkDRolMchgA96Y4n-FwC88c3sOAZeSPKfu3KxjDZEh4cEvAOqgT9s84pcx4s1cts37peCOiBHW5Ynqz3YUNZa__QisiILT8y_TaGrURXOHPvnkuaZtgYd57rUo0c9ec2K_m4iB4KRAk0-DlLu7dUCRQHoRzF73Cw3Og_eB7CQpoB-d6oNmz82rXR9ROuAXGO4I54G_h2bb2uzkGz1E3fmeWnCUNZtEepmgON_DeAexOCzVnMwxSIvzMApMLtPObK8WbloJyfJY3CeSlCboubJGSvzhLfik4CHx1aW_7UduLs-1JSNK86xaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca41dc09d7.mp4?token=lIOrnveIf1sfOnpo_EXTAsANvfTti33tkDRolMchgA96Y4n-FwC88c3sOAZeSPKfu3KxjDZEh4cEvAOqgT9s84pcx4s1cts37peCOiBHW5Ynqz3YUNZa__QisiILT8y_TaGrURXOHPvnkuaZtgYd57rUo0c9ec2K_m4iB4KRAk0-DlLu7dUCRQHoRzF73Cw3Og_eB7CQpoB-d6oNmz82rXR9ROuAXGO4I54G_h2bb2uzkGz1E3fmeWnCUNZtEepmgON_DeAexOCzVnMwxSIvzMApMLtPObK8WbloJyfJY3CeSlCboubJGSvzhLfik4CHx1aW_7UduLs-1JSNK86xaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تو رفتی و بغض، سنگین‌ترین میراثِ ما از این رفتن شد…
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/446393" target="_blank">📅 20:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446392">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f96758e532.mp4?token=FM0ItB7AxdTSwc-okLqcuPQkm8a0HuBtvXYpaPF2sGIYFQKHShIUCuu1zpzP3VuinMXPxFbCQpQsRLnARi-49OaIjFsIAmJN1TwrUSYLG2WAqKjkq4ly649x_EJC94NNgLIeT82_YfsnvdFX3D3FLMwPvt3B81G3Kz5ewbGl92A1xa4fAIOZBhCyGuu8UOJnoA9Uj2RPPjKyGQ2IFTn4tRvN4JyF-0KAmzoVzMIGnMcuQFgmviQ-fC6NI_G-Vfq5mUwBgc1hTB4nM6F4OVbJnZK1ha18x3TLcS61hoCxS6ihjlk8KFEQ2qQPbpgvPIqNU0pt0BWjtqqE69dP7iC4Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f96758e532.mp4?token=FM0ItB7AxdTSwc-okLqcuPQkm8a0HuBtvXYpaPF2sGIYFQKHShIUCuu1zpzP3VuinMXPxFbCQpQsRLnARi-49OaIjFsIAmJN1TwrUSYLG2WAqKjkq4ly649x_EJC94NNgLIeT82_YfsnvdFX3D3FLMwPvt3B81G3Kz5ewbGl92A1xa4fAIOZBhCyGuu8UOJnoA9Uj2RPPjKyGQ2IFTn4tRvN4JyF-0KAmzoVzMIGnMcuQFgmviQ-fC6NI_G-Vfq5mUwBgc1hTB4nM6F4OVbJnZK1ha18x3TLcS61hoCxS6ihjlk8KFEQ2qQPbpgvPIqNU0pt0BWjtqqE69dP7iC4Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار میهمانان خارجی مراسم تشییع رهبر شهید انقلاب با رئیس مجلس
@Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/446392" target="_blank">📅 20:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446391">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgDBLDwUbFIGrC9_e4Ut8YguY-f6jX2utvuLsZ2x0XRLbrGYMEWT5YzqqwLHA5kro7hezG5_MTLlwb4eDTeNvaextLo8W5r7GhavypD-X8XbUit5zjesrHYUMmmRunjJwgGURL-zuKXbIBLy8GJaZY-KmSgZyBLscg8U2Cp5RrEGEOAZLh2RCYvpaSoSuFmxyH5qnVWrj7CchTDnWCONGMi1HvWzdeNlmid7WiHUKOfudbmWcgyMId3bFhPy6FhKIxWBndgMazdde4AZVPADpW_5uyjNMbAWyQfEo_x9NMXM9rbfCYJoq7HRUOLYF3wK4VbxopeTNM9QoB9M7X-U8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
کدام مناطق بدون محدودیت هستند؟
این مناطق یا محدودیت در آن وجود ندارد یا کاملا وابسته به شرایط لحظه‌ای پلیس است.
@Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/446391" target="_blank">📅 20:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446390">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44caeda318.mp4?token=ccRU8QvSEa-S31ZQAYzTHvRGD7Lm8xlAoUsQKPzlQs8yZtp9hXPDEyIcoj96dMXIcb951xDJULn1H96apUbZJqn_q2roW3EOSFiphxYwbDKH6UjaOKeYlTgMKeajcsUKw1PoO3rtKJjohHZg52bSjIzyRKzagMfYsawvoa7NgkfAaCJmLgShOFzJwqjC4XYOVkazQ2m_yPpMuv1ewhterh-fR8eQEhURaDFWnKiLNU5iBsYc3PGyLSJspElEkPUkabuz39ScBjexItuaRAcKP_eg_5UJzY36j1cA3sR8aN-UP73sPP622ichWp0WfwEa-r6tjVBlJIFuskwmeyTebg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44caeda318.mp4?token=ccRU8QvSEa-S31ZQAYzTHvRGD7Lm8xlAoUsQKPzlQs8yZtp9hXPDEyIcoj96dMXIcb951xDJULn1H96apUbZJqn_q2roW3EOSFiphxYwbDKH6UjaOKeYlTgMKeajcsUKw1PoO3rtKJjohHZg52bSjIzyRKzagMfYsawvoa7NgkfAaCJmLgShOFzJwqjC4XYOVkazQ2m_yPpMuv1ewhterh-fR8eQEhURaDFWnKiLNU5iBsYc3PGyLSJspElEkPUkabuz39ScBjexItuaRAcKP_eg_5UJzY36j1cA3sR8aN-UP73sPP622ichWp0WfwEa-r6tjVBlJIFuskwmeyTebg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خانه‌های کوچکی که دل صاحبان‌شان بزرگ است
@Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/446390" target="_blank">📅 20:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446389">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/280e9a8a2e.mp4?token=m5e3VaRb87f7w4F1C2GtHVRfWZvDRbneT2_f_BeFTvSeC_hmIDUh1bpnD6kcB-eyrMZo0WxVvEPFLPNaAZ6OJAgEZ9oov4v1tOkj9JGht4usbo2qTDldw4qWpOdcYu1ukFhJWeV6ntmDdbO7lh4M5Ufa4qR3znHP1Q-KWQ8oSepOlOuPyN-yNuFkSxQpzVvfEWgrcW1xixxrludgp5TyDLnDzMvY12W2gcDO0knGjxaYaKd_3g3BPJdty8FxFv8meUouYTPd2upln83gXiAhhC1R81Yt8LairAsMMrN8AEX2xpGNeKc1Ec1LLL9mz66iQeiIyOZpjE8e48ByGDG5Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/280e9a8a2e.mp4?token=m5e3VaRb87f7w4F1C2GtHVRfWZvDRbneT2_f_BeFTvSeC_hmIDUh1bpnD6kcB-eyrMZo0WxVvEPFLPNaAZ6OJAgEZ9oov4v1tOkj9JGht4usbo2qTDldw4qWpOdcYu1ukFhJWeV6ntmDdbO7lh4M5Ufa4qR3znHP1Q-KWQ8oSepOlOuPyN-yNuFkSxQpzVvfEWgrcW1xixxrludgp5TyDLnDzMvY12W2gcDO0knGjxaYaKd_3g3BPJdty8FxFv8meUouYTPd2upln83gXiAhhC1R81Yt8LairAsMMrN8AEX2xpGNeKc1Ec1LLL9mz66iQeiIyOZpjE8e48ByGDG5Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشور پاکستان: رهبر شهید در یکی از دیدارها دست سید عاصم منیر، فرمانده ارتش پاکستان را به گرمی فشردند و به او گفتند فرزندان حضرت علی(ع) هرگز سر خم نخواهند کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/446389" target="_blank">📅 20:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446387">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmoS48fvRula-2tCQ7ou62UOy5bWlZJQvFeSdHnn0LMD9Uz_QY20GEuNRCcoub-EJmquK2HWkqhnT-wVBRZQ9k03jAnquO3LBpSK29eamz6c1xuiAdiASO_gtEiTajn0R4fPUFwR9xK8VMipk7F3bw-Ycjc3elDIy1PK0EOtdlDicI1VhjHKQjCpjYJV_9D1z792Kzixfbu6v9narjNGo0Ok0NWMpvXznOn42nGF7Spzx694Hmm2yNVQxjzB7mUpMo7Et5-UrGbO_e9jjznmW8e4u7_b3Hb1Aj7xqKSeFXvn5jnP8Sy9Tzb7OAkkT3hT7hckp8eZUV7N5kEZQiKf9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ادای احترام مدودف، نمایندۀ ویژۀ رئیس‌جمهور روسیه، به رهبر شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/446387" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446386">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58817a5d50.mp4?token=T69rcohYP1mPWXO_ozV7DPPzmw3cGgET1MTJih3dr8rm3GKqzJ31MZz3R-CLSDC5MKOs-uWGZuHooVFHTqm8lUY1fm7g2ahEf1Rgpv5mgHS9VIpmm-nAOFkCtKd2SUGNYsWFVUD5IYNWmWRnx19lh8mrJq5X9DMfpd-eM0089oaB5OLCP9JZGa8vleQ95GiHx7H7iTBj5j2nYjXAj4HTXhUkUn6CFB8-zIAgrDLkqzEP0VnIYqgBz825aGP0Pge9dUp8elwPiv_7jMqJCCo21x3FcsOh9EV5lHUaR9BuO4ih7Nz0Eb0eWRfWNqiTJC92BwLLhsVWwCZYsqofOvYMIa1LZpcsRNFFwBRtpmY3jn1kBD323aSvAYLPIPHd75wSCQ9wqUFuUC7asoQ1-nNYmfU4P6MGeVOjgE3ZuprHjXWDyNbytjGQE98UoMsgEPW1j_5M1S6XPEsBu6B4SviwmiHMFYXoqRzVI2Pk4kvVwunK8PMChLbUzDvxMrb04_l2U6lx-KsTh8EPOBnpNJl9zHAHU1bbMLTLzjU4mWBs-BQmA_NYo4NLC8SeJYayXEBX9WuK43gcKZAR3bcWEvcPXo8I1yZgL4VF-Z_91Rlb0FjFQseMNjQnEziwtZTj_9QHpwrgSLLJsPXTIli-9jEfe7pGxpMClmjArtMRb_Ol6uc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58817a5d50.mp4?token=T69rcohYP1mPWXO_ozV7DPPzmw3cGgET1MTJih3dr8rm3GKqzJ31MZz3R-CLSDC5MKOs-uWGZuHooVFHTqm8lUY1fm7g2ahEf1Rgpv5mgHS9VIpmm-nAOFkCtKd2SUGNYsWFVUD5IYNWmWRnx19lh8mrJq5X9DMfpd-eM0089oaB5OLCP9JZGa8vleQ95GiHx7H7iTBj5j2nYjXAj4HTXhUkUn6CFB8-zIAgrDLkqzEP0VnIYqgBz825aGP0Pge9dUp8elwPiv_7jMqJCCo21x3FcsOh9EV5lHUaR9BuO4ih7Nz0Eb0eWRfWNqiTJC92BwLLhsVWwCZYsqofOvYMIa1LZpcsRNFFwBRtpmY3jn1kBD323aSvAYLPIPHd75wSCQ9wqUFuUC7asoQ1-nNYmfU4P6MGeVOjgE3ZuprHjXWDyNbytjGQE98UoMsgEPW1j_5M1S6XPEsBu6B4SviwmiHMFYXoqRzVI2Pk4kvVwunK8PMChLbUzDvxMrb04_l2U6lx-KsTh8EPOBnpNJl9zHAHU1bbMLTLzjU4mWBs-BQmA_NYo4NLC8SeJYayXEBX9WuK43gcKZAR3bcWEvcPXo8I1yZgL4VF-Z_91Rlb0FjFQseMNjQnEziwtZTj_9QHpwrgSLLJsPXTIli-9jEfe7pGxpMClmjArtMRb_Ol6uc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین یکتا: این وداع آغاز ورود ما به مأموریت جدید در مسیر تمدنی و رهبری سوم انقلاب است  @Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/446386" target="_blank">📅 20:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446385">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d118f99fc.mp4?token=BVKs9IYN2mV_14eejJiA0Cm0O1ICkqt27T-2PrmpdW7aHeF8z_8Gcj_f1zhau1abip9wRgOGox2YYSYK2WK3Qp0cqVUhGZSSsXLeS3B8UjFCoDrH6RGpY4HdFkKKyW3ac8YVOiVpLxwb7smnwzyQsMWgA43eZC1anrkPyB2P_cYG09DA6BeLwJsAuXE7qbqlOj0oSosEsUriJFcgMjxal2QUdj_wp1-m1HfLLsKlBFKIr9JFNTwH8D_SkfPK8gyADMaIMpWfcAw6ureI5MtdI7wvWUlKTWDWDh9wO6w7JVLLK-V-AxhxaFkSZiRPgOGmXNb5yZgG-39ugrhRp0m1RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d118f99fc.mp4?token=BVKs9IYN2mV_14eejJiA0Cm0O1ICkqt27T-2PrmpdW7aHeF8z_8Gcj_f1zhau1abip9wRgOGox2YYSYK2WK3Qp0cqVUhGZSSsXLeS3B8UjFCoDrH6RGpY4HdFkKKyW3ac8YVOiVpLxwb7smnwzyQsMWgA43eZC1anrkPyB2P_cYG09DA6BeLwJsAuXE7qbqlOj0oSosEsUriJFcgMjxal2QUdj_wp1-m1HfLLsKlBFKIr9JFNTwH8D_SkfPK8gyADMaIMpWfcAw6ureI5MtdI7wvWUlKTWDWDh9wO6w7JVLLK-V-AxhxaFkSZiRPgOGmXNb5yZgG-39ugrhRp0m1RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین یکتا: نسل به میدان آمده بدانند نباید از خون شهدای انقلاب گذشت و باید آماده اطاعت از آیت‌الله سید مجتبی خامنه‌ای باشیم  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/446385" target="_blank">📅 20:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446384">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec73618ea5.mp4?token=v8AXhU_QvLnD83Izi_TwBd8dSgRUcDm0LtL1_Cu7vhKQeKJFYVuvYZW0UigkBc7pOlVq1bPP-0gQxZPZSDLa2u3GLDqdc--fuBt__O4S3hbY2FwatPgBLsgdsWRVjtXzwvIg7gSspvsPN-dmNB1SyHQQ6sOZkCrt8o_-fr7TqafzuYg-axHiN3Z0vNiuNdnlhvbGpjnGBdxY3RMhimW56lr6xqxUQ7z7uXp1sF_ZzD5-TD7yUptKA6JM5TAJAO_l38vfN4_6amjviIpOReSkRMsoKHPmQ6TjHT4q6N0NxvrjWJGNlZXYzyXHIjjhexT1rNnxCyiE27gu0qARbXG7gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec73618ea5.mp4?token=v8AXhU_QvLnD83Izi_TwBd8dSgRUcDm0LtL1_Cu7vhKQeKJFYVuvYZW0UigkBc7pOlVq1bPP-0gQxZPZSDLa2u3GLDqdc--fuBt__O4S3hbY2FwatPgBLsgdsWRVjtXzwvIg7gSspvsPN-dmNB1SyHQQ6sOZkCrt8o_-fr7TqafzuYg-axHiN3Z0vNiuNdnlhvbGpjnGBdxY3RMhimW56lr6xqxUQ7z7uXp1sF_ZzD5-TD7yUptKA6JM5TAJAO_l38vfN4_6amjviIpOReSkRMsoKHPmQ6TjHT4q6N0NxvrjWJGNlZXYzyXHIjjhexT1rNnxCyiE27gu0qARbXG7gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین یکتا: نسل به میدان آمده بدانند نباید از خون شهدای انقلاب گذشت و باید آماده اطاعت از آیت‌الله سید مجتبی خامنه‌ای باشیم
@Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/446384" target="_blank">📅 20:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446383">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nu_17sljRJMxiAqagH4nCwq7rDA7iCls9CQTcN0HZaxIrcQkuqyAcGlkoRJkngbHfTjsKyVV1BUsj_vhZjP-397NfOevNM3Er2BCrcJtc344tuxeAo0x6iCq6kTqr-nlfi-nJM1VQCaxV3mw2NSLvldAXJ4gHm3Vq4vCfXoZzQkKwP-67bO6O-vD35ZSdNeI9ZA5j4rTIKlm4KnPOHN8-lJd9KPYokSghPnBKWSCE9pxLVk2zfdsYfceJnoDA_BPxZAsjdqGVaic9r_kqzJcysdU5OHjud3_0czqDUY7g0EQh2i-WaA_a7sW_y5O9vHQIZ9DKx660T4Wf7A8On1VDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قاب ماندگار از پیکر مطهر رهبر شهید انقلاب و شهدای خانوادۀ ایشان در جایگاه مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/446383" target="_blank">📅 20:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446382">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99d2988441.mp4?token=BSnHHoQHTaF1_MnCbexC3JcohB7UjLzyo92X-QFoY7UcFklIKK7US3FlxK3USFI7EFaawgrz3xYmLZaK2sd1jOuG6wG808_e1WHVLKPSTqvJryf1dqQaC5sQm0V9sWy-ge0iWvkws_diBtoO7IG8EZw-hYK80D5SKHIbluxhbyaja30e0TTuruQiU6LBZKj9qu5MrWkNFs6yN_M9mp5XmBgYRZPWceyMSfqlUuD83pecQTh3QVlB1N5lw4ssKzcMhEKdy_hvvC-cb6oWRzT3a7EYYU2PiWgMScyUnbDZ2g-XmgEL_p890Jo9VGpM2kHCyo0NdSADoUHx44rag_dPow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99d2988441.mp4?token=BSnHHoQHTaF1_MnCbexC3JcohB7UjLzyo92X-QFoY7UcFklIKK7US3FlxK3USFI7EFaawgrz3xYmLZaK2sd1jOuG6wG808_e1WHVLKPSTqvJryf1dqQaC5sQm0V9sWy-ge0iWvkws_diBtoO7IG8EZw-hYK80D5SKHIbluxhbyaja30e0TTuruQiU6LBZKj9qu5MrWkNFs6yN_M9mp5XmBgYRZPWceyMSfqlUuD83pecQTh3QVlB1N5lw4ssKzcMhEKdy_hvvC-cb6oWRzT3a7EYYU2PiWgMScyUnbDZ2g-XmgEL_p890Jo9VGpM2kHCyo0NdSADoUHx44rag_dPow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ستاد تشییع و وداع با رهبر شهید انقلاب: درهای مصلای تهران فردا از ساعت ۶ صبح به روی مردم باز خواهد شد
🔹
در صورت فراهم‌شدن امکان بازگشایی درهای مصلی از امشب، اطلاع‌رسانی لازم در این مورد انجام خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446382" target="_blank">📅 19:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446381">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a2abe920c.mp4?token=jpzBDlSnRlp43lp0JacE_6JBjpmGBUyZq4EGpuyjbbKcTrd3qFQZer62wiBQ2KDs7TXil5JEqdovw85IlP37qYBUro5MiujuP_fb6XQKOdVmcFEl8pS_JCK9QCNsBN75RbbdBkfcBeF9xOzW1r0sCOlM03QO7HE9R0FZDmj2gHzWGwNaxNEptTGo_b3bzF7YOYzzO1-Cs1UbO9oaty4SlygmlR9FIhl_YwO2y7GtbZ5UX236fWZimGhiwj6PL6ydILE8IFPSWFDlSaiFTmV-2NosqJHvailzYVB6VIQJRRaggCc4Q-xAlTL1olV1Fp7WDz0MWU2TNK3pKfC5O-FIeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a2abe920c.mp4?token=jpzBDlSnRlp43lp0JacE_6JBjpmGBUyZq4EGpuyjbbKcTrd3qFQZer62wiBQ2KDs7TXil5JEqdovw85IlP37qYBUro5MiujuP_fb6XQKOdVmcFEl8pS_JCK9QCNsBN75RbbdBkfcBeF9xOzW1r0sCOlM03QO7HE9R0FZDmj2gHzWGwNaxNEptTGo_b3bzF7YOYzzO1-Cs1UbO9oaty4SlygmlR9FIhl_YwO2y7GtbZ5UX236fWZimGhiwj6PL6ydILE8IFPSWFDlSaiFTmV-2NosqJHvailzYVB6VIQJRRaggCc4Q-xAlTL1olV1Fp7WDz0MWU2TNK3pKfC5O-FIeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جای آقای امام رضایی در گوشه‌ گوشۀ حرم خالی است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/446381" target="_blank">📅 19:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446379">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۸۴.pdf</div>
  <div class="tg-doc-extra">3.8 MB</div>
</div>
<a href="https://t.me/farsna/446379" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۸۳.pdf</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/446379" target="_blank">📅 19:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446378">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzIFuT8-CNTnGMp8LdqRmyf6rF36Ib3sRzWoSygpt1U_ErcUAJtmK43kPdjQeOIMOqNVztPVqZ2Ss03zn13DWu7fW77BIgKkGo_EGxEh_1NGf9150Kel1Vlpa4PbsNx-22fwbNSo_SojvSzbGH_SFdUH6ckYot87eNwEqv8CASSFTZXMZ6Du_ZX1f1RszDZcph0YZMpJD8GQa7YFaRCqqOd27CYjJCzGbJQvIeH8AYsApQ5dyEiFmlo6hoV3XWnfhkBrIHrTAbeqVtGFByHPmeQgSlDOMKql12PjSO-yWhMVQyWkdv-elQMVd5CTBNuf3VdEByfMJx_gORZCorgwgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوت از عراقچی برای شرکت در نشست آتی سازمان همکاری شانگهای
🔹
دبیرکل سازمان همکاری‌ شانگهای در دیدار با عراقچی در تهران از وزیر امور خارجه ایران برای شرکت در نشست آتی وزرای خارجۀ این سازمان دعوت کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/446378" target="_blank">📅 19:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446377">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پلیس فتا: فریب اخبار جعلی دربارۀ مراسم تشییع را نخورید
🔹
رئیس پلیس فتا: دشمن با انتشار اخبار جعلی به نام برخی مسئولان و رسانه‌های معتبر خارجی، در تلاش است فضای مراسم را ناامن جلوه دهد و آرامش روانی مردم را برهم بزند.
🔹
از مردم می‌خواهیم به پیام‌های ناشناس، اخبار غیرموثق و محتواهای مشکوک در شبکه‌های اجتماعی اعتماد نکنند و از بازنشر آن‌ها خودداری کنند.
🔹
تنها مراجع معتبر برای اطلاع از مسیرها، زمان‌بندی و اطلاعیه‌های مراسم، رسانه ملی و خبرگزاری‌های رسمی هستند.
🔹
مردم در صورت مشاهدۀ اخبار جعلی یا محتوای مشکوک، موضوع را از طریق شمارۀ ۰۹۶۳۸۰ یا وب‌سایت رسمی پلیس فتا گزارش کنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/446377" target="_blank">📅 19:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446376">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4820db050.mp4?token=aXd4mRiFnTOgmxxYElZthuU7lv_fjvno_-oRr8SurmXepc-NVVU0gxiHAq39OLw1eF4j6OA9aOwe8ujhIaWf5o4k_ofTPMBpD7a07dNcTMVXmnVxUfHE4YUZUQuPxpAaR2_s-Vh7Y-9H0ujby48eT2EDmL1xre2-tptG95oiKYE8wCBqjqEobJ_NAKtmFne11_r6knO6LmJFrVL0dcQ_bLmGfjHbqtso_mzNKdsEDfY-VJoDiSZrrH5kwew0lINLhbYsPZAmyIgkyl8bVdcgTyp5ZIVZ694srJ0j2Fk1mE02OMEw8J3SCSqyELGL1lork8xITWWTaqIpwrT5eDusd0FLsSmnByfj9FMwjSZqzpQYPPTvhRny71Z5ZZ37TMqtcVhjy7ydMazYzoOy9rPcnfh2ujU0u5anYnykKlyplrvR-nuzBRpiZcMPRZBfp8Ie0qEA8_BiqM-nlinnqvmbYJhZGuENUSqKmn52cse8T7WnXE5PXAOKLBcTfhc9KcwRJYtVA0FsxDhhUNoY17dhE-gdj3kK-2oJYGDwUfAaT2R6PPld928cittsWJWyMvTzttL9FMqTZv5u4xAt1VBeEJfYeU1tFXHWPzg2xCcxaLmpmPHp8k7_slctn9CR7SbQ0YYqkYmlIHQs_c1XejVNj6HhtcdbyCsQPqrBhnT_svA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4820db050.mp4?token=aXd4mRiFnTOgmxxYElZthuU7lv_fjvno_-oRr8SurmXepc-NVVU0gxiHAq39OLw1eF4j6OA9aOwe8ujhIaWf5o4k_ofTPMBpD7a07dNcTMVXmnVxUfHE4YUZUQuPxpAaR2_s-Vh7Y-9H0ujby48eT2EDmL1xre2-tptG95oiKYE8wCBqjqEobJ_NAKtmFne11_r6knO6LmJFrVL0dcQ_bLmGfjHbqtso_mzNKdsEDfY-VJoDiSZrrH5kwew0lINLhbYsPZAmyIgkyl8bVdcgTyp5ZIVZ694srJ0j2Fk1mE02OMEw8J3SCSqyELGL1lork8xITWWTaqIpwrT5eDusd0FLsSmnByfj9FMwjSZqzpQYPPTvhRny71Z5ZZ37TMqtcVhjy7ydMazYzoOy9rPcnfh2ujU0u5anYnykKlyplrvR-nuzBRpiZcMPRZBfp8Ie0qEA8_BiqM-nlinnqvmbYJhZGuENUSqKmn52cse8T7WnXE5PXAOKLBcTfhc9KcwRJYtVA0FsxDhhUNoY17dhE-gdj3kK-2oJYGDwUfAaT2R6PPld928cittsWJWyMvTzttL9FMqTZv5u4xAt1VBeEJfYeU1tFXHWPzg2xCcxaLmpmPHp8k7_slctn9CR7SbQ0YYqkYmlIHQs_c1XejVNj6HhtcdbyCsQPqrBhnT_svA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع با پیکر شهید مصباح الهدی باقری کنی داماد رهبر شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/446376" target="_blank">📅 19:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446375">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249dde3f7a.mp4?token=Fq7bF5479i7opLDaomsfgKlyAe9V-n7VGOAXVdad9R4L-gjPq3_HrCOvWX2fJtlwNa7N8gZXYtogTrae9we5qyiQHrU7JzxTDtQknXsTABi7AqG_rts1jzsYKhgBWXaEoI5acKDx_kkeM3ICbFPsJmC2jEjCBfgz-Ew8rCtZgAaA3bg2wzs79hpF_VktZMtxhmfcJnL-uK-o04CiOduKOyIjs5opnbB1mTgnM9YBCMYKJkBY8LY5lSSviAcEcVgKGP1SZRJ-83KcT6M5oXnRyHegUbuw9iru2-1_oWEtFPgsMhbvtH-1Hgcag4CN-0EC_BerS2D9te7mFmwej0fdGmUvI1jy7W--NDU8SGViaKea0tFcA7oNPhhD5iFc-SodjI0cVohCutc37GDxxZ50zMKm23EhIQADCHX2-4-momlZw0ds44ffkXU_CKoiJ6FrBNKTULefKYiZ-TcABc66DEghiyuTziCOBNzCJXdylbUQY_EfjnqewaZEMTSdJZ-_tyvWqij2yUwr24zHPyQkqrZK2vqzDdyuJa9HkqZeCwKi6IqDJg1g9I1LpU9ofHHI7hJVrCL0sJoWnxFmGJ5drqoZZkWGVAbLzq0KMors73TfywfQ90c1mMcJJfi0d_cgz21u85p05O3pUWEx9W0H-cdkOTyPJAE2TmuAs1pmBww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249dde3f7a.mp4?token=Fq7bF5479i7opLDaomsfgKlyAe9V-n7VGOAXVdad9R4L-gjPq3_HrCOvWX2fJtlwNa7N8gZXYtogTrae9we5qyiQHrU7JzxTDtQknXsTABi7AqG_rts1jzsYKhgBWXaEoI5acKDx_kkeM3ICbFPsJmC2jEjCBfgz-Ew8rCtZgAaA3bg2wzs79hpF_VktZMtxhmfcJnL-uK-o04CiOduKOyIjs5opnbB1mTgnM9YBCMYKJkBY8LY5lSSviAcEcVgKGP1SZRJ-83KcT6M5oXnRyHegUbuw9iru2-1_oWEtFPgsMhbvtH-1Hgcag4CN-0EC_BerS2D9te7mFmwej0fdGmUvI1jy7W--NDU8SGViaKea0tFcA7oNPhhD5iFc-SodjI0cVohCutc37GDxxZ50zMKm23EhIQADCHX2-4-momlZw0ds44ffkXU_CKoiJ6FrBNKTULefKYiZ-TcABc66DEghiyuTziCOBNzCJXdylbUQY_EfjnqewaZEMTSdJZ-_tyvWqij2yUwr24zHPyQkqrZK2vqzDdyuJa9HkqZeCwKi6IqDJg1g9I1LpU9ofHHI7hJVrCL0sJoWnxFmGJ5drqoZZkWGVAbLzq0KMors73TfywfQ90c1mMcJJfi0d_cgz21u85p05O3pUWEx9W0H-cdkOTyPJAE2TmuAs1pmBww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرخ است افق، خون تو پاشیده بر افلاک
@Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/446375" target="_blank">📅 19:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446374">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAQVJ1yrGPKaaicmHK79SuoNl2Fq1hSYCHJTJCB9FhIy97qMonSq8_Q8fOOiwdpRBHj8vrCHPpOiN1kh6ETOcmEkVMdYnE179tkP-ijjkg2G7vYpaxyl1duMLbMv8BA4FQw39a14VknfoJo2WqCtn22fJGXieuZsAtqRs91Ab_v7Cu3u2Fyd9A4rIK7a08AjvVgn2nw3ouyARITVTthTVM0vyTvtu05XeKX35S6lboyKwUC4v1T9cvfZgLoLMSg9krEYwL2nZRGZY0h3nGuFEeKIizMTAUi4ycLEy8LojB_M3yehbIjvsecW2BiLh5HZioJ9agR4p3HYGHXnH-pB7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نقشۀ زائرشهرهای تهران برای اسکان زائران استان‌ها
@farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/446374" target="_blank">📅 19:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446373">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Svyq7j0tggyAHdBUpkbztEKe72MrEcXq1QD6QC4nch92k_tTgcDVWl7GuFO-jXuurJR01EGBQehDknEhncbkAs2gBgg0wQjLQCEMpEejFqF29Yz33PUCp_9Z-FUHARBNlhSipa8Ii5tzs3Dffh_TP_hc_2ekpt4-sIkJm6knhmBqs0vWU2vHN_zhKbMsgphzJ7cbOS4Zl6whUGll0XsXXFr-e212pNdvFEFRei0cOqw99ImxmqrTXeP5YRVYoXVtnvPO0Oi7h06Ex70UVXZcCH_oRkwmGqcmj7BoNoas5fqfGnkcGEBBSuRnmG1l6yNa9cS9iIl2GlBtNh9QggHVeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
متفکر الجزایری: نوۀ رهبر ایران را تمدن اپستین کُشت
🔹
یحیی ابوذکریا متفکر الجزایری : آمریکا، دموکراسی، تمدن و حقوق بشر... دختر فرشته‌گونه زهرا، نوه آقای خامنه‌ای را با موشک، نه، با تُن‌ها موشک کشت. این تمدن شماست، ای فرزندان اپستین.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/446373" target="_blank">📅 19:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446372">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8accf60db.mp4?token=YPMOE-BHH_ZoVFnnkAmiqq-of2tPFy-jdiRF3n_8LssMWIs1njM12wn6BNBHIZrMvQaRh6aktikWIeikASI9VwsgMpvptduUWFC3tDC6ZXAoSc45fG9ndEjaumUEYfSfb_4alJM0HT84FLET1My9dle13Xap6zXNTTr8aMMCbEXV-5DSaybNCa4au1WGACzqGMoqmuwONiMucngINjhPs-4wNJwGkGPI9HTZKsdFaGRF0mWn1c-4FRuvf_kYobKvlPLKCAo7Y2AMG9Aq3kEH5nS07p2x1ToIRHsK2iDcAxCDrsgJKViRX5BzJcQZhvRRrCl--eG__tIf24Vrk7I0aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8accf60db.mp4?token=YPMOE-BHH_ZoVFnnkAmiqq-of2tPFy-jdiRF3n_8LssMWIs1njM12wn6BNBHIZrMvQaRh6aktikWIeikASI9VwsgMpvptduUWFC3tDC6ZXAoSc45fG9ndEjaumUEYfSfb_4alJM0HT84FLET1My9dle13Xap6zXNTTr8aMMCbEXV-5DSaybNCa4au1WGACzqGMoqmuwONiMucngINjhPs-4wNJwGkGPI9HTZKsdFaGRF0mWn1c-4FRuvf_kYobKvlPLKCAo7Y2AMG9Aq3kEH5nS07p2x1ToIRHsK2iDcAxCDrsgJKViRX5BzJcQZhvRRrCl--eG__tIf24Vrk7I0aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پنجرۀ متفاوتی به مراسم امروز ادای احترام نمایندگان کشورهای خارجی به پیکرهای مطهر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/446372" target="_blank">📅 19:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446371">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🎥
سلام بر تو ای وعده‌ی تخلف‌ناپذیر خداوند
@Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/446371" target="_blank">📅 19:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446370">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7abad4ed.mp4?token=ePDw167T_C697gHQgdxIeplefOLZsRDVrHnDdlEbkQcq0AdbsvV8CpcGuitNuIVHlc6cG7hTX8FTH5m891mIpVOXoZXblnk5sM4us0tsPMlXxuECVRCjHdHRjt0M23gw4pj-hq6wjXwwpKJWA27z4qNo-n78_nS78uvMFv_XquV7mlFd88gPfI3Z822zCkznYKBfa2Kkpv3aT6teRnkEOmZwVgRI8ZniukmEtfirLaTpm93OMOkoYsBSzCBxbiIP3ybnmQghsSKtaJQXvVH6WrIuqmm8DXqSxO5IsjrHNvg7056mWE6tpUKT1rLDXWNqfw-dgCeXZxXtOP3ta7a1ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7abad4ed.mp4?token=ePDw167T_C697gHQgdxIeplefOLZsRDVrHnDdlEbkQcq0AdbsvV8CpcGuitNuIVHlc6cG7hTX8FTH5m891mIpVOXoZXblnk5sM4us0tsPMlXxuECVRCjHdHRjt0M23gw4pj-hq6wjXwwpKJWA27z4qNo-n78_nS78uvMFv_XquV7mlFd88gPfI3Z822zCkznYKBfa2Kkpv3aT6teRnkEOmZwVgRI8ZniukmEtfirLaTpm93OMOkoYsBSzCBxbiIP3ybnmQghsSKtaJQXvVH6WrIuqmm8DXqSxO5IsjrHNvg7056mWE6tpUKT1rLDXWNqfw-dgCeXZxXtOP3ta7a1ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خدا دلم ز تو نگشته ناامید...
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/446370" target="_blank">📅 19:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446369">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a69858ce4.mp4?token=Zk7JFCYjN-z2GcZvj_j6rzPGEM0ClEM9ewvGSEm_EHL_pWlUDoRQilRmiWbcFqMyi8UDTtGm5oInvKmp4fi4KuDsYiW8_n26aDkW1j9DMMA88wHmiHLv6t6Gvoo-hCzuePDYS9O2fIyBt3xBhnzdcg8en_kMToB1BIAlNiuiH3Pn_fR0s4rMbt9UN9cpUoLXvd1nP-zM_esoOa9g5PDZ3qGndIDz5rFIfkt_WCS3gi2OPCvvvyl5KAqHzlwNlQkW4EAxPO2Fjx-pTsf3xDR9DC1m63DDgm6Bf3hNutn56GwOX4yys1X2-Ee3N8qJFA4wxZGujwJ2zYUvegHvFh1Fkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a69858ce4.mp4?token=Zk7JFCYjN-z2GcZvj_j6rzPGEM0ClEM9ewvGSEm_EHL_pWlUDoRQilRmiWbcFqMyi8UDTtGm5oInvKmp4fi4KuDsYiW8_n26aDkW1j9DMMA88wHmiHLv6t6Gvoo-hCzuePDYS9O2fIyBt3xBhnzdcg8en_kMToB1BIAlNiuiH3Pn_fR0s4rMbt9UN9cpUoLXvd1nP-zM_esoOa9g5PDZ3qGndIDz5rFIfkt_WCS3gi2OPCvvvyl5KAqHzlwNlQkW4EAxPO2Fjx-pTsf3xDR9DC1m63DDgm6Bf3hNutn56GwOX4yys1X2-Ee3N8qJFA4wxZGujwJ2zYUvegHvFh1Fkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چه کامیون‌هایی می‌توانند در شهر تهران تردد کنند؟
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/446369" target="_blank">📅 19:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446368">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bef907830.mp4?token=HSBMcJ67JEgN5bRfQeTrRKohLpt0pc6GuLrQrQaT2SoGln9hmvqhRX3YYure0iTUQ2GnGPhhItz6ES4vuo9-nn3U7WYBg-tCoEiibljPZ3QDsMmUaLQtxgct4xecd-cb2JLxujxWi-8NSxVez0FZQbVvRyPnNDM7o2EvGJkFJ7hf7Q7_jAX6Lntw-8halT38eiB90M74JRod0aOjlwqj4Uqd4Hyqlj0uriLVitIFV1eUMAdMUheVRxX4lv-5On86TvOTPsl1VDzAqw22eIuAIdJ4OthFMAoBkcjZA9q9stsNPwa6wFGKPU2IYBorV8Dxoj2vKoUMPYggARgysEryt0DGxIzgv4vABkpcY4vhvTsRRbn35aM7Fjfc0OyNHZKxT06nC77bKh0LIUyuIyRWeg7SrWpQnvemS2S4Y-z60yHNsW20EyTlPj-OIEj6rRLef6Q6p5eGR4VjbCHeqMf2D73TgTppWQeLgHkCTeY6bXIuVePdmg-SznpA0Rd34_4TW5yx7fGBkJeUvUMuMTaTMNIGFRHoOXtrbL2RYhMAGn24aFBxtcdbojchaRZgicMHTNGOIv96vh0DxqEBbDXCs17iDxMxIrWu2wVJqEDAHGoryx_V-V3EziIEuICP3lk1P1iEEZtOhMA9Ci6d_BrXNx_CgUtafjv2RwNiIE1Fq-U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bef907830.mp4?token=HSBMcJ67JEgN5bRfQeTrRKohLpt0pc6GuLrQrQaT2SoGln9hmvqhRX3YYure0iTUQ2GnGPhhItz6ES4vuo9-nn3U7WYBg-tCoEiibljPZ3QDsMmUaLQtxgct4xecd-cb2JLxujxWi-8NSxVez0FZQbVvRyPnNDM7o2EvGJkFJ7hf7Q7_jAX6Lntw-8halT38eiB90M74JRod0aOjlwqj4Uqd4Hyqlj0uriLVitIFV1eUMAdMUheVRxX4lv-5On86TvOTPsl1VDzAqw22eIuAIdJ4OthFMAoBkcjZA9q9stsNPwa6wFGKPU2IYBorV8Dxoj2vKoUMPYggARgysEryt0DGxIzgv4vABkpcY4vhvTsRRbn35aM7Fjfc0OyNHZKxT06nC77bKh0LIUyuIyRWeg7SrWpQnvemS2S4Y-z60yHNsW20EyTlPj-OIEj6rRLef6Q6p5eGR4VjbCHeqMf2D73TgTppWQeLgHkCTeY6bXIuVePdmg-SznpA0Rd34_4TW5yx7fGBkJeUvUMuMTaTMNIGFRHoOXtrbL2RYhMAGn24aFBxtcdbojchaRZgicMHTNGOIv96vh0DxqEBbDXCs17iDxMxIrWu2wVJqEDAHGoryx_V-V3EziIEuICP3lk1P1iEEZtOhMA9Ci6d_BrXNx_CgUtafjv2RwNiIE1Fq-U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📌
زائرشهرهای بوستان ولایت برای میزبانی از میهمانان آذربایجان شرقی آماده شد/ بازدید دو عضو شورای شهر از روند آماده‌سازی
✅
اعضای شورای شهر تهران، از روند آماده‌سازی زائرشهرهای بوستان ولایت توسط معاونت مالی و اقتصاد شهری شهرداری، بازدید کردند.
آقامیری رئیس کمیته عمران شورای شهر:
🔺
۱۰۰۰ نفر از نیروهای شهرداری تهران و داوطلب، به میهمانانی که در بوستان‌ ولایت مستقر می‌شوند، خدمات می‌دهند.
پیرهادی رئیس کمیسیون سلامت، محیط زیست و خدمات شهری شورای شهر:
🔺
اقدامات بسیار خوبی توسط سازمان بازنشستگی شهرداری تهران و شهرداری منطقه ۱۹ برای میزبانی از هم‌وطنان آذری زبان انجام شده است.
🔺
در کنار امکانات اقامتی و بهداشتی، وضعیت ایمنی و رفاهیات نیز برای میهمانان اندیشیده و اجرایی شده است.</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/446368" target="_blank">📅 19:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446367">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggERNEGGroBzaGW4mOpJGh3alm6woFfh7gc2giVQWcNvBu78PgUT8TneCMQ5o5sT5XjheGGkGbl1ITHVMAP9flFc4SiwjjsUx8vSy73wH1rPcjjAZnB1ZqKOELmI-UE2VH8c-TK_zRumQTqwyhFZSBAc_X0euXmeUSNFk9PqIT4Y1EwW7EK4tUMS_RhkCnp92UKaefgYsqBkYxFCPDayweUZR8GVBYUpNX9Dd9TU9vnmpCS7RVlpwR1I2dLNOtGQqI7GJGwIPE2mQTG31txJy1p6NBHPBMfThNSB4SUI1048WUAY6dVZvWLrIgznzGZ6xzrBk8soNE0A8ZvEiO5zOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
آمادگی کامل بانک رفاه کارگران برای خدمات‌رسانی به شرکت‌کنندگان مراسم وداع و تشییع رهبر شهید
🔹
بانک رفاه کارگران با بسیج همه امکانات برای خدمات‌رسانی به شرکت‌کنندگان در مراسم وداع و تشییع رهبر شهید انقلاب اسلامی در آمادگی کامل به‌سر می‌برد.
🔹
با هدف تکریم سوگواران و تسهیل در ارائه خدمات، این بانک در استان‌های تهران، قم و خراسان رضوی، اقدام به برپایی موکب خواهد کرد.
🔹
همزمان با مراسم تشییع پیکر رهبر شهید در روز دوشنبه ۱۵ تیرماه در تهران بزرگ، موکب‌های بانک رفاه کارگران در نقاط مختلف این شهر ازجمله پشت ساختمان وزارت تعاون، کار و رفاه اجتماعی (خیابان اردبیل)، ساختمان ستادی بلوار کشاورز، ساختمان اداره آموزش و توسعه دانش (دروازه دولت)، مدیریت شعب منطقه سه تهران(صادقیه)، مدیریت شعب منطقه دو تهران (روبه‌روی مهدیه تهران)، شرکت داده‌پردازی (استاد نجات‌الهی) و برخی از شعب بانک رفاه کارگران، برپا و مشارکت و حضور اثربخشی در برگزاری این مراسم خواهد داشت.
🔹
همچنین همزمان با تشییع پیکر قائد شهید در شهرهای قم و مشهد مقدس به ترتیب در روزهای سه‌شنبه ۱۶ و پنج‌شنبه ۱۸ تیرماه، موکب‌های بانک رفاه کارگران در نقاط مختلف این شهرها برپا خواهد شد و به شرکت‌کنندگان در این مراسم خدمات‌رسانی می‌کنند.
🔹
جمعی از مدیران و کارشناسان بانک رفاه کارگران با حضور در ایستگاه صلواتی بانک در این مراسم‌، پاسخ‌گوی سوالات حاضران خواهند بود.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/446367" target="_blank">📅 18:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446366">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/446366" target="_blank">📅 18:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446365">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ceae37eac.mp4?token=E6N2an31XTrUtr0U_Wf69TOqstW38U0oPWHEXnLOqvLjf-KF0yHMmSCMBCaElWH5q1axa5yPjrE1ajkSvGxb0HPmhy9CWUqb0wr_USS_ugQB8KvrQwzgi_738eMGCZSMDEupqdG0J5lsib8Bqa3R1SqxYkRseSNGhkg9vT-v-e72bpx1z45ZdtHQNoOZ-mE0dxfPC6xPTFqPv2UYAvkBXoQ-pRdlSzqzXLrJpxGELf71QS2IFZUulUyxSaY2Au1T6YNnS4gQ-HpG_PE-2wmjg7CJBcAbPtUbAnm_T296pBjzyfvkYpl_MrZqrOumCBek3MbdqKo4rRvCQDzqKNd8Xoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ceae37eac.mp4?token=E6N2an31XTrUtr0U_Wf69TOqstW38U0oPWHEXnLOqvLjf-KF0yHMmSCMBCaElWH5q1axa5yPjrE1ajkSvGxb0HPmhy9CWUqb0wr_USS_ugQB8KvrQwzgi_738eMGCZSMDEupqdG0J5lsib8Bqa3R1SqxYkRseSNGhkg9vT-v-e72bpx1z45ZdtHQNoOZ-mE0dxfPC6xPTFqPv2UYAvkBXoQ-pRdlSzqzXLrJpxGELf71QS2IFZUulUyxSaY2Au1T6YNnS4gQ-HpG_PE-2wmjg7CJBcAbPtUbAnm_T296pBjzyfvkYpl_MrZqrOumCBek3MbdqKo4rRvCQDzqKNd8Xoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درد دل‌های دخترانه با پدر شهید امت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/446365" target="_blank">📅 18:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446364">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cee7d6c7e.mp4?token=jisvjd71luBvlltcYuK8KdbupneU83284t-HHeVkp040VzthUqmbMiKXoyaS4em8hO6nDMEi5Xx6uDMHKUzKz63Qe-2rGezvya5lbi8jyc8CGvnJZ0kc-E6_BgfBQVnFEH48te3XrCcW7tcD13Eo3D5ePJkH5Vgini3E_QE7hX95EcaHG3kpbaOK-3KZCCT0SQvP-wD0dI4o_o2yQCmDE02Dlp7QtoctSzAPD-44ZbZpko68JBKFrswHd0LImn5H0veU-JzzlN_mcL54KBcRcLLTNY1Q5tkr_TE9TG_w1oV-FuHx8pSmhyGJCmGqxXbJItzDR9xDeS1lyoxRx1ydxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cee7d6c7e.mp4?token=jisvjd71luBvlltcYuK8KdbupneU83284t-HHeVkp040VzthUqmbMiKXoyaS4em8hO6nDMEi5Xx6uDMHKUzKz63Qe-2rGezvya5lbi8jyc8CGvnJZ0kc-E6_BgfBQVnFEH48te3XrCcW7tcD13Eo3D5ePJkH5Vgini3E_QE7hX95EcaHG3kpbaOK-3KZCCT0SQvP-wD0dI4o_o2yQCmDE02Dlp7QtoctSzAPD-44ZbZpko68JBKFrswHd0LImn5H0veU-JzzlN_mcL54KBcRcLLTNY1Q5tkr_TE9TG_w1oV-FuHx8pSmhyGJCmGqxXbJItzDR9xDeS1lyoxRx1ydxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی از پیکرهای مطهر رهبر شهید انقلاب به همراه شهدای خانواده ایشان در مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/446364" target="_blank">📅 18:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446362">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: از اقدام جمهوری اسلامی ایران برای شکستن محاصرۀ عربستان، انتقال بیماران، افراد گرفتار و نیز هیئت‌های رسمی و مردمی شرکت‌کننده در مراسم تشییع پیکر «شهید سید علی خامنه‌ای» قدردانی می‌کنیم. @Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/446362" target="_blank">📅 18:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446361">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: محاصره و محدودیت‌های اعمال‌شده بر فرودگاه بین‌المللی صنعا باید پایان یابد. @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446361" target="_blank">📅 18:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446360">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: تمامی یگان‌های نیروهای مسلح آمادگی کامل دارند تا هر تصمیمی را که رهبر جنبش انصارالله بگیرد، اجرا کنند و برای شکستن محاصرۀ عربستان و بیرون راندن اشغالگران آماده هستند. @Farsna</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/446360" target="_blank">📅 18:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446359">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: ادامۀ محاصرۀ «سعودی-آمریکایی» علیه یمن را برای مدت نامحدود نخواهیم پذیرفت و برای پایان دادن به این محاصره، از تمامی اقدامات مشروع استفاده خواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446359" target="_blank">📅 18:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446358">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: اگر عربستان یک‌بار دیگر حریم هوایی یمن را نقض کند پاسخ همه‌جانبه می‌دهیم
🔹
صبح امروز (جمعه) ساعت ۵:۲۰، چند فروند جنگندۀ ائتلاف سعودی با نقض حریم هوایی یمن تلاش کردند مانع فرود یک فروند هواپیمای غیرنظامی ایرانی در فرودگاه بین‌المللی…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/446358" target="_blank">📅 18:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446357">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: اگر عربستان یک‌بار دیگر حریم هوایی یمن را نقض کند پاسخ همه‌جانبه می‌دهیم
🔹
صبح امروز (جمعه) ساعت ۵:۲۰، چند فروند جنگندۀ ائتلاف سعودی با نقض حریم هوایی یمن تلاش کردند مانع فرود یک فروند هواپیمای غیرنظامی ایرانی در فرودگاه بین‌المللی صنعا شوند؛ هواپیمایی که بیش از ۲۰۰ شهروند گرفتار، مجروح و بیمار یمنی را جابه‌جا می‌کرد.
🔹
این تلاش با رهگیری جنگنده‌های سعودی توسط پدافند هوایی یمن ناکام ماند و پس از شلیک چند موشک پدافندی، جنگنده‌ها مجبور به ترک حریم هوایی یمن شدند.
🔹
به عربستان هشدار می‌دهیم از تکرار هرگونه نقض حریم هوایی یا تجاوز علیه یمن خودداری کند؛ در غیر این صورت، پاسخ همه‌جانبه‌ای دریافت خواهد کرد که فرودگاه‌ها و مراکز حیاتی آن در خشکی و دریا را هدف قرار خواهد داد.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/446357" target="_blank">📅 18:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446356">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eda90d158.mp4?token=VCm0Gy6VXDTT0JV1L2kphUSrWyfcfCPxVrgPVo1f9YzfkHHEtHiVAqxjwbGM88u_fL7PW4oH5ZWItonOD-9Bl8IVZgr299ms8XkJ1_Oa4TosN3HOaI88QM72XuLnrZV8-TECQ6QsqTAWWyvmiW2YzKTBsO9T-g8Nbl9CZjLR8Utir8kuNAJD0V9EhSlL_V3knenVtoo_wPwlWwLtnowk75QPRnXggf4XycuX0ZSRJ1zvkRsbDbAln-DviSS77wEi2Jvw0mj4MRsdsjPj2VAPhmCJXKpTgp2adsrW7R4rEzok46VFZe4MHuTIFQZRBK5xz5vspdIlG7af9kdu6wjdtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eda90d158.mp4?token=VCm0Gy6VXDTT0JV1L2kphUSrWyfcfCPxVrgPVo1f9YzfkHHEtHiVAqxjwbGM88u_fL7PW4oH5ZWItonOD-9Bl8IVZgr299ms8XkJ1_Oa4TosN3HOaI88QM72XuLnrZV8-TECQ6QsqTAWWyvmiW2YzKTBsO9T-g8Nbl9CZjLR8Utir8kuNAJD0V9EhSlL_V3knenVtoo_wPwlWwLtnowk75QPRnXggf4XycuX0ZSRJ1zvkRsbDbAln-DviSS77wEi2Jvw0mj4MRsdsjPj2VAPhmCJXKpTgp2adsrW7R4rEzok46VFZe4MHuTIFQZRBK5xz5vspdIlG7af9kdu6wjdtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی از تابوت شهید زهرا محمدی، نوه رهبر شهید انقلاب در مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/446356" target="_blank">📅 18:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446355">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/212b46c594.mp4?token=mZr3NxxqKpp1XQj4klnsctaalAYdWfrJzbxwlRCnzFXMVtH-u3bcWRLctxDoJB7eidMu7fJko5LW4osBRMeqf8qbdrMKpSdD9HrpOhrUUJn7B-w4nYy7SYbbTDCe0rr0N8lVmvueXfbdZBt5a_1Yu1d7lXr2JHUo2TiKj0hftKhSiXg1Gl9hdtxclKEuw8PukLh-sjJku8eJJEDqP8qIqoPdtKRdPZW2bLvkncdFG5QT4iIiMMIaEuKVXvGikm492yU2etwUGVydFN1Go6GDm_rhTEax5Yy6rKZe7exgoUzW4An_BdpW_88P1jOfwCkUzWcwGde5Jmj-cmQ85QK4Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/212b46c594.mp4?token=mZr3NxxqKpp1XQj4klnsctaalAYdWfrJzbxwlRCnzFXMVtH-u3bcWRLctxDoJB7eidMu7fJko5LW4osBRMeqf8qbdrMKpSdD9HrpOhrUUJn7B-w4nYy7SYbbTDCe0rr0N8lVmvueXfbdZBt5a_1Yu1d7lXr2JHUo2TiKj0hftKhSiXg1Gl9hdtxclKEuw8PukLh-sjJku8eJJEDqP8qIqoPdtKRdPZW2bLvkncdFG5QT4iIiMMIaEuKVXvGikm492yU2etwUGVydFN1Go6GDm_rhTEax5Yy6rKZe7exgoUzW4An_BdpW_88P1jOfwCkUzWcwGde5Jmj-cmQ85QK4Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این روزها چه محدودیت‌هایی برای تردد خودروها در تهران وجود دارد؟
@Farsna</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/446355" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446354">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">📹
#فیلم | آغاز مراسم تشییع پیکر داماد رهبر شهید انقلاب، شهید مصباح‌الهدی باقری‌  #باید_برخاست   @rahbari_plus</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/446354" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446353">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6dab0c195.mp4?token=Ty9nH4eUPRyGYe1nRGCZdH3ZcZWzTxTgg7kT6aSiCll5CRAyyJ0nbiljnVHCvOYz8eRQmlH1Hl5POCNKbGWzwm7NGyTmrxXqDqQLQp65pWL6_u1sOt1YH1pMQGX1uNqXXkFdasY3iRHmt7lVu_VzBpudiozYgMOxJMtOI5x7XQVom3cwMKKK8kMmGstvd-B4_1XOvQ_xSms76MawMkRYODbTt0MXrf9W_8zomS_okfyEVjhVyYQplj6PsdUZxlt0liyG64ciLQbXVgxYv1ydR7P2NebbWi7ktGLWDeqBvhhjWUJUq-uMnsjEENGn3J4yB_uDT_Hhbn-zE4_zUSdFCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6dab0c195.mp4?token=Ty9nH4eUPRyGYe1nRGCZdH3ZcZWzTxTgg7kT6aSiCll5CRAyyJ0nbiljnVHCvOYz8eRQmlH1Hl5POCNKbGWzwm7NGyTmrxXqDqQLQp65pWL6_u1sOt1YH1pMQGX1uNqXXkFdasY3iRHmt7lVu_VzBpudiozYgMOxJMtOI5x7XQVom3cwMKKK8kMmGstvd-B4_1XOvQ_xSms76MawMkRYODbTt0MXrf9W_8zomS_okfyEVjhVyYQplj6PsdUZxlt0liyG64ciLQbXVgxYv1ydR7P2NebbWi7ktGLWDeqBvhhjWUJUq-uMnsjEENGn3J4yB_uDT_Hhbn-zE4_zUSdFCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام دبیرکل سازمان همکاری اقتصادی اکو به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/446353" target="_blank">📅 18:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446343">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oqxMQZbu5FbfIAJlGg9yM1y4KOMrkFy5aDhVQyLuUo-0x6s0aMl_0-GQ5okoWVbxvL61Ci9Wct1KojUsuV4ttGk8jJcqrf0j7SgWswa0oDOYlQskOOZRhapDar2dl7Mt3dFGJcYcTFDA6II5vopdVb2p-DeYlfSVuDxZRC0MRsQ-Ur4cCRuQU0fZl_emNM01ZUQ77I5TgBAtUcuoCCLYs1hwM14xWkuD1AeHy6xAiXUjnY4Ao5zcJG1A-yPIQG20UU3PEGfBT2rSCYKtrC6oB9aNDXtV267uvQ1-mLRyfgg0KbLPbKPRnbr_NpT379KPLUOhTrcE4nEo4dCq2Wt01Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q5l2E6jViu6vm69W3d9E45R3LwNTo3OceEXfIeULLsAriuSJYa2uK3kSRNxLmsavklXmv0vfplG5MlVxER8BwIgvpC90irutG5WdIr6Z8LzNsgG5BxEqPryoaXEpVwFhDzr7jlzX0nFHGHx70pPSGTIIR0aJmIRJbFliqX9KKQJxCyVWTecryZJmfjNReHtuzp-9_XeJqwa3v2zmKT953TpXi-BpivA4nwM6Ry1U2iFCuMZSTDi0coa49G_t1aB9uCyUM-z5Wl-qvNin3WD8ihe8JwgyfczWkbUtNjUzoZdLpu9K05UhwwOnS8LC8ZVfjSPqtPwNgtE3ayoIFfa1RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3MOiPHNz2GIHs5wfDMSnkhwUYZqKOB9zaUC8QUr9KqgqIk91DyHab2oG68MhUZ0Vtuv7DOL-HO9t9TRULXXjYc2aH36WxpgCaNZW2IdxqSX_rdfUGbbTW_0kPivytlavyVjngzVOk_8spkqwz3I0yqMYMgOv8zYLgUV0y_yX8nCvbpwx64bUjImGj9-9XtZiIGteS2ncYH85T0SuYmUyymj6dOCx6m8QTNIvcwOdneDaWgjqSk8gPEqdpMcrs0AhY5NAfIwopHyY82MOFAyuerDifs-ZhfCZHMaNqPr8tKlCd_7kBMFEFe030-uTNiZaWb-US0QhguNyATFOjlBUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IPpk3_tN1HiOM95Vd8Rwv0aCsH4yEF1Y66auKpCmCSh9BCWe8FOAtkdtnDHLeOHuhOrd4A0kSO5BmtKuMw5eeylkdK6ayHO5rnAmiPkuYghwDKwvFmi0YY9jMsNKw_H2YliP3CkfoyyjWoWR4DAlnhJdie3RgMJ0IOYLqCCv0AtFgQClMeE7DUEaZ2W9PA6NKMhLh81cXfDLz2K-HhwwnVeNo-H96WX9MhidJFFpjBrUIOiLU3C-lKxC5dCAVlRumfpSm5NkTU6dN4P_8BBZ-78nUfKXoIopy7jqqFU0QyYCFHbYmq4mER2i2I913stJksGnskbH-ZfHQXBptZ7xmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuwCVrHtE0LZnP3JWY94clsxE3ztP58RZqOC2q5jlmjYRET4EMvLF5uw_ANRL1Y2l3b0thz1CnahKtxVgZ3h0THy69W3uAzCAV58omHnT75gcO_Po8PT0D6JREElpY2HkRTi-OXEZRN8gOoKCIGy54F2OAS7LhrVxg9WjntejlBmTDxZ3vdyo7eHv6LplLagtMFfBCv-tTkH-_OadzTejRHkRxPh_IcR5Oh8v5ULOLqrEhe82PCMPAJNoQ0-XqVfKzP88rpAzY01ShbUMbsiO-aWg0yPUUOb69WTcaSRfoPxgtlgg5rX76saU2DRHrZ1vKKDPkJc4Evujmz_a6fGEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XsCLxJX1ZuV3-UmHzt4TZDJj4kDxJGAp6Z6r2yj9umTes92qKfVyA0lGknau_XO5Zhlyd8N7XeBFcoCLHrYtQ8c-IOOregePcnEu-x_U3TkoiKbZVC7CbfTIGoKce-Bks2qA5L3MmYHovHLYXnOF3aUaQhr8z7RuSovY5T-8m6JT6ATAlf93NbzSBolwPDvC2TFQgUrqG_rpbpxJRhHRet0WHWIWO9PrvySKedyizD9jewHxa5FqL5ZNLhpPsLEzbePVz-fYdtG3UJ6Op3Ujamatq6AU9WRKN3Ewvp-yh4IFYBQFFk_czkW1UL3cpUXFCvSAIBmVXzohOxbTKlCDPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TnZ2C7WzTxrbltW6WPKowmls-5hv7_9ircjVhCJ3ca6_VoVUTZoIkxkjAehFyNXIMsgTmpFX4c2o-GRdm17HDS12SRXDh88t77_OLiINPQzaiB0XQVz7IZcfPSsJSdy-Y9KH_eaCg0SXBZV4cZ72YH61K_pfvpwHe1X8kaqfs79ahoxi7aJJMRI906869PqnmhdzTXBZhz3xZDZ1qXqncZPubxix0l_hXI38w0uIzS4k5mKVvQSA8MdmGqn_PkYSDHDF7NMwcE-0DTQHG-LVTTNllJHYxW3OKj_suCh8n-yVA8xsrcU0GKwJA4Tqf66Z1WnIRzbxPu58wBIEDTK-RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VPAu7Y4A5eFYZPLQZVTg-j1ut75ieRPGftgf5Y19hvl2WA0eOpQ76FyIYtnBdeLPBlzVmR2lnZ9npZQ-u4sR3oozIwYblqD3NMIu8ursp8ku28msI8paRnvZ7DcBc4rmhjOhzpX4IXWvBXEH2Se_hJSa3AXWQOieiXUkkRpEInohlW4MsguWG3tJ-XSEfuYjnrGQZF7_F6TqLFsQgElzN9hWAPNnrxsC8IX_Oh2rp0Mh3wxRrM4v4-kWogK0mG5ihKiL2hCXRPWlMpHrrmHJDEXCTAXqTG55yJeGHkXdnCJwTVHVEf4d8UogC9L1TVrEHW7JK6aRF8ZTcfmg-J4T2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WglvQQUVea02AyluHnU7zzNavlR0otfLDThfgM9xQCM7knGngwzk-2TGf2me6TXojX8bcf8JBBTWBXcJxyFaX-CrecQ5175aH5JA6VMNnFZRUsw-mOz9c7-0US6v6WI62YnGFNhPegKHvp-H9TAWJXYkbBCQLqe8y_uneM7X9Nz9PQUQ8t92ddJG0K26KR_6VCb6e21M_GGPMgBiFC3HjYP39KnSDyZ_2cL9MxgQIoOxmN3_1cPtc4cZKzFV_ZSu4VaAfT3gSezPQ-CvHd-6xdYEG8bmrfIV7N_G1lpQ9Sm8S9v1s5DwKz1f-WPodg2w_Aa44IlHIYYXJKL3-6k8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N-TLCROR29YJB2ZNs5BTyj0Wh4jNADJnCbcP03_qjQDUwVxZNtTGPjj3WnurqQl7T_aj3F8RFd_R3CzMfh960OQiEzW0sYySqys0hI-WtS1s_YSHR4wFBYi2IdOASEzrtX7fdpCaQFW9BZXdRl6QW5oDtBVfJwiE9OhKFwXClhAcUEVDEUsSz9zvKgIztiToP5EhPpv4jC-pNhV49hUBjnktSR28V_Z_jv5ZhLFzoNX5l3PlOhcxnk8IY54p8Ntw6g15Qfv27473Qw-gSzBo_jk2_4d4IDtc2BdrvtPE2LXtK75dYNXTlc8gZFbyC7BrpFC7_QAlRO6QID-tbOPFnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور سران قوا و مسئولان نظام در مصلای امام خمینی تهران برای استقبال از مهمانان خارجی
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446343" target="_blank">📅 18:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446342">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc5765e1db.mp4?token=Mf3_lfMEz6iYp1rNIAg-cSulZNQPkY1cPc0HOOfeK53sft6P72n6Nut-o9JO7oVLqXN_S8wiQUJp-xqSrewP4Q0t2UsQy24XNAPwPJIlYgcZgvC40qzc1yWKigNwjLHnZKdiBQrCf6rDPz1saohm4rewDtQ4x6f7udw8GJ9iK2Dd3m702xsNHSun83wsab9CsuT6s9gs7eagseSAus4AzeoshP22mqqYCSY_ii2w3_mX3--4decAbnQ9iAbu7-mIVNvaHE7_SBfwkPIkHyesPuUB-0Vj9CMjsLiZcyE6tuPCff-3XSKlawo9Ax-Y5JC-SJVbQnnVVSOIQ6ziqTjA1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc5765e1db.mp4?token=Mf3_lfMEz6iYp1rNIAg-cSulZNQPkY1cPc0HOOfeK53sft6P72n6Nut-o9JO7oVLqXN_S8wiQUJp-xqSrewP4Q0t2UsQy24XNAPwPJIlYgcZgvC40qzc1yWKigNwjLHnZKdiBQrCf6rDPz1saohm4rewDtQ4x6f7udw8GJ9iK2Dd3m702xsNHSun83wsab9CsuT6s9gs7eagseSAus4AzeoshP22mqqYCSY_ii2w3_mX3--4decAbnQ9iAbu7-mIVNvaHE7_SBfwkPIkHyesPuUB-0Vj9CMjsLiZcyE6tuPCff-3XSKlawo9Ax-Y5JC-SJVbQnnVVSOIQ6ziqTjA1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام نمایندۀ ویژۀ دولت تانزانیا به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/446342" target="_blank">📅 18:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446341">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48a3b17bba.mp4?token=mGJPRn-iU3y5niVnUXQBIAr_RDH-xM93xkuPLXTEtjTDdElelmv5aUIFErXffyYRncmBxqARc0SscJocCsZUpO4uYCBmRhw-SgVE-gx5QGi8BqX06a-Dt_FAT1wmhmSf1mOKQFqYXXaRDGY7HeGzKkbxeFlrGIVwfj2YbPgwTB2n3Ch95_zPDcVs6WzKMqzv-6bYeREsk2RN2IH2cpKJnZ0JZdE0H2CareqyGmnGdGNjIT-4ZZNcFqH7rkdHo34dXtTUg7UACfJ0YKoFeWaIPxX60NiDAzpoiIi8V65HqkxdNcc_n_QVr68Wyr-6s7SPTA-KJ7SGpazeHPV-N1ZXaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48a3b17bba.mp4?token=mGJPRn-iU3y5niVnUXQBIAr_RDH-xM93xkuPLXTEtjTDdElelmv5aUIFErXffyYRncmBxqARc0SscJocCsZUpO4uYCBmRhw-SgVE-gx5QGi8BqX06a-Dt_FAT1wmhmSf1mOKQFqYXXaRDGY7HeGzKkbxeFlrGIVwfj2YbPgwTB2n3Ch95_zPDcVs6WzKMqzv-6bYeREsk2RN2IH2cpKJnZ0JZdE0H2CareqyGmnGdGNjIT-4ZZNcFqH7rkdHo34dXtTUg7UACfJ0YKoFeWaIPxX60NiDAzpoiIi8V65HqkxdNcc_n_QVr68Wyr-6s7SPTA-KJ7SGpazeHPV-N1ZXaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با این روش از آخرین وضعیت ترافیکی تهران مطلع شوید
@Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/446341" target="_blank">📅 18:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446340">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8671d75c.mp4?token=P29NYZBcgWLKDTQR_0KmO2A_quafcw3D6JUxCQaTIHq_Y5TYxDGewawwqweXARFCXJRZrlH4Zlh7IIbuUsuSaEnsLD2K_J-p7yNSl1WFBt_JXVHbQ01zrq93-KSW50qbA0PiNYNX4Uu-lG5dVhugbAwPTkg5xjxQQXAOssAvPzJN2FaycwTetfzN7hUQgz9t-JJPCZrpcHgUnyAhnOHKaxq3Z4Ry-PM_wxuwH_KBf1TpLX8w6ebdWDVqYbnbsjZcidUC7N8_m8lsyov1U6yYsi0k2kA5grEuZXgK5sm9Eqgz9brEQ7hVDgGsiZ3qnoBBOZ1qh0taAyDZqCNMumJMYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8671d75c.mp4?token=P29NYZBcgWLKDTQR_0KmO2A_quafcw3D6JUxCQaTIHq_Y5TYxDGewawwqweXARFCXJRZrlH4Zlh7IIbuUsuSaEnsLD2K_J-p7yNSl1WFBt_JXVHbQ01zrq93-KSW50qbA0PiNYNX4Uu-lG5dVhugbAwPTkg5xjxQQXAOssAvPzJN2FaycwTetfzN7hUQgz9t-JJPCZrpcHgUnyAhnOHKaxq3Z4Ry-PM_wxuwH_KBf1TpLX8w6ebdWDVqYbnbsjZcidUC7N8_m8lsyov1U6yYsi0k2kA5grEuZXgK5sm9Eqgz9brEQ7hVDgGsiZ3qnoBBOZ1qh0taAyDZqCNMumJMYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوشته‌های مهمانان مراسم ادای احترام به رهبر شهید انقلاب
در دفتر یادبود
@Farsna</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/446340" target="_blank">📅 18:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446339">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c077414a9.mp4?token=MTZSw3y7uqPU9q2kAkdLmB9mjGBdyWMiCcrveMlOi8TaN26r6cf7mKocagBeB_rvWZdp5OrEjPKxc8RAWGQnAN8IRyYEuO1Am7GyW-ep0xgJjTHFXbR6_gZAxRxUoD_vi_xwFJVCMlnjDfT7IsFkl_L3sKLVHUxMeyUFmbWT6uO0FZ8Z5ZTYa31qfLCCnXumiW7apZ04iHuhsBcIEw2-Uu0Q4NG6MfUVIOohDKSDFXA7Y5qrJFDbVyoNCiZ7ZFnfsmfYit8ms2JLm8SSo2kWyixNfQhvbX7bCSiDdOTEXvMhqUxd8qDhnVE7ceSi6wcMfXKU75jLIUiA1PlNChhKCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c077414a9.mp4?token=MTZSw3y7uqPU9q2kAkdLmB9mjGBdyWMiCcrveMlOi8TaN26r6cf7mKocagBeB_rvWZdp5OrEjPKxc8RAWGQnAN8IRyYEuO1Am7GyW-ep0xgJjTHFXbR6_gZAxRxUoD_vi_xwFJVCMlnjDfT7IsFkl_L3sKLVHUxMeyUFmbWT6uO0FZ8Z5ZTYa31qfLCCnXumiW7apZ04iHuhsBcIEw2-Uu0Q4NG6MfUVIOohDKSDFXA7Y5qrJFDbVyoNCiZ7ZFnfsmfYit8ms2JLm8SSo2kWyixNfQhvbX7bCSiDdOTEXvMhqUxd8qDhnVE7ceSi6wcMfXKU75jLIUiA1PlNChhKCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اشک‌های قالیباف هنگام وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/446339" target="_blank">📅 18:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446338">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7bbd75691.mp4?token=b2XtSF9jWwB4gPUxFSTGMrTtXIOrwac1VHo6f2hqmD1DrmuMHQMkDtXPxj0iOyhB48VFDuzXIMjExKJSFoX68OscwzLLafi3l_C4DYWt2VbHllGbeUt3Q0AYf8AlCtGVHq_ik6hR3xaOLomIdrLQTfCwvyysdGmRT_0_tllDGkPS9uiN85qlOkhhAqJRFcIKrFYkvmK-smQkv760PSfoe2gwDOamWsCcgTWLdaOMvS4R9vO553ZrdFEiChXoTpfPtRIRVafcabDGW36x2vrpZmkhdSWrqU2MvkcE201Vwo1Cxn_4imjAWjlt67lS_MIkj4YnhTr2D11vX1b2BwZodw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7bbd75691.mp4?token=b2XtSF9jWwB4gPUxFSTGMrTtXIOrwac1VHo6f2hqmD1DrmuMHQMkDtXPxj0iOyhB48VFDuzXIMjExKJSFoX68OscwzLLafi3l_C4DYWt2VbHllGbeUt3Q0AYf8AlCtGVHq_ik6hR3xaOLomIdrLQTfCwvyysdGmRT_0_tllDGkPS9uiN85qlOkhhAqJRFcIKrFYkvmK-smQkv760PSfoe2gwDOamWsCcgTWLdaOMvS4R9vO553ZrdFEiChXoTpfPtRIRVafcabDGW36x2vrpZmkhdSWrqU2MvkcE201Vwo1Cxn_4imjAWjlt67lS_MIkj4YnhTr2D11vX1b2BwZodw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام نمایندۀ ویژۀ دولت هند به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446338" target="_blank">📅 17:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446337">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kA1-eTVf7KbZiXnbXbEktveHEwtl1zrqX5kflNhVpVQL69GcbbI82ByK9qowkrCyI8bkpmI_4EqoXZeKkWmr64ziyUOwu8B3Sqwk8N7D4rj1QDWsjILe3L4_D71Ir_wnEkoJnHqdGTPTw6Ygn3bQrUvIYCYEhxvtUkzJNzn90YYJvr8GxU3k87Kk9TznlASQfiB-QKgZmCIdZPR3XyngPLhTCXscoLoW3oK4kFGJhNbFzbz0eRPOSetqvC4d45GILUlsCBmXzYBogPOiKCiZoJgg0nRXz4FBN8EgrPEERiYSYZ7KjbSIOAOlYN0KZyjKEqY9wwsdgPTNmz69GBCZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر شهید شدم به آقا می‌گم برایت موکب زدیم
🔹
از همان وقتی که خبر تشییع چند میلیونی آقا، دست‌به‌دست شد، تندی به دلش افتاد که خانه‌شان را زائرسرای مشتاقان کنند و حالا بی‌صبرانه منتظرند تا چراغ خانه شان روشن‌شود.
🔹
مابین شلوغی آماده‌سازی خانه برای میزبانی از زائران، محمدجواد ۶ ساله با حرفی همه را میخکوب می‌کند: من مدرسه‌ای رفتم که ممکنه دشمن موشک بزند؛ اگه شهید شدم و رفتم پیش رهبر، حتما می‌گم خونه‌مون رو تمیز کردیم تا از مهمون‌های تو پذیرایی کنیم.
🔗
حرف‌های شنیدنی محمدجواد و روایت میزبانی خانواده‌اش را از
اینجا
بخوانید.
@farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446337" target="_blank">📅 17:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446336">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb7b7d98a.mp4?token=sgJAZeUthsHQnS1M45hTlckE3sTNTqegmxx6vADanktHAbAzrlFZGKJC9hXuJfCQBk2KvfjDTFrHJU2NJOHVFtOGUKw8243dCDdROQLLNQAt5h5IWZmDpmKAZKxYAw-k6n6hII3VXNKqcnqrEBjQePTTF8nZUl7pXpquErsax2TI8vbevIhCpFcuUnJcnqPUFEwn68CJ1wdWpVVtcpEEL3Mk_Ez6z6SWC5QGR5kY5Mt60Wt-oTxdskTQetNpl64ecaRXxBMmMjq3D7Y9hyxq1PRy2IswEsHO1IkxSzeQ68RAxOmm8uU6I6Sxs-vUdh6vofjgRsD__cI4uB34SKp8NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb7b7d98a.mp4?token=sgJAZeUthsHQnS1M45hTlckE3sTNTqegmxx6vADanktHAbAzrlFZGKJC9hXuJfCQBk2KvfjDTFrHJU2NJOHVFtOGUKw8243dCDdROQLLNQAt5h5IWZmDpmKAZKxYAw-k6n6hII3VXNKqcnqrEBjQePTTF8nZUl7pXpquErsax2TI8vbevIhCpFcuUnJcnqPUFEwn68CJ1wdWpVVtcpEEL3Mk_Ez6z6SWC5QGR5kY5Mt60Wt-oTxdskTQetNpl64ecaRXxBMmMjq3D7Y9hyxq1PRy2IswEsHO1IkxSzeQ68RAxOmm8uU6I6Sxs-vUdh6vofjgRsD__cI4uB34SKp8NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام نمایندۀ دولت تونس به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/446336" target="_blank">📅 17:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446331">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MNAUtgMgpAS8J5KedvGVE-bOrbTfqgiU3j2YoPmdHANm9xN79c7doWfGWBdvoVA9Grd6YnUuJrcuhoCZ1zAwMQ6qBMJWkYPg8kRcUdEL98Yus4bdauMLRudbN9RiGiKtdNpc2UaN2x8mOkqlv2hIONNUdHLaeEb_Y4blZqkKsAwhbCKS6yfwfXUm1cwicOBjbuH7uUe6WjK9U4iLglTPIpib6tgZ5mZp7RvbZafVBTrzxW1st4B4NLICVIeQpYqWy_DE3jBjgQ8_qlmCl1OASjQiPmihjVy4zcvr6M-aAkomo14xj-cgKM3CZmv-U0LGGEigwXCA_AwHRa8A7pne3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pC4w3A_qeNvNH7uECN8Y-1TOUDb2K_h2awWBPru5yw6FdEvKCkyY8zQoDkCn_xVCEKIF0yQJ-hrrv2fB9V3ClIy9kbNLAUUWjhpa4PtTQ8H-8UN1J0QeR58j-lBm5NMsfVTRYIsflW6ayutwAV8C4goJQdkIvZi1rLT3ydsbHoGPWdwtfms9cBNadlE-lAs4X00RvRssHTbHoN1Bzp3Sc-SVNBlBogaRZ5ClnSZ41HLOto8gt5iHQRLVFPipd3hVvmvicCKctRZrNOJ31s3RYX632sjGJ5im95NX7UAsBQXC_WI4S1iJAfs7WNS8uzcttMmktD0ytQWrDz7z5nLVcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GNAO2O84qUO948o95O6Mnh7Adjes5V_vLfG-9-u9WT8ZfX4w8x5EvxElKh8UbbSf3igFu_1puT-8bAXZUuj2vg7uONd5bYa0Rieo5NmpIGxf2PMmOcGvf77KoFFKj6enJ7pZQBQK489iAM7ELb2xyXvbVothmHqs3RHrgb8Q2bZNLQP64i6uOf6MKHABx7QyKvjQ-nq_9FVlyP11bnQ_WgvavurUIrXZm1rRzW_1CQ_BS2YxhujC5l6WsMX5TpNltaLZ0cczAErTUQxCiG_8CyS8dY_6OCshjFOAjDaMPhk2noQd_tPvLSoS3VDsb-6n8nvnTlfinRAuV0KMElcSfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UTv_BnbFZt1ATG3ESg1fvKUbw79itHYy3bP2sbLXSr2ELfSwP70doTBKeTTGDUtBu4xJ7ioigaDyk_Q_IPbz9KP2W8PiowvF4xN3PEdPoRDoYVzRRBIvOCDtT68jiwSi4hLI6ygtKmOnmMWrMUtkBP-kNCVc4D2edssrM8FaObxJqQmSX0EoSw5niVQDe5tNFu5o4nPsP_FSaTkBrzEOvshm6HdTrVEnM5CvHLc1zFGCDN0gfrjPU7QD7xqzKo99p8AGcROvsTtHhXMhhetuIViGUWmpBStrmfE2wwAAHOyRhCWfftH82kAeoY3SFoLX8-vPvlyJzHNHyn5zvmaIBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YRikUrhwOauQMoVYKcfeKPqi9pIm5BcNyts6N-FYxcw64_Et6ze2yZXAfmyExVvBU-qoijFtjGPWcJffMGxjjxy3_kCRUBiW8A1Lz4UlshOchEBfECQIFO7jguEkRQdry2qwaVvMoTVPS2o6axXpyKcn_W3vWkeoxWIIOFa0m6Aog_yfApIth-DGz8TfORerbPJmbJXv6anb1Iz5OdHk5Of2byuexhM-Q-n4BQdRTDxvnCfvLKhTIwlI2RRtD6d4lYzsbQTAHJPBS9qqTfxuAmV-zj7q-mR4PU21I0vU_b5bZBFMU6ckUR2mNhZe-keyvVufl3EXWX2xlAMZHc3F0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گلباران محل شهادت ۲۹۰ مسافر هواپیمای ایران توسط آمریکا در سال ۱۳۶۷
عکس:
رهبر امامدادی
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/446331" target="_blank">📅 17:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446330">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299dd37dc4.mp4?token=ol5DNicAVONYSM6dEAN5AMM8nCc6yqxYIz7VGR0sKZiJqYA4k4MtdXidLbn73vgdl_70MmbXHLOYMO5yOq3yYVlUzyNW-C_wHxGCp4Ja4EE0r01A86Ks1wa8Z0318hXFbeW_HmXLQvgv8z9p90XVJwKqXNxe11cs62eRYkhj4d04CkUzLhncM48xHRJRLSHVkgiZrXOREsRhGRPsKb4ZrJXhra43pXC5Zqs83NnW16o_gHidrq4wI-oIf9f_nIq2jscajuE8aoijvD301Z2fpuMF9aTR_WL22mXu-gNAR65ur03XeApVcyY7EKdbR4yJLagew21Nai85m5Ch9dBCsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299dd37dc4.mp4?token=ol5DNicAVONYSM6dEAN5AMM8nCc6yqxYIz7VGR0sKZiJqYA4k4MtdXidLbn73vgdl_70MmbXHLOYMO5yOq3yYVlUzyNW-C_wHxGCp4Ja4EE0r01A86Ks1wa8Z0318hXFbeW_HmXLQvgv8z9p90XVJwKqXNxe11cs62eRYkhj4d04CkUzLhncM48xHRJRLSHVkgiZrXOREsRhGRPsKb4ZrJXhra43pXC5Zqs83NnW16o_gHidrq4wI-oIf9f_nIq2jscajuE8aoijvD301Z2fpuMF9aTR_WL22mXu-gNAR65ur03XeApVcyY7EKdbR4yJLagew21Nai85m5Ch9dBCsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام نمایندۀ ویژۀ دولت مالزی به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/446330" target="_blank">📅 17:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446329">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سردار سید مجید موسوی: جانفدایان امت در نیروی هوافضا خوشه‌های خشم را بر سر دشمن آوار کرده و خواهند کرد
🔹
پیام فرماندۀ نیروی هوافضای سپاه پاسداران به مناسبت تشییع رهبر شهید انقلاب: اینک که با دلی خون و قلبی محزون، رهبر شهیدمان، آن یگانه دوران را به جایگاه والای ابدی خود بدرقه می‌کنیم، با خدای ایشان عهد میبندیم، تا تحقق اهداف عالیه‌ای که در طول زعامت شریفشان برای جامعه اسلامی ترسیم کردند، لحظه‌ای از پا نخواهیم نشست.
🔹
خط ما همان خواهد بود که رهبر معظم انقلاب حضرت آیت الله سید مجتبی خامنه‌ای اعلام کردند: هر عضوی از ملت که توسط دشمن شهید میشود، خود موضوع مستقلی برای پرونده انتقام است.
🔹
سیلی‌های سخت و غیرمنتظره‌ای که دشمن دریافت کرد، پایانی ندارد، چرا که مسیر مبارزه حق و باطل پایانی نداشته و نخواهد داشت. و به امت شریف ایران اعلام میکنم، جانفدایان شما در نیروی هوافضا به نیابت از شما خوشه‌های خشمتان را بر سر دشمن آوار کرده و خواهند کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/446329" target="_blank">📅 17:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446328">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTujITnQG_HL_EkSmE6IFoxsPXVu4oAHVp2qXRjhqq9HDSsA_mHPFMuTEDsV2F2Zz5Sh3zE2ZrWPeHZ5l-CsQYD8_eOfVvEN4j87BDf20G6vMRbXDeol7OCaToQ2w-U0RSOy_f5IGx_deUqKtlUk8J0jp1pBHOrF0c4RLh346Xw3qGKsNlx6eSuR71MkCpmtXLcEva133GrQKte-sKuZNMvl0zlTi0TNVemt6LhyfXw7FwfJQUefTLPY2Xtaf9ejr1u-b_4IwwFvbAQrpcdaKULvTwD6_cfWdnnTq7ddf4ow4ulUIa2QoB6OrNa7TXRC1QCFQJ5pzO54VRsjGafQVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
فهرست مجتمع‌های خدمات زائر در ورودی‌های شهر تهران برای زوار و شرکت کنندگان تشییع آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/446328" target="_blank">📅 17:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446327">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0ce8fafd3.mp4?token=rVAN8aXRoQz9bktmh_scnmrCWJVzqfF5EWeqs9kEvKXduijrtsTctFVtVbUAAaiJoO6WDNMkaK_ylA3uQmDYa3jcxI_vCaqc3Wwrp3X0Z0ugwh6NozprBPFZsfvk4ZEDm5ybdXi9paPhKiN9f7iIvA3uFh8wvYFWjxJDMw0EOfbYWqij0VmjOHMbrscFnSA9_Dw2fM-fAcgeJh7GZQXV8Cnau6_lE90JgZd5rRcssWdKzJMxS8fKRVrUs-mFjCtn0O7vbMwYwu5yOytMm3GSbkcK-tp33KlRjwj4CYYfdjl55YJ96E2Hu6fcn3qm5I5M9nHO_jUZDh_nc3R-ryoozQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0ce8fafd3.mp4?token=rVAN8aXRoQz9bktmh_scnmrCWJVzqfF5EWeqs9kEvKXduijrtsTctFVtVbUAAaiJoO6WDNMkaK_ylA3uQmDYa3jcxI_vCaqc3Wwrp3X0Z0ugwh6NozprBPFZsfvk4ZEDm5ybdXi9paPhKiN9f7iIvA3uFh8wvYFWjxJDMw0EOfbYWqij0VmjOHMbrscFnSA9_Dw2fM-fAcgeJh7GZQXV8Cnau6_lE90JgZd5rRcssWdKzJMxS8fKRVrUs-mFjCtn0O7vbMwYwu5yOytMm3GSbkcK-tp33KlRjwj4CYYfdjl55YJ96E2Hu6fcn3qm5I5M9nHO_jUZDh_nc3R-ryoozQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام معاون رئیس کنگرۀ ملی خلق چین به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/446327" target="_blank">📅 17:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446326">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86a1ad1097.mp4?token=eEPU4fkeeBPGkECKC01BbUJIPbeh19oVZnUomOShf7jm4bOj56jPIfe0JWAt1Z17g22CLQbETt-z2hRCYcMhJT4VoT6IYar_yxGdFOd-ozck3pKTactNVGW9hlDpM9b1mqAWY5A-7b_VczkTfmwLtPf6RoM4-B3GbWtfTm2h3-cIFtMzUNQ76QPG8DZw0ZTrPzIEtaDZCONS0PorqEYfQS5F1k6WyBfU0RuYjvMlEGWOUPWB6j5ZzOwfrQ0M4lqQTHp6vbR3zI4wZqTjQPC7PTFsV5jqM4414QYyojkDspWOlC78zPIOYWm9WC6B7if1bIyNDr3jQPMNuGVMKyhV5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86a1ad1097.mp4?token=eEPU4fkeeBPGkECKC01BbUJIPbeh19oVZnUomOShf7jm4bOj56jPIfe0JWAt1Z17g22CLQbETt-z2hRCYcMhJT4VoT6IYar_yxGdFOd-ozck3pKTactNVGW9hlDpM9b1mqAWY5A-7b_VczkTfmwLtPf6RoM4-B3GbWtfTm2h3-cIFtMzUNQ76QPG8DZw0ZTrPzIEtaDZCONS0PorqEYfQS5F1k6WyBfU0RuYjvMlEGWOUPWB6j5ZzOwfrQ0M4lqQTHp6vbR3zI4wZqTjQPC7PTFsV5jqM4414QYyojkDspWOlC78zPIOYWm9WC6B7if1bIyNDr3jQPMNuGVMKyhV5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام معاون دبیرکل سازمان همکاری اسلامی به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/446326" target="_blank">📅 17:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446325">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f186ac745.mp4?token=nO6X4tRCtWgYHsnc6H3qFzbaVoNl3ILqu7l2AOm-HWD2eZQ-uAno9cr0dYcRCUWtvnFw0tE0O3rfx4XyImWHWIdQZCVvxB8uFKbO2ncMyCIA3L9aMwzGNieLX72HSarPjI80OIiq8K5_eCtRSP2LEeIvJ16ObMuVqzkkej6twMOaOd0BB--WPL36mWWovU0fEbjMCh5S4NlyVs0Egtc4cHRVfe5dRekkUTM8XnGdGLXLi_wnSwF7zSV5OLEo9c34hDHq98N9H00zmwRWVdgnLKEh8Jt-EkvkgLHkQmwBOpf67yCd0pXDvUB2AENO9aJeT_MwXYvZBlgGZbz6UXHIFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f186ac745.mp4?token=nO6X4tRCtWgYHsnc6H3qFzbaVoNl3ILqu7l2AOm-HWD2eZQ-uAno9cr0dYcRCUWtvnFw0tE0O3rfx4XyImWHWIdQZCVvxB8uFKbO2ncMyCIA3L9aMwzGNieLX72HSarPjI80OIiq8K5_eCtRSP2LEeIvJ16ObMuVqzkkej6twMOaOd0BB--WPL36mWWovU0fEbjMCh5S4NlyVs0Egtc4cHRVfe5dRekkUTM8XnGdGLXLi_wnSwF7zSV5OLEo9c34hDHq98N9H00zmwRWVdgnLKEh8Jt-EkvkgLHkQmwBOpf67yCd0pXDvUB2AENO9aJeT_MwXYvZBlgGZbz6UXHIFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام دبیرکل سازمان همکاری اقتصادی D-8 به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/446325" target="_blank">📅 17:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446324">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/890cd49f92.mp4?token=EIaW0a85oZthgVViWYo-ZbBpSklfp8hJmLOcM6IwS3slyWyR5GPKylUXrNTdTr6_r10PVGBOlGvwzhwxdTn9--6KvxBtLa9WneqPcfu4pIDQLIuTkxF72YC6ABGWzSI8xQEjXgbYg_B1OfU8RVuVtKAyusKzIzI9rxRWaVRWXNZ5RpuxFvUjScuxq3oD3Mr7FEEOXezvUg1pzkDY_fRHsPoxwOEDWljkTAdwDXP20S81ESYVejd0g4nAzelTczquKclja6u-8Q_hxmMhiU3SvK43fa0rvQvMRtPEAnnUcy_IKkKg6puRuMpy_jj14WYrhlWGtyvbqugKAaoZ3Ff3gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/890cd49f92.mp4?token=EIaW0a85oZthgVViWYo-ZbBpSklfp8hJmLOcM6IwS3slyWyR5GPKylUXrNTdTr6_r10PVGBOlGvwzhwxdTn9--6KvxBtLa9WneqPcfu4pIDQLIuTkxF72YC6ABGWzSI8xQEjXgbYg_B1OfU8RVuVtKAyusKzIzI9rxRWaVRWXNZ5RpuxFvUjScuxq3oD3Mr7FEEOXezvUg1pzkDY_fRHsPoxwOEDWljkTAdwDXP20S81ESYVejd0g4nAzelTczquKclja6u-8Q_hxmMhiU3SvK43fa0rvQvMRtPEAnnUcy_IKkKg6puRuMpy_jj14WYrhlWGtyvbqugKAaoZ3Ff3gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
|
آغاز مراسم تشییع پیکر داماد رهبر شهید انقلاب، شهید مصباح‌الهدی باقری‌
#باید_برخاست
@rahbari_plus</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/446324" target="_blank">📅 17:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446323">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a0146f38.mp4?token=jERDAg7aGR8xyuqIQgw_BPUUnSQWBGPYXzT3CBPWyVE_9hQ9NFpVwNNmzHOvtepcWysNh7uGhtTGCRRgc9aNbl4DnTPD706yKOsEE0dzifPyhaanitgWotXTc7uAugvtmL1ktdUcYM6JE0wu_6j_nDrrwRlpk38fOJWrDfvQrARen8G8zVeqUke-5QHJ_N4bJLLycDxRDijtmXjhrvQvZcZkDL7Dwu_ED5bb7AJe_5xvNKj4zdlwA5RyHTjNKCKocD8aVhySoCVfT9EgL5YE76K6E-thwEx-u6OlRdi7dVic-hHIKZ_YlxZ2ASGe9ggAyNGLE_cvQ5muTEPbzkLn1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a0146f38.mp4?token=jERDAg7aGR8xyuqIQgw_BPUUnSQWBGPYXzT3CBPWyVE_9hQ9NFpVwNNmzHOvtepcWysNh7uGhtTGCRRgc9aNbl4DnTPD706yKOsEE0dzifPyhaanitgWotXTc7uAugvtmL1ktdUcYM6JE0wu_6j_nDrrwRlpk38fOJWrDfvQrARen8G8zVeqUke-5QHJ_N4bJLLycDxRDijtmXjhrvQvZcZkDL7Dwu_ED5bb7AJe_5xvNKj4zdlwA5RyHTjNKCKocD8aVhySoCVfT9EgL5YE76K6E-thwEx-u6OlRdi7dVic-hHIKZ_YlxZ2ASGe9ggAyNGLE_cvQ5muTEPbzkLn1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام نمایندۀ دولت و پادشاهی تایلند به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/446323" target="_blank">📅 17:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446322">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dcfe28f4a.mp4?token=Rprwm9JIutlZtT6QtgBCOVxWMGDiBljd2A68pHHxmfN0DPb0J5cdhPSlYvPL1sO1pI7NVvEfiFHbhNtVJWyH0wxdMhws4_mVvWKEISEg4YtvJfF5UARG8sjioWfxapzUju0t4fYX1JV8rAnXKUvlnHsFT87dLHYk-LtSyf0-lKJ2DPB_xkdA2NK_P_PL1vP8u7pvhpD-hVQZb70h07A9pWQ86116s20YLu0fvFoBAZPXmMRfGtO_ohjHaqs99SN45JClY8ntRvApgSh6KJseDX4rU6VxFCKUtfg_TppIMEX88YLxBwEpIr0Hwb6UuNUcb14trbjdkg9oX235Z01feg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dcfe28f4a.mp4?token=Rprwm9JIutlZtT6QtgBCOVxWMGDiBljd2A68pHHxmfN0DPb0J5cdhPSlYvPL1sO1pI7NVvEfiFHbhNtVJWyH0wxdMhws4_mVvWKEISEg4YtvJfF5UARG8sjioWfxapzUju0t4fYX1JV8rAnXKUvlnHsFT87dLHYk-LtSyf0-lKJ2DPB_xkdA2NK_P_PL1vP8u7pvhpD-hVQZb70h07A9pWQ86116s20YLu0fvFoBAZPXmMRfGtO_ohjHaqs99SN45JClY8ntRvApgSh6KJseDX4rU6VxFCKUtfg_TppIMEX88YLxBwEpIr0Hwb6UuNUcb14trbjdkg9oX235Z01feg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام فرستادۀ ویژۀ رئیس‌جمهور میانمار به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/446322" target="_blank">📅 17:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446321">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc21aa2be.mp4?token=idNOUY_gsL6INlccukhF9UNu5HEHKbo5pxuONFIMlpP75rn5iPKGZ-GTFXOFJfPhTWv0t7r4LzlH_GqQSs0xUfPMLOwqi5soAIDDDrQ7uWE8C8qM6fw_AmQxIF0vQMBbYG71EVwxnZ51JT0vMrW_pOHNMlxw8N-HVJKcyeJsEdJ66kLWMFVW07KkITloFFfN6l5g8prLOGSNbri7vDvXmIyi6Kzkpd1TCBQ_yOY9boIIJNqdvarcGzr6Td-88ySEXT_XAkct6wSrVFhetoffP_HyQCBcngBssN6cwMfExrfrXCDYhWAvqlgx0Aqshwx0bjwkp_C79zPzwSbu3bxJhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc21aa2be.mp4?token=idNOUY_gsL6INlccukhF9UNu5HEHKbo5pxuONFIMlpP75rn5iPKGZ-GTFXOFJfPhTWv0t7r4LzlH_GqQSs0xUfPMLOwqi5soAIDDDrQ7uWE8C8qM6fw_AmQxIF0vQMBbYG71EVwxnZ51JT0vMrW_pOHNMlxw8N-HVJKcyeJsEdJ66kLWMFVW07KkITloFFfN6l5g8prLOGSNbri7vDvXmIyi6Kzkpd1TCBQ_yOY9boIIJNqdvarcGzr6Td-88ySEXT_XAkct6wSrVFhetoffP_HyQCBcngBssN6cwMfExrfrXCDYhWAvqlgx0Aqshwx0bjwkp_C79zPzwSbu3bxJhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدودف وارد تهران شد
🔹
نایب رئیس شورای امنیت فدراسیون روسیه به عنوان فرستاده ویژهٔ پوتین، برای شرکت در مراسم وداع رهبر شهید انقلاب وارد ایران شد. @Farsna</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/446321" target="_blank">📅 17:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446320">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08572f73b5.mp4?token=tnYet_9eZEsfCcvfo2mcTwVn5XBWJPHtkHKWyADgGg0jol8sRB0Q8ZAtU10y0LWDw9Ly4984fwv2UXyTTYKb6XC8bwmj1TCUHl52CjA2sV0uO8d7nNXWeBP65BOdagkQ18Yy2rgcJ9MbJVLOvLp3pdCKdVOBNz3RAB1RltQ68J6diiqOLWW_l0P9V6T1rp-vZuVE_SXrCSeo27kotZrovLPgDowhzLeIbSllcW5EMISZjwHou9zfAcDSudG-lTWYg0RLMxKM2X3CeXSX1hBtLlIAFRjIBGyEzq97MQsjSUe28TLcXbr-O46ybKjX6AMLBz2uu8iWWvzNF6euvxu5bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08572f73b5.mp4?token=tnYet_9eZEsfCcvfo2mcTwVn5XBWJPHtkHKWyADgGg0jol8sRB0Q8ZAtU10y0LWDw9Ly4984fwv2UXyTTYKb6XC8bwmj1TCUHl52CjA2sV0uO8d7nNXWeBP65BOdagkQ18Yy2rgcJ9MbJVLOvLp3pdCKdVOBNz3RAB1RltQ68J6diiqOLWW_l0P9V6T1rp-vZuVE_SXrCSeo27kotZrovLPgDowhzLeIbSllcW5EMISZjwHou9zfAcDSudG-lTWYg0RLMxKM2X3CeXSX1hBtLlIAFRjIBGyEzq97MQsjSUe28TLcXbr-O46ybKjX6AMLBz2uu8iWWvzNF6euvxu5bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام وزیر ارتباطات صربستان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/446320" target="_blank">📅 17:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446319">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df855a6622.mp4?token=YncLd-BRVK8ivEdMj-OGCOn7kxOJbhBPpRAYrqSm1eEy73lX-s_zK4CEZ-UA4b1KLsusuxIhhdB7QIcJR2Al15_UwImnGlLhGM8zOziOQ2Kx-Ur1uV7Rhc0Er6vCNysH2ecDaqdANFsd74RboBh949EY3sX5m2bdJjFoV4MsxX7ZtZujVVAG42WZneGWzZamf6IqbQshl3r4Q25eM7x7wBOyGYkf5Szahu5IQP3LRAOW-5yjt1A3TvIYIxaZBsZXqKKnJzwYp6_6iSrcMst2g83vqn77ZcY2L-jKU-M2OhW8yoq6tu0Sv5zvIs6FXgoE1W-L7udlwPaWgNEj0VAEBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df855a6622.mp4?token=YncLd-BRVK8ivEdMj-OGCOn7kxOJbhBPpRAYrqSm1eEy73lX-s_zK4CEZ-UA4b1KLsusuxIhhdB7QIcJR2Al15_UwImnGlLhGM8zOziOQ2Kx-Ur1uV7Rhc0Er6vCNysH2ecDaqdANFsd74RboBh949EY3sX5m2bdJjFoV4MsxX7ZtZujVVAG42WZneGWzZamf6IqbQshl3r4Q25eM7x7wBOyGYkf5Szahu5IQP3LRAOW-5yjt1A3TvIYIxaZBsZXqKKnJzwYp6_6iSrcMst2g83vqn77ZcY2L-jKU-M2OhW8yoq6tu0Sv5zvIs6FXgoE1W-L7udlwPaWgNEj0VAEBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام نایب‌رئیس جمهوری یمن به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/446319" target="_blank">📅 17:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446318">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1bbyHvVAqWgWERkHQz_nuIu8w6KES0Bn6WMv6lb8xRM2NBxly7tDcRD2OiJdyWB3-sIG7keojhdxPh8bMRqYTEk-Wqt3njF9GcK1wCVs7s3wKm_ubM4hyIDBKdyiIStR3uFadjHb9MKll8gxBI_kLkUtAW84j7T5ZiSCyZCtJ71GmIFdadkMcuLIN6n6UAQIrDNYmD24pbWDEptLbxjAVqssr2XdVsjGAtaU1Nfcl9h8MGVKpQ9hgYxVEpuh17KYTpl7BccvetF72Nb7a5TH_I3QziNI2EF8a6JfFaCO6uYRDrdA_VLELQd8bd21IwCmSbczllfEjeYN7POtMtCJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های خارجی مدعی تحویل ۵ فروند بوئینگ به ایران شدند
🔹
رسانه‌های خارجی مدعی شدند که با تایید دولت امارات، شرکت ECT Aviation Support که در این کشور مستقر است، تاکنون پنج فروند بوئینگ به ایران تحویل داده است.
🔹
بر اساس این گزارش‌ها، این پنج فروند هواپیمای پهن‌پیکر دست‌دوم بوئینگ 777-268ER که پیش‌تر متعلق به شرکت هواپیمایی عربستان بودند، به شرکت هواپیمایی ماهان ایران تحویل داده شده‌اند.
🔹
گفته می‌شود که دست‌کم دو فروند از این هواپیما‌ها در فرودگاه مهرآباد تهران هستند.
@Farseconomy
-
Link</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/446318" target="_blank">📅 17:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446317">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9725ce55.mp4?token=qcxjsbM9AQWYTh84FCXfWVt-nNx-61ULvyS8tkCLG8SpgevuU2AeiqdnVsyvYKNAl-k6RexGRfgwBjtCI2uO0AaoVTIUD9TEAiBQ5kZu8R_jq9Rtro9LkS2gNETtJdODXTUKteDaJBmmCaBNVxazB74bWsAAFZOBp-iHRGsdOjoC5vh0e0foUuGhDfrFpAYTfmlCTWXE19Ux7HLYPvBBDsBH00rSBTgRrpYYaLEISWN9HH1MRwWcECv0sms-Who6UKL45lLdfgaM1Px-zsAv_X5eCDEzzRsB-XXMKNk3ABS_XkxbhU-qPlRXC9OeUgH4o1DQljhgPpA_Yfqy7UWUPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9725ce55.mp4?token=qcxjsbM9AQWYTh84FCXfWVt-nNx-61ULvyS8tkCLG8SpgevuU2AeiqdnVsyvYKNAl-k6RexGRfgwBjtCI2uO0AaoVTIUD9TEAiBQ5kZu8R_jq9Rtro9LkS2gNETtJdODXTUKteDaJBmmCaBNVxazB74bWsAAFZOBp-iHRGsdOjoC5vh0e0foUuGhDfrFpAYTfmlCTWXE19Ux7HLYPvBBDsBH00rSBTgRrpYYaLEISWN9HH1MRwWcECv0sms-Who6UKL45lLdfgaM1Px-zsAv_X5eCDEzzRsB-XXMKNk3ABS_XkxbhU-qPlRXC9OeUgH4o1DQljhgPpA_Yfqy7UWUPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام وزیر آموزش عالی گوام به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/446317" target="_blank">📅 17:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446316">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd3533d1cf.mp4?token=mzicqYbQCAuc7yoH_6jk7fYqrOOauk3z1OCdxd2H-wORqZ12aRIuEoQqtDES8Sn2HvHDwa83AUR9IkZQrZwUPym0XNJxFMJ2uJIgIE0WrIIXvLbrbRtY4XDb7wJ_y9YpT9Qj3Lwx5TBPxIvJoQYAdoG1nv9iUOgpM7y_irlA64xuVSrvZWBZRTcZo3KjvRBFWPmVYh1BQcEEEkU38-9BUZdvqMckl_9B1r9dl7F86rsyIgnXD7pzGeCSCtpjCpwasduziFwLObOIGjOV1i3-nEFTd3UB5KEWN65RCXG_xEH7Bg-2hKC-nndlLcfKmFE_NO70yr2NxT-7pXMszco1Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd3533d1cf.mp4?token=mzicqYbQCAuc7yoH_6jk7fYqrOOauk3z1OCdxd2H-wORqZ12aRIuEoQqtDES8Sn2HvHDwa83AUR9IkZQrZwUPym0XNJxFMJ2uJIgIE0WrIIXvLbrbRtY4XDb7wJ_y9YpT9Qj3Lwx5TBPxIvJoQYAdoG1nv9iUOgpM7y_irlA64xuVSrvZWBZRTcZo3KjvRBFWPmVYh1BQcEEEkU38-9BUZdvqMckl_9B1r9dl7F86rsyIgnXD7pzGeCSCtpjCpwasduziFwLObOIGjOV1i3-nEFTd3UB5KEWN65RCXG_xEH7Bg-2hKC-nndlLcfKmFE_NO70yr2NxT-7pXMszco1Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام رئیس مجلس سنای پاکستان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/446316" target="_blank">📅 17:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446315">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de0472153.mp4?token=Yt0ozbFeDZGM4xam0W2FnJcRvSePHhQkSKKQOmu9IrCKrYvcZ0M6iVVlu8uGWcMeDcXJhhcMwBge5g-B8HYvYULFOJDOSCLucRhC_d4e1lvtARgCec-lx5xspqTTt9yB1EbYIvOF6Lr5NxYEMzhDqjkYXwQ3f2uQ9Hz2c4ojGz9cTw2e23ke9y2NDgtBMP-7jBDof35SXb6FnbL4PHdek0UPs7-_8s_SmS7zqqOcbq03EnnwnxDbtSyvUvn7XIcfQOfbWyGahGjQJCyIB78E6R8mZgW49oiep3V2OjXA06DEZVEr452wmC18ugYcbRYoPcIPNoBLUGKZvBa5gmRzlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de0472153.mp4?token=Yt0ozbFeDZGM4xam0W2FnJcRvSePHhQkSKKQOmu9IrCKrYvcZ0M6iVVlu8uGWcMeDcXJhhcMwBge5g-B8HYvYULFOJDOSCLucRhC_d4e1lvtARgCec-lx5xspqTTt9yB1EbYIvOF6Lr5NxYEMzhDqjkYXwQ3f2uQ9Hz2c4ojGz9cTw2e23ke9y2NDgtBMP-7jBDof35SXb6FnbL4PHdek0UPs7-_8s_SmS7zqqOcbq03EnnwnxDbtSyvUvn7XIcfQOfbWyGahGjQJCyIB78E6R8mZgW49oiep3V2OjXA06DEZVEr452wmC18ugYcbRYoPcIPNoBLUGKZvBa5gmRzlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام وزیر دفاع ملی لبنان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/446315" target="_blank">📅 17:00 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
