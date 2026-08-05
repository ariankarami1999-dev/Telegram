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
<img src="https://cdn4.telesco.pe/file/GBIFt5_l3E5RvyyurTKJXJqGSAxjUXZ4GtnuSkx76JLzPmlA7xjEdc551rw_WB5mWZSBIliwPzZuql9725tHLiqDL1dMvC0W4d8VeOVZ3vtqym1J35OId01CDRp9odD1MZcqGe8GXK249aiEHnVIjcH8hbHgXxkP6ga1A05gxv2usVDQcsmJzuVmuGGHbJIRAe9dq3-bjscYe5KewdUkuelfl2NqiuwmJzV-JuJQ4WmYHTtUctm1mv9VulBt2R4GPAOosvH1SaSD3IPbFkUVbaR2UNOraSHeOyyfq1GzRHU1x0u4nFqYU3gw8Z8LTYlc2eDAWIUVkf4fVjw2-QjY4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 628K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 19:56:33</div>
<hr>

<div class="tg-post" id="msg-27160">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tq4YSwrtc709Q-GRM-AbWYs-OvJahaTh07knC3RmmnNUJmTG4TdsMZCITjza6C81dG88hWrSMn8iZa3BpCTXqnguM_pJeyYdt3MNHXzbXwCHf5CC03BlHcpvrO21-GoXWbAuJIt2roF-RUqXqdGTmpSiYLW-xyScwsNpdrhwOgC_l5oypZbWaLicJOP5gAGr2AtNAw_mWmpfRQb7JgNZ_FdJd5xa72_D0gpMntl7JpYfBYJSDc39USyqve9vs7ri15oDQgiRP9OPIbrL-uuEKxB8kipquJsDRp4n8KIzse_UL1Sqmhgaxz9LB4cr3z_kZWOMHqRiF1wOw4w1c4B7IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
باشگاه تزابزون اسپور ترکیه با انتشار این ویدیو از محمد صلاح خریدجدید خود رسما رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/persiana_Soccer/27160" target="_blank">📅 19:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27159">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALR-zXRd-jImnhoRyur_-cfzyl-E3E1HPSKbLsSwrIl-lZVTLucqR3lR_JcpUrKfKRnvhrDQz9LgvlPloezpL2vXG8so2eZarga8sv3rj4wr-u_cfm1JzCWrICVoR9UivHJuYZgFxX8RwDAJNQP0Z8bRiTq-NNZ2B2wSGn1tOjIJQy1SO1IZrMLERav-A3FSiuwg2CrZMrApBDSQGNgUoGtFwXYmmavBtCMB1YDNqIHy_Lcp_kOyKed9CTiEBIwZdf00WfOd-JXYEpGTQXRbLId1DNFQC65CDvCSqhIOMOIdcuD_8KzDjdCCPdKJW4V9om-ZqSpVxYBJwnfle-9hWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بااعلام باشگاه استقلال؛ رامین رضاییان ستاره 36 ساله آبی‌ ها بعد از 1.5 فصل حضور در این تیم جداشد. مقصدبعدی او بزودی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/persiana_Soccer/27159" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27158">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mylT040P_f6prCXpJX3P99zTYiQCT3klEDgQwV4akUhnxaluWuXrsj85-bQ8Cn14mX1IFR3YdbNn4Lb49Aq9au-USERRIgRSFLqIzdsjbPy0Jisnz3n5ZfxnFs6MNS022IPIJ8K-SakLpjiB5ooCIawL5weV_ggHiOvb3jzP6UOtiX1WqiLQr-IaUgsbhSiEAlN1tPQMswpNgScKCFCx7vGo-Csy77ma6T9CRnuzbrIqSDylWOunvtcHBVdLxS_9yN-i-fUNhYD9W6jbhWRVEOaYA4Pk9VMh5xnZV4fE1XhSryZzls9S_D5UcexwPNneXkZK1N9KrFoQfm1jJQKMfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ امید عالیشاه کاپیتان سابق پرسپولیس باعقدقراردادی 1+1 ساله رسما به تیم گلگهر سیرجان پیوست و شاگرد سید مهدی رحمتی در این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/27158" target="_blank">📅 18:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27157">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToFP031Ikh_m7KSQGopUT0FBO68R-tDwBXK9Dfo6tB913h6zX78zuaq_iF7OBSjjIgcbFfovE-4audo22XxrGc6mKsJYJvfVviY887gtWgpMyDsY4cknJX6vC95RVaE7KQN8rIIxUCnyyyIDW38JQyz7NDIXQukFEOfYGh3jSEdjfTzzyx0zfozQzI4LE1pF_tSwtAqIKheflS-MvwnK6EJKGRt6hrq2eKoWI2GsdHB14qz9AVkX5agPLnFBFs2xJJrchhIQeSTmtWN9Iu0cOCimRKCOoQ7TLi-POtJN1OGuAuHf6beGJxbVT-x1RjtWUvSSFIMzM2MwmXG-C1B90A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
خوزه فلیکس دیاز: مدیر ورزشی آرسنال به اعضای این تیم قول داده کارهای انتقال وینیسیوس جونیور به این تیم در حال نهایی شدن است و این بازیکن فصل بعد قطعا در آرسنال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/27157" target="_blank">📅 18:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27156">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BT9RLvw1mF5so-ypUsbGHFP5GmDz5GlI8b6TmLVYDbDH2mNyWN7aoxWXz1XLHMsxGdnHVMx4E86CvBfc0A-hk-Q3sbcVIECQcScdpfKoSUj0g03aVoWJVgDVptPrGf1IAPD5XwWuLOP5tKTeuqAgX1qeluO0hbdOszRRG8aEQV6vF24iujXDX_lJ60RYKaWlIS35IUtROCgQ0jSyY5JPUwH2rWAztg4yRCrYlc880GLq6bBs1sV4LKOrXGSJEZLJdDDomvaYNbthRVMX1MTMtnISeCtdf7Cq_76Cw3xMnq3GZrTaj4bQMKhiyDk5kh5XBYk9B73culuVAgH9sffc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعد از کش‌وقوس‌های فراوان؛ امید عالیشاه برای عقد قراردادی دو ساله با تیم گل گهر سیرجان با مدیریت این باشگاه به توافق نهایی رسید و بزودی از او رونمایی خواهندکرد. بعد از اخباری و گودرزی این سومین خرید گل‌گهری‌ها بود که سید مهدی رحمتی شخصا با بازیکن مدنظرش…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/27156" target="_blank">📅 17:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27155">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITh8KjcJUu9qOKpV7ym3MWwR23xxMiZu83NvCyGh9nizmNKtK9BZj2S3ppFC0Z5Te3R0pB4jWKW48Oa37o1Zwl-qjWMsUC506vyv3fCDwjFONhlqpNuHB5UWW1962sHujwTVLqBanvsEBv29xZ4_zZAna3aqGMyPj2Ye8auIsnOSoHVpt3pw_jmniREF3BJhiqHfbwEIixw2USsovAPfdG37M5pPnqet_gd2FI8Zrgj4yFk81spLJ_PScGSDjsQHMG6fmHEcYHlZUvmHtsDaTr0kUKQdTttGL0A3KTw1z77qoDY7mW6zy3Z12fXW3KEVNY4oKWYg7xVNQyFj2cN4vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های رسانه پرشیانا؛ امیر هوشنگ سعادتی مدیربرنامه‌های رامین‌رضاییان این بازیکن رو به مدیریت باشگاه سپاهان پیشنهاد داده و مدیرعامل طلایی پوشان اعلام کرده در صورت موافقت محرم نوید کیا آماده عقد قرارداد با این بازیکن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/27155" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27154">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4LFu_JNrj-L4auhMasA-YKIS6XROGekPkT5vuetmUua-X6qqXPA798MhSykBoA4qgfrsQGrkJDuvOnRac8NkqmEP_7hOfAXr3kTHn9dLnMuKhYV6-ryQCcOYd95xpLGA2LdanGZYez2CzPqUbmOBkpy63qMJW-EAioJF0A1R0xLItyeEEurIODzxiRF9uQ7VkQuyGTVveog_EQPMAz2KDdoy5gVL5k8k6YosOfQtfEuK40A7oYjmfVEUxcpAHoegs-O7ca5yIdNyvnNcVulLjHcrJZP0QfDj-rFZKNEHqUuLAOujb0B9kuRr3S4HEm0aFtw2QzUumvbgVTXOh7vsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیررسانه‌ای‌باشگاه‌ماخاچ‌قلعه: ایرانی‌ها با کامنت‌های پرشماری‌که در اینستاگرام برامون داشتند حقیقتا دهنمون رو سرویس کردند‌. هر باشگاهی که با ما به توافق‌مالی برسد و حسین نژاد نیز راضی به این انتقال شود این بازیکن رو به اون باشگاه میفروشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/27154" target="_blank">📅 17:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27153">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b7185f121.mp4?token=rGok9M0MeRLQHf9hnxpzm15qvUg8nq03DXhJLRrYfuJWeJkDmTAuNc7caf9oTsTedQB-pMrF3D1Wa2ggHGNnjuY9ZysShymTKrPoFiD_W30JjCvqqqP0PqXamgiEWU2PjCzbNvpZOk8vDJQXCzQQKqw51EDKyIgv1pUeyF1i8iuDEHteN_qeEplRn1Ta496naCJP0KrCMjgDNCJJtInj-w0DBqWwjOcz0K1r3F2YioCJ7lYRGWhlOqUTA9o8FEPowmlCCUm7wgiNdp4IrbxHMSuBJdrcN_EeHt2sL3N_eERU0Vy8xIb5kI978bFrTW44HZuiughK0V6fb3bS61-xSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b7185f121.mp4?token=rGok9M0MeRLQHf9hnxpzm15qvUg8nq03DXhJLRrYfuJWeJkDmTAuNc7caf9oTsTedQB-pMrF3D1Wa2ggHGNnjuY9ZysShymTKrPoFiD_W30JjCvqqqP0PqXamgiEWU2PjCzbNvpZOk8vDJQXCzQQKqw51EDKyIgv1pUeyF1i8iuDEHteN_qeEplRn1Ta496naCJP0KrCMjgDNCJJtInj-w0DBqWwjOcz0K1r3F2YioCJ7lYRGWhlOqUTA9o8FEPowmlCCUm7wgiNdp4IrbxHMSuBJdrcN_EeHt2sL3N_eERU0Vy8xIb5kI978bFrTW44HZuiughK0V6fb3bS61-xSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه‌دو دیداردوستانه‌امروز درتور پیش فصل؛ توقف شاگردان‌آموریم مقابل‌افعی‌ها و پیروزی راحت سیتیزن‌هامقابل‌کره‌ای‌ها در دوران پسا پپ گواردیولا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/27153" target="_blank">📅 17:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27152">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs4W0y1Q2XkgcCWujiwjapIAskiKC49QMX7I9GNuTEiRHbYaT0x8PO2EHrp2F0KrBTsd6vEOJl8uvHYCnXoUKeW4sj2j6cwpJQ0XQ58CtTmW-X2GkFzX9J9mVp_k_Vw4VGhzWD80gnWjVuQYC1x0kUiiJVv_deKYWJl5HBJWMljVoc7x2pKiDZhBK_wO6cqqan8qGgwJAadZk6wRJDv2NBBA44Mh9Ul3hFp6qP7ZGwivYP81vqsfXzb-RMpXDTvj4kZKV--qtUJn4n0_5MWN0xvEr9dgpUYlo9DUMzigDwfV6Tx0ZB6ne0la-igMHqovQedVuyKAhFuCwn7YdtB49w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛ازدربی‌دوستانه دلامادونینا تا دوئل شاگردان ژابی و اسپالتی در کشور هنگ کنگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/27152" target="_blank">📅 16:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27151">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6UYbGC5aYcIgfjwGZA1078-Vs_gqioUcWfchMaugKRP69ziWnYPks-HieWuoxAHm9CDgSI8mTbmVKcD5kWEbc-YyxcEnCwUu8xh2iiCwMiLnrG_JrQfOAL71nA_gbkSLYCYbVxtwdE4PdmJxe-D_StSbTDsypQjsfkc-GLUp0QDuYEk4UoCiTn4MaUmBY06fj6hGMbscXFaZrJYRS6LOxTkqnzjD_vb_SaQDUMqgQEthRDkCNHXjjwTQ4db1CFoHczQh6tLXeUEPPv8liEW_Zy1cAZQFnEx2xx9Y3JeQ7WBJs2LvhLxhlcQzYmrdp6QJWUst13g23AhQFjc9HAlWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
#تکمیلی؛ امروز سرنوشت وینیسیوس جونیور در رئال‌مادرید و پرونده انتقال خولیان آلوارز به‌بارسلونا تاحدود خیلی زیادی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/27151" target="_blank">📅 16:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27150">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d917f67b.mp4?token=QKmG589GxwyvpMfxFC4oZ42PWgnWncNDBZspw2pYdlSDjKrgeoELwU_dTtY4r5H7hA8u0lHN8m1YhKM_lFXVLiMTwMZ3E_k38yK62bd0Yq4iz1XTQs8O9aGtgd5ZTlyXJt7cAWYDJ_yTMtGMz9m2gicbyicUrbnTY3Bzc9a7kNE1PEq9Gs-zQCoyl29efk2vUjdvsGBx9Hm9chAeyELoUpCqJGgSwpxmu0h38bCTtRPD00ON2M5AD3bLhjA0Q40SJd9UmjiIOOaU8_tdeGxahB1NWSdLcCm9YunzOnToiuGv4F4fAikr8y0hWl_2eyTh3qhsZeFP34U0MaMq8d98gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d917f67b.mp4?token=QKmG589GxwyvpMfxFC4oZ42PWgnWncNDBZspw2pYdlSDjKrgeoELwU_dTtY4r5H7hA8u0lHN8m1YhKM_lFXVLiMTwMZ3E_k38yK62bd0Yq4iz1XTQs8O9aGtgd5ZTlyXJt7cAWYDJ_yTMtGMz9m2gicbyicUrbnTY3Bzc9a7kNE1PEq9Gs-zQCoyl29efk2vUjdvsGBx9Hm9chAeyELoUpCqJGgSwpxmu0h38bCTtRPD00ON2M5AD3bLhjA0Q40SJd9UmjiIOOaU8_tdeGxahB1NWSdLcCm9YunzOnToiuGv4F4fAikr8y0hWl_2eyTh3qhsZeFP34U0MaMq8d98gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
🔥
فقط و فقط ۱۱ روز تا شروع بهترین لیگ دنیا و رقابت‌جذاب تارتتا و سهرابیولا مونده؛ برنامه دیدارهای هفته اول رقابتای لیگ برتر خلیج فارس!
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/27150" target="_blank">📅 16:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27149">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sve9nRhjqYllKCS8UK_QQnDviBqYnDR2mQmDAiMeDKBS9VsQsucLfa24w-2FbrGZjOAFJ_6KyKF9wu6UZsr9Lc4mcBCk3pNDbY05KMGAA5681Da4oDtdqr-J0gv4p9zooMkNd0qQjKN9CGTMYfcKfCv5-nHszZqS9JirG99GclZLFU36SKMi-iZfcuPZxRDIQhTuHWT9C-DaE5TrkVyxemupKhbYWI9iko__45e5ANBN6bAaoGeMOVFsrE5psKqQ9OtuQNXf6uV786uVJfbcr1L7nqOF2B7YRR_qpuLcgZ5SYEp6rBAeQjXkme91C5TUPVk33w1wFV0OOitFrCEt8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
چه خبرهه زیر این پست محمد جواد حسین نژاد؛ استقلالی‌ها میگن بیا استقلال، پرسپولیسی‌ ها میگن بیا باشگاه‌ پرسپولیس... اون‌ ویدیو هم فن پیج‌هاش ساختند. انصافا شاه ماهی نقل و انتقالاته. هر تیمی بگیردش برد بزرگی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/27149" target="_blank">📅 16:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27148">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315f795088.mp4?token=LDuvncOfWTY32MvH14AdeqjgaDyOVX6eIyuzqyPh-w5YGfdWSAHi07SWXJD1bTRKuWFHdoTPqwlZddXdMEEmfU4ji4PUY5S0Sv3hbp6lyQGNsCsqotZv6ZHP1XKIknaixVygvccpv1VhPmvWvtdnMWsiYm3_OAE2l44EdDkAP2JX2zS6Bp_9umg_Q4CmiZQAqICjQRZ9tA7O0V9sNhoS4SFjc9gEpIpGF9h7AIanuR_pw94dp3uunLs0PzhrFt8s3gEbSjM1JTry8fYfq5EnRz3145BPjx2P5-34KxFmt1PdKCgKYY3s4h-feJG9hd1kwK9y6T2zePxFtz7jMBJ6KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315f795088.mp4?token=LDuvncOfWTY32MvH14AdeqjgaDyOVX6eIyuzqyPh-w5YGfdWSAHi07SWXJD1bTRKuWFHdoTPqwlZddXdMEEmfU4ji4PUY5S0Sv3hbp6lyQGNsCsqotZv6ZHP1XKIknaixVygvccpv1VhPmvWvtdnMWsiYm3_OAE2l44EdDkAP2JX2zS6Bp_9umg_Q4CmiZQAqICjQRZ9tA7O0V9sNhoS4SFjc9gEpIpGF9h7AIanuR_pw94dp3uunLs0PzhrFt8s3gEbSjM1JTry8fYfq5EnRz3145BPjx2P5-34KxFmt1PdKCgKYY3s4h-feJG9hd1kwK9y6T2zePxFtz7jMBJ6KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
امید عالیشاه کاپیتان سابق پرسپولیس بعد از یه‌ دور مذاکره با سپاهان، فولاد و ذوب آهن حالا با مدیران صنعت‌نفت آبادان نیز درحال مذاکره هست و هر تیمی‌ رقم بالاتری پیشنهاد بدهد قرارداد میبنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/27148" target="_blank">📅 16:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27147">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee60bdfdc.mp4?token=HwUa68fQeTGecnGMhZbgSc00WR3YcPHZ9ujX7AknxT9jhhO5-cy7iHpFdSQaZfYwY02N1Vk7_Vr11CjaV8eNlX35abETAyXjUvs_w85LoVPvSNcLvOGtas75-D9xqLcZ9rbh4mGvmM1uHl1Yxp802jwElJAvJ0kWHWL0ocobyDRpAlFfXbCdrysbSnW-9S4NlMqalzpORkk-F1PHHcZ3gp_0Ei92oVTMhhBicssffFgFH59KnQj2_FSiH-JQl2_q-wv3n5VwNfG6hbn_3nRODhyKiBmuB5MNEnI3u4hOpX3VosiT4EUTxjMCKA2mgnV_ubXD_zS22spPYl9xsQ6qvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee60bdfdc.mp4?token=HwUa68fQeTGecnGMhZbgSc00WR3YcPHZ9ujX7AknxT9jhhO5-cy7iHpFdSQaZfYwY02N1Vk7_Vr11CjaV8eNlX35abETAyXjUvs_w85LoVPvSNcLvOGtas75-D9xqLcZ9rbh4mGvmM1uHl1Yxp802jwElJAvJ0kWHWL0ocobyDRpAlFfXbCdrysbSnW-9S4NlMqalzpORkk-F1PHHcZ3gp_0Ei92oVTMhhBicssffFgFH59KnQj2_FSiH-JQl2_q-wv3n5VwNfG6hbn_3nRODhyKiBmuB5MNEnI3u4hOpX3VosiT4EUTxjMCKA2mgnV_ubXD_zS22spPYl9xsQ6qvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
توضیحاتی‌جالب‌درباره‌پست‌جدید کریستیانو رونالدو در کنار ماشین های لوکس و گرانقیمت خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/27147" target="_blank">📅 15:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27146">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXsEFp6vSrYgwqJEua7GLndI6VnuCYZZx7Pb1Udd5ASz-PZa66nZ7KqUeHKoq0aaRxMhs1K_9yKXARzRdXFdegAlyDciTrpgQPOvvZun7hlMDZswBVC5kgQ3husROCuDlE_h8y6vtmDc1ftLiUsHtCsZVH54ldEZKg6MHpP81Yzkrr25XvYGsM8p0pBDtFvuY9sDqdsd_4BNqGgyasLhvudRAiTkLZNnZUgpxAQU7QqbvcZFGK9VouwwHKtf0pwOKou8OQEh5_QMSoWumUvDEsfPO7V7zzpjY6Ji6cdEeVhkEGOOz-bTke1jrjXSpb0_BOXd04oWR2mZrKTIu_m9CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
فرشیدباقری بادریافت14میلیاردتومان از پیکان قرار دادش رو با خودروسازان یه ساله تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/27146" target="_blank">📅 14:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27145">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jctbalGimfO1RTutSqhWJJAut5JOAAZanFNKARkHisVqYRTct2eC-1uWB1VTFIxy57aRnGxiP1wFktFWN7Lg5s_bBNsowFoMYdQUJ7rMufyzysBWlUcv_OXSpcO9OZNpmQnTUMRUE7I3jQawA3l6JvHhXFJ91iFlbVSQxxwU9OsnBEdVUW9mFQyT2BKEABqyrYd6JkPnGp7bFCf0fibrSxAZP3SHsY2aDa-YkRpI-8ODWBMas4uduX-nTby-tC2a_wm2-BIEPHxAI1BrGoI18SAhmbX7UTz15RyTQBZxTUx9HDbKNBfikmE0Gfzo_DHqWqMxId36Sm_nQCBu0zZsdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های رسانه پرشیانا؛
امیر هوشنگ سعادتی مدیربرنامه‌های رامین‌رضاییان این بازیکن رو به مدیریت باشگاه سپاهان پیشنهاد داده و مدیرعامل طلایی پوشان اعلام کرده در صورت موافقت محرم نوید کیا آماده عقد قرارداد با این بازیکن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/27145" target="_blank">📅 14:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27144">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09ea3c3b07.mp4?token=k4AMYJqc7qjn1jUPJgeWZEqmSEhtWBwySd1s2fV8T9LzKylHFhGgXlypFKTMa1pwqdr7PQnXKYCPrtWf1knF_f4pofp4SY5uRh6s5VAeFmIjFAPA_9moiZcH8vP3pKqdKlD8HcJYGoL034RG2Yjh0OS2n4ibIZSonmKCMQ9lVTBDim9yTh7Mh8pi0E06Xo0VL38fSk7DSP2i198ChJgbo9OggEmzF9TdNZcmFbgh7E_YYttpbEWmyyVS81GTbPWVZo5ioJjvixQjShME8xI90uztymxtw4WqjIbBBxEwiwoshfKV9sCFBLyMstEG_OSPSOrlgSfbDpMpW-Ul43lkp0AiCyx1mSQ4kbX1lAcXGzIqgG9iYkHdAmycZuXv6KWEXI2yYZHm7aRI6iH_32p6tY4WtI9DEsNqKIQVy92LZs0Y3e6MyylayTxoYW49tPwKOmkgXxtyHK-WlmM0fZdwyOQmut7koEJAYP8R2S1qWNIW_QJv65I_qrDPeJj9tlBYEWQlyaCi_ttFUZk392owe74fC3GOODifJvHX840w_3bUyRwqWCYw_7c3A-F9tyjAUpf6Zi8k-ZsR9TtGEKA0r7XFuBzCzMMwgLOjHZvFo5HU_ufMExX9xMbD5Z950yUul3LeOa_9Gj9DNmUsFgwDqjpDFeR2Hnu9cl7jOOc2PR4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09ea3c3b07.mp4?token=k4AMYJqc7qjn1jUPJgeWZEqmSEhtWBwySd1s2fV8T9LzKylHFhGgXlypFKTMa1pwqdr7PQnXKYCPrtWf1knF_f4pofp4SY5uRh6s5VAeFmIjFAPA_9moiZcH8vP3pKqdKlD8HcJYGoL034RG2Yjh0OS2n4ibIZSonmKCMQ9lVTBDim9yTh7Mh8pi0E06Xo0VL38fSk7DSP2i198ChJgbo9OggEmzF9TdNZcmFbgh7E_YYttpbEWmyyVS81GTbPWVZo5ioJjvixQjShME8xI90uztymxtw4WqjIbBBxEwiwoshfKV9sCFBLyMstEG_OSPSOrlgSfbDpMpW-Ul43lkp0AiCyx1mSQ4kbX1lAcXGzIqgG9iYkHdAmycZuXv6KWEXI2yYZHm7aRI6iH_32p6tY4WtI9DEsNqKIQVy92LZs0Y3e6MyylayTxoYW49tPwKOmkgXxtyHK-WlmM0fZdwyOQmut7koEJAYP8R2S1qWNIW_QJv65I_qrDPeJj9tlBYEWQlyaCi_ttFUZk392owe74fC3GOODifJvHX840w_3bUyRwqWCYw_7c3A-F9tyjAUpf6Zi8k-ZsR9TtGEKA0r7XFuBzCzMMwgLOjHZvFo5HU_ufMExX9xMbD5Z950yUul3LeOa_9Gj9DNmUsFgwDqjpDFeR2Hnu9cl7jOOc2PR4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به‌بهانه جدایی رامین رضاییان از استقلال نگاهی بیندازیم به لحظاتی‌که این بازیکن در این تیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/27144" target="_blank">📅 14:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27143">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBtDzqC0-vDepRGFhl9oAVmC1YU9JSoRb6Ec4F7HOkW6NGiBrGcHib4HoR_yO53zyizMz2Fbe0ekZfGeIW6AgYEvBMQSSN1Lxzx851cgB0Wa8bQPfw9vBWm3Gayw-9mK7AAms-VaBZCVjdhNUlmwrTYs4ZcMINDFWwIjXuWi0-vPYlLgzkBVzdY49KD2_Qo8z4dxecz3092EYqvkazuT9kYsCQTizRadv2zQRSRxkA2sde_ULWUuQfGK1dJhtrKYQgehAkarT4ghT4307QkuxmQFhSc6mnJD6CFkqEf3gOMOkYlt4Ta-5_vsC0GxlmW1VHvpjRq98Gl75CBWCeDy5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/27143" target="_blank">📅 14:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27142">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‼️
اولش یه لحظه فکر کردم وحید امیری رو برده اون بالا؛ لامصب ته چهرش کپی وحید امیریه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/27142" target="_blank">📅 13:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27141">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/590b770d9f.mp4?token=TNPDJHA_BKaJskEIkfR5D8ogPfbhek5A0UcIAjleAAiP39hq2ktczKGpqdQy3cPz7IsETE3YklEtKO2dSwOlKA-s7tF1vL3HwSf6aS__ibJlz60aoWiy39ZonG3_qkDbMOxshZQxu8V6MhXdj03q0L6o7GXRS3AeXd5jGbzxczS9F9w4p2zSuxvLglhif4tr4CHDBdVX9pd1eIqldVuisbnJDiK4-bReTqRno1fVuw_jLIw39FmXchBFl0XcLPGkj-qwGonvsgZRnisuQQkPZze4lHSuVxyErJc7z1q8wgAgrppvo6e_8pUepRSQ4qoNeQOvoocgdKEtI4jgdkA9yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/590b770d9f.mp4?token=TNPDJHA_BKaJskEIkfR5D8ogPfbhek5A0UcIAjleAAiP39hq2ktczKGpqdQy3cPz7IsETE3YklEtKO2dSwOlKA-s7tF1vL3HwSf6aS__ibJlz60aoWiy39ZonG3_qkDbMOxshZQxu8V6MhXdj03q0L6o7GXRS3AeXd5jGbzxczS9F9w4p2zSuxvLglhif4tr4CHDBdVX9pd1eIqldVuisbnJDiK4-bReTqRno1fVuw_jLIw39FmXchBFl0XcLPGkj-qwGonvsgZRnisuQQkPZze4lHSuVxyErJc7z1q8wgAgrppvo6e_8pUepRSQ4qoNeQOvoocgdKEtI4jgdkA9yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
ویدیویی‌زیبا بمناسبت درگذشت فرانکو بارسی اسطوره تاریخی باشگاه آث میلان و فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/27141" target="_blank">📅 13:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27140">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇪🇸
🇨🇮
ویدیویی‌جالب‌ازگذشته سخت و درد ناک یان دیومانده ستاره 19 ساله و جدید باشگاه رئال‌مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/27140" target="_blank">📅 12:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27139">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXhh0NsmzPzccmpV-leHQq2qC7Y5WfuCoaSVvLN7Hk_ZuQfN_NjtKyhhTtXNC69svZaV57hx2GcMKvPu0KpRyQj1FT1IiOiMLd5Wy4NNyUpY5ue6HUjtw1NLmLMb7F7mFl37sJ7klX366bXgF5DcUfriaJflTvAgxOqxmVo8Hp6zxHIV5eJmkuTipOqDTL9Y4_n1yX9OKguaQh_mve9v2hSzHlBUmg3kos1kaC33NuvPSFLZOYaNrGqRkaorAKOoRzkR2F4e8ZDaHW-qdGE4u8svdqn18UW0t9oTlVoTqR76zR1TRqCBhFUZKigu1-9gESRuFmY9Kh5Yl72zRgk9rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات|فابریزیو رومانو: با صلاح دید کادرفنی رئال مادرید؛ فرانکو ماسانتوئونو ستاره آرژانتینی رئالی‌ها در ژانویه قرضی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/27139" target="_blank">📅 12:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27138">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdeHYrKnzInEWhihwZverOcS1O5LXPfa9t5nXu6f7Li3mj96mGaGX9gSRCqXgk7qi0i4iWdf0kc7tZlij_5ueWKNEwFLYXe5nQWUHGDvLPPixejI3t_ObjpMSwc4W_2uCt5tDZVaPRzj48culMrbr_UKlOOOop2UDhnamC05-Bvf_yKvIRnheX07y7oQEIpwTxxzL8U8sJrZy8CJfaKDxpBKpxU9BYT_xMQvsHAuW-5rf29SEzF1ZGtshkqUVBOHW1gjcB8lbYhaVSyvKZkO6LIP_ENkerqTgtP0t0zWsD3AetQQnhIJaCNV0m0GP0YTb1pPdUiRhu9eJTqdFCfBAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/27138" target="_blank">📅 12:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27137">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNWWy0SATzYBYexkkdcuLGeC7jtm2eC2Ai8US4pKIJKu_p_JFxgkmWcREXPWSRzS3QOZhnZRdkGBJ73ZqhbazhhK1wCYWVnQGToVVgBsOanBjyb_IXyMble1BF9bSOExSyC1jlLdS-gO7FluwpERiY4kGd3CL6nenKpwXqCgQF2hMBKumq-5BRbKGDPqy8bYQzbKl6Crj1cbqJwMD3KmOLdEV6pNR9hhToxjem-BG1TEb-6B-Yv3CfQKfFRXNjY4M5Yw3JpOLYOkXU3WmAc22pjtABbdHDE8YOTrzF18YPE_eDrfX93GUG4HtfZqaz8MwW2caGA9y_tYcb5NXGJ1CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/27137" target="_blank">📅 11:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27136">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca19ec3ee1.mp4?token=up3sSObqAqszmwwiRxehwC2tXFp6NDPL4sAzhh0C0Ov40wU0guCZNovS8gIko3jMYuM_IhFifFIB66i25eEsQTKmoaaS8cUmVtX5ZUjwaqR2G4Q4BLEkKlYphWcSZGfx3QzIKFLqyYcrXFsONS7aRqR3UmIjYyx8TpCTQAMd7Vm4Epser06pc15E_z4zmAYGPJT-35GWE2_JgmvrSv9qyXYKIhE9U_BOP13C2HfMP-IiSmSXjTWl-FbY1dGsvYKo3_uPAe6K4AbLytK_6blkL0ZhgjhoYonff-FNux20MdP19Rs9sWRfC3wh18Fxrc7KZaAqx_tfECBjG3b7r9eWDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca19ec3ee1.mp4?token=up3sSObqAqszmwwiRxehwC2tXFp6NDPL4sAzhh0C0Ov40wU0guCZNovS8gIko3jMYuM_IhFifFIB66i25eEsQTKmoaaS8cUmVtX5ZUjwaqR2G4Q4BLEkKlYphWcSZGfx3QzIKFLqyYcrXFsONS7aRqR3UmIjYyx8TpCTQAMd7Vm4Epser06pc15E_z4zmAYGPJT-35GWE2_JgmvrSv9qyXYKIhE9U_BOP13C2HfMP-IiSmSXjTWl-FbY1dGsvYKo3_uPAe6K4AbLytK_6blkL0ZhgjhoYonff-FNux20MdP19Rs9sWRfC3wh18Fxrc7KZaAqx_tfECBjG3b7r9eWDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تموم‌ شد؛ صلاح رفت سوپرلیگ ترکیه! با اعلام فابریزیو رومانو؛ محمد صلاح فوق‌ستاره مصری 34 ساله سابق لیورپول به ترابزون اسپور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/27136" target="_blank">📅 11:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27135">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1ef6701e2.mp4?token=rHAL_0kHBW0T16ytWDRchgoSnbL_hmcpONKQ978l4jJYOop5rmfGxvXXqbxmQV_bLJHWLOwhvbOmN4EX5d75Ch0I3D8K2C8IUEePxnkACLGaRyRFHoAWkkH9EZs0WxF3SGD3sFyimLdAq1qE2pSc1uXgcBYh6iTAfL0IJheHsJ51BPdG9oSJI0UPN5ZSsSEcdG0LKQM1FzmtaFCyLwGsy-ZPHf4az32f9MaJa6dCz852nmvQ3piNoD7x0IvFt6EZsjKEUklW5k348yH1TL6kecw0Ex1Jr1S14i1V9wQqwdc57sRp9cLDcQCmDcggs4dA-NcZpGEQl0GokECTrU96UDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1ef6701e2.mp4?token=rHAL_0kHBW0T16ytWDRchgoSnbL_hmcpONKQ978l4jJYOop5rmfGxvXXqbxmQV_bLJHWLOwhvbOmN4EX5d75Ch0I3D8K2C8IUEePxnkACLGaRyRFHoAWkkH9EZs0WxF3SGD3sFyimLdAq1qE2pSc1uXgcBYh6iTAfL0IJheHsJ51BPdG9oSJI0UPN5ZSsSEcdG0LKQM1FzmtaFCyLwGsy-ZPHf4az32f9MaJa6dCz852nmvQ3piNoD7x0IvFt6EZsjKEUklW5k348yH1TL6kecw0Ex1Jr1S14i1V9wQqwdc57sRp9cLDcQCmDcggs4dA-NcZpGEQl0GokECTrU96UDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌تند رئیس باشگاه رمو پس از رفتار نیمار و حذف تیمش توسط سانتوس در جام حذفی برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/27135" target="_blank">📅 11:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27134">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyWNoL-SDPM3IVNXaSstWde_17KRfM3YYNXL4Yzuh9OJtcu6hS2ELmVOhjt2qaInaDJQrlmxdAvJNuOHYKPV_mW1Tu1y9t6rJTK4PMYbmX00GC4QXN1hensvS793_85099gfQ6P0KgsuyxsCaXdS_XIlYOdcyjNfYEMLQt8JwTpsdeNTfVnYMfbQGWLs2k38bv0iAuNBpiUs6zFoPWQFZSPluydpGzirwuHEf8YIYbMEgMJs8VbLxqrML7PwwfsbI1MvIArPoNh716O9h4C39UBK0t3ZLU0AwS_JV-w1fxweYvqt0pGsfaq175Z3nCLomYlYEC3mUxXApEk9q-umkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
🔴
🇧🇷
باشگاه نیوکاسل پیوستن برونو گیمارش ستاره برزیلی خود به آرسنال در ازای دریافت 93 میلیون یورو ناقابل از توپچی ها رو تایید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/27134" target="_blank">📅 10:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27133">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c293e9daff.mp4?token=rHRlrZ3wfA4zSVGRkLhkY0u20Gj-9rgP93_6Cxvyq5fQKHovBqpTp7rmFTOygIFKr7wFZUqC9s8TVuU1LGKOW2V24UA-f2pK0KJhjUtPNMsTEHwY6M11Lw2GdIVrG3FE-xMX0H2zJpsj_c0gu0fW9FV5hBoZ5KS5bq6Maxdo3l75bHPL-GpwKHalrJI9h9VHMLbv3K2vkUtMs9454EPw9BJ1dJZGHibqeM04mIseCCQRvp38ZRmKzI3IEBRxIg5shHuZo70Q5g2hlJB1f4g2y-aLfN0SvN965HMF306pjEXfaFn7mceptbDfHDDxOrymkbfXuGkaphw7G6dYKAE58g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c293e9daff.mp4?token=rHRlrZ3wfA4zSVGRkLhkY0u20Gj-9rgP93_6Cxvyq5fQKHovBqpTp7rmFTOygIFKr7wFZUqC9s8TVuU1LGKOW2V24UA-f2pK0KJhjUtPNMsTEHwY6M11Lw2GdIVrG3FE-xMX0H2zJpsj_c0gu0fW9FV5hBoZ5KS5bq6Maxdo3l75bHPL-GpwKHalrJI9h9VHMLbv3K2vkUtMs9454EPw9BJ1dJZGHibqeM04mIseCCQRvp38ZRmKzI3IEBRxIg5shHuZo70Q5g2hlJB1f4g2y-aLfN0SvN965HMF306pjEXfaFn7mceptbDfHDDxOrymkbfXuGkaphw7G6dYKAE58g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌تند رئیس باشگاه رمو پس از رفتار نیمار و حذف تیمش توسط سانتوس در جام حذفی برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/27133" target="_blank">📅 10:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27132">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pn-IJyYqSHieUiomEMsYNbXYs9H3t2tjrcLZzg3CQ_ewKyDgcHkore_hxLR1HN2z23ikNyxufgeQmtSDij5uUoBRyD9knS49VBnnShQrNDLPDp0pzK-qLObVNkSObEC1-1OAaqpZGRBJKc5f14SB_T12Kz1OS3evwpDVAmhB1zBzcUSi8-bk2b1ahdhCitoKqTRcPhO58-uU2zgSNiEmM2_-DZxm08rzMgwjBI_o6HWmKAp_18OfKbLD9UHtZCVtvQeSQYU2iDYl42THyf2w1iJjE-r2MGDKp4xaRnBaqS8z2PGsZ2ynYjuYR0HIyC5ZLO2mQFjGaH1z_1gB2LkyKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🤩
با اعلام جرارد رومرو؛ دکو مدیرورزشی بارسلونا هم‌اکنون‌درمادرید بسر میبره و قصد داره که فردا بامدیربرنامه‌های‌ خولیان‌آلوارز جلسه مهمی بزاره تاراهی‌برای پیوستن‌این‌بازیکن به بارسا پیدا کنند. چند روز پیش مدیران باشگاه اتلتیکو گفتن آلوارز خودش رو هم بکشه…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/27132" target="_blank">📅 10:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27131">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmDykLp6j8KiAm8fnV2XoUKxRWi-llUV4_lvPMyFrwjPxYJcIOgYTTDVG_G9bkQ3nAGaZmp7FX2otNbsBujm0MMd8rxZLA3mczACM6kPqUyP3B5dsYHelcGquGZ63deR9afFenMXs2PnFN3IejsePtezuVtdRYDSs-gGo9YaargsfAaX71ZjnmeehcFj8G4hpX2rrZncvv-i7f5h_pihUvZZz0lhypdta67SELA7q3-G8rridwYdEPa_YdilBhTK3ByfnvLLBE5tKr_PGZedou88oeEICkwvJWCIn77A03M8EAb6LfglW4O7vQqtOtEP1dThas77PYBX0EGQkBU8vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/27131" target="_blank">📅 10:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27130">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7ky3MnN16YfvEYwMV67zXITc0tkBtoGTHMDWvMLr5DQ-RbIjbHwo9n1p_UkVmXk6If4ojOA7GeuHMgrsajjtj5r7HszA0stC4lhDA5r1m7_Wlzqv1XeuaX4XLwe0wxyWpbwGH-SatELoo_UQTqZ5lLDusVzvgvQCoGlfOiCExRdtm7kCz6Mtsq2bj8KXfGYY9iVRzt7R93qkp8hX03jTSdGPL8IkQY0lfmOO7TGnznDPPkif7hHu50kIISxU-GxUCO3_YxRZM9sg9EKEN8GRm_0vkIQhQoeS8UIRRtUzO0_VUtVojcng095rJFXjTY9UV4w3jRvr1fcILm94m7g0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
درحالی‌تموم‌اخبار این روزهای نقل و انتقالات شده انتقال وینیسیوس به آرسنال؛ ستاره برزیلی رئال مادرید بی توجه به این اخبار با دوست دخترش در تعطیلات به سر میبرد و در حال عشق و حاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27130" target="_blank">📅 02:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27129">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVrL2ZVHZdjWtce5zjjZEFDHo7RBwsTKHmuSghvyMmXA3-3bQIprdSPMqE49o6pdjBBc3E2o8CgU39zgft9EDxUzYLRjLD5FhQnTfTxd0LheDxTXpoarYSgLfk1Lck9ZVpkZDBOP5tp56pgnMM1yH1l5TWVNxIzJDLRiUuysTzf-HZQYsJmrZT9ilH-f2yVG1BS2QVztH8UxEYSV5g0qw68yVGmT8oyBMZMrARj7BUAne-aLgpvCH6aFb1Hyny8K9N5h9-KpCmhqmjuBioJ4WUGduz7gqncA_hiQgiS7m9PS6CN1rzG_GEevAucyqvzVINv8NrhsbsWJLiEO14gRGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بهترین‌و‌باکیفیت ترین ابزارهای هوش مصنوعی که از همه آن‌ها رایگان میشه استفاده کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27129" target="_blank">📅 01:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27127">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnHb91UhO4uAYUrEC3XHp-156xTpKIPsITwEzJvAFP6VpGDrF8lv6veEASWVchPoYbvKvxpPDZZmhHoLznFlIDwyVBMWYbQl1qEtbvi1Z-NvM0_jFOiqBui9hKA9e5Ba9Ce0u900vA1ArwumthEoWsDwDeQxHzJFpC0vSytJJNtkU-79PtdUIdHJipcjTMGE3E00Vge3xuGqLzr1OCYqDqdLMWwuWqcBdQ4Rz4oDw1I_3Z9DQ9VdjMRDH4ToevUNAxif4uJnlPq3Z6c44ZTlVUF9x1JQGs-FD0rG8v5q0yrO9MI-1Dmpk9ZfqBDElg1cR4eqAvtKUUhUKXLOleOsXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
ازدربی‌دوستانه دلامادونینا تا دوئل شاگردان ژابی و اسپالتی در کشور هنگ کنگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27127" target="_blank">📅 01:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27126">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfiPNVkQ6cn_Nqu90YM9A6cNW_cCqfSipXNFgquHphgb5BfnvKWtU0obNBLIvvG2xc5L4X-5K2fGfg7DdJ29YtNFNbCHX-f1R3kUrbHj3CFPPwMEx0Xc1C7_5aNGLC71kIMzkvAhz01o4ixSvBsMmRywNHFIMnt2yp4dcAiortv-sj9UYZQD0LUfn_o8uIfGsT-p14ajsMXvhdbFR7SIy2vu_26B94eu5Lp7VDgIG7XipGMWtqwf8XNvDLB_WNhei7eyDd47ayPTAgchvjxVaTJtvfF-GcNc606GgLkMr8SmpFIaIWaituRC2irpw9AXHNQ6VkSOxUDGUTxlM584CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
از باخت ماخاچ‌ قلعه با حسین‌ نژاد تا برتری بایرن و رم در بازی‌های دوستانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27126" target="_blank">📅 01:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27124">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1X_JJEipGV5I_k4zJT99ZBtsMCsDUjgfgvkBC_TVhvekglmbehdrCK2FNbj6mD0tZyr-CyUbH3B9r4ccDIhjTcwyW7deFH6ptsIeEA56SP6rBnQvpEPkslvhBpEvb440yM8DoAxBYymXc07SownFjQrDFtckZFMyJlWXmKWA61vrDkfCYnb0LwFyYhi867Yy4g5fNYoepEjaFGA4U6CcIg_vw22SSJJ53PBJz8XDyV7GduvIlgZ7BAXRDrrPHTgmkJX6xyd7_v3H5i8TZSollYAVwenEty48fFDtXyWVFXLIphTP3eWqzoC9HruV6Pwa4KAYfsn5N0aCAIgXBNOFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تموم‌ شد؛ صلاح رفت سوپرلیگ ترکیه! با اعلام فابریزیو رومانو؛ محمد صلاح فوق‌ستاره مصری 34 ساله سابق لیورپول به ترابزون اسپور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27124" target="_blank">📅 01:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27123">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjvSYGksE8eLNsCszDCJdUSLXrsw1r8knbFNYHHNRRc9KgRVsDw2aSRjRNQsaEwmWqyt52hl5Jm-VDyZf7mlVEYbJf9g95VpiWx8saIme1T-fq8BKHiXvBkjvSVlDuk38SSyqbuqJWd6SYxwENbEg0ibEqwkEJxfF4Z02JXEgydhDNuyumNT8kolG4Wz6IjnM8OIrxhWDF3Fn_qS9gzuhK_pg10-jMrJ8vw7GBNsoixGZQHttulWn_qHfZSiUB5NgtfoCdE1K1756nKaa8ZQMVJXqVF_nLDlhIzo2lBV48K4RpC15hYe7kAqI9rhntikadauvFPONS6B3wfx_179Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال: مسی؟ فوق‌العاده‌ست. من به نصف دستاورد هایی که او رسیده بتونم برسم بسمه. یامال برای رسیدن به نصف دستاوردهایِ لئو‌ مسی فقط به 455 گل، 205 پاس‌گل،660 تاثیر مستقیم روی گل، 22 جام، 4 توپ طلا، 3 کفش طلا، 4 پیچپیچی، 6 قهرمانی لیگ، 2 لیگ‌قهرمانان،1…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27123" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27122">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9Px2pTfHuSEjQ3yW49ToX5BpYq1i7SArOJfRSQ7GcLM9IEZy5pO0ckAe3nBcOZjuqSP5uqKSdyi6jCPnQRHohHTsDJso8yvqVBrT8hTq6pHVWfMyBG_vD3Z7UyIcNlCNGbLK4aBbq2URZUTEFmgcrvCCRWJxmsYJ0PXWRw6zlXUJ-1de05axC2sBSaZLkVhXYm7P3UbjUz11AMluokcywrCdErIUhIYO_hwo92G7G6XnduPqBJubYio76jDuQCVGxgGI1m_tScK99oUeF2gBcNpzemRIBzSb5LKma1cx88MBqnSi3BB2AuyxKA-1jTXAfCNBZ5LhfSCYf04CUeEYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سعیدفتاحی معاون‌ورزشی‌باشگاه استقلال: قرار شده بود امروز عصر آقای رامین رضاییان همراه‌ با مدیر برنامه‌هایش به ساختمان باشگاه مراجعه کنند تا ‌اقدامات مربوط به بازگشت او به این تیم رو انجام بدهیم اما برخلاف قولی که داده بودند عمل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27122" target="_blank">📅 00:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27121">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c01adXPElgswivrea1atQ8Jgvpu7GfRC_3GZ8HmdY4N0TnruDSfvQflb3zYhtJFOudhpXqTAENP2iqNq6fUnXDOKGRw9z3T6wmjdslhrj57WTqslVN3tzHTdBoC5Ie27noTSWtT5zys5M1uTQa7XTLEqnEbzoML8TZ6ngUqAq7oL4PhIEOWa5_kl9IdMSyCVdkp5bQTD1E0bRdiEVkP71VlgfrmUPp7uUi9Km7NIZtniZMxjajgtmhkOUEpSQ-qzze23i6iFUkbLuRLOHzyeoJk1lwdDofAVhJJ0w_cR5OqWeOaqGs6IrmbmUAFSsk2Bcko76MJxRhYzMkGbZ0Hv8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
طبق‌اعلام‌رسانه‌های ترکیه‌ای، محمد صلاح فردا ساعت 12 ظهر به‌استانبول خواهد رسید تا کار های نهایی برای عقد قرارداد نهایی با ترابزون‌اسپور انجام شود. ازطرفی‌هم رسانه های عربستانی میگن الاتحاد میخواد بارقم بالاتری هایجک کنه صلاح رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27121" target="_blank">📅 00:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27120">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cu57dAGB7x7AARZXE_ePRBDSbGS_PYFJhs1_P8YrBRhvC-FrZ24cWYLQjGa93MFIrluHHAS32D72Pfc8dLkDEWAgG_Ujk_pSmvBamT4yHo7o_MrYovGFpTyRb1lw6CxtaYklfJkkr9nLNrgwk-Kzlx1erjgT9BPb8w4PWbguQq88SaD_iCaqsHztHSLQRr3-6Ye_ffyv949HHS_0tp1q4iwqwwwzEv9Zmu_9EUv_zLUTkNOLfx_uJRpelwKDnA87rfSNNagFKhGa-ihtqEapI_b8baNSDU2CgRqVE6CPAlnIg4WZOOya6u--Hj54CpEc6-Rkq5vP5lSiUqUwGfNzxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال:
مسی؟ فوق‌العاده‌ست. من به نصف دستاورد هایی که او رسیده بتونم برسم بسمه. یامال برای رسیدن به نصف دستاوردهایِ لئو‌ مسی فقط به 455 گل، 205 پاس‌گل،660 تاثیر مستقیم روی گل، 22 جام، 4 توپ طلا، 3 کفش طلا، 4 پیچپیچی، 6 قهرمانی لیگ، 2 لیگ‌قهرمانان،1 لاریوس نیاز داره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27120" target="_blank">📅 00:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27118">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8a21ccb63.mp4?token=mJvBxqyQ_QAvl-0n3F59ZYCqZAJIfeats5ES13XbvgYMGKYj9fE4zSMvfoFEw3E3WExwvSr2KaEeL76mQNOpQYJsMMM-131SpJnaeJVRvkT4flv4wRb8azxvoTYRzDfRbYow3BjCet-5lsAupaYXw2cngj23FTM019mG2sXxsbdjpeeJkNaP0lOyjBSybhIHBmtLn5RvY3dk413Tf09ataKq0BTOQNHgUvQcnU6Gz8iwXkSFdUC9v_Pyoz-m7fN-Yyjo7LswxdbBxN7_Tep9361Q-yKymIu4BtqB2B2EgRnxjwJPuz4K6Rqmjr-hxOScwgcv0jyA_zU-EF_tShQeEiuSaVd0uWL-_yXg0dx-AobQN9FbTHLX9LK5rhlwbQ0JFep5FE3DN71h9JvCxdJEWPsjtGs_5c6YlTwAdSSEFC9zF1eQKjlxNxN87NCTaqix6AptsAKJX3zLj0_Izu6UCzPW3mvSah5-tQ64VtSO3TjEEglkZ54oP87ncHHubw9x2Jkw69q_aDVuelsAKE-JXMI7BoKo16RgTsXDEB5o82d36Praz72azwIq4nwhd88bTxgjJdv_bt6qaNZrCNd_3xCNiLv_HNc1JS9jWqXteaQRy8nKLiE4HSIJqdKEduLhX3NqRzucLUaG0yC4i_56kjAcZXu-fcQN6t8QJ1flhys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8a21ccb63.mp4?token=mJvBxqyQ_QAvl-0n3F59ZYCqZAJIfeats5ES13XbvgYMGKYj9fE4zSMvfoFEw3E3WExwvSr2KaEeL76mQNOpQYJsMMM-131SpJnaeJVRvkT4flv4wRb8azxvoTYRzDfRbYow3BjCet-5lsAupaYXw2cngj23FTM019mG2sXxsbdjpeeJkNaP0lOyjBSybhIHBmtLn5RvY3dk413Tf09ataKq0BTOQNHgUvQcnU6Gz8iwXkSFdUC9v_Pyoz-m7fN-Yyjo7LswxdbBxN7_Tep9361Q-yKymIu4BtqB2B2EgRnxjwJPuz4K6Rqmjr-hxOScwgcv0jyA_zU-EF_tShQeEiuSaVd0uWL-_yXg0dx-AobQN9FbTHLX9LK5rhlwbQ0JFep5FE3DN71h9JvCxdJEWPsjtGs_5c6YlTwAdSSEFC9zF1eQKjlxNxN87NCTaqix6AptsAKJX3zLj0_Izu6UCzPW3mvSah5-tQ64VtSO3TjEEglkZ54oP87ncHHubw9x2Jkw69q_aDVuelsAKE-JXMI7BoKo16RgTsXDEB5o82d36Praz72azwIq4nwhd88bTxgjJdv_bt6qaNZrCNd_3xCNiLv_HNc1JS9jWqXteaQRy8nKLiE4HSIJqdKEduLhX3NqRzucLUaG0yC4i_56kjAcZXu-fcQN6t8QJ1flhys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
فدراسیون‌ والیبال‌ ترکیه‌ به‌ این‌ شکل از زهرا گونش و خانواده‌اش بعداز قهرمانی در لیگ ملت‌ ها تجلیل کرد. گونش با درخشش در لیگ ملت‌ها یک تنه تیم ملی ترکیه رو قهرمان رقابت‌ها کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27118" target="_blank">📅 23:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27117">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBk-DGzMHI1C3v6qzozIqC6zcMlfw-_VcQ4vfTSr4NR-4h91M8Od_zdBmYQ2jjwZvLm2EVdTDy22siyZAPck2xtNR_ZWAm1VlFizwQBTIiM6P7Wt3C6lafJDxLfvT5hWp77WqoXmFGJKCrSrDbOo19NP3zEJ9PdkFV8EK3pVTtM5aEh3e2LUu61gdkKdM9eP6SpUCIvCdXgi_y2_5IR6Lk4myjE9iVIWoBwaWFs9gYkeWj9RvHyMw1zapOq83nl2Tx25kSoPraaAmCHWAV4uxGJdsduCWh-ZK2zlHV8m0hLexYp4EpKuomGgb2i4lkaxFKcnEPRTuL_vIUTxsE9DGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
رئیس باشگاه اتلتیکو مادرید به زبان عامیانه گفته؛ خولیان آلوارز خودشم‌بکشه نمیزاریم از اتلتیکو جدا بشه. 100 میلیون یورو که هیچی 200 میلیون یورو هم بارسا بهمون بده آلوارز رو بهشون نمیدیم. مصاحبه های آلوارز اهمیت نداره. او موندنیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27117" target="_blank">📅 23:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27116">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyO0_8LkIwRWdD3K9lLAtAP0fvjZ0AldT4D8hXkZ4D2UofPX27YuPqfDXi3YTYgmmk8NT5rWYTHCgXON25Zd_qjJiwOxIjLy4MP4YMU6E8qu1aPjy0mdd6GRJMQPigXzBhL8tI0nAn5pGqeZDl1U9lZ1WX_3EwTQsymt7U3ozQAOsWkZ-0CU5fswFuQABHGrkja54vq_QcNDchmCAbTOkDUqICTR5BG0H5XILDxcgG_khkCPwecpHlMZb_Ct5d-HR4ZcnDrEkSvafu3dFLJ0ByjjbqO28vN6NnT2KLN95TMMv4W6AEle2riAigj0psUHs-qyYSi2uKN823tvSAWZ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27116" target="_blank">📅 22:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27115">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52510ee628.mp4?token=mb7Ql7xPV_4j8OxAyArW_1_W-9CPjlkDWX8yy8qWen9DfR51n4mYiqcN8x0fi3hCzNY2wY0hkoRbTPZrEkE7U9Rn-lVcvLQDqcIKoijeXKBArlxx6h5AMl_f49sSGT88jT8m9ewxjRih02K7KbdKccd048b2FTj9DcZIVFJ2vfOtCg-Z0lrahtDqAx9w6saBwuGsTg0mYQXkyJ5B7Mwi7ODtWjrVDlKcXnBTJhc9wV_2sNudaifr8rClI8QuhbQ-DW-3GKG5NRlB4kjdPtYU06DBTB9bogPIjYyg4w1jVG-R7XG3GXPv3IVXT1r7MtXg2nNbKHKpOh-4wwaabdYbjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52510ee628.mp4?token=mb7Ql7xPV_4j8OxAyArW_1_W-9CPjlkDWX8yy8qWen9DfR51n4mYiqcN8x0fi3hCzNY2wY0hkoRbTPZrEkE7U9Rn-lVcvLQDqcIKoijeXKBArlxx6h5AMl_f49sSGT88jT8m9ewxjRih02K7KbdKccd048b2FTj9DcZIVFJ2vfOtCg-Z0lrahtDqAx9w6saBwuGsTg0mYQXkyJ5B7Mwi7ODtWjrVDlKcXnBTJhc9wV_2sNudaifr8rClI8QuhbQ-DW-3GKG5NRlB4kjdPtYU06DBTB9bogPIjYyg4w1jVG-R7XG3GXPv3IVXT1r7MtXg2nNbKHKpOh-4wwaabdYbjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
درمصاحبه‌جدیدخانواده‌نیمار؛همسر نیمار از قلب بزرگ او گفت؛ ازکمک‌هایی‌که حتی دور از چشم همه برای اطرافیان و گاهی حتی غریبه‌ها انجام می‌دهد.
‼️
البته ستاره واقعی این مصاحبه شیرین، شیطنت‌ های بامزه دخترکوچولوی فوق ستاره سابق بارسلونا بود که تمام مدت توجه‌ها را به خودش جلب کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27115" target="_blank">📅 22:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27114">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSu6GfkzbrYvQr_kfFXqDb3QmsI6Ll8w3rWtmQe5nFt9hXMP2jSkZBeffAMdX_cwN8R07FqFqk_NFin9NiH5o43jyAtzq9tG-h4gvJQGnU9zOkZclYGOLoqdSsP1We8-3DWzTJZS_EgmUx44g7El8dKzl4eEXAChThEnvYCQpcIF6Q24NERIMUrIoQ7UkYrudQC-hvXxSWDAOSLHB-bM0w0K-gPObO2_enDZ-gE7SZrmWR31nBzupHCpa_mEP_rd-RfeuGAqPQWCQ0jz9Ppoi2c8-QL5j0_HxYP6j-urBPZYQs9hiRO9RR3uzHUHcu1fi551hBcl8pYeNXbE8BmNdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌انتقالات|نشریه‌ سان: سران آرسنال به درخواست میکل آرتتا به‌دنبال جذب یان کوتو مدافع راست 23 ساله دورتموند در پنجره ژانویه هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27114" target="_blank">📅 21:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27113">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUXEmtxsQE2xrfXn1IKyf3J3SAJ_rhXfQbiSGAze-3e0MGlzxO0bRbk5A0EiV9RbxsWM8vg5smoBf8KxDgjUIpGbxOy-7UFjtwrdTzkGyKGxID7yuGe4QuED0CSjLpG-c5KbeqR7BnCFgHFq_J-bp5lDJ_97Zgmxn5Dw3yS5hIg-K6GpV0PSzBNi1pfKyUsouIi5zWJaX7AU7_53QFh8K5aerKifv4En2eJmju6dtMSQI9sO1o1E2fy0d_IaX4rf0L-XZ8Zi-_q3Ux4tg1qI2rt5CvvEwymFuuQeCXu_dspq_6Gvl6nw_ijv_Uj1imJt8WzMogOjJcXbd3OZ9H_aRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس اسپی مهاجم رئال مادرید:
الگوی من در رئال‌مادرید کریم بنزماست. میخوام با گل‌هایی که میزنم همچون او در مادرید محبوب بشم. برای دیدار مقابل بارسلونا در الکلاسیکو لحظه شماری میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27113" target="_blank">📅 21:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27112">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsuO0zVEF4BE4dWEKhRQ6kleuR4UJ2BSnolFxqx2W780DNF00r5KQ3BnaTZSZmKpE8QUs_rZHIyHCx0TbFqvoylXjAGSTvoqW7cQqsFsWANz--pYT0G3kJaq7m-otfazPnfnXMzu1uZaLWN14Hn5GESjgQiapPtjsrAKXhdxu1TWb87sFizf3lngjoVHATO3ei6c4yaXG3b_9tF7nqkrBCdCnb6urvlcKgMuGmxlN2g0qm9PSJWP49RTGL8YkY_jlRDhKv5H1w_OISdaMQaY7y_ruwzYB8_s6pghf8r7Mj-bXrZwYuYHjzWLVVgFrS7_0jDxuiAX0H43gDBsClM9fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27112" target="_blank">📅 20:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27111">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYhaKAgYheFFKr2gwokB0IGBMSSrfraF1uhhoPRA1kl23AvDZa8CwtA-2XCi3oc0NCDx-Dlx51f_vYmJSGP4NTUZyASIK35fR9_R2Z-CE3QxzwkIBXgcoVzQB7SxdWjp7uA2G6EW9LFHWe79ErWhAfU6txHt60QHSPGXYOAaxowin1ynoAUCC5AdQDITCiL1eGB3VZquLOI800fbAWVhnhr0q-rr4luUeso1IN3g-dC7tVw-07vL0NhR9Dxljxv-Q4qn63j2s31wMUArxl-2SxJEpddFZP0mq7Jbp4N9GsMCdD3UXrFVtUwnxs4zzbE9nzKPTjorJ1Qvp_2MBbthvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: باشگاه ترابزون اسپور ساعاتی قبل‌پیشنهادی دوساله به محمد صلاح ستاره مصری سابق لیورپول داده و منتظر پاسخ این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27111" target="_blank">📅 20:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27110">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-0-ejHqq6TqiM7KxAdleHKXRsamgP7tkTYJ8eCMIyVTy0Ej63cU1AsbjR28nF7wd8QvbXdtuM8vF8CvDZ7uukxqUbqCD4Y2E2GES7lsFb25xXl1e1UsOPWnJIWWEsq7qyEkHxhLxZVi7V-hg5VOHLeaqndIPST8lSofFVw1zzo1N0aMLFq_VqPO5Bz5gwNhwGCNpBH_fuIxP696eIrievAetTTXdtVn0TJ-Z-etyf1-c-ZBQArRYPGFBVqsg0MyeS5_TT24nSgt_Pp84q1l8mqXXmECn9NIxzx2BEj-ccPbqDtZm-VRuLZf8vDMgp1vCp6TLTuUg540DD94hh1Ycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
استوری جدید آلن هلیلوویچ هافبک تهاجمی کروات سابق تیم بارسا و مدنظر باشگاه پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27110" target="_blank">📅 20:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27109">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDSoNs_tMMarRMNl837NvWJMrC8HelMlQMHuZL-vWmt8jJOi8GPWiMZoBwNzl2yc68dntb5vMRMkD3Jj2Gztuuz6pHtIIYEs123aVQq5EufWA6qkN_ZVcwF5mjUw8uHNfu41U8q_BpbqxpC_DzXnzwGedu0PHgTlzgobfMWurTwp4P-wY5HVa2oAPp6Raq-12NPM1X96F7C1kacHYDsce4kvKcylyFqR_aW2ci0Dr_9CG3ItliMXUUS3wvDP-KykCZ_TwLh4tnfLErU3y9smDpwf4ULrZpOcuqNyfDczee-hi7osid-pOsOnr5o0DQetkGo5PawayxtkuJ5DvasnqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
نشریه‌مارکا: انتقال رودری و یان دیومانده به باشگاه رئال مادرید نهایی شده است. بعد از رونمایی از این دو بازیکن پرز پیگیر باستونی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27109" target="_blank">📅 20:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27108">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpfrnob1uwoDQXjOKMwMXCPeTNUYpGMLjRvuX9VEfZx_pqdRE8f6ylaAuglOHMJsi3wKUIEGUjA2QGkaOlxdHRzpmPRFe7ogaWUYFUVSyR9sSjf2_bZxzKU5KpfNsieqyl6RhFoKMmRPaIZe3UpI5aIPIGoIaN4IIg9wpwd0OeZ3i9ycy71N7_F3gk3cCVzZcC-Yz4OSmQk22p73abAj98ERqEZuBD81CEXkW39rzzrraH3KQeed352080WM_MsCriEVCCcf0ky64dCYrj6-N3vJFNOyGAWliTfl5db7AkTi-VR7v5yPBBANsYCwEw6NkEs66kmZRO9iDxwoExfByA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
پاسخ‌نهایی باشگاه‌فولادخوزستان به پیشنهاد باشگاه‌پرسپولیس‌برای‌خریدابوالفضل رزاق‌پور مدافع چپ‌فولادی‌‌ها: 200 میلیاردتومان نقدبدهید تا ما هم رضایت نامه رزاق پور رو براتون صادر خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27108" target="_blank">📅 20:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27107">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIbFr6U-tDhy4XQ9qOXJIbK-XcjLXf_lZI_ui7gyCbu15sPvrsP-cvJJh8ixf-JLCowKtSM-nDHrMoEjrBrK5Qudm32ZCilfJD8sgL3lUelJkxyvhAfSFM7Smsox6S0tAoNGWALNIGM5bLS3m5ql4_k6WlFfDHeFkHkBeORTjwImh5y4emXSqxgNF-GraOUfCVyJ3_W_E8hOB-fvi3_nQR1Uw4W5TuQHaAYygv_rGkCFy2hAFSwzniUMgrOKVt8u0G2XDaqXaiMyWIZP6X7gfx02NFxGE2TxxAPcSZdQd7DL0mua9KYJTEpHgwKuIZ8u4QVfxaz3TxGjmQTlnbAikA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27107" target="_blank">📅 19:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27106">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6169d08e.mp4?token=CgNWZBikWgUuZtPQB3Sr6vxyOY8F1M4t_M5gTM8yVbVG5kXm5YRRJJuwLzfZLIjMYRHzxnsPdJ2Ob7geZPlFHd1Xu83RkvAD0tgUxMdlXW2p5LQefRwdYXptazec8SuOkZO1fxxKNcYldRtHIUA6Ymj5Vxlwb8-fLFSlpRhKXhLj08CyLWlQBqFZ0Mz4ydJ878JMR2BrGUcwXkvXg1NOTGGZF9I0W214CBafCLheG0LM8pbKP4iOFbPjooKlqFcG0bmq3yEIAiqsP3bGZNXjwZP5MlKJEBRMv-vr-O5kG8DZ6_w4ACo0opH2yQyqqg6LmqidOh0TKzHtmWOMJtbLIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6169d08e.mp4?token=CgNWZBikWgUuZtPQB3Sr6vxyOY8F1M4t_M5gTM8yVbVG5kXm5YRRJJuwLzfZLIjMYRHzxnsPdJ2Ob7geZPlFHd1Xu83RkvAD0tgUxMdlXW2p5LQefRwdYXptazec8SuOkZO1fxxKNcYldRtHIUA6Ymj5Vxlwb8-fLFSlpRhKXhLj08CyLWlQBqFZ0Mz4ydJ878JMR2BrGUcwXkvXg1NOTGGZF9I0W214CBafCLheG0LM8pbKP4iOFbPjooKlqFcG0bmq3yEIAiqsP3bGZNXjwZP5MlKJEBRMv-vr-O5kG8DZ6_w4ACo0opH2yQyqqg6LmqidOh0TKzHtmWOMJtbLIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی عجیب احسان علیخانی که چند سال بعد به واقعیت‌تبدیل‌شد! حدود ۱۰ سال پیش، زمانی‌ که عادل‌فردوسی‌پور و محمدحسین‌میثاقی هنوز در کناریکدیگر در برنامه«نود»فعالیت میکردند، احسان علیخانی با لحنی شوخی گفت: «میثاقی رو آوردن که‌بشوننش جای فردوسی‌پور!»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27106" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27105">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYQQEWVlP9vwZbAtvi_vJctER-YB764ZgXFwozOL3KgEXgrDJ0-jEXQ0dx7hBOx6iiP2jhhx4TOS4xGGPd0orzRvv6ZyBZmFmgqgthjRyKkFlqFo95m_yIsDX0c4zC0h66anWf8rQbZUayAs7_Ev01hdpi1nNntmMo8KPdWsXQen7HtWYCGpuva_MvAkgCi0s4ZHuCDoW_Cmspl3YFnjrHH3Gb_ioaXTG3vusZvf-r5PZPxYdwzXOwf7sL2uLzDNVUcYRtiB8C0clKDMtDtkJXQcBgxM2ZNVId1pMvQ1QGKkrJCPvFm-57mWuSiAGNEJb5BS6krzhNx21D9jU55R1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
سانتی‌آئونا: محمد صلاح ستاره‌مصری سابق تیم لیورپول برای‌عقدقراردادی یک‌ساله به ارزش 12 میلیون‌یورو بامدیران تیم بشیکتاش به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27105" target="_blank">📅 19:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27104">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=DzMmLgQPHC3O_YYoH21HRCcd_ewrCypnof0usNwpg3dwGslTTrYqucS08pi0Y3g-SOSe5ga9mg1ODvr-akn9PGNxEV5fvDCs_P4gJCoKLTDar8op8WWLNwjS3imEUW7gngvBw7IcDk7ojD8i5z0fIWxnxSQT-ZVsEYGiV_nHydA4oBLJykSF4PexI2mr2wVtKr45c4ltF6l3kVvJ-KdB2gDRopGK--ImiPLfFxVnDuxP0qKVhNTErS0JeDMcxTdnjYYLCgmyG7atAGedZGy8KW19-rfZ41447RSmE9iWNsgDOE0jp_CWwdIv5TSPJrDIi9e6UwQfwGWwcgHysf40xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=DzMmLgQPHC3O_YYoH21HRCcd_ewrCypnof0usNwpg3dwGslTTrYqucS08pi0Y3g-SOSe5ga9mg1ODvr-akn9PGNxEV5fvDCs_P4gJCoKLTDar8op8WWLNwjS3imEUW7gngvBw7IcDk7ojD8i5z0fIWxnxSQT-ZVsEYGiV_nHydA4oBLJykSF4PexI2mr2wVtKr45c4ltF6l3kVvJ-KdB2gDRopGK--ImiPLfFxVnDuxP0qKVhNTErS0JeDMcxTdnjYYLCgmyG7atAGedZGy8KW19-rfZ41447RSmE9iWNsgDOE0jp_CWwdIv5TSPJrDIi9e6UwQfwGWwcgHysf40xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترِکپی برابر اصل نیمار جونیور!
ماوی، دختر سه‌ساله نیمار باشیطنت‌های بامزه‌اش وسط مصاحبه اجازه نداد پدرش‌راحت‌صحبت کند؛ همچنین حرکات شیرین و بازیگوشی‌های او دیشب بازتاب های زیادی در فضای مجازی داشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27104" target="_blank">📅 17:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27103">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835360d02b.mp4?token=j5f0VwZFGEU4_ZtYudCQcuQWIjDhIo6zveo8JG2N088ehfDvZifkoRbsqatVNhItJYAPChkWNiggazatpHvvX1_ymLosGhizXChYAPnzuj5id5MPjKQR4UMAwHwdSBSUdTk3wQa8dMGh3ribjXZ3sGUeFBuziM48DUYvBJB8xYu7gAFb5J1pKJg4w8eNHCKs7ynkjCHztA8HBhHJf_2T7QJ0Gm2_P1AeluzukdRg2j62aGY7fnH-RxqdRaoMZBdYDPIW_qTBREWv8vcKtsp7lZRROjxtTFTRHXJ3d4km2wCYRNlezMUjRL433wcAli-8b-VtMxp9KgnGMar7g777uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835360d02b.mp4?token=j5f0VwZFGEU4_ZtYudCQcuQWIjDhIo6zveo8JG2N088ehfDvZifkoRbsqatVNhItJYAPChkWNiggazatpHvvX1_ymLosGhizXChYAPnzuj5id5MPjKQR4UMAwHwdSBSUdTk3wQa8dMGh3ribjXZ3sGUeFBuziM48DUYvBJB8xYu7gAFb5J1pKJg4w8eNHCKs7ynkjCHztA8HBhHJf_2T7QJ0Gm2_P1AeluzukdRg2j62aGY7fnH-RxqdRaoMZBdYDPIW_qTBREWv8vcKtsp7lZRROjxtTFTRHXJ3d4km2wCYRNlezMUjRL433wcAli-8b-VtMxp9KgnGMar7g777uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنظرم‌جذابتر از گزارشگران ماگزارش کرد در حد همین چندثانیه؛ گزارش فوق‌العاده گزارشگر زن لیگ MLS روی‌اولین‌گل‌لواندوفسکی برای شیکاگو فایر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27103" target="_blank">📅 16:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27102">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDANOswrHi6xP9DYz0OqBe40CthCAaCsrsTTDymRktr7WGnrtHX6hrEQGlNoEB5HFNROtYIQlYrQbYmaUtQQ-T8a9fR7gNJSd2fEaOoHvwkxk1E_WqbGWR3jHEQHAcex1lAgKEQNL7Wf8gtDhANYhJXhndUUjhk5bRilg4nbNrhYmzCv1P-1u5u3aW9euZm-g_1G0dYzMNNxdr1K-9UNWM5WiGaVIxoH-bsaFpUe3oFI7MM0D3Q3EetH-RtslopoGeR3vU6pc75VA7XUKywbxcxq6YSbPOekQaAmlcHQHw3X7GXRrMClCN59aq0NGfMkpK0q2L4DJG8mL8rFu1n21Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
رتبه‌بندی با سابقه‌ترین سرمربیان حاضر در لیگ برتر انگلیس براساس‌تعدادروزهای‌حضور مداوم روی نیمکت باشگاه فعلی‌؛ میکل آرتتا با بیش از ۲۴۰۰ روز هدایت آرسنال، با فاصله‌ای چشمگیر در صدر جدول تکیه زده است. اونا امری در رتبه دوم قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27102" target="_blank">📅 16:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27101">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=n0x5NL9c0Swb1ZTRgTO1I51YY2EjqOLZ6ThDxX85eIWmk5zZifLIICDKremHBSwV4oG8JSawdp5qe8ON7DCevnMLoakOOwyfjD7S1Emri9OQ3EIiOg1danE-3awZreOV6W5pxojcRrNzbqIYXU1SOztIzH0vDfKcgNBrcCxxKCvnFU5jUlNbNe1n4w1asMR9na4tnLI22LzWZK54wiJVJEuwL69awg5wc1nsA0ufCgiytbsP3DE7eo0Qm7MlpHn7sA1HLZg65bHhM5kIrz_QvP_1zzWVPE-US56VTc43Iz_jeSbSDBmG2ie109KGfysHHo0TD0cJWp3Ul001e-2ToQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=n0x5NL9c0Swb1ZTRgTO1I51YY2EjqOLZ6ThDxX85eIWmk5zZifLIICDKremHBSwV4oG8JSawdp5qe8ON7DCevnMLoakOOwyfjD7S1Emri9OQ3EIiOg1danE-3awZreOV6W5pxojcRrNzbqIYXU1SOztIzH0vDfKcgNBrcCxxKCvnFU5jUlNbNe1n4w1asMR9na4tnLI22LzWZK54wiJVJEuwL69awg5wc1nsA0ufCgiytbsP3DE7eo0Qm7MlpHn7sA1HLZg65bHhM5kIrz_QvP_1zzWVPE-US56VTc43Iz_jeSbSDBmG2ie109KGfysHHo0TD0cJWp3Ul001e-2ToQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو تو چند روز اخیر بیشتر از 12میلیون ویو خورده؛ رونالدو بفهمه تو ایران دارن باهاش چه تبلیغ‌هایی میسازن میاد از همه‌مون شکایت میکنه. طبق گفته رسانه های معتبر، کریستیانو رونالدو و جورجینا قراره بزودی بالاخره باهم ازدواج کنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/27101" target="_blank">📅 15:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27100">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzXJz5SSbXyhumfKEAXU0BTox0-h3U_m_3RH7O7Tg2oEa_boElcXSjPr4I3lGWlcQGBBwPSwYwqz5e4eB4cw2Q-9uAEybcAh5hvgdXMryuYayusf2ORU2oXgjo4ygqBAZdRVHU098xTivJHo8PTjKGo1J2OmiN5CJPWVNPjVpiiK1VfDXUqBX3FvtdgutSDPVCUS2-_D_OxM_SceBtaqPNti9kb5doIDGThlqseQ6fev9AUM2tMeRn9OUMmQcZgBDC8SNSpwFpaKSelIqgvSgFNBcdtrxHtOMiLTnZITaHTcthwOoSuoJTHwHsdHIZMwD1P8dVylaJVrtIa66TO7cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنایی که بهترین بودن ولی از تیم ملی شانس نداشتن و از داشتن یه تیم ملی خوب محروم بودن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27100" target="_blank">📅 15:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27099">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">قیمت محصولات ایران خودرو و سایپا 13مرداد
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27099" target="_blank">📅 15:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27098">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBueJFNQzUmn-c5kbrSj-CIoF5LWJWUc8ritjOhRNa7cME1fhYYR1QAuBbIr8LVDAb_EXFbtf8QtOFL8yTY83LLjPvx4C2GpFsDPN6fHdW74YyV1sA2yUh-ZwYPhnNDmxjWPtHYiATlDHIxmnaP9s0QaQ_9AmpJBafbDKUUpnRkJTyMq8LUEHE8sqz0MX7rQWtSsfMAK3d1jno4n8FmmXNiFY8UymQeIlQ-blkkRaG6N6PQwhUQpO9qlS18XiwZe-8Lp_nv5C5uERoJ4SfUS-Vzw4uldRk3TxIVWUkU7t2XWW9v6t8pzyxwRn3AF2M8MWtv06owpDdoByeewzorRJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کاپیتان‌ های پرسپولیس در فصل جدید:
حسین کنعانی زادگان، علی علیپور و اوستون اورونوف.
🔵
کاپیتان‌های‌استقلال‌درفصل‌جدید:
روزبه چشمی، صالح حردانی و امیر محمد رزاقی نیا. البته درصورت تمدید قرارداد رسمی رامین رضاییان با آبی‌ها، رامین کاپیتان دوم آبی‌پوشان در فصل جدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/27098" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27097">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8vRSokeBFo8kuFTJb9XeK0QZFBSL3CiLfp8BzEnfm2rXRojSxWcqTDk1eN41Y8aF9rov6GY1INGfpGGZdmkV1JMDvXWwn_OYfhcfyexO17nxWqZuTctqP9ch4hi2Bjwuywzf9di4WeYo3o5VcWfGxHA4_s1aACKZKJpN_znDuYO3lW_ylr8y_wC4-CBKMsH9esBxLeOkKuQVKKiBSn8-X-Jj7_TfBLirbXOERH0Ds1HTx4_iz2jc5UqlLzmnir2-dQ8kXa_Bg2cHa3m0yWDSLaThDa3mqeRayMxZaye5T1ZS3K8IoBGml7mm2_61chGYJYwdNb20E7hHMxck4i2ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
عبدالله‌ویسی سرمربی‌ذوب‌آهن: دوست دارم کاری که‌سال 95 بااستقلال خوزستان کردم رو با ذوب‌آهن تکرارکنم. بسیارسخته‌امانشدنی نیست. امید عالیشاه مذاکراتی‌بامدیریت‌باشگاه‌داشت اما درجریان مذاکرات نیستم. امیدوارم که قرار داد منعقد بشه و این بازیکن با تجربه رو…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27097" target="_blank">📅 15:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27096">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyJSPB381_1s5wnFVxf6yeT8q1ZB3Q1fxZAsVreScXDo6VuXycogXotuASowYdKa_cidFKG5reyfzqXM_lq_wDCE0QTM3q2JjAZ2Y84S5KOid8vZRLwduVfIUiBFMy05S9Qj6OxSlyIr6oYIWwS4646IXmvj4tXqum2fHyF8fzUH3OIj_DgieaqGgMt0t9y87wQHmPQOGxsmL2tPqBSCNRRtmdl3gMhuU2XnVgqGH762FK-2-5uGX3uElQ3cNgEX7Fb8GOmRFlnfV5MTzRYakcXfgYkrEixBas-XBTuOdUHdOv5YF798duk7M0m01TtlmIxrosKrH4MQIIY8ksnqPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛مدیرعامل‌ تیم پرسپولیس امروز به حمیدرضا گرشاسبی مدیرعامل فولاد خوزستان اعلام کرده حاضر است برای خرید ابوالفضل رزاق پور 120 میلیاردتومان‌پرداخت کند. گرشاسبی به حدادی اعلام کرده تلاش خواهدکردکه مطهری رو راضی کنه تا این انتفال انجام بشه. مدیریت پرسپولیس…</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27096" target="_blank">📅 14:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27095">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyAXTIRip5bspDqaPM5-oWS776TmEATDwaxgf2V3bD7tlztFny6E08Dxdxx4Lna-AzHNgahPl9hgVjftCWtTGUxk62C3-Qn4V_hYiIcC2EDl5hlT71TqAHUfg421727i_L8ZjO2nWFW9l8QroOJA6E8hxLo29RcvfPUmDl9UR-_H-K7ulXcVOu31dekqDi8tHfO6ckAfhM8z4kHku87jprakUMW9-IOAcjN-6JhkuxFgRClWjwbWxznQcMdn2QS4sSded1V2hGWtGjEub7o9e98K6iC4xb3iBVIedHhEmr6O4AztHERZmYXItxnymRJMGqTYWcZSrGJEkhn906n9ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/27095" target="_blank">📅 14:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27094">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caDn_vqq3Ynwhef-qmAT53cCmjeUiIUFCaXhwjIqHYN7a_u2T628DO2NX-4iIV6AAmB844_mEaTWxi4CWJmhqEApwDDUn_KCEgf0fLm-TIU_DviOFdGmsjuemVh21GhLVzMB7fMc9gx-m97ldE0B455afIVobhOIPx3iLQ7VlIginrCbPHiVwKvIOrL7pwZVVASgjPn60MyjleOltEl8fiSCep0b5U31LqwIortIhP3WANg2Wolk8gn9yhuRC2-zT_zYm9IuK6N0GVb2Vpza5B2A2OJbLLIU13xapyRlnjnGIDRU4AQ6CsUQfNT17NUENHXjuoAIFUUOvZ-q4c6RSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
عملکرد نیمار جونیور فوق ستاره سابق بارسا و PSG در کل دوران حرفه ایش در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/27094" target="_blank">📅 13:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27093">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrAZVdYUzd2iD9aAazRVEsbQnKGs9TOd4Uk1AirhyXnPVUOikxtMVH5yDzBT1IXILXNl3--Y2N7scDjELEg5bxfn_t_CGORIOyl7jSinwVkY4haqfw25rO3rKDmAr4OPgGzHRfgm3xvnr3zliro__EPQehFGQ4l1pYS8qWrow4NHVpZq3-tlAT6tMeKgPcT6t2uJxLQNHVX3gWiXg0NbANrh5C0d-Zn23t8fRnGXb9QVU5ZBfGO_PDcSDf6xQRyfVtoQma2Piz5AOLCk4_3oMOJ9BQzC9Kjxnk62h4bE50lOKGYuJraLm5rJ6wMCOiLGDHmOtcLdxP1kwESrafa9iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روز گذشته شایعاتی بود که فصل جدید رقابت های لیگ‌برتر یه‌هفته‌تعویق میخوره که سازمان لیگ تکذیب کرد. لیگ برتر 10 روز دیگه شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/27093" target="_blank">📅 13:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27092">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCLv__LeVHNJe-voGLngWsQKx5wLakL10j_uPcesJZee2fdp9b91gulAQpnIafhpQY1XzytZqIDo2wqXqJvSvRQtKM4J_wSaCNwHCOexbKLXMep1DwRWlUrePuPWKqd849DBMnpK5rgjDLq1Kwlq_yRdqEkETae_-Kc2q3OhW6otHvANJrZCn0izejVHVCARDRzHwZWNnhGYityRPmLFkpDkMsf43PpqjzBBZ79xX_3NntRk-FKYuSNQt5bUHHqTM7jURXOdqd23STanvTyPgjbBXjNx0e6n60bRPJrUd2jZaomYsczISD3w8oTiYgXnClpb2bHwIcDh9doqxaArug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
استوری محمد جواد حسین نژاد ستاره ایرانی ماخاچ‌قلعه: پروردگارا بخواه برای من که مسیرهایی نروم که باقلبی‌زخمی‌بازگردم. کمکم کن جایی برم که دوست دارم اونجا باشم تا همیشه شکر گزارت باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/27092" target="_blank">📅 13:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27091">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9be54cc9.mp4?token=BCz9bq5YPL0lfp8r5auqW3WwOdcag6vAYGgZfwbv8M8C2CU4tMVjnzDKf5C7jAkh4wax5keAId4jsDTFAJVHYHURVqLaIcDukShlkFp4UYHwhtkPTA0e5dLYCgKUZ0ndPUgmDeyTqq9pIaYeHu4t4GkvbIF4V_gDMky8N05CpD4U2WgVrxTWIPdUUZjDoXHlrL2bGY0QwqhOyx2bkbfMNYr3wwAliRC3N6z5uOdtPSHPebu5klXg2l4VqkvdJz7LdFpB3BlJ_0nZMRjA0oPzDWqnKzFBo1K_ar1PrWnkmrKuZ7G3aZoRedFCuLMp4KWSSPIhpzGosESKs4bDewXgeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9be54cc9.mp4?token=BCz9bq5YPL0lfp8r5auqW3WwOdcag6vAYGgZfwbv8M8C2CU4tMVjnzDKf5C7jAkh4wax5keAId4jsDTFAJVHYHURVqLaIcDukShlkFp4UYHwhtkPTA0e5dLYCgKUZ0ndPUgmDeyTqq9pIaYeHu4t4GkvbIF4V_gDMky8N05CpD4U2WgVrxTWIPdUUZjDoXHlrL2bGY0QwqhOyx2bkbfMNYr3wwAliRC3N6z5uOdtPSHPebu5klXg2l4VqkvdJz7LdFpB3BlJ_0nZMRjA0oPzDWqnKzFBo1K_ar1PrWnkmrKuZ7G3aZoRedFCuLMp4KWSSPIhpzGosESKs4bDewXgeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌جالب‌ببینید از نحو پنالتی زدن برخی از فوق ستاره های فوتبال دنیا و واکنش دروازه‌بانان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/27091" target="_blank">📅 12:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27090">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17e27275fb.mp4?token=MqzJ-OB8vVXckVEyhYsW6i62WZauo0gGprQgwNf0QCo-ntTlZCgF1XM6pGsZ6jGL5k-cvG8fz6molrUTK36Xeuql9COtZymwud-XKbWNHJPjHwl3mGtqRuWetptaJBQ1woUM-B1uN7t49gQN_QP0AGZ5YLwd3LyLDbXJp3cLvrZoDX9jxXvKietGazXzUPaiOWE_OT_NDuzbwCcUP8s-OxHiOMqQ-v20tJW4oeCepsU7PBNjkxcloxf2yw2_1TNYwDhJZRUEvT8pavq6_iYx64Qj2UhfwPc34ERWEVTTcJm1tJCvUxPXzu8QCQcgZszE0NaRqLNkVa8JGxGcWQQRlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17e27275fb.mp4?token=MqzJ-OB8vVXckVEyhYsW6i62WZauo0gGprQgwNf0QCo-ntTlZCgF1XM6pGsZ6jGL5k-cvG8fz6molrUTK36Xeuql9COtZymwud-XKbWNHJPjHwl3mGtqRuWetptaJBQ1woUM-B1uN7t49gQN_QP0AGZ5YLwd3LyLDbXJp3cLvrZoDX9jxXvKietGazXzUPaiOWE_OT_NDuzbwCcUP8s-OxHiOMqQ-v20tJW4oeCepsU7PBNjkxcloxf2yw2_1TNYwDhJZRUEvT8pavq6_iYx64Qj2UhfwPc34ERWEVTTcJm1tJCvUxPXzu8QCQcgZszE0NaRqLNkVa8JGxGcWQQRlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام رسانه‌های افریقایی؛ پیتسو موسیمانه در آستانه عقدقراردادی چهارساله با تیم ملی آفریقاست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27090" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27089">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370ff98a06.mp4?token=CwGjIp9Imw5JEBWb2nViqiJkAzYOz6AFOWMAcLIrbsQwKIze5UFGhtymwKipVDtCrHV3cxsRRz0Agj3077gFmzqzjfHLzQCfjwnb3Izxtzt_bSH2uOH2UHC5RAeTY9LAhkRyZ2gKPjsvyoEnRb3JgbbyiMjwauUhn4YVguezaCGut6Xx8mQHAJ_i8KHWl-ppwDuxw7YCUDdJl4AO9dois9dwRNZlShkhySSswjONR6i1CTIoc8eeHms5IZcb85dvaJZc24aZr5otfyjU4lH3ElARJi__OcKFvIK16GfA2RAdBVGb_j3nSzO9VxrVTuva-f4vVJ0OuMv1OPMW7DeI-ropwu_oXauAlGqGl-1p1huqkYQVJc6CeokqYLVUqqYPwu-ZhrzTtH7gAojOwsz_dnAmn6g3fOJ0GSUrW5NwuojZ5kq0fzXK2Zy5E8UeOSYT5HA4NQc_PxFIC1OFSL1vjb9eZeh2zyCvbhO-aoGGF8XVY0Sc9o7H5KUi7hgu8c56KCqwlFcQL8Yxe22_s_aKEdMMCxQfnXVmBKlTNnp1iDM66f1Gazrwf2598zr5pDlZ7zn4i2hCnv0uk4kjKgpxCxOu3uMKB-7eRuhia74rTovtpcuDX94DTYmV2s8co65ZnOiF_wp0Ss_EV9hFyK66cAaEdhCLaD7zRHBFRHONNlE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370ff98a06.mp4?token=CwGjIp9Imw5JEBWb2nViqiJkAzYOz6AFOWMAcLIrbsQwKIze5UFGhtymwKipVDtCrHV3cxsRRz0Agj3077gFmzqzjfHLzQCfjwnb3Izxtzt_bSH2uOH2UHC5RAeTY9LAhkRyZ2gKPjsvyoEnRb3JgbbyiMjwauUhn4YVguezaCGut6Xx8mQHAJ_i8KHWl-ppwDuxw7YCUDdJl4AO9dois9dwRNZlShkhySSswjONR6i1CTIoc8eeHms5IZcb85dvaJZc24aZr5otfyjU4lH3ElARJi__OcKFvIK16GfA2RAdBVGb_j3nSzO9VxrVTuva-f4vVJ0OuMv1OPMW7DeI-ropwu_oXauAlGqGl-1p1huqkYQVJc6CeokqYLVUqqYPwu-ZhrzTtH7gAojOwsz_dnAmn6g3fOJ0GSUrW5NwuojZ5kq0fzXK2Zy5E8UeOSYT5HA4NQc_PxFIC1OFSL1vjb9eZeh2zyCvbhO-aoGGF8XVY0Sc9o7H5KUi7hgu8c56KCqwlFcQL8Yxe22_s_aKEdMMCxQfnXVmBKlTNnp1iDM66f1Gazrwf2598zr5pDlZ7zn4i2hCnv0uk4kjKgpxCxOu3uMKB-7eRuhia74rTovtpcuDX94DTYmV2s8co65ZnOiF_wp0Ss_EV9hFyK66cAaEdhCLaD7zRHBFRHONNlE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ رافائل لیائو ستاره‌پرتغالی سابق آث میلان در آستانه عقدقرارداد چهار با باشگاه منچستر یونایتد قرار داره و توافقات درحال نهایی شدنست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27089" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27087">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1jX43r5mY_XIAU8g_tkAA2Lk_NAJVoFUUz80Dlr0L_4vfIAocjS8o2bGOIujRpK2w8BsTTD1IFL7PXXpsIvZhkgzPLsFuJLnOJRaodAFTlcUM7t5VH3C1ec8mUKPhghfp2xmEKOiwSqIEUFGZV5l3waMtOwtnYslIUoNSVJuEbhPi2zF2_q7chOCbsnbfHHA2rJDFQVAlrk5Psc14tWR3LISt5dgXckOmp6BBR_zOiOwOZCtHQ_ZgBCE8fCw_xZjTthqp4xZsyu7v8uo-9C3890on0czieYDXbOi115rvtdkVJImpbwP_xovj_kYv7yXfSg6GmidLxVkdH0Sw4owQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینکه‌گفته‌میشه؛ باشگاه ماخاچ‌قلعه رقم رضایت نامه محمدجواد حسین‌نژاد رو 4 میلیون دلار تعیین کرده کذب محضه. بار ها این باشگاه به مدیر برنامه این ستاره اعلام کرده هر تیم ایرانی دو میلیون دلار پرداخت کند و خودِ حسین نژاد هم راضی باشد این انتقال انجام خواهد…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27087" target="_blank">📅 12:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27086">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPrB2hvs8uZFCyWnPTSZC7TKQqgX-0VnPD6sYWGFeQDOI6crnCE2c4zHEmOyRN8YumYK2ZSrcv-CxMVYQ0Gleup5N5HqaKbJ9Fqf0w7jOV5Biob7uppOyL0wR-ct_fb2Lctlm1YJI2rPb7Qqzb7OHFip8WWONrSOq0H6JQgkllS7TJihuM8U8pbgPR38MvpLOjnbqp4WztkrldlP54IQxOOCx_L6WGNPv-CB5MZ4PI3I5d-v6ovA_OJbqRJaJ48CJL6MsXtLRBjMZmKRem0zKSsu6dDUWztLJm22VvEWyx_u8VTU_4rUHYAtb5TJiuPyXKD06r9sSCWUYnPjVT08jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رودری ستاره اسپانیایی 30 ساله باشگاه منچسترسیتی:من‌تمام‌پیشنهاداتم‌از تیم‌های بارسلونا، پاریسن‌ژرمن و منچسترسیتی ردکرده‌ام و تنها هدفم دراین‌تابستون پیوستن به باشگاه رئال‌مادرید است و مطمئن هستم که این انتقال‌بزودی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27086" target="_blank">📅 11:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27085">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xiia39ggZ0_jCkpF1nHvnyGkZYsJC4JMD9dXVMIG75fULweuKUfz0xFV-qRkt3LKrOj7EZo3xyvmFSfpakKwkFQ_ZQzZjTAPPVV1o2-1nZaw-QKkoQaiJkNAb0M2gPlEI5chZpOHdwOQR1H23KdIr9aDv9phECvzz2Kq7BzQQAgb4eTkmKXuzHpaPjIffFWbJI4_jTWkdocmoPUndfFDn01vfv0W6H8wN4eaKf4037moy5TyPm9ZaRQspGdoLq4fRvOWsWJPie7J-H9j5FlSyVeOK55LQT1L-aFYQRpPbmOr2OSCdKEg0AAH69l3WtdTIhx51iWcWdZuhEJLAz6pag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیویی یک دقیقه‌ای از سوپرسیوهای تماشایی مارک آندره‌ ترشتگن در دوران حضورش در بارسلونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27085" target="_blank">📅 11:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27084">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYgc6KdK3ca94_OlsUt-LeAXBrLURkoWhhUcx539LZGz0JmhZbuayl4wsUTY1rqTuFPMGaxfMsblV3DryWNtb1VFAQYVMtj3MOATvgZGW5Nn4ynubeAxT9XZzXrz-7rli85ii9iux1tGOhLIVeD11rGPMMwkQ25nZwTA86n3UAqhlLPupJ7_Wpp-_V_jzk8kAeC7RFXZzOmTORIsFZoo6s8if0a6AynXABrd87fZLBWmqcOg5XPHyULr2LALOzgv78TFq7YwBGOIX2tfvVjje2KEq45kgPl6KVBEf2daVO8hKLzKrB89izdpIz626DE_rMR8gdxf-4RFKXqJ2uIAjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27084" target="_blank">📅 10:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27083">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=oNr1qVIzWPW0XvULUVwSVd7RV_sXKKdBmjMHiVndia7bb4ODZQkdPeWw8-D2ZrWE_kubIAIK2medYOBCilDQ91zuOlER5YpCyBiOXeDY5guFun3jGT1DP7AzfCJ9oPMcwGz9eb1pGpmiXXA-AlHOvNjgSbgUMfN6s4MnkF7ft-cij8gdTJvliM9j1aaAP2dLsN8xoISWwjuv-poZaonVj7GjSL_DGFAMEfYbI03w_TIcg0f6C3OOfWZBHyBnCuw7wfXjJYwN105NVn0otsDX5JPvLYo6nEQbfPLjju_25GOltcdzSoc60xuGPDKQEuZ0eoirxIvRNt4ck1-k526G3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=oNr1qVIzWPW0XvULUVwSVd7RV_sXKKdBmjMHiVndia7bb4ODZQkdPeWw8-D2ZrWE_kubIAIK2medYOBCilDQ91zuOlER5YpCyBiOXeDY5guFun3jGT1DP7AzfCJ9oPMcwGz9eb1pGpmiXXA-AlHOvNjgSbgUMfN6s4MnkF7ft-cij8gdTJvliM9j1aaAP2dLsN8xoISWwjuv-poZaonVj7GjSL_DGFAMEfYbI03w_TIcg0f6C3OOfWZBHyBnCuw7wfXjJYwN105NVn0otsDX5JPvLYo6nEQbfPLjju_25GOltcdzSoc60xuGPDKQEuZ0eoirxIvRNt4ck1-k526G3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هونگ‌میونگ‌بو سرمربی‌کره‌جنوبی درجام جهانی ۲۰۲۶ مجبور شد دربرابرمجلس ملی کره حاضر شود! او توسط نمایندگان مجلس کره جنوبی درباره تک‌تک تصمیمات تاکتیکی‌ اش بازخواست شد. از تعویض‌‌ها و دعوت بازیکنان گرفته تا ترکیب اصلی تیم و سایر تصمیمات فنی اش، همه‌چیز زیر ذره‌بین پارلمان قرار گرفت. هونگ در ابتدای جلسه هم از تمام مردم کره عذرخواهی کرد و مسئولیت نتایج را برعهده گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27083" target="_blank">📅 10:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27082">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAwvMJN5foY2eb7A82WUCpyX-Y3IKbiEkGnz8RewLHt28aJcrRW84iRER7xseREYIv7JI076XIGtA1ktKultdOJmuOCwFE4nDiJzeHJN2wiEyK_s0NeKRyuM_o-cOfO3uOXapmUDe-7_YGvjptfymwI1kogtUE2dHA2x3FTJF0Forn-AhEJw6L8N2JFZcOrIoyXYpkHvIpMC-vTB4SrKMt-AINKXs2Z14Kqotq_02rICZx4J89lEfvTk_s-TpXwtOzUAq1qgFwuDVhJaIOWiWiv8BF3pQaVtbKWVbYvF9Va0VAYz0FoJKr9e4SAPxieSsZw5msooCjNaN3Lj-WlR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
نشریه‌مارکا: انتقال رودری و یان دیومانده به باشگاه رئال مادرید نهایی شده است. بعد از رونمایی از این دو بازیکن پرز پیگیر باستونی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/27082" target="_blank">📅 10:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27080">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGBpdM5bsFWcWdEbifFVwzs1C-uzmmLweHgq6IsDEl9YYQmziAweY9tHu2RFH4VAhAprG4L7E1iUuJnAF4xBtpx8KRu12dbeYlgoL000faRQGiwudojMLrLnqF8vJ02ai1PUU9a5cYAzPDdVo0Wn1is7cmwd25I-jD0N6IIib3Kdcj0YhfNm9UwHTc0uWWPoX19URFx5JVi4wK-ZLnNYDfw7rYhCd0npFgLmlQ4OreCEsHGQCSNqRkaEHsf7PgLYCqZy_4c9E49N4f2iZg3fGNlJ_qVTNg2AF5gl-m8GsqmW7v0ETotJg9fFkY_7dfuQDWaDAyDDi5Hc1bdjWVLkdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه‌جهانی تیم‌های ایرانی در رتبه بندی قدرت اپتا؛ تراکتور تبریز درصدرتیم‌های ایرانی قرار گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/27080" target="_blank">📅 10:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27079">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNaD2x1kQPUjvN6IcLaHhmyUdnhEq7Nnprl38NMk9J89LyenMcyTbDttN2lUnPzh8Uh3GX_JWdvGA9gdurnDSDOKHmdB4tZ_fPh2XpPhvAwQIkhP5M8Bx2rugggf2zkTDazrrJ5ESvLaGk0LxDrbWAy4zAWD7tXJF9jGxVaVN6EhGD-yYwItYrQOwpBaCJmOyam8FvrFdXGhbYEK5wHAsltON_1l7Op_8fCdHdJRC2wUROi0Na88ozVustS60ylu2uyDKHCuSMe30FoXbCA2sXS8NrW43JKjiyob1o2zBIYI01b0dtduUoZkdXFjbrYjECWwlZmnG5l6FhXNE-pUoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق اخبار دریافتی رسانه پرشیانا؛
سعید واسعی هافبک تهاجمی‌سابق تراکتور و مس برای عقد قراردادی دو ساله با سپاهان با مدیریت این باشگاه به توافق رسیده‌است و بزودی باحضور در دفتر مدیریت قراردادش رو امضا خواهدکرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/27079" target="_blank">📅 01:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27077">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvK_ZqYgpWAMhW1diGBcz-LEUeu2YpPmF9KjQbV4oOAsjrHQI-2cXXFnbCFUdAJBgkwhacmtd09pGTjOTRqnfsdsTauPbwFAuBwGWUH0jEBQpaASSIILM3Lte34IC1bL7VUp-xIYTcvDolYPlzBTZvHZ6GM6cvQA8QbdjtD9ZvgRBQtAoar_Jcdnxb4Zn5BLLNpNU0nzksB4xGBg0iOmf6xQ9P0fWlLuytGGqAdC3afARm1GJvZrjcMU6vpA35ftS8aLexPW_eOuB5nEH1HYXCbxQzUq6lv03MZg__DUwD9K6ZUz_VyxqllJPo64joZ-GkemYketPBshGK3hoxBwXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی و راحت باواریایی‌ها با تیم میانه‌جدولی کی‌لیگ کره‌جنوبی
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/persiana_Soccer/27077" target="_blank">📅 00:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27076">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPm7R9lOAQw6LeDTIuj1xD5jwNpUai-oUVTqa83SdXdmsu7l3rp9oyv3q6bZvWDgn-19cj0nCFJkcys1hKQn042oLzcY2mrcU1vQFCvQ4s2AGI_etO78bcjgn6VbiJmIfr8CDj8WaWQ9q1Vt42BUTLSkXv_fLgachwQGNhAo3uwczTY4rB0G3B6fSah8Zy4fAy8jLB33Upp36TtTGaB09W7riEbHOaR2MwFMsoeqtBHg2DlCyoSEdJvlOrdMe4SwIDf2VgQtOHvMoFBkn7JQgpuJt9-T5CEKD_dafNQe-t9cWWP7_Ch8IWxuoYeqvxihFxuoNC2RX827FFXIFnyyVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
روایتی‌جالب‌از آیمن حسین ستاره تیم ملی عراق و زننده دومین گل تاریخ عراق درجام جهانی: در سن 12 سالگی یتیم شد و پدرش رو از دست داد. بعدش داعشی‌ها داداش دو دزدیدن و هنوز هم پیدا نشده. بعد بخاطر جنگ آواره شد و یه‌مدت هم بخاطر اینکه مخارج خانوادشو قید فوتبال…</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/persiana_Soccer/27076" target="_blank">📅 00:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27075">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCh7sSTsj0iBLbO-wcjDKKtXeIRbe4ANLc_dY9XA0fOAx-0UQAAlSJHxGWpflYPdvWqDXcVk0i1PR4rGiR5e5saBieB0jjsVe_meFvlKEWDbwI7qmRRKEzxKDjXrgbA0d7Gokx--XaMu3yZv7dfcf2d68ycSFmowT9sqbOm8dQPo3DgFw6WRSTlojeKX9zaLO2dlQEK8ufju03SfmGwa5cQHL0XFFO2eX_SsJbf6SqkSv3zeGIRGi-YcUJL4FR1gcUdt7eX-XSTBNrFHbC9f_tur8Kifn-QsZOECZw3w39irLUdUMsELJWRJrXvrKbkC-O1bMFUGs2sriYdpf-11OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
محمد قربانی میگه‌الگوی من از بچگی تا حالا کریم باقری بوده. حسین‌نژادمیگه‌من از بچگی طرفدار مجتبی جباری و فرهادمجیدی بودم. خودشون با زبان خودشون دارند میگن که دقیقا فن کدوم تیم بودیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/27075" target="_blank">📅 00:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27074">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYtD633CLTbm7mgBiBgkO_9GMmCvAQyZT8paZQYxnNfclYSTCwFUeAU0cxLnGwvJ7_hWJMX4DyOfgumsjY_ayABjS0Abzi6a7PWjgkrpNaN-ju8Vfv9H51xeTqrgUukmcjYwpiMe-XtZYoNSEW6xiMZAnWK5atQdUgzqTD3bGe81i1Jyzbk0osLLXpz9ncvZfWCnSWqW9TJB5h4FmMHbkClsTwy5J3AFGa6xWHSi0LRdYmTnL2sBj23-Lds3tglSsceNI2ITXxwmIikVl31b0wOErAfrytisyguFdcx9sdJLje0Zcqt3-FS6dzM03CcxGdMSm_xZCwPU3QJeamvW7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/27074" target="_blank">📅 23:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27073">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XazwZawBYga5aGqd9kgtWU1b8Us52f5i-e8orqLluQ7AmhseQfwTlxmJDm9dP1J3mW1FUfccYiOsSlcFtXHBuuOpxXeXVpO3FeEdWvX_0CJyyUs83UivMhxOg5T14MH0yQayDOpOWxyZ-JcuqB-1r66y6Du_JAaEP6eDaWZE1RdZirGsbiD1BWNO2ikkNy5Q_Mk-i93X2ig7k7EmSQeuqUTl3-d5Bt0JS3JIJXrRjWxAy3KrC9wKAcFC45GFKvmgjIjZYkROqvifoQ7RfH1UlJcMaelAKSc4PooaUuRiNylpxr-bjxVeHB8aRWJJYlipsTHCM0m0x4Cc66RIuu3teA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دادگاه‌عالی‌ورزش "CAS" روز سه‌شنبه پیش رورای نهایی‌خود را درخصوص‌پنجره نقل و انتقالاتی باشگاه استقلال خواهد داد. اگر رای مثبت باشد فیفا پنجره رو بازمیکنه. اگرهم رای منفی باشد این پنجره نیزبسته خواهد ماند و با شروع نقل و انتقالات نیم فصل پنجره آبی‌ها توسط…</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/27073" target="_blank">📅 23:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27072">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ff8ICi9YNSDOZT0VTHKHOsatzZtIapQbwEYaUwCXvKRDdlLlI_ou51DgH4138UGjjDTWq3HhMTOfInYt_XzZuXTeEv06PJfx2juqEnje4ztY-TabCICs_4u4dFfQVwXHpCPUFMRrnGCVRH55ic1IzJLUnpzKJPgUoKoDVA8djA_nwq0FZlWm5nA3_P79SsgfOmiiQOFshWVaL6xqkTi7i1R2JgSpeWh-cmfZy3CEIAUvcYjY8-JK-cPGC-ZAYkP-VjWzOzCJmp4wNUqwYdzafLdiLJoM5WasIAnPExrJnfQXcy7Z9qM5N3KBiEKfLdwOzBHQfKybjAwyiBx9Ag7AdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
اسکای‌اسپورت:الساندرو باستونی مدافع 27 ساله تیم ملی ایتالیا درخواست جدایی از اینترمیلان داده و به مدیریت افعی‌ها اعلام کرده با جدایی او و پیوستنش به رئال مادرید دراین‌پنجره موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/27072" target="_blank">📅 23:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27071">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C572c-205rGYRib8A7sNL2Hm3ixWqK12Q6Kl1qlQzM6gSp8JHsYdp0JorXkHY9IlToD61mKAE26n-CHusKwVOIaVA-vcUo9MF7Y005fI6KwZWmqShgbuHuBBNlf4iZaiQYbmyqcl0JLPMp3QXfcqZAYXC5NoguovQokQh-D4aBwnYOK6Sgh5VWV8XDzfdLU6ECVSsovZO_LeSqYhx1Rdq_Ypy2MGSkJQ5B7vNnm8gupRdY-9FIfNTyWmAgy7qYTXFv9lLArjLhAuW3pPZINTC6z52EnzH8dEVFMkxeLJ7L2baYOIS0XL1fGmuZVEqL2LuEoRZmVqfqN-juBMbdx-fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/27071" target="_blank">📅 22:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27070">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/St72TZGdvRzhyCJEiwSJN2dTajOrmpP_Eu05L1IRZxijnzJEzkSXlYouLkDRe5gAYY2ASceoiVuDOxNMDiqjY5QagdR-LacNqDuRp2ZSs4chBf4gpS3JC9ir7w6Zx7TS-zV92kZnMocKSHxBmYmBBd6JW5pSsnV3I0wlrK4dapYd-dgkiBnyXHSeva4Lxiqfc2ntCl1J3WOGt2ZzRZSHLXQuPXTogjQarPFgkeyqDIJc3iuZw_SClMjc2VZiszyoIcGLgcmfPwhKzrh58V5hvukB6AklihIR9XWs6cJ-dXyw6DBo4kkbL5MH_zRlDvumqCF1kNtsG4lGIOjpDywdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ دونالد ترامپ: این آخرین فرصت ایران برای امضای یک توافقنامه خوب است. امروز یا فردا می‌فهمید که چی میگذره. قراره به زودی و به یشکل دیگه، مذاکرات پیش بره. کار خییییلی پیچیده‌ای هم نیست. قراره فرداتنگه هرمز رو کامل باز کنیم. بعدش هم در مورد ظرفیت هسته‌ای…</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/27070" target="_blank">📅 22:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27069">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZZ2dLUv2i1CJucQ1vW-XAq1PMn-2Y4AS8qp8asnGV8DLItKMx6toTTMOytr0gHgUX0LMB2ISw8XXYYv4XcyWTqtA9zhfTmT-QRW4sADxYUSLKjsCcNCHKQUc5vrt0QSRiErSRnikgzeHSee6S58gem2mwGv_tHQZdY5WGhdbFM0nhyyGx0r0SHM_N9BEEPk216NxX2-Ih5qx2PE8Hu_IwyXSXJlFOXPqjtAH-EkAdtRPGv9QIwSyyBmmmSGH1XlNCaD1WrQ9srW97SoJh6EULgOi3GpMvEQzX8xCSVHrwXlIbbeBgwqT1cGnZMA9ovdSD7IYg5ccCS_5id16w8h1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/27069" target="_blank">📅 21:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27068">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97c6b80b0.mp4?token=pc8UOrS-iyJWfga67TB_pOANvq5rtKMLJ-VgP8Vgdwz9XaGLD-dDttoabAa7-QjKFBdcYD8_QafUrVt9O4nb6LWcNc6mbCU8ZBYxfBtOGQ0V7tdy-pNG-guncUyJGjZBDosMsfvNY5tIJzUasnx5LoYi5v1R1lN35qGo0C5GjLOUDwAcK-TWStsgqqcOaBFusQyLFANmqA2r1MkkPwD6XYR_ZJPgWl67scP8UcVcypySY8NGxa0hWS8xbyRKOfvNjpIvrWOlew_K4JnSOpghJ-ADhi1rnjSdOUxhkawPRzluEiRltEp70oRfrzz1E-YLrauUb1FiF3a1sly6lfR_Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97c6b80b0.mp4?token=pc8UOrS-iyJWfga67TB_pOANvq5rtKMLJ-VgP8Vgdwz9XaGLD-dDttoabAa7-QjKFBdcYD8_QafUrVt9O4nb6LWcNc6mbCU8ZBYxfBtOGQ0V7tdy-pNG-guncUyJGjZBDosMsfvNY5tIJzUasnx5LoYi5v1R1lN35qGo0C5GjLOUDwAcK-TWStsgqqcOaBFusQyLFANmqA2r1MkkPwD6XYR_ZJPgWl67scP8UcVcypySY8NGxa0hWS8xbyRKOfvNjpIvrWOlew_K4JnSOpghJ-ADhi1rnjSdOUxhkawPRzluEiRltEp70oRfrzz1E-YLrauUb1FiF3a1sly6lfR_Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فصل آینده تو بارسلونا میمونی؟ فران تورِس:
‏من‌قراردادی با بارسلونا دارم، اما در فوتبال نمیتوان پیش‌بینی‌کرد چه‌اتفاقی دقیقا خواهد افتاد. من هم فقط منتظر هستم تا تصمیم درستی بگیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27068" target="_blank">📅 21:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27067">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d787366ec9.mp4?token=KhLHhNbwNpvKWUaH7d3F0K4oHqW-IbsSSfgf30nAG6ltHUKcZYXkubO-owA_HeqZXxygUyoztFwrbxnm_RMrhKxGKNj0i5ITn0Z4zdVqDOy_O7F8n9Zq_PIO0hUAOtzW5mVAxoc9Zd6cdMtRQSZzM8MT535bKpy3KXBGwFdMz_SIHvXyrr28eqMsqmxAAKY-u1U0eamqNeKT4wJRLnRKXl6q0Y_q1ecjtyFWqwkMGS2DfjW4wXw1csR1hqcqQi7PAg5Rog_F8YWQhCWROPWtGCJeZOclVitfp41xb2ky1P_eXWTyTsx3x4vFSYxeogFphanEQEZRkOIUReCF82WzLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d787366ec9.mp4?token=KhLHhNbwNpvKWUaH7d3F0K4oHqW-IbsSSfgf30nAG6ltHUKcZYXkubO-owA_HeqZXxygUyoztFwrbxnm_RMrhKxGKNj0i5ITn0Z4zdVqDOy_O7F8n9Zq_PIO0hUAOtzW5mVAxoc9Zd6cdMtRQSZzM8MT535bKpy3KXBGwFdMz_SIHvXyrr28eqMsqmxAAKY-u1U0eamqNeKT4wJRLnRKXl6q0Y_q1ecjtyFWqwkMGS2DfjW4wXw1csR1hqcqQi7PAg5Rog_F8YWQhCWROPWtGCJeZOclVitfp41xb2ky1P_eXWTyTsx3x4vFSYxeogFphanEQEZRkOIUReCF82WzLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
دلیل ازدواج کریستیانو مشخص‌شد! حتی قیچی‌ برگردون تماشایی به یووه هم‌به‌پای جورجینا نرسید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/27067" target="_blank">📅 20:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27066">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7tXzwg8eLCDPSYY5L6ZydS_NRAI1VYo6a_foeYS0vjozzdiwmUdZRYLmhyBcSljDonL7A1-CzYWYhAZJxarUluraiW5meyrii9DmAfNMs7E9woWWoedFxqA_F4SiE71dbtbKE9uBvhL8vK4-ed6LvtCbxZcJZpeeb9jwwqKUiwRhpo7-ywA-BppAEJtRNRQ4CDuKTQDOfzEnwETdcpGyyitCH5vro0UWisRowxwe9JL5z-NLE76TfzuYPLHT8l8albUkd9XrHfD_EvaYiRmMYfROUwox9rodHGpxTJijINy_MjE69IgjD9njhvuhg--01pOh1XLr3cpCC0tsfgv7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛
یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27066" target="_blank">📅 20:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27065">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-usbAKYtTA9pD8aBz5TToV3-4lpEZEqC7UuL-gVHBW4Bh-JcmNMaN3jD9maK4glkSkeUNG2kvxfolrM9el63v2yum2P4RjHLdhFFbiv457w0UhHheFD3HaEmjb75osEKvv9B5zJDExoV51yVB6R6uGQ66cxNvKLBdJXAhc3s2o9QTQT6yy2iMi303LnVhbckF2K1yAnLKXaf3F1al1DeFv4Iwe_mqlm1_M48FY2_Fxe46iYYdK-2zqlQ0CmRTb-5HHLcp4RhgxnIF5-mEa2SJh6LkUDcs25W5WmsF39UbrSgVhxA_3gxKdLXZT3DPfs-ku1FWsV_PzuCSsXrdCGYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
عبدالله‌ویسی سرمربی‌ذوب‌آهن:
دوست دارم کاری که‌سال 95 بااستقلال خوزستان کردم رو با ذوب‌آهن تکرارکنم. بسیارسخته‌امانشدنی نیست. امید عالیشاه مذاکراتی‌بامدیریت‌باشگاه‌داشت اما درجریان مذاکرات نیستم. امیدوارم که قرار داد منعقد بشه و این بازیکن با تجربه رو در اختیار داشته باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27065" target="_blank">📅 20:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27064">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ba-r7NYat46GGzpYbkKwxKDmWkgidwRN-5Kph5L8618O0UWgRuJJQtryaeLJihXUIC2e0thuDwGv7VVS7Nv6d5vWSuse4nHDgdfv3nbM9ujFmh67bf3ImF6XEKPrRn8hevbDOqmsCnJmYFJBqGaCM2hnFabotTAU3LjB0QBYgY7u-vqpekRv1Bkn1nNcTh9LhNNjmz87PKE_E3GrIN08bBczZ9ES3aWEK8DNdA6MAIRVUydvifkEZkpIk8IXWxbwXzOcYiK7bakLqexRp6qJrawk1jqAvs4L9lJD2nyhxQTy0V_N0F5inwWoOAe0bsgZcaA0qz-8fSjtz4Z19F_-bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
تایید خبر اختصاصی‌پرشیانا بعنوان اولین رسانه؛ اولیه هدیه ارزشمند سعادتی به زنوزی؛ هادی حبیبی نژاد ستاره فصل گذشته چادرملو با عقد قرار دادی 2 ساله‌رسما به باشگاه تراکتور تبریز پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27064" target="_blank">📅 20:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27063">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmI4gBemIc2U7OHCIas0h3nFb6zdWyg9lBRqEm_BWbC4D_VJtgT8nyFvkkcyHPMxOqjYya_jyMR0Jz8CKCIygC6QigeaWyuAGHI5w40IaV8ESnGljuneI1jc7IV9Ylm1ERK-oeKu300p9Dwy_8ErXicsjbKB5Xf9_jRfzbhki-SyYx29oJnGAu41dlujqewvZWZsIMWDCsqWRYkz5yDk-BYAVQgqY-XwbO2aDIGL7IXVsDxl2zvOcK23U3WW7CsPCuuvJbz0lEyiK4XStm81TjG1Yhm6Q-B1Jp7t-jPZntJcmnrWPYSFelu3wCFllqyFtEjxn8lcSd8U7I2B_TCL5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27063" target="_blank">📅 19:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27062">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab970d5a0.mp4?token=dIBBKmYYsch2ZtcErH2-t5lvpHjLfaL0YIZMWxDh1z2bzsOMKca5Vc195KJ88mlsxJL8A_p_sNcWhOSqbbeMmpOllAECgMqIXTxoUTaj9UVbPGrg0QVyMgiuXFKrWRxM-8LwHEpTca8MoMvNTFbJKJk7mqN2Ckfn6VBG4I3H0jAtNGG8zIbhbezRpx9_a8ZhSm-PKzL4ssjCkdfApJnJFBV5hNa_hKPBlPNy0tiJe-op3b9HsqGqyZ8M4tB-UiPJ2-DufijXdMB-0KaLIhr52e4EIW_MtYXOLocOioD-ATWeJS_TgZsvIue9pxrtJ--lppTr2dGCGVprwOxaAdW9LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab970d5a0.mp4?token=dIBBKmYYsch2ZtcErH2-t5lvpHjLfaL0YIZMWxDh1z2bzsOMKca5Vc195KJ88mlsxJL8A_p_sNcWhOSqbbeMmpOllAECgMqIXTxoUTaj9UVbPGrg0QVyMgiuXFKrWRxM-8LwHEpTca8MoMvNTFbJKJk7mqN2Ckfn6VBG4I3H0jAtNGG8zIbhbezRpx9_a8ZhSm-PKzL4ssjCkdfApJnJFBV5hNa_hKPBlPNy0tiJe-op3b9HsqGqyZ8M4tB-UiPJ2-DufijXdMB-0KaLIhr52e4EIW_MtYXOLocOioD-ATWeJS_TgZsvIue9pxrtJ--lppTr2dGCGVprwOxaAdW9LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ویدیو بازی‌بیلیارد تو اینستاگرام 224 میلیون ویو واقعی خورده بود که یه رکورد محسوب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27062" target="_blank">📅 19:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27061">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hxgj0GEmPgNnwRXNlSlWIfJxTMx-8luWKrQM7VZDXIW7Zx095y103FGEMF-WumqvcWwt_bO4PMw7wgCDsIBfEdJstAHvD_HTaehbwgK_ekqxkk8ksZ38CuJy-P8YEE5-kReDv2DKhNjFoJcSV57Jb8eRnhStNECmDnM8TN60EO40fEde7eE0HvKn99vNsV28ZHSpehwkddwEGG1gT7LphNnyWyccgWyN0qmEWSGVNlMC8FsXCkw4pFsbF3OvjZZ7ugDawGAUqLkS0xwwfHvEn8z7gLPIK1t6qXVuvmN30gO3LHfUCkt26OMlO2arFdV1dEZPZFaOU1wyVx9Wi_Nrag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27061" target="_blank">📅 18:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27060">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhWD6Uv1CBdg5mMXgYzLdFUIsntS2ZHeuy6SpTvaapcNR5EI-o6W6RW4cgnMVzH_oZS_Df6W2TAxVLz6P7MGbXg2AWyBLO8oTC2jARk9CWUszhNFlIvKeT954BK0oftGriaRt9f4d3XZd_vCG_Tg7hvjKnBmsIPEPtdHBqNrueGVV7l9DeZzaIHxLMxqcfklEAwwLd1Fh5PYZiATdCAie_KKX8DktqE0C_S5F1EA7ykv_ZcWJ_QjVJS5tB8cJIBJNKwFvP684ILHPOaDnL2YpdnAwUAGGCdzW8RjQ-D6G6Mh7T85yg9WETKNJ2EGdCNULbch2wfXcSxS5r9N7C7Rzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ نگاهی به کارنامه لیونل مسی در دوران حضورش در پاری سن ژرمن در تمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27060" target="_blank">📅 18:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27059">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYkBZW4hrCVu0eiUjSK5WHbT9l_6fTCzQUn1vmimnV6NdmYd4xvDfPNOcJfDgiN4esqu3IHkiXTrxUy7s1L6zkGmzmycjXpX4_n_ujzGz16rN1Am87epwZ1SCJI17zrBQ6LBCi6MhWmRQNi6qpYb0XKO49kSClVigSKNWsH90LAqD__g8FI1RWR5kg7lPzHYH_dJJPyem5ITzDJQFuHUnELkhX-lYQZpbZLYhVNdFmhreSuReysByFdbmhVlNCsXIuDgIcIenkgvH_eT69Nth9nGiAqA74Pm9ectiD02UELmlmLuklkX5fbWgQuqQ8RbGv93HE1VBdpvvfFok5C8pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛بااعلام‌فیفا؛ دیدیه‌اندونگ هیچ مشکلی برای عقد قرار داد با تیم استقلال ندارد و این بازیکن بزودی قراردادش رو با آبی‌ها تمدید خواهد کرد و از هفته اول رقابت‌ها در خدمت این تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27059" target="_blank">📅 17:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27058">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbcgWgAHxpHmq4rAl-rbsm1xcisSkaynjrOW878npRJq91O-IFF3wo04AHm_XzotWNtAjfm4la76qBj_3B-Hzf9zeC5qsxxaW4Jv1DzPKfg8-KH0DYafBy4bkqIafOKSL7bY4nsWlz6S28Sfb1YyqdH6E0T2BQjsAc6DpG31V61BZh-Ds6nFm9k19QKZOwIZ16hUwlE4BhHQTQ69ZgnvfHbYljEGa1nPKKVpTOYPmhF88ruC7QrMNbcTjCHlVxQxC5jgx5miQqRcIPdudMk6sLyiOmuXhYSXk1N1irGsMigp35A057X4Bl9T9J5kNyDez_7rVpSQl4VUHKKrWIQ8PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هانده ارچل: من از بین تیم های اروپایی طرفدار منچستریونایتد هستم. علاقه من به یونایتد به زمانی برمیگرده که کریس رونالدو در آن حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27058" target="_blank">📅 17:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27057">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPfd3jUB1MWorlEzAt7ITBSYgaZzloH7wSAvaVimNfiC59lBT5Wdna8rbosUSdmI13GCg9RGnwrF2HHYoImlYb8CN5G_7OzgiCWlqOsZhR5NFPdVZLRzkrv9rmfcY6vPcPoJLNmrEwukEqq-oDGEiQIhrcL4g4GtZqxzu2fcYdvh1xNv-d4JNR3CL5MAX43C5MjJ0I295YYUqH8lCAPP_EqlXrQQ6LySBTE0ujuJwGbM8c0UustOletlYGse0KHcrsnXH74ii-T0tKdmOQ1elUcOccjzkn2s86rz84roGPNMSdPsYaA6RTs_z5JS37IUr0N0DH7MMdAMSGQ169ocRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27057" target="_blank">📅 16:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27056">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfPqe1WZHEWs377Y1JO689nkrLIxeEEwdCOUEdt6FoJ9X4czTi9h94BUKG-NCOaQqy-N8ECM-Fovj9e8e0Rv_YdC7F_IhIFe7vysD_G0ZUYEbUKO2bl931s861maXwadAyfoAIbDWPguENHt7HwJqDGREUYe2sLmwloSipzSriAl38KJ6L9c2JINZKln4vKHCRM-GkZvIvH1-HKPNoCPqL4JwzPkPgXstosXqXC-IE8VVsIQc6-vco1H2nnkgvJA8XcxTovQERQL1z0vRFPXJq1sJJk6iTc7sKZu46u5sd5m6Ndgf9_MJmlE4J7l0dJLo4RXON7O9ZuFK7K291U3dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ سید مهدی رحمتی سرمربی‌گلگهر ساعتی قبل در تماس با مهدی گودرزی شاگرد سابق خود در خیبر به او اعلام کرده که پنجره باشگاه استقلال باز نخواهد شد و قید عقد قرارداد با استقلال رو بزند و راهی تیم گل گهر شود.
‼️
رحمتی پیش‌تر نیز مانع حضور…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27056" target="_blank">📅 16:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27055">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5cqBIzdo7LoucZEVCpoc_fPKCARegNTgfyBtIdk5CWiMZoMqdG5Irv3nKEbasZF6EaKAEycE8Ften1Mv0b-ULvbKfhWAitl0TD2GPRAppuWOtMwqlXy2raQ5yoI_72R9U6fS1qcaaZ-F6tkRD8PWLk-VHBlK-7bb0OJ2f-jZNkpk2ettLzmaXJ_cspiB0SBUQFIf4mdzDKf2GVYC4t3b8E12i_xQFhjhwuO0IkYQ0uXYPCbFALh6gJs5DpGCLkBSa0EqWkHB2GRMAAU_ZFXaOLEIEOyxpAWlpljpH2Pr6h_TljL83SIv9GZe-KkW0FTDf836jnwi_I-aptw6-cMOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔴
یکی‌ازمسئولان‌باشگاه‌ملوان‌انزلی در گفتگو با پرشیانا مذاکرات و توافق باباشگاه پرسپولیس بر سر انتقال فرهان جعفری به این تیم رو تایید کرد و گفت تنها مانع این انتقال مدت باقی مانده خدمت سربازی اوست. درصورتی که فرهان جعفری بتواند کسری از خدمت بگیرد این انتقال…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27055" target="_blank">📅 15:54 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
