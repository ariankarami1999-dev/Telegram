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
<img src="https://cdn4.telesco.pe/file/Jiw9pe1vta3Gog8mIMz1nQVW0XegOH7KG_VvJzsP-GEQmcdKN-PyCwF1eZlxVBLUQkNwPNkKv-XGIuBKCdRd4L3fGyz1lvZTBYMEhmknE00td56WVSuMAxIG9MRWUEOmGkosGtQ7voKUqQDD269zyo3x6rIdpaWfO2InDF1vWIjrarr4tAvLVt5fHSLkdsab0g5Ia37psYObv3tBlm4xCBAp2tWs8CaQa_xqyfK0H7gbBymgPiOj6c3RjCwy1U_ddrVGfLyxyF7KH28VEYyk2vtXRQXbRNJA6NVcCBQS9egSbL1jcvDrUm61CUzHbg_F_ib40binEsXso8SwYUYwuw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 570K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 17:38:33</div>
<hr>

<div class="tg-post" id="msg-29313">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGJA3tB0W7QzN1c8QlThCkwNaNmac1TGBxQEAQFkQdhZ4jK94kvjB60ZbFRz7ZtC7NO4MwAFa_jEeCs-qcNZEed5ULKnjtJBrIddHMB6l0INoH7WxXzwt-0aFAVVC_JkD5xS6-YDCIMaMiUd09wQ7JWqUZvLS1o_qNAJMJJbgEU0UjRSI7EJ_Je-bjiUKJyJaxmH_Wr9Xow_9iy2uN9akE31TwHUkPR4p8AT2SQSkvhvXu9xHCoN-2PfFq9_0b1FhB02nY4fl5CU_m6eORJ-DpFkK_Zf62y6qQcWWOUabv_KUNu5Nl6m0n9w8uSpx9sld7k3daIWuayTsAe4TJlLcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
پارتنر گابریل مارتینلی ستاره تیم ملی برزیل هستند که پزشک هستند و گفته دوست داره از بین برزیل و پرتغال یکیشون قهرمان جام جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/persiana_Soccer/29313" target="_blank">📅 17:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29312">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyMM6fq_YQttxFVlvM3fU_a8G1N-QCuaWxcthm6DyjAxvp1TKUTiBYdLVbKR6ubYi7zEbnPtrR0ILSRc5Q-8h39npe9-gl0UgeUqpiLqAfAjoaJdlgca-SFXgE89ArbLZkVY13dXhc-QC0I2j6DzJwWpE-AtCVR44x_7I9R0ebTJ77bK9TQq3z2BIZKTOYJADbLVPGeC57eZvrqGvWyBNRpiMMgHHphL-F83Q_quRaJS3N4fEuYv4mHe0X0OIOQwTCq9ys4D2KaO2BaCJ5fxXLBaKCYsOcK1diOxpzPZG_S0QWOJrlAgLVciawEmLwiy-9KXrgguBw_Uhqgf0Of09g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/29312" target="_blank">📅 17:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29311">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R93EB6xcySV-cOGp_XBTzo_gYg_gP18KZoXP_2-McSBW_dssPSoYXBndFYV4lxWausHIleGfDJUPt0nQJF-ZPD8jUNqVnQl0xutf7Ss1XnFyrkiQZGDVyIjgHQhJf10GLIivkEN6DUuM1YHXBn8A9R6kmuDdIEZF0dNqHzLGOA3rovub_k1OCOMsQ1EfNSv2Y22WfyJVaJ9PrJ7fiHRToH6-9TDj7-Psf67MAqNpAnY6jhS5atDT6iZpaP19qEPEdNm_w3rcGNzuI72mo_i93BhyzCQGzPwiT0mHz3sp24SRAKutOKAhodd18veXYd4O9kxr7I9VlOEGjA9rhuGvAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ اولویت بندی هلدینگ خلیج فارس برای مدیرعاملی تیم‌استقلال مشخص شد: ابتدا علی تاجرنیا، دوم شهاب الدین عزیزی خادم و سوم محمد رجائیان. از بین این 3 تا یکی قطعا بعنوان مدیرعامل جدید آبی پوشان انتخاب و معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/persiana_Soccer/29311" target="_blank">📅 16:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29309">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWY-ENO1T7QlrhRKez5WGtY_9vF6sW9C57o9-PfOof4kHWGaofSAPGDpqX0XV98dlE0U0bJQLbxXIC8J1-0cxQnXZmRZsJzxf5FhLXfFi8ZEfb1sydy6j266RlumhcKw1ccfPjpzY0cO8sYcWEw43r9hukUux8NJZlTXu_-xel26f1EukYAp5H9D27Nus1qYNTpt53f4GDeSctA-j48GaamC0Q7_MBtXDqwDFrEbUQD4Xh0eJbY8ZDhqT8IWyDd0gQT0b-3LWwrjqKFJyIR8M1w7MUeKqhbmN8BV3pm7e9LIQ1FYeeM5lwDxhwCuWcElgt_6RL6O_VKYvbvx6rx2jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مادر کوبارسی‌مدافع‌بارسلونا:
اینو حتی خودشم نمیدونه ولی اون هرشب تو خواب حرف میزنه. یه بار رفتم تا ببینم چی‌میگه دیدم داره تو خواب به مارتین میگه خط آفسایدو نگه دار بازیکن تو افساید باسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/29309" target="_blank">📅 16:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29308">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‼️
هایلایتی‌ازعملکرد موسی‌چنپو وینگر مالیایی سابق استقلال در تیم جدیدش پانایتولیکوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/persiana_Soccer/29308" target="_blank">📅 16:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29307">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vt4bOvzdbnxBJGmgn8Qnfw7p6IaZLF5GlzFU1kM_MlqFBeIDjs_GtL6LXcG7pAeilqj2r4W9s971a5-6FLmf3Ls6YJcpWBznZBFNtFtIdhCpkN4Tc4uSu4AsLRpeMEQrMbb6q-aD_TOXBb5iPt38qzt66jzc0sdUNdlHvw5AYkrZCYPKztWTsYSagKXAmh9l6dbYBNRrd-eZJsNYJhmAwHwhLtKnc72CzkBx9gRk3pIVFcF-L1D-aCd42OhLVl6k377_HQccXEJEEeNVJrqnCHFpi-XOSSTIx8QPfE88pGgyTHGD7bQ4B6Fe_4OL2OLpdekal6CYCeJferbU4eYz-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌گلزنان‌تاریخ‌رقابت‌های لیگ قهرمانان اروپا به‌مناسبت‌شروع‌فصل جدید این مسابقات از امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/29307" target="_blank">📅 15:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29306">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGy7AvCRogbR8wGoce_YAYdX-Ng5_qFyCDBIOwM1cjKbZkS_NAcba1Ug1rbvkdUeGvx8-wHKS-kStgnZjmMNt8qC_cuAb3DUV2ZBXMboCIeFwvlf88Ghw59-JXk4tYu6eP04gtN8RvVTAqJfnL4xOBp-_VSZuAtDOhCu__1VU1OACoWA0WR4rKHPWsuS_2qhzE5DD1-8Nt6-r5ynpKQ6YQiRfx6u6ihtthUzwsx8gjUgbudRKEO-dmey-nXo_gHwCQEKMKPln3srEGUm5-T2mKW5ADKFVZfjdjvUTUgaO37EHYlJeUCTmzmftRTOZa45DvDwlgoKBk8Cv-ZznFkgMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
👤
به مناسبت شروع فصل جدید چمپیونزلیگ؛ نگاهی بندازیم به‌عملکرد کریس رونالدو بهترین گلزن تاریخ این‌رقابت‌ها با وجود دوری چند ساله از UCL.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/29306" target="_blank">📅 15:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29305">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfa4b6c3a4.mp4?token=E47ssO6SJuAua_VwNFEyezpnuMagg-GHe0Sx4Q97IGe_FHS6tvMEpDlwx9FzH7H7rRE0Wvr2w2tBy_6jjFADozuYisvcEOEjOLPMsHWfRLcgOa6KAEElepP24hd730HI5ttpU5Y5mBud1vCNUUijj7po6vsGPvkfbCa4-UipYNdkJGEUQrD7BiHSH477kKGFgOnDDlFiD2798hobeDoHW_JRqJm_dAhvrPgFinAoDcA7U8HUhflHvHjXxMBlajhD6LU-spEK3Khi0SDp62F6U-AwX3ZgeTtC20tYQ24peEJU7HUDtmjl6yPFglCoUxps25GV5Uki3tObF3XV-sFRig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfa4b6c3a4.mp4?token=E47ssO6SJuAua_VwNFEyezpnuMagg-GHe0Sx4Q97IGe_FHS6tvMEpDlwx9FzH7H7rRE0Wvr2w2tBy_6jjFADozuYisvcEOEjOLPMsHWfRLcgOa6KAEElepP24hd730HI5ttpU5Y5mBud1vCNUUijj7po6vsGPvkfbCa4-UipYNdkJGEUQrD7BiHSH477kKGFgOnDDlFiD2798hobeDoHW_JRqJm_dAhvrPgFinAoDcA7U8HUhflHvHjXxMBlajhD6LU-spEK3Khi0SDp62F6U-AwX3ZgeTtC20tYQ24peEJU7HUDtmjl6yPFglCoUxps25GV5Uki3tObF3XV-sFRig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی‌از لیگ جزیره به لالیگا میای؛ برگای رودری ستاره تازه وارد بارسلونا از سطح بازیکنان والنسیا ریخته؛ پنجاه بار گفت داداش اینا خیلی ضعیفن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/29305" target="_blank">📅 15:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29304">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgXwFaaPoGaAX0jlpju0BohhQhyuIAVHdXgW7ssTdUWYtU49LsrZjbkqJ8IeJD2lZbjXgat_7hXTqYVzvYtaHf-uUH_sOr8v4Z9Bcf0CLYaTpUVBEGjJRY2CvtPsJvc6ya3LA3rcvaFpm2Qt-HRLzcwmW-W8e_1ePXpv8DhDlTyoouTihbQOtNR2Uz2IIkrsko14nyXYP8ik0cnEWq4ST_d1D2yMLPxsMmNHYtkuseYgnUH55FNrVU0yfTClwfuWsJb5wqjJ4hkV7r9TsqRbOR4TW7fov1U03GgbaTtGHN_R6JZSlRd94jG6yivLIxmehUDKxu2fCX1b4gYbwejBhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمدرضا شایع به این شکل جواب میثاقی رو داد؛ تو خودت مفت‌بری. دیگه‌از مفت بری حرف نزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/29304" target="_blank">📅 15:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29303">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZH7J7TggoJbQ8uusB6UMs4q75YweS_ySFxZAZfSvNlZ23P5aZeoEQGzjPDHE-DVg6A1izEHOtvz6dwbXANAXLWIrJnS1CsSFjXuLphbsVvd5P3FlSnFrX2Hi4oJTdq56--hxG9s0GlbsFP9xSpdb5wXCTAbCfip3mhDWvIvMmsTCXArduaCtZ4V2z8epjHOgZGUiYjGUihkYDdGRNDJI4dPsTgXTHihXNru6ufEvVkVguGbXZQBeiYyMKEDalCv3dEl9XaBmlH1BpSvHpxaFLdOt6jmAS9Keorcxfz0O4RjHZJ8wg023-hhBOAA6JN96U-CUpmYRaRZRNXa8THV1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/29303" target="_blank">📅 14:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29302">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBD4Zgnu2QB1gd8KzIbgmvM-yi2jV9U9J4ggG6PZes-L-KVbkevz8hUAK6IVMUrmIlJC0ADMfpeqPFqvogXQFVoKrP8HbNSMReDR9kp3RWQbQUO2KIcOeJA15nTDBM1ycATegjlXUCT7WGn230VK_dezEL30Um6kOaAog46l8g4OJCqMUMdKnudyDHVt3yUHR2vp00vAo_SeYpnmdxqloGwUgSudo7tDX-kvKLtSXntNVjc8tFZJa9-MXEfPCh0k_S5HLcjp_jpv6wklXyVW_KxCusbzizty54Nf-Bxv8CEqBt5uNKxog-CEBqYuHAZ-E_KfXb0j2odXT5C1rT7ReQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هواداران باشگاه فنرباغچه بعد از شکست این تیم مقابل تیم بشیکتاش خواستار برکناری اسماعیل کارتال از هدایت این باشگاه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/29302" target="_blank">📅 14:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29301">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d011bda7dc.mp4?token=kJNiAM59NpML_SO-F9hOBe8U-Z6MsF_rXYnrOIn4ouTUzm6PPD7jk_kdARSDz6iuKoFFqxg-0Ml_mep7d-ue8XhDrpY4LE8oLPzE2J2eJjfSLVARtPg40dc8Zc-EVHFWRuRiURfKiqw7VXtNTLLLoKaM7PrjXUBlfTBCHfLbdnQQvap9shSr-pjUr0Xlw-vgYljWSv4gBgVLGOOctl-xuArrB4qcFMoxk7q61k0cpxQLshL18v1C9h_0e0dgLYwnV-Ghi60c5yP3cRsDykLZmqEU_jltP3Xe0vBBx3tbHUl-q-Er32FR2-VDPiSzrFYRuYJ38ODj1X9WwkcMBp-f6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d011bda7dc.mp4?token=kJNiAM59NpML_SO-F9hOBe8U-Z6MsF_rXYnrOIn4ouTUzm6PPD7jk_kdARSDz6iuKoFFqxg-0Ml_mep7d-ue8XhDrpY4LE8oLPzE2J2eJjfSLVARtPg40dc8Zc-EVHFWRuRiURfKiqw7VXtNTLLLoKaM7PrjXUBlfTBCHfLbdnQQvap9shSr-pjUr0Xlw-vgYljWSv4gBgVLGOOctl-xuArrB4qcFMoxk7q61k0cpxQLshL18v1C9h_0e0dgLYwnV-Ghi60c5yP3cRsDykLZmqEU_jltP3Xe0vBBx3tbHUl-q-Er32FR2-VDPiSzrFYRuYJ38ODj1X9WwkcMBp-f6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🤩
خولیان‌آلوارز
🆚
بارسا؛انتقالی‌که‌بالاخره‌اتفاق خواهد افتاد؛ رسانه‌های اسپانیایی خبر از تلاش آلوارز برای راضی‌کردن مدیران‌تیم‌‌اتلتیکو برای پیوستن او به بارسا در پنجره نقل و انتقالات نیم فصل خبر میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/29301" target="_blank">📅 13:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29300">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCJPOi_nb9pUO-N4wIy54s4cJWqC1_NgAlaKjWpjk_F60ovf5pZO2Ln8LOppYLSM2UhJFg5YY7FqkbXwsmfDKDn-OZOyuKxTxiJWQf5WL9SED_gPwn3dNjTmVIaFKVinG4ZbT4hu2P4SBg_sPTp7V64f2h24ZNxKzZkd4u4x87M64nvxu5w6OsvL69b7_RkY5Zm_3foh4kt7Kk0tDdkFxdBXWf9S7hScT8ilWqz-krAnOxGFkB-i-zil7UvmCdP5-kyBAqkMK_eCB2rzSWP0EL-JSyPja5JTg-qi0qG2ze_GuLGdwS2_sTkgBn1y0I1ZkXbF6UuXDmffu1up2G2enQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛‌ کارلوس‌ توز ستاره‌ سابق یووه: کریس رونالدو و لیونل مسی قبول‌کردن برای بازی خدافظی‌ در دسامبر 2026 درتیم بوکا جونیورز هم‌تیمی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/29300" target="_blank">📅 13:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29298">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/npvB-ORMNXp7tKr3vk5V8Y9L6fiw8UmIqPSDy2ecDr-qvNzDl51TJ2ltzpQVYTNHZHnyKuA2IjWL-Jhb70_Tyrk4dsBEhn--h8mJqNE_weDFeQX9RVosea9H2WvrBWidWgatm7H1CDCpqfokBe2BzuhzlN5kztCO5ANFVnI1_3V-eTuJIM9FfholoTOJlQjErd9-qro9Vs5-zcgSbDMFHsjA0icm8vKweVayIXgjbC-CRUKSsQlJcsBqPJzeGZh-sAM3qOmhpkzE7AYZbGRYlEm_owTEwyY_fJ_7EGsQ6jD50S-5HhR5Vq7N0PPR3tTQWVf63LZscA1qRm8XnWmhGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kxb77cA-9qYkRi7j2ysfvBr4_VxC-P1IZM5gEjGyxRm592M8L3HDrRHG0lI8y8sy9ydWEpixk8TJ-z5eNlRQWuzvZWXosZr6j2V6zd2P0g4sKnbcNM3oT5hjsrPbzk3z_mogpc50uEHRhlDGajwtZH9aDA-JZtHO8EuPgAjx39hNZznDvOR47XiA7_3QNrIwnIf1kmeLhLUGKG3EL9UUwVCi8pJJE7wmcMQRmgd_t-4Ad-TncViAQZC__bKfRSgiriezG4GLwecHiy76ITdQidnxVQ6o6IE9UXRTGAEZPwULpfZOvGOjj2QIrR2d3ASpSrwNJ8baJVexPowtAO6-OA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اسماعیل کارتال امشب در دیداری حیثیتی و با ستاره‌هاش دو بر یک به بشیکتاس باخت. ولاهوویچ که درجریان‌بازی بااشکرینیار مدافع فنر باغچه بارها درگیری داشت دقیقه 73 گل برتری تیمش رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/29298" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29297">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyyIE0oV7ATWAmqnYtGsiNRLz0HREuRvN2MsIhCEqGLFZYaQYzcXL0AbtLc7RpMYvV1FkFc570NKXplD_1KwuFrXzaPDZOJmL8bNso_ffHBEA0ch1dl1GOXGgsj8XguIhz4phmBMH_uBNUyDogtH5Ieo90AhQB325_qTcOWZDJajvztcrmDl6titcddvl-L09yecgqsiPIOtn3IfHicOMIGySrqUKdtJZnbW4j-Payr4TLBlyxGenmaf4L4zdbEi5yzfm8DLi0kAww3ISbA16C3ee_LZ8RrU9G68cOTVtsV_VAYtXkD8K9MZPq2cvpSX8MpY9hI4hqIUnL_bFTMwDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خولیان آلوارز تمرین امروز اتلتیکو رو پیچونده و گفته دل درد دارم نمیتونم بیام تمرین اما یه‌کمپ‌دیگه‌رزرو کرده و انفرادی میخواد تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/29297" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29296">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omwyTy3ZgxH4ydfG0rSWK8cy8uwBQl1vAojVqsAJi0dqEY8zv0ouxAwSfFYQff6_5UfZ43XBNr5soQakNS-ndFqrdfIPHtssa-utJODwJzclDJG3-NKhEFRYvsgx8DxV-YWR5SboqeB4TI9-bfCgPVGgVVX5VXi3nBri7hK9Qgnq3RwvOHvrkgY6yiFOHbs_SwQVvg2VN2VN8OwV-fWTNMRqrWjv0ij41Ja4KVZagG2OTx8XIzrBsa0x08ufkDwZ2Cs8xMpgnfHmUOgaDCL4b2N0SSQ8eA6OASxORaBY9b0ybqcDKbgowH84CgpU9y2m5-vHOL5y1xs4MIqFQPeHrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🇵🇹
پورتو
🆚
منچستر‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌ ‌‌سیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
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
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/29296" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29295">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJEtlYP9YUI1NBvHOpXtsr56o2GKQwxW5BDn7ip_CZ-tKuiQn3Cxrzbhrws4JOZNCtMEv89LegQJbHPY8bijT6_2vhamACVZHGiOwJBUDrgN4G7QlWUTtLPBcX2zhl9cuYEANzQlcExZDkBEhm-sMvmSp-B_cO0ESOX6aLXUp22h1Helf_XayHMUPyyxnJj7IhrssgGPkLXox1_Zy3p-Sjk-SnnePXqU3G8XIH-OIc_tIqM6d_urFlHw4u89fmNkKIMWrZu03yleGO-BQHIRj7r5bSP_4TlwdAFfp3SLXbtGUa5AY33uu8wat0w5Y59c7sabZaMYcaNAR6JMFs-qtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیکو ویلیامز، کول پالمر، لامین یامال دزیره دوئه در کل دوران حرفه‌ایشون؛ یامال هر همشون کوچیک‌‌تره از لحاظ سنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/29295" target="_blank">📅 11:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29294">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgak10HrOXVM0zjntYbkECMphbo3bS2BzLgrbgN47Q2bhw-PBlDIo80bS5YwBQUeT8enT2kF8mikRdQUj5UCqyXCIOP9GBBUiaHyJVZ2eML4FKQBkr0SXvmf9bVS7-eidJDDnrD2ucEk-WkJG7Sn5jna4xdP2zSWaansYdLrxQ7Zgjx9dV5HFfhSPJ8LjjmEWRqO0q09gWQGFwGZ4xZFOtt_NN71oR4PalaZ3256j17M8MuQgBoAPFhfFZhpCzmBE7AUSSHlx_s7xVZzcs49uzjkkfVwTfU37kK2ADoGWKV_iPChglQykywWe-KUiWGGvhtuS-DlDemq1u0YzWJydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
امباپه در پاسخ به اینکه آیا باید در کار های دفاعی و پرس بهتر عمل کنه یا نه و مقایسه اش با عملکرد عثمان دمبله و رافینیا در PSG و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/29294" target="_blank">📅 10:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29293">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOaaiU9deyrH2ZfigMmxYJTqMVrULYegZpzsP_IlM6iQeL7ATrND9esb-pyAqnUuDgvXhhd1qJa-bI3d-du12jQvtz4W4P_FYt0iS3R77J7Q46twhSNGoDfQEYHX0s9RhoT99jlvDs6J1X4z0Z7xS9EqwRS5TZTD2HU1Hh3pag7wIjGMr1Ac_yUznrf4lxxG-Lncfgri-u3XlcfG9XwFEmLM-gVQn7Y_dqo9sVITojkL7Vu1tvzusu5tcbAtwcR4JJiQ-e_E9qnyWE3If9xu9OWe_eq228BLkmlf7GEaQBPqKrN9CZcpNCu6WzQ3Af2bEntQUiC2sVEWWem4gHSEoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
منظورعادل‌ازاینیکه‌گفت خداداد یه کارایی کرده که فکر میکنه هرکاری کنه کاریش ندارند یعنی این.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/29293" target="_blank">📅 10:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29292">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jInb9oV8PzyrlRUQ_yTak5xMQobfrEA1qIPJHZvnR80qg6Fzp5NYU0Yah9LLhoj0bTMyRUHHxIUa-jdiPsZTNX33YcaBBkMuWe3otcDwz9ibtVxFqtDuLC-ItopfxDIIndjJxqVjtkuJq9GJ42kuHSVwN3Rk47mkteYXR9NQpL75TskHvOtZ4Z2-XkMRnNtNySz9mZ2tqkxxnwMgnwOVkGTAG-WOoq90qZ-Dj6A-SeHtSehX03JEdOc-ZU5zkXn4xMIO3LaFJSa0qtNb_jfkpH4mOjZhziXBAiND2-zIEX85b_o-dfJhux-UKBcEqls7oNvbNcMNuHWH0TiTPyszpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دنیل گرا مدافع‌مجارستانی پرسپولیس به مدیریت این تیم اعلام کرده با دریافت 400 هزار دلار حاضره قراردادش رو با سرخ‌ها فسخ کنه. به احتمال فراوان بزودی گرا فسخ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/29292" target="_blank">📅 10:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29291">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPGHge9v6PpQDyL2LFZoNJTGpphZVoH4OaYRJI_WdhZy27VhdtAfoN4E8C204Qhk3IAb3X09L23VqwhQYBpdLW2PD8IphdY183gnOAMxCN_eKUqyexvIvBTPfYRvORuNliIhGQOiIuXkZXQ915RBy2wgviULRh1y_Bsuxs8Z2knpSOta5-pZMm9xrBDfBBa6Y29gXUW0q7-UBTq4w9a961AvoAJAJ599NKvHW9mvI-5ElTFiMD4FVnpYJIMQkC0Bb7aS49_1okcjMPN7smceDog2h7CBLqvcYLXlrHqapmBNNliu5-T7JXOygP1OZO6pXD2LGxxxKN62ewCXslo65Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/29291" target="_blank">📅 09:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29290">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bO9aBA4No5IEOFgHswleRFpQpoile52AKmtyMYsqm5gXdbFIrwJWQUuAG0SlQ63l_atyaOC_fAlk-ypu2fV7CcoCufCCmJqkaQyTUwQrpOJNFA3MIxVWcFUYocYZhQybHRhQohhO6flR7zwzyuyuXFX6FNHbpjAY7G7sm8bO22nJy2_UApSz44k8Kb_cfHgyogMVzACAi5xDadNYTqkuqYUtMs17s_0Em8SmFS_0tz3NsavATPJZtMU33UoXlZqFsdWv3ch9F5Ofl-WsMMN2SC4lcrXJR4HQOycCknzywM1DPjv88LTY6lbhqjZICkqGSmgtHiCtKUZddzb0dZZ4dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/29290" target="_blank">📅 09:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29289">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔹
👤
ویدیو کامل ویژه برنامه جذاب امشب عادل فردوسی پور با برسی کامل اتفاقات این هفته فوتبال ایران با حضور دو ستاره جوان فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29289" target="_blank">📅 01:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29287">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ig7dbAWluVnBqrmsd2BhSn78L1df2-M4Xqm_jbo02rWdiFRtxfva83_GDl9pXc5mFWKETG-ozGs7I_bq9e2cTTfKk53kHXJsixFpuGlqJ5CZhECC-YTziVf6EcpUEzm9EjT22LpIseWERQAvMnOOzz1l2F4aBFqUhYWNBHr7dixQL37xFJ08KRuwiyw1xqz6k4RsUC3EYvcHngB1MCaeBWMiUuqEQUCytykZ8bu739AsELcfjAq8RmLh-kr_eVNz4VIC6sWrCaEjptWZxvtmpAztTRE9nXaZWd_Rl80lWIuGUtq36uV2XbqkX-FgqpbOHSfG8VL96LcvU_rSRIpSiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌ دیدارها‌ی‌‌‌‌ امروز
؛ آغاز فصل جدید UCL با میزبانی کهکشانی‌های‌مادرید از تیم سابق آقای خاص!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29287" target="_blank">📅 01:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29286">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prRISydCrGW-yIRv8sqRsQjNKvSS-80LA-oygw9zpXVqU2emTYEp40AlqcpDF83T3eGRv8J9SFIAeI7Ea9C9Z2e_E2-ParLD_fx718AIgAjN1J38vfmwgNWmGo5_ejZKjRLtCuQymqsnMk2FcqEZqTs1OID2A4x1gHCwEv7bKjnHXIkuB3OFnVObMdVMv9cz7nDyCk_gLR5yYC_TICS1BCHyapQrGc8IeafYplrwdN8_BtaOu2fC8FPsWCqFTEwbNZ2hL86KUr6XDBu3_niykSY4mhmS7cz_vgZuWQJ0a3UItW4qj0V4WM5p8Gf23DGyUJxgOEEuPP-wKFzGSrfM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
برتری‌ارزشمند پرسپولیسی‌ ها مقابل ذوب‌آهن در پایان هفته ششم لیگ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/29286" target="_blank">📅 01:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29285">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-Mtrjab160LLJT04DkgcJKn4vHRRBE2ai_nd-zzMOg8Ql-UaALpgSVM-TXZ1a6dxhz_6fetH9tY9ffiqIlZn5LQDqca3OSwGufUjzfUngKs1xM7JJDRLRYkBRUdM0Sy5bSF2CmFylmO-P0Q-v070bQm2IxgrTkYgUjomuCgcxH8HUSd-7mFYF9HAJvSPx7WR85QgaGmFnqD6lEynkrQM8CNsZnodLJLLbgtcTlZl6eBQFNO7fP72wsluvWg2wYsDknvTYSiMnL1UQRwrFcHrCwyBGy8RnddWVx9_1R4HOTEcXiqu2fhIgCJEoZECYENUyYQREAq8eRuKRMsgmHibw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیریت باشگاه پرسپولیس بزودی‌جلسه‌ای رو بانماینده دنیل گرا برای فسخ توافقی قرارداد این بازیکن برگزار خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/29285" target="_blank">📅 01:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29284">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQCQul8tfod6MqiDN_vYbGdQI6Pw0X6b8ZXMctyZ24DXFNULlSuDmS2aaArsH1eAJJ7es-FsCT1HBaCXlfeV4SCow8nux7CXT-wAXHlEFOF85Z2x5IXIHOa5Di_GVmqimI1pCZgxXg4vagIenLYm14KkqRxNf2CASD1C-Fe_DtK07RgPa-lP2FwN6EFw2qqXSmkSz-aGmuFpxzlCn2FN57xyeGFzQF3iz-iXcUqxZnhnsDTDS8cifD2n5sUneYbnXLf4V2Mm_eRzCpu8-pJMABujnU8I0zs20aCmvSzVm4Uz24N8-sA5AL2rnjjMda9D2gcRWwlLcpvKjB64qDUMrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
از پس‌فردا دیدارهای هفته هفتم لیگ‌برتر شروع میشه. تراکتور دراهواز به مصاف استقلال خوزستان خواهد رفت و آبی‌های پایتخت با پیکان بازی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/29284" target="_blank">📅 01:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29283">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c1c191903.mp4?token=BC6qG-D58NKl_4-dj7Amp8lQkSGZOdBXBFkURalj_0JzGgEFpmvWDfVX8G5A1jNugWKXCEFWXfXrr38AVddYLKf_Pq4JwQq6jpFbhACFjGmJHhbJ4NxQuR2vJ_DK3BRX8F6IDGxUQdoyXhRzaBhsngrow6XMpa4FuvZsF-fkHjvAj-iUdmzcq8svszzUMxQT4uhtcCzFgpN9eZOWtXM6IOB6Ogy4XxHtAn3O5oPzad6xXp-5tbnTKEOoRrqYC7HcfvOMRgzsL3aTqNHvZsOSLZARDEaEExXRoDgUNGN35s2baPCEUfOPCzJX_z0g-lQmh8ecZZVs_dOvWVYWWR9bwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c1c191903.mp4?token=BC6qG-D58NKl_4-dj7Amp8lQkSGZOdBXBFkURalj_0JzGgEFpmvWDfVX8G5A1jNugWKXCEFWXfXrr38AVddYLKf_Pq4JwQq6jpFbhACFjGmJHhbJ4NxQuR2vJ_DK3BRX8F6IDGxUQdoyXhRzaBhsngrow6XMpa4FuvZsF-fkHjvAj-iUdmzcq8svszzUMxQT4uhtcCzFgpN9eZOWtXM6IOB6Ogy4XxHtAn3O5oPzad6xXp-5tbnTKEOoRrqYC7HcfvOMRgzsL3aTqNHvZsOSLZARDEaEExXRoDgUNGN35s2baPCEUfOPCzJX_z0g-lQmh8ecZZVs_dOvWVYWWR9bwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ویدیو رواصلا ازدست ندید؛ خنده‌های عادل وقتی عضو هیات‌مدیره‌تراکتور کلمه "بی ناموس" رو به زبان میاره عالیه. تلاش کرد سانسورش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/29283" target="_blank">📅 01:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29281">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7672fe1ae4.mp4?token=pPCsFgbKDQKqcrE-9aLTEdUK2Oq34a4ODPjVsiuUDWx8hiwPFbscUoh2NIm0JqVeauQm4oukVQK8Ct6ho25HA6m_Vs55jZ5Df0KCK6y5bjr-G9OU-Eg_Hlpfhs955oSriF5Q1QWRzDNEDbsh4ajPh9ija07jSjNGTJMj9FzZvMIHQST7wj-NTNpvg78bQ5MtI_XZ1yfw7eWTDfwZwi94OmDKJQa0_AwgieyA1sOgAe8IhevkBKGDXbp2iKZ_HNhVJSObEUDqyn-fxIAHxIxstiyEEpr91MFfJOQKn039gWVDfRT9Rt83PkPbN4rZsZKcAX6oU1l286YJ3J-Ziehsrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7672fe1ae4.mp4?token=pPCsFgbKDQKqcrE-9aLTEdUK2Oq34a4ODPjVsiuUDWx8hiwPFbscUoh2NIm0JqVeauQm4oukVQK8Ct6ho25HA6m_Vs55jZ5Df0KCK6y5bjr-G9OU-Eg_Hlpfhs955oSriF5Q1QWRzDNEDbsh4ajPh9ija07jSjNGTJMj9FzZvMIHQST7wj-NTNpvg78bQ5MtI_XZ1yfw7eWTDfwZwi94OmDKJQa0_AwgieyA1sOgAe8IhevkBKGDXbp2iKZ_HNhVJSObEUDqyn-fxIAHxIxstiyEEpr91MFfJOQKn039gWVDfRT9Rt83PkPbN4rZsZKcAX6oU1l286YJ3J-Ziehsrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇫🇷
کیلیان‌امباپه ستاره رئال‌مادرید:
من بهترین بازیکن دنیام؛ و با اتفاقاتی که این تابستون رقم زدم، حس میکنم امسال سال خوبیه برای بردن توپ طلا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/29281" target="_blank">📅 00:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29280">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/932bc654da.mp4?token=mGhWRW-jQCKSr81aZ13rLeGqNSP0QVHkq65650ahSH-fhAj_zoKTRyjTqMw3cUGdNPJsufAU9QaZBXTSDHBF3uw_sGZ9icfe-bWYAFdnOnRnTlbEofzM7tpM5l7mbvdaH7IU3HM8STzFgUzK0mlbXekOzsVWp_FJDBi8vxccbvYfCMM8P3ucw9PrCmtL_RL8T3TcZwKS924_0jpuEop962jmOwiRnGLhgxoon7dAqNpLgBJELgNEjWrPBVcIAxjCRwF4c0VUK_-m9c2cRzt1awu69Tj5ERugBYjLAybRV131BIwYE5HgeCMvYmGTEe_D6rJQLk2VKksQCTv8hmBFKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/932bc654da.mp4?token=mGhWRW-jQCKSr81aZ13rLeGqNSP0QVHkq65650ahSH-fhAj_zoKTRyjTqMw3cUGdNPJsufAU9QaZBXTSDHBF3uw_sGZ9icfe-bWYAFdnOnRnTlbEofzM7tpM5l7mbvdaH7IU3HM8STzFgUzK0mlbXekOzsVWp_FJDBi8vxccbvYfCMM8P3ucw9PrCmtL_RL8T3TcZwKS924_0jpuEop962jmOwiRnGLhgxoon7dAqNpLgBJELgNEjWrPBVcIAxjCRwF4c0VUK_-m9c2cRzt1awu69Tj5ERugBYjLAybRV131BIwYE5HgeCMvYmGTEe_D6rJQLk2VKksQCTv8hmBFKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چه‌دردهایی‌که‌ بافوتبال‌فراموش‌کردیم؛ ویدیویی زیبا ببینیم از یکی از زمین‌های خاکی فوتبال ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29280" target="_blank">📅 00:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29279">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQkjXTB364Xx2QDRLraocKFY3jDpOhvabPdoLhNJ-0pqv3l5t0QJai89Vy0ezgBWNQEUzdDhHmzkzaxk7PR3_NirN_j7Zkx4gzX3K1rk91qzvGTY9wbCQ5tB3nI5Ni0gi3QX1f-WQICimX8oSaEc84xJjvCCora04WT911Mwgfa3YtXDcbkMT_jexF4aV_C3wum6eVO7bbBdq_qLU0g1Sn-A0CPONhOwkSKzsnQ2oPgv0MIBulw2TjAks9SWjGtOFDV18OxaJe21Kvv0zgOAwfsm5gqOj2p0rCmFp26u2Q2J-cRcR5JLAAZcbAQFWCVapOv2pdtt1rJKzX0hpNpvyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه نرخ بنزین در جایگاه سوخت به این شکله که در تصویر مشاهده میکنید؛ نرخ سوم که بنزین لیتری 10 هزار تومانه از 12 امشب اعمال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29279" target="_blank">📅 00:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29278">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHMoMtx1yij-mJb-O750eGXGyF6ZEUyKunIV7xMAQ3lR28bGXLciYJU88cbTybpBJ_cGmDGl2q2mcGrSG4ascDC7AMJUln2ubjd8PESzovmw02-ITdupNhKstzsYm7IKaudXT_t7We62pbMg_2_ADQvoVPuIAz9_h_fiy_VHGGZGRPxTLjHwkddVulqSuiFDQZUZNWLSF4DVLdPgaW678Z2EyqU1jwaD30ke6rqg3qv1B_Cmfq5P6j2iaCSjjssROEFJqlB3RoPfIdg8R5KTASXMLKuQ7nKNCCiRH8krerLSnziI1xZjKm5NCSvNA49w-G-boU5XakIlLT5O711_4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29278" target="_blank">📅 23:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29277">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7tqExHdZUtsZtV38RBPJ0TllujqxtTyQ6zYdtXgsuu0teIq3XPIU0yMUwv4zmX-g1XsRFqkiTdTlD9HJ0WcK0lk0uhZsmt68RYj96vCNAYe0mtR12_F8GmCTQpYGb87hABTr8I4f-P-DNspdRsQnsT-73F6E8r5YuhStdHd5qrRSWqRx5HvO_-SMjgql_t26AbOEAEkFALgU8B28jOZmWyBUHcuE0eZjjVtvMGJWF4GqpbXbv_FkoDiV0bMdCj2zTMRafG0fLgr3rQy9wR0GGhz1VaRY53ZymOrjjRf0G_nf2-CABfyWZCVO5aYPzeNpAl_L1Pf1NujV0ze77bBHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی‌میگن‌فوتبال‌غیرقابل‌پیش‌بینیه یعنی این؛
الهلال اینزاگی امشب با تموم ستاره های گرانقیمتش همچون مارتینلی و واتکینز اونم در خونه دو بر صفر به‌تیم نئوم باخت. حتی نتونستن به‌این‌تیم گل بزنند. نئوم تا پایان هفته ششم  دومسابقه‌باخته‌بود و چهار گلم خورده بود اما امشب کلین شیت شیرین کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29277" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29276">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bb9f937c.mp4?token=ED8UtDrbDDt5erE1MJz550eJ_cLmkp94SFlZfnCMrsxLHeOFwrEiAQB05waobPHo-Npp6osDfScm7ffCyL0VdUxj3C1hKr5AZKMc-lZ8a_W2LDVon7lOTirCQtJi-788e2XVa6ZmFr9PK3dDrRpx5BOLAmfq76_nl-4LN822CwzZVVHtvUP2NqVILPJ7KsF09Plv6VyAdSmQPM3RW6zw4ha2NhPiETgNMovvkZ8oU08A70VpYmviXkzT8xB2c6jIKnoc5HIfRieA-BH2Z6e81CE934ZVv9F44wV4MftjLQn1w2SjYShp0Sl-bbqdvJ8MlLgz1ef3qlVrDu8lF1zfyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bb9f937c.mp4?token=ED8UtDrbDDt5erE1MJz550eJ_cLmkp94SFlZfnCMrsxLHeOFwrEiAQB05waobPHo-Npp6osDfScm7ffCyL0VdUxj3C1hKr5AZKMc-lZ8a_W2LDVon7lOTirCQtJi-788e2XVa6ZmFr9PK3dDrRpx5BOLAmfq76_nl-4LN822CwzZVVHtvUP2NqVILPJ7KsF09Plv6VyAdSmQPM3RW6zw4ha2NhPiETgNMovvkZ8oU08A70VpYmviXkzT8xB2c6jIKnoc5HIfRieA-BH2Z6e81CE934ZVv9F44wV4MftjLQn1w2SjYShp0Sl-bbqdvJ8MlLgz1ef3qlVrDu8lF1zfyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی هیات‌مدیره‌باشگاه‌تراکتور در گفتگو با عادل: عالیشاه به خداداد‌نگاه‌کرده و گفته خفه شو بی ناموس. فحاشی رو بازیکن گل گهر شروع کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29276" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29275">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba75a2423.mp4?token=EiPaP7trcOQCZt1c2MmavA6DZzOzWHI4_uI_Sz9vYN2KrGTDz17_D8PXgmyHH28TcjZ8bD3l_GmocF7FcuzUug2wVsUjsMslzS-5eYkKCfJ-wSEhgvakDWkhQbbKMCq1G_rbvc93_KXAJAts78BezGHIRxeTQtnBi01329_FZ3IciOw-VPwvCwlBvqU0ryWjxqalJEreZtA_bWPqQXgQ5w3YsYAy6ZA255P0bZ-K0prvbUamcJVE173X8rn6wVy-nGtJ-4ios1AvX1ZQ0bOD_ybHsdP0ykyo61sGTMG0YQgxvC3RTpR0jWii6ZaUFwXujnp0Qx-J8ylQfbG0J2ON2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba75a2423.mp4?token=EiPaP7trcOQCZt1c2MmavA6DZzOzWHI4_uI_Sz9vYN2KrGTDz17_D8PXgmyHH28TcjZ8bD3l_GmocF7FcuzUug2wVsUjsMslzS-5eYkKCfJ-wSEhgvakDWkhQbbKMCq1G_rbvc93_KXAJAts78BezGHIRxeTQtnBi01329_FZ3IciOw-VPwvCwlBvqU0ryWjxqalJEreZtA_bWPqQXgQ5w3YsYAy6ZA255P0bZ-K0prvbUamcJVE173X8rn6wVy-nGtJ-4ios1AvX1ZQ0bOD_ybHsdP0ykyo61sGTMG0YQgxvC3RTpR0jWii6ZaUFwXujnp0Qx-J8ylQfbG0J2ON2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29275" target="_blank">📅 23:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29274">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBgkVgHf2XvgSfoYnc8CWBy_5GLaHZG0pijsZTHoF07ZHhWJxbWz5i7dmNfTCx8UTw2zaxonhmRuqrBRabna5jLRewd0ja9Bda-_Ww7fqYeFxSJadBgnNXn9_Uyz0eyReVGskVg8SNLJJ3v9Lwemso4J_n5kKWL-jSVAiHpD0Yqrgisfcn2UrB9-Havs1uciG6Hbs36DYTh4mLJUWTn_FW2Z7v2Fojq1Xm168gBtfeYdQ7-Xv0crHlQjl3x0N5ZBmVfv15sTnMF4NGqiy1ERwko8UzqmZ7xAGugUM7Lnz5e4h5mpaGcIQS7VQcYD8axT30KBvfBjbXjeJm58csTpoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگارشبکه DAZN ایتالیا که روی برد اینتر در بازی با ناپولی شرط بسته بود و 650 هزار دلار برده بود. پست‌برگ‌ریزون ریپلای شده هم حتما بخونید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29274" target="_blank">📅 22:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29273">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuodZ54gXhxJEq3fX6Y1laKsUHJg_ufhQYKUsHOvmSivTxF8vd2-GEGD6hwgw8ay6cC9-bBNjY6a58JsbW696bn3AfVRX-yiZlN54iiHOcu61f8HbbhHXLTKpfNw4mokurmIExxRRXMcqJFqih-RoI3hAGyQ81-PDTYlsH1EXfAmeBO-BAH9M7FZ_aTzSwbuKnN5QgZNmFMRFew6sC93JEA3SQz5BB_ZihTmL8dxbHsTUtv_oTcuEXZ3GRbiag8cEiXL0BrPKVwcpkF_iSklw4IjywH9d_WAtT2bUHatVEMObmV0kbvldJ7P3ksU8QRaMgul5360xhgzXL-1rQXviA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تایید شد؛ با اعلام کمیته انضباطی؛ خداداد عزیزی سرپرست‌تیم تراکتور به‌دلیل فحاشی به امید عالیشاه چهار ماه از همراهی پروشورها محروم شد. عالیشاه هم چهار مسابقه گل گهری‌ها محروم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29273" target="_blank">📅 22:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29272">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">📹
خلاصه دیدار امشب دو تیم پرسپولیس
🆚
ذوب آهن در هفته ششم رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29272" target="_blank">📅 22:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29270">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hjPFfdiVus_robR9KlK95LSvbn5hRunptDKp4b8TGrrouctz-onedL7ne4rNv0S_S5o3kjBOahRs10cMOvwiKDzaeO_it870tVlFBQfaB4jGTnIaLq_lTc-6U70tVZY_khS4nyeSpdsP_94srz6x2f-UyWvXawPtSCNGjNwx1-K2itEyj9fJUdYCk46mvUspI-YdPgmxplOp535YdQt1mvqsuYAklf6Y19jZClWJ9RvdnRSgS--Tl97sQsfv4nVzF4XbQyfh36Gqzf_T4N3gtou0-9RGaEujqSEea4DPfhv1glFyrhZYFoXr6oUQy3NzblKtzX8atwd6kofKlOXm5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r7eU02SDgtbckqd6G5n8hi8Tsf6FtKXHk-051RbvDV9d-I-y0y7RVYN7Ptf4IpZCB1bjOqby5xBeX5bOKOB8qJP8GYQCJ0IjJC1pXPmW_tEhP4Qccf8S8ZxZoRH6hamgESabo3wZOUW9_TfsjeHxFXAfixGXUJ_Sb3sAAFdW7TJK50THuOjwQTQJZ6C6QxQdM8qcQBGYFgewwIx1RnfBw9vRTFwsCI3SFMdtUjDn8PoRU3UfaKWkKSMelzSJqZ2tteWoL9J1TBm5kFGqf45f4JdZTzUbDOy-U8OLUVv_JVyHo35zuT8PBa8RsyO4xT3DOpiQ9O4SarmetKf4MGaKFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌ششم لیگ برتر؛ دشت سه امتیازی ارزشمند شاگردان‌مهدی‌تارتار در دیداری‌خانگی مقابل گاندوها.
🔴
پرسپولیس
2️⃣
-
0️⃣
ذوب‌آهن اصفهان
🟢
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29270" target="_blank">📅 22:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29268">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dzN6GASkOoxPsUfuT0MleUyB1Q0PlrZdSOZajEg8u83YYQH4QtbF2lnZxRHN5CMezfuviXQgJymhPQAZ2M8WQ_pilOcaYsnDVVtZCZNAdRgBIAb0cEPeQh76in4JZgS3WG1HHGQtz-YoiKtDJ-7d-YCsR_yeO8JYVUmmypok97aRlLYGijBSu-1ZCxXBS2Ge31qmaTEiUYPSbUa3zLcvRhsb24AfpHHq0EgW2GeWCFE-HPo7iXXYFAMQfj105Prv3ZsYWD1CwadrDKG_QLTM_qXdDLZBrq0lGgX_gXYwvCrNJea_m3a_VN2ZqniD1LH9Z5TDaDDAQ2XOikCmi7kg4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fM7-8zrNX3QRtYqbV9nPh0o4xCxW3RSli2GKIg63AllWs_ExirIstq0gfJl8jjT1wJODqOOy_pxKsjHh0f88BwzYubbLMwz04_jVRUylyaAd5IMoYuYdze3uuMl_OgMPh48U1j_iSLryZvgRFPCxy9abLUjgtsaLQrdJDHXvX-Qy4XbY8trkEFb5u9EZTp86J5SgqdNCxPOUDLkrMHR97eO1Hv-HbaG5ayfqSFaAgL2kax5Y39pUT0j9YUbP3h3B2WkVi_GLvvSYj1eRpvkM3Gd-rUMZkizWJiA0BhW0PmcZnKLes_i5bHEjoQM9MRUJOCcaXPQ8Tfm2hN6pAPWwGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟢
🔴
بانوان هوادار تیم فوتبال پرسپولیس در جریان بازی امشب سرخ‌ها مقابل ذوب آهن.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29268" target="_blank">📅 22:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29267">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93952feaa3.mp4?token=bo-VZYMwYYWDMS5SKyY6HVm5njM1PvRHNyK2Xu3pploKwM_3ZMisrTJ9fj2mfdQBo1jojjUh1JJu55j8r3PpmuKrjLNsNg-x3oDw0sa770siRITeOPc14lo4s9ez4EC09-mGX1EGMLVN68J7b2SHL2x0NarNqCmiS_nTU8vHVTiINTcWxfuPiRURyVRT89ZVcMlM4cilUZaS6SvwxKZuYWZzm56P4FOKuJnN7wuxztzaWZWTZ7zk9Vt-Ly_CCD-ReVEAAPU3rhekoHjelt1ItqnSUoahAvGwzH18qpGbhbRDh2Sq1BpNq70u7TskCsm7eGYRDK-qhbh4SJkFjaj67wSbNv3aYFpEobJ23aU5Z2bMQjSjIJv9aVebLyu_ajzzNtkfng73_ZTT1QgBZRHJWfgTEYEzcPrW1iray8qsV6UIGobWkYSO38kAVFvqUct1OCYJfjN1yxJp1WveyxfUhaY8cf21juKYtjThb2xM1fiKt4UM4YjH5b322dwpOLuXynoSM4SEJs1Cwr38S4pqJcmKw_HEkftoq_QaZKBRGon_1JkMyzXtL6mpEcXUxKLIaFc2jbM0DGzjR7eBzFm0aJYd_nzwGeVLfHe_BrXNjJnJFwoxWP0prN9FPym_q1C219_mLYCsQNS2q9WzwExYNOWL_vVHYIKEImvBBa0sdU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93952feaa3.mp4?token=bo-VZYMwYYWDMS5SKyY6HVm5njM1PvRHNyK2Xu3pploKwM_3ZMisrTJ9fj2mfdQBo1jojjUh1JJu55j8r3PpmuKrjLNsNg-x3oDw0sa770siRITeOPc14lo4s9ez4EC09-mGX1EGMLVN68J7b2SHL2x0NarNqCmiS_nTU8vHVTiINTcWxfuPiRURyVRT89ZVcMlM4cilUZaS6SvwxKZuYWZzm56P4FOKuJnN7wuxztzaWZWTZ7zk9Vt-Ly_CCD-ReVEAAPU3rhekoHjelt1ItqnSUoahAvGwzH18qpGbhbRDh2Sq1BpNq70u7TskCsm7eGYRDK-qhbh4SJkFjaj67wSbNv3aYFpEobJ23aU5Z2bMQjSjIJv9aVebLyu_ajzzNtkfng73_ZTT1QgBZRHJWfgTEYEzcPrW1iray8qsV6UIGobWkYSO38kAVFvqUct1OCYJfjN1yxJp1WveyxfUhaY8cf21juKYtjThb2xM1fiKt4UM4YjH5b322dwpOLuXynoSM4SEJs1Cwr38S4pqJcmKw_HEkftoq_QaZKBRGon_1JkMyzXtL6mpEcXUxKLIaFc2jbM0DGzjR7eBzFm0aJYd_nzwGeVLfHe_BrXNjJnJFwoxWP0prN9FPym_q1C219_mLYCsQNS2q9WzwExYNOWL_vVHYIKEImvBBa0sdU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اتفاق‌عجیب‌پس‌از پایان بازی امشب دو تیم ذوب آهن و پرسپولیس؛ اعضای تیم ذوب آهن به خطا روی بازیکن خود درمحوطه‌جریمه‌تیم پرسپولیس معترض شدند و VARهم‌صحنه را چک کرد اما داور در نهایت این اعتراض را نپذیرفت و به رختکن رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29267" target="_blank">📅 21:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29266">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlbJMxlor0VYGRh_ChBqhmEbOH4uOy8HRGCHXoypK9fAFsC8W2dDI8VI82etVBf46TueVsrWg7BROCNdlKDP99p5zBxVLaSfCqzg45zkTUK_ww2nnIMdFQ-nkM1U8EaVkczGt-BIA5OTcgdwJWTthdaJWi_SdW2x_49VUpVchiDREtAw1zYof2fvmnUYffnWLvlFrffL0OjeCp12y5pEm_-GQvX-fyUBruKcYCWEIeMkfZnHzsN4kB9yIjnAi0Z5mULjiC-x8he4yDQZ3W9CNlzMABm0GZgt9__cQBpX6IPtAhJl9FOjLeV9qYlWc7DZIplWLFcv6jqj3OJO6P1LnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛ یه‌پسر ۱۷ ساله اهل مکزیک بوده و بعدِ اینکه دوست‌دخترش گردنش را مکید، جان باخته. شدت مکش به حدی بوده که باعث تشکیل لخته خون دریکی از رگ‌های گردنش‌شده‌ست. این لخته به سمت مغز حرکت‌کرده و باعث‌سکته‌مغزی‌شدید شده و پسر تنها چند ساعت بعد جان خود…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29266" target="_blank">📅 21:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29265">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcFeBaf6PRyRKwAeJd6nj1p_D2SUqJuDYdbBQ3pphHs9D3LfcIPtbc5znAfxKuzT-xE4rCPO9DFB96aiqRB4EJVv4ie_Py3M7aLGYpNRRWMYS1OD6BMItHS4I1qG_kx-UIhAqQ3rC7RIe_ZwDTL5DLd4wupqMT6CfLXTCY-9RJwiTQRJQwVLTue_d85TZMHLsIaIH5jpCciYltCLpGo0gHV8ZHms85Cfc_2kfiRRNo-ywfk2KTq6LmLZAROg991GZkuADL-Xv0Coi3dDAFHLYA2XP6U331DSdzOGviS7soZTaYGhB7QJhDun35cHwPMdoI26X4wcWfSues8XpSa6IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ایساک کونده هافبک‌شانزده ساله لیورپول با عقد قراردادی تا سال 2033 به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29265" target="_blank">📅 21:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29264">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f001dc45.mp4?token=gQElSuWCTm7pJBhSXn8mwhhONsUeavficUW8AN1xWXZlTByNuo-d_X7dqGHczku5_zFvyyiyC14MoN__HCtPc2if--6SvXPAYEVHUEACmk8BhQAgY7npTGXtTkqc76S9UDFj-Bhz3ZAdYrmNg9tiMT5UkZv7xIgH5d_piUb1UALx-LwHVX1KRVVtj1ZA12Y-aQbWM2V97ZyFV9X2C7twC5EPfOyxDt7sVEG0_5U_2oKVSAvIiP8C4j4NtFTL2QdbtJ_cl9d6pgrbXfGqwreO0baExJ82thacRK93qrg4mUHIJrX4DVNBC9UsmhNObVBw_RKZyx9Iz1Ty6Nkndw3LSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f001dc45.mp4?token=gQElSuWCTm7pJBhSXn8mwhhONsUeavficUW8AN1xWXZlTByNuo-d_X7dqGHczku5_zFvyyiyC14MoN__HCtPc2if--6SvXPAYEVHUEACmk8BhQAgY7npTGXtTkqc76S9UDFj-Bhz3ZAdYrmNg9tiMT5UkZv7xIgH5d_piUb1UALx-LwHVX1KRVVtj1ZA12Y-aQbWM2V97ZyFV9X2C7twC5EPfOyxDt7sVEG0_5U_2oKVSAvIiP8C4j4NtFTL2QdbtJ_cl9d6pgrbXfGqwreO0baExJ82thacRK93qrg4mUHIJrX4DVNBC9UsmhNObVBw_RKZyx9Iz1Ty6Nkndw3LSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌ششم لیگ برتر؛ دشت سه امتیازی ارزشمند شاگردان‌مهدی‌تارتار در دیداری‌خانگی مقابل گاندوها.
🔴
پرسپولیس
2️⃣
-
0️⃣
ذوب‌آهن اصفهان
🟢
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29264" target="_blank">📅 21:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29263">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qohXO_p7WW1irmjSQ_4n4TubYOyqcYl6FhaBZVu8B0XgvSWbWaoQB9vwR2Z8mBtHaVPrub-cGy8FBpIF1q2qMhSIl9hf7ZMRPkRqWZ4fdvw3L90s_uIkm3siVto9DcDAu_oHHFD8_JMG7IkqkISNT1iJgzsjOw7L2hhGu1Nfs2pYwRSFTd7QVtnsPn8QWH2zd13HjRvbaARzu6qeFhyREdL22yb12fW179JeGH3A6q6LNzysJix521XOiWObxpnKmio9L3v9qLV_YHv_3mII7sTchUSfPOjlBk1Y-qOs_aiYqIADELdS3wLJyzGKVlRNsbt3Er40mpDuw64BZ5b2dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این‌بار علیپپور پاس گل داد؛ گل دوم پرسپولیس به ذوب آهن توسط پوریا شهر ابادی در دقیقه 63
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29263" target="_blank">📅 20:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29262">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBRdvb1fEmKbgaZvaPVsDe-PIkoGfkph0__2lLDT4wK7sxiTsF7PGkzveG5Bxtd3Z_2fNrKgCKSVhiF6oUoaR_ysdS0RpyQu1zQE4P3cgLorXfdXFDWUgoNTPU-TtLnYy8kwf_bRoG-rYeLz4tS7zHTGF3CYztp-mSh2r7bJSgF1hIFQDxenjSHz0OYfQu0wehiylxzT-BDuSf0oMUC4X9ESGu_cnO_lPZi2fJTFkpDp1hVX0V0pLN4de8iWp4SaXCvVvDitFWXEavfBMftzxQ8zQNOtcJKdImJ8czXnOOyL4ba9ZkusXiMu6ijwU0P5rUyYAHA148tMKl3PHkat7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این‌بار علیپپور پاس گل داد؛ گل دوم پرسپولیس به ذوب آهن توسط پوریا شهر ابادی در دقیقه 63
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29262" target="_blank">📅 20:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29261">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a13ac35bb6.mp4?token=PRYi5vJV85-Sm94TbmpiVsF2mNjuUdwDQHBXbwk2AeNpwTLUevB5j6toxEx6_QgLMyELg9KsjYOFgtpg-KD2mecAFDqnuDg-pIjHqONNcqL7uVsDcnQPHfFfpJGXRC-OgF_cVhSKCFemauriV243w0D7NDApoa7_oXpEveXXmX_MvSl6UWNzP_lFtXeig1tpPYbkEVfrEvpHua3a7Xw0bGYc6H505-TVQ_fYq9WlIMYuK57X1kZFRn4wEV39RsMF-Le73ivPeyUH98XUODRUNurxgPk-1nXA4wxmmlcOrzB22QP_MuZjpSyOoo-W0iux313zUmczSKbQGeK4K066pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a13ac35bb6.mp4?token=PRYi5vJV85-Sm94TbmpiVsF2mNjuUdwDQHBXbwk2AeNpwTLUevB5j6toxEx6_QgLMyELg9KsjYOFgtpg-KD2mecAFDqnuDg-pIjHqONNcqL7uVsDcnQPHfFfpJGXRC-OgF_cVhSKCFemauriV243w0D7NDApoa7_oXpEveXXmX_MvSl6UWNzP_lFtXeig1tpPYbkEVfrEvpHua3a7Xw0bGYc6H505-TVQ_fYq9WlIMYuK57X1kZFRn4wEV39RsMF-Le73ivPeyUH98XUODRUNurxgPk-1nXA4wxmmlcOrzB22QP_MuZjpSyOoo-W0iux313zUmczSKbQGeK4K066pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
روی پاس هوشمندانه مجید عیدی؛ گل اول پرسپولیس به ذوب آهن توسط علی علیپور در دقیقه 41؛ این 96مین‌گل‌علیپور باپیراهن پرسپولیس بود و باعبور از پروین به دومین گلزن تاریخ تیم تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29261" target="_blank">📅 20:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29260">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSVP_i9B0W_HlHJ129TsBwrqRyQxtdzYfE6Buf5k1_uBV3O1GrkCsNIlw00IGKRfIut5n-rcy-FSrBjaPr6pMnEwp0gXXNzR3842AP1kiPkzkAQqaWLDtvddV7Vgf2XpThMOxvHdZkSoaCbpbhmYEgGUSY68WDowMyaZ_WGrQBFFYasJ-y7PdPSgQdhZNDhm-mLVnIkw2DlndbNcKZg_lIIqTojmdykvs2j1ijxNEfrf1epUSLrHHASY-qPA3crWVb7UdSrjmauaZcqt9F78LZ3zFV6BgwWhY56MUndiq7zzETWyAX0jDlFT-O6mFbT4CpaD_TkaAITdYaIKjnP2Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
درپی‌اتفاقات‌دیشب؛ به احتمال زیاد خداداد عزیزی سرپرست تراکتور دو الی چهار ماه از همراهی تیم تراکتور محروم میشه و امید عالیشاه یک الی دو مسابقه گل‌گهر رو به دلیل محرومیت از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29260" target="_blank">📅 20:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29259">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f02306a280.mp4?token=IJAX4ImWsHALOPz1vcLjB90uHGNrPSpbUdFJHl3L1tTumGVcewQgC6mTXxjRqE1tvUjs7tV1acFrTlMXkEQlP451aaKEb9ZaUkSLEXS34KvlTl2HsDTtyD9aOJXtXtIdoC8SxaMJwMpayGarebhS-bsbPdRsngMB5MmoNGTEivqewdGNGc6vHH1LSPhg-Qwav2eyai8G9SFypxGEElqxxlKBd5bI6DsjPULb7KgW4AKjhWzDY1ocdjGS70b0zaHjC2_R6uh-XyuTA3_rvsCJyeP0FVk9HXfn3cmOtjnxaJk89V6IbLyclYZ3XVib8VU2yFiop8dDkScM7l0m1cCYMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f02306a280.mp4?token=IJAX4ImWsHALOPz1vcLjB90uHGNrPSpbUdFJHl3L1tTumGVcewQgC6mTXxjRqE1tvUjs7tV1acFrTlMXkEQlP451aaKEb9ZaUkSLEXS34KvlTl2HsDTtyD9aOJXtXtIdoC8SxaMJwMpayGarebhS-bsbPdRsngMB5MmoNGTEivqewdGNGc6vHH1LSPhg-Qwav2eyai8G9SFypxGEElqxxlKBd5bI6DsjPULb7KgW4AKjhWzDY1ocdjGS70b0zaHjC2_R6uh-XyuTA3_rvsCJyeP0FVk9HXfn3cmOtjnxaJk89V6IbLyclYZ3XVib8VU2yFiop8dDkScM7l0m1cCYMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇫🇷
حرکت جالب کیلیان امباپه درنشست خبری قبلِ‌بازی بااینتر بابرداشتن نوشابه روی میز کنفرانس خبری و جایگزین کردن آن با آب به سبک رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29259" target="_blank">📅 20:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29258">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e921c3810.mp4?token=ZUI8EQuegkSZL9zmAvWV9D7hTT0H-RvcYNcFJd1PPIp2xMzZ-0R5i8pwi54V6AU4w7on7-oCQhnDwPj9YyL0QZP3PSvAUvF5Z9nq9dfRWrOYX2V_8S8sUQ43-_-gUiIIzrxsfW3Z0U4L_k6TzdXUpRMqpx7u-Wr-kkgzWrYKlxfcEHRuWviZPFeRWgwmJ7IYD-BlaDOyD9ssP4-egv-eVTH2uxP8SAxK5_p-N_OufWqxMgOaI8SpN8WPKt1XUxnckcgpoKPkI4VyTrBtWuAVthY58RfZ-kv8h2VJ93pn0RlORmkKSwV4zJvSXNnhZ5OJik9xJr6mwrwUdAzqk0tROw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e921c3810.mp4?token=ZUI8EQuegkSZL9zmAvWV9D7hTT0H-RvcYNcFJd1PPIp2xMzZ-0R5i8pwi54V6AU4w7on7-oCQhnDwPj9YyL0QZP3PSvAUvF5Z9nq9dfRWrOYX2V_8S8sUQ43-_-gUiIIzrxsfW3Z0U4L_k6TzdXUpRMqpx7u-Wr-kkgzWrYKlxfcEHRuWviZPFeRWgwmJ7IYD-BlaDOyD9ssP4-egv-eVTH2uxP8SAxK5_p-N_OufWqxMgOaI8SpN8WPKt1XUxnckcgpoKPkI4VyTrBtWuAVthY58RfZ-kv8h2VJ93pn0RlORmkKSwV4zJvSXNnhZ5OJik9xJr6mwrwUdAzqk0tROw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد؛ لیست‌بازیکنان پرسپولیس و ذوب آهن برای مسابقه‌امشب؛ بازگشت محمدحسین صادقی به لیست هیجده نفره و غیب ادامه دار دنیل گرا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29258" target="_blank">📅 19:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29257">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e05ba1529.mp4?token=gPy9aJ23mCW2mk5z7zfYKB1MqLpdOEWGvn5u5DO9izmQ8KSkdqIiGc82z7NGTM1Z9p5CFa7NA2aiZ6VtGRfMzpHFVSEsEFFUNqhVGhbattLSsAUju7WvzYJUFcjjeXPL2aGa3OjWZxDqH5qoYqDh6oFpkGauimWUCeIM9-VTQtlv9gNjrhrVWyxe9nalR1ehuKx4D0wwikfz4zB8ew6gfusqy4LhEqXp6G0kxMyO9INHwjyDA_Pu4QDQQAMv1X1-TuQua2GzAd-mAb7XY3TeWKSNY8t5dytw0UgpWvIjcRcLzYfZ_Kw5Gmp_8uIbfMwupWT5jJJ6KxtSh8B11Pj0BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e05ba1529.mp4?token=gPy9aJ23mCW2mk5z7zfYKB1MqLpdOEWGvn5u5DO9izmQ8KSkdqIiGc82z7NGTM1Z9p5CFa7NA2aiZ6VtGRfMzpHFVSEsEFFUNqhVGhbattLSsAUju7WvzYJUFcjjeXPL2aGa3OjWZxDqH5qoYqDh6oFpkGauimWUCeIM9-VTQtlv9gNjrhrVWyxe9nalR1ehuKx4D0wwikfz4zB8ew6gfusqy4LhEqXp6G0kxMyO9INHwjyDA_Pu4QDQQAMv1X1-TuQua2GzAd-mAb7XY3TeWKSNY8t5dytw0UgpWvIjcRcLzYfZ_Kw5Gmp_8uIbfMwupWT5jJJ6KxtSh8B11Pj0BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
🟢
مسعود محبی مدافع میانی 22 ساله مدنظر استقلال درنیم‌فصل لیگ برتر باز هم با این ضربه سر استثنایی و محکم‌برای‌ خیبرگلزنی کرد. خیبر درپایان مسابقه رو3بر2 به پیکان ساکت الهامی واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29257" target="_blank">📅 19:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29256">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇪🇺
🇪🇸
🇮🇹
هایلایتی‌خاطره‌انگیز از بازی فوق العاده تماشایی و مهیج اینترمیلان و بارسلونا در استادیوم جوزپه مه آتزا دو فصل‌پیش درلیگ قهرمانان اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/29256" target="_blank">📅 19:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29255">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8anlXjIzBy771Q-IwLOyqKIafr2yNgc9Rwkjnp-Eo95wt9_YU4BHWOBJBzU0j711wCuf47q2WEqVUlf2zdiXIztq8g_e0PfVozgEGU0l7s-Y5a2cA7KJkKvTOooaTabss4ehSEhwBcWPY1VNeZQ7BmniIzTR4QXcPX2AllXWhmlz03_2cmTna6iV7vlQp1iCPhnH3WMCX0XgMxaTpnr5bkxyYA_MwxU9T2pVqN2_C0kmJt7Ig-RUtUZKdxMu6gURpmX9wBnKwAejLpFnBn4fuxROEBzsFbS_YU62zH4-5085sBz7L02Wp69pB2USP_hiv9jIozWa3MXAT0M0JiWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
دلیتا گزارشگرمعروف‌شبکه DAZN ایتالیا که مدعیه امسال‌نیز اینترمیلان قهرمان اسکودتو میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/29255" target="_blank">📅 18:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29254">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69cf7a72c6.mp4?token=vp-7cCvI704ETp933MbNIEVe9M5QfTfym8q0O5Bypk2QENtIvPuAgopma-R-rEAvMUX-6W3n-v_-g-oxUEpegWYlKyQ1y-tiUmZFxvUVmWR71oUljhe6n02pvq2m4jzT4zBb5Zr8wu2SUOvwVl_sQG82xkIdLa7kMMFlbzNNEuFSzc6ZCRLhdffqTZrOsEKS_MB4cdzuCxVcK6ORC5B-bCkIl-wejyJ-_JjZYALHBXWxtpTUc8nMK7rSvPmzPbQ2VDw94GzRn6WEeU5-hr3MRB1g8AZgT5QjKc4z-6M3g-PNcvQYQ5kUBTnyMhLrmZ0XnGqgAwnFSkrcycp1RKJFKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69cf7a72c6.mp4?token=vp-7cCvI704ETp933MbNIEVe9M5QfTfym8q0O5Bypk2QENtIvPuAgopma-R-rEAvMUX-6W3n-v_-g-oxUEpegWYlKyQ1y-tiUmZFxvUVmWR71oUljhe6n02pvq2m4jzT4zBb5Zr8wu2SUOvwVl_sQG82xkIdLa7kMMFlbzNNEuFSzc6ZCRLhdffqTZrOsEKS_MB4cdzuCxVcK6ORC5B-bCkIl-wejyJ-_JjZYALHBXWxtpTUc8nMK7rSvPmzPbQ2VDw94GzRn6WEeU5-hr3MRB1g8AZgT5QjKc4z-6M3g-PNcvQYQ5kUBTnyMhLrmZ0XnGqgAwnFSkrcycp1RKJFKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عملکردبرگ‌ریزون ادواردو کاماوینگا در فصل اول حضورش دررئال‌مادرید؛ سال‌گذشته و در بازی امسال عملکرد فاجعه‌ای داشته این ویدیو رو ببینید باورتون نمیشه کاماوینگا تو الکلاسیکو اینجوری بازی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/29254" target="_blank">📅 18:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29253">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9e3cf516a.mp4?token=ar3Lh5kTYs4DnI99DFE78vtv_lgaQqRuG5e8oIJen2gf83piXEuD6jfVfbLxFhHyfm6YHAoDHVnfZrVKAOKvAf7bubebDUv-AvDUFvHklfOOZWm1xthMlxG86m6k4xLCHo9xKE3zo-DytOccInev8aPaGPgqaBTzwzoeL2rs-dtJsuNk7pjVA9BolItxk1r8Qt406UyIKLbxUuIYp9pKAoQs-XgRYOO46fGfPKCaHpN1FBw-S-4rClAPN3v3H7CNt15l4stAefpmn8mc7MtgjIZP_qBoUe9eKdB1g4OD6pcO0mx0GOS0LWX_osGbxxIlBcZTT7vVFNq4mgvi05aVqHl4riplEHtUd-hOt_8KCJu46rw3_6u-8oytOqnxOME15RHbRip5uLeaIFwE6IVykdCdyi304FNP-gJaNUSuDAVZrSBVasrr_FkG5vWAeCi6BqQta7U6ISlWM3s6BZBzFgIbvfq5coRcHZTjh6CYjM6wnDo44eE5Jc-7T8hfOYBrZNApSrlf9vjazOI2hRM79cV3thP7VDw7iwJHfIK-Mn0w5vfWg_nqdTgnVmuQNbeup7hm75pF7Gea-d38QZsgRO03NidXwUiB_xYjPqOgWJ622o7x_30JvdpHMc26eEdqo9--cuvdwwP3csVcVfUVl8cYMVzaln1zPHPoSBzdFn0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9e3cf516a.mp4?token=ar3Lh5kTYs4DnI99DFE78vtv_lgaQqRuG5e8oIJen2gf83piXEuD6jfVfbLxFhHyfm6YHAoDHVnfZrVKAOKvAf7bubebDUv-AvDUFvHklfOOZWm1xthMlxG86m6k4xLCHo9xKE3zo-DytOccInev8aPaGPgqaBTzwzoeL2rs-dtJsuNk7pjVA9BolItxk1r8Qt406UyIKLbxUuIYp9pKAoQs-XgRYOO46fGfPKCaHpN1FBw-S-4rClAPN3v3H7CNt15l4stAefpmn8mc7MtgjIZP_qBoUe9eKdB1g4OD6pcO0mx0GOS0LWX_osGbxxIlBcZTT7vVFNq4mgvi05aVqHl4riplEHtUd-hOt_8KCJu46rw3_6u-8oytOqnxOME15RHbRip5uLeaIFwE6IVykdCdyi304FNP-gJaNUSuDAVZrSBVasrr_FkG5vWAeCi6BqQta7U6ISlWM3s6BZBzFgIbvfq5coRcHZTjh6CYjM6wnDo44eE5Jc-7T8hfOYBrZNApSrlf9vjazOI2hRM79cV3thP7VDw7iwJHfIK-Mn0w5vfWg_nqdTgnVmuQNbeup7hm75pF7Gea-d38QZsgRO03NidXwUiB_xYjPqOgWJ622o7x_30JvdpHMc26eEdqo9--cuvdwwP3csVcVfUVl8cYMVzaln1zPHPoSBzdFn0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
ویدیویی‌از آنالیزعملکردخط‌دفاعی تیم جواد نکونام که در این فصل با وجود گلر 33 ساله و دو مدافع میانی 33 و 37 ساله گلی دریافت نکرده.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/29253" target="_blank">📅 18:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29252">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8S88B8frreMUYoU-qg0avxDkxITMjySPnisK8nIkG7WjYF4JsN4C_I4zomA7kfFJyZyZoQHJ3Ik8qO9n_ZKTtLmRNy-mv8TVAXKUM6xoD6rhGuIZy5ETm3qQ5Ei_pjv6adNlzjgmrMg8QiPtB81_qsBbmvZLjFVjYSIXZBfNKgOigPHpC2TRRJLzF9MlFTMLci7SXuxd2g-e_-Sf6nTaJckNoXs9MvSlv8HcD3ZZ8PvE_JbpcPi6CMg3nWgYnAiJeiGKR5BMJah2Fv0i7fXuB8pppUDOIwzwH-pSDrF8G_B4c_X0qfhX5D1pFbioFe-cSwalqc2FigbHjMHdXiUZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
هفته سوم سری آ ایتالیا
🇮🇹
اودینزه
🆚
لاتزیو
🇮🇹
⏰
ساعت ۲۲:۱۵
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/29252" target="_blank">📅 18:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29251">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfOIMUpQ0v1AmTAb_Gl6xO4OH6QiWTGZ9wEmrB-17dQy6Y3eXxUFaxHlw7hMtyVA1Xz2oMgDdYgsgJuFgjoHS9y9ARSuNAyXWAyxUDS6x0VQ0wCl-B85AEo5ELvZd4Vs2H8MQcTmqmJ1p4Dvi-DbhnQ6VYMMKGSIpXoX7i7ZkQefsqqSTliHLR8mTf72IoEg-KfE6sOfN-jFm8YIrdbRMkYfFpW27vOnivqHnwcJUMDnr9ULx5TLffaG3ZI5hjkmdGVHLhh5T5mFfMWbleHUr1sYvbm7EwCkY5fj8cS1nxdbRAreIiA8YajrplEYs6O--LIPgYgtXFo4ntnmr38lTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محمدحسین‌صادقی وینگر21ساله پرسپولیس که در پنج‌هفته‌ابتدایی لیگ از لیست سرخپوشان خط خورده بود درتمرینات‌این‌تیم با انگیزه ظاهر شده و از کادر فنی سرخ‌ها خواسته که به او یک فرصت بدهند و در بازی پس فردا با ذوب‌آهن به او بازی بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/29251" target="_blank">📅 18:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29250">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9G8AOvWvInYzG1GrliUqooymZJktmTTYYP9HFOJ7SzNL05BreulxcZ5qDXTJbkeYkoUbXYQCrQ4W2kaQDVUKGun0Y_Dybk6jTLmaiuVXp21KREYAmMa7EhPV_CDeuwoRBDArirgbqjVUouM0f78V_fZ97vy3k7tMZBOveOABIpecUPRueHQy4s4bGbM7SzXhQ_IgKwH44bKET6Qc0PxgIIDz9YTR_p1n8GY1Hzm-b8wT7lAwVYGvB2csK98-J45V_EYwqRgercBBpE-KSqHHS12FcXKusnsi4Rz80fOURuMIhkNoifUYbGX-IQhujHw0OyWPUSOVcPoQXDn-kNSWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ شماتیک‌ترکیب احتمالی پرسپولیس برای دیدار فردا مقابل تیم ذوب آهن اصفهان در هفته ششم؛ به احتمال بسیار زیاد ترکیت تیم تارتار همینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/29250" target="_blank">📅 18:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29249">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4hNBjlmsRHql3gC31qymhO27KpA0mfqs_6XNSyglSMoYfWgWUeRHwEGXMw1IHxETpBuBPSjgAObdNfe8BCTFHOvC6mTaVCBOZo8y1Wq-EXgewx-lm7aAVmHpX7pnQyxNe2UO3gCVNvJnz64y9lOUpfV37CEbnqduxLCIM7lef7RbLt0-zL39HT0jymw0GutaHMqq1cQDgF-SBzZUuyg8_rdi9T1DTsJC9TR71jigNxK_4vOhL6J_VEReX1sw4dXhr0ixrhJGPAXwhOKn3ro-eaOAkR4RcNhrVCwDuFcGrX5zVB2mvbqtBxkCR3XIAcHi2lske5cDDjYpN5cddBHZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ شماتیک‌ترکیب احتمالی پرسپولیس برای دیدار فردا مقابل تیم ذوب آهن اصفهان در هفته ششم؛ به احتمال بسیار زیاد ترکیت تیم تارتار همینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29249" target="_blank">📅 17:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29248">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bf7aGgSSSwS89--ddlLsJGLTUgaAZLnzk8VFMWb5cK-LLTKu_wysa6dkvwmMAZ2YkuGvVdLiDIFfhDC0dvfC8LX6kqijX7iYR4QVtpEonCX8X8vAfF88D-PMTtvdevkRqP1oF4hjyljfCn0FScsdg3Qe7GUyxyZxG_nMRVpJgaXIKjycq0wZzQqeCAzVFdZBgMZHfJvdq4UFgfPvqTcZKuGpqMDwSaJsKrvirUlLSSoM3i2LlvZFqG8PCsxhJOI6JvQm5fOY52kFzQyY4vu6mDO94wVAJalPEnnv1KJQGy9stzICyR1qQvOSw_LSZgTqazJQIZivoZPk7NE0D2S5Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای‌نشریه‌کوپه: براساس برخی مطالعات و نظرسنجی‌ها، هوادارای بارسا تماشای بازی تیم هانسی فلیک روبه‌رابطه‌جنسی در زندگیشون ترجیح می‌هند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/29248" target="_blank">📅 17:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29247">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db6979e1d0.mp4?token=WILf8e7T1_TZwHKkq-mEFMR8mA6u7OJ49p8A0NMHuFzTke-TjumuFNASecJIGdRjQYJv1hBQE6kvxtX7VcHXhIDrvwHIUXTLHxc1e3x0fTF6OLW8ZYZJeMSzNs8wM2brY7qqMNswkxoZd1jb8oGMnT4YmMTMMfYeneXWYOLKFTE9qyRjV73Zai-NeFVwP94Jay-547Ln_HLPxMEZH3_IkkY_OrVPhPdaZCZDkrMkwosvoonDiM0fuv5Z_QS_hVMenF9Bj-Qn3VBw85Us4pBdpLm-EHw3MkZWRgUrxWVniAOXH_7AXHD3szlgJFO8IK9IEhXp67JOyQJEVy6e8P8wdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db6979e1d0.mp4?token=WILf8e7T1_TZwHKkq-mEFMR8mA6u7OJ49p8A0NMHuFzTke-TjumuFNASecJIGdRjQYJv1hBQE6kvxtX7VcHXhIDrvwHIUXTLHxc1e3x0fTF6OLW8ZYZJeMSzNs8wM2brY7qqMNswkxoZd1jb8oGMnT4YmMTMMfYeneXWYOLKFTE9qyRjV73Zai-NeFVwP94Jay-547Ln_HLPxMEZH3_IkkY_OrVPhPdaZCZDkrMkwosvoonDiM0fuv5Z_QS_hVMenF9Bj-Qn3VBw85Us4pBdpLm-EHw3MkZWRgUrxWVniAOXH_7AXHD3szlgJFO8IK9IEhXp67JOyQJEVy6e8P8wdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پاسخ‌کوبنده مورینیو سرمربی رئال به سوال خبرنگاری که‌پرسیده‌بود درآستانه‌دیدار با اینترمیلان با کیوو سرمربی افعی‌ها تلفنی حرف زده ای یا نه؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29247" target="_blank">📅 17:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29246">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyvEmmA_JgxaT1IM6IN_MbJ9Sd9fkiMDPdOpYW9t-1gXxENOD7Ncld7q8r5U_WOKLDbQWZpMq_DvhcYi7pqmf_MGS-PQTD6RiEl9DXf12eQI5iTYUs7kzb966LA1r0FngZutlD76-sgxEqwyKBI1K69d0zts8-47InlZzhZ7QJzqFevyJvN149kA62217oNhjI-QKcG91EiwUmC6mosnLmb1GLbResqn8fHgy6F4IHFWwdFvWwxhB_vRjWAfbO6zcTj8pUwJSMo9-QFTQs4rxIj6miMBb30tmjsCR95C_mRDMiPJSYmaZNMcMIPe8uRPkKAI_2mAK5TZ5v03XjYiMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیکه‌سانچزفلورس سرمربی کهنه‌کار تیم آلاوز به عنوان برترین سرمربی‌ماه‌لالیگاانتخاب‌شد. سانچز در دو سال گذشته بارهابااستقلال مذاکره کرد اما بر سر مفادقراردادبه‌توافق‌نهایی نرسید حالا با درخشش در آلاوز بالاتر ازفلیک و مورینیوشدبهترین‌سرمربی ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/29246" target="_blank">📅 16:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29245">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ef1daff4.mp4?token=RaSPM4_llUv_jhNc2TEAF969eT38Kp_kvTEbFdILb67kNGTjGbFepmLlrMLGUHO33imFpGC7Sx31AGIoPBfa8o3YVNAGBrYUFtFK5q-odLuCTJQ9eA9-TuSw34FRFi6vX-pXbDvGVCCGX9c0Z0yu6c4ufpCw2lXDU6xxpFRx-CSnmCjoSdwxbaYD4w0C_OVVMKlr3EsakVIcjq62PD2jlv3iq2_aelkvFm843qFRpwhwU6Y1KrJqXRsO54kEmLUmh4G4IiK1BB6d1_-1zFUYJamC_uAthIGXK9rpGOrLYt-Syts6qIjCxSQcMUIuCmQFwRs48hYwFPzPfQ2hTpM0qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ef1daff4.mp4?token=RaSPM4_llUv_jhNc2TEAF969eT38Kp_kvTEbFdILb67kNGTjGbFepmLlrMLGUHO33imFpGC7Sx31AGIoPBfa8o3YVNAGBrYUFtFK5q-odLuCTJQ9eA9-TuSw34FRFi6vX-pXbDvGVCCGX9c0Z0yu6c4ufpCw2lXDU6xxpFRx-CSnmCjoSdwxbaYD4w0C_OVVMKlr3EsakVIcjq62PD2jlv3iq2_aelkvFm843qFRpwhwU6Y1KrJqXRsO54kEmLUmh4G4IiK1BB6d1_-1zFUYJamC_uAthIGXK9rpGOrLYt-Syts6qIjCxSQcMUIuCmQFwRs48hYwFPzPfQ2hTpM0qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
امباپه در پاسخ به اینکه آیا باید در کار های دفاعی و پرس بهتر عمل کنه یا نه و مقایسه اش با عملکرد عثمان دمبله و رافینیا در PSG و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29245" target="_blank">📅 16:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29244">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9vEPk-zbcPopkgABoOyTf9fJii7xdZNQsf8aT6LRJ62mGjCL7HmUgvMhLRCoLvbivncTJRgNYhc6xr0LMSg7EHXH6rvSz7tSZ4ZfPWFxmUeRNvyyFbsxKf1oLHVMmOJS2l1q1cBsJFBBbnkVELqs1eX1eTGjZGrBLB280jPLMQXZN32VTRp00d14r_WB8hphuXNyWUiWd6NF4QM1CRQSEEKTF8H_BKWO7V0uSwETxR6Oy2uJGZcgGvTlHkGADSjS6Wh3Du5UPH5RRWFt8dVtuhhEkDl9oibI0YeigaJmqThOf3hPrX7AOWfZ2lkcS2KpIGYDjIvtnvllHFuSCqmWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عملکرد خیره کننده خط حمله بارسلونا در فصل جدید لالیگا؛ به‌ثمر رساندن 17 گل در چهار مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29244" target="_blank">📅 16:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29243">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0me9m29DCeld47nqI2FZsGJaETAFnWE5DzqQmLIubcgzRJbqQ_4CsKc3aOfybbjVO6hy5_aYqZFNU-yTwhSp7P9lnITIO24r6yxX99s5BHa26NMihJUErolKAZFk44rHb7mFIVFbnvY44Vr6yWT4BKWmlBYCTS5zdC0uzexemCDh-2Pkt7oWZhN4SEOiEL0B7ks93xHc_isrAf_XiNggRFcDVpr6Fq2WwRCIMCjdwJZPyUmd2FvOt6WvncG5kYrWWlFNmTmbshtl8bZaZjkksMLUTBF1zTJOuqxEsUiPoHmqe-yrEFGeYgDJFDTd9j4CaNEII9vSxYAtJH_Xn00ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های مهدی تارتار
🆚
عبدالله ویسی به مناسبت بازی امشب‌دوتیم پرسپولیس
🆚
ذوب‌آهن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29243" target="_blank">📅 16:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29242">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch14TXnN3t_-ssZlsqDfdTtk4b48ce6FLy0IR1Nakpndkd5SUl84e51-F2CMXTajIt85so0aPzI3bGV1wqwkPrQ3SDVTfATMVUNa5hLKkFAB7z47OxnFPQy-LcQwK69EUssTi9Ej2jDXGRc9SFoxPMuWbb9CUQuCutW2ryDpdjnC3QWFmLMCJnsBqP93j7KBtLXxqAS3hqyVdwilCn_ayJFgpDK2vCJq5EGlqbo5AeANBMK_EXZ5KBhG9J7uVEXOGdwCKO1kb_pgmwF6GGkUdIBTI2nE03YUjK5hqYRSl1y5a4SPYVZjdZLUt7p8-s-UXCnCRJvWftM3udcFWH-vMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میزان هزینه لیگ‌های معتبر اروپا تو فصل نقل و انتقالات؛ لیگ‌جزیره بااختلاف بیشترین هزینه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/29242" target="_blank">📅 15:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29241">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3910e6991d.mp4?token=wCKlEkEtOVCOI58N1duEwBaFXen-lRyAx0NmHw6dSjOZ0C4ifW4eJ4YdMgEsv1tcdBs1IN-_L4sNlQsThQzsuLGXZbCu2YzaUBZb1bkkTm-QJ93nujrE4GiAAscmwddFjMikwJzrX9ThV26bIQpf-NtVD2BG42VLwj-Hr179HkYAAUdwEHDW9WveMCnHZi0h2EL5m-JV-SAPEkEBOj5SrxUjMRf7WEpFHOyvl2NJ6rwuOT44hcan231LpDykqdFiaDaVsV6IGoNzEB8kiX6SJKbNjQwjMsfJzhxUjfUNNyT4fLcj2sYsvtqHq7_C2E62XPmVTIU7e88kMxtY7j0z4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3910e6991d.mp4?token=wCKlEkEtOVCOI58N1duEwBaFXen-lRyAx0NmHw6dSjOZ0C4ifW4eJ4YdMgEsv1tcdBs1IN-_L4sNlQsThQzsuLGXZbCu2YzaUBZb1bkkTm-QJ93nujrE4GiAAscmwddFjMikwJzrX9ThV26bIQpf-NtVD2BG42VLwj-Hr179HkYAAUdwEHDW9WveMCnHZi0h2EL5m-JV-SAPEkEBOj5SrxUjMRf7WEpFHOyvl2NJ6rwuOT44hcan231LpDykqdFiaDaVsV6IGoNzEB8kiX6SJKbNjQwjMsfJzhxUjfUNNyT4fLcj2sYsvtqHq7_C2E62XPmVTIU7e88kMxtY7j0z4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جورجینا رودریگز همسر کریس رونالدو قبل و بعد از آشنایی با فوق ستاره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29241" target="_blank">📅 15:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29239">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MhFJDSM7UE_QIGCCPd2jC7pXi2C1h9z_YP5NWh_B0jLYyQzuGyGuBzB6j2JkZicHhPkLOlu1yTgBSOLzgEVwhGyNQ9wLlSIOSvHQGhXCh3kKhQHs3ivVT3VT96YtaSboYk2lqglLIAUuZvVjWDjdhnQeKM-dY8eLiYY6AyGqyPVTG2aPFk1Tv-YO_L4K0g58QFTaLMU4BM5zbyIgG43E9h8EFscfGGyml-4s_Pmbw5iJSOQ8TDPU4w3qlLJwXj82FzLeoBaGwdDKh-2hOzSJjPuce4aIaWG1hgbDvf8FrgAAuvpR0quX0nAOPtkyGUR1sfZXm-Qya_pi6j1w8JRnxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OQ8Zy1I9a7ocBjFsYjHFMeOjVZf-RC3ch3IZjigwsBIUjYYNc3is9S7gaAz5ppB1qoABiXcapfnWeuInQYg41hfpDRgs9WNFoFkmB6jxOwa5NojwYZxvBbyIgNUymQQIGWsAO9Niw2PFLBkxXxyTnggwwppEjglQVxaRQepS2XMk4QJKZ1z6SYMcwxSsN_H_J2ae8ColUtiAmFvzNpjdg-nwIGbKNctkati3h4ISy5lOeV0DQfIUs7KHCMvmqLNy3F_sd4y3E9v3AfxU4unVX3MhqlbhQQ1iIZjJKPMi2bIVkPIoXEkynz5fQocq9nw_svd-R9a36_W18TVxIqxGtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
هواداران سه باشگاه اینترمیلان، آث میلان و یوونتوس که مدعیان اصلی قهرمانی اسکودتوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29239" target="_blank">📅 14:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29238">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzJm7VnO4Xf1Mp9j9JlRey1kIYNvHrN-ixKz7MUKnHdCsOsXlqJJbAGGpO-zC9xAqj4lD952DcqbcmBahIiIq757CLOB8yApIMjwPFwZ4emqjyaCr8dxkKYd9ZbNtu86nUWbuW3VJiEylSom14HlLJHX7aEki0IeBnynSYoWlmNGm34ulXlvnv_P2dKSZ8FpppbHv7iPZ3ORFxwjjYFojA-CMf_Qd0D8qA_YwtAXr7KCB3sa5Cj_h7vxvlo7vhWeClxNHshFKT8e6cyep15lOnrHEZvMQqlRUwWVSuTs4-GLxPQo3_QdoqCiY3iRytDQvF-4rOOwEzE2ogryKrOwlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریهTYC اسپورت خبرگزاری معتبر آرژانتین: لیونل مسی و رونالدو به‌مسابقه خداحافظی کارلوس توز دعوت‌شدند و ممکنه باهم‌همتیمی بشن! فکر کنم این‌آرزوی تمام هوادارای فوتبال جهانه که یک بار هم شده دوتا گوت تاریخ فوتبال رو تو یه تیم ببینیم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/29238" target="_blank">📅 14:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29237">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thfD8RsnboXw_jecx1vNyMcLTg5dSc1qEmrC7DxKfsB82JIHUcWzo-mkJTE2jq6kdVEVIk6vT9qLx4sgTORqyvvRPeFr_JmKui6VK-GqMR3HpquolOYadofnbmqIA1005V106QFrrWc9nsRhdHbD5RmaJmoGCJN_ryKbzez64lCtjkcalLMC_ANBjviDaloXcyPdliYQ-isjGvIWrL0sZ7trC9VEOV5iiYBriNqpA_bTsy0XARLt2MOvHgj3hfdEyNn_LQzDHuhzARd510HqasuRoU1hLfj1VCBkEUJbkBUhTVZlaa5AnpEngUMosuVSyjdKK3i1_iBvbyBlQ2Yp0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
؛حکیم‌زیاش ستاره‌مراکشی سابق تیم‌چلسی با عقدقراردادی دو ساله به بوتافوگو برزیل پیوست. دستمزد سالانه زیاش 700 هزار دلار خواهد بود. سال‌گذشته‌ایجنت یاسرآسانی‌تلاش‌ خیلی زیادی کرد او رو به لیگ ایران بیاره ولی شرایط مهیا نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29237" target="_blank">📅 14:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29236">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXBJml9NI_1ATPFIWgFmNc-NmIhQKbKyVrQB8Q6n6Il7gS2ioCKg_SHulycQvI630fk_4jgrX29QO9748de5uo2FHSuM_Qhi9Sa_1_NRynFjiVk3RB2mQyp3WRbDw-vR0-SxooDArvU-sHob9hd3jPM9gYXK4bA5DWC3ybRqdHIvM71y6hxXAeMRucjMOJKv9sQSzghCWQ7r8mPVxa7Owp4O-Iz443Ng4ldTgccYi4x6MuU8fbWox4ybBubMNCdTpF_LtXEbLXm6N5aSDwi7p7Hf2NRBb2t4oLz7CWbl5ARkxAcYMJ85WvyBEtG2FN8MzMPA3-VnMuxG4rPubwjLZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
بهترین‌ترکیب‌تاریخ‌لیگ‌جزیره از نگاه نشریه سان باحضور کریستیانو رونالدو فوق ستاره پرتغالی دنیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29236" target="_blank">📅 13:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29235">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fwpv413z8SbroGSCRJ-RxW7v2Bjk8HxcOZYRR0Rf5xxS7lyiInjLy8aBhCmb5VQU1lpsDT_XAquVtEwdYgx4MCh-AvT5GL80AlZrISikm9YRVJk0tMFxsjBa1RtxASm6-ZnWXlckIDv5rIPIUcLzATCqUk3ds5likgy41qTe1daJYfzlFnHW6JbpAEKyx5rxMbzf-gQ-VcHnWvZWVinrmnb7Sdrba5Nr3UwNW3R12EQEq308vggoq1GxZIfQt02MrNsHvjLupxxwgBw91DPcolJjiBZumBdHLSnBr1JmNc8wATK9B5sZh1EEYte59CEWKrYibvjw5zGGj_Up3y84yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌‌مهدوی‌مدافع‌‌راست‌20ساله‌آلومینیوم یکی‌از بازیکنانیه که قطعا در نیم فصل راهی یکی از سه تیم سپاهان، پرسپولیس، استقلال میشود. مهدوی چه در فصل گذشته چه این فصل عملکرد درخشانی داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29235" target="_blank">📅 13:24 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29234">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3453Xa_DlstQt82uElCsx3EuCGQv5cww1yA52N_HdRwwS8n0RoEyxhBuWTbPuucwsKjjiQ_yL_7fB3TiYCpF_wBlShftmyvuq0MKR8h0pinB7mZC01-ZMuFOWvJZCkkYYxoCRhK2ZZtr4djOsIDwR-p0MSztx5Q80VGpnK24OKwzMcHw4A4uSabYyqL_0f6HavsLAeXoHvbNYpmxwIr82ib9uPWQm6gNM-gWui-G9maR-UFsJJwvcaSqFh4hoMaEcQSF_M6T8Jd2rAmzn9e3MvK2nMaDWeP5ZG85w2Ub7MMdeE2dPOKZVr3UqxYuGWGQxoUrHLeX0QpoLEpDV5n7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های مهدی تارتار
🆚
عبدالله ویسی به مناسبت بازی امشب‌دوتیم پرسپولیس
🆚
ذوب‌آهن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29234" target="_blank">📅 13:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29233">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536549697c.mp4?token=MTRB9lQNdQ2ozfSjgPPqVppkDQk8bK6LDuayHawq3bUSC_WOMZxocVkOR4BOJhRCladbHo14YQ9QHjXCCL4RMJvc6yMhz2FYAU5sOLKOKcjTqxGzqT59UTDA1KbiHfVkIQSFKzBHa-37ArUCi6VxYIhC64mpKnekOGlhat7B7jrmoHqvts3OLhMYkUM0YWZWnokKtZU-0PIz8SCdvxPqp_c6tcSTeC0G0J_3BP369nDfezQHu9MS3KjQnLXawnik8sLx-pVjJBjHIlW5Fdt1BJ-pLvjI9JvU9GtdggKFUdMTDdcIoILIemiqufMfadSRaVz-KRMewvycM-VUAx5xXGxXixxpmAXzoFGV-Ryz1D9BWVyavUAC2rmHtNh-wxK4KQJMDw_gHtglklu09jWtQJ22hjLMhZLdqMLR527R7TCjdtFwYZpCIgj5rFYyRon8a8YKHL3wRRZdxKyJHRCkRUDKThGOp_e2y2a7OpXVmc-sqGg0v6d_1D4QLXjB4zceioO7StpiX8-LdT_KLsdxnQ3F-lnrD1e6KN7c-1eIjlfBPoZQt655BpCLiZYpQta7TOszNEihRzcn4bfiTflzzjv3tRP5-SmhDMWpKkJZg8M7VWjZvpdh8y1i0eLuQoSY8oFLEOBKKWSUHvJuVruw6DJsxB0uoBSyrl3t1paUEZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536549697c.mp4?token=MTRB9lQNdQ2ozfSjgPPqVppkDQk8bK6LDuayHawq3bUSC_WOMZxocVkOR4BOJhRCladbHo14YQ9QHjXCCL4RMJvc6yMhz2FYAU5sOLKOKcjTqxGzqT59UTDA1KbiHfVkIQSFKzBHa-37ArUCi6VxYIhC64mpKnekOGlhat7B7jrmoHqvts3OLhMYkUM0YWZWnokKtZU-0PIz8SCdvxPqp_c6tcSTeC0G0J_3BP369nDfezQHu9MS3KjQnLXawnik8sLx-pVjJBjHIlW5Fdt1BJ-pLvjI9JvU9GtdggKFUdMTDdcIoILIemiqufMfadSRaVz-KRMewvycM-VUAx5xXGxXixxpmAXzoFGV-Ryz1D9BWVyavUAC2rmHtNh-wxK4KQJMDw_gHtglklu09jWtQJ22hjLMhZLdqMLR527R7TCjdtFwYZpCIgj5rFYyRon8a8YKHL3wRRZdxKyJHRCkRUDKThGOp_e2y2a7OpXVmc-sqGg0v6d_1D4QLXjB4zceioO7StpiX8-LdT_KLsdxnQ3F-lnrD1e6KN7c-1eIjlfBPoZQt655BpCLiZYpQta7TOszNEihRzcn4bfiTflzzjv3tRP5-SmhDMWpKkJZg8M7VWjZvpdh8y1i0eLuQoSY8oFLEOBKKWSUHvJuVruw6DJsxB0uoBSyrl3t1paUEZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
هایلایتی از عملکرد درخشان و خیره کننده لامین یامال گراقیمت‌ترین بازیکن حال‌حاضر فوتبال جهان در تیم ملی اسپانیا و باشگاه بارسلونا.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29233" target="_blank">📅 13:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29230">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YvKHE8t2aSMUqVXvT6nMi2B2lywH6jv2yAR3ajjiipuvQW81SlMpLqireejGkUbxHb_X2OpFGJ3R-qDt9azRYX1hBvqbzZj8FW2fi4Ju26HBhUcelLdHwMHWH9dCkjg16XQu8L6yfjHshSdxxQ6LpyeeiuahufhXrIFKMT7HhdNi01cbOGRO9en9Y2iAKWwNqiEeYBwu8y0DgJ5IQRDKAf1Cv5X3JdIu_W_-TkWroXWdQ9iqNxMkobhSfn1n-lMKVaQ6x-7qoi0KReDf-63KuTslRmqCl0FC5Il42SK2ei82Cd3ro0L9S6Yg-NHsnr_UMyIls3MMisj8GCakak3igw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lWPI3KUEcJEf78uDxLu22vSCOggRWgDE_IBMbkIPheaZRBioT29aDx3lAH_qJLce7U7g_9q2Ed4lAtpMVB9nyb023feP4CqLQlc69mC1OSKWgyOR6F8MydV_OQOCwJGPCVmiGmNo-z2XSmzsKmEjWcAxpPo5yCi429KF4NV77ul38oNNLuCsOCwcqw6R5YpGpbpAZYnux_MNTOCc-QqRFnpx5WvSS7X-yEQinzVEkx9QniFHrLoX8pjUvFzBuovtYGn26pv2NhoRH_TIZLxTBLydcBqJW4gc5K8KoTcgeC698hXupqnGde7hMYJr8JxUbezg60PPY_dTsiXUxOW76A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
هایلایتی از عملکرد درخشان رودری ستاره جدید بارسا دربازی‌روزگذشته این تیم مقابل والنسیا؛ وسط زمین با حضور رودری و پدری بسته شده برای رقبا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29230" target="_blank">📅 12:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29229">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwDKRkG_D8M4Hwai6Ihfo-NSQ11HmHo9Gl3HtZxRF_ZRg6HjyGRyn05ZfmmxtFT1V4mdgXsKLITjemyDKbNu2RRcMHFmBodY8RThIy8ocsBf_hdDSFRcGvpvl9H_R_Bo2BBDA3eli2jqis0w728Kds0sktr7MRwe_Hze2JKeckEik_EvRmIpWyc48H3Hpnc3SbnrNV_KLMLLzxWBoQyXv0oEtECmVhfTwJCkvClzzdhwvhLxOEglAkP6aMjrIgakHybuKUYwPRzj_fZgAslBzX3PsElhEGQd8nFoYyNi0WXVWXRzfZzNx_4gzogQ2_o1xwKTildq7EoRGANT-nVMAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ برخلاف صحبت‌های امشب پیروز قربانی سرمربی تیم آلومینیوم؛ باشگاه استقلال مبلغ رضایت نامه محمد خلیفه و بهرام گودرزی دو بازیکن جوان‌آلومینیوم روبه‌حساب این باشگاه واریز کرده و بااین‌دوبازیکن قرارداد پنج ساله امضا کرده‌اند و نیم فصل به جمع آبی پوشان…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29229" target="_blank">📅 12:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29228">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMbCIHR_CFdBD48yNaU8XKLJKE103p-gNXa-SfHOwtLWN10qy7d5iY1ByHFpCCeBCj7HN0pmZpRNLVvDEJT1LxkaSX0wH7xs2Vb0ZP14zIIv5eHHhc1SDAG39lCXdJOkCImyMjQHfrhUiXIgAsaUttQ2R66XlMJT5X-9xZt0z1L7fnBf7S8wnpj9w24GfkAkfwOw72JmQmPRst1Y7erQM0dhvyswl9-n0ML_mk14_qGCGw5TlbIu34RxHFJI3d9rQbvV9EXa4xwF3O4cp2z33kr20yeDvft9xRMOY8LY_XKOmcZ237bjgkWliyVLWk2fS0CaPz6_1kYjBI74hZM3-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
آخرین برد ذوب‌آهن‌مقابل‌پرسپولیس به هفته ۲۸ لیگ ۱۹ برمی‌گردد و این تیم در ۱۹ بازی قبلی خود با سرخپوشان تنها ۲ بار پیروز شده. از آخرین پیروزی عبدالله ویسی برابر پرسپولیس هم ۱۱ سال می‌گذرد و این سرمربی با ۱۱شکست‌مقابل‌پرسپولیس در لیگ برتر از هیچ تیمی به این…</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29228" target="_blank">📅 12:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29226">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇪🇸
شماره‌لباس‌خریدهای جدید بارسا در فصل جدید مشخص شد: آنتونی گوردون شماره 17، کریم آدیمی شماره 14 و رودری هرناندر شماره 16؛ شماره 9 آبی اناری‌ها همچنان خالی نگه داشته شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29226" target="_blank">📅 11:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29225">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AS_MZZqB6pugsYDvVlp2LGiSp1xGYYY0-bu6VcYM8_8CsKGEMy2wwj1PgHhpPv5dQP7hYnUWS5ELJeDpP2IZU7zQ4OEJqyABv-Ni4L9bIkuw-qUW0Zp9JBJQnyqoZdDsYqiqsGUn78e3H2XrRi7FyXWBLKIFpSfJnelKl0meeSPBG9ze5XOnP9oBIwZEaYXLYLaPYyBS-IfuEFZV0qW3tliNCV2pIryC71_x1SF4h6jQpJuIi_JULbW6ZR-Qwu1uAyP8KJ7pL8OcYQ7uyw7rBkbl_7MFQ-Lw-fbu1_pSZFvW5e098rlMaJ6f0tH9CB_jKbMprkob-S0CYng7enYYbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خب‌رسمی‌شد؛ ازساعت 12 فرداشب به بعد بنزین لیتری 10 هزار تومان به مردم فروخته خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29225" target="_blank">📅 11:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29224">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEXNLMKPmVBEk2inbtRMOd7dJ_X724f9APk784vKnjw6EQmxU2vWFgm0LmsCcOhLt4jk-bPMbxwAZWmJtmvM4uEAp7tOIL3AWBNpGRq-sVcQ54orM7jODudpNq8uD0xtrwFXLz1K_AYGBduQZF9QsbO6QioNgJ5hLD_HTcHgY2sH5YzCLtY5dIkUeMLsWKdFA4ih2gSkeG6990KpnuyfoIPiugxLsTG4R1fUAUNeRqtSCTGf7lbTh4RrRazQC8lKcrdtOZ85Brhf4Zhnfn1isXBtbOFqvjhS4P-pqe-P9vLg9hpmbFuWm_MJ0r4rmtpI7_QrlkDZAsYnwVhUjNMrCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گرانقیمت‌ترین‌بازیکنان‌حال‌حاضر فوتبال جهان بر اساس جدیدترین‌آپدیت سایت ترانسفر مارکت. لامین یامال و ارلینگ هالند همچنان با ارزشمندترینند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29224" target="_blank">📅 11:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29223">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Teq6XKH59PgM_ZN_KiH-52ko0f6ZTXlPHT6Qb6-6EfceH4hV9f0R-bcw5IgETbL3llMS8GQqa7rXxxN1DgvaWr654N7qulcCz2wT8a9K2aLeDHRaoAcaHxPEXzLx1XyDqc7FxW_c90OiUGR86yWWYlWTW3xgbHibL1EUFrt6S6ehRE4C65e4GUTkeE6HnnXNdgc8udTyG6DDi_MKqtW9a_vE3QlqkL1c036O5MAPB5v6QltL8GcW1GMZzrEc1cTksT_irESHKFu0j7TGyTjA9N-_eVNsAivMauK3hXKZXftuvOGpFCEYBJUF29b6NDqFQQ0gsuPNSxjW3Xpby2Z7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اردوی تیم‌ملی امید به دلیل کمبود بازیکن لغو شد و شهرآبادی، لطیفی‌فر و ایری سه بازیکن پرسپولیس، محبی بازیکن خیبر و صحرایی بازیکن گل گهر که تنها نفرات حاضر در اردو بودند به تیم‌های خود بازگشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29223" target="_blank">📅 10:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29222">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Grz87vM5-ZX7bJKWXtrINM1n8QM80NzuqJnQGU9qVpbCPjT_aQZDkhh9zCTbBPTITWPPgbsHKBa9zrIVpsMqC8ffPKxeHqBCljKA43NwpscD-nzr7Hf0l0m96ID-F4RwT487d9mQ6bS-KJtB9vgbeM49BCshhlbsXT_4UFQ-e4jZFCZbk5fTzg4fUAFPL10STbgQxLoxt1Ehz9FWWSOYKVh4QQW3La7K35I80w4jJeGNMfYioSZqJPSAr0zA4xTm9L6cMvc44o7--Wx4qH9J864aUJqOhSOOB8QjnSrT85HmGoMu6H4VnN63OiAgVH754Z2xnbScJX-1KsP444NZJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ شماتیک‌ترکیب احتمالی پرسپولیس برای دیدار فردا مقابل تیم ذوب آهن اصفهان در هفته ششم؛ به احتمال بسیار زیاد ترکیت تیم تارتار همینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/29222" target="_blank">📅 10:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29221">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzKp2bzMbVVtGQksCFtaLO4l_DfHJWTGEKGNuy2VFhRQ708WFz3kmZ5ah6ZX3vOaeEDh8kwbuU9uzYGMLumGMfygjDBurSZGfhlt-tihh7ltuOyNrOGqC1xpQnYhXuKOIvUubj0rRgHXnLgLsKq-rT_rg8KD3C66RpMl4sLXoCm113GU9HflqOcPC9tYxfcBrLlFNu2W5M1mpgVmAl0px1ArVKfmMZBv8U4QzcoSDIM8twPu-_srsSvWpy1PnTfMd4E1pNHZZhqV9QTjZy2kJ08nwGK5HTPquwuy_8Je1Ec6SR7vHlbP-KH3pGPW1EwxIvny7XN4bNGpomCIM8k0tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تاریخچه تقابل‌های دو تیم پرسپولیس و ذوب آهن به مناسبت بازی فردا: 77 مسابقه، 35 برد برای پرسپولیس، 16 برد ذوب آهن، 26 بازی مساوی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/29221" target="_blank">📅 00:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29220">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiIBDv2kCW30pjLMKSnjqXLhdpV0nTDoNonxGBf9-Y8o7xpOTGw0c5-8kwQTRaQRoBWotKgZ6ZIsh6VsXoIJNWIvWkOmyXRFiaGWHj4a1qor1rXEexaD3VF1Z_VqrRgkdb8Y97yZfhmet6AmcKm5_ZFxfl2wXacL-ispm50x8MtfNrrt7O-8ManfPEEFIQ1EhbAAhNLNHzHpyxH0jmHuAQDyjoRQLQfFPBqo6DdejIvUQ3q6ZiqQId1y5SL5T5z6dwrkYTfJAcrPxpN5ZE_r-_h4JncXjZ2sWNtSkM_W3xi7mbHoQ4BggETgWkXSO8Aa1gM_NgMddFyab8NoQbzGgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛مصاف‌شاگردان‌مهدی تارتار با گاندوها برای باقی‌ماندن در کورس صدرنشینی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/29220" target="_blank">📅 00:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29219">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gasN5iQTwSI61Im0UDeEaOVNYy-RBUP5RrI-L-03YpVgv6P9uFOeTINVgM9h1x7AJfvVHdGCYZp93CK8WJFCsuAT768BqyIBRToFzuOcOrVeMB-JsjQHQzlrtRu1iDfSaLKTddv-TE9qaAH3Z0KLnGg0IYRTeE8UL8XPT8eSjOUfCZMOBRSOT7RdV0B24sANT3HJnKveTCunJ7MatvcWCPcn9muKBmehyTJGdcL-xMS5Dy8YH_NgU-maf5z-_OjAxZn7cRMwdKBkQ9Y03AdNJi7hShhplsra0B6A_Qf6CXeYbMBT0q1-pVid_78shBfmqYOk621UbCS8sJO0UeFcTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
توقف‌آبی‌ها درشب درخشان خلیفه و شکست‌ناپذیری‌ادامه‌دار آرسنال دردربی‌لندن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/29219" target="_blank">📅 00:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29218">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHSLh59OIg8eNOxk5yN2DinKp--yVmTrvZ0KYOOAuDoQygGI50KXA_mL90EkcQBPykQ9u-Il3yYt8zAh5LKZNqKe9Kzoas5pHTyS4Z4U-5zel66-3D-V8JLd4k6xnQZWkiECukDWWZr1uFJ9yP89bWX-n7qGIZDsMIS5S0fGZdGiDhQ60WALV0Zf4ykegYSelK_3YxMTrkFs6rBXhlaibFKcb_rW93AC3NL8an63azQ2A-a-VJpHjM-I3ykNF8OfN-5LzlrJ3Slp4xkKxbR538HWcLN9--F5E9wvlNnffBk2DcPi1nXm3E4UttW04ZsScRttCHDm6aXxsUavVEmzTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
بعداز نمایش نچندان دلچسب در بازی اول؛ محمد صلاح ستاره‌مصری‌ترابزون‌اسپور شب گذشته دوگل‌خوشکل‌برای‌این تیم زد و سه امتیاز رو گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/29218" target="_blank">📅 00:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29217">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_08GJdFX62W_0aVFFr3zC5jyDcwJGY7DK2l0Hck9R6jgA-2gxAk63ZCdtC7gmJL3xCUlDWkZyH7AhMrek16ELBblaek_uR6qqZUQyV50embxLVxg6b8Ujp5p7Yba1FbS4jJXEwbNZjv-GZ1CCNaSnqNZTSiRDg8NXTenUKyKAZv4GiT2t1LcbqfLtYZaN4EK5Z9rGDWVl-zWCR_uczqYEh_a0o2sZul800hp1taKqBRZKjUAGsKw9kJiIZ0ZlJvcoAeJAeutSb2tWb0XXgn8tdEQvXHLht6uiChYm4lLLE9TFZm71u_6wV3bMxNnCkjz_hGGZebnqEiOoQ_55DOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌‌سوم سری‌آ
؛ شاگردان آموریم در واپسین دقایق بازی گل‌مساوی رو از بیانکونری خوردند و سه امتیاز شیرین بازی رو با یک امتیاز عوض کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/29217" target="_blank">📅 00:18 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29216">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6zszXQIDKCYqyLDped1-ckQPcbPGxgE62CxHiXPkHHOf98_MUaIUgvsDyc992uQpJfarXwzb67KKHStLqAkEgZGd4YRLGhQHw4FkVWLHCxQ5BWZP0D0Dpt0aVqMJ9vYEmRrAE-XYMjcKg5f_wjixOeQ2Fu6jQIEWBnrVmMii95fC-qouo0xBiu_TfMRmkmZLAxxoLzbaGVbjL-fMZWsd_LY2fH05iPmo9jcUUQzkuGMUPUJ2aaJG36_YlciuntRkBeGlkYvs8qxa9puT3VcW4eqymGFww6QBsMC0UNKaG9JxfJmZ5ZOJGVjb3uNIVORhxsUktwRU54f5dPEk6EdgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسابقات لالیگا برای بارسلونا به یه جلسه تمرینی شده! ۱۷ گلزده در ۴ بازی‌واقعیه پلی استیشن نیست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/29216" target="_blank">📅 23:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29215">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac032e583c.mp4?token=Nvai_QtRdpbPgyUpYJlTp6i6LWuH_jyWL7eB3iuuUCWG479LtNWqzGVrxByyyX4c3MuSMjJpzG3Aoa4ibq4NKTdvUo5mzjrq-TDXp8gi_sHQgLVKW88cOQuTS0ctUklZcKmodXpFOhJU0XL9Zjs2MWRhWUxkdIy80i2ADNWZCZjeG9mjkacI3S-m4bDKU6ao0AOsHQWq8t21vp4M3R8W9PcgkIc3U75-qOziUpRf_ndFBEzwAESKE7rKbthE0TOqn-0DpvkmsVbUpTSws9XDonxDz3TA6WI9HpAx7fe2NZxQb8zPL098jtGBcFhNjfZ-CSRhkeh2sING17uKw_aW1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac032e583c.mp4?token=Nvai_QtRdpbPgyUpYJlTp6i6LWuH_jyWL7eB3iuuUCWG479LtNWqzGVrxByyyX4c3MuSMjJpzG3Aoa4ibq4NKTdvUo5mzjrq-TDXp8gi_sHQgLVKW88cOQuTS0ctUklZcKmodXpFOhJU0XL9Zjs2MWRhWUxkdIy80i2ADNWZCZjeG9mjkacI3S-m4bDKU6ao0AOsHQWq8t21vp4M3R8W9PcgkIc3U75-qOziUpRf_ndFBEzwAESKE7rKbthE0TOqn-0DpvkmsVbUpTSws9XDonxDz3TA6WI9HpAx7fe2NZxQb8zPL098jtGBcFhNjfZ-CSRhkeh2sING17uKw_aW1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی آقا دایی هم عصبی کردین؛ واکنش اسطوره فوتبال ایران درباره درگیری خداداد و امید عالیشاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/29215" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29214">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXCt_6CsJbuJytVt9N7cXHCLDCUAhIkWqx4Tv99Y2GCcRJdL4Xshvc_OOd_u3gwg6xj_VNK3splksbwWBD3ZQHzjsa6s0Dr8g6uRt4wPwRh89nOrHmFfB7mEQyBlG-VI_60Bmghh6O1ipU2WMit2N4XbVNhPHuF4SQap0OFISVKwxboZNlFI-LOmNn5QTuW7PNcd6OFCx40mHfz9Djop0vOc9a2rNy4QxnmEkZImKKy9Eicmj3Qz0bFfPqLkRDDXLckJ2WRtvbfg-BMVjtlT3ADqj0n8RFiCPtcZnCLCNAZODwagPjEHtXXCB0e7-Inl0NCFpixjnq5EPwx6zDTntg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیروزقربانی‌سرمربی‌آلومینیوم: کاری به توافقات بین دو باشگاه ندارم و اجازه نمیدم خلیفه و گودرزی دوتا از بهترین‌های لیگ نیم‌فصل از تیم ما جدا بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/29214" target="_blank">📅 23:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29213">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iG3iaBmDMF-LVELXzXWYYxZSd7kWIWssJVSs4WrhpY448OmJRCyGhnDq9bcVG10qA7TNal3ow6SxPYvT0lAScPF1MLDNG-xvqoP_WLPUj3piKMOTpGGUBFOLCPMRZPT6Y0DGGovQwDT-8PTMgVCja3YFfAY3IMQn_fhotUmxYv3WNH3EZhIgUgu-UjPaDaa6X3HO8O6FREuurTBGvVvZEsGxktx2ygHY0AWbxmCpjtSNx-mzGVMC2nKD9Q11tctL3jzNy73bzZEURRE4NcOVPvK6IcT_2Mcf2Hc0pBE_UIEzLzQbJAS1m8wXmLFUEtjhWBJ300RL75gyjKKIOud9KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
موقعیت‌های‌دیدار امشب آلومینیوم
🆚
استقلال؛ محمد خلیفه با نمره 7.7 بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/29213" target="_blank">📅 23:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29212">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c32a03f776.mp4?token=adihrRshWYbAV0TbrWbSyj9v6bYzPOVw6_HDi-BdnfbpVnGEn9_nNYmT83TtSKaIllu1iIFEsR8mH1iUQXzz6jN4NDYPbEnooZqN3oHKswWvSGRgetXBbErsM_A8k65CliAFCf0vv2vyq7I5_daf41MKQs_j16jak04RN_TRh0U6J8shTiMHHzkqEcSHLZEykC39FwK_UxQUZ1liOkxbrOKUGz2j4ykrTHtipmUfgUHagY5kc_Gu-0nZ81EvAg_8c3qXAtMppCa01WbwT4OzsThvULqpIQDT8290E-edIespPd7jofVcwBX9Y4h1VCd277QhDWZar8sG1C3yIO3sbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c32a03f776.mp4?token=adihrRshWYbAV0TbrWbSyj9v6bYzPOVw6_HDi-BdnfbpVnGEn9_nNYmT83TtSKaIllu1iIFEsR8mH1iUQXzz6jN4NDYPbEnooZqN3oHKswWvSGRgetXBbErsM_A8k65CliAFCf0vv2vyq7I5_daf41MKQs_j16jak04RN_TRh0U6J8shTiMHHzkqEcSHLZEykC39FwK_UxQUZ1liOkxbrOKUGz2j4ykrTHtipmUfgUHagY5kc_Gu-0nZ81EvAg_8c3qXAtMppCa01WbwT4OzsThvULqpIQDT8290E-edIespPd7jofVcwBX9Y4h1VCd277QhDWZar8sG1C3yIO3sbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول‌رده‌بندی‌لیگ‌برتر درپایان دیدارهای امروز؛ سپاهان با همون تک گل لیموچی سه امتیاز خانگی تقابل با آبی‌های خوزستانی رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/29212" target="_blank">📅 22:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29211">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DL1Qp5LgZTTLmYSW39irbCfUUA0zNLsrF8Yj9UvLwIKKPCi1GSRbC2ihd32LsgGvWLuTMZibaSuORuAI0yxdlVV6x7Wo17jAFkbiLXkwkMZGWlYn81Uyc7fM5LWQvgFG_-NjnrGysz2Uiip8EWg5k8nZWH8zH8PX-7JqTXkxJV5Ki2PtZY1Ln-CBeiy6WXUmfSbHgLCu6cCX5g4eypoHaJH3wz3iRFW3AZ-JerE3uS5EbVcxyeLh-R6V6RUB-mtzIAixB6G3nfLW4ymUO9MaoPIqDZkhDtL9rvMbfPPoBFQYMwNrzclSWpWubOnyBzrIe6LFkBtcGxffU6YOp75sCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویس‌جدیدخدادادعزیزی: بله امید عالیشاه به من فحش ناموسی داد منم به بدترین شکل ممکن جوابش رو دادم‌. من‌ خیلی باید بیغیرت باشم که طرف پاشده اومده تبریز به من فحش ناموس میده و من جوابش رو ندم. بله من صدتا فحش به امید عالیشاه دادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/29211" target="_blank">📅 22:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29209">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0Cuaaaq_8bv7TBiJUGFscrM5HBrzS3S40IHK0WRZTTbLD4vFGhsXiixuWDCDBoxJUdw7zjTJi0VXKk_sL2WZph3EdDU9kCko4pRgOfS9b_GESc_yG8GAju_6_EzGYWar72R-GxWcBC0KXFgIq3G9EGMsGUpRmynkNtyTuTF0M3tcAieOeGYJ9oGYNe8Lzo66jkEqzGVvUgM-Az1x9zVgUiWFCxROE1-tL2O4hJHevUXxcpXQc9lWQU8GG8jsZIux8zg8Cjp0Hb5xTnOGc7R-DPMlTSsj81niCXlYBVGwJzskx051FmPgr6E3Soo9MPEAkBK9ZB6LGjCUdJp1kkVxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
موقعیت‌های‌دیدار امشب آلومینیوم
🆚
استقلال؛ محمد خلیفه با نمره 7.7 بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/29209" target="_blank">📅 21:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29208">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664fdddf46.mp4?token=aH8id1rpHZqtdcCppeWoMFKvAlCqyernI5RTbu6l3VO-w0jx737k6plrCil5hTuB_qgVV8nHA-3YVrRwkvze0_40uT4YyDWtVOuSrOti6jCSu7h7MSTFvf94ZuMIC_2VT0zRYJJuZkv02vqlG2w7CcIudYrM6MSlvDlA2tV0-4TEqSWI_c-nrrOqLjw8tB8DHf29SIIUv1LkFd-RIlbmv33sunB4lcrI6TiSXgwoNTfxrfwCCewwdy3Y4vBh3Wjg_93eFKjleJKH5a32GF9ZPSQWF9bHJCySRwksow3SXC67k8RUcpgB78C43MVmbfjnbMwc7_FSx_fkCqI4-IQvpIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664fdddf46.mp4?token=aH8id1rpHZqtdcCppeWoMFKvAlCqyernI5RTbu6l3VO-w0jx737k6plrCil5hTuB_qgVV8nHA-3YVrRwkvze0_40uT4YyDWtVOuSrOti6jCSu7h7MSTFvf94ZuMIC_2VT0zRYJJuZkv02vqlG2w7CcIudYrM6MSlvDlA2tV0-4TEqSWI_c-nrrOqLjw8tB8DHf29SIIUv1LkFd-RIlbmv33sunB4lcrI6TiSXgwoNTfxrfwCCewwdy3Y4vBh3Wjg_93eFKjleJKH5a32GF9ZPSQWF9bHJCySRwksow3SXC67k8RUcpgB78C43MVmbfjnbMwc7_FSx_fkCqI4-IQvpIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
موقعیت‌های‌دیدار امشب آلومینیوم
🆚
استقلال؛ محمد خلیفه با نمره 7.7 بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/29208" target="_blank">📅 21:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29207">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsDW_TB-XAyxzlv14jPBbzH-kA9YK5e-wdQjiAculKTfszZnJ7wDBMuE2sqyUWE9pXQi-0ilQDgGZScSNNX0BXKJK-FZkAaex6s5xVJ2pfuRZlSk7_3Yuv5R7WeK-MiauPcuCdpbTHw1xkdnCuM9p30S0GajctcfpMZ8cKzJlCvIoQJUPRLbZnInpH8Sy5YyBe9G86TR_nwa2REGcROhrkv_DhJrejhcjPhPXBMw4ITbUgBXNFfnVURyohA4sao2MA4fzM3_WaGm18TtmDw_BX-fejvbs5c5jrkvT5SAETzzjmtdn243Oom6aRHoR27OexqR1N4GR3GIKEYxNe3jiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برخی‌از خبرنگاران نزدیک به دولت مدعی شده‌اند که از امشب بنزین لیتری 10 هزار تومان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/29207" target="_blank">📅 21:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29206">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UV89fZ54tMzv8J2T1HYDbeWMB432g5Vu9D7dPzwZRlexoYxJD1fSalt_fwpP4PQlMFrm6MSGES-LndGxvOU8LriVXflnjqgfFNn0Qqs7WejKIEA_tcazpkJUb_K8hjpePyaBWI4I30uGiOsjiHvxLt9ZHLsJFHt0ezMi2yyREHFskrFsFDUK3lh9kaVOb6XLvJf7wDJUHbhaBKhwtVNZLt5M_Ei8cb3UK-ajg3-0OPstzFRJ6dKx4hlGHs-62174ic6hP94hXCVZnIsAGiJ7BwG_wE3HCmwYt59C2tHGlMez9K_0Jp7eNotYlVzCFjL9qeSLgcPzw3X3rhBZYzL50A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری جدید یاسر آسانی که نشون میده عزیز گانیف ستاره تیم‌ملی‌ازبکستان هم‌اکنون در تهران به سر میبره و به احتمال فراوان تا پایان این هفته تیم جدیدش رو انتخاب خواهد کرد. اگه استقلال پیش پرداختی رو بهش بده 2.5 ساله آبی‌پوش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/29206" target="_blank">📅 21:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29205">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfcDGGHN3mV6TfksaC6ZLV55H2EzecEgPXVT6djrRi-4-O4zrID9nP-X4DJdEtuw6nqUjKf0LX19WgR5xW2CSQOjxdjC2zu5BX1-6oOUG6uBhLY-4AYs6fwd0tuxOhXFPUSrTNMpBJPflK4VY_LaihphkcDdps4hH2yb8fFmtpDJ-3OLx9SxeCslRGEWXApV8A3PiXJ4cZ-i62W5A0_iBEQNMzXYtZm3W48TzOCKATRla6H8c2O-TxksfWEDnGZ6znWz8lC9_Q3d1ODHZBbiWQ9IDb_DGRUHXC8VTpOODZ6ICt1q7AcLuvHoswwX_5FQpuNxslUJHTFMMu_guydG6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته ششم لیگ برتر؛ توقف شاگردان سهراب بختیاری‌زاده دراراک مقابل یاران پیروز قربانی در روز درخشان محمد خلیفه دروازه‌بان جوان ایرالکویی‌ها.
🟢
آلومینیوم اراک
0️⃣
-
0️⃣
استقلال
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/29205" target="_blank">📅 21:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29204">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4VAS_Eo4_OyBHlEH1UdmCEGa55_KxPoagPOsX0ZtGiFuc7B5dvEth-XTb9_iD3GhYHN_-9pOliYb8eBgrmq0ZCaT-fgqX9hV9RTnkIZXSoumPNPsRKONM2_owat-AKqqofDJGzpdWUn_fL_lAFRl4NXAFdGOD02x84AusYdw7N_sfTgwmrqMTp3jTY-JZzlOpe9jgs_nAcruIKT8T24ZA-Ws-K-kfRzdWCVNhZU40fnugK0yLUNnS-o8ZCqErsgt6K1OW9HyCBN7PFQ-mx2FegrZlfeNuw32Z1A_nqdB9sux21i9sL6O42DrCk6VAWEaayngwHHZ1bbcrAl0vueTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
هفته سوم لیگ جزیره؛ شماتیک ترکیب دو تیم آرسنال
🆚
چلسی؛ساعت19:00در تاریخچه تقابل‌های دوتیم‌چلسی 66 بار برده، آرسنال 87 تقابل رو برد و 62 مسابقه هم مساوی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29204" target="_blank">📅 21:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29203">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBGZNCTvyaP_1IYEE3FC1ToTCFhy9VUptmE88_dLFQ3Sd_gHVHD2LLpqY_b00OvIeO9rlJWz0CWTjp3UGDDeEbqszB_L6joV1bGimmtW0oSEa-CmF3FoQ4vBrafOAbaV-Aq-flx2iDoOOOOXS2ez_jn9eOY6s94wptIFGcR8vywq1T4Hqt5ovAImQLVOqw1OOevJmyxEtLYvXhqJpwp46qc3i-OoN7LgzLYnjw-77yuzUd4S8EjiOJkEa50ylPi_ug5XaayDX9BmNfOF6c8npdOjCWKTDR_cN8Eu57G8yar8kl55YwlwA6u2O9ZnighsxlYrOHLsgQxLv9Lzr7ir0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دبل‌سیودیدنی محمدخلیفه دروازه‌بان استقلال که قرضی در الومینیوم بازی میکنه مقابل حملات آبی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29203" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
