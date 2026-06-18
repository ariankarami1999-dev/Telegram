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
<img src="https://cdn4.telesco.pe/file/BfD5Scqb9-lcxgvvsVgL11eeyjZEiEPfFq6aJzYmBaHPtRZw8IkbdBZz9nPD2E6Ai4wgxOO7C6nbPu5uL73MravNhUYyR8-Rw7NyEn7V31dxihfY_Zea8qfiut3M9gMFXua-ZExgkVx1eWolWjAipX3N3r5Lg-t0uqYlm47eGpfPzufKhxa7Gmgsrnlhcyualh2tJWW7zH_i9NOwNQKUs96_Cp9lgSCNmQ2xEQMuT-AgfUewVV2bubCeyiJQDHC4b-5r8ExaCt-pVgFivzopkmcxbs8mH5UckaCYnpnMu_WEr-TOaOX_oQBayCGuK5EgqQPEl9JCRKdfcX61HxXpBw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 311K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 21:11:13</div>
<hr>

<div class="tg-post" id="msg-23782">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSeoEXCOW4DMF_CgfbIVSt7Ihd3ts0LJ2NYdPFnhvHi1mFlFkwV4YCVefYwWVwjcoHsjQQANIM6qJZjxpwsUA2F6mjzwls7w-Vk9aelVuT5gbURHbZN3iRUsGsqnRnel0XZB9WYE7P36bcNkn10xcOhCHAXOyNTqQaVRnnvTaIDvwAVeWMoQJRgFL-d3S1OWbXifZLTlZ-rLT9c68Pz2aVknhPOa_IxItQSXgDfz9gWWsdsnh6sGfrc1o8Nuet_6po-adwyjMM0AqB5grqPlD7tFxl8YTK3MYVXs_FRLI8gXHchF15mXIm0eWELM2z1mrOlAdaQUqI0SRKttEYLFMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ جلسه مهم امروز پیمان‌حدادی‌مدیرعامل‌باشگاه پرسپولیس و اوسمار ویرا دقایقی‌قبل به پایان رسید و باتوجه به اینکه مالکان این‌باشگاه با درگان اسکوچیچ به توافق رسیده‌اند به احتمال بسیار زیاد با اوسمار ویرا قطع همکاری خواهند کرد…</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/persiana_Soccer/23782" target="_blank">📅 21:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23781">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⚽️
👤
ویدیوکامل‌ویژه برنامه امشب عادل فردوسی پور برای رقابت های جام جهانی با حضور مازیار زارع سرمربی جوان و موفق باشگاه ملوان انزلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/persiana_Soccer/23781" target="_blank">📅 20:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23780">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3TlWDNZD0KvQE9xGJEfb90JtzKZaeVZgp_nsqqL4adLJnWDW7oR5YIblI8vxCsZ9xou3_w4u631MAX5dakO4h4_gXtSnFzthPoLq15BSBTex0-vAynq7wuQ9wyLxHSNYIfGmgO1hIgLcZVowsUBmEHr_RMFvz4dVSFDYFX1AwbgIXxekoYHHo8166GE90KxZ6v1eoWvtfeshR0uQhII1MS3yoUv2EYzyFPnMEFrxFVlm33U8-DalHPK5fpFQArhxuH5MFnFikrkS8pqUC_3jBF2RADxUxUlEt46Lao1jsrkS7U6L0fdtS2N127FIPzP8OIcQFZh4R2sKvzNHAA0Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/23780" target="_blank">📅 20:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23779">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okL6IhEzKQqqtfstl4C30zrXq3MezdvldRuKyl3Pl_hNxSm8BjmhnlpK6Bet_4DrABWXiUdCtFB_bqg-PleaXibaW1jAXmlCyc4dLbUZQF4EP45fSAf5JiWlNRbiwnD4dzvgrl0B-sM-LQshVIefY2PJTnRvBx9qrqxptTbH7aLFLiCVRLTty1h28rCCRaRs3gVrapEp3g60caRbuCEU5vJhL218SGQTTqrmaAu3dsEQ5n_fbtqBqWJiVhKh7nKn_RG7jp9N6ePEc9BdyHB5cYqKcBEBnKQFptReFMPmdweKJlm1_7b5NCXzHTI9kkMsZV2CO0aBTVUODvB_Y1B9CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول جام جهانی 2026؛ پیروزی ارزشمند و شیرین‌شاگردان توخل مقابل کروات‌ها درگام نخست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
4️⃣
-
2️⃣
کرواسی
🇭🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/23779" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23778">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqY2b05oKTJLQbc8daifDEybBcuBgdHbnTy0oDYIPiLKWlV-iip13POtvdwLfPn3gdQDURQpDmZcD548LZAESAWtSE_7iL7_qKXAO-eKzjU5fDepXmxEqLDGAqnW33misfbGvSKzTVUym8omK-yZ0ah9h7f4RINLX8OIifzivC_KA60aYeq_ETlkYhSgr94GLZaF_5JSAnyDQuyfOnia4N2Ci-ZA-03YRL1WGOyswNW6KuAewMIJXwopeLkLkwiJ0Te0Y37ToZohqIHzSsCZ1QHXASYqYgFZb3C7iLm9QqF2PdccFRqnHOfdz17rJkahyR0CfzXhNmg8HMas5wLK2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو برای‌فصل‌آینده رقابت‌ها مندی و فران گارسیا رو در لیست مازاد رئال مادرید قرار داده و قصد داره که در فصل اینده از ریکاردو کالافیوری ایتالیایی و آلوارو کارراس استفاده کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/23778" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23777">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1CTSavjWo7k2u1M0_7u32FSS6vOe2qSIM3MDchSjNWc_OIW4J2uHwERwFKiz155sYLndbz0AGLMsb6n35XgjYGTiMA29INZwb5oEzsFZvM3fcGqtMFVi_UE31CP2LMVdMDlQTaF62_OuqUzeF-Y2tBn2Vw7L8l9htcScrsnNkr94fTAyb_C2eTyKNt9qkWz7_wZIVefu9nCNWhV821wj-v579uRxgL_9BxmnhCMx4bvVHJJdfH0dQaDhZne8tX2NaQ4P9DUN9SM_mQ_sY80ocmO4P8FeNDdZ5xr_TPW9zPRyqCi3q5RvKXIzNEq3UUI-X2ilHE41CA5WVHvurUMZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تورنومنت ۲.۵ میلیارد تومانی رومابت آغاز شد!
🔥
مسابقات جام جهانی 2026 را در رومابت پیش‌بینی کنید، امتیازجمع‌کنید و برای‌سهمی از جایزه بزرگ ۲.۵ میلیارد تومانی رقابت کنید
😍
🏆
هرپیش‌بینی، شما را یک قدم به صدر جدول و جوایز ویژه نزدیک‌تر می‌کند
🚀
⏳
فرصت را از دست ندهید ؛ هیجان واقعی جام جهانی را با رومابت تجربه کنید!
🆔
@RomaBet_official
┅━━━━━━━━━━━┅
🔰
لینک سایت جهت ورود :
🌐
RomaBet.tournament</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/23777" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23776">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4nrKQXTQnS3pPwHGyddFG1ZUi4CH_XLCVON7X0P2FZJtTTtNAS9xiFNnFPhP-hxF9nBMffLwi6wQdx4Ehw9KgZDzMdl8HT8TPAjClibCPpR_Nn8WlEczTudwl4uDCnFGLwvvx_MSfWlsVdEG8jRAgR3grSF7fidax6HkzuM4pGVsVTH5c33yehRuC-HFtVWGEby6A85NZRKi_uBJ6ZWjR9VbRgCnMThjZo3mZHIj3q9N7A5BCWrTN8Lg7hLjFKFXw4WIvXbJd-vcaCXuDhAiMxoZaNsFdfWwb3wMmnpLD3kqRgubr5RsiANBOkwRPpP63CLEnKIJTDuEv3BTJ9cug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای‌فسخ قرارداد توافقی با اوسمار ویرا برزیلی به توافق‌برسند سریعا با دراگان اسکوچیچ قراردادی دو ساله امضا خواهند کرد.
‼️
مدیریت تیم استقلال در ابتدا مذاکراتی با دراگان اسکوچیچ داشت اما عزم‌ علی‌تاجرنیا برای اوردن این سرمربی کروات صدرصدی…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/persiana_Soccer/23776" target="_blank">📅 20:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23775">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceb72d8ebf.mp4?token=PBLVnYIc7bmLhqcvFTTYmcWX1YY_Y5chfbUwkUr_KuOfclWu0SQAQR6Ie-zFhZNnvQk5rq7bL4IZz8zkBGn2ySv8XChTOJKd9Bluc9irdkKmC6FmqWCBJpTfU9jWqT53MYyY-kOINDpl44xVjgRlTdOKzsQfmGwGWxGOsYRgGhKUyN6aC2qRrDau9udDaIcrzpvL8H19OnF4Pn2L1ClXTVL3T1c5jouJQ21MFkJ6GvLxIukHj7cz44fjsxIQU-FyjBlyE10PA1Hi7Q1OOJ3m38C8HqA4AB4q3wAWMbILJOR6JfxeQp_NzDcLGZsISDxjhpbQKxCUQXv0EFGDYlHkvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceb72d8ebf.mp4?token=PBLVnYIc7bmLhqcvFTTYmcWX1YY_Y5chfbUwkUr_KuOfclWu0SQAQR6Ie-zFhZNnvQk5rq7bL4IZz8zkBGn2ySv8XChTOJKd9Bluc9irdkKmC6FmqWCBJpTfU9jWqT53MYyY-kOINDpl44xVjgRlTdOKzsQfmGwGWxGOsYRgGhKUyN6aC2qRrDau9udDaIcrzpvL8H19OnF4Pn2L1ClXTVL3T1c5jouJQ21MFkJ6GvLxIukHj7cz44fjsxIQU-FyjBlyE10PA1Hi7Q1OOJ3m38C8HqA4AB4q3wAWMbILJOR6JfxeQp_NzDcLGZsISDxjhpbQKxCUQXv0EFGDYlHkvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنگ‌کردن‌خداداد‌عزیزی‌از رفتار جواد خیابانی؛ از خداداد سوال میپرسه بعد میگه تو نگو تا خودم بگم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/23775" target="_blank">📅 19:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23774">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVbvmUk4BuZBUO2lE7wIKJXJ7jw4cE9wZKf0RTs1A-ic2idWufRDDi5BYsGf6lrZ_UYDG4T55MD9c1s-gN7qk5XERNyqbk_8I3kTiYa0TaZGIL7xoci-wfEibFMBXDJLo9dNBEbuJYqqUxYImCSh1eWFsk-7-NKW_f4bdbUthK35-DvMYy2HBwwTg_6of_BSRX9eeUEIvUqCrOq4Vm1rxMX1ZvwaimRtzMLvccpnPTNgneqwqrhIENTPdOa-bbtFhGI0Ar1bqevOL9NxpblUMNscW8HqECSx_33Fi4_HnAGgTJNh46FFZStFUcIl28L_IejY2-KEXFuL82wlfEv-Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/23774" target="_blank">📅 19:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23773">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n15l-U_3vSKH-RWfyJTvoCWJkE54EqsJV2YC-gkeDpGVgPqH9-6NZr0IZHw5a0TKtLpwRHQM3ih_DX9HUobbmKx1ZqwfYPWC5cZhfSiwusOJlBPYyO-bzzxULwBoJIPwyd8GAulN55Pku8-ocUOAxAMmClbWQxRHDG1jXW5MocKkRCavfH15utwztWiskhNWipyW-SWXUcgwIMf37RESW1XWTdmCb5OZmQYf8XelNgkv0EYRaAb8loPwlKmDnWtSyqFrvloANREUWqEFuOiFRyKWCR5RPzCXj015IUi1YrG8hhS0ahnJMtWB8xFJUwrr9d0kcVsj2_oD3YmqGh0h_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
با‌اعلام‌باشگاه‌سپاهان‌اصفهان؛ آرش رضاوند و میلاد ذکی پور قراردادشون رو با این باشگاه تمدید کردند اما محمد دانشگر حاضر نشد به باشگاه تخفیف بده و جدا شد. رقم قرارداد دانشگر برای فصل جدید 170 میلیارد تومان ناقابل بود که کم نکرد ازش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/23773" target="_blank">📅 19:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23772">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2lpRaC8vVtWlBzA6yVYT9KKzTJP_ttJVjk_l3ofDUuHpScuArnaSANXB9Lj9kArDyi1G5QP97byhIHB0OZIuEa4MPPgw5mLkjbLivVWZnaFZpA6Fiu_j0rtzNtztZ7Xacz0nrc-Jy7_LJpTWPh8PDSGBA1jk2Ek8LeyyAuQDug-bw0oUgOfv42Fu5HKZRF4n5LJ-trO9K4oSWjHQ_dEuWbqBnM3whZ2spivyVxZjHRhAQQpiGp5imIJesrZ8SpFZ3MZq6x8U2sAf8Auqnd74m9LrxulfU0o7GUroEADli02RDxO31YEZTdNrCkstZEttR6if-nxwNG48cst-0PntA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇧🇷
👤
برخلاف‌ صحبت‌های کادرپزشکی تیم ملی برزیل؛بااعلام‌‌کارلو آنجلوتی؛ نیمار جونیور فوق ستاره سلسائو دیدار حساس برابر مراکش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/23772" target="_blank">📅 18:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23771">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHf4Aoy3nZYKkLjz6NiT7FNiUU7xAEf8mUHj3j-Lw0N0jxLEZ2hxNco0nZYeXtgzzSvFlpG6UvSl8Ql7g55hEMDGmSVXfzEJfDm4epeICBjvgzoGDc0BQrBpkVPzEPNU-4Z9_wRgi7TyM4AyhHLY6NoDOWeAJ-cV2GJy8bGsEFJnUKGNCKA3hnWICU0vLENzS5oWqK-zuGPWzfc1b1oQdOlFArJvk1YMHo5j2Fdoc_qxhSaOD107SSAxaGS9yBYulQbvVWvumw9jL5eu4tdmJAOVMxkEA1gVwSg4xAp-aaWoae--tK1layTPCucVrkpu_dvfe6yJAH9F1oqiSVTzPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: ماتئوس فرناندز ستاره پرتغالی وستهم؛ منچستریونایتد رو به رئال ترجیج داده و به ژوزه مورینیو اعلام کرده که نمیتونه بیاد اسپانیا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/persiana_Soccer/23771" target="_blank">📅 18:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23770">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuIYY5Mvmd6O0-fKw_RyiauPd4BiUW8rmtGkZQz_tDtGjts1vr2ZOyw9hiJnJSnfgqrpiAvHYd5Z5d1xWS8kT_taDktvOxkJ_kqaU7hHFuUe6IRCBrZ1X7zKzfytAUaAguyS1pDuIc3NoFL7jZ6-K-GdA0lau3eTju7KV-SNu30gEEw1RvNdX0Eb66hWeukmm2uof-EgNlTfSsEnCEMS2mlRpPddRpYWqkXaD20kfpxFizAZOd8W-zspaq1fhmvkZB5AG8n3PFd5nJSfXyVc94LxuxqAsKXb2n0PiaGxqAIGUhrolbvpIPdzouTvJVTsXL7F_JZn7zft73SfXpHKqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/23770" target="_blank">📅 18:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23769">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o03nm1bKaTDPED9m_B6IlmXg8AngadIBaNV9ot-kx3tWnbXIvjsiUUqXYTJkI5rQFY9u-GPuPCaVourUabo3B9Y9Tqu4WnMUGMhMTCH81NN-KxzXS63HQHzM8poMcFp7Mo2-uN7kbICmL0-cPV13SMktmbp7u8msoBL9S2qW_H5Xk5zZBZ_1EjguOxTn2TmNy70qILFIKm6qa2Z-rx18v7TBLAV7IEvlXlqR8LeoRVE_CxQqJ8qaA-zXrg57LXKqfhk3V5KdFxPEuPgiywjOURF83Eigts22mFfKhqBjMMUA63nsTgXk74QXBHaEO-qZdwxc0HPJ_lSv2edcTME_Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#اصلاحیه؛ برنامه هفته‌دوم‌جام‌جهانی 2026؛ بازی ایران
🆚
بلژیک ساعت 22:30 برگزار میشود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/23769" target="_blank">📅 18:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23768">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/629abdf2a4.mp4?token=vTIcQJmyVbYseAu1WEpXiiu7VhDNaK4aC4kxlQPFo9NcAaMaHtzPgW0v_JET2zGKlTIQyKj5367Z4wtUFDOI8LQh36juq-pXHu8yDvax6LWnHeBKjkR2lnZvDuRAunET--YjUu52yIRoDIKb6znLR8x27uRgIv14NoY9XWxF0gp_rPYQMMPBHIxj2RX-Uw7Nwd2vc12B7tRjdApiT84IRrU1EFF3q4vtFn6phCVgkzeSlefxt5FTeiZvKS5P6LQu1oF-e3ftTMYQ4rUpPeXjTwnkMD8O_JM8yiVZaCyxhk7Q4AlPtJnKPKv_NEKEfDOLIOC5XChC5ednznh3XRneBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/629abdf2a4.mp4?token=vTIcQJmyVbYseAu1WEpXiiu7VhDNaK4aC4kxlQPFo9NcAaMaHtzPgW0v_JET2zGKlTIQyKj5367Z4wtUFDOI8LQh36juq-pXHu8yDvax6LWnHeBKjkR2lnZvDuRAunET--YjUu52yIRoDIKb6znLR8x27uRgIv14NoY9XWxF0gp_rPYQMMPBHIxj2RX-Uw7Nwd2vc12B7tRjdApiT84IRrU1EFF3q4vtFn6phCVgkzeSlefxt5FTeiZvKS5P6LQu1oF-e3ftTMYQ4rUpPeXjTwnkMD8O_JM8yiVZaCyxhk7Q4AlPtJnKPKv_NEKEfDOLIOC5XChC5ednznh3XRneBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌فتح‌الله‌زاده‌مدیرعامل‌سابق آبی‌ها به میثاقی در گفتگو باپیمان‌یوسفی: مواظب باش بعضیا صندلی نداشتن اومدن صندلی رییس رو صاحب شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/23768" target="_blank">📅 17:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23767">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4riYTDC4yDFUPNAUHZqDyCgPV48GTD3j3XutjSKPy56QAoPWBG5jA5JKsdfI6aKthUJc3hG62wMcYlqj_IgvFfV-90upLv0LTpo9RNfznXaDYFn1IAFuJav70E637rPDT5xZlZTJZPMoOEjGhL0unDEP6R68iyEHVFbwG6CFuNQdMbAtqq8cN_E3wO3GX9bVuZtW5HQB_yYaIX9QtY8-Rh9KS9K-OMVqlq9Tv2-SSeZ5sswP4NcvQepzh37AfZ2hurl8fmGXpbrprrAD6RhW489PPy9G0z1KYJ-8IojoJHHM2fewmtSO5gZ1-zc5HJ6XXdoEwrHzo5jpJFBOiPrUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه‌فلیکس‌دیاز: فلورنتینو پرز رئیس رئال مادرید به مورینیو قول داده بعد از اتمام رقابت های جام‌جهانی 2026 تموم‌تلاشش رو برای جذب مایکل اولیسه فرانسوی از بایرن مونیخ بکار خواهد برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/23767" target="_blank">📅 17:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23766">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUVrrt4Ol7Z3FYenRbwJYYFVS8ceTcOIxAKNxvRt5lUC7A0FBqQz5GHrTpZeC6Dc3WZeqohNvhlzk1AQL8ro2JVywobtMZt3z3SmJyd-NBgiuEE0puglT5KGepg23gFbYZD6lyC4OW0D9GcjAAKSE2N_FFajhwb-pANl2vkgMAvIXNRLzrfgfLaXHi2AumDqjNcXU7COMrtMVIsDMd3C9opVZWKzJrMMw1NhlTLdi4PP1f8-pZI_GcxZzLi7L2AVlm3ITQDhv62kJPrZXy5osKPT5NLFv-q2jGGWM5t9q9AJWZG-99rEhS4RfUtrPcolediSSCKXZhIYa7lTDVlqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد چهار بازیکن بارسا و چهار بازیکن رئال در هفته اول رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/23766" target="_blank">📅 17:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23765">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwJXJR5m6e9uYhw9s6FadlujpPdY_sBPZIYj85ACi8qkWmMeL3qhNooKuqWsmcdqdPXaM7HvaHgzGr8fvV2JXAOqgWnOuHaJq0pLP085jbjjJL326P9e0yeBR6887ir0LYIGQ3uULXDmKj7jVm1EeU6bwf3UgGssdnv33n_9lfr06BjRb3QYHjjz9J55vGeuJB0VfsZKH4-m_X9lFJpahGzK8ystzjOQ2uNklp0UpDgA5DbCsY31vdc0qARZFu8xO5q3X2vxeYiwHTUBCM9u5kkvr1PyznflvGSJPpvkQpStWUOH-stseVIJnK5W0jLfBRYUbyQBT4lS9dtkwiboiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌های‌دوره اول جام‌جهانی ۲۰۲۶ در یک قاب؛ از ارلینگ هالند و لئو مسی تا رامین رضاییان و علوان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/23765" target="_blank">📅 17:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23764">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKiyFi60XPc22hIojnncUbJVQG6b6UfYE61jWlYUsoZDyj2Ei1a-oRcISMY76KvjSjD0e_zxbjyzazPCoQC6tJT6YQ5KT0iAN23eLqfR0zcUBy3NbYkI3zf9oS045oxl3hhoqnFqHOBr9ZLOhkUHYrHO0NY3UQvZoQ8epGNcql1tOcnV6-7VnDIU0jClXuQHhCfoZNNgNEULhAEai6nf4vRTwqFF7nA1-XzRBi91PG5xnmM2E3UYbBNdNNwKiNZITUhqi44xMUYFd1byPaeUwLNTeYW7XeanedW78rRQ-VHElaiq55VQxnTnZ_aOqJpCdsRaVZeRefM-uD9dyiesmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خورخه ژسوس سرمربی‌سابق‌الهلال و النصر بعد از جام جهانی هدایت تیم پرتغال رو بر عهده میگیره. روبرتو مارتینز هم هدایت النصر رو بر عهده میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/23764" target="_blank">📅 16:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23763">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-PaOvOY3Y2wN3x0Tp_Z458ervsMYibF-scxUkOSua1qYWJuRTW0Rcff1vxtCEf8_8rMVU09_JyM-5zOE6MYgdZ4JJG0Hhyvs_hJYkEkSrn9hJj_FF_TrmVVWPr1UE15h6yQvLbiD_3j6e_Ujd_clRKqBEn1c0pSf04tE3U8r2ocRMK4clHpxDzjIWJBnW9XisnOZtkP7iES3NJavuxyB0Vo_506uWpTURJoz_2keksM8T1YprUTQR8u70HCNuHGqofoat50e6_ZKpRnASdjUR6BH-yF-T-EdJ-WyDJ-ECdMa_VrwSjdGhvDknZyVWQ9DtZyOS5ZEs8iRWWcr8AAYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/23763" target="_blank">📅 16:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23762">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzfX7WI-NjdhlnTluU79edx5PMvfuOeRW0con4XcV6d6QdaqIoLVge1DjlmPQ1YrvvQnorrZGlOWRYKHu9FA_9fxNEIFNOzPWO50QWMbTP3lkDscZ43fYEQTkif24gpHxC0U5V4nnGaoqJTlFbDCJ_7a-YyUUgrdcfJcQ2nveX_jy6s18HAoIk6qEUlU28_xJJusQpwqn65x97ly1u6ky9tdNG5aUMgkML_yTgRltar6biV57nyZtZ0qHVv1KD62feymovS83X2SWJ_dKUeW4vBccgMH9hhzV2VIQIMjk56KnzH3VlQpmtzZerwRn-Nd_Me7bi6Zp82YH7IW_n9BUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اطلاعات به دست آمده پرشیانا؛ باشگاه روبین‌کازان‌روسیه به ایجنت ایرانی که ارتباط خوبی با او دارند اعلام‌کرده برای‌صدور رضایت نامه نظمی گریپشی ستاره آلبانیایی 2 میلیون یورو میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/23762" target="_blank">📅 16:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23761">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/td-RTQg0GPaX84KS_vQHby6URLhicIkgZBVHrJXJKjgi5W_TkTTG-VIStbPYf2Xi0tV7_FRzTA0wueyFejwyJTXY4eYmwNVCWLOaUxxa8LuHPG6XnQSawVe7y2JK3f-GCQqCcGNFkG12dmVIYWkUu2uEFlKkca1uoTkURG6zAxIub11szgYWT1uDF4oMhEIRSpv-IDiWq4CcK5NncfKrXVAMfleUq-3mrWLf4D7lIS3KzL8EWIxWaRtM_RU3EG75vnJNkW7ho5x8TE-_R27ns1nBVodwC8QODrr-XNKkohz4N99BxOtxxKnk6EPwIAGU8amo5n6AJaqV7Cpyr5wQ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل دیدارهای هفته دوم رقابت‌های جام جهانی؛ این پست رو فعلا یه جایی سیو کن و بفرس برای رفقات که تایم دقیق مسابقات رو بدونند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/23761" target="_blank">📅 16:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23760">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWVHknxVAwzzVtJ3aTFg4WOJ_SuqeZ5_a45lv-ThVVbHvEKlIS0zUxa9nkxFJzPiJW9qFqyqUiG24Szvd4uAwo_7IAw-Ll_4k5xyOlTobxfRg4AMewSHb3I9Bo25Za1F9UZcwPZx6ii_Lr-hE87kCA7Yyo8Te3c2JV7eF4YXlI7B9Elua8oyz-LdmJWTYjUbUcaK5agvzBN8Z-2aDCqtSZuqOhhR4NvgJZXatj-yzBiQ7V-8wgEXsIpSWM6V_gfgx69yup15IUoNzP7tqITWVADBsoxxornpoH417yJ2I4uBt57aPY9GtIkN7tglWZ2EeSopSPjj9tjBYKKHzsp_Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نشریه ESPN به نقل از مارک کوکوریا مدافع جدید رئال‌مادرید: انزو فرناندز به شدت علاقمند به پیوستن به رئال مادریده و فکر کنم در این تابستون این‌انتقال رسمی میشه و انزو به رئال خواهد آمد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/23760" target="_blank">📅 15:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23759">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvVHn5NLdR45cVaIjPWVcaNnO7hRfBLdb76MpToopVhjk2KtX4nthTYaXjFRdPPY1mBxum6fJLL42RySkGCCeky4bWI5zW-dIAqQnaUec4SBDdhwOspl7uOOmSZRkw88YDuWE5z9pyYDzYX7hlM-XT9nNuW_YoQLY09kSKcfHmFHyd0AcgbR1zGSur1OEDEHBH6MmtaKPi2PJNWiTvlJ8BWOgxfzqNle6O0SKRGJPliZ8NMJjBMu4U8b7aHLBF9dDTMFI1XSfl8T7V92-7i_jv5afoL6cSM6i9wb8RVIb8_4SlS7MkIhjTEur3mcuEfBW00plZDMn4Upod7uHc7hYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
🇦🇷
#فوری؛ باشگاه‌رئال‌مادرید برای عقد قرار دادی شش ساله با انزو فرناندز ستاره 25 ساله چلسی به توافق کامل رسید و حالا تنها توافق بین دو باشگاه باقی مانده است که این انتقال رسما انجام شود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/23759" target="_blank">📅 15:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23758">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e3fa7271.mp4?token=iAnP9eGwPao22Porxe_UJDmKTQpoYj67iJlRMdsjimGe5wbxvKPWOK2M692j2EPzYLOw-vOcsasaaMgx_TtOwoWvPP2XnTqZeg2QQ1E5NAoTgeHZ80TpxUsd9Rt4KS-OACW6YVcxpF24ZHu_R9vqdmaZyGVCcWeSrEYhdJ2TU4YQxIDKSoQAluycWG0fLu_LGU5pIC112VnSbY-u5EwX0rqVNqVx3GSwQxbBzgpceoh0B64oR0NUZ1B6rXFz6RaWw_RFuq9O-IBuagSVtIzyc12n0HPJN0HFN0Jf_sKejPXeBZS75j79UfGKCFKgwR2uP5L10BCIDp4xAxrd-zjh5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e3fa7271.mp4?token=iAnP9eGwPao22Porxe_UJDmKTQpoYj67iJlRMdsjimGe5wbxvKPWOK2M692j2EPzYLOw-vOcsasaaMgx_TtOwoWvPP2XnTqZeg2QQ1E5NAoTgeHZ80TpxUsd9Rt4KS-OACW6YVcxpF24ZHu_R9vqdmaZyGVCcWeSrEYhdJ2TU4YQxIDKSoQAluycWG0fLu_LGU5pIC112VnSbY-u5EwX0rqVNqVx3GSwQxbBzgpceoh0B64oR0NUZ1B6rXFz6RaWw_RFuq9O-IBuagSVtIzyc12n0HPJN0HFN0Jf_sKejPXeBZS75j79UfGKCFKgwR2uP5L10BCIDp4xAxrd-zjh5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
آندره آ استراماچونی سرمربی سابق اینتر میلان و استقلال درگفتگوبا DAZN ایتالیا از محمد محبی حمایت کرد و اعلام کرد شادی بعد گل او رو پیش‌تر از بسیاری از بازیکنان حرفه‌ای فوتبال دیده‌ و معنی خاصی نداشته و فقط یک شادی بعد گل ساده بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23758" target="_blank">📅 14:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23757">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjqRjP8bhvByhu_5sC16df0m1a6Evy22QYJDyMEWVp38QPliPzRjDShnzYbIVI605GFW-kkGHtmXlP4jTZzdBhBSwOFI8M4w9MXhcQyR-676PM1rS7jPif59Rqvw1KlIAFfHgHfHu6Oz877ihyVJr_vp5q_Mn6A86q_LvRAA4YtzDuCsflQCcx0Gdp1M1w3cgdIDQqDO83dTcCb-5WWIXmn-edGmo2JtieA5tjYSDYTKFgEPhshHrdA7t7HsNYXVZCbWrZTXBdB-jIstz_4QnZboV9jDt2fyIItJZoXsgKTdwBU61fBFfJ57TnVmRoAQegaXZH5Tvu3O9tbxoMSZbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛ باشگاه چلسی آمادگی خود را با فروش انزو فرناندز به باشگاه‌رئال‌مادرید درپایان جام جهانی اعلام کرده: 120 میلیون یورو بدهید انزو رو ببرید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/23757" target="_blank">📅 14:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23756">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xze51gKGFiwnpu9nZ9wCQyJYYAfm2pj7nAeKdt_hbUaasENIfJCCsOZ3v3LTtXLKNWg1a3QxSkeUKhLBqnZ4RYKkfw-A1wlLvOm0tC0rNGpKfYJlhwbs2OJRTEooMpith0B4yAIjp-DE330pl9gj5uWf7wnzPjTUGtGAgVgSrhmsdICsuL6sXCULNesIjJZfxjfUD5oG_TrB5VY7_4Y65yX5BcrBvcc346BCuaqKkj_2E3no6nufawsMItcmPVCTVFltqJbg87NSAg5xiyoTV38lsSfRZl8lBHQemqAi0t4imkit5nox7yFbrJEV4lttTF73B4JuxRK6zbzPrNd4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل کارتال در گفتگو با TRT SPORT: آماده پذیرفتن هدایت فنرباغچه هستم. مذاکراتی با باشگاه داشته‌ام باید صبر کنیم ببینیم چه پیش خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23756" target="_blank">📅 14:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23755">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMLCS08umt48lADR7w_zk6q70br8y0rT31Ne01I1r5_V332dPV6vkv1T5anDidgFw1tmzcllGOsFO-oqpHuCIjzQpB0sx-3t7DyYXu-m0-5qPlNwryk8mWWnU5eYSri-QGQxUuvLoMShN3YmJQs2PQzuVtJSumwr1p1StxP6RAMVW_oLuUIqaiHhldqR2SAphIhEQnVymFJQHTDzBSEfpuIxAXvwepdmYNORBh-Mmzbt8DPfOq_s50nQ37in29XgJ1UUP_vzm-_XTUTZFXFQUT8F-ISXD9iqiCqElZHikvnCS4xP9UE8HSmX1Wes8C9xNw9kzappch3ZZ1DR2abDow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای‌فسخ قرارداد توافقی با اوسمار ویرا برزیلی به توافق‌برسند سریعا با دراگان اسکوچیچ قراردادی دو ساله امضا خواهند کرد.
‼️
مدیریت تیم استقلال در ابتدا مذاکراتی با دراگان اسکوچیچ داشت اما عزم‌ علی‌تاجرنیا برای اوردن این سرمربی کروات صدرصدی…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23755" target="_blank">📅 14:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23754">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIuehS7dJfYm-sMCmMgJL9efh15DIihJ6x_HMzio1sP3TyuNGQRiovYAKRNKhTlKM9zXZGuM-bGm7ywGp9a8sM-luvaFnw_nwfW_Xlvvay13kW4pLi_lFBA9U3grlemRzzfaZQ8SPxWBMKOTOfcMXbre3SMVzbAb3pxQnjvTuDIOcDH_kF4wgeQE0FmGwU4dLrBm9Ojz4YCG0EvKKGLk8y8qPnq2j1pvOyKXQr6PBGPN8RE9pOekWWftFF5TxHxkc7cWMCDt-33P5jN3AgvejZrbuxdqogLhH2igmrPB4Nw4Yh12abrzF4I6ECyxFMGJHtmFV_rkT9MoFT2Gdpq1Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جالبه بدونید مثلث خط حمله بایرن مونیخ در فصل گذشته؛ هر سه تاشون عنوان بهترین بازیکن زمین هفته اول رقابت‌ها رو از آن خود کردند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23754" target="_blank">📅 13:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23753">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdwXcgtB61ohOjnU5DLW9_txFPmbX5xE9PVIpBuzCEgEiv2C8YLtVP5aKkppjIUf7aW9BJmVMirecXlgG-uF1xt1gzNMX85RVe8LQS3tF-_klx4G1dMJ6oCU28IJz4JITJlKmcVovU4vSjH-SJoYU27YcIH9w6lO-Ra-YwfNb7xPodowsnZnU_Tfcle89_a_NMfqbfykb4tAalJHY8_JiTe742dmi1NfOKXRXic_7aC3RScUGziGrL2j9HoZn8jHSYqnZhuTQ06aymJURt-GWrJN16m4xEDUIzL6cSwKU64HQ6UIWRcNtWKyfLOyEWzl3Cn3jR9fMfENRMAXzGtvRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک‌شهر برای دوفصل‌حضور در پرسپولیس آفر 2.2میلیون‌یورویی‌به‌‌دراگان‌ اسکوچیچ داده که مورد قبول سرمربی سابق تیم ملی و باشگاه تراکتور قرار گرفته. حالا تنها مانع راضی کردن اوسمار ویرا برای فسخ قراردادش با سرخپوشان پایتخت است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23753" target="_blank">📅 13:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23752">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-fKR9yms4t8ob8FxiTj_TXbJXgXR13Z1nIlbXj3_xbIY5H608e3SwrDqSAL2Qd72y2CgAXf6Sy23lTZz7mMwL9ViAvI23MFn0pQbbStFN8-fSxIhhE0M59L6aqD-LW1KIN4uxhlnpQyEmJ-l7CUxU1dT08LdJe8oZn1JX30dRCthZeUB4G2l5HI1dwS5eDLZJmmvbWCSYKMA9JbQONPLoW0bjsHg46Rc61OgeyTJ8IZzaRecTgwKu60L9GToRKCgJ-3n760-oybDUo_xrNc4UXy1-8YL1rq4EjNcADzkwVVr2JE2Hwn3fCNCDIfqgg6oMm5Exk08qGTUSXJJHF2DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وضعیت عارف آیمن در جدیدترین آپدیت سایت ترانسفر مارکت؛ اعتبار قرار داد فعلی آیمن با باشگاه مالزیایی تاخردادماه سال‌آینده هست. بنظرم می‌ارزه این پنجره جذب‌بشه از فصل بعد ازش استفاده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23752" target="_blank">📅 13:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23751">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10541c5fb4.mp4?token=lXJoSYd0R75XDdo6r-u86uSagQGWfKf0hRGm7dpCStV-MMpBFH25PotD_F0kANLHDNpXXTrAyNWAvsAIqgwBQjLucmhgwRvwXIWyxYRnio1ioaN_G59KHV3vLVkLYm3axxEFGnaaK_HPRB-lZDSrKORqiAXaZzkUN0HIDhFIuFyGnZIgDxPrC5gUeL5A7g70xLFYYnNtIYZkZbLRLzWq9BCR-f1WwQpGrnEExL5tx8tSRuIFTg5Zu4-psXCRxOBIzbYJ7ZEg_FPvXz7dFQfESWjGTnGQmW4pLMj7d9jGTFq7kKQfWSJPLGjWYWGtnphpgRDZaqH9FBIRxrgB_OPLMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10541c5fb4.mp4?token=lXJoSYd0R75XDdo6r-u86uSagQGWfKf0hRGm7dpCStV-MMpBFH25PotD_F0kANLHDNpXXTrAyNWAvsAIqgwBQjLucmhgwRvwXIWyxYRnio1ioaN_G59KHV3vLVkLYm3axxEFGnaaK_HPRB-lZDSrKORqiAXaZzkUN0HIDhFIuFyGnZIgDxPrC5gUeL5A7g70xLFYYnNtIYZkZbLRLzWq9BCR-f1WwQpGrnEExL5tx8tSRuIFTg5Zu4-psXCRxOBIzbYJ7ZEg_FPvXz7dFQfESWjGTnGQmW4pLMj7d9jGTFq7kKQfWSJPLGjWYWGtnphpgRDZaqH9FBIRxrgB_OPLMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
جذاب‌ترین‌بخش‌های‌گفتگواخیرامیرحسین قیاسی با مرتضی‌پورعلی‌گنجی‌وپیروزقربانی دو مدافع میانی فعلی و سابق پرسپولیس و استقلال؛ عالیه ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23751" target="_blank">📅 12:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23749">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/crbscOekK8I1xBGthwxPpqazPxlZxrFhRrJ02oQf4FMBcc0dNjY2kKtEQj1YSEHAzur2lhArb-DAzEUIqFX4_uTLCpXAxadXbFYvB_oLo5_sgtlSD1Vlpc_DpJonBXoPau1kEhYiELlshj_KG4JSU3CZKLzKjSskLWZXXvTPIbc0dnuKys_jYiOGHuAdU2BNd3lY4BRC-tdjn33hlivahmeNPIRG50JQqQtcs4lt3fxCkMFCX5u_OJAoQvLfgfzzUq1ad5E2HyLQ42DuI9EhOLXfBtPr2-4tS2WCoWOu-RACYfhLKJ5YlBPQW0dp3-MmGF3ofgx6n5XY9Du-HYh93g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z2Z_3M_ERGPrZ3FFbE3OKZUgzh3kfU0Rk7VvbLCt4TfmpIBfze9OkcQaAk2dFfd242CpsMT-XKGb00J5TGQtx0WyHBbWLQHl72_NR_i5GFPIDvhuHalDvYBtMbnWawSgvz5HOcRNywApz00U33q249PIabqm10KlKNxZcaWai8Sj9HnA69_jBitqMsPzK7HJwW_B6dbjjsQ2vMFJgfW_YlEowadJfwvrBxGJvjNrxcD0i_59M1Gi4b8fl5Ynk2LvlaRvE37oNMhWn7mWqolMYvKWvL3QYjV9heZ3t7rJICKoeDptPZdwr6bcg5dKGFCNlkLsmnCZx9NiApqohlgiLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
📊
مقایسه عملکرد آنتونیو گوردون
🆚
مارکوس رشفورد درفصل‌گذشته رقابت‌ها؛ باشگاه بارسا بالایی رو جذب کرد اما پایینی رو پس داد به منچستر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23749" target="_blank">📅 12:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23748">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmeCavFp9LdrS0EFKBCFsDfAIEqhk1nBS2-vYaCnVG_AUw_eHaBGTlBNcr8s_uc4MqgDU3_-KOcTZ4Hye8tcYskt1KnyBnbjV9Kr6ApUTEfnXg1bykkZ6SDmaC69gLxRLJTazAZCOxb1WVZCXDI3NO2B3prtuny4Dvi-9mgGFOwDtJL8EmS9dSpZwhQnVf0LTgjvxwxANTDTOuSyOeX6dn5_gVFFT48_jk60wPSbuDYUDz1Iiwzgb44kSGyMLQ0CSDq7B4B3izFke5DXNNXMWneKBcIy8LGkRbQ6iCcPxFKhrhOHiMm09xD1t3Yi9DWEEU1mO0urBfgVanOiCh9_Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23748" target="_blank">📅 12:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23747">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e75ce8522.mp4?token=gcvx-Z5P33036x2CZAj6HlVQDi584U6TXbd3NG6HHnOeKy5_Y0iJs5ZulN5SzOJp5HK3hRoKUPq2UleuiwtawEknWlRstS-jFyaJjssQGcbsp7TRm3sIQIT5gkkWtSzb0djlsWnbYSllMjImF77j-xEBBP5bCW8SDYxySKY9zt357RN_RqwMA1ietsCbSmlMgWEtFaHEryqBrVF_i5FaZxajh4SMlLZZk5eSDwwBgn3jzj-JSbMUM6J4fMaPIXuK-wOrVT8dYql35SGVBmAiCYQ1apig0ZkkxrMTYO_um3iL47Bu29u-DrgFYSFYwGnCyAlTlXp66JbOYlWaUTzZmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e75ce8522.mp4?token=gcvx-Z5P33036x2CZAj6HlVQDi584U6TXbd3NG6HHnOeKy5_Y0iJs5ZulN5SzOJp5HK3hRoKUPq2UleuiwtawEknWlRstS-jFyaJjssQGcbsp7TRm3sIQIT5gkkWtSzb0djlsWnbYSllMjImF77j-xEBBP5bCW8SDYxySKY9zt357RN_RqwMA1ietsCbSmlMgWEtFaHEryqBrVF_i5FaZxajh4SMlLZZk5eSDwwBgn3jzj-JSbMUM6J4fMaPIXuK-wOrVT8dYql35SGVBmAiCYQ1apig0ZkkxrMTYO_um3iL47Bu29u-DrgFYSFYwGnCyAlTlXp66JbOYlWaUTzZmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
رونمایی از تنها سرمربی حال حاضر فوتبال جهان که در چند ساله اخیر تونسته ژاپن رو شکست بده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23747" target="_blank">📅 12:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23746">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJTJ8cBWwEUBY89exFkROOP9Z9jOeVf_bY1J_YEn3E9uJkGoH2xa5kXdjeOtKPLe-f1ftvtylF6nnh2QxRUhsNHlm7X9u15jBdyxS0NIhHvOYPQHEQk7ZTy4bQYsnSRJZWRby3tQklvy4U5a69GUZo_QLQQ3LW1gsp2jkQXDGMPOCwYqiDt0AyCJS5OxEglIF0sfM3vZleY0-ZgXFVSb6qRrF_29_UK3CxwNMwRodLN-g8pi4KYeODGt2gEv4ipx0DkimWgwNeCuZ24BZ4J8B-LAHyolnZyDPmxxRY3mi-i-2s04hQZ3_iPsw40R1cy1sGPsQxZVBniIcldJC5UwMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مسعود پزشکیان رئیس جمهور بعد از امضای توافق‌نامه با آمریکا: به مردم ایران قول میدهم بزودی وضعیت اقتصادی کشور بهتر شود و قیمت‌طلا،خونه و ماشین روز به روز خواهش یابد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23746" target="_blank">📅 12:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23745">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqGBK4wO16OfFsNb2SEcfTHmBq0hNxie00wyEw7uAqMq3mu1vLe-FNKfHlKogBCWQFPVPbOWwMeiPkhPpxQ9G67fX14mw0CH98u3YbsHsHtSGBj1muEsn3cebbwSUd8tv9_2eWqBupV2jybqwfIbwKPDPqLQr7Mj3ZWIci58ocwivXdjwTk1U77A0ZH2eY-KncA_4J5g-MqlJ37gqJwJ-dIn8enC_df4LPEEmIP84WmN9Id9PJaW_Wmg8p06fMfrZdzTxk0NTZvindr3fkFEstOuf03EuMeGYxnw2J_o4iR92gHDUgnCGMg33GIwRcawqSlNh7omulvr1xu3hFKvtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌رده‌بندی12گروه رقابت‌های جام جهانی در پایان هفته نخست؛ از امشب هفته دوم شروع میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23745" target="_blank">📅 11:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23744">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co6koHAZ8xzX6li0GoGIo1ELAYRojPCkZmYTGwHw2vAcmewdxeXuRu1y1I6mga5EsFNvdQojol4LdZLC6VF2teSqHjbj_8ZA-m9bjA4W5qKr7Scs39z-Uxyy4ZfoEccLDBKLI3YA99Ywk1gUUCS4aW5SinqGiu4-y9jUSweQb3fp1OiWjKHnSGQau-sxVaXoP0DUxcOstmI0t3e4I8OBkNZ8fgbyStbZbfgoesu8-ixQeqTx0RPqqk77bIocuqPRrbw2EJqSHFGEtyOgfHki0eVCq7CPndJNGqhZSYhIRpDQ8Rq51qWY58TlQNv5oghH0AsyZa-i1sCeBnDwMEUMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال با نیما اندرز مدافع راست 20 ساله لگانس واردمذاکره‌شده تا درصورت توافق نهایی قراردادی پنج ساله با این بازیکن آینده دار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23744" target="_blank">📅 11:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23743">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">▶️
قسمت‌‌‌هفتم‌ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت‌های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23743" target="_blank">📅 11:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23742">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f495fa66.mp4?token=rpkwMzAuQ1iXdHi9piwnByjeLSsyJDgL_zHfmiMwBDhUAq2DG3Ct9ch12F9qzCs8haQTkCqQkce-Op9K9tewuiBlmb2464e8F74xptHph6t4LB0uPO7ldwRETAKIfH8ooaMuOWeJtpTV3elrmhNGvnNlUbE2RZJ3NikZ3Obo8bE7tINGNUAteOdeTmquHlunNQPO3rs_6ac6JRoHM2OGMAbCvmzTjxknVl8Spd5vT3NITunB7j7He3jQoLF0pGX3m6OBxitbxYEAjc71vOULr0MwI_Zcatqz8AQ2MD1WkLBo5uzCvYwgu_2Qg0eSTVXbYocU6xCs9cL96Lwcg-pNlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f495fa66.mp4?token=rpkwMzAuQ1iXdHi9piwnByjeLSsyJDgL_zHfmiMwBDhUAq2DG3Ct9ch12F9qzCs8haQTkCqQkce-Op9K9tewuiBlmb2464e8F74xptHph6t4LB0uPO7ldwRETAKIfH8ooaMuOWeJtpTV3elrmhNGvnNlUbE2RZJ3NikZ3Obo8bE7tINGNUAteOdeTmquHlunNQPO3rs_6ac6JRoHM2OGMAbCvmzTjxknVl8Spd5vT3NITunB7j7He3jQoLF0pGX3m6OBxitbxYEAjc71vOULr0MwI_Zcatqz8AQ2MD1WkLBo5uzCvYwgu_2Qg0eSTVXbYocU6xCs9cL96Lwcg-pNlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
واکنش‌لیونل‌اسکالونی سرمربی تیم‌ملی آرژانتین به‌سوپرگل لیونل مسی در بازی مقابل الجزایری‌ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23742" target="_blank">📅 10:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23741">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrXN8V-UWjX1jSVtcwvAYI8Ez4Zsei4dZcBcBpgCDACSLd1PDSDbKjXqAWe9WRtxHJEj3dnu9xM19L9q4-VmAdlodMcF9xauZuUxeEq1nqZnHdo9upvXOdLMvWVJsSVXS0gSkcylJGy-5u6qyX2RZcgYWKO6m18Gj85yixmWbM58Z7dp4hHaS1T-3VJEyVvhWFaekhRy5GIK1OlOZeknjz_iSwtytYhVXpKF9fY60ZOFeUPVYqjm0jJAWSdLNvaoiejda5Q4KcJEeYAbFa7VnA91RbSBh2o_c2kKOqtRzwrlBC-Et-aVCybRZRc-8OKWZSD1CkpJdILNmnNhv4bLsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی رسانه‌پرشیانا؛ فرهاد مجیدی سرمربی سابق استقلال پیشنهادی دو ساله از الغرافه قطر دریافت کرده و در حال برسی این آفره. احتمال اینکه گابریل پین به کادرش اضافه شود نیز زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23741" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23740">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaTrX1RmNOqrDSbJF0VVh1T-G8nSIgo35CBYN95hh5WYWgeXyXmQQ6ikO1PUitI8ER03qD_b90_0VvObqxaeF_BXAY-KD5ZRmMZRX37Vh4alnq3iyl70Zd9Co5obi4PLbmlcMJlB4AKv9y7yC4P7m-UKQ1p81K-M8oA4bAdz3u6TA48vU1S9MGrXAU3Q8QWEBk3WHTRbjt6wQ51Jk_bZ_CVn4Kr76_fXie3KfRS52HO6v9QYoMUdphqAawgPxzL75kEt9hydj61wmg9xHjDJnkjnEWcUnMdnyNOHmq9iUeM-HcHY16YpGhQMrfqY3dmWN-ZBOhho8_R0mP5U3g7pkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23740" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23739">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TR2IImgbLIyFjE0wJI6ZE63R1369opqolYZkmKdE37NalGNLOiN-S5m3pJHaNVcbPNfdq5MrMNwP66ZjN_zAWkiZ3zU6Xpf_F8R_5qwGKY1xyjO4OvSt1o4WIwAtCt6FpcK62Zw2bQhrx2qz7cm4Fmh2WGJVq3NqkzuVNF2JCPsvLcaSzMpBfkdM2crrwsAysdXtLgkf8WJu-TIDC1W-1SVMU-notb7S8ASorEfZ8g0xR-HjZngKLXSY6yX7lV71F7togIZl3TltOrmFUlk4xZRRaNpgBuHB8jAY6w8i0fKV4e4ID_NjW7jfgTf61Anycx_7Eeqm2B9rns3LGHZ_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
دیدار فوووق جذااااب
سوئیس
و
بوسنی
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای، مطمئن و درکلاس جهانی پیشبینی کنید!
برای ورود بسایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23739" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23738">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3M9UEK69Ns9SZfYd1o1uDYRuDugxL0YvYuaSdYGOPvBl-QH6Pkj7nc4rYeI8clCw0IkKv5w76o_ImKna43ngOoe47G97wda2OgtTkR3RUPJnJFbLowqLowiyYobg-npUOjSxtxCZjSAKVgoQdd0xf10J9rgdskwobzGKGdgiz6K-0yNz41uHkxmkjvmoMD2748JQwLjXTFgD1zPGYV3iZTGGcBBbg7ZratLijzKSLgF65tE_KdP_wvdC0xdKToVp18pc-KxfOIrIOsYvU-v6clXU8VoYJlG_eG1HjrhTRsFTzUvFXCILhoi5KTP7pYgViMp6zGINmGpGDTFrhmQOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛مدیران‌بانک‌شهربرای‌عقدقرارداد دو ساله باایجنت‌اسکوچیچ‌به‌توافق‌اولیه‌رسیده‌اند و درصورتی که هرچه زودتر با اوسمار ویرا فسخ کنند اسکوچیچ برای انجام مذاکرات نهایی به ایران خواهد امد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23738" target="_blank">📅 09:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23737">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc17874c.mp4?token=eexM9Y9VRwX5gPSR2dmr7lo-uJZdwmmwA-OvoGKmQi3uqYuyD6l2uzgEfndKyiMTBIFYTf-0484JzjiTato5yLHQ6q6W0C_aJE_jGjr4ZG2Qv5ZLm9_67mSHFQsyAz-DFjitubzvUq49pwjJHttKpacyh9wDR7RFmPmpLGQ-SW0hJYSMbLpQ9zoH4gHlJ3zkg2P1Npuccic9_QUtmVTfGx6LWYWatMjmMg0PmCKRDoXK9ryUaS93e-h7qr4rtlmGo_bGuSOiEbIbpL0EqTzXzGZE09R8KrJvsPHSnZyUqAuZ25WCOGVTvwaWguwGrwWVX773jj2zzLKaCAcrk5_QqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc17874c.mp4?token=eexM9Y9VRwX5gPSR2dmr7lo-uJZdwmmwA-OvoGKmQi3uqYuyD6l2uzgEfndKyiMTBIFYTf-0484JzjiTato5yLHQ6q6W0C_aJE_jGjr4ZG2Qv5ZLm9_67mSHFQsyAz-DFjitubzvUq49pwjJHttKpacyh9wDR7RFmPmpLGQ-SW0hJYSMbLpQ9zoH4gHlJ3zkg2P1Npuccic9_QUtmVTfGx6LWYWatMjmMg0PmCKRDoXK9ryUaS93e-h7qr4rtlmGo_bGuSOiEbIbpL0EqTzXzGZE09R8KrJvsPHSnZyUqAuZ25WCOGVTvwaWguwGrwWVX773jj2zzLKaCAcrk5_QqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌داغ‌وسنگین پیروز قربانی سرمربی فجر سپاسی خطاب به حسین میثاقی مجری صداسیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23737" target="_blank">📅 09:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23736">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6e6215526.mp4?token=m8LGOEpvimbMppgqQ9iSpR_orsoJtU3l6sNdKyixuSQyqIYuBT3fl53r_Da6BAsrwBjccYGEfTtE94xrxHYz_qQPXoNktCti4LitIH8WxmWqyyuXvaACVHTfHycDdLaBEGmTqts5Z_ViwaTFxwd8kfv8qwe_V-nYVI6ni87ODksEDHrQZgXs7e_te5P4pjcwokXChOokbHichbZzIRyGqOKujYuuA9hLE5WY7zEBNcbnobbSyAscVnxlsY10EyNUMHiLei8DnCSzeixfM6BSeuzpf_60RTRh2JMHpYPUwhHWK27EDfnIMdIJU4g56MFFTscfYKLRWQForh6s-bpRlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6e6215526.mp4?token=m8LGOEpvimbMppgqQ9iSpR_orsoJtU3l6sNdKyixuSQyqIYuBT3fl53r_Da6BAsrwBjccYGEfTtE94xrxHYz_qQPXoNktCti4LitIH8WxmWqyyuXvaACVHTfHycDdLaBEGmTqts5Z_ViwaTFxwd8kfv8qwe_V-nYVI6ni87ODksEDHrQZgXs7e_te5P4pjcwokXChOokbHichbZzIRyGqOKujYuuA9hLE5WY7zEBNcbnobbSyAscVnxlsY10EyNUMHiLei8DnCSzeixfM6BSeuzpf_60RTRh2JMHpYPUwhHWK27EDfnIMdIJU4g56MFFTscfYKLRWQForh6s-bpRlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دکتر انوشه باتریلی‌از روی ابوطالب رد شد؛
تو عمرش اینقدرسنگین‌دیس‌نشده‌بود. عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23736" target="_blank">📅 09:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23735">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7467784054.mp4?token=G76cdPFvuK1wNIPsKMQy2uZIuxSXhTnCa707gVe_YOH6yGPOq6mPap35XpFZWn0x1XZt25Nu84po9v84FdHjiX146eHl717pzibXd4RBNvmQVE6UKIBGOW1I5aYsGvFOo_6ROiecIG4Pyk6MY_IReKCXhXJ6B6LSjCKYGHDZhMq5bYYWfWmPXD4NgadRQo8GsaL5sIGvD0_zDHe7ky9UwzK6GiuOB1TL9qsMC5j45ScsXDo_ILNK8Kew1-DxgeYl1DFJ25AaH_CVeiz1NnEsnssGgMcExMSxNLrhxSrOm8xRQLGn0Xh9a6WlICvkmRBS_TpDFHcyMmgt4SpIVH1fkxtyiutA4crxKcuSFIzGqfqDUuRlLIPvHyliyuaQnjByO5Il2bILT3-ceqeRRCeHh3M6gVVGB0DIzz9I8UZca9jJF2-DqpVofwdw_V6TpbtZkM9vE8I4rSIebaybZc_xZksq6jjKroL0h8BWb-0vlZFQWfdYa2q5dEMePzZs1owqp02mhsfeB25IokE7oROQKGOZDt-1wxjguDbZpeqlx2ISnLdGbPvkCDlwfuKIR8_h4odSGXlZ6UiViTL0eh7Kno9eHp8IIuYZOsrJzCwlhaaU8dIrcocET0OtB_Yqcob72_d1mS29PvlzEVvsMd9oLLdOvb7wxtqK6T_kXmYhaew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7467784054.mp4?token=G76cdPFvuK1wNIPsKMQy2uZIuxSXhTnCa707gVe_YOH6yGPOq6mPap35XpFZWn0x1XZt25Nu84po9v84FdHjiX146eHl717pzibXd4RBNvmQVE6UKIBGOW1I5aYsGvFOo_6ROiecIG4Pyk6MY_IReKCXhXJ6B6LSjCKYGHDZhMq5bYYWfWmPXD4NgadRQo8GsaL5sIGvD0_zDHe7ky9UwzK6GiuOB1TL9qsMC5j45ScsXDo_ILNK8Kew1-DxgeYl1DFJ25AaH_CVeiz1NnEsnssGgMcExMSxNLrhxSrOm8xRQLGn0Xh9a6WlICvkmRBS_TpDFHcyMmgt4SpIVH1fkxtyiutA4crxKcuSFIzGqfqDUuRlLIPvHyliyuaQnjByO5Il2bILT3-ceqeRRCeHh3M6gVVGB0DIzz9I8UZca9jJF2-DqpVofwdw_V6TpbtZkM9vE8I4rSIebaybZc_xZksq6jjKroL0h8BWb-0vlZFQWfdYa2q5dEMePzZs1owqp02mhsfeB25IokE7oROQKGOZDt-1wxjguDbZpeqlx2ISnLdGbPvkCDlwfuKIR8_h4odSGXlZ6UiViTL0eh7Kno9eHp8IIuYZOsrJzCwlhaaU8dIrcocET0OtB_Yqcob72_d1mS29PvlzEVvsMd9oLLdOvb7wxtqK6T_kXmYhaew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
10 گل‌برتر هفته‌اول‌رقابت‌های‌جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23735" target="_blank">📅 09:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23734">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23734" target="_blank">📅 09:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23733">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDk-_1dKSiYqml-Q3ONOs9QSPinC2jw1uNd56a8PRmvIakRqp4TmWT8lM2VwqFsZoEtGXU7rvCfOoqtN1lu6nDJ-75DeYA8cgIAM3Nw6g3cQCRzKohEJcTdC63OlTJXb8MvzNbWdbEpESd-nxdonmikanwtJpjXMJ5ALcgK0MFiw5CJxb3wSYDqRM5sfGNjBXpRE6wHzxLrEZuxmhFrXj8NCsKpAS73uUDt6aFRfTpVdAkrEqRff8nztAT5aZbHcW57CCeDxecuX5ao_-Np9uCoO1m6kVy9krt7hj95MDVgNpiVi72QADA8FbM3qDowYH7uu1movTRLvgw3UuY5q-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23733" target="_blank">📅 08:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23732">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZ8_on0ir-Gu2v6xp2wIXSPjmCHINBlGpCYkyRCQ-m_cVx1SaMsImqxFwDeDd1EkYYnrqoefOkkQcKjUeHCAI6QhTM1ipnNcVYQ0iwcBCRI5idpQyvoO30mJwOwVNPoU87dBC0upe9QLj-BN-pXKgKbV6DmKMojhi2QpH-xo68hactRvbDRx8xN1lJU19Q28ekO-GAC6CliuNQDqRg7Y-SXj-RdMa3bUk_Bvi6gn5MmQjp-TDFr-957MAxmUuqcPZEjQrQkcYn-WmNxK38u1V1S35jGR6ZlVLkwDTxw_eljFVv_l1eXDj7PYOeGMDGtlq61WL0t0ZizxGzLGVhjhUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23732" target="_blank">📅 08:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23730">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nuCjeVc_Tmuq6SktuDs72hNIsHAhMh_6J6Zy8YBxqLxrIPWERr1r25enuaGmrCcv2nM2tVNflV5NBPYF-cH8AbfHGW75zPfE4KyVT0LUOK3hOXWnWF-pEEdcUIADwjiUjFWljZde0pgOrOu4-5_YFOT1FDrbXaRCGYKlKissrwzFRk7ybAtNhXm5Nf9l3f2v2wkgbbR3B1MEZsecAG-6tNMsSRoRa-K9dS3crOhv2rkbcRR0D-kMk20-Y5zoTl06Ukkh2ekdRTWgmVeBymiBP95C3CYb6GVeYr-7gSt42veBG3LEpFp5xu1sfvB7CvH5zcP6sVXlodY6R-udTftzaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ECLL1GnnQDo4WsR_FBWVqZFHwOQCFW1qiu-TTTmz65hhq31GUgp9LurFTGd51jAyQcjN1VCMUGVo6EDiYXHHuScMItRn9E8pEuSqpICSMoyQWn9OYpvclu-sDRG6h4sXhXdO3N7kavgKKqhZHDc7tw9JxsHR5qYv6oOmKryZyE-g5emCNAwi5QeRvnzAnkfiKmcFvGmaOM-i23ih4lcVIRpxnBdoLm6k8ppAE6695tKIxMmkQiFtqw1SQP2lnlDWmqw1pePorMSQDTg2gFKFGYKA0CNTfZGkkwTAq5hZ85gD1ZPj9liKnwwuFXBHYyTwH_mWv5c63FoZiawr3fSoPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ ازمصاف شاگردان کارلوس کی‌روش با پاناما تاجدال یاران خامس برابر ازبکستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23730" target="_blank">📅 08:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23727">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oo7Jkm63DTrSRLgv45VWjtNHL9yLi10pBIrrJ4tL9gu_ThKIHv_40ER5eZQLVRgI9WqnmroVPjF37bINx4u12F-lqBWAKgCKABrKrCFIudupLlO9SBUxyoA4jO-f3VEQDN0lVQhSUGqIaNU-C-ngyiFpGjjSoyR9Z-jtL4OctmM7TT8rKzzD31JJPI8dLVGN3BiGg_IzFVxNDODVkOqHnOqQTm8s0G9vzwOKqgilLL_N5SIMNAET0ZgZ2HOHYH-qMG_jIT1C4aYVHRBnbdK3wAS3GGkyqC6aafMpmuutBBlwWZZQq7sGWwgNsbuEBUWkCnYrgjvmg3RLDyXi9KkjZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نشریه مارکا: باشگاه رئال مادرید بزودی برای جذب انرو فرناندز به باشگاه چلسی آفر میفرسته. مورینیو برای پست هافبک اولویت اصلی‌ اش رو گذاشته برای ستاره آرژانتینی چلسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23727" target="_blank">📅 02:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23726">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fB39Y0WJAm26IbnTmB_8Rm92j2Fb_L2wwX-mid5h5pGE-VI6-EVbCPuvPbo-S6SR8W2vURCF6YlZKZ1Fe1ov9ZWgrvfQ1eEwgm9FZm18taHo3xd4ExFoIFRmZPsh1kdjsrRCSjzdIvTL1rb6VeMDQvJoR3N2d-_s376e1zwXWCrGtC5tU9knpR9L3WgM_cZ0FpA4luvrz-4N5IDfvT-QQcSQUpmvz1xdT2muF6Hml2DVr3m-ESl1zJ2r0P0_EnU9lnAFtasrEH-nbp3RPY26C2iVdp5rQbzJVDYsN1hWw3pCQHBH4SJeSHLq9K8AOyeYG-kPqtQ877MBRtcHie9Ukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ محمد دانشگر به مدیریت باشگاه استقلال قول داده بزودی 18 میلیارد رو به حساب باشگاه واریزکنه و کار به‌شکایت و دادگاه نمیکشه.  قضیه از این‌قراره‌ویلایی‌که دانشگر خواسته بخره یه مبلغی روکم داشته که‌تکمیل‌بشه به مدیریت استقلال میگه کمکم کنید این رو بخرم…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23726" target="_blank">📅 02:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23724">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMjFgUHeiQ_XKm7YzJYKVA8cAa5Hcovk8QDff3vUKzVeLS0kiqde7j6FxunSrCoC6fplg7qx31EiSsCHxdcjFGaPbXqE1ufnKfIX7Yw2HXLHCL1lc-6hKSCrGKEHOIuPWZzarqsLvS3GSv618Aca_7JIgaGg17fDk6RCJ05_bb8LScTNsMh6SZNeA9fDKudHHCqjzgBBs_z-A0xXKf-16XfbMCKWyAB9I4CnS0H0wa5llcDJmzL13gVGOW9tINE2Gx7fb-Ry5i0TLN6TCZ2mTbw1MjLos_IoBxzRXzdmWMFbe4zZwKY-hSitPAf66w80Wd97uiT8POi_89msq0paZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازمصاف شاگردان کارلوس کی‌روش با پاناما تاجدال یاران خامس برابر ازبکستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23724" target="_blank">📅 02:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23723">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRheIkdHr9nuAAFizYuHiRaKs1Wo3WwaIw1Gk__JQzqP_gLgHHCVK0oTlS9KvQB0h4523OZclAm4B4RqWOEPGToocUeqtFYHlwjKkCNOReeKUxwe1-X-gV6cDJatgkclmYuDLkPC3Z2p6Gzt4Fjz_NcVJD1DAHGL0_y24BgSD_AOm0dI_xdSraKUFy2SkC9wFD9DBqFVX0NCp7thvwsr6ZvAS_N0Cmzu9n9fkxTw1YL99eufyNVy3G1Qw6QEPP7zZSbK_wyXFx4T9XbL7y-2abLCe2UoX1iX96-22Prc2IHFfh2OUin-mMqLYixJewyIUSmJa53-8lTSlgZBB6VKQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌‌دیروز؛
از هتریک فوق‌العاده مسی درگام اول تانمایش‌درخشان‌سه‌شیرها مقابل کرواسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23723" target="_blank">📅 02:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23722">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b735dd21e2.mp4?token=Io1XlqB4nyayt1sh67Le-4t9PhqSKFHB5JDUuqXl9jgAtnA3W796v1-KH-CehjIvpYj192R7ltNpCFenN5k2gt12BsduWBDjkksjgMvfNBzWTGXh0nRI8LgNoyEvBvtWeacEpIDhDvyYwb83rH83NSfIyTC8K9799JUBilM4_E_8gKgMhuLqciVKl2stAMR8gPknTcd06cKK_wcHg-wPXlh96iTRyqWDNasl1wDJqASD2OEjZXUPMS2vK__3yOzebPJmcgzvT67yz9kY4RnOWYEi-Rxl6tPeTu-wDnAc1p3wZEHonOl-jbR2gGABSmosleBciu9ZX-7e_ieSCEeQEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b735dd21e2.mp4?token=Io1XlqB4nyayt1sh67Le-4t9PhqSKFHB5JDUuqXl9jgAtnA3W796v1-KH-CehjIvpYj192R7ltNpCFenN5k2gt12BsduWBDjkksjgMvfNBzWTGXh0nRI8LgNoyEvBvtWeacEpIDhDvyYwb83rH83NSfIyTC8K9799JUBilM4_E_8gKgMhuLqciVKl2stAMR8gPknTcd06cKK_wcHg-wPXlh96iTRyqWDNasl1wDJqASD2OEjZXUPMS2vK__3yOzebPJmcgzvT67yz9kY4RnOWYEi-Rxl6tPeTu-wDnAc1p3wZEHonOl-jbR2gGABSmosleBciu9ZX-7e_ieSCEeQEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروزکریمی‌پیشکسوت‌فوتبال:
بیرانوند درتاریخ بی‌نظیر است ولی لطف کند کمی تنگ تر از این باشد. این چیزی که ما دیدیم خیلی هم تنگ نبود واقعا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23722" target="_blank">📅 01:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23721">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e924ecdff.mp4?token=TFPia_9crxyu8RggD5FKK8ktJdPhNHwIV_mIbM-igGWbQJaEMy-QiOedNiDPcEPJ6oxxs9b0xJQ_Sy0O3dV9tPa9BN6fa4gKDzUf81zXKyTucjs1DL6wkifwk3N0aFdxp9wfdAVHtiYzBzxcZTFsX60-YdtH0vAsCXWbw9rgKw0sbg-U8AEa92E85A-d1Zi-PRQBTMtKW3hvjbQHRkSmpv1T6cO2r7m9DT2wPXqeGKxgOhhcjy0IzNLfiYkCGFaVOA9AKJhZsrRrEqQv1HhtW-XwBzmHKqDyAjkiCawkQ2y2PTfDOx74-i0ET4MUg-OTFZAsesYSJXoLF_Iv3_rb5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e924ecdff.mp4?token=TFPia_9crxyu8RggD5FKK8ktJdPhNHwIV_mIbM-igGWbQJaEMy-QiOedNiDPcEPJ6oxxs9b0xJQ_Sy0O3dV9tPa9BN6fa4gKDzUf81zXKyTucjs1DL6wkifwk3N0aFdxp9wfdAVHtiYzBzxcZTFsX60-YdtH0vAsCXWbw9rgKw0sbg-U8AEa92E85A-d1Zi-PRQBTMtKW3hvjbQHRkSmpv1T6cO2r7m9DT2wPXqeGKxgOhhcjy0IzNLfiYkCGFaVOA9AKJhZsrRrEqQv1HhtW-XwBzmHKqDyAjkiCawkQ2y2PTfDOx74-i0ET4MUg-OTFZAsesYSJXoLF_Iv3_rb5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی‌درگفتگو بادکتر انوشه در برنامه امشب: باورتون نمیشه ولی من دوست دختر ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23721" target="_blank">📅 01:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23719">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/210b9e3441.mp4?token=VaROBAUE1dsuh8rf-v7I7vEdWana5qc9MQsZJlJeiQO8ndEf2U_3_51wkD1zmUNRVhdPEekPPSDPt5wFWZv3KvOPSIeMU6PKLnrWTh5d1p7RWqBZkVgWxvRNfubrHCxqfZGvhj1-SjCDoN-7-0mUZYS4V3xeWGsVoyxfYMM9cRWr_9RqCc443pTpIo07bRG6ntd2tzUCIlVxIt9hR1KTZfqJNRHcpkpRCg1TZQn0P1Z3cWPhGdAInpDWmn9Mlkk6U87PZXWz9NHu4x6qRQQaOjbq4tP2a8TSu4OtIU81HgwuWcFdNfJBA6dtU1A7F1f2OmhhyvD471sSBy_Ae5snEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/210b9e3441.mp4?token=VaROBAUE1dsuh8rf-v7I7vEdWana5qc9MQsZJlJeiQO8ndEf2U_3_51wkD1zmUNRVhdPEekPPSDPt5wFWZv3KvOPSIeMU6PKLnrWTh5d1p7RWqBZkVgWxvRNfubrHCxqfZGvhj1-SjCDoN-7-0mUZYS4V3xeWGsVoyxfYMM9cRWr_9RqCc443pTpIo07bRG6ntd2tzUCIlVxIt9hR1KTZfqJNRHcpkpRCg1TZQn0P1Z3cWPhGdAInpDWmn9Mlkk6U87PZXWz9NHu4x6qRQQaOjbq4tP2a8TSu4OtIU81HgwuWcFdNfJBA6dtU1A7F1f2OmhhyvD471sSBy_Ae5snEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
علی فتح‌الله‌زاده یا تام کروز در نقش ایتن هانت؟ وقتی علی فتح الله زاده در زمان سربازی فرمان آتش به جنگنده میگ 21 صادر کرد؛ فقط نگاه های پیمان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23719" target="_blank">📅 01:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23718">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⚽️
هفته‌اول جام جهانی 2026؛ پیروزی ارزشمند و شیرین‌شاگردان توخل مقابل کروات‌ها درگام نخست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
4️⃣
-
2️⃣
کرواسی
🇭🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23718" target="_blank">📅 01:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23717">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGUgKg7FZ0zAgmxNgiZ834pheDH9JvC_LPJvfDw-l8VNHCBZ9kmehFKcVUXuV1I204ONuaADxtnCdw67_KQe4WmtQGj2256LfmxPerboylzY4iD3W92H8dnroQG2k4jCetkwRPc5JeNPS88yM4OTJ5h_tYhEZAHW4BSbFTpBiwbgaDfL7E4zIJNIn4wK6GRrBe8nT0OrcKBTXVQc8PqQxFB69golhdxccNjfimkMUXwSU6fxDdO1eA_8gnfvC4uaneab4KdRwKtgn3gcn1I6OCi4UvdgeLQieeCRWONYdtXNKpGEvvZljo9SDiYZEhb-h6kjo3nKeDaIO7jYwOru5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هواداران‌تیم‌انگلیس پیش از شروع بازی امشب؛ برای ترامپ شعر ساختن، فیفا هم اعلام کرده هرکی شعرو بخونه از استادیوم میندازیمش بیرون.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23717" target="_blank">📅 01:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23716">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d2128a8f9.mp4?token=ubRwTsanbg7Ws5k6jmiLswhruvRK-cPYKEvvMA9pQXGpHuqSVBQNOFQYfFiuu8FPKDzmgg9gdYcwJnmYkTbqZHjboqjwcioZJMT03ancKAX0xaNVo8_8QQ1oOjABRK-P4pFbJfi34qsRL0HGhN1RoD1jP7JPVCIVCObT1bRsMINIHbK0i0JtEEdPT-dKBdlGhqIYS4N2CCWkAP3drHi1RLKXUYNM5arfTioGLEY6LE2eqxNa7FFI061pclx6NSuFRc5fhyULNX4sZM55wtFEMQc5BfCByRyWDZQVrl6np958SJ7BCLsoY-Gaw40Qj5m7MyZhqR940Fv-WSynZ3voDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d2128a8f9.mp4?token=ubRwTsanbg7Ws5k6jmiLswhruvRK-cPYKEvvMA9pQXGpHuqSVBQNOFQYfFiuu8FPKDzmgg9gdYcwJnmYkTbqZHjboqjwcioZJMT03ancKAX0xaNVo8_8QQ1oOjABRK-P4pFbJfi34qsRL0HGhN1RoD1jP7JPVCIVCObT1bRsMINIHbK0i0JtEEdPT-dKBdlGhqIYS4N2CCWkAP3drHi1RLKXUYNM5arfTioGLEY6LE2eqxNa7FFI061pclx6NSuFRc5fhyULNX4sZM55wtFEMQc5BfCByRyWDZQVrl6np958SJ7BCLsoY-Gaw40Qj5m7MyZhqR940Fv-WSynZ3voDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چه‌غمی‌داشت؛ یه‌روزی به‌خودت میایی می‌بینی دیگه پلی استیشن رو گذاشتی کنار و بازی نمی‌کنی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23716" target="_blank">📅 00:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23715">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PE6qWOfYPCCeQ2Gp5XQmYLTm1zEnGxsW9J6KBPtTYeseAs239NMjJfJuuP03FUH46_LrA514tN2ivoAFluuNJ1f9L9YIofm4TBzVFrzeB49FCQw4azf4169JFwfcsQs93p3QtBpST6FgGM6HtXE-y-AFm19USizh_ROFr1P69znresmj463d661sA-1WlAKhBOIFZg8pkfN9H8ErO3ybhdcRAu6j7vx2vXB4BPAJRMODj5YsfdOj3q5SqmfK6d5IQDAp523LtVpsr3WgOBfiquIwCEKJ5bkh9NZtw2PYOBpWRQEGKyBBopMaejs7vo2NsPu6ZZP0Yr_dA8NBKPGxrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی؛ شماتیک‌ترکیب دو تیم انگلیس - کرواسی برای دیدار فوق‌ العاده جذاب امشب؛ ساعت 23:30 ازشبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23715" target="_blank">📅 23:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23714">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vze17cTLghVm1a8ucp_Untt0Wqgzmo8PIDt4a0baP1kJzg6cuJ-L5cg9OFEZBEOd4YU3b86ubIm6H4y1q3osn2fI1WCXQK5zqJO5FnnA7HDOpe7aO6D0wS2U2Qm0h55M13u3TymFzOST_zVwMIzv6A8CakXctMN4-s_yKFr7bpKJcjoxuiNG5K2ACkUN7S8CeGmG-KizBXsobxBwG_WFmuY5ahVxbd3VczBdnDivsmsZpp5Tq8hvJUItHe3tSVPGNs73sRd3p650QP3yL2pPo3op0tZfZ8sAvmhY_Q7A6EYBo7x-ZV56ogDQak1_NB3PDtUHs5QKAPlh_DwGGxScrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
با‌اعلام‌باشگاه‌سپاهان‌اصفهان
؛ آرش رضاوند و میلاد ذکی پور قراردادشون رو با این باشگاه تمدید کردند اما محمد دانشگر حاضر نشد به باشگاه تخفیف بده و جدا شد. رقم قرارداد دانشگر برای فصل جدید 170 میلیارد تومان ناقابل بود که کم نکرد ازش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23714" target="_blank">📅 22:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23713">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79c30d0c69.mp4?token=cLUtNF8rHTEuq_ks3Wdi-XD3_Ty4zKWgtXDX5TScdVps7THHRQmwKgZzn8eloGBIo0PaWnqTzFcr78hL5yi9jL0JVwOTUXD4J8dfah8Dp9F4nfPSPyLFZBs5fn7zOb49vU8QbdWam-s8FmRdyv1YoWL7GJunaScU2j3fa8tpD2njIClQlCpbmOOzD7A9kpwNfM8XtbzDFtB981Ljei5-FOcHnecCt08b_nvkfXsmBCsxnHUp91IrIKcJtwcUhU9kh4drTiRVzR-swt1amxXJ6b8ZGJPUs3UjCj8Soc5MSjm-1HClbdEvIxcSTa2vv5VoNK5Te493CRnClu80mfxNEwZsU83gXn47AjIMLS82YZdQudbNWQ6xuNfOgB6PYTTRwOyCsJnsOqTBYtoDlpxItqaIKJQfyDaAsB7SkX_NhcvBVaFrnFcGPtsbQkZuc24Oz3FTW5jCsjWkGOE40OVdYt_f89IjgYJ_QOFmDSJlSoYiMfM6TwaVV1ym34dfJcdzygvrZ37AjN5rxuQRQs3CAIBIeHD4PMkwAVeoRpZREmA5D9RyE3Dk0YXuGgPPMzfdV-__znN18RbWiFrywKE9RbM0Hhi9t3dL6ouqpYLqSb_F2Ol2uuxGmHGV3H94noUm2R3XWbAVqmomSj7KDee_joz0XrmBYWgTv0uk5vKBImA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79c30d0c69.mp4?token=cLUtNF8rHTEuq_ks3Wdi-XD3_Ty4zKWgtXDX5TScdVps7THHRQmwKgZzn8eloGBIo0PaWnqTzFcr78hL5yi9jL0JVwOTUXD4J8dfah8Dp9F4nfPSPyLFZBs5fn7zOb49vU8QbdWam-s8FmRdyv1YoWL7GJunaScU2j3fa8tpD2njIClQlCpbmOOzD7A9kpwNfM8XtbzDFtB981Ljei5-FOcHnecCt08b_nvkfXsmBCsxnHUp91IrIKcJtwcUhU9kh4drTiRVzR-swt1amxXJ6b8ZGJPUs3UjCj8Soc5MSjm-1HClbdEvIxcSTa2vv5VoNK5Te493CRnClu80mfxNEwZsU83gXn47AjIMLS82YZdQudbNWQ6xuNfOgB6PYTTRwOyCsJnsOqTBYtoDlpxItqaIKJQfyDaAsB7SkX_NhcvBVaFrnFcGPtsbQkZuc24Oz3FTW5jCsjWkGOE40OVdYt_f89IjgYJ_QOFmDSJlSoYiMfM6TwaVV1ym34dfJcdzygvrZ37AjN5rxuQRQs3CAIBIeHD4PMkwAVeoRpZREmA5D9RyE3Dk0YXuGgPPMzfdV-__znN18RbWiFrywKE9RbM0Hhi9t3dL6ouqpYLqSb_F2Ol2uuxGmHGV3H94noUm2R3XWbAVqmomSj7KDee_joz0XrmBYWgTv0uk5vKBImA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی؛ توقف نا امید کننده یاران کریس رونالدو درگام‌نخست مقابل یاران گائل کاکوتا.
🇨🇩
کنگو
1️⃣
-
1️⃣
پرتغال
🇵🇹
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23713" target="_blank">📅 22:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23712">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qh9dNJtEkJCXTtQAG-QBXHG2xWzy6bagn9UMMb7amNKpYdi0wy2dwhL3qx9KFGmXRynrnyOBLHOAr8io6gm72WoshhUwOlD5fCrmLQtQPO_T-kcGDMvY739OHvbitMWkD77BarZVr7y903hxgEY-LLXedgkAZOskVpbuC3EcLtbCSxHKbSQr-vg_bKtUZyj8vnDrIccoCBaBgWMshbeBr6xErWCPU1DF4GZo0eJbLJMLE99NqWP1uUOfgxq_WSoIcWDUbAFR2eT22atfylVoujd6_7MpN3ZApCh624CmdWvxXLlwzyI52wBpz4v58nSZCForHoWZ8OKrqstZaLj87g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باگلزنی‌برابر پرتغال، یوان ویسا اولین گل تاریخ کنگو در جام جهانی را بثمر رساند. این نخستین بار از جام جهانی ۲۰۰۶ است‌که‌اولین‌گل تاریخ یک کشور در جام جهانی توسط بازیکنی از لیگ برتر به ثمر می‌رسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23712" target="_blank">📅 22:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23710">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TvCrj4JGiDfKlGIDorkQLjyd9lILCQXWTYJm9hExJFq7-pqoO3_rIiSOOu0mOcGkZ9Mo59fNfmx-croHcANh90_k9I6i4J_kcPjIZJMwFx5urTfWDnlCFhKaPC4NAZwz7xorfPVP_KnEGBqC-6h43rPlekKO-uGNkUOOdqoKctAggTr-QDOkL3ovy4JK-KR-upbvIuwZEt-7kI0jzO47WJCMWyEC55W0Swyom3SASieb_cd5v4Woj1cjS0Tf9hlHkefUGTYwOYqhPbO2eBm-ufBJr4bITuyplJOaVGFHdcr9Mto8n_v2BLS-LIYoBlF24i8jghnlg2UIZXPx4_gQWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/in_OkXANADX3y7Hi-wN2DDi8FUP8LuNHErmfHoY6X1RwcNXMbaTLlDK38B_Hwie9eMghJFcAFlLl8eUI-sLffibXf3AjhIJiNspnr_4YDlX_gd-BIF7KZmnwc56YHvWSXdEhHIapsO0gF7c4_98TedQEyRDNxo1V7IKV2ptqoqok9jXvg1b92Cj-mhl_jLrP79GZCLY9vLL7-tXK8WbaCp7TcEguH2nw6viBRa5fkBNK81kgmlslwz2c9PTFUfOTS1GuKnf6QiCVlF-ewaJSDmv83iQhryn0QFIO9Tai0UFyuw3Jn7ZegozxavUqz7XWHogEwoDXqU4oeKUghEg5lQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی
؛ شماتیک‌ترکیب دو تیم انگلیس - کرواسی برای دیدار فوق‌ العاده جذاب امشب؛ ساعت 23:30 ازشبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23710" target="_blank">📅 22:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23709">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXy9eccxwbSx2mbc5fDg10ytDb6IRqIVOImk2vb3MYzpcirLNU8DmuN6Hx0bYFTxbnTYNQ1VItrsprjLFp6BcTquZ7qgMT6CDuEpoYcXD_X7eLhAX3fEZVj6C1MRAvZlmgpY4luGGF5GuZPByj1oJYgQ1lV95QOwUkEXYG26lCc_i8XsON534cMTPnYBbLZW7tcSzZO7Xk6gyxFs1lGT-Y7XLIHCpH9uNF566n20oVQeAcU4378FH5TGgtG941viQlrpgx9XJMSL8UCegX9yrPOL3ZmVJOLQBNsLedHqRODF7CfsqocYv_wqHn0VvHDccPEd0BjLQWW4MbLigYX8yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
رگی لوشکیا هافبک‌آلبانیایی‌ساعتی قبل با صدور رضایت‌ نامه توسط باشگاه مبدأ به تراکتور پیوست. ارزش او در مارکت 400 هزار دلاره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23709" target="_blank">📅 22:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23708">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxswSYbuHd5PjiEpIdHW_E6jPHf02JKdz5Itvce-FxxBSFmioNy3CfO4EdW4QU842yF13lE44I86D13tti35hhVA-HiRdVzjln_3AGhxVJIXJEIE4Tvp8ZNF9C3ezz6GWJ4QoCCF4FydtNppYUEOox2O8rMLE5kEriiUWApEUPzMiUwIwG4GouL3W5rqh8n3Rrje4pZ2ZC3gYucVLBFcGQ8hq5T-ngVNs5hDIk7nLq_6zuVtgkfXdriZIEXgblvi1cnRXfQuc6AV_InQAOOXMoCSx0a3B6t9Op9bf-GpT7Bw9SoRsVSN_PmjW1Ka-bixDfsk8mEQ4YkhFfDXTvoxDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم ملی پرتغال
🆚
کنگو؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23708" target="_blank">📅 21:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23707">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqkWSVqI8OX3cRcRZUvR6VSNtG0IQ1f9QKTJIV7eWMS5mGyGPZWbDkcMoL5NuV-8-RkL0O14R-HW8zWdZSEvLh-1FlnfhK3ZObV_c76jsFFQUIih0-qWaz30aQZ6Ek49jyKATfGnHYxqW6b6ASkv-ufMuBS92RDwnHLuWHYrXL-bUihkYNUTtENRaODc0eOctnQ9cT88kXS65kEAX-RN5ZoBE869xI1Tmq9uhokYO2KzSp4KYp9A4VVB1rAsfdrFVeRFpecBUH4XRrE065aibb9IOrWCIL0UF9qcqTnYHxyZFUoyNbA0op8NshiffSWAheaTjDHvpswYtpV1zF7-Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ آرشیو وار: خطای لیونل مسی روی بازیکن الجزایر یک کارت قرمز واضح داشت اما داور تصمیم گرفت این‌صحنه رونادیده‌بگیرد. شانس با لئو یار بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23707" target="_blank">📅 21:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23706">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGi_Ztqx95cAL9u0Na8g1ggvbt3X6NzVJlGzt4IXZGtwVo671iJQOhttKIjVPdW2ZRVUZoCFGzg83JgIegRmSeBCZ4O8qTUGnyqS8KeDuPgusTPVWzur350Lj9hiFp0Kz1C8mURK2y_gjrPAbDWx55Jbf7y9w0pN9MRcrKQz1SJjaKCmloXF-VImZCnGNyDvfbLk688W2MP9pKJ7rbNk4HGA7GmhEGKa6x6gcE79_dGirMQQWIH0MqwwlQixS2GkXtG6WRfrOM_NEaRrirTJU-zRU0kSOs9v89go0Tk9RvXN8RfWyno3XHidwx83R9iadlBjHO6ujSbzYnPVq47S9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌مذاکراتی‌با اسکوچیج انجام داده تا درصورتیکه بنا به‌هر دلیلی با اوسمار ویرا قطع همکاری‌کردندسریعا با اسکوچیچ قرار داد امضا کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23706" target="_blank">📅 21:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23705">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2F5fJdQlZqTFzdIz69YUU7baJpzk43oITQEkjco-s3BZtfZKzuZbansxqRVYr_o25JvgbB21Bh86Gm4Vr-vVr9sN-oXTd4n0qY0dW4eVolzmZfPS4uPzYrRmgyh9PMcx5XMTKMCo8F7GPZMkdSk5f1rAaUGapjjqkrWtrROkbZuUXc3vtMNXwjPPQY49ZiR7VZ3K4veeG-JGUbFyOAirSm5eMEw5iObqTrsfJiwEfKY6OFNKuoRwQgZ61wOOI5vdFbte0aHm16jm9Q-evNPASTl8DCHM4gv-0NfpFgdVx6lIrzb1l6Jp1kF_0yzJBqFr0-qVyCdL7LR7jNHyqNYIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرنگارESPNاز پارتنر ژائو نوس پرسیده رویای چی درسرداری؟ گفته‌کلا دوتا رویا دارم یکی قهرمانی نوس با پرتغال در جام جهانی فعلی و دومی پیوستن نوس به باشگاه رئال مادرید در این تابستونه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23705" target="_blank">📅 21:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23704">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmQ-2_uok3bYFFwnPfvnLj4CJtd2tvi7pevuFttJ12at2pFIVCOFG8wWEZ7NglRJmuPGEsVQ6dfmrqNP0SrRUXGo4Fm7-LIEQ777Q5HundGXv-aswz9HdUTGUvL5CocNCKfjF_k8omM-6RFOSSIjMG0SzDtDFIoy_RGHCRgf4lGBzRpONn806s_ThI3PVM6LT9GTV4pYEA3TzxJwdzFL68yCoOzN2H9bhEBUUsG8PLlNYUDkFvBemtSkewj4JOuSg7nKkmAxA0xEz4LU3atB29suvdwAT_vPCJao2azCYUreWR4YViQAQYFkMgssZbYToXpyRZxz4gvAbAUdVS5yrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نشریه مارکا: باشگاه رئال مادرید بزودی برای جذب انرو فرناندز به باشگاه چلسی آفر میفرسته. مورینیو برای پست هافبک اولویت اصلی‌ اش رو گذاشته برای ستاره آرژانتینی چلسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23704" target="_blank">📅 20:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23703">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9rwdsSuxRgNR3z1mqOYx3NeyYBijm9L7DLbWQjhzyGcK2yH_PTzctIWfKiBPp1NHM6q8_zi8GoNnhtq60aKihcbtBNj9WTnzy_QYF5Mht6Zj1cbJxSuYmHoC_zU2Z2tMPdN1nNK1aAmeBfKsC3hQ6758SmAcLJVzd-fGUggz6j2juTPe-7VZrRFlJzgJ7zZo7Z4q5RO0jCl3laOS1dVArd4IfPbW9h0shspvT8eF7PYDagSxziGHzgB0u0jlmlRBV0BJ5vFrHofKXG50Ep1PPkMgKr5gahWKql1qRXWtVJOB5mwoE0FSkvygjtwj9-gfxYFa7AKC7okqTOYKAKnWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛کریس‌رونالدو فقط 1 گل تاتبدیل شدن به بهترین‌گلزن پرتغال درتاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23703" target="_blank">📅 20:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23702">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2HWm8srXkTaLLPIX1UE79ulpGefVRmfZUB2bGir4mico7VnHVLhvYhFoGMN5h1k1AigNqrcjayDSrFa1MbBA39Uy2J5TYCT1ZawamNmb4YZfzWqD2GpztVXrFDxFG9xNKv1pbsqgMhk3SNcVzAOlCuw3CwaU47D1_amitRF3m4Y8XjcVNe8ff1pTDNhwsw6QbpaOGIbCg5eZLG8OoEH2LciQzBOcfMaDYgI0bGKBTzz9v2YyO_6gJW6TNJ-Q96XyNsRMNP7cCwWwSQd6Eznu-5HHbSN8SenvzQpw4ix9ivd0IinFyCMJKsWwugv1-8kZUFy8V6q8pc6vg5nMQeAnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23702" target="_blank">📅 20:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23701">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRDH-sjGpaDldJqcRDacX99ajukQ7OkOSOXnyqzlLIuud9I50ykO4rRsP-AfkG9R9_9tr2EuM4as2DzzbWz92DGkEx7mpSJoo45UrHaKzpiH2eY1yGl7ZB0hZUQn3yp-z5qKP-l0hR8l2FfnhcuSF42eAz6jifeFXj51GbRrxsD1Ub36GIw6sJLTDEwVtYnxyPHMZ_5cJx0yWp5RsZckgdjJe53iQkMhRa44Rjg7SE0Dg-Yp6e0Wy2UoD5e3QrFxbcw4Cp94fxdYT1ZuTqjnRinG9WXeIem-sqMW-sqhGA2zH7YSS63wID3Rx1idUvu8a5A3_3Lyhii4kliYjc5CeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23701" target="_blank">📅 19:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23700">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCsOMTb14r0IucWXae0Dccv1yCpQKocB6zkhF1qlQbKUA1XKBVafp0SAg0NLYAnPZorszoaJPTh9YFkkUlVQAyQgcu59lhlHR2gZ28D-su3941ayCVSotIuTeMYrwcOFnTifyrQIwEX4heD_MnUQ3o-k3CH0UI3dCGlbhiv4VZ4ciVK2jiUKt4SFnIgnvennYuR9O_vNncM8wltkHNlh-VQQeW3Ozx-EQlsnfTy5DFVqB5O6xE9so4aNGTt6Glvw4-SQo3DG3oHWmC4_Kri9lQrBlyIMjEq26026dYPC1gVN6FvQmkbYmVqlSphY6JeJIC_CWomDmSQIeTB-j061Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23700" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23699">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXc8zCkeW2I9_QtXs1L2u5tOvml530qFwZ8SySmTwdAin6yc4IPNRVjT9EiTa4CXv27srx_DO6k49VqI0uGjodJR22Op7R7RQDEJe2Xp5A4uiSnYKyNnizt1aKRHUmIvY1gilEVSnUSDxLdsojdMlRqDQX-xf9Pfm7cEL8_U1bB0qMqFiWN6gOEBJY9oPabFCgJejI4xYhX49EGPX-X2GtySikQnJo6h3WiHHF_pQx9peAdB75ZL4PHjWNQ7WMIMmxYU_3EPQyiSO9-d0W6W7mCeWHS2IaCD0LEtGmzLBcQ4bSElkyYQH1gXhOvCxl83Jxj_2IJSjr026DwvGeZFqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23699" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23697">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OoEXlrguKH9r3i0TQaK-t0KVRZEMo2iOzkn3_hY4thFDWf3Fr9mx5dCr8X2n2X-GarxEqKaiLXX1HUe-evLCx5XelXFzkI0aoWdN1GRmxY4TVzrmObZINNAQTo0dXlyGZDonz2TctfEXc4uB9ZFAowRVjFBogrGLGmYY_a2-acx4r1DADNzOYmG5T_K0AyPgmYLIGHEMhF4EgeR-nlhk__amdFV3Vq_QtZaZ_nL4ve4iHvl2ENgFNXfpLL2X6IHXAStV8rAdHcDrjJZbsbE2PLjbW8E_MFpqW5U448WAVzlu5Yaniw-Iw_nhFitRPbavedgFp7DzCJlIV7TJg23MCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vuJ4Co5AB3IT8J3P_8dMSBEQR81reYWzMR8bDXLbMu_64wBLmuUS1oLkNwt1mat5h3RC1F3_eXISjOCsbLEldSRR8oVuSxf7jt-rKjTFQB1KZZoFTOm5lrrSyzTLHC283GuF_7HbE_VqOHADDjh7agCKpH_IQ2EXVNKqUAio-5fFERTUevtbeOSs_tzhk_u4qvl2typkuVJEPAQYY4QCZnA0btntU2z10fxUOOQW7NKJ1N8yEktPkRVBiR9-fWKFSGbdwSNjzMqRJDBshfEUcPXXJ5ulsG8QjccFUntCCHHoSyP_v2FCgVLsrfL_WGNp80IWYnh-rUU04XrC_8qzbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی 2026
؛ شماتیک ترکیب دو تیم ملی پرتغال
🆚
کنگو؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23697" target="_blank">📅 19:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23696">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYMCddi0K732M8vmGYhlFjQ4HaxG3AOyLfNwZ84cvcUTJvY6vAOVzAvkyOtp5LnM3F2s97yWCnaGFaHSlhC-41Tl8ORn_OmKwCWDmTAkwtVjUDmX6W9jc4GuJvVqoWxlWRxLn4X3AP2uloM2vMX4bTeK2M1eV5nxjYX06zHDGlMfIN0fPq1hnji5VA5erAADz4m8RBx61hSQhzkNP7Kp0kBAvFIc1P0NSJbz_vsabbvVUK8mKKiIcsfy6ds3axFNDLwbmEwHrKf71zGnWLMJl8si22AyCQeOguldcxBF_DhmuvKeWPdOg4lTJyLhjWrDdlLxWtZQ_Xv-Nv54V4Bobw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو سرمربی رئال مادرید از فلورنتینو پرز خواسته از بین ماتئوس فرناندز و انزو فرناندز دوستاره‌پرتغال و آرژانتین یکی‌رو جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23696" target="_blank">📅 18:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23695">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzWA2Lee3wzNdUih8q6AcQKtQUxTxCB22QqAEbxZdbetRgRsHgAaG75k3hT1EsXPLIxCZqPZOcod0b-3tvh-Ba2eMO00-8GIQcK1PdPXJDYEivhfhuajDaIUYwJDkboBWOARNk9KgszAZouZkXh5R4AH7xeK6gjBxRNqhY7Ezg1dt_rgrSMveodufcGPJ8AVwHm9DoO4HslsRh39E3R6Su8mWinROuwKcAD73uIoHvCGeWxcQi-BDqlQp8xqjbvGFe56IVkbZXUoAQMXOJF0g3yhIS3pIVQ70EOAd-IYk7Cz85OoZyfkx2AwaITXFcwhyPk8M8dWH885MaOSH6QtyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ پیروزی پرگل آرژانتین و نروز مقابل رقبای خود بادرخشش‌خیره‌کننده لئو مسی و ارلینگ هالند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23695" target="_blank">📅 18:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23694">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNfYiUkapHGj6pnuHiMj_3vYPHOD2ApHqVF3BLhosj3UIM7oPS3TsJhGJatcUnHrD66M1Xe3YCNc-NTn1VXGe5cMO14p_elyrFSxy4OM8WBia8uuFAuTzLAqtbT9imgaU00nqA_46wIdViReilq3wDCKE7XAm08Qo7HRCrQYSUp16oG3ekB8YBL8T7_MjVTMygyTUC0BXxyTk9jNBXSc3MOnf-Em5c5h2BnWKJdd3MtOXUKq6DRlyn9R6XX2snCklz5qOPKIVW8_-unnmyfgOd-7rdBwlvhQtO5mNSwV6AKLGqwrNj70vK5U-5SBZSLolNUXUTw_0S6SW7mWIC2X9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
با اعلام ژابی الونسو؛ دنی سبایوس در رئال موندنی‌شد و او این‌پنجره‌کهکشانی‌هارو ترک نخواهد کرد. همچنین رودریگو پس‌از کش‌وقوس‌های فراوان به این نتیجه رسید که در باشگاه رئال مادرید بموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23694" target="_blank">📅 18:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23693">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0-W52WEctk_C0lM0u1f3tV0g69M8eFgPewzxAMqn4Je29DOfjMPv6iMRjItoFuxidZoygWMBD-719oM_TA78pk3TrW04dTVREs7Es2fcmJPHtKmj_Ps4zB--7UQgE2N-QWJKbZnQDft7sk0kHuMf-2lAqV7nTdXDYV5gOg7qe7vY2Nk19VjVPcVif3qKudyKdJWdG9mwhS_iuF5xriBe1q51VwbUKTiXZ6OOHA-BDEwyfU3QpGicWAoQqEpa-Mi6bb6ylZz5qMuJmyZv8rX0bVNSIBk41NzUTRT26LsYF3EZFXxp8FQfMRRyzVOgIVKmWxDK0ANGNODQc7civ5NmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام باشگاه خیبر خرم آباد؛ سید مهدی رحمتی سرمربی موفق‌فصل‌گذشته این‌باشگاه رسما از جمع لر تباران خرم آباد جدا شد. به احتمال فراوان فراز کمالوند سرمربی این تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23693" target="_blank">📅 18:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23692">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b816759b6.mp4?token=u9mWJa-8p2xkmJyuGzPb3Jx5lK8oW8_hFSe4lC5KOz10N_N01NlQKmZB06wBpNUibPb6k28VekQRzNYxtI_p8ygfrwJNgcuNANfmwqMuBGQbnAq9oCvs3wtEdzBdP-vJuM_GEaRav8qbU0CO-w_eXXGlfHyz_mAIO2nnfMwS2S2t08p4fcRHrSXCGRrzhguhnXWIMK2112YxE7xZaBRBjyCKdSi3bEDECyr9FjOiLYuLyChN6HCaI7RNJ842IramQT-u1dBIWmxWcZGnHXelYDxfh64VkFvIqoyVoO_RFLcUlcQI_W3e4pV66LQqcLjbYop4SneMDHzMFDUGxYPzGArFhy2ncDifOtkpgp2lzNm8L9e1yBnkff56i0orBNtTDEqDU4uGfw5Mcf5ZZsJ0GS9kYsI0exchNhB4CKV5yf5jGQttWl78bAKGwXlyJDhjEFKuTxQJAaNufHad1s_YzH8riZN8I1CNHFQ39WfjeRhmkjP3OFkLBnKw3tvCEwRZQxb2Wy0ofQzZ8ibCUzRb0UtA9eh4BdJPeazmhZb0YbMMp6vVgEQN01mWykKYQ_JgHelHwf6pbe4cCydH0t7ktv3pM5BFrp8dY1hOqMeJi1VhiSekaIWxLFqP8JRWte4E_Timlh3UG0U1lchce2sqS-u3VM_gLvauuD_H3XB8i44" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b816759b6.mp4?token=u9mWJa-8p2xkmJyuGzPb3Jx5lK8oW8_hFSe4lC5KOz10N_N01NlQKmZB06wBpNUibPb6k28VekQRzNYxtI_p8ygfrwJNgcuNANfmwqMuBGQbnAq9oCvs3wtEdzBdP-vJuM_GEaRav8qbU0CO-w_eXXGlfHyz_mAIO2nnfMwS2S2t08p4fcRHrSXCGRrzhguhnXWIMK2112YxE7xZaBRBjyCKdSi3bEDECyr9FjOiLYuLyChN6HCaI7RNJ842IramQT-u1dBIWmxWcZGnHXelYDxfh64VkFvIqoyVoO_RFLcUlcQI_W3e4pV66LQqcLjbYop4SneMDHzMFDUGxYPzGArFhy2ncDifOtkpgp2lzNm8L9e1yBnkff56i0orBNtTDEqDU4uGfw5Mcf5ZZsJ0GS9kYsI0exchNhB4CKV5yf5jGQttWl78bAKGwXlyJDhjEFKuTxQJAaNufHad1s_YzH8riZN8I1CNHFQ39WfjeRhmkjP3OFkLBnKw3tvCEwRZQxb2Wy0ofQzZ8ibCUzRb0UtA9eh4BdJPeazmhZb0YbMMp6vVgEQN01mWykKYQ_JgHelHwf6pbe4cCydH0t7ktv3pM5BFrp8dY1hOqMeJi1VhiSekaIWxLFqP8JRWte4E_Timlh3UG0U1lchce2sqS-u3VM_gLvauuD_H3XB8i44" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌سنگین‌پیروزقربانی به کادر فنی ایران:
من‌ نیوزیلند رو راحت با فجر سپاسی می‌بردم. نیوزیلند اگه درلیگ 16 تیمی ما بود جزو چهارتای آخر میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23692" target="_blank">📅 17:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23690">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pP-XvlNNmLQrbHnoLdoo-LXAJd4uPNw_ZP6c1HIHCt8xP5YwxpszCJKrQhSkoeLjauDoytoaAI8NKq3RUHpgdohPZLhv5YMISLsq3ie5qdq2Q6n9LZH1Hwa76OW98lb787TMfgm352P9DhMRL9he-EQEEe9AIy7rHNKwpdyWmQCocsOtSh3LM3j-XusAHuZ3VJQQZDCJBbGYSIirtQ_1MTCsJwEeNjtUT60uGZ1BHzPbZz36xDMXWKngUXq4IjDySLC4UTMuU2YYMQI0lsRAogkHDudWQd41QVq5YdiTH_TLywGMmhjlnxYbbVCRIRORRqS76cNAqKQ3wnnwjH8N0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qMrkp1i1gBYQ81v4t4zgay2CLRHRK7XDDtN5KgBH_TcB5r7GGBSi961fBwM0Abgmj9oM3KIhGzgW3JufiGzZOeR74o9RrzrOO6LXjEp1fy2llRdItt0vSSvEmfTrJrJCB6z08mMcWG81g6iuXZlxZ9t0UkLQ_x90Z6p9xrbo1ZvRNHI8PiKnD8_XBGeFhgEadyfJ70R1CIzcpqotoqJV_7FXVJKYPB7_dpRwCaadng6VChnrwFRQutfIew6Q00vCbRzPFMMp_TKpfURX8ZpRjzPBEsPvPdm3_XuzppH7bTFM2aM91M_eObE8Qj8Y3-ZP59NnQB2GF6Hgs6zvRhkb3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
#فکت؛کریس‌رونالدو فقط 1 گل تاتبدیل شدن به بهترین‌گلزن پرتغال درتاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23690" target="_blank">📅 17:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23687">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2Qg_pYo3G8kuw3o7BmVHfzKTWZcL_VfSntiIm969OOml3H3CwGS9qyizPpPJDifiPt4sAQGF2G9MAP88WPhdt3g-cbpCLa5NuI_FH0ZzOYkWgKeXi2du8m9jQOjGJxYbEweHs6u_CWcn5p4bT4IKcI97sMZI70pnEIxNtK9n5xMptfzQyP4D1uTJ0qAkwdun91rnRirPQZmh2rN-yXgYCfONtss4WnaR_DKt2FOTt1HZEOiJIjrXyqntYlmttHeTGUvyWK693e4Ne4Gg96nnXfjnPgUOlgOP45LQC2L6XFD9u4Ag3vZSdAft7OV8Etxe2_jzxW3apOuhYavspx00A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23687" target="_blank">📅 17:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23686">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/012fc50185.mp4?token=ic8sCo5U2O9RHgWMktVXuXHm7Dzjcl9gSVmIjkmKgmkU9FwZkVM72RkzhEfv8oIE1WZCtxg2T5VfJ31YohW8mKTVhHOSjbQ_1MNM3UA_SDyw59SmE2QfJEz_xoH5NKk3T90WD1U1AELXbSs0XxYzXyOImOoqFezf9Jh6W3a81_xCZBIAiJK2hhiOC3fBuh_EHMb7Na8MGJKCFJS9E_7CRxDLKdUqhCG1EvKWUtodA4krfH1Ft9sKp_N4ENUJRQtQc_Tf3hthWYjx-vhdl8tzdm3494KGGCTRpZSogpgR4qdveAuHTOSbcSB3W6AWZO9g6_1wPBxvw33xtsDbUH86Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/012fc50185.mp4?token=ic8sCo5U2O9RHgWMktVXuXHm7Dzjcl9gSVmIjkmKgmkU9FwZkVM72RkzhEfv8oIE1WZCtxg2T5VfJ31YohW8mKTVhHOSjbQ_1MNM3UA_SDyw59SmE2QfJEz_xoH5NKk3T90WD1U1AELXbSs0XxYzXyOImOoqFezf9Jh6W3a81_xCZBIAiJK2hhiOC3fBuh_EHMb7Na8MGJKCFJS9E_7CRxDLKdUqhCG1EvKWUtodA4krfH1Ft9sKp_N4ENUJRQtQc_Tf3hthWYjx-vhdl8tzdm3494KGGCTRpZSogpgR4qdveAuHTOSbcSB3W6AWZO9g6_1wPBxvw33xtsDbUH86Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خداداد عزیزی سرپرست‌جدید تیم پرسپولیس:
من اینجا روزی چندین‌بار از حرف های جواد خیابانی هنگ میکنم. بعضا وقتا اصلا نمیفهمم چی میگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23686" target="_blank">📅 16:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23685">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xn_HWFyiQqAUqzKxcR2F6yCGijBrAxH8jHmKdJUCxrbHMIJI44dL2OEvWkbN9hkywhpmrCVZNZrVRfEqpZmmXVJG4a3twvuLmjKdxR2PvYfWcZe3gbMgANty0IM2OXXhwF3AqkIsBfHlsoVY-7h7EuysD9YMgD8Gupl43ELaCvIDVS2qMOhdb47en0dDBvDY23kHeh9RFo7n-apptwC5SupCDSoNltQfbEnr23_Hj60IC2XNqDGOZQRKLjp4Nm_QWVxJnpdONsJhFyJUJdmDt_wTdCKn4YKY5pXBo-iDFj8Co-7fpMv0aKF-5MNgTeqlkkp2TOlzO20r-gNq9MdUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23685" target="_blank">📅 16:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23684">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a3b4e42ac.mp4?token=ZzUry1JwzHFjMo8arP2HSuknfApdMPgoC510-5dHpxw3m2GRaARj5TGYr-0Xhc-YY7uH9ZHZ7wcoScGG6vM-QLecbgiWUJZTT8gwYIsCRnV_ko2pon50A7GNFlp-EuLBm0WekkYpAdDPfWsj8H10ThAR-D-8_Y59JQceAbFH348m54EX7ejr-SmVZVrdrO8aA2aEj-IUE6Ldch_CWZrtH577kjYoBLNEi-LoZlyCbacfzh1jMHEGsHdjEDK1Nm7ds7PFcCyGsMnHjtoGOyxGaLrhh47u8Wp3MiNCqrEyd8HGwbK3uIFXrlWzM1jD32cWETzJPsAF5WphEq9P9afSZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a3b4e42ac.mp4?token=ZzUry1JwzHFjMo8arP2HSuknfApdMPgoC510-5dHpxw3m2GRaARj5TGYr-0Xhc-YY7uH9ZHZ7wcoScGG6vM-QLecbgiWUJZTT8gwYIsCRnV_ko2pon50A7GNFlp-EuLBm0WekkYpAdDPfWsj8H10ThAR-D-8_Y59JQceAbFH348m54EX7ejr-SmVZVrdrO8aA2aEj-IUE6Ldch_CWZrtH577kjYoBLNEi-LoZlyCbacfzh1jMHEGsHdjEDK1Nm7ds7PFcCyGsMnHjtoGOyxGaLrhh47u8Wp3MiNCqrEyd8HGwbK3uIFXrlWzM1jD32cWETzJPsAF5WphEq9P9afSZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇶
#تکمیلی؛ آیمن حسین مهاجم تیم ملی عراق پس از ورود به‌آمریکا توسط‌پلیس دستگیر شد و بعدِ حدود هشت ساعت بازجویی آزاد شد. اتهاماتی مانند همکاری با حشدالشعبی باعث دستگیری او شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23684" target="_blank">📅 16:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23683">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34750719a.mp4?token=UbY1AyHEf9Y0amMhLtBLdXXbMWDIeJVPCeB3xM6UX6bvRoZazyyt36IAhDKWC2rgPTOyFueje2ZlwAOHiSbxKGE2Fk5vVQ0R4jA33fFJSGKEy-Li3UR19VPxcrkFU46R5a4l_rLLyyDI2oS0z90Hm8W6ug0FokCAJFzOO8DXtA8MHcjo4iKb0AcS0prCbJK0ThivfX6duACtniPuMQlIsRzeCyRBC8W5zhWhklLEOohCv4BBBxsXIjy4LauKXRYhoSxUFUF-s68v2nmjDDCkoOTLNpBUJmbwia6fr90wCrh0SdgT-D0xmxIlwn0KZAG5B7fLUpLPiNB4XNQZA3k7xz0NHvdovsZ-C7aa49R73VIOuHfLuliWgMdMDm_VtYdUzeqw80vsVnd6W5IGzoRH7y2GKKMY5gggALGf4VIJlCHNfiCTyASFrbqwdoBGahjw2oj546ufnWXmM7_yQ0MG84n-C0Ukz_NStf3bJ71M4FTI23kPsXLKrE7HX2nYoOy1n0Qraw1xwQwCZCtVZL7p9szgAi_ivt1AG0avVZE9By8IPHBNw_qhZbvvIalfUKoFLMB7HXuSMuuiOvLBM3dpz6onp-H57yC6zwlYVGd-wJdB8ERABr4WjQkntYbWyYtTXuO4xsv-_B2GgVyl-DO2ABcQwluVpcMIcN2PB9S42aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34750719a.mp4?token=UbY1AyHEf9Y0amMhLtBLdXXbMWDIeJVPCeB3xM6UX6bvRoZazyyt36IAhDKWC2rgPTOyFueje2ZlwAOHiSbxKGE2Fk5vVQ0R4jA33fFJSGKEy-Li3UR19VPxcrkFU46R5a4l_rLLyyDI2oS0z90Hm8W6ug0FokCAJFzOO8DXtA8MHcjo4iKb0AcS0prCbJK0ThivfX6duACtniPuMQlIsRzeCyRBC8W5zhWhklLEOohCv4BBBxsXIjy4LauKXRYhoSxUFUF-s68v2nmjDDCkoOTLNpBUJmbwia6fr90wCrh0SdgT-D0xmxIlwn0KZAG5B7fLUpLPiNB4XNQZA3k7xz0NHvdovsZ-C7aa49R73VIOuHfLuliWgMdMDm_VtYdUzeqw80vsVnd6W5IGzoRH7y2GKKMY5gggALGf4VIJlCHNfiCTyASFrbqwdoBGahjw2oj546ufnWXmM7_yQ0MG84n-C0Ukz_NStf3bJ71M4FTI23kPsXLKrE7HX2nYoOy1n0Qraw1xwQwCZCtVZL7p9szgAi_ivt1AG0avVZE9By8IPHBNw_qhZbvvIalfUKoFLMB7HXuSMuuiOvLBM3dpz6onp-H57yC6zwlYVGd-wJdB8ERABr4WjQkntYbWyYtTXuO4xsv-_B2GgVyl-DO2ABcQwluVpcMIcN2PB9S42aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
👤
ویدیویی زیبا از شاهکار فوق العاده علیرضا فغانی دربازی‌ شب‌گذشته فرانسه مقابل سنگالی‌ها؛ همین‌عملکرد درخشانش‌دربازی دیشب که دو تصمیم فوق العاده گرفته ممکنه باعث بشه که از همین حالا بعنوان داور فینال جام جهانی انتخاب شده باشه.
‼️
دو تصمیم مهم فغانی این بود:
که اول نظرش رو تغییرنداد و پنالتی‌نگرفت. دوم اینکه آوانتاژ داد و باعث شد کیلیان امباپه اون سوپرگل دیدنی رو بزنه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23683" target="_blank">📅 15:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23682">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167bd8b41e.mp4?token=gRhd6ZrK9abPtszOHsnWfoZ8KxV9H-_Oj7U5GuA_3fAlVC-jQqgOSJnWG9RlEcET1GyuGKzy68T8u0HSA2MDwc6fpXEJV8nmUlS2B88NYgI-C-4lWJkZJSy3SoMbKV9riVL8exk2HmYWeFo9OzaLdYSuhfnWQKXVRyX99bAlsn0JwBMdl1p0AI836lMGCHJuIACCS4nsNkmxuAeyzbadnfaonv4ecaVP-Gm1Fixb_DanHqHcXmeCD2e2FWEp5qGKn3gYlSHfdcuj3RxdQNF-WvMHj8plLHEgtQepT4NzwXNFF-OERabsF7moCs5Ux8syhtgJC6Bm0wuPKewGtu5nxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167bd8b41e.mp4?token=gRhd6ZrK9abPtszOHsnWfoZ8KxV9H-_Oj7U5GuA_3fAlVC-jQqgOSJnWG9RlEcET1GyuGKzy68T8u0HSA2MDwc6fpXEJV8nmUlS2B88NYgI-C-4lWJkZJSy3SoMbKV9riVL8exk2HmYWeFo9OzaLdYSuhfnWQKXVRyX99bAlsn0JwBMdl1p0AI836lMGCHJuIACCS4nsNkmxuAeyzbadnfaonv4ecaVP-Gm1Fixb_DanHqHcXmeCD2e2FWEp5qGKn3gYlSHfdcuj3RxdQNF-WvMHj8plLHEgtQepT4NzwXNFF-OERabsF7moCs5Ux8syhtgJC6Bm0wuPKewGtu5nxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🇧🇷
#فکت
؛ تعدادگل‌‌های دو شخص حاضر در این تصویر درتاریخ رقابت‌های جام جهانی رسما برابر شد و حتی ممکنه سمت‌چپیه از سمت راستیه جلو بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23682" target="_blank">📅 15:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23681">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuofAvvrt2JtVBVG65YsbnQRl30PktoSSFhM4r87zxCZs756-v6RApoBypHMX2yaAEgNnTTJg0ZyADcsvBAPOsgPRGGtIKtFWlK1SmLIXPhU4vHLnK8iu0gNecs4uyj6iHd8119O1lO9wT-mx6T7HRnjq9B2pja895qrLFkJ4IUyrRJUDmDMa7K2PMi8iidGEmeau0xi6hScHVJLy9YGMPyQCW89OZGmxljaDo9lFnEliKp_Jd0ZI9p8kBJ2ADcKIXQZpQGXodUupXX3Jp7HcHDoYwO6_4xTjvNLNsPmwDdydoq0a0Sn40YTv1bPFFsrl5iP0uAKSXWW7bvwNYh-Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تمام 120 گل لئو مسی باپیراهن‌آرزانتین در بازی‌ های ملی مقابل تیم‌های ملی چه کشورهایی بوده؟
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23681" target="_blank">📅 15:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23680">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qczM5MboqGivGJWxp4WAn6rTll7w-ioV3bF_c4op9thTBdVVDVcXBk5ThkpI3nfawLwL8HNinWvpq5qsP1ZtN7I33La9YEFI-WtnyaL12ueQvv3uOK5DZrcKe_QCDvQVFGTv62meRXEVp7-7GfMlwyMA4cO145KTNsdwMh_RgfWPQi6cHmf1tcqFWrvpMI_3JuOfZQJ9f3QfJ1jsr32Bbv6aOYHWXe73K6hLSeGk2T0G_F5PK418DHIGfImeLYRHoP8wt1fY4ZGS3VPwVAgQWkT64SuwoOUCvLfeQLxCLIpUjBNwQ-isM3SBM5x730himNO9_Tpkw3YnWrSQvC0bRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گابریل پین قرارداد یک‌سالش با سپاهان به پایان رسید و رسما مربی آزاد شد. مدیریت استقلال او رو به سهراب‌بختیاری‌زاده‌پیشنهاد داده‌اند تا درصورتیکه سرمربی آبی‌هاپاسخ مثبت بدهد با او قرارداد ببندند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23680" target="_blank">📅 15:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23679">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTkmz23iCqa2CK2iuu9OaEuKLw6MwlhB29w0dN0SPImAqVyVe-9F4DRJyZaFhNLTJEZ8jQzvyrtxtgbPGUi_Dazv1L7A46GbMjL095GFQaYjYZ2No0Bn585nxEgGZhBMlBw4nzgzVdavHkQmC-evQ3EyKIJBHKESIGklG-tx2dP4q0-Z6Gw-FIGjgJ9lt1PiJQw8YQ7FACxjOa3O1gUsKAx8pHJ_Gm5VaW3kIsYYY5skJEpA6m_gKRlSBim0ac08spmZoJq2S0lJe0a26jltOoPMY2JPTM5BdN8GWL1RL3gkDGYTzDeJkMinkLat1gJIwyUXxLSU1zXdIt5NhMueMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خوشحالی بعد از گل بردلی بارکولا ستاره جوان تیم‌ملی فرانسه به سبک محمد محبی ستاره ایران.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23679" target="_blank">📅 14:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23678">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NATuUjRnPqp_IoP0-bYtcQEXoDvktZ-tJiCBLE-wtTboKUDfePx1QMrhE0e7K5NMF9w9zHKjOynMM1X293rP0y0TrSFZV9LmZWnkqAlJNb8-SeX4nGyj3GswNiOe8CADDLRKM9Kf19_KaNKfajwySFilPAlg1YxawhdCJ6QxImRMrDYQUJ4TdjDGBua_gEanmdOeO0FArZtCerXc5ArJMgrrdOtAFvI5_LR1hrCmg6yuiGgURFigBqxGM_9lo0-7KYFIAmhXZaGzsTWjBYOpN-toeT9ayztfRaBdnMiPmn-slhxgcH1A_eH8cmTX4xchpHl5U1uUr79ogyK8pud5FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#تکمیلی؛ عملکرد کلی لیونل مسی با پیراهن تیم ملی آرژانتین در تمام مسابقات + عملکرد لئو مسی در تاریخ ادوار رقابت‌های جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23678" target="_blank">📅 14:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23677">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbf1AjcF3Hlndf3UoXokj8ImlmFTUBho-F-amBbtC0iLZUc5TVyCKtkhpCvH88LvKFFffxCJnp5hyOq2FEpH8SpNWr2YxieGkXCdxb8rdWlQjAqxZV5PLIy4kuX9DLRClrlbUDb2O92beaLiDbPbSR70UgnZUd_22JdE4CgV_Nhgh2HJpswURPjHaNRP7bTFKxp_8KE7pQqyhfbH2rv9lgvC9-EeNNAhidyCt72LfeiNrGPCpF056wZneDlt7eR0kpyTKVm7CIAaXGjR6R8SDr06RlwyXKOo9EdNA-xmczg_QCpZlAlruYCg1e_H-WKvnQWp7old3libV74joPpT4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌هفته‌دوم‌رقابت‌های‌جام‌جهانی 2026؛ دیدارهای این هفته روز پنجشنبه استارت میخوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23677" target="_blank">📅 14:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23676">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUj9VerMSflTK_kd3xKeFzqDmdHknEyptNSdLZIiNGDN5KC6PVCyQGRGsZH3Bq_CE6u95TYc-XgEhq2PsTqZaXbH7EhMlon81QNOSkcnouoo--qmHY8LhpQV76eHDn_bXAjF-nSn2aiUqV9_H2Ujz3ooXHtUa5m29amtP3Z_LGQ5jDsGnUSN_FFJ_PIBtF6glXTRU0bw1oV6jpuIiI1I8BwGDP_dTFoZ5MjRcndETuQLaL-7WPbbreRY_nm1hR8ooHbBGSkWFH79ri7AlbBtgJ6qOnHpo5_Dw9Lp4S_yH-496LjMsOQHCZbKoVuIsWQ4dyniKuBW_-P66MLXKvJDzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرنگارESPNاز پارتنر ژائو نوس پرسیده رویای چی درسرداری؟ گفته‌کلا دوتا رویا دارم یکی قهرمانی نوس با پرتغال در جام جهانی فعلی و دومی پیوستن نوس به باشگاه رئال مادرید در این تابستونه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23676" target="_blank">📅 13:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23675">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa85532cfb.mp4?token=vQ1dND4RFrwz9WLpdDNmExaafTBEO4jdQVVkol-QkfZlMFHuQ_XOSg9rFNkhBZmTG_mBaSTft7BWKfphx5Eb_ROZDQymWiMhr97AsnOP4pxH-nCAlJFg6g6VL1AM0GiGIkIcgiIUyi9PPV5qMIt4R5FWbH6TXMbYcTk8ATDm1Q-g5hnBrWaT2DzaV-uBkO_EBa8ROzAQzOhDmIc0US-jRFJVlcwwSSkx2mug67ZC3aq-R3IKvQUH1YL7ET1ff5UoydmP7lXN4pp5iHwNcHq5NUpybTDI4t1dKdU6QHPewacAWIGOZE3UTTmJAzmLs_sYjfQuRv_A4GS3ytpYamIl-jHmjLdoy1AEBztSMJP9Efxqvf4BDccMt5WQmW01HhOSkjATZlnrEmHREyQ8aG9MHq4EIdByBZWyPcuYJTFQ3_Ivn4QD_qULT4iYZenUiFsXIzGhdDVVR3zHWjjfmmzoaFKWU-6lqaH4zfgjuScYE41p5MhLX_ks1YvboOwbOV97rEi7e4K5gvK4wKknDjr2A0mVgOZMKcTPMMC8o49GVy4gIS55Qa69wtiuYxvwyIgiMl0LyLHnroI9DaEJD-w-bv0X31sNOm4mFLix4vs8j4JVY24Ec2FOnCR594nmAXiUWU506lYm3bCdUAeGLwbZS2t5FdbFgz3fXlDDCpUKF3Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa85532cfb.mp4?token=vQ1dND4RFrwz9WLpdDNmExaafTBEO4jdQVVkol-QkfZlMFHuQ_XOSg9rFNkhBZmTG_mBaSTft7BWKfphx5Eb_ROZDQymWiMhr97AsnOP4pxH-nCAlJFg6g6VL1AM0GiGIkIcgiIUyi9PPV5qMIt4R5FWbH6TXMbYcTk8ATDm1Q-g5hnBrWaT2DzaV-uBkO_EBa8ROzAQzOhDmIc0US-jRFJVlcwwSSkx2mug67ZC3aq-R3IKvQUH1YL7ET1ff5UoydmP7lXN4pp5iHwNcHq5NUpybTDI4t1dKdU6QHPewacAWIGOZE3UTTmJAzmLs_sYjfQuRv_A4GS3ytpYamIl-jHmjLdoy1AEBztSMJP9Efxqvf4BDccMt5WQmW01HhOSkjATZlnrEmHREyQ8aG9MHq4EIdByBZWyPcuYJTFQ3_Ivn4QD_qULT4iYZenUiFsXIzGhdDVVR3zHWjjfmmzoaFKWU-6lqaH4zfgjuScYE41p5MhLX_ks1YvboOwbOV97rEi7e4K5gvK4wKknDjr2A0mVgOZMKcTPMMC8o49GVy4gIS55Qa69wtiuYxvwyIgiMl0LyLHnroI9DaEJD-w-bv0X31sNOm4mFLix4vs8j4JVY24Ec2FOnCR594nmAXiUWU506lYm3bCdUAeGLwbZS2t5FdbFgz3fXlDDCpUKF3Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
عملکرد فوق‌العاده و سیو‌های محمد العویس گلر تیم ملی عربستان در بازی مقابل تیم ملی اروگوئه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23675" target="_blank">📅 13:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23674">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qzg5lf4zJXVhMe5YUPQY2brsmO13qmueP649AzdjmZ-BFr5c2Uj98-TCfnsG5L4aBKqUK8lGj3hN7xri8jLrJROuO2Ujwq1O0s-187voTYie5_JViEvRsAxLFnna2zfC-sQpBbmreUIUNYnPeeE88-b2qMcBRhNw5-qpxXIvxvmj6VwvpoIeNX36rqiAP5WMv3RbpKyMZ6WVjCZA-H60w-M2dHmiUwsk1ivxdSZZo67NW2mso6eKqXgXFQL6LqNGXtI5aBtZF2X9dWV4lVt1Wje85Mxam15SyROGg6zCpNeEhCmU9cJ03h0-uaRjM4ijuD3kMGGOUZ___QBXiLEXMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ آرشیو وار: خطای لیونل مسی روی بازیکن الجزایر یک کارت قرمز واضح داشت اما داور تصمیم گرفت این‌صحنه رونادیده‌بگیرد. شانس با لئو یار بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23674" target="_blank">📅 13:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23673">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjFe0BThb2XjfoWqfD4sN1si67ij9Vpxu2-WOMy0AEHBpIr_0Jc1rYeKwjaAFNjDsfOpM7AC81vdvXBiMPpARwvNGEHWUiZdcWNQXv5RDgALMCO9ARMHF0T5LiiGzQ_ADspg1pHco5Wst_MiP1Rvgljm9rzeR7jNxN9sDglshGAc7GA1BlwCx2Emx3MxT6g4w-atN78TWQFWznnFDK_qtRQt2t0lUFb3l_2bYykuoaDZgoVd7xjPjrcMdhG-jUBS1atJXsfunx1N-WDVulQ9mWbp4dFAazDPgDb5e0YhsDR52hfISA2eWC-mDqAsaAs5WehXMkjRZsESa3HuXBIuKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
خوزه‌فلیکس‌دیاز:فلورنتینو پرز میدونه برای جذب مایکل اولیسه بایدرقمی بیشتر از 150 میلیون یورو به بایرن مونیخ بدهد تا راضی به فروش این بازیکن شوند و قصد داره همین کار رو نیز بکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23673" target="_blank">📅 12:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23672">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzF9nzSEzN21Eg6v7wQ3QdcEG7XVEh0Gcy_qfhYddo7TtQe1edlAq7JiyHN8Hu3gv9HHimb_RBVgc2LUTK3vpzs3Z9beOmfYFeI6WTCImudTUeFMJU-4Mn0LTILKi_2uIOlejni29A05fm9yAHGukU--iqxPP3_H9djwJeqQuBq-qK57uMYtadw3V_5Sl3FY7rE52GrJohG6wByKGPZ3kqXLbYmRby6WyL8ToNz0Hl4pc41k1ayHfIS0xm0jU3DOoVrtnjqBGlTsrqS1ia65QfrKdYfu536knPfjURIb1VmIs03E8MWqOE3pyhdzff4HBzty3QiphJVbTelNZ3hwRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ برناردو سیلوا تست های پزشکی باشگاه رئال مادرید رو با موفقیت گذرونده و باشگاه بزودی پوسترجذبش رومنتشر میکنه. قرارداد ستاره پرتغال با رئال مادرید 2+1 ساله به ثبت رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23672" target="_blank">📅 12:40 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
