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
<img src="https://cdn4.telesco.pe/file/qPn1eu2yX4CRwEXIqF0Nho8BVCqZA5lOUCt4D6Bl6JuVx7K8VZ-oQmbupbP2NRtmb4x3VJkVToIYYJ_4zqjWg7qXKTKj62eFYIwzT4xe8BA89YC4VbdUN-kRrEW9A8W7BeGm-Mf9TTOBc7_da1rEzoC1Z0qGxZlCRxWBor5HLiBYl8Y0IH54ASCXoqWoQsxIsrByJ2kQ6ufOvStJ5mWtTQgLsKxyKhS_SRz38tKXelQHSXgt86ELAh52EWb56b8qRmbj2OD6HV35tJqxm6u81Mlz26k1RH0pIWH_Jokz39JipRUUCmnm2-vLJv1UAllzOjaQtgo9tDrruOuWCnqmuA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 206K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 10:30:24</div>
<hr>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvN73u2s4ctqoiKKh87APKEYe2GQcS-gSFFuo26yTMIccxYYEh5udQB0TKIfHoyQwLlX4VFnnMHfBLubOhZmC17vbd21m2NjrYCzjsd6X-igKISJr1-_yQFxI2IcLiaz-4vTTy5UqXKGzFMGO9EfccX_eh814J8jXyHDZYJbNZCqpR02XXEADBgp_rEBRdzT4E7ojJXrxBmJu3VYznxW1l7sAlhZ0iIDbYM1KUpV_ZqdsZIhizGs9NbE9hD2bhGve0NVFYQMdmy11Lotcm_gOgYpmCy0SL8itoPy6y-4EXYm2U3FO7bYt6G33OyosZ0Y192GK5L1Z6n58pWzkh-RGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXAshsE8iInYtW-J_WPZzEx21DTtFBBmobWVGjTLRLMPfzM8W7L0V5sU3l79QmhsB4sBZWjBP7hbTnzfc7qrbGLEaFtJPMQbC_culHJsITx6vZ_ztJ7jskDMrtdBjYoDm0e8xMK7QtArUFqh5YOoIrVnZ6nHYdwdENRtHPS6fNMi1vH-vnbXXZ4WFk6Vjr31GAEkYNU4YfZsMMYOQvBTdVRKrr9WOQZBFuEpSU3wDSLSUd4ORlz1SP8zLYE8Fwvto7DLihAAfUyuoc7k3KhxcQyBGeTNnWvJxnSWlizKjaLUILTU8EVaaB5wV0Nno8GAnvJlMwI4fPIU-0pf5vsZHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/persiana_Soccer/22180" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXhMoeQrNLHKdqiuHkhW2yuFpiyUMaagmQUkX217eNHFurgoTlwz-FPTztORdFHVhgA_LCrn-SN-qO-oxkmrpqUUQib9wKTW4R0uBZr6mBlbhyHz3o2Y1bYPFvBslffvRkJsnElkqbWA93CdxOcX69vqXkaPV5wvT5e1OPUcbEEkOxfNKHTAc4XFgYJS8hOtaHm_hwykpUsrAHAMm7qoMT8bbADmSbdSrUPY6YFzFU-oN_E84lB6cD1nwejF9vfmRFKwJjEhUWeRi4QSp0G7jOtRipBva7DCZ4_q__v4vZ_2MArocYVBzMQgjD9lYMZrmwDL8hh5FXVPlDKFpyESlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه جذاب افتخارات پپ گواردیولا و ژوزه مورینیو همراه با هزینه های هنگفت این دو سرمربی محبوب در پنجره های نقل و انتقالاتی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/persiana_Soccer/22179" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22178">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SD61Ju9DTEAoj0fOSr8TxnuEHM6DW_t5yGnVZ2n9WzkLCeK07wmyGPYX8IGy4gp23y--Ut49Zb9elO8kkpdtJ_6EXoF--_qcxP441YcnkH4-hFygdj8vEg6D7ktnuQIeFhFScdR6HSG7tQD0ETmYvcgf16RJeS4sTakLhWvVkOfc7joOvI5h6DNSAidLdFaWcuZS90QD8xMns07OtFCULwafaI9otbGoPruQSSbH3rIzPXWdPd6f8uFiXKo-als1PtQFBrW2i-gPLqAHb2BvoH4HylbuXtLv3sl8-I3qyUrwJBY5CcvKc2Sqj_C0r-dfbjqLOKQ4jK0mg6zLEC9qbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/persiana_Soccer/22178" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22175">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ovIAtYftyTF8ccrHqQCCG57x34XLARaDJj9Ed2rvOurCfwpC-wfcpdhI5udAMsMlOclEgB_MI4buwJNiqh1sO9g6XKR_qzHOJm31HPvhHct-t9chS7vdQShdbM_Jwwc-rc2IhMsHs78xV-fhEx6oFa2uvmgEuXDZmySkk8Z0YwFRNBf3IiZ9oSkFIRtAYZBH1RLdOhXo0OA4z_f5l-Maf0Z8WwXrc3f5xmvixAvroHcrDjkymgqVOhwaJ364sQ38OEA-Aa2LGMN11Juz7-tAjx13OLI1foiZTLHQUfhVt9n8bJcFePfGj2YEYrsOYFvtHw84qgwm4qTCK0o0FNYvMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tXgJ2dFO7YWO0OGjkwmrL7hgasvnWWTn1Oifb2Xb7n0IdozLthWkdo10MEWry4paY4uG5dJ_VZbN6nsyqhVATq1wVXtgL5XAj0m1Fl1NRO2RCbVkEKKANv7C8uU-gnfJWiME2PehJru3nOdd1IMAs4pRn_rZNgh6UCSxFcMRl3J-qvN0N6tS7f84GUXJZDaDsgqGiXGmBVnimjWKmvqqO2FwAx0spq6BHZyx5N9AxegmTyxhFTcQofeFKcruHPR55K8wVEiZidElBxErPfdYukeUEwzyx-WUhKNGc4TUzk0Swk9QPMgDKWkxPOGk8wTR0Q7YrBZjEIsd8dFEkkWTcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مهدی قایدی ستاره 27 ساله ایرانی سابق باشگاه استقلال در کنار پسرش میلان قایدی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlO2khZZOc-l2iN0Fw-AZOI0aO8Oe2DGzolcDsjnYXpdFXoUffAbKIaWIMhuTUAvsaPPuLAnjH-znG5nAVp54RgmYhZuknizGLBJ3xeKTxP2sjiVbWLrBzE7dtJYehyfsi3EmTPIh18oVbpso6Rw2kriinNM4MUpqX02YqnlD3nmo4zmjvJ_MoXLXyOPgvyS6iMfMrcThbO71qsM337aLR0-F_-fK5p99BlLoEKcPFWoVprqIBj59oOm7zPBkIW7JBA811kNM7H9a-hLyEEl723rTAVkucrU4oDDFPUfJkT9oeGLNRB2oyUnDqLx2UjlBL8ursJZhEsY1c-Hh0rqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJjtUfafxtWqO_zERdgESZKNKv28nx8pxdnML--EgH7pyy9Ml7brxsIye_3vFD1AOVOwCXgladLYoOXncX5wj4wSAsKkQzYJyvMIv3ByAjfBCrvrzPXIuFZT9QUXCHC3d3dGLYok1uSJaRwte7FFmXy3q1GWDPkjRW587G8rgkqIkMDAs-kuVCJ_lgoiCHJFSqgkrtMGIs_T7YuTcimZezOndeLI7d5rBzu7n33X2ri9gQ1YUVqxGqBYu377XnxitXCGCxa14iSPgiSIUhPmQtdG4opFILxpfYB8vYc00Mz0Vks0Na1lueHuui9DYkkpTEajTApEBOZTCihDUvDpHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22172">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/persiana_Soccer/22172" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7dLWrHg3zcsCQRVGlBaIRQlDEUZhlIXTZm22mwbknvXQ5XFLrubQzwIEbYCXf9F-7l5bfcrUqVPJCHuI3BPeDdzDUMnkkDoDlgKsGvkGbe3KO7RU4DSP7D5mNvBdZVlJ1SDFk0cCrFxBWFtI6oMFyx5lsuDoyikFdG--o5JJ7gUc06Vri4CpfqlbTx87llEls3FzfO6RbHDW_1T16GJmTDAgmvz4vbQgffuIMe7Vy91mDRJwjVARb1IHDaY3BRPWETtPKvtejVa4hV9c5b21xS0td7u2seTQBxEPxpLVCbd1_DWhA5JFQP3sVJV4lU1EoMxFuAY20k6JXh4Da4ZdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841076b140.mp4?token=DSFVYCFYmoHTE9flS0-f1hov7fVi8Oz9CcaFyLrZCz1MapplnUE2zRHqHKqdOVMjHveyYRVfPXURU-uB774WYrZ-HQvcC5T44qSeo3h-7yqI4DltwWPRu2_kSUTZeTcCRrpAka6KsuuEOwPKlMFiqxs8g7_ByJI61PebyBWfWjoS_4lFTMnVHMJQ2TIcZTERmLmkx8qtY-zLvAZan0eujvos_ZYFQLbSrVBHLUVqaxpUWMU33xBSfUtF4hLnOTxx46X5-d8wVSWdZ9czd2vpN0zfbbprL8M_D7gT3hTzz-qGjvIUP5OXgrMbXbR5HhVOzEUjrcLUpxDz9KTbk65snA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841076b140.mp4?token=DSFVYCFYmoHTE9flS0-f1hov7fVi8Oz9CcaFyLrZCz1MapplnUE2zRHqHKqdOVMjHveyYRVfPXURU-uB774WYrZ-HQvcC5T44qSeo3h-7yqI4DltwWPRu2_kSUTZeTcCRrpAka6KsuuEOwPKlMFiqxs8g7_ByJI61PebyBWfWjoS_4lFTMnVHMJQ2TIcZTERmLmkx8qtY-zLvAZan0eujvos_ZYFQLbSrVBHLUVqaxpUWMU33xBSfUtF4hLnOTxx46X5-d8wVSWdZ9czd2vpN0zfbbprL8M_D7gT3hTzz-qGjvIUP5OXgrMbXbR5HhVOzEUjrcLUpxDz9KTbk65snA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تقویم
؛ 13سال‌قبل‌درچنین‌روزی
؛ دیوید بکام آخرین بازی دوران حرفه‌ای خود را با پیراهن پاری‌سن‌ژرمن انجام داد و از مستطیل سبز خداحافظی کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=v8TP_Af7Zzhd0F1bsanMqlu4m4cem-j6PqZWsCZ6vNZXNC2qpN8DE3cp1O5m1yPAuvDISt6Juvsja8La8xtaeWF80Gttyyah4Vo0pkm7ZUJ8XpjlirNYNCFwjFG0UTMK39Z6C-0vCoDmmhcXw91OsC_vWBVZwx0fqp8iDwbnSJhrBiUXg8W5hBDdq-0DrEXrzpjrvKJ7a3HEGa5k6DAXTL_86t9ub_Kiv-c8Y_0LwnGysMWoxfUTpF0Ca7cUDmzC0lUCBZrEtQ17XWuQYaBAtuggJO08WUngc2PjwD69EYKxnLvwA-YPzODo1GJ9t-RNv0ivUcQBxgK4qonqSZ02kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=v8TP_Af7Zzhd0F1bsanMqlu4m4cem-j6PqZWsCZ6vNZXNC2qpN8DE3cp1O5m1yPAuvDISt6Juvsja8La8xtaeWF80Gttyyah4Vo0pkm7ZUJ8XpjlirNYNCFwjFG0UTMK39Z6C-0vCoDmmhcXw91OsC_vWBVZwx0fqp8iDwbnSJhrBiUXg8W5hBDdq-0DrEXrzpjrvKJ7a3HEGa5k6DAXTL_86t9ub_Kiv-c8Y_0LwnGysMWoxfUTpF0Ca7cUDmzC0lUCBZrEtQ17XWuQYaBAtuggJO08WUngc2PjwD69EYKxnLvwA-YPzODo1GJ9t-RNv0ivUcQBxgK4qonqSZ02kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
لئو مسی آرژانتینی در صدر بازیکنان با بیشترین تعداد بازی درادوار رقابت‌های جام جهانی در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Natb-_Ole7WksiKnrMvsRlRnOL35kvCuUYRb6mUvVFgu1a8zo1iKHmKVpiAuyoPZFD3wTIDTOz3ZzLk0kkNOyK7o-DJRmLjrk7kV9DVt7eBaY8KNB5holUTbKejNSiUbMhQw5q6rwoBN1-7UlcaeO9pyPLuEKegPDmVoH-i_hf7Ehwu9wfqiVRWRo6CPKUg9PZZQnyvPhJfbS9LwWNzq04dgBhhxrpSmL3kq96z6V9M7J1dgc9D9KuIqI29DOkSWTZCOCquE_euI5063KfG5Rb2o5VTbK0fP2MzjD5l9Q5vUyr1cavrwkHK42e8wP0yo2IfcxpK8Dv_hhWxUMhOH0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3vfeCOmkidRGknnx0NJGqFDfv4KMlGBYb4tTgn2XXop4DBk6vmGAHBaXDStS0SY_XheH5I9Tqc6PXR66LcFrQl5IwZK6AhhdEBMlO7Qzfylub2ocNaGqXwOUSjpDKpPOJQcEfPUdW1z-xKa1Wd7-W26E-vx8pTJjFNOqM91hZtRNK-BqfqTJTmsOkbHhd3uj4zfQ1FjSBtZ2BBl3M5E-fTWhrPQYXo1SQsWh3F-0lgOIbOtU0WyQRRPy2mF9l3HtXytvO9riVUs_2RCbxyOQojyCnt2QoXyZKHoB9nR_wuOCjINPhxbY_a_1oOdGjhG4ZacCBuC2KO5L9fMdthtlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHOApNytjJ3TU1eVvYc0g1F_sNDmsGMLpQZUbfOxXyuGeVMSes_ROYs77MUSPQV1T9lZGnAAafLz7IPs2wX69UhNPq-vVtKYgPHIp2KOZ4Bnd22RICkGsVKETFPfPX7_G6oyNq3pJC6DKoydaRYQZ_QUSMmIiuaMY9OPlsEVO6S58FbjpeP4m486XeTTxMB9rbjmzgVVlbOhanw4M3Kt_FeRLLe6xiBSCXu1_-JDoqDF584SSO0qBDndoe1ZoYKU4qiq8hSeVC48yX35vO7qbrdZTHLnfcT51LiDCA1iRUKw6ctjzqhfx-FyraiWrBVlp0wzUaPFv4QK658Naht0tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdDwpnMygaEC1be6ROoVIDZnF0YwALys9ORTHoO2b97txD-HbMzIFqbbkg7UsyJbKHFwSposuykdOrKx3zFp0TejSQgipAbIl_VOx8lGE9dgU5yrYeMnl72qTME5VQtliLF3-jI7ZR4yvVHmUSUFe-g4Neye8fW-9RliAoTEDl167fIZ_xbl-0m2zECFbSRPY06aUN57OrLr2MwYkYUQ9oTuFcUt_m1LKVdXjT6eCBPGT9pq_ISXHn6bJuIg8pjYXwXTYQfTYxCeDpr4lPGjSuASardex_RYgjPEqX-zAMmrzwHi1fHEo6DZ8nAmQ4DhsWJjqAsxCosKrqOl72CEpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h33ZoQoSg0wVH2_Mz7DEPABRTWVFx6vsNf73h5bmqZbSsGIpCzoE_YC6WiUw7YIdyFwss5d_zCjJbsyOwiwg1FYUFx6WDyKYrEcI6sAsAHjq_AAcPY1r2EZ_2DTCAfSEq3lkzDU-bfKz9AKHxkVYFEUwj4LBXSG81JNxjDTQTSuzr3wttjQXvRNKSFJ6UsMhT9DErpQ2WUfeNkGaXMmsP_afR-JZIrxarHn64PTUlfBs5_bSiXq13JlpiGRmZXAoIRd5Uu5V86JYCJOXVbCjODqxxo_qRIBsa5yIkbDjUy5lZLVAW7r14MexEOXiI73kkdFHK_OqPE0i54bUNzZMaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5KCCMqoDYYzt_CFFa9lHMGaRTkG9LrhGV2P-hMuFgou5w6rBRWspi0exXtr0U4PYgQPiB6-zcr0IpjwfM5dTTSsC8wUK8yKU9Lfit5I-3ZFG26FSF6RkvdiHmb-Yy3CO9CxxFLjp9In0gzBRHbCO0KxaZL4I8BpsFY1GaRAi2FoFRDPEf24w1eJVWSstaDfZbRSx-CphltgayfK29eWxcpY8Ih304pnGriLsT75w8OH_EifuZ8y6mE_NqiSVfiVGuLb_2VnWmwTZNznJxSE43y-eIdKee09B0GPoN6Mr9Fc6O2fJjg4fC7q-PpjDC8K3qCapmr5_sSgGxjic52Jew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFK8N4wp8VGERj2ZoZempEFXbLKUrue9ESKN2Gz8ELtT9-Uw6fO3Gg3nE400SJDDfHzwVd6X7mJ-pNNJkoSU5YwPNZXN338WpKCrz26UELUJZdokF26pjEdWCFftmlgeipG88iuYZwvC_JW1cmktZa9nuJW7-kjbSRmnf8cuj2Q5zsSuDN0020AcA8JYus-Nih4225Bbgi_z-jseG9PwHWvJMkT5jFD6StwKCfbHxJogNZ9N1QENNiwoScu9IBXZwDKlzAJj-etw_4u4ll9VCp5sKT1lQAcOjl3XGbrmkw9P_2_14DIJlJOIbrPoLL2rvydQoQB1oiggSqHUIfyoXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6zhYLla02CaW9Z1kLzg7R-Wj-a1SQsaRugygVbixauW1oMjJuNDZbN0WedQC3FHb-u6J0dfyDO12WT2fr_Ml06o5k4zxfOLRjUlhsRlwsWz7f7riuFC7tMFJDcyCjVmLEFcaXzHDerCQXdSPkVVFxPmEXwBjrhR7IvRgyzzyuk9gl9UH5-vcAJ3UeDg20ObHsKUa1YevhjEE0_tfVDQXdWwemq2103uPXqRi70zfUW6pUyUCyRLzWNcuk0sPtEUWnYmKDUcMC9vHvkQT-HQ0hRnefoN-Pt51Ppd7FUQCIkY4DK1HoOLsxpybI7MxFDXZ0Kb8WTAxk8ZONMtTqwCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rG-PlUV5T3LJWWk25U7Q_EIHrUyzPSzytAIRF2NsPNmzZJvUqWFIp6WCECRBt-pQvKuKuudDfOO-nTWEPOxiqOn5fnSkACSGNjSaxvRj3Jhh6GLnKqdWH2LzAUwbDoEsiKQLC11JsLT_1-WpQI8CWuT3DkX9O-hkKOh_tSQg3am9-8Ff9SVlg_sNxBc3QI-j3L3mBHWUHrUz1jG3TE0E_ZTf1kc2mWHgON0lnUsoHieNqfIUgKyHgnYqoGg-4T9xR1dXb1tyuLBxKUw5qRSBMVGQKUS191hAMIr8SLuMvYTpo9aPQ0EBdoIBrRUENXgaSFTOOkPC34YoieZ3QEmuaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEVRGhfzTlDVOXxFMKKTP5zVLEEgtB4WMsrjtcbRv-z79r_NGGRVwHRMqdrwjbgb0GbLrIcPL40UZd6NSeEhJBhXn9vx1TvwtwNnQdKGk2ME3PDp3kImqj6HmNatcMfia6IHNFt8vXxn1vpVNIgmJ4R0xMOibnO4vj65ZgsYiu6HXmJxhqoK25Ya8j6WdIDbivFBvBG9fTFzCBE9frXS-HQZz4oK6l9D5rCkdb3q1cz_0EA5iZZ9JuEllMfMk4i6iVaz28EbIO4XVFfRyO4xeCBRhB57MlmjsdhgT52-Ns5u6rte1STCxCS7LyIMZjfbg3NwBASYacXmntTdMG5c6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUnHHP9mRQefKIshSX3phsSNwMzT16ZqBKw1wctKHfWXtsRzaZ5HCIwR1C1il13FzNvn5DdwFtPIxnfjvVZAwQzUGFDmHoAb0A5JHqGxCASitXgv3hOLcTl4H5Nzx_lIQi8xwDhlKH0dWVUU7Zj09cRVNe79YCEDmwJFCZUSSprYNA5dR-fy09ZK1nSWOgTMDasrGhkrMt9Yn6fyiUUiPSQTqq2DOftiFESIPteS1NVw9a9ygg999IwnnJeUczipour2nlgbedcROogQY8NlEo4xSNufSbEXDMu_zMHJ2aeYJttDgZLwOg6CKg2fWuIkqxMw7kKuR64AtUCdu0xG6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3bbSOpqj-nLMTBokswYax6--qXK0TJ778d-icenqZbUOwhXDaeeP4mM70bkrZ5XudGOn_nXcmd726FJbihOBS_IDuUny8XRjN_bfhbPfC8_C9LYylrSLHW6fQSsB68x80-n1ei43ZytP_Geqdh8-hGOCe7uaiLbELs94hww9wVH1dVpgEb8IN-AgvyRaieNndo3ts9nVfz0oLPsPL8Ul9VUXYiGvOoCkycUomrJ3hw5W-INmrzOl9QGyd3NuXzC7q7_rVX5LqOA7IRzQVNm2I5JiKeNWu_ZEGoA3Aisc9aKHdJ7OE7JQP3HenqO7KYG4XES_b4sN2G7oaU3vsIwbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4FPDgYLARbKPAAkEe3KhphBH4SDiR1z6G3M9PTjRkOL1mVpQkH29RYjUeXIojb58tw-7dnaUJSuZTvXf_0bpL_CFfEYGK0mDjVJ7E712K_LRHhtAFzRAcHnZhXlpoNPTg0FZ7ttfYaxYMphVeDCL0PPCv1Fic-KMu0VKfIp4p_8AxXszXEvXKfO1q_G90MAwCKrP0ZOo9qlmSXN_ncgR_urj9BAkw133RoeQ07AiNYriWgM4CxnkMLflP50fdJVYHYxe9kevIZvjHXn5zVE3gLFRn9TOZpflzlVkwGUnT3YmuesMv7ZR-4fVldJkuMrTaNUqF7zm_jnAy2uiJjR0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUC_uU56s5JR9aKl_XcvYzgxdRe4pqe7iYa7ifTL9Wyp3yBPi-AcdH54oFRcYnqk_EA49l14g4ZDdvtmjaKrtP08zVan3z-8tBYdhdnj78SomI_q4h-VyRJzXaamc3uKLo2X2AzlhWYalvEd52OXN7MEBYt6t5MMttDD_zJk3ViysrI76HZ2XdwsI5g80ro8heRywNhmvKyAzB4E9u0n653eVCs2l6Aoc_laqOesbvttmlOoT2sgP8GFmA3TA3pfBkD1RctOS2iECc0Ew1sLH16W-vPI8LMzfrdauPq99KX0H64Zxz5hbYENmalaYC5pm43A4IawFpLOVXpSSVe-zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8b4AfBtLLOcbwGuBkSdCJ7SvbYMwVC4tOVHZNvoqeOlTL3KM6FdDa89Y7LQ4nTkbLQgINMEM3b1YmjeWGs9pp9Q3QwY6uNjSENe9gBYFI_PtRfH1MY2RUE2mJvyRhXykVRwT34xNplOffrQ2H_gogHTt4JgsiUS2DFAoLyO5GGPyns8mKEcwXE_cqKE58iLcfFnIg1WlTtO1EwBz1yzYlhZSbV05hqg2j4CtuuoYlyGsx84xd6lGtk_S97A1qDKH0a72vCCV1k1X6X2VxAdEPM3B2Wtw2kbZMtnefkA8-uEPx1s-hVMogCaAEiQdux7WCtf-JEnP67iHzyRsDZfJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIier6VcctQ6OfAtpc0OuB7PsiMnqRPqjvxx7NoCFOU235_E31uu3GOjDPLD6H6NfOSKjTuCXBOopDL8RMfOnBtIY6LGEYM3Bk8riKGz0a0iUlkaRBLJK87h1QYK_HFt4kQ-4de9oXjHOSMDJ2MOKsN8Ev5_2w-eGUxLTFBUpr1Rnd-Oklo3yco1wm18Fc4OcwwPD1CBYDzGrbHYpRwWbMWPGdxQgdHY5BPVwOAm68J8kFEEmcEYbEdpeVFMl0w1SYYZA0CcpHiSBbjjAUzZtz7LQIIMMIC2Ic-h40rPfhafn34vBmcNrOYqoVr-75QLb_3YAUYEFD2GITkcx5HgIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vx1Uom22_gByEtammqRJU5pqwqXl5MLWzlnkO2Ljau4zEy0I3NPT5UbKHiG8e5nYLdeDysZtgqM8hpdDXRah8_1upuj_eisv4KbSi4X9CbFA8Xwbr4bNzGizLs-0_iLq5bHAQy-6_v8j2T_45gRyXT4wtBGeKLzNAbjuUFXujh501GPaETA0yIuLxO5IO6gkqozXwEWr73irh1y92n0fEMGTQ-Uc24Dz7Xug8hUnreOXe7hhhKtcR-2DS_-7LYqxXW1ecVxQ9vE_SWuEBZ_5h64tIsylYEdaceOLsxyFiCfur5DtsTH7e_bXFLthEbHqzOKoOQxdoAtUUSbq324cdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fpd4wbofHwDKbUAP2Q1sBohjc1lZDBeGcsnmt3OoCKtg53SsZKXWxJ34MOyhTk5sd3NRj5py8fAb_Y4PxpsxeaatND2kQ_1yHfU6yrRNXr92TLXFozz8zz6o5wF7JUKDw56r3xKaHDmKBVPfqlGWAIIk37a_o8-9pMe6dpRNT5voMOSHeP_SdPCwwjdVSivVzHn224D9jaEwVx0VsT_uHCt3tHnvMiGEAbsrdlMJwO_rfuBV9CJGuhUAwbPArbL9kZn0MNkycvvrHTUabciVMQUAKgaiQuSet0CKdSftRKev-3dvcKH48qoxvZrSL-rEGdzfu4qEry-KdhEYb5om_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRZwbfS5XN8f-9oEz4P_nt5cLHoOtVn32kJlsaZ19WhoClrF7uCc9nkZoBXhEfknnd9tGoiDKwjgkgQkfUVJtCvvFnOpt3Ca9fm3NOJQkOynPVMfqZT7IUwMyyxlVyRw_VTStBKqQQelInKksVIyxhhOC7jYKS2-bGffEi_f3bkYhJZrKXyp8uQH_E1gcMyVeAHhCF9ys43eZGLYD-KHfL8MLnIeO4tSNe8GOpY6gnYRtqfPKjRf89ojL5mRQSXqoiNwDQpIlSDN56tqgN8C4Kz3vraU-6ecg7VdBrj2XYWePh6IIZ0iHcgo0_BkpN6-lpnPKW8R8qqn8o1l7raeHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkOhw5WsQjR2QLrgCDYy5QEBEV9Ag5iALA0X0friDD5Ls0kWd84pbyVJICWhPK7OxZPezmG0qc4I4D5ua95eRdZZDU4i5l1e6IgX-tsh5xZnBoqbTvekafnBGdIu1jN0aoC4myQX19RlzOKFmLk4fWbdbr3nPP1oNOBAER4raeSM1wOm5glhmu27eJVXRdJNMsAQPZoITll6dPWIMSHA4ULtqqV0x0WLsaNLHHlknnge7GXt2qZDWSEJFfSGCvhOrSXn6f6_tJ1XQ5OGfZPWWkDHD7-JVzJoGRskDPF_UvQjMDUL16T2qxngh15pQ6WE-r_mwpTWdFX1a-OJ40Wdsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQ5xplvV1h1r5ekWy4BZfc8zQl3BiVmz-bB_D2EHYQ--k5IRrD8yMAVuPQVuFitGQIqYFr4YWWgb--9w0DHof7D0PwvxN7sz8cX6BFwA2NMpo2VFu08G4UTnUoWhUTNvLrFRXhzqvAGAofBtsMhkVVlfm9R34ptah8TtczmSZzaabSPy79AseaCVZGEpcOFHOARXFMEqBELB2WAGlNNilQL8fvOK65vDt-JWS0eErIvZYTFEJrbWwTkRsmq_KlqWb3K9mWdIE9WVRkBT8RzTRqjTc1lo2Hnw47LeSCZyrLhKFnNZcInEplNh0NBqtfFiT50CSbCjlXdSzZxmKqhHfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh95hhdr-5LLrLBxcAmBBeXLbKKDs9y0vHYSspb6D3XEqXFGoPUeM3DpdqH89VVSMRWa1LiENYWfJQ2N2SFH7N35wYB7aAaLQZg3eQmZZCnS57Fdb28v732SMadfZEtQdxkjAzSNyhcrlWkE0FlQoBFaL7Ra2OoElPsB4kTII7Idj-y4TWoAvMgFEQMc4hoNWEZvBWc9ZIVIEpYD3la5tj5DgoJwMMq66PKqchQE8V0d-SPM3yfjj_kFSv-wmx01-L7bgoaL-Xnwg7GL6eLwz5PHXlwfjM2X40lQ_X4BTSpsAX2cvDyLCSAJ_LYHvnbmQwCWLFYLxKTq5DoayCIodw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pg0uXhkOhH6BwB8p8qQ0gD4M1UvxVKXOLqu4HeyrruPriXgu0_HhBQObOrU640SoIc6vlBHKKqBrMVfz3pzNb97jZgYsPgQGSvVUC7Qb3_LEZOkZrltmMQ8utIF0Y2GmaLwOk9WA_4q7vba_P4BTZmdGXQZKoSw_ziulHsyoycQl9wwxAg5zDGH5_TQizDy3xfcjREOs7ZiaFVO6jqQvDD2BTPxQNn8anL095Vyq8-a3oRGbFd5DPDgJc-Lgkh6wOGkQwPdEFqENziDpQra_zYtlymcGfEYas4m1Zvkm8HNPt90SdyYu88brukUOgf1UizY-wbkPT91RIL_PEaiL6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ve_1mJaWLQ5XOuHx2mk2soh1E4AOS1A3SDgzeZipuYzRkPGAXzeq51AP1Z7isf5hwwI0JPxMBW_DgeHNPsM9LX_g2zGYdyYQUBKQdixaxYrJsda0QPYpDbfGMmf90lVQO6AT5-dkXRI-g3N_xgMI1R_K7fwJPBHR3IGJHg6Zgj5SbS-VJiqJkUJZb1JVcsIgPNnGj1_7g8N2zgjNi43uzY3obF0djaChPtwG6o_chay-dLxv9-j3yJ8dNXm5dJz9nEVhBXPlRxJj9YwJYt_6hNoCOyh0Dy0WMlHVkL6WO53IFhRHuUs-ruMl3rq-5Il0xB9CaEFhACiBLF40-qDT6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvD-BrQMCErWoLfCoGZUzknmYjnxqHpQ15lOi6XP4IjH6WV5ZFnYsj2N00nj0_F5ZJDh8XLpCKHDulnmZAqCvR-HbALqVx-OOiB3qTOp__5I3KV8_epMtOveBvZ9QHNJ4gI5ZhPjNIUoLZ3ZbXw74m95g3ZqYj3Snq8R9KRD9TgECdCJYUWGhkhnN9qPF3KImQ9aBcN7OZjHvTPRo2QrXN4N_Kt-tur3JbQKPmFZkt9m9iCLlpEUcDellIT8GXvcBlwUVwUg_s7PtQxpG1coSp91JmsgzJ31PELAXAyDY06JvdIA8b2eE8ismY1rLS-eBbyIR3G5PdrpgG3EYcpeeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4rnsGHOXLA_ueajs5LmqmiB8pzoBRAaZY-xhkt4n5021G_213JFzIKDuZXU_F09seW4w8IpUUuGe4TMZk4eNwGropD9yDxRLd7sOp3NN4q1JgpS-JuON-7jdgs4bO3z9ta65xbQuSvGgOlIVKeamDsJrbtPGzwsJx4YdkR7-HxbeMOtm9XNSOPUChGGn8jv2H5jy9i_4JwYDansITtN8uBZb5oAQ5E1GBNB6cZqCnIYYwloy1lD7WJUusFjDwtIt6WW1cxaCHEqAWmJw14NCe6U58yI4Pd-iRK6XRvFjDnlFBdIiEwC8L43uecLAhuEXZA_LdA_A6h4nCxKNxW5cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lD04tsVTSQj-MGFwIEq_66kFLR8oLWelv_Xi4ixAzpdZUhQzWOLFetr8DpzyU3j21Hn8g5Mrw9KS7Kwm_Z5c8nttJTAMvn-jn3xY_-EgQXHdVdfRrE9_HkVaK8tAjgi_zSUKa9Ibjv5QyMjA-UFasy0incuGai_Ol-HOjBJuRot7ubQlTtUGNwX_6ujuEzqq8LSxSiJ5FgNnqMQQYKRmV7Q1cBywyiw0O2E7yoOWFPkAti5qKdcop8TMRZDiTIcnRcp_z9UgbwDJUiLAJWbWblzpiCNiOtrl0vWgoqiwUn6C89aosuwVCCTI3Bsx08e9v2royb4Jzn4SVWTBDNG0xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=pwpP8JpbCi90x0sXan3EwzZmsY1eZzcJJhZL3ifc6cSOGNl1Bo9F2ggewgZLyZoxSNN6Y3D6qg1-3gWENo1RbwglhmQS-W9QXLLDT3MOQEJ9c5SjVZEj7Ed3IaCI-bAfDtzdtVRXDUcYJVtEXhMgAkjgl8iL8hskc1Ivcvdhhi0afDWTBGcWsc3asB4KoFuSvgjQhbVGYsUeWoeG2RM42rpKJ5NdeoAcY5lNBJl8EpBpECsR2puu1kGzH4RfiCO_91Gxbk7dsK_hLRA_ucPr9uSXvEGO8ylVsKYNZFQdCO8B4Q5_b0gsOwy92zsrDB93qfaqfn9MOeXH_ZC9yA8HDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=pwpP8JpbCi90x0sXan3EwzZmsY1eZzcJJhZL3ifc6cSOGNl1Bo9F2ggewgZLyZoxSNN6Y3D6qg1-3gWENo1RbwglhmQS-W9QXLLDT3MOQEJ9c5SjVZEj7Ed3IaCI-bAfDtzdtVRXDUcYJVtEXhMgAkjgl8iL8hskc1Ivcvdhhi0afDWTBGcWsc3asB4KoFuSvgjQhbVGYsUeWoeG2RM42rpKJ5NdeoAcY5lNBJl8EpBpECsR2puu1kGzH4RfiCO_91Gxbk7dsK_hLRA_ucPr9uSXvEGO8ylVsKYNZFQdCO8B4Q5_b0gsOwy92zsrDB93qfaqfn9MOeXH_ZC9yA8HDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
👤
در شب درخشان لیونل مسی؛
پیروزی پرگل و ارزش مند اینترمیامی برابر سینسیناتی
اینترمیامی درشبی‌که‌مهمان‌سینسیناتی بود توانست با نتیجه 5-3 به پیروزی برسد. لیونل مسی در این دیدار موفق شد دو گل و 1 پاس گل به ثبت رساند تا نقش اول پیروزی تیمش باشد. با این عملکرد لیونل مسی به آمار 11 گل و 4 پاس‌گل در12 مسابقه فصل جدید ام ال اس رسید تا صدرنشین جدول اثرگذاری لیگ باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FS_MWvgEulWe4MjMGG0EZl6knXg8iV2NQE7eqqiF06VI8CsDwUGb3hFZtu8Hbco2IPCFTtodJLaVpssO-5soO2h0GEr8icVLaiekntiXNtP2QlfyC5FaYkqvDE2pEa5WrqftHYTfOFzXc4loNyVJLB0ow7CXCMCsqbIN3pEDhyYn72sEeV_bVVyD_c3XEJrGxysvvVhcGaa-B3ogw3sEvZ62xB1Lnp6vw7uWlhZ3YhZXv1IBcpO1hH7Q55VfVGA2t8OY5rWKQLglupCHAvFe2eTRLz9j1D8tTkDgH1-NV-bPjH3dyjgKZ3yXpxGlQXklMIv-en4fvTVTmQI4mHa7_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHs07TDWWPASXUcZa9dxxK_Ar1OuUapgh-DyplPyj6a10hjGIOjd_lTvSeSxAHXLLb3qNYQumT44SI03gCkrivLsq_RFqrIlVnQwH9t0-zH96aaOutUsGBUSZT5VXCG87AnVSE9CRQNYL3GVJNjZdIeVEf5UF77P6D7LcUuyj1AJ-eG2H2Oipe-FpfpfULGKe_cQJVYVxMv41aev-tuSGMW1--HGEUKjPRMIu5KJ35dR6pcBX0MIk8sx0VsNvm-a5yIF4n5y1k3p34NVg66hI8DG0OToF5WEV_DgIQLj7TwNdB2hMWVmidCkojCFIXNcqegfRSomt0mv_MUNB9V8jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0bIFlzFNmdO6qDohjI6LCOxJrHlUUYGbP6ZCBaZmjOvbdFkMmekX3SDp8B1Nuo55TZ9AUwv2enZpAkYb_qd96k9n7IYoiGei8sussDIa-bL_OcB2viXaaWguGOt10JgTMmtmbpyqXBrcFR-bm3zNwXZhe4CPb6WtLLd8I3Q_qUQhYTLcpir47w2kEJV-okAsSVMffdAJpi6EQHz3IRQunfNpJTcaDdcuIPtNvVyPYO98v_Qe9bFUIIuC6poqXf9xeyaQuW4ACihRtjjDX3Ojm8iIG6mfKUtR-JXmzdRrH5PyQK9ANdCkFFvNSg8nPBK2MlKuzir836XOT5EGIodVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUgCVz5gdSZKiV9zvbB4Mq9CxBBS09MzhMIpo-AifYcFl_vKfLNfKIo9oJAk0Hi6yXoCGFuHywNpSkKoLGDwB07HsRkE8XbLHj_GL1OFYXbeKJh9b5v9wQ9TrzXSah0XKPdRUpmSwjy6P9v-Bly4whZNGnfGcO0_iu-C9pdTkdBRNKkL_p_fdW84giEMnNJL3zgrTwUlECzMiwVyHSo_rWCjjqR7RFbPJw5NsG86D3p31t__4TsJ5ZIU13I__hAXPuwCIRohCOkPPJqLukZ5eoyKMzp2kw_LZODISpNDOWPm7o75XeiZyBH43dj5k_cVQ7ADn7jH2q-IdHmLd7EYGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8vBU57IP4-2XvkgKIYSLMJgHsD3Zm3Hlenpgz6QLTvNjeHXRdfRnxiwNXdT4R-5D8X8hrhNaBCn08sQnIUt4xnsFHfdEhbRuf5LcIuzw8wW0koImIJ7eKTOSgwF2HsOC2-hfk0neAHOS1i_KbGdds6Glxdai-05r77T-Sjz6mcrv0uM7hO4ukpn7uUSiqI1XLFXHBXt7Fq5NTdQpa65Mxd9Ya5oVz-zFV3VMHmFeUSxqtVWLiFjX7sO6gfQn7OhfNmc-k1ODGaM_D4Sx0STERyAY663TuC3rVl2nvbYBWc_pzD1d-DhI9xlAlljCQirdwz3qUIpCXw-iPOYKWq99Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPL3W43XkGJTiqXvTtfDAwZdgBUjfs2dgqU9dp3V5fJQOEYtCiRyQuDpBNWmFDxjKxR2dj2n7Lg-kbqoOoE7Q5QMBPhxTYEXKln9g2J5suvy0ADLiAgPtRoDebMerZ75dwnyxYacyl8ABt-a7nWsXKvKFX6guyntkUUuzrnaz9j6dBdYcPPVgVkQeNHnL5udo37El9LIo9mr_rYX5q3VHATX0_uayzjHYIop7QQlBi18FmVLg2V2R5oVo020wjfzRO5gaufJ7a_gk_VrK6UW55afhqAsAyErdnt1jfs_gooGDWQ-qUqE4v20oaXMjxtZ3pUdwZCCSbfcOeHuh9u5wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1B_6pYHJ4Uw8FR8z8_AT5MK7KQmvgSJnh1Ohyc7jhSUw1B-U1HGPnwO9OyiU23t7AHLvNvQefr3irNPLMX-RStk4ZYbsgzHMOOL3Iuk4d58DGyRTTJWTNiEhRDkwzCsNoHZ-KYUpIHETERC2R8zfA5rM7RSYJM-G7PNdTEpKDNc3M51B3Xy94AbxerGg2i_IVxFhW0Hc5wN22DPjrR_hAuO2b65R5mj8OhkBqWgdXDSxSjkc_7y2vplFLGbmbUrV8Xy7w7_qlunasvUeYO2gSQkNEPrJZ_4krsvyWAwTL4D-zF678Oz44wRkS6UGqmfajKSKjBtGteG7QzrXIz_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ou0Rip7REn5t2BLAAfcTgttI_eZIngJonrzG8-ngYkhZ5_V2L4WfWG6AdseDdA1I3hiGJIBGXlplQkRLgK9kbeYjOZt-NLo4IxuAyajFalo1Drf8jMX8yypWtBfVPtD1GZrVCdGg-T0_iAEuIves4pdacK_dbkNjoaPqcMg07-LRvZ6VOiE9eh9tRBCaVCM20q-9axtAY2ybux_CYerJONw7XzY_f-LKuJKR14cZE5GMRPPERKwNYzFz72rf3hzEUH7WJXNBp2Q7HWj9iwFmNLbhshvCAUa_Tk6v3D8U8D4uEml3B-Q4ltA9k1mVO5V0b0BeIEUlZzCtXF4irfK8Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=hIV73KfraRwZND7TdSZ1V2jnYx6DZkfIRJR0garAu0YTvKzcG8tCkrDbCCwjqLhlj7hqWEGuhe09zhQlBFAssyquye_nS7DkGzg9NVdQzyQb_-zL-SNEQhzvaxxMtZGfdczoQAGwvt8DVIuU5dWksKHlLe4-OXP5P2NG7vtMntKvbLIwXvtwQwCiiI66h8SP7-qhUyAHFJ5JMZVCDY0hc36-BZMMiv5Gw4pauzGtLOvQK3ZTGs1a4BN5s0sb6scwfGQyH4VvUCKvml8PdZhy7LTvnmw6zRcSViNemhXNd5yaCg02YqB9ZookVhF3oqAdNpUAJA50ht9HJLXx713BCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=hIV73KfraRwZND7TdSZ1V2jnYx6DZkfIRJR0garAu0YTvKzcG8tCkrDbCCwjqLhlj7hqWEGuhe09zhQlBFAssyquye_nS7DkGzg9NVdQzyQb_-zL-SNEQhzvaxxMtZGfdczoQAGwvt8DVIuU5dWksKHlLe4-OXP5P2NG7vtMntKvbLIwXvtwQwCiiI66h8SP7-qhUyAHFJ5JMZVCDY0hc36-BZMMiv5Gw4pauzGtLOvQK3ZTGs1a4BN5s0sb6scwfGQyH4VvUCKvml8PdZhy7LTvnmw6zRcSViNemhXNd5yaCg02YqB9ZookVhF3oqAdNpUAJA50ht9HJLXx713BCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaqVJNNwNB5MYAU5oRt5q_O5bzl8fGxupB1CW7MZT3_0J46aHwy4W_ngxaTiBHfeLNLaYchwZ0qMH_cCibqLpX3EabI9Udeh3ug6z84EH1IV_0suYoAn7xx98vh18fm7lMRGTmNjjYveZBtFuErMHYyfvD5qV6WDpJyy68rk6qvkGrlGRqAgt1-K1Ip4WILbXwoenP17RxEJoX0DqPgFyDeIC5JDHZWqL9d0N3bk2hut5p-dZLQ2Jida6O0d7rqS2Tsnq8Ohul9oDkvYKvwMFPVsQ1GNGaUyG-SvlmOEgn6VDosabLRk8PfBtLmle9GHVlfYUuLjprDPuJSMXX5uNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEr1VRvKtZ2f13UuN1PVbKYExc98d7uAbdXhHHx6PrcHcOKnlPxMMskXhfaTOV1RcgqWPvM6V4YNa_x3ctl2zcmefslrJuaS0rosXXYSrgcfDlyx7q9hQaFy629aYAmeX4aCbuujUv77nlbr7y53AHn1ZlodRqx4gmgxHtMt0iRkhP08NZXexLCagzpyigIDscaQ2rYSlHJfqrrP_W2I0exrh_UU3sklmru2TLCEK9M1qyPiyC5ioPDWzW6gyukwZxxR5uhRkfLJnMP8fpI9G0-aqRUXVXbUcV6HsQD-b0FtEXqihZgu3Pi5KBevyx7-tnqyNQ_oU22DHT74zH690Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=TXMtbjkCMrij3-rvcZ1C0qohXYvfx3tO_PqnJe0sQn8MW6k8vZ8efrOdX18c3QS7ao1xGwaw4rh6ZTk-CEsoWT-fjZY0kE7DU5S7j1ibPTlDbOWZcdHuNvZVWrROWfhC5Ursz1RcOCyGbKgri16drQThOJm_8906bps0nge49eigwtiovLm3ca3s320ILHXlCTFDIN8Q5plPO_JX4AD9GdK3btjN8f3osariapG29YIbANLxeOB0mQ_dC7Zv3H-_v4alMByk8AYryIaxLA6cj0j8PXmOep3vs_ZWXwpUSiPL58-f4YGm1NpR4zcpx6uuB50bhFsTwhvvOvNEdOGN3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=TXMtbjkCMrij3-rvcZ1C0qohXYvfx3tO_PqnJe0sQn8MW6k8vZ8efrOdX18c3QS7ao1xGwaw4rh6ZTk-CEsoWT-fjZY0kE7DU5S7j1ibPTlDbOWZcdHuNvZVWrROWfhC5Ursz1RcOCyGbKgri16drQThOJm_8906bps0nge49eigwtiovLm3ca3s320ILHXlCTFDIN8Q5plPO_JX4AD9GdK3btjN8f3osariapG29YIbANLxeOB0mQ_dC7Zv3H-_v4alMByk8AYryIaxLA6cj0j8PXmOep3vs_ZWXwpUSiPL58-f4YGm1NpR4zcpx6uuB50bhFsTwhvvOvNEdOGN3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGR-Q0q4eM_H1-iVp9AMQp8jJBn_tXH__sfaEDQnuM865hQw8rv8HNNB8vZRmbVzX9hfpicP6IcrNFUZNuO6gXdOjpnXBqtgKI7IQJlecgzO6FChopQvaJ7qn1_rAtZcjOn0ANRSHwKwLzOCjbLaUva7T2VYbP_IqneLwKQo8S9XVskuxL0VYUS7J2i3bbPUhVJTwmsrZbcFLfBY81jv9FM3ObkHaxSTgS4VCSo7a7ro-Y6_mStziEK-dqXLbT53Ano1QC3x-AqJjMshZWyiJV4WvVdwx7BT7_rbkgN3VEbF13JISvsq7C2sQ1FQpflRMtieo53e5BSxy-TAM3JKrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/SgmuSgfh5HqjqmySgmkPWtWo_DocmYLBsv9rtprFU5c7AKRPr4k3Z3b0hfyELaBZhCQfZRJO2ki9fHP1gL-Q5opTbtrcpkW-TGZDVVjwZvsVr1rEHToE-aqxaQPEyPGl7rx3RK4bZt0sYMpkqCK4MNJ1-VrTKKpzbJEY_fgZy_s-MGvZkyWvt_PRR-zMNx5tLfsL0BVEPNqBW_bRR3aPC1zwlD3NVjEto10JgXXq7S4LR9jwNAPCNH6A3CXm-KoyCxCtWJYpL15doD6vYgHuGb-XtWB28_P5GYNNWxsYqf0ul5l02DHzhFY7ZDa0khTDyv0QRNVaIAjmsS7YELw2Wg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZ1IUgDntZpG1_aAk_bWEf--VEUVWNWM_IVSgNP3846kXTMobcolYHGGsHzRltz3eJht0hv7IYHcinumCixhO53TisHSRC3UjS_l33R0vO2PrvhNhfnJRdfXHnrbLfaPfAzinltAcHZrUocTE9Z28H8BW6CHM8kY7USfPDj-evRUn9vOB9leuaJXRDo-LfiDbWmj8NY8xisRhBqXaIzFzySe7G7sSpantLmQKhGwflWyxCyilFZYhr4MBrx6Sr8uhAnn7doy-bgX-Z3z_jQgFxZbYgdt4rWxioRCIOJ42E0sk5CguFOKfrYqcWkdlcgNhXLOmpCdPQWIX4XN97jKuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0hdYrw_YXI50rZg1ChArbzYtLke-dpK4zCwL-BM_tYFjkLFfsy_uPwIaNUCVJ6_hfGETriRvmZscVHbhBaQjlSr_QT9LvKBaHWz2SQ4tspSbeaz52dzZvaSiseUK6ycH1q-SrOL2sFNHMHd53m8_77xEC5m_YaVSvftdcoeyyuYU50DxVxom0VHoTXV5fbM4_p3b633U9eq83bcjhWzpctElLXXUyOwuG9bcI5xZesnhbTpfimmrH1zkpA-BT06CTc_slG33srcVDcLNjBpk2JrTVHc47QpN-Z0ZXFjxKRVuOCT8gV2pnrHbFsv2b2_nkH_FtWi1fOerx_5wIuGYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtlzbRCeSVqBpcUO090d6UeT8BIIVPnBfEtLp77FBSs5xq0_tbL7MF6OIW748SoA_6cYn_ToODlGhYBS_xXdiUF6rgN8_lWbPSSrTm50O_nshcwhETmnKwGGVBP6CpHv9IKnOJcZYKhld-n_8BFuHLk8Ic4ZbTmj3ZRbx9sTNcbMhYY8H9qkVc7mO4gO1_60DiwMzaZL08TgnwFRMOPMITNiV8w-svGq8yVAGbxGRep1gXMnHaApxVgkl5Z__FTWyyF5z-A6PErXi-ejRxNLnZH25YFxpISEwdAME3cfmDPBJi-vfrhIAw1fYIqdxJfCWXOZag1TFxdjz8PhVmA51w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyNfEev1RfCflUPKn5Z4mWoJJ6Iysnf6PDmE7stN0gqLyyeI_jOeZnInEUmGTmbKRTwA-CS9m9BbgQTJnTjA5UEuA9dfp3zHW8udARifeetV1CRonI-6SG1Qk7aEAk7u7X4_vUMjjVXtkE1zYY5U0V4xqmKX86-0WftcaYEuYIRwBugKwLfDlfRM5St0PnMO0AjIyC0vE2KY0OU_7hLqSoGZzRiYm0McCLbfWf11h1jFjAvJgmNJnHcUtvjgx3t3rU9J4cQBuoOcOGtPZKaHpvYIYRhQ4xST8PreO8vKGcAYzF4upOfArW4eD4Bxltumx2km__fHyEdxrnucLCv6kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFGYO7OmLkKcFXvxr8MjGTx7U2XBk_ahu9DaJGlam7T2wY60AfD3IurNKFXGSyVrzXWwk5InaOTrRILSWSPYnuSN6c9tPh0ehtMK2ABmLUpZVTi7FyAf7HlTRmvSK-L1aT10cS-FNwnFDahZkQH5EeA8_16c0qDIVcT8unJZShS6y7slbHchdNCzOHx4ScDjYZ9oLq1_1ilj0BrVIumbNzl9CDLYtMQfHVJWG_Ox4GyVDcG16GnrKK34HU_PVq25NFGJj1WQjQ1WjFpNUzyYycWATkSzTFYdrulj_bMdB34BPRAiH8PuvHfNJgZYxGnwdr3MQ8_5Tg4K5XCs1SqG4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHE53y1U1SsSNJbanS2slFHsnAicJ2vWMd18WjhNUnaN32Hr6hDKe30XviowvRu_VkMlKCQX7NvRIoAbCu7F45OAsWCO1w5Z7yty1D41tMxN5Eu7s6SeCOC30VjFIkl5SuclV62NCbAaB_ooSPv9IQ_G03UvcIg5IG5YDeZqxlnn9MTX2KF9VKTPY1XKnSS10TSTECyTlkiiFdZ-zPFESYmjPiIEjaT39L7E2zEFPVRFy5FzrecDWGsOziJAQVKj4Oo9Vdlg4Tl6um9EVlETRGoacaUeT12Al7MNuhlzRQPNB7vQxSUTQHWXoyjQcNHYopCETwpHtSyo-JblefQLhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CngQSqiVQRlycN1502yjYFu8mh0OoA6_CaMe-yB8tiNUiUBxOCwMtfZXr-IoXRKTJVf-LMgA_EkIXPqQ4Kceog_I4QuMn7exZavug8ORIALd_hGtaW8VvJRhJAXxA_ziAG16Yfj8nFaXXQPLgLBNwT5IVkaMLR25twT2q0L9_c4wojrUYDzjAkDad5glXZVedgR0n2FUUvWbFOfspMUvmxxeg8aF42bgaDyabJGHOS6yYnBKNZG08o2Gi8cVLSY_BFeDKLQ4atD07VGaAXhAKQbtTHmyK1u5ivonbS3nHpFxw_gPu-VEtStQ7YAsSVO9bso-tzvfkFTyC__RN32w1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxMpIelSI1sWXmJLxShbEWnBpXTUHhYv7fAhBFnsO7cevj_u2XJn1Le-a4uxdK6NUteKWEpfo6dT_GpJAGLw98Uqd1XL7hoKd0AiRyVzixoDpFb3_-yZoA4ysdr-XsE5ysxq0eGfAZ92NzB2dTyWW4nAlHnEt3FPQn7FW3vNSBdXVVD1mLDXDyYAQkAmMxSGErx_-FDks-8iairY8MN2w9ma6VCUu7IsJbcHLz-XydxIY_7DiZDi27QNnl92vSLO-HcebHYNT-0Gvr6wTuAyadWJT3RpyYB4kt4yElHyCdXY3HHQ7xT6Lh-WXe1GEbdsM4G4GZEWzBSwoc6AlOZjuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjNSIRN4Jrwg4fLSOVHIqWQuoEFCQWZ1hwpaWWRWS3JAPPEUD202usc23Jj6HyQ3rqWs0hJEpafgsrf36zEjneWy3RTRaRXRrSGZXjgJ-YSj1czc6JfHCirvJ6ZuiSt9GD1a7M4zmhbwk1o3Zr66fhDw5Ipsw-OLXWQfgjCMvFq0-nQZWoC1ndxMEOHTNbdPLSIy91ILGutJeJaD0AhsdRpwL5Dy8YLizFlo6wTKkk2CGIKcUzL4t6ZJ8SDYB6PxAcvWF-Vp09Fgnhnsu6XWTQLa6i04Rhxegqh1Uk3VQpJUFtnfJowtsY_0zZg_NxQ2owkjxhXSCmaiHRzg2sEzSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7qXUJ4h42JpSYTaO59sW2XEmwbcVdojcQkTdDKD5xbIFZLA4NklY7T-zeZ6-eGBQ2mIo9v69jKbJVbIV5S55ICpXNq2vKspvXNHWO78nUKOHyoMpxajJ21xXKsXp6IzoRs954s1hjsSbgicC34pBoupHtYniapbpYie6UfNFmRmHo36hfxTh8jnDxgPj4Cym6vD8bjBMLB5CPEEgXZwitN6u5AhM4sJVachHxCloLK-wkr7d1X3wZ9lUfHDnIzGl76gOkBxi8OMtQzzZjjAzYnzzL35J4R744cTykvVtUeZgk5b7d_T0ugUe9l-zRKY5P1UmUdQnAWMWVf9KKOhCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9vsxh-Xk0FaZC_Fpmr7E7-wS_bnH_DCqCx5Nv8ZSvwsZCf3OsJufS0N0eHuDzzF8Y_JTpXHNu3-dgyGOmnt6VJWr_BTIeby-3RTBkPn5r8l20gFqn5sjvYa4Lx4hkTkJZJDGbiytdXMauzEMrz7Qjt8-yPKLsHqJBGPTWO1fH0xVuyLOWk365xeQr2WKEXq--sBWQ6B1FelLz97bpxtCi0Iln-D1VZRYJkrrXJovQIqYWTcph8o2Wme41z652sFgiN2Ltw3mCBcp7XRikfuzVPDDEP87yUo-WKQx65cJoFFzfah0zrAlHNOf4xfmo5bwsrPrbKGP1wUL9W5LJclJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5-rf4umkZgaR3DWNXo6uWD3qlriOg9PhVgVijUuK-WdnoWBY6f-dwQ2KYTuNWEaAQgp4WzVJEp40FJt13x-JBSPUMjjwbooHdjPnrQ2VAjQaxHfmWwtZkKWIZRppyHbDb2KY4hM-ebyA9jjwCrAgrlW_i4VVXQKX5OC9QTa2xeLVVRFtVgrrWFvbllpzcVQ1PSQd0AxBqooA8kCwUopmz60OI3pFfPm9SIJjoyF9-UKSkjKjURKKn_OZy38ifzcet2BfR9KZoMuO6JhMw4fyjZDgHkyFf8705jJm5AouAGW8NYliek1qIKEZe7q-5BN-sipNEWt070BTkGXBYbMbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=tNT0sbMq39kW-IZes12gPkHuohG2CEa1CdKmdtSqbcoTWS8R2rXvAGA1ZbPlB9Ml3An1va8V3Kzx3Kxd-sKwqZNMw31p_OTsfEjnUrPuLSWjqjOe8lHVJ0Muo3ZoAy6AwxIvsL1FOoqBQHkF865wt3eDXeJ1u4__TGRS3RAQ2d5VNZ_tbLPJ59LhOFa7ixtD3OXFeC4DHaNREHW9R-EdQaUrTtXPQMta2qSv5cnd8nCyrpVHX-eCDPbzSZahM16_rlxN1Pqn9CgZF8H7KX60o5y65tyJdPqNUscozPIFNakaHtT6egjITPvOFCJiEtJleLh9YbrfG009D5CkDP6oFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=tNT0sbMq39kW-IZes12gPkHuohG2CEa1CdKmdtSqbcoTWS8R2rXvAGA1ZbPlB9Ml3An1va8V3Kzx3Kxd-sKwqZNMw31p_OTsfEjnUrPuLSWjqjOe8lHVJ0Muo3ZoAy6AwxIvsL1FOoqBQHkF865wt3eDXeJ1u4__TGRS3RAQ2d5VNZ_tbLPJ59LhOFa7ixtD3OXFeC4DHaNREHW9R-EdQaUrTtXPQMta2qSv5cnd8nCyrpVHX-eCDPbzSZahM16_rlxN1Pqn9CgZF8H7KX60o5y65tyJdPqNUscozPIFNakaHtT6egjITPvOFCJiEtJleLh9YbrfG009D5CkDP6oFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-jUWG844sKsytAUEvlE2O-qSwtsz8lqCCcpXb9QimYAUs_hyX-s5L65N4ZSrqE15nadHIBj5GCxS-07EqQZylG2uuPbPTwT2sCeT5avTLz5LoBZRhod2eKoJXr6a-0m3kbYZvAOK4GFNHs7ppK0l5cuEpa9uEV0K-oBGJ9mIGxfCLOhzBzI-x1bXqN3s17udXJLwFAuyf468ARKhJ49frqPJkjgtCD53CEchAgU6r3BRbifkkuB4jeC6FenHTzSLnpwZ4L6_iNlafaV2RFAo0MVRMFxohRbO5MIEIUZk4m-ssblmSt1ncPpxvXKA1rK0fSe39lbXXGoU7z2XYe7Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l10RG7Y-gaNfGQAiHt7148AUmu3bzkDjzW6vJWQ4F_bQRFl94zyAhe6u3kjWigzR_oPN83VaODm1K2tDGsAFf8Fu6LmPn0md72NM9-dphlaiud3VDblgwVq6L1nY3Wrk9vyxmUFfLUducgZeWtHAL7btqeFqE2rgkhfGSyWzRaGYNHTGDiW22wopapX26fvCIMpSfrDuy9TLMVna64cOO-CFSN-qaJqH8Z6Rmx2xJvrwsH4J3ls-cV9cTuU9o_4ytZG1KaqfGwynHuEiq0kXPy1Bl9BSNkLCSfXGYvEBlUmRlCQysOLfDZFO-CbyNrZA9KI0Bq8BsDTQu64zKsy14g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzTf6MNG1sA4kXIqp3gAyJCRqGWYlEXwquHWMpSuJBabU31U0Zo5eifOq6AqYa4ki6zBN5LNMgGbGM0hJAB8E9eXFVXNAbidjwacIN6JSi-scsfDZYru4OTVhVmNSea9CmZqPad5qpQU1wm2OyIZWJul8RXZKQ0HtvDKBdtqhHskus5WP3FgS2b2OmqDt-MDld6gFRJJgSIW8kQw2aXrS5poARX_tdObskIWVAMMgaxCu9r2GfQ1ifsk9QBPEZKGXweuo3Z1aCGaI7Oy1CCI2rb8GrGk1e5cI6egVIfuh8Gy5myFhsdlicQSMzqq5MIT9FWS_Lzufe9Wv4h32WEP_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gn_zpMVvGPVAcWPkSq9vq1yamChrYtckq1ptF6G3670ITNbjBQrLMUeFUkJpdP-jmUENEPqcTOR3ztWF3XsLkGVe4B4aRgZK9Sskuv94IGSsgNpcCM5kmhFU3251d5o3oBwtB8CMBsfxuVBwIhjZIroRgfhs4LCjLh4vwHJuw89jz8YHp_dWntZAIUSNo7DH-ICYRp4VHoT4tGo5H7YAr6gkKbgELj5zSwcafSzxDd6CBhUhOJip7B63vPQ_KFfMMRD1yhkaPJ0liCYXmiGNTC8cqyjnxa0lboJ-GlWQZL9tltV5rT4A5vGN6mLZULTvMUYIqwGZ_YQNUm7KwWzyRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnZSRFDLChsxXbyf4doslAmeo09J64qIXPy3dV0ImcOHPuve5RfYfkYJe1qo7lJy4TDPu4d29qZfBGW9XFMeGjmXWegmEUDuTwFHXPzu2kPAVXS7gOjz-SRUdLz_kJ-PRKDMWwOJeJsjEio0mawiAYR1F0OYOQWUH2ezmsN7P8tlkbe9yzS8VSGTpULsy0n94GpAIKiykylX_gc9x98boTAsZ4tiXJ2vh1rZXDoJqQs29leux1jadslpYza_8no0H1M0JvYYxkGLk7Z4kqfr7fMedmY_mxnY6EgTznnWF2GyFXdex3JcQcvbITQhM2QMAe1_FA8iJumfdAqyUBH-Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvPZ9Kwom2TrmdRHCyNydvGuYCrRtjL-N0i39BeMUQxC-09rqPxRWbLZ9kYnnI_WkOQ9igZEDsqHXOHpfYKBylc0U0J0ChniZo4q2iUCNGTUR0yobLe2K9Uf2N0o4cihfpKbNtTxNtK7ZoZ5eZk05xcbMGtHRlR9UhmEUigod2_U9alEPQxNcAw3xwD9VO4zx_YAvUfrq6uz0oMFaJ4TfxKPgZmGs8RkyIlrQWXj3PmUVS9Nw7EL1Z41idPx5ppY74D8TNLsZw95Bvg2K3iQKbqRTwV1zopN4Sk5yDrKhyr33ABDZBuMItL5T0BNDMcCVHT0b66OQKQhbh9DkPhZ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raUWTVdKBYzBUidGoRq3pvHk8h3KNVjAfao8yVkM5LnPYV-0X55Vu09_DaIp-aZLk8W84Wx04YM1mHPzKF_kmi5FocYtTJdFvMhoSDtkUuULzdT63ek7wZW15tVw6uE1T5O7Qo9Rfvku8fD-_0tJVKa6q_G9u2JNXirvWKTc0Ig8glGZs1lrveVXDqIkhVk65scCvPMVN-NIy1h4tRtkgssVWzkMFXGNqWNTny9lXD65uljxc7zTgxqHW4YlxbwzBRetrqRKXSSkea_94d-oKPTx_fGsAYHpIkW740HpYb8VT1zbP_BOl-AwRpVZKIGv2sAxBNB7CSgpmkob_51aPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hao1DTKmi_0aKrvg3SwmdXRuR0ej8wn6cVIVokJpMNdp7nUDucTK0gLyA5w4JDA2UuOfR-M8WncCf89NIUhN0RDVPV-S4TA5huQB5ncySGLS26PEUZFnnyW9iju-K6CkmJzf3BGNl_nIg1AE-ziFcHbchHiVzeL9eRkPnXfVhODtvHVvun_bUiJtyVdBo18RWqFmuIKevhI6ekkb77RJzB9kS4A2HvILOagJW481wYKZOkPmYhVAbGUxBF-j1l8rnpUM4n37d6fTxKPlORvdoCNwpQU-rZDwZWt5RPQAlAoiJGqMViz2meQWY6PSRCsCW_5ilQIqTCL9Fs1-QQdJtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vt0G66kBJnnxVaWgLwwjpZFbm_HC-Z3F2m7GeRrAFS76Md9oAx4hhQ1yqRLUEV56-8xBBFCj1gn-YEq98d0ISeRcU2iKZljW8s1kpLWy9pgSAg8YlUk6SXWRTJG3FuqqfhvfAKd8_gf-D4ELejOMu6JRuVb_ELwJktsSxsSjvt6oEFcm9fT2wT-86f7xmUgTSDYiSeK32aDGU-UUk-mthPCvYagpVFdyHQ8_Cx-CmTqTWI7NLfkqx_nz4x_Gyg_Lz_vIB54Hjq4bfCkFFDYTXOPFwOtnAbg22TC_5PVo7L7pqICSS64omyl_Q6WHSt6x1tinFA9RULoL88KzJpblLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9v7B2lCBtjduhJTvqE8buAVARjnYSLtRn4fgzrtRVia0_Pig7OuTYeHe94xXndsvpZSWaPWvECIRwKdbg_37mLzsl6PSq86x-_oPb5O-FA01z-jW3wBVLMFYHwSHHihHz4zLP22ppby_BcvGzSrklVPe-cj3JkvYp6B9EdXyOrgWe5sNVYgkhZSxketu1mdX-x5SUaxlDsCMdVROXmVhid7-aJ6BsZ6nS--GXLUB7iAbmXdj_eiALLEE_-sbTnt3Rf7gNSdQ2Y5ql6dNTZ1GrObhDi-tZiV4Gu2GI_E-OHMHJGxYLdeJ4VlKV2Rx9C5lFcM1-9OrzVOBvmc4hRCNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4wPo6q6z-_uYSbJlKkqB2_wxzxuktv0v052S_Trg_JRZlrqreXCbLjb-3jWkipAHxwANThwx0vauXyfGfDom0zO-GuY-qDQZF359EUfrdEKlfUp8OMPiinSvTJgFtW3HL5c1UwnhApoUPP5c6iO7u8ML94bjiCBOXkZv360cR5HjOce-BBaojvNygR3fk_fMgZU6-ocx9_clHbP1Ld-KYjX3xuK4p3uVBNsDvMADKO89EjZON4yL3aYgaBYoZYTgqi5hF8875zY4MuBYvxD_WexWoXWx4wbmJMz_L2_nvv9BP7MLZInRwf3W2Ew7qNO9e3RlQS6D-z1ldACt1CfAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfcTtLCPQ71BM7k69PnEwFKI_YSOQTUODyHTU0-ReuvJcKzXy2DnHKxysxzgLqyS1x203ptXXsx1X4fpQldI9faguydx77hJ4PnnGp2nWH7Wkn5IBR4oRn51vON_tn9ockPXwqsF0jb-HLMVuRkrlXMobZLpM1hWCMZqOIcgfPvhq5SgDfqb1e5LFG10Qy-poaJDdL9_qPO7ws3YPjzsXjwFz9psvVHYJ4j8CRavnIAvjaETsXUcmtobVdckJC9eLDb3sRWrXc26IJGaS-AAmx3kIYJuYUMdF3u26E-z8mJxCWO0Ne5TtumFWDuRBpsVGDQEsNUkwfo3MlfcqPGGaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbe1PvYQ4ubA1fiWu4AL8IbwKalOmtZ55KDl1zi-JWheCNLBtguQETK0r7UaK45R-4G2pChiYqOq1b7ISjO-1bWpKGdrjyqcTI3-SZSUN9OUJ4BE7MzIg8aB6LzP_OE2gX-gGbWhWSEzkfLSQlNvjHQ3Iz51lFLLK9EwmLOGBzWxrAc8Y2ZEAKImZC4bY5QiKuY5_bd1Jf3e6ArgYS1fGDQPlPohQwPFQYAyXZPy5HGs0fQst6DB6svKbV6hPUdMMM31xxlkTccmLbh4K8o1_V1xZTEIpvib-aiTb1YbQyK4Q43spyJDftWtTkekiC-WPYg1FpHbt8JnD_N57Nr1Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idEKHnNq_2vilPiOvhu5C5PStLGrfm-SgTllNJCwyNQaZqgrI4gNF3HC2i4eykeclyGnO0_xk1aRJ3M5wddnfqglMitZhws7qukGBs8K1Ka7uRf8GYGR5FczAyC58LfKNu3PP8VZsHzimdkR-914rctpPUBtFbgdGsjN6zjKfJxDm0taD0EdjBCQh3r8USWSEj1ZeLyaBerFz2fDsuj2fapufYKzjHpvrRf57Iq_CqY97mu8TWgpiIx9htahVMuZJLrOqFDIt1DtMUXRC4xa5ExGv0YpgjUw24K1317j66MQImm-GaPr1rhijLM8XTL4sUQLrocePdiar9R7HZcAuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkT0kEtBxduUN71mYibeq4XqZkyQNUA6e3pCMY-kFKBboI2fnOpF21sKTpg8S0Brk5sIvBxIrggOWUPES-jbNnfsLcyxFPwR2pJYGsA-omRb6EOtyG1H2O7StSaMd8jyxphmj7Wh-eRRvqztZv6rYDWjQRVMH7rwvQTZz428dhpNCo9y6GFklAboG9v_QBJ4j277hvWvdZ3Z3jhoH7gbYDce3KNNDBwvuKTBTsaZ0gDbxCdKQm0zVT8gH98z38XrKEXU427kQxRb30gYOi_9SoFijT9Ht_5BakwkqJ3BcQDTr_w6W5w5D4CPUVBX9LgUYM2x_Y1IAxzP95Ze2z7SJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-rNZpeyQpRZIO4swekKOeQinjscBLhGLBksTq71udK24_yuPQK22_ZRKihl8n3oXcS9VEdQhp-aEBRDmaGgyLiYwNqI5qN_m0vsYYA6WSj8Pppr7hcgLDpklR5r9EC5dha3yN7YFQUtrB1GnRtTVTZqzDir2qgjJ1MtO3x_1IGPGE2lvQyd9lWgwQVzzavlyIKMJD2F6DTjeFn1Dd4xVMNnCeaxkORUEJQKRdOaAWhsFtd4-YHUZlBWSamLauXpZNV-ub3yjrdjMpZ-ejKTawrrVv4WCk1ts7WwiNLWOulIHbbToLIMlZ46jzRG6MlMFH9OUohO6GoDcTxMLDiCAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsuHvsWX08HEjE1lLW4IDmWOyqsxOW1gxRjL6AEY_RYv6hqbzGTVU91SA0Kvqbsl5OzOD-72QeTJemLa_1nQ6GFFwvWhuG4aDlnGrRZ-bUBPs1BU_jZtjD9dopHp9SyRfKPuU-mHTeMGyMLs84gSsUIwsPbKvv2ejpjEAd5IHTYf92E10eN5GXa0Y4W11DTmBboecl0usUEi7_DPmzD-nPkl-XfwcR4bRmLTUGcrWCXsenElTntG51vijdY0DqFWZFrER1nm5LmVGea8NtmusA5otLOF-XDlKQLty7PtpgfdN7aK4jJYbzC9RgAJ8SuG6QspBK4vh6EyFDUgImZ-Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnM-fBOg6xvDT6kc4OnYw8mF6qybaRSTs7cOUPD-57eT1n2HPAk5L6AfTKHzegSpo5wvIYB2cE-_CpdBB_GmtMKs2WP78iv5pyq05t_qsfdQcwo2EQ3-kzCyRGTeKrocJR1vio8znVd0F0JVKqQG-0c9NWyOlDjnaLZRloCiWRTZoDl5Y0nw5xEnreHT10MLK-kDztzarnX3fWBNHJHFoffSCaNv5Tx2YoVrRAX7HRXsDjd2lAnaTEAUXzMmINmmdm-apXQ86Pyk2COa1QkoyPl4Z9UyI1CtnXuNiKYE8evKFSMt3wQeWqa4k1ZU43IODS3S8l9C7qQAaOFSAGD6zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqUbfa69rfFwfW1-BDpe8bQa6OdXU0MYp08rgyZVr2CaBQzvPWnXthMiUwHZuk5XVfCWr0ihy7bjmjxAa127GMkVutL_42FOf4gtNaztalJMyu2-Y-Nm5SROtKHFqBWvyjAkTB4yEks7MBS3fCvUJ-o1lCkFeICJcaE3izN2QbsylXaS5jInpr6smqJf0e4yqj6UB3GDB1SRN5YrYMBJq1hk0o6f3GakruQ3mXuR3b8914ukI6oeAiPsLXn4WPVWTJPfFuXvNeG2HstOtAzWaY4QBUdIL6rOiC-dF3trOKigLDB7Ng-Pp2paxtOQ1gJimYpp1xJiuYMH1sddsxWWNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGgYYaZ6_XJIsh_J0shdgn5DrKIb8Rlg7oNTuiq3GrQ1A3Kcy9FhXi6-S89Lk72vs4TU4b7GGq0vsnug8g7xsqBsHHRLMMiORUZEghK5dMmGH7e-P_TrH77W4r2qsJFNG3x0H4D6Fi6IT21ZqigDp4pE49hKLju74kHMbde5U2UkAcJJGE5aSVOzt-3VV4PQscODuAPgkVowhwO5vG9gklWQ5dFsijYqDtGptZxtjjmgO4_Kiwzj08cNSOx5KyUP2hfC9FPw_bS2beQCPMioZo2KLMJK1I7BStGxSOQNuOx7i9TrCsCMElOF9k8kXjROvL6Cvw1vZPCkkT0J3q-AGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛ رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‼️
هایلایتی‌از عملکردخیره‌کننده لیونل‌مسی در بازی شب گذشته اینتزمیامی مقابل تورنتو در لیگ MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVmDRXAtelR1b6wlcXGvJU8lm5ZUe-VYbb8HxGr8wglvaLxZK8ZvREA_D1TTwIrZbL3cWzS_IzCZLCppX0q7HEPYQEtZuu9GbwdS_EHWG9ey4aW25ENVtWVu_fH7pxw_tHnxqqHz_FfKXUDqZ1a62mL_HzK2FE1-KH1cwPnzqBcv5DRtZ8uUmuz81WACvzj4j7AL3I-cy5qJKsjpciYPRuTCCARkRVpRYqTWo_0EsUWNxdQwWeK1DBukV4b8zOWMq2TInIyAu_GVTmB3Y3WubT9APSmylpVJeZoaM1B06XlQUtR93BW-V9jZlZEjd-jEMkQK8H7jlQz27Mu3HSwTWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzpcnFa_rEwb75c5ECm6vAoYNrzAIyphJhehjwUci-jzNxKLTpXLkLCXMx_QeCHiMyFe2CPGxd481lX3qV8ZOOV4yL7dk1QBX-L9zh1oWygf8G2piylTJs0_C9fnmr4cF-haFzU5eQWJQbZkOZk9VRMBbdCubo-dTec1N5n6muHVbKU8TrDGhNJQjwCzDEqVujLoloeU_0-7-gZb2xtebytRwuEOFlFyQd9hQjfO_s1Oim_F066aWbQeeUByt1ZjmOF_jcm0VjJcZkvheacJDljzh28Ufh15CKu_HjnQX6al3Gg4N6SqNOEaiBxUbvlG6spOR0SiZTdhQ3HS3no98A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdwVUXzw7UMaxIK5PZcUsPNsMGldQH51HflziwjoP4VSGd_I_FgleNZwbxeciu8B4qz5QvZVR-Hzh0pE34sFP2TMCf5SyKWQ7Sb52F69FfgM-uh0ggf2rbpGSc71WKcgsazXihxUzwFw08UHFt5reo8u1C8EpGJejCDsBCsPiOPT4xxq3MzidpN8kn-xyeszy9n6-pUslHqUzOcFwCHm-Uy4MJuVdpQjMKaMpiaHj7tPontkijG_92wHqRr-ir7hhi-SsDxZLcnRZeq-QCukoIP3ePx-rdmG2cZPvvt9bgJAjYM5o3zqsI8QKSOyMFkAM50A3HMsZSu_ll4cOh-L8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049Egyor0h-tUb0j4i3fLYDJA20GJUd1FAgiQKnuyhNqrlb3HjeWs1GEPGk0Zk4cz1e9jX2KTotZXLejpY65QM5zuEEIVUeGoVajsEAiVPkJuaOi6uvQmhmkRamL5RZdFtviOvs1ZI0yUteFuF_dvvHKPBdEKHRzBEcRLuuh_6ZFPuojONJLFpDNvosFZzrg1SvNOBSqYXFtdifFB1Mb-qX24pH7pdnRbyWARYlbZN1KTBEVG79-xZQn8nplasezDPKkmE3J9T_PmNTHeZbXVEoII0_BoXsrq4nEe69DQC_nvrakhot1J6pQZepqVoDFBTwdyQpoZy4Xvvm1x4s7FNsduUQT2s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049Egyor0h-tUb0j4i3fLYDJA20GJUd1FAgiQKnuyhNqrlb3HjeWs1GEPGk0Zk4cz1e9jX2KTotZXLejpY65QM5zuEEIVUeGoVajsEAiVPkJuaOi6uvQmhmkRamL5RZdFtviOvs1ZI0yUteFuF_dvvHKPBdEKHRzBEcRLuuh_6ZFPuojONJLFpDNvosFZzrg1SvNOBSqYXFtdifFB1Mb-qX24pH7pdnRbyWARYlbZN1KTBEVG79-xZQn8nplasezDPKkmE3J9T_PmNTHeZbXVEoII0_BoXsrq4nEe69DQC_nvrakhot1J6pQZepqVoDFBTwdyQpoZy4Xvvm1x4s7FNsduUQT2s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
از نبرد تماشایی روزهای گذشته فده والورده و شوامنی دو ستاره رئال مادرید رسما رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22066" target="_blank">📅 20:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22065">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOPyULpKF3J13DHW1m90d4kJu749ts_Yc8b5Ng2F1jM0WDzbr-IB6wLj0U5Zqpusf2cRNH00GlBsydXGezSOgHI5Ne6uuJIrUSuNZlhzu7FhliyypYcFDelfXEtHglbgJbypdRjkvXy9ZvynnY7NktYkFyjZSrAeUcU8NBmS29zobV9BFFl4e_JwQJmK5_UrZ1Renm1imbATAOvtnLa-M-DZCx_znXhQ62RSjuVrva7XQom3HKJmURAlG2SUkH6IwMNoH638va7zQ5EVFzUb5BGTQ1PBgRNQfaa547J_aOq1OPmq0ACwBeTuQg72YMv0RyGIguBwbVVsYa2a3DHApQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0q1GxLVliGD9AjH5e0TuCp2l3DqymkQMJFhZNr4jT9KH0YCYL21awaMMgnDskYvuzAFoqOPSiM1WE1yMiaadLmYyvLzj3g8Vn6jJ77a_TXSp8-9Ok7qD59rjQo_uf7rMWW__re49stFTQX2FRkbCAe3LxoosIoCIEa34ozwvumvqBU4enWYG2JZXkvU9tAQVuweFgS0PHUwtCW_FhHzmk0N0JpwNZoM5EO1ozP8JHuPpQ5YiCkqBx132shceAIWfT9ltZ1ukkthu_HdUmEgJwbpvZBehFsDvAQvSss0J66tykmzhGMbq0tT9v5YAyMG1Y32mXSTRMu8DD7I1uOqEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIRRK7mZ1BVP942VbJLHfpwwp4xgbgTzPNK4IEWS49NXZrIzk1BZXwLLA_yGGZMg3rh_fgexDAEAONcCpdCxpFhuKv0TSEYNw4jUjhQIs2YmDGCPxLEEChtZGDO-thk-D6_8YWkrvn00jH-QlksfIpjZGOvCD_PnFQt6R63dXmkOF7f2TvtPYtB1jqaZtAHjc6IVO7UcppJ4xwbyoyXaOScI872P9Bg_gLZyCn_ZCxLde0JT_NqSsNPFAht7UUDfsq0lDE6rIWdy4JHx67pZJrZG5-0WZc7lZbjazEMGJgtXrt2ARAZrrrCj9L-C2MHErQPC6YnmjdhFhHklEjNTrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klmA1lWd1KrAKk7j6F-9fVwApa4oAA6ffV5DOyumwqElUU36MthFyg0obpIsBlkDNNtjIyRop2qO2gtTPj4X_DQh9zQWNnmZuLWgLPNdGKWMULqbUhZPsDucLEq6EKZ_Jz07Y5eWI3AXQrM6R_p6zB1bHZ8fFfr1DfIuRCtn63q90R9gh5_k020RA2ghIspWGcqv7FLrz1ObaCjeknXGQd_oJezyH03bBRkg1J8JKFsFs20IyNKFC34L2poU7TsoxblVhvB_k0D_u087PtRbT5E0RJuQEb-hX29B7K97LkLQqiyVlMEh10oXGJlFi1-rA5X5mRuDoUT49vxlarv6kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
