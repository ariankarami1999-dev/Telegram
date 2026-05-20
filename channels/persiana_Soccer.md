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
<p>@persiana_Soccer • 👥 203K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 14:55:14</div>
<hr>

<div class="tg-post" id="msg-22195">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pwqx5rh0Ongyjaa_IrDuVrgcGoKx_Dki9WXI1OnoV_jwVX76LEPbv8afKzeqdsGhlTQ1oeDKq7j5YpPkKWAV8kUu8O5KzqKJImxb-OJedd8MKubWYj4vFcnaVfhwBwEjCymxM7cPEfkf20G_JJJbNOocYWcq6OO244Y4uwU_l9EEw-Yfjp061-yRveiqu238i1cOUuGv6rX5PgrrNDdL7COdg61w4nKOezgmQBJn8AMMr0TOOYaplBqcFoX9zU2dWcjTq46wHz7M5JImKniHZI_h5rKmA63ldAznEHJKEjn7AcP2fPvAXM1VGmc1QYAwJEZ4bveYGmBzgv37-gIHjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک‌ترکیب‌احتمالی و پرستاره تیم ملی برزیل در رقابت های پیش رو جام جهانی 2026 آمریکا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/persiana_Soccer/22195" target="_blank">📅 11:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22194">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZuOYyx_uNxkqSImfVZzEzQEssr8M2bgz3C8Z9PrClRpGzudHSOyBOTgfdgPV4_kY4d5ofqMRIV_obSEZDhu6ua-XhBruxpXcnoo9mB1XlZ2Mc23nDiNeo0lYou_g8g-_sylE91xqUlZLJxLCwbAN_OWQltmIVTYuqZPusLaJ2exxePX3-Ss2Lf69frlCl0L5YQwbpWdH-22Iv68cg2aK0jVJozE5liG7BpW_hkFpu8h4ktEQXR-Ei-frWYrKm9uMIKqQYAEwubpr_YaFAOLv5Cz4qUqQxGtvkKMyIvHTN9zdwdgx_0K2v5tZn9wTaY_LVUNOHhfBuTccVKp2XPCRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/persiana_Soccer/22194" target="_blank">📅 11:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22193">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_pLfTPtv7hX0PVo4PP0E5l-het7O5Y_uyUCAE_Tm5Bopf2uadgqEMrYCQ-GBcp-dlv2C57JBrPKAz6q2JfELD7nFq1cz7yef6oHFx_X_2HJxhpWlXf3d8q65hJkx3u0bcHWgevsMsqVjlAYrEfy6INsem1n78-OCtvQyA3W3BnC-9scZZPd7Vcw0p7iQUa3YgBx_cw0y-4keoX8oI7VHFt9h2-srfO0k_sq8MGF1Db2hGwgRcEJwxE0X9c8WQmWUqTnfJec1aWOrRmoC-M5EeBEC9OLfmp1dDyAWQafTam6jFXLtJxx-p__YIiLyqTsJf9AxEtTRY8TItFZ4CNCFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/persiana_Soccer/22193" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22191">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tdtxRLVFMpp2LgI1210AbRrOQx5ds2nrLne__PyOjheXSZ0JmpkCAuc-jfflwz1rjw7XdIKxgP2aJgqFfgSVQimNxVjwWgPeXkZ4KVw1f-JINMhxMwgRGU6bMIyMWnZPx4brMBplCox0hTN1axjkI2Xa2okEZDWcrW9U317KDXVv8oXwmv7HRWeaNJPUzP82X1rs643QLD27EEnQj_sLSAJhq8cYksULlNGMnKNqSO5dTz0SBlN_y-d4MbCpTVD6ejj7kL5ol5ldRhxPPIvU0Y_hK5MFRVXxfnlpceDEmY5W5_mNblh-UIigVmohsPpIGO_YX9KPG__qOk0DKQiUIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hIaJuF4sdJkVUO1yoieUQmnVkE-yCYbJAjQZVgshYLmT3Jiy32VJS1dgB2G2YeO88CZdT4zsof6xYq5IyZwyxtcWVN7X87uZeSZstNi5TtWyVHvCaekW0DXEOZf4_mgMeafd6-wsVh-dKFWP6Bf8S_G2gqzzAKWmw8aRrN8BYHZFbnuJqiFILiyh9389dzt-rLjrAss-GfahMON2gBRQNrWd2J5N1FQ9DSM8Kzj5b_7uLsQ3ejnXWEB5V2kxBy9NExRaohd_Oka6AydJs-2jxFj46cOgDbeu-XVeLsaxy7azIvirhpQeCCf3uJP1RwOncO3VYsqjZucnaJxTzYnwSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند.  با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/persiana_Soccer/22191" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22190">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Me0Tkz5ooEnqVKZFCA-p5NVfKiU1w-rReJnKeJ_d5Bc3HsguUZlryRCaQwbExBCztSiMvPkuAWrQDuKTDIOd4y5rksxQegY0gFCetCFVTp9NSWpPXr_bjFNlNNi_szAk1pdwVjS5WDzGGcze5NnSwAVYd8TBWBhi5BBVDoenfzmQ5UW5HAj2o2eK0eulv2HxQ21i36-bfb08lWKowTBUk9RTCrUMyrSzqrKn7Rf1-6qgvNdM-cm8uyn6gLACby5F8Ew5xbL3SUKPfq2l1VRgnyextKiqYBqC_KY32rp_fzKeqRqIJnCAYyK-nVh65LwdnwTBjeLDk6l3BRpiDfWJSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند
.
با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/persiana_Soccer/22190" target="_blank">📅 00:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
متفاوت نه اما همچنان‌چشم‌نواز؛ رونمایی از کیت فصل بعد اینترمیلان: لباسی در قامت فاتح اسکودتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/persiana_Soccer/22189" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jX8DSqAdPe_rgnFPZOptpPkFATzNyFcmTPCj9vh4dHUMQvId7qm6AhurLeT2G-d4dIq5WY6bmBGX6j8TpmMUVNv2wV6J6zBsraMh3AO2KC2dcMENAg8kdXBERJTWNCdkjsiVa0IQjjm-85tm5qCh1LiTh0DqpXLDLT7hBqaK2nZIY-cGhbccJs4iA9ZRgTb_b0zJ-QeccQxSXAGDypn3RAhrIwMdGaseJCvWBP9gZv5mo3AjGf_KiOYUWQYOZ9UOedIThh973zCmVkQu-BLAQfD7CZicA2crB7rYBug1T_84XZtGWDTN-3ZPR3NWjqeGlU23xT8LR40oPpKBEYjhjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/persiana_Soccer/22188" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgZisqJ2pnWt6MfB2I1egbUCfSdxNrjNwedphHiZNg4kHewOnbp44ZNR7n0WUCS6pXCL3Nit2cP0ZriGulpaB-BMWbv3hNNBNRXXR_YGVC4Ky8_HwhXXsROlWZvyLffFAZp3Uq4ipmg3r_7_A20OwhJp7DFsMb2D3OM515pgSIyK3bjm6HhFLG124e-HDLglJmX4XcWt407OAYmmFFmqcDrNJem7ThW7pge24MAVptRnwIXKwyHfZClK0SG1-0FqU8UU7pgp-i6bDOqqAnRQmWEwNphhZS9iF6CW5kJ2WXB81monjqpUeL95FJ9zZBjuFV_vAuNP_27WKrZ_0MpeRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا
؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/persiana_Soccer/22186" target="_blank">📅 16:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6ofVvfNyj-aWA4j9haelPesDryqX_Fc1pTbuINNzIujxK6gCyWXWwBTJ_tNHNhLIUxa76FjvxtfFzz_jIGouZul_d_kMpubywbcuE4_CU7fiqpEr3FF3ZWpRLkREpqNycGMIfHEffqe58v_xdoT6vxoMpmq5Mvgh68IvXmqOyT47J128dm4ZAD-lRzTIafjOwxe1ZpXpfiuFJfBF18egL-GSRe1yHm7JWhlW_LWdjp4dv2GquErVxT4ITZhgp7LabVW2LQBUjozhI3qbwJQjOvXBZ9Swn4HuEK8CfJeHiiEut2IErZyUUdkTGhVFKDNHy4plp8cEMl4UmZKaRr-Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgJWnisfCNaCVdujDf9cy28xWwbz3Oq-GGYDB0sZxAIkjl0lgVK93JVVNWN4P4d4K6IojEoCFiyN-8zjcF5IMqgVT9uGxsYYCUxa-oIqkztVgJSBjE84kW6zpnFWmH3r5G_skryoRLhDwiskTN4kOT1WvmqPZdDVkOFLfjJtKws8MBvbp2nLqh0wKO4ycn8Jl0tvW1uxkJT6JAzL9G8eElsScYvZD5OFotHrVijNM7TZ7d4qKCypBuwEaECAYewa3U1S_s5v--_0jjD77UMTHfluOcZXV2nq0CS0Ab1SZj9yCuBIRH3kMy3E8zz8o42aMMk8_24Gr6cTPcCVM5Qykw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22184" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22183" target="_blank">📅 11:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuoFetV71KluTeoswC1gAqnqBoG0558HjBOkLrEQaBFwBs1BvTTiNjjkvAihZyZiUxR5YiDBexVeBf-JkJwDvtD2PSpvEJYCC8Dv-xz4cIm0KsKx2dHgPF5R718465leRUL52IZwRV5wK1qSeN987wrJGaoaucA72WuPYmZ4oYfJpF4MWnOQSKonTSBf9vByHHonpY4hutozQRvhE5-PycZiRAswVqWEv-1utwhTGqhp-JY9ReUDDMCeRvQ1s27Z9p6LMZfKbpirA8SuziPQySpHo3MvqKfFPgYw0v_pLLAXdCm4rdjfUfpCq9mpq9yknBtifaFO7nUjky6c7iHweQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ پپ گواردیولا سرمربی سیتیزن‌ها در پایان فصل ازمنچسترسیتی جدا خواهدشد و انزو مارسکا دستیار سابق او در من سیتی جانشینش خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22182" target="_blank">📅 10:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJdltt_4g1ii4pqVrC7O4Zwy3K5nUFZQO0Dr8l9Ju0b3o30_6-Ljc97rwylZ6BsOGucUQl5taMMmVca8Fpml0M8ubF5dh2RINTuYk_HJ7Epd2oD9cUOMUV7B9Ybjq4QKj1OCaUAjFxPF28HtRf4dXMKCVLwd4N2lhcDHfxQ0hG5AFTEIvWhHSjY7tM7H-a8UCICn_IXNNUQqE7YmH8ktzcAph5RZSB7KUL7A1blSRb5sGH68o4LF5nvkER7LHmfXBWZL2WxEbHPFlJFKvnN6DJ_v3eXecaJLqQs2B74CaDFrLKD3TIyiEbmxbKVEE6Nx5mG75cbX-TrU3is8HsQQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJ4WmTDtq_LXhgtjXy1IFKRgzdQRcdlYn_bbMS_S-EBKEpOI3tMMBZyPcDM3T8K3-XtELdvtDgrDhREB5cr9ncvYuRnrC1209pioHxn6SGTIetLM4NZWbefbU_458BcecpBLVkezshbOwDNFzEsW5wI4Ff8U-mt6WGowJshLLNZqLbzUfC28d3-5SrfvUeAp960LdJazKAj83vAA2uaEqAXwOQE_NF7JM9joNvhT6pP0sxEakzslzNDCQ48yHHJywy2C6YUsJ-l1OnQ9LbgyzOT8Goy3kV5qPU1ee1JuiDao3Pao89LKDUj2A2JHLK8dxH3xywNzePu29vQFFx7E6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22180" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfJEWFFqT1NWUJhZqD142UK2H8LkNoMmQTEmP99cjfiNktQPZexOc9DG3v01lktlbkPdYV2XGADdaUlaKog97RWXXbnfo4YdpqMTGNNTn9B0TUTHaPrSMSas4LZH1oeygsnUC9sQoPVIqHe8L3R6UW3Rg7qL_vXjwtuwAXwQHrn5SI7Z88sKXVJi3K_oDz4V3r4nCKRz0PxXU5qNV5h19O2jUI9dSNvIvRPXFM9QOZNCPwtrYKFW5rxfc4qDWkxiRB7yuK3T9j5yV6DcnWK2GxKQgn7NGd1s4lE_SihRYciQkYHq7ifPzpjqD2rhdCFE-PfMgEMVU842999-G7gCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه جذاب افتخارات پپ گواردیولا و ژوزه مورینیو همراه با هزینه های هنگفت این دو سرمربی محبوب در پنجره های نقل و انتقالاتی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22179" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22178" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APu0jznb1uE2XQ70wFhB9_tpK3wGv8402n7zZ3cZ16E1kiWnd0J5GRfXNXMukCi8edXeVnlpnBPY8npydPtfEpMwXZJkhUrg1VJSuCP8zRyo838hn-bx_pF8NOTAd2rYC5VO2E8VgkzLoLSFnzEiHL5Cu75hLYM9e2J7YhwkHIAeHaCWgtWmdGnwmhA8QUUQEuW6RYa8Xs_8CV4CGmvRTIxXBrV5t_8qXBs3aTkk0uaTryS-ebEkPFgV7WZBkS7pnUcDu5-2sW1b7a5qKdZENrsw4eLhHwE1dBwMGO6US3xLTFyw50is3lVjdLqqyiDw2QGhunewf43hwp7USF_tjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ru-egjwRMRZkRntLHT5V0J3aclqXfgktbutz7I9quCnAJCkcf5sHgRjz2UZisieuWvZyN43M68laCG4zmP6opyHk2Euc0nkcfYLT8uvbxF59zcBIZ3O04LjXTnBTuaeY_X6sV20wMWNLKfHNO97V0dEwE7AOIyTg3pCLj7Dl8ejP3CQ_s9FcuK8KxFla7YQCPueH5SCGs8mggwrm0h06XarBgBLrkGzFYBInFY9vez9gJI7ERYddApN5m3wo60EoUPMW1YDCDnQLKEE-zc_mK_zkYe4BywwYXoC3xQYX3Z7K5hdA6iZtfMKGbdFS4gb5-BFr5hT2GEzZgdq8hOuwRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZZ9ufDq12GAUUWJ0gpqrI0Lg2hivlFv5VVmu6TCwmuSK8B2Ao85jCgd-ffFRcsXGkRivc525JvhYFjdRQABhf7tiFSNC8IJywulYrpqleeoN-rahPvt5wCxRd5Ko1ffZa2fwrO8g9hYyspbkpfGk2DM3xWxkdKfxuxGRHHw4moxi6jqQQtfxOZXGM0Y-QpGBWl9Bf9qXvyMqnDDJ5FaTLzr6ebK2o-SlOOSF6Ir2416EbwXCpDX3yWE82KbUjD93FslVL10LxFnByXanPS0mNCqr3QNVg8ruU-gz-rq2KyRsx42MSv1Ag8X4hO_UGCB2_4dEwqHceNzYJYiyncUZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841076b140.mp4?token=FIy3wb7n2l2KhniKxN3J7AnL6dU0X6CdjkTzRsjF5hS9GD7SVFaU25woN7e4bITz9TOWeJMC41qO2Xh2gSvA1K6P08GZl9hEDJ59wNH6-T-K5VGT_T6JlJJbAJ-VnvdyMxWE0V95Vjb_otV2Ub2E0cCCuwnBxqAWP8mBYjqN1nBdH8nP07TUzdZDhi8UbNYCTJurMfheJubHzFcg6gIo12-wIDCslw3i7jvlC2AT82cLq4C1iaSzaumoIyQdJAlgUUPqF826w3DRhuneJWZ8QksTD6-nSYtCWIfTgcca5ieRrPCZ0ouO2aHmtcqVOevMWW52bZLJSJGuq6g0B9wWDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841076b140.mp4?token=FIy3wb7n2l2KhniKxN3J7AnL6dU0X6CdjkTzRsjF5hS9GD7SVFaU25woN7e4bITz9TOWeJMC41qO2Xh2gSvA1K6P08GZl9hEDJ59wNH6-T-K5VGT_T6JlJJbAJ-VnvdyMxWE0V95Vjb_otV2Ub2E0cCCuwnBxqAWP8mBYjqN1nBdH8nP07TUzdZDhi8UbNYCTJurMfheJubHzFcg6gIo12-wIDCslw3i7jvlC2AT82cLq4C1iaSzaumoIyQdJAlgUUPqF826w3DRhuneJWZ8QksTD6-nSYtCWIfTgcca5ieRrPCZ0ouO2aHmtcqVOevMWW52bZLJSJGuq6g0B9wWDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تقویم
؛ 13سال‌قبل‌درچنین‌روزی
؛ دیوید بکام آخرین بازی دوران حرفه‌ای خود را با پیراهن پاری‌سن‌ژرمن انجام داد و از مستطیل سبز خداحافظی کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=i848gf9BbTbRSLmp2X_uVuIUdMZs-sRqU-akeqIgeREinEwQiisgCDMYLY11htamznbo8YWdxVbkEdQVXSxKSkGc3ZMBRtzsCKVwdYkoOkpU06uJk2H3WQBQiOz86o2aSVTUpn7S2VXL00JVDfeCuVRGuUurTY9kIdvXKNtqp0qlKZUXxaxaeTSC9GCSQFyWB5wsyLY3FjQy8Z3rDkh9ilVm6QhomvsnrSP4bOtpoFQyHGVLO07r6yHqLMhUDXAqRtPqvNSLFhzG8hMqyPVEj1fkEpHE_UuUizWKTYQk7QMsYYEKL0geCMplFegOxvW2NncUsrHVuzoFV7zZY8-yMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=i848gf9BbTbRSLmp2X_uVuIUdMZs-sRqU-akeqIgeREinEwQiisgCDMYLY11htamznbo8YWdxVbkEdQVXSxKSkGc3ZMBRtzsCKVwdYkoOkpU06uJk2H3WQBQiOz86o2aSVTUpn7S2VXL00JVDfeCuVRGuUurTY9kIdvXKNtqp0qlKZUXxaxaeTSC9GCSQFyWB5wsyLY3FjQy8Z3rDkh9ilVm6QhomvsnrSP4bOtpoFQyHGVLO07r6yHqLMhUDXAqRtPqvNSLFhzG8hMqyPVEj1fkEpHE_UuUizWKTYQk7QMsYYEKL0geCMplFegOxvW2NncUsrHVuzoFV7zZY8-yMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
لئو مسی آرژانتینی در صدر بازیکنان با بیشترین تعداد بازی درادوار رقابت‌های جام جهانی در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cif1e5ayQaZ_c_1xogOyszWNcm9yfwKN0bIxTkX7Xk_W9up5d_K_OiW2AYoj8gvvjunQEMOe_f2fE9s78xcOfXWxUyibKUtY9t3IES9MaWaLxBup8TU5wm4PJbwCRsYSAg0Qv0ZXjd7LpUHtDjkvy4rN8DrlkGn6s1c2rtZ5e3vaFyJUECbB7KarWmRPHl_tf597m38FI8msvfhCbHhMvCV83GBLGg8FMAMkfmvkTXYApH5vJeZ8MxZflB_StAd-3eplqU0iNhZcP6jqTsnPRxyY9To1f8CDCkSO-TGyasyiTKDgiUXKMlCoR6I-snRBP-WPhaGCRbMwwuyszrIA0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UD1qhKF16ssiQrEzLJPDMjbRelJVEEgcnidN6LqDordHYMuAWf7abi6bM7iI-xcd9mymS_h6idPnpwzcJjiI8f739fvH-hFyNk4dU4gnOtJ-uxWRzqbBQHE1efTbidUzQ6KNCr1QJYud0z43N0Ht7kGfB3cbj50szozGO3CiXi2U1FzCWpNgJ-f5Vnx-imr7ayV0qjNCSbZv4o-Kx1yRwn38g3BA6CfDTRy52ZGbXCC9rqWmHzmuICjCixN8Ec941v6BwdOK2fDDXcwcxw0alO5Kg1vsLckC762b-LQhb3317ITlnaOn-GNZCoQ0XBcNmfUdXQ_FLFt4DQT2hCbvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaghYcHuir-XlloynDE9gvFwLUrC_lrp6PWSGXcjapMJvHOdjV2fXaEBIeamjBoeYqXy_LigzjPp7GYIN14CaK34ThZN-ADKcU_pebWJy7vGmto1PnTcfHvjEdto9Ga3H6tHVCcrBkUUPCkkDrdsAaQt4gwsdwP5Ju473jmn3Dgr5l4abR16qdUXYkDUNdlDNdEzPu9stL-qkCV38vXeIE2eb3kTt_NNoPYNHmGwOxTspb0yDsBhiDoyYcCvxJmb8J8o0mgwz7zH7fDn-CNjd1iz5Q0EXYIaM_uLFhJ-niBRMiDjEoaj1XkkQXb6qNsrL_zg5_8Z7I8mRUMHtH4hag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YB7QyXq8YTQaCXmhzkD9Z-uqszZmemkhHtoTAiQTMVYZPf0QVCCO5Aly2vnjWASwRSwxqYb2DVT14gheGpI1pM1zNy3wWgid_QWbUW5qx6jg7XbWDMj-Khqlp6lIhJL3UNtw2pDrGghFBnu8E_DTP9BKj4fFyfY0YcwV6z29bqkWmhQZadRx9AfwCjAcUmHsaVEf4pSlx4Qr1kf9cnM5OEU91V9v5K7O4e25SWlYJt6Cmr2QyeqeD2fveNG1hDFPyqTu4rxXuGCmznG-M4ILuGKWi7DB1nPaXbnLvv5_PjgNiFRqs9CoYgNGNSB_al6KxE64CFbO3snZEsdhm-UvnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ff2he3lRJLVrMMD_t61_dR05Qk2dEBLD74frz2uscWFLoAFFlK-xWqIBWhuZI0c1LNesrYZU6f9BEXSigfOsZ4Q-WE-g24nek6l9aZ5ys3r8o4znb2o31wRanHGVcpsvuhBIfTZ0TGLgbT81PClfO-HQJfRaBs1Y706cC6oVBCUNQO4iyop5_rcDXrdZU5YTa11vNamRNPoJDcCCqVMSAdPVAj7yWIBdmrDHNaKgjXQ0rZOQjKHEr1uyd6M3yG33cL-DSimG1L9Fp1EuDoMnD1HlLPn5KA1iQnOPfqD_AzaLdVWyt7q6RWhmdJvpApjdNME-aYMZuNWFgM2y8TdGQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crlZcjW4OQd6-aREJC6KyZYNupmv3-ZU4sMMd9Qq51zQw4DddhcGEP23vKR6UxBQlDASsfV_9s2oLtekHAPAbDenQSWV4S7-DBD-mefD4KPuq-KhT4KKOujXDi2EeMWLIBNCZJAdg-8OWygAPsIwS5Z4EZlbsaq4GYf336L5n-EQN2QT9gy0BOytRw9w1-wqZJUvdtRKPp1nnP6hCd7yKcH18aNYJ-TM0Vvf-wp0MCAF8kKvsFJwcuv0qXs48ugCIpixKHRKh23Xg2GJWE_asFPFhjaZesCgkl0jRfRY4xpPxofKL044DFjoXOtMzAXqk84ZFVCmAlV5yznpgn7MTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPmGIrE2ausWzv33lr-f5MtsH03CgDz06U9auh13yjRfl4AK1mVuJ-QbzlihWEBQDijZxuVPWxZ2TJedOcg46fYyakUKR1sEgo_tt3wyjrK7HEsLlsHYlcvS22i43nwqP5bTNpvZRgjPgnUwWCSD5MV8bda7b_iwQkOLSWFlOauuYOx1KKQgwx1xljDDuq__JoIf12opxT9rq2iVBD7yeWfnhV0mCK0pKPusPaRFkF_G0_t01qzzd0wsoPsvudEjIEqTkSg4SCFibacY39VEfcUM2snhUaZBIGM9Nl5p39ZxXNxOk9AXI8fnNV2zYsfMtAJIZWAk8s5JM0S0KDjnuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8HlXUPe1LIga7z2uF58G-YJoZInFGwx9RVQb_vTYgxP_M9os911j4gaQKiKhPcyoSfUQxmOnhhtylDANje-xStX9K7ADU8d7fh_8qZJTmrKWlcIrMhe_l84eBHRV1Nb6MvnsogfFLMsKdfDjKtyK2PG8Yy8y8AA0fzzegGJpaMc1qAz4xMtaSVW01Q7AQmueiJNSAwEQZmh2apuKQHu2fSCtJacO4KJulaZPBFnrZawFciGOboFJT2gzxBtE1EPgOtjyZIOjXcYUec8m9NH_BS2s8rOXRe5GG5i7QeX2_ay72FOziJQ4eELoQamCyr695WNrHi-N1FGZEqVOZPVng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pggfy__2kgJ9KShdIhGE9IuWL8xrEF7N2HuYYv_ll5b7rmPxrxi6OdM_UyHYc066Q5AiiX6GndiRkYlvhB71gzfFOL4w5lZvnflMr-MfTUPZVYakEJqZ0QDZpwvxVmpnaxEIZ6SVVT8UwSpjyvIUIX7f6Y7G-UYnKNeMYy19GbE5eInLNgV78Bi599zSAM8ZTzAzLtB0wtWiXMdkpOVMv4zyHEr9tVwV6iDtmZ8qbUEfYTG2pzU1due_FwCWQ9Bby7mw4ZVdAhqJg94xpcIfrPTHNT2Kx3RBW_vIPRJOownx7_2VR_UImuOe_xaquGejNUuLG1l3n8zAtE1dkQMJLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpwNIesaeDJEMAHJltWsie-G97KOh0b6-KpQCIIpoHEqjhHmJNN4WQJwJH6SzPfVx4yVimc35IkPIQ5v4yTNmM4fJC85ouZwuW2V6pXR8dPAFeo-1H7kwBSHjs2r83VDhZLNcXs1KXvqMC4SpeChT_qFgF8N9Qu0HoRVDdCUa_SoZ5pMKpQfRhMfTFSyEMPXh4zR09aZBCz7O4jKEwefObWmrcfdhs3OP3v_9uoYJpH_Zs1CSptq5oi5QKlIBMKQLwThQyvix27ambCpDfG0ClNa4xBY7KAtH8Cp6qJYQR7pitNAfJtPUQ7b8t06_zC-V_CcxhyKA3RH1Ui7atEHOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cecjtDdZ6zYutlra2Ii53Y4AKdsRriQXF2wy9cfBSSNnGQviDrXSPQ3hZq0GG1GF2E4UbZtsKu68Ex_eJ8ifCi3S1NodBjEFwHmWkn3JgiyH6rCCd1IXrUIjmbGOJBXP_ZAzKweZ4bFSt1JI6c31nqQ_Lyfo1q2vYNfCRxWBoMkjWyqS1AhyM9NrtMQFMkTf7smQ-v1qGMrlx0aTGtuQBUIoZSiyeVX3LKmwvn7wPrxsQ8ayQz4JNUuuYO5UWNaQ-CtWSivfYtDZk7Mp0n59sR9G11EtTMMWdxo3_h-MfN-J_15j-Fq6eu6-NOO0azlrz2Si8FsBiidKb3zFKawnWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWkYlSqLPBn5CfEGz0It_F_4NlZrk8_1QAQOUGSx18midm1d0wDX398LFMBuWPU2PWJUABqfnsrK0tz6hH7f4gnal_RiY8zU-fGWcgpVeHuiDYopg64IvXUtqwdEmlfKy5G8YmfzS7tu0aGKLUG5dHlFoK13nIkq-QAuXCSSAUL0CKOS2rBYLlJkA-yO-MueXMjghLy6aA_YnksoCAThr_-4cO2tPLGrHj700j7LapLbDWED92usEn6Dw559ol0gNDiPIvakI08-dnKxTogeREqRYtgJ8YgNQ3Er1g_PGz7uKFMPAWACXLGS_5hycMze34rLfr-dq-jaFvdzsrdZdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnF-i1Pix160BdOlqBmlcOfMteL5hEisCtCHZsRZOzGjuqWWVndVFSne8fcNYRgCzVIXaJgKUl-i0LdAiHDS6cuClSLhONJ8CRAi0SuwOa4JxRJfPR_fsPHVEcB0e9B6LW86BH7-Sz3dye20KsZdZO1PwmoKTh9zn92DhsTXgElbPNAGhV3ovOAx2anLb_5xm3reYUUDggr_MkJLJpy_xUipVQJWwffIUDDikBfbChCZxw-UOIgVMxrArwLl3y5x-mcDVAca4P1x30slbzYCCNCBoeUXw10xRSycTJV8Fhwn8optnwJlkeyEgpXpbCSYYZ9qtZd_t645Jv6OUC745A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2hj90zYoGkZsfZqmdDV3l6HofzOxaGCDI4XsWpOX3PutLxiXKx6KOCyBWg8LXHWpPyd8VuPw-FQw3hpddlJ1EhfXgwyoaC11Vjmvu8bBDYEvLER5sNggjP_jZROSMewvvyRL4SRqlRFbegesw_Ls23OQWDToYlKyVeNUrCqP4tiYtlZc7btfjTlz2med8F8mwsmlKXBRiFJ2Y4Ms3ZcUw0W9I4mgJVKyvKOrhy7kuVdR7ocKMH_Hq_focCmiaBYpleR6yTHuKneu1xJJFzuqMUvf2kz8rhHGu0lgKcGDJ_WSrz522bGiVHQvS8dN51StjFYXCO6er6DewyQaBNEmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWilwLWpmaxa-2G5XAPAa1n4Vb7vnn-BlRIiCSsg-jEelKPA8J1IdDFcZ9gd-pZtuSmiRQ__xOCxXq3py3iDXyeAkn44-pwT-goJ4euAJ2IzTemXVI7xHHEK_WXWJUPwxsQezMphvHqd0vjphfSVi9NZp4CtO4XIww4xRJ5FVvZ0Q02pTeieQ9o_TRZ4DwfdIafpDXwlXqztA111XhArqnbeATEDVQ0dof_qw7waTN-ZJQwvNWv0AHm_mPlqmmESoV4xdPx58Dntl9CtjCru6LjeKXgfjPhroD3-HCs6LMmk8BfxHy1mno2guXrHiQNR1rxuFY6O69CHUmSg83JSTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsJIDncg6hZjfuRYlcpnW6N8SL3vlzNRG87KGWym4TKnoOYMhckHbUC6GW082Tk_voTa26ZdF40DIhVdS0nWncb2uUwc5PjVW-ubL8z5QKVh0r8fVTAhWQGJrEuHI6Ky1knIASv9i0cRh3EFJ4fEQRgjUIbxZ-P-0vxOWF8g9PcQuXbPNsV-hmuTzGI9k3XxbYE4u58LcojKLdGvSbbM-PopvV50oc0PEjay8LEnjIT2fE0UlE3z1iDdVECxTJD9Rmat-hxoMdfK4drg8ijtjW7rhq8ae67fS9gt5CJzxiuNAKE1aSrHQJPCaTb8S-TzQPSqj12DeSf6BGQm9-qtJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qzlm2hFIDB71fr0NT4MRSqwN75zoSE0igqZjzE5FIqW7WWzqi8CBIV6hbVw4ujHe2C6Dc0PA2L1WTuvw7in1ZmyAAmVWwwJmo8ybrR5MyvQy6kV69sEBujCdYtm7J7Zi1HHo4BlfW_hMAE79BdHL8I4J1nAF3K3LrAKe7p067xN52E-DuXmHYqzfTXtysI9P7fgfbJWFjk5VsnHeDbbgFYm5zTpxNb1wiyYa44YMqGarl-Kpb225igE5PjYS1MihHq5jRqarU_5TrtglqlSVarlPLd6hsH-GINioJ1ddIG4whnAB7kBq1jW5GFW1HKXgTF5P3-ZlhNZHevpMt7geOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drbRZ6ev0Lgyn4F-XtMBHi0R4bFLVYHr3EchRRY5UklyKecuGxrZyfiXm_0SKe0Zc_1StSStuF_eF_OPXrtr_sLXKRiBLKFQVltwcF-WxU8ZUGHCRYzVaFPhzjw3N7TZhtFbWTBnY4RDX7hNaE7H1k9gdm1jxYvGTm_1PWhzZOreuWkHn-Va_EDiAIlhvYm0UfiuAhqDk4a7UyUMBfJToF_LzZYxt9DodVOLMImI9nvqb7tQu2gKe4lC-zJ-eKSC-KjNUGfG1grnYQlrFCS9d2ImgwpadA65LYu1PQ7lYvZ-oegUpRrUjuLvj79h_gESzJpzDqQb_BD0CTB5wSzWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEInVbEpq91XpOFQ3KyI7nDan5RK8RyFrf5cFGee4AihN5kWviWlRnWheZKTHiUbU8eb6sowUnE8WQ2AyyDyATOkOocmuY4kj7Q_rbcizH6yE8ja5eyrvwm_pTfjss5zLURO_P7Q0POQjBgrdZxTO9K6WN-sAyiJukB6RMb1jWXQQUiylLQvrUP2lJSN1KlUm0F0sG95ndjnsnTmtSz_YaKhQwFIjFtbZFhxqaisZ4DCedlJd3xHUiopvCJDRzDeRnEbofuhYYpq3WrgGkhTumgF_lv9ylhCTLHbbLxRAJRhVdDMXJueqwWDAK-OOI4XSXOIWqjtq4ycFPWAqGLdkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZYEtqQm0UgOUH8aH7K-YiBGRqFDwhL0qQKhvzB6kB7YVYl7lrlALsnfvQSh2t_Yo4EPWXtMGhNBoWCjruW-0m6gqMadhLjekKfu30Oo1G_zDlpBba5UelIBkBihQbNvcJsYFPUvE7xhZnt4ukoy0k70M1f08O8ovk38HI9CxljAu-pERU7eA779SAbhtW90Vtl0OBBEdBrxbvPRfgmBSfdteSVawTLGAUy8FzVN84B4INPfft1bWWWJAxAkan9y18i8ANh-pOCueJto-VGtzfXm3Ioi-pgdLZ_F01luvNwmyo9iv8hPJIsAOndnPpE0tiaO51Vna7q2H_0UvhaShA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUV9RcShRX1mwYl1kimK54le4yNuL9xH86SvuWKBYzwc89K2hi7npbH7vugO6mK5Ddtn8_6pbrDv_mAbD03-dJrRkkilUr3jfIfSy2bT9LjElWLMSWRhTd0VxZliuUDfnJXMF8uxVWnNqb8xM-DWngdxNiUu4PViyAZ2xQInbCRlWDnSRHtjIXR37l0mD0aQibyDtX--e0QJbvgm-ktxrhYsQl8mzlltAs8s8uorSUdSk1YNwlJ1TNmkLOCoQAjVKqUkar-3-IFGRr_wddkqQUj0HzysxNHb8GUk86kv-MepmmiOV0JfnTQ_FcFyhxnaKkIqxmn55jIBO8IDtvycdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faj8WPW3HEavNhqPJf55KkB9opwdzNijXzHpN_XUUi2HiXamA-jXWQeWLtOuT42qAIbxM_pTk71-qzhEVuqzChL7ac-jBzr8ctT6kHpChAZtcQwxPccWV1kzz9aaY0M85w4iKxfyYNK9Cn7cddMujqQjJZxATvXB41BddROlkOGrS_Lq563JgC6rjeGQR492rVWKJrmsmKim-0WhUj7aGqN6aPxkZUvsv4dwllpJxKzUAdeYJmGwurIcmbX5JjDNi0_4ebeRn-4YdgnI6S_hJhx7Y4YKfSF6Kr0XkGfEhitGC7Tv3--DwHOWLg0erMRQwiABWDEGicBJeC2tLDP7Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfILJv7HGWhfyfxrl78rUJbzZAd80FxXbg7PIlDQSF2sK6xk9ikRu-sPAj8DJz_wDxph8UJqoQUQeG-ADX7b7es14OPn_iNSWI6dLuwlcWDMlCRhK8BIY3JMLn7SubO1ZUeE1VP-x91A2_sKnFc7azz7cctc_tVTiyvBC5tHuxeca-4j4SQAj7bifUnnXlvYxlGybBi3bZV3FNY59aFYDF5TVPVDeYn_Aqc-vZWBLxxxVxbqXf5XnYf9OE28qur46BJSeHQdEkzE-_Wf48JlFgnVRQyg5fYLMMGzIY21t1OQYFB0W8TSO62Ys20-RJDruhWeVvjsPAQtrBeLttoO4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SB-OKaaFqosXCh_1TFBwKIm9dia0aGnwjyUM4o6scl_TMWWRWDaXxbJB9V0DAwmPdxNOf5Iv8gEuROQcD4oXi_eZLYdAVDpVt8kY5L0PqdTJtDqbAq0UY9SD2bZVfM9rXaiJ4TIRl8ePrzthHBRGBtayJO8DNYBPSNh9h29sHbVnE7cPmd8wuLVtgmIj_M3erzrT0KPsaf57niDe7gjVsuS-JDxaORrQmZXArld82LtohNy5lv8jVHOEyDQ_DdbaI_1EtKUT60C5OvSxDRFDvn900VF2mn4I7-5yh-_pXf9ltk-SN0vpOwBKLMM28WZkdB415JvaVr9LKzqseueCcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAFP9-zaHL_VQX6zRIYkPy1xP3piupoHnYdswLkRk9-dbOTfWNOq0rPHYtLXEj-yUESdLgfhAQS1Lm5V-P--b7krMK-j-By1Bh-1Nh1u25_rGU_FeEJVDkxeIH2Q0gAuyz5lv_bGuKqrsPKgF5qcqflaVoFA6bLHJqPP-Hj7jQSJ9w8EvdO-41-7gdrBZsT0a6-3s_KyZPMqdyGcoF0Q-qYrkm-XNShLLyZtwGF4MPQNwSknB7NPDhCDQZQqqOPz16cufnMCiM851Tts6jJ8UbUix2FS2xUH_uJUZ7p1GvOgirLbY0fJHeNS4Ib_M97T1_BvS7ptJHVAwrECG0I88w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuZupVwCVtqGV61I1O5lHiTpUBDgAO9H_ta0hK8UL4IH1B-kKXaG90QgnPyPSxgjQu5Nd3z9fXK6JoKXL1rrkPEF_UzRNuxG9u3-6CnYbVTXjf5zzrlh6YLIJFRiPlvORbw0LlRsGZcXXe0azChgVbGSAZxyGN10BbfHVD8NCIQYUP6yLtEt4NK3yS1z9N-2RTV9jboc5mS5o2RdX0Tfga9xgT1lOqW_wrHN1E14H1n4zx2rD33TtUkOA9fMKnLkZCHOb6zuKT4vwhuZm6OcZl_VVvQC7dT297rWPePQtLvcSQ5Nn3DspAN1a5XKXpxKunypwc0BrDC1lv-RRR098w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNNIN2A7YFbg_uNFyk8jDtzugbnq4RXD-yhVlnE9y7oxBVhUAEn8NxrWVzLz3Nm2we63VTxteT66K4YKT1HvQSQt6VSRthF8O7gXELXcSXPZqanZUFLusPFzaL3uopvIaCEnQO3WiRCR7StxgpQn278RMwnKR672t1YFjI36_Lq7m2uXxJspX9CPx3W8o2ykGs6ut7HwpAE5cHBMdA7hOalDst9_iwhLXy_JUUpIJh7IufynEGomhkDmT87CEVHaKpdOdLy4uudaPD_QVcrNMoKrNYj-iBKDbCri3l_eeDARiSQBpu1zMFldBwtNoEXwCg3kMExD8nOIrX4CXmW06Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=FeN4zCSx3cAylBG3lrcM3T4URf8lH0L3U-ICKIX8OzZ2VOT0S8I4Op0aPibF2RgrdqlMPe0iFwZz6LuFB7oL6oGk3lBlO_Dz-XVCKRCiFkFMyYj0TVkkCIYwXN_pE-P2oAQPZC3HKroeVdEocsfxPfUm0pClLRUGztUw0UrUHz6jPAp4wTdNHfRlq0tK5xEkXLROs4t1NNB5SOnCuYzuwh_q6nm_LvqpyMQFzuBjj4t1U0s8BjOZPn6UCCywlDmEE3NijFRGbhIymIkTht8IrV6I5AT81BGyRmLebeI6j4pSGCRNYseE0bfLl91UGH-wmf6pBvHequiUSqRbTRctlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=FeN4zCSx3cAylBG3lrcM3T4URf8lH0L3U-ICKIX8OzZ2VOT0S8I4Op0aPibF2RgrdqlMPe0iFwZz6LuFB7oL6oGk3lBlO_Dz-XVCKRCiFkFMyYj0TVkkCIYwXN_pE-P2oAQPZC3HKroeVdEocsfxPfUm0pClLRUGztUw0UrUHz6jPAp4wTdNHfRlq0tK5xEkXLROs4t1NNB5SOnCuYzuwh_q6nm_LvqpyMQFzuBjj4t1U0s8BjOZPn6UCCywlDmEE3NijFRGbhIymIkTht8IrV6I5AT81BGyRmLebeI6j4pSGCRNYseE0bfLl91UGH-wmf6pBvHequiUSqRbTRctlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Od9JmcK3PATQnNGeWjDLuqFPj52gDKpRSwFJq53PTDBRWcoiLpHDIiHDjHjFFttkLqBdxQ4g3dilHAT5q3se1sq_BU4MMvPjeNW_GJAt3adCZ04_nywNp2V4H3PneSBTXsUF-EjJGhYd8DUSDTrokLafdpDtzAX_dRiJ0q2E0WuoAFat7lonqNbKadb3oZ7jmZz5LC3Sfmf_uYxssv-urSFiUFKQfbTWEuIRmzLbZ6whpkYAn-P4KNg1HpiBs8Tl1m52HLnodB3I1BkhUwHYM1QZQOQa9YqyBtINnfk-QiCBIalEtqkGJDwOjXRFx-HV1z7-j7l46EHLAT0OrcjsLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSzJOpr6HnL51ZA4PJSxAXJ1W3ioywR0-p6KycAtMalqP8usppQzlfB9V4bjWtn4LN8k-Ewlcmkumrm6-BOMWSeE1c6MzuatUQj6lsC0o9mJqmukpS4fQUJfzndsoeQxSdnIV8RjwQe_ik5tFEqCJs8WKcrLhZZo2XGvrLyT_bYSafpV-iRmTCOih_Oj9xRd9r9ETFYPFnYfBCYYxPfIMxhmJSJDi-MsQFLHM78kSSq02LLu1HcVghT8MyciYbVQNFDrCBenugddtWlkD2AIzgwI0Fs1AHEv8RxoKvRNTBqfXTR3m_LgA7m3i7aEpBkGdDFdW10TJ1rPskyIGGyOYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzySVEunBfwNTkv9c-Pd40FwIBIjd7_4i_xiWq3_uoqZ8T2Sx47OK3yrrbKSPhPEs0-MNwkFC2m_If1sQpNLEsgY_3abBWG8aQDnyJT84gi0-pAvoilTNez6yK2YhtCkrV7ykBbD8qTzbTLGpNd8P1OHISIh6GjFTorrgrEhO6Lu0q3suNnREmAC_CsTnKxDQibEDUQXOV46-DExdJuglh3puQ3fGxQtYyHY_aTXloJ31-uFB0j7cD5sQNAdu-t4p3uP8QP0P6XmS8CpPhs3U99QZmvH7Ziiy2OdDA3RUZOoQzOy45X3PPWIBL_mY4guMrf8jD-jPB9j08sNHq_O6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0rU0iHOT6Y7TSsK1IPJO6hgxpC2bIRS50hY59sMRGfuEHpLGxVhHwvWICq4Ux58_pcLAUh0vgELY1SOp-EhTW5wimNE6D32uMo5NwNjeJVRB0FbOXqJpplpZXH7dgSr7rJsGGEHnkHaU5rYNXo_yAh0k20saQcoOKNV56reLCJUXdHhz-13e8xNdSOumtPtL7rZtlUX1pAP0o5vNpmy8QtOPe7jASTFyIPgjOps29RPvJsnCSIJL_uAG2lKjnsWYGoWsINLVWyfJTpFfaRMICa6ciMxayFKPK9VUA3ZpKNRw4B0dig2OHy4x_Se4p80V3gAad2QgYsuK86bp6DO7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1PLrQIXZfhO1zsW-YoPyF3Te_W8-XwNdl8XtFebzYTLIVL8r2yfAi1rMDQVWY2WExYw4FZvgSCl7S5utHIkEzbpxJZIiAcB4pLMrdBu7D9e_SwL6QpcTZOavObEr_dJXzvUv8rIIHdyXj-qTz8uH2ytGgecXYbsqvICddqT56MZ4Xg6i4VnZxSrt2DgXHxTVGDn6ZjuLNZ3mo1YKSn9vvd5QMRcQT-pFEFVvB1cose7q8g5lVMRIX9mp2ZK9LA2D1xfvsjQMxJ436v9DYo6UaHM-8bAvVVItp1Klp3riDOm1TEaJ-bKfjtKdHdUeIu29ZZJKbopndyV9rbzwbfLMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHFAsLpDqCLnxRohCfteGN6X2Qlpzr4mudxdWZTtF5HWUUd0CTJh_mAcUOSiLy_kT2sVachpI1HraQL3Q5NyXf0vRqUfyyVcDhgjcFTMK94JaVellLNTehZRk61MPo6dB2P4b4cYtTBQ8xjTOO_mkT7FbD03qxEz9MEzSYSP8bWzfqHPi3Fojp4qLcSWjJ4TG0Xopt1YpkIQQT6E7Bmfh7GRLxmAeDBWxUpgFzNxIA5jRIJFwS7sgngkv8qtPdt2_QacsQSm52nkAgbrKdfzylZtSZPXi-ku8INiQ8JFxCt702tCqCyUmr_lDatZweAYLvFwfOJ_5Md11HahkU1y_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHccu8IpEy3p0WhYM6PoYGYrwayqSGQwcwvdcGvIAbchgAeaaQGZCSlKuoeW3ftCycxjthEdAhZAp5_1Zs-zaqUHZeptu_X-S6Z6LxJhV1pfLnvKsJSZ0bGeKg8CidS7F77nMFOQZ4dA1T7YXRFbXwUvxAeS_1jOuJGSfmia00DCOL5EZEEJI0ZNbw2mL04ZJYutiu7uMU5o2bj5sHso2GgORN-h7N5Jo1mpai00Db7sPyp4kE1hPbGynmOSxmIiGOFwi2nu-tu9iy_izQAGxkdwvvfv9PYOQi1OdI3y2Hcoar3Sw8j-XW__SUNsa26-IP1qgHI5P4kI2hE__HG7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLzOH3yo5iJT7XViK8wTHZ80bbF6ZPU3QlAoiY7amAr9krQ5pjm6WkoQuNOYzH8_2PGIptiRRo6QjDWt8gY-a2QZotCy-K6uRUgguYVoMBXW63RjL4RBKtWZVRZho_DaoXFfDSb3MaV-N2uFmm2E2U0aLes_XB4QN9Wp1r_JW8AQbeRu-I_q1QAm2XaSVPYxlOeEKdgO4IpcWj_umB8LTePctw5c2RdmbPq4punO_PjXj518jwhcs9iNWIBcEhBO0LwF-ZQTtg8_2uZfcyGiMTinkQje_YuEEJw63lzvJxOoflUYfkxooXv8si6LWqbtIemojmlPLJXquNZwUsf3pA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=CMP9lmHbQP5w1z0rZbZ3SixznXpXZZKjFMtKCAkpmjGr_KvbWHo6hTeqPJujRqwNw3EA3Q8rktCstA_edRc4f_l2qRqjaYjhpn89cW_EPdFCh4vZXpEJXg3Il9gn4ta4iT9OQiQw4Dk230rZafAnnuA8khSaNj1SwLtkaYfxzQcjhQcAP2w9d-DAVFqzqHuL-hYDeMlKXdY2RBh20VzqcKTU0h1-jeguOpqdEY4TIvrsZfhcBHmdgnbeJy_oWgrflRxlSBBvMMwxUWDffyy9xau7txtFPJU8Cg07wv7KghEqXq2NGeeM-Kaia3wTmcToCP4DprX-YQUQka5dMWTCyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=CMP9lmHbQP5w1z0rZbZ3SixznXpXZZKjFMtKCAkpmjGr_KvbWHo6hTeqPJujRqwNw3EA3Q8rktCstA_edRc4f_l2qRqjaYjhpn89cW_EPdFCh4vZXpEJXg3Il9gn4ta4iT9OQiQw4Dk230rZafAnnuA8khSaNj1SwLtkaYfxzQcjhQcAP2w9d-DAVFqzqHuL-hYDeMlKXdY2RBh20VzqcKTU0h1-jeguOpqdEY4TIvrsZfhcBHmdgnbeJy_oWgrflRxlSBBvMMwxUWDffyy9xau7txtFPJU8Cg07wv7KghEqXq2NGeeM-Kaia3wTmcToCP4DprX-YQUQka5dMWTCyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRCndUFIpNJ-nXB71-nfuuUXsKy_Elinz66kVTaCnZ9pcqtca31dqNfRFceOVIxPf7HOKBgJOeWRu5MsZe9-FO6MjP9IcxMbS-8AtxhjmT0oaMCua5TwS7J1c888VLuwHFioKKzcP13JIMvwaDtfcxJNFxkLmCaqBeh5XfidihAabm8dXFpz7l1YgQYq7Y5BFmVZrZsmlLps6ransP23et8jCA_S03lJjgxAPqm_pTgwxUv8yuTl8iK_9V9lRfWyiQpn-M6QHBrRWQXjYQa6FMsyymWd1xK12wRXBusQm2jK0YdFXZO3W4E1trIuIg76te4kWklx3lfWOImdAg0tvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JL-8OJ09thnYB09KpTkV1SeGzwjpSUd2mGL70eg-QruBfbMg7bP16I3XA2b-lls09CLnDV-IfkclzBU7a1jX0szXocedzGxYJKbt5ov7iYVBHuUXPFfDSdBu3ZbXpY9j7nzuszQk-X4ln6euDMVQX2nRayPeSr_Hj1hTg0Ek2XqLsMtZ-MUmA20POZgoVvaHd_7PCvt-V56uunyGsiA3GpxmMYGgBCh6WewkUWx5VIko0jmQsCPO1VzzHUPM5dQM9-40SshdAnppcodVZQeaC1_OOHaNjSVHrn91UOAMiql8xdm5-I1O-aDvLKwC7Tgjxrz9X-ZJ40FZN33jSlus_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=GtEEH6mWpo3ybfIVYovSsizYb-O9UZbcD5UoOAW5nSSimioLkq-FrGmSuaq5QsHKILQZ0jdDBZaq-OUHYHEa6j6zplX14NOOEiUVu6uzdSwJO3QcBg2AP3EyhMg2E_kgB6o-UuKDgRV1fCyWEs5lotbOnsaQST5DdLpRg6XuYvUYxumM-9aLtpa8NhA1hyfvTg01Ktj-M24QFNnH3f5T1kH4ntQMBrby4irGdy4TDhu4O4IHg-WKvdOwUH3z4jV1aikmk2ZYA39CYijGA3ki8PvOJ310pGvz5g8CTyfX75aC611vIPZNf_G2Hgz_jGn0PrmCBwDY5jmASWzsY35nCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=GtEEH6mWpo3ybfIVYovSsizYb-O9UZbcD5UoOAW5nSSimioLkq-FrGmSuaq5QsHKILQZ0jdDBZaq-OUHYHEa6j6zplX14NOOEiUVu6uzdSwJO3QcBg2AP3EyhMg2E_kgB6o-UuKDgRV1fCyWEs5lotbOnsaQST5DdLpRg6XuYvUYxumM-9aLtpa8NhA1hyfvTg01Ktj-M24QFNnH3f5T1kH4ntQMBrby4irGdy4TDhu4O4IHg-WKvdOwUH3z4jV1aikmk2ZYA39CYijGA3ki8PvOJ310pGvz5g8CTyfX75aC611vIPZNf_G2Hgz_jGn0PrmCBwDY5jmASWzsY35nCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gS-TQKj872IzDwBQf1q-dQGJS3B24wzPrVdbANb_mKEcTf00ozAMk9vTQBfk-yByXtZNyzmZT4FzJe6hpEvC8kg3I_B1n80NmiPhO7gS3WJBOLrGfDcoLz5dIAflmHOQgg9WaeyBLTFTfuEhsqvEm1_JgE_OptW66eR0vR5b-lJxQfORTY7aG8DKEOpgmNOWNrsFIqGyc2SRpTSrksMHiQdKs7euSi91qK2a0hNsuAPjKVJnrtLqbqBctRZ8jQUpFlL2YSrXGAYGrhpOxjV2Lf5FvZ2K5yL5Qw0FTjgrva-By8iR7Flnj4HmsmCkBrPA2hnTjX5TU2RLvAiyazZk-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/bHgpvD6mFWQlFi0pH0Hz_7vKnGeoj9s6ozDTOlkYI9tETbw_z3hHmcehZLc6coO3M3AWZiCoFWU7mWd8PxmGsUnet8815Q-fHVtMkEvhgOoPgwVDMfcqzR_XxKd3GElXPGUMMQ4nIbNoakpxMlwQFIYnqiozYGje7trIHig8INPXsa8pemTxqLsEwlxuAqwXKRcbxIrfpp64yEzSwLq_LvskPoGPESewi6v2tI1Eb6szbcY514Do5iv6c6w7GLYW1cRTMRMQ6HcATN9nhwgZw1nOr8lMDUmbnaBi0a0ExLjtXTN6eok45Fcn5p8hvAuMzOBzHbgQVxDDy8XX8-SY8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EE6L6S4sy89uH_DaWaVM-7lAfEUKk3HQwiJt1aNiTBPj8Jw0EO0PGSiYIItw0mktRhg-c5VJCcgNqu0w6FLPbsLrETYarOkJee4AJ2ZJD_aT2KyZqfBpbwg4VETpu_a4yINL2una0sgrmLvbTfVewifHNtC4pCMoO4H8f2u1JMgj1M_B2svukjqGX6VptY9brORwk5OU5MEOLELzSd9lAcjpAmoT1CFpTjKBKGsll2Fhdkp_7aofOsbG5OxhVwET38Cwye7KfQTEQZS8bLJ5XwG2k2Zr0Zs2hIqQbPIBVSlVkLey-gdSqWRNr_ESSpyRxQ_zmIhQtp276-qdyg0t6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYndjbzwheDtt_WpDKW9g3ZEDC94tJzFwFmY3aJX1NaSN9j4HRq-mC7mqCr96KFVCdS7bP9U3fR6j0RI9AEU3DEWUx8rW9pqsOenn81YFTktHDEkiWD1vbeFQg0yJ3EjI3W9awVDwzUmGKr9vFNNKiuWmICkzgo36KXPt97yvu0jcnUBIwiSL-ber3CimatC31qk1zePp6wvBJWSbRyR9_2H3eWF8OXwgR90m8SxD7GT4OMI6jbBELKVc8kHb0gBb_EBfLJ6xjetMY0DKZPo_e53DlOd6v6tyJHRVK_LNJAPeeeKyT_m9bamq_AfTGCaAr6m1y1u03yQZ3O1OLvDGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqcxwhsuX9WwRQiG9Mik0LhUvKdIy2hC0QdghMJg9o6j5GeyA6L5AEhx8uDY4lztduQDtGckRt7drcAci6r_GREF6nIUD1_syBPuKLoxpP1PKgyVoFB53NRQ3raweSrffhZOcSCtRy6nxpYQ5-jWNjCHsgn8J5b1ZP6avET1sjrnpnkHqD09dpMVGt3II10P9oWheFyZN2o0UKosH9GaMGQ1Dt1LlbtbNJaa6qkP62GM73iZmKtcssGrVg0IRIo_a4nY05uP-oGd2MVxwqF6CKx1Wd4qngbUtlKxjnghfx3YCCgh1YNzWx3ohiRchpNhk6bW-kw3ED_ooRESLsIUnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnlQ90SReYH44uKhoUmjvSdUNFDF60Z8YVenuU19jVxHd8fN0K9UM8ZjqOHQjECD3x8v2CEFm7Mb96jHbwFD0TSDwFLJfIA1_EVl1csE7KNVlkg1FxWlB9cJ77lIXfdYfXCyU0n34cY4z6BThfc7LocWIcaH3GU3EwU5UZRiOUJWDIpz35Lfc9RYMbxeKiin7keK_4ZhffoEl-7dUP4OOWym9Qx2UUuN1OJYAv-wJJjFAg28mksGlW2tuySQzsDNP4VmzB4v3dJVGTBtgS0WHK6aMh6B2zfDyb0vljYa-mPED4fJIaJUGsPn9t6aN3B9awn_xwe-R9pNTB1TFDGamA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-khlH1XJba4nI4aMLQTgWL-Ygy1GlLfXitfg3VaXuYdxjOawkeDBsULZ3O0ANRBdH8iIsbFOnnrv1upsrNFRjBYtVjtIIGKCI8L04HRiBOWau9z-ZQKCxy3mlXnKu1CgrRDZAt3Dq24xp5FbAmL6VSJuoPe4pmNn0TacgqxXgACayznfa8cz5bPYPEU9VNqoUbn6SlOdmuqlcrlFU3bkUeEXX0bw_j3Ec50hw7h34FXd6XHpCXI3YvqDYpl1tdtPXRJWAm-851Cd9tP8xmS_v_X6AdDNDQVvPSCrdDSBIP89JLQfECf-8CVIwfvAlKGDSVllBQRH7_D9c5g5ANGQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daoIw8i9VWGoQ2MHrpqhD5ERuTMcS3Z95bQ3i_umXpHNLvoxyJT-xMGI-ZmhlNSuwbMLRsimgCMJ-U9kxCAqoC9XzRLnNQZU4p8JM9mo8emfXOFCULTM0erhkjOwG2h2uAfIom8xVF_QJ5CkVkbdBRmXPm6oquwTx2F_0tVsyGCh6a5WqX7w6uQ7m7sNVItr9qecDdWobGcRkHTArSCvZ4nCv3C8SRY16z7o-fniCoKx9IZJ8yAbFCmAwm7BK4Ew5g2EkChoxaoWi6Uwhtz7CG9hvPm0JIskYopT9wfA79qXRruG7Db-j2ueOIsV0X-3H2OyApfQsBNV_-br21ptfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_dvB3G2fosZUUJBW9Yy0vgk0QOs2be5-PMd0pFNiEifrSc9sq2FaIZPaT9pyFxxjPGOd_SbT-fL9Q4zJtAO_wrLyggokctAgYO8YdRwbksjzSmvll2GztXJOj8VQs4LwmcIfSoWMVHqFl1D3-KwUvzB-5qk6Sr6agTH0KmVBVOhnktStPNHmYTXkWyvMxYoKHh5IXLOORQfEKm6606OuDROfaMH3JNhPx5nbKWzsyeCSW1gdqJRyI6xizfceuSxx0f_fBtkuJSp_HqjIghBq2qvWi1Kfnguy5D0z0XQjKBlTc8sEK9cthPdUNe6SOpn0VViyfWmLNEnk_bXpBqTZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrzStfvxdgMiUFt24rw0XWr044JDhMbW6zQTaprQYON-3XGBWnflLGvH1HuyqtozDqngbzRDSfm-JaeCwRf9MOHriZvYIMfiHPGxLxfa_Nu_QBIgYb7vFVFrjKRVtdlM7Ezpzd5fD1kQu2u2h1jhhG85F6-Y1U8D2ferv-sayjJWYZNoBFa1whrIT57zuVMZj1NG8Jx2Lez7GlMHdnG6JEvClGXpC6xyP401qnKHkJywHxQhs5bKlRvbEXh6Ns1GaieOFYiuTr4DR7cHMORituhLlMEj0L6XGp9Y4N3Xs7GtFCuLz5ixZO_bOg5Zq5gAQ7DQJF_HPzShmpMvIf5zag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FL0urOftxH2NFkSFT-jgSZyKKgcldnH1bvY58316LhxqDHlfHL8NGSJE-fvCle8tOHnDHKc3oHEwZMKMbaDTJKkfjlBhKVfDlgQB0z9Epi9YP1_g5_DylBhBgNiKv_iAuAIEsPZbNYvWH7gNqoYbnb9roAYCOVq7PQDtm9dlFuPHjAhRzMH2E7nuVSvJjdveS3WdpE1MCACkjrYOt3DJ8lUSutig2H5CAjexTDpXgxkNaGorKmqIOMj8oRsIK40MwvaipWm5CPdo-jnc23ETfuwUEkFNnSDp2gx2xcsw62E6KORAOIQd35BuiEb-CBBiD0amdGblrevgK7m2jqMlNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcZErT-p3ihyOwAl-i4lGx8X1idf1BcDRKKVe3dhl53ZOP8LQSUyt5Cln5XSYtQBi_7lDDWSCuU1v5RboiQrjiyVWsBeiXuYsjnAMWI2-7k7OlSTOF3C2Zb7QKK9ocJyd-UDuUiEgFrt9wL4GqnWZgY4gG7O0bKvtTL7tNM07cebAxCGJ87EqVr7zW-Bg_nSlhoF_DB14UYH77InBwIB4ZBzuvsA3EyLDzVrvNKAFRCP-hjlO3sKRt8odzqVNW8NevIiKwVgsRWmdUaqFsxuQVbvtv1FZEOb0zrPyTp12k3XWBShcXxP4bqLejFcv0tlupukdY-J09apEAhtp549VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nK3f2HJrPJL5hf_EwCQxpywDZkp0WoUsP-Nh6G4oUh1T79xsPg5tXKKxsyZw3vue0ilrDS7zlGD7XtJVauuIOp99Vai6yrztsUFbTBVIFh0xPG0HJjzOqd99bWiuuNiE_LWIkE_vbdSSqC0lTcS-RsbPoJYh0RnZxhzTGUSx-i6kDJbRA7-7Ke6plGpsYR2qn8Gj-rEuEmsapsKmZAepUI5uDYUHZJMQfXlBi4uO5lnD5yR2YeOXNITCah2w3v0R2XJJDCM5wXgmSHlFjE2LC0r8RPy8F3HHt2RJapYsqmpOiqH1a7GU4UNujTh5iT05m6UrzJsUKfm1PKlqP0KPFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O59Pxbut6A-XNjNM0XXeTNAoV-RARxs3_qvLIGc-vI2Mhh-g0oGrmdlLLQva_yDByGdMBfxruB9OOTG3Cghi391OypQFYwuu2mvr9EqIECBxJzGjsqNauuAJ_QOL4yaJbSawucP_6ymFmkKC2m9DvnbHNJkjB17njs7f4f6YBk1ksPQ5Ha7pnUqH8EOScfabLY3vuW_nvlLgptnWDMg_dYHaFSNVgfoRx4niOZSK-wwMsoVyY25n1DC1pAXxGIFVEhr4uPLU6n96f5y4_GtFdz4_QQCNK7_w-czfawthcccH1qTVBBj1d74c7-4PJ8y7BdTk7IULxmEnQJPkXQhboQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=bOt0ghC8X1Np-JiQyiI4O7p2PrSJG-1JIrtShz1fI9qEPXUjvP7xl27ia50Ohofcsk7BF2ubzsI7g8Nlr-hK_HKvZ8ezWB-Hzm2oVwPcNzwxWgT1CrBFCIlo-fbpVMUFJ4HTRm7eoyyvfGuhjqtaRHmswoJ4lzUnLr6ymvjRQHJZJqt6K2dL33-zRkb7nD2A62kKyxrSAIy6Q2VpUSzXK6WUx0Hl9O5Uuee04PlIdVkTC17hiycM8OehSwqvbXdHl5JayqhxwMNxyjRPtoAw3BY1fDgiIveYqJATQpAZEi02EI80RiJtmcd1mpGHy6OH1MgONFKJ0DbW0YB3Kz3QBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=bOt0ghC8X1Np-JiQyiI4O7p2PrSJG-1JIrtShz1fI9qEPXUjvP7xl27ia50Ohofcsk7BF2ubzsI7g8Nlr-hK_HKvZ8ezWB-Hzm2oVwPcNzwxWgT1CrBFCIlo-fbpVMUFJ4HTRm7eoyyvfGuhjqtaRHmswoJ4lzUnLr6ymvjRQHJZJqt6K2dL33-zRkb7nD2A62kKyxrSAIy6Q2VpUSzXK6WUx0Hl9O5Uuee04PlIdVkTC17hiycM8OehSwqvbXdHl5JayqhxwMNxyjRPtoAw3BY1fDgiIveYqJATQpAZEi02EI80RiJtmcd1mpGHy6OH1MgONFKJ0DbW0YB3Kz3QBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3rDGxu9NplS8UPzFBjBikrB9tFGT6qQ0_BPjFD2lY_FCFMgRcJkoumzLT_fSY3DojvoblueCJbfpXImQlrnyiusnwXEI6Tw-R83pSQpBUSwwCulI1j9aTdsppkCvSgJyRuYhMwy8wZqI4TfmqLJyWUYS9yj57AeEtvI0-AGlFOIQkhGkcuYoxIiY1zZE0OtFGz94m4Dgill0Jy8U5TqTcELwQZPHDlLG95b3ydw1mjY8EI1pM-FGCF83JmgsLNih7KXYFB8PaGJO4ca9xMIp41Tmdj1LmKZd0x-V3qOg_AqvFGJ7XcOyo5BFos9M-cbN_K2iSoGOGHHYDj0l0wjVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuzGZ1T1iHw8cK9NPcgxkqOLsz4xRVY9veQNG9TXAkjt4UKucLVQJO87jiI0uyEEMtK5-SF4YRCO9ZtUoMa7hU5APDwIHNxBjAW_oESy-ncwmA35GIsSANiQzTHteyPuNY50i4ww8s-GM_Nn4L1LbvhVdKi8yc2f8xmZYILTGhYbK-E4Uz7-XBi9IluZEF_Y9tyniSS9e9Ao0LmI2Y_wXUw0_0BzjwksZikzPJvOcC6wKB_aYqkWcLQZvUKuLIeDtuq5knLbhrzm6QjBjqX3LhW0Jg4kq-zdRdWIEpsEYP-Uph4ywhed6uYHgkR-B64lcGUIjLMVRH0hvvldqiodkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtolkN1NeHcz_JZFBhLvE9JQ3uNrCA93gu0nE16Yc24wwQXGShggg-MvwqEsNQ6Ogv2TvNjzhRUox8KuS-ytbNZz71O883kENmeklTU8CbfdHpLvQK_IdRytyrtPtir4DbvALzx8EYdUsuzwcQaunIYJ_sgItG5lqCufIkWuCCWtPE-psiMYsbMOKchPls6wU00W6HKDhbBZsuk4_pgoX0w_AWNq-t6eEM_0VsWOcCQjacUVZi5upqpoDv5X6zhwYa2Ok7IHHRAXjel_RvOEumV96HiGczTA8D7f1MVrwnLwO-Doxqe7tS-2ioU443GiGJD3XHlnaJvZYAZW75HlPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IH7p1pYcJ39gPEP0Y5ZiK5-U1fRK4kM6SxQy1KcFR9UCaJeM58Baa7TpaK3GmbT_pL1mQ20cQDV1Vz9YIYtK9kR_8ckIonSrLk0j68vi6Fd-i086Qn_QY7M5vbhV2azQMPVAcp5VC2VzDC78CNYSaPs1TIkSF97AwT6vMtrRMQkkycVJ5f9z8aAo3bV3XDzW70-rXHcNnUqC7JjhtHziBzbdf5Pw5U287duoqIjC-ObUzzeKSUCcAiqK3VRW6zRojy0z3WQ47hSXspamyzBQalyZ5FXHU2MTBNtio59u6bC6Qyad-LQP6zp8QMCLuXkOC_hi80Yy577Ot5fo6sNnGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9cOwUnEy8ZSFgmRcHePhJVlr5xsnuXwuV4DfoaQ09_TnPFvlLuO2kCzmoLjFMTjGC7JbRkE5v2-jhoRNBWzOGILxdtZrgUwuoicclFN3WK5H4rX3M8X4VPBas4ibVS_Uwrs5bJFZ2Zi8XZ8j9cA9nugOdlTrCpffWVJ90XPHjTGwkPv030cY2Q9Xzqb9kB0x-nxeAPHLkG1uziKe2gCjpqVqk7sASl1gQaJS18qfPjWbexF_1e_2cByogvCkQJq4FVjgf_ppFbtWPa6Y1mJioohW0l8VmJ6S1wzodtdI7v0g_MV0Aba7f43FaraJYhzR1ApwFPjYY-iLrdJueK46A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcqA2gFnJpr1urBaKj4dvSb6VbUq5udmvI-bX-vMts3VOSmoS5nAGkyAlyzFlSZXieqH2HkpzOvUOt_Y8xZWs2LXTVRONFCjOTwZSZmf1Mnk5auj9lKQOWkAZTOuZKFHAiDaLw8N9Yr6lweBQxdbxi--QMQVQNIry8jQGFXBgA6NNgNXM7uVxYhdbGII5cZHk9Bco3mpzQStWdjFXlw6G2JJuzOoGxhu_5PyDq4DgozsVPu_Sc7FKE9Gv3vCOgci8bagGP_1FkEAOWOmPfUi-qdK71osFP4tbOxpNfBbDX6vgytYlVtvGls-i36NKjcArsbKU9zMH4WkjiOXLwyCLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soN3oLs9cvxCCTuqmt0GmcXLm3RCMEGmTC6DhkgzdK1xGXzpfJ2beLsFgs1qSEx0xfc6GKc31T5bS7WXlzQKwL416VciYoaEgwDltJ7bTmz3dSYnXNlO6r1BE9_HrsmNvQTt2aa1aYRrCO3IBzaEzD8bIWriELWWN78anNSSUJ2djFfGLCJS0QCHFKqLNC7E_4R-BDcL8p_UMbHYigr34CPsB9q5qPobgR7_vaZPNg_-1mD9d990EfiWKYeMbyRtHYiQFJ1E1rB0nRA4foIHp4p0phmoqw--U1ycJq0kmZi92AqoStiEIT4rqVdXCfFyd4b_dNMFcztZWH4SzUxV-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMeL1y13s5Vg2HZxHue-vi2fB90fHhEkei_gsiiTC1V-2ZslG9Ls64m8_Mhfortsc8tAMZSCvfoJW1sSQuBnOy7LNQLoPlYWkmmcx2Jz1dKLwtrOL9Pai1fF2EhRSATiWbawOi6krgaInaTiDCaFPpt4jKAl9LUhTWj0U9CCKkzu06svo_K7alnTS3VrJCc7eJJzkbCuUZHB7_isgzhru3RQujkBGjW-J3lyPN8Qlo6rvUuy_R8Nt2I-wUvQpy-tqbKGE986fRTmAHpV7SxNMRBG9_mgCWQPl3Uds8sJy4KrAMhO-QuBY-agVCxVOpKcMKGbhPbHQt9hWNllU3QPAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APWjPNi7qAgIy2yEs6bnaW54bSC9C67AjaOFKVOlfg-L6QvDN3q3395s1kPsnfVEM21yEULmmbpNWay3tGUbQfu1rrbyD3iwKDuzAsGEn8dPybYbg8z76SpN8Q87gohgYQbhq7dslWeIjh5FfVTY3z1YmVNWLdP6xMqEOWqyYUKUjThsgKkJ7w2TA6UKTYgZAn0E70Gc7iysFCtFgHtdhFydze3pSIlKrBCOhd1bwNE8J1dMk0eRN8z7Br_zwEKog8yjxYIG6CbRTUqKaS1eyrr-XIOML4K6Zq0CNSnPHnBKFRFRx52HLOq4NNEKd9jI0kWwZkFHD1tWWGqa6nq1oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtbfffTqK7GuAxyNRBdCfTIi_RLLMLY2P_SYs2HDGQicQJh-IvnxxVd66l130haKQG2MmdfzZjnDd9MWdYzlFqXB-IY5z4gotKvTQV3O1bgK05oxFTSVzuLIdPjS1wd4l9qUz0OkLhnSGBMi54bXXDer-R98ZBNcUW6txNc1wfBNfv92wqjv_oolpNy_mqr3w25c6_PcVFY0dVkKGS51XhYeIImEcNwzVpFT0GNiV_Az2Un7Ez6Rce8enDHzEZ-ajIjEK8MGauvGbm6iW-NO1zb41yD7Y26rmLH5cgwZmvkptDpHLIuPA8yyEAuPbmyRDQNElAcd6nHx_iAjcjYVMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4FFy2rxeMabK1V9WgStkSu_cON9YnNHxztzJMClpiP5lR_A5QsrJYPQctJb-dYlPXPyl7yu251-oU5gJi7wgejnhdShQbog00P9Og4pHUim6Lfdxid-ywwAVGnfBKK5QgthwYUncvXByS00ngUHMgtbKfm2NNiOpk9R3HySoDP5LLnnyp7H-JY2vRMNVJDO94lOQYed080fcFrs636JHbw5zbfZJ33NN_wm_G-MCqWAXjCnmSQiSW4lDsPysYX_ZSIkMFD6ZaNYdk_DwmR32HP2T9jkJQFKelt94cJQ9SiMtGjBdiy8s1PfeFVaLM6ukdufdfTmIpTcF5xkXnL5Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nP69GoS-vTAobYcvDddWx8wO0FGq5yYJqccmm1-IZPVYvASdYiJIn2boXIc5i2WcNPEaongqUtiYGlE94MIHY1B9rUGoTxmTI7W4oqRbb3jbPk91e3IuRYlhyomGMCMQxs_KmLxaFVXbRa6g2cMeD2rijwVF5B-odYN5SugONsH3I80Cv7LAQSuG15JU1cJ5fIfHU2PqA-_xsqPjUFbzozeXdtlE4Rkoui0E7oQSkM2d2KoI9PpRCYBzu5-qhwtClGweDmsJXlIQGyXFHJ1CW7OyIZYAhrv9DxAO7xaNHROTJn6Giut1N-yBH53ugLt0gwxxS76mrYla9X9cjbrIUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkxUF32t5HcvNrQY_6bxVCIR6N0isl7NCEuCXXrB2CGYE7aQEYRs5t_0AY9gSMOc2LOXJAnhax2i2SpK04W4SP-yAqmaKXqp4Qqk9TEMCaMaZwovWS9uXVD0qPbh5dIwvvcd0nudp7gbQVRFECuxUA1QrFH1CRjWZKabcsZn44eO-1MBKpymq0MBJ1jqkxLFCb8O7kknDPQ7fInQpT2fZWulJced_AlkAEhbpkKog82P-BeUZEqJNTKXmI5RZgydENeSr3TJc9hsvqtyYZ2KVyftW1_n6FrTFnB5z5sK7PE5hMZQUPC77uhv6Tqnr-7sv_1ei3F7ChIC_E5-LFYDFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwL1Bz6oPSp4hl8nabDbKcpie989kPfjtUmWiZbYycZdVOdO1tBfDLKHO_DLn9stHnYPZDfwrnWYX4TLyp_RGi_Hbl97ELL0eJAyaKVAD51vjC4bD8WhyDYG4zp0h4UlOTeZ4b7kamZx2w_PobzImmYJFWvxugjCt2qyjZ_NDm_ZsEUp4jPJgh4np-QxPDHSmMRPO2AUFpeEuAhiTpb6a_wDpIy1VAWBPyz6okNwwfWF1CpeHml933pFyXIM5w9jJZw342RfA7V2BHF7pw4eQac2-0CM7VdI-x4bAisoV9zOb51xBnB0k7OjYVyst2HHaMlz7FKR12mmoOjBdlciBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oieikhsais9ik-r-XzKFkm83V5qEOkPGO2CM8PTJrjMUJ2yvr8EXqL-6cU3FnWPorqN9wnECJhx7QXUxW8PK_zTPwRATidgpA9lyRIVNFqWfYyhiqrrLIS7TOVFCrTPqsXM_z4faXNwu55O9jOsJmKV09a8BfKCSPAX1A3p_DWJLkAI1DpPFQWNiLDlStaNYwi71IoF3dwBqXbqJUKSHJ-pREjtxLrc6HiPje0mcNth4CSrHYLnUWfiNAq4h4AR0w8cufbHPF9n5zxmWMi3RFhJn4CTyJ1bV7H3VLn-ArxvjUVYf6t4OcZp1TK60TLXfrColmSzDxgrAqI29lLRfYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkgVRn90H1vkhKLqIA89KbtcbYCVN3xorWqOMZ5cH3KtZIOguNeU-v7E8O0O1khdIq6eWMo2uaicenNzIVMwAIvxtHbrzGv7nKPVMHCQnuMrsLxBdK83_r5DfgFPBui6UPfrRYz7VXa1VvDrghbEiCb726GBwfoziwaRMskBj0Y7dUwMxzFV4ziBTmGu9B9tZ3ELBIOwEo3HhZHxvrxh4zQDkPK0TvjLTftDhGpfRxA9rf5sxszNKw2VO0R_XIlOtjIWQku73faoIDRcpkTeHVpwXwpRoFffQ6K9OVTHZs2PfG_gJ5NjfvjVEwR2Ryf9i9JAsgE-HLSKSPMM5c7ICQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGEWZ8b3DhAYmi8vXF3P7NcrhmmIilA_ifGOgHoyQt6TjSgwoKNUtZWyZ1jKlXD5DgCWLnlpNlOpfXoDXuQfH7_4WzxQeKz8bT1V3C9YQkWeWvMQcbdPYylET8HjLwfuCH52CKpTHSlOWkG3HlXvKCHSLO96oo_9KpyfslqT0NqHC_wr73-op3EGMHA8KM61Cqv7MvgJWaZqh56bIYAa3uCPS0LLieGSYE7PTCQ_mnGK9-p9aImvF5oIrLeRuxzKLD4N7QWqbRzpLcbZe_v4krbu1Ia3FyCjTjUnuXSavl9p0Yi8PFusWORvmXig6Pd3-Keek79HotNLpjCARENBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOs93bCcKPBg-vAJZh3svTwTV0TQdjtNL3l8SeayVzLzGgMifJnqdJfPtmsedWgZ_xtLbin2ncSSp0r8QB01xmsR14eNDI47cm1-11g_mMUkF0dK-Aiu_zFgchnhFFnn3-_5ZsCZ_rbW4y7EtyZ6g8GR5xFvj9ftgY9Et2t2i4ESOVH93mW5lsJmZuXXYdqdDNogU86Gh5bfK65Z9xQR5v2Ojbn5blKxXkRD644eH7k-6bh9VIUkNY6LChto6gaaAV2bX0Rv3IbQOlFyG_GzfGK0Lr-Cjl5MeQsC9VDdc88jATFgUZezFmDWLAnUG_BI1yzYUcWlKjyOvJJ6TX4Kzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n18ScAJebJwPfhZG5SrzwlU94-WuRruZ63D0UmIEkMI6d_wvLt5KSN_uZ9w233kXaR4xsy_aALCMqENF5EY5NVMivUwuKZTjlHo6gc2e3d37qBdtT3Eb9mDzXBGsTOfqH1l053A1Mi0KQ6kftLD8P0c7XMyFjFCA2pUU_XmAzbqhH-NHCny4rNk0LkQDRc98ekpHQSJIoz9sTj_jcpTTchLgxpKAZSL1clM4xchH2pauZV_68kCuzgMpYIJlUzfrN1nZVXVPc8h6-P5x-VzKb8GKZKQe34_yCF8IvvUmZu4Aou-AEgcMKibOFyR0NxcjUQL1NbVDadZVADM-qLNJuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMioO3efOhpb4YPJCX8OuO-vJikUI9rP6i90pwBdUXl_1Ltb_vvh1_aks3DYuBC2SgkKOmDZtwQqaD5VpO6EaG4Q2GW4_NvPO3CBv-zE1GMk8eMQ8GtRn2Nnx2yNc9Up5hscpPH8bhQIzkQ1F8DB3Qxtn8XRaMLNtFvZSUzrhkg7dF04SvXbbx_rAjq_XhzSUCkm53jmP8v5IG1s22YAa5rRzU5WJrui2FIJGEl4DAUVn68iAVNsDhYU4AztDaHRqxE_15J_IqzOg4AHOwrId-KdOxsQ9mpAEhvg9RJXON4nGCeGaC0dBhm8IdNugOXpUbEEu0kTkbk0SJfIbQ5Pfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxIjmgzWT8BatS_U04mpfxsgE6PXXXp3CfhjqkrD8OIhZqx-xgzyZ2X62TlWRnERd3E63kA2Tzxv3owfj2qfoZoDhdGOLCdb-aGicxuX_sRwxizplo3kORRO3u588KJMK1vA6b3vzVy6x0dEO2T5PTBJaKDhZcmghAhAz7W4KPTD3TBBkMcAFR8HCp2DQsdNZIMq5U6YRuaRs-nApo2QBqHfwRlTZ8LolktDFbzTcEAfsFd4ZGmI_EY7fimxWu_XRczZw4UBw0siYEtI_-7PCnXzHC_ORgD7fAj4y8XdUjvqc-t6tfny8XHnmfI5h6ueUsmDy4JEFZIR3fWuHWrBpQ.jpg" alt="photo" loading="lazy"/></div>
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
