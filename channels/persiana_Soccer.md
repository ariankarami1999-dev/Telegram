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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 20:18:59</div>
<hr>

<div class="tg-post" id="msg-25541">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/persiana_Soccer/25541" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25539">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2qRFCsvvmoXcPcpaOteUXJB0Q86EKl_YlbmeYtyuzQJsWu97wxWzFRnE6KeclpDNEFzrJDMRUlU82eXvi7Jjc2jDSRp748RqKSLWz20jcDs61OQXEwO7hOcbAqZhdVwbXQ381Vu4FrjBFTLejA1OYrK7yceK7KKXdoD0Y7d7bpAUzHNBBzK2PHP3hCX0TA13FE9AUGobxhS4J6t7EnkhBTNi9zO1oUIqcBBXqEGxvENbQ-X2GLNcjYIrSuVguWwf3FTZV8IOSUIdmGMxRyZsHUIffIHIhHZG9apIkP8TogATGOK2eIS5zUqOaqacXDHAo_fXXVxlb7j1J1i6BmiZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/25539" target="_blank">📅 19:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25538">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmHK0Nv7Ar_sqCUtuG_HRUv3m15unE4eR_WEV5g7n0uIfnA-sDTKa6WHlNsx_h9i9q14YFS5UEExjZIBddGeE_Pl_j7QzIThpn5r7JRi3D1Lre-X2mhXc4x4yGjb2kIjA-C_QCIQ964k930p17jaD9MEbE2DjxwmuXqxROOsmJ0shmsAyjA0-alvQZJ07uV1gyXV2P0Ar6Vak4D6Ar6QciLHG4tJ9waVdzO9mZC7tHXnBTO00Uswo4JSLgVORZkc8RPLcol6CSqCyWdHBQogKlDQPSRjkGuqCQTzB6VNcPIvTXLq_YSmDuQI_4TpggPiH2CZcSNNWVScqttQlkV4nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینی در سپاهان موندنی شد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/25538" target="_blank">📅 19:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25537">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QT8lysGTSIcySF5T6-moibako0eIPYYtwpqzqet3cdYaa2vsy2jSXd1Qy2b1W6nu8e1RxEmjBLkM4z03OTKHhV5E0yjt5X9Tpvy_Pkd39VvueivwqYCAy23e_4DVSaQ9PFXBYMwBwoST2fGlJ_x02KTI4-Q3JKGtes8xJtEtC7c5612f7bALddACDLvs3Ei-UvKgYvylBbGG2QTmF1-pUo8OBzG4_VYe1Y0oJdCzph3giM43Nl2iWurdlFb3xrkC5gV_hzK3pG5F5j70UTfhFdj0hSSI94DD11ecL91xVcLAiZc-nL2LGD5DDf3dVtKV2ErkufsM-Xfd1ylirzMR9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/25537" target="_blank">📅 19:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25536">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/25536" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25534">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHVBM1Osdcs32c4gYd1_TwttiU6nhkWtAYJQXR2Tam3TbXnVrQpT7ulbaSuhewIEBYKtYShD4cmUX7HTjM2Gl-fZ0pSePrr-Uy_StuPWecrilG2FDR9AMEyMJ3r2V0Ix0KLehRFYZYt7N0Bxg1NgweRN7d_dECKbHA-sGC2ZuTwly0lkYNXcPLFmRI7tuso0nJ0L_Aj2uBVry2c6ELY107sJtMpq--Bx0dVpIXHCeG5gjYtCEydIPc-mOWokGdiorjzjwi8V0HzZtpqELgJZWYDS91rwnvAe4mMikQ-lKodgjn0DJWXrXOX3EwgUZxLiV1biAyAmqI5xUFDXgPc62Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوسمار ویرا سرمربی‌سابق‌پرسپولیس در انتخابی عجیب با عقد قراردادی بعنوان سرمربی جدید به دوا یونایتدبنتن انتخاب‌شد. تیم‌یونایتد بنتن فصل گذشته درلیگ 18 تیمی اندونزی‌رتبه 7ام راکسب کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/25534" target="_blank">📅 19:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25533">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iyi03NHvRJKZWB8-FK86aXpbipTzw2obiaQerUYCwKWF_PT4sw4072m0MDWEWT150XK31QLz2s7YeiOn4uys3_QllsWU2cGkFelUw0X3pz0QIxay0F9D5a3z5mPrSK4XGXyT5_Dv7scMrVRMiCKkXTyyQIdp50ks76EXkCYI9QwI4KF9R0O0mNXxpuOOb0R7Ws7bWlAc-2OeXcZq_NU6U6CBtBSC39zr6unzb5LhQ9hgUXGeYtKpR0hcLbMhfHtn_Xoz4O2t8zmqXlVNXnZ-s5_eIBxHaxNUnCYF-Tx-rzn_JRFPQNqma5u6vVvxR786VWPYzJrt3M1z77Gtxkf29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برترین گلر های فعلی فوتبال جهان که بیشترین فالور رو دراینستاگرام‌دارند؛وزینیا بادرخشش در تنها یک بازی‌مقابل‌اسپانیانزدیک 16 میلیون فالور گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/25533" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25531">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/25531" target="_blank">📅 18:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25530">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/25530" target="_blank">📅 18:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25529">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/25529" target="_blank">📅 18:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25528">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8eD4u8ga_x2Syi5_AyL3wlv7Akdxrwa2eKDzjJj1G1mMAHzeM3nbXc3zb8WqUO1vwkl9dP6qorm0sfKg2nqRwZzKDRbJRW2yXfx-1LnEXwF9aG5wdCj_vFhowSa8IH25c6x96Y-ZUarABPpLDL4G0brOKYod7JElOZG8eSdCiQP8GXycHL52sjKMPj9bk45HKBwjA9Snv8dprl3VjAV8fRNIRt_sJJ1cHfRNR3BrreB0smQluVGCPZluH1Qq96U7nMvgpx4znrK53dIpSwNJyYRpHRW5hJ9YRHVC-RjAUu2ToQoC0SbTwu2YkVBvwL73h0vojpY2nBEjKtZ9tjXjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخباردریافتی‌ پرشیانا از اصفهان؛
مدیریت‌ تیم سپاهان‌ با‌ حسین ابرقویی مدافع میانی 29 ساله باشگاه پرسپولیس مذاکرات مثبتی داشته و درصورتیکه حسین‌ابرقویی بتونه رضایت‌نامه اش رو از سرخپوشان بگیره راهی اصفهان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/25528" target="_blank">📅 18:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25527">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‼️
تو یکی‌از خانوادهای‌عشایری یه دختر بچه حالش بد میشه، بعدمیبرنش‌بیمارستان تست میگیرن میبینن باردار شده؛ میپرسن کار کیه!؟ میگه پسرعموم، دعوا میشه بین خانوادهاشون؛ برادر دختره که بازم زیر سن قانونی بوده میزنه پسر عموش‌رو میکشه، میبرنشون دادگاه خانواده عموش…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/25527" target="_blank">📅 17:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25526">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZQumKjx26UpqqAOTYbfEpRrljlXPfesSi_6u0FN8efem4n7tiWGVTsyjb_64pb7tmzvxvSFbTEVgslZpd7OQ4nHes-Ji-_H2nilTVFLHrLsA8p-ZPXlWcnWTgoryQH9RJ2Z_KsKSGxng2RyJ2xm1MFdbHaP2UBBB_3Rp_XTqdBk1ev7rgIEru-a7gKXbp3ApAyxeIPCDF8KoSj2ciQGJUh6mILmEHCuxBvMDJ9ja-nvJpfckG4FJ3kyvja-K9zmBn-hsd1FeLBvo8sLruBiXinz3VNToOsQZ-dI-cKIvtNSwUjqhUARaON13ob0NLGhNG_0tNIJT928USBKTh1cCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تقویم
؛ پنج‌سال‌پیش درچنین‌روزایی؛
مدیریت باشگاه استقلال تهران هفته‌ای یک الی دو بار از سجاد شهباززاده مهاجم جدید خود رونمایی میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/25526" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25525">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C52JfnNMJoiqDi9hYNlFTyc-NvyWDmhKN7zusjb6FHnV2LhhfKbQ_lVGpJ48jzKn80VT2DI6PqXNogOeit81kck60UgoRYkxK2QJT4wYCYhExQUK56c3Q99htaSmzfqMijbPfZZXHybo5HVRF1PIIlW7luRll412J0rwHSwXomf5sKFbE-bSzhQxpMKlDyoehb2osfMnRh93-EUZNVjxta3N33v7ufVhAxiru15IxNK_lIAsaGuSM6AeE7Qc5ND2R1DxBfOW70ygSiN2YLpS5Ylg1ms5Ohj5017U2untuC8BuWzhsVhX1OzuE0Y0-6c2P7a5GZjiyyA9nl6nswMDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/25525" target="_blank">📅 17:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25524">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhaR5RRxBQakZE8NvFYjHMFZN4RrVkySacKs4JVcPc3iWgJVyG7kD9ACSKvi5kfNpUUTuztbCh3VadptPIVQ1_LqmSoWvV3MvjdTj5iHBKIWzrzesxEFRtxn9ZfOxlxrYEu2ISNz8XOndhgZLDfJ3DGjb582wC4jyBSC2k0l3uZ3QXgNfeuGEDwGzpRMd_mvyKB89Al1N3l52-Xmbc5PoKc5DfZMisLsYz6vlC_a_20_yayxaMkg5WXzTzbYO5Du-qJQDXesPmCKHdUAuWyL1neXj4o-D3N3yVMhu0vekMJNASW8h6bgFwZrx1d1tzG4wZpi9hCgohBJbWXcWdpwlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
عارف حاجی‌عیدی هافبک‌جنگنده سپاهان که مدنطر مهدی‌تارتار و پرسپولیس بود بامخالفت شدید محرم نوید کیا در جمع طلایی پوشان ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/25524" target="_blank">📅 17:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25523">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/25523" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25522">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/25522" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25521">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/25521" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25520">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=m1diO67G7QJS1-405qVO0s7_ddwXFiH7vJyIVFzqc1FQNZNX405kFouKOv1NoQOoQ239tduKM0tE2WutXfLUiaUn9NE5Lhxb4LZWuLAHo8WRq4lLIGccVLB58Ati81Fi4mfOpb0LgJJ-dDIIP8-_mussXdTkTqj0NbTZhHcgiK982235UglmchNcPsVPmwTMl3Q2pQGEIHLge3u5UX5gAL0F-QAX9QADR753yNByjvFnlDpE5P5qH09UnSoehzYxthn9mcB-EcGM4Hy-R6XCNV7ZpKPK3herB64PeDDDFb9UbDYYHRH2lzK8l1-sFyBIjTrybpE9C7ZKcNHycQAz3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=m1diO67G7QJS1-405qVO0s7_ddwXFiH7vJyIVFzqc1FQNZNX405kFouKOv1NoQOoQ239tduKM0tE2WutXfLUiaUn9NE5Lhxb4LZWuLAHo8WRq4lLIGccVLB58Ati81Fi4mfOpb0LgJJ-dDIIP8-_mussXdTkTqj0NbTZhHcgiK982235UglmchNcPsVPmwTMl3Q2pQGEIHLge3u5UX5gAL0F-QAX9QADR753yNByjvFnlDpE5P5qH09UnSoehzYxthn9mcB-EcGM4Hy-R6XCNV7ZpKPK3herB64PeDDDFb9UbDYYHRH2lzK8l1-sFyBIjTrybpE9C7ZKcNHycQAz3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
شوخی‌جودبلینگهام‌ و ارلینگ‌هالند در حاشیه دیدار شب گذشته انگلیس
🆚
نروژ در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/25520" target="_blank">📅 16:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25519">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzYC-aGbpyXz-AoD-FMJnJujjYO6Ij4hSQxSpPXdtIl1NWN1PdRtOCu7weHrpmG3ADJyBYWxZAUpFw182_LLl30MQS_-H6v6P-JHCAQZ4wpphxNdAKfB51uwdz1JnAQdDIy-ZahZ8eAzrxtlBSAnFDFFYsYZr1N2SvYK3eKN9olVthy0fbnIHvLxQJNJd8OdEAHu52S59SMtQDaV_IXe3UdDp5g_Dagiixs-uGNfNx3IbgyRK1xOcq231PSg3wMGkecUEpGpu5tDX2B1rcBxb7XoBHd2JUGFHAY43MlBQ_u44JFu_qJ5C_veKcMHFXjF3-EEdPTV70BJoVYZs7MEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/25519" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25518">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VME9K4RT3iCl34PnHAZeUb9EC6RW8t8pL26tIzU6vC2jLQDO3FfBGlJQMp7GA2LX8fzSMTRmEm6UI0jHqJTsi_HloYJ66eVf-BKSNUJLhAH9OELULDrvp1pGPzPLDt10ZdhbvAYDXnJYMR-BOY0fnHfwUF4--av9y6Ygi9VH0Bk2FxOKy2GVkDdd14-C-_bgJRfigmeggljNSJnnpyr6_Yg2VQJ-5cDYThF66j5KWwxkWH1fKlNMu5VcVD6ZC-nf7LBULqOXjx7ZpSDvRzBJ3D_cAueHLsSeMfvZFLVw9j_mS1zxS5qjwDxWslQLHmi-Yv8AlkXgbzcNPf-F4cBP3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دو تقابل جذاب بامداد امروز مرحله یک‌چهارم‌نهایی رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/25518" target="_blank">📅 15:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25517">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HR-Ya7jPtEVUDY_6o7KAptaCbjNhVifM2rkX__-HBGjI_sk2sAzjZxBapvG9_lKJdQYfaSaThkEh1_5RXInbifakPw10nx-yYCSCuEcBnQIX4phN5a61f-Yq2pCjQbJN6KsKGaoY8gvUW7k7aWteJkNhcgOr-LcpYRu8q8AecHr0ePN7w5Deu0W0lp8xNh0SBm3pzgCBnKDlx46E5DMhplmOnYuxaNWbwTZQ6VPyXPY8HFVHMDG2FmdSS_Z-zjSe58KYUuhx5cLdHDH39PauFpUZbDOH3dOPfanJOvEcTnkQ4SDSWBot8XDVwj9vhc-iayeD5HlwOJ1HrJgHFOXnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/25517" target="_blank">📅 15:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25515">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/25515" target="_blank">📅 15:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25514">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIyfhm4-xXY6hvSXYdouxvh0AaY3xNrF6NIKkYjfCuzh1FCDDqW7pOFgjMNdl6gGVskEldp8z4rIIzJ2D5tx0xNtMd_A1-wB-4GYC8qOgo-wWcZgL9Ana6Z-7meWmW0Obb4eY8yN2VjGxVLIVrbTKCipv3Ra1JTj-SJP9xcw5XZaYR-ZllCvsv33NtB8ceO4Je92YEHCA0jTJAxv_r3FfedmjSuwX1xuC7D0dXnqS54NVOzz1XnBEShTY9N-bOeUhcDb44Qbzy-f6tXRTS8qcIiXpRdzJu5U_6660J6EHiWFJF2enXhAqBT-q6ALPrxUEpDR2dwtSAGmXHVXb-lo9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا
#فوری
؛
یکی از بازیکنان فصل قبل پرسپولیس از دست مدیریت این باشگاه بشدت دلخور است و به دوستان نزدیک خود گفته اگر پنجره استقلال باز میبود تا حالا قراردادش رو با آبی‌پوشان امضا کرده بود و یاغی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/25514" target="_blank">📅 14:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25513">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reO2uPjupq_eo93p1GYsEVDFlQFxvS9JD6Cxh8Nnxc7-4XHa0NN1IAoT2ZLXXSPQ1cRyzFuoQ14DIJt5jpuVey9in0v0vEcKvzTNEt_bupskG3jp9aoe7cwJ8Fq9vw9yQao_wwpvCDWjU8C-37tgyyi3VbHj76HUk7GH-AeRB8m6WbZ4QiKzMYY9WhPqDmpdS6KAOd1LJww-50HnMboCVCFEX8jAcF91Ak331d0m5yzFqDHzziExauNUvyKi9rCPzsHJNa7Eb6gyoLZjPCBavWjqq3OtUFq65VTM2fHCn4CCpyWi8EfI1VzkRFVnI-I2SULs1JgOIIpo-ZT2BQX_wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/25513" target="_blank">📅 14:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25512">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=LZiq8C26xUqwWxclyEhVH04X-F22nB6ruYfYsVcuPlR-qL_KvyNknJeljeJeLL0bKGva1LT98IeSblxViIhkzqFT88Ucsg8_pyuiVU2tqqpiZzHJvXVG9QMjakJdo59DgJB8K7r47cKii6V-zfvOiNwBa9x9T_-_j1GhJ3vHxfb4aeEO9Yda0baYHD1cgh93F-G6XPiJ6mi4HGW034x8eL7HEHy7jePehmUqmRNtjojJAZS_U4OrdSOub-RjPM8uPDJgwrfgdpXShSIVX1CUZIfTqfVB_AAtUTO2rmu9z-0zOzHN7BWjlW2ud9rUG6k6d3zGHVC8FHqtPr8DTphgbVKXO8RG2cN3r-v2VBPo3FTiiQpmQkflqZ-0UjqVDCT_Fyw8Xbyyy_t357qAcB0T0WZerMEGAhPdJiGOYoQgUX0VI4_q8S4alLHXFMyLFtmoUPd-vHAkUn4AcqmQpfjxxEeoTRaq-scowcWiV5dhd5pIIf3vGMZtEWFcPspl2TWqMBqCwQc5KrHh4QZU5oPPit2BG2pQVERPj5TcJeMs3q6GVCgS1wKf-gwnE9gUtHzaGJ56QrrLELiDCinbX4EqV9957cuII7s2Q9hEI1qdJ8ppExin_xVWLCfQ7iSw1NBRyjwb8im9FjJXO5LF3YGkulfBgP7ARlzV7m6ufzvU2Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=LZiq8C26xUqwWxclyEhVH04X-F22nB6ruYfYsVcuPlR-qL_KvyNknJeljeJeLL0bKGva1LT98IeSblxViIhkzqFT88Ucsg8_pyuiVU2tqqpiZzHJvXVG9QMjakJdo59DgJB8K7r47cKii6V-zfvOiNwBa9x9T_-_j1GhJ3vHxfb4aeEO9Yda0baYHD1cgh93F-G6XPiJ6mi4HGW034x8eL7HEHy7jePehmUqmRNtjojJAZS_U4OrdSOub-RjPM8uPDJgwrfgdpXShSIVX1CUZIfTqfVB_AAtUTO2rmu9z-0zOzHN7BWjlW2ud9rUG6k6d3zGHVC8FHqtPr8DTphgbVKXO8RG2cN3r-v2VBPo3FTiiQpmQkflqZ-0UjqVDCT_Fyw8Xbyyy_t357qAcB0T0WZerMEGAhPdJiGOYoQgUX0VI4_q8S4alLHXFMyLFtmoUPd-vHAkUn4AcqmQpfjxxEeoTRaq-scowcWiV5dhd5pIIf3vGMZtEWFcPspl2TWqMBqCwQc5KrHh4QZU5oPPit2BG2pQVERPj5TcJeMs3q6GVCgS1wKf-gwnE9gUtHzaGJ56QrrLELiDCinbX4EqV9957cuII7s2Q9hEI1qdJ8ppExin_xVWLCfQ7iSw1NBRyjwb8im9FjJXO5LF3YGkulfBgP7ARlzV7m6ufzvU2Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اگه ایران میزبان رقابت های جام جهانی 2026 بود؛ این مسابقات جذاب چطوری برگزار میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25512" target="_blank">📅 14:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25511">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDObvdSp8zY6p6LC7ow0x1a_0bV83UC1Elnx088WXaLd_u0qWQGVKzGw4t-2b9GoY7ATLMyBJcRQpEIKhhsIcBWKPPDWnDvSSzoJyIyHCAHpNxyiFf3WlQpRYQb271smZPPo0AC6XG6hGvRI8uo6Dyl7lWGaxqNY3yvKWSehWbPdTNSc5kp38tZPoCasaFr_JYSa8NCZc4SlL7RZ8knsSE6rFybCschcULan_o3rIxaTOyJYxYzkdPlefgGU-hwcbznt3Trt6s4risoUIvWrMps2yj_MwHy3SWHupWUE1KMywMbAsUq8E06QecMR42A1E8uiVHNfS7Nw_NS-ddlzVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25511" target="_blank">📅 13:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25510">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6wXzthsNyrA1uOoPxZ3XrZ6XWhtRvU7g2sVuHWzXk0z7m0JWg5hdMZKJrku1jm1kYHFYvSZdCwgljV_0AzsbNXrdth4LqwYFlAHf46Heepfrq5My1SIRceH541IHbvAKKfPvrwb02D3kiRDR3jv-tkmz5zxX4mbRS1Z2hoejZGdEuBcJPkTbw8gKN_joFoQe_4L7r_k7TJodee8Rr5t3P8XLcBZhnqCUcbqR9kx4SYhfTWuksJeuP72y_lUzmgzy-B7VoZea5yeiCclqIPL6Qa6AB2zqPOFnw-KmkAYbA0WNJnnw7YSOrzY4-E6MAEmuBZc-YkJ012q2_4JqFHhFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/25510" target="_blank">📅 13:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25509">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkZ1Ldb1GlfROK8STbZawO7U2kpYNA8Hr-weRwtjf3ib5dT3JpTvtrRWk4LwsOg3aqCgGyfgErdgrJC-iw9ghIlVHvNqRNTsKpiUHxPUNKDRtAQZH2Nae0GMO_aFSHBgPGDPLjTNvWudSCtnZ8cNT0j-WRq3OH370synbj5T1Y7a7NFTlIAUfTGA8OfKdmDwxv2PzC4LOhX6MRJBJa9jbzixBIWfzqhzPMbIJgELmsI35fPEWCtnVg_aN-4XRzbO9HTCJOt-Ao-HWfeUt0cX4bvZCWOgQar-DAmTcQ3e6_6edpSYVMFblxFKfoz0sP18eXOW0wzD2J4nIR1xL33S9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25509" target="_blank">📅 13:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25508">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErXHRkzj1mAxWJQ_ujYPoMLm0TdgFWQ_W3ek6GjauM5JCEJWNz1_HcsKEX2oH4tREVkskr3RmORCtyIq3xpIn2SjsAevKvq-Bk1LGP8HLHPWBgFZbtXViLqN6cwYtpagNQ4XUOiQpBjn14Hs6CsvzPLuzo0_MxOJr1Gn2xIqYiL0G5_sUKJbdwzrfJTnAxrxi45EfMkLtv2WODo82cbPyt_gUoGs9X3Kl9TyXDMRsqMHchFZTK7DxZYOhnlNlg4vvmoRXqLPnPwyu_LTbVRrkzxpnMUj4FeiVgVqLGZmsc2CV5D-ftHXbhD95YngJp0NQmJD8acDms1ddjLfFRLEnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25508" target="_blank">📅 12:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25507">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3yn-09Esruwb5e6Gqybdc_8FsQJRfidqMVtdIGxHeD-wqTdqAKXl2GUzUlXGfDdmWwDs39dNFiHFzbz_UYb8ysFXo20zhs2IgW5D-XZLFM-K_THQ71dSGUWOT-vCnqRJlj7HobrHeQtQp5jyyCk7CFRFSw92ZMMjL3BvJIJYERDv1TbJgMlRHEtnoTDv81smrHziog2JfY8-5oxGV2ohoRE9RqEl95OBZKQxgjlFHDPNRBVvdHgXwJ6KmQKRimVFJlf2fPyjGVvsAAkXRTPFRU7cw4m5-HTP4fzNly3lGFZ0EGsQ896PJ1t1A52UzSYQsv80JSg5vtKyCYpVHzYbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عادل خان فردوسی‌پور پیرو خبر دو روز پیش پرشیانا؛ مهدی ترابی برای عقد قراردادی دو ساله با مدیریت باشگاه پرسپولیس به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25507" target="_blank">📅 12:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25506">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6pirnEhanEAfdU1fFgMrlDSrHTWqVc9_8CX53tnuyVivvqxBNwVT59aRqjAxaQ3z1nNDHZv_q6gqS4DHE4E925jLKZv2EPdYWXGjaXa9z16Ekk2bviYc67MKKkEMaWlzEyCqPqR7yGjShx_Ca-t1Aeudy5vkljMhhjnGsAA2hw-6c9yExYQIIa91AJT9AJHwyvklPzk1N6K-0c6UmIGICYbC1QXlooidCx8602rrpoO7LAl5xwUzdZ82EHmh16xv-Dd2mHY3Ga778z-k7BacvvDz3ACqSdyFVFiuEkAdRxjPdfaz4JDU0Qbwe7tIdZQux4cqg7svitn8QYZ8vWS7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا
#فوری
؛
سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25506" target="_blank">📅 11:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25505">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=I80nTItZNdTCKkfuSLXF8wcSU3FnQl5Feis8oFZZVxoKFCjgDmxdAtmJN-QB7Dg1ZV-3QsTRbX7KHLrFpn_7vGtN3Me2zCgmupIUrFRqJ1KBH4WdCjp7M6DV3cQZkZ44LWT2cznpUfnZaO1p3flpz0DvcAH7Zn9P_A2SU_OhFdgpjZ7c1zYIPGILWATPIJCK2hexTXt-zhvojkPq9DdFAEfh29sMCcpGlT9HSZCt89DolNZ-oWsXKjrBUk2Ay5d1yrKqQEt0_MXsXIRXy8csBWrr0llyz3UiX8v0aVAglAKth_CrcmnLL4SC8dvdQbFVqGlw0R1I8Crkv6vImf-B_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=I80nTItZNdTCKkfuSLXF8wcSU3FnQl5Feis8oFZZVxoKFCjgDmxdAtmJN-QB7Dg1ZV-3QsTRbX7KHLrFpn_7vGtN3Me2zCgmupIUrFRqJ1KBH4WdCjp7M6DV3cQZkZ44LWT2cznpUfnZaO1p3flpz0DvcAH7Zn9P_A2SU_OhFdgpjZ7c1zYIPGILWATPIJCK2hexTXt-zhvojkPq9DdFAEfh29sMCcpGlT9HSZCt89DolNZ-oWsXKjrBUk2Ay5d1yrKqQEt0_MXsXIRXy8csBWrr0llyz3UiX8v0aVAglAKth_CrcmnLL4SC8dvdQbFVqGlw0R1I8Crkv6vImf-B_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25505" target="_blank">📅 11:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25504">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIN5sYFGN7LxeDxtyjk4r0VxcfOGKcmWH9o7brbG2Obdw_ZzFq20G3yDVsM5evEuKz5xVXFZjnfVGeaYauFkXf4iiH9pkrRFf9HyVK7T9Zhf6ssCjsxaFe1FmWJoryD_xYjJHIeGfWUkGLgr4fiWjJeDiNvnzH5cuTvwW8KM8JP2DWugOrSj1PeAh_rXvTywr4vr05f6xksVR1-3is8i6GQIXlWc8dbiErfB0hm3t_sxedKo_DYGDMsl0mQ_zlhmRuUd9tJlAFh2fbwlI_f4KVSU8hS6_gCNKAWHgojqO6knzefD4UUnBLCIxs_hadnX0CpkPXG7N-51daOQ0m0dpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25504" target="_blank">📅 11:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25503">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjs5bxTjsfcFshbPqq9BCg5u6eOW6GOx-hsPflui3N39Zlh9UbNwsktDzrbecJmsJ9OBIT_ROIhdjkz7DDOSDu4jxaA2U8XiQVUNXBqU07bASFXexGfeOVvywAn2ArCEqd18YDN30IwQ2TIxQ1aw3Fr2JxQiuml0_IJetemYwBWnU6psXQLBpOssK_IxE79Nz1pPu4aWmwnC2q9__geMP1JmfXCvGmHQUfGbCnCRG8rG8VH1wW-F80j-EhkXG70nifxoN4edUFdpcteEz6WoW-esrc90iN68vlAJM9Q_Vh90hl5tH7Vc4HWw5ltb3_c_luSiVVzoCG4Bh7XZ_7WHYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25503" target="_blank">📅 11:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25502">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=JK3WHqBfwYN4gj_TR7N7vm2a_Kw9qpeWi62HkJlilACXSsn5p78PAB8RYrjlDsFZcNrnL2fsmHOsFe98sOBygHSylDU-moR7X38ZsBkqH283aXbGGmVinMAf0mB1qZEgf51Hyp1brcEh72MIqQJB04mZh_y4XwJ72I6sTS4u7BeX6YUqDaq7nXnrw91AhpMNARA2F4WOdQG5dkHZxPFGwH_w2sI8XjtEwixucCn4FQV7i-HWAzsDp_fuyfOCShKRKXpNBCrsngGSYcuDaOh-1QN-JppYEI29lSgZg2Te8ZrKldacnMhc0uhaqLYmSq36G8c3fi5sd22J-1bF7z-0pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=JK3WHqBfwYN4gj_TR7N7vm2a_Kw9qpeWi62HkJlilACXSsn5p78PAB8RYrjlDsFZcNrnL2fsmHOsFe98sOBygHSylDU-moR7X38ZsBkqH283aXbGGmVinMAf0mB1qZEgf51Hyp1brcEh72MIqQJB04mZh_y4XwJ72I6sTS4u7BeX6YUqDaq7nXnrw91AhpMNARA2F4WOdQG5dkHZxPFGwH_w2sI8XjtEwixucCn4FQV7i-HWAzsDp_fuyfOCShKRKXpNBCrsngGSYcuDaOh-1QN-JppYEI29lSgZg2Te8ZrKldacnMhc0uhaqLYmSq36G8c3fi5sd22J-1bF7z-0pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
نروژفراموش‌نشدنی‌ترین‌تیم‌جام‌جهانی۲۰۲۶ بود. جسارت‌وجنگندگی‌کم‌نظیری‌داشتن و شدیدا دل‌همه فوتبال‌ دوستان رو بردن. به قول یه بنده‌ خدایی اگه ایتالیا مدل گتوزو تو اون گروه اول میشد جای اینا میومد احتمالا این مراحل رو به چشم نمیدید. من خودم بشدت فن ایتالیام ولی خب مدل اسپالتی و گتوزو افتضاح بود ولی مانچینی درستش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25502" target="_blank">📅 10:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25500">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsc7_WqgsnCTNwdAUYGxmBWY55pE1AomIYjgbVSmBqOrhDNC8uk5h46_QChUy4PrYuyqt2kH3JwWXS2TVV47Qe3wDAGEB3m3Cg3m2Eo_4qxKQln6yzIFmh2wlaVQ2xkPvfDw9NfUtbbGiuLL5yCzkHmOni0AGEC34lmqhSLf2aqymrHOtpehmjIuH_eEQt57q9Q105p2CzoYJYo4wSdJvjZX6Qg8Q-SjJ28_4u6P_hGjAXJ9PddkFHTxXXMzIQ2E_SZMgrCGJqBUQWQiHDklkCn8haW_35EOzSksdTf0BSPwmDlW8fUWBOgEc98rTRjXnafxG2FcF6yzGdISelWPpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=Giiw11oOwBugb-O7_1HAixbwjxkxMRpLIcNhwlBYN6bgqIyt9hy30gJ3n46aGMQUtmE7Tumz4vxYqIFFRw-Eea_E72NHRZiv-vP3ZAqaoYC_nnu8c25ahhpekVbhD-g83Km-NMcZrMa6nUEfQuv0s170KRX_MUberzWXErFU5j9zYWp_bbyq_s5_aqzOUlIr0D2FkbYAG6O47kKzxWmzPelzumoq14gsYLpK3kEy4b4tROKRBoO5FvVHHxtZ1ccY34nbrSWivgcnK8IKuHJp-u6sVfO2ijFS0roYCy3BmLIBRTLBi6agBsQIIGfhtcddcFT9ZBaoRGszSf6oC9nrcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=Giiw11oOwBugb-O7_1HAixbwjxkxMRpLIcNhwlBYN6bgqIyt9hy30gJ3n46aGMQUtmE7Tumz4vxYqIFFRw-Eea_E72NHRZiv-vP3ZAqaoYC_nnu8c25ahhpekVbhD-g83Km-NMcZrMa6nUEfQuv0s170KRX_MUberzWXErFU5j9zYWp_bbyq_s5_aqzOUlIr0D2FkbYAG6O47kKzxWmzPelzumoq14gsYLpK3kEy4b4tROKRBoO5FvVHHxtZ1ccY34nbrSWivgcnK8IKuHJp-u6sVfO2ijFS0roYCy3BmLIBRTLBi6agBsQIIGfhtcddcFT9ZBaoRGszSf6oC9nrcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25500" target="_blank">📅 10:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25499">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/op8PhbyXCxzA2NRx2tJ8DPbwaQ2TX7J_-Buw51d38D2vmsTH3gmMfZQcf_Ua58-gOc0vhrAijeK2JnX33pUg4Ev2OPLdNb_s99Drx_O5OkJ3pGBQsKew5gFIwFJbx50cD50Y-X8y22W9nPb8RahAnPMMjD4GQorweBLzukinh3npWz0vBdFN6ShHLDUbvnr_zBR7cg_qlqQ6kvEMSbCvlr6mn0TaAxm-kJl-pC3m4W_gRqJ5EcqlAw7X8ted1CXRzLribHjIJlDCIiI1Ykfwrx2d5f7ozZWXOATZ0UJgfu20e0jE3JpyuCLzrkmdHOoLaSe-bCGMBpVFIjY5H9QUsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25499" target="_blank">📅 10:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25498">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5cz05sCyvQQDN33i_l7jOCcsq0AXHa0Xetpg8iY5xVWymUEsfTN3PVYJk8ZGHEgLSgw-2AaP9r83apWQlcUdbb-9qDHa2eQbpW2QUcwh54g7FQS5sua-EArfZ-hw7z3g6Jv6PMpGZNyiktWNSZR9uFuTHxmqvlEjATTQBbn6FhSsEOSO_7xpH1LfsrG75A-w44yp6tvFha1VF7pNbbWldnjYwugVuds0jNdP5CQ2-2pzeBZsnoctt_EKWxk0ZvxD2f-yD6_fk4Z5LRcnU09LR8yiXPmy1QFlcITtJWQwqYSTSpXVuzgUeRXihTSKvmFyPQzAlk7frDxswBgjZd4Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ جلسه مدیران دوتیم‌پرسپولیس‌ونساجی‌دقایقی‌قبل به اتمام رسید؛ نساجی‌رقم‌رضایت‌نامه رو550 هزار دلار اعلام کرده که حدادی‌امروز درجلسه‌به مدیرعامل‌باشگاه نساجی گفته تا400 هزار دلار حاضر است به باشگاه نساجی پرداخت کنه. قرار شده که ایری…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25498" target="_blank">📅 10:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25497">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=a7RTOHXK89NYfTpn4c5LuZ4mdZmWzDZ2DZqOAzeDuunpa-TvtX0U76TY4G2gDC2K5ccKPh1B44b-Cwmmyz4xebplil2cVyMroyHv-lt_eUNfoyBsn0phiec2GzdUZLCdCjahpIAn4zy5pYMlYIaevvO-eVu3tfVCmfeYLya4lSATS27NE-bDBbbkD1r7fz-fWExJKcBlLT8siM1DFd4G937KLyU8LQMsfvHGNsdxE9HdIm6wAt-d7LDt6dDNT7RrNxcuf_-Ho-WQsKv93CSTQ9M65yGsYqR7gqEQBzGEjwS42I-5xYCGHavHG9EQ3DXyWyI2yOq2xN367hL4JHhW0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=a7RTOHXK89NYfTpn4c5LuZ4mdZmWzDZ2DZqOAzeDuunpa-TvtX0U76TY4G2gDC2K5ccKPh1B44b-Cwmmyz4xebplil2cVyMroyHv-lt_eUNfoyBsn0phiec2GzdUZLCdCjahpIAn4zy5pYMlYIaevvO-eVu3tfVCmfeYLya4lSATS27NE-bDBbbkD1r7fz-fWExJKcBlLT8siM1DFd4G937KLyU8LQMsfvHGNsdxE9HdIm6wAt-d7LDt6dDNT7RrNxcuf_-Ho-WQsKv93CSTQ9M65yGsYqR7gqEQBzGEjwS42I-5xYCGHavHG9EQ3DXyWyI2yOq2xN367hL4JHhW0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس‌جونیور ستاره‌برزیلی رئال مادرید امروز 26 ساله شد. او تا کنون موفق به زدن 128 گل برای کهکشانی‌ها شده و همچنین برای تمدید قرارداد بااین تیم با فلورنتینو پرز به توافق کامل رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/25497" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25496">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AExBb_ICIFNwI4-IKnekMadF8-tdCpdOeY_fiEpjCaHxTPQzx0WNnafR7DF6eGUr5X50WIjAjWXLsQJG5pRkHr5TkQCyFpIjiqshF31ZyukYOPOvuXyDMcXIjaivazDMwFIp877F8b1Mj2wSUNizNBcDtSKYE-dvgAELnQzSgu3G0XA4FrdbeUqWtZ_rdEXD3A3FoeDORlg-HjANTfsaHvnmktYUW3CPooFf4KyAIGKvm0oP-sDb_xRq1nyUaUalfdEiwXKbDgqAfkLEoyq7SMc8msVtQwrxY3vXPJV_5HsD_ZwO4gx8uwvaVOCpWJbK6mOqX6equE_VoPYEdDeu6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/25496" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25495">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=RzdHC5hvihpwy6SHd0ib04ZM56tRx0qHlGUB0ixH5Xah0CD4tb4_5C-6ErU9pt68thFFnZbAqgwvDgXaXwjTW1RcdgBVEm8y6Aau82HMZIDkq2SLkaQuklgwWT2v9xbAnO-8hDy710TrKENsdtT1oRScOlt47S_GoKkOIyqTScvrkdyhREVnn4zJky5uz7NELpcV0OIs8DUuG7tHnIHdQ5KB4ewVIZypGiLuAJ9wum5UDWF3S_P3V-j5dkN_VtaA9HBrt5L1Clzi12AXjWEMOYfWB5H-bh0QeOXOhf6ZmR3KTnVrWSXc6mibNxOor_mnHYL5chdVydzBuVuSAf75UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=RzdHC5hvihpwy6SHd0ib04ZM56tRx0qHlGUB0ixH5Xah0CD4tb4_5C-6ErU9pt68thFFnZbAqgwvDgXaXwjTW1RcdgBVEm8y6Aau82HMZIDkq2SLkaQuklgwWT2v9xbAnO-8hDy710TrKENsdtT1oRScOlt47S_GoKkOIyqTScvrkdyhREVnn4zJky5uz7NELpcV0OIs8DUuG7tHnIHdQ5KB4ewVIZypGiLuAJ9wum5UDWF3S_P3V-j5dkN_VtaA9HBrt5L1Clzi12AXjWEMOYfWB5H-bh0QeOXOhf6ZmR3KTnVrWSXc6mibNxOor_mnHYL5chdVydzBuVuSAf75UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25495" target="_blank">📅 09:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25494">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzuwr2dSyztznUi7HbZibHTCd2Z5KoAJfcluyQb_MapY8jYDkE6AEqBDmFC8WjvmsbQBiRF-XvBPhpByleGy2XmRzxt_kWqZNOfDByIDN2sm0r74uGu47VhOSP9wejK6DMCXGz7zlm9Hk0BmanvHYfpXeh_wRfV2-2ARzpw5oPagWS15FnjBpGIWJxX0_vduWQs9wD5Xy1VRhU3-hXDo9n0q1IbUAJpPjCO8aVaC6FWVZm5lzDxYq1H1VVcbFesteDar_-zHf96GXRVtG4RETCld4GsufVwAXiYcGdjpoAMDR2JmKYP5-cEjHanFlbu4UWK6YEOCqyQeYquV_rrb9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25494" target="_blank">📅 09:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25493">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cW13vwv3PBCiY8g8lYq_ddzjFWhvfhfqFVhsbsSXwZeOm3qlulGJdmlwhpJw5p2VEtzJ4z4zr0iSYl1asAYBitcx7LnF-Rcl1ByhtCzF0Hg-TNYqG1bM3D87xVs7Tq5ZbZg5pWBKcdNuZR0JZTXPNZlqL-5NLtVLJq4dW41L_GdbEZKjiKmkNOE-II-YE9lQEH0d6KFciUFpEFsxc7zoCHB75eu_MOFUxZvgLVBnF-EP3Xthmst3G_KMHNXztthKBb-24l0y-LewwvnJsMb-yu4fhj59mtMX3xCAetsa88RENHHXi1ieT9kwxlmkxnd-KLClNKcMzrEX2hOjKGID7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی‌رسانه‌پرشیانا
؛ فرزین معامله گری مدافع چپ پرسپولیس بعد از تمدید قراردادش باسرخپوشان راهی سربازی شد و در فصل آینده در یکی از دو تیم فجر یا ملوان بازی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25493" target="_blank">📅 09:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25492">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25492" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25490">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UtW1JFAaeqGG395rK7C3gnKVlaAuHywoUDoMbG7ZziEPwpOF1N5Es4LHa8zcd-_g40btTCmExENQQZTBPz7k2N466o8kzUScv5cxta_XsUYysYLwBx_feOCSRWgmbITmFlpAcJoqRbNwNiowzvXHNXu99H8-XYDYdSxBDqE3XQgizhNf2utyQFvjVcRBm0E9Ws2QDx8W3xF6Rf9l2gG5yVE9O6MHSRpZGQldY4z_19FQgmIXiEB3D_8tuMm_aFs4atqBX9R896TtDdyHBmOTrW_c_cNPy8h7a_r5mpZsK_FiqUSoGZU5I7f6MkdDOf2PQSA47oDFzG_XJithV5dtkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uEb4YrNt4Y6QHmtOfwIthDjjUUiOoSdx-AAMdXPr1vuPrrDgmjs1rXBwUyNTvsMYGUVikFuAeazL1OuL0UUfDuwUEXvgsP64q87AlFXyXH1EcV4JQIgZrBpKUibDFA2NoetJLSkO2hiGUr_4W9MEi3c2QDhDG9xKeCDqy8Sh8LialEKb4UH6IdWXF0yQuuLHICFMnNxzryP8VzV_Jg2FFDQ_Jzi0evRvdX_2ITGnFhOuzIqyec9GoeULBtA26lLZMJHsATACC38sKFhxI0YIXMMFo4Q9_zt9NoPtWdOq3JQ3qpIyHOiYGZbUcXkZaj5EDawCY1NlBmkTZ-C8CLulbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25490" target="_blank">📅 07:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25489">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFr7nF_7-TkZalUegNlas24SZYXjlRqvZpkw6G8jokbkAHJlOUiim6vfiqPMupg9jPKCyol_3mJoOnl8UegROjCErsOJnvSjZPgdfkH_Flvw3M3uuPW1F4h2v2HFjP1sO00uVAHaWXPAtI6VIOd7cvW5CjN-tQ4bX0nhghKCJqqbOx-T3hCefNVSBbn5W94PNmfgBqQVYpMQwxgnF_F5K4_sQPN6QwznSSVdPiS8zc-IgqWvHumG-661BuCP13n6Uu0xL_RUkAIQw8cVtW60Q4s5Db_iojkjqXoMSxVp2XXDtXPyYBL0LPi7wCXRL5QvNsw7VmqPc50lWLUSbLHgxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25489" target="_blank">📅 07:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25488">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDppeimWbntjmFeEc7iEUDe8bi03-ZrYcuHHFGq0L1EoWhi7Iy65U4FzsVL3tLDfnwYuiUWQm88kzZfxpe6RfVmuOQ0811lI5fPYhE-_GyuMxzpa3D0xl7IBpDwYR0Z-s9HON-j8x5PsrL-ovdXlrIkzK7VMO1_m5M4kIOGZwzuk7MQgB-t1MB82CkFXhGqL8k5vCLYBY1WD-fU85c59981-_JTeHjL3OlHdKNsJ2Eg2HJmOj0m9Kagj6Vr5qcfYRuA7nlpqhZueJ5OYpJihMSOFezg_mUJnfnGBdj4PoQblO5jrtEs0plapXBnQDex3sGbt_kvNKOnHBwRPOd9C6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25488" target="_blank">📅 06:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25487">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bt0891XxfNqEihTuRBkEqJc5Gfa0lnWtDT9YagUNsoPtUSGqurZ0G5VvcPuCPP5Gxi_uEv-kpb8oousZ4HuehtRM8uh6FWJMoiK_SxR917Q_qHVk4rJ2J7UW5UTViuNnGE0jHXGL7ucw1ICKKKv6D78WIKzeEoknHclmHFZfXhO81xC3xAXmxg2rT0cCo_ShaVYpa7HAw8fJLjbnl7xaEG-eo9e8fub0hkpyE2-mXye95pszj1AwgYMu8iaLh63CWw6CVS-VQx-QfXcxNjESmP3Vf9kuOemUvI21115NvHA0HCp2uH_qVeTWxs_GftKv5qirWQKgQu22ZAwIyWPH9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25487" target="_blank">📅 06:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25486">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBHitqgukVdG_wQWzvbwgHkwWVrbvBUXz4o0SKPu2k3S4Ug_2INHZ7oHaaGbBqdoDvZXNW0vG9DTgqG_XEErOsshYcOevN1s3bd1H_emeKSQkMirrB7J6ACYjm5EplPXVwwN41h0cCwfbjG2eoagWgQrzW8E0NMxDqil0num2XaIIm4Dx8EN_h57K1yaU1kP5g6jwbTlCURLOPVE0uVcgQMK0DuvgtqZ_5eLnp2awcJCTVJvJuBQirgk0HcaFAJMZ4lgsNpUKcgKZnlTQrAxvY3HIZFs0CL_4-KVntU2fuS5E4goLdWatYmvN_dqopmQL59z0B32dJlQDoLSLWLpzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داش‌چیشد که به این روز افتادی؟
چیبگم اون شب جای‌درس‌خوندن‌نشستم‌بازی آرژانتین-سوییس دیدم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25486" target="_blank">📅 01:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25485">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=XbihqHYrcfw5IwNHgkSHvi3twVabDwzBlGXDgc_07YjaCUGwJ7nK9GKL1MvOXSyT-uHBd0QF5s42NYEz7C0oWWIulouVZJc4zDUjJLKsIjDtKxLmnKDnpKALYpWWYqltgL-XIoysRyqFLkbzY-k1jPFs66kosqTT_KOcB3g5q2vNaOIDKnwRB3PUETzGvr3pgMSj8L7H7mPPJKlL0K93pfu1f-FztxZc4c23DxvGbVqpKykxOiu19gDfxolX3w3WIiT1wjkkdw03350YH1y-08nZ-RiuGk_42NMqSnaVnysZP5WiQbMk_apgIsfNJ0NxcbyH-5WTCb7S8Llq-C5QWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=XbihqHYrcfw5IwNHgkSHvi3twVabDwzBlGXDgc_07YjaCUGwJ7nK9GKL1MvOXSyT-uHBd0QF5s42NYEz7C0oWWIulouVZJc4zDUjJLKsIjDtKxLmnKDnpKALYpWWYqltgL-XIoysRyqFLkbzY-k1jPFs66kosqTT_KOcB3g5q2vNaOIDKnwRB3PUETzGvr3pgMSj8L7H7mPPJKlL0K93pfu1f-FztxZc4c23DxvGbVqpKykxOiu19gDfxolX3w3WIiT1wjkkdw03350YH1y-08nZ-RiuGk_42NMqSnaVnysZP5WiQbMk_apgIsfNJ0NxcbyH-5WTCb7S8Llq-C5QWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
واکنش‌جالب ابوطالب‌حسینی از رابطه سرد بازیکنان تیم ملی پرتغال با کریس رونالدو در پایان دیدار مقابل اسپانیا و حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25485" target="_blank">📅 00:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25484">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqO47HslV74T0CFpmj7LVSsrxPg_y_5cUUiLKxp3nI3r8erF6BcKHbBYIGvyncovaY_rDAVngO2TDgLC4GwKfWznuJ9bThxI1M6gQGvhkqSVZW2R_Tma38Ll5tYP9pVbESK9lLSLKFFojtAE4APqP2wEA3NRYgQBFN3gV87T5mJ4pf_nPxErvEsxv7IUjuVy0oSuxlt35Gpk4lY6ffMdSGXiecPCUjR7W-FdGR0_GrARy8pt_TpK07l3BQI-MyvrBUKB5_vvpghRRd9C2wmN7fhNWar2IWruD02XjnH1g3NcBwQPwjnkaouOGbbEBmPV5c2NgmsB6ByfoBz43oGt3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25484" target="_blank">📅 00:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25483">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5VwqPwqfp6EXXPXJv8A8tp98CIXWPSOSNlt62MYkgX3obGVcmfd8ZVD2O_povWZOoXeZBPrZio-d8rrqNaOvLoFF5YNqUpJC0LWvFz4CUSpujeEoPgU1kYPUx6_jlpk5uKD3rQtEyOsb5G67RylIcDDalpiDA-LZc8FwN2FZjRBNVrgHJsP5HbYcxI189ADp_ZQmlgk-oU9tD9YuyBp4wfJspeG-MJ6zTJS3gj39w1ufblvbxSKjFptXSJBY4toU83qswGEW6xxQAHA2iwzgD6Cxln2kCXnnFJoENInq_4kAotXufXMEBZ7yIYIUqFj2zhtMpIWJkj0b9HMVvWSxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25483" target="_blank">📅 00:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25482">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNm8IwuWY8I9_2zP7jzqPWS4idwoXj9TPLzYMn2UdxxEA0kagOHeJ0wcaY62KlXMdR1NwWGSUc2ZSCxywRx282Rq9szI2EWMXW_s1I8P4PdbZ4N0x8ry4FfMjpYM_z_0Q4tDo-aOwwBTHdUhtUeW50bGbnnbpKPDNoS3EnCXIyigs13rBcC1YbX5VE7NsRtgBqdQIrPM8nn7wEdcUYWkHxrSnV_SLho2c117YVKH0tulbwgP9CcREd96bgCJJpKqGYGNaZ25mf_sHF0dA1G2IQNo_5EtBTVUHsXkta70qBWfYaJHAYY0owBDpAZtWm3nPvlz_ADDkjNZ6ciJH6GptA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25482" target="_blank">📅 00:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25481">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDJxsUYD-Nu-pcCR-PapP7PglQ2ap9yqY1Upp7osILFVZonfFRJg7LJ95H_vjxoyO9jitQyQQt-Nkxy-GQjExxcBPZkKBR8sXYoJaoO1QSoqiUpUqkYq3tVtO4kqlNrKJJH02qdhtp6x2jp7Gvs5ywWFyurmvVbKKJDsVjVv-Fj3-nk567UV04-MGkgFTCODBvWxaJfdn_6dFb3MffC6KrktgJ5oy7TNijnGlbgkJ1FV5GVQBhvuChsuudWFQ6HIzotxErVv91g6pSmRr6qD7_y_vH3A3lOymuJOpe7LIIRkOgCJgqhI6laZOiOIM8lE5MsK0CJb3-Sf7WeWxsy9TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25481" target="_blank">📅 23:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25479">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKdvx8Zssl0NzS2xEgQ-MTc1DK0vJ9es5ZTF9h9vtkxLa2ubwekys6fxvECXk7a5AQqvFlz5clyWrywmMR00dkteKl9P_mQjP6kKcWl519Dbwiv5-1bVgzAhLdHwatcmd9xOpvu3hPMpAKyAlmN0ru_IfM42couQYzbWWfXGbwhPwEGJ5Ik1L6Fg1eRZyAeK4nIC69rhgw5B26dis6QQ1OZ2d_ixwOdPEPnr2jD4nnam06_N_XR-Ld1pUvTKyyjG_88p-ZkbNRp0QFLn6eZox04OA2ZSDiqGKoMHMOB8Zqdu2WF7X9wpnJKZLC_ahd5iv6nXbnYTtRJA4OCTXomUIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JAQhGuE8voUyEyvcGV5Y5w5NenHARiOPf94w7hUsJitulnTvKfrWDrkWmQguugTtpNVEWnpzZYV2ZgRDPJabSEuSTAhHxhuitm2-XtsiRXISFit5_6lQwsMrk8LlSMtjxhW70ZhkZESgQNDswkBPUZsCYqWOicaQG5MtmjVS-5rrj8dYn1mWfC89JIX-axQXBPPUrBoDq3scILjWbcBE2GbnFsgixXG9vQNW0yvlgXDhQGXajhVXsTsq-EO-wUkCbbColQuCtcrt8rdqazrL3TSV9EVjcAFfRZGWT_z4zXmkYIza7o5eu1ensv-z65mAUmCRVdlUkbrTKBLMPtzw2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25479" target="_blank">📅 23:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25478">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebFNuy4K0BVY8DfG9bhA5dzMKDXJBAUg1aamkHKHAlUig0VN7-2AcyewdcBPubHzjvo7tKKfYsiwGkzJvcqlswkcuwEuFumTy6mjQRlVdxKN8PiU3i4p74HH1wjH4eN1bqTTjS2QYwU5lu7ey6Z6QIbFE1llFa8iUmye3wEYDaCIsCSfIt15eDgRVuROtDGfm6oCbjt2nirmDt1knG3A_BK1QbbUeZBqgfgCcIv-GmROIi23VMR8TDTQhgqmzFepI17tSed-jNaudyxcJT9are4ULHqnwlx7O-HS5mnkmIcvPK29BKd_PG3g0fAQfgEFgSIfrPSu8y-kV73c7amH4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد سرلک در حال مذاکره با باشگاه فولاد خوزستان تا درصورت توافق مالی بین طرفین به این تیم اهوازی بپیوندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25478" target="_blank">📅 23:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25477">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbmfq1Q5PjUQf3xwPf-EiubUSEr-Zir5oVYC7cMxsnpodamCe4eh-MqXmmwHjxmPzyHUlXsHKyAJnNUeYVvVpiTtkBJvS7p5bv6N9adhG35K-_d0keJyWpziTAEynxRLPNfD07HuMx-5czGQGdUcgI54LVKiAv6Fibw8tnrgl86xS8pqRlxvtleD-3_IDvFp90OfiVA3pie4-e0l7XSGea3tfbdHLySmaF7Xt2l6WggOeFtv5DOsvpSkktCq9bEnj5CVNkS3v3rZ5L1IU0EmC-HjparBJc22jYQIRkgaZZft7poFgET7HHSglxfSFfXu5fm-GFrU12eIUNplp05mBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25477" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25476">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFVlS6Ne98YLY6nAzlCrwq4oZai9FKA8tYuaNGXClq_WDlYc7rra8_lYOzZfC_ylDCSLGwFcg4_sXG7ptApLQ8lhj-_UcjZUI3o4SJoWk7-aVLxojYSLyjS7K_E34-slzmZpDA9hftIh6QM96MB6se9vFG_CxeY5YgBTmZOGh56RlNCGPFnYI_OImioZQm-Fgmesjw1O7GRbRgZk9AxXpZI9y2Li3EEUdwzrEVA4Z29ERRmpaKEVEd77qI6ZRgXIXjXR46G_xEpmJLa1TLSsaRnFHq_sguLCmvKDEibL8D3qudALJToDSC8PNxjGh9IyRdawfjppo2KTHe7mCOV0bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ روبرتو مانچینی برای‌عقدقرارداد چهار ساله با تیم ملی ایتالیا با فدراسیون فوتبال این کشور به‌توافق نهایی رسید و انتظار میره به زودی پوستر رونمایی از او نیز منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25476" target="_blank">📅 22:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25475">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=u247UcpsRdKr-VBDnx14emC95M0TLXEbFJL1etquqddbVd6c0CVhhg-2aBJq1AWXy9I-fHrkApmgL-VhdGK3oMw8XQPzJ4kOVaG87SMztpVBrKR_u-m9r8zigtv3c0LHlTUefkWretDzIPZvnTxTR8HC2_M40S05kYwsYzUY6QvwZCfjZ9y0tqC_bkLdi10Z6Wl7lHWoNtBq82tvSpfLV_Xlql9oNPGjg5XqrdQEa_eMxJof7pzN1LVUsAEDT1g3Hrrinx1ey558wHMRwY87fUPF8RlnLr8n_eLYLTH0O2G6JvQIzrTbWhs_rkQh_YiVLRI813mZmKhmJ9rkkIodbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=u247UcpsRdKr-VBDnx14emC95M0TLXEbFJL1etquqddbVd6c0CVhhg-2aBJq1AWXy9I-fHrkApmgL-VhdGK3oMw8XQPzJ4kOVaG87SMztpVBrKR_u-m9r8zigtv3c0LHlTUefkWretDzIPZvnTxTR8HC2_M40S05kYwsYzUY6QvwZCfjZ9y0tqC_bkLdi10Z6Wl7lHWoNtBq82tvSpfLV_Xlql9oNPGjg5XqrdQEa_eMxJof7pzN1LVUsAEDT1g3Hrrinx1ey558wHMRwY87fUPF8RlnLr8n_eLYLTH0O2G6JvQIzrTbWhs_rkQh_YiVLRI813mZmKhmJ9rkkIodbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
روزی‌فهمیدم مسی هیچوقت‌تسلیم نمیشه که بعد دعوت به این برنامه‌ازمجریای حشریش جون سالم به در برد. لعنتی‌ها ببینید چه گیری بهش داده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25475" target="_blank">📅 22:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25474">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lex7h46aXl8I9tVvpZvt7s7xpE6N6UpZ9aLatcX9cXww2SckZ_IenqykmE3P_dAx7adBxCWv3ZNJ_ToYmMjsAc1xnDbjyZb4qEHU9tKthRPbkp2-MOVnydidS-5qYVs_D2YPRu_4SmAO9DqneS5IcM3deWfxcq9A8CAJBpavjT-i96DCqc5l2cWd-8qT2cvQYrMrNQJwMX2BcE-0VRMmdpi4k0It71qemExWm_F75iwBIGaz24_yIy8qXM3necltEB1CcspJ-oewlj_-nnu2c4q2zaaFMobUXvvjmRkaQMQn6jy5yAmNtVQ84ZKcOoMItQFOvbHgPqa7vNg0KIKwQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط پیمان حدادی مدیر عامل سرخ‌ها درباره وضعیت علیپور و محمدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25474" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25473">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=NMyuy2MO7P1jCTd4M59zpF6mJr4AO9-f9iiutlaqezYFpwZfInLzVv5mraxHMnwLrI7GFg93ldPg82ZagK35FYaYFVZs_7ce6rrxqxikOC08BfKZwG4MYXv5y6vcNUyExHvDH2xrmfrSJd0-czYTUFxCLC5AjR8AzcyGHI2CNkKr-QxmFq83jicVoXnaMiY93O9mTxXBP_ROx8rebqDSOij3OhraljvbjsibqXrw9vNN0CG2YGhhqwvYn4t4bZHuIvApG-e7bI_mwTlPG-_zV9ZRR1XeAUDdNAheC8J56fbmVX4AuNkg4HxcWJZvdCcVKHl1kQijZRK2jfoF9F5lOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=NMyuy2MO7P1jCTd4M59zpF6mJr4AO9-f9iiutlaqezYFpwZfInLzVv5mraxHMnwLrI7GFg93ldPg82ZagK35FYaYFVZs_7ce6rrxqxikOC08BfKZwG4MYXv5y6vcNUyExHvDH2xrmfrSJd0-czYTUFxCLC5AjR8AzcyGHI2CNkKr-QxmFq83jicVoXnaMiY93O9mTxXBP_ROx8rebqDSOij3OhraljvbjsibqXrw9vNN0CG2YGhhqwvYn4t4bZHuIvApG-e7bI_mwTlPG-_zV9ZRR1XeAUDdNAheC8J56fbmVX4AuNkg4HxcWJZvdCcVKHl1kQijZRK2jfoF9F5lOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
صحبت‌های‌ندیم‌امیری‌بازیکن‌افغانستانی تیم ملی آلمان در رقابت های جام جهانی 2026؛ این بازیکن از دو تیم آرسنال و چلسی آفر دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25473" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25472">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sh3gb2MMhTEupvEjSGQsbz62jbZAJJdsDLNgQyVA2fugWB1wxrhUEvtjeGo5kxDZiCSIlsjOE-_hmqnvZTUW1Ibw_k-KLA4i6FhdFdX-yXy4_dgaEU5emnTYKpOKqioy_s7kvBm0_m8f5gR3iso-jzNxPD2inkSSw4Wjg6HEJ3zkA7_t9LNsyN5syDrzET-rYmb8g_AT6a3_zZO-280kHH2dI6GdzGM5p0Oz6V6keZc2f6vDayUI0KFwYqxKtHJQINXDo-etaWb-P_iwDEpr9oTGcbeLfrmhecstz8wgFFrsWa5j-P_xBg1UvmqtMPQ07RGSAroDkkFwzwjsJvBWQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZvD1qTpQ90cJ8DpZCqzvmyEDyKL3BOl2IhmYYmyLFNMmQGSD8fviMexk6jR2qONxV7vWpGQpLADk_uym91J0pTAdBkOFQlymMvGndwcZ_dMhNM81C3_yxDNoG7KJRlxIsEG54_zWb3Tx0sj2D6JqBiDaSMjYnGLfel71EF6PkQglNfeDCRiIsqxfckOIRYywth7BLkL52QDKn93hyrkxAWXierJrNoUHRH4ExCM7ioLo6HBuFzqq4WK6B9FP1iesaarWtzlS8PQ0WZsXmqu2Yro3wEgJZ1QZWeBV__J52A0MXLGuF4UbvYuIklNSMxG9Nc6vyhbGwTLYoWIBBd4WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25471" target="_blank">📅 22:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25470">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tmok-xccNkbuc4F3-RBYWkRIjGfNs8YUdRbw3licfN9Cn8d32iz8_CN82e0UXRZ_309f7ZSJnVbktM0biNLbk2caaZSWuSswCWN05y0f6pPd7WuXaJ8q9t7I-2eI8I-MAqjWF6izF3_GDIA2lWp-oz-jGvyuwdqYbOKCSCOeGxFdR-nKlF2RqBInMKqP-juWrL25EaIOj62i90UH687WU0dovQQxjs3Z33F8XcMgmF0xGQEgXFgVtdDsmnKF5MeFv039Ub1kV82GtyAVoe9W1VoLSCH3fCU3QvAkohs6yXrdXbYwcrIFEkjYqKa41S33xeodoU-peVSRo7E09NNwKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جالبه بدونید بازی‌هایی که تو این جام به ضربات پنالتی کشیده شدن در نهایت تیمی که پنالتی دوم رو زده برده که این‌فکت هم درنوع خودش جالبه واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25470" target="_blank">📅 21:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25468">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=Aqcle6UIAefOHthY8U6kz-_vk_PCykw03Y1PF_PTlsKqo3k9UR3aG-etq1iikv9VQWaf74j6T3Jnchc2Yz4PVn38jQP83YMMF5lgH4jg5G7VWIMdbmr5gJ_U52CwoNBtbZvZpQbSSMZknpgbn0vQgDbcsCtMtXJQs7I2Nu8kYHiNbS8cUkZy7caktQu5xdzERsEYv8dnrsu9y2_9Kqmx6QEnliQWEtqqARpcAmXvv8mrKwHhf9b-mBea0NyCIAd7k5m7qOgqEjxN35uEHM6htW6lJiFJZwVIrasLFcvy2ZV7zgoDaApMIgGFzU5r1pT7w2lXO9o6jUAuDHzFLi2y2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=Aqcle6UIAefOHthY8U6kz-_vk_PCykw03Y1PF_PTlsKqo3k9UR3aG-etq1iikv9VQWaf74j6T3Jnchc2Yz4PVn38jQP83YMMF5lgH4jg5G7VWIMdbmr5gJ_U52CwoNBtbZvZpQbSSMZknpgbn0vQgDbcsCtMtXJQs7I2Nu8kYHiNbS8cUkZy7caktQu5xdzERsEYv8dnrsu9y2_9Kqmx6QEnliQWEtqqARpcAmXvv8mrKwHhf9b-mBea0NyCIAd7k5m7qOgqEjxN35uEHM6htW6lJiFJZwVIrasLFcvy2ZV7zgoDaApMIgGFzU5r1pT7w2lXO9o6jUAuDHzFLi2y2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌پرسپولیس که دوهفته پیش با ایجنت علی علیپور به توافق شفاهی رسیده بود حالا 72 ساعت به‌این‌مهاجم 30 ساله فرصت‌داده که برای تمدید قراردادش به ساختمان‌باشگاه برود در غیر این صورت قید او رو خواهند زد. درباره میلاد محمدی او تمام توافقات لازم رو…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25468" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25467">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhaV4LerGT7QZrFfUHQKn9pNs9eCcC9L3YNWvLu7MVZVLF8mew3b5BGGW8fEcV1tM_6vtYV1Dgi8gKMDd8cYVYYTBYyrjNpjSUOT_l04YqAAMHGhKU8jr70LFM2ekrgJwi2xiudP_ANpowc5bgzeE6_LJPiBDAQw14ka-cEv1RwGdKku54f_E3b6EKpfGj_Vb-C6HmnN9oQ6Grz6fY2v4VsinBHiUScaANSZ7yis3PffJ5HRx7PtaSklo8C9rJMNzN8Ug08dpCI6wWPuuGvt4LvaLNgzdfniF9IL0NxfOmEZaY9HkASGOijtUqKwZbYZTzj3FiOJNF57MynnsyN61Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25467" target="_blank">📅 21:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25466">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiKZcemf423H_xYNHZkZ_K_GdG9G1yVhxTu-QMSmFfNlvJZpqU8WCtM_kgAaPUx7oejC25m3boXJuF2_w9FBfhsHOAc7IuZo8-f5T3el8PawvjhPjIpxvdWOjjzGWunh7nlQ07A6nYsoFblgxndEsA1H35DSKMPP6YR8vf7qlZ1JYazruUmMjVERWlTcDcDpEktQw8wqMh8wJn4LHomKbyZGBIMKCG7KzZCLOJE3ThpocWRyRlXy50LySSZZeFgk_oa-NthEXQewFeRhiKTgWbahhArRzKYBNRJn0GFf6gUgzWlX-VB0GtJbcdIaBuTXmVnnhn_Rc6dMj7Ir9KZ7Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25466" target="_blank">📅 21:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25465">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnmWiv1K-NHa4Aa0G3zwMOU7rNlyMm5ND2_j2znHifoTHb4Fbp374lLHIeL7YPTDoczc7PM0rrnX3hHjQkwchwiZdHoxeupqXkIxk_wZFDTAPsvG7tRoGK1cbNG4SqxCqYM0llFpW46zlM2S-6TgcIPv3wsNj5367jvY09XdjgfIHILPuee8cEXPlVxyJqryR0EaFoePso-qFvpyUQowLjJKCzFmykDVRYTauemrLjvIMFuvObnysyTaNzBgVOF4_-WlVJNX72KhIWHwDsrt9pvAU7-7b5wmqfvDf0Aun3Wj-HpgKAVXfXnYPa-dUg01GfZPVU_CawN917ylRat-Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل سرمربی تیم ملی انگلیس روش جالبی‌برای‌انگیزه‌دادن‌به‌بازیکنان تیمش در جام جهانی کشف‌کرده که چون یخورده 18+ عه تو کانال دوم‌راجبش‌گفتیم. حالا فهمیدم بلینگهام چرا یهو اوج گرفت. بعدجالبه بدونید 10 گل از 11 گل انگلیس در بازیای اخیر توسط هری…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25465" target="_blank">📅 20:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHD1SFBIAQ1pgV-DH_XtwakYxfqP2bCUYQ2DIoZqnwT3md4SpvnzMddYkxNsI5O5C5_whvlhbmVpLC85aCnnRHl0OBYwkpeKziE3QqdXOVK_ND4eMXZh1zFwhi4qy3UJpYu9yn3I6NQg1A5ZxdeGIV-AI41K5lZUemKZoTtDkOnfn_9vm8SFSBKPAsDjluqLnXu_9d_H8XPwTXVWmmBd_cEZW78gOEbgesK5ihA__RJrwTLxtsRMQBmTIkSkNfk898WVWk6FMMxWp0bjsUYgNJ9pgqbijpW1TEvbZIpo1UCQTK0A2OjW9Os9bifFDegg2k6n-LzXU5HYClOiecwKrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعداز موافقت مهدی‌تارتار سرمربی جدبد تیم پرسپولیس؛کریم‌باقری بزودی‌به کادرفنی سرخپوشان اضافه خواهد شد و قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25464" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25463">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-Dk563lOmht_MBO4kQOciR19jZmBo5DLOweo-U2bKvIlCxGgfBBONyfJAYKU1TakkuQlrmzBCUSTb4emY2Eq_y1EmSxisjuPkdigODb8KF7hqiWTLZBcfdU9AJtK4ihJQde4wo9_lXSDiW_vKMxsyc3glJT6LsDSqTZLT7rezyu7WC9-gzGeRo_UmaWzsWKrW1irJHrETSUvVlJ_6ZadMX7r-_VtvXBeVvAcvYIJooatJZFX46PciE2-RSLLDXqG0eh7izOJHXxBwyK-gTXKrE0jU2Augi0cQI_8Vo88uCo0VCgmTC9dTMCOdXMdrXfmbGrfjMxCVYy6gJgTqJcPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌اخباردریافتی‌رسانه پرشیانا؛ امیر هوشنگ سعادتی ایجنت معروف فوتبال ایران با مالک باشگاه تراکتور آشتی کرد و در اولین اقدام قصد داره هادی حبیبی نژاد که روز گذشته در باشگاه سپاهان جلسه داشت و توافق نیز حاصل شد رو به تبریز ببره. اگه این اتفاق رسما بیفته یکی…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25463" target="_blank">📅 20:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25462">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYWlkkI8jO706efeLGppVr0JkxPxHOuov836ELcwOKhunhoXwq6a3PQiqEsj8e10yc04SZ9Ut5GLjr0aAuaWD0SoHF9wNqIosofdKduE8HnPNFgd5GtKiZiQOeo-iCb8ybS0h9dDHeLxCnXIaR2pfzLzSrPvOnAPqZhJb6sv5196ClFitks3aTyzq2xB3OqlEkyLYCtlHNMXloAYDCHWecf7q-hwsq4jAQ-ot5XSiW79PxW6O5S98MBnBS0rba6cwA2Pdeq7v3tXCCOkifVxT8pQFnChf7JnpGwCAtEg8XYKOelnl7sZ19n2eO_xr8ZeDlFKAcHvRrVg53N60g_lMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25462" target="_blank">📅 20:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25460">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qW5JSOnD61g6kx8LVQCULajJFyKpndGXTBHZQB0FWZ1asNFucUyuzWQPlm7hAfDRmFD1GWw75tShhR2a_bUlS0oEpa_qvh8IfrWZ1v0jnIFy6C29Gy_-xDat_1cfqwLJLAYLsDBAWk0ob0fqVhW04q-uqD4fatagpbIAt7rTULuFnkthArdk9qg3RQNx8JXeiULlRMjqT2I0uvzHCO819lCO75IlQGMMn8qaDESJC4Vaa3J1WdL02aIHIAtdNXlNVM1WKVs3BRSVY6ko-CE5opVjTLhxIsEqZEAMy8_ZpbBIyWz_3k4cH4kW63zh6RWLRA9D1uFa6Qw8ZCX-jAIXAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25460" target="_blank">📅 19:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25459">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSj8hkxE7tUGAjxsfHQQhN-to4UpsYYjVykI2_NChYFtG_JRsM6oN8IiFlvkz9YEYCvdlXKX-cWoDOrBwzEUfiJlpCCXlOb4zDv2t5FVZRqoUQUux_2A0v5mIooa4jcj4tv40sJXfv9rpW9zE5WkhAtruo1IAyIK3CNjYESpdmAD3Z171QudFxRa9ksAvMfybGtUh6gDIxcqFJDHFoqs2kSgBjdC-khn-0pjPB1vIvLn0EGjIhwXFU5rtNu9yWb-_VisjwHXAbMs9c9TJuFlopMFQssWfmNLNxrvLjTgBnpLadToO7o1MJD76f-xrEd5wuBNSVzE5-NtdFYLxtMQAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تقویم
؛ 12سال‌پیش‌درچنین‌روزی؛
بارسلونا با پرداخت تنها75میلیون‌یورو لوییز سوارز فوق ستاره خط حمله لیورپول رو بخدمت گرفت. آمار سوارز در بارسا: 283 بازی، 195 گل‌زده،113پاس‌گل، 13 جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25459" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25457">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=DfA3AF11AqaSAkaAo1XoVs-Pd8Xwl0sllDYKFvkUDIh3ehFHdYFuYrVlvtwWn7XVJuXlvCGr_84VH9lEaQE-fQb4jQVoviUNawaxsfy97MOFANTzDLIX49Kz7NM6elLu1-hjfHzLco7pblaudVBXePKv7ham2ZdncEqtK49dqTz_JX2wR8d8mSPvtbZ8ffUsoHPBQsE3JU69htIAtu9cLywalz9vRY7BVUbSmspcIGanpXRRx0JnPAcDY3pq0r4BAYKlGy9i1nAC7hLEo0thDxl6t7-SEQ22R2oyR5Xt7XKkrviCMGiJJ3MQ07KNdoZULD6gaXhjRubl_ifCkiZi-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=DfA3AF11AqaSAkaAo1XoVs-Pd8Xwl0sllDYKFvkUDIh3ehFHdYFuYrVlvtwWn7XVJuXlvCGr_84VH9lEaQE-fQb4jQVoviUNawaxsfy97MOFANTzDLIX49Kz7NM6elLu1-hjfHzLco7pblaudVBXePKv7ham2ZdncEqtK49dqTz_JX2wR8d8mSPvtbZ8ffUsoHPBQsE3JU69htIAtu9cLywalz9vRY7BVUbSmspcIGanpXRRx0JnPAcDY3pq0r4BAYKlGy9i1nAC7hLEo0thDxl6t7-SEQ22R2oyR5Xt7XKkrviCMGiJJ3MQ07KNdoZULD6gaXhjRubl_ifCkiZi-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛
جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25457" target="_blank">📅 19:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25456">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxxoVGlz4Tqhq8hzmNj7YDM5QTGgfAG0EFAApJa3krSg0GV6Q_c0KZkGutXTwWyZQYkYZY4P9i-9VosY15bn9z2LTpqIbk80FXO7mgH6fgI9d7Gdk-GkfS0vfqxOyAY_nTYtMdT4Xr7QeUZnQD-QYbDH-kdu7q14ySQi6IrRqzB77G4V0o5-cAQMBRm2BMmpiMyVL74i23rQ6r-DdVhU-o94ccah8_632s73aazcInYaty3kyBioBW36JvCWPZONbIIIdCJmSmvQdRaPyNBvtr15Tszg24bwrpE8T7r86ze7PFt_8E0DLBNyHpHfiFUZaajgyaSt_Z4EHmcuyDYS6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام AFC مراسم قرعه‌کشی لیگ نخبگان و سطح 2 آسیا سه‌شنبه27مرداد درکوالالامپور برگزار میشه: استقلال و تراکتور درلیگ‌نخبگان و چادرملو درسطح دو آسیا به عنوان نماینده های ایران حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25456" target="_blank">📅 19:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25455">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e606WQJM3YnaIItSOkNkEio5XiMkuf3XmxMp5921dFrfPEHM9FhsC2PZlQPYf-S5ZEzP-QeSQjlwXuPF5NX0rSInmv9m4xfODAkwefA1MqVqAF9xozHPw8mAe7nRqcKBsScykk3ryGA63B5yi97VjqZcbMrJgCXOHsAKgkTlrdlar4RhMYA_2sDEVltB9E9dGq9GQQSrMV4rE3qnd5pik6MphvqxWMy-dWm-a-qQvBEQP1JhzEsUrkryBvURYBsF5evKKJYq2poeJcu7U8tBKHtf2atQcayC38-TgkwMa2ZlRI7rGPmOSbFZMplqP-wVc1dNGZYZdGMerEKcGv38rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
کریم بنزما اسطوره رئال مادرید: به کیلیان امباپه گفتم الان‌بهترین‌زمان‌ممکن برای انتقام گرفتن ازاسپانیاست. به‌هیچ‌عنوان نباید این فرصت طلایی رو از دست داد. اسپانیا برتر  از فرانسه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25455" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25454">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‼️
خاطره فیروز کریمی از حموم عمومی در برنامه دیشب ویژه برنامه جام جهانی شبکه جم اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/25454" target="_blank">📅 18:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25453">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzYq42bgmkOTsFYIuSC_f4hrwuoDl0StE_Q5lBGOxferLe6f6M0ePa6lqEpZPfrvTJeNrXxe_NUhGTrf_J4dmKQdu_8k2S9MRLcpBnqjq51oCeAe5DcBqJglkVm5aVcdE0hvx5QP7vdGctx3m2WAi5SAbvWYBkp2S0muZ1Y5Epa40lD7qzIc6asAvLDGlSSqUTjYQM_n_-NkKbm2sNF578_bEc9WevzFBiqQUOF4Aaf0UozqAO9XSzoIZqQmxG87OUkgW-Z6ymC5aihh1Ru0PKhn0jNDfli2lOLSWb593V5coKDRHtXdjCYjWNc5IMhBp0SP-Gug0xIEYH7ggkdCtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25453" target="_blank">📅 17:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25452">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQFbnmK6JnuB20ll8qWIoeR0N74tuQijhfFLikCoeChJ5vXxkWbBfX7qISxIdmrbG20vB1uZlRdqllYZXcqR8rdGeBlKle8ssyv2r0fSF9WJhV1MarCIpDYkqt4dqlNR07msA1Cwm6O1nd0-B8BF4l9MJksKI64ZUx8HPQmi4Zg-_6xn9TKYx91_cFiii2XDeKrM4XLBsx6MLCCzjuZcYE_7CnMuZ2zKJY8SGd2vewJR4UgZeTEcljDvXUOwMw-Zh20439dzw4RIAtlb7e6VOSth3AESHdxV9ohwXj37BfEL5J-LVXv4z6ZZ-qrhRyuKVXlQ_8bI4fPiSc6SZecMVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25452" target="_blank">📅 17:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25451">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnZRbKmxliYzIDSx1Jo54L1ZOGmWU2UQEcxoQLM411ve9aW2PtDd-NKYTLvoXvB9WjN4jLnLAL7CDa5y39-P3lJCUEMlB38u5atoxA6ZkqlW1NH9pWd00fPHLPwq8p0PTWAyM8aMkSpfAiWcONOxSmX-_GpS31XVQlX0iGmqV9Id_L7Lcr0u_dUPtp4DSD5w9qI_c6TNPm1QZqcFppyEWlQNivS1pUULaY4j9N2romJrvrYkWhw1SlkXn5jmakt3W059JjXbt41_qHJO--GjS_z-2v84-m_XCz2hkGCx3nY1EjqImnMCguoqiO2rWCY3L6AG4zuUhpKqRdbCg91fWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علیرضا بیرانوند دروازه‌بان ملی پوش تراکتور: اگر در تیم پرسپولیس میماندم شک نداشتم یه روزی مدیریت با من هم مثل وحید امیری رفتار می‌کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/25451" target="_blank">📅 17:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25450">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alRMyDZ-HTmxiXK6hNNs0qWRQ6J4LhYvdB9HKY3zpJbwbnhx6opYmRLVcHPlaPSXlngmj6z-J4kFrNDNEIUyqn6Q6PXDYSS4PRGPmOiZXMGDmvrXzw8VS-0uKdj0MWEQxvLFyNTDXjf1ygtGgj6VjE_UP3mc_yBlnptMdzj05WUXcXdp-msEqYshw5LKnCDq2XgNQDTsHLrbImVa6bMhTxDgWF4HJgc8a2DAhg8xbYKNqCcSNAB_bVnHeH3qUyKGvfTNpUsyKcpRkkbRjdetQL-cpcltTPPUAh-EwjKu7_hJhFX5cgL1FuK6MOFF-JckQ5iIeT6NbXJgtu5kBtuZHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/25450" target="_blank">📅 17:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25449">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blsOAS0lsqYUImyw7vcDJpIkLjb_1Hkz3-KEeMbOoaff8TNmJ6ORHqISHj9dgdjfWFMngFvJcwop5Mj8Hmsqae91JefQlZUWr8-DX0PkSeFQUOWzQye1V10f03Dk6OitWzsvhMYPtip9iYeZQ6XrE2VNSW3rdWzNuhg-TbzmjECxs8AhP_YxOgWQsU9kuW_4ub4gcfyVskvQuW7BIMO_feJwnMMg2iyQAL523KWnKzvRb3LERt6n_OtPJwSyUBCEGBMd7oXiA9HKHkGOsYTMj-2qcBSj6zwiEAuPK7l_3RH7fYXH7Iisxyog2TPTJW6n504PbnAEwHq-w8mpkEVw3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
خبر شوکه‌کننده دنیای فوتبال
؛ جیدن آدامز بازیکن ۲۵ ساله تیم‌ملی‌آفریقای‌جنوبی که همین چند هفته پیش در رقابت‌ های جام جهانی ۲۰۲۶ هم به میدان رفت، به علت افسردگی خودکشی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/25449" target="_blank">📅 16:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25448">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3aAOzqc-Vm19_TwHkOe4dXww3bpGKwk8v6nxTGaj3YGCAiO6bveJA1K-hZ1PWAQBAbIksx3RHCOzphR7S30B9ni-oPFvy9W9XiQliCWBE5fiQN-ZpnP4kMVxB-aX-8LOUfclNYZmFmasQEOjTeNk5Xmuqo66VVqylWMfv_JZ3AJQROtwa9IT99VbDzcuBB5vKT0ArgiAzhjsJBlotEB8P3e_3Nt40lrsd8cYjur6lJuEQ55bMpBv0yZGPW4uab65nlvuB61CqPlHiSI3_kLaSh-3-tpuI3afN9Jo83TEII5b7-YvMmPP2TqZPPojsaPWNlmoyg9GfMFvBCjhkCtkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6a04pvOZChmEfmfaPCC1rLzJIPXfkgxdu0rqAb3CoiKSO3Hglt5Dyld0mBB9uhOg4ylfx4ptHGgU42ci_BFqgQqgiXWgsrVtrHrvfD58XCsH3mba_p9VIct_U2A4knqv15314v7Jqid1F8VAtXGYyxdb6ihchZ1JWcoGTubvgiQQcG_XDU-qpVnm6ZR6tS7aHIQXZ413h9xi14irbNxkGWFoFaXSBGH3hNiWj4gTTNRp_OGQy85QWq0X39i4kj5bpmXFyZaQFUPGWFW5k4zQNJLS3_CcGYpkdWnguKvlK8Y2rnblJ6JDwEyA37WIL9tNffEqonWykqAdXYZmCGVBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/25447" target="_blank">📅 16:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25446">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJIzur0r6Hh9DnDP_lpTAeJK9EpfLU0IX-hVg2QNd8D52wpTuJwKp7uPcBTa5GOqtkQvJbOqXJ2c2D2P0X46hGv_NjWVUfYzRisDBcNcOjgYDS4MhIkk-yXQ59WkN-oe2Sp8dow9B9FuL1DpHpcOObuZs6c910NcKJ-33enwg3AzP9TPnmPrcTdAYkVYRhUxDET7_-2boefS8bSWZDIt2qF0U-zON23ZPcdO5Os2LxiTJdxcOwHr_TH3xWL_ZjpxcQTODH76KC8_4I5mz5ll66H3uUulzcK5xPcu2umcGIqWqdzCfFu8p2BGZ6-tLGDq8BWnzsNbDLcxZgxykoy6vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛ باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/25446" target="_blank">📅 16:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25445">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jw9cS6Xv20-7fQhW0kxe3d4B4Aulqn145WhWcvIzSyOMpWBazBMzcZqEOr9BX0pIjK3p3c5C90awZrD4BTpxxQiJkXM13HF5n7LWXzqLa1ihx7cN_QZqUJuGT4uxx0Ql6buGHN64bjU2ckdCuQC12WaePX6TzBv1GcRnVkyEF-IeYGFPEF1e51UxnqMci1vndraKwqnMRCdStY0SZObPTxumKzefVB2SAcF3cttmh-FHpnDLYmpAJAltBGb5KZg_ScNYJzk7k_fjxgE8VJ3EwJE8v2Yr2rJRAAhSMNF3oWKurqfnphA7q_5qG3htAZPuzF7x6yO-8st-3g7Uam7acg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/persiana_Soccer/25445" target="_blank">📅 16:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25444">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVhl38ZV11bZ4_BY9Zs-clFAX7tH60GW65VUx51ZKRKeG67hkQTvpRu6LcNm7mN6bYjne0oBooFa4CgDnhLczBHPq0rtpYcyB6-1H7dN_wazfefo5lE7o9cnn0JoM9v0XYuAJMfMI0oxgNYJuHB7-oCQ_arydh4j46ZqAPfzKIzD2cNTFpt_hiZc1CyC6nHwl-zBm9QK6YsqSZuMn_ndePZSQ-W7Qk5xMpNXAeRmsbNOg4npo2-OdxPA4J8aH41mq_w8ruslPQck0an5gFno1npa2unYP-a8uI4Bhf6ci81eyFDOAcULsmfEzOJEH5tOjtUxDl3D2vqo1TJBqsty7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/persiana_Soccer/25444" target="_blank">📅 16:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25443">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvDH1b8wH4dChlSHovUF2b9udfi0ETB-7GfDr48MqTdVfFD9zIamkZ4nEBYtviEIiM22aSWXgj3DgXCezLvlICm7dTyasPwc-cPeq6UrocQx8HbM4OnmUbM68BL77aIpZsWbMCcMR5OEtnkIzqCRj8Y5KjgqPy3vsDsyrUPegbvNLbFJxvW-gxf9ZmnDdNekE8rM44xtMW5Ao_goH6cP-31gEpwfu1U00MrxBMIjkMEeSwRAc5DvTZzCrxGIYoPzNgaq8Yoy5VVFgsQaBG8oMifutA3mB4LlXSxviMrKTIPoX9p0OHSRiHW9zZY8pmXchovn9uh-goQHgJatnxPvRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/persiana_Soccer/25443" target="_blank">📅 16:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25442">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGRsozCZ43xOndkMMt1vJ_hpcAtNasZbL138FKrnEsI8xOz0pRzwkM1JpUVuAT3tNcCDXZTUIJPryVAv2iXCIbwj0G7hsVsPJ7grv2l2nQyVIGNOQW3X1v7AIpqeuAwVFy_cH3m8B2jYyndV4pnuV23aga1wgPiyjBT6WQ30DAUTuu3pW7o7yV38cyOBZeEpHE4drfGY6RI72GU0TMANHFzQ7JRdwEaN_uBzUDK8bZCat8_j-gvhoxtgdm01CsEvUW9n6aECo_p2CW-PbIiNqAn_SYxPXSo43O5EbmhzoA_xm-ybEXdX6brd7NtPT8yhsxRgdsA4W0AOPWPYeVPfKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛
رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/persiana_Soccer/25442" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25441">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ad7a6bb4.mp4?token=QQtmTvYteRYuClkcnFfpLKF0mNImyrRLS58K5j1lM9tmr75y4vFM1xviTwBZOIRl2-YAgqKH2Q-FRWGEdWp1gEl5eqME5dATRb48CyUkitrc-l_I_dkHoGMroJKu8DPcr26UY7CB4_CVnErjg0P84XdP_m5vCuPvnodjUtmRm7Le5Dv9W78ZLUGoBwFwTVkA7sFwKoAg6yjErV7fMGILT_QsdkzIrpn0rIZE28h7Tzq9TxoiVvahZMpVytJ5BSUaKMd_NOHy2KYZBg2IRXuFJlW8vZg1toQoh4qfbhL_3uTjXoU8vzEdEIocUGYZLlAgmTLkt2NSfLW_36CXDfOuuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ad7a6bb4.mp4?token=QQtmTvYteRYuClkcnFfpLKF0mNImyrRLS58K5j1lM9tmr75y4vFM1xviTwBZOIRl2-YAgqKH2Q-FRWGEdWp1gEl5eqME5dATRb48CyUkitrc-l_I_dkHoGMroJKu8DPcr26UY7CB4_CVnErjg0P84XdP_m5vCuPvnodjUtmRm7Le5Dv9W78ZLUGoBwFwTVkA7sFwKoAg6yjErV7fMGILT_QsdkzIrpn0rIZE28h7Tzq9TxoiVvahZMpVytJ5BSUaKMd_NOHy2KYZBg2IRXuFJlW8vZg1toQoh4qfbhL_3uTjXoU8vzEdEIocUGYZLlAgmTLkt2NSfLW_36CXDfOuuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
خواسته‌تموم‌پسرای‌فوتبالی؛ روزی‌بخوان ازدواج کنند و بچه‌داربشن، بچشون‌حتماباید اینجوری باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25441" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25440">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZ8SEQwCVcGM7PodHtWvIgFVfbvOE2dgkvQiW19JOQG7aHQyz4BaKWe4ts7Yd68jt8q1yjm6WYR1iWlDWD_OMVnK7suu1LUwa_8EK44n1JLiAhEWFSWRtREy_-KbYwSMmd7RqFRPI_F3AbJAAPTxMlSZ2sRseqp2nddJTeUR7kC67Qr4JDArlHCcr3rs0joTifh34M3zpf72K1uUpEN323iYKr5yM4s4fWXAAdY7Zhvo4PHS_lJ4OiGPPRuJQQwZk_H-pelTERwSxPRi7UvHS4CrZb667kNli6kAIXgcKQ8pRmuEqwZLjayjDIIgQ_nJux6kn20Ij8SHy1A5-2YU0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHnUALi4-jJrlnSdnHc52meO6hAY88NbVyOCa5jo6Hq3pCXjrBsKm9X_JeJ3DcBWCZcU7DMSstfi7e5tjUoMcuRi7cBCqr2yO54m5YAmxTPqdxcfHSIBTY-4LV_TZlw_kAwK9gd4cSbhToG2IHwidnqmJthOmoZ9ecEbBc_9In0ODmBBCfCZfiMaASHyEBAhDWg5uOmZKuTwubGsu9KXpUKEKEfIizI9Kg6_VoIpIobV6moR9iRotgjUQD8gj_IHiFnOUMjuVni0OImdoSCG1whVGS5Cek2Le5AfUMxPwJvRdhe7idCLpm8-5S89MtWFT-D8IQNsajRYdyXXMu6tPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
گردنبند جالب‌ دوس‌دختر لامین‌یامال ستاره اسپانیایی بارسلونا که اسم او و شماره پیراهن‌ های این ستاره از ابتدا تاکنون هک شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25439" target="_blank">📅 15:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25438">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWGjmqTS8nXS-_2tiMh5KjZhxnRFXGXo540oq4wECD1U6M5sQDqWYKs8cpCFJaoVolVQkUoPXw0tZ_Lnr-stElNyxZ4wBlqOqFLldd_Fosih6Aq1uCeKr44PdlO23zCrufpilQaxGP4yizokIHc5c-sHEdwaLWnZOhZiBtqG65338RL6jYYkOLsFpUnPCB012yIzoURAGysPGECB1fftBFZz33muJ19N78MBPPH3VSFlXhonuNsSRE3ddxG-xj92qRoE_udoNdtOYbiUVszOR0QOjfgjca8lbCo6AnbIIc3x-mSatH7DHmM-r6GZTSaJeQcdujbErbIwAg37Qgqv2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌هوادارمکزیکی درصفحه‌اش افشاکرد در شب بازی پرتغال
🆚
اسپانیا؛ یکی از ستاره‌های پرتغال که درلیگ جزیزه بازی میکنه بهش پیشنهاد رابطه داده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25438" target="_blank">📅 15:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25437">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bR-x9vnThAnSeDpIMhwWfCK3yVod9Oy4aQV6_64tm_ReghR-jx227wB91atdZ6UxvGSflojrjsA5xUWkakrvSzJAnjvfQKLNvSVG_Ngvp9AfMMTfaYurLGgG1lEBSSTTnLwYdVAfLoauKdTNSYh4bUcl8Ss2WAiz48IvJ6bXfbl5mCBbU9RzzqvC_EuvL4Cu98-5Lknsr80GE7UD-ID_pP51VRSV44aDt0eqCippxI3E5-RyAmwldxa7AzEgfB3RtgmbJ3SgGqPvV0KQJc4NS5bY6naTIZ-yhiTNxs_3JEcd1YBOHKkiJOff6jRNo_W986bc-bh9CG880fQBL7Q3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
نشریه موندو
: باشگاه الهلال عربستان آماده ست که‌برای‌جذب رافینیا دیاز پیشنهادی 80 میلیون یورویی به بارسلونا بدهد و دستمزد فعلی رافینیا در بارسلونا رو در الهلال چهار برابر افزایش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25437" target="_blank">📅 15:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25435">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WZtJDcJ4KlvaCmMEJBYxQT8JgxNTvJSfvnFpE4JfQxkL9FFAL-sUaPJFwKy2z514J5SNoFJs1BtiCCgzECQPPC-YxJTgcfwDUNKmtRzTtud7JbIaQU6zKjs90xYU3-c4-TFlLFhg1I9QKx2JR3mw1O--RbhsstVfKE6ujQY0zY87I4VnDSXuSmyMQemII2O8JQs4h7WMvRLiktstMCa9wHYzH63_4l4t4vtfFwUjgi2gE6iTTbgl3SSCTrV98UDSQxa9mkFSa4SxUM1bpPLWts2UNSUIFrFxY3nMhBK-utwCgdeKGsWHpTR0So9KCZWiPbQBjzdYUIplrzqhk_S6IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QG7UgAvLoEIcigQzmWI-VW55x5VV1oCSDCPssEwL37yqA_eLPnAACa5Ouo-8-mM19khLO_hXTAlrse4Ny8VeGqu5owlUPlu0yZdbYmQC0GQAIJOuDfy5IqWiNIKfc9lHwDvnc94wvZyP_kntAXB4bv7R_9EShfluoGyGtxIzuZ6IY8x_OLUFEmL1kJvTzihqk7ppV9XbsiBfj8Cw1OPSYmCbzHSQmyhupASYNtBSjJtTmdVrkIWk2sNnDsrm4NG7T_dlWhcbaqi-M7RYWDq5ZCqbbdmO2YHZL_DkA-_wh6lqZRd4ah9hrElttw1NV5WVZNJI4LY632JjJG1UCe0Wsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
جالبه بدونید دوست دختر لامین یامال قبل شروع بازی امشب گفته‌بودکه اسپانیا دو بر یک تیم بلژیک رو میبره و راهی‌نیمه‌نهایی جام جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25435" target="_blank">📅 14:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25434">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=PIIcRbkmqtNGQkYNizuv88lxLWR8RzbdokyY-I7hxjpuhQEd4KBZjTKhbqa6nNRowpOMgASg2M6mTuJed5Z57Ntc1LVnu7zLeGsEXRUh_K3rmLcfviKLRY07AMf-fuTpCR9Q26h7BIuv8y5mHVU_raS9TFjC6CjYkFHKWy23akZDbGkcyVsyC4ny24OlMKdSok65llXva5PH29x1y7n7FSuFw8vTH8QJFSAjsSuuKCKEEX5ti21uqxlUyj-ekF8okWFuu3TEYNyJwJnLMseCXXV3tNpvzotPouJIEjYOXgZfNAGGJ7CWYhyvp2eBU-BS5I_1m8fKXVcc6uZyn4md2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=PIIcRbkmqtNGQkYNizuv88lxLWR8RzbdokyY-I7hxjpuhQEd4KBZjTKhbqa6nNRowpOMgASg2M6mTuJed5Z57Ntc1LVnu7zLeGsEXRUh_K3rmLcfviKLRY07AMf-fuTpCR9Q26h7BIuv8y5mHVU_raS9TFjC6CjYkFHKWy23akZDbGkcyVsyC4ny24OlMKdSok65llXva5PH29x1y7n7FSuFw8vTH8QJFSAjsSuuKCKEEX5ti21uqxlUyj-ekF8okWFuu3TEYNyJwJnLMseCXXV3tNpvzotPouJIEjYOXgZfNAGGJ7CWYhyvp2eBU-BS5I_1m8fKXVcc6uZyn4md2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
آندرس اسکوبار مدافع سابق‌تیم‌ملی کلمبیا بعد از این گل به‌خودی که درجام‌جهانی 1994 به خودشون زد توسط افراد ناشناس به ضرب 12 گلوله کشته شد و پس از 32 از این حادثه بسیار تلخ، قاتل وی در یک رستوران هدف‌گلوله قرارگرفت و براحتی کشته شد.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25434" target="_blank">📅 14:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25433">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svYsrcpmon1SAvHN8p0uF8reIaXN9DQQqa9ye_MulVGMk2Tzw8FYW-RvPsFO_fBGvW_keLnhSS2Xpwn_YOetAwB13lwYjcr9HLYR_AKy8T0Phth-mkk1W0JP6HzWAERQ70gtBGSBDjz7wy0kg2wZGnYza97eRz3YOuRK1FHGXGsAOlei_sxqPZ6Ya-eBKmL4pONSDCKmIxVBjNO6bNTFbZJA6WkWcz1-XFlwR7aa6PI3Gph5nTzUa5TRcLezPEaeCgJ3vDwEJypP4XUr4bsnCH1RdFWEeAjeEvxomfXdkYplI-vJuqWaYsH_vuxLc3FDiXJ-Gh_p4T8Yl9wyNKLcyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25433" target="_blank">📅 14:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25431">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5lY5NxDA6dCM3H-t1UoFoJ_aaG40itax9hBdF2xej6nR5RSQUNyuShNTo7SeuW8HVeLl6LdokTMzz1RdntNxVxhqqMjO5RVLUE-sAeX5VxlEwzEztqijpWny1h4gx3SMvHcHLAsP4rKtyr524xNiR5fluyNUPX8jweiaOezHwB57o9vVfRC2fHMdUhDaWLHvmQFnOTeVDFHODCFVgjcexpF8anjsi0fMy-jybJH23rd1fcEr4yuMQb74pVHhuOekfQklD9UxR7ppfCfj5vJTQj04ALe3OBCxTENFeWuGG5a6h2DPfRKeo2NHEo6alZ3_8VHWbpg9r8Ys7roQfN-xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25431" target="_blank">📅 14:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25430">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYF_nvnSWsMFISm-5e43R7ABZpMsHPQ6SLnmmBM7MUagkbZsD2ALRZPT7DgM0PXntzIs9WEHSFt9mPbN3MZQE7lpq_AQt0Q86IX50VBxbUq6_m81tK1l6Zrje9YlnpCmla7n8e-4dXEJNkxHAeungJ4N2NiQsXhknUZMGPhfWcfi1TWb6AXMUSOojove_YJ3xMcwoLnbDyX3BhGKGRgKVe3rZp6DDtP8yqY6aJcEbZUAIqj-GcKGoeUPc4tzWFgUKnWgs3T-MFG228Z0OTsyIBHnZ2l9de8l60XunYEtD8E3cN89uTouLscmTwOTg2FbktVYDbhyrkRmq4te7JzKbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛مدیرعامل باشگاه پرسپولیس قصد داره که ظرف روزهای آینده با امید عالیشاه کاپیتان 34 ساله سرخ پوشان جلسه برگزار کنه تا طرفین برای جدایی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25430" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
