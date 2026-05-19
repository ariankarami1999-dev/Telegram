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
<p>@persiana_Soccer • 👥 205K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 14:16:55</div>
<hr>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr6Zc717NnwcyPc9GbUKf7oATjOFZyxX_VYhwdm_hVCCF745v6Zp23BGXJY949_o6hqHdp5X1Mk2w9vf2mTdlsqc0EIz5xLCLhf-sPl2YvGk1T4Ya7fHmmn5DofBUlW3HSxtjzGETMZdxV0jZvDDDXgN_01jU9yHgSdreOeVf3o2UE1oExHJL1HguPk3xNE7XOJty5kRfqiU4eyB3We05MkqQiZ7Y1EvUVkaccIJ9ybnGj4ZWaJmxd8HreppsSRxu5NIHJg16D4ds_qRMCtIHXZqLWBFyQ_H30McB9SDm9bfiGA3_N_yuTDuR-c7k0oz60Yr-tDM1-S1qAp4mOAb7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGGTRfG-IIRXU4gy88H5Wbr-rWSSUHHcG9kP6Rl8pp1MNHyNIhX45rlJ5_Y0LXBAfbs-0h43C27qZRLavvmyso-apwtgKXoAVdEERZI6fs_tD9kwZW6-yFtFBWFN4mZkc3C7-_2_qzgRrQzSxCbRIEScwewlYsTHvNYRGLyCnNlwM4N0_qR5dqky0hfg4DvKx2CxT3gaoP7mWNIk4WPJrB8Pp5ShY5JkQyBx5NVjV8Dv0Y7SlupU7Uvv8eIvKnxwAKnsB11I2Vu5gYwE0SQZp6B3VJDlJsrTX9j4lMtBSyW8V_7sdWtFpZpFYNSam567iEsiBv_1M8l6pN9Pnfi8PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/persiana_Soccer/22184" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22183">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7621338636.mp4?token=SewSIDGPMFC-3fbemNtTmpBqVV44Swty1-EkMDIWj_QxBNf-XvYQ5kKttLWUZn4pYZ8JYCQmCK58aDnvPKDDVOuSeGCk38xybA2jbMskrIsh02HU2zG_V_YPAx3jY8AEQrAD1SFfkxBHrBg9ipnwhGEX7vj0lS_J6X3lEtlNT7uTDqKlcx9k5L_BvCCngqASrJJvxYjbFEwgy4FfVUmBvFb7YTyNzPkrmEeaIgkZkgH3j_0qiaKjR17u47kCv1L-U7y15qpDF43tXaeyw58ImRpv38CvdNFMciXeBYIvoyOaczy1EjrgTpuJbZWR2-1yHVZjF1iHjpfxaHcYz2JHkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7621338636.mp4?token=SewSIDGPMFC-3fbemNtTmpBqVV44Swty1-EkMDIWj_QxBNf-XvYQ5kKttLWUZn4pYZ8JYCQmCK58aDnvPKDDVOuSeGCk38xybA2jbMskrIsh02HU2zG_V_YPAx3jY8AEQrAD1SFfkxBHrBg9ipnwhGEX7vj0lS_J6X3lEtlNT7uTDqKlcx9k5L_BvCCngqASrJJvxYjbFEwgy4FfVUmBvFb7YTyNzPkrmEeaIgkZkgH3j_0qiaKjR17u47kCv1L-U7y15qpDF43tXaeyw58ImRpv38CvdNFMciXeBYIvoyOaczy1EjrgTpuJbZWR2-1yHVZjF1iHjpfxaHcYz2JHkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/persiana_Soccer/22183" target="_blank">📅 11:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKZB3K4UFASRPJU-5lhPEYt_hFDUrNPx-Kh6yeTV_VIurIQ64h3QXAoI3J7zeV4ZiXY9NuPF5mhQQjFwpDGrWVkt1qTl56DiaTSKGdhkwyjX0xaviN2QDwTSl5_WSY0LQnZ5HXJYEOJkeIF287dkwmRNoYsP9Y2o_eh8AcWCASljseBx0HeJH7Sy3d6hJ8NuWHyStLFwZdmGDdtGDeY2-G_hlM4DiYZEEj0hjDIl9A_CM2NKjSflrovZ6gNzYuwzlTctXsUgXd8J0Cop-dNBduWmowwmBj4RwyPoVtRFDerDOc0O29hSjPUg9lpQ77eoiRfEEdWbvHmrV7aWtCBl_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ پپ گواردیولا سرمربی سیتیزن‌ها در پایان فصل ازمنچسترسیتی جدا خواهدشد و انزو مارسکا دستیار سابق او در من سیتی جانشینش خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/persiana_Soccer/22182" target="_blank">📅 10:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvN73u2s4ctqoiKKh87APKEYe2GQcS-gSFFuo26yTMIccxYYEh5udQB0TKIfHoyQwLlX4VFnnMHfBLubOhZmC17vbd21m2NjrYCzjsd6X-igKISJr1-_yQFxI2IcLiaz-4vTTy5UqXKGzFMGO9EfccX_eh814J8jXyHDZYJbNZCqpR02XXEADBgp_rEBRdzT4E7ojJXrxBmJu3VYznxW1l7sAlhZ0iIDbYM1KUpV_ZqdsZIhizGs9NbE9hD2bhGve0NVFYQMdmy11Lotcm_gOgYpmCy0SL8itoPy6y-4EXYm2U3FO7bYt6G33OyosZ0Y192GK5L1Z6n58pWzkh-RGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXAshsE8iInYtW-J_WPZzEx21DTtFBBmobWVGjTLRLMPfzM8W7L0V5sU3l79QmhsB4sBZWjBP7hbTnzfc7qrbGLEaFtJPMQbC_culHJsITx6vZ_ztJ7jskDMrtdBjYoDm0e8xMK7QtArUFqh5YOoIrVnZ6nHYdwdENRtHPS6fNMi1vH-vnbXXZ4WFk6Vjr31GAEkYNU4YfZsMMYOQvBTdVRKrr9WOQZBFuEpSU3wDSLSUd4ORlz1SP8zLYE8Fwvto7DLihAAfUyuoc7k3KhxcQyBGeTNnWvJxnSWlizKjaLUILTU8EVaaB5wV0Nno8GAnvJlMwI4fPIU-0pf5vsZHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/persiana_Soccer/22180" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXhMoeQrNLHKdqiuHkhW2yuFpiyUMaagmQUkX217eNHFurgoTlwz-FPTztORdFHVhgA_LCrn-SN-qO-oxkmrpqUUQib9wKTW4R0uBZr6mBlbhyHz3o2Y1bYPFvBslffvRkJsnElkqbWA93CdxOcX69vqXkaPV5wvT5e1OPUcbEEkOxfNKHTAc4XFgYJS8hOtaHm_hwykpUsrAHAMm7qoMT8bbADmSbdSrUPY6YFzFU-oN_E84lB6cD1nwejF9vfmRFKwJjEhUWeRi4QSp0G7jOtRipBva7DCZ4_q__v4vZ_2MArocYVBzMQgjD9lYMZrmwDL8hh5FXVPlDKFpyESlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه جذاب افتخارات پپ گواردیولا و ژوزه مورینیو همراه با هزینه های هنگفت این دو سرمربی محبوب در پنجره های نقل و انتقالاتی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/persiana_Soccer/22179" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22178">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/persiana_Soccer/22178" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22175">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ovIAtYftyTF8ccrHqQCCG57x34XLARaDJj9Ed2rvOurCfwpC-wfcpdhI5udAMsMlOclEgB_MI4buwJNiqh1sO9g6XKR_qzHOJm31HPvhHct-t9chS7vdQShdbM_Jwwc-rc2IhMsHs78xV-fhEx6oFa2uvmgEuXDZmySkk8Z0YwFRNBf3IiZ9oSkFIRtAYZBH1RLdOhXo0OA4z_f5l-Maf0Z8WwXrc3f5xmvixAvroHcrDjkymgqVOhwaJ364sQ38OEA-Aa2LGMN11Juz7-tAjx13OLI1foiZTLHQUfhVt9n8bJcFePfGj2YEYrsOYFvtHw84qgwm4qTCK0o0FNYvMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tXgJ2dFO7YWO0OGjkwmrL7hgasvnWWTn1Oifb2Xb7n0IdozLthWkdo10MEWry4paY4uG5dJ_VZbN6nsyqhVATq1wVXtgL5XAj0m1Fl1NRO2RCbVkEKKANv7C8uU-gnfJWiME2PehJru3nOdd1IMAs4pRn_rZNgh6UCSxFcMRl3J-qvN0N6tS7f84GUXJZDaDsgqGiXGmBVnimjWKmvqqO2FwAx0spq6BHZyx5N9AxegmTyxhFTcQofeFKcruHPR55K8wVEiZidElBxErPfdYukeUEwzyx-WUhKNGc4TUzk0Swk9QPMgDKWkxPOGk8wTR0Q7YrBZjEIsd8dFEkkWTcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مهدی قایدی ستاره 27 ساله ایرانی سابق باشگاه استقلال در کنار پسرش میلان قایدی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlO2khZZOc-l2iN0Fw-AZOI0aO8Oe2DGzolcDsjnYXpdFXoUffAbKIaWIMhuTUAvsaPPuLAnjH-znG5nAVp54RgmYhZuknizGLBJ3xeKTxP2sjiVbWLrBzE7dtJYehyfsi3EmTPIh18oVbpso6Rw2kriinNM4MUpqX02YqnlD3nmo4zmjvJ_MoXLXyOPgvyS6iMfMrcThbO71qsM337aLR0-F_-fK5p99BlLoEKcPFWoVprqIBj59oOm7zPBkIW7JBA811kNM7H9a-hLyEEl723rTAVkucrU4oDDFPUfJkT9oeGLNRB2oyUnDqLx2UjlBL8ursJZhEsY1c-Hh0rqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJjtUfafxtWqO_zERdgESZKNKv28nx8pxdnML--EgH7pyy9Ml7brxsIye_3vFD1AOVOwCXgladLYoOXncX5wj4wSAsKkQzYJyvMIv3ByAjfBCrvrzPXIuFZT9QUXCHC3d3dGLYok1uSJaRwte7FFmXy3q1GWDPkjRW587G8rgkqIkMDAs-kuVCJ_lgoiCHJFSqgkrtMGIs_T7YuTcimZezOndeLI7d5rBzu7n33X2ri9gQ1YUVqxGqBYu377XnxitXCGCxa14iSPgiSIUhPmQtdG4opFILxpfYB8vYc00Mz0Vks0Na1lueHuui9DYkkpTEajTApEBOZTCihDUvDpHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22172">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/persiana_Soccer/22172" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2MUKQxcPPmbBNOoWeYX7m45cfKClv3klSAe4xGnCawy5hV7fPXlUwkqFzRVqrQYKRanEwc722nZrtd2pOCjA1D20RofKn-3Migo49ianpouANt8CN9KDde9dnl3OiQ6486-7H-wiW-g1KLBvbycX7q1Ti6ZCzMZftso-ic2MbA4D0Ka5bpiwmBb3zvBOcOCpMXIN9-oRrSWk5YrJEbIaykYRdARd0EdJ-b7TQt_Ae2J51fBTHrXF58Fkv3EEKOZLq5fxDqNoBjx6GkEY3v7P1u3L6PyrzxIT5Xbmg4XUFQfiRD733UUsUfe8SoXGjK-tpBeTUpkEY7VJkjjKkfO7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Natb-_Ole7WksiKnrMvsRlRnOL35kvCuUYRb6mUvVFgu1a8zo1iKHmKVpiAuyoPZFD3wTIDTOz3ZzLk0kkNOyK7o-DJRmLjrk7kV9DVt7eBaY8KNB5holUTbKejNSiUbMhQw5q6rwoBN1-7UlcaeO9pyPLuEKegPDmVoH-i_hf7Ehwu9wfqiVRWRo6CPKUg9PZZQnyvPhJfbS9LwWNzq04dgBhhxrpSmL3kq96z6V9M7J1dgc9D9KuIqI29DOkSWTZCOCquE_euI5063KfG5Rb2o5VTbK0fP2MzjD5l9Q5vUyr1cavrwkHK42e8wP0yo2IfcxpK8Dv_hhWxUMhOH0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3vfeCOmkidRGknnx0NJGqFDfv4KMlGBYb4tTgn2XXop4DBk6vmGAHBaXDStS0SY_XheH5I9Tqc6PXR66LcFrQl5IwZK6AhhdEBMlO7Qzfylub2ocNaGqXwOUSjpDKpPOJQcEfPUdW1z-xKa1Wd7-W26E-vx8pTJjFNOqM91hZtRNK-BqfqTJTmsOkbHhd3uj4zfQ1FjSBtZ2BBl3M5E-fTWhrPQYXo1SQsWh3F-0lgOIbOtU0WyQRRPy2mF9l3HtXytvO9riVUs_2RCbxyOQojyCnt2QoXyZKHoB9nR_wuOCjINPhxbY_a_1oOdGjhG4ZacCBuC2KO5L9fMdthtlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHOApNytjJ3TU1eVvYc0g1F_sNDmsGMLpQZUbfOxXyuGeVMSes_ROYs77MUSPQV1T9lZGnAAafLz7IPs2wX69UhNPq-vVtKYgPHIp2KOZ4Bnd22RICkGsVKETFPfPX7_G6oyNq3pJC6DKoydaRYQZ_QUSMmIiuaMY9OPlsEVO6S58FbjpeP4m486XeTTxMB9rbjmzgVVlbOhanw4M3Kt_FeRLLe6xiBSCXu1_-JDoqDF584SSO0qBDndoe1ZoYKU4qiq8hSeVC48yX35vO7qbrdZTHLnfcT51LiDCA1iRUKw6ctjzqhfx-FyraiWrBVlp0wzUaPFv4QK658Naht0tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdDwpnMygaEC1be6ROoVIDZnF0YwALys9ORTHoO2b97txD-HbMzIFqbbkg7UsyJbKHFwSposuykdOrKx3zFp0TejSQgipAbIl_VOx8lGE9dgU5yrYeMnl72qTME5VQtliLF3-jI7ZR4yvVHmUSUFe-g4Neye8fW-9RliAoTEDl167fIZ_xbl-0m2zECFbSRPY06aUN57OrLr2MwYkYUQ9oTuFcUt_m1LKVdXjT6eCBPGT9pq_ISXHn6bJuIg8pjYXwXTYQfTYxCeDpr4lPGjSuASardex_RYgjPEqX-zAMmrzwHi1fHEo6DZ8nAmQ4DhsWJjqAsxCosKrqOl72CEpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h33ZoQoSg0wVH2_Mz7DEPABRTWVFx6vsNf73h5bmqZbSsGIpCzoE_YC6WiUw7YIdyFwss5d_zCjJbsyOwiwg1FYUFx6WDyKYrEcI6sAsAHjq_AAcPY1r2EZ_2DTCAfSEq3lkzDU-bfKz9AKHxkVYFEUwj4LBXSG81JNxjDTQTSuzr3wttjQXvRNKSFJ6UsMhT9DErpQ2WUfeNkGaXMmsP_afR-JZIrxarHn64PTUlfBs5_bSiXq13JlpiGRmZXAoIRd5Uu5V86JYCJOXVbCjODqxxo_qRIBsa5yIkbDjUy5lZLVAW7r14MexEOXiI73kkdFHK_OqPE0i54bUNzZMaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5KCCMqoDYYzt_CFFa9lHMGaRTkG9LrhGV2P-hMuFgou5w6rBRWspi0exXtr0U4PYgQPiB6-zcr0IpjwfM5dTTSsC8wUK8yKU9Lfit5I-3ZFG26FSF6RkvdiHmb-Yy3CO9CxxFLjp9In0gzBRHbCO0KxaZL4I8BpsFY1GaRAi2FoFRDPEf24w1eJVWSstaDfZbRSx-CphltgayfK29eWxcpY8Ih304pnGriLsT75w8OH_EifuZ8y6mE_NqiSVfiVGuLb_2VnWmwTZNznJxSE43y-eIdKee09B0GPoN6Mr9Fc6O2fJjg4fC7q-PpjDC8K3qCapmr5_sSgGxjic52Jew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGOyKBqG58NmhcutQKVi5TaE9dk-YYyU8xi_c3nOzJQ3LO3ED-RWBsgwNWtYsKBRd0h6oPrPrw6XQqGQPxVAkDuP-jfGgihI6P4052F6l8TJBET6MjvSuo8221fSD7BwA9GfFimKwHYchw3F2k7eO5Rl-ek1nGzlwJy3zW-Vo0S1mWPRv1Cfscq0qPYY7TcICVa2iZbzK3LHLSRnw8Qm6eRMk60tAq1AeenQziTVqKBAKPXcyAmmziQssCWJ3DuUP5ML66Sl_V3fMGx8Jp_EuPXVg2VFbBAnCL29So2jnDp-BNfiwIEaddGZsKjCtd8dk9Xm0XxAunETzI5cUq5CIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAEcG6hPdQ130BVBk_YWkh5GXccV7Rl8KQUyVUwrelrcGvxUIXTf0BV9vDeWHG8yybqx25GWncJtLEsFTeW1KnozEa_TzSean6sAjMTFQJJlXDtcnnCfuWYT83wA8BOKZJHbPlquFfYecSgttikikp_JCiooSD0iZprssvZrK3kJl6KppZ6IVlr8-5OZ4hgHk4CvJImucF8dEXvh3jod96hKbi5VYh0UgFnZYpKopJeuFocmWKs0swmPn48tmMIa8VUhVkUkS0xhL2MBJK9NEc9lV_nKsDIhz04k3rEy2TKC4XkKJiEs9JAijL10vfEX0xZxfdBzmX2hbhVfxqnsCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rG-PlUV5T3LJWWk25U7Q_EIHrUyzPSzytAIRF2NsPNmzZJvUqWFIp6WCECRBt-pQvKuKuudDfOO-nTWEPOxiqOn5fnSkACSGNjSaxvRj3Jhh6GLnKqdWH2LzAUwbDoEsiKQLC11JsLT_1-WpQI8CWuT3DkX9O-hkKOh_tSQg3am9-8Ff9SVlg_sNxBc3QI-j3L3mBHWUHrUz1jG3TE0E_ZTf1kc2mWHgON0lnUsoHieNqfIUgKyHgnYqoGg-4T9xR1dXb1tyuLBxKUw5qRSBMVGQKUS191hAMIr8SLuMvYTpo9aPQ0EBdoIBrRUENXgaSFTOOkPC34YoieZ3QEmuaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEVRGhfzTlDVOXxFMKKTP5zVLEEgtB4WMsrjtcbRv-z79r_NGGRVwHRMqdrwjbgb0GbLrIcPL40UZd6NSeEhJBhXn9vx1TvwtwNnQdKGk2ME3PDp3kImqj6HmNatcMfia6IHNFt8vXxn1vpVNIgmJ4R0xMOibnO4vj65ZgsYiu6HXmJxhqoK25Ya8j6WdIDbivFBvBG9fTFzCBE9frXS-HQZz4oK6l9D5rCkdb3q1cz_0EA5iZZ9JuEllMfMk4i6iVaz28EbIO4XVFfRyO4xeCBRhB57MlmjsdhgT52-Ns5u6rte1STCxCS7LyIMZjfbg3NwBASYacXmntTdMG5c6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUnHHP9mRQefKIshSX3phsSNwMzT16ZqBKw1wctKHfWXtsRzaZ5HCIwR1C1il13FzNvn5DdwFtPIxnfjvVZAwQzUGFDmHoAb0A5JHqGxCASitXgv3hOLcTl4H5Nzx_lIQi8xwDhlKH0dWVUU7Zj09cRVNe79YCEDmwJFCZUSSprYNA5dR-fy09ZK1nSWOgTMDasrGhkrMt9Yn6fyiUUiPSQTqq2DOftiFESIPteS1NVw9a9ygg999IwnnJeUczipour2nlgbedcROogQY8NlEo4xSNufSbEXDMu_zMHJ2aeYJttDgZLwOg6CKg2fWuIkqxMw7kKuR64AtUCdu0xG6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3bbSOpqj-nLMTBokswYax6--qXK0TJ778d-icenqZbUOwhXDaeeP4mM70bkrZ5XudGOn_nXcmd726FJbihOBS_IDuUny8XRjN_bfhbPfC8_C9LYylrSLHW6fQSsB68x80-n1ei43ZytP_Geqdh8-hGOCe7uaiLbELs94hww9wVH1dVpgEb8IN-AgvyRaieNndo3ts9nVfz0oLPsPL8Ul9VUXYiGvOoCkycUomrJ3hw5W-INmrzOl9QGyd3NuXzC7q7_rVX5LqOA7IRzQVNm2I5JiKeNWu_ZEGoA3Aisc9aKHdJ7OE7JQP3HenqO7KYG4XES_b4sN2G7oaU3vsIwbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4FPDgYLARbKPAAkEe3KhphBH4SDiR1z6G3M9PTjRkOL1mVpQkH29RYjUeXIojb58tw-7dnaUJSuZTvXf_0bpL_CFfEYGK0mDjVJ7E712K_LRHhtAFzRAcHnZhXlpoNPTg0FZ7ttfYaxYMphVeDCL0PPCv1Fic-KMu0VKfIp4p_8AxXszXEvXKfO1q_G90MAwCKrP0ZOo9qlmSXN_ncgR_urj9BAkw133RoeQ07AiNYriWgM4CxnkMLflP50fdJVYHYxe9kevIZvjHXn5zVE3gLFRn9TOZpflzlVkwGUnT3YmuesMv7ZR-4fVldJkuMrTaNUqF7zm_jnAy2uiJjR0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUC_uU56s5JR9aKl_XcvYzgxdRe4pqe7iYa7ifTL9Wyp3yBPi-AcdH54oFRcYnqk_EA49l14g4ZDdvtmjaKrtP08zVan3z-8tBYdhdnj78SomI_q4h-VyRJzXaamc3uKLo2X2AzlhWYalvEd52OXN7MEBYt6t5MMttDD_zJk3ViysrI76HZ2XdwsI5g80ro8heRywNhmvKyAzB4E9u0n653eVCs2l6Aoc_laqOesbvttmlOoT2sgP8GFmA3TA3pfBkD1RctOS2iECc0Ew1sLH16W-vPI8LMzfrdauPq99KX0H64Zxz5hbYENmalaYC5pm43A4IawFpLOVXpSSVe-zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8b4AfBtLLOcbwGuBkSdCJ7SvbYMwVC4tOVHZNvoqeOlTL3KM6FdDa89Y7LQ4nTkbLQgINMEM3b1YmjeWGs9pp9Q3QwY6uNjSENe9gBYFI_PtRfH1MY2RUE2mJvyRhXykVRwT34xNplOffrQ2H_gogHTt4JgsiUS2DFAoLyO5GGPyns8mKEcwXE_cqKE58iLcfFnIg1WlTtO1EwBz1yzYlhZSbV05hqg2j4CtuuoYlyGsx84xd6lGtk_S97A1qDKH0a72vCCV1k1X6X2VxAdEPM3B2Wtw2kbZMtnefkA8-uEPx1s-hVMogCaAEiQdux7WCtf-JEnP67iHzyRsDZfJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIier6VcctQ6OfAtpc0OuB7PsiMnqRPqjvxx7NoCFOU235_E31uu3GOjDPLD6H6NfOSKjTuCXBOopDL8RMfOnBtIY6LGEYM3Bk8riKGz0a0iUlkaRBLJK87h1QYK_HFt4kQ-4de9oXjHOSMDJ2MOKsN8Ev5_2w-eGUxLTFBUpr1Rnd-Oklo3yco1wm18Fc4OcwwPD1CBYDzGrbHYpRwWbMWPGdxQgdHY5BPVwOAm68J8kFEEmcEYbEdpeVFMl0w1SYYZA0CcpHiSBbjjAUzZtz7LQIIMMIC2Ic-h40rPfhafn34vBmcNrOYqoVr-75QLb_3YAUYEFD2GITkcx5HgIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vx1Uom22_gByEtammqRJU5pqwqXl5MLWzlnkO2Ljau4zEy0I3NPT5UbKHiG8e5nYLdeDysZtgqM8hpdDXRah8_1upuj_eisv4KbSi4X9CbFA8Xwbr4bNzGizLs-0_iLq5bHAQy-6_v8j2T_45gRyXT4wtBGeKLzNAbjuUFXujh501GPaETA0yIuLxO5IO6gkqozXwEWr73irh1y92n0fEMGTQ-Uc24Dz7Xug8hUnreOXe7hhhKtcR-2DS_-7LYqxXW1ecVxQ9vE_SWuEBZ_5h64tIsylYEdaceOLsxyFiCfur5DtsTH7e_bXFLthEbHqzOKoOQxdoAtUUSbq324cdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fpd4wbofHwDKbUAP2Q1sBohjc1lZDBeGcsnmt3OoCKtg53SsZKXWxJ34MOyhTk5sd3NRj5py8fAb_Y4PxpsxeaatND2kQ_1yHfU6yrRNXr92TLXFozz8zz6o5wF7JUKDw56r3xKaHDmKBVPfqlGWAIIk37a_o8-9pMe6dpRNT5voMOSHeP_SdPCwwjdVSivVzHn224D9jaEwVx0VsT_uHCt3tHnvMiGEAbsrdlMJwO_rfuBV9CJGuhUAwbPArbL9kZn0MNkycvvrHTUabciVMQUAKgaiQuSet0CKdSftRKev-3dvcKH48qoxvZrSL-rEGdzfu4qEry-KdhEYb5om_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRZwbfS5XN8f-9oEz4P_nt5cLHoOtVn32kJlsaZ19WhoClrF7uCc9nkZoBXhEfknnd9tGoiDKwjgkgQkfUVJtCvvFnOpt3Ca9fm3NOJQkOynPVMfqZT7IUwMyyxlVyRw_VTStBKqQQelInKksVIyxhhOC7jYKS2-bGffEi_f3bkYhJZrKXyp8uQH_E1gcMyVeAHhCF9ys43eZGLYD-KHfL8MLnIeO4tSNe8GOpY6gnYRtqfPKjRf89ojL5mRQSXqoiNwDQpIlSDN56tqgN8C4Kz3vraU-6ecg7VdBrj2XYWePh6IIZ0iHcgo0_BkpN6-lpnPKW8R8qqn8o1l7raeHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkOhw5WsQjR2QLrgCDYy5QEBEV9Ag5iALA0X0friDD5Ls0kWd84pbyVJICWhPK7OxZPezmG0qc4I4D5ua95eRdZZDU4i5l1e6IgX-tsh5xZnBoqbTvekafnBGdIu1jN0aoC4myQX19RlzOKFmLk4fWbdbr3nPP1oNOBAER4raeSM1wOm5glhmu27eJVXRdJNMsAQPZoITll6dPWIMSHA4ULtqqV0x0WLsaNLHHlknnge7GXt2qZDWSEJFfSGCvhOrSXn6f6_tJ1XQ5OGfZPWWkDHD7-JVzJoGRskDPF_UvQjMDUL16T2qxngh15pQ6WE-r_mwpTWdFX1a-OJ40Wdsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQ5xplvV1h1r5ekWy4BZfc8zQl3BiVmz-bB_D2EHYQ--k5IRrD8yMAVuPQVuFitGQIqYFr4YWWgb--9w0DHof7D0PwvxN7sz8cX6BFwA2NMpo2VFu08G4UTnUoWhUTNvLrFRXhzqvAGAofBtsMhkVVlfm9R34ptah8TtczmSZzaabSPy79AseaCVZGEpcOFHOARXFMEqBELB2WAGlNNilQL8fvOK65vDt-JWS0eErIvZYTFEJrbWwTkRsmq_KlqWb3K9mWdIE9WVRkBT8RzTRqjTc1lo2Hnw47LeSCZyrLhKFnNZcInEplNh0NBqtfFiT50CSbCjlXdSzZxmKqhHfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh95hhdr-5LLrLBxcAmBBeXLbKKDs9y0vHYSspb6D3XEqXFGoPUeM3DpdqH89VVSMRWa1LiENYWfJQ2N2SFH7N35wYB7aAaLQZg3eQmZZCnS57Fdb28v732SMadfZEtQdxkjAzSNyhcrlWkE0FlQoBFaL7Ra2OoElPsB4kTII7Idj-y4TWoAvMgFEQMc4hoNWEZvBWc9ZIVIEpYD3la5tj5DgoJwMMq66PKqchQE8V0d-SPM3yfjj_kFSv-wmx01-L7bgoaL-Xnwg7GL6eLwz5PHXlwfjM2X40lQ_X4BTSpsAX2cvDyLCSAJ_LYHvnbmQwCWLFYLxKTq5DoayCIodw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pg0uXhkOhH6BwB8p8qQ0gD4M1UvxVKXOLqu4HeyrruPriXgu0_HhBQObOrU640SoIc6vlBHKKqBrMVfz3pzNb97jZgYsPgQGSvVUC7Qb3_LEZOkZrltmMQ8utIF0Y2GmaLwOk9WA_4q7vba_P4BTZmdGXQZKoSw_ziulHsyoycQl9wwxAg5zDGH5_TQizDy3xfcjREOs7ZiaFVO6jqQvDD2BTPxQNn8anL095Vyq8-a3oRGbFd5DPDgJc-Lgkh6wOGkQwPdEFqENziDpQra_zYtlymcGfEYas4m1Zvkm8HNPt90SdyYu88brukUOgf1UizY-wbkPT91RIL_PEaiL6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ve_1mJaWLQ5XOuHx2mk2soh1E4AOS1A3SDgzeZipuYzRkPGAXzeq51AP1Z7isf5hwwI0JPxMBW_DgeHNPsM9LX_g2zGYdyYQUBKQdixaxYrJsda0QPYpDbfGMmf90lVQO6AT5-dkXRI-g3N_xgMI1R_K7fwJPBHR3IGJHg6Zgj5SbS-VJiqJkUJZb1JVcsIgPNnGj1_7g8N2zgjNi43uzY3obF0djaChPtwG6o_chay-dLxv9-j3yJ8dNXm5dJz9nEVhBXPlRxJj9YwJYt_6hNoCOyh0Dy0WMlHVkL6WO53IFhRHuUs-ruMl3rq-5Il0xB9CaEFhACiBLF40-qDT6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvD-BrQMCErWoLfCoGZUzknmYjnxqHpQ15lOi6XP4IjH6WV5ZFnYsj2N00nj0_F5ZJDh8XLpCKHDulnmZAqCvR-HbALqVx-OOiB3qTOp__5I3KV8_epMtOveBvZ9QHNJ4gI5ZhPjNIUoLZ3ZbXw74m95g3ZqYj3Snq8R9KRD9TgECdCJYUWGhkhnN9qPF3KImQ9aBcN7OZjHvTPRo2QrXN4N_Kt-tur3JbQKPmFZkt9m9iCLlpEUcDellIT8GXvcBlwUVwUg_s7PtQxpG1coSp91JmsgzJ31PELAXAyDY06JvdIA8b2eE8ismY1rLS-eBbyIR3G5PdrpgG3EYcpeeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C57sBEBilj5Juuxsp5tQ9FDXuAv5rle3FufyXW4sU1O0duCF6obwrxkxqxNI7ertShA7N9TVj8Z0aCzcutqn45jlWuJ0XGhEKGpZTAt4mSr28WWvJQcIEAGXWGjntrQQ5iakJXhn79tiHljPA4jizeA9zpnHbPdLLkCCZh6NjI4xpkIn7ROdotwjSLQBFl9WkttcKpnn1MbQ07L07WF4AnTF_teY8jskjkyHPjgFZPoyZQnHz7TyYcPnlFl3NgBToVF2AWjTVuOkgbc5RBV8JnzDCBC1uUqBhJuxhE3did_2TfQxzKQlVdtL9ZzR-DJzQEJBCBkGlUShQu0YJfnlpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWTfK5BLimTrxZLytFO57gnHDkdg7LnCQLgAYoO_vsYIbigBazFgcnNB1KUlNPFmIUv6MClolU8-Mz2iG1JiCZg_ANRWeAyBUapLxquikyxTzY2KqgrmdFEcUxod99r11D_SmSV8Jp0rdifrs0I-djnXMpmOJdLe5-AggF7IrKFbhTBAQSSndurzSeno4pS4JH3mQMdEYd_Yn-5wONQWizuEiNez_2DOoRC7S7OkMP6G6u7YtvozrfcD9qN1SfK1q_I3fSjXrS1fEOGza5WvVpYLONI3G0ytE39QFRxKRsg7oPFsc-KipZBkPS642Wv0XZLHZ3iNhNWBTZKkOx_66w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=cLgGXGlzq-GDPjTpohIGr816J5e53T5umd1GbbthoCf5yEwVg-t6MZN8I1VppLd05xSoqklZ9qcVFoCZYYqZ3V-hhRguYcvuNuiJKhwrmco3xTXViUaDo0gq994EIuS3s3MqnAehJC8NK9ZRbDuctHHognGJ0OQ_rxJpeHcyDvTPyo6-6J-wnMTcvRPCdxoSTTrc0iPjCc50dFxaGqxvxoMQ_b_eLkjGq4ho4Ss145LT4YG-WtPTDuNEgjuO4t4VHjoFm9KKKs19cxdvYl-dHBTOKdfV1kNMCOptg5UO7FtRATOhKGaAzYRDi5fFL7-jDBlwK8T8_7KCGI1r9cL6MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=cLgGXGlzq-GDPjTpohIGr816J5e53T5umd1GbbthoCf5yEwVg-t6MZN8I1VppLd05xSoqklZ9qcVFoCZYYqZ3V-hhRguYcvuNuiJKhwrmco3xTXViUaDo0gq994EIuS3s3MqnAehJC8NK9ZRbDuctHHognGJ0OQ_rxJpeHcyDvTPyo6-6J-wnMTcvRPCdxoSTTrc0iPjCc50dFxaGqxvxoMQ_b_eLkjGq4ho4Ss145LT4YG-WtPTDuNEgjuO4t4VHjoFm9KKKs19cxdvYl-dHBTOKdfV1kNMCOptg5UO7FtRATOhKGaAzYRDi5fFL7-jDBlwK8T8_7KCGI1r9cL6MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pf9aBsTUVkPIDJmEvhNQLFNBbTxU1J5h8351dqeXwf3UVUTChgMzSwZHSf-fdn524xY0wAwUuy0QPAVTwq9U1qO568lLf7I1fSEXMGV09-XMIyDMhLF-SLkdAL0OEpY_qso7S48muZFhPWLfZAdPoiFJwREYTDUGTTFOUJI6LjV_wBziuKCla9BoznQXs1X881mBZ05qbsSttBcme0gsIvl8Oj5C5APlLHxQE9Cou7Wjk0jtLsbmJ3GaS91bY8QXtg4jTq2GLv6YcT0scVd_JKO1zxk00Zdp_eVGubvD-GA0grCK19LS99rZuM28nRtz_zNU5hnnoNAK0ST76JwncA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHs07TDWWPASXUcZa9dxxK_Ar1OuUapgh-DyplPyj6a10hjGIOjd_lTvSeSxAHXLLb3qNYQumT44SI03gCkrivLsq_RFqrIlVnQwH9t0-zH96aaOutUsGBUSZT5VXCG87AnVSE9CRQNYL3GVJNjZdIeVEf5UF77P6D7LcUuyj1AJ-eG2H2Oipe-FpfpfULGKe_cQJVYVxMv41aev-tuSGMW1--HGEUKjPRMIu5KJ35dR6pcBX0MIk8sx0VsNvm-a5yIF4n5y1k3p34NVg66hI8DG0OToF5WEV_DgIQLj7TwNdB2hMWVmidCkojCFIXNcqegfRSomt0mv_MUNB9V8jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUgCVz5gdSZKiV9zvbB4Mq9CxBBS09MzhMIpo-AifYcFl_vKfLNfKIo9oJAk0Hi6yXoCGFuHywNpSkKoLGDwB07HsRkE8XbLHj_GL1OFYXbeKJh9b5v9wQ9TrzXSah0XKPdRUpmSwjy6P9v-Bly4whZNGnfGcO0_iu-C9pdTkdBRNKkL_p_fdW84giEMnNJL3zgrTwUlECzMiwVyHSo_rWCjjqR7RFbPJw5NsG86D3p31t__4TsJ5ZIU13I__hAXPuwCIRohCOkPPJqLukZ5eoyKMzp2kw_LZODISpNDOWPm7o75XeiZyBH43dj5k_cVQ7ADn7jH2q-IdHmLd7EYGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtsYvTkV277HcjgDV5o1Ply0ZUIPZy1wHuKhsr5ydn2nGn3dEZ8Q4LDGPp-9q5RA08R2vqnf8-xzO0pEZNzWCRjpnymY0yqfjNPc7p26vZIhCpKkSm_lxHnybDHIafsRe09E2LlTDiCaosL1AE6Qm2wTiJ-TQo2CG4ZirTg0DJMDOwXo27YI0ebIRSKKiVBBOcmkhIUe5Slnh_5QjpdFnqQD1xwCHwl9WGYJqUhuV3pSvrgmororTdrfIGmXB25uqh5DdgG5Px1S3oTTZyrA5Jvbz9wDstfJiYeqgwUZOuSHzcvAPd3yF3QyEKOxVqDy-8c7da3n-8KEsaGD1LtFTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ph3Fr6jD4Dzl5TEc6ezYMCbOf6Po5VUC0o9P8DhiEfaA5s52tto35mJDo_--glB-_-GRUwItLjJCCcCHSUwYCfOdc4bNZ90GV8JLnENMYHQvqyOdEAMHAoBKsHZxojFqVQhlkHDBs-zksJzirhA1lwKEOu8vx4iLYOB5eGo6nF0HDU9IRVrR903WyemWUXKYRi4d8JHbFxp8DSZnNHjn2CN4eh7ih4aUdZWQdjrtmvyulIeVdRUHaQGDQL5NTabk1Xpm087IQbv_UiJBqvjJgnnOvBsQtwLLeeIIS2Li1ifIP_3hs5pZIeqQWvB3esuU5bBfqXNaUvFgZuTXAUm1bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMZzv_SgoKTKXjwxREEPklBRsv4v6plc2i_wbY2bn8CunELmCynnzkOpgZmycEVck1oheho_5qyFHF5QRMeZV_1l9HHBdcdDJa9JEDDXrkkKevMofbBYGNSv0UO4wUmTvmG4FmhP8ShUw3SWaySMm39e9VGTw5x5BdInAf2Sg8bWIReMbE5Pc29tbf94Lz8mSwOJbTQkBGuQY0KcZUXggwNQ4cxyoBPZW0WUjdTPKvv7sOPpAMz7b1ZMUy7cApj4EGdm7Bw5gQ5tqznF-KQq6c6hsYuQRSBpGMQcr5cdpo_HrDyEQmNXzgZxTjHf2kzqTIoeY2l5f5JnKZW8G5he9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFkNUg_j7YM6UxiYelSiDtyCfE9OHKhd27YejZiDP8GudgAm2hR6bTt2eRN7EoXfuSeahj9mXlKDFdjLe_JzsFXPPi70vk3FVMKk8Zqd8pEAvTTUloa3J3qGPyBbKUv2vOT4vkHfgaqTZTvo9S1xHVH_N_WNXzaIVc9r2SDE82hTxxb-WHfWObn2gLvNYeFUfRvOnPdr0ghcsuG0FIYLzRK6OS7XfcFfimBJ-6wCCCo8qDMkjyyCeuBAh7Si26gFkcVU-vopiTYx_R810EuRUaGmyubb5WL1GUxath_BSIyWJNPnvMvP-txQ30BNN2PSRxZidbfzBdLZt1JVSbUkkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=YZqkgmD2IEAwkL2U7uGxIEYpM5lJJlpejTmrYuarPD2naHThMpQzOVtjsipiKCUCcvaOIHMIGABU-PP5CwDkPurW1GlKjB9xI4H_X4zALLhyuWMGC003hrb4pAanCxcTS6Tcz_tIQUw8mePd2aTn5zNiXte_k4oMfM4QTs6cobYaDQTeMeHdjojU5Io04_ikhg-NpBtVfs4m8poJbK408aDxYtCXXxx8pWqd0tw__xkHPV_ZTilG0pV6ajTkein9nzeTVZHMahEpIWffwZchPfql8EjS18v8uSMSeA5JtxehhSvzMWRNusM7BqU1czY08eIPcZwuMWFpWRcTRCsgUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=YZqkgmD2IEAwkL2U7uGxIEYpM5lJJlpejTmrYuarPD2naHThMpQzOVtjsipiKCUCcvaOIHMIGABU-PP5CwDkPurW1GlKjB9xI4H_X4zALLhyuWMGC003hrb4pAanCxcTS6Tcz_tIQUw8mePd2aTn5zNiXte_k4oMfM4QTs6cobYaDQTeMeHdjojU5Io04_ikhg-NpBtVfs4m8poJbK408aDxYtCXXxx8pWqd0tw__xkHPV_ZTilG0pV6ajTkein9nzeTVZHMahEpIWffwZchPfql8EjS18v8uSMSeA5JtxehhSvzMWRNusM7BqU1czY08eIPcZwuMWFpWRcTRCsgUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RR9StyrbCgNxqo4YjAD_xyxDj77aNityX0eoWWsx9r-I7ZXFUllm83vyBNcb6H29V0oQmcOBgUpysIBKvfvt1mWMUQpVxA7ZoWz_BNKLfV5_lo1Nbun0Hg8R1DXIB3XwSxbv2ffzo80r6gOVMXJwrF02IydAcU2N8zQE5an_Xo9L3QoVQthW5V0nDidpkkv3d2dQZ7lZl0gjFjxOiMi80QVsn_oBR-4Xq5BWHzMTV6-rqFHhqNqB1FeeT_qVDqaCMMFde8T7k1HMmsYPiBF8gAr8Q_bAUkBOBE5UkHhbZtNuYqyos3Z7Yunnaf16KSNXMw716AALwckAYYUILTOQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEr1VRvKtZ2f13UuN1PVbKYExc98d7uAbdXhHHx6PrcHcOKnlPxMMskXhfaTOV1RcgqWPvM6V4YNa_x3ctl2zcmefslrJuaS0rosXXYSrgcfDlyx7q9hQaFy629aYAmeX4aCbuujUv77nlbr7y53AHn1ZlodRqx4gmgxHtMt0iRkhP08NZXexLCagzpyigIDscaQ2rYSlHJfqrrP_W2I0exrh_UU3sklmru2TLCEK9M1qyPiyC5ioPDWzW6gyukwZxxR5uhRkfLJnMP8fpI9G0-aqRUXVXbUcV6HsQD-b0FtEXqihZgu3Pi5KBevyx7-tnqyNQ_oU22DHT74zH690Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=H1OkYh2QG1mH5J6R62DnuUoSi5vgIshhSrMWVQunFfOafvbswOQg9mscug-V30cLv64DVYlHCkvzPVbm5DzxXrSYn7E1NHQQqN24O5AxxJhamTCN12hYRV8LMBMpmf4R_wZXL4okSImbosaAC6NvQrPMkzU5zGvMaCGKHMsQLRlfsIM5SktsnUgFsrUdf_qg19EyYqd0tDQEA3dRWODuQNzDDPJDfSLLb-kj2ugBllhjskeiEzGN0rVC0r-dh0ip732OYCtqzTh4n1BBuD3BZ4C-qXih48tMdGhhEfgANV5s1nKZ6ls3cfLbfRBNdJK3R_P2_tu2gJBBfngCqkZqKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=H1OkYh2QG1mH5J6R62DnuUoSi5vgIshhSrMWVQunFfOafvbswOQg9mscug-V30cLv64DVYlHCkvzPVbm5DzxXrSYn7E1NHQQqN24O5AxxJhamTCN12hYRV8LMBMpmf4R_wZXL4okSImbosaAC6NvQrPMkzU5zGvMaCGKHMsQLRlfsIM5SktsnUgFsrUdf_qg19EyYqd0tDQEA3dRWODuQNzDDPJDfSLLb-kj2ugBllhjskeiEzGN0rVC0r-dh0ip732OYCtqzTh4n1BBuD3BZ4C-qXih48tMdGhhEfgANV5s1nKZ6ls3cfLbfRBNdJK3R_P2_tu2gJBBfngCqkZqKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGR-Q0q4eM_H1-iVp9AMQp8jJBn_tXH__sfaEDQnuM865hQw8rv8HNNB8vZRmbVzX9hfpicP6IcrNFUZNuO6gXdOjpnXBqtgKI7IQJlecgzO6FChopQvaJ7qn1_rAtZcjOn0ANRSHwKwLzOCjbLaUva7T2VYbP_IqneLwKQo8S9XVskuxL0VYUS7J2i3bbPUhVJTwmsrZbcFLfBY81jv9FM3ObkHaxSTgS4VCSo7a7ro-Y6_mStziEK-dqXLbT53Ano1QC3x-AqJjMshZWyiJV4WvVdwx7BT7_rbkgN3VEbF13JISvsq7C2sQ1FQpflRMtieo53e5BSxy-TAM3JKrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/NqRgkv3xcN5rXdmkitKBBN9ZAAy2GmRqsStp4StCSfOAZYxGxR7OJqrl5gf5yx7DdItrLTS9rMHZQ4fcCtseWkBKi0HiiLnOC0RX1a1pqrDFnvGDp3AwsWypBhsHvU5Awc_UAKOQeJI6HxDGQL5vHbujMVSSNGbB_0eN316APgJEWzTrURthVghk6BRJ2NkRlBpT2KeO0Kg6cCgkn-vh6NJjaWsdU-A2E5YYQ5nqGUSEZs529BteE_VB5DcMVmsh1gZhkjb-R33IvloF-2HcsXFlMqjkAJuDnSuLg1xVGWH3QWEW8Msduk0DOlRIk57ORGeswuwXKYxMFW7LdX0XvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه درکنار دوست دختر خوشگلش رقبای بزرگی‌مثل
امباپه
و
چرکی
روپشت سر گذاشت و به عنوان بهترین لژیونر فرانسوی سال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ym3zC2abjTxexhqYQFWCI5IFBF07zYKdtvzS8l00A3s0MQcXbhuE8TbubYdYF53A9boGVkwZ1ioG3pTbJ-NvNyujGvuZv6uEN93ZDYKvH7tklyqkxtvttpjKYJ4NuoclAU535y64x7UYnmGYxEi01RN3N2pVLrM8rFGQ_ZwsTkrI0apciiMNDIrT6y7-Uczo6sMC69VCYh3cljFfwEkSovytZlZUBNneZZO7Wd1xROX9wFwKY-vKKw9NcfLiGa2Ri2FxXOpre7T-1x6wESO9qyVZhuMEgjb5wT8mU5p12rJVoHv627cosBLbeU_kIUmSKZBQdP7_1xESiVR-MY9PFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0hdYrw_YXI50rZg1ChArbzYtLke-dpK4zCwL-BM_tYFjkLFfsy_uPwIaNUCVJ6_hfGETriRvmZscVHbhBaQjlSr_QT9LvKBaHWz2SQ4tspSbeaz52dzZvaSiseUK6ycH1q-SrOL2sFNHMHd53m8_77xEC5m_YaVSvftdcoeyyuYU50DxVxom0VHoTXV5fbM4_p3b633U9eq83bcjhWzpctElLXXUyOwuG9bcI5xZesnhbTpfimmrH1zkpA-BT06CTc_slG33srcVDcLNjBpk2JrTVHc47QpN-Z0ZXFjxKRVuOCT8gV2pnrHbFsv2b2_nkH_FtWi1fOerx_5wIuGYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtlzbRCeSVqBpcUO090d6UeT8BIIVPnBfEtLp77FBSs5xq0_tbL7MF6OIW748SoA_6cYn_ToODlGhYBS_xXdiUF6rgN8_lWbPSSrTm50O_nshcwhETmnKwGGVBP6CpHv9IKnOJcZYKhld-n_8BFuHLk8Ic4ZbTmj3ZRbx9sTNcbMhYY8H9qkVc7mO4gO1_60DiwMzaZL08TgnwFRMOPMITNiV8w-svGq8yVAGbxGRep1gXMnHaApxVgkl5Z__FTWyyF5z-A6PErXi-ejRxNLnZH25YFxpISEwdAME3cfmDPBJi-vfrhIAw1fYIqdxJfCWXOZag1TFxdjz8PhVmA51w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQDADywBgOgj-HSQfhESqBWpocpuIk9X89KynlmBwUUiQLh2Poam_H63LrmBlMUVp0o2swmLUTySKVvaRqgqiPYM7Ilhx6ULa5WI0didrJVhGj2bS2tBHsMUl-mZ9do_gG2JKq_wCBRBkb5ecjUZCQqtC5DAdGVqQcSnwPcElw2hOUyJ7krhwtPdSNWaCogAICWE4LmGZ0whBP3q7myEXIzZz0OkPtBAhh2szBcYZnXY7A9Z_6XoefA0q2FgxZoCEcEL6WIm911wwwFE1yLqKqKBc9199tkQx-M61_K4Iw3gB6El6RAdzJ5FchSrxyUPMaBl02P4PcPYEQfHPnlvgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFGYO7OmLkKcFXvxr8MjGTx7U2XBk_ahu9DaJGlam7T2wY60AfD3IurNKFXGSyVrzXWwk5InaOTrRILSWSPYnuSN6c9tPh0ehtMK2ABmLUpZVTi7FyAf7HlTRmvSK-L1aT10cS-FNwnFDahZkQH5EeA8_16c0qDIVcT8unJZShS6y7slbHchdNCzOHx4ScDjYZ9oLq1_1ilj0BrVIumbNzl9CDLYtMQfHVJWG_Ox4GyVDcG16GnrKK34HU_PVq25NFGJj1WQjQ1WjFpNUzyYycWATkSzTFYdrulj_bMdB34BPRAiH8PuvHfNJgZYxGnwdr3MQ8_5Tg4K5XCs1SqG4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHE53y1U1SsSNJbanS2slFHsnAicJ2vWMd18WjhNUnaN32Hr6hDKe30XviowvRu_VkMlKCQX7NvRIoAbCu7F45OAsWCO1w5Z7yty1D41tMxN5Eu7s6SeCOC30VjFIkl5SuclV62NCbAaB_ooSPv9IQ_G03UvcIg5IG5YDeZqxlnn9MTX2KF9VKTPY1XKnSS10TSTECyTlkiiFdZ-zPFESYmjPiIEjaT39L7E2zEFPVRFy5FzrecDWGsOziJAQVKj4Oo9Vdlg4Tl6um9EVlETRGoacaUeT12Al7MNuhlzRQPNB7vQxSUTQHWXoyjQcNHYopCETwpHtSyo-JblefQLhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRqLla2iLhYFa1aSche4gt0xInBMhkhI_2scF-uYsbrl2-x7yvn6AbyVRaOrSJ1XkpExB_TcfKdhcLTX0i58J1KHIDyQe63UPBTVQLynTJKO5CK5Q5as5S9V79EgOlnxIVwplTm24hKS-NeVPH8gUIgipCPELU4A2XAT7HyL5w3A0WNGXlRxiAi2BIXNwR9M-oeHXsl7kVFN9-wmaBAVZYslfO3cOvK68isaqiicAPnGJGY562QwWucCWqHS0_mvom4cyJWTy6LYbZuixZ9sbn5tFzdxvqFLAKPUXzeAS5x2n71Sn4W4zTaJH0kSVFt-C8zHzLiCmgcoVhpzNfXd0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0SU6j0TE5uMjXFubpPX7hPac7lEe90tdPeMSoULubC8NQ75AaWTxawFVqrH8_9o-I8YAIKjLWfveHbqFNG9Pxj7HycFI33fUvuwAo21jVQpGm5L1uT_kw-M4yx3-OOUuD8CvpePXmBhQEC9f0sG7elhgm_E4CV45VhRhQYMHybSXXXz3Wl4z_wwcNt3Nw4u1tbc0RuTAJCB2hQKzHpdGkb7WV7eemNvze2ElRl3ob8Z1cGjJQ9f7QikWxcudrK27aOgR0sTarc7TdCH5j7E6mV9hJ6nGkY9tVKUwem_X972HzOP0YAReok7ZCh1d1usmbyZsJwsGEp8NnCEeg8jpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APRP9L6d_Iq115KK1iat6ltVjgtp_s0dsQJ06lOlE7IbjPBFYN9kSRJyuXFZOuOLbn6zhtUDPZgIhdOJymiOLrDU6W-kuPRbstRJk5SH9Hthf6vvfZNfPP4xcHU23Wkz27TJ38a8V0OgBKG9HEzU0o1hiW2RspkU2AVDxiPuuA53jQ2FcrfK9w4iVnhPzu1E0EjV4EEPh2hMKVVG85aa3AlwoPRkzBOeajS0ifssz6aYXnxga6dlWo5zRcKNVMHS5DXp5GjWTG1T8zZr_YAcc_2BSmI4A6EeGtclb0U5yXaU9ZKUrV5ppslTD59gm1yGFPTXi3tdfdCq7NZcM6yvUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2TwfueYqOPMvqHCWmiaxvmlWmhkWtDMVHZ92L_HBYtBFl9FOmjt_78rRqmwMe9gGJKNm3_AwxRk0K8KaON3RoUepEdY-mPOBrjvRv_zpRV07rx1YULoAesXLwQ8UAwy7B1uJpjhYdL77UopIaZUS7fn-x8HdBIrKSgBLJkiC4s_HZmM5kB7ArES5Lv6cQ7JdpNFS5qOp10l7ekpP_DRLTg8MJ-ITKhivkeM1REPRv8VXo3Wc0tTIejaBKTEGwjO_8jrpT7a6sH92X3K1ik8HdrfhDfqAGd3sg-CCGFlXPMPSGj1c4irPb6zGlJGX2hVx7nR8FgLmcFwmO6Gdn9dog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvJg3cAaqPiTfRlDiaiM-stXAoSex40fPO1yzJY7w0mGESo16B7hwU0A1ZU-XMui5ZUewV80_2vhXou4N4t3w_W-IJAu_Gb7azwV1Ucgl-PTAV6kgy1_ecVlAzOn84gNZHvyEj2Nl_EcXj-mgXEuV5eT3qaa0FmzAi6mj_iK2mBQ9-ZIb5xN05h1_HijqVaF5fRDLMWXZROOUQmBS-lZx-vh3w21Mhr1DrjVXihqRaPQZ14yIWt8rYd3tw3npNULA72hNKYbgRUEsGNHMBr6xxGuaTvdklD-B3sefEbCLg-n5TmhL0qVsJy336tfvnNOgKRZv_sliyOTHzdX-aJ_ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqCjXC9TefzgRMj-bCYs1OPVEOETy2Q5b4oiIXlUMce4xt8XX4QSoiyVv4-fWrxiwij29_co4PU7LvZzhgOEJ35DTlG-7dfPOcn0VKoB19P7JYKsiPqx306yYKj9RsBW4WKmuBCo_jW9-NtOnw2TzZApckX1PROk0rDKnkhkPICgqdHliIQ3MYhLsL2dOdv7MAil3tZeH6G8ENz3QU6MGcuwhQBoeH6qAdcVkz4G1ZvS6Kz2FMu9FrixBM7ug8C9OgvQhOqjSZE4Ili4obbqtBCq3NgloNUd2tY5roXZO7_eEEsvDgiMEXa-Ah0EOh1BIklUy3W-cMXCKaTQQFSf4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=DOUfdvTb36jpQSsH90sGH407WpWqvxzGwbM2AU2W3ih2RW9gn1PgmLNjbEoeLYYVknZdhjlZv6MuIbRVWdDS2VbXf1etG1DaWjer0qmEP0o6wUv-ru1k_yX1Yhdk5bL4nWu0z-ruhHC_w2HhbYM6vMFeTELDpBY7NNXVxB5Vw8EP35hMLu_me4YouElZPDyE9z5XcFyVWHklMmXQ3swhJbvL_3O2BXEihBoGN1xQqCuLd3BY19A3XiMHvfRNSkQ6AIoEIAzCPGcxdkFVZzMkoV5Ws_NKXboqZdglVx5Rem_7Oxk5hsWEPuIPeW4UbrPKa2xyVka7LeiyGgT20uV6_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=DOUfdvTb36jpQSsH90sGH407WpWqvxzGwbM2AU2W3ih2RW9gn1PgmLNjbEoeLYYVknZdhjlZv6MuIbRVWdDS2VbXf1etG1DaWjer0qmEP0o6wUv-ru1k_yX1Yhdk5bL4nWu0z-ruhHC_w2HhbYM6vMFeTELDpBY7NNXVxB5Vw8EP35hMLu_me4YouElZPDyE9z5XcFyVWHklMmXQ3swhJbvL_3O2BXEihBoGN1xQqCuLd3BY19A3XiMHvfRNSkQ6AIoEIAzCPGcxdkFVZzMkoV5Ws_NKXboqZdglVx5Rem_7Oxk5hsWEPuIPeW4UbrPKa2xyVka7LeiyGgT20uV6_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uI_Cb4OyqPamc2GgLqGNMwrzmi2ctuJqZgrC-QHMqw6la5o5e0Wkq1e0cimOlQM_nMCZX6tnJ5R2we0JS7Z0tzkckSZzSsEflwT6CfE4Rv37CAclbbUE4rq9YL3E7MzHujgiYzCrYm4826LHpcbezL3-yPgJpPPVAnapV6H4JEQ8WsTJY-rXqCOaMq9o2XHzEKs2HZ1iO9fLNioSZ6nGD-pX7RyEifyD6bYKDJEu8BjTR_7dms65I2i0aY9vXQzgWMgMCyv5_83Lu9tD6KicuM0f8Bntjy3-vbnJxTW4HwcH6nzUVuVMNJBLbPY443RSG22ZyAHN-AkmxhC0loULCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmUCldRNyzVUayGS2a1WBKjkEcdSQbwnOo9EN7765cKNQa_gIOkePqpMCmkD8oYTgBFyIGw0_TMCYxjm4ZMVCuSXFMc-P3IOerpQfT-dWbipwS69c9rQZq93yFOy14OyR4jFCkITaJjT3p4YRMKUoAzY8PiIVpg7FSN_EtSV5VR1BOronLIggRqSe5M-N9LI-HI8F55aEPfh60PBimTgk_u7DGaFut2XubZCPE4hiLEIwf43m1PopUmCB0alqPxyZeDXtUV7SyUuBN7sHHUoO0uNmDXZ2gd4tvPp1e_fiQ85DekoItXRWqr-VqP2aqvawdQNvl8pu8f8nQUksMTQQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNMzawBPc3KpmBz5fIQpFjfQTs-nXqlIEr3HkLtY4fTX6JvJIVduic6Xz117Gz6mX6P7oIuZEiZMovtI_yKb9p05ZwBDhmGsEaKaQTa_ChrZlAQeR5dj_SYN-jJbVLJ0i_jiKrqX-deM7jhceDQ-J2z8c-bPtgPkVsZlHRuvBLw_B1tVc4MCKom_h4KtPsZD-hgQAR7ZUjU3vsX81ATmgdEjWuWKgUagbQfZBT9-EimQLuLgRjNs5KRpwgv_knADKeVfqzjpheeBG-p7UAo1ptzI_gb9NnHT1g7fxDgowMk0jxtYEut3rYRLFqGXNV48iFDrHZMbpS0R02yhQyoNtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfzpRguzY0cbAtTB7WjRpaGwpKsaBPKrFUPf73FLnIr9PiTUKmqV5e_qoPIioJu2D9KG7_pJnuyYkNSaavVlYg1ft90rpsnhZle7oJVNohWK-bvPNzl_HUEgLSCS4a4X162SClyNH90lNWVBhYhh3nKJvGISyNB2oE0K9yoGYl67-dXq20RyPUp7r2Tb4-v3yKuqCdpooFCtVz-8xKRjtlLPG4J0mTpA73C8kYEgQrLw2C35QPWdf0mdV0auM_f9Z6Mj3dKKaW_eDmsDmcMwtL6NsSybdA_O-g5N1oxg0uLEZzrXP1RDemkGZfTkBGZFkTQJnVbr1Ix_eVb67xvV6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKsPsrJX40AXC9nWHZfI3jxtWlLpWcDbccz6QsdX0h6BceBPff1MwrjHcz0z47AU_RXB67jCiZhQ-qL3b6n6UkxZsS9rDtlWG7JF79lYo2pDWCSt1Mvo2KhmztaoDuQNlK8w39b6NmLQbYVfZ3w0ICJhYyVL1phQXyIX0LbBdWJNFtFfuDkisWe7sbMBx2vlQfTb6ub-cgN90KKdSG78nYOvLg2tYNWw_xLzXlauPX6NfJc55iPrkH2NdabCelwGJezQJ98ZbpPyHQKAIb-YF7dDUxiQR9NdIH5s5qp4hwfFOrnSkW6b-LGBJ3uuKvHWCFGyTLK7BmPopcBW3fNfRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnZSRFDLChsxXbyf4doslAmeo09J64qIXPy3dV0ImcOHPuve5RfYfkYJe1qo7lJy4TDPu4d29qZfBGW9XFMeGjmXWegmEUDuTwFHXPzu2kPAVXS7gOjz-SRUdLz_kJ-PRKDMWwOJeJsjEio0mawiAYR1F0OYOQWUH2ezmsN7P8tlkbe9yzS8VSGTpULsy0n94GpAIKiykylX_gc9x98boTAsZ4tiXJ2vh1rZXDoJqQs29leux1jadslpYza_8no0H1M0JvYYxkGLk7Z4kqfr7fMedmY_mxnY6EgTznnWF2GyFXdex3JcQcvbITQhM2QMAe1_FA8iJumfdAqyUBH-Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVmZcmpDz_FydeXBbGs9iPH9w3dbNEUplKGV9_kHA0sOmkcG72JUnJzejyKXIhD8t6hqJw_h6VjGxDvCVxP1SvTHl4Om3n2vZupxEExTATF5JjnwkWwGHSCw0U6C_X89afFbxnWc6BhJnKM3R6NabqYZiDB34JMZ7JAJfln9BYTxyxVQQqapnPfxxG3zFYZnel2NEhWVsZ0gwV31NpkPbhAbZiC2D18iEJ8AQhjMCSI-5MowbvdsqHR5WLr3YkCw0wlZOJuRRGF-lFZj44bhhKzwR6ONB3T6bZLAYTkPXrelywsv0q5ktx5rFLD62TC79o2lrMEc6nqAszUF4S67Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVKL8MFbSA8t_CUPRU_6ud2YQa4V6c1E-Zs4oJahYt8MPTvwF3SUqnXk26ekoogiKlOBGFGkAA0sPPvV1ES2QC-eu1OMvRvvjsLg8IRiyMXhM3uun2rU6FDubpnp6G4lL_QNArRAe0eT8FVpdgr4h1Vq-fwUbfFGfFt7KVWZs-wStD00JYKANnRYmmpUyQMJ58MLwbyqDbcteaDBhco2YYabqZYUgL3HAYrMSqgv79KeG79jDiQW0AzUt4BJWFxyLVFNXkJ3Uydroja2SOn1Yr7AvLmB4pEXHSmibOs7h6qcKYXmp68ez4XunkOuBtQFP4E0YqIikIgoiVkmaelo2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvR1rPALje0mPp7t_c5YBt5cERwSgCEc6N8-0s63TNZi2MIQ_69AENSVHdjd1TyowXU9dWWd4zi1QIfcMqi9SuBxRm8_JESPG-eiIa-ulXvA-2Y283QQY6YaKVQUNxVmrNHi0wz6vMF_bm6u_uC9LQ53ov_zwlxhxxTFX5QZTtOV_k9JGjksyKJW1APyjIh3H9hpm7-Kyv_2HsCvogw5V7HjdhjjmEfGlmG_A9e3Z1DrEmR_cvhqZn16pwUfsar0GMY9na8JM1W7Kg9Muot1V4p5BvTuGtklywaJ02HRNH8WjPPBMB-pY608sn__7Ax3BOa2AV2CZ8xvHpA8GJ4GJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOg25R0SXow3hVMWBuqWzbNkO3TtGO-Vmyt1lowEMKpvI7hadXMFmh5oTVdqLCzQb59ldW9eP97Pknf9SL3Mz2gHloxsieJLxOK2jjjYwlvXIiFLkshQ_oq9EBSifR-fIfNm7sKtG-HlRFeG00dOVWujxSUR1_tFQcL9picJlVWeAbWFGORUywKchUApxTF2d2R57_jfVlZ6x4cz7gaUevvL3IM_VlP_bEh4dM8We8Tr6V3mtS9s9YBo6Ub0V3LM9vmL4b8zTCAlBs5gdl15etSbAZ5U9ihspuVLv4wp5nwTvkPplN8BbZAnr8Ks6UthfWoomAqVNGKxhmRLZ2ma1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlSHkbgcmum2PT4T8UCREGBqmDJ5byzR4YEp0LB-H3hiBF-i08kBcfwTM42A4Ek9_BDuDEudLzu5dPTHptMdWcHOt6TDoIFGrouWHSx_11iNNsu6hr6cVtHUsaUN0Wri7SZlo_pt245g4yLg0WRciKxWohWcHt3AITskuihoLNzA02dE1fhHP1VHijJYtZ8QYAmhECuJwEcF4IapvmWJ9ve4NXVugkrIexMf-J_6P_CU-VGHOjpiN4RfhPUr_GyswhX7A__r1SM9qMUlmJN-YOfJMpvlxGHbodjAWWpyvpOuWZigPzqq_D2eyUUNRaimZEKeKGSomcrw_3RkLiMy5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4nLygYQu3MOkLdv9C5QtuLKXNOc9KLD3KS5AK-0FD5lj0Wudj_MEu6ie8jWmIH8h8x9FZ5WhVOwr0AfYfs-SWw-e6hgQqDy3VTvyegITnHXOmFvu-ga0URPHOpD1Ri_vc33JwVCwOfnsaKLaUhpsSqPO2UVi6gUKb7yB_kvX_rfndLjxV6Gb1kD1BmSVRiwVSuE18PruaDZ4_hRlfnvHh6pzkZpo7VyLUhz6HORoyPW07coeiC8FZksrz0Od-uwXfLnr-KR_89_rByY0cnReZ5VB1Q3e3Kj3Lw2NPP_voALkXQMCeaXjeIitWSKXq27Ss9GQbUxoD7J9VVfty-qUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEzeIShSBiFVbfHF2rirFAdPsZZdYvPmRHYZN5_r3x1xR_YR5lN1O84Wqo0507U2ZjXjmDgNiAgAEc3P0rgJCtNilEdaD-LM9QE3Lyr6_cwoXskIMOoVKSHWhFrUnEc9AT3Do9FPJJkQsViWy9MpI-xj3TQh4GOyfUDW5Qb07H7T4hFpgnqYpN_VMtSq2RgalvNj0EIVA47W6xuCW1fiag8vOr9ioeTOakdOyVhsHfLiI1NpRGyMsYYkjBtCRo23vEfM0d4yyahOVsOtwLxbvaK7LwGw9TnZ22nkoBfMXdL5P2YzH3lCMKB_2c7c0xeRKjaQiQvsikGf9uldt7SbLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFH_zzyxD0ahiVdKR9BZbSkkGMEAge0b7BDBD8aP_MD_F2Am2JGjCVZoy0Rf_KqAJ5kJgl2Z07sadOeOJkfUon7oIlY3M_VufE6nXWGtBAK9mtbZXUObgaGgRcjqxr-0iVPeJo1q0Rclp1xwWMMGhJ4p-oMCyyfOF32KqOvzVPSamz6K1dQhlicJLvrlzsSBUs_mO6qc3UX9jx6vWwxMscCl9LpuJiHBiB7VCIYgu69f1IVjZWH2YOVRfkDQe0rzhwQ-sdNjx27_CBrKSsEQbyspWx4A4z_WOKhMIgJl7UXC_ZEOms4Gw3NsM_LbT-9zJkKHSFXCq-mDScu7wvxXeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7FHKETXS8uMyiWPdMqmSv43KmLgK-SZ-aI7LIq_Paz55rfHCMCA7bWogwmEUEFZvR6eotyz8wNz4XkdGVCotyKZlXzwnBnZFPt0ot5aRK4WOuOBlwAlBlGAxvQ_h8u8JuF-DfcFEkmMWhbMm09RsYQzFD1kUqLGFBWhQeiWBLK-xPcsnnzFJ9k8m9M2-KNgfhoeq0V3KN3OyubZJcA73veeNHe1XzPWTSmth-BjKe4fytqWYtSNBSdtaYAYJBVd1JNaJ06M4kDcsf7jnky7rEQgLtqUF9GW_4q0aZyiKI67OnY6ZQT3t_TCJCmpjYdTxlsXMDnGXg62INbckRgy2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUotxQA183wKj-aFwfqno7D9I7ZYttpxzVZowfYbAWKe-bV0JPEvTsVZJ90puCUPaQJxJ0sGp20Og8ucNUjWs0AcEH6o9tuX0XAEYicnlX3WrfkgceRttA0MgY6qkfR5of5pze2rufb_iOb8dJcllZecfYw6Cuo-LkRt5E4LY4mNFyhM6pSFxEqG64zFA6_YEzFk1IA7GffCoqtiV3RJxjzi-ak7asQKCc9pPyVDEjzAzI4jGJnDV6b4e8pjBn4qeJsCccea1Y60Y5GSootgDYsl46CoMnQwZvSoSRndcSa102DHXtOxT3PQI6f-knkV7VgjBabsGt7Shxm_i3DBJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT5nmxg1iAUnpvMN7YjirGBRhpzjb6KsFZs43pdkYe8NZN7HmcVit9s74i1Xwg8-TnO2Ot8tTYlCP9L3MTYylhrTXDSeK2lPj2dCKD9OPaO7qFTbmjaAc3Abia9cgm64yYByqMqcxRoP7h3p_BL9OfPGosllcxRITP7kFVyl7bmanTOpb9DphBx51GPx-OUJaC5I_GpWFw26ZHvWlZq0QT49DnXzKi1fH25-bwBaJd02xTtNjDDFA2Zig1O8Jyg1nI_1fzXPh3DIqNig9e4hiYsnviqAvykSF-nWu-_AjCBB4y8P3jfLtNW226PEE8PQSX7pH_af3RPWTuAA3O2bbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNeUfMnY17rILQL1Dv1ybw9P0bnhLPAgJqC3WiEbVJ2Ul-A9X5XMmYg3NASjEo8IQtUdkmHiq45fMMkg3WCOWIqO2XfQnaJNsEbSbOxp8vjNstgNpO5vtrTXjljiQGg8pMpvfVkEnymacZ0L3PR2KvKcNw2z8y9MwgN6JVe9gxXjyovYyZl4dV6sInn3QmgkBrE34oGKnYGWVizA0AI6EEEpsXjcDeD49NYY2VSgrfS4Oh4Ew8tX3q5gJ9QOw-lOajGGjWeZWrX_t66bXMRyhARou5tWCd-cth25GATrdHuGUbw5yhjoEGlQTYScQi9ytTJgNPrgaQK7178Mi5eXKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2hHRrBNNQbiMupYUY7WDXKRqQXBqg32bXVoPI_oltZtcfADmwCQPOuDrx-e4SFuf7DnWRBLRFQVTwGy84zyYglGqDa215Lv5FBFiBBFBx0QbgiJSadUjxk3Jfr7dBbvML7fR2PWbSjOTW7t-MIHhPOY3V0mNm33zHJ797Z2Xdrbw1jRoaIG4r4w7Ou_HdjfK_aVCx3LKBmc6lSG2GrGmIussaaduKHPdSapNW5rG4RmgTPvbO9A2n10oRrM5fQ00tOgB7uVVYyFtlgtVyRDphhf3VIjTcuh1Hcm4oWKqsnao_34La8UPWzruP_2RsaQJJ5OMGZLKwbTHLaz-rBCmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZ06mNW75xJY8TXuhYipXUQtbG5tclYZIIKSDqDWate8TvQxDgnzvTL934KUfUSzNuqadDn1F-TSiT6MnMxLYNYhplG1U67_EmP7Mrl-P_Xkd3EwWJ0Y5d5s4z7EaKaSoSvN9MHthmG1PMIr8oQYG_iXSYow04EIcW2eyUdzVPoTgjzY-cX3TQjValWhvwQTZJJ41n9I6_Jxweh907bqkSaRJOyqAIFJ9_EMNy9EBVXC9IkbksIDHLniOfaDys9w-w6QjuzaVJJcs4Z1ggxTDSvjUH9jnCShywOG0QNsh_AvxNi2av41TNmzSRLqhZ6hTWpuKg3VSalBmRRe0htTJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqnD4zb5YAI3e2jgChDDjs2tLM0sWvD7ee-HjTCb0LmQ-lZ_QH3Fmxpbb4L3qAUdpC4tvhYy6U4TwvPfV6RTDrQVayaR9WbUgLSt_xy-gq9uQ4CVVe2hg8a5NijZr83lS1EVkhtQcW-yOnwDkqrzm0OTvyEd2lmdupCrAlBVkApyR7QKSINEVj3f58NrcI9H3mofy29w6BxDAIdk94FomrxUeOTkK0d6pN0-9BZxRu92_sSBmK-iPH8vXpGwK1BCwmGXCK9WZpb47fzQLLZ2lj9EMVTvxSy6hq-KVk6XKgscWdSY_SwvYlTJciPKqZFlkPd_FfDE3v9zmGDiBoYGDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛ رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‼️
هایلایتی‌از عملکردخیره‌کننده لیونل‌مسی در بازی شب گذشته اینتزمیامی مقابل تورنتو در لیگ MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5z441SR0LWfVf03Z2AvJDrlcbYfy73YhGQUxwJlD4m7TLojbq37c9318daKdAHE7gbj58gGNz2SuIWUS2ZElWLOXUKItUweDDew1A7GVu0lOmgDZOnFEBDyS7k4qyoIWDX-OdhUjqE0_PABMOhdSpnCLFCXehcHODq_B-XGG2MheP9QGRREcj8UmjesKJL6VRxj74lLUK1ShUeBkyQdSpuzJzRF0vZhR6MK_7sNhGXuT_vg2YEkCwJ0GBdyhgTt6Ykz3bud77mYbGoIWu2W3qWMqdRntLXZTfN0V9v3VuKH1h1hmqrbd9FKeKEALSWY5BCZFehnerXdbMeYcXIufA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0inoLbwXOEJovEDraByJeMrCJyS2_o4jVtMU8jlG5ApA1Q7zc_c7Z3ajPepkwuxgLVtkJah4kRyHnmedy8xOCeURyyQus5Gbbg48E-fiyZ8ns8qg8MnR0CBmajwhw46aRyJXPN_iCZEPwu0uGfwic2PC_llZCb6xcligE9Ts5A6urvhQZO1c34iwnFaMvf-x2A955fk0tM0m6ztGtLoPy3wsKiWLoYJ1npbMh0jD5ZYXDdsWTVwXMRKoIH7Amp9d_NRioWz6irhdP7GR89b-ooLQTuxbitXloZs-9A23BVdvVE35vX9TrM1EFjDrrol4Hi1-zz0zJjbCGB6bJAtqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=Xixb26AeBPjbO684EfhFqPAMJmJ6ZdiDX9pv5NTF5o_28YmHCSz1-nWgFq3gTDmYF1HhUh7gda_8_c6v69TGSKJ-vmkBPfGkm-IODDI52Y5V8a-qMbXwRz2WVb1Rvp5uqkSWsdo1bITgYAKHIodKaa46W_TNvt-E3NBT2PhSQtvCuYuIQ_R38XoKqMA3NG728zMz7qnkbSUKMaseBTTD8p9wNi_kfuxZMkXf1Rr24Coce0QZCgaLrYN_d_kdI0rMN65sz6HSqnj_ha_gxzdibSPyoQ4LLM7FTyU1OznTgmY9huPgo5YtP7TtkfPZXS-W-gUN3Jn_aAJabLjhFIUbJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=Xixb26AeBPjbO684EfhFqPAMJmJ6ZdiDX9pv5NTF5o_28YmHCSz1-nWgFq3gTDmYF1HhUh7gda_8_c6v69TGSKJ-vmkBPfGkm-IODDI52Y5V8a-qMbXwRz2WVb1Rvp5uqkSWsdo1bITgYAKHIodKaa46W_TNvt-E3NBT2PhSQtvCuYuIQ_R38XoKqMA3NG728zMz7qnkbSUKMaseBTTD8p9wNi_kfuxZMkXf1Rr24Coce0QZCgaLrYN_d_kdI0rMN65sz6HSqnj_ha_gxzdibSPyoQ4LLM7FTyU1OznTgmY9huPgo5YtP7TtkfPZXS-W-gUN3Jn_aAJabLjhFIUbJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027
؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22069" target="_blank">📅 21:47 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22068">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwQcWCEsuum9v0CVGNfCLCBLNmIzriSbUG9MyY5iA0mga6SN9YG_qD5pAph3fs2Z6XZcEhK1hhHXBbE7N90OBlqZEkRfJC6zo7qIq5K7P6bRNlkiYWA9FdEtVAmxPgvEmBipGuaFk690ks2hxSwvgzDrHtCIHSi3iHcLuIZ5KEKSAkmT-haV5eJsYPb_-ipTTTZFKjkLC0dh9drlyA3pTmIDs99SfgXtaoM77aTgb59YdV1zr2D5bpui_2MbeiPBnT0LYsCBoHuVe-UhgXgClMo68WZrokDZ1bHN0qFEKXPFWfRp-YAzflQlKv4F4yTjCFBtARpOy04kAhyF0XS3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFZrSk7p6P02-zNGaT9PNI9J_ZzYkTbTeBRGvgx6Xa3MbAZ_CtIBvGWxwRvWl09BuMoAku1RjZEcTtmuOCAU1l6NPKjyhvWGjTNH-F8tpO0s92AqYLi7jjwmkAM0uMxvqDvTcMhjP16_p7FagT6TtN4tbxX_bC5rnnuHFTNqlWA4M4wIKrPi9qIo6U-5UFR4OGd85i_deRlRgE9czzrivM5s8ykQnJegVUowAkRBzbI_TXiuN9_M7eFRifjdV-Tudpk3IqTaa9fK_pCWP9Ojg5K_-y8e2e9hVdTrcSOS7Ck-aHHAa7wN6EQgSuRjktsVY5Gtp-nbyoUz23qLBV68-X7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFZrSk7p6P02-zNGaT9PNI9J_ZzYkTbTeBRGvgx6Xa3MbAZ_CtIBvGWxwRvWl09BuMoAku1RjZEcTtmuOCAU1l6NPKjyhvWGjTNH-F8tpO0s92AqYLi7jjwmkAM0uMxvqDvTcMhjP16_p7FagT6TtN4tbxX_bC5rnnuHFTNqlWA4M4wIKrPi9qIo6U-5UFR4OGd85i_deRlRgE9czzrivM5s8ykQnJegVUowAkRBzbI_TXiuN9_M7eFRifjdV-Tudpk3IqTaa9fK_pCWP9Ojg5K_-y8e2e9hVdTrcSOS7Ck-aHHAa7wN6EQgSuRjktsVY5Gtp-nbyoUz23qLBV68-X7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
از نبرد تماشایی روزهای گذشته فده والورده و شوامنی دو ستاره رئال مادرید رسما رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22066" target="_blank">📅 20:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22065">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ex2AC-O5bmUARVqnluwEhKvp76J4_z94Di7HE95RBmMGpr95CF7PoEUoF9DMXQuTMhVGrPczumzEBNufalaNUYhw3IwmLIUq87GlZWcw6J17QdTkmmYRLTZTldn4JYZVN2OnLHhWQbzon6tkX_x-hfvzxOaeOzuqayMecgziOq5W7noKJ4fbq6tY0GDYHxn0x9iO8kLsGMYyCzVA6ejZFekEjlSgkea1qO6IOHab9QOw4N34V1uKIXoRMaqMXBuOGUYgccbDsBSKKw4T2Ssa_E-c3zUMpsCGA0cUWYnt62fqMupCmfAbaAESKA2gmxbFveBGRy0X7BDXJpmdsr_3jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و سپاهان در سطح دوم رقابت‌های لیگ قهرمانان آسیا حضور پیدا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22065" target="_blank">📅 19:41 · 19 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
