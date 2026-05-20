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
<img src="https://cdn4.telesco.pe/file/D6VfaKvZWakrQtR8I5XWjl5jUbfrBFJnSsBM5Ubs2ZSc-wECV5nJX7LMPZYvmlSS_CBq5MnSAwvzaVWA6Cem7tzvSNKt9IunllwgAZmEVP7qoYqhpHHrODauVbNFjnaZivgCL6T3rAziZsBhP9InQr8tmNY_xZi_bT3SHi7UIQByO4dFa29Nf2Jgnb-H3xREMeSgUtDhbZBKX4_Aaw3-Qz3Nk_68Fyntp8c_eGmXWtbpEemEub4REC9dGpVKYhMktNh2uzTPIAbMxaD7kpDEYJ16xOZhUSd2kEx0aTOw-dKHP-gGpYJ2lYZuR9ebMLVLQRwm7B-oMegqmq9CQ3lJiw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 204K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 11:50:57</div>
<hr>

<div class="tg-post" id="msg-22195">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pwqx5rh0Ongyjaa_IrDuVrgcGoKx_Dki9WXI1OnoV_jwVX76LEPbv8afKzeqdsGhlTQ1oeDKq7j5YpPkKWAV8kUu8O5KzqKJImxb-OJedd8MKubWYj4vFcnaVfhwBwEjCymxM7cPEfkf20G_JJJbNOocYWcq6OO244Y4uwU_l9EEw-Yfjp061-yRveiqu238i1cOUuGv6rX5PgrrNDdL7COdg61w4nKOezgmQBJn8AMMr0TOOYaplBqcFoX9zU2dWcjTq46wHz7M5JImKniHZI_h5rKmA63ldAznEHJKEjn7AcP2fPvAXM1VGmc1QYAwJEZ4bveYGmBzgv37-gIHjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک‌ترکیب‌احتمالی و پرستاره تیم ملی برزیل در رقابت های پیش رو جام جهانی 2026 آمریکا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 820 · <a href="https://t.me/persiana_Soccer/22195" target="_blank">📅 11:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22194">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZuOYyx_uNxkqSImfVZzEzQEssr8M2bgz3C8Z9PrClRpGzudHSOyBOTgfdgPV4_kY4d5ofqMRIV_obSEZDhu6ua-XhBruxpXcnoo9mB1XlZ2Mc23nDiNeo0lYou_g8g-_sylE91xqUlZLJxLCwbAN_OWQltmIVTYuqZPusLaJ2exxePX3-Ss2Lf69frlCl0L5YQwbpWdH-22Iv68cg2aK0jVJozE5liG7BpW_hkFpu8h4ktEQXR-Ei-frWYrKm9uMIKqQYAEwubpr_YaFAOLv5Cz4qUqQxGtvkKMyIvHTN9zdwdgx_0K2v5tZn9wTaY_LVUNOHhfBuTccVKp2XPCRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/persiana_Soccer/22194" target="_blank">📅 11:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22193">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_pLfTPtv7hX0PVo4PP0E5l-het7O5Y_uyUCAE_Tm5Bopf2uadgqEMrYCQ-GBcp-dlv2C57JBrPKAz6q2JfELD7nFq1cz7yef6oHFx_X_2HJxhpWlXf3d8q65hJkx3u0bcHWgevsMsqVjlAYrEfy6INsem1n78-OCtvQyA3W3BnC-9scZZPd7Vcw0p7iQUa3YgBx_cw0y-4keoX8oI7VHFt9h2-srfO0k_sq8MGF1Db2hGwgRcEJwxE0X9c8WQmWUqTnfJec1aWOrRmoC-M5EeBEC9OLfmp1dDyAWQafTam6jFXLtJxx-p__YIiLyqTsJf9AxEtTRY8TItFZ4CNCFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/persiana_Soccer/22193" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22191">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tdtxRLVFMpp2LgI1210AbRrOQx5ds2nrLne__PyOjheXSZ0JmpkCAuc-jfflwz1rjw7XdIKxgP2aJgqFfgSVQimNxVjwWgPeXkZ4KVw1f-JINMhxMwgRGU6bMIyMWnZPx4brMBplCox0hTN1axjkI2Xa2okEZDWcrW9U317KDXVv8oXwmv7HRWeaNJPUzP82X1rs643QLD27EEnQj_sLSAJhq8cYksULlNGMnKNqSO5dTz0SBlN_y-d4MbCpTVD6ejj7kL5ol5ldRhxPPIvU0Y_hK5MFRVXxfnlpceDEmY5W5_mNblh-UIigVmohsPpIGO_YX9KPG__qOk0DKQiUIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hIaJuF4sdJkVUO1yoieUQmnVkE-yCYbJAjQZVgshYLmT3Jiy32VJS1dgB2G2YeO88CZdT4zsof6xYq5IyZwyxtcWVN7X87uZeSZstNi5TtWyVHvCaekW0DXEOZf4_mgMeafd6-wsVh-dKFWP6Bf8S_G2gqzzAKWmw8aRrN8BYHZFbnuJqiFILiyh9389dzt-rLjrAss-GfahMON2gBRQNrWd2J5N1FQ9DSM8Kzj5b_7uLsQ3ejnXWEB5V2kxBy9NExRaohd_Oka6AydJs-2jxFj46cOgDbeu-XVeLsaxy7azIvirhpQeCCf3uJP1RwOncO3VYsqjZucnaJxTzYnwSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند.  با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/persiana_Soccer/22191" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22190">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Me0Tkz5ooEnqVKZFCA-p5NVfKiU1w-rReJnKeJ_d5Bc3HsguUZlryRCaQwbExBCztSiMvPkuAWrQDuKTDIOd4y5rksxQegY0gFCetCFVTp9NSWpPXr_bjFNlNNi_szAk1pdwVjS5WDzGGcze5NnSwAVYd8TBWBhi5BBVDoenfzmQ5UW5HAj2o2eK0eulv2HxQ21i36-bfb08lWKowTBUk9RTCrUMyrSzqrKn7Rf1-6qgvNdM-cm8uyn6gLACby5F8Ew5xbL3SUKPfq2l1VRgnyextKiqYBqC_KY32rp_fzKeqRqIJnCAYyK-nVh65LwdnwTBjeLDk6l3BRpiDfWJSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند
.
با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/persiana_Soccer/22190" target="_blank">📅 00:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
متفاوت نه اما همچنان‌چشم‌نواز؛ رونمایی از کیت فصل بعد اینترمیلان: لباسی در قامت فاتح اسکودتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/persiana_Soccer/22189" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jX8DSqAdPe_rgnFPZOptpPkFATzNyFcmTPCj9vh4dHUMQvId7qm6AhurLeT2G-d4dIq5WY6bmBGX6j8TpmMUVNv2wV6J6zBsraMh3AO2KC2dcMENAg8kdXBERJTWNCdkjsiVa0IQjjm-85tm5qCh1LiTh0DqpXLDLT7hBqaK2nZIY-cGhbccJs4iA9ZRgTb_b0zJ-QeccQxSXAGDypn3RAhrIwMdGaseJCvWBP9gZv5mo3AjGf_KiOYUWQYOZ9UOedIThh973zCmVkQu-BLAQfD7CZicA2crB7rYBug1T_84XZtGWDTN-3ZPR3NWjqeGlU23xT8LR40oPpKBEYjhjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/persiana_Soccer/22188" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgZisqJ2pnWt6MfB2I1egbUCfSdxNrjNwedphHiZNg4kHewOnbp44ZNR7n0WUCS6pXCL3Nit2cP0ZriGulpaB-BMWbv3hNNBNRXXR_YGVC4Ky8_HwhXXsROlWZvyLffFAZp3Uq4ipmg3r_7_A20OwhJp7DFsMb2D3OM515pgSIyK3bjm6HhFLG124e-HDLglJmX4XcWt407OAYmmFFmqcDrNJem7ThW7pge24MAVptRnwIXKwyHfZClK0SG1-0FqU8UU7pgp-i6bDOqqAnRQmWEwNphhZS9iF6CW5kJ2WXB81monjqpUeL95FJ9zZBjuFV_vAuNP_27WKrZ_0MpeRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا
؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/persiana_Soccer/22186" target="_blank">📅 16:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr6Zc717NnwcyPc9GbUKf7oATjOFZyxX_VYhwdm_hVCCF745v6Zp23BGXJY949_o6hqHdp5X1Mk2w9vf2mTdlsqc0EIz5xLCLhf-sPl2YvGk1T4Ya7fHmmn5DofBUlW3HSxtjzGETMZdxV0jZvDDDXgN_01jU9yHgSdreOeVf3o2UE1oExHJL1HguPk3xNE7XOJty5kRfqiU4eyB3We05MkqQiZ7Y1EvUVkaccIJ9ybnGj4ZWaJmxd8HreppsSRxu5NIHJg16D4ds_qRMCtIHXZqLWBFyQ_H30McB9SDm9bfiGA3_N_yuTDuR-c7k0oz60Yr-tDM1-S1qAp4mOAb7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGGTRfG-IIRXU4gy88H5Wbr-rWSSUHHcG9kP6Rl8pp1MNHyNIhX45rlJ5_Y0LXBAfbs-0h43C27qZRLavvmyso-apwtgKXoAVdEERZI6fs_tD9kwZW6-yFtFBWFN4mZkc3C7-_2_qzgRrQzSxCbRIEScwewlYsTHvNYRGLyCnNlwM4N0_qR5dqky0hfg4DvKx2CxT3gaoP7mWNIk4WPJrB8Pp5ShY5JkQyBx5NVjV8Dv0Y7SlupU7Uvv8eIvKnxwAKnsB11I2Vu5gYwE0SQZp6B3VJDlJsrTX9j4lMtBSyW8V_7sdWtFpZpFYNSam567iEsiBv_1M8l6pN9Pnfi8PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/persiana_Soccer/22184" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22183">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7621338636.mp4?token=SMSgThEq20KoBrzp8Suut3uYEP-LUQism5ePmrtiJWyHXr9zWU76iLHwcpYInkXk3JDPNcZIJ-ZnLb1T4-3gZMsrZeYtjg0EOKvYTcoPRXZLYJ38lkb_g-pm9VdCVmcQayimT5-pU_TMElwSN_tpSYvvi86Atcca-o-cp_PUnBY1wFmFuRmJKQZpQYX7xNXXP1IU7EWgK96XzIQBqSo7Gg-KwL7qk95dxeB7QrzjN-71htvWEBvCXIOLlNu3nIzXJSZ_40t-ePUdsNzZ26EoOEw8XMd1Z3h1d78B91LendgydjpId9i_w9rTYH_nPqz6hag5MNM6YmAj8EZEWx0_3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7621338636.mp4?token=SMSgThEq20KoBrzp8Suut3uYEP-LUQism5ePmrtiJWyHXr9zWU76iLHwcpYInkXk3JDPNcZIJ-ZnLb1T4-3gZMsrZeYtjg0EOKvYTcoPRXZLYJ38lkb_g-pm9VdCVmcQayimT5-pU_TMElwSN_tpSYvvi86Atcca-o-cp_PUnBY1wFmFuRmJKQZpQYX7xNXXP1IU7EWgK96XzIQBqSo7Gg-KwL7qk95dxeB7QrzjN-71htvWEBvCXIOLlNu3nIzXJSZ_40t-ePUdsNzZ26EoOEw8XMd1Z3h1d78B91LendgydjpId9i_w9rTYH_nPqz6hag5MNM6YmAj8EZEWx0_3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22183" target="_blank">📅 11:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuoFetV71KluTeoswC1gAqnqBoG0558HjBOkLrEQaBFwBs1BvTTiNjjkvAihZyZiUxR5YiDBexVeBf-JkJwDvtD2PSpvEJYCC8Dv-xz4cIm0KsKx2dHgPF5R718465leRUL52IZwRV5wK1qSeN987wrJGaoaucA72WuPYmZ4oYfJpF4MWnOQSKonTSBf9vByHHonpY4hutozQRvhE5-PycZiRAswVqWEv-1utwhTGqhp-JY9ReUDDMCeRvQ1s27Z9p6LMZfKbpirA8SuziPQySpHo3MvqKfFPgYw0v_pLLAXdCm4rdjfUfpCq9mpq9yknBtifaFO7nUjky6c7iHweQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ پپ گواردیولا سرمربی سیتیزن‌ها در پایان فصل ازمنچسترسیتی جدا خواهدشد و انزو مارسکا دستیار سابق او در من سیتی جانشینش خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22182" target="_blank">📅 10:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJdltt_4g1ii4pqVrC7O4Zwy3K5nUFZQO0Dr8l9Ju0b3o30_6-Ljc97rwylZ6BsOGucUQl5taMMmVca8Fpml0M8ubF5dh2RINTuYk_HJ7Epd2oD9cUOMUV7B9Ybjq4QKj1OCaUAjFxPF28HtRf4dXMKCVLwd4N2lhcDHfxQ0hG5AFTEIvWhHSjY7tM7H-a8UCICn_IXNNUQqE7YmH8ktzcAph5RZSB7KUL7A1blSRb5sGH68o4LF5nvkER7LHmfXBWZL2WxEbHPFlJFKvnN6DJ_v3eXecaJLqQs2B74CaDFrLKD3TIyiEbmxbKVEE6Nx5mG75cbX-TrU3is8HsQQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJ4WmTDtq_LXhgtjXy1IFKRgzdQRcdlYn_bbMS_S-EBKEpOI3tMMBZyPcDM3T8K3-XtELdvtDgrDhREB5cr9ncvYuRnrC1209pioHxn6SGTIetLM4NZWbefbU_458BcecpBLVkezshbOwDNFzEsW5wI4Ff8U-mt6WGowJshLLNZqLbzUfC28d3-5SrfvUeAp960LdJazKAj83vAA2uaEqAXwOQE_NF7JM9joNvhT6pP0sxEakzslzNDCQ48yHHJywy2C6YUsJ-l1OnQ9LbgyzOT8Goy3kV5qPU1ee1JuiDao3Pao89LKDUj2A2JHLK8dxH3xywNzePu29vQFFx7E6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22180" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfJEWFFqT1NWUJhZqD142UK2H8LkNoMmQTEmP99cjfiNktQPZexOc9DG3v01lktlbkPdYV2XGADdaUlaKog97RWXXbnfo4YdpqMTGNNTn9B0TUTHaPrSMSas4LZH1oeygsnUC9sQoPVIqHe8L3R6UW3Rg7qL_vXjwtuwAXwQHrn5SI7Z88sKXVJi3K_oDz4V3r4nCKRz0PxXU5qNV5h19O2jUI9dSNvIvRPXFM9QOZNCPwtrYKFW5rxfc4qDWkxiRB7yuK3T9j5yV6DcnWK2GxKQgn7NGd1s4lE_SihRYciQkYHq7ifPzpjqD2rhdCFE-PfMgEMVU842999-G7gCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه جذاب افتخارات پپ گواردیولا و ژوزه مورینیو همراه با هزینه های هنگفت این دو سرمربی محبوب در پنجره های نقل و انتقالاتی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22179" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22178">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I37bbwMQGWs_8PHy-ih6i4ItCZnZugJxK0JefEGioUPtopFUn_SZDRRdSRNrd0j7UuvqkrfUKzA-QkMAnYS83eZvGmibF5sBztx6d3AwMIGdHj86fWMR4SV7po_BmGb2eQdKc5vnFIuAfP-7EdgsEOSQAzTCxo3cRBigq009NQGvjW80dRxSlD7_oPWDfvJY_83q9MEoUuNfzeFkLkRrD3RbSq9zcI_AzKAJr34T1VfwCwIiqaDcrOdehkvFfcYKKzVfuvyeOgLCqQ5zZuFc1Wrh04DS6SxO5ySPAxo0CbyPGYCc2a92S_3X6YE50eiyPhcq6cwRAsd2E6VWI2IWWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22178" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22175">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P5HATnomEAI4jlW-sixKvX585aXSFSLYL8-dsj1DdbncDRyNFATpp6BJPGwviUDRzZq33S2GlXLnnxUjs1ZphOONs8ZYcT-lmI7WXrS3Je5-FNUwrUL1hQd6jDjv10_R_xVgZ9-RjmwZm5oGbkxniMitjS82vwoIY12pVn0ZvkDux86x9y9GaelVrGR7o-KB7j7wgVBIoUXKCWsKtCDh6chF-wRlJQ-19oWPh5aEDpCbpuqLhJKPnClnF-rcK24vsBjUePewKtaQPY3wUFa5hPJI6i3lBZqCsuBLRaSarYNYShGInIwo5npGWVwvpk7Nbu1sB4xlYC3A5jd5B2jr2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jrGPAeS8mqIweQD29brmOd-a8dy50NXHvXAZADPvLeBQL0Qhis4GO5fCVI3uls_X2I856s4zWS-z0plWvlp6L-8Z8AF0DQ2pQjem3-0mIQO9qPK0hOCuBCIcp1kk1yp7MFarnV55EIFXRMzji6pzcf5fAhyrxRw4ulwpJ_qrSmRNApuJ3L8MzaGgf-FKb30YQAHE94Oxle6O36pKjNY3_9iVGD5T-yNiHHvM5l1ZrHdDuu7z9L3H0ZZvpu3ZOhL5SH0xMJ_1cNOGSifNUMb4_fHpgTnZ-rmxesUxzupxp8rSbOodJs94BFNHJ1S9cOSN7r8BM1Rm9rN7XizBUyW2ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مهدی قایدی ستاره 27 ساله ایرانی سابق باشگاه استقلال در کنار پسرش میلان قایدی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APu0jznb1uE2XQ70wFhB9_tpK3wGv8402n7zZ3cZ16E1kiWnd0J5GRfXNXMukCi8edXeVnlpnBPY8npydPtfEpMwXZJkhUrg1VJSuCP8zRyo838hn-bx_pF8NOTAd2rYC5VO2E8VgkzLoLSFnzEiHL5Cu75hLYM9e2J7YhwkHIAeHaCWgtWmdGnwmhA8QUUQEuW6RYa8Xs_8CV4CGmvRTIxXBrV5t_8qXBs3aTkk0uaTryS-ebEkPFgV7WZBkS7pnUcDu5-2sW1b7a5qKdZENrsw4eLhHwE1dBwMGO6US3xLTFyw50is3lVjdLqqyiDw2QGhunewf43hwp7USF_tjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P94PeU1qGruHVQxHPaTXhsYluX7IdOQ23WrCM11DbzrS1lihReCEftKCrUQDnMuWbihpHiVNJeyPe_Q-bA5yCZnLxK8gd5hDQyIXoa57wkZ17ZMFRsHkzjG6jjxyesR1nogUNJsyWLJBOxcpv_1hWEtXKLQUv3jNhY017VLVSbuMa21ery2AcxHRvn4_AtZp_7k4NEQCZmleBoR9TwBwx3MbmfYbmQqV80fO_gYvLKncNun1g7YH70ZHOm7kyIm3m7tzvVql5hos9o2TGFJJJj1lS-58_a8NTotjSvyuYG3AXbaC8BczfMDk5EDiZU_W06LHBUKXCZkF6_Vs_lmx-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gW_J3shx1BI2Qkr8nBdEPCIw2arWd5F0n7T1IzDW2PTf3jsinI_Ysz3rNMVurUfuKE6AnSwaSajxK-m5nW-3qHRiTKu2KtUNmqhuNvRJEbUO7135IH90r71OrWEl_AS1jViPJYahXdVetNuhBRSNvkCq6WS4oHeoZYAcVQUP6Suh98luU3Jk7VyROzMoKtRU8BG3qJXI-TlsT86ErDnwkizOSCssnnd-ORBmC-9yF7N42SG7BHTxxpVqbhoSG2QSQ-tKwnyLDBJ8jGztjI9vjG-fQ17rjFc0j2fPK_iOpXX4lOvA2q0KdoO5o7-RCIGBN50C6RX1dn-rLuJRF_Vsuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841076b140.mp4?token=b16MUzo6bKPUtR7niBo6eooKv93Uu7Ws8X5KSNawUCL7XERNkU_ek0VBVRdBXtsH-3ZQMksNiZrq5nOSiAjuUA2eVFrgoe87NJ-vsslHD3IOai5jvLX9eXfrUm2bZFyYfYO6ozGphqNeYbDyGK1drqZSVZ53pZNiJWj4AUslPhnXc2T1K9XkQOyoXM73tAFr3SXJBgSSe3mPQJPlEudC4eCQewkKc_x5tt8cuAweaXSmGEeJHgW308Lgrz6bZgcpGv3q1LZStdRL5utmDsW28o5QaG-EZxjj2YY-Ru5rK3NbB1l8DCIt5hEWTBYJ5unokQd2dKOaF7DUQUnNy-9R1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841076b140.mp4?token=b16MUzo6bKPUtR7niBo6eooKv93Uu7Ws8X5KSNawUCL7XERNkU_ek0VBVRdBXtsH-3ZQMksNiZrq5nOSiAjuUA2eVFrgoe87NJ-vsslHD3IOai5jvLX9eXfrUm2bZFyYfYO6ozGphqNeYbDyGK1drqZSVZ53pZNiJWj4AUslPhnXc2T1K9XkQOyoXM73tAFr3SXJBgSSe3mPQJPlEudC4eCQewkKc_x5tt8cuAweaXSmGEeJHgW308Lgrz6bZgcpGv3q1LZStdRL5utmDsW28o5QaG-EZxjj2YY-Ru5rK3NbB1l8DCIt5hEWTBYJ5unokQd2dKOaF7DUQUnNy-9R1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تقویم
؛ 13سال‌قبل‌درچنین‌روزی
؛ دیوید بکام آخرین بازی دوران حرفه‌ای خود را با پیراهن پاری‌سن‌ژرمن انجام داد و از مستطیل سبز خداحافظی کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=op1IQJQ3VCCXL42mIeRr986314TdZYtI69EyhrDbBhCWRD68T46rwA0_kwJ1Hkjf5GvS8x85e7knAmjv8Wb03oJahVDEjVGyLrrP0GXrZjzK0gbrn22VsSIvxqMGTvw1X6FP8I3RrDo3axZfgSHZ4ziYy4irqgPaxeughpFIEWdZEwoGtaxZ1RQ9WUQmyqJ5PueNa4kmYhXOfw80bDJCr0MANYi0Pg4-aKwnrk7-wn6ZLdfMS7blmIA99tsEc2SdaGmQR8moVjncH8VvGZkQKN01Q_vTTTfz8KZ_4RPDd06VKV6g3HTmJAZGBwa6kmEZuZY0BJd48ItZpI_Sj0dUew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=op1IQJQ3VCCXL42mIeRr986314TdZYtI69EyhrDbBhCWRD68T46rwA0_kwJ1Hkjf5GvS8x85e7knAmjv8Wb03oJahVDEjVGyLrrP0GXrZjzK0gbrn22VsSIvxqMGTvw1X6FP8I3RrDo3axZfgSHZ4ziYy4irqgPaxeughpFIEWdZEwoGtaxZ1RQ9WUQmyqJ5PueNa4kmYhXOfw80bDJCr0MANYi0Pg4-aKwnrk7-wn6ZLdfMS7blmIA99tsEc2SdaGmQR8moVjncH8VvGZkQKN01Q_vTTTfz8KZ_4RPDd06VKV6g3HTmJAZGBwa6kmEZuZY0BJd48ItZpI_Sj0dUew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
لئو مسی آرژانتینی در صدر بازیکنان با بیشترین تعداد بازی درادوار رقابت‌های جام جهانی در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkncisrkXq0m-g3lZwAu4RYjDHhD_tz9g6A2nUEBLOoxEKIvF47ZKouR9JACGYsAIhJkydzqumstKtQvv9Xjj_x7iSVMYDj8OKCjuJ-EVyvnQOORVvnx2StuxxXJtVLhrdDzuL7PhvoKH7vGTgb0IL9bA7w0RUgv_COiPJPETNmLJOfZj595MgQ7gEs1nG9REOERBZUQLnDc-X6J80N_wzNg7F7vfNmmJbeyoJ-nlYGhcwv0Ldhn2XozTxv3invNkQNT-QgZgoHz40eU4P1iI7jKunurfI7eFbJJq-v8-jdgOiQ0kZvBH5o33HxIj8V_HTi-kpcDW4wvMC13YLCfIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGycueqpG0OZwNFteoQVcfEr4XqFn4jQ0RN3xU1X1S6cq0jpA2-P5_0-cyv6Du3fKM33cW4C1iymIMGBk7HECvWR7mHkJ6E0wK9LuPSTedvtYc0Ob6ixRWnt7Sv2N2dj1-OQJQAnF7Ze0uNp0MfCcPyAepHRrfSUsKRYYmArHRxSkqz4sJhnrYI0O3aypB1D2e1NrjuolFSelcW-9SEARdNHbLUx92uMMWvbxlo0bHXQAlwpPYxc66rbiy0Vz5sJVTaCfk8PIKdiCSy6mrA5BNPKDwHhotNuyKDCzCOuhEppacjMEP5RAnYwTbygTaU3PhRh-Od2UfzfLqVy4A5X_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7I4KZjVFjGHVSHf8iJFkOuizyfBDKdXg80s7uyW4BQyChUrdC6I2CDoi8ncsLuLikJKb0o4iQ-AlPI9ZN7SkDGhtNhk6aGbkDvJk5LV_z7zpEv8hYdUWuoYtZlE9cinMkTye5qYekihU-SsBGvtxtu9nAW7xMyYN0fTiOEmb8p1Fwe1p-JsaEpbdUGSmhShKLQXoyaJc11EocKChaEFgPEwwgTs-imBTYpCcvG9xcGJXAcUPFlenKNE3QBkXyqq1d2DiuXkd-zyY3c2fMUQEJEZH6TQqDZXRJTs8-VELJTJWZU72HV3TuYgYVmMMCuFrghp809Bn-ynPyupA0u9xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWAXPhty-6MZDplhsOLADYr_ZkBlb6yXlt3hfJazuzNNl-xk1OoDPwA0xRNJEjfXJ7Ex8FdNpYc3xb84M74Daw9Qv_FfTI3eaJOTK8BxiZr09049QpkKxVNCjh_668mxLYkkNCP2-iYgl0HGgX8M4vaSjVBlu5Sc7-HTc_okEkUoKorMvPJftQ6xkLisZLsPYvLwdVbL_d47ujd_9_pLJuYMpUi23CNo94z8GyJORRDD83tL0kPtomLAPFpjv-eF-M9soUc-nGDvs0UM9L_MWvw1j0BAQh2PMThCwQ5XMKq3OH5NOIW2IaNCq7THVa6FgkEaRYgqQEMzaBNUFlY2Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkD634oYO4C_gZ9idFymE8_DeBpJewmRU4pNewixOzHnTsdTmOp1vnHeE9uaJltWvwDhTc3u4KdnwO_tVHdDP-eXkZqJFVsJPfNx-VH_LCHqsenDEJpslU8ABiPJ1pwMK0ZhzRp5Jb15naLqaXfhGq_n2xZcUQWo6DtNn33g5JChL6bcXetOh6DEodUOyx1r6yI0Snb9xv_uHIldnT-9cBCdwNlxH7BMMNQVtVZgPjoKMzLYpEOx0pSDs8Inx8OqVT1UknC30vJwV78J1Qi_N5BZON8Et8pJeVtc6_Hdh-YQeOlwdnEqyl9t4n_4d0lSAFpMyPILXAlND2jb1VCK6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqVsIgYik08XkrzqqXLxTHWNVSEtz9tdsW1JblDIP7xf9taVvcms0aafvWnguOf27XTMGZKvER-XLO6TftgBhfVATo9erNHTaekh_NUvADa7mgisSuPJCaa1ORMQBnR3hFH11meJUhUI_iml3IDo-GEK0z1-W908qCCRahj95-4QLFjJbt4dwsfO1pHkyLGhKsnhL8JRzfta77dKT_BJYrWg4EMc0unBSLN2yB-Ca5DNihnU-5MUC2kHQ66LQTS2Mnm6ijTJf4qcEN1r1Jjt2n17kPysWJ3t4PN7UfURiot4xFyP5FV5uoTVQy__chHuUMU0KU3bS9EL8xmwaz8UpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvKCi047Im8NaUENAS17RLfaE8m32aoE2CgLmDIqaOhkJqUXfHDWMDEy-_al0T7ab2Yga88erQbSHLwRzks4ZF4Lz_l3EtIF03hq-ehkf7mBXMOGlFgjbXiC4z5-6FMOOywO0c4OwbMjChjZu2uBhKxsMDiNftMF8bR3ylwHDxE81BsWMw69eP2bPPOFpYxFA77_Jtswq4HQ-mzuQ0OsZNl58x_1AcNT-UzBItztVG5nqu-1EFMTyrVY66mcoDVrJdVoKA8pghFcWBXzS0JO_30jeOfh3-VWUSboqGmBloVOIhZqD5ab7bgORemEnzaI238SQe6C_jvjTg9DtNOMNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2H7Yhb838yFBykWSAB3xfC-o-_1wjA9r8aFWCtTXDOrISkx_OAFRgOLLyJ7FFKqndJahcHwLZOPRXkK1DGrXrRqzMLymopXbx2AsGBBMOzhU2Qep2z5PpflheYvMHY68rXRmTE9OES2g9Xnf_7AKV6VkH_XZJ6mTKwYZLb8vHLqSD2uNAGY7Be8RdtqsCK64drn_F7VI_Eqk5tYHg0cfsIz_WufbBLXC5SGSKJ1rPao5q_nPUWo7Bfq9vmC6k13EYu7tBaST-P2JIJGRXapAPkn2xtVVteePwZfTG5KT10TVGEsYETsMmbMUlmyiN4XpwWo8uPqCbB32gkTRO-hGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhMKGUQNtqXJt36PJOip8QDTdwbEFjmelznDA2pg6CzQW1MREslViKXZNfvuYSunwt7liDzLVHNG5KnRh3bJ5p263BlT5rPZUKpoJ16e4lpiEmh5L4lAwB9gAf8dRYUOPDdftaxA5yd-tcp8C7p12JOg17FfSmsUyJujhQQpPjHr3w1_SnoYKCyfcLGzRXcmuJ2Q67C0_lAjPn_fx4ylWP3XdN9ICpWk1xn1QpoJREt_XmwHYr3JI4ZrssK4FWl37sRVK9pFSTx1UZ78qIgbce16dwO0X2lKVr9ilgX1-CpnSr5A_X_mZwTKOMs_EXM-_w0FAT1nkE6wBnBWxtSoRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQKsh5EqwMjcbAs-TBDgADWM9vRvIM32NCsZnFYa56U0SyW9nxxKX9B_fOVK4gfPjyXOIHXyfVGjLcuKcI0_uRglOh5Ise5HHWNiz2G09qdAShmnzyFNpmlpyqg3S3jUe0p-tbFct_Xp0y1lXr6INz3JftLEHT0jBfCUXfYfpgk9Z9PCSHAP-8A96_yYba8xRSLJ49xv8zMCpx6snmueZh6LWzEiwtQ7P5gsYlqSEPJttvOei3ZUjPmfBiUugjkcB39kiWqGWYUoDqCTgCgYAmzKBMUcUs7VKPYQ0tU3Qi-brbhHPDhAucR5yWSK6r7Cc6xM4kHe6EsUVuGZrYPlSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1Ar2zpB2dBsqjhCIGh3f16uT2NrrrVx2HPhzrgIH4tFq3XcxeAhNc5WqAsVbXcHso3YffNNW738XeFjqJOQ3dlLTOd01Me4SBdMgpTkAJbUg9Ceh-sTLArGjBm82tuRmAjPaJndpUHGWK-XVF78Nl6pkEnD3GEuDwbxxx2X1kzq-8p-SdmMRyjUwRi_blr6gs9VfzfQIUSd0CrItRHlxuL58zmZO_Vy3gFD9VB33ijN0k_hllnDJeuNnwX2eWJWEnIJ_lYYzHrKaxFHxPEoxykYVCQHAR0_mzFcB4_I6V9I7i4WPoGtl-6WYiZFCFmecY5Wzk-7r_azoHf3eB-zYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sawxOpXkzviPixwaLqfAPRxLs08o-p2Yl4gsf8xux7xH-8WTdHzpS5GOsOSVq01KcX5qPHIlmCLCoVvzE7irZpZrsNoKax4jZ2G1ZAIMDcupoS6-SgY5YC3XxrqsCcL9DLS0Oe-EZ2T3ZlBgpiF_Ii0ArV7kif1Oayk9U28WdZz3R73DrcUuFPmgHVTbAGtBSMdLq6Y6NxEMJHr3A-gP5jCjT-KJ3QBjtS4MN9HulMuavli6Lycup4x2xIZY2JP_152EVr5h1HA16KCJJ-FO2aj567xumRdV8IwczSAPQlGgALBu7FW_vfQO1IlS9nrtz0ND1O5InnoOebaPaZ_ruQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUvnu_TnVrq2lYGvOc7iLPTvwFxBsVsclYBrv19r1Fs-qJqkQ8_-rUys6uyDDhabY29x4OoONdI7OaoYlU3AHQZXi3ESjdfiW1mxFgW91zBAm4_kxa6-XWqxVjKq_E17iObLz-Mfee8-mePjvPPPGJpSdFpYwdfrXYYa8kRIfuPtwyPlBNh4xDF_jtRQ1tDB6n-th0v-2V4qhN7369gqyMqYU2SlZyCWl6NQVk4YeDIJ282YSYWGLJ4rVo7cILiCI1WeDRiN89gujgwERiogXOUXJpuQEFbFSAFLz9thJHo5Ki3blH_KNjF0b2ht9VcQ_wyYZW_2YgSA_jp4L4bhyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AC6cZWh4gY6cTb2Vk890o0Clqiir_cTpPWzFN4RTLQf8KZWXCCFZDJmk4lvvb42n1BfdxpIdR6WoYKJ3fQdHBMSNWoTolti3qngtXd5vr41XmXuJHbeDHqq1tGFnj2P8OXdNhiL5_hjuf5Bl99pwuHVnLtcC_Dp2NylM6jUFQsr17fHvw7P4qg3hHUuy88wYlDN0S8mcKy1V1AP-_W2RWxHIE7OAUB1IvvIEdv1L1LtAAFpaJ_lPFClQwlmc7axpJsAnlWFkR-R2tOT0nhA0avmmXpv2hO8E94NLXAgNCM3z2mlDRYREb0gHM_BRmP_Hn95W0GQkOCw6NTNmulEYUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIeT5RJzp0t09jCGbUH6XD-1cZksHtO9fqkFatiTmAGNYsSQ1nslhN6sfY7pLLkQH5TOnJI6HNl0mHPkZ5e6beIDEfCKRVszuI1_H8EqBwEEE20KLUWmDdi9asLpTkxzmsC8Ya9QOuisKJi8heIBosTDE_9pDtmfBPWOIGOpUi0d66utlHGHfEGaYUr1qJ-6L0Rk5DNohhzJbgGhkbJzGHzH0TTS0R4FsSbyYK0CXyGxQqor0f7IbS6iRoqwd9XxqY1KmXUqrl2g3_EQ0bbUWvrE_IeLkA2YYRiuLWXLOVu4C_Fnbe3aii31dq36tAnOtk71fNvfkfgIg4wIzgp9Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUdxDNA1K7Nj9uMGcmfuH2_mkdr_L2cOxVeJciOmKbYCZ2YF6_ypqHeMsVo30-tpGNxZMrWIDMwKvTVzifUYyvVeYStqPc-FNQO_1UPRK8aJfB-12VxgOstH10rRU30HZCdjfWt8p8YM-8OOVi3rJHSi8BxhfKjmvP2m-AhcPsZlFRZXwJjbzqxNHFln131nq0tIFHcKqbynVQ2w8uuKEcx-GmycM1BXC-TzMHX9w2Tv9YR8s3-Oqa7acH1FNUwli6lrOJRCdqYbaRYaFsXboGjeTwcyX0hX-avzWsrz9izU96DzAwi_Iflv2jE-sJuptmmIyUu4-ttIhyU6vrNw6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-SV9Tw9K65nEv36ZaA_ov2vQPI8IOGNI1Fz2TSYHdgRObXqHqpBkbT_FT3mqOpaVl6Fqc-GWy6tTcT5cVeyitgNa5xndhEfqUpzZGuM_gbFawDrKatq92IJymA8xFkLyeYcdGrdeNrykB1D6uIn9Cq7uFHUMZbuqA_n89L6dHg7ZsvgKJfCeB3WVdEXEb8ahsOH7yNz0SnFCxta53_HqGvhrHdrNIulYptt1vconWQUIskoLMtIsawTTZSxZup29evQseg2RYeVsRHT1OYzIJK1hXdrIod356yuvP_t-jKtdDzVOy5ktkFfbN0sJSZe34xcREd6Yaa1eZInP3-G8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kv9YlqrJ6iXaMRzjr3f80ere9Yg0e_MT8zvtGZSyFLUM7OKRXbz9I6w_eVwP_qeSIk5Kr6yhHB_koTk1x9kUldE_Shg-mwYZT69TmJYaPhM-ZjzgGBPqblVka4Nr3v8u92Zpr5d2T7S-rRKI8RoWIXLYraGs2thU1neBEPr6fW3NA6FvPO3BFCIr2mqqAjdkzGT5n7j3aYzS2_3jQLQ_A_gWu1OI2f_FRwYAvDUF3oWdPF4Xb8EStaWDULIITjuKn8pzV9G1FlN958UxQ7xhPAL51snEuE75dY7Rd2iH0rfu1uSQJRjr4ae_GeXmmB6JenOetqxtKUwRZq6GbzZi0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quOP6jOxoW1zub7p5BtcWLA2Z7wZLYc__2UbcuZ7WeATGLV0bbtSABOs-oQ3ZaClKGI-fZta8rULY-1Kx5kqzd_m5Jf1E6cBHXcxkOdJIeQHg8z7WO10-VEWOM_lDb0pHUWb21OFK-2VfsF1W3q92B21t9Qoa8-wbDMEk6S5yFEP68uh3dMMiwpDsXW4YXJ6JUY3MViIlDtTxbaCyJWS0Xkq95M_fze96pxTzynyfAgdAD5qqEUwCuVaO2ajAvOan-HPb1ZLysno5srUoTUUzFZWkl4ANDSIKYWyfB9X0219bXzCGm6s-yUaHxk_xUGsTYFk5CQ1FPkpZCWBvNXTWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCrK7HajZhpEAi8qgDpBFIm_6rnxjOTglq0E-bhm9wbCvI7hVQZFveyMYO5rF5eKRTuJK8noP2x-UGH7WM7KPZe2m0oQ0gHceQg7Xbkt6xofUuMGjbqRLVFidmXIBpnAIUzaMsi51s-qvor9_H06vEgMMTgfkf2rWyMwpoWRxH3_WtdQTj164R5YMLtetxD8DzdzIlH2gJLlj3uOk5-hnflUTm7qzDLmE6VfCPfPDPetotTrIiGSRlErl-uneyY6uHXCE9tpUg_DKA2NEpS_-xX1eYabbwU2k7eaod753Lm0WiJhbleGcS1ftVypHgSZhxYSsxuDUFSEDoydb4BIFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1jpi982zKvH9976kQBNbwZYS7iAtp3eOwR7n0Uelg2lBHe4hImR9l6x0m9qGp7AoIzmToFDadPFPJl8AHivqR6ZAKTy4SS3wwO70gGZWcJbMw6unWFXT88QF9Yv7vx778gCF0MJh6HRKtTIFJ6l8kzJkKSnXVuxa8ZBqVubg4aSJP3twHdjFZoryGZm-K6eId5wlWHyJoQkS8KxpjC8ZLYy08ddq-SNtDZjgzCWLrdbv2MvwjXxxZZAxxbnHDME04i-DV825dRQw49kiuUd5Nsx_3-zJPPVTzJugJz1pICroB6XgNZhyHH1U2__8DiAfTVskcW7dtxJAGKDM1T2nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1wL5WZf0c9Z7jDF5AcLOLjpYnOD8KABA0zw9XcVQtNUhndXSXl0Yurj7o4voTADfxisjyCvNqqmxAgunR69FynIpc0fYW9ebJbjJ3jPthAUoD3C7CDw-hUKaZUCkoXOSrWzxKaV5iMJ7BNnvLuY-EHNC4Akyj5csWgsyJNH-bclyZgwcastUYnC86TDV5pDguksdyUj7Vd_JMUmQSi-6eC0lDDHGhpFY-oxVAbjE1CPyBgDTilWKlzZ3SesxpX2o4lZGWtmkfsPdsAw5HVmca9pJ1a60BSNVOfHFZF94GHhJFP73uKSIhx3lOXYkUS5kM_7Bs6Jtzrblary8emkRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWDmYz8tnuTjOnTrIj43eNjuETHKXPNPDkWonHxZXQBdnOanBODU2UoP_b6lSgxB7jrwS4qb-AlWvHlJbJS3M0OoApDusGdlQs3lnw-FuRevdgUOI6k1RWr4CxELTbYSPLM0yS9Qfe3eLrfYOrHUbAX-0D_GUIm_S8abgfetkzE2hVPOh4HrpUzTSLZtdfkXfaw3FO1wMiEncUyVOHGOM8Miju-aj4Vakq8RtA9wJQz4ggXzYauZFuL3BqNDn8bQlJd33XVH9rronIceyVf-BGVcnUzDgyBL6ASTgf39oLeDL8UiG1Wcazi2_2N_Aot_eTDUSyKidOqLvKg0y0Y6pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXrmK3Y0_oMpfU2ToNjNhxG9MgDNUI-0q4AkuEoUUWCUgihBuDJXz1HtLcnCryVBffJLmVf-yB3DitsoXr0BXXdzpkGlq0HbSM9ttqQsqqJegBAWSNSLEIv1YSqEwTYUnENYEc38Ur84Ny86P5BJLfzMZ96-4i2IlRj6R1MG6T7LLc4g4WPo5Ib4qshaO8HhxGefSsCFOMX5PRzPRQrmSEWISXvjaL-HzD8QzTa7wxjJBNvbG8X3meWcjiDW69FOabTygiN8CJufvGtr3-3-Ra2nGkfxwKPU2XJTDEiZjlysOZpmAcyqngJ2B38sqhTVIeJs5vvlt8OLVH3dw_jA4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rymtR106r_UY3qk2LEx-wuDXV0KNk73rVeFCNUqon5BRC1K4LsQQdXV0AFLyk3alD_eF8mkeij0fUnqdxNo2UbEzoC_2X1MqJuYUVMjDQR-YlEUM695cm5i5dzXm4Y7UFiIDPdFuNONg5Zt2ZChoJlJCfUHjCPiCOhPt46TKJXViDn-z4ojsX9Ch7hFD45zWBi08AjTWpoX5V4f_M5xuOp6kKSCL7XkUe6ja8QwYsCvAzGv4zWJdgqZZHXD9nQUljHe8vAecvtGhDKEb_b2od6_zz02wxx7MejBHRh70Zwg8WD9vZJ3DGqq39yNREUYxVoOO70v47JXgtYTeGqqQjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wmr_VDOiYyxm-zWdl8Vn-Bxxu8jQ274ipfkl0ewg8cJPG7x17S7ckfqrzQLnDwl3Mz_fmxsL61XSTy1ICpGWczci4dISJQy41NSSGd-zQH0vl8OdyznnLYeeskFfB0GW1NYimAhvwVfbWTPMUQmqM7het_oaHzZNFaqu7Cq3fvpj-sCPzQ1oGJJaTQzMCoXH7HTSC2w36W27meLuqUsIIgxT0rVkCadIsJ4KgLjchMGdY1EO8TXyGIPJBJ9bZMiLdiX_-y1EQWZkkJ70czF3RvWEkCU842DxYv0gBqTdaIX1ZrdkZBywRCwJiRyqB5y4fPl7jDvhG6gKARNhkV9_Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-2waBU3kblUS0mH4pzeXSr5rLVuxtMHu1f_KmrjT3PYIUSDqT7wXwEhePOqOFGYJSM8CTTvyI8hpefgVLACWgYvVH2JSoD-NxT6Ob_m9Ql47xirzjjWoYw-lu07it5QuxRUPie8ctBz7tBOP-PEyi_Wlq8891B-bXUDquGrkgw5w2szeC4yPYYYL3mMt8pN8nRd5dYxkk11jOTE2Qu8QwhWFSXzJuv-2UxwvDdkmtJHWqqVjSg5B8YlJxFsFZZZ6rD8OHLQqR_lI5UwKJBCK74FRRsTnjlOsRr4aYo3kvT4p0FUJZ1y8F1wl7-HYsmYcWm_PbXpahyuOiTYm04vcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DM7Qn0L7vBgTl3X1Ek7B9IsphbG2AQM493lXZKGeLBZZBDVq1Q0jfZe16uqYtgn074t1B9AptyvwVgERYVWRJyPX7edpDn-WCm9FQZACe-Uxx_lDmfHZ1_EO2x-975pICix_uM_dRA7Enb0wUHTcJUItdQAjRx20E6tjv0va1hwDemUeu6e2BFGnKmlrt8avq2K-doVUDmI8jBvlhqjBrvtUkt29v8OL4QUEZMciEm6tqyeKR7wTuVY3TGo-glhFmS6BBnPOjJxQVCuY1jGXR1uIvSuvnTH2Y5ijnEaFr4WQDNlmJmjrgxhnlLGFmsQx4S8cixq1ETYGE3KMT3iJEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=hdBGuqsba-imW0civlkLfDlNe3fT2qzLoLwAHr4c_x6XcRve9nDIYHhwsbr2ZGUdBeoeLzku23zvzpFjGJDHGcTRg5WFB3Pobc_eYWyed42XiM2JI7MKUplkIAC3IJ62Q_koQ_ct6b9lRMXrZsgSK_6eZf9j2ECmcyK_qXJUE2kZ4qlgEHyNuECpHcsaR-WLidCNC7c-ImHAEnBEfR661cZD6VG5-FrpVWD1VJtsuo9jZ34xz7k8RqpWeKeKVp7T9HEQ66HIJ_KNHGIW8e-Cy0CZsqRORtIExr4WcEGfE6BKBEOjVDW5Jf2hNtwWm2RdTNLx769sdANYz3XUvaPW0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=hdBGuqsba-imW0civlkLfDlNe3fT2qzLoLwAHr4c_x6XcRve9nDIYHhwsbr2ZGUdBeoeLzku23zvzpFjGJDHGcTRg5WFB3Pobc_eYWyed42XiM2JI7MKUplkIAC3IJ62Q_koQ_ct6b9lRMXrZsgSK_6eZf9j2ECmcyK_qXJUE2kZ4qlgEHyNuECpHcsaR-WLidCNC7c-ImHAEnBEfR661cZD6VG5-FrpVWD1VJtsuo9jZ34xz7k8RqpWeKeKVp7T9HEQ66HIJ_KNHGIW8e-Cy0CZsqRORtIExr4WcEGfE6BKBEOjVDW5Jf2hNtwWm2RdTNLx769sdANYz3XUvaPW0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
👤
در شب درخشان لیونل مسی؛
پیروزی پرگل و ارزش مند اینترمیامی برابر سینسیناتی
اینترمیامی درشبی‌که‌مهمان‌سینسیناتی بود توانست با نتیجه 5-3 به پیروزی برسد. لیونل مسی در این دیدار موفق شد دو گل و 1 پاس گل به ثبت رساند تا نقش اول پیروزی تیمش باشد. با این عملکرد لیونل مسی به آمار 11 گل و 4 پاس‌گل در12 مسابقه فصل جدید ام ال اس رسید تا صدرنشین جدول اثرگذاری لیگ باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbKUa4AdbweX5lBtAc1Z_25eqvOIGU-iMlFexxzNcuXR_b2yvPj88P7P2cI8pP30g0NKo_5dpuRPZBHGwPFYGrKVARFKL-sCqkU6IHjMMWGqoXp_xStdCfpxvtsmvwGvBbcgCNBduYWK4NGMkrdZtVQ8v5u1YyLDoHPRNnZi7fybBDEi-Ec9fhZZmhPhh0vayzeJV3XH1qjBZmjk8PQK3vvPJ9xMsHzAVPYmpL1PrQpX29aTY8-AHzz_e4nrXAAv1y_mHDe75S3MJCcgUxkCZhW0o56VbQcvEr6QBcohO0MbAmghC5qY9E39IYh4n0_4edTGLLW5o8ENRRmsOPhmvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7iEuhAhx54bemwF3Qmif4L2wBFsmkT1gocp4A-zlShDvf5MVsFVqNLeGQtz_Fjkxn9Ix-ZBNSjRsHVGK2khRv94NnV9TEfcvSdVorPU2JP5uRIOJtEnYTkU-26fNCUzK7-xQilFI0Rx-VWbqrs2MgS4A16KvEvDWhPGutkVMi8fUTtCHGnU-6sIhxESEVKQFbgeTFQ8SLyuj7b3_wi_m-Ry6p_iQHcCYSkvBsVEz0MyBo-eK5Of_oohLNEzaFqwz_enrv5A3pqp1YmkdWueEencxW9gxSnwRGUOJ_VUeb3HhpYVoXIBREP691Xq-91G6xTYwhxdWATy5R3WFfCezA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duFzkoqB56lSgp63Y7K46PH-0SyFj66DoFoaut3oaM08yAtvwg8F5tOUYVpG6b3naxIV3Axw3SnKHluvP_Ap_oDqHKSXHDdD7aJjAmEKOgA9XlDwW3cDO_s9yw_G_5q3Xc1Ylolw9qqZoCPpAd7IUSkxnY7gwEEjZ6M5IMWmzS_VlT_-nBDATYk-F6rLIZJLLyYO3ykkCy0nex3Qatc6a7pwmQKvtz0F_c-5XXTpx50ItAxZkYfWJVp9VblXy7jt4u-Hz08C6R7Uw0n71VBVSnr72DU4y2-QpRRZfy1vULgqWrPk49a9WN_9pdBwK290sPNx5qpwRwv3YsZhici_lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpclH5owKo3yMNpjwNl8Q4Y9NMcteWnLosgVhburNwjm9wP2hXB-QOUlI01073lAGAZ28rS-tp8glJqO8m8ZjS4I4QEbGeB7XK1QGp6ZytBortdhqoKFtn6nwCYrHcAaAXaKO-4SdhDOuNA3aydfj2mXEypvOoLdG-8pe9Y-ovzWq7kTXtYXh-oT4XRE-MT_Haw0R3nZi8049iJHsyLm1WAtfPYWGX1ZzyhI8_Qfb0RTN_12F4vKSQMJFX9r3iyuYw1NYpcQf0Yk_7YAacHAgKorv_CiciM5x8kmY-DMmPds4tdY1ZsEBETFwiPxeOzYDIHmBHJjAqaqJtOKTJIrGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLA_I8VRXczukCgIyV5-vntTh4kOVXTF9lQisRJgvfhQoVzWVECmW_4pbVuBu_Yh3l7UI-BxjreSv7deWMfCzOXQJhrNd829KGsEN13H7OzHCGHayV5qtWQ7uF4PFuqgBBcMwpPTllO5ghNT60QgnBwrw74PzLahKU0MwTxK7L1Ump-17mbIj4yWmkf24ITo8_OsrlQy0VWr2TXe1vaWUVmrZC5ZxPSNsCbuvsWRP70YMjYLlg3Q7Ls_bBgBLePJsPL5rdKXB_sErFfYCnsH9-igG8UsGDTijQGIlcY5N0iMcUPyWfpr1Vth-9zLAi6SwZHyBygPrCOysMkNjqQ65w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lC7JQFH4klozXRWL6qvYyJHQCpy45Jx1VSMSxvDVGMugcMQhSMJaDZKkSsRiBOCB4eFf7zLrnJoNMITtZ4BrwetP8LIv7VE4jTcbUWS2UDuCthkRYlzFw7AluGbzkuNSKScTA2I75OxQvByk7kebXG8QHeKb_Ww4W7RGznMi_8twms7rnkZav9oU5nOJ16NlbDzmrFwWONPeeQ8PQNIod782iuAKVa6j4zDKsZY5_2LI0SMeOU1zgLuCqskn9EVYKFLX3a2SXAkcW375lDMYQUNBXoyaM9J1fgByNi5YUhXYnM4qvYYCA8HxqTHTXLuyHrMxwn_zjRIB8QyCjCB7pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZD1KfTfIG7GoEMS9CppdCzdgxXCnkirulOlMAOp-ZRI3XGEK-SGSzIkLLYorPhFZGSU4V9WCZh_n4T-rvcI-2CGDRKIWIyj5xuVjlkF22oodympa5Hci2i5uCGdgU_i0GkDtxlLHsLPJ3JC4LbGQMLxNjq7IjGbIuB1xpiHpvGaqJ-S4uTK9nNh5uEMX_vLST_Pt4s3OctkS7tXYpjpv0gCKj2EGnK9uRK5e6vf4eVL5pFmrxmy56qU5ohZQ9OdGdQoxThANBee1sxGNox2egNDpbTT5Kwzh7aWpkAuY81vQurLH7kBur6rYcjXGXvaFXo_nU5eJ4uqbOWlgxf-mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owKvRvlG01cfhkoLcfJKveCLNW2LqQ8ApLUTOtUjJWw3xgmspX6E3_bqPywWccqj2M1JND8qP0Bk8PNMHddz8ZpBgjjhF_XgJNwDG2a0SyWovZphBJ5EfR5nfMVox-wvuBZP_u-kJ18Ey3x_Csxgk7-Na9JVZ41wXIqbfvPyh-I7BH7yX266BotS4tLvW3a6IUSaMsP2gUP0BzUVuteNgLgchqZGg1NzMO9_uVtf1QRHH_AnyqELwcZ6c1q0-31Nosc1z92Y2z0l8nzdQ53bkaRWYFPK4fAisYdtUTcCS7TZqtv9s1d1g5wqERkpHijC2I5yH7af3U8tdNc2lLXk-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=UBUmPmbKFKZqdTCLUEIT_QRdU9XkGAaAUZMWZJ16skDrQlHFF8LR3tK3866XUymZq_IL52MRBgagSYZrb38_Aexw9tuI7fCKVItd1Ps7me7lSHXynEx2_n5A_ZEf_zcG_14tLO7Noha8Py45yvnKQVI6e_Ec_tJEch-QYHTQ8mEcm5-vydqSb-CWO1_NIennNqHJW2J0oUSesdf36xGChbGis-h7jT-ePNrr8BbXY9EoVVHlNX_02wXYyCG0a-v1gtHHwOwpbxqlQqg55yJF0-IfX7f8o--xs_WeiLrfdWipHvBQasDA7bnfVTVB6SujpCpsz0VXLoIRUolB-dzNKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=UBUmPmbKFKZqdTCLUEIT_QRdU9XkGAaAUZMWZJ16skDrQlHFF8LR3tK3866XUymZq_IL52MRBgagSYZrb38_Aexw9tuI7fCKVItd1Ps7me7lSHXynEx2_n5A_ZEf_zcG_14tLO7Noha8Py45yvnKQVI6e_Ec_tJEch-QYHTQ8mEcm5-vydqSb-CWO1_NIennNqHJW2J0oUSesdf36xGChbGis-h7jT-ePNrr8BbXY9EoVVHlNX_02wXYyCG0a-v1gtHHwOwpbxqlQqg55yJF0-IfX7f8o--xs_WeiLrfdWipHvBQasDA7bnfVTVB6SujpCpsz0VXLoIRUolB-dzNKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLzJ-pt_Uxu91Y0OaeiKC9GOAYDrBfGdBWTqcizV-RjRzqOULAr-1ndoQubixqInqCd-jrOhAMcjOQzB0jk8ccTJBH887FVAkhfcCESj9pux-awn_CACmFHQRgyM_0oRt_TWQStBoCo7ReVHRy6fh4IdxYbbKFuEA2w6aTXDRV0m7sZy2KiGp00SMHGh0W0TaWDifOD7pmHvUx9AioIouEYBnL_AUkV78w3A5dr7qLk_EWp8xbiQnP3wk5EJr9DLCHjiB4PkfR6cUSU5XsBP_BUaIj7weMnWLHS7cnjlZ78MjiaCl7caxHkhEVGfVMwlhUoCVQ5hXRtZhvF3c0bfqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sosF5fBUJx_JMz8bXpkZmidsVykqrXfe78kbstUvIlfTSXfIM_jy1vu10patrkU4-mIMv-OD93xjxxd1-9J8u7RoQdpq2D4IJklz3fOBEd1VMlRcEudY3uisWDNMJPSvfTGQUgSHfTG2wiKwbqra_21JRR_3ct2Y0EWsXMfcx3fp9HcyM8vDv7cmaHtBDfubby22I81X3kKAYsq3qbrGmW_MGU0IHXmLxJ7dk0AIjGAlCREvgrPC--J6P2FdRcYSBVjPpsGW-LokfBYRtU2EV29dvpdae7InW4l_HlqNXagePzVEOEevThfaaD85p2rW4n5HtRkL0KQ-vHmN_gaWGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=QhrNZXcm8dXp5HHVMloMTMBN8AbNyaVY-QGJetXDDcSg_7h8mLjPAyPFV3Aa-nQNJbqMMX9HFtRB4VVtTiZvFOPhyW9kh3zT7k7iTOiHpTG3dCH1fC5heCd6nE8kLuunmZbpq3vdY9_VFtjOOOvz-qS4UCDfwGIYwLIrhwbrNhCYlm9CYzWCdbJlpv87mODL05zBi6k0ZpSJpPBuTGDUQOKkRVo-u4sYJ2-IXUfIMmh1OnvyiE1Auuviub2npYBdJyTp4O4-hRy9y70lyjQaJNi48FszP8J8xdw6vUqswySYOxbljQwXcrljx4Boz5agUh8PhN5c1SUJystc8WXtsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=QhrNZXcm8dXp5HHVMloMTMBN8AbNyaVY-QGJetXDDcSg_7h8mLjPAyPFV3Aa-nQNJbqMMX9HFtRB4VVtTiZvFOPhyW9kh3zT7k7iTOiHpTG3dCH1fC5heCd6nE8kLuunmZbpq3vdY9_VFtjOOOvz-qS4UCDfwGIYwLIrhwbrNhCYlm9CYzWCdbJlpv87mODL05zBi6k0ZpSJpPBuTGDUQOKkRVo-u4sYJ2-IXUfIMmh1OnvyiE1Auuviub2npYBdJyTp4O4-hRy9y70lyjQaJNi48FszP8J8xdw6vUqswySYOxbljQwXcrljx4Boz5agUh8PhN5c1SUJystc8WXtsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZJPNa-Vti8KAYw-um-5lDmTohJ_iUumLjKUuYJHB7jBCvREri_tlGQlZCyoK_ZzxgclS6lKt0eX7MIiq7hChIS0ACK4BeqzdbURMNDfAtRoZlT5F-qGy8p2Q3GVOAMvRevNk3p42sbC3DdCkCoLVBCB-Kp13eO-guSWKWLxMLWzsTyHEDX0dkE6DZoq4U8d5ZIINqgHJe6nGJygzqjn7WaDc3qmUlLiIncSs2j4FW3Q58XVthk4lRUvaOd3WAs9rLgA5GIyI57ZYV8BaeGAYiVaTre2h6nMVnIfqIZWJShhwgUScZzKXlax5hrwtfUF96grrsH5bIfJpe9SkKt6yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/bQvXVmLqU9oU1U70H3-9OtXCJRCUriKHJ4-c8bKoO7p8DlcxD_wyK3coAgF0CH0E5bn_x-Z9BaEgTMnyygW4WPJEu4eBCGYRsdAQ9STkL9mjdpf5xl0GP-REWhQCREfz4ECHyu-IoOAP-9Rb8pZ3_5ufzL5Z-oVBcsF5w2PWWFB2baPixuf53kTopKiTYwP5NMW9CfdMiZSDN86sXE3nUlyluNta8ej9ZxUdOttiXQPlSiuTNQ-LtrVfhtlAPRBYzDdX7NS1HBw7ScXRGOiiBIwukgLc2Tsr8KArTmdXsnkVrehdumBOdkyX36zCRE2Wl8C64qTjm-9a_p3jGDurrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه درکنار دوست دختر خوشگلش رقبای بزرگی‌مثل
امباپه
و
چرکی
روپشت سر گذاشت و به عنوان بهترین لژیونر فرانسوی سال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QipuFC78ZSl7x9nJ_7Z-A9rjEOhrSZ1Z8T4skfN_Kf4zojSDlj153YQRFKXMWruqy8f_Ep_Q9S25IXi6JXvvIbQYKSlzFP0-Rw21Hrvq58fLa7jbQBuWTo_dHwc-FlR-LJ6qRSa3zKXvIiHZZoFkOyZbqGResvTvGmKfNFbWf6Fb2umibqHhQNpxcbMgWF_o1CWyRWkjGMu8yOiR8PJHlsyoox38mBliMYExIsPbBBDp6tbgVA_mbxPsg3XeXGRT7U2Y7sriBkQA2PaIM76mS6aEvqjaWlWSBECXuExk2KMek0wSR-5t8xpFDb53fXFWI-l7jGdFdWaFb9EurNhu-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JB1UpOcsCQmYR_74OvxpyKfw0lLNzc192bvpeTjSwjUsZD_ZbtC2yBIiSMbYOdzNi1fJDLWY6DOr_4c58RklhjRwJkru4dquXUYsf3eltc5sIfbkpXOVoXp9wNWzNO5yuDsljDe8TPhoA7XIzjTU2TxS-plKbsuvp6WVQ05_-gpHYvZ5G7xCoYpinO5287AF9FbEiIJrEPOvSfsa1vIL2t07jurLduuwz1UqaJGFtWZxc20NtuyCHcv-75rIRtoRb2XuWE0SvHNdbPVNSj9fjHAGfbE0e66pd98eoIB9BwVeQaK96MDylqwWwDNhNyp4i-ojUedX3WveCc6hrLA8Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlqcV4K_FLDVM1KMWGggZXgBEKGwyIiT451QJwC38pixxLns01GjId3MuB7P6TzdzAotX9HHlfEQpDpeV8tfVBQ8ktKWEfkZMHI96FL41lLLfgoq1Tii69foXK6JmZec3RrmfiEsjPLb9DkI5su7UvN_-i6Nnsv1YfJPUSrIwzeKhiq_FH5OEjuYRzhXKR_wSOBK5d5rpeos5-4lOE4UmyK2qOa1_FZyp_axC77uUdkfrJ66zO4f2-zqYTmAGXSGlL6h3OduhJZqu_Sp1YX2Tp36dZVE88slQa1Hyo6mC7REQk4QI4FJdED2nQOEk4q881RObUD3pTg9r_xQ0gulsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKPOKTLpewEjITIIOt27tglRGn6m2WD_HwKERsYgGQH-2OUQQcWb610z-8DffP_SmaI6h1BwGfxAwaJdBQji2EMPt5dyXgUdkNM640qSe5uZkSc-AGezri80o09_w6WryFBl3KnZv1rjA37msNA_Xb2_jY6JzxkMS9XQ9niPuMLsebmRjE_Y7m_82LOyJGf-pssJ4_XoXHuTL2pHVOnBaH15EnDS1E4g4-nMwgBeHsEyIdSlF2bEKi9eoby5uLPdYE3SQC-NSfLSRc0xtrxg5GaQ-z6uhZv9Rlvyn3ECbeIWyhnWmHO6XUnSGgHT42jWEQpPbXKg1fMru8jzlm2PBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AX7_bNFCv-gfxqPsUEWOHqSGR9J1xBvXNfmpZBQHm826GNewMhvzAEpwleXamS1tB4lOsoLHUaeV_gELP3Xj8QfLGYscaEyYRKU480ofkGcnlVRMykmQSjw9iG9UEcUvp3ySMmTJ_ruGgSs4o_J5TepOA4Clp6pJxL66yYCWo9IOoQl7YI2DkaU1HX0r3TBgMQFWlGtlqaQ4AvH-sq6glDz3WTNyIM8vmjsJemz14vGlnLpwTpiXwHHv_mRIH46svQjJ44fyTHf52w1VP1-mawy8dVymwbaf3xuTR-8F521z-VcOrumORwPhzUGWhd8MJM0pEoTCF90lOL6iDOk4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPFXztuFrRvpa9o-ANZC54GWgzkPHtIDlIemS71RyJbO_k3UDl4lahJmQTtqz75UXyebAj6zhsuOGENkiQdzgL6PWarmya0CN8NpLZeLnf2jM6DoEoXeEzEhAUlXnTKa5EQF8WUhxhI7ar7G9tvKpo3kR3ZMWwtZgn35F8vi4Wl-3nMZiNK6Kimi5jAuaVYgU2VYz6CnIPkiFLnHWaKJWYd_W4O2VD8YmPtzKaIYoNyNKvixbPkz3UpFz_2t_CznQkgDY2_K2iDB8WektaMfraE63GB7L-x940nD42Dipfr8u4C3w0PqfHUNDRtggyFv_mMhXDk5XYPGnLsJ9vJVfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiJlwOrpDqSyjMF4u5StlM4XyzFJFKzgm9m8XCzIKlVwj0RGZauT5wr6gRCs8MNG5jnCWcfmw5cqL4s2KyzclRgTVupOmXjdE6z1yd7iG0GngVNX2vp4NQIyCAfmiCqPl9Mz6Dib8-LMBX_R9JjV3sdAkH6DYbhUM9AizyUUlvJKyHed7mFtAbHedVXhXssPTy5WXHs7_O9zbuKceSKOTnm9xxWATc_Tak-4u2wRdMv0ozZwnPlCdEDlBqdnjMjXylOSQj_I3xlKwu1xH7G90iWeLM5mNUp2EPBPJ0UKZAzqv8KaH2IxFHFzX6bi-4sadkvCLGyGa3uGszqfYFnbuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrV_njP5FyD59C1Owj2ElkTJizLnOnwdr1ADf0di7TI8TPg69jxt3iwWiX6RKAmQOK4YxG18lOfh42KpfHHZ6iHt2qZWTWUsaCVeQqaaKGTxxneS_ST_QwqvKamRExdz3rJ_Wbl9kcxYHUL5RzCJGWCQsetnSPJexjPdea_kxTbdYUnhp6I5jUkfBfdyF5cy5gt38-MNhfErj1-TazyYU6q6lpjG04SkpT-JoJGbebyOxQzOsyaxZODPrYuDjhi8YvnvHkZxUJMlcohc_gakBhrmcwZCawe9-dFxIfK1Zv8gNjXhWFssEo3WShR2kpVOIdzx9P-t3tn3xs7hu_X6LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syO0jRIedIr2j3TpIbkskmEy_L2RSRirAeb8fhKGiWxdEQKPmFHB9F1WxdZZ5OatcwFbi66Zc2NDP-hCl5Y_iUbMEjz43KC29yYaeDFu8O3DG7p2pYaUI9_SgZ6KGRZ-SNjFz-wqOABuFGVHOE5G4BHLI3c9kZtDRqaOLhMuPIOoBZdtgAE5xUO3eE9tgMhuRlldCaNeZZgiOO_jsdsjxYEiSrWQiERtPaTujQ9vEyTSQg6JgLJYxJxtYq8kajMoN6fKlupWyNszp7LN_4KqForYYwF-RX8HknYJaycRWnIKvOaa-Y0diJ2CiGQEknrg8mjTsM5La-D47Dctn8a6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4K4IWE1twmjSsoaE9KAhp3oZCwiob39pqMUfklxYbWAlQAdNpXPHmQcaUuwKFqGjDpfJWNJHIQ7Dy3b6U4XW9OOVdYcX07Pa8D6lnOXdLn5lOt6YKuoT-OOiz3fPRJ9Z5IGpMAs9UOzqd1_3tI5gxumkob0faNCXSOjI2HUCjH-oCD6FgrQMf15tukIXAgXOh_twt1v3dLDQcT9TT2cRYtMUXzDqtj41KBSsumTSdfcBokM4lA-bKOxUGme8WvNReHnz0a3RkM5mJKLZso_95mvyfo6y2BaMQZboRSDcQjeOqE4_lXX3y-SkK92CYrOSiLwjffsb_3W7jsnHLNiBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A004RwwdxTx5GajCqSeVIZX6lLk1jzHNUT7Jkb_AP5nzGi40pKVcUxz7vyPpBEiNhSKO44S6jxyCXnc5YA_vG9FTjSWMCskK2M_8Ff_4GVCw8V8p21vFtPb-7hPIwT7-z3h1He1FqnpfZo9Nkq-m2S_kZ7NNH1OLTiAJ7eyzzuK8vxeWGIn1AKmHRGnNg60mXFrIAxYiRV5ek1r7fNEUG32qL-PSuJQ7a_Se8MWxBPiko4kb246TwUHPE-6-Hw1X7V-clXp7AHdozpTKNCmpTiKhq4jf-L7ZtfaujOenKIdSx4swgBusD9t40X5uSdFBnXTgTeXr6TrQ_QNTMFhkmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUvQOSfnZXgAGRO6wn54NXzpwl3Ej_maaCCAHaFGJRIbayLfXLvHzODxXn9iYOP-fL3WrYi8Wu5689h1kx-2Y3Sk2YkP54W1D-ea8ZFAujyjMyU5KoEIKYqejvpfAG19CUvNU6U3I0OYoOkAw8Eg-PoKjK86sReRqDbqnOtoKvAjidgEEQ5gIpQAWQvmfGWvoDcJPHxYIoV8GUAKtHgIUx07IYFeZYW96VpEvjVvs90fLYlDGiyjKWSP6XLpfOSLUbLsVJ_kcZWB_ynDuKnGFBS1z6USq55QNIIYxIXLy-R5KZXRl5mvi-UVXny-L9OZ5WqBDVKFXnycic86A5JycA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=nwNX0skCireMYOD0z8yPyOnLRZNiFvQGDIxe3iayisLP6XP-fNZ1s9TxL_F1MFw8gpofjFOVl2BjJHIqYit-0f3_s31KEG3dJ1mR_aWUFq89-8GxCLpQiDxdPSTT5iyRuQFdoEGh9Te03der-YI62gY2PI0ZMjjer0iA3XePmZM5OXB2JYV57geJ-UNfmqrc9grkogPAKfQVEhV24ukwp_Gx9_HRKxfLeP9Znz13sVQyFom8viESY4foYqiba0Bz2h4PW67VvISgkuLv44DGf4gwWhsDOUyl2FPNN-x0LDp_TdGXzIPdK-egVFJKlKHj2U55S-b4nMZW32M5cN0llQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=nwNX0skCireMYOD0z8yPyOnLRZNiFvQGDIxe3iayisLP6XP-fNZ1s9TxL_F1MFw8gpofjFOVl2BjJHIqYit-0f3_s31KEG3dJ1mR_aWUFq89-8GxCLpQiDxdPSTT5iyRuQFdoEGh9Te03der-YI62gY2PI0ZMjjer0iA3XePmZM5OXB2JYV57geJ-UNfmqrc9grkogPAKfQVEhV24ukwp_Gx9_HRKxfLeP9Znz13sVQyFom8viESY4foYqiba0Bz2h4PW67VvISgkuLv44DGf4gwWhsDOUyl2FPNN-x0LDp_TdGXzIPdK-egVFJKlKHj2U55S-b4nMZW32M5cN0llQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mw7HLCcZ5VkMK8wpkJEfa-29leuT2vUbVWeVFxFXMRQP8g0W4wo1bN1pa8JXWHtI3hLGU_Lu-fttxyqjTgZtX0uPn3EeHhht8aFaY8VGM6GkgE_tALNLX-V-RBeDswpPOQrGA-zOM49_nm4jHzfAVXYaZkWUjzh-U5ku4KqLY1KnlPowGtAli7i-0FlWDbBbNW7LzyZjxivph4cM5nFl5pgyOubAcdH-68H2BX7iM89M7ya0kn6pXmXI9Hu_caqwgWI4CAMwPOGTJtSA692OnrAc51bZu6eLGre1ca0GBBi9Ib7wUavzhTjqkIPVOaheHF7kxFhIVFiCaluxkDZNQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pt1j9skPq4hMnB1bcyfiuGcpUDaIkpWnFnaoLpXmkUmztl53XowY2HKlHZqJpV_ipnOUuW_XX1k-3es3mMNpDwJAGdLj16L9AoRZCe-tsgALCrQ4tTcLxTe743Kxhs90zPH6V-Y7nGHHYB5FX4DlP2SyrackUqZBaFqIE8QXjGu2er70cKCL06kckAI7t_dw2wZp22-QWHx7C2vS3NGavV4uF2wJDLVhVgmlfvKM17izQutjmDjgDcNx7pRCYsUG-AoW6DbdtT7iFDd_strVMa3JBtzbsTuNkQNk15Qw3LMLtlFmUcYuU9Hl1_Mb6P0B7h-HJKW778bljQANgoNOAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usADtq4SXbn6mwqRheF7aDKy6F1bFo5eEPBJXSwa6zR3umh_amul-OhKqWITLL8292-PUr30Tz-AJ8xMBwQHKbcQnbkuDAG3nFYGAHkcGcO9XCdBAb1OC1200XBwxDSLGTw1tzPPlM_Sa-9anAIR_DElXrWaIvwYkYdq6UhBesOW5JFH7U3HVuLTXEWOjDvl2mZqfTyE2XxCTq-EGFJrIc1Z_b0qJYiDRcTxWm7PzAcG2E6Z5qR6e622kao-XIxfyJ9ScPlA5HEpm26ECZZZKCRf2EyfNYi4LPYy7OA21zq7mmiksx-lnjqf5SfrixOTjnhxNsm_rdVbEWxxzkeBqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUMqHE339tHDIaDQXDuhKsWg1frTQYU1jOb8U7T7cRkN1pokD3u6oaSZMwETFsEpgB3vlzk2g2-4_Z0_RngLR_ZloXUpyREwpYoee04y6Kvm3qYvvP4EtQNNU563iagCQlEI08bTovO18pAdY6aMlxs0QlrHyYy6BAysQ34RQCjpfryBGvA-u9lG-f3hd3iOx1HgS1S6Ch2ZcxV1DkfJ8S11B27ifj2hHjqvqLwpMoiEUqzU0a-pMhYKW6Qr4m-r5PbajtODzkAa6MIJRGYP-saWhUrBT1Kk6zubQ6XI2rA7uFy4qJW5xGOZe96kOW4mnz8m--lpKgKBRTbSMw4wuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPU7Vucn1i0oaf8MVy_2soRPE5RVoC-Uu8l1kA2-ad5aoUlV2M0CRrnT4jZFUOE7ycOKeaDT28io1f9zq5h_NqRK47xmYlySDZ1bu0O3yN3e1hJznEtt-13N9_pWU5gAQcSqo8sE1HCIVgNYGv_WMkXD0rIVdyDVZM2Cwkh629r0CLV1-dBXX_aSTMLG28BKclBk3sTbRz7FRS0IC0UoU9FqhqqDCe9Nw9c6vAsRD4cVVrbz1eMxvu_rkOdEEKCC6RdGV3maExdGptHpAheQw2f-wf68FEUoKkQAEU7SkfGWPAO9aOgOkKjwtxuXD4WHp0COVjGeQ1BqFyzm9Qd4UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOJOtjl3WJ4Qhl7pP3S5XCk1TfPS--RVpfAwzTGAjsF3ytNw3RLMgWO3S2Rjzq38SOcf4UWWAuGJ0tAy4BMqVwWHRFdNOozN80tlsw-uxhiSLVpG5Yb8aLPdGiy8YNh6pzjYyS8jtTQP0hx2GC2xUown1IyFkDflnX9fY1QwqWi4rJ42Q47tleJdztIOHBYtmYTTPss3ot49eCUGES8qBCxwRsyb5YnISqFRw4j5B0JJdCE5yYSHPuFL5G6YEVj0g9-S89PwNBEfFdUh2vsStE1jRyMBeg8AsS8R_oU1n89gmRKWcNqEhy15ytl8muNlONSXhaWS_FuLLSV-Hwfe1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxQLmoxxzCI2T47ydEtbL0pbV2RSvgBim0nUYp_5rtCaP5-6uEmMyYwYzZAGvWcnabUB3R0L36I7i6uxZeFYhaAFspnpGuaZIvribIHvGEC9EYK1YZ3ZeDlTFgy7_KvbcRck-lha1x9d1VSko1I2q27ZqDw4-hz4nFF2dzvSFZAARI6yDjQ1xIrP0usgS8cLULKBkOWuvfRMh9RyMyrvSHc7QTO_d-d15s6tUUnNRg1mww9B6FHCnwS_ZC1wX5yMSSCWrkxHYLtJ39wJIs8-zUcAhmqTeemgrSSfbhXhVO2TXXaslS5e83ThBo7EBpsN_Hb7q5CpMjY4rTFmTVy-fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yw9KRNFRjsFqiw0JHaczHYGYNawPxEgKD3mnbiw2J2epZ92nx0nhN1wfZGDDDPxG8IzddAAtljX3zwCLBCSd3v0ha6VAORleC9W1qEYQBkh3RVGIHyTUTvwD3uPF0z1rcwbgFrgFOI6m6Y7Jl7F-2zZqaPKv9VOwdfjlRLB6AA6u4C0nF3CMyXUPDC7b2JoXggalqn83o9iFhcc3wrojqqlLeeSVHllSr4T2XuhSgOljnyjkhRWlt2LFiOioYCBSk0qtHHBjAXYW5D6_N4ZYEoW0-U7nyEHS22n7eOAJJ8b8tF2znadg8mC48UJMkBXRDmOUeI1OVQPDjBQvGjgA1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0dannULlcicbUnhxtF8RcVPNIcDGJAIQNSg6C_33DmztloGCA5qNgmsUbkr12JhVY_ZjStzgSVV3Opcf2A58VSf6bkbmXUpOVxaGmb9p69V4hvKuPo5frle7VuqsyuBiOJPSMsts7ppS5Jz4bQjEJFpekV_rZmuHh3QhgEv5ASYhErg0ljIkrj5bXDi8M1rMtxaUvcthnSDm7emFknwcaknHn9NDE2wzxHbc9ut6WHv4YQhv3L93WuKEY_VrtfY53i0DZz_so48oLmJ7D1ZJOfEUP0Tp80uY36kniT0CLR9J39sVhPaF-idgULXmg0uaaEi9eu1I5xCreigOcgRmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsupK-1QuRZ0-mug4Sp_JQSTl_nz_aQqF5kGqOpwddunu0NMTsWY94tFZ-7hK9tu3P9qyeQVEOpFEY54dGsdLMZY7iYrMhM-01JbqTv2Cx2Tc5N2_gthAaqjyZ2cHoRDdNUYwRVli2NdXY045IlB-Sk_kG9by1dQiSFuCA8lZ9MNPIMFg1tlslQWE0RWy6T3D3lNpHmggGM-SOt2veFMGVqQwe0GAhx-Au8hLe3_ro1QJfms93Nczucr9JjIel7NQjvnRcRBwgSJBeffgjTh6toq83O7Rf0jeWvHbN5yd5NxXGkxbJPWqM549y2gzWcgBv8Ddi-sYXrKUaeElOHyPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5wk_hilQL2Wo4KW89-PYjbHFIqz55M6ol9Lex53XLzonKcIQcEBPkRMlmoYCoOZ-VcYkQsquiVfi2EeCrK3ZHLLdFNpem8L0NPa2OC3cIWjV-Yio_IvKwxNQb5_Xj8eLeM94B7r7qm3CpLUIvAVuY0niDjqR4f4IGOKpoUvyhLUVolPBkYwWRpvVDYpVxh3diLGH9cxDmQLYMAMo14vDXMtiZxRnHedb2lnsXvSFKJFzqITbWBc2uoSrDswiVjCTYjxOIIdp_nh7sEjeTEsA3ECUnerYgmmTmqAiUecHn0IlczMcENJ4CCtSqeWcXUxH7oPLogseVFo3tl2lYi6Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MS5rK1ICOB1auTzU_bNCgCZqO_T6Wwy58qC8w1XHgjrLckYWjhc1XXmB_PpegQ5ZviAvYGpZdnSWiG1sxMQh0nFSy4laHuivBICieeJXzBzNQg2FrhsnLxt9YjZayxfl_TEql1qI83khKm-aYiMv22822jj3XIb7aF3MqmDSU92g4nMyD003dZVv--yPNQrCuxSzXA7jL0Q3CDvTjs6_Qfrgr86x22IKrx92f-5bK6uUd8aRLZWkSKjp8xNCTSYiQBt2io1-BpOxcrmZXEU6xLT7cVleAtOS6xg7CCusb7AGSrqW7tMFhmE5a3O2DaP_aoBEdgWXJmEC0ZGq52zEwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAW06IiMcWT5lDHWll9Rs97AB4u1cpzJy03bEpiUrrjf6dWGZrjyuPCDZXajoI62CJEJgXAY7dQLjqbH8dSPu_G4fJm22eZfzTlnOnkzm1I80et_EpHIWQyaCN1q7B0BYAumyjULw1S-tADqX5oVFuLA1QZIiKFG2KusUmzyS2m9iVdOFh3wbDRPlz4ogoDYYAHvamZETD1AoX3DVl65uMpMBjFYm_uj9KcjNq1pyRYuQEDNpPmVOMyoRX47IbeQT7SDxk469pm2DQTizaP88Lx5NE7tdbd9a91NS5OZFsQnLsJotmeS5yE90sPZ-oNgNJ6UXVMpn9-0wpcg3NSC7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d32194EuxO6oGz9V7a9oQIj1Ci1BEONW-T1MEag3FCsuX2mywAK4ut64d3PtLENi-PtUH5eg7MCTW8IcbE6kA7AwwO8crGQ_teeiLw04afhbag2dZ0SnYyC2DPKDCyiflKuGsPU8GlgFCzfzH07gdfZ6d9EGRvP5SvPwzICqm5ZTf02CjRvvXID4TYvlx25i-HUZKCph3PAwNqIyEFitoyC13LHt_AuWxSf4C3AosEfFVbuZaJOKEQXrj6iKQrJMDY-EF_bTJOgxcYUBDbedAFkIFkaIGgJP6TFzw3vg5moAciy6WA50x2tj2JIGLA0-ur_2nvGBz1tapG_87w-rbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZp1pCcCqtRuT3nQoRg4Qw6tNgvKG2s8iz0fLFn_QQaQTmRzz34Ap0_Y4BGQFZ3eJFRHx2rVKqhix2jFt0cykImBLccx0pKQ7mzJfWUhcdPvVOdq3hvySaCiZFNdkmvy6vV-Jf3jGFdcJaC0NDYQJmpEP9U-V10eUmW4t5ZvqtstT2Yxrn5e4binaKfB-j4s2Ijl7h7omd7tC9oEYrRNlj-G1T1MQDaTDlSVqJul49cFLzftUkTo1QHa3hyl_lJLX-tcf_eg_P22GlLkF4GJ7I4LbMAsToAx5X56J0dqdk2SXlHVZhW_p3JnzmEdLPZYrC-YWAS9yutYoojJPKE_7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgJmhKM2wm42RpllrXVlhes58Cg7teDN1DtnIMFiSAK3RF6a698v0fIMdmQ8FPjUBpMR5tPZzDbos2sp-8YRsYqokyoyI60EaR-F0897rqrTG5T54mh-2J5mvIzW8Xgg3JzmBJWYh0HMveaUQDFVy9XyvHrDBaUZPNJfR7sPIFazCVp46e1wyM2bPSHgQZoxYSRKx0vo-L_XiO3qJE0saFXCU9qesl3gUEh5VmeERnnbbbtjYvSHmpMulmzTGecr0pJjopjwuxmWCjk8xO-YSb0E9Kqn4mWRU5CLIBglw3VMUSjOJAOiwfuLjiZqfI66IoRO8O5Ou-VdzX-7N4jroQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKN3fjim497E0ymxatrAwAHCSqlfd97UskIdPHJqSgJvJQGWuw98va1QxNg7GSD_zZOl8QG06BxJXI_3LDi8ItJwYC5V_GURknhkx8KiAc-Fr7t-PaLr0kpWGXDnkwLK2SxqElNeDABJMuzSX5P6huIewmRB-C-uDKvN-yedErt7a6f2GYVuy6YpUAvaZbCwQI4-InEbO5ukS4rXuAXaDLL2uJxlyLwouwBkVDoMosY66rUV8TnGliGGLevAhBMCMCj91w6-aTq1xYjeWMYgW27c3K9rc9Qli3g3Yc56bHh6mSP7i6hxntGAx5ocOAuXMFcX-9wfF6C9HCY9rhKE_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrH8xKhln4zIinQZyP2z3cfq_wxIk4T27eAMKZ7dXC8BirekQEim-efzg9OmTAYpo0AZZqydb12ibMTHFBH-N6g9LxJfx90oK50nSk1Dw15hhgX05XoxBAHVqqigUqVVXR5LqBw_mgQ4y2S7w2xLQ5vlasffrlPX-mgUspmtVUmigTi10LZuqqNLKl6wOr7vUXnwHGvNkkNvNXcLNoLxzxeuEkhSFbVnJX0uBhS1JMcnc7lODYLkJsDtmxgpgVwaTD98hgTBBGazMTnd9kKlGNejWJw3x_Gtq2u7-pEhkFObEJOYEU5sQBoqFg-5YGPcTZ36G_KXkkdiD3izQ-w99w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N29UaHuI4aWGAzqjh-QGW5L8rCYT_Dn4VeZvp7a7jqCRTyHDGN4GBR-Ycc3sR1r1mWGL-y_fgKptl-To2lNrpYVhsJ7PQ-RDGauUXmP4CqbCASCGrT-1oWn_Te4TcqZ-YOi507zo3kSHP5tAUfbEWGGI_wmW2nQRrlpS9UBCK6E-bUcOUUqFwudkKB2fWZk8eJLYH5zAILYbTZ89mNXGamOlcbQoVWBXSu6ZI3dAuOUEClfIKO2toDtpKA-NS1fkt4e5KmhBxCCafoiL7AKqFJetcKKDfS-gCGJ4LwaR9DlzPFX_2RpOqyUi9-LyGfjj15ElxTTWPWi5DTI0zDWbgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ilec34Jwo3mbYAmSQ7TRvbqbDUOyJUXYz2lkzCTKrN8DZ9f6EEgfIP33savpQw4sVZl69rTxnEJTYezHdEaDzxUlfZZy6eHBwpBTHt4KRepa5YarKjSceHUaDdEjl4kmK-BNJJk03I1CPh_1VqQp6qPIJbUyCccbMfTgtJnGbMrCUGFfktpQuec6h5RLSf0hQd2mmkHL6QUJBZycn_xPobm9opVegvdnQ4vHu9w6y4K8ASjjplCRLFhleRE4Xd4_YCGqpN_5HdHjpvPnLktK_GeVD61f8lmAVIUStZ7WdHtKyV4IJ9eR95q9AnOZFCBnkJdVL3XQQHDzxMFCAAjuCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVd7D9PR9B9RJ0wQEs7Dy0nX3r_YAr91sstnogwN-JyS_2McIp085LBWvf991wxocSmVGnSKTKN2_rLzXxF68UW7jvjQBDeZfRgV-LdeI4aXE_ummPiTD92cK_aUWxYJpgEfP8vXMmMMN3dYYpRpHefqA33Y84a3gZSZ8NZAKXkrbtGPWh0j9VmKWluZO9RndbxbNX9aoW2hveC_jTpb--Ha4hUUqRwbe1SyN3y64DzHODPUufpjg0WuonYZYyg-xdG1ZXL5KMvL5AyO-8Y3POJMm4XfBHDG_x6WPCi2CQg6jwJheRH9MZ24WjihUkWRopI_52fGVwUiFbGvuq4gpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛ رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
