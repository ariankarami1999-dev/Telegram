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
<img src="https://cdn4.telesco.pe/file/PmNBYNO-G410FZxL_8Co1vdovQx_kw_lwwEFxqlfi1k-TROuWvAuGjdDV73fSQNirBdH_uDLTU926kJwiElnxHkmw02MY6LFUc8a8zzqbXuxIkSDAb4FQoJWSWOKSN_O7dobw17iegpfn5fpsHCr195jyTkx1PALLt8RCpQV-dM-RKT7GztruXqHk0dqrjlt25tFABlCATx4eu65uZs5-5_tACKQcjHOh_FpmMeKKbB5zfhF79kp_hODZW4-0mOFU9uSu1G-GzxHXENLmY5zrIQL1loa3OUcBSGGVHLfSB7OcimJG3Fs5n12je1LMUWUtRIJcfT4yvEt_A8bxGXdsQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 208K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 21:21:28</div>
<hr>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIfP9rLJD2YNNE2EG7FPmCNLz_5PCrsSGpodtjB5XXiWLX9S_YeFeWeYrvAucG0oUqYLqD1PHN_2RfEd6_NoV3g_x_WNo7taWRIUi5pEDBv4SCZoBxsHLbar7vmC2EyHkmuAGlq9Y8kScToy9MIQaUjX6UpfQQ5FK_gucdDfKlREi_xvCKMORaBKBQvkZp_K5TAzHuAhQSwckuRTNhjPulcS_0Mjc8LhbFU4ofP_jSijIwANozkTOdptVY2Q-VGCbhLde8Y5q1qf--k49LshvaewE-xjramqqeEAWAFBSFd-yAS6dQXQe55BWtfcVk_181LxmOZb7Do1pJrqVAl-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGLC6fEF3a0pEh31JEifn8mHJighW88fTRVX4nhGiJBuRMGkv3JJMqfaro6wfGvI-8m4xzK0JnZy6_b9CqqQB6jlCYhaNwONTXt5Z4uPIat55ItMWlPn1F2o1nnRLFlMmSKiwsV5j-qdUjJHMkxt77P7rejDNQvAW4mYalE1knBkX9-yIM8UUuZWoai0nNaOUnEIOyiJ2syY7Qaq3Lsb3KBpSyULt8Jh8SqEhtl93q_INulWSqVPy5LK3pjUhmEnrL2u3K-8-KdHu7lWB9FwikoJBHK2tT505WwyzOYUjNQuYA8vFeZF1Lb1Za80ZdP7FziV7BVMt1uJEGzyyPwuJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIJKVMoVGDwXhrk8Wy-OWnvfOkqBYkspHjQDLdwTEZxwtZA2SieqQBPTZ7r9zLYwefzhbltVxarUUSxb332fkpLHLK_-oP--PQClnKexJcp1GlmqkfNxhrLt1WW_cLM_yrh7tYBPeEbgWShmXeZj2vQK5lshfNNkACTgedojiBczkDZ5TBmf0iYwKmr71ygIs2IYKcVsRl5_KrUFip4m6KbxpCd99CwSGibpChW7Fk5O9D5A5m3NCT4mQV3MXgF85codV27uIX5UEzoC4UZNB3KRCI7P188NItmDE02ljGRdY20_HsPGu67X5FZw1jfz_wnL4E_OixJigv5d2la0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCfbJCDahA9sjTq5M4frCjkqHVr0xPnt_6XyaAvcOooYLjRFVJb2sr5NAOGPZWieDr7W85amSHBms7nTyhkhmOGGIqADd09aNmYVSCqXlgUtlEHNtOX7xP3mH3_p6VKEpYrLsBuUsyxhX2QKh5UCH2Sc1zhAMCukjEDMWG7V5sR_NxENM5PnFmliNu-qhTxuXlNP2-bhigeUhcL9kQ9rtJsbNV2MDrV3A7Bhc7iy80i3NpgAvfXZCU-EO9Z2jtGkh818IahXF6YALTG7IHtztwNyRXZaTzxCnTUbkEWQux54ZfPO6f33thJfKAPTIib93ddmoIpGR4O_bybGIAU1hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22161">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
⭕️
⭕️
بچهای پرشیانا
باعلیرضا صحبت کردم هر گیگ کافینگ‌رو ۲۱۰# میده‌سرعتش واقعا محشره اینستاگرام توییتر تلگرام به راحتی بالا میاره
✅
تضمینی
✅
بدون قطعی
✅
بدون ضریب
✅
به همراه لینک ساب
✅
سرعت عالی
اینم ایدیش برید هر چند گیگ لازم دارید ازش بخرید پایین ترین قیمت تلگرام میده
👇
@Alireza_mosve</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/persiana_Soccer/22161" target="_blank">📅 18:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiBGEho4N-vmmjREn7f9EFlp_DPEaFx2BcQ7Pcc6lBO1miK0V4JQBYS6B8OOu4efsGwaMnI1njboyNkeKNVobr5v_YhHMq1uds2ZRSZWaOZJfRvze_7hGaHOs6NsRHvnXCF95iS3DyaMp6-gNhmtFcOq-bSPdc0dSz8wd4PuH7C1_V67fM74rBzpyEYzq8XVLYGNNFe7nPf0iSDeMZ_0xiNVtMYzA7SPmykJonXEYlzmZNd9OVnte-h44_OEag0d1gxRgmMZGHHczSoajuRa9C6OV-KYZFgrQ5Y1-oov23CSiOcEIZbK7mGCIFTPWJPsiKtInXStGAEqvXLNNcLV4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYDC0JSpB8uD2-M-jqckF6T7RIdMZFqLGHr1KU_IrUGXfWy_b0dLMAsCvl0B9GTwFXYVBI3Ot1BQlepkmmQHkTZ66mdGtgXnvuxXb4aQTS7lG2yGg-bfQaJFr_Vq42Yr2QTEfQr0tFdOY0be2TItomSlfiCNEHLIdHD31pr1LgDMaemtlUdB0ZlG6saY6cR7ROnoeFe8wV3Fbf-AWb9ut8lQosrVIcqodO2h37jnrreqs_mvs_H9wzsPHTTrKNzQr5-vdkHI7_iGALpC34yIkXa9-smFdqeoZNQvtkLbRfnX0vSKXFlIr6miVnweHSOL7iwoKIJ56V0ZZNoUTqtoyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuR8yUjKm4Sr07tFi4oEFaIC-DD8AgWzwbcg1grdcEmnO4U8oWXeTaxPpkV4mUf-nQRgA38KOuf7pi_pYc3dppnHtccZNuBVFfTuYR_H1FdMjQwhPnNBrHMTo63cft4BYYRkNw0njidWX2wUdE9y7hXRQhIJ3sJW2CCsLFnpKicCafvw8WkNlts0NDCUH9kFVWR3JYcdTfxp0RSpd_ItypCJWrGaFhBA2H0f91st-3M8SCXQTKX3Q0rGsNZT59Hh6zx3b8vM04BBs4WCAPDH471a7jVr5hHyuNaN6bechX_G3FUOdpBsQx2QF3lSi9cWyPIniga4PwHEsDYuipJgbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzX5PQf1aB-sUGiiC4kzqBd1igphy4wrzkRlFVgFcBOXxSxFor7lOQn0L6f0w4Rw54HgCzCV48VZYoma4IyLE0-mahJX5fVJj6dCPm__Tq1TXzublHzJyIe-0aey7azdPzxJzvpgadmBvc1a3S9_7w8z9AXPDwvm6jGxXKx5JzBIePKJq3dBJgT-BcSdztzOUWSQ1ggu-cmydW-ZLlqzXNU50X-H3O0xPIvYFHcqRiP2dFudgfYuCGcv9DSBORZqMq6VibeI8t5czCz64h-QDeUChiBXQuAi_cjGWE4qN3-7Wof1cWOhAahoeaXLc92h6vwGlG8hRIax_obuR2_muQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTvBdT5O3he3iXNQ_T9TkUAgpxvIgdlpLBZChjlykofWJjixvIFmx1qHRu-xSuZ5AqUt1-Q7-PTehOTzRmNHNeHXHlo3HnDw65l9r3ecNNpUveOi30xxiK5FYUk36izdi8hhp60R3RMIIcUY4d3iCKVuv1LzMapRksfWvGjDwZCxPciSZ98YBWU8vC6lRV8j0tzIW878ozVKey2pcnuZoUA-9bF1tZaRK4Z171PYRoID7P-DGPtDjL-tewyjydP8qibLAI6aDF4uTZJbPBgFayyi4-ozSi8q_da64MUlvuVLzPZ47RGdAOJeYkDxQarxOOImyR1pjPq8JPYq6vy5MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22155">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/az2oeAI1OVjGLCQmFibqwZ3tAFSTzzHyge8dnH0x7SeMHu_jtNJqVxfOGTfNDWw3ipASw381bovjfOZcnuaIaCp48JL6QyHOrOA8uiUKjgFUL8etNkGtPS_QCa6F0Ee9PInin07Jd3eH3_f545qnXq9yydro5qVVmjJgKWpQ4E2NQeeXoi4DHlCeI5MEgdtrPMru_P0O6bMXs_iToY7Da_IUIJAD9-yLAHKSEXeQnrnt8PgAxYjW4wqmjbAM5tXJSSkVEctzjCZKYN1bJVbacU76fg4_Cx_58YbGTuv6CkfEttNufT-BUIPyl9Kv5dVFYEgHU7OUwOg4nUG8OU-VBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورودی کانال VIP بتمونو رایگان کردم
؛
خواستم یحالی بهتون بدم هر کی جوین شه تا ابد میمونه
💯
https://t.me/+--L2Hz5HpiY1YWZk
💎
#تبلیغ‌نیست
💎
👀
کانال وی ای پی رایگان برای همه
👀</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/persiana_Soccer/22155" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCYc6ECHk3SLagFyf3Vf1z628GNBxtGXP0FAeV-ZE98auwMPUWfE0Ft6dHqe2KJnELUK8Zqpz9WPPZvZEWuP_KbfW1NG4vsitxX9WmsvBbYyOm6-w1cRquQeVyqCdb2ZPowKkj6hAhY91e7jUcz4zFvtBB_dtHCBe17N9KwSqBFK29uRMAN8WyL3SdFU_cIxTZ3fyOvhHGTMhPFR85wq-Vv7CLQ8Ji34Wf5axLr0QIaT7nIVON-lByCsBbbyC7CcnHys88JFBvaikZclskXgFmMlgWOLatdo_wlCqZQNVQm_eWw_i9R2q3diLEJ8UZczAhJqtnF9hCE4uGXjaIlhGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRab_-Ge5Hc3eFJoIujQp9cHcxwMq-w5fXGx601nwIaTcyGndKX5Q2Idq4cu31zdy4zXCsaIYex6esm51zMvDtQDI8p5yg_eJScadFLiEYnunTQVzk4JpnxMdghGj1NrAQxmo8JKtrjE_l3O7Y0xgUhS6-qTu-CjqWA2KgB3hsImqGTknX9D3R9G44A2UwyTEZWBepamuJ3emSSr7bad4SEM7yfv3eLmwxhbkc4zW8KSw_Ld9_qJS4GyVlXN3LZW0TukPOUWT22bC3WXmdyYA3MeAODezC4jd5KDROuA8UxYOHxPMyHnWlkmXwUsovZgKMfnnGCXpwN71gx0XVDF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSSGw6gLDyonOF4X6gC803SbhgMoOil8AWG4gYlShM1yxBtXt_YHp_KgMFcvG1iGFWmhm8JHbb1hzlnmBkfG6m75xyTs1SFzbQHOaJIVTWjR1jGhMHKdEJoBfm4YTD3Qjs_9RBsytASJEYxY_EbUM9e3FIBK2ng8yR7b9_hhHaBrwANjxrDHP_d6M7t30HPLQNYEqJujawTlQflhP8G1svK-8eJ0W1DFw6GkK4ZazjQGueQXpJDgYAlU8DCrZNmdi9lQX-RBbb_q7snKoxOMstdoq-3NrAC5R8kgS_X55buPtf3Uuqnv8imS184aLf_KjwhQeJf9UqtBsZKn0I_XQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCHtrwvtbSbGKYvxa3tUPpTG1q-3hK2ZePRt_OHECwsnTgq3vS3S7FJ-CCWnQ91DEWEqyH3ptwgS24T4K0ieTbogOQdmuZGomwvZGQAiRoX2DSg4PmueQpuRjJmH3Ifwi2j8wOmgxVpWwIAV5n0ngfnTGOf3a_nMqNFwlgOLK-dKK_5x-zAIUbouzQhoWIF69MTzVjzfFgPj07oAzDtb9PNV2d7qUSgFo1HZhE02yKmzLzRAF5PCFoI1-xyeoTPW7j2teDfuE4GyOSmAVsN4Nk0baalmVfiABrnYdiosQQ7V9sJFAQIOkBYJeVaNG8xhlunaPd7eED1vzvcVFLISkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22150">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
⭕️
⭕️
بچهای پرشیانا
باعلیرضا صحبت کردم هر گیگ کافینگ‌رو ۲۱۰# میده‌سرعتش واقعا محشره اینستاگرام توییتر تلگرام به راحتی بالا میاره
✅
تضمینی
✅
بدون قطعی
✅
بدون ضریب
✅
به همراه لینک ساب
✅
سرعت عالی
اینم ایدیش برید هر چند گیگ لازم دارید ازش بخرید پایین ترین قیمت تلگرام میده
👇
@Alireza_mosve</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/persiana_Soccer/22150" target="_blank">📅 15:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pattams6lDxb4XpAjRsaLuh_oOdIS6HVlnpxdGImlbyK1opyPx6l6MaSr8h2SLS3iV2SXUdsuJ555GaTjfOdgNm0EkvoqD1CgLFcx0n5F6L_04tfaZn178ZDXngqGA11XNX5sew2HARPR0fOBCrwmLn5NFuOfNSQVVISwCt4eC3p-NVTbwiwEaR1quH1FsPKM0AekZ5IQMkcv5iC9-qXeVBnB6qLiHCz9OlvHtfbsojXScSTdLbNBV8FhXxJMkOkfc28ZuU48gBcKc-qFy1b3EoaTcNqjEIFyPtAaht2rB5O-GuhOR7N6doak8ewo_xLTA33roOO7G8jKYxWA_uXaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIO8VfwE6nLGUeJb5vE433a6Rg41CYwYuvDHpIX01VEv8RKG43enPlyPbFLwnR2siGsdDvF8SRjcWCBPFCwA1UaG8ttc4xiVwXo3-Pv0NV9MfOzK_lIVbUK2YRvxXh5dQ42QhYc0x-eyuyt00L4zMBocqQN2yMUdlHyylloCp40Wo62WXvquXAVJJiOQO6xEk8O4y5SeUo6etkMr9eVDGy9WtpW8MSg891nAAKG7nZFnBNj7i7v9RrRsbYqrKVN3BG2vev2KIce42VPrI0A5LN-Nt-wCyxh-pnq5r19MDpDs5TZ-m-I9qZJ9So6nPDxAm0XSf9xIN79XbKheUSkd_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_OX2msRDN2SlDMHlox5eq47CkLxQSZyUqW8uOXjzQccZ6-Ux2seZGrOJYp26c1StjvZoPJHi7XoQDbpZRW67qpsaOb0GohJpJjI5SunfEEbOEctgNkRZNiJw_x4FGTNCwIjk4gprRvd_v5mlEnvh2uPV8QArMVpS2vB11Fvq_0D3CO-PJvQYbIfvjc_6tr88kM1uoEgdMq44qTKNTWibzpl-tliwuKKxXZ5wLTrpzJEgvktOKbmMw7scRByIHXwW827xIV15TenkV8OUUSO5w_nYijtveKSZnB05v1ifKVYIx45QbmykDsfOTsKEnnY3AMzpss-3G65daX3aeHmcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2nHPpiWWgmRaFFfTRlBV6IQYw0-0XDnOMyPPxZAv59anRgEnEk_7wqIyZOZGYCd2rKbn3AfCurx91f2QbFtVblTQVaxKO-Iq0qu43vR5nIRYpr3BWEIMnYA3-11bTtAV6LbVnsCM54bw6ZTIcArHR5ludhd7KlSpmH0Cw5UazMgN2vn40iettmihWpZgOp0DYxS5NrCiYPNDrUnLjEzTYo4Fide7_bmxm8UtWCQsKGUYsSB8pTYOlZapyuXFYTO2WxEIdNljPCW81M6Do3RiYTxWezyYTMlHM_93qF0U9tsRzAT5nf0_h9ohglsYlmUujr-X-Dq50w0Z3w1xM0-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMjpt8NwCiI18hC1wwQ619bS-TB1eiDDVUwVlzFECRSfRU5TMw83P1SbvD66pHW3OgH3rKK3bPjssFWd08ELs8WxHEYBOlIHwtl6DK0CJPh8whTCIdkJpO5DivjoaHe5Pm4RF7TXohwCUVbIsUzIkzQYrJsn16_SeWZonTbUJvVAWSUQK8c_tP3SK0yfiSpLMPW56LRtHwkUs0cclJvxMVhW1uy48Xy1flASRliKDGNuniFpNOUVBAfOdiPXBcy1lpYmZm94UxfE6CQyTJwtFjSSaJXIamLrwtr-4na5z5YRPhE8LQwrFR3_KgmWs5Vn8p9TMTJ5ZNHx4T-3JSbGUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnksSfa-AvPXjxSEqG314blyQ0xPetpQ0x0kvDH9jfFgqwt-AS6Mn3OhZr2u9-EUDZt4qNX_yb7sp627MpP5emOBzTDT29sRqqENcRFWNx9OjbMXW-jA2tcK2ry0yosegyKp4uOwG4XxXdJ9cvhP_wlw-lJ4Z1c9bCszZB646A6fJwQobSiQOOf-NuPHTf-d-T2pVUG7tUcJOozSgSvGwlZ9kApfTzq1rSI1a6kbXE3_OySh2CLKtUcjbBbmAU_dyKEQptew4Wd3_j5yL4Pp8uRJ2r18hh9ypkDJO7EeBMORtX7ZCpqpjGiQzMwibzgc28T14yKRNE8bdBWaKVQ8SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
مانوئل نویر، گلر ۴۰ سالۀ تیم بایرن‌ مونیخ قرار دادش را برای یک فصل دیگر با این تیم تمدید کرد.
📊
آمار:
✅
۵۹۷ بازی برای بایرن
✅
۱۳ قهرمانی بوندس‌لیگا
✅
۵ قهرمانی جام حذفی
✅
دو قهرمانی لیگ قهرمانان
✅
دو قهرمانی جام جهانی باشگاه‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilbN_gme-dzR0MjvUrKPjJBCCepp9T5Hp9OktCYpPBEPwWIhesk6XZjKZIU6vnmX5E5Xh3_HlTKJUJBRwIZjNjW12HcmXy-1WcGzJY8gfoicMkt44w4q2a9IF7rRDFJs0jXLRrJxY-7klMVc2rDn3EeOeJqAklCNEscUDFG62OVAVyh3MM6DvQ22LFzrWjl132BzM1kLCI4mc8zaX3sic1fgnjKXQu760XvthH8_RnX1Cte0H_X5RpKpPgB0DqshWX7_d-DDmeDh_S6VlNXsteaI_USKg-2Y9XDEH4j5oE5nxey9XsXmJ5l3Xyi9z1ph6Mik_wQpZUpukiq1OCARGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cx0aspYnmYLiUx71vW5Lv3RSYaerO5s2d_UbQrti_usZCoz_UE_uUmr6gnEYRub6O6JQK57baMlzQV0Q-l_FT9Lz9IPAl-4gyErhTPpGOxs4GhG5T3isxoyFLw7dWO9Ia2iUeyQjOkrteIwxcHp7yVaF2ngqKMYJ4Q1qXlcQtV3Tir664GsN4x_jRoI0VeTh2DFJL5HVDBGgTou4T4B9ARTTm-4qPge6BqkYkkIOwls8ETm_NGX6UCR8JdNiDJEvDgihQRru1eT28Q0whL8hGSc-bFl5qwgl28UJVTk_TSOJ6bDotGSM3tZgN30gqnSV1FSe71vg_MzEO43WBpEFGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2RTqAGg2yRUd2oGomY6QrwXUJwhF3abHN01xhue9cKtRPBvTM0cHD7Ip4p_bgleyj7fcXqpfN3xfJohC9m14NLaUat1njfOvTz4RnqvBMENqxA1TORjWMJa1i6FndJKUH7eOSZlt63PYO9U_Ap8LJycjxh83iQE6JMwASxpQ0BJ_ZMmUN0GEeyus6mOc7xDt2CVWsFrKevhRRNlSeHy4kBZEsEZftzu5OIL_iYpqmh9aiI0ZZhZquabFy0tH7ZAGYowFTf-6SIcjTedCqH4dP3Co9Bfm7ZAw7I2P9FbVICg0HhxZxNxN8SECjsTBayCZuGWzd2cgICqeM7Dtm2xYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZr6CZDAKm5Y3ruFLLroPPw0izxnihGJFiL7VdSqA9L2Vd1whexLSR8DP-6PotoQ4PKb5lwEFNuvsL-83tfnZH_84qWwEzAkTUWwHGEPWrz3XwEFRVDOhlhZt4y2QPGCDd1QUsKsOGXyPi2F79RtFC9FZ3Irvq5DfWjIcy84B3a9zh1SbHFN9LcaoyV7_E_BZ5O5MwYr4R9ZNhI2UthD-jPvveCPOFTeBIdDWWZVyaQDTw8-tXHiw7WU4gIMmZOvGuD_GyEL7VdAjROHnlJRavt9oZXcAd9rTDRUFQzf2-Hfz8Q_SNGqQGZBl8eIoOP_tt8XfokJfyZg33rXAjv7Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FI9868W7GvPhJeI8CtWH0UO7tQB6YSHZwUWahsd1lhoE1qkC491BEAQ3CL14cKVhJnUMmZLVLQ_SerOhCbeEN5dU6gPiMHf_-GqhhBCcdwL5grmq-6aD1r22SBZTR-QqnXL6LwqRt76p302r3OhTSWik9cv804ZH0BP60uq4tQHYWqhmgBo5Uu_20HWmQ9mtxf0zTBbihIIFNyvB3IBt0amPFo4Slu_59-2_9kVxsVFzlgibO5MIWjhB75Hv6WEc_I62v0s0N7CjLkVlJTsRnlmdOXEXv-5FA3N4Ofrc4ZulPB8bLqks3IufAw6G5Nzq9rZO28POcu2MDGJ2J0IQ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-uRnzsw4Mvlw76qSIzgJ_GiEmKSEdv4Gp-cly52oTYzhP4CCucUc4mtjs0wdTAntUIP8aj-cBLN2ozxXUSPx5VkZ3j-ryZovsg5v2nDv5bjn2X6ha3BcNzk-sd8LvoG2hYCdrxadI8Mmi_S83LVq8vdtdNWQxMDnzNT6P5Mv6HE6GMViViypwg7BLQzBiXlIK1tEOyDpwRpTFK8Evh_dwkgA4UNaoiScZpF6VulnNUe6nIjEgZFqUYxacRD79pHvcc3dSJt6hfYIWVcOB48MSzZHvftBv16vl7KU68jI6V3jhcJVH_f3xHqJ-L1GwfuO9tqYNO22hPx1VGR9CMeuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Okb-gKMc59swEYskhzwLnafCtorGUWYb8f-vwN7chkMEVvfm9bfFCsAGlQmiVR1y19CF2HMu0OV6nLJC659mBhy0Hg1mzB4Dt8pGoTVopUlizoJ_l_IMT9w0cy633eZdKCnSq_aU9qzl7kwYy1LoZjXthyD-QPaUMP2UF6Zyp1tQIxQcIuAVfjJK466VJ19fa7rgPdrBUfdxF2Gkdy1BSKj4Ea2-4OhxSrTWhNgdNiCBc1vSyXlOOpk2t2RQeVQGh0xT-sONr7ilvJn5apoZrVkeBjvfD6cqMK91tdext70jmHMHYUoDyQG5leeeO-2BiZbLdL3rItPV2IC2ZWLxmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=gAso4GGcsyAHaU3chSQWfjsSiNUasvRYBhHOtaHNa_JSlzfp9g7LV8DIvtLk-p7PUyKIYFSxnnFBmXkaXzX0c-sDNVMy1hjYlXn_N-NH5soPrB6uEbhqIEsT0JRbzBbbZauJhSH_BnQnZ9lSJkY04M9FXrxefViB51dK2Bnn4FgkudneWHDv1l8QKU8z7ajtIyVn_1ZrrDwLRotAeSsFSS301p-F7SmelCG9vsCps2dG2DakZZ17lGPwoeCUjC4A33IF1SfGX8qil3GEOIqq6yzilgG2MRawOsWqAwqyIDgioE-izI_tq30UIoA59GLzxQrk6V19rx04aoGLXlHWtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=gAso4GGcsyAHaU3chSQWfjsSiNUasvRYBhHOtaHNa_JSlzfp9g7LV8DIvtLk-p7PUyKIYFSxnnFBmXkaXzX0c-sDNVMy1hjYlXn_N-NH5soPrB6uEbhqIEsT0JRbzBbbZauJhSH_BnQnZ9lSJkY04M9FXrxefViB51dK2Bnn4FgkudneWHDv1l8QKU8z7ajtIyVn_1ZrrDwLRotAeSsFSS301p-F7SmelCG9vsCps2dG2DakZZ17lGPwoeCUjC4A33IF1SfGX8qil3GEOIqq6yzilgG2MRawOsWqAwqyIDgioE-izI_tq30UIoA59GLzxQrk6V19rx04aoGLXlHWtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
👤
در شب درخشان لیونل مسی؛
پیروزی پرگل و ارزش مند اینترمیامی برابر سینسیناتی
اینترمیامی درشبی‌که‌مهمان‌سینسیناتی بود توانست با نتیجه 5-3 به پیروزی برسد. لیونل مسی در این دیدار موفق شد دو گل و 1 پاس گل به ثبت رساند تا نقش اول پیروزی تیمش باشد. با این عملکرد لیونل مسی به آمار 11 گل و 4 پاس‌گل در12 مسابقه فصل جدید ام ال اس رسید تا صدرنشین جدول اثرگذاری لیگ باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWFls_dcFJUlQkFJFfJFMn_jUjCcMginKbgDot1zC-A8P36E5FuV3YlmHqpd_Stgi4YjOUsEOJ3w_h82rZOvYZTWy9cWXXbnRKuPLhf0lx9O-ZovglXAacKxzp8GZGg2trDILBgAfEADJUkQw73IP-IBJFnxWniXfCc__vTljxjnOB-8nGmG11PwPymmoIxHPvWsjJ50JzkH8tvKUIrKPdC8A2HdifRnPJ6JqMMzr5-8ChTGQu_Gwgz9G8YepR-JtlKoEL4ztkPBS7NibD4fWr788oUfV2ZfOh2GFE0qve4vCcmkVjdVVOD0CA7eMHFQMrko6WNxrCEcnkSqBccyDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ztax8GyVtV3GWZTcBBqxgE9d0UiTH08y15OVecvsmyJF8LpD4pHstKXlB-dJsDSgs9fXY9GSqY7NHpDbz32i8ZfyToUWr8udK_p3h0JtSl0GUmebN4vs9hcGEwV9sdh5CY39cqHTbZB5cDFLaw1gcwS_xyCkRLV93oGGK6Dz3k13J46Lf-NCO18MO_3apPpdpgQ1Q0-BJajCkw7kgIH9pmQOJ-_azyUwZFdC3gUQ13LFhgSPYpg4DqUsf5pMkPakMswyqlUPwrJi_upOZpSEt7Iy0bZZ6cQlmjtzdx-DYBw4dVW4_T7XP9c39g-7UPHfbCJrzBfJW_NjjZER7ylurA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdVQIqDdQpRtjFC-3RPYB4pr468VNMKp3ICHl1Ih44Oli5ovwI0USqalFZ3-r2zSDmO_LpSIgD0P6UV1Am7xJ4QZ9D7GkvOc0S06GaAqJuEDAFGoAO2iYTcuj_MIQqk3EG40HUGySKtK7FE8BPSckuzE6p48TlWpzv8phR5wRWD0jOBV1IfNmrLI9UnYo2i4_KE-hgIYorMtXn4OVnqYhsdfX0UoCPcpaLIje72x3_9kCQNfNUWv7NvD5mxqjWymaFaDGnGYpcrksIRRA_XcM2O27OxRMh4nuHu3dAj-VxCDcj2saK2IVqrRuYjO9QI_ayoPulSj8jy7RXknQMJhEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dub_PTcy_7GNrrE2Qwe9kSr6liDxfF7M3jqMR9DhkQlsQMNEO65o38r3VrBhRUfSBYUEMBl6INVh08ON9jQMqypjOsO3YE_BkXCHCHw-PbrusHM3FcRovPzMX146oWM8twgI9QUd41iXxcaDtTzye8g7cCGU8TQvQo3j9UpjiuPz7d3794OD_KFxWMwhv_LmW6qWkunFVnC7M3sSY8_Gp1VMYqZ1RTVbnWUb2YCbDBPJP1wLJgZ5QG03CbK-RDWuqsY2yhUNyXl5Krgw6lyTaskKF-7JaD6Rr67hI2matzSWVTpL2UijBQ0lyMdEELEKlUtOu3h0SyxmZjtIGTNsEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUp0YbJ-nheyAzvhbZepLWjRh1lEpc-mrNOTpc7BrUhoHrM825ZcQK_BJeCBku1o7kyzB1qrd683OEgLe18JKt8ijZUjX0Sv6mretLCKWMNHxCXhykycNHnNlhaUcUjbGH2qC9dAsJ3lN0byatsW74RFNCnnvMG0Xaa2cmVT_VSoTCerYYHgsAvA6ouEEvogb7wf1CUHbYfBCf2BItbaoFHKzSKLaiv6RpiXSCFtQpmad6_YoW-faH5gC5gOUEj0Mh9Rp7E7NYfi_V_M5CbFJHWli1nq5oKAN4KXk9j2bRTUooo1inhaiUloYPY0EfTHNm4Db8CnpPdo5W2vYiaV6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zhg0wJRfyAtvzMwRGMhVIAo1XOXuMEf8mTjSGi0ZOAD68dnXZySGBTzU-HP54o6zAGmSala2qaMkxk1onXAyklznO-wAfuiRjsPmLzRdSbo1LOkSAHKKoxFn62TikzAIw4mOU2EFGOYxmyOAUYP_FlbUi3l5pD_IHwoaXVdGBWRDN2EoeDvsUL0It2eUIzR9YRSFJwMVsDBBxRFHq_tqQCHpT4JstTbHhMQUesCFM3d_slMZI1K6K-t99iiWNJxliY-zlTrIS95gNB7OF-McPghExH6RTEA3jYfh6ToA-rzFQw3qUN1tDKSZNc1Hm1xzAv3Xiej0b6iUythlEXA9Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgCqWetFaO26PjuakUHWM88oPR8IWVkfJ8NBeVuif2seT2zRex1SD4q39Tb3VHafFtnvimSF-_spCKkUrKySCHmNfmwrIY-yRYWQY5IIlKpC2eL7uD7kGo6TlEJqBjLaXOtMg_Hj0DJpRGBo2WrTQ9Ujtbv55xjzpZRxCZ6_FxWe0-1ojd_YO8JQ7Ax__uH6gLKdyVHg8yzxRq8J7bk9xQRKHpUdhpHgBt-TAJxuYfM8i25r28q44aBGMNpN84q5XiaQ2GsJagkw0kcRQQ0z98K8zcJMWKa1_kFzcPbt-WzuO5HpWITQHhmSiFASiupl4Wst2fYJzJiT4GTw4G_uxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxkPsPIRkAuzEy3kNR1TtTTbLDrBa22yVIFECy-HVQHdrpsz5pV7Pj_lKGS1LAvO0qOqUGEBZnzWKcNBqw-kuyI8zw6VF2AikI2Z3F5eTDHt3gJQTnnXYPCH5rVZRdDIHkVJ9wTwQpXqSUYI34zpDj9ux2p9_YTLh2cVD5cv-x-2C3EmVurm6q7MO_WnI8Eehlaq86sbuO1xAElN4AOo7nvpDtvsp_N0eGY9N8kc6vEKf-WKQCWouGwvJYpn8-fVZlpsbCtUOTpRJB2iA617ez9Jo4PGlqV3wEJmpEtRzaXjbW7bhqymBFiVt0Z77ed8IYDrQ7Hnj6DUQwWdgrQaoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=H2lgrGVLiZKgyFwSBMXgTeNLgdEpJwpOP0iCPk9Fk8QWG6G54lzuBcXoM4r59_daCFynvCWr63G7z2YMtiRF6dDxYWdhLY29gD9rT1ZkLiZ1AMfYPjFWcKedS0k0qom2nIE1OfLRRJM-IevflEOOj2pA7ZNHvWg_wuW36IqDcMVlRfis1R77ZBI5mqdFGgFlbuf8IuBHOQmbRZR16jXYFnYns-IeTYD2qnLMcC9WkowIpVx90tq6cL_jAi4YL2t4UHEsBP92sWdRcCUvtwboRtEcWv8YmsUgPTW35rmPlBGaDQraKdcnf9rITQjiwHGOR4ufAUlbAVS6g_csxIW1cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=H2lgrGVLiZKgyFwSBMXgTeNLgdEpJwpOP0iCPk9Fk8QWG6G54lzuBcXoM4r59_daCFynvCWr63G7z2YMtiRF6dDxYWdhLY29gD9rT1ZkLiZ1AMfYPjFWcKedS0k0qom2nIE1OfLRRJM-IevflEOOj2pA7ZNHvWg_wuW36IqDcMVlRfis1R77ZBI5mqdFGgFlbuf8IuBHOQmbRZR16jXYFnYns-IeTYD2qnLMcC9WkowIpVx90tq6cL_jAi4YL2t4UHEsBP92sWdRcCUvtwboRtEcWv8YmsUgPTW35rmPlBGaDQraKdcnf9rITQjiwHGOR4ufAUlbAVS6g_csxIW1cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXN4RFA36aJNfjsdBmQ9JjKaeb2ZmtFNAL_ZpTBoJwacRiWG3HqrJxj5cS-dFnM46d9NDSCsqDGBA9pRx1MTdTHT770MqW6yRe7urIkMNHdnoxw8sAPk1gJO7tff7F1n260qCktiuArB71zbdEI1uv2ttxFDv8ym_W01_LBJXIk8XWpcsPMsKZWMJIgPSfkDW7IkkrBb1QKNedY9XZY9B1ZNiaIwQnCckhYRTcKcUmJQVBScBrR8kq825vVqx9V5ObKU8NJ0tr1dwXb2-tg-scx-8-NArPgH5JiDA7gmnr5VGqWaN_SDn9LNYRs6Z3jm2wcVgSuxfQZTN0YJpFmQHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Er-fDk9gKM0RhdUiyliUrU35pjHl_sW1l6c-gyOf3sqFSj2HK36-Mzs_uEhVXnK0RKPQIhNSC8ZsSy9GSL4BVxI7zK-yv8Ha43KbLJVNeODVXKwzq7CuM9yX2puG0t-u0mmPUCAnmcx-2pV0MYhvWcgQ19HTD7LniJseKYro75flKRfp6eRH8Szw_utM04PJDLUGUTnq3uQt7B3Hc8S1jYeCVJo9vZhwFIbDW_FeA0JtPYHQpieaNVlSw69xKq13oa5zWdO6xPX6zIgWIIH4MmV5FwFggJWNnZB7rYquBHBV_5KiGfRlO0QBtN0kbHA8UdMHAeiQqxL52yL4Pd8xJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=s97BJg2ZVmYsgi215arl7tV9XT8fD3UuW5bXsp30sVZO2NUKK4jiR6udGtkBKiO70EOavFddSCZcA7f2ZGlIUj5DuC_Zfsgz6s83qhqM0gwnwTgUuOe6LCaiUHEncRK660IysJqC34SiRKzV6cVCW_IaoEHDsGRqCphSWw8d7Hh9bn0CDkX2PZBhClZs0Q1SKUjarGfCEbOz9KJA7cqRQ_xbguMEFw3ZZuIvbq_awi9zsOqcFgML-JSRItP4v5TBCFsQZzIv14_60v-0zySy-rDc_IyKxU4Z3_WvJLo-NUAcCi8-ezfLNM3nBDL03dnusHsvgDWCA0Mh5vkhwQUZNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=s97BJg2ZVmYsgi215arl7tV9XT8fD3UuW5bXsp30sVZO2NUKK4jiR6udGtkBKiO70EOavFddSCZcA7f2ZGlIUj5DuC_Zfsgz6s83qhqM0gwnwTgUuOe6LCaiUHEncRK660IysJqC34SiRKzV6cVCW_IaoEHDsGRqCphSWw8d7Hh9bn0CDkX2PZBhClZs0Q1SKUjarGfCEbOz9KJA7cqRQ_xbguMEFw3ZZuIvbq_awi9zsOqcFgML-JSRItP4v5TBCFsQZzIv14_60v-0zySy-rDc_IyKxU4Z3_WvJLo-NUAcCi8-ezfLNM3nBDL03dnusHsvgDWCA0Mh5vkhwQUZNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHJxsCB357iyHOYKnAO5TrlwAHEex6saU3KGddQf7X2qO7FxvzzNKzOidAVc_CSHwH_v1aR11uCOZRz_XwEIk6oSZ_sf0Uj6PfPaFBTibUBFdxC9ShRPR9l7AON4ojy_Zs0JJ8gdNVk9FYCWbX1EQ8-3xhCuXCWtQU_KRWldZf6cYvQ-ehvaTkKNvHwb5rSAyvL3EdF1eiCRUUoNIg6QlEYTPfB-2c47jFLRhszrKGzZ6Hh7oOsaA-8ikJRN6ve4soOKwu5AO8po5rcyknJwAcuTfwP3taCDt16h5cLkiHaQxTu7gQ1H8dRJGt7Bxm_EjX1n51HYjod2me22cKfOCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BbuqmqLKTKqKXQf90BfCKQusMZOKCMk42obNIvSsOPCju14yhunE2EHbW85F4sQEYLQA00tm0gd5P2o2meixgPj7z7ML79MipJCm-XuyPKqqKCwD96auisjrtYI8W4_L3quftahMb5LQo7boWCgZ7l80mS-gO7hacB4Gbj_v1yz3pk7vaNqJYmfzmDG0sA1pqi8eTYNnp8TFT5AANhNve0XjNkyXKd1Gi3otQjAvr7vMrqiZJrN1aPt8Rof66ETH1RGdGSXPcSZkurTsnijLCL-RSm6C1jVybk2YQlF7ssK58F6xwJCV3UvHZ_ymjt5884qVhk29d3vXlihuOFdlEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه درکنار دوست دختر خوشگلش رقبای بزرگی‌مثل
امباپه
و
چرکی
روپشت سر گذاشت و به عنوان بهترین لژیونر فرانسوی سال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPKPKRiiqulzmE_Qzn7B5wnhcYZhNDjJ9C8AF1TTMn9FfuWHmxOXqaDrZInLevITU1yGqiXOjeadSPkxAUxV73b5Kw1BltYKKtppD5atYlY-B4cdLdwA0MrNAQyz8GOIQTQoOG8w7qCZbHU-TVbRljAVUM4IAg3rzrPPQzU9ay9htyeN5jYAmBvayEwVIq0k5lq2H2w0gAM2we17QWj-hqxVuxwoWy4D6Ax2BdOqFGQthIE2iqIkzl2ZkwVlWeuz9bisdTXUZ8bQqw673x4CUjXUOskkOb8M-2E75Lt4xxCTzZq576g_o_AzQmNks9oCSSYZOMErXWfEb8MRFEmA7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSC4joQ4_KbJaF5RXeYzspQ00TgisszuLVWlFUaC4wSnO30F5tATrbd7GpelbSpL_sAS0V_8fAMOZokNxwh-t7yx1TcZ_rHESGKP2vdnVeu3mu1MdtRa6KC9ktaibwt_q96UK4hZhOQcepiKM38gt1CzexxbAdvSyMKk5xSo7XaFZ5wQWynQQ74ncM00pcaUsqT7Ym6TlIJCTRovsstD64thHkdSo89N19qIHPd4jRfYfLJKgbqEQPpkomGYRQUe9XQcbdpEMFShyQAvSOEp52I5wMPa9BztHluOZLfcu4SBJs1tcNWxKRxiE5DuOoP75dikgVOQxCbadkVrX4sf3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvZI9Rrzdxav39alGzP5Pq9nd0syhJQQ7jjeHnNTMNZbb7_WlMSbItyuqb6BQMtlBB_-sAdwwCdImZhT2xcIPin9fSOWbuhzurpiAQ-9G37WbmHwfuvFUrA8soTKlkNz3eZWUnwjyX0zXfwOFsqwgPBnXwIrdqcUCJ1OevwSoxr5NCt5pelUpq24GNIldebst3vQMQTStcBrcSDamo0KebtAgfsV0VY4WpQKsBEHgSI9knpXGGb9dy4aRY6kCquBsh8FIBiWFZ7t86BTCFmM6c1gGuX2Sc-fGgCzJjyRZOAjuQacqGBpaAdYo7vaMNBf9uHf-nui6Z2Rbm4YesyDsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TK3UwvbNX5MSHMAb64VfAGBSw1gdgySyg9DaO4i6_cuRvFWe08NdwXqei_S_q36Iqd1Y98K_2PjzxzbmaJu08rlMLHcn0RuGP1x29bzty0jOog-UgydJPNp5oaWaZnbbSc98x_xdBEaYCBaSJr60HZJUu1WlfjEw_3462RwPnyVabKSCIhsZfeZh5DPEM0pUn87X3NTEYMbpq5ZZzj86UfEh9vQWvjmrgH0cHrxF-lmqL7w8q6NfQL4e8IAjXEt8pf4VCBiqvs_rKd6Mqxqcf-0qLRAWO0xEKLy-FSOEMwV1XTKkd1ydnFFHwbt1BgG08aJPi34WDOHACUdyy0i-8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5BLWgVyZjKoR-C4uTWvU3CqOsIZs2z_r30_4LqUNTBP803_wv0tuN_Rmt4XT61gpoZ_4K0WHzdH7i-f_L9VqgdHDQj0rz2y2y5GPf6QfGu7wN7-qYQ6-Wd9LGf9hOrGv-eBdX4xwuV3qh1HCUOSGcc7KIVlafRqChnHH0ktVjemxvry_Nf-De705Y4Gg0_axJcscQVNImeSRnWyGTV-rW1ty5gQkDB1P32FJG50fPnr9BDjOZWgi2RSmNXcCV3RP5QdCfg5FJw37QKPImB_xdvoQkyBy3ohgWT0x0kD9IiSIsVF0OesIES1LSDIMP8uAPUO3fUEJGg8zHTnVj56Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3XMin6fQ8l7urnnE3Gx17w3gktzxnX_LOcrJV-RVK6UqraXeGBeUj9duDirjIf2-YhIcZM_z2BNPR-0tL2T22y5oV9E7NI5dYra3Gt0dtaWyoGrX34W7QuB-N8DhDyFdq3LL5fCbst6iookxxW4_ffonEFfA41mz0Afziu_B1qhxvinDgHhg4mKn07NwDcYo0bqL1pEbEUVOcNPBiFYgdXLGldDyEshtazmAlK1EqCIMGyAroPL6XNU4KkdnO9vwyIamr5x6_VwvThQvUATshbRT7oU2SZGvzY7b7KglmHFZi7KqlQB2hwnGEkkoIIfWU4AukT0jRB8AFS6q54IBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkBX8s7XmgKTgLa6ohHs-nOEg9Xvi4q9g-5fwjQmL4T3V0e6Kr45zcAw42mUFFHK15zbt6Ny0T4MSU4qYGO1j0hq-LCOA6iB1AU0IR-wT1phhdC5QBaF4ly0vzLmJK27At_KaYLOFOVhJ2k061b_Ambu3EYv5dB_6YSWr9URhiEzwHVzgpahEBJ48yVUqLBsWNO4VX9sj5MQNAxvWoRY71pXXQ4HyKimAtIVvrVhNPrMK2PcLk7GkcvoNDXQZE1-zqqqAxyd6nD-S_KAL3DZYkN3xNZDd4urjVUKK-4N5pR8BKeh8QeK5CIN5Wp6_7lcQhIE83PhhNJ0Q3ZmrkjdPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4vacpmBFRqCp6GJaWtvvPaD_LwIDHyUhyeTuM2Q_QwKgLMWVrU6kanxc7eHpOaVw0gcYfQzLx4spUGvnx2ePOE2it8JisRVZHLYOq9iVQE2-C5XMB6R-HtDxDU-wy-1uW5rX3-GbE8TkFPXaMIj8y104rA6_Nc1wcKJNH6JHsQjf9edOLjeiuj5NnlVnsNb_XuvpX1jrdxOgnRs0o8mIalYLkBGwODHjlKnFOw7hf-aJyUpzUAVrnwKZylbQIHjjaJQh-HmGT_x5v_-tjESw05BzerUZlpPDRCR6HxGPyXM7il-1RxgMs1xbRAYq_bM0Q4A6C66E5QHKT0aUGNSiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_Emb0CQdVir1wX4rWrePwl_YMuiCr4T9bKH-uoSUCWB8U5RH2xyXPIoYiV92bW0rXNLWYVAAD-Ou4zuH668hAH7rI17jZwaopgn6FXV8G6cX48p4LU9oSBRUjFKly7I0wB9m7YWEZ15NOxHdq2xVWt_EDtbJ71agRYIfYA8VPbl59pN3gVtJLFfWB7AyS75lxt9otbJXMD4t5zdi1nW-TY3-sb0WWQc5o0Ysk1UYv6C7HkYORoIJrh_dOeumg2Zd6wAdNVYkPBgZm_QyJ0XBUtYltL9ddXCVszaBfKtW2XKr1x_xBOTzpPX4bFL-k7B_m1j31FZuFM4NvusoypAww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFE68-ifR0ApJLLt84OSoGht3kv7G3k3VBqGV7GyXgD6AwktfZqWj9UKp_wcIK9haHeaPtLbZNVNxCDPE-tFpnuAgyzdBUf-FZZ7wnbQVMcjjTfDmDbKJJUxtHqjd70Ne1PW1mwY4DuPZq1c0aaeZCEZpCiczMnxdUk4Alxo-mloqx-wmY8Xcut5cqd4Ur62dpyDbr8AzPm3HpBu330Kd5vVAlhtgw1j3l86DztuEcVJE7pGJ5SUKUerBx0mCuG4xtdmCrd4UFXafFUlo_aP7PqNe0SMFvPjuoANifk-llZ2hBz5J6hWR7P3xuQImhXTeTWrLIxBD873SvB9pNEzrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYKcWzvT-hcpiRI8Czw7Jo6M_KbAuadsOLv6ztIPLHj0SHUFf763PzPW15WzDHVAdToAbqtF5yr4n60G-KNLmEYumcdkknQNryMXtCkRrcHCFVLQJpaz6G-eF5Cagb6anQhtWidqx4DzOkdAmng0_1Dn_vlFX0Pmgeyo72q6nsY9Iahg-QKy3KOBLsUKBjUDeNd5-nqA3aURYyljki0orXqktwQJ8tYq7Iylb4NvIRiZHX1BzM2raJyz3lVly3bjWrBlf5nr9WJzv1xdqtDHu-gDS-YxZlYt2NACMChSmgGxrNzNdb6T1rzXk6lEOHubHm5iQujdDIDOGF8nVFT6pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgDBlChby31fEgo8p2V6Ail2X2WTmWq3qoviFU38twcoRX36LZ3UV8DVqs4VIMm-cKeDivJWtv6PLhy1rpMHPC-SgeSXsoX_RRf6sKmNK40uBx2evZrWKPp0PUcrhNRa-2f9SZamgbQIHF0OY4wJknXMo2-EaLZZyNHq60x1_3M_6kVU5816-cEpbFnk8dlVeDmHZXeh_CrJAxnnnYeMzS38YIEzgWNwRjLk6kiT-5tnDg3Fpi4n_xFLslSuU7NoihLfgB3E-e2IbXX6rARqRnDrIIgr4yUxWGJnOhbf2SCRD8gRzZjf1ZZ2u8YQ7HgQFIGtXAg3GvVUQyzwG_dNGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=QjMdWh6FhqeggeE7EQeJKYGH92ti9p7jnZaW5pS38qC9dYnJ1L-fDLbQxv-6tQleuaOC6Ze22LTeNbZHcgXkuHTHVAfaastdXLmsaWLwTSsLsi7iSVzELgR2_ZSuUhtUi7Amb31FeJDDLp-EQvmQpnVeGUxNiu7lwlcK4C-HBwAHMgCQpOQN6QQmE3vB9K3q1HtROUHmAcBT7LvAmmipHnleqEscI-SPRo_QqpX8jFfZAxTojruoQjiJAEVnpv_7DKdoYtqxM1gHV5ReXDM6RugT1zqtoQcopwoayYftGHaFJ-gg6YygloyAz0dDUdU97jdDnltZzgJ6Ve9dvv91Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=QjMdWh6FhqeggeE7EQeJKYGH92ti9p7jnZaW5pS38qC9dYnJ1L-fDLbQxv-6tQleuaOC6Ze22LTeNbZHcgXkuHTHVAfaastdXLmsaWLwTSsLsi7iSVzELgR2_ZSuUhtUi7Amb31FeJDDLp-EQvmQpnVeGUxNiu7lwlcK4C-HBwAHMgCQpOQN6QQmE3vB9K3q1HtROUHmAcBT7LvAmmipHnleqEscI-SPRo_QqpX8jFfZAxTojruoQjiJAEVnpv_7DKdoYtqxM1gHV5ReXDM6RugT1zqtoQcopwoayYftGHaFJ-gg6YygloyAz0dDUdU97jdDnltZzgJ6Ve9dvv91Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2xksTde3k7yCc8GtVNiop_pWseyzD7b4fwxikO0zklPouO4KZV9kbKbCbpOwLAnHk9c-r_QV6BTXMbXsFCgs4EmPjYPSw_soKBCAI7xz-DSRNZlrSsGfebRhqFt4wN3UhZ5ULVANsRaFPXm_4qVasUHcCC5eD9we34WCDjH4e4J77AjOBBii01nbJwRnL8YHW0m_EkKh3eegWXUYhOvCKcWA3OS_-8mhAeldDvasFsR9VbEBybW4ibdtCYDm4PyBdN7fVeH8G3vyiYN9JcAVtUmNYNEElyJ_77amLTzeWlaFx5bb8VFekCfUaZvhHuA5JC2NUL6CInV2k04xeGh9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sd_TF-lqlruBVPC6LQxwRDgQ-ObiyYHUDuOCdlj5uJu4KJwFRfq3N-Skgw2wqfVRAep-IqouKeF5Bv7nayJAAFQxF9JKatcVCI0zJ6tszBqGqwYVFgWPSp4U1Y3oyVaZr38hyKRy8Lopfi-5HiSt-yndAsSM2G7fWH01I6JJ4qhhD5Iu-LYoCSGqNW7QZmv5JZCpb2dFTwrQQDyg9wLMTJMf0djq8kmCtCM9CiQsDzgJ9W9Z-Lm75POfb0Gqt1tvc8ktSYPXQAsDDubl5ZM8yl5k1zAKjtfY6x0aRdgZ-bpA9qda4Rh8DwcAPWeu7Mo44vmfaMW_q9feFnJEW2Xl6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDhVF7G77LCVWHuV1VfBPzk4z47TuNd-ezZkVOE0P-Jw2QKQVQKtrDnwnWxTYuzBxJZvgtaLSUVIrfEQq1C0YSZOIrYy3zgyHobbORuLA0XkwM9PjgETL2W_-mDE7bHgir553Ueo0MCVVJMceBCaTyiE5csWaJ5-RoY6p0sDifQY0QPH-003sMkKkVqsulEH67gvQke9zhD9kMut2i_MOJ53M0_vafC4jvIbCqe3J5jm5igwrRFq8tdKGFT3sJQC_QP41T0-eQXOL0n4p6xUTSw53JQ0G9awx1dL1VyBQqb8XlgDsF-lixYF2oS2p_qE_GGzzTQw8FSmka9-xiahYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnOYKm49FBzlDb73Bm-4jW-c8e3x_p429MSMy_XP8IcRUQ3AtKRTrtkmlehLthvww7XlxRNULA2vZxC4K3k7e9WdrzLREM0BkuMOF2AUWrI9Q0TNX7owfGQdRvUnvDXJomvFL5Qns2rTfpJDznXT0inWTw0jnY5AkR9RfYkui_hrjFGPQm6ASCtyCiAs6gPNup1FSAD0WrLeZUl70BVYeN2t5Xvn_Z9ztCrXrP3l5XruNi2rLdakpaoK35klZX8COXNa8aQJuZbm7IaDHgVQna1OHTgY6Fk5aZ7HiCCTZfQnRcWdpcK7vpPocH4kMIp19AhCVanGuzUUfDpcwNq7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uq49AxLliGXwZ5FDANIIDo88SpiO_7hI57PW_LGJR3-JiqdpP2pIACnhYZ4kSoNKdv6A7mFv_TkoShAtMDQl-R_Noa8otHzJaBC900uHOrqBsV8fUI4so0nfyl5MZzya_iu5pLswK_dp8dLDyUWDQbwdWmXjWdVwur__yMvhh0wZ5PODtQhw4iGP3iYwxYw2XH7FSYI_BAPIeZCSTFPDxw-MTcEJ8J-Wg63h0qQLfU16RkhRusl_skKcDzS8FvSlBcmNpd_Mg-2AKV9mc3toq5oW89JMMbKyvrmL__E-Q6Ck6qeYVdg1bjzQP-stHEJS2hsGUQeWskqLwEiQ9NCokA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzprsBU_-NoahFxNE-ndZH6L6hU6KI90Rpqwg7gUCDF4MPgoVG42trfC3fwPnaBPpSWVGwVzoO7_xH8HcWAmu-dF-PyJy_AfzoFJV_PN2y3oZN7-F_Q6LNRM9LfeusgdlGbHbL8i7EzREjtg5DBrVT0qR9AtHO9Kcol1DwzXlR43T_9s2-TO5XEmnonhtY3WhOEagym2mCK5wda_xiFeTtxYRwqfnS1gTKG-JlOCSPv47yN_RZZQyIR8h8foovjn4NErxtImiHH_vhSy9k6yj6DNKX5LBwnibK_fxeXH3plrJrrRnjpMLp4Unm1-8KDjaW0nInhJmX8N0hOGsrftEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szYw4NtEXwdqD_YPLmQ4rOaIYzA0-dwufC3IDe-6-3fGOr2Z7sla9gyUIlKV50vjkAGSJgJfSyB9pz-l1RYkgVUDqUCLGu2EHuSW38KGfgxx6WlT8uAtI0cmfSkRMaucD_BPjDNXcam_g1_dBs5Vv9hTugAxpThnWU3DJ3rbN_JQmn1-veBIwl4xau3KUb52q4XzURe-xYcczmofRCMrBtisFiDFLqgV2UkJRfWPqSdQiMitzRcPpT3AsF8WomNv9mWb0fMOGs74JHOzSLyU9IZ41tbX8ZgiD_h0Ds7Kz6fpaAlftykjXlPEiHdtVKYfccXbkxV2AJFCdGFF3tGBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyo4hjoJH142dGccpt5fdG1SJhJfXRiDvfdErvgUqvmxsti9sF0yZyIFQawdbIQ9WG8iU02g0cpIkCt8j4Ct2Rq68KMDObRM6cgJcoBZoy29YRazNM2TpQuUDfISwbGfuKqq2T2aN1PeBiOT8EKLloLt7hIUJy01i47v8V-9tegjYYz_nyoYIfcfrm_YP_ZsORcQh-K3NQfHOU-AZrI-GDuWPP4hF_TLkM-Q85r66W-8VpB6V6XoMXh2t7hugkkn4UNfQKjwO4GhDCMLGrl1cVtUp4JHJyigR_HnRzVG378vEvjPoGa3IcdHmOYdqpPTqb48v1TryGtoWgs7PSOiig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKUfGnu5InYs0MPoLe0RSa4pEMritBkw5k0deZwd32ONTgcbWgoKrIQY1AwIF8Vxgh2Uvnyb6V2Nc5iI7oXzIAYI0x7xHglyz3pQR--URz2vHSalwuxN-SgYsS_D3lyePMkfGCBSngtKUvHdrkWmLe3jOAX7FV6YogxYY4fbAbQyS3HFd-htUMTdT0pfs_l6jDRtIyxy60LpJCAFaOCewNkEocnp1N8H1qYdlgsta3EoAsMzlY-zOKF3DOM6X5v_9suRru4rdMTDRa7i1Rs-STlGtGeiSwAByslC8CjF1ETBzBNg9r5mCIT7ly_J19WMC97-aFJj2-lzXBYtlZAMIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPdXjoVPNHxs42xg0JENo-uu4ejnF2dh6awvDU9GSOdSy2BYbBTPQWUvERBtTHJ_CDb7REiPErZfKAL6xW0WeURZ2CkGLK4zRbIpqo1IDvFo5RnE245Ss19MkBO1OyUgsYFvc46aqXN7GoDmP4O1eswr842a4Dj0KhJodDhUimYRJldNhvWuR9xKAwgcod7JC64ZS6rZ0xElOgPbpZbpWDOctsqWuXCc-OM-97vgX-HH0coZbzi_ffK0ynw1z4qUfzj42rkTojMJnfXwcM5fryqu8vhE7nsWk16httCaA6a3WD-N0LmdN5rSbgHgzw2g3ZTijGGpGdW9RbJY-0HIJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Omew26ItzIo1hLJ640sq0Y5lmidnD5RDqeeB8D-3n8JpF7hJmblI-vTiz_EYwrZzUmvjDPBOIZmLcYZE24h4bptcKFQ0nODsmOgRg7N-hf--tishGfYobvM0QzkPJwhM9gDmcVb7RDpLg3QQH802deVJ_wVqlagTk3fGI-aSTUdclEfeifZd8oTibpwD1aS-j-pMKg86-GXM_x9Fcboa3A6GxUf22Z9UzC_xl9RXirVw0hTiL071wNOupi1A2vOek392Q1RtSaB3HLfhg-S9PqlvLJY3ijKCqYJSgqVmgsRgKy9rRdIMGgTHvjIOyAo_BZdOzeQE7lrBwb65ovdHsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1SeIRukEkLMfxmREADvVtPNxHfliR93H5bO1EoaJa3qgWnB0nOWkRdlIsa0Ntp_CDY3MxyWn-m0xfEt0J1DSfZhox4aynpLfku3SxhZRZwmRhAT8nL2NRuyP84xRMTN7beVZSNq1wmjo5I-RttsdQgl1fVIyrpojuRmQkIG4OMoJhjJIm6EQGKmmcBVFQ_WNeqijB70Wrv41QvWNkMJ5J6UygvZDiiBzO2WGDpGKdbfNK4a3hMECqInjKlav1QS0_KBUskFemEMElHZpoSY0Ripfjen7x8ZdO07fppQrqkjck8DzasHtrQ5gzS5EzfXaYMjls-tmtD_GnBujWuXkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzdFf7u5sGQ8qTpD_FM7WhccLYc-lMXuOTiWUt94QlGwo_SbApjnOtIVHW8Jw7v3E4e1qB0qT2P-GjppaRmw_uVOfkVzZMVTqDfGL5vCbNU20WbsPewgVvYByttMiK777fYAsqaYhQ5pTP2XVYippCoegURK4cn167XSVNeC2DUXxscwrHYCSYtVi4EMcEgC7Y283pq8KO8FXcZ6mUz-lP3czXs8YcQGSKcnoSMRy9wgomwJmCJ_1apgFcBtJPwoCibzz7_-V3V7lpq6hwbJuwSCOSwWCPRRs99nk1aIDpUm06qLz6f1D6UkUpZd57OLa5918yCJeoHHPsooWZOSOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_Xh7BM1yFuR4Y52xKV0aPtRM0OtnmjcEgpRkjkIV_iz-fC7S2up3wz8cHE8hLbAjQqrMQFODAxCrWMn702LrBo2PyJVTUiN2rl3Jrrge7f397YeF1i9_0W_I7JDoaUR_sf1D9H4KK5VLIY_FLbomEbNjlmIw-91JyOf2P3VZOKjBXUkyKZNJF9It8WwM8FLG5JMjSctYXF6Z_IiVTXUOcyELOykjw4jl2fvpFluq2VsO55r1zbIDdMkkMAvveGfnxIiSOiI58Wk2TvSssmaYgFK0kBgM_2t2JKucIj72qkkTVKwtatvarYLZMdiXUQGWnbihd-SRoCddLhUpaJzjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSFGFRVjA73lmz2a65tXNoVrGna1mfT6vyo65kTqao3_g9lgjtu5QiMY0VUaalyDtpnMR2jOobdRoA6HLbN3KNM0I56hX22F0_wAamvETylMgTq4vpFdqz6nTPs2NfV6xz1l1JrQ-wzLp3elddUZQvmYv6g9bTa09ET0dfONgP041zzVp45Dpmn8vxgQgdCm8QlZsInXbABEgg2pIJHtBAdgIPhC0YtKIokvk8-65UObOC21Cl-glCMWW96ALBPLx8xfM21z7i8mBH6dqgNOobULqb8FZR6BwVTLsMfWDBn9gT_XHR9qczZ9UUkvdSms7B18LC1K3S09qV-Ja8kJWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZQLjWT7cMaYMechbTzpsPjMp99T09A9AsBrK2cid_cGw1cyI1VxRF-REwsaJVe8InOX-cFz-E74Ynprh-z756hs4GjxUgfFTmyvsUeQxd8_K4bqps6t5fAC674j3PkCHv-cd8J-Bda38vmk37xaU2d_m9hzwFaXqxMBd6lny75MoRsh4ZdYWARiqFpGQdTofV2uEE-uxJOvl5J8GgZFxfpBK5pSWsVDmHF1LDQJMK_VO2cmfdmmYEVBTSiDimS90eMsNJuNKEsuAqT8MdV_bkoWAn6pXKaIWKNgMA6pZ_R4J0Vc-9qSARsASsK1yuENSA3UzuBIeoCxGFkdzwQvug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgEBVx7qCvrUnparTytAk2QsPPc1cQt10-tU3LnB95-wwCKyOnxjzYmsBphLv3Vp79H_ktxmCmv7-Lgxs36LBRGDAlqkU4t1azg4XiBE4VQW2AXLmoPe40ob6zAUJuBbxnoJkPHD6qR04qHapeyQFR0xqFGGsbDVe5B1-Dx0pIqj4xCauwKKzMXp5Yq_4kWO4eVDNVHE9VYSS7ca_a1VpOF5DT94RymVHtw4fgrY9WGxARU4ggI8D0vVQ8SNmnWn9T6Ibfj6detEhwa42DD2BrM5TCtSWFLTS0eKNB_TiPI6oGle830y5WdI5jJjoW4uM7bc3Wy41xIdvGkkWe1GDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXD66bJnrL-105g13kMor7cFNk2AZ9H8x5TI_8mq4Si90SBqL-uSvDDo1LKoGALE7614sj-PlDjyINlthCKLGo4Q9h-whsbEecVh78juTYd1wDKQiVTtFfPiKG2Ik7clXJO8xQMpd-e0RnNcS5GcWstx8hoyIzZIEqS2mzs2tpc01fFXni9H6tPdK60XMrN0NHWq55ukOqmCV2DpdysJmAk2C0M-KP0MfmHKEjMM_wB7R32_SBXCt5w437oGSmZEQCKgGlK-ddV9J_vhj1OUFrS7AWc4kCosRnkz-rqg7_QzPPJNv_SZqbgkNRVgXUnY0PFS9ZLR0y8x6DVZrH8pVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fv26jWyMgwIWs215vbO-ELprm-6Eerq5AJI3bDimXiQur1ETfY7lsPxNiulSzfp9oo1Le32XHu0oLBpbamtBaA0jjlX_A2R8QSGJSjdj3booBncHypgwGgD1YQHEO_Oq3vzTPzR5T11i0pbeHqPkoXYXCSfhHwXF6bQyrbMOB7AdaQmLb-Y4TY7OjT1jbQPoNPu3-Dqn96eCnpOF7S9_1K_OQnJhStQHuM0TRl5jUXuzlUKA8WQuk3LbgltkSxbmk9-8QISraZSI8TmbtoCo6azNVYBg5qqz0NMK3DXyWr4sVv5m64HVJ1QdWVbdoaNwenr8U6mJZPTreUsY5osw8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmB4PJjWvxeylUd28OosxmdvfbrGQfZvTQLAkv4sQEabuDG2911dd3NKErpc1AGhUVODBVubAA_Us1eRVjEEqcHTCCbxWd3LIpII6OofEspoiV8zcONuB_WqSC7UQfvcJUKDBwIDHciVW7ZAaYg1dSEctOZ08jPLr7iTk3WVnDgnFaczI7FHKvZcMtXdcuiIcl-XFTTwaWM44C2PFTHi6jXUb4sdnewXJkKs1TUWeNO-vMkAwLdAp2aN9NT2-WfqsRTtRvuqyskcd-ABN-2DYhW8oSxWI35PUNT5gkGtclGel9ObLMJBEmwp7mQuJJHj8zlJFhfeIpMCtJXa5FVRmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZDTaqkFe1tciLk_zIUUJGRpOZvVYfUNtbU1RjNRKrVPtlsDf-x8iqmhIoN9UNLf30jvSSm-Y3c_QiNOX1ZKZTVytluQ2xjjniAv51Wz_akQiKEbZ1XGAi-WYMlh169u7UPsu8hTajYbE7ENaeICuU1m4LAq25O4YMf1thWmbxz6I4xkfIaN_GgvCnUMmQOllPWvIceGDQ8kTviKHF7_zYJp1SCwCkvDXStlywqJDqWwy-qDIeZkbUW0fvVlYiqHqDJEzHFXfeHOS0j0Dxz1l_KaoNdE1QhpVezBGsUdPa57pV75fEQCBZfS_LnrSAyq0Fspj9geAN6ANqG9NsQYiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛ رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‼️
هایلایتی‌از عملکردخیره‌کننده لیونل‌مسی در بازی شب گذشته اینتزمیامی مقابل تورنتو در لیگ MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNAvjLSZ3C9Zs1UupIu--jzAJu1gjCGGkcSPyY_4kmBWBhr4hQA8Ut64yiiE4fAC2dlz5W8_PfynbPwld-7PCb9nRbQqzrntOwFRYNWc6_2uTofDR3ILn-w3B-vePfJ9jPMDtPNDJUOaQMktLi1SveGtO3icj2C5nO8npHD-JezZlOr09WOnaUpyraooPoz7pjGczWZy_UKecMpuZJGbglZQbDU1zTNIwj8MovfKFVe3-maDkh2Hx_CeTavMMkNsG_BCSLQJiE_0tDwjLvZeiLXqvW-EKldBhVLbYUnlHRv_QmNlGtAAz6-IUMDhvHCLm5IoCKV6qrDt84y11n9atQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOBiOemtMr9pXjAa8AGAdsUXxeNOe3FF7WFlfiVKRrn-7c2_Y90cf59ZjYM2ulWu3wGQXTOLvV9FQH-yiYUC0GycMN74B26_uk4-aIGjnSJXusolaqi77agleBPscX2DMdzq4l0FoFsbPQ23--WkhelM-7tvjaZNfspKDarSIC3rRR8IOFJ-nRjFdOZiaDvxqZ-QhVGzGbTx8LpAtnck7Dc2b7tSs1d0Z8LtJmHDdKlHAbSw1A6tULIxIKvQzIktvpN9Bh5jSWakMqCTiSXFfyZPyzXiS-iiZ91xr3iE9nmYdy3AuJroTqNkUxw3tXXNNrSIT7StGlepEhEvgAWCng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=s8DFlLF4RRcGXequruKBpQAmHf5X2nyln7MaBbroPrOQzzvm63v8K8ip-39yWweBZz0iPQv2AhSu1ET7tPwLqPk2HyabiaM_Y5eMUFtoBLcnZRfRKwR3mHbBO3BebcqkPLHQYNqM3k7oE9HFMtriyW1IsHxVBmkX6Tu3lVNyeBYx7-e-c8CtP0klDc2maRAHTdePY9d40qAcqVWAIHLlCUDoNM0gUqj-CE44yybgCr9EinOh2SIvSbU8JjDd25WxqD_L1mqITfpsfxWo7azB8J_fC52XhqQPPMwwDFt0WNabnDcihIG64UcQwwOD52YS_Hd71g0T41BRe-OcYcIsYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=s8DFlLF4RRcGXequruKBpQAmHf5X2nyln7MaBbroPrOQzzvm63v8K8ip-39yWweBZz0iPQv2AhSu1ET7tPwLqPk2HyabiaM_Y5eMUFtoBLcnZRfRKwR3mHbBO3BebcqkPLHQYNqM3k7oE9HFMtriyW1IsHxVBmkX6Tu3lVNyeBYx7-e-c8CtP0klDc2maRAHTdePY9d40qAcqVWAIHLlCUDoNM0gUqj-CE44yybgCr9EinOh2SIvSbU8JjDd25WxqD_L1mqITfpsfxWo7azB8J_fC52XhqQPPMwwDFt0WNabnDcihIG64UcQwwOD52YS_Hd71g0T41BRe-OcYcIsYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027
؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22069" target="_blank">📅 21:47 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22068">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDmOcueBaaJhtLhdjD3Zfpe2ul3_7ymxWQpWDfaUKtvXq7zM9m-qdDBC0_rjbWQtrWEMRbmAd-3jZ4K1_P37vBwi-W0cCb-Ai0ULckvqqA4yKiY3VmXXq4MLvKba5DPTigEtOWjyfiy7bAfufWfnhYXTAH55yYY9FFGejSUyq627gircy3e4wQ8SMwlieJYJ3REER6QxpXujJq35wu7kwHXOjaDivIXrGrtr7wID0WN37hgI6-2ekhkD24J0xvvoY0snw7C_wceoT_BwNF-kezKmKdZkUa9lksmrdEXEoifLEsIO227LBUvS_F2fXszjjmoUVwSoaAP1GjJSiUQ-qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049Egyor0HbEfh7S1EM3_T-97MWOZpYwCXGM1xPCa0aqEyq9abJEy2BvqtpJJtawXSvERRMyb0zePtWLV9n-AgP-EUVwfQrb06PxcbdI71OpNWPrp_K0OTatpqMb3IT6smeM2SLXNTQaBEJ8u70Eop1Nqj5T6QJj0ZtAKxY3aQWgeCwZLtd4bpbJurn8UO4Ik6nj1PlfzhE1DOcwMx8Mo3vfN4ynSK3GUO70d1Gkt-oL5t0zIdh33onDVlactIEfW3a3pMYStFvkf_lScYJo-ocbWnRiQxS9UMoQUsyCUIqXVdabT2aV1ew3TWMkcp8kmLCijoxO_0tmuAgyGWU91HClEq0RO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049Egyor0HbEfh7S1EM3_T-97MWOZpYwCXGM1xPCa0aqEyq9abJEy2BvqtpJJtawXSvERRMyb0zePtWLV9n-AgP-EUVwfQrb06PxcbdI71OpNWPrp_K0OTatpqMb3IT6smeM2SLXNTQaBEJ8u70Eop1Nqj5T6QJj0ZtAKxY3aQWgeCwZLtd4bpbJurn8UO4Ik6nj1PlfzhE1DOcwMx8Mo3vfN4ynSK3GUO70d1Gkt-oL5t0zIdh33onDVlactIEfW3a3pMYStFvkf_lScYJo-ocbWnRiQxS9UMoQUsyCUIqXVdabT2aV1ew3TWMkcp8kmLCijoxO_0tmuAgyGWU91HClEq0RO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
از نبرد تماشایی روزهای گذشته فده والورده و شوامنی دو ستاره رئال مادرید رسما رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22066" target="_blank">📅 20:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22065">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sk8_ZefuLwoO2raYNY4weSQ7WYXcUdVvvmBv42TlcevDTRai8n6_SyRYLRa0U-NH5SCrNaENftPH7w6J0rBkvN5XvWR0ohllhvSooBTbBO13IMnmrq1mm-lT3GRsrhVWB6Yws2SwQ7ra9t3ZO28M0LmuaDgyvb-yQKFzHJ1wSHXrxeQGq_34iCrCm6FhtnUla4l4tSnBwLBVpqz-kr2b02QfDXNQQVoimCBKYnt-JvKOSnJ0oZNNCWs1zI2FybPUYvRjqGOBRJYQN8DEJlsbqSvetafRvXn36kF1S2QV0LElE504v8LTpeg8fR4FYvlnpF0DCzrBeMqQzoRtB-PZTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و سپاهان در سطح دوم رقابت‌های لیگ قهرمانان آسیا حضور پیدا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22065" target="_blank">📅 19:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22064">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOoXIKHVG_qepq9dxAq8fWGDdysmq6Tss08JlwlAb6ZDMOGywxBo9uMNpx0_1E4DGz6WRXjpjibbT8r7Wi0bLL1SlVQOPalnh4CxfqCwaTkoSX6NwN1VgR42Pka0y8JS7UJ5tsCMaeo0jjouZPQCxNeOgKHGvf3aWo3Z73-0YgOAqYcADeb-qEaeF3r-mdz7aMkUUzBQEi5wOma_-q2gKjiN0pZN4ZT81p52afCkSToQ0M_PuK7tALbeLCfyo2mTfiqjLkJojWbrw-CT0yJzkDRXUzG3XxJhpruwtkqvxy-zbGmrkoq3-cz-9DZc9aZXSE488CWJb6I-zGY_93ieqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozMp12WCBzH9bbo0RqKsEaK2ZViizW-EnuBqImZFhUts0FT8ug6YkrUc0AAam77I0kUPbx5Z2Y68hE-QV0h2DlqDf479KLbGFxzX5vsg5x791NgUqAgA0L9ctqjJ8ZEn_Rm__UNkWhWBRKP94esYiGfUaSION2fbQhH2rgvK0mmP_lZCFVNdLbzd2XBXCZSYi7f_W_ZAWftcw1hLa4xIamM6lGGyLe0BbcrMQ3ahrJLNkuLUsrDMPvN-p33-vWpA-p-I4K3Mz4mU2ER-XbXnNtCEvaM_wz-X6MhPy7Bcq-Vba4lABwIlXB5vE2c_FzmlciCP4QERMGFuJfmkggAs5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qo4zIEVkfxCPXQOyVtgX8q-hzglJihSzE9gx2x3U8dNzV_TgRqB5xcUUROwGpWK6B9Oa6E3Lr2ple6Nj3VjNjA0vpRxqSw7crvcy9jgn87VLIRXl758fZFkGPaQ9hsAUAGLes_6mty8DIgkHSLku8Eh6nVXNDuwl7nVYttD-aMjyQCTIRUPDCryi9j2F04pxboAVSsMVvDRVW5U7vJEBHngmIS8vcmLSEZFe0sLiXLQPZ2vmAGsH8SOSd8i_s4KdfljBLu9wWhTuqLl2FgVqF59VL-X_WgjjoqbWpH5w3AgATJ04EAE3LK0Cbgd9jF2yxCeeJU8j3Re5dKw8MHvA3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWgtNzSLkS5Wv_PZ_AENkfACgbAmRBoD__4K2fGeviOMNhWrqnJ5ch6_PyZoCgigblHBgQbq9iRcgN4NkFXee-yDLrBvlgieTHPDWsKrFFIpcgr0QERF0pn7OtygQfv4n3c13rq0OLyuzr1wGhoYSR84GUVP1pXdk2Bb9qdc5Hg0mciTuC79gZ4xboS7A6F6QMr6eLqlokjZvKKTs6sIzm1QoQeCkoghdsthvga17Sje0Zi9iS1s94w_TD9-brYIxtgH194EQAMa5uu9fh-KpA-FuEJVT1BDezjgb-digF97FqIqPay1N5z1FvDHDY-VCauBV8mKBkftzFWxum4Gaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOM8xBouQ3CFxF95tAIdeKz-UqZM-QbvZYn-sUAHPTaEvslcQ6JVLc_RvAmgkvsvLgU5RS2ToPT_vZlyipWIj1unYbrTUDZLdq_M22xhXW67dVzMBZ_k8-oQhwmAPRXawEXvllM2hdpnPUoF-Wlngt8nIcLvyl9eXTUf_F0FtRMhM3nI5xZ3XvSXmkXbl90FPpExnTUFmYDY1Ku45AWWYxVnMJX5vk690-aFpw20RJBFAvSeJfnUOn_Ws_u5lNd4oz9XAABVU-GI_GbhU1zLSyp7UHdAIaEMj2bcymHvdXin_sPGiOiEytJekOSwVglLOpG6KWGq1CgZMU1KzXqhpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برخلاف‌شایعات‌مطرح‌شده؛ مدیریت باشگاه پرسپولیس برنامه ای برای فروش اوستون اورونوف ستاره 25 ساله خود نداره و این بازی در جمع سرخ‌ پوشان ماندنیه. پیمان حدادی مدیرعامل سرخ قصد داره قرارداد اورونوف رو تا سال 2030 تمدید کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22059" target="_blank">📅 12:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qk1AwQnDRUZiNdk3KwZ0aM6dRtisITZiaSy9zjvtAXjfDqPztT-zpIdTjU_Gqj84RiqtKGveAbVZDBkWBhSMQAZiXKWbZxfFGND6wJ0aAbnfRiV9pCBX_JWtxR4ueNc7p5aPeq41SsRqsf89aXVjYoUImswlfRVsiFzI0qoXEDGXObv6KDNCztYhmK98dmDW5BztHgxS6EJShUuHgkCnJ3y2dDtY6MMe3TrK6_bXI39Ho7yntBLAZpZAo11kfy991IYAuy-S1DRTyjzyrSG5ETiMlCtmkYFjkKCKJkK_mmXA-z_yM_r5kV1bpRB0HGTKSVvwLl8kmVGXFm2k0JZ1Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBRfRj0WsGDYZzhvVMRgiEyYihEz_kC3uhzenUzZc_6TfepT2hmWQ8mvJsTnxGHmTaJ3l38JSXAkswE9FCB8Jyt_AGN1Wu9MuX4KKmArZW9lmUEpVzKNYD7GvCRisRKHZEggiOc1X_p2NAHkMobfGXEiuCiDKZbWIKwp9Gkfrxvqah19Aa1NvGbrYk1f-cBSIRConrggXxD1rQlSKzAfK81cWlAvCpXM3RbkHM3txQHOXhiZZp_lm-QGNpYLonPUi79j0AxAgicxGRMwIJB20rhn5sHppzl0Mn6Q8WDTaEXtY3VAVDAt_5B98l9cEMfqdxd5bTxeMyFbdXcHN1jtSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nBC3lwktK2GiDdVJ4Qmq-H8rfNHV9j4J6kKEDRisQl8TKt09Wj56cpYStQzC9psKFbqMYzFsteUpUejkows-Fl2kT0rys1MVPKkYoJY88LJNh9o2rVsql3oiCTCDkZq3prDVgmGuintPdBoeh146egMF2c2uJNVg2ar1OEDY3RdUBqx7n7uuUDdEiV9ZNsFbo9DtsJJIMQeyvjr9j_e6nCrWR-NMfGBvFpr3B0yf8569vrZFy130QVRjaxBXCEPr1Mg7aECjxCMjioDShep7egcotFAUZDUUKEdUyxElvGrrNCtfe6Z3E1EJwj2QeCnSDFXDZRLuG09j5-keyGFljA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cgDU_Z0C2O5g-TKB6UwPRbLAjloghMiIzh0D2maiT8vrWDzXZ_CQnDJO7RG7CjrGLdfXLpgVKvHVL7jRIWGfXu5p7kHlLfBedMwLCwf0D4sPa45FlxmCItmiAMF9xXJKXfs35v9ysIKzjJxx4LQlQU1ezGJKYU9vpJjX4lkCROm-Huuw3RHYrql-Sl0jXI2ze_Tg4cOWXe-3kmerNpqBlN9DcFC5XbPOYGQTcxcbUobFOFcbtv-m97KKXLu6sXI5hJ0QybE_xAM4sMq53H5b_80GFRC6Hn_35c80S2y04gBwbeuT2O4SSVddUvlY0ZNjmL-jJVwaBEZLjuVD-UObcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACSEDmEKKCnrEOqw2dgjJYijZgzIkC4uJ2gn65AAMVgJrfsyqWSiCGenPQa_ImJ5iJC-Bv0yCEBd7CO_2_DmwV-gzceNpkHJpdtpwMNo6kghv4yOQhqu4ybJKFFvw31NQdVUzAnnylgdo5OZ22zeCm9SodC7RwDl67Wy0Vo3tN7sZRp7PoymJ2N8EQzH2csVlQr2jdhEYrPa3GBiMlA0I54S3kd0xgvxEjZjJZ7kVNYHN-vP7ls_1mf4h8Nkh5W5zMeHJlIKglLEfoeGDKluMsKRB1cJ5bB3z9qxSpdI1hX9i9VHt6eFzgk2joNijVxxSNRtY59vLiBQ13Vipemuiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
دو گل دیدنی احسان محروقی در بازی امروز فولاد و شمس آذر؛ گل دوم روی پاس رامین رضاییان بود. حمیدمطهری درنیم‌فصل دوم و بعد از جانشینی یحیی گلمحمدی در فولاد نتایج قابل قبولی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22054" target="_blank">📅 15:33 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22053">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57250d4705.mp4?token=E6PSNsLB--_0BNzpKyciqT29K40nx1n8cP-PJlTMYcdZiqmcN4g0jVlLXwWHEqqqg9F4GSlVeiYb6267_CaGdQ7ADX3BAm56ErrBm9AhUxjAHUduz6HNZFi2S0qfUH6mzuT2FaBKIWmJucq9OwNCjsv9NgUsdJvz9TTFY1E0Dw3UiujtyN3vj8mh4opoTbrlowF4JKS2tpSLP5j3B7so5rrZtM-VP16kFbrwBHrAxFTxx6Hu3YTRsvLt6wZ90TlHxUTsMJ_Cq_TCB2jd6SFg2d9liJXh12vouTVP7mgunlUMXQbUP_9my1dhfSdjIyyFIngYUIycDtgwk5WMdvdgcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57250d4705.mp4?token=E6PSNsLB--_0BNzpKyciqT29K40nx1n8cP-PJlTMYcdZiqmcN4g0jVlLXwWHEqqqg9F4GSlVeiYb6267_CaGdQ7ADX3BAm56ErrBm9AhUxjAHUduz6HNZFi2S0qfUH6mzuT2FaBKIWmJucq9OwNCjsv9NgUsdJvz9TTFY1E0Dw3UiujtyN3vj8mh4opoTbrlowF4JKS2tpSLP5j3B7so5rrZtM-VP16kFbrwBHrAxFTxx6Hu3YTRsvLt6wZ90TlHxUTsMJ_Cq_TCB2jd6SFg2d9liJXh12vouTVP7mgunlUMXQbUP_9my1dhfSdjIyyFIngYUIycDtgwk5WMdvdgcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ رشید مظاهری عزیز بامداد امروز با یورش نیرو های حکومتی‌جمهوری‌اسلامی به منزلش ربوده شده و به مکان نا معلومی منتقل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22053" target="_blank">📅 15:16 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPhT7nTLuApBH92sxYelIK1NMw1pItLEjzrXLr2SvBeysCUKMhtiPmgVwMR1-q1W_4p_SMfXh7Tz8LVKzxVX9VLAQAF0rZt0k6mH47Dx6szq1XcKZM0Sgf3thxJWH_-BmEiKye-rANfyuyTdLZP7GarZwTuIObRdOZzk4Uja3ugWROnxnHKmQdIXnqDx0H1Lc9xuePTBxZTqjjN002oHALicP8LSi_tWXwq4jNKuGzzwF5S1mJILs0N8W1oo_ARLpIc5rPoVpc2WB5s6LTEAmnjYVK2OI9ZoGdUE2qMPKo7trn7RfKIhULiQzvAsNGRvyoJKYYex_USnRhDu2uhMsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ترامپ در واکنش به قیمت 1120 دلاری بلیت بازی اول آمریکا درجام‌جهانی: من هم قیمتش رو تازه فهمیدم. قطعا دوست دارم اونجا باشم اما راستش رو بخواید حاضر نیستم همچین مبلغی پرداخت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22052" target="_blank">📅 13:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22051">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LB-of_GdW8FyrPNhTrNBN9XGRLrwCpjBosFFTCERmAVUrvHdJ1Skb5rOiJDw8wgt51u697COjnK_krpj0TSc6fSQcXK-D45oQDaVgSchECwmL41z_GMSRFdAO8Ju2fUr9kyjz-NS8KDXsNTDA2hQ_GrB9MSAQDlVxVZGWK6chXeWGZ9i37Gj9f8gPtCMuwhHuhR2n8qeWSYwCwvAtBEufrVUeEC1g6IStpsHHawNF9aCCkSaTPML7UAU3TOeT0fFuyMYB9enpWJ4LjFClQZhqdp2DHcGI0h9fSQDeKYyYqiTT7WVJGuzrfQd0GjNyQh4MVrMT70_XJme5Y_qJy6Lnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22051" target="_blank">📅 12:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22050">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_4nANjREtpTjWjvapB3-ZLDnlKEMIOZDopjnc666Qkk9NBJH9ZjVVvH7o9KD-XwoXcSp8sSO5DZiydlhRlECsalwzDDU8DjcZrGH1kZePycuSfygdmMvKkRt5MiuvC4_LC0qicXcG3nsAX9MKk2wMjGKYzyZ-Ye7DRoPRGq3avpuk0VmMch9bo7WIsbLL7iX-3fAkl7y-wbtPLzTO8r-2f1E0ki7fHSdltTQjHS4_FBDVNbeTd9t9USlvKwKrfHFs_LNlfiXpy74h-c6oGpvO2QjNmEoqp-etmlkGDEskm-uPuLdszrc6F9d9Zt4ODJhgX6fvgH9AlKJJ1lX0aE8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛
رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22050" target="_blank">📅 12:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22049">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XK6X4TTTC7YOL5v-RO1-kqtMoCF99sSTnnrFMc2xEauLmlAm687-Svf6tCpdFPHBncvX1eLrP7hErh56N-5XRumPhs5iazk2T7PBRXtD37R78JWVKvwlDA4T2JH0fHTbnuMQ39kqjtu21N08Y27zh2-jI6y2TuuLkFaE5-xz3caMj7-W2WivaCWfKBNGGB2h8x-k3G3riEon6i-jq64t6vJM4io82Xlz2FTCJIIuZmCSsxMMWIB8SJOSYTAy7NUS5cEzwIihGveb29Xs3kunYa_MQxHYObw1g-3DxQ9YAz8Ne1ZP7aGtqq5zRWp-6ak0H6a4p1o8NVxVk4ptu0yCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22049" target="_blank">📅 11:52 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
