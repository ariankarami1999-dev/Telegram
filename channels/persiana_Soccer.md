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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 17:22:08</div>
<hr>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
متفاوت نه اما همچنان‌چشم‌نواز؛ رونمایی از کیت فصل بعد اینترمیلان: لباسی در قامت فاتح اسکودتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/persiana_Soccer/22189" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jX8DSqAdPe_rgnFPZOptpPkFATzNyFcmTPCj9vh4dHUMQvId7qm6AhurLeT2G-d4dIq5WY6bmBGX6j8TpmMUVNv2wV6J6zBsraMh3AO2KC2dcMENAg8kdXBERJTWNCdkjsiVa0IQjjm-85tm5qCh1LiTh0DqpXLDLT7hBqaK2nZIY-cGhbccJs4iA9ZRgTb_b0zJ-QeccQxSXAGDypn3RAhrIwMdGaseJCvWBP9gZv5mo3AjGf_KiOYUWQYOZ9UOedIThh973zCmVkQu-BLAQfD7CZicA2crB7rYBug1T_84XZtGWDTN-3ZPR3NWjqeGlU23xT8LR40oPpKBEYjhjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/persiana_Soccer/22188" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgZisqJ2pnWt6MfB2I1egbUCfSdxNrjNwedphHiZNg4kHewOnbp44ZNR7n0WUCS6pXCL3Nit2cP0ZriGulpaB-BMWbv3hNNBNRXXR_YGVC4Ky8_HwhXXsROlWZvyLffFAZp3Uq4ipmg3r_7_A20OwhJp7DFsMb2D3OM515pgSIyK3bjm6HhFLG124e-HDLglJmX4XcWt407OAYmmFFmqcDrNJem7ThW7pge24MAVptRnwIXKwyHfZClK0SG1-0FqU8UU7pgp-i6bDOqqAnRQmWEwNphhZS9iF6CW5kJ2WXB81monjqpUeL95FJ9zZBjuFV_vAuNP_27WKrZ_0MpeRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا
؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/persiana_Soccer/22186" target="_blank">📅 16:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr6Zc717NnwcyPc9GbUKf7oATjOFZyxX_VYhwdm_hVCCF745v6Zp23BGXJY949_o6hqHdp5X1Mk2w9vf2mTdlsqc0EIz5xLCLhf-sPl2YvGk1T4Ya7fHmmn5DofBUlW3HSxtjzGETMZdxV0jZvDDDXgN_01jU9yHgSdreOeVf3o2UE1oExHJL1HguPk3xNE7XOJty5kRfqiU4eyB3We05MkqQiZ7Y1EvUVkaccIJ9ybnGj4ZWaJmxd8HreppsSRxu5NIHJg16D4ds_qRMCtIHXZqLWBFyQ_H30McB9SDm9bfiGA3_N_yuTDuR-c7k0oz60Yr-tDM1-S1qAp4mOAb7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGGTRfG-IIRXU4gy88H5Wbr-rWSSUHHcG9kP6Rl8pp1MNHyNIhX45rlJ5_Y0LXBAfbs-0h43C27qZRLavvmyso-apwtgKXoAVdEERZI6fs_tD9kwZW6-yFtFBWFN4mZkc3C7-_2_qzgRrQzSxCbRIEScwewlYsTHvNYRGLyCnNlwM4N0_qR5dqky0hfg4DvKx2CxT3gaoP7mWNIk4WPJrB8Pp5ShY5JkQyBx5NVjV8Dv0Y7SlupU7Uvv8eIvKnxwAKnsB11I2Vu5gYwE0SQZp6B3VJDlJsrTX9j4lMtBSyW8V_7sdWtFpZpFYNSam567iEsiBv_1M8l6pN9Pnfi8PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/persiana_Soccer/22184" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22183">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7621338636.mp4?token=SewSIDGPMFC-3fbemNtTmpBqVV44Swty1-EkMDIWj_QxBNf-XvYQ5kKttLWUZn4pYZ8JYCQmCK58aDnvPKDDVOuSeGCk38xybA2jbMskrIsh02HU2zG_V_YPAx3jY8AEQrAD1SFfkxBHrBg9ipnwhGEX7vj0lS_J6X3lEtlNT7uTDqKlcx9k5L_BvCCngqASrJJvxYjbFEwgy4FfVUmBvFb7YTyNzPkrmEeaIgkZkgH3j_0qiaKjR17u47kCv1L-U7y15qpDF43tXaeyw58ImRpv38CvdNFMciXeBYIvoyOaczy1EjrgTpuJbZWR2-1yHVZjF1iHjpfxaHcYz2JHkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7621338636.mp4?token=SewSIDGPMFC-3fbemNtTmpBqVV44Swty1-EkMDIWj_QxBNf-XvYQ5kKttLWUZn4pYZ8JYCQmCK58aDnvPKDDVOuSeGCk38xybA2jbMskrIsh02HU2zG_V_YPAx3jY8AEQrAD1SFfkxBHrBg9ipnwhGEX7vj0lS_J6X3lEtlNT7uTDqKlcx9k5L_BvCCngqASrJJvxYjbFEwgy4FfVUmBvFb7YTyNzPkrmEeaIgkZkgH3j_0qiaKjR17u47kCv1L-U7y15qpDF43tXaeyw58ImRpv38CvdNFMciXeBYIvoyOaczy1EjrgTpuJbZWR2-1yHVZjF1iHjpfxaHcYz2JHkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/persiana_Soccer/22183" target="_blank">📅 11:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKZB3K4UFASRPJU-5lhPEYt_hFDUrNPx-Kh6yeTV_VIurIQ64h3QXAoI3J7zeV4ZiXY9NuPF5mhQQjFwpDGrWVkt1qTl56DiaTSKGdhkwyjX0xaviN2QDwTSl5_WSY0LQnZ5HXJYEOJkeIF287dkwmRNoYsP9Y2o_eh8AcWCASljseBx0HeJH7Sy3d6hJ8NuWHyStLFwZdmGDdtGDeY2-G_hlM4DiYZEEj0hjDIl9A_CM2NKjSflrovZ6gNzYuwzlTctXsUgXd8J0Cop-dNBduWmowwmBj4RwyPoVtRFDerDOc0O29hSjPUg9lpQ77eoiRfEEdWbvHmrV7aWtCBl_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ پپ گواردیولا سرمربی سیتیزن‌ها در پایان فصل ازمنچسترسیتی جدا خواهدشد و انزو مارسکا دستیار سابق او در من سیتی جانشینش خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/persiana_Soccer/22182" target="_blank">📅 10:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvN73u2s4ctqoiKKh87APKEYe2GQcS-gSFFuo26yTMIccxYYEh5udQB0TKIfHoyQwLlX4VFnnMHfBLubOhZmC17vbd21m2NjrYCzjsd6X-igKISJr1-_yQFxI2IcLiaz-4vTTy5UqXKGzFMGO9EfccX_eh814J8jXyHDZYJbNZCqpR02XXEADBgp_rEBRdzT4E7ojJXrxBmJu3VYznxW1l7sAlhZ0iIDbYM1KUpV_ZqdsZIhizGs9NbE9hD2bhGve0NVFYQMdmy11Lotcm_gOgYpmCy0SL8itoPy6y-4EXYm2U3FO7bYt6G33OyosZ0Y192GK5L1Z6n58pWzkh-RGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXAshsE8iInYtW-J_WPZzEx21DTtFBBmobWVGjTLRLMPfzM8W7L0V5sU3l79QmhsB4sBZWjBP7hbTnzfc7qrbGLEaFtJPMQbC_culHJsITx6vZ_ztJ7jskDMrtdBjYoDm0e8xMK7QtArUFqh5YOoIrVnZ6nHYdwdENRtHPS6fNMi1vH-vnbXXZ4WFk6Vjr31GAEkYNU4YfZsMMYOQvBTdVRKrr9WOQZBFuEpSU3wDSLSUd4ORlz1SP8zLYE8Fwvto7DLihAAfUyuoc7k3KhxcQyBGeTNnWvJxnSWlizKjaLUILTU8EVaaB5wV0Nno8GAnvJlMwI4fPIU-0pf5vsZHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/persiana_Soccer/22180" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXhMoeQrNLHKdqiuHkhW2yuFpiyUMaagmQUkX217eNHFurgoTlwz-FPTztORdFHVhgA_LCrn-SN-qO-oxkmrpqUUQib9wKTW4R0uBZr6mBlbhyHz3o2Y1bYPFvBslffvRkJsnElkqbWA93CdxOcX69vqXkaPV5wvT5e1OPUcbEEkOxfNKHTAc4XFgYJS8hOtaHm_hwykpUsrAHAMm7qoMT8bbADmSbdSrUPY6YFzFU-oN_E84lB6cD1nwejF9vfmRFKwJjEhUWeRi4QSp0G7jOtRipBva7DCZ4_q__v4vZ_2MArocYVBzMQgjD9lYMZrmwDL8hh5FXVPlDKFpyESlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه جذاب افتخارات پپ گواردیولا و ژوزه مورینیو همراه با هزینه های هنگفت این دو سرمربی محبوب در پنجره های نقل و انتقالاتی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/persiana_Soccer/22179" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22178">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/persiana_Soccer/22178" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22175">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ovIAtYftyTF8ccrHqQCCG57x34XLARaDJj9Ed2rvOurCfwpC-wfcpdhI5udAMsMlOclEgB_MI4buwJNiqh1sO9g6XKR_qzHOJm31HPvhHct-t9chS7vdQShdbM_Jwwc-rc2IhMsHs78xV-fhEx6oFa2uvmgEuXDZmySkk8Z0YwFRNBf3IiZ9oSkFIRtAYZBH1RLdOhXo0OA4z_f5l-Maf0Z8WwXrc3f5xmvixAvroHcrDjkymgqVOhwaJ364sQ38OEA-Aa2LGMN11Juz7-tAjx13OLI1foiZTLHQUfhVt9n8bJcFePfGj2YEYrsOYFvtHw84qgwm4qTCK0o0FNYvMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tXgJ2dFO7YWO0OGjkwmrL7hgasvnWWTn1Oifb2Xb7n0IdozLthWkdo10MEWry4paY4uG5dJ_VZbN6nsyqhVATq1wVXtgL5XAj0m1Fl1NRO2RCbVkEKKANv7C8uU-gnfJWiME2PehJru3nOdd1IMAs4pRn_rZNgh6UCSxFcMRl3J-qvN0N6tS7f84GUXJZDaDsgqGiXGmBVnimjWKmvqqO2FwAx0spq6BHZyx5N9AxegmTyxhFTcQofeFKcruHPR55K8wVEiZidElBxErPfdYukeUEwzyx-WUhKNGc4TUzk0Swk9QPMgDKWkxPOGk8wTR0Q7YrBZjEIsd8dFEkkWTcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مهدی قایدی ستاره 27 ساله ایرانی سابق باشگاه استقلال در کنار پسرش میلان قایدی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlO2khZZOc-l2iN0Fw-AZOI0aO8Oe2DGzolcDsjnYXpdFXoUffAbKIaWIMhuTUAvsaPPuLAnjH-znG5nAVp54RgmYhZuknizGLBJ3xeKTxP2sjiVbWLrBzE7dtJYehyfsi3EmTPIh18oVbpso6Rw2kriinNM4MUpqX02YqnlD3nmo4zmjvJ_MoXLXyOPgvyS6iMfMrcThbO71qsM337aLR0-F_-fK5p99BlLoEKcPFWoVprqIBj59oOm7zPBkIW7JBA811kNM7H9a-hLyEEl723rTAVkucrU4oDDFPUfJkT9oeGLNRB2oyUnDqLx2UjlBL8ursJZhEsY1c-Hh0rqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJjtUfafxtWqO_zERdgESZKNKv28nx8pxdnML--EgH7pyy9Ml7brxsIye_3vFD1AOVOwCXgladLYoOXncX5wj4wSAsKkQzYJyvMIv3ByAjfBCrvrzPXIuFZT9QUXCHC3d3dGLYok1uSJaRwte7FFmXy3q1GWDPkjRW587G8rgkqIkMDAs-kuVCJ_lgoiCHJFSqgkrtMGIs_T7YuTcimZezOndeLI7d5rBzu7n33X2ri9gQ1YUVqxGqBYu377XnxitXCGCxa14iSPgiSIUhPmQtdG4opFILxpfYB8vYc00Mz0Vks0Na1lueHuui9DYkkpTEajTApEBOZTCihDUvDpHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2MUKQxcPPmbBNOoWeYX7m45cfKClv3klSAe4xGnCawy5hV7fPXlUwkqFzRVqrQYKRanEwc722nZrtd2pOCjA1D20RofKn-3Migo49ianpouANt8CN9KDde9dnl3OiQ6486-7H-wiW-g1KLBvbycX7q1Ti6ZCzMZftso-ic2MbA4D0Ka5bpiwmBb3zvBOcOCpMXIN9-oRrSWk5YrJEbIaykYRdARd0EdJ-b7TQt_Ae2J51fBTHrXF58Fkv3EEKOZLq5fxDqNoBjx6GkEY3v7P1u3L6PyrzxIT5Xbmg4XUFQfiRD733UUsUfe8SoXGjK-tpBeTUpkEY7VJkjjKkfO7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Natb-_Ole7WksiKnrMvsRlRnOL35kvCuUYRb6mUvVFgu1a8zo1iKHmKVpiAuyoPZFD3wTIDTOz3ZzLk0kkNOyK7o-DJRmLjrk7kV9DVt7eBaY8KNB5holUTbKejNSiUbMhQw5q6rwoBN1-7UlcaeO9pyPLuEKegPDmVoH-i_hf7Ehwu9wfqiVRWRo6CPKUg9PZZQnyvPhJfbS9LwWNzq04dgBhhxrpSmL3kq96z6V9M7J1dgc9D9KuIqI29DOkSWTZCOCquE_euI5063KfG5Rb2o5VTbK0fP2MzjD5l9Q5vUyr1cavrwkHK42e8wP0yo2IfcxpK8Dv_hhWxUMhOH0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3vfeCOmkidRGknnx0NJGqFDfv4KMlGBYb4tTgn2XXop4DBk6vmGAHBaXDStS0SY_XheH5I9Tqc6PXR66LcFrQl5IwZK6AhhdEBMlO7Qzfylub2ocNaGqXwOUSjpDKpPOJQcEfPUdW1z-xKa1Wd7-W26E-vx8pTJjFNOqM91hZtRNK-BqfqTJTmsOkbHhd3uj4zfQ1FjSBtZ2BBl3M5E-fTWhrPQYXo1SQsWh3F-0lgOIbOtU0WyQRRPy2mF9l3HtXytvO9riVUs_2RCbxyOQojyCnt2QoXyZKHoB9nR_wuOCjINPhxbY_a_1oOdGjhG4ZacCBuC2KO5L9fMdthtlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHOApNytjJ3TU1eVvYc0g1F_sNDmsGMLpQZUbfOxXyuGeVMSes_ROYs77MUSPQV1T9lZGnAAafLz7IPs2wX69UhNPq-vVtKYgPHIp2KOZ4Bnd22RICkGsVKETFPfPX7_G6oyNq3pJC6DKoydaRYQZ_QUSMmIiuaMY9OPlsEVO6S58FbjpeP4m486XeTTxMB9rbjmzgVVlbOhanw4M3Kt_FeRLLe6xiBSCXu1_-JDoqDF584SSO0qBDndoe1ZoYKU4qiq8hSeVC48yX35vO7qbrdZTHLnfcT51LiDCA1iRUKw6ctjzqhfx-FyraiWrBVlp0wzUaPFv4QK658Naht0tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouJABkfiialsVrxlUobHYNY52BQsG0H2XXtP3Iy7HTt7xpOytY5jheeBWQwyPy4TPzI8efZGy9Fz4XNG2x32gHg-VWQSfi7RH_qJ7d4np7CVOFQ9vffnP6lSpNHcX3Ha2ulRw41fijJOulG__SUCaeSZQni0M1w8iE8rh-lBpd90yiupePtG-wzFeaPa8v6K9aJwPn08ISp6YKCNDe5x9XHVV86bVeRaeZLCD3Z5g-CxcrftbrcMo3sQAdT0zQi3dkNyciPZIfGE0xVUmlIubXV87XnyalG60lSspij3r43apRNH-drNxHmLKR12qQLZi3Gu8vOwn1XQlG9WZfc8SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FodtZaMJG4K84DNRfvyT5f42DkYk38R_13nAFoc1Y7hylxiD3kU9xt0okJVlebt_wE6hPJ9y5YWrDTQ9FMvqQMvO5S0IMTy74bXB0Zk3cu6Xz7AlRkwYE1Pob5BlDesAgBw0GpgmCvQBCO6E2HFKl-DXcEvQ9SUwdi20wEO66HxacA-Zw-OKNbNLrRROUfTj8O6o9sY-gBNnCrf_HpBZM2NATq4qC-6r-yWGujb6ZuOG5bGkek54nygfmfYTogLJRE1-b_pkes0FIToGPk5VTLMKH-3TCrRN9DLLkTEPEznM2Ct0jIU-j9ekOs2OrtsYxs2kBet5aSZvOkQEOcNL4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBNjleBKQjQMO41XG7SThd4uR3btXQWNWO3GGahjy6crFgMEqOcMtq21heLEQWIw4znBFVfivw6gTuwisX93_bdlgx0LRTcjYBhkoLrMzCS1rQWCVykKH93gBn7P5_zCURYHt6pN6iEvEikMhF5DyuhCZvtDcNb0QBz_kW17oGY4rkOFLZBoO5FS5bhxSU0JOIuc6WMRmUDSNs325Xg1JpGDBlQJkFR43rWDn7TH3lo7UupZoMzYVpWOc9__LN_m3sEnWf6b3GZGzdDNPlUdmhg5pU6-JH7pPveKBkUoPqVxfAVKO7LFGrM3OqTmmwh5teeYtfUN7tAW_z3gB09YMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiTPYv31_ylgjx9YZ4MISPnTw_5-lIuUpnvw-SaRh-GR58axuzREn0dwww7cmt4nh03SaAHEXwuvepse3mt4WLtfVUcAgT3ryUA2sPrM_8eEY3KFSLXiqrFyv0jqiPUSuAg7ODDDBZ1WGqabdeiVPF0PwCiRBO3keSr4-yWN5FisI1EG1lUx_KJfpY6fgK2iF-3mnWLIJ_RnmVKxytN8jffIZTMC-jdOX-QcdwJVh2_8_zlhQwN22sbm86Kxs-hKs0JGNnfj1iNnIzAtoWDhdbVK05AmusvmwkLbdSwKHS9Fl4i5hjgRFTLcTpInmm-Ti5qxxdIpO7YEHvjA0upbfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhPPy83v0mvEAmZQRf1ojDA0RjUg38DyPViTKANFTY-7cIDIkX96rhNBDXzr9gNy4YtI_cigHktsgfQZEjiiTdGB6SHhXMgvbwn749ADIplWKRtV3iFtGKzzlmk8ZYblWTZK9m9PnE3xVyrpFd7daUBqsBm-kVOCpZpgplptK0ryc2AMYswvCNmv07c8PuxgqU3XlXoqCiTJfSb6RAyarEZNBMb52OBZ_0xipyHUTgNio2FCnwT6QLHeWZki2EOLEQwxqpo4igrpGtN1vTci99MCLRj8dPjy0b6Zxawu1zEIa3ib0KKIhVi5lDjo9prubNu6EyBy4qF7mi-u2v0umA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tylAYg6sI80du26SH55UzVvTRQwsL00aShGI4RFPpeTBCZ14OHTBWrJ-TTrdBhxrZ2PojCwQO6gM2cO1uRS54g-8gff8I-mgEU0evVd1dtToEgXMIap70mtuu4bZ6gXN-PoM8cwg2tqHlyN4YJ77-s1zwUfDOx6oz6P57fk-cJ9e58JNAv2nye5OiD1Ut2uhnOS0T0LYWXZqpRIw8_vIWyrQe2TlJ6VHigGFC4IdEsEJvoDDUYCN2W20XhnKip0FOqsu0QOi5N4Vj3ScJ9jHtAEUgX88r1-ekUVrVpXY0che1-lXmNbtB3iCkYbBc-pQ4LtMTY99ItnCoLzV5m51hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pI5UFxAGky3b2j3n1mBPTVw7TBP8LSFQYfkE4K72Im7d6dtKlKKEfGxzwinzmsXLZpd9Tc8H37AIn5Vgho_OkkAjecdgEvNWOE8cMN2R31HEHey8hBYoNQrKKAamYxE6VL8JkBl0uoNQRr2ZptoI5oBcxu1_OkU5EtV6JWSGA97fCmvUk1EBCnoaCET6c2byMX2iS0N-gnpDwcA6SIbIeTuSoYC6Nt6YiO4WImIX0u6mrk0HApKLRbLrvOPm7LHKRNV64qU6UfJqSobNHJqBUZwJF8hCS7D4j7Bi6ul8aUrGc0P88PRZIsuxYWdq99-MOR8ZfGffWgag1PaGPHhu9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/is_tcv9X6xBx6i8a1efaN17p6TB5iLvceGICI1p4jHlrwDpc2La1OqPsQK4rWwc5CWDpWQb1hZz6vTer-V56VVYIgnMOJKtmxmYX4GccyyIQPDV2gmGUAG2QOBV0OEgef2f-tY3xhg8hi7471yUFaR28WGtmIN0RW_Rmi2VlbU9X0-AwwR6jqvqvjnA-WDeR4RUhI0RQzxyGWOGxn03-Lg-nKcBHRUUSdTAQO0pnYBlkYZx35cobgxdR8FLqut13cZVnzc-JAu9iS_WWbKj1oxkZVPuDFERnMCeLp7cSNuGApSErfYerMBbtw5-ntxmWDoOTbqOuCOA-1yCg861KAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kW9sSi44LEmppqI_bwSR0XFi1C-Zt6bWGPAcwtimZ4aHxAOqQtLbHwvYmYrwPv1EI57gz-3ZAesoxUdnMEfhkLgMUpGbAkAbPWxckwRyUk2XrJdQvvBL1_dLkNqCN2L4NJwwVkyQhUssAFRQqkgpV_qB1rXCTc8Q2Z9RfxzZFbC7aVDkYcWemkzSuqDicWBPZmbvPlj4dwOYAzLZuhB2sEGbHNENKYW7qMlr8cV6Lc0u-NoooqdgKAKKPa17vfXGMMr9eJSP0lpRj7f5FU5tig-usd1z7diMDJMfrpnby__IYwPkmb0G8lLppkLHPpdutCAt-Zgr9m_t-xuTfkT9uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5xFu3J1hQEWaZhMQ4p5ltz7vKrz0I9genzoqK5Qr8yznfQkEpz_cB1n-k4pSi-9x36XGI6YJ6oWvNMGz-1HtpdJKA3Nq2FDJs2CxndxtLv4_2toHgRgBkHQdJeWyD9DdJ8vw8DvLK8aAGJRXquW_xht1EXV9qNILpx3H352CbsKzNprPZ8P7_LuwszwzfvF_y9vnQE9-qsKA0DsXXod1FvkmSq2DS8JEqkCSKwAqbPj_Dl4ap--hUyMsEfK48rbIpTz0qMrfFZEoWyS0V_oL0g20CTuhPEoYkz57B1Hkz8AuwcT51D0BuEkPKrAZVa5fxrvypsawAKgF88KgBxssQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otovb7RjjREfclDQWEr2Yv088agOM_xPDQ1wwFr_uhae9gu-9S4MNymTd6qo0hREVPvAm9X-POclC8dWRL-UtmoJJf_0zUyNF4jYVq8MGCrg-A0ayU9LFpboIIDypSM939NwoYkCc1dcZYWEf7i8aPw5FYqQRVaCTgkTiGLwXCEsPwZRpRXQR1tBdafaoVIZP2RpaZbGNJ5dpMH8miv55dv2JEJSWsNupmmivB43JyOpA5HbbpWmJLyFOHlP4qZtyCJuwTDxxaGH9p3QVWi_OMovhdQpBjugFfiow-ld1NzwCtIvfpG6MI-b2JxuJ-dTVPKtbHkT1KeBYgjHv_sogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWj6DebolHdTRqMiqhQhfkngLiwdPr6gWEY_TwGwthiLCl6sbK-g1GOHYR7Uk2I97kWPqBDUOrWOb9gnl4lZ5YNNSUxSXjLgDp9CNCIVJSN37xcC9DiVkSUpaIDRpg9ILqM_c6otyEm80LAXPE44mG4iGZFmUOaSr9QAO9BBEwHj8QU1tX6lhQYEBhfamIc4VqDMS1A6WKrjQoQ05uKSRklEOW0p2ds3jrF3Wll6QDXZyzbnPhrpRhdcjKmtcUexh85x4BNMWySg5zQUonzpHwz_h-UexsYY-ZflFb9fJiTu-zKx1FvHr-REtH3AtVYqQ7B6PoY90VAznSbS8GitwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtI8kL1AnUmx75NRXMLPzSYKPCO2v4oMtJc8H2dIQxNDAJ1ot2f-japzaR3XPJP431prn0fxNZjUYiUZtQVuEZ0yI5wHA0W5D3wnaOv7DEhy9ymronRLIvIfKAwtqocP7Efm80IEk3NLK1E0u-6h8bKJmqxBc4LIrZcrzjviGXHqQC0kRh-rVoYH9NsVci0w2vOBsx5xGQfNeuimY2Yep6xQpjS3VeOR_9GDdkH0ddF17dDbOS2mx4gRvuWyTbRBZfiBZb84iLWAQH4fPxsr56liU_nYaNEXCu_2od3PGpPE9_0z0NE_sJr-OA8nf8ppq_2slhFz9Lzzsn-WUbYWtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ph-D1OkYWp4WgupGgarHUgG0TRgL-W7DgDOlFXY9cV3lIIKKT-lKWiuOdgvWccJbAF9GMjt0RgBBjZsRMvwjY17hfyJ8MS9HZXOUyhZscLj53srgrHIvxQXD5dr5mMkwh60SaySTaxFmrYavvYL5nHFXcqpu0cqGFNiZgZn38LSCMQGOFP39Y2Rgqsy1t12JS8qfgom8eKA53y2WH3ralsd6NxlJWmrIFv_8F1BXTwv1Cbkr8e4sk90ntnD423qhxzwzPIhTbiU2bcMHtft8VHuh09-qLmejSwIeUUVOBbMl7gedhip5MZ_uODmN68cIKeGBxZB17ylNnGSZT97v1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfbon4Ad5KD9yDRyDxD7lz3PMyPDmocJslSwpnBokZhOOxxnbf3BI2V9Xc6Sp1m1CLp2MHfgUN84khA5_vVaa0RjduYyB8d_MzyUA6Ksn20OeypHU6VqPJfLQm1PRtzXdY3iMq9FdBNb-qTAcHhhWaLA5055dCHeEmR2qtClQvtWqH2MDCDrWM4pKcNitfr3_k39KrtXSpxK7eHPybLPuOJJfzYzNXcASCqp-t83yt5wss03lBIudacGtBwMAXZgPfaLL4fxgmcKahuJUwVXkjplVRH4HbRcIZjFsckwwnhYu04y4JGb4ILUSymOkI65h348c_IrcScC4VyvvxptKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVdLNdYFA9u7a9V9_tG8v5TfL279CCzHaTHFV7Di0RZ4Kb4McYOkGLFGcpjXrWoS1XvEBvnwQhtLuhCPcjXFHednVDE98pTE_v9mR2Z9JpqoWYhBSTjCz_8nZfZou3AJRxdOgYPcOB5WK3jlhVUIizOESSz4yXjFpfVIiIQHcZNvbKDWtDx9kt99AQQ6lbESBzUg48-liKx5zqA_01m2JM52GYao_SKKeThdkKh1g9f38ffVZY1mHWJW9wkKzuoHub8PTO9eRcvIbAt9vgyxoq7rTmfUobLPFquJK1X4XKkzWiluXaqSEVLar-z6eurhDlwAYwuUroG6Qllealke7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McbMbEMc9D2rrfdh0DY9XH4YsfXskTgxEpubjWoBitxSkJsYcTr7rjbpE63pU2aS0DOARPxA_0iy4U3bethPQ9jw3wvQqMeG74plpjd_BPyPtbr1cY3feANJd0FcZDPYReEPWc0zbP20eniD_U6FhDCcIQpoKZSAWxWydh_49I_Mv84cf1CwpDIjVQ7gAQMA8wFc_yl1-fbFp4ZRD__0q0k1PWPxzcUCDxNDqrYvZXXfEKq_QY35gGzwGvrkIYosoP3w4IiTmIanyZp7oPmLV2A0JABm1K1RcQ318bQUvbA9ReViG-ESgX9volmntwKgOchDwVhNCEE5OH63KWS3nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDHYYHbb-6Qvblk-mOVCOaOtwkYYK3BlUHHpJe17zvv_5nIWWpPcJijljw_s-jgz07pcSjkVx__iju3CwU0LWH267ndYZKGojRoTt0Gk58AMJQHVDqOvjqstWz_g9YgjsVylLA8F59lSh8d6Jpjpjxw-WwqO54SMNrjTu4BfLx51liRnWeFabCB5x3YtSi4XnB_sGXqnziuQU6BI0lt-Bjz8Dd8yPkNaua8ObvHZwdgzlgm99IIOXNK8IVb1lcBEp-AvfuXNcb1r5SaWcwqovsiSCjzD9EcvTb0_x4LYd1I-Vkr1YbPZmISul_iXPMhxxzYLVB3HI8REhhBVEidt-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWZYI6huarm8wwHmB747f9PRSNPgsYH3loqmYltLMw13PZaQSDYvTJCLnXbItUa_T3MXmL7qeKIENI2QJiT-Zcd2ciEbA-Ntlc3HwNYgesPPrzLXFTTF-nLbKUKiiB-Wuk3KmVYuURfLic8SexxivJIG_Uqfxs0QRia4xzAoqe59dpsfXNIat5cf-UDFWTwRjJeB9VcMYypAmgmfI9zKVCRRVRDzsw97zA_lJB-ObE9Y_iUg5gbIP6aXtYWsmyhh8vMp8qf9U53bMvFeI7AjiuPrITAOJH3hT3EVsGKE6V6b8KGp4YR6YbmvyOUnBo5S3kQUGWVoi5uBu8teBBijdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7WwtQd2VBmEX_1V2C-KGzmAVht8SLvTIWJyID9cWvOciYIV6coMHTv5JOqf1GTZhnQJyrpa5EA0LpWZiSP1P5PbNlrLtpjMH07eyV5Bz9_n48lK5FpPhDNimL3431aDgo0ui9cGka4TxE9OAm-8J9x-NadvVJiIiIcbcwV0V0cfXwBL9wTMwh0DFAYvCikNnrMQTis1YnmJebwqz_s6BnkrX1o5-XIvkCli27A2RJIRzSze6LpLOC1JJxQ-nms9d46KsYAkUKKKNP4Sk1C2W4MuTzsVHvmqXnSfk3YK-CjnuH9Ew90g19PUlE_rl3rV3HetoIRrOsru97QLqkOdqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfEYlboz4G2qIQJk9IwT5aom1GoFOqCsN12KqgOrduTT1gtiOB6Fp-v11KiSv3s4XCHLdId2JpQe3hxC5GK84ViajlSrYc7tU0n1o49UHiflPyVTvZTO-81f6aXPcB_Zev1vvik-nFAFBlyuxxBnkhuf0LMg5QZmGY42QcFrSYVt-ZV-y7LfIDRt3iAdNUpsXmk1hIwOBvtHOA-doUvHUmVqsJIIZ3UW9WULQdCQEBBqvzv_XvxGb2EU0-8nffqyfpnBvEW5uLuXAH1dSfL_BF_ncNQiCMVjdl_0yqlDYYSCxPWrj-41dIiXR-3Ne1scIVcKXVeQbkl1m98AtAm6hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMXQwPrsnYcBF6qakb9zuM7aCa_AsJtXG-HG9FvXWJkT5rjO-OqCijApG3TMQfHjvvpWBm9PEpIBDMQs9T2P2_MneLOSqOhFOWPZK_LnVBnO2xdCr9uBiqtPLnSZS3JwY7iwoKxq0kJOqhk_S4vQS4Ztn2PqSdaa9lqnk8qBSN0BgQiWALWE6NlMxxOWLtmQDytXZw_OUeSnJZxt0WFLMtcu3NiYOqMZYvtY1Tdv2WK-QAIxEUELK90JDQejjrJBXRWJ6x0zuBNYf61kSCc0M92DLuAymgrjF3BtbiTBptqivs7R7GjdrNXv5yAoFOKFi5OffXTRyOqS96TMEErPdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwGxdSAGgk9QNG_2agEh5CS5uligCrO6n5S4UspRBIPBySuh6ijdlMFlaF1OEPdQ1eP0WpTq4ffz6EyfMzZHzo0Ylc-Z05BWsmjY-vHZ1En5awV_yfaJKxoYQ8blveFO7U6HeUqCvgdtu4l5MYGuU2j70vzt2NG1dGLoxzO9eyZ2SMq1wLw3NOzjkaDysXI4Q_BDjhHv3MDUie8cYtTMfcKtZVwK-fJeNk_apgii2Ufeu5Kxew-Y4waiDjkoRbnJHlmMYGqkCM7Hutc_zHfI3XjYosE91A4-MEQRvub585pgf1-YK_PDaWQCmLZgTZ8h0NDPmd4EREk6r-WKOsbuYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxjxr3DAoqQz74W-hg6kt-T8Lgy94BTyuyd-_ftPZP6n5o_gVifGU6Av9g0oeaoK90jxJJVRsLyAt_2LFKutLXtO_zoG2zkOm2n73cj4jzDqOLf7YkJpS2l5NVHcgnuKKcKm4rzdIeOC9Y9cq_6QekdZ-F7FAEJoh6Ptp1r8tHo7zgPHDOXmG6V7Q3IEpY2wIFGMhjbN6_1MqiiIAwsE_dKKWc7E0thnHfmGr2COLDCCx5dP7b_Q3dper4LUZSp3YKjM_4f6IsRmvjXmn00YRXXr5Bc6PPOVy03fHEZJHRnnx9Lq3s05nzLJ0Z4N5O3jSjDZYYo9AP1T6sSH4PkiYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSyOoEeV9p_OJN9vNk1IPPhhwG-lztSP81s1u2MflaOPxz_otILsk5bJeYp72L79IpukL_sqgbRLFOYHIDFO-ZFtlXfIlSVL_n1QwU8tX2X71Sfp8cfo6GF8ArPPP9eSMp4-Y6fMw_w_2AKQ6xK2btqd44QZBSbFSUOxwZg4w2-PRufJ9MtenHktHImFA8eV6LcAolRNaXMCzMzzDaWe3nPcyuzi8FNiRtkqco3veBvVYCkdj0Q7VzxfgqcK-SnqJYGElbb_ra4K1_SbgFLBe-Ib2aWJlqRdg3W8Ujdden4TAhBkBKXoN2_1zUmxV3R7YT0XR8_i4_KjxRdY9NSoZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=HB8Rm3qTZxRzlErWtZ8DKNhlYj8nlzRd4fDBAPvq1GDQHs4_R9qrOq33P_c6_aT0QY2vWblwegRac79klSTulZ2V8-00no8tGDzT954CftAIQt30tJUGvNL4uYN54JsesIvAIWr45NSeGTJrjFFs8eCUMO5TvTp63tlrYSLqb4X5kE6PAfP684cW8P-7lteLqRfLfmmW3zFepLwk1VqPL4PejppkkWHv4s7pu9NXQB7iKX5ujB8xQKUiLyVvxw8Cf2lgzG3M8z3sbRFSD4HoXUmittizQ2t0Ff9zPej876-UiSPSt3LfmfmUuuuFislrvaMB0F6SnFxHbPrRaydALQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=HB8Rm3qTZxRzlErWtZ8DKNhlYj8nlzRd4fDBAPvq1GDQHs4_R9qrOq33P_c6_aT0QY2vWblwegRac79klSTulZ2V8-00no8tGDzT954CftAIQt30tJUGvNL4uYN54JsesIvAIWr45NSeGTJrjFFs8eCUMO5TvTp63tlrYSLqb4X5kE6PAfP684cW8P-7lteLqRfLfmmW3zFepLwk1VqPL4PejppkkWHv4s7pu9NXQB7iKX5ujB8xQKUiLyVvxw8Cf2lgzG3M8z3sbRFSD4HoXUmittizQ2t0Ff9zPej876-UiSPSt3LfmfmUuuuFislrvaMB0F6SnFxHbPrRaydALQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
👤
در شب درخشان لیونل مسی؛
پیروزی پرگل و ارزش مند اینترمیامی برابر سینسیناتی
اینترمیامی درشبی‌که‌مهمان‌سینسیناتی بود توانست با نتیجه 5-3 به پیروزی برسد. لیونل مسی در این دیدار موفق شد دو گل و 1 پاس گل به ثبت رساند تا نقش اول پیروزی تیمش باشد. با این عملکرد لیونل مسی به آمار 11 گل و 4 پاس‌گل در12 مسابقه فصل جدید ام ال اس رسید تا صدرنشین جدول اثرگذاری لیگ باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLke0CyVnxZOsGLh9bfxfRxVI-ZOj_hnoMqVLeci5kTXKzx5OlPYfT9Gp6I20opZOB30tjWMdeLFBS-nLqeg40iHH_DFarZBi7uC3ULkMAPSnU-C8AMNtXj-Oez16G2HCg6liu6AhUUsv6DEISM4xwUhK8_nJMThWWwka2xyN9Owctl5v1B-ePUh995fh_3T_K57GXjiI2Rsm6TQDWsdNprjMMcGXdhu02hoSZW4hfABVbEgaUAYwuZWT6VcImF4jo6SPZxgr6YE_Xewlh5Erp8RqFAGwrJQSE3vPHYZnQfLL2Lxq6MTInn-cty7E4PP3VK34mHifwm6_OTuaqjiPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1W5OjfuYu7xEE3Ansel9PhrMxvBnhSgZKxvRoyMCxvHZcisGKPqIZNUclUTYoxmhEqzKC5JCSA75SEZHweS1sfFoCdTJypUmXT7vnOO7p-cGQtxdzIRz3cKhyZNzIiN2QzcUmfRmTkeXZR067C-Yis8o8Jf4g4EoWrzlBj8kH4PtvHN7ousvkp_wrqnNov7lGcRuwy5DpimFmKANbVU66Iiv-xPg1qpja59HNxNKvp9IbhXpfN2ykVJgbRkgQ4llzed9PfnRoly5fFdUmouJwy4L-8M9P70jhpnfT0fZ3RbQijtrRV7dth2OfKqULyRlnZL1g7NRC5sbqD-CUArpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqviCVm94ysoDaS-7K7jfnes8psnXQi1yY8EFiUQwuI__kBIDZCweJafwF5Oypgh9IRsu2M28_L4iliw7pBNwZ4UPoGpgr9ZPFtr3FEGoN1JG0jM7feNN1YBUfWp-MdwsmCw5TfrwSNm3E6hPtaxAB9igBW4SuCu8qOdAeOb-Q50DLkmrkS5zhNZTMIVVUhan6khwM77kQ0PWf0XsNEZp61e-LCk7lQuVDnjZVmOUtvYT9HCrbnTgSKH3kRDtB-kAgRuTJmF1Std5tBQstfToowkC83WFXp3JSbU7z9EdvikJGpb7ZTQKKkGyCAxgKNDROfCLw2q0CwtpIGljTD3_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npT3vlAc27pIS6_TKNSYgXE_YrT5l6IONby-WERSY0lGnOBRdA_X3IlB9VKVhTgzdmxs2v-VG9wtfBNucj3JahemYPijn0vu5NCWIQcabbMEnUttjl4X1c84kxTAZpeSLxXM1Wnf_zcKf43b7Gu9maVb9RN56P7oYHxeOrKvL5ew7Kdl4BI46w78tZw2wYg_QXjGR2vNellsSnCirI0xCAcNUPWiIJy88G3WJ_8o51uh0BzahXQc-GUgqJgalPpvSW1TrtXZY0OgR2mtKqM7W-xznjOkaIr2Qg0pM68MAn11xdYR9fo7ECJBbXGjXYRh06iPBPTH_QSGRb63re3gpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImVWjRtDubrdNkZm1ji2nY7fD3CDu3zd9-xV14yY32rcOw-oHokF0FPCBHWLeGQdgpOAJdL5OkzED0K1jseto2JqQi9t3QJ-4mYLUnM4CcPOZrZlXxqN1ScOpNprXjHz_JROdOej_YRSeVaH386QCfvSB3G5-y_OBVMfcTDd_3oETq6aH9N3GT4G7oL_pxTJda5Nb6CuSTNgkgASlz9pfibw_9JvWh6LqrbZYOmQZF8L8-_Nb9F1jZq4fgOZf8OWzzIdJL6BuaVI__eG4NWRVN-N7byquoFgb0saFgAGqNPk3pDMXu5s8ZBSf8YPv4NyyQPtss0e21rR2yZbzLSizg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isWIXGAUw67cdeGYwkjkP6-lk9RfGbknC5uRizxMpHC90viuIG96516AfaQwJre_oxcrK21raOrQXiWXLVfMrQ6ue80RhAsJL938khcFHFu7k8kkJtsMNVZMq-QJv6VMimeYMeZXM3rR7IIOEoMg0tkLNFaakEqmUY7Y3-y8vvuzPnvpGfe3vbmG0MSaji9qkC6vk9QeDSiyNstn-JQbZno62bmDyWXS-na3kafBoYtfF-SyiM7aQ5wpmEpPAKWQXaTUwsZY7aogtdt8uZz7I0kJlXYk3lDg0-ZJfYdXL7bDG9vw7-VAEj1-2DoQHNQ8j046MvRzKR6Aoj82ljl88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtJ-Uq_2FS9IqsEA640VJheCYX6jX__bulf94qZgjXQWscpL8-YXpTQ2Xso8otFcL1oPDAANxjRyQNobxTyclZnqNd_Mb9d-NcIjoSrcyVe2uldBvS__lha-bDx6ZHez8LcphUaI3nAYgzz1GX4n57sWOj9jty1lN8XjB8wa70Qr-WEv7zwbJqUA--PI7B21IY51hk1xi1zM2Eu0ySn_ebkUglIQWfZuxPvRB66FSdDLtikkacro8Ycdo7BfldRIG3JvsBph95SrVjyQDh1kE90bt51pMZuf-1UCPDz-QyL9oSetlNLcSGaC42D2rJYFUm9QKybpZzsNajlFO22Nnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhDNBaBMDAODLNi7z6oRWPdfQYDh_fcXFi70Bjmaw2BUa0gqTQNbYGmsDAHXqg2ZzljN4OqcSAJ8WSuayCxSy1-_gJWtwxJwIMFJK28wAiXtmdjH6hyeNLLz347JhAIn97NI8USI3cgy6rVKFa1A4AHfjxhu26aoVK0_vcgO8geedLEdB-CZTfHuXLwEwRBsviDrPgqNMm803LMp3gSaU65LqEAkuxJ2gdOCvhsolC3D8owmCqbwrgiBSCSzvLqhCA2zg5zepqZG1lsKzUZiRV6W5mPeHLxrR5tC5zP5XWvM2Qy6xykntkVSiixkRFCU2QhXDDVAsvLoL75M9t40XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=dc0VZjQIvXa4tlEDX1Y1dY22jXZwoOooUXBBobpUdv4eCCSweXsjzFJGNrWb4l7kQyPUUztNoT7MjPZV8MstVZol8HFTovdvGXLeeoneCPiwhU8URvn8JTQW3EYy2dZzEk-2bvfYzK8WhLvQBqKqnchB-JAnV11HeQuLy8Sj7nFTifasPGpnpVfV69HHgre3jVSYmv12mqTtTkJhH2nt02H0KbyylvKor1zEQJL4XCIseMijU8GFQ1pj1aWhg435Lh9k7fz2ZlPPnIRHJuxnTxPLEkGkaWOHDTIgFKISrCULAlVGHe3ET2eLk-bZ8EyOyJnzQSPELhwbP3W3I2mIHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=dc0VZjQIvXa4tlEDX1Y1dY22jXZwoOooUXBBobpUdv4eCCSweXsjzFJGNrWb4l7kQyPUUztNoT7MjPZV8MstVZol8HFTovdvGXLeeoneCPiwhU8URvn8JTQW3EYy2dZzEk-2bvfYzK8WhLvQBqKqnchB-JAnV11HeQuLy8Sj7nFTifasPGpnpVfV69HHgre3jVSYmv12mqTtTkJhH2nt02H0KbyylvKor1zEQJL4XCIseMijU8GFQ1pj1aWhg435Lh9k7fz2ZlPPnIRHJuxnTxPLEkGkaWOHDTIgFKISrCULAlVGHe3ET2eLk-bZ8EyOyJnzQSPELhwbP3W3I2mIHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jW_9AatH-vrRVAk9j9XbU-g7rTzh1vm-TrVDAJ4P0n1G2dZcvyxNldwrx2kmvcrt3pDsqZRCr2rmlW3C4gbWlPcCO4cEKMIbC3yY06HSVGyX3UrFrTePWzXzx_w9zSJl7WBTAkGQUAH-b2DJAaIxSLJdOhgAo0BABlkwTYv3Zbpl2JBcrN6ZOL-r4iNtgDwR98N1olYZnqQ_B4yZwEp9-pxOgOvSKx9owSWa8JjUv2MVtVoWcenEnBTXa-W84JlY6xmlEM7SDLucA2IVtSy2-iinlNVd4DJSnX9zg1TKu6BfstpvCdlEDMYALSc2sUloUynthvTYE5q-qCt7PR2pNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eh6pJFKVVBlLVpm_2PlwS9KnMYox0H2b7t3eKbJFERJpUKDI_ghtSv_Y6l5EYbznC1PRge5DDoxB3aKaXx_43wdaniMHRp0AxDgjjzIEpjNicWeKhExKtMe2lTS_RJBbkRlnwLMTGTFp0HrV4TPzyQy63r48MJgEutfwr1OfKiB5jwhOi5QMpFlXksDz0LnQMjNHLYaF84DH9094NlYmdME5Q-PWuXPYAbCRfB4mjLKXFXs0teheJcXmjjRHlMb9vyWbI-gPYUiSSjN3iRl0L1eDyQmPyBF_-cMj5pa-cETpnOtl-RiNose-RhtIaaWlRrttytU0IPi0GzkpCBZyDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=PFxdLG_dC0OlMR3ymJRhei99FMXnZyVHqdNNdt28OzKPyrLlUqS1z3csHuDbVB3kXNO9h6FedkHQory1hFMOpyRrkTeJ2_kMAwNNq50KaeOdHOJPL222k9_gFKwlXRT0nq8x_1jSABcz3kgeN8SfTFeoeTTtQymk7KYbLMHxpKIlOP-Kx8MC3hy9RQ5_hDHtVXgkZ7iTJlD_ughkOsvS_GDkVkWdsa_rAK3AMb77l7VbW6r4xQNqqbdMHEQzThUa3H3-b-djcblsvN3P4e1Ib64xwiOw4g39kCFZK-D4IBscXkbI5ybzrAYKix75IH2OyZiC9uGOaSXonFF-ipBAQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=PFxdLG_dC0OlMR3ymJRhei99FMXnZyVHqdNNdt28OzKPyrLlUqS1z3csHuDbVB3kXNO9h6FedkHQory1hFMOpyRrkTeJ2_kMAwNNq50KaeOdHOJPL222k9_gFKwlXRT0nq8x_1jSABcz3kgeN8SfTFeoeTTtQymk7KYbLMHxpKIlOP-Kx8MC3hy9RQ5_hDHtVXgkZ7iTJlD_ughkOsvS_GDkVkWdsa_rAK3AMb77l7VbW6r4xQNqqbdMHEQzThUa3H3-b-djcblsvN3P4e1Ib64xwiOw4g39kCFZK-D4IBscXkbI5ybzrAYKix75IH2OyZiC9uGOaSXonFF-ipBAQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-Rpy2d80Iawm0dOaOAxr34C8fbnacbtHmrVBkuWAQR-bLy9LihRbZBQQZ7lRvSkgVYIYWmSUeYwrhGq45wfy6C9d96fqf962J-XmbGUpFndrGpdsmEe8hnrqFxCG4rrCaS6Hsm8akCtNmZEfI8C09v5saCSwZ5yq1TfMo0T7jnBBBLRq6iQxrHx8I0idn_kDxgmhnSxyBkRAHpyTJFxIUKB_aH8yiE47ZiWSZH8B9ckKHyDn-2ZLBo2i3HdbDC6s0LGsdf2ym8HpZUvb6xlaonRFRAvYQWima0gI9nR41r7zaoTQaiQVfZeaE5KfQ-SODJnAfbAWLHimKXI3ZScSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/adiZ_KMJw9CdpW8VSO7d58IfJsvpdeSdPNcKe0rWI_WKXhZT7iAieZKWd6vvvMD81SN_iMKr1uMDZKFaNLhmmGHVJAp61L8wlzkBzEatmZjWlibetIJ-NFEFRqzOJr9MGc8yERgXjFQWrOuC2ISM4tU6grbV4Kcnm04tgiz_L_PBdbXc7kmqHhdHW4J9fZxttx_mPVTAgolEOUX5LGQ2FcwPUSRJvlQv-PUx_0ohMiM380G0U2xo8CQM6fFQc3r5VhmPxN0EH5GQloFWQPf7Kky3ef9w8F4eViegOoNUEteAzB6Mh4c9Xcbw7WbIJX-qwRPhzr1tusC_w0uceicS9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2aEZCJew8kDQs2FOWOP1Xp2G0veLXIz4IBpa93xx13MWAK8p9glfl6xr9Fk9rNTYHQablF4eKijViEpElEUWvhK97FFZjfUR_bjc85Rm__4W4ZRezZnY0P3DTjoEjeIhlRgt4Fg9P0j5xOZCaAmzaEiV4AKGENzjKtE5yiSpIo2jkKJGlDUo1y0Gitn6otJRQyPLmXJrqdWAMvP3TDPSUOa2cFBMKW1syUcbXUbwP-q8LUV45a95XtlJQ6Wr5wuWyzKAmc1UkBvKw5g1G66qoveFpMWblENEWhRAy8pdnMeYymBaY7vgB3gtbsbsVtyZlpMZ5DsjqBE2WBMco3LwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMSbVieBktwK-cb521bw_9aRIMxBmlb3T5Sl3Zk6fiugORDATzNp6l-o_j2o5mOGGUCqrKT5gELkonVFu1fz-jlC6KxRTHsp57_rFa95qQdGZh3rT-b1mRhpel_i0kL_ya40POZ8l_eum39lqeVwYfxd3fPt1esbLd2BL_x6_c3J1VP4784yd5eIzA7GOI9gb3I0z7ZttTbiJjinx1MmD_SqoC1n1v0Af84ZoSbvQFDst6zmB_42xmH0r0BSHbL9RExeOJchTXuM61apWNlr1c2R5Rh3oBVwxrp-1ER85yD7sSOz-iIcJQnDNUimVeeV4RgO1yXhEkWvSrL3NN7ntA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXO0jmnUOOs1HCsRzEF2Ln1sIm9dh7DnPb4FmLy3Uyxyf8aAbw_EVXqWMP-DDw3JD05S_1tcP8hu4e46Y8iO0OyViN6LWPvdNvJtb6o1xRZRH_bo0qevyyhdecq__Wardudw6o0yghXe_kYptKNP1lekaPl4qdKVBlkLWKFXxYAplqvSsHOuRh4luOSrnNu9hrgXVxD1T7ksiMX5V-tcjgD07wXt3F002qgqccms6gvu1XzC0K7IWF5MEFbIh63cyif5XKNTMO-TSPCvSkNWMelsgVZ-k-ofJqeHLQ5RxGPz7LVy7w1dsrKvUpcM62LSa0B6LczRSfrF74rFctI-zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9abc1Xt54gLuPg-kC9KYmzEyX8-S14lHzDZbrlI18aj-GHP_SP1QfTiDsXo8juf6A-FX4q24kVdKgQAl9ZswD83_klRaPOiWv9k7OpM8LNvSGP-4zchU51L55FsN81N6E2iyjbLrFFnB6KDShJDblDMw2y6cGuGLB8M9tBjSm3xk6mXI54CS3YwHfiBBoZt7wGbzlSs_CIVxFYvaqTRA-Q2xKd_w5deUlNiY0_IScC6s_nyjpTSfWJcEnZ7ICDC6Qpz4fWL4zez2QjcgXriV4pKErJhcGQT6hIyy12fp-5DkaVXFuWstQni1gevvdmz_cQQxP2JO__ohIEpQlsGlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ss_xZzNku-Md_BJNrBHyLnn1IIRoiCyIzlSWalBluLfPWJdsSKL-cAyrJHwJpVwSYHSd7UL42IUEJuxrztNbaPw-tdMFv3yMAbtwDjsBL_pKpieZ1VRJbX7r8FQpx9fFgKw67uoN6ow8BeNhOAWKzeoBOCD1NEIiAbRqzb10219LrYEZU_4svK1_BXW0IUcRo0oRi6BjgPXr7Z2P9-G0klifgnM_sIkpshZ6CXZfK8Dn1aeBULpwphypcOsgCGdxYgU__-O8JbjlGIhqvnMQ6Dm3nhI8E9_6bZEZUL4_hPk-CHQwvQkBtEgwhBRW23_7Yw34NFOG35euskf3_mRa7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6L6HTtHdgEXRwDvA0B6j_PDpX6VOtbEaIuUPP3Tk7b-IyA-N_Nbyqc8390TU5tuAUWQl-5PhGQZ7YBZHgJWoS3rmpFQfdKdmoA9jN2tuG97Geuf6Gc4Bk9crKOjK1-eHbbGYINOpUWJVudF3NQZx-aLIcT7sFcYQ0kJmTIGgkIAQ7zv7l03Hklr8-58RcRo8hklJr6vcsNWqjBSt2USV_T7j3girtZEhhO0gYEnUA_DyXVdUDLAipMxZk1Cocb7QhHiZBEsmEi4pzy6UnJnlSFo5VracNSwbiG6kIKrkfUP6FIqgmlPb4Oywez5K1ceDzlUJjHMyIFSZZzwl5kCng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsIdk9BSzpwAF968_Rti8DRioCJaOUy3R7KdxAWYo-GvMgXDlVlZUouLh6FMg4ceoJmR8y8X7wZHduK70lRPmYyTOlucv2mhLi0Oz8N1fTBa1iDw3vMaaFKhRQjxM_wA6nTd-ilMkRl1SKPWiy8MUFmy2WEI5gT3YU09MqF8mI066R0b91LInzkGTMOjYKRriatmjxvRaZM9dLtkMYFS3ZUhWSuHtHckgTqeaH6zvIbtbyEhl7MZokLkRDw3TQ_uR_P_lxjU1MKKsYR_g05zguV0hMrPatGegWheLcI_zGjGfZwxBrpdEd_f0-usz9zC36_QHqVZCyexSkUbAYL7VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWqVSaZ5kof_zsXb_XP2XPq4UdRVPvFcKUZbR162FhnOpJLMI3pUSzQ3uCTvj5jFEzT29mpnL_e4uaigyPdF8uoFU9sBRrWdTXNon2S26LVTf1Nixshic_p-HDk0xrRriviotVMGkn8JlGQf5-0d4tBgZ8R2qapATszDbwn2JAfMBwFdCxWt1JWG5krBlWolHbrrup3HEqOXplSriU7rHj6fXyVd78XAnWl0YoDCkxXOCLvNUW3QlLyeIM6a5f8FAfTdrFL1_Me6Y8f3brsiX0YWoiu7A1AbN0SReq58rmbRkLcOziEgsPQ94_-FVwefXTjtIfujNhnw3ZsRq_FMlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wb8sfQtrr_7ueCb9-tbFjCJhttD8FajAcEYMvYdyziZSWqXCKR8SQd_gNCKmVcJQzjriD5VvIEunutTfvKaisdnWx7HA9-uGlvaI9EfMAKfR_wW3UDXu4HcDth21TZgj1RP7mlX5P8IMLpEsMtGt6gKJAhSlJh4Y4hyzKIfTzubdmoCMtFmwXrQ1kfWpJiK8dFTtjrDEOct3qKSI2CO84A0o3MWGQrWP30VmJuFjqkGm0RWsitgW-NQBzdw4NeSWKLHYMGhO9iCjGAbYVkpaxdXVeHdVupRSy7rvp-4LJIouEIsQ11Anz5v0KDs6wsUXdgknHRA2Q_pcNcyL02t8KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGoseVjwHG0pcEctIT-tMCoi9SCip8PQjlXboapZsJOYR19X7TZ5Ouj5fYAbGUgp2kmCVAMFvDXPMks3z6wBWhLfsrGQjr47vSq-NqfGQykLuOKOOoi2KdzblG2kYXa9-Kvo7vc4WZirJSKcNUYdjfoQFh_TRvJasldONaPe9UG2bw0R9lMyduheK0IN3IQVsAhpX0Dr6IHFG1gjYtGcqiiHLjZwOOaEzXH-mATcxGjtYOuEnOr050OESD9KNRkwiqQLvh-y4AEeI5Z95NG6PsGTNTh2DbUFXzPcPRmX9eHORSxzPBGNH25eCheJg2mbAj7N8pbONOvTik9SBreC1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdXobTOKTTzecrPVyiDt0VDnL11r23R77ujbxmEoXTAfA_e6jJcckCP2iLVBDwyuQ-30C_rMUNKohcKOAwlC1fu2fcCAy55e2h2DeqSA-WN1ygfSH_WHKqUOU4i5aW99h4sQ7W_ux2T8LW4K1yZjGx8rw4xQ79i_TtnkMzMFXT8pNai-11m2JbcvtJpfdyp13hfoNAnT_pfPiRdVq0qqyorCwkE_3eidh4kavSLZvNsQbqkiRGj8hKwaOQgWtoPfLC7b8neJje20d0XZjpEilJKivTAmUJcQqw_uo7SVd-merYKgJRscuE7xMCDzP66pzenpPStf-e82AWEN0p9E-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RY2vpg9ysSdkF_uQxTA8O7kFr0zs3_I4yadj-JKSW6oKCtbaugzszr6UURxjBP9za1vr01rRbgTYysBMJ27rUbOzDNFfFWbPgFNQFZXlq3B9NsAQK_NYu1dUD4dQTpnDWHNvKKUQTlRcG6E_RX1DPTj7VWb-tBCjIAEwCDfDacCotf7mTtcSULHctfVXq4sqqFy2COT_wAwjvIikWiK3wf-e57uZOOi9KwZcuWqOhMLPfzBrJe-1nZGs2vq85_eAjZ-Sih5cVDXCS_SaO_mHw26AcMUBwXB1QfY686bZJwV3XM1_95xRgB27iqWqPx0FNgRXyvFVUcyqzQDd0yz9cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=FHfEKsxHtP4K3Dvt1xBM6xzlS9L_7wczUZ_hpNB9IlI40FrnlqWp0ycXnPnkRAnu6kiaRjDW6BTf8tBz4DFnN-pFQhtgizuFfb9UJbLzNh8eb8WVzEEXsTIJOANdVvcDc4MgHrMqN7e_BmD9sqEZMExn0rn6gkj9dvUGI_Cmc_cVvBT5fTMUV0FblXXFhSOeWaNghvGKshvMBKjqq9f-GFTpKWruesrlwfq4kr4156gpacHL1e6JYfHBfculA5dCILCx9JlgmNdwrKALCxbYZzVcfgyT_sAWal6qx1ZcLAhaAW8wT8wiT0A9qNTLyhZDZ8C6NmmgbKeTxuM5zEvFww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=FHfEKsxHtP4K3Dvt1xBM6xzlS9L_7wczUZ_hpNB9IlI40FrnlqWp0ycXnPnkRAnu6kiaRjDW6BTf8tBz4DFnN-pFQhtgizuFfb9UJbLzNh8eb8WVzEEXsTIJOANdVvcDc4MgHrMqN7e_BmD9sqEZMExn0rn6gkj9dvUGI_Cmc_cVvBT5fTMUV0FblXXFhSOeWaNghvGKshvMBKjqq9f-GFTpKWruesrlwfq4kr4156gpacHL1e6JYfHBfculA5dCILCx9JlgmNdwrKALCxbYZzVcfgyT_sAWal6qx1ZcLAhaAW8wT8wiT0A9qNTLyhZDZ8C6NmmgbKeTxuM5zEvFww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7VnTjcuxVvQ1ELudq-CTwf73RC_llJSfbwu4Cg-NyuTiW_5ElT8-2M7vgJSX4xEE-exGNCR3npXjx_V3sqZ8dh66VPH_03-yu5q3zR76PS67yPNLWv5yS1UF9dvmSdTN2uZWwJQFVZitk1dv65Fenur_AAB3I9dCPigwHvPcDBPQGm1piUDRCAFwP9LnBH98Zf2SMlZdzYrpJEX_3FfRfHqIxJPYiOO7mV5UEf-Snog6TINu2FVtN5fWmSI8RgBEuZMTmAPs6HTfkhFMEab5ucCuKHi6NsBDPu89IYCG6CVeiTfvDFgWCoaD5i_mv7fntq4Sa74gveetKqT4VFzLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fa3epkn7SKLBAXp2rKUIzcAgOwe9LQ0g4DJRvWxFnvZl0fa6lQ1qlJfNQz63D7xJmOHTKwGHkKq4IctusWYI8Fp_KZ6B5fc1AWnWxsPzARz5BErw8rWJQcjGiFOZQj9eMJa4oALFQvkRmMtjs44Pdt8HXLUz-Ea6anakHBHn-0FlZbtDkoMAmKWGCK18UOeYN1OXpDKlnK_0zOk_adPiDdhICgWElC9BsCMO6ks-83fsgtJVW6nxkJHztdXetO-d46zxxFaLndvvJVa2B2-aaPDAqv_P8KgL1-Q1DS2sguW1zqFh3qziX4OVrA-DPXZxewOqRj_EJTvl9c0-s4cPRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8IUT87v9r1Qwy2nEHVMM8fAVChM8xXGMuqy_MAHw74urfSlucYyq8ww9nY9LbLG4CQ5LXTVMRRTwAYBrHyB5Dq_PgG53EEUFTQ0k8GDSipQ-74iWi9KRNLgi0ZImz271sbJ8ZCaAXmoyU5iYQ9riplHClm0apz9XlORCbekxfo3L3ch2aaPfY642xfQHJW9Ekh2uVJZcsU-39ebtwfKwsmfXYmosnp3YngFUoAWxgWSe2IKAJlhww5sR0p7stioCeab9a6VjiWA-eqUYW6xmvwIJ-J-cgXUL-G2lhytOkKGJM6rfZyUn1jF5G-vebvZrYws3IDBx-EA70SgcPVlLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZ99cPC6pS7ZBWfWOulDmj-LzliuJHaBHwBPtzOZTtqa4R6h1jH8WJ06GICrEKrgFFSRgA_dP3SCbeaHDP70W5gEDdQuDC5ydxeFMMS_q8cwZp1nrmOCs-VAwTRS9A88-u024tDqcXJNQS8uN8AI3JexoCa-BcuyohXBUwCqXCdXUmKD49jv9GENUR2yBODnxDxPLNSXWgnw5p3CJDQ7xKt3jssc0CNKlwjHLMgezg3hjIJ9e_Y_72LBkCUypk49vh3dvx8WLuxVaXSrHSMQg-mTM3vtYw8jcu2Pzn5jP-q8Sco1DwTKrvEG4x9rGrlJ-zrvJfJ8H_6JPiiP5xjYVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPVM1gH43RFQ6VVuwdXrboV9Y3VyjO3Z2JTVTmrhRAH1aJjlDVV6--5MZKcuRnmQCNuLpqMCsUBl4KFbTgGbMRAzuWlzO9Vq2out4vyoSAGIT-11yeOTGwTrFEna3iLEVs_foStdQjiIFL6jlrGTKDRpJ8HZQwDisqCdUx5LKl7WuBux4bhZwjeKsJY251opuYsc0EueA4Kh6ZayfJFmHjyV6CFL-BSGakMFr-dbLpNTK5ub4HeYRVtcI7XO4CMwJYBmgurALuNUvV62ZGPaQAEZp3TZwNhvx4bZFwVwaRNiNb5ZhLTebMML2qVzHDC8VZZhdP-nGoAGbNJgn0tqLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8-Z-7sWN8gpx2hNU4rp8HA8Ebz7KG4J_gX62PJIkNTPyUthO1lX27MktJG3Q5K8rAckUyZGz_4dg5M3_q3pJH7nW-PHVaQUTWIe0RuCppTFkLuhcFloY9YcNPpQy20-sUk4MkOvUCYP8JgQp-zGMD4mKRZkaKzcNQdYJgwDqUdvz7NK56KoXJDjLqIqoU33TOPunQkX30uemIC4OyVL4Y17k2HVulo7BkP-xCDphku1uKSp9x6Hbt42CMIiJXEG_ceFCIotOwH5hNnvndvN8kde0WhzfHbUfE1JqA8gwIDX8UuBnP9H6W3MH_7nAILRUuD5bfIYSfbsFgzsCZaeEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoT3rg6qkAURUtz8fMoNZFm5eYrcTHa-qo8QVHjIBE4MbyGq4UOY4gpej-2UN65e28VVyM0AA242llIN9Rzckp8Gq5ZYW8LtASQcqVMVK0QnNk_kQLr7ALJxn4gV6ttdbwEy5nELh0wzeWkAnsnXJCyAk4xOiD3StmSJPtEdXZkLWr1_27USjgNOlK8qXdMHPsNPHmDAbl6RLIXdnXSbHNR_zUAgLY-58Crqt0jar9ddBAB47YzX751nbIhZ3oesBksavnceMUAq0IfTfWHD2lhO6kY13UKMdRVHi1aerUCSKr7TYMqv1kUy-NrNK_u_MjvLI_7r2gXuAqEwNARMRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9n5o7kpXzq3Ut0yYn7w26xUZxT0tzRhjNXvMWCCYaBT9s6ZRw3rytXrreN8xTf5Fs8613JseXaWwaCTQQCZGzXqZ8xMebSHAef-Zm14QhutWPyg1mup-HIUK5VfaIhA0LmgvWet8KAfzVHPsn4II2wziDgI7GxNcw-vvVmF2TnXLW3l5y3CaY1INiR6tnqKJxgXB_sFVkxiVJJJaVqSVozLjL8a1sWq57Z8m6t908_dkLsBx16q9cgbzdHGDEGlmXuBJHBlh35-LnZBdt8nBF_Rtony7okjl0FMyEamw_MWW2iBh8LIglb5GHN0WZaHDf4IyUKYRMs3IRT8pJvr6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYhrnbB9IHN6hqwvIWq5lxoOPijcLTVudYVn9vwyR9tmgwfsSiZ5YK4mTnKcvW_ghuweNnoFrYeNYy1cOxTmAvHR68q-1EJgNj6eGjo2na9xvjFf1IgCf-6D6Ma8qFlya0ucwu85vJcht2JpGVBhO0GXd14uVnOKNp7p2LZf6XEqxyfONIHJZiSC0KP7fq9fPBv0XfN28gecOHbg1Ds4gMZd6Q6iFAT141f1UsNrrB2IfPk7WKsojbQgj1sRoXSbm09oOKio9FUjUGYm07Suw5IdbR405wJkZTi9NhaO8sv3AuFTKzYjFkQR5v8bQRyAa6DRs_9axnGFZ7Ctyk04TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lis4FqQ2H3E0eG3aFj76Ey_qx0OMijxYiPoXoKHEnjpPRJUKvm0eCTYXmlw-TS0fgIuwF25f20fEiEHJkubfZ7SmCJ0yAS-x3nPtgCUmOxDH6mP-JAbOlccmtaZQov3z340oQXaE5J9SbCSXHpEU98YGe5j0X39aUeMFgbH1WYhkXky2-mvukBor5A-ae7-9oFanDVeTsfT1fFsGPNQJNZOcuaCTmXO3PfhzXH_UOLayvJNrfPhfp6ayHcAEEjHwrTFaJQrLMYJE9EBsVJ0k6asyvBnjX6r2NPejRTI09L2MyhtpzEpZ4GfQas-nyH_dgvzdeU7HFrUwlyawWt1etA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xf7DUhmUlNnYFjHM-ASryHOsWi598gqrA52LelICDqSUWzeCdbVN-Ye2vc92oru5BPyRsffp4rTOtYts24DDCnnY2gZRknIme3FDHVH6QKKeoMhBw5cjhLbzVX1EJEG6xnUL8IGLUjnj2XUmQz8N8VG_I_i7UY5jTjFa8VcDHP23oJrL_Lqj11XJPjLc7ZLAe3gxJC941Bve6h7CnPQ3Ynk2PJg4IG-ypvXd7SKx-9pW5n1WMpu0t3KxvnaMZF2uv3-r77LFeAFAcDzQq_KlqqH5L8w7A445rN_j-3UbWOygm5ZcFAfDRZlharWGIWjlw7OjmAA8ufZ8EpqaWQXiXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTbqC03xvCqLMc6QzjIdkKODJju6zlxIlDw8ilxC0TU5Uskslh4ZgkDAPkRzBK_RwzmcJ78KrCF95pg24m0qzWzmhvj3AcDQGrh9OhBa5KxYsbUoPsLw6vuKm1xVc2fAIzsJgru7_jNfl9yyE8nqJplxXUJAwYI5Mr-3iPR7EJarutOEcC_42s1qIYK3vYV99YVu6-eMf7aGAJWxR7ya5Zuy2rnw2bsEBhzap-dY48oltnQpLBARuoox0wFIvE1vjU14kotWKTiT22oQQg7QzQRGSy1-IZnUZ6kIxO7ljZYzE8zNXFqgXnXIv-TgE--DHWDyMqULAlZby7nqbZaVBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDQYppa1o6UGDjjaTGwPEHsKVIS3sN3UX7wU1KJg4ucviRUgiOCX22yBbYdWl4BEPcxsy16zZO2JdWeQjbIK1hiTS-6aHgCscbPhKAjHnmC-NjHCAmmvmnXbTZdgQU_S9zcLvMUJbTKjlVz6KmxlylBmlRwyJ4Eg1aD0QQgvSKeh_zE88fLTt7R5rzKd86sRPEUEHTbQ2Xnm398H5_yTdZ_UZI6Xf4InkWsxNe_xoWEIV8cBabaPtdhz4HK-Hsr3hgl5CswMw2AeAvAodWGiAH4AaD91YVKmUJYIEkTZ1UcUPJUAoDDpRbxv7t_C1ThjtYZQbh5Mdia4VzwCGCNM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTJhv0_4b4U4XildSZYEwBXzjRr0FlEFeN6FCzFdtK4rX-9SXggyGj70M26aEPPCxry3owAX6QuN8FNfTkLhigo-vBHBIkkga7HdR9xviC6eBThiqgcTKM2KGcphYjftqIv9-Hz4MMy3vKjYYSuaMjoyBTgYbJcwZD4nHK-9vWAQRuyiUuEHAzr9ml0KR40aSxrnwOcJM4wvLB1pflAo5B3eFaIqXzXACUQv8CmVTyEauJmF8OC2m0vxmFuf5bwrmsUu9xYcuvWpJG0UEDRX4DaQ_NpmI0nTzG0IYjNm2SYsU7p0_yMz-zEHj-zwLOSlfUZKfHk4ZXh5OrQ0KvlF_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxPMhFDv4GqEiABTE6MikkWrdMb0BomNH1msDkHFKggDC14qPyuUwY4R82SXZdKrCUuy6G7KMZgi-25FYOMQvfyWP_jC0PgbpUw0J2FR55d8KAeKCAOoCSMPv4d5ULjUpT4l5bS63ofGrGau2-mGcKClD3wBdcOSLO89XyJH4_0H3GLtJZ9v-0cg2bCEoc1JtMU2c9w0ARLq_259mRqo4bRX48rhB1CGahqwDv351rNKC_awjoPX0-sjgyC3OAhHh-FkKRDhu0_MtUNqa1U_Ad3WbB5r7f3teD0YmJ5TjonN5MZQyMJ71eYCPn63H9lb2lAfl6Up49l5JYxMPYvHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRH21b-TemGiigcxe-0sPY4A-XxP6xXNY7L654WrGvw5XoQ5Y-aWMO5IqWZxLW1XtfWd90rnhMBdJMSdBCy_n943bcoGQxeHd1o__7KXr5Gfy3tVDjX8Tivnt3VgElqhGo7t6yrO4pFSj_LNoYMQTYZfG6d2b9AREBqXk-g0-W4jzFte00oIkuZWwwN6KoLwQJqItQvG9Qdj8xGbQP-U8RUPcX1syHjhH-qZabxxzOGAbvTjN_1u_5dj_83-0DxIA4ZdgPCukmEqUN1n7nMQ8J8u1SfdQ4sZmROY35FM5ciBDjWw_kIcb4eFvhyzJ-61aXfHdFfDCxihTYBl-mcINA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5OSO9saDOrjNAgUvoH2ViXg33K3eDQ6RmvmNXQxdD0hV0GF0OLQ2kOXDK9Csacl09i-75Im1QIRF4yAyaeck9yZH2buB4Aor1NyDjmZVyG_5U3rj65SEppvxoE0FII74BRCUAyyJdp74NkGnS6hMzwWAwhoroHjec6CjM_n_Z9SJF1FRlvybvX9lzG1a9kFVLppcWz1LTbf5UwADkr2DIJLsv51Xw00r7UyTMZQ2uHbDFi90AuCLzgDDUZ2J2BptOdBtqURwV-ls2TIcFzMkpbCv3pzbCSngKinTt7ko2JlTHRfhNNsiVkQ-tWKsRbpv_hStg4gbE8av1pSksLh7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTj_CoEsjVhOh6i4nmAJrRC3aeCdi8kqvaMH67j13HI5RyPcudRr3OTwmio2wiX-ZdBf4GDKdUm4evekKxo433BOejRGjGLEsoJMNyx40tF87qmWugBDfvZzuXQ5CT3AZyi5xkcpiGdQ5PiV4w4X3Y55jN4uuuN0W8ZyAQtHMCPx4I3SGvy-pR03Rr710102rC5ehBfqJh8RHpQ-EQRdCeMvZaSZV0RbhlAvc2-VsPPBQ7QGvpeJS9I2jaaIsgfFvrAXbZkl2v-6b_2UGyf10fa4a9_L8pitGK4cIHg6btlBkzmIJex7bREgxJhhHUGwPClF0prg_w7pByqwem9Z8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYXq0QjbpX2wX_ui8u-X7KQrkKpU9dlUil9OOnOiZmTk0fThJdbPPSQcuBtgETJx02dtoQN7E6QKQFItZgT42FzrGzEAGJ4tGiL368EoDYVEXrxR6Nzfcx3dBhffP5rY06WkDmEL0erqhkMrhC6Gzv6nyriIxHAZBQh-c_snyN6-yjhhg4hLrYmrKgaLMYe85aEiRYnG95G7v6eSAnoacLNWO52xwDoHkEZ2GZfDHdIjbW-f-dWDrF86SMymeSy40yZs_rnMU4yv-IT4h8VQ5Oo5N3-3gWGNA3BMdznPqRQbfx768jguudHfhZFAkulQesF_pd9s8uqyub7YL7RGDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXHiM4gFdKX6QY_9PK5MOc07UAot9NB5se2bz5ecI5OJGqDYqBkaPDvAcd-2AxTKQ4PiyyU4JR_k6rvbFQ2huNR-x9kdc1rah2YfCUvbhf_M8rsLZP3WFc2FO1FzzYB4p9ldu8of4PH1odAQk1aUfQ3YZvc3YQayyIDDt_MkdTAZIq-LjruXL69jUExFllp4o2eOsPe_x5GKNPoJWd-MDSWiuyk-O2zm8HOGMD8GWT_kkjLyHzAIv13rCexIOXuNhrhjJEEIMvJ6_9PmsZPg8OfiXZMDAmB85SnFDpajsuvGhM4yyR9xtAHLgibFpp98MWvNgdwmRIhat69kcE3TsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnp0SUIJT_PetcDBECixDyBt1x0ZPa_OIzn2-ur-cwpWXP82frQ4rjD16Mk0oiBBFwpNtb0EHrqqwYCqPjUcsSL9RRiFN4S8JaPlGKw6yPYvDe37ZLQqwQNf5kE2CFiP1pPIoVuZ7jNY_01ORcCWP-0E09KVv5bVcx1NbDoCXPV7IP1UDvQv2srh7Fn7ut-XOLv0065J6OKCGrPdLGp78BmWGmhxKGSbp1L_DPd4Ywqzuxx47NucPZMGBmM-oRSg0euvzLD1nHOOT73VaXDKBHB4VDgYmmbJ_Iz1lWkeaN70gGrZ9EER8r1Q6c3kh48zEMerC6rBETVwck3DZCf1Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛ رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‼️
هایلایتی‌از عملکردخیره‌کننده لیونل‌مسی در بازی شب گذشته اینتزمیامی مقابل تورنتو در لیگ MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcNdxncYmu85xfHPk1CSRBXDJ3g_GWrjs975xW48sPE-KNxnu3z82kQAHZ6CPPXUSgqDwtzfqbkSI_iVKkG6UMYzUjNfqFGVFDpOsH8y6KVIlp2fzj-dz4f0tgzRdK3xMMLb-3dWgI_utAnsfNXK5m-DcPhfK3vHTQWCS5_YETfGMMfcOtJn2MmoUTv01E5ryOLsAtID8TBVeLzZiFCDlfmgyMgK5C6B8MiM7aQVC7V6Ki3qnF2UIP1mqqBZpFhpcFgfdEbTALEFNBBUdNNEas2K8mQN5onGoBjFb3CO2hNEPe2EIurl_9sfBtMTSHgAXMqcw9h1EQKWXae9XBetsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/op6ph_PSLqLq9u3T9s75RyWjE_ZeeYXpDZBzOOJCKANNEudEyBPhomjqc4cPuBTwm5XvfeM7LeXu-zJ-VI5JOO37k-c8HU-XaAip7ofouWcx387TN6Y_T0n0GBO0Ic0248YeNfBTmNit-_dekruMzchR81-ucD5wlHaEzHAAd8LXU_pZYybAbSgChOZxaHHw8t_XOUF5JP7BCbT-XT-37Zksmjm0AfD86bTe2ThFuEPs4mpYsSoBnWgdwalvYuUbL_9211a-WoJsJrknJBta0tezpqpIzgDY_2bQdbgt7BOXQKyqwVLs4PjMO7EzWo5tgcQRei-Qr_evf1KA2cGuGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=EMOL6-CFuZ0fapbZSlOv-4mEC4oDb82DZHXKyI2njjcTIbjGgvOSmSPdURI4aRMu4QbdGu8ITr9lM5zWZMvIVrgv9EPDqhhUNBuF0iYWOWa4_xW0kZFzOuKNTK_DLjE_3raHEVT1WZR3QGRhV89P15bnQqPHas2RYGH9tMiavzvJMilBM4N_nwQRX_TSg2174KNQwU6WOiH-R8Boqnfy68Mha2d27FO-bTMeAZuSgA3YbGtOB6yjGqjuiUNdD31wSHVbrngRD2L67-v4KAvJaO_EhJY0AP6ReNbmDA02hW_tta8RiqjrbvOBaIqvhQHYBcOmDS4xFYGlM0mld5PjnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=EMOL6-CFuZ0fapbZSlOv-4mEC4oDb82DZHXKyI2njjcTIbjGgvOSmSPdURI4aRMu4QbdGu8ITr9lM5zWZMvIVrgv9EPDqhhUNBuF0iYWOWa4_xW0kZFzOuKNTK_DLjE_3raHEVT1WZR3QGRhV89P15bnQqPHas2RYGH9tMiavzvJMilBM4N_nwQRX_TSg2174KNQwU6WOiH-R8Boqnfy68Mha2d27FO-bTMeAZuSgA3YbGtOB6yjGqjuiUNdD31wSHVbrngRD2L67-v4KAvJaO_EhJY0AP6ReNbmDA02hW_tta8RiqjrbvOBaIqvhQHYBcOmDS4xFYGlM0mld5PjnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027
؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22069" target="_blank">📅 21:47 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22068">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-9UZodW1yCSVttDveIeREn4cfu5fdmb9kR8emBW-OgI2038cVcFAfkj2U9wMb8PXkjxSqUzckgbTkr-lYZ79EA7sRDbiIXI73T_3isKeCB2uBM9oueq0y-FCtK_6JAzuSpEXJt31RXx-nuugxUlgu2qzGI9savdEgJPDbE-5bMG1hbPW9tnEt5sOtUPBHXHgMrZ2k4uCqnveCGcUnstiybCM9AedKO2gcCyr3OHS5HAdQsZyJtsi7p3JTJFxKpg48lXkL6xSto59_2_VqT2Vf8sO_LYUb0PWGITVZ6AH8CUhhqmYWYOvRm4qoqfBaPV3zx-5HoSq2INw0uo6p7AiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
