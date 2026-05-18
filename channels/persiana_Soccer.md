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
<img src="https://cdn4.telesco.pe/file/iS-R2wp-n33KVG72K8R5OcLJ85vQEWTgxoeYi7yLG5WAlNr5_P13xW5Dn6U-LaNhIAGBwSVziBuCdKE4soeQrzOgdDsyNF5PyciallEqPEbLAgaojVp5N2QbH2jqefQYswCJINVyudHx_z9GDfIbd7bID1l6qnhQvGdv5FlTNcG7zP53seKC61EOyEByZovQtTCcJ55drY5zaeTqR0qIYOcxUqCQS0YHIBh5MFgvGuZF37jVD8vUCfTPjR4Ve319JyMAMIbwTA72k9HalFEC9OSBYk0hQWEpoiOVbo3ygtPl17RSHQBZ4Q5htbtFVYhKOvrjeRtmQwQ7yVuHQrJZ6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 207K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 21:57:14</div>
<hr>

<div class="tg-post" id="msg-22175">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ovIAtYftyTF8ccrHqQCCG57x34XLARaDJj9Ed2rvOurCfwpC-wfcpdhI5udAMsMlOclEgB_MI4buwJNiqh1sO9g6XKR_qzHOJm31HPvhHct-t9chS7vdQShdbM_Jwwc-rc2IhMsHs78xV-fhEx6oFa2uvmgEuXDZmySkk8Z0YwFRNBf3IiZ9oSkFIRtAYZBH1RLdOhXo0OA4z_f5l-Maf0Z8WwXrc3f5xmvixAvroHcrDjkymgqVOhwaJ364sQ38OEA-Aa2LGMN11Juz7-tAjx13OLI1foiZTLHQUfhVt9n8bJcFePfGj2YEYrsOYFvtHw84qgwm4qTCK0o0FNYvMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tXgJ2dFO7YWO0OGjkwmrL7hgasvnWWTn1Oifb2Xb7n0IdozLthWkdo10MEWry4paY4uG5dJ_VZbN6nsyqhVATq1wVXtgL5XAj0m1Fl1NRO2RCbVkEKKANv7C8uU-gnfJWiME2PehJru3nOdd1IMAs4pRn_rZNgh6UCSxFcMRl3J-qvN0N6tS7f84GUXJZDaDsgqGiXGmBVnimjWKmvqqO2FwAx0spq6BHZyx5N9AxegmTyxhFTcQofeFKcruHPR55K8wVEiZidElBxErPfdYukeUEwzyx-WUhKNGc4TUzk0Swk9QPMgDKWkxPOGk8wTR0Q7YrBZjEIsd8dFEkkWTcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مهدی قایدی ستاره 27 ساله ایرانی سابق باشگاه استقلال در کنار پسرش میلان قایدی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlO2khZZOc-l2iN0Fw-AZOI0aO8Oe2DGzolcDsjnYXpdFXoUffAbKIaWIMhuTUAvsaPPuLAnjH-znG5nAVp54RgmYhZuknizGLBJ3xeKTxP2sjiVbWLrBzE7dtJYehyfsi3EmTPIh18oVbpso6Rw2kriinNM4MUpqX02YqnlD3nmo4zmjvJ_MoXLXyOPgvyS6iMfMrcThbO71qsM337aLR0-F_-fK5p99BlLoEKcPFWoVprqIBj59oOm7zPBkIW7JBA811kNM7H9a-hLyEEl723rTAVkucrU4oDDFPUfJkT9oeGLNRB2oyUnDqLx2UjlBL8ursJZhEsY1c-Hh0rqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJjtUfafxtWqO_zERdgESZKNKv28nx8pxdnML--EgH7pyy9Ml7brxsIye_3vFD1AOVOwCXgladLYoOXncX5wj4wSAsKkQzYJyvMIv3ByAjfBCrvrzPXIuFZT9QUXCHC3d3dGLYok1uSJaRwte7FFmXy3q1GWDPkjRW587G8rgkqIkMDAs-kuVCJ_lgoiCHJFSqgkrtMGIs_T7YuTcimZezOndeLI7d5rBzu7n33X2ri9gQ1YUVqxGqBYu377XnxitXCGCxa14iSPgiSIUhPmQtdG4opFILxpfYB8vYc00Mz0Vks0Na1lueHuui9DYkkpTEajTApEBOZTCihDUvDpHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22172">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚀
فروش کانفیگ های اختصاصی همراه با ساب
⚡
سرعت بالا، بدون ضریب، بدون قطعی
✅
مناسب تمامی فعالیت‌ها(ترید، گیم، وب گردی و..)
💡
پشتیبانی ۲۴ ساعته تا پایان حجم
😉
تضمین بازگشت وجه در صورت نارضایتی!
❗️
تست با هزینه کم
❗️
برای خرید به ایدی زیر پیام بدید:
@Itts_Benii
کانالمون هم برای اتصال رایگان حتما جوین بشید (روزانه ایپی جدید برای شیر و خورشید میزاریم) :
@BllackStar1</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/persiana_Soccer/22172" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7dLWrHg3zcsCQRVGlBaIRQlDEUZhlIXTZm22mwbknvXQ5XFLrubQzwIEbYCXf9F-7l5bfcrUqVPJCHuI3BPeDdzDUMnkkDoDlgKsGvkGbe3KO7RU4DSP7D5mNvBdZVlJ1SDFk0cCrFxBWFtI6oMFyx5lsuDoyikFdG--o5JJ7gUc06Vri4CpfqlbTx87llEls3FzfO6RbHDW_1T16GJmTDAgmvz4vbQgffuIMe7Vy91mDRJwjVARb1IHDaY3BRPWETtPKvtejVa4hV9c5b21xS0td7u2seTQBxEPxpLVCbd1_DWhA5JFQP3sVJV4lU1EoMxFuAY20k6JXh4Da4ZdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841076b140.mp4?token=LaRG8Ru0GTbhcaYbZuOiDrWBAeTjOBf9Km41L3ZG-oZyBUqeou8sU9I-phrgOzBep4tR4oNPRarwLJgSQZYWxb9uQg22zN3Jn8G_pNkYu_y0QStkP3BL_v-QWVI48TybmMlePoJuUbnXVjVOPSwZ2O1YdHyPSOs4w3axqoX--4XM7b9E1exN-cslcsbqKxp9ZSXNJBuKzKYvfFabawor8I8oeZ_MlLtzrJsXxzlAY6SPkduQyve-hZzzM1K4Ik9b4A1_qyfxXy8O56LDmjrLHHw-DoSz4-k-LpvLD7effeY5Q0ozHVYBzeGe0KBaxBZrjlu_cSzYujMagnUlUeWWsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841076b140.mp4?token=LaRG8Ru0GTbhcaYbZuOiDrWBAeTjOBf9Km41L3ZG-oZyBUqeou8sU9I-phrgOzBep4tR4oNPRarwLJgSQZYWxb9uQg22zN3Jn8G_pNkYu_y0QStkP3BL_v-QWVI48TybmMlePoJuUbnXVjVOPSwZ2O1YdHyPSOs4w3axqoX--4XM7b9E1exN-cslcsbqKxp9ZSXNJBuKzKYvfFabawor8I8oeZ_MlLtzrJsXxzlAY6SPkduQyve-hZzzM1K4Ik9b4A1_qyfxXy8O56LDmjrLHHw-DoSz4-k-LpvLD7effeY5Q0ozHVYBzeGe0KBaxBZrjlu_cSzYujMagnUlUeWWsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تقویم
؛ 13سال‌قبل‌درچنین‌روزی
؛ دیوید بکام آخرین بازی دوران حرفه‌ای خود را با پیراهن پاری‌سن‌ژرمن انجام داد و از مستطیل سبز خداحافظی کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=ka6yU7aDI0SgnwDkEMAz2_AU_ovHKAnXkEeVvpWwEX_nMivdrB0CUNRiVTMz2-sl9-yZGQNP1ieBzzwa2rJ51npVtwqzQQFfDabF9HZlzqvUDUkKnzFZupGNOlxUIA4bLfPO0kLf7vT00212Jqr4omfVpmKla7GNmrtRwmamt4F2UbGcsiHqIHAKEsYgSqzu9mRh0O4ejQhOBcSKS2vhDnjpSGeTKeFvrgT-WYQDfhl3csZIgmM3dKnWgWQnuL3ID5CvGjNewIKDkwb_kojGnH45OykTVNSaW5-z6t23I60ggY3gotOuzxaWwI1OYzkjIvsgKb6dBtkxHBxIchvkEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=ka6yU7aDI0SgnwDkEMAz2_AU_ovHKAnXkEeVvpWwEX_nMivdrB0CUNRiVTMz2-sl9-yZGQNP1ieBzzwa2rJ51npVtwqzQQFfDabF9HZlzqvUDUkKnzFZupGNOlxUIA4bLfPO0kLf7vT00212Jqr4omfVpmKla7GNmrtRwmamt4F2UbGcsiHqIHAKEsYgSqzu9mRh0O4ejQhOBcSKS2vhDnjpSGeTKeFvrgT-WYQDfhl3csZIgmM3dKnWgWQnuL3ID5CvGjNewIKDkwb_kojGnH45OykTVNSaW5-z6t23I60ggY3gotOuzxaWwI1OYzkjIvsgKb6dBtkxHBxIchvkEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
لئو مسی آرژانتینی در صدر بازیکنان با بیشترین تعداد بازی درادوار رقابت‌های جام جهانی در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5cRdVuBCUAeEipfdJHH8X5_prW65t1BaeYNsNs4XrERQMY34DD8Z0ehbC5Dn91O5WNqn4edlrF8w0dVmnT6aCmgAR0i7wgKKAa2KuwzghH4JakY7fUVv-i_BQ-D5IsueZ95W9U3nb7vhCn22Fvky8yGT16VrlloSVpPm_-IM4nW6-NN4jhWihaLmiHMKQdY_bYt_lf9ddx3r3DSfWWEbpEA-iXJiH7LZoPaa8ZDTNg5HGZKKNaxRQMe0Agx66DvMfxi2xAbXBMySuoTY8r4OZUiJksLwrymaVGTTpRbj-gtsS7xQyFRrSy8J2s25FdLUE9S_C-F4QRtSvAl7sz2pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y900wnun-3-tv5y-Zb2J3PSH5fXG3N-7ItCe0uYTi6fW6wsGJIjrI0dBw411Kortg8qyx9LgDjvOari-FOjrj9kpITafdCWBEGaK9tdFFqMp6YJWfux8Fop_4UNbuhGNN2KBYYFPV83inS6fxqMfrlUOI13Xf41lk3kB5tgfVrsmUkLaG976Murf7Sfu0Gygxv4_UcAM9eJAJgCDgulj3rWO6SCghVt_m8CAHDycYuvgKuqYBGckObd8yIAd2BbEHCQ16dW4fgtdEMtFAHPgmxcGmZsb-c-cZfbfxUHiPPbAtLndg6abJwKT86JoAffba0YiRoqZ2H5eg-jPCivnRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22166">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxV8dymgd6U-aTBwUBvHk25QSuKAy8NaW5W0h6X33xeUudFOGqpYFA1beBHqto4sa9--wuPbu-7lkt9tbIeC3h0d39MdthpXW-oERjpmQt15eubkGinYtdD5jZmvBTM57-aFhJ9H2WxzmaTXBcIeihbLbpJr3NYgrZCXgFf-4lPabcSwozFGR9cLQmyAH5r0JOT_3AbnRJ1KveCm-SEGEPi_WGOBdZkZrjFDN3LBxAGyFtJLq6enQfsm5TE6GxAemB99NzTjNuqdPf3TiujoDOsUSWjJnS-aksIefpBC88iVLCXnnLYqg2eYni0yeMkQZejEOdAE88YN6A7frKBjeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/persiana_Soccer/22166" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHOApNytjJ3TU1eVvYc0g1F_sNDmsGMLpQZUbfOxXyuGeVMSes_ROYs77MUSPQV1T9lZGnAAafLz7IPs2wX69UhNPq-vVtKYgPHIp2KOZ4Bnd22RICkGsVKETFPfPX7_G6oyNq3pJC6DKoydaRYQZ_QUSMmIiuaMY9OPlsEVO6S58FbjpeP4m486XeTTxMB9rbjmzgVVlbOhanw4M3Kt_FeRLLe6xiBSCXu1_-JDoqDF584SSO0qBDndoe1ZoYKU4qiq8hSeVC48yX35vO7qbrdZTHLnfcT51LiDCA1iRUKw6ctjzqhfx-FyraiWrBVlp0wzUaPFv4QK658Naht0tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdDwpnMygaEC1be6ROoVIDZnF0YwALys9ORTHoO2b97txD-HbMzIFqbbkg7UsyJbKHFwSposuykdOrKx3zFp0TejSQgipAbIl_VOx8lGE9dgU5yrYeMnl72qTME5VQtliLF3-jI7ZR4yvVHmUSUFe-g4Neye8fW-9RliAoTEDl167fIZ_xbl-0m2zECFbSRPY06aUN57OrLr2MwYkYUQ9oTuFcUt_m1LKVdXjT6eCBPGT9pq_ISXHn6bJuIg8pjYXwXTYQfTYxCeDpr4lPGjSuASardex_RYgjPEqX-zAMmrzwHi1fHEo6DZ8nAmQ4DhsWJjqAsxCosKrqOl72CEpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h33ZoQoSg0wVH2_Mz7DEPABRTWVFx6vsNf73h5bmqZbSsGIpCzoE_YC6WiUw7YIdyFwss5d_zCjJbsyOwiwg1FYUFx6WDyKYrEcI6sAsAHjq_AAcPY1r2EZ_2DTCAfSEq3lkzDU-bfKz9AKHxkVYFEUwj4LBXSG81JNxjDTQTSuzr3wttjQXvRNKSFJ6UsMhT9DErpQ2WUfeNkGaXMmsP_afR-JZIrxarHn64PTUlfBs5_bSiXq13JlpiGRmZXAoIRd5Uu5V86JYCJOXVbCjODqxxo_qRIBsa5yIkbDjUy5lZLVAW7r14MexEOXiI73kkdFHK_OqPE0i54bUNzZMaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5KCCMqoDYYzt_CFFa9lHMGaRTkG9LrhGV2P-hMuFgou5w6rBRWspi0exXtr0U4PYgQPiB6-zcr0IpjwfM5dTTSsC8wUK8yKU9Lfit5I-3ZFG26FSF6RkvdiHmb-Yy3CO9CxxFLjp9In0gzBRHbCO0KxaZL4I8BpsFY1GaRAi2FoFRDPEf24w1eJVWSstaDfZbRSx-CphltgayfK29eWxcpY8Ih304pnGriLsT75w8OH_EifuZ8y6mE_NqiSVfiVGuLb_2VnWmwTZNznJxSE43y-eIdKee09B0GPoN6Mr9Fc6O2fJjg4fC7q-PpjDC8K3qCapmr5_sSgGxjic52Jew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFK8N4wp8VGERj2ZoZempEFXbLKUrue9ESKN2Gz8ELtT9-Uw6fO3Gg3nE400SJDDfHzwVd6X7mJ-pNNJkoSU5YwPNZXN338WpKCrz26UELUJZdokF26pjEdWCFftmlgeipG88iuYZwvC_JW1cmktZa9nuJW7-kjbSRmnf8cuj2Q5zsSuDN0020AcA8JYus-Nih4225Bbgi_z-jseG9PwHWvJMkT5jFD6StwKCfbHxJogNZ9N1QENNiwoScu9IBXZwDKlzAJj-etw_4u4ll9VCp5sKT1lQAcOjl3XGbrmkw9P_2_14DIJlJOIbrPoLL2rvydQoQB1oiggSqHUIfyoXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6zhYLla02CaW9Z1kLzg7R-Wj-a1SQsaRugygVbixauW1oMjJuNDZbN0WedQC3FHb-u6J0dfyDO12WT2fr_Ml06o5k4zxfOLRjUlhsRlwsWz7f7riuFC7tMFJDcyCjVmLEFcaXzHDerCQXdSPkVVFxPmEXwBjrhR7IvRgyzzyuk9gl9UH5-vcAJ3UeDg20ObHsKUa1YevhjEE0_tfVDQXdWwemq2103uPXqRi70zfUW6pUyUCyRLzWNcuk0sPtEUWnYmKDUcMC9vHvkQT-HQ0hRnefoN-Pt51Ppd7FUQCIkY4DK1HoOLsxpybI7MxFDXZ0Kb8WTAxk8ZONMtTqwCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBkHqhLp2T-6MhyjtLZxHZFZbNBkB8X5UYoLZWXWaPUe0H4VjJ_iOAOSFmJXHRl0zXZ0XSyV36YHhhHyHccbNc3mTancajbP8KFivfuJAHuP1V1ppwUZpY_NpQxav1pbvGhTga7GrGcny2nNCDJeV1TLwIXGNljVwyV2jPYdnlfOz0dIRPYY7x1mT8nCN1NQVvUDvm2qHVF4UxEZk9U2v3NmF4v4BJRQTWrs9ikz7diDN_sU81c56LPL55UhG9Ccg0zTifTEWMG-deJPubXVudmrjOfze1orXpCLpPOz88dJimbyO9K43ZKov0yzdAGjNvXdxIuywX9jb33vtdaU2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sO_dRVmAntAUHYOkP3j8i9oA2dRp8Oa2KAY9f87Fn8h4a0yFLbLQ1s1nDMyLaFPSNc94mVxEzMM37tUfa4Nac_bX68eNLi_LNDk0Cj-W9mzd4DU_ubVq3d91Mw6opPogbTmQxET8dg3xTGqnc778sw_7GUn2PE6cHjuaJy7LBxDgT-vL5QtBzOOglklyR3uJSI7zRLONj4_rzrxtSZVlZi4mjBR981YJPkZfticsjU0QV5bkS5EcuYINOohAahWxmBKkfW-nf4gQbLdl2Di1nFzOxINPoyCZqcUFReDN8zlBfNuMhD_DgrU__GsG6S1OInv0Rb2ewSHS_t0TqwUGmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzfuEhJu5XQpgUjvBVLoynzWIBGbrVsQrYooYfSzwJnwG7pQx2gihvlZhzmtVypRblxgmN7uoN1UX3lWaTspXkkz9WX9KYvn4CXt6n0lldX_uswpSRmpUuFK-FOvQKFK5Ur69nIBlQJUkCnDhN6wOnjQi5MMqYUoJGZ1ufLL6j5aD7dZHJH2zzs-vr11VaTm6pjxJ3eCyOu-BvYUVG4VeWSqxxoR686NeZLoS8m8ISU15z9o5-kjVzbLWmsTFbMgeXHjrwtBYPBqzsZZxme5_Hdt78Xc7l-CkPv98adDJv7BgqyQQ5qOwtoU-4u4PMRTBJPN4AHDJa5wb4N8FT6aMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3bbSOpqj-nLMTBokswYax6--qXK0TJ778d-icenqZbUOwhXDaeeP4mM70bkrZ5XudGOn_nXcmd726FJbihOBS_IDuUny8XRjN_bfhbPfC8_C9LYylrSLHW6fQSsB68x80-n1ei43ZytP_Geqdh8-hGOCe7uaiLbELs94hww9wVH1dVpgEb8IN-AgvyRaieNndo3ts9nVfz0oLPsPL8Ul9VUXYiGvOoCkycUomrJ3hw5W-INmrzOl9QGyd3NuXzC7q7_rVX5LqOA7IRzQVNm2I5JiKeNWu_ZEGoA3Aisc9aKHdJ7OE7JQP3HenqO7KYG4XES_b4sN2G7oaU3vsIwbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIDrcKPErbyWHiq6g5ZKSQ5nO_xgHAZVwZQ-koocECH_916F3UUteESTOTAiRuxxoQxZ_Fpa2tftkYqcJypPYeMP0atpvENWlHnvxe0maeh98N3xfz6Dgv9MHxpVb1tj42S0BdR4Zwu3SNTRnfm4Ir1pp0gZKAhQMyyfMeHFCJUa5cncaz3cRvSmegkeg6t05FD4j5zuAKOAC0T-udIb9oF8SO20IR2FzjnSEpcSYFnj74HMdtJ9ZxGxWDYKsdFMNjrGMocNVMdgcoryVAObEAbaSqG8dJaNY5D-rv0iqO0MojYvOcuKh4GYRosMANTevpzKtqBTdmRy4IbQLF6JiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfAFBUNHWH3WFZOT9gtCd35rFeh8g0mJRcgwKDcmTEUW_RadSRYparlwEGQ2xrcEwclQYQZiJDb_w0XrQ3sfkniSsv322Yyhp9EqMtIFZLnCLgi4LEIQ-VxZyDLkHMfppL9NQZEziAuS_1jdSy6HAsAj1uoy2WCyvzPPRG-yYgUh0NmFujiCUhIftX9TAbuUkzoBpIsi1J-CC1S4WnqSozgKASd4x6UQEevtEsIq0uL4YCL8ZzFcgyakt-2LZ90pzqSJo3r-Jy0b9N8ryHlbFZ8-mfJ3nU156pW1zclHnPho43S8hWEo6-btAmk4zXJMXMKNWhL7g_QzIAhdDsLHsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIF2vICTuqxUeH-VwYzQTFySALe_ruElbdI-LqIib5ozeccC5DRpNlnn0_7vuL7INyUu1WlAl2FCULqQmbPkJpV0EIqqmkgF265p1R0HT6cjeJ_63u5Vc63Nxl0yJkjdn3WSlzo2cWoP2bs2nlCMxmuJgESdVG3avpXJdUhv4KWJJMuhe8pAZ6pHjzgMbkahzcbzG9TaMeYU7B3MMTgszGN-55aTa3DKqkOa4nCwzDXE4ctFGs_9_DKjNuCyW68WIMT2ABEljA8En_NM9HkZtP9y0kHBzPAzKH9yZp3Bdv9Agd8eEpmW5nsg2ZV7bk_SKld-A0QhfxkOg5ekQwCUlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5FneYyYcLtYOkhI3DNTEIyu4mghJFLqU4wNjiL-4sfPFiBX-Hv7TnD9-KiLCvJ8mYfcmPStg72r34H6VFVUY3ePIvUYUDC3zWIBHYJw1RHK-CDGQmX-bdtjEtDyRRIDcCrA1E0EzbdJLRTN1cf2xiV1sDBVAAAIwSdxKDukbdmiq6KKjztYx0ScGiU3tp9Znz9J8AwTetCVIyGWTk7uRAX2I187X3dVfbCeSVIAM21tPdNLlcqC-MFGZL5Jm_laG0HF5lcUftziOqySuzJXPyNZ-Z4tjC1AUZSzDZ5TYsG1tdGQSeddjOHSa6Z3vdo4mq5z1zB3vY12yA3-Q4RppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7eQ7ib27azYWQ_KBqUxUQUnBhO_NEjt2a9SbZB4HOantbA23NHDGqVLsQct6p-WgbFfy5WcDBQaMdPo8e-LZLwLOFRSCrCqShTZP-ixXhCDBKV9HHqzQx1huUArhqPNpXPdV5RiRU6jbaYzOXMExLJ-CVbjYA4v7UUbNKSSmnI7xq6OmtByypO7cmJAsOkxJnzi7o_U0UvjHkUZBZf0BSjOaJniYKQWK-FCwqmAaHI37J3_9BO7X1PF1Fk4sbre4X58wyOTRVOUxaeKDAwv0yXwDbqjkoyhzJj6zDb2qMurkTL2BYPdeClWKmH1SH5_pX3NP7WeNXSB-Ib2wycKuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fpd4wbofHwDKbUAP2Q1sBohjc1lZDBeGcsnmt3OoCKtg53SsZKXWxJ34MOyhTk5sd3NRj5py8fAb_Y4PxpsxeaatND2kQ_1yHfU6yrRNXr92TLXFozz8zz6o5wF7JUKDw56r3xKaHDmKBVPfqlGWAIIk37a_o8-9pMe6dpRNT5voMOSHeP_SdPCwwjdVSivVzHn224D9jaEwVx0VsT_uHCt3tHnvMiGEAbsrdlMJwO_rfuBV9CJGuhUAwbPArbL9kZn0MNkycvvrHTUabciVMQUAKgaiQuSet0CKdSftRKev-3dvcKH48qoxvZrSL-rEGdzfu4qEry-KdhEYb5om_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euGwDbISjpvFga7Sb9XsBRWg53ii7nHqE9_NWQy_85xL1yAosgt2jsA7JQ9MAcLshQMIbFgaxGjl_wHSB0Zuq3lpYiAWqDhvDddl86kx4t6moYRqmT6CT_O9E0UTywHoyuG0mu8V3nnncaYv41AUE0yoRNPTMl-9f5kacBR54UKc75jHlMw3FvSiWrjLT1WHA_R_SgUCQXnKJ1o41O9iGfivwB-GZdj7DehyQh6SxTrr0LxbF8GqlkT_EnE8NOkniqYvwyxhSw-2kWCNdE2Tl7AzaXjo7MWOQyabCXOenu-ZiviDc3tvU3oGqiroDUHmVcUkYw5J3B_8jRta9vaPUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu1TjoLeldOiRw0Yijmj1XhJPkN9Lq6JG3mFdf2t3jynVcaivgruY3TBWzkMSOIvO_DiNSGh9lsqjoIuX1-GNbje6VIyPaMtmsD6NYA14X2gDqo9xzNLNTzpXGz3wHuHZW8_m-kl_FVfWPVPGT-OMvXDkVP9SnsbpFWinVOcx8_QY9P_tLdNr_e-t2678iYK_3Ct30cKQ4E7pBPP6BKnVtq6Bbt7s7EknVwBoEnuYFqLqp2_RBNstHNS2IMRVQS93KUU4_rhm1_eYYg9alUJRY-4BrhF750GmKFv6zwidrVS0rkLt70e3Xu1xK5_edR_FVeCbb4v0Z1fOnh4XbgnCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kigt8Q4kUqpJAtNzFqEAkDOaopJ0CCx_Dp8kEvbGg35Jgk-kmZkptXeHD7i51a7jQ7kV7rPmrgt6vdQ3D0_8E8HXwnFNhrnFzjJ7gysjzYior9nsk0TrQDGxaNxZ497v_lyCiFFMtqDA1Yzz7ND__NQqK-wOOYhE4wmaB3TZpGSTp3fmzNW9WoffKXV8B2J5c1ywtMkXLRtMCE29GaplIaouRqcWDR39y-nUwZqdROzAfhees6I5yH5GITwvaNxf1z3W70Lrw-trvYYt79t2rJaW3Q2IdZGJsnkvNBahFhSwWdwhM-odSOVtUstCf9Bhr8V3nOrMUA7rAT8ll85dPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeGQi_uTHAN3x5md01TlrIFH3iJJkZLX4CkcwQJvjWGkrfTuEASOKvjtcdEC7FFMUVeMbG--Yay0bRsXxUJEWdj_JgJWlZFJfepAx7g_IrOsrc-MaDLWusHWNPakA0R-a8XknMCPncISQPBYEU-UK1_JJYHmwUp_vmh6N1mXaR48lySNF-_JVefCMTORL7KkHE8hIOkhbaXpcEHozzdlh7wK6F1SbIvj-GRKUptcSAb1_cFHuGZztrD63sKED02hyruETKbsir4B3aUu69PCdOpx0ov3tcRE76r3-Ta-OhrEsuDvPpkvz24u_UoY37j5HyLeE51arVfTgUOYAfIyDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPReWOzXbaGAQ5IvyoI8nr1difGMLOOauh7QZ8EBEDMnXDzQHRb19uqPbpz_5uWIi4q0QxKVtXggIR3pVrDJeLbLQxaelIrw6erCKc2cZ8UrMJo5pR0ySSqcnnQ7K2ww25eRVFuocqjPkg2TCqPiVPeSnfy5AijJC2qSWGy33jlfFjwq1aWZLdm3Um8k04iGBoOP87dboX-tKxtzQ4KQiUHjVVD7_kQhVfG_xpnSpM-NFnZci3y2rCCM6DZi7wVU5H4m6YldS8f47MqhfPz-xYJH2OWxkb3YxQuCZppI5-2zWaR6mjQhpBFghaJcu2GRUxfR6v_pPpPOZSB5hjkF5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPQ9kqg82LX86CmEjfdNOqK5b4rQ5NXhMAmxtfO_gYqEOR68bxEgLZRNFs9qjLKn9koNzCS00iBFW_MW6jyp77rmYrGa2iWv4OxlgfmIt8hUkt3Svf1Q9psNjciPldye7axHV3KDjphVrmb0RZUxyozX8XgO7J0PUffoUcaexMsed3fz4TzLJlj0N30ZWyJ8U5QRaN730fcKo5ePotDTT16CTVChRzB7G8-QgleMZVWFOY3o202wLLTWhztZDTL1eVpxXDbh3ok_6bJAM7RihSrnF9rQBYxSiwRJoqOItkwbYcDUEsFXMBPdukhZBFCQsiRY58LsIr2evsAEO35_Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVKcx3NcpULoYKuCWcZWbyv4reNM4JBWs8U3ePirvb6-9VU-v2du_UslnEhhOr-SDkZNBjcOGPvDxu-9vQViIpjand9Yn6B5uD81FGGx7xMhsBwnV0R-0rKbGodbzXiUhI0MWouQeGopEoPD93ypZQmiJdm-ZrcFtiWxwyrc4_tAfnqPU8GDrVTrzJ0wPMTRMirZjP0nUxCXqynifFh3CzzEScoKysS6a2d1ZWxGbnjqAXQhVdwQL4SVMuzeWw5anij1cf4heAALvCBUx8as6Fnr1JKymCJP6QGReJ3rJ9lFd08W_zVkIqD68jxa77Z7kIoiG7fcYtlu0lL-uhPuTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvD-BrQMCErWoLfCoGZUzknmYjnxqHpQ15lOi6XP4IjH6WV5ZFnYsj2N00nj0_F5ZJDh8XLpCKHDulnmZAqCvR-HbALqVx-OOiB3qTOp__5I3KV8_epMtOveBvZ9QHNJ4gI5ZhPjNIUoLZ3ZbXw74m95g3ZqYj3Snq8R9KRD9TgECdCJYUWGhkhnN9qPF3KImQ9aBcN7OZjHvTPRo2QrXN4N_Kt-tur3JbQKPmFZkt9m9iCLlpEUcDellIT8GXvcBlwUVwUg_s7PtQxpG1coSp91JmsgzJ31PELAXAyDY06JvdIA8b2eE8ismY1rLS-eBbyIR3G5PdrpgG3EYcpeeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBBJIb0usohul7uv3ezFtVlusz3bXSdwFR11rYo9fg5tGla1hTUqsfGLve_NcOVUYcehc1eROoD2nlTj5yAvzF5F4GBP4X_4yEZINlFTXEhT2GHzuwtPVb_sytr-rWNmdREEwHjqjqi1izeuC2LmLEL-R6eJtIjTwDkHJvFT2aVIodp3xmFQs5VNT7MRt2lJ_ipr51tZzFdfLYKgcJyayxQaAxwFy52uIjGS0EZyiVHf_5tfKEV4uJj7OYFfx47bo561joM-k63H-_yd_mahHSenA7KmraIJDUKyyILyRIrZwpN1SOb3DzntUyWEg7Es2K8Nqor00znrtlY4Pq7eqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyqbx5vduDDIIDPRO-NNwt3zcVXpMJiiwj1eO2MA4Qo7pUb1SnkB3StGZHK5fqDgHB35ZgwLhW8N9EWALo1Th7kR4KaZVuGBd1-x6VQirAanEumvKTt1OO9wJ1vPMN_Ie1boLqLqMta8VOt3GGdOuRFLI_7v5u8GTK4SSsAuG8EPNCrH5r_jglitFGw6HeAin9ocvgUY7bfS8T6tU-22WzBLyV5ijBxDOGumyJD1TI8NOmiVTQPi0nyEx1tOqDD1EJlnfOxiP7U_YxNNlx9hAzdDyOhF_6q5zy0iu_TIgovDRUAfuvBH7x9BYlcpspvLLcYu4iQw4fPSpYq7F6vEtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=JYCC2ticp-hBaNdeF_KXjzbfIb5CHzvlyQp384XKifdkn60kSUmGHccbvW3yVUEdkeb7Woh_2mKnUlUTpPapHcdVWH8zy63v_z6_l5lqFn3kdphlGEWALMdZkAp9_biwVe4tJCnQ_jmY27YaF4bBGmmPpP7A72ondt01kjP1IhgnIIGtziRBcMRDB0egPbhCMwEnxsc_yenNS_2xg36zbCMeako_Vh56TgxwZ3zoEgVdTaESSMWjtlkAi8GqC20k8jxaZ8bkKekL8xOfl_xnkusuC8xS3sOOCu8QPPBy0I1UTxz5qsIw8BJYKx9t19ajTzTurg5nkf9pOxByDif59g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=JYCC2ticp-hBaNdeF_KXjzbfIb5CHzvlyQp384XKifdkn60kSUmGHccbvW3yVUEdkeb7Woh_2mKnUlUTpPapHcdVWH8zy63v_z6_l5lqFn3kdphlGEWALMdZkAp9_biwVe4tJCnQ_jmY27YaF4bBGmmPpP7A72ondt01kjP1IhgnIIGtziRBcMRDB0egPbhCMwEnxsc_yenNS_2xg36zbCMeako_Vh56TgxwZ3zoEgVdTaESSMWjtlkAi8GqC20k8jxaZ8bkKekL8xOfl_xnkusuC8xS3sOOCu8QPPBy0I1UTxz5qsIw8BJYKx9t19ajTzTurg5nkf9pOxByDif59g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
👤
در شب درخشان لیونل مسی؛
پیروزی پرگل و ارزش مند اینترمیامی برابر سینسیناتی
اینترمیامی درشبی‌که‌مهمان‌سینسیناتی بود توانست با نتیجه 5-3 به پیروزی برسد. لیونل مسی در این دیدار موفق شد دو گل و 1 پاس گل به ثبت رساند تا نقش اول پیروزی تیمش باشد. با این عملکرد لیونل مسی به آمار 11 گل و 4 پاس‌گل در12 مسابقه فصل جدید ام ال اس رسید تا صدرنشین جدول اثرگذاری لیگ باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkCAX1pA5LDwkk5HC6KzxnCfvXun3jQS_M40gL1qeAgDBkM0ZY3FsZoStfPHGYYqDp4_nZViFClJxI-cRodIzNapszKLrsBySqOiiL_0lQ70rI0_1bSg4kk6FZ40P1GuaIrG1yvAilXlwFICRTi8ewuubIlmbAsSjqmndaEwKARAyyBV6Auk2AsoP4JNzDDkJUPtaUCnOIl8RpjkvGbhop3v-JjPHfV0PgpTR9QhdmvgzpLoQ_7djiQGL31nTRK-9s1bajgQoK9ytmo-qOkdG3JcETfn_4eBtTwmT6im7b-t4OeEcvMPySLJQ8jgN3Cj5X2eeS4e7nv8TzsY5eo9og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbGIgK-sa96Cy0QvWPO5bvcIzCW-Am2CcQxaDmuPwC5-66B4v-lEqS25YvthGujVSb6fTf8BBuxT2qQuEes99_OR3GgoJgOHUM4uhgtqIK-3VhAJQu4enHp-7PrwcvRkfdercv4G3eMyhfcIVRDfHeGeIyRzNtLaTfLtp0oBgX5sUtPTFNVm5mJfqPFCsr9ijnB8rWMpQjNQPmnvwvjUdgPillNSPRWOroRhqdcWB19rjoZDRt3NCQmHrIbE3x6WWV2cadBdmUI4CdIEHqgRPXRKaDwRhiscJR25Gxm6vQ0t7EMKzPy8BMHC9On9e_4lN_8NhT_j0C9QWTDJ0P504g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0bIFlzFNmdO6qDohjI6LCOxJrHlUUYGbP6ZCBaZmjOvbdFkMmekX3SDp8B1Nuo55TZ9AUwv2enZpAkYb_qd96k9n7IYoiGei8sussDIa-bL_OcB2viXaaWguGOt10JgTMmtmbpyqXBrcFR-bm3zNwXZhe4CPb6WtLLd8I3Q_qUQhYTLcpir47w2kEJV-okAsSVMffdAJpi6EQHz3IRQunfNpJTcaDdcuIPtNvVyPYO98v_Qe9bFUIIuC6poqXf9xeyaQuW4ACihRtjjDX3Ojm8iIG6mfKUtR-JXmzdRrH5PyQK9ANdCkFFvNSg8nPBK2MlKuzir836XOT5EGIodVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUgCVz5gdSZKiV9zvbB4Mq9CxBBS09MzhMIpo-AifYcFl_vKfLNfKIo9oJAk0Hi6yXoCGFuHywNpSkKoLGDwB07HsRkE8XbLHj_GL1OFYXbeKJh9b5v9wQ9TrzXSah0XKPdRUpmSwjy6P9v-Bly4whZNGnfGcO0_iu-C9pdTkdBRNKkL_p_fdW84giEMnNJL3zgrTwUlECzMiwVyHSo_rWCjjqR7RFbPJw5NsG86D3p31t__4TsJ5ZIU13I__hAXPuwCIRohCOkPPJqLukZ5eoyKMzp2kw_LZODISpNDOWPm7o75XeiZyBH43dj5k_cVQ7ADn7jH2q-IdHmLd7EYGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isq_aG6bxu2o9Xhx7F560OamJZ3MX49A3b0KD5YKKiwc9zrfvKOhcwTM8gAOelBTKv-lU9rVq_Nk4UbMvFF2i5Uh_6d7AzTAja3SWRhtqm_NMFsXKdPYbKL-IYMomcMXE-ZdUgbXGAszyo1qvUnFTz-AWqJhPfGFPgyrA-Pq0Ah-0Ff8GviYqxU6LkeXJ61z2a1QWLwFcS-W4uaYQmSRVccfMzGJdodfdUKOy5OBDJH_oU5aIsUVjhHjHRr5x27SszRMPBpggciBpw4g7ciP2eBw9CszNigxBGn6b6dkLyt1McAbuv54ng8XU1YUOALUuIR_rze4TQ4Fzh6P3dzPkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9JFnBfRM9NRzkksYd610YuytKrDOwHyQkCx2CdmXnGct2bWeIwVfqf-bZXSwHcv2sT1zfaBgQV8POp3roIHj1kvBPtod2MPYqlWK1abqpkUIQXuhH6mM7Pgei-OuvveXxVyvSxj2nwiYVOnIlvXtBClRlZHLvIV2pxui7ii_4v42aphRRlJPxVVLcs2PHV6MQIvm3llLIA7P9RX7Q7hH4cSOWAs_-CKLbQvkLCxiySoeQEbDbyiudvJVQ6A8v5-RLprzDDa-9RPL_bbcgKNHn-MfhQKWzi0Del-C_fG_wtaxbMxNaI9g0eyIuZbM0pDnWhn_yvm3Um62GAs4wHhzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IztsfrbXrw7ADUhbp9Ilt4WVN2Ck8ZxZ97a4jb86V4oMcbPIiwEAbnSWa2OyazGwmtxtLkppEcybs8nTkmAgvTiADWsz_AFpOeAlHm1y62Hx_5CV4YMIIr0Eba6FNRDCPTSWxx4o9bor38Xi0yEc9U7Brf1_dOc5yZYzJenm8DpqP6_hCRIZ9ACY1cl-3icp1WsrfFCVtWdxJ_dMvELJvUVet2AvzBlNlZdDv_xS8R2rjTymH3RA771BH_m8uTFE-PyvP_QS9Zrgt6Paf03ObX_KsKFYV8jAPJa6Y-p1t3fmJ4PKEf4wJ6lR49l1xPl10b0gCiCkXiic7wYFLbYbzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Df1g_HFI2NT52_e-LWliUo43dfTPCoSbo7dR2wzH14vRR0X-awHgnl8OiaQN2-3UUW9lV5S9krZq2-jLlWPp6P4wEyAPpN8JwJNi1RjW2FM3J9767Ov7OlVE6hnmlyygq4_GxmjpS2ZJd_yAsCQZFeGG-LWXMrtuWhzKZDIeY4GKTX_EXGuBHLeaJzAuqIKkD61R-_n62qOLoFMQpULD4FZDBdeuK85nlgKxRlAY6T8HYKNWGjgm0pDNFtjnVsWJ7aifnVVr6GdfZ_wXxbo8zc4CpFsP0VrsLO2eQBk2YX4-UWe1_gGDa4vdsLmgeDHy24TYVMb2Pkc6VWRt2lyY-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=CANVNNQEZjRjVrllJAWmx9lGbyhfj2KfYKL2gzwQu-xAMvnh3pYY4pQaGywMW3txhZZp8TLiBwYhudjAFEBqvT3JFkTdRlxUaYTKBdHeP46WS7DmBbztTN4QiJpKW_RqDaVBhmk9ORaJ7Ywq0np7gGkp3Bb-CTwxA71CVqYBKGSaX9gL7DzXJssjJQjZAgnG83-9wh_PTaTNrRU-Q7qKxprhCQL0WKFM_0ozTXAI8gLhIqW2CE68M9WGp8KRK5QQEvVPSboJxIT8tdv9DyyA4eLWOhqr565DTEHRvKGvVNvwAguzDHFlSob3OdnxOw_maRmd_NPsBy7V6F7B5Ljbtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=CANVNNQEZjRjVrllJAWmx9lGbyhfj2KfYKL2gzwQu-xAMvnh3pYY4pQaGywMW3txhZZp8TLiBwYhudjAFEBqvT3JFkTdRlxUaYTKBdHeP46WS7DmBbztTN4QiJpKW_RqDaVBhmk9ORaJ7Ywq0np7gGkp3Bb-CTwxA71CVqYBKGSaX9gL7DzXJssjJQjZAgnG83-9wh_PTaTNrRU-Q7qKxprhCQL0WKFM_0ozTXAI8gLhIqW2CE68M9WGp8KRK5QQEvVPSboJxIT8tdv9DyyA4eLWOhqr565DTEHRvKGvVNvwAguzDHFlSob3OdnxOw_maRmd_NPsBy7V6F7B5Ljbtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHWd68dxen6G27aKKJKsIxYvIoKUAPqkjtS2EPtNrK3WTjmkDpD84QBcM8friRofk38ko5_HF3nw7hcrmaUD0RaAVryAPkHJKKBDpu4DojlXmUv_Hb8HoQvKxTWGYf-kFsUMqBsTP1FQpi-JCs_Gs6iqzfGI9kp7vERXrJ-ePVyP2pOTN-ctos6pSHDNItGO5-0GAbi7sRLLygIFl9zGRIPAOQ0uClLRrNYnzFDyJGVCqCP3d6ZdHwxPqM705xQopVrYB0a80s5y4oAL6OxYXjrxRRvwsjBe6YjdzXv22x6nf2UCgorqndkmwWNMMUQaVgLYc4FxvMqpCKL4pCkRnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpOenXjcGff0MlrDkeRJeAY-2WJHucDXQlZ4Wjjk_NDcrq-8vm9kVliWyT5wMdFjk8tw9fujjMUekE4ufNhJKEESLnRp65wPyPqsBpxHdAMpZKO0yFIFcjdB8kdcGEXXXPizLnDDdAOtBdWM_5vcl-QLhxovYP3U9Jh9JheekptuqmtOPLnHTroTWSmpIXHLxw1r9chAb2xB2pZDT1Z7bkkfo3jluQTOc0ybJWomQovGZliIfwr8BmxGhuWX756dKMd1QE3b_oKBR-ZIIoAaTqnLrGyf11cHqmg79UqvRmQ3PO0Un-GvHbAzDfGe2Mo3-ocRg2EiJ_ucNo_521Bukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=k0r8hjJBhJKz7BasmnX45UnGoezGBaL1sLVhDymP1ZPyM5Kpe3RIy9WnJtg6CTqdxeWkH1vdjr7Imq24iJQ3jUuJV1ZHubmL4UYHpDO9QY05xQpy8NT_lYazsFJ3Zx9078vqEIwJ24nr0Rvqb57yNjmBnNV7BeKJxMUccfHbOQGL6t05zeyW_emN0Y7e7Iz4VAziCXiLr_gYpwCWzg0PgW8XPnmF9PaVRH1kmUoQie-e3MSCbf_Pv9dRmEgK45FMLk0eO2t0DS87XlZR2yFz2k_sYUHS-rPWq6F8OgtxaQZe7rH3-b0yw4M2kuB7Gf504u7DPNanUPKaDN8ul3xDag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=k0r8hjJBhJKz7BasmnX45UnGoezGBaL1sLVhDymP1ZPyM5Kpe3RIy9WnJtg6CTqdxeWkH1vdjr7Imq24iJQ3jUuJV1ZHubmL4UYHpDO9QY05xQpy8NT_lYazsFJ3Zx9078vqEIwJ24nr0Rvqb57yNjmBnNV7BeKJxMUccfHbOQGL6t05zeyW_emN0Y7e7Iz4VAziCXiLr_gYpwCWzg0PgW8XPnmF9PaVRH1kmUoQie-e3MSCbf_Pv9dRmEgK45FMLk0eO2t0DS87XlZR2yFz2k_sYUHS-rPWq6F8OgtxaQZe7rH3-b0yw4M2kuB7Gf504u7DPNanUPKaDN8ul3xDag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGR-Q0q4eM_H1-iVp9AMQp8jJBn_tXH__sfaEDQnuM865hQw8rv8HNNB8vZRmbVzX9hfpicP6IcrNFUZNuO6gXdOjpnXBqtgKI7IQJlecgzO6FChopQvaJ7qn1_rAtZcjOn0ANRSHwKwLzOCjbLaUva7T2VYbP_IqneLwKQo8S9XVskuxL0VYUS7J2i3bbPUhVJTwmsrZbcFLfBY81jv9FM3ObkHaxSTgS4VCSo7a7ro-Y6_mStziEK-dqXLbT53Ano1QC3x-AqJjMshZWyiJV4WvVdwx7BT7_rbkgN3VEbF13JISvsq7C2sQ1FQpflRMtieo53e5BSxy-TAM3JKrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/vkuFRYIiDROMJcRG7auEPK0RdVfz1cJqRJu6eihV0kHCwSbO20vxHx0MlPlUpdc3Bk5f--59bVpmBrxMz-UXbQ5c0cZyL_Gdq5tHfPMnfNdw2S8eP5tLd_n8bmWStC28Htfki2ARoXobE_o4v-33ogJlTwy13BW83itFLy13bpNePqNrrU96e7k_crV6wkBbQ_fH2XBbMmG7sn5YWqJUuGCh_5DqRjGNAmobNb1jDY2c_S_Gft7YXiooYOrsxy5myPrYR5KjGgANa8opiePqHY0OZIG-GiR6_YHUmPS1cADXsHDaz06Ku4t8QUK9SaKhv45n3ayeSrTxb_VtNM1RIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه درکنار دوست دختر خوشگلش رقبای بزرگی‌مثل
امباپه
و
چرکی
روپشت سر گذاشت و به عنوان بهترین لژیونر فرانسوی سال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHNRj1ZYpG9pXVbUYlEPN4aEMhD8q48dTcgpPsIQxK3DCMAisUbsRVbGumR4mxVhDaESkv3DHDJ7L5oJP2AqB2Rte64Xy2rjq3xJDQZkSvaUSn7FHqdWHihXLUleSNV8M21EsxMeqGIHjrhBN3okAQXiqg_9w0xufctLRJWgoEnGxccvZ7lqhVM5zGc-q4vDAJ6dHS-cAjmfm4CjzU5z07UP8yefD_3g-uUQhCTnEBQLgriuqwHzfP3S2epGIT2W2po7WmDa_5RSV9JmQITtzkn9aE3QgPnG6QYhP7ay_eaagFBnaBMa9Ntpt9Lm_v3-uhyjm0DngpFDwvfFp6CpZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diDyYw5fEqNv0ylpyN_7tPqWtDSlCxIEiTs3yQQANpQwVBKI9ubJp_4tjjIY2OTSUwmoojRdX_LHkxP8pWCDkwsaIC04EYG16pkuXfFvGu_Yyb36WpFha4RGz9ve6BCtBI62toqqwmGf-q48r09Z6tguQlukNAZ6j4HzhgrAD8qxhnLx9oWDY8mEy0qmSuMz0m9zDAOlQRWRZ_mcu_Xzy4VAn0yaT2yr3qvXuuzgXSqU5rva97ICzqafQMIvOPRcnavDldegnoE-iFYXtZhmn1-le7zWsMWOWA6rykWjUSkF1dBXmGJqIlCRp9bmhVHvn-ytg7QMiCxMtJJ9VDVcDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRoimbc6I9IFVmnTHZoDMLixgweSBtDXHPhcCUNGT9UtoddNZ8kKKeTxoSGbRvymMWjoQQmDhqQs0GhMCKSO1CcGvP6EkeoVq__UXxqgamXBevt_FSP1xLW2kADUk1C9e6sesHNbk6M6BTbzfrBweWuBf89qlgDy1Ixad07QD16oFwoV7nlL3jDz6UxrLX__mETizmvOIoHKWUyAp15dBHzRWi1waNA3U6utM2Z42CF7Pale4EFUyHQk8R14LcGjTeOFh1tGRykKpOaN4PL2wy9m0uy9lp_Vf3_C4n94vK2pRAu4ZWfGLyZm8DhOzAlwo5ciAAEbDMbb8Ds4wuRCpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuQBn_uqA2sGCERLWz3SR-95qL_flIYb3kGbi0tpX2u7OwwXXmgPeex7LAdI4Rfh_C-MJISUqyDOs1nC4N7Uk7zoiwcV_lGA-lhlUxrsw-6LBv4c2VGEewxZct7OFkN5Eu2Sp5DllpMe0pIjx-TKOACF57yd1fOkNdHsaWoxeD_J7-DRw44Em7wKZjyxS_xUDxTnw_xYIv5Jj2vYZjyrwrBRmGuJneqX1vB9LHd5r7m8PbwB3Jkn2Bz4xBEc2lSHFFe9e1xCUVHJC8hia6J-4DPhXI0hiAdsgfPl8mplBQ-ZevpMRDFUqnUOYWzRSOAFkzaqZiql6FfljaiNu5N7hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFGYO7OmLkKcFXvxr8MjGTx7U2XBk_ahu9DaJGlam7T2wY60AfD3IurNKFXGSyVrzXWwk5InaOTrRILSWSPYnuSN6c9tPh0ehtMK2ABmLUpZVTi7FyAf7HlTRmvSK-L1aT10cS-FNwnFDahZkQH5EeA8_16c0qDIVcT8unJZShS6y7slbHchdNCzOHx4ScDjYZ9oLq1_1ilj0BrVIumbNzl9CDLYtMQfHVJWG_Ox4GyVDcG16GnrKK34HU_PVq25NFGJj1WQjQ1WjFpNUzyYycWATkSzTFYdrulj_bMdB34BPRAiH8PuvHfNJgZYxGnwdr3MQ8_5Tg4K5XCs1SqG4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHE53y1U1SsSNJbanS2slFHsnAicJ2vWMd18WjhNUnaN32Hr6hDKe30XviowvRu_VkMlKCQX7NvRIoAbCu7F45OAsWCO1w5Z7yty1D41tMxN5Eu7s6SeCOC30VjFIkl5SuclV62NCbAaB_ooSPv9IQ_G03UvcIg5IG5YDeZqxlnn9MTX2KF9VKTPY1XKnSS10TSTECyTlkiiFdZ-zPFESYmjPiIEjaT39L7E2zEFPVRFy5FzrecDWGsOziJAQVKj4Oo9Vdlg4Tl6um9EVlETRGoacaUeT12Al7MNuhlzRQPNB7vQxSUTQHWXoyjQcNHYopCETwpHtSyo-JblefQLhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdropXuxx7B43CfylzigwnmCaCgJwvMm5qcKJwzbkSZhwLuB8fhOVtb3HOOVeWiT8CuLxdO2alo40reZv5INYrtqh2bLRcjc9-hRH2Peoz6pRPOYrcOTCMt67EhVvrxgPOEHk3LlJuw-UJzR9_ONWB8U-f6WyYyzQi3RLWfYUTXGLXx-x1oh94uBW_-yvkoWB2ZXpS2Cm2q7dCEYK3WogK0a1jCr3-wM9VFG_ELXAu3UkiPnXc0VBrPOEn5Ykow-5YOGZ46gT16gNpCKrw64lLSngOOYsaXyynn6nxu5NFT-VhF4wOZ7gA_BoqBoS2RhkG8gbXlvsnA9GLEyae8qNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9Wg_MhiqU0kvNksd0ieXZ1xwU0SkzKi05saokIUsUHBODr6dTFWSMy7MH8sLQ9AIZQHP2vGNBb-mgEgW8BB_Pc4_0c_edKRJa_aYeL26I98Quon51zfBhym9ET_MT_l54XQevBx5kW1Q3YHMfUHC_R0WiSj2OUpAi2x3Ho6t142FbBwDiJJulX1Y40Vl8yYe5jAcqgoM0sChgwN-DcWdgOAI_mttZ1XislmaHficOsdDmYgWueSqi_g0wcCVAPGqLMeEKhz49EhM12umUiDbWca0LaQ4zoLmG63YssLUdScNtWRek1Cy-Jn0rveMoNHejqqZzzLN_g63SR97O5GjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tx_M-qKtfhiEYI7Ca8Wu4yXKP2-kC0o9ZC_7zRxMb5jEVMt7-sudLcMYg-sNAu1EK2FdTc5_jEOWF36Yiy-2OM64b-a5-LPQB4c5cvm3xacv4DDBq3KjJjrf4-DRZHFZy6gzTUT4vQ-2RgbFSZoiKCuEV0Set_SIJSd4Fs8HDBtUnHHSCtD1PZyy5r7mnw7C6pWcWhhwaM1E15mNWAVrbA3mfMWwQKbW3h8KiFQlWfOBdTWK3Jt71dMqmeeXKACW5d1hDEpjaggf7GEVR-k3r3c0ehyTRvFzA9CbTEwuCOznde6aroY09sM_VETmlIzhNjNNgDRJe-R7Q9_gz2J1NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_M7vAMLXJ24QjUgde3EnT3fHrg53I1NFkc1qg8SpIzCqQU0syYg5EVvFEHvTzqR0BgZcRM-n6LA5q7CVZVW5h6JwwchDR7RI7Tb1IigEyi8gXRGpa4Dr6Qn-f25lj1wLwmY5Q0fKX7RIM9V23pLsNg1mB6LD9Pk8bOF9ViUHK9mwyyA3eufh4ocxgTtOkKscXn39-cw-b2iWovindkgFc7TY3cSNh9fl27Wa7CZv2dIfJvfwwVB0DnyXgVb6VzckOhPvI-j90Kay0Y7PVjP610u3VazHDOLelOXtIqdvd8urdgiWVaW2ceifeLLImh6L6VKmdTRm9XRXQxXpuw-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cu3mFZDSqWgOOAV-5jPwIHtf4vuRbYSVPLJP7QiTBGy4UDgjtMMkSpeC1DzxkloGcz7BTQdie6EHpQ2mUfGwymH0OAeOImXNh5iOe8FZh_vf7FCz9xUJqA3n4P0dlGwBlNFnu_p-AbMUpsp1K1DK1TQlcQicti62D4bCk01_fFGMJWBxCbMNey1dqqZke9KV78AzHBloy9SF34cylfbXE0BoRDUVnKkbyi0_8-k-kwgn2GtB2NQ95qRCH9Z19Bk-jG0HM_b365ZSii6IbBodmFNVudD34gSdVAaW0Ic7Kz8vqV9T8mO4vD6GjOlIdpCGW226GNQv6DMOBMqZ4cOfsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G58tE86gqbL41RR93Whz3JEnSINayJJip2eLToSm__YvsiBU0XcDN6C53SMhACo95TmWHmBGFsIOeQTsKo-fznY6bmVamRku0L0j779osel46gOc1kIcJU5fO00zlUiPJEmC8TJ0K_xOrkNCMWo6dazqpVKZ19gR0bxB5hIndfcCOsdi7Fz09ixCoxe2cR0WlfB_bJKvlBsD-Wk8lnrFvu6KcwkR1SoHO6aQNXleZ-JQsO8c91sVRW3Jz6IJImsKYkb-pb43HlT807a1okkCQI3zQs6TfBNGeiFZbTLkHUVIlQnZJfa5Kn-wImXMSArfe1QSGJ7NGiCaCT_y0FI8eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=qaejyGEIpm8ucRgKXRC1T9cxeoXoA1bDO0AiGOPZSDLb0EA6toTsR2GH7pdajVMtLOweQUPupkWC6R507JEcRNqdzlzHDV_cWfrTM40-nDZHWMuApbYop3G_rJZaxD1SVgd02K6CSHx7S9UXYZ3vMWqKUH8q8fLka0OjaaR29odw895iESMMHSKJv7ayN8MoZigb7mzj1h2HVjV60s_G0LjrMZhzoCRS-VSSYotlfjhG6Y7n_rR2Rgbpi-AhjBRnGawow3Rc1_736vFYQJ4WlzTlRZyR11Hp6GOZtUm59AUuuPwF0qYNilE355ntOZBrFTzDbf6HZSiu1DZt-9fX4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=qaejyGEIpm8ucRgKXRC1T9cxeoXoA1bDO0AiGOPZSDLb0EA6toTsR2GH7pdajVMtLOweQUPupkWC6R507JEcRNqdzlzHDV_cWfrTM40-nDZHWMuApbYop3G_rJZaxD1SVgd02K6CSHx7S9UXYZ3vMWqKUH8q8fLka0OjaaR29odw895iESMMHSKJv7ayN8MoZigb7mzj1h2HVjV60s_G0LjrMZhzoCRS-VSSYotlfjhG6Y7n_rR2Rgbpi-AhjBRnGawow3Rc1_736vFYQJ4WlzTlRZyR11Hp6GOZtUm59AUuuPwF0qYNilE355ntOZBrFTzDbf6HZSiu1DZt-9fX4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiNIg7FIrRqwMkMrph77mdhdcv79lxtpNqQSTn1w7STzlFwsHGwC0Ez1sEWQMd4HSmYxORLzRoBPIkmcPktxXcIbz54pd3IQUIqIWrbKVo062_7rVCHIN7-jAWLjzsqXooTI-M9Y6uuFko9u1UHBpWN9LWT4ZQdT1GkBPAHQ7cjANRhy_5qr-bsO2skr3cfPPlXoTtO5AuPuRU1fuHy3-Jz42FYxSwUlLCF7r8xhIbj5lbFZrov-kSIZDMvzqSpQoFhHDIq6lPEChBKDg0kT6hdrR0x3VT5BrlT2WrQtTOVF-lDF9MTeymg6L-EkpgU6ma4sXZyvc4o6JmwV0EhuDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8jUHzlMVWOzDZ0r5-Nxtm-gBZdZKOJ-JQFQ12zeC9GtkDK4YUPScGJnfwTuZF1FyCw4Y4jnZ-GJwJHGdru1_Db1oJveQgqxNk0ZfM91RVtHtlqI9PA3Rkvw_r56ZZUDYBDLZW9IX1Io21xfUvdducaInuHIBBB68JHqAvaHOU3BmX4I_r8Et5ApT3oNsi_-UZYJV7uFIz1GA5ReRpamFfbR-eov1pvCT4EY-ejdJB7QsWfeWgsmel6VCjdo_QADIRwtPXOrWbmNxFQmlzBb5fs5Wx5r30qug96MQGw51tvd7Ug-4Hc3ltlw8dCI3HNqaZvBavA0wkMLJop1lZrF_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Srndhj5rNHk32mf8jD7JiP2jCn5roFdbr-yCdMnmM8PPy77YcN_Vj8LLP_UiMu1OR5RMDnUQvvCPwlJSHtp1TjfsH0mpvgO_NtG66V8vyFsEaJS21MuTHeaf_L11Ppt2ikToVe7lKEABvhZPn4v5ELlBQ4sE7ZNXRgLvBoEGpIOnxMhvJ-uKoUzpAt_IYQ2YzzCjINvk13c9sgJbbbK9adiqXXb6GSk3yRpEhf9XqBVw9UVf6vwp7eV1IbKMtVpW-ysAIo8WXgJR0r2GowL62XVy5nmd7rYENOXaMu_ZjoOQmn9NfkRWbrRQJQ_bogwDIco-qbfJWs7s87Mop0y3Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enH05bl_mX7MlogZXiaNU_qJQvZvN2DMYXhQm5L-76tN5pg6u5YZ86JULTYy_GTuHvj-jzaRJ4RqLGYxarUsxNdhH5tk-PkTn4s6kw715aKOqw5Q07m6FFoOBZGjKisRTU923D_gVd1PiClz5oN7-BoQ4pEAXjw0mmIg7AQHpseBcX2Mj5eflyoauBNc4v1DMf9REGA_XErPh6BZUSVeWEWjnpoQL0nu4s1vddKAWnY2fzoi8H4Nqf6I3pBcwLUN38_sFozHeHqvZ8O0SkoFsanzK44X3I5bBXErenjk2TLwtife6ti1X3sFaGWunV8ifeYumT6pmUj0Fz-FUGRchw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gy1twHkDqVzh_ych6aRaWA31vfRUeJovjuYALLyubyZFkVjDJcD3DW05BTz8RZnCNpzVgQarXbQ-QGJTckictcuu9Bb7gJ9WcrOrcfbljJrKAob4eFpimPjI9zEygi1zUx5L3rzYIY7HnmJMfs6_4YJBZVFugLgTGNtlhipg7z7wdG_hjdw_Ue19bDS4SSRn5e2c2JRLSN29dIzJhDx-QaI6n3xLrIS_HeJBc7j1GUQog7OTqrJ0v7sOC7trEOtpUCD1NsIV8Q8a3mMNVP2p_BwGsNYFnII6Mi1vvBnw_oMHN2GTHQxZsAz2oOcnSULy7MoDvpaa86nHQpxI6dbPRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnZSRFDLChsxXbyf4doslAmeo09J64qIXPy3dV0ImcOHPuve5RfYfkYJe1qo7lJy4TDPu4d29qZfBGW9XFMeGjmXWegmEUDuTwFHXPzu2kPAVXS7gOjz-SRUdLz_kJ-PRKDMWwOJeJsjEio0mawiAYR1F0OYOQWUH2ezmsN7P8tlkbe9yzS8VSGTpULsy0n94GpAIKiykylX_gc9x98boTAsZ4tiXJ2vh1rZXDoJqQs29leux1jadslpYza_8no0H1M0JvYYxkGLk7Z4kqfr7fMedmY_mxnY6EgTznnWF2GyFXdex3JcQcvbITQhM2QMAe1_FA8iJumfdAqyUBH-Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p53TGeYQgqwNOd-a2nf6oh4XNKQNiWwhECHpdq7gDpcjZYMjjKqfyvmc8t0Q5nknR3Yqj93yeR9c0Ku2s2nakjwvrsclrx8lBKrLSnQFI5QcePWO53BKblDSvOTUc62zncYJOJ9cPXvHsbcjjgRkilm1GZYLSB25zo1wDDZ2yCrLudUMQXh4TIywiWic5vzxHsXgLYSgvF5ii5X_oPOdNm06U4PKry1vC0KHzx-_FnRAVex8ouejlRwn5DnFPXhVp1FUeluN5-cOjB7E-EO1spj_9DFbwJufawAQwRjRiyu171ylPE-1SJ-8sYRVAmkY0ih28WcsJdCSsymA82sVWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y14JF4lUdg-fKyzF3jYvL1_Y1j8vPDjatkibI11DoCvgvRUw8nnb4B5NmFv4aYx1eQTp514mXvd8M-zjWn5DEaxlxuZBwc6OcPxzWBxHWh2eDvBTD8o_gVeMkbvW-kPoSmrfyboT1hP4O1kQl9n9YooTOgOTnQJcuwIYjyJDA9xJ5fKVgoSelLTAL5eHdP-eaE5PiXRwk1D_mYoiAA7YcFqpxRwzR-slQdZaO3GFsNdSkQU13C9sBU-94eonZddx8Hf_0N-3-PLo-koIv3SpPkQlIyC7oBWwxDZTO25sLF2DmyKptFWeN1oGP5QUYDAHO-5-o6LAYO5arcMmJIrVJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFDhZMwqcEj7wdFBYymbhuwcle42vIh7P9XE3WCgX3eRSOMNQ9JXbjMnTxfNSL7DQLfbLQ3D3tsIv0cSUyl7-twzpeOOjQLU5E7OASoHnqvoZYihK0zcdCsFPoeQ9Gf2pMjF1TSmSy9V7A9oSq7nBkxXHQv36lu1bmQoYQrrn7fiMNeLJ1TZX_zsRYTDV7AFd1FxJ0QywLgymZEU8Uhlw1Rb4FjLYvF4Nz-BX7tAO9tEW4wKMQLkiBqsUPXJgo9IVbDbGy6BU3b92kEQE9jJmIiG44WeriiiH0omiw9t4GEJtl0qkhmn4_vzkXCBky7N73S3hV1HT2TiK15qdMR3qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vt0G66kBJnnxVaWgLwwjpZFbm_HC-Z3F2m7GeRrAFS76Md9oAx4hhQ1yqRLUEV56-8xBBFCj1gn-YEq98d0ISeRcU2iKZljW8s1kpLWy9pgSAg8YlUk6SXWRTJG3FuqqfhvfAKd8_gf-D4ELejOMu6JRuVb_ELwJktsSxsSjvt6oEFcm9fT2wT-86f7xmUgTSDYiSeK32aDGU-UUk-mthPCvYagpVFdyHQ8_Cx-CmTqTWI7NLfkqx_nz4x_Gyg_Lz_vIB54Hjq4bfCkFFDYTXOPFwOtnAbg22TC_5PVo7L7pqICSS64omyl_Q6WHSt6x1tinFA9RULoL88KzJpblLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmtGG8XIAAz5VNdhlLeOWo7chqIhHzVAhUjA06lNUF7qLYrtrQv4prUEPgqiv_UIFnUEksCcOTxLtKrwEsUOMfXWxaLlwGYY00oD7OTM5ZwVPV54TtfmbnglBEvYRoEQrVzT8Z5T642JKCPnJ7a-k9f1Voi-BuE1W08QGNydPmFI1G4t4AHoAjEEGiNUcKJeaT1lSPwfqUq0QzSBgxV7d5-Vddj2ZoJ_BjHd6fqqQccZC_boIm_MrahbkAJwr3MNboWmAYfST6ahfzJxQaBsgBz2qsmEN1kOb5CF3FGo_8fkB5QgNzT70KJrqNjl3Ep7TADm2aenmhzpIu9KfAPZaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUhimrg1-K4Dc8x-_RjA_Yy3o64rQ0wM4K6cMt0i_ObREDeTfhTMzEX89ejw_SuL1WrzCZY-ibm7IJ5baNdq_nKwPLQCLIYpTsjRpWnJj90qegPwfD9QeNmz7bcoTJ6qOWnVUPYhL0yusQH3X_yXPqnpaVton_ddhaY_DUaHhFY0WLm4SeVonM-itu9r0Gt4R8ypqoBI9WAyLQEApXcHnR_khO-AXQrogvEUoKE4v265htv2jemFVEUxrk94CCgVMVcpUTtV-FqWTjGF-a8xs_P-AYZcuadvUo6gKMlSZvjiRq6rmqIhMcxMVPqU33vHi0b3lbM4L3Tt9J7Vp7R3ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiyiSk0I57ifeoJBb8PfgxxVkMzJrW3XNDqU42nSk1FzE-JH2AgPa-rbll726vyG1apngvqBHIX-MauY4lO1uZiEkdiPYemecsmuyB2VHxSDW_N1mtDU-_o35go9lhbRuw4epzet-tcFeL-z0Uq65rBG_sAVVs-7BGNLgXJ7aEvJRNl9tU5nLGFIkBGCdTp2I94tI9gN_EKK44rKG8GqBafKGOwXxxM7S4x7tmtj3mfHOatElDmg1oWRqZpAKvuSwX4RAmPq_jgId6bdqu_jPwFWrORaHuQmUzRSiE_2A7VW2bMDCqN7PWvdJaBYsifZaYhZyll6XgwLjjcKMBFkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZlUdm5uNKQt2gl6mqKJ6WPOyUhMo_VThXUjWyd_XixiUs-l3waYN3pC2x2DvAb6PX0BNwuIL04C39GIFRgXB4p6DpYA0a8bqGS4sWt7ZmhTDVKCxJ6p_Qh8FSp_iYaZRRgsL99LBDIBO2_7hbrQzIKIVf394mmH2l5msbUbRdylYaE0K5HN7M5to_4kOaQKXP3_Lq-MqXRpi0TB_q0h1-1ZrN5lldJaBGYvwJa2yZhYfMPfEUxfjgkO_l8gQ8VsL9G7h1gQRYfQPFduYiMccrzaPjIJZn3bu9ne0wGUJznG2ARL0ICoyB16QJzyK-AudmMS2aWujileTLDSXuo8uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmhT0LttdECDjPxQgw8CbbI6zg2goavolpn3yzmdF-U3-s-0VjzN6zS1_B41vEyIbzTjOoIHL1MvmZaI3Eh-h-2y5h2mT3sG329CZ644S5duMXGNrnwL1k-4qP_rKeCNvw2X66a7HL8dhuMAv_XQWMDOoZboIPTcEI5g7_oThzwx4q3Utc9ZaKEGlu2SkFeo5MTNbF8YpaMFm0FHLzhkElSw13GxQ6LoFasPbuWXh6zjbxtnzwPjW7UECuykSsSSVVfVYT9DozTABlCH8BltL-ZZ-6tXLFIIuL7f1dWLOKvOiRQKLgcqaU1JZNYrWE6v5m7RJ9vKgcUxVVR8zwiZgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1au9A6Zxarb_ebi10YXfc4H8W_2LK5LaURoymGmEE561hRDwA8_pRkvdUQdD-KVHT0GsZkbJanXCnjn7UDo8uVoIJSKdfctKiNWEi1M0Pt3-OsBy_8uwQF_Aaaq-5n13RrlJSRS9NFh5zi1gY19c7Dd62XXdwQ5omHuCKoCNPN12cGESP2_-x6vXymxRQI_-oJjZadJIFFqCD_BLNzkjFHgwVa4WLMqD5GT5J_q31690c5s9ZdsZ4gMSicGU3hZGB6-CZYiEsmXCeKZwYqjCr29pvgvEMNE5gx95YBdJ-wmPLYFMWC6c2xU8tZ2ky7Acm6q05LjoELJsg3UE0CdDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r95KMqs1M4zj9B8uf-f3QAN4ZOt1M-wq3jtcp2nQybkNpoo5eTvnjRl1vGNYIpjLe29f5XPvQNaVaSw5hqsSZ_irmtOdFYU1U_C8jMceyPEl3TX-0JIRtpsNd1AhtbKsaaPDcIBM9got2rkpJZnJft3ZjliGkj-bzDu0qiqkhZN8spCTk1kz4cBExQPfs35cVnsQPnNrMVzArhtiUsTqyS5w1-TDnjck5awNOFaHe7gZ3jRiKtxpmVfXApTBlxHQO7lpwhkHxpgHkIxHbs2rrpwbcpfxpQESW_FL7IOBBbvMUNXohiJR7nRWQNGYBL7-AVHvxY0Yi9szhQ64ONY12w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaoWuD75gQXF_DgWA_kDa4Dc5at8e-XuaK7lQ4yGGlCa-niAmSlqaTPnAIbUuqx9E95lJcPoKv0meQZsuqwC-OlpAJwiDJUwB2wZEdcXEsXFnxug3MHLxUQK4YkHm2AXxZhgYAzdhpXMzJq5LX8SFd9p_I7-qgO-RLKjCh4yREn3-xmt9Tpg1wdOlF83W_bfo4ujmMQqMU1-eXDempRJyeQtiLoWiaz9nHkvNsTYsqIjlew4Byt9vPw3mdgDNVCPWtv_UOROWx9k9osvvNt-J2vg2vpfaNFgrrU0-xMccgl7MOByyOy14Y13RG3ncWNGvXca4sRQJDl-5QKpG3ZcqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ai9AqB7BPMvoTHdiAcJFFowFtE-ZSs3BCbe3QidcE9Jlbumtf2WkThlxQ3frte-pFv_577U3bAHr_QR29isXH_ERfc4qVeL8GmLLK__Kl4KikXGTVJgh6F1dz1zQCqeB9TQ-MCQKPVytK7t2YvXtf8Wzf5T0bC6fr9J5_RR166Cj2HLQ25mwclt_k69LcfiZbHWOtZ9OTjbsDGpE5sw4RZgLBelvnrmUUsEWVd0lfnilpmmWhRWjNjY_4zienPzgrS1mZqhRjk7cB1wTWLQp4tUwFMpbYBBQsgqEOFt8AsO9GkrA3JulZk_kTt0gKfdmSqMAh4sDe2r8bVv0ShjWLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIY8HX4eGWP4zbLmtEwDAgrG5SjexTFC39VJpj7cJ0iKM-aG1_s6cqgy-AXOeyyyLYOrWf7fGBeQcQjdt8XG5VGD4ofXpPHh2_kxUE0KrabmNPbHRT8gOs28Db92CNfcsSImYkSZVhWabi9-pLSibOzl_JY4lBHPmPul4uTjU3_k1vFxZ1SpOOmpdZPRTDWY2Z5YKH2JdADbrfzFbcyg1P2AdwzDCQtoUU3KnaDqSmBuLgK5x23y676TdGjN7MLqs_EcMQA0DNEHBIl6Z6GuAWe1MOQeBhqYYWjubjg5L8CIWiu6lzyI4CM3l2OqMQwhtNUXxw9v1jqKzcqbNcVC8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcSGi5Oz6OtUgv5lixU3uxjjr8FlHjUHGtj6StNXsbEyS0Bv_Q2LlvdGWzDHP0dBvf4c5fOAFcImaabM1Kbpp4wrjBnifXLUrfBm_rJ3Yeb4rXIGAZYTW0tkmWTQIt9GcJ6pR8pvcZO1HM_6iJEfEaDYZ1r3KabvxuQPXN_OlJRbuYSfu91TOGu2nRHEJ9TSRPkfpcz-kltTcHdJMem3yrZPUJ11MGlrtjp7702lOvbQpJLiz60IDqmUg_jhETy0Xa9RENGp5ZF8gNM1O8d_eUs4X6HNJ3UEiYCWtcJfswpD8GvcOxD04fKghUQ4UQm9H8SRp-zR6Egobig6kinv-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛ رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‼️
هایلایتی‌از عملکردخیره‌کننده لیونل‌مسی در بازی شب گذشته اینتزمیامی مقابل تورنتو در لیگ MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtZ3psoKnlzywFFgqO60QIqaeXVdzLXQTyyqHqIikpUyM7FxAYa6IxS26fI8EcD1uL54lQJNCK2QKEMBYus5Cnw1JJ1wUeECJ7fvqcowLc8alqu-GhMYogXxHQ6PUB1gZbXqC9H62N4zPEbbiEWfk0mJ8wU4KovBmeECpl_AAniUUyrE1RyB0FU8tFj5oKOrVVXYc9YBcoJD75mRuoe2lWK-Pp4pG25Iq0qvgs6K5sDkZRT-T65QWrP4Ch5SBV4bDh6qreTdpuJdt1j8fPSAnvh259Wgcvv0P3Sij-o_XwUQ2VgL4zQ669EvMWbyvJ49RxtvFQWsW3DQcuSS2qkuxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur9coMtI9zWasTi3DI9gmBCpvQTE21p1lFqR7YQtSLea32LPViQKDsab_nzGSp3CW0PFO_7slCpBK8VwjKKMSDNSoPvSZQkGaAI4BTha1kU7LwLHOwJcuW6-Z2BxNbpOpMUK4FRbRpdZDRRN_qJJWApJDUK4CXr-h1hJqRDYlkBecWsbT57nxirSZ0iwW4gUfCE-h1HMbjj4vwsnbRGg9AIQwUqqM9EhyCjXy9yY9h40sgKaZ3DMkzbKA4jnIAcNthjucHsvUD2YqkFchsCunSONGalvQoP5j4HfGyP2oM_BqRF4YQw3UqW-ppz_NkBgF-RdzDejcs8QypgWnB7fGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=u0NozkKsWchsdvBKP0-5PZGLtFwlRRwRZoYDBNWubKq37M_HiwmbVlYHmPkDhbJaKS8aK2UnzZgWyYlSwf1IniCzu-gaq6lgV3OYPOwV8dWEVV_kO92_iGSyptZXUEhKE4nWii8CHzsbqG6sxNpRyFs3cchZKM347EL_DU9GfeshMg0Y3aVkY9TMjXQWTP6cYo8r9sSiS686LM8CaToRPrrW2RF3YtIf5-zUkCEf9rO7KtvNl2aAXq7DNhWCFVDBLII3epfEvXICbLe213PVfeDALmvHVg7ga2XUhgylsFgzwTK-Wmpzb54kINGjwDV-2CwT1sxg2n0Xe3uk8oYC2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=u0NozkKsWchsdvBKP0-5PZGLtFwlRRwRZoYDBNWubKq37M_HiwmbVlYHmPkDhbJaKS8aK2UnzZgWyYlSwf1IniCzu-gaq6lgV3OYPOwV8dWEVV_kO92_iGSyptZXUEhKE4nWii8CHzsbqG6sxNpRyFs3cchZKM347EL_DU9GfeshMg0Y3aVkY9TMjXQWTP6cYo8r9sSiS686LM8CaToRPrrW2RF3YtIf5-zUkCEf9rO7KtvNl2aAXq7DNhWCFVDBLII3epfEvXICbLe213PVfeDALmvHVg7ga2XUhgylsFgzwTK-Wmpzb54kINGjwDV-2CwT1sxg2n0Xe3uk8oYC2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027
؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22069" target="_blank">📅 21:47 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22068">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1NVDHPNkb_aAVQf9J-tYGYXte1m2KdVMO5VcAaNAqkAZ9ssQ0U0bcTCOOo5GIgvQ_mK49GyVeTaiDDcRDgd26lrerit9wmZrFhfszxM-2RnnEQF_80nf7pOpqr-7-xQtGnzhkC7jryaOAKeyuYk-xqcrFaWuFsN1mNX7thRUBNvVK5bcO0W8BklEDqWs8jHrCCLUwVoVjWziLs9AVMU9nMraKZJFaaDv_WDPKkwZUbrZyxMuveqZYugjf_KydkebR6LfhY6UrVfZ6ZYLXpKjSFOZlQ_7_MQ-m37jX6kdhH1eJ-5ri59njDmffdSYsvg0qI7nDl43Cb-I8x7zan-lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049EgyorzsdrGAH0UQ6scYbGT3IHgamA5BQIDVE-5xJBWsnE0W3Vq0oz_Nl9pL2t3vv61ztIh9XwYpj-21BNXeppHQYZrS0xGrtyxg799NdgLTc8Wy03-jEbA-6ChvuaDYyqy5qxwpl7vd8fipZH1v0ZU7M0q4IWmlM4Xplj5qK6NPI2LprNinv5SDGQsGiv8-kp_A-X0cYvD_DFjqMZh6M0UvqvydiP5dovd-FTrQTxWj7652Bdv3I1xV9xaD9JTJSug1ckTKKHXfKwmv6DyMnbkqvBUj8m6JqalXEiTbButJHe78DnrD7uUs-Y9vA3hvzo4yuqxiXR0Ub2NCnXoBj1n9sa-I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049EgyorzsdrGAH0UQ6scYbGT3IHgamA5BQIDVE-5xJBWsnE0W3Vq0oz_Nl9pL2t3vv61ztIh9XwYpj-21BNXeppHQYZrS0xGrtyxg799NdgLTc8Wy03-jEbA-6ChvuaDYyqy5qxwpl7vd8fipZH1v0ZU7M0q4IWmlM4Xplj5qK6NPI2LprNinv5SDGQsGiv8-kp_A-X0cYvD_DFjqMZh6M0UvqvydiP5dovd-FTrQTxWj7652Bdv3I1xV9xaD9JTJSug1ckTKKHXfKwmv6DyMnbkqvBUj8m6JqalXEiTbButJHe78DnrD7uUs-Y9vA3hvzo4yuqxiXR0Ub2NCnXoBj1n9sa-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
از نبرد تماشایی روزهای گذشته فده والورده و شوامنی دو ستاره رئال مادرید رسما رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22066" target="_blank">📅 20:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22065">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNkfHaz7LP43Yw7CB3MmsFqb9QTSuQWwY-DzZ-8dpZWHu8QWipZcc9vjQo5rXKVCeowFrD3KejXxoeSBQM728qIxxvZpr6PLoq6VO0jDpvwNjws_q4JYxHcti7maM7LpRngChj5BHsG-sOU87txmOX-9h6MY6HZ7RiK6h5E0URzavpxDU33nJUswwpcblG0wnlwtCgXWHhG5kUHsLgaz4ZR-jSw752crCJXElVgJ-4G9AIau_jY_38eqkPQZDVI06CLgEbdxoPHGZQA9WXFqdyNHJ1LRLEEDyeOum4MA7BghCVwQZ0OgJUF09A2UElxevHVFhFku_gYm-1uiAesdjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و سپاهان در سطح دوم رقابت‌های لیگ قهرمانان آسیا حضور پیدا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22065" target="_blank">📅 19:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22064">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLqqiORBKwIW8UcchSTAF6axs_67xzz9dRwBYghXjFNBKWqdC1KQqkRlXImcfKII10UosW99l-AEQr10BdZZWnkwlQEGvmUlGcFi5h60k1xZTAcO1bJrkFvMKESNDYwrjz9qIaKkVHp30lLnqQaE7a-H8j8KrxJSKUy_t9Zz0MToPay3KwnK9dbxfoFSzK40fFBUBPiZKU6kQ7N1QZl33uKpUP42ZlqKGotue30nBsAGzLfWILRDTc5tE6hLucRh2dnoKlmFxsXqpTpXJdsiRZrTAisTpe8VZNwkzrrhYtrOI9ZBzQZlZeO4aff60H4HJFEPoLT7q6oy-lWgVoHoGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AefqgWectmzoHgH6p8VH9uHjHmog6S3Qipoxbjt7c-2NAXWpuT105hD0yqRk3cIOzEFhai6hNSxpiYfQL0I3DPa76fuGo4pNfBZc_cwYgEloPPil_8MqNZhge_NF5R6SkB5PLyM7DtOtePAdhWrhHFsNwZaGdQYcig4Gv8AShNbHvBUuRU5E47pDOamqiO3YCHU7eBAJYpIO6puQmDOQKP8p8VpdTFnynsQ90Feq8_8NMkpBzmBRC7g_fZXTo7KYukLCJ-Z73bBjxidGyXhWChxX2sGtlnB7w3TTjxh30ZR_xVluIlJA5KQcbFAvOA-gkjQQiVt36LFdn9BrAgr5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvbfAq94vqUp39zDbP9UIGIzfvjBF4irrZWxbQXtQW3059zHIQacgnO2A2lQZ_tTFSrCvsFPRD8Ac7KgnOv3HviUbFimrFNmPkV79DgozyiPDLwMY78PHoEoKfF5Du44rHPywtqwvciIuIb3rmUTSjHwWErXTCKgZNV5WlbnduCx8lR1FzVE6qZhZifBW-QKnATPRilxIFGSFMVqd9aZTot5D34h5ASnNs9l1SKBLfGDeFWAA4oNMW2-t7sw5_xDKVFPTn0QsM3mgOGIXP0zPvVOrmv7m212rPqco51GiIU9ikQnE2QQwpwPbpDJDBn1-WRDHt5bp5WCII0q8gvqXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpsN2QYgG2jiKdo56_1yHHdCh9MH-fMMpyepGA_cwC6cqaORW7rI2N577PLHdol4thTANuY8y0rN-mGXq3W7KbrkaVFgq9ZnVqd2FDzrWNfYJoKLfQAsvUZy2koW3aH3CWN89vdhJGOk7tQHUqJJ1xMnU7ADSMazHwHNod_N3SDKi84-r0GFRgj8WMJpEhR4VV-CT9Nwud_tsdKn2VEtXWqPDT5AxRJzetPjmcZyeWbcqJg8jqDXv4L3tio2Xius4kgpMKiDT3ytjTjAVWL3rVSzlnzKZX4PsZS4Odi6pJPk4gX9yl9fAsFPkbcoS72kgwsSinIQ90ES2PpyCB3MNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sr6w0Krq9ek6_K_Hza5WklrMcP5jpBAlzJhg8qrFnfNUVGFiACsKbesW3iLCF1bqZde6rU3-2g4OVOTOPCHJcn4KNyV765bwvcLwpB0-jq87h9rEtps9cv5QJqj1B-PxoluOeknvR9fG4QWoqjrtL9Mp3ycZlM4qPN7sxnBjYC5xHYnrzqTS5BeLZBBzm6GiJbBs2EfH_HpNUP3epwajOyqtsz4C8wasGo5TYx6DPv90BvO7t8W62LZn4VTnK4SYr7E41p2bHSYFQMD1Yui1Eue4o6H1RJwOIFiD2hSaz8MqK57FLVVjVq1oVrCp-BgvcsSpYn-3dOWaBvokrvwG6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برخلاف‌شایعات‌مطرح‌شده؛ مدیریت باشگاه پرسپولیس برنامه ای برای فروش اوستون اورونوف ستاره 25 ساله خود نداره و این بازی در جمع سرخ‌ پوشان ماندنیه. پیمان حدادی مدیرعامل سرخ قصد داره قرارداد اورونوف رو تا سال 2030 تمدید کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22059" target="_blank">📅 12:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAp8E37pcSGgvD4x1Af5AV7MCfsPsxjH6mHNFJUeG0DDUNGqrqhpoWxKtDE7_QqEM0wfXkYZCu19h7DgQU-T-l0c10GWOAmzQKLznARXPCLZWY1V1ZOtCEzY-uofvMQpvAbiV1hb8g6mHd64Zxly1xdsoKLxZB8sEwR9WsLxqf6SiNgqEzflwqJxW3jihoKK_ONuFXa2e1uB1OK_qg4qtQuswh7FuvnIxmm5Btsenm2q0WHa3RLLPCcHx3CybMwTQkANNiz-E_yBQh0vVwo4lvmMs54TXQ52uuF7JfbuIm0gfqv8_zWAc2cXBlS-5GA5vbmuVcEl_ZkRf4lp263nxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IV3vB0F9z49F4v5HyidrwaIl06DTW38V2tin1Pwf8wtfX32jBDSAIamsliidLzeKkGJvdE1BC_zX6CoUVBQN8M_VAZh--LWz7reNnRJCEs6y86XCoGCqlD-VOLSKMqnoBhoahuiLdtjtZO2k6kvGobUJcNlnAOJ2bZHcgJSRQt9M4mHeqZXBkqXk1W8ZDARvPQ8kGcFPAr6_bF7Joz84TBoKHq5Dli0DsIyd43aF1WpdiPP_iGBeResZ_8551vyAY8hQqWIKEagO_SWkR4yxHTtOseyB5wy9wdMeszP4Y_ePNMqDASpyvR0fr4j-xBp0P8MnfQB4zgcb8N3CGzFqIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
