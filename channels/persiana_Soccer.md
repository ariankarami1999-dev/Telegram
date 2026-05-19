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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 20:16:10</div>
<hr>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
متفاوت نه اما همچنان‌چشم‌نواز؛ رونمایی از کیت فصل بعد اینترمیلان: لباسی در قامت فاتح اسکودتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/persiana_Soccer/22189" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jX8DSqAdPe_rgnFPZOptpPkFATzNyFcmTPCj9vh4dHUMQvId7qm6AhurLeT2G-d4dIq5WY6bmBGX6j8TpmMUVNv2wV6J6zBsraMh3AO2KC2dcMENAg8kdXBERJTWNCdkjsiVa0IQjjm-85tm5qCh1LiTh0DqpXLDLT7hBqaK2nZIY-cGhbccJs4iA9ZRgTb_b0zJ-QeccQxSXAGDypn3RAhrIwMdGaseJCvWBP9gZv5mo3AjGf_KiOYUWQYOZ9UOedIThh973zCmVkQu-BLAQfD7CZicA2crB7rYBug1T_84XZtGWDTN-3ZPR3NWjqeGlU23xT8LR40oPpKBEYjhjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/persiana_Soccer/22188" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgZisqJ2pnWt6MfB2I1egbUCfSdxNrjNwedphHiZNg4kHewOnbp44ZNR7n0WUCS6pXCL3Nit2cP0ZriGulpaB-BMWbv3hNNBNRXXR_YGVC4Ky8_HwhXXsROlWZvyLffFAZp3Uq4ipmg3r_7_A20OwhJp7DFsMb2D3OM515pgSIyK3bjm6HhFLG124e-HDLglJmX4XcWt407OAYmmFFmqcDrNJem7ThW7pge24MAVptRnwIXKwyHfZClK0SG1-0FqU8UU7pgp-i6bDOqqAnRQmWEwNphhZS9iF6CW5kJ2WXB81monjqpUeL95FJ9zZBjuFV_vAuNP_27WKrZ_0MpeRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا
؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/persiana_Soccer/22186" target="_blank">📅 16:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr6Zc717NnwcyPc9GbUKf7oATjOFZyxX_VYhwdm_hVCCF745v6Zp23BGXJY949_o6hqHdp5X1Mk2w9vf2mTdlsqc0EIz5xLCLhf-sPl2YvGk1T4Ya7fHmmn5DofBUlW3HSxtjzGETMZdxV0jZvDDDXgN_01jU9yHgSdreOeVf3o2UE1oExHJL1HguPk3xNE7XOJty5kRfqiU4eyB3We05MkqQiZ7Y1EvUVkaccIJ9ybnGj4ZWaJmxd8HreppsSRxu5NIHJg16D4ds_qRMCtIHXZqLWBFyQ_H30McB9SDm9bfiGA3_N_yuTDuR-c7k0oz60Yr-tDM1-S1qAp4mOAb7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGGTRfG-IIRXU4gy88H5Wbr-rWSSUHHcG9kP6Rl8pp1MNHyNIhX45rlJ5_Y0LXBAfbs-0h43C27qZRLavvmyso-apwtgKXoAVdEERZI6fs_tD9kwZW6-yFtFBWFN4mZkc3C7-_2_qzgRrQzSxCbRIEScwewlYsTHvNYRGLyCnNlwM4N0_qR5dqky0hfg4DvKx2CxT3gaoP7mWNIk4WPJrB8Pp5ShY5JkQyBx5NVjV8Dv0Y7SlupU7Uvv8eIvKnxwAKnsB11I2Vu5gYwE0SQZp6B3VJDlJsrTX9j4lMtBSyW8V_7sdWtFpZpFYNSam567iEsiBv_1M8l6pN9Pnfi8PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/persiana_Soccer/22184" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/persiana_Soccer/22183" target="_blank">📅 11:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKZB3K4UFASRPJU-5lhPEYt_hFDUrNPx-Kh6yeTV_VIurIQ64h3QXAoI3J7zeV4ZiXY9NuPF5mhQQjFwpDGrWVkt1qTl56DiaTSKGdhkwyjX0xaviN2QDwTSl5_WSY0LQnZ5HXJYEOJkeIF287dkwmRNoYsP9Y2o_eh8AcWCASljseBx0HeJH7Sy3d6hJ8NuWHyStLFwZdmGDdtGDeY2-G_hlM4DiYZEEj0hjDIl9A_CM2NKjSflrovZ6gNzYuwzlTctXsUgXd8J0Cop-dNBduWmowwmBj4RwyPoVtRFDerDOc0O29hSjPUg9lpQ77eoiRfEEdWbvHmrV7aWtCBl_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ پپ گواردیولا سرمربی سیتیزن‌ها در پایان فصل ازمنچسترسیتی جدا خواهدشد و انزو مارسکا دستیار سابق او در من سیتی جانشینش خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/persiana_Soccer/22182" target="_blank">📅 10:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvN73u2s4ctqoiKKh87APKEYe2GQcS-gSFFuo26yTMIccxYYEh5udQB0TKIfHoyQwLlX4VFnnMHfBLubOhZmC17vbd21m2NjrYCzjsd6X-igKISJr1-_yQFxI2IcLiaz-4vTTy5UqXKGzFMGO9EfccX_eh814J8jXyHDZYJbNZCqpR02XXEADBgp_rEBRdzT4E7ojJXrxBmJu3VYznxW1l7sAlhZ0iIDbYM1KUpV_ZqdsZIhizGs9NbE9hD2bhGve0NVFYQMdmy11Lotcm_gOgYpmCy0SL8itoPy6y-4EXYm2U3FO7bYt6G33OyosZ0Y192GK5L1Z6n58pWzkh-RGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXAshsE8iInYtW-J_WPZzEx21DTtFBBmobWVGjTLRLMPfzM8W7L0V5sU3l79QmhsB4sBZWjBP7hbTnzfc7qrbGLEaFtJPMQbC_culHJsITx6vZ_ztJ7jskDMrtdBjYoDm0e8xMK7QtArUFqh5YOoIrVnZ6nHYdwdENRtHPS6fNMi1vH-vnbXXZ4WFk6Vjr31GAEkYNU4YfZsMMYOQvBTdVRKrr9WOQZBFuEpSU3wDSLSUd4ORlz1SP8zLYE8Fwvto7DLihAAfUyuoc7k3KhxcQyBGeTNnWvJxnSWlizKjaLUILTU8EVaaB5wV0Nno8GAnvJlMwI4fPIU-0pf5vsZHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/persiana_Soccer/22180" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXhMoeQrNLHKdqiuHkhW2yuFpiyUMaagmQUkX217eNHFurgoTlwz-FPTztORdFHVhgA_LCrn-SN-qO-oxkmrpqUUQib9wKTW4R0uBZr6mBlbhyHz3o2Y1bYPFvBslffvRkJsnElkqbWA93CdxOcX69vqXkaPV5wvT5e1OPUcbEEkOxfNKHTAc4XFgYJS8hOtaHm_hwykpUsrAHAMm7qoMT8bbADmSbdSrUPY6YFzFU-oN_E84lB6cD1nwejF9vfmRFKwJjEhUWeRi4QSp0G7jOtRipBva7DCZ4_q__v4vZ_2MArocYVBzMQgjD9lYMZrmwDL8hh5FXVPlDKFpyESlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه جذاب افتخارات پپ گواردیولا و ژوزه مورینیو همراه با هزینه های هنگفت این دو سرمربی محبوب در پنجره های نقل و انتقالاتی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/persiana_Soccer/22179" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/persiana_Soccer/22178" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlO2khZZOc-l2iN0Fw-AZOI0aO8Oe2DGzolcDsjnYXpdFXoUffAbKIaWIMhuTUAvsaPPuLAnjH-znG5nAVp54RgmYhZuknizGLBJ3xeKTxP2sjiVbWLrBzE7dtJYehyfsi3EmTPIh18oVbpso6Rw2kriinNM4MUpqX02YqnlD3nmo4zmjvJ_MoXLXyOPgvyS6iMfMrcThbO71qsM337aLR0-F_-fK5p99BlLoEKcPFWoVprqIBj59oOm7zPBkIW7JBA811kNM7H9a-hLyEEl723rTAVkucrU4oDDFPUfJkT9oeGLNRB2oyUnDqLx2UjlBL8ursJZhEsY1c-Hh0rqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P94PeU1qGruHVQxHPaTXhsYluX7IdOQ23WrCM11DbzrS1lihReCEftKCrUQDnMuWbihpHiVNJeyPe_Q-bA5yCZnLxK8gd5hDQyIXoa57wkZ17ZMFRsHkzjG6jjxyesR1nogUNJsyWLJBOxcpv_1hWEtXKLQUv3jNhY017VLVSbuMa21ery2AcxHRvn4_AtZp_7k4NEQCZmleBoR9TwBwx3MbmfYbmQqV80fO_gYvLKncNun1g7YH70ZHOm7kyIm3m7tzvVql5hos9o2TGFJJJj1lS-58_a8NTotjSvyuYG3AXbaC8BczfMDk5EDiZU_W06LHBUKXCZkF6_Vs_lmx-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2MUKQxcPPmbBNOoWeYX7m45cfKClv3klSAe4xGnCawy5hV7fPXlUwkqFzRVqrQYKRanEwc722nZrtd2pOCjA1D20RofKn-3Migo49ianpouANt8CN9KDde9dnl3OiQ6486-7H-wiW-g1KLBvbycX7q1Ti6ZCzMZftso-ic2MbA4D0Ka5bpiwmBb3zvBOcOCpMXIN9-oRrSWk5YrJEbIaykYRdARd0EdJ-b7TQt_Ae2J51fBTHrXF58Fkv3EEKOZLq5fxDqNoBjx6GkEY3v7P1u3L6PyrzxIT5Xbmg4XUFQfiRD733UUsUfe8SoXGjK-tpBeTUpkEY7VJkjjKkfO7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJWT79kyggMDDDVjWGxcIvVVmShx7x3SEJxf2fw62LcziAaWWc3ppaM8MujFqJwrV0jCCFC5Jr5gYvPdM-VnP7-pRQF1_hTuDCPPj1QR7rx_RX4m4XR_PsZeDzGiFnafbs3j5NRwpWyK-gtWZ3t79-h3xe6E5ONHXCRdXub3-BSXHFUrTglilGX3BVwvIfszCqQGw-1BGk-bpzs7EDN1xsBamd8ylR-qy9BTYuF4h4beoN4Or7_R31WbFf5FZTMzvhWtZUM2Uzou9maNAH4PJaVdROucPFQ7CLgohPpjQ2Agi_yxvsDvQ_oBmuLNLcG0jP4w7LtUd1FMFgmBvNAyxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSr7TIjKMud3FUWVpmRCkQDB8PCEH-a3iVpeEqZfZVADjXKGPWW7dzJ7zbrilEYR5FiP6_BsF6Bqd-8v1uOXu1L0-x9Hjer6LLVcoONkE84rGDXXtNnikq_L6BEr2ECye-PrNj0GEmEZ3oxjzLcKMZETS8llv8yl6I9u1rpPX23IK_wOOkNnEqDSZMQ_wxkE3uMxCp2H3GBx8rVTTnvnFC6LRhgPSvHVgwKAt6w4qtsWaFnJ-pepgc0PRd40TCr8S7Txxicyi1fz7rMRgHLou9_tVGOpA1fJI2s2bhkeC46MLlJGkTWyTn8HAXs9xzPRPAkS74dBnKrtnmo4GhVfKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBNjleBKQjQMO41XG7SThd4uR3btXQWNWO3GGahjy6crFgMEqOcMtq21heLEQWIw4znBFVfivw6gTuwisX93_bdlgx0LRTcjYBhkoLrMzCS1rQWCVykKH93gBn7P5_zCURYHt6pN6iEvEikMhF5DyuhCZvtDcNb0QBz_kW17oGY4rkOFLZBoO5FS5bhxSU0JOIuc6WMRmUDSNs325Xg1JpGDBlQJkFR43rWDn7TH3lo7UupZoMzYVpWOc9__LN_m3sEnWf6b3GZGzdDNPlUdmhg5pU6-JH7pPveKBkUoPqVxfAVKO7LFGrM3OqTmmwh5teeYtfUN7tAW_z3gB09YMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZB4nurb52KgREtVeU_k55jXJ3B4f5JeLrvTuy2Hx6NfXwilIRUaSEWxfHZvl_0uRW91IKeUBH1IRVj8wqv38kiNPJauswX06TO_qFeCrFMOUsyde2qD7w6w2OzylS6CvqpPp-DAAlnWyRHXuf_I7ty_wQ8f39Gb_7lH8rHuZPKRzYV1TOqY-H_x8N8hUhSsxgq6Y7Ps9gjuWRVpOOi5v7nyx-9NQGg4bDSRrV9dOo7xDmvxECS-EUGcwG6Zr841jaaZZTvIlw7y_cTWPY4qqmG8teTMH8k4_UALsuyg4RccMVSctiyCblSeWh4V-gqmrOiEzcaoewQ-GURGUF9pmtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEwq69175tFgRfzHOvrHEF4FIwk_RUEf1ukeApK9EOuyHrT3jh-LvRAOWvwGifVgHg9th3zra7b8i8T_hmyNGZ2W85NO8AaAj2AnKKUf-MD10PMluj1e2p0V14476nI5h9jmWlaQlV7KTP2tnD2KnCD6VeL3yN6WnM943GwjGC3T95wspEI4JLA6DMRlzbWt9bFsaUR_PDPsJHW8yaO2UY4ghODtUSKsFsVD-VADv7D9nXRlvWjkqV2Rktm2ixovOYaT5KvvfkpzO-rM8A1tqW6hCF0jHvj1Z2dG_yeisjxwHcQNiQJYH94rwhsmpRyG_GddlRmiXRY3qRu-g_HcYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kW9sSi44LEmppqI_bwSR0XFi1C-Zt6bWGPAcwtimZ4aHxAOqQtLbHwvYmYrwPv1EI57gz-3ZAesoxUdnMEfhkLgMUpGbAkAbPWxckwRyUk2XrJdQvvBL1_dLkNqCN2L4NJwwVkyQhUssAFRQqkgpV_qB1rXCTc8Q2Z9RfxzZFbC7aVDkYcWemkzSuqDicWBPZmbvPlj4dwOYAzLZuhB2sEGbHNENKYW7qMlr8cV6Lc0u-NoooqdgKAKKPa17vfXGMMr9eJSP0lpRj7f5FU5tig-usd1z7diMDJMfrpnby__IYwPkmb0G8lLppkLHPpdutCAt-Zgr9m_t-xuTfkT9uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hF-fJkZG14oq3ig1NFr9ApQoGt-XN9pp5z6IoGJWAu46hYbySea8dojqgSwa1zccrUsJxgtTKtBxz0iZcagN4bIisW2O6md9r_qXlDkQyvztSSY9vXXqXWu7dO25BYg5WednUYijQj1Sg5mnxS7d8K7bpb9jtHy4_jVdjWCxEBdq81svwrgq3wF0I5ezoClxkP2ZKaztee9lJ_NQZTJgbnd4LW78binuY9PwxjDW3dOB_ZDgZdlFHv-qPnbPy6vIQub2L_kVy_R6L5CYN0bgMn0hfp5ZEICP4mfWfkZ_FgoSUpaPc0g4coJ9VOsDZlJD2mcJgghax2hXqglthA7QuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPVS07Iu1zjRmI_smVgt5IcqTQeH13lS01DLx5DfgvudUkOuGaIZsA9ojx_O0g8sHPS4KmQ3EknUFdBBneTDtie8YuJ1qkqbMgW7holmj2UZaJ5xfS00sjeJsoMqYfRAdJMdNMqmKQ06iht5Rnn1zHcwwSo7sHV8F6_xidhykDMh5D6okpvyWOacwatKlEUf01B5PArY8AIfRCGIhM7TEH6P2l1eE6Ss0D67glbqwadAe9dVFeJh9Rsuko_amhaVzdZKyFFeik0mswcnkvjNq3oUPYhKG1LA9XrNUe8XkkjdsUoKWTIL9rqmW8c9vsx6BsBIe0EldL_-5QC_bn-bNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJkMpahRJFZi_eY3KMe0SfyArqV9UVMh6TVJFMpZXFzxJDLxj2FYXL6Fw3q6eRgXih6fpVh--9R7pnB0oykepRsRGbOQhz3-s2EIsQ0h-Wj56R4_GhWYokyV5s_gY4B69-s00InKgUaSa2AKKbINWGxQNatGotrKtSfCUzeeUWQB7JZLrIUwtaEfbIFeVYVe2e49VonwET8oAb0KtBWOpB9_DpUCSKgVce7HPLZszm_OqMSAbH179OooBD9cZwlfBNba5i-yckTZ1ouc1ujFO1Vggw7hWEFcEfgHbr0pBxFAmTJFZ780y840ZnhC86JJ9ewQXQB1YZWeIXGyfq0aHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivKD7g4RRJ7pzszxkvrhMOVVyUf5lxa-SK1ELwRZtjMwxwm74VDUJ8WYvfEmddWnmWe7ONbLGfW1WBaeToGNntA0nPDkJubwZl4oKAvT02dFsFpSK87cBST2Alc_5fL_X5HbJVsnlbdS8lu8PBIx6yaOsQOwJ13GG1NaMURaN9Aq7J6A8456f-vTgBAw-gfTVcxzXM1_TAx_VRWPMlElZmDGf_cuNekvuCyebNmZT38bbuGaf4rdYo3nlUoD-Nv4WkdcYQ2lMlDjvRRm2Jpj9uJyMBW-D77x8WVhk-O98Ity9CDgQUiWiMVhiFjBs6bYa1nrB3JEsxsSKkwUmvnMTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouhReMpkb1MKi2nzFdGHJ_3FNFKC7tLdyTOvFDC7RBsYAWtvL7H6hycT25ZXX3FAFJuDDwXM4Qz47xPPQ_sHPD7PjYsJpgI8v2jk7WHqQXr-zoga_npAZUkVUSoSJHJ1waBVmJBVhoP0T9N0I4pQ7mtAFX2iR-9i8juMXci_FL1s_VFfqNC4adFq_AvFZ0pqeStpbja2BG1QEVN3ixIlnGHYociEwP2JjHySTcjPVpMjgP22bdkLSSTVfF1TcFRzB_uGdXG4CVrKtLu58926LkMB7Z5xIVD4T3ZQJ-5cBxNkOrFSa_vD2l5mcpCbXw5uNl5WriAeey7i-ySljPBb6Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=HQxCXxLYtLtTwxvKjAKpFVPptayRaaSCFmwvkqBJK2VGGfGtjQOFZWH2QggJUhZI0Q3s3IUz0xxAnQL7Ctd9Cf9SUSz3OIPreSZOFz0qzhXTPZb8hxT79tc0AnWULopT3IDbEv3vxQE84q8pn01FXNccVGkXxGSE4p78s7ASFBEbQ_DOHBc-jz8jmREu-_VOF1Gl-dZcdv1-KojCGawd4Ty2bhn9l5WjfY39OovAmX2GJ9KeBnSocs7O3X_nTFleWwnaNKQ6sNEJs3xE68SBuRwb1wcslmNelB5R9cz65zPuBkNfmaJiXp6SPxbCV07bu31LGcLmKcrFYhnxBwwLbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=HQxCXxLYtLtTwxvKjAKpFVPptayRaaSCFmwvkqBJK2VGGfGtjQOFZWH2QggJUhZI0Q3s3IUz0xxAnQL7Ctd9Cf9SUSz3OIPreSZOFz0qzhXTPZb8hxT79tc0AnWULopT3IDbEv3vxQE84q8pn01FXNccVGkXxGSE4p78s7ASFBEbQ_DOHBc-jz8jmREu-_VOF1Gl-dZcdv1-KojCGawd4Ty2bhn9l5WjfY39OovAmX2GJ9KeBnSocs7O3X_nTFleWwnaNKQ6sNEJs3xE68SBuRwb1wcslmNelB5R9cz65zPuBkNfmaJiXp6SPxbCV07bu31LGcLmKcrFYhnxBwwLbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9p3revsxKmViO1x1wG53JJ6JXtCsCHJA-C2kAqwah5HUcXA2kIyJJdrbyGG8RVJ3Kw8Ti-Y4juL1UyLMMHl0OgUA9A-6whGZwqwTSGJCzwiZvWuWvbb-IBWUVHxLSAoqKH4ImFDzzcZ1RL51TStq-1IjRSOu_JiVdFhW_QlPfbT4b5mxzDMxtee5b2wcVhCmA8jJv43oSXrAop8jxP9G8RkH0x3NE6L8NMuxH3SjhHhgFcdmoXi3-arBkpkD8x5TrWvxuXzTsvSU2Y-npUIVb3ZT0a_Wk7srrnBaQrzrfU7l-CgwQWV9u_3F3wDccsUjTtTraABXDRdOTNMY_eflg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6G3tciAlOaQUWtCShUCnsUqVN-Lv8s9gi18kT7tfBlOHYZp3b3PWCsdV-sgsa3-Z5JgnvVrRJ_kBVDgOStD0vji7VHXMRQm6Y_Wp97ZHMazkQxFyn0jLRqlDFwQ0MOjUPA9ev8RVMFoj54FoVMRMXzIm2iOO8JzXHjZhrVTTF2dWNC9_ftLC5ceLrrjtNhYYQUCX-PP_zhlpl-2KBaZHu-DhSxIi2Vw2DBoOyFFH_aezTSwejK8dii8iD7cDA6_grkWZHxNAgt_IRjVHnfsswD59lTyI6SPDfiq-gdiTw0S09hCbGKQj9FEZx6DH36C2pZCRG99dElvn4v1BOouGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqvAYqPL34UliMRhig4nvwXFyfbkybwJlDorZ15s6yOfsTwM4-oaVieOkJEu997g_1YC4xHUrnQdDiH6O7OJvVmj-IqYqDQkn1fGye1r_-pIZS_XmTBplqCnFBKYLBy5y0RVgJ6BKMvQ3sfJs7uREx29zPuW37y64GIwTSei9S6u6YEMaGA1w8Q0wHOZYgH4SNyt-_P-gDw1izUWslQJ7FNx-oAQO_RHn0iKA35ffd5QUKkpWtceyB0_iSObcLz775Wmmm1BSDhOaMVH6h8rkSPQezIQ9l1CIW6Y5kbFaCeR_6wQHFuG6R31W6nS9fj7I3MDRYkOaaN00QSSTFPrAA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=Y0xiuih66cXi1puJfrIdLB6vDSY2GGQelzVs7dGaTDTjLGUZmJgXOFKDzJX5INkHrPYvb2mN_y1u3u66Y1w_eBPPi9OvfpJzkJlQ6sNeZ-Ls-aUL7iWyQFtJcozL9QD5WvfUmf5xQ1EYrMD0marJ0negJkZjIo6TsYgMQgRQagNdwSKNC_Gmuj_MQ4TgPsBZksNViF-x6R9faI7exyAG5na5-101JlfaLO8MuexZRt7ahpwA07N14lkq3lmtBHT_BNNDPmkaMOGCQyMzhWw7UI9NZzvPNS8lAzne-Ks20o0YwZx1M24ONHBToWQAcGrdmOPmzXzKU_61i3bIR9wUlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=Y0xiuih66cXi1puJfrIdLB6vDSY2GGQelzVs7dGaTDTjLGUZmJgXOFKDzJX5INkHrPYvb2mN_y1u3u66Y1w_eBPPi9OvfpJzkJlQ6sNeZ-Ls-aUL7iWyQFtJcozL9QD5WvfUmf5xQ1EYrMD0marJ0negJkZjIo6TsYgMQgRQagNdwSKNC_Gmuj_MQ4TgPsBZksNViF-x6R9faI7exyAG5na5-101JlfaLO8MuexZRt7ahpwA07N14lkq3lmtBHT_BNNDPmkaMOGCQyMzhWw7UI9NZzvPNS8lAzne-Ks20o0YwZx1M24ONHBToWQAcGrdmOPmzXzKU_61i3bIR9wUlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnPdFr4R3srIBR_uWPY7N7lMhGnJOzmyZOQkuwvp7wFmk8Zzbgk1IOqkudKpczNTplcAVALHfY1yE4Bm7suUMyVlCWvhmr26mCzWfx9cAM7--ocPjQyFXwGN843vwz0_my0uoNVaOzn4mxu0awcvsDYpnzqt9t-CkwE8fhHeyRSFr3st8XiP-_9vW7MsZjHNhw40DAndJSNtP0wMLcRWvWERQZKiIXG4tAaNdP7G89Q5AEv7DNyYsKhjzeyETS2KzIA8Kl20KnDraqfQC62_N3BrGO9JdziiT0WqlREqrPD0oL5xiwn1Rt1thRra1M_Sw7Fr8KWZX8dBLMUWyExWAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YmKGiNDltb9D1gMy5PLOODQdfNL03ZzsHAOgyCIiuV7olbSy5yH2fDri7vrjoNo4ISA5DCIuJzobO8NPFqkFx7BbJbecmXdxP2s7Sc85LcDtw3d1Msmk1beEzVsgtOAFGpSWFcGUf3uEn-EHDWez93oWyIO7tPL4vXxrA151_vN5a2NKbL4FxxlAGfbpj7UDM6bhn7ujpLnFBFp0_c_n3E3qEJLUUjKLxu4Hw9M93ffGTqZl9cJosUelXDhjLLumDfWGnh_5sg88XxnyLc8accwwwQziunOi1HPEpDZOS2ddsB8n9O0rPyVbOJSLAWiQIV_oCYRGSRZpsPBylssp4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKRtCADSMuWZe809IM_bNilMb2D2VUQiKWH81x7yvShk-ihHoymx6yraQIoUVIV4QTg0mJb5RfA0_pcQEOPZBjdcnFKOYx3yfbsNaaNTLfKkLL_cnjHHGgKT9R3NB2m4Px5Il1oqzXqU_3nb1i85xbqn7FKOXm735DJ46yvLAuqGRUl-Vus5kOuApJA3YMwpMnLZZUBKuUnSvCXVaTkNrmBgLB2gskz9p0eg--rk4krUPb9hxwr5O77qwi57TMuz9OU1Wtifz28T_5-Vvmh0WTssoI9CtpG92GttjeACEi1ZTkA_HhtJdqFWDh-2xmDeZsYOP_oCB2eIUljG8um1Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njOGqmNXCTEI4jK7GUnQbaJBjQPjN8LUdiTc2XS5-dGxcYoZbts2ZaN08CBgoh0Z350Im2CyxqnfJGNjiF3QNoCEH2bRAELKW6dD1XaLoh59558qqrBvVMJ32YyDpv37cWPODjq_tHX24oGcYtm2ERzuCedDF3scGocdGOroF2st48x8sX5wlSAypl2krtc53MY2uo61hoRPHGRlZY5EWxwOhYsvWGjnrK6joB-Vyi9H-7_81zWn8refT9gff1sCk7KlZOSicv5fTIxqMrW75rZRgxZaK1Io9J3CeD4WMnWXsnLF6YL83R9LC6VcZ3THmv63pTlGcA9Z1vELIwt0Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueFc0Nl4GfLOsKzG6yexLiims9lltfvMXFWMAWy8GL1qEwMrFHw2BNpTmO9a-MwHqAi8xhBV_Ba10lxXJZbvOBkQmqFf6PLjrR7I0zLlrCi8VqPB1-2mekSDH6Yn2mY7UzJ7IDyPoxxcvjmAPOWZLDBvE0Lm4Cd0kvgk7VISLezZPMJRrjFqZRwYMgigXPFpivSWfubJqXvF_L8y6tya9wtTKHBdTnUcXxotu7riV0xGRGUfr2IX3CX5XA3BTEw2vASqnkOsACJRv3za_k2UXryMwRcaGWY37ExkxZbzQmGkzu5KPvyP3cuaTN025IP1IatoouLl0B27mhFZB8BmUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEngaVa1Y8v2kqJdy3EqxSpHwl_T46xQNuLEkbIYq3BQraCBGXJTDDll5b_88en7HpLj-sVqQLc4UQfUyzB4kqg7ZC2POLpMr2Cit84cE5xaIpucQCBTGl5uit4rAT-qw5eZaR1KmwDU2N7mo5CoyUya-Te9qGcOvN1cFlwHpnL_iSZJ5aqTpqpybwoUu1X7mxd5wwMsR7oa3TJ2-kx81Ntqzm3-YOd8LwaIy_jBXyJgqs60N15C9Eckf0k97k2hJaIeAFejiYea1vftGY7aZ6-RQuyMEt9nyIqysOQhR5u9Tv5m9v2EdzQcWVTsBPIKfLZ8iuMYgTsBLO3pxQYv9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pezah69zMgAV1RjNnPbArf_n-2hpLQyM704hVW3rjSIRyFLVmTHDcf8bURE1ernIpw8MrZKXvJWF7Qr4K2FZI4PajI9u1A3V293iFVV2bWbIngF5EUJLkWqLQYrH5gyv8xkaWsyXiqxlhNkWsamSd1zPRMN_BQK0UIX7dgcOLd8qBnGq4G0yM5I6gQsWS4-G1KCuPu6QA0PR5skx0ghcmo4LTAX53xoJo7c8IfrG3qvIw8NGv54TXR8KV0rf-RxvdP7iz2kK8xA4VcJbecxwA6vhDV2WGx-QWBDDDXkMw2zTE17TlXXKA_UEcLhf5XL7KMW70u5HS9CYh3DxmWBM4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sB2EwiVd6kWstpMk0w7flsp-BhSTdWycGH-qGnvsly4aKsFPq7F-NXSw6cxtulCWyPEv_3PSIHDw8lluk2fz9LWlt0wBrROqAZERNTIxA-l2OHl7IAEy6CjvT9TjxWrTmmG3NXR5tUws5XkroIar5-LJAHO-WL7B2pTXfyHxnviVHjA_i2AXa6I93JIe7tl-aBzZZ1eUSwAqjclqqQYraN9gqERh_0nxxhm4sVSV5ZNBM-jQjAuxT3-1q3y_foscM_nqGPSIIVcipk-OiiyTl2e4o9i3UZeV7oQIpZHQ9CjzdKR-9vOTwMvyPCTxM6VGubi13od_brpKptcQcMElqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yvy_MqZ5Eg_yODs1Ajl1TAuygNWj2GBVYTqRtdYRPImw1auZrbpMfvAl2Be0qFCveKQyruNfBG5BtF_UpnD7MyCe2gLe2_-cJ_IldBPB8v9ZtzKINaDV7aOwtUqaz2zV3aCNDOEEV84gZ750OitFWnG35Mq0nONu_xLs8TKq7C1fKbOvL3tWVCkS2RaIpZ6FgoE-D6y7ORoW9X7bjFmRzY3J5cqugPChCvg8evcYLPja17sDWxuH0IbptcSnRjrnRfVmydRGlIEeGRaI9aST200AcX6uP9A5LRdoyND5eREVr87g1IB08x88GA9PfHKPMWY0mSZzrtVi4y02kHbq2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmiUC-BNgtquTxYwOacFFvWsNuxE3vyBA3YBYrOIWwZJ96S_Lm4xjZowIBPpHERDa09PJXMJBDdIVOL6QpU6TXWhtUmu4AG-AdJXlPEdCHSy0K9YhZ6QFukow9WubFaZTFlXpovD0RSQgernfjvxyMOUXQiVQ3fBci7CUDqHqp9m5JvsmNu8WIDvwa1Vr8WHf3XCD63cYMrhoQuE1fUL_0_57Ig145UriEn391e4COuPvyafVpVGkaYYuctm4Yvorx54fn-ncLk8Ju8wNjWvf3O329MCd4tW_FusRettSQc85CBlVN3jKIpdQqVC73ifHsHBsKjFFIq0bo_HiAFN7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCSJC1EbvTWTZiR-GJJhv58JwRnpdAQJIY92v6NNkAEJKb2ApKbJX9zKdfOrZgUYtqQC3MtAzPJJ0dqP4-RjP9FiLr8QZwkWTUslmQZNwzvPE0WF8IQUHdcsG6fnjqE-13EMRgUAkrJVPjrsYYXFOHZyFFfWQDg22r09FH0Ma_Vz3FMKpWf49_kB1PQt73NfIuTI1ZX8Qe1Q20ZuitzZmhMUkIqFYEA6syQUYDl6rj3XeXhXyzj9xVbOP7TXZ5opKoM9Zkfky_qpoWCmRv6_bLD_0JguoIVjfkOYwQMd_MQeQvzoWhvXwFRiJTYAltNc0CmjaKxHjskdhpavpoZQeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6GxUEillsPcf6vj3ZQawSsOizmRb4EBLELURSinF3sxAw_U7dI3r7h6Lb1NcNqcwBWBv4RcHa2HhASPxow0K_39T9wQRychWjRgQaT06Ezzg9o8BkVlQcXTfJR6y8qaymWN7aKi3r0_My1sXpGATiFmAkr1tD9XFSqRDoUKwTjzKaZuGNvqGbkeg0iBFmu9KUzPhrsWVy-qYaLhQdJcmVJquB856CsNmt3OIBO-7JWGv8JogqKmpF-0IxcUqPlx2Xa3DbiSBSel6W9IETIzOYlZQdMa0U9mXXMmz7Bp9aWgPDU6RAWZACtpoj6Ncx_jPc9ZktwkL32f7c2TOjLrgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUC-dWe_xAqqQnhEJ4MXyqsP5xPqqgzr8jOC_2mV5_aKTf7MiKcodNz9b13Jm8qMh3iIQzuorBmNGebUAOBfdaMGSHebprsjg_ZeUCEzkMijDxhXCxXM1IzhjzPDECRwUdRQ6QgLWsyRwhy348WLgK4hd5xYEey0xxUgyfpfGjgGABPQRnBuEufb3bbWYrM8CXYURKllWDy7Vjb8wtBb2Nptfd6NrUX9m7JwSpxlWicWQP7eRp85__8Ki5ZjoxWrQ5SbkrLA5UFr-BaO1hZEahu_jFN9_HcpdjpkDku3Bq5o3l0I0DY_0INQ67hJ4vuWr37m4xKbKTUGsxecWy89hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qq4YHnqmDCnB5dFpxSxxnD9Cu2n6EQLVGpZYDG3gBZ-BNt8CsRl8IfVPzexjbTaXa8I2DDaELyoC6nWsJ_nLEl6rKwvXH2XJdSqyV2L6s49Q2hHPp9Kyy0UzJycNDEmJr11UrXgXvJaSSq-PWtMKAkpKoxCz0eTBMrFuvcc9QUNk5PFpueaWZjzdz4R8cu6xAdC9VMtd0R-VbEVZAOuAgdfuxIa8zbVh8ZWGj3FTsLxIPv119ESZhXC80-3WPHpzUjqT1hWIH3rZSh5hlQcSBMvj4HbOedgfotWklonWpMgo8eeD1Vj2AOM8yxOzXk_GQ4fcoU4XEjfyIjLPUhhsug.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=a_ipgzHqyiVWvVQzfSSpufohUgplZtIlzAzyYWlQRZwP-MilwdU4uzC5UA7410KKNyDPz2cX3Haen8N0VV8FJyjzjKRhqreUcw-TknrXMtxVwWSelEJSs31NDw9Q9n6p53AOu5Tnn1CJC0dj0tSogwuMs6wo_TQaYruyIVyafSDYzVcFDSkJOPAuH3RsGhGI29yItpAi7FUF7-QdrU95sIV63W19m4iV79g4jzDmvYo8CmYHZXLKpoJGs5qgDwy1IHDG8mV50oLsA5UiZ6XrmErmDRADvSUC28dVuxqE40K3MVz7QBOuujXRmEK0ssSs9Ltqat3tzliVU0KMBDixQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=a_ipgzHqyiVWvVQzfSSpufohUgplZtIlzAzyYWlQRZwP-MilwdU4uzC5UA7410KKNyDPz2cX3Haen8N0VV8FJyjzjKRhqreUcw-TknrXMtxVwWSelEJSs31NDw9Q9n6p53AOu5Tnn1CJC0dj0tSogwuMs6wo_TQaYruyIVyafSDYzVcFDSkJOPAuH3RsGhGI29yItpAi7FUF7-QdrU95sIV63W19m4iV79g4jzDmvYo8CmYHZXLKpoJGs5qgDwy1IHDG8mV50oLsA5UiZ6XrmErmDRADvSUC28dVuxqE40K3MVz7QBOuujXRmEK0ssSs9Ltqat3tzliVU0KMBDixQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMrgRqXvabWSZ1VzPV1majk_9l-NqutJ7J7n2TRl4UU4pSZnW3tRC68fllzTvEM3UQLAaV0QM7z3A-FbsMJlH9VO6DKf2di7cbmPiSaY1tbBVBObGo2kSx9dmnrD1VGMda5fkCcJ8NNVCXZh3uViHzVKgodnIXkywA9kx0_8hnJzK48GmsM1Xdyg0mFN6swEZ9i1vFHkNcYM4gFX1hmoIcQCigp0wDKYI4IodyAIJonjZgGu3KRTYKyr7UB89nww1Ggokj0GFeyoNsMUHsZgn5N55eftIFs4T4Q7WVaY7NY4BnDi923T_6l0Vo7VPgiC_SGiqPJBzk4l5sfFU9NGxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWCAeif4ptY3GWrvAHN84r9d_4FhCAa8xHdLiXWOri80IyE1Cz5HCgj0Ki_NDEXOyohVKQNLWF4AxAcgzdYvWjVm0OJX39U_bPImV1aU0ncSno2O2zr91iwK34RpYTGbtnc7GDDCYw40_CKs4-iCTZfx23VnN3CyQ-3x_T3fFS_XvnvtK5JaIbDn8iu36jux-LWzQ4QsBwp2FBlHNh9aKpHgalVsHJYwugt8qMQA3EYDviD57LkTsCmZm_H3BF0YN7oV9kgUWHym4Oh4Nmi3pq3PU1AcO0mjRNBSXN1nEO3AzG-seEJDq4D3NAMonjdnK03fQBeNLvdH1d4VXLKuHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqGzMIAhYeRgQ7Xrg-pgDabT3cJVJAMbwXyMjFugX45qLlZkb6b4aEjL_B0SwYR4piTxRAOxAct87Nj8Li456pEqMucpJU1aEsxzDX_9yi5c9h-OKJYxFElT3hjpMrIDXboq3pMtEj5o4Ppy3HFEGxGktc598gvyeo6NA-LV51FYjRyETihXVc3hReW0B64p8V1pKYAm4sHnBbL__yMqMM2OR92xm_fnw7NO6qxm0wAWGzTEG0sW7LKGHjdTvUr8CnHovejb0WZHRoGL8j2swAqaQLLep99a9O3xKc261hBP9G_EXeIt4e4jSw_WckDOqArzGuh2QcN001kMKjfpVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfebPl_oz9z0RcZCU2Owg7lnZ20M2U1Y7geyshoX3_myRAZCceJ9mxkwrqveO-lp5qHkKpi6kQhLY0CEfXMPPFOOy1Sx9P3GHociHFCzxurkCAxPlu1DHH62RM_a0_7uXrtst2iBmuC0-0d9gXGzN6_gKls062O3SYp_VNbj4rLwEYjm7v6wZlRkelZEdwylb1aPcjnpZmS9qWcUzgxXg1BJrYQBQgj4sD6XUHCNF-ID_y6O3J1Eh2M3Ay37wb-IgDzCa-D-1P9gw8l6SjQrc9GXbKhMwW5Ls0AtVe9AKejkIHaTmvgbufiKKFIQvHAYJ8pGGRA42vym3vvAyvek6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCg8D0dhWx9TrXYjf1T7jwFP8v-HCGMVPppXHFaEqBHtj-YvN4Pg0W9Pkw8sCv3_QF1MFKc0M3j1TIFR_9PyAw36DhfeX86VIQVBdgmy3VSdAeyH4NH59s92cizqbwpvt7bsAQWnIJCZOxt88jjwHXTwSVNz7wOUPwCaFwSFe4wz-52j0WvlP44i1hVNI_kiw8rF9Zas0PAM35HklX9cMGS1vyTzkBMWf73uYsau56wD9h5_9t7t5I_AfEa3dryxlWOfFMXhgFmLgyGyZnRsNi5MZyR8a5eKQZyE2HVxt0Jst4O0ESFCxuW8CvI7CgmHyfre_n_s1JxiGSoDofku7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2GtEIcKXsKfVBBMEIAmh7kob--PReGFdZP_cC5pUnjavOj58b8QOvOBykL8pezx66jLslDGUJXH3i7NG6NBiFKemOK9khxcASBl0iPeka2gKsY47KYkS7gCuJ6-_gXymJjbBCPHR7O66joWJTua5DhIij9sIBSn9smhq-YY3IXZ2BBYgvze10r-DDLWW_8PQbM0ahxVyyXCtxfRp0ns6uRGJiE0fiLj4aTJN7JNCLxMkP57zGZO7Q7L7t_A2TgpdPokE9XEB2HSicVS_fSCYFBxGmscx-AY0RLLMtLaWph7NJPGvTnEtnHTJShGeY_nxYMrvFBZDlYTRbiqd1hrcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgwgWSuYVZD2mXg70wUuE7kkxDnT0p3Ly76INjMk2gFMO0QG8EtMNSSuQKaBd6IsCy8Z05g-IbUfXxqCopzzeQKKgalSLBMbmvwp77XdKSAZHbsfOqTDrqRK-bDWUFJ3yOj6Ns25lgyEn6Ox6BO1k_bZzHNgsc6HCup7PLSgupby4hjb8C9Sj4rhjKwAkZfgA2ZZsBtz_qRxSmEqS6YUwNqBHIKleSWqj7OZV5-kVOA7H-NWuR0y5PmsmpvKXZhLa-oOt__nC5rx9HseWoXtTaFYNsx5qeLzXaskeKhHa6KBSl6pDGWs1tulRwDdR2XDGTzTMn1tzB7po9UdVPn4FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eB5T77WUal9wEcFUaeK1ox84_ufx3rxDOTMOIpAblaFKfccbaLPGmrn23_gIS2mVlAxkhGOZGg-LYAM1dijsu7GbyR9AOBShoy-YsfQeh9tJG0nm9tjTQaaJmk78PQ_lY6jcc2_aCoqWmTjfTp6c2JcmNpDR44S2gUAp1nrTw15zNCXhLsLxWjrFdZMQ6rt36ds4NS9FywhLHCKigDOLEJfY2C_z6dndY1MbF5mVvJAV8H7-vAWGuaREWYQaMGIrlyCmpYs3OD-dpmyhjEMM2gfRlvbKSKD9wqjQnd_TIz4zyx9XAuj70Pl9n2Fjghk2A5ZY9Axd6O5AmprOy2hNsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8_c1tkmiK1KtmZ_O-z7VL5gVFUNy6q2UAkBVzrxZX68n74c2oQWGJhShYSk6rrD8IqXaEt-DXQP9yhaFJxvCNbmtt8sn-E_kKmhbvynZK9z3Mt7J1R9Z3XEZR5J8snBee4hz9FjV2ZRua8NBfacq04YDhLHtFdCKB1QB0KeNBfw5I8Yl4u_HTy0p_aIM4X182r8ikMUdc68RPq949RDHKUeP-F_mvijRfwD3SwoLFCbWuYUvQrYThdrve618GDpZnpRwcya-HU9UM1_piKE5SAgZX0UQ0WrJwO5kwfXIU1ZDnKY6sfkxf0ybWlAFH46fYyXTnVXN5yG534N53ChPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsupK-1QuRZ0-mug4Sp_JQSTl_nz_aQqF5kGqOpwddunu0NMTsWY94tFZ-7hK9tu3P9qyeQVEOpFEY54dGsdLMZY7iYrMhM-01JbqTv2Cx2Tc5N2_gthAaqjyZ2cHoRDdNUYwRVli2NdXY045IlB-Sk_kG9by1dQiSFuCA8lZ9MNPIMFg1tlslQWE0RWy6T3D3lNpHmggGM-SOt2veFMGVqQwe0GAhx-Au8hLe3_ro1QJfms93Nczucr9JjIel7NQjvnRcRBwgSJBeffgjTh6toq83O7Rf0jeWvHbN5yd5NxXGkxbJPWqM549y2gzWcgBv8Ddi-sYXrKUaeElOHyPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQszFjDtK6aNgOI324B6rsCqCcQadM0BkmVM_tle2PNp8VJ3KwKnu8oTPZXVO_w6DWjUjTDDN6H_vyhe-TLDzRmszuW6WrXSoCt-E2qPXLwMoa6ZbDxWejX-2bK3Tozq-V2U3O_BLEb86sidp2c1GS9_4ttHTi0cx1zhaVBTTeotqQKQF-aw2iRAi9x6UtOrxoa-xBuYdO2NAS3tB1tzX8BmFruUgXvf7eKr6XEyiP2W4c9n0fV_Ixzb8c7S15Ol7iG1Qh524-NuUQjiBoFjA2TsbPYFjXAyM9HCDL-0K2cj3tCzWN5oJ3jYJuS2fbUm9XiRIqLTAJiv8SEFeVauyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbNpjc11qUxc6c1CtyGNlMbQfc8s2DznhhncSgsklodb_WthKLNSzU3-w7DS4SWcq9Ln6oqqdB3ci8hzTo4XG7MvxKUU-Xmxx3Y_U6tWtDEBDxCSS2DwbBYg0EcPtMpubxtMdnnICGII7pFg6e_g1eD8YY2_uVjLre2eTAPpDlS8oE1eqE_cXCq9mv9Y1bt-_rNjIDdpHrXcg6A2wYH8oay2rDYzK17BvRsPrDdxXSCh84Lfi_GnhjEM3V2jrL2gsTYKbzzVBBUSThVqNLBF3OsaYmilfn-fj-pj9MLB8hllsqmYyf2IYbAjZMvyCGxpDxiNE-53sCvgVIcEWv5kGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zkl95js3biN_pyxYH4MT28oDn1LBwsvLy3GgmHSQZkku1nOXm_AJ9MNoR-UEwxkC8DRwJBHvwmZhqiS0AJDZ_Pvb94rDk83jLBGzZ-8EYoi0z3JNoj9rFTxVpz1cvlJh4zdkbghogXm9A-LMIZ5xuLktdjwqrhR6x3M6lnky1I5YkkIuG19QWzlRuNB0rQmfnm4ZPJr7lmOvEXiFSGdUQ6DFmIhN_01XoSUQ6xMVA7DGnHBKwf5BjFi7CTsvEQ0LJpXS-ffE53QcV2nBtq1PdEo27y8bffWENNnc0Hkt4gPSYbyy-m3pCLW4AAcNsO_K5CK8eOzbPsF5jLDgeDaLwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuKOQRjQApJwmgcT7_E1rNMJ2Ktn5arxDwMI3k67YLePLTLCv-x36HwPDZGUjNR-mPV-8ERkQH_tmyW2YgGh1SNB_bn66UktsN0IfHIkXOhHV6AGHjkHwtFduw4v03mWLprFVnRSlc6puHMhXMhk8JwyJ3Xz0LefnvvLaaPsLs1UKi5ol2zPzQLJunaMlHVeHFgIulGkMOeyBBGH8QUENYvgJ4NKk94BzO7dSS4ivjQ-EupoQOuUVqGtOgbdcl05nsJ-L4si1ix1ctdcqmUqRcYcpTF23Sg7AsBGj9IH_Sw9HZgGCbAc-uZou46wGCml12gJ0mti4t_EGmivjJmXWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7TWdxoeQvuUVXZn-FU0A5OtHdYUPwvVsNP9218um9-3qVPafmyPu7HdTyhhr2poFume2jSS4JFbvWbRsIDqIeerBNpw1mJu94qGT7M4mdpcub1GT8C6KRvfR6joouWIurNF4utRes0D9xLnAUen3gjBrT6BliRqMPzDAgmGGk3YOtxq5x5X2w8-aBhvPxP16qhM79_WE5x0kWdWltdRGSwg9weAbABOVGsLkhaTaGKeguOaXg0vcG9tSpB38yh9q1F1vzUCKNaJQyU0p5RN3jufhqsHd0dgSw_cvltH2ukKOPXcN1uQVx7YdWXEvQaJqNPK7hPtqg1ZQNWg0ZUOCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReBiByr9KpiRlRkPmawosTyzkzdHXJ0RQR9jVjCavW816cqBpxUNP4MFoBCziC2hn60nolda8PF_irXo_qY0taSQOh3QuGdpUXknbbfURZeT3Rg3FqzOe3P8a4dy2flblg-xX-bUEKQbJzXNltSGTKDQ1vbGHsEndE8apsgUHIg6ghBoH4J-9bYYEyWW_Th2QoCNeLL-WV2dfu1Liyt5gQYzsLqGRiyXOrHV6T2GYGp5L1zlZ44BfmZRR3fRsG2IUJe4dEfNhwZdqOkX-pGdhtCgXUnr75nvuweJgXEYcSrnUdJlBdPyWPtNkPbp03pJrAgtSMDBESjNcwE-AYRqOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgHKNKmVt2as9EYJahiHEpV03RwSLAvuVv2viFulIT9LyHvSqlLpq-hptFkPFhAUycuguPtxPBznPC86fvGZBjQq8N7J8yhWGt98SpSBxzx7P8J3d2k1u4jP8VjDIImbJbyBWKCXx1umocGd6ieRp1QySbRNFiRocQHgMpqC5kHxCGPy1K7KgQQmWCoqjGYP1mJzcrBEjvbgWsRRgtAl5yo64060TwT8WK0y6prt4Gx2Ko1ooyEQv7xK00lTvHSrZ_5Ipzlo9g0aRogqd0usKQ9lZ7S-nrLCUukzy1uWCLYVT3k_0Qot4whHDGSJIYbJ8IsuiPkoVHtGve0kks3MTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOPk3iBEYcfju_Ex6JK6-ATFjn_P_AETUzvnrMVEIqC-5jXbh50OOw4_wO5Fwg_5C7XskSZs5rOxuGAd1srye44J3DL0bZqxxIyfx7usHPY0gGezkKN3FFL0HqmMHif12R43Ca94sbHsxwed3QGpTccaYHyD_GzsdzHS5SvZkzVX3APL29S3ze9bpPTSMMnI5X_alsftM3VMUtaaExZVylZhuWk5Frabnky_plQJj7sw3eoEt01gTLLZE2_9SAqyoPDPbfQ-7VrNW_YDIWvbYF5V_thnIirg0UKJG0H4crsasUBWrwkmT3EhMnvUzTGohfb7sQRXZN9C2lH7SRUfQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WP5ZWSN-AfCK69vHe2rLJKrdCNyMmHH4ZGivY4noosL054RD64lOHOwH1TPgjjH7UsGrnJRVdwqIlJnRbq62DtnMyEzk4pSBxWksLtk17YCuJ1oOfej254vvcH28A2UlmuXn6AWlCj51VmH-zI5ZETs34Qq5BXSlIwmbXvpAYmj6toCJ99qMBFuHBySuGqW9xUvw8dx7B3jrm2ExYG2Fb0JBUiyL1P78z7AZwTX4iYOWVpia3BWwaHN9in7KVaqMPxBLr3Easbg0N7tV4QKc6yZJHoJ8H6TsUi-D-juOV20CF4BMHDBfUg3HnrQqImj7NcDHMJAVxX5CnsCSJEMTyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZrf3eLqGTMluNcp2VAnorkEWAhE83LFFa9XVtRg4X5fO42WBsv9n34nI0M54P8DiXgHsXr0EHpRf-qlA3eLf_2YZWM3Q_NVdwzeuwRVXGK2piNY9dS2-iu7fXYDc916g-On65-L5e1QoU0__jR-N6RTgVvgLpsPGGNqi3WXzBNkHAc0zqoHchV4VaFFriTMuUA9e8e6Ao71ewxYmzH_32rBzBW53gazQtFO5ua_h4d73rTW3B4B2CJeEtq59zOhhYwlpO1C85laMoqydKmb7YZruXLf1_KPU7Ijp1LYwWQ0rGOcPCRg8eNUgm0APpkRvyZxb5vIGMCpJHKJbMaI5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfAy6n3aqk5KyJCh08nSNzymYPAouuZP2cg6dBwpxVaMMN5ZQcscreC5x0005UyfQAaGLN4bg5bLZMVJvS470ToiVmNE1L6cidpQsLk1ruEoG1DnynlUxAh0hQv5B3IL1p9zRtfbhz6DDTWCK607evujBuCK2vpldFkvYY5VCpjj-GdiqByte6czKMuYhduwo1OPyV5udt-ESWtJbT1xHJftiuc_JUtSWAM4cjVUOx9VgbkKPfPmbYRFPxxEMiAJC9XCXUriP8apiGuAfVTGltt368zYfurIICAtr-LBq18YJARRl-Ow5qPsiaedoxDhuiCSwpeNw3MNUFNDJ-dI2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBX0BHLq3GCBwWPEOKicB5LGGS7K_d4eERcUKKGSngNx28mCbKyUsHT3qELCp0149iQqhaRZ2jBZD3kFfcjr_iyMwvzbdcbc4kdkrANYZIZH-R_uiy6YCcIWZ1jdrm1hitcp8XeNfLSJUX7itZ4_y71kgldZjw0mndUwGyEX21TIdZGFqRBbmId1pRXjOKnYuppuqoXq0fvD_yffp-aPrBPl7JufgijOogOp0EVHInXSyEnvL_pDuJvg5_vBfcfFO08YELQNF9LcZYExeEtrxxUHU0HiZ3kcFpFuLza2JCIFLHH22jFUcbFx8C_NTA7uAsP_8x1RS11mCeAzr0jCyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOI2aWg09mMsn509aBwl-_NKiR3z-Hp3hArrY_HcWvGdD5CUcsgEtQ2dVQT6LiHT4twTonAYvldbEgB1kISOhI3bL1EMhBlq1XnNG5EqdUVXyx995LLsIEoIv92McmvzCRlR01LVNzKpFdQmUPCqkpTogpv7joAg8qA98UwTXDGF6gPIi2pNgakAnzDg5k7w6RRGbplpVB_5c-nb4gINrTPi8WOFghusu7p3dT1B_wBXb2nTYC-5kd9Enw6xfqob7gQclj2_sVPZpLol_8LIo1EvEqZQ5ugMSTorOaMlzu7g4C4rwWYu0X7gmI5wdeGHOUH3XyTE37cMjGaeoc3fCA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=BfbRNC1vOyyDAIl33RqnMc9g7Yu48LUtkG56622V7NQP3d0j5Vdtbg4Nq533XjMIIwcuZZNV7Ea3Zp9ukq1sVZeS-pbBQ1rSyIzVq6ej8pVSkXQRHqw_urwcVrMBibGH0_VxMohLSoz_ogwatOUDjekUfhbG5w5Zt-I3nm3ERFnJMXgNk5-nQKKthIHyaLIxQUubGwTtjP4SQRfkff5pXI2G18UTzVIsbKnEh52cRqFkNT9l7K40h3BzQuXv2McyWvg5N333-2pICEnOjoiZCLxMOmknzMCSfgBaMobiGMkoLP57lUD3Oxnarkgic1Ho11K_LEh1a_wGw6XBAq3N0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=BfbRNC1vOyyDAIl33RqnMc9g7Yu48LUtkG56622V7NQP3d0j5Vdtbg4Nq533XjMIIwcuZZNV7Ea3Zp9ukq1sVZeS-pbBQ1rSyIzVq6ej8pVSkXQRHqw_urwcVrMBibGH0_VxMohLSoz_ogwatOUDjekUfhbG5w5Zt-I3nm3ERFnJMXgNk5-nQKKthIHyaLIxQUubGwTtjP4SQRfkff5pXI2G18UTzVIsbKnEh52cRqFkNT9l7K40h3BzQuXv2McyWvg5N333-2pICEnOjoiZCLxMOmknzMCSfgBaMobiGMkoLP57lUD3Oxnarkgic1Ho11K_LEh1a_wGw6XBAq3N0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KA68h-tXWsrsor88om7Ep9uPyzmTWnFuWbKfqH9bKdMF2Dw0DYYQsdRHy-woo4WCIAK_f3MamF_mUHgq0BfMC14JssVQD-qT8hjdGvkJhWy__6uduvsNdvPRefLlRym0aNUdoIqD8E5Q1dC1rUNpdgCozFR5Pb62LA5WOF8jmgmqQZd00v2f_NZjb5Mnumnq5_Bk0NF1l98JFZJH9VaGoyRSQFLL-BOuSDH42DZ19FhZSXkcsdQXvEFyJV0ml_Ogjeiu76Pb1fq_u--GplfxEbus4OGCm3gU_fjxi6yuPRuIk3ZVyPSKLTJ3muPSF02tKL5b4v4lT9PspSIdsvZELA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
