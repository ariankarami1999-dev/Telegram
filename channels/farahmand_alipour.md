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
<img src="https://cdn4.telesco.pe/file/ufNmzAP2iep-muw_aoxfd_bSq4Ncpm19PuWDc1-pmLR_KKG2pUY4N7hFrvyR9_Sy8QvhZKIeNxnmTjKGfFdg6NofbTp2C_6R8YWOD1frB2pYa95NZnl8HmlVv48JU6ZXDr3zbRYeNdT4b6vo_eI_7oPuQAo85mCCjgL3QFe844su5uFKaZ-ZoMLVmoAwo99QRK6bS6r5EMDn6-fhBFEaU_sXEjFP2FZD8vA_RJ7kkCtWnJvo6Uzpv3Lv_CMbPYfaH7uB6cNPfOxDCDTCdd53VVkHYTlFrXgh37aNlDaL_GkZzxezuzjIQ4hLPiwbPG3piM6jDsoTUSvNB2oer7QePQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 02:01:51</div>
<hr>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=HIpZkecyjlswLl1I9n6eWU_PXqTPdGcQs9nzWDgl1h7A9sUm2Am5UbcsAQlmOVtpMuYglGXmzotofbFzjhrQ68smFjoidsI7YQfM_IN3ZX381HMShOPf0TsCq7zVWVgfYUxXpL0qzXdI05p8UYzR0GOlpWiQjHlCXaYxl2p9e5UxF1Yjnq9-vLgT5BeOabKvPXYnvrNJ2Y1I6pVvuGjzRXRa-23TzMwq_3ogbogmy5hNTD5tHUdjFq20fMygOhXlMZ_YeBmC3-vOxYNGMdOVR7p4lZfX7zGrkE67vBLoilq9YQiOGZqDPMkUPutL7xQhJqqwPtUNVCbU7ao7eOXkMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=HIpZkecyjlswLl1I9n6eWU_PXqTPdGcQs9nzWDgl1h7A9sUm2Am5UbcsAQlmOVtpMuYglGXmzotofbFzjhrQ68smFjoidsI7YQfM_IN3ZX381HMShOPf0TsCq7zVWVgfYUxXpL0qzXdI05p8UYzR0GOlpWiQjHlCXaYxl2p9e5UxF1Yjnq9-vLgT5BeOabKvPXYnvrNJ2Y1I6pVvuGjzRXRa-23TzMwq_3ogbogmy5hNTD5tHUdjFq20fMygOhXlMZ_YeBmC3-vOxYNGMdOVR7p4lZfX7zGrkE67vBLoilq9YQiOGZqDPMkUPutL7xQhJqqwPtUNVCbU7ao7eOXkMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=O1_p8wpk8d825BO6UCX2hCigJwul7281ltIAiQ1uDwGAIH0XCPjDlBQg6Hd4wIS3t517sau9z67MIRpC1Y1CxIarSFx3_Un9d9dQCmfaCrQ8jNsLst5CbON3XShKXnARFqypRPj0SnYRrLtjAkHtykZKjZv9MsZKHqjLs-8y_s19fL5-UOMKVBBuRPWXh0MkvtQr8zpm_XARRKsXhGPBv7qb6Ti3die8xGcPQ8A26vk5TRdmLchOg8ua5VB8l7VVes2iN62mjZEj4h4b1QtTHviaOb-EZnveZ_Eb3YXnYECi_7-cAeUVKRWQ--C9atAyJBQVudsgwqOYLpxK76RDEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=O1_p8wpk8d825BO6UCX2hCigJwul7281ltIAiQ1uDwGAIH0XCPjDlBQg6Hd4wIS3t517sau9z67MIRpC1Y1CxIarSFx3_Un9d9dQCmfaCrQ8jNsLst5CbON3XShKXnARFqypRPj0SnYRrLtjAkHtykZKjZv9MsZKHqjLs-8y_s19fL5-UOMKVBBuRPWXh0MkvtQr8zpm_XARRKsXhGPBv7qb6Ti3die8xGcPQ8A26vk5TRdmLchOg8ua5VB8l7VVes2iN62mjZEj4h4b1QtTHviaOb-EZnveZ_Eb3YXnYECi_7-cAeUVKRWQ--C9atAyJBQVudsgwqOYLpxK76RDEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnGh-YpDmfRCMmLPD7nb1dh1lmMEVB5QuLZEgSJGrQQxBi5s5hl4xfdIdG0Wbqq6SBC8cpK5kept9hHdecChdzfw1cIjcMqp4iHcAa1iXEyYb3ufTOOV-dabNlsfRZiqTTk7C5khsUe437CQnGn5UQk3q_o9t7FhkSfCm32pCmNn65pU8T0kcjAnSmF__MoP-LcomWUptwsS29r4qm4JVY_ZakK5Az3JZejHwDtHEdmnnBwusp4zoYwyoW3Flc6ivm2ptj6P5KEDNMh1keqx7Mkrvw58AYBYHmw-POI4xqUmf2MwKjFSTuhlIenatfsshTVXnfsLq3oyKyr2qqNTXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=AzjG_SL-HbH74xDsW-qMmq7T60FPjARxVa4osEK2rGiB9aQfABXr1mb03jyySs91xAviC1O9v65bRh1T_qngIv-jnL7tYZxfXUILP0H9FWKEp629EfRzIqE9vwYfc1JWMsB2sDNPuAIB_944JP41PtByW578JoyGnA1XtQMABsPzbQLds0GpOReKt_WPc_nvDV5ilb1dF6gmW-ZmXrHrnHGG6JDSRjs9X2Vw9jNEFxn1YSCkfLz0xUf1qUsKk61DlbRrPsGFLftd8MNjcP2CDM-ZHo67Kp9U4h4e2CqV-ynzuWO08poHTETPB3WgSI5tOrY7tcLAPtTHpExHXVKZ_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=AzjG_SL-HbH74xDsW-qMmq7T60FPjARxVa4osEK2rGiB9aQfABXr1mb03jyySs91xAviC1O9v65bRh1T_qngIv-jnL7tYZxfXUILP0H9FWKEp629EfRzIqE9vwYfc1JWMsB2sDNPuAIB_944JP41PtByW578JoyGnA1XtQMABsPzbQLds0GpOReKt_WPc_nvDV5ilb1dF6gmW-ZmXrHrnHGG6JDSRjs9X2Vw9jNEFxn1YSCkfLz0xUf1qUsKk61DlbRrPsGFLftd8MNjcP2CDM-ZHo67Kp9U4h4e2CqV-ynzuWO08poHTETPB3WgSI5tOrY7tcLAPtTHpExHXVKZ_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixqchdPXuTArqJNK3_zh6Ggm8Uw7xNqNx2VZw8zNTGe92I6YSy3bEHIFx-_R3R9yQQA1qegQkVLqX4xK2Y7MVdomnmpl86sF2VwHGWkSeDBNj7H0OhLY9buN6cy7WzfXABDrgucQEJMKl4pcEy_T7Dktbggnuij9YeHIO7YMp820ZjYhbxU611SsaK_MZ8G5b8pj_jmiQCPp4RMpJ8ke7-eUDjExQqKPInuHg016NU8m1IkGxS3rNPNX4xgCDuPYaz9hcilT01oAl9U0feLT5qf6TbPTxaeibtufs-LO_SvKycYiiwxx21kuVsbt1cOxTM_vc1iFU0gM_PvGqFDWyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.  جلوی دوربین‌ها وارد هواپیما شد،  اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!  نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6550" target="_blank">📅 10:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZAS8hiAKSGNNmaPjwtV4BX1NqmK0gUECxTQvx5GAbab0ba-_Nt7Ufd9yObbS-jtjxGzu_y3EwAPv6FBktiMDXmehG6CHX7kqvovYHiiWm3bagvOyNzLZv1-is-WPZ9oYMdH9i9rNqDdXHK87b2Hjtqd1KRXvfYYoCxuldSpLuxNNSrL69vcw-7jGm0Mr1RjT0VLOkJ-9Z5zXUAqTdZ3WWZMB87NvTmsu_1PacY_4zw2Gd1kg59cPSXWmXFRDdroCblVmavW1IvF5CjxSnhEynADxIMUiykOD5LtsIqahcFsNEpmjrFgwD5HuyJGAF98sdwVG54amM2okCx_nb6uHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لکه نفتی به جنگل حرا رسیده
و حیات درختان این جنگل به خطر افتاده.
اما این لکه نفتی که تهدیدی برای سواحل قشم شده از کجا اومده؟
جمهوری اسلامی ۱۲ مرداد (۳ آگوست)
به یک کشتی باربر (و نه نفتکش) حمله موشکی یا پهپادی انجام داد. کشتی داشت از آب‌های ساحلی عمان عبور می‌کرد.
پرتابه به موتورخانه کشتی «مینوان پایونیر» اصابت کرد و نشت نفت رخ داد. این لکه نفتی رو موج‌ها آوردند به ساحل ایران.
سخنگوی وزارت خارجه ج‌ا (بقایی) هم تایید کرد
که این لکه نفتی ناشی از یک کشتی‌فله‌بر است،
گرچه نگفت هنر دست خودشونه که برای بستن تنگه هرکز به کشتی‌هایی که در سواحل عمان حرکت میکنن، حمله می‌کنن.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6549" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9HOcmPk6OFctAPQYmho7HSwrAlyRgeuIStHhDJ4BIbpFsSWgN-5jfggVpBB6gMowdulFuMUCGWF7nYj5jIELAFxCkJ_tDPZuePJrmVXCKUgxeWeF4O2CAqoFO0FJI-UUSnGofAly2F6ow_88ABsBQc7KeFaa7LBmIOv4eWwgBdFh4nxwurj0gLsZ-C5I0tWYqcx2u85wxixFBO3CH3jD-lJoSAKLHjy723bxn8DKrhtvaLrfyP56XcPFXo9zgMKBmxV-0z8iFFZ015VWbPQK6i6K1oPYgzhSX-bR7hipuum35g_-6xudQrWOFLRDeLKalUnck1lCCZu1CflCaolxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بنزین در کرمان ۸۷ هزار و ۲۰۰ تومان!
میخوان آروم آروم و استان به استان
قیمت بنزین رو گرون کنن که بتونن
با تفرقه انداختن بین مردم جلوی اعتراضات رو بگیرن و قیمت بنزین
رو
۱۵۴۰٪
افزایش بدن!!!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6548" target="_blank">📅 21:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WU_WkNruyvGgmMTtTtqNlKd1cclAxuFdzc9OJ-rmh5qyny1hi5mdcgdtyYZbp5z6JVaM6mNRBhmSiJEPdOiefcHewWAF0UEM4JMOclZijA5Vv-j7oSBd78J-YYA9SA05lPi9ySaAhZk0BWbEa8mVi9ogBCba1Tv5FFKXCAOgyD4ZM7OBOdCD_pAKcqkec5X9S-lbUc0nllJySqzuCmlJyTsRQdazCZ2yDDm3J3Q0YQi-vCpJuJiQDkNOPeE7Ljjo_zi5-5IuTdLL7UH1MN-hryOkXVg0wsWUsBDbLMtrm4N_gY2bgowKGZCJxDcpICRPL9kt_Rvr5EeaQ4DSm_oMfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=G7QPXRrh9eiLnUBTykZQxAZGs8NgOrYEBLiEQVtlqekGe_09M2iBuB2i4sycYkJHZkYbKeI25OmOOEIuKuB9EnkIlr6Mh3RTgBObIDEouS-4jpDc5emqxhtVT8KKzGjuPAI4mU45naqfcCLApna_8t6OjEHGkB7Eq-3lx6P9hE5vbkzWjPW5szpcCbMe87fQil7cjU6rJ_kc0lCUbujYuqyr24qxrQuJdKLvCLog7XCi228HN6T4Coe4X693VTlFFwGrxR2YnP7d0oHIxBoUgf9urAt2WUekCeNgYv9Zc364l3fuHvQr6kOzwYKBAmooDknO-iLuWbsGSH1R5x6OLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=G7QPXRrh9eiLnUBTykZQxAZGs8NgOrYEBLiEQVtlqekGe_09M2iBuB2i4sycYkJHZkYbKeI25OmOOEIuKuB9EnkIlr6Mh3RTgBObIDEouS-4jpDc5emqxhtVT8KKzGjuPAI4mU45naqfcCLApna_8t6OjEHGkB7Eq-3lx6P9hE5vbkzWjPW5szpcCbMe87fQil7cjU6rJ_kc0lCUbujYuqyr24qxrQuJdKLvCLog7XCi228HN6T4Coe4X693VTlFFwGrxR2YnP7d0oHIxBoUgf9urAt2WUekCeNgYv9Zc364l3fuHvQr6kOzwYKBAmooDknO-iLuWbsGSH1R5x6OLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی میگه :
۱- موشک مستقیم خورد به خونه مجتبی
۲- مجتبی خودش هدف بوده
۳- زنش کشته شده!
اگه مجتبی هدف بوده و موشک خورده
به خونه، قطعا همون لحظه مجتبی کشته شده!
اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید
که دست اسرائیل (دست خدا) عیان شد
و خامنه‌ای جوان شد، ولی از قرار معلوم میخوان آروم آروم بگن که دست خدا، هر دو رو از زمین برداشت.
موشک خورده به خونه و زخمی شده  باشه :))</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6546" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJ06s1SQkPB1-tsRP_tyH_dtMhgEmV2HPdjWy-XoNmgkjmZOViw-ebc9r5g6b76x0VVJw0yfWsJ2PWWB_HbBs83Vs5n2XCSlxQ6-o0_uG8_k6wUPR7fkFy91sAj5O2utpoB-egDHzO6eOHd-821s3ywkh3A8nOXHWUIaF7xl6ekMrQ4N-HQXswxn1ySkvk9JM_-aHhMzTca4CuGr7st6GTsuqKFcEWbHTxCeSe9GCqIX0fal_DGw1e1_t2w2F7K2Jmzms9eu_0P52l7-30GPG-9QkHsFRpHgaMfkFXxFui0fY1hQ1CZYgaEJby-Ms_f_7s2zvfuxJGaaAJMVInVILg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=qzSVY4n7jy51CsQaPhz5tRial4qA4whUEfak9ARLcV_Mxpy8xGKOdHfxo-jFtkU6jSa-xRt82aof7H-mT-iV7Jo6Ta7ORdCI6XfDMbi7SPNVKlX_k8SS2gvUrEcDRM7p3v0sLQSF7H-MK9KIYAmrjs_Whpl9veC9R99cEzHeh27YmLEmnrMPpdCNGmvhjwIII_ulsdsyYsz_Q4A67NeadFxfsRbFxS3PbVPrXcAfCwnBpIEyGmRZUc2SBksGe6aUjCehw68H_NEiajLClEcU73lHKOGiICYaVEdfjgHwzmGZRasKiysBOohKZLWA06PQhwvK95f1vO-7ClK1O41Nug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=qzSVY4n7jy51CsQaPhz5tRial4qA4whUEfak9ARLcV_Mxpy8xGKOdHfxo-jFtkU6jSa-xRt82aof7H-mT-iV7Jo6Ta7ORdCI6XfDMbi7SPNVKlX_k8SS2gvUrEcDRM7p3v0sLQSF7H-MK9KIYAmrjs_Whpl9veC9R99cEzHeh27YmLEmnrMPpdCNGmvhjwIII_ulsdsyYsz_Q4A67NeadFxfsRbFxS3PbVPrXcAfCwnBpIEyGmRZUc2SBksGe6aUjCehw68H_NEiajLClEcU73lHKOGiICYaVEdfjgHwzmGZRasKiysBOohKZLWA06PQhwvK95f1vO-7ClK1O41Nug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.
جلوی دوربین‌ها وارد هواپیما شد،
اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!
نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31726f423.mp4?token=V26NixDAOVmB2YYwEcDO1w_n1gYAIisHBddZ53fTtq4te66bArhtJQmakzKRiMWDcHxT4vHKxuwlWJyoNhi7eSdjdhOlH-9U6aKlMdmkIFuI1O7WUzG4qySru-TNrQt_JqqM_QovwrgMr58dJUhIdMocvWBRCTFC08an3mnlNIxls6yaxnHoqiN4fzAsk6Uyfxlh9Mytcsj0NbegaAf3K3xHQpUpY9uGRdOmZEsBMwzq08hmNSANfxIHnvv8K6TGatC44lBE_SSgksJGyrJoc7Z3ShfJHHc5ziM9a4--WOK-gH6y-MMvprl82G3Ln22IK59dzs6Xe6bLCcAn5xruIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31726f423.mp4?token=V26NixDAOVmB2YYwEcDO1w_n1gYAIisHBddZ53fTtq4te66bArhtJQmakzKRiMWDcHxT4vHKxuwlWJyoNhi7eSdjdhOlH-9U6aKlMdmkIFuI1O7WUzG4qySru-TNrQt_JqqM_QovwrgMr58dJUhIdMocvWBRCTFC08an3mnlNIxls6yaxnHoqiN4fzAsk6Uyfxlh9Mytcsj0NbegaAf3K3xHQpUpY9uGRdOmZEsBMwzq08hmNSANfxIHnvv8K6TGatC44lBE_SSgksJGyrJoc7Z3ShfJHHc5ziM9a4--WOK-gH6y-MMvprl82G3Ln22IK59dzs6Xe6bLCcAn5xruIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون (نیروی شبه نظامی تحت کنترل سپاه ) در تجمع افغانستانی‌ها در ایران ؛
هر کسی گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRjidTA_v9s5xjP94-n_x6-Tc6kIgidm7LBIRfA7yBYRqF2Bst1L8pReFWSHxwRieI1C01cdr2BjjUllAxv8g7ogFDiB0RBYxdgmwKQjxxtCT42ca3sCjSJ5Rqir1bvsEANzJ-ORqw8bUS1BKP1hlx3KvFpL7x6smiyQkDKI9ZPqhmjuEkbziGHX_BsnHSlZDcr1cES-bcOtbGo8Dgt89lZfsPU9N1zxb0lzAJZdYmzai1SqMAknW0KPdUjh-jaBVIXwrwW0pP8wUOsbnkoE-iFl6lK91jmq--6UsPFnjJK7e9lOrapCxBmEGUSOYaqUugEmigEOOGKJGa2685nxwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUY79ff4aWM2Aaeqq0--7XdvhsR52pZwczGoBrOeWZlyM2etfliXxkxTm0Uv8sy0OSeqRWlr9JL-XuunGaK5cQ2UG5CFS6KE6pDf1SCOXpfDZT8LNfAJ87BPCURaNNHib3kBdaNtsA7eDwkroYNH6TBT45Col4ZXK6zcz0HhPk1aAlVcSPR4VYsRbYMcoXizhMjsS9c21_ceeqk5cWXf1EHvBbXZSFUHUCrJXSGTd6M5RmTQXOAKc5fUUCe8NHgojaMIVdkT_wr7KqPr4vEIIlzXZh259_FpaGHAyPXtm-IS5Ntn60tllxT31TqDomwAkvMAS8mUCZgalfm_EWxzPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQ2T3reqIs-wekxGqFJtaiGdYmImDNMfQ_OOTDirBwQmkirbqdclitmQiGVKEwvtCY5VpLd3SuQsFp8j-60NY4LXJcH81hZb2UJc7RZDrQSr5XzhvYaVsOhZSHtlXDyYCl1PoQYn88-GwGTq7nprbP8Vv4iK6F0zCI0EcsVs7MgUb0Le2BImEZ2B9RLs7zOd2gaO4HNRN2Q6Py-IB35j1EtAeezgMe5t1dyKrEkSNV-6MTYYsym-Fa1PZRDr6XLFw-E3KlSR7zZRIXG0hGyUWIP8cq-IzDZiHkcmOBdHDWWs-1Nfg4sEnmAdKdMAZmGkrKA4TeEn0xalSVRgcjdNcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=qkPCZhekZh_EM5nlr5dqAT9_XE6kt7PhiLOxSt7Hw5I_L3DARMA6ZSrxUKQDs1Q5-DIH2e_b5SSaGzuJTWvX6z-WH8wHokOZvA9W5EJoZlpw-SzUCyAn0BWuwE82xh12sBoCjSQdwunkjVwvLxlc1dE16MKc5qvgg7UMHi3f4doB70Tr8jeUlMlIr9fdcgqii_BKvl-lgHXi79zg6a671B1oDoQUeBDBwaGNL6eSJnqTXyfSvTD5voyhax_O1t6mEU4WW9X4_P8mL9JhuaA_44rwYRGZFkphFtiwpkBtAILqufCM8YS07jx_Dsuu_peVQO7ZtyQYCr1TDSmia2vpRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=qkPCZhekZh_EM5nlr5dqAT9_XE6kt7PhiLOxSt7Hw5I_L3DARMA6ZSrxUKQDs1Q5-DIH2e_b5SSaGzuJTWvX6z-WH8wHokOZvA9W5EJoZlpw-SzUCyAn0BWuwE82xh12sBoCjSQdwunkjVwvLxlc1dE16MKc5qvgg7UMHi3f4doB70Tr8jeUlMlIr9fdcgqii_BKvl-lgHXi79zg6a671B1oDoQUeBDBwaGNL6eSJnqTXyfSvTD5voyhax_O1t6mEU4WW9X4_P8mL9JhuaA_44rwYRGZFkphFtiwpkBtAILqufCM8YS07jx_Dsuu_peVQO7ZtyQYCr1TDSmia2vpRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل کوثری :
‏سردار کوثری: شمخانی برای جلسه فرماندهان در بیت بسیار اصرار کرد
‏سردار رادان جلسه را نیامد و سردار پاکپور هم نمی‌خواست جلسه را بیاید اما دستور شمخانی برای حضور بود؛
‏وزیر دفاع با معاونینش در جلسه حاضر شد؛</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=ZROUCVo-7NGQrXh-d4A_xwu33-Ap66B8zvm3RQFdDTE5c1sZYV4r3Hd0ET9pm_l3JusadyCc3ZikIMe1PJqv2SHJ7bZNBd-bH7b4HoyPGA_Iw2kqjJeuoQrpsRq6h6ugH5ZxYqx89PJyCTQUijYY5gz-CBi0FyoEcTQT7okZD0uy_9pIvX9IPEv-6AhaPHwuuyFxXwRAYaOe-gSPiYqPkvoK2RFMHBJkmF9AnMheIBgEj9mB2Q8qtwqZfXMNlBVQwY0k7U6ZH7BrxZK1e1DJzCPo6NgIWOzxenTOYRudeE3ZqJ030y0nplkQlfIlgdcJ-Ya4b2aZYWIzttiTU2G2jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=ZROUCVo-7NGQrXh-d4A_xwu33-Ap66B8zvm3RQFdDTE5c1sZYV4r3Hd0ET9pm_l3JusadyCc3ZikIMe1PJqv2SHJ7bZNBd-bH7b4HoyPGA_Iw2kqjJeuoQrpsRq6h6ugH5ZxYqx89PJyCTQUijYY5gz-CBi0FyoEcTQT7okZD0uy_9pIvX9IPEv-6AhaPHwuuyFxXwRAYaOe-gSPiYqPkvoK2RFMHBJkmF9AnMheIBgEj9mB2Q8qtwqZfXMNlBVQwY0k7U6ZH7BrxZK1e1DJzCPo6NgIWOzxenTOYRudeE3ZqJ030y0nplkQlfIlgdcJ-Ya4b2aZYWIzttiTU2G2jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frEhci4jemGUO6SsiNPRiVC85Oq1mtSAwY9EZBJfOxSLJPI3l4nvzvgKJy7RDCTB7pa3lTiwjJhPVpYGxngZRuhZXDlHz0EWiMVnUbXyZuJ_wFWOe7ELm_fSv1ZA5IFWd7WzZMdc1Cgk-XM84gQAYa5OgjsCZjPSik7x3osXG7aCRcIt6DFV4pK56TMRI5-xAN8p34Nr1NheiyZoJe63agKoh9Tc0z0-cCOo9glDVz9M3tCC9-SNrwziVRZrGkbBkBP7KvVDh5Q0faqboRQ6RrbBZsIuBEQUs6EBjz7jqAEBaZclYDf3OpCRwynV_T_iFFvbbtpDZAq9ZcM_jmrBSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfpxoUjwRd94KF-XTeCEUiB9naQpiFg6NlVj_RAFO6B4TZ2M8uYg803F5__rI68q2ltXDES3hPEpfDDuWF2YhsjqSepOeMroy4R5DZi7hSlOTEXPBqSqNoYd11UXwSOXBWjlnw23jS-uE2hMM1X763AvTiLC2JdMOPs3UNnhPn9TDF0gfp-5d4z-UHYMCfXhXBbl65oaBZa32lrBSgSrdTvwTzwfk7mItxCbQZd-zR_prSl5ATDqHt2HwTgh5ajnirGINmpj_uXkp0d6Y9ZgjnGJPNG4PLi30QbvBdVVKI3BhH1Z7dD8RYUtGnDanPl9LvISdoVrb3_ZXtD6wK6b0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRngRX7MZJN1qCvh7x84_SKD2RIjmo2btc3dm-c3Slp3xNxm33tUV01mjoIUF5iweZzU8GFO01jEqiXXgoD0hijuvgms6ytn2-gRYM7dqwMgV4VjSBb5xnTivTgOy9rTaOhWthZmL1kVIJINc_RILjzXyktZjWgptqZpKkDKMpKnCnwSGq1kvQEMg02Cl7rIrYBT0ebKYqR4jpXyWNmiQE2QnQb3fhObxb9x69RO1lnG0Q1dyZ8jww1RJSShCEqlcDqKO5mQX2owCoL_kbxk-SD61LHfWTsdqwYHVqgkwLD4MAHrOXisj2FQqt-pTZqE-JAOlIpGdlT7X-N-tqA95A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnlMIVSZ0JElfK3oR2xdppR2HCyPDvQuqMGasdBOGDwAKcZ3lvyT_IEZhf4XRvJB32EhbY9_VeALH0Lu6wnOm5ykk5PEA11klYOjHRN2OS8M8P9fJudjnIyW-0ZquDzwbml8nYKHyRCx3tfUzG-gB-NxCTF3TsVyp1UweM7_8lxlxce5iUfdUoP61hHME5YxBgzT6D_6FVdh1Xa50VwtcJGKl6T1J2ZZ-7WTRm2x7RLzGhKgVYmYNjQSc6d-kuGeiUzMvIj4z9GqnPuDYepSTwa3JYb51Xg4-5h1XYIt5hLSpiS4cSZMxm92RE6c4u8qPVamceaM2yLAQPzr27VROA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJrWNiE6kpRbXyHosNbbnLUIuMBMgpCmjvcQLldh-xKpHRY8h307AO9h4WO2Msl8pOq3I2IXZsdZXJyNyvcP8a8w058Q6ngEtyiDGJbqm-lXPXEr9zyuhR4s2fQxB2YylylFv12Jy27UCErxnD1CPdy3bSrOgmh7kErf6igaUOV72Izq_wUOHkgBlM8ymPsR9O6aZI9MoQSv7wIpM251XGwnbGn70xuylDsTccncYJfJhbJQaWizuQ3Shw2noTJ0BhcS93WpyE4zOu5rgdZHG_gqMO6UFzyVGmgoN5hTKmfCtDtCmbZq5DaMrAYPKxWMIm9sr1Y4hCkVwVrDqAvQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vf8Z_L3HnSdPaVrLN_-pjuCZ7eW4h9xs1hSfzjcqXN2ly-aJT0QlERLL7fggbMZ0DrP19xwfyTcU6emBEzFhOyYk8NPfnOckNYaSXWAKVDaWNQ8SGWRDISDp6CkPBxDx2FHn9528ujLUQMlNPwLvyTRROcr2a9PBafK98xd1uVwyxMpLEZrS47iDCmMKZKCW_nPs78TBTUPD8SQDr0APbxngN25SR7ISCScv8vzjX-QofCnF5NrpODhkzt9le-kLVmBcA_J4_S4i456F2N85WJaLxhPZcEPFNFgdLEWL0N-SgEHSZk-fMc5fF7SJ7XNtxC-Pbn9XUp41rMUj6yUFmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tqJN0IHNemY9S7xV76LHud72iI-RV8nIpDjOsi416aEagfDZ6hIcyo-fU_wKk16l0V3zhPUk38ejHi7PU78IXiVm-NZHm_uaNWGxLtW5htDRo1POA4hN2lPo3vpgcp9jgpSNs7HZjq0tT-nEGEyFQcELxm16QkKiTeGYFsBl4yvPXeuEvrQja7fUB95vKrXBd8CzMy2Rc8-XzRLsw4mPj2RXus43RV5yrRO7i6LieCvkuWpx6bYcUjlyNEo9d75QW5E3L79Oj1tHPyOTyfiK-kWzUY3Ifvm4eIz05wwiSjptu5eD1XR_efKrc0OxlGAyLzSHsywtIj7WRlciUl4Xqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SkdBkYT2AefOAn5EMA0VDkJA7m4ziwvhIx1f1EmS49TPtzDNLsQVG4UZLd3fNgwuhzfWMuUKJUNzN6i4qLuISP3Zsrx02MWWx9m8rFs3tfyYtIKXN8Lf3erhslpyjugi0-PWdMhf3MmenDXoytXyo_FPkh_AD6E-7SpJAreDQxPrsBR9W2aDX6kx6YRJzvjmuwBOKQBGEX0fgjJRYql0t36sd194csBhvOiSpUwzOHfw2rXnDhl9jEVux6m_vRfojlJN5oqmNRyk5oyeeAH5lLcAfbLi9N1uRlfGtnpJoyoTdlsOgiHgRwQWg5fR5olyLmV98Gy36gZ42gwjwhirXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیرین مدرسه ساز در ایران،  ۶۲٪ از مسئولیت ساخت و ساز مدرسه  رو به عهده گرفتند. حدود هزار مدرسه.  فرض بگیریم همه اینها مدارس ۶ کلاسه هستند (برخی ها فقط ۲ کلاسه هستند)  اگه هر مدرسه ۶ کلاسه حدود ۱۲ میلیارد تومن هزینه داشته باشه، هزار تا از این مدرسه‌ها میشه…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6524" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_dLzMFx8P-qI7IBN8KuNiDRuoA95WciGDHV8Nezc7I9KLHjvQC0Se0Ahsk9YYdKd5QuZp498ngZzRD5gSPAMrfsjKHyDv8nOOr5x8oa59GyEaj1YE19gJOgiG4nJZrxXuB9Dmq4_8YSZUJScX4F5fzZsWYGdFFGC8RYQ9VBWcxOMG3si0Cf_7S-Dsp_3RtoqQ9B1zLzZOd7Fi9m5fjmTtV0iSLxQy3rgoX8ac-p52JmaGUztmrohyxK_ErOM_-KnqbaGhDtZamRKoR3e789Zkc6MS5RXYaH0WIeAHSr6MM2nXyxFJxYxV5m7kf6s9uDRCHq5bIK6_5XwsbakLkpHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا این متن با دقت بخونید و قضاوت کنید:    پدر یک خانواده،  نیمی از درآمدش رو صرف مواد مخدر میکنه،  موضوعی که باعث فشار  و فقر در داخل خونه شده.  مادر خانواده ، چون بعد از اجاره و….  پولی براش نمی‌مونه، معمولا از بقیه کمک میگیره که پول پیاز و سیب زمینی و…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6523" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">لطفا این متن با دقت بخونید
و قضاوت کنید:
پدر یک خانواده،
نیمی از درآمدش رو صرف مواد مخدر میکنه،
موضوعی که باعث فشار
و فقر در داخل خونه شده.
مادر خانواده ، چون بعد از اجاره و….
پولی براش نمی‌مونه،
معمولا از بقیه کمک میگیره
که پول پیاز و سیب زمینی و قبض آب و برق رو بده  برای سیر کردم شکم بچه‌ها و…..
هر روز هم دعواست که اگه پدر اعتیاد رو ترک کنه، هم پول بیشتری در خونه می‌مونه، هم کار آبرودارتری پیدا میکنه و پول بیشتری در میاره،
هم خانواده از این فشار و تلخی.
🔺
حالا سوال : به نظر شما افرادی
که به این خانم کمک می‌کنند، دارند کار خیر می‌کنند در سیر کردن شکم این بچه‌ها، یا دارند مسئولیت رو از دوش پدر بر میدارن،
و اون هم با فراغ بال بیشتر، با شنیدن غرهای کمتر، پول خرج اعتیادش میکنه
و در واقع کمک هست به پدر ناشایست؟</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6522" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=jxtxHph2GBnzs9Vucr4XbX1HX1KpdnGK67aVcRkGyU1CP7QaSbRdbB29twv-KYqhtGzp1viN9cQ-8wgXcfkygduGyHRfEcMTWEFr13B_iItM8Fa2HoDXlfnXmgZtPR6nJyUCP_xAFZUq3DrNKeHlP7ImIyyAGKGSzLLB5TU6K7mC3Te_kEKoqhKzJBGp-IEl-iOeDp1ihWkFRen5XMsh6TCUr7TVO_8TfIztqUuUYfi7fBD2Rho5e2oM8N1SzOUY--a1hAv8w-YVKF3-nV48quPvdQJEBEV0rfw_KnpkI2uPzi8ICeC7sGuSexqEMmkTb5sYheK_y3YaQPjJCPcewIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=jxtxHph2GBnzs9Vucr4XbX1HX1KpdnGK67aVcRkGyU1CP7QaSbRdbB29twv-KYqhtGzp1viN9cQ-8wgXcfkygduGyHRfEcMTWEFr13B_iItM8Fa2HoDXlfnXmgZtPR6nJyUCP_xAFZUq3DrNKeHlP7ImIyyAGKGSzLLB5TU6K7mC3Te_kEKoqhKzJBGp-IEl-iOeDp1ihWkFRen5XMsh6TCUr7TVO_8TfIztqUuUYfi7fBD2Rho5e2oM8N1SzOUY--a1hAv8w-YVKF3-nV48quPvdQJEBEV0rfw_KnpkI2uPzi8ICeC7sGuSexqEMmkTb5sYheK_y3YaQPjJCPcewIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، مرداد ۹۷:
‏همه ما انتظار داشتیم ایران درخواست ۵۰ درصد بکند. قانونی هم بود. اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین ۵ کشور، یعنی کمتر از ۲۰درصد
‏برای ما عجیب‌وغریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند
‏این برای بقیه کشورها مثل هدیه الهی بود. از خوشحالی نمی‌دانستند چکار کنند</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6521" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHDIluV5A4Izu0qQHHiRjRukYyGj2QKdvlQ0qZlTi5ewyk_zyNsCj3rzFl1rk18DWCpdoSU1Zx9cwB595IgBNq1bb7OCj-5nkC7CgaBcXxfYUxNdn6rp-SEI1rWX9TEeQHqul2FSh4n7ZkIWwVPRKlEL6Olpak6jq2ktFzx8-gPfotpPuC6N2GghyqBuADUlkOv8wkCIGYwToyEqLjdQVRM-ui-07piUJ0lWmjnd77REHEn7Cipg8H03fefkdJLwAJlDaxCr5g6LR85HeddX8NGRJY2ZNt_WZv85ZdXII7oZp_awYIKFqJMJhlVyyqA_gaTDj76RNjoQcBsOBNIaBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLg2JOvsteZRQYik9ICi1nmkR45jzkQYEcHq_ZIf2Z0lcbmIj0ETtgk3n7qmQb6IXQEHnWCwFZMaYUWNA0ZtFybByUt5-jDKZuzeAFzViwsAcBHMYAJlT43yHpg_6TrU5PZ8FBz9HCJDG0lc_15rb9elky5PJ99QBnBzk0vHu77W93B_PWOJ53hupZU8Xwya7VLIcgh5bPG4H5Osxhgv39uLFmbVqloKppTjXjlWIWvQ-Am7PBQnX7_LKDkWAkVeUi-3cEqt1IAJ-3btSAl0W07MjBgp7LvHDAPtoHXl9d1s3z1HpAqxYf5SdZ9HFLi9gH6SekkKbqgdIaJup4Sy2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«حمله‌ای گسترده در راه است…
نه، صبر کنید، می‌خواهند مذاکره کنند.»
این یعنی «دیپلماسی نمایشی»
که مدام در حال تکرار است.
استفاده از زورگویی، وعده‌های شکسته
و اخبار جعلی به‌عنوان ابزار فشار،
راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید.  ما به نمایش‌های بیشتری نیاز نداریم.
- فهمیدن حمله به کشتی‌ها و زدن زیر تفاهم‌نامه نمی‌تونه براشون دستاوردی داشته باشه ، از ترامپ میخوان که مذاکره کنند.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6519" target="_blank">📅 22:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5iWFysM5Mz1CHXM02n7JbkPsi0G807Rxtyri1SHHxiZcc8YQfBCPSh5NN-8oLqvwYSUYwlZsIO23JwYm8p9xLRsB7zfRqeyK6GZ6QD_GzhBp4VxtsJVFEL1hs8_YTMdEwFnwLwEpWB9T-sHb2jnVjINQp_ki6jYOjBU-XKBakLGgx3BVwkl-8bNT0ElltLy774awwHH_d8-VGM5bHO6bdT7hH_NJvYukyCCA-ORcQ9hhgwQ2VSQeifyQ6vfTdfrYo91ERdtEgJBoDAUXebHsWFbSH3WNlds1BtbwwJukWANoQRvGfMShxcgOYxqHLxjziexXprvB1OMwx1ianb5sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4_4iEWgFUVShgj3CO894LPxxKivp_K2o6Gzbi_ZPKkYXa8M9rgu30ME_ioKd1LLDdkW6bpFhoH8IxVEjgwPek3_kleoDkdw5Pi750LFh8cOxaHJ9sBq3exkdKRiB17hq8SbMisCl7WgRDI38UhayCm1FgS8jryRdHYs4Z2tTPKJU5T1E2f15NPYNfWNBHMiGpA_2evPdkCCUaQwc1det87mafb-qQtTbJqVU6TNXaioJJ4neZYXEjVQbOfADHwvLIvg4a-lZqGSDbfx-NtypZdOzthmHpExHYE8FsqcIzrIk8JrTKfjB9Y9qpYjki_O9zaIB52rGkEdhN5AXQa23Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3pPEdQwIdw8aCzHAsij4Wu7UyYWnmtR-v-QVaJ_X4m4t6fCDb7sDwvZurhjQhMY_HqSU-XlJPaIjypo39qAZNx70zfvHu6LzftzMnxlnPa93kjL6_YU71iuf9gzH3i5CkU7_qBu0arRIwC86n1L_1yv3VvA01_N1JONFp7QE6imjJLmuAwLUuwhczAL_4gub8bG8cURfMuW41lP2o1gWv2jnyJ1AAXctahdf85gF42Z0Acb7GiBilzC8j9Nk26jfM-1Dti9RPanuDUppp-FEVzeF2DSJzAsSJ7S7sinU4_FGd1IuFXfQwQGIu9nEasFQI0rEwfB_kwsTBqSxlNAag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qi33_lznHOiCRGxTETxWHmSHZVTStOVXC1DGjqdSV5v9PLEGzg15Tsd7AdTD1cujwUkJbzR7Ysr5BZWatGLQpGUk27J_xIMzR5VzMHmOmwQ5Tn3GDV_Qv7_tmZP_NxRBqYfL02aY19JyB35dWO-9M966sINSRvzw-CRCOpkYNx19UDK6obzDmdnSoGdY7OAJpAqiJJQDbzyazzKiA2ugaTwL2y9UULS5R52k3WlHNv8l-VQo4lP8FqdZMGLNAiF-2oM2zhOV2V9kAw0FFdyZ7npkCRzxi75zOXK6FEii47stIRqzUfFq5yczPJLNbPstOPzBYgCKtnDIY9WxhE9k2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONJU04ckLLDO9BxM5aVspvijiu9YfkwpX5Wky7mATjBAkLUf5a_8bxciLEo2XosMEjtJOmNSJQ68RAhMqq_T1zQ3K27Sc5jidx8wowFUtcESZGpc_PX5MoibHQR27eJRPuSpvgTVOyNpoRaaJpLHswBeXZ7d8JiOlcfBKdHVYh3sLbSFLfNABgR3JMn52RuG8KJF5VOqtOQ6Uf7Uj0ScjacBDpMU7mQilpDarqia9vzPpuOYiN99BLtURZ3AnVtlwc0GKCUIqA5l4XQd0W0-8uuuBHlO1Jm0h2tCu6afMN3EODkPPh8eVve1jt_k4u2dQDtJkeKcncJ--CyN0Vr1tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=YzV_CgMMAu57A_GCmVTq58j8QznSimaOSF6UTBJ71e0IjGoiqwYvFB_1Arej3uWSh3CciXbI3fHr7hLEharYzKwS0vTQvMfgEbgYQ0-oF5wJEbwIc8CTtqy1URB5fnZY2C1xdgGdVZe0JepicJWckK7B603M6otc-Y6uBvN2f74Sd64OTQXpkPwmAsOMrKgocYmYBLjy-OcYa4sG-v_y2Pg5u-LDsAw5ifLOB8OqvNGXlWDCfNnuu1yhb4tEf1XceKec-BJp_IXff1OE1kRhBuKwoajw_gj3xHxSHttmZ-F-r7beruPupbhEKbYGVuNZ1OWJ9_pG_XrirwLg3x5Gmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=YzV_CgMMAu57A_GCmVTq58j8QznSimaOSF6UTBJ71e0IjGoiqwYvFB_1Arej3uWSh3CciXbI3fHr7hLEharYzKwS0vTQvMfgEbgYQ0-oF5wJEbwIc8CTtqy1URB5fnZY2C1xdgGdVZe0JepicJWckK7B603M6otc-Y6uBvN2f74Sd64OTQXpkPwmAsOMrKgocYmYBLjy-OcYa4sG-v_y2Pg5u-LDsAw5ifLOB8OqvNGXlWDCfNnuu1yhb4tEf1XceKec-BJp_IXff1OE1kRhBuKwoajw_gj3xHxSHttmZ-F-r7beruPupbhEKbYGVuNZ1OWJ9_pG_XrirwLg3x5Gmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.
اینها دنبال «اتفاق مبارک» افزایش قیمت
نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.
اساسا با همین منظور شروع به حمله
به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6512" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.   خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.   او همچنین با اشاره به اعتراض‌ها…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6511" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=E3sHn9y5RXAsd9HYLTThSXv56L3Gpb1ju-UZqKY7CYbtMBxDulRQfnDOne0vBPD18LTWxsmsuStPCgy1oz5SU_iQofNX6zKewejPubCnw62W7RDh5xLvLOB0SWSCmp4hVcjI4rt6vxN3L4mpthalcAF2TR7mxEsu8BRPlklas4QcoMQip0KkdxOHbuLGYQ9T0MOumbylOwk2a00_s3DI7MgJQg5SpGkWArp_uZtTQdG4xtHf90dNUlLqcCA3YM1EtrI6sV7BYge4WIOrWyMTlDpW0y_FfQb0Qo96gUSDR2XvKWvJKdh8YikAIqXU0RgBwlNg6THfSoN8If73dJoHAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=E3sHn9y5RXAsd9HYLTThSXv56L3Gpb1ju-UZqKY7CYbtMBxDulRQfnDOne0vBPD18LTWxsmsuStPCgy1oz5SU_iQofNX6zKewejPubCnw62W7RDh5xLvLOB0SWSCmp4hVcjI4rt6vxN3L4mpthalcAF2TR7mxEsu8BRPlklas4QcoMQip0KkdxOHbuLGYQ9T0MOumbylOwk2a00_s3DI7MgJQg5SpGkWArp_uZtTQdG4xtHf90dNUlLqcCA3YM1EtrI6sV7BYge4WIOrWyMTlDpW0y_FfQb0Qo96gUSDR2XvKWvJKdh8YikAIqXU0RgBwlNg6THfSoN8If73dJoHAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.
خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.
او همچنین با اشاره به اعتراض‌ها و تجمع‌های خیابانی گفت دولت مسعود پزشکیان به پایان دوره خود نخواهد رسید.
@iranintltv</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6510" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBI5ExSqUzqruB5otX00aSWGGcDWtEcDWN_k1SUsxdaV1MEtITuKUeONN3lsH8LAKFn--SdnitokdAcvjdrixy3Oem6cBAT5ZI00z7qYEyQ24znWONOgim3v6PuCUSzX6GlxRj63I6M1WtnT_glE_RuY5KtENs3ZuvIUNTrEoexskKBFD5AsP39MtC3gznAlkpzg1ErM7A2LYY4_qdLTQNKnF8CE_bEXD90OpaIRx0qhI3NFR11yMc3YXyNj6smVfRJb1BhiKo330h5aM8PHSf-vfc2UhPxwyQeakLRD8EC8RZoBSDx0X2LfJfWPqOlEJOPpEufx9hbrymoqe0HFIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akNzCn7sD5Ybr8YDJmFs9yeeX2ZfsNHIXp6Zp2gCELY8gDRpJvilKHSQneLbba9mBhMKyLoKkRxavSiOu7bqiDXQ-8TCct3svt3IQePYpX8xQJK0f3JgzfXUZ-ltVQ-QnKNW0hywiS-rZcYtEzp4b33EiW2KL5Owv5gXEfDf8eWSedHurYFS8hBzky9wsL7-SgkK9ypPNbILieh_q1K272Ij86Q5_c2oSjoZTnQbZEneRXB-mycefz6wKu7eL5jm8mDOgpZra21mNp8xn5F75pxvJOsN85Gwl5mG7PoXg0E3MWDK_UkO7B0bUVljxFlet2AggSwYxhjt1V0vj9OXxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=jm30y1NHjlhmPTZ9a74jedbgyQ1GXt4n9fjoJqQiz1ZUxjsXJOIv4CGFv81YYA9xc9W7DdDLOfJe9lQqKXiTqGCEQ97z3PegMo2NrEg04AsUvKbPVCq5MR_z358mx_VLlI-EVjkUwQ16SGDxEmQvCTAVt9QgeWaUaz3EtOnhzfeMZTv2_DOCiTjcGMELM6CkfTVkBdU7m7vHkt9tOHgS8FHr4VNidkInWLgfpCKTyWz-Mlw8etRL0tPQd1LQIUF_28mqfkK8_d0rROMGQ2Mshzo87mpYhL4Kk8fMCnLfeaeEukOgWu75vsEyp9hKDHUu76psRGzvwapPAuUlD3RtKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=jm30y1NHjlhmPTZ9a74jedbgyQ1GXt4n9fjoJqQiz1ZUxjsXJOIv4CGFv81YYA9xc9W7DdDLOfJe9lQqKXiTqGCEQ97z3PegMo2NrEg04AsUvKbPVCq5MR_z358mx_VLlI-EVjkUwQ16SGDxEmQvCTAVt9QgeWaUaz3EtOnhzfeMZTv2_DOCiTjcGMELM6CkfTVkBdU7m7vHkt9tOHgS8FHr4VNidkInWLgfpCKTyWz-Mlw8etRL0tPQd1LQIUF_28mqfkK8_d0rROMGQ2Mshzo87mpYhL4Kk8fMCnLfeaeEukOgWu75vsEyp9hKDHUu76psRGzvwapPAuUlD3RtKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!
که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده
و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AM27O40JhQDK3h1_qy1RdoM2PHdg7lbsAr0lcl3qqO9Dl8nG-zrnydZqlQ7SWj4eOyasTYbc-BJibEbptVEasQTwC-hHc48CaLplTjU0diLYRJSZ5on5P67pfB_7u4BpbQ20By11wMhuDeIGn79XJXNTPwfMRu1xoAlMii7hQvcd3OjOaoSKj4or3TXft571h7Ho3SNXnCqobaqzXdXxdnHwPXE7LAqCHhuNaxUbolnKXe_NA_cpEvkVHWAp3sfe1RlPM49aIty80m4Z3L6aVDmasQNqPEH3Iio17FbToIO_yP9dXZ_ioYfz_DSfrTqCYRbG_SOJiI0UOjY_Ipl9rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBBCPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTsF_qR_EaeDUrbAhuZlPbn8st7yiv-mUCq1rXPzNcfk_EETKQjcw4Livwfy9vc3DAPRdX-jeOGUbVxTsEj1gjwIxhThIHB3HCyhxKRjINRVlzrmlQteAEZfqxYCbsiwaFL6cxg6l0flfnmv-nSf6MMv2rNAoapiiEYglio-iKyIMGR84ctjPgzk4xbnY0AX_hWuG3ZfV_rzV9A-76DV4OsV9DT4rOx_3w8F858soevJlcMYNz7xIVDLLIrjKS-2VJ7NEDcf5iUTEuzWWU9F06G8_5KAU4tEP1JQcXvFSvI_ANjeUJkYWbKiD2_rJmNPBzbOhvVRqAOzXwWtItargw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔻
سازمان عملیات تجارت دریایی بریتانیا می‌گوید یک گزارش باتاخیر از یک کشتی در فاصله ۹ مایل دریایی (تقریبا ۱۶ کیلومتر) از بندر «مخا» در یمن دریافت کرده است.
بنابر این گزارش، یک شهپاد به این کشتی در دریای سرخ برخورد کرد و باعث آتش‌سوزی شد اما خدمه و کارکنان همگی سالم هستند و نجات یافته‌اند.
به گفته این سازمان این کشتی اکنون غرق شده است.
جزئیات بیشتری منتشر نشده است. ساعاتی پیش حوثی‌های یمن که همسو با ایران هستند، اعلام کردند که با موشک بالستیک به یک نفتکش سعودی در دریای سرخ حمله کرده‌اند.
این هشتمین شناوری بود که از زمان آغاز محاصره دریایی علیه عربستان سعودی هدف قرار گرفته است.
سخنگوی نظامی حوثی‌ها به زمان حمله اشاره نکرد.
📷
Getty
@BBCPersian</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29785e012.mp4?token=hE38e42wBuRz9GnoXVT3iOOKisd5OuablSnijocQcralpuQAjm3LW0_JPa2LNE7m3lcyYGI99NobcGCSXNQi3gnruCMINklz_9-2FrIZFlOevYUAfkLhE9VoC5yVObNNwNfRCOdlIUN70dOdX4H_bT9X4rEZBPbJWAjg3iOF6Yp3eqWwPw2qeEsUb1IiHhFmjyrib57zaFIEV_JU6B5jbVP-qLsvcLgJy1rR8fIgY5TvG5AHsEWtCe8G-0bjmRQlrSip2ZADfe63GpR22b3oB_jFhAl86kytoR27wirIZJEVcKkFczu3J5R9WYmUFkFmwzilO7mx94ld6k5P-vzR6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29785e012.mp4?token=hE38e42wBuRz9GnoXVT3iOOKisd5OuablSnijocQcralpuQAjm3LW0_JPa2LNE7m3lcyYGI99NobcGCSXNQi3gnruCMINklz_9-2FrIZFlOevYUAfkLhE9VoC5yVObNNwNfRCOdlIUN70dOdX4H_bT9X4rEZBPbJWAjg3iOF6Yp3eqWwPw2qeEsUb1IiHhFmjyrib57zaFIEV_JU6B5jbVP-qLsvcLgJy1rR8fIgY5TvG5AHsEWtCe8G-0bjmRQlrSip2ZADfe63GpR22b3oB_jFhAl86kytoR27wirIZJEVcKkFczu3J5R9WYmUFkFmwzilO7mx94ld6k5P-vzR6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اثر یک انفجار در جنوب لبنان ۲ سرباز ارتش اسرائیل کشته و ۷ تن زخمی شدند،
ارتش اسرائیل دست به حملات توپخانه‌ای زد
و سپس دستور تخلیه فوری روستای المنصورن را صادر کرد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6501">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=n9cZCk94Bjgq6di87qI3JF9c-vbCnsisTQzzjSbP_YyBFkwW0hiUEQenI48CsksR2k7-AQ1u9sNVvjP25aUBv0-IgeHI3b1s8nosZynwbCV9zd5B9NPqUj0myttSKE-kFNF3mFlCY_0Z3EAC3b3SaYZDQYLAK-n5qyhJUhmWFdv8Q_-SG-Jx8gT_NEUtBBJVKGOLrgBQCvjsro_hqbJSmO3bou8HtRmrp0ps3n13hkVa9eEA4Vr1lD905GUosU_Jlz8PyoLmxvVSnYGzcOxXlwV9SMeQhJ7oT0ZbVKrp2jDUnmt6eArzjx87S9CLll9oD-bgNueqR0U5-WhuxhJetg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=n9cZCk94Bjgq6di87qI3JF9c-vbCnsisTQzzjSbP_YyBFkwW0hiUEQenI48CsksR2k7-AQ1u9sNVvjP25aUBv0-IgeHI3b1s8nosZynwbCV9zd5B9NPqUj0myttSKE-kFNF3mFlCY_0Z3EAC3b3SaYZDQYLAK-n5qyhJUhmWFdv8Q_-SG-Jx8gT_NEUtBBJVKGOLrgBQCvjsro_hqbJSmO3bou8HtRmrp0ps3n13hkVa9eEA4Vr1lD905GUosU_Jlz8PyoLmxvVSnYGzcOxXlwV9SMeQhJ7oT0ZbVKrp2jDUnmt6eArzjx87S9CLll9oD-bgNueqR0U5-WhuxhJetg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی منطقی بود!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=myx9UesId6ylcnV76WqaLl4PrScmK9gyj8Ct5cUsoRH34Dx-ozTqTwYic92FQqMafckh9PK7nIzaJyhyZ_biB1JAcVxGHDEzR-vNRUf4E3AlgcDoSxBbV_hYaFr3QWYFBOBJwwTJUP2rm9YMlks29b2_AvU8U0qVNO0a0vEm9F-zXISAOU63gwiPDYmaGgPtB67Z3-qFjorTCTeefLYFTWQ6bfzzoN_ilVUS42Pqn0VSYjEG8c4uTjp_Oh_ypC1hKDk3EyckBg-n-shPP25ttwRhJzJtlvxZCJWgR1TgKOAPbvA1jonCzFFva1JZVcqfHGXIamVdt64EiHShv2bxeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=myx9UesId6ylcnV76WqaLl4PrScmK9gyj8Ct5cUsoRH34Dx-ozTqTwYic92FQqMafckh9PK7nIzaJyhyZ_biB1JAcVxGHDEzR-vNRUf4E3AlgcDoSxBbV_hYaFr3QWYFBOBJwwTJUP2rm9YMlks29b2_AvU8U0qVNO0a0vEm9F-zXISAOU63gwiPDYmaGgPtB67Z3-qFjorTCTeefLYFTWQ6bfzzoN_ilVUS42Pqn0VSYjEG8c4uTjp_Oh_ypC1hKDk3EyckBg-n-shPP25ttwRhJzJtlvxZCJWgR1TgKOAPbvA1jonCzFFva1JZVcqfHGXIamVdt64EiHShv2bxeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWgObpXROjZNcf5nanqyzAj0DJ_mjP1q-eAe1QJlF0s-C-Sd26QdljJfff6WfBKf0D_ohNmB3BSdYlBorfu19i9diro-BDuvZSJidrnjoxlmRJGXWoDhlYq6kw7Ujt9s98xk7TARK-t7LauaGru5frVUkYi3n5x1MpOEAQeytfzUWlZYxmQAKLpWI722S6ft_G1JKxW7b4kPzUKNSyv1cqkUofVdcIczSuR5uii69ofmJ8xRAnPCblmobcF0Gjn8fCgWI1VTCwVjBmdIDanZNELIyaZb-427BMbL5pAN8kP7io6P4ZyaMLb_DvGtm3multSrKhz_iQyQGODHCorTGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgdMyjmZMsTAgKjYFfjYTWv-0RsZR4gP0Q3atRaD5fFZ6VFt2j8ONLn5AYeWTe-9SsiJRM6n1Nx_6az5nbAXzfo-xIT4lykvfHFTt9l--14P_U680DiySL773bV8rECvtkb3QPzP7TKL8KDzy2qwuXTW8gB1c9lNt5VYqAblkSrrf8ybpOe2x_upwwvWHoNwSJKJcFA_G_n5jyQmBMmw69k3PtuoCr-kF-qXSGMuiENUyjziq_hmoPUj5aXXSfthGZrULBysf-4M7nMUpyn2eX9IymWshwd8wReZfPGoeVfWv4hI574Q932XbhahRDEneZwGF0kYjRlPbh2t6NLHug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIwLT0VkCvbEbu4B5uhaKCRGxAfdU1xYRR92-PJXkJIqhKwJplp613Pw3855e3zQyPB-Dl799VFi_5kxXAH9t6LnF0fNJrkRJya0dLv9M4fmJDw0uNO3CnSE7653MmxiYRR3sULBeRsak5SjAcEbdlc8qiMz0WjjmD9ZYDQOyDCwgjQd0X1aokj3e--oL5pmkAZzILkR1A3YMhZTHJZHm6tEGWk88TZj8CvqSTNepFUrEQapYhOKuwsAv2ANvEfs33e1xHmK08I5UKPIXlqmN5Iox6LHOsnhLGWVlceFgbAqsNDgA1yWxBfCe2vq8Dz7ZY0-OCmLG2l18fTs_9poRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=j-xcq_ydvWr8HvDveEPukX_oRTPZ9ZsDo4I7ZFTcUVJ6J-oTHdQ1QRJChjfEMOERW9BNuFHpfR-7KWo6hm1iPC4PE3h1AesrVg48pfVToVVj62lfF7xfVqUVFwEUT58DnF0XPz1GknnMBOj7s6xMHI-o3KC0pwTTIpgebNVHiQyUyu5enNFkrP1pT10T4gHgz9Pea4r7EDgtE9-nyTZpGBuK2XO-9s2xbQ8x9_j2jdmN4Wd8uPjjuLlER5dr86UJdZByLPdmo8QLfR5luTtIsyzscCFd4McI0XGrDOQ0XwuO-AvE_PPPPxtQmUDc7sCWvscIftpa3d143YUlwJpAYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=j-xcq_ydvWr8HvDveEPukX_oRTPZ9ZsDo4I7ZFTcUVJ6J-oTHdQ1QRJChjfEMOERW9BNuFHpfR-7KWo6hm1iPC4PE3h1AesrVg48pfVToVVj62lfF7xfVqUVFwEUT58DnF0XPz1GknnMBOj7s6xMHI-o3KC0pwTTIpgebNVHiQyUyu5enNFkrP1pT10T4gHgz9Pea4r7EDgtE9-nyTZpGBuK2XO-9s2xbQ8x9_j2jdmN4Wd8uPjjuLlER5dr86UJdZByLPdmo8QLfR5luTtIsyzscCFd4McI0XGrDOQ0XwuO-AvE_PPPPxtQmUDc7sCWvscIftpa3d143YUlwJpAYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم. می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر
همه مردم برای ایران سختی‌ها را تحمل می‌کنند!
[تحمل نکنند هم یا زندان یا کشته میشن]
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.»
اونهایی که به قول خودش بین ۳ هزار نفر رو کشتن، نامرد و وطن فروش نیستن، کسانی که به کشتار و ظلم معترض هستند، نامردن!!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">جزئیات تازه از طرح تغییر رژیم ایران؛ قرار بود کردها «زیر پرچم شیروخورشید پیشروی کنند»
🔸
یک روزنامه‌نگار سرشناس اسرائیلی در گزارشی تازه نوشته که هدف حقیقی این کشور از جنگ ۴۰روزه با جمهوری اسلامی ایران، تغییر رژیم در تهران بود نه صرفاً نابودی برنامه هسته‌ای و موشکی‌اش.
🔸
نداو ایال مدعی است که ساقط کردن جمهوری اسلامی در حالی به‌عنوان هدف اصلی تعیین شده بود که نقشه راه حقیقی برای عملی کردن آن ترسیم نشده بود؛ تناسب این هدف با امکاناتی که اسرائیل در اختیار داشت به‌طور عمیق بررسی نشد، دولت بنیامین نتانیاهو هشدارهای ارتش این کشور در مورد مخاطرات این طرح را نادیده گرفت و به عواقب آن، مانند آسیب به جایگاه اسرائیل نزد آمریکا، فکر نکرده بود.
🔸
این روزنامه‌نگار در گزارشی که روز ۹ مرداد در مجلهٔ ضمیمه آخر هفتهٔ روزنامهٔ «یدیعوت آحرونوت» منتشر شد، جزئیاتی را از مباحثات کابینهٔ اسرائیل و اختلاف‌نظرها در میان مقامات ارشد سیاسی، اطلاعاتی و نظامی این کشور پیش و پس از جنگ‌های اخیر اسرائیل با ایران ارائه داده که خود آن را «اطلاعات تازه» خوانده است.
🔸
گزارش «رؤیاهای بزرگ؛ افشاگری‌های تازه دربارهٔ طرح تغییر رژیم ایران»، نتیجهٔ «یک تحقیق جامع» نداو ایال بر اساس گفت‌وگوهایش با ده منبع نظامی و سیاسی اسرائیل بوده است.
🔸
این روزنامه‌نگار مدعی است که تلاش او تصویری دقیق‌تر از پشت‌پرده‌ها در بالاترین سطوح امنیتی و سیاسی اسرائیل ترسیم می‌کند؛ فراتر از ادعاهای پیشین که دو روزنامهٔ «نیویورک‌تایمز» و «هاآرتص» در ماه‌های گذشته در خصوص تلاش دولت اسرائیل برای تغییر رژیم در ایران و جلب همکاری محمود احمدی‌نژاد، رئیس‌جمهور پیشین، به‌عنوان یک گزینهٔ رهبری منتشر کرده بودند و به‌شدت بحث‌برانگیز شد.
🔸
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از بین بردن برنامهٔ هسته‌ای و مهار توان موشکی ایران را هدف‌های اول و دوم جنگ ۴۰ روزه اعلام کرده بود.
🔸
نتانیاهو اما از آغاز کار پنهان نکرد که هدف سوم جنگ هم فراهم کردن شرایطی برای مردم ایران است که بتوانند کار حکومت جمهوری اسلامی را یکسره کرده و اسرائیل نیز از وجود چنین رژیمی که نابودی این کشور را عملاً دنبال کرده و با تشکیل گروه‌های نیابتی در محور موسوم به «مقاومت» در اطراف اسرائیل «حلقه آتش» به پا کرده، رهایی یابد.
🔸
نداو ایال گزارش خود را حول این ادعا نوشته که «تغییر رژیم ایران» هدف واقعی جنگ بود، نه یک خواسته فرعی یا شعاری تبلیغاتی.
🔸
به نوشتهٔ او، چنین هدفی قرار بود بر اختلاف‌نظرها دربارهٔ ماهیت نهایی جنگ با ایران در میان مقام‌های اسرائیلی نقطه پایان بگذارد، در حالی که برخی از مقامات و نهادها همچنان خواهان محدود کردن جنگ به اهداف مشخص و معین نظامی بودند.
🔸
نسخه کامل این گزارش را در
وب‌سایت رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=SR1EhGWooVAF1U8HF6vcgxM47-19hWbRI-GgoH9fqfpFZLOa9kyz74x14sdY7Jx4-ewUi4fAlp8ArqRg7sm13abmDv_nTxzq1fTuS4VBk9fUqQgzcQam0bPGzQfbsk1ZKYpmoWLyfGqHZNDNRT55v1MdszOs0FUKWgLcTYOLmjYmoeD07y2NjNWzybRkz51GD_iCFKkNEGMXY00F5mRQO8w3xf7TjAbAQOo4swWpOzREGzVxQaLl7bHGPx3zpoeJo1MSeILAXmUPsj5akyjWwztz91QRTgRWXvSa2KlupYczmzmFJeR-yqN5v-2K9kLV2SQ7oBIOA6oI1LJ4uTqe8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=SR1EhGWooVAF1U8HF6vcgxM47-19hWbRI-GgoH9fqfpFZLOa9kyz74x14sdY7Jx4-ewUi4fAlp8ArqRg7sm13abmDv_nTxzq1fTuS4VBk9fUqQgzcQam0bPGzQfbsk1ZKYpmoWLyfGqHZNDNRT55v1MdszOs0FUKWgLcTYOLmjYmoeD07y2NjNWzybRkz51GD_iCFKkNEGMXY00F5mRQO8w3xf7TjAbAQOo4swWpOzREGzVxQaLl7bHGPx3zpoeJo1MSeILAXmUPsj5akyjWwztz91QRTgRWXvSa2KlupYczmzmFJeR-yqN5v-2K9kLV2SQ7oBIOA6oI1LJ4uTqe8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=vfr6W2dFlwmELw1qWzf_Vv8repQ6vJv8A7tpkiMu6CxxEd6GzbgbGXbkX2dYHd7yZPOjN675NzqhIgpCMSJbvVwL5XFrk7DuI-pwDF0uE-eS7bMfg8w8MuvjssTNzFwhviFkppVMCHZHb0lmngeoLHZzJf_LLNKmbq8eI4GtNtAcnBLzhcpmcUe-SLx46i6tioJ4y6gLhy1yRPqTW3QHTwTM2ZnShePKbLmohwY8t7aSNiX2ka18aVKAZDoPnRyI_dnUsnQVzC2A1olXJ46ufvhT8jfD5PIZHAUHfCbMTbkgZpI_5y5ZYuTKno-iZh_LbzdWF3lh4Y1Ft9bR9Co5UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=vfr6W2dFlwmELw1qWzf_Vv8repQ6vJv8A7tpkiMu6CxxEd6GzbgbGXbkX2dYHd7yZPOjN675NzqhIgpCMSJbvVwL5XFrk7DuI-pwDF0uE-eS7bMfg8w8MuvjssTNzFwhviFkppVMCHZHb0lmngeoLHZzJf_LLNKmbq8eI4GtNtAcnBLzhcpmcUe-SLx46i6tioJ4y6gLhy1yRPqTW3QHTwTM2ZnShePKbLmohwY8t7aSNiX2ka18aVKAZDoPnRyI_dnUsnQVzC2A1olXJ46ufvhT8jfD5PIZHAUHfCbMTbkgZpI_5y5ZYuTKno-iZh_LbzdWF3lh4Y1Ft9bR9Co5UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تبعیت از ولی‌فقیه بر مسئولان واجب است»
می‌دو‌نید شمر تا آخر عمرش
از اینکه در کربلا شرکت کرده بود
هیچ گونه پشیمانی نداشت!
شمر خودش از فرماندهان ارشد امام علی بود!
توی روایات اسلامی هم هست که
هر بار بحثی پیش می‌اومد دفاع می‌کرد از کارش! میگفت  تبعیت از حاکم اسلامی بر من واجبه !</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=PPKjeFKjXJgpn-4sCG6ntzl2qos3Kr9d32y_d1zG_41l25VNbT8YcYmpcJnQsFc9tEldMHTtqiHH52XdfX4uZuwmFqA9AoQU-nczQ3tgsvJhIY6jO3gRGP9pG3d7SP0u2GFphTfgroODHx944MqmdiVIgehdBMQpJnAdNBw6AfdluirrFzU2tPBbOSGh6-uPau8r57HfcHYkIeWzRgug7e6pKq8h-Tj7e4tg9RNXpaur1HkUjPQON1iWahOrZZct552wVNpJk_7IT5rI4hMJAW7VwZP7dmItwSrGbKkwIJazh0aQPMQiiNt4-2DS1kzowatOKhK_-6rLDrllSPe2Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=PPKjeFKjXJgpn-4sCG6ntzl2qos3Kr9d32y_d1zG_41l25VNbT8YcYmpcJnQsFc9tEldMHTtqiHH52XdfX4uZuwmFqA9AoQU-nczQ3tgsvJhIY6jO3gRGP9pG3d7SP0u2GFphTfgroODHx944MqmdiVIgehdBMQpJnAdNBw6AfdluirrFzU2tPBbOSGh6-uPau8r57HfcHYkIeWzRgug7e6pKq8h-Tj7e4tg9RNXpaur1HkUjPQON1iWahOrZZct552wVNpJk_7IT5rI4hMJAW7VwZP7dmItwSrGbKkwIJazh0aQPMQiiNt4-2DS1kzowatOKhK_-6rLDrllSPe2Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWXfisTlCJNnpjq0T4t92iP3eJTbc8IciFMl0YssSOKqbsyc9tZMQb1W5FO8NsHH3AiEycwVoHjyoqAG26lTIQvdqerAuR4F140IOG94QGXSJWDAabuDyYXrrp7H49up4PXGmE5T26vQgdSXe0XRIhfxdoSGEuIx1gnrNuC_LeNCiXDTnU-G0TITc53tmstWKMeFyA0HtUexYI4-GIHkahhw4FvJc5spcX9oaN3GtZecLw3fnbFGg7aQQoZLVTvzZP66ym0X_fBbdYLeSSW23xmGQ2l0rs3B5kZ913veJwRB6UIRZCWxZ8WO6hHSYUUrPswus4wmCFXd4cqRelJurg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgKmoEzS_0MkjSqoFN29oAjTY_6ID5ex3tZVznmVqqiusu-Q5Hj0ctwn9dUa8A6NCJcnFhxuWdYaJLvzKO1cB5YgC7y2K9FVrPFLCgVZiTzeXy5fd_l9N3Q2eJ-NlaKNmviLTN8H_jlgI2NHiKRCMlvQTF9QbgjIDtRQ-OPXriMfTR7qIL8rj9mZ_PLTA3u8fVUkg1PLOX36IQWfWQJBMA1fP-V89Ru9j-fLLSOrpPe5xWyQf9s2jp1HRT1E9yHIEa0ddALaI8AulpV0rmPFtjD3azbqDFoRieuUf7RQArU6CzXTozoot-cbLolCDRJxeyTFDYujXfuA9Me4_TUz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gimcch9cWuJFGxlrns6RR-LccFtXnrbA6VajTxyUQq9aKtia9PV2DLvJk-U7wX1dKWwA2nwnDGILQ_oX3a_qhJ-Ve4BrOn7QUSINg1FMNOuZm-SdxrZfnwJU9TuI5qXH87B5dLfT7b0WOLRACKx9KJxeXCCLQElgxoYvN92qWkMBwv4Jtb91_fm7b-JDfEDet-fP_tuxNkpsywB2tye0g6BG1_voNzf4Q4JIK5gAKZR9lpLoA2VeBw-MrELCf7NDeutRrDnaAwVa2ErPO8ueyAXpxJfiKzCyVvQBGn8PVbdow9r-IU4y0mOH3J778Qnr394Dbcoz8gJQHZ3NgOr7hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oW5CPPljESdX5qw8r554dVyDPZEvgtm0JGofZVl8wszuE7ECBAfj_xgM4yvGd3FAjjZ0tI8LDBPShwU1BJkG4R4xfPZAfKXZYqz6BAiI-QMp58zfuGP2GTSB_NHgxhjPML-QGX7AVz8JehQO4GAO5g9D9PnDaIB7N46rLxhEq8ziprc8Vb8AWXKgGf6a4PpUKTnnT6R2LfRT7w8Ywp-l1GevpJa9twIRVtHBWDqjBw01YdjLsbXH0Rd5USh7HpJsib0kF3pyEN4mgjK_qCSs--unAKe_ELVqSMJXOwy2QNjRkO4NciS4VpP9IrpmlM5Rlj6mxJejKibrvmkOXdKwEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pz0oYkFc08Cqv1m5YaFZjHVyqjkbwEgue-sQRFmequryE6vwq3bKbQ9t94dkE63hsfLvPSytgm--FV0xwnhcQWZrYfIodTlGko9VSJphJH1CcYzxAHIqymJ_ZXA77yiFpQBvwtpHdqiB-qyN23N04Qxkr1yYEojAIR1LkNkb2RA6sw0yvY0H6OF1tSULr8JNzdhzoemzr1fXk14DRR1icIfQxXFbEBgWEkgK5DAJPg_jIov0tpt8yiN5POCXr_b47OQiUV_eH_o_NgPPJrHlybEPEPJuNrNKQ2SdQNiDHsd5xt5Tg9TKyD-WDov0_X32UHGZhk3iKAs99XDofBgFtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlVQtrqorua0NMig77oLpCo_gORiKyUqtSNtcZ-BH5rjOK08kipkaEJ0AghwbhamXXxfpxZGUrhzaldQgpuXVNbtMbUWgq-6Fhc6XU61rXtZ2pu_Xx9OmnlCJdHbCOSIjSno_HbAUeWVqHb_1OfeVIueMKG5gescBILL_0V8taaCxum1PUy-20TB3hRF8fUZ4wdTd3ivBKuu3ogjOSns4GwK0A7AIGBYos8LoO2e-DUkCC9cnznWuOv_WDxOJZ__hm78aD2oX2C-nhqzE4agzNpVspMDz4pNKjARp_6lNGNHnlIkvkvDockWofY1efs2hWeFEl6gv1rGlcvxe1zYJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvcg0HzeCc6cfZ_-O-UWYsTCj0kfAlq9nzcPLV2ezWmmNrCpKbk4soFGeqbeW3C_qORpS5R0mJaH_5ce2IFb0w5tE-MU3y8XIlAMfQ8jjqy3LVjJemLl8lxWxzPeIncOYQBNdF3koFj6WytaQALEsz653neWvAjupREk2mSbtnw5oeuPQqiB2O0LgbNv7fVj4zrfA8JssO0_QR6G4T7yGnqqxx2ll1bgguOH9xG4CpRs4ExFBhEbk9N43u0WmAy_06veeHoFY5qaios-hSRThPjwzdRecapgDuG4OiFJzeJU7d5U0r5wBab_MRvODoN87jnOFsn5M_7-ZeyO1nUO_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phKDXC7j_0QqMTaY_mBtJD5-GCA4OPZ3YaMbjz0ukXZDoANTVq0ybP9MqkNqTZNW6PwbTaTo9EHGM7y-yW_8NvNY6S_RmCWdH1CClELXcDs7Y3KDJ4ex_3rbp6p3XWZgDaKvfYEp3b3Yga7SXj0KA2s2iZt67CTbacO6Xoxnvgana8H1Hlu4KkOCdKy_sOC-diFbfjImHnDXTBO9RSISAaFY-RIulFHq_-RXldoDl2iZEy-8vbgNyMkFjHzx6rERqxBhEKLyTfjT_jQvxHdY1h1_K329nSkTAebB6odHBWEeWxch3cT6LSVmuLy3d43ZTgwXoAiK_YTN3WFPQYsYqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfzoaquP5Nf8xtC2J-IkjsiAENtOZdpx7CGfar6uGb8I1mu5L-mGDYKYd699LzfmSsLb_VcVsroMSJ0AJsBYUXWJ06IkmVVUJLBmZn625ske-PpMJpMigfs5nBlQ8Jy-L9LS6DiLMGTV0jxzzjetTfPWrk411UC-7rjRZpUUjDW4oXNd6MTTzNj-Rt4snCoidNSdFX0lTab5ja6PfKSWwj0bteLHR3myeKAbkrn4ZdkcVZEimrLDI6DM4QkNyOqgDQDQFo0aSC0YZDFT8NAmprAXUdyeNOmE6nThMIheTqvfKjlIYMQNkuI8FtjD3G6w8jphVG1owSLxJbnLBQqn-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرعون، جسد نخست زاده خود
را در دست دارد، زن فرعون گریه می‌کند
و موسی و هارون،
در گوشه‌ای از تصویر دیده می‌شوند.
برای مجازات فرعون، پسر او،
و نخست زادگان «همه مصری‌ها»،
«حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس
که در زندان بود.» همگی کشته شدند!
حتی! حتی نخست زادگان گاو و گوسفندهای مردم مصر!
و این تصمیم و اراده خدا بود!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyxfh3B8FxgzYqs21_I7f40FXnTPmMarxFlnnAF09HzA09Pz8HyiZrHPvVedv55anDobGSFYjNbvWVSUVImjfxQi7zAg0Qw0C5oQrraZvB4mo3xg9EWzgzY_2XiSagEuytorCOj3o_JKv3u0zwpOqwwSv6g2hQNIcMsis4sIp_WPW2aFi-OSjF9PtvrRbOjnRT4BIFJJ6bkAzNrKlIvXTyUaakOqT8B8WU-btV-ZbUUCoYb4NBy0w6WHpbtokbO-usM7RXnnwSpGApp5ON29ovkxsee1vNoXHZ6vUfd00_zSODtS0fS0_qVhNL3MUiy0lZmvIZ_YsRrc7JgaNbuTMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQNdEi7IAdh3WPn6OfKVJeI0ejtoaF3e2C1qDnvLiKXzSmneqt47gFhoflf_yg8kiLh2nRkd89bR8TtMu9Xx_amXDJ4FLIjqHvf7QFKpxALz9IraXRn8FJJK8MvR4M2qG2unRTHv53637YpH1idrYU0VsO71FKwUBVQMPgt26uBH3qd7060EW_wbCumavhmxjiTmcHpq5e8Ov0Q9Uq27BSPaFRIsjWRjEVpLCWNy3QW95h9S8r2V52qEHdcoHVXcpLF3nu-7DIGbUsn4TBVuXQ8kOFY5s-dRlA9cyzgFSuBjwYpg9DpH6pYDSozbihQ-SYMqs65ewYLWRp5RuyaTeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRqopXK1ULoJkIvjDv0aHAeiW8rOrPMJz2w5UzJtxg_8Yk-_m_bXiL4vC7xF3I8z-egoVnLpNOQaYcYWzP_K3Dg1NoR6_uvSNJS10MHN1INPHS0GadkHgKNsX5hmpkatt0_HekXw9jez91Keh3qbPnCmeDZBpNMTVrX3vTEvRJxHUtHM_IUqBWfQhFxNcpqi2xZhBooBCLd9UxPFmd8HSPgxlyP_itgoPKv-d1VkA58tKvUXaYKzyrTKzeWX3oUUo7PiWMw4K9LOBAeG60H_TdI96dWlxTyiZdRQugV1rEFPVuydvKFMmlC9YpaSernlQjxjaHVxRLr62f747bHZaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d435j50B2chYeqcefDX87dr6J8Tc4pxoP68x-yWKJPs1sW9pOv9LO4QwGxnzmBwfC3vGpypRAgNHjOxVzUG5zB7zba44GeRu01cZwMIgzWLLUCQ3J02bPHlcmY6z_YyXA4HRppsb3rtQxDBZLSz7JjErS7qPCRSKMZRWKhEL7Z0cQU4dgu3A5_bl8s5RMa9a7yfOTc0Yrwej0WkBL_3wy0Qx3wInW92Qh6CTUnE6d4BH1dhZu_z8bwdcWpaUluHx-BDyK_baUzFvwOO5G8be46Q0TrtmonmG1_5qkHIlMJes7b8A-8D25jlVAx4nBjSnm0qc75pn_kLIRHDuoAfEOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -
سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!
تباه در تباه!
خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».
احمد شاملو - غلامحسین ساعدی - اسماعیل خوئی - منوچهر هزارخانی - هوشنگ گلشیری - باقر پرهام - محمد علی سپانلو
اینها روشنفکران ما بودن،
جامعه آرمانی اینها، ترکیب کمونیسم و اسلامگرایی بود!
از مسببان انقلاب تباه ۵۷.
از مسببان گمراهی یک نسل از ایرانیان،
از‌مسببان  تنبیه نسل‌هایی از ایرانیان که هنوز  به دنیا نیامده بودند!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQ5ORWjGMOCiAeyMyyvp1hCnF4wlCI5bY3COVGmk3CQJaquHxIW0ixD6gZFlJMQVfnbFERwPDHS9auqQSD7_bln_87YFmh8AwIzg2PLCTegFjSzQl6ylJ477yf-1m09UWx4UI7Izj8xRPXPoH8AzuePBZzjj427FO18jcXAcLFs-aCinN_4R1TJrB5_1luorvfqVFZaqs2nkXH7sU0A7h8P7CI0aD_XJ4DhxZbsEeiaDHaps89HvktqHnCgX8PvHTi2AAaqh79wAiMqbdzrruDEOuQExTGLQKBvOWPGeGgLnRIVDtcYegLkOyHayyQ1u4AATprpn_BE5SviZbSR_gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=fgJcRchuZW92tsgjpd5hr_gJ857Y-1xqYebxIrDXtWs95icAiTMSPBgKB1pIMgoaNiPFPWg8kyVepFiE6QiVmuhha1isHvefSh091hjqtSxGNlEZbdJdn5Obu0sd_wSIZ5d7Wzq3JrE_wWp9sJeAPJ4w5NXkTjTPmSJOY1WZffrQGu_pHe7WvDygsmzsrok-17ssnwU976_bXlWnVpFVrqsR44VJTnRo3JZ0Bt1yPhJy0Jec61MoKLp8Rvtv0NncMg-kwlzDzyw7XsmmAtGNvp3DiEve2q3ZdZEzXpAcjklhQADUEG4W2YAKYVjP0gKAZblJgFvpoLCnm19EuWUlUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=fgJcRchuZW92tsgjpd5hr_gJ857Y-1xqYebxIrDXtWs95icAiTMSPBgKB1pIMgoaNiPFPWg8kyVepFiE6QiVmuhha1isHvefSh091hjqtSxGNlEZbdJdn5Obu0sd_wSIZ5d7Wzq3JrE_wWp9sJeAPJ4w5NXkTjTPmSJOY1WZffrQGu_pHe7WvDygsmzsrok-17ssnwU976_bXlWnVpFVrqsR44VJTnRo3JZ0Bt1yPhJy0Jec61MoKLp8Rvtv0NncMg-kwlzDzyw7XsmmAtGNvp3DiEve2q3ZdZEzXpAcjklhQADUEG4W2YAKYVjP0gKAZblJgFvpoLCnm19EuWUlUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6BTb1PhRAL8W7unk6NTWa9ghFtvLEIUOQDX0MtD3Zy32_pp2e2VOhITfj02LT2MTBEX2C2J_T3ioeKigFthYnI8wILArTSD1w6-DWOLR5_2RH6MFPsj4PYcQxgybdbZhTNMRFODR4h6McxhNyIGUVlLaqp8ei8vwzBR4ZdDHbGpYcWxhxzLR35Rrr_YvzTZkYNTEMBWxWC3YxhQdx9Pa6opXL8cNDFDRVaKvQHdxQBJszg9UcUBxSRLYZHgZOE5atM--aBfcCNSNNT9SW-7Kn8pgMVSI2q7W0IdzyNTPd0c_LHBJ5_Tw7J3opkVQSyIDTg0uGkW4CIs4GNSkwvkpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHZFjaWTDHW7bufCQUL7w3LjAdAGkCk_8-L4nZYnOOKZP8UnkgX0kVYHSHPk6iFWU1glpTBzACJkHiHqxuJCk_HwloQ4TDa-FKEFKdGdgpknGd_3c41rjZl1neUhGFNr_jnUAWK8wW4wi5eWJ1iWpVNyu6WuEDBUWu_7yuqw-jt-3zv9pJEoV5DaaSCeYp3CqX-27SjpZaadbSXORoKLth3iQBx9_5g_aQk-bBPtw60pmzeO34DbgRIn7brIVIOR4kgpd6U2-wE5NcSZRKglqdwNhJaBo8An7Sya56xA2cd4UKTlfjcyhXQ5VIqTqWUf6OJq8LZgtoJxm3ZfYcxgHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZD42IWsJNEMkmQNJ_ZHqxd3WEHNTzKGZMiOfyCBHksnYEl1yb09SE-F897k0Os5hfDEucXt5m6zR1C4qQW-b52fQIWnwXDKyiHVrZXwSChJw_Yx97oWYDVrk7Su8cPRj0sKXPQbxJmuoX674GxMOkLbdifetFcD6Ioo48K2uGlDFaJfTltNaHb_xxQCPo8lUGoP1hVfxAuVW-UOV8uGW9bgy6b5yqvtrkzJM2wON8XIackSnYm0BqTLJ7-obGo_pqdu7Kr2lwrCoVaa8-hKtQl4mKGmvIE1L1HV5d4uYpYWJtLWk3V6EGQlu4txuRlHugJgxp1nsbRvpMN_e_i96Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mh--odXdngVU2ByDE-LuiVwcU-j2CcYyovYIxD1KbmpmN_ZumQBAavvF9L-p6g1i-jslS9j-1QeBga0qre1-f_dRqfnPaHqSKLrrdm0237p3HVJXwzGwoj3-UxgEekyr9s71kAyIM2jes-SAgKqgK27my1oT3pGaJPJZV0pqUs-aYI3w7_8MiY5eXxZQ4TGv1OgBiHEn9hMuAX2yyQqMmbWP_6287HxSG_prSthcKHpndIoQ1rRhHxmcpfCag3komPdALzGNO_JhubVE6MOpWunAA7b624sJg84yL8DvZVK8jQsOdKC8s6s69u4QX2og0QLD6jNodlkv9qzwOJiqRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXNti48I7t0G4Zzx4dgDG33DXn-23O1QGmw1AsqG7RiFkuzBLWOzWHbh_g7sVV_HHMagwgLujI8Ky25LaeXnpEtxVmWID-GjjadvM_IqeE38Gjctxp6uwYscF1_dsoVaTxWitUTOY03nF1JhF99u1V7cSOKZSrKPayWYLuDBBtCKmMuGg9PYN066odUAB4lvzA1-N3RlEIUVkgOVBkOR52UOsmQMrOy595RkxjKiaSdDMQmU7dn0A45II2N8-dOIxRWzPjhLpFpaHBaJZTHGiWsjVXNHHI539EElhxQqmEbQi1Gy-ZE37yZ9lsDk4_977ccUqRT2iealvWVPZaIiAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArDtUiWGapo9T-P1deKqLMp5of0RdVuLIln4F2B6S2o7WvuWt3Z9IcRLwC45UNswD2PTTnJf1Ag3IEMyoUTfoFy3Akz3wQpbBohx9oqN3zyd3aDvb7ySwjkqznVUllwjsAnd5X72Yp53cCzTrujGxQOrLjorpfMIUIh_v1fxRKpjAQm6h6bx2XBK4vF2ySXDFgbouCysd1sEHDx-o3FdEH5FEqF2M_Xjv8yZ33KIvHtb2-2GYqLqcwVfdvb5MGmB3HOrfbc2R1oYRhogc-9eOqM_xw3ZwOoYKGdeifAkMwpu6tlke8BLhzub1Fa3f3dIHXXANrce3nwloaSgjXXxXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZpSnUremJtdTlceq4ruS5MLz4UG1yhm5O0MUiVJKtuR-8-pM_XLH3eynLgqHnBjWnNdp_n52j4YP0NIhQi1tT12zxmxLsjBnY8w4KSlxS3ZFhhqg8PpC4ShkQVxSOSjh8JgeQow8O5wjI-7he7LZNhGxK1SRaqWywQCo_4hoU58loVXif4R5522zVXCTOOA6uMWhrImRN_Qa-Tmm4PwDrBCl3SeCDRbDJonOmxk5zeIsKOkTGQlPg47Jc4-Q534YF_upwA5_cT2Dzaib_QBKdrSbBLwrbGeAtE7UgAgJ5N54cUcM5iAIryoPHkL5vb6evOvw9rLi8ZSOAlS2Ne1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhXHcVSToI-iBRZKB3-aClwlb7s0H19EwiLk-D1cqX2DDmulBn9cOm0mYMpuE_NzH451xpEE1adpVB1rHqKldon_heCrMZbIT74zYJd92gQf63ynblwVfsh7IhA69xLI5tfNhBqLWZXZ2JGST-5c852HuqgVElXBE843gM8deLtlCqBCn_SuftROnUkILs1KRYsaidvKdSno_CNOgfITwOgkvBqn-66Qp-pNm1BWSdxhZfcl5R_wt9n3vMOUnK7bLfPwCTX0Cmm6Mm05-Wbr39uFk8wrPjdwPsk0j1v5-AvQZfvmgD9kOh48OjLDdXxxglL-xvp_HW6B88H74UXqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دولت ایتالیا آزادی رفت و آمد هوایی و دریایی
بین ایتالیا و اسپانیا رو به طور موقت لغو کرد!
این بدین معناست که تا اطلاع ثانوی،
پروازهایی که از اسپانیا به مقصد ایتالیا است،
دولت ایتالیا مسافران آن را کنترل خواهد کرد.
اقدام دولت راستگرای خانم ملونی،
فشار بر دولت چپگرای اسپانیا را افزایش می‌دهد.
دولت پدرو سانچز هم اکنون نیز دارای کمترین حمایت شده و پیش‌بینی‌ها حکایت از آن دارند که در انتخابات سال آینده از قدرت کنار خواهد رفت
گرچه برخی از راستگرایان امیدوارند با انجام انتخابات زودهنگام، انتقال قدرت سریعتر انجام شود.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=crfn8jMIYdSvzWo_5-WFaVKFGNeRe8AXUJ_uiILUMaOqe-EU1QHMfO2vARvUvPfDZEl5kd1AH6n-P1JMpzeDqAJ15B8RFhsziA0DU8SpW3_FQYS2WuOMOOFzhI2V806VtrvOa_ssrxr-xpeX3L6Z5pYic-_Zek29RAJVQ9ekmkwAjvEupSHiyBHHc30YdNHrAQMl8-4VlomjM_Pvze0jg_wmmpNm4BBYNmG__gnGGS8TAtRZIkDMrq8bBPwn9LzkL7weUx3hg2M4GEHW9aBJDvilIUTp83kwOxrX7YR86-cQB6pBBLMCXEFKG8gF_xHCpWQWfEhnrd0dj1AAqCGrpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=crfn8jMIYdSvzWo_5-WFaVKFGNeRe8AXUJ_uiILUMaOqe-EU1QHMfO2vARvUvPfDZEl5kd1AH6n-P1JMpzeDqAJ15B8RFhsziA0DU8SpW3_FQYS2WuOMOOFzhI2V806VtrvOa_ssrxr-xpeX3L6Z5pYic-_Zek29RAJVQ9ekmkwAjvEupSHiyBHHc30YdNHrAQMl8-4VlomjM_Pvze0jg_wmmpNm4BBYNmG__gnGGS8TAtRZIkDMrq8bBPwn9LzkL7weUx3hg2M4GEHW9aBJDvilIUTp83kwOxrX7YR86-cQB6pBBLMCXEFKG8gF_xHCpWQWfEhnrd0dj1AAqCGrpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngeG8M7p48cPD8U4NYzsJhveGDz0WJG0Qn1TPVb8FKY_5Xb3QbV-VIBDS_Ux5igw9zBperPnHNpX6aoDBnOvbQHjK2ZAUUfbVnzouVRxY3cum_qJs7LL3rV_6qxB74NLmTne0kI9BqpLOUL_b3PwomCrJrOPDPszcFT3dp8GDpFqGhNoiM0irWBzjY7rxXI7RB5NG7xXwIuVWb9tghSK8vGxzx2vcwS5okwc9kJ4wLWYHr-WRV3kSVbqQH1juLLd3xRRqUuWcmKsJcmx6UmAjPe3IllXd7AbunDSZzeqFtewMBa_JzV5p3B2AZCJRl8AsF_M7hnCDloO-meKNx8zNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyELJzJyqoxbvVN22uUjs5JZ-vv12EjihdStSSqyi8IwCA_9BRIVC_RpL9xY4scAe1gxqg1coGqC_4HVAscNVAgJUQixPbHv8QL_CDntgZF8fJD2LS4AxW7Kz_i5CjCH8K6_tCEbUdBEINPF0mBVz-DmZKwY1AEUQ-jIcbKWoCAfxCg9pzzg_PjoOEIJz1H8CQ3Y8zD3ZHH8iGusskDp2-5sO8-t-zyTSdcJJt_f9MvIexnLlarv12ndxCpLN06CO3aDvM-ZPMKHl-otuttxkx51bE_n1C_C_GWpm5Vny3K17JmoyCBwFtWCNYDw6htTP8zy2ZRZwSD3EF1FsdeK2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7ijWHRpIeTttlurFN8AaJPPOAY_YuPCYf8oniJsnFZ6Vdiz4IwUNdZHLF7FtAgfS3yZb5HKxj31zUGrOiZpl_Orh6ruOAv0HOf_uT_F4TjrvgyTV2yHIAiLJFbrOBKhhCmQHcJaXvxsqFOEs_V3FaDvY-07H0CXUBOlBza5FwCi0XVwG3hNQzGmQEiGF6pzzSx6Ing8aW534p7qM-gvQbPplv0xFg2UvIAYIM9SCY9NjDDWV30qETkzAqjvZ56CefuUd3FJ41S1uXOE1I9QSMUZv6qvzSV1PKrzpULcdnnVnseugkysvlYEVkUeUeeVHVzIiGJJVJcVig-3-PmHOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Owz8kHpo6upqVlugG3c7CrGzeNwxEmT8Dm4lC7e52ToAQao7e19B2myoQkBITu6GMkWKmUpwRCbBF1uBLO3F4LUu40JifHLttjcCuNSKfMD6xygSgnsJqiqwLZdSNJkXzE4XVxwSsxYL3c4eP2uvEk6M0PWnL-Sj9nH3wua-fyx_EPN4y1nQs6GnwCeFBc0sDy6ywYuEB9sb4cywSC0lSYeZeEG3nNPp8rEZEwTVLeCbzTW6_WhJhcqLAYgwgyK5nNE-DM4-R_NRXiQm-3UD3he5rrD34o4_tkgDLpp9-3qsaYD8bec47ghpuwYJuC5cbg_xkw4RAzyWjt7jxW-54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbZaRETzJ-7xIDUrYe1xJEptCMBXBu7KD3Swx_jFn5SECtV0H5Cx6Z4HN1KSmid3rZXmuh6Qfi9u96Z53LLpwDyVuVnVHiRbPaqtKdDJQfRjktdSEHyxln6dUKYithAOmX3UIobZr-RBI2enw7YvgDQXlPBNE6luHyzC4zIX8HcyxE4X26v5B-8Rt6g0lTPe3ePFxDzkY_NV2JZVPsc0k_9KYHHtJo1D9Mr58qJE0q6XWydh5V4N4FFRpOhtpXjqo7BzvjXD6dhumoRgT8Mc_hTIXOvWMFzRlORqFCxX-SsrZt1qYyLGn8hO5eez5Fw5o88oClt_Ev_BcczKez4M9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQuOdpG4KwIEtwVqUX37_tDkvECa3R__w3bS3fJfFYbTBI22mrO_nCLP_KHKvSqU3h3rB-aGcwlEoDpH5ZhUF3mtKGg4r19OJutcMlO55l6RsDXn-kA6Z0xbH0SnCJBWHcEN_34-1MiSnWqrYohapsJl75vGjmr6sN1on9811plF51OKE2U770PVuY_bT57mgIcMWWcWsm1QBkJiQskwsbSi17lUttIvpBip1RQcMg2Pk_ErNmwR__t3ThfkibKP2Hyz2A8aMKRizVmHk-ETTko_mzQhGIC8WP3PSMb-wIkO_Pz6z30oVfBXqgB4IehkKGFgVhCmCa-T4_hMuO8acw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6Bjl4oSG74lSC6GKmUhWwCUXECX_jEcBN7a1Ys1vtnOUSDOVMDsrIx4iuI4f_ZjV5miorYbynMFCdjY8DR5Mx3yeSQ66N72KPNgVNJF_Hor9t97J9s-UO1sKLuxUjKloq6locnvzIQ2M_cRzPV3yp-70S-U9ZfY4zdZQhTWd-1DXopKhY_9u5yLprLAoQc46ybohIwKkKnTj7lSHlEfUUpNFmiB5UuXU8Kf-QAuxeOwPgZBbUzXk2dE6jpI9pqySE7qlh9yg_FHD6siuo-Xbq1LVQRSyEP90uV5zeqOYQBbmfPrDYR5Zrh6HSv58J8wamZahsxQRjctdpc0WPIXfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=QwIZHzw-5IspvUkRYH7fcb-2JvXwfz3tEIvQkmSq9ZcM_ygUk-hxkRgVCRMfoIXkCghRfrVNPi6abwOksc5k1iO3-u6YnB5Q8B-G2Q4R_5WMuzYSEF8PwIy9ttMTv0qnZZR5yskoRQW566hXE_hAKA76UQzlAheopGJutU8h_KVliRNLBr8HauGf_WwnKMqNToG-Punlh8eYEE16zV9LM9hik9_3OGwMFNwy8nrXKUf24TXfoB3p2WMG6if9tovu3MhHW1B0YoJv7cG0dY2DJN1wbDzGvFsUNyg09nGNAlSc-0yCJZGN5xFv-JEOMwRqabZRrKgFx5j9Wq2vpef8OLjTpNqlcmaQtzxVt7hKx1RcZs4aTVdp_idChiN8u0cIRxiUKnFt4dM0De4y-qwCwHziO1yH9p9VbaJ2-M2fGjdKn4u9YAbCQQC69PvBzRkydc3dXgRJ0rtZExQkRY6WPeol0msXTx1zj8EcTLmOJFcdaaM-sajydxIf0eIvLk-nbj3urTKbt5fVQ7DaEr6q7EgmEpLZtoLDFNggOyS3cjdiDPxK46wGeM60nOrOnuP6Cv9GZd7cPdwFH9kdO4q7t6TrBfXxvRhiZo5MyjW0UvXWnwTecfeFJQEOLKYe0JoHCy-oN__qzxAMRWFV7vUpBFIokrgPuE63Zc2dAkZnJU0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=QwIZHzw-5IspvUkRYH7fcb-2JvXwfz3tEIvQkmSq9ZcM_ygUk-hxkRgVCRMfoIXkCghRfrVNPi6abwOksc5k1iO3-u6YnB5Q8B-G2Q4R_5WMuzYSEF8PwIy9ttMTv0qnZZR5yskoRQW566hXE_hAKA76UQzlAheopGJutU8h_KVliRNLBr8HauGf_WwnKMqNToG-Punlh8eYEE16zV9LM9hik9_3OGwMFNwy8nrXKUf24TXfoB3p2WMG6if9tovu3MhHW1B0YoJv7cG0dY2DJN1wbDzGvFsUNyg09nGNAlSc-0yCJZGN5xFv-JEOMwRqabZRrKgFx5j9Wq2vpef8OLjTpNqlcmaQtzxVt7hKx1RcZs4aTVdp_idChiN8u0cIRxiUKnFt4dM0De4y-qwCwHziO1yH9p9VbaJ2-M2fGjdKn4u9YAbCQQC69PvBzRkydc3dXgRJ0rtZExQkRY6WPeol0msXTx1zj8EcTLmOJFcdaaM-sajydxIf0eIvLk-nbj3urTKbt5fVQ7DaEr6q7EgmEpLZtoLDFNggOyS3cjdiDPxK46wGeM60nOrOnuP6Cv9GZd7cPdwFH9kdO4q7t6TrBfXxvRhiZo5MyjW0UvXWnwTecfeFJQEOLKYe0JoHCy-oN__qzxAMRWFV7vUpBFIokrgPuE63Zc2dAkZnJU0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=MuKa3y1PnaCrDicFoCixn0-J_5QOw5_uludvf0X8xFJ0PL11Ke753YegmTyaQqZT0yYdMvKGkvqL0NsURCYVOvWiak_07Dr45x3hWZ_1fyR3YmB3sztjVLCbp9jsvB5DmxxDafs_cXXW8o7cfB9zGZ_d5T_9RaJPgB9-TEYl4jqrxxHf_tLYkEQg7iomhtE5bkktYtmLk_z_auFkY8wopVhTG_q2WADQKwKOtnxlN-dFAqlJu8kZ60aYR9uPC6Glpn91doOuzlQKyMNmJ_hczKUfH02WG6y1o_VfvC8WD9SwDLH3_NE6lt0n4bjtsMH56UqshyGzmShN6dU4KQb73w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=MuKa3y1PnaCrDicFoCixn0-J_5QOw5_uludvf0X8xFJ0PL11Ke753YegmTyaQqZT0yYdMvKGkvqL0NsURCYVOvWiak_07Dr45x3hWZ_1fyR3YmB3sztjVLCbp9jsvB5DmxxDafs_cXXW8o7cfB9zGZ_d5T_9RaJPgB9-TEYl4jqrxxHf_tLYkEQg7iomhtE5bkktYtmLk_z_auFkY8wopVhTG_q2WADQKwKOtnxlN-dFAqlJu8kZ60aYR9uPC6Glpn91doOuzlQKyMNmJ_hczKUfH02WG6y1o_VfvC8WD9SwDLH3_NE6lt0n4bjtsMH56UqshyGzmShN6dU4KQb73w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
