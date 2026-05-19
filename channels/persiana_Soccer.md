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
<p>@persiana_Soccer • 👥 204K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 23:55:43</div>
<hr>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
متفاوت نه اما همچنان‌چشم‌نواز؛ رونمایی از کیت فصل بعد اینترمیلان: لباسی در قامت فاتح اسکودتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/persiana_Soccer/22189" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jX8DSqAdPe_rgnFPZOptpPkFATzNyFcmTPCj9vh4dHUMQvId7qm6AhurLeT2G-d4dIq5WY6bmBGX6j8TpmMUVNv2wV6J6zBsraMh3AO2KC2dcMENAg8kdXBERJTWNCdkjsiVa0IQjjm-85tm5qCh1LiTh0DqpXLDLT7hBqaK2nZIY-cGhbccJs4iA9ZRgTb_b0zJ-QeccQxSXAGDypn3RAhrIwMdGaseJCvWBP9gZv5mo3AjGf_KiOYUWQYOZ9UOedIThh973zCmVkQu-BLAQfD7CZicA2crB7rYBug1T_84XZtGWDTN-3ZPR3NWjqeGlU23xT8LR40oPpKBEYjhjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/persiana_Soccer/22188" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgZisqJ2pnWt6MfB2I1egbUCfSdxNrjNwedphHiZNg4kHewOnbp44ZNR7n0WUCS6pXCL3Nit2cP0ZriGulpaB-BMWbv3hNNBNRXXR_YGVC4Ky8_HwhXXsROlWZvyLffFAZp3Uq4ipmg3r_7_A20OwhJp7DFsMb2D3OM515pgSIyK3bjm6HhFLG124e-HDLglJmX4XcWt407OAYmmFFmqcDrNJem7ThW7pge24MAVptRnwIXKwyHfZClK0SG1-0FqU8UU7pgp-i6bDOqqAnRQmWEwNphhZS9iF6CW5kJ2WXB81monjqpUeL95FJ9zZBjuFV_vAuNP_27WKrZ_0MpeRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا
؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/persiana_Soccer/22186" target="_blank">📅 16:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr6Zc717NnwcyPc9GbUKf7oATjOFZyxX_VYhwdm_hVCCF745v6Zp23BGXJY949_o6hqHdp5X1Mk2w9vf2mTdlsqc0EIz5xLCLhf-sPl2YvGk1T4Ya7fHmmn5DofBUlW3HSxtjzGETMZdxV0jZvDDDXgN_01jU9yHgSdreOeVf3o2UE1oExHJL1HguPk3xNE7XOJty5kRfqiU4eyB3We05MkqQiZ7Y1EvUVkaccIJ9ybnGj4ZWaJmxd8HreppsSRxu5NIHJg16D4ds_qRMCtIHXZqLWBFyQ_H30McB9SDm9bfiGA3_N_yuTDuR-c7k0oz60Yr-tDM1-S1qAp4mOAb7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGGTRfG-IIRXU4gy88H5Wbr-rWSSUHHcG9kP6Rl8pp1MNHyNIhX45rlJ5_Y0LXBAfbs-0h43C27qZRLavvmyso-apwtgKXoAVdEERZI6fs_tD9kwZW6-yFtFBWFN4mZkc3C7-_2_qzgRrQzSxCbRIEScwewlYsTHvNYRGLyCnNlwM4N0_qR5dqky0hfg4DvKx2CxT3gaoP7mWNIk4WPJrB8Pp5ShY5JkQyBx5NVjV8Dv0Y7SlupU7Uvv8eIvKnxwAKnsB11I2Vu5gYwE0SQZp6B3VJDlJsrTX9j4lMtBSyW8V_7sdWtFpZpFYNSam567iEsiBv_1M8l6pN9Pnfi8PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/persiana_Soccer/22184" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/persiana_Soccer/22183" target="_blank">📅 11:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKZB3K4UFASRPJU-5lhPEYt_hFDUrNPx-Kh6yeTV_VIurIQ64h3QXAoI3J7zeV4ZiXY9NuPF5mhQQjFwpDGrWVkt1qTl56DiaTSKGdhkwyjX0xaviN2QDwTSl5_WSY0LQnZ5HXJYEOJkeIF287dkwmRNoYsP9Y2o_eh8AcWCASljseBx0HeJH7Sy3d6hJ8NuWHyStLFwZdmGDdtGDeY2-G_hlM4DiYZEEj0hjDIl9A_CM2NKjSflrovZ6gNzYuwzlTctXsUgXd8J0Cop-dNBduWmowwmBj4RwyPoVtRFDerDOc0O29hSjPUg9lpQ77eoiRfEEdWbvHmrV7aWtCBl_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ پپ گواردیولا سرمربی سیتیزن‌ها در پایان فصل ازمنچسترسیتی جدا خواهدشد و انزو مارسکا دستیار سابق او در من سیتی جانشینش خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/persiana_Soccer/22182" target="_blank">📅 10:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvN73u2s4ctqoiKKh87APKEYe2GQcS-gSFFuo26yTMIccxYYEh5udQB0TKIfHoyQwLlX4VFnnMHfBLubOhZmC17vbd21m2NjrYCzjsd6X-igKISJr1-_yQFxI2IcLiaz-4vTTy5UqXKGzFMGO9EfccX_eh814J8jXyHDZYJbNZCqpR02XXEADBgp_rEBRdzT4E7ojJXrxBmJu3VYznxW1l7sAlhZ0iIDbYM1KUpV_ZqdsZIhizGs9NbE9hD2bhGve0NVFYQMdmy11Lotcm_gOgYpmCy0SL8itoPy6y-4EXYm2U3FO7bYt6G33OyosZ0Y192GK5L1Z6n58pWzkh-RGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXAshsE8iInYtW-J_WPZzEx21DTtFBBmobWVGjTLRLMPfzM8W7L0V5sU3l79QmhsB4sBZWjBP7hbTnzfc7qrbGLEaFtJPMQbC_culHJsITx6vZ_ztJ7jskDMrtdBjYoDm0e8xMK7QtArUFqh5YOoIrVnZ6nHYdwdENRtHPS6fNMi1vH-vnbXXZ4WFk6Vjr31GAEkYNU4YfZsMMYOQvBTdVRKrr9WOQZBFuEpSU3wDSLSUd4ORlz1SP8zLYE8Fwvto7DLihAAfUyuoc7k3KhxcQyBGeTNnWvJxnSWlizKjaLUILTU8EVaaB5wV0Nno8GAnvJlMwI4fPIU-0pf5vsZHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22180" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXhMoeQrNLHKdqiuHkhW2yuFpiyUMaagmQUkX217eNHFurgoTlwz-FPTztORdFHVhgA_LCrn-SN-qO-oxkmrpqUUQib9wKTW4R0uBZr6mBlbhyHz3o2Y1bYPFvBslffvRkJsnElkqbWA93CdxOcX69vqXkaPV5wvT5e1OPUcbEEkOxfNKHTAc4XFgYJS8hOtaHm_hwykpUsrAHAMm7qoMT8bbADmSbdSrUPY6YFzFU-oN_E84lB6cD1nwejF9vfmRFKwJjEhUWeRi4QSp0G7jOtRipBva7DCZ4_q__v4vZ_2MArocYVBzMQgjD9lYMZrmwDL8hh5FXVPlDKFpyESlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه جذاب افتخارات پپ گواردیولا و ژوزه مورینیو همراه با هزینه های هنگفت این دو سرمربی محبوب در پنجره های نقل و انتقالاتی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/persiana_Soccer/22179" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/persiana_Soccer/22178" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22175">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P5HATnomEAI4jlW-sixKvX585aXSFSLYL8-dsj1DdbncDRyNFATpp6BJPGwviUDRzZq33S2GlXLnnxUjs1ZphOONs8ZYcT-lmI7WXrS3Je5-FNUwrUL1hQd6jDjv10_R_xVgZ9-RjmwZm5oGbkxniMitjS82vwoIY12pVn0ZvkDux86x9y9GaelVrGR7o-KB7j7wgVBIoUXKCWsKtCDh6chF-wRlJQ-19oWPh5aEDpCbpuqLhJKPnClnF-rcK24vsBjUePewKtaQPY3wUFa5hPJI6i3lBZqCsuBLRaSarYNYShGInIwo5npGWVwvpk7Nbu1sB4xlYC3A5jd5B2jr2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jrGPAeS8mqIweQD29brmOd-a8dy50NXHvXAZADPvLeBQL0Qhis4GO5fCVI3uls_X2I856s4zWS-z0plWvlp6L-8Z8AF0DQ2pQjem3-0mIQO9qPK0hOCuBCIcp1kk1yp7MFarnV55EIFXRMzji6pzcf5fAhyrxRw4ulwpJ_qrSmRNApuJ3L8MzaGgf-FKb30YQAHE94Oxle6O36pKjNY3_9iVGD5T-yNiHHvM5l1ZrHdDuu7z9L3H0ZZvpu3ZOhL5SH0xMJ_1cNOGSifNUMb4_fHpgTnZ-rmxesUxzupxp8rSbOodJs94BFNHJ1S9cOSN7r8BM1Rm9rN7XizBUyW2ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مهدی قایدی ستاره 27 ساله ایرانی سابق باشگاه استقلال در کنار پسرش میلان قایدی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APu0jznb1uE2XQ70wFhB9_tpK3wGv8402n7zZ3cZ16E1kiWnd0J5GRfXNXMukCi8edXeVnlpnBPY8npydPtfEpMwXZJkhUrg1VJSuCP8zRyo838hn-bx_pF8NOTAd2rYC5VO2E8VgkzLoLSFnzEiHL5Cu75hLYM9e2J7YhwkHIAeHaCWgtWmdGnwmhA8QUUQEuW6RYa8Xs_8CV4CGmvRTIxXBrV5t_8qXBs3aTkk0uaTryS-ebEkPFgV7WZBkS7pnUcDu5-2sW1b7a5qKdZENrsw4eLhHwE1dBwMGO6US3xLTFyw50is3lVjdLqqyiDw2QGhunewf43hwp7USF_tjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P94PeU1qGruHVQxHPaTXhsYluX7IdOQ23WrCM11DbzrS1lihReCEftKCrUQDnMuWbihpHiVNJeyPe_Q-bA5yCZnLxK8gd5hDQyIXoa57wkZ17ZMFRsHkzjG6jjxyesR1nogUNJsyWLJBOxcpv_1hWEtXKLQUv3jNhY017VLVSbuMa21ery2AcxHRvn4_AtZp_7k4NEQCZmleBoR9TwBwx3MbmfYbmQqV80fO_gYvLKncNun1g7YH70ZHOm7kyIm3m7tzvVql5hos9o2TGFJJJj1lS-58_a8NTotjSvyuYG3AXbaC8BczfMDk5EDiZU_W06LHBUKXCZkF6_Vs_lmx-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2MUKQxcPPmbBNOoWeYX7m45cfKClv3klSAe4xGnCawy5hV7fPXlUwkqFzRVqrQYKRanEwc722nZrtd2pOCjA1D20RofKn-3Migo49ianpouANt8CN9KDde9dnl3OiQ6486-7H-wiW-g1KLBvbycX7q1Ti6ZCzMZftso-ic2MbA4D0Ka5bpiwmBb3zvBOcOCpMXIN9-oRrSWk5YrJEbIaykYRdARd0EdJ-b7TQt_Ae2J51fBTHrXF58Fkv3EEKOZLq5fxDqNoBjx6GkEY3v7P1u3L6PyrzxIT5Xbmg4XUFQfiRD733UUsUfe8SoXGjK-tpBeTUpkEY7VJkjjKkfO7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Natb-_Ole7WksiKnrMvsRlRnOL35kvCuUYRb6mUvVFgu1a8zo1iKHmKVpiAuyoPZFD3wTIDTOz3ZzLk0kkNOyK7o-DJRmLjrk7kV9DVt7eBaY8KNB5holUTbKejNSiUbMhQw5q6rwoBN1-7UlcaeO9pyPLuEKegPDmVoH-i_hf7Ehwu9wfqiVRWRo6CPKUg9PZZQnyvPhJfbS9LwWNzq04dgBhhxrpSmL3kq96z6V9M7J1dgc9D9KuIqI29DOkSWTZCOCquE_euI5063KfG5Rb2o5VTbK0fP2MzjD5l9Q5vUyr1cavrwkHK42e8wP0yo2IfcxpK8Dv_hhWxUMhOH0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3vfeCOmkidRGknnx0NJGqFDfv4KMlGBYb4tTgn2XXop4DBk6vmGAHBaXDStS0SY_XheH5I9Tqc6PXR66LcFrQl5IwZK6AhhdEBMlO7Qzfylub2ocNaGqXwOUSjpDKpPOJQcEfPUdW1z-xKa1Wd7-W26E-vx8pTJjFNOqM91hZtRNK-BqfqTJTmsOkbHhd3uj4zfQ1FjSBtZ2BBl3M5E-fTWhrPQYXo1SQsWh3F-0lgOIbOtU0WyQRRPy2mF9l3HtXytvO9riVUs_2RCbxyOQojyCnt2QoXyZKHoB9nR_wuOCjINPhxbY_a_1oOdGjhG4ZacCBuC2KO5L9fMdthtlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbfncBxUtEXfS1aoaWc6baBv0zVrFHa_JhUEgb7vwlihFFm3cGvo2Xl0DSXgKu8iQVC1VjyXeO8yBc1ysVh4GNmA2l0CnE5-8Kmb6Dh0T-RzzcW3u6VmWE-V8g-BpbnAHFbWsHSymu0NlQiF1Vs0E1xTsiipsxemoOSHSrcXVMkMD71VAwpLW09Tl0SKcFtSVtPfYBlmk0VZQ1NHyR5nI57MHmR9hecLgQjP1q-_qlDuP3gBDGK5cyAO0C-XMvP2NtBmTA69rMLQ0w8HpyETgfGynBm2siWJ_dW4S97xkHknoulISH0BZzbVCveZG8848bFVRr6Gg6Hn8e623dCTOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F__RAJMEbAPObk7gaarXY1BwONr0aSv0MoSMHhNMXxd7mk7ci399o-51_R7Dg8l9VNbLMNCJPaW9Ycwm8WBw9e3KkWZ5ZgXcNMnTrYupRelN_tVw2hcICbTDsAz3prsotCtxHb2ouste0x3RENfBqQd-1yUdG16CQS0izD2AhWESMO9qQfOeu5jSIhlmC5DePImiSpUwDDR57FvzHctz6_cRC2hQ2KCkFCEIF83k_CWSRruh6l7Rh_Lb1kz4T8CThsodno0rAMm5t1mud_CXqZqUzi3oOcP3gb9NoUqSNfc9KWmv6LxGbBtYc5bazyNAe3rhM6bVkW-h4uOYxcPQ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_JmdGO_X-9o6-3Q1kFhnGKcjzc-URAwbk-mAGwowT3PKe7XL6UcR_2m6cLuGaGo6BkRpRWQdhVNkxqD79U7ApPowaKX7z-sfKg6qeRgeGp6o5WEQPFHUmmPWToEkdBcJVs4-kh4OgMePk0aOvulRm_3d6byvorvybwSjXDH-JhGTEEMnMC4lBnPgPBLGdHFJRghhOhzW4wUdcK3LozgGKEpsyPnW5iU4IAB910xryVCY6KAFJmVrFt_Gs_i3CRUsC6kJ4-thjkjx2pTE2SEo1ug-AXOEW8biN9BBysQNrWdpWwmBtnBNTO8Ncu__9R5sO3mfkSCJ46pXAurHVDFjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOn57PFeyEOzfJfAKQGvSYqKJOdaW7RVjcmF7YwUlipDGfCm146rDg78iONTrSoYlKOgBWxcEKTQin-xHrSWaod08G1vq6xXQhEVpikfq2LoV_9lvSofDy3iML1IGeRjhUC8t-BGYqrekLVPa_mJC_jAicJ7kTgOpl83P-pd5w1z9ZyCJJqh9WNotqP8x4kex-FsHvoGInc63KX0w3CTyFHT1HYdnS5BsjsrvP9YCpzX0HSo6GQoeqFlpu-e9JrTBExwBdVtNJ_KdpidhLW1J2tlY8ApN_cjme4vK3EwQkU9Q8OkqlK-AbmAMKZVWxBj6CoWDBsbx2bSAHRMUno6Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7ON1ZAzDro_DUTJO83yD7zdQTtbNlMrnPcthPmrU410zp6RKG4yBZP55imDc-NEOsUmfy9lhdjeduv22V3zeLjq4pIlK2w3JzmFipjLOG2SNGI3yUWxVcH-TPUjkkoAAlJ9gt5463bigdTMMWt7U0NlJMOELINPTHe7pc4eLIZ5RxDSTffzJF0-bQviiMRYarwU5vUmHunb-gS0y9GhFBgsxhk6822aGSD12RXaO9Xfx6U17t_IpKEtZOjCscRC1JfybV3_gk8uB1YkvF467vQZvkuQcjaC7jgWdwXqTILtL1n-m2QAq4nrJ1DNGcSMxTdCmW8r2_TrbhNo3MY6xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPEgUUsy0m8xqCrkrGSftDo1MyIvakxRbO1-FA21UDBj7Qje_843IBmNCrrbC2qzLpo4zer3xw7sFbbxGrrFoRj0hWzxJHv_WeGklZEzcs8Wgd0vTlUb80ArciWs3016I-Z6OdJmcx9TxopuTQpuWa3u8zglj1b8PG5c74sAVvwKjJEYY_dFNDLZ6SDNlFXFWc-r0YopRkp1z8rPGB84cYjP6D73OXGJxs_cseI7LbCtwsxc1YP-4zEYhno8Mu3iK8xE9h5Cftm5DlfEVGOcTUuWK4lpJqPfHvCGdIOstO05f1WBdQP9GcwHDX82HKPDtD1NeDuJ77Q_Zi-X4Rst_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBorDemzvQLNWm_Fln49Wc-p4MGH7xezoiZG9LOChQJlplp5dAietA9pthnYdI1mkKpHTaL01wSXdfMu5r7U9cG4OPzXtfSBEzg_oTFGCzTUrDASo_z_ZCkESI3KlGq3lrZ2VZnDYTm11DqYZ8nXRCOFkP6Ijv8BrsNxPm80QM6tyagu-X015W2GB4SagAZZH_lLQVihLB0eTasytAGt0TJIBbUOYvakZz9pDavuB_8dMB2s0nULSXxLc8kb60U2Sjcm-ZJdPJo_-WcryRP0tYY_pP-Q61e8EeGiKJpu4hvNwzwUH16crVKanPrpHsWrQYSvymNEeYikgWqmuVxvkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ne5c5zI_FBMxvndWUwegrWCTbhkFxzFssDRFc3aIrKGdMU-xtni5WOB3wufJBC9Dk-3w-Ujbc6ImIBMvbLFdg-BdEWCrdVOZbQcWg6w1ETHovnTnQViVQcnAztNIeB7M7VODdjob7uAGmlBx5qgfGF1fCFRcpGaDtjfahTOKKtPw7vb9_XR7-cc2cPXKKv8DS5cGOKakD4sW4w6gqrY-wuTbLw2GsORJ33DARPnL_gmKXDw6KpPo1ww2D5rLAsOdH4ToOqJnGZTE79h-RM0j5KWyv7qyoIbnnLclDUdfCL61E6UdQe2bWosxH36PKdxbjo4hK2ZWwPEI2K1dXLMBUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHU9QYgnJlrueNrAgHgN9zQu5UAocb_-v5al4xT-88nIQWOyr7k0aQQj3-cWIJkKa7Q-VHE39Ap9ZDCbCrfXxJ_bFQCYwiFR2hBp3V-Sfu01pTyd0Gc2I0Rp7Y9hdIL2eYGdjsyRk4nAsQ6u3ok0tfzattxwWVlkCT7wBxwBSUvbN2QdSF1J1fgAjdhNBnMuv_LWiz4Ouavq2XvKIdLAkiFuARuEwGgAzKTp4lo0SoRWTrO0WdaqFz-1iJ47afLrcELVpWV0SZNTTN7Cs-I2ZNjHe8Ee27eBkfopQZCwa_AktVJ7oG1Cw4OG7GcWUes7Db3UH6SnQ-3uO-XMzhSsng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sawxOpXkzviPixwaLqfAPRxLs08o-p2Yl4gsf8xux7xH-8WTdHzpS5GOsOSVq01KcX5qPHIlmCLCoVvzE7irZpZrsNoKax4jZ2G1ZAIMDcupoS6-SgY5YC3XxrqsCcL9DLS0Oe-EZ2T3ZlBgpiF_Ii0ArV7kif1Oayk9U28WdZz3R73DrcUuFPmgHVTbAGtBSMdLq6Y6NxEMJHr3A-gP5jCjT-KJ3QBjtS4MN9HulMuavli6Lycup4x2xIZY2JP_152EVr5h1HA16KCJJ-FO2aj567xumRdV8IwczSAPQlGgALBu7FW_vfQO1IlS9nrtz0ND1O5InnoOebaPaZ_ruQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4n8VqvDmG-YFz5Eh_VrTArQ-6_hNqo7AfPrrfV6zKmil1koYEsP0_IzXgNImFyPnXDZwyUqIlEu6EFeAwrXV_c7Ed0S5HCATCdYT7gRr-5EeHVT3K5oLJLV9xsiy1a6ymeWdGHFa89JD-78FSdHhACTl3UHPPp7NzQSJ-SEXMxQ4zXy5CeIvdxnXP5VICRCtncgLhPlkbOgeWXwnLuKHE571bJjFNHHEqSY5o_rkLM4gdQX0LvMM6Hz_m1ubtjj4FB7Rm1csyzpabl24uUB6JHH1-wQ54_IKC8Q9fwU-SeBYmCnmsxYUJIEFeI9H2T0QwnDqbLlcE5_UemZTKIfXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSZo4rjhLw76xXU8Ww5FvARz3HQyW6SDPrXdcNeQhne0bB4ABbDLxoxcjCaKY5kZEObeBqk085XuUyWlC1PUIKErPWOysh5XVGceOqalC1ws5PyL4U_b6qSWwYuvzgNTUdFMhqAdpXTR11_trcVs3tqua7kXvkyYkxYbpghfXuFS5dmFs8QOmiG_i1MNBdeNXg3e0hA9kLgD6T81Z1PZJmJUDZ5fClpuEPeFbJdO99T4HkmZZzIi5Pzp_hnrj9l3qS8vqAnUY_KmHX4iQTxi4mFsPQhY4d0_o-vDrG7qZ6kfxpaWi0Dp1avqtsf7PDj4dWzMUx7l4nKiv4-pbOmu0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7KndIsrMg4xMNc58Zga-NtP3_jh5tmuiVMUvBDQEW-rP0KPVZFq68pnMeM_0f7PWLZisYB1-7kkN4eOyxgu4tmAfPF4HnkBF53hNe7hIdybJz6IRVpq9AathLy0yHcfjyV2gYEDYh-dORt-W0pzx9OI-l_vsPydSOj2H9mtm7wWwXmRKMW0RvlnTeJbz2eJCS53CgDpJuW-qPcFnUiMQBT3wsG-6-X80XLSEWnsBxdugmm2cZqebEU7y1Cyq2DRF3AKRWitKtnftVpzdSa4m0d63fsbzkH27r85sxAOSfVYfOVCwsIGfMOwSEyu1JMxf4XnzJvbaOR3Y6K2PaRCnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X46y-6e8Z8beEhU4XhjHOZpojhdK5uwM5Q9AlsDnFq6ASBVjyvsgI08xj5fkNknmka2GVoHRNjZ4Acq9b-kHzGsuL0HUb5PeLQlbhQGd7FNHFLSz9mEGT-acb3_4-c-onLHz1NCgvarIFLtJwXrPtrUNTnVQhtUwsxC_78YRr-ZWxj1bFsec-rGUqhnwi8LlKC4o_7qpP-cenN3z4bm-o7GwB7Z4Zqnc7PEiTNwtKSJ_3uJpOs_gN0Oy4utKocdgkDfDra0ezdk-Ad7tXMZN2Tz7XbMHZZSHQoR7o9OX_YHfnlviZOtDQvHQFj_ZSO0q4csch9MYT6Pyg-iKjV0DKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFG8xo9KnaWG3423zx1s56ifCPFF_ShiZwaHn1jPo9546lIKEz8xBnxav7k9k73t_cOFDIaw11EATkkXseYnT9XTJ_zdlPaG3FRIZgHJH8BXN_fexvgVdGUfcNuuEBZMbhehnI13kM0pjnryQCoKZ9dDnjy74oYdZ4_YiU2ydUZ0f7VUcMqpPyoDk1dkeeyqWsAoEEi0l4Qzye0n7iDdQDJqIhAVEA8WZvFAqXj4gOIewSqq4aNcev9LP3n2Gs6HTG0VQa1Ms07ASfDr4tmayrUv16nDkyJUjftf4CKYlUMNcMQk5chLUmL3BOscECldYmAaSe6vKiZAKwvaWuHSoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kv9YlqrJ6iXaMRzjr3f80ere9Yg0e_MT8zvtGZSyFLUM7OKRXbz9I6w_eVwP_qeSIk5Kr6yhHB_koTk1x9kUldE_Shg-mwYZT69TmJYaPhM-ZjzgGBPqblVka4Nr3v8u92Zpr5d2T7S-rRKI8RoWIXLYraGs2thU1neBEPr6fW3NA6FvPO3BFCIr2mqqAjdkzGT5n7j3aYzS2_3jQLQ_A_gWu1OI2f_FRwYAvDUF3oWdPF4Xb8EStaWDULIITjuKn8pzV9G1FlN958UxQ7xhPAL51snEuE75dY7Rd2iH0rfu1uSQJRjr4ae_GeXmmB6JenOetqxtKUwRZq6GbzZi0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1daCH15QBjsEhEtg_YwOg7p-ZfDRMaB3OKviIGrf9HuX0k2WiOKG9k35JCTLbEIfepo7tC-HWmYgIA-gOJVy_fdYu6CnBtzpCTMGE9meVAP8PY032Dgcw6PaPjeQwiVyWCERVcBNE7LRJhw6a3Lo7PbVA2W3OJ61yOqsnMO08lqRfdNtZDZOyVAYF5xqg2i9C5VdurB78syPeit6FpdWQR5ddiGshYzSZmcRB4jNN6WsQw8IO8eA70hmq3uVvG4WkTbwDckzZUTrxvBNCBFclcnMglbifR5zs5zUXdLZqdfqrFxWL4LHu0bk8Ing2w83QwnVO7QFCgaP6o6r_geAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ty4tAW0fxVJKjDjjoj5hfZS82qoNcfpUFB-Q07JSqg2F93WuavjypSAkRlV92rSP_XJeufvdsXthCJNi_acorafT-jynGquxp5FcWdggTCNdfTjOr1wJ56hRFndPAf-LRsSHlqzOhPKDyEzS0B_WJycyo43G9N2feFGTn9SnxX8Unpn2gyqn3r32rO6pN7pbsCaCs8k44L2gzrkq8PJpdPjM0ZaHYq9QhLrbtAYBVXTi6DFiGO5yP5nyzrZ7vwIBXrn4EADUaFNtlYZTFI_0d0_B42eIStJ4P-mQmIujmR8ma4JjgyRiuPad85sL6iEfX-2XxVuZ2L0yjFcC26KJoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgRDkRuXfEFUi7zcnli6JejZMTv2-4h_hfnvnr-MP3g7YXuwDGs-_YDpbTfoCXgsqU2xOBbfK_ONOwoyl0_TYmZA6MVPPztO8YrQEqAKpBhDBkS3y9zbsLLAkGVcjygYqPNNq04Xc3xWFFwj6vlN11cCXlI0U4wWvQH1VIs4cY4jdg9JC76nVors90rcmq7HGFt_8SQD6P6PoejKIaDqRmOzFv7nlvxgCrAM4d8q72Dohc4BHXto-qE6hYs58BpJHLhCulqzEmFjKmce6e9oJ93sPxEB6Jjy20_OxZ_vp0oF5phNq7e2ahyKjBxRmWFGm3CrPHkBAY_WsZbW2k8y6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BggD1TuUk26WT2VPmEvF2oCIUNS8bOU_KK9DyS03dz8zNqkoYX0ISNtleglXhBmKN6R0Mjny6PGwh1kb1WzyYbww5wXc22EsebwNhs3JWw7h3zBEJ8aAGee06mmyO9Bx6jqT7JjdyPg-iIe_DqsMfFT1Avbjpo2j0XjQAtZJ4wSsfR3Mk02WU4XISDgfGvFVNObSBBCr5dFI7oRFFqQfkVBvWknpQjhRytmOUi_TAt7JwFt6ZyBFqsxH2UQ5qqOr3Bmahcxl9C7mXlGNgF4JU4Xxo6E7iEu-mcGfoEM_VFw-ZiKdsvMag1BBMZGV6vorJf37Wf5fGnQkkzUmEJZM0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itTvqW66MGf0vBDZpvktvlsPzTuYLw9qD95sSsSMpOuFNSl2keQLoB5c7PJJa-lfl8uwg_M6Rd0cb-umCA4K-qhcptuZ1yYygzopGFII_3Op6vrTJFRbYFQfSXPizWqv5BEr3yfclWh9aiHMw2qGveiKUWsWAYhssJXJOGPHP8dK88x-FK3jC9X5Hq_iPr-H-gIFXP6kTipj7RcqVmgSqEV8e_lhkGy_nOrN5uFjzIxrmO4kWt4XoC0kBvSLtDskFktPqJMs4ZwwDQTBZ4Mv2m-724oTdcgbGXdXu5AJeEaaDmLa_tnxJG45P-CVOmLNBYckL_4wecHByNItu9ykxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZK9LvqkYOyvdRNNbw_J19U5ZeDHhc7qk3ZtTDKhNjy7IsMPmLFRL4oMcWVorISO7kzjIuIvcmBsvyfaoBmzUuVy3p02Rzmojuy6tW7u17-rYH3_F8gaQv-MLJyiFb2FoUgLkPF727z-o-1ST8f8LnOO1rS6UYibdRfyUFv7G46EkXlSzLKeDUL7v8TTttZ4VFGzJtuxltIkQkoWq7tnlbRYniHW1-jn_Em5rzojbaIHH95f_Vqo43Wjdc3atYIVvCWX6A7IuzvnxH52CC-4GwHXThH4NrYrmAdchQ4fgO7zPauOUrR_1Nn3ZuhPZatw8-T0DlgFwLTqigTYaiSeoJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FonyXIwydQdx3urhUaX3gYVoFhfYJECpwqKjIwYtgFIDmwWsj_6gqsrJLzQmSc68nLH545boXvJJc5xLP7cpm3g5CoccAME11ArkbGtF8PkGS1-3Dp46_qPyO8U13YFkvYLOYSEAnuPXgWuDybTB-pFioVHIeqWR_rWgwmmgQfoEdDji0j8l_3AsTk_uNv2fLLWBWaoMM7Q3Yd4nJjvjB9xeiU1U4nEhxw4gloaCJg6qLDOUbj0YXo-0-7th5aF9O4VqqpMop4j_MCAEx3ner9HgZHNzX9HySSQUt798qIQI9DaCLTCKlhoCjlmlliNlPqIUdHhpJR1CYv1iYzOy4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wmr_VDOiYyxm-zWdl8Vn-Bxxu8jQ274ipfkl0ewg8cJPG7x17S7ckfqrzQLnDwl3Mz_fmxsL61XSTy1ICpGWczci4dISJQy41NSSGd-zQH0vl8OdyznnLYeeskFfB0GW1NYimAhvwVfbWTPMUQmqM7het_oaHzZNFaqu7Cq3fvpj-sCPzQ1oGJJaTQzMCoXH7HTSC2w36W27meLuqUsIIgxT0rVkCadIsJ4KgLjchMGdY1EO8TXyGIPJBJ9bZMiLdiX_-y1EQWZkkJ70czF3RvWEkCU842DxYv0gBqTdaIX1ZrdkZBywRCwJiRyqB5y4fPl7jDvhG6gKARNhkV9_Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjP26feROXHqwNmtHjYbXLhDWtEvo8dclcG7hznNwDrFA9U9ij0cDokOcLzRbkigDSb9FWPgkSxGhU7koJ8qQdwot9vIb-xYsGL7nI2e2glwQscRe40cz2iZLZbHazgb7ErCqN20SCkyhMyCkqqDpOLDBNtyEyVekOy9nvnG_gmunKr4i7zupbeIoZWt4SenrT2ZE6IFTGyn_yK2M41chjg_OJT4VE8sTmeqMJyN4eq9xyxLGvMTcafLrXYHElvpqyph3ZQ9mJsPgDOdKkg9emjECF5uXG7HvNWK-QvgvU0YGX8kJo7zbCH94JtJAUuHEdab4p1jTxw3Lm1tN4C9DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikHcqhYP3cI6FBDu5rGQlMO4f_eg6h8DTGHByqxIRA0h_i95NGUD8nuE4rr_ZBFprCZ9w9Uqq7FBMzd6CCRByRkcCnKyU7DWx9yH9j1rfohWovRB2skZ2-3wTSqemABWHpymHGLoM_tPyYgWwjokawiFHgxgQg4yo-VbAoLsJLBSkbiVWOIi22taNIPL_eAyLatpya7gb8hNYKX5J-Ah892XXjT0wJ8fGNynU-Z6Dp_IMwdu_0RMXKvr9p8VBmUEMk7VpLLIduE45XxxcDtMHRn6rEUqpC5k70hxw9DWnf0b69na8XufxflJp-iODVqIrz4yfvUEHiB7zkMpdqp0xA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=EcMYgBMuhNJYg5gMfquC7VuKE9l-_JOvarQnzTyAfJFAqYZYlEAIWRaBCl6505JXVncSB5ZAj350ar2ecjPdzt5SKelg98_KDoK6slMHWDH0kVv_sr-_M8p1Xz6nmdU_HCosgcEMBalmnxrD3Xh7hErx_q-LT8wG9S5Vq8l3X-iCCCBb6Cq4xB3WRq5gz0LfYR8TOSfJTJy-hUV_qtFHofpp0BH6xQHkfZgF7YZUCmh4hJ0qIvjdFDSlOZOZrs-bYJkirhr679xVy37PgkC2hEv7fKn-TscVXl1qx-VjEB6bF8KuxGxvlTbNdTJpZFWGqc0pSJmEVyjKRCXFj2gz9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=EcMYgBMuhNJYg5gMfquC7VuKE9l-_JOvarQnzTyAfJFAqYZYlEAIWRaBCl6505JXVncSB5ZAj350ar2ecjPdzt5SKelg98_KDoK6slMHWDH0kVv_sr-_M8p1Xz6nmdU_HCosgcEMBalmnxrD3Xh7hErx_q-LT8wG9S5Vq8l3X-iCCCBb6Cq4xB3WRq5gz0LfYR8TOSfJTJy-hUV_qtFHofpp0BH6xQHkfZgF7YZUCmh4hJ0qIvjdFDSlOZOZrs-bYJkirhr679xVy37PgkC2hEv7fKn-TscVXl1qx-VjEB6bF8KuxGxvlTbNdTJpZFWGqc0pSJmEVyjKRCXFj2gz9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njqJuuKr-WpiUa4lGC3D7KnpBWJLga1xWkJyGlvwJGJmzNIv01k1QGC4pl7ESP_IES3kqsnR2Pqm5eAhxKd11g28AEQ5_6gSRt4J0W69A6t0MJetXtIzhbBAefN8dx17ofbpetfzzEOHm0tI1C_3TLn37UCzD5mDzM6o0WAxmEytn9l-1qWqyKaGfu6Cf07kfIRZx4kuIHstUVoNOS08nGc_15UMYrWMAeMSi_t-USZo25lqByxvEY0wKHQ-hdm8jSN4_HcyJG7g3raxs_pNO4Mqt1rkFZvRsDR-HvVFNiOK50ldFgcBqL4DIjF39xe26H-DYCfrIU4fz3602vVsxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XM7VxF554UyfgOFG3X_ZZ7UmC2Y_nPru-ibCwsSmhUYduIxtZrMY5p-OmmbQPs4hRkCvEpV3u8RTA7wLGZjkYJuTmoJZFZ4x24gXRf2zf_WiN364c9REoZtpWkFttR-fiSHvNgzsCZuv9tNdl4uw_CP-sCtSJF9CumHMsmPFwE0v4sfX0mEYCdwYvYiwHx6QRV5sh0RNLOsjyVOwApHdR8OoBwjTuyYHlGz8TsR-FFAfGoUrxiGgJLTmLU1f1FeKKm_FwigF3kw8AmKhk71R-A9BAE1fpQrQnMaJbStoOzQ-_gCekUbThFdBz15X77VdDACOLnRSZDN5wGuc-dGRXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duFzkoqB56lSgp63Y7K46PH-0SyFj66DoFoaut3oaM08yAtvwg8F5tOUYVpG6b3naxIV3Axw3SnKHluvP_Ap_oDqHKSXHDdD7aJjAmEKOgA9XlDwW3cDO_s9yw_G_5q3Xc1Ylolw9qqZoCPpAd7IUSkxnY7gwEEjZ6M5IMWmzS_VlT_-nBDATYk-F6rLIZJLLyYO3ykkCy0nex3Qatc6a7pwmQKvtz0F_c-5XXTpx50ItAxZkYfWJVp9VblXy7jt4u-Hz08C6R7Uw0n71VBVSnr72DU4y2-QpRRZfy1vULgqWrPk49a9WN_9pdBwK290sPNx5qpwRwv3YsZhici_lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpclH5owKo3yMNpjwNl8Q4Y9NMcteWnLosgVhburNwjm9wP2hXB-QOUlI01073lAGAZ28rS-tp8glJqO8m8ZjS4I4QEbGeB7XK1QGp6ZytBortdhqoKFtn6nwCYrHcAaAXaKO-4SdhDOuNA3aydfj2mXEypvOoLdG-8pe9Y-ovzWq7kTXtYXh-oT4XRE-MT_Haw0R3nZi8049iJHsyLm1WAtfPYWGX1ZzyhI8_Qfb0RTN_12F4vKSQMJFX9r3iyuYw1NYpcQf0Yk_7YAacHAgKorv_CiciM5x8kmY-DMmPds4tdY1ZsEBETFwiPxeOzYDIHmBHJjAqaqJtOKTJIrGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcVj_WSsM5whoQPLbcAxFPNJ-siJD9IMIagAxhUksYAgeByo2TxiX5TBImGfr8lE09ObIlblWj08_YaipMp9o9nrA3uNWb_rvcRa6C2k0f4prSfQ13xk42E0yimSTKcu7XxOE5mfRKoAXby19r2T1WKJDdsl1zKK4DY04o4fAp6mhyc1UsVmJ19rrR9RFNp0f-q44GAdYkzw8QzPJdmSmX87BihQjmMXrGS_AkzsU6TsAGRHKraNgm3XzXRzXML08prZHlehApX8VszgdRDaFJKb52p_JNdlG3UXNJP3cIBd8ZdL9nG5XC3HeW1uLALbuXcUGva1m6qeIGFVzMDIZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EehkefzoO_zjH0CCsvK65aAU5zPYfidmmoHSEqBNDNG0T12DLD9Xhz_mQ-ZC7JW6TRsZeRa3Ixey2CfPzhDBC5nf8AnPaPEMkA9gJFYaw_JZfb6CInPnckwv9pFrmaUhUJjylPhIq7kPEcZyDlTrBB3mWtF-4sLOBFF8ZSE3tvdTkrQsI0AgAxidfmpbtne0XJNeZmYjWIprELnfjSol_ZlEhG21M1jF2873w8LNoMNvfxByMyKgaoIaFxamtfk-1hWsut05lrno9kGDRYghhY9SE1enLNwzEs4dKXNJsns86d8med5HHBpVy_TrzXS0D50qlahIVR-5Ed0DToXkUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5yLh8ZctMCOrG7jrScw-mvlbIrhQGy2xvo9XRDetVJwLC4-d87QoT3wvybdIuEMxcrvabQX1BvSJuSOwjKVpI6dw_Vt-eKiJJcabizdTKEPO9hIVLg3B3TbB7Lppph4K55J3-iL-ljKH4oF3B6I0rjQae98KX9-8OM5WKMMa_9PMUZBi1vWsVGQF2C6kS6tOXnLSdo-82sE8HsLCZsEMUPwooeiULR1ZM0B-dqKqNkXeXMglBGYOwhC3up0rjFM9t22FV0ytPztA-Ji-4Al4azMe57yZs4k6NetSF8k_vGjYEjekX-gmNVRJEhis-0rE0bu0uevOpFPI5DXm4LWeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcjBCo9QrwDlqMQKzUp4YMbQt26oone1dRZWlha2hhPCjw5kT6ZcD__ERSjMEv7pCe3dlv_pdAgRS6y_TA-HIjslhpQw03ZzJMrwXN3ukaMVL_nJBmE3ndoEeLsqmTUBliXXoEugUhokUXY3AenconWODUlKDE5uYi5aoUoyyMJ6cbS1mHpomBZW-p57AJEPEM0pMAMdIjb7fSBvyo6od-D2t_C4tRBwQ420JYUJBZAKIRL7pZ01hX_t7SrP2kHoUjF-9cy44jIK078prqtBoMyIPDOEQwWc9evptlxCFBbeFKmGHm7x4uGisqDnEwABOl8XlSMMR-M-sk9uKhbQFA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=CTWjk2cXXj5pbBRaBRjHJsCUFyyKGDJP6nn5FkC34-101aK_-J7cJgmmWXZBMUNQWQ5iJmIRMUlUMvdHi5ScYbbszwXKNn15MYxvff1kWdRlFzUBSa2UAb_RRnWE6kGqMwawinh7PbVG7rN-vhYLIxZ5RKvkfdDVjP4GigxG238CSRgldhl3yNBYHUj0ry72roiQ6teCy65pGjo597uBE3yKZEgYMEJfAaZkA1m9QW7vhggF2N12a2_kDa8iWeK7fc9eg8mi6V3-fXsSS33ZLVNSxGbEj-WS7JrtbTIVCM6_DGsa4dIP81Wf8JZM_FxNBiw83tdDcCf1413GzURfCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=CTWjk2cXXj5pbBRaBRjHJsCUFyyKGDJP6nn5FkC34-101aK_-J7cJgmmWXZBMUNQWQ5iJmIRMUlUMvdHi5ScYbbszwXKNn15MYxvff1kWdRlFzUBSa2UAb_RRnWE6kGqMwawinh7PbVG7rN-vhYLIxZ5RKvkfdDVjP4GigxG238CSRgldhl3yNBYHUj0ry72roiQ6teCy65pGjo597uBE3yKZEgYMEJfAaZkA1m9QW7vhggF2N12a2_kDa8iWeK7fc9eg8mi6V3-fXsSS33ZLVNSxGbEj-WS7JrtbTIVCM6_DGsa4dIP81Wf8JZM_FxNBiw83tdDcCf1413GzURfCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSdV34atSgMMiOXJrS93etC2FgAfkFeJ2OX_G7knkU75e3o8J3UPT-J6TTuUVOhRM0odOkJAXUYfMBH_fJy_tn19V6hkSDNsPov9Ow6pUAoM2Fp9cx0hN5ojxVRey-Hw_eUOYOHirqmxuDUsnjTGHvHxVxJWGhAKuU3I0b67B0pErn2XGdSdB1L0Po7D34qSrhFBzT-9Dq0BkYvATGct1ig47vFxer6tYoD5IgwDUQ9QUdxH-G2FndjDsB_qkW65hw96OiWPaIVF-rw3rVEHK4QZwD7NYAigEBjVw6Na-1MZSpCm31un8fJPdhiUSvWsbkR54KxrF2KBPItn-USGwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFZT-po3esFhdFsF7PIdLsSLaKBjNKl1EzhNbUCjDdcIM5Tjv0dQC3v14kVMl4b09m2uPvWlVpmn2H70i7kGfyw1BXZLYjx970SKBYkqM4XWCHEgdX6WS1G_GH-celKUmqgk9-fXrizLHyQeeyCh8GGYJD7gqmR34GxSk2936i4RASUJUoqlH7ZeqrxbZnEHFD19aePGWlzY1SPkJzISnCJOhWNs-j3G6iZUpgixlImwgrZgi_JD5956uFMuN2Ep96dcyI4kC09zPMy38Fre1LU38pLTsfOQgO-LfaIIMxy5SYKKnwgGIMUE7Cc_9H765aCRDBOp0bTZC8i_IqnkDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=ov9Jt1EPZwQvis_tlInJlUQaHqI3kBSJzybyTTDYSmqZ9SU2ovoJBMwhHs3qxLmwesSdd_QoDB5EhCIDD2vabEkBwTWzf96BLNsEiPJ2Mc6khLurlR7BMcIu_0x-gdlNbdA0lbBIoRMbwbwGZKlYJG4uxOHo_BtrNrw86XKkbIr5ZEbSEvLMDuHirTgpgiBYdUZVc_LkN6J4DFm56X-10t5dCH4pkGOX70hC9MsmvQWyume5qjORMBVXrqiAlMsg7Ix68YCBekKOLVJgWqHWM8VxRz2prQb5ciPW6RfjmIUGWz8QjSt_ooxiZq4NuidDDPfkfoNqejlpAqUcd6KAFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=ov9Jt1EPZwQvis_tlInJlUQaHqI3kBSJzybyTTDYSmqZ9SU2ovoJBMwhHs3qxLmwesSdd_QoDB5EhCIDD2vabEkBwTWzf96BLNsEiPJ2Mc6khLurlR7BMcIu_0x-gdlNbdA0lbBIoRMbwbwGZKlYJG4uxOHo_BtrNrw86XKkbIr5ZEbSEvLMDuHirTgpgiBYdUZVc_LkN6J4DFm56X-10t5dCH4pkGOX70hC9MsmvQWyume5qjORMBVXrqiAlMsg7Ix68YCBekKOLVJgWqHWM8VxRz2prQb5ciPW6RfjmIUGWz8QjSt_ooxiZq4NuidDDPfkfoNqejlpAqUcd6KAFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4y9P-ybM6-HjX0L9CoLE9hEDPf3nP7qSiPq7gfY4n7OibBxpNLzKLzFdErlQhTTQdbZLeWnww089-vFq2uB9AsTTzlbMq36rYPtrGnCYuZGOVHWDg4a5YiZS7Am9vCPHvQCW9Pv37x57q9qf-fe3bsD5te8ZTZCBoXwaypulwKGTVFXaIpJ-4LpvjaDhToDvupdfLHKo_ackj6BmldlPTRid0UJDa_RUcLwPSrzohk7LhldanXD8Ha4Kviqdzuf3rv5UbbZkmkPh6QXaazIsZLTrN13jetnUnHG50VDqKSTdHfAzgjI-LLhXVm3vQStmDm-Qd79LE_rISXJm6H-kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ipyQTtiJWOdcf9INzV1ivKCwCBflp1cibW6N8pzwFIr2kFUB2WswZJ-2cM2pByPrgNPSfGmY7dguaiQAl10EMTLuBoQSeiDaPtoZezDOMSev4I_r8WO7OinC2zF553fWdEC6-_RHcNX9NAtWE1pWjYE6ko9kvQsnW3Hh65aRF3zBFY86QMvhzODlCrnYw7_27466biwnghYA4E1KPTn0dplx5I2d-YxVCoBN3VtGbHx3yp0x3y8fomq6Miq_8udIVmf9yMGl2qJo6XVqcuX6ZKNiuN2YY91l-rgjdI1rd5_zrukUwpMsK-_kuorLk4f38-UcwLFH9Mo0ex11OYL1Tg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLRUfUflXM7UI8V-_o5rxEITeSCx7TpVOuVHL7r-znUcp2Xyke9aBfgJo-dHglWq2F5O8aWGk5cxa_KlWaxmNHqsf-8m5TqsmuIxBYSLxRpYjh6CAq8FiTX1AnefmMCmBk4MyujE37Zq5MUIpGB1Me6ALhBmYD1Eb-YmSZF-3Qoy8giu6Z0Nf5zhBU6tmMu9CRu51y0VbKb4Lt9sH1AmcBm2okvgbaJ339ubdUtxWz4w1qPK9H_Xgl9K_EZepUaeGgj8dcubgnGvvOYjJdfD9Qi1myqqLWhT8YJtz8WyMBtpwWPJDTqriSs4_slW-vNwCeN3Y77hahX-BJB4xBpG3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtKkrr_vcdoxBwq8hLyp7raQSnsRiyv5CCpN_vp6Wj55h1OuHl8Jce0TGrzK_ksUlEDMTCZ0nOw4twcZ2Mhj_2L8KOWfwScuq8PSW4yu1_J3J7aPjkLIJB6JDizkbz-a9hACyTQ6HyL-YKOZVoWtRR0A7kWSghlV18_W53_730PDBvAWNSDrrVXc9tWlYP28WQuWYcrUg8JAB5LKEuztd-AKWCqTKPUAh4dZUYO6ZnGixBaR9uk1IQL8PBjNYP5ltEVkvCC5eDDI5oKBR5zGdeBnJPAAIRxakAfbMw_HI2Ig9l1LUoVYYBZr-Cgvm_WdXWKLm5_aI1uqdtiJ8DDjmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Soy3A171zIkO3Bs5XGDLpwyDPkFqFW7oy4CcOwQ4YfahDALv2JrEN15Cw_0WWk9mDoBl-2aH1N-wMC_3QE3TSNul6t0KNmv2jp-ztKPgR8GCQZDetYY7L_NhrIrLec-KzmEBvLwhGwrmOlv7MKpVTlsKyRkbsxzFzsigf_40aC3wFgKiiP0goDGdvsjGmOOdvGg6mW_U4mDI6JIkTLF4jTfJSi5aA_nzHJCCVD27d0JMSJCBFxYqXzaPiSCF4MY3VPt-7tVFNnyLABBGPH3dBJL-siKl-FLA1tGY939Yq3_OeeBcALqTCq22SpAi6m2Ts7e8O7ciOoQrO4y7nZYRiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZQ4wLAL14Sc5yInTYaaQl6RNeW5ER5086V7BB0ghVXH6b3pVUd6LOyKbS7RDpygsla5nO0Dhk3OrNaKoSi-OVs3Oh5Hr4W1pEwl6P-crGuWZ5l8MBtUY6MhPJixBTJ9PvjuHS1M8Dt-_dk1UonmKC_rBWxCSgEfRYXlZB4iPOXkz0V7SN7CfHcNwhwuiePsBlzpmyHctxxWuKbRQbRc_XvswzAHxl9cKGdK7f7ir0p4bv2dzJw25sMDO-WLKmPM7cWIZeFg3bnQKSl8DB2VktDXc-JVuNXlxZzE31SEnTabGOb7uMknaRy2V0h7wRGgdA3ASS1dhfvvO6vHtsKaaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txBXW6liJXNnJDFn2oyv4rdURyTJrcOp452QJE8VC8pf_Hj7cNfg6gpgwgGob__NbWqj6WAK6Wx1AAvvvDDkRC7r-7u-ZPnu0WijSJzQ6b1D-24JMCeYKWFDgeQc0RQ4mpiTWfRkGuyMcHT9iLDcM6v8lulsuAlLuDAVsvNwMQm6DHwj2KBD_7GLzb7vnfk9kEEruCb5cty5RJtURLecynIIrAI1PzRpMYgQgFrv_821uIcdtTuyQpalZAG2fK5zcTIrveOWDpTO3Lu4YV_GtIEEePE6daKNs-C0E9FHlcH8YreJF-cl89IUHmS7fwN519b3RaL66zrhu9Eat77RkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtSx4Q6SkosGI2_Fy1ODwjM-ofA-qOxsdVLy4gjkv0Inm9mmVCoxUiEbdoMqcwNoqFajWASq72fQtxwug8bhzpXLJZ2xb0W2x33bBHIJ6UAhDqmOC833ze6MyLmKYhIqByDiI7_nQEsHGGuBMXPzaW7_5GdNBNaL6jUTvl5mFk38hN3lp622Z2017G_MFDETYLQjlxSjKLhdTqxOcDxjyMuaAa2aVvPbrgjtC7Dr9HpApNMnSG9nHFqY26LDgwhZCbalnRfWur6qgXYAmoZjO1vbNQVr2S4qOJ1VwzAPMypp15P28edj69_KkmnczZGHC6y7KjO7hTKGr_g_u7MLag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQQg-Ur1I_TkwOsRclbTU4YoUtZOADcUWKZP4lYCoGrimUGmzyGv1cFokt8rXXI_o7ENnyYuM0OHKYs_1R_IqQlPEztFbr6WGrNPXoVFI1F_hOpQ6MnMSLcCdPGmhfnNmlUpKOW78ccwTyYSyD-8TBdpkWvrL4hd4Vzx21qjKNrvoY6CP7ANVorsnuxoas7MD4GtqClPChR5AdXytM9PB9jey6feI__Ne2FnzZI4LuzmMTgvJ0a_1zCgwnTajo00RKvajE2CYK2XfxhrqpodSc_5Txa1Grvjf2BPdyf4NdwhjCsKnUBBy23fRJT3ET_Htf0RtiS9CL0nO2vha141Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxaO6s-PHItpXjbdXILVgvkDp8pHks8x5bG2e37PS9BLxV9K8x6_tFQAr_8VNcjgPViDRP-x3DsRsqb9hQdqwMLzIhgIzPqdoMGqA1bX_rXoK-q46qWh3rlbXkePqSpsuopxgwE6wuwmt6I_DzkpHCvxo1XZbEQ3CUOyqZxCTqo60EBOpiz3apGXWmxVGF68y71Y4D91xweWwfkBhQNNhvbauVou9DRdMFyhPQUT9nxTkT5nFB2fFjJV7y0i5cVDk8iLSP0mSPkHKnAk2m96aN22UmyZB2gg00CN63mheTLpi7GjRgCyzvnKEvBe5JdJ6JkqKp2RtNlCgPR0eUIl1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zkt6RyxJXrYQPcSjs7qABNItLqFaqRFVSexPgbVtwhTbtkXGKIiHz72DE7p71EtfoOqfE018LoPJAGyfz944KaEAGXcTpPG46gkSvbCHNMPGMp0CGAQkGm6QSZffq_HSqz46JD7yc5eVaLMvMN7GjPg_zpwI0C9gDRUQ-ScoPoOE2CGio0IhM9jDqqZlIc27a4PPH1oOmM_Rn6C_HVYonzudoMGlKXVooXZiMkhglE_Fa41Z3LiRVOMZVSk4cdDdpocV0Lzjz425bei56AwglwpscFTAn7NQY4jvWQNT3RoJVTT98K3LSD3YWgvadzwvRDYQmm2O1nIw06A9xHPFIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2vTt_DdF2Bl6CQ3CvQFGiWQ2YS3vlx2mwNzJZgW5ITJbSrayfaiXM2VAVrKAfpRrVN4Y8ZAC9rXihAl47jawMnV_KoEqlRPYN7Tmig6fh_epq8tkqtfRkghVj1_6NeiW8wuuTSU0G31TkikSlIzciFmaFFgeCXSfxZJrD0GTkp54-2Gd_Ebb8eRu43EPrK8p1a9yl2i1DR38_JXiO8yCPNsUeGLtwue1bdqb7wNiRURuT3d7RdB6Rvr4lWLW22GoXSF_Zk3MDoa5rslm0eli4aEAR-TbXAzvrRmoRvZeWqyhq1jEx5EyOBW7DcoAdj0RxgVS5sNlWMyYjC7xLuwxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhSAtvEURN8elL_yZZhxidev50iOIgVNoWYd6zwjDI-i_vZTersZj7LZenj87vuJn7WHfwKEuWeZPoJY7hDMlBC1nyBcV2zBcLl32zyBTrA0ndjPYDijFJYZbAcFYi90XjMayw8F7cMeocpJSOyNQXIlpYS6UndcBdpwMhsnT5lWxZq5_5CNSnlrkkqZhCNxtmVTP-nofdTV46J7iTaufocYfmc8UGw6Q4geGbFtQ9CMQQxUx5h5M76jwtk3e5U6oinGLpz0uhN3zdKWGKOTSK5aIazUHl50qe6AyiLHBSXzyGnigpWG03qYtHb83kGzDkDn3X94ZOOHrFzIx5Xm3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLLTxb7Jf8Kjj0j6YII7FNBPksapnhh2-VzU-1lk88nB5Y2mNBgKEOMzhK42wbdnpm3BVxWgHUiZAzuuIOhmqWbQHUgFZJnOnBbbXAmx1tJ67c1bUMAe8gX6muAT0Ahb7DxkHIwvq2T0dos49Wxn0lvmeSukLag_TJMT4je5desd1rja5da2e7e1X8ag1QlhKX6JGI0Q_NWrCvcQrFwWzgMv5VgaDwHu9_6uvxHRAYVIYoIsiIRxcBrdAkXOfytJAaGw6mQS0OQD8fA0aES45rb0Y8KQ_7tr2tU5PLVwi6nVtQUFbkVyMU4VzHX7GqZX9Q8r4VIqdQ3p6nZIAwMuFQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=VkltOensSY98Oyv5QJi56Ow-oAxUuMV1yqhq02uUx0LsLCTvJvCh7VsSKrDgJjQ1z0MnWYdJKInvRl5MDWoYAJZ2Get_E7BlRU2It_8b8-25Y-bszReqfsjOqyzz-tfSg2FUdtFwUmhXejO4O3hkcwU5xfmi10C1Ww67bH2y8JbyMlx02b8Na651TIXbonAKDf5Yv3txz0Sl6OI2t8vfUoz4zyzd8EzRnREPlP_PCTqltXbLkl-4cQFk4TZnJWIuCHAc_vgd4nJ0AzboDqUOfpfOQBIrHkwiFrAlfIEZBe65JrLuGiHh2DXyB68eQuXrcABYLod5lSTQxE0skUd1RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=VkltOensSY98Oyv5QJi56Ow-oAxUuMV1yqhq02uUx0LsLCTvJvCh7VsSKrDgJjQ1z0MnWYdJKInvRl5MDWoYAJZ2Get_E7BlRU2It_8b8-25Y-bszReqfsjOqyzz-tfSg2FUdtFwUmhXejO4O3hkcwU5xfmi10C1Ww67bH2y8JbyMlx02b8Na651TIXbonAKDf5Yv3txz0Sl6OI2t8vfUoz4zyzd8EzRnREPlP_PCTqltXbLkl-4cQFk4TZnJWIuCHAc_vgd4nJ0AzboDqUOfpfOQBIrHkwiFrAlfIEZBe65JrLuGiHh2DXyB68eQuXrcABYLod5lSTQxE0skUd1RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaNH8ysnPjwC1t_Qao8EzskVcQ-In24-8AFmO0NSSvzyPtHAWY6wU43fln6vjcsYEvqNjxXCXFkMmwwtukE7kvhkebKDVZM9NmSBxZCA3JpELllFZ-b514TZ3ORBCCqVkK1-2pefroWK5GJfpSX3-BxmVB5BupupOs9TCTTm2pYZtkOLGWi0ro7IhaevbMLmJnwhb052etcqHEre18gIkODL9276CuurYETJaUfwv60AWS38MOoA4w3poa1SlKki0-bBkrE7AazNfuuXVm-Ek834SPLXzZ1Sv55sxFIoUFVeA8_MfrvrJ_wMbGfPWiFSVwWqWeXqIcD6_94f9pg43g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntxN_Bd1q-w1e8XBFk81Z9Ug89HsKocz2Ip5L7pQ_p7pa8vsxc2rzOPvMgI0SAHpOyHUe0UR193BtaogZ-gJ2yzXjS7TLgRkED0S3IR4ojHxGb7Iyt4q6MsAz0Vva94FSduD1mWi7V1wx98Lf2Q_ww0oQ0LRDLLyFKdYIuYA-jbXHwuD6Dm85_MDhxQcytOqC4wjmqsIdm2WVj-XmR8-1OXVb5QyGuZp34egzdyKtejF-rwGihEoJQx2LsywjtkKPu3g8pEa2Tk8fT_XabK24OIwln5JWkdO4Hlx5ipWr5kJ5yCN7yI7Mc5I0kUq_woJ659UnDWT4CvYMO4DelTZeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxEEycNDKLLzufGB7vN_r7lfaKRl4XDax6_4F8SJ5Gqomrpyt_P5TqDZVNrfDX8IcZYD7QB-ojJ0yFcmvSNX4vL4oGgBYzWVA6YaPbcmFMdiHsYLMbzGJj0XH-4fyN4EzvQntqmo8nvce19ueGoSSSYgkcoSMYMi6GYGOi-d0RP_mvJ74u0_CqIAugQgYIf6yJjRnaBeQnQWWEt9RFBr18HsvV9aTT5UM6fZjIv0hXK6jAMdJgri5ltHiS9DoQmYgy8P2BnyzIAWDEgKZIXuOty-OsVubRpSB6euKSoQTcFPE0a7Ws1jfSnbpH6b24EcIUy4_Eny6z8ej9rVaNLHwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzJ1cmx5MljdxDS4V4zAJ6Nhx_5ekaJ9GWKyhhzsp6h5SIvZYWRR2eW4e3ojwSG9N2S7saVx1p9wQOioQVkBllxii3KaUOGvgoTu3OL1wLrKun2eA3OXvRLfGEe1IfPsTVQnN73MmX1yDMNdP4gxuR2F7WvPqcdyaw9G0px77dyDxfNVpxZvI6XyLhB0YMgg_OWiSEHRjNh_ZDvGrsxlLSDOZLwgMZMQ-lGXHbLo6rkitMNgM2QyGSgEbN3smrPQd6x9871d-zXbjGAFhazsp-CgMaV-LVnJHtoJYyY7Wv3dQq9M_zkzIRepdpLfyDosx9jkZq1lWcRTmnpcJoinHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veaHWHQ7YDUbIssd4KIdr4R2oYBzaDHdSVBS1a_zUm2SpalYijsyi6RZf7bfpYlhPULcvbRrYQrn0_HObsFbbOb0aTSrGiD6hCj-3C4GSZ4YNN2XidSqY4aD-_aidnWehoclJBBlWalQ9BDHMPttG2K8BeJpWBfyEntBGr4W_wH7msSkfC5IxBhlr_8iqhqrGGeiCY-tbECO-m95-b2PkrdJgqGC5Hji13IZ6YJ28w1cTetokTkJPwD619-mdGmGpfOUgtGJtA1wMr_h76gBP1M9j0dWDxDiucHlAuSByZ1mU3wQ9gQGWZqUe9ri7WaUhRUiW3Tjxl8tLNijm2GU7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bS4S16wJlYLfx9FqIpAbeIdAilRGIiZH56Mq-C7KLZecmmlq8OGgAL0jIeY9dKKrSNY5oqifI8VRQYbRhK0VHKkvMz_JUAwRACqpZATVTyuO7QFGYVzis4Y-YebTCnQ5_P4nmGx_POIkQPfMo5BSfgHqXFuoHa5oYsH7N5DtQKxu2hKF7ImcmaT3adQasMOWuoPoxISRKuG85El36aNNnunZTC0oBsXELZCcnFYFp82lQej8sSaIgG3Ogcabtbo6EFQs0fyN3fvtzEzB_QCZDcmjVjMnRoKI7PVDdaUOKiDUoFrgrVo3DmPe8VTEcpXvEYzyhV_mVDx9aGfuRZ62Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3gXP73sSnBRGzGsKXYsVUziIS-21TnjEeYCO73U2TLqtTLL_qmj4MC80KIJhkLKozPlmaxXdERToiE1_DeT5uDr5bcExpJThQez2PKgcBWjsfnQ6aFnVmgPTmYbuvgk_GikOXOEo5sDQ6N46-BSP0YqEvZ0UBfQIvJ_XnGId9NXZZwGKQCwZl2f2NcSykb6xN5PZ55YcHFnIsNMcQLuBh7nOGhqj6WxwOIfZNCgVtLbtfxULhV5xls7UF3vg3FLoS4hDrU1hsvQzTEnmq4PIu3HjpIIitL2u1AZ9ZWLe5Vp-GXDAQ_n_pAbcIyHja0m5dgRzv8nGCDEU5O6uHlc-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jorLgEYK8eAFfMpDd9Y1p7M-bluKdInAudNEgkwTtaBq7GGy7iz5FtUMfOKomAEQ-vFORMWGiKHi-NKb2141QIdna3or8ev7kEO_6zFjsiW8Yx6IJJbiNxIDFttOORClMFnBaKIzSlRAE0usTqhKkSMHBTMOJ3v0rFCf0_azNwo_mErCyTvwNJPvSRGADxUsCO-bdkE2_Lxu5Q_scA_taglDXfspcQuL6srOSwXlV6Vo154W0s4WJo3xNhBP_8y_i35pi8swZbDLE7GRfH288fhmij6Pt7fsDbfrq8y-h1guclppfgahJrSqIA_gJltkhIQ8ybZ6_y6_1YxWpp3YuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2ZTNvflDuBSC8X7XGttw13-TEA1c1FC9MvLfjParmt7CtuwycI4Dgy7DxlCGvmIwN90qm6_C203hJg94-Vfmc449wRs4XIAODUiE8fJrvf1NxLoxPXYN1HqnWgOVelfqIpZtAL6tE2f6hrXvBxPXwg4e_HWYH31P2aqmxa_3_2mCn3-zYeGyhbAl5KEYRLfjRmjKAhpjzCsaZOtYMfv5ICr5iuAyXuend1eXkgoD1nOXm7xlfHoHTF5kd3J2I8fHXOJXviS4JxnOWUga3oNY7bRXNEFuTL5SXWnkC6fNOne0osGOwqrgbQx8eKarKAYpfZjvtFtrVVfQKPb_XTKLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZBZm4h_i89cA0D0VSVAPEdra17Eyt2rdNGlzzRPQQtwWfIelpD2EngQLN2GPzeqKDyYGDDH_3XjeK4449q2yvBIm4SdcgW9nXTBApHctFX8WIs8O5LUbMPa3tArUaPI1ML2TzbVVE-FKT0iq60V-wVUYOgoWZ0bhmrnYqs3YxbZDgPeoF7YwlUc5VoV1xe11lxi8sKgDT7bDTLN-8frftq5Dv926sk3HtB11Ihg9ae0FSvdN5d9tRrSy1bJbEc67jiYf6Grf6ESKch3F12qWLwPh_nb-H02jMGVqSYT75shGs6zn9GcFDp-_R_ZjkHAaoNG2PWs2zJIk7JjSKVdfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaBv6XtTIKYa4hcbuDK9tWNpIvZLPvTmt6vT9sBULQ73lQ99l9r6FuYChFDV_XegJF7-Pthx4FfjtdK16LWEI1zy7X063zzxONwqFHjmJc9MYicqz5tDz8y2Gk2UMh3Jw88UGjoZuSrrUb8CZSf6kGraRLtfh-EhTF3eMJy34tiQql_tP7MXwWk5n3nbMU2gth2HW3ZMTFB7TUOwWlr2ZPAiwbHJrHFpWPX38IhlRm0Qs4Qaj5QilIA3zNeO2tJW5QaEl2rmaM6Iwa_LBV8aPn_LgSGeVPEkoBECNFmBuziRfkriZm6HUo5gvvIY415pPnIRF-r76_oBhxQhYhhGhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-V1jq1BCMZtJHqWDfmMBmQoWXPiU7Q5vqAEuc2NMMzij_RNGliwu5cuKmsNskGp_YZXdo-weO1S59lMgVl-ZZcyo9j2CwGIq7MuJHfOCAWdroRuvicTcbc2CKa79r0ubJmiIM9Af6oF75uGauuT7dp2XQ119RjlCX1AeP0TY60q5JyHS8qyukW-hmnBHOOvPA10pkV2AAadbiI538MdksunVHzMGvx2Z8ltJG1sHSElMqwsAF8rxv10u3CnOmnNDxqyj5XlZAvqyOGvVeiYAuuxL8VIPl39j6QjTWMqFmDySMv93o5_TMRYKIJfIDitqkpXb3ubMU3WAvomn0R3kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nH4ryGaNRhQiDsMAjZeZE3twMZyeZuONm0MNmv8iPug2kgqkvZqaED12oVAGIxbJBYri7epV-ZHmvBp1N6zGSPVKBbpGXkWn_JjWE2Z0ATF1KGCO8D_vZ9s9msDICnktj-crHpJOOnTy-1MYzw8UmbS1wZTw-mHQDtTIzhH9aCYDR4u1BT55M5RxVNgcpGoNx_n6owtlfcRhS9AtNQ-m3OjPfp5s8sjjtTjgudJ-Fay2NqTPlZUD2pqmEA-B1HjhuOv8mIj3Hz6mXibKg4mra6hYPT8GWzRuHuQo2af-Rx3xE5h5xMB6Ai12OdYtCFJOl33XROc_b7pIc_XKLsa0hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJih1jpx6RHOSPnBUuxOjEBTMAHO-Vptx0oGt-MjMg8DwlOK21grCeppzJU33OOR-WQhBwdAUTe6vofG2SYlCqPHfS7aL-2x8Erbl2KTtwy9kd1qyoZqtWTgZELwLtwVmefxakfxwSaUNe6_m-eCtyNZNVCu2kU0lQPFtju5J00S0-l18ketHqKafVhx5fr-mDK42YCx6YIgbh0ld0CGy3JwYLp7MwgIRsPT-IlALGJggSyjozhYII1Fxq3gJC5GsUPZpAoXEn3p7oSR_9mlJRTBmiu1E_wdhConmUgyWTGFDwyewEqlojc9u-3H_ZBDaIeeCR5WF30lGGOdDkGw-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSyoeOvX6vCwzFdWKP8m2dcmAAZEGiLQGWO1iC1ZxF_j_CXnYhd5ceoLR8LTqxsa60XMiXVzAN0WTK0UuSvDUKHUphqp2IBiXf8ztyHyll2PIH-7P2ew10iDTZ6wVCvQuCOFpjbXlI6-rkP2_xpe_CYS1gQedkod11zlsmZrC5XfnUcqq0XLmHv18LEOUohR-bfReyLWcQSyG6ZggV5FLiivo9OEqbkt4_QUnIB15lYPKo-RcIB9Ha2r0z_6-T_C9tYMb8AznEDAUMnwn_n5edxeY85W4Uf_6tfVXn5rRBeDgzqoSlayS8FcYRlEtJMIo224McbEQza1YUsXnraGXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyOtLkbi9uaduzWUmYPS5O816MVWUsNlnmyAbi-9wlPHSAAyBuoQV7tzk9Hw2ug0vkO_ViUwp22zpGMQ22lQhmvvD32qdXjwTKnVtWZCyugULkAlOwpejhfXjYMXYNgTrf9MaD40m0yrZOMzvPhrM_ivllwxXF9cRA86BnWbmsvFEm6W6GTtxtINeCjJgmcII69pfiNpIcnGzTfegVynITuI2m2_aB2BVeECiBMNQC7Z-6G2BNIgPqvNIc78CBT3gzkOi92vLeNtpRtktOfQxfZDXMsa7jQICxhPSBLp37Nn3icG8HAzO55xwVWG_ZBL3UhHXzOeXJE1ccTxaeX01A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLNkBlX0DRvKFzNLwWCKqoAPzKT5aMIhjcAzn8Jgp59WbRDGnp8S96Okc1fETFqE781An-0DXzuln5925T0dMA1HLHNqa1FZJPpei13dkk7t6Ra-Q70RZ9BrgMXOH6gVbi2LJRu4rCGr53XW5T_N82tupTOT7Z1vqQeTjpXS1mMVMFGbo38T48VF9sbuNxpJEWVb-8M3AaXpAUrwsypgQ8t1yJ9UU1YLol5wQ1xlfy2uMdu6mT2jx177uH1j8lnZ2OfbZRF-J3uCu8eFGjQTtX76G36RRzcrocXawr8pqkUgxt-w8la9ikRIPDkfIx03Yb3qEx7f73cdtTNnT54mMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ME_asliKk7RfUD7yU9gGKCE8JVkN-B6J_seqUW6ZvPh5_Eer8bg0lQgHL50bhOdYPpBGZwRYRMepWE8AvUK3bAhrAlqObbhlFY2dCiZ31dvS9b7VCVoMgQoNPTobXhFYlVLYUd4j_gb1wdkCTWg_DrgH1IfNcYfLEwvzHe8hcYR-Wm6XOvrNx4UJ1orJZCk0xo2mvAInG812GXnQQOzLmHnftgO-2a0ujGrRjcTMNzO1qgBZ2fe5c8wwzX5xdlNEjZPrx6UXE3FGS2GoDM7opxTFmD1xYLwpsqX5R9SFbrVrTxKvl9Om8ZKfh8IdTIqRLemMBHNvnFhVL0Az1jAzQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuyyvvlpbEZ_FBkn8WEeDVm09Zy08ngkVblYkMo-LiGaMlfBXiZ5gRal3PmecosvXiy5izdeNtoadYgqsFzqh7m_b8eaHQflMPJlN-Fpc2WL4WmMTM8T7QrqVmp6slm3y2N2mD0HGWgkO7RoUNwLNawdqt-Rko8-cDQvogSmnvaNXoqMFoAF-KME5VOyiIiFhIcIDhRS0LuLXlEDvBI5TM3gq1jfjY2x6xUtI9BSr8_8EtMFHYMvjQFo5erfn9AQuYjjM4DuWCvF7tO2b5yoo8pAs7SRaEe4S6EwpifNSqYsFAXv4WlZjMMWfA-6g19f-0nQT7n5h2-YMeUzZAE1Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ry9JwRVPEZ-QyYpVX5sX_qFmK-7CmwSAbzUCp1gzxEI-0IJbB7IDvW5Eq-2F_0_GrikceW1sWW-rTI3gDxjo9SnK2rm6PJEuwIvycJOzIt1PyvKxJ-3zSlDOiWax9wAuXvpic-jIR7MEkHgZ5D7oHP2f7b_rqDjNTOXYmX_Bfau_CYdaS84fF3iXga386VC-9xGBcjJWNb9IHryzgxeK0c-xKrZjZIVBHzxE5mI1F09DdNBqkrDK39Oz66kR3CS2Br-OK7z91yZKeg5RoAkKr8Yl54T4am7_luMMmwk6FM_dfi7AhfcR9a3a4KgTQERsoYBPPdhOPXAjmza4HkDvYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ootsj0oS-k677f5OCxWAa52nEd1dN_tdvLcBSkFY3J-eBhg38PeE610aC4u42le_5FpIAz8oS5hz-gdxaSuZXq7-0GXusyQbYYVeC8vGYqtdzkuGvZH1tOE_bzQTE0Bia6CSWYM_fowv6EyRvrLECCSykhHPhGwp3q7D_91LcelUg4cNGSldIAX4f7N2yrfARloH27WwnQ51hgHEGl_TMtxzy8NBg3REyrLbBvZs8UbULkjjLYXqe5PL2FrUwwBhVkrLnpbXr_FMpKd-lqDQqvmCznu6Wt2Q3OD8F6-2QB_rbXOjKs28Avmsr-CXdu-ToDOGYmD7qhhIcI3Oe5Dp1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJ9YV9OewpkKFRTKjioae6t_SgToJ_dwPLrfTbfwux6-obLU2q81Jr6vp7huOIkDBdcHD52yUSP6m64YSR6mUju7Ic46GkX9vG_cy1KdnvIINYIhqkYL5JgdzkTn1fbCQXiift3_gO_GkKeYQD5UOLv0Z2QAD5-GX3dSt57PAkZcMiLqn39XVNfAg2bKnKkawduOwwFOWvALzBFf3iAmg6Dr6rq0yVlk1HPI6uhrLEMD3UuPGFGDOzCtIPrIUPJVOG5nT5kqbIUHHr1t5SX9Lz2tSfQjYI-ERYlrS3SLLByQQoxupI7Fm7wRKZ7kw00OReSyiR-C8l2PNFrxqNMjqA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=bu__RCyc3c1fuYkkVLS4LDMlyPlRWACZEOdPQaHsgfHCiW66mM5BAX3bFn_5csSlJl5oq3XSKMt9u11ZGdq4nUKYeQhpwudogQCqla5ZISxAyfO9CEwe2iTR8rVdoc7RTjoZ9Zyrq9B0C3yT8zTBNy0Z-pXaPYmqdEy4LxBr-X_bafMMsNnsmnHWxx6rtnkK5m5s3ChhUKnetp78ooDQgJrsHAUjEhAqwVrjg4Rv4RVs0dFQhCPsb6GFq5V3qTJZxGUrDb9Mpf3TpuEMWffqRH7tTbcLWxyPtxulPjzaZXgW7XFxkPFfKeS54QDJToAOokIgS5lVlb-R7v0NTpJ-8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=bu__RCyc3c1fuYkkVLS4LDMlyPlRWACZEOdPQaHsgfHCiW66mM5BAX3bFn_5csSlJl5oq3XSKMt9u11ZGdq4nUKYeQhpwudogQCqla5ZISxAyfO9CEwe2iTR8rVdoc7RTjoZ9Zyrq9B0C3yT8zTBNy0Z-pXaPYmqdEy4LxBr-X_bafMMsNnsmnHWxx6rtnkK5m5s3ChhUKnetp78ooDQgJrsHAUjEhAqwVrjg4Rv4RVs0dFQhCPsb6GFq5V3qTJZxGUrDb9Mpf3TpuEMWffqRH7tTbcLWxyPtxulPjzaZXgW7XFxkPFfKeS54QDJToAOokIgS5lVlb-R7v0NTpJ-8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPrDVat4J4AMoYot2VZJ9qcSG_wAyK_0GAz33GIaEfQuPQn8ZNEcgxm8fNb_3VImqZAWXZOyY-j3ImI_I_bHqoFNBNwwFpSKy60F8d4Fzd6vuGjEn9J2z_8kP0QMWVtUNIMYcyU66uIo0rMuYdueFstVEyoGFhd2-GDBcs0Zq3SXbOFrj9NqdNkiAOPpjp3psmibNB_tIhvdhgJ5ocnBPSYoo_gMxfdEZZHbUlc45n06mwHaFXgP8VU7fj2f5uQkGmOkQEcIch55R3eD2O81SYcbyQ_mL563lcUbFqyX0TSzNl1iRNk0WRd-5iUevV7s0uwd_PklYIslO_pKvu3jHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
