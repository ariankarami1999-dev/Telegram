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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 23:41:53</div>
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
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlO2khZZOc-l2iN0Fw-AZOI0aO8Oe2DGzolcDsjnYXpdFXoUffAbKIaWIMhuTUAvsaPPuLAnjH-znG5nAVp54RgmYhZuknizGLBJ3xeKTxP2sjiVbWLrBzE7dtJYehyfsi3EmTPIh18oVbpso6Rw2kriinNM4MUpqX02YqnlD3nmo4zmjvJ_MoXLXyOPgvyS6iMfMrcThbO71qsM337aLR0-F_-fK5p99BlLoEKcPFWoVprqIBj59oOm7zPBkIW7JBA811kNM7H9a-hLyEEl723rTAVkucrU4oDDFPUfJkT9oeGLNRB2oyUnDqLx2UjlBL8ursJZhEsY1c-Hh0rqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJjtUfafxtWqO_zERdgESZKNKv28nx8pxdnML--EgH7pyy9Ml7brxsIye_3vFD1AOVOwCXgladLYoOXncX5wj4wSAsKkQzYJyvMIv3ByAjfBCrvrzPXIuFZT9QUXCHC3d3dGLYok1uSJaRwte7FFmXy3q1GWDPkjRW587G8rgkqIkMDAs-kuVCJ_lgoiCHJFSqgkrtMGIs_T7YuTcimZezOndeLI7d5rBzu7n33X2ri9gQ1YUVqxGqBYu377XnxitXCGCxa14iSPgiSIUhPmQtdG4opFILxpfYB8vYc00Mz0Vks0Na1lueHuui9DYkkpTEajTApEBOZTCihDUvDpHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/persiana_Soccer/22172" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7dLWrHg3zcsCQRVGlBaIRQlDEUZhlIXTZm22mwbknvXQ5XFLrubQzwIEbYCXf9F-7l5bfcrUqVPJCHuI3BPeDdzDUMnkkDoDlgKsGvkGbe3KO7RU4DSP7D5mNvBdZVlJ1SDFk0cCrFxBWFtI6oMFyx5lsuDoyikFdG--o5JJ7gUc06Vri4CpfqlbTx87llEls3FzfO6RbHDW_1T16GJmTDAgmvz4vbQgffuIMe7Vy91mDRJwjVARb1IHDaY3BRPWETtPKvtejVa4hV9c5b21xS0td7u2seTQBxEPxpLVCbd1_DWhA5JFQP3sVJV4lU1EoMxFuAY20k6JXh4Da4ZdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5cRdVuBCUAeEipfdJHH8X5_prW65t1BaeYNsNs4XrERQMY34DD8Z0ehbC5Dn91O5WNqn4edlrF8w0dVmnT6aCmgAR0i7wgKKAa2KuwzghH4JakY7fUVv-i_BQ-D5IsueZ95W9U3nb7vhCn22Fvky8yGT16VrlloSVpPm_-IM4nW6-NN4jhWihaLmiHMKQdY_bYt_lf9ddx3r3DSfWWEbpEA-iXJiH7LZoPaa8ZDTNg5HGZKKNaxRQMe0Agx66DvMfxi2xAbXBMySuoTY8r4OZUiJksLwrymaVGTTpRbj-gtsS7xQyFRrSy8J2s25FdLUE9S_C-F4QRtSvAl7sz2pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y900wnun-3-tv5y-Zb2J3PSH5fXG3N-7ItCe0uYTi6fW6wsGJIjrI0dBw411Kortg8qyx9LgDjvOari-FOjrj9kpITafdCWBEGaK9tdFFqMp6YJWfux8Fop_4UNbuhGNN2KBYYFPV83inS6fxqMfrlUOI13Xf41lk3kB5tgfVrsmUkLaG976Murf7Sfu0Gygxv4_UcAM9eJAJgCDgulj3rWO6SCghVt_m8CAHDycYuvgKuqYBGckObd8yIAd2BbEHCQ16dW4fgtdEMtFAHPgmxcGmZsb-c-cZfbfxUHiPPbAtLndg6abJwKT86JoAffba0YiRoqZ2H5eg-jPCivnRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22166" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdDwpnMygaEC1be6ROoVIDZnF0YwALys9ORTHoO2b97txD-HbMzIFqbbkg7UsyJbKHFwSposuykdOrKx3zFp0TejSQgipAbIl_VOx8lGE9dgU5yrYeMnl72qTME5VQtliLF3-jI7ZR4yvVHmUSUFe-g4Neye8fW-9RliAoTEDl167fIZ_xbl-0m2zECFbSRPY06aUN57OrLr2MwYkYUQ9oTuFcUt_m1LKVdXjT6eCBPGT9pq_ISXHn6bJuIg8pjYXwXTYQfTYxCeDpr4lPGjSuASardex_RYgjPEqX-zAMmrzwHi1fHEo6DZ8nAmQ4DhsWJjqAsxCosKrqOl72CEpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h33ZoQoSg0wVH2_Mz7DEPABRTWVFx6vsNf73h5bmqZbSsGIpCzoE_YC6WiUw7YIdyFwss5d_zCjJbsyOwiwg1FYUFx6WDyKYrEcI6sAsAHjq_AAcPY1r2EZ_2DTCAfSEq3lkzDU-bfKz9AKHxkVYFEUwj4LBXSG81JNxjDTQTSuzr3wttjQXvRNKSFJ6UsMhT9DErpQ2WUfeNkGaXMmsP_afR-JZIrxarHn64PTUlfBs5_bSiXq13JlpiGRmZXAoIRd5Uu5V86JYCJOXVbCjODqxxo_qRIBsa5yIkbDjUy5lZLVAW7r14MexEOXiI73kkdFHK_OqPE0i54bUNzZMaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5KCCMqoDYYzt_CFFa9lHMGaRTkG9LrhGV2P-hMuFgou5w6rBRWspi0exXtr0U4PYgQPiB6-zcr0IpjwfM5dTTSsC8wUK8yKU9Lfit5I-3ZFG26FSF6RkvdiHmb-Yy3CO9CxxFLjp9In0gzBRHbCO0KxaZL4I8BpsFY1GaRAi2FoFRDPEf24w1eJVWSstaDfZbRSx-CphltgayfK29eWxcpY8Ih304pnGriLsT75w8OH_EifuZ8y6mE_NqiSVfiVGuLb_2VnWmwTZNznJxSE43y-eIdKee09B0GPoN6Mr9Fc6O2fJjg4fC7q-PpjDC8K3qCapmr5_sSgGxjic52Jew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFK8N4wp8VGERj2ZoZempEFXbLKUrue9ESKN2Gz8ELtT9-Uw6fO3Gg3nE400SJDDfHzwVd6X7mJ-pNNJkoSU5YwPNZXN338WpKCrz26UELUJZdokF26pjEdWCFftmlgeipG88iuYZwvC_JW1cmktZa9nuJW7-kjbSRmnf8cuj2Q5zsSuDN0020AcA8JYus-Nih4225Bbgi_z-jseG9PwHWvJMkT5jFD6StwKCfbHxJogNZ9N1QENNiwoScu9IBXZwDKlzAJj-etw_4u4ll9VCp5sKT1lQAcOjl3XGbrmkw9P_2_14DIJlJOIbrPoLL2rvydQoQB1oiggSqHUIfyoXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6zhYLla02CaW9Z1kLzg7R-Wj-a1SQsaRugygVbixauW1oMjJuNDZbN0WedQC3FHb-u6J0dfyDO12WT2fr_Ml06o5k4zxfOLRjUlhsRlwsWz7f7riuFC7tMFJDcyCjVmLEFcaXzHDerCQXdSPkVVFxPmEXwBjrhR7IvRgyzzyuk9gl9UH5-vcAJ3UeDg20ObHsKUa1YevhjEE0_tfVDQXdWwemq2103uPXqRi70zfUW6pUyUCyRLzWNcuk0sPtEUWnYmKDUcMC9vHvkQT-HQ0hRnefoN-Pt51Ppd7FUQCIkY4DK1HoOLsxpybI7MxFDXZ0Kb8WTAxk8ZONMtTqwCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBkHqhLp2T-6MhyjtLZxHZFZbNBkB8X5UYoLZWXWaPUe0H4VjJ_iOAOSFmJXHRl0zXZ0XSyV36YHhhHyHccbNc3mTancajbP8KFivfuJAHuP1V1ppwUZpY_NpQxav1pbvGhTga7GrGcny2nNCDJeV1TLwIXGNljVwyV2jPYdnlfOz0dIRPYY7x1mT8nCN1NQVvUDvm2qHVF4UxEZk9U2v3NmF4v4BJRQTWrs9ikz7diDN_sU81c56LPL55UhG9Ccg0zTifTEWMG-deJPubXVudmrjOfze1orXpCLpPOz88dJimbyO9K43ZKov0yzdAGjNvXdxIuywX9jb33vtdaU2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sO_dRVmAntAUHYOkP3j8i9oA2dRp8Oa2KAY9f87Fn8h4a0yFLbLQ1s1nDMyLaFPSNc94mVxEzMM37tUfa4Nac_bX68eNLi_LNDk0Cj-W9mzd4DU_ubVq3d91Mw6opPogbTmQxET8dg3xTGqnc778sw_7GUn2PE6cHjuaJy7LBxDgT-vL5QtBzOOglklyR3uJSI7zRLONj4_rzrxtSZVlZi4mjBR981YJPkZfticsjU0QV5bkS5EcuYINOohAahWxmBKkfW-nf4gQbLdl2Di1nFzOxINPoyCZqcUFReDN8zlBfNuMhD_DgrU__GsG6S1OInv0Rb2ewSHS_t0TqwUGmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzfuEhJu5XQpgUjvBVLoynzWIBGbrVsQrYooYfSzwJnwG7pQx2gihvlZhzmtVypRblxgmN7uoN1UX3lWaTspXkkz9WX9KYvn4CXt6n0lldX_uswpSRmpUuFK-FOvQKFK5Ur69nIBlQJUkCnDhN6wOnjQi5MMqYUoJGZ1ufLL6j5aD7dZHJH2zzs-vr11VaTm6pjxJ3eCyOu-BvYUVG4VeWSqxxoR686NeZLoS8m8ISU15z9o5-kjVzbLWmsTFbMgeXHjrwtBYPBqzsZZxme5_Hdt78Xc7l-CkPv98adDJv7BgqyQQ5qOwtoU-4u4PMRTBJPN4AHDJa5wb4N8FT6aMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3bbSOpqj-nLMTBokswYax6--qXK0TJ778d-icenqZbUOwhXDaeeP4mM70bkrZ5XudGOn_nXcmd726FJbihOBS_IDuUny8XRjN_bfhbPfC8_C9LYylrSLHW6fQSsB68x80-n1ei43ZytP_Geqdh8-hGOCe7uaiLbELs94hww9wVH1dVpgEb8IN-AgvyRaieNndo3ts9nVfz0oLPsPL8Ul9VUXYiGvOoCkycUomrJ3hw5W-INmrzOl9QGyd3NuXzC7q7_rVX5LqOA7IRzQVNm2I5JiKeNWu_ZEGoA3Aisc9aKHdJ7OE7JQP3HenqO7KYG4XES_b4sN2G7oaU3vsIwbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs85gcZGTja5gPlErqCxzn7INQhzwwLbUa2_X2bSIq0Ptj5VceMLslfp3MGwHiR9_B1XwvFKFihXYpV8-dFduFc0QIt6iFsSNe3Ol70hDRJVeLnwUe1WUaZPMZHC1Dstpn1CDlygYivGj5SPJo0a3VnGReh24T8dtwfmhKuQE0RS8vI5xxtvCKlsc2Yv2bwlXJw7x8wKpdE_XtXWOvTTI8Kyqbqfnb3eROTvy3HPn7zwylJD-0p4fhD6TWiGFbh0b5dZhhZQ6Hj19apTff76GlX5xZdw7GRT9_MZpNZamRF53cJULd0GyHKIyPcKoHhUXjYThwf7vUvliSCvlzCQcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnLvaYkBzFmuYdd3G9QGu5eDpUyK5G5taElEByda9hkliRDvXW6VRM0rrD0Unn79MY04ITFZi8xn5iPUEQCG-_Zooo1YrJkfMEoW0SxR8Ij7kMMLOX4dDv02h6c4l8tPvLatnxwAeMrOWGPGvHklhRPEG15GCkA2dP9USXKMvcTWlLe6ksPPFoH3YE1nkGFOxE8iN6sI3kJ9ouPFjlXAR6fMOVtfTBVOwEco9anNcWYwMBvufpspDKR_kL_6Q2zrdx3gZYEuZMgjVDuAfA3aMydUD0-wHejV8vWpgvEw_qPrdSObDzINext7he5NEIkjF4K8bvLKmmnb6kDevDdrxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkEO6VJjQXeQfg-SqQAApL8gE2fSopR689GueAMiXKROV8mK25wtMiJU72bj42vCWehEitmn8WCCwD1G-qkacLBwiOpsvrV0Mfj8SNpZBbjAiaOyqmGdIoZSsDGDx-flmclZAe0yE8cqEZ3B4lAjc4lHFkoD9W8vEhn9QTd4aQoIuk75rn80CTCTxeIRHeVTLbxxSYXq1FFWZuiKNx3CKkzszOQgZkdkxMxPYxTknNUscbwoVl2S474_S9qZsLDZACqC3LAal5nQrDqcuRnGbikALqyFwDV9JMWasgO8MXLekYwu4DWTkNLzcWh7gy7TJf2QMT_nu3jt2Pe_DJf8Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSffepIyVb5xdL3OcyspcG_dI4N96leklNyxmVnpkYDkbVphZxYcW52FiptorSGQrQkIQbQP07p6xxZ7bf38nJlocfXB9WK25MtDCbQgxfIxCgFCkxsc70Ope29Hr3SrdhtDHP-AiLgv5MehedwWUSIiXXlwGT_LvDpOX-5QQs8x2XXrT_mLpT65L-fsjQj5TKZp-VN9vDsa7ZnKZEL2kLIncB6q1ipCWVTEPU4TRkX---y3v4N0GsgyKwEH6I4TrLe0q6ZAaka60cLDJK3oVFh_5YNwJqrfAz_Djz9FRdgrFjSi2szCpe7dQJKZH6JXCXtG1a0S_2-mTWBXW7ernQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XADtwV5eMpAz4dKnGR4aSJGTNTrHeVIxdj76U4YLZBJW2ZvU6wV8SC_sVQOQ09V5vEF_AelMYGUggyQyFSS8QsVuuJstmRx8lPlhHp-FL86i9BFd_e0alhWAnLWbv8KayBQSkEcYS3v7m2jyxr--ryTp7huf-nJ-ozBHHcmtkiqSVdkNePOF91NV2D1qKd6vrmEguedUuKB4lIvXJx6X-vhK9xFxx9Bjd_CzCiHSiySdcT0r3JIg39cZm3a0xHsf7v0OhzyinGXlVh5SkbXriA-l1QbCfZBe__KQT0PepzPMzS2vgz-KChGd-JD_lDOC_MwxmOUkgTH0TpCmvTDi5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fpd4wbofHwDKbUAP2Q1sBohjc1lZDBeGcsnmt3OoCKtg53SsZKXWxJ34MOyhTk5sd3NRj5py8fAb_Y4PxpsxeaatND2kQ_1yHfU6yrRNXr92TLXFozz8zz6o5wF7JUKDw56r3xKaHDmKBVPfqlGWAIIk37a_o8-9pMe6dpRNT5voMOSHeP_SdPCwwjdVSivVzHn224D9jaEwVx0VsT_uHCt3tHnvMiGEAbsrdlMJwO_rfuBV9CJGuhUAwbPArbL9kZn0MNkycvvrHTUabciVMQUAKgaiQuSet0CKdSftRKev-3dvcKH48qoxvZrSL-rEGdzfu4qEry-KdhEYb5om_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EidXvw_7SSbHFPKzQgzx9095aTnYqKPdDtEOOP2OURWhEG3FsZWuwUFjS_RCEOOpT6ttzO4_1w5jDoGz_ujqbG7yfbwLmwedEpVdMM0IhYKAeruoWbLbkCzIizSBssrfM1vzeSHHKuVAV4d4bVX5Vs5zKB-OZ7BPwM-tdZzsSpsuZqbYug_7ZaQnwUWA8JuSs3PYiU_MqUP4e9nBvhOMRAzcU3ShEhB01UBJgSOjGD91nHGXaHQI9swfdujrVjXm09Co3VOVjW_FuAgLHa4OQw2ZyOvo0TbMp5JqRQ4gikiB3T1jMU0phCOfEDS6SlQCLnvt0t1Vy9Itls2e5e_qUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZk64CRYwZEKMtNHZiyWfPP8OOfMkqkXwZkscdJjRifYQIMfBHf9-5WXdOrN7nQI1yvAAhQU-aD3A8J65hpun3BhpodfPTqM5aLKte3M191I0tOToL3sF-VRomK34UPjsUnE8bUWoTpXJqHrnfZtGRL5fb3S5yB6eQ4OBFGy4BqP-YaF61Y0dX-9EussrLyJ7U3wVUmH3zCLwkXXWfLjCEC5aSdqNIbeSei1PSoaEC436BapYmRJuMg7_0DqYhMkDIFuDjzxC-SEsE0M6F8votfz5xbK2OM8fTJk8ahUNpWdqM1OHUTOodTaR3cos56iMVh4Jc5PxmXjdthtP0Z0Jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmgcD6elAldgnp8eKI__5S-tlYDrURt7itXWKVo2rsISIMwEItFYCxTf2Ay5G8Xn_2Z262U3hH_QFblgW8OnZZnGesN6teuOKWlcDj2WbwJSz6JCB3nLcG_TQ9dOw1ScaRPyikNc1Zv3ous_d-xTIFOxnHVy5N81hJGHLttSovmt914cGBtkld3YI2_H-gbtB3fyc6ot0e_FMFF0yKb6hoip6But7Mv2C3exIKyMHvkeCoyr1rb0vxQjdQGqC-Pa0vYIT8KDF3zD-dJQE38aBBAOOKprCP-mgp6cy7QheMMpwwf012uNZLx510cArexyCsaWaxjYflLUhlGblis9kA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaqVUUHUBH2Ed4YRA4FoCfiopeU9O5xPWvCCG2EWxFs_QA8GISnxBlN81N4Q2mWk7P7nikhTPD-Gw22TIoisqfZ6K4gSp1gqV9yydjbIhQuRVnUo9WXbTWvEDF7NA4HFvUHvN5iPh9o5KxIOZ4QF6K4-4w5_1SYotZgGp1jLulx8XM3LDRBULpoTfpfsVaX5vfJrXBNZEebL0KJRZnjKPCSUdFiYkTPacIVPGLfjlIiA5ra5ngAdqCTOAQl8CMJbTzUwQINoBlcasBB1l5J59bn4sIv_rVqbQoGO35C9aL0i27w16ugGTRgu5BGSds3CjddAxuDtc0heYpLTXtzqyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ky7om-F0r0m9S3fx_iAzHkNdmv8PTt5icc_-4904yy0TbMWC9xlOltH3-VGQVpToIOPcXs_byJ1ydE_6X8IgvCCsMxu-nOsm4YCPSGKDlyENNPU22qnSWO-OjC8ATQL45GdvTrBpENumf07JBhPD8sHpblbg4QU0_a1VV9WzF05iSBO78K_aSAt__g15YkCXcEywbSd5FVvym_vug_qF0Lpf1SPMRL-HiesTwmDz8LV73tQzKBNu8PhAbMSYwOrQspmMd5kdDcy9jaRIjHJU2WdGN9fUPM5tN_r7QKP9NSwPzaQlDifIPn3hcZK4K2xFOAmfLoij7q7DG4Bv2ekdFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reoBFHaz2cOrtaR4Vd-q2lCktNBaE2uZB5T-V-qS-JS_1FC8zHAZfxfqQ-bU7x7oeAQzfUVZBQWSQjZVtVLbtU8-W9oV5S2ptPXQZmT06h-IRkuRhgfJOIRLt8D32_LOcVa0XCOjUB1yIwayqE8VMdQC6W043GyW0nKaeYDB1QtFWRmZjQxk7qWt6u_PFROuIhILEul7o3OkD3w2F4cbvZ6s_8GwKqJYQoFvYq7sWct2ftxhWxVhUNFXrKGNLOFz4lfyADRWg2ZsAe5CEMt8Ebf9ClHJr5I58HFf7wBIZMIKnz2bwrVWAafEjSUQo3aZiG38NJiS-tfN_KugyNqPlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmxwfc0sHK96IlkVbBZrnX9t_UjUXsZ5iPIXo8ybrQwRsKwKGx9Gz7mZxLIZnGnKlPFEwtlsHJf-QKYNZquu0CMcebZzFJT3WcX2EXQivtFBixFXrWR_7C9M4zP2313nzQapl0oa7etq0P275G232-yTPteWpReBWLSA8xlNgAATT7GdYvzFV5MxReAXci6rATtg6UPu1V_uuIsqDQ8YEEksmn6Uu6mskU-tJj2E71W_KEeeHHB8mWggB_Dy2PrdqCWOoqOity506rXmOF3R4IBtoxO0NyWwXt-3GCzreeGQYAy3AFSzgxWb4X6lkMw8vSEQM-afqA_w8G-Wetf39g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvD-BrQMCErWoLfCoGZUzknmYjnxqHpQ15lOi6XP4IjH6WV5ZFnYsj2N00nj0_F5ZJDh8XLpCKHDulnmZAqCvR-HbALqVx-OOiB3qTOp__5I3KV8_epMtOveBvZ9QHNJ4gI5ZhPjNIUoLZ3ZbXw74m95g3ZqYj3Snq8R9KRD9TgECdCJYUWGhkhnN9qPF3KImQ9aBcN7OZjHvTPRo2QrXN4N_Kt-tur3JbQKPmFZkt9m9iCLlpEUcDellIT8GXvcBlwUVwUg_s7PtQxpG1coSp91JmsgzJ31PELAXAyDY06JvdIA8b2eE8ismY1rLS-eBbyIR3G5PdrpgG3EYcpeeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rp_wI7ayiaegS_nct8v2AJRyijPyQ7xkXdu978moeUhLuEI2ZzfftlM8BWvaSghOiQV2bc_rKZUGcygvZNDuc2AoLl34C0PGywZoqo1RdGQNxkGvaTD7bMOACvJf8Iu1cxwgL-lh6tg_j1jkAmwZEyQ2WIKwzsS-06tzpbZlLo9zb6Ov3u7FBtJd4AzfhKJ9UBQAHKHHJ55e4WRJw9S-E3FLatN691V19iZ_J0jiVPKqhIHCo73pZBW1RUoxX1-TtT_cFtse5MLHgWd0APt95CzP26EX_wOnHIkylps6Y_gcAnCgakB6S1m_3O8njtFm2nzrna3SdcVw465EbGsSqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2V6Y85TfoLecNbKCGXGn8lmY9jphV6P1Kaw7SwPmkKol_1x1IkTcMKaN8NhEJWoSGPos6-MzTHawXwEXjApSR256bixdaO954CqA4G4-mYOapODHfP8vDzPYjssKi2FFlT7cHrZkpp20CScLMZMX-53msUhpEDyBtB3UDDvz4BOQ9xXXcJ2En_su9zwkLBuPkYcvLkAinZlKEPWHN0RCz8rTvrM8bJDj1BxrIbmTxPdu1cQgQPJdseYC6a0AEUzPXuQ9DY9Qb3hce6huiBoR5nlIhpWRJ0rNQguZ_9Rr2cxPDon24Zy4UjRUCP6D-GuF3gqTFCEapRiEbVWqI5MJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=ES9Rq7uy1aqM9p6hJgJ3mo7ezwvtoUvVzYdVBaMZGmVfjN4K4Yjyl6yXAqKMpORutUHUP0CEypA7Hjn8Dvemn3e1H9mPdXrpo5heC50KyMiPEzXtMvejliJsbe-9DVLACG4DzuhiQXp0ZcK4SbjxPvuENHC_kuWIy8brngE5yYF9u4Hbjx4iMI41p1sySNd1rbkERW5-i-8_hMRpOW15yth-a2k5-KLCoz4tOFmh-gzGlNMakWF5oZHvM1BYzGLN_fu8VHFELTchGqervjOUbkACx4yLLew9JTUbSVzzVwOFMK1EA_kOmoP7UbMu_c4-OByXdISJvdCgmUiZoP3ZOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=ES9Rq7uy1aqM9p6hJgJ3mo7ezwvtoUvVzYdVBaMZGmVfjN4K4Yjyl6yXAqKMpORutUHUP0CEypA7Hjn8Dvemn3e1H9mPdXrpo5heC50KyMiPEzXtMvejliJsbe-9DVLACG4DzuhiQXp0ZcK4SbjxPvuENHC_kuWIy8brngE5yYF9u4Hbjx4iMI41p1sySNd1rbkERW5-i-8_hMRpOW15yth-a2k5-KLCoz4tOFmh-gzGlNMakWF5oZHvM1BYzGLN_fu8VHFELTchGqervjOUbkACx4yLLew9JTUbSVzzVwOFMK1EA_kOmoP7UbMu_c4-OByXdISJvdCgmUiZoP3ZOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
👤
در شب درخشان لیونل مسی؛
پیروزی پرگل و ارزش مند اینترمیامی برابر سینسیناتی
اینترمیامی درشبی‌که‌مهمان‌سینسیناتی بود توانست با نتیجه 5-3 به پیروزی برسد. لیونل مسی در این دیدار موفق شد دو گل و 1 پاس گل به ثبت رساند تا نقش اول پیروزی تیمش باشد. با این عملکرد لیونل مسی به آمار 11 گل و 4 پاس‌گل در12 مسابقه فصل جدید ام ال اس رسید تا صدرنشین جدول اثرگذاری لیگ باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpR59nwtFbw4jML4GQ6dHutx-YdoM9mbNYz-eiw4HLdBK782SkeV6dwxqf1k7xsQSfyO4hptKCXGFJ-_vUyVm2MUgqTVUFvu4TckMrDiSKRg1b2_nmqbVQ2GyqJZP1mJI10CzVjBV5fGzPflO4rr5FfTcgk1A6MzRT8gq4IOOQFeJHijCvatF33DIsuKfpQVIaiIIPpBhEGgmFHs598SQYg8GkcmU4J-ERCx6rR-Yeg6sgp2sOKMNBy8VNTpt5RTej6JJXxNu6zNUmSTD_SWXeBMYm5__UrkFAYuymqBvkDYqW1y-86ROWAiwLKjA0aQfuLapgnsOLR0Zzmm28p_Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGMsvFdDbqbqaw-0OgVhgbhaSOTvbqnECTH-GFkVqlbnVMmTBkENk6D_IKmd0KorzFrIwHCLgcjdCL6f9Ck6Gt8RY-x0CLHu7Hgst8H7-YATnFUyvkPMU9pP5v8LC8dMUJlezHQALMZ9QCfdd1826k3gBNWFDHgUQywVQDiE7tXmEW1NeBiC-P7WvJWlN2NpEY3j5SftT7NnNxFPKYeaHlYQCklZxCllBUqzZ5qPXBzGyB8mWluQqHdPkV4SWB0GbCtqs10L7SIaJswY5zazoCYGl8LhXzUuuHLYiP8XqEH_YVjoVzJAbmJdevpuB_9XcID_02IVUjWIYrsJQ77Vzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtYqIPVXgkp_-L9V_mIzJskbM681IPlJhe5njykRA1a0ElDgxrcqmGUVMAjCyPbX-n-6elfIcT_VfceGGf3ejuX_yr_KO_S2TQ61iP7omP-ME82RSc0aThC3bpfmyilFH_90V4jRrDx4XlwZCO_A75iQnnKASnhs2GOegdTifdK5kM7NH3ecpfK01MBDroGoLM_0Zpz7xfnrZJqKdpFXF2RJE0bocKvAcFOcQ18XbkZuANeP9lQoum-4vP0Ez3P7RsnozcdeHQ03xlO5gCxLPOYUxSN4ElKFzM_d1I7wbW7p3Jk80-qpN02qRrJEAFiagoA75a5iOmO0u6Cf5zGMmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWATFJ0vCR-ayzVVwI-7zx84K9lGY7EToeuN5lQPpV7ZoMqo9q6hEBzEMuqy617sfSBcb2n4VeikOmFvOI1TC3cS-Jm3MM9pNZEi2tBLDHCPr-iXWJQtYSXORWwtyePLDBf_oDVraNFrAYXQzgZEMP9I2wrbmvtIMo1yk-aBFIztNn2snRLJ7pq27VLJuhfy7MABGejmroKKMcUuAMFK5-Uz22o9JmjAN_EBgSVOh29D6HxXrXQP5C2RuijsZoteqddWV92tsE_lB5a58YQxVBQYRw_OtQYbsrPD7YdAzHdKPN0NCyzqvu_kByACRAbhJImp8yd6naNEM-OdhQT86g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSJSrbFbwPi6cSkWXT6dW1GbvLCRlSvNuHQ7u2znpBc8pCLwRnSDQkH8k6h2q8tHecyNHLeUB-1WxFjDYWJU_CeV0jQ1V83Vxr2cRD5hTmaAp9E4L1RZBiQ17uAoJySQe5R8KNsHxPSZyL-MZ253mqfanlghjgS_MEBhQoF_Z_Z9mIvEGuv4XccNOL9VKPDZctSRu3gsRWj68HMmryNLZLvXiBNvkfjNbkDkqaSSqbdIgsio9YgWFFDfwwuFRsiIHF_Evb5jPqH_Sqv4mmR2jUulufawYOWrigIsoD1x3IhYCFiwJh0MzbfTU9xKweyrMJUh-T0qBJlfCRat6V-0Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkYENgJx3Go8c98Ulq9P9RYQamvbKqLFVoEZczx7Lb_vJNPbkKP5WMTtSwOgWTD2XuoiYxKf_atw9ClUoyIGUNaF_EXSvXNJhMFaK4K7qxy6ycYhzaE4O40aVTfNz9dKBTNEkXDU2uvWYe1Y65TbOty2czgmNVLlCgVfnNI1hJ6iORCI1jrq96BwSmfIkzXtwqNpFMFQ4wh2Hb3np5RkMe5fUG7xck6aD-vMLRYlRRozS2tdYnCX1UqsC95Qf2hS0Tls7gDv4_0_c6oBoEPg1PohjlBSp7L_hIQRMIQ0PngLru-5hLToalFYzoKPic24uuvrVRtmNG0Hu6gkvdSgAQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=MHf1W4_AZY_YaxpQMdZEX7oV2OKq3N52Laz_vkXPuW0C58Qbn5SKLZWtoMmCGq1z87aM35loyT1TAgk4621jtvsOsLyaSDRi57Xq2MFQlhgiL0CSzmEA_CE2bPPDpv5qHtLSY1NW_clmRlAT9nvIvAQBEe9eEV4uWL3AoMoa7aE6OYccL57mXQo1C1s5Kr7aXHUTHfD6J8aXOvj-JJQ6AOXIJ5l2no5Lzz2m5frCjt9go9oDnBrYrccWVpGKPcEC8hr2oLcS_9UKCBOpoqH5KtoBm9ehZQ2gaWSu_E5TOWkP7mL2sO1kt5D0Y9SzZbMhYXDJB1AREu6YNzmfIrYOow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=MHf1W4_AZY_YaxpQMdZEX7oV2OKq3N52Laz_vkXPuW0C58Qbn5SKLZWtoMmCGq1z87aM35loyT1TAgk4621jtvsOsLyaSDRi57Xq2MFQlhgiL0CSzmEA_CE2bPPDpv5qHtLSY1NW_clmRlAT9nvIvAQBEe9eEV4uWL3AoMoa7aE6OYccL57mXQo1C1s5Kr7aXHUTHfD6J8aXOvj-JJQ6AOXIJ5l2no5Lzz2m5frCjt9go9oDnBrYrccWVpGKPcEC8hr2oLcS_9UKCBOpoqH5KtoBm9ehZQ2gaWSu_E5TOWkP7mL2sO1kt5D0Y9SzZbMhYXDJB1AREu6YNzmfIrYOow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idmIMWBWVq2oZUzZKgL0YUqyEkylWhwxeYBI-Mod8e--dmm_r5Rwd-pMF0XvIH1x4erDAQ0F0-U2hTXJXe4p8zL6JZQSRO2ydFxiK9mHGEHu3umfYo4BxHgMEBHxCtWMO-UUVqIyEg9uKJNi1ynX_R6yr6JEobKwosocQif7xFiNp78azM26izsM9m9CaRWFG34i_uXilhavqbscPkeAqM1aEH5GTVvxXvZMj0H-N-u3C0tuyr7IkVepRG47Csm9dNeGCWVRYlrNzV76wQI9MekzVto3BHubryyxN58Hwkd7WOvT5R-hbFW0Vbtq6y97BmmHy5ISGf29HBeJbKE55A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEr1VRvKtZ2f13UuN1PVbKYExc98d7uAbdXhHHx6PrcHcOKnlPxMMskXhfaTOV1RcgqWPvM6V4YNa_x3ctl2zcmefslrJuaS0rosXXYSrgcfDlyx7q9hQaFy629aYAmeX4aCbuujUv77nlbr7y53AHn1ZlodRqx4gmgxHtMt0iRkhP08NZXexLCagzpyigIDscaQ2rYSlHJfqrrP_W2I0exrh_UU3sklmru2TLCEK9M1qyPiyC5ioPDWzW6gyukwZxxR5uhRkfLJnMP8fpI9G0-aqRUXVXbUcV6HsQD-b0FtEXqihZgu3Pi5KBevyx7-tnqyNQ_oU22DHT74zH690Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=rle9uMgEkQaXI6yLd2cxxuBEJUwez5pcq24_8LlNkkzUV1eFWHYgyagcL8BXxp6JtaFVZ3JxIzBwrf0x7qmPEnuyfNWB6gYwsdk1qvWKOTaHSR46sTmm2l86GOZ-eGFbjRLyou9avIAfNrBG62YYLnAch-pMaLxoXwAM81En_qOJufIX4BUPDkvJ3JfUL7xarKbia-stZ4pJhOLM54eSqCyBj3t3f2NDS3nIrJDA-hKK3NT7vyQ_bcAPCKP9Mr5ERYOgu5fAUIJJhTXlT7DGUaF1MFHP-WYIHymEqdHVMIxIVm2IYLy3dmfYEjEvHJx7gYkJqhaMLI9_iKSk1F-sdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=rle9uMgEkQaXI6yLd2cxxuBEJUwez5pcq24_8LlNkkzUV1eFWHYgyagcL8BXxp6JtaFVZ3JxIzBwrf0x7qmPEnuyfNWB6gYwsdk1qvWKOTaHSR46sTmm2l86GOZ-eGFbjRLyou9avIAfNrBG62YYLnAch-pMaLxoXwAM81En_qOJufIX4BUPDkvJ3JfUL7xarKbia-stZ4pJhOLM54eSqCyBj3t3f2NDS3nIrJDA-hKK3NT7vyQ_bcAPCKP9Mr5ERYOgu5fAUIJJhTXlT7DGUaF1MFHP-WYIHymEqdHVMIxIVm2IYLy3dmfYEjEvHJx7gYkJqhaMLI9_iKSk1F-sdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/alxFoUj-TRbpoTAZDJcnFILFl6aTDsJV6-mqdPmdyy-ztg0mwBfBYq49fHNOjDL_j7iC-k_TkP6WqqROkiU5227jsd6dhptpYhceAWXHB87gtX2S_lvqsmCp1MxAi6r_g7rD8ouaeEv1_BIq79paITw38qPHnei8i-IPR1HsOoAX6LvlqxZj1CUW8JuFOZCR_qVDFI_Ed76cuskIxIOJpuVe9GYAqD_TManQ0n5ENMgQoNvMPBsCdot0cZlDF-E8FkR534hpu7V-DNifwhyCHRLdOuAiAP-b90Uq7KhOKxcszoHsi81Ptkq0EnMDs65Ia0_wN_baEK4Ut0HEkJsWjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjzxnVxG8Jr0mkYrGkzicdwxWwG2qzGLgtqbxwnP5yJIPhJaYVAzT8BJ8Iv6Zh2QuxVKfdJfffboFsPlxmAbDj12nCFJTMHtDgx83MSFiDMsY-n5GFX0WOWDbeoO4R5qJnNnBTtbrRKqUYV9IdqhoTK8dUKARzkL4kfY-nz9mEaRsgH7wZKPfZfJapoWcz7wPfbiXr-rpZVUkGawGM_d4FtOa1iV7PV6apy4Ue4W_-98lfFYHHruInSrNlLY58I-FirckrGjIARJi2I6n-gUcwMU8xw9GFPeE_pVtvJ0EMDrOFaZNUH-kiVjfTDe1dTtYdZCnXUl-GIF2b7bou_lOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0hdYrw_YXI50rZg1ChArbzYtLke-dpK4zCwL-BM_tYFjkLFfsy_uPwIaNUCVJ6_hfGETriRvmZscVHbhBaQjlSr_QT9LvKBaHWz2SQ4tspSbeaz52dzZvaSiseUK6ycH1q-SrOL2sFNHMHd53m8_77xEC5m_YaVSvftdcoeyyuYU50DxVxom0VHoTXV5fbM4_p3b633U9eq83bcjhWzpctElLXXUyOwuG9bcI5xZesnhbTpfimmrH1zkpA-BT06CTc_slG33srcVDcLNjBpk2JrTVHc47QpN-Z0ZXFjxKRVuOCT8gV2pnrHbFsv2b2_nkH_FtWi1fOerx_5wIuGYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtlzbRCeSVqBpcUO090d6UeT8BIIVPnBfEtLp77FBSs5xq0_tbL7MF6OIW748SoA_6cYn_ToODlGhYBS_xXdiUF6rgN8_lWbPSSrTm50O_nshcwhETmnKwGGVBP6CpHv9IKnOJcZYKhld-n_8BFuHLk8Ic4ZbTmj3ZRbx9sTNcbMhYY8H9qkVc7mO4gO1_60DiwMzaZL08TgnwFRMOPMITNiV8w-svGq8yVAGbxGRep1gXMnHaApxVgkl5Z__FTWyyF5z-A6PErXi-ejRxNLnZH25YFxpISEwdAME3cfmDPBJi-vfrhIAw1fYIqdxJfCWXOZag1TFxdjz8PhVmA51w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1SbIilkW7j-cHfNaB5wykFsqjCbxplWuK-lspW950L8Nv_JLoGt-la95yEg51qgR_jMi7_2xrCoBLAVW2gcUOJVYIqxO8fobGaln9OiPerIcFrOBv1uODx5TBnYpY37vCDnLcQZCqz5hBsJXH32TqZomcmPDN__Rm_Gh7uUmibygkZdHS0L4G8si7-a-nLOCe5-H-MxEtjQmvAu12SWb-OWklf8Dkd4EoPPuaVzXNZXtk3M8BLeJemwGsPECkDVekZLxDJsUp_HUvMLPVdg4Bulm-Z64zZ8GgGTpoYPrEk7HmJO5Ev32i-5e43sIR_QSMU6C11p8B5qHXpLcqZR6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7jQdo59UVr9A26qUkd_HAGzXFVOU3KYmzboOJbOAfGUVEvJcB7LF0LWLztfGTg3G5fWW5Jv23NDQUywps3NH_V2Y1_IX7hJZ0IhrsMIXm45x0w7iO1yAg-Fmqi0nII1Td20LwemXG2BuJkZY55gQxEq_CGmQZoOKxEbg9UdUW2Bmnbr832PUi7_mkbme-q0gariO3j6fOIQDuTJvG5crCCDizD1gJ-Fv40e8Umxn9mvIyq7jsEFheoUcslBOrTcIJUbaBBFg7_hqdgaaRFevLc2DdWkO0N52z7ZyiOw8VvVdV0g8ftd2HB6F5xl-mm1R2LRAybE3g-O7Whvrl3Pmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EklCjzbSRq4lMfHUtE7_mU7nqaiE7JcT2L4-p9LhGisZGN0ljxAX3kI8z92Lj_KMp84Ko4r9oEezbw5H9ZcCtNUIMIxYFBvrCf-X8ttD5zaM0gLx1F6xvO8dQY0qvl5dOy7FckvQqIzB8xFhFOY-PZIBTIulTeA5Wwj5g8a82YMzMLovOEs0F3l5NTYVMjok02xEd2YLKNg66ZjWF1n-qahV3iecHeJnUeQbKX-DB4_2x88RkM2RffkIoeXo_-8dgDDaYqS4lr-dD2opJnZYcxf6MGEegiBmB51bFW4m-oNrD_Jb29UDG71q6PWOlg8x_Cu5F3uMsIq_65BlG1n0vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5k3wlW3mZCzphR9ln_zBkELNRlWebHPFpMlwbXnLXj8AFHk6D-jJIKhzBHPKt_8RKp1jpPJugRFeYRmysBkn9aqY1xoQPrDocc10VwaGDL89nRPb61SRjYXtYq6C7NeqRzdlNWx_1RTJFZOZhJbdrtBVOB6s5Sf5ZUxNLJLvyozyG3VilxjSBUteUlDcByrPMTR8DI6GdCCjch_hs8QpZgs6E2p9D-JXBlN_n4zj5N_R60ozf9yM1FZPASWTEI9fkpVtCik4mDWDQsYp-YGvc1BsUcVXJhGnS7TLJz5grS7EiOjDkNlcmCNy7mtIiCvsVSXCsopEx18DTxwcXDnmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dB-i-PZn8tNw8ui0PB1RW_5JduxNr8rfrElvKmwYdlbeZJXjzr1SEVue3QTNzitr1CA4VUuqsud5mevhnTimI-h1Yc54p1llw9f-AQb4Tcql7B18vldfQe9Me7ACNHQxmkShvrWPE686qmNJvQUhCPGMj4zCwjtX2nboBM5-gdnxQaFuIEAD71DNDTdMTL9xxhfNB5o23pKK1V70PFfEYhHWMXukXIrDWnzI1zMozXcDtAu0-mpfnmIF_OSZ2nJY0FVmAPRIcTArHpipTTwQhg2ElriuQAdaaLTosxUCaag9L4oS5PtCeQsuyzE_9toeMCC5sLl-9ScpmpnTvhY53w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRXEtavW3_FR8eV5SB4HRjipswMBrBQO_Yk1JG5k1ujmsxlz3_MM1oT2Zv_leXh8UaFoLF5Azlv-kqL3OXioQu4QFsZJhg57QfUUxHemoDp1vKsmSKXBC3zANjRGSa4xS9gzrI4GdUsdA3TPZAS2wwWuP-7n4yMe8VHHI2YyqBUuAzeH2ZvsK8YyejA_P3Xmob_Gr-atL6WiQmL2LHua_uZ3mvieGK1r-3RnZXD9yDLjrXTqtBoAaPsFYwCH5so2I6mNYvq19mdEcmLHX5yK78uy9hxTnnCZCTcRQn28figmjWmH0AUAirDuxIzBtLG_0hjrQ5taWJBMCRgrP3_2QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVi2MZqVJxywm4aDs8OjPvHFDYYTxtdnY4o8Mm4JxctOOKPmwiuB-HHTx4JhIOPwRXXvIjzrE8LLszvzm_bUe3hpftOujNqDNZjLyrzj_kVj_zNbVPblW9UUmrwsT5uBgOebYELF1RFvO_q7K4Mf9WBxoFfIyUp23O6zQujjrWMmxJLJmRIUfT6vSWbjwmND8qPtxXvYa83xkkDiOCI_6KhyvD9YOyn8S-WIjXRR5imoCZ10le4UbTEsOW8zSA7Tk0JYXa-0i-0R7ZoUW0Qxqs7a-mskwrd1zflirHSVUnYf1WBgc2RaYibQ5MyWLzCqmuaXQEm6aafp4zxskCaGRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=FucS5Yqiv-amzbQBWAvE-kgIfOXfDD6J605pFpkgq7GuqJPASAnNO1cMkN3A0yZm0vBvJ5orqqqnHD0FpiQ7fwvMcOWiyf2xs3JT69PIAikENiHadJC8PaTDCiIzHOfkmhFBEQsUEzLxr4hmDMmY6_OseKcIrPQcIu4m901zH0VPM2UH7PQxctXmdAn63kVzXtFQpW80Xd86kfRFdY8Qp2zGb5zrctwENf7mlOUtVV97tf_quZdyU7pXMkYanAj6AHpzHqx_jpbUwKa-rKI3-HJLZyGSH9beb1DbAoteN8WjPMJVHoT6-25ptpGYDa2mJXp6lg0so79bo605A5AfCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=FucS5Yqiv-amzbQBWAvE-kgIfOXfDD6J605pFpkgq7GuqJPASAnNO1cMkN3A0yZm0vBvJ5orqqqnHD0FpiQ7fwvMcOWiyf2xs3JT69PIAikENiHadJC8PaTDCiIzHOfkmhFBEQsUEzLxr4hmDMmY6_OseKcIrPQcIu4m901zH0VPM2UH7PQxctXmdAn63kVzXtFQpW80Xd86kfRFdY8Qp2zGb5zrctwENf7mlOUtVV97tf_quZdyU7pXMkYanAj6AHpzHqx_jpbUwKa-rKI3-HJLZyGSH9beb1DbAoteN8WjPMJVHoT6-25ptpGYDa2mJXp6lg0so79bo605A5AfCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVJkzGx6Sm_SdSheiPqsipnPsxtWWncZd6ZU5WDHf7-oC8CY6zFvVcxsuBitAAddArv0bIm5cxo_xGi2kXIXngPEde0hKV77YgKRSlkK9tkd6IGQWKPQO4efzKMQo6xMwoOeFvDfdYqU34W3oYLK8wBqcU9mirdnoDyOwb0SgHdM8fWvxHv4eSzgpvLeiiDig8GhUm9zYEg6C9eO7TWmvg61oTTJUWpxWrQ4j-hv4Rxj96pNjHaHaVcZAkLmV-EhKoP1asRC8BqJ6b9zIitD195VpVFREatsvODuW8cIW6_LTO9XKkzf7zhigR5ZZ90zTI-qovjN0Cv4Ov53IOfWGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARUSEvOktVBcjP6ImyPr8C0y1LZsrSCQ3af28n6T2iqZ5RF-SuKnpSsJ3QcX3ebdFbJwMCCoxG0Euo79SmmW-8KNQ6YBIIWwnaJcA-ZtHMxDHvP6Wa668PnYLjRsYA_WFMl0MzQJK9k_HomfAsy5sV3Y-6BBjOfJsxo2CAgFph2FrNuESiH_Xo1swFSTiKYmU5E9E6K-AkFwHP2SkklCV0eF4l0m-_PF5KN7aN6pp3I7aw9SFJD_IGmkYrAagRdMnM_ARh2nn1dy49kHKU-f8IaJ9yt8oXHAffVriXQafQsfSuv59hq7eF2edRuXhHIkQD-DHnyYs4b7Eh8Fj4APew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vul_9jcZr6o5WmcuXyi1K0r_uL0CBCk7urgwkOcHLpWz32xz6Isi9XZW3c7VMoFekL8YSxo6KKXiq7L3QjXbnFP_ktPWD_fzWgwO5XDfcOByI7D8W132MjIpW8HPcZSLYGkpsC_PXzwinLHWJ6gM0D82KnlSbe4kvmgEnBdvwAdX17eCsaB5tnUDqUzMgW-bqxwl7tgIuSrGSJf2rfW2hz4LeIUiCiu7F9NR_xjeZus8Qj2Jt_ICs4G_JJ64dKE7VLJGIg91EbFAbOko7N49PK6B928N6HIkryztaNTbrHHLjj4wA5k7cDJb7x28awC2kkVe81I-mKjeyvD0z49t-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfzpRguzY0cbAtTB7WjRpaGwpKsaBPKrFUPf73FLnIr9PiTUKmqV5e_qoPIioJu2D9KG7_pJnuyYkNSaavVlYg1ft90rpsnhZle7oJVNohWK-bvPNzl_HUEgLSCS4a4X162SClyNH90lNWVBhYhh3nKJvGISyNB2oE0K9yoGYl67-dXq20RyPUp7r2Tb4-v3yKuqCdpooFCtVz-8xKRjtlLPG4J0mTpA73C8kYEgQrLw2C35QPWdf0mdV0auM_f9Z6Mj3dKKaW_eDmsDmcMwtL6NsSybdA_O-g5N1oxg0uLEZzrXP1RDemkGZfTkBGZFkTQJnVbr1Ix_eVb67xvV6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_pjAmdRYHSsAlZzXcJCLSxtRyFj3-aZl3bAi7gjTvj-6DWvOpUD6lUUMCBlEqWamWNUUsoVNpfFiEs6PGtvUgfOSx8wyyVdk0scwNAwtYxEpiNZ77ovw1SpYppa7dKfNhNLOE4m6OmchypBkquQlkAztv0N1Hd7rn0-eZzKpN2TgFam1cMJu_998Q6lGG1uAjGt01MLS5_iLgiIKFa61IMhBMNUCCGEVuIRSXGM3dtni5P310nDiTgwQJXoZabdfg_muX192mUmjXUNxu-WeqCstH6M4jq1kD_Y4l2ncwAeOxQdSgQAd6vem4EFcJGnGlb5I66CcEciMs743k_OeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOm2jGwmoEsHmvZpgcvCYWxxxP2Yr7X-2zZm7v5iIfUNq9cWaSGZ2SieQ67qa9ZSdm-YYbu5eEMjFrajEZLVxKSYt3LrBuspT2zP67hIIt5gQujeOBbo8XBdt_vZvd4i-1EV12zveRErDihOcecFkYqKOeb7Oig9tq4FxGe0mjxOiUY2pYf9TJ9e__s6b20kRL00rW3qdv8wQpqE645Tz34viFfYWL13DmQPiqxU-hsLgxMNos2By-FL0uKMigDHicxZOX5gMEPdv5941B3Mzx2RfG4ACWYmhhHVPdskNZ46LLP08Dhg5RgaorU_65v1n8mt7HkQRaNBpdfRKeuasg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMMLN50iG24MMb3vLI0uGSl7tSqxrsWrXxz5U0Pb3GVaTAwne2RF2zu0fW1ZXI33b5rZ0CW2avloJ19QtpfcuNiv4TJgJqvLgzluycCNwYPunwJNP0Hcvz3CH5RZWBcyDVjda2-_KZSfvsxSo1ki0mU9XFHwaPve-Wig5tEk48Chk9PISYhmhn9KMQnbStX3r35hrDRzrAi_Lzy9ECHI3Zdg8gjGvB4vREcIYs8D-9wVj2Ds_TfqAclUij5aI-go3vtIi-w7LcyKM0io23lTBj53n3cgJGJkpx4Px3kYIpLx5MChycxh3AH6s2iv0_kjrDVZCekns_tLAiZnzvC74w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqZnLc0YYe4lxj4qd_-_SsrDsufRGzsaRQahxtWuxrUAj8pm4ZPcWj5OCXphjEnYtM0H9MbGIURe5jsSsUqotP4IiuZ2nWr0dYjqHdhse50ZE69FiTdRG79jekfoY8sAIZSWZYUKmQfvMjPMd-9qpjtNBOGQ3MrF0_CnR7QGcszPY6n29PjUK5J58fG2Ng-Cb3HxrFaWZzUbBKSlhY4LykpmNdDRK8rurGzH-Nbv1zni3tKbBRZu5vtmmuBYRY_MWTOFE2QWAyNztIl1BJkbbUjXHnnYwFAu0q8qtLdDDTMVOaaD_bx6Ph9EGFQ6eiMmZGmviZNvQIupxBTy6dDZdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUba-0TJrrC44D_7Aj64Qhck18xSt5HBoAECcYjuDHpPRqvSy5oPk1JXCA0CeQ7UYhMKUmx_zZTK_4z1mV2i397VlDWi0gtxl9VsR17VBVjylYzWfiIyqic35rfqTFx5pD08w_-Cvo0ke_Yls4WygOL7t0UEZxzI54rIf7BMIiXhe9xl1bXExGkI6Fw08hWzH-P1WC9wG6LVwjaqxYc0wd35M-RI2sWI50kqtX7aMWrzMM8J9eWJ-0vvkWkK57pH-IXTszC-7WLmk9xOJTjPD-GyiYUB-TIyCm7Miz1UE-nJKuB4neABdFJsuhkDI6o4kqt74Rz8Okxo7LlHxsegyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBDwxyzWzI4-pq00ZD2RIvD7rU17Suhd-Xa7ObMbIwgbcTsHaWOhrxoAlHH28bc2Z0UG7hdSGZdWNKvR0vQ--j2sgrtmG0DypJt2pnxojKVeepmKaCEjtI5JhBnYdYQjeykSaJqd9E1yuyajegRPWK9pcpMVw78usF7Z7HujYnW5IrE05r6iFZ8MTMFinb1ieIiwbOp06AU3mh9gE336sGR5AVw6PdWQCcZpc-E3GIE7q-b-jkAt9qZIpKGGUnCvOLo41sS_Qe-gZ3K75uwMACrnWKi-2qj67-Hshu110ShA47xF7Z7-vOJPD7Q0K8ECSyLqkzSbz4mHnudkoILCcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsAmktFZlag_47OJj19y4giQ0qT61f_DTdvgThAUCa9xBSKZJXDrWgo4ymZpMoYs2WcLO4L6CdLezH5cas_PpvJOb5kyJOQZFUTuVM03C84IkIwpdKR3J_Vus2G3dZbRoUrVApNLkZBdfE2VV-lK5VSJzyWOMaU31HTLw6Yv9c75xiGFsANbh8HP4Fm9m2w6mwbLTZpCQwJf4kL9Bil80oZuRCV_6UPNI2zMkL-0uq8VGj8F-e0WFXNUlYLaEKqM13HdmSiM4mIkOuG-e4DFFF5S_LBFyIV0kyUHZtmtaQ7Zjy4gqkKv8kLqYEyDRwdea0vdmCbdzAOUcgRSSPG-jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/It1dhR_Z9_UwU1_bKjX7NeDCR37yGpZCR8SsXbLYWYiqryDLk3UX_bxJAbUjYkWxvrJY_TGnAfCYHLJKAJ37mtDl4lqJo3Y1s8LV5dAMciJiQU7dSeAtoFMQtYazONiKFLZcf1gdfsI1Q6zrVYZYat11PKPMaw1NMgZzD8u1ey5TV4nlIQMUpxxpzGFaoqg8DgbxY2y6mYgCqe5jDY2gGt6wIBUW7EO0QwugCJWepE4OICEgUD0d6B9aenaS4qLCPFnOJxfe_7coyp694CQHp4425hD47nknttwACQwnvHL5rP3D8YVwFd9xN66QPPJ2aKSJrWfXYpWVTDCkfJtcyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkUGks9GfNDi3kIYNoFDPRpXBfpaUvV_9f0jY1XHrqcd-sXveKWjxygemW5RyA7lZgCa6fLNRpSsRz4yQB-nqU8VmhBV-6HW_GitEW2r_s5oiyIFH39XUwvVLm6Ru17ZoVL6tB7lKX4vE3nE906O3c9lzPr0bI4TyltZV1zoMS4bSbFKTQMbLO6cGvbHQ2uJmhDNIK0FI_1EwdeTUs64J-fyPZiT_fL-4sb7CHL_E00IwDHVHtsk4gabTBI5xN7YMwtW8IhmegKcykf_JwPwO3JWITQCNLJdkplnRynPLjND5a2-8cTEZK9PQzA_VbIhsRg5EVGQrRpa31XFAqNVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4s377CFdx0Y0Akvk2ge1yeCZMHGkLCn1nieiu6fwVN21ZA_L_lKx1opP9ifYfRyfjENVcRpV7yTMQLvyZcS8SHWSC1bNXFa_ByRQWjb-1mrKaCAw7n9_wY4ikgUMp96-I5G6pUpvytW7qhnOjkHsEC8KKFOvSZsEe-pDTaOE8vX0LrwhfB8-oV3I0HILUsisqhPJnDh4UeYc1InrreMJwcMnyfTz2YUILPKUPwjHagmT69Xb12aScLpb6G0g0iCH3T7bobPMyHkb5CYj6IDspOOvUxN7tB-rd8bOxkW75gZkxPiDv0wGYqNbcyun-mlhYTpGXJ-JKo-kCd8i_K3rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zu-8R2PG12JHLeO_3P2JRrpJJErYzn1__MlskPDEIvRejSI2XFklY_YI5ynXWZDG6jhnS8VmhInPh1fX-Wxu5QyI-j5nZBVnsM0NuohwS_pT7Z14VhQ5EOB8XNgnlydxe1p0Sgz1sRq843kZAxtwvrHTcpgZijEEQxoAezl12j_d4d5rV3dAhMsWQ0wrxvXJxYW-h9ms5XbBQXKH-4FhVowwUZgQ1HPFjI7GKWaGNa7aTQPUWQcSHpGabR7WJTaj27mJhiAGmDnDs9Usy4ymkVBJt1M4N11TGTayv-hoxQYQ48vT-yI9OUvq-ZfQ90HdrcgBtb6ZUoLKxyRkg6T03g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tf0MMriX_sQOm8rY-89PLKxc0Xv9q1L1-ilrwLfxySuUVUs9qnU7bpNhOQinIehhF-DFpbiNpTaHAPqrsue8BMTv13EtAkhR3CrGTq5Ue1Kd57Eswmc-_d0bdZEBsebIcf7Gwmft9Yb280WhipveMJgSt8vVfQ0prguPawJ-5Ekjk0KUTYUThsKF6hebDBPUzP6D9jUrYxQqdFmZCNL5_7T9hclCZ3Sefc01NnmxvZU4_rYV-tzk4CsHq0JfgDYNIU3m30j8bslZP5P1p4xihY0Va9bP2CH8AL6FAu0BXxVEWbMb5KFVRwQFHxiVL8Cym79YBTpHH9vLwtQo9uV_PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXaROVisfYdFH79021nfm7hIbkDMIVQNo4WbImDqXYFSPd2JRpnEwKY5LCKnVetyVzQzVVOhlhI_6mdlCvHoqy9BwrnTL_mXLy0--pA7gMJbU7jlirDK-5JMTdXbha2Hzb2E22l7H2wPBFVSyh7I9KJyXQou2npF5-HA6E9hI4yo6b3jNnpl3nnIJfYzcubHjJp_wDEZsXscPED_j6QvxuPLEu4Jfn9YRTuKHQipzxiIQpkr1KeyCVP4pdOVSEuRvkokNc5B0-wbB9vWDMS70ZdQKcSw_FYyvtIldGGhl1CHNsWdSaoL7Bt3h6e2vCxN8sFqlxVafaNbw4RKM92QBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i32jt3bwho73RLEOtmKC4739PUOfmOeCQ3Uu77eC8RC4fiUvrf8yDchb1dXsxf4JayC-fG0tRO1MTeZYar-p0JgCYEfZLPjO2y85wzNceuWR7snNt8N-Hiko3YmPT-MrgkAh36IohmgcRXyLBaCx-jY1zFQ5UmfTcf8SdDfURW1OBSn0PQAPk_CKCJ1NETlvrPSzCKpqLYXfepeEPfzbNIkUicX5oxsH2kVCvERX84zzc-2vWQyh-8tZjuzFG8uMHljl5SzQ5-ry_cT7oVlSQ0qC6cs5bzNVnYm19KIufzxp-wuxt3a2Yysp92NpQ4ESAayNoLkEZTYKpZdF60KtGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpuO6HHnNk02vxftyBWMaSVtUMPWJQjZ2Dt-ochsI0ZG7NEnwE28Nc_2TyXpTgE0KF9SuEgFa4XBcLjMC1UVXPuZD-BN1jbTYMg1cSOvf_ipEW0_ATGNw5kt021OYoz_avon82XuZni8Ngq7RfESf8O8gYmjcR4QiScd933bEyCq_btCJqs2MbFyaOKFgpw_xAoeMUgZNtW8UCQ-hb_i-k94E1nj_GuNLZWetDIu7MVe9pDJas99xw44EmmQv_C29k46kd_Ce6em4hwJQ7uj1xigw8XXTbIlpLgs80pgsYKZ4zg8U5pRca0M7YchKEfnQWNO2OI6aDg16LDF8VsnLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVmDRXAtelR1b6wlcXGvJU8lm5ZUe-VYbb8HxGr8wglvaLxZK8ZvREA_D1TTwIrZbL3cWzS_IzCZLCppX0q7HEPYQEtZuu9GbwdS_EHWG9ey4aW25ENVtWVu_fH7pxw_tHnxqqHz_FfKXUDqZ1a62mL_HzK2FE1-KH1cwPnzqBcv5DRtZ8uUmuz81WACvzj4j7AL3I-cy5qJKsjpciYPRuTCCARkRVpRYqTWo_0EsUWNxdQwWeK1DBukV4b8zOWMq2TInIyAu_GVTmB3Y3WubT9APSmylpVJeZoaM1B06XlQUtR93BW-V9jZlZEjd-jEMkQK8H7jlQz27Mu3HSwTWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z97v3Qrj6XwB9UxjQ1TfdtzVFAzdqYl14LzA0PWD8k3neeMZY9o_a4_w1LSd_cuczD0-ZickzHklGnYizWatS4IWdsiZmP8QrGjOHRUb7KzN3wiqPWl54hu7Tl4EuRL3q2LLg6HDlrM51-WvgXM0yEsgQQyGwM6NkxleSiEvj6mnjCb8Od1ZB7PxGLasiuTownDKlcQWeVbGwKyT7cn_Te8FpFLpYH8IuPUo_H0vaWxcEgvOdZbU5fecI_Lro3K9l4faL0-5K0ZG8UkmpsXHHC9xwjUrzoesD4BJPRSAgT-w6BThje9zG-FhgthKVSDAanzFGxDCBb2PKbkoJDvPtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgGrW8dh5XZ6ehVdntxoUfyBCUYsZAdD3BazrirlCzWcH_7vv9jv_7fUhd1HECUDe2ZjY_6erzc0Xr3wTNcMlfdR6iKVs6iKVTwMhbf5TnMlIbKWNTZsAPpUHizeaZyvGpJKvwWDwckXBpiypJ7h2MBr231vTOAUYQ-U6qPup0TlRIIIvgaqOK6CD3e4EzthYjppmrWJO8_zxgiGa8LkfmFNNNC-NTV-mukoBGDcF6GobuNtqScDMxKkdk56wups1IOYfYaERdFlLBVcllAChFqTs4sNbq-yM7bj_p8eJb40OZTkUtUzM-DI-w58x7S6DrWWxuwaVbYITjTFZaWBXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049Egyor0z-gRbxrLsORsnQuuD8vr1ow55GM313XysTwmde5OnS9Tr3Kq14_zgLCoggCZ38kfHFGIlRuUfun0DsX9ckoW9NG19jjoIRx3PJ8T_gUotmscO6yHbz0f35iBbNCIIsq1ZzmvKV8q6U5ME6mNULkSOg97Et17EEk5pi8mWBerqWmMPyqUolKaZs4YFUw7xQmzAk7NTps16VVLzmecIKjaXvGK1c3UubfsXLreMYjumiLcukXnWFj1Vn7ghok8rTPD5lWky0vaVTbEaU2UEOUsfH0pKg-jmuChoAFXPcz6p7HvQm6liEfrLspE-VnkPj_gV6cDuvwj0k8qq0tEHXxwc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049Egyor0z-gRbxrLsORsnQuuD8vr1ow55GM313XysTwmde5OnS9Tr3Kq14_zgLCoggCZ38kfHFGIlRuUfun0DsX9ckoW9NG19jjoIRx3PJ8T_gUotmscO6yHbz0f35iBbNCIIsq1ZzmvKV8q6U5ME6mNULkSOg97Et17EEk5pi8mWBerqWmMPyqUolKaZs4YFUw7xQmzAk7NTps16VVLzmecIKjaXvGK1c3UubfsXLreMYjumiLcukXnWFj1Vn7ghok8rTPD5lWky0vaVTbEaU2UEOUsfH0pKg-jmuChoAFXPcz6p7HvQm6liEfrLspE-VnkPj_gV6cDuvwj0k8qq0tEHXxwc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOPyULpKF3J13DHW1m90d4kJu749ts_Yc8b5Ng2F1jM0WDzbr-IB6wLj0U5Zqpusf2cRNH00GlBsydXGezSOgHI5Ne6uuJIrUSuNZlhzu7FhliyypYcFDelfXEtHglbgJbypdRjkvXy9ZvynnY7NktYkFyjZSrAeUcU8NBmS29zobV9BFFl4e_JwQJmK5_UrZ1Renm1imbATAOvtnLa-M-DZCx_znXhQ62RSjuVrva7XQom3HKJmURAlG2SUkH6IwMNoH638va7zQ5EVFzUb5BGTQ1PBgRNQfaa547J_aOq1OPmq0ACwBeTuQg72YMv0RyGIguBwbVVsYa2a3DHApQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ard0MkQiFfIFoZFpakwm8_x9tGcSjbSvkCDKxYOdQw-Yyi7RZ3KHkiCpN7uI9BwEwnsA_RnS802p89v79gONA02yRy1Bbp02mJkej29y0uBLZAOlA-wqUS0B7jNKSBO20a5R3lQOv63rLmcN1WH5fDTCM_VwSNAYqHP-zWTpZD-fk-AjlqajtV7oYpXrrBPg8M6j_QEf0NQfjnQeciNy6o-jvyz2R9EOxezBQiev3Ztc7pOOEC1UdbUxyLZodjvZfz7jao48DGrUHV8kiUGGYDL8iBAY9FurUXUyX0DdtyAhfK8KJWKP55nj1bVI1jWpNmZ5Dsou8G0pjc98KvqglQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqIxhCtTqqOdnzBmey1gu1KvpsFgNSRDIT3NgHAwtehzYOANFWucf4FFdLiDHi_8FANHbBn_0w208JWab-vht_rTCPfCJ6KkSqDjJr4v3xJBpW9j4AHKNZ8w1mI1CVreG8em56PaSMSA5yRDlGn4Dmo_NjWyzeLLEvH_d0znPwi06L53tN56rKObpGZEFjIe-48gluKpkRMa5y9nQWrLFBKCUTTN6D74JJJlrejw3U74SIOTchTBcQhmrc4q1u9EKTn5IRFcxuAclIiznWJPUQa4T8zweoOtN3v_mESUruiYsL5MCXfkqVdh6WZwpQUSXaJGW4t97-htBb6B5lYJ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBzFTgOsjiRTuZ31lbckKpCie29pCZkRnEe1t3EU6DQIy0a4KDuIgBWYVmPV9QBwgL100HK_6PeBD2ORQYCPCJF2MPWy8kIj0i2HtiL5sWfZ_eVUAeMKLgKGrS9kQX1Fu4H6omyo06tLKFamxLleT6WDE8yvxFS1PBzaOW-gUDUUUMDb-Vcf9t_hZKufRZU4jIISx5caRaII5DeKk6gfnrKwGSdwI_yap_pPGDSqACcZ8NRT1a96Sj3-mdAO4MlRdrtj4NTFftB8R9lK0OOuvlSWKLuSNKA--CDhVBS_DmNioVOmODDSpZD4OpW7E5s312HlCXa1xTieZBxUNE-rPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSwdc_bqYa0T8SYSyx4hr9elP8lVqajQGolIs0vUOAIpg-js-0VkSjAFwGYQJMc2xey1qoVhISucit8diK4d_x6zxsLS590YsGqimk3bTkvaUw5Gddm7JorZdA56ykLiRhUMqDwzfvzlum7jP3pZ9beiJCHR1BuJFvDjZ1NNI5-yIZZUkCnUFMSzsKNiTG1sQx_B3ztJ4NLfuDcX1OO9okl9_REDpwJA9yHhdZGWukcwO5dO1s0c-VXuUk_G1O3zD6jUfUL7hfH5RaXpQCOkBj-CMSZisEhEAFEMOA68lOj3x_I7DFtfOs2VjnRSKMP-TWSq4zDGotYG06SEnvMZ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsHQEC85l6rvtlEEMdseE5M_njxL8qmV38EiSHwu5uWRVhUsd_EBie_XctKFOi1pAFIUzwJUCJdochV5LGzj-TD2FxMfDIDV2snLzXyHax-OUXLipg8WHtCsuvv3TjSW75wUbhr-dNSA4Rzx2ecCO0EX-Cglr9tiv6K-q4Q8ToYH8OY_Da8WZrq1LKGKk_BqV0Deb0DC6gc9VlCu_mj27sMsKfecXxtbapJUMP7fKPaQtyISj01FNfSKwKXI52N1g2zY3YsooqP7t5KkL_6VV3OPqwpUtqN5nRdyfMI3YZq03343M-JPk9J10agkV1ghfgKV0qAwo9umUnyx5REQVA.jpg" alt="photo" loading="lazy"/></div>
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
