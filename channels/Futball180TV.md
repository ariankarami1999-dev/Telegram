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
<img src="https://cdn5.telesco.pe/file/PpQsdMp-cW7KjfsaJ0lPWHcJhECRgDQ9-uk8ulpl2eNhgByEqOVTHiFRDSxstdUiNSw-6AXQZ6CALjNlDYjVQLHbP07LlEoBnSkweytOOhCZu5r9DoW0VCtzIrgJHfKen-C28xTxbBMZFDDEtFaxfuTb0wkGfq-i0oEbf6hnEtbRA62RN732XhhT3ybdIrFXfvPzthclRxLA1dGEEZeSE-CvxmUmdp_Kw-6Xzgeh_UFz1N7s9p4sSsY-ZUXXct7bfcK1aU3JySFKdtK4JI7IIULPVJkoiNtC1Ct0WrTMLaC_QJ86uyNEdEaVp1d9iUSPp7OUblsyP4SDIycUnlcvHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 698K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 21:36:08</div>
<hr>

<div class="tg-post" id="msg-96417">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnaz5fC0BSo_bEZve7cFrDrTgqZqQf4eoyhhXWGUC8Wb9Z_KgU6mFlRZuPSiWRtlX2jcF0subMENAaiaFdH8rl9WzokRKbOsG--585LpQ2XIuOHOMwxyd-FopmVZ-tdUZ8r58kjjvCmrH-p3TqC4HpQayiLflGX70pfTr-56cJX4_-deMd9fqB17HECN132YnTJsfunGBObb1UdciBjKeylEQvlEx_is025Ag-kFebkpiRxLYXModPUWKWFs8mJkVxuYhquCyGyyJEtwXGO0_afrlPvmHwq9QASHnpN5q7D26WgwhGppFd6ZrcFCjPROXgcCEI6o3i1q6OdLFSD37A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه لگانس قراره برای یک مناسبت تاریخی یه بازی دوستانه برگزار کنه
و اینم جایزه برای بهترین بازیکن زمینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/Futball180TV/96417" target="_blank">📅 21:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96416">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c950377a2.mp4?token=c-singA9S9rDREjiBsQHqsRzLTqDA_mCFb9yR-QDLi7OhT40n9bJpqVFD0OLMa_rb-0ylNiH-7-sRzqo7mbAhPckZi5jW_RMesh4FvjpAvPgqJ1tVs6JjmyiZA9-fr9928WArFpX1SzVgkzkXmWLDdojzYVazrTmUdFXvXInZjn0ucDURS1c5uQd8XvuMcBJoWiBTo-7oqbLOR6geNHK8uKoCFFh_qPLZS6rwp5U7ofkKeWNHkeHxFfgIjg9dkLJwhXoKYojDMFR86lflB8pz9Hg70E6Q4B6vrnU9myD11f5CZOrWkHtTwZ10BcEErqYO9ocInKBcvWE_BTjNG1ZnXxL5sE3XxwVe2HuVNiwKX-ujAI3G7-p-79Vao67DukUgBzgsG3IfGHy94mN_u0lz3dGFmVFCdnS4EHJ4VbQ6bozlApBdj2YeuT7epEZalF5I4o3Lcskc7B423eeXdFTyCMu3bthjod43yX_VxcJlWi1l0eHYZSC9HX2dWcpb_eQ1zSZ2onVJWb55SA4vKa6NbGzi4A5dDM8fLM1L--DZL6NARCc57SjCpfJIDSJIULgSponvWdemTgp4SquScFU7Ub_cHYkbAY5UVZI9obsHYY6L_JEO70DhgtzewT8LsYUNxdLTCYQeNsimve3AWNuLR0QHLcyIkH8H-8eJr1SOCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c950377a2.mp4?token=c-singA9S9rDREjiBsQHqsRzLTqDA_mCFb9yR-QDLi7OhT40n9bJpqVFD0OLMa_rb-0ylNiH-7-sRzqo7mbAhPckZi5jW_RMesh4FvjpAvPgqJ1tVs6JjmyiZA9-fr9928WArFpX1SzVgkzkXmWLDdojzYVazrTmUdFXvXInZjn0ucDURS1c5uQd8XvuMcBJoWiBTo-7oqbLOR6geNHK8uKoCFFh_qPLZS6rwp5U7ofkKeWNHkeHxFfgIjg9dkLJwhXoKYojDMFR86lflB8pz9Hg70E6Q4B6vrnU9myD11f5CZOrWkHtTwZ10BcEErqYO9ocInKBcvWE_BTjNG1ZnXxL5sE3XxwVe2HuVNiwKX-ujAI3G7-p-79Vao67DukUgBzgsG3IfGHy94mN_u0lz3dGFmVFCdnS4EHJ4VbQ6bozlApBdj2YeuT7epEZalF5I4o3Lcskc7B423eeXdFTyCMu3bthjod43yX_VxcJlWi1l0eHYZSC9HX2dWcpb_eQ1zSZ2onVJWb55SA4vKa6NbGzi4A5dDM8fLM1L--DZL6NARCc57SjCpfJIDSJIULgSponvWdemTgp4SquScFU7Ub_cHYkbAY5UVZI9obsHYY6L_JEO70DhgtzewT8LsYUNxdLTCYQeNsimve3AWNuLR0QHLcyIkH8H-8eJr1SOCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
😁
😁
😁
شادی اعضای تیم‌منتخب ایران بعد از گل مردود شجاع خلیل‌زاده از این نما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/96416" target="_blank">📅 21:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96415">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyE4Gm4X_WC5nkfZv6P_4Gjd-cgQGDBkkupnIJVNhDwrOIVOSCJzGlNptUOS4hgOi7YjWabNteHnRwDuS3NY9577P3UK0XiqhYu1xEI4qVyGFaisDkxQKJrgtEXnyKeC3Q3SKmCxrkF82p-E_D4-fG5nkVmMIee_fj6j9wo8nAdcHDTa-UYrumnK5o5C15MwmKwBgaG8vm5JS5JBdDq75JEx2OxasAm8sEA7yiVWs13_-3gvCkUl9L-D5pZOO9KKov3uDgssG1zb8KZVCpHnNA6qSCppojS07McOwqAZBzJmxE8JisgrfxGv6EY71jfxcHcDJPpDtvMp_eFGdAQnXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇦🇷
این می‌تواند یک مسیر ممکن برای تیم ملی آرژانتین در جام جهانی ۲۰۲۶ باشد:
مرحله یک‌شانزدهم: کیپ ورد
🇨🇻
مرحله یک‌هشتم: استرالیا
🇦🇺
مرحله یک‌چهارم: کلمبیا
🇨🇴
نیمه نهایی: برزیل/انگلستان
🇧🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فینال: اسپانیا/فرانسه
🇫🇷
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/96415" target="_blank">📅 21:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96414">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eh0H2Z6V_Uyj7DjFzYe6cXgPtVeYCK3x-uu13RqgXeD2PV4qxx05izi7XfH8SaulS6OnZMWKyNL_gNS9AZLIMjSFXiFYyKnWQr54E8CbIG_3QGvl8-puAwMF81bIW5nBUr2cglpc4L9L57UFeB7ZfSLj8UNq3jFXTOOV1c9FusGiCHwnvn8gmZnQtPB8aSuX17W8j8bXCxUtA4Ye9-eC6G76WY-ki5gEUmrTMSdZ3ij3Jb3oY34Zq9VEIa5uDC52xMpz1hB0S-gxK_Bf8lTAw4gocgfp4pZkKofhgYw3ffJx_VjgYJndpNKjBMjA5mNnjoKu2PMFDlp2chZY_sEQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🆚
🇵🇦
🗓️
۷ تیر
⏰
۰۰:۳۰
انگلستان
🆚
پاناما
📌
صدرنشین در مسیر صعود یا تلاش تیم حذف‌شده برای پایان آبرومند؟
؛
جایی که یک مدعی جدی گروه برای تثبیت جایگاه خود وارد میدان می‌شود و تیمی دیگر آخرین بازی‌های خود را بدون فشار صعود برگزار می‌کند.
⚽
🔥
انگلستان، با ۴ امتیاز و قرار گرفتن در صدر جدول، حالا تنها یک پیروزی تا قطعی کردن صعود و تثبیت صدرنشینی فاصله دارد و به نظر می‌رسد با توجه به شرایط، کار دشواری در پیش نداشته باشد
در مقابل پاناما، که در قعر جدول قرار دارد و عملاً از رقابت برای صعود کنار رفته، برای حفظ اعتبار و ارائه یک نمایش متفاوت در آخرین دیدارهای خود به میدان می‌آید.
🚀
⚡️
آیا انگلستان به راحتی صدرنشین می‌شود؟
یا پاناما می‌تواند در آخرین فرصت خود غافلگیری ایجاد کند؟
👀
🏆
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/Futball180TV/96414" target="_blank">📅 21:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96405">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p2riMlaYoLDCEVpg1ufoNPZmeAnic_7UK34HNrOIDJ4_Pk4Qzuw0Zn19bajWD_ate6c8nNEOYc-rwLyZDq5XM34Qrqc4wVxUMIbw4iltsjFxZDdKYdHkZCq1PlYTpKWjzi9zXnqrfZ6ajo9jtTygRyIy3gONmkdmEn4W0lvSj6g6QzYwEwafbnbCm_oTMjcGgCbk6KS9Od_62ZJBzptN_a0xMUi_kF2GHJrDd1_aTP_SVjMQrvbbd65y95ZvBHmmZBO_ux23iT-tuoDH_uDpLrlR6NvAPVhLF5rjfBKzlVfjHtC8P50D_pOwJWZ0B0b2KKux7r1pcAYsqTQ_GORE2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/inJfT33graFvOTkqouuSJi6-Gtp8T-cAhxsapFmk05WpiAnuHEmzOV7U9cWm_1_KNHiTBAPqoTBfbOYUpMp9iI2LoQQ80Qdk1lmEedktpyTIardp0GfpHq_1elgTM4LkvMqDaE3-VkMDqzyeXFkOz98XOKcfIceHHramamD-UIlNpRPD9gI7AFkHcc8g03QxYwCaB6iKUrAuh07DbYy8TNRntWXfAcZNjpmjQkgixkDNUmiZvn9i6YIA-uuBBu97dDc787vdK7NTBTSX8cbBvB87lwXnh6d8V99qby1Pbw8855uyvRahNhVQBlOXxSi-TAwp5lV0EqA6CvtAioetXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YU-QpIZQBIBJtO3iXFZ4HhSpXWvX_2SIqTdvg-mnxQjyVslHXLUBnZaecZGDQ-EbW3WITdg_3-gLX7Ko5RHf9xGHfEszKCSomzoHehWRfb-cHThmspV0CKSvXin8NqHNTStjEP9l3HyHTC-Sr9Yt0ljiPaNRtHiWG8byrbVlx39P8v3t8B2Wt1F_nhu0mM4aoOZpTI9sgPdL5q7DmEjFORRLOSRbgBT_mz0r6qYPXx4gvzc6HqGeXJW4mBx9Mfh9S4mzCCVr0yN3tq4_zOImSXnMPkkPwlXYJDOzbKjXINIKsMA0L3KAGXNAUtwkQ_6vXUYSvYLg9024NhDL-R1r9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SIg_ZGBCO7Qt5keaQp72HQ0z8m7nUrkB1wKXTu2IpM6Q9xeww43199WE4WSMffIAr2YS7WzznrDj7LwRbx2tVgh80wid1PMXPNjP-sttJo3erk-XHQGN58Pyp0BJhiVuFbUuSE39nQVrnYgfSZA-CQ70J3owpEewqCeFf-Xiu4J7UMKMGsPFDOUCvm72n0jUoax3QDHYE3vQfufdv-iwlWHRkahQrSqausnsu5LhPsaAAL1svcf7QDobPRdnXjUk5w0ciZ0_Zxu_T5sUMCDcPN8oBYZmX4ELOdYzn7tmpp6fcKzMRjcUOLmgdsD6zlvgSt8nmnqwy0pxMuav0GcQ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uJWnmLH3wymLjIlbBlpfNy9woN4GSDE3ZiWAg4t-kf4a1g6edDahjKMPdE0K75V0Epc7tQ2tpQ_pcJhPQZ7bBkjtubqwfNK-PWG26rAORF3El4UHU2Rh5ePzAvjDd5w2sFvXO5CThcFnSglWcSjdYZBmN5MFjlO8VQN3hNpV-JI7Gmhdc4g6AenPf5c4cY5dTQFbfC-1CMPYMJLugpv2X2z6_nZVnj6NAj3T_-F_uvLPzCpflLDjlHesltKBHJcA_YZN2Q5A6UXtceyOOnP3yI400omv-Tc2AI9pYMPzxwfs4wHT-BlNakMu4Nwx4osH7P_1fkbovWqSqTBPsh3Cgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2CqwSiLbTG62rj9OCieahTpuQgpHSsj9tjMJcbvpeUxAh_sS5a_btcSLEycqAjdviQ4UAmFNzwUtAQ-8YfTybUXSoRbLlq7R2IQEwtIMPKpBYpyMXaIvfw1Vke1mVxGW4hANObAc9o5fpDoH3ZpM-QtsLbyJNRnl8H4WekN-DfwnuZB86dKMjECDu-TkRmkwkRmi2KeI_N4GPpxfrWoCsPDU6N6IEYMe7uPGgAAgM3rdivtup7Q0D2oR3GE7ev0OqxTi8TyNBSpdCUSSlt9T0ou1HzTgKZydz_1iasSs0AfFhNK7jGqxv2g9iCdFtjXJGayt_1gWg7v_SMqdi_sxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dLmmUQaCL6o7IJdZ7r4IX3m7SanWS5s1mBgPJcds-fIxilrPqSbGkDkmjFolsPSDhguS-MpL9pki9gotGAHti4VOiVE3dHteNYn2yP9xY7a7xGxYb0CZj6atUZCh0VCTSc2api0YaNQ8UUzR-FXcMtixMnk7nMyogruE1Xp0P47ZURmLyzSohEQGBbPNy9YhedckAAO1dgQg-0UZgDEWD5lAVtY-Is1cR-txUnhyvaAzApcN-6cmJ8yTl9qviZMLoi8u_bqZmeWI6svUDvoObzKwxhIWxst9nQjz_zDR8oeTo_rBCHe3XyvPUyZo1pRY7Ton5AOlESbt8FDBTsQcYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tTaughOxWbYybskY2U5qJlviyX6lVgz-Gyf-H9N2w6GtX8fJ4V_48SPqrLf1mo5RJZr9XdV_-iuZWZ0uLFnRVeq6bYaYwxc1E04-iZpeEZuK0bCkVYYbrdCTgq2cVd1l00McZ6_D7DafAqbulMS4a8tmun6O5bap6rvm2RV5pAMQs8YwNMfk0iwA_ysvFJtsGKGqE-ZiQsgiH4UXV842MOQkPrfGvLBhZlbFYccrbYMbufjq7PvzZ8AO6Qou11qcARPAzb0qjkqcRqRVEbh7B8VLd2UWee7ZbvIc48nmpxwxdjc5inwUVPgKvW6awo4LXTk3eZu6WSqcsV9k6ssacQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CiMZuvMiZ2sTSz6GIq5wa_IinrfPfXOHBv1-4Y4sZyT2JRbCBhKuCvXVoDIqkROJ1BHH8n6PvgEn1w4PDhuTjg_ZA9_PvU8kJq7V13dDI_NSuBBpkb1E68wWx_uAiptIcc3ggdCQlppjAz7o0y7K-gni950N_JE9NtrQ_woJ4scFpcoeVX5368Xl_SNHl6-4TwAWUtYb8ZPrdXj5WrH41eOdknwDkdAXro2AvZ5mpIo6becv6HIX4cJvRhe0quaSwwBHTzr8mXY-XAs0_q6pibgzpaq3QvpXr-oCI9xF0mdL0cGdHzy5190DaphQQQ0q5L7GQHu_qwN3SdnIv1GpNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
💥
🏆
فیفا با انتشار تصاویری نوشت: زنان ایرانی واقعا زیبا و جذاب هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/Futball180TV/96405" target="_blank">📅 21:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96404">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWdY0M2vM1cyv8tiNsd8kz3V72CDQVLoBwTftQqEPHg_QEpBpE0lvqY0PlfTsng_U83XGavfllqUpTgxL-DLulQRPqOKJcLzJrJpextocYrTWPt6INpqmbT-PyS0tYenn7Y4es8ckEjkK4HiwBT2kvDmpmBTHthUE_9mqsU7MI3CP7AjKy1fpwiLJQhoQJS49thOleYE9XtqbSXSmUeNRJVaBSDVjnXAUVYl7G1Z665fsGrlId6rSplKEbi99ybTbHpWdCDFfjcMioQ7KUtHgNgprR0AbvV2gGK_TzdmDoaotzufrYwz9CTKYWs-nmwCMem1wDXxpUQkhLydbhKTjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
بازی اتریش و الجزایر هم جالبه...
الجزایر میاد نبازه چون حذفه از اون طرف الجزایر میاد که نبره چون میخوره به اسپانیا
اتریش میاد که نبازه چون حذف میشه
مساوی و برد اتریش هم مساویه با برخورد به اسپانیا...
خیلی شرایط دارکیه خلاصه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/96404" target="_blank">📅 21:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96403">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90c1abba44.mp4?token=sW2r_RJDMqAtNBbXicSgGm2Jjwken5Zk5Ez17mYr2p38MsksUsV1MzlxCIRXtWps69yIbYwWBmuN-XLrLAOJdTZR3U5F12qQuxLfxrf4S_sk_kXaLQu-VMHjPXNoWiceR4knWCipavp7j7IeRi5np7HIUDlEc28iza_4IZOKZcCNq9HlGqJ9GfRUXfKj6PJKrV6atcIXb8jNeRD2RAWccQnzD8m9RIKhqoy02_V6aatzfBtFz2I0k2Grf0M8SUrSP4q_jJ2S4ExsiOi2OYjycqZZzjUG-qT7FZovVBB7hqkz3qiza78WiOVUy6xGkMA1d5Awt5xzhBELpL2Ik-mWeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90c1abba44.mp4?token=sW2r_RJDMqAtNBbXicSgGm2Jjwken5Zk5Ez17mYr2p38MsksUsV1MzlxCIRXtWps69yIbYwWBmuN-XLrLAOJdTZR3U5F12qQuxLfxrf4S_sk_kXaLQu-VMHjPXNoWiceR4knWCipavp7j7IeRi5np7HIUDlEc28iza_4IZOKZcCNq9HlGqJ9GfRUXfKj6PJKrV6atcIXb8jNeRD2RAWccQnzD8m9RIKhqoy02_V6aatzfBtFz2I0k2Grf0M8SUrSP4q_jJ2S4ExsiOi2OYjycqZZzjUG-qT7FZovVBB7hqkz3qiza78WiOVUy6xGkMA1d5Awt5xzhBELpL2Ik-mWeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇪🇬
مردم مظلوم و ستم‌دیده غزه با پرچم مصر به تماشای بازی با منتخب ایران نشستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/96403" target="_blank">📅 20:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96402">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jU7Tb5wic2wnmc2SL3ZPq-NJafuBC16Y1rh0HAl15hip5M07hwqqeou7LfreOqClVCrRr81lS6dMh2bOtTyFIoNbGC4ewku2x_TSBvpYITGudvZEdSfoLG8quLPaca5fLdOqkufoPKvWbw5zmvNlDh3TPy4HHfxMdPLMDCqx5a14nARMwkFldc67kjbxt8VZjbSmT4o4aGpfKnxU-R8jOwRDKYbMbZ0deKqor4lOmD68LYYhG3QVqzubo-hxgoTVn2dEJ_jPqUFSChpk6v7qDXQw7bB1N-3uwOh3AT1l7Pes-ntIKE8lKnw8q4eQM6HyT1DYSn9s3j_Ll0UHc2jSfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇧🇷
🇯🇵
ماریانی‌ایتالیایی داور بازی برزیل و ژاپن در مرحله حذفی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/96402" target="_blank">📅 20:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96401">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCz22QS5NR-eoBGxCNxdf8qAhGzIsVDFjqvKYUHckDi5cy70kdfhFOdvItVsjXXggxe2jItBvmVplGR5ccZY52qA50ihJfqeQsGIDftaG7bAL7WBg3AMUDbTSHOmiLt_FpWxcWsdsHZLcFZ8em6UwmF65qreN0CHhTt50ru5Qan_7I9RiAxOf1YZuzxLWNrZuWPiGnsUbXBK-pl4GGk3hJKWqQ1A5RVE-i1ztPgjd7h6HjJy9RychkbaRQ1bS9cMiEbN4fNFE6jdRpuAJ8mRJGXwCdX-yFm9m7UMezZRCL64nA0y6W8te8LjqAuTGXsAXQFYsUc9mlWwKAalw7mROQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پشمامممممم
یه زن و شوهر تو قرچک که شش ماه پیش ازدواج کردن سر طرفداری از تیم فوتبال ایران از هم جدا شدن
‼️
🔺
زن طرفدار تیم فوتبال ایران بوده و به دلیل اینکه شوهرش همیشه موقع پخش بازیا آرزوی باخت تیم ملی رو داشته با هم درگیر میشن و آخرشم از هم دیگه طلاق میگیرن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/96401" target="_blank">📅 20:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96400">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0tlvPVA861jOYsB_swqXZIrmnT5k0Z210QYHi7b4zi85ANWjHMjG4SjBlZ1guSQRi9u9cewQDwxyMpCZ8d-h_UP34HjVyo3frqfroa5w_gMFkv4qUlG_wyyMPz7DABROUX1o1YQhwIQEKd3m3PKmcKc-q-yOoJ515IYoeIqMePJS-ayWQmeF_x2NS_xNYE8EF7xzIoLulkenjXJ7x5gCA-QP10M-Kbmb0EF3x7EVdkZ9D4Rq2se2jDr-0oka_01FrfV48JVkvJzH3-tAtT2W8u7wQKyvCd5fjMnilIJYNcJ9yVHlx6lfv43u-yaPegDDwlTh1at6JsCczZrbl3ohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🎙
🇯🇵
شیوکای‌بازیکن تیم‌ملی ژاپن
: درباره تقابل با برزیل باید بگویم که در دهه اخیر تیم مطرحی نبودند و دلیلی برای ترس از آنها وجود دارد. بنظرم فرانسه و آرژانتین بهترین هستند و ما از سایر تیم‌های دنیا چیزی کم نداریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/96400" target="_blank">📅 20:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96399">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-CzKdWvyKznyiIsOhx3a7zvQTbiOpGLEx2xzU4AZr1jvbiCAhAbi5Fc2C8oojPrVlzvBo3ifWXrH3-IQo4zlH2WPbOBE2dLQl0HhnHdiodOEw8XdNiDlFtBR8fK4fStTodjPZ691Dw_Z3nkoYWmcgUBGmUwkaTmYmfN0mUS9tBV5xhuhZQXMKqlmiuiC2u-50rpAaGnDiwSfv5aXvNQKI0IHOdlrDjX7sVgdWj7rJBu0rhZVwjH6-Blsx8Zbt61LSOFl5nSl746t0tsdQlHhdCysBMaS2JaLF6Rygfgjlt8YrN4ChZWvw1Djps0buU8YXtEFXzuZdjPWlsH4LIBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت بده مورینیو
حقیقت رو بگو سیمئونه
اعتراف کن آرتتا
آیا او بهترین حرامبال نیست؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/96399" target="_blank">📅 20:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96396">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DmupZgQ2GPc2ZlTRfwFlpFcTuO7By1J-Ntl7aXyzT9MJHe9jyWhjO0NE7Yi-qSsRES78TEk14vXv--z22QIEerFRj-4RaB8b62qJcsDRT_faEjDj5owjo8wI9VLWctGgYxFjFHpFOq4Y4Lxo14sHamnqNatx7JQ-YY2JFCWQmjUiU8COagl-CYYvtLEfFOyBYFNgh4-0Qj1i920RQEaR9uk7vrOBVPrmQIpixfWShKdWGYvnNYdJm8KQW-rrBU18LBeTaU-WeLIiuaFGW8mXvXryTJRapweMQJ-ZWJPSD4wwh5cZBOw6-fc4Z_TdKObyDKChbh9D9likksVfNokp2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GLCNtaq8MEbvTGTx0tvk0Q4_lPNJkK_UKYciXkyhpwtrN_W5_xhfZ9PuQu0kXHzTQKTgPJpyQl6s1VT4n4T8Xrt5I8kr9HMEJNqlv33HgZbAqEgFLQd7gdjwGfsoxwncueF0wcgYqcDCum5vmyYvyHVkG-yCpLmQVJ6IhDFfMW_zfB9hWXTaTSHWYQ1BRA1Nzz2rXWdlz9k9JHfEgf0nZu-ZIjopF8LhvywbLXghJFjfESXn0KKqdygfqFwA5eyjOmdoor9gj5cj2fe244hbNDgk0Fc145Npcl0y4MyjQl95ozF8zW9jp1osARoHMArnAH7i-deF3vqYhMA3F1S87w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ioqnJiLRvw8cwHUuDOz9_yn6Ppcjis0O-J1F8B2xeBSoo-elBis87k5EQNwYDBXzasAP3-zhjIBpBt3b7D_t7DXkmfkaMkMyhTVVb3miWzEWEpeEPlEF5GeJ9bJQUwIamVwujD3HJMePQi-2723302B5Cy0iTwNaWz80oko4ANK0WmrpKoBdR3zY6D2xw0zzA5dyCHrHkFNaShs0z6L6bkoI543lL1cuY5A2jkBJBmwjOchYOo1SQ4MxNkbBf1gB8BNb_AJC9jCrOqS2zVnX_CfjSDtnfURQoiZIw-YSWvme6WUkbPg99zA4jS9ObB6CaYS8UGcEiMwTuQq58BxNfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
🇨🇴
کلمبیا سابقه بدی در بازی جوانمردانه مقابل برخی از بزرگ‌ترین ستاره‌های این نسل دارد:
🚑
🇧🇷
نیمار در مقابل کلمبیا در جام جهانی ۲۰۱۴ دچار مصدومیت شد.
🚑
🤩
لیونل مسی در مقابل کلمبیا در کوپا آمریکا ۲۰۲۴ مصدوم شد.
🇵🇹
- امشب... قرار ملاقات با کریستیانو رونالدو
⌛️
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/96396" target="_blank">📅 20:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96395">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaVTgcdeYihiFSRPhAu0f_QWOllNLxoTTpuaffvwDKMydPT-TcEcFCVFC5-bXC01sr6d1h7npPdsy7p8lqMO894UD9f4y44BSI9o7FMH5eCJJHUnotqylob9LzDYgfyI6mwUjA8bmIjE3ZfbeDFQIZDc7jOIX7L7meoqoUIpVrtSuZUC3CqH_1-41sJ41t5jOqY3p6Ni5dVUmgtK9Ws8RkLWQszG7e0GkI52iQvRXbAFrg3hqVXyEB-_cL4LON09SHwDbhiGr96YVtQcJERFGDhPM6Akb88kHVoHCOlZgUAmokrJPEGKzzusJYZT8Nx39fp84_VloLyW52r9w1a7mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووری
؛ فلوریان پلتنبرگ: چلسی با ساندرلند برای جذب گرانیت‌ژاکا‌به توافق رسید. ارزش این انتقال حدود ۳۰ میلیون یورو خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/96395" target="_blank">📅 20:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96394">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c7a6696a.mp4?token=rwXonryIWz3sIphycdXKw5agXC7GpbNOIJTXThsCaadoisUavkt3PUto_WjTHM3ylgXIgCZi7JvJz8wWQpU_eY0ycQrPOK7ahlTF8fsBFpaXtelholZ8b3XmJkH3FL4mvYffgv17mNOxVaJ2KMZkYxp85FnOOm2cWeunHV4GYbv8X3JaIMuO-Vhr_jYszno0t4gvXqKh_ISZn4LEmIvkjCt45cLFzPO6v11weTagA-uY3IvfU6PAQC9pyvxJZCE35jjPrcNoGgzctT6shp_m_oL6sxM0Nd1-3yaZ2LLFEOGssWlzxf4YK9ya-rYQbSuhWi1h2SXI1W1Yxb6J28XzhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c7a6696a.mp4?token=rwXonryIWz3sIphycdXKw5agXC7GpbNOIJTXThsCaadoisUavkt3PUto_WjTHM3ylgXIgCZi7JvJz8wWQpU_eY0ycQrPOK7ahlTF8fsBFpaXtelholZ8b3XmJkH3FL4mvYffgv17mNOxVaJ2KMZkYxp85FnOOm2cWeunHV4GYbv8X3JaIMuO-Vhr_jYszno0t4gvXqKh_ISZn4LEmIvkjCt45cLFzPO6v11weTagA-uY3IvfU6PAQC9pyvxJZCE35jjPrcNoGgzctT6shp_m_oL6sxM0Nd1-3yaZ2LLFEOGssWlzxf4YK9ya-rYQbSuhWi1h2SXI1W1Yxb6J28XzhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فحاشی‌ هواداران داخل ورزشگاه به کنعانی‌زادگان موقع گرم‌کردن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/96394" target="_blank">📅 20:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96393">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwjgT4mszYiHSHhpP680dM3Td5gqb9oLS65CdHhfRfhnKXwibP9Ssv6wU772Sn_q6zX4zsJb-VZAflXIgpp_FLnQwmmtR0HJiItgKBmIyIjZB3lWaT0J0zpcFNKjY88Af7yABfGseYm_r5mCDRWVOA-ISpqW44LVUkJ-R6-cua_wzEqeWzmLkzE5-ssgQ4wFaKkCd3ZFCGGVjEqyaxcEHJDlk7wz62hMYtuFAEf9WFALkIWFgAr4cic3L-q6czX3hL_MaMM01FfIJQRkW5pfMfCzJuYhDUF87YEox9dLa6TJPhQF_T6oCBQGYuE1VM_9X8RlWcbmOYExsVSkPLIuww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💔
نوزاد کودی گاکپو ستاره تیم‌ملی هلند و لیورپول امروز بدلیل بیماری درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/96393" target="_blank">📅 19:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96392">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad3a9c910.mp4?token=OElBu9lxTJ8MjrRLV4-mdg0UtHGiA9x246dMmBaVnMJzw7A-lWbsvm0AXjpwQVwBVwXCqZ-xFEekI1kPLMCpeZ6siMeytLHdPNDEXOSeOvl8uUQC2sr7GOTubAj5VziLt9UJLSSSrHk-1LEtiXVgR6zbnl5ViDJCl6CpPz1_EbgQnEvObtNnOP0KYKnzA9NShnkhjZyf5maqtzXJhY6clxfpXflcT9KOanVwQk1BJULRls6HyfgE6CED_4vc-vMfMNxTzkmne5CLBDlLFMmyjRzFOkalTxLQbD4Bsa5_kSquCo3SjG5N_FrgiOkPJFVVsu5tZylEtSlvO-mkDJKNjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad3a9c910.mp4?token=OElBu9lxTJ8MjrRLV4-mdg0UtHGiA9x246dMmBaVnMJzw7A-lWbsvm0AXjpwQVwBVwXCqZ-xFEekI1kPLMCpeZ6siMeytLHdPNDEXOSeOvl8uUQC2sr7GOTubAj5VziLt9UJLSSSrHk-1LEtiXVgR6zbnl5ViDJCl6CpPz1_EbgQnEvObtNnOP0KYKnzA9NShnkhjZyf5maqtzXJhY6clxfpXflcT9KOanVwQk1BJULRls6HyfgE6CED_4vc-vMfMNxTzkmne5CLBDlLFMmyjRzFOkalTxLQbD4Bsa5_kSquCo3SjG5N_FrgiOkPJFVVsu5tZylEtSlvO-mkDJKNjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
انتقاد تند شریفی‌مقدم مجری صداوسیما از امیر قلعه‌نویی سرمربی تیم‌منتخب ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/96392" target="_blank">📅 19:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96391">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7Clvc2jety22C5s9FtA6oyKlnB8oNXTbzlMTeOYIZv_QtcH1mIiNtCUG2lEiRiWyKZTIUahbWKew4aQr2UWszf2tC9osCZgYn7z_ufqmc-rSVFnnqmJM8WYOenrDGwdC54-Cnx0N6bpP-mHoP4JIBluNH5mq0Nok2ooIkohFIJUnYxh5lSjWZDKizGC5DOd3l_X3zXazQW2dHhhr1gUSpoXrzizstocPGbCRhhZBbL6CA_OpopOlhBHSNbnaG8TQDrujkblQDwQ301nsGRS-MDF3xQCqcILesIYicDWJG8TiYMTBVodH3L-feq8FtxwMCquyX1RAeULzCV7NEy_Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عثمان دمبله در ۱۹ بازی اولش برای فرانسه در تورنمنت‌های بین‌المللی نتونست گلزنی کنه.
🔺
این درحالیه که دمبله در جام جهانی ۲۰۲۶ در تنها ۳ بازی، ۴ گل به ثمر رسونده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/96391" target="_blank">📅 19:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96390">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcc5deaca3.mp4?token=LV-MNBQ_pveE_HBR6FjOE0mXX3sp8I4y7n1Z_Vk0MV78ReC6wbNOtZnEKVx5EeiNInbfdJd1AdryKX_FJlZxIiUPOFAxM0HwglFqZM3i9kMNa7JaBZMuRMi-sepk09Rvl3l3NRg64SUdhL0TDv8YTVmGgDb7XA93oBjOrRtgHIraW0eNTOHMaI-7sD8yJcys7IBaT8R8SK3esVbiuNKsK3y1H_vQ-rTcHVXoCAVJdPOsNZI1MZDKjd6j4HDY5zmD8NOyXrbN_6jcEqDIy9vyqzu68HPxCSf_NkAuWRYrKI5fM2e78FSgaaDWAdJOuTvLytI8S2VAyL0J043DFG4bxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcc5deaca3.mp4?token=LV-MNBQ_pveE_HBR6FjOE0mXX3sp8I4y7n1Z_Vk0MV78ReC6wbNOtZnEKVx5EeiNInbfdJd1AdryKX_FJlZxIiUPOFAxM0HwglFqZM3i9kMNa7JaBZMuRMi-sepk09Rvl3l3NRg64SUdhL0TDv8YTVmGgDb7XA93oBjOrRtgHIraW0eNTOHMaI-7sD8yJcys7IBaT8R8SK3esVbiuNKsK3y1H_vQ-rTcHVXoCAVJdPOsNZI1MZDKjd6j4HDY5zmD8NOyXrbN_6jcEqDIy9vyqzu68HPxCSf_NkAuWRYrKI5fM2e78FSgaaDWAdJOuTvLytI8S2VAyL0J043DFG4bxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرمربی مصر از لحظه گل شجاع خلیل زاده تا آفساید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/96390" target="_blank">📅 19:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96389">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96389" target="_blank">📅 19:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96388">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IYEUolvJdejmDUIMpx3FK0vt13rTAFdz2qElY3LtPVtfDpTfAyi7W7vzcZA55rYHlShGUOJXvhpHADI2r2OcH2Gmqt4QuKynooSNV_JHBwdMHarqz7AF5gzN9Z6hz5uHLwuBryN9NCSq1grKDSvlr8IKfW0mGQNVPsWguZNa3LTBuvd_oZnPMDXVok1DcqWsnip2lpVT6kURBAU7msc82XApnBzt-PtXR4Dhf9Kv-1aPVMcpPZNLFDucMBy1mRkCjUrcKZkW3eXQ-U7Jg4DpBJaaHJLxdgWxA5k8RlKPSSBfPaFaSL1FFOEg05K1qEYv4auLgjkZK5kG9G7iUGYCJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/96388" target="_blank">📅 19:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96387">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0acf3e8fc9.mp4?token=Vi_iD45RtxMR_Qv6BrO3UuuvfWgCiRZJo3HpqT4kZdBOkVd9Yxym1IhSb_rUskgrdSecn3E2rJk_w54rCDV1r2iJlRildQYjS0JwcRqyiAPey1029tegdvwmy4XjscFtiCZ4qdinZjR-w1vH8hyjI7dOixpsv_Jx_wlovoJtmP7gIt6o2ej4c9-yE0C5-TKamxTQh_wVgkdCn8k5Ssx7REHOGv79QN3lQTqNne36lDyHXqGa6wGpW-s7GCI-HDl1h63Lojrye8DnfGzl4lKNZy7dCh4qPZA6akT1YrWI-NHArOQo0iERpLLSq5mAg5pOYYBXM9GD8zm_jkDLfgnl8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0acf3e8fc9.mp4?token=Vi_iD45RtxMR_Qv6BrO3UuuvfWgCiRZJo3HpqT4kZdBOkVd9Yxym1IhSb_rUskgrdSecn3E2rJk_w54rCDV1r2iJlRildQYjS0JwcRqyiAPey1029tegdvwmy4XjscFtiCZ4qdinZjR-w1vH8hyjI7dOixpsv_Jx_wlovoJtmP7gIt6o2ej4c9-yE0C5-TKamxTQh_wVgkdCn8k5Ssx7REHOGv79QN3lQTqNne36lDyHXqGa6wGpW-s7GCI-HDl1h63Lojrye8DnfGzl4lKNZy7dCh4qPZA6akT1YrWI-NHArOQo0iERpLLSq5mAg5pOYYBXM9GD8zm_jkDLfgnl8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چی میگذره کلیپای بیشتری رو میشه؛ وسط خوشحالی بعد گل شجاع خلیل‌زاده اون وسط یه دماغم باخت دادن
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/96387" target="_blank">📅 19:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96386">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53c9100fbd.mp4?token=e4WuhNiq1xCFe-0QHR7mC9gJwfRwVZiD3aChd1jigC0gnC8U2K1M99fVudMY3tkzEUyTUEAWV8OJx3j6Gq5nA3R_Ih49E1K2ei40GVRlOW7XhCobXcPdZhUgxyKcYGeSOQpstGVqi0FyieJblvATVSg0HEHzlIk8WeunxF2K3NBiU9yTwSGqUd7ipjIU6qkscMd-CluMT_IAYFZNMt2-v6Us_mmS9PA2p9-8SPE2VN-HlOtGL-hyN107spH7DS8ayFU0wi6FE4ihRc704x4eMoqrUgllBgGjET-WfeMgROlNSX3JtGiHsnjDNUnNwVYIcesZATwk98RF5NMyCEvIww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53c9100fbd.mp4?token=e4WuhNiq1xCFe-0QHR7mC9gJwfRwVZiD3aChd1jigC0gnC8U2K1M99fVudMY3tkzEUyTUEAWV8OJx3j6Gq5nA3R_Ih49E1K2ei40GVRlOW7XhCobXcPdZhUgxyKcYGeSOQpstGVqi0FyieJblvATVSg0HEHzlIk8WeunxF2K3NBiU9yTwSGqUd7ipjIU6qkscMd-CluMT_IAYFZNMt2-v6Us_mmS9PA2p9-8SPE2VN-HlOtGL-hyN107spH7DS8ayFU0wi6FE4ihRc704x4eMoqrUgllBgGjET-WfeMgROlNSX3JtGiHsnjDNUnNwVYIcesZATwk98RF5NMyCEvIww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
جلالی: سر حرفم هستم و قلعه‌نویی از مورینیو بهتره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/96386" target="_blank">📅 19:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96385">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCuN_eil9WDgGbUqprblUqxDWVINIvYdu3SX0bbSojNztecAjtd7fRanzuatD89h0Aj55qo9JvMLPycOJ30442W_p8dgJaPVm70CtLBn4d2sFV520NbCMUrc8KxDxCNqjr9tT1gr7J6pYSXn9LD8ylWNp1DE3ofh5Pd1uSDrBfDwwSsev_sVnpodqiwzlRZUKcA9li-Wyu0rmIVSaBlDU5gCrfLgeaw1_uR3mS0BMQEyo8ska4osCuql8Dax-05X5KX4QbWNaQ9qEl6ADQzLBY5uSl6IuGamzKSyrWIkN3dQy-qe4HMwAEfsrhPLoVI81Gek4haTCLBVAk64u5KGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مربی های با بیشترین برد در تاریخ جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/96385" target="_blank">📅 18:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96384">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quXhV6E4CzkH_rBUDTUmMK5NKv6xtoL8UyJRC07ysr2V0QCziVjpPx79TQAc9_XdKXdSBR0WyYFA3XkKGafLnLDjjMmP-gL6SD2tFdA2jLHOcJS2OtV1u0bKT-jCDGxhH_zuB69TrswN7VVC3GmgKSQR56G3_TMuHMy0-Eo42PDm7c6QRNxEOGCseou2QCIJLNngEKlLB95ZgAUTbvAtOpSAmQWVj8recses5OS7_bMDYzB9HlMOAfxreE4izkh0U7XTjf3umjK_dVjxasdi-meIulCZY99B_FmfvavgImxGHa5mJdPTPBYgz8GlBK8fG81geu_AhTsHqYO7HJnrWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
کفش‌طلایی کریس‌رونالدو در تمرینات پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/96384" target="_blank">📅 18:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96383">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IymxLAZjEPh5_UnSdV_DEK57mxgJiYfX_0xJL1f5I1_uT2Fz5dwWtVscSe3M89rK6VKnY5zTf6gkqUx3eKw00mmV5nzzFBvUHjvvYi99h2ZmDIJnaql3GTTqf5W4gnbVyegaGefBoQ7f6axBBmKaiPckenr__OhRzXJVCKrbxeNSM-1cXMDqUHzZf_dqWtJKUppSwNzWy-wofjvJwm7dr7R_d6rRSphCMPDPKSEVh3wcEdEv1yhqILsdrSIGfK5QwJSx_fshKWQrH4W45xv9vaUlFj2aAW7quSN_VXlAsyidvVzPem7hX0q4D74PKtewojK36UT-Y-xQgXgJeFVjVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانواده مسی از سال 2022 تا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/96383" target="_blank">📅 17:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96382">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9jsd_zLWi9RSIV1aV7brXucob8g5lfh2XeXQaehkLZnhp21wuDpHcEKStgMPbBUhmzt1lvoLHa9uwnBtJkd_LttQfZCwfwTR833UGgyU7qvvSpb6Nuf0aKUXD53bHLJKvLD3CMY7-Gw9794gwOATzfuVDTBrTBkVdm4aVc95VGHEQdqjLN3V5_5Sm6TaNoeK8fuMhT2JvYCZzR_ML4wMPD6L9-y2bgvkLa7lnvaSBP1rw27sFwCRyYMIKkUyM1d0T8T1p6UVRFFcfhu4VSi2Enbsgk1YWR1UjIu5MHZmiPBHzDBTTSvQmZnaG_ZLBW2C8Yke4B7ABacAvDkmQGgHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رودری تاکنون 328 پاس دقیق در جام جهانی ثبت کرده است که 109 پاس بیشتر از هر هافبک دیگر در مسابقات است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/96382" target="_blank">📅 17:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96381">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzAm3I_WlnY0KqVIrKqI7zDMz6HmfOu1QzkPMqMgb4GaWFTgQOmAA4Nn9X-NCQXXFGkvKXrml1-g2u1h8gYx2LgYMTgCXA-inC109uJybQQYBKclLGOVbcyy-Vr6H2f_SFBxXAylX8rHplKiYOFaHdxAWJm73QAOVs5gIhfUBgaOFyJ9wbgwaWceLPJwh5dqE-h4cDL38Ga_yFsW1CCKowuTD2fEcTGI9hPfq7x7sRMV21G6t64-GVul62TKKC7Nvo1THqs6NG_ZckUM0vfJsDlPTPVEbQaQbPrUGIAWwomFON3Tz38vcjfxojgZt349Us0k5egQe4aaR3xlPnOBTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسامی برندگان جشنواره ۹۳×۹۳ بانک کشاورزی تا این لحظه
⬇️
⬇️
⬇️
https://www.bki.ir/fifa2026lottery
‌
🔹
برای شرکت در ‌قرعه‌کشی
اینجا
رو کلیک کن.
⚽️
فقط تا پایان بازی‌های جام جهانی فرصت دارید
‌
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/96381" target="_blank">📅 17:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96380">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cke6ZmcYnr6GQVf8fULcro-ZxM4OVJTzWtYnZTi3Z6GrGIv__RpgDId4UquK9WL5PmnvLmSUSXbEkbBR31US5xEfo5FF2dX2HPuSbwdHADcXSFjNT2h0F2U9QZNXXV_NqzgYXsU7n7OA_w5iZy5cVXzslRA08J0j_tx-qox-OlJFFwbJSYTYPvqjON8zhlT2A_rh5deTQuiXc9dIaonJNRydBx9RwpjuiPw4RLVrKiUIGHiad5yuI4VGIfHYXo2LOL5RLKIPNMQRcjhyunha_kywWrncy7yia4bes89cPyPgj7Cjd8Fz-pssbWGWFb5yWfMkBXXmejBUv1lrZ4PqAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به پرز بگید حرکت نکنه که اوضاع خیطه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/96380" target="_blank">📅 17:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96379">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgwQNZNN_SwC4pu7Zq3jx5hO5xnIZwLuFoACFBSOwH6ACVR_qaGZ_eyAdR9P2SpZDjn3eYJGfYmf7l05QpAgCz-6NXVLtwOEaru_pXvXJ_SLro5RA0ppMTmQ0fnpyZwRLkhV8bibGOvzGacHOYAP1pwdbj32KW_UAKSX6Zx3KAhZ1wDMdVOErThyo14-ctuyT8dl8bBkytCDx7F5syfxjJ6yXl_Iyi6o2Rx_9hsuasEDr1FZkpsKei3wV8vfLNuyqohz-KSZBa9iVv6qrth4dzVd6_gWuddXcSnQE2CTLBo82wyQ09IadoF2F3Qa63DdE7IwRWhDNm17i_v6fkWnHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آبرومون رفت و شجاع خلیل‌زاده تبدیل به ترندترین میم حال حاضر جام جهانی شد.🫪
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/96379" target="_blank">📅 16:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96375">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tINOzXAoAZV_IsI9qQoemWvl2ltwUsLg9W8SAZYbP1xA1wvWEC9lL0WE-H20zOoGqZ8VVzqm1pt90uw_Yf-5sAqHGeVoJ7qawYvQoyTLjJsMeiadAoHdpigM4gOC-J6miUoiZA1q29VNEMNXfqkZfB00Aw9QoX3Qn8BKcsBh7hiJYWBcGvNAD41i26dUi9dhHNuZR4Ex4m-lt-Jn6xA4ru5ZKOv0FBEiKW0pG0OV-K-3DVZrBNQ0WvO_01c4PGKdWFZaiBDJnm2IovbUBwycN99KfDVNVIXT00Wf8SWc6mZMhl8uV6R-1gIbPGEOQQfsO35MFpNmVQyPkKgLAycM-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bd5QsJImBjdOrixrtgJbr3mwbxpd2HsyiE0mWAL5ozJYM3c7Kv2g2-enA8PAfAJRZFM3beIifl28gXvPKjIQKKdnL48P6UCC_uZfe6Mtx5utqvdom2i8hl44InvfxrEeuwYvipwPhf6lyM8U4B9JthRh98ennXdhGvPEnGu_oDetASo_8FxD-_BD7tcpLrjADCtnrS5q4l48Mlcqif4nulTyYlPorE_ddf0rtWzTH_DBaJ6048ehe-zoSbQ1AU2UgA_gWV6aQcftY9DOfSbqkhBxn6UVepkTQSKZA5_ArvEqwHQrWOL4tYseY1tvPRH4qRdxjxYwEj05GvvrvQak-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vPrTeVnEfytaFchEBcbPLTdvBSh6pzUs-l4ohZ7jM6QP5lIEk9adLsrgbuSEUYrPKTR9RKlyUTHDRmvq2OhLjwf76zBdAmdoBOd5vWY2riIRvaYy8UiSgq1K9EUUbCIEInT1udJGQYH_28adjy_iTkdeROQ9YYcGdPKwuiy-Xeqdo-P8ZfUH2_R7eHkfQU41OzwRCXYP-Htk4QGefl26-a98HcMFKrYkvAERjRCe2FwvHgl9i7puPOHXxe-CkBXu5V-MlFzuVEGuuWZVWjvq4wAGRE0enz1lk9YhNRVok1ZdjekOZEF3PVEde6p3fkGRxCkyjH3fM_Jw0rDkETZxfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FG_H9vInuFVxx9dFs1N89Ej9IXLeJ_fatPsEAEOAD3WpoU8W1TFz808D1UDAgu8qfxfVAsfPsB12f5VwV0YBSk0VYigHRJ_7eKObTKHeM-UIQtHzskqxOBexCj6OgfOjXQXDB4cyZst_DGqOC3rP5JFNqOX1xc7iH-UP8JL8LnS--WKgOQThUAuWvVlYmxnsybyMB9DozwRGgOQL7RLoYgNIGHsBQBl8HPlWVjhphsD3XMqMfTOqO4iRgYvOOTPbpE1iR1OfqDDu0vJ42rsIKZNuU_ASyprT-3RSqx9FXYfSDZd4ewcKOgj79gvR1X15YHQHSHtl9aeNIKEGQZEpPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حیف شد عربستان دیشب حذف شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/96375" target="_blank">📅 16:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96374">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/96374" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/96374" target="_blank">📅 16:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96373">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=Dl3MX69AgDV1FQoOkxFrv4ElnTdHkpjxMij_knJYKbIv_1jKNDzJmrbaetKN9-RlSdjt7DvWLwbbTVluKW0HRgtQ4fuIu-Z40MzsD4WFaUGynfBA2fXtTaksF3EHDnqV7uy1ZMH3csiqaZqGGsvW9asHZiTFQE6UlYcEnkAerosZDSmCbcWZ35EjQ83IJHE543n9Rzpnox_5v5TtNUyX_z9O6t6oFHJK63ZLQvR0Jqu-PRhgojGCX8uOZ1kjOUXMNiQMIENwbwK4HyXuSw7Xj6G5kYFRJSjIE-3Bjm3iuB-Xh5v3xvAe61q0sOYUG9fdF7LVySSoyPj7NVAiuClqADNo_Moav7wMAzWUX9K8oV2C9hBjwwCEJwIrWiIp5RpO_422yBquOMbNoErQsZrYEh2qG91tskjBGb-UpzMmsm9f7mIYNLNcZ1-dbD-hbFn7JmVRw0RAi5YqMUbL99OJsvHS2POJpJyg47cMMqeink9ZlPHCvY03dF53vYxbG4gwme2cox0qdFrH7fown6Fq73uS1lC96ngZdI2zaP1zsG0rCexh61lOr02iGlrYE-B6L6vZHP9hsV7nL7J2ghOkWSxsfnTqGdpgmRtbOrl67peWHb4OIBCdUdJ8X5rZlubDzoQXv4l8DMayCfySqLacNWsbmDPQ66Yhc6af9IHrJ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=Dl3MX69AgDV1FQoOkxFrv4ElnTdHkpjxMij_knJYKbIv_1jKNDzJmrbaetKN9-RlSdjt7DvWLwbbTVluKW0HRgtQ4fuIu-Z40MzsD4WFaUGynfBA2fXtTaksF3EHDnqV7uy1ZMH3csiqaZqGGsvW9asHZiTFQE6UlYcEnkAerosZDSmCbcWZ35EjQ83IJHE543n9Rzpnox_5v5TtNUyX_z9O6t6oFHJK63ZLQvR0Jqu-PRhgojGCX8uOZ1kjOUXMNiQMIENwbwK4HyXuSw7Xj6G5kYFRJSjIE-3Bjm3iuB-Xh5v3xvAe61q0sOYUG9fdF7LVySSoyPj7NVAiuClqADNo_Moav7wMAzWUX9K8oV2C9hBjwwCEJwIrWiIp5RpO_422yBquOMbNoErQsZrYEh2qG91tskjBGb-UpzMmsm9f7mIYNLNcZ1-dbD-hbFn7JmVRw0RAi5YqMUbL99OJsvHS2POJpJyg47cMMqeink9ZlPHCvY03dF53vYxbG4gwme2cox0qdFrH7fown6Fq73uS1lC96ngZdI2zaP1zsG0rCexh61lOr02iGlrYE-B6L6vZHP9hsV7nL7J2ghOkWSxsfnTqGdpgmRtbOrl67peWHb4OIBCdUdJ8X5rZlubDzoQXv4l8DMayCfySqLacNWsbmDPQ66Yhc6af9IHrJ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/96373" target="_blank">📅 16:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96372">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6f86a272c.mp4?token=YNPev_NsGFFo3jmUF1K_FAco2iqQsMT2bEroe6qoTvqmvB28UMdv2-bfNeOl5Aueb18_LMi6orpt5eGj2PgDlqamaCNFy9qnE7sErRfT6M7t6dz_PBojOfUxbP5XxVK1S1wuNrEWPRpiIJna-O3Wac9MdrJcYkwufx2HuTrzdo9HV9rfS_iUg7m33tKrjatLJGm20jynvvzY3szRhjlck1iyL3ClUtl4GjVHKCS3NrQ1gci10ekM62Ugo7HqnbEUvQf2SHpTtzCczZYHFPk4wwnjXkxRAqAOSL2pTM_RB1w6M1M4hMpBfKOAA1YuoYrBJwBjg-VCXIaCiKaKaKgkkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6f86a272c.mp4?token=YNPev_NsGFFo3jmUF1K_FAco2iqQsMT2bEroe6qoTvqmvB28UMdv2-bfNeOl5Aueb18_LMi6orpt5eGj2PgDlqamaCNFy9qnE7sErRfT6M7t6dz_PBojOfUxbP5XxVK1S1wuNrEWPRpiIJna-O3Wac9MdrJcYkwufx2HuTrzdo9HV9rfS_iUg7m33tKrjatLJGm20jynvvzY3szRhjlck1iyL3ClUtl4GjVHKCS3NrQ1gci10ekM62Ugo7HqnbEUvQf2SHpTtzCczZYHFPk4wwnjXkxRAqAOSL2pTM_RB1w6M1M4hMpBfKOAA1YuoYrBJwBjg-VCXIaCiKaKaKgkkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
دستم را بگیر و مرا دوباره به آن روزهای خوب ببر سپس رهایم کن و برگرد؛ من نمی‌آیم...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/96372" target="_blank">📅 16:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96371">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTW6_PtOCXCM6hiQeEe7dbsKb2gf7_p0IEGRZdoe7-8oqONC9OVXBc-LaQEwRmyOIb9U0EfH1VRDQV_NyEUKrHzDBaXN-JJbXJrMA4XK6wChaB1D4a_grx1gy_mz9PeuWojaBIFho_lXNiWzYnUy1huWrQ7ioxTmcaKOixQrbcSiS_R1qoIP9Kz_CCDwUv05QXx4UUIiNjtMMFl_IY7TnVICFmhpwH5REXWQCAFIWBWpKPF116klkxdUcSugD8CazA1zmNuOFmggRAZkwvCCQBZf15tdG7H5sN1k2F-th836MwG1XFNZn8qEQMUC-QvEe6d82z2SCSNSPq1lAFP0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هکتور بیو ، بازیکن تیم ملی ونزوئلا اعلام کرد که همسرش در زلزله 7.3 ریشتری این کشور هنگام مراقبت از دخترشان کشته شده است
همسر بیو زمانی که ساختمان در حال فرو ریختن بود با در آغوش گرفتن دخترش از ریخته شدن آوار روی او جلوگیری کرد اما خودش کشته شد، ساعتی بعد ماموران آتش‌نشانی فرزند یکساله این بازیکن را در آغوش جسد مادرش زنده پیدا کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/96371" target="_blank">📅 16:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96370">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuVIFtQmwZ4NsTp2mdAv7OG5uX1hY9MSIZipQzYTRoMvF429da54d2ihO26iD9XIf3L3YAeTYCP54IS2eDYZVt8pgqcLJwgBZasg2ZNdRRvDYVfm7g3Kv76eO13ZwNYOgHGUxBKrprKKBLdjWYx0vk5dEnA7YGx-FWai0qBrHizrdXKAH_ILQUodV1xKd6wIcgKzSL0whU2qsVHcKu5EWGzJXnnLXPH_wPtylXqb-lLur7gpcWPlY49J9uOIJBsWkELmli87vTNE50hz4APsEkPd3fueJdEok71cc89eJaOeNYxhd7amJkJvB_o8zRVUrkVDa5uasMkrJPl8LuA9Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🤯
رکورد تاریخی به نام لوکاکو!
🇧🇪
روملو لوکاکو در سن ۳۳ سالگی جوان‌ترین بازیکن در تاریخ فوتبال است که ۹۱ گل برای تیم‌های ملی به ثمر رسانده است
🇧🇪
:
‏
✅
جوان‌تر از علی‌دایی
‏
✅
جوان‌تر از کریستیانو رونالدو
‏
✅
جوان‌تر از لیونل مسی
‏
✅
جوان‌تر از سونیل چتری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/96370" target="_blank">📅 16:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96369">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b68a2145c.mp4?token=Yf6wxom624GJVMIwqepOTdB66f4q9glWZ0wuzjaKCxwID75F2EHtRbE1761x0FQxv6bP8cCNpTYP-rl4L2Zw2yhEcZenNGOEzlK0BBKYEtBUvpgJPjZ7WUiWQXG28JOcWi8GKBO8LWwzc97Fc20fm7TUu0eEZJCo9TSvdtml8A3EZYe1gOsZvqBa61NbWchJdY_Hwobl4N04OaUSXw3VXlTUoCULPa7NJvpamGZ-SqtAWAR-DqmfpinXgnbN-Jg4FPMGE3tjJV12EYm3ftzH-SDgjajLznNEwRWJbZSlHmql1ZpFYW2mUqXExXLA83YKXfWOuYNFac80hmnZVOlFHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b68a2145c.mp4?token=Yf6wxom624GJVMIwqepOTdB66f4q9glWZ0wuzjaKCxwID75F2EHtRbE1761x0FQxv6bP8cCNpTYP-rl4L2Zw2yhEcZenNGOEzlK0BBKYEtBUvpgJPjZ7WUiWQXG28JOcWi8GKBO8LWwzc97Fc20fm7TUu0eEZJCo9TSvdtml8A3EZYe1gOsZvqBa61NbWchJdY_Hwobl4N04OaUSXw3VXlTUoCULPa7NJvpamGZ-SqtAWAR-DqmfpinXgnbN-Jg4FPMGE3tjJV12EYm3ftzH-SDgjajLznNEwRWJbZSlHmql1ZpFYW2mUqXExXLA83YKXfWOuYNFac80hmnZVOlFHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میثاقی: اوسمار بعد از بازی دیشب اخراج شد و پرسپولیس با اسکوچیچ بسته است
مدیرعامل پرسپولیس وعده داده بود که اگر پرسپولیس قهرمان نشود کل حقوق و مزایای ۳ سال گذشته‌اش را پس بدهد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/96369" target="_blank">📅 16:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96368">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ffa49c692.mp4?token=qG7HPAdja19adN5UiGMGxGGRnmobmKFjFAMJ2vhidSJvLLFu3Ske3FjqezjpTqF-lIxf6xqvv_b350AJP3UjX8uS-8uO2ZRw2zzO-IJlYrbXQIo147Rp7o_NCj3DXKi1Bdh1TffI8GVdeWlSNse2_DC1iJ_wk1VCb6BrzYAkflESex6JKreEVJhS4Bk2DJyaYoAsNAxMcyWRwMP49-yzSwNH9KWZJscLxDFS1f52rPKGiTGSSCb_Rrt986bVVFxU3xXTBwYuD-kX2yycy1nICYSjATTam1ZFX-zueZ4tw0DDTv1fhU8QYoNnX8LTOYiqxK2LFEIepQTwsxZgsqu20w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ffa49c692.mp4?token=qG7HPAdja19adN5UiGMGxGGRnmobmKFjFAMJ2vhidSJvLLFu3Ske3FjqezjpTqF-lIxf6xqvv_b350AJP3UjX8uS-8uO2ZRw2zzO-IJlYrbXQIo147Rp7o_NCj3DXKi1Bdh1TffI8GVdeWlSNse2_DC1iJ_wk1VCb6BrzYAkflESex6JKreEVJhS4Bk2DJyaYoAsNAxMcyWRwMP49-yzSwNH9KWZJscLxDFS1f52rPKGiTGSSCb_Rrt986bVVFxU3xXTBwYuD-kX2yycy1nICYSjATTam1ZFX-zueZ4tw0DDTv1fhU8QYoNnX8LTOYiqxK2LFEIepQTwsxZgsqu20w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مارچلو بیلسا بعد از حذف اروگوئه از جام جهانی: «خود موسلرا این تصمیم رو گرفت که تعویض بشه. درباره‌ی تعویض والورده هم، راستش دنبال این بودم که با دو تا مهاجم نوک بازی کنیم تا بتونیم موقعیت‌های هجومی بیشتری روی دروازه خلق کنیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/96368" target="_blank">📅 16:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96367">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b871ffb756.mp4?token=JJHloOba9ixYFHPEFD2z5mnJOsAIA8a_57MuS3x7njJZJUh4nOEIHENHWDTGFme6Sbe0hPJFjgBeJOedsTQBZHiR5S7cXHA3XTinbrO-nlahkkNb_7_PKz7mQGkZpoDtLlMhWnPreVVHxBcfy6gf4YrPk1EcvoT8oF-KWR4hUsrD6iLxXRSgzemQq7o2fw0lqAmqDFqQ3f7UPznm37RzaaI6Iwfa9qjIUsEjff0hzLtkiwxw8ko2uLkjMyrRFGnlczpp4lcCUjSpadmnfAYIwOKdw0BNZ7UOyl2coVU2M9YJ9eWcTj5RDESoVwfNJNlq-6f6lNezR-a6sXZ7uSlAZ6shPPtXBZ_kVBQBNSmuJp1GQjrhzepoNXJHUcJGirdT9VFfdkeFw4p9VOZ_KKVSoKtAUP0eGrRW72W-QPTfsuxiw-2k3TxTYF7f7sMsZ6In8Cza6V4WoqQfobB8q6N0BKFMuZfOrviwf-4grshyp-Q4MX7--K4KWjWvUbyC2UvjC0pv9Sa5K989tYpNRWhh576ehAKDOyL1u9tkG5kOhvLM2Iv-fO1G86_wjnaRk4ArV2MkUIN_Lq7uPwL_0dgbFbCAhrtiIqNb58MbcxwyTb7GJDRK4Ugvh_fkIrsr8cNIM7lF-NGmZEOtz6V4n787vxPerIOoONpOo18d1GIf66c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b871ffb756.mp4?token=JJHloOba9ixYFHPEFD2z5mnJOsAIA8a_57MuS3x7njJZJUh4nOEIHENHWDTGFme6Sbe0hPJFjgBeJOedsTQBZHiR5S7cXHA3XTinbrO-nlahkkNb_7_PKz7mQGkZpoDtLlMhWnPreVVHxBcfy6gf4YrPk1EcvoT8oF-KWR4hUsrD6iLxXRSgzemQq7o2fw0lqAmqDFqQ3f7UPznm37RzaaI6Iwfa9qjIUsEjff0hzLtkiwxw8ko2uLkjMyrRFGnlczpp4lcCUjSpadmnfAYIwOKdw0BNZ7UOyl2coVU2M9YJ9eWcTj5RDESoVwfNJNlq-6f6lNezR-a6sXZ7uSlAZ6shPPtXBZ_kVBQBNSmuJp1GQjrhzepoNXJHUcJGirdT9VFfdkeFw4p9VOZ_KKVSoKtAUP0eGrRW72W-QPTfsuxiw-2k3TxTYF7f7sMsZ6In8Cza6V4WoqQfobB8q6N0BKFMuZfOrviwf-4grshyp-Q4MX7--K4KWjWvUbyC2UvjC0pv9Sa5K989tYpNRWhh576ehAKDOyL1u9tkG5kOhvLM2Iv-fO1G86_wjnaRk4ArV2MkUIN_Lq7uPwL_0dgbFbCAhrtiIqNb58MbcxwyTb7GJDRK4Ugvh_fkIrsr8cNIM7lF-NGmZEOtz6V4n787vxPerIOoONpOo18d1GIf66c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
عشق و عشق‌بازی کف آمریکای شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/96367" target="_blank">📅 15:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96366">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0f23a0551.mp4?token=a-qEhzjNu8BPVubC9mQ4B7rHL8s6DeeQwVp29wuFeCjvNr1TBycTzDhs_YzyLsw-EmFXMO4FXzkIBAZ0CIqlz2ZZySwS879k1mECmmvhRlgBoIT3FiEjBsWRS68kG_-6IDSuu-_HJ6_6JKEAzX-SK2XVJq_DNFheXlMKvzzUc0PVr9LejrfKm2fFMQt26wI4yasLbyRmmQjkees83sLmWTpNNK5xMwuGug-3hVTG-GhzCNiqw9VfLfVYIOwoaDmD5Xwml5QjZdEpbck_S3gvLciSRXBLq5K_hJ8CC7TkdjLO0K7gVvTPPet0WUToLJVJGBV_G15uvHHWYhw5PGl4xoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0f23a0551.mp4?token=a-qEhzjNu8BPVubC9mQ4B7rHL8s6DeeQwVp29wuFeCjvNr1TBycTzDhs_YzyLsw-EmFXMO4FXzkIBAZ0CIqlz2ZZySwS879k1mECmmvhRlgBoIT3FiEjBsWRS68kG_-6IDSuu-_HJ6_6JKEAzX-SK2XVJq_DNFheXlMKvzzUc0PVr9LejrfKm2fFMQt26wI4yasLbyRmmQjkees83sLmWTpNNK5xMwuGug-3hVTG-GhzCNiqw9VfLfVYIOwoaDmD5Xwml5QjZdEpbck_S3gvLciSRXBLq5K_hJ8CC7TkdjLO0K7gVvTPPet0WUToLJVJGBV_G15uvHHWYhw5PGl4xoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🙂
🇫🇷
شادی دیشب فرانسوی‌ها به سبک وایکینگ‌ها بعد برد پرگل مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/96366" target="_blank">📅 15:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96365">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f46f8116.mp4?token=BNDLDErOp4hUhLk17Ky5fnrp5wAsgeFkt2fkGkEOkPbABr6qk1jZLyPy4CwflgV0B6e_yzqIt8v84pczwwxFHbjgqosdvnWpbvAusVYmHq5Nh321h5ia-LodoPTBx0CezygVrhGIUJnam7oPDOw248j62WYFcP4Xo0ZUDFI1OU5M5d7KMktMPvc6rxV79tj7HgfLwYXH7DbvLotgFQL70OSIer4kRLK_TkDjpWyjHigrbZI5VUQrACjBam7aec0EJ332gmjYJjHexnkcxsUPtV6jbIejZjAg_PiZP4BNkzgVKS_quVJjlxpL9G7GqTtk-T-8NnIfFluDpfTPpzyCOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f46f8116.mp4?token=BNDLDErOp4hUhLk17Ky5fnrp5wAsgeFkt2fkGkEOkPbABr6qk1jZLyPy4CwflgV0B6e_yzqIt8v84pczwwxFHbjgqosdvnWpbvAusVYmHq5Nh321h5ia-LodoPTBx0CezygVrhGIUJnam7oPDOw248j62WYFcP4Xo0ZUDFI1OU5M5d7KMktMPvc6rxV79tj7HgfLwYXH7DbvLotgFQL70OSIer4kRLK_TkDjpWyjHigrbZI5VUQrACjBam7aec0EJ332gmjYJjHexnkcxsUPtV6jbIejZjAg_PiZP4BNkzgVKS_quVJjlxpL9G7GqTtk-T-8NnIfFluDpfTPpzyCOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇳🇴
شادی نروژی‌ها در میان سربازان ارتش‌کشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/96365" target="_blank">📅 15:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96364">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68b317fa40.mp4?token=hPRMHAtPZVH7qpTGXrRORFTjKiUNGiD-iQZ6Vc-T1yzPIvzFHVE-xDQzlYQoqVRDTjPXZLrcRs11wAqR35iutaHpcecO7LEYWVUbzBKRYr4k1dfxiSQcmKQyodVC8LP2qVGOWvVkUt_KPBp_9m6pDMDCXey_lUOrg28nvff8F2R1oRYp53XxaQGoCJIrypKT7s1cbRxRhYpZMwuOap5JhlHa_AHR-bXrVap-wDJx_V-oXLpw1H4xDVVBA-DBbwJCJrVNLN6arUn0vXvZpRbFjEke2YNx7ee4otq6HmXqa1E5JdJMoZYSZ4hV51U6Bgp28a9hvKz-dI9xSAUA1WbHBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68b317fa40.mp4?token=hPRMHAtPZVH7qpTGXrRORFTjKiUNGiD-iQZ6Vc-T1yzPIvzFHVE-xDQzlYQoqVRDTjPXZLrcRs11wAqR35iutaHpcecO7LEYWVUbzBKRYr4k1dfxiSQcmKQyodVC8LP2qVGOWvVkUt_KPBp_9m6pDMDCXey_lUOrg28nvff8F2R1oRYp53XxaQGoCJIrypKT7s1cbRxRhYpZMwuOap5JhlHa_AHR-bXrVap-wDJx_V-oXLpw1H4xDVVBA-DBbwJCJrVNLN6arUn0vXvZpRbFjEke2YNx7ee4otq6HmXqa1E5JdJMoZYSZ4hV51U6Bgp28a9hvKz-dI9xSAUA1WbHBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
مارچلو بیلسا سرمربی اروگوئه دیشب بعد بازی با اسپانیا کلش کیری بود سر خبرنگار خالی کرد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/96364" target="_blank">📅 14:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96363">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025a2a9a9e.mp4?token=Vw7G5pwIhg59-9XKPxy_L9yJ3bIXsRvht0h8dfks5wD25MySZ-v8p3l6R5kZsQMPoFir9TevYEjYalzk_xWrQQ0Ckgcr1b7OUrWonk6mXekKLgDwfZXIvklfWmIviSHzJJ8xlyyPg9aPzcRipVnfvBl8KFqOrDiASo5t-X6J5cV6ZMJtB6UAnNhkdsbW0MSj74ohDJ3L08SmN5s4Co-7KmBG-EJs3g4b7tTrfhhF6tJtcwH13QCdv4XxsfsOWkOgMnXRyu1ZrWZoPBRcXelKWxgzq1j9n3gJb-X3KuHG7rlNI9dvngmikcYLxL0NJ8xHjxsZpWrecnDMHIwwMrQ-3Q9rWhlvBkkL4zfFr_nFJisrNmtydRzUMC-Sm9muvBdIHuRzIGgllIShiGdZaxf5Kk-G4IPxECdEVivbnFcNNZb_bgMPQkAeuEk6mQ0g2emr6a-T0kd40q5Jk2_f0Ax6bX8owAeCxP4De4_nZpP82tJ87pnIMvMY9bwAN9qJN4ofk9fBUO9ToPt7T5ijBqwVvfHKzzvNqz8oOV298a0tK9ei6mv4R1MnpGuuEcdN-IN5gMQvF0hC0IglRmzTT3Wyul8muoUhE9MfD3hKM3py_JSy4e0ZtpjirKmfYhUGITTThzPNDuTRBrLWMjDqP3BtCMYw0q_iQyFHScajIco59mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025a2a9a9e.mp4?token=Vw7G5pwIhg59-9XKPxy_L9yJ3bIXsRvht0h8dfks5wD25MySZ-v8p3l6R5kZsQMPoFir9TevYEjYalzk_xWrQQ0Ckgcr1b7OUrWonk6mXekKLgDwfZXIvklfWmIviSHzJJ8xlyyPg9aPzcRipVnfvBl8KFqOrDiASo5t-X6J5cV6ZMJtB6UAnNhkdsbW0MSj74ohDJ3L08SmN5s4Co-7KmBG-EJs3g4b7tTrfhhF6tJtcwH13QCdv4XxsfsOWkOgMnXRyu1ZrWZoPBRcXelKWxgzq1j9n3gJb-X3KuHG7rlNI9dvngmikcYLxL0NJ8xHjxsZpWrecnDMHIwwMrQ-3Q9rWhlvBkkL4zfFr_nFJisrNmtydRzUMC-Sm9muvBdIHuRzIGgllIShiGdZaxf5Kk-G4IPxECdEVivbnFcNNZb_bgMPQkAeuEk6mQ0g2emr6a-T0kd40q5Jk2_f0Ax6bX8owAeCxP4De4_nZpP82tJ87pnIMvMY9bwAN9qJN4ofk9fBUO9ToPt7T5ijBqwVvfHKzzvNqz8oOV298a0tK9ei6mv4R1MnpGuuEcdN-IN5gMQvF0hC0IglRmzTT3Wyul8muoUhE9MfD3hKM3py_JSy4e0ZtpjirKmfYhUGITTThzPNDuTRBrLWMjDqP3BtCMYw0q_iQyFHScajIco59mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو رسانه مطرح مارکا اسپانیا از درگیری میان طرفداران و مخالفان حکومت در سیاتل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/96363" target="_blank">📅 14:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96362">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=fz9aQSp-Z-JuKvPv4SUZQZVZQhtAqLHFrG98oihjkPbbxDjmjqeTeVDaMqqm9yvlSxO4TqOvdwPY7Q6dLEyK40MkXqv2xoWmayDBiqYHb-l3zLlP-hMYKuEhS6HBz5mfE9aS_jooMZdjh3vGQWpZRlWhmTcMUDRKijSO6J_V7_fFjx_zTbCQ_KgOB3GvYC2WUT7yBziqGT1F0GDi_nvcSEyesCPy0GjY6_k9xiVzu54pZTIeci8HECg9HyRtG1YQF2uSxVUiaPEjBNCGDV5-kElVkYP19HBxXvQ-DJRtRdFJnHb7FY-mXaIqcsCvtfWqUigQ3DBlvHyZeHppEbywJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=fz9aQSp-Z-JuKvPv4SUZQZVZQhtAqLHFrG98oihjkPbbxDjmjqeTeVDaMqqm9yvlSxO4TqOvdwPY7Q6dLEyK40MkXqv2xoWmayDBiqYHb-l3zLlP-hMYKuEhS6HBz5mfE9aS_jooMZdjh3vGQWpZRlWhmTcMUDRKijSO6J_V7_fFjx_zTbCQ_KgOB3GvYC2WUT7yBziqGT1F0GDi_nvcSEyesCPy0GjY6_k9xiVzu54pZTIeci8HECg9HyRtG1YQF2uSxVUiaPEjBNCGDV5-kElVkYP19HBxXvQ-DJRtRdFJnHb7FY-mXaIqcsCvtfWqUigQ3DBlvHyZeHppEbywJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
گزارش تلویزیون الجزیره از خوشحالی مردم مظلوم غزه بعد از گل مصر به ایران.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/Futball180TV/96362" target="_blank">📅 14:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96361">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdEY2h-SC0TT-3TV6J-R4aJoIeETBJQogduOkxrKQLrzZjU5IMPBDelxESbTb4xBICt9QzuOSrq37Opm6iEshAAKz3qdIao_rJQZE_60kxIR8saVzcOwjJHIYqo2sfNu0q2FGfXmoisVdAeRfZOHkaBByeD2S6TjW5quaf2Kud_sy5Qy_gYPLJySYQeh1PhHkuyCT7duR9V6RE4VtORF-eZNcqoi0KxRCEcGQTr0sklcP2LHl-T41-g845Lzwp7X5_X003w8keE3lmPy83vUoew2E3G-ABf0TNbvxNgunDOgWkadGEqQYARPjwFa9FNmPR57B6VHFQ-ZMWpxz2NZAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
آژاکس در حال بررسی احتمال جذب تراشتگن به صورت قرضی است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/96361" target="_blank">📅 14:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96360">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12bac0d662.mp4?token=kkwZe4bsx-2rrqeHAye1Cvvq73rjxz3TK68eGH33Zq2tbExcXnPd6bN5E37Ld5dQhZ0FPheeWqfbfOENeqSXVL5Hb75J6wnpk5WYECKUlsmlXWk2JqdBKEP1oDtcmwrXZogfOkQPUYINKiT-9L_J1w0NQ9xzL_EjfHNXUr-3rptrNrC6hgDs4TPiQ93CabwpxdHIuJnPpIQW8Irg6sU-zkDPTRONNx-oo0Lg5VzAX_J0pNJNzQsTpNYPS-6rBvkIelD8ERK8ucbsfe3lJrpHUbcutc_JZbpMgzwk8_wrMkdldIGZEtDJBT1UOGY7V-LwAqy3srK80PRnnu9AWNvWkXq5Qch_yyLYScGErIvLUaCC_3wnVuoVMPMJnA0vIPXQ-shSOxRm_M1raYiLA-sPrPjp-AhBw0cAUjXfs2kfSuuXgkgWj0W4tVAzhhhmVolgKEZYHegic5e5ak8w66g-F1XmdCtIS5LmRo_IHH39wC8sHdt5lx9Vo8oEoRUhIriQBNcATY_f9maaLzz1uDRBUIrxkTJpLPnKKmpR1gh-8nvZhLBcQUDBr7t8G4KJtOUCU6LAxVu7q7_NJQ6rFsWyLNMA6jvYW970FWr55fR34J-NrRZHwyilut9eFjg-ZUaXT2sGxr917y-ScQsm3F4QbtBYki6ZII5D9RR9d9U7iDc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12bac0d662.mp4?token=kkwZe4bsx-2rrqeHAye1Cvvq73rjxz3TK68eGH33Zq2tbExcXnPd6bN5E37Ld5dQhZ0FPheeWqfbfOENeqSXVL5Hb75J6wnpk5WYECKUlsmlXWk2JqdBKEP1oDtcmwrXZogfOkQPUYINKiT-9L_J1w0NQ9xzL_EjfHNXUr-3rptrNrC6hgDs4TPiQ93CabwpxdHIuJnPpIQW8Irg6sU-zkDPTRONNx-oo0Lg5VzAX_J0pNJNzQsTpNYPS-6rBvkIelD8ERK8ucbsfe3lJrpHUbcutc_JZbpMgzwk8_wrMkdldIGZEtDJBT1UOGY7V-LwAqy3srK80PRnnu9AWNvWkXq5Qch_yyLYScGErIvLUaCC_3wnVuoVMPMJnA0vIPXQ-shSOxRm_M1raYiLA-sPrPjp-AhBw0cAUjXfs2kfSuuXgkgWj0W4tVAzhhhmVolgKEZYHegic5e5ak8w66g-F1XmdCtIS5LmRo_IHH39wC8sHdt5lx9Vo8oEoRUhIriQBNcATY_f9maaLzz1uDRBUIrxkTJpLPnKKmpR1gh-8nvZhLBcQUDBr7t8G4KJtOUCU6LAxVu7q7_NJQ6rFsWyLNMA6jvYW970FWr55fR34J-NrRZHwyilut9eFjg-ZUaXT2sGxr917y-ScQsm3F4QbtBYki6ZII5D9RR9d9U7iDc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🤩
🤩
کنایه بازیکنان چادرملو به پرسپولیس: به 2 روز تمرین بردیمشون!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/96360" target="_blank">📅 14:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96359">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czroTHHYzr5K5yrCUQLDU1M6WMvfVGXUsf-zodOyc_G9Q35B9h29tdmJJhFl40Ewq8pU9CTiDYk-xAQbVzf9gm92aAfZ01Ohz-f43jNm0p5XZivywzh3Nxbv_FD_jQnOaQbhtWiHelHGdIZN2XBxVa0M4AlvxWYfLBJ214MmlSvpljjTz-xnjhcNYM_jIWxTs9IOMK4PHgtuAoie7xrXZuVdT8sqUdYK55MNQoJvSGGz3n-ZZBwekMVp7WVq5mKoBZ5015twtEFgH2IJfAnhvJ3TlEAjtgdKztHnPHvwDRxi6H91pSHgkST9QlN5SeKeH3PFYzVnPEn2NUPz1ggSPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه چلسی از لوگوی جدید خودش رونمایی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/96359" target="_blank">📅 14:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96358">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe474ed8e.mp4?token=ijid_Y8f26sTDvkJTkRM7yFOzGPM8rg0ggHVZOJ5qEgwWLOH1_hXusQmIphaMSe1wpKrDQZCUKBS87Rs2ik77W8_jajlIXawWguP_RBYdxXqpNSDtdyOA4bPy8HBohrvX8FXnJh_YjGkz8vCfJlDyHU17NoA-XT7QB0U8qfXZukSEmvvl9-6J8YFpuopfFBFy1Bh0CSqN1IAFuxTPnBN2sfFkx-16mdzhjkEDQmF1k2kfke-QfNQ2pv-N5TZJGS53aIV0B7-FeLjdNAt_7LOQN4MVy1dCrPC0CtmQ135JFRCJrsUNP2iX2Bcwu2UC6XkBx5EuJPkKm5I7GeeAofNww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe474ed8e.mp4?token=ijid_Y8f26sTDvkJTkRM7yFOzGPM8rg0ggHVZOJ5qEgwWLOH1_hXusQmIphaMSe1wpKrDQZCUKBS87Rs2ik77W8_jajlIXawWguP_RBYdxXqpNSDtdyOA4bPy8HBohrvX8FXnJh_YjGkz8vCfJlDyHU17NoA-XT7QB0U8qfXZukSEmvvl9-6J8YFpuopfFBFy1Bh0CSqN1IAFuxTPnBN2sfFkx-16mdzhjkEDQmF1k2kfke-QfNQ2pv-N5TZJGS53aIV0B7-FeLjdNAt_7LOQN4MVy1dCrPC0CtmQ135JFRCJrsUNP2iX2Bcwu2UC6XkBx5EuJPkKm5I7GeeAofNww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌈
مهدی طارمی:
همجنسگراها نظر خودشونو دارن و قابل احترامن و ما به همه این عزیزان احترام میذاریم چون این موضوع به ما ربطی نداره.
💞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/96358" target="_blank">📅 14:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96357">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDCGIDMbxNLUOHZFk8lOz4Dt7B_N_krVyQtJV_vmG-pYB1QQcu8DYJnzATsrS4QbnMvnBmDv71B5Wi3cSp4ShxUf5gsX6T7v2JQri0kKpYOQkZGv-URnV0MvgeRI6rYWL9sRBrryYx6M6P0IYhMhQ7Y3qCtd3W6Fyne-wjoDVVBxcnwRff4SPcct8b80eDkRkRSvhrRqvUOiawKLS8HBagt0sIkH4rNHYL94KBmqwZZrLA6-sU5QMcCrJzRol8jA7FNExH8os6azb9ZAElh-WCWHLI7aNslfpYM2vzroDwmTsi2mc5K3dMqpIKVasSYS8XCFJQgzn98vj82Ozcfasg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
🇳🇴
در میانه بازی نروژ و فرانسه، یک زوج نروژی در جایگاه‌ها نامزدی خود را جشن گرفتند و شبی در جام جهانی را به خاطره‌ای مادام‌العمر تبدیل کردند.
💍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/96357" target="_blank">📅 13:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96356">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d12d8ac3.mp4?token=dtyR8xGaGWMXyHUZujAnDjdzhvm9ESVrADJYyABcikFNDu2PvVwJVZ5s_oMRHUixdU49RfbPFhQ1Oliogbj76Yk6tvvaOs71pd1SohtUXJJiXPsxPk_u-Et-a2p24TYVldjEtxq0fmO-UsY5oLFHhlS9uYDakYQGnC8reQFbt6Mhe7VAEG_fM3USSkOQL1j8b1Eti6-bEB7ohjLDvxQyOdr1a984toKugNSaKp6bPhbVKdZrpaCgjn9v0inomdy1C7WNi1n4kDha6FtOeuz6YTuRDlpX1teO83n6Ef-WwbyCAbmEOI78wkaw9d9Jvkx_FeDteFnNJZ8PtKuJpLc-Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d12d8ac3.mp4?token=dtyR8xGaGWMXyHUZujAnDjdzhvm9ESVrADJYyABcikFNDu2PvVwJVZ5s_oMRHUixdU49RfbPFhQ1Oliogbj76Yk6tvvaOs71pd1SohtUXJJiXPsxPk_u-Et-a2p24TYVldjEtxq0fmO-UsY5oLFHhlS9uYDakYQGnC8reQFbt6Mhe7VAEG_fM3USSkOQL1j8b1Eti6-bEB7ohjLDvxQyOdr1a984toKugNSaKp6bPhbVKdZrpaCgjn9v0inomdy1C7WNi1n4kDha6FtOeuz6YTuRDlpX1teO83n6Ef-WwbyCAbmEOI78wkaw9d9Jvkx_FeDteFnNJZ8PtKuJpLc-Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این شجاع هم حسابی سوژه مصری‌ها شده‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/Futball180TV/96356" target="_blank">📅 13:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96355">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/014d5401dc.mp4?token=vZUFXhdwSrmOoGJcH4Gg0qezeCy7kbK1XP63FgelTmcjIEjz6NgNXVx14SF2pZDjW2VseJt15g5ZNKQBplsICMJKnK3ZasalLf4bs9W9SiN_3sw2EYaGv8e2maMzJFD79L-_YQEZHyhEE1cjk-u2mixV0uLyRxDzpfGhzqJUHhs9OnJulpRijgUvihzOlXbOe1NIXKRZXW1jWwFu3-5xtPsru_ZPWELOeK_iftIKlQ6QAxOPqbvbJUqXW0cQCrtp9Dwz8eyMPdcSIgg0WPbp0Tip4jUJP8NNIydwkpap7kP18H9jIyhX63dT3BetI2HZivR1oPkHhVgKNO0ZQWK7dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/014d5401dc.mp4?token=vZUFXhdwSrmOoGJcH4Gg0qezeCy7kbK1XP63FgelTmcjIEjz6NgNXVx14SF2pZDjW2VseJt15g5ZNKQBplsICMJKnK3ZasalLf4bs9W9SiN_3sw2EYaGv8e2maMzJFD79L-_YQEZHyhEE1cjk-u2mixV0uLyRxDzpfGhzqJUHhs9OnJulpRijgUvihzOlXbOe1NIXKRZXW1jWwFu3-5xtPsru_ZPWELOeK_iftIKlQ6QAxOPqbvbJUqXW0cQCrtp9Dwz8eyMPdcSIgg0WPbp0Tip4jUJP8NNIydwkpap7kP18H9jIyhX63dT3BetI2HZivR1oPkHhVgKNO0ZQWK7dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
زلاتان هم از شادی وایکینگ‌ها بی‌نصیب نماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/Futball180TV/96355" target="_blank">📅 13:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96354">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ql1JpjWoxFLPIWRnmIxdkzPX2fqUP6qCyYK1f6CYZd2w5acjvXDoGzFLGqSLeedOfMTOmin3pybMu4OCQZeRP7yDeer7_DmQKWIx3OLXNm5G-Aq3xTRPSyE5lYjc0VA3PlywELE73ErYUthLYpbTYTy2tXoKKWHv69hoSjVjPvX4WRhIgj14ura9mEyY5BbOxz3d3qceoGpbMsN6xwv533akKSwxEtLpUiUq8pEY2KH0CsLYNLbS7JC-qX97f8_1rv82TCm0gln7T8n8PTWGN_BWG3NAxxxVaQzRTp838wK3QkyPIDHY4dGtlPtdM9voLLQ0BulpHHai7gEbIjsi8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بهترین تفاضل گل‌ها در بین تیم‌هایی که ۳ بازی در جام جهانی ۲۰۲۶ انجام داده‌اند:
🇫🇷
فرانسه — +۸
🇧🇷
برزیل — +۶
🇩🇪
آلمان — +۶
🇲🇽
مکزیک — +۶
🇳🇱
هلند — +۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/Futball180TV/96354" target="_blank">📅 13:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96353">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1942a3cf51.mp4?token=XgqpitE6KMT6p-elmESVAhzYgQEjMTtXeEfIh_LvC0XApdjnZLTy6qab17CyCS7-ig5Fi57lLGHCK7jUbW_fCgbTx5zLsU4AYfCJwq2MX4W13G4HbGAQ6D5JyiF2-1o-Bzfg8yI7VR5lh3sqvoiv8ufhe35RjLCvJMmnXDu9AtGT-wIlrQ3g6-DrUAMY6w9008ZoVQEfGRfVPMKAuwtmh-qI65Ow6KRPCxi5bu0FnlQ07dkcerz8YqAp2IlxXnKa1KYBfICBwqya3H39KpmcplbIFUZriHq0EWLVmp3xXuPkQ866sjcFQX-bTM6rcCetwtP505T6nj58puWsnP-QYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1942a3cf51.mp4?token=XgqpitE6KMT6p-elmESVAhzYgQEjMTtXeEfIh_LvC0XApdjnZLTy6qab17CyCS7-ig5Fi57lLGHCK7jUbW_fCgbTx5zLsU4AYfCJwq2MX4W13G4HbGAQ6D5JyiF2-1o-Bzfg8yI7VR5lh3sqvoiv8ufhe35RjLCvJMmnXDu9AtGT-wIlrQ3g6-DrUAMY6w9008ZoVQEfGRfVPMKAuwtmh-qI65Ow6KRPCxi5bu0FnlQ07dkcerz8YqAp2IlxXnKa1KYBfICBwqya3H39KpmcplbIFUZriHq0EWLVmp3xXuPkQ866sjcFQX-bTM6rcCetwtP505T6nj58puWsnP-QYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇫🇷
دیکتاتور امباپه تو بازی دیشب هم نشون داد که چرا بهش این لقب رو دادن
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/Futball180TV/96353" target="_blank">📅 12:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96352">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5c4a20441.mp4?token=q_RpGG2eFsv1_y4xrPGycyONCSLp-Lc_SbeG8S0bdS5aJhstemtq73BIBOTP_mLMMuZMu26oT550wsvtHCoLqxOt1847kqc2S3YZMT7gcIefTResmWRr0grUdm8hq01-CPzn62rwF8JNH_spksdna0WMS-BBO5iyLM62tWfYyeSaH-gxMKe91SRG0GP2fsJkydTsorQRZqzYBenpsGdOEsytnOwBi6kzTZPkClZo_XaiS8B4j5_fwv-8Odu9tZyYi9MjAR3PeyZpdlJgPTuf10V2T4GMcMERUplofs96Pa2aU2zjqYZZZmk-whZ0ApS7jrI-3gGsYmu8CJaIljoUB6o4AHr82ji5v8kFNalrGAUem88T1yLgHB9ekQjNGLYSWRdlyaSTVque6khMxN7knBN7cGMcE1yvJyNy30CS2sRuTJcPEjqVtnyZpgdVAu_NZmw23CBZtCLIq5e7TveIJrJNNBsbSqBCuyiHmhkoTrTEei0vFTSc8OMRMQGIr4AS35W-4_FdrE9Zd_pSlLTOr7xQPbZs-YNVgpDUfdwotQyCIUkhuZHh0RYmTxVYtLcSZQznaoKvFDJAJPdJEgr9cxWjHxT8lepGIsmG7WTYxZbzn6q7lLnnJfG6F8fMoNvmXlUSdIZJc_gqWMCAJ0sYwxwK7UiapkQYTCtRgXEIdz4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5c4a20441.mp4?token=q_RpGG2eFsv1_y4xrPGycyONCSLp-Lc_SbeG8S0bdS5aJhstemtq73BIBOTP_mLMMuZMu26oT550wsvtHCoLqxOt1847kqc2S3YZMT7gcIefTResmWRr0grUdm8hq01-CPzn62rwF8JNH_spksdna0WMS-BBO5iyLM62tWfYyeSaH-gxMKe91SRG0GP2fsJkydTsorQRZqzYBenpsGdOEsytnOwBi6kzTZPkClZo_XaiS8B4j5_fwv-8Odu9tZyYi9MjAR3PeyZpdlJgPTuf10V2T4GMcMERUplofs96Pa2aU2zjqYZZZmk-whZ0ApS7jrI-3gGsYmu8CJaIljoUB6o4AHr82ji5v8kFNalrGAUem88T1yLgHB9ekQjNGLYSWRdlyaSTVque6khMxN7knBN7cGMcE1yvJyNy30CS2sRuTJcPEjqVtnyZpgdVAu_NZmw23CBZtCLIq5e7TveIJrJNNBsbSqBCuyiHmhkoTrTEei0vFTSc8OMRMQGIr4AS35W-4_FdrE9Zd_pSlLTOr7xQPbZs-YNVgpDUfdwotQyCIUkhuZHh0RYmTxVYtLcSZQznaoKvFDJAJPdJEgr9cxWjHxT8lepGIsmG7WTYxZbzn6q7lLnnJfG6F8fMoNvmXlUSdIZJc_gqWMCAJ0sYwxwK7UiapkQYTCtRgXEIdz4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
تفریحات تماشاگران جام‌جهانی در محل بازیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/Futball180TV/96352" target="_blank">📅 12:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96351">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGeAPVxu6zypOjHY0K2j0-5j07i0stN70fgW3a68AVPKo11yJHsEffttaFplUn2j0JWL10tMC6pIlgJxdqbxaXutXQtVywizhh_o9wEIAovEa--925iNivq9FNYkrYrmXP1xGDgjud-yYX7BkUz6HOC6ByH-Tg_focobK5-U2-FiMJyT8ft4Nfbx_Kn5oP6g74fi-e1oRiqy1WkifKJCWCMe27uHVD7pfn0iDBD9WchXrwSOpjY4ucqpCWB_s-Zj5yuI9x9dKEcufW-UhKjA4nAk2HILJ-IYdyszRWS2YWYPKlXmaxsI0Mys0a3NvEd8lhREVs9eZUsvbG7br81VWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
در چنین روزی در سال ۲۰۰۹؛ رئال مادرید قرارداد خود را با کریستیانو رونالدو پرتغالی ۲۴ ساله به مبلغ ۹۴ میلیون یورو اعلام کرد.
🇵🇹
🇪🇸
😊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/Futball180TV/96351" target="_blank">📅 12:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96350">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6b9d3e103.mp4?token=gVvl4VJgunU2Jo2j4Cq9WM2p6_SznM5LIbECMSUnib5ZFgiqMvtx5s21wn3Nazn8HWHlEezXYI0WPwyxEuHrl-Eg8eJn8ogPrArmZUv8lawb7dNOmKJYxLthL1J1mzN1N7DnpwMqsO9n_oWa2OG5wBlN0Qni0rpq8vR2w8ii6_sq1-mG_sfrTyRnnqVPf8EkbJxre2eVWU_SgvMrFwyFviLJ-b0W2Eh09-OMJMvM4dSVyPaLDfmrSxxzVoLP-p3AUp1PjX2gSqDGKPhsYSNLhQgDB3apIByDrvBH0kdGiAogc-K7IcgWo8sCRM3vBgs0sGP6Erc1z3LeLhCxbhz5SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6b9d3e103.mp4?token=gVvl4VJgunU2Jo2j4Cq9WM2p6_SznM5LIbECMSUnib5ZFgiqMvtx5s21wn3Nazn8HWHlEezXYI0WPwyxEuHrl-Eg8eJn8ogPrArmZUv8lawb7dNOmKJYxLthL1J1mzN1N7DnpwMqsO9n_oWa2OG5wBlN0Qni0rpq8vR2w8ii6_sq1-mG_sfrTyRnnqVPf8EkbJxre2eVWU_SgvMrFwyFviLJ-b0W2Eh09-OMJMvM4dSVyPaLDfmrSxxzVoLP-p3AUp1PjX2gSqDGKPhsYSNLhQgDB3apIByDrvBH0kdGiAogc-K7IcgWo8sCRM3vBgs0sGP6Erc1z3LeLhCxbhz5SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
صحبت‌های جالب و تکان‌دهنده تبریزی خطاب به بازیکنان جوان
: گوشی رو بگذارید کنار، عشق و حال زمانی کنید که جایگاه خودتان در فوتبال را محکم کرده باشید! بازیکن ۱۷-۱۸ ساله نباید مشروب بخورد…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/Futball180TV/96350" target="_blank">📅 12:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96349">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CilKlrbYj0UeOYr0GgKX_zZrxL_9vSIhDYhwyJ_djixD7-QNTBoQd9v9n2zZ3i0z_fA4Ucx7skIBa8RFMdc23qd0U3LBv6naAA3Tsom1Ce7fxfBnVjOKmCewiG2WgpnUbh1NWRJDrr5QJdxLkybRSUenuenuHpWz0szTVrTIccBqGW54YbH8hFVFwrCaBm8HB2ivQIgtTZQZgb5g4kU3Ua1qFQzMRKsEcF-95z0QSH05OVTvjolYK12knPIW7sWN3GPB7T-eHXeH3BV3j54kbhlPzlGq_sED9GOZrxOStdd5uBvSWQbWBIdnwjtZcNsT0ozOX5CViVcZVjGs5lAVXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
رامین رضاییان با گلی که امروز زد، به کافو اسطوره برزیل رسید و با 3 گل، گلزن ترین دفاع راست تاریخ جام جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/Futball180TV/96349" target="_blank">📅 12:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96348">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee48f95460.mp4?token=MPmkBnTSfvDJJM9DUyFuwDEgWN6GAYGwDxlCZSn9txgcb67FBMUqauOwlWx-VDmp9B3IL-jY76VuzVknmOHvUkR-P3VPLCRjZ1YMBOfYK00myZ57Ht9f9j_zl-tah3sOhyNpr3_PryBQOr7XEmAqPQs6c07NWdVBXuB4rKYlIJFcrdl0SQB-vlY0xO6BNzeKh_eq14JV7j4H8d_sli8FDy-laNbhy99n7Gbkn2UoFpDC3m1-h0qEzJMhoegDH0DqakwQCCxfm44GrjVLkWlaTkvM4xCtjeYMM_AweFmdgkY4xfEW6tc5vjrvoW39qJwLYFJlhCJBgu6hLWowOKJ_wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee48f95460.mp4?token=MPmkBnTSfvDJJM9DUyFuwDEgWN6GAYGwDxlCZSn9txgcb67FBMUqauOwlWx-VDmp9B3IL-jY76VuzVknmOHvUkR-P3VPLCRjZ1YMBOfYK00myZ57Ht9f9j_zl-tah3sOhyNpr3_PryBQOr7XEmAqPQs6c07NWdVBXuB4rKYlIJFcrdl0SQB-vlY0xO6BNzeKh_eq14JV7j4H8d_sli8FDy-laNbhy99n7Gbkn2UoFpDC3m1-h0qEzJMhoegDH0DqakwQCCxfm44GrjVLkWlaTkvM4xCtjeYMM_AweFmdgkY4xfEW6tc5vjrvoW39qJwLYFJlhCJBgu6hLWowOKJ_wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇫🇷
اثر جدید حمید سحری از درخشش دمبله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/Futball180TV/96348" target="_blank">📅 11:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96347">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBGKXgViLFtF3OHrZ6b39QCHRBH_gD56SELJOlvSomq-P_KXrKgyE_LrelWQgFzm-FcY5fm9GviHbYk4MV75LL3b9GgQM2_2YQdxApNLPycuc_gqnm17MxAgIBmyqDQNkJWpPOlRyKQFa3X50Ktz8eikTVWiLOxcMcBFi9hOQMKeJqCC5a2VWn1cL8V9oh6O_kZaKIZkWCaXsSn_9Z_r9uyo6L2FjU7oyksFYsgvVXw8aiQRFgTvGGNn4dB2YyHzYu75ehtSmZ31mgpvxYAcfkC7gUF4LWnD8216JtqmK0QwjQIWwwYjRri07St5OO4805x-TM6kSvaxppybeyyiXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
آرزوی هوادار بانوی برزیلی
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/Futball180TV/96347" target="_blank">📅 11:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96346">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/330a09c36c.mp4?token=MWbHYLGJWcEcaKrCxpWaeAMWMxGyOHorfTCXEhq59K9Xx5irdmFBRXMo433xM15kX47YE7gt5zPu78QU28D9Sd6aGjMylF9Q4c9pz8fO-wObZE-ZGyGJcfUaKHwp4Hg_BFciJTLuewLIo1pp4VK0JEkZuN1E1aAk8bd4WAdVpPRUiG-zUfBV1w0ilDN9CBpu3y6SEAna1AAWeuIf9Xvgbf50N2c3d2WAHMTzkI1Dv_6k4h771o2nnRUVYaQOVGKDI7GLwI-K-dsSkuIcUFcr5BABzxz0UiHHvmZ1M7mIBD2qu7HrDuzqkGHVI_Q4WpPZZG8EJ4FJBZi5DKIP-swpmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/330a09c36c.mp4?token=MWbHYLGJWcEcaKrCxpWaeAMWMxGyOHorfTCXEhq59K9Xx5irdmFBRXMo433xM15kX47YE7gt5zPu78QU28D9Sd6aGjMylF9Q4c9pz8fO-wObZE-ZGyGJcfUaKHwp4Hg_BFciJTLuewLIo1pp4VK0JEkZuN1E1aAk8bd4WAdVpPRUiG-zUfBV1w0ilDN9CBpu3y6SEAna1AAWeuIf9Xvgbf50N2c3d2WAHMTzkI1Dv_6k4h771o2nnRUVYaQOVGKDI7GLwI-K-dsSkuIcUFcr5BABzxz0UiHHvmZ1M7mIBD2qu7HrDuzqkGHVI_Q4WpPZZG8EJ4FJBZi5DKIP-swpmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
از هواداران جذاب و پرفکت رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/Futball180TV/96346" target="_blank">📅 11:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96345">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ml3QOcjzH7aiHpbyz0p4Wo_ysELdWnn600FDQcvCjVBBUtKXeM39hL0PidN9tVByE_vFtzdB1tD8D1ltOq7zx5LYboAG3LRomv-xvfNiO6MiisCerNlwrHBLiXrK00phqQEIDO-jL8qKCZQPWT87LCBgshCmnXR4hK_01Tl3NZUqsKUI0NqgBm0juHMIFz1TYlVv-X4pkRNq0ZGiNSJdQmtcy8mzxDo5wiY1a2NlVVzu919E6B0OfM_e6GD1GtG3RgYt38ewdje_SO2DgUJjiR59MXXgjyNIMhmdz06BtCVN__6gL-m2zQHCvM7zYe6Mn6uvJJoIGLJGN3_0cu4UFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووری
؛ مارکا: نیکو ویلیامز ستاره تیم‌ملی اسپانیا بدلیل مصدومیت از ادامه جام‌جهانی بازماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/Futball180TV/96345" target="_blank">📅 11:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96344">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXfSbk9vWlK0QlSfD-7Q1BluFCbTA4EjfULzcKjXl7oRQP3t27q9PP9bNOt_BI_o46clFPF6JzSiPw2uy-Z3pTiqQJfCHXtOvrJUqQPFU9aCWpxYqcHLXUBaE0KZt8_4mAjHYTcndunhQD7CMloTIm5YdPD89fPT-Bo7MNZKJaTrGfqTuJct-sYA1o1YCmOMQo1jsIBXurut0ncm-k1CW53TFNicwUq6XZdEDUq5piKkIlJLsI7GGcBK00-O6kl7gK4tMGH4_WdHqsY36_47Fh8ePZ61IOFWRCLisAFU2M4hFp4uvgIqppQ-A3yErC45XWubRHX2XjGBq31S5xxA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
کیت‌دوم پاری‌سن‌ژرمن در فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/Futball180TV/96344" target="_blank">📅 10:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96343">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4d474911.mp4?token=dGj7Gs_D25lH3v76LlU1NFwkvu_prq8sOBlx_vzVHz-iPsuFgs6_1gDYnXocIrVBkZgoJvBedAJ8_E2ekwditAsjVN8re7Bh3Os4WXwiBSNavyrcXErzIemHgQYlUCXz4Vn8XfW3H1Qw1nfH5BqEkHWy3XMx1kYqTCdv5GbaDR-xXd8n3fS_gRFl3CAzx7VdxTE15Tq9BVtyLl28NWjyWiItwMgnTW5-NYXyWhb2FFE6diaj1S3VRc3ws2qZmDmIQCill6lqh1eQriar2y9bqUm2RiiAOiKhpP4EWr_S6rFW6pDm-GxobSB0g5j2o7j2rQfXzsk-gizhBkazQF4s9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4d474911.mp4?token=dGj7Gs_D25lH3v76LlU1NFwkvu_prq8sOBlx_vzVHz-iPsuFgs6_1gDYnXocIrVBkZgoJvBedAJ8_E2ekwditAsjVN8re7Bh3Os4WXwiBSNavyrcXErzIemHgQYlUCXz4Vn8XfW3H1Qw1nfH5BqEkHWy3XMx1kYqTCdv5GbaDR-xXd8n3fS_gRFl3CAzx7VdxTE15Tq9BVtyLl28NWjyWiItwMgnTW5-NYXyWhb2FFE6diaj1S3VRc3ws2qZmDmIQCill6lqh1eQriar2y9bqUm2RiiAOiKhpP4EWr_S6rFW6pDm-GxobSB0g5j2o7j2rQfXzsk-gizhBkazQF4s9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🤣
تو برنامه پخش زنده ورزش سه پژمان راهبر به خیابانی میگه انقدر از قلعه نویی انتقاد نکن، خیابانی هم کلا برنامه رو ترک میکنه و میگه از یه جای دیگه بهت زنگ زدن پرت کردن:)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/Futball180TV/96343" target="_blank">📅 10:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96342">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86220511a3.mp4?token=mCtCYC1OFHKW-rQwoL1zBCFInJaMaJA2Ldb-WRxtDMMikAjv9TyGem_s3DdPaVVWbIiQRUP4fp0KBLEMQliQTY9kxozXKhh9qYlDUfBMX2AWvpIGciKetiRejln-IZJyRZCLytlugiLvp7H7rVVpPBnElC7EHB8GjqwnROHZMXqA4ye9zYiQYhmaqLTQHL-5Y5mJk1l_sBj2kfONsBSTTGKDC6Esx0PqbL1Uyf16RLRNcIC-6iJd_PgcBgVgg042uKSrl-TmhMd660hUojiqYwl-EwV2P35PwwCWk_tNT7gwTHOYilQ0aX2ZqjCfCN2_pcMf_LYbTjvf9g2yWZnCOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86220511a3.mp4?token=mCtCYC1OFHKW-rQwoL1zBCFInJaMaJA2Ldb-WRxtDMMikAjv9TyGem_s3DdPaVVWbIiQRUP4fp0KBLEMQliQTY9kxozXKhh9qYlDUfBMX2AWvpIGciKetiRejln-IZJyRZCLytlugiLvp7H7rVVpPBnElC7EHB8GjqwnROHZMXqA4ye9zYiQYhmaqLTQHL-5Y5mJk1l_sBj2kfONsBSTTGKDC6Esx0PqbL1Uyf16RLRNcIC-6iJd_PgcBgVgg042uKSrl-TmhMd660hUojiqYwl-EwV2P35PwwCWk_tNT7gwTHOYilQ0aX2ZqjCfCN2_pcMf_LYbTjvf9g2yWZnCOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👀
آقای‌هری‌کین امشب لاشی بازیو بذار کنار تا این طرفدارت ناراحت نشه
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/Futball180TV/96342" target="_blank">📅 10:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96341">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a81f32bd6c.mp4?token=veH5U7dTmPDNbCd-nrafusjZ11hzNXjLvwd_BumC8RTBuQ2ZGqvnWIM92yGNimu707JYxoVVvF3UClRgPywA1mEkh7N3MoGMPNCTBMsqN9DEpf-P6QqPnL1rI0S84OaxcI3a4RZD-uEBkAZWVaVklx4JVuo4pTrlyeMjQssxTwwXKFYlc9PAo0jPfqxtzLRz8yeL4-m8PRHMTS4E28rNBjz0fBQZ30wDqwYgdsdCHOzkiBhQNpaWLBKH3tAyaLBv0fE40Y6CML8LLBNEkqF_optmdhuprknkPzt7CweI9dCwpflCckYlBqtlhotvPAB1gD3d7Mvi8Q50JaBIAxBcGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a81f32bd6c.mp4?token=veH5U7dTmPDNbCd-nrafusjZ11hzNXjLvwd_BumC8RTBuQ2ZGqvnWIM92yGNimu707JYxoVVvF3UClRgPywA1mEkh7N3MoGMPNCTBMsqN9DEpf-P6QqPnL1rI0S84OaxcI3a4RZD-uEBkAZWVaVklx4JVuo4pTrlyeMjQssxTwwXKFYlc9PAo0jPfqxtzLRz8yeL4-m8PRHMTS4E28rNBjz0fBQZ30wDqwYgdsdCHOzkiBhQNpaWLBKH3tAyaLBv0fE40Y6CML8LLBNEkqF_optmdhuprknkPzt7CweI9dCwpflCckYlBqtlhotvPAB1gD3d7Mvi8Q50JaBIAxBcGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🏆
وضعیت قلعه‌نویی بعد تساوی با مصر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/Futball180TV/96341" target="_blank">📅 10:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96340">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97e7871462.mp4?token=fR7-GE1cpTGmgz3h4bupssXvaJOx0V8z_5G9y34Atr6iEisogY4BkVguRXGYMtjKjyil1QaT5Z9VNIUsMm_kpKkwAv998erw9dVQ8mARj3CGFuzK_xchGQhnfNjNqpTV4Xukzt8YpSDJDgK0ZFlhdWVdIe5hetFlqfeVGmY7fK6FxFleJB8h3SzAC8H6hEB7Sm5pfhNILS3PfOtyK3Km_F6SbP9aKhaNl892kY4j3JsZt6u46GSF3gIF7qNnzQX7HpcMlvOispLAOCfvUAMhbYvJ5DyimR77fqzGy6CFqk1b9Idp31w81IKtIzCeJKUqoNAG3NGSWnkokl58PTJVpFG15rIhwnWfCbId07TJCSXrwA9LRTY4J6sNqCVr4CfX5ksLr6l5RONmWBfuMULh5Hk-EVSecxsFkZyreGy6ptxsrOLSpCCUv83IZCiK_Q1CxlPQgBn1tM-5-oZGuP3cGj9XVW5pv4PD0D0NUJ6LnnNJ0DGF_gMmhLDDhhoSXB7KuCYeT4afOEvogCvVUmcyYqcFO0x2P9oYKqAoSA38cyX5uF1tUWrcOKsJMzdUu0Eti-C93pkuUzlCRpER9XhnzUlqJiFLGRiD_ngn_IT5vMIYz9LIRWSDA8ko3hLcrAyvNsEQcFdJsmmzUm7rBEfkRZSSbmlqUqsBAE_WOh0I708" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97e7871462.mp4?token=fR7-GE1cpTGmgz3h4bupssXvaJOx0V8z_5G9y34Atr6iEisogY4BkVguRXGYMtjKjyil1QaT5Z9VNIUsMm_kpKkwAv998erw9dVQ8mARj3CGFuzK_xchGQhnfNjNqpTV4Xukzt8YpSDJDgK0ZFlhdWVdIe5hetFlqfeVGmY7fK6FxFleJB8h3SzAC8H6hEB7Sm5pfhNILS3PfOtyK3Km_F6SbP9aKhaNl892kY4j3JsZt6u46GSF3gIF7qNnzQX7HpcMlvOispLAOCfvUAMhbYvJ5DyimR77fqzGy6CFqk1b9Idp31w81IKtIzCeJKUqoNAG3NGSWnkokl58PTJVpFG15rIhwnWfCbId07TJCSXrwA9LRTY4J6sNqCVr4CfX5ksLr6l5RONmWBfuMULh5Hk-EVSecxsFkZyreGy6ptxsrOLSpCCUv83IZCiK_Q1CxlPQgBn1tM-5-oZGuP3cGj9XVW5pv4PD0D0NUJ6LnnNJ0DGF_gMmhLDDhhoSXB7KuCYeT4afOEvogCvVUmcyYqcFO0x2P9oYKqAoSA38cyX5uF1tUWrcOKsJMzdUu0Eti-C93pkuUzlCRpER9XhnzUlqJiFLGRiD_ngn_IT5vMIYz9LIRWSDA8ko3hLcrAyvNsEQcFdJsmmzUm7rBEfkRZSSbmlqUqsBAE_WOh0I708" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
این یارو هم از شدت خوشحالی سر گل دوم و مردود ایران نزدیک بود جررررر بخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/Futball180TV/96340" target="_blank">📅 09:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96339">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🎙
میثاقی: اگر بازی در لیگ خودمون برگزار میشد، چون هوش مصنوعی و تجهیزات پیشرفته var نداریم الان گلمون آفساید نبود و برده بودیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/Futball180TV/96339" target="_blank">📅 09:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96338">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03b41f5781.mp4?token=opl5hkDbMMBWreOm269f8m_3O1qW1607lvZ3_CwXb-FCEVNVcn2QNRzwXEJBTDkJ9gY1yGsxZD2ZVvzQ7Ds2WPExs-xUHrAagRLOvjjHnkKW-IlpP4l3iQhjspJeL4Uqm-GEW-ktXzd51lC2K-6cdIL3HwPxNKgbVGky7TqvGgbR6pNm5LbFfioxV4RYoAPKCSGajppmc7ACu19nQGTsGUB22M81A9yMyahU-kHuSbo7eLk9Aft9-gqxS7yqXJGRPSCCnAVG4LKakgYC64CxHM1e2ny4i4g7YvHG5HCsv0ldSvcz3OiL6XLFG6n7I3mSHr_SyHSAlmhbOfd0Wdw6sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03b41f5781.mp4?token=opl5hkDbMMBWreOm269f8m_3O1qW1607lvZ3_CwXb-FCEVNVcn2QNRzwXEJBTDkJ9gY1yGsxZD2ZVvzQ7Ds2WPExs-xUHrAagRLOvjjHnkKW-IlpP4l3iQhjspJeL4Uqm-GEW-ktXzd51lC2K-6cdIL3HwPxNKgbVGky7TqvGgbR6pNm5LbFfioxV4RYoAPKCSGajppmc7ACu19nQGTsGUB22M81A9yMyahU-kHuSbo7eLk9Aft9-gqxS7yqXJGRPSCCnAVG4LKakgYC64CxHM1e2ny4i4g7YvHG5HCsv0ldSvcz3OiL6XLFG6n7I3mSHr_SyHSAlmhbOfd0Wdw6sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
وقتی وسط سیاتل تریاک ناب گیرت میاد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/Futball180TV/96338" target="_blank">📅 09:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96337">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_GD3r2s6oM1hPIe9N7M5XVwkqjpp-zhj79iHG4jb4iRxgr6HeeicQOS7vhS05T9-P9qEcJmSjhLaxqWXI6tPBOcWgFzMcSdM_x1YdCTrWaQmpOtXovqIZVCGtvMnnIyvlecHqu1qDuGGRXJhWWJ9P0aG8Q3eBF8hUJtPFvqnC8z3klMOVvFGezpGL9x9aBsOJ9R-z7q7_I99x306tyG54RPCHCnumuPQkmVoi7exUWlmzI4dYl3mHnu06wBb51IXLU0GPDbRP5JJ6_-ebff7TZpEtE3NKBDZ7PJmhZKpdruTgDFzmXEeWbGm08pOUHuTDkG3IuOjq0iYoAPbnB3Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اتاق var بازی ایران و مصر
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/Futball180TV/96337" target="_blank">📅 09:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96336">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzv2A6m58ojHdIGY4a4l9j_RWbPaJ4vLs5xOjpd49PEGFfsFI8LPsTu7GFxA0tFNN5G-s-q7WeMovpXYkcktnMX7QuxvkB2ivll8I-jfat7XErz9FMhhJlO662p-4EIa5yBD5IgO2WfcsrFNDlEyBk8OmgwFs94awpLdxkTAe9Xqh_U27tpI-rNQ5iqcgb5SqYOBZ0CUJFbfk_n4tHn0crHm7XkczNuYzA03KRE760XD_JBBCpz1SDYO0EMbCKCBAtzmi6ya30vomahwNlfhQY7nMs5ILSaStCwtLAlk14ypg2JsO-xmi2MeQIa6Pa3y27NxAgSRKNlgPuqMh9QrjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤣
🤣
تفاوت‌سطح از این عکس مشخصه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/Futball180TV/96336" target="_blank">📅 09:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96335">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57704b3690.mp4?token=TyFdyfw334wbLuDdV5TW0h4G-TEXEt_VfgsuoiIZhBzhuRAPTmUJa4AYbboL2WPi2gZXJRTHKOQth13Gt2PQ8J_yOHpECRLAqyxOo4pBzuNw_mx7R14-aA2r3nsvxl8O5O18Zje-Iojedb8yjI02IlMdr2szFR_bGs-MX6z2KqmGhV87jor7O3TZHg0dzldK2WsXSVN1EEfbT0RySP-zBcyiYHUlLnVwA53ak5xRGF9ZWZLMNW2Q9p56X6vACQYcwtMn5c0t6oke6bbOvJLtbCt45cOgZ9hoHHT_ceGJJYv-2whADqsIu5GsZSTOB8kW1yM90j6BzMauL2GHz2h3rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57704b3690.mp4?token=TyFdyfw334wbLuDdV5TW0h4G-TEXEt_VfgsuoiIZhBzhuRAPTmUJa4AYbboL2WPi2gZXJRTHKOQth13Gt2PQ8J_yOHpECRLAqyxOo4pBzuNw_mx7R14-aA2r3nsvxl8O5O18Zje-Iojedb8yjI02IlMdr2szFR_bGs-MX6z2KqmGhV87jor7O3TZHg0dzldK2WsXSVN1EEfbT0RySP-zBcyiYHUlLnVwA53ak5xRGF9ZWZLMNW2Q9p56X6vACQYcwtMn5c0t6oke6bbOvJLtbCt45cOgZ9hoHHT_ceGJJYv-2whADqsIu5GsZSTOB8kW1yM90j6BzMauL2GHz2h3rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
قلعه نویی:
شاید خدا داره منو میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/Futball180TV/96335" target="_blank">📅 09:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96334">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaO8EhM5B80sGfwIB6y6qTyCcQKS2HfoIfPa_WCAaPQM88E2nOZTFUVqGiENC1BV-nf-XbigMjytLtzm2qTfy-aCZeruPwycOnsxmufjOMrCQnYO491yxunzWv6_CVhrqB5xYHkcmt5F5Zyc59h6L6HWygIBihWylcidoeTV99sVZQB1ljje17bHfWt6Dtl-HrGM4dPtTQ7_2gcIIUHquyBwEYCy7_9pKhH7vWcHlYviPCzbeGRJqGOvi54UQJmYRNCINi5Zm0bAPNjyi_3s18s0Bt6A0PBDngftriuW8cBoV2sbBQJz8I1f0XaRpW6LrWxrRnm9UCMbLaq9kWaKWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک حالت از سه حالت رخ بدهد، منتخب ایران صعود می‌کند
🇩🇿
🇦🇹
گروه j بازی الجزایر اتریش باید برنده داشته باشد.
🇺🇿
گروه K ازبکستان مقابل کنگو شکست نخورد.
🇬🇭
گروه L برد غنا برابر کرواسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/Futball180TV/96334" target="_blank">📅 09:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96333">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBp1Ke1bDhQO0353vPqXszrba99ihWUAPILOdavfouG9yx5KghNLhg5pFMSmE4h7Od_R8CW3B6F6cjIPTqCURBtANrS-6bEVeHVrFfh6IH7_BAF72087fPIDm2U-odmD5s4kTHCAvtb03Qn4CNxQus2fXtO62ssePkDcKn_k4CwD_lmeK9Int3gAhJ4u1A3FKn00T2La9YxllphRf81SOkEkqVoZWA7Z8SN_eD2f_Y7N7Ez5bKU3ShbMH3hXTSDMv-J9Z0Qkooc-Du-iJW69m76uWb5vmNsOLQnhR40uSFshk0gj_NYNFPjcC76vhA5k20ZfQ6xPYSWz-PmA26_n8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
جدول‌فعلی بهترین تیم‌های سوم مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/Futball180TV/96333" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96332">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vc6LtWsYWrHzcdFH0tu0AO-A8dJ_H--X4JrtsOdV2aa4KmTGmI9oTdRcbeVjJ6C7gswxV5wZSV31ebtz1KsA30Qk_92HQI4IOsEGjGIhS-mMjBk-4YS4iJB6csJVHXweePL6yboT98tFecchrtmfAT8oPe7Ojm5TDaYnzIb272W7wFJnX_hmi-3Uui2JjNsKsj2LEf2EqMcqRi7F7EIaaZ8fAPXJoxs95jx7lV2f9oP0ezUibkm1AaXutufDESHVOoAD0-4i_HJhrd4rJaTW2HczVFRj-N_8BKxAryD81ROj94iMD81cpVIgCowvWdwV41JBIINK1Uz8PV9YNnYAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خلاصه ی بازی واسه کسایی که خوابیدن ندیدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/Futball180TV/96332" target="_blank">📅 08:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96331">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dnsk_tgARVa-AfZKJEXZTQi4fJYqpWrfwfThj4goLTOEEe2kYfui3C2mDYGVw3TtO5MJuYvBGgX-TzY8Zh3h1c268AEMNC5qXLSQ66ttTNBEmMyuDqREDuI3T_NmYTsojdC4JmH3HE_IdelLP0NFhbo5xK0tybZ-obNkUVklZ5WTIlsHi3Bo1LQFTz0j37TVYxoa7pdmywwGNEpcC-0_733N4Sjd2z_O-NArWWt0ZKZnlhrewIkM77KBHKekvS29kC_LdV8HNSz8_vU_219bO5qlpLAR9le347jDlahFL54R5AuEeeOVLGDW8ol0JzXybLCRz4Nnn0eWtZcYOBkvyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
سه‌بازی حساس برای منتخب ایران:
🇬🇭
غنا - کرواسی
🇭🇷
ساعت 00:30 بامداد
🇺🇿
ازبکستان-کنگو
🇨🇩
ساعت 03:30 بامداد
🇩🇿
الجزایر-اتریش
🇦🇹
ساعت 05:30 صبح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/Futball180TV/96331" target="_blank">📅 08:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96330">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grHkbGMW-Qtl7ZgXxc-al7zruZXNP6AXsn32FHu0uJno-kVSZi4_R6fLqDKKPjA3pOMmapJg1NMg5iVFDEVpnfiRTZ3m9oFfSvDSj4ZcM_gQAOPPrlHr1r-iTkkclCGgf_CJU_Vz7SXZiHA4DKqs8HPCLDqgnwO1HM3fm9mR48sNc3CkW0NoioZ9mebjGSCalGosiCO6RLwnwEoJ244FzjnTihTWpMwBe_fALX7hhej3N_-WeKrFH0QvFP0tR4N3t6nN_3z3tiu7roQH9L4UD4iyCdHnxYQ8T0Esv8BFxbRS319y0tpDwSD24ATdjvxr-O5lzUuLh8hu2fqTiZwvbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤣
جلو جلو ذوق کنی، کیررررررر میشی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/Futball180TV/96330" target="_blank">📅 08:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96329">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
یک حالت از سه حالت رخ بدهد، منتخب ایران صعود می‌کند
🇩🇿
🇦🇹
گروه j بازی الجزایر اتریش باید برنده داشته باشد.
🇺🇿
گروه K ازبکستان مقابل کنگو شکست نخورد.
🇬🇭
گروه L برد غنا برابر کرواسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/Futball180TV/96329" target="_blank">📅 08:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96328">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
یک حالت از سه حالت رخ بدهد، منتخب ایران صعود می‌کند
🇩🇿
🇦🇹
گروه j بازی الجزایر اتریش باید برنده داشته باشد.
🇺🇿
گروه K ازبکستان مقابل کنگو شکست نخورد.
🇬🇭
گروه L برد غنا برابر کرواسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/Futball180TV/96328" target="_blank">📅 08:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96327">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-pj9TUNSjHjb6K4StXnVQX4D_pMT9CAWN26mkwIL22TNX1q5nY5K3pKp3JDE9NEmkFjODP3KQ0lMPA3hBEvm35vAkRj5GPTz7HZnPylSCtjx5IDtoTnKcqkLWoKj8xIkg0z2jRnkmdYU8IJxW6PiFk4ekMmnIsrZLoFt0WfRPXS2lIiSqkFFANErYSpUI8C94zX_0vBfznJUyWuSCYcolhxmRWcSjQuPXU_gH30z_rqMOIuiPOYYMTtGDsTfw5PX9bfRV-0rQNbou66pIEj-mgMgqEYAeZShhUkoF77trH95FDqfIX1xdH0TrGZd8D9pDrpYPxaubeI-jCr1njkdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله یک‌شانزدهم نهایی جام‌جهانی
🇪🇬
مصر
🆚
استرالیا
🇦🇺
🗓
جمعه 12 تیرماه ساعت 21:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/Futball180TV/96327" target="_blank">📅 08:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96326">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fb6mSE-vbN-3dTh4dtSzX5563YJUH0JszzSZpupKl5RNeCus2DQBxjyPyJt5RM6V7tx6RagoI7BBvjQd2fnrLxN5cYlVHWbgA2VraPiFDiXwSiqDGutmd5KmQIuKU3ccuR5ue-pRBt4T3PD7zcgk9hjmXXUn5LHGVshFNHj3dpWevp4wYhNOf8M-wHnUWl6Hk-AQiUdNtwaXq-pc1qj4_IBZzLx68h0KYZQZz2-zOqFnFuq_g2Qc9XYATFH2VA-P-VOa6b8NHiFK2jaEn8aDpB7XZYeEnF-IFCPZ991PpsDAh4wNHwOQtjrA-mjhZVqIuZCFpTspKxD4h1JKQi-26w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیم‌های راه‌یافته به مرحله حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/Futball180TV/96326" target="_blank">📅 08:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96325">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PP13Vm8TwsReYLQwj-AGCrK5GVs8AsVCffl7pOa3RVU0t9Y5_gBBBN8VRAMVf6e6dYSd2eYz6IOGljKOetewG51hlXFC_ZRU1GxIYw3eT-RqZNzuwge33_b5qjxbRCyaIaNc7hsPipusgEwKQ1gMzEcNChO6W38z3nCxnnzr5YILUOWvtYULdHIc7FiF_XaWmtTUbLnszFujA7szkI0A1kIt-ZPL6fp6Zis9XOHE0VowxWJNPLwFvwlL7Qu85N8YM3fdAZYSISyhzenGv26LZSBqT1zWXt5vWHLOriQW_FBbO17QKtYB_F31sQNcb7WtrydQEKJ15XZOdB2sxpIjDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ بازی کثیف و زشت تیم قلعه‌نویی در روزی که برای صعود نیاز به برد داشت؛ منتخب ایران حالا باید منتظر معجزه باشد
🇪🇬
مصر
😃
😃
منتخب ایران
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/Futball180TV/96325" target="_blank">📅 08:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96324">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🇧🇪
تیم‌ملی بلژیک به عنوان صدرنشین راهی مرحله حذفی مسابقات شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/Futball180TV/96324" target="_blank">📅 08:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96323">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNjTYwhxcaTW2WjnFexD2vuWAvdAomC15YxcjJDr6PjjbhSP3t5TVoIHA4nVDP_KxKMUtQQcyPRUAScbB9p5qqME7phGtlKE39tLaEDZxAFq2h2ynLLsvSdGKkNLU0qt5aRz9IBa_5WDYPGg4zR6PHbnV4ALM8wcOe2EEjKRwhFsONSF9EB4CMHJIzHG3ezCw2tp-6cAN5BEqpLb0Ng8vtqW1nqaR2UC0K5aocBgLDjGLlqmWih44_bM2rpYsk3OS6LExkCAH_mR3SRk2uY39TTZuX2g9srDN0g4n_9xW5A5x9CI6tOoE8M1lBg72AHCpREgE2MuXN7CG0ysT6pGlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ بازی کثیف و زشت تیم قلعه‌نویی در روزی که برای صعود نیاز به برد داشت؛ منتخب ایران حالا باید منتظر معجزه باشد
🇪🇬
مصر
😃
😃
منتخب ایران
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/Futball180TV/96323" target="_blank">📅 08:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96321">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گل رد شددددددد</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/Futball180TV/96321" target="_blank">📅 08:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96320">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گل رد شددددددد</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/Futball180TV/96320" target="_blank">📅 08:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96319">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بنظر گل مردوده</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/Futball180TV/96319" target="_blank">📅 08:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96318">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">صحنه رفته وار</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/Futball180TV/96318" target="_blank">📅 08:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96317">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شجاع خلیل‌زادهههههه
🤣
🤣
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/Futball180TV/96317" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96316">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">😂
😂
😂
🔥
🔥
😂</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/Futball180TV/96316" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96315">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گل برای ایران شجاع</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/Futball180TV/96315" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96314">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ایرااااان زدددددد</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/Futball180TV/96314" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96313">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گلگگلگلگلگلگگل</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/Futball180TV/96313" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96312">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">۶ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/Futball180TV/96312" target="_blank">📅 08:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96311">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">جهانبخش رو آورد زمین
😂
😂</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/Futball180TV/96311" target="_blank">📅 08:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96310">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پشمامممم چی گل نشدددد</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/Futball180TV/96310" target="_blank">📅 08:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96309">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بعد بازی قراره رسانه‌ها قلعه‌نویی رو دوتا شکم دیگه حامله کنن منتظر باشید
😂
😂</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/Futball180TV/96309" target="_blank">📅 08:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96308">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">منتخب ایران بخاطر وقت‌کشی داره هو میشه
😂
😐</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/Futball180TV/96308" target="_blank">📅 08:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96307">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">قلعه‌نویی تو این گرما چرا کاپشن پوشیده
😐</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/Futball180TV/96307" target="_blank">📅 08:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96305">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مصر صعود کرده کیرشه
تیم قلعه‌نویی ۹۹ درصد حذفه داره وقت کشی میکنه
😂
😂
😂</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/96305" target="_blank">📅 08:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96303">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بلژیک چهارمی رو زد</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/96303" target="_blank">📅 08:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96302">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/96302" target="_blank">📅 08:18 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
