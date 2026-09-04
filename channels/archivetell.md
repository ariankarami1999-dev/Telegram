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
<img src="https://cdn4.telesco.pe/file/goqBWJ5aXGEqpV7xMWvOtpkFShVtC39CSdbGNR2k-lGg3iBICa_534wX8xUzChvwEHLchPhAZ0DhQ6IdmlkSl3z_tShsrgFKaQLGVyym2uclq4NxNBdwZSvGjd6UShf5RGBXXO6UlNsJjVtchxB3n2nEGU2iOcQphVOWRTC6M979suUM8HhyEw4KzhgSLVDfNngPvhUC0ieK6CjKrgwCMLHXrvD7DIZpFMtCU93eGnY5MPjvciHsuM-p6p-9pp3U2hCSwowt8v4Xe5h3sblqRF8lzEx7I8_SJEFPhXYYBzcd15uBbl9DZwOK51M5MRqHidZEKp4TdE8RSinKGQ34PQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 17:07:57</div>
<hr>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=qLt1w4xFocfFau-qeNEvSibICVI2ENTNSzCQEL4GGkCDBuLVOZJPAbo_QWhFAomNKUwLzImIWsW8rd_1dnzW1Eo6e_ybR7qfakyL-QlenkBRRcqMi6o7GVXJo2YdfDL5dZgOCi9cBpxi3zHQuDUNhwD2dOsY88U2Mn9iH77iLzqSQiwUkd-7k-42BKV3eP70J7EcoWeBG3rJPYmrLkW3aHlXi8d-x0vUWmzg9-QawCYIdty0jrmev1hEdd5eMX_dObZuWvDQy_up07Cn5ZfcGlhHWDszGiiJKbCEmY2yVnu4fcCDqmY_AZ04IKH9re22u2hSU6kMnzxWwcLIRX19Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=qLt1w4xFocfFau-qeNEvSibICVI2ENTNSzCQEL4GGkCDBuLVOZJPAbo_QWhFAomNKUwLzImIWsW8rd_1dnzW1Eo6e_ybR7qfakyL-QlenkBRRcqMi6o7GVXJo2YdfDL5dZgOCi9cBpxi3zHQuDUNhwD2dOsY88U2Mn9iH77iLzqSQiwUkd-7k-42BKV3eP70J7EcoWeBG3rJPYmrLkW3aHlXi8d-x0vUWmzg9-QawCYIdty0jrmev1hEdd5eMX_dObZuWvDQy_up07Cn5ZfcGlhHWDszGiiJKbCEmY2yVnu4fcCDqmY_AZ04IKH9re22u2hSU6kMnzxWwcLIRX19Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌍
Pythia — رادار زنده جهان برای هوش مصنوعی
ابزاری متن‌باز که وضعیت لحظه‌ای کل دنیا رو جمع می‌کنه و بهت میگه احتمالاً چه اتفاقی قراره بیفته
🛰
🔺
بیش از ۴۰ منبع خبری و اطلاعاتی رو هم‌زمان رصد می‌کنه (اخبار، درگیری، بلایای طبیعی، هشدار آب‌وهوا و...)
🔺
پیش‌بینی از فردا تا یک سال آینده
🔺
کاملاً رایگان، روی سیستم خودت اجرا میشه — بدون اینترنت، بدون سرویس ابری
🔗
لینک گیت‌هاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 135 · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=JHzqIfwQxxS_dX2t1IzVxHd4X5inCRtfun42O6RMw_xNuuRSDJp-r_jGQ6q4aRBbHrh_CqgM02GdkolhMtq6YNR9osxghbUfA6XrQ8A-437QkmBeCU7_pFOA8sCdTAenhvP1W_r8UQklHfHcCmUGsnmUUKVavDGDiPeqU_S_zB829ltoyX_rmc-UELumS3jNgW2W2o8VC_HxBjthW322AMODmUNyLrTj-mnQHJZ6GNeqh0utLZydfMWhYKF0NHfdzTkMBtjx7rwNiPDB02l-YNonR4LDvwpDgy1vNkwU8-K5YujTk5LhTmZCYzmdQG_w_RE3xpvC1PCoccn9deg1Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=JHzqIfwQxxS_dX2t1IzVxHd4X5inCRtfun42O6RMw_xNuuRSDJp-r_jGQ6q4aRBbHrh_CqgM02GdkolhMtq6YNR9osxghbUfA6XrQ8A-437QkmBeCU7_pFOA8sCdTAenhvP1W_r8UQklHfHcCmUGsnmUUKVavDGDiPeqU_S_zB829ltoyX_rmc-UELumS3jNgW2W2o8VC_HxBjthW322AMODmUNyLrTj-mnQHJZ6GNeqh0utLZydfMWhYKF0NHfdzTkMBtjx7rwNiPDB02l-YNonR4LDvwpDgy1vNkwU8-K5YujTk5LhTmZCYzmdQG_w_RE3xpvC1PCoccn9deg1Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
شرکت Anthropic ابزار رسمی بررسی محتوای Claude رو منتشر کرده
راهی برای فهمیدن اینکه یه فایل با Claude ساخته یا ویرایش شده — مستقیم تو مرورگر، بدون آپلود
🔒
📎
دنبال یه نشونه امضاشده (C2PA Content Credential) می‌گرده که Claude موقع تولید عکس، ویدیو یا صدا داخلش می‌ذاره.
🖼
فرمت‌ها: عکس، ویدیو و صدا (تا ۱۰۰ مگابایت)
⚠️
محدودیت‌ها:
🔺
فقط نشونه Claude رو تشخیص میده، نه هوش‌مصنوعی‌های دیگه
🔺
نتیجه «پیدا نشد» یعنی نامشخص، نه «قطعاً انسانی» — این نشونه با ادیت یا اسکرین‌شات پاک میشه
🔺
هیچ اطلاعاتی درباره سازنده فایل نشون نمیده
🔗
لینک ابزار
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 499 · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=iinuBCtLDZZS-Zu-dygFN_EmDDMVe9Dwo4TsOKK8MbM3X6bJXvhzg3yjqTx_BIY6mHHzn4LiERGY5_u046M0tgR0_OVc2sg9mQNQp7d7thyFeLbRdS55wFUA3ITMh7HHJt_7GWq8eBzaKJVaAYBMB2m4-0i7FhLlqeORnFRYoleqyI_rT_lC8LGnsTtuwzkF0MyO9qDztxO6QFzJXy7IaZPNdzCytiGein-goTqNeG18UJrpz8rJR_9F4LUiYnKFQgQDQQFWIJ5gUmxXlFZTbWTBjyYn48v8GzMV6NK9Br1j9R8MgrZVs3dkdzhR4gYKUXHbztl1jeEnTH2VIkAlCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=iinuBCtLDZZS-Zu-dygFN_EmDDMVe9Dwo4TsOKK8MbM3X6bJXvhzg3yjqTx_BIY6mHHzn4LiERGY5_u046M0tgR0_OVc2sg9mQNQp7d7thyFeLbRdS55wFUA3ITMh7HHJt_7GWq8eBzaKJVaAYBMB2m4-0i7FhLlqeORnFRYoleqyI_rT_lC8LGnsTtuwzkF0MyO9qDztxO6QFzJXy7IaZPNdzCytiGein-goTqNeG18UJrpz8rJR_9F4LUiYnKFQgQDQQFWIJ5gUmxXlFZTbWTBjyYn48v8GzMV6NK9Br1j9R8MgrZVs3dkdzhR4gYKUXHbztl1jeEnTH2VIkAlCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساخت رایگان ویدیو با مدل قدرتمند Seedance 2.5
🎬
🆓
خبر خوب برای علاقه‌مندان به هوش مصنوعی! سایت Dola مدل Seedance 2.5 رو به خودش اضافه کرده و حالا می‌تونید هر روز به‌صورت رایگان با این مدل ویدیوهای جذاب بسازید و لذت ببرید.
🍸
🎉
✨
ویژگی‌ها:
🔺
تولید ویدیو به صورت…</div>
<div class="tg-footer">👁️ 689 · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7631">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMFvZ53dR0lV0a1slCX33caf5nwxjmQ8791LpFfn-6Qs5rPIEmkeE0w7sgKRrGpV50E5geo79ndXJmP35i1Xr4iCcS9dEJCluy7-0iD56ZC_uURhgJQStUUr56enddw5-A0indoHp_J30ULXnjyK-7vtpV4TWWSJGRLaWqxXm1D6e-Kex9VVvLJQkHRcNr2D-4EDPWQ0k09cyZhcHava6J2HNxxTb9JW2altd6G4IGHZWpI0ut-v9Mk46SvhyF9yNZeazPvo3qeBYMMvheOD1Z3_JA21w27fxuv0hqrs7EdQh9UwNRFNVv09cluy5vR0VGgRPgjS9WbOPP5_8GZBYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن API رایگان GLM-5.3 از طریق TokenRouter
💥
🆓
بدون کارت اعتباری، مستقیم قابل اتصال به اپ، چت‌بات، اسکریپت یا هر ابزار هوش مصنوعی دیگه‌ای
🤖
📌
راه‌اندازی:
1️⃣
ثبت‌نام یا ورود به حساب TokenRouter
2️⃣
ساخت API Key
3️⃣
تنظیم Base URL:
https://api.tokenrouter.com/v1
4️⃣
انتخاب مدل:
z-ai/glm-5.3-free
⚠️
نکته :
به دلیل رایگان بودن ، مدل کمی کند هست و باید در ساعات خلوت استفاده کنید ، محدودیت و ریت لیمیتی اعلام نشده ، این پیشنهاد به مدت محدود در دسترس هست
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 834 · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=YZUPn-XnanGuaWAHAtCZTWdIao6UMcKx-i8iGh6goyZdS3iJvYkvf4uQTusPZGGxNZCY6_GuJY0XwYBZQ5F4RtoFYSX2KI1BJrirne3vdGl1j73xLEObpL4l91-jJVOkbuHtltlhUkxswTFHh70xN7oHau0nW8IMtq2SlCDzoz_A966P_dCb7_bG0v-NSM8Ni6ObcoLF_nT--yHv4aufUsXTdwMZ-okz0hOyuJudpoRfxF-Gwvm90JFzdocdZbc95h3hJ1YqOjKMhSf2Ls5xNHmuUExHreXnxbVoZhnaIzQkNmPsJUpnKdlOkG-9_aQTXGomHsH4xCVmEKJedeqOZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=YZUPn-XnanGuaWAHAtCZTWdIao6UMcKx-i8iGh6goyZdS3iJvYkvf4uQTusPZGGxNZCY6_GuJY0XwYBZQ5F4RtoFYSX2KI1BJrirne3vdGl1j73xLEObpL4l91-jJVOkbuHtltlhUkxswTFHh70xN7oHau0nW8IMtq2SlCDzoz_A966P_dCb7_bG0v-NSM8Ni6ObcoLF_nT--yHv4aufUsXTdwMZ-okz0hOyuJudpoRfxF-Gwvm90JFzdocdZbc95h3hJ1YqOjKMhSf2Ls5xNHmuUExHreXnxbVoZhnaIzQkNmPsJUpnKdlOkG-9_aQTXGomHsH4xCVmEKJedeqOZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثر های شگفت انگیزی که تا الان توسط GPT 6 Astra خلق شدن
🚀
✨
🔗
منبع اول
🔗
منبع دوم
🔗
منبع سوم
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 900 · <a href="https://t.me/ArchiveTell/7623" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7622">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 839 · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvMZrDjuxd8OKafrUnSdE3FmiIG2khvq3cO4YUiDVSHMdSZVtpSKXKjcZw15V3BFlVlBMnKAj3aUxyoWe-IKjRBPkteW5xgAq8Ntm0nFsyY3HhljTUqhD4aX-BhRvvSkKOTQSl0Jxuc-mvo7qYmEpNsJ57G2MufRczS8GAThHwQd5QSjkapbAWdexVJ2ERznG7cFELQ8Og6jc-gChRMvRhm6N6WKwULIZcIbYyX9OqLKVoC_MshzZmr5m1YOfvApn3gSBJ6uCQVkx4r4Vh9N43EFPHd-fZGAX0lcajo3ED99xNFLDbc6cNEnKFoqQGMEe0__9v5hwmv5rUB-m0gu2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
کتابخانه پرامپت YouMind
بیش از ۳۰٬۰۰۰ پرامپت آماده برای هوش مصنوعی
100% رایگان و هر روز آپدیت می‌شه
⏱
📦
چی توش هست؟
🖼
پرامپت تصویر (+۳۲ هزار)
🎬
پرامپت ویدیو (+۹ هزار)
🌐
پرامپت طراحی صفحه وب
⚡️
بر اساس مدل‌های داغ:
GPT Image 2 · Nano Banana Pro · Seedance · Gemini · Grok Imagine
🗂
دسته‌بندی حرفه‌ای بر اساس سبک، کاربرد و موضوع (پرتره، انیمه، سینمایی، سفر، اکشن و...)
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 931 · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7620">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7618">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGEMION | مرجع خدمات مجازی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrOSEeBjMf2WGOcSVIXM6XRWwfgsB9y7miPTx5Ex5ojFdz9eJquWdGyiwWMKw8_SyLtzxq--tDUM6oz79YSGeCVKeKDypTvQpVq8SceMRNRAlphHDgWGgPQhJwOljEEB27KFkprIiZ-oxanVgzpruMw4GS5DBhZ3x46vD5SdXucs32zq1gNAByx3REnzdm_rOHNy4oXscGdWmmgrCrnXxRwghAMpHMtLzi7maYEfCv03tw2bSlSOB_cmqoU94zweCSwZ4ltqwZ2q0bM78HuwTnCy68RvXqf-eTfjtTH5mNzdVSMDLsYZJN56e5Ag9XIUQXFtyrX7KauKbvdpiJAa7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی که تو دنیای دیجیتال لازم داری، جمیون کنارتــــه
😄
پـریمیــوم،اسـتـارز، ارز، گیــفت و خدمــات مجازی؛ هــمه با هــم در جمیون
⭐
🤖
☝️
@Gemion_bot</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/7618" target="_blank">📅 21:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7617">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/7617" target="_blank">📅 21:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqZGb8ybNlGTvmgAfVX221sL63l7co1Hkjs4OYIa8yuHe0ONrtMud8r4maRdQN2rcpxoXpVQG1oxW4snbY63jsJiFGLdc8w9Xi8eoQlR9dbFamAgECN8Z3FnYcqr-Vn8oydeI0YwRmUC70cszVa5cc8OuPG1E036LePFuTaAO8z-WY-EyDv6z3cYY-73yxGwcXAJx0ElRn1DOTwOtRwwsb_fPXQYhwdFJsi9etH7LwaNq54kTzQwHDy17yaL-hLC1UGV6O63yEcHaDDGB3P9boravbohG4NWK7uPopdpm1fpJLGxjEnss2_MZFUEPqst522s_F3xRFdwxlLa0NSJEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5.1 2 days Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=claude-fable-5.1-high
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7Q1O4wHCam1No3dBd9TNMPgHk8vxYP5iI4vIw5QAM_DvCokfqVUMqc-UYV-E1AK9XfkiaTYbynJCVt5YsD33npmkhQZk_l8rnbXtcFdmA2dGR80du6uXfIQfjFJKQUcWDkA0yP9x4zz2iQFfss6Hj4mUQaS6kbnjfRp827aHYW3mMkoxnM2fATFm4rq6SImbnsWAlGzA7GxKedpCYLQYi-Ywk9GacWCtVoBLyL2hT-gVxJNkRPT_35INosi6ctP3cI3J8n0NtCsalN327d1quMX6RjnhmRlCHXDBXIRzGlKW2xw8XPbYevOxz5eTu2-Y1Kvp54DU2IZY3ikRrM_9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
خبر خوب برای برنامه‌نویس‌ها و علاقه‌مندان به AI!
مدل‌های قدرتمند GLM 5.3 Flash و DeepSeek V4 Flash الان به‌صورت کاملاً رایگان
🎁
داخل IDE چندعامله‌ی Verdent در دسترس هستن — بدون نیاز به کلید API جداگانه یا اشتراک مدل!
❌
🛠
روش استفاده:
1️⃣
برو به سایت
Verdent.ai
2️⃣
نسخه IDE رو دانلود کن
3️⃣
وارد شو و از GLM 5.3 Flash یا DeepSeek V4 Flash به رایگان استفاده کن
⚠️
نکته مهم:
این دسترسی رایگان دائمی نیست! محدودیت مصرف ۵ ساعته و هفتگی داره پس قبل از شروع یه پروژه‌ی طولانی، حتماً سقف باقی‌مونده رو چک کن
📊
⏳
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7614" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7613">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuxfRL2JsK7XzJos8Ho7rQcggcFiWfRhJU636GCxvGExRf2ocs0tbvnqHcPSFLNsMBct54CBaa5aSMNqaX5sPVL-0tKllE94O-2Zx7O2pihKJIh9VOOPxOl5j8X7htESAIgnGrp1doz62pZ4T1zVI1YWMwnqH2muvaKHh6HvfcyACixjXDpvbrIuCIZYCmV9gbm2uzXxKkxzcJTdSU3gq2gfY_3XTKjBVea8fQN0M0Rgj-PpXDKi4CsghThw9j5vJn3YpIcZgIJjYFr6Ozvm1N_T0FwOj10cz355-CdeHq3q1Ud4JpANeOscsKScrKUQEO1wt5BoNfukrII8YwarFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه
سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت، Prisma، Supabase، و اتوماسیون‌های ClawHub (اسلک، دیسکورد، نوشن)
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7611">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">10000 دلار کریدیت رایگان Fable 5.1
💥
🆓
🔺
Base URL: https://syntro.up.railway.app/v1
🔺
Model ID: claude-fable-5.1
🔺
API Key: sk-pHXhquluKg5xOejYuGxaFkrZbgArNB7kX9HtvekqCwA64pWc
✈️
@ArchiveTell | #API</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7611" target="_blank">📅 14:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7610">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxCRHPFesN8T13xtP_H0CkJwgP23_Gfle5Pot86WcQzuVtRKns1yNfl_iHuXY_OqHrlQYO9YaGjoqgNvvAQTDHlZ8UZiIWOop-KR9ZPYsvyBoba7SbVwnOB-_uCJnI-nfaZByLWEJ3I5vsUJRBlpBiYHqM3XASS4yh-wAtBVS1Ghm57aCoAN6V23FwI1BYgqT7tFBgWOeNeY_hvkPqIfAOQvrQlomE1YyV9viAMIlqFu2TpMUXn244VIcLb_6pgf_oiziO51WAxwj3HjZyIH1irH4rkL3INCUBm1TbnoyWKgN-T9CkepsNtC_gindnosbgZXsTWhlrqCxp08uPrxNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10000 دلار کریدیت رایگان Fable 5.1
💥
🆓
🔺
Base URL:
https://syntro.up.railway.app/v1
🔺
Model ID:
claude-fable-5.1
🔺
API Key:
sk-pHXhquluKg5xOejYuGxaFkrZbgArNB7kX9HtvekqCwA64pWc
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7609">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">Free Deepseek 2.5 Billion Tokens
🌊
Base URL:
api.pkay.fun/v1
Endpoint:
https://api.pkay.fun/v1/chat/completions
Key: pkay_f38d9bbbfdaea88a190f415eb007ef2ffb74bed33961c366
Model: deepseek-v4-flash
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6TbZKUxHeiEGpAn-Va3SNYBbahR9BHFPxVPDg_DfEf_Z-sOZAF9R-HBnwik_BePmwHGjr60tvLcVmETp9xNeZNC9DPktSuxRw5Zjj8tPN8EMeB4bxOseiepl4w52iVIyYjMwXS8qwWqA6WeDObNybrhdXtwgFj7HzdfqBtzRbi4W59H8Ekc5jHw6hY61OQxqxldlsKUOR-CdvMyBgKxXZ9z-hVAAS9ctOCaX1S_dMT1y_3-kcYjddgDc6TVaJnc311jaaFQPLMC0OxyEnTWrDLTgwknmgXHBjs8T5Xhew6i0C56lT61oWx6SkSeSwW0wtCBB6tw02OhkrKLzFvg3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل Gemini 3.8 Flash در برخی موارد از Opus 5 پیشی گرفت - با قیمت 0.75 دلار برای هر میلیون توکن
شرکت گوگل، سومین مدل Flash را در عرض شش هفته منتشر کرد. Gemini 3.8 Flash برای برنامه‌نویسی، کار با ابزارها و سیستم‌های عامل مستقل طراحی شده است.
بر اساس تست‌های گوگل، نتایج به این صورت است:
⚡️
Terminal-bench 2.1: 89.4%
در مقابل 89.1% برای Opus 5
⚡️
Finance Agent v2: 61.4%
در مقابل 58.6% برای Opus 5 و 53.8% برای GPT‑5.6 Sol
⚡️
HLE-Verified: 54.9%
در مقابل 54.4% برای Opus 5
⚡️
پردازش ویدیوهای طولانی: 87.8%
در مقابل 75.4% برای Opus 5
اما این مدل در همه زمینه‌ها از مدل‌های پیشرو پیشی نگرفته است:
⚡️
DeepSWE v1.1: 71%
در مقابل 74% برای Opus 5
⚡️
Terminal-bench 4.0: 19.1%
در مقابل 51.8%
⚡️
OSWorld 2.0: 59%
در مقابل 75.4%
به عبارت دیگر، این مدل "جایگزین Opus" نیست، بلکه یک مدل سریع و ارزان است که در برخی وظایف به مدل‌های پیشرو نزدیک شده است، اما در کارهای پیچیده و تست‌های جامع سیستم عامل، عملکرد ضعیف‌تری دارد.
قیمت این مدل تا پایان سال 2026 ثابت باقی می‌ماند: 0.75 دلار برای هر میلیون توکن ورودی و 3.75 دلار برای هر میلیون توکن خروجی. پس از آن، قیمت دو برابر خواهد شد.
همزمان، گوگل مدل Gemini 3.8 Flash Cyber را برای جستجو و رفع آسیب‌پذیری‌ها معرفی کرد. این مدل در CWE-Bench امتیاز 47.2% را کسب کرد، در حالی که مدل پیشرو امتیاز 47.8% را کسب کرده است. دسترسی عمومی به این مدل وجود ندارد: نسخه Cyber فقط به متخصصان امنیت تأیید شده از طریق برنامه Fairwind ارائه می‌شود.
در حال حاضر، این نتایج توسط خود گوگل ارائه شده است. هنوز هیچ تست مستقل از این مدل جدید انجام نشده است.
⚡️
جزئیات بیشتر:
Google
⚡️
بنچمارکش داخل سایت
https://artificialanalysis.ai/models
اومده
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7604">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rq-eKkqW2YIA4R9Urbl5MMNhdWrycK6NEc9OriAp7_LbC7cYNZHWSNnqfAEmlqP774NJ9b0zwuTQfAH5jccc_rf4eGV7aQ50jDqurCfG6lSNKSPgHmdi9HWZkVs-4XHabGnCUKNbZj8Y1t9bnqQE4XUMI7IWHxlrfuC2MmpTTgFXeLz3jrKxZTCs_GlMzEct7VkCPrpHbTBFTwYtcLWmTFzb2DSQkFWYSAdrIKzelTN6cZW3P3zNjxZSFZtAPqcjChwhMYh-jIUGC4VLMjANZ3GBR1KNlHfq6oToCHDmkJkPJbcaeJFeNtl9MhKox8qBVC54mUXZmq5gOs5oWY5K5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0jesaDD-GdXVxpjIBTEG8rCf4Wqw-amPynkg0pyKa7g7SWbYjY3GWo-OCZ6Zc8-M5Q1X5SOY5IzyT4Z_Xo0ErqYTao06aL2RSCSxgVcDFtXbFApdsZZT9jY9e3AEI95dwmh4L6dx1b_5MCQzqbGZqozvNedgLeSiWQkNKV_XwUXZhtkvwPphgpjueICcTIXF9TqO9P7P2tW7h-J0r-r-Wa3lRzMEgCpPAQbUrP9Ztrz_6-kckv6FJ7hbJXue7qlSCSlD-cVALpFBYr1ACwMQKDE4ptNhMY1yu_QklbnG8ESPpFLR0MPPhzDR-ijxYDec8PlEVjJG07RSFnSrQnbFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pus13uSduaJi8Ok4Rd-ibBzt2xm4MD5ry65t_fh-6CtKIprnHTA2-7n2INJrdpMxYBmu0RkEeJEGDpheeiymvQl9rcKh6XHFzxiWxy7oiSKOMWlxafWwVKOkslIkzNvkzpWshwYViw5hNAGLoG_LOsq1iBQzsbppmCbLlDKwov1gi-T8sRi4M6uDVPqPVI__jTnp4oVXvc3_O9i1-pR4JMLCcw2UloeR_uu3fNxTTOouKDqxaNCgvvD9YHYQSt7hgcp2i-cfvsDf5KnOco7sO7em7FHgesyJL9ZO1V9MCakx6-M--BwuRBt7Sbkml8tzGCQUtKoS8GTw6xGKqKOPVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ریپوی ArasClient پابلیک شد!
بالاخره سورس کامل کلاینت روی گیت‌هاب عمومی شد
✅
🔗
گیت‌هاب:
github.com/ArasTey/ArasClient
📥
دانلود مستقیم:
github.com/ArasTey/ArasClient/releases
فایل arm64-v8a برای اکثر گوشی‌ها
✅
فایل universal برای بقیه دستگاه‌ها
⭐️
اگه خوشتون اومد یه Star یادتون نره — برای ادامه مسیر خیلی انگیزه میده
❤️
━━━━━━━━━━━━━━━
چرا ArasClient؟
چون کار چند تا اپ رو یکجا می‌کنه:
⚡️
اسمارت کانکت
یه دکمه: همه سرورها همزمان پینگ می‌گیرن و سریع‌ترین وصل می‌شه
🔃
سورت سراسری
بعد از هر تست، سریع‌ترین کانفیگ از هر سابی بالای لیست قرار می‌گیره
🔓
فرمت اختصاصی .arasc
ک
انفیگ‌هات رو تو یه فایل رمزنگاری‌شده امن ذخیره و به اشتراک بذار
حالت Protected: طرف فقط می‌تونه وصل شه و پینگ بگیره — نه آدرس، نه URI، نه اشتراک‌گذاری مجدد
📊
اطلاعات ساب
حجم مصرفی، حجم کل و زمان باقی‌مونده ساب مستقیم از لینک ساب خونده می‌شه و بالای کانفیگ‌ها نمایش داده می‌شه
📣
اعلانات ساب
پیام‌های سازنده ساب خودکار نمایش داده می‌شه
🏳️
پرچم کشور
کنار هر کانفیگ پرچم کشور سرورش (از روی IP واقعی سرور تشخیص داده می‌شه)
📊
آمار اتصال
تایم اتصال، آپلود و دانلود لحظه‌ای + آمار کلی در تنظیمات
🛡️
همه پروتکل‌ها
VLESS • VMess • Trojan • Shadowsocks • Hysteria2 • WireGuard و…
💎
پر-اپ پروکسی، روتینگ کامل، بکاپ و رستور، تم روشن و تاریک
━━━━━━━━━━━━━━━
🔒
ویژگی‌ای که هیچ کلاینتی نداره:
کانفیگ‌هات رو با پسورد به دوستات بده — اونا فقط می‌تونن وصل شن و پینگ بگیرن. نه می‌تونن آدرس سرور رو ببینن، نه کپی کنن، نه برای کسی بفرستن. مخصوص فروشنده‌ها و ادمین‌ها
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEDSQqvg9X_Juix1FIKVfW4jQfQs-OcU2xV65dTW1bfPgrvXOTQcEtHBV7kj9UnFZ1HCXUI2Si4BtQgHVU6qIGQuOarS5hf-vhbyozxF76EHb7vOhOlrevV6ImrsMBjDpCzMlWaePgbE1qoc9eFEZFE2K0KPRjQWwyoxKG1--Gteh1yGu6XHOZXllrAiIj5TgpoDU6PsakmELmg0IlBC8dYKqkNHxPEwZH4a0r79loevY2uwNLKhslzCK-cKWP1wuojHrhiv_8om9sjDXJLlUOIg8_w7yqbPBs5AioBSHSxfil_19oZ5KEpd057JBm5TJ-OBSl2CYkXc1jyCuR-bmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧑‍🎓
✨
OpenMAIC — کلاس درس تعاملی با هوش مصنوعی
هوش مصنوعی داره تبدیل به یه دانشگاه آنلاین کامل میشه!
OpenMAIC
یه پلتفرم متن‌باز برای ساخت دوره‌های آموزشی تعاملیه — شبیه NotebookLM، ولی با کلاس درس مجازی واقعی
📚
📤
چیکار کن؟
یه موضوع، فایل PDF، اسلاید، صوت یا ویدیو آپلود کن، سیستم خودکار می‌سازه:
✍️
ساختار منطقی دوره + اسلایدهای آماده
🔤
آزمون، تمرین و سیستم تصحیح خودکار
🔬
شبیه‌سازی، مینی‌گیم و مدل‌های سه‌بعدی
👨‍🏫
معلم‌ها و همکلاسی‌های هوش مصنوعی برای بحث گروهی
🎙
سخنرانی صداگذاری‌شده + تخته‌ی هوشمند با نمودار تعاملی
📦
خروجی:
فایل
.pptx
یا
.html
قابل ویرایش
🔌
سازگار با:
ChatGPT، Claude، Gemini، DeepSeek و مدل‌های محلی (لوکال) هم پشتیبانی میشه
⭐️
۲۰.۷ هزار ستاره روی گیت‌هاب
— پروژه‌ی فعال و پرطرفدار
🔗
لینک سایت
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDDOQrFMEvHF_cgpLNpkfRydmeJQj8EBm08Z3rNNeB6MfipLJxNJVUl_bHGz7W-u6cR84OhTT8-y0XSOlqE53NMnPTHf8xzHvqtSCAJ7Md4TAnG0d68yBozo7gwRc2-HyZnTE-opoikYfUVmEIf3oSvl3Drx7TKt5Sa9h4bl9RI06Nh3-aNkzkGsJIVCFOO4YhrWmhqpuIDuBLCR_XB4g8llNEsANjyHGrrpj25PWAtjUIs8zSIS0_2nnEFAAyBjBJJ0oTP3hE4yChoIDhPXJVuMPLzSWNPDz4TFfPtHP2OTBFcuUfWaS4psec-1TxJdrDFwLP1BmXLubOeF3BCw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
✨
۵ ویدیوی رایگان روزانه با MiniMax H3 Max — بدون ثبت‌نام!
با این سایت میتونی این مدل ساخت ویدیو رو به صورت رایگان امتحان کنید
🔥
✨
ویژگی های کلیدی :
🔺
روزی ۵ بار تولید ویدیو، کاملاً رایگان
🔺
هر کلیپ ۵ ثانیه، کیفیت 768p
🔺
صدای طبیعی همزمان‌شده
🔺
متن و عکس به ویدیو
🔺
فریم اول و آخر بده، مدل حرکت وسطش رو بسازه
🔺
نسبت تصویر: 16:9 | 9:16 | 1:1 و...
بدون نیاز به اکانت برای ۵ تای رایگان روزانه — با لاگین هم ۵ تای دیگه اضافه می‌گیری (تا ۱۵ ثانیه‌ای)
💡
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvVQPsRP6a1Lh-iKmlg8S4Tshfw7kqbXsikrgW59l8wp2aykRYAHgyAaOniDarqiNU0O1kaKkOZXDfGxwxlcfE5XDep9lOWAjaAIuiDfIZkgOcK4AXL4i4GQqwCDs7kVTWFCRIRESzTLWsQweYRzWld5gMr87P9G5nXNIRnCcDdUi66Z0VNVeJ7Qt83zhNA17TV2RhKmT-NNqbfX8zC12Nxrh9UhcZ36VyVU6rYhFV4Djcrxs8UvDJeTKDhEo95b0xm4D9wdEhvFfxl27fl-P3aTrraC3APPuQGiUJUeylDrRhOFjy9mL2mA-WRCCioRh5CN3qMJh4nqGL51BJXRiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔧
✨
دانلود کامل گفتگوهای Claude با یک کلیک!
معرفی
Discussion Downloader
— یک اکستنشن ساده و سبک برای Chrome که گفتگوهاتو با
claude.ai
به فرمت
Markdown
ذخیره می‌کنه
📝
📥
چیکار می‌کنه؟
کل گفتگو رو استخراج می‌کنه — همراه با:
👤
مشخص بودن نویسنده هر پیام
🖥
بلوک‌های کد سالم و دست‌نخورده
✍️
لیست‌ها و جدول‌ها با فرمت درست
🏷
هدر YAML با متادیتا (عنوان، لینک، مدل، تاریخ)
⚙️
چطور کار می‌کنه؟
برخلاف روش‌های معمولی، داده‌ها رو مستقیم از API داخلی
claude.ai
می‌گیره، نه از روی صفحه! چون توی گفتگوهای طولانی پیام‌های قدیمی از DOM حذف میشن و روش‌های عادی نتیجه‌ی ناقص میدن
🎯
🔒
حریم خصوصی در اولویت:
✅
فقط دسترسی
activeTab
و
scripting
✅
بدون آنالیتیکس، بدون تله‌متری
✅
هیچ داده‌ای از مرورگرت خارج نمیشه
✅
رایگان و اوپن سورس
⚠️
محدودیت‌ها:
🔺
فقط شاخه‌ی فعال گفتگو صادر میشه
🔺
آرتیفکت‌ها و بخش thinking صادر نمیشن
🔺
رابط کاربری فقط روسیه
🔺
نصب دستی (unpacked) — توی Chrome Web Store نیست
🔗
لینک مخزن در گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCs0bRF4RMlaTixZpirbDwLm3sioO2pea5y4eMMVreH3LEsiuV4OM3GWbylgg1rYugdtaQUVI17yXNQZJP-NUw4p-XuD1PB5FAM9EF9rhI3coAYcCX5NrvHpjW6PUVYuYTjjiI3p2yIjxzJbmoPG-hgA6eNzArLo92kh8UCd-Ftrn34E1008vfHR-Y5CugaoPcl9OAiMfGNBU9OHI_jae_QsUvSLWPu36pXYuBhBXuj5MtAF37_OW7pcMIgl09NADBjkF2RlqFLIvOELhWZObNTBY0TVmnzF5VMlQry2Mh_hSBeFvzU-5ROutKbEkcnx0q_7NKOXRV9L_Q7U1CFRkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦆
✨
حریم خصوصیتو با هوش مصنوعی معامله نکن!
با
Duck.ai
بدون ثبت‌نام، بدون اکانت، بدون هیچ دردسری به قدرتمندترین ابزارهای هوش مصنوعی دسترسی داری
💥
🆓
💬
چت و وب‌سرچ با GPT 5.6 Luna
🎨
ساخت عکس با GPT Image 2
🔊
ویس چت با هوش مصنوعی
سؤال بپرس، جستجو کن، تحقیق کن، عکس بساز —  همه‌چیز رایگان و خصوصی، بدون اینکه ردی از هویتت جایی بمونه
🥸
🔒
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeNNM68jLcGuvyj4CffJ_f9obZ9GkKudzqEWniqEmEzsWRPa4-x7tRoZQM1WggvMMWUwyhOlySkNov8a1BgloJycxEittrlhdYUkYbvL5xrtOordbNZw-Jo9iZGiygpxZj4fakkVZ92CYqNAukjUxlyhIb0Y1ejhhgFX-ZvaJtu0ikhiXN6OAuvR42LHjDhCI5ZnEJKAkuy9ORxlgclsotVZ9ax3RbbOhhWsOuUxAkf1AxNAMbSgY7SkxkPubzh_qXVVhBp2ghE5HO3xvojTFsJnchaDAIx6LIabGDW22KPxfMBayCfSYZZ3xAnfl7vZWo3BRULLr_98aQ7y7VH1JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Hy4 Preview: رقیب جدید GLM-5.3 و Kimi K3
شرکت تنسنت، مدل جدیدی از خانواده Hy را منتشر کرده است که قبلاً با نام Hunyuan شناخته می‌شد. این بار، برخلاف روال قبلی، مدل به صورت عمومی منتشر شده است، وزن‌های آن در دسترس قرار گرفته و به سرویس‌های محبوب اضافه شده است.
اطلاعات کلیدی:
🟢
770 میلیارد پارامتر، با 49 میلیارد پارامتر فعال به صورت همزمان
🟢
ظرفیت پردازش متن: 1 میلیون توکن
🟢
حداکثر طول پاسخ: 64 هزار توکن
تمرکز اصلی این مدل بر روی وظایف پیچیده و طولانی است: کار با کدهای بزرگ، تحلیل چندین سند، نمونه‌سازی بازی‌ها و تحقیقات علمی و غیره.
در یک آزمایش کور، شرکت تنسنت 203 وظیفه مهندسی را به 163 متخصص ارائه داد. نتایج به این صورت بود:
1. Hy4 Preview – 2.99 ( از 4 )
2. Kimi K3 – 2.94
3. GLM-5.3 – 2.92
این مدل در تست‌های منتشر شده نشان می‌دهد یکی از قوی‌ترین مدل‌های متن‌باز موجود است.
نکته جالب دیگر این است که این مدل به طور جزئی در فرآیند توسعه خود نیز نقش داشته است. این مدل نقاط ضعف در عملکرد خود را شناسایی کرده، پیشنهادهای بهینه‌سازی ارائه داده، آزمایش‌ها را انجام داده و به افزایش 31.8 درصدی سرعت پردازش کمک کرده است.
نحوه تست:
>
WorkBuddy
– به صورت رایگان در دو هفته اول پس از انتشار
>
CodeBuddy
– دوره رایگان دو هفته‌ای، با تمرکز بیشتر بر روی کد
>
OpenCode Go
– مدل به اشتراک اضافه شده است
>
Hugging Face
و
GitHub
– وزن‌های مدل برای اجرای محلی در دسترس هستند
برخی مشکلات شناخته شده وجود دارد: مدل گاهی اوقات بیش از حد طول می‌کشد و نتایج نهایی را دوباره بررسی می‌کند. به همین دلیل، این مدل در حال حاضر یک نسخه آزمایشی است و نه نسخه نهایی Hy4.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0NdmegRP3wfZMtKAcKKFzm9WU0oCn6ehtqVsRf0jHJeMeyhuSvvWjjvgxPuWlupsVGjKxg3WbDtLCyzmt0IbOVV87Z-BG0opORUaANQPKL_5hDE3LCafZMYr2zGzJaGaJ3NIvGZnhk2igsVgbgUF8V8dJuoqPyDuI71EGxfx3BJGDQUWcI0OQI0FIVdGRXkL5Cq6EoTTTCNW49F6IAtZN4Y24fmKJJ_6lP8p2tDVWzca6uQE0fzxcW_5k6_EiiUCYknV68KXnAyp59Ip-0_YpByvp_skWEPyUcpA-tgKEalmmIogjwml0_tKcZgblclbOpO81bx2RAn7cGEJxLrCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تبدیل PDFهای قطور فارسی به متن تمیز برای هوش مصنوعی!
نرم‌افزار ویندوزی و رایگان
PDF2MD Studio
. با این ابزار، PDFهای ۱۰۰۰ صفحه‌ای رو به متن استاندارد مارک‌داون تبدیل کنید.
فقط در ۳ قدم ساده:
1️⃣
تبدیل هوشمند:
PDF رو بکشید تو برنامه تا به عکس‌های سبک و باکیفیت تبدیل بشه.
2️⃣
استخراج متن:
عکس‌ها رو تو Google Drive آپلود و با Google Docs باز کنید (بهترین OCR رایگان فارسی).
3️⃣
تمیزکاری نهایی:
متن خامِ گوگل رو دوباره بندازید تو برنامه. نرم‌افزار تمام خطوط و نیم‌فاصله‌ها رو مرتب می‌کنه و یک فایل فوق‌العاده تمیز میده!
حالا این متن رو بدید به AI تا براتون خلاصه کنه یا تست امتحانی بسازه!
😍
🤔
پردازش امن روی سیستم شما
🤔
بدون نیاز به اشتراک پولی
🤔
اصلاح خودکار باگ‌های تایپوگرافی
دانلود رایگان از گیت‌هاب
(ستاره
⭐️
یادتون نره):
🔗
دانلود نرم‌افزار PDF2MD Studio
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWj0jtuYQccbN0WFXCKkZfr5-asZ2Nzque_UydweVz2weuwjsmxZaC7Yz8Of3pNmz26_Gdh5Cds2u6ongWsupvKNMONNjcFT_8i1Bt4BqF03alXP3J8ek-Lg2GIp8A8vpxwYVisRM2E4OCzPaSAT93RlKbUvuqAuKO2yJPyaiE38H0mPOZNAoYLeO1YIz2SZY84rRzWjA6NT2Wpl1mxCUtf_VCE40nd7L_6PTmMBjZOn1i27Nk6djAE5VNwhdHGPoe9hUc2HtfSjcS-ytYpJ13B6qjVzdqsisWaKKQjViZLtcUcZqrCmuI4y0ZvskcHnZ9BpusGJtOqI4uc1SELptA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100
د
لار برای دسترسی به API بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدمت یکساله )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
25 دلار
و شخص دریافت کننده
100
دلار
دریافت می‌کند!
همچنین 20 دلار پاداش روزانه
🎉
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFxXrIGJc7KK6cXnIp7N99I7fztSG7ceHzEypGkItS-FdqzJqf1Z6OpYR4OqkdjZz-_r-0zr8PLQX_tvPekJx9JP4-RpAjMoIXJ19O2KpJgVZYAQWcTwpd1jnclDybZY8IIsfNAA-ssFZTRslQztzQIeF7HayeBej06StppunTXDo8WFG2fIIRmlItaGsCEQ4cZUFOGBw3sqUfNWUsgd8Fbhgwv9Jqk7JMktJyOHKoxv5wKk2mFIrM8UJXYo2Qwh7Rl_QuL6fUWJf6INJCY9okglEeBKlucwNR-POxrQIuf2H4PJtPVF2xTRRzbeJSJiF7LATx40-QF7hs3Se6mRbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت 10000 کریدیت رایگان سایت Genspark
💥
🆓
با این روش میتونید داخل این سایت برای مدل های زیر و دها مدل قدرتمند دیگر 10K کریدیت ۱ ماهه معادل ۲۵ دلار دریافت کنید
💵
😎
Opus 5 | Fable 5 | GPT 5.6 Sol | GLM 5.3 | Kimi k3 | Grok 4.6 | Deepseek V4 | Nano banana 2 | Seedance 2.5 | GPT image 2 | Gemini 3.1 flash TTS
✅
❗️
نکات مهم :
چت متنی در این سایت نامحدود هست ، محیط وب سایت یک محیط دارای Agent هست ، همچنین می‌توانید از این سایت API بگیرید ، همچنین این سایت یک نسخه cli هم داره
برای دیدن آموزش کلیک کنید
✅
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dbmk3raWtuB4iLouX5qRVc1xWFycmXRVSKIDnL7GA3xUL8YIBc5BZX1th0R5WatIbIqBMHzkx8Gn6jShj1oZO7teIz6v9C5go-YkSEvfMoe0S7tsEmxi-g_dNrcGY8Ir97zo_PfRAFdi_ez6MRtdwIEes3jwFAGEczJPxPGiNf0009Zlx1e9vLP3UU93FDLzaIWncWTZ4O5sEwpT3_ttrJ4Z9E4YpCxTtzvYVD4mpXJM0aNt-01yv7qJo4NoUctprmXGipM83Y7uHhpZAfRg41FprvyDzFGJsg1v_ssbEmE_689DLb2Q5WQCZBnAY4SGBlYkLr0S1T9CggEqMZeJdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
ساخت تصویر با هوش مصنوعی؛ رایگان و بدون ثبت‌نام!
🔺
بدونه اکانت و کارت بانکی
🔺
بدونه کردیت و واترمارک
🔺
بدونه هیچگونه سانسور
🔺
تا رزولوشن 1024×1024
🔺
چندین سایز تصویر
🚀
فقط وارد سایت شو، پرامپتت رو بنویس، فرمت رو انتخاب کن و تصویر رو دانلود کن
⚠️
مدل دقیق استفاده‌شده مشخص نیست و محدودیت رسمی روزانه هم اعلام نشده؛ ممکنه در ترافیک بالا با صف یا محدودیت مواجه بشی.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=HRPlob0TFltSpwMegX5aS-3LijzJ2pcxc8MbZlY16EBbWUxKJCtt-sDXNwOsDB_nFQ0DQDdkCOmJDj8MJwCfjIDXDr9KFjvhmlR0zblvfUkUp40BR6v3W6CVTRwTnh3XBV8sKY87eKqmaWqW5Ep3MtGahVwCviPvt4U4w6tLMxlm96WlYgQXqE6All2Zl6BLEzbzxasLwXtbuKtDEy0JNctsbwSJIiMecXhCKFK6myO-elVjpyAHyZM9LQ-_jIxVC9aS-OBXryMX0mtbOtwHTQi3jDayxOXyAns8wYw-nwiuhuDMPb7pJqe0mdCUsBghRX3M3jH05pFF5ItiJEc26w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=HRPlob0TFltSpwMegX5aS-3LijzJ2pcxc8MbZlY16EBbWUxKJCtt-sDXNwOsDB_nFQ0DQDdkCOmJDj8MJwCfjIDXDr9KFjvhmlR0zblvfUkUp40BR6v3W6CVTRwTnh3XBV8sKY87eKqmaWqW5Ep3MtGahVwCviPvt4U4w6tLMxlm96WlYgQXqE6All2Zl6BLEzbzxasLwXtbuKtDEy0JNctsbwSJIiMecXhCKFK6myO-elVjpyAHyZM9LQ-_jIxVC9aS-OBXryMX0mtbOtwHTQi3jDayxOXyAns8wYw-nwiuhuDMPb7pJqe0mdCUsBghRX3M3jH05pFF5ItiJEc26w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدها ابزار متن‌باز و رایگان، همه توی یه جا
💥
🆓
سرویس NoSignups یه دایرکتوریِ از جایگزین‌های متن‌باز و رایگان ابزارایی مثل فتوشاپ، کپ‌کات و فیگما رو جمع کرده — همشون هم به‌صورت آنلاین توی مرورگر کار می‌کنن.
✅
🔺
بدون ثبت‌نام، بدون نیاز به کارت بانکی
🔺
توی کاتالوگ، ابزار برای برنامه‌نویسی، کار با متن، عکس، ویدیو، موزیک و خیلی موارد دیگه هست
🔺
همه‌ی ابزارا کاملاً رایگانن
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwpNJO0Xxmli4xu9l7bNQp8tmmkSMVz0-1q9Zy1EAbxV44Ca4JC2A2s4BEzzbkDvALGLiZIDym0WHGSwKZZxxt-3wQxkTlOQsy1mfrhkJnNULbQF9QQ5_hHN-FEyKaG05V7CoqP4t_9x914-kHP7X5xTFPZh4lWomNzAAEGiqrJUDf3tEbVTAO5eSHeaMnsj4mMdhwQO6MVrFAX2h1-TCF9kZ5xfP_SaR2FW1MsbIJkKikSjI39zCXynmy9J93H7wFAvdFNmetE2ETYM_5H5RhALeerKvs-VwNWX6sM9RZiSx0_tiJrq7clI1EqtLUWFs6h_odQ9GO1WTmp43Ng-sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجموعه رایگان ابزارهای تشخیص محتوای جعلی و تولیدشده با AI
🔍
سایت
forensics.media
یه سری ابزار مرورگرمحور برای بررسی عکس، صوت و فایله که کاملاً روی دستگاه خودت اجرا می‌شه — هیچی آپلود نمی‌شه
🛡
✨
چیزایی که می‌تونی باهاش چک کنی:
📷
تصویر:
تشخیص ادیت و اسپلایس (ELA)، متادیتای عکس (مکان، دستگاه، تاریخ)، تشخیص تولیدشده با GAN یا دیفیوژن (Midjourney، Stable Diffusion)، واترمارک نامرئی، SynthID گوگل، کلون/کپی‌-مووِ بخشی از عکس، و متن مخفی داخل پیکسل‌ها
🎧
صوت:
اسپکتروگرام، تشخیص موزیک ساخته‌شده با AI، فینگرپرینت صوتی، ENF (برای فهمیدن منطقه ضبط از روی هوم برق شهری)، و تاریخچه‌ی فشرده‌سازی
📁
فایل:
هش SHA-256 برای اثبات دست‌نخوردگی فایل
⚠️
نکته‌ی مهم:
هر کدوم از این ابزارا فقط یه سیگنال جدا رو می‌سنجن، پس هیچ‌کدوم به‌تنهایی حکم قطعی نیست. برای اطمینان واقعی باید چند سیگنال رو کنار هم دید
🔗
لینک وبسایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=DmfnmLoO6cPiUhcfX-k2uagt9oJmN5qHHI1XC-Zjnf0aLz7TIKwqaPIp7WLfwOCqDPDLLSOobvIAPa6ht8E_-4W0r4B0CSjLP7IfsAzWCtAFI0j8OGt4tyeLN-iZOkoWkBnjo2WBoNuQDTrjgqnLtSjc6_OF8i43_ZAjJfcnhOXx2Dv_ikqTK68lOPKd-AoLDvPlolWXtgvCXKg2QVedZzNHpIK8EnnYFSe1nYnzOA0q3Uer5T3SYXZj6Y3keQVSunpEnVlwxCUj-Nq8BNZ3oeoG2pEBbfwZ6XajtYmoDCI8FrTBZablozpSBKZELjRyZ6VH0WaouuSsjSZlM92t9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=DmfnmLoO6cPiUhcfX-k2uagt9oJmN5qHHI1XC-Zjnf0aLz7TIKwqaPIp7WLfwOCqDPDLLSOobvIAPa6ht8E_-4W0r4B0CSjLP7IfsAzWCtAFI0j8OGt4tyeLN-iZOkoWkBnjo2WBoNuQDTrjgqnLtSjc6_OF8i43_ZAjJfcnhOXx2Dv_ikqTK68lOPKd-AoLDvPlolWXtgvCXKg2QVedZzNHpIK8EnnYFSe1nYnzOA0q3Uer5T3SYXZj6Y3keQVSunpEnVlwxCUj-Nq8BNZ3oeoG2pEBbfwZ6XajtYmoDCI8FrTBZablozpSBKZELjRyZ6VH0WaouuSsjSZlM92t9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوی ترین ابزار افزایش کیفیت ویدیو رایگان
💥
🆓
🎬
هیچی نصب نمی‌کنی — فقط فایلو بنداز توی مرورگر
✨
خروجی با کیفیت 2K یا 4K، هر کدوم بخوای
🔍
جزئیات ریز هم تمیز و شفاف پردازش می‌شن
🎁
کاملاً رایگان — نه واترمارک، نه حتی ثبت‌نام
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJR3cmcKw1c1RqbNJSroObeD_jx2gGD7kxRHNCMsnZAh6ehDeAPA68wdnIHEXW3ZxH_4vhKl4iraWiFUK_ym8vXLwm8k3rK5Z7rNQ7e62BRQPK5KeV_zWcouDubNQWpZ7XjqzTyTVNzmSPEMCvNlAo2SF9H6qWLF7JZS99AnAnhbcUJneXRiqQDmWXtGALP3Ax2PuqsAUq2O2APwAglhBvN3P4T5S1R4kN9aHJUSeWHQEo_T-DWh85u0EiPwlNpA1fSmkn0D_HFGNfdRZ5QXbywNBVpDhJIGzWpFdoEXvygJE3wFrATSCmIcWClbDS2PUX0f3Rwi8tZsn5xkew737w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به API مدل های رایگان
💥
🆓
مدل MiniMax M3 و چند مدل دیگه از طریق Ollama Cloud به‌صورت رایگان قابل استفاده‌ان ( با محدودیت روزانه و هفتگی
⌛
)
1️⃣
وارد سایت
Ollama
بشو و اکانت کلود بساز
2️⃣
با گوگل یا جی‌سوییت لاگین کن
3️⃣
از داشبورد اکانتت یک API Key بساز
4️⃣
کلید رو به 9Router یا هر سرویس مشابه دیگه اضافه کن
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RorsDZ16d6sDalWufzcja-rGHZoOwDFVxzX5EROfqmKIuEjp6nSV3hp0UjrzBm7jTKI4IgDobdg4YZA3XEBiiPh-ha4XUQ-P_nCtjRoj2ycafYEYYUEbcdcOcHW2ZqDlY6De_Sk7cGWPnY15ez-ZENSNAcgaFW8OXvccZ8jKxi-I9FSp41ODcw_javrnHCtjEg4TJigL2LMRqvlpTy53KjloATgav7ON3yH5NHi4AJwf5UrsU9PcgSnwGqtKRmW4o1p6keBLNEwukfbfCvaORg36DRkMiwqfNwCyV_CTmho3OwErUtngafsYrrmBX-gr7kK8Ec-dqOMtx_qpd4Xr6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
DeepSeek Harness Studio
رابط گرافیکی ویندوزی برای DeepSeek Harness
🤔
بدون نیاز به ترمینال یا Node.js!
🤔
نصب خودکار در اولین اجرا
🤔
وب UI رسمی داخل برنامه
🤔
پشتیبانی از پروکسی داخلی
💎
https://github.com/ScannerVpn/DeepSeekHarnessGui
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a7-EhSCcJyxq2DZjVrvDYvaS60HawwY65hqUCOsJWz-N-gay9MPtsyDRnh13o3dlYSSilOR_HEos3obJHKhrPRsjzA4_Rij38BbsUF8pdVQRCgc9ASfsjy46_C3qsu1t8NQJl04sdA3HGegdVxgXsvNav2iCrEtGQhb_8RsgBvpRJ8oyY9Mz1vKMn4cRvY5vS6eDo21a_F-m0rj67EMpW4u9jKYnbA0EiTG_JoW4zk_gaAyT2V2riMXajSsEa6klxyUBdNJoYuzM8fFxRdQ55RmU3b8r1SdJn1Ggx5dRzw-gXo7oWcP80pSTiuHDflxpxuPgFndyWedjWYMQXmAuEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GYersSin1f0TcSBTASgRydE7m0aDO1WWazdim1IygBQMJAhz3mA-N2OkBMu13HD2ZP1yD9Cxes9Tgu20GXVFingd_LdpzB2-OGo-XsDvRQatFvnq4gSb6cyCMa1ukKUSU0O2SzMPMY2_rPbn5ORZmx6CqaMbw7in3weptghxy6rKKWkuc08OXvoV4eGbjaPRqElBLaRAe0bjYAUS32BXas_kPaebkQcxyIla1hoO5iPT7wd623FCHMkIRm_fChRjAZb_mUwcChm2rYq7eztU5oMW1xxs1xzm4LLOOC4jPG6M4pAbL3HUcLZXe7SBJmSaV84XoXV89Zdks1CACDvnXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcEi2ejbhsNYLsQHVZHvpiRirWPUFXtcilh_IYx8-Hks4zSb2ooasroZ5VUXLCTf0tVwZAD4Oj_57uHhhYYl6tHNme6d_kUKAECyLWH_oJ-2d4PqxIoP7Xkkgk-8NGxWJTWRZlYEKLs8jP8LdeDyhIw-FX4C1JtDT2K3dz7Uxjt8OBj3l-PTNKUiQHd3NjwtMy-mHN2Nh44acfjGTU6JKHcJ3eiKsY2LfDNJ6-XznK9wDugk90RCXiIolMP0NnxgR0HaW2P2iVLNpQsXbu1M7sSZm5wL1wO0QSfVFnPZ7eEsNKX3PLBfefibKQnmbYiDoQ8FwgeqlE2Iy72eDlIzOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E5PkK7BuHCzOMG3J3YmjQsUIB8KluYBZ09_lvQSFMt8Hgokry1yJqR0SjWLzF07MiWIkEDKTWx9Nr_D7VrXneYM0w-30YZgXmUg-NmvwGhHQd7NIH2AaIpWWI6QSiiaNpqKfKgP9BpNusTtmSOUDdLG9ocNTwXIiF-74YE9Ty593Uqd4HhdnhAO7vHiMMeykd94IhoMmjaCiLmpbIAoELyhcVs2afMyiAFGy2KQI5KDhHW2CyvQGfhZ4ERNih3NYzIKgWcFynJCDcUu-XDUW5nmmOBjoKiZSRhob-pAzpenlxNkb_EuLPkj_5OjSUuLNa0w-T0XUwdjTaBk_8uzvcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🛍
خرید اکانت
Windscribe
با کریپتو از طریق
Build a Plan
اگر قصد دارید اشتراک
Windscribe
تهیه کنید، می‌توانید از بخش
Build a Plan
پلن دلخواه خودتان را بسازید
⚡️
کافی است مقدار دیتای موردنیاز و مدت اشتراک را انتخاب کنید، سپس در مرحله پرداخت گزینه
Crypto
را انتخاب کرده و پرداخت را با ارز دیجیتال انجام دهید
🪙
🔵
انعطاف‌پذیر و اقتصادی
🔵
امکان انتخاب لوکیشن‌های دلخواه
🔵
پرداخت با ارزهای دیجیتال
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DU5u0u4dZDLDNuaT5_csUi3dxDzTy4PV2P1WhOrsS3X7wLHdOTo6dk57-HZpcq39knz8jSaWy_Z4hL0ovab812DIPP5RlfqGubqwydcbAtXuHZZOq8oQo0XRtZW-v2T3JSTUJG0Nuo6Lsk03mwhM6uRyWTg6r2OyqfEbBsUNK8mXJ6bDsYO1s0OOA8_Hcr8lf2H3ln3S5M7WPi0U1Pu699sQDjQSaEv7gM2VOjb91u9mxrFO_c87-gfwoYEtgZgpMqkWzTA8CrM9ZSjCRfaIjy21tQmBrF0E_HR0-D0QHpCIXZYAUM0DtXh2zL-27fMoqp3KgIdiUPDDy6pZ0FfN-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!
‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون
‌GLM-5.3 Flash⁩
محصول شرکت چینی
‌Z.ai
⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی تست واقعی با ‌Cline⁩، هر دو مدل از پس باگ بر اومدن، اما Ox Alpha با مصرف یک سوم توکن و سرعتی خیره‌کننده‌، برنده بی‌‌چون ‌و چرای میدان شد
😎
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">عکس‌های داغونت رو تبدیل به شاهکار کن
✨
دیگه لازم نیست از عکس‌های بی‌کیفیت بگذری! نورون InvSR رو پیدا کردیم که هر پیکسل رو زنده می‌کنه، بهش عمق و جزئیات واقعی اضافه می‌کنه.
🔥
📦
نصب لوکال از
گیت‌هاب
🖥
آنلاین رو
Hugging Face
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">Avast SecureLine VPN
4KAX6F-Q7LM6J-5LCJ6E
3N7RAW-SG38HJ-5LCJ7W
BJS8N3-NNAVTJ-5LCJZJ
J3BSAR-XJZR32-5LCJME
VUYR9T-JZ5GBJ-5LCJVN
23RWWJ-SEAQGJ-5LCJTN
GFU46H-QA2CDJ-5LCJBE
7SKUU3-S97Y42-5LCJD6
UENGEB-Y9NGA2-5LCJEE
EBF8PY-8CPH82-5LCJ6J
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b12d1vZvlB0zjV9O_WjBmZeLpwQRKcjQVtibd0udyZSVOTbofV8JJaWZA844H_mgEWNPlEbyclKgAR9cmFT3iAWW13BDViZqpkotiZRVzvNXIzibyBUCgAfXW1BVizobwuP2FrfmLSVd7--PVax5IKmnNnJgU6Kn01seUPq_GtBG2-ubvSN2vH-fDdz25mDKNjiHK_3BF7MtxUk49Fh6pSWydoiVysO6UKcagxZOc0zo3LtnkLEVBfg1Enc1vj650mrxuXloe5NvGUwtsh5U0y0DrXOFGrks1OnjGlRDIKfu6z2fitGw5ziNXldzRCdvThw4eZOOOO7A5gWB0ibPTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب
قدیمی داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
100 دلار
و شخص دریافت کننده
175 دلار
دریافت می‌کند!
فقط در کلاینت های گفته شده در Docs میتوان API را استفاده کرد
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBf9_0q5bdij59EIwghWEUfELH1zyjoB4Pe2bmv4GYQv0WJNxS8-FamG1einffEV9XDCfiniirNeHU7P9gnNYjhTBQ4Gxgli-kS8jt2ixnis81J1hE4PO4V57LBdmV5nJ7U9KpBXF8YPjovcYC0VLiv6D-T3r5tjzRysFIHTJqMjwUPG23eD42YgpLZT9zpAAMh5nSLhQY6aVqb1R9ZaQs6UrpKzK_dMMCieKBAfQ-YC0kZEfsSrTJVT68Ykt8xGjb46Ux6w0KZaCEcykZV5zsd45SSPhg7e5U0DEgbZ2y8ottzH42VhifSQ1B41zA7HAkcsqwDrQpv2GTtjCekZew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌های قدرتمند MiniMax M3 و M2.7 به مدت ۱۴ روز کاملاً رایگان و نامحدود روی GMI Cloud در دسترسه
⚠️
⚡️
📌
از
۲۴
اوت تا
۶
سپتامبر
🔥
همراه با
Speech 2.8
و
Music 3.0
🪧
دسترسی از طریق
API
خود
GMI
یا
OpenRouter
💎
بدون محدودیت استفاده
⛓
Link
🔝
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgSjh7XYUq90qnMw5mNDWqhxA54AMkCMs1lRdY3pLQC8264D9e3ipVERSeTun0fTZHAHtJFUq08jt10bYmGkaJWDuLBv_waJ-udXkYl9RWVob2e_npwj82M_XkfAQRBnMZMvOBsj7ZvcKaOUx2X-4P4AHxTkPEyxPWORc-YIhsgdFxoOi6ONvoqE_6fXdkEuhIcPXEz7cQcsNxJiNzuRxmKQ1afrZ80XtF7y8BlrsD0gQSQ7Y1yTwsfGOpk3ru1MCsnlB8NJQoGQuuu6kpTjuR0c28FYUfJdkhwvQ0rxEpsLQHa3jVSEYaeQ2p7IJ1hwojVcZGg_4hTc_Cyqh788VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API بسیاری از مدل ها مانند
💥
🆓
:
Gemini 3.7 Flash | Gemini 3.5 | Flash-Lite | Gemini 3.6 Flash | GPT-OSS 20B | NVIDIA Nemotron | Nano 9B V2 | NVIDIA Nemotron | Nano 12B V2 VL | Ling 3.0 Flash | North Mini Code
✅
📌
Base URL :
http://aihubmix.com/v1
🔗
لینک ثبت نام در سایت
🔗
لیست مدل های رایگان
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6EW-JADtlv8vdaV4w8rLY8OasXjw-R--23cmejqxpM9yAsDpwwvU-ltf6amEQLncjYvrAsEV9Fr773pE3UigFISa5HlhtzNOkQfF1EPMTniZtV8SRcBdvxB1cJKxrrNKSlgwjQiUvGk91BlIaHciVu0BCUrlS-Ahk3OsAkSsHOp5wmRBaMJUPcvR7uldyYS046N08vI0iON4y4yJUiIbFn5w-ehMTPX7f099p7eYFbMv5EaVHRTyGqezlCpbepc123o_EI2YjJfnvLwQ2iqXT1AivAwGFKROYT_5BU6y1hOIIK5J-DbGRiWHAZhz1vnUNMsupLkltKpo8kqwN9eFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به برترین مدل های ساخت ویدیو
💥
🆓
Seedance 2.5 | Kling V3 | Minimax H3 | Seedance 2 | Seedance 2 fast | Happy Horser | Kling V3 Omni | Kling O1 | Q3 Pro Video | Q2 Pro Video
✅
با این سایت 1000 عدد کریدیت معادل 10 دلار برای دسترسی به مدل های بالا دریافت میکنید
🚀
✨
مراحل فعال‌سازی :
1️⃣
وارد
این سایت
بشید
2️⃣
پلن رایگان رو انتخاب کنید
3️⃣
با اکانت گیتهاب یا گوگل ثبت نام کنید
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL : https://api.b.ai/v1
📌
Model ID : deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید …</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMeGe4px-9c_H8e2UU2wCeYTsRBEQkMv1vuKuKBs4k5gyBF3ElFywtWi_CghaC6MArYiWpXTunH_eTbYdkAPXhTkP3xmPv13h7KTY5jZz3x4uVRhzwX3i8xZEByW0wOt-X0nNWV1k0hmH762fvhLVQ8bdVfUrruJT5LFXo_xpXCjIXTGadpB_Igup9Re2l4xLt1CZr16OqSBegVRfzfKfhCHpHRlmTkEgVj99cxpIr9CkyLF9kpH74_MKlq1L4Quk23v_y7wlOAtjejXLH3f8LdLvXNs9w_TpNkckCNH46emWU5JdIQqDC7J74T7wXw1i97f8Jqd_LejSUXtkwtJtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی رایگان به GLM 5.3
شرکت
Z.ai
یک اپ دسکتاپ جدید به اسم AutoClaw معرفی کرده که یه دستیار هوش مصنوعی agentic است — یعنی می‌تونه به‌جای تو روی فایل‌ها، مرورگر، برنامه‌های آفیس و حتی پیام‌رسان‌هایی مثل تلگرام و واتساپ کار کنه.
😎
🎁
هدیه ثبت‌نام:
کاربران جدید ۲۶,۰۰۰ اعتبار (معادل تقریبی ۲۰ دلار) می‌گیرن که تا ۳۰ روز اعتبار داره و می‌تونی باهاش مدل پرچمدار جدید GLM-5.3 و همچنین DeepSeek رو امتحان کنی
✨
مراحل دریافت:
1️⃣
برو به
autoclaw.z.ai
2️⃣
نسخه دسکتاپ رو دانلود کن (macOS یا Windows، نصب کمتر از ۱ دقیقه)
3️⃣
با ایمیل ثبت‌نام و وارد شو
4️⃣
۲۶,۰۰۰ اعتباری که داخل پلتفرم منتظرته رو فعال کن
⌛
زمان محدوده، هر لحظه ممکنه تموم بشه — الان ثبت‌نام کن!
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کانفیگ amneziavpn
[Interface]
PrivateKey = YM8CabYhib72x4z1G3Tv6YPTzkN1EgieYgzRAiEOXGA=
Address = 10.0.0.3/32
DNS = 1.1.1.1,8.8.8.8
MTU = 1280
Jc = 8
Jmin = 74
Jmax = 195
S1 = 115
S2 = 80
S3 = 44
S4 = 21
H1 = 220741314
H2 = 689752078
H3 = 1491205382
H4 = 2102461473
[Peer]
PublicKey = MF3gfbfjik3PoBeXrASElNP8OOXDlalC1ZCmLfqUuSo=
PresharedKey = 5AUecEnESNGx35D0nM1REFG1HAGtUuLTxlzhUHDhkSM=
AllowedIPs = 0.0.0.0/0
Endpoint = 65.109.215.18:51820
PersistentKeepalive = 15
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwSyegrs7G0dvyxOCoBuNGKxlOWc6qZzcro_2toj0gDzh3cFNZbf-ZHDW6VK7MwQUuhDhh4_JrarueD6uQBgPQoLGVsxDgEzuTz5DOZBfxzLTfgSqw3GOtKUUdBNo-nxyQdl29ew8RFqUWUzd8R5w8-AcztFnMeoabRVtPFz94S6u5j7Xtf_DNPfYquF6cQRAS2ulLzPUDjX83SGD_C2jNey8fBjmZlPO6WXBoMK7mCtt0xiw_CF67fxAiuIlsvThCiMgJ2amPzzZAhhZ_KzPVnWVdpRJ0BR_ynOXb-fg6rKqDYXcmWejnx5T31ZvgRKNI9RPCE4FEl5R1d1pcijIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)
همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟
پروژه «روح‌گرام» یک یوزربات فوق‌پیشرفته و اوپن‌سورس با اتصال به Google Gemini هست که مستقیماً روی اکانت تلگرام شخصی شما سوار میشه و رفتارهای یک انسان واقعی رو شبیه‌سازی می‌کنه!
🔥
قابلیت‌های خفن روح‌گرام:
⭐
کدهای رمزی و نامحسوس (Stealth):
با کدهای ۳ رقمی مثل 777 یا 666 کنترل میشه و دستورات بلافاصله بعد از ارسال پاک میشن تا هیچ‌کس نفهمه!
⚡
شبیه‌ساز واقعی تایپ و خوانش:
🌹
قبل از جواب دادن، اول به اندازه طول پیام «مکث خواندن» می‌کنه، بعد علامت ...typing رو فعال می‌کنه و با سرعت دست انسان تایپ می‌کنه!
🎭
تغییر آنی شخصیت
🎲
با یه دستور ساده لحنش رو عوض کنید.
دریافت و استفاده از پروژه از گیت هاب:
https://github.com/faithsaly5-stack/GhostGram
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=ja29XmwDL0n0kWkewphvxYbTWRUFy3ua7CkxMuNbU3PR4CYz8Z4X1Rt4rlbjMaiGSsi2ZI2dGbMrofEMLwvD_GyYnxGpbHsrmj8zaRfey8d7Zv3GDFkqOf5orM0GjSIi2gi8-H1qF2v5hVgHcF-Pl7cfTpMibbHbQs2CpMfo-PoI9_rm7nwxiEZBa0erloBhj8KE4W6mRPQXx-B8F0-1gdMTHjxbkWSNEOssSUEEWTndCyUWXGy9jQzNiM8RG_fQ3isB3rRD2_coQnwuesKUJzyh4hqqBOwyzpHpr8kwAp8paXoTzEZDwhjk9Uh26vLIt7SEZnp_8zqZ61STclVmWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=ja29XmwDL0n0kWkewphvxYbTWRUFy3ua7CkxMuNbU3PR4CYz8Z4X1Rt4rlbjMaiGSsi2ZI2dGbMrofEMLwvD_GyYnxGpbHsrmj8zaRfey8d7Zv3GDFkqOf5orM0GjSIi2gi8-H1qF2v5hVgHcF-Pl7cfTpMibbHbQs2CpMfo-PoI9_rm7nwxiEZBa0erloBhj8KE4W6mRPQXx-B8F0-1gdMTHjxbkWSNEOssSUEEWTndCyUWXGy9jQzNiM8RG_fQ3isB3rRD2_coQnwuesKUJzyh4hqqBOwyzpHpr8kwAp8paXoTzEZDwhjk9Uh26vLIt7SEZnp_8zqZ61STclVmWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡
مدل‌های غول‌پیکر روی سیستم گیمینگ خودت!
محققان دانشگاه‌های UC Berkeley و MIT سورس‌کد سیستمی به نام FreeToken رو منتشر کردن که مدل‌های بزرگ MoE رو بدون کوانتیزاسیون شدید، روی سخت‌افزار معمولی اجرا می‌کنه. سیستم به‌صورت هوشمند محاسبات رو بین GPU، CPU و RAM توزیع می‌کنه.
💻
📊
نتایج کلیدی:
🔺
مدل Qwen3.6 35B روی لپ‌تاپ با RTX 4060 8GB تا ۳۹ توکن بر ثانیه
🔺
مدل DeepSeek-V4-Flash 284B روی RTX 5090: ۲۲ تا ۲۵ توکن بر ثانیه
🔺
حتی مدل ۷۵۳ میلیاردی GLM-5.2 روی یک GPU ورک‌استیشن قابل اجراست
✨
ویژگی‌های دیگه:
🔺
پشتیبانی از ۲۰+ مدل باز MoE با فرمت‌های مختلف کوانتیزاسیون
🔺
یک API سازگار با Anthropic/OpenAI برای اتصال به Claude Code، Codex و ابزارهای مشابه
🔺
نصب یک‌کلیکی با GUI برای ویندوز و لینوکس، بدون نیاز به تبدیل GGUF
🔺
متن‌باز و رایگان با لایسنس Apache 2.0
🔗
لینک مخزن گیتهاب
🔗
لینک وب‌سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=OQblPbYGa80DhSgoY1Fm3wJ_EUG0fdFKCeM_CoF97e9LaSEYAAz8h98IT8GVsv3GSzE1ueJYqaO3c-5dDWpYevzWrG-JFwcanj-T0hEX0zYz4mBH4UhkQjcu1PMleN4OVD21xrHemrW3m4DjnmsjaHKQuAbkBZ8IQgO8aVOQQ8C0MbEwPUVf_3bq-I5cy--POSAOw6Z5NQDlw9h-1F39n6yOCR5UEMVGjp8H0eJ7PZC9Uh5NiTQ8hyb-qYHlopqruYx0Ok1l5TK9Fl1xbqh6xexNDHfp_3PJTERi_cI_N0JjGDoUV-uGkZq23yZIEtPP_iUykhqePMRuF59XhZ6fUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=OQblPbYGa80DhSgoY1Fm3wJ_EUG0fdFKCeM_CoF97e9LaSEYAAz8h98IT8GVsv3GSzE1ueJYqaO3c-5dDWpYevzWrG-JFwcanj-T0hEX0zYz4mBH4UhkQjcu1PMleN4OVD21xrHemrW3m4DjnmsjaHKQuAbkBZ8IQgO8aVOQQ8C0MbEwPUVf_3bq-I5cy--POSAOw6Z5NQDlw9h-1F39n6yOCR5UEMVGjp8H0eJ7PZC9Uh5NiTQ8hyb-qYHlopqruYx0Ok1l5TK9Fl1xbqh6xexNDHfp_3PJTERi_cI_N0JjGDoUV-uGkZq23yZIEtPP_iUykhqePMRuF59XhZ6fUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت خروجی 0x Alpha و fable 5 در یک نگاه
👀
تو کل سطح اینترنت واقعا اتفاق های خیره کننده ای با این مدل رقم خورده
🔥
➡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7548">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgmZxQj1JPsc-R0zDJjLIMWb9FrinfWQbFLWzrD-kKCmZrQ7-QqAVW4Ft7UR4BOMYEMb6UnllEkCFBIgumZ5WZ2ud4WwkdmDlQWmTVRUrnYFzosWy301RPLJ_rRgeQ7jK3-dP8T0ztk7yCt4OLjsBlTnPJfCT0DuFJFJRxQrI8ofOpsumOLVp3mCbFvVmUEKHkNGvUy2-bknv3qyjthkt4jAGT8DdkBAHmuh9oYaAXyLZ9Tyw_rbz-BQZ_HjCnfQXuxn3C6EQGD13pyJX2z0AAIaVqJ9Sg7HTWnBopk5prXN28fcs3CyRcBqbtz6Gmr_eobWTEYEj9mzQ4ebB4VKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔬
دانشمند هوش مصنوعی که خودش مقاله می‌نویسه
یک پوشه از داده خام رو بهش می‌دی، یه جهت تحقیقاتی مشخص می‌کنی، و سیستم از فرضیه‌سازی تا مقاله‌ی نهایی PDF رو خودش انجام می‌ده.
🧪
✨
ویژگی‌ها:
🔺
کار با هر فرمتی: تصویر، صدا، ویدیو، اسکن سه‌بعدی، جدول، فرمول
🔺
درک مستقیم داده‌ی خام علمی، بدون تبدیل انسانی به جدول
🔺
سه مرحله: فرضیه‌سازی → آزمایش با کد واقعی → نگارش مقاله با DOI معتبر
🔺
اعتبارسنجی داخلی: هر عدد باید از خروجی واقعی کد تأیید بشه
🔺
سه روش اجرا: دسکتاپ، CLI، ماژول ادغام با ایجنت‌ها
🔺
پشتیبانی از Windows، macOS، Linux
🔗
لینک وب‌سایت
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7547">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOMaLpUlGFx-qKf7qa7nUDMbFg_0TI__hq43wSQqeyvF0eGbqPOJMzWGXvAk-lCAelel-MesW0qrhKb9BQwapI3FAnSZALVRQdALdIkQYAINu9ovCpWJXvduLrgrB5oHQmBILRNQlUBQi7veJTGdL3_nle504-vZqR0oJ4zxa7SmlRkLbzjocz9m7FVU0HoPJPv6E0-QddR-UO0QXVrDov7RqPCFWSqXFuF3HEnYNI-nIUFmYDz-PXTkib9Ls8Dfj4Vp6RmFOQi9gois0wb0qln2hKroxA7J-BT5Trh7NsK_uG-1lLqT0yrFSVQH_yfHsbUyXr9FCybzHSr9GH8cUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جدا کردن صدا و موسیقی با یک کلیک
یک ابزار آنلاین رایگان مبتنی بر هوش مصنوعی Demucs که صدای خواننده رو از موسیقی پس‌زمینه جدا می‌کنه. کافیه فایل صوتی رو آپلود کنی.
🎶
✨
ویژگی‌ها:
🔺
آپلود فایل محلی با فرمت‌های مختلف
🔺
جدا کردن خودکار صدای خواننده از موسیقی
🔺
پیش‌نمایش آنلاین قبل از دانلود
🔺
دانلود جداگانه‌ی تِرَک صدا و موسیقی
🔺
بدون نیاز به ثبت‌نام یا حساب کاربری
مناسب برای موزیسین‌ها، خواننده‌ها، تولیدکننده‌های محتوا و ادیتورهای صوتی که سریع نیاز به جدا کردن استم دارن.
✅
🔗
لینک ورود به سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUhGKoG5-KhYEGU-hkJl5yU5NIxjEH4aRUxMN_ZfNkUcG1IEUveOcYmnmNr8DAJuvLy3O1-ksruwaRnZtW2nGi8aYh9N_lbn_Z7jk1BTFjD-Q-tXu14TO1OxNwLcZSJGqfBIJbHgjvHY8S0meCEjLDbzBOMBwu6AFaC-LjTv7iLQ9WU9tvLYFeT3pEidXp7JZu3nzmUgcf9JveG7Q8dVla942Uy3c2gSFSDvxrkAQ6yngLk6l1mJDJfQNo9QJmqOQG64qTxrzh1ccN2KA2_jAtIBDB3XEQj29dZvmyguXSQtKaYVrKzXLDEMMj2dmpamSKK9Ck7bFuucd1bVIL3srg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 دلار برای استفاده از API مدل های هوش منصوعی زیر
😎
🆓
Opus 5 | GPT 5.6 Sol
✅
در سایت زیر با ایمیل یا اکانت گیتهاب ثبت نام کنید
( ابتدا کپچای سایت رو تکمیل کنید )
سپس کلید خود را بسازید
✅
📌
Base URL :
https://true-sota.com/v1
📌
Model ID :
claude-opus-5
|
gpt-5.6-sol
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">DeepSeek V4 Pro
| MiniMax M3
♾
♾
♾
♾
♾
ApiKey
—
sk-dc9d4b7df36ba555-rcaq9e-2790fa25
Model
—
am/deepseek-v4-pro
/
am/deepseek-v4-flash
/
am/minimax-m3
URL
:
https://anymodel.org
♾
♾
♾
♾
♾
Free
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7544" target="_blank">📅 21:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7543">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به
هرمس
اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7542" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7541">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">5 میلیون توکن برای استفاده از GLM
💥
🆓
به مدت 5 روز هروز 3 میلیون توکن برای GLM 5.3 و 2 میلیون توکن برای GLM 5 Turbo برای کاربران جدید در اپیکیشن Zcode
✨
مراحل دریافت :
1️⃣
وارد سایت z.ai بشید و با اکانت جدید ثبت نام کنید
2️⃣
برنامه Zcode رو دانلود کنید…</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=PV7kiM8vEBMewpklEqde2qBpnkk1fWkZmtcIDspN8GR63nMNWhOk69vWbqtaf8qFKUPZDYpsd-cdCKT5GnDrmd70b1hhxXYm4VDH4bcdQ2G8K-DSgFp47wK65y8tHHcfTdYJC0SupLIl_64IUpzs1r2JUMZODpFiQ_xzHRx5qZVtxZpC4D-bjRwYAB0mzHOt3KXTOsDwo2wZewruwn5_000se4i9axEXVVSfjJ6PN4kV4ki2vl0M6S3-Rq6v9TseA8lk3Yw5KdwperUnggQ6XyrSRUBwl0su9yqhQ_AKWqlUSwS6t1wxS4GZugcS-_ikQ8DL5ziaJz6O7hwtSjcyNyfX4u9NiwCNVlKNM-rrpPMPusAXHzCPw9PNuaxf86SHrUXk4qYsQTu07nDdR48xdJdLQOLiWs-ROYrffzipBNFiKzBRRorvH0k9N_TF8jcvqEnW_sGC3FTDIg9uhwcGnZf7VVy7XHLmamJRrUbj4Ch8rqyMa73XXrjGw0OXdoz-6bqEPhmZarbfxSUNlHpCsy7_io7WxOFWu90aZjSPaERMtX41twZgc-qyghrp7OpJGZ8yK0fwnMFly4S83SD3juscJWtJM-PL_VLtiJFVPmvr3Zc95BONA5nnF7b28VCV5J-m0AAb8cxWy8cDkXwW25OBF982DqCqKyCHclBtYCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=PV7kiM8vEBMewpklEqde2qBpnkk1fWkZmtcIDspN8GR63nMNWhOk69vWbqtaf8qFKUPZDYpsd-cdCKT5GnDrmd70b1hhxXYm4VDH4bcdQ2G8K-DSgFp47wK65y8tHHcfTdYJC0SupLIl_64IUpzs1r2JUMZODpFiQ_xzHRx5qZVtxZpC4D-bjRwYAB0mzHOt3KXTOsDwo2wZewruwn5_000se4i9axEXVVSfjJ6PN4kV4ki2vl0M6S3-Rq6v9TseA8lk3Yw5KdwperUnggQ6XyrSRUBwl0su9yqhQ_AKWqlUSwS6t1wxS4GZugcS-_ikQ8DL5ziaJz6O7hwtSjcyNyfX4u9NiwCNVlKNM-rrpPMPusAXHzCPw9PNuaxf86SHrUXk4qYsQTu07nDdR48xdJdLQOLiWs-ROYrffzipBNFiKzBRRorvH0k9N_TF8jcvqEnW_sGC3FTDIg9uhwcGnZf7VVy7XHLmamJRrUbj4Ch8rqyMa73XXrjGw0OXdoz-6bqEPhmZarbfxSUNlHpCsy7_io7WxOFWu90aZjSPaERMtX41twZgc-qyghrp7OpJGZ8yK0fwnMFly4S83SD3juscJWtJM-PL_VLtiJFVPmvr3Zc95BONA5nnF7b28VCV5J-m0AAb8cxWy8cDkXwW25OBF982DqCqKyCHclBtYCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
استودیوی هوش مصنوعی که خودش کارگردانی می‌کنه!
اپیکیشن MiniMax Design یک اپلیکیشن مستقل برای ویندوز و مک‌ هست . کافیه ایده‌ت رو توضیح بدی، هوش مصنوعی خودش برنامه‌ریزی، اجرا، کنترل کیفیت و نهایی‌سازی پروژه رو انجام می‌ده.
✅
✨
ویژگی‌ها:
🎬
ساخت تیزر تبلیغاتی، گرافیک، بنر، محتوای کاربرساخته (UGC) و انیمیشن
🧩
ادغام فیلم‌نامه، استوری‌بورد، ویدیو، تصویر، صدا و ادیتور در یک فضای کاری واحد
🔌
دسترسی به پلاگین‌ها و مهارت‌های تخصصی متعدد
📂
امکان وارد کردن فایل‌های محلی و اتصال به سرویس‌های خارجی از طریق API
💰
بعد از ثبت‌نام، ۳۰۰۰ کردیت رایگان اولیه به کاربر داده می‌شه
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7540" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7539">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lz-7Ys00d8y3V_lYJlz3ZnIGs5RrEjIBSrMvR9AgdLQo2PDelHFV-M1aUfr0mOzK9YCM74mQO05k6isAz4MkhC6fOhSyqjOEWEfgg2XWIecE_WzAq9ajjwJEmJFgaLsmP69a0tja7MVBnsnQYFo6hrgWiU70Olo1vTwTTr8m7tsiKBdTXp2J_yozr-_dtiGMO115KvXgpGNNs9KGBAXiXWxaJkNw-nvQYszsCELmvBsLKpX2GW5UFU88Y4FW-Uzg-B--HIhAt7jmwu8FMFfLMXtKDx7M5PaJ7QyPfpyUfBsLJHBWDZBYvf9vuSz8KGdbNTcJ5UWGx7bH4CyFYC46Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐳
۹۷ ابزار جادویی برای DeepSeek Harness — یک دستور، قدرت نامحدود!
یک لیست باز از افزونه‌ها برای DeepSeek Harness (dsh) — با یک دستور می‌تونی قابلیت جدید به ایجنت اضافه کنی.
🔌
✨
دسته‌بندی پلاگین‌ها:
💻
بهبود رابط کاربری — TUI، پنل‌های کناری، پالت دستورات
💬
نشست‌ها و پیام‌ها — شاخه‌بندی تاریخچه، اشتراک‌گذاری گفتگو، حافظه
🛠
ابزارها — اتصال به دیتابیس، CSV، JSON، regex، آمار
⚙
اتوماسیون — هماهنگی چند-ایجنت، زمان‌بند وظایف
🔔
اعلان‌ها — اتصال به تلگرام، هشدار دسکتاپ
🧩
توسعه/رانتایم — ممیزی امنیتی، sandbox، ابزارهای گیت
🎮
فقط برای سرگرمی — بازی‌های کوچک، استیکر، پت مجازی
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7539" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7538">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebIaMkGlbLNK0x60xuiyqr2dr6GPQk1Ih6qk2OpOCFBnHMX0atCONfys3fyjVJlUbRANsihSw60bI3KTEHloV68eyThZz_EYeBcPUPvAurIjnDyImCsgDtQJshi1HWbeNgv76uIFSupD1e0XFSC0kutqI3AYUp3vj7HcXtTkiqVpN8GfoCnbLXEMB6eMzTbXi7sfKzZNsghyGIwh3pVr5uqMjFX-W3FbmdRr6DMpOG74O9Z_sahFW7Ys0z_m_Y0nzkc1F88J6ta_B5QJMZRB1yH8xZ3deJw2RhMtyJ1PK_KG0B2VnY2mYvHbzNrg1zCC9quZSrV_JcYhmKxTHk0bqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
پروکسی وب جدید تلگرام — پنهان‌شدن پشت سایت‌های معمولی
تلگرام یک روش جدید برای دور زدن فیلترینگ آماده کرده که ترافیک پروکسی رو کاملاً شبیه ترافیک عادی وب می‌کنه.
🥸
⚙️
نحوه‌ی کار:
🖥
تلگرام دسکتاپ یک مرورگر کوچک داخلی باز می‌کنه و یک اتصال معمولی HTTPS/WebSocket با دامنه‌ای برقرار می‌کنه که ظاهرش شبیه یه سایت عادیه
📦
کل ترافیک MTProxy در یک جریان واحد بسته‌بندی و از طریق این کانال مبدل ارسال می‌شه
↔
روی سرور، یک نود واسط (relay) این جریان رو به اتصالات جدا تفکیک می‌کنه و بدون رمزگشایی، به MTProxy معمولی می‌فرسته
🌐
دامنه هم‌زمان یک سایت عادی نشون می‌ده، و صفحه‌ی «پل» فقط برای تلگرام و بعد از تأیید باز می‌شه
🎯
نتیجه:
کل ترافیک از دید ارائه‌دهنده‌ی اینترنت مثل بازدید از یه سایت معمولی به نظر می‌رسه — یعنی پنهان‌کاری تقریباً کامل در برابر فیلترینگ.
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7538" target="_blank">📅 16:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7537">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJlZ398_4TB3aEHmAHyjLov_eJt25Lum4NGtOIJ_VzuvwI1ZLfLM3KFewtj0mbZYogJ5Dgqwxxmcc2EhbY8o1xeWXt58Dk4fkL7RDt5_xusHa7uORHDKIWg7n4sW_SuZ4wtP-7JzjlKetYmiVeJ5ZaokCon84zHcPUeIgxAiYs7wbYXntQ2-NPs8o3f6WdA31lyF-k7ikVA8n1s9j-O43KZWXTOz_M0SPwwUfJL5n6eJwpAc8tbspGdQoSl6L6cwRfXoSIaniihjmT7JnK7NhWTw7HStoWkZz29aKuvChiEUu_QASCebS04ALc11m6fj2I1bq0dTtRkV21dTOCpZAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
زمین بازی هوش مصنوعی برای ساخت چهره و آثار هنری
سایت Artbreeder یک ابزار رایگان آنلاین برای ساخت تصاویر با هوش مصنوعیه که تو ساخت چهره، کاراکتر، منظره و هنر انتزاعی خیلی خوب عمل می‌کنه.
🖼
با کشیدن اسلایدرها می‌تونی ویژگی‌های چند تصویر مختلف رو با هم ترکیب کنی و یه تصویر کاملاً جدید بسازی.
⚡️
✨
ویژگی‌ها:
🧬
ترکیب و «تولیدمثل» تصاویر با تنظیم سن، جنسیت، حالت چهره و...
🖌
ابزارهای متنوع مثل Composer، Splicer و Collager
🤝
کامیونیتی فعال برای ریمیکس و اشتراک‌گذاری آثار
⚠️
نکته‌ی مهم:
تو پلن رایگان، تصاویری که می‌سازی
به‌صورت پیش‌فرض عمومی
هستن و همه می‌تونن ببیننشون.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7537" target="_blank">📅 15:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7536">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpgMiB-GdjsfP-Mm8Iqo-WXhPOhFb-aMHh9QCDJnuqepdyp-XP8-wV2HJf246Ypr4i-a0Ee4i5otJ2M2Zv7LNuqSq2NoH27b3TiBJxcWllQ_lfQZmWYMZsQowcXZi3W4nTfuaQwCHyv7XdfQhJ_JhOGG3R2ahcXMv7pxFtxeFV9JkFPGtH8TZDx4bQADOHEqEXwgl80D_1iwk_v1jYcvYjdsFaKhvOxP2J1EsSaJNF73XQPt8loL6LQI91-r-6UTHhVRK1BWymiXhQheYfiyRFzNW-d2U40gRi6KMPIFq-nH3X3t9zYCxYWan0Hfau_N_--0IXw4wuRoCpz6S1t9hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
دروازه‌ی رایگان به میلیون‌ها مقاله علمی
سایت CORE یکی از بزرگ‌ترین موتورهای جست‌وجوی مقالات با دسترسی آزاد (Open Access) در دنیاست.
🌎
بیش از ۴۰۰ میلیون رکورد علمی رو ایندکس کرده و برای بیش از ۴۰ میلیون تاشون، دسترسی به متن کامل رایگانه — بدون نیاز به اشتراک یا پرداخت پول.
🆓
✨
ویژگی‌ها:
🔍
جست‌وجوی پیشرفته
📥
دانلود مستقیم PDF بدون پی‌وال
🎓
پوشش تقریباً همه‌ی رشته‌ها
اگه دانشجویی و داری پایان‌نامه، مقاله یا مرور ادبیات می‌نویسی، CORE می‌تونه یکی از منابع خیلی خوب برای پیدا کردن رفرنس‌های معتبر و رایگان باشه.
📝
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7536" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7535">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IN-vDmhyDOogLufn6c9Jx2jm-z4_Vr1kdfA74NOb0wEYCVkTrPoRpjnj_8Qy6ooZK3aI-Srwm5rwXqsW5I8zCmAeJC9HMPCyh_DHcUySE_qqCUWd6AIP0VMwtHVLPyPJo5XwD6wwn-V7zVMXtrD2goSYsJp_N6fB2mdAgTwRaWbRVmuUDU9xtG0Dw1dT2u_HuNG3d_q-1uKDMx6kjkGo4nzzXzEYrQDiWFaaNNZCb9XgKbrtkCW9j5M_KPZ-VyEENEy251hPFkUH5il0DFpwT6amVGWvmXISnl5D54NImRO6SiR-YrV7UlKZbxRuhKy8cySJNF7A0BVcEqVfJNWJkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتبار رایگان API تا ۳۰۰ دلار بدون نیاز به کارت بانکی
🆓
🧠
فقط با اکانت
گیت‌هاب
ثبت‌نام کن و بسته به سن
اکانتت
اعتبار رایگان بگیر
✅
با این اعتبار می‌تونی از
مدل‌های قوی
مثل
GPT
،
Qwen
،
DeepSeek
و بقیه استفاده کنی بدون اینکه هزینه‌ای
پرداخت
کنی
🟩
Link
🔗
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7535" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7534">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-text">🚀
آپدیت جدید ربات وگا
🧠
حافظه هوشمند وگا
از این پس وگا اطلاعات مهم شما را به خاطر می‌سپارد تا گفتگوهای پیوی طبیعی‌تر و شخصی‌تری داشته باشید.
💬
حافظه در پیوی:
اسم، سن، دستورات و قوانین دلخواه شما ذخیره و در گفتگوهای بعدی استفاده می‌شود ( قابل حذف کردن هست )
👥
حافظه ماندگار در گروه:
دو نوع حافظه مجزا
• حافظه عمومی: قوانینی که برای همه اعضای گروه اعمال می‌شود
• حافظه فردی: اطلاعات هر کاربر به‌صورت جداگانه در همان گروه ذخیره می‌شود
از بخش «سرویس‌های هوشمند» گروه فعال می‌شود و قابلیت ریست نیز دارد
♻️
📊
حافظه کلی ربات نیز گسترش یافت. وگا اکنون پیام‌های بیشتری را در گروه‌ها و پیوی‌ها به خاطر می‌سپارد.
🧰
جعبه ابزار جدید در پیوی
پنج ابزار کاربردی اضافه شد:
💵
بررسی قیمت ارزها
📰
آخرین اخبار
🌐
تعامل با وب
🌎
مشخصات IP
💱
تبدیل ارز
🌐
تعامل با وب:
لینک هر سایتی را ارسال کنید تا وگا از آن اسکرین‌شات بگیرد، لینک‌های صفحه را استخراج کند، یا به HTML/JSON تبدیل کند
🌎
مشخصات IP:
آدرس IP یا دامنه را ارسال کنید تا لوکیشن، دیتاسنتر و سایر مشخصات آن نمایش داده شود
💱
تبدیل ارز:
به‌سرعت بفهمید هر مقدار از یک ارز معادل چقدر از ارز دیگر است
🛠️
بهبودهای فنی
✅
تمام باگ‌ها و مشکلات گزارش‌شده برطرف شد
⚡️
ریت لیمیت گفتگو از ۳۰ به ۴۰ افزایش یافت
🤖
مدل هوش مصنوعی جدید DeepSeek V4 Flash (0731) اضافه شد
✉️
هر مشکلی مشاهده کردید، به پشتیبانی ربات گزارش دهید
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
🧠
Vega AI
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7534" target="_blank">📅 00:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7533">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efaTxBz3NErpuprR1t3zY1l9hZHk0RMQw4iQSoLKL_BwhTXFAqkIo018hfTYHrYu3Cb5AhmiYGlc2B_4eV0k7OII2-qlIjJ9uEBcdwb06Y51iOzd_r7bhsuS6tpnqgsxJXLB5tdqyZchLgYpn_6XcNzucVbQrP-1Z9Q21raj--TekR8GTIGeNtnLyyAFX5JeQkgTZ7DZWHwDyN7J5WN_DXnFrkXCxf7rCORbeDt-whucyPDvTUAbamYNysbSFBC4R2V5MtIauNNo14VJdF_e4VoErlCzZR2ttR3x-jPZbkoacZ4qO2KVytXuU9RCwfWC5bN-hjMNLHAXLQdcd50YQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی کاملا رایگان به مدل های هوش منصوعی زیر
💥
🆓
Opus 4.8 | ox alpha | Kimi k3 | GLM 5.2 | Deepseek V4 Flash 0731 | muse spark 1.2 | Mimo 2.5 | GPT 5.4 | Grok 4.1 | Haiku 4.5
✅
📌
Base URL :
https://api.yjs.im/v1/
موقع ساخت کلید حتما گروه Free یا Free lite رو انتخاب کنید ، قبلش به بخش Playground برید تا بفهمید هر گروه چه مدل هایی رو پشتیبانی میکنه
✅
برای استفاده از مدل های رایگان داشتن کریدیت نیازی نیست
❗️
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=REyDCN8GwQK1YjXTBOUcu5ncRpGuGnizo5cSIJbIyBADWZXT6RQhrPa3NNB_o2KP2o3lkj4ReXw5bNacPCWEClb3GWsFa_vjgb9OZUATj48Twd-x8E7cNpcUB7EZmU8fyqpCWTqTlfCdPNJ2GIbW_bBnlh1lp7TflRyUWRpZNQ9lmMBR4OniSce105B0TkON11d39Fr5m0tymPNls5UAeBjSfIMXuL-UT7vT2MGUjdGzDmaqxlwzvHO5Nz3JZNJDo1lbpdr9eWClacfXJ3mmYjR8rCkrfTd2kipeDC41y5SX7PCnyyyMTEeXdGVK7qAINLde0hNlj_O6xJPmsoTBkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=REyDCN8GwQK1YjXTBOUcu5ncRpGuGnizo5cSIJbIyBADWZXT6RQhrPa3NNB_o2KP2o3lkj4ReXw5bNacPCWEClb3GWsFa_vjgb9OZUATj48Twd-x8E7cNpcUB7EZmU8fyqpCWTqTlfCdPNJ2GIbW_bBnlh1lp7TflRyUWRpZNQ9lmMBR4OniSce105B0TkON11d39Fr5m0tymPNls5UAeBjSfIMXuL-UT7vT2MGUjdGzDmaqxlwzvHO5Nz3JZNJDo1lbpdr9eWClacfXJ3mmYjR8rCkrfTd2kipeDC41y5SX7PCnyyyMTEeXdGVK7qAINLde0hNlj_O6xJPmsoTBkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
بزرگ‌ترین نقشه جهان منتشر شد
دانشمندان بزرگ‌ترین و دقیق‌ترین نقشه‌ای که تا امروز از جهان ساخته شده رو منتشر کردن؛ حاصل ۱۳ سال رصد بی‌وقفه با ده‌ها تلسکوپ برتر دنیا.
📊
اعداد و ارقام قابل توجه:
🪐
۴ میلیارد جرم آسمانی
☀️
نزدیک به ۶ تریلیون پیکسل
📷
برگرفته از ۲۶۳ هزار عکس
این فقط یه تصویر ساده نیست؛ دقیق‌ترین و جزئی‌ترین تصویری‌ه که تا حالا از کیهان ثبت شده و بعید هست به این زودی‌ها دقیق‌تر از این ساخته بشه.
🔭
می‌تونید خودتون توی این نقشه کاوش کنید و گم بشید توی ابعاد کهکشان‌ها:
🔗
لینک سایت برای مشاهده
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQNDs-8Fvmn2UNQ1txgwcC_ysAJqWyNlrHJLP_tdqwnNTemsvhXu1VZIA7fZqKREr4rwUGnROMFyEFDc1C0dsundKTH6zd8uU9P6MoAkpxHKxVA3I-N00ZYIyF6zxZh5GYlMqxqK_oFmR3Gh-xWWbLRUuTXe_m5E1yuhDrG9r8Zclj6bk-AE7UhGqFMoODYvSHUuwMoXqMb2ybQSyLrh294JYJexK_pkh0H5YL2CsmCljLG-4aGXIfoi6OLUdE6KCUJGAb6C6V-sBeX9GjWhOta7LZTlwBunt4T3GGkgHqfCQPRccpypDwJBfPllxxD-4rCwz4VBaha_hfbqsUcwUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل استلثِ ناشناس Ox Alpha رایگان شد
🥷
مدلی ناشناس با نام
Ox Alpha
، بدون هیچ اعلام رسمی از سمت سازنده‌اش، روی OpenRouter به صورت یک هفته رایگان و OpenCode منتشر شد
⚡
✍️
مشخصات فنی:
🔺
پنجره کانتکست: ۱ میلیون توکن
🔺
حداکثر خروجی: ۱۳۱ هزار توکن
🔺
ورودی مولتی‌مدال: متن، تصویر، ویدیو
🔺
قیمت: رایگان طی دوره پیش‌نمایش
🥸
سازنده مدل مشخص نیست. این یک انتشار «استلث» است — یک تأمین‌کننده ناشناس در حال آزمایش مدل است، و OpenRouter صرفاً درخواست‌ها را روتینگ می‌کند، نه توسعه‌دهنده یا مالک آن.
🇨🇳
❓
درباره منشأ مدل، برخی کاربران گزارش داده‌اند که در پاسخ به سؤالات حساس ژئوپلیتیکی (از جمله تایوان) رفتاری مشابه مدل‌های چینی نشان می‌دهد. این صرفاً یک گمانه‌زنی است و هویت سازنده رسماً تأیید نشده.
📈
طبق ادعای برخی کاربران، این مدل در تسک‌های کدنویسی agentic عملکرد قابل‌توجهی داشته، هرچند این ارزیابی‌ها فیدبک کاربری هستند، نه بنچمارک مستقل رسمی.
🔒
بر اساس توضیحات ارائه‌شده، داده‌های ارسالی طی دوره تست برای آموزش مدل استفاده نخواهد شد
🔗
لینک صفحه در OpenRouter
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7529">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9NJ7V235Nq76HNdSSm3OrmcCeoVnDpnb45pOZQguduVm1xt4m8gcJTb7GxWaA9TmX-sUd0iv_6xnJE5JzTcG_UMAgTmj7AZZyrvLsLI_2GXsPHz7CIJua3amyASPegLOSj8-bvJkKjarXHiqBlI55oJvyKlf1IgOgv9WWA7gIEeBDA47CjoYXow8dLTiqaVsam7JsQZxS-5p95eF7H5qAYrVO9E7QRoDdFtI692oXQOASmRTQcOTXC7TE349B_9VIrmc_54NS8zgMr_dghYpo2V3b39kSwlpRh8x2AIwEur3cOae7RfB5FQoEXvflhj8vm8m1Fu4UMkuK7VkDgBYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">70 دلار برای دسترسی به API بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدمت یکساله باشه )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
40 دلار
و شخص دریافت کننده
70 دلار
دریافت می‌کند!
همچنین تا 25 دلار پاداش لاگین روزانه
🎉
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tarh2fq_kHBYbhSlp297swWX73-FQXDcTK-K12oIoLY9Jc_NphR3-BhmVHMTNM9ZqU5r7FJwlSunPD23uC1a_4NdHXig4CRQ6UP4OP9LkV2aIDzknmCGr9-hM8jou7oftRj0XMoUy7Esq-AIAODTY5VOWxElkpC1kZeuqvAMS2cBxCBeiPehacS_u02uEpPlgLwuXnx8cxnkmjnPlQN9A4Nm0fNMs6ImpbK2598yrScddF9FAAc84fDQ1V4ET60YChk3_CE7W3WxgwuO_nkFNrcptV3XUllZG5eitCk_oGj6hseEaLDMEhZoWPYLFVlXT9jltkxQXz_HLzBWJJ2U9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7525">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AO-zA3yQzK6__TVHZL308ekZNeSFpTbqSnMWcBfswwY13LQFJ5sFcllUDRGZAwHWMJqShwvsv-46EvA3G1L2YluY1fMfzRxOBi03YVbOYNR8evOEmGF1QVjABNWFeEMYmiyACIdIGmzv2KNe7BxqVwQU9aLkQuO-VYL2tnqNG8Gbf5rc6-_aa10Lp-VGo3es4JZr1_8LMe3EATcT3rmWAmQSQHEcKJIPXu2QyhzqGA7xQZa5MPOaZI8-jXwrUFdIHC_67Y176z-Lnwdw3D36OfxYVWWkk3SDGPysLKMRIeG3VhcTudiu8V5KMEw0lk0UB6Mv-mTIPetTGP9Cu8m-5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 میلیون توکن برای دسترسی به API هوش منصوعی زیر
💥
🆓
Deepseek V4 Flash 0731 | Kimi k2.6 | MiniMax M2.7
✅
📌
Base URL :
https://hskyauefqcgbvgvxkluj.supabase.co/functions/v1/gonka
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7525" target="_blank">📅 20:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7524">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔒
بهترین ایمیل‌های امن و خصوصی
اگه دنبال یه سرویس ایمیل هستی که حریم خصوصیت رو جدی بگیره، رمزنگاری کنه و داده کمتری ازت جمع کنه، این‌ها بهترین گزینه‌ها هستن
🛡
🇨🇭
Proton Mail
— معروف‌ترین ایمیل رمزنگاری‌شده، با پشتیبانی کامل E2E
🇩🇪
Tuta Mail
— تمرکز کامل روی حریم خصوصی، رمزنگاری در هسته سرویس
🇧🇪
Mailfence
— پشتیبانی از OpenPGP، مناسب کاربرای حرفه‌ای
🇺🇸
Riseup
— سرویس غیرانتفاعی با تمرکز بر حریم خصوصی
🇳🇱
StartMail
— قابلیت ایمیل مستعار (alias) برای حفظ گمنامی
🇩🇪
Posteo
— بدون تبلیغات، حداقل جمع‌آوری داده
🇸🇪
CounterMail
— امنیت بالا، پشتیبانی کامل از OpenPGP
🇨🇦
Hushmail
— مناسب استفاده شخصی و حرفه‌ای، رمزنگاری‌شده
🇩🇪
mailbox
— سرویس قدیمی و معتبر آلمانی با PGP
🇨🇭
Librem Mail
— از تیم Purism، تمرکز بر حفاظت داده
⚠️
نکته مهم:
داشتن رمزنگاری همیشه به این معنی نیست که ایمیلت کاملاً end-to-end رمز شده — یعنی گاهی خودِ سرویس‌دهنده هم می‌تونه محتوای ایمیلت رو بخونه، هیچ ایمیلی هم امنیت 100% تضمین نمی‌کنه؛ این چیز به عوامل زیادی بستگی داره: تو کدوم کشور سرور داره، چطور داده‌هات رو ذخیره می‌کنه، و حتی خودت چقدر رعایت می‌کنی
❗️
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U90MR8hpV4Z-xuDZk72jK3StVm7E-FIsueF-fAJH08of_LKz9no_zXH1kpyeNpaDWX07QfUPnZI3dz7oN2rb_MELAfgYBWsFPWCv4Vt4PbqtcAnSurTx1LyZEFIGECxL1TzK_jV-vurQe_bgg-OLufDv99zju4GLvJaoHjwUFympEkcl0vOGBSRO_bZBLQKYrvxyRu4kD3Zb_X269HrT8qb13PLEAXoNqI0LUiGpEgUYqXVJRk1OW7tS3JvpC-IFrEA39aCo_9zTTcEukBnAlE0Ff_8X5e64jY-4y13SIA4zwD7qM6azBOzsWf2li25fu297Y8ieJeCajCndpfV_Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">60 دلار کریدیت رایگان برای استفاده از API بهترین مدل های جهان
💥
🆓
این سایت 50 دلار + 10 دلار هدیه رفرال و هر روز 5 دلار بهتون میده تا بتونید از بهترین مدل ها استفاده کنید
✅
Opus 5 | Fable 5 | GLM 5.3 | Kimi K3 | Qwen 3.8 max | Grok 4.5 | Deepseek V4 Flash
✅
✨
مراحل دریافت:
1️⃣
ابتدا در
این سرور دیسکورد
جوین بشید
2️⃣
حالا در
این سایت
با اکانت گیتهاب ثبت نام کنید
3️⃣
حالا سایت رو به اکانت دیسکورد خود متصل کنید
تمام حالا برید
از این بخش
کلید بگیرید و استفاده کنید ، همچنین به بخش پروفایل برید و 5 دلار امروز رو دریافت کنید
🎉
📌
Base URL :
https://tokengate-cqt9ivzs.manus.space/v1
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7522">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دو سایت عالی برای گرفتن دامنه رایگان یک‌ساله
🎁
با این دو سایت می‌تونید کاملاً رایگان دامنه بگیرید، فقط کافیه مراحل زیر رو دنبال کنید
👇
━━━━━━━━━━━━━━━━━━━━
سایت اول (ساده و سریع)
✅
🔺
دامنه‌های قابل دریافت:
de5.net
–
cc.cd
–
bot.cd
–
bbroot.com
–
ddns.ge
–
l.cd
–
ccwu.cc
📝
مراحل:
1.
وارد لینک ثبت‌نام بشید
2. یک اکانت بسازید
3. تا ۳ دامنه رایگان می‌تونید دریافت کنید
🎉
━━━━━━━━━━━━━━━━━━━━
سایت دوم (کمی زمان‌بر )
⚙️
🔺
دامنه‌های قابل دریافت:
indevs.in
–
sryze.cc
–
ryzedns.org
–
nx.kg
–
ryzn.pro
📝
مراحل به ترتیب:
1️⃣
وارد سایت بشید
و با اکانت گیت‌هاب (GitHub) لاگین کنید
⚠️
نکته مهم:
اکانت گیت‌هاب شما باید حداقل ۱ ماه از تاریخ ساختش گذشته باشه
2️⃣
بعد از ورود، یک کد QR نمایش داده میشه
اپ Google Authenticator رو باز کنید و این QR رو اسکن کنید
3️⃣
کدی که اپ بهتون میده رو داخل سایت وارد کنید
4️⃣
به این بخش برید
و روی گزینه Repo Star بزنید و برید به ریپازیتوری گیت‌هاب اونها
⭐️
بدید
5️⃣
در آخر روی گزینه Verify کلیک کنید
🎉
تبریک! حالا می‌تونید از هر ۵ دامنه، یکی رو انتخاب و دریافت کنید (در مجموع ۵ دامنه رایگان)
━━━━━━━━━━━━━━━━━━━━
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7521">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxCM8GzmSav5xxrMV9gdMpeH21JXcMIO0D4d5_GhhN_psZNHCFJcIQW68PVDK-W5Na4lQGKdai2uX-zI27e836UryFi2ihTG6J05PSrWMyIx0sCn9rnNR4JELdqSUSiR8ozO33t1Z4io9I3JD-XLTIJHVvBe8_C6LafORS1LjYuM0B8HMCxkTX8OE1UmsWQH-7G8VJqnjH0QDt1zzki8s7xh5eUrvRlOzYbEafzRk80lKNoY1I-ahWKjHbS7AN03FmN7-dvnMI6Jdf1uiAbbvtB061YkhmCOXbOgSlLjG6O140SFJsZkyfFX_m2J62SvPn2FzLXsvQs_i_-xIMba_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون توکن رایگان هر روز تو xkiro
🔥
مدل‌های
Qwen
،
DeepSeek
و
Grok
4.6
رو بدون نیاز به کارت بانکی امتحان کن
😤
برو
x
kiro.com
،
ثبت‌نام
کن، پلن
رایگان
رو انتخاب کن و کلید
API
بساز
🔻
هم می‌تونی مستقیم از
API
استفاده کنی، هم بعد از ثبت‌نام با اکانت
تلگرامت
احراز هویت
کنی و 5
دلار
اعتبار هدیه بگیری
🎁
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qh3nNKKJT_aNoDPNz_H8G0XleLMrlXnP0VpfXG-XwcKn82J3e4NoQNV6vLLL3ETpHw3I_NzgdrzoGBXhjPCTB3zMH7SRJ58VOD9HGdv3V5J21VRpABiGVvpfsgPvVQgxDcfesX_rpU-7_4nkNQAveEGAklVudfgtc_ok6F1_Tw3fF5eimiQ7kU4CabRqYGBqslCLReQA1aTvI3cjBP88NSy50pgbC3N341p5oqSQ79dXs9gCztYijKbi4ZKn3sdbgtfMvxTjNLqNIi3mdXAl5IXgycLKWvvZHSYBO2qdyqb0LueqxFocCuHi74UWnltI2Dw8Menrxo7J3RI9Owm_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به برترین مدل های هوش منصوعی
💥
🆓
Kimi K3 | Qwen 3.8 max |  Gemini 3.7 flash | Sonnet 5 | GPT 5.6 Terra | Deepseek V4 Pro 0813 | Deepseek V4 Flash 0713 | Gemini 3 pro image
✅
با این سایت میتونید به کلی مدل قدیمی و جدید دسترسی پیدا کنید این سایت هر روز به شما 100k کریدیت میده
✅
📌
Base URL:
https://api.anyapi.ai/v1
🔗
لینک ثبت نام
🔗
لینک گرفتن کلید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7517">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مدل قدرتمند
Qwen 3.8
با ۲۷ میلیارد پارامتر الان رایگان روی پلتفرم آزمایشی هتزنر در دسترسه
☑️
اگه اکانت
هتزنر
دارید، فقط
API
رو بردارید و به هر ابزاری که با
OpenAI
سازگاره وصل کنید دیگه لازم نیست پول بدید
🆓
مستندات کامل اینجاست
➡️
experiments.hetzner.com/docs/inference
اگه کسی بلده چطور راحت‌تر اکانت بسازه یا ترفندی داره، لطفاً اینجا بگه تا همه بتونن استفاده کنن
🤝
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/ArchiveTell/7517" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7514">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nibl9HZIDWLWYc5uPqSFZX8HpK-5t3CoSSY7gvPWUnL8D4-JlUUG7-SnGjHMkBXlz_hhIrAVHHYBXMG6XiKZpIzSB-rRbaoBqNGhYSkw3XxjhQhZ0Ftd1QxnUZ90Q1FPc1SrXWx1felVMBDMvPirtIxeI4KrNa_voGUbcs5gY82GtoWPeg5qc2Wj-7RuBkCFjzchQT-wA35HsPg82x9mq6QnS1fGeNEUVTwe7dRtnriauUOBtCuFgdyCGqD4W5PFzhD8RCgijJrivctpFjiscC_HJBZtnaemL53jXlUD3eaLVkoVpmYJ8csdFUmHFf8C_pBmmpZOKIqYoIntp9wBwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZG357t4gzVjnOTjz2q3sIoyEUmxd_df-vWGom135zSigGXBlP8zGX1TjvsYehUVHpHbIV_tFq6M3LAkQJtOaKy9Rl3wQ0880STxR5u0i_1lCvsBx97HtZrrf_HW1ehad2aP2HeSTnIhb9l1LsWjSHJ-nQr-GTcecJEIn8RkkNk8lGN6uQMv7aexbUJQnNFdEXNBROOUSzNKeSNtxdG4XezCOWvs8-uX3e2lohFggp5Z0jZ831Y0GsqMhE3tuXM29ZljsSfHxPqetugTF7l0kNa-7UK6R-YEWEBmBQOCVidQ2DE0RUs4qLePL8Eb7M1w6R0jvpTyTOl8jR1-m0MJRpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت دامنه رایگان مادام‌العمر
💥
🆓
با این سایت یک ساب دامنه روی دامنه‌ی
kdns.fr
رو به صورت دائمی و رایگان دریافت میکنید همچنين میتونید اون رو به کلودفلر اضافه کنید
✅
✨
مراحل دریافت:
1️⃣
وارد
این سایت
بشید و ثبت نام کنید
2️⃣
به بخش
My Domains
برید
3️⃣
روی Order a domain بزنید و دامنه خودتون رو بگیرید
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=Vij8RUxYhRfR1IB0T0eMXIG9V82X6tR1JabC-o0djtoJNZi6dUZCfl0RjHIeD39LB4dPg2eHTXQ28AG2Mp8Z8FhEf9SIZL_f_d7Qx6XhULA78QRePif0lKNs5ExYjhTlifs-TUyv0GhV72W_fQZ7jh1sIFtupTBaKksSVbFO1mPyqW39Ybek0Jsg97vL-L-qW1Ytnm5WbBSYR0xKa_nv9dGElxy9jzZylg4twdOVhbbAKRJVMV8HDLpmg4bvusH0tOD53Jgg11Esl9m7qajavg-nSsEYEk73Jco2rEiIl1ZPYhvaKAjecHLGJEpMULpHu0dgEA_gN2ptLLJWcHfVQoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=Vij8RUxYhRfR1IB0T0eMXIG9V82X6tR1JabC-o0djtoJNZi6dUZCfl0RjHIeD39LB4dPg2eHTXQ28AG2Mp8Z8FhEf9SIZL_f_d7Qx6XhULA78QRePif0lKNs5ExYjhTlifs-TUyv0GhV72W_fQZ7jh1sIFtupTBaKksSVbFO1mPyqW39Ybek0Jsg97vL-L-qW1Ytnm5WbBSYR0xKa_nv9dGElxy9jzZylg4twdOVhbbAKRJVMV8HDLpmg4bvusH0tOD53Jgg11Esl9m7qajavg-nSsEYEk73Jco2rEiIl1ZPYhvaKAjecHLGJEpMULpHu0dgEA_gN2ptLLJWcHfVQoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
📱
وایب‌کدینگ حالا رو گوشیته!
ابزار HAPI اومده که به‌جای جایگزین کردن ایجنت‌های کدنویسی، همون‌هایی که روی سیستمت داری رو مستقیم از موبایل کنترل می‌کنی
🔥
سازگار با Claude Code، Codex، Cursor Agent، Grok Build، OpenCode و چندتای دیگه
✅
🎙
کنترل با دستور صوتی، بدون نیاز به تایپ
📂
دسترسی به ترمینال، چک فایل‌ها و اعمال تغییرات — همه از گوشی
💻
سشنی که روی کامپیوتر شروع کردی رو بدون قطعی و از صفر شروع کردن، رو موبایل ادامه بده
🔔
تایید هر درخواست هوش مصنوعی فقط با یه تپ، حتی وقتی پشت سیستم نیستی
🤖
حتی از تلگرام هم قابل کنترله
نکته‌ی جالب: HAPI کاملاً local-first و متن‌بازه (AGPL-3.0) — یعنی داده‌هات روی سیستم خودت می‌مونه و به سرور خارجی آپلود نمیشه.
✨
🔗
لینک سایت برای دسترسی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7512" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7511">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">الان سه تا مدل قوی رو می‌تونید کاملاً رایگان تست کنید
🆓
برید سایت زیر ثبت نام کنید و به راحتی از مدل های زیر استفاده کنید
✅
✔️
مدل‌ها:
•
z-ai/glm-5.3-free
• dots-studio/dots3-note-prev
• deepseek/deepseek-v4-flash-free
🧾
Link
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/ArchiveTell/7511" target="_blank">📅 09:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7509">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تلگرام برای دریافت پسوند دامنه .gram درخواست داده است
🉐
اگر این درخواست از سوی ICANN تأیید شود، بیش از یک میلیارد کاربر تلگرام می‌توانند دامنه سطح دوم اختصاصی خود را داشته باشند
💎
مثلاً
@durov
می‌تواند durov.gram و
@monk
می‌تواند monk.gram را ثبت کند
☑️
علاوه بر این، کاربران فقط با نوشتن یک
پرامپت ساده،
وب‌سایت‌های تعاملی خود را مستقیماً روی زیرساخت تلگرام راه‌اندازی خواهند کرد
🤯
🚀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7509" target="_blank">📅 22:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7508">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbiHHmJetoMuLTIoFvsGyugpJZhYdBgBjTSnazdEkURlq3xJXEFPmFGeieKZRcMd16Hj3UPOdt6jT_wOAXvRjUNjIYWigQLuJyt1yd85H-VzcVCo5I_wH3PnYDw7yU3f09OcllkHACuXsWyhZE4pjWjR7OW-BuaNy5pGhSJvwamAzWCYrCBkwaogZHKaLDgrJ0vIqtcvBhN1tkkYB6IMvblAH79_TqUH6vc59gVOvQ05jkGOHGTo_7o_DBAW7xAfVsaaU0nBm0xm66JPx6Kain0iQbTzmBLrLuM3ADWg-uD9IcgZPlna7vuRQV2CPvFBSlluI7YRyJt5bZqn_ZEu1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلود کد ابزار قدرتمند طراحی گرفت
🎨
تیم Anthropic به عامل هوشمند خود قابلیت جدیدی برای طراحی رابط کاربری وب‌سایت‌ها و اپلیکیشن‌های موبایل داده است. کافی‌ست دستور /design را وارد کنید و تغییرات موردنظرتان را توضیح دهید.
🔥
سیستم به‌صورت خودکار کدبیس موجود را می‌خواند، خودش را با سبک طراحی فعلی تطبیق می‌دهد و پیش‌نویس‌های متعددی را در قالب طرح (artboard) تولید می‌کند که می‌توانید به‌صورت آرتیفکت به‌اشتراک بگذارید  (The Decoder) . کافی‌ست طرح موردعلاقه‌تان را انتخاب و ویرایش کنید، سپس آن را وارد فاز کدنویسی کنید.
✨
این ویژگی هم‌اکنون به‌صورت پیش‌نمایش اولیه در دسترس است  (The Decoder) ؛ برای امتحان کردنش کافی‌ست دستور claude update را اجرا کنید.
✅
🔗
لینک دیدن جزئیات
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/ArchiveTell/7508" target="_blank">📅 20:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7506">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تست کردن مدل‌های هوش مصنوعی
🚀
حتماً براتون این سوال پیش اومده که مدل هوش مصنوعی‌ای که از یک سایت دریافت می‌کنید، چقدر به مدل واقعی نزدیکه؟
🧐
آیا واقعاً همون مدلی رو که ادعا می‌شه دریافت می‌کنید، یا یک نسخه‌ی ضعیف‌تر و متفاوت؟
👀
✨
توی این پست، ۲ سایت معتبر رو بهتون معرفی می‌کنیم که باهاشون می‌تونید مدل رو تست کنید و خودتون نتیجه رو بسنجید
🔗
لینک سایت اول
🔗
لینک سایت دوم
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7506" target="_blank">📅 18:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7505">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trWtnJ8bzN-OuA-a9cgmqJKpr6V02CQqvJ3SWdd767WRdwbuXUQgnFuKSyLChfuxK8zu0LI20s0eoEndTSem33P7rsayTWFnrtOA1soZWUI0AUB5-m8npXeOz9y1Jy77fErieqbp_CROpAXrdAJLBhaKR7-NpNo310ud2y4xCXUdmgWh8ts4SMNgI9IL9YPhhtSCKnqiye6kXxpw5bE8JnccAtgdfeHqai09V0yLsWO66CG2-eyHIcpJWNMnAxFW7IiLofxDqvh3M90BV1Vx-bmhnRufwaXE6H6nNcChjC32_G9diF7rHTRlWlGN21bo8eZWOkuRcJNieFfCQ9S_9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL :
https://api.b.ai/v1
📌
Model ID :
deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7505" target="_blank">📅 16:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7504">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnKq5pwErT-7HMUZ_VuyWWd42a6NAYCERmQw1t6OgLLl62kZ2uubUoPqEgptx3VS7jPBK2CjVwxGiw5Z8IdVofDAXU0OtLpno0F6DAqkCk8gKtCtoHQrGFmvsRJ4l0MKEwRlWkGyNSeRActtV9WTu4cKZuGgK4WCSCINbK0LX5iSxwxHH5LCaa_Jshy7qDfZjRFpbWE1HvPeoSIHFQAWpAH6bThykCr3H3q_ma3tf6a8F3IKAzoTfI2kfTlfqssXK9hUoDu9S5XKKy0TlW0AKSxjHR4MIrj5tTH82wkJSETdm0aJ60TwrPbTubMdZ2pFF8_Rm3BLhn3OnAKZ44SzBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.2 الان روی OpenRouter رایگانه
💥
🆓
هوش مصنوعی GLM 5.2 یک مدل Reasoning قدرتمند برای برنامه‌نویسی، AI Agent ها و اتوماسیون پیچیده‌ست. نسخه رایگانش در اینجا با 128k Context عرضه شده و از طریق مرورگر یا API سازگار با OpenAI در دسترسه.
✅
❗️
از مدل z-ai/glm-5.2:free استفاده کنید — بدون پسوند :free نسخه پولی اجرا می‌شه.
⚠️
محدودیت اکانت رایگان حدود ۵۰ درخواست در روزه
🔗
لینک دسترسی
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/ArchiveTell/7504" target="_blank">📅 13:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7503">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">هدیه ویژه برای شما
🎁
3 هزار دلار کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
sk-IXNxrDiaLV2vNxU73TC0Y4zSW1uPrXj0a24SxG8LbD4TYkfp
🔺
Base URL:
https://tabitoken.com/v1
🔺
Model ID: claude-opus-5
ری اکشن فراموش نشه
❤️
توی کامنتای پست چندتا کلید دیگه هم گذاشتم واستون
✅
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7503" target="_blank">📅 11:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7502">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAwy0vAJciYFWP1R9tzpppyyWqzANRpmymMBhmU6nhPhnczrIgaWjLrp7_MV8iDd6Fq9PGBTvWnFoVBGKltsKC4jOr2AjETAUeBTRLJNW-wrZAxwYYHhO6Sn3IfG481lnOZD9acPXIT4F2w3JLOXbVKP8EnRjm-8C9d5-zNUFaig5vBDmtzeOvxGFUHSgbavS5EeBXg33K8H3H6VnSPTXF4jvzykeG2FLXVdsJygkm78nyX5t6TBH2nebfs4rRt-ajciJIg0ilVN9xN79riYK51l3wFwogLexmjYo4ViT21KNdFJuaTe8IY0pU_AykLA7ebsfuDkOw0GzEDUZL-oCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4 Pro 0813 و Qwen 3.8 max به صورت رایگان
💥
🆓
این دو مدل در این سایت به مدت محدود به صورت کاملا رایگان و فقط از طریق API در دسترس هستن
✅
📌
Base URL :
https://api.tokenrouter.com/v1
📌
Model ID :
deepseek/deepseek-v4-pro-0813-free
|
qwen/qwen3.8-max-free
⭕️
محدودیت ایی در میزان استفاده وجود نداره اما به دلیل شلوغی بسیار زیاد سایت مدل ها کند هستن،  پس باید در تایم خلوت استفاده کرد
🔗
لینک دسترسی
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7502" target="_blank">📅 10:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7500">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=R9ovvZ-rN_cZt0k53TDIg0GTheQAcZETfaKlBQjPe0viXhYzHKFnAvmhCa8VQGq_q-P-zrqQKxE42ah3kyNoVcPvkT2ojAuJb_kFYvQL1bvDvNMdoMaKHB7S0PuwsueF1RJYBVPFpEXhzhTNQNheY2iUljYJbrG3kxisCDt1mLRPp1U-FsVhiHAWwSDQostR1XdCVzTguTQSP5VL95ZIZxjAMH_s-L31KLaTPpM_ewiXqSMa8AkbRRkYG6o6FCfpCYq28PmklE_XlauDoTXqS13NOFRuF04r1ftBB-Ll6yYRx1Tk7CD5oD22cQ8iP_7atwOsWkDc8MSjxMzgqhF3HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=R9ovvZ-rN_cZt0k53TDIg0GTheQAcZETfaKlBQjPe0viXhYzHKFnAvmhCa8VQGq_q-P-zrqQKxE42ah3kyNoVcPvkT2ojAuJb_kFYvQL1bvDvNMdoMaKHB7S0PuwsueF1RJYBVPFpEXhzhTNQNheY2iUljYJbrG3kxisCDt1mLRPp1U-FsVhiHAWwSDQostR1XdCVzTguTQSP5VL95ZIZxjAMH_s-L31KLaTPpM_ewiXqSMa8AkbRRkYG6o6FCfpCYq28PmklE_XlauDoTXqS13NOFRuF04r1ftBB-Ll6yYRx1Tk7CD5oD22cQ8iP_7atwOsWkDc8MSjxMzgqhF3HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎧
این اپ کنترل موزیک رو مستقیم به تسک‌بار ویندوز میاره
ما FluentFlyout رو پیدا کردیم — اپلیکیشن رایگان و متن‌بازی که پنل کنترل موزیک رو دقیقاً روی Taskbar ویندوز ۱۱ نصب می‌کنه. کاور آلبوم، Play/Pause، Seek، تعویض ترک، Repeat و Shuffle، همه یک کلیک اونورترن.
🎶
با Spotify کامل کار می‌کنه
💻
با Windows Media Player کامل کار می‌کنه
🖥
با مرورگرهای Chromium و Firefox هم کار می‌کنه (بدون Shuffle/Repeat)
🎬
با VLC هم کار می‌کنه (ممکنه Plugin لازم داشته باشه)
⌨️
با هر پلیری که از SMTC ویندوز پشتیبانی کنه سازگاره
سبک، حدود ۵۰ تا ۲۰۰ مگابایت RAM مصرف می‌کنه و عملاً مصرف CPU نداره.
✅
🔗
لینک سایت برای دسترسی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7500" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7499">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RO8qYlW_selt3xLqZzM8lcEgc9atKUCdhNAl3pGQmnRRHTz9KM1JYhR_AXtIhS5MsfASRKIbcTk36eW0E0z-LZULLCs8yaV4cnSagH9-oXKlmNJJZ3u4rptlsiTRMhktbzLVbTHECx7ScwytHa4bh--aL43xzSiFMkGx9e7kO7Ej_Dal_z2l0d-O0e71bZ9iNrrWE-6z3dvXBRQdz_2roXqFTHt1ykGZcAM810BPEd3EkpDjjefhxcndXn7AAClOMbJIvj6lvlOY_qR57TBozHWp-YqGBWbzxHUxguJq3t5gyG8VC__UkcKWNiVNk__AflUu4oKe_dha655qXUS23Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
این ابزار خط‌فرمان، یوتیوب رو مستقیم توی ترمینال میاره
ما ytsurf رو پیدا کردیم — یک CLI رایگان و متن‌باز که ویدیوهای یوتیوب رو تمیز و بدون حواس‌پرتی مستقیم توی Terminal پخش می‌کنه.
✅
👥
قابلیت تماشای مشترک با Syncplay
🎶
پخش و دانلود فقط صدا (Audio-only)
📥
دانلود ویدیو یا صوت با یک دستور
📌
انتخاب تعاملی Format و Quality هنگام پخش یا دانلود
📃
تاریخچه پخش با امکان تماشای سریع مجدد
📂
تنظیم مسیر دلخواه برای دانلودها
🔄
بررسی خودکار آپدیت برای نصب‌های Manual
📺
پشتیبانی از Subscription کانال و Feed شخصی‌سازی‌شده
⚙️
نیاز به چند Dependency داره: yt-dlp، mpv، fzf، jq، curl، ffmpeg، chafa. روی Arch (AUR)، Homebrew و NixOS هم قابل نصبه.
🔗
لینک پروژه گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7499" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
