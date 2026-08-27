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
<img src="https://cdn5.telesco.pe/file/LjwAqdJpD-VU8n7OPa7mlcD0QwIeaBwHB0IjWjKZCsDHbzNbEu_K4CrTJEjcAJo7AsvzpUh9dm8qxdG-gToMSxYMg2F8ZeEUQMHUsWRUt3k_7Bov4aIkRCEor0euJ04_q2ewuwskDBrTpYeiQuNwsAeEzJF4rNg9ymkuArw6UcQuKI1sPPmF0u1dpIGmWyWWxUSn7SLDM8elQSGae8iC3qLkbVjlblQH5yiMot0tstTn0pvieItc98um3UUN9pVByULKkwKBLlPt11-xnZ03gmZxHOQIyDmGtpw-XzomcKTHthc54qlYhxsmzDdJFJ8FLPwfiQqwapBvIt0eXfJeYQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 442K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-05 09:25:37</div>
<hr>

<div class="tg-post" id="msg-104760">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47cd3fb6e5.mp4?token=jz9QzQ1IH_sB-h51uVSyEyHxGAJDVvxA5wAp2ECUqhBq4UblQJWVtpQc5PwwO20J9J37wrWxGjgxOMLKJ1wPryh_qxysdxT7hN_uFwBtKVKv1ckRU_s1DQs_I56H2fkoon_Sd9CIABec7kUPKz6uFMGc2AGVa1gbRBZXd8SpA41F0yx_yHx2w39t3dFTIRYXdWQDfyMjSP-pXofrEiUO7Exbkfo7HGsa1SNzPt62VtK5fdo9MOAw-ynLHO2nHY3q5-OqbUHRZEvf891EHOBFO9slsVol08yWEEOfAajwJofjo072CjbJXnLQqaXIvYikeCGt77qS1_HlXhJtXlKKUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47cd3fb6e5.mp4?token=jz9QzQ1IH_sB-h51uVSyEyHxGAJDVvxA5wAp2ECUqhBq4UblQJWVtpQc5PwwO20J9J37wrWxGjgxOMLKJ1wPryh_qxysdxT7hN_uFwBtKVKv1ckRU_s1DQs_I56H2fkoon_Sd9CIABec7kUPKz6uFMGc2AGVa1gbRBZXd8SpA41F0yx_yHx2w39t3dFTIRYXdWQDfyMjSP-pXofrEiUO7Exbkfo7HGsa1SNzPt62VtK5fdo9MOAw-ynLHO2nHY3q5-OqbUHRZEvf891EHOBFO9slsVol08yWEEOfAajwJofjo072CjbJXnLQqaXIvYikeCGt77qS1_HlXhJtXlKKUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عشق‌به خدمت مثل هدایت‌ممبینی دلقک!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 339 · <a href="https://t.me/Futball180TV/104760" target="_blank">📅 09:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104759">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LakkwyUkiBODt9TsNZO9HauxLP69WNQ5og6ENvpUnXi7OQk2MzM_0fjAha4ARFpRzQidZ8Kld65_TVhJQEWrncrLGYunOJsdf3fOyR_IjE62st_gF53GJuPSqM3oqwUMyyP2OUhqx01zJfIHCH_2PNaPgZhwTmC4qPPe7BZWCbUeabnXTkKaMNx6OUHJWk6V9QDm8VCYkehXQruGq9s61PWlSxi-lW-fOeRJ2rGKoqBkCtHeixKcrImr440r_D2VNO5fAmibFPRrLHYHi3yGzQPDb8ZAWT1twZtP5v1zz7EJ2rNKnWAk76PkVeI4l8q1QSZz9kg5Yux2EIPXW63K-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👀
تمامی فروش‌های سیتیزن‌ها در نقل‌وانتقالات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/Futball180TV/104759" target="_blank">📅 09:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104758">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJOB0DUtTmXqjAkpVQ0_sIas26F_qK6x4d9FDhbmA0Tr3VavKg0S1Px6LK7Bisgp5t9oYclRE8608wag2d_qrd_VBh0CMM8Gqjdlv2lewA5xbU5MeFVnqcDADlFOQg2ciKldKsDKMiLfbH4C0BU1ZpyxtgZRDWY7mrzz7VDyk78YyzATDi-KZp1BorbxPrHkntl6n4DUOiv541qVQb8lbIzoXFwz6qNrIP5dId8Z3vydlmbVGXPYYLEF7EvQj7M8BIQtZorsFaTF7l-8B3sa-r8wwpF-TNOJ0HPomxh3ucj1v8vWR__YY0CTposSxeMxjB-7ncxp6owvUOE4WtcZ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رسانه Tala Radio ( نزدیک به اتلتیکو ):
⚽️
روایت اتلتیکو اینه که در ماه مارچ به خولیان گفتن حاضرن دستمزدش رو بالا ببرن و جزو پردرآمدترین‌های تیمش کنن. در عین حال، اگر می‌خواست جدا بشه، باید تا ۲۰ ژوئن پیشنهاد نقدی ۱۵۰ میلیون یورویی می‌آورد.
❓
اما چرا ۲۰ ژوئن؟ چون سال جام جهانی بود و ارزش بازیکنان افزایش پیدا می‌کرد. اگر قرار بود اتلتیکو دیگه روی خولیان حساب نکنه، باید پول و برنامه لازم برای مشخص کردن خریدهای بعدی را در اختیار می‌داشت.
❌
هیچ پیشنهادی با این مبلغ نرسید و بعدا بارسلونا با پیشنهاد ۹۰ میلیون + ۱۰ میلیون یورو پاداش وارد شد که قرار بود طی ۶ قسط در ۶ سال پرداخت بشه.
❗️
اتلتیکو معتقده خولیان توسط ایجنتش و بارسلونا تحت تاثیر قرار گرفته و ازش سوءاستفاده شده؛ برای همین می‌خواد با تمام قدرت جلوی انتقالش به بارسلونا رو بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/104758" target="_blank">📅 02:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104757">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFSS8DMlr1vL4C6FYthngrRWiP63nQHxnEy76wqG6X6fopI7qKLq8qMRHewu86DqVvp4XDzyP0d19Qw3SvkmjdhRuCh3SEMDAyheUHkyqUxLPUE1KudiAxUVhIzlg54JthjAOHwJwlBNqt49qMK7dfgwus8kYZ1FJRmelDfQMiP0_3JXrLzv-2hbLocrsf40-lv0xhqmTjFRPmYNUYoIZgZLe8sSKZdJqd6u-K4KbEepB2PbPSJZjGGLZXNAk8tmr29Nv04yXM5Dk5BoLMdsjFNnQ1e0t2dYR5pUMd471wLe11NsDupObhOmOeUPJoNwLmlwibwhBt3pAdfL78OhXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📅
در چنین روزی سال 2021
🏴󠁧󠁢󠁥󠁮󠁧󠁿
باشگاه منچستر یونایتد اعلام کرد که با کریستیانو رونالدو، اسطوره پرتغالی، از باشگاه یوونتوس قرارداد امضا کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/104757" target="_blank">📅 02:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104755">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cy3APomPMg_PmQRy99UQoGxXG0mKJewR1Z74lX_9_njxYVgG9aqjf3VN16Q0rINwLCboyomAqwb1T0FH_q31636JRYQWEiYcgr5663-KH8pZzhjAG-7zFZiA63F3ks_upfGTRE7r0H5eiYE_KYN6kuUd9aYixb02O64XVDA-WXTq4s8LbrGslvu-Pd0GR40y8PLFEgPSe9LafM4_12L6gjE6FMhEsmHSHH10CzRDGmWDiVufuKG9iJVXfFKWyClLTbTr_ktdeYdxdhH7ZFQW5hhonRnLGHiqJSjyqsA1oXROCEBX5VcBPMltTv6HjftRR3ZAmtZDFjfQdNQCN_jE9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
🇮🇹
#فوووووری
از یاگیز خبرنگار ترکیه‌ای: باشگاه گالاتاسرای با میلان بر سر جذب رافائل لیائو‌ با رقم ۴۵ میلیون یورو به توافق نهایی رسید
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/104755" target="_blank">📅 01:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104754">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/secgCudmMUS0sukP9g-1vynmSwj_mtro3tjR0doJm4GytR8z-BONccC1JtbjZ5uOHSGDmqw8w4hIhBE60kZZQr8ycaqbI2cQ9mqIIU5TLyI8Da6m9VKr797wfYCc73qh4ecLZrxmG1dJO-aE4lFcQZE8GDUuLJgy0U-ZAXeb_f1ZfCxoP2VyQX3sfP-iobC9tdZs4wjTyzaKrMMdPpa4Lbh--ZYD3vttzM6zcVkjMglK0ACgt07JAQb_jnvYx5aTdq6HlqoYM6lBCOUIDgY7_3SW1tKszTlgb-MuSLFbe-ETpXTe94HVW-e9tAV-XEcYCKQlVZ7G-3uJ9scvdRlqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
#فوووووری
و
#رسمیییییی
✔️
سیدبندی فصل‌آینده لیگ‌قهرمانان اروپا تکمیل شد. قرعه‌کشی امشب ساعت ۲۱ برگزار میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104754" target="_blank">📅 01:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104753">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVhHZa0bbgQKa2dGX740YTYCHdmE1dOelucfl8q7wstThco154v7ekzcLGDxprO0GPAL-emfwv2UWHCXOYSEKYQCtbuoV5hmcFhk-oB0k0KkmfRiJtYMH4VXYvvsNI6xtGFudl06CS89PNVbYp4pLjpxZVgkzbPVsKjNDatM4w4vY8Yl9wbV007YuY4rT6i0KrfUNYKTTwu3boKq2QPeWDchM94pmQmBf8l037ckc6h2loIbh9IUPLciI1dgf600Ui5uNc-ULhf6KeIR4Td7tgewbRb2TF9fvXZSTzd80ENL_IagX8KVl-hDvVGLmU26tA_TUpF-2-xSUREOLB1ECQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇹🇷
🇫🇷
فنرباغچه تو فرانسه تونست جلو لیون برنده بشه و مجوز حضور در UCL رو بگیره. حالا وضعیت دعواهای بعد بازی رو ببینید
😐
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/104753" target="_blank">📅 00:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104752">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogi6h5pASooi8B_9QVNioQBMBde8YQCR7XWEXytktfZrDQplE3aRoJk3O088JyeWFnbQkh3OY67Nn-m1anTJCtuG38s44aZ4Od2Uwdkl7oxUXGFKSvk9CYNCJwa289eFQ55EiBpuPErfoJh538vW3KhsthAWtK5q7CHqBjfFEgBOLQHyQQUD1YGGHbWkObWWZj02Bob6OpGGJY4mT4h779miYJB3rNFvKXkMNP6ZznpbUnIjVoBUeT24FNAYpHsssSVn8wp0yWMQdg9F0ZLSUgpbOzvEOd5W1GwDX9I7dCIwaB4C1ujdoFYHWiqkqetcQHhSIbsGrXWFRGN-k16AJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نتایج دور سوم قرعه‌کشی کارابائو کاپ (جام‌اتحادیه) انگلیس؛ تیم‌های سمت چپ میزبانن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/104752" target="_blank">📅 00:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104751">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a74ce22999.mp4?token=lIvY7xGefs-mcUymnWmUIFzoFP0FBvmpCfrrFcZX8Pu4XFdjSbgBOAUcSv_DGurhKhx1KNngf1L9_lTg2deMEGQLd-Hyap7CARpCzs9X9n7MQisQw8D47hCmgoAL6ygENq3o0195I8XzFV9pH6ptjclXfXC2iICDxLpmeDav_4BAXCIWzTUA9me4IoAtQgt6qeQvMrhbzS-sH8POThOVdQbU_yWd_aC7pQf3IOBHeS9sQNVv_ZHIrmKdBdoVSiMmkvRcrY92lQccSjLpH9dDwf4ipPst7LfbcxaMcTraB8CM_SQqVq2meyUcsmg9BnLU3_u0cBLSmX4WPm4-bciKMym07oJfMqAL0ierRfOFfCvBv1zGKT5p2uXjoIFhVGPT2G0V-txWZNd9Dqu_vs10rwa9UpHGDoS8La28Ji9vFA5JwIhMsJgJKTnAoAGQGfM61WDgWoqjL-WrFOADKnAEq_9WWGB0L5ZL7e1X0GJDjHJUiTomfUl7KjsoKnszsY7_1uaoDz68b4KJZ-CneurbDkpB6UCcoz2w3WCdxuom067CeKOCvYd0H6G0w0KsxUGbpCILRobxa5BiAUsC9Zrg2gTf8bRYz5bPr3lHgK3taPT0UHwiwL2Qg_TNScxu6PWbut5GStVJNxaRATBRftNhY2oNeExuqg8itBKOhuDdJYU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a74ce22999.mp4?token=lIvY7xGefs-mcUymnWmUIFzoFP0FBvmpCfrrFcZX8Pu4XFdjSbgBOAUcSv_DGurhKhx1KNngf1L9_lTg2deMEGQLd-Hyap7CARpCzs9X9n7MQisQw8D47hCmgoAL6ygENq3o0195I8XzFV9pH6ptjclXfXC2iICDxLpmeDav_4BAXCIWzTUA9me4IoAtQgt6qeQvMrhbzS-sH8POThOVdQbU_yWd_aC7pQf3IOBHeS9sQNVv_ZHIrmKdBdoVSiMmkvRcrY92lQccSjLpH9dDwf4ipPst7LfbcxaMcTraB8CM_SQqVq2meyUcsmg9BnLU3_u0cBLSmX4WPm4-bciKMym07oJfMqAL0ierRfOFfCvBv1zGKT5p2uXjoIFhVGPT2G0V-txWZNd9Dqu_vs10rwa9UpHGDoS8La28Ji9vFA5JwIhMsJgJKTnAoAGQGfM61WDgWoqjL-WrFOADKnAEq_9WWGB0L5ZL7e1X0GJDjHJUiTomfUl7KjsoKnszsY7_1uaoDz68b4KJZ-CneurbDkpB6UCcoz2w3WCdxuom067CeKOCvYd0H6G0w0KsxUGbpCILRobxa5BiAUsC9Zrg2gTf8bRYz5bPr3lHgK3taPT0UHwiwL2Qg_TNScxu6PWbut5GStVJNxaRATBRftNhY2oNeExuqg8itBKOhuDdJYU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇹🇷
🇫🇷
فنرباغچه تو فرانسه تونست جلو لیون برنده بشه و مجوز حضور در UCL رو بگیره. حالا وضعیت دعواهای بعد بازی رو ببینید
😐
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/104751" target="_blank">📅 00:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104750">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALRnSRGFG01uGJBzplchPn7aRqU5z6dKIx3gy7BytfYjXqhyitw4SabxvEOT-NMJR0qoutNMLKWvQI3v0m9JpBSLLb_t8_wIp9M7IKY7cywwyD4Mg0YHGpf_Yo9-4xb9sRDJODSZ9f7kADvSxusqiloO3-BrTHxtmooclWYKhoM3C5Ry9WtXx5DkNKgmA3MGnRv50Fz84w7fOLcBcJBZg1802Zk6F_3PmPbrTBy79VXeZhobpi-41Jp3qZ-1qYGAj_KZ3NGo7qXlTwXYJ1d-tvYShB1BcwvoQaTqoLU8twdwoVYmqNw-DzvO8LZdLaUM1e2g2UeCHxQXjmjxUTRQmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
🥶
🥶
🇪🇸
اروپا خایه‌کن که صاحبش داره میاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/104750" target="_blank">📅 00:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104749">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2024k42XRgXUpqkxykb-vlxVuaZ4tQvxyQ-4_pxBitEUZjRthhpJjU-OOpL-8mSmRYIsPo2SdJ2bgJ0ILgpx4vRF0vPm9PQO-wOz4tNVuAl6uqT8lozEjMs36uuRwKR9BosffXHmk5LOg-DPWXT6Ka47JHkrILP7BBih9WWRJ23CPeOLyoYXS65KW8FdQndTVdT2n5g07sY621wrivjOgqoPGEkcuQqrWmjU-nUJSmDjDDc96N6cTXLlW9CSw9GFLHESR3MkfeJdoR8UuxX3Y_eW0AbLfI0CcCP38F2QilAMaKFuogty1h4p-5FGcp7xk9UyYdXjxTftGneyyp6EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🐐
📊
🇪🇸
عملکرد امباپه در رئال‌مادرید:
🏟️
[105] بازی.
⚽️
[89] گل
🔴
[12] پاس‌گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/104749" target="_blank">📅 00:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104748">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YD4ce4JGLN8ESTicv48HufKVNG6siGmFDWfhuD-qDIbm7hlNckCfSW0FSwHPpwyGIJ7BTXJXlqTlM4KNa4tsGeaRP4L4rFlYHczHiLPaTe_UnIRQy8R4uZCGut5pBmxjbYyEQJf_n5B7oQPm-AlFlTZHPhzAKbu5HMcC_JrxOglC4iUr_782JapiCLMD2G8CmdNSEBXj08Og6HBCpSRnMBoQKT-Plc9s5Tay-jBdr7PLbxEWmYVvEtGA_g5BVF7Lx7VoH3AfVD0wTU15_E4-r3bgybATtRPXdmi8cdSTeq-8oUkHUqrkXvtTcvXrcQ-xg15Xsvc_qjH0bgHWPDjlNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌اول لالیگا؛ اولین ضربه قاطع در برنابئو؛ ژوزه با امباپه به آسمان پرواز کرد
🇪🇸
رئال‌مادرید
😀
-
😃
رئال‌سوسیه‌داد
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/104748" target="_blank">📅 00:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104747">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/104747" target="_blank">📅 00:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104746">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=eMFIliKv4er7ifEULIqO7Cb8MRYwzu7x0hYn7pDqdFfnrjbjLQ4VtfStsFBIOXxxhQ6KkZyUrnJLA4QMKCXqo-TQhZoMO7f3jOAMM0e9_JZIiojwiePqhUq8MwtRxAO8E0VOdLpbNvUG1kT4qjHQwS4eMj3iVb4soOrA0GdCNrPmTImD-1wv9JnTQ369Henclwn3qfLvNmoVNwQqQt3mmFituGmu8VlzmoOvxlax1PMFhAHLf8_aNHSlx38I9plWSHlJXo7Wd5NVSTxOKiWUUjIdisTKMcEMnjc0uUrVrRKfhYgw7HWAPJsHRAHlp2QxvyK-ecoMEj2lL-DVx-wWig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=eMFIliKv4er7ifEULIqO7Cb8MRYwzu7x0hYn7pDqdFfnrjbjLQ4VtfStsFBIOXxxhQ6KkZyUrnJLA4QMKCXqo-TQhZoMO7f3jOAMM0e9_JZIiojwiePqhUq8MwtRxAO8E0VOdLpbNvUG1kT4qjHQwS4eMj3iVb4soOrA0GdCNrPmTImD-1wv9JnTQ369Henclwn3qfLvNmoVNwQqQt3mmFituGmu8VlzmoOvxlax1PMFhAHLf8_aNHSlx38I9plWSHlJXo7Wd5NVSTxOKiWUUjIdisTKMcEMnjc0uUrVrRKfhYgw7HWAPJsHRAHlp2QxvyK-ecoMEj2lL-DVx-wWig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a4
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/104746" target="_blank">📅 00:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104745">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7653010aad.mp4?token=p9ka0me2J2YrZllH_nL_x8M9P_q86JDVhGGxalwgQWEdQ8yekKQsirB1xA4PWPdojKzFZWtGNfQf-DO7QhnQ-dd965b1Klphl8fTeg9TIQUXOF6yyjN4u6ioz7UnXOzOyqfTA4dNrrXF3N7FIhqJ309uVZKfaQqlh27Tnxh1A_oW_2QY8Xll4Hl0PE14WB-RujAlQ3MNgBEGbAbWn4NMPQD-4T33TUEd0IJYQcoHCNT0cCkIhIcmPIbZDlN95-5IbrOHSsU78_Fu-LCwh59VdMxSIkX0rULig-O46IFDzD5SoVEbM17XNPz59O9dj4eC1NQmAE3PNfieTww7uiFI2FwMMy3gGyLVC4pg5cgethVucG40H2Qy3-GwmftVa6Bl_Yfq0j0af80zADf37f4qSTm3WQNxiY-yw90v-MkCJSrRogh_blHPKdjqCrQttwA3Q4Cje4DIjN7rzFgB9g4MQtcRt8O1BxwJO26zz15sG5s-nY3lllzynKt-r6rXJ4NHELZHX-IKAzAkkTBXO7q2v2oIKJvlCXUicHrMaUq6gwyLWm-pNItKl-HpPT6BxHPGFmuHOwZ_2AG7VurUUIA9M80CZwVkGFPU7lFTHMYe1VEQqJ4POwm901uPILMKMviORkz8uWAJBV7pmWHgrsmpnRu-UQWC8e8XDy249-UM8n8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7653010aad.mp4?token=p9ka0me2J2YrZllH_nL_x8M9P_q86JDVhGGxalwgQWEdQ8yekKQsirB1xA4PWPdojKzFZWtGNfQf-DO7QhnQ-dd965b1Klphl8fTeg9TIQUXOF6yyjN4u6ioz7UnXOzOyqfTA4dNrrXF3N7FIhqJ309uVZKfaQqlh27Tnxh1A_oW_2QY8Xll4Hl0PE14WB-RujAlQ3MNgBEGbAbWn4NMPQD-4T33TUEd0IJYQcoHCNT0cCkIhIcmPIbZDlN95-5IbrOHSsU78_Fu-LCwh59VdMxSIkX0rULig-O46IFDzD5SoVEbM17XNPz59O9dj4eC1NQmAE3PNfieTww7uiFI2FwMMy3gGyLVC4pg5cgethVucG40H2Qy3-GwmftVa6Bl_Yfq0j0af80zADf37f4qSTm3WQNxiY-yw90v-MkCJSrRogh_blHPKdjqCrQttwA3Q4Cje4DIjN7rzFgB9g4MQtcRt8O1BxwJO26zz15sG5s-nY3lllzynKt-r6rXJ4NHELZHX-IKAzAkkTBXO7q2v2oIKJvlCXUicHrMaUq6gwyLWm-pNItKl-HpPT6BxHPGFmuHOwZ_2AG7VurUUIA9M80CZwVkGFPU7lFTHMYe1VEQqJ4POwm901uPILMKMviORkz8uWAJBV7pmWHgrsmpnRu-UQWC8e8XDy249-UM8n8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌چهارم رئال‌مادرید توسط کیلیان امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/104745" target="_blank">📅 00:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104744">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c75ce2b54d.mp4?token=WPt_eywWbHvw1wzmjonKp9H1Gu_oAxZb_rsuI7eMhwkhD6VVKq6HksfTBaLfVqqWUVRoNdZWwK9nyPLfx5dJyjhJH8YkyzTEx6Mf4_pqPJL34TDCenE25yg9WMLuWX2WG0NHwrpH4uUAbZg6BFX8jj0oaa-vd83xzlfHdjzwld0_jicsih-dxxYGArwgsx4hGKRsv2gmpoHc_diwurplNWXWI8cLWgcKtzFTg1eO5dDRgrzvoz5tJ25bMcXeYGcAH9hvrDYaUVG7O7Y2zkQoZY4WTk8BjmE6tADbOwitHvlAozgnvI5rfnX25VVcS1vqySXu_MR-YT4zZc5tH-lMbA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c75ce2b54d.mp4?token=WPt_eywWbHvw1wzmjonKp9H1Gu_oAxZb_rsuI7eMhwkhD6VVKq6HksfTBaLfVqqWUVRoNdZWwK9nyPLfx5dJyjhJH8YkyzTEx6Mf4_pqPJL34TDCenE25yg9WMLuWX2WG0NHwrpH4uUAbZg6BFX8jj0oaa-vd83xzlfHdjzwld0_jicsih-dxxYGArwgsx4hGKRsv2gmpoHc_diwurplNWXWI8cLWgcKtzFTg1eO5dDRgrzvoz5tJ25bMcXeYGcAH9hvrDYaUVG7O7Y2zkQoZY4WTk8BjmE6tADbOwitHvlAozgnvI5rfnX25VVcS1vqySXu_MR-YT4zZc5tH-lMbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم رئال‌مادرید توسط وینیسیوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/104744" target="_blank">📅 00:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104743">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1714a1550.mp4?token=LviJ6o4u51uHI6PhQOXBzGVzl_EMqPJwSbo4Fi4nY506NfcpZY06u4TIamhbdtiOIykcqm0juryCLkC9H3l8AOAxdTf-B2DHSzUWGU1ZuFqi0mWYQG50whFLpt4uecbycCnAb8oxGK-AoFU8llcIVNYv8_ltoKS-fMwB6aJp89dztpVRm0NjOlzZaWFrBbf0Wrc3JyVk6SMVyBerC-ImMsIDDJfXS8RVE5n-VqOO2kbmAEULl5ZYTM4jYQrWSFYyshKAC09OX5Y8lxXIDFR5-pIEo0Kp_AkHu9Nhy_lfyUhBzlQtxKWMiRCLx0AG7sZoKUDD-HZ0wlbrcl0qPYlBsA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1714a1550.mp4?token=LviJ6o4u51uHI6PhQOXBzGVzl_EMqPJwSbo4Fi4nY506NfcpZY06u4TIamhbdtiOIykcqm0juryCLkC9H3l8AOAxdTf-B2DHSzUWGU1ZuFqi0mWYQG50whFLpt4uecbycCnAb8oxGK-AoFU8llcIVNYv8_ltoKS-fMwB6aJp89dztpVRm0NjOlzZaWFrBbf0Wrc3JyVk6SMVyBerC-ImMsIDDJfXS8RVE5n-VqOO2kbmAEULl5ZYTM4jYQrWSFYyshKAC09OX5Y8lxXIDFR5-pIEo0Kp_AkHu9Nhy_lfyUhBzlQtxKWMiRCLx0AG7sZoKUDD-HZ0wlbrcl0qPYlBsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم رئال‌مادرید توسط کیلیان امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/104743" target="_blank">📅 23:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104742">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/592c7db362.mp4?token=XVo5xr1euY2eaqe1dzU0shFzFdng-iQeFAlAHNI13yMnzrcqwIKSSp6wOix0aKwLUmZv7_f_q74M5xU-smAxlyxoWZT_unp3U5HATVICLJ9K0BhV0TXIHRQx_iFxNMFxf2v80y4NrEmy54X8K5oWPvQ2FmXy73EFUdJwY4ghYX8bjGan76MxK-BC7nHNdNN52yzOtXqPQqy6DrsM6bJIKrtHf8P6YQOuDwDo8hsKjaDYyKJFYahuoIJtfb1_4-4plsXl_8uFWstEVjSMr9Hj_8g19ICG7RDr65TUvFLnOM5DKY36dqmVaxo5rJHh1c8GPRu0j4iN7G4dh6oYg6OPoKwbb4ol_UOeBdqE4KMt6fzHx-3zOwCXwZs3QnV3nZgfnFFI6u22N7UTdB2ZHfJZqfV-aLabHtzRd2xb0enjy4kuOfUmuCcVXn76_ycbOSsihmW8Op0ff8t6PCanzcoK20PKwYPtC1lfZ-jjhKdrmr3e7yQOq6DXlPs_jSzI1Ba0cFYPiEvuTqsegRYt-f2cjTgISekPqEppkBmWf5fLQj4JTedB3_XyhMPyQeEYdJKVRLEemXgIvk2q-EbNd9yUv_mYvEl42JJqE0dceVKdhoP5ZqP_nY6BlSnyRe84KCEjTD5wcxRs_U35P07mW7_2eGzp6B1Y7z-gCHpa8S7VgiA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/592c7db362.mp4?token=XVo5xr1euY2eaqe1dzU0shFzFdng-iQeFAlAHNI13yMnzrcqwIKSSp6wOix0aKwLUmZv7_f_q74M5xU-smAxlyxoWZT_unp3U5HATVICLJ9K0BhV0TXIHRQx_iFxNMFxf2v80y4NrEmy54X8K5oWPvQ2FmXy73EFUdJwY4ghYX8bjGan76MxK-BC7nHNdNN52yzOtXqPQqy6DrsM6bJIKrtHf8P6YQOuDwDo8hsKjaDYyKJFYahuoIJtfb1_4-4plsXl_8uFWstEVjSMr9Hj_8g19ICG7RDr65TUvFLnOM5DKY36dqmVaxo5rJHh1c8GPRu0j4iN7G4dh6oYg6OPoKwbb4ol_UOeBdqE4KMt6fzHx-3zOwCXwZs3QnV3nZgfnFFI6u22N7UTdB2ZHfJZqfV-aLabHtzRd2xb0enjy4kuOfUmuCcVXn76_ycbOSsihmW8Op0ff8t6PCanzcoK20PKwYPtC1lfZ-jjhKdrmr3e7yQOq6DXlPs_jSzI1Ba0cFYPiEvuTqsegRYt-f2cjTgISekPqEppkBmWf5fLQj4JTedB3_XyhMPyQeEYdJKVRLEemXgIvk2q-EbNd9yUv_mYvEl42JJqE0dceVKdhoP5ZqP_nY6BlSnyRe84KCEjTD5wcxRs_U35P07mW7_2eGzp6B1Y7z-gCHpa8S7VgiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌تساوی سوسیه‌داد به رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/104742" target="_blank">📅 23:19 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104741">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گلگلگل تساوی سوسیه‌داد!!!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/104741" target="_blank">📅 23:19 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104740">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf83d89368.mp4?token=uUq3AzPo9lcfVWRplCwg1sC1IQfaO9Beh65f-0w6OPv7eL1UZLrLeY09fyAhm6N9GB_IfN6vObbXOpVMOGLaUsKU0E3qVWDzAAbHyOrgFTVK1oIlWIRDyfsQUWf7EKwmj8xPhYvGJolHP-h67biE45FjQax_hDNVXMeggUgoXunHNNOlai23Dq05d1T3HC27fhJ2Z_PSuxUZ2hiu36r2I04VZHWAq29SiaDB28E1tXI7VLr5REvwnz6uobUEeGjz8sYwXwRVi1Fu_9eY9rlu0LEUhtvVe0SS7WtHh50bE5ZZhWsufhjpZ2YLsX6BjvEVtpvsewrbwgRULbt58KL5pw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf83d89368.mp4?token=uUq3AzPo9lcfVWRplCwg1sC1IQfaO9Beh65f-0w6OPv7eL1UZLrLeY09fyAhm6N9GB_IfN6vObbXOpVMOGLaUsKU0E3qVWDzAAbHyOrgFTVK1oIlWIRDyfsQUWf7EKwmj8xPhYvGJolHP-h67biE45FjQax_hDNVXMeggUgoXunHNNOlai23Dq05d1T3HC27fhJ2Z_PSuxUZ2hiu36r2I04VZHWAq29SiaDB28E1tXI7VLr5REvwnz6uobUEeGjz8sYwXwRVi1Fu_9eY9rlu0LEUhtvVe0SS7WtHh50bE5ZZhWsufhjpZ2YLsX6BjvEVtpvsewrbwgRULbt58KL5pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول رئال‌مادرید توسط کیلیان امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104740" target="_blank">📅 23:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104739">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">امباپه یکی برای رئال زد</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/104739" target="_blank">📅 23:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104738">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rq11yY_FRlZ_XPclXayNYbATL_oUXkRU2yIXvKrIUUZlN5ArMgGmsuIDm2neVI39tlPeVb83qQn1cNSkrQzvk8QKaCl8zIpVo1hfzWSnwNOUFpT2dDniAzUzQMWu0trUh-z7OhGvaDO2d0ZaftLKlBhJYqTGImMKLUqadPhk6xNkr44adifn9C4ZHeyFtsVphKrC0CCzvxB6-5glNs8168gtoOuD8K3SpmKW1ARjdyjS3kC-fhho5EE8O7un-MKaMei4c7U41LIXO9DPWHPmcojI8SiuvFPFbe0GzES7caQbGnnaLSbZAalyr6hf7P0BpbkQcRfoeZnFvQjMqadicA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جرارد رومرو: هیچ توافقی میان آرسنال و اتلتیکومادرید بر سر خولیان آلوارز وجود ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104738" target="_blank">📅 22:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104737">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvOW_VHRQ7vlM8xCUsQBh87APjWq0nM_lDjMGBdMsHZWA-659A-d0bBSG5BTS2b8Az_LBxCIia8ij24bBv6VtDeg_IjCaO1T0gIJiWG9GUKtOFzeimXPLbCPgsf0OfosK8uu5vfFv9WXyluhTjX1J-AwzeBYBtzIxQzxkEAE0e3MSuxy3MM-U1wF0TxSnsyhx5o9N9hk-ParGdzM6IMxOa5-dVsoOKLvjDIXnjKEaF0CuZ0veb8EdE-jjY3IhhPVatfpKZIWZdo1EM_Fci4tol2WZaIC9AnkSN1Wnng6IZUvncSdRb6zkym1Nyv6PLc-aMEkJDa_gaBxffHrfG4PiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🔵
🗞
#فوووووری
از رومانو؛ اولی واتکینز از استون‌ویلا به الهلال عربستان
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104737" target="_blank">📅 22:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104736">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a7a829591.mp4?token=ptrb1kxNuMqei6d73ydRUfCvIl3v-vmScyhA5OgAbu0SD2RoTd0kAE80mDuSsV7fhi8iK7OUm1kOaGWKXaTn-QiXl1TMyOpMFtjzgEMGB9Tl9lLN4T3a43VWxPsb2xSRG9YYUBzZPiiDys2xzNDKHN8u20Al5Dwve7cTfbpve_im_1g1i5_G_CrnQKabMNq9XmZK3gAWkE-l-wBfmy8J1jvrN2wJ8PVo0j642evueNFVsLT5QUzBoEM761rt8RiUYNrdx94j_Lm8IFPNYmVwAIA_UQhcjcafl6601KDgZquaNold1y6u2xZtBwskODfgDjOTsnKAeQWbh5yfvtLWqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a7a829591.mp4?token=ptrb1kxNuMqei6d73ydRUfCvIl3v-vmScyhA5OgAbu0SD2RoTd0kAE80mDuSsV7fhi8iK7OUm1kOaGWKXaTn-QiXl1TMyOpMFtjzgEMGB9Tl9lLN4T3a43VWxPsb2xSRG9YYUBzZPiiDys2xzNDKHN8u20Al5Dwve7cTfbpve_im_1g1i5_G_CrnQKabMNq9XmZK3gAWkE-l-wBfmy8J1jvrN2wJ8PVo0j642evueNFVsLT5QUzBoEM761rt8RiUYNrdx94j_Lm8IFPNYmVwAIA_UQhcjcafl6601KDgZquaNold1y6u2xZtBwskODfgDjOTsnKAeQWbh5yfvtLWqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رونمایی نیوکاسل از نیکو گونزالس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104736" target="_blank">📅 22:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104735">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKlc2asHwqlHZhz3jAa2B2djKkCQHJH7V7jtQkplFWCYv6x-gOdRxpESO1veqI2RfVzZhhbMGUhpvQdaDmsDAHasJ-Vnh0vTwG97VFZUNf6Fj7SzTkvM0GQmomW2I-wqeA-IWsWAoGL-sNeEyLslKiAf7Ire7f90HShKXeCL9hHwx2cJfqxcscLHif30jnxR3lCzvYSZHo8zldYqIoye85QyvNWm1R3Or4de9sEHatPUmeJu2xl1j5WSCBW4aSiIvfl2iCLZjdEZ_3Ac5iLi6p34nV3AVaBvPPyMxC2rO_fUW00JjSgLK9xiB9mh3vPbuV43qkT6tsiJGNI0SY3gDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اتلتیکومادرید و استون‌ویلا با نیکولاس جکسون به توافق شخصی رسیدن و مذاکرات با چلسی برای توافق نهایی ادامه داره و بزودی جکسون راهی یکی از این دو تیم میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/104735" target="_blank">📅 21:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104734">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c61000564.mp4?token=TYSeolXhud0-Aq7XvtzJ_K5aTTmPo0uZfN4WE6t9Mne4U-m1PRgdm1jD-h3p8POtXRvL7vcqOXAKqQwg5JEk3tuRtWmt4KYtuR8lyAHxaSTldvHsSxfgrBW_92ucZE9xKq-9SD21-y3MjThtNRnP1crbkB9xmrr2T_7DGEvrlO89tYaU_XdnItRlBWX-JCoAPwzgBHsC4OQYwcY2ybdVZC8OT53Z4Yv6hBtX0LTaQXFYT43FuP176xlJkA1p35LbP1Z6me9EuNKBYzAE9zr4uldkb4V9aLYyS9oU0BAzLHFLvHAcHBEu2gSSP-jLLJzIt_I7CpIbadRekGGnEl9Mlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c61000564.mp4?token=TYSeolXhud0-Aq7XvtzJ_K5aTTmPo0uZfN4WE6t9Mne4U-m1PRgdm1jD-h3p8POtXRvL7vcqOXAKqQwg5JEk3tuRtWmt4KYtuR8lyAHxaSTldvHsSxfgrBW_92ucZE9xKq-9SD21-y3MjThtNRnP1crbkB9xmrr2T_7DGEvrlO89tYaU_XdnItRlBWX-JCoAPwzgBHsC4OQYwcY2ybdVZC8OT53Z4Yv6hBtX0LTaQXFYT43FuP176xlJkA1p35LbP1Z6me9EuNKBYzAE9zr4uldkb4V9aLYyS9oU0BAzLHFLvHAcHBEu2gSSP-jLLJzIt_I7CpIbadRekGGnEl9Mlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
جوری که رونالدو به گلر کسخل النصر دیشب داشت گلری کردن رو یاد میداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/104734" target="_blank">📅 21:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104733">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QwVYdGLRqnFIVbHe-N_67ipuJ4iphjnV9COLAxD9Ml_M_TgZCds4GAYKICgsiohIoXQISoB2f75n6tJX8aU2am4YllxCS5LzjozKRC8FGyeO3Pvx4TOc97jFwD3K_izIE9wEyv8UbTaWxcIJmR3fgpqoVsoEzpYnPYJjcs2sXMLmg9-UmMh_fNEtEeX27U8aLBsr6-9ml6RxbIhUAt0oTACbOrZ3dViG6MlE23WLKtJYYKTObOdc8LFHvuxar3toDdW-dlqgCjWXcACPaICPqu4GrcB2zNlIyJYkqduEMDkLyXjTQ2CB1fyN3UFjfQSEp3jmp5BVWaEzi-qPwmyhFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
ترکیب رئال‌مادرید مقابل رئال سوسیه‌داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/104733" target="_blank">📅 21:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104732">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/576668f60b.mp4?token=nI8K1VUEgp5n1QPMG2_Jl76k5XjSGOlveo7ye4VfeYJUI-asAsyCFeIN41wjFLYRy93342vStEyTSSY9ia_LicJgmGWxvnCCsukIBVS1fo7I39Tv8uwr3RZiXFS0i5OsxMdDQqoAoPAGvWpkWf5bxsDQqXqh9emFxEd5c01Iko0D6Ar9HC5NyiZr2Xi8Ffia8-xuLgzPoowWy3FngLEM9887aqxaAXxsXSEd33aPkKk1qOFQ7j7UyCTxJnG1r3vb8-fe_YMD1yQtXjQMAhUY3a3V6e6yV5WSF_0gLBSDIEj9JPJ6qvq-4dpSLFmBHlTOWkKZV8YY72xVSj__scO-Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/576668f60b.mp4?token=nI8K1VUEgp5n1QPMG2_Jl76k5XjSGOlveo7ye4VfeYJUI-asAsyCFeIN41wjFLYRy93342vStEyTSSY9ia_LicJgmGWxvnCCsukIBVS1fo7I39Tv8uwr3RZiXFS0i5OsxMdDQqoAoPAGvWpkWf5bxsDQqXqh9emFxEd5c01Iko0D6Ar9HC5NyiZr2Xi8Ffia8-xuLgzPoowWy3FngLEM9887aqxaAXxsXSEd33aPkKk1qOFQ7j7UyCTxJnG1r3vb8-fe_YMD1yQtXjQMAhUY3a3V6e6yV5WSF_0gLBSDIEj9JPJ6qvq-4dpSLFmBHlTOWkKZV8YY72xVSj__scO-Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و ژابی آلونسو که دوباره خوشحاله ...
🥲
👏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104732" target="_blank">📅 20:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104731">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpOiTsJV2aU7ltjslw2do1HqOpfpBJRc0Me-S7E-KXoAXifCISzS7Amxcu5Fu5_yujeeN5ORwMtmkCaZBkGq7Hx7Qa8Vp-rKN6slsUtNZlePHq7JBWv7D9vPa_BNo1in18feUhzCcZdBuBzKOWolUQwC0rCCwlyUZ6af2f_iFtH9DcsK58lIyT65qn_kh3oa_nl_TvlCOXenK3si6KD5KUe6VcF3bGFctn-5IjYos7JEAQFSjkqeba75WNWClDgaGbrpFkSsFPY_xYq9HRtTj-t4_52hE8ylTOahJrl2Rg32Pb6Ym80hZb8AeCHVSWtC2WTXv2BJghDfQPbrlygT6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته اول لالیگا اسپانیا
🇪🇸
رئال مادرید
🆚
رئال سوسیداد
🇪🇸
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104731" target="_blank">📅 20:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104730">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
🇮🇷
عصبانیت و فریادهای محمد نوری سرمربی صنعت‌ نفت بعد شکست عجیب جلو فولاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/104730" target="_blank">📅 20:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104729">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6p3RhIYBUyclJsaRjoOKoO_GbhWJngCC38Hp_Or8VP-N43QHtqzEraN3nXgRJc3yMVzOqXU9nMAadEf9sFGMss40PeFTpJfE5z_VW7C1mOR8MEotrKORb8K8TTJ4955dIzaLdfkBlV-kb1W9s9LiLX7rN343635178CrUAt0RqOZNMHPlOKmbWNfep7EitsrDLXPhG3qNa1MCdWdvMUiL57NTLL18-cgsFsWjfzUg__IkO6WaxeGBuIdTITZ42ZTWs3XbOH_dZZ1c4Ygu2Cp610KXfg8BG99p8BDnuTCVGxcMUbErLMvfjaYbtA2dg9Nv2LPQv8Z7mPeC6LpjIURA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
یک حساب کاربری که فقط اخبار مربوط به باشگاه اتلتیکو مادرید را منتشر می‌کند، گاهی اوقات منابع آن قابل اعتماد هستند:  جولیان به احتمال زیاد به آرسنال خواهد پیوست و به پیشنهاد این تیم موافقت خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104729" target="_blank">📅 20:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104728">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQ4i0ywfGwZ0F3mfj1ECbMPxPz5Nwl8ltDdgljmCx9a3VzHlHdiNpERD954tcSKE9whW7Vsy257niqNy4maDOBjKJ8slM_bZPB6g566JtklFGPsBQO_IBUdk1pGXwcMOHcrgUsNmRgLGW_ImlhhPDMydgYPUnDdANpPTW48YO-0Cao6R1lf_J1i9aYwyKvVEwqWgOg4v20IzjxcCM3sYtgEeJGpotoGHx_LWA9P32KcyQpwa-TUXignxhsTeegujWpOqiidjJtz2To9u0cYSDttSakMWdwIII-iqAtOu7Jpp-UgKwTyItMdnO4FaaE1pFq_ldhf8Kft6bIECVH6U-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اتلتیکومادرید و استون‌ویلا با نیکولاس جکسون به توافق شخصی رسیدن و مذاکرات با چلسی برای توافق نهایی ادامه داره و بزودی جکسون راهی یکی از این دو تیم میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104728" target="_blank">📅 20:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104727">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78e019b361.mp4?token=Mxj4rBy1dzYo04oBf4I4t0qbijlBYkVxYqgb94abxgZ5U1GMB0PC9BI-h3ipZNgo8rfx52uXVRSR1p2Il2CaFjoteB4q2LtCNvPafKFVF6xK1we0VWJ5-1UfLojGwyIwQmVgGQ_ruefWGP0RP5FOxog1R_OUFtZA9lOG99VTptNSXuCq9WW8v4DYciv_xWflPn3AoZ9MvMWtH0pEa5qFEKnGRVnLwv-hRBiCQOFKKPKtMnSwNrQwFWjV_cJlC9OUFGWBBFBW2FQ6xhfFlTcQZ7mTwJL-5l67wIIGLpbddurHeKCGZeqEG5m7qBUf4Kf2OEzO5zPI7czy46pXF2pd9jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78e019b361.mp4?token=Mxj4rBy1dzYo04oBf4I4t0qbijlBYkVxYqgb94abxgZ5U1GMB0PC9BI-h3ipZNgo8rfx52uXVRSR1p2Il2CaFjoteB4q2LtCNvPafKFVF6xK1we0VWJ5-1UfLojGwyIwQmVgGQ_ruefWGP0RP5FOxog1R_OUFtZA9lOG99VTptNSXuCq9WW8v4DYciv_xWflPn3AoZ9MvMWtH0pEa5qFEKnGRVnLwv-hRBiCQOFKKPKtMnSwNrQwFWjV_cJlC9OUFGWBBFBW2FQ6xhfFlTcQZ7mTwJL-5l67wIIGLpbddurHeKCGZeqEG5m7qBUf4Kf2OEzO5zPI7czy46pXF2pd9jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاطمه خلیلی بازیکن تیم‌ملی والیبال ایران که به زبان انگلیسی به طور کامل مسلط نیست، دیشب خودشو در گفتگو با یه خبرنگار به چالش کشید که مورد تحسین رسانه‌ها پوشش‌دهنده مسابقات قرار گرفت. ببینید صحبت‌هاشو جالبه
😁
😁
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/104727" target="_blank">📅 19:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104726">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaevHRynWQIVGjU5XNCvPUbASOOVp-jC-7ETJ1b4sg3h1k8gESmbnTy8xBzZeh9jmWO4NsG5qPi3IAB3qJyCzG6BJcZXRVBKg8Pu-l-UmfAFDYRYPYjXS87qTe_nC9rpvUGbV3S-tXZcAeazFsTD2iTqFHWafLqSek-yPPb1D8j_y0nYQBpCcZ5S-FkD6iicGoIXe2x8J5mjVc4IMtYTQn5gLv8kzY48nt9SE8crGpzKzupLhO4kD6Rm3xH3Er18cZlvSvgdYKeNMvBEYKx6vB2LZ3mExEzsjRerI5_N0wSgq9EkDVjtaaNYhoFK947WMO13DWItf-TZ56VCZQ2gKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
یک حساب کاربری که فقط اخبار مربوط به باشگاه اتلتیکو مادرید را منتشر می‌کند، گاهی اوقات منابع آن قابل اعتماد هستند:
جولیان به احتمال زیاد به آرسنال خواهد پیوست و به پیشنهاد این تیم موافقت خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104726" target="_blank">📅 19:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104725">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64ba0d1ad8.mp4?token=PtTsaDwtfabG_Cy-GS5w-YEW4xqDPP463IaN7UG2Lm2U9wEDduMJjy3_6GiiW2Sn6qjgVLOYuCZWXgSipG2TSGz3KeTbmR_4qZ56hgO0uM642E5pc66SGKBR8LaCjU3bHylVJfgaPn1XzkNDp9yZINpGhUgUgFoN_TYVUBx7N1GgOpNqts4zA6riia1GqRJxJTaTjrMu03iCWPDjd9JZbpXcxB5Cw_YnhH2HhGwPmseI_34WshA8vv6fLdmDAn8J4XUQ3_0o1LFFYv-PxeGSPPEWmzbvJYUPuqploQ96FddTKLUAuuZIuLuWM6f-S9KS4Td49vnILIOl5bO76HnuDmPuhrOvYDM7NRaboE_nN2nbsDi_VdpyATsDL7qHpxY3AGKr-sYWyGjKU_32yqi8YhadBSiBx6z-WG3m1dUnnzR6_UCDBdp3_LBXEj0NgfHERMiB-5dbe2pREVuv1jEcJ8wCLfurAowI--HDSUm6c4TrXQnoT8NIU9md7GWqopMY74GKbAv6qs2UYgrz5f5MsSchmNkAd16hhdeL9OUTkZy5Rs4jgA4k7tAbD9caaUIYsSFg2lKJ2_tLt91aq3-13UxfFNSzL9Af7l9Kd6DL9sU_VmU85ht7nI-060XdJ92fRu3IFnYzH8ch4zNuuLTuvdTJw70VT-zXUVs_AHMYZk0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64ba0d1ad8.mp4?token=PtTsaDwtfabG_Cy-GS5w-YEW4xqDPP463IaN7UG2Lm2U9wEDduMJjy3_6GiiW2Sn6qjgVLOYuCZWXgSipG2TSGz3KeTbmR_4qZ56hgO0uM642E5pc66SGKBR8LaCjU3bHylVJfgaPn1XzkNDp9yZINpGhUgUgFoN_TYVUBx7N1GgOpNqts4zA6riia1GqRJxJTaTjrMu03iCWPDjd9JZbpXcxB5Cw_YnhH2HhGwPmseI_34WshA8vv6fLdmDAn8J4XUQ3_0o1LFFYv-PxeGSPPEWmzbvJYUPuqploQ96FddTKLUAuuZIuLuWM6f-S9KS4Td49vnILIOl5bO76HnuDmPuhrOvYDM7NRaboE_nN2nbsDi_VdpyATsDL7qHpxY3AGKr-sYWyGjKU_32yqi8YhadBSiBx6z-WG3m1dUnnzR6_UCDBdp3_LBXEj0NgfHERMiB-5dbe2pREVuv1jEcJ8wCLfurAowI--HDSUm6c4TrXQnoT8NIU9md7GWqopMY74GKbAv6qs2UYgrz5f5MsSchmNkAd16hhdeL9OUTkZy5Rs4jgA4k7tAbD9caaUIYsSFg2lKJ2_tLt91aq3-13UxfFNSzL9Af7l9Kd6DL9sU_VmU85ht7nI-060XdJ92fRu3IFnYzH8ch4zNuuLTuvdTJw70VT-zXUVs_AHMYZk0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشت‌صحنه کوتاه شدن موهای وایکینگ دیوانه!
😄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104725" target="_blank">📅 18:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104724">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گستون‌ایدول: دو باشگاه چلسی و تاتنهام درحال رقابت برای جذب امی‌مارتینز سنگربان تیم‌ملی آرژانتین هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104724" target="_blank">📅 18:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104723">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba5429d657.mp4?token=mMBw7C9IqgU2GRvciuJqTwadcoMzIi9WAC7cXXlWJAsyiRdXMTIWYiafCTqYVUBrqb-4zioddDOOExRTsfQRoFaiSOHH0i7B7k_rtlD-5m5ma1II-FZIvma3mR3593UOY2brJgVOET9GQ7vlMubRFlz3mkaNYcoZPZ-5GDzReurb1yDEg_BGk7WXgwapqDelMgd3QdqUABBcV3Vv7hE4TLorf5II_JW7cGOzO9VqvQj_9QQ1dyPjoaMnYOcp2zUBMiT8Htof4jbstFdmQCpaxCMUIBy2PH5Qhg4gTwSaXw5p-olTM_gcyxBR3a0OSU6-HiltkeDfXBzsYupSBsjOEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba5429d657.mp4?token=mMBw7C9IqgU2GRvciuJqTwadcoMzIi9WAC7cXXlWJAsyiRdXMTIWYiafCTqYVUBrqb-4zioddDOOExRTsfQRoFaiSOHH0i7B7k_rtlD-5m5ma1II-FZIvma3mR3593UOY2brJgVOET9GQ7vlMubRFlz3mkaNYcoZPZ-5GDzReurb1yDEg_BGk7WXgwapqDelMgd3QdqUABBcV3Vv7hE4TLorf5II_JW7cGOzO9VqvQj_9QQ1dyPjoaMnYOcp2zUBMiT8Htof4jbstFdmQCpaxCMUIBy2PH5Qhg4gTwSaXw5p-olTM_gcyxBR3a0OSU6-HiltkeDfXBzsYupSBsjOEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش میثاقی به وضعیت استادیوم قلعه حسن خان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104723" target="_blank">📅 18:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104722">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72db3ef094.mp4?token=pNvVL2zlWJOG-kcJc7D1kgvDhvPazSdk2oszoD7uCn4UtSXmP1EXRHaq5K8qubOJ4VkousYvhP0CvGsRt3QeKuLhssD1ZxgqSZZPr6_Tk9rWCrxAUM-5yi_akDl5tGOtvJ_HpsQHOl-vCqunDBMXNPatdhv6Fx7SlR7Bg3y8yxDHIUyNkSB255q69PBrFV717wXUNLnALU-EhZ2p_epp2VvkT4Ze8DZZHkfd1IHUvg7AYZDbIYAmdWBADB__gFqta16xVY6ieFr8hlJ2haM2XVnIfvPzznYXdfcAVqJcGPJitG-wW4Xvh2BoBEzUke242U8U-Ssa7S-IXhVXOc31ZTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72db3ef094.mp4?token=pNvVL2zlWJOG-kcJc7D1kgvDhvPazSdk2oszoD7uCn4UtSXmP1EXRHaq5K8qubOJ4VkousYvhP0CvGsRt3QeKuLhssD1ZxgqSZZPr6_Tk9rWCrxAUM-5yi_akDl5tGOtvJ_HpsQHOl-vCqunDBMXNPatdhv6Fx7SlR7Bg3y8yxDHIUyNkSB255q69PBrFV717wXUNLnALU-EhZ2p_epp2VvkT4Ze8DZZHkfd1IHUvg7AYZDbIYAmdWBADB__gFqta16xVY6ieFr8hlJ2haM2XVnIfvPzznYXdfcAVqJcGPJitG-wW4Xvh2BoBEzUke242U8U-Ssa7S-IXhVXOc31ZTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما فقط رفتار سرمربی آلومینیوم و شمس‌آذر رو ببینید.‌ بعد میگن چرا لیگ‌ایران سطحش پایینه
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/104722" target="_blank">📅 17:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104721">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/104721" target="_blank">📅 17:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104720">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAjZmuxN-jXAYuaF6mJfa6FuIsha6aYH_jBkmrhoYAyQytcnERPBGhv0pkADFulP1YSoIuUAtIRizJmsyYCZl1QvzXqCF0vewj__SaDMh3PopnqzyvMK_-NTCcRUK8WIlkEam5XuSStyV2MdpFQ8uFRcY0MY9uTrgTkJvZBjneSqjiMBHXElbhau5Oo1jETjF70qEBIG_YUxmhl2cdOXHW9SCmfzZVXfLPYbZYKS7b4DEcBR1wPV8KTkX4cKvJkrCs8rX_DgKRnisWrEmTW1AV1Hj657W_eaebZQgVX10FFQp8jIExEzphX_bpMfUGLz8LcKAcih9H989uDp-V8_65xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAjZmuxN-jXAYuaF6mJfa6FuIsha6aYH_jBkmrhoYAyQytcnERPBGhv0pkADFulP1YSoIuUAtIRizJmsyYCZl1QvzXqCF0vewj__SaDMh3PopnqzyvMK_-NTCcRUK8WIlkEam5XuSStyV2MdpFQ8uFRcY0MY9uTrgTkJvZBjneSqjiMBHXElbhau5Oo1jETjF70qEBIG_YUxmhl2cdOXHW9SCmfzZVXfLPYbZYKS7b4DEcBR1wPV8KTkX4cKvJkrCs8rX_DgKRnisWrEmTW1AV1Hj657W_eaebZQgVX10FFQp8jIExEzphX_bpMfUGLz8LcKAcih9H989uDp-V8_65xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
g4
⭐
کانال اطلاع رسانی سایت:
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/104720" target="_blank">📅 17:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104719">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cecc802f04.mp4?token=fN1DUc0TIf7auLA2ARzKe_RVo_ro95_sguiEd0g70kryEQ42Nr7QlB8XcVixfoyGsm3xlEBpgtY3htMbMjSijcCst1dugjDk6jxWTN2KII-5Mc6OoWPDAsIRVOsrvx6XrNzJBTwFMFQUVZ-oxErlA8nWB3uPN48_2dv-LXRi9J4_mKMbKC5suu21lSIMi4NTeyyMS7tV8gzIEyDjSAQtwXcuNaEF0kwxktFpOVd2VxTHo83djKWi6AbXnQ6VGgY_xyCPqo_Y_kVOkW0a4hx0Z2LZXc2K7lGK2P1fmw8MZwyY-OYh735RMWl_SB2jSLLeqyOYdEsM1nCHd_YxrkS3ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cecc802f04.mp4?token=fN1DUc0TIf7auLA2ARzKe_RVo_ro95_sguiEd0g70kryEQ42Nr7QlB8XcVixfoyGsm3xlEBpgtY3htMbMjSijcCst1dugjDk6jxWTN2KII-5Mc6OoWPDAsIRVOsrvx6XrNzJBTwFMFQUVZ-oxErlA8nWB3uPN48_2dv-LXRi9J4_mKMbKC5suu21lSIMi4NTeyyMS7tV8gzIEyDjSAQtwXcuNaEF0kwxktFpOVd2VxTHo83djKWi6AbXnQ6VGgY_xyCPqo_Y_kVOkW0a4hx0Z2LZXc2K7lGK2P1fmw8MZwyY-OYh735RMWl_SB2jSLLeqyOYdEsM1nCHd_YxrkS3ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئال و سیتی فردا تو قرعه‌کشی لیگ قهرمانان:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104719" target="_blank">📅 17:51 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104718">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/823997ed12.mp4?token=JUDjd0odCJ4l22Du9OeIdusHdzTd6dMgq4UYMVoG3BZUFnDUD1Oyu3e-leFOpDoL6gQuMq9opJ0Q5bACduRnqKdfQ0VpEaFH2fiKuuxRVW5tAFolT1jkNx6kr7QaxxpXQ9sV5d9WztReVb_LGWz4B0DU094WrTyg1wVOpj0Fs6iNzo7DMhF6MawnwLnmujyk8qs_poh7wt6WHZdJFJaZc7FrQwAnTeXbj8ywAvgaoCK1JWAECcT3PpPGH43Rdn-wYqoFxHEBVsiPQdnGAy57a1Fd92-tyIYX2kJ0l4Vwerm6n6RpNAD43YChooX6WEsrI4W7R8WpdPtvV_2plGQk_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/823997ed12.mp4?token=JUDjd0odCJ4l22Du9OeIdusHdzTd6dMgq4UYMVoG3BZUFnDUD1Oyu3e-leFOpDoL6gQuMq9opJ0Q5bACduRnqKdfQ0VpEaFH2fiKuuxRVW5tAFolT1jkNx6kr7QaxxpXQ9sV5d9WztReVb_LGWz4B0DU094WrTyg1wVOpj0Fs6iNzo7DMhF6MawnwLnmujyk8qs_poh7wt6WHZdJFJaZc7FrQwAnTeXbj8ywAvgaoCK1JWAECcT3PpPGH43Rdn-wYqoFxHEBVsiPQdnGAy57a1Fd92-tyIYX2kJ0l4Vwerm6n6RpNAD43YChooX6WEsrI4W7R8WpdPtvV_2plGQk_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
😐
نهایت‌واکنش مجلس شورای‌اسلامی به تحریم ویژه‌ آمریکا و محاصره دریایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104718" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104717">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIuPh-AU_4cB7paafr5OqrBeMfv4obzTmND1wCum_yahKlonRi_eSCW13iB10OlrAvJTwsbja0eIpbmxmifcnMc9aUntb0FBmpESmN8nCLVCoFDLnOOyZu9XHfpcfsezH6U9RU8eZfHqH8zSJt_3FpANUlLV20404DTZwFToHYroQjBzfb4B8dpJZLs4p8blTp6xko-2UJz6w7rXmBOuj8X-7uGJquL9llZbk8oKJR8zop6YfcuZVHAafJt2X040KxypgVdEeCNQu6LdEPMB00AbCpHjHqYORo9c4H9Legvi-fenC9f_jKVmMMgMKz615gj3hzV-VLd89BTB2qO_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
بیانیه اتلتیکو مادرید به MARCA:
🔴
«بازیکن را به‌عنوان قربانی نشان می‌دهند، اما تنها قربانی در ماجرای خولیان، ما هستیم.
🔴
آن‌ها از نظر اقتصادی و اجتماعی به ما آسیب زده‌اند. احتمال فروش او به بارسلونا ۰٪ است. این پرونده دیگر بحث پول نیست، بلکه بحث حیثیت و عزت باشگاه است. احتمال فروش او به بارسلونا ۰٪ است.
🔴
یک کمپین رسانه‌ای شکل گرفته که شامل دروغ‌های زیاد و روایت‌های نصفه‌نیمه است. اتلتیکو تنها باشگاهی است که هزینه تمام این اتفاقات را می‌پردازد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104717" target="_blank">📅 17:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104716">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb2788185.mp4?token=d1XYvULGDp7f7tharHOdTWoaQ4q7k0aJOh5B_pEGpSaigE-cW4Y4gwBfq49KKddER-i_J9kVapneq0Y-2i7O9azFlUHqgYmYU38Qo9QsRs_pkl_k8zZxQwpafzx7GJSF0mUinTTVcSjuaQdicGQRht7uuo_z7hhqgN_958RfvZ9CUSSa3mf8UEqk3RkzNTl2P8Q2J4enOVScVo6IZLoOKtfWFoluswII78iTD2Ixz9DFf2fjYens_e9Cg4Lj_ubsnn1-4T4eyFSNssHdGnJAWy4sxD8axXfsIvbgSX7lrR6dqkCAYa6ngO_VvbTMwjsf4NuxA-FeZFU50Mzxl3F-zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb2788185.mp4?token=d1XYvULGDp7f7tharHOdTWoaQ4q7k0aJOh5B_pEGpSaigE-cW4Y4gwBfq49KKddER-i_J9kVapneq0Y-2i7O9azFlUHqgYmYU38Qo9QsRs_pkl_k8zZxQwpafzx7GJSF0mUinTTVcSjuaQdicGQRht7uuo_z7hhqgN_958RfvZ9CUSSa3mf8UEqk3RkzNTl2P8Q2J4enOVScVo6IZLoOKtfWFoluswII78iTD2Ixz9DFf2fjYens_e9Cg4Lj_ubsnn1-4T4eyFSNssHdGnJAWy4sxD8axXfsIvbgSX7lrR6dqkCAYa6ngO_VvbTMwjsf4NuxA-FeZFU50Mzxl3F-zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جناب بالیبا خرید جدید یونایتد که استعداد ویژه‌ای در کار با عضلات کونش داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104716" target="_blank">📅 17:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104715">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6091db717a.mp4?token=iTwHmisAdYWWUue7ocJfGUU8admFDbBCSAqM6-j_bWm47myw1OP1v7szZPakQ4PWCtnkFGJzlbqGW2JKq7leg7h_3vg3ufu7w2CGPyEqKQz0uHIn_doGsAxnz0qXLlxoUojz8lTmzjUCzt1Rkm1B2Bce6UP83dXO5j_cpsPPGvD_nsYe0-VxeaPh3quXN9s6PP-8IyX_wCGqKneJygtlRs3oab2S9cO9YTgBoiaxdDUakZCmuQlKizbXh42iLj9vEo-BKaKWDDJOf1gDeS_UDKaYXvuPMtOMGnoG2nM3OxuUyByS7SoweiGuYd2wYutjQSAxXZifKgZ8b0SuyijcRnXbC4goj017FjNRgmDonYSTHewzrweXNgY9Rs8qd_mlJA0xl4HK-0PMJ5bM8mI4buXVESiEqrO_DyVWPBZVy7-VNLxEWSXLK6W5u617LLHkT3VkNipigTWqGDMlKJ0M5O7-U7TDfAF7aiT1lPT6Zc0ZBnuiplFWpzqVs00ljxiNpvzqNmqbVC5VOpIxUkmIAwuLLmFmogYSr_KSv_P_sFXDyNBagCricd9pn8q2qPEYSu-djGk9x-NCpIjphcqDWvyW3demm_OkzwVvgxGwIFoB0WnYE-N8hoU-L496kNz83d8DYbUhSPQYYQ6_X6yAv9oeC5aZwehrEzEc-eYmMEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6091db717a.mp4?token=iTwHmisAdYWWUue7ocJfGUU8admFDbBCSAqM6-j_bWm47myw1OP1v7szZPakQ4PWCtnkFGJzlbqGW2JKq7leg7h_3vg3ufu7w2CGPyEqKQz0uHIn_doGsAxnz0qXLlxoUojz8lTmzjUCzt1Rkm1B2Bce6UP83dXO5j_cpsPPGvD_nsYe0-VxeaPh3quXN9s6PP-8IyX_wCGqKneJygtlRs3oab2S9cO9YTgBoiaxdDUakZCmuQlKizbXh42iLj9vEo-BKaKWDDJOf1gDeS_UDKaYXvuPMtOMGnoG2nM3OxuUyByS7SoweiGuYd2wYutjQSAxXZifKgZ8b0SuyijcRnXbC4goj017FjNRgmDonYSTHewzrweXNgY9Rs8qd_mlJA0xl4HK-0PMJ5bM8mI4buXVESiEqrO_DyVWPBZVy7-VNLxEWSXLK6W5u617LLHkT3VkNipigTWqGDMlKJ0M5O7-U7TDfAF7aiT1lPT6Zc0ZBnuiplFWpzqVs00ljxiNpvzqNmqbVC5VOpIxUkmIAwuLLmFmogYSr_KSv_P_sFXDyNBagCricd9pn8q2qPEYSu-djGk9x-NCpIjphcqDWvyW3demm_OkzwVvgxGwIFoB0WnYE-N8hoU-L496kNz83d8DYbUhSPQYYQ6_X6yAv9oeC5aZwehrEzEc-eYmMEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇪🇸
درگیری وینیسیوس با آردا گولر در جریان بازی مقابل اسپانیول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/104715" target="_blank">📅 16:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104714">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa2e0d67f9.mp4?token=a7pMYY0SLTpSaQqPBQuUOKhO2GAq5t5P8is6Wso0UQou4iPtakbCUBQZ9bg2AS7F4_sbUL0vB0Fjx6yQ-xhrBVB1RPXluewAD9XcWZ-zogpG-BaoRvq35PLzs4zuVLpzLvtDAzkI3m2TJ6NdBCJaw-b_FB-xI6EVpYuuakNWViFvN_SR56XXyEakx4obkc6dXUUkXbdGHQeewikJgYWeySON5RhY46gsO-XcIrHI2TF9oFBhXpzm4Ho9DckGEpK71ncVJkdFmV7vxSBNPwJFgUGRiWbgci6cnpDwkzA1NzBMvDj9CjzmzaH7z77KTf1Xe9e_rA_PtaIhR3BZLc6Uug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa2e0d67f9.mp4?token=a7pMYY0SLTpSaQqPBQuUOKhO2GAq5t5P8is6Wso0UQou4iPtakbCUBQZ9bg2AS7F4_sbUL0vB0Fjx6yQ-xhrBVB1RPXluewAD9XcWZ-zogpG-BaoRvq35PLzs4zuVLpzLvtDAzkI3m2TJ6NdBCJaw-b_FB-xI6EVpYuuakNWViFvN_SR56XXyEakx4obkc6dXUUkXbdGHQeewikJgYWeySON5RhY46gsO-XcIrHI2TF9oFBhXpzm4Ho9DckGEpK71ncVJkdFmV7vxSBNPwJFgUGRiWbgci6cnpDwkzA1NzBMvDj9CjzmzaH7z77KTf1Xe9e_rA_PtaIhR3BZLc6Uug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
علیرضا فغانی: عملکرد داوران در این‌سه هفته از مسابقات لیگ‌برتر قابل قبول بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/104714" target="_blank">📅 16:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104713">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37b6ede186.mp4?token=Cpo0nnZrkKUvK9fy4vkPpOWg5atzlDSltzadBee-SctUgCzymjPMB6eogw6k1TsufByMM4Gkb05qyU_hVdcVLo-Wy8yqY1NiDLu1sX1aYqgLWP0yb_wPbsY8dyd8LMIi9wApi_j39LsMl3MPSnI_YcH-3z3DffxG5IfE9qpNRcsSGXmGO5WLbnSZ-hNY3gkF4laLlR1VS3acswegXriR8993q9HID_OmfCFfHs74bKej1rF3Ri-3s02gb_Ck7DvavdrjoiOW_8OhK-rwpxlQWQdr7ZIb8bW3LOHSyz8UG8MghH_An1wjOglRSgWvlZSdF3LbUTN3B2cRzvdkk7wz_FVZp3rvZlNow7rXWpVD1WKSqRS8uVdBl_32WHLYHliRjjCc6hK_y6kHrJOOdOfGrgo-a7pzrbqKs5If8AdaLXb0PpeFMhRprkR6d46eB1wpVFI9lCMAERFQU7TCvLxHCCsN19LyWyUHIWsq852OhqlsDWervT6ImmlHO7C3WUrGRe4YWKCjh6fucXtwv0z2D1kxpaRnew_7UGhC8sKC8xaAb8fvtznUlCqK_8eB8XbLcyXdSPCF5pv3LXhWQuM0iIcwK1DdrwToVZyROzU1Ak2k9MLe9tQ-CKKS4JOZGJTODEgV7pm2jTVITQ6QFAMDIT_8Z37_6UVkgnh3BXAM2OM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37b6ede186.mp4?token=Cpo0nnZrkKUvK9fy4vkPpOWg5atzlDSltzadBee-SctUgCzymjPMB6eogw6k1TsufByMM4Gkb05qyU_hVdcVLo-Wy8yqY1NiDLu1sX1aYqgLWP0yb_wPbsY8dyd8LMIi9wApi_j39LsMl3MPSnI_YcH-3z3DffxG5IfE9qpNRcsSGXmGO5WLbnSZ-hNY3gkF4laLlR1VS3acswegXriR8993q9HID_OmfCFfHs74bKej1rF3Ri-3s02gb_Ck7DvavdrjoiOW_8OhK-rwpxlQWQdr7ZIb8bW3LOHSyz8UG8MghH_An1wjOglRSgWvlZSdF3LbUTN3B2cRzvdkk7wz_FVZp3rvZlNow7rXWpVD1WKSqRS8uVdBl_32WHLYHliRjjCc6hK_y6kHrJOOdOfGrgo-a7pzrbqKs5If8AdaLXb0PpeFMhRprkR6d46eB1wpVFI9lCMAERFQU7TCvLxHCCsN19LyWyUHIWsq852OhqlsDWervT6ImmlHO7C3WUrGRe4YWKCjh6fucXtwv0z2D1kxpaRnew_7UGhC8sKC8xaAb8fvtznUlCqK_8eB8XbLcyXdSPCF5pv3LXhWQuM0iIcwK1DdrwToVZyROzU1Ak2k9MLe9tQ-CKKS4JOZGJTODEgV7pm2jTVITQ6QFAMDIT_8Z37_6UVkgnh3BXAM2OM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
🚨
این ویدیو رو نبینی امروزت به فناست :)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104713" target="_blank">📅 16:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104712">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZD3j-0gCXmqOByqZ_kXUTCgb-9NlfqstprttZVkHRSWljjzN4UYyuT4gLCvDm9_Mttwm-c1tVM4tH8A43iEq2faFSZskdB5lUtfcm5Vp-L2XvNjiGXr6sYlA_RavwZwEVi54Lu_l5N3Z3TkmFiay5qAinJY4xcDfWTqZdLK_43Z6ysXsjDGLHD8KHCgBpTrxnuSewmKltmwSA49K45iI-pugM4UfIXp1Rypx-hB_BoEHrSSlu58zNSsxjDFMTQnPt8FF0XVdClXdtbm_EMtQ4UJboxn2In2_VQ-W-8WjiAbBWtT637LazNAv3QRHyhpASZfFf_qP5PDCkTxjx2lhxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇮🇷
🇮🇷
استوری رامین رضاییان و دعوت از هواداران فولاد برای حضور در استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/104712" target="_blank">📅 15:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104711">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
#فوووووری از گستون‌ایدول: آلوارز قراره دست به سیم آخر بزنه و فردا پس‌فردا تمایل خودش برای جدایی از اتلتیکو رو علنی اعلام کنه.‌ منتظر اخبار داغ باشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104711" target="_blank">📅 15:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104710">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQeOTxu5ORcFHhvzVaY_4gGkXAiyPOFD_340D5dDYGwv7eHweE7BdL8yhupxCaibE6ibqJh8cppSAEy1Sk2FxvyQzWs1xlGKpiQzsvEK5i2AH3UnyX0snVp9gOrdsAv_c8d37-WVPGVU-FpeilLKwba6k_0OtORxWDURpes-yYuz_NCU-52W4JB_v13XwpaeJ3h8FegmdrSSsWDjBXRxBMgUbxI_gFPIr1O71h8P2wah3RiQKV77BMGtIpuF8NHFKGejnKAc_1zAf4LGOoPYm_5PMNs5PkDCkvGI5kSp-NcFFVH51Na7IdvDyeajxOLK2MwiTa-KOJ_l6748RbgURw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: مذاکرات دو تیم لیورپول و کريستال‌پالاس بر سر اسماعیل‌سار به رقم ۵۸ میلیون پوند آغاز شده و احتمال زیاد بزودی شاهد حضور سار در آنفیلد خواهیم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104710" target="_blank">📅 15:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104709">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaMd0i6Rhuid1S50RJAJ1QD7LtMKlPN9oXrlAXDzArGsvSUHnBco8InNiSKlfiQcbh0a2nR6YhwcnMMf13w-2iWvurVdOgKml4TWNz1tvMCxJ9n2AUuKVMqeBBAQAtdlxNs42H9fi2lminUVIPfM-18i2sizK-UuGn-OAwiHIllkrVblpsE8ySOSk6GJNll-wFO3l3pEqyN2qJgB4l9hrTovfbizT3HV6ESWD9QpX97VBcPLN2vW5upKRzwAr2qxNgFjDEC3RJcmJ4kEaC58o0_ChdgvqYTZkkK4Hq-4ecjR_5Y0CCx6DoNK3GHcugxN3e5k8sOcmE_pkGFYN_mGDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✅
بدلیل اقدامات مالشانه هادی‌چوپان در ایام اخیر، ایالات متحده آمریکا ویزای این شخص رو برای حضور در مسترالمیپا صادر نکرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104709" target="_blank">📅 15:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104708">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYMjNsiwYcRU6AU8v6qiEOqodu99WGgWG3bnEPdVW0hMGllrTKffdzvJzfQ_54omvb3SsDQHa8ZntCMuz_Lh9lSk37zsy-1sWE_IRIt3xAbwtnVMy-i1PCJCMtCeFetNj_HZln4ttUaV4KPYqfTXxJ2goNkuGtwBGr9x9-wsHrA45IeYucmGLaXlRZYxN-71FlrWI9qB8GpfaqH2xUBl5R3nGxM7WCtdO9-yhLcLq12L4GcuhXMv4ecqtEMMYgKtYVaGSU8MZejJYSPFBEs3OpH5h5v_b_-4GTw-SZxdgMkAg9bhBiBybBPJ9QRpIeywNQ2KCUQ-3dIUrSCLh9-dPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
عذرخواهی عارف حاجی‌عیدی از هواداران استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104708" target="_blank">📅 15:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104707">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1136d451.mp4?token=CbHWIwe0xyMn_DgEWgfBQ75xmd7aV0T9ipEzMH4vxx8qkHzmi7eZZWs0cqOniGcstx4XOBivFsDJu8I_jdCELT3UYs8VXZK8_XJjdH3L7-_wTc30F3PXyrhQpuDxmkaJ4VNbOk-kYCMo5924crANNU-59nXWMuAsjCr2aepHA5FWX2F_BAtG_1VKTWS4YFyWUAfwXAIETB4WLMNjA5ZVlHv--VQ7n3-sDMG1pleUkbYXZDDbPLUpmhL2bEp3WiAkfP2TgqftRkUKaiPHaWNft7Z7gQdQDrgjVK-cCpp0AfuIJvWM3OwjMvkAs5onLLJLtAsqQ5IQg_9oY0aC4vyV0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1136d451.mp4?token=CbHWIwe0xyMn_DgEWgfBQ75xmd7aV0T9ipEzMH4vxx8qkHzmi7eZZWs0cqOniGcstx4XOBivFsDJu8I_jdCELT3UYs8VXZK8_XJjdH3L7-_wTc30F3PXyrhQpuDxmkaJ4VNbOk-kYCMo5924crANNU-59nXWMuAsjCr2aepHA5FWX2F_BAtG_1VKTWS4YFyWUAfwXAIETB4WLMNjA5ZVlHv--VQ7n3-sDMG1pleUkbYXZDDbPLUpmhL2bEp3WiAkfP2TgqftRkUKaiPHaWNft7Z7gQdQDrgjVK-cCpp0AfuIJvWM3OwjMvkAs5onLLJLtAsqQ5IQg_9oY0aC4vyV0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇮🇷
آنالیز حرکات خاص یاسر‌آسانی برای دور زدن مدافعان سپاهان و گلزنی در بازی قبلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104707" target="_blank">📅 14:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104706">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f87467034f.mp4?token=U9m6Ve8uXLOklQETj5O3XwuoPKpv5_C9BdAABFUZOd0QkPVHS3NJ3rVPoUk5S0N7lwMafi5U6jbCdopdgOYWfpSKab4C8RVgMyRB9dWsLTVvkyvVLOsPXACL26x0vG042r0_-FmI8VlneRXpbILDIpiYcG6Xd-4z06jT3W2r5V0ubcByQj8zArdO32vYb-30L8kWpsKfsYfqxpOKy5ZC3VifLerbb0wOLuwlSxsmTsUUU-IcRdgj6Pqa6Vlw338hnMTSEmZ5q_YgPqy06cPMu9rY-m0bsFxzAip15L9elaSxheFDvOtuHsxcLZj-2okaVr8tGNP96_flJ-Y4WAASRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f87467034f.mp4?token=U9m6Ve8uXLOklQETj5O3XwuoPKpv5_C9BdAABFUZOd0QkPVHS3NJ3rVPoUk5S0N7lwMafi5U6jbCdopdgOYWfpSKab4C8RVgMyRB9dWsLTVvkyvVLOsPXACL26x0vG042r0_-FmI8VlneRXpbILDIpiYcG6Xd-4z06jT3W2r5V0ubcByQj8zArdO32vYb-30L8kWpsKfsYfqxpOKy5ZC3VifLerbb0wOLuwlSxsmTsUUU-IcRdgj6Pqa6Vlw338hnMTSEmZ5q_YgPqy06cPMu9rY-m0bsFxzAip15L9elaSxheFDvOtuHsxcLZj-2okaVr8tGNP96_flJ-Y4WAASRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
سردار آزمون به تیم ملی بازمی گردد؟
🎙
فاطمه مهاجرانی سخنگوی دولت در یک مصاحبه جدید از تلاش های خود مبنی بر بازگرداندن سردار آزمون به تیم ملی خبر داد و گفت:  سردار آزمون فرزند این کشور است و اگر خطایی کرده نباید از خانه بیرونش کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/104706" target="_blank">📅 14:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104705">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BA2bPmOpe3_aJPKVmiW1QHz9PsiNBpwToRLHy-EtI0DeT7WGGwXLIoU_K-6SdPaNL3C367D_DIivNObkMh0njWohR3d2PU3e5XzApbNlWtY_j6-pzuTsrR5PaqK7BM17rgmMidyewvuVzY_txsBHbh387qNnMQEcrOgbZoM_uW75EnwTgNkHMHi_VgeJsyP85PzXaRNpWaO2-08sJdtUzlLH22-VDDpeeBRffaai-qFxzm8JOz3ONlwfC_6Tc5z9wsOHK2RZN1cOvwtphCNnacHxD09vpWymNVC2SF2uIxIEddFom3Nt0XJs7JbSTSiOZKHShhLADxm6bLjzJE-VVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🤯
🏴󠁧󠁢󠁥󠁮󠁧󠁿
در اتفاقی عجیب دومینک‌سوبوسلای تمام پنالتی‌های خودش رو به سمت چپ و بالای دروازه زده و با این وجود هیچ گلری نتونسته توپش رو بگیره و دوتا پنالتی که خراب کرده هم به تیرک خورده!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104705" target="_blank">📅 14:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104704">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635ed4f4de.mp4?token=eR0TzBm2ekmnr8D9mHMp7Or48sIQe0CqksjMq5CG2At5eMs457YlMSuUw0YjG2jJvfr8O0elu_xnfNATMAq9EsdYby_kwNBSK7T3UmfqlE061YW8pQH7bDCOSHmgZzWT7mfkMq74AmVIbB5rqAYlpFZoP9TCt283SE6aCBu4QrnQQH17bwvgWDggMCxXTxNmwNP3Udcdmhp5ZRTE7DANgCqtQ9QZHkfLmc5kkV6NyLL7m2o69I4JiwSXztWlyO4VO2FtNx7beNZyg1s3BE6EbsqFZPo2JXYhFODaR0W56z6mHtPM2cAOjsECYPZIVKkt7QwsHULUbOjZRyB6qWgS9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635ed4f4de.mp4?token=eR0TzBm2ekmnr8D9mHMp7Or48sIQe0CqksjMq5CG2At5eMs457YlMSuUw0YjG2jJvfr8O0elu_xnfNATMAq9EsdYby_kwNBSK7T3UmfqlE061YW8pQH7bDCOSHmgZzWT7mfkMq74AmVIbB5rqAYlpFZoP9TCt283SE6aCBu4QrnQQH17bwvgWDggMCxXTxNmwNP3Udcdmhp5ZRTE7DANgCqtQ9QZHkfLmc5kkV6NyLL7m2o69I4JiwSXztWlyO4VO2FtNx7beNZyg1s3BE6EbsqFZPo2JXYhFODaR0W56z6mHtPM2cAOjsECYPZIVKkt7QwsHULUbOjZRyB6qWgS9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
شور و هیجان بالای گزارشگر خانم لیگ‌آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104704" target="_blank">📅 13:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104703">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e638c7d28e.mp4?token=HQi_TlPqHRwewkIXVSnWtNkduzb9F38j671dv2imvp65_d-_rMm55knIPoFz1dez7DMUMZxnJmCkJHxnv0XYLSiX1nEc0q576Z4KA6aRtzrt7ap4TbDcej9baV8qCOVXoan1Isq9dcZ4h072HgoZbOFlbXODRz_mSeAux6hmaE6VU5wCYjP2w06NbMUtx86FbFkpd6lT2q0zZB53sUx5ES6xnR4EKfL7ykGMWgQfHiDX8MebQyORCYFlx5ej1Jh4rdqVDQT8Cnrq8BpfeD3ttYSPd-ZeqbcfIheY-dtg2uYL2d1rFj6sQjMfUnkVcwgjGMeCOtwcWgeVwkND0vI8Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e638c7d28e.mp4?token=HQi_TlPqHRwewkIXVSnWtNkduzb9F38j671dv2imvp65_d-_rMm55knIPoFz1dez7DMUMZxnJmCkJHxnv0XYLSiX1nEc0q576Z4KA6aRtzrt7ap4TbDcej9baV8qCOVXoan1Isq9dcZ4h072HgoZbOFlbXODRz_mSeAux6hmaE6VU5wCYjP2w06NbMUtx86FbFkpd6lT2q0zZB53sUx5ES6xnR4EKfL7ykGMWgQfHiDX8MebQyORCYFlx5ej1Jh4rdqVDQT8Cnrq8BpfeD3ttYSPd-ZeqbcfIheY-dtg2uYL2d1rFj6sQjMfUnkVcwgjGMeCOtwcWgeVwkND0vI8Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدون شرح
❤️‍🩹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104703" target="_blank">📅 13:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104702">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chCVwnWmDd99iXRNyinDI0r1rJ34Xvr9FOD3eX58rEOiogRdhC9SSEQtEHodg0SLKSc635jOLFeubDswgnGWOLHw0wzs6pcuN5SrZAXe5mvaf4hXehsaC8lBlGN11AdQbAdhGiCnv5fRZeY2sv8yRQHtXraV4nwLUAtcrwL1nQYIni_g70MVMAobpvecypM6w3rf4s6cbMuuFsmAeIrHVPIbXVTNOZUnUS1brhkJgfkje50tyyZ0DiB41YcfmcTjXakLOOZouXBjKs3nEcNa18ziWh8BOxlzBAT081vDmZ3Va4QwmPrz_tzhC5aNDpYBvtmzFp9xEx_a6Pv6UnsBNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
#رسمیییییی
؛ قرارداد اردشیر قلعه‌نویی تا پایان جام‌ملت‌های آسیا تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104702" target="_blank">📅 12:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104701">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🇪🇸
صحنه عجیب از کتک‌خوردن خشن هوادار الچه توسط پلیس اسپانیا در بازی اخیر مقابل بارسا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/104701" target="_blank">📅 12:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104700">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f195b85bac.mp4?token=Q4ruGs19cozHJj5MGExbrh64nQclo3aItXu6r6KBfVQO3HIxsoyaZr35dYKXCAs56um7lIn6b6ZVDenGRUt6eFBps6N03HVLIAZ0leQBZ_PAT7h4Hx-Wuhw3bazpjvyCe3kV1TGQ0RGfaP9wH9_mXv1xWy36J-oOVZYjjCNEcWAgz0nh4S7S8FRryi7u_6FrR91cTyZS3by5u-S8hg6qe7k9ZQEHWFPIC_u1yifemXLbuJNyyjTZkb4LZusrag1yQEbJnmlJHX5XBtg49_qJWXTQ1lVIwBr8PzQBL_x2ClM0j_MWzI3h2CJPfNhY4cvN4Pufuu5VmV3ZojUyTuU7WLhPdBIEUi5IxUkzLlEgaQghIdvH60l5Wszgwwd4Cow2QnBr-4sGx-J0hGBWgUAoyCHTYhenbrFzgSEwJ-x9o94JVQD6LTz9u96yhnosbkttLSMPtNpFUQ3fzPEk27qc2F8QTLyn1tIhswpBDYGRRdBHvvb-1Ze51atApIGAAYMZs3QPdXrdgPhRuy3LjwU6jy5kal1lKyh4bgOzOyn7YL_IsTYFckG_61QBhYHHb1yxwfJTZnHt7a4i4o3CvimceqbWdX-NKJmODbb82qNQNxw56GhCTT6MCljBW0XQAn7Oye39hT767a-dzJkNHrs2NwopbhXrjdOPz7PxGmoPQU0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f195b85bac.mp4?token=Q4ruGs19cozHJj5MGExbrh64nQclo3aItXu6r6KBfVQO3HIxsoyaZr35dYKXCAs56um7lIn6b6ZVDenGRUt6eFBps6N03HVLIAZ0leQBZ_PAT7h4Hx-Wuhw3bazpjvyCe3kV1TGQ0RGfaP9wH9_mXv1xWy36J-oOVZYjjCNEcWAgz0nh4S7S8FRryi7u_6FrR91cTyZS3by5u-S8hg6qe7k9ZQEHWFPIC_u1yifemXLbuJNyyjTZkb4LZusrag1yQEbJnmlJHX5XBtg49_qJWXTQ1lVIwBr8PzQBL_x2ClM0j_MWzI3h2CJPfNhY4cvN4Pufuu5VmV3ZojUyTuU7WLhPdBIEUi5IxUkzLlEgaQghIdvH60l5Wszgwwd4Cow2QnBr-4sGx-J0hGBWgUAoyCHTYhenbrFzgSEwJ-x9o94JVQD6LTz9u96yhnosbkttLSMPtNpFUQ3fzPEk27qc2F8QTLyn1tIhswpBDYGRRdBHvvb-1Ze51atApIGAAYMZs3QPdXrdgPhRuy3LjwU6jy5kal1lKyh4bgOzOyn7YL_IsTYFckG_61QBhYHHb1yxwfJTZnHt7a4i4o3CvimceqbWdX-NKJmODbb82qNQNxw56GhCTT6MCljBW0XQAn7Oye39hT767a-dzJkNHrs2NwopbhXrjdOPz7PxGmoPQU0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
امروز 4 شهریور، روز بزرگداشت نمادین کوروش بزرگه.
🔴
هیچ منبع تاریخی دقیقاً نگفته کوروش بزرگ کی به دنیا اومده، فقط حدود سالش معلومه؛چهارم شهریور رو آدمای امروز، مخصوصاً کسایی که به تاریخ باستان علاقه دارن، به شکل نمادین به اسم تولد کوروش بزرگ گذاشتن
🔴
دلیلش هم اینه که ماه شهریور توی تقویم باستانی نشونه قدرت و فرمانروایی بوده، واسه همین گفتن خب چه روزی بهتر از این واسه کوروش بزرگ
🔴
پس در واقع چهارم شهریور تاریخ واقعی زادروز کوروش بزرگ نیست، بیشتر یه جور روز نمادین و فرهنگی برای بزرگداشت این قهرمان ملی تاریخ ایرانه
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/104700" target="_blank">📅 12:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104699">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTNNN0dJ14e-tIMvdhwwZeWHAo-Q0ogFb5hNxpqc3Dx5DiBmyG5SrwiDvljISbvUgmq4S_0Ip_LuPFpr3NLgWtQPV1VJppPRDWnqXkLCs6IRdEzOgl_9D6528gqvNOqo78YqTJHknbGJG1oeLbbSyxLbOn4Yoo3z2H0gdBAP4ixEeuKa30ALLzfyZJ1SD92_gHEif3lsB0Pm3c9KOgEW7r7tGLzOgfEmxqUMtywmVk0TPHLv1JbZAICQjQQ1KMZ7x6sl9tlhwfOuMjysC-KuGbAQ8Sp62QEUgFFUQakKNQ2nziKHXqFREdpfbJIJuNfLCV9w0BzqjDfCytN60gE7-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رونمایی از توپ‌فصل‌آینده لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104699" target="_blank">📅 11:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104698">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P50JFLoGv862rZPxklnzgqK5_xuCWsc3hpDseo_raC2xHVwPy3pZ_p0NkZn9frJexi7dBs53TR1sGwQ6TnSYS6X_fHQ5pA_e7YgN9waLc2ilckHsbF85spziZeVNklsXBVbO37xJpN_r0-ZPQD3C-8ndoyQ7_FwQ-QoMSr3qaKFVN3ZHZGC6I67NSDosVDV0OBrv8ZV34bBU3jgSoYP02CF6crCphojWB9-mTSAbEf0GkndvKzk1KLLbMBOdl6kd4Y8c-lRlI_L2Rae3god6DadaywB2wNVJcB8JazRXdINBMvgDNdIoSsY6nnHVY9umHQdthuDpkZmlid2bXxJyNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
منابع خبری اسپانیا: خولیان الوارز با تیم اتلتیکو تمرین نمیکنه
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/104698" target="_blank">📅 11:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104697">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jx2VITk8BX2yM8dTacZa2eZfjqn5aRkhWzNy6r4Aj_IE5YOGwhIW6KYHX8sCpH1NQrzpT8lthehJzmUK-HjymSMecEWyzbegqbIYaPYYze_ltDHVWId2l1sbiszISh2pIColv49v_Mc8oTEnKnU0J-4F2r2SfGlMh_mIRvVd5T2kRCrR5JtAhyCCxfcvN3ERNAu-Szvq-xlQccevJOXNN_KpQal3NU1CA7Wg72odHDoUl9SSLVVCZKyftZOoRutjCaPF627ejvb-Z2XWIMCue6Cju1P3cmJTwK1HnMAXbhQItea0gORjl5aPAyjoSSfs3ZNZSxZ1qsnBoRNTxIbQMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
کنان‌یلدیز ستاره تیم‌ فوتبال یوونتوس بدلیل مصدومیت ۳ ماه از میادین دور خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104697" target="_blank">📅 11:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104696">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290e961780.mp4?token=IzTDlAhIqBjrBg8u-HEzBIAL_GfuNEW7fO7UbB5WbFxSt8TmKN16QJL_K-HV-WJMSFD13R7Rw5Yy4QPINTDCR1Z4F6XUsH2BVKLNtJP9FyFvP-Q8CRAl3UQEllQU1vvrTrp-OYDmH8CtLVBfslmJmqLiF93dbY30j7yP5_ortnk6TBGn8JM3h4KKa8h98_4xZnC7gzNwcSpVkqTqAHgWaex5UaC2AquIJ9w5Pd27ItszTZrnURlye2O0kcLjzr_89DBsVEqfvsAkD7v0gJHP96n279j-nkQiJK-we_VrvN4xMiIqvoFZxx-aM0SwnLUXrmsiTzMZyCm9suM5m_d7zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290e961780.mp4?token=IzTDlAhIqBjrBg8u-HEzBIAL_GfuNEW7fO7UbB5WbFxSt8TmKN16QJL_K-HV-WJMSFD13R7Rw5Yy4QPINTDCR1Z4F6XUsH2BVKLNtJP9FyFvP-Q8CRAl3UQEllQU1vvrTrp-OYDmH8CtLVBfslmJmqLiF93dbY30j7yP5_ortnk6TBGn8JM3h4KKa8h98_4xZnC7gzNwcSpVkqTqAHgWaex5UaC2AquIJ9w5Pd27ItszTZrnURlye2O0kcLjzr_89DBsVEqfvsAkD7v0gJHP96n279j-nkQiJK-we_VrvN4xMiIqvoFZxx-aM0SwnLUXrmsiTzMZyCm9suM5m_d7zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚠️
تفاوت آزادی بیان در ایران و استرالیا‌ از زبان اسطوره داوری دنیا علیرضا فغانی
وقتی مجری از او درباره فیلترینگ فوتبال ۳۶۰ به‌دلیل انتقاد سؤال می‌کند، پاسخ علیرضا فغانی شنیدنی است.⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/104696" target="_blank">📅 11:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104695">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/104695" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/104695" target="_blank">📅 11:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104694">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gl4FUyyLAbA3PaQ84IJGkzPL_phsCJ47hM1I5FWqf3fcuv18ITPve9bGYo3qOVDaCNKcPSabiAZdLQutG_7b6q_LmO6d6Fafdo59nix8lBHIbrxeXvzi1-RcOT2o_vcpwxHBicuS2Zza3Cy7o8wd7MWTj-F9A9WD1Wb0HhtqwBfXt8NPZvYMrenLs4TG6YIxdFNUG5e5Qy0lnfRa9Tw-04_VpKJ-YAcEOSjWTxVFMS2Um4iNoIZ0dF_Hs-PFZ3xUr6fUkG3xdosS20lZXQU8blepC_PSBbRRSjUy7EPLbpcB5xemtDpUeJ9aAIEZweqWsod3WvtjMbdVco4G6BS4xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r4
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/104694" target="_blank">📅 11:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104693">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb7772379.mp4?token=bHdPmFMrNlPYsnEKIo1np5obuog1Xah9D_A9zpfezBtIqhiUA1N2Y2ZdN0aO9LTVE4G5wYcOvUA8bNSgOFNcqIgcG6-m6KAS4Iyb2aqCEH5Kni_Ehd2SlYDUHNFNfXKFHz-JJusrfdVSeywf2WOMaceKiLRNNKaWUdZ9Lizkt-wzrXHwQzb4S96vieXg_RbMZ5-XD4lAi9gsc0HPs2gLGM9w1krTg8ODxO5d-VvoTZrC_jkoSCUExcPdRczqXNc7Rtkv2m8dDp-_1IUEj6gon67GUi4bFEXyNlxhl1Pb4p_C-haid7tvOVRbgIZWV3oS5sk83pbtDLT34Qh7ZyRw0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb7772379.mp4?token=bHdPmFMrNlPYsnEKIo1np5obuog1Xah9D_A9zpfezBtIqhiUA1N2Y2ZdN0aO9LTVE4G5wYcOvUA8bNSgOFNcqIgcG6-m6KAS4Iyb2aqCEH5Kni_Ehd2SlYDUHNFNfXKFHz-JJusrfdVSeywf2WOMaceKiLRNNKaWUdZ9Lizkt-wzrXHwQzb4S96vieXg_RbMZ5-XD4lAi9gsc0HPs2gLGM9w1krTg8ODxO5d-VvoTZrC_jkoSCUExcPdRczqXNc7Rtkv2m8dDp-_1IUEj6gon67GUi4bFEXyNlxhl1Pb4p_C-haid7tvOVRbgIZWV3oS5sk83pbtDLT34Qh7ZyRw0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ژاوی هرناندز در اولین کنفرانس مطبوعاتی به عنوان سرمربی تیم ملی هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/104693" target="_blank">📅 11:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104692">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fdf3f04ed.mp4?token=vFuQWSqrlpd6vhhOQLssh37KGlt5qLIfzBnWvQ2OW9Y58A03BEE7vtNmB4-b_ueiZyYGvKw6MAWZndoLB48cB0GBdyzrCaw2_NUaQAGf3iu7wCqFdYy4xt4IPVH6RYKSR6Tsc-PXVxYqoLbebNVemEeQL2gCfnp8hvve9P3Msw2IOyUciL04RQMActCdMI1Zhh-3G65CY4XFqGvFGm0PWmg6SgSGFM6r2BgChGnpgs4SUjvGAdlt99467XXlmUXH-YMT7atWnJDplJb_R-QXvRiQcCFUfas4RhQsgVTxS5VP8mDlY7HglLqmQVM6AtOddtHuBNG6SxfCqOelkqItiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fdf3f04ed.mp4?token=vFuQWSqrlpd6vhhOQLssh37KGlt5qLIfzBnWvQ2OW9Y58A03BEE7vtNmB4-b_ueiZyYGvKw6MAWZndoLB48cB0GBdyzrCaw2_NUaQAGf3iu7wCqFdYy4xt4IPVH6RYKSR6Tsc-PXVxYqoLbebNVemEeQL2gCfnp8hvve9P3Msw2IOyUciL04RQMActCdMI1Zhh-3G65CY4XFqGvFGm0PWmg6SgSGFM6r2BgChGnpgs4SUjvGAdlt99467XXlmUXH-YMT7atWnJDplJb_R-QXvRiQcCFUfas4RhQsgVTxS5VP8mDlY7HglLqmQVM6AtOddtHuBNG6SxfCqOelkqItiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلنگر و صحبت های جالب انریکه درباره رفتارهای دمبله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104692" target="_blank">📅 10:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104691">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mboyftFkAB2MmapyYujar8KYgt9Q5au2acjqE2eUjlK5QaytAkLgHhLG7bmR1OVioSagR1Irwi_WoEROWVXDm2BWwLezWjkkwRXpucO1WTm82B8Uz28eWhHTyPklEphzJW7zXq7eQylu-ly_TkA_ejUP17IBsrdOsSfiUs6jUHGmZt6hYOpvbDyc7QumE1Ituj7i6Pi7LDQDcd9LWC3FK7xDPsXJyvtyk6at5pi96mV88zlHeyIgrxpnKQUewzbH6YyDh7Zluji41_Z4QXk483JYxB0fKdhdC5slPO7cOFwG0e7YkKIim1QJwpYiK9uSOC-Vo1t732DPyLeDGwJMhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
اعلام اسامی داوران هفته چهارم لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104691" target="_blank">📅 10:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104690">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521128dbfe.mp4?token=SlT2HTMBHGKQ5ByOlg1oky-nv5m5MfbzXT0vaeVeEy4x9FY1kRH-fFIiMiOkCI5S1H-oMCyP9GxB8k5kGdkI3diBOGsU5eTrmeKQ7doo_bM9cZJDDFPQqN9Z-jLSILWQgw1-gL4oI6DiDPROyh6bKLh6v25RraR37Ao246YD6I3p1-qa88fvm0tBIi3KyrrUxZmRoi50p9noHg8z_zBQwQ0amyPjMcF3jjvarpcN6oScpbwwRiVPmD5QtmLhquIIfFZ0BrLpbUfYnPm72CM43FZ4FcUdnnHTutWBTbR-jCs0N4GNWEwCW6wenL1lx25AOCnybHJmXShk7JKMVuPgoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521128dbfe.mp4?token=SlT2HTMBHGKQ5ByOlg1oky-nv5m5MfbzXT0vaeVeEy4x9FY1kRH-fFIiMiOkCI5S1H-oMCyP9GxB8k5kGdkI3diBOGsU5eTrmeKQ7doo_bM9cZJDDFPQqN9Z-jLSILWQgw1-gL4oI6DiDPROyh6bKLh6v25RraR37Ao246YD6I3p1-qa88fvm0tBIi3KyrrUxZmRoi50p9noHg8z_zBQwQ0amyPjMcF3jjvarpcN6oScpbwwRiVPmD5QtmLhquIIfFZ0BrLpbUfYnPm72CM43FZ4FcUdnnHTutWBTbR-jCs0N4GNWEwCW6wenL1lx25AOCnybHJmXShk7JKMVuPgoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حشمت مهاجرانی سرمربی تاریخ‌ساز فوتبال ایران، به ثمر رسیدن اولین گل تاریخ ایران در جام‌‌های جهانی رو با روشن کردن یه سیگار جشن گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104690" target="_blank">📅 09:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104689">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUjFa_nhPl0y1wtJt-YjXcW1e1_ou4pJnYcY42lH44EW3a_opbcVwZxXPV2ojE4sA4oiP9plLHm8fdEE2nBF3ajJHBZFIr5UnYGVLQIpMDZRbjIU9v9rCjc8qFg7frsmZvCwkG-64xjhbXtyrWFRUQwrTyZiYiF_6vZTf-9Y-AA8V5ZttiWSAN-1YgzSKjH2DRfl0Q2-g-_3Ay7SduK47r2Ke2kC34yDqSvbgtQ3B1GdRT2OrZKM-8IqAbq8G_N0mZEoUZhZVuLzhRN0JrCnf-PODNIcQl0pw9PRmlJgXWzzF9ldGrj0iaqtUKNpM7AdYejdahZkH2dSWri3HOeAcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
📊
محمد صلاح در دوران فوتبالش در تمامی ۹۰ دقیقه مسابقات گلزنی کرده بجز در دقیقه ۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/104689" target="_blank">📅 09:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104688">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fdb56b243.mp4?token=JeyV-8m1SU5npC5Mrbi_eJVouYkBDtgteJwrjpdqynmfbxLiKxLo_CI9CmNlMg582Zq1uUWF8BlpUR7yaSeocorm1RUvbRlXgdoC48r3k2L8XoTheOwS6HNZma3zU9jkvT_RhUpevrD5ukWiX1-lNbvWjKy1UFPOCevU62_JRDyT2xsdLL-vkvCUUPOGCB8cAfO1efX-0r0xjszql0sdOcr8z9A_ybQFdVP3jAohyGKpJWJzbIs6dNnRoFh_jO3KWQNM_KwCjCg8o874X2zVBLoHzZBrvHhAEBQIFhxGwrH6ZBmFwf0UREyBoUROVB-8tDnn0A6ElPIRfEJ9CNejTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fdb56b243.mp4?token=JeyV-8m1SU5npC5Mrbi_eJVouYkBDtgteJwrjpdqynmfbxLiKxLo_CI9CmNlMg582Zq1uUWF8BlpUR7yaSeocorm1RUvbRlXgdoC48r3k2L8XoTheOwS6HNZma3zU9jkvT_RhUpevrD5ukWiX1-lNbvWjKy1UFPOCevU62_JRDyT2xsdLL-vkvCUUPOGCB8cAfO1efX-0r0xjszql0sdOcr8z9A_ybQFdVP3jAohyGKpJWJzbIs6dNnRoFh_jO3KWQNM_KwCjCg8o874X2zVBLoHzZBrvHhAEBQIFhxGwrH6ZBmFwf0UREyBoUROVB-8tDnn0A6ElPIRfEJ9CNejTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‏
✅
نخستین تیزر رسمی از سریال مرد سه هزار چهره به کارگردانی مهران مدیری منتشر شد. این سریال بزودی از شبکه‌سه پخش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/104688" target="_blank">📅 09:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104687">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vc3iDqooVvg0lUxuI44IHZNS3gRgkzFHEXc8fw2V4BxCBNFLqbbi82F3gQCMO1ySGudc0Po7ZdEmuzzd18ya0PcexBmM11iQKzCiZQRLEn5z3grL5A8NfDSsu4OyKPfUCo8xsd-1XpKNSjxsO4AEQD8HayAgirkd7zSiR8F57BCdfa7jfnufHgFEirYURxlwd6uvtUhLnW2Oh0YvMq3fis2I9o5NKr85cxdtqHYcmtDnfLx-nGmoVENLjdyjJ9hpk2FkI-ZsbqvSsgjccDftEbzrJA8mef9dsLAoLvUog3I8wKkB57Q8VAmQxNZTzABy4U14P3J4x0SYFBcNLV2t8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق‌گفته برخی منابع خبری، باشگاه منچستریونایتد قصد داره در ساعات پایانی نقل‌وانتقالات برای جذب کاماوینگا از رئال رقم ۵۰ میلیون یورو پیشنهاد بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/104687" target="_blank">📅 02:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104686">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9Asge-nTTolWNm-xedKt15l5TMkTTy9tSuERmizg6kApM5bWPGxjSSOS6eFqHrN80dYvcPYmwqkJHRephYpWN9G_Z9mI6CAm4Xj2Io-9P5JOMayfGgAyv81yC8yZceHI7aun3pfmAPQcuTQz7vCEnRMU_BP9aHnSsEsGt6uzCvpGrDA8bBAjBtlH141dM2HYPkaH3JB4BrWkCgKigPiwDjJyuf7TqWVLScD9CwZCMf1rdXkSLu23Fbb3ymcEvqoJGex5FUjsoXNxlyvpH3G2zYicPsQzrMRqcOhXkyO8691Mr_faBg4NaFXRgX9lKLug_o7xDC9E5U95pEAI2BR4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇦🇹
تیم‌لاسک‌اتریش که در بازی رفت سه بر صفر از سلتیک‌ باخته‌بود، امشب تو یه کامبک سوپر تونست ۵ بر ۱ برنده بشه و در مجموع به مرحله گروهی لیگ‌قهرمانان اروپا صعود کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/104686" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104685">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pF2sseF8Ra6wMztQNxby2apjMAuzfGbIU5AuFooMhz9QM4rAQtokdNX1oScsl-dwUw4PBmlRsMDHuwytgkmfJ647Y7nZAT41C_CypVFEiHqcm0cZYG1ldr8V536y284Hh57yIIN_hz_bUgt8P2Ul-D01kQQ01cNhZuH5dwgSJUEqVkmG1D1AEp2Gu5jYU_wm02Bf-8wx-D0zxZTW_kMAXk-UGeoPgWnmavIO9SxpacZODJ6A_SZivPI_HFqD9VYXlZw0cuDlm0B--vEh-u9TNbcIRo3MKT2VErgxf5g3rvxdSUMlivM7ge5MB_x1Z18WtCizB7RNbYwBQsH8toTpvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارسلونا ۱۵۰ میلیون یورو دست به نقد ایستاده که آلوارز رو بگیره بعد خیل‌مارین مادرقحبه نمیذاره آلوارز جدا بشه. حالا اتلتیکو باید بمونه و یه تیم ناقص و‌ آلوارزی که دروازه‌خالی هم احتمالا به زور براشون گل بزنه
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/104685" target="_blank">📅 01:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104684">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JV8BOiRq_uWlW7B6BWU0ri7zz2Io5ecTIq6uL4Zi42T3dNWST82xVtt-hN7I8sC_sS4m7vPhRICU1i_OeA1IlzwBSbvercjx5VvnOWz5b3H1suKPyg81uGEJAzuXK8MGpWpZZ5HlXKI_Va7Lp4bQ3VKKdJQqA1ZrlJTkxQ_vJLAWH9JdvCh2jJ1B9NXs4ZfGQpELOYzcPsyAka3B1svot6qx8uT5qBb2pkuKTOTxUVS-w49VyTKty7gpN2gKZvKV3fD5o261la4CVf8Fknak5rPWWPiJ6k2ixI6byt9OqUCwXU6zlR_x6JKd0B_Gx8eXTXbr5L_ooV_rwBeIZeR-4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇳🇴
باشگاه بودو گلیمت نروژ با برتری قاطع مقابل حریفش راهی دور گروهی UCL شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/104684" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104683">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lARqTj9eGD5FsD8cjZxrFytxUSnfKTHQ3WlzpDBBvNHWodUZUB00JRKcE26wxfxbYa9t45VFGjRfYrbMGrhoXLHFxAxUIoIoC2KUSFMd3yV1k0NAo4LUABJT4kMroWYO1-p0lnoUmRybAE4yEiRC3SChsc8Ug78wrfcPChwcTDz0vj-vKdHeH_cb7KDsenRFeDG4pr6zMv_ZWOYY-fRH4LvxSeXtcMw485pXgtXUowkdQoIghir5RZ-Xyv1u-LLsC1u3GTnJiQE0u4wFcwAXqQCJ_qdTaMMi9yPbEz6Vo9dJaGVY6-J_rSx5QgX6JstWYXeKH4u_Rlv-T677LWoCFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
✍️
اتلتیکو مادرید نتوانست با تیجانی ریندرز قرارداد ببندد، زیرا شرایط مالی دشواری در این باشگاه وجود داشت.  ‏
🎙
پدر تیجانی ریندرز:
🔻
‏"ما امیدوار بودیم که با اتلتیکو مادرید همکاری کنیم و دو پیشنهاد باشگاه القادسیه را رد کردیم. آن‌ها بسیار علاقه‌مند بودند،…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/104683" target="_blank">📅 00:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104681">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpoGuZyHvz9Mq7iJHhOxBUP7PJzZ99LvXdz4PwqKQplvCbmaCJ1nNR2XyYUYzjjJ3B8ZGaSRdTWBLZHztWYtiE982aI7MvV1qyTHZxdCyn_r4jY4A4KPDcMRiwM0NZyxgiSmiMutwxrn4yj4o4eVGvJpcKFRDcZrdDd7QVCPjO8KJdeuenL8Dpjm3wIadZ9HwJ9TuuYLlWPmMY18O_StRuXouRn9_p0bErTsvuGF3hV82H8rBS6RDHyuYIigHAhUUvldqnmGJgv0r9gYi08kTP88G3o5jkShkpplNRSY5B_sMb6eK-JlDVQTnREAiP4Pp0DKzM5bFk3_pVpC_5h_uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇸🇦
رومانو: اولی واتکینز قطعا از تیم استون‌ویلا به الهلال خواهد پیوست و مارتینلی هم بعد جدایی قریب‌الوقوع از آرسنال در یک قدمی حضور در تیم اینزاگی قرار داره
!
گمونم خدا به تیم‌های ایرانی اساسی حال داده که قرار نیست با الهلال فعلا بازی کنن
😢
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/104681" target="_blank">📅 00:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104680">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTFBRZxz9QZL-UdxfWb0sA9PXFlWujZ350DLn-w91NM7TKT2eV-Srz8UjT3Iyt55L2XUWxTqhfoO19IPCkLgCskkzFUXSO4vgEnaB65qwxY6Yv8UkLiAUd4NfjF_U0YZIlhd-Phzd48a5QqmwF0rIzZNVkka0dFwCZA0axzDOrqzR-qMQESTLeRxsb0NzBqMZjrxcx7OeCNePOnnoVUHig0ea11ke4TfzEdGrrO-AfTE2gwYoh0_XYJzcof6SWQo4WZaHCk6a7qaUbqcinyljv_vsVUJ-RtK0jCwfoMOLt2CjXGjQuNKQ0mqaiBuvFH2DaGaG4WXdJh1mW482Ma3GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
✍️
اتلتیکو مادرید نتوانست با تیجانی ریندرز قرارداد ببندد، زیرا شرایط مالی دشواری در این باشگاه وجود داشت.
‏
🎙
پدر تیجانی ریندرز:
🔻
‏"ما امیدوار بودیم که با اتلتیکو مادرید همکاری کنیم و دو پیشنهاد باشگاه القادسیه را رد کردیم. آن‌ها بسیار علاقه‌مند بودند، اما در نهایت به دلیل مشکلات مالی، از این معامله منصرف شدند."
🔻
‏ما بلافاصله دو پیشنهاد از باشگاه القادسیه را رد کردیم. تیجانی هیچ تمایلی به انتقال به خاورمیانه نداشت.
🔻
‏آن‌ها برای بار سوم دوباره تماس گرفتند و پیشنهادی را از طریق تماس تصویری ارائه دادند. سپس، ما برای بررسی این موضوع به آنجا رفتیم. آن‌ها به دنبال این هستند که بزرگترین و بهترین باشگاه در آسیا شوند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/104680" target="_blank">📅 00:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104677">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🏆
باشگاه صباح آذربایجان برای اولین بار در تاریخ خود، به لیگ قهرمانان اروپا فصل 2026/27 صعود کرد. این باشگاه آذربایجانی در سال 2017 تأسیس شد و کم‌قدمت ترین باشگاهی است که در لیگ قهرمانان شرکت می‌کند، با عمر کمتر از 10 سال.
🇦🇿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104677" target="_blank">📅 00:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104676">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myrMNO0tjjF74aCimg2mQS5oTwsUzBnb-3x__hjadCerpBn8QidiYh1_FcQ5GLA7qr3bXC7uG9X3KwAN2z881hxN5Wouc1jsM3hZ4JzSpdjzbqWzUYH4EkXDk9D39GqmlTIgj86skDWvyMNFBXgyRFraPU_8JjZWnU4B4iPEX1C4MeYoyPH7mdLGiFF7Rz1gfRouWmW_LEa5B35KOzoCVw2K2Oq9QJ_66MsRaITQ416XIZZht44MCsm1CkZAX5TpohFcV_OogWWKa4AnoTmb6DDwF-hLV4_vGo4zWGCsqvfyoMHn16tw48gpDZ51AW6xjXXIvFNlH3n5EOefREN9SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
باشگاه صباح آذربایجان برای اولین بار در تاریخ خود، به لیگ قهرمانان اروپا فصل 2026/27 صعود کرد. این باشگاه آذربایجانی در سال 2017 تأسیس شد و کم‌قدمت ترین باشگاهی است که در لیگ قهرمانان شرکت می‌کند، با عمر کمتر از 10 سال.
🇦🇿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/104676" target="_blank">📅 23:56 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104675">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5LFmO1GGJvRT-XDDBEElEz2z-tbp99FkbTOriH8GpZt3PSB_CoRdS5dB24L47mrFZRivNMwouAt3fY4QzkzUTZBzLLTBG-GnOnQTzu8e4rFoZm55dJQj7YXryCgYiFDu-lCEmHgADcwBQ8BfJs5zVi6WPEyGro_4pr7uzKD8jCNu7YVkzdnCCfYHBHJs9CuejeKOuv0p6jHnePh7ecHVXZfSprd8lHskz-zdhJ7YXUbEJyShRxZR3H3W2YQ21OuHzYCbFJN2oepm3fYTNKOuw-8OlRB8N0bMS1oLmz7nl01oSlFTw4Z7FLUDK8k6JJDAt-gLlhc0zPXA3MYkYyP2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚑
🇮🇷
#فوووووری؛ اوستون اورونوف در بازی امروز دوستانه پرسپولیس مصدوم شده و تا فردا وضعیت دوری احتمالی‌ش مشخص خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/104675" target="_blank">📅 23:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104674">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41704fa8fe.mp4?token=rCPRJOhP7qBcKYpeuRcEJpjnJSLsVcX_fTLjbrLWwKAefdGiZhXJIxx20qcLuMIoiHRtxERUhlI752fZvyBCD7yPgJOCtyLPJPu8DnSVSqo80Y0CyoU5rl4oU83SW4o8M8EUaIZ0ecGcZW98Aq0VyX9V1Y4Ph_OqGTpJaOZukYX5hWrX_jYi9T73UTSHjnIOdW2Grtqm2RgQ-ZYe7TNKh0mkrybA_6keuFZQunBUQD7ht9d0k2fPAZXlXPcVAqrpoWFxjDC0F2Q0kHtOiGGdGJ_hcIAgOk-yewyfN56TpdUNXbGtPb_pF9vj7Qlp2Ek7lYj2J9Td7_nuqEiApHzQPF5h4DLDbnmz5_NzA9x9Ay99oAa88to4b91nET7fQXy3R8VeONONGwlnq90M3xIBnY7LWDtAyiLBp9ek97aw5BAhlMy2ln2HBaaS-JEDRfTfV6YVTl3NkQ18gGRLvopk257xqHxAGk7N2sTsqL_ALFajXccylsCwJiJWiXBY3rSc2CiwCOo0euVcV5FfIABZHs4-oitau0u86XZH2J8n44ghA2UdcdKWsyMNFYgGrqnQRjmhRBudwIakG2IyyGlu54phinMIJTs_uIsV1u30-Us2YKACJlHzFEObOYpQmQgGuI0AZEst6vitOmwxTBXu7tWbM8Tsk-SaNPhQ6ntj3wI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41704fa8fe.mp4?token=rCPRJOhP7qBcKYpeuRcEJpjnJSLsVcX_fTLjbrLWwKAefdGiZhXJIxx20qcLuMIoiHRtxERUhlI752fZvyBCD7yPgJOCtyLPJPu8DnSVSqo80Y0CyoU5rl4oU83SW4o8M8EUaIZ0ecGcZW98Aq0VyX9V1Y4Ph_OqGTpJaOZukYX5hWrX_jYi9T73UTSHjnIOdW2Grtqm2RgQ-ZYe7TNKh0mkrybA_6keuFZQunBUQD7ht9d0k2fPAZXlXPcVAqrpoWFxjDC0F2Q0kHtOiGGdGJ_hcIAgOk-yewyfN56TpdUNXbGtPb_pF9vj7Qlp2Ek7lYj2J9Td7_nuqEiApHzQPF5h4DLDbnmz5_NzA9x9Ay99oAa88to4b91nET7fQXy3R8VeONONGwlnq90M3xIBnY7LWDtAyiLBp9ek97aw5BAhlMy2ln2HBaaS-JEDRfTfV6YVTl3NkQ18gGRLvopk257xqHxAGk7N2sTsqL_ALFajXccylsCwJiJWiXBY3rSc2CiwCOo0euVcV5FfIABZHs4-oitau0u86XZH2J8n44ghA2UdcdKWsyMNFYgGrqnQRjmhRBudwIakG2IyyGlu54phinMIJTs_uIsV1u30-Us2YKACJlHzFEObOYpQmQgGuI0AZEst6vitOmwxTBXu7tWbM8Tsk-SaNPhQ6ntj3wI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
ویدیو وایرال شده از دعوای خیابونی عجیب در گیلان که یک مرد در دفاع از همسرش دست به کتک‌زدن دوتا خانم دیگه زده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/104674" target="_blank">📅 23:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104672">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkLHYw4Hylq5PKCkKX52bkPBks6eOEHQcd9GUVfpxLH5cXCirH3S2YhfV4h8WJFdK8A-qmWRvsWlKlpfdysGSoLfblk--q6UzN-g4UIUz2pRW5xbHh5jcXZmVwVQee58BDT4aruB5s5_sd1U980CZXM-OQQMZQr5r_lINx3j3JIFr--CSq8AJLSh8wVuIBZEUYSX6DGlHJ1f8FqzLVIwXkuYEL5haIKrs5D-VfTSWGKc_6b8-MxuwqFPeWeQQqAfkfXj2sPOzi6ZaTUiXRMzjo1nPXtK4QxNpj63FFKp3StAxJ8IwMAf2oehU2OGmSNdptdUzXRkoDisebppwZ7_YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برونو فرناندز، برنده جایزه بهترین بازیکن لیگ انگلیس برای فصل 2025/26، بر اساس رای اتحادیه بازیکنان حرفه‌ای.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/104672" target="_blank">📅 23:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104671">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcFDenyt6p-IRJaUTX8gLqyEyZBlII3olHOe5nYX4aJFvjr2ZX8M2SKTW8_chynxQ0Cbzmycx_MQMFoXEH5X6onZANwW0JxpAQWhu4JDALE_HrV2vnFoGa5bmt3mQvD6EnL0tA-As-BBYrptSZuKNUULtOBT-gskqPN_5UhbmpQtrlarqrhxpUquwYDEGtRcrexWjlmHGNLDlL9zFnXA4gcRl-Q9r-7Quk-q-R2cLB7cpns_vwGA2eC6dT14TKj1nWcKDkEgPEgmphA_oLSBV9-gtBw934UDkQCwVwGNPBnKmP3O4E896HAdjEyLplpn_Ac9jQ2FDPagIdNXRnfwoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب منتخب فصل‌گذشته پریمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/104671" target="_blank">📅 22:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104670">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/090cee5ae0.mp4?token=ICH5o0TIgu9w99ovHd3ZOEYLg-qzS-ayLVKRBuhacDvLd0MVq5nVNurQCk0iHt2HQwyGSDJBP9WUNpj6RUG0bsm5vsMoKUe2pcqSO4QxK008dP_-a1twebRBb2MjLgrHI7Wz4xDKViQLMIaC2sLfWeNrPgr9jrt2alV7iWfgjBF5Bq5f0mGlCvu1jNxhjqz0uPGB5aUcsJUPICvSHWY85X7Hoq-5XfRXQEdbf9BgYaQ0vQR0Bhi75ZHADL_ZqA-SZDLRnOvaKbQRpDoHwTwSNjk6484iCuoUKL9PmTgcitnA51EHHZX_hh1tiZ6-ehIsIQBG3QM7pdcn2nhuc2hwGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/090cee5ae0.mp4?token=ICH5o0TIgu9w99ovHd3ZOEYLg-qzS-ayLVKRBuhacDvLd0MVq5nVNurQCk0iHt2HQwyGSDJBP9WUNpj6RUG0bsm5vsMoKUe2pcqSO4QxK008dP_-a1twebRBb2MjLgrHI7Wz4xDKViQLMIaC2sLfWeNrPgr9jrt2alV7iWfgjBF5Bq5f0mGlCvu1jNxhjqz0uPGB5aUcsJUPICvSHWY85X7Hoq-5XfRXQEdbf9BgYaQ0vQR0Bhi75ZHADL_ZqA-SZDLRnOvaKbQRpDoHwTwSNjk6484iCuoUKL9PmTgcitnA51EHHZX_hh1tiZ6-ehIsIQBG3QM7pdcn2nhuc2hwGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🎙
سخنگوی دولت پزشکیان: احتمالا قیمت آزاد بنزین به حوالی ۱۰ هزار تومان میرسه و ارقام بالایی که مطرح شده صحت نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/104670" target="_blank">📅 22:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104669">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TK65sTaUwua2abgsjgf4urSRfF8L0iLhueGw6cVP1-p-uVQFdY_EYrLkYjUznc9FtpjyjuYxYmP4KdrwlOib5RKNc38L_laPzX0AR7WVF3jVigS8tOCjAWzdOcP-xCIIutVgHDpVOkXe_g7My0jQP2hlN9BAutbOAKEdskUzbftIknGBUxUZcnylaNYpaFgtKp88k0YYYsmWKcIRHjDnPevYK2mfF82mhqA7nKXQIaArWbrgHPfvzgGvnBY2aCTX0bPJAltn2SBR-jreabEcAr14PQVkMLWZlOT0ziweudLGydn4MiJ8nmihoBP6T7yTEbTi9a0LGNlaj9K1UFWf1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گستون‌ایدول خبرنگار مطرح آرژانتین: مذاکرات سیتی و چلسی درباره انزو فرناندز آغاز شده. ژابی‌آلونسو در جریان این انتقال هست و در صورت توافق مشکلی با جدایی این بازیکن نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/104669" target="_blank">📅 22:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104668">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2063216dff.mp4?token=QpIOGpmoHsicRf3AhZCUF3YN4q7RAOjNnPHBv8_z9-wPDFV3MYs--oq1DU_BGT1GMfeH3qJUl3gh7IyVg0Uto1Y-fv95tjRG8zKf4iGF-KWHw--hBYWi3MsgI9iSlEHEVz-EYJdXB2HX2zQKTAgt8i66B4i8P5JpVPFqqsktJy6Ynzwy8lgMKOfccvjVwhy8pE5xNVLWWSGaNPsXBfwXc2uBIPTe9lZ_0-EvXBIuBidHVr46RKs4fKx5lqFWV6iv0NkmydAS_GeTS8d2XIVWghfZuXayF3abb4mvW5SH-86nHV9Qq6d3xoumhl88lp1LGLKBRX9_aSER7zP8DmodM48o9n2KKARAt6ipjxNZUhqDe9YiaMbaZ5AEnSIoDdCMQjapDMGSyA2Yxyw8FMgo-150_qy9BdQZQ93ipDSKOCOre58RQtN0NU0jLj2Y9wXjnSUGlZUOvKPhejz9aNpVxV_xiX1jUOQRHom2LeDF3oaGNxUsz6mRqJlvBpNl1yN7K9hN2m3qSwApesVoiueTMp16KGR6bLMYcSeGZJAyONJUWMIsW_mn_xUdB6ZnZNr1NsvwXnj7f4viQVcYw_kTKjM61E_4PVjayf0ZbMr4PRuPwUNMIQPhVdn7WtYaGa9qsL3Gp2FqMzFg37lYP2M_gZpJldYLxPMIwK3TxbGIndw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2063216dff.mp4?token=QpIOGpmoHsicRf3AhZCUF3YN4q7RAOjNnPHBv8_z9-wPDFV3MYs--oq1DU_BGT1GMfeH3qJUl3gh7IyVg0Uto1Y-fv95tjRG8zKf4iGF-KWHw--hBYWi3MsgI9iSlEHEVz-EYJdXB2HX2zQKTAgt8i66B4i8P5JpVPFqqsktJy6Ynzwy8lgMKOfccvjVwhy8pE5xNVLWWSGaNPsXBfwXc2uBIPTe9lZ_0-EvXBIuBidHVr46RKs4fKx5lqFWV6iv0NkmydAS_GeTS8d2XIVWghfZuXayF3abb4mvW5SH-86nHV9Qq6d3xoumhl88lp1LGLKBRX9_aSER7zP8DmodM48o9n2KKARAt6ipjxNZUhqDe9YiaMbaZ5AEnSIoDdCMQjapDMGSyA2Yxyw8FMgo-150_qy9BdQZQ93ipDSKOCOre58RQtN0NU0jLj2Y9wXjnSUGlZUOvKPhejz9aNpVxV_xiX1jUOQRHom2LeDF3oaGNxUsz6mRqJlvBpNl1yN7K9hN2m3qSwApesVoiueTMp16KGR6bLMYcSeGZJAyONJUWMIsW_mn_xUdB6ZnZNr1NsvwXnj7f4viQVcYw_kTKjM61E_4PVjayf0ZbMr4PRuPwUNMIQPhVdn7WtYaGa9qsL3Gp2FqMzFg37lYP2M_gZpJldYLxPMIwK3TxbGIndw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🥶
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتیاس‌یاسله بعد ترک عربستان و بازگشت به اروپا؛ عجب حرارت و شوقی داره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/104668" target="_blank">📅 22:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104667">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olJwSnoY9_2su06bKw6b5rfy69qiFGltObzoIPSOxI5HxCQ8ZNGMt21FWrOtbW4FMuok5odKnzfTBfaq5MpX_OpOut2JxZDNFG3Y5dJfJ4_gpF3gSt1_PYj5LC75EzaJSOfqDqMQ3IWDMKrfDCnsLVGVFPsR4n2I-lY161Chv2qI8P9U-DSLLj3MJm0Z-yirnKHIq1R9vJJREXBR6M8ZgM3LZZyHEY1kEicNcKIgRa-j09za0_yJn4yZf38I31fMDUP8JMIhkI9_SwoSLC2p4TFL33tUg1eSzYFO9uimzd5YzXr36YjDj5WnhvUffIrATdmIIYlVlCBhkIyPffBAAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نیکو اورایلی جایزه بهترین بازیکن جوان لیگ برتر انگلیس را برای فصل 2025/26 از آن خود کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/104667" target="_blank">📅 21:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104665">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccff2e7a05.mp4?token=Rx-cNfGIhpuId60Qi_uWar4sOojMnX2GuxO68ZaxEJ6AChl46Vbv96Z8hNO60skHfJc8sidv5ZElKEXW4F5pb7ZsEn2ETQmMvaR0zM-CChny11u2hTvWRoxuBYwrgNPt03rQAadUBcpXtJBw88H9lvjNd0rr7-Ci9NK3ghS0Njtqc1VXfEsyV9ooM-xwwxeBe74HFAeaqjmBhRFc2Nl2eeucmZMU2nYNZ9lgDkYLUEvPdd5YqjqGv3iaijO-7llKPBOaKn447kdP5wkcAb9w-7LaEJRK81a2PxYqr3bUHmrEcXVz-DP1bWVhfyv5SoJnll2YdMGoiQt2XExbXur4sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccff2e7a05.mp4?token=Rx-cNfGIhpuId60Qi_uWar4sOojMnX2GuxO68ZaxEJ6AChl46Vbv96Z8hNO60skHfJc8sidv5ZElKEXW4F5pb7ZsEn2ETQmMvaR0zM-CChny11u2hTvWRoxuBYwrgNPt03rQAadUBcpXtJBw88H9lvjNd0rr7-Ci9NK3ghS0Njtqc1VXfEsyV9ooM-xwwxeBe74HFAeaqjmBhRFc2Nl2eeucmZMU2nYNZ9lgDkYLUEvPdd5YqjqGv3iaijO-7llKPBOaKn447kdP5wkcAb9w-7LaEJRK81a2PxYqr3bUHmrEcXVz-DP1bWVhfyv5SoJnll2YdMGoiQt2XExbXur4sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⚪️
ممبینی دبیرکل فدراسیون فوتبال: قبل از جلسه فردای هیئت رئیسه  تقریبا به این نتیجه رسیدیم که قلعه نویی سرمربی تیم ملی در جام ملتهای آسیا باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104665" target="_blank">📅 21:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104664">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFMyQ4q_RJGEguRi_CtuNxYss5NYeSi1pvZu8UTEeniwqbDNSl6NztNSTvRXYsCQkmeK2cfVngz59ZvfP6G6-a3xI6yHbfaAms6YsfRjgCGe5EuHR8aJboQgBg4ADhpwUbZlFJ6M-HvpLVgZbxmu80_POUg4ugdbYggSFJX5wiB0g-7eVFmsiUykOIDKA3iBKt-Tp1WauTkgDSPyX47efU5EJ2MPsUSzm3_e3h3O7DNyuJn9kEaCZYLD4r7VlVEqOZRuii8an0w886SjsZcjcGs0oekMVglNNMXMktKpcvJwEC7yHidZgTUR26TL-scDBUqgxu_CatsOHDvBZGvbSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚑
🇮🇷
#فوووووری
؛ اوستون اورونوف در بازی امروز دوستانه پرسپولیس مصدوم شده و تا فردا وضعیت دوری احتمالی‌ش مشخص خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/104664" target="_blank">📅 21:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104663">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db2b316284.mp4?token=CGK6V3-y1cHowxxzsnp5a-4js53hu1WQ0ZmhKuXRXhfWlfVk3xDUrOiI5GuoaQZlonFbwp4YqAadp1IeEakro7_zGyG0u2Blk42BtQkfhnl2tcZRN5IuyJ8XmJRtUZXN5H-2pJ8NGPWTNfDfiE4_YNRrcvftjd1N935Yi-06irHSmABS3i9JUJtERBeNiGap6xziLEYAeA8aNsyHZgbq7dk8mcO7eZz3NaaL2ngNGzvRzTZmF2TTYRlYK4uue8ixe3FrG8CTefkGAVkrQ-PF7WPwaTJbUgXNDQqglkU62oZ3k3r1vezN7uja8JP4m--vQIssLWprygGdWkHJL2KaXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db2b316284.mp4?token=CGK6V3-y1cHowxxzsnp5a-4js53hu1WQ0ZmhKuXRXhfWlfVk3xDUrOiI5GuoaQZlonFbwp4YqAadp1IeEakro7_zGyG0u2Blk42BtQkfhnl2tcZRN5IuyJ8XmJRtUZXN5H-2pJ8NGPWTNfDfiE4_YNRrcvftjd1N935Yi-06irHSmABS3i9JUJtERBeNiGap6xziLEYAeA8aNsyHZgbq7dk8mcO7eZz3NaaL2ngNGzvRzTZmF2TTYRlYK4uue8ixe3FrG8CTefkGAVkrQ-PF7WPwaTJbUgXNDQqglkU62oZ3k3r1vezN7uja8JP4m--vQIssLWprygGdWkHJL2KaXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
اشک ریختن هوادار فولاد خوزستان در بازی دیشب در آرزوی دیدار با رامین رضاییان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/104663" target="_blank">📅 21:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104662">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1q0afJjGfFG6taPVIPJbH4bl8SVeBKNS8PxXpaKUDXtH8DMTxdKGcD2gA6x9dLbzQ8sIdGFhXipFRq4awORDpPCFANctOHJCuHKtf70elUytvjOD-SYtHl91lnabgGvJwIyobxbwHkOlVtclKWXFaFFFwjf8p6qLHCt9et3_sWw06kB89YveOo6mT9ErkKLYSrLiDtwa_QmWILqMRXxh9iAx9AVyhUfcwXwSiEgmDqwQ36BvGf4ZC2KcWmZcxMEiGMQKA6tMSd1CsTiVxLZK-N3oYXtwFgllOr-q4_rWyJexbEuzxqBOLMth3q55FFcCTAAP43BTq2RRCOQITkQvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فابریزیو رومانو: لیام دلاپ با 50 میلیون یورو از چلسی به ناتینگهام
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/104662" target="_blank">📅 20:39 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104661">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FUSMtGa2EmFKMszOqIYwMfCDH1fLXGwEbxniv3j9fzgtLwcuI7WT3doegs7i5qLWthxGGeJSFJslvQcS5Vc9khdZR9ZFZaVZvBL3hqEhB3rtgskD0F4lZCftVc5M4cuAGCddyGpqyfX0M0By-E7ggxbUUZHAyNEIhT211pNUQpeESHOfaatsWmTVi84tnWuvBsytzCgQmUxP-y6G58ns4KTueYzotDuCe4HtJvLlBc3IB7LdMlOTmS0J72_0mnqPtYiT32H1pfGOQ8uyHbokIqBTJDkIK7Yweam7oHkv8neXSIzbiIJ0W99hJNNcnWkEwtYFMCTJ1kAAsghG1Ahubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رونالدو در ترکیب فیکس النصر مقابل الاتفاق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/104661" target="_blank">📅 20:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104660">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFRSvfFJ6oJ-klQRcfMDwi5K3Mk2IJnDCbV2YJTpkL_eUwmFJK-Dj2oVIKdISVcSjzbvjBx6ERYHyhg-de35fLLX2lrh1S7t9bUFo4FSEf6-rGJPtXuUpQK8n7LZfdOb3hBupMcrqj3XDfdex_4JNe4YzWKFtJm7FotCkw2wL1ljHrvf4h8u3soInUUMZdNHAjjk_HdeNFFzV0kCqya9NPjSfsVlSr4eqaVI7NbrWknK3B4n3UN7EvOoNwoY2KcNrEpSXlfPQR8nDuzdF-nm2MVUdiQHnWqxIg6mwwr15hPsIugi0K2VP-plLSIcPgRsgI_VqUQT0uMOFDGrsFPwpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✅
🇮🇷
🇮🇷
بیانیه باشگاه سپاهان: رفتار عارف حاج‌عیدی مصداق بارز رفتار غیراخلاقی بوده و از تمام هواداران استقلال عذرخواهی میکنیم و تنبیه‌انضباطی متناسب برای این بازیکن در نظر گرفته خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/104660" target="_blank">📅 20:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104659">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jW1_wAJcMBWnH7ChRLtHvM0zxS0Ht1-8eUua6Ut7XOVeBsB5v-llvryIVdFbA3HXQJ4T5361gbct5CW2zkGBneJkHffNaDjg7XYnPUnsBwF27Xebua-NqjKroDKRbcZfwGg2hYfZRrDvf01O67MCPqjkuGyd4BuH8TQ37_2VLxdBtY4od6oPFkDL0m_cLblpjzqagyM19a-zFm2SdqByq1m9cZ1PBqq13I1Sg_tdDGCu50D8StkFQlSRJdxjmStdDY7GGkI5uHF_i5pL6ez80HaysBEX30pAThf5ZkFqHxIQIVRgIu0UoOC4vfO4-MU8XfL6eeslMi99uAXjaPc2LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
دیوید اورنشتین؛
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
لیورپول و پاریسن‌ ژرمن امروز در حال انجام مذاکرات کلیدی بر سر یک توافق احتمالی برای بردلی بارکولا هستن.
🔻
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بارکولا میخواد به لیورپول بره و نمی‌خواد قرارداد جدیدی با پاریسن‌ ژرمن امضا کنه.
🔻
🇫🇷
پاریس این بازیکن رو حدود 145 میلیون پوند ارزش‌گذاری کرده، در حالی که لیورپول می‌خواد معامله‌ای نزدیک به 100 میلیون پوند انجام بده.
🔻
✅
مذاکرات امروز دو تیم گامی مهم در جهت مشخص کردن اینکه آیا میشه به توافقی دست یافت یا نه، تلقی میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/104659" target="_blank">📅 19:49 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104658">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48bb1d2255.mp4?token=m7x9B01iDgAyluaXVjgp00zcYS8rcmg3y-cDPySVYzdJxiMlf2f4h2s2xWyIROPVdDBckaLYQTyyMdKjsbvq527HE8B1_DmczYiIKUXCsxXGWDStwdgvfWz9bmyvFj1iUjxCLO6dDVgHEZVa8M9qkaloSeQWo9zF52LWwrz_RGzDkxJbOmsgRW4Xqruh4GU73--4sFhOcONW2VrwyQYyHggWAa72OHok3IPqfT-CEhiuDMm4YjiotEJq4Mg65_3U0aJpu2FvNiAzcldNuId0x0duXhhKVhweCQ1wmtHbR8n4AtQE6YuD5pDdWpPQTJ0L47Pv3uUuBy08XtETf-VziRg8Np62SthOvvudMjbhzwlU63pu18iVn2YFFwVlQuuWN1HUlfbldhLu0dtBftsQKGbbFF-tRA9P3AtMcC6ig0WEBEsyMXYEdWZdM-Rdvd8V8z-6Hj12vrGVqwdcS9rN8tiqeGOkIvl98a_zJjiTVMjhDkX8Flbjlj9L5SpDGCAljw0Fe4dwyPe8gM9zaH0I2KLR2bNQ-1XVdt6ciZT9TfHaMB5qzv8iMeuluHuuv2zHRELmopZPL0nToDVUmBgrJwSsMg8mKwB0htboUbmYJ6NRFbz9DlFxq5q0x6FZNEwi4Kfxi_842uD4_w9aDITto3na4nkHEIVqAcgz7NW2U5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48bb1d2255.mp4?token=m7x9B01iDgAyluaXVjgp00zcYS8rcmg3y-cDPySVYzdJxiMlf2f4h2s2xWyIROPVdDBckaLYQTyyMdKjsbvq527HE8B1_DmczYiIKUXCsxXGWDStwdgvfWz9bmyvFj1iUjxCLO6dDVgHEZVa8M9qkaloSeQWo9zF52LWwrz_RGzDkxJbOmsgRW4Xqruh4GU73--4sFhOcONW2VrwyQYyHggWAa72OHok3IPqfT-CEhiuDMm4YjiotEJq4Mg65_3U0aJpu2FvNiAzcldNuId0x0duXhhKVhweCQ1wmtHbR8n4AtQE6YuD5pDdWpPQTJ0L47Pv3uUuBy08XtETf-VziRg8Np62SthOvvudMjbhzwlU63pu18iVn2YFFwVlQuuWN1HUlfbldhLu0dtBftsQKGbbFF-tRA9P3AtMcC6ig0WEBEsyMXYEdWZdM-Rdvd8V8z-6Hj12vrGVqwdcS9rN8tiqeGOkIvl98a_zJjiTVMjhDkX8Flbjlj9L5SpDGCAljw0Fe4dwyPe8gM9zaH0I2KLR2bNQ-1XVdt6ciZT9TfHaMB5qzv8iMeuluHuuv2zHRELmopZPL0nToDVUmBgrJwSsMg8mKwB0htboUbmYJ6NRFbz9DlFxq5q0x6FZNEwi4Kfxi_842uD4_w9aDITto3na4nkHEIVqAcgz7NW2U5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💥
ستاره استقلال رکورد جهان را شکست
🏋️‍♀️
عبدالله بیرانوند از تیم استقلال در جریان لیگ برتر وزنه برداری با مهار وزنه ۱۷۲ کیلوگرمی رکورد یکضرب دسته ۸۵ کیلوگرم جهان را یک کیلو جابجا کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104658" target="_blank">📅 19:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104657">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c5505a725.mp4?token=kBSd33wmO31kPmj3c5FKQKaaNnahMJprRNvF6PtrPn0k4nvpNrI_iTq85cAX-e_aNsiq3w5gzudz3ttKU9ibRV2zHr6iH9V4kHwoY33-O2DyLvP_RWJxxWPphcOUpWAhyKZaSTZGj5MtMzOj6WX3i3S00IkvhMOc4qYOwHeG3mt0kD0a5clMTwDSR92gZES6gVUBsGC87x6DhC1zEjmvmWcIQczAUDjzqVwkk9o5UXgvUrb9EAovYWsFBgOzsbGYNNRvjpZjbee9UFsFepguaCox0UvHytFWTobAyTad00aweFjgetFd4tmCtgsl521Bw_LgEDUn5GiVAfIHMNBM1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c5505a725.mp4?token=kBSd33wmO31kPmj3c5FKQKaaNnahMJprRNvF6PtrPn0k4nvpNrI_iTq85cAX-e_aNsiq3w5gzudz3ttKU9ibRV2zHr6iH9V4kHwoY33-O2DyLvP_RWJxxWPphcOUpWAhyKZaSTZGj5MtMzOj6WX3i3S00IkvhMOc4qYOwHeG3mt0kD0a5clMTwDSR92gZES6gVUBsGC87x6DhC1zEjmvmWcIQczAUDjzqVwkk9o5UXgvUrb9EAovYWsFBgOzsbGYNNRvjpZjbee9UFsFepguaCox0UvHytFWTobAyTad00aweFjgetFd4tmCtgsl521Bw_LgEDUn5GiVAfIHMNBM1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
❌
⚠️
علی‌محمدزاده: پژمان جمشیدی از اتهام رابطه جنسی عادی هم تبرئه شد
!
💬
محمدزاده وکیل پژمان جمشیدی بازیکن اسبق سایپا و پرسپولیس و تیم ملی فوتبال ایران: قبلا هم پیش‌بینی کرده بودم که رای پرونده پژمان جمشیدی چه خواهد شد. خوشبختانه، متهم یعنی پژمان جمشیدی از اتهام تجاوز به عنف و حتی از اتهام رابطه جنسی عادی هم برائت گرفته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104657" target="_blank">📅 19:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104656">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ کارلوس‌بالبا هافبک باشگاه برایتون با عقد قراردادی به ارزش ۷۰ میلیون پوند به تیم منچستریونایتد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104656" target="_blank">📅 19:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104655">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moN6Win1DDmH6L4njdIP09XvNKo2yhybGOnGR7xcHv9BB32nPfvJEnPOycU7Q8k4T0KiPfLxqzVicKPPOOq2M9Ou363KBuTcY_-epdIa0YojdceAPn_z_ZRtgCAdaLUCsedWVXureeUX9zyWEt81mTiJtNSp592AtJ4NWEmmFRQvpIjTx7pMnuhw1uhyVkBHl0Jj5xLcTnOZ00trzDOZ-RycuEtgoglmC-ethEtSFzMZxBkMSUlJ5QUglPicz6EznfYN-pqMnhtpY56DMYRDUgSNeEnOCjgQHbPtopmHEviiUK7jzW6ZLBkF6A3IakEu-_7Kjf0-AupVr9Hs6Ye0iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔴
پرسپولیس در دیداری تدارکاتی با نتیجه 2-0  تیم امید این باشگاه را شکست داد.
⚽️
شهرآبادی و ایگور سرگیف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/104655" target="_blank">📅 19:00 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
