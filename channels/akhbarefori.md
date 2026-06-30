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
<img src="https://cdn4.telesco.pe/file/GoxK92jFV1TD4kSacUT0namVFn_4mZHzbld4AdeZRTyZUvQK3LX8-qrXbdECKfsvB8KxpghfmuK2m5h9R5A5dAqdT4tcQtdUrUuXqOnhzmTZSeT3GzPjn_0UO6DKWkILbfUlaPbtww67hdjGMpe7EeYQByyydbTSLOqRtqGxxXEzzgprf5DK1mJm6pUI0NlsdXNX2H22kIiMsD401o0VH8il0UBaDjBFSWLNpXjKy-MfUr9K7tXgFOcL8PUcDufH8xGSWGtGtVpCjhLWNxmfHqezdOjrLn8eFO8IuqsFTmRt9kLMzxr3m-OAjt4xkG_PK6-huLK-8CkZr_AXKZ3o9Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.17M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 15:58:22</div>
<hr>

<div class="tg-post" id="msg-664953">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rU9v_XCZlO3uOD4MB2bvPc7WWgDFVBzBzTpjBs4L2cf4ljjJqA88WQP--OZS3Tnby-O096IKetLfBk8sl-dzu2406y7YENbd6H1zm_rJUYsEPHfnLHWBhvLEh2qerldH-eBNU2CQVez5p7DKCUlfajIK13NvSckOrajLyP11fqyZGQ3-_4uK9hh2Y5S74uVIaehSRjTyS2lHDS3VCRgMsccbn1-Oz3sYwTVgcF2Hhq51Oh33Qlq9yQZ45ZvQ1V3l0fFtG9jJ-PJ4EC-70TOOF1Z6_Ouf89SVXBKoHtEgKDn6KAGXQjjUVy2PS7SN6EZg7z7Sv4uH6JuaXFxg10NJ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عجایب زبان‌فارسی که از شنیدن آن حیرت‌زده ‌خواهید شد
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/akhbarefori/664953" target="_blank">📅 15:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664952">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0a535da08.mp4?token=MsbF0SzPvLAUGUP4LAjYVkUPV6OWTizrLipWb-NZpX1Fl9yzW79NLSagDGi4UzzmzW1sVQmWJ3NifXLnjfmpfGig7QUYfYtSCoiC7PkB6FvmtmMVRFlDu5rdJ1zsD3JUmb7YdytLBU-ZoDK2uEHmbRNDvxcSGgA__Hn-ZEVYn3DySlRwxjMFtiL_3pORJVVWmSWflUN5FoHEMQ-krye8WhHcwA4GYQc0fOAPc0SCUAHLODKq-olCLbsl6sBRWSethTjXJiJKZZCoN9pUu6T1xCydDBogc-mbq1vclB8a7DXtgn3ae0G9hle3vkA5ZjphpnQT3Ey08qr4E5yehMyAQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0a535da08.mp4?token=MsbF0SzPvLAUGUP4LAjYVkUPV6OWTizrLipWb-NZpX1Fl9yzW79NLSagDGi4UzzmzW1sVQmWJ3NifXLnjfmpfGig7QUYfYtSCoiC7PkB6FvmtmMVRFlDu5rdJ1zsD3JUmb7YdytLBU-ZoDK2uEHmbRNDvxcSGgA__Hn-ZEVYn3DySlRwxjMFtiL_3pORJVVWmSWflUN5FoHEMQ-krye8WhHcwA4GYQc0fOAPc0SCUAHLODKq-olCLbsl6sBRWSethTjXJiJKZZCoN9pUu6T1xCydDBogc-mbq1vclB8a7DXtgn3ae0G9hle3vkA5ZjphpnQT3Ey08qr4E5yehMyAQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: قالیباف به‌عنوان نمایندهٔ ویژهٔ ایران به چین سفر می‌کند و ترکیب هیئت همراه و جزئیات سفر به‌زودی اعلام خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/akhbarefori/664952" target="_blank">📅 15:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664951">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجهٔ قطر: اموال مسدودشدهٔ ایران آزاد نشده و آزادی آن به پیشرفت مذاکرات ایران و آمریکا بستگی دارد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/664951" target="_blank">📅 15:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664950">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a301d9738e.mp4?token=hNv-2SQCZv2bsXJv9yjAcphnxL58uZiz6EwYBG9O2RL9k3YxKWQXcIuddj2Ep_fmGK2OCuegOhjYhezNAtsAWpGUxtgcoNon7g-cYrHIl-SWYMAAfd6he5OZvA_5veUl1M3snAuOLbx4M13Gd9R3pRT0DSNB0NBQntwgcVYOm11I4rNQkHqGATs9s6j3Yida3pYvDaHnM2ldH5HMKjlpN2GD_lII3Rx5Lt6-JMcMARDfKZ2176uae33ay7tTJrqqNHDw_KqepuMCRXwpBqkvK2nSSri_qEEw6Mtu_ArDLwkBmTxJeyd1BwZAlpNnNFD2ocFewZufduCHLJ61u8lEMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a301d9738e.mp4?token=hNv-2SQCZv2bsXJv9yjAcphnxL58uZiz6EwYBG9O2RL9k3YxKWQXcIuddj2Ep_fmGK2OCuegOhjYhezNAtsAWpGUxtgcoNon7g-cYrHIl-SWYMAAfd6he5OZvA_5veUl1M3snAuOLbx4M13Gd9R3pRT0DSNB0NBQntwgcVYOm11I4rNQkHqGATs9s6j3Yida3pYvDaHnM2ldH5HMKjlpN2GD_lII3Rx5Lt6-JMcMARDfKZ2176uae33ay7tTJrqqNHDw_KqepuMCRXwpBqkvK2nSSri_qEEw6Mtu_ArDLwkBmTxJeyd1BwZAlpNnNFD2ocFewZufduCHLJ61u8lEMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صنعت‌زدایی؛ راهبرد تازه پس از ناکامی پروژه براندازی
🔹
برخی تحلیلگران معتقدند پس از ناکامی سناریوهای براندازی، تمرکز فشارها به سمت تضعیف زیرساخت‌های صنعتی و زنجیره تولید ایران تغییر کرده است. در این نگاه، هدف فقط توقف تولید نیست، بلکه افزایش وابستگی اقتصادی و کاهش توان خوداتکایی کشور است. از این رو، تقویت صنایع راهبردی، توسعه فناوری بومی و تکمیل زنجیره ارزش، مهم‌ترین راهبرد برای حفظ استقلال و امنیت اقتصادی کشور به شمار می‌رود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/664950" target="_blank">📅 15:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664949">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59f4c0cc01.mp4?token=iTW7XimQmrqpATQuZKGM2pIEnM9VGDhXReh1-lZ4Y0VmMSJgL_CkDmTj6PXIDIsXSZyrb7Gi9wWA069fJvOCaViG4FAJBDiXGYYji-GF_gdA5BD_uIjhupMP85UF4aj20-35JdpKxnDAbJ0TToLolqwecPVAraW2H0ApoDtlFi3th3RM0xPi8vKzjElN1F-1iw3DhHDY89f-wSbMrfQ3qmvI9mOYHf-H9Dci1fa0GxwI2qXh222MbVaZ9W0w0pamsAhPs_5sTY53EUHYEVqTs9rR1vBSRh2kYo32KYRVRsElcSBtZQzo8QNDwKivevlEhwKaZljRDz93t0eYwhVfcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59f4c0cc01.mp4?token=iTW7XimQmrqpATQuZKGM2pIEnM9VGDhXReh1-lZ4Y0VmMSJgL_CkDmTj6PXIDIsXSZyrb7Gi9wWA069fJvOCaViG4FAJBDiXGYYji-GF_gdA5BD_uIjhupMP85UF4aj20-35JdpKxnDAbJ0TToLolqwecPVAraW2H0ApoDtlFi3th3RM0xPi8vKzjElN1F-1iw3DhHDY89f-wSbMrfQ3qmvI9mOYHf-H9Dci1fa0GxwI2qXh222MbVaZ9W0w0pamsAhPs_5sTY53EUHYEVqTs9rR1vBSRh2kYo32KYRVRsElcSBtZQzo8QNDwKivevlEhwKaZljRDz93t0eYwhVfcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از شهدای حمله تروریستی در پاوه
🔹
روابط عمومی سپاه استان کرمانشاه از شهادت دو تن از نیروهای بومی سپاه پاوه، «برهان کریسانی» و «خالد خالدی‌نیا»، در پی حمله تروریستی و تیراندازی بزدلانه به درب منزلشان در شامگاه دوشنبه خبر داد.  #اخبار_کرمانشاه در فضای…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/664949" target="_blank">📅 15:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664948">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
آغاز مرحلۀ سوم ثبت‌نام طرح مسکن استیجاری
🔹
طبق اعلام وزارت شهرسازی مرحلۀ سوم طرح آشیان؛ ویژۀ استان‌های گلستان، ایلام و کرمانشاه، از ساعت ۱۲ امروز آغاز و تا پایان روز چهارشنبه ۱۰ تیر ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/664948" target="_blank">📅 15:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664947">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
بقایی: هیچ درخواست رسمی درخصوص بازگشایی سفارت کانادا دریافت نکرده‌ایم/در صورت دریافت بررسی خواهیم کرد  سخنگوی وزارت امور خارجه:
🔹
از دسامبر ۲۰۱۲، کانادا بدون هیچ دلیلی به‌صورت یک‌جانبه تصمیم به تعلیق روابط دیپلماتیک با جمهوری اسلامی ایران گرفت.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/664947" target="_blank">📅 15:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664946">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d935105e6.mp4?token=ebjGq5dMKH1fXZ3ESTa0zJiS6mxPdmpXZP88eFLVVHtERaD0EqiApfE5zS7rrnPi0dD_77MStfkVk3_cqeuUF7wFFhrXOFACvJ4DwRqGLeNI80jK6qlbc_NGwSdcA5lUHljUktjrnU-WLnqiuC1OJePbaG_LWCKMnZt3vVBbaN-pgqeIslPOziMaGQXhPO1A9a9gfMwNo8TWlCxK_Y7iLwQjAJPwHQbuZrZlcq5_N2DwOGqJEwq5TT0f2ZVLp29B7B8R9GFtXHZl90XEngyu9Pr4PrgUbOjNGEjHNOz4t271kVZd_p60fATC91TDjz9sk0X0QSJdiOWnBm1m-nSw7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d935105e6.mp4?token=ebjGq5dMKH1fXZ3ESTa0zJiS6mxPdmpXZP88eFLVVHtERaD0EqiApfE5zS7rrnPi0dD_77MStfkVk3_cqeuUF7wFFhrXOFACvJ4DwRqGLeNI80jK6qlbc_NGwSdcA5lUHljUktjrnU-WLnqiuC1OJePbaG_LWCKMnZt3vVBbaN-pgqeIslPOziMaGQXhPO1A9a9gfMwNo8TWlCxK_Y7iLwQjAJPwHQbuZrZlcq5_N2DwOGqJEwq5TT0f2ZVLp29B7B8R9GFtXHZl90XEngyu9Pr4PrgUbOjNGEjHNOz4t271kVZd_p60fATC91TDjz9sk0X0QSJdiOWnBm1m-nSw7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازگشت تلخ کره جنوبی به اینچئون؛ هواداران خشمگین به استقبال تیم حذف‌شده آمدند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/664946" target="_blank">📅 15:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664945">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هرمز؛ برگی که نباید بسوزد!
🔹
همه نگاه‌ها به تنگه هرمز دوخته شده؛ آبراهی باریک که این روزها شاید ارزش آن از بسیاری از میدان‌های نبرد هم بیشتر باشد.
🔹
شواهد نشان می‌دهد نبرد اصلی دیگر فقط بر سر عبور کشتی‌ها از این تنگه نیست، بر سر این است که چه کسی کنترل مهم‌ترین گلوگاه انرژی جهان را در دست بگیرد.
🔹
امروز تنگه هرمز مهم‌ترین برگ برنده ایران در معادلات منطقه‌ای و مذاکرات با آمریکاست.
🔹
برگی که اگر از دست برود، تهران یکی از قدرتمندترین ابزارهای چانه‌زنی خود را از دست خواهد داد و به میز مذاکره با شرایطی نزدیک به گذشته بازمی‌گردد.
🔹
به همین دلیل، مخالفت ایران با هرگونه دخالت خارجی در مین‌روبی یا مدیریت تنگه هرمز، صرفاً یک موضع نظامی نیست، بلکه دفاع از یک دارایی راهبردی است.
🔹
در چنین وضعیتی، طرح‌هایی با بازیگردانی غربی‌ها برای ایجاد مسیرهای جایگزین کشتیرانی و سپردن امنیت تنگه به بازیگران دیگر مطرح شده است.
🔹
پیشنهادهایی که با استفاده از ظرفیت کشور دوست یعنی عمان، در ظاهر با هدف تسهیل تجارت جهانی ارائه می‌شود، اما در عمل می‌تواند نقش ایران را در مهم‌ترین اهرم ژئوپلیتیکی‌اش کمرنگ کند.
🔹
اما این فقط یک ضلع ماجراست؛ ضلع دیگر عمان است، کشوری که شریک تنگه هرمز و یکی از معدود میانجی‌های قابل اعتماد در سال‌های اخیر بوده است.
🔹
برخی بازیگران به‌خوبی می‌دانند اگر تهران و مسقط بر سر آینده تنگه اختلاف پیدا کنند، مسیر اجرای طرح‌های ضدایرانی هموارتر خواهد شد.
🔹
نبرد واقعی امروز، نبرد بر سر کنترل روایت و مدیریت تنگه هرمز است. هر تصمیم درباره این آبراه می‌تواند توازن قدرت در منطقه را تغییر دهد.
🔹
ایران باید بیش از هر زمان دیگری مراقب این بازی چندلایه باشد، بازی‌ای که شاید با یک پیشنهاد دیپلماتیک آغاز شود، اما پایان آن می‌تواند تغییر موازنه قدرت در حساس‌ترین آبراه جهان باشد.
../خبرفوری
#سرمقاله
@TV_Fori</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/664945" target="_blank">📅 15:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664944">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نگاهی به عملکرد ۳ سال اخیر بانک توسعه صادرات ایران
🔹
از رشد شاخص ها تا بهبود خدمات بانکی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/664944" target="_blank">📅 15:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664943">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: آمریکا صراحتاً دربارهٔ پایان جنگ در لبنان تعهد داده و باید به تعهدش عمل کند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/664943" target="_blank">📅 15:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664942">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ded290b18.mp4?token=BiR6iEb0GHKNUPYO7pYW1Fdbl5CANbq3sDg8rjepX5bG4GpiWkroGmsRGLFGe4CDfry2c-zZR4a_5qVCHfAi5G1GWmevXW1hIUCPdA47I1j3iyu9PzX3SS6faZ140e2fdM8riFDAadMiiyAoPyuCy1dox3ZFDtWePCKnxNQbTns3TEfBi08W-UC_LUjpQyfZB1hbMIS4JQjqhWWwbzDvA-sEZYCWdlIFXYmC2qc56RodhF6tcuAxxahcLZgLoy2PoJs6D8XZq0ZHt2F-ZYHSADPYxMvWtYnabg0z_q6J7Gf4FqRTAvD5KQGmMa2dJ8B2pioQkXODNbmVhwjJGTm24Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ded290b18.mp4?token=BiR6iEb0GHKNUPYO7pYW1Fdbl5CANbq3sDg8rjepX5bG4GpiWkroGmsRGLFGe4CDfry2c-zZR4a_5qVCHfAi5G1GWmevXW1hIUCPdA47I1j3iyu9PzX3SS6faZ140e2fdM8riFDAadMiiyAoPyuCy1dox3ZFDtWePCKnxNQbTns3TEfBi08W-UC_LUjpQyfZB1hbMIS4JQjqhWWwbzDvA-sEZYCWdlIFXYmC2qc56RodhF6tcuAxxahcLZgLoy2PoJs6D8XZq0ZHt2F-ZYHSADPYxMvWtYnabg0z_q6J7Gf4FqRTAvD5KQGmMa2dJ8B2pioQkXODNbmVhwjJGTm24Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی دیده نشده از شهیده زهرا محمدی گلپایگانی نوه رهبر شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/664942" target="_blank">📅 15:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664941">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ادعای اکونومیست: جنگ ۶۰۰ میلیارد دلار به ایران خسارت وارد کرد!
اکونومیست:
🔹
در چهار ماه گذشته، طبق گزارش صندوق بین‌المللی پول، جنگ ۶۰۰ میلیارد دلار به ایران خسارت وارد کرده و تا ۷ درصد از نیروی کار این کشور بیکار شده‌اند.
🔹
اقتصاد همسایگان ثروتمندتر ایران در منطقه خلیج‌فارس نیز کوچک شده و این درگیری ممکن است امسال دو درصد از رشد تولید ناخالص داخلی را در خاورمیانه بزرگتر کاهش دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/664941" target="_blank">📅 15:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664940">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: اساساً برنامه‌ای برای دیدار با آمریکایی‌ها در هیچ سطحی نداشته‌ایم که بخواهیم از آن منصرف بشویم
🔹
گفت‌وگوهای دوحه دربارهٔ اجرای بندهایی از یادداشت تفاهم است و با هیئت قطری انجام خواهد شد.
🔹
اجرای بند آزادسازی دارایی‌های ایران در حال انجام…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/664940" target="_blank">📅 15:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664939">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: مین‌روبی تنگهٔ هرمز براساس یادداشت تفاهم مربوط به ایران است و نیازی به دخالت دیگران در این موضوع نیست.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/664939" target="_blank">📅 15:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664938">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czwTLFwopqEEUxIiMGm8WVHbeDEZZpuYDhXplmz5SxfdA9_t3I1E-31GZyFLZfNfydYVMW4NeUYOFNdxcNzFS7hm5cwTnbmmKDaD3_k_gZxIEc0uepDYtncKcwvs3c3JfNc7V6x_1ufsLGaEXxOA5z5bKOF3ZL-ohmgtdJ-kJe57FxAGvAjjglZAaJyL1sUFQT1EcFf5Pqqap9Z9n8w8QqtpH_i_uLbj8zZnEryYnNC25xjjFfCEYRuvD3kPNFdQqH67uRkj6XPdsxXcoDNRWGYgYgTkP2dfwCIGGuHrdNW98NHC0gDX4MPgbMjcrZnMYicxdmlrc9Nelmjr9uNe-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اطلاعیه شماره یک قرارگاه برگزاری آیین وداع و تشییع قائد عظیم الشان شهید امت (تهران)
🔹
از هموطنانی که قصد حضور در مراسم را دارند، درخواست می‌شود اطلاعیه‌های رسمی را دنبال کرده و با عوامل اجرایی همکاری کنند.
🔹
برای کاهش ازدحام، زمان حضور خود در تهران را کوتاه…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/664938" target="_blank">📅 14:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664937">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781702a3b6.mp4?token=hVr_oRaT-Q0IgbARsIXEUaETsGyvcwMnF-EHd9bRkyES44pm0A_glilF39-AVsD1-tl6Lt9rcSFnkw9FqQ2w7PUKzOPtpj5G_sLYW_rOdicHViPu9lU-BwbJOuL7MyT7hp-i6aD1wQmalvvOdc5DCthds0YQVYkv11yb5BRHE6rh_6flYUznUP3JecVgi9ZDcXEnhyhpBBKKP-L8XI_jKDxlUzJ-IwrLJLEzHU0RFGn2ULi8VLdoKp_97LnV-1sccz1AvdLnz3oeL20kvtANQLWljAjUCXfchJTLBvYyxckeNiFQaHvozSuL5wL-gb9dQdz6I3r-SoIUwSn2YwzV1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781702a3b6.mp4?token=hVr_oRaT-Q0IgbARsIXEUaETsGyvcwMnF-EHd9bRkyES44pm0A_glilF39-AVsD1-tl6Lt9rcSFnkw9FqQ2w7PUKzOPtpj5G_sLYW_rOdicHViPu9lU-BwbJOuL7MyT7hp-i6aD1wQmalvvOdc5DCthds0YQVYkv11yb5BRHE6rh_6flYUznUP3JecVgi9ZDcXEnhyhpBBKKP-L8XI_jKDxlUzJ-IwrLJLEzHU0RFGn2ULi8VLdoKp_97LnV-1sccz1AvdLnz3oeL20kvtANQLWljAjUCXfchJTLBvYyxckeNiFQaHvozSuL5wL-gb9dQdz6I3r-SoIUwSn2YwzV1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: مین‌روبی تنگهٔ هرمز براساس یادداشت تفاهم مربوط به ایران است و نیازی به دخالت دیگران در این موضوع نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/664937" target="_blank">📅 14:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664936">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
قطر: هیچ دیدار سطح بالایی بین آمریکا و ایران برنامه‌ریزی نشده است  سخنگوی وزارت خارجه قطر:
🔹
ویتکاف و کوشنر در دوحه هستند و مستقیماً با مقامات ایرانی دیدار نخواهند کرد.
🔹
۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است./جماران
🇮🇷
…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/664936" target="_blank">📅 14:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664935">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bd43a26eb.mp4?token=PKmf7xtamjTgMLSVa6FBC4SQQ2VHKnEtt6SzVIQVRtgWSWYrsE2T7UnW-X5vf0EiMO8Zs3HPqmNy5w-6r994NIPx8kWIccTsOFQqRNdzrb3MfsnJ4UckTg_d0wIUMHZE1W3TLUFcMvtqRjPAcOYrQBAwMkxPpu435DqUyAUC-6oQI2PnbiJoR8-Hc51oYEqw3qu1_f53kseiZClEgWOHBxL23OWwvz1RP2mtmNRLXTqGG7BF6A_REfMQex14H_-i8n4Twevv50gLkZUpWZ91HiWnreVqbB7mloudQc3M5HNoVoLOyfdgmNfnga0Vu6w5FJeLzTcrnUJ7Ky4He-4Wzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bd43a26eb.mp4?token=PKmf7xtamjTgMLSVa6FBC4SQQ2VHKnEtt6SzVIQVRtgWSWYrsE2T7UnW-X5vf0EiMO8Zs3HPqmNy5w-6r994NIPx8kWIccTsOFQqRNdzrb3MfsnJ4UckTg_d0wIUMHZE1W3TLUFcMvtqRjPAcOYrQBAwMkxPpu435DqUyAUC-6oQI2PnbiJoR8-Hc51oYEqw3qu1_f53kseiZClEgWOHBxL23OWwvz1RP2mtmNRLXTqGG7BF6A_REfMQex14H_-i8n4Twevv50gLkZUpWZ91HiWnreVqbB7mloudQc3M5HNoVoLOyfdgmNfnga0Vu6w5FJeLzTcrnUJ7Ky4He-4Wzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کادوهاتو شکلاتی بسته‌بندی کن
🍬
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/664935" target="_blank">📅 14:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664934">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تشکیل وزارت مدیریت بحران در دست بررسی مجلس
کامران پولادی، عضو کمیسیون امور داخلی کشور و شوراها در
#گفتگو
با خبرفوری:
🔹
در دنیا حدود ۴۵ حادثه و بحران وجود دارد که ۳۴ مورد از آن‌ها مانند سیل، فرونشست زمین و... در کشور ما در حال وقوع است.
🔹
خیلی از کشورهای دنیا برای این منظور وزارت مستقلی تحت عنوان وزارت مدیریت بحران دارند؛ ضمن اینکه ماموریت دستگاه‌های مختلف در این راستا نیاز به یکپارچه‌سازی داشت که ذیل یک وزارتخانه قرار بگیرد و فعلا تشکیل این وزارتخانه در مرحله مقدماتی است که روی آن بحث صورت می‌گیرد.
@TV_Fori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/664934" target="_blank">📅 14:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664933">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlXCILegzV81l14gj2721wH35tWKokhiR-WO85bveRiL45z79C5WfCWO3KibxlBAe8xUzvIHV3Ga2DCsbG3BipOTz4gNAr9cAEEta-SnVfsMSPKm_pInt8vAne5Dmf-Yome6fqmwhFpJNru8k_xG_DiIMYBGg6vixAIDVzhnJLKk3H4-AQhPULkjq-Np197PphySunsJYFthS62E1hiCk2b6chRID62viJQsx4ls2rPT3mhmmZVa5Gd3mnljQI2Oi0gsttZ6mUk78YCVhlZXzfXB3wnrCmEFpuiVn4UkCwuKZz6j5z2JDFMdVAW26R3-owBR2oBofO84iSU3ZddhKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایرنا متن خبر درباره رای سعید جلیلی درباره توافق با آمریکا را تغییر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/664933" target="_blank">📅 14:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664932">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
تهران ۳ روز تعطیل شد
🔹
به مناسبت برگزاری مراسم وداع، نماز و تشییع پیکر رهبر شهید و خانواده ایشان، تهران به مدت سه روز تعطیل شد.  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/664932" target="_blank">📅 14:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664931">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iI9ikYj4krwVkSDCPeA_LYtrh0yEewKIjlEGnyx3NYQnZrjZAItM8kPbit7aUr0NeMuHuj5Qlk2diYNdN0SqZ3MlzxmE7PLrmc0y-_6B6Uk4XfFrxvCfniFLMHls4pXQcd_wHKkTmmcG7k_RrGtbgOdDTDAEMyLvdrH3MEPpAZ2sMLZJtBHZFML_iNAmXzBD8lPH7KefLkvZbI67ORNODwMZSpeN8WocCaf4A9HMGMwtqtVFvI3j1hBgt7dZMonqJAck4VgxftoUGUhIpUjoYXSJqRhoM54h2S4thdbfB_3hXdcYP4W3xMUpKJzOLHSr0lef36pDtvF6AYPiFRGZnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بالاخره بعد از سال‌ها یوزرنیم به واتساپ اضافه میشه!
🔹
واتساپ بعد از مدت ها قابلیت انتخاب یوزرنیم برای حساب‌های کاربری رو اضافه کرده و از همین الان میتونید یوزرنیمی که مد نظر دارید رو برای خودتون رزرو کنید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/664931" target="_blank">📅 14:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664930">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وششم از فصل چهارم
🔹
در این قسمت بخشی از روایت تجربه‌ نزدیک به مرگ خانم زهره ابراهیمی که چند روز قبل از تجربه حضور ملک‌الموت را در کنار خود احساس می‌کردند و در شبی با رؤیت ایشان و فشار اجزای اتاق روح از بدنش جدا شده و با سفر به عالم برزخ و درک کامل از مرور زندگی گفته‌های شنیدنی را نقل می‌کند ، نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: زهره ابراهیمی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/664930" target="_blank">📅 14:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664929">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
محل تدفین رهبر شهید نقطه‌ای انتخاب شده که در آینده امکان زیارت هم‌زمان برای بانوان و آقایان به راحتی فراهم باشد  دبیر ستاد مراسمات بدرقه و تشییع رهبر شهید:
🔹
همچنین جایگاه تدفین به‌گونه‌ای جانمایی شده که در روند زیارت مرقد مطهر امام رضا (ع) و آمدوشد سایر…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/664929" target="_blank">📅 14:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664928">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9b6b04288.mp4?token=DtdXk-Jx-LIhxYyVpymiNHATk2knaT19gFnZ2veEDcpw0oKIjemwZlyJi45kIo7r4hIde-4pSiJRU-1ZocGkJQduLiKnigntRInfv_yMH1AX8vSYqa3l86xzWgOusklYXaJ_KK89EYr79h0K4I_vyn3IPNzsEZTsUqFYs5e8ZWy3NsiWM1tP-Pi8o0PuOuFFqhD2OZg_oCpj8D18TLxu-KXlqRz6WO-e3jdoDTPmOtrxyCIX6xinQ599bTzzCywVuMmukJZE0Skdinkl5IWkSoIABbo2mch2d5tYVuEq2kxsmIT_y0RrZmq-CrnI4qswegNX3YUB4VE6weFnT25XohREHO5eiliJ8WIKuYznhwy5Ak_2CxHZ_hLR546fF7m3z7NUoyRKlM0aXeBFnzLn-LB9LR1RFpxZIHpedPNSduoclZ-zCfCO3O8eoTAp9NcYv6aOFG_Foe__ftLfXtyJ-0Wa4CaXu4YdDURuW_STcCymBg1KoNoDc5zxxBrpvG7FZUagBnBIeo4f9O2YjLvThNh8UZnn75W3cTjGSjW5P0nmVIxYVQByraCLwqAa3iULHcyy1IFL7wirMrrC750KKF46RY3qAkHme4PMRI0jFhOjGoZRw54xUTUJmpNz8d1O-VS0TyBdM8LGbc-2yt9KCz9NJ65rVTBeORj2Se30oD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9b6b04288.mp4?token=DtdXk-Jx-LIhxYyVpymiNHATk2knaT19gFnZ2veEDcpw0oKIjemwZlyJi45kIo7r4hIde-4pSiJRU-1ZocGkJQduLiKnigntRInfv_yMH1AX8vSYqa3l86xzWgOusklYXaJ_KK89EYr79h0K4I_vyn3IPNzsEZTsUqFYs5e8ZWy3NsiWM1tP-Pi8o0PuOuFFqhD2OZg_oCpj8D18TLxu-KXlqRz6WO-e3jdoDTPmOtrxyCIX6xinQ599bTzzCywVuMmukJZE0Skdinkl5IWkSoIABbo2mch2d5tYVuEq2kxsmIT_y0RrZmq-CrnI4qswegNX3YUB4VE6weFnT25XohREHO5eiliJ8WIKuYznhwy5Ak_2CxHZ_hLR546fF7m3z7NUoyRKlM0aXeBFnzLn-LB9LR1RFpxZIHpedPNSduoclZ-zCfCO3O8eoTAp9NcYv6aOFG_Foe__ftLfXtyJ-0Wa4CaXu4YdDURuW_STcCymBg1KoNoDc5zxxBrpvG7FZUagBnBIeo4f9O2YjLvThNh8UZnn75W3cTjGSjW5P0nmVIxYVQByraCLwqAa3iULHcyy1IFL7wirMrrC750KKF46RY3qAkHme4PMRI0jFhOjGoZRw54xUTUJmpNz8d1O-VS0TyBdM8LGbc-2yt9KCz9NJ65rVTBeORj2Se30oD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بدون فرمان، بدون پدال؛ تسلا آزمایش تاکسی‌های آینده را آغاز کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/664928" target="_blank">📅 14:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664923">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UAPKgzqHy4Ss_VONuWPWLbN1DX7ai7uMkuxFDnreaX1rt01fBxhMw8cIjAqZPmHl7AMGBwYTPQ4lobAiz4d_cQi9tbQn2m9aU7kASrURgNrgF8Spov1LjRLZTT4ppF_CEbeKKOdA1_pcRb-2Jg8z8zqc9GQH3euh9_k8OFxNkzh_ohqKAkFXZrVF_3os8JZn3Caw8nxYJW1Q37V4pdKUAz-pDzN-t1A8cqB9E7D997Bo2UgjQKcwJ_43RnbpEXkVsPEDXRrDyryJWJBBgW5mj74I-VTSSrn8fhZOPnwtzBkWUNKAl_xtWJqC3eCFCVYbImNIM6BDIEzE-eM9Y4N-uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MKAPrcxb5IXIyXyrxx2AxZE30xlwFwUo4PEIHB6BSowY_96oAMyY75ygCD1QSsnLVmJRtAxjwjB2XV0ZXmWPHLazZKhLCSaJGmdlEEb67dQI0XaTZk8F5-I0SYkd_6_P6rgHvJV1AB0nkyLZ4T66-6Ucq0qoqmcQIMbC61eCpxZZ5S_el43J9zClvkxA16RhSxFaY1-BuGUEd1aiVZ7kRwBXTLewIXkwMbPde1d_9fSyBJCJnpob6XWymbEnSaJ1_0m_aR8sZtVSi0llBq16OeSq5uoXmtH8tKqAyYLnUe9H_Vmr607ILBy1-v_5aGKiHgKI6yT6iLx0WDO6X3H7Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8ARzBvC9uCwyPNvYpOzXnXf5i7CBs1efXhsE5vHAQlPxPxxJxM0PC1Xh9zl9MRkTP2PHsHRdtWaVGgy0Hm406mWyzRgxwmtQVpgoIRcENJyGZ3K2miw15DTcCOw0aHsNritbCVC9-L0ZRT9plqHmX7HIb34IaWyrC9SZ-Li_jiXcc0p2grfk3S05jpCPc_LvndCCQSC2Dk_hUrZntAtuTtIzUALGB2KG7jcMZ0s8bqp_6RFYKqoLeKplWSg-eWQE9_HeoHr-X64f8dQ0gFPOahYL8Joo4IuAlLqt7h_ncOcSdpEE3e_Ca4u3EJu3F9kNJKHcOio_v8XgrI0nfpEjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/odIt0DAj_J0srJ8R0vAHIXeHJtiiLi4mgHT_cfHePmPXKnoYsowbaAOh4rPpI50TGe2nLglzv7A2nfXPpE71M2IgtR0NzTSHercKtRI1xjwYM571oE45GwJInKWtrXg0R0FYYF_nHHD8QCWD44v9x7Zm7aPnc_FT8kQrNByaE6-AXuS9scYHw8CHc_u_VrOuNCkiGrAb-pjbgCCvtYeZkR44OQDkZSy_n4MkQEkdzJRAzmhLNmuzZA6DMc8_dEitwPzlmVbf7_vz03sQ0fdMpv-pqiRi7o51_ktUVd91l_rgGIrfpgqQJcLuxbTciAKkjQVxIzvRLhMIY0ymdiEmeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jz6Pa9zyPZCx-NE5j1V6B8iXKL0MF7XNlhPEORlGxRmlO_9gKyes5pTxaMUH0t65OSun7j6boYMYGUpsIEOZ1OMZhg6ryxO_IYuNSQfDGMxewUV3tE4LISEwKDbWp_4ntvv3feOAAuyXGvXpsy1rAp0abGLsQijkBy8zZrSqzYvTDnhs0J8XiSSitEbJkmWLp-17YZGY5OfrRQy0viQXaWbcsYmNrAxnp99E2kdpfcAjW5hhqF0G3xl4kz6whxuqlIESfT_lX9HZkROKAsC0BZGBDMtMas9Xu3JN7DgXFLRcrSIQ_ffF_ht_BoKMzEPaXZrkA_eV2yn4pwmhnmfAJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تأثیر هر قرص بر سلامت و رشد مو چیست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/664923" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664922">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcbd4f0172.mp4?token=FeOTZLqbPoIyDAc7Z6k1An-y8a1aWV34mTIAnyxsHaXFfkcwSXtMl6qp8JQpCNVnxSXMBJhzPGI9QT0Cp-AzACCDY95xFIYd8lzipzhPCdnu0MAvsd9nO5PIzUKkXatibfHEO-CZXJidv5HPtURyI-xJZWgKjlxDUYWPd12h1alSDD2vvqWhVwZ3ly9ZaewuyAeZJ45JdTSomWYL-iRpjK6_lO9yer9H1GZ7mkXEiqQKMH1UCkcaQUFoT-wPfjoYlP6YHzfbl3DEUkGKLlsRIFEovKuLlFvjAJLtEyY7McHYF5H4E1uNquXpdmmOqSURLIK2NpELBDpuLzsDwRp1SwYxHJQF8KNYTeg07NPqAX0q0aNFEnwEb0MA01eErDgkjazGCMdNf2crHWXpZFufdnMY6msljSu_vhVfYrjNpzU6GZEfoGeaH9i3pDBF4QgxcgwiB-22IlIpN0XdkEH1a55jL9mogGmPk-D3BnoerEqGpqayFd5m5DROYw7cu9RNBKiZRvRJ0eO4aWZE6XSixEQ7Hj1fj4KQJdKoajqbU74smU4YDxqTDHnvUK7XxafER_4dJGOEDXg3ZeunhmF6pcx6FyIM-lyg81Daj-femQrH9JhBuhygNaQI2IGc0jvG4Y8r28rVbiFZrCW4wpR8NWDT3XqGMEw3g_AOPllbPds" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcbd4f0172.mp4?token=FeOTZLqbPoIyDAc7Z6k1An-y8a1aWV34mTIAnyxsHaXFfkcwSXtMl6qp8JQpCNVnxSXMBJhzPGI9QT0Cp-AzACCDY95xFIYd8lzipzhPCdnu0MAvsd9nO5PIzUKkXatibfHEO-CZXJidv5HPtURyI-xJZWgKjlxDUYWPd12h1alSDD2vvqWhVwZ3ly9ZaewuyAeZJ45JdTSomWYL-iRpjK6_lO9yer9H1GZ7mkXEiqQKMH1UCkcaQUFoT-wPfjoYlP6YHzfbl3DEUkGKLlsRIFEovKuLlFvjAJLtEyY7McHYF5H4E1uNquXpdmmOqSURLIK2NpELBDpuLzsDwRp1SwYxHJQF8KNYTeg07NPqAX0q0aNFEnwEb0MA01eErDgkjazGCMdNf2crHWXpZFufdnMY6msljSu_vhVfYrjNpzU6GZEfoGeaH9i3pDBF4QgxcgwiB-22IlIpN0XdkEH1a55jL9mogGmPk-D3BnoerEqGpqayFd5m5DROYw7cu9RNBKiZRvRJ0eO4aWZE6XSixEQ7Hj1fj4KQJdKoajqbU74smU4YDxqTDHnvUK7XxafER_4dJGOEDXg3ZeunhmF6pcx6FyIM-lyg81Daj-femQrH9JhBuhygNaQI2IGc0jvG4Y8r28rVbiFZrCW4wpR8NWDT3XqGMEw3g_AOPllbPds" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری ماندگار از حضور رهبر شهید در رزمایش بزرگ ذوالفقار ارتش سال ۷۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/664922" target="_blank">📅 13:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664921">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
قطر: هیچ دیدار سطح بالایی بین آمریکا و ایران برنامه‌ریزی نشده است
سخنگوی وزارت خارجه قطر:
🔹
ویتکاف و کوشنر در دوحه هستند و مستقیماً با مقامات ایرانی دیدار نخواهند کرد.
🔹
۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است./جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/664921" target="_blank">📅 13:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664920">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fc7a470172.mp4?token=TwBLcXBGbeUOXGZjSXy3BoCpuUewQKaSqpCzBHYEPvzA8rbHxNHwU23X8s3sakREnw4bZcHDUY8yw0W3iC7puk1yrXyW_x48o0tOhq-HuTHqE0w08zvBBy-ZzThwQxygz278CGqvVyiVcAiPyoYmbU--gv8L1WtebVgtB7AOM9K0-U_u0GbhM4fm6ky9Gbay51mRvdeAo9vN-3WCTxvg9T9Q5nUj8dr4g6F8atga66k87HTxNVRt1L5PqaI-0Kp-6TDFfIidiuz1rnObApZBYNxve5RB5aEqTcHGAD1R6K6aRTj1JOK0zZDmh_lxx2MPhmlc_XDj8c5kw4Ytg7LpTw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fc7a470172.mp4?token=TwBLcXBGbeUOXGZjSXy3BoCpuUewQKaSqpCzBHYEPvzA8rbHxNHwU23X8s3sakREnw4bZcHDUY8yw0W3iC7puk1yrXyW_x48o0tOhq-HuTHqE0w08zvBBy-ZzThwQxygz278CGqvVyiVcAiPyoYmbU--gv8L1WtebVgtB7AOM9K0-U_u0GbhM4fm6ky9Gbay51mRvdeAo9vN-3WCTxvg9T9Q5nUj8dr4g6F8atga66k87HTxNVRt1L5PqaI-0Kp-6TDFfIidiuz1rnObApZBYNxve5RB5aEqTcHGAD1R6K6aRTj1JOK0zZDmh_lxx2MPhmlc_XDj8c5kw4Ytg7LpTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شب سقوط غول‌ها؛ آلمان و هلند حذف شدند، برزیل در دقیقه ۹۶ از کابوس فرار کرد
▪️
قسمت دهم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/664920" target="_blank">📅 13:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664919">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
اطلاعیه شماره یک قرارگاه برگزاری آیین وداع و تشییع قائد عظیم الشان شهید امت (تهران)
🔹
از هموطنانی که قصد حضور در مراسم را دارند، درخواست می‌شود اطلاعیه‌های رسمی را دنبال کرده و با عوامل اجرایی همکاری کنند.
🔹
برای کاهش ازدحام، زمان حضور خود در تهران را کوتاه نگه دارید و در صورت نیاز از امکانات اسکان و خدمات پیش‌بینی‌شده استفاده کنید.
🔹
همراه داشتن وسایل ضروری مانند دارو، کارت شناسایی، آب، خوراکی خشک و پتوی سبک توصیه می‌شود. از لباس خنک، کلاه یا چتر استفاده کنید و از آوردن کودکان، بانوان باردار، سالمندان و افراد دارای بیماری‌های سخت به محل‌های شلوغ خودداری شود.
🔹
اطلاعیه‌های بعدی از طریق رسانه‌های رسمی منتشر خواهد شد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/664919" target="_blank">📅 13:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664918">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kg5YDEz05N2n583WdPicuyU0UFmR9VEU6rHOdPQhGaNwx06drZwb4bXG6KmIVf5MEA7UV8-shKsHpuVPe9JvFWLHaakIK9i5NdQNGzDyhrHPosDusbiUQUsJ_PXdEICmrtbumT5JZ4cjxBn0-Ore2LOo6UigfgiyFq01-vwZh74yAYlLXRgW_uZAwCbmL8-tMxjAglAA3sv28_p9W3Gc3ezK-p53THTMlyDb0zyBXhOfm-ZMEM8We6x0iKJb6QyOAHSUCk5QrBz4B5eerti_2G4Lb039SGR34-1NvH-gZFkCZuRsyiT9RwGVZrrLHTyxMHjM8X6vBVslWQE20kBEjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنان در کدام کشورها به‌طور قانونی حق موتورسواری ندارند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/664918" target="_blank">📅 13:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664917">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
پورجمشیدیان: ۱۷ تیر پیکرهای مطهر به عراق منتقل خواهد شد  دبیر ستاد ملی مراسم وداع و تشییع رهبر شهید:
🔹
در یکی از دو فرودگاه بغداد یا نجف مراسم استقبال رسمی با حضور سران این کشور از جمله جناب نخست‌وزیر برگزار خواهد شد. در ادامه، تشییع و طواف در کربلا و نجف…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/664917" target="_blank">📅 13:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664916">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
هشدار سیلاب و آبگرفتگی برای ۸ استان صادر شد
سخنگوی سازمان مدیریت بحران کشور:
🔹
در ارتفاعات مازندران، سمنان و تهران و همچنین در استان‌های آذربایجان شرقی، اردبیل، گیلان، البرز و گلستان احتمال بارش‌های رگباری، نقطه‌ای و وقوع سیلاب وجود دارد و این بارش‌ها می‌تواند باعث طغیان رودخانه‌ها و آبگرفتگی معابر شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/664916" target="_blank">📅 13:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664915">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نخست وزیر عراق: اجازه استفاده از خاک عراق برای حمله به کشورهای همسایه را نمی‌دهیم.
🔹
وزارت ارتباطات عراق از برقراری اینترنت رایگان در مسیر پیاده‌روی اربعین -بغداد به کربلا خبر داد.
🔹
ترکیه: آمریکا قصدی برای خروج از ناتو ندارد.
🔹
کاروان تیم ملی فوتبال فردا به کشور باز خواهد گشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/664915" target="_blank">📅 13:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664914">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
قیمت جدید شکر و برنج اعلام شد
🔹
قیمت هر کیلو شکر در بنکداری‌ها ۹۷ هزار تومان
🔹
قیمت هر کیلو برنج ایرانی  ۲۹۰ تا ۴۶۰ هزار تومان
🔹
قیمت هر کیلو برنج پاکستانی ۱۹۰ تا ۲۶۵ هزار تومان و برنج هندی ۲۴۰ تا ۲۶۵ هزار تومان /باشگاه خبرنگاران جوان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/664914" target="_blank">📅 13:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664913">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس کمیسیون انرژی اتاق بازرگانی: مردم دو ساعت کمبود برق را تحمل کنند تا برق صنعت قطع نشود!
آرش نجفی، رییس کمیسیون انرژی اتاق بازرگانی ایران در
#گفتگو
با خبرفوری:
🔹
پیشنهاد ما این است که به جای قطع برق واحدهای تولیدی، مردم روزانه دو ساعت کمبود برق را تحمل کنند تا تولید کشور متوقف نشود؛ چرا که تداوم تولید، ضامن درآمد و پایداری اقتصادی است.
🔹
به دلیل نبود رگولاتور و نبود نهاد تنظیم‌گر، وزارت نیرو در قیمت‌گذاری، سیاست‌های حمایتی و مدیریت برق هرطور که دلش بخواهد عمل می‌کند و این عدم شفافیت باعث می‌شود مطمئن نباشیم که رویکرد و عملکرد کاملا صحیحی از وزارت نیرو دیده می‌شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/664913" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664912">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
تهران ۳ روز تعطیل شد
🔹
به مناسبت برگزاری مراسم وداع، نماز و تشییع پیکر رهبر شهید و خانواده ایشان، تهران به مدت سه روز تعطیل شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/664912" target="_blank">📅 13:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664910">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPfVX4zu520_Yr4HJJ6ErCzzUKfo2slAOp3B2xgTN0hvMkbRa0yEJDuOL6q_5xdiQcLVIuAnYgkLo1m1RYIPN-u6VTiOTStyZrD2P8vYmK5vzwNmE7zPNGyPwmn8ynlLGk83SeCU1hHjnuayhHI9PrsIjTP1OP-EQDNDADuKxZhR0I45s8jIrHpt2MEiRIla5P7w09p1TxeTb1mmBCYYlqOMhxu3Fy38jfYh3g2mzHRjrYdFe2r5N3GbtDtipvdf-7QQPGOv0ZODerWVOts7qrRIc0xWFbotDP_DVct_sf8twqiqDvh96ZDlP6iAUnfwXxQbvIAdmTfWsEX9uzuJwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرونده جنایت‌ شیاطین زمان نباید مشمول مرور زمان شود
🔹
مسئولان موظف هستند عاملان این جنایت را به میز محاکمه بکشانند؛ عدالت و تقاص، تنها پاسخ معتبر به این تعدّی آشکار است.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/664910" target="_blank">📅 13:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664908">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huTQHTdOH29c43jEiTHWFSKXM3p-x1vD8HZShMQl-wdj7JWPaJNVNtAkXT-f7bXYQ6XQS07jZrSDJw5sjirmBuwdMX-x2pr3PXMBmtjKmIVqMxBGftbmOJJ3JZG7Bvv2Ikpn5hB0uMP1lueHLArdGQ5QD3UwUK3P0wgWzuD9ss_nrYx4bwGoWNL7bciFya7enLqPvv79rJeSvQzWufkDv58elivIL6corKJ7u3zFeYlAzugPhZNo0rNzW3mYE89NpTGSFIbXlal1XXdJq7bR2lgAiQ8qeJ5U5RaWcNzz2rpu3dwsY4n7R6YGj1bRsHodDjCGUJ03_62Rvp_lUnWLCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله‌ تظاهرکنندگان به دفتر هواپیمایی اسرائیل (ال عال) در تهران؛ ۱۳ آبان ۱۳۵۷
🔹
کاوه کاظمی/گتی ایمجز
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/664908" target="_blank">📅 13:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664907">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f984c921ab.mp4?token=scaJshaWOLjJOlfkqbav8RGuEtJ7YC8yiKtlv6h7abwGWZwZKYsCodQ0kMnWOxP3j9zQJT3kSSqULvlr-JJjl3tQNQgHpToDz9KW92M_OFt0bWETkv6e2himWI-1qeEy4xnfLghPILzFhUgaDx3gnXpodGZ_Z_g7gDNPL6SrOepJpG9AmWwf3TZhknHKtcBuquwtFGXUoDcB_CYFPz-RfILZJXm6vMWRPKU9wRpSl2c0-XS83FUStVwDImkl2wXPUiUr5mKT9VT2XU1ktlm20SIcgHGZ28I5G1aRoHYm8037rqMd7FA6fjobEwSUiwHNJH6awzIRKP2kry2EgZhF-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f984c921ab.mp4?token=scaJshaWOLjJOlfkqbav8RGuEtJ7YC8yiKtlv6h7abwGWZwZKYsCodQ0kMnWOxP3j9zQJT3kSSqULvlr-JJjl3tQNQgHpToDz9KW92M_OFt0bWETkv6e2himWI-1qeEy4xnfLghPILzFhUgaDx3gnXpodGZ_Z_g7gDNPL6SrOepJpG9AmWwf3TZhknHKtcBuquwtFGXUoDcB_CYFPz-RfILZJXm6vMWRPKU9wRpSl2c0-XS83FUStVwDImkl2wXPUiUr5mKT9VT2XU1ktlm20SIcgHGZ28I5G1aRoHYm8037rqMd7FA6fjobEwSUiwHNJH6awzIRKP2kry2EgZhF-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازداشت زن سالمند حامل پرچم فلسطین در تظاهرات برلین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/664907" target="_blank">📅 13:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664904">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDGOC1raNiRFzu3zHZ0YWTG49MZzfcQrSuhGJmBWNVHzDa383BdqrINeAxTPlinaDKh9lgcjnWEpwumBrPS0dDtj4YYtnLp5XvKbLk5RWiAmIFrY8IOz8bzHOp02txgaYybr0xqNni998S-lSZLLSn1_J_j844a-IOQhUiJY8jTb9zhmycVJEgin7QjXWOdlVvsH4o_sBjwFT_VJYztkZExnDNbcDVLJZMoDeF1HwXgc5AFz74zsX-fBYHfymR1I0qtr554rFHVEfgiEucga4p531jH__yeyosfBhsEN7M6TlyYgWvcHCgNyiFv2oSz0XKvsE8fr-ETaJvMbtusejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴ حرکت کششی ساده برای رشد قد کودکان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/664904" target="_blank">📅 13:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664903">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8b1240f7.mp4?token=Tggjb0lhV-I_Kse0VRwBKb0rwQ89L4rWnRGyDzRIswQhHOJgko89akSNP6OsD2ZuoWSomLAP6AO_pHIjCn3IelQVHLob9Z7hX3F5OhMk4tYhNHyeHgmCL3N4tdtAo-sH9o_SFDY7miBUlaqTIRcpkFfIFFISrDQJTVBqjXIAvZuA5sN6_vloIm4yKEO4m0mpsc20vlGPneNGixOswF9E_x_t0HsTpQJeWmMQV-SssUMZ0oabU_fBDunQfpOHxdQnHvhLZxA2rxyIrNrowixQMcm5AN_qKso-5o-e_AsHW9SEvWGsy3GAEPEuUOj9BfrJcjb7zneSSuuFAMarhqraHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8b1240f7.mp4?token=Tggjb0lhV-I_Kse0VRwBKb0rwQ89L4rWnRGyDzRIswQhHOJgko89akSNP6OsD2ZuoWSomLAP6AO_pHIjCn3IelQVHLob9Z7hX3F5OhMk4tYhNHyeHgmCL3N4tdtAo-sH9o_SFDY7miBUlaqTIRcpkFfIFFISrDQJTVBqjXIAvZuA5sN6_vloIm4yKEO4m0mpsc20vlGPneNGixOswF9E_x_t0HsTpQJeWmMQV-SssUMZ0oabU_fBDunQfpOHxdQnHvhLZxA2rxyIrNrowixQMcm5AN_qKso-5o-e_AsHW9SEvWGsy3GAEPEuUOj9BfrJcjb7zneSSuuFAMarhqraHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسینی، سخنگوی اتحادیه صادر کنندگان نفت، گاز و پتروشیمی: مدارس و دانشگاه‌ها در سال تحصیلی جدید، فقط یکی دو روز باید حضوری باشند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/664903" target="_blank">📅 13:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664902">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a798239640.mp4?token=jkGQOOFjw23o5IKSMHyXKg-1I38n-Zx8Jhso3qIAdTw2yp8MP6jDdVnNAtSexOPUq9Gvbf01jMKJF4nddDRi50zhD7ykoNjR0ra_ZbhzUO_ERWfJlCZXQxmmgg_oWck-_mEsn538643FdCi55-DNr_mtFWA4IFgBYPBll3t5DUy3MGwIiHU1bYSXcFDe9BkihC6Ob_0CFNcui0byRNHslluOTx-imUYVZMzTZ7gfgziiERL_MrPYR512r5iZf06EN0qZwAgxbctkphg-zpfNKQupvKqY7Y3hTnvp-36oyjzip41ISFAMZcWcjo3Vjfsk_MO2DAV0-_zcv_SdVVuBag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a798239640.mp4?token=jkGQOOFjw23o5IKSMHyXKg-1I38n-Zx8Jhso3qIAdTw2yp8MP6jDdVnNAtSexOPUq9Gvbf01jMKJF4nddDRi50zhD7ykoNjR0ra_ZbhzUO_ERWfJlCZXQxmmgg_oWck-_mEsn538643FdCi55-DNr_mtFWA4IFgBYPBll3t5DUy3MGwIiHU1bYSXcFDe9BkihC6Ob_0CFNcui0byRNHslluOTx-imUYVZMzTZ7gfgziiERL_MrPYR512r5iZf06EN0qZwAgxbctkphg-zpfNKQupvKqY7Y3hTnvp-36oyjzip41ISFAMZcWcjo3Vjfsk_MO2DAV0-_zcv_SdVVuBag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس پلیس راهور: ممکن است نیاز شود برای تخلیۀ جمعیت برخی آزادراه‌ها مثل تهران-قم یا بالعکس را یک‌طرفه کنیم
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/664902" target="_blank">📅 13:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664901">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kS7xv_47l9lkvsAHcx-hZzbewynaWzId71TQ88xJoXeFtjM07FayQKb9bVHlmGfAPSYJ2DnwrNO_Aw0Q7A5iTQ7bz5FA-9cb6aJwv21fL-UpynibNG7FpHz9lfZ_uS9Aext-ogL4a7Rs8b8ZElugna7O1mV8znNB2Y3eEfwa1VVGxccRJNDB2BT6Jjl3QH0Ce3S1tqYDyiRdSx556o_uzTXG5LGbcHIA19E5afXQA6_oQgk-FbD-3O1ZuFOpNFW5Zt69nTyYkHUzkDSDkzGdjt_o3J4vLYXehYOHZH-UngOyT36EPx17lelsLrNSC2O6dxa8wBsMrgYfWAkq6lJrew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
سوگواره بدرقه یار
▪️
از تمامی هنرمندان، عکاسان، اصحاب رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود تا با ارسال آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور در سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» شرکت نمایند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگو تایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر، مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبر فوری ارسال کنند.
▪️
به برگزیدگان هر بخش، جوایز ارزنده‌ و یادبود
#بدرقه_یار
اهدا خواهد شد.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق آیدی
@Badraghe_yar
در تمام پیام‌رسان‌ها ارسال کنید
▪️
برای کسب اطلاعات بیشتر به کانال رسمی سوگواره در تمامی پیام رسان‌ها مراجعه کنید
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/664901" target="_blank">📅 12:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664900">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/250d698f21.mp4?token=HlQFbdYmUJdsSGx3BdDNjcVldbYQW-B7MIzmSatvOAhyumK4XyWvHl2Zk-3cM4KtRniDxtXiV2aCH0WXD6ZC-tHVi94lpohJIm3v6kBCHAnqs72yOelRw5peR2hsNHPgdsNEiRp0DS01nCMzCTMJDYxOYVhFdAKi_VSAaFiBIFk1SL7mpQSt-1XRJsnbmZR3FfVfhVJMvCET5QQqditTRscmvZY99SYV1PsS578MvwXyc1fdy2h0HeQep3KH50HKLbm6645-aazx5qP_F0bMu95eeGSmpAbCVZWC9YHBKrbB6nPaSGKONqd1CFJd4mMhdQkAj7PUFN-D2o9ODLaQIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/250d698f21.mp4?token=HlQFbdYmUJdsSGx3BdDNjcVldbYQW-B7MIzmSatvOAhyumK4XyWvHl2Zk-3cM4KtRniDxtXiV2aCH0WXD6ZC-tHVi94lpohJIm3v6kBCHAnqs72yOelRw5peR2hsNHPgdsNEiRp0DS01nCMzCTMJDYxOYVhFdAKi_VSAaFiBIFk1SL7mpQSt-1XRJsnbmZR3FfVfhVJMvCET5QQqditTRscmvZY99SYV1PsS578MvwXyc1fdy2h0HeQep3KH50HKLbm6645-aazx5qP_F0bMu95eeGSmpAbCVZWC9YHBKrbB6nPaSGKONqd1CFJd4mMhdQkAj7PUFN-D2o9ODLaQIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیزنکوت، رئیس پیشین ستاد ارتش اسرائیل: نتانیاهو در انتخابات شکست می‌خورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/664900" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664899">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7265ebc810.mp4?token=Rs0vlNGwkB00Bz-r43SC6mtRFT0EdGd9xXJghqJoECK4gWk47M_pTGYtS-tgf_n0Ic3bSoWy33F7_3J1g5uQWTtRthR_BzKa8yWv-HCI9zx_jBQn9JWPl9_vXXqYhbdOgI5jRb60fQZkTpHrb4ASk9fl-tnMfQlT56-FIOM5qKKgizD3VGuqFYeP35n0D_Pljgl9BWidVKyXM4MCwS_nQilHSGym0kuVH4yVow6rQciFm7-mK69wnnCQEGnP7RUtIdX-caySxo-JU-lxWQrbb4I3_nVZvlkMBEaeYKYDOFZLlf6RErbcU8FcGsT3HEQ7YLWXNtl9g581knMQ5bwqgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7265ebc810.mp4?token=Rs0vlNGwkB00Bz-r43SC6mtRFT0EdGd9xXJghqJoECK4gWk47M_pTGYtS-tgf_n0Ic3bSoWy33F7_3J1g5uQWTtRthR_BzKa8yWv-HCI9zx_jBQn9JWPl9_vXXqYhbdOgI5jRb60fQZkTpHrb4ASk9fl-tnMfQlT56-FIOM5qKKgizD3VGuqFYeP35n0D_Pljgl9BWidVKyXM4MCwS_nQilHSGym0kuVH4yVow6rQciFm7-mK69wnnCQEGnP7RUtIdX-caySxo-JU-lxWQrbb4I3_nVZvlkMBEaeYKYDOFZLlf6RErbcU8FcGsT3HEQ7YLWXNtl9g581knMQ5bwqgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جشن صعود تیم ملی مراکش به دور بعدی رقابت‌های جام‌جهانی همراه با شعار فلسطین آزاد
🇵🇸
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/664899" target="_blank">📅 12:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664898">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqWveFj_JerTFU1I0lvemaElrHa51U7ZtKsp7CTLE84YAFi-fHazHh9PquO46e1eJNXnkgYPMIDI0pi2BekLpNlgQ-Vg5XZ_7P3rMoXSdqbwIwr6KOcX53BMhwWcqaoHckt4uxqdHMtw4IQu2hWkmxkcotwTuXmYRb-hD2iTCyBjzUJSHIYRz9cCb5Rqno4dQNjMsmz-Kini0x5rCBHb11XnqWugd3-r-FxVw2Pc7_NagHbhggzM8_tJQ-rWFR0N6a2q977fcXZ9Oc3u_6TH7gVxsz9NeECY1HwRGO5XUgsmEBkkyuLDv3q2GsYcPhbl3R6eXKGa9fBUS71GfubV6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص کل بورس در پایان معاملات امروز با جهش ۶۸ هزار واحدی به ۵ میلیون و ۱۲۸ هزار واحد رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/664898" target="_blank">📅 12:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664897">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75235e49d8.mp4?token=UJuY9CICTR1JE3lGFNKEdrbv4awLlBs-aFnGU5-vy5IViIcEBjk-Ko-8sbUXa0a_tHzCfppONjGHmrHAuz2Jixq9iLM53T63xgmZTdDvt8Wjukgp71dC8LwhLhOuI43-vCMPZxrM09ZyUSF56wdWFi4s-RxSGQNSeBlWicuGHlKtvavsaLEN0JR97WL8qIIsQLDosd4vcxe35JfzL8Pdr0Y8hugzUCv4AH3IxTjUs06zkWNFI2H7fSPDtdTRo7fOkR2NYOmFDsQKWsu2XEx2uwZbyV1nLbbyM_bQqS36pL5aWsnAZWdWp190Mv0KZvuJ_fe7DdiZKgAcGmTgytEUAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75235e49d8.mp4?token=UJuY9CICTR1JE3lGFNKEdrbv4awLlBs-aFnGU5-vy5IViIcEBjk-Ko-8sbUXa0a_tHzCfppONjGHmrHAuz2Jixq9iLM53T63xgmZTdDvt8Wjukgp71dC8LwhLhOuI43-vCMPZxrM09ZyUSF56wdWFi4s-RxSGQNSeBlWicuGHlKtvavsaLEN0JR97WL8qIIsQLDosd4vcxe35JfzL8Pdr0Y8hugzUCv4AH3IxTjUs06zkWNFI2H7fSPDtdTRo7fOkR2NYOmFDsQKWsu2XEx2uwZbyV1nLbbyM_bQqS36pL5aWsnAZWdWp190Mv0KZvuJ_fe7DdiZKgAcGmTgytEUAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نجات مادر و نوزاد پس از ۳۲ ساعت زیر آوار زلزله ونزوئلا
🔹
نیروهای امدادی ونزوئلا یک مادر و نوزادش را ۳۲ ساعت پس از گرفتار شدن زیر آوار زمین‌لرزه‌های اخیر، زنده بیرون کشیدند؛ عملیات جست‌وجو در مناطق آسیب‌دیده همچنان ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/664897" target="_blank">📅 12:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664896">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h27Z2rgRLtt-3tH_1s1FBEBF0tIVCt3TXyNHybVBlZHrLf4z6831plJsqlSABkiN-XwGB1sl32CvoeGK-L_S-a8T1ttDAsavm3iCsjc54sWWui_uGwL1hf4FXxPyFLnkYZC3DT5LLGJ_XcVMwxswxlkAOlMInVed5OdU3YIbjn__TS3dZVj0Mc64ypEPEpN24Hr3YFxFRCABjc_pV7nOT9uHZESYMQ18dK2j638BdGgKhuuli72yxlriYd8ku8gZWCQbcaDdWtnx5GSRxK0cJnzW4mn3onSAluXg_lUjPI9gHcQX5QZM6x90TgZLppNwaX3tMifqInhmqL26rinxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر امنیت داخلی آمریکا: پس از حذف ایران از جام جهانی رقصیدم
نشریه اتلتیک:
🔹
مارک‌وین مولین، وزیر امنیت داخلی ایالات متحده اعلام کرد که پس از حذف تیم ملی ایران از مرحله گروهی جام جهانی ۲۰۲۶، «رقص شادی» کرده و حتی «چند آهنگ» خوانده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/664896" target="_blank">📅 12:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664892">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WbWrFYIrnOPH1fVCrJYyRFfsiJbDs8XunOT0kIj4wYKYLUCWHvBeSFTOtHxJGvNbAhOHp_AzdDg8WN1Ur51_xxjNEX8riI2fSceWxKQP36vvZAClQlWzd78NIMCcniZX3mrv99_TaUqpQsrw7GRa0AbxV2vq7JqRSRHZu9ODwIuwNLtJajSkW1hjcOgs6-_9UWtOkdsBQEKUy5wRA9bw7u6KNkPCdBAjRAvdCEByyre3BRmgs2v8WNTIit9SH6z0_aB9u-Hk4DfYbqejwg-dgXQIp9UQXu6Ikg_oL74z-MGsUa0jv0f_Z4eA73dnQIFKstc4ilVf5Ojcla2UOQuoOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a7dQgteooT-dW6_34bYCSYRAjK03w5mEZoNsHNp_U7G0c4RAl4ZkY9WLuxproAXQg1xEYnHYmTxDQmeqLoZzXj9K23IA3yPahuwnBOlEkRC0N8lMZFvRFPLo3Lj4bm4E2P-KMPe5T_8vOwPDaKBDIU3dlL9UHgcfviqGBdjfLvd1ua3svWaDZDfXLzI6jdGC5HbnkZDgkd867smau5e7mbtboja4OhEefq2SnxbGRy7SE3naj1Hs79Fd3v1vk6PQJICJXBFzkkYmRIehgI5hAka8V6xvezz8pJ3b6Ymxo4IYLbhgU3aZ7byYQia07dzA0aT8IFxZJ0VNI4uBsAO9Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qdxA5NVreAFqN_6Cbgv818xu8XrhGLAFVQVgg1shOPbrsnXlE6U8v3Ir51b_OHqtxmXYwBHeEnVvHCkCfGiqM5YhuL0GGREOx0CUiVfPhVsG7qfNnJJisxqsUCaS7pAb7JXlfp-gFVm8shBtQBNu82K-IAZ14tN1J71tPsLbONFoLBd_fAEfHYzQCaskDHknFN3UGVRVBMpoO87cN18nLkU0NHJ7tbY8vxxq6aW0w22KGaCutXq5W7OwFkUXIGX29yeBHflB-GpWARSRmxww7i5uWhHVJW2NUjn2ftYQpWzL29RMQ52KikHjKPI5XhvgKHi4YWL8lvUKIAvm7pgUhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VudF7RjjcXjolpSADw-BLU1Maa5yQ1M4L1rWp-OKqBqB5uptD-RyeokGfs94u7FdBO5c5xw36zWVqr_JbFRFiRjv-JWOcVjabzu0GX9qWwDo8dGkMfsE1t5LoOHVWi0BsBeaCPG0qn95U52H0aAFCK7x9e0XmCnl_RtWgdigeQQhD6xEBPrMP2hqxiUCVnWZq0pZhQ9hMTQYky23v3j2__dylGUJTbNLHK3Wwbe4u3O1aRnNAaVADB_7OzNAkesGHf1mNcTLNAa_OCDeubZ1gN6F1hBxeM5FJJlvNtEQIJy0XZ5T4STFIkPRqtTdpNqbCQAA4WJtNxm9N3TyiOBrGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رازِ میزهای مجلسی؛ ۱۲ ترکیب جادویی سریع و خوشمزه با نان لواش
😋
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/664892" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664891">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTA60Ffh_J-EKxVzfd2dWk4T6I93aEgtxndqHhMf0_HOmyY1QQPiFw4PxWhQ8P0aO0cGRoT6P0CHU22q0PAIXF4iXwKn6D13zo0neEC63Y1Gh7Re4_9yZZHM05PklAbliX8_DwFiFC8lGuQO7dm2YykWlJSJtGzmAI0Q1WAiw-j7jJGueWQJfP1ts2ELV0GolNYPQCGqXF8ENVBo6D5gixPP8ehUP8OfYB_8nOXBBpbDZG20JcBZ-GRXDSlQpuqeXLVWLhtBd1THrQysHudrDZeqgGm7Mz-w-DScati_n5DQgAWKIlcVX61m_CM3UFIcPzQXiyugCr3L79J0tzAYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
تداوم حمایت بانک تجارت از خانواده‌های ایران
🙏
💍
پرداخت 4.8 همت در  قالب19 هزار و 345 فقره تسهیلات ازدواج و فرزندآوری توسط بانک تجارت در بهار 1405
🔗
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/664891" target="_blank">📅 12:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664890">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9381c0dfa0.mp4?token=fy8pNwWNnrxop0xVUY5q2_CK7si2WA_8FgPmwSorVJjyJIm4E9_IIvLgVbuGY8m0dJHoQJ11zWpCymUmTTUKb8Xx5xUWRuF8CDa0Xu2NLYSyny1ctTzot3ZJNSmMhtnBz2CCdPCnOM6x2pyN_vtscjzNLLQit0bcNX0m1fyeAwy23HSK7asPgoDP1060uyyGiMYBopzZnDcZ3nUZl5ayr8N-M9B78Pcv8dbPt5b7_s1KARH6-SVCqJWSKtho6Ua2iBfdCizKHWyYN5vYwOOeDcktxjUYUovpYgLh_F3f0q_k9KK2qTZOCvuzG6CafCpxe5_xluRSIBytxTZFudxZnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9381c0dfa0.mp4?token=fy8pNwWNnrxop0xVUY5q2_CK7si2WA_8FgPmwSorVJjyJIm4E9_IIvLgVbuGY8m0dJHoQJ11zWpCymUmTTUKb8Xx5xUWRuF8CDa0Xu2NLYSyny1ctTzot3ZJNSmMhtnBz2CCdPCnOM6x2pyN_vtscjzNLLQit0bcNX0m1fyeAwy23HSK7asPgoDP1060uyyGiMYBopzZnDcZ3nUZl5ayr8N-M9B78Pcv8dbPt5b7_s1KARH6-SVCqJWSKtho6Ua2iBfdCizKHWyYN5vYwOOeDcktxjUYUovpYgLh_F3f0q_k9KK2qTZOCvuzG6CafCpxe5_xluRSIBytxTZFudxZnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روبیو: تفاهم‌نامه با ایران فقط یک تکه کاغذ است
مارکو روبیو، وزیر خارجه آمریکا، در اظهاراتی افشاشده توسط یکی از نمایندگان کنگره:
🔹
تفاهم‌نامه جدید با ایران را فاقد محتوای اجرایی است و این سند تنها توافقی بر سر «ادامه صحبت درباره صحبت کردن» است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/664890" target="_blank">📅 12:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664889">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
امین زندگانی، بازیگر: جلوی لوکیشن، ۳ بار موشک خورد، اما به عوامل می‌‎گفتم کار در این شرایط ادای دین‏ ما است و نباید تعطیل کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/664889" target="_blank">📅 12:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664888">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZnYTkTM6SWGR1FKieQ7R4Ysv7cvEOWUSsjjJWDqVbMR_gDMkWjE5r1KelBnKqcMMVxdTMIxWORMLOO7QTfXJK6zCnFAnDxVpozfm2nNYWjqcY-HkQzfen2TVfgE6wcuPl4-_BD-gLEAfA-uLUH6UPTg5BwJX7hjUphFr3SglmSj4L4wJlT6YSp2A1XHOAAtbBEsZ-offP7ujZy2xbvkPz8W6v4J34NR3PEsOKHiPAmUkKo-FOA_L8Q4h_qj37l-eFtcZyMStvIZDvOm-b2Y_dzmo0E-UYI-KUJ5iwDMQ3Ku8Cb-B6Sk6GdqiyGFwFLqadYIYx9maoVaE1n074YrZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انهدام تیم تروریستی در مرزهای شمال‌غرب
🔹
قرارگاه حمزه سیدالشهدا(ع) از انهدام یک تیم ۶ نفره از عناصر گروهک‌های معاند در ارتفاعات میان مهاباد و پیرانشهر خبر داد؛ در این عملیات چهار جسد به‌همراه سلاح و تجهیزات کشف شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/664888" target="_blank">📅 12:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664887">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
دبیر ستاد ملی مراسم وداع و تشییع رهبر شهید: چهاردهم تیرماه برنامه نماز بر پیکر مطهر رهبر شهید انقلاب اسلامی و خانواده گرانقدر ایشان در مصلای حضرت امام خمینی(ره) در شهر تهران برگزار خواهد شد
🔹
مراسم اقامه نماز بر پیکر رهبر شهید در قم ۱۶ تیر برگزار می‌شود/…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/664887" target="_blank">📅 12:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664885">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdpMP9YD9CxIJ2EkAZSLpkV3_YNvYotNn7VTIAnlk2PcKs_IAtdff7kWCyMuFYQ8-jURjEXk5rQvz4j1LOccPYjaN0osJ769Q_fyFaNtzoygJvBXP6EzUZcdRLRjpIUbGkz6IXRz7bt9eWSpmtLPqL7RhrLcGythZTBXmmD4HjMH-4mQF14ZaLIKe4hy3wqBfRipkcc6pQF5UzhikKNPAMdWnan67HhFLcf0rGmtfPv74ocglJCrCR6iMkhIfG0wnl7bhF56LR3ISa3aKYtgZ8Pt0cCt1t1zmyWXtOJjPkDRS_SRI8KshsHLQrYVcRyTK6vsH9cJ_QCQ7uFaVtEjcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برزیل؛ همچنان گلزن‌ترین تیم تاریخ جام جهانی
🔹
تیم ملی برزیل با ثبت ۹ گل در جام جهانی ۲۰۲۶، جایگاه خود را به‌عنوان گلزن‌ترین تیم تاریخ جام‌های جهانی حفظ کرده است.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/664885" target="_blank">📅 12:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664884">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9a84eb55.mp4?token=lkAPjfI-Imt8r9fKZpTnWbSiLa-8VG96nFyB9wb-QQwXkYhvrNTyCSjNK02wKvk76hoAApFfAdJEI5TIsCrGRy9X4ma1lkGDhG6rs96XhgNXtmM4VSfJEHAIzesmeoOkpa5iCqZccA15tm2owvrk2nMFnlF5vnnjLoJjWuiwfqnYRaH_L-bIcUarhozBseUH-dMF0B07jo68rwwT6109wIU6QpkWDjoJ1vZX_deocSmCxeyWjwqDx7ap9GqX8ORj7WRTsaSWzRy4I-kB5TtRQ9qPPykfH3a236NZb3yGs-tPGWkqNCaTj1wNkD__mT7NrP55RT6_mK7QGnfX_yokHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9a84eb55.mp4?token=lkAPjfI-Imt8r9fKZpTnWbSiLa-8VG96nFyB9wb-QQwXkYhvrNTyCSjNK02wKvk76hoAApFfAdJEI5TIsCrGRy9X4ma1lkGDhG6rs96XhgNXtmM4VSfJEHAIzesmeoOkpa5iCqZccA15tm2owvrk2nMFnlF5vnnjLoJjWuiwfqnYRaH_L-bIcUarhozBseUH-dMF0B07jo68rwwT6109wIU6QpkWDjoJ1vZX_deocSmCxeyWjwqDx7ap9GqX8ORj7WRTsaSWzRy4I-kB5TtRQ9qPPykfH3a236NZb3yGs-tPGWkqNCaTj1wNkD__mT7NrP55RT6_mK7QGnfX_yokHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر ستاد مراسمات بدرقه و تشییع رهبر شهید: برنامه تشییع در استان‌های تهران، قم، خراسان رضوی و کشور عراق اجرا می‌شود #بدرقه‌‌_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/664884" target="_blank">📅 12:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664879">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P6XyIQgSSNdFIfXIeGkNpbXNqAb0Pp1nKUh6FMF8SpIscPtyY_1tiSKmyJy5spW_0A4Z47pMzsfk4KeikD_ZpQjIzPkxKhkHGsCYusGlhksGcq8VUSji4Sb_o-yjwaPbJecEMHj1SljEEtmju0-hPJvomnz4vZ9FoJWjIqZy5O2spvW4grz_UbAQacUQtKguyAqga3kvc_5xFUD8URE6vTqJdQQiArCbjFY_Qql5gom50IxAXukHlbWS5M3KEaFC7pSxI4NyhfB8Hg1JR8K7w7dO8sAWKTkSoXTQjjlqSLVt1vlZ1c-XnS3Spoept2hWZrsihdET5mlvhAem6KcZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ct1oiBIjGSsKo8pk1KBYEJqT8FsS1WR_hZ_IDyEJ0M16PYFrEu2zflw2fFxVfS8IijENHL_OlRVWXltzuat0g9OBeE0LQFXAM0XQOpVceY0w-OLVdLl_im2oWiUghNlxM2_umAXjp3jUlCDt7RFFOfTNDtEZ8vjFnbVCTWM6xxS3kql9k7jkekNws5TsVn3m15vODdZbkm677y5RBTS_EiiWCOJLPgiKyvqUHWdhZcdIWJXxBvmd_OQQwKCrM6WmNv0OTDDJRLxbkTRLP1jPmbOUhfpWBL6ST3qHnTtzv8RtepWqjHjylXH_qtsXY_LYPOv5HObGJ0oMPZsk2VZpuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qZ0am5xArNQhn3VbNFeVKU-UGbj24atO5EoOHoT4QmNr6-yn3yysasDN8wp1q381KWo0GUKP0_lfcQkFiQ9si4mT15fAgomWv4cMBCwFsAaNfTlDnHUil3ajesgSXhL5T8aahhOD3Cu_vgqRYuA7sbr1dqeJ3yFBHQAlldmVYCGUB62iu_At0I9eHaaJ7X5wz1mwbu9Z7jaibf36RLjFGITk4fsilQzHDSJ7Y_ooGGWM3v0yZPsiq2QXwvWtRfHD1ZKc5Cp49p2yj8cbAdHkGKm1-SD-K8rSa9u2k9kGQvf0SCNqquqno4ShkkAS6hHtj6VGIMcH8EOc19i5T64nzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/crh7nvyWh21kX2BOu-6M_Eux3nnFJFu9cu-kJTKm-m9Wp2ur3sSt0VHwD3HB7r35dXMtK7S77nXNz4oauOXzXX4yOEmaZ4J55twJaEY5vPIGt3lGohi5hQ4tl2H90mPhpHrWzRouwDkW6gh1d8AEAIjhhUkON7nQ-YYQglKI5PHK4mtFKB8wPqVl3Q5tW-liVE2LWxtJ1jb8Qm4IbIDIre4f6LxYGKKsu7H50Dl71gm45aMfT_wjnh6HoihgiCR4A5HmFhUH4Z9-iAI24wjvwa-jQ0tErMtuJlc1Gt7cv2_xnImba70n3SlbLZcYXj7MW5-B_69DVVGt_rQXG07Opw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c4804f04f.mp4?token=QQ495zn9PXEEp6qVIu-d9Te8ZNIoy_OWGkp0k6QV1uLiyaro2wy2gjW9FCrZqmzhOmc3A7wy7_ismpMzTRw7WXrQ3JY57lGFm3GW6TAbasN0x0790vcAmahDgpUVBRyuGOYXFrv5YRngzbwDOwhht_sHxjxyu55yO2vpqJaw2yGeahzmRSJSpUlON1OJ4QyeJx69W-4_0enMGi_XI_RIyDjKdTZ1mGIxCykRecatF51duxL7cFdFJg2w9Fkb76n0HUDqfVE-yAJLMi1auAuA28e8C5O7c0Z0g6g8FSx17__mzRYNrn5c0YqavQgKhlJz0jgxbd2AB8VsK10zJaNdpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c4804f04f.mp4?token=QQ495zn9PXEEp6qVIu-d9Te8ZNIoy_OWGkp0k6QV1uLiyaro2wy2gjW9FCrZqmzhOmc3A7wy7_ismpMzTRw7WXrQ3JY57lGFm3GW6TAbasN0x0790vcAmahDgpUVBRyuGOYXFrv5YRngzbwDOwhht_sHxjxyu55yO2vpqJaw2yGeahzmRSJSpUlON1OJ4QyeJx69W-4_0enMGi_XI_RIyDjKdTZ1mGIxCykRecatF51duxL7cFdFJg2w9Fkb76n0HUDqfVE-yAJLMi1auAuA28e8C5O7c0Z0g6g8FSx17__mzRYNrn5c0YqavQgKhlJz0jgxbd2AB8VsK10zJaNdpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شورش در زندان کارولینای شمالی
🔹
شورش حدود ۸۰ زندانی در بازداشتگاه «برتی-مارتین» کارولینای شمالی که منجر به گروگان‌گیری دو نگهبان شده بود، با ورود نیروهای امنیتی و اف‌بی‌آی و انجام مذاکره، ساعاتی بعد با آزادی گروگان‌ها و برقراری دوباره امنیت پایان یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/664879" target="_blank">📅 11:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664878">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
اولین شگفتی جام در دور حذفی/ پاراگوئه، آلمانی‌ها را به خانه فرستاد
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/664878" target="_blank">📅 11:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664877">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b1531e58b.mp4?token=pyxOGeV1_J-hLz-a5YBVy5fon-q2x4dQ7wDfSDOzMtQltjfEGxL9nxA60RtjNz3qn52Jk7DAAcuqTeeaCYM7to4lQouEKjb_ZPxDoRZP3rTVP1SLfLJg-P9rdmkXEiZmHsyrr6yqSY5ytBYWDMFQFafECWarpUXMtc8V53y3XsZROmEiP6AFeYh7u_JYENDnXjC3DS6CZHSPbukDqX3UMlGA0d7Pa4ba845_Ky8CHV8yoPgnJEtkUG5SiOJcmaI3VrB57r53xu6zhKfyN5MchgRAWAjhsyXEYKPfzecS07O8dx5B6lgf5VQhAN6x8G7ci3rdX9Oah0vLqwMtoaD9og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b1531e58b.mp4?token=pyxOGeV1_J-hLz-a5YBVy5fon-q2x4dQ7wDfSDOzMtQltjfEGxL9nxA60RtjNz3qn52Jk7DAAcuqTeeaCYM7to4lQouEKjb_ZPxDoRZP3rTVP1SLfLJg-P9rdmkXEiZmHsyrr6yqSY5ytBYWDMFQFafECWarpUXMtc8V53y3XsZROmEiP6AFeYh7u_JYENDnXjC3DS6CZHSPbukDqX3UMlGA0d7Pa4ba845_Ky8CHV8yoPgnJEtkUG5SiOJcmaI3VrB57r53xu6zhKfyN5MchgRAWAjhsyXEYKPfzecS07O8dx5B6lgf5VQhAN6x8G7ci3rdX9Oah0vLqwMtoaD9og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو پربازدید از تست ترشی توسط پیرزن خراسانی
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/664877" target="_blank">📅 11:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664876">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPX2bK-y3Ykv-uc9MdjP-zbBamBAI_3JB4hieoBrBoDx0bXBCuwvEbyCH2GfVO2ti24kdNJsHnoSNEQiUSiTQkH7GI1uOZ6HNLGvjU1RWzDwXKvpVAjj_9XuJ3PI1aqn7EQmIrl0DO6g2iylywuYgxqhb-Siy9FplhQzS_fXS4Qe-Ja655P-D_Vh0ejoXheT7yQif1HdC6ikBk4NViCMQRI9Xb3642P_UY2BL8MMcKwfTaQZn46Q6hww8ALB3emzOGlfbXplz1r27bEMyF5TrpOZA4mx-VnY8wb6iyv1cEWhktO2DJO-O0xL1ppzgtNE8J0TOCjJr-MQaKxXL7wKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی برق می‌رود، دخل مغازه هم خاموش می‌شود
🔹
قطعی برق فقط خاموش شدن چراغ‌ها نیست؛ برای بسیاری از مغازه‌های کوچک، یعنی توقف فروش، اختلال در کار و خسارت روزانه #برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/664876" target="_blank">📅 11:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664873">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DedkrrO7hhqBLju9up9270X_yXGkiNI2nSd4MqJF6ioNJ_nNvU2hZybezWpUDqXfgQJsSXOhYwzM9wj5R8Q3P2KJXMJV6DzhIMIIy4ZBsYEzorDB0OZCJadRCS6NvFOpUpuPVS7kD496V-WUWUE9udHTmcvoCFcRWqGwdwGmY2ChnXGlN2WD98FwF49TuGTHBYiZcwo1umTVT3JeY_1r3vGo8uo9oUYJsQfjyRG9R9kDSsbozOjTlQDfGLWzVX06tyE4IlaoX_WN05sb_hKXZSebjxmBpYDCly8qWqs7IncYv1GqWowdOBbOqU336Ml2sRvFVYvPTXhsUlVWuFDUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهی یک بدرقه تاریخی؛ تجربه‌ای شبیه پیاده‌روی اربعین...
🇮🇷
🔹
اگر قصد شرکت در مراسم تشییع رهبر شهید را دارید، پیاده‌روی طولانی، گرمای هوا و ازدحام جمعیت را در نظر بگیرید و با آمادگی کامل راهی این مراسم شوید.
🕊
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/664873" target="_blank">📅 11:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664871">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_qIJhtL1niLoejC7M3xwnNZpecWmBFkgYZy5v4qI_xqHwQo4DfRxQFNS1d054kVpnYeGKVq6xC-fko7lTo9atAK602rPf1YPeKa0IR4QAEXhEX-ggzoH54-rTw0OIUjwQ_BTIrnotMVZ7IpZxzOJGRA_Mmx3P8gV9MJuwVSkw1IBEc4uTR7YVdokq-wdC9aSgS018CPPnQyMVX34wvkhIHPgR9jVrZJDTegxQrd_1n50_OqgFZ9nX-E-ERv8BPe8yZUT2ZfwZSc09SqcpEhwehrMM16lFR9Z73gekqdxkNrkOiCH8eRMuljsR9ZTHeK-w2UEI0YyKBGu9XJRBpezw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرزاد جمشیدی درگذشت
🔹
او صبح امروز بر اثر سکته قلبی درگذشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/664871" target="_blank">📅 11:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664870">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c592c0d3d4.mp4?token=n-Kh6hXsU6zGmNW8IHxsLSS9mo8UK2g3G_g5vlqSvQYw6N6WD-haDDTarILFHFYkyYiiBFs9eiPCl9GyWFmbUjNVgWHkXJAZzPKc8Zl9wJJXSSRw58Li4x4gr3fuvPgQ-yDm7ImnONUnYj86fNfXZCZhxiy3tBVf7Iv7d6y3p9bXoL3RDNl_GHh_5rOtPJs2RNE93E8p4iQO0lfVE8xlODUypPqW0pAX_sl0slTV9QApLQLD-mrvTORfcDb7Jin5C31pUD1HKahXuMS1auziy-gA6LoWNF2s3FezU6SeC5rl8arSBz2yS-QjTLv2sIXa6JnJuNh69fGQtXTn52whxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c592c0d3d4.mp4?token=n-Kh6hXsU6zGmNW8IHxsLSS9mo8UK2g3G_g5vlqSvQYw6N6WD-haDDTarILFHFYkyYiiBFs9eiPCl9GyWFmbUjNVgWHkXJAZzPKc8Zl9wJJXSSRw58Li4x4gr3fuvPgQ-yDm7ImnONUnYj86fNfXZCZhxiy3tBVf7Iv7d6y3p9bXoL3RDNl_GHh_5rOtPJs2RNE93E8p4iQO0lfVE8xlODUypPqW0pAX_sl0slTV9QApLQLD-mrvTORfcDb7Jin5C31pUD1HKahXuMS1auziy-gA6LoWNF2s3FezU6SeC5rl8arSBz2yS-QjTLv2sIXa6JnJuNh69fGQtXTn52whxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درب کارخانه‌های خودروسازی را ببندیم و کارمندانش را در هتل پنج ستاره اسکان دهیم، خرجش از این مبلغ زیان سالانه کشتارجاده‌ای، آلودگی محیط زیست کمتر می‌شود؛ مردم هم راضی‌ترند
/ مدار
گفتگوی کامل را در آپارات ببینید
👇
https://www.aparat.com/v/jmrz2dg
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/664870" target="_blank">📅 11:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664869">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vbg315yeLkVrBy8nmQqoGCcXF8bDLjs-erWiAhb1nu27myvR9Usl7Paj9YYIz5W831t1KiZjAmPSa-tci0VKgoyyHtXl81F_mtC-f7RFgAA_The7Do8TGdAiKS7qf_AoctArNEfg3xf1P84kgGexGt8bBIKtc6SzI0sPUkcWp4r0JuZm50UmoOpVEnBEf9XaA5pnp6eFb3hTzIiKIlpe5czddf7ROC-khTNi14a8Pol1eQtwRN6zfZKnQBIAmzSDMXSlDU5cJJvRepQNafpJngfESomEz3RAeGPCth7a08oLlRmRAElWq28DwHoknYBaROyXINupjbRhiKBCEPFvqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه مترو و بی ار تی برای روزهای وداع با رهبر شهید انقلاب
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/664869" target="_blank">📅 11:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664868">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1be5d8473.mp4?token=uGG6xWxnAnwUYPCxbyZaK1PRxfYS774WMcoqODaoC3lRAOkQYXe0b-sXMB_NXkfNKTw8QiZTNLhPPprGIUxtcVrNNLBPunIgU7tlmPMeNUVQBNFWTvR198pKzlCkjErs0-FVBxdJPXNSd-sIAqchSkkT8kqrWB-tRYq42FC6vxOYVmXAL9hmsxIkTb3pMz3SqjmoHd8DcXPuqzNGFvc2Z0suRiIgO6Y0AgxFgbffBYPqyVQRaKcUV8g0WICB3dPuiHtOi5PiCr3dPy-s9HRFbd1wMSqMwc52pFIpaIrN7y087MuHwWaDiajiJ3bN6zhBk3xER88YSeAXH0aR7yRs4D6jScEur7dggcn3rOxthf08ZPFuWWD0W2DIIoeA4KjsRLSpHbsfLoYJy7ivLafbqJNaxF-47thwXU4p92oRK69lMEyRsq36nk0WRfGLWeKIu3F1Er3ZfNAWt1Wrsy9JOT5ZWJ7G7jvDw6jrncA0QsBAvXxT3qfUkHPDBo8xELO3dS0QJexEYLzovVikUP4xBnKGO5Yr5tFe-MwgaopmHrbQVmNRteaC_nQojINOOB8rFfvyKjnDgxMMrE3ET7DylE1QF-hNDbAv5K48SBElCU847uHUtZMSxzceWGgafcohbdCvVmJkZgtao1NDmxtm7B2763to5NMWfgEqPHRf7LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1be5d8473.mp4?token=uGG6xWxnAnwUYPCxbyZaK1PRxfYS774WMcoqODaoC3lRAOkQYXe0b-sXMB_NXkfNKTw8QiZTNLhPPprGIUxtcVrNNLBPunIgU7tlmPMeNUVQBNFWTvR198pKzlCkjErs0-FVBxdJPXNSd-sIAqchSkkT8kqrWB-tRYq42FC6vxOYVmXAL9hmsxIkTb3pMz3SqjmoHd8DcXPuqzNGFvc2Z0suRiIgO6Y0AgxFgbffBYPqyVQRaKcUV8g0WICB3dPuiHtOi5PiCr3dPy-s9HRFbd1wMSqMwc52pFIpaIrN7y087MuHwWaDiajiJ3bN6zhBk3xER88YSeAXH0aR7yRs4D6jScEur7dggcn3rOxthf08ZPFuWWD0W2DIIoeA4KjsRLSpHbsfLoYJy7ivLafbqJNaxF-47thwXU4p92oRK69lMEyRsq36nk0WRfGLWeKIu3F1Er3ZfNAWt1Wrsy9JOT5ZWJ7G7jvDw6jrncA0QsBAvXxT3qfUkHPDBo8xELO3dS0QJexEYLzovVikUP4xBnKGO5Yr5tFe-MwgaopmHrbQVmNRteaC_nQojINOOB8rFfvyKjnDgxMMrE3ET7DylE1QF-hNDbAv5K48SBElCU847uHUtZMSxzceWGgafcohbdCvVmJkZgtao1NDmxtm7B2763to5NMWfgEqPHRf7LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر ستاد مراسمات بدرقه و تشییع رهبر شهید: برنامه تشییع در استان‌های تهران، قم، خراسان رضوی و کشور عراق اجرا می‌شود
#بدرقه‌‌_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/664868" target="_blank">📅 11:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664867">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
نفس سامورایی‌ها در لحظات آخر برید/ شاگردان کارلتو به سختی به یک‌هشتم رسیدند
🇯🇵
1️⃣
🏆
2️⃣
🇧🇷
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/664867" target="_blank">📅 11:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664866">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9454900b44.mp4?token=euApx-CN_KWmtjo4qoZVYOS9fGPHCAQ5_Cm_I1gj_SkOWJVPalYG005Xi0y08YPfOUqb7XKj1f78xYYRD5H4Zg1ygycw0JhWs5G0qMfom6IEMXLvO1tf1IzYXKVxBgaYfwMKLIf_DmsCcuc09R6pnuDeBSSTSI13zaQr7nyt3nt0wc_XkaKJuA_wvDAe0VUu_uOdpH-Tb4UamkqEOCpZCvY4GxQIFjnk8VTVhXUSeoG1gZsIujh5MvDY3-Efqap6cbWirO7BsE2SMTJk9tpObNWefX5hW81WXTJWCxv80apO6BmRskKBSYbsUC1HJbQqG1RJezaqkAfsc7zGWhp-GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9454900b44.mp4?token=euApx-CN_KWmtjo4qoZVYOS9fGPHCAQ5_Cm_I1gj_SkOWJVPalYG005Xi0y08YPfOUqb7XKj1f78xYYRD5H4Zg1ygycw0JhWs5G0qMfom6IEMXLvO1tf1IzYXKVxBgaYfwMKLIf_DmsCcuc09R6pnuDeBSSTSI13zaQr7nyt3nt0wc_XkaKJuA_wvDAe0VUu_uOdpH-Tb4UamkqEOCpZCvY4GxQIFjnk8VTVhXUSeoG1gZsIujh5MvDY3-Efqap6cbWirO7BsE2SMTJk9tpObNWefX5hW81WXTJWCxv80apO6BmRskKBSYbsUC1HJbQqG1RJezaqkAfsc7zGWhp-GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پروفسور گرگ سایمونز، استاد
دانشگاه و پژوهشگر سوئدی: آمریکا یک امپراتوری در حال زوال است و توان شکست دادن ایران را ندارد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/664866" target="_blank">📅 11:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664865">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/664865" target="_blank">📅 11:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664864">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDsZkiybF5I7UfkvHub0zCg9YCXIv_BCFHxyVuP-GNT2Wwd9tJ2tNNpk4XDW43UF85z4sw7t24C85Kq-myZRYEGsfI_ohyfcpo8pi2_oniZfKe-y3ZnzQNX3RS0c-qwrYfLKY4HWTDzsvfk0Inr8xB5EjduIlnzOoXKkLZEVQViKsxmpEwbRYriiXmg45TJHu4fq4LyyyvIDk7NAQD-kSHpkxu3JRGPLZPZyQ1VmuO7I2UzyzfVwvAvGhTrpj9G_PfGLdKUsmd4c4o-CimiZe0BkvQxdjtWahNgOmx1BclZicJGQyy1esITNboyfBL2cbx5GIY2jIQNbsbHJ4IRDXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعویض به‌موقع قطعات خودرو را جدی بگیرید
🔹
تعویض به‌موقع قطعات مصرفی، علاوه بر افزایش عمر خودرو و کاهش هزینه‌های تعمیرات، ایمنی رانندگی شما را نیز تضمین می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/664864" target="_blank">📅 11:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664863">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de30243299.mp4?token=AqTP4Q45ZyA_WOQl-ghohgMLpjQHIgeX5nWlr9O2cBQ1Gxrzkq4jHKeEOE1yAWxOzKwDzuT9U-UbSLi8IU7ozTbSD4zbZAncALYqIG9CVe2C4aYHuQJjh32zSJuON0EjLNi85Ym2m-nk5tLYe88volDXRD5NmB_vAzGgkmhT7p5O1EFkqoOnfJDIPOueUQrGWVLZLjreDbH0FwkK5KEv_3furKO40NjMlmdMkV3brm0oiepOqi99D36T8RLbWyeCMAmm32NcWwpKtV0NFDM8dPOtlrofFXF2OXNY9L359BoFFtynitztwBSRqOAt_FXJYAC1nyN2g7hwIklp8tzD94WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de30243299.mp4?token=AqTP4Q45ZyA_WOQl-ghohgMLpjQHIgeX5nWlr9O2cBQ1Gxrzkq4jHKeEOE1yAWxOzKwDzuT9U-UbSLi8IU7ozTbSD4zbZAncALYqIG9CVe2C4aYHuQJjh32zSJuON0EjLNi85Ym2m-nk5tLYe88volDXRD5NmB_vAzGgkmhT7p5O1EFkqoOnfJDIPOueUQrGWVLZLjreDbH0FwkK5KEv_3furKO40NjMlmdMkV3brm0oiepOqi99D36T8RLbWyeCMAmm32NcWwpKtV0NFDM8dPOtlrofFXF2OXNY9L359BoFFtynitztwBSRqOAt_FXJYAC1nyN2g7hwIklp8tzD94WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اژه‌ای: باید نگاهمان را در بعضی بخش‌های حکمرانی تغییر بدهیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/664863" target="_blank">📅 11:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664862">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5e8403a8a.mp4?token=YtCP2oBRaFPKCwv4-SQS0Nps8w7jQ2u8GBpUh1JPYRvOlzSVNM8q1zOTNCW9vFqPZdjsr8N7_fu1GKk_wcBJr-RNoJrVY5cAAvsIrWnZ_X5trPKDgRlYF0ROIHfHyIUs9NNR9Czd1i2HM5JJ3b8lMeIwZ7P8HCHAcmVkOSgRnSM_OFVYz_PglE-KW2Urf7VtEKfan9EczmV1LZtj3LWAiAjA4V4YaHGfgFDaqyu3f9POpCw5TRSsXdjBpXhUOBn5UggyTUb2jDEMhcP6F9jnUvJC3oxiRlyGa9quogw6O21RcH66UdNIZYQ8Am8vi6UrZPxniQ8crmVo2i2rwW7B4Ui6tDUmbEY3sS9mb8i_ql1GbMpgknwPhYUJ7TF0ml_NT6kTGElHApOerXdnlAwtkzx3iJDKI6u29uB4HfmJq9FoU5er8wGYdQbiTcmHfubj8kQmAEF8glCJssZsMdoU7LYyoAl8JksEL31MEztHXTpSZyii-2e9dLcNL1J1RtAmYwAfw9DqSWOdU4N-rKFLpw0Ms86jEg9sRtVszGuN9BC9GXmsfCsJqyEyY8498VM3DwT4xfKpbWza_9xbafmpCeOFMepvL1DcisJAuS_X8PtFtaIDKgDdohkhQJOPE2cBFT5cZryndAHNyiuM0TSkSizyRvssDJyI3xBN3ARLj1E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5e8403a8a.mp4?token=YtCP2oBRaFPKCwv4-SQS0Nps8w7jQ2u8GBpUh1JPYRvOlzSVNM8q1zOTNCW9vFqPZdjsr8N7_fu1GKk_wcBJr-RNoJrVY5cAAvsIrWnZ_X5trPKDgRlYF0ROIHfHyIUs9NNR9Czd1i2HM5JJ3b8lMeIwZ7P8HCHAcmVkOSgRnSM_OFVYz_PglE-KW2Urf7VtEKfan9EczmV1LZtj3LWAiAjA4V4YaHGfgFDaqyu3f9POpCw5TRSsXdjBpXhUOBn5UggyTUb2jDEMhcP6F9jnUvJC3oxiRlyGa9quogw6O21RcH66UdNIZYQ8Am8vi6UrZPxniQ8crmVo2i2rwW7B4Ui6tDUmbEY3sS9mb8i_ql1GbMpgknwPhYUJ7TF0ml_NT6kTGElHApOerXdnlAwtkzx3iJDKI6u29uB4HfmJq9FoU5er8wGYdQbiTcmHfubj8kQmAEF8glCJssZsMdoU7LYyoAl8JksEL31MEztHXTpSZyii-2e9dLcNL1J1RtAmYwAfw9DqSWOdU4N-rKFLpw0Ms86jEg9sRtVszGuN9BC9GXmsfCsJqyEyY8498VM3DwT4xfKpbWza_9xbafmpCeOFMepvL1DcisJAuS_X8PtFtaIDKgDdohkhQJOPE2cBFT5cZryndAHNyiuM0TSkSizyRvssDJyI3xBN3ARLj1E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اژه‌ای: باید نگاهمان را در بعضی بخش‌های حکمرانی تغییر بدهیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/664862" target="_blank">📅 11:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664861">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
ارجاع پروندۀ تخلف یک بانک دولتی به دیوان محاسبات
🔹
در بررسی عملکرد شرکت‌های زیرمجموعۀ یکی از بانک‌های دولتی ناتراز، مواردی از عدم رعایت صرفه و صلاح دولت در اجرای تکالیف قانونی مرتبط با مولدسازی دارایی‌های مازاد شناسایی و پرونده جهت رسیدگی به  دادسرای دیوان محاسبات کشور ارجاع شد.
🔹
بررسی‌ها نشان می‌دهد در فرآیند انتخاب کارشناس، قیمت‌گذاری و تصمیمات اتخاذ‌شده برای تهاتر دارایی‌ها، اشکالات موثری وجود داشته و در یک مورد بالغ بر ۱۰۰۰ میلیارد تومان انحراف در قیمت احصا شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/664861" target="_blank">📅 10:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664860">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzasCjLt4gSC7zlRK5IMEhrDpnDRnj4yIdaRX-b2sdev-nE5dptkTYJcGy1Q0pAv3I7QAYgmAoN1dm5CeR7FXTOJ28vOAdqn1kiB1wZ6tGe0P9PhKFO9sSK3q_07_effEc6PHcFHlOdsrV_VQj3iZeesbTl27TCx_el2pTTbzCDmDz5E_YDcrBuHSEpJOsRKptbRCB6eanfX37mBNyaaGLe7eQrvllLyOAeb8qtdDBhFpDyH_RX25UhOIUVcAyAhvUDbdEFtpuWGIFyO9rvw9btlby8C-NY4q2toJs8sgKE20EeraVBf-dR3HfBHzAw791EVsqWAd_tH6I3b1vJN0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این روزها که جنگ خبری و رسانه‌ای اوج گرفته، این ۳ کار را تمرین کنید تا فریب نخورید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/664860" target="_blank">📅 10:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664859">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316b8b1ceb.mp4?token=OIqLoL8tz69HhkHUkoOO_f5R2q73FkPBK2xPFx5lYnKCFcji8iefhLiQCFCaoE7O9LDpBd_Ezl9-chALFnzKTniYYjjebG2RCC8TSPFEG7hr4ccbKmC-h8ZfcaohZp91eCGR4-wxyHhQw2VECA6-SMi0go3kt5YUI7w2LZGaOSXsNZKhJx2POmoJHKWWD1jrjbzHtmjvdABDwxou53C8EgqYIgqVGvq3ztM6Xk7vX5u3AaCjp_fRSjTGxB8w5fNDC6xkGFc6lvsEF42Mz_iFTUAxgFv7qYUuK7iSPCrxrfTlc8bboWOsfdZfPyGvVfIMkMdPelFFwlCcU_Dp6gy4LmD3ZnPJ9Jw5UhBdgRaEl6RKo9pP40JD1qF9lHWCVzKKoX1RqbgJrJFe6Hft2pKHK1OG7Q_Z18hWLKYfvTzXMAC7fnI4BQzFoZhN9XpO2iB2kBvpTfid50QZA4SggCgfIwc65OLT-wcC_bI0c83J4fckvr6tXX1pc67mmVYGpSMC0tkdwdTiY7g851xqTCZBStIS6SbymAZILZGGNgCHUoCkKHSpQAYVXVOi5vgESV5RXD1Mau-lxhFM4-OJBWqS8ev1jFJO1edl_m0GkiGwVmjVEv4pZrWNC8KrZ4R3QwhisNFdWsH8iuHDEtS3rBImXTJ8m99jQ_hBl4dHiobuVdM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316b8b1ceb.mp4?token=OIqLoL8tz69HhkHUkoOO_f5R2q73FkPBK2xPFx5lYnKCFcji8iefhLiQCFCaoE7O9LDpBd_Ezl9-chALFnzKTniYYjjebG2RCC8TSPFEG7hr4ccbKmC-h8ZfcaohZp91eCGR4-wxyHhQw2VECA6-SMi0go3kt5YUI7w2LZGaOSXsNZKhJx2POmoJHKWWD1jrjbzHtmjvdABDwxou53C8EgqYIgqVGvq3ztM6Xk7vX5u3AaCjp_fRSjTGxB8w5fNDC6xkGFc6lvsEF42Mz_iFTUAxgFv7qYUuK7iSPCrxrfTlc8bboWOsfdZfPyGvVfIMkMdPelFFwlCcU_Dp6gy4LmD3ZnPJ9Jw5UhBdgRaEl6RKo9pP40JD1qF9lHWCVzKKoX1RqbgJrJFe6Hft2pKHK1OG7Q_Z18hWLKYfvTzXMAC7fnI4BQzFoZhN9XpO2iB2kBvpTfid50QZA4SggCgfIwc65OLT-wcC_bI0c83J4fckvr6tXX1pc67mmVYGpSMC0tkdwdTiY7g851xqTCZBStIS6SbymAZILZGGNgCHUoCkKHSpQAYVXVOi5vgESV5RXD1Mau-lxhFM4-OJBWqS8ev1jFJO1edl_m0GkiGwVmjVEv4pZrWNC8KrZ4R3QwhisNFdWsH8iuHDEtS3rBImXTJ8m99jQ_hBl4dHiobuVdM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پخش بخشی از وصیت‌نامه منتشر نشده رهبر انقلاب در سال ۴۲ برای اولین بار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/664859" target="_blank">📅 10:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664858">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srsOs3Y8W3tq0BkENjKVcnwCVmsCtrASPyEuYnQ5WgGoUhFMvEydL4I9jwYcFwCLq_saxwNXpHMVG61byIFY4h8VcrWvnJQUYRyiWYeNluUniYhPL3sO3emAjOAqhKnFIOtiHypUxhGbkeI7nijIonVMYLVtqanPCcJR9X_zssKlmcfZXgwshy6PlNotmmn-nYslSOsGhYBVEi-lF5V21NaDtR7ZtkDDFfNhbogjl0Iv-5-Cpvb97tGDNXOFNUJ3CzbXdVvIJ01SG9Sv5iQE1vS95JxOaA4GybuUzZnbUDo5rQkNG8G-BA2BdSg94AA2qvvlUcp_UxXsxi-t7THVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز عملیات طرح جامع پایانه مرزی نوردوز در آینده نزدیک؛ توسعه مبادلات تجاری و ترانزیتی ایران با همسایگان
‌
🔹
معاون وزیر راه و شهرسازی و رئیس سازمان راهداری و حمل‌ونقل جاده‌ای در جریان بازدید از پایانه مرزی نوردوز در استان آذربایجان شرقی، از آغاز عملیات اجرای طرح جامع این پایانه در راستای توسعه مبادلات تجاری و ترانزیتی با کشورهای همسایه خبر داد.
‌
🔹
رضا اکبری گفت: با تأمین اعتبار حدود ۹۰۰ میلیارد تومانی و تعیین پیمانکار و مشاور پروژه، عملیات اجرایی طرح جامع این پایانه پس از ابلاغ قرارداد و در کوتاه‌ترین زمان ممکن آغاز خواهد شد.
‌
🔹
وی به اهمیت راهبردی مرز نوردوز در توسعه مبادلات تجاری و ترانزیتی اشاره و اظهار کرد: توسعه زیرساخت‌ها، افزایش ظرفیت پذیرش و تسهیل در  تردد ناوگان حمل‌ونقل کالا و مسافر از مهمترین اهداف اجرای طرح جامع این پایانه مرزی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/664858" target="_blank">📅 10:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664857">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af34e16564.mp4?token=N2ioBhIiON2BhjU2uoa7m8zuATxMA0MI4RIAwn1N_dyze_6W7xzTDNddLAo64hTdyDzFKh8pmpYsx5sSKPmkr9KPA63LPagAl9c_qfv2WERWE_vfX22xZibzGePfNNZM-Z8CKOPGIuHVtzeYeBLhaIDUydUJIFf-8u6p0Z76NrnlGfc9BMLFT3XlJKygah1zhI-atVbrVEfA-CXof5mOkdSiV4wRyvImlJKpslXDi9pbZdN9U7c2csctWFzCvju7bScOuSqtkgqt2EQPCicVKvk0MO-z8GzWDlD9ykDFJtuvcqwngmKzcsTQyrG44zAsbRxJAdSpVJX0FwU_ZpqiEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af34e16564.mp4?token=N2ioBhIiON2BhjU2uoa7m8zuATxMA0MI4RIAwn1N_dyze_6W7xzTDNddLAo64hTdyDzFKh8pmpYsx5sSKPmkr9KPA63LPagAl9c_qfv2WERWE_vfX22xZibzGePfNNZM-Z8CKOPGIuHVtzeYeBLhaIDUydUJIFf-8u6p0Z76NrnlGfc9BMLFT3XlJKygah1zhI-atVbrVEfA-CXof5mOkdSiV4wRyvImlJKpslXDi9pbZdN9U7c2csctWFzCvju7bScOuSqtkgqt2EQPCicVKvk0MO-z8GzWDlD9ykDFJtuvcqwngmKzcsTQyrG44zAsbRxJAdSpVJX0FwU_ZpqiEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزی روزگاری نوکیا
🔹
نوکیا N95 در سپتامبر ۲۰۰۶ معرفی و در مارس ۲۰۰۷ عرضه شد. این گوشی پرچم‌دار چندرسانه‌ای نوکیا با فروش بیش از ۱۰ میلیون دستگاه یکی از موفق‌ترین گوشی‌های دوران خود بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/664857" target="_blank">📅 10:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664856">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
معاون وزیر نفت: از کارت سوخت شخصی استفاده کنید و کارت جایگاه فقط برای شرایط اضطراری مانند پایان سهمیه یا نداشتن کارت شخصی به کار گرفته شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/664856" target="_blank">📅 10:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664855">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fb57cd5f5.mp4?token=MjAAyHzd5JXn4K42-PmwPv85nYnPlwZBelADitzz_UCoibIsNEETtx_pJtPwXx-GHLi8AgqL00F1JZSsnaWxjz2R1aTHc6xWoj_fEpcLQhb53GMzIaiQOI0AR59lcznvu9LEP3FJb4lg2ef2FZ0QWt8iyqcFaFSlQieFV4L9P7ZD8kp_hFqtlMq6nccqa4sxWE_pnnUy2FRjbeCpN5XqSHUqAokQEql7vZHYi1-caRzUlMKjnsBhugIFOAJ9DJu2RbWWqMFPuIiwWYbPhSleQmW8GaE-Ee4Cexjyayox_20LTRrE431UWAwhzGvvKChe_cdOqOM-ygzCBvGvaRjYxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fb57cd5f5.mp4?token=MjAAyHzd5JXn4K42-PmwPv85nYnPlwZBelADitzz_UCoibIsNEETtx_pJtPwXx-GHLi8AgqL00F1JZSsnaWxjz2R1aTHc6xWoj_fEpcLQhb53GMzIaiQOI0AR59lcznvu9LEP3FJb4lg2ef2FZ0QWt8iyqcFaFSlQieFV4L9P7ZD8kp_hFqtlMq6nccqa4sxWE_pnnUy2FRjbeCpN5XqSHUqAokQEql7vZHYi1-caRzUlMKjnsBhugIFOAJ9DJu2RbWWqMFPuIiwWYbPhSleQmW8GaE-Ee4Cexjyayox_20LTRrE431UWAwhzGvvKChe_cdOqOM-ygzCBvGvaRjYxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در
مزرعه پسر یکی از نمایندگان زن عراق میلیون‌ها دلار که در زیر شن‌ها دفن شده بود، کشف شد. همچنین تعدادی اسب و خودرو مدل بالا نیز توقیف شده
است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/664855" target="_blank">📅 10:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664854">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
اعتراف دبیرکل ناتو به همکاری با آمریکا در جنگ علیه ایران: هزاران پرواز از اروپا به سمت ایران بلند شد/ آمریکا بدون اروپا قادر به انجام این عملیات نبود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/664854" target="_blank">📅 10:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664853">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
سرپرست وزارت دفاع: بدون تردید به نقض آتش‌بس پاسخ می‌دهیم
ابن‌الرضا در گفت‌وگوی تلفنی با وزیر دولت در امور دفاع قطر:
🔹
با اعتماد به برادرانمان، به دشمن اعتماد نداریم و دستانمان روی ماشه قرار دارد و بدون تردید، در صورت هرگونه نقض مفاد آتش‌بس، اقدام و واکنش متناسب و لازم را خواهیم داشت.
🔹
تنگۀ هرمز نباید مورد سوءاستفاده کشورهای فرامنطقه‌ای قرار گیرد. حضور نیروهای بیگانه نه‌تنها امنیت‌آفرین نیست، بلکه موجب افزایش سوءتفاهم، بی‌اعتمادی و ناامنی می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/664853" target="_blank">📅 10:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664852">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUkooBD_Hk4kBuwesi3dQaFfTY4K-ToV_7i999bgLXFO5jJdXLJ-M8tM58LCiQGNb5R5csgoC87TRlKnNkbtgf6EdnB3CwtQqe5VQgdHjZg8J7fMdVDTukECXk9o1KHH-DONqzoH-FIZdJzfv4dFstIvUl3LVjTSARihiZ9ZaOzSyF42PzKfe-P_g7GBFhB6sv0nsVLkya7NdyBtYdPcJDdvmN4oxZ87cx8Z9w58KpCsdJLV4asONUd6SG_axwDcNIxmiF4kSfQHRNOTbk6cieH1pjXw4wXqcxuNXooEBz97vsIGQd1bFP32SEx7Tv5tLcpigeNhavirJvryWjtISA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید ترامپ: هدیه‌ای طلایی به کاخ سفید به مناسبت دویست و پنجاهمین سالگرد تولدش
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/664852" target="_blank">📅 10:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664851">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پاداش استمرار خدمت فرهنگیان مربوط به سال ۱۴۰۴ به حساب مشمولان واریز شد.
🔹
نخست‌وزیر ارمنستان برای مراسم تشییع پیکر رهبر شهید به ایران می‌آید
🔹
امارات ممنوعیت سفر به لبنان را لغو کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/664851" target="_blank">📅 10:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664850">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
انهدام مهمات عمل نکرده دشمن در بندرعباس
🔹
انهدام مهمات عمل نکرده تجاوز آمریکایی - صهیونی در شهرستان بندرعباس محدوده دهستان سرخون و ایسین امروز صورت می‌گیرد.
🔹
احتمال شنیده شدن صدای انفجار، ناشی از عملیات فنی وجود دارد و جای هیچ گونه نگرانی برای شهروندان نیست.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/664850" target="_blank">📅 10:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664849">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f41fd695a5.mp4?token=hvbb5Oz23Skdj3FjHQVDUUVxJdEVKFWp96jn8mdKrP80GdQ_9EOJrOM1N5ITH10ZFDXITF7oaZFu9QRt2-bQiS0iXxX5JSY0mt2uMyrynfisRb9JeDmOg08rBoAmcLZ2SczXjTTmqKmCbo3T4G8jARKCH4WMiVh4iKAEmikOXMZaENODGqfofiQnA7oltXKe8MYwXNHzyQzRyZjeh28Wjkt0JfmqFiMgIj2a2EgpztYsw86ddlYv8UsbjwSrPZIReelgOcO4oC-EuYvKKW3P2dKZyMD2qp0Y8ZdjHhocYCYCHombjJCznSK4ALUR7N_Qq1vA1h3pVaxT9HGP15KveA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f41fd695a5.mp4?token=hvbb5Oz23Skdj3FjHQVDUUVxJdEVKFWp96jn8mdKrP80GdQ_9EOJrOM1N5ITH10ZFDXITF7oaZFu9QRt2-bQiS0iXxX5JSY0mt2uMyrynfisRb9JeDmOg08rBoAmcLZ2SczXjTTmqKmCbo3T4G8jARKCH4WMiVh4iKAEmikOXMZaENODGqfofiQnA7oltXKe8MYwXNHzyQzRyZjeh28Wjkt0JfmqFiMgIj2a2EgpztYsw86ddlYv8UsbjwSrPZIReelgOcO4oC-EuYvKKW3P2dKZyMD2qp0Y8ZdjHhocYCYCHombjJCznSK4ALUR7N_Qq1vA1h3pVaxT9HGP15KveA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول مراکش به هلند توسط دیوپ/ مراکش با حذف هلند، ‌حریف کانادا در یک‌هشتم شد
🇲🇦
1️⃣
(۳)
🏆
(۲)
1️⃣
🇳🇱
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/664849" target="_blank">📅 10:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664848">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa6f773f03.mp4?token=ksAeDuauS1Uq8WmNGDUNyzdE7ntzD-VDsp3jQnCvThSSWG0i-AS7j8H6h5HdIFjpumdT9Zn6t84vo8Q2Y0QDAiL1r2Nwv_tINk6rx4JfwHH3jcy2qNekBQsvRtP1jIEzl_A9uXx--0gQ0x8ieLaV_hxP9FWpEY4E7AVe83PWR9UhN2Vtbzp5UzjbQWaObN9PlmG8NZKi20X8caVJv-j0lJb2IfPi3MiOimWg7sZ39rkgbdGa4NIOP_xasr3v5JH-HZysjeOA65BumJyfe9Vdwime66jKpzwrBeYB5fL4sdq6BoXO8LxX6udqp-ZMP-0jcVDZ02fAn4H6vQQOr3U8Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa6f773f03.mp4?token=ksAeDuauS1Uq8WmNGDUNyzdE7ntzD-VDsp3jQnCvThSSWG0i-AS7j8H6h5HdIFjpumdT9Zn6t84vo8Q2Y0QDAiL1r2Nwv_tINk6rx4JfwHH3jcy2qNekBQsvRtP1jIEzl_A9uXx--0gQ0x8ieLaV_hxP9FWpEY4E7AVe83PWR9UhN2Vtbzp5UzjbQWaObN9PlmG8NZKi20X8caVJv-j0lJb2IfPi3MiOimWg7sZ39rkgbdGa4NIOP_xasr3v5JH-HZysjeOA65BumJyfe9Vdwime66jKpzwrBeYB5fL4sdq6BoXO8LxX6udqp-ZMP-0jcVDZ02fAn4H6vQQOr3U8Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خطاهای شناختی در یک نگاه #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/664848" target="_blank">📅 10:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664847">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kp8C97t-43EJ1sUhiU8oYHeu_P-dFUIND8ht6Phg81Tlwbj8Qki2fTxXOitQer-En0hH5OUIAlXqoKluqF4pfhahjsUq-rLIaOqwcidHrkgdJWDEqIA3rX5W1gx6tdRiKOUHTz7pIQ-EdSdMLVJdAd6rjex91EZOSD-5Kc3bj9jHjK9vZkgkRa3V54ZYogrXpf8MG5-3KYV_YN8ZUH4PC55br2NUImZVAOw75wx82qglZc36cumEkJ9uhkUDGY3Y04MRSqYXCwHXMQhk6CxrEmR7HDBrjdT4z1ty36wo1-LuAQpKXvMCwhPXEgDC3uM7N04girvhKY1qdfjb0kDENQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نامه زیبای جمعی از ایرانیان مقیم خارج از کشور به تیم ملی: اگر صدای بی‌احترامی از عده‌ای را شنیدید، لطفاً بدانید که آن صدا، صدای همه ایرانیان نبود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/664847" target="_blank">📅 10:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664846">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ایازی: برخلاف حواشی، علما با مذاکره مخالف نیستند
ایازی، دبیر مجمع محققین و مدرسین حوزه علمیه قم:
🔹
برخلاف فضاسازی‌هایی که گاه در برخی رسانه‌ها و تریبون‌ها دیده می‌شود، بخش قابل توجهی از علما، روحانیان و اندیشمندان با اصل مذاکره و تعامل سازنده با جهان مخالفتی ندارند و آن را راهکاری عقلایی برای کاهش فشارها و حفظ مصالح کشور می‌دانند.
🔹
آنچه گاه به عنوان مخالفت عمومی مطرح می‌شود، بیشتر صدای گروهی پرهیاهو است که به دلیل برخورداری از امکانات رسانه‌ای، صدای بلندتری دارند؛ اما این صدا، الزاما بازتاب‌دهنده دیدگاه اکثریت نخبگان و روحانیت نیست.
🔹
مهم‌ترین سرمایه هر حکومت، اعتماد عمومی است و این سرمایه جز با احترام به کرامت مردم، شنیدن صدای آنان و مشارکت دادن همه جریان‌های دلسوز کشور بازسازی نمی‌شود./ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/664846" target="_blank">📅 10:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664845">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a72040862.mp4?token=VjkCF_rC__24MYQQYeHsgP9QrBcfOXQld5RF1tuddc0iDkoy2sWriGPJkRkTqMkWQj9urjy0vrknN5vm3Bd8_mrrm94UqnC9aZSrENToEFrFSxBo04ry6A3YiBeL3vqAZaJw-ycdETEwJVh4A2iGNFa-ErH17jnmbrv10TrXAdxNIE-T7wcN5U9xiPO0LMS9SNIGiqNx89Em1WCxXZ1uM_ILEr-qrKan1EkKANP5IIIWn4NrxGeOA0gDAZ49ROBQGupunzukfWkTiTD0KIeDDgk2Sn3Ppk5WShU5m2BvHVZycX1GQaWs9Tf64e6II7b97KKApSRjcHaXqPx5v7q4MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a72040862.mp4?token=VjkCF_rC__24MYQQYeHsgP9QrBcfOXQld5RF1tuddc0iDkoy2sWriGPJkRkTqMkWQj9urjy0vrknN5vm3Bd8_mrrm94UqnC9aZSrENToEFrFSxBo04ry6A3YiBeL3vqAZaJw-ycdETEwJVh4A2iGNFa-ErH17jnmbrv10TrXAdxNIE-T7wcN5U9xiPO0LMS9SNIGiqNx89Em1WCxXZ1uM_ILEr-qrKan1EkKANP5IIIWn4NrxGeOA0gDAZ49ROBQGupunzukfWkTiTD0KIeDDgk2Sn3Ppk5WShU5m2BvHVZycX1GQaWs9Tf64e6II7b97KKApSRjcHaXqPx5v7q4MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول هلند به مراکش توسط خاکپو
🇲🇦
0️⃣
🏆
1️⃣
🇳🇱
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/664845" target="_blank">📅 10:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664843">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
پزشکیان: توافق اخیر در هماهنگی کامل با رهبر انقلاب و حمایت شعام به‌ دست آمده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/664843" target="_blank">📅 10:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664842">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1970246926.mp4?token=hgI48mwr3Dj3PznGoDkWQlPGNpg6fnMWYkvMfLmZr_4yKdiVEGkK93rQWIbsL2ufpnKqleQiEWLU7QVzv5MTTic0ophwzm-zwtzz1Em7adsk_PUSbE_whG-jjGcg3eltxUOvtz0x8ulZgv2dzFTzQGHwYFnQN_M16j6FgnZANv7xZopzxX2A97jbN7Mq4b7KHAkS16FfLpf5i-8R9GUpSaR3udQ2i66MdUgw6-hJsJbqDPGugnsA7hLGBnW5jzVFCozJGfyRQP7tnyO18-IRUfRbvyDjmFzUL_934CsALmhdsnFz6bJxLghTK7ii2Tw8CaIBJX3_AXQK3d7M5O66vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1970246926.mp4?token=hgI48mwr3Dj3PznGoDkWQlPGNpg6fnMWYkvMfLmZr_4yKdiVEGkK93rQWIbsL2ufpnKqleQiEWLU7QVzv5MTTic0ophwzm-zwtzz1Em7adsk_PUSbE_whG-jjGcg3eltxUOvtz0x8ulZgv2dzFTzQGHwYFnQN_M16j6FgnZANv7xZopzxX2A97jbN7Mq4b7KHAkS16FfLpf5i-8R9GUpSaR3udQ2i66MdUgw6-hJsJbqDPGugnsA7hLGBnW5jzVFCozJGfyRQP7tnyO18-IRUfRbvyDjmFzUL_934CsALmhdsnFz6bJxLghTK7ii2Tw8CaIBJX3_AXQK3d7M5O66vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شادی راهبه‎‌های برزیلی هنگام بازی این تیم و گل سلسائو
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/664842" target="_blank">📅 10:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664841">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سرقت اطلاعات آیفون ۱۸ پرو مکس از یک شرکت هندی
🔹
اطلاعات محرمانه مربوط به گوشی آیفون ۱۸ پرو مکس از یکی از شرکای تجاری اپل در هند به سرقت رفته است.
🔹
رویترز گزارش می‌دهد که اپل به‌ شدت نگران نشت این داده‌هاست، زیرا جزئیات فنی محصولی که هنوز سال‌ها تا عرضه فاصله دارد، در دسترس افراد غیرمجاز قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/664841" target="_blank">📅 09:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664840">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQhxL0jvEAU_C8Kbz9KZUeN8BSt34fizKlMytMllLh7-ef_PEQiy4_SWonUHcwcfFeeiDJybWX7N1Q7s7Tg6rKsXfLeJEDI04-AgD_lvgiIGV9y4zfcB_YRG-emYAY2pKGG0S8hHMgrf9MpPr2QU63HaXkkgAUtWE5Dbij7alfNmYtJsF-yDjrJ4-CG8RC5EmE5bxFuRuiosEeGHUW2ZhXPhgiFvd-oemiZQ4Nfu2RyDvMJyE_U3XnFQtu99bRv-VQokr7NhOT4ermi0t8s1Rq8193uXR5eeQace6UHFA43kX5mLLUC-GRYEc1CMVoc_e5cVkyKFgpe57ODw9G5_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار تند ایران به فرانسه و مکرون؛ دخالت بی‌جا نکن!
آناتولی:
🔹
ایران با رد پیشنهاد مکرون برای همکاری در مین‌روبی تنگه هرمز، به فرانسه هشدار داد که هرگونه دخالت یا سازوکار موازی در این آبراه راهبردی را تحمل نخواهد کرد. عملیات مین‌روبی در تنگه هرمز تنها در چارچوب تفاهمات موجود و توسط ایران انجام می‌شود.
🔹
تهران از پاریس خواست از تحرکات بی‌جا خودداری کند چرا که این اقدامات می‌تواند وضعیت حساس منطقه را پیچیده‌تر کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/664840" target="_blank">📅 09:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664839">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
کیهان: این روز‌ها طرفداران «یک شخصیت سیاسی» برای اثبات نگاه خود در‌باره اینکه رهبر انقلاب گفتند «بنده علی‌الاصول نظر دیگری داشتم»، با بدترین شکل مسئولین نظام را مورد انتقاد قرار می‌دهند
🔹
رهبر شهید می‌گفتند «نقد کردن با تهمت زدن فرق می‌کند؛ مراقب باشید که کسی را متهم نکنید»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/664839" target="_blank">📅 09:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664838">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdmtZwCFgQWwdTJx6_s59Da1Ttle6h46B6s28ltwAHLNkQhrw_7IUGRTGK9Xf5mj3ZR7Rw402VlYP2_3RGyxoUR5ZZmyGo9IjvNdz5ncJgntRGZ93kUJlMQ0dwwM7Abx-LDvxLwKqRYY_rds9_U7QAI723dBuUh9FX5d6BXzyS0E4r3L2UesX41emfpILYgc1V2hYXRLJuiTtmP2EgWkJLqoi43wqVVTedWceo-RHXVbuDGa8jgwryfeaQDwZh0UBMZQYxQZFPEoECIq4dRfb2UjQVx-8bdryo0o76wM6FrnqdnM_aMEH74hCHf8c1b__CdDrFyQIrzc2J3I3P-onA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگر نمی‌تونیم بخوابیم یا صبح‌ها احساس خستگی می‌کنیم، چی بخوریم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/664838" target="_blank">📅 09:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664835">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66fb2b0eb0.mp4?token=lGuSfdbGmTO_OvL4znDAlZ33xnQJXJV3h6HqSMICaKFdVHCNbhdvp2e4tdHSHj47kujLKrQ1srhEAMSxMFNkKSbKlUrwE5oHd2ZUEfYroT_Fesftbg3Cf8nInHGAQxrhRpBFZl46wkl37Yy1x1TU1LeIRjq1WE_o17ELpa7SvpAMp-P1wLAMiUXwjdkQ6HAXvQapzLfzJo8my41WjzUPr7h1EFW8UbjabsY5MdITlTiVnKM7UrCcewkvGptM9axvqj9xxQm56_4GZ0vkPN24FupkOTwrI2DwdfRg5cTpbmoYDjCMgTFIHkO04ZakGU6FqoRVP5cBioKwaFr3EqbKVzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66fb2b0eb0.mp4?token=lGuSfdbGmTO_OvL4znDAlZ33xnQJXJV3h6HqSMICaKFdVHCNbhdvp2e4tdHSHj47kujLKrQ1srhEAMSxMFNkKSbKlUrwE5oHd2ZUEfYroT_Fesftbg3Cf8nInHGAQxrhRpBFZl46wkl37Yy1x1TU1LeIRjq1WE_o17ELpa7SvpAMp-P1wLAMiUXwjdkQ6HAXvQapzLfzJo8my41WjzUPr7h1EFW8UbjabsY5MdITlTiVnKM7UrCcewkvGptM9axvqj9xxQm56_4GZ0vkPN24FupkOTwrI2DwdfRg5cTpbmoYDjCMgTFIHkO04ZakGU6FqoRVP5cBioKwaFr3EqbKVzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
قاب احساسی اسماعیل صیباری، ستاره مراکشی‌ها بعد از صعود به یک هشتم در آغوش مادرش
🥹
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/664835" target="_blank">📅 09:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664834">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bapW7JdEBGrgkuLMkvWB9t4Ey8hhWzKbwhxmkLdk1-ccbaS3-ioU5nkYgh1JcdnJy6tFo1zxLVrsDNbaIPW3_C9FTvAEzWkznrq18t3TWMpGNvr331w9NW0s6r4iaBe6VKuMyQN4xYZwg8z2G7aqI0DSb9CZ74wj-1b_0yJvG-M5K66UY5wYWuAaeWNgvZWi6sjbDCS5gjfjQqz-aXLpJfKWErDu7wRKYieDnWs7CmGEfWcK3UEXZvbtmYoU_B2WzoAVxXCeD6G7GlcY5AzOats6pESHMHMgRbnfjSZxFaSVsUpH5FPJnlpVNUnBKs3vk26pNaBMePwCvFFzHTkBmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاراگوئه تعطیل شد
🔹
رییس‌جمهور پاراگوئه، در یک دستور به نهادهای دولتی و خصوصی این کشور، روز شکست آلمان را جشن ملی و تعطیل رسمی، اعلام کرد.
🔹
آلمان در بازی مقابل پاراگوئه، در ضربات پنالتی، شکست خورد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/664834" target="_blank">📅 09:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664833">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cg0EhvCyG5d3aGXf-Y3t_1OhkFO204Lant0PBjGyRhdgfJ76rNSetAKK7NlMs4srEek_NMx02nknZibPaLQP1jbolM0GwiFAgvK7HRBiHe57Zd3OhATNiwg3F9crUJKwulcl0h1aDO3i5NYrVb574tzzR6U6RiUuHxOZu6lLMNy-YYFhP4UEPHiJ5dtumFqk9KoZx9hWJBuTR9Qr_6omFSUvtLHGIPojH95G9gWoZvQnRofH1GTGecBdKesdHs8PTEO54L6jLq0vBL-0V4BZnKtxPBgTSpGCKPELHqyDRhUYM-0SK_v-ZRljy6LrWdn3i7cqS2lMDvEXfuOsAMaY1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی برق می‌رود، دخل مغازه هم خاموش می‌شود
🔹
قطعی برق فقط خاموش شدن چراغ‌ها نیست؛ برای بسیاری از مغازه‌های کوچک، یعنی توقف فروش، اختلال در کار و خسارت روزانه
#برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/664833" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664831">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427c44222d.mp4?token=IKO5uvQWT9S3b8y2ecyCKiDMAowC1ryIHokROjqP9tn6yXf-f61G4OJR34KXtKBU5ETj17ErBWqW2R2uKkJL_bLmmBlMjwx0gJ_yVYn5h3tLAjlmEyv99NSQL-ojr79DFdnanrab8-pwlS6DyFEYmhWViqoekita-OjTva5TxAVukU47TwOkIUYtONzzfXUfd-b8lKVVlzikni6lcEJGJ6Stj3txt0YLVScJD2dlxHTfRXjvFOjVWonSVffU1KVzde1WXKTaroKOaTufb8ag_QJvriyR7g-Mij9c4FFIWNo-TFwj67eZvZOELErTLyD6noKjXGbvepfRi2EIUCXXVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427c44222d.mp4?token=IKO5uvQWT9S3b8y2ecyCKiDMAowC1ryIHokROjqP9tn6yXf-f61G4OJR34KXtKBU5ETj17ErBWqW2R2uKkJL_bLmmBlMjwx0gJ_yVYn5h3tLAjlmEyv99NSQL-ojr79DFdnanrab8-pwlS6DyFEYmhWViqoekita-OjTva5TxAVukU47TwOkIUYtONzzfXUfd-b8lKVVlzikni6lcEJGJ6Stj3txt0YLVScJD2dlxHTfRXjvFOjVWonSVffU1KVzde1WXKTaroKOaTufb8ag_QJvriyR7g-Mij9c4FFIWNo-TFwj67eZvZOELErTLyD6noKjXGbvepfRi2EIUCXXVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول پاراگوئه به آلمان توسط انسیسو در دقیقه ۴۲
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا     #بیمه_پارسیان #بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/664831" target="_blank">📅 09:16 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
