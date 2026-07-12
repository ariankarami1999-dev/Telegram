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
<img src="https://cdn4.telesco.pe/file/UVE4kDOR6uh7OvvoDUfGIXEaULS_ae5vGc8mSAzYrelbWk1gt4_Lc4dK_Rr_yDCzocEo25LoQyOLjVAyU1R35VACJl6sb49IaOqOPRmvPtjufM001mHfI4nK3wWTiflKjiaoGUNTZ-sVu5ACHdu2zJGmuB0w6Du8iZLx7Pr79RTH5lxF9y6BMNvDQIio6Fok9ztIyK4CygvczkAORQVu7jQ-vToGBQcbPCuJdLrFFkeXGu98o74J3R-RNXoTaAuEulT9JcrkIomqPTiVADI7p5KjSJstfgF9lzQNvi4Ain8vB2HrVO7Yd-hS5UOXTyr8aqVynL-fiCHC5jrWiE0Zsw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 435K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 21:22:18</div>
<hr>

<div class="tg-post" id="msg-25544">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d86d8e16.mp4?token=FXbRifL0KOPWq5uHkEHy-8OFFDTpY4u0UPZZgmx3fCzcUYwGJ2WVT_zCsPtiRxF3to-_lAFlJupS80ak_XwBYakL010KJ-iq4OXN7Zwrn9_W74hmmLjJESruQETaGqt09s8q53qY_kUplG4QBstfP4hN49q_kqnrECrNv1SqIagBqDDyAmsehbTwWXePbgB6S-8oDQi4W9Qrs6nxbSL4VlFRy3-mSwS9TWSEhHBIhYtTSQSWGeDsUg7qqhClfmf4fXjhQwfjje6JB2fbbUU430NVSnYeGvP54wkNLcDWu_y4xoB2D_HrVijC6fOAWpQsha-KCUATyUO3uZCj0_ao0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d86d8e16.mp4?token=FXbRifL0KOPWq5uHkEHy-8OFFDTpY4u0UPZZgmx3fCzcUYwGJ2WVT_zCsPtiRxF3to-_lAFlJupS80ak_XwBYakL010KJ-iq4OXN7Zwrn9_W74hmmLjJESruQETaGqt09s8q53qY_kUplG4QBstfP4hN49q_kqnrECrNv1SqIagBqDDyAmsehbTwWXePbgB6S-8oDQi4W9Qrs6nxbSL4VlFRy3-mSwS9TWSEhHBIhYtTSQSWGeDsUg7qqhClfmf4fXjhQwfjje6JB2fbbUU430NVSnYeGvP54wkNLcDWu_y4xoB2D_HrVijC6fOAWpQsha-KCUATyUO3uZCj0_ao0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌بامداد‌فردا؛از نبرد انگلیس مقابل وایکینگ‌ها تا جدال مسی و یارانش با سوئیس
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/persiana_Soccer/25544" target="_blank">📅 21:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25543">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY2FGKQBNHpJtxLsMxLq5N_D5mc7yhgOCexPviESN0L5wZ7h568TXZPn5OefyXglZRtmBmPrQlOzFKdeWgvqHuBj80PkvuECVAVhXoxfucWq_uCRvxK4DVz6iHuEWBBZ1daJZfr-6OpXwfmNphgiljyLke0AQzBCgvR_4_TpbGIWCgkXorMy430eIj2eYyJnfdjwtq3j6MyRdvN75C2roHGfMhGjZPCq0t_gwC231tavb-jB-rnQO-kvND6u5TvZ19ZvHTMQs31UEK0Swi4tWbKcc75dKb_rmCdyPwaopX-CxG9OfKVo45JM7kxh4MrSikXdGIEil7rwC1UyNqpgTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طوری‌که سورلوث در بازی با انگلیس؛ نروژی‌ هارو به فنا داد؛ وایکینگ فن‌ها عکس رو میفهمن. برگ‌های هالند از خودخواهی سورلوث ریخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/25543" target="_blank">📅 20:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25542">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlta18X9RDKHdT5ctvHdXHZJeYtW1mCawL4hLOjuDMo9LApgJ4k5gLa84SeBnniJ9I-lN8s_D9klpmH_va1ER2us0oGdGDhLOxNdD_0eISvqduxgftTuMRhZxRcUcbeMuVmM8wtDIlWLdyz_cHnZVCi3mEyxBKBXYKjd7lmPHY24eTy-sP0ivYXHe1e3UEz10Sysl9XjJ2puRxa9lRorR7WeI_LNKgH-asqqyYATz8B9HB7ccDDWc0vlTbB_65gqCc6pYayqLIt2UFtrHzrGJrq4WSZv-Q9GvbKhGdhDJWsDZT7pfaV2OPyGFmArX0WRQwxdZaj_JtA0ivg4CeeHSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو انتقال مهم امروز؛
آرسنال 20 میلیون یورو گرفت‌و لئاندرو تروسارد روبه‌بشیکتاش‌داد و مارکوس لئوناردو ستاره الهلال هم رفت آژاکس؛ هلندی‌ها بابت این انتقال 17.5 میلیون یورو به الهلالی‌ها دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/25542" target="_blank">📅 20:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25541">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/104d086276.mp4?token=JLoAyFFCLKXF6R5VT_H7rVSTEVq1IlFpLoCoN59_AGL1LdBgZkqralzYqGqvRpNZ1kJmCMaQfoEzMaRy1u8mX_KcjH_FeYVKmb0u7Hj3CCjRgZCDbzffa2fcBRm0w8sRXVj87vT-XgHo8yv4MaixFMpji5ktMeBimJocaBN_4GlhQEB7I5bdfv8yB42Zpp1hgoHGv7bjgpfEVgxZ8RhJXtv0PBEV7DTL43iGW0dsab7AGQUMaVbxLRF1cl9ErJ9TT8z_rZ--f5W_iV_6KPqzta3wI9mnZ86yUYi866OvpPCy-0-bUfRqS88mGU9HoKDGuIe4JftEo-pOH4ymx4R7Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/104d086276.mp4?token=JLoAyFFCLKXF6R5VT_H7rVSTEVq1IlFpLoCoN59_AGL1LdBgZkqralzYqGqvRpNZ1kJmCMaQfoEzMaRy1u8mX_KcjH_FeYVKmb0u7Hj3CCjRgZCDbzffa2fcBRm0w8sRXVj87vT-XgHo8yv4MaixFMpji5ktMeBimJocaBN_4GlhQEB7I5bdfv8yB42Zpp1hgoHGv7bjgpfEVgxZ8RhJXtv0PBEV7DTL43iGW0dsab7AGQUMaVbxLRF1cl9ErJ9TT8z_rZ--f5W_iV_6KPqzta3wI9mnZ86yUYi866OvpPCy-0-bUfRqS88mGU9HoKDGuIe4JftEo-pOH4ymx4R7Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کنایه جواد خیابانی به قلعه نویی و کادرفنی تیم ملی به‌دلیل‌عملکرد ضعیف در جام جهانی: فکر کردی منم عین مربیای تیم‌ملی‌ام که 180 میلیارد بگیرم؟
‼️
هومن‌افاضلی‌خیلی‌جدی‌داره میگه فکر میکردیم که میتونیم تا فینال جام جهانی 2026 پیش بریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/25541" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25539">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2qRFCsvvmoXcPcpaOteUXJB0Q86EKl_YlbmeYtyuzQJsWu97wxWzFRnE6KeclpDNEFzrJDMRUlU82eXvi7Jjc2jDSRp748RqKSLWz20jcDs61OQXEwO7hOcbAqZhdVwbXQ381Vu4FrjBFTLejA1OYrK7yceK7KKXdoD0Y7d7bpAUzHNBBzK2PHP3hCX0TA13FE9AUGobxhS4J6t7EnkhBTNi9zO1oUIqcBBXqEGxvENbQ-X2GLNcjYIrSuVguWwf3FTZV8IOSUIdmGMxRyZsHUIffIHIhHZG9apIkP8TogATGOK2eIS5zUqOaqacXDHAo_fXXVxlb7j1J1i6BmiZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/25539" target="_blank">📅 19:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25538">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmHK0Nv7Ar_sqCUtuG_HRUv3m15unE4eR_WEV5g7n0uIfnA-sDTKa6WHlNsx_h9i9q14YFS5UEExjZIBddGeE_Pl_j7QzIThpn5r7JRi3D1Lre-X2mhXc4x4yGjb2kIjA-C_QCIQ964k930p17jaD9MEbE2DjxwmuXqxROOsmJ0shmsAyjA0-alvQZJ07uV1gyXV2P0Ar6Vak4D6Ar6QciLHG4tJ9waVdzO9mZC7tHXnBTO00Uswo4JSLgVORZkc8RPLcol6CSqCyWdHBQogKlDQPSRjkGuqCQTzB6VNcPIvTXLq_YSmDuQI_4TpggPiH2CZcSNNWVScqttQlkV4nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینی در سپاهان موندنی شد.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/25538" target="_blank">📅 19:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25537">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QT8lysGTSIcySF5T6-moibako0eIPYYtwpqzqet3cdYaa2vsy2jSXd1Qy2b1W6nu8e1RxEmjBLkM4z03OTKHhV5E0yjt5X9Tpvy_Pkd39VvueivwqYCAy23e_4DVSaQ9PFXBYMwBwoST2fGlJ_x02KTI4-Q3JKGtes8xJtEtC7c5612f7bALddACDLvs3Ei-UvKgYvylBbGG2QTmF1-pUo8OBzG4_VYe1Y0oJdCzph3giM43Nl2iWurdlFb3xrkC5gV_hzK3pG5F5j70UTfhFdj0hSSI94DD11ecL91xVcLAiZc-nL2LGD5DDf3dVtKV2ErkufsM-Xfd1ylirzMR9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/25537" target="_blank">📅 19:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25536">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146af45fcc.mp4?token=BlNTkQsQs-M7BMVSqdtSnsr8uVIWOqJTom4bHGu1nx_XjpFyeO3lMEMq_U7IY8TCZvjFWs0mqa7XbCTJwNxdI_0AFyFAL6LfSeTCBwWoewDhkZqmHXNDho0eeqerL92q8yNz9_Vjx5CYcSezG13W4RX53Fzy08Zc-fV7yk_4SI-SeVISyBWNXMknzgkDuJpIujA-9CuG27_NTd3mzfP725L9Hp5US0e0zO0xOi-_IB2jqYU7MvaVjJzl0eznh5RWoPA9MT_jyEIDOjx6s2GF1SGC6_Cbwvp_69T2_WlIwxpvoaC-hMSTBLFpioVfWXptq7INoaAVwM-xBZHA4FNcwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146af45fcc.mp4?token=BlNTkQsQs-M7BMVSqdtSnsr8uVIWOqJTom4bHGu1nx_XjpFyeO3lMEMq_U7IY8TCZvjFWs0mqa7XbCTJwNxdI_0AFyFAL6LfSeTCBwWoewDhkZqmHXNDho0eeqerL92q8yNz9_Vjx5CYcSezG13W4RX53Fzy08Zc-fV7yk_4SI-SeVISyBWNXMknzgkDuJpIujA-9CuG27_NTd3mzfP725L9Hp5US0e0zO0xOi-_IB2jqYU7MvaVjJzl0eznh5RWoPA9MT_jyEIDOjx6s2GF1SGC6_Cbwvp_69T2_WlIwxpvoaC-hMSTBLFpioVfWXptq7INoaAVwM-xBZHA4FNcwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلینگهام ستاره انگلیس در پایان دیدار با نروژ:
مادرم یه هفته‌کامل بهم میگفت مراقب زبونت باش، نه فحش بده، نه به‌داور گیر بده که کارت زرد نگیری. آخرش هم مثل همیشه حرف مادرم اجرا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/25536" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25534">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHVBM1Osdcs32c4gYd1_TwttiU6nhkWtAYJQXR2Tam3TbXnVrQpT7ulbaSuhewIEBYKtYShD4cmUX7HTjM2Gl-fZ0pSePrr-Uy_StuPWecrilG2FDR9AMEyMJ3r2V0Ix0KLehRFYZYt7N0Bxg1NgweRN7d_dECKbHA-sGC2ZuTwly0lkYNXcPLFmRI7tuso0nJ0L_Aj2uBVry2c6ELY107sJtMpq--Bx0dVpIXHCeG5gjYtCEydIPc-mOWokGdiorjzjwi8V0HzZtpqELgJZWYDS91rwnvAe4mMikQ-lKodgjn0DJWXrXOX3EwgUZxLiV1biAyAmqI5xUFDXgPc62Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوسمار ویرا سرمربی‌سابق‌پرسپولیس در انتخابی عجیب با عقد قراردادی بعنوان سرمربی جدید به دوا یونایتدبنتن انتخاب‌شد. تیم‌یونایتد بنتن فصل گذشته درلیگ 18 تیمی اندونزی‌رتبه 7ام راکسب کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/25534" target="_blank">📅 19:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25533">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iyi03NHvRJKZWB8-FK86aXpbipTzw2obiaQerUYCwKWF_PT4sw4072m0MDWEWT150XK31QLz2s7YeiOn4uys3_QllsWU2cGkFelUw0X3pz0QIxay0F9D5a3z5mPrSK4XGXyT5_Dv7scMrVRMiCKkXTyyQIdp50ks76EXkCYI9QwI4KF9R0O0mNXxpuOOb0R7Ws7bWlAc-2OeXcZq_NU6U6CBtBSC39zr6unzb5LhQ9hgUXGeYtKpR0hcLbMhfHtn_Xoz4O2t8zmqXlVNXnZ-s5_eIBxHaxNUnCYF-Tx-rzn_JRFPQNqma5u6vVvxR786VWPYzJrt3M1z77Gtxkf29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برترین گلر های فعلی فوتبال جهان که بیشترین فالور رو دراینستاگرام‌دارند؛وزینیا بادرخشش در تنها یک بازی‌مقابل‌اسپانیانزدیک 16 میلیون فالور گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/25533" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25531">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nm4dKF9netNceUd1VQonlbmfyjr-FE8titpYNJ3BPLMOQlHxh043OXgcEZNnso8szDnNS92X4NbQ3X-26w2JH69VQiLNIpgRfZSJxFAfjz07nyDMt9Q8kVe0lYZx99E2bs7zsW5k5D57F3iTX9r3WQb_EoozphQ3kO4Ar0kgjj3EdL4GuRyBxRzAz6wjKyuQWbYaMGt6zP8v-seUHRujnBJgSlgDfchR26QEB2MdAY84lu3YGEvLQZ0NP50jrAYKC2iBIqS2aV5DEFlYcRa1UjlJ0NkcoVw3q5cCVfiY2oYUkEkNl1lIbMmUKbQuBD8frCtpNXoTrkAY-aD_pmG19A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec951e804.mp4?token=sqrRDSudeuhmXjY9ZIvXPAGWlr_JAYczpXmhgMWgi0kehHwZVzQbUaQgCiORt8sBV_ll9cDjur0hPh4EGxxgbs7ium4msfBGwTZn29HUaL1eJyEIzcLeCSRtF92gB6EIOTh8uodaIpx60kjygbyNVYoS_KUqZ62auRn_WVUVlf-ywRoykoJeefxnosoQ7_nXLeoJRfSNtZPj3DIp0ImbaAB7rJySyScrzFxQ9XQ-f0INmcLxLmGbT-iaQ7MLS4WKoXT-FfKn6XTHoDoTxoBOOq1x8siwQ3Y4VtIMabob7fR6gh2EiOLaWrE8DS51Zi8yFwtcEtIeiJD6OCTCT1aPcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec951e804.mp4?token=sqrRDSudeuhmXjY9ZIvXPAGWlr_JAYczpXmhgMWgi0kehHwZVzQbUaQgCiORt8sBV_ll9cDjur0hPh4EGxxgbs7ium4msfBGwTZn29HUaL1eJyEIzcLeCSRtF92gB6EIOTh8uodaIpx60kjygbyNVYoS_KUqZ62auRn_WVUVlf-ywRoykoJeefxnosoQ7_nXLeoJRfSNtZPj3DIp0ImbaAB7rJySyScrzFxQ9XQ-f0INmcLxLmGbT-iaQ7MLS4WKoXT-FfKn6XTHoDoTxoBOOq1x8siwQ3Y4VtIMabob7fR6gh2EiOLaWrE8DS51Zi8yFwtcEtIeiJD6OCTCT1aPcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/25531" target="_blank">📅 18:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25530">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2121b6e4e.mp4?token=hXTGJqEWJ4CmsAnXhFr30iXXUfqRXqVNzZTaiO747OOAVydX7PtpIvtJm8ft8o_nV7Fs4Jj3fQynLUsX3xDVMobqs3nbh0dM7gV-hFn4IWhI9hutV-b8AVA0Of2CD-CNGl7AGAYJavoCDLhrYctgpexwqmTqv7SGVto92ekdFzaAS2RTjBk0tC5yEz1NtmNv0dss5rQ1kW1Z30DrstzBJ2oEwprYPcnJEguZpgDMBkUAKuSkNZjozK2-7qigXhR_Tfg-Bb-NXQBA1GaR44t_346ZLcp8ZHegLTp-X6ayPFGN7pg-bs77RAlJzgkk0B3UDfY0tPgxZA9nHdZhGpXquQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2121b6e4e.mp4?token=hXTGJqEWJ4CmsAnXhFr30iXXUfqRXqVNzZTaiO747OOAVydX7PtpIvtJm8ft8o_nV7Fs4Jj3fQynLUsX3xDVMobqs3nbh0dM7gV-hFn4IWhI9hutV-b8AVA0Of2CD-CNGl7AGAYJavoCDLhrYctgpexwqmTqv7SGVto92ekdFzaAS2RTjBk0tC5yEz1NtmNv0dss5rQ1kW1Z30DrstzBJ2oEwprYPcnJEguZpgDMBkUAKuSkNZjozK2-7qigXhR_Tfg-Bb-NXQBA1GaR44t_346ZLcp8ZHegLTp-X6ayPFGN7pg-bs77RAlJzgkk0B3UDfY0tPgxZA9nHdZhGpXquQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسی تو نیمه اول با پینیرو داور پرتغالی بحثش شد دیشب: بامن‌درست‌صحبت‌کن، بی احترامی نکن. من باتومحترمانه‌صحبت‌میکنم تو هم باید همینکارو بکنی. انگار نمیدونی‌چجوری باید بابقیه حرف بزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/25530" target="_blank">📅 18:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25529">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=ZMoDFPWNraue4r34TJUFOlsuByTk_GU50R9p72Gc7s3nCaROU1fpuNrA2QYBSNGBi2QJLDI-KN7wYcwhRqHX_ooVSclZHXM7Vr2vsVZQD5OqcU3oK5KPl00KGOT9pjsJ4grt_AkUKE0a790b7Y9Gap-hThm75E3UOpvursLImaYtV3q4Yl4YTX6IM6CvX2FWoLqZx4egEaB3eSEur53WSUZql7Yms0m2fc9wXcF0-uGs-ri6R7U-11Lw8Bj0Xf7ok4HcpVn5rp0ScpsoMB6VQblWQKeMNI-cNax4xXxbvffYCZ0mUlYpMxSH3xu0Oze5PWDXq_rmwzgeMMmUUa43HTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=ZMoDFPWNraue4r34TJUFOlsuByTk_GU50R9p72Gc7s3nCaROU1fpuNrA2QYBSNGBi2QJLDI-KN7wYcwhRqHX_ooVSclZHXM7Vr2vsVZQD5OqcU3oK5KPl00KGOT9pjsJ4grt_AkUKE0a790b7Y9Gap-hThm75E3UOpvursLImaYtV3q4Yl4YTX6IM6CvX2FWoLqZx4egEaB3eSEur53WSUZql7Yms0m2fc9wXcF0-uGs-ri6R7U-11Lw8Bj0Xf7ok4HcpVn5rp0ScpsoMB6VQblWQKeMNI-cNax4xXxbvffYCZ0mUlYpMxSH3xu0Oze5PWDXq_rmwzgeMMmUUa43HTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیوزیبا از لحظاتی فان و با مزه لامین یامال و داداش کوچیکش که این روزها سوژه رسانه‌‌ها شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/25529" target="_blank">📅 18:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25528">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8eD4u8ga_x2Syi5_AyL3wlv7Akdxrwa2eKDzjJj1G1mMAHzeM3nbXc3zb8WqUO1vwkl9dP6qorm0sfKg2nqRwZzKDRbJRW2yXfx-1LnEXwF9aG5wdCj_vFhowSa8IH25c6x96Y-ZUarABPpLDL4G0brOKYod7JElOZG8eSdCiQP8GXycHL52sjKMPj9bk45HKBwjA9Snv8dprl3VjAV8fRNIRt_sJJ1cHfRNR3BrreB0smQluVGCPZluH1Qq96U7nMvgpx4znrK53dIpSwNJyYRpHRW5hJ9YRHVC-RjAUu2ToQoC0SbTwu2YkVBvwL73h0vojpY2nBEjKtZ9tjXjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخباردریافتی‌ پرشیانا از اصفهان؛
مدیریت‌ تیم سپاهان‌ با‌ حسین ابرقویی مدافع میانی 29 ساله باشگاه پرسپولیس مذاکرات مثبتی داشته و درصورتیکه حسین‌ابرقویی بتونه رضایت‌نامه اش رو از سرخپوشان بگیره راهی اصفهان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/25528" target="_blank">📅 18:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25527">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
تو یکی‌از خانوادهای‌عشایری یه دختر بچه حالش بد میشه، بعدمیبرنش‌بیمارستان تست میگیرن میبینن باردار شده؛ میپرسن کار کیه!؟ میگه پسرعموم، دعوا میشه بین خانوادهاشون؛ برادر دختره که بازم زیر سن قانونی بوده میزنه پسر عموش‌رو میکشه، میبرنشون دادگاه خانواده عموش…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/25527" target="_blank">📅 17:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25526">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZQumKjx26UpqqAOTYbfEpRrljlXPfesSi_6u0FN8efem4n7tiWGVTsyjb_64pb7tmzvxvSFbTEVgslZpd7OQ4nHes-Ji-_H2nilTVFLHrLsA8p-ZPXlWcnWTgoryQH9RJ2Z_KsKSGxng2RyJ2xm1MFdbHaP2UBBB_3Rp_XTqdBk1ev7rgIEru-a7gKXbp3ApAyxeIPCDF8KoSj2ciQGJUh6mILmEHCuxBvMDJ9ja-nvJpfckG4FJ3kyvja-K9zmBn-hsd1FeLBvo8sLruBiXinz3VNToOsQZ-dI-cKIvtNSwUjqhUARaON13ob0NLGhNG_0tNIJT928USBKTh1cCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تقویم
؛ پنج‌سال‌پیش درچنین‌روزایی؛
مدیریت باشگاه استقلال تهران هفته‌ای یک الی دو بار از سجاد شهباززاده مهاجم جدید خود رونمایی میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/25526" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25525">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C52JfnNMJoiqDi9hYNlFTyc-NvyWDmhKN7zusjb6FHnV2LhhfKbQ_lVGpJ48jzKn80VT2DI6PqXNogOeit81kck60UgoRYkxK2QJT4wYCYhExQUK56c3Q99htaSmzfqMijbPfZZXHybo5HVRF1PIIlW7luRll412J0rwHSwXomf5sKFbE-bSzhQxpMKlDyoehb2osfMnRh93-EUZNVjxta3N33v7ufVhAxiru15IxNK_lIAsaGuSM6AeE7Qc5ND2R1DxBfOW70ygSiN2YLpS5Ylg1ms5Ohj5017U2untuC8BuWzhsVhX1OzuE0Y0-6c2P7a5GZjiyyA9nl6nswMDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/25525" target="_blank">📅 17:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25524">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhaR5RRxBQakZE8NvFYjHMFZN4RrVkySacKs4JVcPc3iWgJVyG7kD9ACSKvi5kfNpUUTuztbCh3VadptPIVQ1_LqmSoWvV3MvjdTj5iHBKIWzrzesxEFRtxn9ZfOxlxrYEu2ISNz8XOndhgZLDfJ3DGjb582wC4jyBSC2k0l3uZ3QXgNfeuGEDwGzpRMd_mvyKB89Al1N3l52-Xmbc5PoKc5DfZMisLsYz6vlC_a_20_yayxaMkg5WXzTzbYO5Du-qJQDXesPmCKHdUAuWyL1neXj4o-D3N3yVMhu0vekMJNASW8h6bgFwZrx1d1tzG4wZpi9hCgohBJbWXcWdpwlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
عارف حاجی‌عیدی هافبک‌جنگنده سپاهان که مدنطر مهدی‌تارتار و پرسپولیس بود بامخالفت شدید محرم نوید کیا در جمع طلایی پوشان ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/25524" target="_blank">📅 17:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25523">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=dDP6Cj7FuGB04YixsAahLKYKoJs3OfSlCpOGHfdr9QX-LJlUEG4gGV6neDOryB5Acb47aZLO9FLHG0hRfOCi4MoyqMPLC5LeiUniY5i6kFD50x1KryVCguZEvaLAzhKLi6wk8gWHlhctXLI_w4JW0mhwiYDbnDD_kLjrSYU0U2BNW1mlX9tAEvFaLGDRYEKPJBAv9W7nI6r1XZeshtFP24pG72kf-2XYOVxwDAOW1ULhtEIhKXAI9An5PluacdQFiD6vSfwfDBGMLOKk3m9lr15NavnjT5BTfvUg9tipx3R_4ewJwHFjFfn9Nw9n9xp4wQajFbMfrceFftZXlT79oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=dDP6Cj7FuGB04YixsAahLKYKoJs3OfSlCpOGHfdr9QX-LJlUEG4gGV6neDOryB5Acb47aZLO9FLHG0hRfOCi4MoyqMPLC5LeiUniY5i6kFD50x1KryVCguZEvaLAzhKLi6wk8gWHlhctXLI_w4JW0mhwiYDbnDD_kLjrSYU0U2BNW1mlX9tAEvFaLGDRYEKPJBAv9W7nI6r1XZeshtFP24pG72kf-2XYOVxwDAOW1ULhtEIhKXAI9An5PluacdQFiD6vSfwfDBGMLOKk3m9lr15NavnjT5BTfvUg9tipx3R_4ewJwHFjFfn9Nw9n9xp4wQajFbMfrceFftZXlT79oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هومن‌افاضلی‌از کادرفنی تیم قلعه‌نویی:
شجاع پاهاش پرانتز برعکسه اگه پرانتزی بود پاهاش اون گل‌هم افساید نمیشد ما میرفتیم مرحله بعد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/25523" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25522">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=ZjagCP72b48UANjEJB9xTHjlhjUnqNGN7lnlq0UWLc1I3ZOn_cAm4bcYEdA7hbM7GuYOwo30UU0KYVPeHxFLI2elv_mDgKDWFj8xoOI7Xk7zjTZjdLHJIpOXkCBokKUvfITMqW28CAxqoGlx3hzHHKm_Npr6lmLixJavaC3hrSxG2xMAkECsTuoCEQq9gOc1YhF-oQamWwql5WTnN9g-Vm4T7-dL8VtdvgKx6WQtaH0hB82NBllzQmsGFH-D8xmZySl5cq-FqNF4TjULCewJF5jnTfHNu6E5GZSpPZnwmyPVjLji_NPeIziu3sI-h2uqjJ42Gt09wznZywI-SDfMdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=ZjagCP72b48UANjEJB9xTHjlhjUnqNGN7lnlq0UWLc1I3ZOn_cAm4bcYEdA7hbM7GuYOwo30UU0KYVPeHxFLI2elv_mDgKDWFj8xoOI7Xk7zjTZjdLHJIpOXkCBokKUvfITMqW28CAxqoGlx3hzHHKm_Npr6lmLixJavaC3hrSxG2xMAkECsTuoCEQq9gOc1YhF-oQamWwql5WTnN9g-Vm4T7-dL8VtdvgKx6WQtaH0hB82NBllzQmsGFH-D8xmZySl5cq-FqNF4TjULCewJF5jnTfHNu6E5GZSpPZnwmyPVjLji_NPeIziu3sI-h2uqjJ42Gt09wznZywI-SDfMdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل فردوسی پور
: آقای اژدهایی، خبرنگار صداوسیما وقتی‌صدتا موشک‌خوردیم و صدنفر آدم کشته شده ‌میاد میگه که همه چیز عادی است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/25522" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25521">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4009214e91.mp4?token=JJ68B73lD_DPtnowezEOUCtn9ne9gUioj_Z4_8KkaBj7z3XMb02us45e6WC2Mp7cCSkcrFECs9nMsb_REkZWCOb59oiXFhBB5U60pp0pwAblxOYjF15v0bTIPce2YRqHLLwq03dZ9KPQ3xtBD2VObFwns2biblw3ovXySNEYPag87DZ-K-FMuzsCm7JIUvtgAkjC3p-Z9xCVYBXDOyzEsoG7M6vrC2FXsK7emuxI8ywtODE-ncXJwJnXlp2XaGNY2541YP2ZLMSIkx8dJ2jMcMA_6fbvi5GuYHiHOvekb78rI3dFbRUoeLTd-8lQGZrqO4FmmKaOUFYy2rb5NxrSvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4009214e91.mp4?token=JJ68B73lD_DPtnowezEOUCtn9ne9gUioj_Z4_8KkaBj7z3XMb02us45e6WC2Mp7cCSkcrFECs9nMsb_REkZWCOb59oiXFhBB5U60pp0pwAblxOYjF15v0bTIPce2YRqHLLwq03dZ9KPQ3xtBD2VObFwns2biblw3ovXySNEYPag87DZ-K-FMuzsCm7JIUvtgAkjC3p-Z9xCVYBXDOyzEsoG7M6vrC2FXsK7emuxI8ywtODE-ncXJwJnXlp2XaGNY2541YP2ZLMSIkx8dJ2jMcMA_6fbvi5GuYHiHOvekb78rI3dFbRUoeLTd-8lQGZrqO4FmmKaOUFYy2rb5NxrSvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بازی های جذاااب
جام جهانی فوتبال
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
⚽️
🔥
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🌐
دانلود مستقیم اپلیکیشن اندروید
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای‌مطمئن و درکلاس‌جهانی پیشبینی کنید!
برای‌ورود بسایت‌فیلترشکن خود را خاموش کنید!
▶️
‌
Link
🔜
MelBet1.net
▶️
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/25521" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25520">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=E6gSvRvsphdqMq9TfYkK_QBVIsScvIVtz4EX_w9K7GVSajkp6AOF7rwizxJHj9L6myiZgRyLBgoJCrj1ZwE9EDfctEWvjXfbOLNiQiQ_RH_QNTeiibv8Oe5f2vSXBaGR2TFlqY2U4B6z4ic5SgVI01zFpw2Eeb09HwuhBwqHTRcd4M-8Ekt5RpT75AhCI1QDPodm2X8Q81wl8ANyl11p1cVju8bcD4Mm0tt6cRQV4PEKQY1sB2PGOW8nAwPX6PD7pn8ubQMb4sojX_YmXD1K-9xNG4QF_dptJ7Vtf5dKZ3ei-Bruf8VfyAdbS3rVI-c4lQKbL5bxneevCgjt4nYm4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=E6gSvRvsphdqMq9TfYkK_QBVIsScvIVtz4EX_w9K7GVSajkp6AOF7rwizxJHj9L6myiZgRyLBgoJCrj1ZwE9EDfctEWvjXfbOLNiQiQ_RH_QNTeiibv8Oe5f2vSXBaGR2TFlqY2U4B6z4ic5SgVI01zFpw2Eeb09HwuhBwqHTRcd4M-8Ekt5RpT75AhCI1QDPodm2X8Q81wl8ANyl11p1cVju8bcD4Mm0tt6cRQV4PEKQY1sB2PGOW8nAwPX6PD7pn8ubQMb4sojX_YmXD1K-9xNG4QF_dptJ7Vtf5dKZ3ei-Bruf8VfyAdbS3rVI-c4lQKbL5bxneevCgjt4nYm4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
شوخی‌جودبلینگهام‌ و ارلینگ‌هالند در حاشیه دیدار شب گذشته انگلیس
🆚
نروژ در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/25520" target="_blank">📅 16:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25519">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlXfxJdfdGaruJaPO1zsDLbAyivOeJ7ip5dLpNclYy2y0sMwlBLd0X3Gy-38g4O7O4aPmY3xDDfF-pt7R01QEFbw_evZguyA0hsmaXHqImRF6TxXjzen-kb_Bz_MTYxlttCg8I__vYXiUmyHfAQ8oCQhny7hQeGqbodwCJv2GSqU1Z14NP__JMCb77eK3tCnCF_g3xVnZI2FI1wRjjHXpIeR-8b8VqvMBA-N3GNB6Ge03BrQu3s_-9oBflHcUhaj21Un625DGNagiMq-lK_7VrAvmU9-0V6kXrfBB9K5KzUVscJ8u8SJksPCmHCBX4S6QjYGccaJhbHp2NcA1-UPAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/25519" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25518">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kA1rTkJV7F3mdBRenLhVeG6Uqcs57zZU8tOLLi7LfkfxeySwh9oCJJ-Fxs-bFm8PGOfh23aBOME4m_3y0xp9VBBaudvPvO2p6RtUsgY0c6lBPTHFfpN4270fOHCJUxGLs3yOiIDhLAHXj8rsIVAcjWuPrbm1xOYBoI6ZSQ9x6WlfzvIEwFeARPumm_qRfl67_fRNsBMzmNI_xk9GePfcbRMDsUX3n6CSzVZXlT5hnLnsmJeDh_9TvuaEcV7FPSrRW4Cdln_nwIzPpPuFac43Uzy9si3f5ZsP2wFa8SAegiG0P_H9NtHFALVC0R2N4GeD29M5bgWMckAbDmgrkPqV3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دو تقابل جذاب بامداد امروز مرحله یک‌چهارم‌نهایی رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/25518" target="_blank">📅 15:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25517">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HR-Ya7jPtEVUDY_6o7KAptaCbjNhVifM2rkX__-HBGjI_sk2sAzjZxBapvG9_lKJdQYfaSaThkEh1_5RXInbifakPw10nx-yYCSCuEcBnQIX4phN5a61f-Yq2pCjQbJN6KsKGaoY8gvUW7k7aWteJkNhcgOr-LcpYRu8q8AecHr0ePN7w5Deu0W0lp8xNh0SBm3pzgCBnKDlx46E5DMhplmOnYuxaNWbwTZQ6VPyXPY8HFVHMDG2FmdSS_Z-zjSe58KYUuhx5cLdHDH39PauFpUZbDOH3dOPfanJOvEcTnkQ4SDSWBot8XDVwj9vhc-iayeD5HlwOJ1HrJgHFOXnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/25517" target="_blank">📅 15:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25515">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/25515" target="_blank">📅 15:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25514">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByNrKRqYACNIaHUT6RtC61UN3Qd6FitCFlVBWJn1sN02xArE62kq-mB-N5G82x5_T0227Xahv1epL7PqQycW93goLwAa1wHTLvrGCFnKHt4rXrl4T8DGHk99AuW8fzZkbqn2HjWXKdb1e7SqLzqXR2Ykb8_zPpxxkmLa_jT1ipxDOcaA6JsLKQGTkyAzunSxtlH65n-bb6DU_kvPv6_u8rESyJcLoQHT_IJ-kHFwYtOPen4fVPlqeWF5MEOHmV2KFuXaqtniCgt5V_JgTWWysy4xnmfmYu2wPhdEMBe2hxYJPqs6TpP0f3WhnU4h1l4bKnbeCqzJ10wiygMKHUhDqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا
#فوری
؛
یکی از بازیکنان فصل قبل پرسپولیس از دست مدیریت این باشگاه بشدت دلخور است و به دوستان نزدیک خود گفته اگر پنجره استقلال باز میبود تا حالا قراردادش رو با آبی‌پوشان امضا کرده بود و یاغی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/25514" target="_blank">📅 14:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25513">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EENnet-K50RSceHz53-qIFm3lKKVmnMQrx_umvD4F5hkpJDLfD80VMPwvWqirBEs-4iqxlVxmxA7iAK2G5I9Ehjm6kqrsmGIjSqxg9FKm9qz5PcZ7w_fnRc5dUxFZzEVPlxs-eI8Zt-imEVvCH7mRPAZfz5N6acSmd7uf5xb48bvlnR5zBdF4Fmen6KB6u-Nr-3N8NKg_5IHLO2n0ZTZoTJVlBs8gYyHYHExXqOch9v-QmxXsP4q852kM95qoU3BkqiN83IkAKmrkeDaCjlFxP4x-D9u_fzDoIMI9i71ccBEe3dZXSGeT8isAEy-Ww0QEC9TaP9OXVqnuG1EYIACOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/25513" target="_blank">📅 14:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25512">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=lKb5h9bID8XbEkrScCoFUnT5eRzDkjujux61ls1idmkb8UqIJ2y0vFDd2CyPCoEKWXe0MlsMDiN_3blo1uCbLuury5N4RaHxWbFCWa1zkVA1Vny9hzeLHEWm2lQf9_zwRUvJfTwTWOMVc-xiLvslD9wBPR8CdVrP5pO5QL0gJOFYtl2jnHSGDD-kK6FNa7VWoEbke-mXRTXarIEbtoWQ6D4ib3ouQAgKn-Tc6eet0sNHfMjuNBg1oEbka3ECqT5LA8L52h33SFPn42KwomaRbhsKBh-w1Ci10oNuG2XvMzHAlVybXrnjsWfoBwbOQhpKswdom8gDJFL0U9JqM1QpvbPkZZ5xOdV1oQAyiXF3bi2IhawzHfnSiAN93mshKmeepVphjIgj5OSjI6TMJqwX7ZOx_Qq8JC6avNGUUqyZyDaLygqVrRGmsSbXW3ZqAAVekwZeL8s6-aJS9tykIjYkTp4AEmHpgtYMszwkc62-WC6BXeU1f72FvKAJRoD9M5E_4SagDyvumqLx8PcjCK1E6TYkjkR2w9gu_dDx1mshs7PuZmLAPlfa8HQsS2Tyt2WHZl8rJA8Kpy1U_ZxiZo0d4FZ4-Sns0BN36LafiMkp06Z31ry0M8JneocHsrypEMZPpLEVievpcoxgWJ98gjMFNKubEj6SZUCoZnZZgPcp_7k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=lKb5h9bID8XbEkrScCoFUnT5eRzDkjujux61ls1idmkb8UqIJ2y0vFDd2CyPCoEKWXe0MlsMDiN_3blo1uCbLuury5N4RaHxWbFCWa1zkVA1Vny9hzeLHEWm2lQf9_zwRUvJfTwTWOMVc-xiLvslD9wBPR8CdVrP5pO5QL0gJOFYtl2jnHSGDD-kK6FNa7VWoEbke-mXRTXarIEbtoWQ6D4ib3ouQAgKn-Tc6eet0sNHfMjuNBg1oEbka3ECqT5LA8L52h33SFPn42KwomaRbhsKBh-w1Ci10oNuG2XvMzHAlVybXrnjsWfoBwbOQhpKswdom8gDJFL0U9JqM1QpvbPkZZ5xOdV1oQAyiXF3bi2IhawzHfnSiAN93mshKmeepVphjIgj5OSjI6TMJqwX7ZOx_Qq8JC6avNGUUqyZyDaLygqVrRGmsSbXW3ZqAAVekwZeL8s6-aJS9tykIjYkTp4AEmHpgtYMszwkc62-WC6BXeU1f72FvKAJRoD9M5E_4SagDyvumqLx8PcjCK1E6TYkjkR2w9gu_dDx1mshs7PuZmLAPlfa8HQsS2Tyt2WHZl8rJA8Kpy1U_ZxiZo0d4FZ4-Sns0BN36LafiMkp06Z31ry0M8JneocHsrypEMZPpLEVievpcoxgWJ98gjMFNKubEj6SZUCoZnZZgPcp_7k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اگه ایران میزبان رقابت های جام جهانی 2026 بود؛ این مسابقات جذاب چطوری برگزار میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25512" target="_blank">📅 14:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25511">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppL3emcatPnfDd2woLRH3_H0KyfsL4OewXtf4iX5rWVqrVla2pyy1aO8e4S2bqE63hxYyvh73V2JS2gXz3PH-Z-B2OA5sc2l3FR1opoWDr8od67DAiu4f5j6bluHKPZB8BZIbjLHpu-I2GBmvoZ6N2JojZhi5DAVs2aK-xil4zu3x0uFk8ZuL9Q8HInOc6cKrR40RiTNwMyR-OCTgS7dZKPfeKaXUzT_pxq9VOHVZOsjtXCUuSywLVXrmenCl19o_OTu7lXg398T55CATB4RftCY3YTRayUEgFKbejr7S8Ha-unMSUe24MEplPkfBtubq8InUCwxJ7LAqUpiFq8W1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25511" target="_blank">📅 13:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25510">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZizfqKTXnQiwfaJfWotU2sGCe7NyHmIq74XGuIgWXdaIjoUKyUliOvGZtChGD_K7Y5ylRcmpjMh0VQApcDFDo5hzkQFt48Jc6i0E8SHKI4-MpNqY5m--oxxn9ROkP-nzdimj2OH3LnO-HpigVFruydxhUXNt1v2vl0Vfwo90F5z7VcJ5QUwTclj5yrDwB5bSWypA4L_zV9jbFE7CTdniGcZ5q8EoXpXh9noo0mho3QYPv3QDC6YbzFxf4o5KrDl6xTU9Wxf9d7Z1shG01c_vgjv0s99ymne1Z_ADHZ9KwEXy1lIlb1dZn5YXQTyFyFqJDfsLXal-SgDM_3p4kTG3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25510" target="_blank">📅 13:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25509">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/logs8suRGiuy6gr7ghL5H-hSj3PEzPD3jd0iP1P9XD0uAjpafyQynF84jRm1tOAd8-LF1i7Qc4mRpFBhPwRqHgr3eTr7HlwnTgYzAEde6d9bM2jMrOr_fuaXaOJOxwm77tl8NjWKKayUMlYS9nkhEgaTAseRWX1UHpNJGckZQTWBHILgPUyxdXgP-16wT2cjFABmJZM1puJhY7R-mq4ZBe3KxNS1pzyBVXCu2om8r4xquXxJ_folcKQcAkbHe8x_VkH7yQy6_KFhKn8HComvyvRUojA5CjAH1o1Pe_MLl-G_-ZFcN8NL2vI00Va8cU8cXPNyCy5tvFJndBb0EcMmng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25509" target="_blank">📅 13:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25508">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5lVFM70gZGAZC1QEbsr-878AOTJiaU0teTQqo-Nw98SvNz2SHVKrj4jJJ57IxYkP1u_C_tZqSQS5kZaTGyAl8a0ZhiQF9J9dLvfWjabnNQQKpN-5qhXYxvYXVZCCXS10lGl_Uwd_zrYuR3FdKbIPDgZl2doLJ6D-zdy6uTtialDZ9c70WKchB9W8-qlK7UeOHODTbm8u_b1Z357CmwrT-rHp256JEN17ANWK4AbxB34UxaUHsZt5aFbyCnnWygrE0z2oH9tJ68HxLmvtVVBmsk3yi3vVf4hJLSia9S3k8HAo2efcwHKnsOe0aLeZsAK5Zz1PKLlfu9rE7OY-FtUnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25508" target="_blank">📅 12:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25507">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObziVqexb0fwbc_kTbs9fzCK69WUyEihJi6Jcuu98JM-H8wQ9sBGefubFr0LxwcWh4eLmPuTG9bYpxNGsdGHIi84IGV8vopGJZ7r9hN44Wh86e-ZHzqJ9zE_xh43uxN0i7tMnMvK8cepDK3OidID1U4SQC6PLtilCrMbwOBfk9Yq-uEqEzicRbIRRV8yI_q2dvH35qVEOC--W-pBw-uKipJZOJL-gaw_H_pns4y5GbzmLQcCHPAldJRoxMIIYvVUgxe-g6Le4kWh9Ds45Tt77hEDsgHl-Omts1ZfjiwF4iSnHTe9PAG7navCTJ2ce-768fbFBsF4e9IYYiNADxNdIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عادل خان فردوسی‌پور پیرو خبر دو روز پیش پرشیانا؛ مهدی ترابی برای عقد قراردادی دو ساله با مدیریت باشگاه پرسپولیس به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25507" target="_blank">📅 12:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25506">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6pirnEhanEAfdU1fFgMrlDSrHTWqVc9_8CX53tnuyVivvqxBNwVT59aRqjAxaQ3z1nNDHZv_q6gqS4DHE4E925jLKZv2EPdYWXGjaXa9z16Ekk2bviYc67MKKkEMaWlzEyCqPqR7yGjShx_Ca-t1Aeudy5vkljMhhjnGsAA2hw-6c9yExYQIIa91AJT9AJHwyvklPzk1N6K-0c6UmIGICYbC1QXlooidCx8602rrpoO7LAl5xwUzdZ82EHmh16xv-Dd2mHY3Ga778z-k7BacvvDz3ACqSdyFVFiuEkAdRxjPdfaz4JDU0Qbwe7tIdZQux4cqg7svitn8QYZ8vWS7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا
#فوری
؛
سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25506" target="_blank">📅 11:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25505">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=Mfa2tm-JzKULs_GRkYmeG8TF9lHkdRuaPfeM4sL8P-BaQCj5fzpy4sWcPxUEZHiVIm2K8DY5HPuYktkH8Hhw-kSQiQkr5KlgGGvmnaE895D3MdWkeWKuotnhKUGYjn5NOjskQrVOUExGJvOwUrUb15WPFkJFNULJjxi7_eSPm6dhaHBeuY3S6D6OzapMqwjcoT4JT1gihVKh1K3MFCt_Og6k48qFO0Bgc5MjVbynfX83tqIqy76cEnyKPbC2IFjY2X7_1pURXBk0WMgXfi_4fJ-mtvRItJxf-iZrm93poC8pZ2fRz9TCfzRT22h1Fhr_AJpFgpTIKfy1jBSBJD04Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=Mfa2tm-JzKULs_GRkYmeG8TF9lHkdRuaPfeM4sL8P-BaQCj5fzpy4sWcPxUEZHiVIm2K8DY5HPuYktkH8Hhw-kSQiQkr5KlgGGvmnaE895D3MdWkeWKuotnhKUGYjn5NOjskQrVOUExGJvOwUrUb15WPFkJFNULJjxi7_eSPm6dhaHBeuY3S6D6OzapMqwjcoT4JT1gihVKh1K3MFCt_Og6k48qFO0Bgc5MjVbynfX83tqIqy76cEnyKPbC2IFjY2X7_1pURXBk0WMgXfi_4fJ-mtvRItJxf-iZrm93poC8pZ2fRz9TCfzRT22h1Fhr_AJpFgpTIKfy1jBSBJD04Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25505" target="_blank">📅 11:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25504">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8G-pcCi7Iis8WyOPUlaMARrUjnaQRJ-94lxOHSMcw1-gW9UTuFlVh3OG1024dKOT8B7vkPHnROo90YePTHQs3nwGIyTNh1Y0w2VG72oIG2P7OS9nU5iRD_5-VXjDyumQszLMwUByLnY3b9sswyQQzlTGvzg50spc-tupuk-1sz1JQmiTvLKx9nM1gNiiJjM_fsTJ7XwqLXoRsHJNSuhiFl_LL5xL4UgLcz_WiovENCgR5lFXOc0ScWvFfzVu85Z38knVrKIubsslyHcCl0oJNJHNqrkWoIDfE8OFF68a8Q5EpDWDuifsAc86zqX3G6fqTK8OxA6IUOxSXgYrEKKeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25504" target="_blank">📅 11:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25503">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfL79bER5LpVse0n02AVdrtExMm3XzBOtW_bVBMOBM9a5Z3euHOSCn4JajXPN1jaDGmFJo7sGBP1SRAP8jDOFPHh9agibogM_1xygkGXEN_CxJCk2KDw1ok7xekzBfxAc09QiXTtVn7_nEtZZyWzWLq31CPE6L-Hgxbx3D3_Aa5XhpJgiPyteWVN9Zl-AvQyZ9NKaLnGEaYwDdLSoi7vze1llgRrBgYXtk4pzTKCZa5IBePo_M_00kqRgcpYSmT_wCmVpxMfpxeJYvS8MxM9bS3EvYOR9T4fJwSFDE-9oRIJGW7N-vY1kwMpheyGhhbE447MdoJyj5JkROAA3fMGxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25503" target="_blank">📅 11:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25502">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=OHUCkduA-uEzl2Y5kxMTEM3uMILNP4hC6U1eI9Uqie7fuH7LQmTgC4dglglEGOAJ_8w_GKL9jfCfcSIPhcbVkzyOIkhfARe8Rv1jRKILgapb5oF5aLsugVMI9uHBr4bEZWsHhlEKYcTyI_LZmD_cb9ROw4MbV3roiucebAf6gh5bxsyeXq221lk6nv4V0Wc-NZHN27m0LOPzPARyHeAERVjwi_4naY2twDoZczDCRHhl21kvYJkE7g7J7or24-3aHx4HXrPOBmqlm3SK36TOV1H64HMoybASCP_PD7vp2LitAoVA5ckHdlEHm_CHG3bIYxxzHWPCqgrlPYf1NvLJiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=OHUCkduA-uEzl2Y5kxMTEM3uMILNP4hC6U1eI9Uqie7fuH7LQmTgC4dglglEGOAJ_8w_GKL9jfCfcSIPhcbVkzyOIkhfARe8Rv1jRKILgapb5oF5aLsugVMI9uHBr4bEZWsHhlEKYcTyI_LZmD_cb9ROw4MbV3roiucebAf6gh5bxsyeXq221lk6nv4V0Wc-NZHN27m0LOPzPARyHeAERVjwi_4naY2twDoZczDCRHhl21kvYJkE7g7J7or24-3aHx4HXrPOBmqlm3SK36TOV1H64HMoybASCP_PD7vp2LitAoVA5ckHdlEHm_CHG3bIYxxzHWPCqgrlPYf1NvLJiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
نروژفراموش‌نشدنی‌ترین‌تیم‌جام‌جهانی۲۰۲۶ بود. جسارت‌وجنگندگی‌کم‌نظیری‌داشتن و شدیدا دل‌همه فوتبال‌ دوستان رو بردن. به قول یه بنده‌ خدایی اگه ایتالیا مدل گتوزو تو اون گروه اول میشد جای اینا میومد احتمالا این مراحل رو به چشم نمیدید. من خودم بشدت فن ایتالیام ولی خب مدل اسپالتی و گتوزو افتضاح بود ولی مانچینی درستش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25502" target="_blank">📅 10:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25500">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmqlA-WVGgiLDGIDn-OBUtfA0z93DvHXojIrHLABVtV6GgVP-rJoNEW20HSO7pz-dnKtGvoqjdQOYESUD9c3VpJFvU1GVtmgxvM89Tt2lYLUDYtK1FE1uIAnk5VZSfTQmATovcP0lpzlvsDe3bHOJyr2uqIRf8MFIx8Y6xu4AxAhozNetZEZrI1O4oM8ixMYsZPljzIMeVnCHoQYV5OQnXHNUBtXHZ5HzYr0EUdrcNLdtL4uB03mvvme9BUxBd1dWz7uTSgSuyk_Y3McWcNAjPfPC7Ah0GpmHXTAFMsj0EkpTrsVCcnG8UVtSyqc1XWkvXNTrB5XlnG8GBX6UwoCWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=kcbvJB1o-L9n2pVVZSn8zvIUaCdEiFpvJBwvQZdWQTwjVsE7ogX_nGTwuiCGeWdis7wb54cvuRJ1Ip6_cvLqBjDWagTxmUh9SjJTtFVZvSnpKeLrBzC0KeJ_aCwF7oUFcAir_eiUA2rcv2od880PrFr6wGGSa4W4_bIzP1Zr3cWLS7CR_2HWtk36y97NQcuo-t4vasQdxJr3f2apylk-FH0GX4nXFosqWUjm84iO8t2HXiLA1sP2W4w7oiqtiGECu_BrIsI171GyHeSDvuxUEdlZSyWYukp1b5P-FgDVA8610UTIPMp-X8Wn-68IDsdFZ4aUk8TTI5lXviLV1TlAQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=kcbvJB1o-L9n2pVVZSn8zvIUaCdEiFpvJBwvQZdWQTwjVsE7ogX_nGTwuiCGeWdis7wb54cvuRJ1Ip6_cvLqBjDWagTxmUh9SjJTtFVZvSnpKeLrBzC0KeJ_aCwF7oUFcAir_eiUA2rcv2od880PrFr6wGGSa4W4_bIzP1Zr3cWLS7CR_2HWtk36y97NQcuo-t4vasQdxJr3f2apylk-FH0GX4nXFosqWUjm84iO8t2HXiLA1sP2W4w7oiqtiGECu_BrIsI171GyHeSDvuxUEdlZSyWYukp1b5P-FgDVA8610UTIPMp-X8Wn-68IDsdFZ4aUk8TTI5lXviLV1TlAQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25500" target="_blank">📅 10:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25499">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOs628NPuh1H8b7LAgRATvOZoemi7xvsEDmWYKyKh6rf47vNkW6T1ziB6Fasx7DaJwH4_hTHWBsy8MFYONL0TN_jDsNOz3SxYX20Tp0BSaWJuxxHOK5Udx6o16a3FSV-oHG5obhmXJP50SGY7kkdENqYBo3C_anB1iRDjM3YfwVqXAB-V2W-uvBLhFydaMrVpSsTaleVbyzSoiNxnfmIbG-HDOrUJTFUmzdkc30Re-gU3P4GFO41JEXpj4MgbbjZa9b4TqT7DTTVpLkvQXroYWQwlxh3KddNkU3wT5oDNUArjZLHfsayxDh_efefsqVEQA4Y07lSbeguZWZA_6mCoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25499" target="_blank">📅 10:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25498">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STYxvLnDYzxREFd6TnU8xRLC44M5-64UGt2_rPt5etCPZQRBWvOvGFTmZQaNBspR7p04RO5Eo3TD7Id7DmK4IDy5-I_pJ12XIfBUP1PrJjKdPqy1Xo6CCL7rTYVF5gT9GIOsKGZ6zLLJPfAgmyWknUWsaJY4xdWn2aR1t1qYk1N5O0opVvX8BiNXB0iDfUzh5JWKkEjI0SJbdO0iM2pVE3Zpux7iU8hmm8kgfskF-ap91AUdEAcKQckKc7P-cD97rpgyLg3IYyIgHg0Pm-_4MruqRmn_blMwFsPgPdXLcGdgfuUyYh3nCeb1FHqsuF4G8KUMdWguaIY9-n1vmVtvdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ جلسه مدیران دوتیم‌پرسپولیس‌ونساجی‌دقایقی‌قبل به اتمام رسید؛ نساجی‌رقم‌رضایت‌نامه رو550 هزار دلار اعلام کرده که حدادی‌امروز درجلسه‌به مدیرعامل‌باشگاه نساجی گفته تا400 هزار دلار حاضر است به باشگاه نساجی پرداخت کنه. قرار شده که ایری…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25498" target="_blank">📅 10:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25497">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=dCVQtGddch_CUxhYF184bIxrVJuJ-R7oQJQV-ImccaUEGAnSclSZYc12pGpMkjoyW1Hw2kUsNAcLO7moYzxQZTeTnz7wgDRc4ni2NmdIQMKW3jimXbcOwDw0c3PRCznJZzS0d_xPW83MPgOV8YqOuRtO5vd2CpveszDDUplBpzP3ASVKO9AnYZoRp5puGqBhPOcq1IOzK9vqJSyz3L5K1TzMPfWrO59LoEFR9I4nBYaTmFaL8JHqfIyfZvIFzP7Zseo2jcheUNvsGHIztS51R_GPB_zZw2wWeivGY-tIo9O9ahviHjq2LqP2RbEoQZoiiv-U5iLxtAc7gZTCOgjgjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=dCVQtGddch_CUxhYF184bIxrVJuJ-R7oQJQV-ImccaUEGAnSclSZYc12pGpMkjoyW1Hw2kUsNAcLO7moYzxQZTeTnz7wgDRc4ni2NmdIQMKW3jimXbcOwDw0c3PRCznJZzS0d_xPW83MPgOV8YqOuRtO5vd2CpveszDDUplBpzP3ASVKO9AnYZoRp5puGqBhPOcq1IOzK9vqJSyz3L5K1TzMPfWrO59LoEFR9I4nBYaTmFaL8JHqfIyfZvIFzP7Zseo2jcheUNvsGHIztS51R_GPB_zZw2wWeivGY-tIo9O9ahviHjq2LqP2RbEoQZoiiv-U5iLxtAc7gZTCOgjgjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس‌جونیور ستاره‌برزیلی رئال مادرید امروز 26 ساله شد. او تا کنون موفق به زدن 128 گل برای کهکشانی‌ها شده و همچنین برای تمدید قرارداد بااین تیم با فلورنتینو پرز به توافق کامل رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25497" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25496">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwKpXaAt6uNpyHxRNShWgpRBWvdXIdlLqSs101P1MrjFPVrTmoL8XtbU6J4ZMfmyWzf7HKIjmO4ofTcRNuF2hXRE7bXjEmQOhvPdv1qzgPRM997Da4WsI0IfUyhRv65ObYQVMBlITPjR8PFCM8ERG8YzBmT3ZStbavwQMY6TEF8b3mEqbfyG6TL0Io9nwRfefgNDc3LMg658WuoHNjzasy9ajCJeSIKNDKcQUc0hTGy1Ni8RD1N4DecC4JLXAHmiL5sKsgfS7QzP_mP79sWEqMhgzxDtMSwmeiPZitQvatecTYPUZlItAjCypGM38NdSwZrMCwRz4QJm_Qc_tiQdPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
5️⃣
میلیون‌ریال‌فری بت ویژه ی فینال ویمبلدون
🎲
بدون ریسک در وینرو پیشبینی کنید و از تماشای تنیس لذت ببرید
🎁
🎾
فینال تنیس ویمبلدون
🎾
🎾
زوروف
🇩🇪
✖️
🇮🇹
سینر
⏰
امروز ساعت 18:40
🚨
ورزشگاه سنتر کورت
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
بابیش‌از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
📩
Winro.io
معتبرترین سایت ایران
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr21
📩
@winro_io</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25496" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25495">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=fdQHbLR8MVukqdqWw5ALrjmQP1Rf4JdNPbG3Y4EW7e52EAaJ3ZQ3X_i8FcvO52VXBtjLYN-oUGV5b7YYO2PaVr1dcPUQ7pGBaYXrnioR9viJ8b0PXLG6wZGQdqOd5T5LZxR2bZ3PI2TnReAEjeA0Z5eZyRXCvEbzDsKsmYASFlAP0nhnZf4YsiljTzrNQSM8tmwFDQs9xjxXZ-0QTsSRn6FtLHiEIrW4EzjTZC4Gm6-s8J3PP_m8DqZtowaU7ICulf1_1gapQR2NLIGFvBu_OTbp-BVYMrQNQb75E9PQyIO7DO3uGKpiYWq0bB75ajVQvd8p5rwLXzmxqli99qQ7iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=fdQHbLR8MVukqdqWw5ALrjmQP1Rf4JdNPbG3Y4EW7e52EAaJ3ZQ3X_i8FcvO52VXBtjLYN-oUGV5b7YYO2PaVr1dcPUQ7pGBaYXrnioR9viJ8b0PXLG6wZGQdqOd5T5LZxR2bZ3PI2TnReAEjeA0Z5eZyRXCvEbzDsKsmYASFlAP0nhnZf4YsiljTzrNQSM8tmwFDQs9xjxXZ-0QTsSRn6FtLHiEIrW4EzjTZC4Gm6-s8J3PP_m8DqZtowaU7ICulf1_1gapQR2NLIGFvBu_OTbp-BVYMrQNQb75E9PQyIO7DO3uGKpiYWq0bB75ajVQvd8p5rwLXzmxqli99qQ7iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25495" target="_blank">📅 09:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25494">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7uNKiDfTwsDzi0NjnqzyGuoq8QtYPSz7iWiZMsUD2GqeNeoHDxSdSRotOkEC5CaBBf3CIKiuaKOuTCWyzQfGqxmetcpjOJvvJvF3lJeoIosA276RU1yvxOgevngnBK2jbtuX08Gnf1-i-oFgZ2PQ4Nj2fcNIxxYg0vhf6Wia5ll2N7Aai0Q0eTfSZFjcF20S916e4hqDEc0dEQeddV2ktwfN1kaQJ2DX-dQqERSH3GU1v4ClY0VRIVrjUJR17ymuTr672eyYeFzvRfVJxqedF0y8J-vCZ3rxHd6GiPDCIJjCj7hZ6iIQ4pMf8_aVZR-aiaCPSt-2vMVABf6MgXcqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25494" target="_blank">📅 09:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25493">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyUAGoiA6hsgaq8UMuyK6dtZd71xT2Dm5g4pekxUu5PlBc_rMrghrWaUZwTQOseLHgoWQQentA2QFOFG4tUyra6JPL9cKisWEKSJFDo7QgqXR9nVRwNEuJ_CeBG99bIrCivPs8RbrydEQuURiYVnrcFUS2KnO5sPLbkl3LnFcVP9_EU8WjWm1e4ChwTPq1KJOMUWb-1CBObQE9nMTfv9ZXq-CKmV5Rcn_NsVUt8rUDdbSFK-6FdDKvVPySi2YJwjv16Y26fX1DvPt37illBXSGwPDzKp4aCbh3xQhWsw_PObjtCRmGKGnvW9tuko931Ls2Kv8grdVIXPaC1zcONRJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی‌رسانه‌پرشیانا
؛ فرزین معامله گری مدافع چپ پرسپولیس بعد از تمدید قراردادش باسرخپوشان راهی سربازی شد و در فصل آینده در یکی از دو تیم فجر یا ملوان بازی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25493" target="_blank">📅 09:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25492">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c6aec402.mp4?token=M5kLQDvcMNUECai2meJKXaOSiHrfhGlxMv5WyRX0bop9rSL0ZDq72EDivja5JIYbwfUN5fXFS0qoHX090zF1EXMHmCqrG4tx-jPfbzEcdqRCYZpFRMaH2m8HHa7Arkvv2sjZANlmaXlCzA95QMi23FWCWmVwDP2H-6pZtPRKCK7s9aceFUkBM0l990X9CSib_Ab6w0lK1jIdfHs6M0JduNt4R-cXh4tRTXtyXEyhAicZdgZ0q0hCUC_IO5Snwv31Pg8XVsegi9gWvcC6_yq6vSIPu5c9Ggnmjvuf30DCdBau7wm3-VD4cDBHFI2NhImmiwWfOZrm3VLe6AQMHMQHbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c6aec402.mp4?token=M5kLQDvcMNUECai2meJKXaOSiHrfhGlxMv5WyRX0bop9rSL0ZDq72EDivja5JIYbwfUN5fXFS0qoHX090zF1EXMHmCqrG4tx-jPfbzEcdqRCYZpFRMaH2m8HHa7Arkvv2sjZANlmaXlCzA95QMi23FWCWmVwDP2H-6pZtPRKCK7s9aceFUkBM0l990X9CSib_Ab6w0lK1jIdfHs6M0JduNt4R-cXh4tRTXtyXEyhAicZdgZ0q0hCUC_IO5Snwv31Pg8XVsegi9gWvcC6_yq6vSIPu5c9Ggnmjvuf30DCdBau7wm3-VD4cDBHFI2NhImmiwWfOZrm3VLe6AQMHMQHbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25492" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25490">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jOqZj2ikxTgwMrWD5mMS_Ay1-59ArOs9LN-lvYZsZ-my2En0Nvv3f-Vo3F9gJXM1B50R2kl6y4cPrOdzNfgRj3BCsDE8R5lcxOd5GQ_hRwHzYJons1RJG54LaMkj7H0UtEecUUQboeJJSak6xLZb_zzrDb4b3kd3bZhr23tQp67wVZZoJWy08_orZaabdCld5Gpm2pUc9J_cOwmIlJiW5VGRX2SXhjXt6gp6JSZnh_pqfuxoWOUehevHbX8HXylYU0LX2gjDBr_2sQITXcBmoxIEPVb6QGVCNcf27fy0Q6qNqzx2W1Y9IkKq8-vkv8BQk8yEOiwJYcpvcbPLoDn36A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YzAUmn2NKZaQy09weBkQSqO5ZKER9j3D6lRIdZkSeMSsf88I0Z1rxtC0wzQ83mBYozJXWLT4LNjlTQFW8AOBJKpaXsZj-IBY3VRLr6vYoO-6QK-alO9jO_5s6MSHLXFc9Xgb1R5E-2eueWrVdH6lzoWFiBq4xGNV8XC9JaIk4FY0BX6Ysjuk4Aio3n352INtS4mIpULU_eGdqsPvo5yPY4lY8f31ZuzRwpqz0hLQfxVvNBZHvlhROnO-ea84YsccajwyFDO4e0s_x9NjnvHX-hhR2WQbtC4nqgPoSZc6N4u1HIw_Xay9glQ08yJEdhRcLwlNTeAyDUeGiypVCsICbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25490" target="_blank">📅 07:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25489">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFr7nF_7-TkZalUegNlas24SZYXjlRqvZpkw6G8jokbkAHJlOUiim6vfiqPMupg9jPKCyol_3mJoOnl8UegROjCErsOJnvSjZPgdfkH_Flvw3M3uuPW1F4h2v2HFjP1sO00uVAHaWXPAtI6VIOd7cvW5CjN-tQ4bX0nhghKCJqqbOx-T3hCefNVSBbn5W94PNmfgBqQVYpMQwxgnF_F5K4_sQPN6QwznSSVdPiS8zc-IgqWvHumG-661BuCP13n6Uu0xL_RUkAIQw8cVtW60Q4s5Db_iojkjqXoMSxVp2XXDtXPyYBL0LPi7wCXRL5QvNsw7VmqPc50lWLUSbLHgxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25489" target="_blank">📅 07:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25488">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4jtX84KHYDDYPFZvKVLrIvp9wR-12uKwwa9FVo7VVDbGqV3b_qRuVZXrimQfpYJKTzrMF5TlyH-NOtNLMKNnndxNKxzUKYaWjJ02MVUBKROb01BvyuC2luZAMJjNIaOTB6HdI8jaiCwIhvUSZIXVenNKq1Bfzz_YTFgdGRPb30JGt_Z47iBi5_hWXPzt69Bj1BV9gRttBL6ofMiX0NQf1yagV7BkiNwGcfO6jWKosrpV7Mzgm0Vs1S_pP2MDpbsekgBu9ZVsgK9_XIw58aImYLVHqgrPbsQrP8Np6_im5xzpREXoeYtY1rGeokvDETam73kOcJ8OW6iJ7agYf-okg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25488" target="_blank">📅 06:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25487">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWvNkgGe7pfEpUHi25fHJvFehsa1fQkFVr2Ga_zoWfBcKxphzP3ccMuSLh5fMHPq5pYjI96Ob9zXz-N8necTULYNpYZ1m4LRpW5Hxu_zlNhdUzyrUBUgwqtTRbVGe_jW6aHeL1gOGRM0_d0pUdgq_VG9mrF5mI6MWIh9sjyKmVNPlSQyuzkTlkZnhy2SQoW9zEGP9isxfF7KyB7ImBOilbbgtvC-dWCqZGsQhOyLlGA-NNz9WxhIK84Nvg2GpFaTzDvZpdLfeVr4t5dyCcY8PFOf949eqo6XMOfdcjZd4Rx0DcYjZiKKtMdrLTGu89cTEuO926UntBfL8OFqDudkeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25487" target="_blank">📅 06:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25486">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBHitqgukVdG_wQWzvbwgHkwWVrbvBUXz4o0SKPu2k3S4Ug_2INHZ7oHaaGbBqdoDvZXNW0vG9DTgqG_XEErOsshYcOevN1s3bd1H_emeKSQkMirrB7J6ACYjm5EplPXVwwN41h0cCwfbjG2eoagWgQrzW8E0NMxDqil0num2XaIIm4Dx8EN_h57K1yaU1kP5g6jwbTlCURLOPVE0uVcgQMK0DuvgtqZ_5eLnp2awcJCTVJvJuBQirgk0HcaFAJMZ4lgsNpUKcgKZnlTQrAxvY3HIZFs0CL_4-KVntU2fuS5E4goLdWatYmvN_dqopmQL59z0B32dJlQDoLSLWLpzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داش‌چیشد که به این روز افتادی؟
چیبگم اون شب جای‌درس‌خوندن‌نشستم‌بازی آرژانتین-سوییس دیدم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25486" target="_blank">📅 01:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25485">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=oOET-NbcNkCuiXsbpKXnHptqMO-t5IFr4kzwKC12ctvAJgYYMbei4ADOsyaNCwUX-lCrEl8qVyOlG1_WwVuQhWNFEYc1ogRU7ze57itbwtNfDj9UyRh3X1XYWGyjgYCIYrYKB4C6MOlPG9ji7xwVFCES04mFc4VXpbclBccJEbX23aeH64WaYip3xkEJMOPntUN858LbiM3ai9ZuCj6cb7D0HB1RDJTRDDZpKey4mV-3JMeX_OHXgc9AAx0v5VC6LZRJ0Qz5SlGY7O5K5PxiEJj9vVydUfDOYBaSK32m8eHeGop_P_77ZezxWasFuk7EI3kKZelC4nTy5oxLvuqwDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=oOET-NbcNkCuiXsbpKXnHptqMO-t5IFr4kzwKC12ctvAJgYYMbei4ADOsyaNCwUX-lCrEl8qVyOlG1_WwVuQhWNFEYc1ogRU7ze57itbwtNfDj9UyRh3X1XYWGyjgYCIYrYKB4C6MOlPG9ji7xwVFCES04mFc4VXpbclBccJEbX23aeH64WaYip3xkEJMOPntUN858LbiM3ai9ZuCj6cb7D0HB1RDJTRDDZpKey4mV-3JMeX_OHXgc9AAx0v5VC6LZRJ0Qz5SlGY7O5K5PxiEJj9vVydUfDOYBaSK32m8eHeGop_P_77ZezxWasFuk7EI3kKZelC4nTy5oxLvuqwDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
واکنش‌جالب ابوطالب‌حسینی از رابطه سرد بازیکنان تیم ملی پرتغال با کریس رونالدو در پایان دیدار مقابل اسپانیا و حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25485" target="_blank">📅 00:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25484">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdNQmIsC4oxpTcbAUO6P4gzsaPSRVx7kUKnG2xf7u2MSnNRuaqCTLVCCoXyb4gkKvjEzeSgAVozSRrbZOV3O2ra1fQFHuO-G69NKvr5z3ltgHBMVN1NqpuNVK4O3ZT0RaBer6qp7BtOauCpCdfFzS_u7KD0h2U8EKRZk5CocINZkQOw-jejAgsnZpFj72AP2BDhD7rDhjg3dDKQCzghC_syJt2xKsT6-OUE4WtwpC-OXVaD5m6gXZbZ25yMaf-2QuFxPPnNkEVdZr3KplFQVOfm9W7Wgrx5jr_xv0ndds_YnxYxbzx_iMPyaDEC2-hJz1kFOevlhiAeNmpOleHW8oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25484" target="_blank">📅 00:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25483">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rrw4nbpPShZCTHJaisvphWKqWy9i2bn5p0eui9D6thjU26kxCEmNWlGFU0J7DpxOnR5DbB9sWkmt7VFbu3RUx_UdPyVx-pR9YIbZu6tc5cQ5Mtwi96D_Bz0cOQEAark6WSu_f8hLDwmId870WsAJg_M7la4obMMwrZLxYxCD5Dk5cs7j9vmu4BtOH-eSD28GNybrifdXj1pbYYGweLH-MGiX4CwtOfU1d7ZMEzz6P3A340JC5sjSgS55IcJMYwe95UK85mUVoRx4bVw1w46zgbF0O4ZPwxh0kaodCS659qxukxes74dBuTze2gv097FshMymB5lfyOqX5xKhHjFl9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25483" target="_blank">📅 00:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25482">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLlCaU5YWkzkPKR1ZtXKKXOzBLEkXYT_EGBj3I85D_9gMJlKnJqWQGdTmktLg_vNl6EyonFneZiIDKTTEkmYA6aIy9MDk3KztYIQDhi85U6wai1xEVw7JMjD6cF1xC1jsrTMrW4W27LHCr-djNX5Lm-QLnlp8Xs_xa4ONMqTtPqXLi4i4T5i99DAGW69xeKfwqj2PoAMh2qPAdyWQtxmFJsrxBVyJeni9DjGd12lmFSB0ysoM7wwGFzy57m7bOX_9tWQ28c1ABfKwsMoKgBQa_AslSzRRoSt9ZlH0s8XX6mJ6U0F8Hr8SIQkU7GNj0IFDtlVHOnygu9_Z25b6dXL8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25482" target="_blank">📅 00:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25481">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aG4oHwypla-u9X-Fr8O7qcVqmiv8GY6pVXlDbzHNPl77rLLgB5n6QdZBUBD_Zefe3MEiXJC4g21EVtXuaZoUaQV_HClrhXB56QFyrrAQGkNf1hhwvKGSNRP1SOL4gIy9jUpksldqDKH0GoYoi85mIQQuBNeCO6CupPcXJUQODWMgqYUztij137-g2rFmTYQQ85ZeFuFMNs_VLrGYVJ_r1THe1_jiWvoOUgGj4cWy1VzAZopw3qOxKuhoLGt-4hP8Fih3vzGv7T7uOWPDwNyDJxtkPcG_8CWHFchaEwxIthIWNzpv8I9vmX5q_bh1AdQGuVFeUArhW10cr_5Z7TVSAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25481" target="_blank">📅 23:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25479">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mizdYwoopXr2iM53k91mMPd6nEZl8-31S04EDblv_VFzpkZS1F-zztcAaNKKEcR-gjxd9_oMC6jLC-81ca9qtACD0MXZo-82azPcqoN7QM-qxTJdEtlP9XJqus7S36lxDB-p564jZwh9-D4F2xc-CII-HKBG9U-KJ9rcuPetP8fGvM5d8FlVVdVOc5s-dZtjU1DSv7q7N08hHXwCvJATYiELfco64VQUe3HRmbQDOMw04ezVPrY7TXt0Ah0TQadYZDfttYPW0KntrF-_ESmXvj77hfMrYVjrIGXgYh0ExULjcmkSFLKjdLlv6bk1lDDqd0fwIDOYij9GHjri3dS6Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RPalqxqdLsoJJxbAKn_S9Y4o-5pQLRLgohxxIMt9-KgLhsGQBA8V-txlA3mgbH0vZfQ2dEiKgsrs6Ir03xRE159LwmAIQiEGBm3-yW9IEa9O12EN6SgirxTHEa7zATqM_k0x0xB56PZkL9_-97KbRAncArwLnajqckEcYf23OjqkEiD6bID8YSRVweDULd4lD8o5jLOYnFcnl-tVLgyL8QU_-LbL8u7ruziEWJuszXz_qSzgaflKTHhOXFezCmKtdzI_4ubOyHtmIQOE6PSDe52qwr3hPTGLZO9jJ_oA8Ifd4n2dZ5I2_DbvbsnYas7g36lsVscPXI2HH0WOBMm_RA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25479" target="_blank">📅 23:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25478">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ct-6hTJwHnMvVWQ5kmmC0uXrr-PSNRirMRORd9-ldQ92QvrPsPhUQfTDa-ApymcrcmOGdS4um23asJ_8gmikyKUBXDbRPtWHgg1liV6wendFafVsqwklqZXkMDw4zsg4l05b5DEgzvgnPt4P-zKvHm_uCo_yIyo_upamqckWRGB5C9WACUN81qgYB0iXYSnj_oSY5Ji1VqZ-PgEFBKrwiEcWITLtmK83z2QAm4RxKolVGTffvQUP96loV6e5PAUW3fzO23D4WIUqLoR1Ifc-kmE_MA4YQ9-n5lbzMY0_kUOnNHtJCvLLwG8e77nHn2OgKQ6vGVYgEXvUotDDjBYDKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد سرلک در حال مذاکره با باشگاه فولاد خوزستان تا درصورت توافق مالی بین طرفین به این تیم اهوازی بپیوندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25478" target="_blank">📅 23:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25477">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcTJQFGgft1SWpjaCOhjhsSuYvFetrDr1JZwHW4DZF0dLXh0YkmIUAMSKHI_Y0qhv4p4b4gDV5GP1PYGYcgvN3zzWPu2Ie_l3Ei_ZuKBmliWp3zKRqh-VcNV53c8tRgpFKQMOQGKIP9DTvWqr6ytj4K666NdA_4w9SZJep3oWZJakTUQTjVj1mhNf5IvV-EDZKZy0TEx4omsTeaZ7jcLl2QuR2_rkPyiyrHbji8ZZqdsg9ExyrLob53nlladTVZPrPNKM_Vi4-QwO4701_08hgk_XhqmAizAXms_wOdvAntlJeYBgLYmWUS79wDymBfj1UCbJgRLJCq1-M6deFf30g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25477" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25476">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccQi5yGx0QO3nMoWeE-sNSnN33whYTHM2DmjE_tOQp7XaqREN3pty7rC4y-PQoMJAOoAYrwZZMZaIM9K3wjlCr6NiDQS8saxmysU3aWBWbqrJBWc07tcbsGNba21uxFrIR_VbBMm6q4j2IumyLnh2R3crcrqNX3lgWUZeqLk5WNdgtBlSdX3k2sooJM6xrWl6ZSkSs9CvTk5mipYsptqb_ulX22NRn1O0owDEp6kXkwwNKYKUVLDb1ZQopzYa6yYJQ8as62OdIyMcSgIXMJjruZUNdOr44zLHuUGB6xMvlBQt9W5RMgUME0ZJuhfkrs5-gKuclkx9COKTAqK2CCc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ روبرتو مانچینی برای‌عقدقرارداد چهار ساله با تیم ملی ایتالیا با فدراسیون فوتبال این کشور به‌توافق نهایی رسید و انتظار میره به زودی پوستر رونمایی از او نیز منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25476" target="_blank">📅 22:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25475">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=Cs1-Y44irDHc7gD2zBARHv6XQr0rD6-F8nLZdqNwQChu9YnqdrP5e8cgt8ZYr0EoTvJgSeNSzEYevwrPzIbdwkzLg5LsDtZhyzFgrhGNrZrFoq55xGMpcGCH-eJTfiaKajgyjIRl29b6GFUIIxBetjwSpGediq5h_g-VqCQX37mZE0kGWe9rEc7jYX-HT5MxDwtypDHj0WOBHn3XlDbizQwnXCpJFfZ6H28WklSMa0zqNBxQJ0Y_bnEb8O4R6IAU1iZVsKzI_rn2E4BFvie6mT9W-QWpbz23GLsL3BEsLDt4ePAiALdOJ75athZqBYQrg9Qc4jTzV0EDHXT8n2lf6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=Cs1-Y44irDHc7gD2zBARHv6XQr0rD6-F8nLZdqNwQChu9YnqdrP5e8cgt8ZYr0EoTvJgSeNSzEYevwrPzIbdwkzLg5LsDtZhyzFgrhGNrZrFoq55xGMpcGCH-eJTfiaKajgyjIRl29b6GFUIIxBetjwSpGediq5h_g-VqCQX37mZE0kGWe9rEc7jYX-HT5MxDwtypDHj0WOBHn3XlDbizQwnXCpJFfZ6H28WklSMa0zqNBxQJ0Y_bnEb8O4R6IAU1iZVsKzI_rn2E4BFvie6mT9W-QWpbz23GLsL3BEsLDt4ePAiALdOJ75athZqBYQrg9Qc4jTzV0EDHXT8n2lf6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
روزی‌فهمیدم مسی هیچوقت‌تسلیم نمیشه که بعد دعوت به این برنامه‌ازمجریای حشریش جون سالم به در برد. لعنتی‌ها ببینید چه گیری بهش داده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25475" target="_blank">📅 22:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25474">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIkRsdFacG3NL-xiAnHFsk7BbjbyXVo7qGdYWCp_WY8rlONBZUizBjcvH_ZewVR1fJ3PGqpaEbXlcxh0oTzLaETUvIsLVvuPOdw0w02kpfHC5dRw_p6Oe5CZij2EMMz-mV_9FqQWXcCAElFC7UqejF_SUS8wNw9lo25pcPGpoDRYglOkI3bvnEgum-nD9X3yafRJ88MJJm-8RdzVdxTWfNYb2rYYkQQ1dMeJKH40f8nGlsQ5-QqiqDcghPveMnv3qLat1LtdhehCWag9qhUG-FqN6ZWKQG5UWgAmrZe60m4pdNWwGUzslttDaTSC_Vm--FOUsTUqrG2JIu1dHqsgqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط پیمان حدادی مدیر عامل سرخ‌ها درباره وضعیت علیپور و محمدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25474" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25473">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=Tn1IIITXLgp5ANRoITNaIXr7k59DyKopQlJsDZGdVHw9lvUlu9v3JH8X_pjDhQSDC03SAoC_g7a5QrLpS267LOZE8K3RG8arlTWh2Ih9_h5xja4dm373pbytam77UFk5gZFo4gwXU2dYVMTxrgP9n8D919DvV__kXMKH0YZ3QH4yv13djgago1kt20szRiKc_d_85UGf_OxF7k3lCcHAwucZc0ntyV4LZzFRr5rYQlTyIEhYMNaNoKjXJw7uE3zBDpZ8PKl_YXq1QjxwfU23jc7OpLYSi9Wdltop1y8zfbK6H-zDjxt7WOnzuLEmkDqB6C3yh2cLhQ_wYhwK9k4Z_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=Tn1IIITXLgp5ANRoITNaIXr7k59DyKopQlJsDZGdVHw9lvUlu9v3JH8X_pjDhQSDC03SAoC_g7a5QrLpS267LOZE8K3RG8arlTWh2Ih9_h5xja4dm373pbytam77UFk5gZFo4gwXU2dYVMTxrgP9n8D919DvV__kXMKH0YZ3QH4yv13djgago1kt20szRiKc_d_85UGf_OxF7k3lCcHAwucZc0ntyV4LZzFRr5rYQlTyIEhYMNaNoKjXJw7uE3zBDpZ8PKl_YXq1QjxwfU23jc7OpLYSi9Wdltop1y8zfbK6H-zDjxt7WOnzuLEmkDqB6C3yh2cLhQ_wYhwK9k4Z_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
صحبت‌های‌ندیم‌امیری‌بازیکن‌افغانستانی تیم ملی آلمان در رقابت های جام جهانی 2026؛ این بازیکن از دو تیم آرسنال و چلسی آفر دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25473" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25472">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifwcl79LYoEcLeDlQeZ7Jb4DipjkX5cZB3rcwASO42yXtZR2g90XX65GxETlniN5P5fsJwH_iDK7Xz0uttApFEVtx9h3HdbzRKNmodUCudmv0sj-u1rIqd9JWcFl4ypTW4Jl-9osTxX-ZR45wuX0tIsGCWtNhFEvwQPg_RNudh4hiLN3DWtuHhwbNDx26577dMhBwkmV2X8Eb8dlwRYehuAc5Iir_DUz1hXWg5l-uL4KArhv-_BQPeq51Y1KUCTkBApVdTCmLR-KDPCe89cjbtzt77O-1kNyJkWISP-9sX6Aa1UswXD_F4EpeGISoDDJsuFo-4ohSfblbC75CealtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
قدرت پیش‌بینی‌ات رو ثابت کن!
⚽
🔥
دو مسابقه جذاب:
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🇳🇴
نروژ
🆚
انگلستان
🏴
🎁
500 دلار فری‌بت
بین تمام کاربرانی که نتایج را به‌درستی پیش‌بینی کنند،
مطابق قوانین سایت
تقسیم می‌شود.
🤖
پیش‌بینی خودت رو از طریق ربات تلگرام ثبت کن:
👉
https://t.me/betegram_bot?start=p6_r4EF37DCE
⏳
فقط تا قبل از شروع مسابقات فرصت داری!
موفق باشی!
🍀
⚽</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/25472" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25471">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXDYSHzvTZ32nXKFgLsFwPPhMDiSjVtRbATMSlUJZwdagSECuHVD07hy5vGDhq5Sqw5EESGBsr0hdtD_FqrRHTcjlUXTrp8KgvL7EMCGjpkzSSOwDERKBah2guTEdATyPRGzx4EwJ8qyiq8Yue2FVnznONtd6F-uujOou33v7WBuRDEEBUZe5gMFf-Zb7n0K_Ojn-JoWDqI5yd0jyEi0StnC8Lvse7q6Z6IgXj9nAzLUfk86xSmNxKxE2Cun1YWRdrGlXOI7FiaR8jiYNPdY36U4aSjhzPIiZ1jBsYOu_LJYUpuPQG-kSWh82A5ewjc_9CQf3qkEUJhpofvWrSLweA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25471" target="_blank">📅 22:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25470">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ob3VCmtltEIdialEBRik61TnFhOwCPTzOPyJZEKuenUMaLy7FVpceK4yhST5wAU8hZEYtDUJrqOBc-KRdx8rW_gVZ-SGST9g728oubC_UfVWrfLh8-NWkDu9VaDuxnFQ1h-BOFwQ6_nose8KpqE203TXiKB-AeT06i-4Cm-5mHkaqWb-JDNm_ZLC_idZWGR98mH2k87Tj9N2FO5eJKCoK2J6vBKlgfB4S1gSgleYCSPefFbWyh_AqkGXndg8OIi7m8X4VF5CcBe54AAVst9j6cRICWiC4LNP9muHKEe51M-5plYjaCoQBSJnjG-R7tJau09kBpLukU7NkSS5IH48YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جالبه بدونید بازی‌هایی که تو این جام به ضربات پنالتی کشیده شدن در نهایت تیمی که پنالتی دوم رو زده برده که این‌فکت هم درنوع خودش جالبه واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25470" target="_blank">📅 21:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25468">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=SpYuB7s3A1G-Z4arNW24YtofTJePWn3a7Rjec5brx7HXeqmslCy6HSt2_dHM7MxNEugPWAREKUEIsUTSu9aG9QsLNDOwWP2KueXz-qswMuSsk2zryVzz7c_jG-VGQd0vXkC5EWw8xMpLwFOrNdJ1dNH_74kojucKVTWbMlTnm48xsZ58LDix5jtO0fr1ctPuhz1CTSpShI-7zv-1NrptYnP1oXXuPK_lnq_qYGK9BxP3q_B8wsaVqErFwplWfA40TxzPPzK2u_WP0UdeREQt4TAhhbGNEq7qO1l7t9NZBnVaUk1zOaSVoeT5h93_V6HXT2yIKlWGf6ipnj5Conyg1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=SpYuB7s3A1G-Z4arNW24YtofTJePWn3a7Rjec5brx7HXeqmslCy6HSt2_dHM7MxNEugPWAREKUEIsUTSu9aG9QsLNDOwWP2KueXz-qswMuSsk2zryVzz7c_jG-VGQd0vXkC5EWw8xMpLwFOrNdJ1dNH_74kojucKVTWbMlTnm48xsZ58LDix5jtO0fr1ctPuhz1CTSpShI-7zv-1NrptYnP1oXXuPK_lnq_qYGK9BxP3q_B8wsaVqErFwplWfA40TxzPPzK2u_WP0UdeREQt4TAhhbGNEq7qO1l7t9NZBnVaUk1zOaSVoeT5h93_V6HXT2yIKlWGf6ipnj5Conyg1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌پرسپولیس که دوهفته پیش با ایجنت علی علیپور به توافق شفاهی رسیده بود حالا 72 ساعت به‌این‌مهاجم 30 ساله فرصت‌داده که برای تمدید قراردادش به ساختمان‌باشگاه برود در غیر این صورت قید او رو خواهند زد. درباره میلاد محمدی او تمام توافقات لازم رو…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25468" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25467">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZ6CZ7XB_HQKOu1Xq361yv_DDtmvl31NY2LL3KoQaophX6b5EOwruqpT2BMY1H5VywSG8-Ux-g8QRz2_I2PGSDyTSBTiS3kYNSi39GkqajpkZkvhOAENP8v0Sx8GE5SXEaZ4RUCnlFkrzzbKHXWlZCQb0OFdkCI9CocSksTcXJcL2y7y7E_Sk_O5WExvz1Jd0mIsYqr6B1sogHsx6P8P-3DEjKuk3v2PtEWD6h8pvNX7YK6X-wU79OvEWVWqgF5Z5D3tZSAAnzZ9zW0OT349ZtM7JW1fVtlVJReBOmoxqssvT7q571vTmz3pFpBZgStRdHcehRlaw7sUlB2WjkuZgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25467" target="_blank">📅 21:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25466">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXtJgH8M_m3OkWtMSHXuT3nlNZ5V_FDLm8TJ9EuaigrxNfQJWmmyJZiR9U3o_U04yyw6-IzNoXP7k489sEw5LpZpgWWQJWto5JtioOFsbpZv3c7eldDMUSl9kEAU3nvqCC_6-HYYGwEl3UG79ovIfVWJEgx8UIuJUgWv5yhBWlFhCcEsxCCY8Oc9L5q5RsASAthQaFrOKWGDX3x_RkDzm4V28yDr2ZSfMYH2a02jylBWlryfCcoxbplL9XcUDjrh1mSpcY-0fefNri58rcR-RtU9Ej5lSD6WGkr_rxgac8ASuU85JRmqr6-9dAWNthlHMUOQUJELBcrP4I-P4oRj3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25466" target="_blank">📅 21:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25465">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLmfrYsIh-oCDVLJB6D7vhAf4xoX0u4QqxeSBepqmWL065BtcIUy0T-s_kIoUebrZbclHcEal1V1kx9dqZ8aj-zccRC7Q1yUj_OQ9ioxxYPO4SKTwJX7JXp5MFP7iF-oefICAfZGt6xXrey4SFP0-fWN35vSOZetgc8jBFDqOuNJPZq63D3DTJGSrpvG-1uUG1qhtSqOb737dmJ0Z0crBdU7WgOet6uFlN2N8WYUQyU3rOmsCBh7Eyp91P8X_9GNuk_kI77Q9qqYqxzxBIH9z3NQuhoTm8s5NklDhsjEj6OVDjIVtI-h6SvtxaFI8JLv9b-Zfad0X4Q1Jl0CEt3uJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل سرمربی تیم ملی انگلیس روش جالبی‌برای‌انگیزه‌دادن‌به‌بازیکنان تیمش در جام جهانی کشف‌کرده که چون یخورده 18+ عه تو کانال دوم‌راجبش‌گفتیم. حالا فهمیدم بلینگهام چرا یهو اوج گرفت. بعدجالبه بدونید 10 گل از 11 گل انگلیس در بازیای اخیر توسط هری…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25465" target="_blank">📅 20:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjruKe14Rl5dYQycK6xqlnzjTwR5Di2AWEa3CLbV9uweQUOatedAuvzkVoT0h1S5O-QEJcM49klnpZO9W4Jl8NMJ8t6ydJrTiB-s42Y-IqjY070K-f4FbBmyhrQ5-Nzk6AcmsPyrb9bDfSNb6puGUpOfBlD-bgAnVJtLnRzGdmSbn54mi0JbkcmdEWtc1S0wrm1V7MiaxgCeab3eyNTf0hd_nY57a5BLFlb7QLgMKU3TCnPt58tz_CBSbqVkAMTe_-wIfPfKSMslI_L2uAH-hQePvhVTnInm2fml2Wa10L5EibtxCla6_A989PBGXUX0q2hJyfKRYS5y0nE2j78bNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعداز موافقت مهدی‌تارتار سرمربی جدبد تیم پرسپولیس؛کریم‌باقری بزودی‌به کادرفنی سرخپوشان اضافه خواهد شد و قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25464" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25463">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnBnlmlm61aMMCxOlz_5CXFbMtAauOdfruepuDW4ggQOrrqUTEJfC7OfzOB87qrwGaUOU3PAQSGgjcclLW6XsMZsR_8aXOCbcgi6kzOzsugbB7QI1rx_42b4FkPa3FA3V8aYfQvolUz7xWTcOz-dBtyDVnArDIQtl0333BUlitI9c9ZwQDloplsa92hc1KkeVZdHe9NOS9Zhv6gEcYhSHetkb8Jfz9UXqdiDveNiLWLwstJ_DWnaxMwlFPdWlW7o27lY7lD0Tm7dZIriWUjJWaAMxNTPX6GYj7piTO9SwlKC-UZZw0vB7BkXHZdVGEA5H8_OyLi7IoBT4bFm6jPAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌اخباردریافتی‌رسانه پرشیانا؛ امیر هوشنگ سعادتی ایجنت معروف فوتبال ایران با مالک باشگاه تراکتور آشتی کرد و در اولین اقدام قصد داره هادی حبیبی نژاد که روز گذشته در باشگاه سپاهان جلسه داشت و توافق نیز حاصل شد رو به تبریز ببره. اگه این اتفاق رسما بیفته یکی…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25463" target="_blank">📅 20:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25462">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EE3VFprbUER7Af0C01KdJiY7Po0NsMN1dL3m-4LqTNucdRSNDVbge47wd-u-bcK5zbMB0j9TMrBszbh5JTthPf3QUsx0GzbzDlJ53u-zjh4zjW0Fr5l2smgL2p8sYJR5wg6KAlmEYyLpk74IzfEEnB87k9KlSt-KByIPDBTiOQaGbu9JMk63zBZZnYszwC3ByLkdz8nTp8rJpgKzf9Po6ml_CDJ2y-GRprOvBLGI_BQdyRf65zrvam92YoV9A7GuFQFUHAfHYmGDHcMG7F5t8y-ZHZ8ai34JqrC4ZM3mN9o4lUTXm53-Ht4vLGsXLjk_jc7_r5-NYPD_XkhAjTh4dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25462" target="_blank">📅 20:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25460">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPGi123y4bgvzGDqi8JcB7BTmvsLnBE_GEUw8KuYfzidpZzRnCtSLQ7FDTPwXiWCHYlHPnxHWzilOz6hYzka0dsMRqNQCyf_Qqgz586HfPR2bmgM-FqMdsxoPQuFzDDar2OZdbMEouqKeasFqE51iZgYUyiP5Z6ViK2XKrjiv-fTZCZFuDOaS_Q3Hr6Lb9eYk0yEInRLMne4-F30bFzCAg3RE4m_kzSeOg5xSjWBqOah4JFzZSv9NT8jMprcBKUO0I2buY3wNgGLIOHXjLAF9FI9IzVYvKTKWG_zo-6F8hGcoRUi9hNCH4zrbEoZnSio51ZWeBtgi1MNxQ8JMEpVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25460" target="_blank">📅 19:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25459">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjXq0i70G6Bt3d8RGr9J-fYeBxENaRd8Lk1vZ7SVyaOyaxKmME_dcXEqW48Jy2m_btB9wUa8ZPP6t3pKzF2HIltqcupy3F66EI42MPOF9p6vDjRr4QAOEg4VFwY4g0IZS7P4H0xrau4ycLGnJEgsP_B2ylKdxQvr-Exodu3tXcbAlXtoDrd1uy-1us_l2msgvt0p7T8vdaIOaQovQJyWzTenLj3X_Etx8ZJsxt97H5Ktf7b510qfG48sc6oVjSttF7DkIcAuCRLbM1BEJhtGPu3Jx9DID9PxNkl77lBfEiOUrgpj_OLuIE54t5PROnDG5_355rx6BZ0DMQzKNg3Odw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تقویم
؛ 12سال‌پیش‌درچنین‌روزی؛
بارسلونا با پرداخت تنها75میلیون‌یورو لوییز سوارز فوق ستاره خط حمله لیورپول رو بخدمت گرفت. آمار سوارز در بارسا: 283 بازی، 195 گل‌زده،113پاس‌گل، 13 جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25459" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25457">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=WsQzd_xN6P8_4dEIDHKkziz6wkxCUE9NWOj4NxUgj0kk4DEeKUaXBpEYhywtYS0b7mGQ8B9Xya-X37JDLZ55jfyR-drJ-obOrlz8xQd7R-N6u-_7T9LF935vd5CPAtK4iSvfWyZSFM38M01LE_Ohfo8x7vLE97fkVg2yQuatPqbbDd_z8ECXfiz1ovcZOvXqH61yw9Bl_EbhMqIA5RX-9yPc-_7aLvSj-todcNiCkEqunycIVU6DZdVIh6hTZLCUFGqdOLFvWVaCKbeSgLWPG_IEQh0KieCjyWYOQPenirpHJKluPIukbeC_bWRQg85ExavTxh-6gKqMAOPG-Bx0yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=WsQzd_xN6P8_4dEIDHKkziz6wkxCUE9NWOj4NxUgj0kk4DEeKUaXBpEYhywtYS0b7mGQ8B9Xya-X37JDLZ55jfyR-drJ-obOrlz8xQd7R-N6u-_7T9LF935vd5CPAtK4iSvfWyZSFM38M01LE_Ohfo8x7vLE97fkVg2yQuatPqbbDd_z8ECXfiz1ovcZOvXqH61yw9Bl_EbhMqIA5RX-9yPc-_7aLvSj-todcNiCkEqunycIVU6DZdVIh6hTZLCUFGqdOLFvWVaCKbeSgLWPG_IEQh0KieCjyWYOQPenirpHJKluPIukbeC_bWRQg85ExavTxh-6gKqMAOPG-Bx0yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛
جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25457" target="_blank">📅 19:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25456">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nE504YS3pUY9eGbNw9-xo0pemTnP5c1PsGyXaPJ5uoPJ6kGorJm8xQARcKWF1lhhHAiM9KlcNkXBH3nkIqPPhXGs05vTCP98sf_EN4ym3GLjt6E7yl1kRaVgdX0jKZokYVXRTQYM8hrC0DlCFW98PDPQoZpMgNr8genZHDIrYhwgpVi1roT0m2OPcqReweVHHtYv4J9PX_-hEFF_ocZomZKtSGityskI1uAoCm3axbSoxvWv-jD1hEk27Y93NXwizUwhI7BuQPO1k5aOfvb0X4kxHIQng-cDMRDOrHzevG9lzroyDTGuS374aNqjhs4c0ksI9uQEz4lqCvAUf7mjCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام AFC مراسم قرعه‌کشی لیگ نخبگان و سطح 2 آسیا سه‌شنبه27مرداد درکوالالامپور برگزار میشه: استقلال و تراکتور درلیگ‌نخبگان و چادرملو درسطح دو آسیا به عنوان نماینده های ایران حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25456" target="_blank">📅 19:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25455">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUT-0HcZhjAYLYjIYLnt0gE0QLt2Y-teHgGFAGnqkChG_NwBDvvkhXx-Ovr72cJZGpzxs2FFoTy7QJkIGBRjAm3Zy6-5uNPy_fZJfC8pal1gDy1h2N2g9uz9YPV3jT9MbONzYS8AozM-iCl4bukOLPWak_J5jIRnfXS3BYEi89U_qUIGy7mq-eotLWzd_s-AShxzCbfSba4pPiWuMBiuOqaK6svt4LtwHevi3rkeK81B9oWshw0wSZDOPOPuv4QNIWaUTymKvcsZUPGDcR69l5Teoy8NgxcZDGS9R93_WzdicJ7iZTC-m_H9xdEhkeDBGNwOzruiAr4gG0W2YF2pDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
کریم بنزما اسطوره رئال مادرید: به کیلیان امباپه گفتم الان‌بهترین‌زمان‌ممکن برای انتقام گرفتن ازاسپانیاست. به‌هیچ‌عنوان نباید این فرصت طلایی رو از دست داد. اسپانیا برتر  از فرانسه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25455" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25454">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‼️
خاطره فیروز کریمی از حموم عمومی در برنامه دیشب ویژه برنامه جام جهانی شبکه جم اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/25454" target="_blank">📅 18:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25453">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKKu_Xsz2iY6C-ZzyBJyBnFUshifUjmKcgaq8pyJoT7bXh3fWgCJ5LFbEendZmQfSPxuB7WEccyXAb99JZqH3pXRGP5hQcuS1jvZDmRNHfdJ-4Gb3YilOjOLZa-hJ81JkFlXs_So_IlFZyLBOaI0DEuIc-Zc1mPnNYRZC1yoKlGDsBrXE_WenMGICb5L7ltM8fXUJQxkbomyqorA2nBBoSauIZ-BrdEPBtR01u2QS0ew8JzVKu4uZYKZU1vps9u-8vCfKvUFTPxfHFb1OfwbFHELtZFOUX-hSGfQP4M2JRdAAGN5TPtimkew3eCyQUXOkBiFs9TlidAgKJrTGc3NCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25453" target="_blank">📅 17:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25452">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrCBtJLN54-ssalyTYUA52tsIsPEpX69X3jysbagR7Zg78lbcCSQXIqwStkTS9E2fIBz5K2JxEK5S7cZKbJVjJeq2lTwBrwW1YM0D7QPNHau0zFEFI_IxY1z41XJTaL1lw2wFXPxMvDXryKWFpaXY9lulAaBcJkEOX-gQKpCG4q0ouSyQkle4skyKgEGMouFXtyz-Ly5F82vXJEH0zEyIAH0c5nqxhLouURedsZ8n17WiPWAJMWlIs2QZaSm2SKnFO7WgowLw9YtAEeb5Zs10RNYh6azNp0NqflMFeQwAxB7dK1DY2ZQFQuDwx1LtQ-N5GTkkaEvRfMXdTfXDhY3IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25452" target="_blank">📅 17:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25451">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dj2Xx1g9EnNPsP9wDtVIjb9M0aqEyoi75GVBx6Doqt7YSsP7cnB2xzbwgwyGWXBRbyModhdcnbkvGX7ZiY-ebLG96BYMRw0Vi7jV-pvUekDnvVXRlxLwsMqFZwsuJixg1gI_rbx7FOC4guFlQyZhkPz5Df2IsaQQSlXO9LB6E1C6TWA5WZYLYavmWQ1QyUzaZyfLWLg_M8IHPkVgVs3_9aJGplgBQ2t4k1WMkvdu0rab2k7Un-0RZ5i0KXmOHEA8SnQengmZtfDTAXaaU3IFl_FsGtkmchNsEo71UkgJJylvMgeYy1v6nAXyCKABSTel47UbvtvGgpEZ0Gv76hgeYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علیرضا بیرانوند دروازه‌بان ملی پوش تراکتور: اگر در تیم پرسپولیس میماندم شک نداشتم یه روزی مدیریت با من هم مثل وحید امیری رفتار می‌کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/25451" target="_blank">📅 17:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25450">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLGTQ7lHm-xeIS7B-rVAvrL7rfy-9XMZY_ONEv1aBXLYgZly290EIcI2Zpy0am8i-YKCItRnirz48ruzJ42LLbY112O59qjV29rA-TImy5770k7nDRF4dyR8LknNsE7NiWyDPPbNHVbIJhTjrrKGcCwiU7cxoENdojqpta_p0Q-U7gZPXu534SnqwcvbPevAGsO6H3pM55XHuwTVTgiLcjqMDa93JbYti5T0IQcCVQ576Ml2LU4fDemR2aRKPLLB97lVX1qoSZsi2qs-Ah7woQzY-uqKU-d-3OQXZrS5AsATmea1iINnsfgSpVAponF4C4GQ5S-GO6CHMHejfQ6Jtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/25450" target="_blank">📅 17:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25449">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2FxefCWiTuk4eweP2I6zGU57JSrIfxQJ179aMmzm4YvBinvFAzYdZbeNWp2lunN-L40jP0lkLeJ239SGWfywrC7_4mjq2dJ8nCKeCrDUrx0w-ukE2IVyNJ8ODyLuNHlV8GUBGUAE5v1moQ_DtkTfivAD_bz1AUQwf4a6x2BNAQ169YV-g9y9LU4BNmu9i_rQlD1kZoW7TTIG91f0mFX7iiqTS_fYIXqtHYB_vFoviC_VA6JO2xZY4GUJCm542VwcCaoNakWriPFEDcS308QjgynloOX-ijYS_qX2O0nNXsCOqdBqtBYIUyY3hAP0cTt5ipy6cfLi6AYXKlgaAWASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
خبر شوکه‌کننده دنیای فوتبال
؛ جیدن آدامز بازیکن ۲۵ ساله تیم‌ملی‌آفریقای‌جنوبی که همین چند هفته پیش در رقابت‌ های جام جهانی ۲۰۲۶ هم به میدان رفت، به علت افسردگی خودکشی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/25449" target="_blank">📅 16:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25448">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSC575gAT8GTJMULE6V6-1R06PM13EyQiC87v6HfZ1yUR7hHxSeQMMH1lMQ6oVE2U-57GzUqh7VB0_vGeb8Z9wbKbr1nwGxGpJ9m4J1Tcr1N_6AiUPuoUb5IRfEbRXq0NY_NRvm5myUp-Y-p2_2i9GRb35xXfhDmu-sWG9gAi91tlR8291LivwFcoDQ00SkdqFnSebek2HLoqkWYcQP2vnjET3i1JKVOknAMgm3UhAPLnyMpH1gWzgxRaptuoGoDkrizdaqQHS_mU6Fy91MpWUezKQIaJ6B1ZX23OE03i6D6RiMFh6KzkAtLs3h6eKXfWrfWTf1oa1m9YVAWqUOPgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#اختصاصی‌پرشیانا
#فوری
؛ باشگاه گل‌ گهر بدرخواست سیدمهدی‌رحمتی خواستار جذب ضرغام سعداوی مدافع‌میانی 20 ساله تیم استقلال شد که با مخالفت کادرفنی آبی پوشان این انتقال انجام نشد؛ بختیاری‌زاده به سعداوی گفته به.سبک بازیش اعتقاد داره و در فصل جدید بیشتر بهش بازی خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/25448" target="_blank">📅 16:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25447">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1u8DuN7FbKq-WNnuqoAVKmDI7I8birveWtB5RI6maWYYL9BgdEQcXq6C3xyMbaUP8VUjcylaG1NULPMx_PjZPXaMBRj-XzPNWHvBJPQX9If5c_TLKy_WVE3rvzvNnNg4zAeU3PV01zm21RuiCmb78S_Uj3PFpBTKuSNWGR91NF-14aQBSwNq46bly7qfSI58bbcEWOLGrXnLwB4qmuPklu4IQGSOZNcutjVkSxDPyMY-Dmcez3RghXoPt3LZaZLxvqsMakvm7pZHPwvykMkhwxB64DqC_BEFx8N-yQxc3Me73T2i3upTzsszjHwDOFzBY3lDYEw8vczZE2qqc7JBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/25447" target="_blank">📅 16:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25446">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlB7WYTM-zDRW6p_hPCA-1XzvysH64EpHy6HbH22GX5ch3-V_lA-JB6f9gEoHRSEn-cXgmRgWDWhZ7Stox1t6GoofFfFzbij-0wGDCcUvcL_T_U6nVK-mloafnrnVG61y1p9KslJtUw8r0T1lMD6YeGaxxYShxIgGO486J7wyO2aqd2sH3c0bCXHTKQ8tWNFixsbaCw2MQmWpWNfedl_Qy2Kouo6XhvhrwJR-hsXrNZGuugbuy9utiZaOM1taH5WhrcqPRAU6FQV0imAnoGFdk80F57M3U4jGwHqYzc4TdhSyO0qIOc6XRGZwW4AsARZghCPQXN001zoFF1dIdmH3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛ باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/25446" target="_blank">📅 16:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25445">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tg8Mn_UJKTwjSpx-WAsWb4HGV_VqMrh0qjbHxKufz-8DerZfyD2AeQdnkOjettAsBLKUk9a29qZFoS_yAbA3BrXWGJ0Gtt-x8Zfa8_uu4yEHT5JO2ivyoDdokAPQ3NRwMSa58J1HshtSmz2FttYoDF60J87AjjgcfT2czA8x25ROv1pciERBq5QujY21lkT8V1MBJoufmuaolcxDGFKDaGn3gUH-gOGD-SKWUw5Nbczw8jeXn-bUIJ-cgYDbiRLzAVod-3eMcM7rbTQKf9H205ViqLuZBH9i7YXW5v4wbOHLVMJ_tJPf092PeJzYQ2SL0RfH-IJz67bo4el_WMIHcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/persiana_Soccer/25445" target="_blank">📅 16:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25444">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lG5TYnhn58imH3CnQc-yaM8dncqjJ4fMPzDoI8J7oeH_JYgc_rrXgUliQ9i1SjEGQ8s2tQI9TwP2Fco8epIcMnvhhbGNPaFKsjPvW5iVpYv2LLSmhlLZRoxeBvJ79qbN0hYfh0HsHIhiqVqtMcuj-pXeCzmoh9-Nk5aANl_a6DFmmjRa5_Zuuo3O5Dlc6cojcE58suPcsPwdeaZ5hHfuixJGWeiEVn65xLmUsCRs1ngC79WqGxWluDLh1fNdbnrLdWvRGHEPtNzp8uik0iw93S-ofHJsFtmfjh8Ho8JE0sX13fvGpCNY7vrTem-kFCSMKAOomHlgKrgl37nuw3cmug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/persiana_Soccer/25444" target="_blank">📅 16:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25443">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcJRi2C-U7ejG9a0a-cMo8kdUUQbCXeVROxc2-rzB8JtOEJX3J0Ibozxhtk0BNwrZDG2va17CpgxR4eunJwmDkjLTB3ooYcsDPIF2zj4s2VtVKNXamp-Y4Rc3V_Ionu07LJ7X2NpjofPPNAw1WmtJf6NAInBnSbT_WNL67mFJmiPJPhwEWZkm6Rofxd1THI84Ak1ehYD01Pwg1kowbT14AY3uoD7w6Cm3v0YZbTK0rBa80xgz2enziBkG2ICHuMS437gwa12NXIgT3OFh9xYqlHgIQwYmwCaHJ5oqcYcBbJ5289q_GiaxmB7SoJYeTevseon1wkkb52horqfEvpjMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/persiana_Soccer/25443" target="_blank">📅 16:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25442">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vo-ICBeFpb63XTSgp14lG-g76-VRl5bwWUbWntfGaLQi6Ag04dFZVQ5455WLcFJZnsWt3V9MZlHlQhYDKLjOxPKKkhZLhiEAweT0zzYYGaoeHC1nEMbF5s5kVB2Ki72E840VJnRJMe4H2xJTRpd_rOMODpXmDxLHxdCHRiH9uRxfltgFsnqHuuJaP3vKwJkrVtrNPiphpPwDg_CM5Ismqub_vspK_QJZzcygOO6eA1rZfqQedOpCdTbdlN5-oA71w1COgJnuFhd1GnWeHoHhS5RywKdAypXxdWbBPez5cLfn7mtqZSEiCoFisEdEpsg8DvmVx8Dd3Aav_8o3HJpVEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛
رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/persiana_Soccer/25442" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25441">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ad7a6bb4.mp4?token=c5U2vu540q9n4cjeuEzjRMLR9jnD7IL5Y-9Qv9EPdzha5nBoFDTiZoDasUhM5qWy5kn-XsxTOPC3KEK7QifNJLo45DhRo1lDzo6pfK9K1iT_Zg_ccgjxgPfwxc6IuYecXqnhCvoqAdLBuOMJYmKK25kqQNgSka3P1cJmt3hHQ4l8_vfZfc8z6YMuqvtZxMxcoD2ZxHu_cR_DcgLThlDLR1JrR48gatSm_Y4cJ55uxKpJrZQfJbCtcK2s0Z32PM7kh1loa6QF-SrWNTXJ_rFhR6KDxwry6uGY2tkQ2spJUlScUjkDnL3vjaFAqWy28KfoXH1rVTOyWEvLZ8Tm6scIdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ad7a6bb4.mp4?token=c5U2vu540q9n4cjeuEzjRMLR9jnD7IL5Y-9Qv9EPdzha5nBoFDTiZoDasUhM5qWy5kn-XsxTOPC3KEK7QifNJLo45DhRo1lDzo6pfK9K1iT_Zg_ccgjxgPfwxc6IuYecXqnhCvoqAdLBuOMJYmKK25kqQNgSka3P1cJmt3hHQ4l8_vfZfc8z6YMuqvtZxMxcoD2ZxHu_cR_DcgLThlDLR1JrR48gatSm_Y4cJ55uxKpJrZQfJbCtcK2s0Z32PM7kh1loa6QF-SrWNTXJ_rFhR6KDxwry6uGY2tkQ2spJUlScUjkDnL3vjaFAqWy28KfoXH1rVTOyWEvLZ8Tm6scIdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
خواسته‌تموم‌پسرای‌فوتبالی؛ روزی‌بخوان ازدواج کنند و بچه‌داربشن، بچشون‌حتماباید اینجوری باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25441" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25440">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBnhmXkWOm9rq2jQga9D7orUGXp3KW8Ng3pwDVYJcETO32gOoUQVawd0Wc6HoJpJtnMfTwa_QCj1UyY5qsp10Y_5kXvWxhXpBKM36DVwflm5U1o0rSmHxuD1kR5BJMA-58xFB-cPMLDeGJKNqg6q4SBOugSWXdQjR7zyLNCENh-BZkxLke9hbtvGvyLt7nCGIb-a8a-Pe6W9TlvHVlYU5P9HEj52ydWi99r49x4rhnLdyu-U9sSJP_7nDuM2xxl77s5HjfQeKIrjzJqsXF2K7kSddRuCs8MwMVf_r71aNEckSa9B7IWreyegcywnomecUg5kHL5Pdt-biSuhh2ZwOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/25440" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25439">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ms6jlGsi12kqbP6YGRyIEhwzroAEnFmBOLF4vO_ufrooJXm-y-dC_2nkMX0Vd7y85U16XdpRmHEccg38qcgpXKr4MOg2Tc3XG49AzyRrCjCZs4a2JqTTKHWL4tCsNHYA_zAbBKtWvZ504vWGlyV9L5VidEw4G9hH7vZll4VerbidXfnfPtiT7133W8-3JrewqrQ0adyZk02PXp3qvHSlZcqWahpgIEmapWFB_sluiHWhWWfDZ3TlZqqG3Tk7z8OOioqHAD4n56UjgKqr4MU8YQu8VY244f1Cd8ycbDL6Sj-DypgRT-VWXk30GVpkabICQ7kNeJwrlcrTmzgImNJsYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
گردنبند جالب‌ دوس‌دختر لامین‌یامال ستاره اسپانیایی بارسلونا که اسم او و شماره پیراهن‌ های این ستاره از ابتدا تاکنون هک شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25439" target="_blank">📅 15:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25438">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Antf2eo_9Rnv55uAlYm44XSLH9EPQYBhuBqKdisSt_k4xHhfUWp5TydL49tyxwNpZ7R3TV0VKYPBQZFUrxRNTNczZoovnwCmPiDbESFt0K265cvOFWyKW605R9EZwa4Arqa-6yWxG9qZgvhFyg0GLHCuWcp45m-XKFsLNLDKdVUBPj-6XJKEU9JdgmXvHxiLxzv-eLy1wsz7jVrWcK27sfe9R8-mPF9As1s2R6S53h9eV3jrxTFTXPHl0IfEFlzmqp2PB5UHzHwn5ebjcST9z5pUPB96PLUP5cYW_kVK0oyD2XBdZNvlmIB8xnlBYNrkKIiP5d3D53TcKUxoE8dnfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌هوادارمکزیکی درصفحه‌اش افشاکرد در شب بازی پرتغال
🆚
اسپانیا؛ یکی از ستاره‌های پرتغال که درلیگ جزیزه بازی میکنه بهش پیشنهاد رابطه داده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25438" target="_blank">📅 15:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25437">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfKrdumXfsrTR0KXaxMNvVW7MYU9z4rEa0RRoTWGcrCFgd4N_UU94J1xWQtFjxs7HVzWluHd1EK-twniSyDViK_kkWmWhYxi5jbuEEQzwwvK7RkXXFhmBj93UhnJopGguEuMShDEAlirqzlyUSNKSsa6w56IbQXQgClnEWTdyKwd8NYG1YSTejxjR3e7XGwqEEGe-qL1xaNsHYmS3bD_cgMLmS6DnF5HyVAWTEyn-uuyMBRP80-fk-f8l6U1jNUKg98NaOGEKq7TFtRp-AACiCksBzzZjv_Or7KRj8qgBgAHpLuS5OxhzXPhJ3Js3sEVR6F7NvljCDWlckBeQmPKmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
نشریه موندو
: باشگاه الهلال عربستان آماده ست که‌برای‌جذب رافینیا دیاز پیشنهادی 80 میلیون یورویی به بارسلونا بدهد و دستمزد فعلی رافینیا در بارسلونا رو در الهلال چهار برابر افزایش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25437" target="_blank">📅 15:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25435">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LG0G98pXmejpjKRaFeH_6lLTRyxPBxZUJeSVXPQ3uS91BdUnss1iKpaGAU5s-PXELHsppmVPmCQGaT_RJ7z79xbsGkp5-mVRaY2OGSmi6wN3VGmrxT1qMO7048bFeBciCcxafRs250Ts9Br2WJ5VgaNmJbJDFGJ5PcCLetRRCmlF7PR1AUAInByVAemwPaN1WVZJMQoFGuQe7LFwCXgEZfV2s_KABrjTdjo9pr_wAjgiCfXi_NYWaNXAcKDuLhteBjZsD1wjPmEm6WLNmB0ApZaebscSvAfN9hOm-roYVAGcaNz0zIg3GCAAWbS_gaPJ9hc7c8TjE0ZJkslxfJ2czg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KPXZF8vPI8rEASJqClCohuRFB1b0V8E826iRbvKmQSvJMn6h8GrVupxw-Xg3nNLDAoWJrKb3ic488SA3iFEyZ3akD0bfuYLcQRXzjySvPBUBPAZtFGy-4HWmhKIG1YNLKqOaiAlLDxqZ8jvKsbfiKnbYiFASY9tKZumNtqOHom99QMNosJ1u-_QItql74nk8yJmyK3gd9foDqj487Z5z9qy6mHpU1iGT-76rHMK-r9hGMccCOaUNUG9czOv7rswcZudwEtimFrorFWawflyRriqln1OXCTpsW0Ue6phYnPv7Jrkq5MaA4ZVOh4RgIabj-SdHB2B8F_H80Ev6Azkncg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
جالبه بدونید دوست دختر لامین یامال قبل شروع بازی امشب گفته‌بودکه اسپانیا دو بر یک تیم بلژیک رو میبره و راهی‌نیمه‌نهایی جام جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25435" target="_blank">📅 14:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25434">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=bPpoEXuY6c5R5fiqiQ5x-KCOi-RNP9scbyXvqFyBvDiq51JFLzY2ooSZQn8hD0TuoowD5FuLBvTeF3wHniK1nPaPJdqzQgCdPN_0z6cGar0FdZM4ed9YogpANyD8liTdopKVmVsmq1dB5y91bXna0KaY5KvSHshvi0pdpTt7j33AygM3ZS7HMF7PHrdkGVcN1FUV418S2DBaViVCxAlOvb6yWPTRxeKhDD869vLqp170KgAF0ZAQtIj5Ap4McHCnw2k8LdWsojZhrEszcKJubu86bEINxiB8SCcZAohQeh__6aS99mP5aRxM7rjBs_sFEb2p-lRn0trpHzelnytvKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=bPpoEXuY6c5R5fiqiQ5x-KCOi-RNP9scbyXvqFyBvDiq51JFLzY2ooSZQn8hD0TuoowD5FuLBvTeF3wHniK1nPaPJdqzQgCdPN_0z6cGar0FdZM4ed9YogpANyD8liTdopKVmVsmq1dB5y91bXna0KaY5KvSHshvi0pdpTt7j33AygM3ZS7HMF7PHrdkGVcN1FUV418S2DBaViVCxAlOvb6yWPTRxeKhDD869vLqp170KgAF0ZAQtIj5Ap4McHCnw2k8LdWsojZhrEszcKJubu86bEINxiB8SCcZAohQeh__6aS99mP5aRxM7rjBs_sFEb2p-lRn0trpHzelnytvKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
آندرس اسکوبار مدافع سابق‌تیم‌ملی کلمبیا بعد از این گل به‌خودی که درجام‌جهانی 1994 به خودشون زد توسط افراد ناشناس به ضرب 12 گلوله کشته شد و پس از 32 از این حادثه بسیار تلخ، قاتل وی در یک رستوران هدف‌گلوله قرارگرفت و براحتی کشته شد.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25434" target="_blank">📅 14:43 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
