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
<img src="https://cdn4.telesco.pe/file/qnH6093dB_hs3kqc-xb5tae1zdvzf8ZwKfmLvvu3f1cuy2soWhVY4ETnxN8aUCZujewDMFkJsTdLhXRfJYzyANT0so94L6_czv7SBgI0EcioNjzUS79gFwyPBmXEF2qVGtd56_U53fsuOTlrE1rO9oBUL7n_QCiqxvKMIt1Q9ehHhPjnvBVm2RrakBpY7Fdt-8WjVw_Rx-q10o_Ns4aFH-bNugGMvms0FEo-KXQPNNjkZ1pjIKpIbrgkC0ImQ4cU_f8CHObHXL8k5Km3Q3Si-8RQsPGOjiqq2zsFR7-XiF8THE8CsSRtP_zImB6Uazf_FfeNiW2g1GjlrDWGednmiw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 18:02:50</div>
<hr>

<div class="tg-post" id="msg-441173">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3UuUBxejHRoud3Bu1ucu6bqBuPvYFW6ujZNtw2PqKQ62lwZopmmt3m7Rr-6EI-H_deSnT4CJPkYLBF7b0ZLbS_oyq9mV3jf-GMT2ZLKKYYJ_qIzapsNkG8FTeSUYVOV0wfDb8Rjx7phgmXqwBQQOOKX_0_ScOb_99nRerxB2jrJDStOYFPXFDuCqiBRx9alF6oLiwhT0wlY7LlhLqM5QgD1g3bJ-1s3c6L9AuKOSWdc6oKRf4nKf9SjfJ6u_LJ8tBlZ2TwjfiCTmdXUsoW7-hWlp_IXdKiqJySpWGGWLHZGbDaCvaHgvt3huBqE0jUUev0b_FhNMO5G3AjxF_rFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر خوب پلیس برای متقاضیان گواهینامه
🔹
پلیس راهور اعلام کرد مدت اعتبار «برگۀ ثبت‌نام و قبولی مراحل آموزش و آزمون رانندگی» از ۲ سال به ۴ سال افزایش می‌یابد.
🔸
با این تغییر افراد در صورت طولانی‌شدن روند آموزش، تا ۴ سال نیاز به ثبت‌نام مجدد و پرداخت هزینه برای دریافت برگۀ جدید نخواهند داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/441173" target="_blank">📅 18:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441172">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🎥
پدر و مادری که فرزندشان را در حملهٔ لامرد از دست دادند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/farsna/441172" target="_blank">📅 17:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441171">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5yWbJgv2QPoh46Prns7U-tYd7uhKAszOwGX9UO9CJbf2-IoK5HetRbr4vG5c6-udixJQIf7jOq5XxI_5ClTBwL6a1DcxIOBDQRmJRUXkMZKgqE0NbX6QMKPM3vuI0b7C9oxw8cSOOloStuvVOpqO_hXtbpjSSZ2VBqgjOScAAJFwwIq1aw06ksxAg-hKtYtQ8acBvsKEDptLRcqUfRCTMCF4GFOQoisGHtm_wGXJ5eiI8BRPZK-WZcR1v1HyWmbm9WmjOLV26qVIlAJd458QvFrAWRR8fn2sNTFEW45Yj-Oc3XFZ3Wuh_H1zLzQFSUwcQMwJHbcKPjYze_ctfYSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبابافی نائین جهانی شد
🔹
عبای نائین به‌عنوان سیزدهمین پروندۀ ایران در حوزۀ نشان جغرافیایی، در سازمان جهانی مالکیت فکری ثبت شد.
🔹
عبابافی که بیشترین رواج آن در شهر محمدیۀ نائین است، قدمتی چندصدساله دارد و یکی از شاخص‌ترین دست‌بافته‌های سنتی ایران محسوب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/farsna/441171" target="_blank">📅 17:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441170">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmhOrgS1fV8myHE35JG09uDd-graguw6rgbkWfoG7e54wk9Tg3p0-26_oein4j14Erg8oX6FXmCvkjtMr5hWUXmq8CozxJQtxBjdJ4xdVdJiyuU4BuqVMvp93wY4xIifhCgRbFIz0DAOIrcZo-Hp6iQZo6EeKiCFGfCS5aFGYozmSe7WUFWDpQSKHbQ8S3pkMnNl01-qc8fwyxCPOYqbpwtOSgjwnICqYxSedh55TZBo_lWQPscQYENU3oUyF6UCILIlAimOk0i6ffvrKX_IxHI5HmG5lsnK1zd_XBPd_-XwI8wM5abbExmR9Op7kQlthXF1yclnGDi2mFSZv7CkfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام مقصران آلودگی هوا به کجا رسید
🔹
فلسفی، عضو کمیسیون کشاورزی، آب و منابع طبیعی مجلس می‌گوید سازمان حفاظت محیط‌زیست تاکنون هیچ گزارشی دربارۀ ترک‌فعل دستگاه‌های مسئول در اجرای قانون هوای پاک ارائه نکرده و بیشتر جنبۀ توصیفی و کلی دارند و عملکرد دستگاه‌های متخلف را مشخص نمی‌کنند.
🔹
به‌گفتۀ او، با گذشت ۹ سال از تصویب قانون هوای پاک، کمتر از ۱۵ درصد این قانون اجرایی شده است.
🔹
براساس قانون، سازمان حفاظت محیط‌زیست موظف است عملکرد ۱۷ دستگاه مسئول را رصد و موارد ترک‌فعل را به مراجع نظارتی اعلام کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/farsna/441170" target="_blank">📅 17:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441169">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d26352c7b.mp4?token=FTkflXV5-L5vDgQYeMY80nHzLO25N5hSfhb-CU0Wmq_NYYJso6vD8A09PCijYKPtMXKNxX3r5FM1ksDsfGitkQakk1QYrU8lrzaYCA98TuHRQrALra6xqpwE6OKdmGNK6cr5mn1nhXUB4srVWSMnkDbatGxCLmMyTMWN3QNUE5sZyBgsDJFmej7HU9JdXtV61TLc2mZv5ZmTO4bQBA29BHIlW41NqIet3-gOj9zGc88k5Ricat3bZwEdGBdgyej0R8mJm5OmuFKwqTVPzf-RBMEpL3r3eq49G885wrh1Jntx_Y97WmgAIcX1uLkjmqtMDvmX2EX8Fr10_TubwaReAouYGi7-g7wbO44pcOVEFYryefbxNykKM0mOXxjIbJ4m3hQvjYC4XaDPVrAf0eTjxI9HZCtxEe6YdUHVs6xgm_iXYLsGgqSe5alyLPuG5T5htQfp0EyfugcLNH6QjQhVeZ-DU-Ht9POSHZpInxS7cK0nAZTPZjhLxZEK531kLnOC9LeuSMpWOCYLRClbILWfhyQiHfpvIdSgO5dJCJwgRW_8fWVPXsA5NMstvhwWhVpRY38oNBqcOhBWmTABpDUszNZ70x8brY-j8p5wnsl_HIRVUZG0UhO0sb6nHa6XU-ouM1-oHA7YJhhMmb8wrWkhY4dZi1Zbpu3pTjqkB06Pl7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d26352c7b.mp4?token=FTkflXV5-L5vDgQYeMY80nHzLO25N5hSfhb-CU0Wmq_NYYJso6vD8A09PCijYKPtMXKNxX3r5FM1ksDsfGitkQakk1QYrU8lrzaYCA98TuHRQrALra6xqpwE6OKdmGNK6cr5mn1nhXUB4srVWSMnkDbatGxCLmMyTMWN3QNUE5sZyBgsDJFmej7HU9JdXtV61TLc2mZv5ZmTO4bQBA29BHIlW41NqIet3-gOj9zGc88k5Ricat3bZwEdGBdgyej0R8mJm5OmuFKwqTVPzf-RBMEpL3r3eq49G885wrh1Jntx_Y97WmgAIcX1uLkjmqtMDvmX2EX8Fr10_TubwaReAouYGi7-g7wbO44pcOVEFYryefbxNykKM0mOXxjIbJ4m3hQvjYC4XaDPVrAf0eTjxI9HZCtxEe6YdUHVs6xgm_iXYLsGgqSe5alyLPuG5T5htQfp0EyfugcLNH6QjQhVeZ-DU-Ht9POSHZpInxS7cK0nAZTPZjhLxZEK531kLnOC9LeuSMpWOCYLRClbILWfhyQiHfpvIdSgO5dJCJwgRW_8fWVPXsA5NMstvhwWhVpRY38oNBqcOhBWmTABpDUszNZ70x8brY-j8p5wnsl_HIRVUZG0UhO0sb6nHa6XU-ouM1-oHA7YJhhMmb8wrWkhY4dZi1Zbpu3pTjqkB06Pl7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ پهپادی حزب‌الله به مواضع نظامیان صهیونیست در ۲ شهرک الناقوره‌ ‌و القنطره در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/441169" target="_blank">📅 17:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441168">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHz71K81YuRoa9_ahmBfkhyivMp0REn6maj3Uvx4ADUZHj-GeRU8E8GekTUFLLhCzwzdtUJg6pI1ZvAqOUIxs2c0srKnTN-sqEsw2pThalq5hporyT1I9VMHRwJWlEpX8WJYXWjfgrkRRa8GuNilOCT7j9Wa_z_Q4UNXqQ1RPT1SbpfGGG8fHYOI5e98WIUsORIkkV5yram-jNukfElJcwmzQTlwfvl4XMEf-6cGlq2DgOiDGSdSPcVqFMlzgy9JuwNXRg0dBySb9R_hHe29WNUhY7t3pN8w5m6YvXnh-iTvckKc1og6GJhAwNFxKqEfvZ1EreWAn9qfWe58Y1xXFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۲ هزار حاجی امروز وارد کشور می‌شوند
🔹
رئیس سازمان حج و زیارت اعلام کرد امروز بیش از ۲ هزار زائر ایرانی با ۹ پرواز از جده به فرودگاه‌های تهران، اصفهان، شیراز و گرگان منتقل می‌شوند.
🔹
هنوز بیش از ۱۰ هزار زائر ایرانی در عربستان حضور دارند و عملیات بازگشت آن‌ها همچنان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/441168" target="_blank">📅 17:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441167">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZfojin-8acRaFuds7TataHlXw-a9UKHomanK1GgzW-hrFabydMFORlzLy3THoYsy-JBYnFOvrrz136lsvz6JYZYReZJtAaJJDoi2KFXYha0qjWrChUJgVyBbBUQOqAhQNPYS1qaSD2FMpdS7cNkvzVJAkcd7xNGQDhP4c4DrcTYI2B27ei47oomq8J7IqjR2BeQJQYsFAoz5vqVuaXrXQiZHdlyFMwM_GjHtDO53H9vnmfq0QR1MENChcWJYVSNC7hfLdSAqevjmpb9voMpGzFYX1re42__FG-0LUfAP-DY7E6w-fnG_Z5Dk1TQgW6pBBsseQ9r27hhmOVy95C45w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال اصلاح مالیات کسب‌وکارها در بودجۀ ۱۴۰۵
🔹
رئیس ‌کل سازمان مالیاتی اعلام کرد با توجه به فشارهای اقتصادی ناشی از جنگ ۱۲ روزه و مشکلات ماه‌های اخیر، احتمال اعمال اصلاحات مالیاتی متناسب با شرایط جدید در بودجه ۱۴۰۵ وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/441167" target="_blank">📅 17:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441166">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4b4ccd71c.mp4?token=Gsvqg9BRBAR2--p9RensZLDQn36e-O324SE_mF8z0g9cE9iVDo4Zt1Wr12PWFSPe3VCnNabk6ocBFjrZmSGT9otJ9vVhTyqzW7qqmJJ6lOr-2oC1_q69onoA-UUdpflwKpDmcUX01r81co0SkSI5BUXlq8oQlRK_rxJLC4IB3NHo5dKzXcI-QM0hztR_ltoLghC967fe2kuiVKrp4vHtQoPp3OKplxxRxOaO5AkJhHifhSURbs33Fy7Bb21mSVWwFVgq3U99fLNmkpTGpwZK63Jl1nBb-Ha-RDBGcxb0HS2kCpZnJPzj_xqrWNuB4gbl2FpgE-IOyciC9UJG4BWNUTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4b4ccd71c.mp4?token=Gsvqg9BRBAR2--p9RensZLDQn36e-O324SE_mF8z0g9cE9iVDo4Zt1Wr12PWFSPe3VCnNabk6ocBFjrZmSGT9otJ9vVhTyqzW7qqmJJ6lOr-2oC1_q69onoA-UUdpflwKpDmcUX01r81co0SkSI5BUXlq8oQlRK_rxJLC4IB3NHo5dKzXcI-QM0hztR_ltoLghC967fe2kuiVKrp4vHtQoPp3OKplxxRxOaO5AkJhHifhSURbs33Fy7Bb21mSVWwFVgq3U99fLNmkpTGpwZK63Jl1nBb-Ha-RDBGcxb0HS2kCpZnJPzj_xqrWNuB4gbl2FpgE-IOyciC9UJG4BWNUTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت حجاج از نگاه مسلمانان جهان پس از جنگ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/441166" target="_blank">📅 16:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441165">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkwYy2AfQwa3zo4MDYJ1SGGrObe3zQbJYQRkzyjEApseEhFBLsbUaihPh4gDaj86N5xRtbHtS3bryUkJNshP3PD0nUA5rdVuFWp7Q5k-HYECEoe_d_qu1OrtV3o_85SHerntl6lyukfuSH4A56zzjy1rjI4VJ3A4kcOzjQZPR665mjh2WCzAqJGkbOFO3Tkf8xlIJeSciDs3-5O9FePHIa5r_Pg3ioSH3p9Cw5uqVl8mn_t5d2pfKwV0ZaFV-Gguk-xFvBIqlBBi6t63cvyBpOXkw6Rjj-MYx2r3OzUm7CSjoVVNLNHHKGWgjDPG2legvRHI0qJ9WWyp9gwCTnE-fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلای جهانی در یک روز ۱۲۰ دلار ریزش کرد
🔹
قیمت جهانی هر اونس طلا در معاملات امروز با ریزش ۱۲۳ دلاری حدود ۳ درصد کاهش پیدا کرد و به ۴۱۳۴ دلار رسید.
@Farsna</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/441165" target="_blank">📅 16:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441164">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8867f73f.mp4?token=DiSRnuejqYBwdF3AaT6LYiXIeMTC2tWLabNr6g3VJu9dP8pQgJfdlUGtFdiCoDbE6YCeTbmGCuA-wqu8_YfArfgl1OkJHp3-fWXgAAgLXxAUjS2l2Dx2S7bw3c3Wjap5hdFKgOIOb57NCw-qEE3BOxdkcFHWqFP-uB3Ixh2wzkP3r2PC-pj3tFm0FgbaQ6u1cxbxadvB_utTRp8KnYakwKVAHEDhdEEmLzzYfR8qrkrWPSKooWnsRnPkF1n1TjyFplfThsQjH5MmXXtuNM9b53iCiNY13Ql2Y9v-nrfK7vxUlm3QEHoGL47Wp1FqXQdRjH97NzRj0GcxPJLfnTSbjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8867f73f.mp4?token=DiSRnuejqYBwdF3AaT6LYiXIeMTC2tWLabNr6g3VJu9dP8pQgJfdlUGtFdiCoDbE6YCeTbmGCuA-wqu8_YfArfgl1OkJHp3-fWXgAAgLXxAUjS2l2Dx2S7bw3c3Wjap5hdFKgOIOb57NCw-qEE3BOxdkcFHWqFP-uB3Ixh2wzkP3r2PC-pj3tFm0FgbaQ6u1cxbxadvB_utTRp8KnYakwKVAHEDhdEEmLzzYfR8qrkrWPSKooWnsRnPkF1n1TjyFplfThsQjH5MmXXtuNM9b53iCiNY13Ql2Y9v-nrfK7vxUlm3QEHoGL47Wp1FqXQdRjH97NzRj0GcxPJLfnTSbjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان کار گوشی‌قاپ‌ها و گردنبندقاپ‌های سریالی تهران
🔹
مأموران پایگاه دوم پلیس آگاهی تهران بزرگ در عملیاتی ضربتی، دو سارق حرفه‌ای به نام‌های «محسن» و «رامین» را در مخفیگاهشان در یکی از شهرستان‌های غرب تهران دستگیر کردند.
🔹
این متهمان در بازجویی‌های اولیه به ۲۰ فقره گوشی‌قاپی و گردن‌بندقاپی در نقاط مختلف پایتخت اعتراف کردند.
🔹
پلیس اعلام کرد برخورد با سارقان و مخلان امنیت با جدیت ادامه دارد و هیچ نقطه‌ای برای مجرمان امن نخواهد بود.
🔹
پیش‌تر نیز عامل سرقت مسلحانه از دو طلافروشی در میدان امام حسین(ع) و بلوار اندرزگو شناسایی و دستگیر شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/441164" target="_blank">📅 16:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441163">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-text">دیدند راهبان صلیبی و اهل دیر
خیر کل آمده است به‌همراه کل خیر
🔹
شعرخوانی حبیبی کسبی برای عید مباهله
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/441163" target="_blank">📅 16:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441162">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4625748c1.mp4?token=CmacFMgLvmy22bzndpACxbtQN4n36oXP78bklUOi6Ywn3LUSeptTNQvrVemDcNKRvm9rNouD602wJDofhz74E_5GU0bKPhtLGTKyWLLJd0uOoVfsL3xk4qqehmMMMjF2tRW_dLbisxmygHY8WcmRXoXSc06orUbb2fnZsdlr0W65P7mxrXEoG6SEru1_45w4zD6JY5fV5yVOZURJtknMqArESTKAKJ43bah5G-6smmWWR9kMutXo4ubovWNXllAhhbcJWOLxpTWUNJfL0l4K371Q9E9sGfCywzgCewG0Wy5ff9BAb0yys6oM-tiEG89ZETPxLxmydvlEecHDq-eFlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4625748c1.mp4?token=CmacFMgLvmy22bzndpACxbtQN4n36oXP78bklUOi6Ywn3LUSeptTNQvrVemDcNKRvm9rNouD602wJDofhz74E_5GU0bKPhtLGTKyWLLJd0uOoVfsL3xk4qqehmMMMjF2tRW_dLbisxmygHY8WcmRXoXSc06orUbb2fnZsdlr0W65P7mxrXEoG6SEru1_45w4zD6JY5fV5yVOZURJtknMqArESTKAKJ43bah5G-6smmWWR9kMutXo4ubovWNXllAhhbcJWOLxpTWUNJfL0l4K371Q9E9sGfCywzgCewG0Wy5ff9BAb0yys6oM-tiEG89ZETPxLxmydvlEecHDq-eFlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔞
تصاویر لحظهٔ شلیک نظامی رژیم صهیونیستی به نوزاد ۷ ماههٔ فلسطینی در کرانهٔ باختری
⚠️
حاوی تصاویر دلخراش
@Farsna</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/441162" target="_blank">📅 16:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441161">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01957eb299.mp4?token=GFju5wIZTPW76b8kSadUlAdBxQEJIT3ymqDnf1kFkMIal4KrL0Um70UDSqdA1PZoHwDJ3T1YZWjmv2lsosTfgJWhtzzQ3UysPQ_gS7IVDCk7tMd5NNSFW9O0QREessgGvFJVUzPZUU0eBaskaP04zqv9H9v468y5fdoGRWhs_VFLRpZ9EYPgv6rFBtIjOXxF-LMowbnT4vxqoRYwa_D5P0y1FiAdvsaD4Z_ZQ4egMqGUMyZjIuJwny15-vjIy9CfetNpn2F6Y8X6nhv1eUbDRxJsXT-CjX8hhMOISMbYDH-wzVCFR0EBgKs9oqS3QpSI9OkXCanHUP5fQmyrrPadjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01957eb299.mp4?token=GFju5wIZTPW76b8kSadUlAdBxQEJIT3ymqDnf1kFkMIal4KrL0Um70UDSqdA1PZoHwDJ3T1YZWjmv2lsosTfgJWhtzzQ3UysPQ_gS7IVDCk7tMd5NNSFW9O0QREessgGvFJVUzPZUU0eBaskaP04zqv9H9v468y5fdoGRWhs_VFLRpZ9EYPgv6rFBtIjOXxF-LMowbnT4vxqoRYwa_D5P0y1FiAdvsaD4Z_ZQ4egMqGUMyZjIuJwny15-vjIy9CfetNpn2F6Y8X6nhv1eUbDRxJsXT-CjX8hhMOISMbYDH-wzVCFR0EBgKs9oqS3QpSI9OkXCanHUP5fQmyrrPadjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فیلم دیده‌نشده از سلام نظامی شهدای دانش‌آموز میناب به رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/441161" target="_blank">📅 16:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441160">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🎥
پس از تجاوز دیشب دشمن آمریکایی، نیروهای مسلح کشورمان چه اهدافی را هدف قرار دادند؟  @Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/441160" target="_blank">📅 16:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441159">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a74VSdhZBcDyK0bkduJdTJKlNzR8SH6mw-MV9hDo2BureZt1q_0s67yjAGqlHlIFFAWFKnM45s1_kcZVMuJFkKXoMKXX0KrrOzM-D7huRkMSFvHa_rrLHF2R-IK3zkqlZZZbAk2A0Cl1xbM9E6ia9b9TN5_TNTz-OZ1yevREccwfkBgdkWtr5jv-1SAzp-QRIDbBdd41dHOuCsA39Hz45KdwBjWH4giqrzKHt_qro7KTokQBv3gpKjrOo4VwDPbH-8Gu7-CsJUKacQUtwWqFEui2D7D2vuGAQDEgtRlMWmCQ0pQuRREzd8tKEa0FRQSSY_sCP-ivRXVjFlt4oTkG1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسته ماندن
تنگۀ هرمز کویت را به قرض لوله کشاند
🔹
براساس گزارش بلومبرگ، کویت برای صادرات نفتی خود کاملا به تنگۀ هرمز وابسته است. این مسئله باعث شده این کشور میادین نفتی خود را در حداقل سطح ممکن فعال نگه دارد تا بتواند از آسیب به چاه‌های نفت جلوگیری کند و بتواند نیاز داخلی به سوخت را تأمین نماید.
🔹
مدیر مؤسسه نفت کویت می‌گوید مذاکراتی را با عربستان و امارات آغاز کرده تا سیستم‌های خطوط لوله این دو کشور را به گونه‌ای گسترش دهند که قادر به انتقال نفت صادراتی کویت نیز باشد.
🔹
این در حالی‌است که به اذعان او «ایستگاه‌های پمپاژ و تأسیسات صادراتی، آسیب‌پذیرترین حلقه در زیرساخت خطوط لوله هستند؛ شما دیدید که ایران چگونه هر دو تأسیسات سعودی و اماراتی را هدف قرار داد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/441159" target="_blank">📅 15:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441157">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXeQUY92SezRHWYJ0q8qT3smUd6fY_VyMWGOw27Ks_LZ7Hu5SkWkovaYzteey2X5GDaK2VO3zEX_EoazezFg3TNUw_aD8hJnZ4VXgqUc144iOk5BJmvEd0zyB5qIKPv_PVbZG4zb3M0Ub_rt9jpXbJbZKXbkM4z0hayc5eocNDRCmEYEDkJ-f1MJv-lY0Oe6HWeI5R6sJMUris0D9kL7-5QMkFAqq6z8Kk7f-Q3c4-YaZSn8tZxaVzLA-vp_qWQQ2WRjU7asMY-MSz6Xisz6QG2fIyUnVBHettnPVFp41PN7ovopY6IHXQWmBcCVdHOotop8onE95JP35OmMRfFHuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادق زیباکلام بازداشت شد
🔹
صادق زیباکلام صبح امروز با دستور قضایی بازداشت شد. پیش‌تر دادستانی تهران از تشدید قرار نظارت قضایی او به‌دلیل نقض ممنوعیت هرگونه فعالیت رسانه‌ای و تولید محتوا در شبکه‌های اجتماعی خبر داده بود.
🔹
براساس اعلام مراجع قضایی، زیباکلام با وجود این محدودیت‌ها در یک مصاحبۀ رسانه‌ای اظهاراتی مطرح کرد که به اعلام جرم جدید علیه او و تشدید قرار نظارت قضایی منجر شد.
🔹
پروندۀ او هم‌اکنون در دادسرای فرهنگ و رسانه در حال رسیدگی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/441157" target="_blank">📅 15:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441156">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc5c819659.mp4?token=Z86RWz9c2D_d03AVsgV4eY8HIMWggyCigluHBTwvv0lz0byo6janrRKD8ZrB4vWsVVDDA6RTvjjs1ayaY_G6cLcNnVweHWnE0YArX1_6tFDyq5mBu5J6LRICLaYYsRc8dmafG_l1Z-SPTuLAQ-IEoXdXQhNyGjMw5Bf6W9xNOqADUtwxDCwQYKpoEbhskjiLCJMtmcK2fzf5ZzwObA5914y70Qh4bhDIVvt9kKYm9EqzEUUE_MjqJ7Kj4UaPUuW9LgUzLEINN0yLIB7pGAUs4dEBQn2MTkuBglkFSeiXFyVzTWhOYWSTTJpAly1NjUFlfeNdlC4rrdqML0HxDH4vDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc5c819659.mp4?token=Z86RWz9c2D_d03AVsgV4eY8HIMWggyCigluHBTwvv0lz0byo6janrRKD8ZrB4vWsVVDDA6RTvjjs1ayaY_G6cLcNnVweHWnE0YArX1_6tFDyq5mBu5J6LRICLaYYsRc8dmafG_l1Z-SPTuLAQ-IEoXdXQhNyGjMw5Bf6W9xNOqADUtwxDCwQYKpoEbhskjiLCJMtmcK2fzf5ZzwObA5914y70Qh4bhDIVvt9kKYm9EqzEUUE_MjqJ7Kj4UaPUuW9LgUzLEINN0yLIB7pGAUs4dEBQn2MTkuBglkFSeiXFyVzTWhOYWSTTJpAly1NjUFlfeNdlC4rrdqML0HxDH4vDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشتگ ۱۶۸# تیم ملی ایران در جام جهانی خبرساز شد
@Farsna -
Link</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/441156" target="_blank">📅 15:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441155">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnHUfDAzprHVgeDYAksd91517bi4YN6rCLrmbQiSuQfEze7qcHz6kzyI5AzjchOVIy7dNlX4JAiglMtPt548ScM_XNgvOMO3z8A1RYszjukQnBEC1NoXABWhwhbxFBLTgw03_Ta9sSKHY0bOexyIwEldUxRydQBJxXsBu2JIRnWFFJNji3xD942J_nZHPAggfvyWSFbgQhjg-VTVbsBwxjKK2E69JkYsxiYFctUiqmLRpbbKM9jS19DrVg3EUucaQXdT-m7QBVfe-oteMQl472cpaqEtyeQWpgWE66ZGCJw6cIwhuazBS-BvjLfVwSXwkCjm4kLP4pRAut_4yoZE-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: مدیری که تصور کند برای حل مسائل تنها یک راه‌حل وجود دارد، در واقع شکست را پذیرفته است
🔹
بنده شکست را نخواهم پذیرفت و معتقدیم برای عبور از چالش‌های کشور راه‌های متعدد و ظرفیت‌های فراوانی وجود دارد و دانشگاهیان و نخبگان می‌توانند در شناسایی و به‌کارگیری…</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/441155" target="_blank">📅 15:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441147">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ue5u8V0MGjqacDmZ-ZqrLmb6J-HBNFgg5oUgOG951PZuqab1-1JodnOgcs5M71lw0sSZwfLEF5c_9b2KUyDHy0nJIl0CjIu7uU3KE8yRWvzDbNe4ZB_nJ0ovMS9l26-QNyHit46WEaz18pSZRky9tmfusb5DHE8N_QxF5ZrsGZvo2SeiwGg2Br-_UlumIu2vUCFjFe1ehawZANmCRZpSgEWtgzhfMyzqWRIb_n6mCTzMawSsAfhjzjhA90PABXph1BCcG8fswlNawwi-FvgSHXjS3eRbE3vhA8bCzRua--JYgtxRBjAFAr85JBpFEC7xRnQZkW4cCjV6_KFZAbtmvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: مدیری که تصور کند برای حل مسائل تنها یک راه‌حل وجود دارد، در واقع شکست را پذیرفته است
🔹
بنده شکست را نخواهم پذیرفت و معتقدیم برای عبور از چالش‌های کشور راه‌های متعدد و ظرفیت‌های فراوانی وجود دارد و دانشگاهیان و نخبگان می‌توانند در شناسایی و به‌کارگیری این راهکارها نقش مؤثری ایفا کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/441147" target="_blank">📅 15:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441146">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckbJ5KLnrq_JUSsEmk8gfhXF31eESIFE-qNISyAg46qxStMc5V-87YAgUYZg740Jvt56SuhIbUQFTCOPQS053be_UUQxB11CU-m9dy8mSbKa3yftQ2bWSr3zLLGt2Y4CmggNNMAJva1OaqJyx6T9B2FjiWQhTs0Dlpt0C42KGHw1nMSiogENLqM1-Nb3jzYM0HUUedJj31pd_PPZteobE86_1jH-DD-Dv96dWnEeMMCnPSB0iDuHYxvg4ursRx-OHdex8pApBfMFOPnW7DMVSVrJ3A9D8FN4s5j9nEwCCPZhxFNAMlri_uMphDWkteVgRhV75PLertebqnXcKWWueA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام محدودیت‌های ترافیکی جاده‌های شمال
پنجشنبه ۲۱ خرداد:
🔹
کامیون‌ها و کامیونت‌ها (به‌جز حاملان مواد سوختی و فاسدشدنی) از ساعت ۸ تا ۲۴ در محور هراز ممنوع‌التردد هستند.
🔹
در صورت سنگینی ترافیک، محدودیت یک‌طرفه مقطعی در محور کندوان با صلاحدید پلیس راه اعمال خواهد شد.
روز جمعه ۲۲ خرداد:
🔸
از ساعت ۱۴ ورود خودروها از آزادراه تهران–شمال به سمت چالوس ممنوع می‌شود.
🔸
از ساعت ۱۵ مسیر پل زنگوله به سمت چالوس مسدود خواهد شد.
🔸
از ساعت ۱۶ مسیر مرزن‌آباد به سمت تهران یک‌طرفه می‌شود.
🔸
این محدودیت‌ها تا ساعت ۲۴ ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/441146" target="_blank">📅 15:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441145">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0rI-ZU4lFXh-XpZ1O-AEN_kX4N03tqRoLnJAMH163-8YasXhw3dBAhsV8boeIWIjBodtq59WAnn7Yij1oWydc8NMbjpZp0QPkvNlbYuYA3cycGFp2k5i3O4KFteikrGLe4BNbOkeMBDJhrMTePHOhsNrl4hhkvxVxHgsOx-WhtweShHjfaTszE9dCfGONYb8ATaN3f4hkCvgsX1GkQf70Bw_MxiGL4U664cjdqFBmTcdMu5rXX8yFNydgo4b5JWXzz3wZI6SgFDwH9zPzZX9fD2MQtkzCPs_uAOXGjld4eYnkLR3cdINFks9zRWVOuJ_S30sNQXg1ZH9TyXQy3mmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام رفع فیلتر می‌شود؟
🔹
درحالی‌که برخی رسانه‌ها از احتمال رفع فیلتر تلگرام خبر دادند، براساس اطلاعاتی که به فارس رسیده دیروز کمیتهٔ بازگشایی پلتفرم‌های فیلترشده جلسه‌ای برگزار نکرده‌اند و هیچ مصوبهٔ جدیدی در خصوص رفع فیلتر تلگرام تصویب نشده است.
🔸
هرگونه…</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/441145" target="_blank">📅 15:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441144">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bf0RaT4UJYkD_pojqWJ4l0qA1g5zitymFMUbDwTTRXWya2XIW9RYxS3mmQD14zBgf_uMIvcXQ4jIGiDJNpeAO2f6d7t8RroSWGx5UEtT8MvCX7xm1NluTgSeXcSV7xTcBDfVE5cNUJxG6XMeatftL4aXXEUJku4ww2OaYVqgtfcqPncH8_5U2xKKeio0EnZHl0oDqD-eDHuYWuff1Q5KceKTRlfDB_Kejp4TIKYNG2Y-0c0s0CL233P3m4eiWKtVv33qTbGyfIPSFN4R2Tlb4ktiI6N99Zgh_d8FmDnnvv4DmzTuAgq91t-tMWWsN8kla9COzEZn9GivrS5mA-b26A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۶۳ هزار لیتر گازوئیل قاچاق در سواحل میناب
🔹
فرماندۀ پایگاه دریابانی میناب: ۳ مشک ماری حاوی ۱۶۳ هزار لیتر گازوئیل قاچاق در سواحل این شهرستان کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/441144" target="_blank">📅 15:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441143">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jm2Mtq9MuswkWx3rrNTE7SYR69YxYBdNq0PTg8zlCaOVlZ1tTyHQqpzdkFRX4jGfIWJWzEwb9qlK26jzjflpCrAOtyhxGI3Ky-N3wgfmjKTu-YplXPmEVw3gVxawrCLHsLo_Mx8kAA3Nr6mVnXGMiDAN7SpTwn_QszrydsAFgw38hnPPr-IrkXVSYIbW8MR3cB8gBgIFoAfjc0yU6vnX98YzXEfjo669jfc9_T3wynD482YV3qlXDc4sgMv4jpPinTJohCf8B3EzzTS3tAAz_RQs0roNwUvmyv6qaxN3RLFaqHq0mfmP37yF3ZaWJHp7SQcjEujZigUIrKscQpN4eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیکود نامزدی نتانیاهو برای انتخابات آینده را اعلام کرد
🔹
حزب لیکود رژیم صهیونیستی اعلام کرد که نتانیاهو ریاست این حزب را برعهده خواهد داشت و در انتخابات پارلمانی آیندۀ رژیم نامزد خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/441143" target="_blank">📅 15:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441142">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ff7d0417a.mp4?token=SmEjXH6r2Mh-PJBp9TY7RWNCA7neYZJfPq0Oi-FbeZ1wCAZQcswxsakNEv-n5mI1J8m-XN23PqHzWptk-tdtTtvhMmBBTRBSj6MYmAdQIpzBkU7-HaGdUVfFcXsW-16t8AsNX3v5aQA8R0MpZnQEfzMlF03uIv1iBsG1hR5L5FxuCViiaiTL69nOOfnhBjc9eu3HAEB7OjaELQ2EI_Rty-iArHkt9S43s-Q9UqyzWbFj-9ygYaRwcIaprpF1zXmcEtbLIjuLJRB8lHxtREyGVwj89mGuqyed5bd1Xds5xVjv5-GXIq5ME0yJ-ClawmeMhYpPweL10DkkUX4ZK3Jmwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ff7d0417a.mp4?token=SmEjXH6r2Mh-PJBp9TY7RWNCA7neYZJfPq0Oi-FbeZ1wCAZQcswxsakNEv-n5mI1J8m-XN23PqHzWptk-tdtTtvhMmBBTRBSj6MYmAdQIpzBkU7-HaGdUVfFcXsW-16t8AsNX3v5aQA8R0MpZnQEfzMlF03uIv1iBsG1hR5L5FxuCViiaiTL69nOOfnhBjc9eu3HAEB7OjaELQ2EI_Rty-iArHkt9S43s-Q9UqyzWbFj-9ygYaRwcIaprpF1zXmcEtbLIjuLJRB8lHxtREyGVwj89mGuqyed5bd1Xds5xVjv5-GXIq5ME0yJ-ClawmeMhYpPweL10DkkUX4ZK3Jmwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌بازی ضدچینی تایوان با موشک‌های آمریکایی
🔹
تایوان برای اولین‌بار با سامانه‌های موشکی توپخانه‌ای هایمارس ساخت آمریکا شلیک واقعی انجام داد و حملات دقیق فرامنطقه‌ای را شبیه‌سازی کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/441142" target="_blank">📅 15:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441141">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رویترز: هیئتی قطری امروز راهی تهران شد
🔹
خبرگزاری رویترز به‌نقل از منابع آگاه مدعی شده که هیئت مذاکره‌کنندهٔ قطری صبح امروز پس‌از رایزنی با آمریکا، راهی تهران شده است.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/441141" target="_blank">📅 14:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441140">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2c73674cb.mp4?token=TbZGMiKUS936SpRpydlVzjv4_FUhqS_7P-qIJGCMfUTP2yzx_ONZY-RrIJ9AL6nmUwwPiOseWv5sAIXu0SIbUvU9t3B1q8amtUzvd5Z7L6KRH_xMcCqpWSJreD71M2M2OeMEFLj4lwt7POrvTmy0Zo3Ms2Pm1rG645cMi2iaDun8TQfqbTejjg2VjFIHHALCJezK3QWFtxWM_HV1ZHTnu0Qd5ejqfHHQM8l_M7kkK5BU5eu2idMyCx_Jqf9xE9qIP9ECkYNbcc6OpmYF0mtrEa3CyGUx2foTYwtEQ3HKC6FsdRQbMqlEySP68iPrlFzbkvuWTwgMGkzBKRbl7SM1OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2c73674cb.mp4?token=TbZGMiKUS936SpRpydlVzjv4_FUhqS_7P-qIJGCMfUTP2yzx_ONZY-RrIJ9AL6nmUwwPiOseWv5sAIXu0SIbUvU9t3B1q8amtUzvd5Z7L6KRH_xMcCqpWSJreD71M2M2OeMEFLj4lwt7POrvTmy0Zo3Ms2Pm1rG645cMi2iaDun8TQfqbTejjg2VjFIHHALCJezK3QWFtxWM_HV1ZHTnu0Qd5ejqfHHQM8l_M7kkK5BU5eu2idMyCx_Jqf9xE9qIP9ECkYNbcc6OpmYF0mtrEa3CyGUx2foTYwtEQ3HKC6FsdRQbMqlEySP68iPrlFzbkvuWTwgMGkzBKRbl7SM1OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پالایشگاه بزرگ روسیه هدف قرار گرفت
🔹
پالایشگاه نفت در استان سامارا پس از حملۀ پهپادی اوکراین دچار آتش‌سوزی شد. این پالایشگاه یکی از بزرگترین تأسیسات صنعت نفت در منطقه و بخشی از شرکت دولتی روس‌نفت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/441140" target="_blank">📅 14:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441139">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9232e26f.mp4?token=EtrMEmtESnQN2b8u1WcBLMYU4DUZIdxdrYvP2QA2EM0YWBKplyhGe4HhqoU5Kvq53owOodnI7Cvp3_3iE-XociV1BiTe2elbUZAuGZOGlbXv9ORmc4KtM-jJbuarvGIOXaQTgDC0fU3YF6JjGyUAlnWLYKbRGORF7wMMTijEP5mkZVSvlhwLmLKAPJ-OWsXLysnBBqCWf39LI4Y-fKzgeS5UyC7JGIdUO6C8lBulR6q4ddXCdTik8PAd1n_Er0TaHo3mc9YMCuf5_P3a-14O9jp1tq3ccvWf_iY7E26RMFM0anmvBF20f8-ocu4XHfQ2z3y1lUVzMa8l_wWrjglnww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9232e26f.mp4?token=EtrMEmtESnQN2b8u1WcBLMYU4DUZIdxdrYvP2QA2EM0YWBKplyhGe4HhqoU5Kvq53owOodnI7Cvp3_3iE-XociV1BiTe2elbUZAuGZOGlbXv9ORmc4KtM-jJbuarvGIOXaQTgDC0fU3YF6JjGyUAlnWLYKbRGORF7wMMTijEP5mkZVSvlhwLmLKAPJ-OWsXLysnBBqCWf39LI4Y-fKzgeS5UyC7JGIdUO6C8lBulR6q4ddXCdTik8PAd1n_Er0TaHo3mc9YMCuf5_P3a-14O9jp1tq3ccvWf_iY7E26RMFM0anmvBF20f8-ocu4XHfQ2z3y1lUVzMa8l_wWrjglnww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ آب شرب کوهستک و ۱۰ روستای اطراف تا فردا وصل می‌شود
🔹
مدیرعامل آبفای هرمزگان: عملیات اجرای خطوط لولهٔ جدید برای تأمین آب درحال انجام است و پیش‌بینی می‌شود آب شرب مردم شهر کوهستک و ۱۰ روستای اطراف تا فردا وصل شود.
🔸
بامداد امروز درپی حملهٔ دشمن آمریکایی به…</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/441139" target="_blank">📅 14:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441138">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-NPbq5Uib4k3OOOj_IF-1R7ePjNkfiNai57oO6UebgJ4Js2f0FXJsgjk8UcxLjqOmM9XvJhA1qlRBdcYNhWPebCcQjk-4ZSDs0gNlkmTmhTLH7MH5KQyJTh2JAkKDclBh5_vR7gpEWnjdqEkwc2_RvAnT2CHk1ALWpMsbs5bbY-CTsRTQU7TVeGQsk90HhrgHJkTbVuYqFjWDU-0l7l-eqC5u8QxSZTi25cfwHd9AHA2g0K1eF-Rextri7T53r-bYshyHDzFSn8yXs4mEdGSPiuYTiMVQgURto8RoNser6l1OVmau7SrhvI-h53ue9eznD_vx32i5oxiEhMG4owbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان: حملات اسرائیل به سوریه و لبنان تهدیدی برای ترکیه است
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/441138" target="_blank">📅 14:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441137">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwfeMFgBGtJf5l_x1C5ZdOgHUG2FfmDcq-Y3Fq35gQvaqaltqwhroQKcbQMWNQ8YS_zYDirL-BcSfDJpokOZqxMh5JKMv_wVwrU42VAXU9YC_v558f3c2anuEN6d9ILAMDrFzggFrkyEJGh-ThdLc4lA2zMXLfFjrEM76FTCgpV6T8beuGZpjaoMqbIVneuWBBiV_e_Z0jabXfLy-AqZwIL-R8hp6GPvDdzso5isjc1-_oz8No61pxbBpzqNy24a0NB98fXIA08Qd-4jc48-9LWuV9eQ5ftYaUDEnavUsRRFbvxEUhPqjD0AU4ecrg7ea12-39eDlCLgZa15LOD8ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحولی مهم در منطقه آزاد ارس
جایگاه گمرک نوردوز به اداره‌کل ارتقا پیدا کرد
در پی پیگیری‌های مستمر استاندار آذربایجان شرقی، نماینده مردم مرند و جلفا در مجلس شورای اسلامی و مدیرعامل سازمان منطقه آزاد ارس، جایگاه گمرک نوردوز به عنوان تنها مرز زمینی ایران با ارمنستان، به سطح «اداره‌کل» ارتقا یافت.
مرز نوردوز که در محدوده منطقه آزاد ارس قرار دارد، یکی از مهم‌ترین گذرگاه‌های تجاری کشور در مسیر ارتباطی ایران با حوزه قفقاز و اوراسیا محسوب می‌شود و ارتقای جایگاه گمرک آن می‌تواند نقش مهمی در تسهیل تجارت، افزایش ظرفیت ترانزیت و توسعه مبادلات اقتصادی با کشورهای همسایه ایفا کند.
با ارتقای جایگاه گمرک نوردوز به اداره‌کل، اختیارات مدیریتی و عملیاتی این گمرک افزایش یافته و بسیاری از فرآیندهای اداری و تصمیم‌گیری که پیش از این نیازمند ارجاع به سطوح بالاتر بود، در همین مرز قابل انجام خواهد بود. این موضوع موجب تسریع در تشریفات گمرکی، کاهش زمان توقف کامیون‌ها و تسهیل صادرات و واردات از این مسیر خواهد شد.
ارتقای ساختاری گمرک نوردوز زمینه تقویت زیرساخت‌های گمرکی و توسعه تجهیزات و لجستیک در این مرز مهم را فراهم می‌کند.</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/441137" target="_blank">📅 14:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441136">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgJGYk09RY-ZDKnGvVMP77BbR_9l2TV80otdCmjkoqPIxulC51WTBEcnNsJ5ZDs09kNd7dJPfsntJ3-QKNIo2UuhlFjGWUbRUrcBO7J-Ybtuwu3G8h0K1F7S72pJywE19Q-2W-FxBwGIVJpCtb5mkc7SGR_S1iKDQgAshGcJa5T44-bQdBCd5FQj1o-3inXpDP30sLO4J7li2caUorG_aW_yK8KPtILhgBF-l2Oe62e6RLNFEsMD4FthD4RpH3W_2wSHJZaLl59ogHLKvtdaqCVcPhKvApjvCZYAgLfX9ZuHGYnz6nrptDNjOO62ri1u-oxiE02Z2FMR2sQuE5NJoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ گیگ اینترنت هدیه بدون قرعه‌کشی منتظرته!
🎁
با پیش‌بینی بازی‌های جام جهانی در اپلیکیشن «همراه من»، ۵ گیگ اینترنت رایگان هدیه بگیر؛ به همین راحتی.
اما این فقط شروع بازیه…
با ادامه پیش‌بینی مسابقه‌ها می‌تونی شانس بردن میلیاردها جایزه هیجان‌انگیز دیگه رو هم داشته باشی.
🏆
زمین بازی در «همراه من» منتظر توئه!
⚽️
👇
https://www.mci.ir/-4S0XAJB</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/441136" target="_blank">📅 14:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441135">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/441135" target="_blank">📅 14:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441134">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40024382dd.mp4?token=S_COGhWFGuC8fPT1CV2zVo8O7dpPH87cSjfsABbaxG8y5cZxsh6Td8ZXlbFvgQxI-Z9cSNs7BcNJXgvHF0kYmw35uYgyoUWqx5KFrHwSlJrmSTVPSy-vsCuAcOacMLfpOTEd1cVFTNpAPGA6PceNym40QcPY1D2d0ZL0FHqEiJW_a_hCBxSmYeDT1jtfDC--lBGg2HV4VmR_XFm8phpnmaRxCYOfBAHqe9c9TCSQfVcD6FDiOk7fFaVHndKLrBHzkBs2i1ieZyED5VhlfQQnEEP7f9KXBiChpAKIfK0Ie0C7xc4iNS9f4GrUASYbMJ3T8G2Mcbh34Yszj0nO7BAoojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40024382dd.mp4?token=S_COGhWFGuC8fPT1CV2zVo8O7dpPH87cSjfsABbaxG8y5cZxsh6Td8ZXlbFvgQxI-Z9cSNs7BcNJXgvHF0kYmw35uYgyoUWqx5KFrHwSlJrmSTVPSy-vsCuAcOacMLfpOTEd1cVFTNpAPGA6PceNym40QcPY1D2d0ZL0FHqEiJW_a_hCBxSmYeDT1jtfDC--lBGg2HV4VmR_XFm8phpnmaRxCYOfBAHqe9c9TCSQfVcD6FDiOk7fFaVHndKLrBHzkBs2i1ieZyED5VhlfQQnEEP7f9KXBiChpAKIfK0Ie0C7xc4iNS9f4GrUASYbMJ3T8G2Mcbh34Yszj0nO7BAoojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر شلیک موشک‌های سوخت جامد و مایع دوربرد قدر و عماد و خیبرشکن به‌سمت اهداف آمریکایی در منطقه  @Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/441134" target="_blank">📅 14:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441133">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‌
🔴
قالیباف: جنگ‌های تحمیلی اول، دوم و سوم به جهان نشان داد که مسیر فتح و پیروزی از دل ایستادگی و شهادت می‌گذرد. @Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/441133" target="_blank">📅 14:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441131">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‌
🔴
قالیباف: با وجود شهادت فرماندهان و دانشمندان در جنگ ۱۲ روزه، نه حرکت علم و دانش در کشور متوقف شد و نه توان دفاعی و بازدارندگی ایران کاهش یافت.
🔸
فرماندهان شهید و دانشمندان کشور با سال‌ها مجاهدت و ایستادگی، نام خود را در حافظۀ تاریخی ملت ایران ماندگار…</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/441131" target="_blank">📅 14:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441130">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
قالیباف: جمهوری اسلامی ایران به هرگونه تجاوز با قاطعیت و بدون درنگ پاسخ می‌دهد.  @Farsna</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/441130" target="_blank">📅 14:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441129">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
قالیباف: جمهوری اسلامی ایران به هرگونه تجاوز با قاطعیت و بدون درنگ پاسخ می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/441129" target="_blank">📅 14:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441128">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ad86abac7.mp4?token=vOg5B_luQMRmu3A3-auXhHOdWoNW950DXDqpq9C5zypEMCuXVOtQBdgXGV6WdZ-_x3FYRdRKx_OyyiJakyWOB1_h61DhAz0EF-ws5td5sIDRxINz5qBclfeCGEr6eYRwYfsN7bThKtgaOL41MkDGqZEoCK6BdljKDa9W76lr-ZE1t1MD8jPPqTrNyQMnDOj4vLHu1bONVpLKhbnoXtD5HxbKPyAFSzxAFxrLsrlf6midWpyRRQKP0Z6S4Awyf_inAX1duiQOLtI_KokLdHT_JgSLwmUG1rhxhGHXtl_RCLwSxKgoPw0TtN45O-enxM65y8mmNOB4fVZzQAryaKhi7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ad86abac7.mp4?token=vOg5B_luQMRmu3A3-auXhHOdWoNW950DXDqpq9C5zypEMCuXVOtQBdgXGV6WdZ-_x3FYRdRKx_OyyiJakyWOB1_h61DhAz0EF-ws5td5sIDRxINz5qBclfeCGEr6eYRwYfsN7bThKtgaOL41MkDGqZEoCK6BdljKDa9W76lr-ZE1t1MD8jPPqTrNyQMnDOj4vLHu1bONVpLKhbnoXtD5HxbKPyAFSzxAFxrLsrlf6midWpyRRQKP0Z6S4Awyf_inAX1duiQOLtI_KokLdHT_JgSLwmUG1rhxhGHXtl_RCLwSxKgoPw0TtN45O-enxM65y8mmNOB4fVZzQAryaKhi7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو کمیسیون امنیت ملی مجلس: بررسی‌های ایران مبنی بر همکاری اردن با متجاوزان به کشور ما، تنبیه اردن را درپی داشت
🔹
این رویه شامل کشورهای هم‌دست خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/441128" target="_blank">📅 14:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441127">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🎥
خسارت دشمن آمریکایی به تاسیسات آب‌رسانی سیریک
🔹
مدیرعامل شرکت آب‌وفاضلاب هرمزگان: زيرساخت‌هاى توزيع آب‌شرب شامل ۲ مخزن بتنى به حجم ۵۰۰ و ۲۰۰۰ متر مكعب با تأسيسات مكانيكى مربوطه مربوط به شهر كوهستك و ۱۰ روستاى بخش بمانى با جمعيت ۲۰ هزار نفری در پی حملات دشمن…</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/441127" target="_blank">📅 14:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441126">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoP2gfh_TRBsuLckTbJrRsN3F2Wv9afzIYGAfrnScWvDvmE7ns_WL9QgfR8YUyLdn5ctUy1qjhHkw2AXNxxomCcGJmAcAOjdmocFF6bchX8gc1D6kbsEjOMezLSpHKKtbhNA_4-YVIMWqmpnSeLhmp95Oz9vVVOaHgBt2ED-G_AjlU6yd1OylixeYSoqYhrPxvsCcYf70H5DFoSw-BrvEagOxnZFfthNDaiWgncvvWyTLxrbYWiWP6VXVZuyJKY9KVsW1oDA-sLNXWd-h__DFUPX6rSc_cuRFgHNptztmbWX59sXkFo19QNYXN6rAWL70TmkM1VUw-BuD8MIQFArJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از انهدام آشیانه و انبار پایگاه‌ هوایی رامات دیوید بر اثر حملات موشکی شب گذشته ایران  @Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/441126" target="_blank">📅 14:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441125">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1117278651.mp4?token=In4IOJTWBhQGH0vF3M0D0TD9oFyVgCr9EPhPfFgibykPhWZHsyaDecPq8vLPRVaasSV1kiQIaJD_lR0YRZxM70OofdChfu1mPeI3Om1HdHFFxGYZpOQrrNKlYrzltoCwy6tU6kY9QEXBz6b8Pz4CViPn_OtjR99KlLsCtwqL5DM9ftP5w8mZR_TsZRermPObT6j9DCDXcVXi2gohSOERXUpKRIQVI-gKQeC8IzZMyCuscklk13FizztfZznZ1i04uTUi-a9g5P-Nl1-BQMSMv0gEWI37iKCNXjrRSW0sotwL0DTCK9ry8fTY7DQrnomFUD9R57lDtwlXf6PnKbmAVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1117278651.mp4?token=In4IOJTWBhQGH0vF3M0D0TD9oFyVgCr9EPhPfFgibykPhWZHsyaDecPq8vLPRVaasSV1kiQIaJD_lR0YRZxM70OofdChfu1mPeI3Om1HdHFFxGYZpOQrrNKlYrzltoCwy6tU6kY9QEXBz6b8Pz4CViPn_OtjR99KlLsCtwqL5DM9ftP5w8mZR_TsZRermPObT6j9DCDXcVXi2gohSOERXUpKRIQVI-gKQeC8IzZMyCuscklk13FizztfZznZ1i04uTUi-a9g5P-Nl1-BQMSMv0gEWI37iKCNXjrRSW0sotwL0DTCK9ry8fTY7DQrnomFUD9R57lDtwlXf6PnKbmAVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی حزب اصلاح‌طلبِ ندای ایرانیان: ایستادگی نیروهای مسلح در ماجرای لبنان هوشمندانه بود.  @Farsna</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/441125" target="_blank">📅 14:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441124">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">️انهدام یک پهپاد متخاصم در آسمان خوزستان
🔹
یک فروند پهپاد متخاصم توسط شبکهٔ یکپارچهٔ پدافندی ایران صبح امروز در محدودهٔ روستای چال بلوطک شهرستان اندیکای خوزستان منهدم شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/441124" target="_blank">📅 14:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441123">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9de031baa.mp4?token=QGCwv9M_pkj6YIHiwT2ujs3r1iOZK1RIQKwkMrgyn5VTmy6rRtEXHCidZgA3E-yjTgemcGrBr6As0N67eWyShQXeOJIWwZQGD_07SOS8sY-xAIb8QT-fiLUOeu6CKf0oMUH9ynA6Tv32hgIX4OedV8zyBgevArNTyN7eafsAAZ1hbOiUwvg_4gETktg9iLG9SeBqYYx9SNa1bkMDtNzsy3c3TzKMnrAKT3tE7Gu-lS448r2RyW-H2CROSJjFoIU9sFsuwIWdoKd2zG39xkrM1f147F3e_GwOtSJJ1VCC7mbkbhF1Nr94skRd03eWqQMULfmCSp1fCfcT9Mifr5QrxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9de031baa.mp4?token=QGCwv9M_pkj6YIHiwT2ujs3r1iOZK1RIQKwkMrgyn5VTmy6rRtEXHCidZgA3E-yjTgemcGrBr6As0N67eWyShQXeOJIWwZQGD_07SOS8sY-xAIb8QT-fiLUOeu6CKf0oMUH9ynA6Tv32hgIX4OedV8zyBgevArNTyN7eafsAAZ1hbOiUwvg_4gETktg9iLG9SeBqYYx9SNa1bkMDtNzsy3c3TzKMnrAKT3tE7Gu-lS448r2RyW-H2CROSJjFoIU9sFsuwIWdoKd2zG39xkrM1f147F3e_GwOtSJJ1VCC7mbkbhF1Nr94skRd03eWqQMULfmCSp1fCfcT9Mifr5QrxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: هدایت‌های رهبر انقلاب پشتوانۀ اصلی مدیریت بحران‌های کشور است
🔹
دشمن که از مواجهۀ نظامی با ایران ناامید شده، تمام برنامه‌ریزی خود را بر ایجاد تفرقه و دامن زدن به اختلافات داخلی متمرکز کرده است.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/441123" target="_blank">📅 13:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441122">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6361ab1ac.mp4?token=K2l2cY62DsjW6iApYN8RYLwTtSHCQOPXzkUjbYhRvBqa7hnEVnbRqimEgjtstXeV07jScyPhtD6SqjFYToc8te9GlLRIkEgWHaG8Rq7uhDeOq5HU0YY7pVqFll-H43_JQ83nx1O_aageyiSTDUAg43OY0uOzifqvmTnl4dxYmNDe7_qTLDh3goUC9UsaAbRlVuEalklwPLWnPr_raZFqgyVSfBCp4AK4xkW5s9IkHCQt8AHPZH062BwfcTSN3HiCdWITh-rz0cnf52DDXeze2Ugdq2_kLiwGmL4bpi2OpxTxKCcpLbDyzjLF2bY2KvTjB84S1BBBzjJ4gWXW9qfusw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6361ab1ac.mp4?token=K2l2cY62DsjW6iApYN8RYLwTtSHCQOPXzkUjbYhRvBqa7hnEVnbRqimEgjtstXeV07jScyPhtD6SqjFYToc8te9GlLRIkEgWHaG8Rq7uhDeOq5HU0YY7pVqFll-H43_JQ83nx1O_aageyiSTDUAg43OY0uOzifqvmTnl4dxYmNDe7_qTLDh3goUC9UsaAbRlVuEalklwPLWnPr_raZFqgyVSfBCp4AK4xkW5s9IkHCQt8AHPZH062BwfcTSN3HiCdWITh-rz0cnf52DDXeze2Ugdq2_kLiwGmL4bpi2OpxTxKCcpLbDyzjLF2bY2KvTjB84S1BBBzjJ4gWXW9qfusw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو کمیسیون امنیت ملی مجلس: بررسی‌های ایران مبنی بر همکاری اردن با متجاوزان به کشور ما، تنبیه اردن را درپی داشت
🔹
این رویه شامل کشورهای هم‌دست خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/441122" target="_blank">📅 13:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441121">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a594dfda42.mp4?token=oRrBJaIrz3DgbtM661TJgtGV2Rixp4gc3o8qhwufFYAzQJGATbQthKO4z7s0WUpYsgTy3XNwcHNyTnLcZcJBtm3LcvjrqcYwAEDqZUdDU9JIf_GLMObrhILzTjJN8fs9Ng1gKd1eIvMzibSluv70P19QBr1qoeYZev05nQkwqk4Ihj9Gi-Smq6W7uAg3e97wF1FbTK0-26lXFJy9AuXKsfnT9ObWPhzVpsg6v9IcT-IcRh7t1AzG9mxjOiaKzBV_svtKlvxpf47pNX1eAhPA9c_VWkZ2yTj3adQ2-AkjpTfwRnI0NUeuhc3XNU6bUfgQkkx4zU_aJVIyiXBtNfUiVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a594dfda42.mp4?token=oRrBJaIrz3DgbtM661TJgtGV2Rixp4gc3o8qhwufFYAzQJGATbQthKO4z7s0WUpYsgTy3XNwcHNyTnLcZcJBtm3LcvjrqcYwAEDqZUdDU9JIf_GLMObrhILzTjJN8fs9Ng1gKd1eIvMzibSluv70P19QBr1qoeYZev05nQkwqk4Ihj9Gi-Smq6W7uAg3e97wF1FbTK0-26lXFJy9AuXKsfnT9ObWPhzVpsg6v9IcT-IcRh7t1AzG9mxjOiaKzBV_svtKlvxpf47pNX1eAhPA9c_VWkZ2yTj3adQ2-AkjpTfwRnI0NUeuhc3XNU6bUfgQkkx4zU_aJVIyiXBtNfUiVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: امکان ندارد دشمن یک کشور را با هواپیما و بمباران وادار به تسلیم کند
🔹
غزه با آن کوچکی را ۳ سال است که نتوانسته‌اند وادار به تسلیم کنند. ایران ما را هم قادر نخواهند بود و قطعا تسلیم نخواهیم شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/441121" target="_blank">📅 13:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441117">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bba0f34ba3.mp4?token=j2jUCW32xenfPfbBbNMkyd_JNDWQPt5sKhpTz27lNGmCKGXZuVxsTpRFayKPyDRe83hFh3psim-BknTDuwmvmdR6fwmH1OR_SyVKxv8OAFSBS-vl-SkyGvrePOwmocXkmbTY7mHhDSVzi68Qqybn1RB5nWwRTMSJ8XUQX3-JCuiLT2hr8UX8XTjuXK8_9vzvtLHJ7t6IzsZsG6uAPBqywIonK2ZII9GHaIDpLv6pbR_8g6Czt7iV2kkR9ZPbj8_ESFnNufTS36HTJg1VMw0T1W-4nnAYbstiAEPEwFViJHXd6HFOEnH2bN1_XEOtzFWvyuaZyEiO2d0LRF6Ox017uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bba0f34ba3.mp4?token=j2jUCW32xenfPfbBbNMkyd_JNDWQPt5sKhpTz27lNGmCKGXZuVxsTpRFayKPyDRe83hFh3psim-BknTDuwmvmdR6fwmH1OR_SyVKxv8OAFSBS-vl-SkyGvrePOwmocXkmbTY7mHhDSVzi68Qqybn1RB5nWwRTMSJ8XUQX3-JCuiLT2hr8UX8XTjuXK8_9vzvtLHJ7t6IzsZsG6uAPBqywIonK2ZII9GHaIDpLv6pbR_8g6Czt7iV2kkR9ZPbj8_ESFnNufTS36HTJg1VMw0T1W-4nnAYbstiAEPEwFViJHXd6HFOEnH2bN1_XEOtzFWvyuaZyEiO2d0LRF6Ox017uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معترضان ضدمهاجرت در ایرلند شمالی خانه‌ها و خودروها را به‌آتش کشیدند
🔹
پس‌از انتشار تصاویر حملهٔ یک پناهجوی سودانی با چاقو به یک فرد دیگر، اعتراضات خشونت‌آمیز ضدمهاجرتی در مرکز ایرلند شمالی شعله‌ور شد.
🔹
صدها معترض که بسیاری از آن‌ها نقاب بر صورت داشتند، در چند نقطه از پایتخت ایرلند شمالی که بخشی از بریتانیاست، تجمع کردند و در جریان آشوب‌ها یک اتوبوس، چند خودرو و یک ساختمان به‌آتش کشیده شد و ساکنان آن مجبور به تخلیه شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/441117" target="_blank">📅 13:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441116">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0411677642.mp4?token=IuIyhbjQW3-Ii_GTZlevvodP8J9ZB9Ll0dBANByIdPMt5Rvkn0wC147g58kMKQYi9xj6NitEgZq3jFWnqrGYiHZ3ve-EOmSzqakSiJ1jnl0OrhwgJAlhW9C3ehwIUNhLMpjRSd9lpuFanr0kErUJG6q4Svv4rlaLw6hNPoAA5m0ELlhH6ikPE486yPDGd97E_o9XsS6l7wsGUwnjlYeL0QttLNQio4H9HEIC4IwZucWef5tG0r2kn9RIJBJZghcN0cjOHAKgIeqXqCnPldS9HwCaBzrHq4n-M3nPGwMbSwus7_HDrJmXX6pQ2UjUBywEbJDUe7UBMy0OcGCSsIZbbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0411677642.mp4?token=IuIyhbjQW3-Ii_GTZlevvodP8J9ZB9Ll0dBANByIdPMt5Rvkn0wC147g58kMKQYi9xj6NitEgZq3jFWnqrGYiHZ3ve-EOmSzqakSiJ1jnl0OrhwgJAlhW9C3ehwIUNhLMpjRSd9lpuFanr0kErUJG6q4Svv4rlaLw6hNPoAA5m0ELlhH6ikPE486yPDGd97E_o9XsS6l7wsGUwnjlYeL0QttLNQio4H9HEIC4IwZucWef5tG0r2kn9RIJBJZghcN0cjOHAKgIeqXqCnPldS9HwCaBzrHq4n-M3nPGwMbSwus7_HDrJmXX6pQ2UjUBywEbJDUe7UBMy0OcGCSsIZbbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: باید از حالت نه جنگ نه صلح خارج شویم
🔹
دشمن باید خواب این را ببیند که ما در برابر تجاوز آن‌ها کوتاه بیاییم.
🔹
وضعیت نه جنگ نه صلح برای کشور خوب نیست و باید این وضعیت را از بین ببریم.  @Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/441116" target="_blank">📅 13:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441115">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aba412f0f.mp4?token=gQctVdp1nYTbhQCzMp5tCcx_mxC4MkmWnrngd1F2UeK3w79MWMTqrG8xlwlQxxFYFphhmZRtc9shmEETEPGytvNOqvk5wuON2XN6Cif8AgEBDb5T6uVT-Q957LwrmoyepoKHrqByYPKNXCxeUb3w98YuSju_TVvGi9N-0LQWeg2ZVa8fD3T9auTxUm5fgIPenBfcZNlZDotSts7Zkn7ljnE-CbfMc-n9pc7EmxL8oHTVEeihl02joqyPA1lkHdnAzL_dRCLIUWK6B90jL4iNyVf0DVxtIxT2WbfM1FiHTFG4tbhUX1E0KF5l7rbUSjZSI7py9zryZx49mpowXMiNsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aba412f0f.mp4?token=gQctVdp1nYTbhQCzMp5tCcx_mxC4MkmWnrngd1F2UeK3w79MWMTqrG8xlwlQxxFYFphhmZRtc9shmEETEPGytvNOqvk5wuON2XN6Cif8AgEBDb5T6uVT-Q957LwrmoyepoKHrqByYPKNXCxeUb3w98YuSju_TVvGi9N-0LQWeg2ZVa8fD3T9auTxUm5fgIPenBfcZNlZDotSts7Zkn7ljnE-CbfMc-n9pc7EmxL8oHTVEeihl02joqyPA1lkHdnAzL_dRCLIUWK6B90jL4iNyVf0DVxtIxT2WbfM1FiHTFG4tbhUX1E0KF5l7rbUSjZSI7py9zryZx49mpowXMiNsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: باید از حالت نه جنگ نه صلح خارج شویم
🔹
دشمن باید خواب این را ببیند که ما در برابر تجاوز آن‌ها کوتاه بیاییم.
🔹
وضعیت نه جنگ نه صلح برای کشور خوب نیست و باید این وضعیت را از بین ببریم.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/441115" target="_blank">📅 13:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441114">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHbOa7Ke7Py77FXiofdpMWSzlc0ZH8C_7zsCtXiWsStx-FOMfwGYf0wi3jc784I8VUsH_SXm2hYdrW9pnDS0CFOmmNLTHScHRuLDeFe3xhRmfLuaVSdN6vWXiQGYMPmpIw7TA2CotYKGBp23QF7xxsybRtWKU6-kwnBB0ntQpcoi7_I09EHcIuh-GVmW4fQSZiMuMRIK7vz4Xmz2eh6sTMEw5HcWCF2s7f2DhlV88CWSUApVnuwwIg2Q5o2rUSKgBqRQ53tlEsf7XJeVuL1sRg8yzGyappInoMI7EkNoeNDk4HKhlSkmq2adpNjQ6kiPzkQfpkO7NCocrCPyEM2dKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حادثهٔ دریایی در نزدیکی تنگهٔ هرمز
🔹
سازمان تجارت دریایی انگلیس: گزارشی از حادثه در ۲۰ مایلی شمال‌شرقی صحار عمان دریافت کرده‌ایم. موتورخانهٔ یک نفتکش ‌آتش گرفته و خدمه در حال تخلیه‌شدن هستند.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/441114" target="_blank">📅 13:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441113">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7Rl2_W4uISLpe3TLHwrYkdLiOG3LWNgspcuUBfmlMQwLvT7T16Y7INp16GQZCgfT1zQ84Y5Ylpl8oMIehvCXGmw0kxlNAM7iwn6XrUAOYQBi9Zb_RS9C-BSlQELqR2x9c_YQ-n0ixM7VnbGeLjivaMWchxjqH6O73ocrZTtjM8W-ZLbKvwD-mdxXadPgF8w5Ki-EepjP6GYzz5frhByouts38HMS5RrQNMKQZut0aR8S_vGAFjr0VppBiMY5euoylvpJ_pcRHC0I9FTQnVg8HSgjs2yEpu1sFtxqihHhNKnTCtII7A8KrQXShAK9utGUNiyxLsO8ub9sXr_kiHyGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«از سرگذشت» محرم امسال پخش نمی‌شود
🔹
نجفی سولاری، تهیه‌کنندهٔ برنامهٔ «از سرگذشت» در گفت‌وگو با فارس گفت که فصل جدیدی از این برنامه ساخته نشده و امسال تنها گلچینی از فصل‌های پیشین از تلویزیون پخش خواهد شد.
🔸
«از سرگذشت» با اجرای علی‌اکبر قلیچ، جزو برنامه‌های مناسبتی و گفت‌وگومحور است که محرم پارسال فصل سوم آن از شبکهٔ نسیم پخش شد و با سوژه‌هایی متنوع مثل شهدای جنگ تحمیلی ۱۲ روزه، توانست نظر مخاطبان تلویزیون را به خود جلب کند.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/441113" target="_blank">📅 13:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441112">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
منابع عراقی از آتش‌سوزی گسترده در مرکز اربیل و شنیده‌شدن صدای انفجار در نزدیکی پایگاه آمریکا در اربیل خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/441112" target="_blank">📅 13:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441111">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e6704a05.mp4?token=uWJ_OpN5m2l81FJuvuOrZYknrdxih32M6x-BblbV0s7H8eA3cE_d9Myswqj2Z6nC0Z7Ft4o-zvLbv_ZklsWhZyRI74paE42D7S_cCLJy38BL0ZMk3_zlcc3e_nYRSsOMf0bVq0Px5DVDqkTTYw0bKsFbGYi8zT3ePQTnvjLH5s-Qhpw4hkj8xvetDJ-dL8d-6iGuG39iyXIZ1mNHr9U0UErMo5BdJRQqSGeIIEQH3xHRvz6yi6bkL-nxXngBiZSZZVK-fYbQzoYrbopiqcblOiGWzBAnf3EywiilViGOocilyHMQvLvhTY_YPryBPjwSZ1p1qow5WVGyyG2h163o0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e6704a05.mp4?token=uWJ_OpN5m2l81FJuvuOrZYknrdxih32M6x-BblbV0s7H8eA3cE_d9Myswqj2Z6nC0Z7Ft4o-zvLbv_ZklsWhZyRI74paE42D7S_cCLJy38BL0ZMk3_zlcc3e_nYRSsOMf0bVq0Px5DVDqkTTYw0bKsFbGYi8zT3ePQTnvjLH5s-Qhpw4hkj8xvetDJ-dL8d-6iGuG39iyXIZ1mNHr9U0UErMo5BdJRQqSGeIIEQH3xHRvz6yi6bkL-nxXngBiZSZZVK-fYbQzoYrbopiqcblOiGWzBAnf3EywiilViGOocilyHMQvLvhTY_YPryBPjwSZ1p1qow5WVGyyG2h163o0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عبدالکریمی: جریان روشن‌فکری همواره در پی تعمیق شکاف حاکمیت و ملت بوده
🔹
عضو هیئت علمی دانشگاه: روشن‌فکران ما امروز از غرب‌زدگی به غرب‌پرستی رسیده‌اند. این جریان در یکی از مبتذل‌ترین دوران تاریخی خود قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/441111" target="_blank">📅 13:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441110">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxS0dIV57f1KraP76tXI1fWlvzUT_sbPgbWVqVg7fWdfXDTYHrsWvk7fZmgEu_OjJkCgRABJx6ASyrmyMyIyLtrnp3lAh8dfZKjtNIq06-YEV8GKzO_unP6sb23P8JHCzrlExPQv4T01SbvlZDng0DCNKIszd1vRLhMicOgeFZUUQac9pXoaZgT_UT0ZBcmXuASUrc-s_3tW4oo47utOOa7pT7JGbzWjdgfV_i12A_3W0O37oaa5pts0ySx8rlzRMGZNjmxPVWkgR-iUp-lHutqMUfH0_vXye0eU9NP5jZ-GVAGyfJZYSE2hVNgzrGKWPFxcJM3wVdF9p2UUpHe4gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رِد بانک؛ با ارائه مجموعه‌ای جامع از سرویس‌های بانکی، سرمایه‌گذاری و هواداری فوتبال، تجربه‌ای متفاوت و یکپارچه را برای کاربران سراسر کشور فراهم آورده است.
🟢
در قالب طرح «رِدبانکی شو»، کاربران جدید پس از دانلود اپلیکیشن(دریافت از آدرس:
https://red-bank.ir/download
) انجام احراز هویت و افتتاح حساب، مبلغ ۱۰۰ هزار تومان هدیه افتتاح حساب دریافت می‌کنند.
🟡
همچنین هر کاربر می‌تواند با دعوت از دوستان خود از طریق لینک اختصاصی، به ازای هر افتتاح حساب موفق، ۱۰۰ هزار تومان پاداش دریافت کند.
مشروح خبر را
اینجا
بخوانید.</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/441110" target="_blank">📅 12:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441107">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه مالی فیروزه | Firouzeh</strong></div>
<div class="tg-text">💎
شمارش معکوس IPO فیروزه آغاز شد
شمارش معکوس برای عرضه اولیه
#وفیروزه
آغاز شد! در این ویدئو با رامین ربیعی، مدیرعامل گروه مالی فیروزه درباره چشم‌انداز این عرضه و شرایطی که فیروزه در آن عرضه اولیه می‌شود، گفت‌وگو کردیم.
00:40 - دو دهه اخیر فیروزه درخشان و سخت بود!
01:11 - تاب‌آوری و استقامت فیروزه ادامه‌دار است...
01:50 - ارزش‌گذاری فیروزه چگونه بود؟
02:17 - دارایی‌های ارزشمند هلدینگ فیروزه
04:00 - داشته‌های پنهان و ارزشمند گروه مالی فیروزه
03:58 - رکورد مشارکت در وفیروزه شکسته خواهد شد؟
🛒
شرکت در عرضه اولیه
«وفیروزه»
در تمام کارگزاری‌ها با ثبت سفارش خرید از طریق سامانه معاملات برخط امکان‌پذیر است.
💎
گروه مالی فیروزه
سرمایه‌گذاری، برای همه مردم ایران
🔜
+982179672000
💎
@firouzeh</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/441107" target="_blank">📅 12:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441106">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/441106" target="_blank">📅 12:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441105">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jk-TumZ2Z8W5FZ6A4mvjryIsugsU8muffV4Fa9P27sX_kgjOI45KkJ6CE4M_ftnexDJvmGfXgxPM3LlzolVBMv80gABrHnhlFH43swA8weKvef7aPSnvEgyzJLo0qHbnEOLnAUCdQIwCJ_IBhraKuF-_BengTyUUmBGNogdiXpQ3o-Xi8je99UPtBo-Uth--RHBknJGpfWa7mBh0YTM9-N9BwI8pr6XqH5rYqV9q5nPuzfTfbDr_M9m9eL-QtHILIGikB8rPujNMtdrHKxKJ8TxhQmE1oBpqhu-XeFQEzGPK1HpuEJMNxLkVP7C8icpl7elQjMowDbamLBX6hr7Srw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس رکورد جدید زد
🔹
شاخص کل بورس در دقایق ابتدایی معاملات امروز با رسیدن به ۴ میلیون و ۶۰۲ هزار واحد رکورد تاریخی جدیدی را ثبت کرد. @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/441105" target="_blank">📅 12:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441104">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f13cb69a.mp4?token=lozXPAIZzeNpVm40Io9uMm1GftcR2RqhlMEGEJ5sEDL1rdBy65w_R4LPVqEoblXnMouIvwU39IsCnCM7uQY_i-9jo5Eh7AKw_JxUz9jUZ2FDTdH7XXyhSW_2MXDEMSqNgucKAug2HIPUCIcz0kvFtHODZhvpTlsXwGPcTT-hLuEzelVGoV3-dcHrF7tgzjd73fU7nhLfmwGPst_qbnycm_EvZoHkNcjLjmSQ-iVg_cUL2FTffI5j7nwzLKkA9AyFlcRAsFqT9yYVcUpdGoie_bCk5IGCNE7Xvy2S2o3zRBnr8lYtFGEk25uxrDbEXWno3OgBHoaUBY3ZUK9tFS-wwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f13cb69a.mp4?token=lozXPAIZzeNpVm40Io9uMm1GftcR2RqhlMEGEJ5sEDL1rdBy65w_R4LPVqEoblXnMouIvwU39IsCnCM7uQY_i-9jo5Eh7AKw_JxUz9jUZ2FDTdH7XXyhSW_2MXDEMSqNgucKAug2HIPUCIcz0kvFtHODZhvpTlsXwGPcTT-hLuEzelVGoV3-dcHrF7tgzjd73fU7nhLfmwGPst_qbnycm_EvZoHkNcjLjmSQ-iVg_cUL2FTffI5j7nwzLKkA9AyFlcRAsFqT9yYVcUpdGoie_bCk5IGCNE7Xvy2S2o3zRBnr8lYtFGEk25uxrDbEXWno3OgBHoaUBY3ZUK9tFS-wwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعرخوانی سید حمیدرضا برقعی در جشن مباهلهٔ آستان مقدس مسجد جمکران
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/441104" target="_blank">📅 12:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441103">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
انتصاب اعضای جدید هیئت‌مدیرۀ مرکز خدمات حوزه‌های علمیه با حکم رهبر انقلاب
🔹
حضرت آیت‌الله سیّدمجتبی خامنه‌ای، طی حکمی اعضای جدید هیئت مدیرۀ مرکز خدمات حوزه‌های علمیه را برای مدت پنج سال منصوب کردند.
🔹
بر این اساس، حجج اسلام حسین رحیمیان، محمد جعفری گیلانی، محی‌الدین مکارم شیرازی، قدمعلی اسحاقیان، محمدمهدی حقانی و محمدحسین احسانی، به‌همراه نماینده مرکز مدیریت حوزه علمیه قم، نماینده حوزه علمیه خراسان و رئیس جامعة المصطفی العالمیه، به‌عنوان اعضای جدید هیئت مدیره مرکز خدمات حوزه‌های علمیه منصوب شدند.
🔹
جلسه تودیع و معارفه اعضای جدید هیئت مدیره مرکز خدمات حوزه‌های علمیه در روزهای ابتدایی خردادماه جاری با حضور حجت‌الاسلام والمسلمین محمدیان معاون ارتباطات حوزوی دفتر مقام معظم رهبری، دکتر ایروانی معاون نظارت و حسابرسی دفتر مقام معظم رهبری، اعضای سابق و اعضای جدید هیئت مدیره مرکز خدمات حوزه علمیه برگزار شد.
🔹
در این جلسه ضمن تشکر از اعضای سابق و رئیس مرکز، براساس نتیجه رأی‌گیری از اعضای جدید، حجت‌الاسلام والمسلمین حسین رحیمیان مجدداً به عنوان رئیس هیئت مدیره مرکز خدمات حوزه‌های علمیه انتخاب شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/441103" target="_blank">📅 11:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441102">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLsILYsPxtvQ9LNHO4LnM13oBdiKUosP_3Ei0EAy4Ee9WPbW88uKFa4hF60x96ZrHukg50cQWl-dSfn2-bZ-BVHaVJ9tV2U_HhAtKHG5i96iOUMyEaw6c8z-4ElyM_0gUnKdMwtHLYKjbAjVeP4bpgcF7KMDY8Nzom7DXZ-EUxjU68hQNSDav-jOXpLcP5FX6QtKbPI_MdBNfyu6F1kA2utYDy0T44kof6857mXDzd54XWRA-wsFxWqKu-yGupB6uar9tIC82n6UXHwfK7Yk_qrPAE91dwMij9AM6duemOVJNU0pUb1r3NAuhv7eStMR8EOY5W32nvjHIt2lS7KRug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراق در سوگ آیت‌الله فیاض ۳ روز عزای عمومی اعلام کرد
🔹
در پی درگذشت مرجع تشیع آیت‌الله شیخ محمد اسحاق فیاض در عراق، دولت این کشور، سه روز عزای عمومی اعلام کرد.
🔹
در پی این ضایعه، «نزار آمیدی» رئیس‌جمهور و علی الزیدی نخست‌وزیر عراق  با صدور پیامهایی جداگانه،…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/441102" target="_blank">📅 11:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441101">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYnJY8OSGoPKDy8d-eW1408mlI6Ux37fFFVB_WBXNfJ2-6NKuxRmuUgTlUG8dojt6xeXLITnj5M5S30W-7C085otlGDHJdW2W7ASIPyoOLVGr36_eDNHiCBL3kys3mPxcDDZt4822l1vHh6SgXUWbcURTBEcoscbBQnetVuHNJDcVfjVxgCyFbyMF0elO3UARAMtSMsb9yAA9sbK16S4EnosqM8ixbOPYbwMcuhbSjXayrch_aIPKJ_cBbRRk4U9Zo9BogKESbNe7wrRHdT1eZRJ_T3n3OmUo0lClwsAmYWJzwB8cZF_gl4DzhPSVNS-g1n4LvJx-Sdm_B9RoYH7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واگذاری فجر جم و پارسیان متوقف شد
🔹
هیئت وزیران با واگذاری پالایشگاه‌های فجر جم و پارسیان مخالفت کرد؛ دو مجموعه‌ای که در مجموع بیش از ۲۰۰ میلیون مترمکعب گاز در روز فرآورش می‌کنند و سهم مهمی در تأمین انرژی کشور دارند.
🔹
فجر جم حدود ۲۷ درصد و پارسیان بیش از ۱۰ درصد گاز کشور را تأمین می‌کنند؛ موضوعی که به‌دلیل اهمیت راهبردی این پالایشگاه‌ها در امنیت انرژی، واگذاری آن‌ها را متوقف کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/441101" target="_blank">📅 11:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441100">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a85b1410e.mp4?token=DDvuCEa8vgqqFEOcEwmW5X6mPYQzg0Nou7R83Rr2zVBrVkn_xOtmSxjUTR_Jyg6aopFdcy7tW9V4GibqyOYkZ8367Vj63wyJvOZKYyACa63Wm23m_kjtIcTrI7m8KPPuGCs2V1wqA4WGTGhjR0DBX1oylXOFpuqZw8r0_IqjjrjLh5VbNWVeEuyM7uiaUz7WadHqyO0ux3vAzaXztYPkx9hFoUM4FjGzPKSSUIgkQSBOagP6SfZv7Jq5Fu1j4YSxPa-RNHZS6aFf3e18fXpYCkCDLNvAq7IMs2CmaLgYz2qNEdM136r3hrPHxLxlCT7X0vUAPgiCI4I3JnNA8QXEFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a85b1410e.mp4?token=DDvuCEa8vgqqFEOcEwmW5X6mPYQzg0Nou7R83Rr2zVBrVkn_xOtmSxjUTR_Jyg6aopFdcy7tW9V4GibqyOYkZ8367Vj63wyJvOZKYyACa63Wm23m_kjtIcTrI7m8KPPuGCs2V1wqA4WGTGhjR0DBX1oylXOFpuqZw8r0_IqjjrjLh5VbNWVeEuyM7uiaUz7WadHqyO0ux3vAzaXztYPkx9hFoUM4FjGzPKSSUIgkQSBOagP6SfZv7Jq5Fu1j4YSxPa-RNHZS6aFf3e18fXpYCkCDLNvAq7IMs2CmaLgYz2qNEdM136r3hrPHxLxlCT7X0vUAPgiCI4I3JnNA8QXEFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه پاسداران: یک فروند پهپاد MQ9 دشمن رهگیری و منهدم شد
🔹
در جریان درگیری‌های هوایی جاری در تنگۀ‌هرمز یک فروند پهپاد MQ9 که از آسمان شمال خلیج‌فارس قصد نزدیک شدن و مداخله در صحنۀ نبرد را داشت، در آسمان شهرستان جم استان بوشهر مورد اصابت آتش رزمندگان قهرمان…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/441100" target="_blank">📅 11:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441098">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iARFisp2zF2i6v9lJE-Y32rmR4Hig4As3kYpz6QR4dc9uDO1wAUZd1lA7epgT3klhg7UD4DRxOTVwQlYOWQ2Eao5MSp_nhIy49NEnRZRbbbMQXszBckR1FjxbjaEtdOEnjwlgaJoX4ncJSGLZ5qc3DcIAHKybcvo89HjRQg_WtFR_kEZiIq8OKRS8_01usSR5kFhKDFOuGwrKuFxSOBL-Q4Tsk5YPN_FAjiUzFOA8Cp-2P750C5Q6Pz_f9s-aPdahOnpVL4zlPloZfYDJcuAoYD2TRB4YjIGqpHN1_jaAZTGcgqKCSXJCVaoHLo6W_rgC-SNj54ZK19VVnomeZ3YzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ia9n264r1xSc1PsUNKY-Sas237ZMlx5S-1MtdxHoZCPQj0rC37NG3pyyJWPkpHrwEHTK7bNkyJ4j2LutCjgStEuWCt4wBpm0cYGq3k9j6zYl9hssSdmaXg_T0XPQHPhhigFFYd1svtO5fro2FVaUk5R-wfgHznRrdVjZdHCYSgdz-RQ6B9QmswlNtt0D3jM22XzkAFOXM9onSbQal_NBoeQcM8mWBibYKWMWu1e6VHWAbbk1ruu4loYnrGsgyFwZAgEeqPZxwwLJ5uHMLQc2EhWK1o87k_oDlNxzHYZ5f60R7jFIBAos6farQWVp_GBEYIOGJ5t5_CSktHrBwc2ytA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمایندگان ایران در فوتبال آسیا مشخص شدند
🔹
کنفدراسیون فوتبال آسیا به‌صورت رسمی جدول تیم‌های صعودکننده به لیگ نخبگان و قهرمانان فصل بعد را منتشر کرد.
🔹
نمایندگان ایران در لیگ نخبگان استقلال و تراکتور و در لیگ قهرمانان گل‌گهر سیرجان اعلام شده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/441098" target="_blank">📅 11:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441096">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SFnwUZS2lueo3KRLgslndOdZEZ6O3G45AmvgngvjPp2yijapAZCY3bsC-Pj5o4dARV0i6eM8SWJJdcnqKUeBHpINc3IH2vwr89o9Z-psCipF4TZyLjlMCOzQPGzClI7LmsTbe3RZwn8j-697294FXQgoRNIjvlEhwYbjXnWGXQFZtMoqQyCHufwfQQqhcPFGurnik_NbuU6WNnU7Wbb38yIXcU4UbwIRgZ-ggUzGLiz2ZdgYdpHMbUvvdDF3VWMpCyM9lNaVBSWs1BcF6iyuoYxUk36tUGauuTDdXVeSZJcMXUl-e1r2etUFVcDBexptpZuh-ObQTItG0PRX4VYjjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TwlX3YNL4My78wVVHdbbxS79PBfe_8O1_f-UIa3zbiXuPMYijhRV4AYogTADX6opIZw2Hf7rgHQE6sR_-eS1hBbYRA1NgpPapi3KLqpzB-yRP3eQLsbmUJOD6VcWlpOjUknUkCdXjCLVUBzuDqbssWygvlnVzK3JGV_cKiBANgtb__dm3rFwawpFjFN5PRB7ovh2Z8pS_6uQf9yWxPgNXoG1nr_FfBRcBiSJa6rSZSLQZzYXK0PrzenMX5utiqqV_t_UaqW29NZxMuVviaNkf3rmpdATIMOQiAXEy8XhSMXbSf7dyjyga2aUX6TE0d2ENqfBXMFhwt41o_EKtTVrTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هلیکوپتر آپاچی آمریکایی مایه تمسخر ترامپ شد
🔹
در پی گزارش سرنگونی یک هلیکوپتر آپاچی آمریکایی در نزدیکی تنگه هرمز، کاربران خارجی یک سوال اساسی پرسیدند و آن این که هلیکوپتر آمریکایی هزاران کیلومتر دورتر از مرزهای آمریکا چه کار می کند؟
🔹
بسیاری از کاربران با اشاره به ریتوئیت پست ترامپ درباره سرنگونی هلیکوپتر ارتش آمریکا در نزدیکی تنگه هرمز در صفحه رسمی کاخ سفید این سوال را مطرح کردند که اصلا چرا باید ارتش آمریکا در نزدیکی مرزهای ایران که هزاران کیلومتر دورتر از مرزهای ایالات متحده است،‌ حضور داشته باشد؟
🔗
اظهارات کاربران در این باره را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/441096" target="_blank">📅 11:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441095">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a856502fd2.mp4?token=SxoTUlTs2Gs74QQAuKt3WfcIgoFb2D3_TX9JVLc9rxyG4klPC8JHUx3Uh4ulvMLThFmJITvPDTOYS-OwII_njtHtau_5-VSLuHFXjazCGGdnu6Sg0D66s8ZmNZxkLvbE-T8AG-yFikvWONYzEJF38v6WCYJTBLLlkRhPsNRzuXZhT94yP8PNx5CKrhNderIooyvTOy7c-gP0SfxZdcNr28Mlc65JY1GOhIrCpZ-puH_T_mN1sp1LY4YRj57ZkjRtjB5oqnYG3-oA3I6YcxdUOsTRfxZSzTSYglqOxwHjrdSVRQ2ZRQnTOjs3Wn6iXsgjnYpdocuAuLGGOSc-rWOZiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a856502fd2.mp4?token=SxoTUlTs2Gs74QQAuKt3WfcIgoFb2D3_TX9JVLc9rxyG4klPC8JHUx3Uh4ulvMLThFmJITvPDTOYS-OwII_njtHtau_5-VSLuHFXjazCGGdnu6Sg0D66s8ZmNZxkLvbE-T8AG-yFikvWONYzEJF38v6WCYJTBLLlkRhPsNRzuXZhT94yP8PNx5CKrhNderIooyvTOy7c-gP0SfxZdcNr28Mlc65JY1GOhIrCpZ-puH_T_mN1sp1LY4YRj57ZkjRtjB5oqnYG3-oA3I6YcxdUOsTRfxZSzTSYglqOxwHjrdSVRQ2ZRQnTOjs3Wn6iXsgjnYpdocuAuLGGOSc-rWOZiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترخیص ۵۱ اتوبوس ضدآلایندگی از گمرک هرمزگان
🔹
رئیس‌ دادگستری هرمزگان: با پیگیری دستگاه قضایی، ۵۱ دستگاه اتوبوس ۱۸ متری مجهز به سامانه‌های ضدآلایندگی از گمرک ترخیص و به ناوگان حمل‌ونقل شهری کشور اضافه شد.
🔹
این اتوبوس‌ها با هدف کاهش آلودگی هوا و روان‌سازی ترافیک شهری وارد چرخۀ خدمت می‌شوند و ظرفیت جابه‌جایی مسافر در هر دستگاه معادل یک واگن قطار شهری است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/441095" target="_blank">📅 11:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441094">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: به‌دلیل انجام انفجارهای کنترل‌شده تا ساعت ۱۴ امروز، احتمال شنیدن صدای این انفجارها در صفه، بهارستان و اطراف آن وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/441094" target="_blank">📅 10:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441093">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35603f2115.mp4?token=dxEnDbEAiZJaJkH5rEqyUWVf6WL4RwsLcxLvTAQqkSQun_dKdvCc3AoZATeECwEnRQfdskUk5NRxsQLhHkxGhybL12KI1tDHktnXNhtu5fEzVdzTHh15QQ0rWoWI9J2EFRMrAkpQDPWjro05JXOQqKIvwuhgd1kXYVJbDgYOcN3d9vtqaeRKi9s0WlpIxM__wJj7Vv19-8Ba6xLpfylhZfgZOdV-95WmYAi124JZhofLqUFhwgXxqLdvhfH3IEyuQHB7wUwh3reiry1grio76OT2S1-e1DMZD50SNRnCv-O0wIWSEUI8By4RGqrtYWyTaKavXXcyksZx1Jo7YOE6KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35603f2115.mp4?token=dxEnDbEAiZJaJkH5rEqyUWVf6WL4RwsLcxLvTAQqkSQun_dKdvCc3AoZATeECwEnRQfdskUk5NRxsQLhHkxGhybL12KI1tDHktnXNhtu5fEzVdzTHh15QQ0rWoWI9J2EFRMrAkpQDPWjro05JXOQqKIvwuhgd1kXYVJbDgYOcN3d9vtqaeRKi9s0WlpIxM__wJj7Vv19-8Ba6xLpfylhZfgZOdV-95WmYAi124JZhofLqUFhwgXxqLdvhfH3IEyuQHB7wUwh3reiry1grio76OT2S1-e1DMZD50SNRnCv-O0wIWSEUI8By4RGqrtYWyTaKavXXcyksZx1Jo7YOE6KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در بندرعباس
🔹
دقایقی پیش صدای چندین انفجار شدید در بندرعباس شنیده شد. هنوز محل دقیق این انفجارها مشخص نیست.
🔹
همچنین ساعتی پیش، دو مخزن آب در بخش بمانی سیریک هدف قرار گرفت و تخریب شد.
🔸
در ساعات گذشته پدافند در مناطقی از بندرعباس و…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/441093" target="_blank">📅 10:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441092">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">توقیف اموال ۴۷ خائن به وطن در خراسان‌شمالی
🔹
رئیس‌کل دادگستری خراسان‌شمالی: تاکنون اموال ۴۷ خائن به وطن و افراد تأثیرگذار در شبکهٔ کمک به‌نفع دشمن، در خراسان‌شمالی شناسایی و توقیف شده است.
🔹
۴ نفر از متهمان مقیم آلمان، ۶ نفر مقیم انگلیس، ۲ نفر مقیم فرانسه، ۱۰ نفر مقیم ترکیه، ۵ نفر مقیم آمریکا، ۲ نفر مقیم کانادا، ۲ نفر مقیم ایتالیا، ۲ نفر مقیم استرالیا، ۲ نفر مقیم عمان و مابقی مقیم دانمارک، اسپانیا، قطر، امارات، چین، اسکاتلند، قبرس، یونان، نیوزیلند و کشورهای دیگر هستند که دستور‌های لازم در راستای توقیف اموال آن‌ها صادر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/441092" target="_blank">📅 10:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441091">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCcGxpDN316qA8qqcs3ylFNP4LCxv4LQFnOeUpjZaANjzlBhPHb8Rll9GaOwhLAr9fYupbl2H7WfoUk6d2t7FhojYNT6IjiOygSAlubEbW7W0jmIUpJERLDt5e9KH1JmavBqosGexRUl3FsJC_mfCXMb2Nnjhh1dG5BegC-pbmlbzK76J7CsVhEtcH2Wavgq3nETwevJvw8_tFmCTWDDpGXMTUieEuai2j3jqcAm2Upv2UHLqn3RIwx1Fcb-VThtGEswb41fsdcuWMMAXXYaS0n9IYR6hjeng-aR9xAv6khtnc2PrxJVmWdM60EzpGz_VbfeRLjWliL_UfpdAhU28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
اولین سالگرد شهادت شهید نصیرباغبان فرمانده اطلاعات نیروی قدس سپاه
🔹
پنجشنبه ۲۱ خرداد ساعت ۱۷ الی ۱۹ حرم حضرت عبدالعظیم (ع)
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/441091" target="_blank">📅 10:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441090">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تماس‌های خانگی رایگان شد
🔹
شرکت مخابرات همزمان با افزایش ۴۵ درصدی آبونمان تلفن ثابت، اعلام کرد مکالمات درون‌شهری و بین‌شهری به‌صورت ثابت به ثابت برای مشترکان خانگی از ابتدای خرداد رایگان محاسبه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/441090" target="_blank">📅 10:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441088">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎥
تصاویر شلیک موشک‌های سوخت جامد و مایع دوربرد قدر و عماد و خیبرشکن به‌سمت اهداف آمریکایی در منطقه  @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/441088" target="_blank">📅 10:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441087">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b52068ab5.mp4?token=Uag9Rgj8ROeB0-fqX3G_37E4uTU74Wg-hSqyIPquRXcrxA_vzik0IhqZuCN_yD_3PElrq9JWHhVBEl7Va6SHUPXYWXDiYdXYa4TLLo8N-KIsAHm6YnVgUHlkB12HsZ0W53TxPb90dRujKnbPHXUa53CzHfiwYjUjuT2RcPoAqsxMdzXod5v5EMzXDB91poGrzbUhwCj0bVUpcaFR1zz1U-XECI_57bQpshCDfguHIXsK8hpOseGOsNgGhoGW8qLzIzVxp2urMsbAmk82MSm7CT1HjXhzKEo2bJHrmpuYRJP-8QETqvwgyH_ZO-ntqLeHyBbL2YPQBFLoyD51o8-IJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b52068ab5.mp4?token=Uag9Rgj8ROeB0-fqX3G_37E4uTU74Wg-hSqyIPquRXcrxA_vzik0IhqZuCN_yD_3PElrq9JWHhVBEl7Va6SHUPXYWXDiYdXYa4TLLo8N-KIsAHm6YnVgUHlkB12HsZ0W53TxPb90dRujKnbPHXUa53CzHfiwYjUjuT2RcPoAqsxMdzXod5v5EMzXDB91poGrzbUhwCj0bVUpcaFR1zz1U-XECI_57bQpshCDfguHIXsK8hpOseGOsNgGhoGW8qLzIzVxp2urMsbAmk82MSm7CT1HjXhzKEo2bJHrmpuYRJP-8QETqvwgyH_ZO-ntqLeHyBbL2YPQBFLoyD51o8-IJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سگ‌های بمب‌یاب محافظ کاروان ایران شدند
🔹
سایت DifCorrupcion مکزیک: ارتش این کشور به‌دلیل تهدید احتمالی از سوی دولت آمریکا علیه کاروان فوتبال ایران برای پیشگیری از خراب‌کاری از سگ‌های بمب‌یاب استفاده کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/441087" target="_blank">📅 10:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441086">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfV87ahufGQ0SObuxNAeH6bmFzJRI2wxDz45v-YbqKvcWkSDzwz5te_Xa10kZx_nXFiIYxiDykXhC0vuWcKH72LnI8-clWtUAAk0s4LSCwtva1SF0rjIbYuonwruz7v3tbZHcn4KAhb3JESFSqkNwSNHf6CnW0j5j34kBrzYBGY_KUIzJeDu-DvRnGjdogMm6uM-aL1DRiHIm0eDFKKZ6FF3kp-5VJWyfMjy4ZHDQM3wb8Q83jnGqp_eHytzxWFLqO3__uHWSqqfM1n1UJgOQPKpvTNDCYkDMRPIeHyF3oxnG3DSY8sSKgFsY9jaBVsN8yUYGArPslxDsvcZdulZ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی کل سپاه: آفرین بر شما مداحان، شاعران و هنرمندان متعهد
🔹
۱۰۰ روز از درخشش بی‌نظیر ملت مؤمن و شجاع ایران می‌گذرد‌. بعثتی الهی که جهان را شگفت‌زده کرد و زورگویان مستکبر را در مقابل ارادۀ ملتی بصیر و مقاوم تسلیم کرد و ان‌شاءالله پاداش این ایستادگی بی‌مثال،…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/441086" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441085">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMqQ46t0gCSNmVsOGggIwVeYXsohFjJ9ufWJnVLrFhynkbor4Q_2SAMcj4CR4M_9FeOMb_MNI6_ZX-K0Uq0rvbc2Ybxc0cVKkPuVtVncfjpml1fjG4KBjEXuMGQQwjkZQqBcCJ0VXwenYTUvD61oOiEdARbET2ijfpNJpi8SbQuxxipFATbxVkc_X90c0vHQE-wQ_Pt7qZQmx3DJv5npUWfnnpRlXJyPHpYonIh5uzgR9Brg2WMNXEpF5voxkdrPaRjFrKERT8TaBmrslPd8hI9fKrcESyC2XTLovRUzdeVH4Uu_Z5WNj8eL_LjdgXk2Gez7AH1SH5M1b-m1RY3qeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حادثهٔ دریایی در نزدیکیِ باب‌المندب
🔹
سازمان عملیات دریایی انگلیس گزارش کرد که یک حادثه در ۸۸ مایلی جنوب غربی بلحاف یمن اتفاق افتاده است.
🔹
این سازمان گزارش کرده که «یک قایق با ۶ فرد مسلح به یک کشتی باری نزدیک شده و تبادل آتش بین قایق کوچک و کشتی‌های باری رخ داده است».
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/441085" target="_blank">📅 09:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441084">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پلیس آفریقای جنوبی: در پی تیراندازی افراد مسلح به یک سکونتگاه غیررسمی در شرق ژوهانسبورگ، دست‌کم ۱۲ نفر کشته و ۹ نفر دیگر زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/441084" target="_blank">📅 09:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441083">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
با تصمیم شورای معین شورای‌عالی انقلاب فرهنگی، تاثیر معدل پایهٔ یازدهم در کنکور امسال مثبت شد
🔹
همچنین شورای معین با کاهش تعداد دروس امتحانات نهایی پایۀ یازدهم به ۶ درس برای کنکور ۱۴۰۶ موافقت کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/441083" target="_blank">📅 09:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441082">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1at-aQusV56WwzuebISDAL-ymkkX1SaXmGOH8-WNWJHzAKWvzi6pDEypdZXoR2nAuFiSmB-8uYuLMbjmFirbpAsEmRpnHnbKLAVsgzQ7Kgba4n-MfA7umyGmmA0HcydfCzWgeegMwD9JwpJxSY3ZiUnnTLk9ydG6-jXx8ETX1U9EJKb4CgJd5cg5_FjwJ2qiHoLGe5sEAjTXekUIXGIh381-VdMfm8r02zuWvp1GFPRd3_V-HBleT576Eq5LIyn2tgtFoncYGjFbgX1kStms8vdbXztNqZpVInPsAf6raUtRctFC3ohIGD-5FkUMbqXZ11QU3jDwaITwIbTTpg_aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس رکورد جدید زد
🔹
شاخص کل بورس در دقایق ابتدایی معاملات امروز با رسیدن به ۴ میلیون و ۶۰۲ هزار واحد رکورد تاریخی جدیدی را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/441082" target="_blank">📅 09:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441081">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52f500d34d.mp4?token=dD5GXdCNuxUQHeoFJghXtpj74MEB1t0FeQo8wDNzcEqmX_b4zEkbT1nDnZcc7h-WZK03WMj6OZYJVZR7ODIhJDjtjdT-A9tUOqe5oB-ndsz4jQZALulgPlZ3mzS-FExIVjYmkMLgPGGsGp4g8QFkQjCxOc2ePRWFQXEqbr30uyNEpFQpqM_3YvejsHU23ZsgUTxsC_lmoEceTWYs5UFFmIcb0k-7p-Nvn5o2fcq7Pldo4CJp7mia4P-Y9vsqorBhLWU0964nCKLB7PuWPiP8Sp4WXYLAv2dLikwO05sP-6lIHeA5hPNDRYnof0ijy36qd5wpq9_wbPbxcFqYHEnBWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52f500d34d.mp4?token=dD5GXdCNuxUQHeoFJghXtpj74MEB1t0FeQo8wDNzcEqmX_b4zEkbT1nDnZcc7h-WZK03WMj6OZYJVZR7ODIhJDjtjdT-A9tUOqe5oB-ndsz4jQZALulgPlZ3mzS-FExIVjYmkMLgPGGsGp4g8QFkQjCxOc2ePRWFQXEqbr30uyNEpFQpqM_3YvejsHU23ZsgUTxsC_lmoEceTWYs5UFFmIcb0k-7p-Nvn5o2fcq7Pldo4CJp7mia4P-Y9vsqorBhLWU0964nCKLB7PuWPiP8Sp4WXYLAv2dLikwO05sP-6lIHeA5hPNDRYnof0ijy36qd5wpq9_wbPbxcFqYHEnBWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بانوان روستای پنداش کاشان با نصب پنل‌های خورشیدی به درآمدزایی رسیدند.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/441081" target="_blank">📅 09:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441080">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf04ab66a8.mp4?token=HNR1H22FmtgANVvfI8TPTsZ4Zez8mLjxH6tsZmR0siMHwUpT341zKIVzJoa7PU2YQjyEyYsQXSmRKi0C71UccWUJn-zLQVvruhDd50w52Ut65CPj8Q1KBygVZ-Ikfz4v6EyWLLD-K-TucIW9W-AFCxYOFilUSYIWtocvzP4HDiw0wAJl8ah_LRdfiRhASEdKmmWA-Jbr7P5ua6BZNM-cs2ABs8F9zb3RrAtlzD9AIKnEq6JqnZT2uA8KDduFymc8970-PIi-27GiuQ4LUXbfVYjZr_inKpc-k6EpqC2W2oh9CtSzLHQZLd83mc-BTXwUUOdrD7EgW03TVutYPLEofg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf04ab66a8.mp4?token=HNR1H22FmtgANVvfI8TPTsZ4Zez8mLjxH6tsZmR0siMHwUpT341zKIVzJoa7PU2YQjyEyYsQXSmRKi0C71UccWUJn-zLQVvruhDd50w52Ut65CPj8Q1KBygVZ-Ikfz4v6EyWLLD-K-TucIW9W-AFCxYOFilUSYIWtocvzP4HDiw0wAJl8ah_LRdfiRhASEdKmmWA-Jbr7P5ua6BZNM-cs2ABs8F9zb3RrAtlzD9AIKnEq6JqnZT2uA8KDduFymc8970-PIi-27GiuQ4LUXbfVYjZr_inKpc-k6EpqC2W2oh9CtSzLHQZLd83mc-BTXwUUOdrD7EgW03TVutYPLEofg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تگرگ در شمال، گردوخاک در شرق
🔹
هواشناسی: امروز و فردا در آذربایجان‌غربی و شرقی، اردبیل، گیلان، مازندران، گلستان، ارتفاعات البرز و شمال خراسان‌شمالی بارش باران پیش‌بینی می‌شود و در مناطق مستعد احتمال وقوع تگرگ نیز وجود دارد.
🔹
افزایش سرعت وزش باد در غرب، جنوب‌غرب، جنوب، شرق، شمال‌شرق و دامنه‌های جنوبی البرز طی ۲۴ ساعت آینده می‌تواند باعث خیزش گردوخاک و کاهش کیفیت هوا شود.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/441080" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441079">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LukE1ckRZqU8GCj-vjJ3sQd70Yh2gujS81vMYRF6cUxS1BNolBrdTEG3veSSSEYCKfTWjOEAhh5f0_vT7ssho3p9IKw4ald4hWcieZQj8inrCBVDk98ufjcjp9fR06BQVJW5GqHE852Grzyn1Y7qTYWjjW5NBlVjHr7AoPpSMwJbucfao0V3wcXgA_ErQ-pUWFZWaFxyMeswFjOYtm5a7VLWXRhFFWWoCjiAPnRtrqrYwG7k7Thn6HYq2_2R1KuaCCsDHDWBfAs6NDpTrgSwPuMPbVZyHy8RESqpIWWWfZab7lfpKdDly_tV_Bd0Lub_t2UNDeJlnBZopxPYAVDLZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفت‌وگوی عراقچی با همتایان ترکیه‌ای و عربستانی
🔹
فیدان و بن‌فرحان نیمه‌شب دیشب در تماس‌های تلفنی جداگانه با وزیر خارجهٔ کشورمان آخرین وضعیت تحولات منطقه‌ای متعاقب حملات تجاوزکارانهٔ آمریکا به مناطقی در جنوب ایران را بررسی کردند.
🔹
عراقچی در این تماس‌ها ضمن محکومیت تجاوز نظامی آمریکا و نقض حاکمیت ملی و تمامیت ارضی ایران، بر حق ذاتی دفاع مشروع برای پاسخ متقابل نیروهای مسلح مقتدر کشورمان تأکید کرد.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/441079" target="_blank">📅 08:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441078">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ff164d2d4.mp4?token=rIvBnFmKA59HOUaWIM00tqfcfUgEz6UjR6PaSIiGTFosIC70e3hz4R9izIXjQqnZViP8tdgyF7wl-igMqB0VOOlZ7onLnl1lRYPPewjicnNwJpJ_ovDFVQ3Ej0eU1LtlJkdpX9OdvOqTQpqi8-7wjQxe9n_n5vdKefwECzcUV8nlyrKShDVFNpCgY7fXj14uDUXrhT5efQRuubFX97aSh7oNIJ7A8Yzggq1F_MODF0KdSddM-Qb5I0zKB_CDuA5McN8SXKRh2FcNJo_9xmn1gHc7oNP9Q5Q1vW2P25c7L9C9o3xR_Bk5QjapDQE2lWOwbwqdrUqFOSlIn3xVlrJv7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ff164d2d4.mp4?token=rIvBnFmKA59HOUaWIM00tqfcfUgEz6UjR6PaSIiGTFosIC70e3hz4R9izIXjQqnZViP8tdgyF7wl-igMqB0VOOlZ7onLnl1lRYPPewjicnNwJpJ_ovDFVQ3Ej0eU1LtlJkdpX9OdvOqTQpqi8-7wjQxe9n_n5vdKefwECzcUV8nlyrKShDVFNpCgY7fXj14uDUXrhT5efQRuubFX97aSh7oNIJ7A8Yzggq1F_MODF0KdSddM-Qb5I0zKB_CDuA5McN8SXKRh2FcNJo_9xmn1gHc7oNP9Q5Q1vW2P25c7L9C9o3xR_Bk5QjapDQE2lWOwbwqdrUqFOSlIn3xVlrJv7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی پیش از اصابت موشک به اهداف آمریکایی در بحرین   @Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/441078" target="_blank">📅 08:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441077">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-9IW9Mta4wgxac4FreGfIeSquTT4tdSDgVqHvIk2uZpY0O8QmTnaaMVe53JHy0dDAR8DxyWHN7UPZMg7-vjTpGzJ2X8m322RL8l__l6BE3ABALUq6dWV1aOeTPesHe-P9nJ9QN2NyjWrAUB2UgfylLAzEL9LR0NwT5bWhDKRjvvYufd3fuB6u6u9pGmfqw7x0_1BKqnVUkvboGHzgR80mlYGG3fhW04U1zHItAHO9Rg4jCsUgqrNQt1lzcPaFG_B0oLmC6hLGGfSM3u9Me1zXQJedOoibRh1JckUlN5Vr_akvPTVHA9YmN2eWIWu7IkArz_kuYW-buzWfCXAFgaIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه: در حمله به مبدأ تجاوزات درنگ نخواهیم کرد
🔹
رژیم آمریکا در اولین دقایق بامداد چهارشنبه به بهانهٔ سقوط یک بالگرد ارتش تروریستی این کشور بر فراز تنگهٔ هرمز حملات وحشیانه‌ای را علیه مناطقی در جنوب کشور انجام داد که نقض فاحش منشور سازمان ملل و قاعدهٔ بنیادین «منع توسل به زور» در روابط بین‌الملل است و هیئت حاکمهٔ آمریکا با این اقدامات تجاوزکارانه بار دیگر ماهیت جنایتکارانه و جنگ‌طلب خود را نشان داد.
🔹
نیروهای مسلح مقتدر جمهوری اسلامی ایران در واکنش به تجاوز نظامی آمریکا به ایران و نقض آشکار حاکمیت ملی و تمامیت سرزمینی کشورمان، پایگاه‌ها و دارایی‌های آمریکا در منطقه که مبدأ این تجاوزها بود را هدف ضربهٔ شدید قرار دادند.
🔹
ما ضمن محکوم‌کردن شدید جنایت آمریکا در تجاوز نظامی علیه ایران، بار دیگر مسئولیت قانونی و اخلاقی همهٔ کشورهای منطقه، به‌ویژه کشورهای حاشیهٔ جنوبی خلیج فارس، برای ممانعت از هرگونه استفاده ارتش تروریستی آمریکا و رژیم صهیونیستی از قلمرو و امکانات آنها جهت طراحی، سازماندهی، اجرا و پشتیبانی از اقدامات تجاوزکارانه علیه ایران را یادآوری می‌کنیم و هشدار می‌دهیم که ایران در اعمال حق ذاتی دفاع از خود، از جمله از طریق هدف‌قراردادن مبدأ حملات و پایگاه‌ها و امکانات لجستیک مورد استفاده برای عملیات‌های تجاوزکارانه علیه ایران، درنگ نخواهد کرد.
🔹
ما همچنین بار دیگر مسئولیت سازمان ملل، خصوصاً شورای امنیت این سازمان و دبیرکل را برای صیانت از صلح و امنیت بین‌المللی و پاسخگوکردن طرف‌های متجاوز خاطرنشان می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/441077" target="_blank">📅 08:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441075">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358fade751.mp4?token=JYENn0n8bj95MAX97DHr8zcVNlCmTugDxsdaZQTXuKDRiJQBzAWDCuKnBhE1i7QWWq2uFzgNKC_z55IRgi_OXgITnMoPPp5Wl9LY6hkQEqUkRQ63uK0BGptCzmK9jnkftTrquyNeQCihO3xrYVccgClwYJgn8w0ewk762KvHZG1QHPx66iDP8kQMQ5Jzh4BV5Ljj9pQsG5FMY8kmS5hUOPhrQupvlVIlF0EhC-WFc8LLVfbFXL3WvaRrEwCAWqqX9XqbQWbkWTKaQOkLd3fPZ4rJ7wJAx4a7ZqjF5_F8HY32QbAmi-P-HQVhiYtxxPhOK4kGiOqmsjBj6GHrYsrwCYH7XuTnQpvatUF3aodEkEthRINQJlVxs7y1wR4K55Vxq-KFtmn83ihlEh9f1Q7g0_6shhm13A1UOx5H4ONcB3HragCWFTQmKOyRfle5aaq_c-A5UTWcy6FGAagy8owW34m8qJJFLzx9JcRt-Mga_-r1HeleyN4d0zKVPeXLqdMHUSqbd_5yhpMVzZKi20TZaXQMeFxK2meHDTMmN88xrRX0H6GsV3132JjnOZhZRECMmU65pm653frMHVTVDI5EKB9QNT3VfljEQlS6nfKpTc6PQdCKto3r4W0UesPtCPyCv3Mc9xteWmGWYyFQw5ktrQ_HvRpbVPSEVtU2QkIaN_o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358fade751.mp4?token=JYENn0n8bj95MAX97DHr8zcVNlCmTugDxsdaZQTXuKDRiJQBzAWDCuKnBhE1i7QWWq2uFzgNKC_z55IRgi_OXgITnMoPPp5Wl9LY6hkQEqUkRQ63uK0BGptCzmK9jnkftTrquyNeQCihO3xrYVccgClwYJgn8w0ewk762KvHZG1QHPx66iDP8kQMQ5Jzh4BV5Ljj9pQsG5FMY8kmS5hUOPhrQupvlVIlF0EhC-WFc8LLVfbFXL3WvaRrEwCAWqqX9XqbQWbkWTKaQOkLd3fPZ4rJ7wJAx4a7ZqjF5_F8HY32QbAmi-P-HQVhiYtxxPhOK4kGiOqmsjBj6GHrYsrwCYH7XuTnQpvatUF3aodEkEthRINQJlVxs7y1wR4K55Vxq-KFtmn83ihlEh9f1Q7g0_6shhm13A1UOx5H4ONcB3HragCWFTQmKOyRfle5aaq_c-A5UTWcy6FGAagy8owW34m8qJJFLzx9JcRt-Mga_-r1HeleyN4d0zKVPeXLqdMHUSqbd_5yhpMVzZKi20TZaXQMeFxK2meHDTMmN88xrRX0H6GsV3132JjnOZhZRECMmU65pm653frMHVTVDI5EKB9QNT3VfljEQlS6nfKpTc6PQdCKto3r4W0UesPtCPyCv3Mc9xteWmGWYyFQw5ktrQ_HvRpbVPSEVtU2QkIaN_o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجرای «محمد غلوم» مداح سلب‌تابعیت شدۀ بحرینی در اجتماع دیشب میدان انقلاب تهران
🔸
دولت بحرین اخیرا تعداد قابل‌توجهی از شهروندان این کشور را به بهانۀ حمایت و ابراز همدردی با مردم ایران سلب‌تابعیت کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/441075" target="_blank">📅 07:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441074">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">طالبان: ۱۳ نفر در حمله هوایی پاکستان به افغانستان کشته شدند
🔹
سخنگوی طالبان افغانستان: در پی حملات هوایی ارتش پاکستان به سه ولایت افغانستان، دست‌کم ۱۳ نفر کشته و ۱۴ نفر زخمی شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/441074" target="_blank">📅 07:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441073">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🎥
لحظاتی پیش از اصابت موشک به اهداف آمریکایی در بحرین   @Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/441073" target="_blank">📅 07:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441072">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsJ9DbCc1PLW6Fb25Z70QCcKb8ksJMcldG5Gkk_tI8RYojq9dr4btwFYkS_PzCQNaSW6n2e0nrheH2-7fLJohnZZeOi1EEpPwY9xLilj2WaVSJHZW-vGneSCnMbu3ufzLhDFyva_Dn6HFFx1oFWXPnPvFzg1Dd2o2RqQzauO-H1D1A5OB9r2lckwkj0o9CQsa8xxXGyXeD1V3w73pv4UDa0IhdofLy5ZcT5hyER6YcLqfT-b33icupFsNVME8Taw743n0nMHq9J8VdJMyZ9OhchV6_i0KtQ0hcYSx1L9INLpKipthRoUEAF4Szg52r-SP-KVhyim4jRZzJFmuFlm6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتبار کالابرگ سرپرستان خانوار دارای رقم پایانی کد ملی ۳، ۴، ۵ و ۶ شارژ شد.
@Farsna</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/441072" target="_blank">📅 06:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441071">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/667c81d9ef.mp4?token=ZRxYgZetpCc174LohoPsJJyE9pPHldrK2kJS4AxZhsQDqkXuG7gg8olpf21vvnaeBmQlvWLDlx0tUzXgNS7gQ9hbL8F-0OH-DUmMf5JOqNLqA24qMw0g88M9y4lFv_9WdXbVPHsFLSVYnBJDX5LWbX1qXTheCFL35F2NiLY6UHvjuw8HeP8UTbgRkSPjtOheE-k55qNz5w0BtuKFvcFRAyMCM8mYa1b2P66TIijS4t3vn3hXDkWiqSEgcOBanrhonXq32Q7COiT6RMH7pHCqSdzaXnBZVKwyDuBCSxroUK5qStkMuwVHDfa5yV5fb4Xd1IXqsFC3DFk7E6lnKX_JwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/667c81d9ef.mp4?token=ZRxYgZetpCc174LohoPsJJyE9pPHldrK2kJS4AxZhsQDqkXuG7gg8olpf21vvnaeBmQlvWLDlx0tUzXgNS7gQ9hbL8F-0OH-DUmMf5JOqNLqA24qMw0g88M9y4lFv_9WdXbVPHsFLSVYnBJDX5LWbX1qXTheCFL35F2NiLY6UHvjuw8HeP8UTbgRkSPjtOheE-k55qNz5w0BtuKFvcFRAyMCM8mYa1b2P66TIijS4t3vn3hXDkWiqSEgcOBanrhonXq32Q7COiT6RMH7pHCqSdzaXnBZVKwyDuBCSxroUK5qStkMuwVHDfa5yV5fb4Xd1IXqsFC3DFk7E6lnKX_JwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ویدیوی منتشرشده در منابع عربی از اصابت به پایگاه آمریکا در بحرین  @Farsna</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farsna/441071" target="_blank">📅 06:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441070">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
منابع خبری از حملات هوایی رژیم صهیونیستی به شهرک‌های النبطیه‌الفوقا، حبوش و کفررمان در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/441070" target="_blank">📅 06:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441069">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9e8f3330.mp4?token=uiSFhoEoSmsa4QMHGBfQC_4VDmBX4i56GpBdzhk0n_ExpQGlF5wQQw-_WBtkr3PyfCqPnhwvuV0Qf3EfvMm4C1IGf2vX59-4PQMGaQ_szrMg56_2Fqsx_CG4J_fCokwu_wtcvnfl--fMsluHpz1vh6ZwVKfiZMrnaGAcYRlf5YADmlAkaHkkc7GPxUw7gCfHNrlUJfBfG18cJRk84MnqCtWFuKpr_nEJdG44c7fX1e2wZzt7NstgAXsmssgeXkHpJfU5lshfJzLK5p1BpWqxKtkiC08n1s7u-nA-fPRq0pZht3m_sPl3XL6LnoZEH6W5nwFtgW0MozsRA1oNHLZElw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9e8f3330.mp4?token=uiSFhoEoSmsa4QMHGBfQC_4VDmBX4i56GpBdzhk0n_ExpQGlF5wQQw-_WBtkr3PyfCqPnhwvuV0Qf3EfvMm4C1IGf2vX59-4PQMGaQ_szrMg56_2Fqsx_CG4J_fCokwu_wtcvnfl--fMsluHpz1vh6ZwVKfiZMrnaGAcYRlf5YADmlAkaHkkc7GPxUw7gCfHNrlUJfBfG18cJRk84MnqCtWFuKpr_nEJdG44c7fX1e2wZzt7NstgAXsmssgeXkHpJfU5lshfJzLK5p1BpWqxKtkiC08n1s7u-nA-fPRq0pZht3m_sPl3XL6LnoZEH6W5nwFtgW0MozsRA1oNHLZElw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
وقوع انفجارهای جدید در کویت و بحرین
🔹
به گفتۀ منابع محلی، پایگاه‌های آمریکا در بحرین و کویت بار دیگر هدف حملۀ هوایی قرار گرفته‌اند. @Farsna</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/441069" target="_blank">📅 06:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441068">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
وقوع انفجارهای جدید در کویت و بحرین
🔹
به گفتۀ منابع محلی، پایگاه‌های آمریکا در بحرین و کویت بار دیگر هدف حملۀ هوایی قرار گرفته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/441068" target="_blank">📅 06:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441067">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🎥
آسمان اردن پس از حملۀ موشکی ایران به پایگاه هوایی «موفق‌السلطی» و تلاش‌های ناموفق آمریکا برای رهگیری موشک‌ها
@Farsna</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/441067" target="_blank">📅 06:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441066">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: ۴ هدف مهم از جمله آشیانه‌های جنگنده های F35 در پایگاه هوایی و مرکز فرماندهی کنترل ارتش کودک‌کش آمریکا در الازرق اردن مورد هدف قرار گرفت و منهدم شد.  @Farsna</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/441066" target="_blank">📅 05:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441065">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: ۴ هدف مهم از جمله آشیانه‌های جنگنده های F35 در پایگاه هوایی و مرکز فرماندهی کنترل ارتش کودک‌کش آمریکا در الازرق اردن مورد هدف قرار گرفت و منهدم شد.  @Farsna</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farsna/441065" target="_blank">📅 05:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441064">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
سپاه پاسداران دقایقی قبل پایگاه آمریکایی الازرق در اردن را هدف حملۀ موشکی قرار داد.  @Farsna</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/441064" target="_blank">📅 05:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441063">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
سپاه پاسداران دقایقی قبل پایگاه آمریکایی الازرق در اردن را هدف حملۀ موشکی قرار داد.  @Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/441063" target="_blank">📅 05:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441062">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0ef1e3afd.mp4?token=WaekKBgrmElh80WBxUEjK9B4PZYKC4j2ve960A_-LXW2-axk0TToE-UsZE_xLUwOeGkm45GlQK2LNJuFOFHPpM1-CoDdu8Mk-eQ1FRMQw4hMPy3SrphTNvot2ftQ5vVjUKkGbGYTYQDoYNurr_Se4daLwciiTIv8qhkzV1NJnwDdyFB1HuOCaHKCX8Hx0R85Xd84gX_yASsyW-bcrvXER79vvlQVrnFy1fG4FqOlLazTFqPXfJ96c5DOR3ErKMEukD7Zo7QBc3srk2_0KFktGDLDyyE4Zf7zuH7zmwSWNBPWFBxMEYzQkPUroIbcqntQHRqOa0I0oEcJiB49QStQoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0ef1e3afd.mp4?token=WaekKBgrmElh80WBxUEjK9B4PZYKC4j2ve960A_-LXW2-axk0TToE-UsZE_xLUwOeGkm45GlQK2LNJuFOFHPpM1-CoDdu8Mk-eQ1FRMQw4hMPy3SrphTNvot2ftQ5vVjUKkGbGYTYQDoYNurr_Se4daLwciiTIv8qhkzV1NJnwDdyFB1HuOCaHKCX8Hx0R85Xd84gX_yASsyW-bcrvXER79vvlQVrnFy1fG4FqOlLazTFqPXfJ96c5DOR3ErKMEukD7Zo7QBc3srk2_0KFktGDLDyyE4Zf7zuH7zmwSWNBPWFBxMEYzQkPUroIbcqntQHRqOa0I0oEcJiB49QStQoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه: ناوگان پنجم دریایی آمریکا در بحرین هدف حملۀ پهپادی قرار گرفت</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/441062" target="_blank">📅 05:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441060">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
سپاه پاسداران دقایقی قبل پایگاه آمریکایی الازرق در اردن را هدف حملۀ موشکی قرار داد
.
@Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/441060" target="_blank">📅 05:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441059">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
آژیرهای خطر در بحرین فعال شد
🔹
منابع عربی از فعال‌شدن آژیرهای هشدار در بحرین، در پی واکنش موشکی ایران به نقض آتش‌بس توسط آمریکا خبر دادند. @Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/441059" target="_blank">📅 05:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441058">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
آژیرهای خطر در بحرین فعال شد
🔹
منابع عربی از فعال‌شدن آژیرهای هشدار در بحرین، در پی واکنش موشکی ایران به نقض آتش‌بس توسط آمریکا خبر دادند. @Farsna</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/441058" target="_blank">📅 05:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441057">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
آژیرهای خطر در بحرین فعال شد
🔹
منابع عربی از فعال‌شدن آژیرهای هشدار در بحرین، در پی واکنش موشکی ایران به نقض آتش‌بس توسط آمریکا خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/441057" target="_blank">📅 05:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441056">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
حملات پهپادی ارتش به پایگاه‌های آمریکا در منطقه
🔹
روابط‌عمومی ارتش: در ادامۀ عملیات مقابله با شرارت‌ها و مزاحمت‌های ارتش تروریستی آمریکا برای ساکنان جنوب کشور، بامداد امروز، ارتش جمهوری اسلامی ایران در اقدامی متقابل، با موجی از حملات پهپادی، پایگاه‌های آمریکایی و سامانه‌های راداری ناوگان پنجم ایالات متحده را در بحرین آماج حملات خود قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/441056" target="_blank">📅 05:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441055">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
پایگاه‌های آمریکا در منطقه مورد حملۀ مشترک ارتش و سپاه قرار گرفت
🔹
قرارگاه مرکزی حضرت خاتم الانبیا(ص): در پاسخ به تجاوز ارتش تروریست آمریکا در مناطقی از جنوب کشور به بهانۀ واهی سقوط بالگرد خود، برخی از پایگاه‌های آمریکا در منطقه هدف هجوم قدرتمند ارتش قهرمان جمهوری اسلامی و دلاورمردان سپاه پاسداران انقلاب اسلامی قرار گرفت
🔹
ارتش جنایتکار آمریکا بداند در صورت تکرار تعرض به جمهوری اسلامی ایران، حملات سهمگین و گسترده تر علیه بانک اهداف تعیین شده در منطقه انجام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/441055" target="_blank">📅 04:47 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
