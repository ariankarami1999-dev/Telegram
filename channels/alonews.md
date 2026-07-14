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
<img src="https://cdn4.telesco.pe/file/OFmAsl6AJkLnCDdVMTYWn0Nvq4a6zMxJkG7jW0LVOWH0zYiDhf8XYAfIYYEbtUaHMt9KBURRypRn607pWUJOE9IA78uZwioSJPKGswfd1ruU0z6iQaJjwa_BrpbbqkrQDIMzzOSAIY8XouiewMkIyl_W8k4UZ_TZHpL1Y9fEuCUrb_jmqcLUhGAAT4zBwd5_mTMUXrD1FFB1Y6PyvCrUKEj30I6qGNc51Udtn9IPVyPkf0rwqP9vbr5CMKDo7COiNh4M2nKEZtAf1ZOiFsmmKu6rN3csrbxgZw_emlj4uyQ8zgNyC9piy1cPnelRsnxLk0FKWmc3CzW_uMN449fR0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 918K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 19:38:12</div>
<hr>

<div class="tg-post" id="msg-134112">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
صدای انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/alonews/134112" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134111">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ایران اعلام کرد که زیرساخت‌های شرکت اسپیس‌اکس (SpaceX) متعلق به ایلان ماسک، هدف نظامی مشروعی محسوب می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/alonews/134111" target="_blank">📅 19:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134110">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9Y86jN_gQO29cZquWUKXuV3w3NlQhPldG0Cdh-yD-9LL3wvE_llOwJ_km5VpDsgFiYkBRCO0zcnyZj-TaDy1pi94rInkvmYdfwg6DB5NT1pJLDmftTlijG3yrogN0vWxRgk_j7CloaoFzeDdJj2rlIrw9vsE8wEi9XutaKmUf_8MIpIh4fOPNKkFXATddxoOHZlcrWlI0va4So6X1EdvfX6iPaCXeQpc3H9F96Cp522cua-VyVuOJ7H4R8dGd2vAlCFpDnheuHObDIhQ5mRE1L0mr7Y1AHHGWH86b5-MiH1PRJGBW1Kac6YLB5QTBJ46B88_2bjlTZf4PlpRmPnRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/134110" target="_blank">📅 19:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134109">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1ce5aae87.mp4?token=XhfIcvbYmqj9-AZ8YfySCDy5D2bu-XEl2Qu2aej0MWVDWu6T9wsJg9G6Y-QM1q2aHTFhFKX37oAzotP5B7NToHnGx7tkugH2tKGx3G4rKs4_Ay9SxcaUBq1ZggcMgpE_NbCpU3R_EZJm86p-hA5FottxMcm8IPrcwLFO6q47NP4FusyPx5g5J3aVLjBoS9xd4o8jcuDlRdAuhvRFO58rmz8UtZHXpVvpClv4dVVwpwk6jtO2OLX0nrGv5p_AbaRbjLAhuY4VGeLYR-53IiGhCaEWFsZviK3MXFEXUcIIxaI6BaXmsafBdE7R5HQWiZi1on4S1k9vMvxPPCdvyWKWZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1ce5aae87.mp4?token=XhfIcvbYmqj9-AZ8YfySCDy5D2bu-XEl2Qu2aej0MWVDWu6T9wsJg9G6Y-QM1q2aHTFhFKX37oAzotP5B7NToHnGx7tkugH2tKGx3G4rKs4_Ay9SxcaUBq1ZggcMgpE_NbCpU3R_EZJm86p-hA5FottxMcm8IPrcwLFO6q47NP4FusyPx5g5J3aVLjBoS9xd4o8jcuDlRdAuhvRFO58rmz8UtZHXpVvpClv4dVVwpwk6jtO2OLX0nrGv5p_AbaRbjLAhuY4VGeLYR-53IiGhCaEWFsZviK3MXFEXUcIIxaI6BaXmsafBdE7R5HQWiZi1on4S1k9vMvxPPCdvyWKWZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ستون‌های دود در کویت، نزدیک مرز عراق، مشاهده می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/134109" target="_blank">📅 19:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134108">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
شرکت آب و برق کیش :  قطعی‌های موقت برق اجتناب‌ناپذیره و بررسی‌ها برای تعمیرات داره انجام می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/134108" target="_blank">📅 19:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134107">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618a7045f0.mp4?token=HYY5URvMC_-mEN_vI7DX0p4YE4GSOKhEyRQc1SDooao_-mlch-e2r_xV6FGMJ8Q68RppU6RMLScl85vsOR2iGRct_NPvqH7niatAAkRSJYZRaTliGcnY7t23gblfQg1IjPVqDElEVxsXbGAkKh3DfJSIZPFxZ9d-qXTDydJg-6y4fpD1b31udtakAvlZ6U6ptcf4wA0F8m3-alFeb6OJBQ9QZdiPnej9v6zvGHN2NAHWAbQiOFqammxlT7n7ToIUop4XWMjs7E-JheUhTWoJshxwJHn0KwND5mThsf1TsLhevogxGFKBwi6gykZ5nAxL62aAHC2jruR8R2sn6VTXqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618a7045f0.mp4?token=HYY5URvMC_-mEN_vI7DX0p4YE4GSOKhEyRQc1SDooao_-mlch-e2r_xV6FGMJ8Q68RppU6RMLScl85vsOR2iGRct_NPvqH7niatAAkRSJYZRaTliGcnY7t23gblfQg1IjPVqDElEVxsXbGAkKh3DfJSIZPFxZ9d-qXTDydJg-6y4fpD1b31udtakAvlZ6U6ptcf4wA0F8m3-alFeb6OJBQ9QZdiPnej9v6zvGHN2NAHWAbQiOFqammxlT7n7ToIUop4XWMjs7E-JheUhTWoJshxwJHn0KwND5mThsf1TsLhevogxGFKBwi6gykZ5nAxL62aAHC2jruR8R2sn6VTXqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
علی الزیدی، نخست وزیر عراق که به واشنگتن سفر کرده، در کاخ سفید مورد استقبال ترامپ قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/134107" target="_blank">📅 19:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134106">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
صدای انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/134106" target="_blank">📅 19:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134105">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوری / اخبار تائید نشده از هدف قرار گرفتن یک نفتکش با پرچم لیبریا در سواحل عمان
🔴
منابع خبری گزارش دادند یک نفتکش تجاری با پرچم کشور لیبریا در نزدیکی سواحل عمان هدف یک حادثه امنیتی قرار گرفت که منجر به بروز حریق در این شناور شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/134105" target="_blank">📅 19:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134104">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
بر اساس گزارش‌های رسانه‌های دولتی، شبکه ملی برق کوبا بار دیگر دچار قطعی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/134104" target="_blank">📅 19:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134103">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
فوری / انفجار در سفارت آمریکا در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/134103" target="_blank">📅 19:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134102">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فوری / ارتش کویت: درحال مقابله با موشک و پهباد های شلیک شده از طرف ایران هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/134102" target="_blank">📅 19:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134101">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
فارس: صدای انفجار در قشم
🔴
صدای چند انفجار حوالی ساعت ۱۸:۴۵ در جزیره قشم شنیده شده است.
🔴
صدای دست کم ۵ انفجار در جزیرهٔ قشم حوالی ساعت ۱۸:۴۵ شنیده شد.
🔴
ماهیت انفجارها مشخص نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/134101" target="_blank">📅 19:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134100">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnqIMcHUrmvWNo15xPCHBkLcvbWqCNFr_57528BHNpHnMbX8LOsghumeVU6Wpeqvt07ZDLlDkf7GNXOzaXXx3rQC9cPC-EdxORwp7W9P25EL345k4a-7qAfVuy4LyntUHcODfK-uI9xOuWaSvBbh7N-ZdGEtyIiNYtxgGH-Pn0bbrx2X_r1BwOhz24VVIAr_r3u5gGyVvzHc3dDjGwu4FZbKvtQ7GfXqPVMHITIT4SN7mQbEeDmPXik1Q2swNesj-QnTx3jVN0kvMtKqqqh1-ahiUoSAgMD6NOUCP-Z4kRSZh3Qn-usxx_LnP6fnDD8XjorKfzuThbtgXR3MjB_5Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: در تاریخ، جنوب ایران همواره نماد مقاومت در برابر استعمار و پاسداری از استقلال بوده است.
🔴
امروز نیز مردم نجیب این دیار با صبوری، ایستادگی و پایمردی، روزهای سخت ناشی از تجاوز دشمن را با عزت پشت سر می‌گذارند.
🔴
در کنار و قدردان این مردم وفادار و مقاوم هستم. ‌همه جای ایران، سرای من است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/134100" target="_blank">📅 19:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134099">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری / ارتش کویت: درحال مقابله با موشک و پهباد های شلیک شده از طرف ایران هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/134099" target="_blank">📅 18:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134098">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imGQ3a6rtgQoeT2QqjiWC7HWt8V8YqqB-pL8H2rgAEFlAuFw8GrUSyEflmOlGLII6b7nzLmghr0bxQ_Fme2kRwWBcNmjFFXYGNmVxDSVNF_HgZdGqOKV9Hz7HZJJTBsCu68dK9jvqSowKGgrrJ-dME21z9vOwgi4dE3_5pt1Ho81I8O0sAaW0LvtRRzFAfZVPGe_Tbfp4uG2sXVVIHvRgzf_jHlSMBhK22KpPrPse-HUL5fbeBLs2bHgk0VefI2G1L8YXASahKCJkcMH4b2IIriGnZQSSB80S7EEG9SlVcKRvLjQsO16n6EV3nOJzG5e3xnX4yZwSWbfGlLTIiHguw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ: ما یک محاصره کامل خواهیم داشت، اما فقط بر روی کشتی‌هایی که به بنادر ایران می‌آیند و می‌روند، یا هر چیزی که مربوط به محمولهٔ ایرانی است را حمل می‌کنند.
🔴
همچنین تصمیم گرفته‌ام که هزینهٔ ۲۰ درصدی بازپرداخت ایالات متحده را با قراردادهای تجاری و سرمایه‌گذاری جایگزین کنم که کشورهای مختلف حوزهٔ خلیج [فارس] در ایالات متحده انجام خواهند داد. آن سرمایه‌گذاری‌ها بسیار کلان (عظیم) خواهند بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/134098" target="_blank">📅 18:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134097">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
آسوشیتدپرس: تلاش میانجی‌ها برای ازسرگیری مذاکرات ایران و آمریکا
🔴
خبرگزاری آسوشیتدپرس به نقل از دو مقام منطقه‌ای گزارش داد که میانجی‌ها، به‌ویژه پاکستان، در تلاش هستند تا آتش‌بس را احیا کرده و ایران و آمریکا را بار دیگر به میز مذاکره بازگردانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/134097" target="_blank">📅 18:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134096">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ: ما یک محاصره کامل خواهیم داشت، اما فقط بر روی کشتی‌هایی که به بنادر ایران می‌آیند و می‌روند، یا هر چیزی که مربوط به محمولهٔ ایرانی است را حمل می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/134096" target="_blank">📅 18:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134095">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ترکیه حکم بازداشت نتانیاهو را صادر کرد
🔴
به نوشته «ترکیه تودی»، این حکم موقت از سوی دادگاه عالی کیفری یازدهم استانبول و در چارچوب رسیدگی به پرونده مربوط به توقیف ناوگان صمود - که عازم غزه بود - صادر شد.
🔴
فهرست اتهامات علیه نخست‌وزیر اسرائیل شامل «جنایت علیه بشریت»، «نسل‌کشی»، «صدمه عمدی» و «شکنجه» است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/134095" target="_blank">📅 18:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134094">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMAl3reYVVB3H6BaHlItw_odOpah7XeNZcDIhY2C1r7-iokfgkCVYBQPgXsFKG6mPYMGL9YG1j_LJnaQaql4LfPmjhP9qJ30O4OWp_hT809n-ABhGUCuc0s1PJF_a3SEQ5smBiFZTB5B0UKEZHUluN2i59iLsqEQzgxvwUICk1xyIvimWYqVtTKQeoq0rx04VOIWwYb9jA0w1Tm1j2pAU1yq_-mX7vMTA6E4YmN2oDevEkk3yG5ED-BNEi8ErAR2mYYnCgk8w8Jw08X3Q7533UntFO8OVYa-u2J-MIEcbaNJea1cJ7nGAbLuTZ8lZqvgKv9MWTjgJ7FyM1xU4uZMxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نقشه منتشر شده توسط آمریکا برای اعمال محاصره دریایی بر ایران
🔴
برخلاف محاصره قبلی که از سمت دریای عمان کنترل می‌شد، این محاصره جدید هوشمندتر و دقیق تر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/134094" target="_blank">📅 18:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134093">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
بمب‌افکن‌های بی-۵۲ آمریکایی در حال رفتن به سمت پایگاه دیگو گارسیا (پایگاهی که در جنگ ۱۲ روزه توسط بمب‌افکن‌های بی-۲ استفاده شده بودند) هستند.
🔴
امروز این بمب‌افکن‌ها در پایگاه Guam آمریکا در غرب اقیانوس آرام سوخت‌گیری کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/134093" target="_blank">📅 18:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134092">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6xPaFmiuZfpbCejx1Cfd1axxO8iRTwMhDnP1ZtTatDLdHypfiRgoW3vH1nARTkeixFMEIaN0kTiIv6pPNFz3pY0pDgM4bD09cxYeS3JvvheHCSCZ6gEs6uNwMI5dVJYAYvda_SpjxaIhk3j74i7mBHFSQCbyy99tmgVCNrfEvA9R3gpqkfQxANWqSMzT0ilVUtiDGeF2EkOe_5RU8jfG1Q13OQnxAVR68EtRAxH7T8wgAtg-e2M9JXpda9Z_dtMb-wOsE82BbYuMNXkd3N1MF8U4ZiWrYyPTdpor-y1A6ukD2-zlyuQtqpgjWny_AtjSCeYL5b78SCRxP-QfZVOnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
شاید باورتون نشه اما حدادعادل برای اینکه معادل فارسی کلمه کنسرو رو پیدا کنه 64میلیارد تومن بودجه گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/134092" target="_blank">📅 18:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134091">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5vYCXZHYyJ9UWKjMUTfPborIL5c-qI_tiqtiq3ktq7Y0kp6FNImNG4Ksq4kqGAfbugmsQLVvc8FbISAjmMg_l0VrzD-9aJQdt1EbHdcKSXuakidMtkwW7fxZ0AiRdW4CcumbUFRUtD9_zB87WUFTnjSM5LULB6dvJmRPh1pq3PVhv9J0hDH7ZRDecfyL8-jzT_WczO5-mdDgKWTMjYi_rU6sosKzaHYgtujV3bDpzW16PHxCbp9NKhbgnbhRCEMwb1mON4GBshd5PLuPSFom_u8_9tLehSWrTXwyHIL1-CAGORdnc0ZOwDkghdq2YktF8LWp9BGw79XOdg8rS7dYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ این پستو رو ریپست کرد:
"اشغال جزیره خارک!"
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/134091" target="_blank">📅 18:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134090">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd0bc9aa7.mp4?token=kmrzJslDW5Pa6Yt3zDkn6vrKhBsL2k7ePptt4ReZ1K76TgE6j9cSzkHI3a8DARcAreyCk70I4V-GDDc7_QrLZXGsQbPoZXaYxx70ctKj0qMm7QtrwfW3LFUOUEyg1vDe9ByyHFGla3VKQG6ETzd9_dQiQObr9hhfeJ29fX95qUgotxjoyFsVuuFrg3LoeSriDL40R5wa1szp1onolsIotgMdKIIaSwM7JkWOyvmn13ljyUysTTTWAH5-dYP2ColcrL3lqWIsG2XXnkkme7kSLs-DJmx2HokIU20iB55MFkceJlg8VnpyCjQuqoF9P-p_I2AEHK7xYRLaTu_CP7LJQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd0bc9aa7.mp4?token=kmrzJslDW5Pa6Yt3zDkn6vrKhBsL2k7ePptt4ReZ1K76TgE6j9cSzkHI3a8DARcAreyCk70I4V-GDDc7_QrLZXGsQbPoZXaYxx70ctKj0qMm7QtrwfW3LFUOUEyg1vDe9ByyHFGla3VKQG6ETzd9_dQiQObr9hhfeJ29fX95qUgotxjoyFsVuuFrg3LoeSriDL40R5wa1szp1onolsIotgMdKIIaSwM7JkWOyvmn13ljyUysTTTWAH5-dYP2ColcrL3lqWIsG2XXnkkme7kSLs-DJmx2HokIU20iB55MFkceJlg8VnpyCjQuqoF9P-p_I2AEHK7xYRLaTu_CP7LJQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حداقل 20 فروند هواپیمای سوخت‌رسان آمریکایی در فرودگاه بن‌گوریون اسرائیل حضور دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/134090" target="_blank">📅 18:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134089">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGQ06knYCqmFss4VPpDihN_CR1zJsmxWbfQK8-ohx51BSN5N-Y5YuC4zTsNQhNv2FOTRAjQAHnhpUjMz9L7Ucr0-dJhM7eTShhQeiJCtCjqLr05TG5JSb0fCORJC5_dDydCEz9wl3aet0B4MtqrcOnUCIw3ZuC_JQkThUVL8krz3fmjesmVoMq4136YRB_dGO1iTNtYEoGFuXsdyhGb9_BOwbImPebnp1PjKi_dfSHujDwI3iwfG-CXGVKESxD7piMREJqE90lqaMW0kfVbXjm4HeZmETljulX8n3pSS2aLHIy60ptGyZTWrkaXDvoozwxuVCk_xdiQ77h1zxpDLSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم‌اکنون ۵ فروند هواپیمای سوخت‌رسان نیروی هوایی آمریکا بر فراز منطقه خلیج فارس در حال عملیات هستند!
🔴
همچنین یک پهپاد MQ-4C Triton متعلق به نیروی دریایی آمریکا پس از تکمیل یک مأموریت شناسایی، مراقبت و جمع‌آوری اطلاعات (ISR) در سواحل ایران، در حال بازگشت به پایگاه هوایی پرنس حسن در اردن است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/134089" target="_blank">📅 17:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134088">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
توانیر: از فردا قطعی برق برنامه‌ریزی شده در شهر تهران آغاز خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/134088" target="_blank">📅 17:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134087">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: ارتش ایالات متحده تصمیم گرفته تا بازگشت برنامه‌ریزی‌شده‌ی هواپیماهای سوخت‌رسان از فرودگاه بن گوریون را به دلیل تشدید تنش‌ها با ایران، به حالت تعلیق درآورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/134087" target="_blank">📅 17:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134086">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس:
آمریکا رسماً وارد جنگ با ایران شده است، دیگر یادداشت تفاهم نامه ای در کار نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/134086" target="_blank">📅 17:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134085">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkJDAhWXra-RghSyIXt-sB2qrDqlflJQsWrjxUUWMfNdB_Ay9NQTv5Z5KoZ3CLiOmp--YrlVCb368e4bK6oc1hgGAe9iJx1l5-c4yb51PS-8YsZf2cpEO5ziOQgQUcmRRyv77Fda-q0SK3y5NiboDqXdIqSN-b0P_4PsDMZuUf6UhrcwKmBiUbqYFRpp15R4gxISZQO_hcrsmyJeZ1tZoX_WM8hfXwcN-H-OojjPFrjPZu71zKoUYHD26mf_3lZgYoNTtH7NbJSVnvXrASGoeSp8wYmZY-dbipJUuAtRaxLi6EvM83Ue9TkexaEefJVLjtvxkzTjrdMIQPwRklc5QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت ترامپ در تروث سوشال: وزارت کار اعلام کرد که نرخ تورم سالانه در ماه ژوئن ۳.۵ درصد بوده است، که بزرگترین کاهش ماهانه در طول شش سال گذشته محسوب می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/134085" target="_blank">📅 17:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134084">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bk_UHfdNAgJ7UqX8-bkNwieDKAY7cD12sDImcC4o3ba5B4jwyOsjQlBC8vy2jpj13UKh6kZMaDiUo6TBkfMusMktVICOr1a34LL_duL5-k4_IqUVI3XWem9QnjWEarTVEawTjKziz1z3myc33aYkylJ4dwcd-LGzsc6Pt0F5A5SI_IjHmIXG_deVDG8VG4glHFRq1nTxfaz8wwU4FxYJX61HLosp-PNiBthd1FmvWMyc8LplmcjiI35taUkevrZzZEY50ds1QhbDGQX4UHkAmajapbVb8dDk5cnLSjSeQAIazbKkfehcS4MA6lcyZy7N4MdPGs2MGzChYWwLmIbVXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ در گفت‌وگو با Newsmax گفته است که راسل فرای (Russell Fry)، نماینده جمهوری‌خواه کنگره از کارولینای جنوبی، می‌تواند گزینه‌ای «فوق‌العاده» برای پر کردن کرسی سنای این ایالت باشد که پس از درگذشت سناتور لیندزی گراهام خالی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/134084" target="_blank">📅 17:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134083">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که تعداد نیروهای آمریکایی مستقر در خاورمیانه از ۵۰ هزار نفر فراتر رفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/134083" target="_blank">📅 17:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134082">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏
👈
هشدار یمن به شرکت‌های هواپیمایی بین‌المللی
🔴
رسانه جنگی یمن، نسبت به عبور هواپیماهای بین‌المللی از حریم هوایی عربستان سعودی هشدار دادند.
🔴
تمامی شرکت‌های هواپیمایی از عبور پروازهای خود از آسمان عربستان خودداری کنند.
🔴
این هشدار تا زمان رفع محاصره فرودگاه بین‌المللی صنعا پابرجا خواهد بود.
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/134082" target="_blank">📅 17:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134081">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
بیش از 180 نماینده مجلس در بیانیه ای خواستار پایان فوری یادداشت تفاهم نامه با آمریکا شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/134081" target="_blank">📅 17:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134080">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ca9fe379.mp4?token=m_FcXj4l61hqwYPOMYVSQnlIws2cDg9inLzU_9qbRimKWzp5j-X-CgaxXeRbgdphFQ3g4VzsfkGZHXcSvU9ove6PG7BRPkA4PLZniwIgN3NvXTGC-6xl4Zj5PhwcPlVEUCI-5VTu6rEdRbz-QzwuIw0BJQ8ybskmN9CLsh3yXyl9pRvNA0ciDi275AXE6vJEZazVV8OupjIXCsGpiM9vcOo-0jrYdt3lYFfVBW6q58ym75lGTcZue70bGWRkrXA5rn3WIpqtpV_jE4t_SEqqAhxwVB1oFTAmNHDH8XRs4-PezuVhS-a_xqu11tEAv2tuZIhXA7biqcnGF0qKSkshFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ca9fe379.mp4?token=m_FcXj4l61hqwYPOMYVSQnlIws2cDg9inLzU_9qbRimKWzp5j-X-CgaxXeRbgdphFQ3g4VzsfkGZHXcSvU9ove6PG7BRPkA4PLZniwIgN3NvXTGC-6xl4Zj5PhwcPlVEUCI-5VTu6rEdRbz-QzwuIw0BJQ8ybskmN9CLsh3yXyl9pRvNA0ciDi275AXE6vJEZazVV8OupjIXCsGpiM9vcOo-0jrYdt3lYFfVBW6q58ym75lGTcZue70bGWRkrXA5rn3WIpqtpV_jE4t_SEqqAhxwVB1oFTAmNHDH8XRs4-PezuVhS-a_xqu11tEAv2tuZIhXA7biqcnGF0qKSkshFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک جوان: قطعی برق بدون برنامه ریزی ۱۸۰کیلو بستنی منو فاسد کرده، خدا لعنتتون کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/134080" target="_blank">📅 17:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134079">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4vXXPtbrS6n3bG_rQZMuDIDHxxQgYQlB5bIFFvEdjd6qO64ropgl_qAEjQM8bx3JweZGFQuxZn1W6zoH4FIusZf5_plTSR0Z73PQO8KLYKlpq_3svhnj19CA-VbgQhDKZxXE4FsIEKfiNwkZQRxhr91muZDd7naJTdtN_c25a5-7lp0dw-Ez7jxyZdUiXbQAUjZgQCFzcGrBCsDFfsXU_IXQEH5f-AmvcZuOt068RQyfZKzXubQ89EclhMv3YWMf8PiHP0Q9EBbCP4Z1pbzNFq-5YNqwXunLXI7B97-YrFToMjSkdaoRfHQTtRSwjvtbLZwNMZPWbu7b1Vr-CYtsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آیت الله خاتمی:
هدف تندروها و اسرائیل یکی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/134079" target="_blank">📅 17:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134078">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rluat0rikufE9K7ZjxOxge-ALGhqIwJy6i6SQiSS3h-qOBitAlLZNvH8De7CjNjjEiqkUJSeDBwXPSveKNFacdVYuEXp-iEBlwnow_VNVOInlHYtHi-lF8amBWxTiZzN-rk6W70ZWj8DdqVeCfuOJPYchgD_6aAW3uC3QEIWxd9azqM_sBODXj979rK4xF0g_Y0gqRdSWnqG4HLQrrXx5ozDFjqmIKov5lMZPft-ilf1HLy6_DOtPOC0I0bylwz_VkqKM4JCxUZVAm71Tc42CoID8nQwRBn8VjZ-FKcxTtsrK-JEsOr3EdRvmKexPw1Lbnzojj2ts7c6Oz6X2mbgWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط
سکس
چت بیرانوند لو رفت
😂
◀️
مشاهده فوری  موقت هست و پاک میکنیم
😂
ببین تا از دستت در نرفته</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/134078" target="_blank">📅 16:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134077">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
فوتبال 360: امیر قلعه‌نویی 140 میلیارد تومن از پاداش صعود تیم ملی به جام جهانی 2026 رو دریافت کرده؛ اون قبل از بازی با نیوزیلند، پرداخت پاداشش رو شرط حضور روی نیمکت تیم ملی قرار داده بود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/134077" target="_blank">📅 16:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134076">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEHCTRclTZGoFknRid4K1jQl_Nm86q_ZYsSrUSiLP4lm0an-3Vn1XK1xNKlnqgpN23m2RQu6mVyIbaNhz-z-5vOf-yeKh3boPkSPnG6xfjx5Tqjwb3K9ePPsZ-wQieZw_FF2HgDTiYO_8czn_HO-ns4oJZDnot3abXfR8peVR0U3XCvrZdc8E0csILtsTUsCAL4ApKVhbZtNCsFASPvVOt7JQv7k2WaHCHibXdRsIKYZjxMTqukdSBOqHEmw9RAGXxfFP4TskwS04PmuQzo9EUmaO-Ve5dkrHh24hsbmkAD7ifr2cBeFAGzpSoXXsQLudLnSSbAVMJ6P1pC6-DfHgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رادار کلادفلر:  طی ۴۸ ساعت گذشته، سهم ترافیک IPv۶ به تدریج در حال افزایش است/ نسبت ترافیک عبوری از این پروتکل در حال حاضر حدود ۲.۵ درصد از ترافیک کل کشور است
🔴
پس از قطعی ۲۰ روزه اینترنت در دی و بهمن ۱۴۰۴، دسترسی کاربران ایرانی به اینترنت از طریق IPv۶ مسدود مانده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/134076" target="_blank">📅 16:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134075">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHToqw9EyfIYiytCLJ_IE94RVLq3wSLYW6mgyTxxED-KKdWrNif-fkw8O9FZiSnNSiq35DYvqppzNUAw0_TelRDqfeDrFonCYc-NHCDrb2J1DiF5o7F5vzptFeERczUj5_1Q-ri06j6rsoik8Gm9jj5n7WNeFsyVUyRcoAq-y5uwbFfmlxjqIsJZ-lqIoc5eG4K5p6TiaWmObz5jFUBXmIAIXo3KTnNXOlOiKj3aXKyQlqMJUmjVR2YDZTlbuPCrmio3xnWkHLQfaXVT7lGAyjAhqJ33vYDpXJsUvEYnw_o4KPwE66s0818tl5EpxBihe6-2CoCxVYwlM2CQGYT_Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: وقوع آتش‌سوزی در یک کشتی حامل مواد شیمیایی در پی حمله‌ دیشب در نزدیکی سواحل عمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134075" target="_blank">📅 16:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134074">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
شهرک‌نشینان مناطق مرکزی اسرائیل از شنیده شدن صدای یک انفجار خبر داده‌اند.
🔴
جزئیات بیشتری از منشأ این صدا هنوز منتشر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/134074" target="_blank">📅 16:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134073">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KG8Wr4P4979i1421DTEBDUHDLUl30COc3y6hzwu4kG14I6ibzgnX5p03flhLRkTyq58IKUZ2D2UFhovB5Cseyt5WFBp35-fEKbHtKqiDVadxOhrhwMJFywYuT57UXgXj9Z6HjfTkJd3KBq68DI8j1YNLdyDFbO3ayw9L7XXCGQTL39C3cgor9qkyQeVsd4lZ-kBbHZSmxEJFRBG8aoNkL9cBskA_fqD4os5F7SCjZSTTQbTM4QL4tqwGOKwNJm6EffgeZ6rji7rI6YmjZeLw1x0hn8Oe5mOKRdm6sXm9kz1OilO488HXZW0YGSTNbc3RI_Jbu_uKklPc-M847C6hVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نهاد مدیریت آبراه خلیج فارس:
تا قبل از تنش‌آفرینی آمریکا در تنگهٔ هرمز، ۲۰۰ شناور غیرایرانی به‌طور هماهنگ‌شده از این تنگه عبور کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/134073" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134072">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
اسرائیل به جنوب لبنان حمله کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/134072" target="_blank">📅 16:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134071">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
نتانیاهو: به رهبران ایران می گویم به حمله به ما فکر نکنید زیرا پاسخ ما بسیار قوی تر از قبل خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/134071" target="_blank">📅 16:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134070">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ul187_dIjH6mLmzpL0r0b131yH0eSIrnmPf2EHVZV_I5HjSnGGGELW6gcghCsx664_J75Hwer9h6rbb54uRP20vY21fcdR6rn1oVhfKR2ysst57Se-koUYmqP71B5DoEZXwPAgJmhB9dJFsSrnZN3mzrvr1r0qCLu-ttaxPytvlSH5i-dB3eVj8U3qoamsIfctrH0nGdFEryv7qUjHst2zWmtFgylSUrW-zps5qElerpa3K-6U4ox9e-pnEIP6rhtPJN4Zua9lO4SIg_ijE4nOVbMaPvlUCafL7kN8LvbJC_eriYYZm0qQRWpWibzs_YaUgqr7_ZMOMbDvTEJfRKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رحیم صفوی، فرمانده سابق کل سپاه:
سال ۷۶ ما ۲۰۰۰ تا موشک داشتیم. رهبری گفتند این تعداد خیلی کم است و ما باید چند ده هزار موشک داشته باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/134070" target="_blank">📅 16:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134069">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/134069" target="_blank">📅 16:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134068">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-wCrdaKCD-NT0SX86pWixl0wJdKdOYtTxbKzKP_liqiO8VJ4QZcMpO6Flslo02oByNZ0bQAg2HzqLkbNgGfXutCCP5WuaJFdYxTxDOtzORJiA5avLwHLUynsLCssDlmFDOGwFeR87t-f9VRjBxyk3FMURSvQ4uJ0cBJkudysFvZgqEr6emNAIP4-ACZi1glOYxTG8cK8GO9bEKTpKqMbNxCpu83B1NEesSlttQxFrslkhDbY01fhq_vZCs7W4WDJu-a9o9JpGwTRm0oWrlCaz-xjZh6imX-MMOHIDFee1TVp0m3QzBSTffqUI_pg6B98KQQTaiJ76CvPk2g8JEMaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غلامرضا تاجگردون برای سومین سال متوالی به عنوان رئیس کمیسیون برنامه و بودجه انتخاب شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/134068" target="_blank">📅 16:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134067">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97470ef355.mp4?token=Hlk5SvB2-WZtzlmPr84qMRP7JAr9FpIOvN8YcfK2zUwyHCcIKlX9MgutSZONrcTG1WYtPxYOD7oRpOYsOi3NJd7Dcdj832OWPMhd4bbWrCn3EPDeQa4X__tgSuELqN-odpvx-Lr3p06mtZsYk8N6iLTiSdFElWkaoAwe_cBe8pjnmITb4pEw--NCeOpUNkG6pw2hjpyvN2z4mXSyvVY38merMOKcQMCjZgK6jA68Gym9U0iqJwwzdHAae7xtFRVAlyaQvSWEtR-A5LLSc27sI6JWpuAoyCMuBEumFOfWE5PyJSOhg1ERWmF2GCdcH3DlLTKa1seOA-4yP_3Ainz8sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97470ef355.mp4?token=Hlk5SvB2-WZtzlmPr84qMRP7JAr9FpIOvN8YcfK2zUwyHCcIKlX9MgutSZONrcTG1WYtPxYOD7oRpOYsOi3NJd7Dcdj832OWPMhd4bbWrCn3EPDeQa4X__tgSuELqN-odpvx-Lr3p06mtZsYk8N6iLTiSdFElWkaoAwe_cBe8pjnmITb4pEw--NCeOpUNkG6pw2hjpyvN2z4mXSyvVY38merMOKcQMCjZgK6jA68Gym9U0iqJwwzdHAae7xtFRVAlyaQvSWEtR-A5LLSc27sI6JWpuAoyCMuBEumFOfWE5PyJSOhg1ERWmF2GCdcH3DlLTKa1seOA-4yP_3Ainz8sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روسیه امروز رگباری از پهپادها و موشک‌های بالستیک را به سمت کی‌یف شلیک کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/134067" target="_blank">📅 16:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134066">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhG3PMDCY2uMGbmBwIgie5HYX_8dPcsp96AJvvBZ2maORCfN9s4xpIV4Ibq6OPLCy0z6eEUupVFzoHXesC5hemTFOwzXo5S6k6UknfC1a8J0X4L702CPnuVvdr6l9VAnMhyC-cOYEFJYRYtipQdENPUIFctLAp1svRlR2NqIlW82RTYQRRgeWxrfmTkYK2TMGz6tGO233fbP7rky41up10cDTruawUsEg8A0ZP-fPT8Woq_g-mBsT8GIaIG3X6Palyqr0T3iNNN0ehsk_1VnKhhpXhmndn4qTH7m537ro-9VeFsiH1QQ8-8em5pOPZWqnUvJVw3v4LXYuBcIGhWQMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جلسه صبح امروز دکتر احمدی نژاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/134066" target="_blank">📅 16:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134065">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f6da19594.mp4?token=p_omIrwdKccLZFw4bHKrwAZY1faQbvkSTSCVFvxmjATBOnLulWeZZQCqmIwFV9Z8Ik74IiXSLMsDgA2sqH28WRq3-mdnyytjNEc_avcBftHJgG32OambXbwJR18n0OoNcYKHCDDuUPjPenVfsp0GIx4lk44cwDChv4wehKkLUNXW5Q8_Gz56QqUvSuAfN1l1UOiRLvGijqTgWHRmqLkbyFraGaULaMUhrvoLyw-QA5F_6HYU0bh6_Z3POEOnCKQg0iPtb_sfn3TITfHu8ed9eHN3JYh9Trrizlnt6ZzOrw-IUYMNc-8nMryzxI03wQf2q9V3ljC0RoaGp_WN6QG6mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f6da19594.mp4?token=p_omIrwdKccLZFw4bHKrwAZY1faQbvkSTSCVFvxmjATBOnLulWeZZQCqmIwFV9Z8Ik74IiXSLMsDgA2sqH28WRq3-mdnyytjNEc_avcBftHJgG32OambXbwJR18n0OoNcYKHCDDuUPjPenVfsp0GIx4lk44cwDChv4wehKkLUNXW5Q8_Gz56QqUvSuAfN1l1UOiRLvGijqTgWHRmqLkbyFraGaULaMUhrvoLyw-QA5F_6HYU0bh6_Z3POEOnCKQg0iPtb_sfn3TITfHu8ed9eHN3JYh9Trrizlnt6ZzOrw-IUYMNc-8nMryzxI03wQf2q9V3ljC0RoaGp_WN6QG6mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی که یکی از سربازان ارتش آمریکا منتشر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/134065" target="_blank">📅 16:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134064">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
سفارت ایران در ابوظبی: ۵۵ صیاد اهل سیستان و بلوچستان و هرمزگان که به دلیل اختلال در سامانه‌های ردیابی توسط گارد ساحلی امارات بازداشت شده بودند، پس از بیش از دو ماه آزاد شدند و در حال بازگشت به کشور هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/134064" target="_blank">📅 15:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134063">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‌
👈
فارس: انتخابات ریاست کمیسیون امنیت ملی مجدد برگزار می‌شود
🔴
یکی از اعضای کمیسیون امنیت ملی مجلس: انتخابات هیئت‌رئیسه کمیسیون امنیت ملی، در هاله‌ای از ابهام قرار دارد. قرار شد امروز عصر انتخابات در سطح ریاست، مجدد برگزار شود.
🔴
علاءالدین بروجردی و ابراهیم…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/134063" target="_blank">📅 15:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134062">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک کارشناس:
آمریکا ممکن است در جریان جنگ با ایران بین یک سوم تا نیمی از ذخیره مهمات حیاتی خود را مصرف کرده باشد
🔴
این موضوع نگرانی‌هایی را درباره کمبود‌های آتی ایجاد کرده
🔴
یک سرهنگ بازنشسته تفنگداران دریایی آمریکا می‌گوید «اگر امروز سفارش یک پاتریوت جدید بدهید، تا چهار یا پنج سال دیگر آن را تحویل نخواهید گرفت»
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134062" target="_blank">📅 15:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134061">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f866843be5.mp4?token=PQQKX4-hRQjYyf1NPNqoGmxQz5dWssAG2Mo7deaDGlhpPnxgFRmOaweJnlI_ioeB42qojzGEUUQjqzn5ViI7MbatCiWWtB9-d1IB2gYT4VIWR4TJskRL3uIiaWCQSp2BAdW_l4iLTQWNMkKuFgm4WBsdu_uUzvQv08flXa5yUU5ODX5gFXIRAXx7pafpNJRsnjafMQDV9HOGQSAj4ofrFDYvMl5IusFzpMf3Fff_OZP9r6L801PgTv3kjJ6mj6ZCeq5-v2-ON8EWahXOrcOTl4AcasvtbgR7o2xZ6tyFGdhz0-ukfS2MGdu9MjO2J-xjfhGpGvjpQuOyUDj8QXCT6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f866843be5.mp4?token=PQQKX4-hRQjYyf1NPNqoGmxQz5dWssAG2Mo7deaDGlhpPnxgFRmOaweJnlI_ioeB42qojzGEUUQjqzn5ViI7MbatCiWWtB9-d1IB2gYT4VIWR4TJskRL3uIiaWCQSp2BAdW_l4iLTQWNMkKuFgm4WBsdu_uUzvQv08flXa5yUU5ODX5gFXIRAXx7pafpNJRsnjafMQDV9HOGQSAj4ofrFDYvMl5IusFzpMf3Fff_OZP9r6L801PgTv3kjJ6mj6ZCeq5-v2-ON8EWahXOrcOTl4AcasvtbgR7o2xZ6tyFGdhz0-ukfS2MGdu9MjO2J-xjfhGpGvjpQuOyUDj8QXCT6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیام صدراعظم آلمان، مرز، به مسکو:
زمان آن فرا رسیده است که به میز مذاکره بیاییم.
🔴
زمان آن فرا رسیده است که بر سر آتش‌بس توافق کنیم.
🔴
زمان آن فرا رسیده است که خونریزی غیرضروری در اوکراین را پایان دهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134061" target="_blank">📅 15:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134060">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
آژانس ایمنی هوانوردی اتحادیه اروپا (EASA) به دلیل تشدید مجدد تنش‌ها میان آمریکا و ایران، به شرکت‌های هواپیمایی دستور داد از حریم هوایی بحرین، کویت، قطر و امارات متحده عربی و همچنین بخشی از دریای عمان اجتناب کنند.
🔴
این هشدار برای «تمام سطوح ارتفاعی و پروازی» اعمال می‌شود و تا ۲۹ جولای معتبر خواهد بود، مگر اینکه زودتر مورد بازبینی قرار گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134060" target="_blank">📅 15:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134059">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
فرودگاه بن گوریون : حجم سوخت‌رسان زیاده، دیگه نمیزاریم چیزی فرود بیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/134059" target="_blank">📅 15:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134058">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
واکنش شرکت مخابرات ایران به انتقادات درخصوص گرانی بسته های اینترنت ثابت: قیمت بسته افزایش نداشته است، فقط حجمشان کاهش داشته است :/
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/134058" target="_blank">📅 15:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134057">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJ8XetlnNs96csF08Vqt0qFpWZhXhJIYcQEAokaT041k2xtSbk6AY8KukIxJb9DuQZODg6YSZ7Hq4ax_Tvvz724IF2vqPsxZmibZSzXsLk3njFWJ6o8faCd-b9RLRosdSpz7TmoRc6KWFm7dH-6P7oIjL5zAex_UIO9y9UKGL2vcDNnKuhxB3YYdEPwDv7ZsQEFVfaUl0UdOhW1kvGDjZ7i6xpXZ-Z0JP5tMJBpLtM7BtpGbt7D3F2Ri0BCcb_xhjSbvnqCwVoW10YuH09zg766wvmHj5BOym0Jpffw7gPgiHVI3FaoElUSPdr4TEDJr0I3lY3BzUlNrjUF4XOdbHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه آمریکایی: ترامپ در مورد وضع ۲۰ درصدی عوارض بر تنگه هرمز جدی است و او ماه‌ها به این طرح می‌پرداخته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/134057" target="_blank">📅 15:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134056">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
وزیر خارجه روسیه: حملات کی‌یف به کشتی‌های غیرنظامی در دریای آزوف، تروریسم محض است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134056" target="_blank">📅 15:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134055">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
فایننشال تایمز به نقل از یک فرد آگاه نوشت که مقام‌های کشورهای حاشیه خلیج فارس مظنون هستند ایران یا گروه‌های هم‌پیمان آن از توافق‌های رومینگ میان اپراتورهای تلفن همراه منطقه برای ردیابی نیروهای آمریکایی سوءاستفاده کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/134055" target="_blank">📅 15:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134054">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZ-qSr1Ob_o_Oxu-m-CCl4i0I0BX-t7UyISo3KK2d-M8Y64qmhlpi5euTjk0XsJdHOiQNQD0rNMkmSosA3qmcIsLK5Chw00UIeohn2X2yzJ82qCpqCRj363md25cPLzB83-vSgXt2nZj6AodIQxUfG0PT3pu3x0LtoFbRYkQ3upwCsJQCwQztguNGyd5juSy6Yp0uyZs8-XSBFN7kXDdO1QqdfXyPy4UqmR0cLkgtRCIky3QdLBgr6B8jitpuX0VlzKWTv8460pSsxIMDpk_zUtK1TYYmpLbEwU7XSAW9D5nIraH9oW-K8yjUyyniJEg1OS3AVSbs2G74zA9Sm4imA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش نشریه واشنگتن اگزامینر، در طول 26 روزی که از امضای توافق‌نامه تفاهم بین ایالات متحده و ایران گذشته بود تا زمانی که تحریم‌های آمریکا دوباره اعمال شد، تهران بیش از 6 میلیارد دلار محصول نفتی به خریداران خارجی صادر کرد.
🔴
با این حال، تحریم‌ها قبل از آنکه ایران بتواند ظرفیت ذخیره‌سازی خود را به طور کامل خالی کند، دوباره اعمال شدند. در نتیجه، حدود 30 میلیون بشکه نفت خام قابل ارسال نشدند.
🔴
با در نظر گرفتن صادرات انجام شده و کشتی‌های بازگشته، حدود 60 میلیون بشکه ظرفیت ذخیره‌سازی همچنان در داخل محدوده تحریم‌ها موجود است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134054" target="_blank">📅 14:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134053">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d196b16ee9.mp4?token=UbHV7fKS1Pk3KjAluEyyz8cEakZv7UVKoPzeGRhXHUkl_8gRuZ32ruW1c4Y33QA4a8HOiGFe9xTfl7fbab42dfvSyuPk26Sh36clsUAMZUS_tjnDLUfFn_R8_LH98LHiVFhTi9NchkilfwPFXIRGO72g0R6hDxlom0gVhlf3tEXA-FwClp8NnzgUG4CwWqtdBTbOPR3I40Bt3e6SbhZnDMzIM5NbTLI_jgbifwe-xGWBhGV7ad80rA75T_Jmhvq2MVr4CwVA30Uk7aa-zjqeOfWvE80QxQM_umB1V5QiJ78ni3FMTT0MmUZEnLq4Rbqfmzm3UN_kUhr15URluQjFEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d196b16ee9.mp4?token=UbHV7fKS1Pk3KjAluEyyz8cEakZv7UVKoPzeGRhXHUkl_8gRuZ32ruW1c4Y33QA4a8HOiGFe9xTfl7fbab42dfvSyuPk26Sh36clsUAMZUS_tjnDLUfFn_R8_LH98LHiVFhTi9NchkilfwPFXIRGO72g0R6hDxlom0gVhlf3tEXA-FwClp8NnzgUG4CwWqtdBTbOPR3I40Bt3e6SbhZnDMzIM5NbTLI_jgbifwe-xGWBhGV7ad80rA75T_Jmhvq2MVr4CwVA30Uk7aa-zjqeOfWvE80QxQM_umB1V5QiJ78ni3FMTT0MmUZEnLq4Rbqfmzm3UN_kUhr15URluQjFEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار صداوسیما از جنوب کشور :با بسته‌ماندن تنگۀ هرمز کشتی‌ها همچنان در خلیج فارس لنگر انداخته‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134053" target="_blank">📅 14:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134052">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
استانداری هرمزگان: در حملات جدید آمریکا به برخی نقاط استان هیچ مصدوم غیرنظامی یا خسارت به زیر ساخت‌های مسکونی و تجاری گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134052" target="_blank">📅 14:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134051">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
پهپادهای اوکراینی شب گذشته به ۱۱ شناور در دریای آزوف حمله کردند، که شامل پنج تانکر، پنج کشتی باری و یک یدک‌کش بود. این حمله، نهمین روز متوالی از یک عملیات گسترده برای هدف قرار دادن کشتی‌های روسی است.
🔴
نیروهای سامانه‌های بدون سرنشین اوکراین اعلام کردند که بین ۶ جولای و ۱۴ جولای، به ۱۱۶ شناور روسی حمله کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134051" target="_blank">📅 14:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134050">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVWsoM2mosONBaeTROk5ZVlbRGuM9HOWMX4jHDftKhP7igjZu5cgM_y0SRpXUr86qxWCYoX-dcwjdBuJbONaST5zew3AN95sOezy_Bsc5nj6DXmmseiEimit5eaGOWShfgSLbv0r4GwmeqTtmLypxE2RCP4_9ZVvgfP02k67-3ATZ1s3IjzfzJI4tQyxVXLtoD5C7j3N8AGUx1DXJiaLbwCZRrODUkl_UZq5K3D7CDiFaaEYnJ_TVUNi4aBcfpjhgRyijg2e1Cmrq6CMKSrjdetdOngjqzwIecyjfaxGhl_28R2PpI8ScTwaYNgH_ZjOxHSbT-jrZDXRpEVrEu-wAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهباز شریف، نخست‌وزیر پاکستان:
پاکستان به شدت حملات آشکار انجام شده علیه کشور برادر، عربستان سعودی، را در شب گذشته محکوم می‌کند.
🔴
این اقدامات ناپسند، نقض حاکمیت و تمامیت ارضی عربستان سعودی محسوب می‌شوند و می‌توانند به تضعیف بیشتر صلح و ثبات منطقه‌ای منجر شوند.
🔴
پاکستان بار دیگر از حمایت قاطع خود از امنیت این کشور حمایت می‌کند و در این زمان حساس، همبستگی کامل خود را با کشور برادر، عربستان سعودی، اعلام می‌دارد.
🔴
از سوی خود، پاکستان به حمایت از تمامی تلاش‌های صادقانه که با هدف ترویج صلح، ثبات، امنیت و درک متقابل در سراسر منطقه انجام می‌شوند، ادامه خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134050" target="_blank">📅 14:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134049">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
فرانسه: هیچ قصدی برای ورود به درگیری‌ نظامی در خاورمیانه نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134049" target="_blank">📅 14:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134048">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌
👈
فارس: انتخابات ریاست کمیسیون امنیت ملی مجدد برگزار می‌شود
🔴
یکی از اعضای کمیسیون امنیت ملی مجلس: انتخابات هیئت‌رئیسه کمیسیون امنیت ملی، در هاله‌ای از ابهام قرار دارد. قرار شد امروز عصر انتخابات در سطح ریاست، مجدد برگزار شود.
🔴
علاءالدین بروجردی و ابراهیم عزیزی ۲ کاندیدای جایگاه ریاست در مجلس هستند که طبق اعلام اولیه نتیجه انتخابات، ابراهیم عزیزی به‌عنوان رئیس معرفی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134048" target="_blank">📅 14:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134047">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
مذاکرات بین اسرائیل و لبنان در رم آغاز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134047" target="_blank">📅 14:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134046">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
استان خوزستان: منطقه ای در شهر آبادان مورد اصابت موشک‌هایی قرار گرفت که توسط نیروهای آمریکایی شلیک شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134046" target="_blank">📅 14:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134045">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGlAXB-4dbd5Kjru09U57Lo3j5iDryD2R7f1nNRRntGZTgKQiQDasPnQlKpplmH99i-AdDwmcHWKNUtRrkbjYspdjHTFCWBjls1XQN45bW9bL_mTbOD28DMrlQiuN_Hm4D_M0BaqlQODqbM_H5ij8SeuS0wXHZKuLylzsuk0swCpSSj88ZZffX8jz2qUkMNRBlip9PrNgXnExA3Im76gpqtUp8Xak0JCc1IFxZYH9qAFSJ7YOO4_E9X-ksKEx4QFw6iJ6fDfe-wspYslSj1ieDAcYnQT02Yoe1wwkyiJENM6G4VqawWZasNd1d_yOSChUu3nedGlWXTZT_QaNJwNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لحظاتی پیش، آتش توپخانه‌ای ارتش اسرائیل مناطق حومه شهر قنطره در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134045" target="_blank">📅 14:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134044">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
روزنامه اطلاعات: کالابرگ دیگر گره‌گشا نیست؛ تدبیر دیگری باید کرد
🔴
ارزش یارانه یک میلیونی تا آخر امسال به ۳۰۰ هزار تومان می رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/134044" target="_blank">📅 14:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134043">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ce5ac263.mp4?token=lyAfjbRYaYDItq_jiLmA_YvsKGJX5oVevIZPT2cMbikDVO0Pt_WTEJuQ36_VbULwHcItPDkBzzWPkKYn_BglaNBQLXnz1I4K0Puo1tBe2Fr9Ne60bvUYXptDu8ZE5104dRo3HdpUD49Oj5Il2NDSWAD5YCZyC2zJEyB2wAq0AkgdIYK6HspJCDA1gPPGs92lPK8fvuLSZaP6VweoGz9Pv35FdoGaST10myBMxFasGN_JSXE6__KIiq-Q0pM_UlcfiKfih5lleTpmKge_APqQa8ZLtcwfa1yRBwgIZaSoxhHeoH1htKvvB62pRtKDw60HgvTpo1_CGJRt9K5vPznckw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ce5ac263.mp4?token=lyAfjbRYaYDItq_jiLmA_YvsKGJX5oVevIZPT2cMbikDVO0Pt_WTEJuQ36_VbULwHcItPDkBzzWPkKYn_BglaNBQLXnz1I4K0Puo1tBe2Fr9Ne60bvUYXptDu8ZE5104dRo3HdpUD49Oj5Il2NDSWAD5YCZyC2zJEyB2wAq0AkgdIYK6HspJCDA1gPPGs92lPK8fvuLSZaP6VweoGz9Pv35FdoGaST10myBMxFasGN_JSXE6__KIiq-Q0pM_UlcfiKfih5lleTpmKge_APqQa8ZLtcwfa1yRBwgIZaSoxhHeoH1htKvvB62pRtKDw60HgvTpo1_CGJRt9K5vPznckw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پایگاه هوایی شاهزاده حسن، اردن؛ تصاویر ماهواره‌ای خسارت‌های وارد شده را ثبت کرده‌اند
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/134043" target="_blank">📅 14:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134042">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCTpwYBKFzEEtgaLgkhb--hCu3Pu8vgZQNh7PpvJF269b8d-3ZNNNZ_ebkj5iuD230oA6oLkoUQEtYG4WqEDrh5BOQCPs3ecFTqWPjLzYLuP-ap7PZvIGQuFlqGpW3gr3zQ4ad29JE1ZDm6QnNtPEsKHbliZ9vyCcOxHXopyhrB5H1qzC0kY_s2GSbQ_o21BdRnqzTNK8qy5U8G7vEFx8EdcN60-b9uFKNxdPvB2m2zEah3ojvbQkcivh8Cr2ktJUrOuNTImB1OfWUnFM_x4_timzqA1-fmDjHOJt1Vgd4a7Za34b4w9wSz-vuYwlqNgl2KbZ1hM-S9n210bB3h0qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پوستر جدیدی تو تهران نصب شده :
خون در برار خون
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/134042" target="_blank">📅 14:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134041">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cw8HA2zeIFP9vGcindOQ1kHNHlA0Te9HrVhTzIvb-f2-nU4pUHdI6F6sX1tkfW21m_oDAz3ap5h4_gG-26tBkjiQj-eVJDkHsS02twiRAbGWN_3-yw1tNcfWaltp10CfJYRaIOaG8ABNl4Xg5G8cs1B6kNvWy1N3oIwWIe2GL_pQ0109WLnJ7wxXNcJrWGR3R024iGG1bCreUxXfTBDUL9GriVXntLN1w-OdBQMiOgnrruZLjM3soq2IaqQ4Z2ESGYTLgc6ibuIVRGIUwMGsuHQX-HCRTz4YH9KdfeXh1-LT2AT8h3TuklF8YRg09UktggwmEtjZun_FWTpJoBSqTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۸۷.۲۳ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134041" target="_blank">📅 14:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134040">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
یک منبع ارشد در تهران به سی‌ان‌ان گفت اگر دونالد ترامپ تهدید اخیر خود مبنی بر حمله به کوه کلنگ (Pickaxe Mountain) را عملی کند، ایران «پاسخی ویرانگر» خواهد داد
🔴
این منبع افزود: «اگر ترامپ به تهدیدهایش عمل کند، ما پاسخی ویرانگر خواهیم داد و بهای آن را سربازان آمریکایی و شرکای منطقه‌ای او خواهند پرداخت.»
🔴
این منبع همچنین تأکید کرد که ادعاهای آمریکا درباره انجام فعالیت‌های هسته‌ای در کوه کلنگ نادرست است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/134040" target="_blank">📅 14:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134039">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
خبرگزاری دانشجو (SNN): یک حمله هوایی آمریکا به ساختمان سازمان تنظیم مقررات و ارتباطات رادیویی در بندرعباس انجام شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/134039" target="_blank">📅 13:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134038">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIJEFYIDorVzp8yFUCqYHxXBEEHr0A6BtbwPbH7VsLfk4rvq8D_zgxy34zrlKxnkrcWXys4PpTiVlrddwSUsXWrs4W-PC_Ru00ZXrWIUsXULdGetbxbKGRdzpbSxBiP0_Q8An_Mgk39VblrrUV48iEQ8wpLGp2Y-fGc20kLQ4L_Nh9l4nUFY_PUl1ycO-U3s8CxCWbsXru12GbWM1M0Ae_W6ZV2P2hiV1w0F-YuLHMvfMd_aWc6vemRfqWFGR_1-OJfqvejkSg5K9sAfDkd4wAnYA9Y1g1-yHXi4BG-6ABYWnI1AYS6T3LAEyL-IN6a0dm1eadxaBQenyO0sJ4bnxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حالا که کنار گذاشته شدید، توییت بزنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/134038" target="_blank">📅 13:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134037">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/062bc90f38.mp4?token=oJwi_16cqobd1vlIYVoXe9UTBFLWA8jPZFU1OqCgNiY2ejwyQSzbw6fqzIWnv7ooM0ivDB6TXSKP7nIXR_7m-1o5hxEyI42APVT3O32J-BaXQyHa9b_mlQn0cC7sSFbNl8AEiveGbT__PzA5OQQOAhzeT162cZV_TTNVfuooNyMFevroh9BeXwaTKKkHkJUXM2K0qm1suLd_PdL-JbiWspzcLgxfRDzjvo9bsk62Y5Gmwc-bgH-UR5ln0vi6w47m08alsYvS236bvi6IwQrXd66X_Ky6UP0SrXR442flOI4WLgUEdbCaUubLiy286WWEhE5Km-XS3i51EVMJd7WnFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/062bc90f38.mp4?token=oJwi_16cqobd1vlIYVoXe9UTBFLWA8jPZFU1OqCgNiY2ejwyQSzbw6fqzIWnv7ooM0ivDB6TXSKP7nIXR_7m-1o5hxEyI42APVT3O32J-BaXQyHa9b_mlQn0cC7sSFbNl8AEiveGbT__PzA5OQQOAhzeT162cZV_TTNVfuooNyMFevroh9BeXwaTKKkHkJUXM2K0qm1suLd_PdL-JbiWspzcLgxfRDzjvo9bsk62Y5Gmwc-bgH-UR5ln0vi6w47m08alsYvS236bvi6IwQrXd66X_Ky6UP0SrXR442flOI4WLgUEdbCaUubLiy286WWEhE5Km-XS3i51EVMJd7WnFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روح الله زم در سال ۱۳۹۷:
محمود احمدی نژاد هرکاریم بکنه؛ نظام جلوش کوتاه میاد و کاری باهاش نداره.‌ چون سند و مدرک زیادی از مجتبی خامنه ای داره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/134037" target="_blank">📅 13:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134036">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
مهندس ایرانی‌تبار در آمریکا به اتهام صادرات غیرقانونی فناوری محکوم شد
🔴
بر اساس گزارش رویترز، یک مهندس ایرانی‌تبار در آمریکا به اتهام صادرات غیرقانونی فناوری با کاربرد بالقوه در پهپادهای نظامی به یک شرکت ایرانی که یکی از مشتریان آن سپاه عنوان شده است، مجرم شناخته شد.
🔴
دادستان‌های آمریکا مدعی شدند مهدی صادقی به همراه یک تاجر ایرانی، در ساخت سامانه ناوبری مورد استفاده در پهپادهای نظامی ایران نقش داشته‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/134036" target="_blank">📅 13:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134035">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
دلار هم اکنون 184,000
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/134035" target="_blank">📅 13:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134034">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ درباره لیندزی گراهام:
پزشکان گفته‌اند که یک بخش خاص از بدن او به معنای واقعی کلمه منفجر شد، این وضعیتی است که پدرش هم داشت. در پاسخ به تئوری توطئه، دوست دارم بگویم بله، اما فکر می‌کنم او مشکلاتی داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/134034" target="_blank">📅 13:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134033">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-Gymfl6Kcz6peISrQCy20MF3sh3rCrpctOCVhK2L0FY5HBXupzRszJr40OUggnbMkZVGEzUvdsGyTNmjC1xRoaMBvf61HcIUux5IT2Kq-G_YHTUto9iU3N7-jGgLFnf3XNcM1BIpzwPet4yMuA2jDHB-KcaZtqeraDG-QThFkhQdM_JvWidksCYvwr7BvJnhiOhsWcZnNJvxS_CQktzf6FLEwEEartsRN6FQee3gzEKr1MUiePSuHAxRo8V7JPaMZ1cNHfr8seFVhD6R6Cd6h0h2W4BGwGwVs8hKguxcVl-x6mf7dNSfhyT4ZGuvMjuGmmGCyJghVzSh8ZiikhZJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منتست به بندر عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/134033" target="_blank">📅 13:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134032">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: ارتش آمریکا تخلیه هواپیماهای سوخت‌رسانی آمریکایی از فرودگاه بن گوریون را متوقف کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/134032" target="_blank">📅 12:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134031">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
دقایقی پیش؛ صدای ۵ انفجار در غرب بندرعباس شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/134031" target="_blank">📅 12:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134030">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
دقایقی پیش؛ صدای ۵ انفجار در غرب بندرعباس شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/134030" target="_blank">📅 12:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134029">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZCFc_Og6v91tbwKWFvqNiJzZB8SIdypPRbIK-Sak4E703B9fU0cvNUaXKfNArhGzdScS1udb9Tl_VflwmgeHn4_20VEUQ7sRvv6lv287zRh7LVSh0P1bLud_8_VMhs4UWxVBFNE2Np8H9WOtzCdVaR-toqQ245_FbOAVJDtpbmy0oH6gXqQkyvybe97SD97WbfuxC3V0RtEYaXYQz3pk9i_Dpzl6mv-hQP3a6HEBo3Zo0ah02AJBZzUwlBCs7CrFvI_IOm2VDR4z8FW6Zafq4NDvY0N1fUOpHMTreyoW1BEK1yOyGZ64Hp3gem1sv1pejVgmY2dazyQROtP4dVVdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وایچرت: بن‌سلمان خود را برای جنگ زمینی آمریکا با ایران آماده می‌کند
🔴
برندون وایچرت، نویسنده و تحلیلگر آمریکایی:  دلیل حمله سعودی‌ها به حوثی‌ها این است که محمد بن سلمان به وضوح می‌داند که ترامپ به زودی قصد دارد حمله زمینی آمریکا به ایران را آغاز کند.
🔴
در آن زمان، حوثی‌ها به هر حال به سمت سعودی‌ها حمله خواهند کرد.
🔴
بنابراین، محمد بن سلمان در تلاش است تا پیش از آنکه آمریکایی‌ها نقشه دیوانه‌وار خود را آغاز کنند، به طور پیشگیرانه شرایط را به نفع خود تغییر دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/134029" target="_blank">📅 12:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134028">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uav2bDWu1hAAjUSwKeuv6SF6k7laSaa19fjEj6ru6hWn7VMIn13FjEDuvVu8rnZyQf4CRyG_Zs3Q7U_vbwowoIggvi2Aq8HEurtwbvuzjHxMBW0Hu7f2WQMmLPTPVLVyiyQMrMNvGOOB0JF11dSLe3AtrG4In5AlCfRIccOnMokmB_bkFA2bGEd8ZSPjgUzgpV3p7Qz70jVo0Y5bG831Xz9lkpR289qUtXyFtt314nLjsg-KHbd_BN3ksJfvVRCNM7rDzNWVr6dIv57OxuGSAu2NTvTvBJuogqxVE2LS7GmIKoeuKcoix-FB7TxiO8fkM2psO-uoHy5zWIEgYY5YbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محدودیت کامل سرویس های گوگل و گیت هاب در روسیه اعمال شد
🔴
هم‌چنین سایت اپل نیز از دسترس خارج شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/134028" target="_blank">📅 12:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134027">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3LnQY5-l6IZqFKo2jQIiUdSYY7GJ6sTXwnr6t1csECmsmsIp_pp1_nAiVS2kMBkIUoSM7-a_sx2mhPONza2vuxOaB1_jmIcQTWRfSvDEce_u380p8iRDhl9Bvb9s63SRGZIWs6IWxtFpLY17VgBd3VL4alQVpVrqNxcucZ3vJICUPE_6NHxn5ITU85eRRozXlDm_HuIVu5ywbNJFhAY-lLdAuLOPqtq7_hZZOuNdfAJZ0UEyg0zL79Iy1ZCIfc_wnBQpyhKBrQ_AVI55zaGeqqruz2APj1SoVuk522XSgq7bv4yrY6eE2k59ROH6tbYy3zqVmDQy5MeWbqivHcdYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ندا خدایاری ، خبرنگار حوادث : انتقام از نامزد سابق، به مرگ دختر همسایه ختم شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/134027" target="_blank">📅 12:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134026">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
روزنامه «واشينگتن پست»: 19 ناو جنگی آمریکا در خاورمیانه مستقر هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/134026" target="_blank">📅 12:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134025">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
مترو و اتوبوس‌های بی‌آرتی به مدت ۲ ماه دیگر رایگان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134025" target="_blank">📅 12:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134024">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزیر امور خارجه عمان: در حال حاضر، مذاکرات پیچیده‌ای در جریان است تا یک توافق بلندمدت حاصل شود که از آزادی تردد در تنگه هرمز اطمینان حاصل کند.
🔴
ما مسئولیت داریم که با ايران و جامعه بین‌المللی همکاری کنیم تا به توافقی دست یابیم که آزادی تردد در تنگه هرمز را تضمین کند.
🔴
خطرناک‌ترین تهدیدات برای امنیت خلیج فارس، نه از داخل آن، بلکه از تصمیمات و اقدامات موجود در خارج از آن، به ویژه در تل‌آویو، سرچشمه می‌گیرند.
🔴
باید روابط با آمریکا را بازنگری کرد تا با واقعیت‌های استراتژیکی که جنگ آشکار کرده، همخوانی بیشتری داشته باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/134024" target="_blank">📅 12:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134023">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فوری/کان نیوز: ارتش آمریکا هواپیما های سوخت رسان خود را مجدداً در فرودگاه بین المللی تل‌آویو مستقر کرده و برنامه ریزی برای بازگشت سوخت رسان ها به اروپا را نیز لغو کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/134023" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134022">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
قیمت دلار آزاد به ۱۸۲ هزار تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/134022" target="_blank">📅 12:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134021">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2041b839.mp4?token=EKTscX0y6tBtoqaM4WZocmrS9ndN1CnrfKiiTC7xmVX5AGINNJlG25Avsq1AW0RB8d0wV2zXRDq0BSpaysbQTc3UwkAeAbP0LbeYjYYlpUKyI8rTh24ajEJBlRHYvlGU_KIMBr5tnHNjoWvdEcM05zCBx5YwEM_y0L1d-AMwcvE03MI1d7-8Oak7IVvxNLzkz2D9BZ1iO7djpafB5CiGxG4e2VrUjcEOBwgLtILT9hrOrP_vXFhlTfmxYi3tDjD9Rdg0-sVkapg-C2GspDNCzFBvRc2EIgAMoPqf-h2hEJXH8aNEF3t1bmNmceB_gZEmXljx9SqtwnLgcRP20VPdOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2041b839.mp4?token=EKTscX0y6tBtoqaM4WZocmrS9ndN1CnrfKiiTC7xmVX5AGINNJlG25Avsq1AW0RB8d0wV2zXRDq0BSpaysbQTc3UwkAeAbP0LbeYjYYlpUKyI8rTh24ajEJBlRHYvlGU_KIMBr5tnHNjoWvdEcM05zCBx5YwEM_y0L1d-AMwcvE03MI1d7-8Oak7IVvxNLzkz2D9BZ1iO7djpafB5CiGxG4e2VrUjcEOBwgLtILT9hrOrP_vXFhlTfmxYi3tDjD9Rdg0-sVkapg-C2GspDNCzFBvRc2EIgAMoPqf-h2hEJXH8aNEF3t1bmNmceB_gZEmXljx9SqtwnLgcRP20VPdOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادعای ارتش اسرائیل: در حملات جداگانه‌ای در نوار غزه، یک فرمانده حماس و سه عضو دیگر این گروه را کشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/134021" target="_blank">📅 12:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134020">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
داریوش فرضیایی» مجری و برنامه‌ساز شناخته‌شده تلویزیون که سال‌ها با نام «عمو پورنگ» در میان مخاطبان شناخته می‌شود، در غم از دست دادن مادر خود عزادار شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/134020" target="_blank">📅 12:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134019">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffac33808d.mp4?token=LJwz1-OliN2WFuxL6iMyJ53gxqFQT1mcV1IdA7ceELXgX3IfpbCYgm19b_ER2dIL31TuD94pr0miMLjxB13aRIvRIuVAsnoQg_olX_vyhZypejXk6nUxMcCx4644qEm_PNGvVrmOzLhVajG3ZKRzL1vnuKVwxZNvJhLUUN2keBSoarLYouvEE_hmtt8zq2sQjmpC7Si2R2bMNg5l_-sz3vlhQpCrs9Wp9D5fSrDKaVVh2w5tf089x22oveLKPfJXQZYUzEp_nnFFg0ZJjR7n1zoY8hClqdvyuI8KhUUj4aDtZsVyXeGfNGwIFJEXABuVRVPH8_1dJ7ROzI-zcxkGo7nITue_IELjdJO_SadK12vS58g2rgu-XadW6wAK3bHgQ_gpzWNimO0SOxPlXt0V10X1lzZ8DT8JGrP4Ey0Ek4L6NQBbgM4j73e9iGZDNh4IyjESy0hVxOHB_NqORgPF2PPGbEWZv16s2GuLLHwUt2vf-HQ1KXYOsgaJyTpxYlhOgq22eQFuZZMw8JuHM8yDXoGpb8jNuBz_pxO1vbnTaAJ2a1a7_wmk73LjI3SrmLkg7Y2irsZzegB-w20Ce3kKA83abAtHDrMOdZoRq8lHtXzpzDI6A1AJfoZIDe53YRPbIovaGpXC0YGdNZdMoF3lVS2GalGYtKYqEljSn7LbwFI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffac33808d.mp4?token=LJwz1-OliN2WFuxL6iMyJ53gxqFQT1mcV1IdA7ceELXgX3IfpbCYgm19b_ER2dIL31TuD94pr0miMLjxB13aRIvRIuVAsnoQg_olX_vyhZypejXk6nUxMcCx4644qEm_PNGvVrmOzLhVajG3ZKRzL1vnuKVwxZNvJhLUUN2keBSoarLYouvEE_hmtt8zq2sQjmpC7Si2R2bMNg5l_-sz3vlhQpCrs9Wp9D5fSrDKaVVh2w5tf089x22oveLKPfJXQZYUzEp_nnFFg0ZJjR7n1zoY8hClqdvyuI8KhUUj4aDtZsVyXeGfNGwIFJEXABuVRVPH8_1dJ7ROzI-zcxkGo7nITue_IELjdJO_SadK12vS58g2rgu-XadW6wAK3bHgQ_gpzWNimO0SOxPlXt0V10X1lzZ8DT8JGrP4Ey0Ek4L6NQBbgM4j73e9iGZDNh4IyjESy0hVxOHB_NqORgPF2PPGbEWZv16s2GuLLHwUt2vf-HQ1KXYOsgaJyTpxYlhOgq22eQFuZZMw8JuHM8yDXoGpb8jNuBz_pxO1vbnTaAJ2a1a7_wmk73LjI3SrmLkg7Y2irsZzegB-w20Ce3kKA83abAtHDrMOdZoRq8lHtXzpzDI6A1AJfoZIDe53YRPbIovaGpXC0YGdNZdMoF3lVS2GalGYtKYqEljSn7LbwFI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئو از شلیک موشک‌های سپاه به پایگاه‌های آمریکا تو منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/134019" target="_blank">📅 12:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134018">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOcFokPpePM6I83A_bbAbWCnELCKZxFDtnGuWZsbII_HrHm70Y6m0izJrXSfnn_4FvuUrsH5_2wniM4Zy2hlK-Pk6seNZ1bMWYhosZBZzO4hTUgCjMTuWSOAbfEOxDCjsviEuz1KnpnQ8900CuPZ5dk5W2qfDYsgPvVgZgBnuV9enF_tgKO2xv9jYJkMn1JbFvZyfAF8aNPXm4bxfHfEQt3AtFK3tXcEA-O9yszA2ieloTF2N--9u8e9XafeTrZSy_qXvUMb5_w-szlGK7Af6FkfeXYWznVJvwen7TtG442XLBFHjvTzzKQNqQVP1tb6pzHJF9ptLP6ZcuUzQZm0uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۸۶.۵۷ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/134018" target="_blank">📅 11:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134017">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ایندیپندنت کیف: وزارت دفاع امارات مدعی شد که موشک‌های کروز ایران که به دو نفتکش اماراتی در تنگه هرمز حمله کردند منجر به کشته شدن یک خدمه و زخمی شدن هشت نفر، از جمله دو اوکراینی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/134017" target="_blank">📅 11:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134016">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVnWdL1TO6EV59yZVg1oNUfVFy99CU4rMN9zT3RjErc-i0dlzDiVDSEoFF2fZnjD1ij3HskSwOmCBc8Od46zjz0OVUiTxoJaJyDPXHhR1O3h7hT6I2c74qKemDk15Bz0LkHSyktZ1KWCJEd4fM0ckQ7h9yn4Kw84KLnYMLKGsXL4qdcDRUBT1zcQNbYyS6C_AcM1ipqoUxGBd24V25u8C9RgW_XJ8_Xa0gsx86YrapduYtPnouZAjI4vemQgnmMBl-6Ciw-7EoYjZGkd-RF5tXDog-iBkinQ3BF-BV2vNwoTw1YmpONvsHFgq8rkiAaKDefGAFBQoYUhuPptyV3zhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سیستم ردیابی هشدار قرمز لبنان نشان می‌دهد که فعالیت گسترده پهپادهای اسرائیلی بر فراز مناطق جنوبی حومه بیروت (دهیه) وجود دارد. هشدارهای متعددی در مناطق غوبری، برج البراجنه و برج حمود متمرکز شده‌اند، و همچنین فعالیت‌هایی در نزدیکی شهر زحله در دره بقاع گزارش شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134016" target="_blank">📅 11:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134015">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
نبویان و ابراهیم رضایی از هیئت رئیسه کمیسیون امنیت ملی مجلس کنار گذاشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/134015" target="_blank">📅 11:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134014">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
یک دادگاه عراقی، ۱۸ نفر را به دلیل تبلیغ حزب بعث ممنوع، در شبکه‌های اجتماعی، به سه سال حبس محکوم کرد. این حکم بر اساس ماده ۱۰ قانون شماره ۳۲ سال ۲۰۱۶ صادر شده است که فعالیت این حزب و سایر گروه‌های افراطی را ممنوع می‌داند. این خبر توسط رسانه‌های دولتی اعلام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/134014" target="_blank">📅 11:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134013">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec0db543ef.mp4?token=tM3ZjbArqr-BLKf5Rhk_SEu6S58GwKkBJBaaHoxDKTgzwuHaWKQXC5mZKoJO7TF0DkXs15yyTlD_1pUZo8B9teItaa9TuKbwe9uT1qPWt3PnFh4ccsEECrG7vxV_YgJsQ7qKKZEnol9afKkkDoj9W-o3HuT7FvEiczjFS4HAFFfAXadsNl_26XwWWYtViCZFGldb-5iU41hGmgOU1KQeV_fXfCkEyiQWfrBfpVURk-RvzjE46gqy-JRJpwo9cgTh3DKPI3dQdBEkAzwwynUJcf5rgKdnWPYWwz815Q9t8Wtw-kKbvxAqXGX_8A417X_CSWypFIBPxFuRwfO5VBvhGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec0db543ef.mp4?token=tM3ZjbArqr-BLKf5Rhk_SEu6S58GwKkBJBaaHoxDKTgzwuHaWKQXC5mZKoJO7TF0DkXs15yyTlD_1pUZo8B9teItaa9TuKbwe9uT1qPWt3PnFh4ccsEECrG7vxV_YgJsQ7qKKZEnol9afKkkDoj9W-o3HuT7FvEiczjFS4HAFFfAXadsNl_26XwWWYtViCZFGldb-5iU41hGmgOU1KQeV_fXfCkEyiQWfrBfpVURk-RvzjE46gqy-JRJpwo9cgTh3DKPI3dQdBEkAzwwynUJcf5rgKdnWPYWwz815Q9t8Wtw-kKbvxAqXGX_8A417X_CSWypFIBPxFuRwfO5VBvhGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آتش‌سوزی گسترده در محوطه نگهداری کانتینرهای بندر بیروت رخ داد و ستون‌های عظیمی از دود سیاه را به آسمان پایتخت فرستاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/134013" target="_blank">📅 11:32 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
